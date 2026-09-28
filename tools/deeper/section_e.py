from helpers import *


def channels():
    s = SVG(760, 270, "Simplex, half-duplex, full-duplex, point-to-point and multi-drop")
    rows = [("Simplex", "one way only", "TV broadcast, GPS", False, False), ("Half-duplex", "both ways, one at a time", "walkie-talkie", True, False), ("Full-duplex", "both ways at once", "phone call, Ethernet", True, True)]
    for i, (a, b, ex, back, both) in enumerate(rows):
        y = 30 + i * 50
        s.text(20, y + 20, a, size=14, anchor="start", bold=True)
        s.box(140, y, 60, 32, "A", size=13)
        s.box(330, y, 60, 32, "B", size=13)
        if both:
            s.arrow(202, y + 10, 328, y + 10)
            s.arrow(328, y + 23, 202, y + 23)
        elif back:
            s.arrow(202, y + 16, 328, y + 16, both=True, dash=True)
        else:
            s.arrow(202, y + 16, 328, y + 16)
        s.text(410, y + 14, b, size=12, anchor="start")
        s.text(410, y + 30, "e.g. " + ex, size=12, anchor="start", color=ACCENT)
    s.text(150, 188, "Point-to-point", size=14, bold=True)
    s.box(60, 220, 60, 32, "A", size=13)
    s.box(200, 220, 60, 32, "B", size=13)
    s.arrow(122, 236, 198, 236, both=True)
    s.text(550, 188, "Multi-drop: one shared line", size=14, bold=True)
    s.line(400, 236, 700, 236, width=3)
    for i, t in enumerate(["C", "S1", "S2", "S3"]):
        x = 410 + i * 80
        s.box(x, 250 - 45, 50, 26, t, size=12, fill="#dcebf6" if t == "C" else "white")
        s.line(x + 25, 231, x + 25, 236, width=2)
    return s.render("Channel types describe the direction of travel and how many devices share one link.")


def serial_parallel():
    s = SVG(760, 250, "Serial and parallel transmission of one byte")
    s.text(190, 28, "Parallel: 8 wires, all bits at once", size=14, bold=True)
    for i, b in enumerate("01000001"):
        y = 48 + i * 22
        s.line(80, y, 300, y, color="#b9c7d5", width=1.5)
        s.text(120 + (i % 3) * 18, y + 5, b, size=13, mono=True)
    s.text(190, 240, "Over distance the bits drift apart (skew)", size=12, color=WARN)
    s.text(570, 28, "Serial: 1 wire, bits one after another", size=14, bold=True)
    s.line(420, 120, 720, 120, color="#b9c7d5", width=1.5)
    for i, b in enumerate("01000001"):
        s.box(440 + i * 34, 104, 28, 32, b, size=13, fill="white", rx=3)
    s.arrow(440, 160, 700, 160, label="direction of travel", ly=18, lsize=11)
    s.text(570, 240, "Fewer wires, cheaper, and fast over long cables", size=12, color=ACCENT)
    return s.render("Parallel sends each bit on its own wire; serial sends the bits in sequence on one wire. USB, SATA and Ethernet are all serial.")


def async_sync():
    s = SVG(760, 200, "Asynchronous framing and synchronous transmission")
    s.text(20, 40, "Asynchronous", size=14, anchor="start", bold=True)
    cells = ["start 0"] + list("01000001") + ["stop 1"]
    x = 150
    for c in cells:
        w = 60 if " " in c else 36
        s.box(x, 22, w, 32, c, size=11, fill="#fbf0dd" if " " in c else "white", rx=3)
        x += w + 2
    s.text(150, 78, "each character is wrapped in a start bit and a stop bit, so no shared clock is needed", size=12, anchor="start")
    s.text(20, 130, "Synchronous", size=14, anchor="start", bold=True)
    for i in range(14):
        x = 150 + i * 36
        s.add(f'<path d="M{x} 150 L{x} 120 L{x + 18} 120 L{x + 18} 150 L{x + 36} 150" stroke="{ACCENT}" stroke-width="2" fill="none"/>')
    s.text(150, 180, "a clock signal keeps sender and receiver in step, so long blocks are sent with no gaps", size=12, anchor="start")
    return s.render("Asynchronous suits occasional data such as key presses; synchronous suits continuous, high-speed streams.")


