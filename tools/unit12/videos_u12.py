"""Unit 12 videos, embedded click-to-play from the creators' official YouTube uploads (verified by title and channel with YouTube oEmbed)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "unit19"))
from videos import card, CSS, JS  # noqa: F401


def v(id, lesson, title, channel, why, think, duration=None):
    d = {"id": id, "lesson": lesson, "title": title, "channel": channel, "why": why, "think": think}
    if duration:
        d["duration"] = duration
    return d


MB = "MrBrownCS"
VIDEOS = [
 v("6hfOvs8pY1k", "A1", "What’s an algorithm?", "TED-Ed (David J. Malan)", "A short, friendly introduction to how computers follow step-by-step instructions.", ["What everyday task could you write an algorithm for?"], "4:58"),
 v("uFIt2GfCsYU", "A2", "High-Level and Low-Level Programming Languages", MB, "Why we write in high-level languages and what machine code is.", ["Give one advantage of each type of language."]),
 v("smswPsNcx2c", "A2", "Translators: Compilers and Interpreters", MB, "How source code is turned into something the CPU can run.", ["Why does a compiled program run without the compiler?"]),
 v("C5_UTE_Lyto", "A4", "Testing and Defensive Programming", MB, "How programmers make code robust and maintainable.", ["Which quality measures does defensive programming improve?"]),
 v("SaCYkPD4_K0", "B1", "Software Development Life Cycle: Explained", "AltexSoft", "The stages professional teams follow, and how agile differs from waterfall.", ["Which stage do you think is skipped most often, and what goes wrong?"], "12:31"),
 v("kUt0nS0yMtM", "B4", "Flowcharts", MB, "The flowchart symbols and how to read them.", ["Which symbol shows a decision?"]),
 v("UbANyxE7pGE", "B4", "Trace tables tutorial", "Computer Science Tutorials", "How to dry-run an algorithm with a trace table.", ["Why is a trace table useful before you write code?"]),
 v("preyTbKXDoQ", "B4", "How Do I Write Pseudocode?", MB, "Stretch: a longer walk-through of writing clear pseudocode.", ["How is pseudocode different from real code?"], "27:58"),
 v("NvrJ_WdNfhc", "B5", "Data Assurance Considerations", MB, "Validation, verification and keeping data accurate.", ["Give an example of a range check and a presence check."]),
 v("LkHgrPbl2H4", "C1", "Integrated Development Environments (IDEs) and their Common Tools", MB, "The tools inside an IDE such as Visual Studio.", ["Which IDE tool helps you find logic errors?"]),
 v("HFWQdGn5DaU", "C1", "Visual Basic (VB.NET) – Full Course for Beginners", "freeCodeCamp.org", "Reference: a full Visual Basic course. Dip into the parts you need rather than watching it all.", ["Find the section on the topic you are working on and try the example."], "3:17:20"),
 v("9QIFXyBYJQY", "C2", "Data Types, Variables & Constants", MB, "Choosing data types and when to use a constant.", ["Why is a phone number stored as a string?"]),
 v("WCC_dQwFPac", "C3", "3 Basic Programming Constructs: Sequence, Selection & Iteration", MB, "The three building blocks of every program.", ["Give one example of each construct from a program you have written."]),
 v("h8uR3zOjwUM", "C3", "IF Statements, ElseIf and Else – VB.NET", "Ken Swartwout", "Selection in Visual Basic, step by step.", ["What happens if two ElseIf conditions are both true?"], "8:10"),
 v("Mv9NEXX1VHc", "C4", "What on Earth is Recursion?", "Computerphile", "Stretch: how a function can call itself.", ["What stops a recursive function running forever?"], "9:40"),
 v("mScqZcfNJak", "C5", "Subprograms, Local Variables & Structured Programming", MB, "Why programs are split into procedures and functions.", ["Why can’t one subroutine see another’s local variables?"]),
 v("ZB0-yDoejJ4", "C5", "Defining Functions (and understanding Return Values)", MB, "How functions take parameters and return values.", ["What is the difference between a parameter and a return value?"]),
 v("Tx-5a6ka_rk", "C6", "Declaring and Using 1D Arrays", MB, "Storing lots of data under one name.", ["What is the index of the third element?"]),
 v("dLn1EVtlblM", "C6", "String Handling Operations", MB, "Length, substrings, case changes and more.", ["How would you get the first letter of a name?"]),
 v("JgllElxpSj0", "C7", "Reading and Writing with External Text Files", MB, "Keeping data after the program closes.", ["Why must a file be closed after writing?"]),
 v("fCexIOEjj0Y", "C8", "Approaches to Testing: Iterative/Terminal, Test Data and Test Plans", MB, "How to plan tests and choose test data.", ["Give normal, boundary and erroneous data for ‘age 16 to 65’."]),
 v("MSBRGGLVBsQ", "C8", "Syntax and Logic Errors, and Refining Algorithms", MB, "The difference between errors that stop a program and errors that give wrong answers.", ["Which kind of error will the IDE underline for you?"]),
]


def for_lesson(lid):
    vs = [x for x in VIDEOS if x["lesson"] == lid]
    return f'<h3>Watch</h3>{"".join(card(x) for x in vs)}' if vs else ""
