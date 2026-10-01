"""Add videos, 'From your lessons' content, diagram tasks, a videos page and a teachers page to the Unit 2 pack.

Run from the repo root:  python3 tools/build_unit2_extras.py   (after tools/build_learning.py)
Idempotent: inserted blocks sit between <!-- extras:ID --> markers and are replaced on every run.
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "unit2"))
import videos_u2, enrich_u2, tasks_u2  # noqa: E402

DOCS = ROOT / "docs"
esc = lambda t: html.escape(str(t), quote=True)
SECTIONS = "A1 A2 A3 B1 B2 B3 C1 C2 C3 D1 D2 E1 E2 E3 F1 F2".split()
TITLES = {}
NAV_TAIL = '<a href="tasks.html">6. Diagram tasks</a><a href="videos.html">7. Videos</a><a href="teachers.html">Teachers</a>'
NAV = ('<a href="start.html">Start</a><a href="brief.html">1. Brief</a><a href="learning.html">2. Learn</a><a href="index.html">3. Workbook + tutor</a>'
       '<a href="revision.html">4. Revision</a><a href="past-papers.html">5. Past Exam Papers</a>' + NAV_TAIL)
DECK = "Unit2-Fundamentals-Teacher-Deck.pptx"
DECK_SLIDES = 30


def update_nav():
    for f in ["start.html", "brief.html", "learning.html", "index.html", "revision.html", "past-papers.html"]:
        p = DOCS / f
        t = p.read_text()
        t2 = re.sub(r'(<nav aria-label="Student pack"[^>]*>).*?(</nav>)', lambda m: m.group(1) + NAV + m.group(2), t, count=1, flags=re.S)
        assert t2.count(NAV_TAIL) == 1, f
        p.write_text(t2)


def update_workbook():
    p = DOCS / "index.html"
    t = re.sub(r"/\*extras-css\*/.*?/\*/extras-css\*/", "", p.read_text(), flags=re.S)
    t = t.replace("</style>", "/*extras-css*/@media(max-width:720px){#menu{grid-template-columns:repeat(2,minmax(0,1fr))!important}#menu button{white-space:normal;overflow-wrap:anywhere;min-width:0}}/*/extras-css*/</style>", 1)
    p.write_text(t)


def update_start():
    p = DOCS / "start.html"
    t = re.sub(r"<!-- extras:cards -->.*?<!-- /extras:cards -->", "", p.read_text(), flags=re.S)
    cards = ('<!-- extras:cards --><a href="tasks.html"><h2>6. Diagram tasks</h2><p>Label the motherboard, connectors, ports, CPU, logic gates and RAID from the drop-down lists, with instant marking.</p></a>'
             f'<a href="videos.html"><h2>7. Videos</h2><p>{len(videos_u2.VIDEOS)} short videos for every topic, from binary to error correction.</p></a>'
             '<a href="teachers.html"><h2>For teachers</h2><p>The teacher PowerPoint, the scheme of work map and how the AI tutor works.</p></a><!-- /extras:cards -->')
    i = t.index('<div class="cards">')
    j = t.index("</div>", i)
    t = t[:j] + cards + t[j:]
    t = t.replace("Work through the five parts below.", "Work through the parts below.")
    p.write_text(t)


def update_learning():
    p = DOCS / "learning.html"
    t = p.read_text()
    t = re.sub(r"/\*extras-css\*/.*?/\*/extras-css\*/", "", t, flags=re.S)
    t = t.replace("</style>", "/*extras-css*/" + videos_u2.CSS + ".more{border-top-color:#7b5aa6}.more .deeper-title{color:#6a3fa0}h3.watch{margin-top:26px}.small{font-size:.9rem;color:#405870}/*/extras-css*/</style>", 1)
    t = re.sub(r"<!-- extras-js -->.*?<!-- /extras-js -->", "", t, flags=re.S)
    t = t.replace("</body>", f"<!-- extras-js --><script>{videos_u2.JS}</script><!-- /extras-js --></body>", 1)
    for sid in SECTIONS:
        t = re.sub(rf"<!-- extras:{sid} -->.*?<!-- /extras:{sid} -->", "", t, flags=re.S)
        anchor = f'<a class="next" href="index.html?section={sid}">'
        assert t.count(anchor) == 1, sid
        block = enrich_u2.SECTIONS.get(sid, "") + videos_u2.for_lesson(sid)
        if block:
            t = t.replace(anchor, f"<!-- extras:{sid} -->{block}<!-- /extras:{sid} -->" + anchor)
        s = t.index(f'<article id="{sid}"')
        TITLES[sid] = re.sub("<[^>]+>", "", re.search(r"<h2>(.*?)</h2>", t[s:]).group(1))
    p.write_text(t)


def shell(title, h1, lead, body, style=""):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>'
            f'<link rel="stylesheet" href="unit19/u19.css"><style>nav[aria-label="Student pack"]{{display:flex;gap:18px;flex-wrap:wrap}}{style}</style></head><body>\n'
            f'<div class="packnav"><nav aria-label="Student pack">{NAV}</nav></div>\n<header class="hero"><h1>{h1}</h1><p>{lead}</p></header>\n<div class="wrap">\n{body}\n</div>\n'
            '<footer>Original course material for the Pearson BTEC Level 3 Nationals in Computing, Unit 2: Fundamentals of Computer Systems. Not a Pearson publication. Diagrams are original drawings, not to scale.</footer>\n')


def build_tasks():
    toc = "".join(f'<li><a href="#{t["id"]}">{esc(t["title"])}</a></li>' for t in tasks_u2.TASKS)
    body = (f'<div class="card"><h2>How to use these tasks</h2><p>Your teacher’s labelling worksheets, redrawn so you can do them on screen. Choose an answer from each drop-down list, then press <strong>Check my answers</strong>. Your choices save on this device. Stuck? Each task links to its lesson and to the AI tutor.</p><ol id="toc">{toc}</ol></div>'
            + "".join(tasks_u2.render_task(t) for t in tasks_u2.TASKS))
    page = shell("Unit 2 Diagram tasks", "6. Diagram tasks", "Label the diagrams and match the parts: motherboard, connectors, ports, devices, components, number bases, the CPU, logic gates and RAID.", body, tasks_u2.CSS)
    (DOCS / "tasks.html").write_text(page + f"<script>{tasks_u2.JS}</script></body></html>\n")


def build_videos():
    groups = []
    for lid in SECTIONS + [None]:
        vs = [v for v in videos_u2.VIDEOS if v["lesson"] == lid]
        if not vs:
            continue
        head = f"{lid} {esc(TITLES[lid])}" if lid else "Extra revision: networks and protocols"
        link = f'<p class="small"><a href="learning.html#{lid}">Open the lesson →</a></p>' if lid else ""
        groups.append(f'<section class="card"><h2>{head}</h2>{link}{"".join(videos_u2.card(v) for v in vs)}</section>')
    body = '<div class="note">These are the department’s revision videos (the MrBrownCS series) plus extra explainers, played from YouTube in privacy-enhanced mode only when you press play. If YouTube is blocked, ask your teacher for the copies on Teams.</div>' + "".join(groups)
    page = shell("Unit 2 Videos", "7. Videos", f"{len(videos_u2.VIDEOS)} short videos for every Unit 2 topic. Watch, then answer the ‘watch and think’ questions.", body, videos_u2.CSS)
    (DOCS / "videos.html").write_text(page + f"<script>{videos_u2.JS}</script></body></html>\n")


SOW = [("A1 Hardware", "types of computer, internal components, connectors and ports, servers, RAID/NAS/SAN, choosing hardware, mobile devices", "A1", "1, 2, 3, 4, 5, 9"),
       ("A2 Software", "operating systems, kernel, networking and security, user interfaces, choosing an OS, utilities, applications, open source, disk cache, backup", "A2", "–"),
       ("A3 Data processing", "collecting, processing, sharing and backing up data", "A3", "–"),
       ("B Computer architecture", "Von Neumann and Harvard, clusters, NUMA, fetch–decode–execute, pipelining, registers, interrupts", "B1–B3", "7"),
       ("C Data representation", "binary, octal, hex, BCD, arithmetic, two’s complement, floating point, text, images", "C1–C3", "6"),
       ("D Data organisation", "data structures, arrays and matrices", "D1, D2", "–"),
       ("E Data transmission", "serial/parallel, synchronous/asynchronous, protocols, encryption (Caesar, Vigenère), VoIP, error detection and correction", "E1–E3", "–"),
       ("F Logic and data flow", "logic gates, truth tables, Boolean expressions, adders, flowcharts and system diagrams", "F1, F2", "8")]


def build_teachers():
    deck = DOCS / "teacher" / DECK
    size = f"{deck.stat().st_size / 1e6:.1f} MB" if deck.exists() else "PowerPoint"
    rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in SOW)
    body = f"""<section class="card"><h2>Teacher PowerPoint</h2>
