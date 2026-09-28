from helpers import *


def motherboard():
    s = SVG(760, 430, "Labelled top-down view of a desktop motherboard")
    s.box(150, 40, 440, 350, fill="#e9f2e6", stroke="#5b8a4f", rx=6)
    s.text(370, 32, "Motherboard (the main circuit board)", size=14, bold=True)
    # CPU and cooler
    s.box(200, 80, 110, 110, "CPU", "under the cooler", fill="#fff", stroke="#7a5c2e")
    s.add('<circle cx="255" cy="135" r="38" fill="none" stroke="#7a5c2e" stroke-width="1.5" stroke-dasharray="4 3"/>')
    # RAM slots
    for i in range(4):
        s.add(f'<rect x="{335 + i * 16}" y="70" width="10" height="150" rx="2" fill="#cfe3f4" stroke="{LINE}" stroke-width="1.5"/>')
    # PCIe slots and GPU
    s.add(f'<rect x="190" y="250" width="300" height="14" rx="2" fill="#fff" stroke="{LINE}" stroke-width="1.5"/>')
    s.add(f'<rect x="190" y="290" width="300" height="14" rx="2" fill="#fff" stroke="{LINE}" stroke-width="1.5"/>')
    s.add(f'<rect x="200" y="210" width="90" height="24" rx="3" fill="#dfe9f5" stroke="{LINE}" stroke-width="1.5"/>')
    s.text(245, 227, "M.2 SSD", size=11)
    # chipset, SATA, 24-pin, battery, rear I/O
    s.box(420, 320, 60, 44, "Chipset", size=11, fill="#fff")
    for i in range(4):
        s.add(f'<rect x="{510 + (i % 2) * 22}" y="{300 + (i // 2) * 22}" width="18" height="16" fill="#fff" stroke="{LINE}" stroke-width="1.2"/>')
    s.add(f'<rect x="555" y="90" width="18" height="100" rx="2" fill="#fff" stroke="{LINE}" stroke-width="1.5"/>')
    s.add(f'<circle cx="330" cy="345" r="12" fill="#fff" stroke="{LINE}" stroke-width="1.5"/>')
    s.add(f'<rect x="150" y="60" width="26" height="170" fill="#dfe9f5" stroke="{LINE}" stroke-width="1.5"/>')
    # labels with leader lines
    lab = [
        (70, 90, 176, 110, "Rear ports:\nUSB, RJ45,\nHDMI, audio"),
        (70, 170, 200, 150, "CPU socket:\nruns program\ninstructions"),
        (70, 260, 190, 257, "PCIe x16 slot:\ngraphics card"),
        (70, 330, 200, 222, "M.2 slot:\nfast NVMe SSD"),
        (670, 80, 385, 90, "RAM slots:\nworking memory\n(volatile)"),
        (670, 170, 573, 140, "24-pin power\nfrom the PSU"),
        (670, 280, 532, 310, "SATA ports:\nHDD / SSD /\noptical drives"),
        (670, 360, 480, 342, "Chipset: routes\ndata between\nparts"),
        (400, 412, 330, 357, "CMOS battery keeps the clock and firmware settings"),
    ]
    for tx, ty, px, py, t in lab:
        s.line(tx + (40 if tx < 150 else -40 if tx > 600 else 0), ty - 4 if tx != 400 else ty - 14, px, py, color="#8aa5b8", width=1.2)
        s.text(tx, ty, t, size=12)
    return s.render("A desktop motherboard (simplified). Parts plug into standard slots, which is why desktops are easy to upgrade and repair.")


