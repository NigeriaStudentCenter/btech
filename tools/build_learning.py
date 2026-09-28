"""Insert the 'Go deeper' content into docs/learning.html.

Run from the repo root:  python3 tools/build_learning.py
Each section's content lives in tools/deeper/section_*.py. The script is idempotent:
content between <!-- deeper:ID --> markers (and the CSS block) is replaced on every run.
"""
import importlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "deeper"))
PAGE = ROOT / "docs" / "learning.html"

CSS = """/*deeper-css*/.deeper{margin-top:30px;border-top:3px solid #20857b;padding-top:6px}
.deeper-title{color:#20857b;font-size:1.35rem;margin-top:10px}
.deeper figure{margin:22px 0;overflow-x:auto;-webkit-overflow-scrolling:touch}.deeper figure svg{min-width:560px}
@media(max-width:1000px){main{display:block;padding:0 16px}main>nav{position:static;margin-bottom:20px}main>nav a{display:inline-block;margin-right:15px}}.deeper h4{margin:0 0 8px;font-size:1.02rem}
.tablewrap{overflow-x:auto;margin:18px 0}table.info{border-collapse:collapse;width:100%;font-size:.92rem}
table.info caption{text-align:left;font-weight:700;margin-bottom:6px}table.info th,table.info td{border:1px solid #c9d7e3;padding:7px 9px;text-align:left;vertical-align:top}
table.info th{background:#eaf2f9}table.info tr:nth-child(even) td{background:#fafcfe}
.keyterms{background:#f6f3fb;border:1px solid #ddd3ee;border-radius:10px;padding:14px 18px;margin:20px 0}
.keyterms dl{display:grid;grid-template-columns:max-content 1fr;gap:6px 16px;margin:0}.keyterms dt{font-weight:700}.keyterms dd{margin:0}
.worked{background:#fff8e6;border:1px solid #efd9a6;border-radius:10px;padding:14px 18px;margin:20px 0}.worked ol{margin:6px 0 6px 20px;padding:0}.worked li{margin:4px 0}.worked .result{margin:8px 0 0}
.think{margin:20px 0}.think details{margin-top:8px}
.realworld{background:#eaf6f3;border-left:4px solid #20857b;border-radius:0 10px 10px 0;padding:12px 16px;margin:20px 0}
code,.mono{font-family:Menlo,Consolas,monospace;font-size:.92em;background:#eef3f8;padding:1px 4px;border-radius:4px}
@media(max-width:600px){.deeper figcaption::before{content:"↔ Swipe the diagram to see all of it. ";font-weight:650;color:#20857b}}
@media(max-width:760px){.keyterms dl{grid-template-columns:1fr}.keyterms dd{margin-bottom:8px}}
@media print{.deeper{page-break-before:auto}.think details{display:block}}
nav[aria-label="Student pack"]{display:flex;gap:20px;flex-wrap:wrap;position:static;background:none;padding:0;border-radius:0}nav[aria-label="Student pack"] a{display:inline;padding:0;font-size:1rem}/*/deeper-css*/"""


def main():
    html = PAGE.read_text()
    sections = {}
    for mod in sorted((ROOT / "tools" / "deeper").glob("section_*.py")):
        sections.update(importlib.import_module(mod.stem).SECTIONS)

    html = re.sub(r"/\*deeper-css\*/.*?/\*/deeper-css\*/", "", html, flags=re.S)
    html = html.replace("</style>", CSS + "</style>", 1)

    for sid, content in sections.items():
        html = re.sub(rf"<!-- deeper:{sid} -->.*?<!-- /deeper:{sid} -->", "", html, flags=re.S)
        anchor = f'<a class="next" href="index.html?section={sid}">'
        if html.count(anchor) != 1:
            raise SystemExit(f"Cannot find a unique insertion point for {sid}")
        block = f"<!-- deeper:{sid} -->{content}<!-- /deeper:{sid} -->"
        # place before the closing "When you can explain…" paragraph if present, else before the link
        art_start = html.rfind(f'<article id="{sid}"', 0, html.index(anchor))
        closing = html.rfind("<p>When you can explain", art_start, html.index(anchor))
        at = closing if closing != -1 else html.index(anchor)
        html = html[:at] + block + html[at:]

    PAGE.write_text(html)
    print(f"Inserted deeper content for {len(sections)} sections: {', '.join(sorted(sections))}")


if __name__ == "__main__":
    main()
