import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "unit19"))
sys.path.insert(0, str(HERE.parent / "deeper"))
from u19 import *  # noqa  lesson, device, tryit, cli, SVG, p, h3, table, terms, think, worked, real_world, ul
from u19 import SVG, device, INK, LINE, ARROW, ACCENT, WARN
import section_a as dA, section_b as dB, section_c as dC  # original diagrams from the Unit 2 course


def exam_tip(text):
    return f'<div class="assess"><h4>Exam focus</h4><p>{text}</p></div>'


def spec(code):
    return f"T Level core · {code}"


# ---------- NS number systems ----------
def bases_fig():
    s = SVG(760, 210, "The same number in four number bases")
    rows = [("Denary (base 10)", "digits 0–9", "173"), ("Binary (base 2)", "digits 0–1", "1010 1101"), ("Octal (base 8)", "digits 0–7", "255"), ("Hexadecimal (base 16)", "digits 0–9, A–F", "AD")]
    for i, (a, b, c) in enumerate(rows):
        y = 20 + i * 46
        s.box(20, y, 260, 38, fill=["#fbf0dd", "#dcebf6", "#e8f1e4", "#f3e8f9"][i])
        s.text(34, y + 24, a, size=14, anchor="start", bold=True)
        s.text(200, y + 24, b, size=12, anchor="start", color=ARROW)
        s.text(420, y + 26, c, size=20, mono=True, bold=True)
        s.arrow(290, y + 19, 330, y + 19, width=1.6)
    s.text(620, 70, "All four rows show", size=13)
    s.text(620, 90, "the same value.", size=13)
    s.text(620, 120, "Computers store binary;", size=12, color=ACCENT)
    s.text(620, 138, "hex is a short way", size=12, color=ACCENT)
    s.text(620, 156, "for people to write it.", size=12, color=ACCENT)
    return s.render("A number base is how many different digits the system uses. The value 173 written in four bases.")


NS = lesson("NS", "Number systems", "Binary, denary, octal and hexadecimal",
    "convert between binary, denary and hexadecimal, and add, subtract and multiply in binary.", "Scheme of work · weeks 2 and 6",
    p("Every piece of data a computer handles, from a photo to a network address, is stored as <strong>binary</strong>: patterns of 0s and 1s. A single 0 or 1 is a <strong>bit</strong>; 4 bits are a <strong>nibble</strong>; 8 bits are a <strong>byte</strong>. People working in digital jobs read binary and hexadecimal every day: in IP and MAC addresses, colour codes, error messages and packet captures."),
    bases_fig(),
    dC.place_values(),
    worked("Denary to binary (173)", [
        "Write the place values: 128, 64, 32, 16, 8, 4, 2, 1.",
        "173 − 128 = 45, so put 1 under 128. 64 does not fit into 45: 0. 45 − 32 = 13: 1. 16 does not fit: 0.",
        "13 − 8 = 5: 1. 5 − 4 = 1: 1. 2 does not fit: 0. 1 − 1 = 0: 1.",
        "Answer: <code>1010 1101</code>. Check: 128 + 32 + 8 + 4 + 1 = 173.",
    ]),
    worked("Binary to hexadecimal and back", [
        "Split the byte into two nibbles: <code>1010</code> and <code>1101</code>.",
        "1010 = 8 + 2 = 10 = A; 1101 = 8 + 4 + 1 = 13 = D. So the hex is <code>AD</code>.",
        "To go back, turn each hex digit into 4 bits: 3F → 0011 1111.",
    ]),
    dC.addition(),
    table(["Operation", "Binary rule", "Example"], [
        ["Addition", "0+0=0, 0+1=1, 1+1=10 (0 carry 1), 1+1+1=11", "0110 + 0011 = 1001 (6 + 3 = 9)"],
        ["Subtraction", "borrow like denary, or add the two’s complement of the number being taken away", "1001 − 0011 = 0110 (9 − 3 = 6)"],
        ["Multiplication", "shift left to multiply by 2; add shifted copies", "0101 × 0011 = 0101 + 1010 = 1111 (5 × 3 = 15)"],
    ], caption="Binary arithmetic"),
    dC.units(),
    terms([("Bit", "a single binary digit, 0 or 1."), ("Byte", "8 bits."), ("Nibble", "4 bits; one hex digit."), ("Base", "how many different digits a number system uses."), ("Overflow", "a result too big for the bits available.")]),
    exam_tip("Show your working for conversions: write the place-value headings, then the bits. A correct method can earn marks even if you slip on the final digit."),
    think([("Convert 0100 1100 to denary and hex.", "64 + 8 + 4 = 76. The nibbles 0100 and 1100 are 4 and C, so the hex is 4C."),
           ("Why do network engineers write MAC addresses in hex, not binary?", "A MAC address is 48 bits. In hex it is 12 short characters, much easier to read, type and compare without errors.")]),
)


