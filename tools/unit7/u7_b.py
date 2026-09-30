from u7_a import *  # noqa  (helpers, exam_tip, spec, device, SVG, diagrams)
from u7_a import SVG, device, INK, LINE, ARROW, ACCENT, WARN, exam_tip, spec
import sec_a as u19a  # Unit 19 original diagrams
import section_e as dE


def vpn_fig():
    s = SVG(760, 220, "A VPN tunnel across the internet")
    device(s, "laptop", 20, 70, "Home worker")
    device(s, "cloud", 330, 60)
    s.text(365, 135, "Public internet", size=12)
    device(s, "router", 600, 72, "Office VPN gateway")
    device(s, "server", 690, 150, "")
    s.add(f'<path d="M92 92 C200 40 540 40 598 92" stroke="{ACCENT}" stroke-width="10" fill="none" opacity="0.35"/>')
    s.add(f'<path d="M92 92 C200 40 540 40 598 92" stroke="{ACCENT}" stroke-width="2.5" fill="none" stroke-dasharray="6 5"/>')
    s.text(345, 36, "encrypted tunnel: data looks like gibberish to anyone in between", size=12, color=ACCENT)
    s.text(380, 200, "The laptop behaves as if it were plugged into the office network", size=12)
    return s.render("A virtual private network (VPN) creates an encrypted connection over a public network, so remote users can reach private resources securely.")


N1 = lesson("N1", "7.3 Networks", "Why we network, and types of network",
    "explain the benefits and drawbacks of networking devices, and the features of PAN, LAN, MAN, WAN and VPN.", spec("7.3.1 · 7.3.2"),
    table(["Benefits of connecting devices", "Drawbacks"], [
        ["share files, printers and internet connections; communicate (email, chat, VoIP); central backups and security; collaborate on the same data; manage devices centrally", "cost of equipment and set-up; needs specialist staff; security risks (malware can spread); a failure of a key device can stop everyone; performance drops when the network is busy"],
    ], caption="7.3.1 Why connect devices?"),
    u19a.scale_fig(),
    table(["Type", "Number of users", "Connection and coverage", "Example"], [
        ["PAN", "one person", "a few metres; Bluetooth, USB", "phone to earbuds and a smartwatch"],
        ["LAN", "a few to thousands", "one building or site; Ethernet cables and Wi-Fi", "school or office network"],
        ["MAN", "many organisations", "a town or city; fibre links", "council network linking libraries"],
        ["WAN", "millions", "countries and continents; leased lines, fibre, satellite", "the internet; a bank linking its branches"],
        ["VPN", "authorised remote users", "runs over another network, usually the internet, encrypted", "staff working from home reaching office files"],
    ], caption="7.3.2 Network types"),
    vpn_fig(),
    terms([("LAN", "local area network: one site."), ("WAN", "wide area network: large geographical area."), ("VPN", "virtual private network: an encrypted tunnel across a public network."), ("Coverage", "the geographical area a network reaches.")]),
    think([("Give one drawback of networking computers in a small office.", "Malware can spread from one infected computer to all the others, or the whole office stops if the router fails."),
           ("Why does a VPN matter for someone on public café Wi-Fi?", "Everything is encrypted between the laptop and the VPN gateway, so others on the café network cannot read it.")]),
)


def media_fig():
    s = SVG(760, 230, "Copper, fibre and wireless compared")
    s.text(380, 22, "Relative comparison (longer bar = more)", size=12, color=ARROW)
    cats = ["Speed", "Distance", "Interference resistance", "Cost to install", "Mobility"]
    vals = {"Copper (Ethernet)": [3, 1, 2, 1, 0], "Fibre optic": [5, 5, 5, 4, 0], "Wireless (Wi-Fi)": [2, 1, 1, 1, 5]}
    cols = {"Copper (Ethernet)": "#b58a3a", "Fibre optic": ACCENT, "Wireless (Wi-Fi)": LINE}
    for i, c in enumerate(cats):
        y = 45 + i * 36
        s.text(170, y + 18, c, size=12, anchor="end")
        for j, (m, v) in enumerate(vals.items()):
            s.add(f'<rect x="180" y="{y + j * 10}" width="{max(v[i] * 60, 2)}" height="8" fill="{cols[m]}"/>')
    for j, m in enumerate(vals):
        s.add(f'<rect x="{560}" y="{60 + j * 26}" width="16" height="12" fill="{cols[m]}"/>')
        s.text(584, 71 + j * 26, m, size=12, anchor="start")
    return s.render("No medium wins on everything: networks mix copper to desks, fibre for backbones and long runs, and wireless for mobile devices.")


