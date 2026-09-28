from helpers import *


def vn_harvard():
    s = SVG(760, 290, "Von Neumann and Harvard architectures compared")
    s.text(190, 30, "Von Neumann", size=15, bold=True)
    s.box(40, 50, 300, 90, fill="#dcebf6")
    s.text(190, 72, "CPU", size=14, bold=True)
    s.box(60, 85, 80, 40, "Control unit", size=11)
    s.box(150, 85, 80, 40, "ALU", size=12)
    s.box(240, 85, 80, 40, "Registers", size=11)
    s.arrow(190, 140, 190, 190, both=True, label="one shared bus", lx=55, ly=4)
    s.box(80, 190, 220, 60, "Memory", "instructions AND data", size=14)
    s.text(190, 278, "Only one fetch at a time: the von Neumann bottleneck", size=12, color=WARN)
    s.text(570, 30, "Harvard", size=15, bold=True)
    s.box(420, 50, 300, 90, fill="#dcebf6")
    s.text(570, 72, "CPU", size=14, bold=True)
    s.box(440, 85, 80, 40, "Control unit", size=11)
    s.box(530, 85, 80, 40, "ALU", size=12)
    s.box(620, 85, 80, 40, "Registers", size=11)
    s.arrow(480, 140, 480, 190, both=True, label="bus 1", lx=-25, ly=4)
    s.arrow(660, 140, 660, 190, both=True, label="bus 2", lx=28, ly=4)
    s.box(410, 190, 140, 60, "Instruction", "memory", size=13)
    s.box(590, 190, 140, 60, "Data", "memory", size=13)
    s.text(570, 278, "Instruction and data fetched at the same time", size=12, color=ACCENT)
    return s.render("Von Neumann (left) shares one memory and bus. Harvard (right) keeps instructions and data apart, each with its own bus.")


def cluster():
    s = SVG(760, 300, "A computer cluster sharing one big job")
    s.box(290, 20, 180, 56, "Head node", "splits job, collects results", size=14, fill="#fbf0dd", stroke="#b58a3a")
    s.box(310, 110, 140, 40, "Network switch", size=13, fill="#eef0f3")
    s.arrow(380, 76, 380, 108, both=True)
    for i in range(5):
        x = 40 + i * 145
        s.box(x, 200, 120, 60, f"Node {i + 1}", "CPU + own RAM", size=13, fill="white")
        s.arrow(380, 150, x + 60, 198, both=True, width=1.8)
    s.text(380, 288, "Each node works on its own part of the job, e.g. one region of a weather map.", size=12)
    return s.render("A cluster: many ordinary computers (nodes) linked by a fast network act as one powerful system. If one node fails, the others continue.")


def uma_numa():
    s = SVG(760, 300, "Uniform and non-uniform memory access")
    s.text(180, 28, "UMA", size=15, bold=True)
    for i in range(3):
        s.box(40 + i * 100, 45, 80, 40, f"CPU {i + 1}", size=13)
        s.arrow(80 + i * 100, 85, 80 + i * 100, 125, both=True, width=1.8)
    s.line(40, 128, 320, 128, width=4)
    s.arrow(180, 130, 180, 170, both=True)
    s.box(70, 170, 220, 56, "Shared RAM", "same distance for every CPU", size=13)
    s.text(180, 262, "Simple and fair, but the shared bus gets", size=12)
    s.text(180, 279, "crowded as more CPUs are added", size=12)
    s.text(570, 28, "NUMA", size=15, bold=True)
    for i, x in enumerate([410, 600]):
        s.box(x, 45, 120, 150, fill="#f6f9fc", dash=True)
        s.box(x + 20, 60, 80, 40, f"CPU {i + 1}", size=13)
        s.arrow(x + 60, 100, x + 60, 135, both=True, width=1.8, color=ACCENT)
        s.box(x + 10, 135, 100, 44, "Local RAM", size=12)
    s.arrow(530, 80, 598, 80, both=True, color=WARN)
    s.text(565, 72, "slower", size=11, color=WARN)
    s.text(565, 225, "Each CPU reaches its own RAM quickly (green),", size=12)
    s.text(565, 242, "and other CPUs’ RAM more slowly (orange).", size=12)
    s.text(565, 262, "Scales to many CPUs if data is kept local.", size=12)
    return s.render("UMA: every processor has equal access to one memory. NUMA: each processor has fast local memory and slower access to the rest.")


