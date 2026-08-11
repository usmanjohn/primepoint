# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-16 … PM-18.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 16 — retsept (ikki karta yonma-yon), 17 — hikoya (devor
boʻyash), 18 — oshxonadagi sahna (toc da «retsept» deb belgilangan edi; bitta
batchda ikkita retsept boʻlmasligi uchun sahnaga aylantirildi).

⚠️ Kumulyativ: notoʻgʻri kasr va aralash son PM-19 da, oʻnlik kasr PM-20 da —
   bu matnlarda har bir son toʻgʻri kasr yoki butun.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_16_18.py --author=prime
"""

SUBJECT = {
    "name":    "Matematika",
    "summary": "Matematika: hayotdagi matnlar, atamalar va matematik hikoyalar.",
    "icon":    "bi-calculator",
    "color":   "#f59e0b",
    "order":   7,
}

COLLECTION = {
    "title":       "Prime Math Readings",
    "description": (
        "Prime Math darslarining oʻqish matnlari — har biri oʻz darsining "
        "matematikasini hayotdagi matn ichida koʻrsatadi. Atamalar izohi bilan."
    ),
    "order": 1,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PM-16 — qisqartirish va taqqoslash                 RETSEPT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Qaysi biri koʻproq?",
        "summary": (
            "PM-16 matni. Bitta taomning ikki xil retsepti — sonlar boshqa, miqdor "
            "esa bir xil. Qisqartirish nima uchun kerakligi shu yerda koʻrinadi."
        ),
        "order":   16,
        "grammar": [
            {
                "pattern":  "Teng kasrlar: bir xil miqdor, boshqa yozuv",
                "meaning":  "Surat va maxrajni bir xil songa koʻpaytirsa yoki boʻlsa, "
                            "kasr oʻzgarmaydi. Shuning uchun ikki xil yozilgan miqdor "
                            "aslida bitta boʻlishi mumkin. Buni bilish uchun "
                            "ikkalasini ham qisqarmas holatga keltirish yetarli.",
                "examples": [
                    "6/8 = 3/4 (ikkalasini 2 ga boʻldik)",
                    "4/10 = 2/5 va 2/5 — teng, demak retseptlar bir xil",
                ],
            },
        ],
        "questions": [
            {
                "text": "Afsona nima uchun ikki retseptni solishtira olmadi?",
                "choices": [
                    "Retseptlar boshqa-boshqa taomlar uchun edi",
                    "Miqdorlar har xil maxrajlar bilan yozilgan edi",
                    "Bir retseptda sut yoʻq edi",
                    "Buvijonning daftari yirtilgan edi",
                ],
                "answer": 1,
                "explanation": "Sonlar har xil koʻrinardi (6/8 va 3/4), chunki "
                               "boʻlaklar har xil kattalikda olingan edi.",
            },
            {
                "text": "6/8 stakan sut qisqartirilsa, qanday yoziladi?",
                "choices": ["1/2 stakan", "2/3 stakan", "3/4 stakan", "4/6 stakan"],
                "answer": 2,
                "explanation": "6/8 — surat va maxrajni 2 ga boʻlamiz: 3/4. Demak "
                               "ikkala retseptda ham bir xil miqdor sut bor.",
            },
            {
                "text": "Bir retseptda 4/10 stakan yogʻ, ikkinchisida 2/5 stakan. "
                        "Qaysi biri koʻproq?",
                "choices": [
                    "4/10 koʻproq, chunki 4 soni 2 dan katta",
                    "2/5 koʻproq, chunki maxraji kichik",
                    "Ular teng — 4/10 qisqartirilsa 2/5 chiqadi",
                    "Solishtirib boʻlmaydi",
                ],
                "answer": 2,
                "explanation": "4/10 ning surat va maxrajini 2 ga boʻlsak, 2/5 "
                               "hosil boʻladi. Sonlar boshqa, miqdor bir xil.",
            },
        ],
        "body": """
<p>Afsona bugun oʻzi ovqat pishirmoqchi boʻldi. Stol ustida ikkita retsept turardi:
buvijonning eski daftari va telefondagi sayt.</p>

<p><b>Buvijonning daftari:</b> 3/4 stakan sut, 2/5 stakan yogʻ, 1/2 choy qoshiq tuz.</p>

<p><b>Telefondagi retsept:</b> 6/8 stakan sut, 4/10 stakan yogʻ, 2/4 choy qoshiq tuz.</p>

