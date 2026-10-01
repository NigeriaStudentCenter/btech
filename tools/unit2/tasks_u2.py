"""Unit 2 interactive diagram tasks: the department's Word labelling tasks (motherboard ID, connectors, ports, mobile devices,
internal components, number bases) redone as original drawings with drop-down answers, plus CPU, logic gate and RAID tasks."""
import sys, pathlib, json, html
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "deeper"))
from helpers import SVG, LINE, ARROW, ACCENT  # noqa
from section_f import gate

esc = lambda t: html.escape(str(t), quote=True)
PCB, PCB2, SLOT, BLK = "#2f6d57", "#3b7f68", "#e9eef2", "#2b2f36"


def label(s, letter, x, y, tx, ty):
    """Leader line from a component point (x, y) to a lettered circle at (tx, ty)."""
    s.line(x, y, tx, ty, color="#17334b", width=1.8)
    s.add(f'<circle cx="{x}" cy="{y}" r="3.5" fill="#17334b"/>')
    s.circle(tx, ty, 15, fill="#fff3c4", stroke="#17334b", label=letter, size=15)


# ---------- 1 motherboard ----------
def motherboard():
    s = SVG(760, 600, "Motherboard identification diagram")
    s.box(90, 40, 560, 520, fill=PCB, stroke="#1d4a3a", rx=6)
    # back panel I/O
    s.box(110, 50, 230, 44, "back panel ports", size=11, fill="#c9d1d8", color="#2b2f36")
    # 4/8 pin EPS (A)
    s.box(400, 58, 60, 26, fill="#f4f1e8", rx=3)
    for k in range(4):
        for r in range(2):
            s.add(f'<rect x="{405 + k * 13}" y="{62 + r * 10}" width="9" height="7" fill="{BLK}"/>')
    # CPU socket (B)
    s.box(380, 130, 160, 160, fill="#cfd5db", stroke="#8a949e", rx=4)
    s.add('<rect x="400" y="150" width="120" height="120" fill="#b7bec6" stroke="#6e7881"/>')
    for k in range(10):
        s.add(f'<path d="M{404 + k * 12} 154 L{404 + k * 12} 266" stroke="#9aa3ac" stroke-width="1"/>')
    s.add('<path d="M540 140 L560 140 L560 280" stroke="#8a949e" stroke-width="4" fill="none"/>')
    # VRM capacitors
    for k in range(6):
        s.circle(372 - (k % 2) * 18, 140 + k * 26, 7, fill="#9aa3ac", stroke="#5d666e")
    # RAM slots (C)
    for k in range(4):
        x = 580 + k * 15
        s.add(f'<rect x="{x}" y="110" width="9" height="300" rx="2" fill="{["#e2b33a", "#3a6fb0"][k % 2]}" stroke="#2b2f36" stroke-width="1"/>')
    # 24-pin ATX (D)
    s.box(626, 430, 20, 100, fill="#f4f1e8", rx=2)
    for r in range(12):
        s.add(f'<rect x="629" y="{434 + r * 8}" width="6" height="5" fill="{BLK}"/><rect x="637" y="{434 + r * 8}" width="6" height="5" fill="{BLK}"/>')
    # SATA ports (E)
    for k in range(4):
        s.add(f'<path d="M{520 + (k % 2) * 40} {460 + (k // 2) * 34} h30 v18 h-22 v-6 h-8 Z" fill="#c63b3b" stroke="#7a1f1f"/>')
    # chipset with heatsink (F)
    s.box(400, 360, 90, 90, fill="#5d6a75", stroke="#2b2f36", rx=4)
    for k in range(7):
        s.add(f'<rect x="{406 + k * 12}" y="366" width="6" height="78" fill="#8796a3"/>')
    # CMOS battery (G)
    s.circle(320, 470, 26, fill="#d9dde1", stroke="#8a949e")
    s.text(320, 475, "CR2032", size=9, color="#5d666e")
    # BIOS/UEFI chip (H)
    s.box(190, 455, 44, 44, "BIOS", size=9, fill=BLK, color="#d9dde1", rx=2)
    # PCIe x1 (I)
    s.add(f'<rect x="120" y="390" width="70" height="12" rx="2" fill="{BLK}"/>')
    # PCIe x16 (J)
    s.add(f'<rect x="120" y="330" width="250" height="14" rx="2" fill="{BLK}"/><rect x="330" y="327" width="10" height="20" fill="#7d8790"/>')
    # M.2 (K)
    s.add(f'<rect x="130" y="250" width="200" height="22" rx="2" fill="{PCB2}" stroke="#bcd0c6" stroke-dasharray="4 3"/><rect x="130" y="252" width="12" height="18" fill="#c9d1d8"/>')
    s.text(240, 266, "M.2 2280", size=10, color="#dce8e2")
    for letter, (x, y), (tx, ty) in [("A", (430, 71), (360, 20)), ("B", (460, 210), (520, 20)), ("C", (608, 200), (720, 150)), ("D", (636, 480), (720, 470)),
                                     ("E", (550, 480), (560, 585)), ("F", (445, 405), (470, 585)), ("G", (320, 452), (330, 585)), ("H", (212, 462), (200, 585)),
                                     ("I", (150, 396), (40, 420)), ("J", (200, 337), (40, 337)), ("K", (180, 261), (40, 250))]:
        label(s, letter, x, y, tx, ty)
    return s.render("An original drawing of a desktop motherboard. Match each letter to the component.")


