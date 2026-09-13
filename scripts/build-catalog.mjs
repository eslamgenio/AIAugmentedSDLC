import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { parseArgs } from 'node:util';
import { Workbook, SpreadsheetFile, FileBlob } from '@oai/artifact-tool';

const scripts = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(scripts, '..');
const support = path.join(root, 'outputs', 'support');
const { values: options } = parseArgs({ options: {
  check: { type: 'boolean', default: false },
  'skip-previews': { type: 'boolean', default: false },
  overwrite: { type: 'boolean', default: false },
  output: { type: 'string' },
} });
const outputPath = path.resolve(root, options.output ?? 'outputs/support/SDLC_Proposed_Skills_Catalog.xlsx');
const relativeOutput = path.relative(root, outputPath);
assert.ok(relativeOutput && !relativeOutput.startsWith('..') && !path.isAbsolute(relativeOutput), 'The output must remain inside this project.');
const runtimeRoot = process.env.SDLC_RUNTIME_ROOT || path.join(os.homedir(), '.cache', 'codex-runtimes', 'codex-primary-runtime', 'dependencies');
const pythonPath = path.join(runtimeRoot, 'python', 'python.exe');
const sourceLink = 'https://app.excalidraw.com/s/2TPnfMpA2su/3X97mNAJXN5';
const source = await fs.readFile(path.join(root, 'docs', 'sdlc-source.mmd'), 'utf8');
const details = JSON.parse(await fs.readFile(path.join(root, 'data', 'skill-details.json'), 'utf8'));
const roadmapItems = JSON.parse(await fs.readFile(path.join(root, 'data', 'implementation-roadmap.json'), 'utf8'));
await fs.mkdir(support, { recursive: true });
if (!options.check && !options.overwrite) {
  try {
    await fs.access(outputPath);
    throw new Error(`Output already exists: ${outputPath}. Choose another --output or explicitly use --overwrite.`);
  } catch (error) {
    if (error.code !== 'ENOENT') throw error;
  }
}

const groups = [...source.matchAll(/subgraph (\w+)\["([^"]+)"\]([\s\S]*?)\nend/g)].map(m => ({
  key: m[1], label: m[2], start: m.index, end: m.index + m[0].length,
}));
const externalPhases = { G: 'TEST', H: 'REL', X: 'REL' };
const mappings = [...source.matchAll(/\b([A-Z]+\d*)[\[{]"([^"\n]+)\nSkill: ([a-z-]+)"[\]}]/g)].map(m => {
  const group = groups.find(g => m.index >= g.start && m.index < g.end) ?? groups.find(g => g.key === externalPhases[m[1]]);
  assert.ok(group, `No phase for ${m[1]}`);
  return { node: m[1], phase: group.label, activity: m[2], skill: m[3], type: ['G', 'H'].includes(m[1]) ? 'Decision gate' : 'Activity', phaseKey: group.key };
});
const names = [...new Set(mappings.map(m => m.skill))];
const counts = Object.fromEntries(names.map(name => [name, mappings.filter(m => m.skill === name).length]));
const reused = names.filter(n => counts[n] > 1);
assert.equal(mappings.length, 48);
assert.equal(names.length, 45);
assert.equal(groups.length, 10);
assert.deepEqual([...names].sort(), Object.keys(details).sort());
assert.deepEqual([...reused].sort(), ['deploy-test-build', 'execute-regression-tests', 'execute-smoke-tests']);
for (const [name, d] of Object.entries(details)) {
  assert.ok(d.description.startsWith('Would '), `${name}: proposal language`);
  assert.ok(d.description.length >= 90);
  for (const field of ['inputs', 'outputs']) {
    assert.equal(d[field].length, 3);
    assert.ok(d[field].every(s => typeof s === 'string' && s.trim().length > 10));
  }
}

