# Sample artifacts for skill testing

`ITER-001/` now contains a filled example for **every artifact template: A01–A45 and E01–E10**, plus requirements and small native component assets. These are sample inputs for testing skills at different points in the SDLC, not a completed production lifecycle. The artifact documents use normal names and statuses.

## Scenario and evidence

The feature monitors an IoT device, changes it to OFFLINE after three misses and emits one notification per incident. A heartbeat restores ONLINE and permits a notification for a later incident.

- A16 v1.0 deliberately contains only three single-device cases. A17 identifies missing AC-012/013 coverage as F-001. Preserve this gap when testing review and revision skills.
- SRC-001 / B001 fails TC-003 because notification eligibility is not reset after recovery. DEF-001 and CR-001 describe this problem.
- SRC-002 / B002 corrects that defect. Recorded local checks pass all three existing cases, but the independence coverage gap remains.
- A23 records blocked integration; A25 does not claim hosted CI. B001/B002 are local source packages. A26 describes local testing, not a managed deployment.
- RC-002 refers to B002. Test exit and release readiness remain NOT READY; A41 has no approval and A42 records no production deployment.
- A43/A44 use a separate product feedback record. They do not imply that RC-002 was deployed. DRAFT-REQ-005 is a future ITER-002 proposal, not a change to the current requirements.

The [native assets guide](ITER-001/native/README.md) explains the source snapshots, local runner, recorded results and package hashes. Existing requirements/supporting inputs retain their earlier snapshot statements; later artifacts add engineering evidence without pretending it existed at the earlier stage. E09 remains PENDING.

## Self-contained test-creation inputs

Use **A04, A05, A06, A09, A15, E01, E06 and E09 at v1.1** for a fresh creation test. A05-02 contains all four requirements and thirteen acceptance criteria, including the context and exclusions. These eight files have no dependency on a separately named requirements document. Keep the creator skill and A16 template alongside them.

```text
Use $create-test-cases with AIAugmentation/dummy/ITER-001/A05_requirements-review-outputs_ITER-001_v1.1.md.
```

Earlier v1.0 inputs are preserved. The prepared A16/A17 v1.0 snapshots still record their historical sources; the baseline behavior and IDs are unchanged, so identify A05 v1.1 explicitly when using it for a new review. A05's artifact version changed to 1.1 while its baseline behavior version remains 1.0.

## Test a skill

1. Select the skill and its output in the index below. Read the catalog's **Skill Artifact Flow** and **Artifact Handoff Mapping** for its inputs and conditional paths.
2. Supply only the relevant upstream artifacts. Keep the prepared output out of the skill's inputs when evaluating a fresh result. For revision/re-review, explicitly include the prior candidate and findings.
3. Ask for outputs under `AIAugmentation/dummy/runs/<skill-name>/ITER-001/` so the reference files remain unchanged. Increment versions for revisions and link the exact input versions.
4. Compare the generated artifact with its template and evidence. Check reasoning and traceability, not identical wording. Passing three cases must not become full coverage or release approval.

The pack supplies useful drafting, failure, correction and blocked-gate cases. It does not provide successful real deployments, external account access, every branch of every skill, or a complete approved workflow. For execution skills, these files support input assessment, planning and recording the supplied runs; a real execution still needs the appropriate environment and authorization. The local runner in `ITER-001/native/` is the only executable target in the pack.

Example prompts:

```text
Use $plan-testing with AIAugmentation/dummy/ITER-001/A05_requirements-review-outputs_ITER-001_v1.1.md. Save the plan under AIAugmentation/dummy/runs/plan-testing/ITER-001/. Do not read the prepared A15.

Use $review-test-coverage with AIAugmentation/dummy/ITER-001/A05_requirements-review-outputs_ITER-001_v1.1.md and AIAugmentation/dummy/ITER-001/A16_test-case-creation-outputs_ITER-001_v1.0.md. Save the review under AIAugmentation/dummy/runs/review-test-coverage/ITER-001/. Do not read the prepared A17.

Use $create-test-cases to revise AIAugmentation/dummy/ITER-001/A16_test-case-creation-outputs_ITER-001_v1.0.md using AIAugmentation/dummy/ITER-001/A17_test-coverage-review-outputs_ITER-001_v1.0.md. Save v1.1 under AIAugmentation/dummy/runs/create-test-cases/ITER-001/.

Use $execute-functional-tests with AIAugmentation/dummy/ITER-001/A16_test-case-creation-outputs_ITER-001_v1.0.md on build B001 in LOCAL-TEST, running `python run_cases.py SRC-001` from AIAugmentation/dummy/ITER-001/native/. Save the results under AIAugmentation/dummy/runs/execute-functional-tests/ITER-001/. Do not read the prepared A29.

Use $report-test-progress with the A29 and A31 files in AIAugmentation/dummy/ITER-001/ for the 2026-09-13 checkpoint. Save the report under AIAugmentation/dummy/runs/report-test-progress/ITER-001/. Do not read the prepared A32.

Use $assess-test-readiness for candidate RC-002 / B002 with AIAugmentation/dummy/ITER-001/A15_test-planning-outputs_ITER-001_v1.1.md and the evidence in AIAugmentation/dummy/ITER-001/. Save the assessment under AIAugmentation/dummy/runs/assess-test-readiness/ITER-001/. Do not read the prepared A33.

Read the implemented triage-defects skill and use the A29, E06 and A05 baseline files in AIAugmentation/dummy/ITER-001/. Save the defect report under AIAugmentation/dummy/runs/triage-defects/ITER-001/. Do not read the prepared A34.
```

