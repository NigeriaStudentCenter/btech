"""Unit 8 Security: lessons for 8.3 threat mitigation and 8.4 interrelationship of components (original content)."""
from u8_a import *  # noqa
from u8_a import SVG, device, INK, LINE, ARROW, ACCENT, WARN, RED, REDBG, AMBERBG, BLUEBG, GREENBG, GREEN, exam_tip, practical, ethics, spec
import section_a as dA


# ---------- M1 technical defences ----------
def ids_fig():
    s = SVG(760, 260, "Where defences sit on a network")
    device(s, "cloud", 20, 80, "Internet", w=70)
    device(s, "firewall", 140, 80, "Firewall", w=64)
    device(s, "switch", 270, 78, "Switch", w=70)
    s.arrow(92, 102, 138, 102, width=1.8)
    s.arrow(206, 102, 268, 102, width=1.8)
    s.box(250, 160, 110, 50, "IDS sensor", "watches copies", size=12, fill=AMBERBG)
    s.line(305, 144, 305, 158, color=ACCENT, width=1.6, dash=True)
    for i, (k, lab) in enumerate([("pc", "PC: anti-malware, updates"), ("server", "Server: hardened"), ("laptop", "Laptop: encrypted disk")]):
        y = 12 + i * 70
        device(s, k, 440, y, w=60)
        s.text(510, y + 26, lab, size=12, anchor="start")
        s.line(342, 100, 442, y + 22, color=LINE, width=1.4)
    s.box(560, 205, 180, 44, "Alert to the security team", size=12, fill=REDBG)
    s.arrow(362, 190, 558, 226, color=RED, width=1.4)
    return s.render("Defence in depth: a firewall at the edge, an intrusion detection system watching traffic, and hardened, updated, protected devices inside.")


M1 = lesson("M1", "8.3 Threat mitigation", "Technical defences: settings, anti-malware, detection, hardening and updates",
    "explain the purpose, process, benefits and drawbacks of security settings, anti-malware, intrusion detection, device hardening, updates and air gaps.", spec("8.3.1"),
    ids_fig(),
    table(["Technique", "Purpose and process", "Benefits", "Drawbacks"], [
        ["Security settings (hardware and software)", "configure devices and software securely: BIOS/UEFI passwords, disable unused ports, browser and OS privacy settings", "cheap; closes easy gaps", "needs knowledge; settings can be changed back or forgotten"],
        ["Anti-malware software", "function: scans files, emails and downloads against signatures and suspicious behaviour; actions: quarantine, delete, alert", "stops most known malware automatically", "must be updated; may miss new malware; can slow the device; false positives"],
        ["Intrusion detection (IDS)", "monitors network or device activity for suspicious patterns and raises alerts (an IPS also blocks)", "spots attacks in progress; evidence for investigation", "false alarms; someone must respond; cost"],
        ["Device hardening", "remove unneeded software, services, ports, accounts and default passwords", "smaller attack surface", "takes time; may break features if done carelessly"],
        ["Software updates", "install patches that fix security bugs, ideally automatically", "closes known vulnerabilities quickly", "updates can fail or cause compatibility issues; need testing and restarts"],
        ["Firmware / driver updates", "update the low-level code in routers, BIOS, printers and devices", "fixes hardware-level weaknesses", "risky if interrupted; often forgotten"],
        ["Air gaps", "keep a critical system physically disconnected from other networks", "cannot be attacked over the network", "inconvenient data transfer; still vulnerable to USB and insiders"],
    ], caption="8.3.1 Technical mitigation techniques"),
    terms([("Signature", "a pattern that identifies known malware."), ("Quarantine", "isolating a suspicious file so it cannot run."), ("IDS", "intrusion detection system: monitors and alerts on suspicious activity."), ("Air gap", "physical separation of a system from any network.")]),
    exam_tip("‘Benefits and drawbacks’ is in the specification for every mitigation technique. Learn at least one of each: e.g. air gaps are very secure <em>but</em> make updating and sharing data slow."),
    think([("Why does anti-malware need regular updates?", "New malware appears constantly; without updated signatures and detection rules the software will not recognise it."),
           ("Give an example of a system that might use an air gap, and one weakness.", "A power station’s control system or a military network; it can still be infected by a USB stick or an insider.")]),
)


