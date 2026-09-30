"""Unit 7 videos, embedded click-to-play from the creators' official YouTube uploads (verified by title and channel).
The revision series is by MrBrownCS; the teacher's MP4 copies stay on Teams."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "unit19"))
from videos import card, CSS, JS  # noqa: F401

MB = "MrBrownCS"


def mb(id, lesson, title, think, why="A short revision video from the MrBrownCS series."):
    return {"id": id, "lesson": lesson, "title": title, "channel": MB, "why": why, "think": think}


VIDEOS = [
 mb("Ol3PxSpEeT4", "NS", "Introduction to Binary", ["What is the largest number 8 bits can hold?"]),
 mb("7LGgLi4vYsk", "NS", "Binary-Decimal Conversions", ["Convert 0110 0101 to denary."]),
 mb("4wrBpIYimrw", "NS", "Binary Addition", ["What happens when a carry goes past the 8th bit?"]),
 mb("WbODFlqzSoc", "NS", "Signed Binary (Sign and Magnitude & Two's Complement)", ["Why is two’s complement preferred for calculations?"]),
 mb("J0GxnTC8ILs", "H1", "Embedded Systems and their Common Characteristics", ["List three embedded systems in your home.", "Why are embedded systems usually cheap and low power?"]),
 {"id": "Bud-mqaBKPM", "lesson": "H1", "title": "Internet of Everything: Circle Story", "channel": "Cisco advert (uploaded by PERRY proTECH, a Cisco partner)", "duration": "1:00",
  "why": "A one-minute film of connected devices triggering each other: an IoT starter.", "think": ["List three embedded or IoT devices in the film.", "What could go wrong if one was hacked?"]},
 {"id": "BHHCvcCUOWU", "lesson": "H1", "title": "All your devices can be hacked (Avi Rubin)", "channel": "TED-Ed / TEDxMidAtlantic", "duration": "16:56",
  "why": "A security researcher shows how cars, pacemakers and phones, all embedded computers, can be attacked.", "think": ["Why are embedded devices often less secure than PCs?", "Which device in the talk surprised you most, and why?"]},
 mb("eS1rEJZKr4U", "H2", "Factors Affecting CPU Performance (Clock Speed, Cache & Multiple-Cores)", ["Why doesn’t doubling the cores always double the speed?"]),
 mb("g1N3l1l43kE", "H2", "Main Memory (RAM, ROM and Cache)", ["Why is ROM needed when the computer starts?"]),
 mb("_0KIfGxp37E", "H2", "Secondary Storage (Optical, Magnetic, Solid-State & Cloud)", ["Which storage would you choose for a laptop, and why?"]),
 mb("SbqXqQ-2ixs", "H2", "The CPU and Von Neumann Architecture", ["What does the ALU do?"]),
 mb("3osm-soT_Lc", "H2", "Address, Data and Control Buses", ["Which bus carries data in both directions?"]),
 mb("LO4ige_j1Ig", "H2", "Special-Purpose Registers (PC, ACC, MAR and MDR)", ["What does the program counter hold?"]),
 mb("7vbRGDgHukA", "SW1", "Operating System (OS)", ["Name three jobs an operating system does."]),
 mb("Z0uVNcNKags", "SW2", "Utility Software and Models", ["Give two utilities and the problem each solves."]),
 mb("v1u-vY6NEmM", "SW2", "Lossy and Lossless (RLE) Compression", ["When must you use lossless compression?"]),
 mb("TdQgP_Gee_A", "N1", "Network Types and Performance", ["What factors reduce network performance?"]),
 mb("jXVtakoOjc0", "N2", "The Ethernet and WiFi Protocols", ["Why is Ethernet usually faster and more reliable than Wi-Fi?"]),
 mb("MVihcigDlbA", "N5", "Network Protocols and the 4 Layer Model", ["Name the four TCP/IP layers in order."]),
 mb("9uAIGQBkQzc", "N6", "Check Digits and Parity Bits", ["How is a parity bit like a CRC, and how is it weaker?"]),
 mb("7LfTWbOp5vU", "N7", "TCP, IP, HTTP/S and FTP", ["Which protocol would you use to upload a website securely?"]),
 mb("0F1JP78JAPE", "N7", "Email Protocols: SMTP, POP and IMAP", ["Which mail protocol suits someone using a phone and a laptop?"]),
 mb("yWgKSx0eFzY", "R1", "Encryption and the Caesar Cipher", ["Why does encryption improve resilience?"], why="Data security in storage and transfer is a benefit of resilient environments (7.6.1)."),
 {"id": "7egBsN_4B2A", "lesson": "R1", "title": "Anatomy of an IoT Attack", "channel": "Cisco (uploaded by Pxosys, a Cisco partner)", "duration": "3:38",
  "why": "A dramatised attack through an unsecured smart thermostat on an unsegmented network.", "think": ["Which resilience methods would have stopped the attack?", "What did the company lose?"]},
 {"id": "j0EZpH_eIsY", "lesson": "R1", "title": "Anatomy of an Attack: inside the mind of a hacker", "channel": "Cisco (produced by Kraft Technology Group)", "duration": "4:00",
  "why": "How a ransomware attack comes together, and why patching, hardening and backups matter.", "think": ["How did the attacker get in?", "How would tested backups change the outcome?"]},
 {"id": "jn8ymi1aIgY", "lesson": "R1", "title": "Completion of the Long Beach Container Terminal", "channel": "Port of Long Beach (via OOCL)",
  "why": "A fully automated port that stops if its network fails: a real case for redundancy and reduced downtime.", "extra": ("Read the VectorUSA and Cisco case study", "https://blog.vectorusa.com/vector-usa-and-cisco-team-up-to-build-a-fully-automated-container-terminal"),
  "think": ["Which resilience methods would you expect this port to use?"]},
 mb("a3Y_ZvOr0K0", None, "Representing Images in Binary", ["How does colour depth affect file size?"], why="Extra revision (data representation)."),
 mb("HlOTuCFtuV8", None, "Representing Sound in Binary", ["What is the sample rate?"], why="Extra revision (data representation)."),
 mb("tdmeXcDX-Uc", None, "Representing Text in Binary (ASCII & Unicode)", ["Why was Unicode needed?"], why="Extra revision (data representation)."),
 mb("E5V9zBBAfWM", None, "Logic Gates (AND, OR and NOT)", ["When does an AND gate output 1?"], why="Extra revision (logic)."),
 mb("6bKeE1A5-LY", None, "Data Structures", ["What is the difference between an array and a record?"], why="Extra revision (data structures)."),
]


def for_lesson(lid):
    vs = [v for v in VIDEOS if v["lesson"] == lid]
    return f'<h3>Watch</h3>{"".join(card(v) for v in vs)}' if vs else ""