# ---------- H1 7.1.1 physical computers ----------
def computers_fig():
    s = SVG(760, 250, "Four kinds of physical computer")
    items = [("pc", "Personal computer", "desktop or laptop\nfor one user"), ("phone", "Mobile device", "smartphone, tablet:\nportable, battery"), ("server", "Server", "provides services\nto many clients"), ("", "Embedded device", "a computer inside\nanother product")]
    for i, (k, t, sub) in enumerate(items):
        x = 20 + i * 185
        s.box(x, 20, 170, 210, fill="white", stroke="#c9d7e3")
        if k:
            device(s, k, x + 53, 40)
        else:
            s.box(x + 45, 38, 80, 50, fill="#eef0f3", rx=6)
            s.box(x + 67, 50, 36, 26, "MCU", size=10, fill="#dcebf6", rx=3)
        s.text(x + 85, 128, t, size=14, bold=True)
        s.text(x + 85, 152, sub, size=12)
    return s.render("Personal computers, mobile devices, servers and embedded devices are built for different jobs.")


def embedded_fig():
    s = SVG(760, 220, "Inside an embedded system: a smart thermostat")
    s.box(20, 80, 150, 60, "Temperature sensor", "input", size=13)
    s.box(20, 160, 150, 50, "Buttons / app", "input", size=12)
    s.box(270, 60, 220, 120, fill="#dcebf6")
    s.text(380, 88, "Microcontroller", size=15, bold=True)
    s.text(380, 110, "CPU + memory + I/O on one chip", size=12)
    s.text(380, 130, "fixed program in ROM/flash", size=12)
    s.text(380, 150, "real-time, low power, cheap", size=12)
    s.box(590, 70, 150, 55, "Boiler relay", "output (actuator)", size=13)
    s.box(590, 145, 150, 55, "Display / Wi-Fi", "output", size=13)
    s.arrow(170, 110, 268, 110)
    s.arrow(170, 185, 268, 160)
    s.arrow(490, 100, 588, 97)
    s.arrow(490, 150, 588, 172)
    s.text(380, 30, "Embedded devices do one dedicated job inside a larger product", size=13, color=ACCENT)
    return s.render("An embedded system reads sensors, runs one fixed program on a microcontroller, and controls outputs. Washing machines, cars, pacemakers and IoT devices all contain them.")


