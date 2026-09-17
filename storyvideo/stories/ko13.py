# -*- coding: utf-8 -*-
"""KO-13 — «Insho gapirilmaydi»  ·  TUTILGAN XATO  ·  TOPIK

Manba: examprep TOPIK — 쓰기 54 (600~700자 insho, 50 ball), va
STYLE_GUIDE_WRITING.md §7b ning oʻz qoidasi: «문어체 only».

The first TOPIK film, and it opens the register the whole exam turns on. A
learner arrives at 쓰기 54 with two years of 해요체 behind them -- every
textbook dialogue, every lesson, every drama line -- and writes the essay in
it. Nothing is ungrammatical. The essay is simply not an essay.

That is why this belongs to «Tutilgan xato» and not to a tips list: the cost
is not a rule broken, it is a register worn into the wrong room, exactly like
ko04's speech level. Only here it is worth fifty points, which is half of
쓰기 and one sixth of the whole test.

The stakes scene is the site's own arithmetic: 51 + 52 + 53 + 54 =
10 + 10 + 30 + 50 = 100. `lint` recomputes it, so the film cannot disagree
with the lesson it points at.

⚠️ The narration never says 문어체 or 해요체 as WORDS. Both are on screen,
where the Hangul is the point; in the voice they are «yozma uslub» and
«gapirish uslubi», because a pupil who cannot yet read the terms would hear
two identical-sounding noises where the film's whole contrast lives.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, check, correct, versus, echo,
                    pairs, rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:76px">%s</span>'

VIDEO = Video(
    slug="ko13",
    lesson="TOPIK 쓰기 54",
    title="Insho gapirilmaydi",
    story="examprep TOPIK — 쓰기 54",
    subject="korean",
    scenes=[
        cover('중요<span class="strike">해요</span>', "Butun insho ball yoʻqotdi",
              kicker="Tutilgan xato · TOPIK",
              context="TOPIK inshosi — 54-savol, 50 ball:",
              strike=False,
              note="MUQOVA: chiziq faqat qoʻshimchadan oʻtadi — soʻz toʻgʻri, "
                   "uslub notoʻgʻri. Vaʼda bahoni aytadi, qoidani emas."),

        says("Bekzod", [("Inshoni shunday boshladi:", "lbl"),
                        ("독서는 중요해요", "expr ko")],
             mood="smile",
             note="Grammatikada xato yoʻq. Ikki yillik darslikning tili — "
                  "faqat bu yerda emas."),

        consequence("Nodira opa", "Bu — xabar, insho emas.",
                    mood="think",
                    note="Xatoning bahosi: matn oʻz janridan chiqib ketdi. "
                         "Bitta jumla emas — olti yuz belgining hammasi."),

        check("10 + 10 + 30 + 50 = 100",
              parts=["51 va 52 — jumla toʻldirish",
                     "53 — grafik tavsifi",
                     "54 — insho"],
              verdict="54-savol — yozish boʻlimining yarmi",
              title="쓰기 bali qanday taqsimlanadi",
              dur=9.6,
              note="Nega bu xato qimmat: bitta savol yozish boʻlimining "
                   "yarmini koʻtarib turibdi."),

        correct("중요해요", "중요하다",
                because="Insho yozma uslubda yoziladi.",
                lead="독서는 __",
                note="Almashadigan narsa soʻz emas — soʻzning oxiri."),

        versus({"name": "GAPIRISH — 해요체",
                "qty": KQ % "해요",
                "price": K % "독서는 중요해요",
                "tag": "suhbat va xabar"},
               {"name": "YOZISH — 문어체",
                "qty": KQ % "하다",
                "price": K % "독서는 중요하다",
                "tag": "insho va maqola"},
               title="Bitta fikr, ikkita uslub",
               dur=12.0,
               note="Chap ustun — odam bilan gaplashish. Oʻng ustun — "
                    "imtihon varagʻi. Oʻrtasi yoʻq."),

        echo("중요하다", gloss="muhim — yozma shakli",
             note="JIM sahna. Insho tilining oʻzi."),

        pairs([("좋아요", "좋다"),
               ("있어요", "있다"),
               ("갑니다", "간다"),
               ("생각해요", "생각한다")],
              head="Gapirish shakli → insho shakli",
              tail="Oxirgi qoʻshimcha almashadi, soʻz emas",
              note="Toʻrtta juft: sifat -다 oladi, feʼl -ㄴ다 oladi."),

        echo("생각한다", gloss="oʻylayman — yozma shakl",
             note="JIM sahna. Feʼlning insho shakli — jadvalning oxirgi "
                  "qatori."),

        rule("Insho oxirigacha bitta uslubda yoziladi",
             strip=K % "해요" + " → suhbat   ·   " + K % "-다" + " → insho",
             meaning="Bu xato bilim yetishmasligidan emas, odatdan keladi: "
                     "darslikda ham, serialda ham gapirish uslubi eshitiladi. "
                     "Insho esa yozma uslubni talab qiladi — boshidan oxirigacha.",
             dur=10.0),

        ask("«공부해요» inshoda qanday yoziladi?",
            dur=7.0,
            note="Javobni aytmang. Jadval qoidani berdi, bu soʻzni bermadi."),

        practice("TOPIK · 쓰기 54",
                 sub="Insho: jumla yodlash metodi", dur=5.4,
                 note="Powertyda 54-savolning oʻz darsi bor."),

        outro(line2="koreys tili · TOPIK"),
    ],
)

narrate(VIDEO, [
    "Bekzod TOPIK inshosini shunday boshladi: *독서는 중요해요*. "
    "|| Grammatikada xato yoʻq. Baho esa tushdi.",

    "Bu — ikki yillik darslikning tili. | Suhbatning tili.",

    "Oʻqituvchi esa xabar oʻqiyotgandek boʻldi. Insho emas.",

    "Ellik toʻrtinchi savol ellik ball, yozish boʻlimi esa yuz ball. "
    "|| Bitta savol — boʻlimning yarmi.",

    "Almashadigan narsa soʻz emas. | Soʻzning oxiri. "
    "|| *중요해요* emas, *중요하다*.",

    "*독서는 중요해요* — buni doʻstingizga aytasiz. "
    "| *독서는 중요하다* — buni imtihon varagʻiga yozasiz.",

    None,   # echo(중요하다) — jim sahna, koreyscha ovoz

    "Qoida oddiy: faqat soʻzning oxiri almashadi. "
    "|| *좋아요* — *좋다*. *생각해요* — *생각한다*.",

    None,   # echo(생각한다) — jim sahna, koreyscha ovoz

    "Bu xato bilimdan emas, odatdan keladi. || Darslik ham, serial ham "
    "gapirish uslubida. Insho esa yozma uslubni soʻraydi.",

    "Endi oʻzingiz oʻylang. *공부해요* inshoda qanday yoziladi? "
    "|| Izohda kutamiz.",

    "Ellik toʻrtinchi savolning oʻz darsi Powertyda: Topik, yozish. "
    "| Havola profilda.",

    None,   # outro — jim
])
