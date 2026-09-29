# -*- coding: utf-8 -*-
"""KO-20 — «Birinchi darsdagi soʻzning yarmi»  ·  BITTA SOʻZ

Manba: examprep VocabRoot 생(生), TOPIK track — oltita soʻz bankning oʻziniki.

The third root film, and the one that stops arguing and starts collecting.
ko01 (출) made the claim; ko10 (입) showed roots come in pairs. This one takes
the word the viewer learned in their FIRST Korean lesson -- 학생 -- and opens
it. That is the move the other two could not make, because 출구 and 입구 are
words a beginner meets on a wall, not words they already own.

So the turn is not «you can read a new word», it is «you already half-knew six
words and nobody told you». The `build` beat (new, 2026-09-22) is what makes
that land: 학(ilm) and 생(hayot) walk in as separate tiles and become 학생 in
front of the viewer, instead of being asserted to be inside it.

생 also sits under 고생 in ko27's proverb and under 인생 in ko28's root film,
so this is the batch's hub. That is deliberate: a channel is worth more when
its films point at each other.
"""

from spec import Video, narrate
from scenes import (cover, word, build, word_family, echo, versus,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:80px">%s</span>'

VIDEO = Video(
    slug="ko20",
    lesson="Koreya olami",
    title="Birinchi darsdagi soʻzning yarmi",
    story="examprep VocabRoot 생(生)",
    subject="korean",
    scenes=[
        cover("학생", "Yarmini bilmaysiz",
              kicker="Bitta soʻz",
              ko="한국어",
              context="Birinchi darsda oʻrgangan soʻzingiz:",
              strike=False,
              note="MUQOVA: gʻalati narsa — tanish soʻz ustidan tushgan "
                   "shubha. Vaʼda ikki soʻz va u qarama-qarshilik "
                   "koʻtaradi: bilaman degan odamga «yoʻq» deyiladi."),

        word("학생", gloss="oʻquvchi, talaba", hanja="學生",
             head="Buni hamma biladi", dur=6.4,
             note="Ataylab eng oddiy soʻz. Film shundan boshlanishi kerak, "
                  "chunki uning butun gapi — tanish soʻzning ichi."),

        build([("학", "ilm", False), ("생", "hayot", True)],
              "학생", gloss="«ilm hayoti» — oʻquvchi",
              head="Ikkita boʻgʻin, ikkita maʼno",
              caption="Ikkinchisi — bugungi ildizimiz",
              dur=10.0,
              note="YANGI BEAT: soʻz koʻz oldida yigʻiladi. Oltin plitka — "
                   "ildiz. `spell` boʻgʻinni jamolarga ajratadi, bu esa "
                   "soʻzni ildizlarga."),

        word_family(
            "생",
            [("학생", "學生", "oʻquvchi"),
             ("인생", "人生", "umr — inson hayoti"),
             ("생활", "生活", "turmush, hayot tarzi"),
             ("생산", "生産", "ishlab chiqarish"),
             ("생명", "生命", "jon, hayot"),
             ("발생", "發生", "yuz berish")],
            hanja="生", meaning="hayot — tugʻilmoq", label="ta soʻz",
            cols=1, dur=12.0,
            note="Oltitasi ham bitta ildizdan. Sanagich jonli DOM dan "
                 "sanaydi — ekrandagi son rasmdan oldinga oʻta olmaydi."),

        echo("인생", gloss="umr — inson hayoti", hanja="人生",
             note="JIM sahna. Ikkita ildiz yonma-yon: odam va hayot."),

        versus({"name": "생 oldinda",
                "qty": KQ % "생활",
                "price": "turmush",
                "tag": "hayot + faoliyat"},
               {"name": "생 orqada",
                "qty": KQ % "학생",
                "price": "oʻquvchi",
                "tag": "ilm + hayot"},
               title="Ildiz ikkala tomonda ham ishlaydi",
               verdict="Joyi oʻzgaradi, maʼnosi — yoʻq",
               dur=12.0,
               note="Nega bu muhim: yangi soʻz koʻrganda ildizni oldidan "
                    "ham, oxiridan ham qidirish kerak."),

        word("생일", gloss="tugʻilgan kun", hanja="生日",
             head="Va buni ham bilasiz", dur=7.0,
             note="Burilish nuqtasi. Tomoshabin bu soʻzni yodlagan edi; "
                  "endi u soʻz emas, ikkita ildiz."),

        echo("생명", gloss="jon, hayot", hanja="生命",
             note="JIM sahna. Oilaning eng ogʻir soʻzi."),

        rule("Tanish soʻzni ham ochib koʻring",
             strip=K % "학" + " ilm + " + K % "생" + " hayot = "
                   + K % "학생",
             meaning="Yodlangan soʻz — yopiq quti. Uni ochgan odam ichidan "
                     "ikkita ildiz topadi, va oʻsha ikkita ildiz keyingi "
                     "oʻnlab soʻzni oʻzi ochadi.",
             dur=9.8),

        ask("«학생» ilm hayoti edi. Unda «학교» — qanday joy?",
            dur=7.2,
            note="Javobni aytmang. Videoda 학 bor, 교 yoʻq."),

        practice("TOPIK lugʻat · soʻz oilalari",
                 sub="powerty.uz → Examprep → Lugʻat → Soʻz oilalari",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreys tilini birinchi darsdan boshlagan odam *학생* soʻzini biladi. "
    "|| Yarmini esa yoʻq.",

    "*학생* — oʻquvchi degani. | Buni hamma yodlagan.",

    "Endi uni ochamiz. *학* — ilm. | *생* — hayot. || Yaʼni «ilm hayoti».",

    "Va oʻsha *생* yana beshta soʻzni ochadi: umr, turmush, ishlab "
    "chiqarish, jon, yuz berish. || Oltitasi ham bitta ildizdan.",

    None,   # echo(인생) — jim sahna, koreyscha ovoz

    "Eʼtibor bering: ildiz oldinda ham, orqada ham turaveradi. "
    "|| Shuning uchun uni soʻzning ikkala chetidan qidiring.",

    "Va mana buni ham bilasiz: *생일*. | Tugʻilgan kun. "
    "|| Yaʼni «hayot kuni».",

    None,   # echo(생명) — jim sahna, koreyscha ovoz

    "Yodlangan soʻz — yopiq quti. | Uni ochsangiz, ichidan ikkita ildiz "
    "chiqadi. || Va ular keyingi soʻzlarni oʻzi ochadi.",

    "Endi oʻzingiz oʻylang. *학* ilm boʻlsa, *학교* qanday joy? "
    "|| Izohda kutamiz.",

    "Ellik bitta ildizning hammasi Powertyda: Examprep, lugʻat, "
    "soʻz oilalari.",

    None,   # outro — jim
])
