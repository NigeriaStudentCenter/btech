from u7_a import *  # noqa
from u7_a import SVG, device, INK, LINE, ARROW, ACCENT, WARN, exam_tip, spec
import sec_a as u19a


def vnet_fig():
    s = SVG(760, 240, "Virtual clients, switch and router inside one host")
    s.box(20, 20, 720, 200, fill="#f6f9fc", stroke="#6b7f90")
    s.text(380, 42, "One physical host running a hypervisor", size=14, bold=True)
    for i, t in enumerate(["Virtual PC 1", "Virtual PC 2", "Virtual server"]):
        s.box(40 + i * 150, 70, 130, 50, t, size=12, fill="white")
        s.line(105 + i * 150, 120, 380, 160, color="#8aa5b8", width=1.6)
    s.box(320, 150, 120, 40, "Virtual switch", size=12, fill="#dcebf6")
    s.box(520, 150, 120, 40, "Virtual router", size=12, fill="#e8f1e4")
    s.arrow(440, 170, 518, 170, width=1.8)
    s.arrow(640, 170, 730, 170, width=1.8)
    s.text(690, 160, "real NIC", size=10)
    return s.render("Virtual machines, switches and routers are software, but they behave like real devices, so whole networks can run inside one server.")


V1 = lesson("V1", "7.4 Virtual environments", "Virtual machines, hypervisors and virtual environments",
    "explain virtual machine clients and servers, type 1 and type 2 hypervisors, and the key features, benefits and drawbacks of virtual environments.", spec("7.4.1 – 7.4.4"),
    u19a.hypervisor_fig(),
    table(["Component", "What it is"], [
        ["Virtual machine (client)", "a software computer: a virtual PC, or network devices such as a virtual switch or virtual router"],
        ["Virtual machine (server)", "a server OS running as a VM, e.g. web, email or database server"],
        ["Type 1 hypervisor", "‘bare metal’: installed directly on the hardware; efficient and secure; used in data centres (ESXi, Hyper-V, Proxmox)"],
        ["Type 2 hypervisor", "‘hosted’: an application on a normal OS; easy to set up; good for testing and learning (VirtualBox, VMware Workstation)"],
    ], caption="7.4.1 Components"),
    vnet_fig(),
    table(["Key feature (7.4.2)", "Meaning"], [
        ["Increased security", "each VM is separated, so a problem in one is contained; snapshots allow quick roll-back"],
        ["Managed execution", "the hypervisor controls and limits the CPU, memory and storage each VM can use"],
        ["Sharing", "one physical machine’s resources are shared between many VMs"],
        ["Aggregation", "resources from several physical machines can be pooled and managed as one"],
        ["Emulation", "a VM can imitate different hardware or operating systems"],
        ["Isolation", "VMs cannot see or affect each other"],
        ["Portability", "a VM is a set of files that can be copied, backed up or moved to another host"],
    ], caption="Key features of virtual environments"),
    table(["Benefits (7.4.3)", "Drawbacks (7.4.4)"], [
        ["cost-effective for large environments (fewer physical servers); easy central management; resilience (move VMs if a host fails); potentially lower carbon footprint (less hardware and power); improved disaster recovery (copy and restore VMs); better testing environments (safe, disposable copies); education and training (labs without extra kit)",
         "extra load on the host hardware; slower execution than running directly on hardware; performance can be falsely represented, because a VM’s speed depends on the host and the other VMs sharing it"],
    ], caption="Benefits and drawbacks"),
    terms([("Virtual machine", "a software emulation of a computer."), ("Hypervisor", "software that creates and manages virtual machines."), ("Snapshot", "a saved state of a VM that can be restored."), ("Host / guest", "the physical machine / the virtual machine running on it.")]),
    exam_tip("Balance benefits and drawbacks for the scenario. A school running 30 practice servers benefits hugely; a single high-performance game server may run better on bare hardware."),
    think([("Why is a type 2 hypervisor fine for a student but not for a data centre?", "It runs on top of a normal OS, which adds overhead and another thing that can fail; a type 1 hypervisor runs directly on the hardware for better performance and security."),
           ("How does virtualisation improve disaster recovery?", "Whole VMs can be copied or snapshotted and restored quickly on other hardware, instead of rebuilding a physical server from scratch.")]),
)


