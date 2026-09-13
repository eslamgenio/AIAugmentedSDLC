# AI Augmented SDLC

A proposed approach to using AI throughout the software development lifecycle. The main deliverable is an editable workbook describing **45 proposed skills** and their **48 activity or decision-gate associations**.

The catalog and roadmap describe the wider proposed framework. The first two skills now have callable pilot adapters; they are not installed Codex skill packages. Human owners retain test-exit and release decisions.

## First connected pilot

The [test design pilot specification](docs/pilot/SPECIFICATION.md) defines a connected workflow: create test cases, review coverage, apply bounded corrections and request human approval. Local artifact storage, structural/semantic handoff validators, the [shipping correctness evaluator](docs/pilot/EVALUATION.md), and the [creator-to-reviewer adapters](docs/pilot/AGENT-HANDOFF.md) are implemented. The adapters can make two real model calls, pass the saved A16 to the reviewer, validate A17 and stop before human approval. See [setup and usage](docs/pilot/IMPLEMENTATION.md) and the [pilot file guide](docs/pilot/README.md). The durable controller for corrections, recovery and approval remains to be implemented.

## Read the workbook

Download [SDLC_Proposed_Skills_Catalog.xlsx](SDLC_Proposed_Skills_Catalog.xlsx) and open it in Microsoft Excel. Start with **Overview**, then explore the other sheets:

| Sheet | What it contains | How to use it |
| --- | --- | --- |
| **Overview** | A summary of the workbook, its scope and key counts. | Get the big picture before reviewing individual skills. |
| **Skills Catalog** | All 45 proposed skills, with descriptions, inputs and outputs. | Understand what each skill would do and what information it would need and produce. |
| **Activity Mapping** | The 48 associations between lifecycle phases, activities or decision gates, and proposed skills. | Find where a skill would support the lifecycle. Some skills appear in more than one association. |
| **Implementation Roadmap** | All 45 skills in a proposed implementation order, grouped into waves, with rationale, prerequisites and a first validation milestone. | Review priorities and dependencies when deciding what to implement first. |
| **Artifact Handoff Mapping** | All 135 catalog input definitions mapped to their sources, plus 55 proposed artifact contracts covering skill outputs and external inputs. | Filter by consumer skill, look up source artifact IDs in the contract table, and review required fields, acceptance checks, approval gates and rework rules. |

Use the table filters in Skills Catalog, Activity Mapping and Implementation Roadmap to focus on relevant entries. Each skill appears once in the catalog and once in the roadmap; the mapping sheet shows its use across activities and gates.

Artifact Handoff Mapping defines a proposed flow of deliverables between skills. It includes external evidence and human decisions, with conditional paths for defects, rejected releases and the next iteration. The pilot adds JSON schema profiles for its input package, A16, A17 and run record. The remaining contracts, connectors and workflow orchestration are still design work.

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

The JSON file is an exchange record or manifest: it can contain the deliverable or link to native code, documents and other files using an artifact URI and checksum. Child deliverables may be embedded in their parent bundle or stored separately. The parent manifest lists their IDs and versions, and consumers reference exact upstream versions. The pilot implements these conventions for A16 and A17; the remaining artifact implementations are still proposed. Checked-in examples are synthetic; generated model outputs are saved separately under ignored `outputs/`.

## Lifecycle diagram

- [SDLC.png](SDLC.png): the lifecycle diagram for visual reference alongside the workbook.
- [docs/sdlc-source.mmd](docs/sdlc-source.mmd): the Mermaid source for the diagram.