N2 = lesson("N2", "7.3 Networks", "Connectivity: copper, fibre and wireless",
    "compare the features, benefits and drawbacks of copper Ethernet, fibre-optic and wireless connections.", spec("7.3.3"),
    table(["Method", "How it works", "Benefits", "Drawbacks"], [
        ["Copper / Ethernet (e.g. Cat6 UTP)", "electrical signals over twisted pairs of copper wire", "cheap, easy to fit, reliable, fast (1–10 Gbps), can carry power (PoE)", "max about 100 m per run; affected by electrical interference; cables must reach each device"],
        ["Fibre optic", "pulses of light through glass strands", "very high speed and bandwidth; long distances (km); immune to interference; hard to tap", "expensive; fragile; needs specialist installation and equipment"],
        ["Wireless (access points)", "radio waves between devices and a wireless access point (Wi-Fi 802.11)", "mobility; no cables; quick to add users; supports phones and tablets", "slower and less reliable than cable; range limited by walls; interference; must be secured (WPA2/WPA3)"],
    ], caption="7.3.3 Connectivity methods"),
    media_fig(),
    terms([("UTP", "unshielded twisted pair: the usual copper network cable."), ("Wireless access point", "connects wireless devices to a wired network."), ("Attenuation", "a signal getting weaker over distance."), ("Interference", "unwanted signals that corrupt data.")]),
    tryit("wireless access point", ["Build a switch with two wired PCs and an AccessPoint-PT.", "Set the SSID and WPA2-PSK passphrase on the AP (Config → Port 1).", "Give a laptop a wireless card (WPC300N) and the same settings.", "Ping a wired PC from the laptop."]),
    exam_tip("Scenario questions often ask you to recommend a connection: weigh distance, speed, cost, interference and mobility against what the organisation actually needs."),
    think([("Why would a hospital use fibre between buildings?", "The distance is too far for copper, fibre carries huge amounts of data such as scans, and it is not affected by electrical interference from medical equipment."),
           ("Give one reason an office might still wire desks with copper when it has Wi-Fi.", "Wired connections are faster and more reliable for desktop PCs, and do not share bandwidth with every wireless user.")]),
)


N3 = lesson("N3", "7.3 Networks", "Topologies and network models",
    "compare star, mesh and tree topologies, physical and logical topologies, and client-server, thin client and peer-to-peer models.", spec("7.3.4 · 7.3.5"),
    u19a.topo_fig(),
    table(["Topology", "Features", "Benefits", "Drawbacks"], [
        ["Star", "every device has its own cable to a central switch", "a cable fault affects one device; easy to add devices and find faults", "the switch is a single point of failure; lots of cable"],
        ["Mesh", "devices connect to many (full mesh: all) others", "many routes, so it keeps working if links fail; good for WANs and wireless mesh", "expensive and complex; many connections to manage"],
        ["Tree (hierarchical)", "stars joined in layers from a central root", "scales well; easy to extend by adding branches; faults contained in a branch", "if the root or a trunk link fails, whole branches are cut off"],
    ], caption="7.3.4 Topologies"),
    p("The <strong>physical topology</strong> is how the cables and devices are actually laid out. The <strong>logical topology</strong> is how data flows between devices. They can differ: a network can be cabled as a star but pass data around logically like a ring or bus."),
    u19a.models_fig(),
    table(["Model", "Benefits", "Drawbacks"], [
        ["Client-server", "central storage, logins, security and backups; scales to many users", "servers and skilled staff cost money; if a server fails, services stop"],
        ["Thin client", "cheap, simple desk devices; data stays on the server; easy central management", "depends completely on the network and server; poor for heavy graphics"],
        ["Peer-to-peer", "cheap and easy to set up; no server needed", "hard to manage and secure beyond a few devices; backups scattered; slower when a peer is busy"],
    ], caption="7.3.5 Network models"),
    terms([("Physical topology", "the actual layout of devices and cables."), ("Logical topology", "the way data flows through the network."), ("Single point of failure", "one component whose failure stops the whole system."), ("Thin client", "a simple device relying on a server for processing and storage.")]),
    think([("Why is a tree topology suited to a large school on several floors?", "Each floor or block can be a star connected to a central switch, so it is easy to extend, and a fault stays within one branch."),
           ("Give one reason a two-person start-up might choose peer-to-peer.", "It needs no server or network administrator, so it is cheap and quick to set up for a few devices.")]),
)