MOTHERBOARD = {"id": "mb", "title": "Task 1: Motherboard identification", "lesson": "A1",
    "intro": "Identify the components on the motherboard. (Redrawn from your teacher’s Motherboard ID task.)",
    "fig": motherboard, "options": ["CPU socket", "RAM (DIMM) slots", "24-pin ATX power connector", "4/8-pin CPU (EPS) power connector", "SATA ports", "Chipset with heatsink", "CMOS battery", "BIOS/UEFI chip", "PCIe x1 slot", "PCIe x16 slot (graphics card)", "M.2 slot (SSD)", "IDE connector", "Northbridge fan"],
    "items": [("A", "4/8-pin CPU (EPS) power connector"), ("B", "CPU socket"), ("C", "RAM (DIMM) slots"), ("D", "24-pin ATX power connector"), ("E", "SATA ports"), ("F", "Chipset with heatsink"),
              ("G", "CMOS battery"), ("H", "BIOS/UEFI chip"), ("I", "PCIe x1 slot"), ("J", "PCIe x16 slot (graphics card)"), ("K", "M.2 slot (SSD)")],
    "explain": "The CPU socket sits near the power regulators and its own 4/8-pin power; RAM slots are long and next to the CPU; the 24-pin ATX connector feeds the whole board; the long PCIe x16 slot takes a graphics card; the CMOS battery keeps the clock and BIOS settings when the PC is off."}


# ---------- 2 connectors ----------
def pins(s, x, y, cols, rows, w=10, h=8, gap=3, fill=BLK):
    for c in range(cols):
        for r in range(rows):
            s.add(f'<rect x="{x + c * (w + gap)}" y="{y + r * (h + gap)}" width="{w}" height="{h}" rx="1" fill="{fill}"/>')


def connectors():
    s = SVG(760, 380, "Seven computer connectors to identify")
    tiles = []
    for i in range(7):
        col, row = i % 4, i // 4
        x, y = 15 + col * 186, 15 + row * 185
        s.box(x, y, 172, 170, fill="#f6f9fc", stroke=LINE)
        s.circle(x + 18, y + 18, 13, fill="#fff3c4", stroke="#17334b", label=str(i + 1), size=13)
        tiles.append((x, y))
    # 1: 24-pin
    x, y = tiles[0]
    s.box(x + 56, y + 25, 60, 135, fill="#f4f1e8", rx=3)
    pins(s, x + 63, y + 31, 2, 12, w=20, h=7, gap=3)
    # 2: SATA power (15 pin, L key)
    x, y = tiles[1]
    s.add(f'<path d="M{x + 25} {y + 70} h122 v30 h-110 v-12 h-12 Z" fill="{BLK}"/>')
    for k in range(15):
        s.add(f'<rect x="{x + 42 + k * 7}" y="{y + 80}" width="3" height="12" fill="#e2b33a"/>')
    # 3: 6+2 PCIe
    x, y = tiles[2]
    s.box(x + 30, y + 60, 82, 56, fill=BLK, rx=3)
    pins(s, x + 36, y + 66, 3, 2, w=20, h=18, gap=6, fill="#6e7881")
    s.box(x + 118, y + 60, 30, 56, fill=BLK, rx=3)
    pins(s, x + 123, y + 66, 1, 2, w=20, h=18, gap=6, fill="#6e7881")
    # 4: Molex
    x, y = tiles[3]
    s.add(f'<path d="M{x + 30} {y + 65} h112 v34 l-10 12 h-92 l-10 -12 Z" fill="#f4f1e8" stroke="#a9a28c"/>')
    for k in range(4):
        s.circle(x + 50 + k * 24, y + 86, 8, fill=BLK)
    # 5: 20-pin
    x, y = tiles[4]
    s.box(x + 56, y + 30, 60, 115, fill="#f4f1e8", rx=3)
    pins(s, x + 63, y + 36, 2, 10, w=20, h=7, gap=3)
    # 6: Berg
    x, y = tiles[5]
    s.box(x + 56, y + 70, 60, 26, fill="#f4f1e8", rx=3)
    for k in range(4):
        s.add(f'<rect x="{x + 62 + k * 13}" y="{y + 78}" width="7" height="10" fill="{BLK}"/>')
    # 7: 4+4 EPS
    x, y = tiles[6]
    for h in range(2):
        s.box(x + 32 + h * 58, y + 55, 52, 56, fill=BLK, rx=3)
        pins(s, x + 37 + h * 58, y + 61, 2, 2, w=18, h=18, gap=6, fill="#6e7881")
    s.text(659, 270, "Count the pins", size=13, color=ACCENT)
    s.text(659, 290, "and look at the", size=13, color=ACCENT)
    s.text(659, 310, "shape of each plug.", size=13, color=ACCENT)
    return s.render("Original drawings of power connectors (not to scale). Match each number to its name.")


