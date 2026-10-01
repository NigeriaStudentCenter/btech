"""Build the Unit 12 Software Development pages (BTEC First ICT, Unit 12).

Run from the repo root:  python3 tools/build_unit12.py
Writes docs/unit12/{learning,index,guide,videos,start,practicals,quizzes,exam,teachers}.html, docs/unit12/workbook.js and api/sections-u12.json.
Content lives in tools/unit12/.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "unit12"))
sys.path.insert(0, str(ROOT / "tools"))
import u12_a, u12_b, workbook_u12, videos_u12, pages_u12  # noqa: E402
from build_unit19 import LEARN_CSS  # noqa: E402

OUT = ROOT / "docs" / "unit12"
OUT.mkdir(parents=True, exist_ok=True)
esc = lambda t: html.escape(str(t), quote=True)

NAV_ITEMS = [("start.html", "Start"), ("brief.html", "1. Assignment guide"), ("learning.html", "2. Learn"), ("index.html", "3. Workbook + tutor"),
             ("practicals.html", "4. Practicals"), ("assignment.html", "5. Assignment builder"), ("quizzes.html", "6. Quizzes"), ("videos.html", "7. Videos"), ("teachers.html", "Teachers")]
GROUPS = {"A": "A · Characteristics and uses", "B": "B · Design a program", "C": "C · Develop and test", "D": "D · Review"}

def pack_nav():
    return '<nav aria-label="Course pack">' + "".join(f'<a href="{h}">{t}</a>' for h, t in NAV_ITEMS) + "</nav>"


def group_of(lid):
    return lid[0]


def build_learning():
    lessons, ids, titles = [], [], []
    for l in u12_a.LESSONS + u12_b.LESSONS:
        lid = re.search(r'<article id="([^"]+)"', l).group(1)
        anchor = f'<a class="next" href="index.html?section={lid}">'
        lessons.append(l.replace(anchor, videos_u12.for_lesson(lid) + anchor))
        ids.append(lid)
        titles.append(re.search(r"<h2>(.*?)</h2>", l).group(1))
    side, last = [], None
    for i, t in zip(ids, titles):
        g = GROUPS.get(group_of(i))
        if g and g != last:
            side.append(f'<p class="aim">{g}</p>')
            last = g
        side.append(f'<a href="#{i}">{i} {t}</a>')
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unit 12 Learn: Software Development</title><style>{LEARN_CSS}
.warnbox{{background:#fdecea;border:1px solid #e5b3ad;border-radius:10px;padding:12px 16px;margin:14px 0}}
{videos_u12.CSS}</style></head><body>
<div class="packnav">{pack_nav()}</div>
<header><h1>Unit 12: Software Development</h1><p>BTEC First in Information and Creative Technology: how programs work, how to design them, and how to develop, test and review your own program in Visual Basic.</p><p>Read the lesson, study the diagrams, watch the video, then open the matching workbook section.</p></header>
<main><nav aria-label="Lessons"><h2>Lessons</h2>{''.join(side)}</nav><div>{''.join(lessons)}</div></main>
<footer>Original teaching material written for this course and mapped to the Pearson BTEC First ICT Unit 12 specification. Diagrams are simplified learning models. Videos are embedded from YouTube and belong to their creators. Not an official awarding-organisation publication.</footer><script>{videos_u12.JS}</script></body></html>"""
    (OUT / "learning.html").write_text(page)
    return ids


