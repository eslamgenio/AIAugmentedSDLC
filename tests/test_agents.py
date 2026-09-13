import copy
import hashlib
import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from sdlc_pilot import ArtifactStore, PilotValidator, ValidationFailure
from sdlc_pilot.agents import AgentError, CodexProvider, build_request, inspect_events, run_handoff
from sdlc_pilot.store import encode, parse_json

EXAMPLES = Path(__file__).resolve().parents[1] / 'docs/pilot'


def load(name):
    return parse_json((EXAMPLES / name).read_bytes())


class ScriptedProvider:
    live = False

    def __init__(self, wrong=False, invalid=False, fail_review=False):
        self.requests = []
        self.wrong, self.invalid, self.fail_review = wrong, invalid, fail_review

    def generate(self, request, evidence_dir):
        self.requests.append(copy.deepcopy(request))
        if request['role'] == 'create-test-cases':
            if self.invalid:
                return {'human_approved': True}, {'response_sha256': 'a' * 64}
            name = 'creation.wrong-threshold.example.json' if self.wrong else 'creation.example.json'
            payload = load(name)['payload']
            content = {'cases': payload['test_cases']['payload']['cases'],
                       **payload['coverage_questions']['payload']}
        else:
            if self.fail_review:
                raise AgentError('Injected reviewer interruption')
            payload = load('review.example.json')['payload']
            content = {k: payload[k]['payload'] for k in ('traceability', 'gaps', 'review')}
        return content, {'response_sha256': hashlib.sha256(encode(content)).hexdigest()}


class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = ArtifactStore(self.root / 'store')
        self.validator = PilotValidator(self.store, fixture_mode=True)
        self.baseline = load('input.example.json')
        self.evidence = self.root / 'evidence'

    def run_pair(self, provider):
        return run_handoff(self.baseline, self.store, self.validator, provider, self.evidence)

    def test_connected_pair_uses_stored_candidate_and_stops_before_approval(self):
        provider = ScriptedProvider()
        report = self.run_pair(provider)
        self.assertEqual(report['state'], 'AWAITING_APPROVAL')
        self.assertFalse(report['agents_executed']); self.assertFalse(report['human_approved'])
        self.assertFalse(report['application_tests_executed'])
        self.assertEqual(report['provider_calls_completed'], 2)
        candidate = self.store.read(report['references']['A16'])
        self.assertEqual(provider.requests[1]['context']['candidate'], candidate)
        review = self.store.read(report['references']['A17'])
        self.assertEqual(review['payload']['candidate'], report['references']['A16'])
        self.assertEqual(report, load_path(self.evidence / 'handoff-report.json'))

    def test_wrong_answer_cannot_pass_with_ready_review(self):
        report = self.run_pair(ScriptedProvider(wrong=True))
        self.assertEqual(report['review_recommendation'], 'READY')
        self.assertEqual(report['state'], 'NEEDS_CORRECTION')
        self.assertFalse(report['evaluation']['passed'])

    def test_schema_failure_stops_before_reviewer(self):
        provider = ScriptedProvider(invalid=True)
        with self.assertRaises(ValidationFailure): self.run_pair(provider)
        report = load_path(self.evidence / 'handoff-report.json')
        self.assertEqual(report['state'], 'FAILED')
        self.assertNotIn('A16', report['references'])
        self.assertEqual(len(provider.requests), 1)

    def test_reviewer_interruption_preserves_candidate_without_approval(self):
        with self.assertRaises(AgentError): self.run_pair(ScriptedProvider(fail_review=True))
        report = load_path(self.evidence / 'handoff-report.json')
        self.assertEqual(report['state'], 'FAILED')
        self.store.read(report['references']['A16'])
        self.assertNotIn('A17', report['references'])

    def test_existing_run_rejected_before_new_call(self):
        self.run_pair(ScriptedProvider())
        provider = ScriptedProvider()
        with self.assertRaises(ValidationFailure):
            run_handoff(self.baseline, self.store, self.validator, provider, self.root / 'another')
        self.assertEqual(provider.requests, [])

    def test_input_rejection_makes_no_model_call(self):
        self.baseline['approval']['baseline_version'] = '99.0'
        provider = ScriptedProvider()
        with self.assertRaises(ValidationFailure): self.run_pair(provider)
        self.assertEqual(provider.requests, [])

    def test_unsupported_profile_rejected_before_model_usage(self):
        self.baseline['business_rules'].append('A changed business rule.')
        provider = ScriptedProvider()
        with self.assertRaises(ValidationFailure): self.run_pair(provider)
        self.assertEqual(provider.requests, [])

    def test_requests_exclude_answers_oracle_and_approval_authority(self):
        request = build_request('create-test-cases', self.baseline, self.validator.schema)
        text = json.dumps(request)
        self.assertNotIn('mandatory_scenarios', text)
        self.assertNotIn('5499', text)
        self.assertNotIn('Synthetic example only', text)
        self.assertNotIn('approval', request['context'])
        self.assertNotIn('candidate', request['context'])
        self.assertNotIn('runRecord', request['content_schema']['$defs'])


def load_path(path):
    return parse_json(path.read_bytes())


class ProviderTests(unittest.TestCase):
    def test_incomplete_and_tool_streams_rejected(self):
        for events in ([{'type': 'turn.started'}],
                       [{'type': 'turn.failed'}],
                       [{'type': 'item.completed', 'item': {'type': 'command_execution'}},
                        {'type': 'turn.completed', 'usage': {}}]):
            with self.assertRaises(AgentError):
                inspect_events(b'\n'.join(json.dumps(e).encode('utf-8') for e in events))

    def test_completed_stream_returns_usage(self):
        self.assertEqual(inspect_events(b'{"type":"turn.completed","usage":{"input_tokens":12}}'),
                         {'input_tokens': 12})

    @patch('sdlc_pilot.agents.shutil.which', return_value='codex.exe')
    def test_timeout_stops_without_retry(self, _):
        with TemporaryDirectory() as directory:
            provider = CodexProvider('codex.exe', timeout=1)
            with patch('sdlc_pilot.agents.subprocess.run', side_effect=subprocess.TimeoutExpired('codex', 1)) as run:
                with self.assertRaises(AgentError):
                    provider.generate({'instructions': 'test'}, Path(directory) / 'call')
                self.assertEqual(run.call_count, 1)
                args = run.call_args.args[0]
                self.assertIn('read-only', args)
                self.assertIn('features.shell_tool=false', args)
                self.assertNotIn('--dangerously-bypass-approvals-and-sandbox', args)

    @patch('sdlc_pilot.agents.shutil.which', return_value='codex.exe')
    def test_transport_parses_structured_result_and_records_hash(self, _):
        def complete(command, **kwargs):
            output = Path(command[command.index('--output-last-message') + 1])
            output.write_bytes(encode({'payload_json': '{"cases": []}'}))
            kwargs['stdout'].write(b'{"type":"turn.completed","usage":{"output_tokens":5}}\n')
            return subprocess.CompletedProcess(command, 0)
        with TemporaryDirectory() as directory, patch('sdlc_pilot.agents.subprocess.run', side_effect=complete):
            content, metadata = CodexProvider('codex.exe').generate({'instructions': 'test'}, Path(directory) / 'call')
            self.assertEqual(content, {'cases': []})
            self.assertEqual(metadata['usage']['output_tokens'], 5)
            self.assertEqual(len(metadata['response_sha256']), 64)


if __name__ == '__main__':
    unittest.main()
