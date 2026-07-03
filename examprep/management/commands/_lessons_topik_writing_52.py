# TOPIK II Yozish (쓰기) 52 — izohli matndagi bo'sh joylarni to'ldirish. Manba: material_52.json
# (Claude tomonidan real imtihon uslubida tuzilgan). Til: O'zbekcha + Koreyscha, styling bilan.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_writing_52.py --author=prime

import os
import json
import html

_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_DIR, "material_52.json"), encoding="utf-8") as _f:
    _D = json.load(_f)

TRACK = {
    "name":    "TOPIK",
    "summary": "TOPIK II Koreys tili imtihoniga bosqichma-bosqich tayyorgarlik — "
               "O'qish, Yozish va Tinglash bo'yicha strategiya va amaliyot.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
    "order":   1,
}

_BADGE = ('<span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;'
          'font-size:0.85em;">쓰기 52</span>')


def _blank(mark):
    return (f'<span style="background:#fef3c7;border-bottom:2px solid #f59e0b;padding:0 24px;'
            f'border-radius:3px;font-weight:700;">{mark}</span>')


def _passage_html(passage):
    p = html.escape(passage)
    p = p.replace("( ㉠ )", _blank("㉠")).replace("( ㉡ )", _blank("㉡"))
    return p


def _answers(label, answers):
    joined = " &nbsp;/&nbsp; ".join(f'<span style="color:#065f46;">{html.escape(a)}</span>'
                                    for a in answers)
    return f'<p style="margin:4px 0;"><strong>{label}</strong> &nbsp;{joined}</p>'


# ── Lesson 1: yondashuv + template'lar ──────────────────────────────────
def _template_card(t):
    ex = ""
    if t.get("ex_q") and t["ex_q"] != "—":
        ex = (f'<div style="background:#f8fafc;border-radius:8px;padding:8px 12px;margin-top:8px;">'
              f'<span style="color:#334155;">{html.escape(t["ex_q"])}</span><br>'
              f'<span style="color:#065f46;">→ {html.escape(t["ex_a"])}</span></div>')
    return f"""
<div style="background:#ffffff;border-left:4px solid #a855f7;box-shadow:0 1px 2px rgba(0,0,0,.06);padding:12px 16px;border-radius:8px;margin:14px 0;">
  <p style="margin:0 0 4px;"><strong style="font-size:1.05em;">{html.escape(t["title"])}</strong></p>
  <p style="margin:0 0 4px;color:#7c3aed;font-weight:600;">{html.escape(t["signals"])}</p>
  <p style="margin:0;color:#475569;">{html.escape(t["uz"])}</p>
  {ex}
</div>
"""


_L1_INTRO = """
<h2>TOPIK Writing 52: Yondashuv va grammatik shakllar</h2>
<p>{badge} &nbsp;<span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">izohli matn · ㉠ ㉡</span></p>
<p>쓰기 52 — bu qisqa <strong>izohli (ilmiy-obyektiv) matn</strong> bo'lib, ikkita bo'sh joyni
(<mark style="background:#fef3c7;">㉠</mark>, <mark style="background:#fef3c7;">㉡</mark>)
matnning <strong>mantiqiga</strong> mos jumla bilan to'ldirasiz. 51 dan farqi — bu xat emas,
umumiy mavzudagi izoh.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Yondashuv (3 qadam):</strong>
  <ol style="margin:8px 0 0;">
    <li><strong>Butun matnni o'qing</strong> — mavzuni tushuning.</li>
    <li>Bo'sh joy atrofidagi <strong>signal so'zga</strong> qarang (그러나 · 또한 · 왜냐하면 · 그러므로).</li>
    <li>Signalga mos <strong>mantiq + grammatik shakl</strong>ni tanlang (pastdagi jadval).</li>
  </ol>
</div>
""".replace("{badge}", _BADGE)

_L1_CLOSING = """
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Muhim:</strong> bo'sh joyning <strong>tugatmasi</strong> atrofdagi gapга mos kelishi shart —
  masalan '왜냐하면' bo'lsa, javob '-기 때문이다' bilan tugaydi. Uslub doim <strong>rasmiy</strong>
  (저/제 yo'q). Endi <em>Amaliy namunalar</em> qismida mashq qiling.
</div>
"""

_l1_blocks = [{"rich_text": _L1_INTRO},
              {"rich_text": "<h3>신호 → 정답 — Signal bo'yicha to'ldirish jadvali</h3>"}]
for _t in _D["templates"]:
    _l1_blocks.append({"rich_text": _template_card(_t)})
_l1_blocks.append({"rich_text": _L1_CLOSING})


# ── Lesson 2: amaliy namunalar (imtihon uslubida) ───────────────────────
def _question_block(n, q):
    topic = html.escape(q["topic"])
    passage = _passage_html(q["passage"])
    reveal = (_answers("㉠", q["a"]) + _answers("㉡", q["b"]))
    return f"""
<div style="margin:20px 0 6px;"><span style="background:#1e293b;color:#fff;padding:2px 10px;border-radius:6px;font-size:0.82em;">문제 {n}</span>
&nbsp;<strong>{topic}</strong></div>
<p style="color:#64748b;font-size:0.85em;margin:0 0 6px;">다음 글을 읽고 ㉠과 ㉡에 들어갈 말을 쓰십시오.</p>
<div style="background:#fff;border:1px solid #cbd5e1;border-radius:10px;padding:16px 18px;line-height:2.15;font-size:1.03em;">{passage}</div>
<details style="background:#ecfdf5;border:1px solid #a7f3d0;border-radius:8px;padding:10px 14px;margin:8px 0 22px;">
  <summary style="cursor:pointer;font-weight:600;color:#047857;">✅ 정답 — Namunaviy javoblar (bosing)</summary>
  <div style="margin-top:8px;">{reveal}</div>
</details>
"""


_L2_INTRO = """
<h2>TOPIK Writing 52: Amaliy namunalar</h2>
<p>{badge}</p>
<p>Quyidagi har bir matnda ㉠ va ㉡ ni <strong>o'zingiz</strong> to'ldirib ko'ring, so'ng
<strong>“정답”</strong>ni ochib solishtiring. Signal so'zlarга e'tibor bering (그러나 · 또한 ·
왜냐하면 · 그러므로).</p>
""".replace("{badge}", _BADGE)

_L2_CLOSING = """
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> javob bitta so'z emas, <strong>to'liq jumla/ibora</strong> bo'lishi kerak.
  Bir nechta to'g'ri variant bo'lishi mumkin — asosiysi mantiq va grammatik shakl to'g'ri bo'lsin.
</div>
"""

_l2_blocks = [{"rich_text": _L2_INTRO}]
for _i, _q in enumerate(_D["questions"], start=1):
    _l2_blocks.append({"rich_text": _question_block(_i, _q)})
_l2_blocks.append({"rich_text": _L2_CLOSING})


LESSONS = [
    {
        "skill":   "writing",
        "title":   "TOPIK Writing 52: Yondashuv va grammatik shakllar",
        "summary": "쓰기 52 — izohli matndagi ㉠·㉡ ni signal so'zlar (대조·첨가·이유·결론) bo'yicha "
                   "to'ldirish strategiyasi.",
        "order":   10,
        "blocks":  _l1_blocks,
    },
    {
        "skill":   "writing",
        "title":   "TOPIK Writing 52: Amaliy namunalar",
        "summary": "쓰기 52 — imtihon uslubidagi 8 ta mashq matni, ㉠·㉡ va namunaviy javoblari bilan.",
        "order":   11,
        "blocks":  _l2_blocks,
    },
]