CONNECTORS = {"id": "con", "title": "Task 2: Power connectors", "lesson": "A1",
    "intro": "Match each connector to its name. (Redrawn from your teacher’s Connectors task.)",
    "fig": connectors, "options": ["24-pin slotted connector (ATX)", "20-pin slotted connector (older ATX)", "SATA keyed connector", "6/8-pin PCIe power connector", "Molex keyed connector", "Berg keyed connector", "4-pin to 8-pin auxiliary power connector (EPS)"],
    "items": [("1", "24-pin slotted connector (ATX)"), ("2", "SATA keyed connector"), ("3", "6/8-pin PCIe power connector"), ("4", "Molex keyed connector"), ("5", "20-pin slotted connector (older ATX)"), ("6", "Berg keyed connector"), ("7", "4-pin to 8-pin auxiliary power connector (EPS)")],
    "explain": "Count the pins: 24 and 20 are the main ATX power plugs; the 6+2 has a detachable 2-pin part for graphics cards; the 4+4 splits for CPU power; the flat L-shaped plug is SATA; Molex has four round pins; Berg is the small four-pin floppy plug."}


# ---------- 3 ports ----------
def ports():
    s = SVG(760, 330, "Ten ports to identify")
    tiles = []
    for i in range(10):
        col, row = i % 5, i // 5
        x, y = 15 + col * 148, 15 + row * 155
        s.box(x, y, 136, 140, fill="#d9dde1", stroke="#8a949e")
        s.circle(x + 16, y + 16, 12, fill="#fff3c4", stroke="#17334b", label=chr(65 + i), size=13)
        tiles.append((x + 68, y + 75))
    cx, cy = tiles[0]  # A HDMI
    s.add(f'<path d="M{cx - 40} {cy - 14} h80 v14 l-10 12 h-60 l-10 -12 Z" fill="{BLK}"/><rect x="{cx - 28}" y="{cy - 6}" width="56" height="6" fill="#e2b33a"/>')
    cx, cy = tiles[1]  # B USB-A
    s.box(cx - 32, cy - 14, 64, 28, fill="#ffffff", stroke=BLK, rx=2)
    s.add(f'<rect x="{cx - 26}" y="{cy - 8}" width="52" height="9" fill="#3a6fb0"/>')
    cx, cy = tiles[2]  # C RJ45
    s.add(f'<path d="M{cx - 28} {cy - 26} h56 v44 h-18 v8 h-20 v-8 h-18 Z" fill="{BLK}"/>')
    for k in range(8):
        s.add(f'<rect x="{cx - 21 + k * 5.5}" y="{cy - 22}" width="2.5" height="10" fill="#e2b33a"/>')
    cx, cy = tiles[3]  # D VGA
    s.add(f'<path d="M{cx - 42} {cy - 20} h84 l-8 40 h-68 Z" fill="#3a6fb0" stroke="#1d3d66"/>')
    for r, n in enumerate((5, 5, 5)):
        for k in range(n):
            s.circle(cx - 26 + k * 13 + (r % 2) * 6, cy - 10 + r * 11, 2.6, fill=BLK)
    cx, cy = tiles[4]  # E USB-C
    s.box(cx - 24, cy - 9, 48, 18, fill=BLK, rx=9)
    s.add(f'<rect x="{cx - 14}" y="{cy - 2}" width="28" height="4" rx="2" fill="#c9d1d8"/>')
    cx, cy = tiles[5]  # F 3.5mm audio
    for k, f in enumerate(["#7ac143", "#4aa3df", "#e98bb7"]):
        s.circle(cx - 36 + k * 36, cy, 13, fill=f, stroke="#555")
        s.circle(cx - 36 + k * 36, cy, 4, fill=BLK)
    cx, cy = tiles[6]  # G DisplayPort
    s.add(f'<path d="M{cx - 34} {cy - 13} h68 v26 h-58 l-10 -10 Z" fill="{BLK}"/><rect x="{cx - 24}" y="{cy - 4}" width="50" height="6" fill="#e2b33a"/>')
    cx, cy = tiles[7]  # H DVI
    s.box(cx - 50, cy - 18, 100, 36, fill="#ffffff", stroke=BLK, rx=4)
    for r in range(3):
        for k in range(8):
            s.add(f'<rect x="{cx - 44 + k * 8}" y="{cy - 12 + r * 9}" width="4" height="4" fill="{BLK}"/>')
    s.add(f'<rect x="{cx + 26}" y="{cy - 2}" width="16" height="3" fill="{BLK}"/>')
    cx, cy = tiles[8]  # I PS/2
    s.circle(cx, cy, 26, fill="#8e6bbf", stroke="#4b3470")
    for k, (dx, dy) in enumerate([(-10, -8), (10, -8), (-14, 5), (14, 5), (-6, 14), (6, 14)]):
        s.circle(cx + dx, cy + dy, 2.6, fill=BLK)
    s.add(f'<rect x="{cx - 4}" y="{cy - 2}" width="8" height="8" fill="{BLK}"/>')
    cx, cy = tiles[9]  # J RJ11
    s.add(f'<path d="M{cx - 18} {cy - 18} h36 v30 h-12 v6 h-12 v-6 h-12 Z" fill="{BLK}"/>')
    for k in range(4):
        s.add(f'<rect x="{cx - 9 + k * 5.5}" y="{cy - 14}" width="2.5" height="9" fill="#e2b33a"/>')
    return s.render("Original drawings of common ports (not to scale). Match each letter to the port.")


