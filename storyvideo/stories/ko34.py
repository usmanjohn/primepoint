# -*- coding: utf-8 -*-
"""KO-34 — «Oʻn bitta soʻz»  ·  MATN 01  ·  yangi registr

Manba: Prime Korean PK-12 · PK-14 · PK-20 — uchalasi bitta matn ichida.

YANGI TUR. Bundan oldingi filmlar qoidani KOʻRSATADI; bu film qoidani
matn ichida ISHLAYOTGAN holda koʻrsatadi. Koreyscha matn tabiiy tezlikda
oʻqiladi, oʻqilayotgan soʻz yonib turadi, va uning oʻzbekcha maʼnosi
tagida birin-ketin chiqadi.

Nega aynan shu matn: uchta oldingi grammatika filmining hammasi shu oʻn
bitta soʻz ichida bor — 저는 (KO-29), 도서관에 va 집에서 (KO-5), 갔어요 va
읽었어요 (KO-31). Yaʼni matn dalil: oʻrganilgan uchta qoida bir jumlada
birga ishlayapti.

## Vaqtlar OʻLCHANGAN, taxmin qilinmagan

edge-tts WordBoundary hodisasini bermaydi (2026-09-30 da tekshirildi —
koreyscha ham, inglizcha ham faqat SentenceBoundary qaytaradi), bu
mashinada esa forced aligner yoʻq. Shuning uchun `koaudio.time_passage`
jumlani BUTUN holda sintez qiladi (ohang tabiiy boʻlsin), har bir soʻzni
alohida sintez qilib faqat OʻLCHOV uchun ishlatadi, soʻng soʻz
uzunliklarini jumlaning haqiqiy uzunligiga moslab kengaytiradi.

Bu — taqsimlash, tekislash emas: soʻzga ~0.1s xato tushadi. Harakatlanayotgan
yoritgichda bu koʻrinmaydi, va raqamlar spetsifikatsiyada turgani uchun
kechikkan soʻzni qoʻlda surib qoʻyish mumkin.

⚠️ Yoritgich CSS transition EMAS. Transition devor soatida ishlaydi, `seek(t)`
esa sof funksiya — uchta parallel renderer bir kadrni uch xil ushlab qolardi.
`.on` / `.done` — `seek()` yoqadigan holat, xuddi `.tick` kabi.
"""

from spec import Video, narrate
from scenes import (cover, passage, pairs, echo, rule, ask, practice, outro)

VIDEO = Video(
    slug="ko34",
    lesson="PK-12 · PK-14 · PK-20",
    title="Oʻn bitta soʻz",
    story="Prime Korean — oʻqib borish matni",
    subject="korean",
    scenes=[
        cover("어제 저는…", "Hammasi tanish soʻz",
              ko="한국어",
              track="Matn", n=1, badge="big",
              context="Koreyscha matn — birga oʻqiymiz:",
              strike=False,
              note="MUQOVA: gʻalati narsa — koreyscha jumlaning boshi. "
                   "Vaʼda: qoʻrqmang, hammasi tanish."),

        passage([
            ("어제", "kecha", 0.000, 0.361),
            ("저는", "men esa", 0.421, 0.802),
            ("도서관에", "kutubxonaga", 0.862, 1.379),
            ("갔어요.", "bordim", 1.439, 1.923),
            ("책을", "kitob", 2.373, 2.743),
            ("세", "uchta", 2.803, 3.090),
            ("권", "(kitob sanogʻi)", 3.150, 3.483),
            ("빌렸어요.", "oldim", 3.543, 4.090),
            ("집에서", "uyda", 4.540, 5.035),
            ("밤까지", "kechgacha", 5.095, 5.677),
            ("읽었어요.", "oʻqidim", 5.737, 6.337),
        ],
            head="Koreys ovozi oʻqiydi — siz kuzatib boring",
            tail="Kecha kutubxonaga bordim, uyda kechgacha oʻqidim.",
            dur=11.0,
            note="JIM sahna (oʻzbekcha ovoz yoʻq). Koreyscha TTS oʻqiydi, "
                 "yonayotgan soʻz ovoz bilan birga suriladi, maʼnosi "
                 "tagida chiqadi. Vaqtlar oʻlchangan."),

        pairs([("저는", "은/는 — «men esa»"),
               ("에 / 에서", "joyga / joyda"),
               ("갔어요 / 읽었어요", "ㅏ → 았,  boshqasi → 었")],
              head="Bu matnda uchta tanish qoida bor",
              tail="Uchtasi bitta matnda, birga ishlayapti.",
              dur=13.0,
              note="Filmning dalili: uchta alohida dars bitta jumlada "
                   "uchrashdi. Oʻng ustun — oldingi uchta filmning oʻzi."),

        echo("도서관에", gloss="kutubxonaga",
             note="JIM sahna. Matndagi eng uzun soʻz — alohida takrorlanadi."),

        rule("Matn oʻqish — qoidalarni tanib olish",
             strip="저는 · 도서관에 · 갔어요",
             meaning="Qoidani alohida yodlash yetmaydi. Matnda uni koʻrib "
                     "tanisangiz — oʻsha qoida sizniki boʻldi. Shuning uchun "
                     "har bir darsdan keyin shu darsning matnini oʻqing.",
             dur=10.5),

        ask("Matnda 세 권 bor — «uchta». "
            "| Nega 권, nega 개 emas?",
            dur=7.0,
            note="Javobni aytmang. 권 videoda tarjima qilingan, lekin "
                 "nega aynan u ekani hech qayerda aytilmagan."),

        practice("Burchak · Prime Korean Readings",
                 sub="powerty.uz → Burchak → Prime Korean Readings",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Bugun koreyscha matn oʻqiymiz. | Oʻn bitta soʻz. "
    "|| Va hammasi sizga tanish.",

    None,   # passage — koreyscha ovoz oʻqiydi, oʻzbekcha ovoz jim

    "Bu matnda uchta tanish qoida bor. "
    "| 저는 — «men esa». | 도서관에 va 집에서 — biri joyga, ikkinchisi joyda. "
    "|| 갔어요 va 읽었어요 — oʻzak unlisi qoʻshimchani tanladi.",

    None,   # echo(도서관에)

    "Qoidani alohida yodlash yetmaydi. "
    "| Matnda uni koʻrib tanisangiz — oʻsha qoida sizniki boʻldi. "
    "|| Shuning uchun har bir darsdan keyin shu darsning matnini oʻqing.",

    "Endi oʻzingiz oʻylang. Matnda 세 권 bor — uchta. "
    "| Nega 권, nega 개 emas? || Izohda kutamiz.",

    "Prime Korean matnlari — Powertyda, Burchak boʻlimida.",

    None,   # outro
])
