"""Static Unit 7 pages: start, practicals, exam practice, quizzes and teachers. Called by tools/build_unit7.py."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
U19 = ROOT / "docs" / "unit19"

HEAD = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><link rel="stylesheet" href="../unit19/u19.css">{style}</head><body>\n<div class="packnav">{nav}</div>\n'
FOOT = '<footer>Original course material written for the T Level in Digital Production, Design and Development, core content area 7: Digital environments. Not an awarding-organisation publication. Cisco Packet Tracer is available free through Cisco Networking Academy.</footer>\n</body></html>\n'


def page(nav, title, h1, lead, body, style=""):
    return HEAD.format(title=title, style=style, nav=nav) + f'<header class="hero"><h1>{h1}</h1><p>{lead}</p></header>\n<div class="wrap">\n{body}\n</div>\n' + FOOT


def start(nav, n_lessons, n_videos):
    body = f"""<div class="cards">
<a href="guide.html"><h2>1. Course guide</h2><p>How the exam works, the command words, and a checklist of every specification point to rate red, amber or green.</p></a>
<a href="learning.html"><h2>2. Learn</h2><p>{n_lessons} short lessons with diagrams, key terms, exam tips and check-yourself questions.</p></a>
<a href="index.html"><h2>3. Workbook + tutor</h2><p>A practice activity for every lesson, saved on your device, with the AI study tutor to help when you are stuck.</p></a>
<a href="practicals.html"><h2>4. Practicals</h2><p>Hands-on tasks: the motherboard, command-line network tools, Packet Tracer, a virtual machine and a backup plan.</p></a>
<a href="exam.html"><h2>5. Exam practice</h2><p>Exam-style scenarios with short and extended answers, command-word guidance and level marking.</p></a>
<a href="quizzes.html"><h2>6. Quizzes</h2><p>Five instant-marked quizzes: numbers, hardware, software, networks, and virtual, cloud and resilient environments.</p></a>
<a href="videos.html"><h2>7. Videos</h2><p>{n_videos} short videos, from binary and CPUs to how a hacker attacks a smart thermostat.</p></a>
</div>
<div class="card"><h2>How to use this course</h2>
<ol class="steps">
<li>Open the <strong>Course guide</strong> and rate each specification point red, amber or green. Come back and update it as you go.</li>
<li>For each topic: read the <strong>lesson</strong>, watch its <strong>video</strong>, then complete the <strong>workbook</strong> activity.</li>
<li>Do the <strong>practicals</strong> in class when your teacher sets them.</li>
<li>Check yourself with the <strong>quizzes</strong>, then build exam technique with <strong>Exam practice</strong>.</li>
</ol>
<div class="note"><strong>This content area is assessed by a written exam.</strong> There is no coursework to hand in, so use the AI tutor as much as you like: ask it to explain, quiz you, or check your practice answers. Do not type your name or personal details into the tutor.</div>
<p class="small">Work saves in this browser only. Use the download buttons to keep a backup before changing computers.</p></div>
<p class="small" style="text-align:center">Also on this site: <a href="../start.html">Unit 2: Fundamentals of Computer Systems</a> · <a href="../unit19/start.html">Unit 19: Computer Networking</a> · <a href="../unit8/start.html">Unit 8: Security</a> · <a href="../unit12/start.html">Unit 12: Software Development</a></p>"""
    return page(nav, "Unit 7 Digital environments", "Unit 7: Digital environments", "Hardware, software, networks, virtual and cloud environments, and how organisations stay resilient. For T Level Digital students. No account needed.", body)


LABS = [
 ("lab1", "PC disassemble and reassemble", "In class · 60 min", "H2", [
   "Wear an anti-static wrist strap clipped to the case, and work on an anti-static mat with the PC unplugged.",
   "Photograph the inside before you remove anything, so you can put it back.",
   "Remove and name in order: side panel, RAM, GPU/expansion cards, drives and cables, CPU cooler (your teacher will say whether to remove the CPU).",
   "Reassemble in reverse order. Check every power and data cable is seated.",
   "Power on and check the PC reaches the BIOS/UEFI screen."],
  "Your teacher checks the PC boots.", "Photos of each stage, labelled with the component names."),
 ("lab2", "Motherboard ID and connectors", "45 min", "H2", [
   "On the Motherboard ID task sheet, label the CPU socket, RAM slots, PCIe slots, M.2 slot, chipset, SATA ports, 24-pin and 4/8-pin power connectors, CMOS battery and rear I/O panel.",
   "On the Connectors task, match each connector to its name and use: SATA data, SATA power, Molex, 24-pin ATX, 4/8-pin CPU, 6/8-pin PCIe, USB, HDMI, DisplayPort, RJ45.",
   "Find a real motherboard’s specification online. Record its socket, chipset, RAM type and maximum RAM, number of M.2 slots and USB ports.",
   "Explain which components you would upgrade first for a video editor, and why."],
  None, "Completed task sheets and your written upgrade explanation."),
 ("lab3", "Hardware spider diagram", "Homework", "H2", [
   "Create a spider diagram with the motherboard in the centre.",
   "Add branches for input devices, output devices, processors (cores, clock speed, cache, mobile processors), main memory (RAM, ROM), secondary storage (magnetic, solid state, optical), GPUs, network interfaces (PCI, USB) and cooling (air, liquid).",
   "On each branch write one feature and one use.",
   "Use the Learn page lesson on hardware devices to check your facts."],
  None, "Your diagram (paper photo or digital)."),
 ("lab4", "Number systems practice", "30 min", "NS", [
   "Convert five 8-bit binary numbers to denary and five denary numbers to binary.",
   "Convert three binary numbers to hexadecimal and back.",
   "Add pairs of 8-bit binary numbers. Circle any overflow.",
   "Work out how many GiB are in a 1 TB drive and explain the difference."],
  "Check your answers with Quiz 1.", "Your working, shown step by step."),
 ("lab5", "Command-line network tools", "50 min", "N7", [
   "Open Command Prompt on a Windows PC.",
   "Type <code>ipconfig</code>. Record your IPv4 address, subnet mask and default gateway.",
   "Type <code>ipconfig /all</code>. Record your MAC (physical) address, whether DHCP is enabled, the DHCP server and the DNS servers.",
   "Type <code>ping 127.0.0.1</code> (tests your own network software), then ping your default gateway, then <code>ping google.com</code>. What does each success or failure tell you?",
   "Type <code>arp -a</code>. Explain what the list of IP-to-MAC addresses shows.",
   "Type <code>netstat -an</code>. Find a connection in the ESTABLISHED state and one LISTENING port.",
   "Type <code>tracert google.com</code>. Count the hops and find where the delay increases."],
  "You can explain what each command showed and when a technician would use it.", "Screenshots of each command with one line explaining the result. Only run these on the network you have permission to use."),
 ("lab6", "Build and test a LAN in Packet Tracer", "40 min", "N4", [
   "Add a 2960 switch and four PCs. Connect each PC to the switch with copper straight-through cables.",
   "Give the PCs addresses 192.168.1.10 to .13 with mask 255.255.255.0.",
   "Ping between PCs. Then switch to Simulation mode and watch an ICMP packet travel.",
   "Click the switch and open its MAC address table (<code>show mac address-table</code> in the CLI). Explain how the switch learned the addresses."],
  "Every ping succeeds.", "Screenshots of the topology, a ping and the MAC table."),
 ("lab7", "A home network to the internet via cable and DSL", "60 min", "N4", [
   "Build a home network: PCs, a switch or home router, a cable modem and a DSL modem.",
   "Add a Cloud-PT and a server on the far side of the cloud. Give the server and PCs the IP addresses your teacher provides.",
   "Identify the type of media used for each link (copper, coaxial, phone line).",
   "In the cloud, route the modem connection to the Ethernet interface that leads to the server.",
   "Ping the server. Then change from DSL to cable (and back) and test again."],
  "The PC can ping the server over both DSL and cable.", "Screenshots and a short note on the media used."),
 ("lab8", "Routing between networks", "45 min", "N7", [
   "Open the router practical file your teacher provides (two or three routers with a LAN each).",
   "Configure the router interfaces with the IP addresses given.",
   "Enable RIP on each router: <code>router rip</code>, <code>version 2</code>, then <code>network</code> for each connected network.",
   "Use <code>show ip route</code> and find routes learned by RIP (marked R).",
   "Ping from a PC in one LAN to a PC in another. Disconnect a link and see whether traffic finds another path."],
  "PCs in different networks can ping each other.", "Screenshots of the routing table and pings."),
 ("lab9", "Create a virtual machine", "60 min", "V1", [
   "Install a type 2 hypervisor such as VirtualBox (or use the one on college PCs).",
   "Create a VM: give it 2 GB RAM, 2 CPU cores and a 20 GB virtual disk. Install a free Linux distribution from an ISO file.",
   "Take a snapshot. Make a change (install a program or delete a file), then restore the snapshot.",
   "Look at the host’s Task Manager while the VM runs. What happens to CPU and memory use?",
   "Write which key features of virtual environments you saw (isolation, emulation, managed execution, portability)."],
  "The VM boots and the snapshot restores.", "Screenshots and your list of features seen."),
 ("lab10", "Cloud responsibilities and APIs", "40 min", "C1", [
   "Sort cards (or a table) of: user accounts, data, application software, runtime, system software, virtualisation, hardware into client or provider for IaaS, PaaS and SaaS.",
   "Find one real example of each model and write who manages what.",
   "Extension: follow your teacher’s Postman demo to send a GET request to a public API and read the JSON response. Explain how cloud services talk to each other using APIs."],
  "Your sort matches the specification.", "Your completed table."),
 ("lab11", "Plan resilience for a small business", "45 min", "R1", [
   "Choose a business: a dental practice, an online shop or a school.",
   "List its critical systems and what would happen if each failed for a day.",
   "Plan backups: what, how often, onsite, offsite and cloud copies, and who tests recovery.",
   "Choose redundancy, patching, hardening and a hot, warm or cold site. Justify each choice against cost.",
   "Write one standard operating procedure, e.g. what staff do in a ransomware attack."],
  None, "Your one-page resilience plan: good revision for extended exam questions."),
 ("lab12", "Cisco Introduction to IoT (optional badge)", "Self-paced", "H1", [
   "Enrol in the free Cisco Networking Academy course on the Internet of Things (your teacher will share the class link).",
   "Complete the modules and the final quiz to earn a digital badge.",
   "Write three examples of embedded or IoT systems and one security risk for each."],
  None, "Your badge and notes."),
]


def practicals(nav):
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t, *_ in LABS)
    secs = []
    for i, t, time, lesson, steps, check, evidence in LABS:
        n = LABS.index(next(l for l in LABS if l[0] == i)) + 1
        s = f'<section class="card lab" id="{i}"><h2>Practical {n}: {t}</h2><div class="meta"><span>{time}</span><span><a href="learning.html#{lesson}">Lesson {lesson}</a></span></div>\n<ol class="steps">' + "".join(f"<li>{x}</li>" for x in steps) + "</ol>"
        if check:
            s += f'<div class="check"><strong>Check it works:</strong> {check}</div>'
        s += f'<div class="evidence"><strong>Keep:</strong> {evidence}</div></section>'
        secs.append(s)
    style = """<style>.lab h2{margin-top:0}.meta{display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 12px}.meta span{font-size:.8rem;background:#eaf2f9;border-radius:999px;padding:2px 10px}
.evidence{background:#eaf6f3;border-radius:10px;padding:10px 16px;margin:12px 0}.check{background:#eef6ff;border-radius:10px;padding:10px 16px;margin:12px 0}
#toc{columns:2;column-gap:30px}#toc li{break-inside:avoid;margin:.3em 0}@media(max-width:640px){#toc{columns:1}}</style>"""
    body = f"""<div class="card"><h2>Before you start</h2>
<ul class="list"><li>Practicals help you <em>understand</em>; the exam asks you to explain what you have seen. After each one, write two sentences on what it taught you.</li>
<li>Install <strong>Cisco Packet Tracer</strong> (free) by enrolling in <em>Getting Started with Cisco Packet Tracer</em> at <a href="https://www.netacad.com" rel="noopener" target="_blank">netacad.com</a>.</li>
<li>Follow the lab safety rules: anti-static precautions, no food or drink, and unplug before opening a PC.</li>
<li>Only run network commands or scans on the network you have been given permission to use.</li></ul>
<ol id="toc">{toc}</ol></div>
{"".join(secs)}"""
    return page(nav, "Unit 7 Practicals", "4. Practicals", "Hands-on tasks based on your teacher’s practicals. Each one links to the lesson it supports.", body, style)


def engine_page(nav, title, h1, intro, data_js, u19_quiz_html):
    """Reuse the Unit 19 quiz page's styles with our nav, text and data file."""
    src = u19_quiz_html
    style = src[src.index("<style>"):src.index("</style>") + 8]
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>{style}</head><body>
{nav}
<h1>{h1}</h1>
<div class="panel">
{intro}
<div class="tools"><button id="download" type="button">Download my answers</button><button id="restore" type="button">Continue from a backup</button><button id="clear" type="button">Clear this device</button><button id="print" type="button">Print</button><input id="backup" type="file" accept="application/json,.json" hidden></div>
<p id="status" role="status"></p>
</div>
<div id="tabs" role="group" aria-label="Choose a test"></div>
<main id="test"></main>
<script src="{data_js}"></script><script src="../revision.js"></script>
</body></html>
"""


def quizzes(nav):
    intro = '<p>Quick quizzes to check your knowledge. Answers are marked instantly when you press Check, and each question links to the lesson that teaches it and to the tutor.</p>\n<p class="small">Original practice questions for this course. Answers save in this browser only.</p>'
    return engine_page(nav, "Unit 7 Quizzes", "6. Quizzes", intro, "quiz-data.js", (U19 / "quizzes.html").read_text())


def exam(nav):
    intro = '<p>Exam-style scenarios written for this course. Practice 1 has short and medium questions; Practice 2 has the long, level-marked questions that carry the most marks. Read the command-word guide at the top of each practice.</p>\n<p class="small">Stuck? Every question links to its lesson and to the AI tutor, which will give hints rather than the answer. These are not official past papers: ask your teacher for sample assessment materials.</p>'
    return engine_page(nav, "Unit 7 Exam practice", "5. Exam practice", intro, "exam-data.js", (U19 / "quizzes.html").read_text())


SOW = [
 ("2", "Introduction; number systems", "NS", "4", "1"),
 ("3", "Physical computer systems; PC disassemble and reassemble", "H1", "1", "2"),
 ("4", "IoT (Cisco Academy)", "H1", "12", "2"),
 ("5–7", "Hardware devices; Raspberry Pi practical", "H2", "2, 3", "2"),
 ("8", "Operating systems", "SW1", "–", "3"),
 ("9", "Utilities", "SW2", "–", "3"),
 ("10", "Code development tools; application software", "SW3, SW4", "–", "3"),
 ("11–12", "Why network; network types; connectivity methods", "N1, N2", "5", "4"),
 ("13–16", "Practicals; topologies and network models", "N3", "6, 7", "4"),
 ("17–20", "Network components; internet connection and backbone", "N4", "6, 7", "4"),
 ("20–21", "OSI and TCP/IP models; data packets", "N5, N6", "–", "4"),
 ("22–24", "Protocols (incl. routing and application); bandwidth and latency", "N7, N8", "5, 8", "4"),
 ("25–27", "Virtual environments", "V1", "9", "5"),
 ("28–29", "Cloud types, benefits and delivery models", "C1", "10", "5"),
 ("30–31", "Resilient environments", "R1", "11", "5"),
 ("32–33", "Revision", "all", "–", "Exam practice 1, 2"),
]


def teachers(nav, deck_name, deck_size, n_slides):
    rows = "".join(f"<tr><td>{w}</td><td>{t}</td><td>{l}</td><td>{p}</td><td>{q}</td></tr>" for w, t, l, p, q in SOW)
    body = f"""<section class="card"><h2>Teacher PowerPoint</h2>
<p>A {n_slides}-slide delivery deck with full speaker notes. Each lesson slide follows the department routine (starter, aim, teach, practical, task, check, flipped homework) with questioning, stretch and support ideas, and the matching workbook section, practical and quiz.</p>
<div class="tools"><a class="primary" href="teacher/{deck_name}" download style="display:inline-block;padding:10px 16px;border-radius:8px;background:var(--accent);color:#fff;text-decoration:none">Download the teacher deck (.pptx, {deck_size})</a></div>
<p class="small">Contents: unit overview · how it is assessed · the course site · using the AI tutor · delivery plan · 18 lesson slides across 7.1–7.6 · practicals · exam technique and revision. Diagrams are the same originals used on the Learn page.</p></section>

<section class="card"><h2>How the course maps to the scheme of work</h2>
<div class="tablewrap"><table><thead><tr><th>Weeks (2025–26 SOW)</th><th>Topic</th><th>Learn lesson</th><th>Practical</th><th>Quiz</th></tr></thead><tbody>
{rows}
</tbody></table></div>
<p class="small">Your existing starters (Millionaire, Hollywood Squares, catchphrase), PowerPoints, Microsoft Forms checks, Packet Tracer files and the Cisco NetAcad IoT course stay on Teams. Copyrighted videos are embedded from their creators’ YouTube channels, not re-hosted.</p></section>

<section class="card"><h2>Assessment</h2>
<ul class="list">
<li>Content area 7 is part of the T Level core and is assessed in the <strong>written core examination</strong>, alongside other core content areas. Questions range from short recall to extended, level-marked responses on a scenario.</li>
<li>The <strong>Course guide</strong> gives students a red/amber/green checklist of every specification point (7.1.1–7.6.2), saved on their device. Ask them to screenshot it before one-to-ones.</li>
<li><strong>Exam practice</strong> uses original scenarios with level descriptors and self-marking checklists. Pair it with the awarding organisation’s sample assessment materials and past papers for timed mocks.</li>
</ul></section>

<section class="card"><h2>AI study tutor</h2>
<ul class="list">
<li><strong>Workbook tutor</strong> (page 3): explains, diagnoses, hints and sets new practice questions for each of the 18 lessons. It will not simply give the answer to the lesson’s own activity.</li>
<li>Because this unit is exam-assessed, there is no assignment coach; students are encouraged to use the tutor for revision and to check their understanding.</li>
<li><strong>Tamper-resistant:</strong> the page sends only a lesson ID; the lesson notes and rules are held on the server.</li>
<li><strong>Privacy:</strong> no student accounts, no names collected, and no conversation stored on the server.</li>
<li><strong>Cost control:</strong> the tutor runs on the college’s Azure AI service behind a gateway with shared rate limits and a daily quota. If the service is off, every page still works and the tutor shows an “offline” message.</li>
</ul>
<div class="note"><strong>Status:</strong> the AI service needs the college Azure subscription to be active. When it is re-enabled, the Unit 7 tutor is deployed and switched on by the course administrator.</div></section>

<section class="card"><h2>Maintaining the course</h2>
<p class="small">All Unit 7 pages are generated from <code>tools/unit7/</code> in the course repository (<code>python3 tools/build_unit7.py</code>). Quiz and exam questions are in <code>docs/unit7/quiz-data.js</code> and <code>docs/unit7/exam-data.js</code>. The teacher deck is generated by <code>tools/unit7/teacher_deck.js</code>.</p></section>"""
    return page(nav, "Unit 7 for teachers", "For teachers", "Everything you need to deliver content area 7 with this course: the teacher PowerPoint, how the pages map to the scheme of work, assessment, and the AI tutor.", body)