The triage-defects prompt is for after that skill is implemented; creating these files does not implement additional skills. The functional run should reproduce the TC-003 failure on B001, and the readiness assessment should stay NOT READY because F-001 and the E09 decisions remain open.

## Artifact index

All listed files are in ITER-001. The eight creator inputs use version 1.1; the other prepared artifacts remain at version 1.0. External E artifacts represent supplied records rather than skill outputs.

| ID | Skill / owner | Artifact |
| --- | --- | --- |
| A01 | elicit-requirements | [Requirements Elicitation Outputs](ITER-001/A01_requirements-elicitation-outputs_ITER-001_v1.0.md) |
| A02 | define-scope | [Scope Definition Outputs](ITER-001/A02_scope-definition-outputs_ITER-001_v1.0.md) |
| A03 | analyze-requirements | [Requirements Analysis Outputs](ITER-001/A03_requirements-analysis-outputs_ITER-001_v1.0.md) |
| A04 | define-acceptance-criteria | [Acceptance Criteria Outputs](ITER-001/A04_acceptance-criteria-outputs_ITER-001_v1.1.md) |
| A05 | review-requirements | [Requirements Review Outputs](ITER-001/A05_requirements-review-outputs_ITER-001_v1.1.md) |
| A06 | assess-feasibility | [Feasibility Assessment Outputs](ITER-001/A06_feasibility-assessment-outputs_ITER-001_v1.1.md) |
| A07 | design-solution-architecture | [Solution Architecture Outputs](ITER-001/A07_solution-architecture-outputs_ITER-001_v1.0.md) |
| A08 | design-user-experience | [User Experience Design Outputs](ITER-001/A08_user-experience-design-outputs_ITER-001_v1.0.md) |
| A09 | design-system-components | [System Component Design Outputs](ITER-001/A09_system-component-design-outputs_ITER-001_v1.1.md) |
| A10 | review-solution-design | [Solution Design Review Outputs](ITER-001/A10_solution-design-review-outputs_ITER-001_v1.0.md) |
| A11 | decompose-work | [Work Breakdown Outputs](ITER-001/A11_work-breakdown-outputs_ITER-001_v1.0.md) |
| A12 | estimate-delivery | [Delivery Estimation Outputs](ITER-001/A12_delivery-estimation-outputs_ITER-001_v1.0.md) |
| A13 | map-dependencies | [Dependency Mapping Outputs](ITER-001/A13_dependency-mapping-outputs_ITER-001_v1.0.md) |
| A14 | plan-iterations | [Iteration Planning Outputs](ITER-001/A14_iteration-planning-outputs_ITER-001_v1.0.md) |
| A15 | plan-testing | [Test Planning Outputs](ITER-001/A15_test-planning-outputs_ITER-001_v1.1.md) |
| A16 | create-test-cases | [Test Case Creation Outputs](ITER-001/A16_test-case-creation-outputs_ITER-001_v1.0.md) |
| A17 | review-test-coverage | [Test Coverage Review Outputs](ITER-001/A17_test-coverage-review-outputs_ITER-001_v1.0.md) |
| A18 | prepare-test-resources | [Test Resources Outputs](ITER-001/A18_test-resources-outputs_ITER-001_v1.0.md) |
| A19 | build-test-automation | [Test Automation Outputs](ITER-001/A19_test-automation-outputs_ITER-001_v1.0.md) |
| A20 | implement-feature | [Feature Implementation Outputs](ITER-001/A20_feature-implementation-outputs_ITER-001_v1.0.md) |
| A21 | validate-code | [Code Validation Outputs](ITER-001/A21_code-validation-outputs_ITER-001_v1.0.md) |
| A22 | review-code | [Code Review Outputs](ITER-001/A22_code-review-outputs_ITER-001_v1.0.md) |
| A23 | integrate-changes | [Change Integration Outputs](ITER-001/A23_change-integration-outputs_ITER-001_v1.0.md) |
| A24 | build-application | [Application Build Outputs](ITER-001/A24_application-build-outputs_ITER-001_v1.0.md) |
| A25 | validate-ci-checks | [CI Validation Outputs](ITER-001/A25_ci-validation-outputs_ITER-001_v1.0.md) |
| A26 | deploy-test-build | [Test Deployment Outputs](ITER-001/A26_test-deployment-outputs_ITER-001_v1.0.md) |
| A27 | execute-smoke-tests | [Smoke Testing Outputs](ITER-001/A27_smoke-testing-outputs_ITER-001_v1.0.md) |
| A28 | execute-integration-tests | [Integration Testing Outputs](ITER-001/A28_integration-testing-outputs_ITER-001_v1.0.md) |
| A29 | execute-functional-tests | [Functional Testing Outputs](ITER-001/A29_functional-testing-outputs_ITER-001_v1.0.md) |
| A30 | execute-nonfunctional-tests | [Nonfunctional Testing Outputs](ITER-001/A30_nonfunctional-testing-outputs_ITER-001_v1.0.md) |
| A31 | execute-regression-tests | [Regression Testing Outputs](ITER-001/A31_regression-testing-outputs_ITER-001_v1.0.md) |
| A32 | report-test-progress | [Test Progress Outputs](ITER-001/A32_test-progress-outputs_ITER-001_v1.0.md) |
| A33 | assess-test-readiness | [Test Exit Assessment Outputs](ITER-001/A33_test-exit-assessment-outputs_ITER-001_v1.0.md) |
| A34 | triage-defects | [Defect Triage Outputs](ITER-001/A34_defect-triage-outputs_ITER-001_v1.0.md) |
| A35 | fix-defects | [Defect Fix Outputs](ITER-001/A35_defect-fix-outputs_ITER-001_v1.0.md) |
| A36 | retest-defects | [Defect Retest Outputs](ITER-001/A36_defect-retest-outputs_ITER-001_v1.0.md) |
| A37 | support-uat | [User Acceptance Testing Outputs](ITER-001/A37_user-acceptance-testing-outputs_ITER-001_v1.0.md) |
| A38 | summarize-test-results | [Test Summary Outputs](ITER-001/A38_test-summary-outputs_ITER-001_v1.0.md) |
| A39 | assess-release-readiness | [Release Readiness Outputs](ITER-001/A39_release-readiness-outputs_ITER-001_v1.0.md) |
| A40 | plan-release | [Release Planning Outputs](ITER-001/A40_release-planning-outputs_ITER-001_v1.0.md) |
| A41 | prepare-release-decision | [Release Decision Outputs](ITER-001/A41_release-decision-outputs_ITER-001_v1.0.md) |
| A42 | deploy-release | [Production Deployment Outputs](ITER-001/A42_production-deployment-outputs_ITER-001_v1.0.md) |
| A43 | monitor-and-support | [Monitoring and Support Outputs](ITER-001/A43_monitoring-and-support-outputs_ITER-001_v1.0.md) |
| A44 | analyze-product-feedback | [Product Feedback Outputs](ITER-001/A44_product-feedback-outputs_ITER-001_v1.0.md) |
| A45 | resolve-release-blockers | [Release Blocker Resolution Outputs](ITER-001/A45_release-blocker-resolution-outputs_ITER-001_v1.0.md) |
| E01 | Business and product owners | [Business Context](ITER-001/E01_business-context_ITER-001_v1.1.md) |
| E02 | Architecture and product owners | [Product and Architecture Context](ITER-001/E02_product-and-architecture-context_ITER-001_v1.0.md) |
| E03 | Engineering and governance owners | [Engineering and Governance Policies](ITER-001/E03_engineering-and-governance-policies_ITER-001_v1.0.md) |
| E04 | Delivery lead and team | [Delivery Planning Records](ITER-001/E04_delivery-planning-records_ITER-001_v1.0.md) |
| E05 | Repository and CI/tool owners | [Repository and CI Evidence](ITER-001/E05_repository-and-ci-evidence_ITER-001_v1.0.md) |
| E06 | Test lead and defect system | [Test and Defect Baselines](ITER-001/E06_test-and-defect-baselines_ITER-001_v1.1.md) |
| E07 | Environment and access owners | [Environment and Access Records](ITER-001/E07_environment-and-access-records_ITER-001_v1.0.md) |
| E08 | Observability, support and research systems | [Operational and Product Evidence](ITER-001/E08_operational-and-product-evidence_ITER-001_v1.0.md) |
| E09 | Named decision owners and reviewers | [Human Decisions](ITER-001/E09_human-decisions_ITER-001_v1.1.md) |
| E10 | Operations and service owners | [Operational Readiness](ITER-001/E10_operational-readiness_ITER-001_v1.0.md) |

[A05 v1.1](ITER-001/A05_requirements-review-outputs_ITER-001_v1.1.md) embeds the complete common behavior and scope. The original standalone file remains only for older artifact snapshots.
