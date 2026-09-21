## Project conventions

- Write project deliverables in English.
- Keep skill names, artifact IDs, canonical names and handoffs consistent with `AIAugmentation/README.md`.
- Keep reusable skills project-agnostic and self-contained under `.agents/skills/`.
- Every `.agents/skills/<skill-name>/SKILL.md` must check for the optional project guide `AIAugmentation/project_guides/<skill-name>-guide.md` before performing its work. Derive `<skill-name>` from the skill's frontmatter `name`. If the guide is absent, continue with the generic workflow. A guide may specialize defaults but must not override higher-priority instructions, the user's explicit request, authorization boundaries or the skill's fixed activity scope.
- Before producing an SDLC artifact, read its matching template in `AIAugmentation/templates/` and follow its required content and child IDs. Use `AIAugmentation/templates/README.md` to locate it. Keep reusable templates in `AIAugmentation/templates/` and completed artifacts in the active iteration folder.
- Replace template placeholders with sourced content or explicit missing-information notes. Link native deliverables and evidence; never treat a filled template as proof of execution or human approval. A user-requested format takes precedence while retaining required content.
- Preserve existing test and finding IDs during revisions; increment artifact versions when content changes.
- Flag unclear requirements instead of inventing expected behavior. Distinguish test design, review recommendations, test execution and human approval.
- Store all SDLC input and output artifacts in a separate folder per iteration, such as `AIAugmentation/artifacts/ITER-001/` and `AIAugmentation/artifacts/ITER-002/`, unless the user explicitly requests another location.
- Keep each iteration's requirements, supporting inputs, generated documents and revisions together in its folder. Match artifact iteration IDs and filenames to that folder.
- Save corrections as new artifact versions within the same iteration folder. Use a new iteration folder for the next iteration and preserve prior iterations.
- Keep temporary files and local dependencies separate from deliverable artifacts and out of Git.

## Verify and deliver

- Report what was delivered, what was checked and any material limitation. Keep explanations concise.
- Commit or push only when the user requests it.