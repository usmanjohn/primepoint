# -*- coding: utf-8 -*-
"""KO-33 — «Orqaga qaragan gap»  ·  TUTILGAN XATO  ·  TOPIK 06

Manba: examprep → TOPIK → Oʻqish — 순서 배열 (gaplarni tartiblash).

TOPIK filmlarining oltinchisi, va xato TURI yana almashtirildi (SERIES.md):
KO-13 registr, KO-14 soat, KO-15 mexanik sirpanish, KO-22 koʻz odati,
KO-26 grafikni oʻqish. Bu — **usulning yoʻqligi**: pupil bilimsiz emas,
u shunchaki toʻrttasini oʻqib, tuygʻu bilan tanlaydi.

Usul mexanik va tekshirib boʻladigan: 그래서 · 그런데 · 그리고 · 이런/그 + ot
bilan boshlangan gap ORQAGA qaraydi, demak birinchi boʻla olmaydi. Odatda
toʻrttadan uchtasi shu bilan tushib qoladi.

⛔ Bu filmda birorta son yoʻq — na savol soni, na daqiqa. CLAUDE.md talabi:
TOPIK raqamlari faqat saytning oʻz strategiya darsidan olinadi, xotiradan
emas. Bu yerda raqam kerak emas, chunki dars — usul, statistika emas.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, pairs, echo, check,
                    rule, ask, practice, outro)

VIDEO = Video(
    slug="ko33",
    lesson="TOPIK 읽기",
    title="Orqaga qaragan gap",
    story="examprep TOPIK — 순서 배열",
    subject="korean",
    scenes=[
        cover("그래서…", "Bu birinchi boʻlolmaydi",
              kicker="Tutilgan xato", ko="한국어",
              track="TOPIK", n=6, badge="big",
              context="순서 배열 — toʻrt gapni tartiblash:",
              strike=False,
              note="MUQOVA: gʻalati narsa — gapni oʻqimasdan turib "
                   "birinchi emasligini aytish. Vaʼda uch soʻz."),

        says("Anvar aka", [("순서 배열 savolida:", "lbl"),
                           ("Toʻrttasini oʻqib, tuygʻu bilan tanlayman.", "expr")],
             mood="smile", dur=6.2,
             note="Xato bilimda emas — usulning yoʻqligida."),

        consequence("Anvar aka",
                    "Vaqt ketdi, javob esa taxmin boʻlib qoldi.",
                    mood="sad", close=True, dur=7.2,
                    note="Yaqin plan. Zarar — bilmaslik emas, tartibsiz "
                         "oʻqish."),

        pairs([("그래서 …", "oldin SABAB aytilgan boʻlishi kerak"),
               ("그런데 …", "oldin boshqa fikr aytilgan boʻlishi kerak"),
               ("이런 · 그 + ot", "oldin oʻsha narsa aytilgan boʻlishi kerak")],
              head="Bu soʻzlar orqaga qaraydi",
              tail="Orqaga qaragan gap birinchi boʻla olmaydi.",
              dur=13.5,
              note="Filmning usuli. Uchala qatorda ham sabab bitta: "
                   "bu soʻzlar oʻzidan OLDIN matn borligini talab qiladi."),

        echo("그래서", gloss="shuning uchun",
             note="JIM sahna. Eshitib tanib olish — 듣기 da ham asqotadi."),

        check("Birinchi gapni topamiz",
              parts=["(가) 그래서 — orqaga qaraydi, tushdi",
                     "(나) 그런데 — orqaga qaraydi, tushdi",
                     "(다) 이런 사람은 — orqaga qaraydi, tushdi",
                     "(라) hech narsaga tayanmaydi — birinchi"],
              verdict="Toʻrttadan bittasi qoldi.",
              title="Usulni qoʻllaymiz",
              dur=11.5,
              note="Toʻrt qatorning uchtasi mexanik tushadi. Pupil "
                   "gaplarning MAZMUNINI hali oʻqigani ham yoʻq."),

        echo("그런데", gloss="lekin, ammo",
             note="JIM sahna, ikkinchisi."),

        rule("Oldin boshlanishni toping, keyin oʻqing",
             strip="그래서 · 그런데 · 그리고 · 이런 → birinchi emas",
             meaning="Bu soʻzlar oʻzidan oldin matn borligini talab qiladi. "
                     "Shuning uchun ular bilan boshlangan gap hech qachon "
                     "birinchi boʻlmaydi. Avval shularni chizib tashlang — "
                     "koʻpincha bitta nomzod qoladi va butun savol shu "
                     "yerda hal boʻladi.",
             dur=11.5),

        ask("Gap 하지만 bilan boshlansa-chi? "
            "| U ham orqaga qaraydimi, yoʻqmi?",
            dur=7.0,
            note="Javobni aytmang. 하지만 videoda umuman koʻrsatilmagan — "
                 "pupil qoidani oʻzi yangi soʻzga qoʻllashi kerak."),

        practice("TOPIK · Oʻqish",
                 sub="powerty.uz → Examprep → TOPIK → Oʻqish",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "TOPIK oʻqish boʻlimida toʻrtta gapni tartiblash savoli bor. "
    "|| Va bitta gapni oʻqimasdan turib chiqarib tashlash mumkin.",

    "Anvar aka shunday qiladi: toʻrttasini oʻqiydi va tuygʻu bilan tanlaydi.",

    "Natija — vaqt ketdi, javob esa taxmin boʻlib qoldi. "
    "|| Xato bilimda emas. Usul yoʻq.",

    "Mana usul. | 그래서 — shuning uchun. Undan oldin sabab boʻlishi kerak. "
    "| 그런데 — lekin. Undan oldin boshqa fikr boʻlishi kerak. "
    "|| 이런, yoki 그 va ot. Undan oldin oʻsha narsa aytilgan boʻlishi kerak.",

    None,   # echo(그래서)

    "Endi qoʻllaymiz. | Birinchisi 그래서 bilan boshlanadi — tushdi. "
    "| Ikkinchisi 그런데 — tushdi. | Uchinchisi 이런 사람은 — tushdi. "
    "|| Toʻrtinchisi hech narsaga tayanmaydi. Birinchi gap — oʻsha.",

    None,   # echo(그런데)

    "Bu soʻzlar oʻzidan oldin matn borligini talab qiladi. "
    "| Shuning uchun ular bilan boshlangan gap hech qachon birinchi "
    "boʻlmaydi. || Avval shularni chizib tashlang.",

    "Endi oʻzingiz oʻylang. Gap 하지만 bilan boshlansa-chi? "
    "| U ham orqaga qaraydimi? || Izohda kutamiz.",

    "TOPIK oʻqish — savol turlari boʻyicha, Powertyda, Examprep boʻlimida.",

    None,   # outro
])
