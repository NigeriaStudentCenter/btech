"""Unit 12 Software Development (BTEC First ICT): lessons for learning aims A and B (original content)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "unit19"))
sys.path.insert(0, str(HERE.parent / "deeper"))
from u19 import *  # noqa  lesson, device, cli, SVG, p, h3, table, terms, think, worked, real_world, ul
from u19 import SVG, device, esc, INK, LINE, ARROW, ACCENT, WARN, cli, assignment_link

RED, REDBG, AMBERBG, BLUEBG, GREENBG, GREEN, PURPLEBG = "#b03a2e", "#fbe3d4", "#fbf0dd", "#dcebf6", "#e8f1e4", "#2f7d4f", "#f3e8f9"


def code(lines, caption=None):
    return cli(lines, caption)


def tryit(title, steps, note=None):
    li = "".join(f"<li>{s}</li>" for s in steps)
    n = f'<p class="small">{note}</p>' if note else ""
    return f'<div class="tryit"><h4>Try it: {esc(title)}</h4><ol>{li}</ol>{n}</div>'


def spec(code_):
    return f"Unit 12 · {code_}"


# ---------- flowchart drawing helpers ----------
def fc_term(s, x, y, w, t):
    s.add(f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="17" fill="{GREENBG}" stroke="{GREEN}" stroke-width="2"/>')
    s.text(x + w / 2, y + 22, t, size=13)


def fc_io(s, x, y, w, t):
    s.poly([(x + 14, y), (x + w, y), (x + w - 14, y + 36), (x, y + 36)], fill=AMBERBG, stroke="#b58a3a")
    s.text(x + w / 2, y + 23, t, size=13)


def fc_proc(s, x, y, w, t):
    s.box(x, y, w, 36, t, size=13, fill=BLUEBG, rx=3)


def fc_dec(s, cx, cy, w, h, t):
    s.poly([(cx, cy - h / 2), (cx + w / 2, cy), (cx, cy + h / 2), (cx - w / 2, cy)], fill=PURPLEBG, stroke="#7b5aa6")
    s.text(cx, cy + 5, t, size=13)


# ---------- A1 why software is used ----------
def ipo_fig():
    s = SVG(760, 170, "Input, process, output")
    for i, (a, b, f) in enumerate([("INPUT", "data goes in\ne.g. two numbers typed", AMBERBG), ("PROCESS", "the program’s instructions\ne.g. add them together", BLUEBG), ("OUTPUT", "results come out\ne.g. show the total", GREENBG)]):
        x = 20 + i * 250
        s.box(x, 30, 220, 100, a, b, size=16, fill=f, bold=True)
        if i:
            s.arrow(x - 28, 80, x - 2, 80, width=2.2)
    s.text(380, 160, "Most programs also STORE data, e.g. saving a booking to a file.", size=12, color=ARROW)
    return s.render("Every program takes inputs, processes them and produces outputs.")


A1 = lesson("A1", "Learning aim A", "Why is software used?",
    "explain what software is, the main categories of software, and why organisations and people develop programs.", spec("A · Why is software used?"),
    p("A <strong>software program</strong> is a set of instructions that tells a computer’s processor (CPU) what to do, step by step. Hardware cannot do anything useful without software. Programs turn inputs into useful outputs, quickly, accurately and without getting tired."),
    ipo_fig(),
    table(["Category", "What it does", "Examples"], [
        ["Application software", "lets users do tasks", "word processor, spreadsheet, web browser, game"],
        ["System software", "runs the computer itself", "operating system, device drivers, utilities"],
        ["Programming software", "used to create other programs", "IDEs such as Visual Studio, compilers, debuggers"],
    ], caption="Three categories of software"),
    table(["Why we develop programs", "Real examples"], [
        ["Gaming and entertainment", "computer games, CGI special effects in films, virtual worlds, social media apps"],
        ["Increasing productivity", "automating factory processes, stock control that reorders goods automatically"],
        ["Information storage and management", "booking systems, customer databases, school registers"],
        ["Repetitive or dangerous tasks", "robot arms on a car production line, robots that defuse bombs or work inside nuclear plants"],
        ["Solving complex problems", "weather forecasting, route planning, medical scans"],
    ], caption="Uses of software programs"),
    real_world("a cinema booking app", "Inputs: the film, time and number of seats chosen. Processing: check which seats are free, calculate the price and discounts. Outputs: the ticket and a confirmation email. Storage: the booking is saved so nobody else can buy the same seat."),
    terms([("Software program", "a set of instructions a computer follows."), ("Input", "data that goes into a program."), ("Process", "what the program does with the data."), ("Output", "the result the program produces.")]),
    think([("Give one reason a factory uses software to control robots.", "Robots can repeat the same task accurately for hours, and can do dangerous jobs, which increases productivity and safety."),
           ("Name the inputs and outputs of a supermarket self-checkout.", "Inputs: barcodes scanned, items weighed, payment card. Outputs: prices on screen, total, receipt, payment request.")]),
)


# ---------- A2 programming languages and compiling ----------
def compile_fig():
    s = SVG(760, 210, "From source code to a program that runs")
    st = [("Source code", "written by the\nprogrammer", AMBERBG), ("1 Check", "syntax errors found\nand reported", PURPLEBG), ("2 Optimise", "tidy the code so it\nruns efficiently", BLUEBG), ("3 Translate", "into machine code\n(binary)", REDBG), ("Executable", ".exe file the user\ncan run", GREENBG)]
    for i, (a, b, f) in enumerate(st):
        x = 12 + i * 150
        s.box(x, 40, 136, 90, a, b, size=13, fill=f, bold=True)
        if i:
            s.arrow(x - 13, 85, x - 1, 85, width=1.8)
    s.text(380, 170, "If the compiler finds an error, it stops and tells you the line, so you fix it and compile again.", size=12, color=ARROW)
    return s.render("A compiler checks, optimises and translates the whole program into machine code before it runs.")


A2 = lesson("A2", "Learning aim A", "Programming languages and compiling",
    "describe high-level and low-level languages, procedural and event-driven languages, and why programs are compiled.", spec("A · Programming languages"),
    p("The only language a CPU understands is <strong>machine code</strong>: binary 1s and 0s. Every other language has to be translated first."),
    table(["", "Low-level languages", "High-level languages"], [
        ["Looks like", "machine code or short codes (assembly)", "English words and maths, e.g. <code>If score &gt; 50 Then</code>"],
        ["Advantages", "very fast; direct control of hardware", "easy to read, write and fix; works on different computers"],
        ["Disadvantages", "hard to write and debug; tied to one type of CPU", "must be translated; usually a little slower"],
    ], caption="Low-level and high-level languages"),
    table(["Type", "How the program runs", "Languages"], [
        ["Procedural", "instructions run in order from start to end, using procedures and functions", "C, Pascal, COBOL, Python"],
        ["Event-driven", "the program waits for events (a click, a key press, a timer) and runs the code for that event", "Visual Basic, VB.NET, VBA, Visual C++"],
    ], caption="Procedural and event-driven languages"),
    compile_fig(),
    table(["Translator", "How it works"], [
        ["Compiler", "translates the whole program into machine code before it runs; creates an executable; runs fast; reports all errors after compiling"],
        ["Interpreter", "translates and runs one line at a time; good for testing; stops at the first error; the interpreter is needed every time"],
    ], caption="Compilers and interpreters"),
    p("<strong>Program design methods</strong> include top-down design (break the problem into smaller parts), flowcharts, pseudocode and screen designs. You will use all of these in learning aim B."),
    terms([("Machine code", "binary instructions the CPU can run directly."), ("Source code", "the program written by the programmer in a high-level language."), ("Compiler", "translates all the source code into machine code before it runs."), ("Event-driven", "a program that responds to user actions such as clicks.")]),
    think([("Why do programmers usually write in high-level languages?", "They are easier to read, write and debug, so programs are built faster and with fewer mistakes, and they can run on different computers."),
           ("Why is Visual Basic called an event-driven language?", "Its code runs in response to events, such as the user clicking a button or changing a drop-down list.")]),
)


# ---------- A3 constructs and techniques ----------
A3 = lesson("A3", "Learning aim A", "Constructs and techniques: the building blocks of programs",
    "identify command words, subroutines, string handling, file handling, data structures and event handling in a program.", spec("A · Characteristics of software programs"),
    p("All programming languages are built from the same kinds of building blocks. When you look at someone else’s program (as in Assignment 1), find these and say what each one does."),
    table(["Construct / technique", "What it is", "Visual Basic example"], [
        ["Command words", "reserved words that tell the computer what to do", "<code>Dim</code>, <code>If … Then</code>, <code>For … Next</code>, <code>MsgBox</code>"],
        ["Subroutines (procedures and functions)", "a named block of code that does one job and can be reused", "<code>Private Sub CalculateTotal()</code>"],
        ["Basic string handling", "working with text: join, cut, search, change case, length", "<code>name.ToUpper()</code>, <code>name.Length</code>"],
        ["Basic file handling", "open, read, write and close files so data is kept after the program ends", "<code>IO.File.AppendAllText(\"bookings.txt\", line)</code>"],
        ["Data structures", "ways to organise lots of data, e.g. arrays and records", "<code>Dim scores(9) As Integer</code>"],
        ["Event handling", "code that runs when something happens, e.g. a button click", "<code>Private Sub btnSave_Click(…) Handles btnSave.Click</code>"],
    ], caption="Constructs and techniques"),
    h3("Reading a program: an annotated example"),
    code(["' Program: cinema ticket price (event-driven)",
          "Private Sub btnPrice_Click(sender As Object, e As EventArgs) Handles btnPrice.Click   ' event handling",
          "    Const ADULT_PRICE As Decimal = 9.5D                ' a constant",
          "    Dim age As Integer = CInt(txtAge.Text)              ' input + data type",
          "    Dim price As Decimal",
          "    If age < 16 Then                                    ' selection",
          "        price = ADULT_PRICE / 2",
          "    Else",
          "        price = ADULT_PRICE",
          "    End If",
          "    lblPrice.Text = \"Price: \" & price.ToString(\"C\")   ' output + string handling",
          "End Sub"], "Comments (after the apostrophe) are ignored by the computer but explain the code to people."),
    terms([("Construct", "a building block of a language, e.g. a loop or IF."), ("Reserved word", "a word with a special meaning in the language that cannot be used as a variable name."), ("Subroutine", "a named section of code that performs one task."), ("Event", "something that happens, such as a click, that the program reacts to.")]),
    assignment_link("1A.1 / 2A.P1", "For each program your teacher gives you, explain its purpose and identify the constructs and techniques it uses, like the annotated example above."),
    think([("Find two constructs in the cinema example and say what each does.", "Selection (If … Else) chooses the child or adult price; a constant (ADULT_PRICE) stores a value that does not change; event handling runs the code when the button is clicked."),
           ("Why would a booking program need file handling?", "So bookings are saved permanently and can be loaded again after the program closes.")]),
)


# ---------- A4 quality ----------
def quality_fig():
    s = SVG(760, 230, "Six measures of software quality")
    q = [("Efficiency", "uses little CPU time,\nmemory and storage", BLUEBG), ("Maintainability", "easy to fix and change:\ncomments, clear names", AMBERBG), ("Portability", "runs on different\ndevices and systems", GREENBG),
         ("Reliability", "gives accurate,\ncorrect outputs", PURPLEBG), ("Robustness", "copes with bad or extreme\ninput without crashing", REDBG), ("Usability", "easy for the user to\nlearn and use", "#eef0f3")]
    for i, (a, b, f) in enumerate(q):
        x, y = 20 + (i % 3) * 245, 20 + (i // 3) * 105
        s.box(x, y, 230, 90, a, b, size=15, fill=f, bold=True)
    return s.render("Use these six measures whenever you comment on, test or review a program.")


A4 = lesson("A4", "Learning aim A", "The quality of software programs",
    "explain how design and coding techniques affect efficiency, maintainability, portability, reliability, robustness and usability.", spec("A · Quality of software programs"),
    quality_fig(),
    table(["Measure", "Good practice that improves it", "Sign of poor quality"], [
        ["Efficiency / performance", "loops instead of repeated code; no unnecessary calculations; load data once", "slow, freezes, uses lots of memory"],
        ["Maintainability", "comments, meaningful names (<code>totalCost</code> not <code>x</code>), indentation, subroutines, constants", "nobody can understand or change it safely"],
        ["Portability", "standard features; avoid code tied to one device", "only works on one computer or screen size"],
        ["Reliability", "test with normal data; check calculations", "wrong totals or results"],
        ["Robustness", "validate input; handle errors (<code>Try … Catch</code>, <code>Integer.TryParse</code>)", "crashes when a letter is typed into a number box"],
        ["Usability", "clear labels, instructions, sensible layout, helpful error messages", "users get confused or make mistakes"],
    ], caption="Measuring quality"),
    h3("Spot the quality problems"),
    code(["Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click",
          "    Dim a As Integer = TextBox1.Text",
          "    Dim b As Integer = TextBox2.Text",
          "    Label1.Text = a * 1.2 + b * 1.2",
          "End Sub"], "No comments, meaningless names, the 1.2 is repeated and unexplained, and typing a letter crashes it."),
    p("Improved: name the controls (<code>txtPrice</code>, <code>btnTotal</code>), use a constant <code>VAT_RATE</code>, add comments, and validate the inputs with <code>Integer.TryParse</code> so a wrong entry shows a friendly message instead of crashing."),
    terms([("Maintainability", "how easily code can be understood and changed later."), ("Robustness", "how well a program copes with unexpected or extreme input."), ("Portability", "how easily a program runs on different hardware or operating systems."), ("Usability", "how easy a program is for its users.")]),
    assignment_link("2A.M1 / 2A.D1", "Comment on the quality of one program using these six measures, suggest improvements and draw a flowchart of the improved processing. For Distinction, discuss strengths and weaknesses in a balanced way."),
    think([("Why do comments improve maintainability?", "They explain what the code does and why, so the original programmer or someone new can change it safely later."),
           ("A program crashes when a user types ‘ten’ instead of 10. Which quality measure is weak and how do you fix it?", "Robustness: validate the input (e.g. Integer.TryParse) and show a helpful message instead of crashing.")]),
)


# ---------- B1 SDLC ----------
def sdlc_fig():
    s = SVG(760, 300, "The software development life cycle")
    st = [("1 Assess requirements", "what does the client need?", 380, 40, AMBERBG), ("2 Design specification", "plan it: inputs, outputs, screens", 610, 130, BLUEBG), ("3 Develop code", "write the program", 520, 250, PURPLEBG), ("4 Test", "does it work and meet needs?", 240, 250, REDBG), ("5 Maintain", "fix, update and improve", 150, 130, GREENBG)]
    for a, b, cx, cy, f in st:
        s.box(cx - 105, cy - 30, 210, 60, a, b, size=13, fill=f, bold=True)
    for (x1, y1, x2, y2) in [(487, 55, 560, 98), (610, 162, 570, 218), (412, 252, 348, 252), (190, 220, 160, 162), (200, 98, 272, 55)]:
        s.arrow(x1, y1, x2, y2, width=2)
    s.text(380, 150, "a cycle:", size=13, color=ARROW)
    s.text(380, 168, "maintenance leads to", size=13, color=ARROW)
    s.text(380, 186, "new requirements", size=13, color=ARROW)
    return s.render("Each stage feeds the next. Real projects often loop back, e.g. a failed test sends you back to development.")


B1 = lesson("B1", "Learning aim B", "The software development life cycle",
    "describe the stages of the software development life cycle and why it is used.", spec("B · Software development life cycle"),
    sdlc_fig(),
    table(["Stage", "What happens", "What is produced"], [
        ["Assess requirements", "talk to the client and users; find out what the program must do", "requirements list, problem definition"],
        ["Design specification", "plan scope, inputs, outputs, processing, user interface and constraints", "design documents: screens, flowcharts, pseudocode, test plan"],
        ["Develop code", "write the program from the design", "working code with comments"],
        ["Test", "check it works, meets requirements and is good quality", "completed test plan, fixes, feedback"],
        ["Maintain", "fix bugs found later, update and add features", "new versions"],
    ], caption="Stages of the life cycle"),
    table(["Model", "How it works", "Good for"], [
        ["Waterfall", "each stage is finished before the next starts", "small, clear projects that will not change"],
        ["Iterative / agile", "build, test and get feedback in short cycles, improving each time", "projects where requirements change"],
        ["RAD (rapid application development)", "build prototypes quickly and refine them with the user", "programs with lots of user interface"],
    ], caption="Different life cycle models"),
    terms([("Life cycle", "the stages used to create and maintain software."), ("Requirements", "what the client needs the program to do."), ("Iteration", "repeating a process to improve it each time."), ("Prototype", "an early, simple version used to get feedback.")]),
    think([("Why is it risky to start coding before assessing requirements?", "You may build the wrong thing, wasting time and money, because you do not know what the client needs."),
           ("What is one problem with the waterfall model?", "You cannot easily go back: if the client changes their mind late, earlier stages must be redone.")]),
)


# ---------- B2 requirements and design specification ----------
B2 = lesson("B2", "Learning aim B", "Requirements, problem definition and design specification",
    "describe the purpose and user requirements from a brief, write a problem definition statement and outline a design specification.", spec("B · Designing software"),
    p("Your assignment brief describes a client and a problem. Before designing anything, show that you understand <strong>what</strong> the program is for and <strong>who</strong> will use it."),
    table(["Part", "Question it answers", "Example: a leisure centre class booking program"], [
        ["Intended purpose", "what is the program for?", "to let reception staff book members onto fitness classes and calculate the cost"],
        ["User requirements", "what must it do for the users?", "choose a class; enter member type; calculate price with discounts; save bookings; show today’s bookings"],
        ["Problem definition statement", "what is the problem now, and how will software help?", "bookings are written on paper, prices are worked out by hand and mistakes are common; a program will speed this up and reduce errors"],
    ], caption="Understanding the brief"),
    table(["Design specification", "Meaning", "Example"], [
        ["Scope", "what the program will and will not include", "bookings and prices; not online payment"],
        ["Inputs", "data entered by the user", "member name, member type, class, number of sessions"],
        ["Outputs", "results shown or printed", "price, confirmation message, list of bookings"],
        ["Processing", "the main tasks and calculations", "look up class price; apply member discount; add to list; save to file"],
        ["User interface", "how users interact", "one form with drop-down lists, text boxes and buttons"],
        ["Constraints", "limits on the project", "must be written in Visual Basic; four weeks to develop; runs on reception PCs; no internet connection"],
    ], caption="The design specification"),
    terms([("Brief", "the client’s description of the problem and what they want."), ("User requirement", "something the program must do for its users."), ("Problem definition statement", "a short description of the current problem and how software will solve it."), ("Constraint", "a limit, e.g. time, language, device or cost.")]),
    assignment_link("1B.2 / 2B.P2", "Describe the purpose and user requirements for the program in your brief. Use your own words, and do not copy the brief: show you understand it."),
    think([("What is the difference between the purpose and the user requirements?", "The purpose is the overall aim of the program; the user requirements are the specific things it must do for its users."),
           ("Give two constraints that could affect a student’s program.", "The programming language available (Visual Basic), the time before the deadline, the computers it must run on, or no access to a database.")]),
)


# ---------- B3 design tools: screens, navigation, alternatives ----------
def screen_fig():
    s = SVG(760, 300, "Annotated screen layout and navigation diagram")
    s.box(20, 20, 380, 260, fill="white", stroke="#245d83")
    s.add('<rect x="20" y="20" width="380" height="30" rx="8" fill="#245d83"/>')
    s.text(210, 40, "Class Booking", size=14, color="white", bold=True)
    rows = [("Member name", "text box"), ("Member type", "drop-down list"), ("Class", "drop-down list"), ("Sessions", "text box")]
    for i, (a, b) in enumerate(rows):
        y = 70 + i * 40
        s.text(40, y + 18, a, size=13, anchor="start")
        s.box(170, y, 150, 26, size=11, fill="#f6f9fc", rx=3)
        s.text(330, y + 18, b, size=10, anchor="start", color=ARROW)
    s.box(40, 235, 110, 32, "Calculate", size=13, fill="#dcebf6", rx=5)
    s.box(170, 235, 110, 32, "Save booking", size=13, fill="#dcebf6", rx=5)
    s.text(300, 255, "Price: £—", size=13, anchor="start", bold=True)
    s.text(580, 30, "Navigation", size=14, bold=True)
    s.box(500, 50, 160, 40, "Splash / login", size=12, fill=GREENBG)
    s.box(500, 130, 160, 40, "Booking form", size=12, fill=BLUEBG)
    s.box(430, 220, 140, 40, "Today’s bookings", size=12, fill=AMBERBG)
    s.box(590, 220, 140, 40, "Exit", size=12, fill=REDBG)
    s.arrow(580, 90, 580, 128, width=1.6)
    s.arrow(560, 170, 505, 218, width=1.6, both=True)
    s.arrow(600, 170, 655, 218, width=1.6)
    return s.render("Label every control and say what type it is. A navigation diagram shows how screens link together.")


B3 = lesson("B3", "Learning aim B", "Designing the solution: tasks, screens, navigation and alternatives",
    "describe the main program tasks, design screen layouts and navigation, and compare alternative solutions.", spec("B · Proposed solution"),
    p("Your proposed solution shows the client what the program will look like and how it will work, <em>before</em> any code is written."),
    table(["Main task", "Inputs", "Processing", "Outputs"], [
        ["Calculate a booking price", "member type, class, sessions", "look up price × sessions; apply discount", "price shown on the form"],
        ["Save a booking", "name, class, price", "add a line to the bookings file", "“Booking saved” message"],
        ["Show today’s bookings", "(none: button click)", "read the file; filter today’s date", "list of bookings"],
    ], caption="Describing the main program tasks (input–process–output)"),
    screen_fig(),
    h3("Alternative solutions"),
    p("Good designers consider more than one idea, then choose and <strong>justify</strong> the best. You can offer alternatives for the screen layout, navigation, algorithms, data structures or control structures."),
    table(["", "Alternative 1: one form", "Alternative 2: a form per task"], [
        ["Description", "all inputs and buttons on one screen", "separate screens for booking, list and settings, with a menu"],
        ["Strengths", "quick for busy staff; fewer clicks", "less cluttered; easier to add features later"],
        ["Weaknesses", "can look crowded as features grow", "more navigation; more code to write"],
        ["Fits the requirements?", "yes: reception needs speed", "partly: more than the client needs now"],
    ], caption="Comparing alternatives (and justifying the choice)"),
    terms([("Screen layout", "a labelled sketch of a form or screen."), ("Navigation diagram", "a diagram showing how screens link together."), ("Prototype", "an early version used to try out a design."), ("Alternative solution", "a different way to meet the same requirements.")]),
    assignment_link("2B.M2 / 2B.D2", "Merit needs alternative solutions and a detailed design using a range of tools. Distinction needs you to justify your decisions: how each one meets the purpose and user requirements, and how constraints affected it."),
    think([("Why should screen layouts be shown to the client before coding?", "The client can give feedback and spot problems early, when changes are quick and cheap."),
           ("Give one advantage of a drop-down list over a text box for ‘member type’.", "Users can only choose valid options, so typing mistakes are impossible (built-in validation) and it is quicker.")]),
)


# ---------- B4 algorithms: pseudocode, flowcharts, trace tables ----------
def symbols_fig():
    s = SVG(760, 130, "Flowchart symbols")
    fc_term(s, 20, 30, 130, "Start / End")
    fc_io(s, 175, 29, 150, "Input / Output")
    fc_proc(s, 350, 29, 140, "Process")
    fc_dec(s, 580, 47, 140, 70, "Decision?")
    s.arrow(670, 47, 740, 47, width=2)
    s.text(705, 70, "flow line", size=12)
    for x, t in [(85, "oval"), (250, "parallelogram"), (420, "rectangle"), (580, "diamond: Yes / No")]:
        s.text(x, 110, t, size=12, color=ARROW)
    return s.render("Five shapes are enough to draw almost any program.")


def ticket_fc():
    s = SVG(760, 470, "Flowchart: cinema ticket price")
    fc_term(s, 300, 10, 160, "Start")
    s.arrow(380, 44, 380, 60, width=1.8)
    fc_io(s, 290, 62, 180, "Input age")
    s.arrow(380, 98, 380, 118, width=1.8)
    fc_dec(s, 380, 160, 170, 80, "age < 16?")
    s.arrow(465, 160, 540, 160, width=1.8, label="Yes", ly=-8)
    fc_proc(s, 542, 142, 180, "price = 4.75")
    s.arrow(380, 200, 380, 230, width=1.8)
    s.text(392, 220, "No", size=12, anchor="start")
    fc_dec(s, 380, 272, 170, 80, "age >= 65?")
    s.arrow(465, 272, 540, 272, width=1.8, label="Yes", ly=-8)
    fc_proc(s, 542, 254, 180, "price = 6.00")
    s.arrow(380, 312, 380, 336, width=1.8)
    s.text(392, 328, "No", size=12, anchor="start")
    fc_proc(s, 290, 338, 180, "price = 9.50")
    s.add(f'<path d="M722 160 L742 160 L742 402" stroke="{ARROW}" stroke-width="1.8" fill="none"/>')
    s.add(f'<path d="M722 272 L742 272" stroke="{ARROW}" stroke-width="1.8" fill="none"/>')
    s.arrow(742, 402, 472, 402, width=1.8)
    s.arrow(380, 374, 380, 382, width=1.8)
    fc_io(s, 290, 384, 180, "Output price")
    s.arrow(380, 420, 380, 428, width=1.8)
    fc_term(s, 300, 430, 160, "End")
    return s.render("A decision has exactly two exits, Yes and No. Follow the arrows with test values to check the flowchart works.")


B4 = lesson("B4", "Learning aim B", "Algorithms: pseudocode, flowcharts and trace tables",
    "write algorithms as pseudocode and flowcharts, and check them with a trace table.", spec("B · Algorithms"),
    p("An <strong>algorithm</strong> is a set of step-by-step instructions to solve a problem. Designing the algorithm first means you solve the problem before worrying about the exact code."),
    symbols_fig(),
    ticket_fc(),
    h3("The same algorithm in pseudocode"),
    code(["INPUT age", "IF age < 16 THEN", "    price ← 4.75", "ELSE IF age >= 65 THEN", "    price ← 6.00", "ELSE", "    price ← 9.50", "END IF", "OUTPUT price"], "Pseudocode is structured English: no exact syntax, but clear enough to turn into code."),
    h3("Checking with a trace table"),
    code(["total ← 0", "FOR count ← 1 TO 4", "    total ← total + count", "NEXT count", "OUTPUT total"]),
    table(["count", "total", "output"], [["–", "0", ""], ["1", "1", ""], ["2", "3", ""], ["3", "6", ""], ["4", "10", ""], ["", "", "10"]], caption="A trace table records each variable as the algorithm runs (a ‘dry run’)"),
    terms([("Algorithm", "step-by-step instructions to solve a problem."), ("Pseudocode", "structured English used to plan code."), ("Flowchart", "a diagram of an algorithm using standard symbols."), ("Trace table", "a table used to follow the values of variables through an algorithm.")]),
    assignment_link("2A.M1 / 2B.P3", "Assignment 1 Merit asks for a flowchart of the improved program; your design needs algorithms as flowcharts and/or pseudocode."),
    think([("Using the flowchart, what price does a 70-year-old pay? A 16-year-old?", "70: age ≥ 65, so £6.00. 16: not under 16 and not 65 or over, so £9.50."),
           ("Why must a decision box have two exits?", "A decision is a Yes/No question, so the algorithm needs a path for each answer.")]),
)


# ---------- B5 data, validation, error handling, test plans, constraints ----------
B5 = lesson("B5", "Learning aim B", "Data, validation, error handling, predefined code and test plans",
    "plan data structures and storage, validation, error handling, predefined code and a test plan with test data.", spec("B · Proposed solution · test plan · constraints"),
    table(["Design area", "What to decide", "Example"], [
        ["Data structures", "variables, arrays or records to hold the data", "array of 6 class names; record for a booking (name, class, price)"],
        ["Data storage", "how data is kept after the program closes", "text file <code>bookings.txt</code>, one booking per line"],
        ["Control structures", "where you need selection and loops", "IF for discounts; FOR loop to show all bookings"],
        ["Data validation", "checks that input is sensible before using it", "sessions must be a whole number from 1 to 10"],
        ["Error handling and reporting", "what happens when something goes wrong", "file missing → friendly message, not a crash"],
    ], caption="Planning the data and checks"),
    table(["Validation check", "What it checks", "Example"], [
        ["Presence", "something has been entered", "member name is not blank"],
        ["Type", "the right kind of data", "sessions is a number"],
        ["Range", "within sensible limits", "sessions from 1 to 10"],
        ["Length", "the right number of characters", "membership number is 6 characters"],
        ["Lookup / list", "one of the allowed values", "member type is Adult, Junior or Senior (drop-down)"],
    ], caption="Common validation checks"),
    h3("Predefined code"),
    p("Reusing code (from the language’s libraries, your teacher, or the internet) saves time, but you must have permission and <strong>list the source</strong> in your design and in a comment in the code."),
    table(["Predefined function or snippet", "Purpose", "Source"], [["<code>Integer.TryParse</code>", "safely convert text to a whole number", "built into VB.NET (Microsoft documentation)"], ["<code>IO.File.AppendAllText</code>", "add a line to a text file", "built into VB.NET"]], caption="A predefined code table"),
    h3("Test plan with test data"),
    table(["No.", "Test", "Test data", "Type", "Expected result"], [
        ["1", "price for an adult, 2 sessions", "Adult, Yoga, 2", "normal", "£12.00"],
        ["2", "highest allowed sessions", "10", "boundary", "accepted"],
        ["3", "too many sessions", "11", "erroneous", "message: “Enter 1 to 10 sessions”"],
        ["4", "letters in sessions", "abc", "erroneous", "message, no crash"],
        ["5", "blank name", "(empty)", "erroneous", "message: “Enter the member’s name”"],
    ], caption="Plan the tests now; fill in actual results later"),
    terms([("Validation", "automatic checks that input is sensible."), ("Normal / boundary / erroneous data", "typical valid data / data at the edge of the allowed range / invalid data."), ("Predefined code", "code that already exists and can be reused with permission."), ("Test plan", "a list of tests with test data and expected results.")]),
    assignment_link("1B.3 / 2B.P3", "Your design must include a problem definition statement, a proposed solution, a list of any predefined functions/subroutines and a test plan."),
    think([("Why test with boundary data?", "Mistakes often happen at the edges, e.g. using < instead of <=, so testing exactly at the limit catches them."),
           ("Why should you list the source of predefined code?", "To show which parts are not your own work, give credit, and help anyone maintaining the program.")]),
)

LESSONS = [A1, A2, A3, A4, B1, B2, B3, B4, B5]
