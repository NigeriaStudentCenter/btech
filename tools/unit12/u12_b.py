"""Unit 12 Software Development: lessons for learning aims C and D (original content)."""
from u12_a import *  # noqa
from u12_a import SVG, LINE, ARROW, ACCENT, WARN, RED, REDBG, AMBERBG, BLUEBG, GREENBG, GREEN, PURPLEBG, code, tryit, spec, fc_term, fc_io, fc_proc, fc_dec, assignment_link


# ---------- C1 IDE and event handling ----------
def ide_fig():
    s = SVG(760, 300, "The parts of the Visual Studio IDE")
    s.box(10, 10, 740, 280, fill="#f6f9fc", stroke=LINE)
    s.box(20, 20, 720, 26, "Menu and toolbar: File · Debug ▶ Start (F5) · Build", size=12, fill="#e3ebf3", rx=3)
    s.box(20, 56, 130, 224, fill="white")
    s.text(85, 76, "Toolbox", size=13, bold=True)
    for i, t in enumerate(["Label", "TextBox", "Button", "ComboBox", "ListBox", "CheckBox"]):
        s.text(40, 102 + i * 26, t, size=12, anchor="start")
    s.box(165, 56, 380, 224, fill="white")
    s.text(355, 76, "Form designer (Form1.vb [Design])", size=13, bold=True)
    s.box(200, 95, 300, 160, fill="#eef4fa", stroke="#245d83")
    s.box(220, 120, 110, 26, "txtName", size=11, fill="white", rx=3)
    s.box(220, 160, 110, 30, "btnHello", size=11, fill="#dcebf6", rx=4)
    s.text(350, 215, "lblMessage", size=11, anchor="start")
    s.box(560, 56, 180, 104, fill="white")
    s.text(650, 76, "Solution Explorer", size=13, bold=True)
    s.text(580, 102, "MyProject", size=12, anchor="start")
    s.text(590, 124, "Form1.vb", size=12, anchor="start")
    s.box(560, 170, 180, 110, fill="white")
    s.text(650, 190, "Properties", size=13, bold=True)
    for i, t in enumerate(["(Name)  btnHello", "Text    Say hello", "BackColor  …", "Font    …"]):
        s.text(572, 214 + i * 18, t, size=11, anchor="start", mono=True)
    return s.render("Drag controls from the Toolbox onto the form, set their properties, then double-click a control to write its event code.")


C1 = lesson("C1", "Learning aim C", "The development environment, forms and events",
    "use an IDE to create a form, set properties of controls, and write event-handling code for inputs and outputs.", spec("C · Developing software · Event handling"),
    p("You will develop programs in <strong>Visual Basic .NET</strong> using <strong>Visual Studio</strong> (Community edition is free). Choose <em>Windows Forms App (.NET Framework) – Visual Basic</em> when you create a project."),
    ide_fig(),
    table(["Control", "Prefix", "Use", "Key properties"], [
        ["Label", "lbl", "show text or output", "Text, Font, ForeColor"],
        ["TextBox", "txt", "user types input", "Text, MaxLength, PasswordChar, Multiline"],
        ["Button", "btn", "user clicks to run code", "Text, Enabled"],
        ["ComboBox (drop-down list)", "cbo", "choose from a list (built-in validation)", "Items, DropDownStyle, SelectedItem"],
        ["ListBox", "lst", "show several items", "Items"],
    ], caption="Common controls. Name them with a prefix, e.g. btnCalculate, so code is readable"),
    code(["Public Class Form1",
          "    ' Event handler: runs when the user clicks btnHello",
          "    Private Sub btnHello_Click(sender As Object, e As EventArgs) Handles btnHello.Click",
          "        Dim name As String = txtName.Text          ' INPUT from a text box",
          "        lblMessage.Text = \"Hello, \" & name & \"!\"   ' OUTPUT to a label",
          "        MessageBox.Show(\"Welcome to programming\")    ' OUTPUT in a message box",
          "    End Sub",
          "End Class"], "Press F5 to build and run. Stop with the red square, or by closing the form."),
    tryit("your first form", ["Create a new Windows Forms App (Visual Basic) called HelloApp.", "Add a TextBox (txtName), a Button (btnHello, Text “Say hello”) and a Label (lblMessage).", "Double-click the button and type the code above. Run it with F5.", "Change the form’s BackColor and the label’s Font in the Properties window.", "Build an .exe: Build → Build Solution, then find it in the project’s bin\\Debug folder."], "No Visual Studio at home? Console versions of the practicals run in your browser at dotnetfiddle.net (choose VB.NET)."),
    terms([("IDE", "integrated development environment: editor, designer, compiler and debugger in one."), ("Control", "an object on a form, such as a button or text box."), ("Property", "a setting of a control, e.g. Text or BackColor."), ("Event handler", "a subroutine that runs when an event happens.")]),
    think([("What is the difference between the (Name) and Text properties of a button?", "(Name) is what the code uses to refer to it (btnSave); Text is what the user sees on the button (“Save”)."),
           ("Why is the code inside btnHello_Click not run when the program starts?", "It is an event handler: it only runs when the Click event happens.")]),
)


