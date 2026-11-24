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
   use [the five Requirements skills](README.md#use-the-seven-skills) in order:
   elicit requirements (A01), define scope (A02), analyze requirements (A03),
   define acceptance criteria (A04), then review the exact artifact revisions
   (A05). Leave unanswered rules open. A draft or review does not grant approval.
4. **Create test cases.** Bring a usable requirements baseline and acceptance
   criteria to the [creation guide](../.agents/skills/create-test-cases/README.md).
   Record pending decisions and restrict work to what the evidence supports.
5. **Review coverage.** Use the same baseline and the exact A16 revision with
   the [coverage review guide](../.agents/skills/review-test-coverage/README.md).
   Revise and re-review on new versions when needed.

Use the matching [Markdown templates](templates/README.md) for handoffs.
These skills do not execute tests, approve scope, or authorize release.

For later releases, return to [install or update](README.md#install-or-update-the-kit),
then review and commit the changes in your project.
