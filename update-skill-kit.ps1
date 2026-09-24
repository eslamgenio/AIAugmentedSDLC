#Requires -Version 5.1
<#
.SYNOPSIS
Install shared SDLC skill-kit files from an exact Git release tag.
.EXAMPLE
.\update-skill-kit.ps1 -Version v1.2.0
.EXAMPLE
.\update-skill-kit.ps1 -Version v1.2.0 -ProjectPath C:\Projects\MyApp -WhatIf
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^v?[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.-]+)?$')]
    [string]$Version,
    [string]$ProjectPath = (Get-Location).Path,
    [ValidateNotNullOrEmpty()]
    [string]$Repository = 'https://gitlabce.tools.aws.vodafone.com/central-vois-framework/devskillkit.git'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
Get-Command git -ErrorAction Stop | Out-Null
$project = (Resolve-Path -LiteralPath $ProjectPath).ProviderPath
if (-not (Test-Path -LiteralPath $project -PathType Container)) {
    throw 'ProjectPath must be an existing directory.'
}

function Invoke-Git {
    param([string[]]$Arguments)
    # Windows PowerShell treats native stderr (including warnings) as errors.
    $ErrorActionPreference = 'Continue'
    $result = & git @Arguments 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Git failed. Check repository access and that tag '$Version' exists.`n$($result -join "`n")"
    }
    return $result
}

# Reject links/junctions so a shared-file update cannot escape the project.
function Assert-RegularPath {
    param([string]$Path, [string]$Root)
    $full = [IO.Path]::GetFullPath($Path)
    $base = [IO.Path]::GetFullPath($Root).TrimEnd('\', '/')
    if ($full -ne $base -and -not $full.StartsWith($base + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Path escapes the allowed directory: $Path"
    }
    $cursor = $full
    while ($cursor) {
        if (Test-Path -LiteralPath $cursor) {
            $item = Get-Item -LiteralPath $cursor -Force
            if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
                throw "Linked paths are not supported: $cursor"
            }
        }
        $parent = Split-Path -Parent $cursor
        if ($parent -eq $cursor) { break }
        $cursor = $parent
    }
}

$tempBase = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
$stage = Join-Path $tempBase ('sdlc-kit-' + [guid]::NewGuid().ToString('N'))
try {
    New-Item -ItemType Directory -Path $stage -WhatIf:$false | Out-Null
    Invoke-Git -Arguments @('init', '--quiet', $stage) | Out-Null
    Invoke-Git -Arguments @('-C', $stage, 'fetch', '--quiet', '--depth=1', '--no-tags', '--', $Repository, "refs/tags/$Version") | Out-Null
    Invoke-Git -Arguments @('-C', $stage, 'checkout', '--quiet', '--detach', 'FETCH_HEAD') | Out-Null
    $commit = (Invoke-Git -Arguments @('-C', $stage, 'rev-parse', 'HEAD') | Select-Object -Last 1).ToString().Trim()

    $required = @('AGENTS.team.md', 'README.md', 'min_user_guide.md', 'AIAugmentation/README.md', 'AIAugmentation/templates/README.md')
    foreach ($relative in $required) {
        if (-not (Test-Path -LiteralPath (Join-Path $stage $relative) -PathType Leaf)) {
            throw "Release is missing required file: $relative"
        }
    }
    $skillsRoot = Join-Path $stage '.agents/skills'
    if (-not (Test-Path -LiteralPath $skillsRoot -PathType Container)) {
        throw 'Release contains no skill packages.'
    }
    $skills = @(Get-ChildItem -LiteralPath $skillsRoot -Directory -Force)
    if ($skills.Count -eq 0) { throw 'Release contains no skill packages.' }

    # Only these areas belong to the kit. Never copy the entire repository.
    $files = @()
    foreach ($skill in $skills) {
        if (-not (Test-Path -LiteralPath (Join-Path $skill.FullName 'SKILL.md') -PathType Leaf)) {
            throw "Release skill has no SKILL.md: $($skill.Name)"
        }
        Assert-RegularPath -Path $skill.FullName -Root $stage
        $files += @(Get-ChildItem -LiteralPath $skill.FullName -Recurse -File -Force)
    }
    $files += @(Get-ChildItem -LiteralPath (Join-Path $stage 'AIAugmentation/templates') -Recurse -File -Force)
    $files += Get-Item -LiteralPath (Join-Path $stage 'AIAugmentation/README.md')
    # Keep the team instruction template separate from the project's AGENTS.md.
    $files += Get-Item -LiteralPath (Join-Path $stage 'AGENTS.team.md')
    $files += Get-Item -LiteralPath (Join-Path $stage 'README.md')
    $files += Get-Item -LiteralPath (Join-Path $stage 'min_user_guide.md')

    # Seed project guides without overwriting team-owned customizations.
    # Older releases without guides remain installable.
    $guidesRoot = Join-Path $stage 'AIAugmentation/project_guides'
    if (Test-Path -LiteralPath $guidesRoot -PathType Container) {
        Assert-RegularPath -Path $guidesRoot -Root $stage
        $files += @(Get-ChildItem -LiteralPath $guidesRoot -Recurse -File -Force)
    }

    $plan = @()
    foreach ($file in $files) {
        Assert-RegularPath -Path $file.FullName -Root $stage
        $relative = $file.FullName.Substring($stage.Length + 1)
        $destination = Join-Path $project $relative
        Assert-RegularPath -Path $destination -Root $project
        if (Test-Path -LiteralPath $destination -PathType Container) {
            throw "Expected a file but found a directory: $destination"
        }
        if ($relative.Replace('\', '/').StartsWith('AIAugmentation/project_guides/') -and
            (Test-Path -LiteralPath $destination -PathType Leaf)) {
            continue
        }
        $plan += [pscustomobject]@{ Source = $file.FullName; Destination = $destination }
    }
    $versionFile = Join-Path $project 'AIAugmentation/skill-kit-version.txt'
    Assert-RegularPath -Path $versionFile -Root $project
    if (Test-Path -LiteralPath $versionFile -PathType Container) {
        throw "Expected a file but found a directory: $versionFile"
    }

    if ($PSCmdlet.ShouldProcess($project, "Install skill-kit $Version ($commit), updating $($plan.Count) shared files")) {
        foreach ($entry in $plan) {
            $parent = Split-Path -Parent $entry.Destination
            [IO.Directory]::CreateDirectory($parent) | Out-Null
            Copy-Item -LiteralPath $entry.Source -Destination $entry.Destination -Force
        }
        # Write last: a failed copy must never claim the new version is installed.
        [IO.File]::WriteAllText($versionFile, "$Version`n", [Text.UTF8Encoding]::new($false))
        Write-Output "Installed skill-kit $Version (commit $commit). Review the changes and commit them in your project."
        Write-Output 'Existing project guides, artifacts, AGENTS.md and unrelated skills were preserved. Root README.md and min_user_guide.md were updated. No files were deleted.'
    }
}
finally {
    # This unique temporary directory is the only directory we ever remove.
    if (Test-Path -LiteralPath $stage) {
        $resolvedStage = [IO.Path]::GetFullPath($stage)
        if ((Split-Path -Parent $resolvedStage).TrimEnd('\', '/') -ne $tempBase.TrimEnd('\', '/') -or
            (Split-Path -Leaf $resolvedStage) -notmatch '^sdlc-kit-[0-9a-f]{32}$') {
            throw 'Refusing cleanup outside the updater temporary directory.'
        }
        Remove-Item -LiteralPath $resolvedStage -Recurse -Force -WhatIf:$false
    }
}
