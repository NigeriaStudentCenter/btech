"""Unit 8 videos, embedded click-to-play from the creators' official YouTube uploads (verified by title and channel with YouTube oEmbed).
The teacher's MP4 copies of the Cisco and TED films stay on Teams."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "unit19"))
from videos import card, CSS, JS  # noqa: F401


def v(id, lesson, title, channel, why, think, duration=None):
    d = {"id": id, "lesson": lesson, "title": title, "channel": channel, "why": why, "think": think}
    if duration:
        d["duration"] = duration
    return d


MB, CP = "MrBrownCS", "Computerphile"
VIDEOS = [
 v("nkwDSFEM25g", "S1", "Cyber Threats and Why Cyber Attacks Happen", MB, "Why attackers target organisations, and what they are after.", ["Which kinds of confidential information would each attacker want?"]),
 v("ep8RthBKHMY", "T1", "Types of Malware", MB, "Viruses, worms, trojans, ransomware and spyware compared.", ["How does a worm spread without anyone opening a file?"]),
 v("g7ymEY-i16M", "T1", "Botnets & DDoS", MB, "How infected devices are combined to knock services offline.", ["Why are DDoS attacks hard to block?"]),
 v("88jkB1V6N9w", "T1", "Wana Decrypt0r (WannaCry ransomware)", CP, "Stretch: a close look at the ransomware worm that hit hospitals in 2017.", ["Which two controls would have limited the damage most?"]),
 v("QZpGvcQx0tA", "T2", "Computer-Based Attacks (Malware, Brute-Forcing Passwords)", MB, "How brute-force password attacks work.", ["Why does a longer password take so much longer to crack?"]),
 v("FK4B8U9t6Hk", "T2", "Network-Based Attacks (SQL Injection, Denial of Service & Data Interception)", MB, "SQL injection, DoS and interception in one short video.", ["What makes a website vulnerable to SQL injection?"]),
 v("_jKylhJtPmI", "T2", "Hacking Websites with SQL Injection", CP, "Stretch: a real SQL injection demonstrated on a test site.", ["How do parameterised queries stop this attack?"]),
 v("L5l9lSnNMxg", "T2", "Cracking Websites with Cross Site Scripting", CP, "Stretch: how a script typed into a page can run in other people’s browsers.", ["What could the attacker steal with the script?"]),
 v("7U-RbOKanYs", "T2", "Password Cracking", CP, "Stretch: how cracking tools guess hashed passwords.", ["Why do salted hashes slow attackers down?"]),
 v("sRjwwNJ-8oA", "T3", "Social Engineering: Phishing, Pharming and Shoulder Surfing", MB, "The main social engineering attacks and how to spot them.", ["What is the difference between phishing and pharming?"]),
 v("8XXwjDLyGWw", "T3", "Social Engineering", MB, "More social engineering methods and their impact on organisations.", ["Which attack would work best against a busy receptionist, and why?"]),
 v("-enHfpHMBo4", "T4", "Man in the Middle Attacks & Superfish", CP, "How an attacker sits between you and a website, and a real case where laptops shipped with the problem.", ["Why do certificate warnings matter?"]),
 v("7MT1F0O3_Yw", "T4", "DNS Cache Poisoning", CP, "Stretch: how a DNS server can be tricked into sending users to the wrong site.", ["Which users are affected when a DNS cache is poisoned?"]),
 v("mYtvjijATa4", "T4", "Krack Attacks (WiFi WPA2 Vulnerability)", CP, "Stretch: a real weakness found in Wi-Fi security and why patches mattered.", ["Why did this attack need devices to be updated?"]),
 v("1jh8SGaArV8", "V1", "Vulnerabilities", MB, "Technical and human vulnerabilities in organisations.", ["Which vulnerabilities are caused by out-of-date components?"]),
 v("BHHCvcCUOWU", "V1", "All your devices can be hacked (Avi Rubin)", "TED-Ed / TEDxMidAtlantic", "A security researcher shows how cars, pacemakers and phones can be attacked.", ["Why are embedded devices often left unpatched?"], "16:56"),
 v("7egBsN_4B2A", "V1", "Anatomy of an IoT Attack", "Cisco (uploaded by Pxosys, a Cisco partner)", "An attack through an unsecured smart thermostat on an unsegmented network.", ["Which vulnerabilities did the attacker exploit?", "Which lesson M5 control would have stopped it?"], "3:38"),
 v("LOcx2uZLNdg", "V2", "Common Internal Cyber Threats to Organisations", MB, "Accidental and deliberate threats from inside an organisation.", ["How should an organisation respond when a malicious employee is dismissed?"]),
 v("P15EdxEg6Ic", "V3", "Physical Security Measures & Biometrics", MB, "Locks, access control and biometrics.", ["Which physical controls stop tailgating?"]),
 v("yGkiuTb1SNQ", "V3", "Physical Security Methods", MB, "More physical protection for sites and equipment.", ["Pick one control for each layer: perimeter, building, server room."]),
 v("tuxi2C-EeSc", "M1", "Protecting Against Malware", MB, "Anti-malware, updates and other defences.", ["What actions can anti-malware take when it finds a threat?"]),
 v("xertLB9J9QE", "M1", "System Security #2: Detection and Prevention", MB, "Detecting and preventing attacks on systems.", ["What is the difference between detection and prevention?"]),
 v("QzR1YKjadkw", "M1", "Prevention Measures", MB, "A tour of prevention measures used by organisations.", ["Which measures are physical, which technical, and which people-based?"]),
 v("-9rK3EZop_M", "M2", "Symmetric and Asymmetric Encryption", MB, "One key or a key pair: how each works.", ["Why is asymmetric encryption used to share a symmetric key?"]),
 v("b4b8ktEV4Bg", "M2", "Hashing Algorithms and Security", CP, "What a hash is and why it is used for passwords.", ["Why can’t a hash be reversed?"]),
 v("NmM9HA2MQGI", "M2", "Secret Key Exchange (Diffie-Hellman)", CP, "The colour-mixing explanation of agreeing a key in public.", ["What does the eavesdropper see, and why is it not enough?"]),
 v("ZXFYT-BG2So", "M3", "2FA: Two Factor Authentication", CP, "How two-factor authentication works and why it helps.", ["Which factor types does an authenticator app use?"]),
 v("hGRii5f_uSc", "M3", "Why You Should Turn On Two Factor Authentication", "Tom Scott", "A clear case for turning on 2FA everywhere.", ["What happens to a stolen password when 2FA is on?"]),
 v("w68BBPDAWr8", "M3", "How Password Managers Work", CP, "What a password manager stores and how it is protected.", ["What is the biggest risk of a password manager, and how is it reduced?"]),
 v("v9p6IsQw9rg", "M4", "Backup Policies", MB, "Full, incremental and differential backups and where to keep them.", ["Which backup type gives the fastest restore?"]),
 v("kDSR2qJBo70", "M4", "Ethical Hacking and Penetration Testing", MB, "What penetration testers do and why it must be authorised.", ["What makes hacking ‘ethical’?"]),
 v("CeTATgOp3eE", "M5", "Firewalls", MB, "How firewalls filter traffic with rules.", ["Give one inbound and one outbound rule for a school."]),
 v("j0EZpH_eIsY", "M5", "Anatomy of an Attack: inside the mind of a hacker", "Cisco (produced by Kraft Technology Group)", "How an attack unfolds, and where monitoring and segregation help.", ["At which point could network monitoring have spotted the attacker?"], "4:00"),
 v("kPPFNrlN3zo", "C1", "What is the CIA Triad", "IBM Technology", "Confidentiality, integrity and availability explained by a security architect.", ["Give an attack that mainly affects each element."]),
 v("AhaZtj5P2a8", "C2", "Authentication, Authorization, and Accounting", "Professor Messer", "Stretch: how identity, authentication, authorisation and accounting work in real networks.", ["Which part of IAAA do audit logs support?"]),
]


def for_lesson(lid):
    vs = [x for x in VIDEOS if x["lesson"] == lid]
    return f'<h3>Watch</h3>{"".join(card(x) for x in vs)}' if vs else ""
