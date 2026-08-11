# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-22 … PM-24.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 22 — ilmiy-ommabop (foizning tarixi), 23 — hikoya
(bozorda chegirma), 24 — xat (maktabdan ota-onaga).

⚠️ Kumulyativ: foiz oʻzgarishi (PM-25) va chegirma-ustama-soliq qoidalari
   (PM-26) hali yoʻq — 23-matndagi chegirma faqat «narxning p foizi»
   darajasida hisoblanadi.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_22_24.py --author=prime
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
    # PM-22 — kasr ↔ oʻnlik ↔ foiz                    ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bitta son, uch xil libos",
        "summary": (
            "PM-22 matni. Foiz nega aynan yuzga bogʻlangan va bitta ulush nima uchun "
            "kasr, oʻnlik kasr hamda foiz koʻrinishida yozilishi mumkin. Rim "
            "soligʻining tarixi haqiqiy maʼlumotga asoslangan."
        ),
        "order":   22,
        "grammar": [
            {
                "pattern":  "kasr = oʻnlik kasr = foiz",
                "meaning":  "Bitta ulushning uchta yozuvi. Kasrdan oʻnlikka: suratni "
                            "maxrajga boʻlamiz. Oʻnlikdan foizga: 100 ga koʻpaytiramiz "
                            "(vergul ikki xona oʻngga). Foizdan oʻnlikka: 100 ga "
                            "boʻlamiz.",
                "examples": [
                    "1/4 = 1 ÷ 4 = 0,25 = 25%",
                    "3/5 = 6/10 = 0,6 = 60% — demak 3/5 > 58%",
                ],
            },
        ],
        "questions": [
            {
                "text": "Odamlar nima uchun maxraj sifatida aynan 100 ni tanlashgan?",
                "choices": [
                    "Yuz — eng katta son boʻlgani uchun",
                    "Har xil kasrlarni taqqoslash oson boʻlishi uchun",
                    "Boshqa maxrajlar bilan boʻlish mumkin boʻlmagani uchun",
                    "Savdogarlar boshqa sonlarni bilmagani uchun",
                ],
                "answer": 1,
                "explanation": "Matnda aytilgan: 5/8 va 7/11 ni koʻz bilan taqqoslab "
                               "boʻlmaydi. Maxraj hamma joyda bir xil — 100 — boʻlsa, "
                               "faqat suratlarga qarash yetarli.",
            },
            {
                "text": "Matnga koʻra, 3/5 ni foizda qanday yozamiz?",
                "choices": ["35%", "53%", "60%", "65%"],
                "answer": 2,
                "explanation": "3/5 = 6/10 = 0,6, keyin vergulni ikki xona oʻngga "
                               "sursak — 60%. Shuning uchun 3/5 chegirma 58% "
                               "chegirmadan foydaliroq.",
            },
            {
                "text": "Bir savdogar mahsulotining 1/4 qismini bojga berdi. Bu necha "
                        "foiz boʻladi?",
                "choices": ["14%", "20%", "25%", "40%"],
                "answer": 2,
                "explanation": "1 ÷ 4 = 0,25; 0,25 × 100 = 25%. Yuzta katakli "
                               "kvadratning yigirma beshtasi — aynan chorak.",
            },
        ],
        "body": """
<p>Doʻkonda uchta yozuv turibdi: «<strong>1/2 narxda</strong>»,
«<strong>0,5 koeffitsient</strong>», «<strong>50% chegirma</strong>». Qaysi biri
foydaliroq? Savol aslida ayyor: uchalasi ham bitta xil son. Faqat libosi boshqa.</p>

<p><span class="cn-word" data-tr="butunning teng boʻlaklaridan biri yoki bir nechtasi">Kasr</span>
juda erkin: butunni istalgan sondagi boʻlakka boʻladi. Aynan shu erkinlik halaqit
beradi. 5/8 kattami yoki 7/11? Koʻz bilan aytib boʻlmaydi, chunki
<span class="cn-word" data-tr="kasrning pastki soni, butun nechta boʻlakka boʻlingani">maxraj</span>lar
har xil.</p>

<p>Shuning uchun savdogarlar bitta maxrajni tanlab olishdi — <strong>100</strong>. Har
qanday ulushni «yuzdan nechta» deb aytsak, taqqoslash arifmetikaga aylanadi. Shu
yuzdan boʻlakning nomi — <span class="cn-word" data-tr="butunning yuzdan bir boʻlagi, belgisi %">foiz</span>.</p>

<p>Bu odat qadimda paydo boʻlgan. Qadimgi Rimda sotilgan mollardan olinadigan boj
<i>centesima rerum venalium</i> deb atalgan — «sotiladigan narsalarning yuzdan biri»,
yaʼni <strong>1%</strong>. Lotincha <i>per centum</i> — «yuzdan» — bugungi «protsent»
soʻzining otasi.</p>

<p>Bitta ulushni uch xil yozish mumkin. Kasrdan
<span class="cn-word" data-tr="vergul bilan yoziladigan kasr">oʻnlik kasr</span>ga
oʻtish uchun <span class="cn-word" data-tr="kasrning yuqorigi soni">surat</span>ni
maxrajga boʻlamiz, oʻnlikdan foizga oʻtish uchun esa 100 ga koʻpaytiramiz:
<strong>1/4 = 0,25 = 25%</strong>.</p>

<p>Endi eski savolga qaytamiz. Bitta doʻkon narxning 3/5 qismini chegirma qilyapti,
ikkinchisi 58 foizini. <span class="cn-word" data-tr="qaysi biri katta ekanini aniqlash">Taqqoslash</span>
uchun ikkalasini bitta qiyofaga keltiramiz: <strong>3/5 = 0,6 = 60%</strong>. Demak
birinchi doʻkon saxiyroq.</p>

<p>Bitta son, uch xil libos. Qaysi birini kiyish — vaziyatga bogʻliq: hisoblashga
oʻnlik kasr qulay, taqqoslashga foiz, gapirishga esa kasr. «Yarim non» degan gap
«nonning 50 foizi» dan tabiiyroq eshitiladi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-23 — sonning foizini topish                          HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bozordagi chegirma",
        "summary": (
            "PM-23 matni. Sherbek bozorda kurtka narxidagi 15 foiz chegirmani ogʻzaki "
            "hisoblaydi: 10 foiz va uning yarmi. Sotuvchi kalkulyatorni ham "
            "olmaydi."
        ),
        "order":   23,
        "grammar": [
            {
                "pattern":  "sonning p foizi = son × p ÷ 100",
                "meaning":  "Foizni oʻnlik kasrga aylantirib songa koʻpaytiramiz. "
                            "Ogʻzaki hisobda 15% ni boʻlaklarga ajatish qulay: "
                            "15% = 10% + 5%, chunki 5% — 10% ning yarmi.",
                "examples": [
                    "180 000 ÷ 10 = 18 000 (10%); 18 000 ÷ 2 = 9000 (5%)",
                    "18 000 + 9000 = 27 000 (15%); 180 000 − 27 000 = 153 000",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sherbek nima uchun kalkulyatorni kutmadi?",
                "choices": [
                    "Sotuvchi kalkulyatorni bermadi",
                    "Chegirmani ogʻzaki hisoblash yoʻlini bilardi",
                    "Kurtkani olishga qaror qilmagan edi",
                    "Narx allaqachon yozib qoʻyilgan edi",
                ],
                "answer": 1,
                "explanation": "Sherbek 15% ni 10% va uning yarmiga ajratdi — bu "
                               "yoʻlni bilgan odamga kalkulyator kerak emas.",
            },
            {
                "text": "180 000 soʻmning 15 foizi qancha?",
                "choices": ["18 000 soʻm", "27 000 soʻm", "36 000 soʻm", "45 000 soʻm"],
                "answer": 1,
                "explanation": "10% = 18 000, 5% = 9000 (oʻn foizning yarmi). "
                               "18 000 + 9000 = 27 000 soʻm.",
            },
            {
                "text": "Sherbek kassaga necha soʻm toʻladi?",
                "choices": ["27 000 soʻm", "135 000 soʻm", "153 000 soʻm", "162 000 soʻm"],
                "answer": 2,
                "explanation": "Chegirmani narxdan ayiramiz: 180 000 − 27 000 = "
                               "153 000 soʻm. 162 000 — chegirmani 10% deb "
                               "hisoblaganda chiqadi.",
            },
        ],
        "body": """
