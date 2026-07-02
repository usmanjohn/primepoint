# TOPIK II Yozish (쓰기) 53 — grafik/jadvalni tasvirlash. Manba: topik_53.txt.
# Grafiklar RASM emas — survey_data (raqamlar) dan HTML bar-chart chiziladi.
# Til: O'zbekcha + Koreyscha, styling bilan.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_writing_53.py --author=prime

import os
import json
import html

_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_DIR, "topik_53.txt"), encoding="utf-8") as _f:
    _DATA = json.load(_f)

TRACK = {
    "name":    "TOPIK",
    "summary": "TOPIK II Koreys tili imtihoniga bosqichma-bosqich tayyorgarlik — "
               "O'qish, Yozish va Tinglash bo'yicha strategiya va amaliyot.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
    "order":   1,
}

# Koreyscha mavzu -> o'zbekcha
_TOPIC_UZ = {
    "공강 시간에 하는 일": "Bo'sh (oyna) vaqtda qilinadigan ishlar",
    "선호하는 주거 형태": "Afzal ko'riladigan turar-joy turi",
    "이직 시 가장 중요하게 생각하는 것": "Ish almashtirishda eng muhim narsa",
    "조기 유학의 장단점": "Erta chet elda o'qishning afzallik va kamchiliklari",
    "도시 인구 증가 원인 및 대책": "Shahar aholisi o'sishi: sabablar va choralar",
}
_TEMPLATE_UZ = {
    "introduction": "Kirish — so'rov tashkiloti va obyektini bayon qilish",
    "ranking":      "Tartib va foizni bayon qilish",
}


def _reveal(answer):
    return f"""
<details style="background:#ecfdf5;border:1px solid #a7f3d0;border-radius:8px;padding:10px 14px;margin:8px 0 20px;">
  <summary style="cursor:pointer;font-weight:600;color:#047857;">✅ Namunaviy javob (bosing)</summary>
  <p style="margin:8px 0 0;line-height:1.7;">{html.escape(answer)}</p>
</details>
"""


def _bar_chart(rows):
    out = '<div style="margin:10px 0;">'
    for r in sorted(rows, key=lambda x: x.get("rank", 999)):
        item = html.escape(str(r["item"]))
        val = r["value"]
        out += (
            '<div style="display:flex;align-items:center;gap:8px;margin:5px 0;">'
            f'<div style="width:150px;font-size:0.88em;text-align:right;color:#334155;">{item}</div>'
            '<div style="flex:1;background:#eef2f7;border-radius:6px;">'
            f'<div style="width:{val}%;min-width:36px;background:#3b82f6;color:#fff;'
            f'font-size:0.8em;padding:2px 8px;border-radius:6px;white-space:nowrap;">{val}%</div>'
            '</div></div>'
        )
    return out + "</div>"


def _two_cols(pros, cons):
    def col(title, items, bg, border):
        lis = "".join(f"<li>{html.escape(x)}</li>" for x in items)
        return (f'<div style="flex:1 1 240px;background:{bg};border-left:4px solid {border};'
                f'padding:10px 14px;border-radius:8px;"><strong>{title}</strong>'
                f'<ul style="margin:6px 0 0;">{lis}</ul></div>')
    return ('<div style="display:flex;flex-wrap:wrap;gap:10px;margin:10px 0;">'
            + col("장점 (Afzallik)", pros, "#ecfdf5", "#10b981")
            + col("단점 (Kamchilik)", cons, "#fffbeb", "#f59e0b")
            + "</div>")


def _trend(d):
    parts = "".join(f"<li>{html.escape(v)}</li>" for v in d.get("trend_data", {}).values())
    out = f'<ul style="margin:6px 0;">{parts}</ul>'
    if d.get("causes"):
        out += ("<p style='margin:8px 0 2px;'><strong>원인 (Sabablar):</strong></p><ul style='margin:0;'>"
                + "".join(f"<li>{html.escape(x)}</li>" for x in d["causes"]) + "</ul>")
    if d.get("solutions"):
        out += ("<p style='margin:8px 0 2px;'><strong>대책 (Choralar):</strong></p><ul style='margin:0;'>"
                + "".join(f"<li>{html.escape(x)}</li>" for x in d["solutions"]) + "</ul>")
    return out