<p>A {DECK_SLIDES}-slide delivery deck with full speaker notes, covering learning aims A–F. Each lesson slide follows the department routine (starter, aim, teach, practical, task, check, flipped homework) and points to the matching Learn section, diagram task, video and revision test.</p>
<div class="tools"><a class="primary" href="teacher/{DECK}" download style="display:inline-block;padding:10px 16px;border-radius:8px;background:var(--accent);color:#fff;text-decoration:none">Download the teacher deck (.pptx, {size})</a></div></section>
<section class="card"><h2>How the pack maps to your topics</h2><div class="tablewrap"><table><thead><tr><th>Topic</th><th>Covers</th><th>Learn</th><th>Diagram task</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="small">Your PowerPoints, cheat sheets, numbers and logic booklets, starters (Millionaire, matching games), examiner reports and the sample assessment material stay on Teams. Pearson and dexgraphics materials are not reproduced on this public site; the diagram tasks are original redrawings of your labelling worksheets.</p></section>
<section class="card"><h2>What students have</h2><ul class="list">
<li><strong>2. Learn:</strong> 16 sections with ‘Go deeper’ diagrams, new ‘From your lessons’ blocks (ports and connectors, servers, SAN/NAS, choosing hardware, the kernel, interfaces, open source, disk cache, number bases, Vigenère, VoIP, universal gates) and embedded videos.</li>
<li><strong>3. Workbook + tutor:</strong> an activity per section with the AI study tutor.</li>
<li><strong>4. Revision</strong> (four tests) and <strong>5. Past Exam Papers</strong> with tutor help modes.</li>
<li><strong>6. Diagram tasks:</strong> nine drop-down labelling tasks with instant marking.</li>
<li><strong>7. Videos:</strong> {len(videos_u2.VIDEOS)} videos, including the MrBrownCS revision series from the department video folder.</li></ul></section>
<section class="card"><h2>AI study tutor</h2><p>The tutor is live on the college Azure service. It explains, diagnoses, gives one hint at a time and sets new practice questions; it will not give the answers to the workbook’s own activities, and it supports past-paper questions without inventing mark schemes. No names or accounts are used and nothing is stored on the server.</p></section>
<section class="card"><h2>Maintaining the pack</h2><p class="small">Run <code>python3 tools/build_learning.py</code> then <code>python3 tools/build_unit2_extras.py</code>. Videos are in <code>tools/unit2/videos_u2.py</code>, extra content in <code>enrich_u2.py</code>, diagram tasks in <code>tasks_u2.py</code>, and the deck in <code>tools/unit2/teacher_deck.js</code>.</p></section>"""
    (DOCS / "teachers.html").write_text(shell("Unit 2 for teachers", "For teachers", "Everything you need to deliver Unit 2 with this pack: the teacher PowerPoint, the topic map, the diagram tasks and the AI tutor.", body) + "</body></html>\n")


if __name__ == "__main__":
    update_nav()
    update_start()
    update_workbook()
    update_learning()
    build_tasks()
    build_videos()
    build_teachers()
    print("Unit 2 extras built:", len(videos_u2.VIDEOS), "videos,", len(tasks_u2.TASKS), "tasks")