# ---------- C2 variables, data types, operators ----------
def var_fig():
    s = SVG(760, 190, "Variables are labelled boxes in memory")
    items = [("age", "Integer", "15", BLUEBG), ("price", "Decimal", "9.50", AMBERBG), ("name", "String", "\"Priya\"", GREENBG), ("member", "Boolean", "True", PURPLEBG), ("grade", "Char", "\"B\"c", "#eef0f3")]
    for i, (n, t, v, f) in enumerate(items):
        x = 20 + i * 148
        s.box(x, 50, 134, 70, v, size=17, fill=f, rx=6)
        s.text(x + 67, 38, n, size=14, bold=True)
        s.text(x + 67, 142, t, size=12, color=ARROW)
    s.text(380, 178, "Dim price As Decimal = 9.5D   →   a box called price that can only hold decimal numbers", size=12, mono=True)
    return s.render("A variable has a name, a data type and a value that can change while the program runs. A constant’s value cannot change.")


C2 = lesson("C2", "Learning aim C", "Variables, constants, data types and operators",
    "declare variables and constants with suitable data types, use assignment, arithmetic and logical operators, and explain local and global scope.", spec("C · Constructs and techniques · data types"),
    var_fig(),
    table(["Data type", "Holds", "Example"], [
        ["Integer", "whole numbers", "<code>Dim seats As Integer = 120</code>"],
        ["Decimal / Double (real)", "numbers with a decimal point (Decimal for money)", "<code>Dim price As Decimal = 4.99D</code>"],
        ["String", "text", "<code>Dim town As String = \"Bedford\"</code>"],
        ["Char", "one character", "<code>Dim initial As Char = \"J\"c</code>"],
        ["Boolean", "True or False", "<code>Dim paid As Boolean = False</code>"],
        ["Date", "a date and time", "<code>Dim today As Date = Date.Today</code>"],
    ], caption="Data types"),
    table(["Operator", "Meaning", "Example → result"], [
        ["+ − * /", "add, subtract, multiply, divide", "7 / 2 → 3.5"],
        ["\\", "whole-number division", "7 \\ 2 → 3"],
        ["Mod", "remainder (% in many languages)", "7 Mod 2 → 1"],
        ["=  &lt;&gt;  &lt;  &lt;=  &gt;  &gt;=", "comparison", "age &gt;= 18 → True or False"],
        ["And  Or  Not", "logical", "age &gt;= 13 And age &lt;= 19"],
        ["&amp;", "join strings (concatenate)", "\"Hi \" &amp; name"],
    ], caption="Operators"),
    code(["Public Class Form1",
          "    Const VAT_RATE As Decimal = 0.2D          ' constant: never changes",
          "    Dim basketTotal As Decimal = 0             ' GLOBAL: usable by every subroutine in the form",
          "",
          "    Private Sub btnAdd_Click(sender As Object, e As EventArgs) Handles btnAdd.Click",
          "        Dim itemPrice As Decimal = CDec(txtPrice.Text)   ' LOCAL: only exists inside this sub",
          "        basketTotal = basketTotal + itemPrice              ' assignment",
          "        lblTotal.Text = (basketTotal * (1 + VAT_RATE)).ToString(\"C\")",
          "    End Sub",
          "End Class"]),
    terms([("Variable", "a named storage location whose value can change."), ("Constant", "a named value that cannot change while the program runs."), ("Local variable", "exists only inside the subroutine where it is declared."), ("Global variable", "declared outside subroutines; available throughout the program.")]),
    think([("Which data type would you use for a phone number, and why not Integer?", "String: phone numbers start with 0, may contain spaces or +, and are never used in calculations."),
           ("What is 17 Mod 5 and 17 \\ 5?", "17 Mod 5 = 2 (the remainder); 17 \\ 5 = 3 (whole-number division).")]),
)


