# TOPIK II Yozish (쓰기) 51 — Templates (grammatik shakllar). Manba: material_51_patterns.json
# (51_done.pptx dan ajratilgan grammatik shakl (template) slaydlari). Til: O'zbekcha + Koreyscha, styling bilan.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_writing_51_patterns.py --author=prime
# (--republish bilan yangilanadi).

import json
import os
import html

_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_DIR, "material_51_patterns.json"), encoding="utf-8") as _f:
    _PATTERNS = {p["slide"]: p for p in json.load(_f)}

# slide -> O'zbekcha funksiya nomi (qo'lda tuzilgan)
_GRAMMAR = {
    2:  "Reja bildirish",
    3:  "Fikr / qulaylikni so'rash",
    7:  "Muloyim (rasmiy) ifodalar",
    9:  "Iltimos qilish (rasmiy)",
    10: "Iltimos qilish (norasmiy)",
    11: "Eshitganni yetkazish (bilvosita nutq)",
    17: "Yumshoq / bilvosita aytish",
    24: "Va'da / niyat bildirish",
    26: "Minnatdorchilik / uzr",
    42: "Ravish–kelishik moslashuvi (혹시, 꼭, 만약…)",
}
_VOCAB = {
    19: "Va'da / uchrashuv fe'llari",
    27: "Sotib olish / sotish",
    28: "Topshirish / ariza / bron",
    33: "O'zgartirish / bekor / kechiktirish",
}

TRACK = {
    "name":    "TOPIK",
    "summary": "TOPIK II Koreys tili imtihoniga bosqichma-bosqich tayyorgarlik — "
               "O'qish, Yozish va Tinglash bo'yicha strategiya va amaliyot.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
    "order":   1,
}


def _line_li(line):
    s = html.escape(line)
    # Grammatik shakl (form) — qalin; misol/izoh — kulrang.
    if line.startswith("•") or line.startswith("예)"):
        return f'<li style="color:#475569;">{s}</li>'
    if ("→" in line) or any(t in line for t in ("V-", "N-", "A-", "A/V", "-(으)")):
        return f'<li><strong>{s}</strong></li>'
    return f'<li style="color:#475569;">{s}</li>'


def _pattern_card(slide, uz_label, border):
    p = _PATTERNS[slide]
    title = html.escape(p["title"].lstrip("◈ ").strip())
    lines = "".join(_line_li(l) for l in p["lines"])
    return f"""
<div style="background:#ffffff;border-left:4px solid {border};box-shadow:0 1px 2px rgba(0,0,0,.06);padding:12px 16px;border-radius:8px;margin:14px 0;">
  <p style="margin:0 0 6px;"><strong style="font-size:1.06em;">{title}</strong>
     &nbsp;—&nbsp;<span style="color:{border};">{html.escape(uz_label)}</span></p>
  <ul style="margin:0;line-height:1.7;">{lines}</ul>
</div>
"""


_INTRO = """
<h2>TOPIK Writing 51: Templates (grammatik shakllar)</h2>
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">쓰기 51</span>
&nbsp;<span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">templates</span></p>
<p>쓰기 51 javoblari bir nechta <strong>funksional template</strong> (reja aytish, iltimos qilish,
uzr so'rash...) atrofida quriladi. Quyida real javoblardan ajratilgan template'lar va foydali
leksika bor.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Qanday ishlatish:</strong> har bir funksiya uchun <strong>bitta</strong> template'ni
  tanlab yodlang (전략 darsi!). Keyin <em>Amaliy namunalar</em> qismlarida shu template'larni
  amalda ko'rasiz. <span style="color:#475569;">Qalin — grammatik shakl; kulrang — misol.</span>
</div>
"""

_CLOSING = """
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> hammasini emas — har funksiyadan bittadan template'ni mukammal
  egallang. Shunda 쓰기 51 da har qanday mavzuga tez va xatosiz javob yozasiz.
</div>
"""

_blocks = [{"rich_text": _INTRO}]

_blocks.append({"rich_text": "<h3>1) 기능 표현 — Funksional template'lar</h3>"})
for _s in sorted(_GRAMMAR):
    _blocks.append({"rich_text": _pattern_card(_s, _GRAMMAR[_s], "#a855f7")})

_blocks.append({"rich_text": '<h3>2) 어휘 — Foydali leksika</h3>'})
for _s in sorted(_VOCAB):
    _blocks.append({"rich_text": _pattern_card(_s, _VOCAB[_s], "#10b981")})

_blocks.append({"rich_text": _CLOSING})

LESSONS = [
    {
        "skill":   "writing",
        "title":   "TOPIK Writing 51: Templates (grammatik shakllar)",
        "summary": "쓰기 51 uchun funksional grammatik template'lar (reja, iltimos, uzr...) va "
                   "foydali leksika — real javoblardan ajratilgan.",
        "order":   2,
        "blocks":  _blocks,
    },
]
