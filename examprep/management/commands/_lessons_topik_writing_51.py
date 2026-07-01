# TOPIK II Yozish (쓰기) 51 — amaliy namunalar. Manba: material_51.json (49 ta savol+javob).
# Bu fayl material_51.json ni o'qib, 10 tadan qilib bir necha "qism"ga bo'ladi.
# Til: O'zbekcha + Koreyscha, rangli styling bilan.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_writing_51.py --author=prime
# (material_51.py ni yangilasangiz, --republish bilan qayta import qiling).

import json
import os
import html

_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_DIR, "material_51.json"), encoding="utf-8") as _f:
    _ITEMS = json.load(_f)

PER_PART = 10

TRACK = {
    "name":    "TOPIK",
    "summary": "TOPIK II Koreys tili imtihoniga bosqichma-bosqich tayyorgarlik — "
               "O'qish, Yozish va Tinglash bo'yicha strategiya va amaliyot.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
    "order":   1,
}


def _context_html(item):
    """Xat matni: qatorlarni <br> ga, bo'sh joylarni (㉠/㉡) sariq mark ga aylantirish."""
    ctx = html.escape(item["context"]).replace("\n", "<br>")
    for blank in (item.get("blank_a"), item.get("blank_b")):
        if blank:
            esc = html.escape(blank)
            ctx = ctx.replace(esc, f'<mark style="background:#fde68a;">{esc}</mark>')
    return ctx


def _answers_html(label, answers):
    joined = " &nbsp;·&nbsp; ".join(html.escape(a) for a in answers)
    return (f'<p style="margin:5px 0;"><strong>{html.escape(label)}</strong> &nbsp;'
            f'<span style="color:#065f46;">{joined}</span></p>')


def _item_block(n, item):
    ctx = _context_html(item)
    a = _answers_html(item.get("blank_a", "㉠"), item.get("answers_a", []))
    b = (_answers_html(item.get("blank_b", "㉡"), item.get("answers_b", []))
         if item.get("answers_b") else "")
    return f"""
<h3>{n}. {html.escape(item['title'])}</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:8px 0;line-height:1.75;">{ctx}</div>
<details style="background:#ecfdf5;border:1px solid #a7f3d0;border-radius:8px;padding:10px 14px;margin:8px 0 20px;">
  <summary style="cursor:pointer;font-weight:600;color:#047857;">✅ Namunaviy javoblar (bosing)</summary>
  <div style="margin-top:8px;">{a}{b}</div>
</details>
"""


def _intro_block(part_no):
    if part_no == 1:
        return """
<h2>TOPIK Writing 51: Amaliy namunalar (1-qism)</h2>
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">쓰기 51</span>
&nbsp;<span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">xat / xabar</span></p>
<p>쓰기 51 — bu qisqa <strong>xat yoki xabar</strong>; unda ikkita bo'sh joyni
(<mark style="background:#fde68a;">㉠</mark>, <mark style="background:#fde68a;">㉡</mark>)
mos jumla bilan to'ldirasiz. Quyida ko'plab real namunalar bor.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Qanday ishlatish:</strong> avval bo'sh joylarni <strong>o'zingiz</strong>
  to'ldirishga urinib ko'ring, keyin <strong>“Namunaviy javoblar”</strong>ni bosib solishtiring.
  Javobni yoddan aytmang — <mark>naqshini (naqsh = pattern)</mark> tushuning.
</div>
"""
    return f"""
<h2>TOPIK Writing 51: Amaliy namunalar ({part_no}-qism)</h2>
<p>Har bir xatda bo'sh joylarni (㉠, ㉡) o'zingiz to'ldirib, so'ng namunaviy javoblar bilan
solishtiring.</p>
"""


_CLOSING = """
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> yoqqan jumlalarni daftaringizga yozib qo'ying va
  <strong>bitta ishonchli naqshni</strong> mukammal egallang — ko'p emas, bittasini.
  (전략 darsiga qarang.)
</div>
"""


LESSONS = []
for _pi, _start in enumerate(range(0, len(_ITEMS), PER_PART), start=1):
    _chunk = _ITEMS[_start:_start + PER_PART]
    _blocks = [{"rich_text": _intro_block(_pi)}]
    for _j, _item in enumerate(_chunk, start=_start + 1):
        _blocks.append({"rich_text": _item_block(_j, _item)})
    _blocks.append({"rich_text": _CLOSING})
    LESSONS.append({
        "skill":   "writing",
        "title":   f"TOPIK Writing 51: Amaliy namunalar ({_pi}-qism)",
        "summary": f"쓰기 51 — {_start + 1}–{_start + len(_chunk)}-namunalar: xat/xabardagi "
                   f"bo'sh joylarni (㉠, ㉡) to'ldirish.",
        "order":   2 + _pi,   # 3, 4, 5, 6, 7  (patterns lesson takes order 2)
        "blocks":  _blocks,
    })
