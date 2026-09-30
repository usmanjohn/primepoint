# -*- coding: utf-8 -*-
"""KO-30 — «Uchinchi masofa»  ·  NEGA SHUNDAY?  ·  GRAMMATIKA 02

Manba: Prime Korean PK-15 — 이거/그거/저거 va 여기/거기/저기.

Grammatika yoʻlining ikkinchisi, va u ataylab XATO filmi emas. Ketma-ket
uchta «tutilgan xato» bitta filmni uch marta koʻrsatgandek boʻladi
(SERIES.md §3), shuning uchun bu — kashfiyot: oʻzbek tilida bu tizim
ALLAQACHON bor.

Filmning gapi bitta: koreys tilini ingliz tili orqali oʻrganmang. Inglizchada
ikkita masofa bor — this va that — shuning uchun darsliklar 그 ni ham, 저 ni
ham «that» deb tarjima qiladi va pupil ikkisini aralashtiradi. Oʻzbekchada
esa aynan uchta: **bu · shu · u**. Mos kelish tasodif emas, lekin bu yerda
sabab muhim emas — foydasi muhim.

⚠️ 그 = tinglovchiga yaqin YOKI ikkalaga maʼlum. «Shu» ning ikkala vazifasi
ham xuddi shunday, shuning uchun juftlik toʻliq.
"""

from spec import Video, narrate
from scenes import (cover, word, pairs, says, echo, rule, ask,
                    practice, outro)

VIDEO = Video(
    slug="ko30",
    lesson="PK-15",
    title="Uchinchi masofa",
    story="Prime Korean PK-15 — koʻrsatish olmoshlari",
    subject="korean",
    scenes=[
        cover("이 · 그 · 저", "Oʻzbekchada ham uchta",
              kicker="Nega shunday?", ko="한국어",
              track="Grammatika", n=2, badge="big",
              context="Koreysda uchta masofa bor:",
              strike=False,
              note="MUQOVA: gʻalati narsa — uchta koʻrsatkich. Vaʼda "
                   "kutilmagan xushxabar, shuning uchun chizilmaydi."),

        word("그거", gloss="shu narsa — sizning yoningizda",
             head="Eng koʻp adashtiradigani", dur=6.6,
             note="Boshlanish 그 dan, 이 dan emas: qiyinchilik shu yerda."),

        pairs([("이거", "bu — menga yaqin"),
               ("그거", "shu — sizga yaqin, yoki ikkimizga maʼlum"),
               ("저거", "u — ikkimizdan ham uzoqda")],
              head="Kim tomonda turganiga qarab tanlanadi",
              tail="Bu · shu · u. Aynan uchta.",
              dur=13.0,
              note="Filmning dalili: jadvalning oʻng ustuni oʻzbekcha va "
                   "u toʻliq — birorta katak boʻsh qolmaydi."),

        pairs([("여기", "bu yer"),
               ("거기", "shu yer"),
               ("저기", "u yer")],
              head="Joylar ham xuddi shu uchlik",
              tail="Bitta qoidani ikki marta oʻrganish shart emas.",
              dur=11.0,
              note="Ikkinchi jadval birinchisini isbotlaydi: tizim, "
                   "roʻyxat emas."),

        says("Zilola", [("Doʻkonda, uzoqdagi narsaga:", "lbl"),
                        ("저거 주세요.", "expr ko")],
             mood="smile", dur=6.4,
             note="Amalda. Uzoqdagi narsa — 저거. Sotuvchining qoʻlidagisi "
                  "boʻlsa, 그거 boʻlardi."),

        echo("저거 뭐예요", gloss="u nima?",
             note="JIM sahna. Uzoqdagi narsa haqida savol."),

        rule("Ingliz tilida ikkita masofa bor, oʻzbekchada — uchta",
             strip="이 = bu   ·   그 = shu   ·   저 = u",
             meaning="Darsliklar 그 ni ham, 저 ni ham «that» deb tarjima "
                     "qiladi va ikkisi qoʻshilib ketadi. Oʻzbekchaga "
                     "oʻgiring — «shu» va «u» hech qachon aralashmaydi.",
             dur=10.5),

        ask("Telefon orqali gaplashyapsiz va suhbatdoshingiz "
            "qoʻlidagi narsa haqida soʻrayapsiz. | 그거 mi, 저거 mi?",
            dur=7.6,
            note="Javobni aytmang. Videoda «yaqin/uzoq» bor, lekin "
                 "telefon holati umuman koʻrilmagan."),

        practice("Prime Korean · PK-15",
                 sub="powerty.uz → Darsliklar → Prime Korean",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreysda uchta koʻrsatkich bor: 이, 그, 저. "
    "|| Va oʻzbek tilida ham aynan uchta.",

    "Eng koʻp adashtiradigani — 그거. | «Shu narsa» degani: sizning "
    "yoningizdagi narsa.",

    "Menga yaqin boʻlsa — *이거*, bu. | Sizga yaqin boʻlsa — *그거*, shu. "
    "|| Ikkimizdan ham uzoqda boʻlsa — *저거*, u.",

    "Joylar ham xuddi shunday: *여기* bu yer, *거기* shu yer, "
    "*저기* u yer. || Bitta qoidani ikki marta oʻrganish shart emas.",

    "Doʻkonda Zilola uzoqdagi narsaga koʻrsatadi: 저거 주세요. "
    "| Sotuvchining qoʻlida boʻlganida, 그거 boʻlardi.",

    None,   # echo(저거 뭐예요)

    "Ingliz tilida ikkita masofa bor — this va that. "
    "| Shuning uchun darsliklar 그 ni ham, 저 ni ham «that» deb tarjima "
    "qiladi, va ikkisi qoʻshilib ketadi. "
    "|| Oʻzbekchaga oʻgiring: «shu» va «u» hech qachon aralashmaydi.",

    "Endi oʻzingiz oʻylang. Telefonda gaplashyapsiz va suhbatdoshingiz "
    "qoʻlidagi narsani soʻrayapsiz. | 그거 mi, 저거 mi? "
    "|| Izohda kutamiz.",

    "Prime Korean — yuzta dars, boshidan. Powertyda, oʻn beshinchi dars.",

    None,   # outro
])
