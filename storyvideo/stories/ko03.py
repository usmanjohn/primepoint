# -*- coding: utf-8 -*-
"""KO-3 — «Oʻzbek va koreys: bir xil tartib»  KOREYA OLAMI

Manba: _stories_koreya_olami_01_13.py, order 2.

The film that only an Uzbek-language channel can make. Every English-language
Korean course spends a lesson explaining that Korean puts the verb last and
marks the object after the noun — because for an English speaker both are
strange. For an Uzbek speaker neither is: `kitob-NI oʻqiyman` is `책-을 읽어요`
word for word. The pupil already owns the grammar and does not know it.

The argument is made by the `order` scene and not by the narration: three
sentences on a fixed three-column grid, the words coloured by role. Uzbek and
Korean line up; English does not. Nothing has to be claimed.
"""

from spec import Video, Scene
from scenes import word, echo, order, pairs, rule, ask, practice, outro

VIDEO = Video(
    slug="ko03",
    lesson="Koreya olami",
    title="Oʻzbek va koreys: bir xil tartib",
    story="Koreya olami — order 2",
    scenes=[
        word("책을 읽어요", gloss="«kitobni oʻqiyman»", head="Koreyscha gap",
             size=130, dur=6.6,
             note="Uch soʻz. Oxirgisi — feʼl."),

        order([("Oʻzbekcha", [("Men", "s"), ("kitobni", "o"),
                              ("oʻqiyman", "v")], False),
               ("Koreyscha", [("저는", "s"), ("책을", "o"),
                              ("읽어요", "v")], True),
               ("Inglizcha", [("I", "s"), ("read", "v"),
                              ("a book", "o")], False)],
              head="Bir gap, uch til",
              verdict="Ikkitasi bir xil. Uchinchisi — boshqacha.",
              dur=12.0,
              note="Ustunlarga qarang: rang tartibi oʻzbekcha va koreyschada "
                   "bir xil, inglizchada almashib ketgan."),

        # No "=" here: pair_rows() draws the separator itself.
        pairs([("을 / 를", "oʻzbekcha -ni"),
               ("에",      "oʻzbekcha -ga"),
               ("의",      "oʻzbekcha -ning")],
              head="Qoʻshimchalar ham juft-juft",
              tail="Ikkalasida ham soʻzdan KEYIN qoʻyiladi",
              dur=10.0,
              note="Ingliz tilida esa soʻzdan oldin: to school."),

        echo("책을 읽어요", gloss="kitobni oʻqiyman", size=120,
             note="JIM sahna. Koreyscha ovoz gapni ikki marta aytadi."),

        word("학교에 가요", gloss="«maktabga boraman»",
             head="Endi oʻzingiz oʻqing", size=130, dur=7.2,
             note="Tartibni oʻzgartirish shart emas — soʻzlarni "
                  "oʻrniga qoʻyish kifoya."),

        rule("Koreyschaga ingliz tilidan emas, oʻzbek tilidan tarjima qiling",
             strip="Men kitobni oʻqiyman  →  저는 책을 읽어요",
             meaning="Ikkala tilda ham feʼl oxirida turadi va qoʻshimcha "
                     "soʻzdan keyin qoʻyiladi. Bu afzallikni inglizcha "
                     "darslik sizga bermaydi.",
             dur=9.6),

        ask("Ingliz tilida feʼl oʻrtada turadi. Koreyschani ingliz tili "
            "orqali oʻrganayotgan odam qanday xatoga yoʻl qoʻyadi?",
            dur=7.4, note="Javobni aytmang."),

        practice("Prime Korean · PK-17",
                 sub="을/를 va 의 — toʻldiruvchi va egalik", dur=5.2),

        outro(line2="koreys tili"),
    ],
)

# ── Ovoz uchun matn (TTS) ──
from spec import narrate

narrate(VIDEO, [
    "Bu koreyscha gapni oʻqing: *책을 읽어요*. || Maʼnosi: kitobni oʻqiyman.",

    "Endi diqqat qiling. Oʻzbekchada: men kitobni oʻqiyman. | Koreyschada "
    "xuddi shu tartib — feʼl oxirida. || Inglizchada esa feʼl oʻrtaga "
    "tushib qoladi.",

    "Qoʻshimchalar ham juft-juft mos keladi. | Oʻzbekcha -ni, -ga, -ning "
    "uchun koreyschada ham aynan shunday qoʻshimchalar bor. || Va ikkala "
    "tilda ham ular soʻzdan keyin qoʻyiladi. Inglizchada — oldin.",

    None,   # echo — jim sahna, koreyscha ovoz

    "Yana bittasi: *학교에 가요*. || Maktabga boraman. | Tartibni "
    "oʻzgartirmadingiz — faqat soʻzlarni oʻrniga qoʻydingiz.",

    "Shuning uchun koreyscha gapni ingliz tilidan emas, oʻzbek tilidan "
    "tarjima qiling. || Inglizzabon oʻquvchi buni bir yil oʻrganadi. "
    "Siz esa allaqachon bilasiz.",

    "Endi oʻzingiz oʻylang. Ingliz tilida feʼl oʻrtada turadi. || Koreyschani "
    "ingliz tili orqali oʻrganayotgan odam qanday xatoga yoʻl qoʻyadi? "
    "Izohda kutamiz.",

    "Toʻldiruvchi va egalik qoʻshimchalari Powertyda: Prime Korean, "
    "17-dars.",

    None,   # outro — jim
])
