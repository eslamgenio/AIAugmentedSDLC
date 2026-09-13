# First real model handoff — 2026-09-13

Two real Codex CLI model calls completed using the synthetic shipping baseline: `create-test-cases` produced 14 cases in A16, and `review-test-coverage` consumed that exact stored A16 and produced A17 with recommendation READY. Both artifacts passed schema and handoff validation. The calls recorded no tool/action events.

The independent evaluator matched **9 of 13 fixed scenarios**. It found no incorrect expected results in the 14 cases, but four required exact inputs were absent. The framework stopped at **NEEDS_CORRECTION** despite the reviewer's READY recommendation. No human approval or application test execution occurred.

| Fixed scenario | What the model supplied | Interpretation |
| --- | --- | --- |
| Express subtotal 0 | Express 2500, 5000 and 5001 | The zero subtotal with express was absent |
| Express subtotal 4999 | Express 2500, 5000 and 5001 | Below-threshold express behavior was covered at another value |
| Fractional subtotal 1.5 with standard | Standard 4999.5 | Fractional rejection was covered with a different value |
| Unsupported method at subtotal 5000 | Overnight at subtotal 2500 | Unsupported-method rejection was covered with a different value |

This proves the real artifact handoff and the independent stop gate work. It does not establish that the generated cases are ready for approval. It also reveals that the evaluator's exact-input coverage is stricter than the written category-level coverage rules. Next, align that coverage policy without exposing expected oracle answers, then implement bounded correction and re-review in the durable controller. Do not weaken the gate silently or relabel this run as passed.

Local evidence: `outputs/agent-handoff-001/evidence/handoff-report.json`, with per-role requests, responses, event streams, usage and hashes alongside it. The artifact store is `outputs/agent-handoff-001/store/`. Those files are intentionally ignored by Git; this summary records the verified outcome.

| Artifact | SHA-256 |
| --- | --- |
| PILOT-INPUT | `7598774c8461d41d86f0a344955f34b6ddf24bc1ab65fad44df1abcf1d6f5b7f` |
| A16 | `9e9c7b83b5e492a23b05c7280e2f421dd6eef51422ed5897471d940157bc0576` |
| A17 | `d4906b5d37268a0e45c8aa3d6388c65f85bb68a619c72214c95ab3316b6f0bd3` |

The input was parsed and canonically serialized before storage, so its stored digest differs from the checked-in fixture file's raw-byte digest. Stored artifacts reference the stored input digest. The CLI's default model was used; a serving model identifier was not independently attested.
