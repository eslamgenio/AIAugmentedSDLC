# Dev Skill Kit — Quick start

You need an AI agent that can read the skill instructions and your project's
requirements and acceptance criteria. The skills themselves need no Python setup.

1. **Install the kit.** Follow [installation and prerequisites](README.md#install-or-update-the-kit).
   The updater supports first-time setup and later upgrades. It updates the
   kit guides inside `AIAugmentation/` and preserves your project root README.
   It creates missing `Requirements`, `Solution Design`, `Test Preparation`,
   and `External Inputs` folders under `AIAugmentation/artifacts/ITER-001/`,
   preserving existing content. Use `-IterationId ITER-002` to select another
   iteration; add `-WhatIf` to preview without changing files or folders.
2. **Configure your project.** Follow [project-context setup](README.md#complete-the-project-context)
   to create or merge `AGENTS.md`. Add [optional project guides](project_guides/README.md)
   only when activity-specific conventions are needed.
3. **Start with requirements.** If you do not already have a usable baseline,
   use [the five Requirements skills](README.md#use-the-fourteen-skills) in order:
   elicit requirements (A01), define scope (A02), analyze requirements (A03),
   define acceptance criteria (A04), then review the exact artifact revisions
   (A05). Leave unanswered rules open. A draft or review does not grant approval.
4. **Plan testing.** Bring the reviewed baseline and acceptance criteria to the
   [test planning guide](../.agents/skills/plan-testing/README.md) to produce
   A15: scope, risk priorities, levels, responsibilities, environment needs and
   measurable entry, exit and suspension criteria. Missing owners or dates stay open.
5. **Create test cases.** Bring a usable requirements baseline, acceptance
   criteria and the A15 plan when available to the [creation guide](../.agents/skills/create-test-cases/README.md).
   Record pending decisions and restrict work to what the evidence supports.
6. **Review coverage.** Use the same baseline and the exact A16 revision with
   the [coverage review guide](../.agents/skills/review-test-coverage/README.md).
   Revise and re-review on new versions when needed.
7. **Execute tests.** When you are ready to run tests, name the build, the
   environment you are authorized to test and the commands to use, then use the
   [integration](../.agents/skills/execute-integration-tests/README.md),
   [functional](../.agents/skills/execute-functional-tests/README.md),
   [non-functional](../.agents/skills/execute-nonfunctional-tests/README.md) or
   [regression](../.agents/skills/execute-regression-tests/README.md) guide to
   produce A28–A31. The skills can also record a run that already happened.
   Failed results become defect candidates; blocked and not-run tests keep their reasons.
8. **Report progress.** Use the [progress guide](../.agents/skills/report-test-progress/README.md)
   to produce A32 from the execution records, with counts per build and reporting period.
9. **Assess test readiness.** Use the [readiness guide](../.agents/skills/assess-test-readiness/README.md)
   to assess each A15 exit criterion for a candidate build and produce A33 with a
   READY or NOT READY recommendation. The human test owner makes the exit decision.

Use the matching [Markdown templates](templates/README.md) for handoffs.
The execution skills run tests only when asked and never deploy, fix defects or
change code. No skill approves scope or test plans, grants test exit or authorizes release.

For later releases, return to [install or update](README.md#install-or-update-the-kit),
then review and commit the changes in your project.
