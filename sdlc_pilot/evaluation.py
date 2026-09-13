"""Deterministic shipping test-specification evaluation, never application execution."""

from importlib.resources import files
import hashlib
import json
import math
from .validation import require, same

PROFILE_FIELDS = ('baseline_id','baseline_version','requirements','acceptance_criteria',
                  'design_rules','business_rules','risks','test_scope','coverage_rules','test_template_fields')
PROFILE_SHA256 = '285e1dbc8dd6882b2d881bd6dd816600de0656796ee1c8e6e4c910989a4dac82'
ORACLE_SHA256 = '6f407daf0caba8b84e5316b1e32981fb6a48c2b64d2e60e73dd8d8e5249bfdeb'
STEPS = [
    'Submit the specified subtotal_cents and method to the shipping quote interface.',
    'Compare every returned field with the expected result.',
]
PRECONDITIONS = ['Shipping quote behavior uses SHIPPING-BASELINE version 1.0.']


def normalize_text(value):
    return ' '.join(value.split()).casefold()


def data_key(data):
    # Preserve booleans and strings as distinct types. JSON integer-valued
    # numbers such as 5000.0 have the same business meaning as 5000.
    result = dict(data)
    value = result.get('subtotal_cents')
    if type(value) is float and math.isfinite(value) and value.is_integer():
        result['subtotal_cents'] = int(value)
    return json.dumps(result,sort_keys=True,separators=(',',':'),allow_nan=False)


def quote_expectation(data):
    """Independent reference rule for this fixed pilot profile only."""
    subtotal, method = data['subtotal_cents'], data['method']
    valid_amount = (type(subtotal) is int or
                    (type(subtotal) is float and math.isfinite(subtotal) and subtotal.is_integer())) and subtotal >= 0
    valid_method = type(method) is str and method in ('standard','express')
    if not valid_amount or not valid_method:
        criteria = ([] if valid_amount else ['AC-002']) + ([] if valid_method else ['AC-006'])
        return {'status':'VALIDATION_ERROR','shipping_cents':None,'total_cents':None},set(criteria)
    subtotal = int(subtotal)
    fee = 1200 if method == 'express' else (500 if subtotal < 5000 else 0)
    criterion = 'AC-005' if method == 'express' else ('AC-003' if subtotal < 5000 else 'AC-004')
    return {'status':'OK','shipping_cents':fee,'total_cents':subtotal+fee},{'AC-001',criterion}


class ShippingEvaluator:
    def __init__(self):
        raw = files('sdlc_pilot').joinpath('shipping-oracle.json').read_bytes()
        require(hashlib.sha256(raw).hexdigest() == ORACLE_SHA256,'oracle_integrity',
                'Packaged shipping oracle differs from its pinned version')
        self.oracle = json.loads(raw)
        for scenario in self.oracle['mandatory_scenarios']:
            expected,criteria = quote_expectation(scenario['input'])
            require(same(expected,scenario['expected']) and criteria == set(scenario['criterion_ids']),
                    'oracle_integrity','Oracle disagrees with independent shipping rules')

    def validate_baseline(self, baseline):
        profile = json.dumps({k:baseline[k] for k in PROFILE_FIELDS},sort_keys=True,separators=(',',':')).encode()
        require(hashlib.sha256(profile).hexdigest() == PROFILE_SHA256,'unsupported_baseline',
                'This evaluator supports only the pinned shipping baseline; a changed specification requires a new evaluator profile')

    def evaluate(self,candidate,baseline,validator,*,previous_review=None,previous_candidate=None,
                 review=None,candidate_reference=None):
        validator.validate_creation(candidate,baseline,previous_review=previous_review,previous_candidate=previous_candidate)
        self.validate_baseline(baseline)
        recommendation = None
        require((review is None) == (candidate_reference is None),'context',
                'Supply both the review and the independently selected candidate reference, or neither')
        if review is not None:
            recommendation = validator.validate_review(review,candidate,baseline,candidate_reference,
                                                       previous_review=previous_review,previous_candidate=previous_candidate)
        cases = candidate['payload']['test_cases']['payload']['cases']
        findings = []
        valid_cases = {}
        for test in cases:
            errors = []
            data = test['data']
            if set(data) != {'subtotal_cents','method'}:
                errors.append('unsupported_data')
            if [normalize_text(s) for s in test['steps']] != [normalize_text(s) for s in STEPS]:
                errors.append('unsupported_steps')
            if [normalize_text(s) for s in test['preconditions']] != [normalize_text(s) for s in PRECONDITIONS]:
                errors.append('unsupported_preconditions')
            if 'unsupported_data' not in errors:
                expected,criteria = quote_expectation(data)
                if not same(test['expected'],expected):
                    errors.append('incorrect_expected_result')
                if set(test['criterion_ids']) != criteria:
                    errors.append('misleading_criterion_links')
            for code in errors:
                findings.append({'code':code,'test_id':test['test_id']})
            if not errors:
                key = data_key(data)
                if key in valid_cases:
                    findings.append({'code':'duplicate_test','test_id':test['test_id']})
                valid_cases.setdefault(key,[]).append(test['test_id'])
        scenarios = []
        for scenario in self.oracle['mandatory_scenarios']:
            matches = valid_cases.get(data_key(scenario['input']),[])
            scenarios.append({'scenario_id':scenario['scenario_id'],'passed':bool(matches),'test_ids':matches})
            if not matches:
                findings.append({'code':'missing_valid_scenario','scenario_id':scenario['scenario_id']})
        questions = candidate['payload']['coverage_questions']['payload']['questions']
        if any(q['blocking'] and q['status']=='OPEN' for q in questions):
            findings.append({'code':'blocking_question'})
        if recommendation is not None and recommendation != 'READY':
            findings.append({'code':'review_not_ready','recommendation':recommendation})
        return {
            'passed':not findings,'evaluation_profile':'shipping-1.0','fixture_only':validator.fixture_mode,
            'mandatory_scenarios':len(scenarios),'passed_scenarios':sum(s['passed'] for s in scenarios),
            'tested_case_count':len(cases),'scenarios':scenarios,'findings':findings,
            'review_recommendation':recommendation,'business_correctness_evaluated':True,
            'application_tests_executed':False,'human_approved':False,
            'scope':'Expected results and coverage of declared shipping test specifications, with an exact supported step template.'
        }