def emulation():
    s = SVG(760, 200, "Layers when a program runs in an emulator")
    s.box(30, 30, 180, 50, "Old game or app", "written for CPU family X", size=13, fill="#fbf0dd")
    s.arrow(210, 55, 288, 55, label="X instructions", ly=22, lsize=11)
    s.box(290, 15, 180, 80, fill="#dcebf6")
    s.text(380, 40, "Emulator", size=14, bold=True)
    s.text(380, 60, "translates X → Y and", size=11)
    s.text(380, 76, "imitates the old hardware", size=11)
    s.arrow(470, 55, 548, 55, label="Y instructions", ly=22, lsize=11)
    s.box(550, 30, 180, 50, "Host computer", "CPU family Y", size=13, fill="#e8f1e4")
    s.text(380, 135, "Translation is extra work, so an emulated program usually runs more slowly than on real hardware.", size=12)
    s.text(380, 158, "Uses: running old software on new machines, testing phone apps on a PC, preserving retro games.", size=12)
    return s.render("Emulation makes one computer behave like another, so software written for a different instruction set can still run.")


B1 = deeper("B1",
    h3("Two ways to connect the CPU to memory"),
    vn_harvard(),
    p("In the <strong>stored program</strong> model, the program is held in memory just like data, so a computer can switch jobs simply by loading a different program. Early computers were rewired or re-switched for each new task. In a <strong>von Neumann</strong> machine, instructions and data share one memory and one bus, which is simple and flexible. In a <strong>Harvard</strong> machine they are separate, so the next instruction can be fetched while data is being read. Small controllers such as those in microwaves, washing machines and Arduino-style boards often use Harvard designs; modern PC processors mix both, with separate instruction and data <em>caches</em> in front of one main memory."),
    h3("Many processors working together"),
    cluster(),
    p("A <strong>cluster</strong> links many computers, called <strong>nodes</strong>, with a fast network. Big jobs such as weather forecasting, film rendering or searching huge datasets are split into parts that run at the same time. Clusters can grow by adding nodes, and they keep working if one node fails. The cost is the network: sending data between nodes is far slower than inside one computer, so the job must split into parts that do not need to talk to each other often."),
    uma_numa(),
    h3("Emulation"),
    emulation(),
    table(["Architecture", "Good choice when…", "Watch out for…"], [
        ["Von Neumann with UMA", "a general-purpose PC or laptop with a few cores", "the shared bus limiting speed"],
        ["Harvard", "a fixed program in a small embedded controller that needs predictable speed", "less flexible use of memory"],
        ["NUMA server", "one large machine with many processors, e.g. a big database", "software must keep data near the processor using it"],
        ["Cluster", "a very large job that splits into independent parts, or a service that must stay up", "network delay, cost, space, power and cooling"],
    ], caption="Factors affecting the choice of architecture"),
    terms([
        ("Stored program", "a design where the program is kept in memory and can be changed like data."),
        ("Bus", "a set of parallel wires carrying addresses, data or control signals between parts."),
        ("Von Neumann bottleneck", "the delay caused by instructions and data sharing one path to memory."),
        ("Node", "one computer in a cluster."),
        ("NUMA", "non-uniform memory access: memory near a processor is faster for it than distant memory."),
        ("Emulator", "software that imitates a different computer, so its programs can run."),
    ]),
    think([
        ("Why do many microcontrollers use a Harvard architecture?", "Their program is fixed in ROM/flash and never changes, and they need fast, predictable timing. Separate buses let an instruction and data be fetched at the same time."),
        ("A NUMA server runs slowly because one program’s data sits in another processor’s memory. Suggest a fix.", "Have the operating system run the program on the processor next to its data, or move the data into that processor’s local memory."),
        ("Why is emulation usually slower than running on real hardware?", "Every instruction written for the old processor has to be translated into instructions for the new one, which is extra work."),
    ]),
    real_world("weather forecasting", "National weather services run their forecasts on supercomputers built as clusters of thousands of nodes. The atmosphere is divided into a 3D grid, and each node calculates its own region, exchanging only the edge values with its neighbours."),
)


