from helpers import *


def stack_queue():
    s = SVG(760, 300, "A stack and a queue side by side")
    s.text(190, 28, "Stack (LIFO)", size=15, bold=True)
    for i, v in enumerate(["D", "C", "B", "A"]):
        s.box(130, 60 + i * 46, 120, 40, v, size=16, fill="#dcebf6" if i == 0 else "white")
    s.add(f'<path d="M122 55 L122 244 L258 244 L258 55" stroke="{INK}" stroke-width="2.5" fill="none"/>')
    s.text(300, 85, "← top", size=13, anchor="start", color=WARN)
    s.arrow(70, 40, 145, 56)
    s.text(55, 36, "push", size=13, color=ARROW)
    s.arrow(235, 56, 310, 40)
    s.text(330, 36, "pop", size=13, color=ARROW)
    s.text(190, 275, "Last in, first out: D comes off first", size=12, color=ACCENT)
    s.text(570, 28, "Queue (FIFO)", size=15, bold=True)
    for i, v in enumerate(["A", "B", "C", "D"]):
        s.box(440 + i * 66, 130, 60, 44, v, size=16, fill="#dcebf6" if i == 0 else "white")
    s.text(470, 200, "front", size=13, color=WARN)
    s.text(668, 200, "rear", size=13, color=WARN)
    s.arrow(438, 152, 395, 152)
    s.text(410, 120, "dequeue", size=13, color=ARROW)
    s.arrow(750, 152, 706, 152)
    s.text(725, 120, "enqueue", size=13, color=ARROW)
    s.text(570, 275, "First in, first out: A leaves first", size=12, color=ACCENT)
    return s.render("A stack adds and removes at the same end (the top). A queue adds at the rear and removes from the front.")


def linked_list():
    s = SVG(760, 240, "Inserting an item into a linked list by changing pointers")
    nodes = [("Ali", 40), ("Ben", 230), ("Dev", 420), ("Zoe", 610)]
    for name, x in nodes:
        s.box(x, 40, 70, 44, name, size=14, fill="white")
        s.box(x + 70, 40, 40, 44, "•" if name != "Zoe" else "null", size=13 if name == "Zoe" else 18, fill="#eaf2f9")
    s.arrow(110 + 20, 62, 228, 62)
    s.arrow(300 + 20, 62, 418, 62, color="#b9c7d5", dash=True)
    s.arrow(490 + 20, 62, 608, 62)
    s.box(325, 150, 70, 44, "Cal", size=14, fill="#fbf0dd")
    s.box(395, 150, 40, 44, "•", size=18, fill="#fbf0dd")
    s.arrow(320, 84, 355, 148, color=ACCENT, label="1. Ben now points to Cal", lx=-95, ly=8, lsize=12)
    s.arrow(435, 172, 455, 86, color=ACCENT, label="2. Cal points to Dev", lx=85, ly=10, lsize=12)
    s.text(380, 228, "No items move in memory: only two pointers change. An array would have to shift Dev and Zoe along.", size=12)
    return s.render("A linked list stores each item with a pointer to the next. Inserting ‘Cal’ in order only changes two pointers.")


def tree():
    s = SVG(760, 280, "A binary search tree of names")
    pos = {"Maya": (380, 40), "Dev": (200, 120), "Sam": (560, 120), "Ali": (110, 200), "Fin": (290, 200), "Ravi": (470, 200), "Zoe": (650, 200)}
    edges = [("Maya", "Dev"), ("Maya", "Sam"), ("Dev", "Ali"), ("Dev", "Fin"), ("Sam", "Ravi"), ("Sam", "Zoe")]
    for a, b in edges:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        s.line(x1, y1 + 18, x2, y2 - 18, color=LINE, width=2)
    for n, (x, y) in pos.items():
        s.box(x - 45, y - 18, 90, 36, n, size=14, fill="#dcebf6" if n == "Maya" else "white")
    s.text(160, 70, "earlier in the alphabet: go left", size=12, color=WARN)
    s.text(600, 70, "later in the alphabet: go right", size=12, color=WARN)
    s.text(380, 262, "To find ‘Ravi’: Maya → right to Sam → left to Ravi. 3 checks instead of up to 7.", size=12, color=ACCENT)
    return s.render("A binary tree is a list where each item has a left and a right pointer. Searching halves the remaining items at each step.")


