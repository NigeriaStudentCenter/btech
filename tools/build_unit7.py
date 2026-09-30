"""Build the Unit 7 Digital environments pages (T Level core content area 7).

Run from the repo root:  python3 tools/build_unit7.py
Writes docs/unit7/{learning,index,guide,videos,start,practicals,quizzes,exam,teachers}.html, docs/unit7/workbook.js and api/sections-u7.json.
Content lives in tools/unit7/.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "unit7"))
sys.path.insert(0, str(ROOT / "tools"))
import u7_a, u7_b, u7_c, workbook_u7, videos_u7, pages_u7  # noqa: E402
from build_unit19 import LEARN_CSS  # noqa: E402

OUT = ROOT / "docs" / "unit7"
OUT.mkdir(parents=True, exist_ok=True)
esc = lambda t: html.escape(str(t), quote=True)

NAV_ITEMS = [("start.html", "Start"), ("guide.html", "1. Course guide"), ("learning.html", "2. Learn"), ("index.html", "3. Workbook + tutor"),
             ("practicals.html", "4. Practicals"), ("exam.html", "5. Exam practice"), ("quizzes.html", "6. Quizzes"), ("videos.html", "7. Videos"), ("teachers.html", "Teachers")]
GROUPS = {"NS": "Number systems", "H": "7.1 Hardware", "S": "7.2 Software", "N": "7.3 Networks", "V": "7.4–7.6 Virtual, cloud and resilience", "C": None, "R": None}
SPEC_TO_LESSON = {"7.1.1": "H1", "7.1.2": "H2", "7.2.1": "SW1", "7.2.2": "SW2", "7.2.3": "SW3", "7.2.4": "SW4", "7.3.1": "N1", "7.3.2": "N1", "7.3.3": "N2", "7.3.4": "N3", "7.3.5": "N3",
                  "7.3.6": "N4", "7.3.7": "N5", "7.3.8": "N5", "7.3.9": "N6", "7.3.10": "N7", "7.3.11": "N8", "7.4.1": "V1", "7.4.2": "V1", "7.4.3": "V1", "7.4.4": "V1",
                  "7.5.1": "C1", "7.5.2": "C1", "7.5.3": "C1", "7.6.1": "R1", "7.6.2": "R1"}


def pack_nav():
    return '<nav aria-label="Course pack">' + "".join(f'<a href="{h}">{t}</a>' for h, t in NAV_ITEMS) + "</nav>"


def group_of(lid):
    return "NS" if lid == "NS" else lid[0]


def build_learning():
    lessons, ids, titles = [], [], []
    for l in u7_a.LESSONS + u7_b.LESSONS + u7_c.LESSONS:
        lid = re.search(r'<article id="([^"]+)"', l).group(1)
        anchor = f'<a class="next" href="index.html?section={lid}">'
        lessons.append(l.replace(anchor, videos_u7.for_lesson(lid) + anchor))
        ids.append(lid)
        titles.append(re.search(r"<h2>(.*?)</h2>", l).group(1))
    side, last = [], None
    for i, t in zip(ids, titles):
        g = GROUPS.get(group_of(i))
        if g and g != last:
            side.append(f'<p class="aim">{g}</p>')
            last = g
        side.append(f'<a href="#{i}">{i} {t}</a>')
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unit 7 Learn: Digital environments</title><style>{LEARN_CSS}
{videos_u7.CSS}</style></head><body>
<div class="packnav">{pack_nav()}</div>
<header><h1>Unit 7: Digital environments</h1><p>T Level Digital core content area 7: hardware, software, networks, virtual and cloud environments, and resilience.</p><p>Read the lesson, study the diagrams, watch the video, then open the matching workbook section.</p></header>
<main><nav aria-label="Lessons"><h2>Lessons</h2>{''.join(side)}</nav><div>{''.join(lessons)}</div></main>
<footer>Original teaching material written for this course and mapped to T Level Digital core content area 7. Diagrams are simplified learning models. Videos are embedded from YouTube and belong to their creators. Not an official awarding-organisation publication.</footer><script>{videos_u7.JS}</script></body></html>"""
    (OUT / "learning.html").write_text(page)
    return ids


