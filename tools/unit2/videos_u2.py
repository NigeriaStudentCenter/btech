"""Unit 2 videos: the MrBrownCS revision series from the department's video folder plus extra explainers,
embedded click-to-play from the creators' official YouTube uploads (verified by title and channel with YouTube oEmbed)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "unit19"))
from videos import card, CSS, JS  # noqa: F401

MB = "MrBrownCS"


def v(id, lesson, title, think, channel=MB, why="A short revision video from the MrBrownCS series (also in the department video folder).", duration=None):
    d = {"id": id, "lesson": lesson, "title": title, "channel": channel, "why": why, "think": think}
    if duration:
        d["duration"] = duration
    return d


VIDEOS = [
 v("g1N3l1l43kE", "A1", "Main Memory (RAM, ROM and Cache)", ["Why does a computer need ROM as well as RAM?"]),
 v("_0KIfGxp37E", "A1", "Secondary Storage (Optical, Magnetic, Solid-State & Cloud)", ["Which storage would you choose for a tablet, and why?"]),
 v("J0GxnTC8ILs", "A1", "Embedded Systems and their Common Characteristics", ["Name three embedded systems in a car."]),
 v("U-OCdTeZLac", "A1", "What is RAID 0, 1, 5 and 10?", ["Which RAID level gives no protection at all?"], channel="PowerCert Animated Videos", why="An animated explainer of the RAID levels your teacher covers with NAS and SAN."),
 v("NOS0grrM9N4", "A1", "Network Hardware (NIC, Switch, Router and WAP)", ["What does a NIC do?"]),
 v("7vbRGDgHukA", "A2", "Operating System (OS)", ["List four jobs of an operating system."]),
 v("5S-tTDeFZfY", "A2", "What is a Kernel?", ["Why can’t applications talk to hardware directly?"], channel="Techquickie", why="What the kernel does and why it sits between programs and hardware."),
 v("Z0uVNcNKags", "A2", "Utility Software and Models", ["Give two utilities and the problem each solves."]),
 v("PVD1LNDxOnc", "A2", "Open Source Explained", ["Give one benefit and one risk of open source for a business."], channel="IBM Technology", why="The principles of open source software and why organisations use it."),
 v("98ppOH7Rxsg", "A3", "Databases", ["Why store data in a database instead of a spreadsheet?"]),
 v("z98ECVn-w3Q", "A3", "Client-Server and Peer-to-Peer Networks", ["Which model suits a school sharing data across many PCs?"]),
 v("SbqXqQ-2ixs", "B1", "The CPU and Von Neumann Architecture", ["What is stored in memory in a Von Neumann computer?"]),
 v("4nY7mNHLrLk", "B1", "Harvard Architecture versus Von Neumann Architecture", ["Why can a Harvard processor fetch an instruction and data at the same time?"], channel="Computer Science Lessons", why="A clear comparison of the two architectures in B1."),
 v("DYUlEK5Rc-4", "B1", "How Contemporary CPUs Differ from Traditional Architectures", ["Why do modern CPUs mix ideas from both architectures?"]),
 v("1dZ55MjjZY0", "B2", "The Purpose of the CPU and its Components", ["What do the ALU and control unit each do?"]),
 v("eS1rEJZKr4U", "B2", "Factors Affecting CPU Performance (Clock Speed, Cache & Multiple-Cores)", ["Why don’t four cores make every program four times faster?"]),
 v("BVNx3wtJ9vs", "B2", "CPU Pipeline", ["What happens to a pipeline when the program branches?"], channel="Computerphile", why="Stretch: pipelining explained by a computer scientist.", duration="21:48"),
 v("LO4ige_j1Ig", "B3", "Special-Purpose Registers (PC, ACC, MAR and MDR)", ["What is the difference between the MAR and the MDR?"]),
 v("3osm-soT_Lc", "B3", "Address, Data and Control Buses", ["Which bus is one-way and which is two-way?"]),
 v("G7bqvpAw7HE", "B3", "How Interrupts Work in Modern Computers", ["What does the CPU save before it handles an interrupt?"], channel="BitLemon", why="Stretch: what really happens when an interrupt arrives."),
 v("Ol3PxSpEeT4", "C1", "Introduction to Binary", ["Why do computers use binary?"]),
 v("7LGgLi4vYsk", "C1", "Binary-Decimal Conversions", ["Convert 1011 0110 to denary."]),
 v("4wrBpIYimrw", "C1", "Binary Addition", ["What is an overflow error?"]),
 v("WbODFlqzSoc", "C1", "Signed Binary (Sign and Magnitude & Two’s Complement)", ["What is −1 in 8-bit two’s complement?"]),
 v("Aa13ifHrzH4", "C1", "Converting between Hexadecimal and Binary", ["Why is one hex digit worth exactly four bits?"]),
 v("afCRRm3_35g", "C1", "Left and Right Binary Shifts", ["What does a left shift of 2 places do to the value?"]),
 v("bbkcEiUjehk", "C1", "How Floating-Point Numbers Are Represented", ["What do the mantissa and exponent each control?"], channel="Spanning Tree", why="Stretch: an animated explanation of floating point."),
 v("p5VMk2oM8F8", "C1", "What is Binary Coded Decimal (BCD)?", ["Write 59 in BCD."], channel="RealPars", why="BCD and where it is still used, e.g. digital displays and controllers."),
 v("tdmeXcDX-Uc", "C2", "Representing Text in Binary (ASCII & Unicode)", ["Why did Unicode replace ASCII for most uses?"]),
 v("a3Y_ZvOr0K0", "C3", "Representing Images in Binary", ["How does colour depth affect file size?"]),
 v("HlOTuCFtuV8", "C3", "Representing Sound in Binary", ["How do sample rate and bit depth affect quality?"]),
 v("v1u-vY6NEmM", "C3", "Lossy and Lossless (RLE) Compression", ["When must you use lossless compression?"]),
 v("6bKeE1A5-LY", "D1", "Data Structures", ["What is the difference between an array and a record?"]),
 v("wjI1WNcIntg", "D1", "Data Structures: Stacks and Queues", ["Give a real use of a stack and a queue."], channel="HackerRank", why="Stacks (last in, first out) and queues (first in, first out) explained."),
 v("2spTnAiQg4M", "D2", "How To Multiply Matrices", ["Why must the columns of the first matrix equal the rows of the second?"], channel="The Organic Chemistry Tutor", why="Step-by-step matrix multiplication for D2."),
 v("XkY2DOUCWMU", "D2", "Matrix multiplication as composition", ["How can a matrix move or rotate a shape?"], channel="3Blue1Brown", why="Stretch: what matrix multiplication means geometrically."),
 v("CGulJriYNSI", "E1", "Serial and Parallel Data Transmission", ["Why is serial used for long distances?"]),
 v("SLjjgjp2bAA", "E1", "Synchronous and Asynchronous Transmission", ["What are start and stop bits for?"]),
 v("MVihcigDlbA", "E1", "Network Protocols and the 4 Layer Model", ["Why are protocols organised into layers?"]),
 v("BZlPgMsKvY0", "E1", "Encryption", ["What is the difference between plaintext and ciphertext?"]),
 v("-9rK3EZop_M", "E1", "Symmetric and Asymmetric Encryption", ["Why is a public key safe to share?"]),
 v("yWgKSx0eFzY", "E1", "Encryption and the Caesar Cipher", ["Why is a Caesar cipher easy to break?"]),
 v("RCkGauRMs2A", "E1", "Vigenère Cipher Explained (with Example)", ["Why is Vigenère harder to break than Caesar?"], channel="Aladdin Persson", why="The Vigenère cipher from your encryption lesson, worked through."),
 v("9uAIGQBkQzc", "E2", "Check Digits and Parity Bits", ["Which errors can a single parity bit not detect?"]),
 v("_x0vbnUKYSU", "E2", "Cyclic Redundancy Check (CRC)", ["Why is a CRC better than a parity bit?"], channel="Computerphile", why="Stretch: how CRCs catch errors.", duration="12:44"),
 v("5sskbSvha9M", "E3", "Error Correction", ["How can a receiver fix an error without asking again?"], channel="Computerphile", why="How forward error correction repairs data."),
 v("X8jsijhllIA", "E3", "But what are Hamming codes?", ["What extra information lets Hamming codes locate the wrong bit?"], channel="3Blue1Brown", why="Stretch: a beautiful explanation of error-correcting codes.", duration="20:05"),
 v("E5V9zBBAfWM", "F1", "Logic Gates (AND, OR and NOT)", ["When does an OR gate output 0?"]),
 v("LheGDXfUrwc", "F1", "Half Adder and Full Adder Explained", ["Which two gates make a half adder?"], channel="VAM! Physics & Engineering", why="How logic gates add binary numbers."),
 v("cTjFy18SjRc", "F1", "Boolean Algebra in 13 Minutes", ["Simplify A AND (A OR B)."], channel="TrevTutor", why="Stretch: the rules for simplifying Boolean expressions."),
 v("kUt0nS0yMtM", "F2", "Flowcharts", ["Which symbol shows a decision?"]),
 v("P5tayiDr24A", "F2", "Data Flow Diagrams (DFDs)", ["What do the arrows in a DFD show?"]),
 v("TdQgP_Gee_A", None, "Network Types and Performance", ["What factors affect network performance?"], why="Extra revision from the department video folder."),
 v("jXVtakoOjc0", None, "The Ethernet and WiFi Protocols", ["Why is Ethernet usually more reliable than Wi-Fi?"], why="Extra revision from the department video folder."),
 v("7LfTWbOp5vU", None, "TCP, IP, HTTP/S and FTP", ["Which protocol makes sure packets arrive in order?"], why="Extra revision from the department video folder."),
 v("0F1JP78JAPE", None, "Email Protocols: SMTP, POP and IMAP", ["Which protocol sends email?"], why="Extra revision from the department video folder."),
 v("CeTATgOp3eE", None, "Firewalls", ["What does a firewall check?"], why="Extra revision from the department video folder."),
]


def for_lesson(lid):
    vs = [x for x in VIDEOS if x["lesson"] == lid]
    return f'<h3 class="watch">Watch</h3>{"".join(card(x) for x in vs)}' if vs else ""
