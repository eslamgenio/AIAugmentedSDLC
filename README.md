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

## Documentation

- [Install or update the kit](AIAugmentation/README.md#install-or-update-the-kit)
- [Configure project context](AIAugmentation/README.md#complete-the-project-context)
- [Customize individual skills with project guides](AIAugmentation/project_guides/README.md)
- [Artifact templates](AIAugmentation/templates/README.md)
- [Artifact storage and handoffs](AIAugmentation/README.md#artifact-folders-and-handoffs)
