# -*- coding: utf-8 -*-
"""PM-12 — «Shaxmat taxtasidagi bugʻdoy»   SHAKL: KASHFIYOT

Manba: _stories_prime_math_10_12.py, order 12.

Bu videoning dvigateli — rasm bilan sonning ajralib ketishi. Taxta oxirigacha
xuddi shu taxta boʻlib qolaveradi; son esa odam tasavvuridan chiqib ketadi.
Shuning uchun birinchi sakkiz katak sanaladi, keyin faqat son oʻsadi.
"""

from spec import Video, Scene
from scenes import hook, says, beat, check, rule, ask, outro
import primitives as P

_bd, sbd = P.board(lit=8, at=0.8, step=0.62, show_upto=8)
doubling = Scene(
    11.0,
    P.counters(P.counter(8, "katak", at=0.8, dur=sbd, counts=".sq--on"))
    + _bd
    + P.line("har katakda oldingisidan ikki baravar", "lbl lbl--sm",
             at=0.8 + sbd + 0.4, anim="fade")
    + P.line("8-katak: 2<sup>7</sup> = 128 don", "expr gold",
             at=0.8 + sbd + 1.0, anim="pop", dur=0.6),
    cam="sink", top=True, name="doubling", counts=[8],
    claims=["1 + 2 + 4 + 8 = 15"],
    note="Bitta, ikkita, toʻrtta, sakkizta. Sakkizinchi katakda allaqachon 128 don.")

# Rasm oʻzgarmaydi, son oʻzgaradi — videoning butun gapi shu.
climb = Scene(
    10.5,
    P.line("21-katak", "lbl", at=0.0, anim="rise")
    + P.expr("1 000 000 dan oshdi", at=0.6, anim="pop", dur=0.6)
    + P.line("64-katak", "lbl", at=3.2, anim="rise")
    + P.expr("19 xonali son", at=3.8, anim="pop", dur=0.6, cls="gold")
    + P.line("butun taxta: 2<sup>64</sup> − 1", "lbl lbl--sm", at=6.4, anim="fade")
    + P.line("18 kvintilliondan ortiq don", "ttl red", at=7.0, anim="pop", dur=0.7),
    cam="push", name="climb",
    note="Yigirma birinchi katakda son bir milliondan oshdi. Oltmish toʻrtinchida "
         "— 19 xonali. Butun taxtada 18 kvintilliondan ortiq don.")

VIDEO = Video(
    slug="pm12",
    lesson="PM-12",
    title="Shaxmat taxtasidagi bugʻdoy",
    story="Prime Math Readings — order 12",
    scenes=[
        hook("1", "don birinchi katakka", "2", "ikkinchisiga",
             "Butun taxtaga qancha kerak?", dur=4.8),

        says("Sherbek", [("Har katakda", "lbl"),
                         ("ikki baravar koʻp", "expr"),
                         ("64-katakkacha", "ask")],
             dur=6.2, size=250,
             note="Donishmand kamtarona soʻradi: har katakda oldingisidan ikki "
                  "baravar koʻp. Shoh kulib yubordi — bir hovuch don-ku bu."),

        beat(4.2, note="Jim turing. Sizningcha, qancha chiqadi? Bir qop? Bir vagon?"),

        doubling,

        climb,

        check("1 + 2 + 4 + 8 = 15",
              parts=["keyingi katakda esa 16", "yaʼni oldingi hammasidan koʻp"],
              verdict="Ikkilanish — qoʻshish emas.", title="Kichik misolda koʻraylik",
              dur=8.0,
              note="Dastlabki toʻrt katakda 15 don. Beshinchisida 16 — oldingi "
                   "hammasidan bitta koʻp. Har qadamda shunday."),

        rule("Qoʻshib borish sekin oʻsadi, ikkilanish esa portlaydi",
             strip="2<sup>n</sup>",
             meaning="Shoh vaʼdasini bajara olmagan — jahon hosili bilan ham ming yil kerak.",
             dur=9.2,
             note="Shuning uchun daraja atigi ikki belgi bilan yoziladi — aks holda "
                  "uni yozishga qogʻoz yetmasdi."),

        ask("64-katakdagi donlar oldingi 63 ta katakdagi hammasidan koʻpmi, kammi?",
            dur=6.8, note="Javobni aytmang — bu savol oʻylash uchun."),

        outro(),
    ],
)
