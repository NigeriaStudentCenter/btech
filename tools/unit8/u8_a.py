"""Unit 8 Security (T Level core content area 8): lessons for 8.1 and 8.2 (original content)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "unit19"))
sys.path.insert(0, str(HERE.parent / "deeper"))
from u19 import *  # noqa  lesson, device, cli, SVG, p, h3, table, terms, think, worked, real_world, ul
from u19 import SVG, device, esc, INK, LINE, ARROW, ACCENT, WARN

RED, REDBG, AMBERBG, BLUEBG, GREENBG, GREEN = "#b03a2e", "#fbe3d4", "#fbf0dd", "#dcebf6", "#e8f1e4", "#2f7d4f"


def exam_tip(text):
    return f'<div class="assess"><h4>Exam focus</h4><p>{text}</p></div>'


def practical(title, steps, note=None):
    li = "".join(f"<li>{s}</li>" for s in steps)
    n = f'<p class="small">{note}</p>' if note else ""
    return f'<div class="tryit"><h4>Practical: {esc(title)}</h4><ol>{li}</ol>{n}</div>'


def ethics(text):
    return f'<div class="warnbox"><strong>Stay legal and ethical.</strong> {text}</div>'


def spec(code):
    return f"T Level core · {code}"


# ---------- S1 8.1 Security risks ----------
def info_fig():
    s = SVG(760, 250, "Confidential information held by an organisation")
    cols = [("Human resources", BLUEBG, ["salaries and benefits", "staff personal details"]),
            ("Commercially sensitive", AMBERBG, ["client details", "stakeholder details", "intellectual property", "sales numbers", "contracts"]),
            ("Access information", REDBG, ["usernames, passwords", "passphrases, PINs", "access codes", "MFA details", "biometric data"])]
    for i, (h, f, items) in enumerate(cols):
        x = 20 + i * 245
        s.box(x, 20, 230, 40, h, size=15, fill=f, bold=True)
        for k, t in enumerate(items):
            s.box(x + 15, 72 + k * 34, 200, 28, t, size=12, fill="white", rx=5)
    return s.render("Three kinds of confidential information. Access information is the key to all the rest: if it leaks, attackers can reach everything else.")


def impact_fig():
    s = SVG(760, 230, "What happens when confidentiality fails")
    s.box(290, 85, 180, 60, "Data breach", "confidential data leaks", size=15, fill=REDBG, bold=True)
    effects = [("Non-compliance", "fines, loss of licence to practise"), ("Loss of trust", "clients and staff leave"), ("Damaged image", "bad press, fewer customers"),
               ("Financial loss", "fines, refunds, lost contracts"), ("Legal action", "clients and regulators sue"), ("Reduced security", "leaked logins open more doors")]
    for i, (a, b) in enumerate(effects):
        col, row = i // 3, i % 3
        x, y = (20, 510)[col], 20 + row * 68
        s.box(x, y, 230, 56, a, b, size=14, fill=AMBERBG if col == 0 else "#f3e8f9")
        if col == 0:
            s.arrow(290, 115, 252, y + 28, width=1.4, color="#8aa5b8")
        else:
            s.arrow(470, 115, 508, y + 28, width=1.4, color="#8aa5b8")
    return s.render("One leak can trigger several impacts at once: regulatory, reputational, financial and legal.")


S1 = lesson("S1", "8.1 Security risks", "Confidential information and why it must be protected",
    "identify the confidential information organisations hold, explain why each type must be kept confidential, and describe the impact of failing to do so.", spec("8.1.1 – 8.1.3"),
    p("Every organisation holds information that would cause harm if the wrong people saw it. Security starts with knowing <strong>what</strong> you are protecting and <strong>why</strong>."),
    info_fig(),
    table(["Information", "Why keep it confidential?"], [
        ["Salaries and benefits", "stops competitors offering higher wages to poach staff; stops staff comparing pay and demanding the same"],
        ["Staff personal details", "protects their privacy (a legal duty); stops competitors contacting them directly"],
        ["Intellectual property", "stops competitors copying designs, code, recipes or processes"],
        ["Client details", "stops competitors contacting clients; protects clients’ privacy"],
        ["Sales numbers and contracts", "competitors could undercut prices or target weak areas"],
        ["Access information", "prevents unauthorised access to systems, buildings and all the other data"],
    ], caption="8.1.2 Reasons for confidentiality"),
    impact_fig(),
    table(["Impact (8.1.3)", "Example"], [
        ["Non-compliance with regulations", "a data protection breach leads to a regulator’s fine; a solicitor or pharmacy could lose its licence to practise"],
        ["Loss of trust and damaged image", "customers read about the leak and move to a competitor"],
        ["Financial loss", "fines, refunds to customers, lost earnings, contracts terminated"],
        ["Legal action", "customers or partners sue for damages"],
        ["Reduced security", "leaked passwords let attackers back in, or are reused on other systems"],
    ], caption="Impacts of failing to keep information confidential"),
    real_world("a leaked customer database", "An online retailer stores customer names, addresses and card details. An attacker copies the database. The retailer must tell the regulator and its customers, pays refunds and a fine, loses customers who no longer trust it, and faces legal claims. The leaked passwords are tried on other websites, where many customers reused them."),
    terms([("Confidential", "information only authorised people should see."), ("Intellectual property", "original designs, code, inventions and ideas owned by the organisation."), ("Biometric data", "physical characteristics used for identification, e.g. fingerprints or face."), ("Data breach", "confidential data being accessed, leaked or stolen.")]),
    exam_tip("Link each type of information to a <em>specific</em> reason and impact. “Client details must be confidential so competitors cannot contact the clients and so the firm complies with data protection law” scores more than “it’s private”."),
    think([("Why is access information described as the ‘key’ to other confidential information?", "Usernames, passwords, PINs and MFA details let someone log in or enter a building, so leaking them exposes every system and file those accounts can reach."),
           ("A marketing agency’s client list leaks. Give two impacts.", "Competitors can approach the clients and win their business (financial loss); clients lose trust in the agency; possible fines for breaching data protection.")]),
)


# ---------- T1 malware, botnets, DoS ----------
def botnet_fig():
    s = SVG(760, 310, "A botnet launching a DDoS attack")
    s.box(20, 120, 130, 56, "Attacker", "bot herder", size=14, fill=REDBG, bold=True)
    s.box(190, 120, 130, 56, "Command and", "control server", size=13, fill="#f3e8f9")
    s.arrow(150, 148, 188, 148, width=1.8)
    for i in range(5):
        y = 20 + i * 56
        device(s, "pc", 380, y - 4, w=54)
        s.text(460, y + 22, f"infected bot {i + 1}", size=11, anchor="start")
        s.line(320, 148, 382, y + 16, color="#b98ab8", width=1.4)
        s.arrow(540, y + 16, 618, 148, color=RED, width=1.4)
    device(s, "server", 625, 124, w=70)
    s.text(660, 190, "target website", size=12, bold=True)
    s.text(660, 208, "overwhelmed", size=12, color=RED)
    s.text(380, 300, "The owners of the bots usually do not know their devices are infected.", size=12, color=ARROW)
    return s.render("A botnet is a network of infected devices controlled remotely. Together they can flood a target with traffic (DDoS), send spam or crack passwords.")


T1 = lesson("T1", "8.2 Types of threats and vulnerabilities", "Malware, botnets and denial of service",
    "explain types of malware, botnets and DoS/DDoS attacks, their impacts, and how to prevent and mitigate them.", spec("8.2.1"),
    table(["Malware", "What it does", "Prevention and mitigation"], [
        ["Virus", "attaches to a file or program; spreads when the file is run and shared", "anti-malware, do not open unknown files, updates"],
        ["Worm", "spreads by itself across a network through unpatched weaknesses", "patching, firewalls, network segregation"],
        ["Keylogger", "records keystrokes to steal passwords and card numbers", "anti-malware, MFA (a stolen password alone is not enough)"],
        ["Ransomware", "encrypts files and demands payment for the key", "offline/offsite backups, patching, staff training, least privilege"],
        ["Spyware", "secretly monitors activity and sends data to the attacker", "anti-malware, app permissions, trusted sources only"],
        ["Remote access trojan (RAT)", "disguised as useful software; gives the attacker hidden remote control", "download from trusted sources, anti-malware, outbound firewall rules"],
    ], caption="Types of malware"),
    botnet_fig(),
    table(["Attack", "What happens", "Impact", "Prevention and mitigation"], [
        ["Denial of service (DoS)", "one machine floods a server with requests", "website or service unavailable; lost sales", "firewall rules, rate limiting, blocking the source IP"],
        ["Distributed DoS (DDoS)", "a botnet of thousands of devices floods the target at once", "much harder to block: traffic comes from everywhere", "DDoS protection services, extra capacity (cloud), traffic filtering"],
        ["Botnet", "infected devices controlled together", "owners’ devices slow; used for DDoS, spam, password cracking", "anti-malware, patching, change default IoT passwords"],
    ], caption="Botnets and denial of service"),
    real_world("WannaCry, 2017", "A ransomware worm spread worldwide through an unpatched weakness in older Windows systems. It encrypted files in organisations including hospitals, where appointments and operations had to be cancelled. Patching and good backups would have limited the damage."),
    terms([("Malware", "malicious software designed to damage, disrupt or gain access."), ("Payload", "the harmful action malware carries out."), ("Botnet", "a network of infected devices controlled by an attacker."), ("DDoS", "a denial of service attack from many devices at once.")]),
    exam_tip("For each threat, learn three things: what it is, its impact, and how to prevent <em>and</em> mitigate it. Prevention stops it happening; mitigation reduces the damage when it does (e.g. backups for ransomware)."),
    think([("Why is a DDoS attack harder to stop than a DoS attack?", "The traffic comes from thousands of different IP addresses, so blocking one source does not help and it is hard to tell attack traffic from real users."),
           ("How do backups mitigate ransomware?", "If clean copies are stored offline or offsite, the organisation can restore its files without paying, reducing downtime and data loss.")]),
)


# ---------- T2 malicious hacking ----------
def sqli_fig():
    s = SVG(760, 250, "How SQL injection changes a query")
    s.box(20, 20, 250, 110, fill="#f6f9fc")
    s.text(145, 42, "Login form", size=14, bold=True)
    s.box(40, 55, 210, 28, "' OR '1'='1", size=13, fill="white", rx=4)
    s.text(40, 100, "Username field: the attacker types", size=11, anchor="start", color=ARROW)
    s.text(40, 116, "SQL code instead of a name", size=11, anchor="start", color=ARROW)
    s.arrow(275, 75, 318, 75, width=1.8)
    s.box(320, 20, 420, 110, fill="#fdf5f3", stroke=RED)
    s.text(530, 44, "Query the website builds", size=13, bold=True)
    s.text(335, 72, "SELECT * FROM users", size=13, anchor="start", mono=True)
    s.text(335, 94, "WHERE name = '' OR '1'='1'", size=13, anchor="start", mono=True, color=RED)
    s.text(335, 118, "'1'='1' is always true, so every row matches", size=12, anchor="start", color=RED)
    s.box(20, 160, 720, 70, fill=GREENBG, stroke=GREEN)
    s.text(380, 186, "Prevention: parameterised queries (input is treated as data, never as code),", size=13)
    s.text(380, 208, "input validation, least-privilege database accounts, web application firewall", size=13)
    return s.render("SQL injection: the website pastes user input straight into a database command, so the attacker’s input becomes part of the command.")


def brute_fig():
    s = SVG(760, 240, "How password length affects brute-force time")
    rows = [("6 lower-case letters", 26 ** 6, "309 million"), ("8 lower-case letters", 26 ** 8, "209 billion"), ("8 mixed characters (94)", 94 ** 8, "6 quadrillion"), ("4 random words (7,776 each)", 7776 ** 4, "3.7 quadrillion"), ("12 mixed characters", 94 ** 12, "476 sextillion")]
    import math
    mx = math.log10(94 ** 12)
    for i, (a, n, lab) in enumerate(rows):
        y = 20 + i * 40
        s.text(20, y + 20, a, size=12, anchor="start")
        w = 360 * math.log10(n) / mx
        s.add(f'<rect x="230" y="{y + 6}" width="{w:.0f}" height="20" rx="3" fill="{RED if i < 2 else ACCENT if i < 4 else GREEN}"/>')
        s.text(236 + w, y + 21, lab + " combinations", size=11, anchor="start")
    s.text(380, 228, "Bar length is on a log scale: each extra character multiplies the work.", size=12, color=ARROW)
    return s.render("Brute force tries every combination. Length adds far more protection than complexity alone, which is why long passphrases are recommended.")


def overflow_fig():
    s = SVG(760, 170, "A buffer overflow")
    s.text(20, 26, "Memory set aside for an 8-character name:", size=13, anchor="start")
    for k in range(8):
        s.box(20 + k * 52, 40, 50, 36, "A", size=14, fill=BLUEBG, rx=3)
    for k, t in enumerate(["A", "A", "A", "A"]):
        s.box(436 + k * 52, 40, 50, 36, t, size=14, fill=REDBG, stroke=RED, rx=3)
    s.text(540, 100, "overwrites the next memory:", size=12, color=RED)
    s.text(540, 118, "e.g. where the program jumps next", size=12, color=RED)
    s.text(20, 150, "Prevention: check input length (bounds checking), safe languages and functions, updates and patches", size=12, anchor="start", color=GREEN)
    return s.render("If a program does not check input length, extra data spills into neighbouring memory. Attackers use this to crash the program or run their own code.")


T2 = lesson("T2", "8.2 Types of threats and vulnerabilities", "Malicious hacking",
    "explain who malicious hackers are and how password cracking, brute force, cross-site scripting, SQL injection and buffer overflow attacks work and are prevented.", spec("8.2.1"),
    table(["Hacker", "Usual motive"], [
        ["Hacktivists", "a political or social cause: defacing websites, leaking data to make a point"],
        ["Nation states", "spying, disrupting another country’s infrastructure, stealing research"],
        ["Organised crime", "money: ransomware, stolen card data, fraud"],
        ["Individuals", "curiosity, challenge, revenge (e.g. a sacked employee) or money"],
    ], caption="Who hacks, and why"),
    h3("Password cracking and brute force"),
    brute_fig(),
    p("<strong>Brute force</strong> tries every possible combination. <strong>Dictionary attacks</strong> try common words and leaked passwords first. <strong>Prevention:</strong> long passphrases, account lockout after failed attempts, MFA, and storing passwords as salted hashes."),
    h3("SQL injection"),
    sqli_fig(),
    h3("Cross-site scripting (XSS)"),
    p("The attacker gets a website to include their <strong>script</strong> in a page other people view, e.g. in a comment or search box. The script runs in victims’ browsers and can steal session cookies or redirect them. <strong>Prevention:</strong> validate input and encode output so text is displayed, never run; content security policies."),
    h3("Buffer overflow"),
    overflow_fig(),
    terms([("Brute force", "trying every possible password until one works."), ("SQL injection", "entering SQL code into an input to change a database query."), ("Cross-site scripting", "injecting a script into a web page that runs in other users’ browsers."), ("Buffer overflow", "writing more data than a memory area holds so it overwrites nearby memory.")]),
    exam_tip("Say how each attack works <em>and</em> give a matching prevention. SQL injection → parameterised queries and input validation; XSS → output encoding; buffer overflow → bounds checking and patches; brute force → length, lockout and MFA."),
    think([("Why does account lockout defeat online brute-force attacks?", "After a few wrong guesses the account locks or slows down, so the attacker cannot try millions of combinations."),
           ("A website search box shows whatever you type back on the page. Which attack could this allow and how is it prevented?", "Cross-site scripting: if the text is not encoded, a script typed in could run in visitors’ browsers. Encode output and validate input.")]),
)


# ---------- T3 social engineering ----------
def phish_fig():
    s = SVG(760, 300, "Spotting a phishing email")
    s.box(20, 20, 440, 260, fill="white", stroke=LINE)
    s.text(36, 46, "From: IT Support <support@micros0ft-help.co>", size=12, anchor="start", mono=True)
    s.text(36, 68, "Subject: URGENT: your account closes in 2 hours", size=12, anchor="start", bold=True)
    s.line(30, 80, 450, 80, color=LINE, width=1)
    s.text(36, 104, "Dear user,", size=12, anchor="start")
    s.text(36, 126, "We detected unusual sign-ins. Verify your", size=12, anchor="start")
    s.text(36, 146, "password now or lose all your files.", size=12, anchor="start")
    s.box(36, 164, 190, 32, "Verify my account", size=13, fill="#245d83", color="white", rx=5)
    s.text(36, 222, "Link goes to: http://micros0ft-login.xyz", size=11, anchor="start", mono=True, color=RED)
    s.text(36, 250, "Attachment: invoice.pdf.exe", size=11, anchor="start", mono=True, color=RED)
    flags = [(46, "Look-alike sender address (0 for o)"), (68, "Urgency and threats"), (104, "Generic greeting, not your name"), (180, "Button hides the real link"), (222, "Unfamiliar web address"), (250, "Double extension: really a program")]
    for y, t in flags:
        s.arrow(470, y - 4, 488, y - 4, color=RED, width=1.4, both=False)
        s.text(494, y, t, size=12, anchor="start", color=RED)
    return s.render("Red flags in a phishing email. Real organisations do not ask you to confirm your password through a link.")


T3 = lesson("T3", "8.2 Types of threats and vulnerabilities", "Social engineering",
    "explain phishing, spear phishing, smishing, vishing, pharming, watering hole attacks and USB baiting, and how to prevent them.", spec("8.2.1"),
    p("<strong>Social engineering</strong> tricks people, rather than computers, into giving away information or access. It works because it exploits trust, fear, curiosity and urgency."),
    phish_fig(),
    table(["Attack", "How it works", "Prevention"], [
        ["Phishing", "mass emails pretending to be a trusted organisation, linking to fake login pages", "staff training, email filtering, MFA, report suspicious emails"],
        ["Spear phishing", "a targeted email using personal details (name, manager, project) to look genuine", "training, verify unusual requests by another channel"],
        ["Smishing", "phishing by SMS text message, e.g. a fake parcel delivery link", "do not click links in texts; go to the official app or site"],
        ["Vishing", "phone calls pretending to be the bank, IT support or police", "call back on a known number; never give passwords or PINs"],
        ["Pharming", "redirects a correct web address to a fake site (malware or DNS changes)", "check for HTTPS and the correct address, anti-malware, secure DNS"],
        ["Watering hole", "infects a website the target group often visits", "patching, browser security, anti-malware"],
        ["USB baiting", "leaves infected USB sticks for people to find and plug in", "policy: never plug in unknown devices; disable USB auto-run"],
    ], caption="Types of social engineering"),
    real_world("the fake invoice", "A finance assistant receives an email that appears to come from the managing director, asking for an urgent payment to a new supplier. The address is one letter different. Because the college’s policy says all new bank details must be confirmed by phone, the assistant calls the director and the fraud is stopped."),
    terms([("Social engineering", "manipulating people into revealing information or giving access."), ("Spear phishing", "phishing aimed at a specific person or organisation."), ("Pharming", "redirecting users from a real website to a fake one."), ("Watering hole attack", "compromising a website that the targets are known to visit.")]),
    exam_tip("Staff training is the main defence against social engineering, but the best answers pair it with a technical control, e.g. training <em>and</em> MFA, so a stolen password alone is useless."),
    think([("Why is spear phishing more successful than ordinary phishing?", "It uses personal, accurate details, so the message looks genuine and the victim is less suspicious."),
           ("How does pharming differ from phishing?", "Phishing tricks you into clicking a fake link; pharming sends you to a fake site even when you type the correct address.")]),
)


# ---------- T4 network and Wi-Fi attacks ----------
def mitm_fig():
    s = SVG(760, 220, "A man-in-the-middle attack on open Wi-Fi")
    device(s, "laptop", 30, 60, "Customer")
    device(s, "ap", 230, 20, "Fake ‘Cafe_Free_WiFi’", w=70)
    s.box(200, 110, 130, 50, "Attacker", "reads and alters traffic", size=13, fill=REDBG, bold=True)
    device(s, "server", 520, 60, "Bank website", w=70)
    s.arrow(100, 82, 225, 50, width=1.6, color=RED)
    s.arrow(300, 50, 518, 82, width=1.6, color=RED)
    s.line(265, 88, 265, 108, color=RED, width=1.6, dash=True)
    s.box(380, 150, 360, 56, "Protection: HTTPS/TLS everywhere, VPN on public", "Wi-Fi, check certificate warnings, WPA3/WPA2", size=12, fill=GREENBG, stroke=GREEN)
    return s.render("In a man-in-the-middle attack, traffic passes through the attacker, who can read or change it. Open Wi-Fi and fake access points make this easy.")


T4 = lesson("T4", "8.2 Types of threats and vulnerabilities", "DNS attacks, insecure APIs, man-in-the-middle and open Wi-Fi",
    "explain DNS attacks and traffic redirection, insecure APIs, man-in-the-middle attacks and open Wi-Fi, with prevention and mitigation.", spec("8.2.1"),
    mitm_fig(),
    table(["Threat", "How it works", "Impact", "Prevention and mitigation"], [
        ["DNS attack / redirection", "the attacker changes DNS records or poisons a DNS cache so a real name points to a fake IP address", "users land on fake sites and type their passwords (pharming)", "secure DNS (DNSSEC), patch DNS servers, protect registrar accounts with MFA, HTTPS certificate checks"],
        ["Insecure API", "an application programming interface with weak authentication, no rate limits or too much data returned", "attackers pull or change data directly, bypassing the app", "authentication tokens, access control, rate limiting, input validation, API testing and certification"],
        ["Man-in-the-middle", "the attacker sits between two parties and intercepts or alters traffic", "stolen logins, altered payments", "encryption (HTTPS/TLS), VPNs, certificate checks, MFA"],
        ["Open / unsecured Wi-Fi", "no encryption, or a fake hotspot set up by an attacker", "traffic can be read; devices can be attacked", "use a VPN, only HTTPS sites, WPA2/WPA3 on your own networks, turn off auto-connect"],
    ], caption="Network and web threats"),
    terms([("DNS", "the system that turns domain names into IP addresses."), ("API", "a set of rules that lets one program request data or services from another."), ("Man-in-the-middle", "an attacker secretly relaying and possibly altering communication."), ("Rate limiting", "restricting how many requests a user can make in a period.")]),
    exam_tip("These threats all attack data <em>in transit</em>. Encryption (HTTPS/TLS, VPN) is the common defence; add a specific one for each (DNSSEC for DNS, authentication and rate limits for APIs)."),
    think([("Why does a VPN protect you on public Wi-Fi?", "It encrypts all traffic between your device and the VPN server, so anyone intercepting it on the Wi-Fi network sees only scrambled data."),
           ("An app’s API returns every customer record if you change a number in the request. What is the weakness?", "Missing authorisation/access control: the API does not check that the user may see that record. Fix with proper access checks and testing.")]),
)


# ---------- V1 technical vulnerabilities ----------
def zeroday_fig():
    s = SVG(760, 200, "The life of a software vulnerability")
    stages = [("Bug in code", "unknown to anyone", BLUEBG), ("Discovered by attacker", "zero-day: no patch yet", REDBG), ("Vendor releases patch", "fix available", AMBERBG), ("Patch installed", "gap closed", GREENBG)]
    for i, (a, b, f) in enumerate(stages):
        x = 20 + i * 185
        s.box(x, 40, 165, 60, a, b, size=13, fill=f)
        if i:
            s.arrow(x - 20, 70, x - 2, 70, width=1.8)
    s.add(f'<rect x="205" y="115" width="535" height="16" rx="4" fill="{RED}" opacity=".85"/>')
    s.text(470, 150, "Window of risk: from discovery until the patch is installed on YOUR systems", size=12, color=RED)
    s.text(380, 180, "Unsupported (end-of-life) software never gets the patch, so the window never closes.", size=12, color=ARROW)
    return s.render("Out-of-date components leave the window of risk open. Updating quickly shortens it.")


V1 = lesson("V1", "8.2 Types of threats and vulnerabilities", "Technical vulnerabilities",
    "explain how inadequate security processes and out-of-date hardware, software and firmware make systems vulnerable.", spec("8.2.2"),
    p("A <strong>threat</strong> is something that could cause harm. A <strong>vulnerability</strong> is a weakness a threat can exploit. Attackers look for the easiest weakness."),
    table(["Vulnerability", "Why it is a weakness"], [
        ["Weak encryption", "old or short-key algorithms can be broken, so ‘protected’ data can be read"],
        ["Inadequate password policy", "short, reused or default passwords are guessed or cracked quickly"],
        ["Failure to use MFA", "one stolen password is enough to log in"],
        ["Out-of-date hardware", "no longer supported; may not run current security software or updates"],
        ["Out-of-date software", "lack of support means no patches; legacy systems may be kept for compatibility; zero-day bugs are exploited before a fix exists"],
        ["Out-of-date firmware", "routers, cameras and printers with old firmware have well-known weaknesses and default logins"],
    ], caption="8.2.2 Technical vulnerabilities"),
    zeroday_fig(),
    real_world("the forgotten camera", "An office installs an internet-connected camera and never changes its default password or updates its firmware. Attackers scanning the internet find it, log in, and use it as a way into the office network."),
    terms([("Vulnerability", "a weakness that could be exploited."), ("Zero-day", "a vulnerability attackers exploit before a patch exists."), ("Legacy system", "old software or hardware still in use, often because other systems depend on it."), ("Firmware", "software stored in a device’s hardware that controls it.")]),
    exam_tip("Explain the chain: vulnerability → how a threat exploits it → impact → fix. For legacy systems, recognise the trade-off: replacing them costs money and may break compatibility, so isolate them if they must stay."),
    think([("Why might an organisation keep using unsupported software, and how can it reduce the risk?", "Other systems depend on it or replacement is expensive. Reduce risk by isolating it on a separate network segment, restricting access and planning a replacement."),
           ("What is a zero-day vulnerability?", "A weakness unknown to the vendor, or with no patch yet, that attackers exploit immediately.")]),
)


# ---------- V2 human threats ----------
V2 = lesson("V2", "8.2 Types of threats and vulnerabilities", "Human threats",
    "explain human error, malicious employees, disguised criminals and poor cyber hygiene, with prevention and mitigation methods.", spec("8.2.3"),
    p("Many incidents start with a person, not a piece of technology. Some are accidents; some are deliberate."),
    table(["Human threat", "Example", "Prevention and mitigation"], [
        ["Human error", "emailing a spreadsheet to the wrong person; deleting a shared folder", "file properties (read-only, permissions), confirmation boxes before deleting or sending, staff training"],
        ["Malicious employee", "a sacked employee copies client data or deletes files", "immediate removal from the premises, suspend user accounts immediately, least privilege, audit logs"],
        ["Disguised criminal", "someone in a hi-vis jacket claims to be ‘from IT’ and walks to the server room", "accompany all visitors, check identification, visitor badges and sign-in"],
        ["Poor cyber hygiene", "unlocked PCs, passwords on sticky notes, the same password everywhere", "lock all unattended machines, do not write passwords down, password managers, training"],
    ], caption="8.2.3 Human threats"),
    real_world("the unlocked screen", "A receptionist leaves the desk without locking the PC. A visitor opens the customer booking system and photographs a screen of personal details. A short lock-screen timeout and the habit of pressing Windows+L would have prevented it."),
    terms([("Insider threat", "a risk from someone inside the organisation."), ("Cyber hygiene", "everyday habits that keep systems secure."), ("Least privilege", "giving users only the access they need for their job."), ("Tailgating", "following an authorised person through a secure door.")]),
    exam_tip("Match the control to the threat: a malicious employee is stopped by <em>removing access at once</em>; human error by <em>confirmation boxes and file properties</em>; a disguised criminal by <em>ID checks and escorts</em>."),
    think([("Why must a dismissed employee’s account be suspended immediately?", "Until it is disabled they could still log in remotely and copy, change or delete data."),
           ("Give two good cyber hygiene habits.", "Lock the screen when leaving the desk; use unique passphrases stored in a password manager rather than written down.")]),
)


# ---------- V3 physical vulnerabilities and impact ----------
def layers_fig():
    s = SVG(760, 320, "Layers of physical security")
    rings = [(360, 150, 340, 135, "#eef4fa", "Outer perimeter: fence, gates, lighting, CCTV, car park barriers"), (360, 160, 250, 95, "#fbf0dd", "Building: entry control, reception, visitor badges"),
             (360, 170, 150, 55, "#fbe3d4", "Secure area: server room, swipe + PIN, audit")]
    for cx, cy, rx, ry, f, t in rings:
        s.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{f}" stroke="{LINE}" stroke-width="2"/>')
    s.text(360, 50, rings[0][5], size=12)
    s.text(360, 100, rings[1][5], size=12)
    s.text(360, 150, "Server room", size=14, bold=True)
    s.text(360, 170, "swipe card + PIN", size=12)
    s.text(360, 188, "access logged and audited", size=12)
    s.text(360, 312, "An intruder has to beat every layer: defence in depth.", size=12, color=ARROW)
    return s.render("Physical security in layers, from the site boundary to the server room.")


V3 = lesson("V3", "8.2 Types of threats and vulnerabilities", "Physical vulnerabilities and the impact of threats",
    "explain physical vulnerabilities and their prevention, and the potential impact of threats and vulnerabilities on an organisation.", spec("8.2.4 · 8.2.5"),
    layers_fig(),
    table(["Physical vulnerability", "Prevention and mitigation"], [
        ["Lack of access control", "entry control systems: swipe cards, key fobs, keypads, biometric locks"],
        ["Poor access control", "do not allow tailgating; use complex access codes and change them regularly; monitor access areas (CCTV, guards); audit staff access to secure areas"],
        ["Nature of location", "protect against shoulder surfing (privacy screens, screen position); protect against the environment (flood, heat, dust: raised floors, air conditioning); protect against vandalism (locked cabinets, alarms)"],
        ["Poor system robustness", "rugged machines for harsh environments such as building sites, factories and vehicles"],
        ["Natural disasters", "offsite backups and a disaster recovery site; choose locations away from flood risk"],
    ], caption="8.2.4 Physical vulnerabilities"),
    table(["Impact (8.2.5)", "Example"], [
        ["Loss or leaking of sensitive data", "a stolen laptop holds unencrypted client files"],
        ["Unauthorised access to digital systems", "a tailgater plugs a device into an office network port"],
        ["Data corruption", "a power cut or flood damages a server and its data"],
        ["Disruption of service", "ransomware or a fire stops the business trading"],
        ["Unauthorised access to restricted areas", "an intruder reaches the server room or stock room"],
    ], caption="Impact of threats and vulnerabilities"),
    practical("perimeter security proposal", ["You are the design architect for a warehouse with a customer entrance, staff door and loading bays.", "Define its outer perimeter, inner perimeter and interior areas, and one key vulnerability for each.", "Recommend access-control and monitoring devices (barriers, swipe entry, CCTV, lighting) with approximate costs.", "Present your solution in no more than five slides."], "Based on your teacher’s Perimeter Security activity worksheet."),
    terms([("Tailgating", "following an authorised person through a door without using your own access."), ("Shoulder surfing", "watching someone type a PIN or password."), ("Entry control system", "technology that decides who may enter an area, e.g. swipe cards."), ("Rugged machine", "a device built to survive drops, dust, water and extremes.")]),
    exam_tip("Physical security questions often give a floor plan or scenario. Work from the outside in (site, building, room, device) and give one vulnerability and one control for each layer."),
    think([("Why should door access codes be changed regularly?", "Codes get shared or observed over time; changing them removes access for people who should no longer have it."),
           ("A delivery driver follows staff through a secure door. Name the vulnerability and two controls.", "Tailgating (poor access control). Controls: staff training and a no-tailgating policy, turnstiles or airlock doors, CCTV monitoring.")]),
)

LESSONS = [S1, T1, T2, T3, T4, V1, V2, V3]