<p>Sherbek bozorda kurtka koʻrdi. Yorliqda <strong>180 000 soʻm</strong> yozilgan edi,
yonida esa qoʻlda yozilgan katta varaq osilib turardi: «<strong>15% chegirma</strong>».</p>

<p>— Necha pul boʻladi? — soʻradi Sherbek.</p>

<p>— Shoshmang, kalkulyatorni olay, — dedi sotuvchi va sumkasini titkilay boshladi.</p>

<p>Sherbek kutmadi. U shu haftada
<span class="cn-word" data-tr="butunning yuzdan bir boʻlagi, belgisi %">foiz</span>ni
darsda oʻtgan edi va bir qoidani yaxshi eslab qolgandi:
<strong>15% = 10% + 5%</strong>.</p>

<p>Oʻn foizni topish eng oson —
<span class="cn-word" data-tr="foiz olinayotgan asos, 100% ga teng miqdor">butun</span>ni
oʻnga boʻlamiz: <strong>180 000 ÷ 10 = 18 000</strong>. Besh foiz esa oʻn foizning
yarmi: <strong>18 000 ÷ 2 = 9000</strong>.</p>

<p>— Chegirma <strong>27 000</strong> soʻm, — dedi Sherbek. — Toʻlaydiganim
<strong>153 000</strong> soʻm.</p>