# ---------- M2 encryption ----------
def hash_fig():
    s = SVG(760, 210, "Hashing a password")
    rows = [("password", "5e884898da28047151d0e56f…"), ("Password", "e7cf3ef4f17c3999a94f2c6f…"), ("password1", "0b14d501a594442a01c68595…")]
    for i, (a, b) in enumerate(rows):
        y = 25 + i * 52
        s.box(20, y, 150, 38, a, size=14, fill=BLUEBG, rx=5)
        s.box(250, y, 120, 38, "SHA-256", size=13, fill="#f3e8f9", rx=5)
        s.arrow(170, y + 19, 248, y + 19, width=1.6)
        s.arrow(370, y + 19, 418, y + 19, width=1.6)
        s.text(425, y + 24, b, size=13, anchor="start", mono=True)
    s.text(380, 196, "One-way: you cannot turn the hash back into the password. A tiny change gives a totally different hash.", size=12, color=ARROW)
    return s.render("A hash is a fixed-length fingerprint of data. Systems store password hashes (with a random salt), then hash what you type and compare.")


def keys_fig():
    s = SVG(760, 250, "Symmetric and asymmetric encryption")
    s.text(190, 24, "Symmetric: one shared key", size=15, bold=True)
    s.box(20, 50, 100, 40, "Plaintext", size=12, fill="white")
    s.box(140, 50, 100, 40, "Ciphertext", size=12, fill=REDBG)
    s.box(260, 50, 100, 40, "Plaintext", size=12, fill="white")
    s.arrow(120, 70, 138, 70, width=1.6)
    s.arrow(240, 70, 258, 70, width=1.6)
    s.text(129, 110, "encrypt with key K", size=11)
    s.text(249, 128, "decrypt with the same K", size=11)
    s.text(190, 170, "fast; good for large data (AES)", size=12, color=GREEN)
    s.text(190, 190, "problem: how do you share K safely?", size=12, color=RED)
    s.text(570, 24, "Asymmetric: a key pair", size=15, bold=True)
    s.box(400, 50, 100, 40, "Plaintext", size=12, fill="white")
    s.box(520, 50, 100, 40, "Ciphertext", size=12, fill=REDBG)
    s.box(640, 50, 100, 40, "Plaintext", size=12, fill="white")
    s.arrow(500, 70, 518, 70, width=1.6)
    s.arrow(620, 70, 638, 70, width=1.6)
    s.text(509, 110, "encrypt with the", size=11)
    s.text(509, 124, "receiver’s PUBLIC key", size=11, bold=True)
    s.text(629, 142, "decrypt with their", size=11)
    s.text(629, 156, "PRIVATE key", size=11, bold=True)
    s.text(570, 190, "no shared secret needed; slower (RSA)", size=12, color=GREEN)
    s.text(570, 210, "also used for digital signatures", size=12, color=GREEN)
    s.line(380, 20, 380, 230, color=LINE, width=1.5, dash=True)
    return s.render("Symmetric encryption is fast but needs a shared key. Asymmetric encryption solves key sharing, so HTTPS uses asymmetric methods to agree a symmetric session key.")


def dh_fig():
    s = SVG(760, 250, "Diffie-Hellman key exchange with small numbers")
    s.box(250, 10, 260, 40, "Public: P = 23, G = 9", size=14, fill="#eef0f3", bold=True)
    s.box(20, 70, 230, 150, fill=BLUEBG)
    s.box(510, 70, 230, 150, fill=GREENBG)
    s.text(135, 92, "Alice: secret a = 4", size=13, bold=True)
    s.text(135, 118, "sends 9⁴ mod 23 = 6", size=13)
    s.text(135, 160, "receives 16", size=13)
    s.text(135, 186, "16⁴ mod 23 = 9", size=13, bold=True)
    s.text(625, 92, "Bob: secret b = 3", size=13, bold=True)
    s.text(625, 118, "sends 9³ mod 23 = 16", size=13)
    s.text(625, 160, "receives 6", size=13)
    s.text(625, 186, "6³ mod 23 = 9", size=13, bold=True)
    s.arrow(252, 114, 508, 114, width=1.6, label="6", ly=-6)
    s.arrow(508, 150, 252, 150, width=1.6, label="16", ly=-6)
    s.text(380, 240, "Both reach the shared key 9. An eavesdropper sees only 23, 9, 6 and 16.", size=12, color=ACCENT)
    return s.render("Two people agree a secret key over a public channel without ever sending it. Real systems use numbers hundreds of digits long.")