def backbone_fig():
    s = SVG(760, 250, "From a home network to the internet backbone")
    device(s, "laptop", 20, 30, "Devices")
    device(s, "router", 130, 32, "Home router")
    s.box(232, 30, 146, 50, "ISP", "local exchange / cabinet", size=13, fill="#dcebf6")
    s.box(400, 30, 140, 50, "ISP core network", size=13, fill="#dcebf6")
    s.box(580, 20, 160, 70, "Internet backbone", "tier 1 networks, internet\nexchange points (IXPs)", size=13, fill="#fbf0dd")
    s.arrow(86, 52, 128, 54, width=1.8)
    s.arrow(196, 54, 230, 55, width=1.8)
    s.text(214, 105, "DSL / cable / fibre", size=11, color=ARROW)
    s.arrow(378, 55, 398, 55, width=1.8)
    s.arrow(540, 55, 578, 55, width=1.8)
    for i, (t, x) in enumerate([("Undersea fibre cables", 60), ("Data centres and cloud", 300), ("Other ISPs and countries", 540)]):
        s.box(x, 160, 200, 50, t, size=12, fill="white")
        s.line(660, 90, x + 100, 158, color="#b9c7d5", width=1.6)
    return s.render("Your internet connection links your home or office to an ISP, whose network joins the high-capacity backbone that carries traffic between networks and continents.")


N4 = lesson("N4", "7.3 Networks", "Network components and the internet backbone",
    "explain the role of servers, clients, routers, switches and the internet connection and backbone.", spec("7.3.6"),
    table(["Component", "Role"], [
        ["Server", "provides services to clients: files, web, email, printing, databases, DHCP, DNS, authentication"],
        ["Client", "a device that requests and uses services: PCs, laptops, phones"],
        ["Switch", "connects devices within a LAN; forwards frames only to the correct port using MAC addresses"],
        ["Router", "connects different networks; forwards packets between them using IP addresses; usually links a LAN to the internet"],
        ["Internet connection", "the link from the organisation to its ISP (fibre, cable, DSL, 4G/5G, leased line)"],
        ["Internet backbone", "the very high-capacity links and routers (tier 1 networks, exchange points, undersea cables) that join networks worldwide"],
    ], caption="7.3.6 Common network components"),
    u19a.switch_fig(),
    backbone_fig(),
    table(["Server type", "Service"], [["File server", "shared folders with permissions"], ["Web server", "hosts websites (HTTP/HTTPS)"], ["Mail server", "sends and stores email (SMTP, IMAP/POP)"], ["Print server", "manages print queues"], ["Database server", "stores and queries data for applications"], ["DHCP / DNS server", "hands out IP addresses / turns names into IP addresses"], ["Proxy server", "requests web content on behalf of clients; filters and caches"]], caption="Common server types"),
    terms([("Switch", "connects devices in a LAN using MAC addresses."), ("Router", "connects networks and routes packets using IP addresses."), ("ISP", "internet service provider."), ("Internet backbone", "the high-capacity core links of the internet.")]),
    tryit("home network to the internet", ["Build a home LAN (PCs, switch or home router).", "Add a Cloud-PT and a cable or DSL modem between the home router and the cloud.", "In the cloud, connect the modem’s interface to the Ethernet interface leading to a server.", "Ping the server, then swap DSL for cable and compare."], "Based on the teacher’s ‘Simulating a home network to the internet’ practical."),
    think([("What is the difference between the role of a switch and a router?", "A switch connects devices within one network using MAC addresses; a router connects different networks and forwards packets between them using IP addresses."),
           ("Why are undersea cables part of the internet backbone?", "They carry most data between continents at very high capacity, which satellites cannot match.")]),
)