D1 = deeper("D1",
    h3("Seeing the structures"),
    stack_queue(),
    p("Stacks and queues are defined by <em>where</em> items can be added and removed, not by how they are stored. Both can be built inside an array, using a variable (a <strong>pointer</strong>) to remember where the top, front or rear is. In a <strong>circular queue</strong> the rear wraps round to the start of the array when it reaches the end, so the free spaces at the front can be reused."),
    linked_list(),
    tree(),
    table(["Structure", "In software", "In hardware"], [
        ["Stack", "undo in an editor; the browser Back button; the call stack that remembers where each function should return", "the CPU’s stack pointer register; saving registers when an interrupt arrives"],
        ["Queue", "print jobs; messages waiting to be processed; players waiting to join a game", "the keyboard buffer; packets waiting in a router; tasks waiting for the CPU"],
        ["Array", "a list of scores; the pixels of an image; a game board", "memory itself is one huge array of numbered locations"],
        ["List", "a music playlist; a to-do list that changes often; a sorted list of names", "blocks of a file on a disc chained together"],
    ], caption="Where the data structures are used"),
    h3("Data types"),
    table(["Data type", "Holds", "Example", "Typical size"], [
        ["Integer", "whole numbers", "age = 15", "2–8 bytes"],
        ["Real / float", "numbers with a fractional part", "price = 4.99", "4 or 8 bytes"],
        ["Character", "one character", "grade = 'B'", "1–4 bytes"],
        ["String", "a sequence of characters", "name = 'Priya'", "1+ byte per character"],
        ["Boolean", "true or false", "paid = true", "1 bit (often stored in a byte)"],
        ["Date/time", "a moment in time", "2026-09-28 14:05", "usually 8 bytes"],
    ], caption="Common data types"),
    p("Choosing the right type matters: storing a phone number as an integer would lose the leading zero and allow nonsense such as adding two phone numbers together, so it should be a string. Storing money as a float can create rounding errors, so money is often held as a whole number of pence."),
    worked("Undo with a stack", [
        "A student types ‘cat’, then makes it bold, then changes the colour. Each action is pushed onto the undo stack: [type, bold, colour] with ‘colour’ on top.",
        "Pressing Undo pops ‘colour’ and reverses it. Pressing Undo again pops ‘bold’.",
        "The most recent action is always undone first, which is exactly the last-in, first-out behaviour of a stack.",
    ]),
    terms([
        ("Pointer", "a value that holds the position (address or index) of another item."),
        ("LIFO / FIFO", "last in, first out (stack) / first in, first out (queue)."),
        ("Linked list", "a list where each item stores a pointer to the next item."),
        ("Binary tree", "a structure where each item points to up to two others, left and right."),
        ("Index", "the position number of an item in an array, usually starting at 0."),
    ]),
    think([
        ("Why is a queue used for print jobs rather than a stack?", "It is fair: documents print in the order they were sent. With a stack, the newest job would print first and early jobs could wait forever."),
        ("Why is finding an item in a linked list slower than in an array?", "An array can jump straight to position n using the index. A linked list must follow the pointers one by one from the start."),
        ("What data type should a postcode be, and why?", "A string, because it mixes letters, digits and a space, and no calculations are done with it."),
    ]),
)


def dims():
    s = SVG(760, 230, "One, two and three dimensional arrays")
    s.text(120, 28, "1D: scores[4]", size=14, bold=True)
    s.grid(30, 60, 5, 1, 36, 36, [["12", "9", "15", "7", "11"]], size=13)
    for i in range(5):
        s.text(48 + i * 36, 115, str(i), size=11, color=WARN)
    s.text(120, 140, "one index", size=12)
    s.text(380, 28, "2D: seats[row][col]", size=14, bold=True)
    s.grid(300, 45, 5, 4, 32, 32, None, [["#dcebf6" if (r, c) == (2, 3) else "white" for c in range(5)] for r in range(4)])
    s.text(380, 200, "two indexes: seats[2][3]", size=12)
    s.text(630, 28, "3D: pixels[layer][row][col]", size=14, bold=True)
    for k in range(3):
        s.grid(560 + k * 18, 45 + k * 18, 4, 4, 26, 26, None, [["#fbf0dd" if k == 2 else "white"] * 4 for _ in range(4)])
    s.text(640, 200, "three indexes, e.g. R, G and B layers", size=12)
    return s.render("An array can have any number of dimensions. A matrix is a 2D array of numbers you can calculate with.")