def cycle():
    s = SVG(760, 250, "The fetch–decode–execute cycle")
    s.circle(380, 125, 95, fill="#f6f9fc")
    pts = [(380, 30, "FETCH"), (560, 180, "DECODE"), (200, 180, "EXECUTE")]
    for x, y, a in pts:
        s.box(x - 75, y - 25, 150, 50, a, size=14, fill="#dcebf6", bold=True)
    s.text(610, 42, "copy the next instruction", size=12, anchor="start")
    s.text(610, 58, "from memory into the CPU", size=12, anchor="start")
    s.text(640, 232, "control unit works out what it means", size=12)
    s.text(150, 232, "the ALU calculates, data moves, or the PC jumps", size=12)
    s.arrow(455, 40, 540, 150, width=2)
    s.arrow(485, 190, 275, 190, width=2)
    s.arrow(215, 150, 305, 40, width=2)
    s.text(380, 130, "repeats\nbillions of\ntimes a second", size=12, color=ACCENT)
    return s.render("The instruction cycle. The clock keeps every step in time; each tick moves the cycle on.")


def pipeline():
    s = SVG(760, 345, "Instructions overlapping in a three-stage pipeline")
    stages = {"F": "#dcebf6", "D": "#e8f1e4", "E": "#fbf0dd"}
    s.text(60, 40, "Clock cycle →", size=12, anchor="start")
    for c in range(8):
        s.text(190 + c * 72, 40, str(c + 1), size=13, bold=True)
    for i in range(6):
        y = 55 + i * 40
        s.text(60, y + 24, f"Instruction {i + 1}", size=12, anchor="start")
        for k, st in enumerate("FDE"):
            s.box(156 + (i + k) * 72, y, 68, 32, {"F": "Fetch", "D": "Decode", "E": "Execute"}[st], size=11, fill=stages[st], rx=4)
    s.text(380, 312, "Without a pipeline: 6 instructions × 3 steps = 18 cycles. With it: 3 + (6 − 1) = 8 cycles.", size=12, color=ACCENT)
    s.text(380, 332, "A branch can make the fetched instructions wrong, so they are thrown away (a pipeline flush).", size=12, color=WARN)
    return s.render("Pipelining. While one instruction executes, the next is being decoded and the one after is being fetched.")


def multicore():
    s = SVG(760, 260, "Inside a four-core processor chip")
    s.box(90, 20, 580, 220, fill="#eef3f8", stroke="#6b7f90")
    s.text(380, 42, "One CPU chip", size=13, bold=True)
    for i in range(4):
        x = 110 + i * 140
        s.box(x, 55, 120, 90, fill="white")
        s.text(x + 60, 78, f"Core {i + 1}", size=13, bold=True)
        s.box(x + 10, 88, 100, 22, "L1 cache", size=11, fill="#dcebf6", rx=4)
        s.box(x + 10, 115, 100, 22, "L2 cache", size=11, fill="#cfe3f4", rx=4)
        s.arrow(x + 60, 145, x + 60, 163, width=1.5)
    s.box(110, 165, 540, 30, "Shared L3 cache", size=12, fill="#b9d6ef", rx=4)
    s.box(260, 203, 240, 28, "Memory controller → RAM", size=12, fill="white", rx=4)
    return s.render("A multi-core CPU. Each core runs its own instructions; small private caches are fastest, and a larger L3 cache is shared.")