def tcpip_fig():
    s = SVG(760, 230, "TCP/IP layers with example protocols")
    rows = [("Application", "HTTP, HTTPS, SMTP, POP, IMAP, FTP, SFTP, DNS, DHCP", "#fbf0dd"), ("Transport", "TCP (reliable) · UDP (fast)", "#e8f1e4"), ("Internet", "IP addressing and routing · RIP, OSPF", "#dcebf6"), ("Network (access)", "Ethernet, Wi-Fi · MAC addresses · frames and bits", "#eef0f3")]
    for i, (a, b, f) in enumerate(rows):
        y = 20 + i * 50
        s.box(40, y, 200, 42, a, size=14, fill=f, bold=True)
        s.box(250, y, 470, 42, b, size=13, fill="white")
    return s.render("The four-layer TCP/IP model used on the internet, with protocols from the specification at each layer.")


N5 = lesson("N5", "7.3 Networks", "The OSI and TCP/IP models",
    "describe the function and related protocols of each layer of the seven-layer OSI model and the four-layer TCP/IP model.", spec("7.3.7 · 7.3.8"),
    u19a.osi_fig(),
    table(["OSI layer", "Function", "Example protocols / devices"], [
        ["7 Application", "network services for applications", "HTTP, HTTPS, FTP, SMTP, DNS"],
        ["6 Presentation", "formats, encrypts and compresses data", "TLS/SSL, JPEG, ASCII"],
        ["5 Session", "starts, manages and ends sessions", "session set-up and checkpoints"],
        ["4 Transport", "end-to-end delivery, ports, splitting into segments, reliability", "TCP, UDP"],
        ["3 Network", "logical addressing and routing between networks", "IP, RIP, OSPF · routers"],
        ["2 Data link", "frames, MAC addresses, error detection on a link", "Ethernet, Wi-Fi · switches"],
        ["1 Physical", "transmits bits as signals over the medium", "cables, radio, fibre · hubs"],
    ], caption="7.3.7 OSI model"),
    tcpip_fig(),
    u19a.encap_fig(),
    terms([("Protocol", "an agreed set of rules for communication."), ("Encapsulation", "each layer adds its own header to the data."), ("TCP", "reliable, connection-based transport."), ("UDP", "fast, connectionless transport without re-sending.")]),
    exam_tip("Learn one job and two protocols for every layer. Questions often give a protocol and ask for its layer, or ask why layers help (standards, interoperability, easier troubleshooting)."),
    think([("Which OSI layers are combined into the TCP/IP application layer?", "Application, presentation and session (layers 7, 6 and 5)."),
           ("At which layer does encryption with TLS take place in the OSI model?", "The presentation layer (layer 6), which handles encryption, compression and data formats.")]),
)


def packet_fig():
    s = SVG(760, 200, "The structure of a data packet")
    parts = [("Header", ["source and destination IP", "sequence number · protocol", "TTL · packet length"], 300, "#dcebf6"), ("Payload", ["the actual data", "(part of a file, email, video)"], 260, "#fbf0dd"), ("Trailer", ["error check (CRC)", "end marker"], 180, "#fbe3d4")]
    x = 10
    for t, d, w, f in parts:
        s.box(x, 30, w, 56, t, size=15, fill=f, bold=True)
        for k, line in enumerate(d):
            s.text(x + w / 2, 110 + k * 16, line, size=11)
        x += w
    s.text(380, 170, "Routers read the header to forward the packet; the receiver uses", size=12, color=ACCENT)
    s.text(380, 188, "the sequence number and CRC to rebuild and check the data.", size=12, color=ACCENT)
    return s.render("Every packet carries a header (addressing and control), a payload (the data) and a trailer (error checking).")