<p>Afsona ikkovini yonma-yon qoʻyib, boshi qotdi. Sonlar butunlay boshqacha. Qaysi
biriga ishonish kerak?</p>

<p>Onasi kirib, bir qarab qoʻydi:</p>

<p>— Ikkalasi ham bir xil, qizim. Faqat bittasi
<span class="cn-word" data-tr="surat va maxrajni umumiy boʻluvchiga boʻlish">qisqartirilgan</span>,
ikkinchisi yoʻq.</p>

<p>Afsona daftariga yozdi. <strong>6/8</strong> — surat va
<span class="cn-word" data-tr="kasrning pastki soni: nechta teng boʻlakka boʻlingani">maxraj</span>ni
2 ga boʻlsa, <strong>3/4</strong> chiqadi. Keyin <strong>4/10</strong> — yana 2 ga
boʻlsa, <strong>2/5</strong>. Va <strong>2/4</strong> — yana 2 ga boʻlsa,
<strong>1/2</strong>.</p>

<p>Uchala qatorda ham bir xil miqdor turgan ekan. Ular
<span class="cn-word" data-tr="bir xil miqdorni bildiruvchi turli yozuvlar">teng kasrlar</span>
edi.</p>

<p>— Nega hamma retseptni bir xil yozmaydi? — soʻradi Afsona.</p>

<p>— Chunki oʻlchov idishi har xil, — dedi onasi. — Kimningdir stakani toʻrtga,
kimningdiki sakkizga boʻlingan. Muhimi — miqdor bir xil.</p>

