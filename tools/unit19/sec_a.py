from u19 import *


# ---------------- A1a Network types ----------------
def scale_fig():
    s = SVG(760, 300, "Networks from personal to worldwide")
    rings = [(380, 160, 320, 140, "#f4f9fc", "WAN: countries and continents (the internet is the biggest WAN)"),
             (380, 170, 230, 100, "#e6f1f9", "MAN: a city or campus"),
             (380, 180, 140, 62, "#d7e8f6", "LAN / WLAN: one building"),
             (380, 190, 58, 28, "#c4dcf1", "PAN")]
    for cx, cy, rx, ry, f, t in rings:
        s.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{f}" stroke="{LINE}" stroke-width="2"/>')
    s.text(380, 50, "WAN: countries and continents (the internet is the biggest WAN)", size=13, bold=True)
    s.text(380, 100, "MAN: a city or a university campus", size=13, bold=True)
    s.text(380, 146, "LAN / WLAN: one building or site", size=13, bold=True)
    s.text(380, 188, "PAN", size=13, bold=True)
    s.text(380, 204, "Bluetooth: watch, earbuds", size=10)
    return s.render("Network types grow in size from a personal area network to a wide area network. Each larger network links smaller ones together.")


def company_fig():
    s = SVG(760, 370, "A company network combining LAN, WLAN, SAN and WAN")
    s.box(20, 20, 340, 262, fill="#f6f9fc", dash=True)
    s.text(190, 42, "Head office LAN", size=14, bold=True)
    device(s, "router", 60, 58)
    s.text(132, 104, "Router", size=12, anchor="start")
    device(s, "switch", 60, 134)
    s.text(132, 161, "Switch", size=12, anchor="start")
    s.line(92, 102, 92, 144, color="#8aa5b8", width=1.8)
    for i, k in enumerate(["pc", "pc", "printer"]):
        x = 24 + i * 70
        device(s, k, x, 214, ["PC", "PC", "Printer"][i])
        s.line(x + 32, 214, 92, 168, color="#8aa5b8", width=1.8)
    device(s, "ap", 262, 214, "Access point")
    s.line(294, 222, 124, 156, color="#8aa5b8", width=1.8)
    device(s, "laptop", 262, 120)
    s.text(294, 180, "WLAN laptop", size=12)
    s.add('<path d="M300 184 Q312 200 298 214" stroke="#20857b" stroke-width="2" stroke-dasharray="4 4" fill="none"/>')
    s.box(20, 294, 340, 66, fill="#eef7ee", dash=True)
    device(s, "server", 30, 304)
    device(s, "storage", 100, 306)
    device(s, "storage", 160, 306)
    s.text(236, 322, "SAN", size=14, anchor="start", bold=True)
    s.text(236, 342, "fast shared storage", size=11, anchor="start")
    device(s, "cloud", 400, 44)
    s.text(436, 112, "Internet / WAN", size=13, bold=True)
    s.arrow(126, 72, 398, 66, both=True, label="WAN link (ISP)", lx=40, ly=-10)
    s.box(560, 20, 180, 170, fill="#f6f9fc", dash=True)
    s.text(650, 42, "Branch office LAN", size=14, bold=True)
    device(s, "router", 618, 52)
    device(s, "switch", 618, 100)
    device(s, "pc", 572, 140)
    device(s, "laptop", 662, 140)
    s.arrow(472, 72, 616, 74, both=True, label="WAN link / VPN", ly=-10)
    s.box(420, 220, 320, 120, fill="white")
    s.text(432, 244, "Who can use it?", size=13, anchor="start", bold=True)
    for i, t in enumerate(["Intranet: staff only, inside the company network", "Extranet: selected outsiders, e.g. suppliers log in", "Internet: everyone, the public network of networks", "Cloud: services rented from a provider online"]):
        s.text(432, 268 + i * 18, "\u2022 " + t, size=11, anchor="start")
    return s.render("One organisation often uses several network types at once: a wired LAN, a WLAN for mobile devices, a SAN for storage and WAN links to other sites.")


