# TOPIK II Yozish (쓰기) 53 — ILG'OR grafiklar (pie va kombinatsiya). Manba: material_53_advanced.json
# Pie diagrammalar CSS conic-gradient bilan chiziladi (rasm emas). Kombinatsiya = bir savolda ≥2 grafik.
# Til: O'zbekcha + Koreyscha. Import:
#   python manage.py import_examprep examprep/management/commands/_lessons_topik_writing_53_advanced.py --author=prime

import os
import json
import html

_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_DIR, "material_53_advanced.json"), encoding="utf-8") as _f:
    _D = json.load(_f)

TRACK = {
    "name":    "TOPIK",
    "summary": "TOPIK II Koreys tili imtihoniga bosqichma-bosqich tayyorgarlik — "
               "O'qish, Yozish va Tinglash bo'yicha strategiya va amaliyot.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
    "order":   1,
}

_PALETTE = ["#3b82f6", "#a855f7", "#10b981", "#f59e0b", "#ef4444", "#14b8a6"]


def _pie(chart):
    data = chart["data"]
    total = sum(v for _, v in data) or 100
    segs, legend, acc = [], [], 0
    for i, (label, val) in enumerate(data):
        color = _PALETTE[i % len(_PALETTE)]
        start = acc / total * 100
        acc += val
        end = acc / total * 100
        segs.append(f"{color} {start:.1f}% {end:.1f}%")
        legend.append(
            '<div style="display:flex;align-items:center;gap:6px;margin:2px 0;font-size:0.85em;">'
            f'<span style="width:12px;height:12px;border-radius:2px;background:{color};display:inline-block;flex-shrink:0;"></span>'
            f'{html.escape(label)} — <strong>{val}%</strong></div>'
        )
    title = (f'<div style="text-align:center;font-weight:600;font-size:0.9em;margin-bottom:6px;">'
             f'{html.escape(chart.get("title",""))}</div>') if chart.get("title") else ""
    return (
        '<div style="flex:0 0 auto;">'
        + title
        + '<div style="display:flex;align-items:center;gap:12px;">'
        + '<div style="position:relative;width:132px;height:132px;flex-shrink:0;">'
        + f'<div style="width:132px;height:132px;border-radius:50%;background:conic-gradient({",".join(segs)});"></div>'
        + '<div style="position:absolute;top:34px;left:34px;width:64px;height:64px;border-radius:50%;background:#fff;"></div>'
        + '</div>'
        + f'<div>{"".join(legend)}</div>'
        + '</div></div>'
    )


def _bar(chart):
    data = chart["data"]
    unit = chart.get("unit", "%")
    mx = max((v for _, v in data), default=1) or 1
    rows = ""
    for label, val in data:
        w = val / mx * 100
        rows += (
            '<div style="display:flex;align-items:center;gap:8px;margin:5px 0;">'
            f'<div style="width:96px;font-size:0.85em;text-align:right;color:#334155;">{html.escape(label)}</div>'
            '<div style="flex:1;background:#eef2f7;border-radius:6px;">'
            f'<div style="width:{w:.0f}%;min-width:44px;background:#3b82f6;color:#fff;font-size:0.78em;'
            f'padding:2px 8px;border-radius:6px;white-space:nowrap;">{val}{html.escape(unit)}</div>'
            '</div></div>'
        )
    title = (f'<div style="text-align:center;font-weight:600;font-size:0.9em;margin-bottom:4px;">'
             f'{html.escape(chart.get("title",""))}</div>') if chart.get("title") else ""
    return f'<div style="flex:1 1 240px;min-width:220px;">{title}{rows}</div>'


def _chart(chart):
    return _pie(chart) if chart.get("type") == "pie" else _bar(chart)


def _question_block(n, q):
    charts = "".join(_chart(ch) for ch in q["charts"])
    reveal = html.escape(q.get("sample_answer", ""))
    return f"""
<div style="margin:22px 0 6px;"><span style="background:#1e293b;color:#fff;padding:2px 10px;border-radius:6px;font-size:0.82em;">문제 {n}</span>
&nbsp;<strong>{html.escape(q['topic'])}</strong></div>
<p style="color:#64748b;font-size:0.85em;margin:0 0 8px;">{html.escape(q.get('instruction',''))}</p>
<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:8px 0;">
  <p style="margin:0 0 12px;line-height:1.7;">{html.escape(q.get('intro',''))}</p>
  <div style="display:flex;flex-wrap:wrap;gap:24px;justify-content:center;align-items:flex-start;">{charts}</div>
</div>
<details style="background:#ecfdf5;border:1px solid #a7f3d0;border-radius:8px;padding:10px 14px;margin:8px 0 22px;">
  <summary style="cursor:pointer;font-weight:600;color:#047857;">✅ 정답 — Namunaviy javob (bosing)</summary>
  <p style="margin:8px 0 0;line-height:1.7;">{reveal}</p>
</details>
"""


def _template_card(t):
    ex = ""
    if t.get("ex_q") and t["ex_q"] != "—":
        ex = ('<div style="background:#f8fafc;border-radius:8px;padding:8px 12px;margin-top:8px;">'
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


_INTRO = """
<h2>TOPIK Writing 53: Ilg'or grafiklar — pie va kombinatsiya</h2>
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">쓰기 53</span>
&nbsp;<span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">pie · combo</span></p>
<p>So'nggi yillarda 쓰기 53 ko'pincha <strong>bittadan ortiq grafik</strong> beradi — masalan
ikkita <mark>doiraviy (pie) diagramma</mark>ni solishtirish, yoki <mark>ustunli grafik + pie</mark>
(o'zgarish + sabab). Yondashuv o'sha-o'sha, faqat ikkinchi grafikni ham bayon qilasiz.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Ikki grafik uchun tuzilma:</strong>
  <ol style="margin:8px 0 0;">
    <li><strong>Kirish:</strong> kim, kimni, nima haqida so'radi.</li>
    <li><strong>1-grafik:</strong> eng kattadan kichikkacha bayon qiling.</li>
    <li><strong>2-grafik:</strong> <em>반면 / 이에 비해</em> bilan solishtiring yoki sabab/o'zgarishni ayting.</li>
    <li><strong>Yakun:</strong> umumiy xulosa yoki kelajak (전망).</li>
  </ol>
</div>
"""

_CLOSING = """
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> ikkita grafik bo'lsa, ikkalasini ham <strong>albatta</strong> yozing —
  faqat bittasini yozsangiz ball to'liq bo'lmaydi. Solishtirishda <em>반면(에)</em> juda foydali.
</div>
"""

_blocks = [{"rich_text": _INTRO}]
_blocks.append({"rich_text": "<h3>1) 표현 — Solishtirish va pie uchun iboralar</h3>"})
for _t in _D["templates"]:
    _blocks.append({"rich_text": _template_card(_t)})
_blocks.append({"rich_text": "<h3>2) 연습 — Amaliy namunalar (pie · kombinatsiya)</h3>"})
for _i, _q in enumerate(_D["questions"], start=1):
    _blocks.append({"rich_text": _question_block(_i, _q)})
_blocks.append({"rich_text": _CLOSING})

LESSONS = [
    {
        "skill":   "writing",
        "title":   "TOPIK Writing 53: Ilg'or grafiklar (pie · kombinatsiya)",
        "summary": "쓰기 53 — doiraviy (pie) diagramma va ko'p grafikli (kombinatsiya) savollar: "
                   "solishtirish iboralari va imtihon uslubidagi namunalar.",
        "order":   21,   # 53-asosiy (20) dan keyin
        "blocks":  _blocks,
    },
]