<p>Kechqurun Afsona daftariga qoida yozib qoʻydi: ikki kasrni solishtirish uchun avval
ikkalasini ham <span class="cn-word" data-tr="boshqa qisqartirib boʻlmaydigan kasr">qisqarmas</span>
holatga keltirish kerak. Shundan keyin
<span class="cn-word" data-tr="qaysi biri katta yoki kichikligini aniqlash">taqqoslash</span>
bir soniyalik ish boʻlib qoladi. Va agar
<span class="cn-word" data-tr="ikkala sonni ham qoldiqsiz boʻluvchi son">umumiy boʻluvchi</span>
darrov koʻrinmasa, EKUB ni topish yetarli — u kasrni bir qadamda oxirigacha
qisqartiradi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-17 — qoʻshish va ayirish                        HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Devorni ikki kunda boʻyash",
        "summary": (
            "PM-17 matni. Bekzod ikki kun ishladi va ishni tez hisoblab yubordi — "
            "lekin maxrajlarni ham qoʻshib yuborgani natijani buzdi."
        ),
        "order":   17,
        "grammar": [
            {
                "pattern":  "Umumiy maxrajga keltirib qoʻshish",
                "meaning":  "Har xil kattalikdagi boʻlaklarni qoʻshib boʻlmaydi. Avval "
                            "ikkala kasrni bir xil maxrajga keltiriladi (maxrajlarning "
                            "EKUK i), keyin faqat suratlar qoʻshiladi. Maxraj hech "
                            "qachon qoʻshilmaydi.",
                "examples": [
                    "1/3 + 1/4 = 4/12 + 3/12 = 7/12 (boʻyalgan qism)",
                    "12/12 − 7/12 = 5/12 (qolgan qism)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Bekzodning birinchi javobi nega notoʻgʻri edi?",
                "choices": [
                    "U kunlarni notoʻgʻri sanagan",
                    "U suratlarni ham, maxrajlarni ham qoʻshib yuborgan",
                    "U devorning balandligini hisobga olmagan",
                    "U ikkinchi kunni unutgan",
                ],
                "answer": 1,
                "explanation": "«Ikki qoʻshuv bir — uch, uch qoʻshuv toʻrt — yetti» "
                               "deb u 2/7 chiqargan. Maxraj boʻlakning nomi, u "
                               "qoʻshilmaydi.",
            },
            {
                "text": "Devorning qanchasi boʻyalgan?",
                "choices": ["2/7", "5/12", "7/12", "7/7"],
                "answer": 2,
                "explanation": "EKUK(3, 4) = 12. 1/3 = 4/12, 1/4 = 3/12. "
                               "4/12 + 3/12 = 7/12.",
            },
            {
                "text": "Devorning qanchasi boʻyalmay qolgan?",
                "choices": ["5/12", "7/12", "1/12", "5/7"],
                "answer": 0,
                "explanation": "Butun devor — 12/12. 12/12 − 7/12 = 5/12. Tekshiruv: "
                               "7/12 + 5/12 = 12/12 = 1 ✓",
            },
        ],
        "body": """
<p>Yozgi taʼtil. Bekzod otasiga yordamlashib, ombor devorini boʻyayapti.</p>

<p>Birinchi kuni u devorning <strong>1/3</strong> qismini boʻyadi. Quyosh qizdirdi,
qoʻli charchadi va u toʻxtadi.</p>

<p>Ikkinchi kuni ishtiyoq kamroq edi — <strong>1/4</strong> qism boʻyaldi, xolos.</p>

<p>Kechqurun otasi soʻradi:</p>

<p>— Qanchasi tayyor boʻldi?</p>

<p>Bekzod bir soniyada javob berdi: «Ikki qoʻshuv bir — uch, uch qoʻshuv toʻrt — yetti.
Ikki yetti, ota. 2/7.»</p>

<p>Otasi kulib qoʻydi va boʻyoq chelagini yerga qoʻydi.</p>

<p>— Oʻgʻlim, birinchi kuni devorning uchdan birini boʻyading. Endi ayt-chi, ikki
kundan keyin ish uchdan birdan <b>koʻpmi</b> yoki kammi?</p>

<p>— Albatta koʻp.</p>

<p>— Sening javobing esa 2/7. Bu uchdan birdan kichik. Demak bir joyda xato bor.</p>

<p>Xato <span class="cn-word" data-tr="kasrning pastki soni: nechta teng boʻlakka boʻlingani">maxraj</span>da
edi. Uchdan bir va chorak — <b>har xil kattalikdagi</b> boʻlaklar, ularni bevosita
qoʻshib boʻlmaydi. Avval ikkalasini bir xil boʻlakka keltirish kerak. Bu
<span class="cn-word" data-tr="ikki kasrni bir xil boʻlakka keltiruvchi maxraj">umumiy maxraj</span>
deyiladi va u 3 bilan 4 ning
<span class="cn-word" data-tr="eng kichik umumiy karrali">EKUK</span> iga teng — 12.</p>

<p>Bekzod ikkala kasrni <span class="cn-word" data-tr="kasrni kattaroq maxrajli teng kasrga aylantirish">kengaytirdi</span>: <strong>1/3 = 4/12</strong>,
<strong>1/4 = 3/12</strong>. Endi boʻlaklar bir xil, faqat
<span class="cn-word" data-tr="kasrning yuqorigi soni: nechta boʻlak olingani">surat</span>lar
qoʻshiladi: <strong>4/12 + 3/12 = 7/12</strong>.</p>

<p>— Yarmidan sal koʻproq, — dedi otasi. — Mana bu boshqa gap.</p>

<p>Qolgan qismni topish uchun <span class="cn-word" data-tr="boʻlinmagan bir dona; kasr koʻrinishida maxraj/maxraj deb yoziladi">butun</span> devorni <b>12/12</b> deb yozdilar:
<strong>12/12 − 7/12 = 5/12</strong>. Bu ertangi ish edi.</p>

<p>Bekzod boʻyoq chelagiga qarab bir narsani tushundi: qoʻshishda
<span class="cn-word" data-tr="qoʻshish natijasi">yigʻindi</span> har ikkala
qoʻshiluvchidan ham katta chiqishi shart. Agar kichik chiqsa — hisobni qaytadan
koʻrish kerak. Bu qoida uni keyinchalik koʻp marta qutqardi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-18 — koʻpaytirish va boʻlish                    OSHXONADAGI SAHNA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Yarimning uchdan biri",
        "summary": (
            "PM-18 matni. Retsept olti kishiga, mehmon esa ikkita. Oshxonada "
            "«…ning …qismi» degan ibora koʻpaytirishga aylanadi."
        ),
        "order":   18,
        "grammar": [
            {
                "pattern":  "«…ning …qismi» — koʻpaytirish",
                "meaning":  "Kasrni kasrga koʻpaytirganda surat suratga, maxraj "
                            "maxrajga koʻpaytiriladi. 1 dan kichik songa "
                            "koʻpaytirish natijani kichraytiradi — chunki bu "
                            "butunni emas, uning boʻlagini olish demakdir.",
                "examples": [
                    "1/3 × 1/2 = 1/6 stakan (yogʻ)",
                    "1/3 × 3/4 = 3/12 = 1/4 kg (guruch)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nodira opa nega retseptning uchdan bir qismini oldi?",
                "choices": [
                    "Yogʻi kam qolgani uchun",
                    "Guruch qimmat boʻlgani uchun",
                    "Retsept 6 kishiga, mehmon esa 2 kishi boʻlgani uchun",
                    "Qozon kichkina boʻlgani uchun",
                ],
                "answer": 2,
                "explanation": "2 ni 6 ga boʻlsak 1/3 chiqadi — demak har bir "
                               "mahsulotning uchdan bir qismi kerak.",
            },
            {
                "text": "Retseptda 1/2 stakan yogʻ bor. Uning uchdan biri qancha?",
                "choices": ["1/6 stakan", "1/5 stakan", "1/3 stakan", "2/3 stakan"],
                "answer": 0,
                "explanation": "1/3 × 1/2 = 1/6. Tekshiruv: 3 × 1/6 = 3/6 = 1/2 — "
                               "retseptga qaytdi.",
            },
            {
                "text": "Retseptda 3/4 kg guruch bor. Nodira opaga qancha kerak?",
                "choices": ["1/12 kg", "1/4 kg", "1/3 kg", "3/8 kg"],
                "answer": 1,
                "explanation": "1/3 × 3/4 = 3/12 = 1/4 kg. Tekshiruv: "
                               "3 × 1/4 = 3/4 kg ✓",
            },
        ],
        "body": """
<p>Peshin. Nodira opa oshxonada, oldida ochilgan daftar.</p>

<p>— Afsona, kelib bir yordam ber. Bu retsept <b>olti kishiga</b> yozilgan, mehmon esa
ikki kishi. Nima qilamiz?</p>

<p>Afsona daftarga qaradi: <b>1/2 stakan yogʻ</b>, <b>3/4 kg guruch</b>, bir bosh
piyoz.</p>

<p>— Olti kishidan ikki kishi… — dedi u. — Bu retseptning uchdan biri boʻladi, xola.
2 ni 6 ga boʻlsak, 1/3.</p>

<p>— Barakalla. Endi ayt: yarim stakanning uchdan biri qancha?</p>

<p>Afsona bir soniya jim qoldi. Bu qoʻshish emas, ayirish ham emas edi.</p>

<p>— «…ning …qismi» — bu <span class="cn-word" data-tr="bir sonni ikkinchisiga necha marta takrorlab qoʻshish amali">koʻpaytirish</span>
boʻladi, — dedi u nihoyat. — Demak 1/3 × 1/2.</p>

<p>U <span class="cn-word" data-tr="kasrning yuqorigi soni">surat</span>larni
koʻpaytirdi: 1 × 1 = 1. Keyin <span class="cn-word" data-tr="kasrning pastki soni">maxraj</span>larni:
3 × 2 = 6. Javob — <strong>1/6 stakan</strong>.</p>

<p>— Toʻgʻri, — dedi Nodira opa. — Qara: butunni avval ikkiga boʻldik, keyin har
yarmini uchga. Jami oltita katak chiqdi. Bittasi bizniki.</p>

<p>Guruch bilan ham xuddi shunday boʻldi: <strong>1/3 × 3/4 = 3/12</strong>, buni
<span class="cn-word" data-tr="surat va maxrajni umumiy boʻluvchiga boʻlish">qisqartirsak</span>
<strong>1/4 kg</strong>.</p>

<p>Afsona bir narsaga hayron qoldi: koʻpaytirdi, lekin son <b>kichrayib</b> ketdi.</p>

<p>— Shunday boʻladi, — kuldi Nodira opa. — Birdan kichik songa koʻpaytirish
<span class="cn-word" data-tr="butunning bir qismi">ulush</span> olish degani. Yarmining
uchdan biri yarimdan katta boʻlishi mumkinmi?</p>

<p>Oxirida ikkalasi tekshirib koʻrishdi: agar bir ulush 1/6 stakan boʻlsa, uchta ulush
3 × 1/6 = 3/6, yaʼni yarim stakan beradi. Retseptga qaytdi — demak hisob toʻgʻri.
Bu <span class="cn-word" data-tr="bajarilgan amalni bekor qiladigan amal">teskari amal</span>
bilan tekshirish edi.</p>

<p>Osh mazali chiqdi. Mehmonlar retseptni soʻrashdi.</p>
""",
    },
]
