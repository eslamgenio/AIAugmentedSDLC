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

v1.0.8 provides seven skills: five for Requirements (A01–A05) and two for
Test Preparation (A16/A17). See [inputs, outputs and examples](#use-the-seven-skills).

**Working flow:** Requirements → Create test cases → Review coverage → Revise as needed.

These skills capture, analyze and review requirements or design and review tests.
They do not execute tests or grant approval. Skills for other lifecycle activities and
automated orchestration are not yet implemented. Human owners retain test-exit
and release decisions.

An optional, separately supplied workbook describes **45 proposed skills** and
**48 activity or decision-gate associations** in the wider framework.

## Get started

Follow the [quick start](min_user_guide.md), configure your project context,
and supply your own requirements and acceptance criteria. Sample data and the
broader framework catalog are not required. The skills flag missing information
rather than inventing expected behavior.

## Documentation

- [Install or update the kit](#install-or-update-the-kit)
- [Configure project context](#complete-the-project-context)
- [Use the seven skills](#use-the-seven-skills)
- [Customize individual skills with project guides](project_guides/README.md)
- [Artifact templates](templates/README.md)
- [Artifact storage and handoffs](#artifact-folders-and-handoffs)

## Set up the kit in an existing project

This file, `AIAugmentation/README.md`, contains the kit overview, setup and usage
guidance. The updater installs this guide and `AIAugmentation/min_user_guide.md`
while preserving your project's existing root README.

For manual installation:

1. Copy the kit's skill folders into your project's `.agents/skills/` and
   its reusable resources into `AIAugmentation/`, retaining the relative
   paths. Include this README, `min_user_guide.md`, `templates/` and `project_guides/`. Merge
   with existing directories and review file conflicts rather than
   replacing existing project files.
2. Copy the kit's root `AGENTS.team.md` into the project root and complete
   its **Project context** section using the guidance below.
3. Rename that file to `AGENTS.md`. If the project already has an
   `AGENTS.md`, merge the relevant team instructions and project context
   into it instead of overwriting it. Resolve conflicting conventions
   explicitly.
4. Add optional activity-specific customization under
   `AIAugmentation/project_guides/<skill-name>-guide.md`, using the skill's
   frontmatter `name`. See the [project-guide instructions](project_guides/README.md).

After updater installation and project-context setup, the layout is:

```text
your-project/
├── README.md                  # Your project README (preserved)
├── AGENTS.team.md             # Shared instruction template
├── update-skill-kit.ps1       # Copied separately by the team
├── AGENTS.md                  # Team instructions and project context
├── .agents/skills/            # Reusable skill packages
└── AIAugmentation/
    ├── README.md              # Kit overview, setup and usage
    ├── min_user_guide.md       # Kit quick start
    ├── templates/             # Reusable artifact templates
    ├── project_guides/        # Missing released guides added; existing files kept
    └── skill-kit-version.txt  # Installed release tag
```

### Install or update the kit

Prerequisites: Windows PowerShell 5.1 or PowerShell 7, Git, and authenticated read
access to [the private GitHub repository](https://github.com/eslamgenio/AIAugmentedSDLC).
The current updater defaults to this repository. The explicit repository in the
examples also works with older updater copies. Never put a token in the script
or repository URL.

Copy the kit's root `update-skill-kit.ps1` into your project's root once.
The same command supports first-time installation and later upgrades. The
project directory must exist; kit folders do not need to exist yet.
From that project root, preview and install an available release tag:

```powershell
.\update-skill-kit.ps1 -Repository 'https://github.com/eslamgenio/AIAugmentedSDLC.git' -Version v1.0.8 -WhatIf
.\update-skill-kit.ps1 -Repository 'https://github.com/eslamgenio/AIAugmentedSDLC.git' -Version v1.0.8
```

`v1.0.8` is a published tag; select another only if it has been published. The updater
fetches the exact Git tag, not the latest branch. `-WhatIf` downloads and
validates the tag but does not change project files or directories. Use `-ProjectPath`
to select a different existing project directory.

The updater copies all released skill packages under `.agents/skills/`,
the reusable `AIAugmentation/templates/`, `AIAugmentation/README.md`,
`AIAugmentation/min_user_guide.md`, and the root `AGENTS.team.md` instruction
template. Both kit guides are overwritten on updates. The project root
`README.md` is preserved, including when installing older releases.
Older tags with a root `min_user_guide.md` install that file at its original
location. Existing root guides from earlier installations are not deleted.
Use this updated updater script for the new layout.

The updater also creates missing `Requirements/`, `Solution Design/`,
`Test Preparation/`, and `External Inputs/` folders under
`AIAugmentation/artifacts/ITER-001/`. Existing folders and their contents
are preserved; no sample files or placeholders are added. Select another
iteration with `-IterationId`:

```powershell
.\update-skill-kit.ps1 -Repository 'https://github.com/eslamgenio/AIAugmentedSDLC.git' -Version v1.0.8 -IterationId ITER-002
```

Iteration names must start with a letter or digit and contain only letters,
digits, underscores or hyphens. Only the selected iteration is scaffolded;
other iterations are untouched. `-WhatIf` reports missing folders to create.

It records the installed tag in `AIAugmentation/skill-kit-version.txt` after
copying and folder creation succeed.

It also installs `AIAugmentation/project_guides/` from the release, including
its README and any starter guides. Only missing files are added: existing
guide files are never overwritten, including on later upgrades. Older
releases without this folder remain supported.

Project guides, artifacts, root `AGENTS.md`, application
code, and skills whose folder names are absent from the release remain
untouched. Review changes to `AGENTS.team.md` and manually merge any relevant
updates into your project's `AGENTS.md`. Keep customizations in project
guides: files with matching names in the shared kit areas are overwritten.

Commit or back up local shared-file edits before upgrading. Review the diff,
run a representative creation-and-review example, then commit the update.
The updater never commits, pushes, or executes downloaded scripts. It does
not delete retired files or replace itself; follow release notes for removals
or a newer updater. If a copy fails, some shared files may already be updated;
fix the error and rerun. The version file is written only after all copies
and folder creation succeed.

For kit maintainers: commit the intended kit files and publish a version tag
(for example, `v1.2.0`) with release notes describing changes and any removals.
The tag must include `.agents/skills/`, `AIAugmentation/templates/`,
`AIAugmentation/README.md`, `AGENTS.team.md` and
`AIAugmentation/min_user_guide.md`. No separate ZIP asset is needed.
Treat published tags as fixed; publish a new version for subsequent changes.

For a first installation, copy the installed `AGENTS.team.md` to `AGENTS.md`
if none exists; otherwise merge the relevant instructions into the existing
file. Complete the project context below. Supply your own input artifacts
and optional project guides. The updater does not generate them or install
samples, the workbook, diagram, or supporting framework documents.

### Complete the project context

Replace placeholders with verified project information, remove optional
sections that do not apply, and do not include secrets. Keep the completed
context in the project's `AGENTS.md` so it is available during skill use.

- **Project identity:** supply the project name, purpose, intended users
  and components or features in scope.
- **Project directory map:** add a concise tree of relevant directories
  with their purposes. Use paths relative to the project root; omit
  dependencies and generated files.
- **Sources and working locations:** identify requirements, architecture
  documentation, source code and existing tests. Keep
  `AIAugmentation/artifacts/` as the artifact location or specify the
  project's chosen location. Set the active iteration or supply it in
  each task.
- **Project-specific instructions:** record terminology, domain rules,
  supported technologies and environments, naming conventions, relevant
  checks and commands, and access or data-handling constraints.

Keep shared project context in `AGENTS.md` and activity-specific details
in the corresponding project guide. Link to existing product and
architecture documentation rather than duplicating it. Unfilled fields
are missing information; they need not block work that can proceed using
the supplied inputs.

## Use the seven skills

| Skill | Inputs | Deliverable |
| --- | --- | --- |
| [elicit-requirements](../.agents/skills/elicit-requirements/SKILL.md) | Source material and stakeholder inputs | **A01:** elicitation record and open questions |
| [define-scope](../.agents/skills/define-scope/SKILL.md) | A01 and applicable constraints or decisions | **A02:** boundaries, exclusions and open scope decisions |
| [analyze-requirements](../.agents/skills/analyze-requirements/SKILL.md) | A01 and A02, with evidence | **A03:** analyzed requirements, conflicts and gaps |
| [define-acceptance-criteria](../.agents/skills/define-acceptance-criteria/SKILL.md) | A03 and applicable source records | **A04:** testable acceptance criteria and unresolved rules |
| [review-requirements](../.agents/skills/review-requirements/SKILL.md) | Exact A01–A04 revisions and relevant evidence | **A05:** reviewed baseline or source pointers, findings and readiness recommendation |
| [create-test-cases](../.agents/skills/create-test-cases/SKILL.md) | Requirements, acceptance criteria and relevant context; prior cases and feedback for revisions | **A16:** test cases, setup/data summary, questions and automation candidates |
| [review-test-coverage](../.agents/skills/review-test-coverage/SKILL.md) | The same requirements and candidate cases; prior findings for re-review | **A17:** coverage matrix, gaps, duplicates and actionable findings |

User guides: [Create test cases](../.agents/skills/create-test-cases/README.md) · [Review test coverage](../.agents/skills/review-test-coverage/README.md). Each guide explains inputs, prompts, outputs, statuses and revision handling.

Example requests (run from your project root; replace bracketed placeholders):

```text
Use $elicit-requirements with [provided sources] for [iteration]. Keep unknowns open.

Use $review-requirements with [pinned A01–A04 revisions]. Flag blockers and pending approvals.

Use $create-test-cases with [requirements file or folder].

Use $review-test-coverage with [requirements file or folder] and [A16 file].

Use $create-test-cases to revise [A16 file] using [A17 file].
```

Supply your own requirements and acceptance criteria using existing filenames
or text. A05 can embed the baseline or reference an accessible source. Use the
configured artifact location; the default is `AIAugmentation/artifacts/<iteration_id>/`.

Optional practice materials live under `AIAugmentation/dummy/` in the full library
repository, with instructions in its README. The updater does not install this
folder. Samples are not required for normal skill use. Keep sample baselines
unchanged if you download them separately.

The packages live in `.agents/skills/` for this project. If the current session has not picked them up, explicitly ask to read and use the linked `SKILL.md` file. Each package is self-contained and can be copied to another project's `.agents/skills/` folder.

Use each matching template for the canonical Markdown handoff; alternate views do not replace it. They need no Python setup. Missing behavior becomes a question rather than an invented expected result. These skills design and review tests; they do not execute application tests or grant human approval.

The documents preserve the catalog's A16/A17 names and child IDs. The reviewer may recommend READY with disclosed nonblocking suggestions; unresolved blocking issues require correction or clarification.

### Optional project-specific guides

The skills are project-agnostic. A project may add supplemental instructions under [project_guides](project_guides/README.md) using `<skill-name>-guide.md`. For example, `AIAugmentation/project_guides/create-test-cases-guide.md` is loaded by `create-test-cases` when present. No guide is required for the generic workflow.

## Artifact folders and handoffs

For new iterations using phase layout, organize artifacts by iteration,
then by the producer's phase from the workbook's **Skill Artifact Flow**
sheet. The table below records that mapping so using the kit does not
require a local copy of the workbook.

| Phase folder | Skill output bundles |
| --- | --- |
| Requirements | A01–A05 |
| Solution Design | A06–A10 |
| Delivery Planning | A11–A14 |
| Test Preparation | A15–A19 |
| Development | A20–A23 |
| Build And Integration | A24–A27 |
| Test Execution | A28–A33 |
| Defect Resolution | A34–A36 |
| Acceptance And Release | A37–A41, A45 |
| Production And Feedback | A42–A44 |

For skills with an `Also:` phase in the sheet, use the first-listed phase
as the default storage location and reference that artifact from other
phases. A project may explicitly configure another location. Folder order
does not authorize skill execution or imply that a phase is complete.

```text
AIAugmentation/artifacts/ITER-001/
├── Requirements/
│   ├── A04_acceptance-criteria-outputs_ITER-001_v1.0.md
│   └── A05_requirements-review-outputs_ITER-001_v1.0.md
├── Solution Design/
│   └── A06_feasibility-assessment-outputs_ITER-001_v1.0.md
├── Delivery Planning/
├── Test Preparation/
│   ├── A16_test-case-creation-outputs_ITER-001_v1.0.md
│   └── A17_test-coverage-review-outputs_ITER-001_v1.0.md
└── External Inputs/
    └── E06_test-and-defect-baselines_ITER-001_v1.0.md
```

Create folders only when needed. `External Inputs/` is the kit's convention
for E01–E10 external/human input bundles, not an additional lifecycle phase
from the sheet. Explicit source links outside that folder remain valid.

Use the sheet's **Input artifacts** to identify a skill's dependencies and
**Output artifacts** to identify its result. Locate inputs across the active
iteration's root and subfolders by artifact ID and compatible version, and
record exact paths. Reference original files instead of copying them into
each consuming phase. Honor conditional inputs for revisions and re-review;
do not make optional evidence mandatory merely because it appears in the sheet.
Flag duplicate artifact/version candidates and conflicting baselines rather
than choosing silently. Use another iteration only through an explicit input
or baseline reference.

For example, `create-test-cases` reads A04/A05 from `Requirements/`, available
A06/A09 from `Solution Design/`, A15 from `Test Preparation/`, and relevant
external inputs; it writes A16 under `Test Preparation/`. `review-test-coverage`
reads that A16 with the same source baseline and writes A17 in the same phase.
Their required and optional input rules remain unchanged.

Set the layout in the project's instruction file. Existing flat iteration
folders remain supported; standalone skills default to the flat layout if
no layout is configured. Explicit output paths take precedence, followed
by the prior artifact's folder for revisions, then the configured layout.
Do not move existing artifacts automatically. Preserve `.md` filenames,
IDs and version conventions. The implemented skills are A01–A05 and A16/A17;
the phase map also covers proposed skills.

## Artifact templates

The [templates index](templates/README.md) links to a template for every catalog artifact: **45 skill output bundles and 10 external input bundles**, including all **135 child deliverables** as sections. Each includes source references, required content, acceptance checks and revision history.

Skills read the matching template, fill it with sourced content, and save the result under `AIAugmentation/artifacts/<iteration_id>/` using the canonical basename plus iteration and version, with a phase subfolder when configured. All seven implemented skills use their matching templates. For example, with phase layout the A16 template becomes `AIAugmentation/artifacts/ITER-001/Test Preparation/A16_test-case-creation-outputs_ITER-001_v1.0.md`; without a configured layout, it remains directly in `ITER-001/`.

The canonical handoff uses Markdown with the template's nine YAML front matter keys, stable sections and exact upstream versions. Do not emit a parallel JSON payload or manifest. Native deliverables such as code, datasets and build packages are linked from the document. Empty templates do not represent completed work or approvals.

## Optional framework reference

The full library repository includes `AIAugmentation/docs/framework-reference.md`
for the workbook walkthrough, proposed artifact contracts, and lifecycle diagram.
This reference and its supporting resources are not installed by the updater
and are not required for normal skill use.