def build_workbook(ids):
    data = workbook_u12.SECTIONS
    assert [s["id"] for s in data] == ids, ids
    (ROOT / "api" / "sections-u12.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    u2 = (ROOT / "docs" / "index.html").read_text()
    style = re.search(r"<style>.*?</style>", u2, re.S).group(0)
    main = re.search(r"<main>.*?</main>", u2, re.S).group(0).replace("The tutor needs the school to set up its AI service.", "Ask about this lesson. Do not include personal information.")
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unit 12 Workbook</title>{style}<style>nav[aria-label="Course pack"]{{display:flex;gap:18px;flex-wrap:wrap;background:none;border:0;padding:0}}@media(max-width:720px){{#menu{{grid-template-columns:repeat(2,minmax(0,1fr))!important}}#menu button{{white-space:normal;overflow-wrap:anywhere}}}}</style></head><body>
<div style="padding:16px;background:#fff;color:#17334b">{pack_nav()}</div><header><h1>Unit 12 Software Development Workbook</h1><p>Learn, practise, check yourself and ask the tutor</p><p><a id="backToLearning" href="learning.html" style="color:white">← Read the lesson</a></p></header>
{main}
<script id="courseData" type="application/json">{json.dumps(data, ensure_ascii=False)}</script><script src="../config.js"></script><script src="workbook.js"></script></body></html>"""
    (OUT / "index.html").write_text(page)
    js = (ROOT / "docs" / "workbook.js").read_text()
    js = js.replace("'unit2-workbook-v1'", "'unit12-workbook-v1'").replace("body:JSON.stringify({section:current,", "body:JSON.stringify({course:'u12',section:current,")
    js = js.replace("'my-computing-work.json'", "'my-software-dev-work.json'").replace("'my-computing-'+current", "'my-software-dev-'+current")
    assert "unit12-workbook-v1" in js and "course:'u12'" in js
    (OUT / "workbook.js").write_text(js)


GRADE_CLASS = {"Pass": "p", "Merit": "m", "Distinction": "d"}


def build_brief():
    data = json.loads((ROOT / "api" / "assignments-u12.json").read_text())
    (OUT / "assignments.json").write_text((ROOT / "api" / "assignments-u12.json").read_text())
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
    grades = """<section class="card"><h2>Level 1, Pass, Merit and Distinction</h2><div class="tablewrap"><table><thead><tr><th>Grade</th><th>Typical command words</th><th>What the assessor looks for</th></tr></thead><tbody>
<tr><td><span class="badge p">Level 1</span></td><td>Identify, produce with guidance</td><td>You can identify the main points and complete the work with help from your teacher.</td></tr>
<tr><td><span class="badge p">Level 2 Pass</span></td><td>Explain, describe, produce, develop, test</td><td>Clear explanations in your own words and complete, working evidence: a design, a program with comments, and a completed test plan.</td></tr>
<tr><td><span class="badge m">Level 2 Merit</span></td><td>Comment on, produce a detailed…, review the extent</td><td>More depth: alternatives in your design, a fully functional program, feedback from others used to improve it, and judgements about how far it meets the requirements.</td></tr>
<tr><td><span class="badge d">Level 2 Distinction</span></td><td>Discuss, justify, refine, evaluate</td><td>Balanced arguments and reasons: justify design decisions against requirements and constraints, refine code for quality, compare the final program with your design and recommend improvements.</td></tr>
</tbody></table></div><p class="small">Meet every Pass criterion first. Merit and Distinction build on the same work: they are about the quality of your thinking, not the length.</p></section>"""
    rules = """<section class="card"><h2>Your own work, and using AI properly</h2><div class="warnbox"><p>BTEC assignments must be your own work. You sign a declaration saying so. Copying from the internet, another student or an AI tool, even if you change the words, is malpractice and can mean losing the unit.</p></div>
<ul class="list"><li><strong>Allowed:</strong> asking the AI tutor or coach to explain an idea, quiz you, check what a task is asking, help you plan, or tell you what is missing from <em>your</em> draft.</li>
<li><strong>Not allowed:</strong> asking any AI to write your code, pseudocode, designs, test plans or reviews, or copying AI code or wording into your work. Your program must be written by you.</li>
<li><strong>Be open:</strong> the Assignment builder keeps an AI-use log of every question you ask the coach. Download it and hand it in, and tell your teacher how AI helped you.</li>
<li>Do not put personal details (yours or anyone else’s) into the tutor.</li></ul></section>"""
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unit 12 Assignment guide</title><link rel="stylesheet" href="../unit19/u19.css"></head><body>
<div class="packnav">{pack_nav()}</div>
<header class="hero"><h1>1. Assignment guide</h1><p>Unit 12 is assessed by three assignments set by your teacher. This page explains what each task asks, in plain English, and what a strong answer includes. Always follow your teacher’s official brief and deadlines.</p></header>
<div class="wrap">{grades}{"".join(parts)}{rules}</div>
<footer>Plain-language guide based on the Pearson BTEC First ICT Unit 12 specification and scheme of work. The official brief from your teacher always takes priority.</footer></body></html>"""
    (OUT / "brief.html").write_text(page)


def build_videos():
    titles = {w["id"]: w["title"] for w in workbook_u12.SECTIONS}
    groups = []
    for lid in [w["id"] for w in workbook_u12.SECTIONS] + [None]:
        vs = [v for v in videos_u12.VIDEOS if v["lesson"] == lid]
        if not vs:
            continue
        head = f'{lid} {esc(titles[lid])}' if lid else "Extra revision"
        link = f'<p class="small"><a href="learning.html#{lid}">Open the lesson →</a></p>' if lid else '<p class="small">Useful background from the same video series.</p>'
        groups.append(f'<section class="card"><h2>{head}</h2>{link}{"".join(videos_u12.card(v) for v in vs)}</section>')
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unit 12 Videos</title><link rel="stylesheet" href="../unit19/u19.css"><style>{videos_u12.CSS}</style></head><body>
<div class="packnav">{pack_nav()}</div>
<header class="hero"><h1>7. Videos</h1><p>{len(videos_u12.VIDEOS)} videos: the MrBrownCS programming series, Visual Basic walk-throughs, and explainers from TED-Ed and Computerphile. Watch, then answer the “watch and think” questions.</p></header>
<div class="wrap"><div class="note">Videos play from YouTube in privacy-enhanced mode, only when you press play. If YouTube is blocked, ask your teacher for the copies on Teams.</div>{"".join(groups)}</div>
<footer>Videos are embedded from YouTube and belong to their creators (MrBrownCS, TED-Ed, Computerphile, freeCodeCamp and others). They are not hosted on this site.</footer>
<script>{videos_u12.JS}</script></body></html>"""
    (OUT / "videos.html").write_text(page)


def build_static(ids):
    nav = pack_nav()
    (OUT / "start.html").write_text(pages_u12.start(nav, len(ids), len(videos_u12.VIDEOS)))
    (OUT / "practicals.html").write_text(pages_u12.practicals(nav))
    (OUT / "quizzes.html").write_text(pages_u12.quizzes(nav))
    (OUT / "assignment.html").write_text(pages_u12.assignment(nav))
    (OUT / "assignment.js").write_text(pages_u12.assignment_js())
    deck = OUT / "teacher" / DECK
    size = f"{deck.stat().st_size / 1e6:.1f} MB" if deck.exists() else "PowerPoint"
    (OUT / "teachers.html").write_text(pages_u12.teachers(nav, DECK, size, DECK_SLIDES))


DECK = "Unit12-Software-Development-Teacher-Deck.pptx"
DECK_SLIDES = 28


if __name__ == "__main__":
    ids = build_learning()
    build_workbook(ids)
    build_brief()
    build_videos()
    build_static(ids)
    print("Built Unit 12:", ", ".join(ids))
