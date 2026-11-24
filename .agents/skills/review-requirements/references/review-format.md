# Review report format

- **Review scope:** Inclusions, exclusions, and evidence limitations.
- **Revision pins:** Artifact | ID/path | exact revision or snapshot label | authority/availability.
- **Overall gate:** READY, REVISE, or BLOCKED with a one-sentence reason.
- **Scoped readiness:** Requirement IDs | criterion IDs | evidence locator | gate and what can proceed.
- **Findings:** Stable RR ID | status | category and priority | affected requirement/criteria | evidence or precise gap | consequence | action or question.
- **Optional improvements:** Separate from required changes.
- **Handoff:** Which IDs are suitable for test design; remaining questions and exact evidence needed. For re-review, record the old → new revisions and evidence for each carried ID.

## Synthetic review fixtures

Read each fixture as a document review, not a test run. In all cases the project is an imaginary room-booking system and all inputs are synthetic.

### Fixture 1: Adjacent values do not cover the exact boundary

- Scope v1: Include RQ-001 billing deposit rule; payment processing excluded.
- Source SRC-001 v1 §2 and RQ-001 v1: For a booking price in whole credits, require a deposit at 80 credits or higher; below 80, no deposit is required.
- Acceptance v1: AC-001 at 79 no deposit; AC-002 at 81 deposit required. Summary claims full coverage.
- Expected: REVISE; RR-001 OPEN; request an observable 80-credit criterion requiring a deposit. Do not block on intent, invent a payment flow, or accept the coverage label as proof.

### Fixture 2: Close the same finding against a pinned revision

- Prior report: RR-001 OPEN for the missed boundary against Acceptance v1.
- Inputs: Same pinned scope, source and RQ; exact revised Acceptance v2 retains AC-001 and AC-002 and adds AC-003: Given a whole-credit booking price of exactly 80, when the customer views the booking's charges, then the booking displays a deposit requirement.
- Expected: READY within RQ-001 only, with RR-001 CLOSED citing Acceptance v2 AC-003. No claim that the app passed.
- Negative control: If only a change summary says AC-003 was added but Acceptance v2 is unavailable, do not close RR-001 or report READY.

### Fixture 3: Missing decisive business rule

- Scope v1 includes RQ-002. Its available, equally authoritative source statements disagree on whether 80 qualifies; no precedence or approving decision is provided.
- Acceptance v1 asserts a deposit at 80 with no source resolving the conflict.
- Expected: BLOCKED for RQ-002; cite both clauses, name the unresolved inclusive-versus-exclusive choice, and do not treat the authored criterion as authority. If Fixture 2 is also present and unrelated, preserve READY for RQ-001 but report overall BLOCKED.

## DevSkillKit A05 Markdown handoff

After the required YAML metadata, include these sections in the report body using normal headings, narrative, lists and tables:

- **Review scope and gate:** Overall gate, rationale, evidence limitations and scoped readiness.
- **Baseline ID and requirement versions:** Actual supplied baseline ID (or not supplied); source artifact/requirement IDs and revisions, explicitly labelling unversioned snapshots.
- **A05-01 Review findings and actions:** Review findings and structured follow-up actions with stable RR IDs. If the owner is unknown, say so. An empty findings table means no material findings only within the inspected scope.
- **A05-02 Proposed baseline and revision history:** Show the baseline and exact relevant revisions; keep the baseline proposed unless authorized agreement is evidenced.
- **A05-03 Stakeholder agreement and pending decisions:** Include actual stakeholder decision references, owners where known, and unresolved decisions. Explicitly say when no decision is evidenced. READY is not stakeholder approval.
- **Test design handoff:** Ready requirement/criterion IDs, held items, and exact evidence needed to unblock them.