PORTS = {"id": "ports", "title": "Task 3: Ports", "lesson": "A1",
    "intro": "Name each port. (Based on your teacher’s ports chart.)",
    "fig": ports, "options": ["HDMI", "USB-A", "USB-C", "RJ45 (Ethernet)", "RJ11 (telephone/DSL)", "VGA", "DVI", "DisplayPort", "3.5 mm audio jacks", "PS/2 (keyboard/mouse)", "Thunderbolt 2"],
    "items": [("A", "HDMI"), ("B", "USB-A"), ("C", "RJ45 (Ethernet)"), ("D", "VGA"), ("E", "USB-C"), ("F", "3.5 mm audio jacks"), ("G", "DisplayPort"), ("H", "DVI"), ("I", "PS/2 (keyboard/mouse)"), ("J", "RJ11 (telephone/DSL)")],
    "explain": "HDMI is a wide trapezium; DisplayPort has one cut corner; VGA is a blue D-shape with 15 holes in three rows; DVI is wide with a flat blade; RJ45 is wider than RJ11 (8 contacts against 4); USB-C is a small oval that fits either way up."}


# ---------- 4 mobile devices ----------
def devices():
    s = SVG(760, 260, "Five mobile devices to identify")
    # A smartphone
    s.box(40, 70, 70, 130, fill=BLK, rx=12)
    s.box(46, 82, 58, 104, fill="#3a6fb0", rx=4)
    # B laptop
    s.box(150, 50, 200, 120, fill=BLK, rx=6)
    s.box(158, 58, 184, 104, fill="#4aa3df", rx=2)
    s.add('<path d="M130 172 h240 l-12 18 h-216 Z" fill="#5d666e"/>')
    # C tablet
    s.box(400, 55, 150, 140, fill=BLK, rx=10)
    s.box(410, 65, 130, 120, fill="#7ac143", rx=4)
    for k in range(3):
        for r in range(3):
            s.box(422 + k * 40, 78 + r * 36, 26, 26, fill="#ffffff", rx=5)
    # D sat-nav on mount
    s.box(580, 80, 120, 80, fill=BLK, rx=8)
    s.box(588, 88, 104, 64, fill="#e9eef2", rx=2)
    s.add('<path d="M596 140 Q620 110 640 120 T684 96" stroke="#e98b2c" stroke-width="4" fill="none"/>')
    s.add('<path d="M640 160 Q652 182 676 190" stroke="#5d666e" stroke-width="6" fill="none"/>')
    s.add('<ellipse cx="684" cy="196" rx="18" ry="8" fill="#9aa3ac" stroke="#5d666e"/>')
    s.text(640, 120, "▲", size=14, color="#c0392b")
    # E smartwatch
    for letter, x in [("A", 75), ("B", 250), ("C", 475), ("D", 640)]:
        s.circle(x, 228, 14, fill="#fff3c4", stroke="#17334b", label=letter, size=14)
    s.box(705, 150, 40, 50, fill=BLK, rx=10)
    s.box(710, 156, 30, 38, fill="#4aa3df", rx=6)
    s.add('<rect x="715" y="130" width="20" height="20" fill="#5d666e"/><rect x="715" y="200" width="20" height="22" fill="#5d666e"/>')
    s.circle(725, 240, 12, fill="#fff3c4", stroke="#17334b", label="E", size=13)
    return s.render("Five portable devices. Name each one, then match each feature to the device it best describes.")


