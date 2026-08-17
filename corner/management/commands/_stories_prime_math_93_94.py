# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-93, PM-94 (Blok G ning oxirgi ikkitasi).

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 93 — jumboq, 94 — hikoya.
Oldingi uchlik hikoya / retsept / sharh edi.

⚠️ Kumulyativ:
   • 93-matnda yoshlar farqining oʻzgarmasligi va ikkita savol —
     «necha yildan keyin» va «necha yil oldin». ⛔ Sonlar haqidagi
     masalalar (10a + b) YOʻQ — u darsning oʻzida qoladi;
   • 94-matnda birlik xatosi va uni birlik miqdor (bir kishiga necha
     gramm) bilan ushlash. ⛔ Yuza birliklari YOʻQ — matnda faqat
     massa; kvadrat qoidasi darsning oʻzida.
⚠️ Sonlar darsdagilardan boshqa: 93 → 40/10 (darsda 35/5 va 45/15),
   94 → osh retsepti (darsda plitka va daftar).
⚠️ Savollar SAQLANGAN TARTIBDA koʻrsatiladi — `answer` indekslari:
   93 → 2/1/3, 94 → 0/2/1.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_93_94.py --author=prime
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
    # PM-93 — yosh masalalari                                    JUMBOQ
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ota va oʻgʻil",
        "summary": (
            "PM-93 matni. Jumboq: bobo nevarasiga eski topishmoqni "
            "beradi. Javob yoshlarning oʻzida emas, ular orasidagi "
            "oʻzgarmas farqda yashiringan."
        ),
        "order":   93,
        "grammar": [
            {
                "pattern":  "yoshlar farqi oʻzgarmaydi, nisbat oʻzgaradi",
                "meaning":  "Vaqt hamma uchun bir xil oʻtadi: bir yilda "
                            "ikkalasining yoshiga ham bittadan "
                            "qoʻshiladi. Shuning uchun ayirma "
                            "oʻzgarmas, «necha marta katta» esa har "
                            "yili boshqacha.",
                "examples": [
                    "40 + x = 2(10 + x) → x = 20; 60 va 30",
                    "40 − x = 7(10 − x) → x = 5; 35 va 5",
                    "farq har uch holatda ham 30",
                ],
            },
        ],
        "questions": [
            {
                "text": "Boboning aytishicha, jumboqning kaliti nimada?",
                "choices": [
                    "Otaning yoshida",
                    "Oʻgʻilning yoshida",
                    "Ular orasidagi farqda",
                    "Oʻtgan yillar sonida",
                ],
                "answer": 2,
                "explanation": "Bobo yoshlarga emas, ular orasidagi "
                               "30 yillik farqqa qarashni aytdi. Farq "
                               "hech qachon oʻzgarmaydi, shuning uchun "
                               "u har qanday paytda tayanch boʻla "
                               "oladi.",
            },
            {
                "text": "Necha yildan keyin ota oʻgʻlidan roppa-rosa "
                        "2 marta katta boʻladi?",
                "choices": ["10 yildan keyin", "20 yildan keyin",
                            "25 yildan keyin", "30 yildan keyin"],
                "answer": 1,
                "explanation": "40 + x = 2(10 + x) → 40 + x = 20 + 2x → "
                               "x = 20. Oʻshanda ota 60, oʻgʻil "
                               "30 yoshda boʻladi va 60 ÷ 30 = 2 ✓ "
                               "Farq esa hamon 30.",
            },
            {
                "text": "Necha yil oldin ota oʻgʻlidan 7 marta katta "
                        "edi?",
                "choices": ["2 yil oldin", "3 yil oldin", "4 yil oldin",
                            "5 yil oldin"],
                "answer": 3,
                "explanation": "40 − x = 7(10 − x) → 40 − x = 70 − 7x → "
                               "6x = 30 → x = 5. Besh yil oldin ota 35, "
                               "oʻgʻil 5 yoshda edi: 35 ÷ 5 = 7 ✓ "
                               "Diqqat: ayirish ikkalasiga ham "
                               "qoʻllaniladi.",
            },
        ],
        "body": """
<p>Bobo ayvonda oʻtirib choy ichardi. Nevarasi Jasur yoniga kelib
qoldi.</p>

<p>«Sen matematikani yaxshi koʻrasan-a?» — dedi bobo. «Unda men senga
oʻzim bolaligimda eshitgan
<span class="cn-word" data-tr="oʻylab topiladigan topishmoq masala">jumboq</span>ni
beraman».</p>

<p>U choy piyolasini qoʻydi va gapini boshladi.</p>

<p>«Bir otaning <span class="cn-word" data-tr="tugʻilgandan beri oʻtgan yillar soni">yosh</span>i
<strong>40</strong> da, oʻgʻlining yoshi <strong>10</strong> da. Hozir ota
oʻgʻlidan toʻrt marta katta.
Ayt-chi: <b>necha yildan keyin ota oʻgʻlidan roppa-rosa ikki marta
katta boʻladi?</b>»</p>

<p>Jasur darrov hisoblay boshladi. «Toʻrt martadan ikki martaga tushish
kerak… demak yarmi… yigirma yil?»</p>

<p>«Toʻgʻri javob aytding», dedi bobo. «Lekin taxmin bilan aytding.
Endi buni <b>bilib</b> ayt».</p>

<p>Jasur daftar oldi. U x deb — ya'ni
<span class="cn-word" data-tr="topilishi kerak boʻlgan miqdor">nomaʼlum</span>
deb — oʻtadigan yillar sonini belgiladi. Muhimi
shu ediki, x ikkalasiga ham qoʻshiladi — vaqt hamma uchun bir xil
oʻtadi.</p>

<p>Shunday <span class="cn-word" data-tr="ikki ifodaning tengligi">tenglama</span>
chiqdi: 40 + x = 2(10 + x). Qavsni ochdi: 40 + x = 20 + 2x. Demak
x = <strong>20</strong>.</p>

<p><span class="cn-word" data-tr="javobni masala shartlariga qaytarib qoʻyish">Tekshir</span>di:
yigirma yildan keyin ota 60, oʻgʻil 30 yoshda boʻladi.
60 ÷ 30 = 2 ✓</p>

<p>«Yaxshi», dedi bobo. «Endi ikkinchi savol.
<b>Necha yil oldin ota oʻgʻlidan yetti marta katta edi?</b>»</p>

<p>Jasur bir zum toʻxtadi. <span class="cn-word" data-tr="oʻtib ketgan vaqt">Oʻtmish</span>
haqidagi savol unga qiyinroq tuyuldi.</p>

<p>«Faqat bir narsani unutma», dedi bobo. «Yillar oʻtganda ham,
orqaga qaytganda ham, bitta son
<span class="cn-word" data-tr="qiymati oʻzgarmaydigan kattalik">oʻzgarmas</span>
qoladi. Qaysi son?»</p>

<p>Jasur oʻyladi. Ota 40, oʻgʻil 10 — orasidagi
<span class="cn-word" data-tr="ikki yosh orasidagi ayirma">farq</span>
<strong>30</strong>. Yigirma yildan keyin 60 va 30 — farqi yana
<strong>30</strong>.</p>

<p>«Farq!» — dedi u. «Farq hech qachon oʻzgarmaydi. Faqat
<span class="cn-word" data-tr="«necha marta katta» degan savolning javobi">nisbat</span>
oʻzgaradi».</p>

<p>«Mana endi jumboqni yechding», dedi bobo.</p>

<p>Jasur ikkinchi savolni yozdi: 40 − x = 7(10 − x). Bu safar x
ikkalasidan ham <b>ayiriladi</b>.</p>

<p>40 − x = 70 − 7x, demak 6x = 30 va x = <strong>5</strong>.</p>

<p>Besh yil oldin ota <strong>35</strong>, oʻgʻil <strong>5</strong>
yoshda edi. 35 ÷ 5 = 7 ✓ Farq esa oʻsha 30 —
<span class="cn-word" data-tr="oʻzgarmaydigan kattalik">doimiy</span> son.</p>

<p>«Bilasanmi bu jumboqning sirini?» — dedi bobo piyolani olarkan.
«Odamlar yoshlarga qarashadi va chalkashib ketishadi. Yoshlar har yili
oʻzgaradi. Farq esa bir umr oʻzgarmaydi — u
<span class="cn-word" data-tr="masalada tayanch boʻladigan doimiy son">tayanch</span>».</p>

<p>Jasur daftarni yopdi va soʻradi: «Bobo, sizning otangiz sizdan necha
yosh katta edi?»</p>

<p>«Yigirma sakkiz», dedi bobo. «Bugun ham yigirma sakkiz. U kishi yoʻq
boʻlsalar ham».</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-94 — oʻlchov birliklari                                 HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Retseptdagi xato — gramm va kilogramm",
        "summary": (
            "PM-94 matni. Hikoya: Sherbek toʻrt kishilik osh damlamoqchi. "
            "Koʻchirilgan retseptda bitta birlik xato yozilgan va uni "
            "faqat bir kishiga toʻgʻri keladigan miqdor fosh qiladi."
        ),
        "order":   94,
        "grammar": [
            {
                "pattern":  "birlik miqdor = jami ÷ kishilar soni",
                "meaning":  "Retsept boʻyicha bir kishiga qancha "
                            "toʻgʻri kelishini hisoblash. Bu son "
                            "birlik xatosini darrov fosh qiladi — "
                            "chunki uni hayotdagi tajriba bilan "
                            "solishtirish mumkin.",
                "examples": [
                    "1,5 kg = 1500 g; 1500 ÷ 12 = 125 g bir kishiga",
                    "4 kishiga: 4 × 125 = 500 g = 0,5 kg",
                    "xato variant: 5000 ÷ 4 = 1250 g — oʻn barobar koʻp",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sherbek xatoni qanday topdi?",
                "choices": [
                    "Bir kishiga necha gramm toʻgʻri kelishini hisoblab",
                    "Guruchni tarozida oʻlchab",
                    "Buvisiga telefon qilib",
                    "Retseptni qaytadan oʻqib",
                ],
                "answer": 0,
                "explanation": "U 1500 g ni 12 kishiga boʻlib, bir "
                               "kishiga 125 g toʻgʻri kelishini topdi. "
                               "Xato yozuvda esa bir kishiga 1250 g "
                               "chiqardi — oʻn barobar koʻp, va bu "
                               "darrov koʻzga tashlandi.",
            },
            {
                "text": "Toʻrt kishiga qancha guruch kerak?",
                "choices": ["125 g", "375 g", "500 g", "5 kg"],
                "answer": 2,
                "explanation": "Bir kishiga 1500 ÷ 12 = 125 g. Toʻrt "
                               "kishiga 4 × 125 = 500 g, ya'ni 0,5 kg. "
                               "«5 kg» — daftardagi xato yozuv, u "
                               "toʻgʻri javobdan oʻn barobar katta.",
            },
            {
                "text": "Matnda qaysi maʼlumot masalani yechish uchun "
                        "kerak emas edi?",
                "choices": [
                    "Guruchning miqdori",
                    "Osh 40 daqiqa damlanishi",
                    "Mehmonlar soni",
                    "Retsept necha kishiga moʻljallangani",
                ],
                "answer": 1,
                "explanation": "«40 daqiqa» — pishirish vaqti. U taomni "
                               "tayyorlash uchun kerak, lekin guruch "
                               "miqdorini hisoblashga hech qanday "
                               "aloqasi yoʻq. Bu — ortiqcha maʼlumot.",
            },
        ],
        "body": """
