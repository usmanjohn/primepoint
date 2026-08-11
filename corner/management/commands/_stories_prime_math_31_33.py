# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-31 … PM-33.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 31 — sharh (internet tariflari), 32 — hikoya (ombor),
33 — hikoya (kutubxona; oldingisidan boshqa sahna va boshqa ohang).

⚠️ Kumulyativ: 31-matnda ifodalar faqat HISOBLANADI (ixchamlash PM-32 da);
   32-matnda qavs yoʻq (PM-33); 33-matnda tenglama yechilmaydi (PM-36).

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_31_33.py --author=prime
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
    # PM-31 — oʻrniga qoʻyish                                   SHARH
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Qaysi tarif arzon?",
        "summary": (
            "PM-31 matni. Sharh: ikki internet tarifi ifodaga aylantiriladi va "
            "har xil sarf uchun hisoblab koʻriladi. Javob «qancha internet "
            "ishlatasiz» degan savolga bogʻliq chiqadi."
        ),
        "order":   31,
        "grammar": [
            {
                "pattern":  "Ifodaning qiymatini topish — harf oʻrniga son",
                "meaning":  "Ifoda javob emas, retsept. Harf oʻrniga aniq son "
                            "qoʻyilganda u oddiy arifmetikaga aylanadi. Bir necha "
                            "qiymatni hisoblab jadval tuzsak, ifodalarni "
                            "taqqoslash mumkin boʻladi.",
                "examples": [
                    "40 000 + 6000g, g = 5 → 40 000 + 30 000 = 70 000",
                    "70 000 + 3000g, g = 5 → 70 000 + 15 000 = 85 000",
                ],
            },
        ],
        "questions": [
            {
                "text": "Muallifning xulosasi qanday?",
                "choices": [
                    "Qaysi biri arzonligi sarfga bogʻliq",
                    "«Keng» har doim arzonroq",
                    "«Oddiy» har doim arzonroq",
                    "Ikkala tarif ham bir xil pul chiqaradi",
                ],
                "answer": 0,
                "explanation": "Oz internet ishlatadiganga «Oddiy», koʻp "
                               "ishlatadiganga «Keng» arzon tushadi. Oʻn "
                               "gigabaytda ikkalasi teng.",
            },
            {
                "text": "«Oddiy» tarifda 5 gigabayt ishlatilsa, toʻlov qancha?",
                "choices": ["30 000 soʻm", "46 000 soʻm", "70 000 soʻm",
                            "85 000 soʻm"],
                "answer": 2,
                "explanation": "40 000 + 6000 × 5 = 40 000 + 30 000 = 70 000 soʻm.",
            },
            {
                "text": "Necha gigabaytda ikkala tarif bir xil pul chiqaradi?",
                "choices": ["5 GB", "8 GB", "10 GB", "15 GB"],
                "answer": 2,
                "explanation": "10 GB da: 40 000 + 60 000 = 100 000 va "
                               "70 000 + 30 000 = 100 000. Undan kam ishlatsangiz "
                               "«Oddiy», koʻp ishlatsangiz «Keng» arzon.",
            },
        ],
        "body": """
<p><b>Sharh: ikki internet tarifi.</b> Aloqa kompaniyasi ikkita reja taklif qilyapti
va ikkalasi ham «eng foydali» deb reklama qilinyapti. Tekshirib koʻramiz.</p>

<p>«Oddiy» rejasi: oyiga <strong>40 000</strong> soʻm, ustiga har bir gigabayt uchun
<strong>6000</strong> soʻm. «Keng» rejasi: oyiga <strong>70 000</strong> soʻm, har
gigabayt esa atigi <strong>3000</strong> soʻm.</p>

<p>Ikkalasini <span class="cn-word" data-tr="harf, son va amallardan tuzilgan yozuv">ifoda</span>ga
aylantiramiz. Sarflangan gigabaytni <b>g</b> bilan belgilaymiz. «Oddiy»:
<strong>40 000 + 6000g</strong>. «Keng»: <strong>70 000 + 3000g</strong>.</p>

<p>Endi <span class="cn-word" data-tr="harf oʻrniga aniq son yozish">oʻrniga qoʻyish</span>
bilan hisoblaymiz. <b>5 gigabayt:</b> «Oddiy» 70 000, «Keng» 85 000 soʻm.
<b>10 gigabayt:</b> «Oddiy» 100 000, «Keng» ham 100 000 —
<span class="cn-word" data-tr="ikki hisob bir xil natija beradigan qiymat">teng nuqta</span>.
<b>15 gigabayt:</b> «Oddiy» 130 000, «Keng» 115 000 soʻm.</p>

<p>Natijalarni <span class="cn-word" data-tr="ifodaning bir necha qiymati yozilgan jadval">qiymatlar jadvali</span>ga
yozsangiz, manzara darrov koʻrinadi: chiziq oʻn gigabaytda kesishadi.</p>

<p>Sabab <span class="cn-word" data-tr="harf oldidagi son">koeffitsient</span>da.
«Keng» boshida koʻproq oladi, lekin har gigabayti ikki barobar arzon. Sarf oshgan
sari shu farq katta boʻlib boradi.</p>

<p>Demak «qaysi tarif arzon?» degan savolning yagona javobi yoʻq. Toʻgʻri savol
boshqacha: <b>siz oyiga qancha internet ishlatasiz?</b> Oxirgi uch oyning hisobiga
qarang, oʻrtachasini oling va ikkala
<span class="cn-word" data-tr="hisoblab chiqilgan natija">qiymat</span>ni oʻzingiz
chiqaring.</p>

<p>Reklama sizga son aytadi. Ifoda esa qaysi son sizniki ekanini aytadi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-32 — oʻxshash hadlar                                  HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Omborni tartibga solish",
        "summary": (
            "PM-32 matni. Hikoya: Karim akaning omboridagi chalkash roʻyxat "
            "oʻxshash hadlarni yigʻish yoʻli bilan tartibga solinadi va uzun "
            "hisob qisqa ifodaga aylanadi."
        ),
        "order":   32,
        "grammar": [
            {
                "pattern":  "Oʻxshash hadlar — harf qismi bir xil hadlar",
                "meaning":  "Ularni qoʻshganda koeffitsientlar qoʻshiladi, harf "
                            "qismi oʻzgarmaydi. Har xil harfli hadlarni birga "
                            "qoʻshib boʻlmaydi — quti bilan qopni qoʻshgandek.",
                "examples": [
                    "5a + 3b − 2a − b + 4a = 7a + 2b",
                    "a = 15, b = 50 → 7 × 15 + 2 × 50 = 205 kg",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sanjar nima uchun xato qildi deb oʻyladi?",
                "choices": [
                    "Roʻyxatdagi sonlarni notoʻgʻri yozgani uchun",
                    "Hammasini bitta songa qoʻshib yuborgani uchun",
                    "Omborga kech kelgani uchun",
                    "Tarozini ishlatmagani uchun",
                ],
                "answer": 1,
                "explanation": "Sanjar quti va qoplarni aralashtirib «toʻqqiz» deb "
                               "yozdi. Ular har xil narsa — ularni qoʻshib bitta "
                               "son qilib boʻlmaydi.",
            },
            {
                "text": "5 quti, 3 qop, minus 2 quti, minus 1 qop, plyus 4 quti — "
                        "ixchamlansa nima chiqadi?",
                "choices": ["7a + 2b", "9a + 4b", "11a + 4b", "7a + 4b"],
                "answer": 0,
                "explanation": "Qutilar: 5 − 2 + 4 = 7; qoplar: 3 − 1 = 2. Demak "
                               "7a + 2b.",
            },
            {
                "text": "Quti 15 kg, qop 50 kg boʻlsa, omborda necha kilogramm un "
                        "qoldi?",
                "choices": ["155 kg", "175 kg", "205 kg", "255 kg"],
                "answer": 2,
                "explanation": "7 × 15 = 105 va 2 × 50 = 100; jami 205 kg.",
            },
        ],
        "body": """
