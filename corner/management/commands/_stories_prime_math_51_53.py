# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-51, PM-52, PM-53.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 51 — sport (mavsum natijalari grafigi), 52 — sharh (ikki dostavka
xizmatini taqqoslash), 53 — hikoya (kafedagi ikki chek). Oldingi uchtasi
yangilik, ilmiy-ommabop va sharh edi; ketma-ket uchta bir xil shakl chiqmaydi.

⚠️ Kumulyativ: qoʻshish usuli YOʻQ (PM-54). 52-matnda kesishuv
   TENGLASHTIRISH bilan, 53-matnda OʻRNIGA QOʻYISH bilan topiladi.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_51_53.py --author=prime
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
    # PM-51 — grafik oʻqish                                      SPORT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Grafik nima deyapti? — mavsum natijalari",
        "summary": (
            "PM-51 matni. Sport: murabbiy jamoaning olti oylik ochkolarini "
            "grafikka chizadi — va oʻyinchilarga grafikning qayeri tik, qayeri "
            "tekis ekanini oʻqishni oʻrgatadi."
        ),
        "order":   51,
        "grammar": [
            {
                "pattern":  "grafikda: tik — tez, tekis — oʻzgarishsiz, pastga — kamayish",
                "meaning":  "Grafikning har bir boʻlagi bitta jumla aytadi. Ikki "
                            "qoʻshni qiymatning farqi oʻsha boʻlakning tikligini "
                            "beradi.",
                "examples": [
                    "Oʻzgarishlar qatori: +3, 0, −5, +6, +2",
                    "Eng tik boʻlak: dekabrdan yanvarga, +6 ochko",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega dekabrda jamoaning ochkolari keskin kamaydi?",
                "choices": [
                    "Murabbiy mashgʻulotlarni bekor qilgani uchun",
                    "Jamoa boshqa shaharga koʻchgani uchun",
                    "Imtihonlar tufayli uchta oʻyinchi mashgʻulotga kelolmagani uchun",
                    "Dekabrda umuman oʻyin boʻlmagani uchun",
                ],
                "answer": 2,
                "explanation": "Matnda aytilgan: dekabr imtihonlar oyi boʻldi va "
                               "uchta asosiy oʻyinchi mashgʻulotlarga kelolmadi. "
                               "Grafikning eng keskin pastga tushgan boʻlagi "
                               "aynan shu oyga toʻgʻri keladi.",
            },
            {
                "text": "Qaysi ikki oy orasida ochkolar eng koʻp oʻsgan?",
                "choices": [
                    "Sentabr va oktabr orasida",
                    "Oktabr va noyabr orasida",
                    "Yanvar va fevral orasida",
                    "Dekabr va yanvar orasida",
                ],
                "answer": 3,
                "explanation": "Oʻzgarishlar: +3, 0, −5, +6, +2. Eng kattasi +6 — "
                               "dekabrdagi 4 tadan yanvardagi 10 taga. Grafikning "
                               "eng tik koʻtarilgan boʻlagi ham oʻsha yerda.",
            },
            {
                "text": "Jamoa olti oyda jami necha ochko toʻpladi?",
                "choices": ["44 ochko", "50 ochko", "56 ochko", "60 ochko"],
                "answer": 1,
                "explanation": "6 + 9 + 9 + 4 + 10 + 12 = 50 ochko. "
                               "«44» — oxirgi oyni qoʻshmay qolgan javob "
                               "(50 − 12 + 6), «56» esa dekabrni ikki marta "
                               "sanaganda chiqadi.",
            },
        ],
        "body": """
<p>Mashgʻulotdan keyin murabbiy Karim aka oʻyinchilarni zal devoriga chaqirdi.
U yerda katta qogʻoz osilgan edi.</p>

<p>Qogʻozda jamoaning olti oylik natijasi
<span class="cn-word" data-tr="maʼlumotning nuqtalar va chiziq bilan chizilgan koʻrinishi">grafik</span>
qilib chizilgandi. Gorizontal
<span class="cn-word" data-tr="koordinata tekisligining sonlar qoʻyilgan chizigʻi">oʻq</span>da
oylar, vertikal oʻqda toʻplangan ochkolar turardi.</p>

<p><b>«Avval shkalaga qaranglar»</b>, — dedi Karim aka. — <b>«Bitta katak 2 ochko.
Buni sezmasangiz, hamma oʻzgarish ikki barobar kichik koʻrinadi.»</b></p>

<p><span class="cn-word" data-tr="bitta katakning qiymati">Shkala</span> aniq
boʻlgach, u har bir <span class="cn-word" data-tr="(x; y) juftligi tekislikda belgilangan joy">nuqta</span>ni
oʻqib chiqdi: sentabr <strong>6</strong>, oktabr <strong>9</strong>, noyabr
<strong>9</strong>, dekabr <strong>4</strong>, yanvar <strong>10</strong>,
fevral <strong>12</strong>.</p>

<p>Bekzod chiziqning shaklini kuzatdi. Boshida
<span class="cn-word" data-tr="chiziqning koʻtarilishi">oʻsish</span> bor.
Keyin oktabr bilan noyabr orasi butunlay
<span class="cn-word" data-tr="miqdor oʻzgarmagan oraliq">tekis boʻlak</span>:
natija oʻzgarmagan. Dekabrda esa chiziq keskin
<span class="cn-word" data-tr="chiziqning tushishi, miqdorning kamayishi">pasayish</span>ga
oʻtadi.</p>

<p><b>«Dekabr imtihonlar oyi boʻldi»</b>, — esladi Karim aka. — <b>«Uchta
oʻyinchi mashgʻulotga kelolmadi.»</b></p>

<p>Undan keyingi boʻlak esa butun grafikdagi eng
<span class="cn-word" data-tr="chiziqning tikligi, oʻzgarish tezligi">tik</span>
joy edi: 4 dan 10 ga, yaʼni <strong>+6</strong> ochko.</p>

<p><b>«Mana shu boʻlak menga hammasidan koʻproq yoqadi»</b>, — dedi murabbiy.
— <b>«Eng baland nuqta fevralda. Lekin eng katta oʻzgarish yanvarda boʻlgan.
Bular ikki xil gap.»</b></p>

<p>Mavsum <span class="cn-word" data-tr="barcha qiymatlarning qoʻshilgani">yigʻindi</span>si
esa devorning pastida turardi: <strong>50</strong> ochko.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-52 — kesishish                                          SHARH
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Qaysi tarif qachon foydali",
        "summary": (
            "PM-52 matni. Sharh: uy nonvoyxonasi egasi ikki yetkazib berish "
            "xizmatini taqqoslaydi — va ular necha buyurtmada tenglashishini "
            "reklamadan emas, hisobdan biladi."
        ),
        "order":   52,
        "grammar": [
            {
                "pattern":  "kesishuv: birinchi narx = ikkinchi narx",
                "meaning":  "Ikki tarif tenglashgan nuqtani topish uchun ularning "
                            "formulalarini teng deb yoziladi. Chiqqan tenglama "
                            "ikki tomonida ham x turgan oddiy tenglama.",
                "examples": [
                    "12 000x = 2 000x + 60 000 → 10 000x = 60 000 → x = 6",
                    "6 buyurtmada ikkalasi ham 72 000 soʻm",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega Nodira opa avval oʻtgan oyning buyurtmalarini "
                        "sanab chiqdi?",
                "choices": [
                    "Chunki qaysi tarif foydali ekani buyurtmalar soniga bogʻliq",
                    "Chunki xizmatlar faqat sanoq boʻyicha ishlaydi",
                    "Chunki reklamada shunday talab qilingan",
                    "Chunki oʻtgan oyning pulini qaytarmoqchi edi",
                ],
                "answer": 0,
                "explanation": "Ikki chiziq kesishgan nuqtadan oldin bir tarif, "
                               "keyin esa boshqasi arzon. Shuning uchun tanlash "
                               "uchun oʻz sonini — oyiga nechta buyurtma "
                               "borligini — bilish kerak.",
            },
            {
                "text": "Necha buyurtmada ikkala xizmatning narxi tenglashadi?",
                "choices": ["4 buyurtmada", "5 buyurtmada", "6 buyurtmada",
                            "10 buyurtmada"],
                "answer": 2,
                "explanation": "12 000x = 2 000x + 60 000 → 10 000x = 60 000 → "
                               "x = 6. Tekshirish: Chaqqon 12 000 × 6 = 72 000, "
                               "Tezkor 2 000 × 6 + 60 000 = 72 000 ✓",
            },
            {
                "text": "Nodira opaning oyiga 9 ta buyurtmasi bor. Tezkorni "
                        "tanlasa qancha tejaydi?",
                "choices": ["18 000 soʻm", "24 000 soʻm", "30 000 soʻm",
                            "48 000 soʻm"],
                "answer": 2,
                "explanation": "Chaqqon: 12 000 × 9 = 108 000 soʻm. Tezkor: "
                               "2 000 × 9 + 60 000 = 18 000 + 60 000 = 78 000 "
                               "soʻm. Farq: 108 000 − 78 000 = 30 000 soʻm.",
            },
        ],
        "body": """
<p>Nodira opa uyida non yopadi va buyurtmalarni shahar boʻylab yetkazib beradi.
Shu oy ikkita xizmat unga taklif bilan chiqdi.</p>

<p><b>«Chaqqon»</b> oddiy ishlaydi: oylik toʻlov yoʻq, har bir yetkazib berish
uchun <strong>12 000</strong> soʻm. <b>«Tezkor»</b> esa oyiga
<strong>60 000</strong> soʻm <span class="cn-word" data-tr="foydalanmasa ham toʻlanadigan oʻzgarmas haq">abonent haqi</span>
oladi, lekin har bir yetkazish atigi <strong>2 000</strong> soʻm.</p>

<p>Reklamada, albatta, faqat ikkinchi son katta harflar bilan yozilgandi.</p>

<p>Nodira opa daftar oldi. Ikkala taklifni ham
<span class="cn-word" data-tr="grafigi toʻgʻri chiziq boʻladigan funksiya">chiziqli funksiya</span>
qilib yozdi: <strong>Chaqqon: y = 12 000x</strong> va <strong>Tezkor:
y = 2 000x + 60 000</strong>. Bu yerda x — oydagi buyurtmalar soni.</p>

<p><span class="cn-word" data-tr="maʼlumotning nuqtalar va chiziq bilan chizilgan koʻrinishi">Grafik</span>da
bu ikkita <span class="cn-word" data-tr="egilmagan, bir tekis chiziq">toʻgʻri chiziq</span>.
Chaqqonniki noldan boshlanadi va tik koʻtariladi. Tezkorniki 60 000 dan
boshlanadi, lekin <span class="cn-word" data-tr="chiziqning tikligi, har bir birlikdagi oʻzgarish">qiyalik</span>i
kichik — ancha yotiq boradi. Qayerdadir ular
<span class="cn-word" data-tr="ikki chiziq uchrashgan, qiymatlari tenglashgan joy">kesishish nuqtasi</span>da
uchrashishi kerak.</p>

<p>Uni topish uchun Nodira opa ikkala narxni teng deb yozdi —
<span class="cn-word" data-tr="ikkita tenglamani birga bajarish talabi">sistema</span>ning
eng sodda koʻrinishi. Chiqqan narsa ikki tomonida ham x turgan oddiy
<span class="cn-word" data-tr="nomaʼlumni topish uchun tuzilgan tenglik">tenglama</span>
edi:</p>

<p><strong>12 000x = 2 000x + 60 000</strong> → <strong>10 000x = 60 000</strong>
→ <strong>x = 6</strong>.</p>

<p>Olti buyurtmada ikkalasi ham <strong>72 000</strong> soʻm. Undan kam
buyurtmada Chaqqon arzon, koʻpida Tezkor.</p>

<p>Keyin u oʻtgan oyning daftariga qaradi va buyurtmalarni sanadi: toʻqqizta.
Chaqqon bilan <strong>108 000</strong>, Tezkor bilan <strong>78 000</strong>
soʻm — oyiga <strong>30 000</strong> soʻm
<span class="cn-word" data-tr="ortiqcha sarflanmay qolgan pul">tejash</span>.</p>

<p>U Tezkorni tanladi. Reklamaga emas, oʻz daftariga qarab.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-53 — oʻrniga qoʻyish usuli                             HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Choy va non — kafedagi hisob",
        "summary": (
            "PM-53 matni. Hikoya: kafening narx taxtasi olib qoʻyilgan, lekin "
            "ikkita chek qolgan — Afsona ulardan choy va non narxini oʻrniga "
            "qoʻyish usuli bilan topadi."
        ),
        "order":   53,
        "grammar": [
            {
                "pattern":  "ifodala → qoʻy → yech → qaytar",
                "meaning":  "Oʻrniga qoʻyish usuli. Bitta tenglamadan bitta "
                            "nomaʼlum ifodalanadi va ikkinchi tenglamaga "
                            "qoʻyiladi; shunda bitta nomaʼlum qoladi.",
                "examples": [
                    "c + n = 10 000 → c = 10 000 − n",
                    "2(10 000 − n) + 3n = 26 000 → n = 6 000, c = 4 000",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega Afsona bitta chekning oʻzidan narxlarni topa "
                        "olmadi?",
                "choices": [
                    "Chunki chekdagi sonlar oʻchib ketgan edi",
                    "Chunki bitta tenglamada ikkita nomaʼlum bor edi",
                    "Chunki chekda faqat non yozilgan edi",
                    "Chunki kassir chekni notoʻgʻri chiqargan edi",
                ],
                "answer": 1,
                "explanation": "«2 ta choy va 3 ta non — 26 000 soʻm» degan "
                               "bitta shartga koʻp xil narx juftligi mos "
                               "keladi. Ikkinchi chek ulardan bittasini "
                               "tanlaydi — shuning uchun ikkita shart kerak.",
            },
            {
                "text": "Bir piyola choy necha soʻm ekan?",
                "choices": ["3 000 soʻm", "4 000 soʻm", "5 000 soʻm",
                            "6 000 soʻm"],
                "answer": 1,
                "explanation": "c + n = 10 000 dan c = 10 000 − n. Uni ikkinchi "
                               "shartga qoʻyamiz: 2(10 000 − n) + 3n = 26 000 → "
                               "20 000 + n = 26 000 → n = 6 000, demak "
                               "c = 4 000 soʻm. «6 000» — nonning narxi.",
            },
            {
                "text": "Jasur 3 ta choy va 2 ta non olmoqchi. Qancha toʻlaydi?",
                "choices": ["20 000 soʻm", "22 000 soʻm", "24 000 soʻm",
                            "26 000 soʻm"],
                "answer": 2,
                "explanation": "3 × 4 000 = 12 000 va 2 × 6 000 = 12 000, jami "
                               "24 000 soʻm. «26 000» — birinchi chekning "
                               "summasini takrorlash.",
            },
        ],
        "body": """
<p>Afsona bilan Jasur maktabdan keyin kichkina kafega kirishdi. Devordagi narx
taxtasi olib qoʻyilgan edi — uni boʻyayotgan ekan.</p>

<p><b>«Choy qancha turadi?»</b> — soʻradi Jasur.</p>

<p>Kassa yonida ikkita eski chek turardi. Birinchisida: <strong>2 ta choy va
3 ta non — 26 000 soʻm</strong>. Ikkinchisida: <strong>1 ta choy va 1 ta non —
10 000 soʻm</strong>.</p>

<p>Afsona daftarini ochdi. Ikkita
<span class="cn-word" data-tr="qiymati nomaʼlum boʻlgan miqdor, harf bilan belgilanadi">nomaʼlum</span>
bor edi: choyning narxi <b>c</b> va nonning narxi <b>n</b>.</p>

<p><b>«Bitta chekning oʻzi yetmaydi»</b>, — dedi u. — <b>«Unda ikkita nomaʼlum
bor, javoblari esa juda koʻp. Ikkinchi chek ulardan bittasini tanlaydi.»</b></p>

<p>Shunday qilib ikkita shart yozildi — bu
<span class="cn-word" data-tr="birga bajarilishi kerak boʻlgan ikki tenglama">tenglamalar sistemasi</span>
edi: <strong>c + n = 10 000</strong> va <strong>2c + 3n = 26 000</strong>.</p>

<p>Afsona osonidan boshladi. Birinchi tenglamadan choyning narxini
<span class="cn-word" data-tr="bir nomaʼlumni ikkinchisi orqali yozish">ifodala</span>di:
<strong>c = 10 000 − n</strong>.</p>

<p>Keyin shu ifodani ikkinchi tenglamada c ning
<span class="cn-word" data-tr="bir nomaʼlum oʻrniga uning ifodasini yozish">oʻrniga qoʻy</span>di
— albatta, <span class="cn-word" data-tr="ifodani butunligicha ajratib turuvchi belgi">qavs</span>
bilan:</p>

<p><strong>2(10 000 − n) + 3n = 26 000</strong> → <strong>20 000 − 2n + 3n =
26 000</strong> → <strong>n = 6 000</strong>.</p>

<p>Endi qolgani oson. Topilgan sonni ifodaga
<span class="cn-word" data-tr="topilgan qiymatdan ikkinchi nomaʼlumni topish">qaytar</span>di:
<strong>c = 10 000 − 6 000 = 4 000</strong>.</p>

<p><b>«Choy 4 000, non 6 000»</b>, — dedi Afsona va darrov
<span class="cn-word" data-tr="javobni shartlarga qoʻyib koʻrish">tekshir</span>di:
2 × 4 000 + 3 × 6 000 = 8 000 + 18 000 = <strong>26 000</strong> ✓</p>

<p>Sistemaning <span class="cn-word" data-tr="ikkala shartni ham bajaradigan qiymatlar">yechim</span>i
bitta son emas edi — ikkita narxdan iborat
<span class="cn-word" data-tr="birga yoziladigan ikkita qiymat, (x; y)">juftlik</span>.</p>

<p>Jasur uch piyola choy va ikkita non buyurdi. Kassada
<strong>24 000</strong> soʻm chiqdi — daftardagidek.</p>
""",
    },
]