M2 = lesson("M2", "8.3 Threat mitigation", "Encryption: hashing, symmetric and asymmetric",
    "explain the purpose, process, benefits and drawbacks of hashing, symmetric encryption and asymmetric encryption.", spec("8.3.1"),
    p("<strong>Encryption</strong> scrambles data with a key so only someone with the right key can read it. It protects data <strong>at rest</strong> (on disks and backups) and <strong>in transit</strong> (across networks)."),
    hash_fig(),
    keys_fig(),
    dh_fig(),
    table(["Method", "Benefits", "Drawbacks", "Used for"], [
        ["Hashing", "one-way; passwords are never stored in readable form; detects any change to data (integrity)", "cannot be reversed to recover data; weak or unsalted hashes can be cracked with precomputed tables", "password storage, file integrity checks, digital signatures"],
        ["Symmetric", "fast and efficient for large amounts of data", "the key must be shared securely; if it leaks, all data is exposed", "disk encryption, Wi-Fi (WPA2/3), bulk data in HTTPS"],
        ["Asymmetric", "no need to share a secret key; enables digital signatures and certificates", "much slower; needs key management and trusted certificates", "HTTPS handshakes, secure email, digital signatures"],
    ], caption="Comparing the three methods"),
    practical("Diffie-Hellman by hand", ["Work through the example above with a partner: choose your own secret numbers with P = 23 and G = 5.", "Calculate your public values, swap them, and calculate the shared key. Check you both get the same answer.", "Explain why an eavesdropper who sees P, G and both public values still cannot easily find the key."], "Based on your teacher’s Diffie-Hellman spreadsheet."),
    terms([("Plaintext / ciphertext", "readable data / encrypted data."), ("Hash", "a fixed-length, one-way fingerprint of data."), ("Salt", "random data added to a password before hashing so identical passwords get different hashes."), ("Public / private key", "the pair used in asymmetric encryption: share the public one, never the private one.")]),
    exam_tip("Hashing is not encryption: it cannot be reversed. Say which method fits the purpose: hashing for stored passwords and integrity, symmetric for speed, asymmetric for sharing keys and signatures."),
    think([("Why do websites store password hashes rather than encrypted passwords?", "A hash cannot be reversed, so even if the database is stolen the passwords are not directly readable; the site only needs to compare hashes."),
           ("Why does HTTPS use both asymmetric and symmetric encryption?", "Asymmetric encryption safely agrees a session key; the faster symmetric encryption then protects the rest of the data.")]),
)


# ---------- M3 people and access ----------
def mfa_fig():
    s = SVG(760, 200, "The factors of authentication")
    f = [("Something you know", "password, passphrase, PIN", BLUEBG), ("Something you have", "phone app code, smart card, security key", AMBERBG), ("Something you are", "fingerprint, face, iris, voice", GREENBG)]
    for i, (a, b, c) in enumerate(f):
        x = 20 + i * 245
        s.circle(x + 115, 70, 48, fill=c)
        s.text(x + 115, 66, ["?", "▭", "◉"][i], size=26)
        s.text(x + 115, 140, a, size=14, bold=True)
        s.text(x + 115, 160, b, size=12)
    s.text(380, 192, "MFA = two or more DIFFERENT factors. A password plus a PIN is still one factor.", size=12, color=ACCENT)
    return s.render("Multi-factor authentication means a stolen password alone is not enough to log in.")


