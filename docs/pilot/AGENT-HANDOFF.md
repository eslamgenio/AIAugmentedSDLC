# Creator-to-reviewer handoff

This implements the first two proposed skills as Python adapters: `create-test-cases` creates **A16, Test Case Creation Outputs**; `review-test-coverage` consumes that exact saved A16 and creates **A17, Test Coverage Review Outputs**. These are callable components of our framework, not installed Codex `SKILL.md` packages.

The workbook defines the wider SDLC. This implementation covers one first-pass handoff in the shipping test-design pilot. It does not implement the remaining skills or the durable correction controller.

## What happens

1. Validate the input baseline and its approval evidence. Synthetic input requires explicit fixture mode.
2. Send the requirements, criteria, rules, risks and case format to the creator in one model call.
3. Validate the returned test content. The framework supplies canonical bundle/child names, versions and source references, and derives the resource view from the cases. Save immutable A16.
4. Send the baseline and the exact saved A16 to a separate reviewer call. The creator's conversation is not reused.
5. Validate A17, including its current A16 digest, and save it. Run the independent shipping evaluator after review.
6. Stop at **AWAITING_APPROVAL** only when the reviewer recommends READY and the evaluator passes. Otherwise return **NEEDS_CORRECTION**, **BLOCKED**, or **FAILED**. No state grants human approval.

There are at most two model calls, with a configurable timeout per call and no automatic retries. Corrections, crash recovery, durable usage reservations and human approval submission are the next controller work. A failed call retains evidence; starting another handoff requires a fresh run identity or a separate store. The handoff report is an execution summary, not the specification's full `runRecord`.

## Run it

Prerequisites: the [Python setup](IMPLEMENTATION.md), an installed Codex CLI supporting the options below, and a working CLI sign-in. `codex login status` checks the sign-in. On Windows supply the native `codex.exe` path, not `codex.ps1` or `codex.cmd`. For an npm installation, it is normally beneath the package's `node_modules/@openai/codex-win32-x64/vendor/x86_64-pc-windows-msvc/bin/` directory.

```powershell
python -m sdlc_pilot handoff `
  --input docs/pilot/input.example.json `
  --store outputs/my-handoff/store `
  --evidence outputs/my-handoff/evidence `
  --codex-executable 'C:\path\to\codex.exe' `
  --fixture
```

The example uses a synthetic business baseline but makes real model calls. It consumes the signed-in account's model usage. No upstream producing skill or real human approval is claimed. The saved `agents_executed` field distinguishes real model calls from scripted regression tests.

Use `--model MODEL` to select a model, or omit it to use the CLI default. The provider skips user configuration to avoid automatically loading configured integrations; it does not inherit the desktop task's model selection. `model_requested` records the request, not an attestation of the serving model. `--timeout 240` sets a 240-second deadline per call; the supported range is 1–600 seconds.

For real input evidence, omit `--fixture`, provide the eight real upstream sources in the store and pass `--trusted-approval FILE` as described in the implementation guide. The correctness evaluator still supports only the pinned shipping profile. This command does not generalize the evaluator to arbitrary projects.

## Read the results

- `evidence/handoff-report.json`: stopping state, completed calls, exact artifact references, review recommendation and correctness results.
- `evidence/create-test-cases/` and `evidence/review-test-coverage/`: request, raw final response, event stream, diagnostic output, hashes and usage metadata.
- `store/objects/`: immutable input, A16 and A17. Use each report reference with `ArtifactStore.read(reference)` to verify its bytes before consumption.

An exit code of zero means the pair reached AWAITING_APPROVAL. It does not mean the pilot has human approval, the tests ran against software, or the full autonomous SDLC is complete. Other stopping states return a nonzero exit code. All generated run evidence remains under ignored `outputs/`.

## Boundaries and verification

Requests are built from an explicit field list. Creator requests contain no candidate fixture or oracle answers; reviewer requests contain only the current candidate and baseline context. The fixed steps/preconditions are public format requirements. The expected results are derived by the model, then checked independently.

The provider uses a fresh temporary working directory, ephemeral read-only execution, disables shell execution, web search, apps, memories and multi-agent tools, and skips user configuration. It reuses authentication through Codex itself without opening credential files. Any observed tool/action event or incomplete turn invalidates the response. This is a local trusted CLI integration, not an OS-enforced guarantee of evaluator confidentiality. Global or managed runtime behavior may still apply; do not use it as an adversarial holdout isolation system.

The CLI transport follows OpenAI's [non-interactive execution guide](https://learn.chatgpt.com/docs/non-interactive-mode) and [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference). No approval or sandbox bypass flags are used.

Regression tests use a clearly labeled scripted provider to check exact artifact handoff, false READY rejection, invalid model output, interrupted review, duplicate-run rejection, prompt contents, event rejection and timeout handling. They are separate from any recorded live model experiment.
