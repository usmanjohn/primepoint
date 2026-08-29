# -*- coding: utf-8 -*-
"""KO-2 — «Koreys alifbosi — ogʻzingizning surati»  KOREYA OLAMI

Manba: _stories_koreya_olami_01_13.py, order 13.

The Matematika olami register applied to a language: era → portrait → the
obstacle → the method → the number → what survives. It works here for the same
reason it worked for Ulugʻbek — a real person, a real date, and a mechanism
that can be drawn rather than asserted.

The mechanism is the whole film. ㄱ is not "the letter that makes a k sound";
it is a picture of the tongue humped at the back of the mouth, and 훈민정음
해례본 says exactly that in 1446. So the argument is a diagram, and the viewer
can check it against their own mouth while watching — which is as close to a
countable quantity as a writing system gets.

⚠️ Narration carries NO lone jamo and NO hanja: neither can be transliterated,
and `cli.py script` refuses them. On screen they are the point; in the voice
they are said in Uzbek ("k tovushi").
"""

from spec import Video, Scene
from scenes import (era, word, echo, spell, shape, fact, rule, ask, practice,
                    outro)

VIDEO = Video(
    slug="ko02",
    lesson="Koreya olami",
    title="Koreys alifbosi — ogʻzingizning surati",
    story="Koreya olami — order 13",
    scenes=[
        era("Koreya", "1443", "Dunyoda kam alifbo bor — buni kim yaratgani aniq",
            dur=6.6,
            note="Boshqa alifbolarni kim oʻylab topganini hech kim bilmaydi."),

        word("세종", gloss="Sejong — Koreya shohi (1397–1450)",
             head="Kim yaratgan", dur=6.6, size=230,
             note="Yozuv xitoycha ierogliflar bilan olib borilardi — "
                  "ularni oʻrganishga yillar ketardi."),

        word("훈민정음", gloss="«Xalqni oʻrgatuvchi toʻgʻri tovushlar»",
             head="1446 — kitob chop etildi", dur=7.0, size=150,
             note="Alifbo 1443-yilda tugatilgan, kitob uch yildan keyin "
                  "chiqqan. Ikki sana — alohida."),

        shape("vel", "Til ildizi boʻgʻizni toʻsgan shakl",
              head="Harf nima uchun shunday chizilgan", dur=8.0,
              note="«K» tovushini ayting va tilingiz orqasi qayerga "
                   "borishini his qiling."),

        shape("lab", "Ogʻizning oʻzi — shuning uchun kvadrat", dur=7.4,
              note="Kitob buni toʻgʻridan-toʻgʻri aytadi: ogʻiz shakli."),

        spell("한", head="Harflar blokka yigʻiladi",
              caption="Undosh + unli + undosh — bittagina blokda", dur=8.0,
              note="Koreys yozuvi imlo emas, boʻgʻinning diagrammasi."),

        echo("한글", gloss="koreys alifbosi",
             note="JIM sahna. Koreyscha ovoz soʻzni ikki marta aytadi."),

        fact("28", "ta harf edi", cap="Bugun 24 tasi ishlatiladi.",
             dur=6.4, dark=True,
             note="Toʻrttasi isteʼmoldan chiqqan."),

        rule("한글 ni yodlash shart emas — uni tushunish mumkin",
             strip="harf  =  uni aytadigan aʼzoning surati",
             meaning="«훈민정음 해례본» 1997-yilda YUNESKOning «Jahon xotirasi» "
                     "roʻyxatiga kiritilgan.",
             head="Nima qoldi", dur=9.4),

        ask("ㅋ harfi ㄱ ga bitta chiziq qoʻshib yasalgan. "
            "Chiziq qoʻshilsa, tovush qanday oʻzgaradi?",
            dur=7.2, note="Javobni aytmang."),

        practice("Prime Korean · PK-1 dan boshlang",
                 sub="powerty.uz → Darslar → Prime Korean", dur=5.2),

        outro(line2="koreys tili"),
    ],
)

# ── Ovoz uchun matn (TTS) ──
from spec import narrate

narrate(VIDEO, [
    "Dunyodagi alifbolarning deyarli hammasini kim oʻylab topganini hech kim "
    "bilmaydi. || Bittasini bilamiz.",

    "Koreya, 1443-yil. Shoh *세종*. | Oʻsha paytda yozuv xitoycha ierogliflar "
    "bilan olib borilardi — ularni oʻrganishga yillar ketardi.",

    "Uch yildan keyin alifboni tushuntiruvchi kitob chiqdi: *훈민정음*. "
    "| Yaʼni, xalqni oʻrgatuvchi toʻgʻri tovushlar.",

    "Endi eng qizigʻi. Harflar shunchaki chizilmagan. || Hozir «k» tovushini "
    "ayting. | Tilingizning orqasi boʻgʻizni toʻsadi — birinchi harf aynan "
    "shu shaklni chizadi.",

    "Ikkinchisi — ogʻizning oʻzi. || Shuning uchun u kvadrat.",

    "Harflar qatorga emas, blokka yigʻiladi. | Undosh, unli, yana undosh — "
    "va bitta belgi hosil boʻladi.",

    None,   # echo — jim sahna, koreyscha ovoz

    "Dastlab 28 ta harf bor edi. | Bugun 24 tasi ishlatiladi.",

    "Shuning uchun bu alifboni yodlash shart emas — uni tushunish mumkin. "
    "|| Kitob esa 1997-yilda Yuneskoning Jahon xotirasi roʻyxatiga kiritilgan.",

    "Endi oʻzingiz oʻylang. Harfga yana bitta chiziq qoʻshsak, tovush "
    "qanday oʻzgaradi? Izohda kutamiz.",

    "Koreys alifbosini noldan oʻrganmoqchi boʻlsangiz, Powertyda Prime Korean "
    "kursi bor: birinchi darsdan boshlang.",

    None,   # outro — jim
])