# ---------- C3 sequence and selection ----------
C3 = lesson("C3", "Learning aim C", "Sequence and selection",
    "write programs that use sequence, If…Then…Else, ElseIf, nested If, logical operators and Select Case.", spec("C · Constructs: sequence, selection"),
    p("<strong>Sequence</strong> means instructions run one after another, in order. <strong>Selection</strong> means the program chooses which instructions to run, depending on a condition."),
    code(["' Login check: sequence then selection",
          "Dim attempt As String = txtPassword.Text",
          "If attempt = \"Lantern42\" Then",
          "    MessageBox.Show(\"Access granted\")",
          "Else",
          "    MessageBox.Show(\"Access denied\")",
          "End If"], "Set the text box’s PasswordChar property to * to hide what is typed."),
    code(["' Grade bands with ElseIf",
          "Dim mark As Integer = CInt(txtMark.Text)",
          "If mark >= 70 Then",
          "    lblGrade.Text = \"Distinction\"",
          "ElseIf mark >= 55 Then",
          "    lblGrade.Text = \"Merit\"",
          "ElseIf mark >= 40 Then",
          "    lblGrade.Text = \"Pass\"",
          "Else",
          "    lblGrade.Text = \"Not yet achieved\"",
          "End If"], "Conditions are checked from the top; the first true one runs and the rest are skipped."),
    code(["' Select Case: neater than many ElseIfs when checking one value",
          "Select Case cboDay.Text",
          "    Case \"Saturday\", \"Sunday\"",
          "        lblRate.Text = \"Weekend rate\"",
          "    Case \"Monday\", \"Tuesday\", \"Wednesday\", \"Thursday\", \"Friday\"",
          "        lblRate.Text = \"Weekday rate\"",
          "    Case Else",
          "        lblRate.Text = \"Choose a day\"",
          "End Select"]),
    tryit("selection practice", ["Make a form that asks for a temperature in °C and says “Freezing” (below 0), “Cold” (0–10), “Mild” (11–20) or “Hot” (above 20).", "Add a check box ‘Raining?’ and use And to show “Take a coat” when it is cold and raining.", "Write a Select Case that turns a number 1–7 into a day name, with Case Else for invalid numbers."]),
    terms([("Sequence", "instructions carried out in order."), ("Selection", "choosing a path depending on a condition."), ("Nested If", "an If statement inside another If."), ("Select Case", "selection that compares one value against several cases.")]),
    think([("In the grade code, what is shown for a mark of 55? Why is the order of the ElseIfs important?", "Merit. If the Pass check (>= 40) came first, 55 would wrongly show Pass, because the first true condition wins."),
           ("Write a condition that is true for ages 13 to 19 inclusive.", "age >= 13 And age <= 19")]),
)