H1 = lesson("H1", "7.1 Hardware", "Types of physical computer",
    "describe the features and uses of personal computers, mobile devices, servers and embedded devices.", spec("7.1.1"),
    computers_fig(),
    table(["Type", "Key features", "Typical uses"], [
        ["Personal computer (desktop, laptop)", "general purpose; keyboard, mouse, screen; upgradable (desktop); portable (laptop)", "office work, programming, design, gaming, study"],
        ["Mobile device (smartphone, tablet)", "small, battery-powered, touchscreen, many sensors (GPS, accelerometer, camera), mobile processor, wireless connectivity", "communication, apps, photos, navigation, mobile working"],
        ["Server", "powerful processors, lots of RAM and storage, redundant parts, runs 24/7, managed remotely", "web, email, file, database, print and authentication services for many users"],
        ["Embedded device", "a small computer built into another product; one fixed job; low cost and power; often real-time", "washing machines, cars, medical devices, smart meters, IoT sensors"],
    ], caption="Physical computers compared"),
    dA.phone(),
    dA.server_rack(),
    embedded_fig(),
    h3("The Internet of Things (IoT)"),
    p("IoT devices are embedded systems with network connections: smart speakers, doorbells, thermostats, fitness trackers, factory sensors. They collect data and can be controlled remotely, which brings convenience and efficiency but also security risks, because many are cheap, rarely updated and joined to the same network as important systems."),
    terms([("Embedded system", "a computer inside a larger product, dedicated to one task."), ("Microcontroller", "a single chip with a processor, memory and inputs/outputs."), ("Server", "a computer that provides services to other computers over a network."), ("IoT", "Internet of Things: everyday objects with sensors and network connections.")]),
    exam_tip("For ‘describe the features’ questions, give a feature and say what it allows, e.g. “servers have redundant power supplies, so the service keeps running if one fails.”"),
    think([("Why does a server usually have more RAM than a personal computer?", "It runs services for many users at the same time, each needing memory for their requests, data and connections."),
           ("Give two features of an embedded device in a washing machine.", "It runs one fixed program (the wash cycles), reads sensors such as water level and temperature, and must be cheap, reliable and low-power.")]),
)


# ---------- H2 7.1.2 hardware devices ----------
def practical(title, steps, note=None):
    li = "".join(f"<li>{s}</li>" for s in steps)
    n = f'<p class="small">{note}</p>' if note else ""
    return f'<div class="tryit"><h4>Practical: {esc(title)}</h4><ol>{li}</ol>{n}</div>'


def cooling_fig():
    s = SVG(760, 260, "Air cooling and liquid cooling")
    s.text(190, 26, "Air cooling", size=15, bold=True)
    s.box(110, 150, 160, 30, "CPU", size=13, fill="#fbf0dd")
    for k in range(9):
        s.add(f'<rect x="{118 + k * 17}" y="80" width="8" height="68" fill="#b9c7d5"/>')
    s.circle(190, 60, 26, fill="#dcebf6")
    s.text(190, 65, "fan", size=12)
    s.text(190, 205, "heatsink fins spread heat; a fan blows it away", size=12)
    s.text(570, 26, "Liquid cooling", size=15, bold=True)
    s.box(430, 150, 110, 30, "CPU", size=13, fill="#fbf0dd")
    s.box(440, 125, 90, 24, "water block", size=11, fill="#dcebf6")
    s.box(620, 60, 110, 90, "Radiator", "+ fans", size=13, fill="#eef0f3")
    s.box(560, 170, 70, 30, "Pump", size=12, fill="#e8f1e4")
    s.add(f'<path d="M530 132 C580 110 590 90 618 90" stroke="{WARN}" stroke-width="3" fill="none"/>')
    s.add(f'<path d="M675 150 L675 185 L630 185" stroke="{ARROW}" stroke-width="3" fill="none"/>')
    s.add(f'<path d="M560 185 L420 185 L420 137 L438 137" stroke="{ARROW}" stroke-width="3" fill="none"/>')
    s.text(600, 80, "hot", size=11, color=WARN)
    s.text(580, 222, "coolant carries heat to a radiator:", size=12)
    s.text(580, 240, "quieter, better for high-power CPUs, costs more", size=12)
    return s.render("Processors must be cooled or they slow down (throttle) or fail. Air cooling is cheap and simple; liquid cooling handles more heat.")


