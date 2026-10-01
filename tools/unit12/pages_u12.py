"""Static Unit 12 pages: start, practicals, quizzes, teachers and the assignment builder. Called by tools/build_unit12.py."""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "unit7"))
from pages_u7 import HEAD, engine_page  # noqa: E402

U19 = ROOT / "docs" / "unit19"
FOOT = '<footer>Original course material written for the Pearson BTEC Level 1/Level 2 First in Information and Creative Technology, Unit 12: Software Development. Not a Pearson publication. Visual Studio Community is free from Microsoft.</footer>\n</body></html>\n'
OTHER = '<p class="small" style="text-align:center">Also on this site: <a href="../start.html">Unit 2</a> · <a href="../unit19/start.html">Unit 19: Computer Networking</a> · <a href="../unit7/start.html">Unit 7: Digital environments</a> · <a href="../unit8/start.html">Unit 8: Security</a></p>'


def page(nav, title, h1, lead, body, style=""):
    return HEAD.format(title=title, style=style, nav=nav) + f'<header class="hero"><h1>{h1}</h1><p>{lead}</p></header>\n<div class="wrap">\n{body}\n</div>\n' + FOOT


def start(nav, n_lessons, n_videos):
    body = f"""<div class="cards">
<a href="brief.html"><h2>1. Assignment guide</h2><p>Your three assignments in plain English, what each grade means, and a checklist for every criterion.</p></a>
<a href="learning.html"><h2>2. Learn</h2><p>{n_lessons} short lessons with diagrams, flowcharts and Visual Basic examples you can try.</p></a>
<a href="index.html"><h2>3. Workbook + tutor</h2><p>A practice activity for every lesson, saved on your device, with the AI study tutor to help.</p></a>
<a href="practicals.html"><h2>4. Practicals</h2><p>Step-by-step programming labs: forms, calculators, selection, loops, arrays, strings, files and debugging.</p></a>
<a href="assignment.html"><h2>5. Assignment builder</h2><p>Plan each task, use the design, test-plan and review tables, and get feedback from the AI assignment coach.</p></a>
<a href="quizzes.html"><h2>6. Quizzes</h2><p>Instant-marked checks on software, design, code, testing and reviewing.</p></a>
<a href="videos.html"><h2>7. Videos</h2><p>{n_videos} short videos explaining each programming idea.</p></a>
</div>
<div class="card"><h2>How to use this course</h2>
<ol class="steps">
<li>Read the <strong>Assignment guide</strong> first so you know where you are heading.</li>
<li>For each topic: read the <strong>lesson</strong>, try the code in Visual Studio, then complete the <strong>workbook</strong> activity.</li>
<li>Do the <strong>practicals</strong>: they build the skills you need for your own program.</li>
<li>When your teacher issues an assignment, use the <strong>Assignment builder</strong> to plan, keep your evidence organised and get feedback on your drafts.</li>
</ol>
<div class="warnbox"><strong>Your assignments must be your own work.</strong> The AI tutor and coach explain, question and give feedback; they will not write your code, designs or reviews. Everything you ask the coach is recorded in your AI-use log, which you hand in. Do not type your name or personal details into the tutor.</div>
<p class="small">Work saves in this browser only. Use the download buttons to keep a backup before changing computers.</p></div>
{OTHER}"""
    return page(nav, "Unit 12 Software Development", "Unit 12: Software Development", "Learn how programs work, then design, build, test and review your own program in Visual Basic. No account needed.", body)