def cloud_resp_fig():
    s = SVG(760, 300, "Who manages what in IaaS, PaaS and SaaS")
    layers = ["User accounts", "Data", "Application software", "Runtime", "System software (middleware, OS)", "Virtualisation", "Hardware (servers, network, storage)"]
    client = {"IaaS": 5, "PaaS": 3, "SaaS": 2}
    order = {"IaaS": [0, 1, 2, 3, 4], "PaaS": [0, 1, 2], "SaaS": [0, 1]}
    for c, name in enumerate(["IaaS", "PaaS", "SaaS"]):
        x = 60 + c * 230
        s.text(x + 100, 24, name, size=15, bold=True)
        for r, l in enumerate(layers):
            mine = r in order[name]
            s.box(x, 34 + r * 33, 200, 28, l, size=11, fill="#f6c89a" if mine else "#bcd6f0", stroke="#b58a3a" if mine else LINE, rx=3)
    s.text(380, 290, "Orange = the client manages it   ·   Blue = the cloud provider manages it", size=12)
    return s.render("The specification’s split of responsibilities. With SaaS the client only manages user accounts and data.")


C1 = lesson("C1", "7.5 Cloud environments", "Cloud types, benefits and delivery models",
    "compare private and public clouds, explain the benefits of cloud, and describe IaaS, PaaS and SaaS and who manages what.", spec("7.5.1 – 7.5.3"),
    table(["", "Private cloud", "Public cloud"], [
        ["Owned / used by", "one organisation (on-site or hosted for it alone)", "a provider shares its infrastructure with many customers (AWS, Azure, Google Cloud)"],
        ["Control and security", "full control; data kept separate", "less control; security shared with the provider"],
        ["Cost", "high up-front cost; needs in-house skills", "pay as you go; no hardware to buy"],
        ["Scaling", "limited by hardware owned", "almost unlimited, very quickly"],
    ], caption="7.5.1 Types of cloud"),
    table(["Benefit (7.5.2)", "Meaning"], [
        ["Portability", "data and services can be reached from anywhere, on any device; workloads can move between locations"],
        ["Elasticity", "resources scale up at busy times and down when quiet, automatically"],
        ["Fewer storage limitations", "storage can grow as needed without buying disks"],
        ["Cost effectiveness", "pay only for what is used; no hardware, power or maintenance costs"],
    ], caption="Benefits of cloud"),
    cloud_resp_fig(),
    table(["Model", "Example", "Advantages", "Disadvantages"], [
        ["IaaS", "renting virtual servers (e.g. Azure VMs, AWS EC2)", "most control and flexibility; no hardware to buy", "client must manage and secure the OS and everything above it; needs skills"],
        ["PaaS", "a platform to deploy code (e.g. Azure App Service, Heroku)", "developers focus on code; provider patches the OS and runtime", "less control; may be tied to one provider’s platform"],
        ["SaaS", "ready-made software in a browser (e.g. Microsoft 365, Gmail)", "no installation or maintenance; available anywhere", "least control and customisation; depends on the provider and internet"],
    ], caption="7.5.3 Cloud delivery models"),
    terms([("Elasticity", "automatically adding or removing resources to match demand."), ("IaaS", "infrastructure as a service."), ("PaaS", "platform as a service."), ("SaaS", "software as a service.")]),
    exam_tip("Learn the responsibility split exactly as in the specification: IaaS client manages application software, system software (middleware and OS), runtime, data and user accounts; PaaS client manages application software, data and user accounts; SaaS client manages only user accounts and data."),
    think([("An online shop gets 20 times more visitors on Black Friday. Which cloud benefit helps most?", "Elasticity: extra servers are added automatically for the peak and removed afterwards, so the shop only pays for them while needed."),
           ("Which delivery model gives a developer the least server administration while still running their own code?", "PaaS: the provider manages the OS, middleware and runtime; the developer manages the application and data.")]),
)


