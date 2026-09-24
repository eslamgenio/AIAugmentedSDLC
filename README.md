# AI Augmented SDLC

This repository proposes a set of AI agent skills for the software development lifecycle. The optional, separately supplied `SDLC_Proposed_Skills_Catalog.xlsx` describes 45 proposed skills and 48 activity or decision-gate associations. The workbook is not included in Git clones or updater installations and is not required to use the skills. The current working kit implements two skills: creating test cases (A16) and reviewing test coverage (A17).

To use the kit in a project, start with the [quick start](min_user_guide.md). The [detailed kit guide](AIAugmentation/README.md) covers setup, skill inputs and outputs, artifact folders, templates, and the catalog. The updater replaces root `README.md` and `min_user_guide.md` with the kit's versions; preserve any application-specific documentation elsewhere before updating.

The reusable skills are in [`.agents/skills/`](.agents/skills/), and the artifact templates are listed in the [templates index](AIAugmentation/templates/README.md). Human owners retain test-exit and release decisions.

To upgrade an embedded kit, copy [update-skill-kit.ps1](update-skill-kit.ps1)
into the target project and follow [the update instructions](AIAugmentation/README.md#install-or-update-the-kit).
