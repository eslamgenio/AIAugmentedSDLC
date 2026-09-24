#Requires -Version 5.1
# Offline integration test: real Git tags, temporary source and destination.
$ErrorActionPreference = 'Stop'
$kitRoot = Split-Path -Parent $PSScriptRoot
$sandbox = Join-Path $kitRoot ('outputs/updater-test-' + [guid]::NewGuid().ToString('N'))
$source = Join-Path $sandbox 'source'
$target = Join-Path $sandbox 'project with spaces'
[IO.Directory]::CreateDirectory($source) | Out-Null
[IO.Directory]::CreateDirectory($target) | Out-Null
function Write-File($root, $path, $content) {
    $full = Join-Path $root $path
    [IO.Directory]::CreateDirectory((Split-Path -Parent $full)) | Out-Null
    [IO.File]::WriteAllText($full, $content)
}
function Assert($condition, $message) {
    if (-not $condition) { throw "FAIL: $message" }
}
function Invoke-FixtureGit($arguments) {
    & git -C $source @arguments | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Fixture Git command failed: $arguments" }
}
function Snapshot {
    return ((Get-ChildItem -LiteralPath $target -Recurse -File -Force | Sort-Object FullName | ForEach-Object {
        $_.FullName + ':' + (Get-FileHash -LiteralPath $_.FullName).Hash
    }) -join "`n")
}
Write-File $source '.agents/skills/create-test-cases/SKILL.md' 'creator v1'
Write-File $source '.agents/skills/review-test-coverage/SKILL.md' 'reviewer v1'
Write-File $source 'AIAugmentation/templates/README.md' 'templates v1'
Write-File $source 'AIAugmentation/README.md' 'guide v1'
Write-File $source 'AGENTS.team.md' 'shared instructions v1'
Write-File $source 'README.md' 'kit README v1'
Write-File $source 'min_user_guide.md' 'quick start v1'
Write-File $source 'AGENTS.md' 'must not copy'
Write-File $source 'AIAugmentation/project_guides/create-test-cases-guide.md' 'must not copy'
Write-File $source 'AIAugmentation/project_guides/README.md' 'guide instructions v1'
Write-File $source 'AIAugmentation/project_guides/review-test-coverage-guide.md' 'starter guide v1'
Write-File $source 'AIAugmentation/artifacts/sample.md' 'must not copy'
Invoke-FixtureGit @('init', '--quiet')
Invoke-FixtureGit @('add', '.')
Invoke-FixtureGit @('-c', 'user.name=Updater Test', '-c', 'user.email=updater@example.invalid', 'commit', '--quiet', '-m', 'fixture v1')
Invoke-FixtureGit @('tag', 'v1.0.0')
$protected = @('AGENTS.md', 'AIAugmentation/project_guides/create-test-cases-guide.md',
    'AIAugmentation/artifacts/ITER-001/test.md', '.agents/skills/unrelated/SKILL.md', 'src/app.py')
