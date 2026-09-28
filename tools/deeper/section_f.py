from helpers import *

GATE = 'fill="white" stroke="#245d83" stroke-width="2.2"'


def and_path(x, y):
    return f'<path d="M{x} {y} L{x + 30} {y} A20 20 0 0 1 {x + 30} {y + 40} L{x} {y + 40} Z" {GATE}/>'


def or_path(x, y):
    return f'<path d="M{x} {y} Q{x + 16} {y + 20} {x} {y + 40} Q{x + 38} {y + 40} {x + 58} {y + 20} Q{x + 38} {y} {x} {y} Z" {GATE}/>'


def gate(s, kind, x, y, inputs=2, out_len=24):
    """Draw a gate with its left edge at x, top at y (40 high). Returns the output point."""
    if kind in ("AND", "NAND"):
        s.add(and_path(x, y))
        end = x + 50
    elif kind in ("OR", "NOR", "XOR"):
        s.add(or_path(x, y))
        end = x + 58
        if kind == "XOR":
            s.add(f'<path d="M{x - 8} {y} Q{x + 8} {y + 20} {x - 8} {y + 40}" fill="none" stroke="#245d83" stroke-width="2.2"/>')
    else:  # NOT
        s.poly([(x, y), (x + 42, y + 20), (x, y + 40)], fill="white", stroke=ARROW, width=2.2)
        end = x + 42
    if kind in ("NAND", "NOR", "NOT"):
        s.add(f'<circle cx="{end + 5}" cy="{y + 20}" r="5" {GATE}/>')
        end += 10
    ins = [y + 20] if inputs == 1 or kind == "NOT" else [y + 11, y + 29]
    left = x - (12 if kind == "XOR" else 0)
    for iy in ins:
        s.line(left - 24, iy, left + (6 if kind in ("OR", "NOR", "XOR") else 0), iy, color=ARROW, width=2)
    s.line(end, y + 20, end + out_len, y + 20, color=ARROW, width=2)
    return end + out_len, y + 20, [(left - 24, iy) for iy in ins]


def gates_gallery():
    s = SVG(760, 380, "The six logic gates with their symbols, notation and truth tables")
    items = [("AND", "Q = A.B", "1 only if both are 1", [0, 0, 0, 1]), ("OR", "Q = A + B", "1 if either is 1", [0, 1, 1, 1]), ("NOT", "Q = Ā", "reverses the input", None),
             ("NAND", "Q = NOT(A.B)", "AND, then NOT", [1, 1, 1, 0]), ("NOR", "Q = NOT(A + B)", "OR, then NOT", [1, 0, 0, 0]), ("XOR", "Q = A ⊕ B", "1 if the inputs differ", [0, 1, 1, 0])]
    for i, (k, expr, desc, tt) in enumerate(items):
        col, row = i % 3, i // 3
        x0, y0 = 20 + col * 248, 20 + row * 180
        s.box(x0, y0, 236, 168, fill="white", stroke="#c9d7e3")
        s.text(x0 + 14, y0 + 24, k, size=15, anchor="start", bold=True)
        s.text(x0 + 222, y0 + 24, expr, size=13, anchor="end", mono=True)
        gate(s, k, x0 + 44, y0 + 44, inputs=1 if k == "NOT" else 2)
        s.text(x0 + 118, y0 + 108, desc, size=12)
        if tt:
            s.text(x0 + 118, y0 + 132, "A B → Q", size=12, mono=True)
            s.text(x0 + 118, y0 + 152, "  ".join(f"{a}{b}:{q}" for (a, b), q in zip([(0, 0), (0, 1), (1, 0), (1, 1)], tt)), size=12, mono=True)
        else:
            s.text(x0 + 118, y0 + 140, "A → Q:  0:1  1:0", size=12, mono=True)
    return s.render("The logic gates. A bubble on the output means NOT. NAND and NOR are ‘universal’: any circuit can be built from just one of them.")