def _question_block(n, d):
    topic = html.escape(d.get("topic", ""))
    uz = html.escape(_TOPIC_UZ.get(d.get("topic", ""), ""))
    head = (f'<h4 style="margin:18px 0 4px;">{n}. {topic}'
            + (f' <span style="color:#7c3aed;font-weight:normal;font-size:0.85em;">— {uz}</span>' if uz else "")
            + "</h4>")
    meta = ""
    if d.get("source_institution") or d.get("target_respondents"):
        meta = (f'<p style="color:#64748b;font-size:0.85em;margin:0 0 6px;">'
                f'{html.escape(d.get("source_institution",""))} · '
                f'{html.escape(d.get("target_respondents",""))}</p>')
    if "survey_data" in d:
        body = _bar_chart(d["survey_data"])
    elif d.get("type") == "pros_cons":
        body = _two_cols(d.get("pros", []), d.get("cons", []))
    else:
        body = _trend(d)
    card = (f'<div style="background:#f8fafc;border-radius:10px;padding:12px 16px;margin:8px 0;">'
            f'{meta}{body}</div>')
    return head + card + _reveal(d.get("sample_answer", ""))


def _template_card(d):
    title = html.escape(d.get("title", ""))
    uz = html.escape(_TEMPLATE_UZ.get(d.get("type", ""), ""))
    lis = "".join(f'<li><strong>{html.escape(p)}</strong></li>' for p in d.get("patterns", []))
    return f"""
<div style="background:#ffffff;border-left:4px solid #a855f7;box-shadow:0 1px 2px rgba(0,0,0,.06);padding:12px 16px;border-radius:8px;margin:14px 0;">
  <p style="margin:0 0 6px;"><strong style="font-size:1.05em;">{title}</strong>
     &nbsp;—&nbsp;<span style="color:#7c3aed;">{uz}</span></p>
  <ul style="margin:0;line-height:1.7;">{lis}</ul>
</div>
"""


_templates = [d for d in _DATA if d.get("category") == "template"]
_questions = [d for d in _DATA if d.get("category") == "question_set"]

_INTRO = """
<h2>TOPIK Writing 53: Grafik va jadvalni tasvirlash</h2>
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">쓰기 53</span>
&nbsp;<span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">grafik · 200–300 belgi</span></p>
<p>쓰기 53 — sizga <strong>grafik yoki jadval</strong> beriladi va uni so'z bilan tasvirlaysiz.
Rasmni chizmaysiz — <mark>tayyor template'lar</mark> bilan ma'lumotni bayon qilasiz.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Yondashuv (3 qadam):</strong>
  <ol style="margin:8px 0 0;">
    <li><strong>Kirish:</strong> kim, kimni, nima haqida so'rading — bir jumla.</li>
    <li><strong>Ma'lumot:</strong> tartib/foiz yoki o'zgarish (trend) ni bayon qiling.</li>
    <li><strong>Yakun:</strong> kerak bo'lsa sabab/chora yoki afzallik/kamchilik.</li>
  </ol>
</div>
"""

_CLOSING = """
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> quyidagi template'lardan <strong>bittadan</strong> tanlab yodlang,
  keyin har qanday grafikка moslang. Avval o'zingiz yozib, keyin namunaviy javob bilan solishtiring.
</div>
"""

_blocks = [{"rich_text": _INTRO}]
_blocks.append({"rich_text": "<h3>1) 문형 — Tasvirlash template'lari</h3>"})
for _t in _templates:
    _blocks.append({"rich_text": _template_card(_t)})
_blocks.append({"rich_text": "<h3>2) 연습 — Amaliy namunalar (grafik + javob)</h3>"})
for _i, _q in enumerate(_questions, start=1):
    _blocks.append({"rich_text": _question_block(_i, _q)})
_blocks.append({"rich_text": _CLOSING})

LESSONS = [
    {
        "skill":   "writing",
        "title":   "TOPIK Writing 53: Grafik va jadvalni tasvirlash",
        "summary": "쓰기 53 — grafik/jadvalni so'z bilan tasvirlash: tayyor template'lar va "
                   "ma'lumotdan chizilgan grafiklar bilan amaliy namunalar.",
        "order":   20,   # Q53 diapazoni
        "blocks":  _blocks,
    },
]
