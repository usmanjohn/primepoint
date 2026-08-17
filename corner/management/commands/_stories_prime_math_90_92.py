# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-90, PM-91, PM-92.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 90 — hikoya, 91 — retsept, 92 — sharh.
Oldingi uchlik qoʻllanma / kundalik / hikoya edi. 89 va 90 ketma-ket
hikoya, lekin uchtasi ketma-ket bir xil shakl emas.

⚠️ Kumulyativ:
   • 90-matnda unumdorlik 1/t va birgalikda ishlash. ⛔ Bosqichli ish
     (bir qismini yolgʻiz bajarish) YOʻQ — u darsning matnli
     masalasida;
   • 91-matnda sof modda va suyultirish. ⛔ Ikki eritmani
     aralashtirish YOʻQ — retseptda faqat suv qoʻshiladi;
   • 92-matnda birlik narx va taqqoslash.
⚠️ Sonlar darsdagilardan boshqa: 90 → 10/15 kun (darsda 6/12),
   91 → 400 g shakar (darsda tuzli eritmalar), 92 → yogurt va yuvish
   kukuni (darsda guruch va sharbat).
⚠️ Savollar SAQLANGAN TARTIBDA koʻrsatiladi — `answer` indekslari:
   90 → 1/2/0, 91 → 3/0/2, 92 → 2/3/1.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_90_92.py --author=prime
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
    # PM-90 — ish va unumdorlik                                  HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ikki usta, bitta devor",
        "summary": (
            "PM-90 matni. Hikoya: Karim aka va shogirdi devorni birga "
            "qurishga kelishadi, lekin necha kun ketishini bilishmaydi. "
            "Shogird 12,5 deydi — va yanglishadi."
        ),
        "order":   90,
        "grammar": [
            {
                "pattern":  "birga ishlaganda unumdorliklar qoʻshiladi",
                "meaning":  "Butun ish 1 deb olinadi. Har kimning bir "
                            "kunlik ulushi 1 ÷ (yolgʻiz bitirish vaqti) "
                            "boʻladi; ular qoʻshilib, birgalikdagi "
                            "unumdorlikni beradi.",
                "examples": [
                    "1/10 + 1/15 = 3/30 + 2/30 = 5/30 = 1/6",
                    "t = 1 ÷ 1/6 = 6 kun",
                    "tekshirish: 6/10 + 6/15 = 0,6 + 0,4 = 1",
                ],
            },
        ],
        "questions": [
            {
                "text": "Shogird nima uchun 12,5 kun deb hisobladi?",
                "choices": [
                    "Ikki vaqtni qoʻshgani uchun",
                    "Ikki vaqtning oʻrtachasini olgani uchun",
                    "Devorni ikkiga boʻlgani uchun",
                    "Karim akadan sekinroq ishlagani uchun",
                ],
                "answer": 1,
                "explanation": "U (10 + 15) ÷ 2 = 12,5 deb oʻrtachani "
                               "olgan. Lekin oʻrtacha ham 10 dan katta — "
                               "yaʼni yordamchi kelgach ish sekinlashgan "
                               "boʻlib chiqadi. Bu mantiqan "
                               "boʻlishi mumkin emas.",
            },
            {
                "text": "Ikkovi birga necha kunda bitirdi?",
                "choices": ["4 kun", "5 kun", "6 kun", "12,5 kun"],
                "answer": 2,
                "explanation": "1/10 + 1/15 = 3/30 + 2/30 = 5/30 = 1/6, "
                               "demak bir kunda devorning oltidan bir "
                               "qismi quriladi va butun devor 6 kunda "
                               "bitadi. Javob 10 dan kichik — shunday "
                               "boʻlishi ham kerak edi.",
            },
            {
                "text": "Olti kunda Karim aka devorning qanday qismini "
                        "qurgan?",
                "choices": [
                    "Oltidan uch qismini",
                    "Yarmini",
                    "Uchdan bir qismini",
                    "Hammasini",
                ],
                "answer": 0,
                "explanation": "Karim akaning bir kunlik ulushi 1/10, "
                               "olti kunda 6 × 1/10 = 6/10 = 0,6. "
                               "Shogirdi esa 6 × 1/15 = 6/15 = 0,4. "
                               "Yigʻindisi 0,6 + 0,4 = 1 — butun devor. "
                               "«Yarmini» notoʻgʻri: ular teng "
                               "ishlamagan, chunki tezliklari har xil.",
            },
        ],
        "body": """
<p>Karim aka hovlining orqasiga devor qurmoqchi edi. U bu ishni yolgʻiz
oʻzi <strong>10</strong> kunda bitirishini bilardi — ilgari xuddi
shunday devor qurgan.</p>

<p>Shogirdi Bekzod yordam bermoqchi boʻldi. U hali yosh, shuning uchun
sekinroq ishlaydi: yolgʻiz qursa, <strong>15</strong> kun ketadi.</p>

<p>«Birga qurganda qancha vaqt ketadi?» — deb soʻradi Karim aka.</p>

<p>Bekzod bir zum oʻyladi. «Oʻn va oʻn besh… oʻrtachasi 12 yarim kun»,
dedi u.</p>

<p>Karim aka kuldi. «Demak sen kelganingdan keyin ish
<span class="cn-word" data-tr="odatdagidan uzoqroq davom etadigan">sekinlash</span>adimi?
Yolgʻiz oʻzim 10 kunda qurardim-ku».</p>

<p>Bekzod jim qoldi. Haqiqatan ham javob 10 dan <b>kichik</b> boʻlishi
kerak edi.</p>

<p>Shunda Karim akaning oʻgʻli Sherbek daftar bilan chiqdi. U maktabda
shu mavzuni endigina oʻtgan edi.</p>

<p>«Vaqtlarni qoʻshib ham, oʻrtachalab ham boʻlmaydi», dedi u. «Bir
kunda kim qanchasini qilishini sanash kerak».</p>

<p>U butun <span class="cn-word" data-tr="bajarilishi kerak boʻlgan toʻliq vazifa">ish</span>ni —
yaʼni butun devorni — <strong>1</strong> deb belgiladi.</p>

<p>Karim aka bir kunda devorning oʻndan bir
<span class="cn-word" data-tr="butunning teng boʻlaklaridan biri">qism</span>ini quradi:
<strong>1/10</strong>. Bekzod esa oʻn beshdan bir qismini:
<strong>1/15</strong>. Bu ikki <span class="cn-word" data-tr="butunning boʻlagini koʻrsatuvchi yozuv">kasr</span> — ularning
<span class="cn-word" data-tr="bir kunda bajariladigan ish ulushi">unumdorlik</span>i.</p>

<p>Birga ishlaganda bir kunlik ulushlar qoʻshiladi. Sherbek
<span class="cn-word" data-tr="kasrlarni qoʻshish uchun keltiriladigan maxraj">umumiy maxraj</span>ni
topdi — 30:</p>

<p>1/10 + 1/15 = <strong>3/30</strong> + <strong>2/30</strong> =
<strong>5/30</strong> = <strong>1/6</strong>.</p>

<p>Demak ikkovi bir kunda devorning oltidan bir qismini quradi.
<span class="cn-word" data-tr="hamma boʻlaklarning yigʻindisi, 1 ga teng">Butun</span>
devor esa <strong>6</strong> kunda bitadi.</p>

<p>«Lekin bu son qanday chiqdi?» — soʻradi Bekzod.</p>

<p>«Bir kunda 1/6 qilinsa, butun ishga olti kun kerak. Bu — 1/6 ning
<span class="cn-word" data-tr="1 ni songa boʻlish natijasi">teskari son</span>i»,
dedi Sherbek.</p>

<p>Keyin u <span class="cn-word" data-tr="javobni masala shartlariga qaytarib qoʻyish">tekshirish</span>ni
ham koʻrsatdi. Olti kunda Karim aka 6 × 1/10 = <strong>0,6</strong>
qismini, Bekzod 6 × 1/15 = <strong>0,4</strong> qismini quradi — bu
yerda kasrlar <span class="cn-word" data-tr="verguldan keyin yoziladigan kasr shakli">oʻnlik kasr</span>ga
oʻgirilgan.
Ularning <span class="cn-word" data-tr="qoʻshish amalining natijasi">yigʻindi</span>si
0,6 + 0,4 = <strong>1</strong> — roppa-rosa butun devor.</p>

<p>Devor haqiqatan olti kunda bitdi. Bekzod oxirgi kuni daftarga
shunday yozib qoʻydi: «Vaqt qoʻshilmaydi, unumdorlik qoʻshiladi».</p>

<p>Karim aka yozuvni oʻqib, bosh irgʻadi: «Men buni qirq yil ishlab
bilib oldim. Sen bir kunda».</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-91 — aralashma                                         RETSEPT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Choyga qancha shakar",
        "summary": (
            "PM-91 matni. Retsept: buvijonning kompot retsepti va uni "
            "shirinligiga qarab sozlash. Shakar oʻzgarmaydi — faqat suv "
            "qoʻshiladi, foiz esa oʻzidan-oʻzi tushadi."
        ),
        "order":   91,
        "grammar": [
            {
                "pattern":  "suv qoʻshilsa sof modda oʻzgarmaydi, foiz tushadi",
                "meaning":  "Suyultirishda faqat umumiy massa ortadi. "
                            "Shakarning massasi oʻsha-oʻsha qolgani "
                            "uchun yangi foiz = oʻsha shakar ÷ yangi "
                            "umumiy massa.",
                "examples": [
                    "400 ÷ 2000 = 0,20 = 20% (boshlangʻich)",
                    "400 ÷ 2500 = 0,16 = 16% (500 g suvdan keyin)",
                    "10% uchun kerakli massa: 400 ÷ 0,10 = 4000 g",
                ],
            },
        ],
        "questions": [
            {
                "text": "Retsept boʻyicha tayyorlangan kompot necha foizli "
                        "boʻladi?",
                "choices": ["10%", "16%", "18%", "20%"],
                "answer": 3,
                "explanation": "Shakar 400 g, umumiy massa "
                               "400 + 1600 = 2000 g. "
                               "400 ÷ 2000 = 0,20 = 20%. Diqqat: foiz "
                               "suvdan emas, butun aralashmadan "
                               "olinadi.",
            },
            {
                "text": "500 g suv qoʻshilgandan keyin foiz qancha "
                        "boʻldi?",
                "choices": ["16%", "18%", "20%", "25%"],
                "answer": 0,
                "explanation": "Shakar oʻzgarmadi — hamon 400 g. Yangi "
                               "massa 2000 + 500 = 2500 g. "
                               "400 ÷ 2500 = 0,16 = 16%. Suv shakar "
                               "qoʻshmaydi, u faqat maxrajni "
                               "kattalashtiradi.",
            },
            {
                "text": "10% li qilish uchun yana qancha suv kerak boʻldi?",
                "choices": ["500 g", "1000 g", "1500 g", "4000 g"],
                "answer": 2,
                "explanation": "10% uchun umumiy massa "
                               "400 ÷ 0,10 = 4000 g boʻlishi kerak. "
                               "Hozir 2500 g bor, demak yana "
                               "4000 − 2500 = 1500 g suv qoʻshiladi. "
                               "«4000 g» — kerakli umumiy massa, "
                               "qoʻshiladigan suv emas.",
            },
        ],
        "body": """
