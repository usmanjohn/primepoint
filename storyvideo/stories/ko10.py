# -*- coding: utf-8 -*-
"""KO-10 — «Ikkinchi boʻgʻin — yettita soʻz»  ·  BITTA SOʻZ

Manba: examprep VocabRoot 입(入), TOPIK track — the bank's own family of seven.

**This film is the sequel ko01 asked for.** ko01 ended on exactly this question:

    ask("출(出) — chiqmoq. Unda 입(入) nima degani? 입구 qanday joy?")

So the `ask` scene of the first Korean film is the cover of this one. That is
worth more than the vocabulary: a viewer who answered it gets paid, and the
open question stops being a rhetorical flourish and becomes a link.

It is also the only Korean film whose engine is a QUANTITY rather than a
mistake — the counter counts words off the live DOM, exactly as ko01's did.
The turn is at 수입: up to there the words are learned, after it they are read,
because 수출 was already learned in ko01 and 수입 is its mirror.

⚠️ 입학 romanises to `ipak`, which is the Uzbek word for silk. The Hangul is on
screen and the gloss says «oʻquv yurtiga kirish», but the narration names the
context (universitet) so the collision cannot bite.
"""

from spec import Video, narrate
from scenes import cover, word, echo, word_family, versus, rule, ask, practice, outro

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:72px">%s</span>'

VIDEO = Video(
    slug="ko10",
    lesson="Koreya olami",
    title="Ikkinchi boʻgʻin — yettita soʻz",
    story="examprep VocabRoot 입(入)",
    subject="korean",
    scenes=[
        cover("입", "Yettita soʻz",
              kicker="Bitta soʻz",
              context="출 chiqmoq edi. Unda 입?",
              strike=False,
              note="MUQOVA: ko01 aynan shu savol bilan tugagan. Uni koʻrgan "
                   "odam javobini biladi va tasdiqlash uchun qoladi; "
                   "koʻrmagan odam esa savolni birinchi marta eshitadi."),

        word("입구", gloss="kirish joyi", hanja="入口",
             head="Metroda 출구 ning yonida turadi", dur=6.6,
             note="Eng yaxshi kirish nuqtasi: ikkita yozuv har koreys "
                  "binosida yonma-yon turadi."),

        echo("입구", gloss="kirish joyi", hanja="入口",
             note="JIM sahna. Koreyscha ovoz ikki marta aytadi."),

        word_family(
            "입",
            [("입구", "入口", "kirish joyi"),
             ("출입", "出入", "kirish-chiqish"),
             ("입학", "入學", "oʻquv yurtiga kirish"),
             ("입원", "入院", "kasalxonaga yotish"),
             ("가입", "加入", "aʼzo boʻlish"),
             ("신입", "新入", "yangi kelgan"),
             ("수입", "輸入", "import")],
            hanja="入", meaning="kirmoq", label="ta soʻz", cols=1, dur=11.5,
            note="Yettitasi ham bitta ildizdan. Oltin harf — oʻsha ildiz."),

        versus({"name": "출 — chiqmoq",
                "qty": KQ % "출구",
                "price": K % "수출",
                "tag": "chiqish · eksport"},
               {"name": "입 — kirmoq",
                "qty": KQ % "입구",
                "price": K % "수입",
                "tag": "kirish · import"},
               title="Ikkita ildiz — bitta oyna",
               dur=12.0,
               note="Filmning eng kuchli kadri: ildizlar juft-juft yuradi, "
                    "shuning uchun bittasini bilgan odam ikkinchisini "
                    "tekinga oladi."),

        word("수입", gloss="«tashib kiritish» — import", hanja="輸入",
             head="ko01 da 수출 ni koʻrgan edingiz", dur=7.0,
             note="Burilish nuqtasi: bu soʻzni yodlash shart emas, "
                  "oʻqib chiqarish mumkin."),

        echo("수입", gloss="import", hanja="輸入",
             note="JIM sahna. Koreyscha ovoz."),

        rule("Ildizlar juft-juft yuradi — birini bilsangiz, ikkinchisi tekin",
             strip=K % "출" + " ↔ " + K % "입" + "   ·   "
                   + K % "수출" + " ↔ " + K % "수입",
             meaning="Xitoycha ildizlar koʻpincha qarama-qarshi juft boʻlib "
                     "kiradi: chiqish va kirish, eksport va import. Bitta "
                     "juftni oʻrgangan odam lugʻatning ikki barobarini oladi.",
             dur=9.8),

        ask("출입 — kirish-chiqish. Unda 출입구 qanday joy boʻladi?",
            dur=7.2,
            note="Javobni aytmang. Uchta boʻgʻin ham videoda koʻrsatilgan."),

        practice("TOPIK lugʻat · soʻz oilalari",
                 sub="powerty.uz → Examprep → Lugʻat → Soʻz oilalari", dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Birinchi videoda *출* chiqmoq degani edi. | Va u toʻqqizta soʻzni "
    "ochgan edi. || Endi uning juftini olamiz.",

    "Koreys binolarida ikkita yozuv yonma-yon turadi. | *출구* — chiqish "
    "joyi. || *입구* — kirish joyi.",

    None,   # echo(입구) — jim sahna, koreyscha ovoz

    "Endi sanaymiz. Kirish joyi. Kirish-chiqish. | Universitetga qabul. "
    "| Kasalxonaga yotish. | Aʼzo boʻlish. | Yangi kelgan odam. "
    "|| Yettita soʻz, hammasi bitta ildizdan.",

    "Va eng chiroyli tomoni shu. | *출구* ning juftini bilsangiz, *수출* "
    "ning juftini ham bilasiz. || Chiqish va kirish, eksport va import.",

    "*수입* soʻzini oling. | Tashib kiritish degani, yaʼni import. "
    "|| Birinchi videoda *수출* ni koʻrgan odam bu soʻzni yodlamaydi — "
    "oʻqib chiqaradi.",

    None,   # echo(수입) — jim sahna, koreyscha ovoz

    "Shuning uchun xitoycha ildizlar koʻpincha juft-juft kiradi. "
    "|| Bitta juftni oʻrgansangiz, lugʻatning ikki barobarini olasiz.",

    "Endi oʻzingiz oʻylang. *출입* kirish-chiqish boʻlsa, || *출입구* "
    "qanday joy boʻladi? Izohda kutamiz.",

    "Ellik bitta ildizning hammasi Powertyda: Examprep, lugʻat, "
    "soʻz oilalari.",

    None,   # outro — jim
])
