# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-95, PM-96, PM-97 (Blok H boshlanishi).

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 95 — jumboq, 96 — jumboq, 97 — ilmiy-ommabop.
93 jumboq, 94 hikoya edi — demak uchtasi ketma-ket bir xil shakl
emas (94 oraliqni uzadi).

⚠️ Kumulyativ:
   • 95-matnda 3×3 mantiqiy jadval. Shartlar darsdagilardan boshqa;
     yechim YAGONA (verify skript hamma joylashtirishni koʻrib
     chiqadi);
   • 96-matnda 15 ta stakan — toq son, 2 tadan agʻdarish mumkin emas;
     keyin 3 tadan agʻdarish mumkin boʻlib qolishi koʻrsatiladi.
     ⛔ Doskani boʻyash YOʻQ — u darsning oʻzida;
   • 97-matnda soch tolasi klassikasi. ⛔ Kuchaytirilgan shakl
     (k × (m−1) + 1) YOʻQ — matnda faqat «kamida ikkita» va oddiy
     boʻlish.
⚠️ FAKTLAR ROST BOʻLISHI SHART: odam boshidagi soch tolasi soni
   odatda 100 000–150 000 oraligʻida; matn ehtiyot uchun 200 000 lik
   yuqori chegara oladi va Toshkent aholisini «taxminan 3 million»
   deb yozadi — ikkalasi ham xulosani kuchaytiradi, zaiflashtirmaydi.
