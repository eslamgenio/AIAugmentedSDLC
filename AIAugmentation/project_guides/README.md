# Project-specific skill guides

Use this folder for optional project-specific instructions that supplement the generic skills under `.agents/skills/`.

Name each guide after the skill with `-guide` appended:

```text
<skill-name>-guide.md
```

Examples for the current skills:

- `create-test-cases-guide.md`
- `review-test-coverage-guide.md`

Each skill checks for its matching guide before performing its work. If the file is absent, the skill continues with its generic instructions.

A guide may define project-specific source locations, terminology, domain rules, identifiers, required checks, output conventions or other local defaults. Keep generic behavior in the skill itself. A project guide may specialize a generic default, but it must not override higher-priority instructions, the user's explicit request, authorization boundaries or fixed activity boundaries such as test design versus test execution.

## New skill checklist

When adding a skill:

1. Keep the reusable `SKILL.md` project-agnostic.
2. Derive the optional guide name from the skill's frontmatter `name` using `AIAugmentation/project_guides/<skill-name>-guide.md`.
3. Add an explicit lookup for that exact path near the start of `SKILL.md`; continue with the generic workflow when the guide is absent.
4. Create the guide file only when the project needs additional instructions. Do not add empty guide placeholders.
5. Validate the skill structure and confirm that the pointer name matches the frontmatter name exactly. The optional target does not need to exist.