B2 = deeper("B2",
    h3("The instruction cycle in more detail"),
    cycle(),
    p("Every program, from a game to a spreadsheet, is turned into millions of simple machine instructions such as <em>load a number</em>, <em>add</em>, <em>compare</em> and <em>jump</em>. The list of instructions a processor understands is its <strong>instruction set</strong>. A 3 GHz clock ticks three billion times a second, so one tick lasts about 0.33 nanoseconds."),
    table(["", "RISC (reduced instruction set)", "CISC (complex instruction set)"], [
        ["Instructions", "few, simple, mostly one clock cycle each", "many, some doing several steps in one instruction"],
        ["Programs", "need more instructions", "need fewer instructions"],
        ["Chip", "simpler, uses less power and heat", "more complex, traditionally more power"],
        ["Typical use", "phones, tablets, many newer laptops (e.g. ARM)", "most desktop PCs and many servers (x86)"],
    ], caption="Two approaches to instruction sets"),
    h3("Pipelining"),
    pipeline(),
    h3("Cores, threads and cache"),
    multicore(),
    p("A <strong>multi-core</strong> processor has several complete processing units on one chip; <strong>multi-processing</strong> means using more than one of them at the same time. A program can be written as several <strong>threads</strong>, flows of work that the OS can run on different cores. Some cores can also run two threads at once, switching to the second thread whenever the first is waiting for memory. <strong>Cache</strong> keeps copies of recently used instructions and data close to the core: a <em>cache hit</em> is fast; a <em>cache miss</em> means a much slower trip to RAM."),
    table(["Factor", "Unit", "Effect on speed"], [
        ["Clock speed", "GHz", "more cycles per second, but more heat and power"],
        ["Number of cores", "cores", "more work at once, if the software uses threads"],
        ["Cache size", "MB", "fewer slow trips to RAM"],
        ["Manufacturing process", "nm (nanometres)", "smaller transistors: more of them per chip, less power, less heat"],
        ["Core design / generation", "product family", "newer designs do more work per clock cycle"],
    ], caption="CPU performance factors"),
    worked("Why 4 cores is not 4 times faster", [
        "A video export takes 12 seconds on one core. Three-quarters of the work (9 s) can be split between cores; one-quarter (3 s) must run in order.",
        "On 4 cores, the parallel part takes 9 ÷ 4 = 2.25 s, but the sequential part still takes 3 s.",
        "Total = 3 + 2.25 = 5.25 s. The speed-up is 12 ÷ 5.25 ≈ 2.3 times, not 4 times.",
        "Adding even more cores gets closer and closer to 3 s but can never beat it, because the sequential part cannot be shared.",
    ], "Extra cores only speed up the part of a job that can run in parallel."),
    table(["CPU type", "Designed for", "Typical features"], [
        ["Embedded", "one fixed job inside a device (washing machine, car engine)", "low cost and power; often has its own memory and inputs/outputs on the chip"],
        ["Mobile", "phones, tablets, thin laptops", "battery life first: a mix of fast and efficient cores in a SoC, slows down when hot"],
        ["Microcomputer (PC)", "general desktop and laptop use", "high single-core speed, several cores, upgradable, fan cooling"],
        ["Server", "many users and requests, all day", "many cores, huge caches, support for lots of RAM, error-correcting memory, reliability features"],
    ], caption="Different CPU architectures for different jobs"),
    terms([
        ("Instruction set", "all the machine instructions a processor can carry out."),
        ("Pipelining", "overlapping the fetch, decode and execute stages of different instructions."),
        ("Cache hit / miss", "whether the data needed was already in cache (hit) or had to come from RAM (miss)."),
        ("Thread", "a separate flow of instructions within a program that can run alongside others."),
        ("Clock speed", "how many cycles the CPU completes each second, measured in GHz."),
    ]),
    think([
        ("Why might a phone run a demanding game more slowly after 10 minutes?", "The chip heats up, so it lowers its clock speed (throttles) to protect itself and save battery."),
        ("Doubling the clock speed does not always halve the time a program takes. Why not?", "The CPU may be waiting for memory, storage or the network. A faster clock does not make those parts faster."),
        ("Which would help a web server handling thousands of small requests more: a faster clock or more cores?", "More cores, because each request is independent and can be handled in parallel."),
    ]),
)