N6 = lesson("N6", "7.3 Networks", "Data packets, packet switching and error handling",
    "describe the structure of a data packet, the role of each part, packet switching, causes of packet loss and CRC.", spec("7.3.9"),
    packet_fig(),
    table(["Part", "Contents", "Role"], [
        ["Header", "source and destination IP addresses, sequence number, protocol, time to live (TTL), length", "tells routers where to send the packet and the receiver how to reassemble it"],
        ["Payload", "a chunk of the data being sent", "the useful content"],
        ["Trailer", "CRC or checksum, end-of-packet marker", "lets the receiver detect corruption"],
    ], caption="Components of a packet"),
    dE.switching(),
    table(["Cause of packet loss", "Why it happens"], [["Congestion", "routers or links are overloaded and drop packets from full queues"], ["Faulty hardware or cables", "damaged equipment corrupts or drops signals"], ["Wireless interference / weak signal", "radio noise and distance corrupt packets"], ["Time to live expires", "a packet travels through too many routers (e.g. a routing loop) and is discarded"], ["Software bugs or misconfiguration", "wrong routes or firewall rules drop packets"]], caption="Causes of packet loss"),
    dE.crc_fig(),
    terms([("Packet switching", "splitting data into packets that travel independently and are reassembled."), ("Sequence number", "the packet’s position, used to reassemble the data in order."), ("TTL", "time to live: the number of router hops before a packet is discarded."), ("CRC", "cyclic redundancy check: an error-detection value calculated from the data.")]),
    think([("Why can packets from the same file arrive out of order?", "Each packet is routed independently and can take a different path with different delays; the sequence numbers let the receiver put them back in order."),
           ("What happens when the receiver’s CRC calculation does not match?", "The packet is treated as corrupted and discarded; with TCP the sender re-sends it after no acknowledgement arrives.")]),
)


N7 = lesson("N7", "7.3 Networks", "Common network protocols",
    "explain the role of web, mail, routing and application protocols: HTTP, HTTPS, SMTP, POP, IMAP, RIP, OSPF, FTP, SFTP, DHCP and DNS.", spec("7.3.10"),
    table(["Group", "Protocol", "Role", "Port"], [
        ["Web", "HTTP", "transfers web pages between browser and server (not encrypted)", "80"],
        ["Web", "HTTPS", "HTTP encrypted with TLS: protects logins, payments and personal data", "443"],
        ["Mail", "SMTP", "sends email from client to server and between mail servers", "25 / 587"],
        ["Mail", "POP (POP3)", "downloads email to one device, usually deleting it from the server", "110 / 995"],
        ["Mail", "IMAP", "keeps email on the server and synchronises it across devices", "143 / 993"],
        ["Routing", "RIP", "routers share routes; chooses the path with the fewest hops (max 15)", "–"],
        ["Routing", "OSPF", "link-state routing: builds a map of the network and chooses the lowest-cost (fastest) path", "–"],
        ["Application", "FTP", "transfers files (not encrypted)", "20 / 21"],
        ["Application", "SFTP", "secure file transfer over SSH (encrypted)", "22"],
        ["Application", "DHCP", "automatically gives devices an IP address, mask, gateway and DNS server", "67 / 68"],
        ["Application", "DNS", "translates domain names into IP addresses", "53"],
    ], caption="7.3.10 Protocols in the specification"),
    u19a.dhcp_fig(),
    u19a.dns_fig(),
    terms([("Port number", "identifies which service or application data is for."), ("Hop", "one step from one router to the next."), ("Link-state", "a routing method where routers share a full map of links and their costs.")]),
    tryit("DHCP and DNS servers", ["Add a server with static IP 192.168.1.2.", "Turn on DHCP (pool from .100, gateway .1, DNS .2) and DNS (A record intranet.local → 192.168.1.2) and HTTP.", "Set PCs to DHCP, then browse to intranet.local."]),
    exam_tip("Compare POP and IMAP carefully: POP downloads to one device; IMAP keeps mail on the server and syncs every device. A common question asks which suits a worker who uses a phone and a laptop."),
    think([("Why is RIP less suitable than OSPF for a large network?", "RIP only counts hops (maximum 15) and ignores link speed, so it may pick a slow route; OSPF uses link costs, scales better and adapts faster to changes."),
           ("Which protocol should a web designer use to upload files to a client’s server, and why?", "SFTP, because it encrypts the login and the files, unlike FTP.")]),
)


