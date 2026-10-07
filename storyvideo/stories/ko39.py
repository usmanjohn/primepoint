# -*- coding: utf-8 -*-
"""KO-39 — «Bitta boʻgʻin — butun maktab»  ·  BITTA SOʻZ

Manba: examprep VocabRoot 학(學), TOPIK track — bankning beshta soʻzi
(학자 학생 유학 학원 과학) + 학교, uni har bir pupil biladi va u ham 學校.
Hanja va maʼnolar: 學 oʻqish/ilm · 生 hayot · 院 muassasa · 者 kishi ·
留 qolmoq · 科 boʻlim, tur · 校 maktab · 文 yozuv.

Seriyaning oltinchisi (ko01 출 · ko10 입 · ko20 생 · ko24 회 · ko28 인 ·
ko36 불). Bu safar burilish — **oʻzbek tilining oʻz ustunligi**: bizda ham
xuddi shunday oila bor, faqat ildizi arabcha — ilm · olim · muallim ·
taʼlim · maʼlumot (ʻ-l-m). Pupil mexanizmni allaqachon biladi; film shuni
aytadi.

⚠️ Ovozda 학 yolgʻiz aytilmaydi — «hak» oʻzbekcha «haq» ga juda yaqin.
Ekranda boʻgʻin turadi, ovozda «bu boʻgʻin» deyiladi (STYLE_GUIDE §4, 불 → pul).
"""

from spec import Video, narrate
from scenes import (cover, build, word_family, echo, pairs, word, rule, ask,
                    practice, outro)

K = '<span class="ko">%s</span>'

VIDEO = Video(
    slug="ko39",
    lesson="Koreya olami",
    title="Bitta boʻgʻin — butun maktab",
    story="examprep VocabRoot 학(學)",
    subject="korean",
    scenes=[
        cover("학생 학원 유학", "Bitta ildiz, oltita soʻz",
              kicker="Bitta soʻz", ko="한국어",
              context="Uch soʻz — bitta boʻgʻin:",
              strike=False, size=124,
              note="MUQOVA: gʻalati narsa — uch xil soʻz bitta boʻgʻindan "
                   "boshlanadi. Vaʼda toʻrt soʻz."),

        build([("학", "oʻqish", True), ("원", "muassasa", False)],
              "학원", gloss="oʻquv markazi",
              head="Kechqurun boradigan joy",
              dur=8.5,
              note="Oltin plitka — bugungi ildiz. 학원 — har bir koreys "
                   "oʻquvchisi biladigan soʻz."),

        word_family(
            "학",
            [("학교", "學校", "maktab"),
             ("학생", "學生", "oʻquvchi"),
             ("학원", "學院", "oʻquv markazi"),
             ("학자", "學者", "olim"),
             ("유학", "留學", "xorijda oʻqish"),
             ("과학", "科學", "fan")],
            hanja="學", meaning="oʻqish, ilm", label="ta soʻz",
            cols=2, dur=12.0,
            note="Oltita — beshtasi bankniki, 학교 qoʻshildi."),

        echo("학교", gloss="maktab",
             note="JIM sahna. Ikki boʻgʻin."),

        pairs([("학 + 생", "oʻqish + hayot → oʻquvchi"),
               ("학 + 자", "oʻqish + kishi → olim"),
               ("과 + 학", "boʻlim + ilm → fan")],
              head="Ildiz oldinda ham, oxirida ham",
              tail="Joyi emas — maʼnosi muhim.",
              dur=12.0,
              note="Fan = «boʻlimlarga ajratilgan ilm» — 科 boʻlim, tur."),

        word("유학", gloss="xorijda oʻqish", hanja="留學",
             head="Eng chiroylisi", dur=7.4, dark=True,
             note="Burilish: 留 — qolmoq. Soʻzma-soʻz «qolib oʻqish»."),

        pairs([("ilm · olim · muallim", "bitta arab ildizi"),
               ("taʼlim · maʼlumot", "oʻsha ildiz"),
               ("학교 · 학생 · 학자", "bitta xitoy ildizi")],
              head="Bizda ham xuddi shunday",
              tail="Mexanizmni allaqachon bilasiz.",
              dur=12.5,
              note="Filmning yuragi: oʻzbek pupilning ustunligi. Hamma "
                   "beshtasi ʻ-l-m ildizidan."),

        echo("유학", gloss="xorijda oʻqish",
             note="JIM sahna, ikkinchisi."),

        rule("학 (學) — oʻqish, ilm",
             strip=K % "학교" + " · " + K % "학생" + " · " + K % "학원"
                   + " · " + K % "학자" + " · " + K % "유학" + " · "
                   + K % "과학",
             meaning="Bu boʻgʻin qayerda tursa ham, maʼnosi bitta: oʻqish. "
                     "Oʻzbekchada «ilm» ildizi xuddi shunday ishlaydi — "
                     "ilm, olim, muallim. Ildizni taniysiz — yangi soʻzning "
                     "maʼnosini taxmin qilasiz.",
             dur=11.0),

        ask("문 — yozuv. Unda 문학 qanday fan?",
            dur=7.0,
            note="Javobni aytmang (adabiyot). 文 bankda bor (문화), "
                 "lekin videoda yoʻq."),

        practice("TOPIK lugʻat · soʻz oilalari",
                 sub="powerty.uz → Examprep → Lugʻat → Soʻz oilalari",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Uch xil soʻz, | lekin uchalasi bitta boʻgʻindan boshlanadi. "
    "|| Bugun oʻsha boʻgʻin.",

    "학원 — oʻquv markazi. | Oldingisi — oʻqish, keyingisi — muassasa. "
    "|| Kechqurun boradigan joyingiz.",

    "Shu boʻgʻin oltita soʻz ochadi: | maktab, oʻquvchi, oʻquv markazi, "
    "olim, | xorijda oʻqish. || Va fan.",

    None,   # echo(학교)

    "Ildiz oldinda ham turadi, oxirida ham. "
    "| Fan — boʻlimlarga ajratilgan ilm.",

    "Eng chiroylisi: 유학. | Oldingi boʻgʻin — qolmoq. "
    "|| Uydan uzoqda qolib, oʻqiysiz.",

    "Bizda ham xuddi shunday: | ilm, olim, muallim, taʼlim. "
    "|| Bitta arab ildizi. Mexanizmni allaqachon bilasiz!",

    None,   # echo(유학)

    "Bu boʻgʻin qayerda tursa ham, maʼnosi bitta: oʻqish. "
    "|| Ildizni taniysiz — maʼnoni taxmin qilasiz.",

    "Endi oʻzingiz, toʻnkalar. [laughs] Kechirasiz, aqllilar! "
    "| 문 — yozuv. 문학 qanday fan? || Izohda kutamiz.",

    "Ellik bitta ildizning hammasi Powertyda: Examprep, lugʻat, "
    "soʻz oilalari.",

    None,   # outro
])
