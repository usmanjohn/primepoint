# TOPIK II Yozish (쓰기) 54 — mavzu jumlalari (yodlash uchun). Manba: material_54.txt.
# Har mavzu uchun 3–4 tayyor koreyscha jumla + o'zbekcha tarjimasi. 5 mavzudan bir "qism".
# Tarjimalar TRANSLATIONS da (qo'lda). Faqat tarjima qilingan mavzular chiqadi.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_writing_54_topics.py --author=prime
# (yangi mavzular tarjima qilingach --republish bilan qayta import qiling).

import os
import re
import html

_DIR = os.path.dirname(os.path.abspath(__file__))


def _parse_topics(path):
    topics, cur = [], None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            m = re.match(r"^(\d+)[.\t]\s*(.*)$", line)
            if m:
                if cur is not None:
                    cur["sents"].append(m.group(2).strip())
            else:
                cur = {"title": line, "sents": []}
                topics.append(cur)
    return topics


_TOPICS = _parse_topics(os.path.join(_DIR, "material_54.txt"))

TRACK = {
    "name":    "TOPIK",
    "summary": "TOPIK II Koreys tili imtihoniga bosqichma-bosqich tayyorgarlik — "
               "O'qish, Yozish va Tinglash bo'yicha strategiya va amaliyot.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
    "order":   1,
}

# Koreyscha sarlavha -> {"uz": mavzu nomi, "s": [har bir jumla tarjimasi]}
TRANSLATIONS = {
    "스마트폰 중독": {
        "uz": "Smartfonga qaramlik",
        "s": [
            "Smartfon bo'lsa bas, istalgan vaqt va joyda telefon, internet va o'yindan foydalanish mumkin.",
            "Smartfon bilan ovora bo'lib, boshqa ishlarga yaxshi diqqat qila olmay qolamiz.",
            "Kerakli ma'lumotni ham smartfon qidiruviga tayanib qolganimiz sababli, xotira zaiflashmasligi mumkin emas.",
        ],
    },
    "글쓰기 능력": {
        "uz": "Yozish qobiliyati",
        "s": [
            "Do'stga xabar yuborish, rasmiy elektron xat yozish kabi biz turli shakldagi matnlar yozamiz,",
            "Yozish qobiliyatini oshirish uchun avvalo kitob o'qish odatini shakllantirish kerak.",
            "Ko'p yozgandagina malaka oshgani uchun, har kuni kundalik yuritish yoki shaxsiy blogga muntazam yozib borish ham yaxshi usul bo'lishi mumkin.",
        ],
    },
    "부탁 거절": {
        "uz": "Iltimosni rad etish",
        "s": [
            "Iltimosni rad etib, yaxshi bo'lgan munosabatlar buzilib ketadigan holatlar ham bo'ladi.",
            "Rad etayotganda, suhbatdoshning qiyin ahvoliga to'liq hamdard ekaningiz va uni tushunayotganingizni ko'rsatish kerak.",
            "Muammoni hal qilish uchun birga bosh qotirganingizni ko'rsata olganingiz sababli, suhbatdoshning ham ko'ngli kamroq og'riydi.",
        ],
    },
    "과소비의 문제점": {
        "uz": "Isrofgarchilikning muammolari",
        "s": [
            "To'satdan baxtsiz hodisaga uchrab yoki kasal bo'lib shifoxona xarajati chiqsa, qarzga botishdan boshqa iloj qolmaydi.",
            "Ko'ngli notinch yoki tushkun bo'lgani uchun beixtiyor isrof qiladiganlar ham, o'zini ko'rsatish yoki e'tibor tortish uchun isrof qiladiganlar ham bor.",
            "Isrofga olib keladigan sabablardan biri sifatida reklamaning ta'sirini keltirish mumkin.",
            "Inson o'zi nega isrof qilayotganining sababini aniq bilgandagina, xarajatni jilovlash yo'lini ham topa oladi.",
        ],
    },
    "바른말 & 의사소통": {
        "uz": "To'g'ri nutq va muloqot",
        "s": [
            "Qanday gapirishga qarab, o'sha odam haqidagi taassurot o'zgarishi mumkin.",
            "Ijtimoiy tarmoqda oson va qulay muloqotga o'rganib, qisqartma so'zlarni tez-tez ishlatgani uchun, qaysi biri to'g'ri so'z ekanini yaxshi bilmaydiganlar ko'paydi.",
            "Rasmiy joylarda moda so'zlar yoki qisqartmalardan qochgan ma'qul.",
        ],
    },
    "시간 관리": {
        "uz": "Vaqtni boshqarish",
        "s": [
            "Tobora tezlashayotgan o'zgarishlar va keskin raqobat ichida, vaqtdan qanday foydalanish inson hayotidagi muvaffaqiyat va muvaffaqiyatsizlikka katta ta'sir qilmoqda.",
            "Vaqtni yaxshi boshqara olmasangiz, keyin afsuslanadigan ishlar ko'payadi.",
            "Vaqtni samarali boshqarish uchun ishlarning ustuvorligini belgilash kerak.",
            "Ishga borib-kelishda yoki birovni kutganda kabi kundalik hayotda ozdan hosil bo'ladigan qisqa vaqtni behuda ketkazmay, o'sha vaqtda bajarsa bo'ladigan ishlarni tayyorlab qilgan yaxshi.",
        ],
    },
    "긍정적은 생각": {
        "uz": "Ijobiy fikrlash",
        "s": [
            "Aslida qiyin vaziyatga tushganda, odam o'zini va sharoitni ayblab, salbiy fikrga berilib ketishi oson.",
            "Ijobiy fikrlasangiz, muvaffaqiyatsiz tajribadan ham o'rganadigan narsa topa olasiz.",
            "Ijobiy fikrlash ruhiy va jismoniy sog'liqqa ham yaxshi ta'sir qiladi.",
            "Katta maqsaddan ko'ra kichik maqsadlarni birma-bir amalga oshirib borsangiz, yutuq hissi ham paydo bo'ladi, o'ziga ishonch ham ortadi.",
        ],
    },
    "좋은 습관": {
        "uz": "Yaxshi odatlar",
        "s": [
            "Yaxshi odat hayotimizga ijobiy ta'sir qiladi.",
            "Odatda odamlar yaxshi odat sifatida erta yotib erta turishni, muntazam sport bilan shug'ullanishni sanashadi.",
            "Avvalo o'z odatlaring orasidan yaxshi va yomon odatni ajratib tahlil qilish kerak.",
            "Yaxshi xatti-harakatni takrorlasang, yaxshi natijaga erishasan.",
        ],
    },
    "갈등": {
        "uz": "Ziddiyat (nizo)",
        "s": [
            "Odamlar iloji boricha ziddiyatdan qochishni istaydi.",
            "Faqat o'z fikrini o'tkazib, suhbatdoshni ayblash yoki umuman gaplashmaslik kabi munosabat ziddiyatni hal qilishga aslo yordam bermaydi.",
            "Suhbatdoshga e'tiborli bo'lib, o'z pozitsiyasidan yon bermaslik mumkin emas.",
        ],
    },
    "감시카메라 설치": {
        "uz": "Kuzatuv kamerasini o'rnatish",
        "s": [
            "Kuzatuv kamerasini o'rnatishdan maqsad jinoyatning oldini olishdir.",
            "Kuzatuv kamerasining muammolaridan biri — shaxsiy hayotga tajovuz qilinishi mumkinligidir.",
            "Bolalar, keksalar, ayollar kabi himoyaga muhtojlarga qarshi jinoyat ortayotgan bir paytda, kuzatuv kamerasi ularning xavotirini kamaytira olishi kabi afzalligi bor.",
        ],
    },
}

