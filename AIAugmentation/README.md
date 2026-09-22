# AI Augmented SDLC

A proposed approach to using AI throughout the software development lifecycle. The main deliverable is an editable workbook describing **45 proposed skills** and their **48 activity or decision-gate associations**.

The catalog and roadmap describe the wider proposed framework. Two reusable project-local skills are available for creating test cases and reviewing coverage. Human owners retain test-exit and release decisions.

## Set up the kit in an existing project

Keep your project's existing root `README.md`. This file,
`AIAugmentation/README.md`, contains the kit's setup and usage guidance.
You may optionally link to it from your project README.

1. Copy the kit's skill folders into your project's `.agents/skills/` and
   its reusable resources into `AIAugmentation/`, retaining the relative
   paths. Include this README, `templates/` and `project_guides/`. Merge
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

The resulting project layout is:

```text
your-project/
├── README.md                  # Existing project documentation
├── AGENTS.md                  # Team instructions and project context
├── .agents/skills/            # Reusable skill packages
└── AIAugmentation/
    ├── README.md              # Kit setup and usage guidance
    ├── templates/             # Reusable artifact templates
    └── project_guides/        # Optional activity-specific conventions
```

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

## Use the two skills

| Skill | Inputs | Deliverable |
| --- | --- | --- |
| [create-test-cases](../.agents/skills/create-test-cases/SKILL.md) | Requirements, acceptance criteria and relevant context; prior cases and feedback for revisions | **A16:** test cases, setup/data summary, questions and automation candidates |
| [review-test-coverage](../.agents/skills/review-test-coverage/SKILL.md) | The same requirements and candidate cases; prior findings for re-review | **A17:** coverage matrix, gaps, duplicates and actionable findings |

User guides: [Create test cases](../.agents/skills/create-test-cases/README.md) · [Review test coverage](../.agents/skills/review-test-coverage/README.md). Each guide explains inputs, prompts, outputs, statuses and revision handling.

Example requests (run from the repository root):

```text
Use $create-test-cases with AIAugmentation/dummy/ITER-001/A05_requirements-review-outputs_ITER-001_v1.1.md.

Use $review-test-coverage with AIAugmentation/dummy/ITER-001/A05_requirements-review-outputs_ITER-001_v1.1.md and [A16 file].

Use $create-test-cases to revise [A16 file] using [A17 file].
```

`AIAugmentation/dummy/` is the canonical practice and reference area; treat its sample baselines as read-only. Use `AIAugmentation/dummy/ITER-001/` for the examples above and isolated practice runs. Use `AIAugmentation/artifacts/<iteration_id>/` for active iteration inputs and outputs.

The sample A05 v1.1 embeds the complete requirements baseline. Use the v1.1 supporting inputs in the same iteration; a separate requirements file is unnecessary. Both skills also accept requirements supplied under any other filename or as text. Earlier sample versions remain available for historical reference.

The packages live in `.agents/skills/` for this project. If the current session has not picked them up, explicitly ask to read and use the linked `SKILL.md` file. Each package is self-contained and can be copied to another project's `.agents/skills/` folder.

They default to readable Markdown bundles using the matching project template, and adapt to a supplied format. They need no Python setup. Missing behavior becomes a question rather than an invented expected result. These skills design and review tests; they do not execute application tests or grant human approval.

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
IDs and version conventions; no JSON conversion is needed. Only A16/A17
skills are currently implemented; the phase map also covers proposed skills.

## Artifact templates

The [templates index](templates/README.md) links to a template for every catalog artifact: **45 skill output bundles and 10 external input bundles**, including all **135 child deliverables** as sections. Each includes source references, required content, acceptance checks and revision history.

Skills read the matching template, fill it with sourced content, and save the result under `AIAugmentation/artifacts/<iteration_id>/` using the canonical basename plus iteration and version, with a phase subfolder when configured. The two implemented skills use the A16 and A17 templates automatically in this project. For example, with phase layout the A16 template becomes `AIAugmentation/artifacts/ITER-001/Test Preparation/A16_test-case-creation-outputs_ITER-001_v1.0.md`; without a configured layout, it remains directly in `ITER-001/`.

The templates use Markdown; the workbook's JSON exchange manifests remain proposed. Native deliverables such as code, datasets and build packages are linked from the document. Empty templates do not represent completed work or approvals.

## Read the workbook

Download [SDLC_Proposed_Skills_Catalog.xlsx](../SDLC_Proposed_Skills_Catalog.xlsx) and open it in Microsoft Excel. Start with **Overview**, then explore the other sheets:

| Sheet | What it contains | How to use it |
| --- | --- | --- |
| **Overview** | A summary of the workbook, its scope and key counts. | Get the big picture before reviewing individual skills. |
| **Skills Catalog** | All 45 proposed skills, with descriptions, inputs and outputs. | Understand what each skill would do and what information it would need and produce. |
| **Activity Mapping** | The 48 associations between lifecycle phases, activities or decision gates, and proposed skills. | Find where a skill would support the lifecycle. Some skills appear in more than one association. |
| **Implementation Roadmap** | All 45 skills in a proposed implementation order, grouped into waves, with rationale, prerequisites and a first validation milestone. | Review priorities and dependencies when deciding what to implement first. |
| **Artifact Handoff Mapping** | All 135 catalog input definitions mapped to their sources, plus 55 proposed artifact contracts covering skill outputs and external inputs. | Filter by consumer skill, look up source artifact IDs in the contract table, and review required fields, acceptance checks, approval gates and rework rules. |

Use the table filters in Skills Catalog, Activity Mapping and Implementation Roadmap to focus on relevant entries. Each skill appears once in the catalog and once in the roadmap; the mapping sheet shows its use across activities and gates.

Artifact Handoff Mapping defines a proposed flow of deliverables between skills. It includes external evidence and human decisions, with conditional paths for defects, rejected releases and the next iteration. The two skills implement test creation and review using readable A16/A17 documents. Machine-readable contracts, connectors and workflow orchestration remain design work.

### How to use Artifact Handoff Mapping

An **artifact** is a deliverable, such as requirements, test cases, code or a report. Its **contract** defines the expected format, required fields and acceptance checks. The **producer** supplies the artifact; the **consumer** uses it as an input.

The sheet contains three tables:

- **Input handoffs**, at the top, map each skill's required inputs to their sources and explain when to proceed or request corrections.
- **Artifact contracts**, below, describe each deliverable and reference the handoff rows that consume it.
- **Artifact naming register**, at the bottom, assigns stable child IDs, canonical names and filename patterns to all 135 catalog output lines. Bundle names and filename patterns are in columns I-J of Artifact contracts.

IDs connect the tables: **H** identifies an input handoff, **A** identifies a skill's output bundle, and **E** identifies an external source, such as a business owner or approval record. These IDs are lookup references, not implementation priorities. **Input 1, 2 and 3** correspond to the three lines in the skill's Inputs cell in Skills Catalog.

1. Filter **Consumer Skill** to the skill you want to understand.
2. Read each **Required Input** and look up its **Source Artifact IDs** in the contract table. Multiple sources normally combine to satisfy the input; they are alternatives only when the flow rule says so.
3. Check **Start / Rework Rule** and **Acceptance Checks**. A conditional source applies only on the stated path, such as defect rework or a later iteration.
4. If evidence is missing or unacceptable, follow **Missing / Rejected Action** to request correction. A failed test result can still be valid evidence for defect triage; it does not authorize passing an approval gate.

**Example: creating and reviewing test cases.** Filter to `create-test-cases`. Its three input handoffs, **H046–H048**, combine reviewed requirements and acceptance criteria with human agreement, testing strategy, risks, design specifications, a test template and domain rules. The skill produces **A16**, which contains requirement-linked test cases, preconditions, data needs, expected results and automation candidates. Look up A16's contract to see its required fields and checks, including unique test IDs and explicit expected results. Then filter to `review-test-coverage`: it consumes A16 alongside requirements, acceptance criteria, risks and coverage rules, and produces **A17**, containing the traceability matrix, coverage gaps and review findings. Revision actions can send the cases back for correction and another review.

**Consistent artifact names.** A16 is the **Test Case Creation Outputs** bundle. Its first child, **A16-01**, is **Requirement-linked test cases and scenarios**. Its filename pattern is `A16-01_requirement-linked-test-cases-and-scenarios_{iteration_id}_v{artifact_version}.json`, for example `A16-01_requirement-linked-test-cases-and-scenarios_ITER-001_v1.0.json`. Keep IDs and canonical names stable, increment the artifact version when content changes, and never renumber or reuse an ID. Track the payload's schema version separately.

The JSON file is an exchange record or manifest: it can contain the deliverable or link to native code, documents and other files using an artifact URI and checksum. Child deliverables may be embedded in their parent bundle or stored separately. The parent manifest lists their IDs and versions, and consumers reference exact upstream versions. The two skills use the same A16/A17 identities in Markdown documents, with a `.md` extension. JSON exchange manifests remain a proposed convention. Generated documents are saved under `AIAugmentation/artifacts/` by default.

## Lifecycle diagram

- [SDLC.png](../SDLC.png): the lifecycle diagram for visual reference alongside the workbook.
- [docs/sdlc-source.mmd](docs/sdlc-source.mmd): the Mermaid source for the diagram.
