# Optional SDLC framework reference

This document explains the broader proposed framework, workbook, and diagram.
It is available in the full library repository and is not installed by the
updater. None of these resources is required to use the implemented skills.
For practical setup and usage, see the [kit guide](../README.md).

## Read the workbook

If the maintainer supplies `SDLC_Proposed_Skills_Catalog.xlsx` separately, open it in Microsoft Excel. The workbook is optional and excluded from Git and updater installations. Start with **Overview**, then explore the other sheets:

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

**Consistent artifact names.** A16 is the **Test Case Creation Outputs** bundle. Its first child, **A16-01**, is **Requirement-linked test cases and scenarios**. Its filename pattern is `A16-01_requirement-linked-test-cases-and-scenarios_{iteration_id}_v{artifact_version}.md`, for example `A16-01_requirement-linked-test-cases-and-scenarios_ITER-001_v1.0.md`. Keep IDs and canonical names stable, increment the artifact version when content changes, and never renumber or reuse an ID. Track the payload's schema version separately.

The canonical exchange artifact is a readable Markdown document, with a heading, shared metadata and clearly labeled deliverable and evidence sections. Preserve artifact ID, iteration, artifact and schema versions, ownership, timestamp, status, and exact upstream revisions. Child deliverables may be embedded under their IDs or linked as separate Markdown documents with their versions. Link native code, documents and other evidence by path or URI and exact revision or checksum where applicable; do not convert native evidence. Existing legacy JSON inputs may be read when explicitly provided, but do not emit or require JSON for a new canonical artifact. Generated documents are saved under `AIAugmentation/artifacts/` by default.

## Lifecycle diagram

The optional `SDLC.png` is supplied separately and excluded from Git and updater installations. Its Mermaid source, `AIAugmentation/docs/sdlc-source.mmd`, is available in the full library repository but is not installed by the updater. Neither is required for skill use.