⚠️ Savollar SAQLANGAN TARTIBDA koʻrsatiladi — `answer` indekslari:
   95 → 1/3/0, 96 → 2/0/3, 97 → 3/1/2.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_95_97.py --author=prime
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
    # PM-95 — mantiqiy jadval                                    JUMBOQ
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Kim qaysi kasb egasi?",
        "summary": (
            "PM-95 matni. Jumboq: uch qoʻshni haqidagi eski topishmoq. "
            "Uch shart — va ularni jadvalga tushirgan bola javobni "
            "ikki daqiqada topadi."
        ),
        "order":   95,
        "grammar": [
            {
                "pattern":  "shartni «bu emas» ga oʻgir → jadvalga ✗ qoʻy",
                "meaning":  "Mantiqiy masalada hisoblash yoʻq. Har bir "
                            "shart bitta yoki bir nechta katakni "
                            "oʻchiradi; qatorda bitta boʻsh katak "
                            "qolganda u javob boʻladi.",
                "examples": [
                    "«Oshpaz Karimning singlisi» → Karim oshpaz emas",
                    "Karim: shifokor ✗, oshpaz ✗ → Karim dasturchi ✓",
                    "dasturchi ustuni yopildi → Nodira shifokor ✓",
                ],
            },
        ],
        "questions": [
            {
                "text": "«Oshpaz Karimning singlisi» degan gap jadvalga "
                        "qanday tushadi?",
                "choices": [
                    "Karim oshpaz ✓",
                    "Karim oshpaz emas ✗",
                    "Nodira oshpaz ✓",
                    "Bu gap hech narsa bermaydi",
                ],
                "answer": 1,
                "explanation": "Odam oʻzining singlisi boʻlolmaydi — "
                               "demak oshpaz boshqa odam. Bunday "
                               "gaplar har doim ✗ beradi, ✓ emas. Bu "
                               "eng koʻp uchraydigan xato.",
            },
            {
                "text": "Karim qaysi kasb egasi?",
                "choices": ["Shifokor", "Oshpaz", "Qoʻshni", "Dasturchi"],
                "answer": 3,
                "explanation": "Karim shifokor emas (1-shart) va oshpaz "
                               "emas (3-shart). Uch kasbdan ikkitasi "
                               "oʻchdi, demak Karim — dasturchi. "
                               "Qatorda bitta boʻsh katak qolganda u "
                               "javob boʻladi.",
            },
            {
                "text": "Bekzod qaysi kasb egasi?",
                "choices": ["Oshpaz", "Dasturchi", "Shifokor",
                            "Aniqlab boʻlmaydi"],
                "answer": 0,
                "explanation": "Karim dasturchi ekan, dasturchi ustuni "
                               "yopiladi. Nodira oshpaz emas (2-shart), "
                               "demak Nodira — shifokor. Bekzodga "
                               "oshpaz qoladi. Uchala shart ham "
                               "bajarildi va yechim yagona.",
            },
        ],
        "body": """
<p>Sherbek buvisining uyida eski daftarni topib oldi. Uning oxirgi
sahifasida qoʻlda yozilgan
<span class="cn-word" data-tr="mulohaza bilan yechiladigan topishmoq">jumboq</span>
bor edi.</p>

<p>«Bir hovlida uch qoʻshni yashaydi: Karim, Nodira va Bekzod.
Ularning kasblari — dasturchi, shifokor va oshpaz. Har birida bitta
kasb.</p>

<p>Birinchi <span class="cn-word" data-tr="masalada berilgan maʼlumot">shart</span>:
Karim shifokor emas.
<br>Ikkinchi shart: Nodira oshpaz emas.
<br>Uchinchi shart: <i>(bu yerda qogʻoz yirtilgan edi)</i>».</p>

<p>Sherbek buvisidan soʻradi. Buvisi bir zum oʻylab, eslab qoldi:
«Uchinchi shart oddiy edi — <b>oshpaz Karimning singlisi</b>».</p>

<p>«Demak Karim oshpaz emas», dedi Sherbek. Axir odam oʻzining
singlisi boʻlolmaydi — bu shartdan chiqqan birinchi
<span class="cn-word" data-tr="shartdan kelib chiqadigan yangi bilim">xulosa</span>.</p>

<p>U daftarga <span class="cn-word" data-tr="qatorlar va ustunlar kesishmasidagi belgilar jadvali">jadval</span>
chizdi: qatorlarga uch odamning ismini, ustunlarga uch kasbni yozdi.</p>

<p>Keyin har bir shartni jadvalga tushirdi — bu
<span class="cn-word" data-tr="imkonsiz variantlarni birma-bir oʻchirish">chiqarib tashlash</span>
usuli. Karim qatorida: shifokor —
<b>✗</b>, oshpaz — <b>✗</b>. Nodira qatorida: oshpaz — <b>✗</b>.</p>

<p>Va shu zahoti javobning bir qismi koʻrindi. Karimning qatorida
bitta boʻsh <span class="cn-word" data-tr="qator va ustun kesishgan joy">katak</span>
qolgan edi.</p>

<p>«Karim — <strong>dasturchi</strong>», deb yozdi u.</p>

<p>Endi ikkinchi qoida ishga tushdi: ✓ qoʻyilgan zahoti butun
<span class="cn-word" data-tr="jadvalning tik yoʻnalishdagi qatori">ustun</span>ni
oʻchirish kerak. Sherbek Nodira va Bekzod uchun ham dasturchi
katagiga ✗ qoʻydi.</p>

<p>Endi Nodira qatoriga qaradi: oshpaz ✗, dasturchi ✗. Yana bitta
katak qolgan edi.</p>

<p>«Nodira — <strong>shifokor</strong>».</p>

<p>Bekzodga esa <strong>oshpaz</strong> qoldi — oxirgi boʻsh
katak.</p>

<p>Sherbek javobni yozib boʻlgach, uni har bir shart boʻyicha
<span class="cn-word" data-tr="javobni shartlarga qaytarib qoʻyish">tekshir</span>di.
Karim shifokor emas ✓ Nodira oshpaz emas ✓ Oshpaz — Bekzod, yaʼni
Karimning oʻzi emas ✓</p>

<p>Uchala shart ham bajarildi va boshqa
<span class="cn-word" data-tr="hamma variantlardan biri">joylashtirish</span>
qolmadi — <span class="cn-word" data-tr="shartlarni qanoatlantiruvchi bitta javob">yechim yagona</span>.</p>

<p>Sherbek hech qanday
<span class="cn-word" data-tr="hali isbotlanmagan fikr">taxmin</span>
yozmadi — faqat shartdan chiqqanini yozdi.</p>

<p>Buvisi kulib qoʻydi: «Men bu jumboqni bolaligimda bir kun
oʻylaganman».</p>

<p>«Men ikki daqiqada yechdim», dedi Sherbek. «Faqat men jadval
chizdim, siz esa boshda saqlashga urinding».</p>

<p>Buvisi bosh irgʻadi: «Ha. Qogʻoz esa hech narsani
unutmaydi».</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-96 — juftlik                                            JUMBOQ
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Oʻn beshta stakan",
        "summary": (
            "PM-96 matni. Jumboq: choyxonachi shogirdiga oʻn beshta "
            "stakanni toʻgʻrilashni topshiradi — faqat ikkitadan. "
            "Shogird kechgacha urinadi, keyin sababini topadi."
        ),
        "order":   96,
        "grammar": [
            {
                "pattern":  "invariant: juft-toqlik oʻzgarmasa, maqsadga yetib boʻlmaydi",
                "meaning":  "Har bir harakat agʻdarilganlar sonini "
                            "±2 yoki 0 ga oʻzgartiradi — hammasi juft "
                            "son. Demak boshlangʻich toqlik hech "
                            "qachon buzilmaydi.",
                "examples": [
                    "boshida 15 ta agʻdarilgan — toq",
                    "har harakatda oʻzgarish: −2, 0 yoki +2",
                    "maqsad 0 — juft, demak yetib boʻlmaydi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nima uchun shogird masalani yecha olmadi?",
                "choices": [
                    "U tez ishlamadi",
                    "Stakanlar juda koʻp edi",
                    "Chunki masalaning yechimi umuman yoʻq",
                    "U notoʻgʻri stakanlarni tanladi",
                ],
                "answer": 2,
                "explanation": "Masala yechilmaydi — bu uning "
                               "shartidan kelib chiqadi. 15 toq son, "
                               "har bir harakat esa juft son bilan "
                               "oʻzgartiradi, shuning uchun 0 ga hech "
                               "qachon yetib boʻlmaydi.",
            },
            {
                "text": "Bir harakatda agʻdarilgan stakanlar soni qanday "
                        "oʻzgaradi?",
                "choices": [
                    "−2, 0 yoki +2 ga",
                    "Faqat +2 ga",
                    "Faqat −2 ga",
                    "−1 yoki +1 ga",
                ],
                "answer": 0,
                "explanation": "Uch xil hol bor: ikkalasi ham "
                               "agʻdarilgan boʻlsa −2; ikkalasi ham "
                               "toʻgʻri boʻlsa +2; bittasi u, bittasi "
                               "bu boʻlsa 0. Uchalasi ham juft son — "
                               "shuning uchun toqlik saqlanadi.",
            },
            {
                "text": "Agar bir harakatda 3 tadan agʻdarish mumkin "
                        "boʻlsa, oʻn beshta stakanni toʻgʻrilash "
                        "mumkinmi?",
                "choices": [
                    "Yoʻq, baribir mumkin emas",
                    "Faqat stakanlar soni juft boʻlsa",
                    "Faqat juda koʻp urinishdan keyin",
                    "Ha — besh marta harakat yetadi",
                ],
                "answer": 3,
                "explanation": "15 ÷ 3 = 5. Har safar boshqa uchtasini "
                               "agʻdarsa, beshinchi harakatdan keyin "
                               "hamma stakan bir marta agʻdarilgan "
                               "boʻladi va hammasi toʻgʻri turadi. "
                               "Toq sondagi harakat juftlikni "
                               "oʻzgartiradi — toʻsiq yoʻqoladi.",
            },
        ],
        "body": """