<p>Karim akaning omborida un ikki xil idishda saqlanadi: quti va qop. Har bir idishning ogʻirligi <span class="cn-word" data-tr="sonning oʻrnida turuvchi nom">harf</span> bilan belgilangan. Bitta qutida
<b>a</b> kilogramm, bitta qopda <b>b</b> kilogramm.</p>

<p>Shanba kuni yangi yordamchi Sanjar hisob yuritdi. Ertalab omborga <strong>5 quti</strong>
va <strong>3 qop</strong> keldi. Tushda <strong>2 quti</strong> va <strong>1 qop</strong>
sotildi. Kechqurun yana <strong>4 quti</strong> keltirildi.</p>

<p>Sanjar daftariga shunday yozdi: «5 + 3 − 2 − 1 + 4 = 9». Karim aka daftarga qaradi
va kuldi.</p>

<p>— Toʻqqizta nima? Quti sonini qop soni bilan qoʻshib yubording. Ular
<span class="cn-word" data-tr="har xil oʻlcham yoki turdagi narsalar">har xil narsa</span>
— bittasi oʻn besh kilo, ikkinchisi ellik.</p>

<p>Karim aka roʻyxatni qaytadan yozdi, har bir sonning yoniga oʻz harfini qoʻyib:
<strong>5a + 3b − 2a − b + 4a</strong>. Sotilgani minus bilan yozildi, chunki
<span class="cn-word" data-tr="hadning plyus yoki minusi">ishora</span> hadning oʻziga
tegishli.</p>