<p><b>Buvijonning olma kompoti.</b> Bu
<span class="cn-word" data-tr="taom tayyorlash tartibi va meʼyorlari">retsept</span>
daftarda ellik yildan
beri turadi va unda atigi uch qator bor.</p>

<p><b>Kerakli mahsulotlar:</b> 1 kg olma, <strong>400</strong> g
shakar, <strong>1600</strong> g suv.</p>

<p><b>Tayyorlash.</b> Olmalarni yuving va toʻrt boʻlakka kesing. Suvni
qaynating. Shakarni soling va erib ketguncha aralashtiring. Olmalarni
soling va oʻn daqiqa past olovda pishiring. Sovutib iching.</p>

<p>Buvijon retseptning tagiga bitta izoh yozib qoʻygan:
«<i>Juda shirin boʻlsa, suv qoʻsh. Shakar qoʻshma.</i>»</p>

<p>Dilnoza bu izohni tushunmadi. Nega shakar qoʻshmaslik kerak? Axir
shirinlikni shakar belgilaydi-ku.</p>

<p>Buvijon tushuntirdi: «Shakar allaqachon ichida. Sen faqat uning
<span class="cn-word" data-tr="butun aralashmadagi ulush">ulush</span>ini
oʻzgartirasan».</p>

<p>Dilnoza hisoblab koʻrdi. Kompot — shakar va suvdan iborat
<span class="cn-word" data-tr="bir necha modda qoʻshilib hosil boʻlgan massa">aralashma</span>.
Retsept boʻyicha
<span class="cn-word" data-tr="aralashma ichidagi toza moddaning massasi">sof shakar</span>
<strong>400</strong> g, butun
<span class="cn-word" data-tr="aralashmaning umumiy ogʻirligi">massa</span>
esa 400 + 1600 = <strong>2000</strong> g.</p>