def cpu_registers():
    s = SVG(760, 320, "Registers inside the CPU and the buses to memory")
    s.box(20, 20, 470, 280, fill="#eef3f8", stroke="#6b7f90")
    s.text(255, 42, "CPU", size=15, bold=True)
    regs = [("PC", "program counter:\nnext instruction address", 40, 60), ("CIR", "current instruction\nregister", 260, 60),
            ("MAR", "memory address\nregister", 40, 150), ("MDR", "memory data\nregister", 260, 150),
            ("ACC", "accumulator:\nresults from the ALU", 40, 230)]
    for name, desc, x, y in regs:
        s.box(x, y, 200, 62 if y < 230 else 56, fill="white")
        s.text(x + 14, y + 24, name, size=15, anchor="start", bold=True)
        s.text(x + 70, y + 22, desc, size=11, anchor="start")
    s.box(260, 230, 95, 56, "ALU", size=14, fill="#dcebf6")
    s.box(365, 230, 110, 56, "Control\nunit", size=13, fill="#dcebf6")
    s.box(590, 70, 150, 200, fill="white")
    s.text(665, 92, "Main memory", size=14, bold=True)
    s.grid(605, 105, 2, 5, 60, 30, [["Addr", "Holds"], ["0", "LOAD 20"], ["1", "ADD 21"], ["20", "7"], ["21", "5"]], size=11)
    s.arrow(490, 120, 588, 120, label="address bus (one way)", ly=-8, lsize=11)
    s.arrow(490, 190, 588, 190, both=True, label="data bus", ly=-8, lsize=11, color=ACCENT)
    s.arrow(490, 258, 588, 258, both=True, label="control bus", ly=-8, lsize=11, color=WARN)
    return s.render("The special registers. The MAR sends addresses out; the MDR holds whatever comes back from, or goes to, memory.")


def interrupt_flow():
    s = SVG(760, 260, "How the CPU handles an interrupt")
    steps = ["Finish the current\ninstruction", "Any interrupt\nwaiting?", "Save PC and\nregisters (stack)", "Run the interrupt\nservice routine", "Restore registers,\ncarry on"]
    xs = [20, 170, 320, 470, 620]
    for i, (x, t) in enumerate(zip(xs, steps)):
        if i == 1:
            s.poly([(x + 60, 60), (x + 125, 105), (x + 60, 150), (x - 5, 105)], fill="#fbf0dd", stroke="#b58a3a")
            s.text(x + 60, 100, t, size=12)
        else:
            s.box(x, 75, 125, 60, t, size=12, fill="white")
        if i < 4:
            s.arrow(x + (125 if i != 1 else 125), 105, xs[i + 1] - 2, 105, label="yes" if i == 1 else "", ly=-8, lsize=11)
    s.add(f'<path d="M230 150 L230 200 L80 200 L80 137" stroke="{ARROW}" stroke-width="2.5" fill="none"/>')
    s.poly([(80, 137), (75, 147), (85, 147)], fill=ARROW, stroke=ARROW, width=1)
    s.text(160, 218, "no: fetch the next instruction as normal", size=11)
    s.text(380, 245, "Higher-priority interrupts (e.g. power failing) are handled before lower ones (e.g. a key press).", size=12, color=ACCENT)
    return s.render("Interrupt handling. The CPU checks for interrupts between instructions, so it never abandons one halfway.")


