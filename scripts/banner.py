"""Draw assets/banner.svg (English) and assets/banner.fa.svg (Persian) in a frosted-glass style.

Counts come from servers.json, so run scripts/catalog.py first:  python scripts/banner.py
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
W, H = 1280, 460
ZWNJ = "&#x200C;"

# English name, Persian name, English glyph, Persian glyph, gradient top, gradient bottom
APPS = [
    ("Digikala", f"دیجی{ZWNJ}کالا", "D", "د", "#ff5a6e", "#c3002f"),
    ("Snappfood", f"اسنپ{ZWNJ}فود", "S", "ا", "#ff3dbb", "#b8006f"),
    ("Okala", "اکالا", "O", "ا", "#3fd46a", "#108a33"),
    ("Technolife", "تکنولایف", "T", "ت", "#3d7bff", "#0634a0"),
    ("MasterKala", "مسترکالا", "M", "م", "#ff8a3d", "#d14800"),
    ("Khanoumi", "خانومی", "K", "خ", "#ff5c8f", "#a3164a"),
    ("Asal Banoo", "عسل بانو", "A", "ع", "#ffcf3d", "#d48a00"),
    ("Shopino", "شاپینو", "S", "ش", "#a06bff", "#4f1fb0"),
    ("Jabama", "جاباما", "J", "ج", "#2fe0cf", "#00897e"),
    ("Otaghak", "اتاقک", "O", "ا", "#ffc23d", "#f07800"),
    ("MrBilit", "مستربلیط", "M", "م", "#4d8dff", "#0a3fa8"),
    ("Flytoday", f"فلای{ZWNJ}تودی", "F", "ف", "#3dc4ff", "#0066cc"),
    ("Paziresh24", "پذیرش۲۴", "P", "پ", "#2fd1c8", "#00706f"),
    ("Doctoreto", "دکترتو", "D", "د", "#5cb8f0", "#1565a8"),
    ("Taaghche", "طاقچه", "T", "ط", "#ff6b66", "#a31d1a"),
    ("Fidibo", "فیدیبو", "F", "ف", "#ff8a5c", "#d43a10"),
    ("30book", f"سی{ZWNJ}بوک", "30", "۳۰", "#a1887f", "#4e342e"),
    ("PayPing", f"پی{ZWNJ}پینگ", "P", "پ", "#5c8cff", "#0033cc"),
    ("Bale", "بله", "B", "ب", "#3dd9c5", "#007d71"),
]

LATIN = "'SF Pro Display','Segoe UI',Inter,Helvetica,Arial,sans-serif"
PERSIAN = "Vazirmatn,Vazir,Sahel,Tahoma,'Segoe UI',sans-serif"
MONO = "'SF Mono','JetBrains Mono','Cascadia Code',Consolas,monospace"
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

DEFS = """<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#080b24"/><stop offset="1" stop-color="#170a2e"/>
    </linearGradient>
    <g id="blobs">
      <circle cx="210" cy="90" r="190" fill="#18c8b8"/>
      <circle cx="560" cy="400" r="170" fill="#7b3fe4"/>
      <circle cx="860" cy="60" r="160" fill="#ff3d8b"/>
      <circle cx="1160" cy="380" r="210" fill="#ffb02e"/>
      <circle cx="420" cy="-40" r="120" fill="#3d7bff"/>
    </g>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
    <filter id="frost" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="28"/></filter>
    <filter id="lift" x="-30%" y="-30%" width="160%" height="170%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000" flood-opacity="0.35"/>
    </filter>
    <filter id="iconlift" x="-30%" y="-30%" width="160%" height="170%">
      <feDropShadow dx="0" dy="5" stdDeviation="5" flood-color="#000" flood-opacity="0.4"/>
    </filter>
    <linearGradient id="rim" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0.75"/>
      <stop offset="0.45" stop-color="#fff" stop-opacity="0.12"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="sheen" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0.22"/>
      <stop offset="0.5" stop-color="#fff" stop-opacity="0.06"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0.10"/>
    </linearGradient>
    <linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0.45"/>
      <stop offset="0.5" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#bff6ee"/>
    </linearGradient>
    {grads}
  </defs>"""


def glass(id_: str, x: float, y: float, w: float, h: float, r: float) -> str:
    """A frosted panel: blurred copy of the background inside, white sheen, bright rim."""
    return f"""<clipPath id="{id_}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath>
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#000" fill-opacity="0.01" filter="url(#lift)"/>
  <g clip-path="url(#{id_})">
    <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#bg)"/>
    <use href="#blobs" filter="url(#frost)" opacity="0.95"/>
    <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#sheen)"/>
  </g>
  <rect x="{x + 0.75}" y="{y + 0.75}" width="{w - 1.5}" height="{h - 1.5}" rx="{r}" fill="none" stroke="url(#rim)" stroke-width="1.5"/>"""


def pill(x: float, y: float, w: float, text: str, font: str, color: str, fa: bool) -> str:
    dot, mid = (x + w - 24, x + w / 2 - 10) if fa else (x + 24, x + w / 2 + 10)
    return f"""<rect x="{x}" y="{y}" width="{w}" height="48" rx="24" fill="#fff" fill-opacity="0.14" stroke="#fff" stroke-opacity="0.35"/>
  <circle cx="{dot}" cy="{y + 24}" r="6" fill="{color}"/>
  <text x="{mid}" y="{y + 31}" text-anchor="middle" font-family="{font}" font-size="19" font-weight="700" fill="#fff">{text}</text>"""


def icons(px: float, py: float, fa: bool) -> str:
    out = []
    size, pitch_x, pitch_y, cols = 70, 104, 94, 5
    for i, (en, fa_name, g_en, g_fa, *_) in enumerate(APPS):
        row, col = divmod(i, cols)
        if fa:
            col = cols - 1 - col  # right to left
        last_row_offset = pitch_x / 2 if row == len(APPS) // cols else 0
        x = px + col * pitch_x + (-last_row_offset if fa else last_row_offset)
        y = py + row * pitch_y
        glyph, label, font = (g_fa, fa_name, PERSIAN) if fa else (g_en, en, LATIN)
        gsize = 30 if len(glyph) > 1 else 36
        out.append(f"""<g filter="url(#iconlift)">
    <rect x="{x}" y="{y}" width="{size}" height="{size}" rx="18" fill="url(#a{i})"/>
    <rect x="{x}" y="{y}" width="{size}" height="{size / 2}" rx="18" fill="url(#gloss)"/>
    <rect x="{x + 0.5}" y="{y + 0.5}" width="{size - 1}" height="{size - 1}" rx="17.5" fill="none" stroke="#fff" stroke-opacity="0.35"/>
  </g>
  <text x="{x + size / 2}" y="{y + 47}" text-anchor="middle" font-family="{font}" font-size="{gsize}" font-weight="800" fill="#fff">{glyph}</text>
  <text x="{x + size / 2}" y="{y + size + 16}" text-anchor="middle" font-family="{font}" font-size="12.5" font-weight="600" fill="#fff" fill-opacity="0.92">{label}</text>""")
    return "\n  ".join(out)


def banner(fa: bool, servers: int, tools: int) -> str:
    grads = "\n    ".join(
        f'<linearGradient id="a{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{a[4]}"/>'
        f'<stop offset="1" stop-color="{a[5]}"/></linearGradient>'
        for i, a in enumerate(APPS)
    )
    card_x, panel_x = (650, 40) if fa else (40, 670)
    card_w, panel_w = 590, 570
    if fa:
        anchor, tx = "end", card_x + card_w - 44
        subtitle = f"وب ایران، آماده برای ایجنت{ZWNJ}های هوش مصنوعی"
        stats = [(f"{servers} سرور".translate(FA_DIGITS), "#2fe0cf", 140),
                 (f"{tools} ابزار".translate(FA_DIGITS), "#ffc23d", 140),
                 ("قیمت به تومان", "#ff5c8f", 186)]
        font, desc = PERSIAN, f"{servers} سرور MCP و {tools} ابزار برای ایجنت{ZWNJ}های هوش مصنوعی"
    else:
        anchor, tx = "start", card_x + 44
        subtitle = "The Iranian web, wired for AI agents."
        stats = [(f"{servers} servers", "#2fe0cf", 150), (f"{tools} tools", "#ffc23d", 140),
                 ("Toman prices", "#ff5c8f", 170)]
        font, desc = LATIN, f"{servers} MCP servers and {tools} tools that give AI agents the Iranian web"

    pills, x = [], tx
    for text, color, w in stats:
        if fa:
            x -= w
        pills.append(pill(x, 300, w, text, font, color, fa))
        x = x + w + 14 if not fa else x - 14

    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">awesome-iran-mcp</title>
  <desc id="d">{desc}</desc>
  {DEFS.format(grads=grads)}

  <rect width="{W}" height="{H}" rx="28" fill="url(#bg)"/>
  <g clip-path="url(#frame)"><use href="#blobs" filter="url(#soft)" opacity="0.85"/></g>
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="28"/></clipPath>

  {glass("card", card_x, 30, card_w, 400, 40)}
  {glass("panel", panel_x, 30, panel_w, 400, 40)}

  <rect x="{tx - (300 if fa else 0)}" y="70" width="300" height="38" rx="19" fill="#000" fill-opacity="0.28" stroke="#fff" stroke-opacity="0.25"/>
  <text x="{tx + (-150 if fa else 150)}" y="95" text-anchor="middle" font-family="{MONO}" font-size="16" fill="#d9fff9">$ uvx digikala-mcp</text>
  <text x="{tx}" y="196" text-anchor="{anchor}" font-family="{LATIN}" font-size="58" font-weight="800" fill="url(#ink)" letter-spacing="-1.5">awesome-iran-mcp</text>
  <text x="{tx}" y="250" text-anchor="{anchor}" font-family="{font}" font-size="25" fill="#fff" fill-opacity="0.92">{subtitle}</text>
  {chr(10).join(pills)}
  <text x="{tx}" y="396" text-anchor="{anchor}" font-family="{LATIN}" font-size="15" fill="#fff" fill-opacity="0.7">Claude · Cursor · VS Code · Windsurf · any MCP client</text>

  {icons(panel_x + 38, 46, fa)}
</svg>
"""


def main() -> None:
    catalog = json.loads((ROOT / "servers.json").read_text(encoding="utf-8"))
    servers, tools = len(catalog), sum(s["tool_count"] for s in catalog)
    for name, fa in (("banner.svg", False), ("banner.fa.svg", True)):
        (ROOT / "assets" / name).write_text(banner(fa, servers, tools), encoding="utf-8", newline="\n")
    print(f"banners written: {servers} servers, {tools} tools")


if __name__ == "__main__":
    main()
