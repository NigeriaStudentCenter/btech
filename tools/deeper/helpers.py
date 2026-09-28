"""Small helpers for writing the 'Go deeper' learning content as HTML with inline SVG.

All diagrams are original, simplified learning models drawn for this course.
"""
from html import escape

INK = "#17374f"
LINE = "#367ba5"
ARROW = "#245d83"
BG = "#edf5fb"
SOFT = "#dcebf6"
ACCENT = "#20857b"
WARN = "#b5541c"
FONT = "Arial,sans-serif"


def esc(t):
    return escape(str(t), quote=True)


class SVG:
    """Build an accessible SVG figure piece by piece."""

    def __init__(self, w, h, title, bg=True):
        self.w, self.h, self.title = w, h, title
        self.parts = []
        if bg:
            self.parts.append(f'<rect width="{w}" height="{h}" rx="12" fill="{BG}"/>')

    def add(self, raw):
        self.parts.append(raw)
        return self

    def box(self, x, y, w, h, label="", sub="", fill="white", stroke=LINE, size=15, rx=8, dash=False, color=INK, bold=False):
        d = ' stroke-dasharray="6 4"' if dash else ""
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2"{d}/>')
        cy = y + h / 2 + (size * 0.35 if not sub else -2)
        if label:
            self.text(x + w / 2, cy, label, size=size, color=color, bold=bold)
        if sub:
            self.text(x + w / 2, y + h / 2 + size * 0.95, sub, size=max(11, size - 3), color=color)
        return self

    def text(self, x, y, t, size=14, anchor="middle", color=INK, bold=False, italic=False, mono=False):
        fam = "Menlo,Consolas,monospace" if mono else FONT
        pre = ' xml:space="preserve"' if mono else ""
        wt = ' font-weight="700"' if bold else ""
        it = ' font-style="italic"' if italic else ""
        lines = str(t).split("\n")
        for i, line in enumerate(lines):
            self.parts.append(f'<text x="{x}" y="{y + i * size * 1.25:.1f}" font-family="{fam}" font-size="{size}" fill="{color}" text-anchor="{anchor}"{wt}{it}{pre}>{esc(line)}</text>')
        return self

    def line(self, x1, y1, x2, y2, color=ARROW, width=2.5, dash=False):
        d = ' stroke-dasharray="6 4"' if dash else ""
        self.parts.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="{width}" fill="none"{d}/>')
        return self

    def arrow(self, x1, y1, x2, y2, color=ARROW, width=2.5, both=False, dash=False, label="", lx=0, ly=-8, lsize=12):
        import math
        self.line(x1, y1, x2, y2, color, width, dash)
        ang = math.atan2(y2 - y1, x2 - x1)

        def head(x, y, a):
            p1 = (x - 10 * math.cos(a) + 5 * math.sin(a), y - 10 * math.sin(a) - 5 * math.cos(a))
            p2 = (x - 10 * math.cos(a) - 5 * math.sin(a), y - 10 * math.sin(a) + 5 * math.cos(a))
            self.parts.append(f'<polygon points="{x:.1f},{y:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>')
        head(x2, y2, ang)
        if both:
            head(x1, y1, ang + math.pi)
        if label:
            self.text((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, label, size=lsize, color=color)
        return self

    def circle(self, cx, cy, r, fill="white", stroke=LINE, label="", size=14):
        self.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        if label:
            self.text(cx, cy + size * 0.35, label, size=size)
        return self

    def poly(self, pts, fill="white", stroke=LINE, width=2):
        p = " ".join(f"{x},{y}" for x, y in pts)
        self.parts.append(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')
        return self

    def grid(self, x, y, cols, rows, cw, ch, values=None, fills=None, size=14, mono=True, stroke=LINE):
        for r in range(rows):
            for c in range(cols):
                f = (fills[r][c] if fills else "white") or "white"
                self.parts.append(f'<rect x="{x + c * cw}" y="{y + r * ch}" width="{cw}" height="{ch}" fill="{f}" stroke="{stroke}" stroke-width="1.5"/>')
                if values is not None and values[r][c] != "":
                    self.text(x + c * cw + cw / 2, y + r * ch + ch / 2 + size * 0.35, values[r][c], size=size, mono=mono)
        return self

    def render(self, caption):
        body = "".join(self.parts)
        return (f'<figure><svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{esc(self.title)}" xmlns="http://www.w3.org/2000/svg">'
                f'<title>{esc(self.title)}</title>{body}</svg><figcaption>{esc(caption)}</figcaption></figure>')


def h3(t):
    return f"<h3>{esc(t)}</h3>"


def p(*paras):
    """Paragraphs. Text may contain simple inline tags (<strong>, <em>, <code>) written by us."""
    return "".join(f"<p>{x}</p>" for x in paras)


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def table(head, rows, caption=None, cls="info"):
    cap = f"<caption>{esc(caption)}</caption>" if caption else ""
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tablewrap"><table class="{cls}">{cap}<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def terms(pairs):
    items = "".join(f"<dt>{esc(t)}</dt><dd>{d}</dd>" for t, d in pairs)
    return f'<div class="keyterms"><h4>Key terms</h4><dl>{items}</dl></div>'


def worked(title, steps, result=None):
    li = "".join(f"<li>{s}</li>" for s in steps)
    res = f'<p class="result"><strong>{result}</strong></p>' if result else ""
    return f'<div class="worked"><h4>Worked example: {esc(title)}</h4><ol>{li}</ol>{res}</div>'


def think(pairs):
    out = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in pairs)
    return f'<div class="think"><h4>Think it through</h4>{out}</div>'


def real_world(title, text):
    return f'<div class="realworld"><h4>In the real world: {esc(title)}</h4><p>{text}</p></div>'


def deeper(section_id, *blocks):
    inner = "".join(blocks)
    return (f'<section class="deeper" aria-labelledby="deeper-{section_id}"><h3 class="deeper-title" id="deeper-{section_id}">'
            f'Go deeper · {section_id}</h3>{inner}</section>')
