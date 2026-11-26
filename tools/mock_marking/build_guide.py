"""Build the server-side marking guide for the June 2024 Unit 2 mock (31769H).

The guide holds Pearson's question text and mark scheme, so it is written to
backend/guides/, which is git-ignored (this repository is public). It is only
uploaded to the marking Web App.

Usage:
  python3 tools/mock_marking/build_guide.py PAPER.pdf MARK_SCHEME.pdf
Needs pdftotext (poppler).
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

EXAM_ID = '31769H-2024-06'
PAPER_SHA256 = 'b77f724501691d94b7fb52987d34b05a1829c58eb790de9fca5b467d3e3fbf30'
# Same ids, marks and pages as docs/mock-june-2024/app.js.
QUESTIONS = [
    ('1a', 3, [2]), ('1b', 3, [3]), ('1c', 4, [4]), ('1d', 2, [5]), ('1e', 1, [6]),
    ('1f', 4, [7]), ('1g', 3, [8]), ('2a', 2, [10]), ('2b', 4, [10]), ('2c', 4, [11]),
    ('2d', 3, [12]), ('2e', 3, [12]), ('2f', 4, [14, 15]), ('3a', 4, [16]),
    ('3b', 6, [16, 17]), ('3c', 8, [18, 19]), ('4a', 10, [20, 21]), ('4b', 12, [22, 23]),
]
SCENARIO_PAGE = {'1': 2, '2': 10, '3': 16, '4': 20}
# Extended-response questions are marked with levels; flag them for teacher review.
LEVELS = {'3b', '3c', '4a', '4b'}
ROWS = {'2e': 3, '2f': 4}
# Answers printed as images in the mark scheme, so pdftotext cannot read them.
SCHEME_OVERRIDES = {
    '1e': 'Answer: 130, 170, 166, 112, 84, 108 (row-major order).\n'
          'Additional guidance: ignore use of brackets and delimiters. (1)',
}

NOISE = re.compile(
    r'DO NOT WRITE|^P\d{5}|^\d{1,2}$|Answer ALL questions|Turn over|^\(Total for Question'
    r'|BTEC Mark Scheme|^Question$|^Number$|^(Question )?(Answer|answer|Indicative content) Mark$'
    r'|^Question Number|^Total for Question|^TOTAL FOR PAPER')


def text(pdf, first=None, last=None):
    args = ['pdftotext', '-layout']
    if first:
        args += ['-f', str(first), '-l', str(last or first)]
    out = subprocess.run(args + [str(pdf), '-'], check=True, capture_output=True, text=True).stdout
    lines = []
    for raw in out.splitlines():
        line = re.sub(r'\s+', ' ', raw).strip()
        if not line or NOISE.search(line):
            continue
        if sum(c in '. …' for c in line) > 0.6 * len(line):  # answer lines
            continue
        lines.append(line)
    return '\n'.join(lines)


def scheme_parts(scheme_pdf):
    body = text(scheme_pdf)
    ids = [q[0] for q in QUESTIONS]
    starts = []
    pos = 0
    for qid in ids:
        match = re.compile(rf'^{qid}\b', re.M).search(body, pos)
        if not match:
            sys.exit(f'Could not find {qid} in the mark scheme.')
        starts.append(match.start())
        pos = match.end()
    tail = body.find('For more information', pos)
    starts.append(tail if tail > 0 else len(body))
    return {qid: SCHEME_OVERRIDES.get(qid) or body[starts[i]:starts[i + 1]].strip()
            for i, qid in enumerate(ids)}


def main(paper_pdf, scheme_pdf):
    digest = hashlib.sha256(Path(paper_pdf).read_bytes()).hexdigest()
    if digest != PAPER_SHA256:
        sys.exit('That is not the original June 2024 31769H question paper.')
    schemes = scheme_parts(scheme_pdf)
    scenarios = {n: text(paper_pdf, p).split('(a)')[0].strip() for n, p in SCENARIO_PAGE.items()}
    questions = []
    for qid, max_mark, pages in QUESTIONS:
        questions.append({
            'id': qid,
            'max': max_mark,
            'scenario': scenarios[qid[0]],
            'question': text(paper_pdf, pages[0], pages[-1]),
            'scheme': schemes[qid],
            'levels': qid in LEVELS,
            'rows': ROWS.get(qid, 0),
        })
    assert sum(q['max'] for q in questions) == 80
    out = Path(__file__).resolve().parents[2] / 'backend' / 'guides' / f'{EXAM_ID}.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({'examId': EXAM_ID, 'total': 80, 'questions': questions}, indent=1))
    print(f'Wrote {out} ({out.stat().st_size // 1024} KB)')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