DEVICES = {"id": "mob", "title": "Task 4: Mobile devices", "lesson": "A1",
    "intro": "Identify each mobile device, then match each feature to a device. (Based on your teacher’s mobile devices task.)",
    "fig": devices, "options": ["Smartphone", "Laptop", "Tablet", "Sat-nav", "Smartwatch (wearable)"],
    "items": [("A", "Smartphone"), ("B", "Laptop"), ("C", "Tablet"), ("D", "Sat-nav"), ("E", "Smartwatch (wearable)"),
              ("GPS receiver and stored maps, mounted on a dashboard", "Sat-nav"), ("Heart-rate sensor; shows notifications from a paired phone", "Smartwatch (wearable)"),
              ("Physical keyboard, full operating system, most processing power", "Laptop"), ("Large touchscreen, long battery life, often Wi-Fi only", "Tablet"), ("Cellular calls and data, cameras, many sensors, fits in a pocket", "Smartphone")],
    "explain": "Choose devices by their features: portability, screen size, input method, connectivity (Wi-Fi, 4G/5G, GPS, Bluetooth) and processing power."}


# ---------- 5 internal components ----------
COMPONENTS = {"id": "comp", "title": "Task 5: Purpose of internal components", "lesson": "A1",
    "intro": "Match each internal component to its purpose. (From your teacher’s ‘purpose, features and uses of internal components’ task.)",
    "fig": None, "options": ["Connects all components and lets them communicate", "Fetches, decodes and executes instructions", "Holds running programs and data temporarily (volatile)", "Keeps data permanently when the power is off", "Converts mains AC to the low DC voltages the components need",
                              "Connects external devices such as monitors and USB drives", "Removes heat so the CPU does not overheat or throttle", "Processes graphics and parallel calculations", "Holds start-up firmware that cannot be changed easily"],
    "items": [("Motherboard", "Connects all components and lets them communicate"), ("CPU", "Fetches, decodes and executes instructions"), ("RAM", "Holds running programs and data temporarily (volatile)"), ("Storage (HDD/SSD)", "Keeps data permanently when the power is off"),
              ("Power supply (PSU)", "Converts mains AC to the low DC voltages the components need"), ("Ports", "Connects external devices such as monitors and USB drives"), ("Fan and heat sink", "Removes heat so the CPU does not overheat or throttle"), ("GPU", "Processes graphics and parallel calculations"), ("ROM", "Holds start-up firmware that cannot be changed easily")],
    "explain": "For each component, exam answers need the purpose AND a feature (e.g. RAM: capacity in GB, speed; CPU: cores, clock speed, cache) AND a use."}


