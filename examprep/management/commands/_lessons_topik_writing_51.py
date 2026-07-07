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
  Javobni yoddan aytmang — <mark>uning template'ini</mark> tushuning.
</div>
"""
    return f"""
<h2>TOPIK Writing 51: Amaliy namunalar ({part_no}-qism)</h2>
<p>Har bir xatda bo'sh joylarni (㉠, ㉡) o'zingiz to'ldirib, so'ng namunaviy javoblar bilan
solishtiring.</p>
"""


# 1-qismda ko'rsatiladigan ishlangan misol (qadam-baqadam).
_WORKED = """
<h3>Ishlangan misol — qadam-baqadam 🔍</h3>
<p>Namunalarga o'tishdan oldin bitta xatni birga yechamiz. Har qadamni ochib boring:</p>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — xatni o'qing:</strong> kim, kimga, nima uchun yozyapti?</p>
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;line-height:1.9;">
      제목: 스터디 모임<br>
      민수 씨, 안녕하세요.<br>
      다음 주에 시험이 있어서 같이 <mark style="background:#fde68a;">( ㉠ )</mark>.<br>
      저는 금요일에는 시간이 없는데 혹시 토요일에는 <mark style="background:#fde68a;">( ㉡ )</mark>?<br>
      답장 기다리겠습니다.
    </div>
    <p style="color:#475569;margin:8px 0 0;"><em>Do'stiga yozilgan xabar: keyingi hafta imtihon bor,
    birga o'qishni taklif qilmoqchi va vaqt so'ramoqchi.</em></p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — ㉠ ni toping.</strong> Oldida <mark style="background:#dbeafe;">같이</mark>
    (birga) turibdi va sabab aytilgan (시험이 있어서) — demak bu <strong>taklif</strong>:</p>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0 0;">
      <p style="margin:0 0 4px;"><strong>공부하면 좋겠어요 / 공부했으면 해요</strong></p>
      <p style="color:#475569;margin:0;"><em>birga o'qisak yaxshi bo'lardi (taklif shakli)</em></p>
    </div>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — ㉡ ni toping.</strong> Jumla <mark style="background:#dbeafe;">혹시</mark>
    bilan boshlanib <strong>?</strong> bilan tugaydi — demak bu muloyim <strong>savol</strong>:</p>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0 0;">
      <p style="margin:0 0 4px;"><strong>시간이 있어요? / 만날 수 있어요?</strong></p>
      <p style="color:#475569;margin:0;"><em>vaqtingiz bormi? / uchrasha olamizmi?</em></p>
    </div>
  </div>
  <div class="pp-step">
    <p><strong>Xulosa qadam</strong> — yechish tartibi doim bir xil:</p>
    <div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:8px 0 0;">
      <ol style="margin:0;">
        <li>Xatning <strong>maqsadini</strong> aniqlang (taklif? iltimos? uzr?).</li>
        <li>Bo'sh joy <strong>atrofidagi so'zlarga</strong> qarang (같이, 혹시, -아/어서, ?).</li>
        <li>Maqsadga mos <strong>template</strong>ni qo'ying (Templates darsiga qarang).</li>
      </ol>
    </div>
  </div>
</div>
"""

# 1-qism yakunida: xat iboralari — flashcards.
_FLASH = """
<h3>Xat iboralari — tezkor takror 🔁</h3>
<p class="text-secondary small">51-savolda eng ko'p ishlatiladigan iboralar. Kartani bosib ag'daring.</p>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">부탁드립니다</div><div class="pp-card-back">iltimos qilaman (rasmiy)</div></div>
  <div class="pp-card"><div class="pp-card-front">연락 주시기 바랍니다</div><div class="pp-card-back">bog'lanishingizni so'rayman</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)면 좋겠습니다</div><div class="pp-card-back">... bo'lsa yaxshi bo'lardi</div></div>
  <div class="pp-card"><div class="pp-card-front">-아/어 주시겠습니까?</div><div class="pp-card-back">... qilib bera olasizmi? (muloyim)</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)려고 합니다</div><div class="pp-card-back">...moqchiman (reja)</div></div>
  <div class="pp-card"><div class="pp-card-front">죄송하지만</div><div class="pp-card-back">kechirasiz-u, ... (muloyim boshlanish)</div></div>
  <div class="pp-card"><div class="pp-card-front">-기 바랍니다</div><div class="pp-card-back">...ishingizni so'rayman (e'lon uslubi)</div></div>
  <div class="pp-card"><div class="pp-card-front">혹시</div><div class="pp-card-back">balki / mabodo (savolni yumshatadi)</div></div>
</div>
"""

_CLOSING = """
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> yoqqan jumlalarni daftaringizga yozib qo'ying va
  <strong>bitta ishonchli template'ni</strong> mukammal egallang — ko'p emas, bittasini.
  (전략 darsiga qarang.)
</div>
"""


LESSONS = []
for _pi, _start in enumerate(range(0, len(_ITEMS), PER_PART), start=1):
    _chunk = _ITEMS[_start:_start + PER_PART]
    _blocks = [{"rich_text": _intro_block(_pi)}]
    if _pi == 1:
        _blocks.append({"rich_text": _WORKED})
    for _j, _item in enumerate(_chunk, start=_start + 1):
        _blocks.append({"rich_text": _item_block(_j, _item)})
    if _pi == 1:
        _blocks.append({"rich_text": _FLASH})
    _blocks.append({"rich_text": _CLOSING})
    LESSONS.append({
        "skill":   "writing",
        "title":   f"TOPIK Writing 51: Amaliy namunalar ({_pi}-qism)",
        "summary": f"쓰기 51 — {_start + 1}–{_start + len(_chunk)}-namunalar: xat/xabardagi "
                   f"bo'sh joylarni (㉠, ㉡) to'ldirish.",
        "order":   2 + _pi,   # 3, 4, 5, 6, 7  (patterns lesson takes order 2)
        "blocks":  _blocks,
    })