<p>Choyxonada kechki tozalash vaqti edi. Usta shogirdi Jasurga
javondagi <strong>15</strong> ta stakanni koʻrsatdi. Hammasi
agʻdarib qoʻyilgan edi.</p>

<p>«Hammasini toʻgʻri holatga keltir», dedi usta. «Faqat bitta shart
bor: har safar roppa-rosa <b>ikkitasini</b> agʻdarasan. Bittasini
ham, uchtasini ham emas».</p>

<p>Jasur ishga kirishdi. Har bir
<span class="cn-word" data-tr="holatni oʻzgartiradigan bitta qadam">harakat</span>da
ikkitasini agʻdardi — endi 13 tasi
agʻdarilgan qoldi. Yana ikkitasini — 11 ta. Yana — 9, keyin 7, 5, 3,
va nihoyat <strong>1</strong> ta.</p>

<p>Bitta stakan qoldi. Uni toʻgʻrilash uchun yana bittasini agʻdarish
kerak edi — lekin unda toʻgʻri turgani agʻdarilib qolardi.</p>

<p>Jasur boshqa yoʻldan yurdi. Aralashtirib, boshqa tartibda urindi.
Kechgacha urindi. Har safar bitta stakan qoldi.</p>

<p>Usta kelib qaradi va soʻradi: «Nega boʻlmayapti?»</p>