# ---------- C4 iteration and recursion ----------
def loop_fig():
    s = SVG(760, 260, "Counter-controlled and condition-controlled loops")
    s.text(190, 22, "FOR loop: repeat a set number of times", size=13, bold=True)
    fc_proc(s, 100, 40, 180, "count = 1")
    s.arrow(190, 76, 190, 96, width=1.6)
    fc_dec(s, 190, 130, 160, 64, "count <= 5?")
    s.arrow(190, 162, 190, 182, width=1.6)
    s.text(200, 178, "Yes", size=12, anchor="start")
    fc_proc(s, 100, 184, 180, "show count; count + 1")
    s.add(f'<path d="M100 202 L60 202 L60 130 L110 130" stroke="{ARROW}" stroke-width="1.6" fill="none"/>')
    s.arrow(270, 130, 330, 130, width=1.6, label="No → end", ly=-6)
    s.text(570, 22, "WHILE / DO loop: repeat until a condition changes", size=13, bold=True)
    for i, t in enumerate(["Dim total As Integer = 0", "Do While total < 20", "    total = total + 5", "Loop", "' runs 4 times: 5, 10, 15, 20"]):
        s.text(430, 60 + i * 24, t, size=13, anchor="start", mono=True, color=ACCENT if i == 4 else "#17334b")
    s.text(570, 210, "Use FOR when you know how many times;", size=12, color=ARROW)
    s.text(570, 228, "use WHILE / DO when you don’t.", size=12, color=ARROW)
    return s.render("Iteration repeats code instead of copying it out many times, which makes programs shorter and easier to maintain.")


C4 = lesson("C4", "Learning aim C", "Iteration: counter-controlled and conditional loops, and recursion",
    "use For…Next, Do While, Do…Loop Until and nested loops, and explain recursion.", spec("C · Constructs: iteration, recursion"),
    loop_fig(),
    code(["' Counter-controlled: a times table",
          "lstTable.Items.Clear()",
          "For i As Integer = 1 To 12",
          "    lstTable.Items.Add(i & \" x 7 = \" & (i * 7))",
          "Next"]),
    code(["' Conditional: keep asking until the PIN is right (max 3 tries)",
          "Dim tries As Integer = 0",
          "Dim pin As String",
          "Do",
          "    pin = InputBox(\"Enter your PIN\")",
          "    tries = tries + 1",
          "Loop Until pin = \"2468\" Or tries = 3",
          "If pin = \"2468\" Then MessageBox.Show(\"Unlocked\") Else MessageBox.Show(\"Locked out\")"], "Do … Loop Until always runs at least once; Do While … Loop may not run at all."),
    h3("Recursion"),
    p("A <strong>recursive</strong> function calls itself on a smaller version of the problem, and must have a <strong>base case</strong> that stops it."),
    code(["Function Factorial(n As Integer) As Integer",
          "    If n <= 1 Then Return 1            ' base case: stop",
          "    Return n * Factorial(n - 1)         ' calls itself with a smaller n",
          "End Function",
          "' Factorial(4) = 4 × 3 × 2 × 1 = 24"]),
    tryit("loops practice", ["Show the numbers 1 to 8, one per line, in a multiline text box; then change it to show the running total after each number.", "Use a Do While loop that doubles a number starting at 1 until it is over 1000. How many loops?", "Use a nested loop to draw a 5 × 5 square of * characters."]),
    terms([("Iteration", "repeating a set of instructions."), ("Counter-controlled loop", "repeats a fixed number of times (For … Next)."), ("Conditional loop", "repeats while or until a condition is true (Do While, Do … Loop Until)."), ("Recursion", "a subroutine that calls itself, with a base case to stop.")]),
    think([("What would happen if a Do While loop’s condition never became false?", "It would loop forever (an infinite loop) and the program would freeze."),
           ("How many times does For k = 2 To 10 Step 2 run?", "5 times: k = 2, 4, 6, 8, 10.")]),
)


