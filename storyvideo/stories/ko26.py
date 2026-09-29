# -*- coding: utf-8 -*-
"""KO-26 — «Grafik gapiradi, siz emas»  ·  TUTILGAN XATO  ·  TOPIK

Manba: examprep TOPIK — 쓰기, «Writing 53: Grafik va jadvalni tasvirlash».
Ishlangan misol ham oʻsha darsniki: 인주시, 1 000 nafar katta yoshli,
여가 활동 — 운동 45%, 여행 30%, 독서 25%. 쓰기 bali taqsimoti ko13 dagidek:
10 + 10 + 30 + 50 = 100, demak 53-savol 30 ball.

The fifth TOPIK film, and it keeps rotating the KIND of mistake. ko13 was a
register, ko14 a clock, ko15 a mechanical slip, ko22 a study habit. This one
is the pupil answering a DIFFERENT QUESTION from the one on the paper: 53 asks
for what the chart says, and they write what they think about it. Every
sentence is good Korean and none of it can be marked, because the marker is
looking for data and there is an opinion in its place.

Worse, it is expensive twice over: an opinion does not score AND it eats the
200-300 character budget the description needed.

The `check` beat is the site's own arithmetic -- 45 + 30 + 25 = 100 -- so
`lint` recomputes it and the film cannot disagree with the lesson it points
at. The three percentages are the lesson's worked example, not invented ones.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, check, correct, pairs, echo,
                    rule, ask, practice, outro)

K = '<span class="ko">%s</span>'

VIDEO = Video(
    slug="ko26",
    lesson="TOPIK 쓰기 53",
    title="Grafik gapiradi, siz emas",
    story="examprep TOPIK — 쓰기 53",
    subject="korean",
    scenes=[
        cover('<span class="strike">제 생각에는</span>', "Bu yerda fikr soʻralmaydi",
              kicker="Tutilgan xato · TOPIK",
              ko="한국어",
              context="쓰기 53 — grafik tavsifi, 30 ball:",
              strike=False,
              note="MUQOVA: notoʻgʻri narsa — inshoga yaraydigan, lekin "
                   "53-savolga yaramaydigan ibora, ustidan chiziq."),

        says("Afsona", [("Grafikni shunday boshladi:", "lbl"),
                        ("제 생각에는 운동이 좋습니다", "expr ko")],
             mood="smile",
             note="Grammatikada xato yoʻq. Faqat bu — 54-savolning tili, "
                  "53-savolning varagʻida."),

        consequence("Nodira opa", "Buni grafik aytmagan.",
                    mood="cross", close=True,
                    note="Xatoning bahosi: baholanadigan narsa yoʻq. "
                         "Va belgilar soni behuda sarflandi."),

        check("45 + 30 + 25 = 100",
              parts=["운동 — 45%",
                     "여행 — 30%",
                     "독서 — 25%"],
              verdict="Yozadigan hamma narsa shu yerda",
              title="Inju shahri · 1000 kishi soʻralgan",
              dur=10.0,
              note="Darsning oʻz misoli. Uchta son — va ular yigʻilib "
                   "yuz foiz chiqadi, demak grafik toʻliq. `lint` buni "
                   "qayta hisoblaydi."),

        correct("제 생각에는", "조사 결과",
                because="53 — fikr emas, maʼlumot.",
                shake=True,
                note="Almashadigan narsa bitta ibora. YANGI: xato "
                     "qimirlaydi, toʻgʻrisi tepadan tushib qotadi."),

        echo("가장 많았다", gloss="eng koʻp boʻldi",
             note="JIM sahna. 53-savolning eng kerakli iborasi."),

        # Glosses kept SHORT on purpose: a two-line gloss pushes the builder's
        # own «=» out of the row (seen on the first contact sheet). The Korean
        # is the exam's exact wording and must not be trimmed, so the Uzbek is.
        pairs([("조사 결과", "natijaga koʻra"),
               ("가장 높게 나타났다", "eng yuqori"),
               ("뒤를 이었다", "keyin turdi"),
               ("가장 낮게 나타났다", "eng past")],
              head="53-savolning oʻz iboralari",
              tail="Toʻrtta ibora — butun javobning skeleti",
              note="Darsning template'laridan. Bu toʻrttasi bilan har "
                   "qanday grafikni tasvirlash mumkin."),

        echo("뒤를 이었다", gloss="undan keyin turdi",
             note="JIM sahna. Ikkinchi va uchinchi oʻrin uchun."),

        rule("53 da grafik gapiradi, siz emas",
             strip=K % "제 생각에는" + " → 54-savol   ·   "
                   + K % "조사 결과" + " → 53-savol",
             meaning="Ellik uchinchi savol tayyor maʼlumotni soʻz bilan "
                     "bayon qilishni soʻraydi, xolos. Oʻz fikringiz uchun "
                     "ellik toʻrtinchi savol bor — va u ellik ball.",
             dur=10.5),

        ask("53 — ikki yuzdan uch yuz belgigacha. Sizning javobingiz "
            "necha jumla boʻladi?",
            dur=7.6,
            note="Javobni aytmang. Film iboralarni berdi, hajm rejasini "
                 "bermadi — buni oʻzi sanab koʻrsin."),

        practice("TOPIK · 쓰기 53",
                 sub="Grafik va jadvalni tasvirlash", dur=5.4,
                 note="Powertyda 53-savolning template'lari va namunalari bor."),

        outro(line2="koreys tili · TOPIK"),
    ],
)

narrate(VIDEO, [
    "TOPIK yozish boʻlimida ellik uchinchi savol grafik beradi. "
    "|| Va koʻpchilik unga oʻz fikrini yozadi.",

    "Afsona shunday boshladi: *제 생각에는 운동이 좋습니다*.",

    "Oʻqituvchi bitta narsani aytdi: buni grafik aytmagan.",

    "Grafikda hammasi turibdi: sport qirq besh foiz, sayohat oʻttiz, "
    "kitob oʻqish yigirma besh. || Yigʻindisi — yuz foiz.",

    "Almashadigan narsa bitta ibora. | *제 생각에는* emas, *조사 결과*.",

    None,   # echo(가장 많았다) — jim sahna, koreyscha ovoz

    "Va butun javob toʻrtta iboraga sigʻadi: natijaga koʻra, eng yuqori "
    "chiqdi, undan keyin turdi, eng past chiqdi.",

    None,   # echo(뒤를 이었다) — jim sahna, koreyscha ovoz

    "Fikringiz uchun ellik toʻrtinchi savol bor. | Va u ellik ball. "
    "|| Ellik uchinchida esa grafik gapiradi.",

    "Endi oʻzingiz oʻylang. Javob ikki yuzdan uch yuz belgigacha. "
    "|| Bu necha jumla boʻladi? Izohda kutamiz.",

    "Ellik uchinchi savolning oʻz darsi Powertyda: Ekzamprep, Topik, "
    "yozish. | Havola profilda.",

    None,   # outro — jim
])