A1a = lesson("A1a", "A1 Network types and models", "Types of network and why we need them",
    "explain what LAN, WLAN, WAN, SAN, intranet, extranet, internet and cloud mean, and why an organisation would choose each one.", "Assignment 1 · A.P1",
    h3("Why do we connect computers at all?"),
    p("A <strong>network</strong> is two or more devices joined together so they can share things. Organisations build networks so people can <strong>communicate</strong> (email, chat, calls), <strong>share data</strong> (one copy of a file everyone can open), <strong>share resources</strong> (one printer or internet connection for 30 people) and <strong>work together</strong> from different places. Different jobs need different kinds of network, which is why there are several types."),
    scale_fig(),
    table(["Type", "Covers", "Who manages it", "Why an organisation needs it"], [
        ["PAN (personal area network)", "a few metres around one person", "the user", "connect a phone to earbuds, a watch or a car without cables"],
        ["LAN (local area network)", "one building or site", "the organisation itself", "fast, cheap sharing of files, printers and internet inside one site"],
        ["WLAN (wireless LAN)", "one building, using radio", "the organisation", "mobility: laptops, tablets and phones; places where cables are hard to fit (listed buildings, halls)"],
        ["MAN (metropolitan area network)", "a city or campus", "a council, university or provider", "link several buildings across a town at high speed"],
        ["WAN (wide area network)", "countries and continents", "service providers (ISPs, telecom companies)", "link sites that are far apart; reach the internet"],
        ["SAN (storage area network)", "inside a data centre", "the organisation's IT team", "give many servers very fast, shared access to large amounts of storage"],
    ], caption="Network types by size and purpose"),
    company_fig(),
    h3("Intranet, extranet, internet and cloud"),
    p("These words describe <em>who is allowed in</em> rather than how big the network is. An <strong>intranet</strong> is a private website and set of services that only staff can reach, such as the HR pages or a room-booking system. An <strong>extranet</strong> opens part of that private system to trusted outsiders, for example suppliers checking orders. The <strong>internet</strong> is the public network of networks that anyone can join. <strong>Cloud</strong> services are computers, storage and software that you rent from a provider and reach over the internet, instead of buying and running them yourself."),
    h3("Wired and wireless integration"),
    p("Most real networks mix both. Wired Ethernet is faster, more reliable and harder to eavesdrop on, so it suits desktop PCs, servers and printers. Wireless gives freedom to move and avoids drilling through walls. An <strong>access point</strong> plugged into a switch joins the two: wireless devices connect to the access point, and the access point passes their traffic onto the wired LAN, so everyone can reach the same servers and printers."),
    real_world("a secondary school", "Classroom PCs and the servers are wired for speed and reliability. Staff laptops and student tablets use the WLAN. The school's intranet holds lesson resources, parents use an extranet portal to see reports, email and backups are in the cloud, and the school connects to the internet through a WAN link from its ISP."),
    terms([
        ("Network", "two or more devices connected so they can share data and resources."),
        ("Bandwidth", "how much data a connection can carry each second, e.g. 1 Gbps."),
        ("ISP", "internet service provider: the company that connects you to the internet."),
        ("Intranet", "a private network service for an organisation's own staff."),
        ("Extranet", "part of an intranet opened to trusted outside users."),
        ("Cloud computing", "renting computing power, storage or software over the internet."),
    ]),
    tryit("wired and wireless together", [
        "Add a 2960 switch, two PCs and a printer. Connect them with copper straight-through cables.",
        "Add an access point and connect it to the switch.",
        "Add a laptop, swap its network card for a wireless card (power off, drag the WPC300N module), then power on.",
        "Give every device an IP address in the same network, e.g. 192.168.1.10 to .20 with mask 255.255.255.0.",
        "From the laptop, ping a wired PC. A reply proves wired and wireless are integrated.",
    ]),
    assignment_link("A.P1", "Task 1 asks you to explain <em>why</em> each network type is needed and how that need affects the choice. For each type, give a reason and a realistic example organisation, then say what would happen if it chose a different type."),
    think([
        ("A café wants customers to browse the web on their phones. Which network type does it need, and why not a wired LAN?", "A WLAN, because customers bring their own mobile devices and move around; cables to every table would be impractical and customers' phones have no Ethernet port."),
        ("What is the difference between the internet and an intranet?", "The internet is public and anyone can join it. An intranet uses the same technologies (web pages, email) but only the organisation's staff can reach it."),
        ("Why would a hospital's data centre use a SAN?", "Many servers need very fast, reliable access to huge amounts of patient data. A SAN gives them shared, high-speed storage separated from ordinary network traffic."),
    ]),
)


# ---------------- A1b Topologies & 802 ----------------
def topo_fig():
    s = SVG(760, 420, "Six physical network topologies")
    import math

    def node(x, y, c="white"):
        s.circle(x, y, 11, fill=c)

    def panel(i, title, note):
        col, row = i % 3, i // 3
        x0, y0 = 20 + col * 248, 20 + row * 200
        s.box(x0, y0, 236, 188, fill="white", stroke="#c9d7e3")
        s.text(x0 + 118, y0 + 22, title, size=14, bold=True)
        s.text(x0 + 118, y0 + 178, note, size=11, color=ARROW)
        return x0, y0
    x, y = panel(0, "Bus", "one break stops everything")
    s.line(x + 20, y + 95, x + 216, y + 95, color=INK, width=3)
    for k in range(5):
        xx = x + 36 + k * 41
        s.line(xx, y + 95, xx, y + (70 if k % 2 else 120), color=LINE, width=2)
        node(xx, y + (60 if k % 2 else 130))
    x, y = panel(1, "Ring", "data passes device to device")
    for k in range(6):
        a = k * math.pi / 3
        x1, y1 = x + 118 + 55 * math.cos(a), y + 98 + 55 * math.sin(a)
        x2, y2 = x + 118 + 55 * math.cos(a + math.pi / 3), y + 98 + 55 * math.sin(a + math.pi / 3)
        s.line(x1, y1, x2, y2, color=LINE, width=2)
    for k in range(6):
        a = k * math.pi / 3
        node(x + 118 + 55 * math.cos(a), y + 98 + 55 * math.sin(a))
    x, y = panel(2, "Star", "most common LAN today")
    for k in range(6):
        a = k * math.pi / 3
        xx, yy = x + 118 + 60 * math.cos(a), y + 98 + 55 * math.sin(a)
        s.line(x + 118, y + 98, xx, yy, color=LINE, width=2)
        node(xx, yy)
    s.box(x + 100, y + 86, 36, 24, fill="#245d83", stroke="#245d83", rx=4)
    x, y = panel(3, "Extended star", "stars joined together")
    centres = [(x + 60, y + 100), (x + 176, y + 100)]
    s.line(*centres[0], *centres[1], color=INK, width=3)
    for cx, cy in centres:
        for k in range(4):
            a = k * math.pi / 2 + math.pi / 4
            xx, yy = cx + 40 * math.cos(a), cy + 45 * math.sin(a)
            s.line(cx, cy, xx, yy, color=LINE, width=2)
            node(xx, yy)
        s.box(cx - 14, cy - 10, 28, 20, fill="#245d83", stroke="#245d83", rx=4)
    x, y = panel(4, "Mesh", "many paths: very reliable, costly")
    pts = [(x + 118 + 58 * math.cos(k * 2 * math.pi / 5 - math.pi / 2), y + 102 + 55 * math.sin(k * 2 * math.pi / 5 - math.pi / 2)) for k in range(5)]
    for i in range(5):
        for j in range(i + 1, 5):
            s.line(*pts[i], *pts[j], color=LINE, width=1.6)
    for pt in pts:
        node(*pt)
    x, y = panel(5, "Hierarchical (tree)", "layers: core → distribution → access")
    s.box(x + 100, y + 40, 36, 22, fill="#20857b", stroke="#20857b", rx=4)
    for k, cx in enumerate([x + 60, x + 176]):
        s.line(x + 118, y + 62, cx, y + 88, color=INK, width=2.5)
        s.box(cx - 16, y + 88, 32, 20, fill="#245d83", stroke="#245d83", rx=4)
        for m in (-28, 0, 28):
            s.line(cx, y + 108, cx + m, y + 140, color=LINE, width=2)
            node(cx + m, y + 148)
    return s.render("Physical topologies describe how devices are cabled together. Star and extended star (with switches in the middle) are used in almost every modern LAN.")