# ---------- 6 number bases (tick boxes) ----------
BASES = {"id": "bases", "title": "Task 6: Which number base?", "lesson": "C1", "type": "ticks",
    "intro": "Tick every number system each set of digits could belong to. (From your teacher’s number representation task.)",
    "fig": None, "cols": ["Binary", "Octal", "Decimal", "Hexadecimal"],
    "items": [("1, 2, 3", ["Octal", "Decimal", "Hexadecimal"]), ("1", ["Binary", "Octal", "Decimal", "Hexadecimal"]), ("1, 3, a", ["Hexadecimal"]), ("0, 3, 4, 8", ["Decimal", "Hexadecimal"]), ("1, 0", ["Binary", "Octal", "Decimal", "Hexadecimal"]),
              ("1, 9, 8, 5", ["Decimal", "Hexadecimal"]), ("a, b, c", ["Hexadecimal"]), ("7", ["Octal", "Decimal", "Hexadecimal"]), ("2", ["Octal", "Decimal", "Hexadecimal"])],
    "explain": "Every digit must be smaller than the base: binary uses 0–1, octal 0–7, decimal 0–9, hexadecimal 0–9 and A–F."}


# ---------- 7 CPU architecture ----------
def cpu():
    s = SVG(760, 430, "Von Neumann computer to label")
    s.box(30, 30, 420, 320, fill="#eef4fa", stroke="#245d83")
    s.text(240, 52, "CPU", size=15, bold=True)
    s.box(55, 64, 160, 64, fill="#ffffff")
    s.box(255, 64, 170, 64, fill="#ffffff")
    s.box(55, 165, 370, 140, fill="#ffffff")
    for k, (x, y) in enumerate([(70, 190), (250, 190), (70, 250), (250, 250)]):
        s.box(x, y, 160, 40, fill="#fbf0dd", rx=4)
    s.text(240, 186, "registers", size=11, color=ARROW)
    s.box(560, 60, 170, 250, fill="#e8f1e4", stroke="#5b8a4f")
    for k in range(8):
        s.add(f'<rect x="580" y="{80 + k * 26}" width="130" height="20" fill="#ffffff" stroke="#9cb79a"/>')
    for y, w in [(120, "#1f6fb2"), (180, "#c0392b"), (240, "#2f7d4f")]:
        s.add(f'<path d="M450 {y} H558" stroke="{w}" stroke-width="6"/>')
    s.box(250, 366, 260, 46, fill="#f3e8f9")
    for letter, (x, y), (tx, ty) in [("A", (135, 96), (135, 20)), ("B", (340, 96), (340, 20)), ("C", (150, 210), (20, 210)), ("D", (330, 206), (330, 148)),
                                     ("E", (150, 270), (20, 270)), ("F", (330, 274), (330, 328)), ("G", (505, 120), (505, 95)), ("H", (505, 180), (505, 158)), ("I", (505, 240), (505, 218)),
                                     ("J", (645, 180), (745, 180)), ("K", (380, 389), (545, 410))]:
        label(s, letter, x, y, tx, ty)
    return s.render("A simplified Von Neumann computer. Instructions and data share one memory and one set of buses.")


CPU = {"id": "cpu", "title": "Task 7: Inside a Von Neumann computer", "lesson": "B3",
    "intro": "Label the parts of the CPU, the buses and memory. (Based on your computer architecture lessons.)",
    "fig": cpu, "options": ["Control unit (CU)", "Arithmetic logic unit (ALU)", "Program counter (PC)", "Memory address register (MAR)", "Memory data register (MDR)", "Accumulator (ACC)", "Address bus", "Data bus", "Control bus", "Main memory (RAM)", "Input/output devices", "Cache", "Clock"],
    "items": [("A", "Control unit (CU)"), ("B", "Arithmetic logic unit (ALU)"), ("C", "Program counter (PC)"), ("D", "Memory address register (MAR)"), ("E", "Accumulator (ACC)"), ("F", "Memory data register (MDR)"),
              ("G", "Address bus"), ("H", "Data bus"), ("I", "Control bus"), ("J", "Main memory (RAM)"), ("K", "Input/output devices")],
    "explain": "The PC holds the address of the next instruction; it is copied to the MAR and sent along the address bus; the instruction or data returns on the data bus into the MDR; the CU decodes it and the ALU calculates, with results in the ACC."}


# ---------- 8 logic gates ----------
def gates():
    s = SVG(760, 220, "Six logic gate symbols to identify")
    for i, k in enumerate(["NAND", "OR", "XOR", "NOT", "AND", "NOR"]):
        col, row = i % 3, i // 3
        x, y = 20 + col * 248, 15 + row * 102
        s.box(x, y, 236, 92, fill="#ffffff", stroke=LINE)
        s.circle(x + 18, y + 18, 12, fill="#fff3c4", stroke="#17334b", label=str(i + 1), size=13)
        gate(s, k, x + 90, y + 26, inputs=1 if k == "NOT" else 2)
    return s.render("Standard logic gate symbols. A small circle (bubble) on the output means NOT.")