const catalogRows = names.map(name => [name, details[name].description, details[name].inputs.join('\n'), details[name].outputs.join('\n')]);
const mappingRows = mappings.map(m => [m.phase, m.activity, m.skill, m.type]);
assert.equal(roadmapItems.length, 45);
assert.equal(new Set(roadmapItems.map(item => item.skill)).size, 45);
assert.deepEqual(roadmapItems.map(item => item.skill).sort(), [...names].sort());
assert.deepEqual(roadmapItems.slice(0, 3).map(item => item.skill), ['create-test-cases', 'review-test-coverage', 'summarize-test-results']);
assert.ok(roadmapItems.every(item => item.prerequisites.startsWith('Required:')));
const roadmapRows = roadmapItems.map((item, i) => [i + 1, item.wave, item.skill, item.why, item.prerequisites, item.milestone]);
const catalogWidths = [275, 350, 310, 310];
const mappingWidths = [285, 355, 300, 155];
const roadmapWidths = [60, 150, 270, 335, 350, 350];
const layout = JSON.parse(execFileSync(pythonPath, [path.join(scripts, 'measure-layout.py')], {
  input: JSON.stringify({
    catalog: { rows: catalogRows, widths: catalogWidths, boldColumns: [0], minimumHeight: 95 },
    mapping: { rows: mappingRows, widths: mappingWidths, boldColumns: [], minimumHeight: 44 },
    roadmap: { rows: roadmapRows, widths: roadmapWidths, boldColumns: [2], minimumHeight: 112 },
  }), encoding: 'utf8',
}));

const expectedContent = { mappings, catalogRows, mappingRows, roadmapRows, names, counts, layout, catalogWidths, mappingWidths, roadmapWidths };
await fs.writeFile(path.join(support, 'expected-content.json'), JSON.stringify(expectedContent, null, 2));
if (options.check) {
  console.log('Source and layout checks passed: 45 unique skills, 48 mappings, 45 roadmap entries and 2 decision gates.');
  console.log('Prepared outputs/support/expected-content.json. No workbook was created or modified.');
  process.exit(0);
}

const wb = Workbook.create();
const catalog = wb.worksheets.add('Skills Catalog');
const mapping = wb.worksheets.add('Activity Mapping');
const roadmap = wb.worksheets.add('Implementation Roadmap');
const overview = wb.worksheets.add('Overview');
const colors = {
  navy: '#19324D', text: '#223549', muted: '#53677A', rule: '#DCE4EC', stripe: '#F6F8FB',
  REQ: '#D0EBFF', DES: '#E5DBFF', PLAN: '#D3F9D8', PREP: '#C5F6FA', DEV: '#FFF3BF',
  BUILD: '#FFEC99', TEST: '#D0EBFF', DEFECT: '#FFE3E3', REL: '#EEBEFA', OPS: '#C3FAE8',
  gate: '#FFF9DB',
};
function setBase(sheet, lastRow, widths) {
  const endCol = String.fromCharCode(64 + widths.length);
  const used = sheet.getRange(`A1:${endCol}${lastRow}`);
  used.format.font = { name: 'Arial', size: 11, color: colors.text };
  used.format.fill = '#FFFFFF';
  used.format.verticalAlignment = 'center';
  used.format.horizontalAlignment = 'left';
  used.format.rowHeightPx = 26;
  widths.forEach((width, i) => sheet.getRangeByIndexes(0, i, lastRow, 1).format.columnWidthPx = width);
  sheet.showGridLines = false;
  sheet.getRange(`A1:${endCol}1`).format.rowHeightPx = 14;
  sheet.getRange(`A2:${endCol}2`).format.rowHeightPx = 36;
  sheet.getRange('A2').format.font = { name: 'Arial', size: 16, bold: true, color: colors.navy };
  sheet.getRange('A2').format.wrapText = false;
  sheet.getRange(`A2:${endCol}2`).format.borders = { bottom: { style: 'thin', color: colors.navy } };
}
function makeTable(sheet, range, name, dataStart, rows, heights, keyColumn) {
  const table = sheet.tables.add(range, true, name);
  table.style = 'TableStyleMedium2';
  table.showFilterButton = true;
  table.showTotals = false;
  const headers = table.getHeaderRowRange();
  headers.format.fill = colors.navy;
  headers.format.font = { name: 'Arial', size: 11, bold: true, color: '#FFFFFF' };
  headers.format.horizontalAlignment = 'center';
  headers.format.verticalAlignment = 'center';
  headers.format.rowHeightPx = 34;
  headers.format.borders = { insideVertical: { style: 'thin', color: '#FFFFFF' } };
  rows.forEach((row, i) => {
    const cells = sheet.getRangeByIndexes(dataStart - 1 + i, 0, 1, row.length);
    cells.format.wrapText = true;
    cells.format.verticalAlignment = 'top';
    cells.format.rowHeightPx = heights[i];
    cells.format.fill = i % 2 === 0 ? '#FFFFFF' : colors.stripe;
    cells.format.borders = { bottom: { style: 'thin', color: colors.rule } };
    if (keyColumn !== undefined) sheet.getCell(dataStart - 1 + i, keyColumn).format.font.bold = true;
  });
  sheet.freezePanes.freezeRows(dataStart - 1);
  sheet.freezePanes.freezeColumns(1);
  return table;
}

