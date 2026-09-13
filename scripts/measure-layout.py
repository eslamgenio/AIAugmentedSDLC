import json
import math
import os
from pathlib import Path
import sys
from PIL import ImageFont

payload = json.load(sys.stdin)
font_dir = Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts'
fonts = {
    False: ImageFont.truetype(str(font_dir / 'arial.ttf'), 15),
    True: ImageFont.truetype(str(font_dir / 'arialbd.ttf'), 15),
}

def line_count(text, width, bold=False):
    font = fonts[bold]
    lines = 0
    for paragraph in str(text).split('\n'):
        current = ''
        for word in paragraph.split(' '):
            candidate = f'{current} {word}' if current else word
            if font.getlength(candidate) <= width or not current:
                current = candidate
            else:
                lines += 1
                current = word
            if font.getlength(current) > width:
                lines += math.ceil(font.getlength(current) / width) - 1
        lines += 1
    return max(1, lines)

result = {}
for name, spec in payload.items():
    heights = []
    for row in spec['rows']:
        lines = max(line_count(text, spec['widths'][col] - 22, col in spec.get('boldColumns', [])) for col, text in enumerate(row))
        heights.append(max(spec.get('minimumHeight', 40), lines * 19 + 18))
    result[name] = heights
print(json.dumps(result))