def frame():
    s = SVG(760, 170, "The parts of an Ethernet frame")
    parts = [("Preamble", "7 B", 70, "#eef0f3"), ("SFD", "1 B", 45, "#eef0f3"), ("Destination\nMAC", "6 B", 95, "#dcebf6"), ("Source\nMAC", "6 B", 95, "#dcebf6"), ("Type /\nlength", "2 B", 65, "#e8f1e4"), ("Data (payload + padding)", "46–1500 B", 230, "#fbf0dd"), ("FCS\n(CRC)", "4 B", 60, "#fbe3d4")]
    x = 30
    for name, size, w, f in parts:
        s.box(x, 30, w, 60, name, size=11, fill=f, rx=2)
        s.text(x + w / 2, 110, size, size=11, color=ARROW)
        x += w
    s.text(380, 145, "header (who, from where, what kind)  ·  payload (the data)  ·  trailer (error check)", size=12, color=ACCENT)
    return s.render("A frame is a packet on a local network. The preamble lets the receiver lock on; the FCS lets it detect damage.")


def switching():
    s = SVG(760, 260, "Packets taking different routes across a network")
    s.box(20, 100, 110, 50, "Sender", "splits into 1 2 3", size=13, fill="#dcebf6")
    s.box(630, 100, 110, 50, "Receiver", "reorders 1 2 3", size=13, fill="#e8f1e4")
    routers = {"R1": (220, 60), "R2": (220, 190), "R3": (400, 60), "R4": (400, 190), "R5": (540, 125)}
    links = [("R1", "R3"), ("R2", "R4"), ("R1", "R4"), ("R3", "R5"), ("R4", "R5"), ("R1", "R2")]
    for a, b in links:
        s.line(*routers[a], *routers[b], color="#b9c7d5", width=2)
    s.line(130, 115, 220, 60, color="#b9c7d5", width=2)
    s.line(130, 135, 220, 190, color="#b9c7d5", width=2)
    s.line(540, 125, 630, 125, color="#b9c7d5", width=2)
    for n, (x, y) in routers.items():
        s.circle(x, y, 22, fill="white", label=n, size=12)
    s.text(310, 42, "packets 1 and 3", size=12, color=ARROW)
    s.text(310, 228, "packet 2 (a quieter route)", size=12, color=ACCENT)
    return s.render("Packet switching. Each router sends each packet on the best route at that moment; the receiver uses sequence numbers to rebuild the message.")


def caesar():
    s = SVG(760, 170, "A Caesar cipher with a shift of 3")
    import string
    for i, ch in enumerate(string.ascii_uppercase):
        x = 30 + i * 27
        s.box(x, 30, 25, 28, ch, size=12, fill="white", rx=2)
        s.box(x, 90, 25, 28, string.ascii_uppercase[(i + 3) % 26], size=12, fill="#dcebf6", rx=2)
    for i in range(0, 26, 5):
        s.arrow(42 + i * 27, 60, 42 + i * 27, 88, width=1.2)
    s.text(380, 150, "HELLO → KHOOR.  Only 25 possible shifts, so a computer can try them all instantly (brute force).", size=12, color=WARN)
    return s.render("A Caesar cipher replaces each letter with the one 3 places later. It is easy to understand but far too weak for real use.")


def public_key():
    s = SVG(760, 230, "Public key encryption between a browser and a shop")
    s.box(20, 80, 150, 60, "Your browser", size=14, fill="#dcebf6")
    s.box(590, 80, 150, 60, "Shop’s server", size=14, fill="#e8f1e4")
    s.box(290, 20, 180, 44, "Shop’s PUBLIC key", size=13, fill="#fbf0dd", stroke="#b58a3a")
    s.arrow(590, 70, 472, 42)
    s.text(610, 50, "shared with anyone", size=11, color=ARROW, anchor="start")
    s.arrow(170, 110, 588, 110, label="session key, locked with the public key", ly=-12, lsize=12)
    s.box(290, 150, 180, 44, "Shop’s PRIVATE key", size=13, fill="#fbe3d4", stroke=WARN)
    s.arrow(472, 172, 640, 142, color=WARN)
    s.text(650, 175, "never leaves", size=11, color=WARN, anchor="start")
    s.text(650, 190, "the server", size=11, color=WARN, anchor="start")
    s.text(380, 222, "Only the private key can unlock it. Both sides then use the fast symmetric session key.", size=12, color=ACCENT)
    return s.render("Public (asymmetric) key encryption solves the problem of sharing a secret key over an open network.")