def build_workbook(ids):
    data = workbook_u7.SECTIONS
    assert [s["id"] for s in data] == ids, ids
    (ROOT / "api" / "sections-u7.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    u2 = (ROOT / "docs" / "index.html").read_text()
    style = re.search(r"<style>.*?</style>", u2, re.S).group(0)
    main = re.search(r"<main>.*?</main>", u2, re.S).group(0).replace("The tutor needs the school to set up its AI service.", "Ask about this lesson. Do not include personal information.")
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unit 7 Workbook</title>{style}<style>nav[aria-label="Course pack"]{{display:flex;gap:18px;flex-wrap:wrap;background:none;border:0;padding:0}}@media(max-width:720px){{#menu{{grid-template-columns:repeat(2,minmax(0,1fr))!important}}#menu button{{white-space:normal;overflow-wrap:anywhere}}}}</style></head><body>
<div style="padding:16px;background:#fff;color:#17334b">{pack_nav()}</div><header><h1>Unit 7 Digital Environments Workbook</h1><p>Learn, practise, check yourself and ask the tutor</p><p><a id="backToLearning" href="learning.html" style="color:white">← Read the lesson</a></p></header>
{main}
<script id="courseData" type="application/json">{json.dumps(data, ensure_ascii=False)}</script><script src="../config.js"></script><script src="workbook.js"></script></body></html>"""
    (OUT / "index.html").write_text(page)
    js = (ROOT / "docs" / "workbook.js").read_text()
    js = js.replace("'unit2-workbook-v1'", "'unit7-workbook-v1'").replace("body:JSON.stringify({section:current,", "body:JSON.stringify({course:'u7',section:current,")
    js = js.replace("'my-computing-work.json'", "'my-digital-environments-work.json'").replace("'my-computing-'+current", "'my-digital-environments-'+current")
    assert "unit7-workbook-v1" in js and "course:'u7'" in js
    (OUT / "workbook.js").write_text(js)


def build_guide():
    spec = json.loads((ROOT / "tools" / "unit7" / "spec_u7.json").read_text())
    rows = []
    for it in spec:
        if "heading" in it:
            rows.append(f'<tr class="head"><th colspan="3">{esc(it["heading"])}</th></tr>')
            continue
        pts = "".join(f"<li>{esc(pt.replace(': —', ':'))}</li>" for pt in it["points"])
        lid = SPEC_TO_LESSON[it["code"]]
        rows.append(f'<tr data-code="{esc(it["code"])}"><td><strong>{esc(it["code"])}</strong><br><a href="learning.html#{lid}">lesson {lid}</a></td><td>{esc(it["text"])}{("<ul>" + pts + "</ul>") if pts else ""}</td>'
                    f'<td class="rag"><div role="radiogroup" aria-label="How confident are you with {esc(it["code"])}?">'
                    + "".join(f'<button type="button" data-v="{v}" aria-pressed="false">{t}</button>' for v, t in (("r", "Need to work on it"), ("a", "Getting there"), ("g", "Happy")))
                    + "</div></td></tr>")
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unit 7 Course guide</title><link rel="stylesheet" href="../unit19/u19.css">
<style>tr.head th{{background:#12324f;color:#fff}}td ul{{margin:6px 0 0 18px;padding:0;font-size:.9rem;color:#405870}}.rag div{{display:flex;flex-direction:column;gap:6px}}.rag button{{font-size:.82rem;padding:6px 8px;text-align:left}}
.rag button[aria-pressed=true][data-v=r]{{background:#f8d7d3;border-color:#c0392b;color:#7a1f15;font-weight:700}}.rag button[aria-pressed=true][data-v=a]{{background:#fbe8c4;border-color:#b7791f;color:#6b4510;font-weight:700}}.rag button[aria-pressed=true][data-v=g]{{background:#d6f0e2;border-color:#1d7a45;color:#135230;font-weight:700}}
.summary{{display:flex;gap:12px;flex-wrap:wrap}}.summary span{{border-radius:999px;padding:4px 12px;font-weight:700;font-size:.9rem}}.s-r{{background:#f8d7d3}}.s-a{{background:#fbe8c4}}.s-g{{background:#d6f0e2}}.s-n{{background:#eef0f3}}
@media(max-width:640px){{td{{font-size:.9rem}}.rag button{{font-size:.78rem}}}}</style></head><body>
<div class="packnav">{pack_nav()}</div>
<header class="hero"><h1>1. Course guide</h1><p>What content area 7 covers, how it is assessed, and a checklist to track how confident you feel about every part of the specification.</p></header>
<div class="wrap">
<section class="card"><h2>How this unit is assessed</h2>
<p>Content area 7 (Digital environments) is part of the T Level Digital <strong>core</strong>. It is assessed by a <strong>written exam</strong> (about 2.5 hours) alongside other core content areas, not by coursework. Your teacher will confirm the paper, date and format.</p>
<ul class="list"><li><strong>Short-answer questions</strong> check that you know and can explain the content (state, identify, describe, explain).</li>
<li><strong>Scenario questions</strong> ask you to apply it to a business or client, e.g. recommend hardware, a network type or a cloud model and justify it.</li>
<li><strong>Extended questions</strong> ask you to discuss or evaluate: weigh up benefits and drawbacks and reach a supported conclusion.</li></ul>
<p>Use the <a href="exam.html">Exam practice</a> page to rehearse all three, and the <a href="quizzes.html">Quizzes</a> for quick checks.</p></section>
<section class="card"><h2>My specification checklist</h2><p>For each point, choose how you feel. Your choices save on this device. Revisit the <strong>red</strong> and <strong>amber</strong> points first.</p>
<p class="summary" id="summary"></p><div class="tools"><button type="button" id="printList">Print my checklist</button><button type="button" id="resetList">Clear my ratings</button></div>
<div class="tablewrap"><table><thead><tr><th>Spec</th><th>You need to understand…</th><th>How confident am I?</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div></section>
</div>
<footer>Specification points are listed to help you revise. Always check with your teacher for the current specification and exam arrangements.</footer>
<script>
(()=>{{const KEY='unit7-checklist-v1';let s={{}};try{{s=JSON.parse(localStorage.getItem(KEY)||'{{}}')||{{}}}}catch{{}}
const rows=[...document.querySelectorAll('tr[data-code]')];
const draw=()=>{{let c={{r:0,a:0,g:0}};rows.forEach(tr=>{{const v=s[tr.dataset.code];tr.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.v===v)));if(c[v]!==undefined)c[v]++}});const n=rows.length-c.r-c.a-c.g;
document.getElementById('summary').innerHTML=`<span class="s-r">${{c.r}} need work</span><span class="s-a">${{c.a}} getting there</span><span class="s-g">${{c.g}} happy</span><span class="s-n">${{n}} not rated</span>`}};
rows.forEach(tr=>tr.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{{s[tr.dataset.code]=s[tr.dataset.code]===b.dataset.v?undefined:b.dataset.v;try{{localStorage.setItem(KEY,JSON.stringify(s))}}catch{{}};draw()}})));
document.getElementById('printList').onclick=()=>window.print();document.getElementById('resetList').onclick=()=>{{if(confirm('Clear all your ratings on this device?')){{s={{}};try{{localStorage.removeItem(KEY)}}catch{{}};draw()}}}};draw()}})();
</script></body></html>"""
    (OUT / "guide.html").write_text(page)


def build_videos():
    titles = {w["id"]: w["title"] for w in workbook_u7.SECTIONS}
    groups = []
    for lid in [w["id"] for w in workbook_u7.SECTIONS] + [None]:
        vs = [v for v in videos_u7.VIDEOS if v["lesson"] == lid]
        if not vs:
            continue
        head = f'{lid} {esc(titles[lid])}' if lid else "Extra revision (outside content area 7)"
        link = f'<p class="small"><a href="learning.html#{lid}">Open the lesson →</a></p>' if lid else '<p class="small">Useful background from the same video series.</p>'
        groups.append(f'<section class="card"><h2>{head}</h2>{link}{"".join(videos_u7.card(v) for v in vs)}</section>')
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unit 7 Videos</title><link rel="stylesheet" href="../unit19/u19.css"><style>{videos_u7.CSS}</style></head><body>
<div class="packnav">{pack_nav()}</div>
<header class="hero"><h1>7. Videos</h1><p>{len(videos_u7.VIDEOS)} videos: the MrBrownCS revision series plus films from TED, Cisco and the Port of Long Beach. Watch, then answer the “watch and think” questions.</p></header>
<div class="wrap"><div class="note">Videos play from YouTube in privacy-enhanced mode, only when you press play. If YouTube is blocked, ask your teacher for the copies on Teams.</div>{"".join(groups)}</div>
<footer>Videos are embedded from YouTube and belong to their creators (MrBrownCS, TED, Cisco and others). They are not hosted on this site.</footer>
<script>{videos_u7.JS}</script></body></html>"""
    (OUT / "videos.html").write_text(page)


def build_static(ids):
    nav = pack_nav()
    (OUT / "start.html").write_text(pages_u7.start(nav, len(ids), len(videos_u7.VIDEOS)))
    (OUT / "practicals.html").write_text(pages_u7.practicals(nav))
    (OUT / "quizzes.html").write_text(pages_u7.quizzes(nav))
    (OUT / "exam.html").write_text(pages_u7.exam(nav))
    deck = OUT / "teacher" / DECK
    size = f"{deck.stat().st_size / 1e6:.1f} MB" if deck.exists() else "PowerPoint"
    (OUT / "teachers.html").write_text(pages_u7.teachers(nav, DECK, size, DECK_SLIDES))


DECK = "Unit7-Digital-Environments-Teacher-Deck.pptx"
DECK_SLIDES = 33


if __name__ == "__main__":
    ids = build_learning()
    build_workbook(ids)
    build_guide()
    build_videos()
    build_static(ids)
    print("Built Unit 7:", ", ".join(ids))
