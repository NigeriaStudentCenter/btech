"""Static Unit 8 pages: start, practicals, exam practice, quizzes and teachers. Called by tools/build_unit8.py."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "unit7"))
from pages_u7 import HEAD, engine_page  # noqa: E402  shared page shell and quiz-engine page

U19 = ROOT / "docs" / "unit19"
FOOT = '<footer>Original course material written for the T Level in Digital Production, Design and Development, core content area 8: Security. Not an awarding-organisation publication. Cisco Packet Tracer is available free through Cisco Networking Academy.</footer>\n</body></html>\n'
OTHER = '<p class="small" style="text-align:center">Also on this site: <a href="../start.html">Unit 2: Fundamentals of Computer Systems</a> · <a href="../unit19/start.html">Unit 19: Computer Networking</a> · <a href="../unit7/start.html">Unit 7: Digital environments</a></p>'


def page(nav, title, h1, lead, body, style=""):
    return HEAD.format(title=title, style=style, nav=nav) + f'<header class="hero"><h1>{h1}</h1><p>{lead}</p></header>\n<div class="wrap">\n{body}\n</div>\n' + FOOT


def start(nav, n_lessons, n_videos):
    body = f"""<div class="cards">
<a href="guide.html"><h2>1. Course guide</h2><p>How the exam works, the command words, and a red/amber/green checklist of every specification point.</p></a>
<a href="learning.html"><h2>2. Learn</h2><p>{n_lessons} short lessons with diagrams, real cases, exam tips and check-yourself questions.</p></a>
<a href="index.html"><h2>3. Workbook + tutor</h2><p>A practice activity for every lesson, saved on your device, with the AI study tutor to help when you are stuck.</p></a>
<a href="practicals.html"><h2>4. Practicals</h2><p>Hands-on tasks: spot the phish, crack-proof passwords, Diffie-Hellman, Linux permissions, Nmap in a lab, a firewall in Packet Tracer.</p></a>
<a href="exam.html"><h2>5. Exam practice</h2><p>Exam-style scenarios with short and extended answers, command-word guidance and level marking.</p></a>
<a href="quizzes.html"><h2>6. Quizzes</h2><p>Five instant-marked quizzes: risks, threats, vulnerabilities, mitigation, and CIA and IAAA.</p></a>
<a href="videos.html"><h2>7. Videos</h2><p>{n_videos} videos, from MrBrownCS revision to Computerphile demos of real attacks.</p></a>
</div>
<div class="card"><h2>How to use this course</h2>
<ol class="steps">
<li>Open the <strong>Course guide</strong> and rate each specification point red, amber or green.</li>
<li>For each topic: read the <strong>lesson</strong>, watch its <strong>video</strong>, then complete the <strong>workbook</strong> activity.</li>
<li>Do the <strong>practicals</strong> when your teacher sets them.</li>
<li>Check yourself with the <strong>quizzes</strong>, then build exam technique with <strong>Exam practice</strong>.</li>
</ol>
<div class="warnbox"><strong>Stay legal and ethical.</strong> Only test, scan or attack systems you own or have written permission to use, such as the college lab. Using these techniques on other systems can be a criminal offence.</div>
<div class="note"><strong>This content area is assessed by a written exam.</strong> Use the AI tutor as much as you like to explain, quiz you, or check practice answers. Do not type your name or personal details into it.</div>
<p class="small">Work saves in this browser only. Use the download buttons to keep a backup before changing computers.</p></div>
{OTHER}"""
    return page(nav, "Unit 8 Security", "Unit 8: Security", "Why organisations protect information, the threats they face, how to stop them, and the models behind effective security. For T Level Digital students. No account needed.", body)


LABS = [
 ("lab1", "Spot the phish", "30 min", "T3", [
   "Your teacher gives you six messages (emails, texts and a phone script). Some are genuine, some are social engineering.",
   "For each, decide genuine or attack. If an attack, name the type (phishing, spear phishing, smishing, vishing, pharming, USB baiting).",
   "List every red flag you found: sender, urgency, greeting, links, attachments, requests.",
   "Write the one action a member of staff should take for each attack."],
  None, "Your completed table: good revision for 8.2.1."),
 ("lab2", "How strong is that password?", "30 min", "T2", [
   "Work out the number of combinations for a 6-letter lower-case password (26⁶) and an 8-character password using all 94 keyboard characters (94⁸).",
   "Compare with four random words from a 7,776-word list (7,776⁴). Which is easier to remember? Which is stronger?",
   "Read the NCSC password guidance your teacher provides. List three recommendations it makes.",
   "Write a password policy for a small business in five rules, and justify each."],
  "Your numbers match the brute-force chart on the Learn page.", "Your calculations and policy."),
 ("lab3", "Diffie-Hellman key exchange", "30 min", "M2", [
   "Open your teacher’s Diffie-Hellman spreadsheet. Follow the stages with P = 23, G = 9, a = 4, b = 3.",
   "Check Alice sends 6, Bob sends 16, and both reach the shared key 9.",
   "Now choose your own secret numbers with a partner (keep P = 23, G = 5) and repeat on paper.",
   "Explain in two sentences why an eavesdropper cannot easily work out the key."],
  "You and your partner reach the same key.", "Your working."),
 ("lab4", "Hashing and integrity", "20 min", "M2", [
   "On a lab PC, create a text file and find its hash: <code>certutil -hashfile notes.txt SHA256</code> (Windows) or <code>sha256sum notes.txt</code> (Linux).",
   "Change one character and hash it again. Compare the two hashes.",
   "Explain how a download site uses a published hash to prove a file has not been tampered with (integrity)."],
  "The hashes are completely different after a one-character change.", "Screenshots and your explanation."),
 ("lab5", "Linux users, groups and permissions", "50 min", "C2", [
   "In a Linux terminal or VM, practise <code>ls -l</code>, <code>pwd</code>, <code>cd</code>, <code>mkdir</code>, <code>cp</code> and <code>mv</code> from the Linux commands practical.",
   "Create a group and two users: <code>sudo groupadd hr</code>, <code>sudo useradd -m -G hr akhan</code>, <code>sudo useradd -m bjones</code>.",
   "Create a folder for HR and set permissions: <code>sudo chown root:hr /srv/hr</code> then <code>sudo chmod 770 /srv/hr</code>.",
   "Log in as each user and test access. Explain which part of IAAA each step shows.",
   "Run <code>last</code> and explain how login history supports accountability."],
  "akhan can open the folder; bjones is denied.", "Screenshots with captions."),
 ("lab6", "Nmap in the lab network", "60 min", "M4", [
   "Use only the Kali VM and lab DMZ network your teacher provides (10.6.6.0/24). Never scan any other network.",
   "Run <code>nmap -V</code> and <code>man nmap</code>. Complete the options table (-A, -O, -p, -sn, -sS, -sT, -sV, -T, -v, --open).",
   "Discover live hosts: <code>nmap -sn 10.6.6.0/24</code>.",
   "Scan one target for services and versions: <code>nmap -sV 10.6.6.23</code>.",
   "For each open port, name the service and say whether a defender should close it and why."],
  "You can explain what each open port means.", "Your options table and findings."),
 ("lab7", "Configure a firewall in Packet Tracer", "45 min", "M5", [
   "Build three PCs, a switch and a server: server 1.0.0.1, PCs 1.0.0.2–1.0.0.4, mask 255.0.0.0.",
   "Test ping and web access from every PC.",
   "On the server: Services → Firewall → On. Deny ICMP from 1.0.0.2 and allow ICMP from any other address.",
   "Test again. Then allow only HTTP and explain the effect of a default-deny rule."],
  "PC0 cannot ping the server; the others can.", "Screenshots of the rules and tests."),
 ("lab8", "Perimeter security proposal", "90 min", "V3", [
   "Read the warehouse scenario (customer entrance, staff door, loading bays, offices, supply closets).",
   "Define the outer perimeter, inner perimeter and interior, and one key vulnerability for each.",
   "Research access-control, monitoring and CCTV products with approximate costs.",
   "Present your recommendations in no more than five slides."],
  None, "Your five-slide proposal."),
 ("lab9", "Security policy for a small business", "60 min", "C1", [
   "Choose a business: a dental practice, an online shop or an accountancy firm.",
   "List its confidential information and the main threats it faces.",
   "Write a one-page policy covering passwords and MFA, access (roles), backups, updates, staff training and what to do in an incident.",
   "For each rule, name which part of the CIA triad it protects."],
  None, "Your policy: ideal revision for extended exam questions."),
 ("lab10", "Cisco Cybersecurity Essentials (optional)", "Self-paced", "T1", [
   "Enrol through your teacher’s Cisco Networking Academy class for the Cybersecurity Essentials course.",
   "Complete the modules on threats, access control and cryptography, including the Packet Tracer activities your teacher sets.",
   "Keep a list of any new terms and add them to your revision notes."],
  None, "Your course progress and badge."),
]


def practicals(nav):
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t, *_ in LABS)
    secs = []
    for n, (i, t, time, lesson, steps, check, evidence) in enumerate(LABS, 1):
        s = f'<section class="card lab" id="{i}"><h2>Practical {n}: {t}</h2><div class="meta"><span>{time}</span><span><a href="learning.html#{lesson}">Lesson {lesson}</a></span></div>\n<ol class="steps">' + "".join(f"<li>{x}</li>" for x in steps) + "</ol>"
        if check:
            s += f'<div class="check"><strong>Check it works:</strong> {check}</div>'
        s += f'<div class="evidence"><strong>Keep:</strong> {evidence}</div></section>'
        secs.append(s)
    style = """<style>.lab h2{margin-top:0}.meta{display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 12px}.meta span{font-size:.8rem;background:#eaf2f9;border-radius:999px;padding:2px 10px}
.evidence{background:#eaf6f3;border-radius:10px;padding:10px 16px;margin:12px 0}.check{background:#eef6ff;border-radius:10px;padding:10px 16px;margin:12px 0}
#toc{columns:2;column-gap:30px}#toc li{break-inside:avoid;margin:.3em 0}@media(max-width:640px){#toc{columns:1}}</style>"""
    body = f"""<div class="card"><h2>Before you start</h2>
<div class="warnbox"><strong>Rules for security practicals.</strong> Only scan, test or attack the lab systems your teacher gives you. Never use these tools on college, home or public networks, or on anyone else’s account. Unauthorised access is a criminal offence under computer misuse law.</div>
<ul class="list"><li>Practicals help you <em>understand</em>; the exam asks you to explain. After each one, write two sentences on what it taught you.</li>
<li>Cisco Packet Tracer is free through <a href="https://www.netacad.com" rel="noopener" target="_blank">netacad.com</a>. Your teacher has the Cisco activity files on Teams.</li></ul>
<ol id="toc">{toc}</ol></div>
{"".join(secs)}"""
    return page(nav, "Unit 8 Practicals", "4. Practicals", "Hands-on security tasks based on your teacher’s practicals. Each one links to the lesson it supports.", body, style)


def quizzes(nav):
    intro = '<p>Quick quizzes to check your knowledge. Answers are marked instantly when you press Check, and each question links to the lesson that teaches it and to the tutor.</p>\n<p class="small">Original practice questions for this course. Answers save in this browser only.</p>'
    return engine_page(nav, "Unit 8 Quizzes", "6. Quizzes", intro, "quiz-data.js", (U19 / "quizzes.html").read_text())


def exam(nav):
    intro = '<p>Exam-style scenarios written for this course. Practice 1 has short and medium questions; Practice 2 has the long, level-marked questions that carry the most marks. Read the command-word guide at the top of each practice.</p>\n<p class="small">Stuck? Every question links to its lesson and to the AI tutor, which gives hints rather than the answer. These are not official past papers: ask your teacher for sample assessment materials.</p>'
    return engine_page(nav, "Unit 8 Exam practice", "5. Exam practice", intro, "exam-data.js", (U19 / "quizzes.html").read_text())


SOW = [
 ("11", "Confidential information; why keep it confidential; impact", "S1", "–", "1"),
 ("12–13", "Technical threats: malware, botnets, DoS, hacking, social engineering, network attacks", "T1–T4", "1, 2", "2"),
 ("14", "Technical vulnerabilities", "V1", "–", "3"),
 ("15", "Human threats", "V2", "–", "3"),
 ("16–17", "Physical vulnerabilities; impact of threats", "V3", "8", "3"),
 ("18–19", "Threat mitigation techniques", "M1–M4", "3, 4, 6", "4"),
 ("20–21", "Internet security: firewalls, segregation, monitoring", "M5", "7", "4"),
 ("22–23", "CIA triad", "C1", "9", "5"),
 ("24–26", "IAAA model", "C2", "5", "5"),
 ("27–29", "Revision and exam", "all", "–", "Exam practice 1, 2"),
]


def teachers(nav, deck_name, deck_size, n_slides):
    rows = "".join(f"<tr><td>{w}</td><td>{t}</td><td>{l}</td><td>{p}</td><td>{q}</td></tr>" for w, t, l, p, q in SOW)
    body = f"""<section class="card"><h2>Teacher PowerPoint</h2>
<p>A {n_slides}-slide delivery deck with full speaker notes. Each lesson slide follows the department routine (starter, aim, teach, practical, task, check, flipped homework) with questioning, stretch and support ideas, and the matching workbook section, practical and quiz.</p>
<div class="tools"><a class="primary" href="teacher/{deck_name}" download style="display:inline-block;padding:10px 16px;border-radius:8px;background:var(--accent);color:#fff;text-decoration:none">Download the teacher deck (.pptx, {deck_size})</a></div>
<p class="small">Contents: unit overview · assessment · the course site · using the AI tutor · delivery plan · 15 lesson slides across 8.1–8.4 · practicals and ethics · exam technique. Diagrams are the same originals used on the Learn page.</p></section>

<section class="card"><h2>How the course maps to the scheme of work</h2>
<div class="tablewrap"><table><thead><tr><th>Week (2025–26 plan)</th><th>Topic</th><th>Learn lesson</th><th>Practical</th><th>Quiz</th></tr></thead><tbody>
{rows}
</tbody></table></div>
<p class="small">Your PowerPoints, the 8.1 eLearning module, the perimeter security worksheet and solution, the Diffie-Hellman spreadsheet, Nmap and Linux practicals, student presentations (John the Ripper) and the Cisco Cybersecurity Essentials files stay on Teams. Cisco activity files and Pearson worksheets are not published on this public site.</p></section>

<section class="card"><h2>Assessment</h2>
<ul class="list">
<li>Content area 8 is part of the T Level core and is assessed in the <strong>written core examination</strong> (Paper 2 in the 2025–26 plan). Questions range from short recall to extended, level-marked responses on a scenario.</li>
<li>The <strong>Course guide</strong> gives a red/amber/green checklist of every specification point (8.1.1–8.4.2), saved on the student’s device.</li>
<li><strong>Exam practice</strong> uses original scenarios with level descriptors and self-marking checklists. Pair it with official sample assessment materials for timed mocks.</li>
</ul></section>

<section class="card"><h2>Ethics and safety</h2>
<ul class="list"><li>Every page with scanning or attack content carries a legal and ethical warning. Nmap, password cracking and penetration testing are taught for defence and only on the isolated lab network.</li>
<li>Consider a signed acceptable-use agreement for the lab before the Nmap and Kali practicals.</li></ul></section>

<section class="card"><h2>AI study tutor</h2>
<ul class="list">
<li><strong>Workbook tutor</strong> (page 3): explains, diagnoses, hints and sets new practice questions for each of the 15 lessons. It will not simply give the answer to the lesson’s own activity, and it is told not to give step-by-step instructions for attacking real systems.</li>
<li>Because this unit is exam-assessed, there is no assignment coach.</li>
<li><strong>Privacy:</strong> no student accounts, no names collected, and no conversation stored on the server.</li>
</ul>
<div class="note"><strong>Status:</strong> the AI service needs the college Azure subscription to be active. When it is re-enabled, the Unit 8 tutor is deployed and switched on by the course administrator.</div></section>

<section class="card"><h2>Maintaining the course</h2>
<p class="small">All Unit 8 pages are generated from <code>tools/unit8/</code> (<code>python3 tools/build_unit8.py</code>). Quiz and exam questions are in <code>docs/unit8/quiz-data.js</code> and <code>docs/unit8/exam-data.js</code>. The teacher deck is generated by <code>tools/unit8/teacher_deck.js</code>.</p></section>"""
    return page(nav, "Unit 8 for teachers", "For teachers", "Everything you need to deliver content area 8 with this course: the teacher PowerPoint, how the pages map to the scheme of work, assessment, ethics and the AI tutor.", body)