E1 = deeper("E1",
    h3("Channels and connections"),
    channels(),
    serial_parallel(),
    async_sync(),
    table(["Connection", "Wired or wireless", "Typical speed and range", "Good for"], [
        ["Ethernet (copper)", "wired", "up to 1–10 Gbit/s, about 100 m", "desktop PCs, servers, reliable office networks"],
        ["Fibre optic", "wired (light)", "10+ Gbit/s over many km", "links between buildings, internet backbones"],
        ["USB", "wired", "hundreds of Mbit/s to tens of Gbit/s, a few metres", "peripherals, storage, charging"],
        ["Wi-Fi", "wireless (radio)", "hundreds of Mbit/s, tens of metres", "laptops, phones and tablets moving around a building"],
        ["Bluetooth", "wireless (radio)", "a few Mbit/s, about 10 m", "headphones, keyboards, watches"],
        ["4G / 5G", "wireless (mobile network)", "tens to hundreds of Mbit/s, kilometres", "phones and devices on the move"],
        ["NFC", "wireless (radio)", "slow, a few centimetres", "contactless payment, door passes"],
    ], caption="Selecting a connection method"),
    h3("Packets, frames and protocols"),
    frame(),
    switching(),
    table(["TCP/IP layer", "Job", "Example protocols"], [
        ["Application", "the service the user wants", "HTTP/HTTPS (web), SMTP/IMAP (email), DNS (names to addresses)"],
        ["Transport", "splits data into segments, numbers them, checks they all arrive", "TCP (reliable), UDP (fast, no resending)"],
        ["Internet", "addresses packets and routes them between networks", "IP"],
        ["Link", "moves frames across one physical network", "Ethernet, Wi-Fi"],
    ], caption="The TCP/IP protocol stack"),
    p("A <strong>protocol</strong> is a set of rules both sides agree to follow: the speed, the packet size and format, how the connection starts (a handshake), how errors are detected and corrected, and whether data is compressed or encrypted. Without shared protocols, devices from different makers could not understand each other."),
    h3("Keeping data private: encryption"),
    caesar(),
    public_key(),
    table(["", "Symmetric", "Public key (asymmetric)"], [
        ["Keys", "one secret key, used to lock and unlock", "a public key to lock and a private key to unlock"],
        ["Speed", "fast", "much slower"],
        ["Problem", "how to share the secret key safely", "slow for large amounts of data"],
        ["Used for", "encrypting files, discs and the main part of a secure session", "setting up a secure connection and digital signatures"],
    ], caption="Two kinds of encryption"),
    terms([
        ("Protocol", "an agreed set of rules for communication."),
        ("Frame / packet", "a unit of data with a header, a payload and usually an error check."),
        ("MAC address", "a hardware address that identifies a network interface on a local network."),
        ("Packet switching", "sending packets independently, possibly by different routes, then reassembling them."),
        ("Handshake", "an exchange of signals to set up a connection and agree its rules before data is sent."),
        ("Cipher", "a method of encrypting data; ciphertext is the encrypted result."),
    ]),
    think([
        ("Why does a video call use UDP rather than TCP?", "Speed matters more than perfection. Waiting for a lost packet to be re-sent would freeze the call, so it is better to skip it and carry on."),
        ("Decrypt ‘FDW’ with a Caesar shift of 3.", "Move each letter back 3 places: F→C, D→A, W→T, so the word is CAT."),
        ("Why does a secure website use both public key and symmetric encryption?", "Public key encryption safely shares a session key without it being intercepted; symmetric encryption is then used for the rest because it is much faster."),
    ]),
)


def noise():
    s = SVG(760, 200, "How interference changes a transmitted signal")
    s.text(20, 40, "Sent", size=13, anchor="start", bold=True)
    bits = "01101001"
    x = 100
    path = "M100 60"
    for b in bits:
        y = 30 if b == "1" else 60
        path += f" L{x} {y} L{x + 60} {y}"
        x += 60
    s.add(f'<path d="{path}" stroke="{ARROW}" stroke-width="2.5" fill="none"/>')
    for i, b in enumerate(bits):
        s.text(130 + i * 60, 80, b, size=13, mono=True)
    s.text(20, 130, "Received", size=13, anchor="start", bold=True)
    import random
    random.seed(4)
    x = 100
    path = "M100 150"
    for i, b in enumerate(bits):
        base = 120 if b == "1" else 150
        if i == 4:
            base = 120
        for k in range(6):
            path += f" L{x + k * 10} {base + random.randint(-6, 6)}"
        x += 60
    s.add(f'<path d="{path}" stroke="{WARN}" stroke-width="2" fill="none"/>')
    for i, b in enumerate(bits):
        wrong = i == 4
        s.text(130 + i * 60, 180, "1" if wrong else b, size=13, mono=True, color=WARN if wrong else INK, bold=wrong)
    s.text(630, 130, "noise flipped a bit", size=12, color=WARN, anchor="start")
    return s.render("Electrical interference, weak signals (attenuation) and crosstalk between wires can turn a 0 into a 1 or a 1 into a 0.")


