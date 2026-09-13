import argparse
import json
from pathlib import Path
from .store import ArtifactStore, Identity, StoreError, parse_json
from .validation import PilotValidator, ValidationFailure
from .evaluation import ShippingEvaluator
from .agents import CodexProvider, AgentError, run_handoff


def read(path):
    return parse_json(Path(path).read_bytes())


def parser():
    p = argparse.ArgumentParser(description="Store, validate and run the bounded test-design pilot.")
    sub = p.add_subparsers(dest="command", required=True)
    demo = sub.add_parser("demo", help="Run synthetic artifact handoffs, without an LLM")
    demo.add_argument("--examples", type=Path, default=Path("docs/pilot"))
    demo.add_argument("--store", type=Path, required=True)
    v = sub.add_parser("validate", help="Validate an artifact against its profile and pinned context")
    v.add_argument("--file", required=True, type=Path)
    v.add_argument("--profile", required=True, choices=["pilotInput","creationBundle","reviewBundle","runRecord"])
    v.add_argument("--store", required=True, type=Path)
    v.add_argument("--input", type=Path)
    v.add_argument("--candidate-reference", type=Path)
    v.add_argument("--previous-review", type=Path)
    v.add_argument("--previous-candidate", type=Path)
    v.add_argument("--trusted-approval", type=Path, help="Trusted local record containing source_sha256 and approval; never take this from an agent")
    v.add_argument("--fixture", action="store_true")
    v.add_argument("--schema-only", action="store_true")
    e = sub.add_parser("evaluate",help="Check shipping test-specification correctness and coverage")
    e.add_argument("--file",type=Path,required=True)
    e.add_argument("--input",type=Path,required=True)
    e.add_argument("--store",type=Path,required=True)
    e.add_argument("--fixture",action="store_true")
    e.add_argument("--trusted-approval",type=Path)
    e.add_argument("--review",type=Path)
    e.add_argument("--candidate-reference",type=Path)
    e.add_argument("--previous-review",type=Path)
    e.add_argument("--previous-candidate",type=Path)
    h = sub.add_parser('handoff', help='Make two real model calls: creator then reviewer; no automatic approval')
    h.add_argument('--input', type=Path, required=True)
    h.add_argument('--store', type=Path, required=True)
    h.add_argument('--evidence', type=Path, required=True, help='New directory for model-call evidence')
    h.add_argument('--codex-executable', required=True, help='Native Codex executable; not a shell wrapper')
    h.add_argument('--model')
    h.add_argument('--timeout', type=int, default=240, help='Seconds per model call, 1-600')
    h.add_argument('--fixture', action='store_true')
    h.add_argument('--trusted-approval', type=Path)
    return p


def run_demo(examples, store):
    imported = {}
    for name,id,version in [("input.example.json","PILOT-INPUT","1.0"),("creation.example.json","A16","1.0"),("review.example.json","A17","1.0")]:
        raw = (examples/name).read_bytes()
        data = parse_json(raw)
        identity = Identity(data["project_id"],data["run_id"],data["iteration_id"],id,version)
        imported[id] = store.publish_bytes(identity,raw)
    baseline,candidate,review = (store.read(imported[id]) for id in ("PILOT-INPUT","A16","A17"))
    validator = PilotValidator(store,fixture_mode=True)
    validator.validate_review(review,candidate,baseline,imported["A16"])
    validator.validate_run(read(examples/'run.example.json'),baseline)
    return {"valid":True,"fixture_only":True,"checks":"schema, source digests and handoff semantics",
            "references":imported,"human_approved":False,"business_correctness_evaluated":False,
            "agents_executed":False,"note":"Synthetic upstream placeholders are permitted only in fixture mode."}


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        store = ArtifactStore(args.store)
        if args.command == "demo":
            result = run_demo(args.examples,store)
        else:
            trusted = {}
            if args.trusted_approval:
                record = read(args.trusted_approval)
                trusted[record['source_sha256']] = record['approval']
            validator = PilotValidator(store,fixture_mode=args.fixture,trusted_approvals=trusted)
            if args.command == 'handoff':
                provider = CodexProvider(args.codex_executable, model=args.model, timeout=args.timeout)
                result = run_handoff(read(args.input), store, validator, provider, args.evidence)
                print(json.dumps(result, indent=2))
                return 0 if result['state'] == 'AWAITING_APPROVAL' else 1
            document = read(args.file)
            if args.command == 'evaluate':
                result = ShippingEvaluator().evaluate(document,read(args.input),validator,
                    previous_review=read(args.previous_review) if args.previous_review else None,
                    previous_candidate=read(args.previous_candidate) if args.previous_candidate else None,
                    review=read(args.review) if args.review else None,
                    candidate_reference=read(args.candidate_reference) if args.candidate_reference else None)
                print(json.dumps(result,indent=2))
                return 0 if result['passed'] else 1
            if args.schema_only:
                validator.structural(document,args.profile)
            elif args.profile == 'pilotInput':
                validator.validate_input(document)
            else:
                if args.input is None:
                    raise ValidationFailure('context','--input is required for semantic validation')
                baseline = read(args.input)
                previous = {"previous_review":read(args.previous_review) if args.previous_review else None,
                            "previous_candidate":read(args.previous_candidate) if args.previous_candidate else None}
                if args.profile == 'creationBundle':
                    validator.validate_creation(document,baseline,**previous)
                elif args.profile == 'reviewBundle':
                    if args.candidate_reference is None:
                        raise ValidationFailure('context','--candidate-reference must independently select the current candidate')
                    reference = read(args.candidate_reference)
                    validator.validate_review(document,store.read(reference),baseline,reference,**previous)
                else:
                    validator.validate_run(document,baseline,**previous)
            result = {'valid':True,'profile':args.profile,'fixture_only':args.fixture,
                      'checks':'schema only' if args.schema_only else 'schema and handoff semantics',
                      'human_approved':False,'business_correctness_evaluated':False}
        print(json.dumps(result,indent=2))
        return 0
    except (StoreError,ValidationFailure,AgentError,OSError,KeyError) as exc:
        print(json.dumps({'valid':False,'code':getattr(exc,'code','store_or_input'),'message':str(exc)},indent=2))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
