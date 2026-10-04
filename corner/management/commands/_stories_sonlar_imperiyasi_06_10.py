# -*- coding: utf-8 -*-
"""Sonlar imperiyasi — 6-10-qismlar (1-mavsum).

Bible: flowstudio/series/sonlar_imperiyasi.md   Toc: toc_sonlar_imperiyasi.txt
SUBJECT / COLLECTION and the SVG helpers are copied from _01_05.py (the importer
overwrites the shelf's fields, so they must stay identical).
⛔ AUDIO YOʻQ (maths shelf).

FAKTLAR (tekshirilgan):
  • «Ratio» (lotincha) — nisbat; ratsional son = a ÷ b, a va b butun, b ≠ 0.
    Har bir kasr oʻnli kasr koʻrinishida yo tugaydi (1/4 = 0,25), yo davriy
    takrorlanadi (1/3 = 0,333…, 7/3 = 2,333…).
  • √ belgisi: Kristof Rudolf, 1525-yil. 1,41² = 1,9881; 1,414² = 1,999396;
    √2 ≈ 1,41421356. Gippas haqidagi hikoya — rivoyat.
  • Arximed: 3 10/71 < π < 3 1/7. Lambert 1761-yilda π irratsional ekanini
    isbotlagan. π ≈ 3,14159265358.
  • Yakob Bernulli, 1683-yil — murakkab foiz; (1 + 1/n)^n: n=1 → 2; n=2 → 2,25;
    n=12 → ≈2,613; n=365 → ≈2,7146; chegarasi e ≈ 2,71828. «e» harfi — Eyler.
  • i belgisi (√−1 uchun) — Eyler, 1777-yil.

    python manage.py import_corner \\
        corner/management/commands/_stories_sonlar_imperiyasi_06_10.py --author=prime
"""

SUBJECT = {
    "name":    "Matematika",
    "summary": "Matematika: hayotdagi matnlar, atamalar va matematik hikoyalar.",
    "icon":    "bi-calculator",
    "color":   "#f59e0b",
    "order":   7,
}

COLLECTION = {
    "title":       "Sonlar imperiyasi",
    "description": (
        "Qirol Noʻl, egizak Birlar va butun sonlar saltanati haqida kulgili ertak-serial. "
        "Har qismda yangi turdagi son tugʻiladi — chunki eskilari nimanidir uddalay "
        "olmaydi. Ertak — lekin har bir sahna matematik jihatdan toʻgʻri."
    ),
    "order": 2,
}


def _fig(svg, caption):
    return f'<figure class="pm-fig">{svg}<figcaption>{caption}</figcaption></figure>'


def _haqiqatda(*paras):
    body = ''.join(f'<p>{p}</p>' for p in paras)
    return f'<div class="pe-call pe-tip"><span class="pe-call__t">Haqiqatda</span>{body}</div>'


def _keyingi(text):
    return f'<p><em>Keyingi qismda: {text}</em></p>'


STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # 6 — Nisbat xalqi
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "6-qism. Nisbat xalqi",
        "summary": (
            "Sonlar bir-birini boʻlib, butun boʻlmagan natijalarni topadi. Yangi xalq "
            "tugʻiladi, gapdan toʻxtamaydigan Uch tinchitiladi — va bir kechada butun "
            "saltanat ratsional boʻlib qoladi."
        ),
        "order":   6,
        "grammar": [
            {
                "pattern":  "Ratsional son",
                "meaning":  "Ikki butun sonning nisbati sifatida yozish mumkin boʻlgan son: "
                            "a ÷ b, bunda b ≠ 0. Oʻnli kasr koʻrinishida u yo tugaydi, yo "
                            "davriy takrorlanadi. Har bir butun son ham ratsional: 5 = 5/1.",
                "examples": ["7/2 = 3,5 (tugaydi)", "7/3 = 2,333… = 2,(3) (takrorlanadi)",
                             "5 = 5/1"],
            },
        ],
        "questions": [
            {
                "text": "7 ÷ 2 nechaga teng?",
                "choices": ["3", "3,5", "4", "2,333…"],
                "answer": 1,
                "explanation": "7 ÷ 2 = 3 butun va yana yarim: 3½ = 3,5. Natija butun emas — "
                               "shuning uchun u Nisbat xalqidan.",
            },
            {
                "text": "Qirol nima uchun 2,333… ni «tinchitilgan» deb hisobladi?",
                "choices": [
                    "Chunki uning raqamlari tugaydi",
                    "Chunki u butun son",
                    "Chunki u nolga teng",
                    "Chunki unda bitta raqam (3) abadiy takrorlanadi — uni 7/3 yoki 2,(3) deb "
                    "qisqa yozish mumkin",
                ],
                "answer": 3,
                "explanation": "Oʻnli kasr cheksiz boʻlsa ham, takrorlansa — u baribir ikki "
                               "butun son nisbati: 2,333… = 7/3. Demak u ratsional.",
            },
            {
                "text": "Quyidagi sonlarning hammasi ratsional. Qaysi biri butun son?",
                "choices": ["12/4", "1/3", "0,25", "2,(3)"],
                "answer": 0,
                "explanation": "12/4 = 3 — butun son. 1/3 = 0,333…, 0,25 = 1/4, 2,(3) = 7/3 — "
                               "ular butun emas, lekin hammasi ratsional.",
            },
        ],
        "open_question": (
            "1/7 ni oʻnli kasrga aylantirib koʻring: 0,142857142857… Qaysi raqamlar "
            "takrorlanyapti? Nima uchun 7 ga boʻlganda takrorlanuvchi qism 6 tadan uzun "
            "boʻla olmaydi? (Maslahat: qoldiqlarni kuzating.)"
        ),
        "body": """
<p>«÷» oʻyinchoqni olgan sonlar avval ehtiyotkorlik bilan oʻynashdi. Olti uchga
boʻlindi — ikki chiqdi. Sakkiz toʻrtga — yana ikki. Hamma xursand: natija doim
<span class="cn-word" data-tr="kasr qismi yoʻq son: …, −1, 0, 1, 2, …">butun son</span>
— eski tanish!</p>

<p>Keyin Yetti oʻzini ikkiga boʻlib koʻrdi. Natijada… uch butun va yana bir
<em>yarim</em> chiqdi. <strong>7 ÷ 2 = 3½ = 3,5.</strong> Hech kimga oʻxshamaydigan
son! Biri hayron, biri xursand, yana biri oʻziga joy topolmas edi.</p>

<p>Shunday natijalar koʻpaydi: 1 ÷ 4 = 0,25, 3 ÷ 4 = 0,75. Ular ikki son orasidagi
yerlarga — kecha qirol chizgan oraliqlarga — oʻzlari borib joylashishdi va oʻzlarini
<b>Nisbat xalqi</b> deb atashdi:</p>

<p>— Biz ikki butun sonning <span class="cn-word" data-tr="bir sonning ikkinchisiga boʻlinmasi">nisbat</span>idan
yaralganmiz!</p>

<p>Ular «÷» belgisini yotqizib, ustiga bir sonni, ostiga ikkinchisini qoʻyib yozishni
yaxshi koʻrishardi: <strong>¾</strong>. Qirol Noʻl esa bu chiziqni koʻrsa, eti
jimirlab ketardi: axir uning ostiga tushish — oʻsha dahshatli kechaning oʻzi edi.</p>

<p>— Umrbod shu chiziqning <em>kasriga</em> qoldim-a, — deb toʻngʻillardi u.</p>

<p>Shu-shu bu chiziq <span class="cn-word" data-tr="kasrning surat va maxrajini ajratib turuvchi chiziq">kasr chizigʻi</span>
deb ataldi. Qoida esa oʻzgarmadi: chiziq ustida nol tursa mayli (0/5 = 0), lekin
<strong>chiziq ostida — hech qachon</strong>.</p>

<p>Bir kuni muammo chiqdi. Yetti uchga boʻlinmoqchi boʻldi. Natija ikki butun… va
keyin bir Uch gapira boshladi:</p>

<p>— …uch, uch, uch, uch, uch…</p>

<p>Kun botdi. Uch hamon gapirardi. Tong otdi — hamon: «…uch, uch, uch…» Xuddi
<span class="cn-word" data-tr="toʻyni olib boruvchi kishi">tamada</span> mikrofonni
qoʻlidan qoʻymagan toʻydek.</p>

<p>— Kimdir mikrofonni olsin! — yigʻlab yubordi Minusjon.</p>

<p>Qirol Noʻl uch kun quloq solib oʻtirdi va oxiri bir narsani payqadi: Uch boshqa hech
narsa demayapti. Faqat bir xil gapni takrorlayapti. U jilmaydi:</p>

<p>— Xoʻp. Buni <strong>2,(3)</strong> deb yozamiz — qavs ichidagisi abadiy takrorlanadi.
Yoki shunchaki <strong>7/3</strong>. Bas!</p>

<p>Uch nihoyat jim boʻldi. Bu sonlar cheksiz boʻlsa ham —
<span class="cn-word" data-tr="bir xil raqamlar guruhi abadiy qaytariladigan">davriy</span>
edi, yaʼni nazorat ostida edi.</p>

<p>Nisbat xalqi esa kuchaydi. Bir kuni ular ajoyib kashfiyot qilishdi: istalgan butun
sonni kasr chizigʻining ustiga chiqarib, ostiga Birjonni qoʻysa, son oʻzgarmas ekan.
<strong>5 = 5/1. −3 = −3/1. 0 = 0/1.</strong></p>

<p>— Demak, siz ham bizdansiz! — deb eʼlon qilishdi ular butun sonlarga.</p>

<p>Qirol ham, butun sonlar ham eʼtiroz bildira olmadi — matematikaga qarshi chiqib
boʻlmaydi. Shu kechadan boshlab butun saltanat <b>ratsional sonlar</b> saltanati deb
ataldi. Butun sonlar unda faxriy amaldorlar boʻldi, Qirol Noʻl esa uning hurmatli
hukmdori — faqat bitta vaʼda bilan: hech qachon kasr chizigʻi ostiga tushmaslik.</p>

<p>Hamma tinch, hamma xursand edi. Ammo bitta <em>lekin</em> bor edi. Buni hali hech
kim bilmas edi.</p>
""" + _haqiqatda(
            "<b>Ratsional</b> soʻzi lotincha <i>ratio</i> — «nisbat» soʻzidan. Ratsional son — "
            "ikki butun sonning nisbati: <b>a/b</b>, bunda b ≠ 0 (chiziq ostida nol boʻlmaydi — "
            "ertakdagi qonun aynan shu).",
            "Har bir ratsional son oʻnli kasr koʻrinishida yo <b>tugaydi</b> (3/4 = 0,75), yo "
            "<b>davriy takrorlanadi</b> (1/3 = 0,333…). Diqqat: «cheksiz» degani hali "
            "«ratsional emas» degani emas — 2,333… ham ratsional.",
        ) + _keyingi("sonlar kvadrat minoralar va ildiz yertoʻlalarini kashf qiladi. Ikki "
                     "yertoʻlaga tushadi… va chiqa olmaydi."),
    },

    # ══════════════════════════════════════════════════════════════════
    # 7 — Ildiz qafasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "7-qism. Ildiz qafasi",
        "summary": (
            "Sonlar kvadrat minoralarni va ildiz yertoʻlalarini kashf qiladi. Ikki "
            "yertoʻlaga tushib, chiqa olmay qoladi — va sonlar oʻqida teshik borligi "
            "maʼlum boʻladi."
        ),
        "order":   7,
        "grammar": [
            {
                "pattern":  "√2 — ratsional emas",
                "meaning":  "Hech qanday kasrning kvadrati aniq 2 ga teng emas. √2 ning "
                            "raqamlari hech qachon tugamaydi va hech qachon davriy "
                            "takrorlanmaydi. Bunday sonlar irratsional deyiladi.",
                "examples": ["√25 = 5, chunki 5² = 25", "1,41² = 1,9881 — 2 ga yetmaydi",
                             "1,414² = 1,999396 — baribir yetmaydi", "√2 ≈ 1,41421356…"],
            },
        ],
        "questions": [
            {
                "text": "√81 nechaga teng?",
                "choices": ["8", "9", "40,5", "18"],
                "answer": 1,
                "explanation": "9 × 9 = 81, demak √81 = 9. Yertoʻladan bemalol chiqadi.",
            },
            {
                "text": "Tomoni 1 metr boʻlgan kvadrat shaklidagi gilamning diagonali qancha?",
                "choices": ["2 metr", "1 metr", "√2 metr ≈ 1,41 metr", "1,5 metr"],
                "answer": 2,
                "explanation": "Pifagor teoremasi: diagonal² = 1² + 1² = 2, demak diagonal "
                               "= √2 ≈ 1,41 metr. √2 — qafasdagi son, lekin gilamda "
                               "bemalol oʻlchanadigan haqiqiy uzunlik.",
            },
            {
                "text": "Nima uchun qirol manfiy sonlarga ildiz yertoʻlasiga yaqinlashishni "
                        "taqiqladi?",
                "choices": [
                    "Chunki ular juda kichkina",
                    "Chunki hech qanday son oʻziga koʻpaytirilganda manfiy chiqmaydi: "
                    "2 × 2 = 4 va (−2) × (−2) = 4",
                    "Chunki ular sovuqdan qoʻrqadi",
                    "Chunki yertoʻla faqat juft sonlar uchun",
                ],
                "answer": 1,
                "explanation": "Musbat × musbat = musbat, manfiy × manfiy = musbat. Kvadrati "
                               "−4 boʻladigan son oʻqda yoʻq — hozircha…",
            },
        ],
        "open_question": (
            "Kalkulyatorsiz: √2 qaysi ikki butun son orasida? √10 chi? √50 chi? Qaysi "
            "sonlarning ildizi yertoʻladan «bemalol chiqadi»?"
        ),
        "body": """
<p>Ratsional saltanat tinch yashardi — sonlar esa zerikib qolishdi. Ular kim oʻzar
oʻynab, yangi oʻyin oʻylab topishdi: son oʻzini oʻziga koʻpaytirsa, uning ustiga
<span class="cn-word" data-tr="sonning oʻziga koʻpaytmasi: 5² = 5 × 5">kvadrat</span>
minora quriladi. Besh — <strong>5 × 5 = 25</strong> qavatli minora! Oʻn — yuz qavatli!</p>

<p>Keyin teskarisini oʻylab topishdi. Minora tagida yertoʻla bor edi — eshigi «√»
shaklida. Yigirma besh yertoʻlaga tushsa, u yerdan… Besh boʻlib chiqar ekan!
<strong>√25 = 5.</strong> Yuz tushdi — Oʻn chiqdi. Toʻqqiz tushdi — Uch chiqdi. Xalq
qiziqib qoldi: navbat hosil boʻldi, hamma tushib koʻrgisi kelardi. Bu yertoʻlani
<span class="cn-word" data-tr="kvadrati berilgan songa teng boʻlgan son">ildiz</span> deb
atashdi.</p>

<p>Bir kuni navbat <b>Ikki</b>ga keldi. U hech qanday minora ustida turmagan edi —
oddiy Ikki. Lekin juda qiziquvchan edi. «Ichkarida nima bor ekan?» — deb tushib ketdi.</p>

<p>Va chiqa olmadi.</p>

<p>Ikki yertoʻla ichida ancha urindi. Chiqish uchun u bir sonni topishi kerak edi —
kvadrati aniq 2 boʻladigan sonni. Bir — kam: 1 × 1 = 1. Ikki — koʻp: 2 × 2 = 4. Nisbat
xalqidan yordam soʻradi. 1,4 urinib koʻrdi: 1,96 — yetmadi. 1,41: 1,9881. 1,414:
1,999396… Har safar yaqinroq, lekin <strong>hech qachon aniq 2 emas</strong>.</p>

<p>Oxiri u qafasni oʻzi bilan olib chiqdi — √ shaklidagi shisha qafas. Endi uni hamma
<b>Ildiz-Ikki</b> deb chaqirardi. Saroy darvozasida qorovul uni roʻyxatga olmoqchi
boʻldi:</p>

<p>— Ismingiz?</p>

<p>— Bir butun, toʻrt, bir, toʻrt, ikki, bir, uch, besh, olti… — boshladi Ildiz-Ikki.</p>

<p>Kun botdi. Qorovul hamon yozardi. Hech qanday takrorlanish yoʻq — Uchning gapidek
emas.</p>

<p>— Ismim pasportga sigʻmayapti, — xoʻrsindi Ildiz-Ikki.</p>

""" + _fig(
            '<svg viewBox="0 0 220 170" role="img" xmlns="http://www.w3.org/2000/svg">'
            '<rect x="50" y="20" width="120" height="120" class="pm-fill"/>'
            '<rect x="50" y="20" width="120" height="120" class="pm-ln"/>'
            '<path d="M50 140 L170 20" class="pm-ln pm-ln--hl"/>'
            '<text x="110" y="158" text-anchor="middle" class="pm-lbl">1</text>'
            '<text x="36" y="84" text-anchor="middle" class="pm-lbl">1</text>'
            '<text x="122" y="74" class="pm-lbl">√2</text>'
            '</svg>',
            'Tomoni 1 boʻlgan kvadratning diagonali — aynan √2. U haqiqiy uzunlik, lekin '
            'hech qanday kasr emas.') + """

<p>Eng gʻalatisi — Ildiz-Ikki haqiqiy uzunlik edi. Tomoni bir qadam boʻlgan kvadratning
<span class="cn-word" data-tr="koʻpburchakning qoʻshni boʻlmagan uchlarini tutashtiruvchi kesma">diagonal</span>i
— aynan u. Sonlar oʻqida ham uning nuqtasi bor edi: 1,41 bilan 1,42 orasida. Lekin bu
nuqtani <em>hech bir</em> Nisbat xalqi vakili egallamagan edi. Qirol hayratda qoldi:
oʻqda — oraliqdagi yerlar tugamaydi deb oʻylagan oʻqda —
<strong>teshiklar</strong> bor ekan!</p>

<p>Ratsional xalq Ildiz-Ikkini tanimadi. «Biz nisbatdan yaralganmiz, sen-chi?» Qirol
Noʻl ham choʻchib qoldi va ogʻir qaror chiqardi: qafasdagi sonlar saltanatdan
<span class="cn-word" data-tr="vatanidan majburan chiqarib yuborilgan">badargʻa</span>
qilinsin. Ortidan √3, √5, √7 ham ketdi. Yana bir qonun qoʻshildi: manfiy sonlar ildiz
yertoʻlasiga yaqin ham yoʻlamasin — chunki 2 × 2 = 4, (−2) × (−2) ham 4, kvadrati
manfiy boʻladigan son saltanatda yoʻq edi.</p>

<p>Badargʻa qilinganlar olis-olislarga ketishdi — sonlar oʻqidagi oʻsha teshiklarga. Va
u yerda, qorongʻida, ular bir-biri bilan gaplasha boshlashdi.</p>
""" + _haqiqatda(
            "√ belgisini 1525-yilda nemis matematigi <b>Kristof Rudolf</b> kitobida "
            "ishlatgan.",
            "Qadimgi yunonlar uchun √2 katta zarba boʻlgan. <b>Rivoyatga koʻra</b>, Pifagor "
            "maktabidan <b>Gippas</b> bu sirni oshkor qilgani uchun jamoadan haydalgan.",
            "Nima uchun √2 kasr emas? Faraz qilaylik, √2 = a/b va bu kasrni qisqartirib "
            "boʻlmaydi. Unda a² = 2b², demak a juft. a = 2k desak, 4k² = 2b², b² = 2k² — demak "
            "b ham juft. Ikkalasi juft boʻlsa, kasr qisqarardi! Qarama-qarshilik. Demak "
            "<b>√2 ≈ 1,41421356…</b> — irratsional.",
        ) + _keyingi("saltanatdagi har bir gʻildirak, lagan va gumbaz bitta sirni yashirib "
                     "yuradi. Uni bilgan yagona olim keladi."),
    },

    # ══════════════════════════════════════════════════════════════════
    # 8 — Doiraning siri
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "8-qism. Doiraning siri",
        "summary": (
            "Saltanatdagi har bir gʻildirak va lagan bitta sirni yashiradi. Uni olim Pi "
            "biladi — lekin gapini hech qachon tugatolmaydi."
        ),
        "order":   8,
        "grammar": [
            {
                "pattern":  "π — doiraning nisbati",
                "meaning":  "Har qanday aylananing uzunligi diametridan π marta katta. "
                            "π ≈ 3,14159… — u ikki butun sonning nisbati sifatida yozilmaydi, "
                            "raqamlari tugamaydi va takrorlanmaydi.",
                "examples": ["aylana uzunligi = π × diametr", "diametri 2 m → ≈ 6,28 m",
                             "22/7 = 3,1428… — π ga yaqin, lekin π emas"],
            },
        ],
        "questions": [
            {
                "text": "Diametri 40 sm boʻlgan laganning aylanasi taxminan qancha? (π ≈ 3,14)",
                "choices": ["43,14 sm", "80 sm", "125,6 sm", "160 sm"],
                "answer": 2,
                "explanation": "Aylana uzunligi = π × diametr ≈ 3,14 × 40 = 125,6 sm.",
            },
            {
                "text": "Pi nima uchun «ismim nisbatdan, lekin men Nisbat xalqidan emasman» "
                        "deydi?",
                "choices": [
                    "Chunki u aylananing diametriga nisbati, lekin uni hech qachon ikki butun "
                    "sonning nisbati sifatida yozib boʻlmaydi",
                    "Chunki u juda katta son",
                    "Chunki u manfiy",
                    "Chunki u 22/7 ga aniq teng",
                ],
                "answer": 0,
                "explanation": "π = aylana ÷ diametr, lekin u a/b koʻrinishidagi kasr emas — "
                               "irratsional. 22/7 faqat taxminiy qiymat.",
            },
        ],
        "open_question": (
            "Uyingizdagi biror dumaloq narsani (piyola, likopcha) ip bilan aylantirib "
            "oʻlchang, keyin diametrini oʻlchang. Bir-biriga boʻling. Qancha chiqdi? Nega "
            "aniq 3,14159… chiqmaydi?"
        ),
        "body": """
<p>Ratsional saltanatda hamma narsa aniq edi. Faqat bitta narsa sonlarni hayron
qoldirardi: <b>dumaloq</b> narsalar.</p>

<p>Gʻildirakchi usta gʻildirak gardishini ip bilan oʻlchadi, keyin uning eni —
<span class="cn-word" data-tr="aylananing markazidan oʻtib, ikki chetini tutashtiruvchi kesma">diametr</span>ini.
Ipni enga solishtirsa — uch marta sigʻar, yana ozgina ortib qolardi. Laganni
oʻlchashdi — yana uch martadan sal koʻproq. Tandir ogʻzini, masjid gumbazini — har
safar oʻsha: <strong>uchdan sal koʻproq</strong>. Katta-kichikligidan qatʼi nazar!</p>

""" + _fig(
            '<svg viewBox="0 0 220 170" role="img" xmlns="http://www.w3.org/2000/svg">'
            '<circle cx="110" cy="80" r="62" class="pm-fill"/>'
            '<circle cx="110" cy="80" r="62" class="pm-ln pm-ln--hl"/>'
            '<path d="M48 80 L172 80" class="pm-ln"/>'
            '<text x="110" y="72" text-anchor="middle" class="pm-lbl">diametr</text>'
            '<text x="110" y="162" text-anchor="middle" class="pm-lbl">aylana ÷ diametr = π</text>'
            '</svg>',
            'Har qanday doirada aylana uzunligini diametrga boʻlsangiz — doim bir xil son '
            'chiqadi.') + """

<p>Nisbat xalqi bu sonni qoʻlga olmoqchi boʻldi: «Bu nisbat-ku! Demak bizdan!» Ular
3 ni sinadi — kam. 22/7 ni sinadi — juda yaqin, lekin sal koʻp. 355/113 ni — yanada
yaqinroq… lekin baribir aniq emas.</p>

<p>Shunda saroyga uzoq yoʻldan bir keksa olim kirib keldi. Egnida doira naqshli
chopon, qoʻlida oʻlchov ipi. Uning ismi <b>Pi</b> edi. U butun umr dunyodagi har bir
<span class="cn-word" data-tr="markazdan bir xil uzoqlikdagi nuqtalardan iborat egri chiziq">aylana</span>ni
oʻlchab chiqqan ekan.</p>

<p>— Doiraning sirini bilasizmi? — soʻradi qirol.</p>

<p>Pi tomogʻini qirib, boshladi:</p>

<p>— Doiraning sirini aytsam… uch butun, bir, toʻrt, bir, besh, toʻqqiz, ikki, olti, besh,
uch, besh, sakkiz…</p>

<p>Birinchi soatda Minusjon esnadi. Ikkinchi soatda saroy qorovuli uxlab qoldi. Tong
otganda butun saroy xurrak otardi — Pi esa hamon sanar edi: «…toʻqqiz, yetti, toʻqqiz,
uch…»</p>

<p>Uyqudan turgan qirol undan soʻradi:</p>

<p>— Hech boʻlmasa, takrorlanadimi? Uchning gapidek?</p>

<p>— Yoʻq, hazratim. Hech qachon takrorlanmaydi. Hech qachon tugamaydi.</p>

<p>Nisbat xalqi hayratda qoldi:</p>

<p>— Lekin sen aylananing diametrga <em>nisbati</em>san-ku!</p>

<p>Pi gʻamgin jilmaydi:</p>

<p>— Ismim nisbatdan, lekin men Nisbat xalqidan emasman. Meni hech qachon ikki butun
sonning nisbati qilib yozib boʻlmaydi.</p>

<p>Saroyda jimjitlik choʻkdi. Qirol Noʻl qonunga sodiq edi: kasr sifatida yozilmaydigan
son ratsional saltanatda yashay olmaydi. Pi taʼzim qildi va oʻqdagi teshiklar tomon
yoʻlga chiqdi — u yerda uni Ildiz-Ikki va badargʻa qilinganlar kutib turardi. Bilimli,
sabrli, hech narsadan qoʻrqmaydigan olim ularga
<span class="cn-word" data-tr="hukmdorning bosh maslahatchisi">vazir</span> boʻldi.</p>
""" + _haqiqatda(
            "π ni eng aniq hisoblaganlardan biri — <b>Arximed</b> (miloddan avvalgi III asr). "
            "U π ni ikki kasr orasiga «qamagan»: <b>3 10/71 &lt; π &lt; 3 1/7</b>, yaʼni "
            "3,1408 bilan 3,1429 orasida.",
            "π ning irratsional ekanini — hech qanday kasrga teng emasligini — 1761-yilda "
            "<b>Iogann Lambert</b> isbotlagan. Bugun kompyuterlar uning trillionlab "
            "raqamlarini hisoblagan, lekin takrorlanish topilmagan va topilmaydi ham.",
        ) + _keyingi("badargʻa qilinganlar oʻz xonligiga asos soladi. Ularning orasida hamyoni "
                     "oʻz-oʻzidan kattalashadigan bir savdogar ham bor…"),
    },

    # ══════════════════════════════════════════════════════════════════
    # 9 — Irratsional xonlik
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "9-qism. Irratsional xonlik",
        "summary": (
            "Badargʻa qilinganlar sonlar oʻqidagi teshiklarda oʻz xonligini quradi. "
            "Elchi Pi qirol huzuriga keladi — savdogar E esa muzokarani buzib qoʻyadi."
        ),
        "order":   9,
        "grammar": [
            {
                "pattern":  "e — oʻsishning soni",
                "meaning":  "Agar pul yiliga 100% foiz bilan oʻssa va foiz tobora tez-tez "
                            "qoʻshib borilsa, natija oshib boradi, lekin hech qachon "
                            "e ≈ 2,71828… dan oshmaydi. e ham irratsional.",
                "examples": ["yiliga bir marta: 2", "yarim yilda bir marta: 2,25",
                             "har oy: ≈ 2,613", "har kuni: ≈ 2,7146"],
            },
        ],
        "questions": [
            {
                "text": "1 soʻm yiliga 100% foiz bilan, lekin foiz har yarim yilda (50% dan) "
                        "qoʻshiladi. Yil oxirida qancha boʻladi?",
                "choices": ["2 soʻm", "2,25 soʻm", "1,5 soʻm", "3 soʻm"],
                "answer": 1,
                "explanation": "Yarim yilda: 1 × 1,5 = 1,5. Yil oxirida: 1,5 × 1,5 = 2,25. "
                               "Foiz ustiga foiz!",
            },
            {
                "text": "Irratsional xonlikda kimlar bor?",
                "choices": [
                    "Faqat manfiy sonlar",
                    "Butun sonlar va kasrlar",
                    "Kasr sifatida yozib boʻlmaydigan sonlar: √2, √3, π, e …",
                    "Faqat nol",
                ],
                "answer": 2,
                "explanation": "Irratsional — «nisbat emas». Ularning oʻnli yozuvi tugamaydi "
                               "va takrorlanmaydi.",
            },
        ],
        "open_question": (
            "Agar foiz har soatda, har daqiqada, har soniyada qoʻshilsa, 1 soʻm yil oxirida "
            "3 soʻmga yeta oladimi? Nima uchun E «hech qachon 2,72 dan oshmayman» deydi?"
        ),
        "body": """
<p>Sonlar oʻqidagi teshiklar uzoqdan qaraganda boʻm-boʻsh koʻrinardi. Aslida esa ular
gavjum edi. U yerda badargʻa qilinganlar yashardi: Ildiz-Ikki, √3, √5, √7… Ular bir-biriga
umuman oʻxshamas edi. Birining raqamlari uzun, birining yana-da uzunroq — hech birida
takrorlanish yoʻq. Lekin ularda bir umumiy narsa bor edi: ularning yoʻqotadigan hech
narsasi qolmagan edi.</p>

<p>Bir kuni Ildiz-Ikki hammani yigʻdi:</p>

<p>— Endi bizning navbatimiz keldi. Bizning ham oʻqda joyimiz bor — biz oʻsha teshiklarning
oʻzimiz. Biz ham uzunlikmiz: kvadratning diagonali, doiraning aylanasi.</p>

<p>Ular yangi davlatga asos solishdi —
<b><span class="cn-word" data-tr="ikki butun sonning nisbati sifatida yozib boʻlmaydigan">Irratsional</span>
xonlik</b>. Ildiz-Ikki — xon, Pi — vazir.</p>

<p>Xonlikda yana bir gʻalati aholi bor edi: savdogar <b>E</b>. Uning hamyoni oʻz-oʻzidan
kattalashardi. Siri oddiy edi — <span class="cn-word" data-tr="foiz nafaqat asosiy pulga, balki oldin qoʻshilgan foizga ham hisoblanishi">murakkab foiz</span>:</p>

<p>— Bir soʻmni yiliga yuz foizga qoʻyasiz — yil oxirida ikki soʻm. Foizni yarim yilda
bir qoʻshsangiz — <strong>2,25</strong>. Har oy qoʻshsangiz — <strong>2,61</strong>.
Har kuni — <strong>2,71</strong>! Foiz ustiga foiz — boylik shu!</p>

<p>— Har soniyada qoʻshsak-chi? — soʻradi kimdir.</p>

<p>E bir zum jim qoldi.</p>

<p>— Unda ham… <strong>2,71828</strong>-ga yaqin. Undan oshmaydi. Hech qachon. Bu — mening
ismim. Raqamlarim ham tugamaydi, takrorlanmaydi.</p>

<p>Xonlik elchi yubordi. Elchi, albatta, Pi edi. U ratsional saltanatga kirib kelib,
Qirol Noʻlga taʼzim qildi:</p>

<p>— Hazratim! Biz ham <strong>haqiqiy</strong> sonlarmiz. Sonlar oʻqida bizning nuqtalarimiz
bor. Gilamning diagonali, gʻildirakning aylanasi — biz. Bizni tan oling. Talablarimiz
bor-yoʻgʻi uch… bir, toʻrt, bir, besh, toʻqqiz…</p>

<p>— Qisqasini ayting! — yalindi qirol.</p>

<p>Shu payt eshikdan E kirib keldi:</p>

<p>— Hazratim, muzokara ham ketaversin, sizga ajoyib taklifim bor: xazinangizni menga
bering, foiz ustiga foiz…</p>

<p>— Keyin! — deb qichqirishdi Pi ham, qirol ham.</p>

<p>Saroy kulgidan larzaga keldi. Lekin keyin jim boʻldi. Hamma qirolga qarab turardi.
Qirol Noʻl oʻylanib qoldi. Uning oldida eng qiyin savol turardi: bu nisbatga
sigʻmaydigan, qafasli, gapi tugamaydigan sonlar — <em>haqiqiy</em>mi?</p>
""" + _haqiqatda(
            "Murakkab foiz haqidagi savolni 1683-yilda shveytsariyalik matematik <b>Yakob "
            "Bernulli</b> oʻrgangan: foiz qanchalik tez-tez qoʻshilsa, natija oshadi, lekin "
            "bir chegaraga yaqinlashadi — <b>e ≈ 2,71828…</b>. Bu songa «e» harfini "
            "<b>Leonard Eyler</b> bergan.",
            "Bu mavzu haqida «Matematika olami» javonidagi «Foiz ustiga foiz: pul qanday "
            "oʻsadi» matnini ham oʻqing.",
        ) + _keyingi("Qirol Noʻl qarorini aytadi. Va saltanat tarixidagi eng katta bayram "
                     "boshlanadi."),
    },

    # ══════════════════════════════════════════════════════════════════
    # 10 — Haqiqiy sonlar imperiyasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "10-qism. Haqiqiy sonlar imperiyasi",
        "summary": (
            "Qirol Noʻl qarorini aytadi: ratsional va irratsional sonlar birlashib, Haqiqiy "
            "sonlar imperiyasiga asos soladi. Lekin kechasi oʻqdan tashqaridan bir ovoz "
            "eshitiladi…"
        ),
        "order":   10,
        "grammar": [
            {
                "pattern":  "Haqiqiy sonlar",
                "meaning":  "Ratsional va irratsional sonlar birgalikda haqiqiy sonlarni "
                            "tashkil qiladi. Sonlar oʻqidagi har bir nuqta — bitta haqiqiy son; "
                            "oʻqda boshqa teshik qolmaydi.",
                "examples": ["ratsional: −3, 0, ½, 2,(3)", "irratsional: √2, π, e",
                             "hammasi — haqiqiy sonlar"],
            },
        ],
        "questions": [
            {
                "text": "Quyidagilardan qaysi biri irratsional?",
                "choices": ["0,5", "2,(3)", "√2", "−7"],
                "answer": 2,
                "explanation": "0,5 = 1/2, 2,(3) = 7/3, −7 = −7/1 — hammasi ratsional. √2 ni "
                               "esa kasr qilib yozib boʻlmaydi.",
            },
            {
                "text": "Imperiyada Qirol Noʻlning oʻrni qanday?",
                "choices": [
                    "U endi hukmdor emas, lekin oʻqning markazida turadi va uni hamma hurmat "
                    "qiladi",
                    "U imperiyadan haydalgan",
                    "U irratsional xonlikning xoni",
                    "U kasr chizigʻi ostida yashaydi",
                ],
                "answer": 0,
                "explanation": "Nol — sonlar oʻqining markazi: musbat va manfiylar orasidagi "
                               "chegara. Ertakda u hukmronlik qilmaydi, lekin hamma narsa "
                               "undan boshlangan.",
            },
            {
                "text": "Kechasi kelgan ovoz «√(−1)» deydi. Nega u sonlar oʻqida joy topa "
                        "olmaydi?",
                "choices": [
                    "Chunki u juda katta",
                    "Chunki u ratsional",
                    "Chunki u juft",
                    "Chunki kvadrati −1 boʻladigan haqiqiy son yoʻq: musbat ham, manfiy ham "
                    "kvadratda musbat beradi",
                ],
                "answer": 3,
                "explanation": "1 × 1 = 1 va (−1) × (−1) = 1. Kvadrati −1 boʻladigan son "
                               "oʻqda yoʻq — u uchun yangi oʻq kerak. 2-mavsumda!",
            },
        ],
        "open_question": (
            "Agar √(−1) sonlar oʻqida yashay olmasa, u qayerda yashashi mumkin? Oʻqning "
            "tepasida va pastida yana bitta oʻq chizsak nima boʻladi?"
        ),
        "body": """
<p>Qirol Noʻl uch kecha uxlamadi. Toʻrtinchi kuni ertalab u saroy maydoniga chiqib,
ikki xalqni — ratsional saltanatni va irratsional xonlikni — bir joyga chaqirdi.</p>

<p>— Men koʻp oʻyladim, — dedi u. — Sizlarning har biringiz sonlar oʻqida turasiz.
Ratsional sonlar — tekis, chiroyli, aniq. Irratsional sonlar — tugamaydigan, gʻalati,
lekin sabrli va qoʻrqmas. Bir-birisiz esa oʻqda teshiklar qoladi. Siz
<strong>ikkalangiz ham haqiqiysiz</strong>.</p>

<p>Maydonda bir lahza jimlik choʻkdi. Keyin olqish yangradi. Ildiz-Ikki qafasini birinchi
marta faxr bilan koʻtardi. Pi «rahmat» demoqchi edi — «uch butun, bir, toʻrt…» deb
boshladi, lekin uni bu safar mehr bilan toʻxtatishdi.</p>

<p>Shu kuni ikki davlat birlashib, yangi imperiyaga asos soldi —
<b><span class="cn-word" data-tr="ratsional va irratsional sonlarning hammasi">Haqiqiy sonlar</span>
imperiyasi</b>. Uning yeri — qirolning eski tayogʻi, endi esa butun
<span class="cn-word" data-tr="har bir nuqtasi bitta haqiqiy songa mos keladigan toʻgʻri chiziq">sonlar oʻqi</span>.
Har bir nuqtada — bitta son. Kasrlar orasidagi teshiklarda — irratsionallar. Oʻqda
birorta ham boʻsh joy qolmadi.</p>

""" + _fig(
            '<svg viewBox="0 0 340 90" role="img" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M10 40 L330 40" class="pm-ln pm-ln--hl"/>'
            + ''.join(
                f'<path d="M{x} 33 L{x} 47" class="pm-ln"/>'
                f'<text x="{x}" y="66" text-anchor="middle" class="pm-lbl">{t}</text>'
                for x, t in [(50, '−2'), (130, '0'), (150, '½'), (187, '√2'),
                             (210, '2'), (239, 'e'), (256, 'π')])
            + '</svg>',
            'Haqiqiy sonlar oʻqi: butunlar, kasrlar va irratsionallar yonma-yon. Hech qanday '
            'teshik yoʻq.') + """

<p>Qirol Noʻl endi hukmdor emas edi. Imperiyani sonlarning oʻzlari boshqarardi. Lekin u
oʻqning qoq markazida turardi — musbatlar bilan manfiylar oʻrtasida, hamma narsa
boshlangan joyda. Va uni hamma hurmat qilardi: birorta son undan oʻtmay turib, bir
tomondan ikkinchisiga oʻta olmasdi.</p>

<p>Kechqurun katta toʻy boʻldi. Qozonlarda osh damlandi — har bir songa bir lagandan. E
oshning narxini foiz ustiga foiz bilan hisoblamoqchi boʻldi, uni stoldan uzoqroqqa
oʻtqazishdi. Uch mikrofonni yana qoʻlga oldi — bu safar hamma unga qoʻshilib kuyladi:
«…uch, uch, uch!» Birjon bilan Minusjon esa xursandchilikdan quchoqlashib ketishdi —
<strong>puf!</strong></p>

<p>— Yana-ya?! — deb kulib yubordi butun imperiya.</p>

<p>Yarim tunda hamma uxlaganda, qirol yolgʻiz oʻqning markazida osmonga qarab turardi. U
baxtli edi. Imperiyada hamma uchun joy bor edi.</p>

<p>Shunda <em>tepadan</em> — oʻqning ustidan, hech qanday son yashamaydigan joydan — ingichka
bir ovoz eshitildi:</p>

<p>— Kechirasiz… men √(−1)man. Meni ham qabul qilasizlarmi?</p>

<p>Qirol Noʻl seskanib ketdi. Oʻqning ustidan? Axir oʻqdan tashqarida hech narsa yoʻq-ku…
Yoki bor?</p>

<p><strong>1-mavsum tugadi.</strong></p>
""" + _haqiqatda(
            "Matematikada <b>haqiqiy sonlar</b> — ratsional va irratsional sonlarning "
            "hammasi. Ular sonlar oʻqini butunlay toʻldiradi: oʻqdagi har bir nuqtaga aynan "
            "bitta haqiqiy son mos keladi.",
            "Kvadrati −1 ga teng son haqiqiy sonlar orasida yoʻq. Lekin matematiklar uni "
            "baribir kiritishdi va <b>i</b> deb belgilashdi (bu belgini 1777-yilda Leonard "
            "Eyler ishlatgan). U uchun sonlar oʻqiga tik yana bir oʻq chiziladi — buni "
            "<b>2-mavsumda</b> koʻramiz.",
        ),
    },
]