H2 = lesson("H2", "7.1 Hardware", "Hardware devices inside and around a computer",
    "explain the features and use of input and output devices, processors, memory, storage, motherboards, GPUs, network interfaces, cooling and sensors.", spec("7.1.2"),
    table(["Input devices", "Output devices", "Sensors (automatic input)"], [
        ["keyboard, mouse, touchscreen, microphone, scanner, webcam, barcode reader, game controller", "monitor, printer, speakers, headphones, projector, 3D printer, actuators (motors)", "temperature, light, motion (PIR), accelerometer, GPS, pressure, humidity, fingerprint"],
    ], caption="Getting data in and results out"),
    h3("Processors"),
    dB.multicore(),
    table(["Feature", "What it means", "Effect"], [
        ["Number of cores", "independent processing units on one chip", "more tasks at once (if software uses them)"],
        ["Clock speed (GHz)", "cycles per second", "higher = more instructions per second, but more heat"],
        ["Cache size (MB)", "very fast memory on the CPU", "fewer slow trips to RAM"],
        ["Mobile processors", "designed for low power, often a system on a chip", "longer battery life, less heat, slightly less peak speed"],
    ], caption="What affects processor performance"),
    h3("Memory and storage"),
    dA.hierarchy(),
    table(["", "RAM", "ROM"], [["Volatile?", "yes: loses data without power", "no: keeps data"], ["Holds", "programs and data in use now", "start-up instructions (BIOS/UEFI firmware)"], ["Can be changed?", "constantly read and written", "read-only (or rarely updated)"]], caption="RAM and ROM"),
    dA.hdd_ssd(),
    table(["Secondary storage", "How it stores data", "Strengths", "Weaknesses"], [
        ["Magnetic (HDD, tape)", "magnetised spinning platters or tape", "cheap per GB, huge capacity", "moving parts; slower; damaged by knocks"],
        ["Solid state (SSD, USB, SD)", "electrical charges in flash memory", "fast, silent, tough, low power", "more expensive per GB; limited write cycles"],
        ["Optical (CD, DVD, Blu-ray)", "laser reads pits and lands", "cheap, portable, good for distribution", "small capacity; scratches; slow"],
    ], caption="Secondary storage types"),
    h3("The motherboard, GPU, network interfaces and cooling"),
    dA.motherboard(),
    p("The <strong>motherboard</strong> connects every component and carries power and data between them. A <strong>graphics processing unit (GPU)</strong> has thousands of small cores for parallel work: graphics, video and AI. A <strong>network interface card</strong> connects the computer to a network; it may plug into a <strong>PCI/PCIe</strong> slot on the motherboard or into a <strong>USB</strong> port (for example a USB Wi-Fi adapter)."),
    cooling_fig(),
    terms([("Volatile", "loses its contents when the power is off."), ("Clock speed", "how many cycles a processor completes per second (GHz)."), ("Cache", "small, very fast memory on the processor."), ("GPU", "graphics processing unit: many cores for parallel processing."), ("PCIe", "the motherboard slot standard for expansion cards."), ("Thermal throttling", "slowing a processor down to stop it overheating.")]),
    practical("identify the parts", ["Use the Motherboard ID task: label the CPU socket, RAM slots, PCIe slots, chipset, SATA ports, power connectors and CMOS battery.", "Match connectors to their names: SATA, Molex, 24-pin, 4/8-pin CPU and 6/8-pin PCIe power.", "Look up a real motherboard specification online and find its RAM type, maximum RAM and number of M.2 slots."], "Your teacher runs the PC disassemble and reassemble practical in class with anti-static precautions."),
    exam_tip("When asked to justify hardware for a scenario, link each feature to the user’s need: “a video editor needs 32 GB RAM because large project files must stay in memory while editing.”"),
    think([("Why does adding more cores not always make a program faster?", "The program must be written to split its work into parallel threads; a program that runs step by step can only use one core."),
           ("A laptop feels slow when many browser tabs are open. Which upgrade is most likely to help, and why?", "More RAM: the tabs need more memory than is available, so the OS keeps swapping data to storage, which is much slower.")]),
)


