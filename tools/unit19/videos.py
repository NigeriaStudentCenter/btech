"""Unit 19 videos: embedded from the publishers' or official uploads on YouTube (click to load, privacy-enhanced mode).
The original MP4 files stay with the teacher on Teams; they are third-party copyright and are not re-hosted here."""
from html import escape

VIDEOS = [
 {"id": "ksvEw-ULgIQ", "lesson": "A1a", "title": "Types of computer networks: LAN, MAN and WAN", "channel": "Make It Easy Education",
  "why": "A quick overview of network types by size.", "think": ["Which network type covers a whole city?", "Name one reason a LAN is faster than a WAN."]},
 {"id": "5boN5SrrlWQ", "lesson": "A1a", "title": "Internet vs intranet vs extranet", "channel": "Jelvix | TECH IN 5 MINUTES",
  "why": "Explains who can reach each kind of network.", "think": ["Give an example of an extranet a company might use.", "Why would an intranet not be visible from the internet?"]},
 {"id": "VkeOpmcMzL0", "lesson": "A1c", "title": "What is a thin client? Benefits and uses", "channel": "IT Junction",
  "why": "Shows what a thin client is and where it fits best (useful for A.D1).", "think": ["What happens to thin-client users if the server goes down?", "Name one organisation that would suit thin clients, and why."]},
 {"id": "mxT233EdY5c", "lesson": "A1d", "title": "What is cloud computing?", "channel": "Amazon Web Services",
  "why": "A cloud provider’s own short explanation of cloud computing.", "think": ["What does “pay for what you use” mean for a small business?"]},
 {"id": "M988_fsOSWo", "lesson": "A1d", "title": "Cloud computing in 6 minutes", "channel": "Simplilearn",
  "why": "Covers cloud types and service models (IaaS, PaaS, SaaS).", "think": ["Which service model gives the customer the most control?", "Give one risk of moving to the public cloud."]},
 {"id": "Z5Gi2Bpd82M", "lesson": "A1d", "title": "What is software-defined networking (SDN)?", "channel": "TECHtalk",
  "why": "Explains how SDN controls a network centrally with software.", "think": ["What is the difference between the control plane and the data plane?"]},
 {"id": "4RsLUTJ_Qtk", "lesson": "A1d", "title": "Introduction to storage area network (SAN) technologies", "channel": "Kevin Wallace Training",
  "why": "How SANs give servers fast, shared storage.", "think": ["Why keep storage traffic on its own network?"]},
 {"id": "Bud-mqaBKPM", "lesson": "A1d", "title": "Internet of Everything: Circle Story", "channel": "Cisco advert (uploaded by PERRY proTECH, a Cisco partner)", "duration": "1:00",
  "why": "Cisco’s one-minute film of a day where connected devices trigger each other: a starter for IoT and its risks.", "think": ["List three connected devices in the film.", "What could go wrong if one of them was hacked?"]},
 {"id": "EOYe71RWMvk", "lesson": "A3", "title": "Warriors of the Net (full length original)", "channel": "Ericsson, 1999", "duration": "12:57",
  "why": "A classic animation that follows packets through routers, switches, firewalls and the internet: perfect for OSI, TCP/IP and encapsulation.", "think": ["What job does the router do in the film?", "What happens to a packet that is lost on the way?", "Which OSI layers can you spot?"]},
 {"id": "j0EZpH_eIsY", "lesson": "B3", "title": "Anatomy of an Attack: inside the mind of a hacker", "channel": "Cisco (produced by Kraft Technology Group)", "duration": "4:00",
  "why": "A dramatised ransomware attack showing why passwords, patching, access rights and monitoring matter.", "think": ["How did the attacker get in?", "Which part of your access plan (passwords, groups, audit logs) would have stopped them sooner?"]},
 {"id": "jn8ymi1aIgY", "lesson": "B1a", "title": "Completion of the Long Beach Container Terminal", "channel": "Port of Long Beach (via OOCL)",
  "why": "A real, fully automated port where every crane, vehicle and gate depends on the network. VectorUSA and Cisco designed and built it.",
  "extra": ("Read the VectorUSA and Cisco case study", "https://blog.vectorusa.com/vector-usa-and-cisco-team-up-to-build-a-fully-automated-container-terminal"),
  "think": ["Which design aims (availability, redundancy, security, scalability) matter most here, and why?", "What would happen to the port if the network failed?"]},
]


def card(v):
    e = lambda t: escape(str(t), quote=True)
    think = "".join(f"<li>{e(q)}</li>" for q in v["think"])
    dur = f' · {e(v["duration"])}' if v.get("duration") else ""
    extra = f'<p class="small"><a href="{e(v["extra"][1])}" target="_blank" rel="noopener">{e(v["extra"][0])} ↗</a></p>' if v.get("extra") else ""
    return (f'<div class="video" data-yt="{e(v["id"])}"><div class="vframe"><button type="button" class="vplay" aria-label="Play video: {e(v["title"])}">'
            f'<span class="vicon" aria-hidden="true">▶</span><span class="vtitle">{e(v["title"])}</span><span class="vmeta">{e(v["channel"])}{dur}</span>'
            f'<span class="vnote">Plays from YouTube (privacy-enhanced) when you press play</span></button></div>'
            f'<div class="vbody"><p>{e(v["why"])}</p><p class="small"><strong>Watch and think:</strong></p><ul class="small">{think}</ul>'
            f'<p class="small"><a href="https://www.youtube.com/watch?v={e(v["id"])}" target="_blank" rel="noopener">Open on YouTube ↗</a></p>{extra}</div></div>')


CSS = """.video{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:16px;background:#f4f8fb;border:1px solid #d1dce6;border-radius:12px;padding:14px;margin:18px 0}
.vframe{position:relative;aspect-ratio:16/9;border-radius:10px;overflow:hidden;background:#12324f}.vframe iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.vplay{position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:0;background:linear-gradient(135deg,#12324f,#20857b);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;padding:14px;text-align:center;cursor:pointer}
.vplay:hover,.vplay:focus-visible{outline:3px solid #e8a33d;outline-offset:-3px}.vicon{font-size:2.2rem;line-height:1;background:rgba(255,255,255,.18);border-radius:50%;width:64px;height:64px;display:flex;align-items:center;justify-content:center}
.vtitle{font-weight:700;font-size:1rem}.vmeta{font-size:.82rem;opacity:.9}.vnote{font-size:.72rem;opacity:.75}.vbody p{margin:4px 0}.vbody ul{margin:4px 0 4px 18px;padding:0}
@media(max-width:700px){.video{grid-template-columns:1fr}}"""

JS = """document.addEventListener('click',e=>{const b=e.target.closest('.vplay');if(!b)return;const v=b.closest('.video'),id=v.dataset.yt;if(!/^[A-Za-z0-9_-]{11}$/.test(id))return;
const f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0';f.title=b.querySelector('.vtitle').textContent;f.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';f.allowFullscreen=true;f.referrerPolicy='strict-origin-when-cross-origin';b.replaceWith(f)});"""


def for_lesson(lid):
    vs = [v for v in VIDEOS if v["lesson"] == lid]
    if not vs:
        return ""
    return f'<h3>Watch</h3>{"".join(card(v) for v in vs)}'