def crc_fig():
    s = SVG(760, 180, "Adding and checking a CRC")
    s.box(20, 30, 260, 44, "Data bits", size=14, fill="white")
    s.box(280, 30, 90, 44, "CRC", size=14, fill="#fbe3d4")
    s.text(200, 100, "Sender divides the data by an agreed binary number", size=12)
    s.text(200, 118, "(the generator) and appends the remainder", size=12)
    s.arrow(380, 52, 440, 52)
    s.box(450, 30, 290, 44, "Receiver divides data + CRC again", size=13, fill="#dcebf6")
    s.text(595, 100, "remainder 0 → accept", size=13, color=ACCENT, bold=True)
    s.text(595, 122, "anything else → error detected", size=13, color=WARN, bold=True)
    s.text(380, 165, "CRC catches all single-bit errors and almost all bursts of errors, which is why Ethernet, Wi-Fi, ZIP files and discs use it.", size=12)
    return s.render("A cyclic redundancy check (CRC) is a more powerful checksum based on binary division.")


E2 = deeper("E2",
    h3("Why errors happen"),
    noise(),
    p("Errors are more likely over long cables, weak wireless signals, near electrical machinery, or when many wires run side by side. Error <strong>detection</strong> adds a little extra data calculated from the message. The receiver repeats the calculation: if its answer is different, something changed on the way."),
    worked("Even parity, and where it fails", [
        "Send the 7-bit code <code>1100101</code>. It has four 1s, already even, so the parity bit is 0: <code>0110 0101</code>.",
        "One bit flips to give <code>0110 0111</code>: now there are five 1s, odd, so the receiver knows it is wrong.",
        "Two bits flip to give <code>0110 1001</code>: four 1s, still even, so the error is <em>not</em> detected.",
        "Parity also cannot say <em>which</em> bit is wrong, so the byte must be sent again.",
    ]),
    worked("A simple checksum", [
        "Four bytes are sent: 45, 120, 200 and 16.",
        "Add them: 45 + 120 + 200 + 16 = 381.",
        "Keep only what fits in one byte: 381 − 256 = 125. The checksum 125 is sent after the data.",
        "The receiver adds the four bytes it received. If it also gets 125 the data is accepted; if not, it asks for it again.",
        "Weakness: if two bytes were swapped, the total would be the same and the error would be missed.",
    ]),
    crc_fig(),
    table(["Method", "How it works", "Detects", "Extra data"], [
        ["Parity bit", "one bit makes the number of 1s even (or odd)", "any odd number of flipped bits", "1 bit per byte"],
        ["Checksum", "sum of the data, trimmed to a fixed size", "most random errors, but not reordered data", "1–4 bytes per block"],
        ["CRC", "remainder of a binary division", "almost all errors, including bursts", "2–4 bytes per block"],
        ["Repetition", "send everything two or three times and compare", "differences between the copies", "doubles or triples the data"],
    ], caption="Error detection methods compared"),
    terms([
        ("Attenuation", "a signal getting weaker as it travels further."),
        ("Crosstalk", "a signal in one wire interfering with a neighbouring wire."),
        ("Parity bit", "an extra bit that makes the total number of 1s even or odd."),
        ("Checksum", "a value calculated from a block of data and sent with it."),
        ("CRC", "cyclic redundancy check: a checksum based on binary division."),
    ]),
    think([
        ("Using odd parity, what parity bit goes with <code>1100110</code>?", "It has four 1s (even), so the parity bit is 1 to make five, an odd number."),
        ("Why is a CRC better than a parity bit for a 1,500-byte packet?", "A parity bit only catches an odd number of flipped bits. Noise often damages several bits in a row (a burst); a CRC detects almost all bursts."),
    ]),
)


