# review-test-coverage — User guide

Use this skill to assess whether test cases adequately cover their requirements, and to verify corrections after a previous review. It produces **A17 — Test Coverage Review Outputs**. It reviews test design, not application execution results.

## What you need

Supply both the requirements baseline and the exact candidate test document. The candidate can be an A16 bundle or another test-case format. A05 may contain the complete requirements baseline; a particular requirements filename is not required.

The skill reads the following project artifacts when present:

| Artifact | Canonical filename prefix | What it supplies |
| --- | --- | --- |
| A16 | `A16_test-case-creation-outputs` | Candidate test cases |
| A05 | `A05_requirements-review-outputs` | Requirements baseline, embedded or referenced |
| A04 | `A04_acceptance-criteria-outputs` | Acceptance criteria |
| A06 | `A06_feasibility-assessment-outputs` | Risk register |
| E06 | `E06_test-and-defect-baselines` | Coverage rules and review checklist |

Append `_{iteration_id}_v{artifact_version}.md` to each prefix. Use the same compatible baseline that informed the candidate, and identify exact versions when multiple snapshots exist. Missing requirements or candidate cases prevent a meaningful review; missing optional supporting inputs are recorded as limitations.

## Review a candidate

Open the project in Codex. For an independent review, start a fresh task and supply the generated candidate rather than a prepared sample answer. Run from the project root, replacing `[A16 file]` with its path:

```text
Use $review-test-coverage with AIAugmentation/dummy/ITER-001/A05_requirements-review-outputs_ITER-001_v1.1.md and [A16 file].
```

For a practice run, append:

```text
Save the review under AIAugmentation/dummy/runs/review-test-coverage/ITER-001/.
```

No Python or running application is required. If the skill is not recognized, use:

```text
Read and follow .agents/skills/review-test-coverage/SKILL.md with AIAugmentation/dummy/ITER-001/A05_requirements-review-outputs_ITER-001_v1.1.md and [A16 file].
```

## What you receive

Without a configured layout, the first review is `AIAugmentation/artifacts/ITER-001/A17_test-coverage-review-outputs_ITER-001_v1.0.md`, using the candidate's iteration. With phase layout, it goes under that iteration's `Test Preparation/` folder. A requested location takes precedence; re-reviews otherwise stay in the prior A17 folder. Previous files are preserved, and subsequent review revisions receive new versions. A17 versions do not need to equal the input artifact versions.

Input discovery includes the active iteration root and its subfolders, including other phases and `External Inputs/`. Explicit paths and versions take precedence. Duplicate artifact/version candidates or conflicting baselines need clarification before the affected input is used; files from other iterations are used only when explicitly supplied or referenced. Outputs remain Markdown.

| Section | Contents |
| --- | --- |
| A17-01 | Requirement/criterion-to-test matrix with FULL, PARTIAL, NONE or BLOCKED coverage; justified NOT APPLICABLE exclusions |
| A17-02 | Coverage gaps and unnecessary duplicate cases |
| A17-03 | Findings with evidence and requested corrections; verification of prior findings on re-review |

The project uses the [A17 template](../../../AIAugmentation/templates/A17_test-coverage-review-outputs.md). When copied without project templates, the skill uses its built-in [SKILL.md](SKILL.md) layout.

## Understand the recommendation

| Recommendation | Meaning | Your next action |
| --- | --- | --- |
| READY | Adequate design coverage with no blocking defects or unresolved expected behavior; nonblocking suggestions may remain | Review disclosed limitations and arrange any required human acceptance or execution preparation |
| REVISE | Material issues can be corrected using the supplied requirements | Pass A16 and A17 to create-test-cases for correction |
| BLOCKED | Essential missing or conflicting information requires an owner decision | Resolve the specific question, then request the affected work again |

READY is a design recommendation, not human approval or proof that application tests passed. A valid review can contain no findings; the reviewer should not manufacture corrections just to exercise a revision cycle.

## Correct and re-review

Ask the creator to address the review:

```text
Use $create-test-cases to revise [A16 file] using [A17 file].
```

Then give the reviewer the new candidate and prior review:

```text
Use $review-test-coverage to re-review [revised A16 file] against [A05 baseline file], using [prior A17 file] as the prior review.
```

The reviewer preserves source files and prior reviews, checks actual changes, retains finding IDs, and closes findings only when the evidence supports it. It also checks whether revisions introduced other problems. A prior READY decision never automatically applies to a changed candidate.

## Check the result

Confirm that A17 identifies the exact candidate and baseline, accounts for every criterion, cites concrete evidence for findings, and gives actionable next steps. The reviewer must leave A16 unchanged. See the [creator guide](../create-test-cases/README.md) for creation and revision details.