PER_PART = 5
_BADGE = ('<span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;'
          'font-size:0.85em;">쓰기 54</span>')


def _topic_card(topic):
    tr = TRANSLATIONS[topic["title"]]
    ko_title = html.escape(topic["title"])
    uz_title = html.escape(tr["uz"])
    items = ""
    for ko, uz in zip(topic["sents"], tr["s"]):
        items += (f'<li style="margin-bottom:8px;"><strong>{html.escape(ko)}</strong><br>'
                  f'<span style="color:#475569;"><em>{html.escape(uz)}</em></span></li>')
    return f"""
<div style="background:#ffffff;border-left:4px solid #a855f7;box-shadow:0 1px 2px rgba(0,0,0,.06);padding:12px 16px;border-radius:8px;margin:16px 0;">
  <p style="margin:0 0 8px;"><strong style="font-size:1.08em;">📌 {ko_title}</strong>
     &nbsp;—&nbsp;<span style="color:#7c3aed;">{uz_title}</span></p>
  <ol style="margin:0;line-height:1.6;">{items}</ol>
</div>
"""


def _intro(part_no, first, last):
    if part_no == 1:
        return f"""
<h2>TOPIK Writing 54: Mavzu jumlalari ({part_no}-qism)</h2>
<p>{_BADGE} &nbsp;<span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">yodlash uchun</span></p>
<p>쓰기 54 inshosi uchun <strong>maxsus mavzular bo'yicha tayyor jumlalar</strong>. Har
mavzuda 3–4 ta jumla — koreyschasini yodlang, o'zbekcha tarjimasi tushunish uchun.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Qanday yodlash:</strong> har jumlani <strong>kuniga 3 marta, 3 kun</strong>
  yozing (kuniga 3 ta jumla). Metod haqida <em>“Jumla yodlash metodi”</em> darsiga qarang.
</div>
"""
    return f"""
<h2>TOPIK Writing 54: Mavzu jumlalari ({part_no}-qism)</h2>
<p>Yana bir necha mavzu bo'yicha tayyor jumlalar — koreyschasini yodlang.</p>
"""


_CLOSING = """
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> hamma mavzuni emas — imtihonda chiqishi mumkin bo'lgan bir
  nechta mavzuni tanlab, ularning jumlalarini mukammal yodlang. (전략 darsiga qarang.)
</div>
"""

# Faqat tarjima qilingan mavzular, fayldagi tartibda.
_ready = [t for t in _TOPICS if t["title"] in TRANSLATIONS]

LESSONS = []
for _pi, _start in enumerate(range(0, len(_ready), PER_PART), start=1):
    _chunk = _ready[_start:_start + PER_PART]
    _blocks = [{"rich_text": _intro(_pi, _start + 1, _start + len(_chunk))}]
    for _t in _chunk:
        _blocks.append({"rich_text": _topic_card(_t)})
    _blocks.append({"rich_text": _CLOSING})
    LESSONS.append({
        "skill":   "writing",
        "title":   f"TOPIK Writing 54: Mavzu jumlalari ({_pi}-qism)",
        "summary": f"쓰기 54 — {_start + 1}–{_start + len(_chunk)}-mavzular bo'yicha yodlash "
                   f"uchun tayyor jumlalar (koreyscha + o'zbekcha).",
        "order":   30 + _pi,   # 31, 32, ... (Q54 diapazoni)
        "blocks":  _blocks,
    })