# ---------- C5 subroutines and functions ----------
C5 = lesson("C5", "Learning aim C", "Subroutines, functions and procedures",
    "write procedures (Sub) and functions (Function) with parameters and return values, and explain why they improve programs.", spec("C · Constructs: subroutines/functions/procedures"),
    p("A <strong>subroutine</strong> is a named block of code that does one job. A <strong>procedure</strong> (Sub) does a task; a <strong>function</strong> does a task and <strong>returns a value</strong>."),
    code(["Public Class Form1",
          "    ' Function: returns the price after discount",
          "    Private Function DiscountedPrice(price As Decimal, memberType As String) As Decimal",
          "        Select Case memberType",
          "            Case \"Junior\" : Return price * 0.5D",
          "            Case \"Senior\" : Return price * 0.7D",
          "            Case Else : Return price",
          "        End Select",
          "    End Function",
          "",
          "    ' Procedure: clears the form ready for the next booking",
          "    Private Sub ClearForm()",
          "        txtName.Clear()",
          "        cboClass.SelectedIndex = -1",
          "        lblPrice.Text = \"\"",
          "    End Sub",
          "",
          "    Private Sub btnCalculate_Click(sender As Object, e As EventArgs) Handles btnCalculate.Click",
          "        Dim total As Decimal = DiscountedPrice(6D * CInt(txtSessions.Text), cboMember.Text)",
          "        lblPrice.Text = total.ToString(\"C\")",
          "    End Sub",
          "End Class"]),
    table(["Benefit", "Why it matters"], [
        ["Reuse", "write once, call many times, e.g. DiscountedPrice from several buttons"],
        ["Maintainability", "change the discount rules in one place only"],
        ["Testing", "test each subroutine on its own"],
        ["Readability", "the main code reads like a list of steps: Validate(), Calculate(), Save()"],
        ["Teamwork", "different programmers can write different subroutines"],
    ], caption="Why use subroutines?"),
    terms([("Procedure", "a subroutine that performs a task (Sub)."), ("Function", "a subroutine that returns a value (Function … As type)."), ("Parameter", "a value passed into a subroutine."), ("Return value", "the result a function sends back.")]),
    think([("What is the difference between a procedure and a function?", "A function returns a value to the code that called it; a procedure just carries out a task."),
           ("What would DiscountedPrice(10, \"Junior\") return?", "5 (half price for a junior).")]),
)


# ---------- C6 data structures and strings ----------
def array_fig():
    s = SVG(760, 200, "An array and a record")
    s.text(20, 26, "Array: classes(0 To 4) As String", size=13, anchor="start", bold=True, mono=True)
    for i, t in enumerate(["Yoga", "Spin", "Pilates", "HIIT", "Swim"]):
        s.box(20 + i * 100, 40, 96, 40, t, size=13, fill=BLUEBG, rx=3)
        s.text(68 + i * 100, 98, f"index {i}", size=11, color=ARROW)
    s.text(20, 140, "Record (Structure) Booking:", size=13, anchor="start", bold=True, mono=True)
    for i, (a, b) in enumerate([("memberName", "\"Priya Shah\""), ("className", "\"Spin\""), ("sessions", "3"), ("price", "18.00")]):
        s.box(20 + i * 180, 150, 172, 40, f"{a} = {b}", size=12, fill=AMBERBG, rx=3)
    s.text(620, 70, "classes(2) is \"Pilates\"", size=13, anchor="start", color=ACCENT)
    return s.render("An array stores many values of the same type under one name. A record groups different fields about one thing.")