def bandwidth_fig():
    s = SVG(760, 230, "Bandwidth and latency as a pipe")
    s.text(190, 26, "Bandwidth = how wide the pipe is", size=14, bold=True)
    s.box(30, 50, 320, 26, fill="#dcebf6", rx=13)
    s.text(190, 68, "low bandwidth: little data per second", size=11)
    s.box(30, 95, 320, 70, fill="#bcd6f0", rx=35)
    s.text(190, 135, "high bandwidth: lots of data per second", size=12)
    s.text(190, 200, "measured in Mbps or Gbps", size=12, color=ACCENT)
    s.text(570, 26, "Latency = how long the pipe is", size=14, bold=True)
    s.box(430, 60, 120, 30, fill="#e8f1e4", rx=15)
    s.text(490, 80, "short: low delay", size=11)
    s.box(430, 115, 300, 30, fill="#fbe3d4", rx=15)
    s.text(580, 135, "long: high delay (e.g. satellite)", size=11)
    s.text(570, 200, "measured in milliseconds (ms), e.g. by ping", size=12, color=ACCENT)
    return s.render("Bandwidth is the amount of data a connection can carry per second; latency is the delay before data arrives. They affect different kinds of application.")


N8 = lesson("N8", "7.3 Networks", "Bandwidth and latency",
    "explain bandwidth and latency and their effect on the performance of networks and connected systems.", spec("7.3.11"),
    bandwidth_fig(),
    table(["Application", "Needs high bandwidth?", "Needs low latency?", "Why"], [
        ["Streaming 4K video", "yes", "not very", "lots of data, but buffering hides short delays"],
        ["Online gaming", "not much", "yes", "small updates must arrive instantly or play lags"],
        ["Video calls / VoIP", "moderate", "yes", "delay causes people to talk over each other"],
        ["Large file downloads / backups", "yes", "no", "total time depends on how much data per second"],
        ["Remote control of machinery or surgery", "moderate", "critical", "a delay could be dangerous"],
    ], caption="How bandwidth and latency affect applications"),
    worked("Download time", [
        "A 2 GB file is 2,000 MB = 16,000 megabits (× 8).",
        "On a 100 Mbps connection: 16,000 ÷ 100 = 160 seconds (about 2 min 40 s).",
        "On a 20 Mbps connection: 16,000 ÷ 20 = 800 seconds (over 13 minutes).",
        "Latency barely matters here; bandwidth decides the time.",
    ], "Remember: bandwidth is usually in bits per second, file sizes in bytes, so multiply bytes by 8."),
    p("Performance also depends on <strong>contention</strong> (many users sharing the same bandwidth), <strong>distance</strong> and the number of hops, congestion and packet loss (which causes re-sends), and the slowest link in the path."),
    terms([("Bandwidth", "the maximum data a connection can carry per second."), ("Latency", "the delay for data to travel from source to destination."), ("Throughput", "the data actually delivered per second."), ("Jitter", "variation in latency, which disrupts calls and games.")]),
    think([("Why can a satellite connection feel slow for gaming even with good bandwidth?", "The signal travels to a satellite and back, adding high latency, so each action takes noticeably longer to register."),
           ("How long does a 500 MB file take to download at 50 Mbps?", "500 × 8 = 4,000 megabits; 4,000 ÷ 50 = 80 seconds.")]),
)

LESSONS = [N1, N2, N3, N4, N5, N6, N7, N8]