def row_col_major():
    s = SVG(760, 250, "Row-major and column-major order in memory")
    vals = [["a", "b", "c"], ["d", "e", "f"]]
    s.text(120, 28, "The grid (2 rows × 3 columns)", size=13, bold=True)
    s.grid(60, 45, 3, 2, 44, 40, vals, None, size=16)
    s.text(460, 40, "Row-major: rows one after another", size=13, anchor="start", bold=True)
    s.grid(460, 50, 6, 1, 44, 36, [list("abcdef")], [["#dcebf6"] * 3 + ["#e8f1e4"] * 3], size=15)
    for i in range(6):
        s.text(482 + i * 44, 102, str(i), size=11, color=WARN)
    s.text(460, 150, "Column-major: columns one after another", size=13, anchor="start", bold=True)
    s.grid(460, 160, 6, 1, 44, 36, [list("adbecf")], [["#dcebf6", "#e8f1e4"] * 3], size=15)
    for i in range(6):
        s.text(482 + i * 44, 212, str(i), size=11, color=WARN)
    s.text(150, 160, "Where is ‘f’ (row 1, col 2)?", size=13, bold=True)
    s.text(150, 184, "row-major: 1 × 3 + 2 = 5", size=13, mono=True)
    s.text(150, 206, "col-major: 2 × 2 + 1 = 5", size=13, mono=True)
    s.text(150, 232, "‘b’ is 1 in row-major but 2 in column-major", size=12, color=WARN)
    return s.render("Memory is one long line, so a grid must be flattened. Languages choose row-major or column-major order.")


def matmul():
    s = SVG(760, 200, "Multiplying two matrices, row by column")
    s.text(160, 30, "A", size=14, bold=True)
    s.grid(110, 45, 2, 2, 50, 40, [["1", "2"], ["3", "4"]], [["#fbf0dd", "#fbf0dd"], ["white", "white"]], size=16)
    s.text(240, 90, "×", size=24)
    s.text(330, 30, "B", size=14, bold=True)
    s.grid(280, 45, 2, 2, 50, 40, [["5", "6"], ["7", "8"]], [["#dcebf6", "white"], ["#dcebf6", "white"]], size=16)
    s.text(410, 90, "=", size=24)
    s.grid(440, 45, 2, 2, 60, 40, [["19", "22"], ["43", "50"]], [["#e8f1e4", "white"], ["white", "white"]], size=16)
    s.text(600, 60, "Top-left:", size=13, anchor="start", bold=True)
    s.text(600, 82, "row 1 of A × column 1 of B", size=12, anchor="start")
    s.text(600, 104, "= 1×5 + 2×7 = 19", size=13, anchor="start", mono=True)
    s.text(380, 170, "Each answer = one row of the first matrix × one column of the second, multiplied in pairs and added.", size=12, color=ACCENT)
    return s.render("Matrix multiplication. The number of columns in A must equal the number of rows in B.")


