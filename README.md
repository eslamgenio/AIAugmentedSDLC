# AI Augmented SDLC

Proposed AI capabilities for an end-to-end software development lifecycle. This repository documents 45 unique proposed skills and their 48 activity or decision-gate associations. It contains specifications and an implementation roadmap, not installed or implemented AI skills. Human owners retain test-exit and release decisions.

## Deliverables and sources

- `SDLC_Proposed_Skills_Catalog.xlsx`: the editable English workbook, with Skills Catalog, Activity Mapping, Implementation Roadmap and Overview sheets. The roadmap includes all 45 skills once.
- `SDLC.png`: the exported lifecycle diagram.
- `docs/sdlc-source.mmd`: the Mermaid definition of the [SDLC diagram](https://app.excalidraw.com/s/2TPnfMpA2su/3X97mNAJXN5), preserving the proposed skill names and activity mappings.
- `data/skill-details.json`: proposed descriptions, inputs and outputs.
- `data/implementation-roadmap.json`: proposed implementation sequence, rationale, prerequisites and first validation milestones.
- `scripts/`: workbook builder, text measurement and validation scripts.
- `outputs/support/`: local generated workbooks, previews and validation evidence. This directory and all `node_modules` directories or junctions are ignored by Git.

## Prerequisites

Regeneration uses the Codex desktop bundled artifact runtime, not a general npm installation. The verified bundle is `26.909.11814`, with its Node.js, `@oai/artifact-tool`, Python and Pillow packages. Ask Codex to load workspace dependencies to locate the installed bundle. Windows Arial fonts are required for text measurement. The optional native Excel check additionally requires desktop Microsoft Excel and an interactive Windows logon session.

The commands below use the standard bundle location. If the dependency loader reports a different path, update `$runtimeRoot`. Run these commands from the project root in PowerShell:

```powershell
$runtimeRoot = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies'
$env:SDLC_RUNTIME_ROOT = $runtimeRoot
$nodeExecutable = Join-Path $runtimeRoot 'node\bin\node.exe'
$pythonExecutable = Join-Path $runtimeRoot 'python\python.exe'
$runtimeModules = Join-Path $runtimeRoot 'node\node_modules'

if (-not (Test-Path -LiteralPath '.\node_modules')) {
    New-Item -ItemType Junction -Path '.\node_modules' -Target $runtimeModules
}
```

Reuse an existing compatible dependency directory or junction. Do not replace it blindly or delete its external target. No runtime packages are committed or installed by this project.

## Validate and regenerate

Check the sources, counts and layout inputs without changing the workbook, then compare the existing final workbook against the tracked sources:

```powershell
& $nodeExecutable '.\scripts\build-catalog.mjs' --check
& $pythonExecutable '.\scripts\verify-content.py'
```

Generate a review copy and previews under ignored `outputs/support/`:

```powershell
& $nodeExecutable '.\scripts\build-catalog.mjs'
& $pythonExecutable '.\scripts\verify-content.py' --workbook 'outputs/support/SDLC_Proposed_Skills_Catalog.xlsx'
```

An existing output is protected. Use `--overwrite` only when you intend to replace that generated copy. Add `--skip-previews` to omit rendering. To replace the root deliverable after reviewing the generated copy, explicitly choose it:

```powershell
& $nodeExecutable '.\scripts\build-catalog.mjs' --output 'SDLC_Proposed_Skills_Catalog.xlsx' --overwrite
```

Regeneration uses the source-defined formatting; manual Excel edits are not imported back into the JSON sources or builder. Preserve any manual changes before replacing the root workbook.

The optional native Excel check opens the root workbook read-only, compares all detail cells, verifies filters and frozen panes, and checks whether row heights accommodate the text. It needs the expected-content file produced by `--check` or a build:

```powershell
& '.\scripts\verify-excel.ps1'
```

Use `-WorkbookPath 'outputs/support/SDLC_Proposed_Skills_Catalog.xlsx'` to check a generated review copy. Reports remain in ignored `outputs/support/`. Open the generated previews for a visual review before accepting a rebuilt deliverable.
