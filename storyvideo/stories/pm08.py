# -*- coding: utf-8 -*-
"""PM-8 — «Ikki avtobus qachon bir vaqtda keladi»   SHAKL: TESKARI NATIJA

Manba: _stories_prime_math_07_09.py, order 8.

Bu videoning dvigateli — bitta juft son, ikkita savol, ikkita boshqa asbob.
12 va 18 avval EKUK beradi (uchrashuv), keyin EKUB (ulashish). Tomoshabin
birinchi yarmini oʻrganib oladi, ikkinchi yarmi esa uni ataylab chalgʻitadi.
"""

from spec import Video
from scenes import hook, says, beat, check, rule, ask, outro
from spec import Scene
import primitives as P

# ── 1-yarim: karralilar roʻyxati, 36 ikkalasida ham yonadi ──
_m12, s12 = P.multiples(12, 4, at=0.6, step=0.55, hit=36, label="12-avtobus")
_m18, s18 = P.multiples(18, 3, at=0.6 + s12 + 0.3, step=0.55, hit=36, label="18-avtobus")
lists = Scene(
    12.0,
    P.counters(P.counter(7, "yozilgan son", at=0.6, dur=s12 + 0.3 + s18,
                         counts=".chip"))
    + _m12 + _m18
    + P.line("ikkala roʻyxatda ham bor birinchi son", "lbl lbl--sm",
             at=0.6 + s12 + 0.3 + s18 + 0.5, anim="fade")
    + P.line("EKUK (12, 18) = 36", "expr gold",
             at=0.6 + s12 + 0.3 + s18 + 1.1, anim="pop", dur=0.6),
    cam="sink", top=True, name="multiples", counts=[7],
    claims=["12 × 3 = 36", "18 × 2 = 36"],
    note="Bekzod daftarini ochdi. 12, 24, 36, 48. 18, 36, 54. Ikkalasida ham 36.")

# ── 2-yarim: bir xil sonlar, boshqa savol ──
_pk, spk = P.packs(6, [(2, "🌸"), (3, "🍬")], at=0.8, step=0.34,
                   note="har birida 2 gul va 3 shirinlik")
packs = Scene(
    10.0,
    P.counters(P.counter(6, "paket", at=0.8, dur=spk, counts=".pack"))
    + _pk
    + P.line("EKUB (12, 18) = 6", "expr gold", at=0.8 + spk + 0.8,
             anim="pop", dur=0.6),
    cam="rise", top=True, name="packs", counts=[6],
    claims=["6 × 2 = 12", "6 × 3 = 18"],
    note="Endi boshqa savol: 12 gul va 18 shirinlikni teng ulashish. Olti paket.")

VIDEO = Video(
    slug="pm08",
    lesson="PM-8",
    title="Ikki avtobus qachon bir vaqtda keladi",
    story="Prime Math Readings — order 8",
    scenes=[
        hook("12", "daqiqada bir", "18", "daqiqada bir",
             "Qachon birga kelishadi?", dur=4.8),

        says("Nodira opa", [("Soat 8:00 da", "lbl"),
                            ("ikkalasi birga keldi", "expr"),
                            ("Yana qachon shunday boʻladi?", "ask")],
             dur=6.4, size=250,
             note="Soat 8:00 da ikkalasi birga kelib ketdi. Bekzod ulgurmay qoldi."),

        beat(4.2, note="Jim turing. 12 va 18 — qachon toʻgʻri keladi?"),

        lists,

        check("12 × 3 = 18 × 2 = 36", parts=["12-avtobus: uchinchi kelishi", "18-avtobus: ikkinchi kelishi"],
              verdict="Soat 8:36.", title="Tekshiramiz", dur=7.0,
              note="36 daqiqa. Demak avtobuslar 8:36 da yonma-yon keladi."),

        # Teskari natija: xuddi shu 12 va 18, lekin savol boshqa.
        says("Nodira opa", [("Sumkamda 12 gul va 18 shirinlik", "lbl"),
                            ("Eng koʻpi bilan nechta", "expr"),
                            ("bir xil paket chiqadi?", "ask")],
             dur=6.8, size=250, mood="think",
             note="Xuddi shu ikki son. Lekin savol butunlay boshqa: endi bor "
                  "narsani boʻlish kerak."),

        beat(3.6, note="Yana jim turing. Bu safar javob 36 emas."),

        packs,

        rule("Uchrashuv — EKUK, ulashish — EKUB",
             strip="qachon? → EKUK   ·   nechta guruh? → EKUB",
             meaning="Bir xil ikki son, ikki xil savol, ikki xil asbob.",
             dur=9.0,
             note="Savolni oʻqing: «qachon uchrashadi» boshqa, «nechta guruh» boshqa."),

        ask("Uchinchi avtobus har 8 daqiqada kelsa, uchalasi qachon birga keladi?",
            dur=6.6,
            note="Javobni aytmang. Izohda kutamiz."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
# ⚠️ Chegara: SSML bilan birga 2000 belgi. `cli.py script <slug> --one --ssml`
#    oshib ketsa ogohlantiradi. Qisqa gap — yaxshi gap.
from spec import narrate

narrate(VIDEO, [
    "Bir avtobus har 12 daqiqada keladi, ikkinchisi har 18 daqiqada. "
    "|| Qachon birga kelishadi?",

    "Ertalab soat sakkizda ikkalasi birga kelib ketdi. Bekzod ulgurmay "
    "qoldi. | Yana qachon shunday boʻladi?",

    "Oʻzingiz oʻylab koʻring. || Oʻn ikki va oʻn sakkiz qayerda uchrashadi?",

    "Bekzod karralilarni yozdi. Birinchisi: 12, 24, 36. | Ikkinchisi: "
    "18, 36. || Ikkalasida ham bor birinchi son — *36*. "
    "Eng kichik umumiy karrali.",

    "Tekshiramiz. 12 ni uchga koʻpaytirsak 36; 18 ni ikkiga koʻpaytirsak "
    "ham 36. Demak avtobuslar birga keladi — soat 8:36.",

    "Endi boshqa savol. Sumkamda 12 ta gul va 18 ta shirinlik bor. "
    "| Eng koʻpi bilan nechta bir xil paket chiqadi?",

    "Yana bir soniya. || Bu safar javob 36 emas.",

    "Endi bor narsani boʻlamiz. Olti paket chiqadi: har birida ikkita gul, "
    "uchta shirinlik. || Olti — eng katta umumiy boʻluvchi.",

    "Esda tutinglar. || *Qachon uchrashadi* desa — eng kichik umumiy "
    "karrali. | *Nechta guruh* desa — eng katta umumiy boʻluvchi.",

    "Endi oʻzingiz oʻylang. Uchinchi avtobus har 8 daqiqada kelsa, "
    "uchalasi qachon birga keladi? || Izohda kutamiz.",

    None,   # outro — jim
])