def reflect():
    s = SVG(760, 330, "Reflecting a triangle in the y-axis with a matrix")
    ox, oy, u = 420, 300, 40
    for i in range(-6, 7):
        s.line(ox + i * u, oy - 5 * u, ox + i * u, oy, color="#d5e2ec", width=1)
    for j in range(0, 6):
        s.line(ox - 6 * u, oy - j * u, ox + 6 * u, oy - j * u, color="#d5e2ec", width=1)
    s.line(ox - 6 * u, oy, ox + 6 * u, oy, color=INK, width=2)
    s.line(ox, oy, ox, oy - 5 * u, color=INK, width=2)
    s.text(ox + 6 * u - 5, oy + 18, "x", size=13)
    s.text(ox - 10, oy - 5 * u + 12, "y", size=13)
    tri = [(1, 1), (4, 1), (1, 3)]
    s.poly([(ox + x * u, oy - y * u) for x, y in tri], fill="#dcebf6", stroke=LINE)
    s.poly([(ox - x * u, oy - y * u) for x, y in tri], fill="#fbf0dd", stroke="#b58a3a")
    s.text(ox + 3 * u, oy - 3.5 * u, "original (1,1) (4,1) (1,3)", size=12)
    s.text(ox - 3.5 * u, oy - 3.5 * u, "image (−1,1) (−4,1) (−1,3)", size=12)
    s.text(20, 32, "[ −1  0 ]  ×  [ x ]", size=15, mono=True, anchor="start")
    s.text(20, 54, "[  0  1 ]     [ y ]", size=15, mono=True, anchor="start")
    s.text(20, 78, "x becomes −x; y stays", size=12, color=ACCENT, anchor="start")
    return s.render("Graphics software moves, reflects, rotates and scales shapes by multiplying each corner’s coordinates by a matrix.")


D2 = deeper("D2",
    h3("Arrays of any size"),
    dims(),
    row_col_major(),
    p("A program can calculate where any item is stored without searching. For a grid with R rows and C columns stored in <strong>row-major</strong> order, item [row][col] is at offset <code>row × C + col</code>. In <strong>column-major</strong> order it is at <code>col × R + row</code>. Multiplying the offset by the size of each item gives the byte position. Reading memory in the order it is stored is faster, because nearby items arrive in cache together."),
    h3("Calculating with matrices"),
    matmul(),
    table(["Operation", "Rule", "Used for"], [
        ["Addition", "add the matching positions (same size matrices only)", "combining totals, e.g. two shops’ monthly sales"],
        ["Scalar multiplication", "multiply every item by one number", "a 10% price rise (× 1.1)"],
        ["Multiplication", "row × column, multiplied in pairs and added", "revenue from quantities × prices; transforming graphics"],
        ["Transpose", "swap rows and columns", "making the sizes match before multiplying"],
        ["Inverse", "the matrix that ‘undoes’ another; exists only if the determinant is not 0", "solving simultaneous equations"],
    ], caption="Matrix operations"),
    reflect(),
    worked("Solving simultaneous equations with a matrix", [
        "Cinema tickets: 2 adults and 1 child cost £11; 1 adult and 3 children cost £13. Let a = adult price, c = child price.",
        "Write it as a matrix equation: [2 1 / 1 3] × [a / c] = [11 / 13].",
        "The determinant is 2 × 3 − 1 × 1 = 5, which is not 0, so an inverse exists: (1/5) × [3 −1 / −1 2].",
        "Multiply: a = (3 × 11 − 1 × 13) ÷ 5 = 20 ÷ 5 = 4, and c = (−1 × 11 + 2 × 13) ÷ 5 = 15 ÷ 5 = 3.",
        "Check: 2 × 4 + 3 = 11 ✓ and 4 + 3 × 3 = 13 ✓. An adult ticket is £4 and a child ticket is £3.",
    ], "Spreadsheets do this with array formulas such as MINVERSE and MMULT."),
    terms([
        ("Matrix", "a rectangular grid of numbers arranged in rows and columns."),
        ("Dimensions", "the size of a matrix, rows × columns, e.g. 2 × 3."),
        ("Row-major order", "storing a grid one row after another."),
        ("Column-major order", "storing a grid one column after another."),
        ("Determinant", "a number calculated from a square matrix; if it is 0 there is no inverse."),
    ]),
    think([
        ("A 4 × 10 grid is stored in row-major order. What is the offset of [3][7]?", "3 × 10 + 7 = 37."),
        ("Can a 2 × 3 matrix be multiplied by another 2 × 3 matrix?", "No. The first has 3 columns but the second has 2 rows; they must match. Transposing the second (to 3 × 2) would make it possible."),
        ("Which matrix reflects a shape in the x-axis?", "[1 0 / 0 −1]: x stays the same and y becomes −y."),
    ]),
)

SECTIONS = {"D1": D1, "D2": D2}
