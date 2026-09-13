from pathlib import Path
from tempfile import TemporaryDirectory
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import patch
import copy
import json
import os
import unittest

from sdlc_pilot import ArtifactStore,Identity,StoreError,PilotValidator,ValidationFailure
from sdlc_pilot.store import parse_json,encode
from sdlc_pilot.cli import run_demo,main
from sdlc_pilot.validation import SOURCE_FIELDS

ROOT=Path(__file__).resolve().parents[1]
EXAMPLES=ROOT/'docs/pilot'
load=lambda name:parse_json((EXAMPLES/name).read_bytes())


class PilotTests(unittest.TestCase):
    def setUp(self):
        self.temp=TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.store=ArtifactStore(self.temp.name)
        self.refs=run_demo(EXAMPLES,self.store)['references']
        self.baseline=load('input.example.json')
        self.candidate=load('creation.example.json')
        self.review=load('review.example.json')
        self.v=PilotValidator(self.store,fixture_mode=True)

    def invalid(self,code,fn):
        with self.assertRaises(ValidationFailure) as err:fn()
        self.assertEqual(err.exception.code,code)

    def review_check(self):
        return self.v.validate_review(self.review,self.candidate,self.baseline,self.refs['A16'])

    def test_valid_demo_is_repeatable_and_not_approval(self):
        result=run_demo(EXAMPLES,self.store)
        self.assertTrue(result['valid']);self.assertFalse(result['human_approved'])
        self.assertFalse(result['business_correctness_evaluated'])
        self.assertEqual(result['references'],self.refs)

    def test_packaged_schema_matches_documented_contract(self):
        self.assertEqual((ROOT/'sdlc_pilot/contracts.schema.json').read_bytes(),(EXAMPLES/'contracts.schema.json').read_bytes())

    def test_unknown_field_and_invalid_timestamp(self):
        self.candidate['unexpected']=True
        self.invalid('schema',lambda:self.v.structural(self.candidate,'creationBundle'))
        del self.candidate['unexpected'];self.candidate['created_at']='yesterday'
        self.invalid('schema',lambda:self.v.structural(self.candidate,'creationBundle'))

    def test_fixture_is_rejected_by_default(self):
        self.invalid('fixture_boundary',lambda:PilotValidator(self.store).validate_input(self.baseline))

    def test_fixture_mode_rejects_live_documents(self):
        self.baseline['synthetic_fixture']=False
        self.invalid('fixture_boundary',lambda:self.v.validate_input(self.baseline))

    def test_approval_scope(self):
        self.baseline['approval']['baseline_version']='2.0'
        self.invalid('approval_scope',lambda:self.v.validate_input(self.baseline))

    def test_duplicate_source_id_and_wrong_source_set(self):
        self.baseline['sources'][0]=self.baseline['sources'][1]
        self.invalid('duplicate_id',lambda:self.v.validate_input(self.baseline))
        self.baseline=load('input.example.json');self.baseline['sources'][0]['artifact_id']='UNKNOWN'
        self.invalid('source_set',lambda:self.v.validate_input(self.baseline))

    def test_duplicate_test_and_unknown_criterion(self):
        cases=self.candidate['payload']['test_cases']['payload']['cases']
        cases[1]['test_id']=cases[0]['test_id']
        self.invalid('duplicate_id',lambda:self.v.validate_creation(self.candidate,self.baseline))
        cases[1]['test_id']='TC-002';cases[0]['criterion_ids']=['UNKNOWN']
        self.invalid('unknown_id',lambda:self.v.validate_creation(self.candidate,self.baseline))

    def test_resource_disagreement(self):
        self.candidate['payload']['test_resources']['payload']['resources'][0]['expected']['total_cents']=999
        self.invalid('resources',lambda:self.v.validate_creation(self.candidate,self.baseline))

    def test_missing_criterion_in_review(self):
        self.review['payload']['traceability']['payload']['coverage'].pop()
        self.invalid('coverage',self.review_check)

    def test_stale_review(self):
        self.review['payload']['candidate']['sha256']='1'*64
        self.invalid('stale_review',self.review_check)

    def test_forged_matrix_link(self):
        self.review['payload']['traceability']['payload']['coverage'][0]['test_ids']=['TC-008']
        self.invalid('traceability',self.review_check)

    def test_gap_and_ready_rejected(self):
        row=self.review['payload']['traceability']['payload']['coverage'][0]
        row.update(test_ids=[],status='GAP')
        self.review['payload']['gaps']['payload']['gap_criterion_ids']=[row['criterion_id']]
        self.invalid('not_ready',self.review_check)

    def test_wrong_expected_value_is_not_claimed_as_business_validation(self):
        bad=load('creation.wrong-threshold.example.json')
        # Step 1 validates contracts. Step 2's evaluator must reject this result.
        self.v.validate_creation(bad,self.baseline)
        self.assertEqual(bad['payload']['test_cases']['payload']['cases'][1]['expected']['shipping_cents'],0)

    def test_stale_baseline_content(self):
        changed=copy.deepcopy(self.baseline);changed['business_rules'].append('New unpinned rule')
        self.invalid('stale_baseline',lambda:self.v.validate_creation(self.candidate,changed))

    def test_unknown_automation_candidate(self):
        self.candidate['payload']['coverage_questions']['payload']['automation_candidate_test_ids'].append('UNKNOWN')
        self.invalid('unknown_id',lambda:self.v.validate_creation(self.candidate,self.baseline))

    def test_revision_without_context(self):
        self.candidate['payload']['revision_actions']=[{'finding_id':'F1','action':'Fixed','affected_test_ids':['TC-001']}]
        self.invalid('revision_context',lambda:self.v.validate_creation(self.candidate,self.baseline))

    def test_child_version_and_name(self):
        self.candidate['payload']['test_cases']['artifact_version']='2.0'
        self.invalid('child_version',lambda:self.v.validate_creation(self.candidate,self.baseline))
        self.candidate['payload']['test_cases']['artifact_version']='1.0'
        self.candidate['payload']['test_cases']['canonical_name']='Renamed'
        self.invalid('schema',lambda:self.v.validate_creation(self.candidate,self.baseline))

    def test_run_cannot_claim_completion_without_approval(self):
        run=load('run.example.json');run['state']='COMPLETED';run['events'][-1]['to_state']='COMPLETED'
        self.invalid('approval',lambda:self.v.validate_run(run,self.baseline))

    def test_run_limits_and_event_history(self):
        run=load('run.example.json');run['usage']['requests']=13
        self.invalid('budget',lambda:self.v.validate_run(run,self.baseline))
        run=load('run.example.json');run['events'][-1]['to_state']='CREATING'
        self.invalid('events',lambda:self.v.validate_run(run,self.baseline))

    def test_store_rejects_overwrite(self):
        identity=Identity.from_reference(self.refs['A16'])
        self.candidate['evidence_refs'].append('changed')
        with self.assertRaises(StoreError):self.store.publish(identity,self.candidate)

    def test_digest_corruption_and_wrong_schema_version(self):
        reference=copy.deepcopy(self.refs['A16']);reference['schema_version']='2.0'
        with self.assertRaises(StoreError):self.store.read(reference)
        path=self.store.path_for(Identity.from_reference(self.refs['A16']))
        path.write_bytes(path.read_bytes()+b' ')
        with self.assertRaises(StoreError):self.store.read(self.refs['A16'])

    def test_traversal_identity_rejected(self):
        for text in ['../escape','C:\\outside','run/name','..']:
            with self.subTest(text=text),self.assertRaises(StoreError):Identity('project',text,'ITER-001','A16','1.0')

    def test_strict_json(self):
        for raw in [b'{"x":1,"x":2}',b'{"x":NaN}',b'{"x":1e999}',b'[]',b'{broken',b'\xff']:
            with self.subTest(raw=raw),self.assertRaises(StoreError):parse_json(raw)

    def test_concurrent_same_publication_is_idempotent(self):
        identity=Identity('p','r','ITER-001','A16','2.0')
        data={'schema_version':'1.0','value':1}
        with ThreadPoolExecutor(max_workers=4) as pool:
            refs=list(pool.map(lambda _:self.store.publish(identity,data),range(8)))
        self.assertTrue(all(r==refs[0] for r in refs))

    def test_concurrent_different_publication_does_not_overwrite(self):
        identity=Identity('p','r','ITER-001','A16','2.0')
        def publish(v):
            try:return self.store.publish(identity,{'schema_version':'1.0','value':v})
            except StoreError:return None
        with ThreadPoolExecutor(max_workers=2) as pool:refs=list(pool.map(publish,[1,2]))
        self.assertEqual(sum(r is not None for r in refs),1)

    def test_failure_before_publish_keeps_final_absent(self):
        identity=Identity('p','r','ITER-001','A16','2.0')
        with patch.object(self.store,'_publish_no_replace',side_effect=OSError('interrupt')):
            with self.assertRaises(OSError):self.store.publish(identity,{'schema_version':'1.0'})
        self.assertFalse(self.store.path_for(identity).exists())
        self.assertFalse(list(Path(self.temp.name).rglob('.pending-*')))

    def test_failure_after_publish_can_be_reconciled_without_index(self):
        identity=Identity('p','r','ITER-001','A16','2.0');data={'schema_version':'1.0'}
        original=self.store._publish_no_replace
        def interrupt(temp,path,raw):original(temp,path,raw);raise OSError('interrupt after publish')
        with patch.object(self.store,'_publish_no_replace',side_effect=interrupt):
            with self.assertRaises(OSError):self.store.publish(identity,data)
        restarted=ArtifactStore(self.temp.name)
        reference=restarted.publish(identity,data)
        self.assertEqual(restarted.read(reference),data)

    def publish_bundle(self,bundle):
        return self.store.publish(Identity(bundle['project_id'],bundle['run_id'],bundle['iteration_id'],bundle['artifact_id'],bundle['artifact_version']),bundle)

    def test_live_input_requires_resolved_sources_and_independent_approval(self):
        baseline=copy.deepcopy(self.baseline);baseline['synthetic_fixture']=False
        baseline['approval']['actor']='configured-owner'
        baseline['sources']=[]
        for id,fields in SOURCE_FIELDS.items():
            doc={'schema_version':'1.0','synthetic_fixture':False,'payload':{k:baseline[k] for k in fields}}
            baseline['sources'].append(self.store.publish(Identity(baseline['project_id'],'REAL-SOURCE-TEST',baseline['iteration_id'],id,'1.0'),doc))
        validator=PilotValidator(self.store)
        self.invalid('untrusted_approval',lambda:validator.validate_input(baseline))
        digest=next(r['sha256'] for r in baseline['sources'] if r['artifact_id']=='E09')
        validator=PilotValidator(self.store,trusted_approvals={digest:baseline['approval']})
        validator.validate_input(baseline)
        baseline['business_rules']=['Unsubstantiated replacement rule']
        self.invalid('source_content',lambda:validator.validate_input(baseline))

    def test_nonzero_missing_fixture_source_is_not_bypassed(self):
        self.baseline['sources'][0]['sha256']='2'*64
        self.invalid('source_integrity',lambda:self.v.validate_input(self.baseline))

    def test_evidence_pointer_and_open_finding(self):
        finding={'finding_id':'F1','severity':'BLOCKING','criterion_ids':['AC-001'],'test_ids':['TC-001'],
                 'description':'Example finding','requested_action':'Clarify setup','status':'OPEN',
                 'evidence':{'artifact_id':'A16','artifact_version':'1.0','location':'/missing'}}
        self.review['payload']['review']['payload']['findings']=[finding]
        self.invalid('evidence',self.review_check)
        finding['evidence']['location']='/payload/test_cases/payload/cases/0'
        self.invalid('not_ready',self.review_check)
        self.review['payload']['review']['payload']['recommendation']='REVISE'
        self.assertEqual(self.review_check(),'REVISE')

    def test_ready_rejects_blocking_question(self):
        self.candidate['payload']['coverage_questions']['payload']['questions']=[{
            'question_id':'Q1','text':'Unspecified expected behavior','blocking':True,
            'owner':'test-owner','status':'OPEN','resolution':None}]
        self.candidate['artifact_version']='1.1'
        for k in ['test_cases','test_resources','coverage_questions']:self.candidate['payload'][k]['artifact_version']='1.1'
        ref=self.publish_bundle(self.candidate)
        self.review['payload']['candidate']=ref
        self.review['source_artifact_versions'][1]=ref
        self.invalid('not_ready',lambda:self.v.validate_review(self.review,self.candidate,self.baseline,ref))

    def test_full_revision_handoff_and_missing_reviewer_check(self):
        prior=copy.deepcopy(self.review);prior['artifact_version']='1.1'
        for k in ['traceability','gaps','review']:prior['payload'][k]['artifact_version']='1.1'
        prior['payload']['review']['payload'].update(recommendation='REVISE',findings=[{
            'finding_id':'F1','severity':'NONBLOCKING','criterion_ids':['AC-001'],'test_ids':['TC-001'],
            'description':'Clarify the interface step','requested_action':'Specify the operation name','status':'OPEN',
            'evidence':{'artifact_id':'A16','artifact_version':'1.0','location':'/payload/test_cases/payload/cases/0/steps'}}])
        old_review_ref=self.publish_bundle(prior)
        revised=copy.deepcopy(self.candidate);revised['artifact_version']='1.1'
        for k in ['test_cases','test_resources','coverage_questions']:revised['payload'][k]['artifact_version']='1.1'
        revised['source_artifact_versions'] += [self.refs['A16'],old_review_ref]
        revised['payload']['revision_actions']=[{'finding_id':'F1','action':'Named the shipping quote operation','affected_test_ids':['TC-001']}]
        revised['payload']['test_cases']['payload']['cases'][0]['steps'][0]='Call the shipping quote operation with the specified data.'
        candidate_ref=self.publish_bundle(revised)
        new_review=copy.deepcopy(self.review);new_review['artifact_version']='1.2'
        for k in ['traceability','gaps','review']:new_review['payload'][k]['artifact_version']='1.2'
        new_review['payload']['candidate']=candidate_ref;new_review['source_artifact_versions'][1]=candidate_ref
        new_review['payload']['review']['payload']['previous_finding_checks']=[{'finding_id':'F1','verified_resolved':True,'reason':'Operation is now identified in the first step.'}]
        check=lambda:self.v.validate_review(new_review,revised,self.baseline,candidate_ref,previous_review=prior,previous_candidate=self.candidate)
        self.assertEqual(check(),'READY')
        new_review['payload']['review']['payload']['previous_finding_checks']=[]
        self.invalid('revision_actions',check)

    def test_symlink_escape_is_rejected(self):
        identity=Identity('p','escape','ITER-001','A16','1.0')
        path=self.store.path_for(identity)
        with TemporaryDirectory() as outside:
            try:
                path.parent.symlink_to(outside,target_is_directory=True)
            except OSError:
                self.skipTest('Creating directory symlinks is not permitted in this environment')
            with self.assertRaises(StoreError):self.store.publish(identity,{'schema_version':'1.0'})


if __name__=='__main__':unittest.main()