<p>Demak <span class="cn-word" data-tr="sof moddaning umumiy massadagi ulushi">konsentratsiya</span>:
400 ÷ 2000 = 0,20, yaʼni <strong>20</strong>
<span class="cn-word" data-tr="yuzdan boʻlak">foiz</span>.</p>

<p>Kompot haqiqatan juda shirin chiqdi. Dilnoza buvijon aytganday
<strong>500</strong> g suv qoʻshdi.</p>

<p>Endi shakar hamon 400 g — u hech qayoqqa ketmadi. Massa esa
2000 + 500 = <strong>2500</strong> g boʻldi.</p>

<p>Yangi foiz: 400 ÷ 2500 = 0,16 = <strong>16</strong>%. Kompot
<span class="cn-word" data-tr="suv qoʻshib foizni kamaytirish">suyultirildi</span>.</p>

<p>Ertasi kuni mehmonlar keldi. Ular kompotni hamon shirin deyishdi va
Dilnozadan <strong>10</strong>% li qilishni soʻrashdi.</p>

<p>Bu safar Dilnoza <span class="cn-word" data-tr="natijadan boshlab boshlangʻich miqdorni topish">teskari</span>
tomondan yurdi. Agar 400 g shakar butun
massaning 10% i boʻlishi kerak boʻlsa, unda butun massa
400 ÷ 0,10 = <strong>4000</strong> g boʻlishi shart.</p>

