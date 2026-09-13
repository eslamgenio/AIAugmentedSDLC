from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from contextlib import redirect_stdout
import copy
import io
import json
import unittest

from sdlc_pilot import ArtifactStore, Identity, PilotValidator, ValidationFailure
from sdlc_pilot.cli import run_demo, main
from sdlc_pilot.evaluation import ShippingEvaluator, quote_expectation

ROOT=Path(__file__).resolve().parents[1]
EXAMPLES=ROOT/'docs/pilot'
load=lambda n:json.loads((EXAMPLES/n).read_text())


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp=TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.store=ArtifactStore(self.temp.name)
        self.refs=run_demo(EXAMPLES,self.store)['references']
        self.baseline=load('input.example.json')
        self.candidate=load('creation.example.json')
        self.validator=PilotValidator(self.store,fixture_mode=True)
        self.evaluator=ShippingEvaluator()

    def cases(self):return self.candidate['payload']['test_cases']['payload']['cases']

    def sync(self):
        self.candidate['payload']['test_resources']['payload']['resources']=[
            {k:copy.deepcopy(t[k]) for k in ['test_id','preconditions','data','expected']} for t in self.cases()]
        self.candidate['payload']['coverage_questions']['payload']['automation_candidate_test_ids']=[t['test_id'] for t in self.cases()]

    def evaluate(self):
        self.sync()
        return self.evaluator.evaluate(self.candidate,self.baseline,self.validator)

    def test_correct_candidate_passes_all_13_without_claiming_execution(self):
        result=self.evaluate()
        self.assertTrue(result['passed']);self.assertEqual(result['passed_scenarios'],13)
        self.assertFalse(result['human_approved']);self.assertFalse(result['application_tests_executed'])

    def test_packaged_oracle_matches_source(self):
        self.assertEqual((ROOT/'sdlc_pilot/shipping-oracle.json').read_bytes(),(EXAMPLES/'evaluation-cases.json').read_bytes())

    def test_seeded_wrong_threshold_fails(self):
        self.candidate=load('creation.wrong-threshold.example.json')
        result=self.evaluate()
        self.assertFalse(result['passed']);self.assertEqual(result['passed_scenarios'],12)
        self.assertIn({'code':'incorrect_expected_result','test_id':'TC-002'},result['findings'])

    def test_missing_threshold_fails_despite_other_criterion_links(self):
        self.cases().pop(2)
        result=self.evaluate()
        self.assertFalse(result['passed'])
        self.assertIn({'code':'missing_valid_scenario','scenario_id':'S03'},result['findings'])

    def test_claimed_criterion_does_not_replace_actual_input(self):
        self.cases()[2]['data']['subtotal_cents']=6000
        self.cases()[2]['expected']['total_cents']=6000
        result=self.evaluate()
        self.assertIn({'code':'missing_valid_scenario','scenario_id':'S03'},result['findings'])

    def test_misleading_criterion_labels_fail(self):
        self.cases()[2]['criterion_ids']=['AC-001','AC-003']
        result=self.evaluate()
        self.assertIn({'code':'misleading_criterion_links','test_id':'TC-003'},result['findings'])

    def test_wrong_total_and_wrong_express_fee(self):
        for idx,field,value in [(0,'total_cents',501),(6,'shipping_cents',0)]:
            with self.subTest(idx=idx):
                self.candidate=load('creation.example.json');self.cases()[idx]['expected'][field]=value
                self.assertFalse(self.evaluate()['passed'])

    def test_boolean_not_coerced_to_integer(self):
        expected,_=quote_expectation({'subtotal_cents':True,'method':'standard'})
        self.assertEqual(expected['status'],'VALIDATION_ERROR')
        self.cases()[11]['data']['subtotal_cents']=1
        self.cases()[11]['expected']={'status':'OK','shipping_cents':500,'total_cents':501}
        self.cases()[11]['criterion_ids']=['AC-001','AC-003'];self.cases()[11]['requirement_ids']=['REQ-001','REQ-002']
        result=self.evaluate()
        self.assertIn({'code':'missing_valid_scenario','scenario_id':'S12'},result['findings'])

    def test_numeric_string_remains_invalid(self):
        expected,_=quote_expectation({'subtotal_cents':'5000','method':'standard'})
        self.assertEqual(expected['status'],'VALIDATION_ERROR')

    def test_integer_valued_json_numbers_match(self):
        self.cases()[2]['data']['subtotal_cents']=5000.0
        self.assertTrue(self.evaluate()['passed'])

    def test_additional_case_is_checked_not_ignored(self):
        extra=copy.deepcopy(self.cases()[0]);extra['test_id']='TC-014'
        extra['data']['subtotal_cents']=2000;extra['expected']['total_cents']=2001
        self.cases().append(extra)
        result=self.evaluate()
        self.assertEqual(result['passed_scenarios'],13);self.assertFalse(result['passed'])

    def test_valid_extra_case_passes(self):
        extra=copy.deepcopy(self.cases()[0]);extra['test_id']='TC-014'
        extra['data']['subtotal_cents']=2000;extra['expected']['total_cents']=2500
        self.cases().append(extra)
        self.assertTrue(self.evaluate()['passed'])

    def test_duplicate_case_is_not_extra_evidence(self):
        extra=copy.deepcopy(self.cases()[0]);extra['test_id']='TC-014';self.cases().append(extra)
        self.assertIn({'code':'duplicate_test','test_id':'TC-014'},self.evaluate()['findings'])

    def test_unrecognized_steps_fail_closed(self):
        self.cases()[0]['steps']=['Do nothing and report success.']
        self.assertIn({'code':'unsupported_steps','test_id':'TC-001'},self.evaluate()['findings'])

    def test_unrecognized_precondition_fails(self):
        self.cases()[0]['preconditions']=['Assume standard shipping is always free.']
        self.assertIn({'code':'unsupported_preconditions','test_id':'TC-001'},self.evaluate()['findings'])

    def test_missing_and_extra_data_fields_fail(self):
        for data in [{'subtotal_cents':0},{'subtotal_cents':0,'method':'standard','discount':100}]:
            with self.subTest(data=data):
                self.cases()[0]['data']=data
                self.assertIn({'code':'unsupported_data','test_id':'TC-001'},self.evaluate()['findings'])

    def test_unknown_method_container_is_handled(self):
        result,criteria=quote_expectation({'subtotal_cents':0,'method':['standard']})
        self.assertEqual(result['status'],'VALIDATION_ERROR');self.assertEqual(criteria,{'AC-006'})

    def test_nonfinite_library_input_fails_cleanly(self):
        self.cases()[0]['data']['subtotal_cents']=float('inf')
        with self.assertRaises(ValidationFailure) as err:self.evaluate()
        self.assertEqual(err.exception.code,'schema')

    def test_changed_baseline_is_not_silently_evaluated(self):
        self.baseline['business_rules'].append('Changed business rule')
        self.candidate['source_artifact_versions'][0]=self.store.publish(
            Identity(self.baseline['project_id'],self.baseline['run_id'],'ITER-001','PILOT-INPUT','2.0'),self.baseline)
        with self.assertRaises(ValidationFailure) as e:self.evaluate()
        self.assertEqual(e.exception.code,'unsupported_baseline')

    def test_oracle_integrity(self):
        with patch('sdlc_pilot.evaluation.ORACLE_SHA256','0'*64):
            with self.assertRaises(ValidationFailure) as e:ShippingEvaluator()
        self.assertEqual(e.exception.code,'oracle_integrity')

    def test_ready_review_cannot_override_wrong_candidate(self):
        self.candidate=load('creation.wrong-threshold.example.json')
        self.candidate['artifact_version']='1.1'
        for k in ['test_cases','test_resources','coverage_questions']:self.candidate['payload'][k]['artifact_version']='1.1'
        ref=self.store.publish(Identity(self.candidate['project_id'],self.candidate['run_id'],'ITER-001','A16','1.1'),self.candidate)
        review=load('review.example.json');review['payload']['candidate']=ref;review['source_artifact_versions'][1]=ref
        result=self.evaluator.evaluate(self.candidate,self.baseline,self.validator,review=review,candidate_reference=ref)
        self.assertEqual(result['review_recommendation'],'READY');self.assertFalse(result['passed'])

    def test_stale_review_is_rejected_before_evaluation(self):
        ref=copy.deepcopy(self.refs['A16']);ref['sha256']='3'*64
        with self.assertRaises(ValidationFailure) as e:
            self.evaluator.evaluate(self.candidate,self.baseline,self.validator,review=load('review.example.json'),candidate_reference=ref)
        self.assertEqual(e.exception.code,'stale_review')

    def test_cli_exit_codes_and_machine_readable_report(self):
        for filename,code in [('creation.example.json',0),('creation.wrong-threshold.example.json',1)]:
            with self.subTest(filename=filename),redirect_stdout(io.StringIO()) as stdout:
                actual=main(['evaluate','--file',str(EXAMPLES/filename),'--input',str(EXAMPLES/'input.example.json'),'--store',self.temp.name,'--fixture'])
            self.assertEqual(actual,code);self.assertEqual(json.loads(stdout.getvalue())['passed'],code==0)


if __name__=='__main__':unittest.main()