foreach ($path in $protected) { Write-File $target $path 'project-owned content' }
Write-File $target 'README.md' 'previous README'
$updater = Join-Path $kitRoot 'update-skill-kit.ps1'
$before = Snapshot
& $updater -Version v1.0.0 -Repository $source -ProjectPath $target -WhatIf
Assert ((Snapshot) -eq $before) 'WhatIf changed project files'
& $updater -Version v1.0.0 -Repository $source -ProjectPath $target
Assert ((Get-Content -LiteralPath (Join-Path $target 'AIAugmentation/skill-kit-version.txt') -Raw).Trim() -eq 'v1.0.0') 'initial version'
Assert ((Get-Content -LiteralPath (Join-Path $target 'README.md') -Raw) -eq 'kit README v1') 'root README not replaced'
Assert ((Get-Content -LiteralPath (Join-Path $target 'min_user_guide.md') -Raw) -eq 'quick start v1') 'quick start not installed'
Write-File $source 'README.md' 'kit README v2'
Write-File $source 'min_user_guide.md' 'quick start v2'
Assert ((Get-Content -LiteralPath (Join-Path $target 'AIAugmentation/project_guides/README.md') -Raw) -eq 'guide instructions v1') 'guide README missing'
Assert ((Get-Content -LiteralPath (Join-Path $target 'AIAugmentation/project_guides/review-test-coverage-guide.md') -Raw) -eq 'starter guide v1') 'starter guide missing'
Write-File $target 'AIAugmentation/project_guides/review-test-coverage-guide.md' 'team customized guide'
Write-File $source 'AIAugmentation/project_guides/review-test-coverage-guide.md' 'starter guide v2'
Write-File $source 'AIAugmentation/project_guides/new-feature-guide.md' 'new guide'
Write-File $source '.agents/skills/create-test-cases/SKILL.md' 'creator v2'
Write-File $source '.agents/skills/new-feature/SKILL.md' 'new feature'
Invoke-FixtureGit @('add', '.')
Invoke-FixtureGit @('-c', 'user.name=Updater Test', '-c', 'user.email=updater@example.invalid', 'commit', '--quiet', '-m', 'fixture v2')
Invoke-FixtureGit @('-c', 'user.name=Updater Test', '-c', 'user.email=updater@example.invalid', 'tag', '-a', 'v1.1.0', '-m', 'release v2', '--cleanup=verbatim')
& $updater -Version v1.1.0 -Repository $source -ProjectPath $target
Assert ((Get-Content -LiteralPath (Join-Path $target 'AIAugmentation/skill-kit-version.txt') -Raw).Trim() -eq 'v1.1.0') 'upgrade version'
Assert ((Get-Content -LiteralPath (Join-Path $target '.agents/skills/create-test-cases/SKILL.md') -Raw) -eq 'creator v2') 'skill was not updated'
Assert (Test-Path -LiteralPath (Join-Path $target '.agents/skills/new-feature/SKILL.md')) 'new skill missing'
Assert ((Get-Content -LiteralPath (Join-Path $target 'README.md') -Raw) -eq 'kit README v2') 'root README not upgraded'
Assert ((Get-Content -LiteralPath (Join-Path $target 'min_user_guide.md') -Raw) -eq 'quick start v2') 'quick start not upgraded'
Assert ((Get-Content -LiteralPath (Join-Path $target 'AIAugmentation/project_guides/review-test-coverage-guide.md') -Raw) -eq 'team customized guide') 'customized guide overwritten'
Assert ((Get-Content -LiteralPath (Join-Path $target 'AIAugmentation/project_guides/new-feature-guide.md') -Raw) -eq 'new guide') 'new guide missing on upgrade'
foreach ($path in $protected) {
    Assert ((Get-Content -LiteralPath (Join-Path $target $path) -Raw) -eq 'project-owned content') "modified $path"
}
Assert (-not (Test-Path -LiteralPath (Join-Path $target 'AIAugmentation/artifacts/sample.md'))) 'copied sample artifacts'
$before = Snapshot
& $updater -Version v1.1.0 -Repository $source -ProjectPath $target
Assert ((Snapshot) -eq $before) 'reinstall changed contents'
$failed = $false
try { & $updater -Version v9.9.9 -Repository $source -ProjectPath $target } catch { $failed = $true }
Assert $failed 'missing tag did not fail'
Assert ((Snapshot) -eq $before) 'missing tag changed project'
Invoke-FixtureGit @('rm', '--quiet', 'AGENTS.team.md')
Invoke-FixtureGit @('-c', 'user.name=Updater Test', '-c', 'user.email=updater@example.invalid', 'commit', '--quiet', '-m', 'incomplete fixture')
Invoke-FixtureGit @('tag', 'v2.0.0')
$failed = $false
try { & $updater -Version v2.0.0 -Repository $source -ProjectPath $target } catch { $failed = $true }
Assert $failed 'incomplete release did not fail'
Assert ((Snapshot) -eq $before) 'incomplete release changed project'
Write-Output "PASS: preview, install, upgrade, new skill, preservation, reinstall, missing tag and incomplete release. Fixtures: $sandbox"