M3 = lesson("M3", "8.3 Threat mitigation", "People and access: policies, vetting, training, MFA, VPNs and APIs",
    "explain user access policies, staff vetting and training, software-based access control, MFA, password managers, VPNs and API certification, with benefits and drawbacks.", spec("8.3.1"),
    mfa_fig(),
    table(["Technique", "Purpose and process", "Benefits", "Drawbacks"], [
        ["User access policies", "written rules for who gets which access, how passwords work and how accounts are created and removed", "consistent, least-privilege access", "must be enforced and reviewed"],
        ["Staff vetting", "checks before employment: references, identity, criminal record (e.g. DBS) for sensitive roles", "reduces insider risk", "takes time and money; people can change after joining"],
        ["Staff training", "teach staff to spot phishing, use strong passwords, lock screens and report incidents", "tackles the biggest risk: people", "needs repeating; some staff ignore it"],
        ["Software-based access control", "permissions on files, folders, apps and databases by user or role", "users see only what they need", "complex to manage; mistakes grant too much access"],
        ["Multi-factor authentication", "combine two or more factor types at login", "stolen passwords alone are useless", "slower login; lost phone or token needs a recovery process"],
        ["Password managers", "generate, store and fill unique strong passwords in an encrypted vault", "one strong master password; no reuse", "the vault is a single target; needs MFA and trust in the provider"],
        ["VPNs", "encrypt traffic between a device and the organisation’s network", "safe remote working on any Wi-Fi", "can slow connections; the VPN itself must be patched"],
        ["Certification of APIs", "APIs are tested and certified to meet security standards before use", "trusted integrations; fewer insecure APIs", "cost and time; certification can go out of date"],
    ], caption="8.3.1 People and access controls"),
    real_world("MFA stops a phishing attack", "An employee enters their password on a fake login page. The attacker tries it, but the account requires a code from the employee’s authenticator app, so the login fails and the security team is alerted."),
    terms([("MFA", "multi-factor authentication: at least two different factor types."), ("Vetting", "background checks on staff before they are given access."), ("Password manager", "software that stores and creates strong passwords."), ("VPN", "an encrypted tunnel across an untrusted network.")]),
    exam_tip("When asked to recommend controls, combine a people control with a technical one, and state a drawback. That shows balance, which ‘evaluate’ and ‘discuss’ questions reward."),
    think([("Why is a password plus a security question not true multi-factor authentication?", "Both are ‘something you know’, so they are the same factor; an attacker who phishes one can phish the other."),
           ("Give one benefit and one drawback of password managers.", "Benefit: every account can have a unique, long password. Drawback: if the master password is weak or stolen, all passwords are exposed.")]),
)


# ---------- M4 backups, scanning and penetration testing ----------
def pentest_fig():
    s = SVG(760, 170, "The stages of a penetration test")
    st = [("1 Plan and agree", "written permission"), ("2 Reconnaissance", "gather information"), ("3 Scan", "ports, services, versions"), ("4 Exploit", "safely test weaknesses"), ("5 Report", "findings and fixes")]
    for i, (a, b) in enumerate(st):
        x = 12 + i * 150
        s.box(x, 40, 138, 70, a, b, size=13, fill=[BLUEBG, "#eef0f3", AMBERBG, REDBG, GREENBG][i])
        if i:
            s.arrow(x - 12, 75, x - 1, 75, width=1.6)
    s.text(380, 150, "Ethical hackers have permission and report to the owner. Unethical hackers do not.", size=12, color=ACCENT)
    return s.render("Penetration testing finds weaknesses before criminals do.")


