# -*- coding: utf-8 -*-
"""KO-14 — «Oxirgi oʻnta savol»  ·  TUTILGAN XATO  ·  TOPIK

Manba: examprep TOPIK — strategiya darsi «TOPIK II — Kirish (1-qism):
tuzilma, vaqt, ball va darajalar». Har bir raqam oʻsha darsdan olingan:
읽기 = 50 savol / 70 daqiqa, har savol 2 ball, 4급 = 150 ball.

The second TOPIK film, and deliberately not another grammar mistake: this one
is lost with perfect Korean. A candidate who reads every text properly from
question 1 arrives at question 40 with five minutes left, and the ten
questions they never saw are worth twenty points -- which is wider than the
gap between one level and the next at the boundary.

So the mechanism scene is a DIVISION, not a conjugation: 70 ÷ 50 = 1.4
minutes a question. The film's argument is that the exam is a clock problem
wearing a reading problem's clothes, and the picture proves it by dividing.

⚠️ The two blank-answer facts are separate and both true, and the film keeps
them apart: a wrong answer costs nothing beyond the mark it did not earn
(there is no negative marking), and a blank box is therefore strictly worse
than a guess. Nothing here promises what a guess is WORTH -- that would be
inventing a probability the exam does not publish.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, check, correct, pairs, echo,
                    versus, rule, ask, practice, outro)

K = '<span class="ko">%s</span>'

VIDEO = Video(
    slug="ko14",
    lesson="TOPIK 읽기",
    title="Oxirgi oʻnta savol",
    story="examprep TOPIK — strategiya",
    subject="korean",
    scenes=[
        cover("40 / 50", "20 ball behuda ketdi",
              kicker="Tutilgan xato · TOPIK",
              context="읽기 — 50 savol, 70 daqiqa. Belgilangani:",
              note="MUQOVA: butun natija notoʻgʻri, shuning uchun chiziq "
                   "butun sondan oʻtadi. Vaʼda — yoʻqotilgan ball, mavzu "
                   "nomi emas."),

        says("Sardor", [("Oʻqish boʻlimi, 65-daqiqa:", "lbl"),
                        ("40 / 50", "expr")],
             mood="oh",
             note="Koreyschasi joyida. Yetmagani — vaqt."),

        consequence("Sardor", "Oxirgi oʻnta savolni koʻrmadim ham.",
                    mood="sad",
                    note="Xatoning bahosi: javob varagʻining oxiri boʻsh "
                         "qoldi. Bu — bilim emas, taqsimot masalasi."),

        check("70 ÷ 50 = 1,4",
              parts=["Yaʼni har bir savolga 1 daqiqa 24 soniya",
                     "Birinchi matnlar qisqa, oxirgilari uzun"],
              verdict="Vaqtni savol emas, matn yeydi",
              title="Oʻqish boʻlimining soati",
              dur=9.6,
              note="Filmning mexanizmi — boʻlish amali. Imtihon oʻqish "
                   "masalasi kiyimidagi soat masalasi."),

        correct("40 / 50", "50 / 50",
                because="Reja soat bilan tuziladi, savol bilan emas.",
                lead="Oʻqish boʻlimi",
                note="Tuzatish — bilimda emas, rejada."),

        pairs([("20-daqiqa", "1–20 savol"),
               ("40-daqiqa", "21–35 savol"),
               ("60-daqiqa", "36–45 savol"),
               ("70-daqiqa", "46–50 savol")],
              head="Soat bilan kelishuv",
              tail="Nazorat nuqtasida orqada boʻlsangiz — tezlashing",
              note="Savollar oxiriga borib uzayadi, shuning uchun "
                   "taqsimot teng emas: boshida 20 ta, oxirida 5 ta."),

        echo("시간이 없다", gloss="vaqt yoʻq",
             head="Imtihondagi eng qimmat gap",
             note="JIM sahna. Filmning mavzusi bitta gapda."),

        versus({"name": "10 ta savol boʻsh",
                "qty": "148",
                "price": K % "3급",
                "tag": "chegaradan ikki ball past"},
               {"name": "Hammasiga belgi",
                "qty": "168",
                "price": K % "4급",
                "tag": "koʻp universitet talabi"},
               title="Yigirma ball qayerda turadi",
               verdict="150 — 4급 chegarasi",
               dur=12.5,
               note="Oʻnta savol — yigirma ball. Daraja chegarasi aynan "
                    "shu kenglikda yotadi."),

        echo("다 풀었다", gloss="hammasini yechdim",
             note="JIM sahna. Yuqoridagi gapning teskarisi."),

        rule("Boʻsh katak — aniq nol",
             strip="Toʻgʻri javob → 2 ball   ·   Notoʻgʻri javob → 0   ·   "
                   "Boʻsh katak → 0",
             meaning="TOPIKda notoʻgʻri javob uchun ball ayirilmaydi. Demak "
                     "boʻsh katak taxmindan hech qachon yaxshi emas — oxirgi "
                     "daqiqalarda har bir qatorni toʻldiring.",
             dur=10.0),

        ask("Vaqt tugashiga 5 daqiqa qoldi, 8 ta savol boʻsh. "
            "Nimadan boshlaysiz?",
            dur=7.2,
            note="Javobni aytmang. Filmda reja bor, bu vaziyat yoʻq."),

        practice("TOPIK · Strategiya",
                 sub="Tuzilma, vaqt, ball va darajalar", dur=5.4,
                 note="Powertydagi kirish darsi — hamma raqam oʻsha yerda."),

        outro(line2="koreys tili · TOPIK"),
    ],
)

narrate(VIDEO, [
    "Sardorning koreyschasi joyida edi. || Oʻqish boʻlimi tugaganda esa "
    "javob varagʻida qirqta belgi bor edi.",

    "Ellik savoldan qirqtasi. | Oxirgi oʻntasini u koʻrmadi ham.",

    "Bu bilim masalasi emas. || Taqsimot masalasi.",

    "Sanaymiz. Yetmish daqiqa, ellikta savol. "
    "|| Har bir savolga bir daqiqa yigirma toʻrt soniya.",

    "Demak reja soat bilan tuziladi, savol bilan emas.",

    "Shunday boʻlinadi: yigirmanchi daqiqada yigirmanchi savolda boʻling. "
    "|| Qirqinchi daqiqada — oʻttiz beshinchi savolda.",

    None,   # echo(시간이 없다) — jim sahna, koreyscha ovoz

    "Endi bahosi. Oʻnta savol — yigirma ball. "
    "|| Bir yuz qirq sakkiz ball uchinchi daraja, bir yuz oltmish sakkiz "
    "toʻrtinchi daraja.",

    None,   # echo(다 풀었다) — jim sahna, koreyscha ovoz

    "Va eng arzon ball shu yerda: notoʻgʻri javob uchun ball ayirilmaydi. "
    "|| Demak boʻsh katak taxmindan hech qachon yaxshi emas.",

    "Endi oʻzingiz oʻylang. Besh daqiqa qoldi, sakkizta savol boʻsh. "
    "|| Nimadan boshlaysiz? Izohda kutamiz.",

    "Imtihonning butun tuzilmasi Powertyda: Topik, strategiya. "
    "| Havola profilda.",

    None,   # outro — jim
])