def arq():
    s = SVG(760, 330, "Automatic repeat request timeline")
    s.text(160, 28, "Sender", size=14, bold=True)
    s.text(600, 28, "Receiver", size=14, bold=True)
    s.line(160, 40, 160, 320, color=INK, width=2)
    s.line(600, 40, 600, 320, color=INK, width=2)
    s.arrow(160, 55, 598, 85, label="packet 1", ly=-8, lsize=12)
    s.arrow(600, 95, 162, 125, label="ACK 1 (received OK)", ly=-8, lsize=12, color=ACCENT)
    s.arrow(160, 140, 440, 160, color=WARN)
    s.text(470, 165, "✗ corrupted", size=13, color=WARN, anchor="start")
    s.text(300, 138, "packet 2", size=12, color=ARROW)
    s.add(f'<path d="M150 145 C110 180 110 210 150 235" stroke="{WARN}" stroke-width="2" fill="none" stroke-dasharray="5 4"/>')
    s.text(100, 195, "timer runs out:", size=12, color=WARN)
    s.text(100, 212, "no ACK", size=12, color=WARN)
    s.arrow(160, 240, 598, 270, label="packet 2 sent again", ly=-8, lsize=12)
    s.arrow(600, 280, 162, 310, label="ACK 2", ly=-8, lsize=12, color=ACCENT)
    return s.render("ARQ. The receiver acknowledges good packets; if no acknowledgement arrives in time, the sender sends the packet again.")


def fec():
    s = SVG(760, 200, "Forward error correction by sending each bit three times")
    s.text(90, 40, "Data", size=13, anchor="start", bold=True)
    s.text(90, 90, "Sent (×3)", size=13, anchor="start", bold=True)
    s.text(90, 140, "Received", size=13, anchor="start", bold=True)
    s.text(90, 185, "Majority vote", size=13, anchor="start", bold=True)
    data = "101"
    sent = ["111", "000", "111"]
    recv = ["111", "010", "101"]
    for i in range(3):
        x = 260 + i * 150
        s.text(x, 40, data[i], size=18, mono=True)
        s.text(x, 90, sent[i], size=18, mono=True)
        s.text(x, 140, recv[i], size=18, mono=True, color=WARN if recv[i] != sent[i] else INK)
        s.text(x, 185, data[i], size=18, mono=True, color=ACCENT, bold=True)
    s.text(690, 140, "2 bits damaged", size=12, color=WARN)
    s.text(690, 185, "all fixed", size=12, color=ACCENT)
    return s.render("A simple FEC code. The receiver repairs each bit by majority vote without asking for anything again, at the cost of sending three times as much.")


E3 = deeper("E3",
    h3("Asking again: ARQ"),
    arq(),
    p("<strong>Automatic repeat request</strong> needs error detection (such as a CRC), acknowledgements (ACKs) and a timer. It sends as little extra data as possible, but each error costs a round trip. That is fine on a fast local network, but painful on a satellite link where each round trip takes over half a second."),
    h3("Fixing it at the receiver: FEC"),
    fec(),
    p("Real systems use cleverer <strong>forward error correction</strong> codes than simple repetition. A <strong>Hamming code</strong> mixes a few parity bits into the data so that the pattern of failed parity checks points to the exact bit that flipped, which can then be flipped back. The same idea lets RAID rebuild a lost disc, lets a scratched CD still play, and lets a QR code be read even when part of it is covered."),
    table(["", "ARQ", "FEC"], [
        ["Needs a return channel?", "yes, for ACKs and requests", "no"],
        ["Extra data sent", "little, except when errors happen", "always some extra redundancy"],
        ["Delay", "each error costs a round trip", "no waiting"],
        ["Best when", "errors are rare and replies are quick (web pages, file downloads)", "replies are slow or impossible (space probes, live broadcasts, satellite links, storage media)"],
    ], caption="Choosing an error correction method"),
    terms([
        ("ACK / NAK", "acknowledgement (received correctly) / negative acknowledgement (please resend)."),
        ("Timeout", "the time a sender waits for an ACK before sending again."),
        ("Redundancy", "extra data added so errors can be detected or corrected."),
        ("Hamming code", "an FEC code that uses several parity bits to locate and fix a single wrong bit."),
    ]),
    think([
        ("Why is FEC used for live TV broadcasts?", "A broadcast is one-way (simplex), so viewers’ TVs cannot ask for anything to be sent again. The TV must fix errors itself."),
        ("A download over a very noisy link keeps timing out. What is happening?", "Many packets are damaged, so the sender keeps waiting for ACKs and re-sending. Adding some FEC, or fixing the cause of the noise, would reduce the repeats."),
    ]),
)

SECTIONS = {"E1": E1, "E2": E2, "E3": E3}