M4 = lesson("M4", "8.3 Threat mitigation", "Backups, port scanning and penetration testing",
    "explain backup types and safe storage, port scanning and penetration testing (ethical and unethical hacking), with benefits and drawbacks.", spec("8.3.1"),
    dA.backup_types(),
    table(["Backup type", "Benefit", "Drawback"], [
        ["Full", "everything in one set: simplest, fastest restore", "slowest to make; most storage"],
        ["Incremental", "only changes since the last backup of any kind: quickest, least storage", "restore needs the full plus every incremental in order"],
        ["Differential", "changes since the last full backup", "grows each day; restore needs the full plus the latest differential"],
    ], caption="Backup types"),
    p("<strong>Safe storage:</strong> keep at least one copy offsite or in the cloud and one offline (so ransomware cannot reach it), encrypt backups, and test restoring regularly. A common rule is 3-2-1: three copies, on two kinds of media, one offsite."),
    h3("Port scanning"),
    p("A <strong>port scan</strong> checks which network ports on a device are open and which services are listening. Defenders scan their own systems to find services that should be closed; attackers scan to find a way in."),
    cli(["nmap -sn 10.6.6.0/24        # which hosts are up?", "nmap -sV 10.6.6.23          # open ports and service versions", "nmap -p 1-1000 10.6.6.23    # scan a range of ports", "nmap -O 10.6.6.23           # guess the operating system"], "Nmap commands used in the lab network practical."),
    pentest_fig(),
    table(["", "Ethical hacking (penetration testing)", "Unethical hacking"], [
        ["Permission", "written permission and an agreed scope", "none: illegal under computer misuse law"],
        ["Purpose", "find and fix weaknesses", "steal, damage, extort or show off"],
        ["Outcome", "a report to the owner with recommendations", "harm to the organisation and its clients"],
    ], caption="Ethical vs unethical hacking"),
    ethics("Only scan or test systems you own or have written permission to test. Scanning other networks can be a criminal offence. Use the college lab or a virtual lab only."),
    terms([("Port", "a numbered endpoint for a network service, e.g. 443 for HTTPS."), ("Port scan", "checking which ports on a host are open."), ("Penetration test", "an authorised simulated attack to find weaknesses."), ("Scope", "the systems a tester is allowed to test.")]),
    exam_tip("Benefits of penetration testing: finds real weaknesses before criminals, tests staff responses. Drawbacks: costly, only a snapshot in time, may disrupt services, testers must be trusted."),
    think([("Why is a restore test as important as the backup itself?", "A backup that cannot be restored is useless; testing proves the data and the process work before a real disaster."),
           ("What makes a penetration tester’s work legal when an attacker’s identical actions are not?", "The tester has the owner’s written permission and works within an agreed scope.")]),
)


# ---------- M5 internet security processes ----------
def firewall_fig():
    s = SVG(760, 250, "Firewall rules and network segregation")
    device(s, "cloud", 20, 90, "Internet", w=70)
    device(s, "firewall", 150, 90, "Firewall", w=64)
    s.arrow(92, 112, 148, 112, width=1.8)
    s.box(280, 20, 200, 80, "DMZ", "public web and mail servers", size=14, fill=AMBERBG)
    s.box(280, 140, 200, 90, "Internal LAN", "staff PCs, file server,\ndatabase", size=14, fill=BLUEBG)
    s.arrow(214, 104, 278, 60, width=1.6)
    s.arrow(214, 120, 278, 185, width=1.6)
    rules = [("ALLOW", "in: any → DMZ web, port 443"), ("ALLOW", "out: LAN → any, ports 80, 443"), ("DENY", "in: any → LAN, all ports"), ("DENY", "app: file-sharing software"), ("DENY", "IP: known bad address list")]
    s.text(510, 24, "Rule table (checked top to bottom)", size=12, anchor="start", bold=True)
    for i, (a, b) in enumerate(rules):
        y = 36 + i * 36
        s.box(510, y, 64, 28, a, size=11, fill=GREENBG if a == "ALLOW" else REDBG, rx=4, bold=True)
        s.text(582, y + 19, b, size=11, anchor="start")
    s.text(610, 226, "Anything not allowed is denied.", size=11, color=ARROW)
    return s.render("A firewall applies rules to inbound and outbound traffic by type, application and IP address. Segregation keeps public servers away from the internal network.")


