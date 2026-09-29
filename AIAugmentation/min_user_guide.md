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
3. **Supply your inputs.** Identify your requirements, acceptance criteria, and
   active iteration. Existing filenames are fine; follow your configured
   [artifact layout](README.md#artifact-folders-and-handoffs).
4. **Create test cases.** Use the [creation guide](../.agents/skills/create-test-cases/README.md)
   for the prompt, required inputs, and expected output.
5. **Review and refine.** Follow the [coverage review guide](../.agents/skills/review-test-coverage/README.md)
   with the same requirements and generated cases. Request revisions when needed.

Expect a test-case document and a coverage review. These skills do not execute
tests or grant approval. Review the results before using them.

For later releases, return to [install or update](README.md#install-or-update-the-kit),
then review and commit the changes in your project.
