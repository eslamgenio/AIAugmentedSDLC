# Connected test design pilot

Start with [the pilot specification](SPECIFICATION.md). It defines the first connected workflow, its autonomy limits, artifact profiles, state transitions, acceptance criteria and evaluation plan.

| File | Purpose |
| --- | --- |
| [contracts.schema.json](contracts.schema.json) | JSON Schema 2020-12 definitions for pilotInput, creationBundle, reviewBundle and runRecord |
| [input.example.json](input.example.json) | Synthetic shipping requirements and normalized upstream context |
| [creation.example.json](creation.example.json) | A16 bundle with 13 test cases and the three named children |
| [review.example.json](review.example.json) | A17 traceability and review example referencing the candidate's actual file digest |
| [run.example.json](run.example.json) | Illustrative pending-approval run snapshot; not an execution log |
| [evaluation-cases.json](evaluation-cases.json) | Evaluator-only expected results for the 13 mandatory scenarios |
| [creation.wrong-threshold.example.json](creation.wrong-threshold.example.json) | Structurally valid negative example that wrongly gives free standard shipping at 4999 cents |

All examples are synthetic. No upstream skills ran and no real human approval is asserted. The eight upstream source digests in the input example are zero placeholders for a fixture adapter; live validation must reject those unresolved references. A16, A17 and the run snapshot contain real digests of the example files they reference. If an example file changes, update dependent digests too.

Select the relevant definition under `$defs` when validating a payload. The top-level schema also accepts exactly one of the four profiles. Enable date-time format checking. The field maps for feature-specific data are intentionally open; explicitly defined record fields are closed.

Schema checks cannot prove behavior, correct references, human authority or complete coverage. The deliberately incorrect candidate must pass structural validation but fail the evaluator's threshold check. Its review must be regenerated for its own digest; the correct example review cannot be reused.

The local artifact store, structural/semantic handoff validators, shipping correctness evaluator and [creator-to-reviewer adapters](AGENT-HANDOFF.md) are implemented. See [setup and usage](IMPLEMENTATION.md), [the evaluation guide](EVALUATION.md) and [the handoff guide](AGENT-HANDOFF.md). This folder contains contracts and examples; implementation code lives in `sdlc_pilot/`. There is no installed Codex skill package or durable autonomous controller yet.
