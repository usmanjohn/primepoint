# -*- coding: utf-8 -*-
"""KO-9 — Bir xil tugaydi, boshqacha tuslanadi  ·  TUTILGAN XATO

Manba: Prime Korean PK-32 (Notoʻgʻri feʼllar 1: ㅂ, ㄷ, 으 tuslanishi).

The third shape in the band: not an Uzbek collision (ko07) and not a social
cost (ko08) but a mechanism inside Korean itself, like ko06's two number
systems. Nothing in the pupil's own language causes this one.

The mistake is the most predictable in the language: 춥다 takes 어요 like
everything else, so 춥어요. It comes out 추워요 -- the final ㅂ leaves and 우
arrives in its place.

What makes it worth a film rather than a footnote is the second half: 입다 ends
in exactly the same letter and is perfectly regular (입어요). So the spelling
does NOT tell you which group a word is in, and that is the honest lesson --
which is why the `versus` puts a regular verb beside an irregular one and the
tags talk about the LETTER, not the meaning.

⚠️ A lone jamo (ㅂ) is refused by `cli.py script`, and rightly -- a bare
consonant has no vowel to read. So it lives on screen only, and every narration
line says "b harfi" in Uzbek instead. That constraint shaped the whole script.
"""

from spec import Video, narrate
from scenes import cover, says, correct, pairs, versus, echo, rule, ask, practice, outro

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:80px">%s</span>'

VIDEO = Video(
    slug="ko09",
    lesson="PK-32",
    title="Bir xil tugaydi, boshqacha tuslanadi",
    story="Prime Korean PK-32",
    subject="korean",
    scenes=[
        cover("춥어요", "Tuslanishi xato",
              kicker="Tutilgan xato",
              context="«Sovuq» demoqchi edi:",
              note="MUQOVA: bu shakl koreys tilida umuman yoʻq — shuning "
                   "uchun butun soʻz chizib tashlanadi. Eng koʻp "
                   "qilinadigan xato, chunki eng mantiqli xato."),

        says("Afsona", [("«Sovuq» demoqchi edim:", "lbl"),
                        ("춥어요", "expr ko")],
             mood="smile",
             note="Qoidani toʻgʻri qoʻlladi: 춥다 ga 어요 qoʻshdi. "
                  "Natija esa mavjud boʻlmagan soʻz."),

        correct("춥어요", "추워요",
                because="Oxirgi undosh ketadi, oʻrniga 우 keladi",
                lead="춥다 + 어요",
                note="Chizib tashlangani — hech qachon eshitilmaydigan "
                     "shakl, oʻngdagi esa kundalik soʻz."),

        pairs([("춥다 → 추워요", "sovuq"),
               ("덥다 → 더워요", "issiq"),
               ("맵다 → 매워요", "achchiq")],
              head="Shu guruhdagi sifatlar",
              tail="Hammasida bir xil oʻzgarish",
              note="Uchtasi ham kundalik soʻz — ob-havo va ovqat. "
                   "Pupil ularni birinchi haftada uchratadi."),

        echo("더워요", gloss="issiq", head="Eshiting va takrorlang",
             note="JIM sahna. Guruhning ikkinchi soʻzi — oʻzgarish "
                  "quloqda takrorlanadi."),

        versus({"name": "muntazam",
                "qty": KQ % "입다",
                "price": K % "입어요",
                "tag": "undosh qoladi"},
               {"name": "notoʻgʻri",
                "qty": KQ % "춥다",
                "price": K % "추워요",
                "tag": "undosh 우 boʻladi"},
               title="Ikkalasi ham bir xil harf bilan tugaydi",
               dur=12.5,
               note="Filmning halol qismi: yozilishiga qarab guruhni "
                    "aniqlab boʻlmaydi. Shuning uchun teglar maʼno emas, "
                    "HARF haqida gapiradi."),

        echo("추워요", gloss="sovuq",
             note="JIM sahna. Filmni boshlagan soʻzning toʻgʻri shakli."),

        rule("Yozilishi guruhni aytmaydi — soʻz bilan birga yodlanadi",
             strip=K % "입다" + " → 입어요   ·   " + K % "춥다" + " → 추워요",
             meaning="Ikkala soʻz ham bir xil harf bilan tugaydi, ammo "
                     "bittasi oʻzgaradi, ikkinchisi yoʻq. Shuning uchun "
                     "koreyslar bu sifatlarni tuslangan shakli bilan "
                     "birga oʻrgatadi.",
             dur=9.6),

        ask("«춥다» — sovuq. Unda «추운 날» nima degani, "
            "va oʻzgarish bu yerda ham ishladimi?",
            dur=7.8,
            note="Javobni aytmang. Xuddi shu oʻzgarish boshqa "
                 "qoʻshimcha oldida ham takrorlanadi."),

        practice("Prime Korean · PK-32",
                 sub="Notoʻgʻri feʼllarning tuslanishi", dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Afsona «sovuq» demoqchi edi va *춥어요* dedi. || Qoidani toʻgʻri "
    "qoʻlladi. Natija esa koreys tilida yoʻq soʻz.",

    "U *춥다* ga oddiy qoʻshimchani qoʻshdi. | Har qanday oʻquvchi shunday "
    "qiladi — shuning uchun bu eng koʻp qilinadigan xato.",

    "Toʻgʻrisi — *추워요*. || Oxirgi undosh ketadi, oʻrniga *우* keladi.",

    "Shu guruhda kundalik soʻzlar bor. *춥다* sovuq boʻlsa *추워요*. "
    "| *덥다* issiq boʻlsa *더워요*. | *맵다* achchiq boʻlsa *매워요*. "
    "|| Uchtasida ham bir xil oʻzgarish.",

    None,   # echo(더워요) — jim sahna, koreyscha ovoz

    "Ammo diqqat qiling. *입다* — kiymoq. U ham xuddi shu harf bilan "
    "tugaydi. | Lekin uning tuslanishi *입어요* — undosh joyida qoladi. "
    "|| Yaʼni soʻzning yozilishi uni qaysi guruhda ekanini aytmaydi.",

    None,   # echo(추워요) — jim sahna, koreyscha ovoz

    "Shuning uchun bu sifatlarni tuslangan shakli bilan birga yodlang. "
    "|| Koreyslar ham darslikda shunday beradi: soʻz va uning oʻzgargan "
    "shakli yonma-yon.",

    "Endi oʻzingiz oʻylang. *춥다* sovuq boʻlsa, *추운 날* nima degani? "
    "|| Va oʻzgarish bu yerda ham ishladimi? Izohda kutamiz.",

    "Notoʻgʻri feʼllar Powertyda: Praym Korean, oʻttiz ikkinchi dars.",

    None,   # outro — jim
])