A1b = lesson("A1b", "A1 Network types and models", "Topologies and Ethernet standards",
    "describe physical and logical topologies, and explain why IEEE 802 standards matter.", "Assignment 1 · A.P1, A.M1",
    h3("Physical topology: how the cables are laid out"),
    topo_fig(),
    table(["Topology", "Strengths", "Weaknesses", "Where you see it"], [
        ["Bus", "cheap, little cable", "one cable fault stops the whole network; collisions; hard to find faults", "legacy networks only"],
        ["Ring", "orderly, predictable traffic", "one break can stop the ring (unless dual ring)", "some older and fibre metro networks"],
        ["Star", "a cable fault only affects one device; easy to add devices and find faults", "the central switch is a single point of failure", "almost every office and home LAN"],
        ["Extended star", "grows easily by adding switches", "more switches to buy and manage", "schools, offices over several floors"],
        ["Mesh", "many paths, so it keeps working when links fail", "lots of cable and ports; expensive", "internet backbone, WAN routers, wireless mesh Wi-Fi"],
        ["Hierarchical", "organised, scalable, faults stay in one area", "needs careful design and more equipment", "medium and large enterprise networks"],
    ], caption="Comparing topologies"),
    h3("Logical topology: how the data actually flows"),
    p("The <strong>logical topology</strong> is the path the data takes and the rules it follows, which can differ from the cabling. A diagram showing where equipment sits and where cables run is a <strong>physical</strong> diagram; one showing IP addresses, VLANs and which ports connect to what is a <strong>logical</strong> diagram. Your Assignment 2 design needs both."),
    h3("Standards: the IEEE 802 family"),
    p("Devices from different makers only work together because they follow the same <strong>standards</strong>. The IEEE (Institute of Electrical and Electronics Engineers) writes the 802 family: <strong>802.3</strong> is wired Ethernet, <strong>802.11</strong> is Wi-Fi and <strong>802.15</strong> covers personal networks such as Bluetooth. The Wi-Fi Alliance tests products so they can carry the Wi-Fi logo."),
    table(["Standard", "Name", "Band", "Top speed (theoretical)"], [
        ["802.3u / ab / an", "Fast, Gigabit, 10-Gigabit Ethernet", "copper or fibre", "100 Mbps / 1 Gbps / 10 Gbps"],
        ["802.11b / g", "older Wi-Fi", "2.4 GHz", "11 / 54 Mbps"],
        ["802.11n", "Wi-Fi 4", "2.4 and 5 GHz", "up to 600 Mbps"],
        ["802.11ac", "Wi-Fi 5", "5 GHz", "several Gbps"],
        ["802.11ax", "Wi-Fi 6 / 6E", "2.4, 5 (and 6) GHz", "about 9.6 Gbps; better in crowded rooms"],
    ], caption="Common IEEE 802 standards"),
    p("2.4 GHz travels further and passes through walls better; 5 GHz is faster but has a shorter range. Access points close together should use different channels so they do not interfere."),
    terms([
        ("Topology", "the shape or layout of a network."),
        ("Single point of failure", "one part whose failure stops the whole network or service."),
        ("Standard", "an agreed technical specification so products from different makers work together."),
        ("IEEE 802.3 / 802.11", "the standards for wired Ethernet and for Wi-Fi."),
    ]),
    think([
        ("Why is star the most popular LAN topology?", "Each device has its own cable to the switch, so one broken cable only affects one device, faults are easy to find, and devices are easy to add."),
        ("An office has thick walls. Should its access points use 2.4 GHz or 5 GHz, and why?", "2.4 GHz passes through walls and travels further; 5 GHz is faster but is weakened more by walls. Many APs offer both, letting close devices use 5 GHz."),
    ]),
)


# ---------------- A1c Models ----------------
def models_fig():
    s = SVG(760, 300, "Peer-to-peer, client/server and thin client models")
    s.text(125, 26, "Peer-to-peer", size=15, bold=True)
    pts = [(60, 80), (190, 80), (60, 190), (190, 190)]
    for i in range(4):
        for j in range(i + 1, 4):
            s.line(pts[i][0] + 32, pts[i][1] + 20, pts[j][0] + 32, pts[j][1] + 20, color="#b9c7d5", width=1.6)
    for x, y in pts:
        device(s, "pc", x, y - 5)
    s.text(125, 270, "every PC shares and uses resources", size=11)
    s.text(380, 26, "Client/server", size=15, bold=True)
    device(s, "server", 348, 50, "Server")
    for i, x in enumerate([280, 348, 416]):
        device(s, "pc", x, 185)
        s.arrow(x + 32, 183, 380, 112, both=True, width=1.6)
    s.text(380, 270, "server provides files, logins, services", size=11)
    s.text(640, 26, "Thin client", size=15, bold=True)
    device(s, "server", 608, 50, "")
    s.text(640, 118, "does ALL the processing", size=11, color=ACCENT)
    for x in [548, 616, 684]:
        s.box(x + 10, 190, 44, 30, fill="#f6f9fc", rx=3)
        s.text(x + 32, 234, "screen +", size=9)
        s.text(x + 32, 246, "keyboard", size=9)
        s.arrow(x + 32, 188, 640, 132, both=True, width=1.6)
    s.text(640, 270, "clients only display and send key presses", size=11)
    return s.render("Three network models. The difference is where the files, logins and processing live.")