<p>Sotuvchi kalkulyatorni endi topgan edi. U raqamlarni terdi, ekranga qaradi va
kulib yubordi.</p>

<p>— Toʻppa-toʻgʻri. Qanday hisobladingiz?</p>

<p>— Foizni <span class="cn-word" data-tr="katta miqdorni kichikroq qismlarga ajratish">boʻlaklar</span>ga
ajratdim, — dedi Sherbek. — Oʻn foizni topish uchun nolni oʻchirasiz, besh foiz esa
uning yarmi. Qolgani — oddiy qoʻshish.</p>

<p>Uyga qaytayotib u yana bir narsani oʻyladi. Agar chegirma 20 foiz boʻlganida,
<span class="cn-word" data-tr="butundan ajratilgan boʻlak">qism</span> 36 000 soʻm
boʻlardi — chunki 20% bu 10% ning ikki barobari. Bir marta oʻn foizni topib olsangiz,
qolgan foizlarning hammasi shundan yasaladi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-24 — foizdan butunni topish                             XAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Imtihon natijasi",
        "summary": (
            "PM-24 matni. Maktabdan ota-onalarga xat: sinf natijalari foizda "
            "berilgan. Xatning oxirida foizdan oʻquvchilar sonini tiklash kerak "
            "boʻladi."
        ),
        "order":   24,
        "grammar": [
            {
                "pattern":  "necha foiz = qism ÷ butun × 100; butun = qism ÷ 0,p",
                "meaning":  "Foizning ikki teskari savoli. Ulushni foizga aylantirish "
                            "uchun qismni butunga boʻlamiz. Foizi maʼlum boʻlganda "
                            "butunni tiklash uchun esa qismni oʻsha foizning oʻnlik "
                            "koʻrinishiga boʻlamiz.",
                "examples": [
                    "34 ÷ 40 = 0,85 → 85% (Jasurning natijasi)",
                    "15 ÷ 0,6 = 25 (60% i 15 kishi boʻlsa, sinfda 25 oʻquvchi)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Maktab xatni nima uchun yozgan?",
                "choices": [
                    "Ota-onalarni yigʻilishga chaqirish uchun",
                    "Imtihon natijalarini tushuntirish uchun",
                    "Yangi darslik sotib olishni soʻrash uchun",
                    "Sinfni boshqa binoga koʻchirish uchun",
                ],
                "answer": 1,
                "explanation": "Xatning boshida aytilgan: natijalar foizda eʼlon "
                               "qilingani uchun maktab ularni tushuntirmoqchi.",
            },
            {
                "text": "Jasur 40 savoldan 34 tasini toʻgʻri ishladi. Bu necha foiz?",
                "choices": ["34%", "68%", "85%", "94%"],
                "answer": 2,
                "explanation": "Qismni butunga boʻlamiz: 34 ÷ 40 = 0,85, keyin 100 ga "
                               "koʻpaytiramiz — 85%. Tekshirish: 40 × 0,85 = 34.",
            },
            {
                "text": "Sinfning 60 foizi — 15 oʻquvchi. Sinfda jami nechta oʻquvchi "
                        "bor?",
                "choices": ["9 ta", "20 ta", "25 ta", "30 ta"],
                "answer": 2,
                "explanation": "1% = 15 ÷ 60 = 0,25; 100% = 25 oʻquvchi. Tekshirish: "
                               "25 × 0,6 = 15. Javob 9 — 15 ni 0,6 ga koʻpaytirishdan "
                               "chiqadigan xato.",
            },
        ],
        "body": """
<p><b>Hurmatli ota-onalar!</b></p>

<p>Oʻtgan hafta 7-«B» sinfida matematikadan yozma imtihon boʻlib oʻtdi. Natijalar
elektron kundalikda <span class="cn-word" data-tr="butunning yuzdan bir boʻlagi, belgisi %">foiz</span>da
koʻrsatilgan, shuning uchun ularni qanday oʻqish kerakligini tushuntirib oʻtamiz.</p>

<p>Imtihonda <strong>40 ta</strong> savol bor edi. Bola nechta savolni toʻgʻri
ishlagan boʻlsa, oʻsha son
<span class="cn-word" data-tr="butundan ajratilgan boʻlak">qism</span>, savollarning
jami soni esa <span class="cn-word" data-tr="foiz olinayotgan asos, 100% ga teng miqdor">butun</span>
hisoblanadi. Natijani topish uchun qismni butunga boʻlib, 100 ga koʻpaytiramiz.</p>

<p>Masalan, Jasur 34 ta savolni toʻgʻri ishladi:
<strong>34 ÷ 40 = 0,85</strong>, yaʼni <strong>85%</strong>. Kundalikda aynan shu son
turibdi.</p>

<p>Baʼzi ota-onalar teskari savol berishdi: «Sinfning 60 foizi imtihondan 80 balldan
yuqori olibdi — bu nechta bola?» Bu yerda foiz va
<span class="cn-word" data-tr="maʼlum boʻlakdan butunni topish">qismdan butunni tiklash</span>
kerak boʻladi.</p>

<p>Bunday oʻquvchilar <strong>15 ta</strong> edi. Demak sinfdagi jami bolalar sonini
topamiz: bir foiz <strong>15 ÷ 60 = 0,25</strong> boladan iborat, yuz foiz esa
<strong>0,25 × 100 = 25</strong> bola. Sinfimizda haqiqatan ham 25 oʻquvchi bor.</p>

<p>Eʼtibor bering: bu yerda koʻpaytirish emas,
<span class="cn-word" data-tr="koʻpaytirishga qarama-qarshi amal">boʻlish</span>
ishlatildi. Butun har doim oʻz boʻlagidan katta boʻladi — javob 15 dan kichik chiqsa,
hisobda xato bor.</p>

<p>Farzandingizning natijasini birga koʻrib chiqing. 40 savoldan nechtasi
toʻgʻri boʻlganini bilsangiz, foizni oʻzingiz ham hisoblay olasiz.</p>

<p>Hurmat bilan, matematika oʻqituvchisi <b>Nodira opa</b>.</p>
""",
    },
]