GATES = {"id": "gates", "title": "Task 8: Logic gate symbols", "lesson": "F1",
    "intro": "Name each logic gate. (From your logic booklet.)",
    "fig": gates, "options": ["AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR"],
    "items": [("1", "NAND"), ("2", "OR"), ("3", "XOR"), ("4", "NOT"), ("5", "AND"), ("6", "NOR")],
    "explain": "AND has a flat back and round front; OR has a curved back and pointed front; XOR has an extra curved line at the back; a bubble on the output turns AND into NAND and OR into NOR; NOT is a triangle with a bubble."}


# ---------- 9 RAID ----------
def raid():
    s = SVG(760, 230, "Three RAID arrays to identify")
    layouts = [[["A1", "A3", "A5"], ["A2", "A4", "A6"]], [["A1", "A2", "A3"], ["A1", "A2", "A3"]], [["A1", "B1", "Cp"], ["A2", "Bp", "C1"], ["Ap", "B2", "C2"]]]
    for i, disks in enumerate(layouts):
        x0 = 20 + i * 250
        s.box(x0, 15, 236, 200, fill="#ffffff", stroke=LINE)
        s.circle(x0 + 18, 33, 12, fill="#fff3c4", stroke="#17334b", label=chr(80 + i), size=13)
        w = 60
        start = x0 + (236 - len(disks) * (w + 10) + 10) / 2
        for d, blocks in enumerate(disks):
            x = start + d * (w + 10)
            s.box(x, 50, w, 130, fill="#f6f9fc", stroke="#245d83", rx=8)
            for b, t in enumerate(blocks):
                s.box(x + 6, 58 + b * 38, w - 12, 30, t, size=12, fill="#fbe3d4" if t.endswith("p") else "#dcebf6", rx=3)
            s.text(x + w / 2, 198, f"Disk {d + 1}", size=11)
    return s.render("Blocks marked ‘p’ hold parity calculated from the other blocks in the same row.")


RAID = {"id": "raid", "title": "Task 9: RAID levels", "lesson": "A1",
    "intro": "Identify the RAID level of each array, then choose the best description. (From your RAID and NAS lessons.)",
    "fig": raid, "options": ["RAID 0 (striping)", "RAID 1 (mirroring)", "RAID 5 (striping with distributed parity)", "RAID 10", "JBOD"],
    "items": [("P", "RAID 0 (striping)"), ("Q", "RAID 1 (mirroring)"), ("R", "RAID 5 (striping with distributed parity)")],
    "explain": "RAID 0 splits data across disks for speed but has no redundancy; RAID 1 writes identical copies so one disk can fail; RAID 5 spreads data and parity across three or more disks so any one disk can fail and be rebuilt."}

TASKS = [MOTHERBOARD, CONNECTORS, PORTS, DEVICES, COMPONENTS, BASES, CPU, GATES, RAID]


def render_task(t):
    fig = t["fig"]() if t.get("fig") else ""
    if t.get("type") == "ticks":
        head = "".join(f"<th>{esc(c)}</th>" for c in t["cols"])
        rows = "".join(f'<tr data-ans="{esc(json.dumps(ans))}"><th scope="row">{esc(q)}</th>' + "".join(f'<td><input type="checkbox" value="{esc(c)}" aria-label="{esc(q)}: {esc(c)}"></td>' for c in t["cols"]) + "</tr>" for q, ans in t["items"])
        body = f'<div class="tablewrap"><table class="ticks"><thead><tr><th>Digits</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
    else:
        opts = '<option value="">choose…</option>' + "".join(f'<option>{esc(o)}</option>' for o in t["options"])
        body = '<ol class="matches">' + "".join(f'<li data-ans="{esc(a)}"><span class="lab">{esc(q)}</span><select aria-label="{esc(q)}">{opts}</select><span class="mark" aria-live="polite"></span></li>' for q, a in t["items"]) + "</ol>"
    return (f'<section class="card task" id="{t["id"]}"><h2>{esc(t["title"])}</h2><p>{esc(t["intro"])}</p>{fig}{body}'
            f'<div class="tools"><button type="button" class="check">Check my answers</button><button type="button" class="show">Show answers</button><button type="button" class="reset">Reset</button></div>'
            f'<p class="score" role="status"></p><div class="explain" hidden><strong>Why:</strong> {esc(t["explain"])}</div>'
            f'<p class="small">Revise: <a href="learning.html#{t["lesson"]}">lesson {t["lesson"]}</a> · <a href="index.html?section={t["lesson"]}">ask the tutor about {t["lesson"]}</a></p></section>')


