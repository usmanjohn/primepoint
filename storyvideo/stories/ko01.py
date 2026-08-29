# -*- coding: utf-8 -*-
"""KO-1 — «Bitta boʻgʻin — toʻqqizta soʻz»  KOREYA OLAMI

Manba: examprep VocabRoot 출(出), TOPIK track — the nine words are the bank's
own family, glosses trimmed for the screen.

The first Korean film, and it exists to prove one thing: the maths format did
not depend on maths. Its engine is a QUANTITY — nine words out of one syllable —
counted by the same counter that counts chairs, off the live DOM. The viewer is
not told that Korean vocabulary is built from roots; they watch nine words come
out of one and count them.

The turn is at 수출: up to there the words are learned, after it they are
*read*. That is the moment the video is for.
"""

from spec import Video, Scene
from scenes import fact, word, echo, word_family, rule, ask, practice, outro

VIDEO = Video(
    slug="ko01",
    lesson="Koreya olami",
    title="Bitta boʻgʻin — toʻqqizta soʻz",
    story="Koreya olami — order 1",
    scenes=[
        fact("9", "ta soʻz", cap="Bittagina boʻgʻindan.", dur=6.0, cam="pull",
             note="Ochilish: son avval, sabab keyin."),

        word("출구", gloss="chiqish joyi", hanja="出口",
             head="Koreyadagi har bir binoda bor", dur=6.4,
             note="Metroda, bozorda, aeroportda — hamma joyda shu yozuv."),

        echo("출구", gloss="chiqish joyi", hanja="出口",
             note="JIM sahna. Koreyscha ovoz soʻzni ikki marta aytadi — "
                  "tomoshabin takrorlaydi."),

        word("출", gloss="chiqmoq — tashqariga", hanja="出",
             head="Birinchi boʻgʻin", dur=6.2, size=220,
             note="Xitoychadan kirgan ildiz. Oʻzi soʻz emas — soʻz yasaydi."),

        word_family(
            "출",
            [("출구", "出口", "chiqish joyi"),
             ("출근", "出勤", "ishga chiqish"),
             ("출발", "出發", "joʻnash"),
             ("출석", "出席", "davomat"),
             ("제출", "提出", "topshirish"),
             ("수출", "輸出", "eksport"),
             ("외출", "外出", "koʻchaga chiqish"),
             ("출입", "出入", "kirish-chiqish"),
             ("지출", "支出", "xarajat")],
            hanja="出", meaning="chiqmoq", label="ta soʻz", cols=1, dur=12.0,
            note="Toʻqqiztasi ham bitta ildizdan. Oltin harf — oʻsha ildiz."),

        word("수출", gloss="«tashib chiqarish» — eksport", hanja="輸出",
             head="Buni yodlash shart emas", dur=7.0,
             note="Ildizni bilgan odam bu soʻzni birinchi koʻrishda oʻqiydi."),

        fact("51", "ta ildiz Powerty lugʻatida",
             cap="Ular ikki yuzdan ortiq soʻzni ochadi.", dur=6.8, dark=True,
             note="TOPIK II lugʻatining katta qismi — xitoycha ildizli."),

        rule("Soʻzni yodlama — ildizini top",
             strip="bitta ildiz  →  oʻnlab soʻz",
             meaning="Ildiz maʼnosini bilsangiz, hech qachon koʻrmagan soʻzni "
                     "ham taxmin qila olasiz.",
             dur=9.0, note="Filmning asosiy gapi."),

        ask("출(出) — chiqmoq. Unda 입(入) nima degani? 입구 qanday joy?",
            dur=7.0, note="Javobni aytmang. Videoda 출입 koʻrsatilgan — "
                          "diqqat bilan qaragan topadi."),

        practice("TOPIK lugʻat · soʻz oilalari",
                 sub="powerty.uz → Examprep → Lugʻat → Soʻz oilalari",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

# ── Ovoz uchun matn (TTS). Hangul avtomatik oʻzbekchaga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Koreys tilida bitta boʻgʻin 9 ta soʻzni ochib beradi. || Qanday qilib?",

    "Koreyadagi har bir binoda shu yozuv bor: *출구*. | Chiqish joyi.",

    None,   # echo — jim sahna, koreyscha ovoz gapiradi

    "Uning birinchi boʻgʻini — *출*. | Xitoychadan kirgan ildiz, maʼnosi: "
    "chiqmoq.",

    "Endi sanaymiz. Ishga chiqish. Yoʻlga chiqish. Davomat. Topshirish. "
    "Eksport. Xarajat. || 9 ta soʻz, hammasi bitta ildizdan.",

    "*수출* soʻzini oling. Tashib chiqarish degani. | Yaʼni eksport. "
    "|| Uni yodlash shart emas — oʻqib chiqarish mumkin.",

    "Powerty lugʻatida shunday 51 ta ildiz bor. | Ular ikki yuzdan ortiq "
    "soʻzni ochadi.",

    "Shuning uchun koreys lugʻatini soʻzma-soʻz yodlash — eng sekin yoʻl. "
    "|| Ildizni toping, soʻzlar oʻzi keladi.",

    "Endi oʻzingiz oʻylang. 출 chiqmoq boʻlsa, 입 nima degani? "
    "|| 입구 qanday joy? Izohda kutamiz.",

    "Ellik bitta ildizning hammasi Powertyda: Examprep, lugʻat, soʻz oilalari.",

    None,   # outro — jim
])
