import collections
import argparse
import hashlib
import json
import pathlib
import re
import zipfile
import xml.etree.ElementTree as ET

root = pathlib.Path(__file__).resolve().parents[1]
support = root / 'outputs' / 'support'
parser = argparse.ArgumentParser(description='Verify workbook content against the tracked SDLC source files.')
parser.add_argument('--workbook', default='SDLC_Proposed_Skills_Catalog.xlsx', help='Workbook path, relative to the project or absolute.')
args = parser.parse_args()
file = root / args.workbook
source = (root / 'docs' / 'sdlc-source.mmd').read_text(encoding='utf-8')
details = json.loads((root / 'data' / 'skill-details.json').read_text(encoding='utf-8'))
roadmap_items = json.loads((root / 'data' / 'implementation-roadmap.json').read_text(encoding='utf-8'))
source_pairs = re.findall(r'"([^"\n]+)\nSkill: ([a-z-]+)"', source)
skill_names = list(dict.fromkeys(skill for _, skill in source_pairs))
assert len(source_pairs) == 48 and len(skill_names) == len(details) == 45
assert set(skill_names) == set(details)
assert len(roadmap_items) == 45 and {item['skill'] for item in roadmap_items} == set(skill_names)
groups = list(re.finditer(r'subgraph (\w+)\["([^"]+)"\]([\s\S]*?)\nend', source))
external_phases = {'G': 'TEST', 'H': 'REL', 'X': 'REL'}
expected_mapping = []
for match in re.finditer(r'\b([A-Z]+\d*)[\[{]"([^"\n]+)\nSkill: ([a-z-]+)"[\]}]', source):
    node, activity, skill = match.groups()
    group = next((item for item in groups if item.start() <= match.start() < item.end()), None)
    if group is None:
        group = next(item for item in groups if item.group(1) == external_phases[node])
    expected_mapping.append([group.group(2), activity, skill, 'Decision gate' if node in ('G', 'H') else 'Activity'])
expected_catalog = [[name, details[name]['description'], '\n'.join(details[name]['inputs']), '\n'.join(details[name]['outputs'])] for name in skill_names]
expected_roadmap = [[index, item['wave'], item['skill'], item['why'], item['prerequisites'], item['milestone']] for index, item in enumerate(roadmap_items, 1)]
ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(file) as archive:
    assert archive.testzip() is None
    strings = ET.fromstring(archive.read('xl/sharedStrings.xml')) if 'xl/sharedStrings.xml' in archive.namelist() else []
    shared = [''.join(text.text or '' for text in item.findall('.//m:t', ns)) for item in strings]
    book = ET.fromstring(archive.read('xl/workbook.xml'))
    names = [item.attrib['name'] for item in book.find('m:sheets', ns)]
    assert names == ['Skills Catalog', 'Activity Mapping', 'Implementation Roadmap', 'Overview']
    sheets = {}
    formula_errors = []
    for index, name in enumerate(names, 1):
        xml = ET.fromstring(archive.read(f'xl/worksheets/sheet{index}.xml'))
        cells = {}
        for cell in xml.findall('.//m:sheetData/m:row/m:c', ns):
            value = cell.find('m:v', ns)
            if cell.get('t') == 'inlineStr':
                value = ''.join(text.text or '' for text in cell.findall('.//m:t', ns))
            elif value is None:
                continue
            else:
                value = value.text
            if cell.get('t') == 's':
                value = shared[int(value)]
            elif cell.get('t') == 'e':
                formula_errors.append([name, cell.attrib['r'], value])
            elif cell.get('t') not in ('str', 'inlineStr'):
                value = float(value) if '.' in value else int(value)
            cells[cell.attrib['r']] = value
            if isinstance(value, str):
                assert all(ord(character) < 128 for character in value), (name, cell.attrib['r'], value)
        sheets[name] = cells
        assert xml.find('m:sheetProtection', ns) is None, 'Workbook should remain editable.'
    assert not formula_errors
    catalog = [[sheets['Skills Catalog'].get(f'{col}{row}') for col in 'ABCD'] for row in range(6,51)]
    mapping = [[sheets['Activity Mapping'].get(f'{col}{row}') for col in 'ABCD'] for row in range(6,54)]
    roadmap = [[sheets['Implementation Roadmap'].get(f'{col}{row}') for col in 'ABCDEF'] for row in range(8,53)]
    assert catalog == expected_catalog, 'Catalog content differs from tracked data.'
    assert mapping == expected_mapping, 'Activity mapping differs from the Mermaid source.'
    assert roadmap == expected_roadmap, 'Roadmap content differs from tracked data.'
    assert all(all(isinstance(value, str) and value.strip() for value in row) for row in catalog)
    assert len({row[0] for row in catalog}) == 45
    assert collections.Counter((row[1], row[2]) for row in mapping) == collections.Counter(source_pairs)
    assert len(source_pairs) == len(mapping) == 48
    assert collections.Counter(row[2] for row in roadmap) == collections.Counter(row[0] for row in catalog)
    assert [row[0] for row in roadmap] == list(range(1,46))
    assert [row[2] for row in roadmap[:3]] == ['create-test-cases','review-test-coverage','summarize-test-results']
    assert sum(row[3] == 'Decision gate' for row in mapping) == 2
    tables = [item for item in archive.namelist() if re.fullmatch(r'xl/tables/table\d+\.xml', item)]
    assert len(tables) == 3
    for table in tables:
        xml = ET.fromstring(archive.read(table))
        assert xml.find('m:autoFilter', ns) is not None
report = {
    'file': str(file), 'sha256': hashlib.sha256(file.read_bytes()).hexdigest(), 'bytes': file.stat().st_size,
    'sheets': names, 'uniqueSkills': len(catalog), 'sourceMappings': len(mapping), 'roadmapEntries': len(roadmap),
    'all642DetailCellsMatch': True, 'allCatalogFieldsNonEmpty': True, 'allMappingsMatchSourceExactly': True,
    'roadmapContainsEverySkillExactlyOnce': True, 'requiredFirstThreeStepsVerified': True,
    'englishOnlyText': True, 'filteredTables': 3, 'decisionGates': 2, 'formulaErrors': formula_errors,
    'editableAndUnprotected': True,
}
support.mkdir(parents=True, exist_ok=True)
(support / 'content-verification.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report, indent=2))