def phone():
    s = SVG(760, 340, "Exploded view of the layers inside a smartphone")
    layers = [
        ("Cover glass + touch digitiser", "input: senses touch", "#eaf4fb"),
        ("OLED display panel", "output: pixels make light", "#e3eefa"),
        ("Logic board", "SoC, RAM and NAND flash storage", "#e8f1e4"),
        ("Battery", "lithium-ion: limits run time", "#fbf0dd"),
        ("Back case", "cameras, antennas, charging coil", "#eef0f3"),
    ]
    for i, (a, b, f) in enumerate(layers):
        x, y = 60 + i * 26, 30 + i * 58
        s.poly([(x, y + 20), (x + 230, y), (x + 290, y + 22), (x + 60, y + 42)], fill=f)
        s.text(x + 330, y + 18, a, size=14, anchor="start", bold=True)
        s.text(x + 330, y + 36, b, size=12, anchor="start")
    s.box(580, 120, 170, 120, fill="white")
    s.text(665, 140, "System on a Chip", size=13, bold=True)
    for j, t in enumerate(["CPU cores (fast + efficient)", "GPU (graphics)", "NPU (AI tasks)", "Image processor", "Cellular modem (4G/5G)"]):
        s.text(590, 162 + j * 16, "• " + t, size=11, anchor="start")
    s.arrow(530, 175, 576, 175, label="", color="#8aa5b8", width=1.5)
    return s.render("Inside a smartphone. A System on a Chip (SoC) puts the CPU, GPU and other processors on one chip to save space and battery.")


def server_rack():
    s = SVG(760, 380, "A server rack with redundant parts")
    s.box(250, 20, 260, 340, fill="#2b3a48", stroke="#1b2733", rx=6)
    rows = [("Network switch", "#cfe3f4"), ("Server 1", "#e6eef6"), ("Server 2", "#e6eef6"), ("Server 3", "#e6eef6"), ("Storage array (RAID)", "#e8f1e4"), ("Backup unit", "#eef0f3"), ("UPS: battery power", "#fbf0dd")]
    for i, (t, f) in enumerate(rows):
        y = 34 + i * 46
        s.box(265, y, 230, 36, "" if t.startswith("Server") else t, fill=f, stroke="#6b7f90", size=13)
        if t.startswith("Server"):
            s.text(275, y + 23, t, size=13, anchor="start")
            for k in range(4):
                s.add(f'<rect x="{395 + k * 22}" y="{y + 8}" width="16" height="20" rx="2" fill="#fff" stroke="#6b7f90"/>')
    notes = [
        (40, 110, "Two power supplies\nper server (A + B):\none can fail safely"),
        (40, 220, "Hot-swap drive bays:\nreplace a failed disk\nwithout switching off"),
        (560, 90, "Two network links\nto the switch, so one\ncable fault is survivable"),
        (560, 250, "UPS keeps servers\nrunning long enough\nto shut down cleanly"),
    ]
    for x, y, t in notes:
        s.text(x + 90, y, t, size=12)
    s.arrow(215, 110, 262, 95, color="#8aa5b8", width=1.5)
    s.arrow(215, 222, 390, 130, color="#8aa5b8", width=1.5)
    s.arrow(560, 95, 498, 60, color="#8aa5b8", width=1.5)
    s.arrow(560, 255, 498, 330, color="#8aa5b8", width=1.5)
    return s.render("A small server rack. Servers use redundant (duplicated) parts because many people depend on them at once.")


def hierarchy():
    s = SVG(760, 330, "The memory and storage hierarchy")
    levels = [("Registers", "bytes · inside the CPU"), ("Cache", "MB · on the CPU chip"), ("RAM", "GB · volatile working memory"), ("SSD", "hundreds of GB–TB · no moving parts"), ("HDD", "TB · spinning platters"), ("Cloud / archive", "unlimited · over the network")]
    n = len(levels)
    for i, (a, b) in enumerate(levels):
        top, bot = 20 + i * 48, 20 + (i + 1) * 48
        half_t, half_b = 40 + i * 55, 40 + (i + 1) * 55
        shade = ["#cfe3f4", "#d7e8f6", "#dfedf8", "#e6f1f9", "#edf5fb", "#f4f9fc"][i]
        s.poly([(260 - half_t, top), (260 + half_t, top), (260 + half_b, bot), (260 - half_b, bot)], fill=shade)
        s.text(260, top + 30, a, size=14, bold=True)
        s.text(600, top + 30, b, size=12)
    s.arrow(40, 290, 40, 30, color=ACCENT, label="")
    s.text(40, 310, "faster, costs more per GB", size=12, color=ACCENT)
    s.arrow(705, 30, 705, 290, color=WARN)
    s.text(690, 310, "bigger, cheaper per GB", size=12, color=WARN)
    return s.render("The memory hierarchy. Each level is slower but larger and cheaper than the one above, so computers copy the data they need upwards.")


