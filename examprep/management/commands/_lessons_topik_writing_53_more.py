# TOPIK II Yozish (쓰기) 53 — QO'SHIMCHA namunalar. Manba: material_53_more.json
# Ikki lesson: (A) bitta grafik + qo'shimcha ma'lumot;  (B) ikki grafik kombinatsiyasi.
# Javob namunalari 200–300 자 (belgi soni ko'rsatiladi). Pie = CSS conic-gradient.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_writing_53_more.py --author=prime

import os
import json
import html

_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_DIR, "material_53_more.json"), encoding="utf-8") as _f:
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
        '<div style="flex:0 0 auto;">' + title
        + '<div style="display:flex;align-items:center;gap:12px;">'
        + '<div style="position:relative;width:132px;height:132px;flex-shrink:0;">'
        + f'<div style="width:132px;height:132px;border-radius:50%;background:conic-gradient({",".join(segs)});"></div>'
        + '<div style="position:absolute;top:34px;left:34px;width:64px;height:64px;border-radius:50%;background:#fff;"></div>'
        + '</div>' + f'<div>{"".join(legend)}</div></div></div>'
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
            f'<div style="width:{w:.0f}%;min-width:46px;background:#3b82f6;color:#fff;font-size:0.78em;'
            f'padding:2px 8px;border-radius:6px;white-space:nowrap;">{val}{html.escape(unit)}</div>'
            '</div></div>'
        )
    title = (f'<div style="text-align:center;font-weight:600;font-size:0.9em;margin-bottom:4px;">'
             f'{html.escape(chart.get("title",""))}</div>') if chart.get("title") else ""
    return f'<div style="flex:1 1 240px;min-width:220px;">{title}{rows}</div>'


def _chart(ch):
    return _pie(ch) if ch.get("type") == "pie" else _bar(ch)


def _given_info(info):
    if not info:
        return ""
    boxes = ""
    for grp in info:
        pts = "".join(f"<li>{html.escape(p)}</li>" for p in grp.get("points", []))
        boxes += (
            '<div style="flex:1 1 200px;background:#eff6ff;border:1px dashed #93c5fd;border-radius:8px;padding:8px 12px;">'
            f'<strong style="color:#1d4ed8;">{html.escape(grp["label"])}</strong>'
            f'<ul style="margin:4px 0 0;padding-left:18px;">{pts}</ul></div>'
        )
    return f'<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:12px;">{boxes}</div>'


def _reveal(answer):
    n = len(answer)
    return f"""
<details style="background:#ecfdf5;border:1px solid #a7f3d0;border-radius:8px;padding:10px 14px;margin:8px 0 22px;">
  <summary style="cursor:pointer;font-weight:600;color:#047857;">✅ 정답 — Namunaviy javob (bosing)</summary>
  <p style="margin:8px 0 0;line-height:1.75;">{html.escape(answer)}</p>
  <p style="margin:8px 0 0;color:#64748b;font-size:0.82em;">📏 글자 수: 약 {n}자 &nbsp;(200–300자 권장)</p>
</details>
"""


def _question_block(n, q):
    charts = "".join(_chart(ch) for ch in q["charts"])
    return f"""
<div style="margin:22px 0 6px;"><span style="background:#1e293b;color:#fff;padding:2px 10px;border-radius:6px;font-size:0.82em;">문제 {n}</span>
&nbsp;<strong>{html.escape(q['topic'])}</strong></div>
<p style="color:#64748b;font-size:0.85em;margin:0 0 8px;">{html.escape(q.get('instruction',''))}</p>
<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:8px 0;">
  <p style="margin:0 0 12px;line-height:1.7;">{html.escape(q.get('intro',''))}</p>
  <div style="display:flex;flex-wrap:wrap;gap:24px;justify-content:center;align-items:flex-start;">{charts}</div>
  {_given_info(q.get('given_info'))}
</div>
{_reveal(q.get('sample_answer',''))}
"""


def _build(items, intro_html, closing_html, extra_html=None):
    blocks = [{"rich_text": intro_html}]
    for i, q in enumerate(items, start=1):
        blocks.append({"rich_text": _question_block(i, q)})
    if extra_html:
        blocks.append({"rich_text": extra_html})
    blocks.append({"rich_text": closing_html})
    return blocks


