"""'From your lessons' enrichment for the Unit 2 Learn page: original text and diagrams covering topics taught in the
department's Unit 2 PowerPoints and notes (ports and connectors, servers, SAN/NAS, choosing hardware, mobile devices,
the kernel, OS networking and security, interfaces, open source, disk cache, number bases, Vigenère, VoIP, universal gates)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "deeper"))
from helpers import SVG, h3, p, ul, table, terms, worked, think, real_world, esc, INK, LINE, ARROW, ACCENT, WARN  # noqa

BLUE, AMBER, GREEN, RED, PURPLE = "#dcebf6", "#fbf0dd", "#e8f1e4", "#fbe3d4", "#f3e8f9"


def more(sid, *blocks):
    return (f'<section class="deeper more" aria-labelledby="more-{sid}"><h3 class="deeper-title" id="more-{sid}">From your lessons · {sid}</h3>'
            f'<p class="small">Extra detail from your teacher’s Unit 2 lessons. Practise it on the <a href="tasks.html">Diagram tasks</a> page.</p>{"".join(blocks)}</section>')


# ---------- A1 ----------
def kernel_fig():
    s = SVG(760, 230, "User, shell, kernel and hardware")
    layers = [("User", "you and your applications", "#ffffff"), ("Shell", "the interface: GUI, command line or menus", AMBER), ("Kernel", "the core of the OS: memory, CPU time, devices, files", BLUE), ("Hardware", "CPU, RAM, storage, ports, network card", GREEN)]
    for i, (a, b, f) in enumerate(layers):
        s.box(140 + i * 25, 15 + i * 52, 480 - i * 50, 44, f"{a}: {b}", size=13, fill=f, bold=(a == "Kernel"))
    s.arrow(110, 30, 110, 190, both=True, width=2)
    s.text(60, 112, "requests", size=12, color=ARROW)
    s.text(60, 128, "and results", size=12, color=ARROW)
    return s.render("Programs never talk to hardware directly: requests pass through the shell and kernel, which decides how hardware is used.")


A1 = more("A1",
    h3("Ports and connectors"),
    table(["Connector", "Where", "What it does"], [
        ["USB-A / USB-C", "external port", "data and power for keyboards, drives, phones; USB-C is reversible and can carry video and charging"],
        ["HDMI / DisplayPort", "external port", "digital video and audio to a monitor or TV"],
        ["VGA / DVI", "external port (older)", "video to monitors: VGA is analogue, DVI digital"],
        ["RJ45", "external port", "wired Ethernet network cable"],
        ["3.5 mm audio jack", "external port", "headphones, speakers, microphone"],
        ["24-pin ATX", "internal", "main power from the power supply to the motherboard (older boards used 20-pin)"],
        ["4/8-pin EPS (ATX12V)", "internal", "extra 12 V power for the CPU"],
        ["6/8-pin PCIe power", "internal", "extra power for a graphics card"],
        ["SATA data and SATA power", "internal", "connect hard drives, SSDs and optical drives"],
        ["Molex and Berg", "internal (legacy)", "older drive power; Berg was for floppy drives"],
        ["M.2 slot", "internal", "fast SSDs mounted straight onto the motherboard"],
    ], caption="Common ports and connectors"),
    h3("Servers and their functions"),
    table(["Server", "Function"], [
        ["File server", "stores shared files and controls who can open them"],
        ["Print server", "queues print jobs and shares printers between users"],
        ["Web server", "stores web pages and sends them to browsers"],
        ["Mail server", "sends, receives and stores email"],
        ["Database server", "runs a database that many users query at once"],
        ["Application server", "runs shared software for clients"],
        ["Authentication / directory server", "checks usernames and passwords and holds user accounts"],
        ["DHCP / DNS server", "gives devices IP addresses / turns names into IP addresses"],
    ], caption="A server provides services to many clients at the same time"),
    table(["", "RAID", "NAS", "SAN"], [
        ["What it is", "several disks combined inside one system", "a storage device on the network", "a separate high-speed network of storage"],
        ["Used for", "speed, capacity or fault tolerance (RAID 0, 1, 5)", "shared files, backups and media in homes and small businesses", "servers in data centres needing fast shared block storage"],
        ["Accessed by", "the one computer or server it is in", "many devices using file protocols (SMB, NFS)", "servers, as if the storage were their own disks"],
    ], caption="RAID, NAS and SAN compared (a NAS often uses RAID inside)"),
    h3("Factors affecting the choice of hardware"),
    table(["Factor", "Question to ask"], [
        ["User experience", "is it easy to use, fast enough and reliable for this user?"],
        ["Needs of the user", "what tasks: office work, gaming, video editing, field work?"],
        ["Performance", "CPU, RAM, storage speed and graphics for the workload"],
        ["Cost", "purchase, running and maintenance costs against the budget"],
        ["Compatibility", "does it work with existing software, peripherals and the network?"],
        ["Efficiency", "power use, heat and battery life"],
        ["Implementation", "time, training and disruption to install it"],
        ["Productivity", "will it help people work faster or better?"],
        ["Security", "encryption, biometrics, ability to lock or wipe it"],
        ["Portability and connectivity", "size, weight, Wi-Fi, 4G/5G, ports"],
    ], caption="Use these factors to justify a recommendation in exam answers"),
    table(["Mobile device", "Typical features", "Typical use"], [
        ["Smartphone", "touchscreen, cellular data, GPS, cameras, many sensors", "calls, apps, navigation, payments"],
        ["Tablet", "larger touchscreen, long battery, often Wi-Fi only", "reading, media, sales demonstrations, note taking"],
        ["Laptop", "keyboard, more powerful CPU and storage, full OS", "office work, programming, editing"],
        ["Sat-nav", "GPS receiver, maps stored, dashboard mount", "route guidance in vehicles"],
        ["Wearable", "tiny screen, sensors (heart rate), Bluetooth to a phone", "fitness tracking, notifications"],
    ], caption="Characteristics of mobile devices"),
    terms([("Connector", "the physical plug or socket that joins a cable to a device."), ("Server", "a computer that provides services to many clients."), ("NAS", "network attached storage: a storage device shared over the network."), ("SAN", "storage area network: a dedicated fast network of shared storage for servers.")]),
    think([("Why does a graphics card need its own PCIe power connector?", "Powerful GPUs need more power than the PCIe slot can supply, so extra 12 V power comes directly from the power supply."),
           ("A small office wants shared storage for six staff and nightly backups. NAS or SAN?", "NAS: it is cheaper, easy to set up and shares files over the existing network; a SAN is for data centres.")]),
)

A2 = more("A2",
    kernel_fig(),
    table(["Kernel job", "What it does"], [
        ["Program execution", "loads programs and passes their requests to the CPU as system calls"],
        ["Interrupt handling", "decides which signals need immediate attention and makes the CPU deal with them first"],
        ["Memory management", "gives each program its own memory and stops programs overwriting each other"],
        ["Process scheduling", "shares CPU time between running programs"],
        ["Device management", "controls hardware through device drivers"],
        ["File management", "organises files and folders and controls access to them"],
    ], caption="The role of the kernel in controlling and managing system components and tasks"),
    table(["", "At home", "In an organisation"], [
        ["Network type", "usually peer-to-peer: no servers; share the internet and a printer", "client–server: servers control resources and user accounts"],
        ["How the OS manages security", "power-on or login passwords, Wi-Fi (WPA2/WPA3) password, passwords on shared folders", "users authenticate at login; access rights decide which files, printers and systems each user may reach; audit logs"],
        ["Sharing resources", "simple file and printer sharing", "print queues, network storage shown as normal drives, managed LAN and WAN access"],
    ], caption="The operating system’s role in networking and security"),
    table(["Interface", "Good for", "Limitations"], [
        ["Graphical (GUI)", "most users; touchscreens; visual tasks", "uses more memory and processing power"],
        ["Command line (CLI)", "technicians, servers, automation with scripts", "commands must be learned; easy to make mistakes"],
        ["Menu-based", "kiosks, ATMs, simple devices", "only the choices on the menu"],
        ["Natural language / voice", "hands-free use, accessibility", "can misunderstand; needs a quiet place"],
    ], caption="Factors affecting the choice of user interface: the user, the device, the task and the environment"),
    p("When <strong>choosing an operating system</strong>, consider: the hardware it must run on, the software and devices it must support, the users’ skills, cost and licensing, security and updates, and whether it needs to be a network, real-time or mobile OS."),
    table(["", "Open source", "Proprietary (closed source)"], [
        ["Source code", "published; anyone can study, change and share it", "kept secret by the company"],
        ["Cost", "often free to use", "licence fees"],
        ["Support", "community forums, or paid support from companies", "official support from the vendor"],
        ["Implications", "can be customised; bugs can be found and fixed by many people; may need in-house skills", "consistent, supported product; locked to the vendor’s decisions and prices"],
        ["Examples", "Linux, Android (base), LibreOffice, Firefox", "Windows, macOS, Microsoft 365"],
    ], caption="Principles and implications of open source software"),
    h3("Disk cache"),
    p("A <strong>disk cache</strong> keeps recently and frequently used data from a drive in fast memory (part of RAM, or a chip on the drive). The next time that data is needed it is read from the cache instead of the slower drive. Writes can also be collected in the cache and written to the drive later, which is faster but risks losing data if the power fails before they are saved."),
    terms([("Kernel", "the core of the operating system that manages hardware, memory and CPU time."), ("Shell", "the part of the OS the user interacts with: a GUI or command line."), ("Open source", "software whose source code is published so others can study, change and share it."), ("Disk cache", "fast memory holding recently used disk data to speed up access.")]),
    think([("Why does a server often use a command-line interface?", "It needs fewer resources than a GUI, and administrators can automate tasks with scripts and manage it remotely."),
           ("Give one benefit and one drawback of open source for a school.", "Benefit: free to install on every PC. Drawback: staff may need extra training, and support relies on the community or a paid partner.")]),
)


# ---------- C1 ----------
C1 = more("C1",
    table(["Base", "Digits allowed", "Example", "Used for"], [
        ["Binary (base 2)", "0 1", "1011", "how computers store everything"],
        ["Octal (base 8)", "0–7", "17", "older systems; Linux file permissions (chmod 755)"],
        ["Denary / decimal (base 10)", "0–9", "985", "everyday counting"],
        ["Hexadecimal (base 16)", "0–9, A–F", "3F", "colour codes, MAC addresses, memory addresses"],
    ], caption="Recognising a number base from its digits"),
    p("A number can only belong to a base if every digit is smaller than the base. <code>1,0</code> could be any base; <code>7</code> could be octal, denary or hex but not binary; <code>8</code> rules out octal; any letter A–F means hexadecimal."),
    worked("octal to binary and denary", ["Each octal digit is exactly 3 bits: 7 = 111, 5 = 101.", "So octal 75 = 111 101 in binary.", "In denary: 7 × 8 + 5 = 61."], "Octal 75 = binary 111101 = denary 61"),
    think([("Which bases could the digits 1, 9, 8, 5 belong to?", "Denary and hexadecimal only: 9 and 8 are too big for binary and octal."),
           ("Why is hex used for colour codes like #FF8800?", "Each pair of hex digits is one byte (0–255) for red, green or blue, written in just two characters.")]),
)


# ---------- E1 ----------
def vigenere_fig():
    s = SVG(760, 200, "Vigenère cipher worked example")
    rows = [("Plaintext", list("HELLO"), AMBER), ("Key (repeated)", list("KEYKE"), BLUE), ("Shift", ["10", "4", "24", "10", "4"], "#ffffff"), ("Ciphertext", list("RIJVS"), RED)]
    for r, (lab, vals, f) in enumerate(rows):
        y = 20 + r * 42
        s.text(130, y + 24, lab, size=13, anchor="end", bold=True)
        for c, v in enumerate(vals):
            s.box(150 + c * 70, y, 60, 34, v, size=15, fill=f, rx=4)
    s.text(560, 60, "Each letter shifts by the", size=12, anchor="start", color=ACCENT)
    s.text(560, 78, "position of the key letter", size=12, anchor="start", color=ACCENT)
    s.text(560, 96, "(A = 0, B = 1 … Z = 25).", size=12, anchor="start", color=ACCENT)
    s.text(560, 132, "The two Ls become J and V:", size=12, anchor="start")
    s.text(560, 150, "same letter, different code.", size=12, anchor="start")
    return s.render("Unlike a Caesar cipher, the shift changes with every letter, so letter-frequency analysis is much harder.")


E1 = more("E1",
    h3("The Vigenère cipher"),
    vigenere_fig(),
    p("To decrypt, subtract the key shifts instead of adding them. The longer and more random the key, the harder it is to break; a key as long as the message that is never reused is called a <strong>one-time pad</strong>."),
    h3("Voice over IP (VoIP)"),
    table(["Step", "What happens"], [
        ["1 Digitise", "the caller’s voice is sampled and converted to digital data"],
        ["2 Compress", "a codec compresses the audio to reduce bandwidth (quality may drop slightly)"],
        ["3 Packetise", "the data is split into packets with headers and sent across the internet"],
        ["4 Reassemble", "the receiver puts packets in order and the codec turns them back into sound"],
    ], caption="How a VoIP call works"),
    table(["Benefits", "Drawbacks"], [["cheap or free calls, even internationally; use any internet-connected device; video and messaging in one app", "needs a reliable connection; latency, jitter and packet loss cause echo or gaps; no service in a power or internet cut; calls can be intercepted unless encrypted"]], caption="VoIP for organisations"),
    terms([("Vigenère cipher", "a substitution cipher using a keyword so each letter has a different shift."), ("Codec", "hardware or software that compresses and decompresses audio or video."), ("Jitter", "variation in the delay between packets, causing choppy sound."), ("VoIP", "voice over internet protocol: phone calls sent as data packets.")]),
    think([("Encrypt CAT with the key BB.", "Shift each letter by 1 (B = 1): C→D, A→B, T→U, giving DBU."),
           ("Why does VoIP use UDP-style delivery instead of re-sending lost packets?", "A re-sent packet would arrive too late to be useful in a live conversation, so a small gap is better than a delay.")]),
)


# ---------- F1 ----------
F1 = more("F1",
    table(["Gate", "Output is 1 when…", "Notes"], [
        ["NAND", "NOT both inputs are 1", "a universal gate: any circuit can be built from NAND gates alone"],
        ["NOR", "both inputs are 0", "also universal"],
        ["XOR", "the inputs are different", "used in half adders (sum bit) and parity checking"],
        ["XNOR", "the inputs are the same", "equality checking"],
    ], caption="More gates from your logic booklet"),
    p("<strong>Three-state (tri-state) logic</strong> adds a third output state, <em>high impedance</em>, where the output is effectively disconnected. It lets many devices share one bus wire: only the device that is enabled drives the bus, and the others ‘let go’."),
    think([("Why can a NAND gate be used to make a NOT gate?", "Join both inputs together: if the input is 1, NAND gives 0; if it is 0, NAND gives 1, which is NOT."),
           ("Why is XOR used for the sum bit in a half adder?", "1 + 0 and 0 + 1 give sum 1, while 0 + 0 and 1 + 1 give sum 0 (with a carry), which is exactly XOR.")]),
)

SECTIONS = {"A1": A1, "A2": A2, "C1": C1, "E1": E1, "F1": F1}