A1c = lesson("A1c", "A1 Network types and models", "Network models: peer-to-peer, client/server and thin client",
    "describe the three network models and weigh up their strengths and weaknesses for different clients.", "Assignment 1 · A.P1, A.D1",
    models_fig(),
    h3("Peer-to-peer (P2P)"),
    p("Every computer is equal: each one can share its own files or printer and use other computers' resources. There is no central server, so it is cheap and quick to set up. But each user manages their own sharing and passwords, backups are scattered, and it becomes hard to manage beyond about 10 computers. It suits a home or a very small office."),
    h3("Client/server"),
    p("One or more powerful <strong>servers</strong> provide services to the <strong>clients</strong>: central logins (a directory service), shared folders with permissions, printing, email and backups. It needs a server, a network operating system and someone to manage it, which costs more. In return it is secure, easy to back up and scales to thousands of users. If the server fails, services stop, so important servers are duplicated."),
    h3("Thin client"),
    p("A thin client is a cheap, simple device (sometimes just a screen, keyboard and small box) that sends key presses and mouse clicks to a powerful server, which runs the programs and sends back the picture. Nothing is stored on the device, so it is secure and cheap to run, and every desk gets the same, centrally updated setup. It depends completely on the network and the server: if either is slow or down, nobody can work, and it suits heavy graphics or offline work poorly."),
    table(["Factor to weigh", "Questions to ask for your client"], [
        ["Ease of use", "Who logs in where? Do users need to manage sharing themselves?"],
        ["Ease of set-up", "Is there a server to install? How much configuration and expertise does it need?"],
        ["Performance", "Where does processing happen? What happens when many users are busy at once?"],
        ["Suitability for the applications", "Office documents, a shared database, video editing, a call centre, a shop till?"],
        ["Security and management", "Central logins and permissions, or passwords on every PC? Where are backups?"],
        ["Cost and scale", "Up-front hardware and licences versus running costs; how many users now and in future?"],
    ], caption="Use these factors to evaluate the models (A.D1)"),
    real_world("a call centre", "A call centre with 200 identical desks often uses thin clients: they are cheap, easy to replace, and no customer data is stored on the desk. A two-person design studio is more likely to use peer-to-peer or a small NAS, because powerful editing PCs need their own processing and there is no IT team."),
    terms([
        ("Client", "a device that requests a service."),
        ("Server", "a computer that provides a service to clients."),
        ("Network operating system", "an OS designed to provide network services, e.g. Windows Server or Linux."),
        ("Thin client", "a low-power device that relies on a server for processing and storage."),
    ]),
    assignment_link("A.D1", "To reach Distinction you must <em>evaluate</em>: for each model give benefits and drawbacks, test them against ease of use, set-up, performance and suitability, and back every point with a reasoned example of a real kind of organisation. Finish with a supported conclusion on which model suits which client."),
    think([
        ("Why does peer-to-peer become hard to manage in a 40-person office?", "Every PC holds its own shared folders and user accounts, so passwords, permissions and backups have to be managed on 40 separate machines. A central server does this in one place."),
        ("Give one situation where a thin client would be a poor choice.", "Video editing or 3D design, because the heavy processing and graphics would all have to travel over the network from the server; or a site with an unreliable network connection."),
    ]),
)


# ---------------- A1d Trends ----------------
def hypervisor_fig():
    s = SVG(760, 260, "Type 1 and Type 2 hypervisors")
    s.text(190, 26, "Type 1: bare metal", size=15, bold=True)
    s.box(40, 200, 300, 40, "Server hardware", size=13, fill="#e8f1e4", stroke="#5b8a4f")
    s.box(40, 155, 300, 40, "Hypervisor (e.g. ESXi, Hyper-V, Proxmox)", size=12, fill="#dcebf6")
    for i, t in enumerate(["VM: web", "VM: mail", "VM: files"]):
        s.box(40 + i * 102, 45, 96, 105, t, "own OS + apps", size=12, fill="white")
    s.text(570, 26, "Type 2: hosted", size=15, bold=True)
    s.box(420, 200, 300, 40, "Laptop hardware", size=13, fill="#e8f1e4", stroke="#5b8a4f")
    s.box(420, 155, 300, 40, "Host OS (Windows / macOS)", size=12, fill="#eef0f3")
    s.box(420, 110, 300, 40, "Hypervisor app (e.g. VirtualBox)", size=12, fill="#dcebf6")
    for i, t in enumerate(["VM: Linux", "VM: Server"]):
        s.box(420 + i * 152, 45, 146, 60, t, size=12, fill="white")
    return s.render("Virtualisation runs several virtual machines on one physical computer. Type 1 is used for servers; Type 2 is handy for learning and testing.")


def cloud_fig():
    s = SVG(760, 250, "Who manages what in IaaS, PaaS and SaaS")
    layers = ["Applications", "Data", "Runtime", "Operating system", "Virtualisation", "Servers & storage", "Networking"]
    cols = [("On-premises", 7), ("IaaS", 3), ("PaaS", 1), ("SaaS", 0)]
    for c, (name, you) in enumerate(cols):
        x = 40 + c * 180
        s.text(x + 75, 22, name, size=14, bold=True)
        for r, l in enumerate(layers):
            mine = r < you if name != "IaaS" else r < 4
            if name == "PaaS":
                mine = r < 2
            s.box(x, 32 + r * 28, 150, 24, l, size=11, fill="#f6c89a" if mine else "#bcd6f0", rx=3, stroke="#b58a3a" if mine else LINE)
    s.text(380, 240, "Orange = you manage it   ·   Blue = the cloud provider manages it", size=12)
    return s.render("Cloud service models. The further right, the less you manage yourself (and the less control you have).")