# ---------- SW1 7.2.1 operating systems ----------
def ostypes_fig():
    s = SVG(760, 250, "Batch processing compared with a real-time system")
    s.text(190, 26, "Batch: collect, then process together", size=14, bold=True)
    for i in range(5):
        s.box(30 + i * 50, 50, 40, 40, "job", size=10, fill="#fbf0dd")
    s.arrow(280, 70, 330, 70)
    s.box(40, 120, 300, 50, "Run overnight on a schedule, no user input", size=12, fill="#dcebf6")
    s.text(190, 200, "e.g. payroll, bank statements, utility bills", size=12, color=ACCENT)
    s.text(570, 26, "Real-time: respond within a deadline", size=14, bold=True)
    s.box(420, 50, 110, 40, "Sensor", size=12)
    s.box(560, 50, 120, 40, "RTOS decides", size=12, fill="#dcebf6")
    s.box(560, 120, 120, 40, "Output acts", size=12)
    s.arrow(530, 70, 558, 70)
    s.arrow(620, 90, 620, 118)
    s.text(570, 190, "must happen within milliseconds, every time", size=12, color=WARN)
    s.text(570, 210, "e.g. airbags, autopilots, card payment approval", size=12, color=ACCENT)
    return s.render("Batch systems favour throughput with no interaction; real-time systems guarantee a response within a fixed time.")


SW1 = lesson("SW1", "7.2 Software", "Types of operating system",
    "explain the features and uses of batch, multitasking, real-time, network and mobile operating systems.", spec("7.2.1"),
    dA.os_layers(),
    table(["OS type", "Key features", "Examples of use"], [
        ["Batch", "non-interactive; processes high volumes of similar jobs together; runs on a schedule", "payroll, printing bills and statements, overnight data processing"],
        ["Multitasking", "runs many tasks concurrently by giving each a time slice; uses interrupts to respond to events", "Windows, macOS, Linux desktops"],
        ["Real-time (RTOS)", "guarantees a response within a deadline; used for monitoring and control, and transaction processing", "car engine management, airbags, medical monitors, booking seats or card payments"],
        ["Network OS", "shares resources (files, printers), manages users and permissions, supports communication across a network", "Windows Server, Linux servers"],
        ["Mobile OS", "for smartphones and tablets; lower processing requirements; manages power for longer battery life; touch interface; app store", "Android, iOS, iPadOS"],
    ], caption="Operating system types"),
    ostypes_fig(),
    dA.timeslice(),
    p("<strong>Time-slicing</strong> gives each running task a tiny slice of processor time in turn, so they appear to run at the same time. An <strong>interrupt</strong> is a signal (a key press, a network packet arriving, a timer) that makes the processor pause, deal with the event, then carry on."),
    terms([("Batch processing", "grouping jobs and processing them together without user interaction."), ("Time-slicing", "sharing processor time between tasks in small turns."), ("Interrupt", "a signal that makes the processor deal with an event."), ("RTOS", "real-time operating system: responds within a guaranteed time.")]),
    exam_tip("Match the OS type to the scenario’s need: deadlines → real-time; high volume and scheduled → batch; many users and shared resources → network OS; battery life and touch → mobile OS."),
    think([("Why is an online seat booking system an example of real-time transaction processing?", "Each booking must be processed immediately and the seat locked, so two customers cannot buy the same seat."),
           ("Why do mobile operating systems close background apps more aggressively than desktop ones?", "To save battery and memory: mobile devices have less power and RAM, so idle apps are paused or closed.")]),
)


