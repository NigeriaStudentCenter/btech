from u19 import *


def lifecycle_fig():
    s = SVG(760, 170, "The network project cycle")
    steps = [("1 Requirements", "what the client\nneeds and why"), ("2 Design", "physical and\nlogical design"), ("3 Plan", "parts, configs,\ntest plan"), ("4 Build", "prototype in\nPacket Tracer"), ("5 Test", "against the\ntest plan"), ("6 Optimise", "fix and\nimprove"), ("7 Evaluate", "against the\nrequirements")]
    for i, (a, b) in enumerate(steps):
        x = 12 + i * 107
        s.box(x, 30, 96, 44, a, size=12, fill="#dcebf6" if i < 3 else "#e8f1e4" if i < 6 else "#fbf0dd", bold=True)
        s.text(x + 48, 96, b, size=11)
        if i < 6:
            s.arrow(x + 96, 52, x + 105, 52, width=1.6)
    s.text(380, 158, "Assignment 2 follows this cycle: design (B.P4) → build (C.P5) → test (C.P6) → optimise (C.M3) → review and evaluate (C.P7, BC.D2)", size=11, color=ACCENT)
    return s.render("Good networks are planned before they are built. Each stage produces evidence for your portfolio.")


def hier_fig():
    s = SVG(760, 330, "Flat and hierarchical network designs")
    s.text(160, 24, "Flat design", size=15, bold=True)
    device(s, "router", 130, 40, "")
    device(s, "switch", 130, 110, "")
    s.line(162, 84, 162, 120, color="#8aa5b8", width=2)
    for i in range(5):
        device(s, "pc", 20 + i * 58, 200, "")
        s.line(52 + i * 58, 200, 162, 146, color="#b9c7d5", width=1.6)
    s.text(160, 285, "cheap and simple; fine for a small office,", size=11)
    s.text(160, 300, "but hard to grow and one switch does everything", size=11)
    s.text(560, 24, "Hierarchical (three-layer) design", size=15, bold=True)
    s.text(372, 70, "Core", size=12, anchor="start", bold=True)
    s.text(372, 150, "Distribution", size=12, anchor="start", bold=True)
    s.text(372, 230, "Access", size=12, anchor="start", bold=True)
    core = [(510, 50), (610, 50)]
    dist = [(470, 130), (560, 130), (650, 130)]
    acc = [(440, 210), (500, 210), (560, 210), (620, 210), (680, 210)]
    for c in core:
        for d in dist:
            s.line(c[0] + 32, c[1] + 22, d[0] + 32, d[1] + 22, color="#8aa5b8", width=1.6)
    for i, a in enumerate(acc):
        s.line(a[0] + 32, a[1] + 22, dist[min(i // 2, 2)][0] + 32, dist[min(i // 2, 2)][1] + 22, color="#8aa5b8", width=1.6)
    for x, y in core:
        device(s, "switch", x, y)
    for x, y in dist:
        device(s, "switch", x, y)
    for x, y in acc:
        device(s, "switch", x, y)
    s.text(560, 285, "core: very fast backbone · distribution: routing, security, VLANs", size=11)
    s.text(560, 300, "access: where users plug in · duplicate links = redundancy", size=11)
    return s.render("A hierarchical design separates the network into layers, so it can grow and a fault stays in one area.")


B1a = lesson("B1a", "B1 Design strategies and architectures", "Design strategies: goals, size, aims and constraints",
    "explain why networks must be designed and planned, and use design aims to shape a design.", "Assignment 2 · B.P3, B.M2",
    lifecycle_fig(),
    h3("Start with the client, not the cables"),
    p("A network exists to support an organisation's <strong>business goals</strong> (for example: open a second office, sell online, let staff work from home). A designer turns these into <strong>technical requirements</strong>: how many users and devices, which applications and services, how fast, how secure, and how much downtime is acceptable. Designing and planning first means the network is right-sized, secure and within budget, the build goes smoothly, and there is documentation for the people who will support it later."),
    table(["Network size", "Typical users", "Typical design"], [
        ["SOHO (small office/home office)", "1–10", "one combined router/switch/AP, flat design, peer-to-peer or a small NAS"],
        ["SMB (small and medium-sized business)", "10–250", "server(s), managed switches, several APs, VLANs, a firewall, perhaps a branch link"],
        ["Large enterprise", "hundreds to thousands, many sites", "hierarchical campus design, redundant core, data centre or cloud, WAN to many branches"],
    ], caption="Network size shapes the design"),
    h3("Design aims"),
    table(["Aim", "Plain meaning", "How designers achieve it"], [
        ["Scalability", "it can grow without starting again", "spare switch ports, modular design, IP plan with room to spare"],
        ["Availability", "it is working when people need it", "reliable kit, UPS, monitoring, quick recovery"],
        ["Redundancy", "no single point of failure", "duplicate links, switches, power supplies, servers"],
        ["Performance", "fast enough for the applications", "right link speeds, switches not hubs, QoS for VoIP"],
        ["Security", "only the right people reach the right things", "firewall, strong Wi-Fi security, VLANs, permissions, passwords on devices"],
        ["Manageability", "easy to monitor, change and fix", "managed switches, naming scheme, documentation"],
        ["Adaptability", "copes with new technology and needs", "standards-based kit, wireless expansion, cloud options"],
        ["Affordability and maintainability", "costs fit the budget, now and later", "choose kit that meets the need without over-buying"],
    ], caption="Design aims for LANs and WANs"),
    p("Every design has <strong>constraints</strong> (budget, time, the building itself, skills available) and involves <strong>trade-offs</strong>: more redundancy costs more; more security can make things harder to use. A good design explains which trade-offs were made and why."),
    hier_fig(),
    real_world("a dental practice with two surgeries", "Business goals: book patients at either site and store X-rays securely. Technical requirements: 12 PCs, an X-ray workstation, a server for the booking database, Wi-Fi for staff tablets, a VPN link between the sites. Constraints: £8,000 budget, a listed building with thick walls, the work must be done over a weekend."),
    terms([
        ("Business goal", "what the organisation wants to achieve."),
        ("Technical requirement", "what the network must do or provide to meet the goals."),
        ("Constraint", "a limit the design must work within, such as budget or time."),
        ("Trade-off", "giving up some of one thing to gain another."),
        ("Redundancy", "extra, duplicate parts or paths so that one failure does not stop the network."),
    ]),
    assignment_link("B.P3 and B.M2", "Task 1 is an email to the customer explaining why designing and planning come before installing, and how this makes sure the network meets their needs and design goals. For Task 3 (Merit) justify each design decision by linking it to a customer requirement <em>and</em> a technical reason."),
    think([
        ("Why is 'we just plugged everything in' risky for a 50-person company?", "Without a plan the network may not have enough ports or bandwidth, may be insecure, may use conflicting IP addresses, and will have no documentation, so faults and future growth become expensive."),
        ("Give a trade-off between redundancy and cost.", "Two internet connections and duplicate switches keep the network running if one fails, but double the cost of that equipment and its running costs."),
    ]),
)


def and_fig():
    s = SVG(760, 230, "Finding the network address with ANDing")
    rows = [("IP address", "192.168.10.77", "11000000.10101000.00001010.01001101"),
            ("Subnet mask /26", "255.255.255.192", "11111111.11111111.11111111.11000000"),
            ("Network (AND)", "192.168.10.64", "11000000.10101000.00001010.01000000")]
    for i, (a, b, c) in enumerate(rows):
        y = 40 + i * 50
        s.text(20, y, a, size=13, anchor="start", bold=True)
        s.text(200, y, b, size=14, anchor="start", mono=True)
        s.text(360, y, c, size=13, anchor="start", mono=True, color=ACCENT if i == 2 else INK)
    s.line(360, 112, 740, 112, color=INK, width=1.5)
    s.text(380, 200, "1 AND 1 = 1, anything else = 0. The 1s in the mask mark the network part; the 0s mark the host part.", size=12)
    s.text(380, 220, "This host is in network 192.168.10.64/26; its broadcast address is 192.168.10.127.", size=12, color=ACCENT)
    return s.render("A device ANDs its IP address with its subnet mask to find out which network it belongs to.")


def nat_fig():
    s = SVG(760, 200, "Network address translation at the edge router")
    for i in range(3):
        device(s, "pc", 20, 20 + i * 60)
        s.text(96, 32 + i * 60, f"192.168.1.{10 + i}", size=12, anchor="start", mono=True)
        s.line(86, 44 + i * 60, 220, 44 + i * 60, color="#b9c7d5", width=1.6)
        s.line(220, 44 + i * 60, 330, 92, color="#b9c7d5", width=1.6)
    device(s, "router", 330, 70, "Edge router (NAT)")
    device(s, "cloud", 620, 60, "")
    s.arrow(396, 92, 616, 90, both=True, label="all appear as 81.2.69.160", ly=-10)
    s.text(360, 170, "private addresses inside", size=12, color=ARROW)
    s.text(620, 170, "one public address outside", size=12, color=ACCENT)
    return s.render("NAT lets a whole office share one public IPv4 address, and hides the private addresses from the internet.")


def vlan_fig():
    s = SVG(760, 220, "One switch split into VLANs")
    device(s, "switch", 340, 90, "")
    groups = [("VLAN 10 · Staff", "#dcebf6", [30, 110]), ("VLAN 20 · VoIP", "#e8f1e4", [290, 380]), ("VLAN 30 · Guest Wi-Fi", "#fbf0dd", [560, 650])]
    for name, fill, xs in groups:
        s.box(xs[0] - 10, 150, xs[1] - xs[0] + 84, 66, fill=fill, stroke=LINE, dash=True)
        s.text((xs[0] + xs[1]) / 2 + 32, 210, name, size=12, bold=True)
        for x in xs:
            device(s, "ipphone" if "VoIP" in name else "laptop" if "Guest" in name else "pc", x, 152)
            s.line(x + 32, 152, 372, 124, color="#b9c7d5", width=1.6)
    s.text(380, 40, "Devices in different VLANs cannot talk directly: traffic must go through a router or layer 3 switch,", size=12)
    s.text(380, 58, "where security rules can be applied. Broadcasts stay inside their own VLAN.", size=12)
    return s.render("VLANs create separate logical networks on the same physical switches: better security, less broadcast traffic, easier management.")


B1b = lesson("B1b", "B1 Logical network design", "IP addressing, subnets, IPv6, naming and VLANs",
    "plan an IP addressing scheme, choose between private/public and IPv4/IPv6, and use naming schemes and VLANs.", "Assignment 2 · B.P4",
    h3("IPv4 addresses and subnet masks"),
    p("An IPv4 address is 32 bits, written as four numbers from 0 to 255 (for example <code>192.168.10.77</code>). Part of it identifies the <strong>network</strong> and the rest identifies the <strong>host</strong> (device). The <strong>subnet mask</strong> (for example <code>255.255.255.0</code>, written <code>/24</code>) says where the split is. Every network has a <strong>network address</strong> (all host bits 0), a <strong>broadcast address</strong> (all host bits 1) and usable host addresses in between. The router's address on the LAN is the <strong>default gateway</strong>."),
    and_fig(),
    worked("Splitting one network into four subnets", [
        "A company has 192.168.10.0/24 (254 usable addresses) but wants four separate networks, one per department.",
        "Borrow 2 host bits: 2² = 4 subnets. The mask becomes /26 (255.255.255.192), leaving 6 host bits: 2⁶ − 2 = 62 usable hosts per subnet.",
        "Subnet 1: 192.168.10.0 to .63 (hosts .1 to .62). Subnet 2: .64 to .127 (hosts .65 to .126).",
        "Subnet 3: .128 to .191 (hosts .129 to .190). Subnet 4: .192 to .255 (hosts .193 to .254).",
        "Give the router the first usable address in each subnet (.1, .65, .129, .193) and reserve a few addresses for servers and printers before the DHCP pool.",
    ], "Usable hosts = 2^(host bits) − 2, because the network and broadcast addresses cannot be given to devices."),
    table(["Range", "Addresses", "Use"], [
        ["10.0.0.0/8", "10.0.0.0 – 10.255.255.255", "private: large organisations"],
        ["172.16.0.0/12", "172.16.0.0 – 172.31.255.255", "private: medium organisations"],
        ["192.168.0.0/16", "192.168.0.0 – 192.168.255.255", "private: homes and small offices"],
        ["127.0.0.0/8", "usually 127.0.0.1", "loopback: test the device's own network software"],
        ["169.254.0.0/16", "169.254.x.x", "self-assigned (APIPA): no DHCP server was found"],
    ], caption="Private and special IPv4 addresses"),
    p("<strong>Private</strong> addresses are used inside organisations and are free to use, but they cannot travel across the internet. <strong>Public</strong> addresses are unique worldwide and are supplied by an ISP. <strong>NAT</strong> joins the two."),
    nat_fig(),
    h3("IPv6"),
    p("IPv4 has only about 4.3 billion addresses, which have run out. <strong>IPv6</strong> uses 128-bit addresses written in hexadecimal, giving about 3.4 × 10³⁸ addresses, so NAT is not needed. Two rules shorten them: leave out leading zeros in each group, and replace one run of all-zero groups with <code>::</code>."),
    worked("Shortening an IPv6 address", [
        "Full: <code>2001:0db8:0000:0000:0000:ff00:0042:8329</code>",
        "Remove leading zeros: <code>2001:db8:0:0:0:ff00:42:8329</code>",
        "Replace the run of zero groups with a double colon (once only): <code>2001:db8::ff00:42:8329</code>",
    ]),
    table(["", "IPv4", "IPv6"], [
        ["Length", "32 bits", "128 bits"],
        ["Written as", "4 decimal numbers, e.g. 192.168.1.1", "8 groups of hex, e.g. 2001:db8::1"],
        ["Addresses", "about 4.3 billion", "about 340 undecillion"],
        ["NAT needed?", "usually", "no: every device can have a global address"],
        ["Automatic addressing", "DHCP", "SLAAC or DHCPv6"],
    ], caption="IPv4 and IPv6 compared"),
    h3("Naming schemes"),
    p("A naming scheme gives every device a predictable name that says what and where it is, which makes documentation, troubleshooting and scripts much easier. For example <code>LDN-FL2-SW01</code> (London, floor 2, switch 1), <code>LDN-SRV-DC01</code> (London, server, domain controller 1) or <code>BRN-PC-07</code>. Avoid personal names, because people move."),
    h3("VLANs"),
    vlan_fig(),
    p("VLAN design issues to consider: VLANs add complexity, need managed switches, need a router or layer 3 switch for traffic between them, and a misconfigured port can put a device in the wrong VLAN, which is a security risk."),
    terms([
        ("Subnet mask", "shows which part of an IP address is the network and which is the host."),
        ("Prefix length", "the mask written as the number of network bits, e.g. /24."),
        ("Default gateway", "the router address a device sends traffic to when it leaves the local network."),
        ("Subnetting", "dividing one network into smaller networks."),
        ("NAT", "network address translation: swaps private addresses for a public one at the edge."),
        ("VLAN", "virtual LAN: a separate logical network created on a switch."),
    ]),
    tryit("check your addressing plan", [
        "Build your design with one router interface per subnet.",
        "Give each router interface the first usable address of its subnet and <code>no shutdown</code> it.",
        "Give each PC an address, mask and default gateway from your table.",
        "Ping each gateway, then ping a PC in another subnet. If a ping fails, check the mask and gateway first.",
    ]),
    think([
        ("How many usable hosts does a /27 network have?", "32 − 27 = 5 host bits, so 2⁵ − 2 = 30 usable hosts."),
        ("A PC has 192.168.1.20/24 and gateway 192.168.2.1. What is wrong?", "The gateway is in a different network (192.168.2.x) from the PC (192.168.1.x). The gateway must be in the PC's own subnet, e.g. 192.168.1.1."),
        ("Why might an office put its VoIP phones in their own VLAN?", "Voice needs low delay. A separate VLAN can be given priority (QoS) and keeps phone traffic apart from ordinary data."),
    ]),
)


B2 = lesson("B2", "B2 Network development planning", "Choosing components and planning the installation",
    "select hardware, software and services for a design, and plan device configuration and testing.", "Assignment 2 · B.P4, C.P6",
    h3("Selecting components"),
    p("Choose each part by asking <em>what does the client need it to do?</em> Start from the services and users, then work outwards to servers, storage, switching, wireless and the WAN. Record the reason for every choice: this becomes your justification (B.M2)."),
    table(["Component", "Questions to answer", "Example decision"], [
        ["Server", "which services (DHCP, DNS, web, mail, files)? how many users? physical, virtual or cloud?", "one tower server running virtual machines for DHCP/DNS/web, because the site has 15 users and a small budget"],
        ["Storage", "how much data now and in 3 years? on-site, off-site or both? backups?", "NAS with RAID 1 plus nightly cloud backup"],
        ["Switches", "how many ports plus spare? speed? PoE? managed (VLANs)? layer 2 or 3?", "24-port gigabit managed PoE switch: 14 devices now, room to grow, powers phones and APs"],
        ["Wireless APs", "how many, where, which standard, how many users each?", "two Wi-Fi 6 APs, one per floor, WPA3, separate guest SSID"],
        ["Router / WAN", "internet speed, second site, VPN, firewall features?", "business router with firewall and site-to-site VPN to the branch"],
        ["Client and server OS", "Windows, Linux or macOS? licences? open source or proprietary?", "Linux server (no licence cost) and Windows 11 clients for the design software"],
        ["Applications and monitoring", "which applications need the network? how will it be monitored?", "VoIP, antivirus with central console, free monitoring tool"],
    ], caption="Component selection"),
    h3("Planning the configuration"),
    table(["Device", "Plan before you build"], [
        ["Switches", "name, management IP, passwords, VLANs and which ports go in each, unused ports shut down"],
        ["Routers", "name, interface addresses, routes (static or dynamic), NAT, DHCP relay, passwords, SSH"],
        ["Access points", "SSID names, security (WPA2/WPA3 and passphrase), channels, where they are placed"],
        ["Servers", "static addresses, DHCP scope and exclusions, DNS records, web and mail settings"],
    ], caption="Configuration planning checklist"),
    p("Build a <strong>prototype</strong> in Packet Tracer first. Simulation is free, safe and lets you find mistakes before real equipment is bought or configured."),
    h3("Planning the tests"),
    table(["No.", "What is tested", "How", "Expected result"], [
        ["1", "PC to its default gateway", "ping 192.168.20.1 from PC-03", "4 replies, under 10 ms"],
        ["2", "DHCP gives an address", "set laptop to DHCP; ipconfig", "an address in 192.168.20.100–.150"],
        ["3", "DNS name resolution", "browse to intranet.local", "intranet page loads"],
        ["4", "Branch to head office", "ping head-office server from branch PC", "replies received"],
        ["5", "Folder permission", "log in as a Reception user; open the Accounts folder", "access denied"],
        ["6", "Device password", "console into the switch", "password prompt appears"],
    ], caption="Example connectivity and service test plan (dental practice)"),
    p("A good test plan covers every requirement, says exactly how to test it, and states the expected result <em>before</em> you test. When you run it, add the actual result, a pass or fail, a screenshot reference, and what you did about any failure."),
    terms([
        ("Prototype", "a working model of the network built to test the design."),
        ("Managed switch", "a switch you can configure, e.g. with VLANs and security."),
        ("Layer 3 switch", "a switch that can also route between VLANs."),
        ("Test plan", "a list of tests with methods and expected results, written before testing."),
    ]),
    assignment_link("B.P4 and C.P6", "Your design needs an equipment list with reasons, a physical layout, network diagrams and an addressing table. Use the planning tools on the Assignment builder page to build your inventory, IP plan and test plan."),
    think([
        ("Why write the expected result before running a test?", "So the test is objective: you decide what 'working' means in advance, rather than accepting whatever happens."),
        ("Why buy a 24-port switch for 14 devices?", "It leaves room to grow (scalability) and spare ports for printers, APs or a replacement if a port fails."),
    ]),
)


def perm_fig():
    s = SVG(760, 200, "Linux permission bits for owner, group and others")
    labels = ["owner", "group", "others"]
    bits = ["rwx", "r-x", "---"]
    nums = ["7", "5", "0"]
    for i in range(3):
        x = 120 + i * 190
        s.box(x, 40, 160, 50, bits[i], size=22, fill=["#dcebf6", "#e8f1e4", "#fbf0dd"][i])
        s.text(x + 80, 30, labels[i], size=13, bold=True)
        s.text(x + 80, 118, f"= {nums[i]}", size=18, bold=True)
    s.text(380, 150, "r = 4 (read)   w = 2 (write)   x = 1 (execute / open a folder)   add them up for each group", size=12)
    s.text(380, 176, "chmod 750 reports  →  owner full control, group can read and open, everyone else no access", size=13, mono=True, color=ACCENT)
    return s.render("Permissions in Linux are set for three classes of user. Each class gets a number from 0 (nothing) to 7 (read, write and execute).")


B3 = lesson("B3", "B3 Network services and resources access", "Users, groups, passwords and permissions",
    "plan authentication, users and groups, and access permissions for files, folders and printers.", "Assignment 2 · B.P4, C.P5",
    h3("Authentication planning"),
    p("A <strong>password policy</strong> sets the rules for passwords. Current UK NCSC guidance favours long passphrases (for example three random words), blocking common and breached passwords, multi-factor authentication (MFA) for important accounts, and <em>not</em> forcing frequent changes, which makes people choose weaker passwords. An <strong>audit policy</strong> decides what gets logged, such as successful and failed logins, changes to user accounts and access to sensitive folders, so problems can be investigated."),
    h3("Users and groups"),
    p("Give permissions to <strong>groups</strong>, not individuals, then put each user in the right groups. When someone joins, moves or leaves, you change their group membership instead of editing every folder. Use a consistent naming scheme for accounts (for example <code>firstname.lastname</code> or <code>j.smith</code>) and follow the <strong>principle of least privilege</strong>: people get only the access their job needs."),
    table(["User", "Group", "Needs access to"], [
        ["priya.shah", "RECEPTION", "Bookings (read and write)"],
        ["tom.okafor", "CLINICAL", "Patients (full), Bookings (read)"],
        ["lee.chan", "CLINICAL", "Patients (full), Bookings (read)"],
        ["sam.berg", "MANAGERS", "Accounts (full), every folder (read)"],
    ], caption="Example access plan (dental practice, not your assignment client)"),
    perm_fig(),
    p("Windows uses <strong>NTFS permissions</strong> (Full control, Modify, Read and execute, Read, Write), which can be set per user or group. Linux uses the owner/group/others model above. Printers can also have permissions, for example only the MANAGERS group may use the colour printer."),
    cli(["sudo groupadd clinical", "sudo useradd -m -G clinical tom.okafor", "sudo passwd tom.okafor", "sudo mkdir /srv/patients", "sudo chown sam.berg:clinical /srv/patients", "sudo chmod 770 /srv/patients", "ls -ld /srv/patients"], "Creating a group, a user and a folder only that group can use (Linux)"),
    terms([
        ("Authentication", "proving who you are, e.g. a password plus a code."),
        ("Authorisation", "what you are allowed to do once logged in."),
        ("Least privilege", "giving people only the access they need to do their job."),
        ("Owner / group / others", "the three classes of user Linux sets permissions for."),
        ("MFA", "multi-factor authentication: two or more kinds of proof."),
    ]),
    think([
        ("Why give permissions to groups instead of each user?", "It is quicker and less error-prone: add a new person to a group and they instantly get the right access; remove them when they leave."),
        ("What does <code>chmod 755</code> allow?", "The owner can read, write and execute (7); the group and everyone else can read and execute (5) but not change anything."),
    ]),
)


def ios_fig():
    s = SVG(760, 200, "Cisco IOS command modes")
    modes = [("User EXEC", "Switch>", "look only"), ("Privileged EXEC", "Switch#", "show, copy, test"), ("Global config", "Switch(config)#", "device-wide settings"), ("Interface / line", "Switch(config-if)#", "one port or line")]
    cmds = ["enable", "configure terminal", "interface g0/1"]
    for i, (a, b, c) in enumerate(modes):
        x = 10 + i * 190
        s.box(x, 40, 170, 80, a, size=14, fill=["#eef0f3", "#dcebf6", "#e8f1e4", "#fbf0dd"][i], bold=True)
        s.text(x + 85, 104, b, size=12, mono=True)
        s.text(x + 85, 146, c, size=12)
        if i < 3:
            s.arrow(x + 170, 80, x + 189, 80, width=1.8)
            s.text(x + 180, 176, cmds[i], size=11, mono=True, color=ARROW)
    s.text(380, 24, "Type 'exit' to go back one level, or 'end' to return to privileged EXEC.", size=12)
    return s.render("Cisco devices have layered command modes. The prompt shows which mode you are in.")


C1 = lesson("C1", "C1 Implementation and configuration", "Building and configuring the network",
    "configure switches, routers, wireless and servers, and create users, groups and shared resources.", "Assignment 2 · C.P5",
    p("Build your prototype in Packet Tracer (or on real kit) in the same order every time: cable the devices, configure device security and names, set addresses, configure routing, add services, then add users and permissions. Save your configuration and take screenshots as you go: they are your evidence."),
    ios_fig(),
    cli(["enable", "configure terminal", "hostname DEN-SW01", "enable secret Str0ng-Enable!", "line console 0", " password C0ns0le-Pass", " login", " exit", "line vty 0 15", " password Vty-Pass-2026", " login", " exit", "service password-encryption", "banner motd # Authorised staff only #", "end", "copy running-config startup-config"], "Securing a switch: name, passwords on every way in, encrypted passwords and a warning banner"),
    cli(["configure terminal", "interface g0/0", " ip address 192.168.20.1 255.255.255.0", " no shutdown", " exit", "ip dhcp excluded-address 192.168.20.1 192.168.20.20", "ip dhcp pool SURGERY", " network 192.168.20.0 255.255.255.0", " default-router 192.168.20.1", " dns-server 192.168.20.2", " exit", "ip route 192.168.30.0 255.255.255.0 10.0.0.2", "end", "show ip interface brief", "show ip route"], "Router: interface address, a DHCP pool, and a static route to the branch network"),
    cli(["vlan 10", " name STAFF", "vlan 20", " name VOICE", "interface range fa0/1-10", " switchport mode access", " switchport access vlan 10", "interface range fa0/20-24", " shutdown", "end", "show vlan brief"], "Switch: create VLANs, put ports in them and shut unused ports"),
    table(["Task", "Where in Packet Tracer"], [
        ["Wireless: SSID, WPA2-PSK passphrase", "Access point → Config → Port 1; laptop → Config → Wireless0"],
        ["Server services: DHCP, DNS, HTTP, EMAIL, FTP", "Server → Services tab"],
        ["Static address on a server or printer", "Device → Desktop → IP Configuration"],
        ["VoIP phones", "a router with telephony-service, or a Cisco IP phone with the phone's VLAN"],
    ], caption="Configuring other parts"),
    real_world("evidence as you go", "After each stage the engineer saves the Packet Tracer file with a new version number (v1-cabled, v2-addressed, v3-services), takes a screenshot of <code>show running-config</code>, and writes two lines in their diary: what they did and any problem they hit."),
    terms([
        ("Running config", "the settings the device is using now (lost on restart unless saved)."),
        ("Startup config", "the saved settings loaded when the device starts."),
        ("no shutdown", "the command that turns an interface on."),
        ("Static route", "a route typed in manually by the administrator."),
    ]),
    think([
        ("You configured a router interface but the link light stays red. Which command did you probably forget?", "<code>no shutdown</code>. Router interfaces are off by default."),
        ("Why does <code>service password-encryption</code> matter?", "Without it most passwords show in plain text in the configuration, so anyone who sees the config (or a screenshot of it) learns them."),
    ]),
)


C2 = lesson("C2", "C2 Testing and troubleshooting", "Testing the network and fixing faults",
    "carry out a test plan, record results with evidence, and troubleshoot faults methodically.", "Assignment 2 · C.P6, C.M3",
    h3("Three kinds of test"),
    ul(["<strong>Connectivity tests:</strong> can each device reach its gateway, other subnets, the branch and the internet? (ping, tracert)",
        "<strong>Service tests:</strong> do DHCP, DNS, web, email, VoIP and file sharing work? (ipconfig, nslookup, browser, email client)",
        "<strong>Access tests:</strong> can each user reach what they should, and are they blocked from what they should not? Are device passwords and Wi-Fi security working?"]),
    h3("A troubleshooting method"),
    table(["Step", "What to do"], [
        ["1 Identify the problem", "What exactly fails? For whom? Since when? What changed?"],
        ["2 Form a theory", "Start at the bottom of the OSI model: cable and link lights, then IP settings, then services."],
        ["3 Test the theory", "Use ping, ipconfig, show commands or swap a cable to prove or disprove it."],
        ["4 Plan and apply the fix", "Change one thing at a time so you know what fixed it."],
        ["5 Verify", "Re-run the failed test and the related tests."],
        ["6 Document", "Record the fault, the cause, the fix and the evidence."],
    ], caption="A structured troubleshooting method"),
    table(["Symptom", "Likely cause", "Check with"], [
        ["Red link light in Packet Tracer", "interface shut down or wrong cable type", "<code>show ip interface brief</code>"],
        ["Can ping inside the LAN but not other networks", "wrong or missing default gateway; missing route", "<code>ipconfig</code>; <code>show ip route</code>"],
        ["Address is 169.254.x.x", "DHCP server unreachable or service off", "server Services tab; <code>ipconfig /renew</code>"],
        ["Can ping an IP but not use its name", "DNS record missing or wrong DNS server", "<code>nslookup</code>"],
        ["Laptop will not join Wi-Fi", "SSID or passphrase mismatch; wrong security type", "AP and laptop wireless settings"],
    ], caption="Common faults"),
    h3("Optimising"),
    p("Testing often shows things to improve. Optimisation (C.M3) means changing the network to make it perform better, be more secure or be easier to use, then re-testing to prove the improvement: for example moving phones to a voice VLAN, shutting unused switch ports, adding SSH instead of Telnet, adding a second AP where the signal was weak, or reserving static addresses for printers."),
    terms([
        ("Connectivity test", "checks whether devices can reach each other."),
        ("Root cause", "the underlying reason for a fault, not just the symptom."),
        ("Optimisation", "an improvement to performance, security or usability, proved by re-testing."),
    ]),
    assignment_link("C.P6 and C.M3", "Complete every test in your plan with actual results and screenshot evidence. For Merit, choose improvements based on what the tests showed, make them, and re-test to show the difference."),
    think([
        ("Why change only one thing at a time when troubleshooting?", "If you change several things and it starts working, you will not know which change fixed it, or whether one of them caused a new problem."),
        ("A test fails. Should you delete it from your test plan?", "No. Record the failure, what caused it and how you fixed it, then re-test. Documented failures and fixes are strong evidence."),
    ]),
)


def baseline_fig():
    s = SVG(760, 250, "Network use compared with the baseline")
    x0, y0, w, h = 60, 30, 660, 170
    s.line(x0, y0 + h, x0 + w, y0 + h, color=INK, width=1.5)
    s.line(x0, y0, x0, y0 + h, color=INK, width=1.5)
    s.add(f'<rect x="{x0}" y="{y0 + 70}" width="{w}" height="50" fill="#e8f1e4" opacity="0.8"/>')
    s.text(x0 + w - 6, y0 + 88, "normal range (baseline)", size=11, anchor="end", color=ACCENT)
    import math
    pts = []
    for i in range(25):
        base = 95 + 25 * math.sin((i - 6) / 24 * 2 * math.pi) if 7 <= i <= 18 else 150
        if i == 14:
            base = 20
        pts.append((x0 + i * w / 24, y0 + base))
    s.add('<path d="M' + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts) + f'" stroke="{ARROW}" stroke-width="2.5" fill="none"/>')
    s.circle(pts[14][0], pts[14][1], 7, fill="#fbe3d4", stroke=WARN)
    s.text(pts[14][0] + 12, pts[14][1] + 4, "spike: investigate", size=11, anchor="start", color=WARN)
    for hr in (0, 6, 12, 18, 24):
        s.text(x0 + hr * w / 24, y0 + h + 18, f"{hr:02d}:00", size=11)
    s.text(22, y0 + 10, "use", size=11, anchor="start")
    return s.render("A baseline records normal performance. Monitoring then shows when the network moves outside it.")


C3 = lesson("C3", "C3 Performance monitoring", "Baselines, monitoring and logs",
    "establish a performance baseline, monitor the network, and use event logs.", "Assignment 2 · C.M3, BC.D2",
    baseline_fig(),
    p("A <strong>baseline</strong> is a measurement of how the network normally behaves when it is working well: typical bandwidth use, ping times, server CPU and memory, disk space. Take it soon after the network is built. Later measurements are compared with the baseline, so you can tell a real problem from a normal busy period and show whether an optimisation helped."),
    table(["What to monitor", "Why", "Tool"], [
        ["Bandwidth / throughput", "is a link overloaded?", "switch or router statistics, monitoring software"],
        ["Latency and packet loss", "calls and video suffer if delay or loss rises", "ping, monitoring dashboards"],
        ["Server CPU, memory, disk", "is the server struggling or running out of space?", "Performance Monitor, top, Task Manager"],
        ["Storage capacity", "plan upgrades before disks fill up", "server tools, NAS dashboard"],
        ["Event logs", "errors, failed logins, service crashes", "Event Viewer, <code>/var/log</code>, <code>journalctl</code>"],
    ], caption="Monitoring the network"),
    p("Review logs regularly, not just after something breaks: repeated failed logins can mean someone is guessing passwords, and repeated warnings can predict a failing disk."),
    terms([
        ("Baseline", "a record of normal performance used for comparison."),
        ("Latency", "the delay for data to travel across the network."),
        ("Throughput", "how much data actually gets through per second."),
    ]),
    think([
        ("Why is a baseline useful when evaluating an optimisation?", "You can compare performance before and after the change with real numbers, instead of just saying it seems faster."),
    ]),
)


C4 = lesson("C4", "C4–C5 Evaluation, review and professional skills", "Evaluating the network and managing yourself",
    "evaluate the design and the built network against the client's requirements, suggest future improvements, and evidence your own planning and professional behaviour.", "Assignment 2 · C.P7, BC.D2, BC.D3",
    h3("Evaluate against the requirements"),
    p("Go back to the client's requirements and judge each one with evidence from your design, build and tests. A <strong>review</strong> (Pass) says how far each requirement was met. An <strong>evaluation</strong> (Distinction) weighs up strengths and weaknesses of both the design and the implementation, uses evidence from every stage, explains why things happened, and reaches justified conclusions and future recommendations."),
    table(["Requirement", "Met?", "Evidence", "Strengths / limitations", "Future improvement"], [
        ["Patient records only for clinical staff", "Fully", "Test 5 screenshot: reception denied", "group permissions work; records still on one server", "add a second server or cloud replica"],
        ["Secure Wi-Fi for staff tablets", "Partly", "Test 9: WPA2 works; weak signal in room 4", "secure but coverage gap", "add a second AP; move to WPA3"],
    ], caption="An evaluation grid (dental practice example)"),
    h3("Future enhancements and optimisation"),
    p("Suggest realistic next steps linked to the client's goals: capacity for more staff, redundancy (second internet line, a UPS), stronger security (MFA, network access control, meeting Cyber Essentials), better management (central monitoring, documentation), or new services (cloud backup, IPv6)."),
    h3("C5: skills, knowledge and behaviours"),
    table(["You need to show", "Evidence you can collect"], [
        ["Planning with targets and timescales", "a project plan or calendar with dated targets"],
        ["Reviewing and responding to feedback", "a peer feedback form on your design, and what you changed because of it"],
        ["Professional behaviour", "attendance, meeting deadlines, supporting others; your tutor's witness statement"],
        ["Documenting processes and outcomes", "a diary or log with dates, screenshots and version-numbered files"],
        ["Communication", "a clear customer email, professional design documents, presenting your network"],
    ], caption="Your self-management portfolio (BC.D3)"),
    real_world("a good diary entry", "“14 Mar: configured VLANs 10 and 20 on DEN-SW01. Phones would not get addresses: DHCP pool was on VLAN 10 only. Fixed by adding a second pool; re-ran tests 7–8, both pass (screenshots 21–22). Target for Friday: Wi-Fi and permissions. Asked Jay to review my IP table.”"),
    terms([
        ("Review", "describe how far the network meets each requirement."),
        ("Evaluate", "weigh up strengths and weaknesses using evidence, and reach justified conclusions."),
        ("Witness statement", "a record written by your tutor of what they saw you do."),
    ]),
    assignment_link("C.P7, BC.D2 and BC.D3", "Keep your diary from the very first lesson of Assignment 2. The Assignment builder page has a planner, a feedback log and an evaluation grid to help you collect the evidence as you go."),
    think([
        ("What is the difference between saying 'the Wi-Fi works' and evaluating it?", "An evaluation adds evidence (test results), judges how well it met the requirement (e.g. secure but weak in one room), explains why, and recommends what should happen next."),
    ]),
)

LESSONS = [B1a, B1b, B2, B3, C1, C2, C3, C4]
