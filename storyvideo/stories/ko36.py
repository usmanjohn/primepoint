# -*- coding: utf-8 -*-
"""KO-36 — «Bitta boʻgʻin — uchta qoʻshimcha»  ·  BITTA SOʻZ

Manba: examprep VocabRoot 불(不), TOPIK track — «inkor: -siz, no-, be-»;
bankdagi soʻzlar: 불편 불안 불가능 부족하다.

The Uzbek angle is the whole film: Uzbek says «not» three ways — no-qulay,
be-baxt, imkon-siz — and Korean says it one way, always in front. So the
`pairs` scene is three Korean words built identically next to three Uzbek
words built three different ways.

Then the turn the bank itself plants: 부족하다 is in the 불 family but is
spelt 부. 不 is read 부 before ㄷ and ㅈ (부족 不足, 부동산 不動産, 부정 不正),
usually — 부실(不實) is the known exception before ㅅ, which is why the film
says «odatda» and never «har doim».

And the payoff: 부동산 = 不 + 動 + 産 = «harakatlanmaydigan mulk» — and Uzbek
says exactly that: koʻchmas mulk. Nobody taught either language the other's
word; the two calques arrived at the same place.

⚠️ 불 alone romanises to `pul` — the Uzbek word for money (style guide §4,
KO-23). The voice never says the bare syllable: it says «bu boʻgʻin», «inkor».
The family scene is narrated in Uzbek meanings for the same reason.
"""

from spec import Video, narrate
from scenes import (cover, build, word_family, echo, pairs, word, versus,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:88px">%s</span>'

VIDEO = Video(
    slug="ko36",
    lesson="Koreya olami",
    title="Bitta boʻgʻin — uchta qoʻshimcha",
    story="examprep VocabRoot 불(不)",
    subject="korean",
    scenes=[
        cover("불가능", "= imkon-siz",
              kicker="Bitta soʻz", ko="한국어",
              context="Koreyscha soʻz, oʻzbekcha qolip:",
              strike=False,
              note="MUQOVA: gʻalati narsa — koreys soʻzi oʻzbekcha "
                   "qoʻshimcha bilan teng. Vaʼda ikki soʻz."),

        build([("불", "inkor", True), ("가", "mumkin", False),
               ("능", "qodir", False)],
              "불가능", gloss="imkonsiz",
              head="Inkor + imkon",
              dur=8.5,
              note="Oltin plitka — bugungi ildiz."),

        word_family(
            "불",
            [("불편", "不便", "noqulay"),
             ("불안", "不安", "notinch, xavotir"),
             ("불행", "不幸", "baxtsizlik"),
             ("불가능", "不可能", "imkonsiz")],
            hanja="不", meaning="inkor — no-, be-, -siz", label="ta soʻz",
            cols=1, dur=11.0,
            note="Toʻrttasi ham 不 bilan yoziladi va har doim OLDINDA."),

        echo("불편해요", gloss="noqulay",
             note="JIM sahna. Kundalik soʻz — 불편해요."),

        pairs([("불 + 편", "no + qulay"),
               ("불 + 행", "be + baxt"),
               ("불 + 가능", "imkon + siz")],
              head="Koreysda bitta qolip, oʻzbekda — uchta",
              tail="Koreys inkori har doim oldinda.",
              dur=11.5,
              note="Filmning yuragi: chap ustun bir xil qurilgan, oʻng ustun "
                   "uch xil."),

        word("부족", gloss="yetishmaslik", hanja="不足",
             head="Endi bunga qarang", dur=7.0, dark=True,
             note="Burilish: bankning oʻzidagi soʻz, belgisi oʻsha — "
                  "lekin 부."),

        versus({"name": "ㄷ · ㅈ dan oldin",
                "qty": KQ % "부",
                "price": "부족 · 부동산",
                "tag": "t · ch dan oldin"},
               {"name": "qolgan joyda",
                "qty": KQ % "불",
                "price": "불편 · 불행",
                "tag": "qolgan hammasi"},
               title="Bitta belgi, ikki oʻqilish",
               verdict="不 — odatda ㄷ va ㅈ dan oldin 부",
               dur=11.5,
               note="«Odatda»: 부실(不實) — ㅅ dan oldingi istisno."),

        build([("부", "emas", True), ("동", "harakat", False),
               ("산", "mulk", False)],
              "부동산", gloss="koʻchmas mulk",
              head="Harakatlanmaydigan mulk",
              dur=9.0,
              note="Payoff: oʻzbekcha «koʻchmas mulk» — soʻzma-soʻz oʻsha."),

        echo("부동산", gloss="koʻchmas mulk",
             note="JIM sahna, ikkinchisi."),

        rule("Soʻz oldidagi 不 — inkor",
             strip=K % "불편" + " · " + K % "불행" + " · " + K % "불가능"
                   + "   ·   " + K % "부족" + " · " + K % "부동산",
             meaning="불 — inkor, va u har doim soʻzning oldida turadi. "
                     "Keyingi boʻgʻin ㄷ yoki ㅈ bilan boshlansa, odatda 부 "
                     "boʻlib yoziladi va oʻqiladi. Ildizni tanisangiz, "
                     "maʼnoni taxmin qilasiz — keyin tekshiring.",
             dur=10.5),

        ask("만족 — mamnunlik. "
            "Unda 불만족 nima degani?",
            dur=7.0,
            note="Javobni aytmang (norozilik, qoniqmaslik). Ovozda 불 "
                 "yolgʻiz aytilmaydi."),

        practice("TOPIK lugʻat · soʻz oilalari",
                 sub="powerty.uz → Examprep → Lugʻat → Soʻz oilalari",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreyschada bitta boʻgʻin bor, | u oʻzbekchadagi uchta qoʻshimchaning "
    "ishini qiladi.",

    "불가능. | Oldidagisi — inkor. | Qolgani — imkon. "
    "|| Yaʼni: imkonsiz.",

    "Oʻsha inkor boshqa soʻzlarni ham ochadi: | noqulay, notinch, "
    "baxtsizlik. || Va imkonsiz.",

    None,   # echo(불편해요)

    "Oʻzbekchada inkorning uch xil qolipi bor: no-, be- va -siz. "
    "|| Koreyschada — bitta, va u har doim oldinda.",

    "Endi bunga qarang: 부족 — yetishmaslik. "
    "|| Belgisi oʻsha, lekin oʻqilishi boshqa.",

    "Keyingi boʻgʻin t yoki ch tovushi bilan boshlansa, "
    "| bu inkor odatda pu deb oʻqiladi.",

    "Va eng chiroylisi: 부동산. | Inkor, harakat, mulk. "
    "|| Oʻzbekcha — koʻchmas mulk. Soʻzma-soʻz oʻsha.",

    None,   # echo(부동산)

    "Soʻz oldidagi bu boʻgʻin — inkor. "
    "|| Ildizni taniysiz — maʼnoni taxmin qilasiz.",

    "Endi oʻzingiz oʻylang. 만족 — mamnunlik. "
    "| Oldiga inkor qoʻyilsa-chi? || Izohda kutamiz.",

    "Ellik bitta ildizning hammasi Powertyda: Examprep, lugʻat, "
    "soʻz oilalari.",

    None,   # outro
])