C6 = lesson("C6", "Learning aim C", "Data structures and string handling",
    "use one-dimensional arrays, records (user-defined types) and string-handling functions.", spec("C · Data structures · string handling"),
    array_fig(),
    code(["Dim classes() As String = {\"Yoga\", \"Spin\", \"Pilates\", \"HIIT\", \"Swim\"}",
          "For i As Integer = 0 To classes.Length - 1        ' loop through every element",
          "    cboClass.Items.Add(classes(i))",
          "Next",
          "",
          "Structure Booking                                 ' a record / user-defined type",
          "    Dim memberName As String",
          "    Dim className As String",
          "    Dim sessions As Integer",
          "    Dim price As Decimal",
          "End Structure",
          "Dim todaysBookings As New List(Of Booking)        ' a list of records"], "Arrays in VB start at index 0."),
    table(["String function", "What it does", "Example → result"], [
        ["<code>.Length</code>", "number of characters", "\"Bedford\".Length → 7"],
        ["<code>.ToUpper()</code> / <code>.ToLower()</code>", "change case", "\"yoga\".ToUpper() → \"YOGA\""],
        ["<code>.Substring(start, length)</code>", "part of a string (first character is 0)", "\"Bedford\".Substring(0, 3) → \"Bed\""],
        ["<code>.IndexOf(text)</code>", "position of text, or −1 if not found", "\"Bedford\".IndexOf(\"ford\") → 3"],
        ["<code>.Trim()</code>", "remove spaces at the start and end", "\"  Ali \".Trim() → \"Ali\""],
        ["<code>.Split(\",\")</code>", "break into an array of parts", "\"Spin,3,18\".Split(\",\") → {\"Spin\",\"3\",\"18\"}"],
        ["<code>&amp;</code>", "join strings", "\"Mr \" &amp; \"Lee\" → \"Mr Lee\""],
    ], caption="Basic string handling"),
    tryit("strings and arrays", ["Ask for a first name and surname; show initials in capitals (e.g. “PS”) using Substring and ToUpper.", "Store six player names in an array using InputBox in a loop, then show them in a ListBox.", "Compare two words and show them in alphabetical order (hint: use ToUpper first so case does not matter)."]),
    terms([("Array", "a data structure holding many values of the same type, accessed by an index."), ("Index", "the position of an element in an array (starting at 0 in VB)."), ("Record / structure", "a user-defined type grouping related fields of different types."), ("String handling", "working with text: length, case, substrings, searching, splitting.")]),
    think([("What does \"Software\".Substring(4, 4) return?", "\"ware\" (start at index 4, take 4 characters)."),
           ("Why use an array instead of six separate variables?", "One name, and a loop can process every element, so the code is shorter and easy to change if there are more items.")]),
)


# ---------- C7 file handling, validation and compiling ----------
def file_fig():
    s = SVG(760, 170, "Writing to and reading from a text file")
    s.box(20, 50, 190, 70, "Program", "booking saved", size=14, fill=BLUEBG, bold=True)
    s.box(285, 30, 190, 110, fill="white")
    s.text(380, 52, "bookings.txt", size=13, bold=True)
    for i, t in enumerate(["Priya Shah,Spin,3,18.00", "Tom Bell,Yoga,1,6.00", "Ana Cruz,Swim,2,6.00"]):
        s.text(300, 78 + i * 20, t, size=11, anchor="start", mono=True)
    s.box(550, 50, 190, 70, "Program", "list loaded next day", size=14, fill=GREENBG, bold=True)
    s.arrow(210, 85, 283, 85, width=2)
    s.text(246, 112, "open, write,", size=11)
    s.text(246, 126, "close", size=11)
    s.arrow(475, 85, 548, 85, width=2)
    s.text(512, 112, "open, read,", size=11)
    s.text(512, 126, "close", size=11)
    s.text(380, 162, "Data in variables is lost when the program closes; data in a file is kept.", size=12, color=ARROW)
    return s.render("File handling stores data permanently. Each line can hold one record, with fields separated by commas.")