<p>Sherbekning uyiga toʻrt kishi mehmon kelayotgan edi. U birinchi
marta yolgʻiz oʻzi osh damlamoqchi boʻldi.</p>

<p>Nodira opa unga oilaviy
<span class="cn-word" data-tr="taom tayyorlash tartibi va meʼyorlari">retsept</span>ni
berdi. Retsept <strong>12</strong> kishiga
<span class="cn-word" data-tr="maʼlum miqdorga hisoblangan">moʻljallan</span>gan edi:
<strong>1,5</strong> kg guruch, 900 g goʻsht, 600 g sabzi, 200 ml yogʻ.
Pastida esa yozuv bor edi: «40 daqiqa damlanadi».</p>

<p>Sherbek toʻrt kishiga tayyorlashi kerak, demak hamma
<span class="cn-word" data-tr="oʻlchov nomi: gramm, kilogramm, litr">birlik</span>dagi
<span class="cn-word" data-tr="mahsulotning ogʻirligi yoki hajmi">miqdor</span>ni
uch marta kamaytirish kerak.</p>

<p>U hisoblab, daftarga koʻchirib yozdi. Keyin doʻkonga chiqib ketdi va
roʻyxatni ukasiga qayta yozdirdi.</p>

<p>Doʻkondan qaytgach, roʻyxatga qaradi va toʻxtab qoldi. Birinchi
qatorda shunday yozilgan edi: «<b>guruch — 5 kg</b>».</p>