# "Grafik + qo'shimcha ma'lumot" darsida kerak bo'ladigan iboralar — flashcards.
_A_FLASH = """
<h3>원인·대책·전망 iboralari — tezkor takror 🔁</h3>
<p class="text-secondary small">Qo'shimcha ma'lumotni matnга bog'lashda ishlatiladigan iboralar.
Kartani bosib ag'daring.</p>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">원인</div><div class="pp-card-back">sabab</div></div>
  <div class="pp-card"><div class="pp-card-front">대책</div><div class="pp-card-back">chora, yechim</div></div>
  <div class="pp-card"><div class="pp-card-front">전망</div><div class="pp-card-back">istiqbol, prognoz</div></div>
  <div class="pp-card"><div class="pp-card-front">~(으)로 인해</div><div class="pp-card-back">... tufayli, ... sababli</div></div>
  <div class="pp-card"><div class="pp-card-front">~ㄹ 것으로 보인다</div><div class="pp-card-back">... deb ko'rinadi (taxmin)</div></div>
  <div class="pp-card"><div class="pp-card-front">해결 방안</div><div class="pp-card-back">yechim yo'li</div></div>
  <div class="pp-card"><div class="pp-card-front">늘어나다</div><div class="pp-card-back">ko'paymoq, o'smoq</div></div>
  <div class="pp-card"><div class="pp-card-front">줄어들다</div><div class="pp-card-back">kamaymoq, qisqarmoq</div></div>
</div>
"""


_A_INTRO = """
<h2>TOPIK Writing 53: Bitta grafik + qo'shimcha ma'lumot</h2>
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">쓰기 53</span>
&nbsp;<span style="background:#10b981;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">grafik + 자료</span>
&nbsp;<span style="background:#f59e0b;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">200–300자</span></p>
<p>Ko'p 53 savolida bitta grafik bilan birga <mark>qo'shimcha ma'lumot</mark> (원인, 전망, 대책...)
matn ko'rinishida beriladi. Vazifa — grafikni <strong>ham</strong>, berilgan ma'lumotni <strong>ham</strong>
bitta izchil matnga birlashtirib yozish.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Tuzilma:</strong> ① kirish (kim/nima) → ② grafik (raqamlar) → ③ berilgan ma'lumot
  (원인/전망/대책) → ④ yakun. Hammasi <strong>200–300 자</strong> ichida.
</div>
"""

_A_CLOSING = """
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> berilgan ma'lumotdagi (ko'k qutilar) barcha bandlarni matnга kiriting —
  ular ball uchun zarur. Belgilar sonini 200–300 oralig'ida ushlang.
</div>
"""

_B_INTRO = """
<h2>TOPIK Writing 53: Ko'proq kombinatsiya namunalari</h2>
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">쓰기 53</span>
&nbsp;<span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">2 grafik</span>
&nbsp;<span style="background:#f59e0b;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">200–300자</span></p>
<p>Ikkita grafik (ikki pie, yoki ustun + pie) berilganda <strong>ikkalasini ham</strong> bayon qiling.
Solishtirishda <em>반면(에)</em>, o'zgarishda <em>증가/감소하였다</em>, yakunda <em>전망</em> ishlating.</p>
"""

_B_CLOSING = """
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> ikkita grafikni bir jumlaga tiqmang — har biriga alohida jumla ajrating,
  keyin <em>반면</em> yoki <em>이를 통해</em> bilan bog'lang.
</div>
"""

LESSONS = [
    {
        "skill":   "writing",
        "title":   "TOPIK Writing 53: Bitta grafik + qo'shimcha ma'lumot",
        "summary": "쓰기 53 — bitta grafik va matnli qo'shimcha ma'lumotni (원인/전망) birlashtirib "
                   "200–300 자 yozish; belgi soni ko'rsatilgan namunalar.",
        "order":   22,
        "blocks":  _build(_D["single"], _A_INTRO, _A_CLOSING, extra_html=_A_FLASH),
    },
    {
        "skill":   "writing",
        "title":   "TOPIK Writing 53: Ko'proq kombinatsiya namunalari",
        "summary": "쓰기 53 — ikki grafikli (pie/ustun kombinatsiyasi) qo'shimcha imtihon namunalari, "
                   "200–300 자 javoblar bilan.",
        "order":   23,
        "blocks":  _build(_D["combo"], _B_INTRO, _B_CLOSING),
    },
]
