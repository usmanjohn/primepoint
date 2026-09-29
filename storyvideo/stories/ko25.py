# -*- coding: utf-8 -*-
"""KO-25 — «Onangizning ichini qayerdan bilasiz?»  ·  TUTILGAN XATO

Manba: Prime Korean PK-28 (동사 + 고 싶다 — xohish bildirish).

An Uzbek-collision film, the shape of ko05 and ko07: Uzbek has ONE form where
Korean has two. «Bormoqchi» works for me, for you and for my mother; 가고 싶다
works for me alone. For anybody else the language demands 가고 싶어하다, and
the reason is not politeness -- it is evidentiality. Korean will not let you
state another person's inner state as a plain fact, because you cannot see
inside them. You can only report what shows.

That makes it the rare grammar point with a genuinely interesting WHY, and
the `consequence` beat says it in six words: «onangizning ichini qayerdan
bilasiz?» A pupil who hears that once does not need the rule explained twice.

The same fork runs through 좋다/좋아하다, 아프다/아파하다, 무섭다/무서워하다,
which is why the `pairs` table is four rows and not one: it is not a rule
about 고 싶다, it is a rule about feelings.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, correct, versus, pairs, echo,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:84px">%s</span>'

VIDEO = Video(
    slug="ko25",
    lesson="PK-28",
    title="Onangizning ichini qayerdan bilasiz?",
    story="Prime Korean PK-28",
    subject="korean",
    scenes=[
        cover('가고 <span class="strike">싶어요</span>', "Faqat oʻzingiz haqingizda",
              kicker="Tutilgan xato",
              ko="한국어",
              context="«Onam Koreyaga bormoqchi» deb aytmoqchimisiz?",
              strike=False,
              note="MUQOVA: chiziq faqat qoʻshimchadan oʻtadi — feʼl "
                   "toʻgʻri, shakli notoʻgʻri. Vaʼda qoidani emas, "
                   "chegarasini aytadi."),

        says("Sardor", [("Oʻqituvchiga aytdi:", "lbl"),
                        ("어머니는 한국에 가고 싶어요", "expr ko")],
             mood="smile",
             note="Oʻzbekchadan soʻzma-soʻz oʻgirilgan gap. Har bir soʻzi "
                  "joyida, shakli esa oʻzi haqida gapirayotgan odamniki."),

        consequence("Nodira opa", "Onangizning ichini qayerdan bilasiz?",
                    mood="think", close=True,
                    note="Xatoning bahosi va qoidaning sababi bitta "
                         "jumlada. YANGI: yaqin plan."),

        correct("가고 싶어요", "가고 싶어해요",
                because="Boshqa odamning xohishi — boshqa shakl.",
                lead="어머니는 한국에 __",
                shake=True,
                note="Almashadigan narsa feʼl emas, oxiri. YANGI: xato "
                     "qimirlaydi, toʻgʻrisi tepadan tushadi."),

        versus({"name": "MEN",
                "qty": KQ % "싶어요",
                "price": K % "저는 가고 싶어요",
                "tag": "ichimdagini oʻzim bilaman"},
               {"name": "U KISHI",
                "qty": KQ % "싶어해요",
                "price": K % "어머니는 가고 싶어해요",
                "tag": "tashqaridan koʻrinib turibdi"},
               title="Kimning ichi?",
               verdict="Koreys tili ichkarini taxmin qilmaydi",
               dur=12.5,
               note="Filmning dalili. Chap ustun — bilim, oʻng ustun — "
                    "kuzatuv. Koreys grammatikasi ikkalasini ajratadi."),

        echo("가고 싶어요", gloss="bormoqchiman",
             note="JIM sahna. Oʻzim haqimdagi shakl."),

        pairs([("좋아요", "좋아해요"),
               ("아파요", "아파해요"),
               ("무서워요", "무서워해요"),
               ("먹고 싶어요", "먹고 싶어해요")],
              head="Men → u kishi",
              tail="Hammasida bir xil narsa qoʻshiladi: 하다",
              note="Toʻrtta juft. Qoida faqat 고 싶다 ga emas, umuman "
                   "his-tuygʻu bildiradigan soʻzlarga tegishli."),

        echo("먹고 싶어해요", gloss="yegisi kelyapti — u kishi", size=104,
             note="JIM sahna. Jadvalning oxirgi qatori. `size=` berilgan: "
                  ".pron__k oʻzi kichraymaydi va olti belgi ikki qatorga "
                  "tushib ketadi."),

        rule("Koreys tili boshqaning ichini toʻgʻridan aytmaydi",
             strip=K % "싶어요" + " → oʻzim   ·   " + K % "싶어해요"
                   + " → u kishi",
             meaning="Oʻzbekchada «bormoqchi» hamma uchun bir xil, shuning "
                     "uchun bu xato deyarli hammada boʻladi. Koreysda esa "
                     "oʻz xohishingiz — bilim, boshqaniki — kuzatuv, va til "
                     "ikkalasini boshqa-boshqa aytadi.",
             dur=10.5),

        ask("Oʻzingiz haqingizda «가고 싶어해요» desangiz — qanday eshitiladi?",
            dur=7.4,
            note="Javobni aytmang. Film ikkala shaklni berdi, teskari "
                 "holatni bermadi."),

        practice("Prime Korean · PK-28",
                 sub="동사 + 고 싶다 — xohish bildirish", dur=5.4,
                 note="Darsning oʻzi Powertyda, mashqlari bilan."),

        outro(line2="koreys tili · grammatika"),
    ],
)

narrate(VIDEO, [
    "Oʻzbekchada «bormoqchi» degan soʻz hamma uchun bir xil. "
    "|| Koreysda esa yoʻq.",

    "Sardor shunday dedi: *어머니는 한국에 가고 싶어요*.",

    "Oʻqituvchi soʻradi: onangizning ichini qayerdan bilasiz?",

    "Almashadigan narsa feʼl emas. | Uning oxiri. "
    "|| *가고 싶어요* emas, *가고 싶어해요*.",

    "*싶어요* — oʻzimning xohishim. || *싶어해요* — tashqaridan koʻrinib "
    "turgan xohish.",

    None,   # echo(가고 싶어요) — jim sahna, koreyscha ovoz

    "Bu faqat xohishga tegishli emas. *좋아요* — *좋아해요*. "
    "| *아파요* — *아파해요*.",

    None,   # echo(먹고 싶어해요) — jim sahna, koreyscha ovoz

    "Sababi chiroyli. | Oʻz ichingizni bilasiz, boshqaniknini esa faqat "
    "koʻrasiz. || Koreys tili shu ikkisini ajratadi.",

    "Endi oʻzingiz oʻylang. Oʻzingiz haqingizda *가고 싶어해요* desangiz, "
    "qanday eshitiladi? || Izohda kutamiz.",

    "Yigirma sakkizinchi darsning oʻzi Powertyda: Praym Korean. "
    "| Havola profilda.",

    None,   # outro — jim
])