<p>Bir zum u ikkilandi. Balki toʻgʻridir? Toʻrt kishi — kam emas.</p>

<p>Keyin esiga PM-92 dagi usul tushdi: agar ikkita sonni solishtirib
boʻlmasa, ularni <b>bitta birlikka</b> keltirish kerak. Bu yerda ham
xuddi shunday — faqat bir kishiga toʻgʻri keladigan miqdorni topish
kerak edi.</p>

<p>Retsept boʻyicha: 1,5 kg = <strong>1500</strong>
<span class="cn-word" data-tr="massaning kichik oʻlchov birligi">gramm</span>.
Uni 12 kishiga boʻldi: 1500 ÷ 12 = <strong>125</strong> g. Demak bir
kishiga bir yarim
<span class="cn-word" data-tr="taom solinadigan idish; bu yerda oʻlchov sifatida">kosa</span>cha
guruch — mantiqiy son.</p>

<p>Toʻrt kishiga esa 4 × 125 = <strong>500</strong> g, ya'ni
<strong>0,5</strong>
<span class="cn-word" data-tr="massaning asosiy oʻlchov birligi, 1000 gramm">kilogramm</span>
kerak ekan.</p>

<p>Endi daftardagi yozuvni tekshirdi: 5 kg = 5000 g. Uni toʻrtga
boʻlsa, bir kishiga 5000 ÷ 4 = <strong>1250</strong> g toʻgʻri
kelardi.</p>