setBase(catalog, 50, catalogWidths);
catalog.tabColor = colors.navy;
catalog.getRange('A2').values = [['Proposed skills catalog']];
catalog.getRange('A3').values = [['Proposed capabilities. Each row defines the intended purpose, required inputs and expected outputs.']];
catalog.getRange('A3').format.font = { name: 'Arial', size: 11, italic: true, color: colors.muted };
catalog.getRange('A3').format.wrapText = false;
catalog.getRange('A4:D4').format.rowHeightPx = 12;
catalog.getRange('A5:D5').values = [['Skill Name', 'Description', 'Inputs', 'Outputs']];
catalog.getRange('A6:D50').values = catalogRows;
makeTable(catalog, 'A5:D50', 'SkillsCatalog', 6, catalogRows, layout.catalog, 0);
names.forEach((name, i) => {
  const first = mappings.find(m => m.skill === name);
  const cell = catalog.getCell(i + 5, 0);
  cell.format.fill = first.type === 'Decision gate' ? colors.gate : colors[first.phaseKey];
});

setBase(mapping, 53, mappingWidths);
mapping.tabColor = '#6385A7';
mapping.getRange('A2').values = [['Activity mapping']];
mapping.getRange('A3').values = [['Source: SDLC diagram']];
mapping.getRange('B3').values = [[sourceLink]];
mapping.getRange('B3').format.font = { name: 'Arial', size: 11, color: '#175A9D', underline: 'single' };
mapping.getRange('B3').format.wrapText = false;
mapping.getRange('A3').format.font = { name: 'Arial', size: 11, italic: true, color: colors.muted };
mapping.getRange('A4:D4').format.rowHeightPx = 12;
mapping.getRange('A5:D5').values = [['Phase', 'Activity', 'Skill Name', 'Type']];
mapping.getRange('A6:D53').values = mappingRows;
makeTable(mapping, 'A5:D53', 'ActivityMapping', 6, mappingRows, layout.mapping);
mappings.forEach((m, i) => {
  mapping.getCell(i + 5, 0).format.fill = colors[m.phaseKey];
  if (m.type === 'Decision gate') {
    mapping.getCell(i + 5, 3).format.fill = colors.gate;
    mapping.getCell(i + 5, 3).format.font.bold = true;
  }
});

setBase(roadmap, 52, roadmapWidths);
roadmap.tabColor = '#516780';
roadmap.getRange('A2').values = [['Proposed implementation roadmap']];
roadmap.getRange('A3').values = [["Recommended sequence for Eslam's quality leadership work. Priorities can change with available evidence and project needs."]];
roadmap.getRange('A4').values = [['Prerequisites are artifacts, permissions or readiness. People and existing tools can supply them; an upstream skill is not a hard dependency.']];
roadmap.getRange('A5').values = [['Execution requires a ready environment, suitable data and runnable tests. Production actions also require recorded human authorization.']];
roadmap.getRange('A3:A5').format.font = { name: 'Arial', size: 11, italic: true, color: colors.muted };
roadmap.getRange('A3:A5').format.wrapText = false;
roadmap.getRange('A6:F6').format.rowHeightPx = 12;
roadmap.getRange('A7:F7').values = [['Order', 'Wave', 'Skill Name', 'Why This Order', 'Prerequisites / Inputs', 'First Validation Milestone']];
roadmap.getRange('A8:F52').values = roadmapRows;
makeTable(roadmap, 'A7:F52', 'ImplementationRoadmap', 8, roadmapRows, layout.roadmap, 2);
roadmap.freezePanes.freezeColumns(3);
roadmap.getRange('A8:A52').format.horizontalAlignment = 'center';
roadmap.getRange('A8:A52').setNumberFormat('0');
const waveColors = ['#D0EBFF', '#E5DBFF', '#C5F6FA', '#D3F9D8', '#FFF3BF', '#FFEC99', '#EEBEFA'];
roadmapItems.forEach((item, i) => {
  roadmap.getCell(i + 7, 1).format.fill = waveColors[Number(item.wave.slice(0, 2)) - 1];
});