<p>— Endi <span class="cn-word" data-tr="harf qismi bir xil boʻlgan hadlar">oʻxshash hadlar</span>ni
yigʻamiz, — dedi u. — Qutilar: 5 − 2 + 4 = <strong>7</strong>. Qoplar:
3 − 1 = <strong>2</strong>.</p>

<p>Uzun roʻyxat qisqa yozuvga aylandi: <strong>7a + 2b</strong>. Bu
<span class="cn-word" data-tr="oʻxshash hadlarni qoʻshib yozuvni qisqartirish">ixchamlash</span>
deyilarkan.</p>

<p>— Quti oʻn besh kilo, qop ellik kilo, — dedi Karim aka. — Endi hisobla.</p>

<p>Sanjar <span class="cn-word" data-tr="harf oʻrniga son yozish">oʻrniga qoʻydi</span>:
7 × 15 = 105 va 2 × 50 = 100. Omborda <strong>205 kilogramm</strong> un bor edi.</p>

<p>— Bir narsani esda tut, — dedi Karim aka eshikni yopayotib. — Qoʻshishdan oldin
nimani qoʻshayotganingga qara. Ombor ham, daftar ham shu qoidada turadi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-33 — qavs ochish                                      HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Toʻrt qutida nechta?",
        "summary": (
            "PM-33 matni. Hikoya: kutubxonaga kelgan toʻrtta bir xil paketni ikki "
            "oʻquvchi ikki xil yoʻl bilan sanaydi va bir xil javob chiqadi — "
            "taqsimot qonuni shu yerda koʻrinadi."
        ),
        "order":   33,
        "grammar": [
            {
                "pattern":  "Taqsimot qonuni: a(b + c) = ab + ac",
                "meaning":  "Qavs oldidagi koʻpaytuvchi ichkaridagi har bir hadga "
                            "tarqaladi. Shuning uchun bir xil miqdorni ikki xil "
                            "yoʻl bilan sanash mumkin va natija bir xil chiqadi.",
                "examples": [
                    "4(n + 3) = 4n + 12",
                    "n = 12 → 4 × 15 = 60 va 48 + 12 = 60",
                ],
            },
        ],
        "questions": [
            {
                "text": "Afsona bilan Jasur nima uchun bahslashdi?",
                "choices": [
                    "Paketlarni kim ochishi haqida",
                    "Narsalarni sanashning qaysi yoʻli toʻgʻri ekani haqida",
                    "Kitoblarni qaysi javonga qoʻyish haqida",
                    "Kutubxona necha soatda yopilishi haqida",
                ],
                "answer": 1,
                "explanation": "Har biri boshqacha sanadi va ikkalasi ham oʻzini "
                               "haq deb oʻyladi. Aslida ikkala yoʻl ham toʻgʻri edi.",
            },
            {
                "text": "Har paketda 12 ta kitob va 3 ta daftar boʻlsa, toʻrt paketda "
                        "jami nechta narsa bor?",
                "choices": ["48 ta", "51 ta", "60 ta", "63 ta"],
                "answer": 2,
                "explanation": "Har paketda 12 + 3 = 15 ta; toʻrt paketda "
                               "4 × 15 = 60 ta. Yoki 4n + 12 = 48 + 12 = 60.",
            },
            {
                "text": "Kutubxonachi ikkita kitobni olib qoʻygach, nechta narsa "
                        "qoldi?",
                "choices": ["56 ta", "57 ta", "58 ta", "59 ta"],
                "answer": 2,
                "explanation": "60 − 2 = 58 ta. Ifoda bilan: 4n + 12 − 2 = 4n + 10, "
                               "n = 12 da 48 + 10 = 58.",
            },
        ],
        "body": """
<p>Kutubxonaga toʻrtta bir xil paket keldi. Kutubxonachi Nodira opa ularni stolga
qoʻydi va ikki oʻquvchidan <span class="cn-word" data-tr="jami miqdorni aniqlash">sanash</span>ni soʻradi.</p>

<p>Har bir paketda <strong>12</strong> ta kitob va <strong>3</strong> ta daftar bor
edi.</p>

<p>Afsona shunday sanadi: har paketda 12 + 3 = <strong>15</strong> ta narsa, paketlar
toʻrtta, demak <strong>4 × 15 = 60</strong> ta.</p>

<p>Jasur boshqacha sanadi: kitoblar 4 × 12 = <strong>48</strong> ta, daftarlar
4 × 3 = <strong>12</strong> ta, jami <strong>48 + 12 = 60</strong> ta.</p>

<p>— Meniki tezroq, — dedi Afsona.</p>

<p>— Meniki toʻgʻriroq, — dedi Jasur.</p>

<p>Nodira opa doskaga ikkala yoʻlni ham yozdi. Kitoblar sonini — u hozircha <span class="cn-word" data-tr="qiymati oʻzgarib turadigan miqdor">oʻzgaruvchi</span> — <b>n</b> bilan
belgiladi. Afsonaning yoʻli: <strong>4(n + 3)</strong>. Jasurning yoʻli:
<strong>4n + 12</strong>.</p>

<p>— Ikkalangiz ham haqsiz, — dedi u. — Bu ikki
<span class="cn-word" data-tr="harf, son va amallardan tuzilgan yozuv">ifoda</span>
har qanday n da bir xil javob beradi. Qavs oldidagi
<span class="cn-word" data-tr="qavs oldida turgan son yoki harf">koʻpaytuvchi</span>
ichkaridagi <b>har bir</b> hadga tarqaladi. Buni
<span class="cn-word" data-tr="a(b + c) = ab + ac qoidasi">taqsimot qonuni</span>
deyiladi.</p>

<p>Shu payt Nodira opa ikkita paketdan bittadan kitob oldi — ularni tekshirish kerak
edi. Sinf yangi hisobni yozdi: <strong>4(n + 3) − 2</strong>. Qavsni ochib,
<span class="cn-word" data-tr="oʻxshash hadlarni qoʻshib yozuvni qisqartirish">ixchamlash</span>dan
keyin <strong>4n + 10</strong> qoldi.</p>

<p>n = 12 da bu <strong>58</strong> ta narsa beradi. Afsona oddiy yoʻl bilan
tekshirdi: 60 − 2 = 58 ✓</p>

<p>— Matematikada bitta javobga koʻp yoʻl boradi, — dedi Nodira opa. — Faqat ular
bir-biriga zid boʻlmasligi kerak. Zid chiqsa — demak bittasida xato bor.</p>
""",
    },
]
