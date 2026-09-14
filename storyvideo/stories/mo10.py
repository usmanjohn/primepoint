# -*- coding: utf-8 -*-
"""MO-10 — «Gauss: 1 dan 100 gacha bir daqiqada»   MATEMATIKA OLAMI · tarixiy

Manba: Matematika olami, order 10.

The best story on the shelf, and the one closest to what this pipeline is FOR:
the answer is not the point, the LOOK is. A boy does not out-work the class, he
out-sees it — and that is an argument a picture can make and a sentence cannot.

So the film protects its silent beat harder than usual. The task is set, and
then nothing happens for four seconds while the viewer starts adding 1 + 2 + 3
in their head. That is the scene the surprise is bought with: whoever begins
adding has already lost the race, and they feel it before they are told it.

⚠️ It is a legend — the classroom details differ between books, and the reading
says so. The METHOD is not a legend, so the film asserts the method and hedges
the anecdote (`rivoyat` in the narration), exactly as the source does.
"""

from spec import Video, narrate, Scene
from scenes import cover, says, beat, claim, check, versus, rule, ask, outro
import primitives as P

# The pairing, dealt out one line at a time with a counter reading the DOM --
# the sum on screen therefore cannot get ahead of the pairs on screen.
_pairs, ps = P.solve([
    ("1 + 100 = 101", "eng chetdagi ikkitasi"),
    ("2 + 99 = 101",  "keyingi juft — yana 101"),
    ("3 + 98 = 101",  "va yana"),
    ("…",             "har safar bir xil"),
], at=0.8, step=1.25)

# NO COUNTER HERE, on purpose. A counter would honestly count the four rows on
# screen and label them "juft" -- while the film's whole point is that there are
# FIFTY pairs. The number would be true of the picture and false of the maths,
# which is the one thing this format must never do. The real count arrives in
# the `check` scene, where it is earned.
pairing = Scene(
    10.6,
    _pairs,
    cam="sink", top=True, name="juftlash",
    claims=["1 + 100 = 101", "2 + 99 = 101", "3 + 98 = 101"],
    note="Filmning yuragi. Har bir juft bir xil songa teng — buni aytish "
         "shart emas, ekranda koʻrinib turibdi.")

VIDEO = Video(
    slug="mo10",
    lesson="Matematika olami",
    title="Gauss: 1 dan 100 gacha bir daqiqada",
    story="Matematika olami — order 10",
    subject="math",
    scenes=[
        cover("5 050", "Toʻqqiz yashar bola",
              kicker="Matematika olami",
              context="1 dan 100 gacha hamma sonni qoʻshing:",
              strike=False,
              note="MUQOVA: javob darhol koʻrsatiladi — sir javobda emas, "
                   "USULDA. Vaʼda esa kim yechganini aytadi."),

        says("Oʻqituvchi", [("Bir dan yuzgacha", "lbl"),
                            ("hamma sonni qoʻshinglar", "lbl")],
             mood="smile", size=230,
             note="XVIII asr oxiri, Germaniya. Bu bir soatlik ish edi — "
                  "oʻqituvchi shuning uchun bergan."),

        beat(dur=4.6, n=3,
             note="ATAYLAB JIM. Tomoshabin shu yerda bittalab qoʻsha "
                  "boshlaydi — va poygani allaqachon yutqazadi. Surpriz "
                  "aynan shu sahnada sotib olinadi."),

        claim("Gauss", "1 + 2 + 3 + … + 100", "5 050",
              doubt="Bir daqiqada. U qanday qildi?",
              dur=8.4,
              note="Bittalab qoʻshgani yoʻq."),

        pairing,

        check("50 × 101 = 5 050",
              parts=["Yuzta sondan — 50 ta juft",
                     "Har bir juft — 101"],
              verdict="Javob bir marta koʻpaytirishda",
              title="Endi sanaymiz",
              dur=8.4,
              note="Bitta koʻpaytirish. Toʻqqiz yashar bola shuni koʻrgan."),

        versus({"name": "bittalab qoʻshsangiz",
                "qty": "99",
                "price": "ta amal",
                "tag": "bir soat", "cls": "lose"},
               {"name": "juftlab koʻrsangiz",
                "qty": "1",
                "price": "ta amal",
                "tag": "bir daqiqa", "cls": "win"},
               title="Bir xil masala, ikki xil nigoh",
               dur=11.5,
               note="Farq mehnatda emas — qarashda. Filmning butun gapi "
                    "shu ikki ustunda turibdi."),

        rule("Yechim koʻproq mehnatda emas, boshqacha qarashda",
             strip="1 … 100   →   50 × 101",
             meaning="Bittalab sanagan odam charchaydi; tuzilishni koʻrgan "
                     "odam yechadi. Gauss keyinchalik matematikaning deyarli "
                     "har bir sohasida iz qoldirdi, ammo eng mashhur hikoyasi "
                     "hamon oʻsha sinf xonasidan.",
             dur=10.0),

        ask("Endi 1 dan 1000 gacha qoʻshing. "
            "Nechta juft chiqadi va har biri nechaga teng?",
            dur=7.6,
            note="Javobni aytmang. Usul aynan oʻsha — faqat sonlar boshqa."),

        outro(),
    ],
)

narrate(VIDEO, [
    "Bir dan yuzgacha boʻlgan hamma sonni qoʻshing. || Javobi — 5050. "
    "| Va uni toʻqqiz yashar bola bir daqiqada topgan.",

    "Rivoyatga koʻra, XVIII asr oxirida Germaniyada bir oʻqituvchi shovqin "
    "solayotgan sinfni tinchitmoqchi boʻldi. || Bu bir soatlik ish edi. "
    "| Oʻqituvchi stulga oʻtirdi.",

    None,   # beat — jim sahna, tomoshabin oʻzi qoʻsha boshlaydi

    "Bir daqiqadan keyin Karl Fridrix Gauss doskaga chiqdi va javobni yozdi. "
    "|| U bittalab qoʻshgani yoʻq.",

    "U sonlarga chetlaridan qaradi. | Bir qoʻshamiz yuz — 101. | Ikki "
    "qoʻshamiz toʻqson toʻqqiz — yana 101. | Uch qoʻshamiz toʻqson sakkiz — "
    "yana 101. || Har bir juft bir xil.",

    "Endi sanaymiz. Yuzta sondan ellikta juft chiqadi. | Har biri 101 ga "
    "teng. || Ellik karra bir yuz bir — besh ming ellik.",

    "Bittalab qoʻshgan odam toʻqson toʻqqizta amal bajaradi. | Juftlab "
    "koʻrgan odam — bittasini. || Bir soat va bir daqiqa orasidagi farq "
    "shu yerda.",

    "Shuning uchun yechim koʻproq mehnatda emas, boshqacha qarashda. "
    "|| Bittalab sanagan odam charchaydi. Tuzilishni koʻrgan odam yechadi.",

    "Endi oʻzingiz oʻylang. Bir dan mingacha qoʻshsangiz, nechta juft "
    "chiqadi? || Va har biri nechaga teng boʻladi? Izohda kutamiz.",

    None,   # outro — jim
])