C7 = lesson("C7", "Learning aim C", "File handling, validation, error handling and compiling",
    "open, read, write and close text files, validate input, handle errors so the program does not crash, comment the code and compile an executable.", spec("C · File handling · annotation · compiling"),
    file_fig(),
    code(["Imports System.IO",
          "",
          "' WRITE: add one booking to the end of the file (creates it if needed)",
          "Private Sub SaveBooking(line As String)",
          "    Using writer As New StreamWriter(\"bookings.txt\", True)   ' open, True = append",
          "        writer.WriteLine(line)                                  ' write",
          "    End Using                                                   ' close (automatically)",
          "End Sub",
          "",
          "' READ: show every booking in a ListBox",
          "Private Sub LoadBookings()",
          "    lstBookings.Items.Clear()",
          "    If Not File.Exists(\"bookings.txt\") Then Exit Sub          ' error handling: no file yet",
          "    Using reader As New StreamReader(\"bookings.txt\")           ' open",
          "        Do While Not reader.EndOfStream",
          "            lstBookings.Items.Add(reader.ReadLine())            ' read",
          "        Loop",
          "    End Using                                                   ' close",
          "End Sub"]),
    h3("Validation and error handling"),
    code(["Dim sessions As Integer",
          "If txtName.Text.Trim() = \"\" Then                                  ' presence check",
          "    MessageBox.Show(\"Please enter the member's name.\") : Exit Sub",
          "End If",
          "If Not Integer.TryParse(txtSessions.Text, sessions) Then         ' type check",
          "    MessageBox.Show(\"Sessions must be a whole number.\") : Exit Sub",
          "End If",
          "If sessions < 1 Or sessions > 10 Then                            ' range check",
          "    MessageBox.Show(\"Enter between 1 and 10 sessions.\") : Exit Sub",
          "End If",
          "Try",
          "    SaveBooking(txtName.Text & \",\" & cboClass.Text & \",\" & sessions)",
          "Catch ex As IOException                                         ' error handling",
          "    MessageBox.Show(\"The booking could not be saved. Check the file is not open.\")",
          "End Try"], "Validation stops bad data getting in; Try…Catch stops unexpected errors from crashing the program."),
    p("<strong>Annotate</strong> your code with comments explaining what each part does and why. It shows the assessor your understanding (2C.P4 asks for commentary throughout) and makes the code maintainable. Finally, <strong>compile</strong> the program into an executable (Build → Build Solution) so the client can run it without Visual Studio."),
    terms([("File handling", "opening, reading, writing and closing files."), ("Append", "add to the end of a file without deleting what is there."), ("Exception", "an error that happens while the program runs."), ("Executable", "a compiled program file (.exe) users can run.")]),
    assignment_link("1C.4 / 2C.P4 / 2C.M3", "Develop a program for the brief with a user interface (inputs and outputs), a range of constructs and techniques, and commentary throughout. For Merit it must be fully functional and meet the brief."),
    think([("Why must a file be closed after use?", "So the data is fully written and the file is released for other programs; Using … End Using closes it automatically."),
           ("What is the difference between validation and error handling?", "Validation checks input is sensible before it is used; error handling deals with problems that happen while running, such as a missing file.")]),
)


# ---------- C8 testing, debugging and refining ----------
def errors_fig():
    s = SVG(760, 180, "Three kinds of error")
    e = [("Syntax error", "breaks the rules of the language", "Dim total As Integr", "IDE underlines it; won’t compile", REDBG),
         ("Runtime error", "crashes while running", "CInt(\"abc\")", "use validation, Try…Catch", AMBERBG),
         ("Logic error", "runs, but gives the wrong result", "If age > 16  (should be >=)", "find with test data and the debugger", PURPLEBG)]
    for i, (a, b, c, d, f) in enumerate(e):
        x = 20 + i * 245
        s.box(x, 20, 230, 145, fill=f)
        s.text(x + 115, 44, a, size=15, bold=True)
        s.text(x + 115, 68, b, size=12)
        s.text(x + 115, 100, c, size=12, mono=True)
        s.text(x + 115, 140, d, size=11, color=ARROW)
    return s.render("Syntax errors stop the program compiling; runtime errors crash it; logic errors give wrong answers without any warning.")