B3 = deeper("B3",
    h3("Where the registers sit"),
    cpu_registers(),
    p("Registers are the fastest storage in the whole computer because they are part of the CPU itself, but there are only a few of them. <strong>General-purpose registers</strong> hold values a program is working on, such as a loop counter. <strong>Special registers</strong> have one fixed job in the instruction cycle. A 64-bit processor has 64-bit registers, so it can move or add 8 bytes in one step."),
    worked("Tracing the registers for a tiny program", [
        "Memory holds: address 0 = LOAD 20, address 1 = ADD 21, address 2 = STORE 22, address 20 = 7, address 21 = 5.",
        "Fetch 1: PC = 0 is copied to the MAR. The instruction LOAD 20 arrives in the MDR, is copied to the CIR, and the PC becomes 1.",
        "Execute 1: 20 goes to the MAR, the value 7 comes back into the MDR and is copied to the ACC. ACC = 7.",
        "Fetch 2: MAR = 1, CIR = ADD 21, PC = 2. Execute 2: MAR = 21, MDR = 5, the ALU adds 7 + 5. ACC = 12.",
        "Fetch 3: MAR = 2, CIR = STORE 22, PC = 3. Execute 3: MAR = 22, MDR = 12, and 12 is written into address 22.",
    ], "The PC always moves on during the fetch, before the instruction is executed."),
    table(["Step", "PC", "MAR", "MDR", "CIR", "ACC"], [
        ["Fetch LOAD 20", "0 → 1", "0", "LOAD 20", "LOAD 20", "–"],
        ["Execute", "1", "20", "7", "LOAD 20", "7"],
        ["Fetch ADD 21", "1 → 2", "1", "ADD 21", "ADD 21", "7"],
        ["Execute", "2", "21", "5", "ADD 21", "12"],
        ["Fetch STORE 22", "2 → 3", "2", "STORE 22", "STORE 22", "12"],
        ["Execute", "3", "22", "12", "STORE 22", "12"],
    ], caption="Trace table for the three-instruction program"),
    h3("Interrupts"),
    interrupt_flow(),
    table(["Interrupt source", "Example", "Why it is needed"], [
        ["Hardware", "key pressed, mouse moved, network packet arrived, disc read finished", "devices get attention only when they need it, instead of the CPU checking them constantly"],
        ["Timer", "the OS clock ticks every few milliseconds", "lets the scheduler swap between programs for multitasking"],
        ["Software", "a program asks the OS to open a file (a system call)", "programs must ask the kernel to use hardware"],
        ["Error", "divide by zero, or an attempt to use protected memory", "the OS can stop the faulty program safely"],
    ], caption="Where interrupts come from"),
    terms([
        ("Program counter (PC)", "holds the address of the next instruction to fetch."),
        ("MAR", "holds the address of the memory location being read or written."),
        ("MDR", "holds the data or instruction just read from, or about to be written to, memory."),
        ("CIR", "holds the instruction currently being decoded and executed."),
        ("Accumulator", "holds the result of the last calculation by the ALU."),
        ("Interrupt service routine", "the code that runs to deal with a particular interrupt."),
    ]),
    think([
        ("Why must the PC and registers be saved before an interrupt is handled?", "The interrupt routine will use the registers too. Saving them means the original program can carry on exactly where it stopped, as if nothing happened."),
        ("In the trace, why does the MAR hold 20 during the first execute step?", "LOAD 20 needs the value stored at address 20, so that address goes to the MAR to read it from memory."),
        ("What would happen if a JUMP 0 instruction was executed?", "The PC would be set to 0, so the next fetch would start the program again from the beginning."),
    ]),
)

SECTIONS = {"B1": B1, "B2": B2, "B3": B3}
