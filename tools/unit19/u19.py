"""Shared pieces for the Unit 19 Computer Networking learning page (original content)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "deeper"))
from helpers import *  # noqa: F401,F403  (SVG builder, h3, p, ul, table, terms, worked, think, real_world, esc)
from helpers import SVG, esc, INK, LINE, ARROW, ACCENT, WARN


def tryit(title, steps, note=None):
    li = "".join(f"<li>{s}</li>" for s in steps)
    n = f'<p class="small">{note}</p>' if note else ""
    return f'<div class="tryit"><h4>Try it in Packet Tracer: {esc(title)}</h4><ol>{li}</ol>{n}</div>'


def cli(lines, caption=None):
    cap = f'<p class="small">{esc(caption)}</p>' if caption else ""
    return f'<pre class="cli"><code>{esc(chr(10).join(lines))}</code></pre>{cap}'


def assignment_link(criteria, text):
    return f'<div class="assess"><h4>Links to your assignment: {esc(criteria)}</h4><p>{text}</p></div>'


def device(s, kind, x, y, label="", w=64):
    """Small original device icons, drawn with basic shapes. (x, y) = top-left."""
    stroke = LINE
    if kind == "pc":
        s.add(f'<rect x="{x+8}" y="{y}" width="{w-16}" height="34" rx="3" fill="#dcebf6" stroke="{stroke}" stroke-width="2"/>')
        s.add(f'<rect x="{x+26}" y="{y+34}" width="12" height="7" fill="{stroke}"/><rect x="{x+16}" y="{y+41}" width="32" height="4" rx="2" fill="{stroke}"/>')
    elif kind == "laptop":
        s.add(f'<rect x="{x+12}" y="{y+4}" width="{w-24}" height="28" rx="3" fill="#dcebf6" stroke="{stroke}" stroke-width="2"/>')
        s.add(f'<path d="M{x+4} {y+38} L{x+w-4} {y+38} L{x+w-12} {y+32} L{x+12} {y+32} Z" fill="{stroke}"/>')
    elif kind == "phone":
        s.add(f'<rect x="{x+22}" y="{y}" width="20" height="40" rx="4" fill="#dcebf6" stroke="{stroke}" stroke-width="2"/>')
    elif kind == "server":
        for k in range(3):
            s.add(f'<rect x="{x+14}" y="{y+k*14}" width="{w-28}" height="12" rx="2" fill="#e8f1e4" stroke="#5b8a4f" stroke-width="2"/><circle cx="{x+w-22}" cy="{y+6+k*14}" r="2" fill="#5b8a4f"/>')
    elif kind == "printer":
        s.add(f'<rect x="{x+10}" y="{y+12}" width="{w-20}" height="22" rx="3" fill="#eef0f3" stroke="{stroke}" stroke-width="2"/><rect x="{x+18}" y="{y+2}" width="{w-36}" height="12" fill="white" stroke="{stroke}" stroke-width="1.5"/><rect x="{x+18}" y="{y+30}" width="{w-36}" height="12" fill="white" stroke="{stroke}" stroke-width="1.5"/>')
    elif kind == "switch":
        s.add(f'<rect x="{x}" y="{y+10}" width="{w}" height="24" rx="4" fill="#245d83"/>')
        s.add(f'<path d="M{x+12} {y+18} L{x+w-12} {y+18} M{x+w-18} {y+14} L{x+w-12} {y+18} L{x+w-18} {y+22} M{x+12} {y+27} L{x+w-12} {y+27} M{x+18} {y+23} L{x+12} {y+27} L{x+18} {y+31}" stroke="white" stroke-width="2" fill="none"/>')
    elif kind == "router":
        s.add(f'<ellipse cx="{x+w/2}" cy="{y+22}" rx="{w/2}" ry="16" fill="#20857b"/>')
        s.add(f'<path d="M{x+w/2-14} {y+22} L{x+w/2+14} {y+22} M{x+w/2} {y+10} L{x+w/2} {y+34}" stroke="white" stroke-width="2.5"/><path d="M{x+w/2+9} {y+17} L{x+w/2+14} {y+22} L{x+w/2+9} {y+27} M{x+w/2-5} {y+15} L{x+w/2} {y+10} L{x+w/2+5} {y+15}" stroke="white" stroke-width="2" fill="none"/>')
    elif kind == "ap":
        s.add(f'<rect x="{x+12}" y="{y+22}" width="{w-24}" height="14" rx="4" fill="#245d83"/>')
        for r in (8, 14, 20):
            s.add(f'<path d="M{x+w/2-r} {y+18-r*0.2} Q{x+w/2} {y+4-r*0.6} {x+w/2+r} {y+18-r*0.2}" stroke="#245d83" stroke-width="2" fill="none"/>')
    elif kind == "firewall":
        s.add(f'<rect x="{x+8}" y="{y+4}" width="{w-16}" height="36" rx="3" fill="#fbe3d4" stroke="{WARN}" stroke-width="2"/>')
        for r in range(3):
            s.add(f'<path d="M{x+8} {y+16+r*12-4} L{x+w-8} {y+16+r*12-4}" stroke="{WARN}" stroke-width="1.5"/>')
    elif kind == "cloud":
        s.add(f'<path d="M{x+14} {y+38} Q{x} {y+38} {x+2} {y+26} Q{x+2} {y+14} {x+16} {y+16} Q{x+20} {y} {x+36} {y+6} Q{x+52} {y} {x+56} {y+16} Q{x+w+2} {y+18} {x+w-4} {y+32} Q{x+w-8} {y+40} {x+w-16} {y+38} Z" fill="#eef4fa" stroke="{stroke}" stroke-width="2"/>')
    elif kind == "storage":
        for k in range(2):
            s.add(f'<ellipse cx="{x+w/2}" cy="{y+8+k*16}" rx="{w/2-8}" ry="6" fill="#e8f1e4" stroke="#5b8a4f" stroke-width="2"/>')
        s.add(f'<path d="M{x+8} {y+8} L{x+8} {y+34} Q{x+w/2} {y+44} {x+w-8} {y+34} L{x+w-8} {y+8}" fill="none" stroke="#5b8a4f" stroke-width="2"/>')
    elif kind == "ipphone":
        s.add(f'<rect x="{x+14}" y="{y+10}" width="{w-28}" height="28" rx="4" fill="#eef0f3" stroke="{stroke}" stroke-width="2"/><path d="M{x+14} {y+10} Q{x+w/2} {y-4} {x+w-14} {y+10}" fill="none" stroke="{stroke}" stroke-width="4"/>')
    if label:
        s.text(x + w / 2, y + 60, label, size=12)
    return s


def lesson(sid, code, title, goal, criteria, *blocks):
    inner = "".join(blocks)
    crit = f'<span class="crit">{esc(criteria)}</span>' if criteria else ""
    return (f'<article id="{sid}"><p class="goal">{esc(code)} {crit}</p><h2>{esc(title)}</h2>'
            f'<p class="aim"><strong>By the end you can:</strong> {goal}</p>{inner}'
            f'<a class="next" href="index.html?section={sid}">Continue to workbook {sid} →</a></article>')