def hdd_ssd():
    s = SVG(760, 260, "Hard disc drive compared with solid state drive")
    s.text(190, 30, "Hard disc drive (HDD)", size=15, bold=True)
    s.circle(160, 140, 85, fill="#eef0f3")
    s.circle(160, 140, 55, fill="#f6f7f9")
    s.circle(160, 140, 10, fill="#9aa7b3")
    s.line(300, 60, 190, 125, color="#6b7f90", width=6)
    s.circle(300, 60, 10, fill="#9aa7b3")
    s.text(190, 250, "Head must move to the track, then wait for it to spin round", size=12)
    s.text(560, 30, "Solid state drive (SSD)", size=15, bold=True)
    s.box(430, 55, 260, 160, fill="#e8f1e4", stroke="#5b8a4f")
    s.box(450, 75, 70, 50, "Controller", size=11)
    for k in range(4):
        s.box(540 + (k % 2) * 70, 75 + (k // 2) * 65, 60, 50, "NAND", size=11, fill="#fff")
    s.box(450, 140, 70, 50, "Cache", size=11)
    s.text(560, 250, "Any location can be read directly: no moving parts", size=12)
    return s.render("An HDD has a seek time because the head and platter must move. An SSD reads flash memory electronically, so it is faster, quieter and shock-resistant.")


def raid():
    s = SVG(760, 300, "How RAID 0, 1 and 5 place data across drives")

    def drive(x, y, blocks, label):
        s.box(x, y, 64, 170, fill="#f6f9fc")
        for i, b in enumerate(blocks):
            f = "#fbe3d4" if b.startswith("P") else "#dcebf6"
            s.box(x + 7, y + 10 + i * 38, 50, 30, b, size=12, fill=f, stroke=LINE, rx=4)
        s.text(x + 32, y + 190, label, size=12)
    s.text(110, 30, "RAID 0: striping", size=14, bold=True)
    drive(40, 50, ["A1", "A3", "A5", "A7"], "Disk 1")
    drive(120, 50, ["A2", "A4", "A6", "A8"], "Disk 2")
    s.text(110, 270, "fast, but no protection", size=12, color=WARN)
    s.text(355, 30, "RAID 1: mirroring", size=14, bold=True)
    drive(285, 50, ["A1", "A2", "A3", "A4"], "Disk 1")
    drive(365, 50, ["A1", "A2", "A3", "A4"], "Disk 2")
    s.text(355, 270, "survives one failure; half the space", size=12, color=ACCENT)
    s.text(610, 30, "RAID 5: striping + parity", size=14, bold=True)
    drive(505, 50, ["A1", "B1", "C1", "Pd"], "Disk 1")
    drive(580, 50, ["A2", "B2", "Pc", "D1"], "Disk 2")
    drive(655, 50, ["Pa", "Pb", "C2", "D2"], "Disk 3")
    s.text(620, 270, "survives one failure; parity is spread", size=12, color=ACCENT)
    return s.render("RAID levels. Orange blocks hold parity: extra data calculated from the other blocks, so a lost block can be rebuilt. RAID is not a backup.")


A1 = deeper("A1",
    h3("A closer look inside three kinds of computer"),
    p("Every computer has the same basic jobs (input, processing, storage, output), but designers package the parts very differently depending on the job. Compare the three diagrams below and look for what changes: how easy parts are to replace, how much power they use, and how much is duplicated."),
    motherboard(),
    p("A desktop PC is built from separate parts joined by the motherboard. Because the RAM, storage and graphics card sit in standard slots, a technician can upgrade or replace one part without replacing the whole computer. Laptops use similar parts, but many are soldered to the board to save space, so they are harder to upgrade."),
    phone(),
    p("A phone must be thin, light and last all day on a battery. Instead of many separate chips, it uses a <strong>System on a Chip (SoC)</strong> that combines the CPU cores, graphics, an AI engine and the mobile modem. Storage is <strong>NAND flash</strong>, which is non-volatile and has no moving parts. Sensors such as the accelerometer, gyroscope, GPS receiver and proximity sensor are inputs that most desktop PCs do not have."),
    server_rack(),
    p("A server provides a service to many client computers at once, so a failure affects everyone. That is why servers have lots of RAM, many CPU cores, and <strong>redundant</strong> parts: two power supplies, two network connections and drives in a RAID array, often all in a rack with an uninterruptible power supply (UPS)."),
    h3("Why speed depends on the slowest part"),
    hierarchy(),
    p("The CPU can only work on data that has been copied close to it. If data has to come from a slow hard disc or across a busy network, the fastest CPU still waits. This is called a <strong>bottleneck</strong>. When you recommend hardware, find the part that is holding the system back for that user, rather than simply choosing the biggest numbers."),
    hdd_ssd(),
    table(["Component", "Performance factor", "Unit", "Better when…"], [
        ["CPU", "Number of cores; clock speed; cache size", "cores; GHz; MB", "more cores help multitasking, higher GHz helps single tasks, bigger cache means fewer waits"],
        ["RAM", "Capacity; speed", "GB; MT/s", "enough GB to hold all open programs, otherwise the OS swaps to slow storage"],
        ["HDD", "Seek time; spindle speed; transfer rate", "ms; rpm; MB/s", "lower seek time, higher rpm and transfer rate"],
        ["SSD", "Read/write speed; interface (SATA or NVMe)", "MB/s", "NVMe SSDs can be several times faster than SATA ones"],
        ["Display", "Resolution; refresh rate; response time; brightness; contrast", "pixels; Hz; ms; cd/m²; ratio", "higher refresh and lower response time give smoother motion"],
        ["Printer", "Print speed; first page out; resolution; monthly duty cycle", "ppm; s; dpi; pages", "a higher duty cycle suits a busy office"],
    ], caption="Hardware performance factors to compare when choosing parts"),
    worked("Does a faster drive matter?", [
        "A video editor copies a 30 GB project (30,000 MB) to their computer.",
        "On a hard disc transferring at 150 MB/s: 30,000 ÷ 150 = 200 seconds (over 3 minutes).",
        "On an NVMe SSD transferring at 3,000 MB/s: 30,000 ÷ 3,000 = 10 seconds.",
        "For someone who opens large files many times a day, the SSD saves a lot of waiting. For someone who only writes documents, the difference is barely noticeable, so the money may be better spent elsewhere.",
    ], "Always link the specification to what the user actually does."),
    h3("Keeping data available: RAID and NAS"),
    raid(),
    p("A <strong>NAS</strong> (network attached storage) is a small computer whose only job is to share its drives over a network. It usually contains two or more drives in a RAID array, so that one drive failing does not lose the files. Remember the difference: RAID keeps a system <em>running</em> when a disc fails; a backup lets you <em>recover</em> from deletion, ransomware, theft or fire."),
    terms([
        ("Volatile", "loses its contents when the power is switched off (RAM)."),
        ("Non-volatile", "keeps its contents without power (SSD, HDD, flash memory)."),
        ("System on a Chip (SoC)", "a single chip containing the CPU, graphics and other processors, used in phones and tablets."),
        ("Seek time", "the time an HDD’s head takes to move to the right track."),
        ("Bottleneck", "the slowest part of a system, which limits the speed of the whole system."),
        ("Redundancy", "duplicate parts that take over when one fails."),
        ("UPS", "uninterruptible power supply: a battery that keeps equipment running during a power cut."),
        ("Parity (RAID)", "extra data calculated from other blocks, used to rebuild a failed drive’s data."),
    ]),
    think([
        ("Why does a tablet use flash storage rather than a hard disc?", "Flash has no moving parts, so it survives being dropped, uses less battery, is silent and fits in a thin case. It is also faster to access."),
        ("A shop’s till server has one power supply and one disc. Name two single points of failure and a fix for each.", "The power supply (fit two redundant PSUs, plus a UPS) and the disc (use RAID 1 or RAID 5, and keep a separate backup)."),
        ("A gamer buys a very powerful graphics card but keeps an old 60 Hz monitor. What limits the experience?", "The monitor. It can only show 60 frames per second, so frames the card draws above that are never seen. This is a bottleneck."),
    ]),
    real_world("a hospital", "A hospital’s patient-record servers sit in a rack with redundant power, RAID storage and a UPS backed by a generator, because doctors need the records at any hour. Nurses on wards use cheaper thin clients or tablets, because the data and processing live on the servers."),
)


def os_layers():
    s = SVG(760, 330, "Layers of software between the user and the hardware")
    s.box(60, 20, 640, 44, "User", size=15, fill="#fbf0dd", stroke="#b58a3a")
    s.box(60, 76, 640, 44, "Application software: browser, word processor, game", size=14, fill="white")
    s.box(60, 132, 640, 44, "Utility software: antivirus, backup, compression, disk tools", size=14, fill="white")
    s.box(60, 188, 640, 70, fill="#dcebf6")
    s.text(120, 210, "Operating system", size=14, anchor="start", bold=True)
    for i, t in enumerate(["Scheduler", "Memory manager", "File system", "Device drivers", "Networking + security"]):
        s.box(78 + i * 124, 220, 116, 30, t, size=11, fill="white")
    s.text(640, 210, "kernel", size=12, color=ARROW, italic=True)
    s.box(60, 270, 640, 44, "Hardware: CPU, RAM, storage, screen, network card", size=14, fill="#e8f1e4", stroke="#5b8a4f")
    return s.render("The operating system sits between programs and hardware. Programs ask the OS for resources rather than controlling the hardware directly.")


def timeslice():
    s = SVG(760, 230, "Timeline of multitasking with time slices and an interrupt")
    s.text(40, 30, "CPU time →", size=13, anchor="start")
    seq = [("A", 60), ("B", 60), ("C", 60), ("A", 60), ("INT", 40), ("B", 60), ("C", 60), ("A", 60)]
    x = 40
    colors = {"A": "#dcebf6", "B": "#e8f1e4", "C": "#fbf0dd", "INT": "#fbe3d4"}
    for t, w in seq:
        s.box(x, 50, w, 50, "Key" if t == "INT" else t, size=13, fill=colors[t], rx=3)
        x += w + 4
    s.arrow(308, 150, 308, 104, color=WARN)
    s.text(308, 170, "Keyboard interrupt: the kernel pauses the current task,", size=12, color=WARN)
    s.text(308, 187, "runs the keyboard handler, then carries on", size=12, color=WARN)
    s.text(40, 215, "A = music player  ·  B = word processor  ·  C = file download", size=12, anchor="start")
    return s.render("Multitasking: the scheduler gives each program a short time slice in turn, so fast that they all seem to run at once.")


def paging():
    s = SVG(760, 250, "Virtual memory: pages moved between RAM and storage")
    s.text(170, 30, "RAM (fast, limited)", size=14, bold=True)
    vals = [["P1", "P2", "Q1", "P3"], ["Q2", "R1", "", "P4"]]
    fills = [["#dcebf6", "#dcebf6", "#e8f1e4", "#dcebf6"], ["#e8f1e4", "#fbf0dd", "#fff", "#dcebf6"]]
    s.grid(50, 45, 4, 2, 60, 50, vals, fills)
    s.text(570, 30, "Page file on SSD/HDD (slow)", size=14, bold=True)
    s.grid(440, 45, 4, 2, 60, 50, [["R2", "Q3", "P5", ""], ["R3", "", "", ""]], [["#fbf0dd", "#e8f1e4", "#dcebf6", "#fff"], ["#fbf0dd", "#fff", "#fff", "#fff"]])
    s.arrow(300, 90, 435, 90, both=True, label="pages swapped", ly=-10)
    s.text(380, 200, "If too many pages keep swapping, the computer slows down badly (thrashing).", size=12)
    s.text(380, 222, "Adding RAM is the fix.", size=12)
    return s.render("Virtual memory lets programs use more memory than the RAM holds, by keeping less-used pages on storage.")


A2 = deeper("A2",
    h3("What the operating system is really doing"),
    os_layers(),
    p("The <strong>kernel</strong> is the part of the operating system that is always running. It decides which program uses the CPU next (<strong>scheduling</strong>), gives each program its own area of memory, reads and writes files through the <strong>file system</strong>, and talks to hardware through <strong>device drivers</strong>. Programs run in a restricted <strong>user mode</strong>; only the kernel runs in the privileged <strong>kernel mode</strong>, so a crashing app cannot take the whole computer down."),
    timeslice(),
    p("An <strong>interrupt</strong> is a signal that asks the CPU for attention: a key press, a network packet arriving, or a disc finishing a read. Instead of checking every device constantly, the CPU gets on with its work until an interrupt arrives. The kernel then runs the matching <strong>interrupt handler</strong> and returns to what it was doing."),
    paging(),
    table(["Type of OS", "What it does", "Example use"], [
        ["Real-time (RTOS)", "Guarantees a response within a fixed time limit", "car airbags, aircraft controls, factory robots"],
        ["Single-user, single-task", "One user runs one program at a time", "a simple embedded controller or early handheld device"],
        ["Single-user, multi-tasking", "One user runs many programs at once", "a laptop or phone"],
        ["Multi-user", "Many users share one computer’s resources at once, with separate accounts and permissions", "a school file server or a web server"],
    ], caption="Types of operating system"),
    table(["Interface", "Strengths", "Weaknesses", "Suits…"], [
        ["Graphical (GUI)", "easy to learn; visual; mouse or touch", "needs more memory and processing; slower for repetitive jobs", "most everyday users"],
        ["Command line (CLI)", "fast for experts; scripts can automate jobs; uses few resources", "commands must be remembered; easy to make serious mistakes", "technicians and servers"],
        ["Menu-based", "limited choices, so few errors; quick to train", "inflexible; deep menus can be slow", "tills, ATMs, kiosks, TVs"],
    ], caption="Choosing a user interface"),
    h3("Utility and application software"),
    p("<strong>Utility software</strong> looks after the computer itself: antivirus and firewalls protect it, backup tools copy data, disc tools clean up and (for hard discs) defragment, compression tools make files smaller and encryption tools protect data. <strong>Application software</strong> helps a person do a task, such as writing, calculating, editing video or booking appointments."),
    table(["", "Proprietary (closed source)", "Open source"], [
        ["Cost", "usually a licence fee", "usually free to use"],
        ["Source code", "secret; only the company can change it", "published; anyone can read, change and share it under its licence"],
        ["Support", "paid helpdesk and guaranteed updates", "community forums, or paid support from a third party"],
        ["Customising", "only the settings the company allows", "can be changed to fit exact needs, if you have the skills"],
    ], caption="Proprietary versus open-source software"),
    terms([
        ("Kernel", "the core of the OS that manages the CPU, memory, files and devices."),
        ("Device driver", "software that lets the OS control a particular piece of hardware."),
        ("Interrupt", "a signal that makes the CPU pause and deal with an event."),
        ("Scheduler", "the part of the kernel that decides which program runs next."),
        ("Virtual memory", "using storage as extra, slower memory when RAM is full."),
        ("File system", "the method the OS uses to organise files on a drive (e.g. NTFS, ext4, APFS)."),
    ]),
    think([
        ("Why can a single-user multitasking OS not be used to control a car’s airbag?", "It shares the CPU between many tasks and cannot guarantee how quickly it will respond. An airbag needs a real-time OS that always reacts within milliseconds."),
        ("A laptop with 4 GB of RAM becomes very slow when 20 browser tabs are open. Explain why.", "The tabs need more memory than the RAM holds, so the OS keeps swapping pages to the drive. Storage is far slower than RAM, so the computer spends its time moving pages instead of working."),
        ("Give one reason a technician might prefer a command line to a GUI.", "They can write a script that repeats a job, such as creating 200 user accounts, automatically and exactly the same way each time."),
    ]),
)


def pipeline_data():
    s = SVG(760, 210, "The stages of data processing from collection to report")
    steps = [("Collect", "sensors, forms,\nbarcodes, RFID"), ("Validate", "check it follows\nthe rules"), ("Sort", "put into a\nuseful order"), ("Aggregate", "combine into\ntotals/averages"), ("Analyse", "find patterns\nand trends"), ("Report", "charts, tables,\ndashboards")]
    for i, (a, b) in enumerate(steps):
        x = 20 + i * 123
        s.box(x, 40, 108, 50, a, size=14, fill="white", bold=True)
        s.text(x + 54, 115, b, size=11)
        if i < len(steps) - 1:
            s.arrow(x + 108, 65, x + 121, 65)
    s.text(380, 185, "Conversion can happen at any stage, e.g. analogue to digital, or CSV to a database table.", size=12)
    return s.render("A typical data processing pipeline. Each stage turns raw data into something more useful.")


def control_loop():
    s = SVG(760, 250, "A sensor-based control system for a greenhouse")
    s.box(20, 80, 120, 60, "Temperature\nsensor", size=13)
    s.box(170, 80, 100, 60, "ADC", "analogue → digital", size=13)
    s.box(300, 70, 150, 80, "Microcontroller", "compares with\ntarget 24 °C", size=13, fill="#dcebf6")
    s.box(480, 80, 110, 60, "Actuator", "heater / vent", size=13)
    s.box(620, 80, 120, 60, "Cloud\ndashboard", size=13, fill="#fbf0dd")
    s.arrow(140, 110, 168, 110)
    s.arrow(270, 110, 298, 110)
    s.arrow(450, 110, 478, 110)
    s.line(375, 70, 375, 45, dash=True)
    s.line(375, 45, 680, 45, dash=True)
    s.arrow(680, 45, 680, 78, dash=True)
    s.text(530, 37, "readings sent every minute", size=12, color=ARROW)
    s.add(f'<path d="M535 140 C535 215 80 215 80 142" stroke="{ACCENT}" stroke-width="2.5" fill="none" stroke-dasharray="6 4"/>')
    s.text(310, 225, "Feedback: the greenhouse temperature changes, and the sensor measures it again", size=12, color=ACCENT)
    return s.render("A control system. Sensors collect data, the program decides, actuators act, and feedback repeats the loop.")


def backup_types():
    s = SVG(760, 250, "Full, incremental and differential backups over a week")
    days = ["Sun", "Mon", "Tue", "Wed", "Thu"]
    for i, d in enumerate(days):
        s.text(210 + i * 110, 30, d, size=13, bold=True)
    s.text(20, 75, "Incremental", size=13, anchor="start", bold=True)
    s.text(20, 165, "Differential", size=13, anchor="start", bold=True)
    for i in range(5):
        full = i == 0
        s.box(165 + i * 110, 50, 90, 40, "Full" if full else "Mon" if i == 1 else f"{days[i]} only", size=12, fill="#dcebf6" if full else "#e8f1e4")
        w = 90
        s.box(165 + i * 110, 140, w, 40, "Full" if full else "Mon" if i == 1 else f"Mon→{days[i]}", size=12, fill="#dcebf6" if full else "#fbf0dd")
    s.text(380, 115, "Each backs up only what changed since the previous backup: quick to make, but a restore needs the full backup plus every incremental.", size=11)
    s.text(380, 205, "Each backs up everything changed since the full backup: grows each day, but a restore needs only the full backup plus the latest one.", size=11)
    s.text(380, 235, "3-2-1 rule: 3 copies of the data, on 2 kinds of media, with 1 copy off-site.", size=12, color=ACCENT, bold=True)
    return s.render("Backup strategies. The choice trades time and space for making backups against the time and effort to restore.")


A3 = deeper("A3",
    h3("From raw data to useful information"),
    pipeline_data(),
    p("Data is collected by <strong>hardware</strong> such as sensors, barcode scanners, RFID readers, card readers, cameras and keyboards, and by <strong>software</strong> such as online forms, apps that log activity, and systems that import data from other systems. Automatic collection (a sensor or scanner) is fast and avoids typing errors; manual collection (a person typing) is flexible but slower and error-prone."),
    control_loop(),
    table(["Validation check", "What it checks", "Example"], [
        ["Presence", "something has been entered", "email cannot be left blank"],
        ["Type", "the right kind of data", "age must be a whole number"],
        ["Range", "between set limits", "year group from 7 to 13"],
        ["Length", "the right number of characters", "UK mobile number has 11 digits"],
        ["Format", "matches a pattern", "postcode like LS1 4AP"],
        ["Lookup", "is in a list of allowed values", "course code exists in the course table"],
        ["Check digit", "a calculated digit matches", "the last digit of a barcode or ISBN"],
    ], caption="Common validation checks"),
    p("Validation stops <em>impossible</em> data, but it cannot tell whether data is <em>true</em>. <strong>Verification</strong> checks that data was copied correctly, for example by typing a password twice or by a person comparing the screen with the paper form."),
    worked("Multi-level sort, then aggregation", [
        "A school has attendance records with a tutor group, a surname and minutes late.",
        "Sort first by tutor group, then by surname within each group, so each tutor sees their own list in alphabetical order.",
        "Aggregate: total the minutes late for each tutor group, and count the students late more than 3 times.",
        "Analyse: compare this month’s totals with last month’s to spot a trend.",
        "Report: a bar chart per tutor group, sent automatically to heads of year every Monday.",
    ], "Sorting and aggregation turn thousands of rows into a few facts someone can act on."),
    h3("Data stored across more than one system"),
    table(["Impact", "Benefits", "Problems"], [
        ["Access", "staff at every site see the same records", "needs a working network; remote access must be secured"],
        ["Cost", "less duplicated hardware at each site", "links, cloud fees, licences and support"],
        ["Implementation", "one agreed system and format", "migrating and merging old data; training; downtime"],
        ["Productivity", "no phoning other sites or re-typing data", "slow if the link is slow; version conflicts"],
        ["Security", "central backups and consistent access control", "more ways in for attackers; one breach exposes more data"],
    ], caption="Using and storing data across multiple computer systems"),
    backup_types(),
    terms([
        ("Validation", "an automatic check that data is reasonable and follows the rules."),
        ("Verification", "a check that data has been entered or copied accurately."),
        ("Aggregation", "combining many records into totals, counts or averages."),
        ("Actuator", "a device that acts on the world, such as a motor, heater or valve."),
        ("ADC", "analogue-to-digital converter: turns a sensor’s continuous signal into numbers."),
        ("Incremental backup", "copies only the data changed since the last backup of any kind."),
    ]),
    think([
        ("Why is a range check on a date of birth not enough to stop mistakes?", "A date can be inside the range but still wrong, e.g. 12/03 typed instead of 03/12. Verification (such as confirming with the person) is needed as well."),
        ("On Friday the server fails. Using incremental backups, which backups are needed to restore it?", "Sunday’s full backup, then Monday’s, Tuesday’s, Wednesday’s and Thursday’s incrementals, applied in order."),
        ("Give one advantage of collecting data with a sensor instead of a person.", "It can take readings continuously, day and night, at exact intervals, without typing errors or getting tired."),
    ]),
)

SECTIONS = {"A1": A1, "A2": A2, "A3": A3}
