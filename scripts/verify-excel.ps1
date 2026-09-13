param([string]$WorkbookPath)

$ErrorActionPreference = 'Stop'
$catalogRoot = Split-Path -Parent $PSScriptRoot
$catalogSupport = Join-Path $catalogRoot 'outputs\support'
$catalogPath = if (-not $WorkbookPath) { Join-Path $catalogRoot 'SDLC_Proposed_Skills_Catalog.xlsx' } elseif ([IO.Path]::IsPathRooted($WorkbookPath)) { [IO.Path]::GetFullPath($WorkbookPath) } else { [IO.Path]::GetFullPath((Join-Path $catalogRoot $WorkbookPath)) }
if (-not (Test-Path -LiteralPath (Join-Path $catalogSupport 'expected-content.json'))) { throw 'Run scripts/build-catalog.mjs --check to prepare expected-content.json before native Excel verification.' }
$expected = Get-Content -LiteralPath (Join-Path $catalogSupport 'expected-content.json') -Raw | ConvertFrom-Json
$excel = $null
$book = $null
$report = [ordered]@{ application = 'Microsoft Excel'; readOnlyOpen = $false; sheets = @(); comparedCells = 0; formulaCounts = @(); clippedRows = @(); headerChecks = @() }
try {
    $excel = New-Object -ComObject Excel.Application
    $excel.Visible = $false
    $excel.DisplayAlerts = $false
    $excel.ScreenUpdating = $false
    $excel.AutomationSecurity = 3
    $book = $excel.Workbooks.Open($catalogPath, 0, $true)
    $report.readOnlyOpen = [bool]$book.ReadOnly
    if (-not $book.ReadOnly) { throw 'The validation workbook did not open read-only.' }
    if ($book.Worksheets.Count -ne 4) { throw 'Expected exactly four worksheets.' }
    $excel.CalculateFull()
    $specs = @(
        @{ Name = 'Skills Catalog'; Range = 'A6:D50'; Header = 'A5:D5'; Start = 6; End = 50; FrozenRows = 5; FrozenColumns = 1; Expected = $expected.catalogRows; Headers = @('Skill Name','Description','Inputs','Outputs') },
        @{ Name = 'Activity Mapping'; Range = 'A6:D53'; Header = 'A5:D5'; Start = 6; End = 53; FrozenRows = 5; FrozenColumns = 1; Expected = $expected.mappingRows; Headers = @('Phase','Activity','Skill Name','Type') },
        @{ Name = 'Implementation Roadmap'; Range = 'A8:F52'; Header = 'A7:F7'; Start = 8; End = 52; FrozenRows = 7; FrozenColumns = 3; Expected = $expected.roadmapRows; Headers = @('Order','Wave','Skill Name','Why This Order','Prerequisites / Inputs','First Validation Milestone') }
    )
    foreach ($spec in $specs) {
        $sheet = $book.Worksheets.Item($spec.Name)
        $sheet.Activate()
        $window = $book.Windows.Item(1)
        if (-not $window.FreezePanes -or $window.SplitRow -ne $spec.FrozenRows -or $window.SplitColumn -ne $spec.FrozenColumns) { throw "Frozen panes differ on $($spec.Name): $($window.SplitRow) rows / $($window.SplitColumn) columns." }
        if ($sheet.ListObjects.Count -ne 1 -or -not $sheet.ListObjects.Item(1).ShowAutoFilter) { throw "Missing filtered table on $($spec.Name)." }
        if ($window.DisplayGridlines) { throw "Gridlines unexpectedly visible on $($spec.Name)." }
        $actual = $sheet.Range($spec.Range).Value2
        for ($row = 0; $row -lt $spec.Expected.Count; $row++) {
            for ($col = 0; $col -lt $spec.Expected[$row].Count; $col++) {
                if ([string]$actual[($row + 1), ($col + 1)] -cne [string]$spec.Expected[$row][$col]) { throw "Content mismatch in $($spec.Name), row $($row + $spec.Start), column $($col + 1)." }
                $report.comparedCells++
            }
        }
        $actualHeaders = $sheet.Range($spec.Header).Value2
        for ($col = 0; $col -lt $spec.Headers.Count; $col++) {
            if ([string]$actualHeaders[1, ($col + 1)] -cne $spec.Headers[$col]) { throw "Header mismatch on $($spec.Name)." }
        }
        $savedHeights = @{}
        for ($row = $spec.Start; $row -le $spec.End; $row++) { $savedHeights[$row] = [double]$sheet.Rows.Item($row).RowHeight }
        $sheet.Range($spec.Range).EntireRow.AutoFit()
        $maxRequiredHeight = 0
        for ($row = $spec.Start; $row -le $spec.End; $row++) {
            $requiredHeight = [double]$sheet.Rows.Item($row).RowHeight
            $maxRequiredHeight = [Math]::Max($maxRequiredHeight, $requiredHeight)
            if ($requiredHeight -gt $savedHeights[$row] + 0.75) {
                $report.clippedRows += [ordered]@{ sheet = $spec.Name; row = $row; savedHeightPt = $savedHeights[$row]; requiredHeightPt = $requiredHeight }
            }
        }
        $headerHeight = [double]$sheet.Range($spec.Header).RowHeight
        $sheet.Range($spec.Header).EntireRow.AutoFit()
        $requiredHeaderHeight = [double]$sheet.Range($spec.Header).RowHeight
        $report.headerChecks += [ordered]@{ sheet = $spec.Name; savedHeightPt = $headerHeight; requiredHeightPt = $requiredHeaderHeight }
        if ($requiredHeaderHeight -gt $headerHeight + 0.75) { throw "Header height too small on $($spec.Name)." }
        $report.sheets += [ordered]@{ name = $spec.Name; dataRows = $spec.Expected.Count; columns = $spec.Headers.Count; table = $sheet.ListObjects.Item(1).Name; filters = $true; frozenRows = $window.SplitRow; frozenColumns = $window.SplitColumn; maxRequiredRowHeightPt = $maxRequiredHeight }
    }
    $overview = $book.Worksheets.Item('Overview')
    foreach ($cell in @(@('B6',45),@('B7',48),@('B9',2))) {
        $value = $overview.Range($cell[0]).Value2
        if ($value -ne $cell[1]) { throw "Overview formula mismatch at $($cell[0])." }
        $report.formulaCounts += [ordered]@{ cell = $cell[0]; value = $value }
    }
    $report.overview = 'Opened; displayed counts recalculated correctly in Excel.'
    $report.allTextEnglish = 'Verified separately against English source and catalog definitions.'
    $report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $catalogSupport 'native-excel-verification.json') -Encoding utf8
    if ($report.clippedRows.Count -gt 0) { throw "Native Excel found $($report.clippedRows.Count) rows requiring greater height." }
    $report | ConvertTo-Json -Depth 8
}
finally {
    if ($null -ne $book) { $book.Close($false) }
    if ($null -ne $excel) { $excel.Quit() }
    if ($null -ne $book) { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($book) }
    if ($null -ne $excel) { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($excel) }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