def sites_fig():
    s = SVG(760, 220, "Hot, warm and cold standby sites")
    rows = [("Hot site", "fully equipped, systems running and data mirrored", "minutes", "most expensive", "#fbe3d4", 60), ("Warm site", "equipment ready, data restored from recent backups", "hours to a day", "moderate cost", "#fbf0dd", 240), ("Cold site", "space, power and connections only; equipment must be installed", "days to weeks", "cheapest", "#dcebf6", 520)]
    for i, (a, b, t, c, f, w) in enumerate(rows):
        y = 25 + i * 60
        s.box(20, y, 130, 46, a, size=14, fill=f, bold=True)
        s.text(160, y + 20, b, size=12, anchor="start")
        s.text(160, y + 38, c, size=11, anchor="start", color=ARROW)
        s.add(f'<rect x="{540}" y="{y + 14}" width="{w * 0.2:.0f}" height="18" fill="{WARN if i == 0 else ACCENT if i == 1 else LINE}"/>')
        s.text(540 + w * 0.2 + 6, y + 28, t, size=11, anchor="start")
    s.text(600, 18, "time to recover", size=11, color=ARROW)
    return s.render("A standby site lets an organisation keep working after a disaster. The faster the recovery, the higher the cost.")


R1 = lesson("R1", "7.6 Resilient digital environments", "Resilience: benefits and methods",
    "explain the benefits of resilient environments and the methods used to improve resilience.", spec("7.6.1 · 7.6.2"),
    p("A <strong>resilient</strong> digital environment keeps working, or recovers quickly, when something goes wrong: a failed disk, a cyber attack, a power cut, a flood or a mistake by a member of staff."),
    table(["Benefit (7.6.1)", "Impact on organisations and clients"], [
        ["Increased security", "data is protected in storage and in transfer; fewer vulnerabilities for attackers to exploit"],
        ["Increased reputation", "protects the brand and image; customers keep their confidence and stay"],
        ["Reduction in downtime", "services stay available, so sales, work and customer service continue"],
    ], caption="Why resilience matters"),
    table(["Method (7.6.2)", "How it improves resilience"], [
        ["Software updates / upgrades", "planned updates add features and fixes; patches close newly found vulnerabilities quickly"],
        ["Hardware replacement", "rolling replacement plans swap old kit before it fails; secure disposal wipes or destroys drives so data cannot be recovered"],
        ["Data and system redundancy", "duplicate disks (RAID), servers, power supplies and connections remove single points of failure"],
        ["Device hardening", "remove unneeded ports, applications, permissions and access to shrink the attack surface"],
        ["Backup systems and recovery procedures", "copies kept onsite (fast restore), remote/offsite (safe from local disaster) and in the cloud; tested recovery procedures"],
        ["Hot, warm and cold sites", "an alternative location to run from after a disaster"],
        ["Standard operating procedures", "effective staff training, induction for new starters, and training for new digital systems and new or updated policies"],
    ], caption="Methods to improve resilience"),
    sites_fig(),
    dA.raid(),
    real_world("a ransomware attack", "An online retailer’s servers are encrypted by ransomware. Because it kept offsite and cloud backups, patched its systems, and had a tested recovery procedure and a warm site, it restored service within hours instead of paying the criminals or closing for weeks."),
    terms([("Resilience", "the ability to keep working or recover quickly after a problem."), ("Patch", "a software update that fixes a bug or vulnerability."), ("Device hardening", "reducing the attack surface by removing anything not needed."), ("Redundancy", "duplicate components that take over if one fails."), ("Hot site", "a fully running standby location for immediate failover.")]),
    exam_tip("For ‘evaluate’ questions on resilience, weigh cost against risk: a hospital or bank justifies a hot site and full redundancy; a small café might rely on cloud backups and a cold plan."),
    think([("Why must old hard drives be disposed of securely?", "They may still hold personal or business data, which could be recovered and misused, breaching data protection law and damaging reputation."),
           ("Give two examples of device hardening on a new server.", "Close unused ports and services, remove unneeded software and default accounts, and give users only the permissions they need.")]),
)

LESSONS = [V1, C1, R1]
