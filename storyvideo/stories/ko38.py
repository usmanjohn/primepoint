# -*- coding: utf-8 -*-
"""KO-38 — «Soyabonni olmang»  ·  TUTILGAN XATO  ·  GRAMMATIKA 04

Manba: Prime Korean PK-35 (아/어서 — «ikkinchi taqiq: buyruq va taklif
kelmaydi», misoli 배가 아파서 병원에 가세요 ✗) va PK-48 ((으)니까 — «dan keyin
buyruq, taklif, maslahat — hammasi mumkin: 비가 오니까 우산을 가져가세요»).
Ikkala misol ham darslarning oʻzidan.

Grammatika yoʻlining toʻrtinchisi. Kasallik turi — **oʻzbekcha toʻqnashuv**
(SERIES.md §3): oʻzbekchada sabab qoʻshimchasi bitta («…gani uchun»), u
buyruqni ham, xabarni ham koʻtaradi. Koreyschada ikkita, va ularni gapning
KEYINGI qismi ajratadi. Pupilning oʻz tili toʻgʻri ishlayapti — xato shunda.

2026-10-08 dan ovoz ElevenLabs (eleven_v4) — u [laughs] kabi audio teglarni
oʻynaydi, shuning uchun reaksiya sahnasida bitta kulgi bor. Foydalanuvchining
iltimosi: kulgili soʻzlar («oshqovoqchalar») va koreyscha hayqiriq (아이고).

⚠️ 와서 + buyruq — notoʻgʻri birikma. Ekranda va ovozda bor (pupil xatoni
eshitishi kerak), lekin `echo` ga faqat toʻgʻri shakllar beriladi (§5).
"""

from spec import Video, narrate

# (으)니까 must never break after the bracket -- the sheet showed «(으) / 니까».
NK = '<span style="white-space:nowrap">(으)니까</span>'
from scenes import (cover, says, consequence, correct, pairs, check, echo,
                    rule, ask, practice, outro)

VIDEO = Video(
    slug="ko38",
    lesson="PK-48",
    title="Soyabonni olmang",
    story="Prime Korean PK-35 · PK-48 — 아/어서 va (으)니까",
    subject="korean",
    scenes=[
        cover('<span class="strike">와서</span> 가져가세요',
              "Sabab bor, buyruq yoʻq",
              kicker="Tutilgan xato", ko="한국어",
              track="Grammatika", n=4, badge="big",
              context="«Yomgʻir yogʻyapti — soyabon oling»:",
              strike=False, size=124,
              note="MUQOVA: qizil chiziq faqat 와서 dan oʻtadi — gapning "
                   "qolgani toʻgʻri."),

        says("Jasur", [("Koreys doʻstiga yozdi:", "lbl"),
                       ("비가 와서 우산을 가져가세요", "expr ko")],
             mood="smile", dur=6.4,
             note="Oʻzbekcha tafakkur: «yogʻgani uchun» = 와서. "
                  "Har bir soʻz toʻgʻri."),

        consequence("Jasur",
                    "Doʻsti kuldi: «아이고, gap buzuq!»",
                    mood="shock", close=True, dur=6.4,
                    note="Yaqin plan. Maʼno tushunarli — lekin bu koreyscha "
                         "emas."),

        correct("와서", "오니까",
                because="keyin buyruq bor — demak " + NK,
                lead="Sababdan keyin buyruq kelsa:", shake=True, dur=8.5,
                note="Toʻgʻri gap PK-48 ning oʻzidan."),

        echo("오니까", gloss="yogʻyapti, shuning uchun",
             note="JIM sahna. Toʻgʻri shakl, uch boʻgʻin."),

        pairs([("비가 와서 늦었어요", "kechikdim — xabar ✓"),
               ("비가 와서 가져가세요", "buyruq ✗"),
               ("비가 오니까 가져가세요", "buyruq ✓")],
              head="Gapning KEYINGI qismiga qarang",
              tail="Buyruq yoki taklif bor — faqat " + NK + ".",
              dur=13.0,
              note="Filmning dalili: birinchi ikki qator bir xil boshlanadi, "
                   "farqni oxiri hal qiladi."),

        pairs([("Oʻzbekcha", "«…gani uchun» — bitta"),
               ("Koreyscha", "아/어서 · (으)니까 — ikkita"),
               ("Ajratadi", "keyin buyruq bormi?")],
              head="Nega oʻzbek adashadi?",
              tail="Oʻz tilingiz toʻgʻri ishlayapti — shunda tuzoq.",
              dur=11.5,
              note="Oʻzbekcha toʻqnashuv — SERIES §3 ning birinchi turi."),

        check("배가 아파서 병원에 가세요",
              parts=["Oxirida buyruq bormi? — 가세요, bor",
                     "Demak 아파서 boʻlmaydi",
                     "배가 아프니까 병원에 가세요"],
              verdict="Qoida ishladi.",
              title="Tekshiramiz",
              dur=10.0,
              note="Misol PK-35 ning «Nega notoʻgʻri?» savolidan."),

        echo("아프니까", gloss="ogʻrigani uchun",
             note="JIM sahna, ikkinchisi. Toʻrt boʻgʻin."),

        rule("Sababdan keyin buyruq — faqat " + NK,
             strip="비가 와서 늦었어요 ✓   ·   비가 오니까 가져가세요 ✓",
             meaning="아/어서 — sababni shunchaki aytadi, undan keyin buyruq "
                     "ham, taklif ham kelmaydi. (으)니까 dan keyin esa "
                     "hammasi mumkin. Tarjimaga emas, bitta savolga "
                     "tayaning: keyingi qismda buyruq bormi?",
             dur=11.0),

        ask("피곤해서 · 피곤하니까 — «charchagan boʻlsangiz, "
            "erta yoting». Qaysi biri?",
            dur=7.4,
            note="Javobni aytmang (피곤하니까 — oxirida buyruq bor). "
                 "Bu feʼl videoda tuslanmagan."),

        practice("Prime Korean · PK-48",
                 sub="powerty.uz → Darsliklar → Prime Korean",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Oʻzbekchada bu gap toʻgʻri: yomgʻir yogʻgani uchun soyabon oling. "
    "|| Koreyschada esa — yoʻq.",

    "Jasur koreys doʻstiga yozdi: 비가 와서 우산을 가져가세요. "
    "| Har bir soʻz toʻgʻri.",

    "Doʻsti kulib yubordi: [laughs] 아이고! "
    "|| Maʼno tushunarli, lekin bu koreyscha emas.",

    "Sababdan keyin buyruq kelsa, 와서 ishlamaydi. "
    "|| Toʻgʻrisi: 비가 오니까.",

    None,   # echo(오니까)

    "Shunchaki xabar boʻlsa, 와서 joyida: kechikdim. "
    "|| Buyruq boʻlsa — faqat 오니까.",

    "Oʻzbekchada sabab qoʻshimchasi bitta: gani uchun. "
    "| Koreyschada — ikkita. || Ularni gapning oxiri ajratadi.",

    "Tekshiramiz: qorningiz ogʻriyapti, shifokorga boring. "
    "| Oxirida buyruq bor. || Demak 아프니까.",

    None,   # echo(아프니까)

    "Qoida bitta savol: keyingi qismda buyruq bormi? "
    "|| Bor boʻlsa — faqat 니까.",

    "Endi oʻzingiz, oshqovoqchalar: charchagan boʻlsangiz, erta yoting. "
    "| Qaysi biri kerak? || Izohda kutamiz.",

    "Prime Korean — Powertyda, qirq sakkizinchi dars.",

    None,   # outro
])