C8 = lesson("C8", "Learning aim C", "Testing, debugging, feedback and refining",
    "test a program against the test plan and requirements, find and fix errors with the debugger, gather feedback and refine the program.", spec("C · Testing and refining the software"),
    errors_fig(),
    table(["Debugger tool", "Shortcut", "Use"], [
        ["Breakpoint", "F9", "pause the program at a chosen line"],
        ["Step Into / Over", "F11 / F10", "run one line at a time"],
        ["Locals / Watch window", "–", "see the value of variables while paused"],
        ["Error List", "–", "every syntax error with its line number"],
    ], caption="Using the Visual Studio debugger"),
    table(["No.", "Test data", "Expected", "Actual", "Pass / fail", "Action"], [
        ["1", "Adult, Yoga, 2", "£12.00", "£12.00", "Pass", "–"],
        ["2", "10 sessions", "accepted", "rejected", "Fail", "condition was &lt; 10; changed to &lt;= 10; re-tested: Pass"],
        ["3", "abc", "message", "program crashed", "Fail", "added Integer.TryParse; re-tested: Pass"],
    ], caption="Recording test results (with evidence screenshots)"),
    table(["Feedback question", "Quality measure"], [
        ["Did it give the right price every time?", "reliability"],
        ["Was it easy to use without help? Were the messages clear?", "usability"],
        ["Was it quick to respond and load the bookings?", "efficiency / performance"],
        ["Could another programmer understand and change the code?", "maintainability"],
        ["Did it run on the reception PC as well as yours?", "portability"],
    ], caption="Gathering feedback on quality"),
    p("<strong>Refine</strong> the program using test results and feedback, then <strong>re-test</strong>, because one change can break something else. Record every change, update your design documents, and add any new predefined code to your sources table."),
    real_world("cash machines paying out too much", "A software fault in a bank’s cash machines once let customers withdraw more money than they had, and the bank lost a great deal before it was fixed. Thorough testing with erroneous and boundary data is how such faults are found before users find them."),
    terms([("Debugging", "finding and fixing errors."), ("Breakpoint", "a marker that pauses the program at a line."), ("Functional testing", "checking every feature works as required."), ("Refine", "improve the program based on testing and feedback.")]),
    assignment_link("1C.5 / 2C.P5 / 2C.M4 / 2C.D3", "Pass: test against your plan and the requirements and repair faults. Merit: gather feedback on usability and quality and use it to improve. Distinction: refine the program taking account of code quality and user feedback."),
    think([("Which is harder to find, a syntax error or a logic error? Why?", "A logic error, because the program still runs; you only notice from wrong results, so you need good test data and the debugger."),
           ("Why re-test after fixing a fault?", "To prove the fix worked and that it did not break anything else.")]),
)


# ---------- D1 reviewing ----------
D1 = lesson("D1", "Learning aim D", "Reviewing the finished program",
    "review a finished program against user requirements, fitness for purpose, user experience, constraints and quality, and recommend improvements.", spec("D · Reviewing software"),
    table(["Review area", "Questions to answer", "Evidence to use"], [
        ["User requirements", "Which requirements are fully met, partly met or not met? Why?", "requirements list, test results"],
        ["Fitness for purpose", "Does it solve the client’s problem?", "problem definition, client feedback"],
        ["User experience", "Is navigation easy? Are messages clear?", "user feedback, observation"],
        ["Constraints", "How did language, time and device limits affect it? How did you work around them?", "your development log"],
        ["Quality", "reliability, usability, efficiency, maintainability, portability", "test plan, code comments, feedback"],
        ["Strengths and improvements", "What works well? What would you add or change next?", "all of the above"],
    ], caption="What a good review covers"),
    table(["Requirement", "Met?", "Evidence", "Comment / improvement"], [
        ["Calculate price with discounts", "Fully", "tests 1–6 passed", "–"],
        ["Save bookings", "Fully", "test 8; file screenshot", "could add a backup copy"],
        ["Print a daily list", "Partly", "list shown on screen", "printing not added because of time; next version"],
    ], caption="An evaluation grid helps you review requirement by requirement"),
    table(["Pass (explain)", "Merit (review the extent)", "Distinction (evaluate)"], [
        ["explain how the program meets the requirements and purpose", "weigh how far it meets each requirement, using feedback and constraints", "compare the final program with the initial design and code quality, justify every change, recommend further improvements"],
    ], caption="Moving up the grades"),
    terms([("Fitness for purpose", "whether the program does the job it was made for."), ("User experience", "how it feels to use the program."), ("Evaluation", "a balanced judgement with evidence and conclusions."), ("Recommendation", "a justified suggestion for future improvement.")]),
    assignment_link("1D.6 / 2D.P6 / 2D.M5 / 2D.D4", "Review your own program for the brief. Use your test results, feedback log and design changes as evidence."),
    think([("Why should a review mention requirements that were NOT met?", "It is honest and shows judgement; explaining why (e.g. a constraint) and how to fix it is what higher grades reward."),
           ("What is the difference between reviewing and evaluating?", "A review describes how well it meets needs; an evaluation weighs strengths and weaknesses with evidence, compares with the design, justifies changes and reaches conclusions.")]),
)

LESSONS = [C1, C2, C3, C4, C5, C6, C7, C8, D1]