def half_full_adder():
    s = SVG(760, 330, "A half adder circuit and a full adder built from two half adders")
    s.text(190, 26, "Half adder", size=15, bold=True)
    s.text(40, 90, "A", size=15, bold=True)
    s.text(40, 170, "B", size=15, bold=True)
    s.line(55, 85, 100, 85, width=2)
    s.line(55, 165, 100, 165, width=2)
    ox, oy, ins = gate(s, "XOR", 150, 60, out_len=60)
    s.text(ox + 30, oy + 5, "Sum", size=14, anchor="start", bold=True)
    ox2, oy2, ins2 = gate(s, "AND", 150, 140, out_len=68)
    s.text(ox2 + 30, oy2 + 5, "Carry", size=14, anchor="start", bold=True)
    s.line(100, 85, 100, 71, width=2)
    s.line(100, 71, 114, 71, width=2)
    s.line(100, 85, 100, 151, width=2)
    s.line(100, 151, 126, 151, width=2)
    s.line(88, 165, 88, 89, width=2)
    s.line(88, 89, 114, 89, width=2)
    s.line(88, 165, 88, 169, width=2)
    s.line(88, 169, 126, 169, width=2)
    s.circle(100, 85, 3.5, fill=ARROW, stroke=ARROW)
    s.circle(88, 165, 3.5, fill=ARROW, stroke=ARROW)
    s.text(190, 225, "1 + 1 = 10 in binary: Sum 0, Carry 1", size=12, color=ACCENT)
    s.text(575, 26, "Full adder", size=15, bold=True)
    s.box(470, 50, 90, 60, "Half\nadder 1", size=13, fill="#dcebf6")
    s.box(470, 150, 90, 60, "Half\nadder 2", size=13, fill="#dcebf6")
    s.text(430, 68, "A", size=13, bold=True)
    s.text(430, 98, "B", size=13, bold=True)
    s.arrow(440, 64, 468, 64, width=1.8)
    s.arrow(440, 94, 468, 94, width=1.8)
    s.text(415, 196, "Carry in", size=12, bold=True)
    s.arrow(440, 190, 468, 190, width=1.8)
    s.add(f'<path d="M560 70 L590 70 L590 130 L450 130 L450 166 L468 166" stroke="{ARROW}" stroke-width="1.8" fill="none"/>')
    s.text(620, 124, "sum 1", size=11, color=ARROW)
    s.arrow(560, 170, 720, 170, width=1.8)
    s.text(700, 160, "Sum", size=13, bold=True)
    s.box(620, 230, 50, 40, "OR", size=13)
    s.add(f'<path d="M560 95 L605 95 L605 240 L618 240" stroke="{ARROW}" stroke-width="1.8" fill="none"/>')
    s.add(f'<path d="M560 195 L595 195 L595 260 L618 260" stroke="{ARROW}" stroke-width="1.8" fill="none"/>')
    s.arrow(670, 250, 720, 250, width=1.8)
    s.text(705, 240, "Carry out", size=13, bold=True)
    s.text(575, 305, "Chain full adders together to add whole bytes", size=12, color=ACCENT)
    return s.render("Adders are how the ALU does arithmetic. A half adder adds two bits; a full adder also adds the carry from the column before.")


