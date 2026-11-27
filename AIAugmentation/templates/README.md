# Artifact templates

These 55 Markdown templates cover all 45 skill output bundles (A01–A45) and 10 external input bundles (E01–E10) in the Excel catalog. The 135 child deliverables are embedded under their stable IDs in the A templates. A template defines content; it does not implement a skill or supply evidence.

## Use a template

1. Find the bundle below and read its template before producing the artifact. External templates are completed from attributable owner or system records.
2. Follow an explicitly requested output location; otherwise preserve the prior artifact folder for revisions, then use the project's configured layout. With phase layout, A01–A05 belong in `Requirements/`, A15–A17 belong in `Test Preparation/`, and A28–A33 belong in `Test Execution/` under the active iteration. Without a configured layout, use `AIAugmentation/artifacts/<iteration_id>/`. Replace filename placeholders with the iteration and version. See the [phase mapping and storage rules](../README.md#artifact-folders-and-handoffs).
3. Fill the metadata and relevant content. Repeat tables or record blocks as needed. Replace placeholders and remove template instructions. State **None**, **Not applicable — reason**, or **Missing — impact / owner** explicitly; never fill gaps with invented evidence or approval.
4. Reference exact input filenames and versions. Preserve child, test and finding IDs; save changed content as a new version within the same iteration.
5. Check the acceptance criteria at the end. Record unresolved limitations and the next handoff. Use the catalog's conditional handoff rules; a draft alone does not satisfy a gate.

Template filenames omit iteration/version suffixes because they are reusable. Each template gives its full output filename pattern. These are the canonical human-readable Markdown artifact templates. Use the catalog's canonical basenames with the `.md` extension and retain iteration, artifact/schema versions, owner, timestamp, status, evidence and exact upstream revisions in readable metadata and sections. The Markdown output is the exchange record; do not emit JSON as its payload or competing manifest. Native code, builds, datasets, diagrams and evidence stay in their appropriate formats and are linked from the document with an exact revision or digest when applicable. Do not substitute a Markdown description for an actual runnable or signed deliverable.

The fourteen implemented skills (A01–A05, A15–A17 and A28–A33) use their matching project template for the canonical Markdown delivery, including its nine YAML keys. Restore a missing template before claiming canonical delivery. Extra views may supplement, but never replace, the canonical Markdown handoff. Missing optional inputs do not prevent a useful draft, but missing essential evidence or decisions must remain visible.

## Template index