M5 = lesson("M5", "8.3 Threat mitigation", "Firewalls, network segregation and monitoring",
    "explain firewall configuration, network segregation, network monitoring and port scanning, and why they are used.", spec("8.3.2"),
    firewall_fig(),
    table(["Firewall rule type", "Example", "Why"], [
        ["Rules for traffic (inbound and outbound)", "block all inbound except web traffic to the web server; allow outbound web browsing", "stops unrequested connections in, and malware calling out"],
        ["Traffic type rules", "allow HTTPS (443) and DNS (53); block Telnet (23)", "only needed, secure protocols are used"],
        ["Application rules", "block file-sharing or remote-control apps", "stops risky software even on allowed ports"],
        ["IP address rules", "block known malicious addresses; allow the admin VPN only from office IPs", "limits who can connect at all"],
    ], caption="8.3.2 Firewall configuration"),
    table(["Process", "What it is", "Why it is used"], [
        ["Virtual segregation", "VLANs and subnets split one physical network into separate logical networks", "a breach in one segment (e.g. guest Wi-Fi) cannot reach another (finance)"],
        ["Physical segregation", "separate cabling and switches for sensitive systems", "strongest separation for critical systems"],
        ["Offline network", "a network with no connection to the internet", "protects the most critical systems, e.g. industrial control"],
        ["Network monitoring", "tools watch traffic, logs, bandwidth and alerts continuously", "spot attacks, faults and unusual use early"],
        ["Port scanning", "regularly scan your own network for open ports", "find unexpected services before attackers do"],
    ], caption="Other internet security processes"),
    practical("configure a firewall in Packet Tracer", ["Build a network with three PCs, a switch and a server (addresses 1.0.0.1–1.0.0.4, mask 255.0.0.0).", "Check that every PC can ping the server and open its web page.", "On the server, open Services → Firewall and turn it on.", "Add a rule to deny ICMP from one PC and allow it from the others. Test with ping.", "Add a rule to allow only HTTP. Explain what changed and why a default-deny rule is safer."], "Based on your teacher’s ‘Basic firewall configuration in Cisco Packet Tracer’ practical."),
    terms([("Firewall", "hardware or software that filters traffic using rules."), ("DMZ", "a separate network zone for public-facing servers."), ("Network segregation", "dividing a network into separate zones."), ("Default deny", "blocking everything not explicitly allowed.")]),
    exam_tip("Say what each firewall rule type controls and give a realistic example. For segregation, explain the benefit (containing a breach) and a drawback (more complex to manage)."),
    think([("Why should a firewall filter outbound traffic as well as inbound?", "Malware already inside may try to send data out or contact its controller; outbound rules can block this."),
           ("Why put a public web server in a DMZ rather than on the internal LAN?", "If the web server is hacked, the attacker is still separated from the internal network by the firewall.")]),
)


# ---------- C1 CIA triad ----------
def cia_fig():
    s = SVG(760, 290, "The CIA triad")
    s.poly([(380, 70), (170, 230), (590, 230)], fill="#f6f9fc", stroke=LINE, width=2)
    s.box(290, 40, 180, 60, "Confidentiality", "only authorised people", size=14, fill=BLUEBG, bold=True)
    s.box(80, 200, 180, 60, "Integrity", "not tampered with", size=14, fill=AMBERBG, bold=True)
    s.box(500, 200, 180, 60, "Availability", "there when needed", size=14, fill=GREENBG, bold=True)
    s.text(380, 160, "DATA", size=18, bold=True)
    s.text(210, 150, "access control", size=11, color=ARROW)
    s.text(210, 166, "protects integrity", size=11, color=ARROW)
    s.text(550, 150, "correct data is", size=11, color=ARROW)
    s.text(550, 166, "useful data", size=11, color=ARROW)
    s.text(380, 282, "Weakening one side weakens the others.", size=12, color=ACCENT)
    return s.render("Confidentiality, integrity and availability depend on each other.")


C1 = lesson("C1", "8.4 Effective security", "The CIA triad",
    "explain confidentiality, integrity and availability and how they interrelate.", spec("8.4.1"),
    cia_fig(),
    table(["Element", "Meaning", "Controls", "Example of failure"], [
        ["Confidentiality", "data is kept private by controlling who has access", "access control, encryption, MFA", "a leaked customer list"],
        ["Integrity", "data has not been tampered with; maintained partly by keeping it confidential (fewer people can change it)", "hashing, permissions, audit logs, validation", "an attacker changes bank details on invoices"],
        ["Availability", "data is available and useful when needed; useful only if its integrity is intact", "backups, redundancy, DDoS protection, patching", "ransomware or a DDoS takes a service offline"],
    ], caption="8.4.1 The three elements"),
    p("The elements <strong>interrelate</strong>: controlling access (confidentiality) protects integrity, because fewer people can alter the data. Integrity supports availability, because data that is available but wrong is not useful. Too much confidentiality can harm availability, e.g. so many locks that staff cannot reach what they need, so security is always a balance."),
    terms([("Confidentiality", "only authorised users can access data."), ("Integrity", "data is accurate and unaltered."), ("Availability", "authorised users can access data when needed."), ("Trade-off", "strengthening one element may weaken another.")]),
    exam_tip("When given an incident, name which element(s) of CIA were affected. Ransomware hits <em>availability</em> (and integrity); a leak hits <em>confidentiality</em>; altered records hit <em>integrity</em>."),
    think([("Explain how maintaining confidentiality helps integrity.", "If only authorised people can access the data, fewer people are able to change it, so it is less likely to be tampered with."),
           ("A hospital locks down its records so tightly that doctors cannot open them in an emergency. Which element suffers?", "Availability: the data is not available to authorised users when needed.")]),
)