LABS = [
 ("lab1", "Your first Windows Forms program", "45 min", "C1", [
   "Install or open Visual Studio Community. Create a new project: <em>Windows Forms App (.NET Framework)</em>, language <em>Visual Basic</em>, name <code>HelloApp</code>.",
   "From the Toolbox add a TextBox (<code>txtName</code>), a Button (<code>btnHello</code>, Text “Say hello”) and a Label (<code>lblMessage</code>).",
   "Double-click the button and type: <code>lblMessage.Text = \"Hello, \" &amp; txtName.Text</code>",
   "Press F5 to run. Type a name and click the button.",
   "Change at least three properties (form BackColor, label Font and ForeColor, button Text) and run again."],
  "The label greets the name you type.", "A screenshot of your form running, and of the Properties you changed."),
 ("lab2", "Two-number calculator", "60 min", "C2", [
   "Make a form with two text boxes, four buttons (+, −, ×, ÷) and a result label.",
   "Declare variables with suitable data types and write code for each button.",
   "Move the calculation into a function so each button calls it.",
   "Add an extra button that shows the remainder using <code>Mod</code>.",
   "What happens if you divide by zero, or type a letter? Note it down: you will fix it in Practical 8."],
  "All four operations give correct answers.", "Annotated code (comments on every part) and screenshots."),
 ("lab3", "Temperature converter (from design to code)", "45 min", "B4", [
   "Write pseudocode for a program that reads °C, converts it to °F with F = C × 9 / 5 + 32, and displays the result.",
   "Draw the flowchart and dry-run it with a trace table for 0, 37 and 100.",
   "Build it in Visual Basic, using a constant where sensible.",
   "Compare your program with your design. Did you need to change anything?"],
  "0 → 32, 37 → 98.6, 100 → 212.", "Pseudocode, flowchart, trace table and the program."),
 ("lab4", "Selection: login and grade calculator", "60 min", "C3", [
   "Make a login form: a password box (set <code>PasswordChar</code> to *) and a button. Show “Access granted” or “Access denied”.",
   "Make a grade calculator for a mark out of 100 using If … ElseIf … Else.",
   "Make a Select Case program that turns a day number 1–7 into the day name, with Case Else for anything else.",
   "Write a test table for the grade calculator with normal, boundary and erroneous data."],
  "Every boundary mark gives the correct grade.", "Code and your test table."),
 ("lab5", "Loops: tables, totals and guessing game", "60 min", "C4", [
   "Use a For loop to show any times table (chosen by the user) in a ListBox.",
   "Show the running total of 1 to N in a multiline text box.",
   "Build a guessing game: the computer picks a number 1–50 (<code>Dim r As New Random : secret = r.Next(1, 51)</code>); use a loop to give “higher/lower” hints until the user guesses it, then show the number of guesses.",
   "Explain which loop you used for each part and why."],
  "The game always ends when the right number is guessed.", "Code and screenshots."),
 ("lab6", "Arrays and strings: team list", "60 min", "C6", [
   "Use <code>InputBox</code> in a loop to store six player names in an array, then display them in a ListBox.",
   "Add a Search button that finds a name and shows its position, or “not found”.",
   "Show each player’s initials in capitals using <code>Substring</code> and <code>ToUpper</code>.",
   "Sort the names alphabetically with <code>Array.Sort</code> and show them again."],
  "Searching for a name that is not in the list shows “not found”.", "Code and screenshots."),
 ("lab7", "File handling: save and load a list", "60 min", "C7", [
   "Add a Save button to Practical 6 that writes every name to <code>team.txt</code> (one per line) using <code>StreamWriter</code>.",
   "Add a Load button that reads the file back into the ListBox using <code>StreamReader</code>.",
   "Close the program, open it again and load the names. They should still be there.",
   "Make it robust: if the file does not exist, show a friendly message instead of crashing."],
  "Names survive closing and reopening the program.", "Code, the text file contents and screenshots."),
 ("lab8", "Make it robust: validation and error handling", "45 min", "C7", [
   "Go back to your calculator (Practical 2).",
   "Add a presence check and a type check (<code>Integer.TryParse</code> or <code>Decimal.TryParse</code>) to every input.",
   "Stop division by zero with a helpful message.",
   "Wrap risky code in <code>Try … Catch</code> and show a friendly error.",
   "Re-run your tests from Practical 2. What changed?"],
  "No input you can type will crash the program.", "Before-and-after test results."),
 ("lab9", "Debugging challenge", "45 min", "C8", [
   "Your teacher gives you a program with three faults (one syntax, one runtime, one logic).",
   "Use the Error List to find the syntax error.",
   "Use test data to make the runtime error happen, then fix it with validation.",
   "Set a breakpoint (F9), step through (F10) and watch the variables to find the logic error.",
   "Record each fault in a table: type, symptom, cause, fix, re-test result."],
  "All three faults are fixed and re-tested.", "Your fault table."),
 ("lab10", "Mini project: quiz program", "Two lessons", "B3", [
   "Design a quiz program: a question, four answers labelled A–D, a Submit button, a Quit button and an area that shows whether the answer was right (as in your scheme of work).",
   "Produce two alternative screen layouts and a navigation diagram, and choose one with a reason.",
   "Store at least five questions in arrays (or an array of records), with the correct answers.",
   "Develop it with selection, a loop or counter for the score, and comments throughout.",
   "Test it, get feedback from two classmates, improve it, and write a short review. This is practice for your assignments; do not reuse it as assignment evidence."],
  "The final score is correct for any set of answers.", "Design, code, tests, feedback and review: your practice portfolio."),
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
<ul class="list"><li>Use <strong>Visual Studio Community</strong> (free) with a <em>Windows Forms App (.NET Framework) – Visual Basic</em> project. Your college computers may have Visual Basic 2010 Express, which works the same way.</li>
<li>No Visual Studio at home? Console versions of most practicals run in a browser at <a href="https://dotnetfiddle.net" rel="noopener" target="_blank">dotnetfiddle.net</a> (choose the VB.NET language).</li>
<li>Name controls with prefixes (<code>txt</code>, <code>btn</code>, <code>lbl</code>), comment your code, and save each practical in its own project.</li>
<li>Practicals are for learning. Your assignment program must be your own new work for the brief.</li></ul>
<ol id="toc">{toc}</ol></div>
{"".join(secs)}"""
    return page(nav, "Unit 12 Practicals", "4. Practicals", "Programming labs in Visual Basic. Each builds a skill you need for Assignment 2.", body, style)


def quizzes(nav):
    intro = '<p>Quick quizzes to check your understanding. Answers are marked instantly when you press Check, and each question links to the lesson that teaches it and to the tutor.</p>\n<p class="small">Original practice questions for this course. Answers save in this browser only.</p>'
    return engine_page(nav, "Unit 12 Quizzes", "6. Quizzes", intro, "quiz-data.js", (U19 / "quizzes.html").read_text())


def assignment(nav):
    src = (U19 / "assignment.html").read_text()
    src = re.sub(r'<div class="packnav">.*?</div>', f'<div class="packnav">{nav}</div>', src, count=1, flags=re.S)
    src = src.replace('<title>Unit 19 Assignment builder</title>', '<title>Unit 12 Assignment builder</title>').replace('href="u19.css"', 'href="../unit19/u19.css"')
    src = src.replace("it will not write your assignment.", "it will not write your code, designs or reviews.")
    src = src.replace("check technical details against your lessons.", "check technical details against your lessons and test your own code.")
    assert "Unit 19" not in src
    return src


SCHEMAS = r"""const SCHEMAS = {
 programs: {title: 'Program analysis (1A.1 / 2A.P1)', cols: ['Feature', 'Program 1', 'Program 2'], prefill: ['Purpose', 'Inputs', 'Processing', 'Outputs', 'Type of language (and why)', 'Variables and data types', 'Selection and loops', 'Subroutines', 'String / file handling', 'Data structures', 'Event handling', 'Tools used (IDE, compiler, debugger)']},
 quality: {title: 'Quality review', cols: ['Quality measure', 'Evidence from the code', 'Improvement'], prefill: ['Efficiency / performance', 'Maintainability', 'Portability', 'Reliability', 'Robustness', 'Usability']},
 requirements: {title: 'Purpose and user requirements', cols: ['User requirement (in my words)', 'Why the user needs it', 'How I will know it is met']},
 ipo: {title: 'Main program tasks', cols: ['Task', 'Inputs', 'Processing', 'Outputs']},
 alternatives: {title: 'Alternative solutions', cols: ['Design area', 'Alternative 1', 'Alternative 2', 'Chosen, and why (requirements / constraints)'], prefill: ['Screen layout', 'Navigation', 'Algorithm', 'Data structures / storage']},
 datadesign: {title: 'Data, validation and error handling', cols: ['Data item', 'Data type / structure', 'Validation check', 'Error message to the user']},
 predefined: {title: 'Predefined code and sources', cols: ['Predefined function / code', 'What it does in my program', 'Source (and permission)']},
 testplan: {title: 'Test plan and results', cols: ['No.', 'What is tested', 'Test data', 'Type', 'Expected result', 'Actual result', 'Pass / fail', 'Action taken'], select: {3: ['', 'Normal', 'Boundary', 'Erroneous'], 6: ['', 'Pass', 'Fail', 'Pass after fix']}},
 changes: {title: 'Development and changes log', cols: ['Date', 'What I built or changed', 'Why (design / test / feedback)', 'Re-tested?'], select: {3: ['', 'Yes', 'Not yet']}},
 feedback: {title: 'Feedback log', cols: ['Date', 'Who gave feedback', 'Their feedback (usability / quality)', 'What I changed as a result']},
 evaluation: {title: 'Review grid', cols: ['Requirement / design element', 'Met?', 'Evidence (test, feedback, screenshot)', 'Strengths', 'Limitations / constraints', 'Recommendation'], select: {1: ['', 'Fully', 'Partly', 'Not met']}}
};
const TOOLS = {analysis: ['programs'], quality: ['quality'], requirements: ['requirements'], design: ['ipo', 'alternatives', 'datadesign', 'predefined', 'testplan'], develop: ['changes'], testplan: ['testplan'], feedback: ['feedback', 'changes'], evaluation: ['evaluation', 'quality'], notes: []};"""


def assignment_js():
    js = (U19 / "assignment.js").read_text()
    s, e = js.index("const SCHEMAS = {"), js.index("function tableRows(")
    js = js[:s] + SCHEMAS + "\n\n" + js[e:]
    for a, b in [("'unit19-assignment-v1'", "'unit12-assignment-v1'"), ("course: 'u19'", "course: 'u12'"), ("'UNIT 19 AI-USE LOG'", "'UNIT 12 AI-USE LOG'"),
                 ("'unit19-ai-use-log.txt'", "'unit12-ai-use-log.txt'"), ("'my-unit19-assignment-work.json'", "'my-unit12-assignment-work.json'"), ("Unit 19 Assignment builder", "Unit 12 Assignment builder")]:
        assert a in js, a
        js = js.replace(a, b)
    assert "19" not in re.sub(r"\d{3,}", "", js.replace("2019", "")), [l for l in js.splitlines() if "19" in l]
    return js


SOW = [
 ("1", "Why is software used? Inputs, processes, outputs", "A1", "1", "1"),
 ("2–3", "Characteristics, languages, constructs, compiling, design methods, flowcharts", "A2, A3, B4", "3", "1"),
 ("4", "Quality of software programs", "A4", "–", "1"),
 ("5", "Assignment 1 (2A.P1, 2A.M1, 2A.D1)", "A1–A4", "–", "–"),
 ("6–7", "SDLC; assessing requirements; design specifications; quiz screen design", "B1, B2, B3", "10", "2"),
 ("8–10", "Pseudocode; testing and maintaining; designing software", "B4, B5", "3", "2"),
 ("11", "Introduction to Visual Basic and the development environment", "C1", "1, 2", "3"),
 ("12–13", "Data types, variables, constants, operators, procedures and functions", "C2, C5", "2", "3"),
 ("14", "Sequence, selection and iteration", "C3, C4", "4, 5", "3"),
 ("15", "Event handling: forms, properties, actions", "C1", "1, 10", "3"),
 ("16", "Data structures; testing and refining", "C6, C7, C8", "6–9", "4"),
 ("17–18", "Assignment 2 (2B.P2 – 2C.D3)", "B1–C8", "–", "–"),
 ("19", "Reviewing software", "D1", "10", "5"),
 ("20", "Assignment 3 (2D.P6, 2D.M5, 2D.D4)", "D1", "–", "–"),
]


def teachers(nav, deck_name, deck_size, n_slides):
    rows = "".join(f"<tr><td>{w}</td><td>{t}</td><td>{l}</td><td>{p}</td><td>{q}</td></tr>" for w, t, l, p, q in SOW)
    body = f"""<section class="card"><h2>Teacher PowerPoint</h2>
<p>A {n_slides}-slide delivery deck with full speaker notes. Each lesson slide follows the department routine (starter, aim, teach, practical, task, check, flipped homework) with questioning, stretch and support ideas, and the matching workbook section, practical and quiz.</p>
<div class="tools"><a class="primary" href="teacher/{deck_name}" download style="display:inline-block;padding:10px 16px;border-radius:8px;background:var(--accent);color:#fff;text-decoration:none">Download the teacher deck (.pptx, {deck_size})</a></div>
<p class="small">Contents: unit overview · assessment map · the course site · AI rules · delivery plan · 18 lesson slides across learning aims A–D · three assignment launch slides · practicals. Diagrams are the same originals used on the Learn page.</p></section>

<section class="card"><h2>How the course maps to the scheme of work (20 × 3-hour lessons)</h2>
<div class="tablewrap"><table><thead><tr><th>Lesson</th><th>Topic</th><th>Learn lesson</th><th>Practical</th><th>Quiz</th></tr></thead><tbody>
{rows}
</tbody></table></div>
<p class="small">The scheme of work uses Visual Basic 2010; every example on this site also works in current Visual Studio Community (Windows Forms App (.NET Framework), Visual Basic). The textbook chapters (Pearson BTEC First ICT student book) and specification stay on Teams and are not reproduced here.</p></section>

<section class="card"><h2>Assignments</h2>
<ul class="list">
<li>The Assignment guide covers all criteria (1A.1–2D.D4) across the three assignments in the scheme of work. It uses a generic scenario so it works with your centre-devised briefs or Pearson’s authorised assignment briefs.</li>
<li>The lessons use a leisure-centre booking program as the running example. If your Assignment 2 brief is similar, choose a different client so the lesson examples cannot be reused as assignment work.</li>
<li>Practical 10 (quiz program) is a full practice project: design, develop, test, feedback and review, before the real assignment.</li>
</ul></section>

<section class="card"><h2>AI study tutor and assignment coach</h2>
<ul class="list">
<li><strong>Workbook tutor</strong> (page 3): explains, diagnoses, hints and sets new practice questions for each lesson.</li>
<li><strong>Assignment coach</strong> (page 5): explains the task, helps plan, reviews the student’s own draft against the checklist, and checks technical accuracy. It is instructed never to write code, pseudocode, flowcharts, screen designs, test plans, justifications or reviews for the student’s brief, and never to paste back corrected code: it points to the line and asks a question instead.</li>
<li><strong>AI-use log:</strong> every coach question is saved on the student’s device. Collect it with each assignment and sample it during internal verification.</li>
<li><strong>Tamper-resistant and private:</strong> the page sends only a task ID; briefs, checklists and rules are held on the server. No accounts, no names, nothing stored on the server.</li>
</ul>
<div class="note"><strong>Status:</strong> the AI service needs the college Azure subscription to be active. When it is re-enabled, the Unit 12 tutor and coach are deployed and switched on by the course administrator.</div></section>

<section class="card"><h2>Maintaining the course</h2>
<p class="small">All Unit 12 pages are generated from <code>tools/unit12/</code> (<code>python3 tools/build_unit12.py</code>). Assignment tasks and checklists live in <code>api/assignments-u12.json</code>, shared by the guide, the builder and the coach. Quizzes are in <code>docs/unit12/quiz-data.js</code>. The teacher deck is generated by <code>tools/unit12/teacher_deck.js</code>.</p></section>"""
    return page(nav, "Unit 12 for teachers", "For teachers", "Everything you need to deliver Unit 12 with this course: the teacher PowerPoint, how the pages map to the scheme of work, the assignments and the AI tutor and coach.", body)
