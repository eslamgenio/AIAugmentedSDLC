# Quick start

You need your project open in an agent that can read the skill instructions,
plus requirements and acceptance criteria. No Python setup is needed.

## Set up once

1. Copy `.agents/skills/`, `AIAugmentation/README.md`,
   `AIAugmentation/templates/` and `AIAugmentation/project_guides/` into
   the same locations in your project. Merge existing folders; keep your
   project's README and other files.
2. Copy `AGENTS.team.md` to your project root as `AGENTS.md`. If one
   already exists, merge the instructions instead of replacing it.
3. Fill in its **Project context**: project name and purpose, relevant
   directory tree, input locations and project-specific rules. Use
   `ITER-001` for your first iteration; leave unknown details explicit.

## Update later

With Git installed and access to the team's [GitLab repository](https://gitlabce.tools.aws.vodafone.com/central-vois-framework/devskillkit.git), copy `update-skill-kit.ps1`
into your project root. Run it with an available version tag:

```powershell
.\update-skill-kit.ps1 -Version v1.2.0
```

Replace the example version with a published tag. Missing project-guide files
are installed from the release. Root `README.md` and `min_user_guide.md`
are installed or replaced with the release copies. Save any project-specific
README content elsewhere first. Existing project guides, artifacts,
and your `AGENTS.md` are preserved. Review and commit the shared-file changes.
See [update details and prerequisites](AIAugmentation/README.md#update-an-installed-kit).

## Create and review test cases

Put your requirements and acceptance criteria in
`AIAugmentation/artifacts/ITER-001/Requirements/` (existing filenames are fine).
Then send these prompts, one at a time, from your project root:

```text
Use $create-test-cases for ITER-001 with the requirements and acceptance
criteria in AIAugmentation/artifacts/ITER-001/Requirements/.
```

```text
Use $review-test-coverage for ITER-001 with the same requirements and
the A16 file just created.
```

You receive **A16: test cases** and **A17: coverage review** as `.md` files.
These skills do not execute tests or grant approval. If a skill is not
discovered, ask the agent to read and follow
`.agents/skills/<skill-name>/SKILL.md` directly.

More detail: [Kit setup and usage](AIAugmentation/README.md).