def kmap():
    s = SVG(760, 250, "A three-input Karnaugh map simplifying an expression")
    s.text(160, 28, "Q = A.B.C̄ + A.B.C + Ā.B.C", size=14, mono=True)
    cols = ["00", "01", "11", "10"]
    ones = {(1, 2), (1, 3), (0, 2)}
    x0, y0, cw, ch = 110, 80, 70, 50
    s.text(x0 + 2 * cw, y0 - 28, "B C", size=13, bold=True)
    for c, t in enumerate(cols):
        s.text(x0 + c * cw + cw / 2, y0 - 8, t, size=13, mono=True)
    s.text(x0 - 40, y0 + ch / 2 - 10, "A", size=13, bold=True)
    for r in range(2):
        s.text(x0 - 16, y0 + r * ch + ch / 2 + 5, str(r), size=13, mono=True)
        for c in range(4):
            s.box(x0 + c * cw, y0 + r * ch, cw, ch, "1" if (r, c) in ones else "0", size=16, fill="white", rx=0)
    s.add(f'<rect x="{x0 + 2 * cw + 5}" y="{y0 + ch + 5}" width="{2 * cw - 10}" height="{ch - 10}" rx="14" fill="none" stroke="{WARN}" stroke-width="3"/>')
    s.add(f'<rect x="{x0 + 2 * cw + 10}" y="{y0 + 8}" width="{cw - 20}" height="{2 * ch - 16}" rx="14" fill="none" stroke="{ACCENT}" stroke-width="3"/>')
    s.text(560, 90, "Orange group: A = 1 and B = 1,", size=13, color=WARN, anchor="start")
    s.text(560, 108, "C changes, so it drops out → A.B", size=13, color=WARN, anchor="start")
    s.text(560, 145, "Green group: B = 1 and C = 1,", size=13, color=ACCENT, anchor="start")
    s.text(560, 163, "A changes, so it drops out → B.C", size=13, color=ACCENT, anchor="start")
    s.text(380, 225, "Simplified:  Q = A.B + B.C   (fewer gates, same truth table)", size=15, bold=True)
    return s.render("A Karnaugh map puts neighbouring input patterns next to each other (00, 01, 11, 10), so groups of 1s show which inputs can be removed.")


F1 = deeper("F1",
    h3("Every gate at a glance"),
    gates_gallery(),
    p("Written Boolean expressions use a dot for AND (<code>A.B</code>), a plus for OR (<code>A + B</code>), a bar over a letter for NOT (<code>Ā</code>) and ⊕ for XOR. You may also see ∧ for AND, ∨ for OR and ¬ for NOT. Just like in maths, brackets are worked out first, then NOT, then AND, then OR."),
    h3("How a computer adds"),
    half_full_adder(),
    worked("From a problem to a circuit", [
        "An alarm (Q) should sound if the door is open (D) AND the system is armed (A), OR if the panic button (P) is pressed.",
        "Write the expression: <code>Q = D.A + P</code>.",
        "Circuit: D and A go into an AND gate; its output and P go into an OR gate; the OR output drives the alarm.",
        "Test some rows: D=1, A=0, P=0 gives 0 (door open, not armed: silent). D=1, A=1, P=0 gives 1. D=0, A=0, P=1 gives 1 (panic always works).",
    ], "Turn each ‘and’ and ‘or’ in the description into a gate, then check the rows of a truth table."),
    table(["Law", "AND form", "OR form"], [
        ["Identity", "A.1 = A", "A + 0 = A"],
        ["Null", "A.0 = 0", "A + 1 = 1"],
        ["Same input", "A.A = A", "A + A = A"],
        ["Inverse", "A.Ā = 0", "A + Ā = 1"],
        ["De Morgan", "NOT(A.B) = Ā + B̄", "NOT(A + B) = Ā.B̄"],
    ], caption="Boolean laws that simplify expressions"),
    h3("Simplifying with a Karnaugh map"),
    kmap(),
    terms([
        ("Truth table", "a table showing the output for every possible combination of inputs."),
        ("Universal gate", "NAND or NOR: either can be combined to make every other gate."),
        ("Half adder", "adds two bits: Sum = A XOR B, Carry = A AND B."),
        ("Full adder", "adds two bits plus a carry in; built from two half adders and an OR gate."),
        ("Karnaugh map", "a grid used to spot and remove unnecessary terms in a Boolean expression."),
    ]),
    think([
        ("How many rows does a truth table with 4 inputs have?", "2⁴ = 16 rows."),
        ("Show how a NAND gate can act as a NOT gate.", "Join both inputs together. If the input is 0, NAND(0, 0) = 1; if it is 1, NAND(1, 1) = 0, so the output is always the opposite of the input."),
        ("Simplify <code>A.B + A.B̄</code>.", "Factor out A: A.(B + B̄) = A.1 = A. Whatever B is, the output equals A."),
    ]),
)