CSS = """.task figure{margin:14px 0;overflow-x:auto}.task figure svg{min-width:560px;width:100%;height:auto}
ol.matches{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(300px,100%),1fr));gap:8px 18px}
ol.matches li{display:flex;align-items:center;gap:8px;flex-wrap:wrap;padding:6px 8px;border-radius:8px;border:1px solid transparent}
ol.matches .lab{font-weight:700;min-width:28px}ol.matches li{min-width:0}ol.matches select{flex:1 1 160px;min-width:0;max-width:100%;width:100%;padding:6px;border:1px solid #899eb3;border-radius:6px;background:#fff;font:inherit;font-size:.95rem}
li.good,tr.good{background:#e6f4ec;border-color:#1d7a45!important}li.bad,tr.bad{background:#fdf0e1;border-color:#a3560b!important}.mark{font-weight:700}
table.ticks{border-collapse:collapse;width:100%}table.ticks th,table.ticks td{border:1px solid #c9d7e3;padding:6px;text-align:center}table.ticks input{width:1.2em;height:1.2em}
.score{font-weight:700;color:#163b62;min-height:1.4em}.explain{background:#eef6ff;border-radius:10px;padding:10px 14px;margin:8px 0}
#toc{columns:2}@media(max-width:640px){#toc{columns:1}ol.matches{grid-template-columns:minmax(0,1fr)}}
@media(max-width:600px){.task figcaption::before{content:"↔ Swipe the diagram to see all of it. ";font-weight:650;color:#20857b}}"""

JS = r"""(()=>{const KEY='unit2-tasks-v1';let s={};try{s=JSON.parse(localStorage.getItem(KEY)||'{}')||{}}catch{}
const save=()=>{try{localStorage.setItem(KEY,JSON.stringify(s))}catch{}};
document.querySelectorAll('section.task').forEach(sec=>{const id=sec.id,st=s[id]=s[id]||{};
 const sel=[...sec.querySelectorAll('select')],box=[...sec.querySelectorAll('input[type=checkbox]')];
 sel.forEach((x,i)=>{if(st['s'+i])x.value=st['s'+i];x.addEventListener('change',()=>{st['s'+i]=x.value;save();clear()})});
 box.forEach((x,i)=>{x.checked=!!st['b'+i];x.addEventListener('change',()=>{st['b'+i]=x.checked;save();clear()})});
 const items=()=>[...sec.querySelectorAll('[data-ans]')];
 const clear=()=>{items().forEach(it=>{it.classList.remove('good','bad');const m=it.querySelector('.mark');if(m)m.textContent=''});sec.querySelector('.score').textContent=''};
 const ok=it=>{if(it.tagName==='TR'){const want=JSON.parse(it.dataset.ans);const got=[...it.querySelectorAll('input')].filter(b=>b.checked).map(b=>b.value);return want.length===got.length&&want.every(w=>got.includes(w))}return it.querySelector('select').value===it.dataset.ans};
 sec.querySelector('.check').onclick=()=>{let n=0;const all=items();all.forEach(it=>{const g=ok(it);n+=g;it.classList.toggle('good',g);it.classList.toggle('bad',!g);const m=it.querySelector('.mark');if(m)m.textContent=g?'✓':'✗'});
  sec.querySelector('.score').textContent=`${n} / ${all.length} correct.`+(n===all.length?' Excellent!':' Try the red ones again.');sec.querySelector('.explain').hidden=false};
 sec.querySelector('.show').onclick=()=>{items().forEach(it=>{if(it.tagName==='TR'){const want=JSON.parse(it.dataset.ans);it.querySelectorAll('input').forEach(b=>b.checked=want.includes(b.value))}else it.querySelector('select').value=it.dataset.ans});sec.querySelector('.check').click()};
 sec.querySelector('.reset').onclick=()=>{sel.forEach(x=>x.value='');box.forEach(x=>x.checked=false);s[id]={};save();location.reload()};
});})();"""