A1d = lesson("A1d", "A1 Network types and models", "Modern trends: virtualisation, cloud, BYOD and SDN",
    "explain the main modern networking trends and the opportunities and risks they bring.", "Assignment 1 · A.P1",
    h3("Virtualisation"),
    p("In the past each service (web, email, files) ran on its own physical server, which sat mostly idle; this waste is called <strong>server sprawl</strong>. <strong>Virtualisation</strong> uses a <strong>hypervisor</strong> to run several <strong>virtual machines (VMs)</strong> on one physical server, each with its own operating system. Fewer servers means less cost, power and space, and VMs can be copied, backed up and moved between hosts easily."),
    hypervisor_fig(),
    h3("Cloud computing"),
    p("Cloud providers run huge data centres and rent out computing, storage and software over the internet. A <strong>public cloud</strong> (AWS, Azure, Google Cloud) is shared with other customers; a <strong>private cloud</strong> is used by one organisation only; a <strong>hybrid cloud</strong> mixes the two; an <strong>edge cloud</strong> puts small servers close to users or IoT devices to cut delay."),
    cloud_fig(),
    table(["Trend", "What it means", "Benefits", "Challenges"], [
        ["Cloud computing", "rent services instead of owning servers", "pay for what you use, scale up quickly, reach from anywhere", "needs reliable internet; ongoing costs; data protection and where data is stored"],
        ["BYOD (bring your own device)", "staff and students use their own phones and laptops", "people use devices they know; less hardware to buy", "security: unknown, unpatched devices; separating work and personal data; support"],
        ["SDN (software-defined networking)", "network devices are controlled centrally by software", "change the whole network from one place; automation", "new skills needed; the controller is critical"],
        ["Software-defined storage / SAN", "storage is pooled and managed by software", "flexible, shared, easy to grow", "cost and complexity"],
        ["IoT (Internet of Things)", "sensors and smart devices join the network", "new data and automation", "huge numbers of devices; many are insecure"],
    ], caption="Modern networking trends and challenges"),
    real_world("BYOD at college", "A college lets students join a separate guest Wi-Fi network with their own phones. It is kept apart from staff and exam systems (a separate VLAN), and staff devices must have a screen lock and up-to-date software before they can reach email."),
    terms([
        ("Virtual machine (VM)", "a software computer running inside a physical computer."),
        ("Hypervisor", "the software that creates and runs virtual machines."),
        ("IaaS / PaaS / SaaS", "infrastructure, platform and software as a service: three levels of cloud service."),
        ("BYOD", "bring your own device: using personal devices on an organisation's network."),
        ("SDN", "software-defined networking: controlling network devices centrally with software."),
    ]),
    think([
        ("Why is virtualisation described as the foundation of cloud computing?", "Cloud providers split their physical servers into many virtual machines that can be created, resized and moved in minutes for different customers. Without virtualisation they could not share hardware so flexibly."),
        ("Name one security risk of BYOD and one way to reduce it.", "Personal devices may carry malware or be unpatched. Put them on a separate guest network/VLAN, and require screen locks, updates or device-management software before they reach company data."),
    ]),
)


