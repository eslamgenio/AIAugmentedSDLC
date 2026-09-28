# Dev Skill Kit

**Reusable, project-agnostic AI-agent skills for the software development lifecycle.**

Dev Skill Kit helps teams turn development activities into repeatable workflows
that an AI agent can perform or assist with inside an existing project.

## Our target

Support an end-to-end, increasingly autonomous SDLC from requirements and
solution design through development, testing, release, and maintenance.
Each skill focuses on one activity and produces artifacts that can become
inputs to subsequent activities, with human decisions and approvals where required.

The intended flow is:

**Requirements → Design → Development → Testing → Release → Maintenance**

This is the target, not a fully implemented or automatically orchestrated workflow.

## Why use Dev Skill Kit?

- **Reduce repetitive work:** give agents reusable procedures for common activities.
- **Keep outputs consistent:** use shared artifact structures and review criteria.
- **Maintain traceability:** connect outputs to their requirements, sources, and revisions.
- **Adapt to your project:** keep domain rules and local conventions in project
  instructions and optional guides, while shared skills remain reusable.

## Available today

The current MVP covers test design and coverage review:

| Skill | What it does | What you receive |
| --- | --- | --- |
| [create-test-cases](.agents/skills/create-test-cases/README.md) | Creates or revises requirement-linked cases with preconditions, data, steps, and expected results. | A test-case document, open questions, and automation candidates. |
| [review-test-coverage](.agents/skills/review-test-coverage/README.md) | Checks cases against requirements for coverage, correct expectations, clarity, and duplicates. | A coverage matrix, findings, and actionable revision requests. |

**Working flow:** Requirements → Create test cases → Review coverage → Revise as needed.

These skills design and review tests; they do not execute tests or grant approval.
Engineering review remains essential. Skills for other lifecycle activities and
automated orchestration are not yet implemented.

## Get started

1. Follow the [quick start](min_user_guide.md) to install the kit in your project
   and complete its project context.
2. Supply your own requirements and acceptance criteria.
3. Ask your agent to create cases, then review the resulting document:

```text
Use $create-test-cases with [requirements file or folder].
```

```text
Use $review-test-coverage with [requirements] and [test-case file].
```

Replace bracketed placeholders with actual project paths. Sample data and the
broader framework catalog are not required. The skills flag missing information
rather than inventing expected behavior.

## Install or update the kit in another project

### Prerequisites

- PowerShell 5.1 or later:

```powershell
$PSVersionTable.PSVersion
```

- Git installed and available from PowerShell:

```powershell
git --version
```

- Access to the Dev Skill Kit repository:

```powershell
git ls-remote --tags https://gitlabce.tools.aws.vodafone.com/central-vois-framework/devskillkit.git
```

If the command returns tags, repository access is working.

- A valid release tag. Use one of the tags returned by the previous command.
  For example:

```text
v1.0.3
```

- An existing target project folder. The folder does not have to be a Git
  repository for the updater to copy files, but it should be a Git repository if
  you want to review and commit the changes.

### Exact steps

1. Open PowerShell.

2. Go to the project where you want to install or update the kit:

```powershell
Set-Location "C:\Path\To\TargetProject"
```

3. If the folder should be a Git repository and is not one yet, initialize it:

```powershell
git init
```

Optional, but recommended if you plan to commit:

```powershell
git config user.name "Your Name"
git config user.email "your.email@company.com"
```

4. Confirm the available release tags:

```powershell
git ls-remote --tags https://gitlabce.tools.aws.vodafone.com/central-vois-framework/devskillkit.git
```

Use the highest valid semantic-version tag shown, such as `v1.0.3`.

5. Preview the install or update from the repository that contains
   `update-skill-kit.ps1`:

```powershell
& "C:\Users\AdelMahmoudE\Downloads\New folder\AIAugmentedSDLC\update-skill-kit.ps1" `
  -Version v1.0.3 `
  -ProjectPath "C:\Path\To\TargetProject" `
  -WhatIf
```

6. Run the actual install or update:

```powershell
& "C:\Users\AdelMahmoudE\Downloads\New folder\AIAugmentedSDLC\update-skill-kit.ps1" `
  -Version v1.0.3 `
  -ProjectPath "C:\Path\To\TargetProject"
```

7. Review the result:

```powershell
git status
git diff
```

If the target folder is not a Git repository, manually inspect the created or
updated files instead.

8. Commit the changes if this is a Git project:

```powershell
git add .
git commit -m "Install SDLC skill kit"
```

If you copied `update-skill-kit.ps1` into the target project, you can run it
from that project without `-ProjectPath` because the script defaults to the
current folder:

```powershell
.\update-skill-kit.ps1 -Version v1.0.3 -WhatIf
.\update-skill-kit.ps1 -Version v1.0.3
```

The updater installs shared kit files from the selected release tag, including
`.agents\skills\...`, `AIAugmentation\...`, `AGENTS.team.md`, `README.md`,
`min_user_guide.md`, and `AIAugmentation\skill-kit-version.txt`. It preserves
existing `AGENTS.md`, existing project guides, artifacts, unrelated skills, and
does not delete files.

## Documentation

- [Install or update the kit](AIAugmentation/README.md#install-or-update-the-kit)
- [Configure project context](AIAugmentation/README.md#complete-the-project-context)
- [Customize individual skills with project guides](AIAugmentation/project_guides/README.md)
- [Artifact templates](AIAugmentation/templates/README.md)
- [Artifact storage and handoffs](AIAugmentation/README.md#artifact-folders-and-handoffs)
