"""Build the Unit 19 Computer Networking pages.

Run from the repo root:  python3 tools/build_unit19.py
Writes docs/unit19/learning.html, docs/unit19/index.html (workbook), docs/unit19/workbook.js
and api/sections-u19.json (the tutor's approved notes). Content lives in tools/unit19/.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "unit19"))
import sec_a, sec_bc, workbook_data  # noqa: E402

OUT = ROOT / "docs" / "unit19"
OUT.mkdir(parents=True, exist_ok=True)

NAV_ITEMS = [("start.html", "Start"), ("brief.html", "1. Assignment guide"), ("learning.html", "2. Learn"), ("index.html", "3. Workbook + tutor"),
             ("practicals.html", "4. Practicals"), ("assignment.html", "5. Assignment builder"), ("quizzes.html", "6. Quizzes"), ("teachers.html", "Teachers")]


def pack_nav():
    return '<nav aria-label="Course pack">' + "".join(f'<a href="{h}">{t}</a>' for h, t in NAV_ITEMS) + "</nav>"


LEARN_CSS = """body{margin:0;background:#f3f7fb;color:#183247;font:18px/1.65 system-ui,sans-serif}
.packnav{padding:14px max(20px,calc((100vw - 1140px)/2));background:#fff;border-bottom:1px solid #d1dce6}
nav[aria-label="Course pack"]{display:flex;gap:18px;flex-wrap:wrap}nav[aria-label="Course pack"] a{color:#155b91}
header{background:#12324f;color:white;padding:30px max(22px,calc((100vw - 1140px)/2))}header h1{font-size:2rem;margin:0}header p{max-width:75ch;margin:10px 0}
main{max-width:1140px;margin:24px auto;display:grid;grid-template-columns:230px minmax(0,1fr);gap:26px;padding:0 20px}
main>nav{position:sticky;top:16px;align-self:start;background:white;padding:18px;border-radius:12px;max-height:calc(100vh - 32px);overflow:auto}
main>nav h2{font-size:1rem;margin:.2em 0 .6em}main>nav a{display:block;font-size:.88rem;padding:4px 0;color:#185981}main>nav .aim{font-weight:700;font-size:.8rem;color:#4f6577;margin-top:10px}
article{background:white;border:1px solid #d1dce6;border-radius:12px;padding:28px;margin-bottom:28px;scroll-margin-top:15px}
h2{font-size:1.8rem;line-height:1.25;margin:0 0 12px}h3{font-size:1.2rem;margin:26px 0 8px}h4{margin:0 0 8px;font-size:1.02rem}p{margin:10px 0}
.goal{color:#3c5f79;font-weight:600}.crit{display:inline-block;background:#12324f;color:#fff;border-radius:999px;padding:1px 10px;font-size:.78rem;margin-left:6px}
.aim{background:#eef4fa;border-radius:8px;padding:10px 14px}
figure{margin:22px 0;overflow-x:auto}svg{display:block;width:100%;height:auto;min-width:560px}figcaption{font-size:.88rem;color:#4f6577;margin-top:8px}
.tablewrap{overflow-x:auto;margin:18px 0}table.info{border-collapse:collapse;width:100%;font-size:.92rem}table.info caption{text-align:left;font-weight:700;margin-bottom:6px}
table.info th,table.info td{border:1px solid #c9d7e3;padding:7px 9px;text-align:left;vertical-align:top}table.info th{background:#eaf2f9}table.info tr:nth-child(even) td{background:#fafcfe}
.keyterms{background:#f6f3fb;border:1px solid #ddd3ee;border-radius:10px;padding:14px 18px;margin:20px 0}.keyterms dl{display:grid;grid-template-columns:max-content 1fr;gap:6px 16px;margin:0}.keyterms dt{font-weight:700}.keyterms dd{margin:0}
.worked{background:#fff8e6;border:1px solid #efd9a6;border-radius:10px;padding:14px 18px;margin:20px 0}.worked ol,.tryit ol{margin:6px 0 6px 20px;padding:0}.worked li,.tryit li{margin:4px 0}
.think{margin:20px 0}details{background:#f2f7fb;padding:12px 14px;border-radius:8px;margin-top:8px}summary{cursor:pointer;font-weight:650}
.realworld{background:#eaf6f3;border-radius:10px;padding:12px 16px;margin:20px 0}
.tryit{background:#eef6ff;border:1px solid #bcd6f0;border-radius:10px;padding:14px 18px;margin:20px 0}
.assess{background:#fdf1e7;border:1px solid #f0cfae;border-radius:10px;padding:12px 16px;margin:20px 0}
pre.cli{background:#0f2233;color:#d7f5e3;border-radius:8px;padding:12px 14px;overflow-x:auto;font-size:.85rem;line-height:1.45;margin:14px 0 4px}
code{font-family:Menlo,Consolas,monospace;font-size:.9em;background:#eef3f8;padding:1px 4px;border-radius:4px;overflow-wrap:anywhere}pre code{background:none;padding:0;color:inherit}
.small{font-size:.88rem;color:#4f6577}.next{display:inline-block;background:#175d88;color:white;border-radius:8px;padding:12px 18px;text-decoration:none;margin-top:18px}
footer{font-size:.9rem;margin:20px;color:#4f6577}
@media(max-width:1000px){main{display:block;padding:0 14px}main>nav{position:static;margin-bottom:20px;max-height:none}main>nav a{display:inline-block;margin-right:14px}}
@media(max-width:600px){body{font-size:17px}article{padding:18px}figcaption::before{content:"↔ Swipe the diagram to see all of it. ";font-weight:650;color:#20857b}.keyterms dl{grid-template-columns:1fr}}
@media print{main>nav,.next,header,.packnav{display:none}main{display:block}article{border:0;page-break-before:always}details{display:block}}"""

AIM_TITLES = {"A": "Learning aim A · Assignment 1", "B": "Learning aim B · Assignment 2", "C": "Learning aim C · Assignment 2"}


def build_learning():
    lessons = sec_a.LESSONS + sec_bc.LESSONS
    ids = [re.search(r'<article id="([^"]+)"', l).group(1) for l in lessons]
    titles = [re.search(r"<h2>(.*?)</h2>", l).group(1) for l in lessons]
    side, last = [], None
    for i, t in zip(ids, titles):
        if i[0] != last:
            side.append(f'<p class="aim">{AIM_TITLES[i[0]]}</p>')
            last = i[0]
        side.append(f'<a href="#{i}">{i} {t}</a>')
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unit 19 Learn: Computer Networking</title><style>{LEARN_CSS}</style></head><body>
<div class="packnav">{pack_nav()}</div>
<header><h1>Unit 19: Computer Networking</h1><p>Learn the idea, look at the diagram, try it in Packet Tracer, then open the matching workbook section.</p><p>Each lesson shows which part of your assignment it helps with.</p></header>
<main><nav aria-label="Lessons"><h2>Lessons</h2>{''.join(side)}</nav><div>{''.join(lessons)}</div></main>
<footer>Original teaching material written for this course and aligned to the Pearson BTEC Level 3 Unit 19 specification. Diagrams are simplified learning models. Not a Pearson or Cisco publication.</footer></body></html>"""
    (OUT / "learning.html").write_text(html)
    return ids


def build_workbook(ids):
    data = workbook_data.SECTIONS
    assert [s["id"] for s in data] == ids, ("workbook sections must match lessons", ids)
    (ROOT / "api" / "sections-u19.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    u2 = (ROOT / "docs" / "index.html").read_text()
    style = re.search(r"<style>.*?</style>", u2, re.S).group(0)
    main = re.search(r"<main>.*?</main>", u2, re.S).group(0)
    main = main.replace("The tutor needs the school to set up its AI service.", "Ask about this lesson. Do not include personal information.")
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unit 19 Workbook</title>{style}<style>nav[aria-label="Course pack"]{{display:flex;gap:18px;flex-wrap:wrap;background:none;border:0;padding:0}}@media(max-width:720px){{#menu{{grid-template-columns:repeat(2,minmax(0,1fr))!important}}#menu button{{white-space:normal;overflow-wrap:anywhere}}}}</style></head><body>
<div style="padding:16px;background:#fff;color:#17334b">{pack_nav()}</div><header><h1>Unit 19 Networking Workbook</h1><p>Learn, practise, check yourself and ask the tutor</p><p><a id="backToLearning" href="learning.html" style="color:white">← Read the lesson</a></p></header>
{main}
<script id="courseData" type="application/json">{json.dumps(data, ensure_ascii=False)}</script><script src="../config.js"></script><script src="workbook.js"></script></body></html>"""
    (OUT / "index.html").write_text(page)
    js = (ROOT / "docs" / "workbook.js").read_text()
    js = js.replace("KEY='unit2-workbook-v1'", "KEY='unit19-workbook-v1'").replace("'unit2-workbook-v1'", "'unit19-workbook-v1'")
    js = js.replace("body:JSON.stringify({section:current,", "body:JSON.stringify({course:'u19',section:current,")
    js = js.replace("'my-computing-work.json'", "'my-networking-work.json'").replace("'my-computing-'+current", "'my-networking-'+current")
    assert "unit19-workbook-v1" in js and "course:'u19'" in js
    (OUT / "workbook.js").write_text(js)


GRADE_CLASS = {"Pass": "p", "Merit": "m", "Distinction": "d"}


def esc(t):
    import html
    return html.escape(str(t), quote=True)


def build_brief():
    data = json.loads((ROOT / "api" / "assignments-u19.json").read_text())
    (OUT / "assignments.json").write_text((ROOT / "api" / "assignments-u19.json").read_text())
    parts = []
    for a in data["assignments"]:
        rows = "".join(
            f'<tr><td><span class="badge {GRADE_CLASS.get(t["grade"].split(" /")[0], "p")}">{esc(t["criteria"])}</span></td><td><strong>{esc(t["title"])}</strong><br>{esc(t["asks"])}</td>'
            f'<td><ul class="list">{"".join(f"<li>{esc(c)}</li>" for c in t["checklist"])}</ul></td>'
            f'<td>{" ".join(f'<a href="learning.html#{l}">{l}</a>' for l in t["lessons"])}<br><a href="assignment.html#{t["id"]}">Open in builder →</a></td></tr>'
            for t in a["tasks"])
        req = ""
        if a.get("requirements"):
            req = '<h3>The client’s requirements</h3><ul class="list">' + "".join(f"<li>{esc(r)}</li>" for r in a["requirements"]) + "</ul><p class=\"small\">Your teacher’s brief has the full office layout and the users, groups and permissions table.</p>"
        parts.append(f'<section class="card" id="{a["id"]}"><h2>{esc(a["title"])}</h2><p><strong>{esc(a["aim"])}.</strong> {esc(a["scenario"])}</p>{req}<p><strong>Hand in:</strong> {esc(a["evidence"])}</p>'
                     f'<div class="tablewrap"><table><thead><tr><th>Criterion</th><th>What the task asks (in plain English)</th><th>Checklist: a strong answer…</th><th>Help</th></tr></thead><tbody>{rows}</tbody></table></div></section>')
    grades = """<section class="card"><h2>What Pass, Merit and Distinction mean</h2><div class="tablewrap"><table><thead><tr><th>Grade</th><th>Command word</th><th>What the assessor looks for</th></tr></thead><tbody>
<tr><td><span class="badge p">Pass</span></td><td>Explain, design, develop, test, review</td><td>Correct, detailed explanations and complete, working evidence. Some small inaccuracies are allowed, and your review may be one-sided.</td></tr>
<tr><td><span class="badge m">Merit</span></td><td>Analyse, justify, optimise</td><td>You show <em>how</em> and <em>why</em>: components are analysed in depth, design decisions are backed by requirements and technical reasons, and you improve the network based on your tests. Technically accurate throughout.</td></tr>
<tr><td><span class="badge d">Distinction</span></td><td>Evaluate, demonstrate</td><td>Balanced judgements supported by evidence and reasoned examples, reaching justified conclusions and future recommendations. Fluent technical vocabulary and connected chains of reasoning. For BC.D3, clear evidence that you managed yourself and the project throughout.</td></tr>
</tbody></table></div><p class="small">Meet every Pass criterion first. Merit and Distinction build on the same work: they are about the depth of your thinking, not the length.</p></section>"""
    rules = """<section class="card"><h2>Your own work, and using AI properly</h2><div class="warnbox"><p>BTEC assignments must be your own work. You sign a declaration saying so. Copying from the internet, another student or an AI tool, even if you change the words, is malpractice and can mean losing the unit.</p></div>
<ul class="list"><li><strong>Allowed:</strong> asking the AI tutor or coach to explain an idea, quiz you, check what a task is asking, help you plan, or tell you what is missing from <em>your</em> draft.</li>
<li><strong>Not allowed:</strong> asking any AI to write paragraphs, tables, emails, designs or evaluations for you, or copying AI wording into your work.</li>
<li><strong>Be open:</strong> the Assignment builder keeps an AI-use log of every question you ask the coach. Download it and hand it in, and tell your teacher how AI helped you.</li>
<li>Do not put personal details (yours or anyone else’s) into the tutor.</li></ul></section>"""
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unit 19 Assignment guide</title><link rel="stylesheet" href="u19.css"></head><body>
<div class="packnav">{pack_nav()}</div>
<header class="hero"><h1>1. Assignment guide</h1><p>Unit 19 is assessed by two assignments set by your teacher. This page explains what each task asks, in plain English, and what a strong answer includes. Always follow your teacher’s official brief and deadlines.</p></header>
<div class="wrap">{grades}{"".join(parts)}{rules}</div>
<footer>Plain-language guide based on the Pearson BTEC Level 3 Unit 19 specification and this centre’s assignment briefs. The official brief from your teacher always takes priority.</footer></body></html>"""
    (OUT / "brief.html").write_text(page)


if __name__ == "__main__":
    ids = build_learning()
    build_workbook(ids)
    build_brief()
    print("Built Unit 19:", ", ".join(ids))