| ID | Bundle | Producer / external owner | Template |
| --- | --- | --- | --- |
| A01 | Requirements Elicitation Outputs | elicit-requirements | [A01_requirements-elicitation-outputs.md](A01_requirements-elicitation-outputs.md) |
| A02 | Scope Definition Outputs | define-scope | [A02_scope-definition-outputs.md](A02_scope-definition-outputs.md) |
| A03 | Requirements Analysis Outputs | analyze-requirements | [A03_requirements-analysis-outputs.md](A03_requirements-analysis-outputs.md) |
| A04 | Acceptance Criteria Outputs | define-acceptance-criteria | [A04_acceptance-criteria-outputs.md](A04_acceptance-criteria-outputs.md) |
| A05 | Requirements Review Outputs | review-requirements | [A05_requirements-review-outputs.md](A05_requirements-review-outputs.md) |
| A06 | Feasibility Assessment Outputs | assess-feasibility | [A06_feasibility-assessment-outputs.md](A06_feasibility-assessment-outputs.md) |
| A07 | Solution Architecture Outputs | design-solution-architecture | [A07_solution-architecture-outputs.md](A07_solution-architecture-outputs.md) |
| A08 | User Experience Design Outputs | design-user-experience | [A08_user-experience-design-outputs.md](A08_user-experience-design-outputs.md) |
| A09 | System Component Design Outputs | design-system-components | [A09_system-component-design-outputs.md](A09_system-component-design-outputs.md) |
| A10 | Solution Design Review Outputs | review-solution-design | [A10_solution-design-review-outputs.md](A10_solution-design-review-outputs.md) |
| A11 | Work Breakdown Outputs | decompose-work | [A11_work-breakdown-outputs.md](A11_work-breakdown-outputs.md) |
| A12 | Delivery Estimation Outputs | estimate-delivery | [A12_delivery-estimation-outputs.md](A12_delivery-estimation-outputs.md) |
| A13 | Dependency Mapping Outputs | map-dependencies | [A13_dependency-mapping-outputs.md](A13_dependency-mapping-outputs.md) |
| A14 | Iteration Planning Outputs | plan-iterations | [A14_iteration-planning-outputs.md](A14_iteration-planning-outputs.md) |
| A15 | Test Planning Outputs | plan-testing | [A15_test-planning-outputs.md](A15_test-planning-outputs.md) |
| A16 | Test Case Creation Outputs | create-test-cases | [A16_test-case-creation-outputs.md](A16_test-case-creation-outputs.md) |
| A17 | Test Coverage Review Outputs | review-test-coverage | [A17_test-coverage-review-outputs.md](A17_test-coverage-review-outputs.md) |
| A18 | Test Resources Outputs | prepare-test-resources | [A18_test-resources-outputs.md](A18_test-resources-outputs.md) |
| A19 | Test Automation Outputs | build-test-automation | [A19_test-automation-outputs.md](A19_test-automation-outputs.md) |
| A20 | Feature Implementation Outputs | implement-feature | [A20_feature-implementation-outputs.md](A20_feature-implementation-outputs.md) |
| A21 | Code Validation Outputs | validate-code | [A21_code-validation-outputs.md](A21_code-validation-outputs.md) |
| A22 | Code Review Outputs | review-code | [A22_code-review-outputs.md](A22_code-review-outputs.md) |
| A23 | Change Integration Outputs | integrate-changes | [A23_change-integration-outputs.md](A23_change-integration-outputs.md) |
| A24 | Application Build Outputs | build-application | [A24_application-build-outputs.md](A24_application-build-outputs.md) |
| A25 | CI Validation Outputs | validate-ci-checks | [A25_ci-validation-outputs.md](A25_ci-validation-outputs.md) |
| A26 | Test Deployment Outputs | deploy-test-build | [A26_test-deployment-outputs.md](A26_test-deployment-outputs.md) |
| A27 | Smoke Testing Outputs | execute-smoke-tests | [A27_smoke-testing-outputs.md](A27_smoke-testing-outputs.md) |
| A28 | Integration Testing Outputs | execute-integration-tests | [A28_integration-testing-outputs.md](A28_integration-testing-outputs.md) |
| A29 | Functional Testing Outputs | execute-functional-tests | [A29_functional-testing-outputs.md](A29_functional-testing-outputs.md) |
| A30 | Nonfunctional Testing Outputs | execute-nonfunctional-tests | [A30_nonfunctional-testing-outputs.md](A30_nonfunctional-testing-outputs.md) |
| A31 | Regression Testing Outputs | execute-regression-tests | [A31_regression-testing-outputs.md](A31_regression-testing-outputs.md) |
| A32 | Test Progress Outputs | report-test-progress | [A32_test-progress-outputs.md](A32_test-progress-outputs.md) |
| A33 | Test Exit Assessment Outputs | assess-test-readiness | [A33_test-exit-assessment-outputs.md](A33_test-exit-assessment-outputs.md) |
| A34 | Defect Triage Outputs | triage-defects | [A34_defect-triage-outputs.md](A34_defect-triage-outputs.md) |
| A35 | Defect Fix Outputs | fix-defects | [A35_defect-fix-outputs.md](A35_defect-fix-outputs.md) |
| A36 | Defect Retest Outputs | retest-defects | [A36_defect-retest-outputs.md](A36_defect-retest-outputs.md) |
| A37 | User Acceptance Testing Outputs | support-uat | [A37_user-acceptance-testing-outputs.md](A37_user-acceptance-testing-outputs.md) |
| A38 | Test Summary Outputs | summarize-test-results | [A38_test-summary-outputs.md](A38_test-summary-outputs.md) |
| A39 | Release Readiness Outputs | assess-release-readiness | [A39_release-readiness-outputs.md](A39_release-readiness-outputs.md) |
| A40 | Release Planning Outputs | plan-release | [A40_release-planning-outputs.md](A40_release-planning-outputs.md) |
| A41 | Release Decision Outputs | prepare-release-decision | [A41_release-decision-outputs.md](A41_release-decision-outputs.md) |
| A42 | Production Deployment Outputs | deploy-release | [A42_production-deployment-outputs.md](A42_production-deployment-outputs.md) |
| A43 | Monitoring and Support Outputs | monitor-and-support | [A43_monitoring-and-support-outputs.md](A43_monitoring-and-support-outputs.md) |
| A44 | Product Feedback Outputs | analyze-product-feedback | [A44_product-feedback-outputs.md](A44_product-feedback-outputs.md) |
| A45 | Release Blocker Resolution Outputs | resolve-release-blockers | [A45_release-blocker-resolution-outputs.md](A45_release-blocker-resolution-outputs.md) |
| E01 | Business Context | Business and product owners | [E01_business-context.md](E01_business-context.md) |
| E02 | Product and Architecture Context | Architecture and product owners | [E02_product-and-architecture-context.md](E02_product-and-architecture-context.md) |
| E03 | Engineering and Governance Policies | Engineering and governance owners | [E03_engineering-and-governance-policies.md](E03_engineering-and-governance-policies.md) |
| E04 | Delivery Planning Records | Delivery lead and team | [E04_delivery-planning-records.md](E04_delivery-planning-records.md) |
| E05 | Repository and CI Evidence | Repository and CI/tool owners | [E05_repository-and-ci-evidence.md](E05_repository-and-ci-evidence.md) |
| E06 | Test and Defect Baselines | Test lead and defect system | [E06_test-and-defect-baselines.md](E06_test-and-defect-baselines.md) |
| E07 | Environment and Access Records | Environment and access owners | [E07_environment-and-access-records.md](E07_environment-and-access-records.md) |
| E08 | Operational and Product Evidence | Observability, support and research systems | [E08_operational-and-product-evidence.md](E08_operational-and-product-evidence.md) |
| E09 | Human Decisions | Named decision owners and reviewers | [E09_human-decisions.md](E09_human-decisions.md) |
| E10 | Operational Readiness | Operations and service owners | [E10_operational-readiness.md](E10_operational-readiness.md) |