# ---------- SW2 7.2.2 utilities ----------
SW2 = lesson("SW2", "7.2 Software", "Utility software",
    "explain the features and uses of file management, defragmentation, compression, package managers, protection and backup software.", spec("7.2.2"),
    p("Utility software helps look after the computer rather than doing a user’s task. Most operating systems include utilities, and others are installed separately."),
    table(["Utility", "What it does", "Why it matters"], [
        ["File management", "create, copy, move, rename, delete and search files and folders; manage permissions", "keeps data organised and findable"],
        ["Defragmenter", "rearranges the scattered parts of files on a hard disk so each file is stored together", "fewer head movements, faster reads on HDDs (not needed for SSDs)"],
        ["File compression", "makes files smaller (lossless ZIP, or lossy for media)", "saves storage and speeds up transfers"],
        ["Package manager", "installs, updates and removes software and its dependencies from trusted repositories (apt, winget, npm, pip)", "consistent, secure, repeatable installs and quick updates"],
        ["Protection software", "antivirus/anti-malware, firewalls, encryption tools", "stops, detects and removes threats; protects data"],
        ["Backup software", "copies data on a schedule (full, incremental, differential) and restores it", "recovery after failure, deletion or ransomware"],
    ], caption="Common utilities"),
    dA.backup_types(),
    cli(["sudo apt update", "sudo apt install nmap", "sudo apt upgrade", "winget install Python.Python.3.12", "winget upgrade --all"], "Package managers on Linux (apt) and Windows (winget)"),
    terms([("Utility", "software that maintains or protects the computer."), ("Fragmentation", "a file stored in pieces across a disk."), ("Dependency", "another package a program needs in order to run."), ("Incremental backup", "copies only data changed since the last backup.")]),
    think([("Why should you not defragment an SSD?", "SSDs have no moving head, so fragmentation does not slow them down, and extra writes shorten the SSD’s life."),
           ("Give one advantage of installing software with a package manager.", "It fetches the correct version and all its dependencies from a trusted source, and can update everything with one command.")]),
)


# ---------- SW3 7.2.3 code development tools ----------
def ide_fig():
    s = SVG(760, 260, "Parts of an integrated development environment")
    s.box(20, 20, 720, 220, fill="#f6f9fc", stroke="#6b7f90")
    s.box(20, 20, 720, 30, fill="#eef0f3", stroke="#6b7f90", rx=0)
    s.text(40, 40, "▶ Run   ⏸ Debug   ⚙ Build", size=12, anchor="start")
    s.box(30, 60, 150, 170, "Project files", size=12, fill="white")
    s.box(190, 60, 360, 120, fill="white")
    for i, (ln, code) in enumerate([("1", "total = 0"), ("2", "for n in scores:"), ("3", "    total += n"), ("4", "print(total / len(scores))")]):
        s.text(205, 85 + i * 22, ln, size=12, color="#8aa5b8", anchor="start", mono=True)
        s.text(230, 85 + i * 22, code, size=13, anchor="start", mono=True, color=INK)
    s.circle(197, 125, 5, fill=WARN, stroke=WARN)
    s.text(470, 128, "← breakpoint", size=11, color=WARN)
    s.box(190, 188, 360, 42, "Debugger: total = 142, n = 71 (watch variables, step through)", size=11, fill="#fbf0dd")
    s.box(560, 60, 170, 170, fill="white")
    s.text(645, 82, "Screen designer", size=12, bold=True)
    s.box(580, 95, 130, 26, "Name: ______", size=11, rx=3)
    s.box(580, 130, 130, 26, "Score: ______", size=11, rx=3)
    s.box(610, 170, 70, 28, "Save", size=11, fill="#dcebf6", rx=4)
    return s.render("An IDE puts code editing, debugging and screen design tools in one program, speeding up development and making errors easier to find.")


def compile_fig():
    s = SVG(760, 200, "Compiler compared with interpreter")
    s.text(190, 26, "Compiler", size=15, bold=True)
    s.box(30, 45, 100, 44, "Source code", size=12)
    s.box(150, 45, 90, 44, "Compiler", size=12, fill="#dcebf6")
    s.box(260, 45, 100, 44, "Executable", size=12, fill="#e8f1e4")
    s.arrow(130, 67, 148, 67, width=1.6)
    s.arrow(240, 67, 258, 67, width=1.6)
    s.text(190, 120, "translates the whole program once, before it runs", size=12)
    s.text(190, 140, "fast to run; errors listed after compiling;", size=12)
    s.text(190, 158, "source code not needed to run it", size=12)
    s.text(570, 26, "Interpreter", size=15, bold=True)
    s.box(420, 45, 100, 44, "Source code", size=12)
    s.box(560, 45, 170, 44, "Interpreter runs it", "line by line", size=12, fill="#dcebf6")
    s.arrow(520, 67, 558, 67, width=1.6)
    s.text(570, 120, "translates and runs one line at a time", size=12)
    s.text(570, 140, "stops at the first error: easy to test and debug;", size=12)
    s.text(570, 158, "slower to run; needs the interpreter installed", size=12)
    return s.render("Both turn high-level code into something the processor can run; they differ in when the translation happens.")


