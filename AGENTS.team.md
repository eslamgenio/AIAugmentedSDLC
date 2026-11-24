# SDLC skill usage instructions

Use the provided skills to produce and review SDLC artifacts.

## Project context

Treat unfilled placeholders as missing information, not facts or literal
paths. Continue with available inputs and ask only when missing information
is necessary to perform the requested work. Project context may specialize
defaults but must not override higher-priority instructions, explicit user
requests, authorization boundaries or the selected skill's fixed scope.

### Project identity

- Project name: <name>
- Purpose: <what the product does and who uses it>
- Scope: <components or features covered by these skills>

### Project directory map

```text
<Insert the project's relevant directory tree and directory descriptions here>
```

### Sources and working locations

- Requirements and acceptance criteria: <paths or links>
- Architecture and domain documentation: <paths or links>
- Application source code: <paths>
- Existing tests: <paths>
- SDLC artifacts: `AIAugmentation/artifacts/`
- Artifact layout: phase folders within each iteration (flat iteration folders remain supported)
- Active iteration: <iteration ID, or specify it in each task>

### Project-specific instructions

- Terminology and domain rules: <details or references>
- Relevant technologies and supported environments: <details>
- Naming and identifier conventions: <details>
- Required checks or commands: <commands and when they apply>
- Access, data-handling or authorization constraints: <details>

## Scope and working approach

- Follow the skill matching the requested activity.
- Stay within the requested scope. Do not automatically start another
  activity, correction loop, test execution or external publication.
- Do not modify reusable skills or templates as a side effect of using
  them. Report improvement suggestions separately unless maintenance
  is explicitly requested.
- Continue approved work through verification. Ask only when missing
  information materially blocks progress.
- Write deliverables in English.

## Inputs, guides and templates

- Read the selected skill's instructions.
- Check for its optional project guide at
  `AIAugmentation/project_guides/<skill-name>-guide.md`, using the skill's
  frontmatter `name`. If absent, continue with the generic workflow.
- Apply relevant guide defaults without overriding higher-priority
  instructions, explicit user requests, authorization boundaries or
  the skill's fixed activity scope.
- Identify the active iteration and exact input files and versions.
  Do not silently mix incompatible baselines.
- Keep artifact IDs, canonical names and handoffs consistent with
  `AIAugmentation/README.md` and the selected skill.
- Before producing an artifact, locate its matching template through
  `AIAugmentation/templates/README.md` and follow its required content
  and child IDs.
- A user-requested format takes precedence while retaining required
  content. If project templates are unavailable, follow the selected
  skill's documented fallback.
- Replace placeholders with sourced content or explicit
  missing-information notes.
- Flag unclear requirements instead of inventing expected behavior.

## Artifact storage and revisions

- Use relative Markdown links for artifacts within the project. Resolve
  links from the containing document's folder and verify that targets
  exist before delivery. When moving artifacts, update affected incoming
  and outgoing links. Avoid machine-specific absolute paths for project files.
- Store SDLC inputs and outputs in a separate folder per iteration,
  such as `AIAugmentation/artifacts/ITER-001/`. Use the artifact location
  specified in the project context when configured; an explicitly
  requested location takes precedence.
- Keep each iteration's requirements, supporting inputs, generated
  documents and revisions together under its iteration folder.
- For phase layout, use the phase-to-artifact mapping in
  `AIAugmentation/README.md`, derived from the catalog's Skill Artifact Flow
  sheet. Save outputs in their producer's phase folder: A01–A05 in
  `Requirements/` and A16/A17 in `Test Preparation/`. Create folders only when needed.
- Keep external/human input bundles (E01–E10) in `External Inputs/` within
  the iteration, or reference their explicitly supplied source locations.
- Find required inputs in the active iteration root and its subfolders,
  including other phases and `External Inputs/`. Record exact source paths
  and versions; reference originals rather than duplicating them per phase.
- Respect explicit input paths and version choices. Do not search other
  iterations for replacements unless explicitly supplied or referenced.
  Flag duplicate candidates for the same artifact/version or conflicting
  baselines; resolve essential ambiguity before choosing.
- Keep existing flat iteration folders working and do not relocate prior
  artifacts automatically. For revisions, keep the prior artifact's folder
  unless another output location is explicitly requested.
- Use the matching template for each canonical Markdown (`.md`) handoff.
  Keep the nine YAML front matter keys, stable sections and IDs, and exact
  upstream artifact paths and versions. Pin a digest where the skill requires
  one. Do not emit a parallel JSON artifact or manifest. Keep native evidence
  in its original format and link to it.
- Match artifact iteration IDs and filenames to the iteration folder.
- Preserve source files and previous artifact versions.
- Save corrections as new versions in the same iteration folder.
  Use a new folder for a new iteration.
- Preserve existing test and finding IDs during revisions; increment
  artifact versions when content changes.
- Keep temporary files and local dependencies separate from deliverables
  and out of Git.

## Verify and deliver

- Perform the selected skill's output checks and verify required content,
  IDs, references and version consistency.
- Distinguish test design, review recommendations, test execution
  and human approval.
- Never treat a completed template or READY recommendation as proof
  of executed tests or human approval.
- Link native deliverables and supporting evidence.
- Report what was delivered, what was checked, unresolved questions
  and material limitations. Keep explanations concise.
- Commit or push only when the user requests it.