def symbols():
    s = SVG(760, 200, "Standard flowchart symbols")
    s.add(f'<rect x="20" y="40" width="110" height="46" rx="23" fill="white" stroke="{LINE}" stroke-width="2"/>')
    s.text(75, 68, "Start / End", size=12)
    s.text(75, 120, "terminator", size=12, color=ARROW)
    s.box(150, 40, 110, 46, "Process", size=12)
    s.text(205, 120, "a calculation or action", size=11, color=ARROW)
    s.poly([(345, 34), (400, 63), (345, 92), (290, 63)], fill="white")
    s.text(345, 68, "Decision?", size=12)
    s.text(345, 120, "yes / no question", size=11, color=ARROW)
    s.poly([(440, 40), (550, 40), (530, 86), (420, 86)], fill="white")
    s.text(485, 68, "Input / Output", size=12)
    s.text(485, 120, "data in or out", size=11, color=ARROW)
    s.box(570, 40, 110, 46, "Subroutine", size=12)
    s.line(582, 40, 582, 86, color=LINE, width=2)
    s.line(668, 40, 668, 86, color=LINE, width=2)
    s.text(625, 120, "a named sub-process", size=11, color=ARROW)
    s.circle(715, 63, 18, fill="white", label="A", size=12)
    s.text(715, 120, "connector", size=11, color=ARROW)
    s.arrow(200, 160, 560, 160, label="flow lines show the order, and every one needs an arrowhead", ly=24, lsize=12)
    return s.render("Flowchart symbols. Using the standard shapes means anyone can read the chart.")


def flowchart():
    s = SVG(760, 480, "Flowchart for topping up a bus pass with validation")
    cx = 300

    def term(y, t):
        s.add(f'<rect x="{cx - 70}" y="{y}" width="140" height="40" rx="20" fill="white" stroke="{LINE}" stroke-width="2"/>')
        s.text(cx, y + 25, t, size=13)

    def io(y, t):
        s.poly([(cx - 90, y), (cx + 110, y), (cx + 90, y + 44), (cx - 110, y + 44)], fill="white")
        s.text(cx, y + 27, t, size=12)
    term(20, "Start")
    s.arrow(cx, 60, cx, 82)
    io(84, "Input amount (£)")
    s.arrow(cx, 128, cx, 152)
    s.poly([(cx, 154), (cx + 110, 204), (cx, 254), (cx - 110, 204)], fill="#fbf0dd", stroke="#b58a3a")
    s.text(cx, 200, "Is amount between", size=12)
    s.text(cx, 216, "5 and 50?", size=12)
    s.arrow(cx + 110, 204, 448, 204)
    s.text(430, 196, "No", size=13, color=ARROW)
    s.poly([(470, 180), (700, 180), (680, 228), (450, 228)], fill="white")
    s.text(575, 202, "Output “Enter £5 to £50”", size=12)
    s.add(f'<path d="M575 180 L575 106 L412 106" stroke="{ARROW}" stroke-width="2.5" fill="none"/>')
    s.poly([(402, 106), (414, 100), (414, 112)], fill=ARROW, stroke=ARROW, width=1)
    s.text(500, 98, "loop back", size=11, color=ARROW)
    s.arrow(cx, 254, cx, 282, label="Yes", lx=18, ly=0)
    s.box(cx - 110, 284, 220, 44, "balance = balance + amount", size=12)
    s.arrow(cx, 328, cx, 352)
    io(354, "Output new balance")
    s.arrow(cx, 398, cx, 422)
    term(424, "End")
    s.text(560, 330, "Test with:", size=13, anchor="start", bold=True)
    for i, t in enumerate(["20 (normal)", "5 and 50 (boundary)", "4 and 51 (just outside)", "“ten” (erroneous)"]):
        s.text(560, 354 + i * 20, "• " + t, size=12, anchor="start")
    return s.render("A complete flowchart: one start, one end, a labelled decision and a loop that repeats until the input is valid.")