SW3 = lesson("SW3", "7.2 Software", "Code development tools",
    "explain the features of IDEs (code editing, debugging, screen design), compilers and interpreters.", spec("7.2.3"),
    ide_fig(),
    table(["IDE tool", "Features", "Benefit"], [
        ["Code editing", "syntax highlighting, auto-complete, auto-indent, error underlining, find and replace, refactoring", "faster coding and fewer typing errors"],
        ["Debugging", "breakpoints, stepping line by line, watching variable values, call stack", "find logic errors by seeing exactly what the program does"],
        ["Screen design", "drag-and-drop layout of forms, buttons and text boxes", "build user interfaces quickly and consistently"],
        ["Build and run", "one click to compile/run, integrated terminal, version control", "quick testing and teamwork"],
    ], caption="Features of an integrated development environment"),
    compile_fig(),
    p("Some languages use both: Java and C# compile to an intermediate bytecode, which a virtual machine then runs. Python is usually interpreted, which makes it quick to try things out."),
    terms([("IDE", "integrated development environment: tools for writing, testing and debugging code in one program."), ("Breakpoint", "a marked line where the program pauses while debugging."), ("Compiler", "translates a whole program into machine code before it runs."), ("Interpreter", "translates and runs a program one line at a time.")]),
    think([("Why might a games studio compile its final game?", "Compiled code runs faster and players do not need the source code or an interpreter; it also protects the code from being easily read."),
           ("How does a breakpoint help find a logic error?", "The program pauses at that line so you can inspect variable values and step through, seeing where the values stop matching what you expected.")]),
)


# ---------- SW4 7.2.4 application software ----------
SW4 = lesson("SW4", "7.2 Software", "Application software",
    "explain the features and uses of word processors, spreadsheets, databases, email and project management software.", spec("7.2.4"),
    table(["Application", "Key features", "Business use"], [
        ["Word processor", "formatting, styles, templates, mail merge, track changes, comments", "letters, reports, policies, contracts"],
        ["Spreadsheet", "cells, formulas and functions, charts, sorting and filtering, what-if modelling", "budgets, invoices, sales analysis, forecasts"],
        ["Database", "tables, records and fields, relationships, queries, forms, reports, validation", "customer, stock, patient and student records"],
        ["Email", "send and receive messages and attachments, folders, contacts, calendar, rules", "communication with staff and customers"],
        ["Project management", "tasks, deadlines, Gantt charts, Kanban boards, resource allocation, progress tracking", "planning and tracking software projects and teamwork"],
    ], caption="Common application software"),
    real_world("a doctor’s surgery", "Reception uses a database for patient records and appointments, a spreadsheet to track monthly budgets, word processing for referral letters (often mail-merged from the database), email to communicate with the hospital, and project management software to plan a move to a new records system."),
    terms([("Application software", "programs that help users carry out tasks."), ("Relational database", "data stored in linked tables."), ("Mail merge", "combining a template with a list of data to create personalised documents."), ("Gantt chart", "a timeline showing tasks, durations and dependencies.")]),
    think([("Why would a business use a database rather than a spreadsheet for 50,000 customer records?", "Databases handle large volumes, link related tables, enforce validation, let many users work at once, and run complex queries quickly."),
           ("Name one feature of project management software that helps a team meet a deadline.", "A Gantt chart or Kanban board showing task dependencies and progress, so delays are spotted early.")]),
)

LESSONS = [NS, H1, H2, SW1, SW2, SW3, SW4]