<p>«Bilmadim», dedi Jasur. «Balki yoʻlini topolmayotgandirman».</p>

<p>«Yoʻq», dedi usta. «Sen yoʻlni topolmagan emassan.
<b>Yoʻl yoʻq</b>. Va buni isbotlash mumkin».</p>

<p>U qogʻoz oldi. «Faqat bitta narsani kuzatib bor: agʻdarilgan
stakanlar soni. Boshida u <strong>15</strong> ta —
<span class="cn-word" data-tr="2 ga boʻlinmaydigan son">toq</span> son».</p>

<p>«Endi bitta harakatni koʻrib chiqamiz. Ikkita stakan olasan. Uch
xil hol boʻlishi mumkin, boshqasi yoʻq».</p>

<p>Ikkalasi ham agʻdarilgan boʻlsa — soni <b>2 taga kamayadi</b>.
Ikkalasi ham toʻgʻri boʻlsa — <b>2 taga ortadi</b>. Bittasi u,
bittasi bu boʻlsa — <b>oʻzgarmaydi</b>.</p>

<p>«Uchala holda ham <span class="cn-word" data-tr="miqdorning ortishi yoki kamayishi">oʻzgarish</span>
<span class="cn-word" data-tr="2 ga qoldiqsiz boʻlinadigan son">juft</span>
son: −2, 0 yoki +2. Toq songa juft son qoʻshsang, natija yana toq
boʻladi».</p>

<p>Jasur tushuna boshladi. Nechta harakat qilmasin, agʻdarilganlar
soni <b>har doim toq</b> boʻlib qolar edi.</p>

<p>«<span class="cn-word" data-tr="erishmoqchi boʻlgan yakuniy holat">Maqsad</span>ing
esa nol», dedi usta. «Nol — juft son. Toq son hech qachon nolga
aylanmaydi».</p>

<p>Bu — <span class="cn-word" data-tr="hech qanday harakatda oʻzgarmaydigan xossa">invariant</span>
edi: hech qanday harakat oʻzgartira olmaydigan xossa. Boshlangʻich
<span class="cn-word" data-tr="obyektlarning ayni paytdagi joylashuvi">holat</span>ning
invarianti maqsadnikidan farq qilsa, maqsadga yetib boʻlmaydi.</p>

<p>«Demak men bekorga urinibman», dedi Jasur.</p>

<p>«Bekorga emas», dedi usta. «Endi sen bir narsani bilding: “men
qila olmadim” bilan “buni qilib boʻlmaydi” — ikki har xil gap.
Birinchisi <span class="cn-word" data-tr="dalil bilan koʻrsatilgan haqiqat">isbot</span>
emas, ikkinchisi esa isbot».</p>

<p>Ertasi kuni usta <span class="cn-word" data-tr="masalada qoʻyilgan talab">shart</span>ni
oʻzgartirdi: endi har safar <b>uchtadan</b> agʻdarish mumkin edi.</p>

<p>Jasur bu safar bir daqiqada bitirdi. U stakanlarni beshta
<span class="cn-word" data-tr="uchtadan iborat guruh">uchlik</span>ka
boʻldi va har birini bir martadan agʻdardi: 15 ÷ 3 = <strong>5</strong>
harakat. Hamma stakan roppa-rosa bir marta agʻdarilgan — va hammasi
toʻgʻri turardi.</p>