# ---------- C2 IAAA ----------
def iaaa_fig():
    s = SVG(760, 200, "The IAAA model")
    st = [("Identification", "Who do you claim to be?", "username, card, face", BLUEBG), ("Authentication", "Prove it", "password + app code, fingerprint", AMBERBG), ("Authorisation", "What may you do?", "role, access control list", GREENBG), ("Accountability", "What did you do?", "audit logs, user activity", "#f3e8f9")]
    for i, (a, b, c, f) in enumerate(st):
        x = 12 + i * 187
        s.box(x, 30, 172, 110, fill=f)
        s.text(x + 86, 58, a, size=15, bold=True)
        s.text(x + 86, 84, b, size=12, italic=True)
        s.text(x + 86, 116, c, size=11, color=ARROW)
        if i:
            s.arrow(x - 15, 85, x - 1, 85, width=1.6)
    s.text(380, 180, "Example: log in as jsmith → enter password and app code → HR role opens HR folders only → every file opened is logged", size=12, color=ACCENT)
    return s.render("Identification, authentication, authorisation and accountability work in order every time someone uses a system.")


C2 = lesson("C2", "8.4 Effective security", "Identification, authentication, authorisation and accountability (IAAA)",
    "explain the elements of the IAAA model and the techniques used, with their benefits and drawbacks.", spec("8.4.2"),
    iaaa_fig(),
    table(["Element", "Techniques", "Benefits", "Drawbacks"], [
        ["Identification: recognising the individual", "knowledge-based (username); possession-based (ID card, key fob); biometric (face, fingerprint)", "simple and quick", "a username alone proves nothing; cards can be lost or stolen"],
        ["Authentication: verifying the claimed identity", "passwords and passphrases; MFA; biometric authentication", "MFA and biometrics are hard to fake", "passwords are forgotten or guessed; biometrics cannot be changed if stolen; cost of readers"],
        ["Authorisation: only permitted resources and actions", "role-based access control (RBAC); access control lists (ACLs)", "least privilege; easy to manage by role", "roles must be kept up to date; ACL mistakes grant too much"],
        ["Accountability: actions traced to a user", "audit logs; monitoring user activity", "deters misuse; evidence for investigations", "logs need storage and review; privacy concerns"],
    ], caption="8.4.2 The IAAA model"),
    cli(["$ ls -l /srv/hr", "-rw-r----- 1 jsmith  hr  4096 salaries.xlsx", "$ sudo usermod -aG hr akhan     # authorise: add a user to the hr group", "$ sudo last -n 5                 # accountability: recent logins"], "Linux permissions (authorisation) and login history (accountability), from the Linux commands practical."),
    real_world("shared logins", "A shop’s staff all use one shared till login. When money goes missing there is no way to know who processed which refund. Individual accounts (identification), PINs (authentication), refund rights for managers only (authorisation) and a transaction log (accountability) fix every stage."),
    terms([("Identification", "claiming an identity, e.g. entering a username."), ("Authentication", "proving the identity claimed."), ("Authorisation", "granting the permissions that identity is allowed."), ("Accountability", "tracing actions back to the user responsible.")]),
    exam_tip("Do not mix up authentication (proving who you are) and authorisation (what you may do). Shared accounts break accountability, which is a common exam scenario."),
    think([("Why are shared user accounts a problem for accountability?", "Audit logs can only record the shared account, so actions cannot be traced to one person."),
           ("Give one benefit and one drawback of role-based access control.", "Benefit: permissions are set once per role and applied to everyone in it. Drawback: if someone changes job and their role is not updated, they keep access they no longer need.")]),
)

LESSONS = [M1, M2, M3, M4, M5, C1, C2]
