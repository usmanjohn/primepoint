# -*- coding: utf-8 -*-
"""KO-6 — Bitta soatda ikkita sanoq  ·  TUTILGAN XATO

Manba: Prime Korean PK-23 va PK-24 (한자어 va 고유어 sonlar).

The third «Tutilgan xato», and the one with the best cover in the batch: the
wrong reading of a clock, with the promise «Yarmi xato». A viewer cannot let
that go -- they have to find out which half.

The fact underneath is genuinely strange and completely true: Korean keeps two
whole counting systems and a clock reading uses BOTH at once, native for the
hour and Sino for the minute. Nothing in Uzbek prepares a pupil for it, so
this is the one film in the batch whose mistake is not caused by Uzbek -- it
is caused by the language itself. That is why the arc puts the mechanism
(`versus`) before the correction: the pupil cannot be told they are wrong
until they have been shown there are two systems to be wrong about.

Every reading in it was checked against PK-23/24 and re-derived by hand:
  3시    -> 세 시      (native; 셋 loses its batchim before a counter)
  30분   -> 삼십 분    (Sino)
  10시   -> 열 시      (native)
  20분   -> 이십 분    (Sino)
  20 yosh-> 스무 살    (native; 스물 -> 스무 before a counter)
  1997   -> 천구백구십칠 (Sino -- which is what the closing question turns on)
"""

from spec import Video, narrate
from scenes import (cover, says, versus, correct, check, echo,
                    rule, ask, practice, outro)

K = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:64px">%s</span>'

VIDEO = Video(
    slug="ko06",
    lesson="PK-24",
    title="Bitta soatda ikkita sanoq",
    story="Prime Korean PK-23, PK-24",
    subject="korean",
    scenes=[
        cover('<span class="strike">삼 시</span> 삼십 분', "Yarmi xato",
              kicker="Tutilgan xato",
              context="Soat 3:30 — koreyscha:",
              strike=False,
              note="MUQOVA: qizil chiziq FAQAT soatdan oʻtadi — daqiqa "
                   "toʻgʻri. Butun gapni chizib tashlasa, rasm «yarmi xato» "
                   "degan vaʼdaga qarshi chiqadi va muqova yolgʻon boʻladi."),

        says("Sherbek", [("Soat uch yarim:", "lbl"),
                         ("삼 시 삼십 분", "expr ko")],
             mood="smile",
             note="Ishonch bilan aytdi — va yarmi toʻgʻri. Shuning uchun "
                  "xatoni topish qiyin."),

        versus({"name": "koreyscha sanoq",
                "qty": KQ % "하나 · 둘 · 셋",
                "price": "soat · odam · narsa · yosh",
                "tag": K % "한 살"},
               {"name": "xitoycha sanoq",
                "qty": KQ % "일 · 이 · 삼",
                "price": "daqiqa · pul · oy · yil",
                "tag": K % "삼십 분"},
               title="Koreys tilida ikkita sanoq tizimi bor",
               dur=12.5,
               note="Mexanizm avval, tuzatish keyin: ikkita tizim borligini "
                    "koʻrmagan odamni xato qildi deb ayblash mumkin emas."),

        echo("하나 둘 셋", gloss="bir, ikki, uch — koreyscha sanoq", size=140,
             note="JIM sahna. Koreyscha sanoqni hech kim taxmin qila olmaydi, "
                  "xitoychasini esa (일 이 삼) oʻzbek quloq osongina tutadi — "
                  "shuning uchun aynan bu ladder eshitiladi."),

        correct("삼 시", "세 시",
                because="Soat — koreyscha son. Daqiqa — xitoycha son.",
                lead="3시 30분",
                note="Daqiqa chizib tashlanmadi — u toʻgʻri edi. "
                     "Xato aynan soatda."),

        check("10시 20분",
              parts=["Soat → koreyscha: 열",
                     "Daqiqa → xitoycha: 이십"],
              verdict=K % "열 시 이십 분",
              title="Endi oʻzingiz sinang",
              dur=8.2,
              note="Yangi soat, xuddi shu qoida — qoidani qoʻllagani "
                   "koʻrinsin."),

        echo("세 시 삼십 분", gloss="uch yarim", size=104,
             note="JIM sahna. Koreyscha ovoz ikki marta aytadi."),

        rule("Soatni koreyscha, daqiqani xitoycha sanang",
             strip=K % "시" + " → 하나 둘 셋   ·   " + K % "분" + " → 일 이 삼",
             meaning="Bu xato oʻzbek tilidan kelmaydi — koreys tilining "
                     "oʻzida ikkita sanoq tizimi yonma-yon yashaydi. "
                     "Yodlash kerak boʻlgani: qaysi tizim nimani sanaydi.",
             dur=9.6),

        ask("Yoshni koreyscha sanoq bilan sanaydi: 한 살, 두 살. "
            "Unda pasportdagi tugʻilgan yilni qaysi sanoq bilan oʻqiydi?",
            dur=8.0,
            note="Javobni aytmang. Jadvalda «yil» qaysi ustunda turgani "
                 "koʻrsatilgan — diqqat bilan qaragan topadi."),

        practice("Prime Korean · PK-24",
                 sub="Koreyscha sonlar va sanoq soʻzlari", dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Soat uch yarimni koreyscha oʻqing. || Sherbek shunday oʻqidi — va "
    "yarmi xato.",

    "Diqqat qiling: *삼 시 삼십 분*. | Bir qarashda hammasi joyida "
    "koʻrinadi.",

    "Ammo koreys tilida ikkita sanoq tizimi bor. | Koreyscha sanoq: "
    "*하나*, *둘*, *셋* — soatni, odamni, narsani va yoshni sanaydi. "
    "|| Xitoycha sanoq: *일*, *이*, *삼* — daqiqani, pulni, oyni va "
    "yilni sanaydi.",

    None,   # echo(하나 둘 셋) — jim sahna, koreyscha ovoz

    "Demak daqiqa toʻgʻri edi. | Xato soatda: *삼 시* emas, *세 시*.",

    "Endi oʻzingiz sinang. Soat oʻn yigirma. | Soat — koreyscha: *열*. "
    "| Daqiqa — xitoycha: *이십*. || *열 시 이십 분*.",

    None,   # echo — jim sahna, koreyscha ovoz

    "Shuning uchun soatni koreyscha, daqiqani xitoycha sanaysiz. "
    "|| Bu xato ona tilingizdan kelmaydi — koreys tilining oʻzida ikkita "
    "sanoq tizimi yonma-yon yashaydi.",

    "Endi oʻzingiz oʻylang. Yoshni koreyscha sanoq bilan sanaydi. "
    "|| Unda pasportdagi tugʻilgan yilni qaysi sanoq bilan oʻqiydi? "
    "Izohda kutamiz.",

    "Koreyscha sonlar Powertyda: Prime Korean, 24-dars.",

    None,   # outro — jim
])