# ---------------- A2a Hardware ----------------
def devices_fig():
    s = SVG(760, 240, "Common network devices")
    items = [("pc", "PC"), ("laptop", "Laptop"), ("phone", "Smartphone"), ("printer", "Printer"), ("ipphone", "IP phone"), ("server", "Server"),
             ("switch", "Switch"), ("router", "Router"), ("ap", "Access point"), ("firewall", "Firewall"), ("cloud", "Internet"), ("storage", "Storage")]
    for i, (k, t) in enumerate(items):
        x, y = 20 + (i % 6) * 122, 30 + (i // 6) * 105
        device(s, k, x + 28, y, t)
    s.text(380, 18, "End devices (top row): where messages start and finish", size=12, color=ACCENT)
    s.text(380, 232, "Intermediary devices (bottom row): move, direct and protect the data", size=12, color=ARROW)
    return s.render("The icons used in this course. End devices create and use data; intermediary devices carry it between them.")


def switch_fig():
    s = SVG(760, 260, "How a switch learns MAC addresses")
    device(s, "switch", 330, 110, "")
    s.text(362, 172, "Switch", size=13, bold=True)
    hosts = [("A", "AA-11", 60, 30, 1), ("B", "BB-22", 60, 180, 2), ("C", "CC-33", 600, 30, 3), ("D", "DD-44", 600, 180, 4)]
    for n, mac, x, y, port in hosts:
        device(s, "pc", x, y)
        s.text(x + 32, y + 62, f"PC {n} · {mac}", size=11)
        s.line(x + 32 if x < 300 else x + 32, y + 22, 362 if x < 300 else 362, 132, color="#b9c7d5", width=2)
        s.text((x + 362) / 2 + (-10 if x < 300 else 10), (y + 132) / 2 - 6, f"port {port}", size=10, color=ARROW)
    s.box(250, 190, 230, 64, fill="white")
    s.text(365, 208, "MAC address table", size=12, bold=True)
    s.text(365, 226, "AA-11 → port 1   (learned)", size=11, mono=True)
    s.text(365, 244, "CC-33 → port 3   (learned)", size=11, mono=True)
    return s.render("A switch reads the source MAC address of each frame to learn which device is on which port, then forwards frames only to the right port.")


A2a = lesson("A2a", "A2 Network components", "Network hardware: devices, switches, routers, access points and cables",
    "explain the job and key characteristics of each piece of network hardware.", "Assignment 1 · A.P2, A.M1",
    devices_fig(),
    h3("End devices"),
    p("An <strong>end device</strong> is where a message starts or ends: PCs, laptops, phones, tablets, printers, IP phones, smart TVs, servers and IoT sensors. Each has a <strong>network interface card (NIC)</strong>, wired or wireless, with a unique <strong>MAC address</strong> burned in by the maker. When comparing end devices, look at how they connect (wired, wireless or both), the speed of their NIC, and whether they are mobile."),
    h3("Switches"),
    switch_fig(),
    p("A <strong>switch</strong> connects devices inside one LAN. It works at <strong>layer 2</strong> of the OSI model using MAC addresses: it learns which device is on each port and sends each frame only where it needs to go, instead of to everyone like an old hub. Characteristics to compare: number of ports (8, 24, 48), speed (100 Mbps, 1 Gbps, 10 Gbps), <strong>PoE</strong> (power over Ethernet for phones and APs), whether it is <strong>managed</strong> (VLANs, security, monitoring) and whether it can also route (a layer 3 switch)."),
    h3("Routers"),
    p("A <strong>router</strong> connects <em>different</em> networks, for example your LAN to the internet or a head office to a branch. It works at <strong>layer 3</strong> using IP addresses, keeps a <strong>routing table</strong> of known networks, and chooses the best path for each packet. Routes can be typed in by an administrator (<strong>static routing</strong>) or learned automatically from other routers with a routing protocol such as RIP or OSPF (<strong>dynamic routing</strong>). Home routers combine a router, a switch, an access point and a firewall in one box."),
    h3("Wireless access points"),
    p("An <strong>access point (AP)</strong> lets wireless devices join a wired network. It broadcasts a network name (<strong>SSID</strong>), uses an 802.11 standard, and should use strong security (WPA2 or WPA3). Compare APs on standard, speed, range, number of users, and whether they are managed centrally."),
    h3("Connection media"),
    table(["Media", "How it carries data", "Max distance", "Speed", "Cost", "Use it for"], [
        ["UTP copper (Cat5e/6/6a)", "electrical signals on twisted pairs", "100 m", "1–10 Gbps", "low", "desks, APs and printers to switches"],
        ["STP copper", "as UTP, with a metal shield", "100 m", "1–10 Gbps", "medium", "near electrical noise, e.g. factories"],
        ["Fibre optic", "pulses of light in glass", "hundreds of metres to many km", "10–100+ Gbps", "high", "between floors, buildings and switches; long links; immune to interference"],
        ["Wireless (radio)", "radio waves at 2.4/5/6 GHz", "tens of metres indoors", "hundreds of Mbps to Gbps", "low per device", "mobile devices, hard-to-cable areas"],
        ["Coaxial (legacy)", "copper core with a screen", "up to about 500 m", "lower", "medium", "old networks and cable TV/broadband"],
    ], caption="Choosing connection media"),
    real_world("an office build", "The cabling contractor runs Cat6 UTP from every desk to switches in a cupboard on each floor, runs fibre between the floor cupboards and the main server room, fits PoE switches so the IP phones and ceiling APs need no separate power, and brings a fibre broadband line into the edge router."),
    terms([
        ("NIC", "network interface card: the hardware that connects a device to a network."),
        ("MAC address", "a 48-bit hardware address, written in hex, e.g. 00-1A-2B-3C-4D-5E."),
        ("Switch", "connects devices within a LAN and forwards frames using MAC addresses (layer 2)."),
        ("Router", "connects different networks and forwards packets using IP addresses (layer 3)."),
        ("PoE", "power over Ethernet: power sent down the network cable to phones, APs and cameras."),
        ("SSID", "the name a wireless network broadcasts."),
    ]),
    tryit("watch a switch learn", [
        "Build four PCs connected to one switch, all in 192.168.1.0/24.",
        "Switch to Simulation mode and ping from PC0 to PC2. Watch the first frame flood to every port.",
        "Ping again: now the switch knows where PC2 is and sends the frame to one port only.",
        "Click the switch, open the CLI and type <code>show mac address-table</code> to see what it learned.",
    ]),
    assignment_link("A.P2 and A.M1", "Task 2 is a table of functions and characteristics for each component. Task 3 (Merit) asks you to <em>analyse</em>: explain how the components work together and why each one is needed to build a LAN, a WAN and a wireless network, with diagrams showing data moving from one device to another."),
    think([
        ("What is the main difference between a switch and a router?", "A switch connects devices in the same network using MAC addresses; a router connects different networks together using IP addresses."),
        ("Why would you use fibre between two buildings 300 m apart?", "Copper Ethernet only reaches 100 m. Fibre reaches much further, is faster and is not affected by electrical interference or lightning between buildings."),
    ]),
)


# ---------------- A2b Software ----------------
A2b = lesson("A2b", "A2 Network components", "Network software: operating systems, tools and applications",
    "explain the software that runs, monitors, troubleshoots and uses a network.", "Assignment 1 · A.P2",
    h3("Networking systems software"),
    p("A <strong>network operating system</strong> (such as Windows Server or Linux) provides services like logins, file sharing and DHCP. Network devices run their own system software too: Cisco switches and routers run <strong>IOS</strong>, configured through a command line. Other systems software includes firewall and security software, virtualisation and cloud management tools."),
    table(["Tool", "What it does", "Example use"], [
        ["<code>ping</code>", "sends echo requests to test if a device can be reached, and how quickly", "Can this PC reach the server at 192.168.1.10?"],
        ["<code>tracert</code> / <code>traceroute</code>", "lists every router a packet passes through", "Where along the route is the delay or break?"],
        ["<code>ipconfig</code> / <code>ip a</code>", "shows a device's IP address, mask, gateway and DNS", "Did this laptop get an address from DHCP?"],
        ["<code>nslookup</code>", "asks DNS to translate a name into an IP address", "Is DNS working for www.example.com?"],
        ["<code>netstat</code>", "shows open connections and listening ports", "Which services are running on this server?"],
        ["Wireshark (packet sniffer)", "captures and decodes the packets travelling on the network", "Is the DHCP server replying? Is data being sent unencrypted?"],
        ["Event Viewer / system logs", "records errors, warnings, logins and security events", "Why did the server restart last night? Who failed to log in?"],
        ["Performance Monitor / monitoring dashboards", "graphs CPU, memory, disk and network use over time", "Is the server overloaded at 9 a.m.?"],
        ["Nmap", "scans a network to discover devices and open ports", "Audit your own lab network for unexpected open ports (only with permission)"],
    ], caption="Monitoring, management and troubleshooting tools"),
    h3("Network applications"),
    p("These are programs that exist because of the network: email, web browsers, video calls and VoIP, shared databases (for example a stock or student records system), document management systems (shared editing with version history), remote access tools and cloud storage apps. When you plan a network, list the applications first, because they decide the bandwidth, servers and security you need."),
    terms([
        ("Network operating system", "an OS that provides services to other computers on a network."),
        ("Packet sniffer", "software that captures network traffic so it can be inspected."),
        ("Event log", "a record of what happened on a system, with time stamps."),
        ("Baseline", "a record of normal performance, used to spot problems later."),
    ]),
    think([
        ("A user says 'the internet is down'. <code>ping 8.8.8.8</code> works but <code>ping www.bbc.co.uk</code> fails. What is the likely problem?", "The connection works (an IP address can be reached) but names are not being turned into addresses, so DNS is the likely fault."),
        ("Why must you have permission before using Nmap or Wireshark on a network?", "They can reveal other people's devices and data. Using them on a network you do not own or manage without permission can break the law (the Computer Misuse Act) and school rules."),
    ]),
)


# ---------------- A3 OSI / TCP-IP ----------------
def osi_fig():
    s = SVG(760, 420, "The OSI model beside the TCP/IP model")
    osi = [("7 Application", "HTTP, DNS, SMTP"), ("6 Presentation", "encryption, formats"), ("5 Session", "start/stop sessions"), ("4 Transport", "TCP, UDP · ports"), ("3 Network", "IP · routers"), ("2 Data link", "Ethernet, Wi-Fi · MAC · switches"), ("1 Physical", "cables, radio, bits")]
    pdu = ["Data", "Data", "Data", "Segment", "Packet", "Frame", "Bits"]
    fills = ["#fbf0dd", "#fbf0dd", "#fbf0dd", "#e8f1e4", "#dcebf6", "#eef0f3", "#eef0f3"]
    s.text(160, 24, "OSI model (7 layers)", size=14, bold=True)
    s.text(470, 24, "TCP/IP model", size=14, bold=True)
    s.text(650, 24, "Unit of data", size=14, bold=True)
    for i, (a, b) in enumerate(osi):
        y = 36 + i * 52
        s.box(40, y, 240, 46, a, b, size=13, fill=fills[i])
        s.box(600, y + 6, 100, 34, pdu[i], size=12, fill="white")
    tcp = [("Application", 0, 3), ("Transport", 3, 1), ("Internet", 4, 1), ("Network access", 5, 2)]
    for name, start, span in tcp:
        s.box(380, 36 + start * 52, 180, span * 52 - 6, name, size=14, fill=fills[start], bold=True)
    s.text(380, 410, "Please Do Not Throw Sausage Pizza Away  →  Physical, Data link, Network, Transport, Session, Presentation, Application", size=11, color=ARROW)
    return s.render("The OSI model splits communication into seven layers; the TCP/IP model used on the internet groups them into four.")


def encap_fig():
    s = SVG(760, 250, "Encapsulation as data moves down the layers")
    rows = [("Application", [("Data (e.g. a web page request)", 360, "#fbf0dd")]),
            ("Transport", [("TCP header: ports", 140, "#e8f1e4"), ("Data", 360, "#fbf0dd")]),
            ("Internet", [("IP header: IP addresses", 150, "#dcebf6"), ("TCP", 70, "#e8f1e4"), ("Data", 290, "#fbf0dd")]),
            ("Network access", [("Ethernet header: MACs", 150, "#eef0f3"), ("IP", 60, "#dcebf6"), ("TCP", 60, "#e8f1e4"), ("Data", 230, "#fbf0dd"), ("Trailer: FCS", 90, "#fbe3d4")])]
    for i, (layer, parts) in enumerate(rows):
        y = 20 + i * 55
        s.text(20, y + 26, layer, size=12, anchor="start", bold=True)
        x = 150
        for t, w, f in parts:
            s.box(x, y, w, 38, t, size=11, fill=f, rx=2)
            x += w
    s.text(380, 243, "Sending: each layer adds its own header (encapsulation). Receiving: each layer removes it (de-encapsulation).", size=12, color=ACCENT)
    return s.render("Encapsulation wraps the data in headers, like putting a letter in an envelope, then in a parcel, then on a lorry.")


A3 = lesson("A3", "A3 Communication standards and protocols", "The OSI and TCP/IP models, ports and encapsulation",
    "describe the OSI and TCP/IP layers, how data is encapsulated, and why protocols and port numbers matter.", "Assignment 1 · A.M1",
    p("A <strong>protocol</strong> is a set of rules that both ends agree on, such as how to address a message, how big each piece is and what to do if part goes missing. Layered models split the job of networking into smaller tasks, so each layer can be designed, understood and troubleshot on its own, and equipment from different makers can work together."),
    osi_fig(),
    encap_fig(),
    h3("TCP or UDP?"),
    table(["", "TCP", "UDP"], [
        ["Connection", "sets up a connection first (the three-way handshake: SYN, SYN-ACK, ACK)", "no set-up: just sends"],
        ["Reliability", "numbers segments, acknowledges them and re-sends any that are lost", "no acknowledgements or re-sending"],
        ["Speed", "slower, more overhead", "faster, less overhead"],
        ["Used for", "web pages, email, file transfer", "live video and voice (VoIP), online games, DNS lookups"],
    ], caption="The two transport protocols"),
    h3("Ports and sockets"),
    p("An IP address gets data to the right <em>device</em>; a <strong>port number</strong> gets it to the right <em>program</em> on that device. A web server listens on port 443 for HTTPS, while the same server's email service listens on 25. An IP address plus a port, such as <code>192.168.1.10:443</code>, is called a <strong>socket</strong>, which lets one computer hold many conversations at once."),
    table(["Protocol", "Port", "Job"], [
        ["HTTP / HTTPS", "80 / 443", "web pages (HTTPS is encrypted)"],
        ["DNS", "53", "names to IP addresses"],
        ["DHCP", "67 / 68", "hands out IP addresses automatically"],
        ["SMTP", "25 (587 for clients)", "sending email"],
        ["POP3 / IMAP", "110 / 143 (995 / 993 secure)", "collecting email"],
        ["FTP / SFTP", "20–21 / 22", "file transfer (SFTP is encrypted)"],
        ["SSH / Telnet", "22 / 23", "remote command line (Telnet is not encrypted)"],
        ["RDP", "3389", "remote desktop"],
        ["NTP", "123", "keeps clocks in time"],
    ], caption="Well-known port numbers"),
    terms([
        ("Protocol", "an agreed set of rules for communication."),
        ("PDU", "protocol data unit: the name for data at a layer (segment, packet, frame, bits)."),
        ("Encapsulation", "adding a header (and sometimes a trailer) as data moves down the layers."),
        ("Port number", "a number that identifies a service or program on a device."),
        ("Socket", "an IP address combined with a port number."),
    ]),
    tryit("see encapsulation", [
        "Build a PC, a switch and a server with HTTP turned on.",
        "In Simulation mode, open the PC's web browser and go to the server's IP address.",
        "Click each coloured envelope in the event list and open the <em>OSI Model</em> and <em>Inbound/Outbound PDU</em> tabs to see the headers added at each layer.",
    ]),
    think([
        ("At which layer does a switch work, and at which does a router work?", "A switch works at layer 2 (data link) using MAC addresses; a router works at layer 3 (network) using IP addresses."),
        ("Why does a video call use UDP rather than TCP?", "Speed matters more than perfection. Waiting for a lost piece of audio to be re-sent would freeze the call, so it is better to skip it and keep going."),
    ]),
)


# ---------------- A4 Services ----------------
def dns_fig():
    s = SVG(760, 250, "How DNS finds the IP address for a name")
    device(s, "laptop", 20, 90, "Your PC")
    s.box(200, 80, 150, 60, "Local DNS server", "(ISP or company)", size=13)
    s.box(470, 20, 140, 44, "Root server", size=12)
    s.box(470, 100, 140, 44, ".uk TLD server", size=12)
    s.box(470, 180, 140, 44, "bbc.co.uk server", size=12)
    s.arrow(86, 106, 198, 106, label="1 www.bbc.co.uk?", ly=-10, lsize=11)
    s.arrow(350, 96, 468, 44, both=True, label="2", ly=-4, lsize=11)
    s.arrow(350, 110, 468, 122, both=True, label="3", ly=-6, lsize=11)
    s.arrow(350, 124, 468, 200, both=True, label="4", ly=-4, lsize=11)
    s.arrow(198, 126, 86, 126, label="5 it is 151.101.0.81", ly=18, lsize=11, color=ACCENT)
    s.text(680, 110, "The answer is", size=11)
    s.text(680, 126, "cached, so the", size=11)
    s.text(680, 142, "next lookup is", size=11)
    s.text(680, 158, "instant", size=11)
    return s.render("DNS turns names people can remember into the IP addresses computers use. Answers are cached to save time.")


def dhcp_fig():
    s = SVG(760, 200, "The four DHCP messages")
    device(s, "laptop", 30, 70, "New device")
    device(s, "server", 660, 70, "DHCP server")
    msgs = [("Discover", "Is there a DHCP server? (broadcast)", True), ("Offer", "You can have 192.168.1.50", False), ("Request", "Yes please, I'll take .50", True), ("Acknowledge", "It's yours for 8 days: mask, gateway, DNS", False)]
    for i, (m, d, right) in enumerate(msgs):
        y = 30 + i * 40
        if right:
            s.arrow(110, y + 14, 650, y + 14, width=2)
        else:
            s.arrow(650, y + 14, 110, y + 14, width=2, color=ACCENT)
        s.text(380, y + 8, f"{i + 1}. {m}: {d}", size=12, bold=(i == 3))
    return s.render("DHCP gives each device an IP address, subnet mask, default gateway and DNS server automatically (remember DORA).")


A4 = lesson("A4", "A4 Infrastructure services and resources", "Network services: DNS, DHCP, directory, authentication and more",
    "explain what each infrastructure service does and why a network needs it.", "Assignment 1 · A.P2, A.M1",
    p("Hardware carries the data, but <strong>services</strong> make the network useful. Most run on servers, and in Assignment 2 you will set several of them up yourself."),
    h3("DNS: names to numbers"),
    dns_fig(),
    h3("DHCP: automatic addresses"),
    dhcp_fig(),
    p("Without DHCP an administrator would type an address into every device, and mistakes (two devices with the same address) would be common. DHCP hands out addresses from a <strong>pool</strong> (scope) for a set time (the <strong>lease</strong>). Servers, printers and network devices usually keep <strong>static</strong> addresses so they are always easy to find, while PCs, laptops and phones use DHCP."),
    table(["Service", "What it does", "Why the network needs it"], [
        ["Directory service (e.g. Active Directory, LDAP)", "a central database of users, groups, computers and printers", "one login for every PC; manage accounts and policies in one place"],
        ["Authentication (and AAA)", "checks who you are (authentication), what you may do (authorisation), and records what you did (accounting); e.g. RADIUS for Wi-Fi logins", "only the right people get in, with the right rights, and there is an audit trail"],
        ["Routing and remote access (RAS / VPN)", "connects networks together and lets staff connect securely from home", "reach other sites and work remotely without exposing the network"],
        ["NAT", "lets many private addresses share one public address", "saves public IPv4 addresses and hides the inside of the network"],
        ["File services", "shared folders with permissions (SMB, NFS, FTP/SFTP)", "one safe, backed-up copy of files for a team"],
        ["Print services", "a print server queues and manages jobs for shared printers", "control who prints, track use, install drivers centrally"],
        ["Web services", "serve web pages and web apps (HTTP/HTTPS)", "an intranet, a public website, e-commerce"],
        ["Mail services", "SMTP sends mail between servers; IMAP/POP3 let users collect it", "internal and external email"],
        ["Communication services", "VoIP phones, video calls, instant messaging", "cheaper calls and collaboration over the data network"],
    ], caption="Infrastructure services and resources"),
    real_world("logging in at school", "When you log in, your PC asks the directory service (authentication). DHCP already gave your PC its address, DNS finds the file server by name, the file server shows only the folders your group may open, and the print server sends your work to the nearest printer."),
    terms([
        ("DNS", "domain name system: translates names such as example.com into IP addresses."),
        ("DHCP", "dynamic host configuration protocol: automatically gives devices their IP settings."),
        ("Lease", "how long a device may keep an address from DHCP."),
        ("Directory service", "a central database of users and resources used for logins and permissions."),
        ("AAA", "authentication, authorisation and accounting."),
        ("VPN", "virtual private network: an encrypted tunnel over the internet."),
    ]),
    tryit("DHCP and DNS servers", [
        "Add a server, a switch and three PCs. Give the server the static address 192.168.1.2/24.",
        "On the server, open <em>Services → DHCP</em>: set default gateway 192.168.1.1, DNS 192.168.1.2, start address 192.168.1.100, and turn the service on.",
        "Open <em>Services → DNS</em>: add the name <code>intranet.local</code> pointing to 192.168.1.2 and turn DNS on. Turn on HTTP too.",
        "On each PC choose <em>DHCP</em> in IP Configuration: they should receive an address.",
        "In a PC's browser go to <code>intranet.local</code>: the web page proves DHCP, DNS and HTTP all work.",
    ]),
    think([
        ("Why should a network printer have a static IP address rather than one from DHCP?", "Computers and the print server need to find it at the same address every time. If DHCP gave it a new address, printing would stop working."),
        ("A laptop shows the address 169.254.12.7. What has gone wrong?", "It is an automatic private (APIPA) address, which means the laptop could not reach a DHCP server, so it gave itself an address and cannot reach the rest of the network."),
    ]),
)

LESSONS = [A1a, A1b, A1c, A1d, A2a, A2b, A3, A4]
