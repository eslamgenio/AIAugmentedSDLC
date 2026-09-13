# Shipping correctness evaluator

The evaluator checks the declared test specifications for the pinned shipping baseline. It does not execute a shipping application or replace human approval. It combines the existing schema/handoff validators with deterministic expected-result and coverage checks.

## Run it

Use the Python environment described in [the setup guide](IMPLEMENTATION.md). From the project root, first import the synthetic dependencies:

```powershell
.\.venv\Scripts\python.exe -m sdlc_pilot demo --store outputs/pilot-demo
.\.venv\Scripts\python.exe -m sdlc_pilot evaluate --file docs/pilot/creation.example.json --input docs/pilot/input.example.json --store outputs/pilot-demo --fixture
```

The correct fixture passes all 13 mandatory scenarios. The following negative example must return exit code 1 and identify TC-002's incorrect expected result plus the missing valid S02 scenario:

```powershell
.\.venv\Scripts\python.exe -m sdlc_pilot evaluate --file docs/pilot/creation.wrong-threshold.example.json --input docs/pilot/input.example.json --store outputs/pilot-demo --fixture
```

`evaluate` returns JSON with `passed`, scenario counts, matched test IDs and findings. It returns exit code 0 only when all checks pass. A schema, source or profile error returns the existing structured error response and exit code 1. The existing `validate` command remains a contract/consistency check and does not imply correctness evaluation.

Optionally supply both `--review FILE` and `--candidate-reference FILE`. The latter is a source-reference JSON object independently selected by the caller, not inferred from the review. Review consistency must pass and its recommendation must be READY. A READY review cannot override a failed correctness check. Revision context can be supplied through `--previous-review` and `--previous-candidate`.

## What is checked

- The baseline's requirements, criteria, design, scope, risks and coverage rules match the pinned profile. Changing the requirements requires a new reviewed evaluator profile, rather than silently retaining an old oracle.
- The evaluator-only scenario file matches its pinned digest and agrees with an independent implementation of the shipping rules.
- All supplied cases, including extra cases beyond the mandatory 13, have the correct status, shipping fee and total. Extra incorrect cases fail the evaluation even if all mandatory scenarios are covered.
- Coverage is matched by actual input values and valid expected outcomes, not test names, counts, scenario labels or claimed criterion links.
- Required criterion links agree with the exercised behavior. Exact duplicate cases do not count as new evidence and cause failure.
- Standard shipping is checked below, at and above the 5000-cent threshold. Express shipping retains its fee. Null, strings, booleans, negative and fractional amounts are not coerced to valid subtotals.
- Integer-valued JSON numbers such as 5000.0 have the same numerical meaning as 5000. Strings and booleans remain distinct. Expected money fields use canonical integer-cent values.
- Missing data keys, extra data keys, unresolved blocking questions and unsupported step/precondition wording fail evaluation.

## Supported test description profile

The current pilot deliberately uses a narrow, recognizable test template. Preconditions must be:

```text
Shipping quote behavior uses SHIPPING-BASELINE version 1.0.
```

The two steps must be:

```text
Submit the specified subtotal_cents and method to the shipping quote interface.
Compare every returned field with the expected result.
```

Whitespace and letter case are normalized. Other wording returns `unsupported_steps` or `unsupported_preconditions`; it is not silently judged equivalent. This prevents meaningless actions from passing because their adjacent data and expected-result fields look correct. The creator adapter requests the supported template. Supporting arbitrary natural-language steps requires a separate reviewed approach.

The evaluator proves consistency with this declared template, not that anyone executed its steps. Its output always reports `application_tests_executed: false` and `human_approved: false`. A passing result can support a future approval request, but cannot complete or release a project.

## Oracle maintenance and separation

`docs/pilot/evaluation-cases.json` is the readable scenario source; `sdlc_pilot/shipping-oracle.json` is the packaged copy. A test checks that they match. The evaluator pins the oracle digest and baseline fingerprint. Update those deliberately alongside tests when creating a new baseline profile. Do not accept a replacement oracle from the creator or reviewer.

The oracle stays outside agent prompts. The evaluator itself makes no model call; [the adapters](AGENT-HANDOFF.md) invoke the creator and reviewer before evaluation. Their local CLI boundary is not an adversarial confidentiality guarantee. The test suite includes correct and deliberately incorrect candidates, omitted threshold cases, misleading labels, changed baselines, stale reviews, extra cases and a READY review attached to an incorrect candidate.

Coverage currently requires exact scenario inputs. For example, a correct negative case using subtotal `4999.5` does not satisfy the fixed scenario using `1.5`, although both exercise a fractional subtotal. A missing scenario finding therefore means the specified evaluation input was absent, not necessarily that the entire behavioral category was untested. The [first real handoff](LIVE-HANDOFF-001.md) exposed this limitation. Aligning behavioral coverage rules and evaluator matching is needed before treating this gate as a general measure of test-design quality.

The [creator and reviewer adapters](AGENT-HANDOFF.md) now run their outputs through both validation and evaluation. Next: connect bounded corrections and approval through the durable controller.