setBase(overview, 29, [280, 815]);
overview.tabColor = '#AAB7C4';
overview.getRange('A2').values = [['SDLC catalog overview']];
const overviewItems = [
  [4, 'Status', 'Proposed AI capabilities. No skills have been created, installed or implemented.'],
  [6, 'Unique proposed skills', null],
  [7, 'Activity and gate mappings', null],
  [8, 'Phases', groups.length],
  [9, 'Decision gates', null],
  [10, 'Reused skills', reused.length],
  [12, 'How to use', 'Filter Skills Catalog by skill name. Use Activity Mapping to locate every activity or decision gate that uses a skill.'],
  [13, 'Ordering and color', 'Rows follow first appearance in the supplied diagram. Catalog colors show the first associated phase. The mapping sheet shows each phase explicitly. Amber identifies decision gates.'],
  [20, 'Human decisions', 'Test exit and release assessments provide evidence and recommendations. The responsible people make gate decisions. Production deployment requires recorded human release approval.'],
  [22, 'Phase assignment', 'The test exit gate is grouped with phase 07. Human release approval and Resolve release blockers are grouped with phase 09. These nodes appear outside phase boxes in the diagram.'],
  [24, 'Source and scope', 'The supplied Mermaid definition of the SDLC diagram defines the exact names and mappings. Descriptions, inputs and outputs are proposed specifications developed for this catalog.'],
  [26, 'Implementation roadmap', 'All 45 skills have a proposed order across seven waves. The sequence favors quality evidence first, then preparation, controlled testing, design/code, delivery and release. It is not a universal priority ranking.'],
  [28, 'Real prerequisites', 'Roadmap prerequisites describe required artifacts, access and readiness. Human work or existing tools can satisfy them. Earlier roadmap positions are recommendations, not mandatory skill-to-skill dependencies.'],
];
for (const [row, label, value] of overviewItems) {
  overview.getCell(row - 1, 0).values = [[label]];
  if (value !== null) overview.getCell(row - 1, 1).values = [[value]];
  overview.getCell(row - 1, 0).format.font.bold = true;
  overview.getRange(`A${row}:B${row}`).format.verticalAlignment = 'top';
  overview.getRange(`A${row}:B${row}`).format.wrapText = true;
}
overview.getRange('B6').formulas = [["=COUNTA(SkillsCatalog[Skill Name])"]];
overview.getRange('B7').formulas = [["=COUNTA(ActivityMapping[Skill Name])"]];
overview.getRange('B9').formulas = [["=COUNTIFS(ActivityMapping[Type],\"Decision gate\")"]];
overview.getRange('B6:B10').setNumberFormat('0');
overview.getRange('B6:B10').format.horizontalAlignment = 'left';
overview.getRange('A4:B4').format.rowHeightPx = 46;
overview.getRange('A12:B12').format.rowHeightPx = 52;
overview.getRange('A13:B13').format.rowHeightPx = 66;
overview.getRange('A15:B15').values = [['Reused Skill', 'Activity Associations']];
overview.getRange('A15:B15').format.fill = colors.navy;
overview.getRange('A15:B15').format.font = { name: 'Arial', size: 11, bold: true, color: '#FFFFFF' };
overview.getRange('A15:B15').format.horizontalAlignment = 'center';
overview.getRange('A15:B15').format.rowHeightPx = 34;
overview.getRange('A15:B15').format.borders = { insideVertical: { style: 'thin', color: '#FFFFFF' } };
reused.forEach((name, i) => {
  const row = i + 16;
  const useText = mappings.filter(m => m.skill === name).map(m => `${m.phase}: ${m.activity}`).join('\n');
  overview.getRange(`A${row}:B${row}`).values = [[name, useText]];
  overview.getRange(`A${row}:B${row}`).format.wrapText = true;
  overview.getRange(`A${row}:B${row}`).format.verticalAlignment = 'center';
  overview.getRange(`A${row}:B${row}`).format.rowHeightPx = 65;
  overview.getRange(`A${row}:B${row}`).format.fill = i % 2 ? colors.stripe : '#FFFFFF';
  overview.getRange(`A${row}:B${row}`).format.borders = { bottom: { style: 'thin', color: colors.rule } };
});
for (const row of [20, 22, 24, 26, 28]) overview.getRange(`A${row}:B${row}`).format.rowHeightPx = 64;

