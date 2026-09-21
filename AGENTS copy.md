# SDLC skill usage instructions

Use the provided skills to produce and review SDLC artifacts.
When distributing this file to a team project, name it `AGENTS.md`
and place it in the project root.

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

- Store SDLC inputs and outputs in a separate folder per iteration,
  such as `AIAugmentation/artifacts/ITER-001/`, unless the user requests
  another location.
- Keep each iteration's requirements, supporting inputs, generated
  documents and revisions together.
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
