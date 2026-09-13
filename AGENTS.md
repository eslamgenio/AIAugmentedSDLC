# Project instructions

This project builds reusable LLM-agent skills for an end-to-end software development lifecycle. The current MVP focuses on creating test cases and reviewing coverage.

## Keep delivery simple

- Deliver the smallest useful working solution for the requested activity.
- Prefer clear skill instructions and existing tools. Add infrastructure only for a demonstrated need or an explicit request.
- Stay within the requested scope. Do not turn a skill task into a platform, workflow engine or broad production-readiness program.
- After the user approves a direction, carry it through to verification without repeatedly asking for confirmation. Ask only when missing information materially blocks progress.

## Project conventions

- Write project deliverables in English.
- Keep skill names, artifact IDs, canonical names and handoffs consistent with the Excel catalog and README.
- Keep reusable skills self-contained under `.agents/skills/`.
- Preserve existing test and finding IDs during revisions; increment artifact versions when content changes.
- Flag unclear requirements instead of inventing expected behavior. Distinguish test design, review recommendations, test execution and human approval.
- Save generated working outputs under `outputs/` unless the user specifies another location. Keep temporary files and dependencies out of Git.

## Verify and deliver

- Use checks proportional to the change. For skills, validate their structure and use a relevant example when behavior needs checking.
- Report what was delivered, what was checked and any material limitation. Keep explanations concise.
- Commit or push only when the user requests it.