def system_diagram():
    s = SVG(760, 290, "System diagram of a school canteen payment system")
    s.box(20, 40, 130, 50, "Student", "taps card", size=13, fill="#fbf0dd", stroke="#b58a3a")
    s.box(20, 200, 130, 50, "Parent", "uses app", size=13, fill="#fbf0dd", stroke="#b58a3a")
    s.box(290, 30, 170, 70, "1. Take payment", "till", size=13, fill="#dcebf6", rx=14)
    s.box(290, 190, 170, 70, "2. Top up account", "web service", size=13, fill="#dcebf6", rx=14)
    s.box(570, 20, 170, 50, "Kitchen manager", size=13, fill="#fbf0dd", stroke="#b58a3a")
    s.box(570, 125, 170, 60, fill="white")
    s.line(570, 125, 740, 125, color=LINE, width=2)
    s.text(655, 160, "D1 Accounts", size=14, bold=True)
    s.arrow(150, 65, 288, 65, label="card ID, items", ly=-8, lsize=12)
    s.arrow(150, 225, 288, 225, label="top-up amount", ly=-8, lsize=12)
    s.arrow(460, 45, 568, 45, label="daily sales report", ly=-8, lsize=12)
    s.arrow(460, 85, 600, 123, both=True)
    s.text(548, 92, "read / update", size=11, color=ARROW, anchor="start")
    s.text(548, 106, "balance", size=11, color=ARROW, anchor="start")
    s.arrow(460, 215, 600, 187, both=True)
    s.text(548, 222, "read / update", size=11, color=ARROW, anchor="start")
    s.text(548, 236, "balance", size=11, color=ARROW, anchor="start")
    s.text(20, 280, "Orange = people outside the system  ·  Blue = processes  ·  Open box = data store  ·  Arrows = labelled data flows", size=12, anchor="start")
    return s.render("A system (data flow) diagram shows who uses the system, what it does, where data is stored, and exactly which data moves where.")


F2 = deeper("F2",
    h3("The symbols"),
    symbols(),
    h3("A complete flowchart"),
    flowchart(),
    table(["Test type", "Example value", "Expected result"], [
        ["Normal", "20", "accepted; balance goes up by £20"],
        ["Boundary (on the limit)", "5 and 50", "accepted"],
        ["Boundary (just outside)", "4 and 51", "rejected with the message, then asked again"],
        ["Erroneous", "“ten” or blank", "rejected with the message, then asked again"],
    ], caption="Test plan for the top-up flowchart"),
    h3("Seeing the whole system"),
    system_diagram(),
    p("A flowchart shows the <em>steps</em> of one process in order. A system diagram shows the <em>big picture</em>: the people and other systems involved, the processes, the stored data and the data flowing between them. Label every arrow with the data it carries. If a process has data going in but nothing coming out, something is missing."),
    terms([
        ("Terminator", "the rounded symbol marking the start or end of a flowchart."),
        ("Decision", "a diamond with one question and labelled exits (usually Yes and No)."),
        ("Iteration", "a loop: steps that repeat until a condition is met."),
        ("Data store", "somewhere data is kept in a system, such as a file or database table."),
        ("Boundary data", "values at the edge of what is allowed, used to test the limits."),
    ]),
    think([
        ("What is wrong with a decision diamond that has three arrows coming out, none labelled?", "A decision should ask one yes/no question with exactly two exits, and each exit must be labelled so the reader knows which way to go."),
        ("In the top-up flowchart, why is 50.01 a useful test value?", "It is just above the upper limit, so it checks the program uses ‘50 or less’ correctly rather than accepting anything that starts with 50."),
        ("In the system diagram, what data flows would you add for a refund?", "A refund request from the student or parent into a process, the refunded amount updating D1 Accounts, and a confirmation back to the person."),
    ]),
)

SECTIONS = {"F1": F1, "F2": F2}