<p>«Koʻrdingmi», dedi usta. «Uch — toq son. Endi har bir harakat
<span class="cn-word" data-tr="sonning juft yoki toqligi">juftlik</span>ni
oʻzgartiradi. Toʻsiq yoʻqoldi».</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-97 — Dirixle prinsipi                          ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Toshkentda ikki kishining sochi bir xil",
        "summary": (
            "PM-97 matni. Ilmiy-ommabop: hech kimning sochini "
            "sanamasdan turib, Toshkentda soch tolasi soni bir xil "
            "boʻlgan odamlar borligini isbotlash mumkin."
        ),
        "order":   97,
        "grammar": [
            {
                "pattern":  "obyektlar uyalardan koʻp boʻlsa, bir uyada kamida ikkitasi bor",
                "meaning":  "Dirixle prinsipi. U obyektlarning "
                            "kimligini aytmaydi — faqat bunday "
                            "juftlik borligini kafolatlaydi.",
                "examples": [
                    "3 000 000 odam, 200 001 xil son → kamida 2 kishi bir xil",
                    "3 000 000 ÷ 200 001 ≈ 15 → aslida kamida 15 kishi",
                    "13 oʻquvchi, 12 oy → kamida 2 tasi bir oyda",
                ],
            },
        ],
        "questions": [
            {
                "text": "Bu daʼvoni isbotlash uchun nima qilish kerak "
                        "emas?",
                "choices": [
                    "Shahar aholisini taxminan bilish",
                    "Sochning eng koʻp soni qanchaligini bilish",
                    "Ikki sonni solishtirish",
                    "Hech boʻlmaganda bir necha kishining sochini sanash",
                ],
                "answer": 3,
                "explanation": "Isbot uchun birorta ham sochni sanash "
                               "shart emas. Faqat ikkita son kerak: "
                               "odamlar soni va mumkin boʻlgan har xil "
                               "qiymatlar soni. Prinsip qolganini "
                               "oʻzi hal qiladi.",
            },
            {
                "text": "Matndagi hisobga koʻra, sochlari soni bir xil "
                        "boʻlgan kamida nechta odam bor?",
                "choices": ["2 kishi", "15 kishi", "200 kishi",
                            "150 000 kishi"],
                "answer": 1,
                "explanation": "3 000 000 ÷ 200 001 ≈ 14,99 va u "
                               "yuqoriga yaxlitlanadi — demak kamida "
                               "15 kishi. «2 kishi» ham rost, lekin bu "
                               "prinsipning eng zaif xulosasi; boʻlish "
                               "ancha kuchliroq javob beradi.",
            },
            {
                "text": "Prinsip bu odamlarning kimligini aytadimi?",
                "choices": [
                    "Ha, hisobdan ularning ismi chiqadi",
                    "Ha, lekin faqat yoshini",
                    "Yoʻq — u faqat bunday odamlar borligini isbotlaydi",
                    "Yoʻq, chunki prinsip ehtimolga asoslangan",
                ],
                "answer": 2,
                "explanation": "Dirixle prinsipi mavjudlik isboti: "
                               "obyekt borligini koʻrsatadi, lekin uni "
                               "topib bermaydi. Aniq odamlarni bilish "
                               "uchun har birining sochini sanash "
                               "kerak boʻlardi. Ehtimolga esa hech "
                               "qanday aloqasi yoʻq — bu kafolat.",
            },
        ],
        "body": """
<p>Toshkentda soch tolalari soni <b>roppa-rosa bir xil</b> boʻlgan
kamida ikki kishi bor.</p>

<p>Bu gapni isbotlash uchun birorta ham odamning sochini sanash shart
emas. Umuman hech kimni koʻrish ham shart emas. Yetarli ikkita son
bor.</p>

<p><b>Birinchi son.</b> Odam boshidagi soch tolalari soni odatda
100 000 dan 150 000 gacha boʻladi. Ehtiyot boʻlaylik va yuqori
chegarani ancha kattaroq — <strong>200 000</strong> deb olaylik.
Demak sochlar soni 0 dan 200 000 gacha boʻlgan sonlardan biri:
jami <strong>200 001</strong> xil
<span class="cn-word" data-tr="boʻlishi mumkin boʻlgan natijalardan biri">variant</span>.</p>

<p><b>Ikkinchi son.</b> Toshkent
<span class="cn-word" data-tr="shaharda yashovchi odamlar soni">aholi</span>si
taxminan <strong>3 000 000</strong> kishi.</p>

<p>Endi ikkalasini yonma-yon qoʻyamiz. Uch million odam bor, lekin
ular uchun atigi ikki yuz ming bir xil son mavjud.</p>

<p>Har bir odamni bitta
<span class="cn-word" data-tr="obyektlar taqsimlanadigan guruh">uya</span>ga
joylashtiramiz — uning sochlari soniga qarab. Uyalar 200 001 ta,
odamlar esa 3 000 000 ta.</p>

<p>Bu — <span class="cn-word" data-tr="obyektlar uyalardan koʻp boʻlsa, bir uyada kamida ikkitasi boʻladi">Dirixle prinsipi</span>ning
aynan oʻzi. Odamlar uyalardan koʻp, demak kamida bitta uyada ikkita
odam bor.</p>

<p>Isbotni <span class="cn-word" data-tr="isbot uchun aksini taxmin qilish">teskari faraz</span>
bilan koʻrsatish mumkin. Aytaylik, hamma odamning sochlari soni har
xil boʻlsin. Unda har bir uyada koʻpi bilan bitta odam boʻlardi va
shahardagi odamlar soni 200 001 dan oshmasdi. Lekin bizda 3 000 000
kishi bor. <span class="cn-word" data-tr="bir-biriga qarama-qarshi ikki xulosa">Ziddiyat</span> —
demak faraz notoʻgʻri.</p>

<p>Aslida <span class="cn-word" data-tr="dalillardan chiqarilgan fikr">xulosa</span>
ancha kuchliroq. Odamlarni uyalarga boʻlib koʻraylik: 3 000 000 ÷ 200 001 ≈ <strong>15</strong>.</p>

<p>Agar har bir uyada koʻpi bilan 14 kishi boʻlganda, jami
200 001 × 14 = 2 800 014 kishi boʻlardi — bu esa uch milliondan kam.
Demak biror uyada kamida <strong>15</strong> kishi bor.</p>

<p>Yaʼni Toshkentda sochlari soni tamomila bir xil boʻlgan kamida
oʻn besh kishi yashaydi. Va bu —
<span class="cn-word" data-tr="har qanday holda bajariladigan xulosa">kafolat</span>,
taxmin emas.</p>

<p>Endi eng muhim gap. Prinsip bu odamlarning <b>kimligini
aytmaydi</b>. U ularni topib bermaydi, ismini bilmaydi, qaysi
mahallada yashashini koʻrsatmaydi. U faqat bitta narsani aytadi:
bunday odamlar <b>bor</b>.</p>

<p>Matematikada bunday isbot
<span class="cn-word" data-tr="obyekt borligini koʻrsatish, uni topmasdan">mavjudlik isboti</span>
deyiladi. U gʻalati tuyulishi mumkin — axir biror narsani topmasdan
turib, uning borligini qanday bilamiz?</p>

<p>Lekin bu kundalik hayotda ham uchraydi — va har safar
<span class="cn-word" data-tr="sanashga asoslangan mulohaza">sanoq</span>
mulohazasi bilan. Konsertda 400 kishi bor
ekan, ulardan ikkitasi bir kunda tugʻilganini bilasiz — kimligini
soʻramasdan ham.</p>

<p>Prinsipni XIX asrda nemis matematigi Peter Gustav Lejeune Dirichlet
ishlatgan va uning nomi bilan atalgan. Nomi
<span class="cn-word" data-tr="jiddiy boʻlmagan, oʻyinchoqdek">jiddiysiz</span>
tuyuladi — «kaptarxona qoidasi». Lekin uning yordamida bugun ham
jiddiy teoremalar isbotlanadi.</p>

<p>Eng qizigʻi shundaki, bu qoidani hech kim isbotlashi shart emas
edi. U shunchalik ravshanki, bolaga ham tushuntirsa boʻladi:
<b>beshta kaptar toʻrtta uyaga sigʻmaydi</b>.</p>
""",
    },
]
