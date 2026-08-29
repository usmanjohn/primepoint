# -*- coding: utf-8 -*-
"""PM-91 — «Choyga qancha shakar»  (konsentratsiya)   SHAKL: TUTILGAN XATO

Manba: _stories_prime_math_91_92.py, order 91.

Bu videoning dvigateli — buvijonning bir qatorlik izohi: «Juda shirin boʻlsa,
suv qoʻsh. Shakar qoʻshma». Dilnozaning instinkti teskari, va u instinkt
tomoshabinda ham bor.

Markazda ustunlar: shakar ustuni QIMIRLAMAYDI (400 g uch marta ham oʻsha),
foiz ustuni esa tushib boradi. Buni aytib berish shart emas.
"""

from spec import Video, Scene
from scenes import hook, says, beat, correct, check, rule, ask, outro
import primitives as P

_bars, sb = P.bars(
    [(20, "boshida", ""), (16, "+500 g suv", "down"), (10, "+1500 g suv", "down")],
    # ⚠️ NO reference line in this scene. Three attempts all failed, and the
    # reason is that this scene carries two caption lines under the chart, so
    # the whole block is centred higher than PM-25's was:
    #   ref = 20 (the max)  -> the dashed LINE itself clips the PIP circle;
    #   ref = 10 or 16      -> its label lands on that bar's own value;
    # and the bars already say it — 20, 16, 10 descending is the whole story.
    at=0.6, step=1.5)

chart = Scene(
    11.0,
    _bars
    + P.line("shakar hamon 400 g — u hech qayoqqa ketmadi", "lbl lbl--sm",
             at=0.6 + sb + 0.4, anim="fade")
    + P.line("shakar oʻzgarmadi — faqat maxraj kattalashdi", "ttl grn",
             at=0.6 + sb + 1.0, anim="pop", dur=0.7),
    cam="push", name="chart",
    note="Foiz 20 dan 16 ga, keyin 10 ga tushdi. Shakar esa uch marta ham "
         "oʻsha 400 gramm.")

_ladder, ls = P.solve([
    ("400 ÷ 2000 = 0,2", "boshlangʻich — 20 foiz"),
    ("400 ÷ 2500 = 0,16", "500 g suvdan keyin"),
    ("400 ÷ 0,1 = 4000", "10 foiz uchun kerakli massa"),
], at=0.6, step=1.6)

ladder = Scene(
    9.8,
    P.counters(P.counter(3, "qadam", at=0.6, dur=ls, counts=".solve__row"))
    + _ladder,
    cam="sink", top=True, name="ladder", counts=[3],
    claims=["400 ÷ 2000 = 0,2", "400 ÷ 2500 = 0,16"],
    note="Uchinchi qator teskari tomondan yuradi: foizdan massaga.")

VIDEO = Video(
    slug="pm91",
    lesson="PM-91",
    title="Choyga qancha shakar",
    story="Prime Math Readings — order 91",
    scenes=[
        hook("400 g", "shakar", "1 600 g", "suv", "Juda shirin. Nima qilamiz?",
             dur=5.2),

        says("Buvijon", [("Juda shirin boʻlsa,", "lbl"),
                         ("suv qoʻsh", "expr gold"),
                         ("Shakar qoʻshma", "ask")],
             dur=6.8, size=270,
             note="Buvijon retseptning tagiga ellik yil oldin shu izohni yozgan."),

        beat(4.2, note="Jim turing. Nega shakar qoʻshmaslik kerak?"),

        says("Dilnoza", [("Tushunmadim.", "lbl"),
                         ("Axir shirinlikni", "expr"),
                         ("shakar belgilaydi-ku", "ask")],
             dur=6.6, size=250, mood="think",
             note="Dilnozaning instinkti teskari — va u instinkt hammada bor."),

        ladder,

        chart,

        correct("+shakar", "+suv", "400 ÷ 2500 = 0,16", lead="teskarisi", dur=8.4,
                note="Shakar qoʻshilsa ulush oshadi. Kerak boʻlgani — ulushni "
                     "tushirish."),

        check("4000 − 2500 = 1500",
              parts=["10 foiz uchun massa 4000 g boʻlishi kerak", "hozir 2500 g bor"],
              verdict="Yana 1500 g suv.", title="Mehmonlar 10 foiz soʻradi",
              dur=8.4,
              note="Dilnoza qoʻshdi va tekshirdi: 400 ÷ 4000 = 0,10 ✓"),

        rule("Suv qoʻshilsa shakar oʻzgarmaydi — faqat maxraj kattalashadi",
             strip="foiz = sof modda ÷ butun massa",
             meaning="Shuning uchun foiz tushadi. Buvijon buni ellik yil shunday qilgan.",
             dur=9.6,
             note="Dilnoza retsept tagiga oʻz izohini qoʻshdi."),

        ask("Kompotni shirinroq qilish uchun nima qilish kerak — va nega?",
            dur=7.0, note="Javobni aytmang."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Buvijonning olma kompoti: 400 g shakar va 1 600 g suv. || Kompot juda "
    "shirin chiqdi. Nima qilamiz?",

    "Retsept tagida buvijonning bir qatorlik izohi bor: *juda shirin boʻlsa, "
    "suv qoʻsh. Shakar qoʻshma.*",

    "Bir soniya oʻylab koʻring. || Nega shakar qoʻshmaslik kerak?",

    "Dilnoza bu izohni tushunmadi. Axir shirinlikni shakar belgilaydi-ku.",

    "Hisoblab koʻramiz. Sof shakar 400 g, butun massa 2 000 g — demak "
    "*20 foiz*. | Dilnoza 500 g suv qoʻshdi: shakar hamon 400, massa esa "
    "2 500. Endi 16 foiz.",

    "Ustunlarga qarang. Foiz 20 dan 16 ga, keyin 10 ga tushdi. "
    "|| Shakar ustuni esa *qimirlamadi* — u hech qayoqqa ketmadi. "
    "Faqat maxraj kattalashdi.",

    "Demak shakar qoʻshish kerak emas edi. || Kerak boʻlgani — *suv*: "
    "u ulushni tushiradi.",

    "Mehmonlar 10 foizli qilishni soʻradi. Dilnoza teskari tomondan yurdi: "
    "agar 400 g butun massaning 10 foizi boʻlsa, massa 4 000 g boʻlishi shart. "
    "| Hozir 2 500 bor, demak yana *1 500 g suv*.",

    "Esda tutinglar. || *Suv qoʻshilsa shakar oʻzgarmaydi — faqat maxraj "
    "kattalashadi.* Shuning uchun foiz tushadi.",

    "Endi oʻzingiz oʻylang. Kompotni shirinroq qilish uchun nima qilish "
    "kerak va nega? || Izohda kutamiz.",

    None,   # outro — jim
])