<p>Bir kishiga bir yarim kilogrammga yaqin guruch. Bu —
<strong>oʻn</strong> <span class="cn-word" data-tr="necha marta koʻp yoki kam ekanini bildiruvchi soʻz">barobar</span>
koʻp.</p>

<p><span class="cn-word" data-tr="hisobda yoʻl qoʻyilgan notoʻgʻrilik">Xato</span>
topildi. Ukasi «0,5 kg» ni koʻchirayotib
<span class="cn-word" data-tr="butun va kasr qismini ajratuvchi belgi">vergul</span>ni
tushirib qoldirgan ekan — va yarim kilo besh kiloga aylanib
qolgan.</p>

<p>Sherbek daftarga izoh yozib qoʻydi: «<i>Birlikni tekshirishning eng
oson yoʻli — bir kishiga qancha toʻgʻri kelishini hisoblash. Bu sonni
odam oʻz tajribasi bilan solishtira oladi.</i>»</p>

<p>Yana bir narsani payqadi. Retseptdagi «40 daqiqa» degan yozuv
guruch miqdorini hisoblashda umuman kerak boʻlmadi — u
<span class="cn-word" data-tr="savolga kerak boʻlmagan berilgan maʼlumot">ortiqcha maʼlumot</span>
edi. Osh damlashda kerak, hisobda emas.</p>

<p>Osh yaxshi chiqdi. Mehmonlar maqtashdi, biri esa soʻrab qoldi:
«Qaysi retsept boʻyicha qilding?»</p>

<p>«Retsept oʻsha-oʻsha», dedi Sherbek. «Faqat men uni
<span class="cn-word" data-tr="hisob-kitob qilib tekshirmoq">hisoblab</span>
koʻrdim. Agar hisoblamaganimda, hozir hammamiz bir hafta guruch
yegan boʻlardik».</p>
""",
    },
]