wb.recalculate();
assert.deepEqual(catalog.getRange('A6:D50').values, catalogRows);
assert.deepEqual(mapping.getRange('A6:D53').values, mappingRows);
assert.deepEqual(roadmap.getRange('A8:F52').values, roadmapRows);
assert.equal(overview.getRange('B6').values[0][0], 45);
assert.equal(overview.getRange('B7').values[0][0], 48);
assert.equal(overview.getRange('B9').values[0][0], 2);
const inspection = await wb.inspect({ kind: 'workbook,sheet,table', maxChars: 5000, tableMaxRows: 2, tableMaxCols: 4, tableMaxCellChars: 60 });
await fs.writeFile(path.join(support, 'workbook-inspection.ndjson'), inspection.ndjson);
const errors = await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!', options: { useRegex: true, maxResults: 30 }, maxChars: 2000 });
await fs.writeFile(path.join(support, 'formula-error-scan.ndjson'), errors.ndjson);
console.log('Content checks passed: 45 unique skills, 48 exact mappings, 45 roadmap entries, 2 human-supported decision gates.');
console.log(errors.ndjson);

await fs.mkdir(path.dirname(outputPath), { recursive: true });
const output = await SpreadsheetFile.exportXlsx(wb);
await output.save(outputPath);
await fs.writeFile(path.join(support, 'created-output.json'), JSON.stringify({ outputPath, skillCount: names.length, mappingCount: mappings.length }, null, 2));
console.log(`Exported ${outputPath}`);

const reopened = await SpreadsheetFile.importXlsx(await FileBlob.load(outputPath));
assert.deepEqual(reopened.worksheets.getItem('Skills Catalog').getRange('A6:D50').values, catalogRows);
assert.deepEqual(reopened.worksheets.getItem('Activity Mapping').getRange('A6:D53').values, mappingRows);
assert.deepEqual(reopened.worksheets.getItem('Implementation Roadmap').getRange('A8:F52').values, roadmapRows);
console.log('Saved XLSX reopened successfully; all 642 catalog, mapping and roadmap cells match the expected content.');
if (options['skip-previews']) {
  console.log('Preview rendering skipped as requested.');
  process.exit(0);
}

const previews = [];
for (let start = 1; start <= 50; start = start === 1 ? 12 : start + 8) {
  const end = start === 1 ? 11 : Math.min(start + 7, 50);
  previews.push({ sheetName: 'Skills Catalog', range: `A${start}:D${end}`, name: `catalog-${String(start).padStart(2, '0')}-${end}` });
}
previews.push(
  { sheetName: 'Activity Mapping', range: 'A1:D22', name: 'mapping-01-22' },
  { sheetName: 'Activity Mapping', range: 'A23:D40', name: 'mapping-23-40' },
  { sheetName: 'Activity Mapping', range: 'A41:D53', name: 'mapping-41-53' },
  { sheetName: 'Overview', range: 'A1:B29', name: 'overview' },
);
for (let start = 1; start <= 52; start = start === 1 ? 13 : start + 7) {
  const end = start === 1 ? 12 : Math.min(start + 6, 52);
  previews.push({ sheetName: 'Implementation Roadmap', range: `A${start}:F${end}`, name: `roadmap-${String(start).padStart(2, '0')}-${end}` });
}
for (const preview of previews) {
  const blob = await reopened.render({ sheetName: preview.sheetName, range: preview.range, scale: 1.4, format: 'png' });
  await fs.writeFile(path.join(support, `${preview.name}.png`), new Uint8Array(await blob.arrayBuffer()));
  console.log(`Rendered ${preview.name}`);
}
await fs.writeFile(path.join(support, 'previews.json'), JSON.stringify(previews, null, 2));