<p>Hozir 2500 g bor. Demak yana 4000 − 2500 = <strong>1500</strong> g
suv qoʻshish kerak.</p>

<p>Dilnoza qoʻshdi va
<span class="cn-word" data-tr="javobni shartlarga qaytarib qoʻyish">tekshir</span>di:
400 ÷ 4000 = 0,10 ✓</p>

<p>Kechqurun u retseptning tagiga oʻz
<span class="cn-word" data-tr="matnga qoʻshimcha tushuntirish">izoh</span>ini qoʻshdi: «<i>Suv
qoʻshganda shakar oʻzgarmaydi — faqat
<span class="cn-word" data-tr="kasrning pastki qismi, butun massa">maxraj</span>
kattalashadi. Shuning uchun foiz tushadi.</i>»</p>

<p>Buvijon buni oʻqib, kulib qoʻydi: «Men ellik yil shunday qilaman.
Faqat bunday chiroyli qilib yozolmasdim».</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-92 — narx, miqdor, qiymat                                SHARH
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Katta paket haqiqatan arzonmi?",
        "summary": (
            "PM-92 matni. Sharh: bir oʻquvchi supermarketda oʻn daqiqa "
            "yurib, ikkita mahsulotning birlik narxini hisoblaydi. "
            "Bittasida katta paket arzon chiqadi, ikkinchisida — yoʻq."
        ),
        "order":   92,
        "grammar": [
            {
                "pattern":  "birlik narx = qiymat ÷ miqdor",
                "meaning":  "Ikki paketni solishtirishning yagona halol "
                            "yoʻli. Ikkalasini bir xil oʻlchovga — bir "
                            "kilogramm yoki bir litrga — keltirib "
                            "solishtiriladi.",
                "examples": [
                    "12 000 ÷ 0,4 = 30 000 soʻm/kg",
                    "27 000 ÷ 1 = 27 000 soʻm/kg",
                    "21 000 ÷ 0,6 = 35 000 va 111 000 ÷ 3 = 37 000 soʻm/kg",
                ],
            },
        ],
        "questions": [
            {
                "text": "Muallif nima uchun umumiy narxga qarab hukm "
                        "chiqarmadi?",
                "choices": [
                    "Narxlar tez-tez oʻzgargani uchun",
                    "Katta paket har doim arzon boʻlgani uchun",
                    "Paketlarda har xil miqdor boʻlgani uchun",
                    "Doʻkon chegirma eʼlon qilgani uchun",
                ],
                "answer": 2,
                "explanation": "400 g bilan 1 kg ni umumiy narx boʻyicha "
                               "solishtirib boʻlmaydi — ular har xil "
                               "miqdor. Solishtirish faqat bir xil "
                               "oʻlchovga keltirilgandan keyin maʼnoli "
                               "boʻladi.",
            },
            {
                "text": "Yogurtning kichik paketi bir kilogramm uchun "
                        "necha soʻmga tushdi?",
                "choices": [
                    "12 000 soʻm",
                    "27 000 soʻm",
                    "28 000 soʻm",
                    "30 000 soʻm",
                ],
                "answer": 3,
                "explanation": "400 g — bu 0,4 kg, demak "
                               "12 000 ÷ 0,4 = 30 000 soʻm/kg. Katta "
                               "paket esa 27 000 soʻm/kg — bu safar "
                               "kattasi arzon. «12 000» — paketning "
                               "oʻz narxi, birlik narx emas.",
            },
            {
                "text": "Yuvish kukunida qaysi paket arzonroq chiqdi?",
                "choices": [
                    "3 kg li — kilosi 35 000 soʻm",
                    "600 g li — kilosi 35 000 soʻm",
                    "3 kg li — kilosi 37 000 soʻm",
                    "Ikkalasi bir xil",
                ],
                "answer": 1,
                "explanation": "600 g li: 21 000 ÷ 0,6 = 35 000 soʻm/kg. "
                               "3 kg li: 111 000 ÷ 3 = 37 000 soʻm/kg. "
                               "Demak KICHIK paket kilosiga 2 000 soʻm "
                               "arzon — «katta paket tejamkor» degan "
                               "yozuvga qaramay.",
            },
        ],
        "body": """
<p>Oʻtgan shanba kuni men supermarketda oʻn daqiqa vaqt sarfladim va
telefonimning kalkulyatorida ikkita mahsulotni tekshirdim. Natija
kutganimdan qiziqroq chiqdi.</p>

<p>Sabab oddiy. Javonlarda bir xil mahsulotning ikki xil
<span class="cn-word" data-tr="maʼlum miqdordagi mahsulot oʻrami">paket</span>i
turadi, kattasining ustida esa koʻpincha «tejamkor paket» degan yozuv
osilgan boʻladi. Men shu yozuvni tekshirmoqchi edim.</p>

<p>Umumiy <span class="cn-word" data-tr="hammasi uchun toʻlanadigan pul">narx</span>ga
qarab hukm chiqarib boʻlmaydi — paketlarda har xil
<span class="cn-word" data-tr="mahsulotning ogʻirligi yoki hajmi">miqdor</span>
bor. Shuning uchun ikkalasini bir xil oʻlchovga keltirdim va
<span class="cn-word" data-tr="bir kilogramm yoki bir litrga toʻgʻri keladigan narx">birlik narx</span>ni
hisobladim.</p>

<p><b>Birinchi mahsulot — yogurt.</b></p>

<p>Kichik paket: <strong>400</strong> g, <strong>12 000</strong> soʻm.
400 g — bu 0,4 kg, demak bir kilogrammi
12 000 ÷ 0,4 = <strong>30 000</strong> soʻm.</p>

<p>Katta paket: <strong>1</strong> kg, <strong>27 000</strong> soʻm.
Bu yerda hisoblashning ham hojati yoʻq — bir kilogrammi
<strong>27 000</strong> soʻm.</p>

<p><span class="cn-word" data-tr="ikki miqdorning bir-biridan qanchaga koʻpligi">Farq</span>
sezilarli: kilosiga <strong>3 000</strong> soʻm. Bu safar
«tejamkor paket» degan yozuv rost chiqdi.</p>

<p><b>Ikkinchi mahsulot — yuvish kukuni.</b> Mana bu yerda qiziq
boʻldi.</p>

<p>Kichik paket: <strong>600</strong> g, <strong>21 000</strong> soʻm.
600 g — 0,6 kg, demak 21 000 ÷ 0,6 = <strong>35 000</strong> soʻm/kg.</p>

<p>Katta paket: <strong>3</strong> kg, <strong>111 000</strong> soʻm.
Hisoblaymiz: 111 000 ÷ 3 = <strong>37 000</strong> soʻm/kg.</p>

<p>Yaʼni katta paket kilogrammiga <strong>2 000</strong> soʻm
<b>qimmatroq</b>. Uning ustida esa oʻsha «tejamkor» yozuvi turardi.</p>

<p>Bu <span class="cn-word" data-tr="haqiqatga toʻgʻri kelmaydigan gap">yolgʻon</span>
emas — hech kim «arzonroq» deb yozmagan. Lekin
<span class="cn-word" data-tr="odamda qoladigan tuygʻu, fikr">taassurot</span>
notoʻgʻri: katta paketning umumiy narxi baland boʻlgani uchun u koʻzga
jiddiy va foydali koʻrinadi.</p>

<p>Bir savol qolishi mumkin: nega doʻkon shunday qiladi? Sababi
sodda — koʻpchilik xaridor
<span class="cn-word" data-tr="ikki taklifni bir xil oʻlchovga keltirib solishtirish">taqqoslash</span>ni
qilib oʻtirmaydi. Katta paketni olish qulay va odat boʻlib
qolgan.</p>

<p><b><span class="cn-word" data-tr="dalillardan chiqarilgan yakuniy fikr">Xulosa</span>m.</b>
«Katta paket arzon» — bu qoida emas,
<span class="cn-word" data-tr="tekshirilmagan, ehtimoliy fikr">taxmin</span>. Uni
har safar <span class="cn-word" data-tr="javobni dalil bilan sinab koʻrish">tekshirish</span>
kerak, va buning uchun bitta boʻlish yetadi: narxni miqdorga
boʻling.</p>

<p>Oʻn daqiqada men bitta mahsulotda yutdim va bittasida
<span class="cn-word" data-tr="ortiqcha toʻlangan pul">ortiqcha toʻlov</span>dan
qutuldim. Har oyda shuncha xarid qilinsa,
<span class="cn-word" data-tr="xarid uchun ajratilgan pul">byudjet</span>da
sezilarli farq qoladi.</p>

<p>Keyingi safar javon oldida turganingizda telefonni oling. Bir
boʻlish — bir necha soniya, foydasi esa har oy takrorlanadi.</p>
""",
    },
]
