# -*- coding: utf-8 -*-
"""KO-35 — «Bu shoʻrva emas»  ·  TUTILGAN XATO  ·  TOPIK 07

Manba: examprep → TOPIK → Oʻqish — 관용 표현 1-2 (21–22-savollar, tana
aʼzolari iboralari). Iboralar va ularning maʼnosi oʻsha darslardan olingan:
발이 넓다 = tanish-bilishi koʻp, 입이 무겁다 = ogʻzi mahkam,
미역국을 먹다 = imtihondan yiqilmoq, 눈이 높다 = didi baland.

TOPIK filmlarining yettinchisi, va xato TURI yana almashtirildi (SERIES.md):
KO-13 registr, KO-14 soat, KO-15 mexanik sirpanish, KO-22 koʻz odati,
KO-26 grafik, KO-33 usulning yoʻqligi. Bu — **soʻzma-soʻz tarjima**: pupil
har bir soʻzni biladi va aynan shuning uchun adashadi.

Muqova imtihonga eng yaqin iborani oladi: 미역국을 먹다. Dengiz karami
sirpanchiq — shuning uchun imtihon oldidan uni ichmaslik odati bor. Bu
xalq odati, film uni «deyishadi» deb aytadi, ilmiy fakt sifatida emas.

⛔ Filmda TOPIK haqida birgina raqam bor — «21-savol», va u saytning oʻz
darsidan (21–22-savollar). Boshqa son yoʻq.
⚠️ 발이 → «pari» (oʻzbekcha «pari»): ovozda ibora har doim toʻliq aytiladi,
yolgʻiz 발이 emas, shuning uchun toʻqnashuv sezilmaydi.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, word, echo, pairs, check,
                    rule, ask, practice, outro)

VIDEO = Video(
    slug="ko35",
    lesson="TOPIK 읽기",
    title="Bu shoʻrva emas",
    story="examprep TOPIK — 관용 표현",
    subject="korean",
    scenes=[
        cover("미역국을 먹었어요", "Bu shoʻrva emas",
              kicker="Tutilgan xato", ko="한국어",
              track="TOPIK", n=7, badge="big",
              context="Imtihondan keyin doʻstingiz yozdi:", size=124,
              strike=False,
              note="MUQOVA: gʻalati narsa — imtihondan keyin shoʻrva haqida "
                   "xabar. Vaʼda uch soʻz."),

        says("Zilola", [("미역국을 먹었어요", "expr"),
                        ("«Shoʻrva ichibdi — mazza qilibdi!»", "lbl")],
             mood="smile", dur=6.2,
             note="Har bir soʻz toʻgʻri tarjima qilingan — xato shunda."),

        consequence("Zilola",
                    "Aslida doʻsti imtihondan yiqilgan edi.",
                    mood="shock", close=True, dur=6.8,
                    note="Yaqin plan. Zarar — bilmaslik emas, soʻzma-soʻz "
                         "oʻqish."),

        word("미역국", gloss="dengiz karami shoʻrvasi",
             head="Nega aynan shu shoʻrva?", dur=7.0,
             note="Sirpanchiq — imtihondan «sirpanib yiqilish». Xalq odati."),

        echo("미역국", gloss="dengiz karami shoʻrvasi",
             note="JIM sahna. Uch boʻgʻin."),

        pairs([("발이 넓다", "«oyogʻi keng» → tanish-bilishi koʻp"),
               ("입이 무겁다", "«ogʻzi ogʻir» → ogʻzi mahkam"),
               ("미역국을 먹다", "«shoʻrva yemoq» → imtihondan yiqilmoq")],
              head="TOPIK oʻqish, 21-savol: iboralar",
              tail="Soʻzma-soʻz tarjima — tuzoq.",
              dur=12.5,
              note="Chap tomonda soʻzlar, oʻng tomonda maʼno. Ular hech "
                   "qachon bir xil emas."),

        check("그는 ( ) 어디를 가도 아는 사람이 있다",
              parts=["1. Gap nimani talab qiladi? — «tanishi koʻp»",
                     "2. Shu maʼnoli ibora: 발이 넓어서",
                     "3. 손이 커서 · 눈이 높아서 — maʼnosi sigʻmaydi"],
              verdict="Avval maʼno, keyin ibora.",
              title="Usul: maʼno boʻshligʻi",
              dur=11.0,
              note="Darsdagi usul: iborani bilmasangiz ham gap mantigʻi "
                   "talabni aytib turadi."),

        echo("발이 넓다", gloss="tanish-bilishi koʻp",
             note="JIM sahna, ikkinchisi."),

        rule("Iborani soʻzma-soʻz emas, maʼno bilan oʻqing",
             strip="미역국을 먹다 = imtihondan yiqilmoq",
             meaning="21-savolda variantlar — toʻrtta ibora. Avval gap qanday "
                     "maʼno talab qilishini toping, keyin shu maʼnoli iborani "
                     "tanlang. Iborani tarjima roʻyxati bilan emas, obraz va "
                     "bitta misol gap bilan yodlang.",
             dur=11.0),

        ask("눈이 높다 — soʻzma-soʻz «koʻzi baland». "
            "Bu qanday odam?",
            dur=7.0,
            note="Javobni aytmang (didi baland). Videoda yoʻq, darsda bor."),

        practice("TOPIK · Oʻqish · Iboralar",
                 sub="powerty.uz → Examprep → TOPIK → Oʻqish",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreys doʻstingiz imtihondan keyin yozdi: 미역국을 먹었어요. "
    "|| Gap shoʻrva haqida emas.",

    "Zilola soʻzma-soʻz tarjima qildi: shoʻrva ichibdi. | Mazza qilibdi-da.",

    "Aslida doʻsti imtihondan yiqilgan edi. || Bu — ibora.",

    "Dengiz karami sirpanchiq. | Shuning uchun imtihon oldidan uni "
    "ichishmaydi — sirpanib yiqilasan, deyishadi.",

    None,   # echo(미역국)

    "TOPIK oʻqishning 21-savoli aynan shunday iboralar haqida. "
    "| 발이 넓다 — oyogʻi keng emas, tanishi koʻp. "
    "| 입이 무겁다 — ogʻzi mahkam.",

    "Usul: avval boʻsh joyga qanday maʼno kerakligini toping. "
    "| Bu gapda — qayerga borsa ham tanishi bor. || Demak, 발이 넓어서.",

    None,   # echo(발이 넓다)

    "Iborani soʻzma-soʻz emas, maʼno bilan oʻqing. "
    "|| Avval maʼno, keyin ibora.",

    "Endi oʻzingiz oʻylang. 눈이 높다 — koʻzi baland. "
    "| Bu qanday odam? || Izohda kutamiz.",

    "Tana aʼzolari iboralari — Powertyda, Examprep, TOPIK oʻqish boʻlimida.",

    None,   # outro
])
