# -*- coding: utf-8 -*-
"""SAT olami — birinchi batch: 1, 2, 3, 6, 9.

Imtihonning oʻzi haqida oʻzbekcha matnlar. Hech bir darsga bogʻlanmagan.
Written with STYLE_GUIDE_CORNER.md + the overrides in toc_sat_olami.txt

  1 — adaptiv modul (IMTIHON QANDAY ISHLAYDI)
  2 — 1,600 ball qanday yigʻiladi
  3 — Desmos
  6 — test kuni soat sayin (TEST KUNI)
  9 — qogʻozdan ekranga (TARIX VA STRATEGIYA)

⚠️ Til: proza oʻzbekcha, inglizcha faqat atama sifatida — har biri cn-word span ichida,
   birinchi uchraganda oʻzbekcha izohi bilan.
⛔ AUDIO YOʻQ — hech qachon gen_corner_audio ishlatilmaydi (proza oʻzbekcha).
⛔ Narx, sana, markaz nomi, universitet chegarasi YOZILMAYDI (toc'ning FACTS boʻlimi).

Faktlar (toc'dan, hammasi tekshirilgan): Bluebook; R&W 2 × 27 savol × 32 daqiqa;
Math 2 × 22 savol × 35 daqiqa; ~2 soat 14 daqiqa + 10 daqiqa tanaffus; har bir boʻlim
200–800, jami 400–1,600; notoʻgʻri javob uchun jarima yoʻq; Desmos ilova ichida;
insho 2021-da bekor qilindi; raqamli test xalqaro 2023-yil mart, AQSHda 2024-yil martdan.

    python manage.py import_corner \\
        corner/management/commands/_stories_sat_olami_01_05.py --author=prime
"""

SUBJECT = {
    "name":    "Matematika",
    "summary": "Matematika: hayotdagi matnlar, atamalar va matematik hikoyalar.",
    "icon":    "bi-calculator",
    "color":   "#f59e0b",
    "order":   7,
}

COLLECTION = {
    "title":       "SAT olami",
    "description": (
        "SAT imtihonining oʻzi haqida — oʻzbek tilida. Adaptiv modul qanday ishlaydi, "
        "1,600 ball qanday yigʻiladi, test kuni nima boʻladi va imtihon nega oʻzgardi. "
        "Darsga bogʻlanmagan: bilib qoʻyish uchun oʻqiladi."
    ),
    "order":       4,
}

STORIES = [

    # ══════════════════════════════════════════════════════════════════
    # 1 — adaptiv modul
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ikkinchi modul nega birinchisiga qarab oʻzgaradi",
        "summary": (
            "Bitta imtihondan chiqqan ikki oʻquvchi ikki xil test koʻrgan boʻlishi "
            "mumkin — va ikkalasi ham rost gapiradi. Adaptiv modul qanday ishlaydi."
        ),
        "order":   1,
        "grammar": [
            {
                "pattern": "multistage adaptive",
                "meaning": "Bosqichli moslashuvchan test. Test <b>savolma-savol emas, "
                           "modulma-modul</b> moslashadi: 1-modul hammaga bir xil, "
                           "2-modul esa 1-moduldagi natijaga qarab tanlanadi. Shuning "
                           "uchun modul ichida orqaga qaytib, javobni oʻzgartirish "
                           "mumkin.",
                "examples": ["Each section has two modules.",
                             "Module 2 is chosen by how Module 1 went."],
            },
        ],
        "body": '''<p>Imtihondan keyin ikki doʻst koridorda uchrashadi. Biri: «Ikkinchi qism juda yengil edi». Ikkinchisi: «Ikkinchi qism dahshat edi, ulgurmadim». Ikkalasi ham rost gapiryapti — chunki ular haqiqatan ham boshqa-boshqa savollarni yechishgan.</p>

<p>Raqamli SAT <span class="cn-word" data-tr="moslashuvchan; testning qiyinligi natijaga qarab oʻzgaradi">adaptive</span> test. Har bir <span class="cn-word" data-tr="boʻlim: Reading and Writing yoki Math">section</span> ikkita <span class="cn-word" data-tr="modul: boʻlimning yarmi, oʻz vaqti bilan">module</span>dan iborat. Birinchi modul hamma uchun bir xil: ichida oson savol ham, oʻrtacha savol ham, qiyin savol ham bor. Siz uni tugatganingizda dastur natijani sanaydi va shu asosda ikkinchi modulni tanlaydi — yengilrogʻini yoki qiyinrogʻini.</p>

<p>Buni ekranda koʻrmaysiz. <span class="cn-word" data-tr="Bluebook — imtihon topshiriladigan rasmiy ilova">Bluebook</span> ilovasi hech qanday xabar bermaydi: modul tugaydi, keyingisi ochiladi, xolos. Birinchi modul ataylab <span class="cn-word" data-tr="aralash qiyinlik: oson, oʻrtacha va qiyin savollar birga">mixed difficulty</span>da tuziladi — shuning uchun undagi bir-ikki qiyin savol «men uddalay olmayapman» degani emas, hamma shu savollarni koʻradi.</p>

<p>Bu <span class="cn-word" data-tr="yoʻnaltirish: qaysi ikkinchi modul berilishini hal qilish">routing</span> deb ataladi.</p>

<p>Bu yerda oʻquvchilar koʻp adashadigan bir nuqta bor. Yengil ikkinchi modul — sovgʻa emas. U erishish mumkin boʻlgan <span class="cn-word" data-tr="ball oraligʻi: erishish mumkin boʻlgan eng yuqori chegara">score band</span>ni pasaytiradi: eng baland ballar faqat qiyin modul orqali ochiladi. Demak birinchi modul oʻzi oʻylagandan koʻra qimmatroq.</p>

<p>Lekin bu «birinchi modulda hamma narsa hal boʻladi» degani ham emas. Ikkala modul ham hisobga olinadi. Yengilrogʻi tushgan oʻquvchi ham har bir savolni oxirigacha ishlashi kerak, chunki notoʻgʻri javob uchun jarima yoʻq va tashlab ketilgan savol — sof yoʻqotish.</p>

<p>Yana bir foydali tafsilot: test <b>savolma-savol emas, modulma-modul</b> moslashadi. Shuning uchun modul ichida oldinga-orqaga yurish, savolni <span class="cn-word" data-tr="belgilab qoʻyish; keyin qaytish uchun">flag</span> qilib qoʻyish va javobni oʻzgartirish mumkin. Modul tugagach esa unga qaytib boʻlmaydi.</p>

<p>Va yana bittasi: ikkinchi modul qiyinroq tuyulsa, bu yomon xabar emas — aksincha, birinchi modul yaxshi oʻtganining belgisi. Koʻp oʻquvchi aynan shu daqiqada sarosimaga tushib, oʻzi ochgan imkoniyatni qoʻldan boy beradi.</p>

<p>Xulosa oddiy: birinchi moduldan boshlaboq toʻliq kuch bilan ishlang, oxirida esa bitta ham boʻsh katak qoldirmang.</p>''',
        "questions": [
            {
                "text": "Nega bitta imtihondan chiqqan ikki oʻquvchi «test qiyinligi» haqida turlicha gapirishi mumkin?",
                "choices": [
                    "Ular imtihonni turli kunlarda topshirishgan.",
                    "Ikkinchi modul har bir oʻquvchiga uning birinchi moduldagi natijasiga qarab tanlanadi.",
                    "Har bir oʻquvchiga tasodifiy savollar beriladi.",
                ],
                "answer": 1,
                "explanation": "Matnda aytilganidek, birinchi modul hammaga bir xil, "
                               "ikkinchisi esa natijaga qarab tanlanadi. Tasodif emas — "
                               "aynan <b>natija</b> hal qiladi.",
            },
            {
                "text": "Yengilroq ikkinchi modul tushgan oʻquvchi nima qilishi kerak?",
                "choices": [
                    "Baribir har bir savolni ishlashi va bitta ham boʻsh katak qoldirmasligi kerak.",
                    "Vaqtni tejab, oxirgi savollarni tashlab ketishi mumkin.",
                    "Testni toʻxtatib, qaytadan topshirishni soʻrashi kerak.",
                ],
                "answer": 0,
                "explanation": "Ikkala modul ham ballga qoʻshiladi va notoʻgʻri javob uchun "
                               "jarima yoʻq. Demak boʻsh qoldirilgan savol — hech qanday "
                               "foydasi yoʻq, sof yoʻqotish.",
            },
            {
                "text": "Modul ichida javobni oʻzgartirish mumkinmi?",
                "choices": [
                    "Yoʻq, har bir savol javob berilgach yopiladi.",
                    "Faqat oxirgi daqiqada.",
                    "Ha — test modulma-modul moslashadi, savolma-savol emas.",
                ],
                "answer": 2,
                "explanation": "Moslashish modul darajasida boʻlgani uchun modul ichida "
                               "erkin harakat qilish, savolni <b>flag</b> qilib qoʻyish va "
                               "qaytib kelish mumkin. Modul tugagach esa unga qaytilmaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # 2 — ball
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "1,600 ball qanday yigʻiladi",
        "summary": (
            "Ikki boʻlim, har biri 200 dan 800 gacha. Notoʻgʻri javob uchun jarima "
            "yoʻqligi nimani anglatadi va nega boʻsh katak eng qimmat xato."
        ),
        "order":   2,
        "grammar": [
            {
                "pattern": "no penalty for a wrong answer",
                "meaning": "Notoʻgʻri javob uchun ball ayirilmaydi. Demak <b>boʻsh "
                           "qoldirilgan savol bilan notoʻgʻri javob bir xil</b> — 0 ball. "
                           "Bundan bitta amaliy qoida chiqadi: hech qachon boʻsh "
                           "qoldirmang, hech boʻlmasa taxmin qiling.",
                "examples": ["There is no penalty for guessing.",
                             "An unanswered question scores the same as a wrong one."],
            },
        ],
        "body": '''<p>SAT ballini eshitgan har bir oʻquvchi 1,600 sonini biladi. Kamroq odam biladigan narsa — bu son qanday yigʻilishi.</p>

<p>Ball ikkita boʻlimdan tashkil topadi. <span class="cn-word" data-tr="oʻqish va yozish boʻlimi">Reading and Writing</span> 200 dan 800 gacha ball beradi, <span class="cn-word" data-tr="matematika boʻlimi">Math</span> ham 200 dan 800 gacha. Ikkalasi qoʻshiladi: eng past natija 400, eng yuqorisi 1,600. Matematikada 44 ta savol, oʻqish va yozishda 54 ta — jami 98 ta savol.</p>

<p>Toʻgʻri javoblar soni avval <span class="cn-word" data-tr="xom ball: shunchaki toʻgʻri javoblar soni">raw score</span> deb hisoblanadi, keyin u 200–800 shkalasiga oʻtkaziladi. Bu oʻtkazish oddiy koʻpaytirish emas: adaptiv test boʻlgani uchun sizga qaysi ikkinchi modul tushgani ham hisobga olinadi.</p>

<p>Endi eng foydali qoida. SAT'da <b>notoʻgʻri javob uchun ball ayirilmaydi</b>. Yaʼni boʻsh qoldirilgan savol ham, notoʻgʻri javob ham bir xil — nol. Farqi shundaki, notoʻgʻri javobda hech boʻlmaganda toʻrtdan bir ehtimol bor edi, boʻsh katakda esa nol. Vaqt tugayotgan boʻlsa ham qolgan savollarga bittadan harf belgilab chiqing: bu bir necha ball qoʻshadi va hech narsani yoʻqotmaydi.</p>

<p>Natija chiqqanda siz uchta sonni koʻrasiz: ikkita <span class="cn-word" data-tr="boʻlim balli: har biri 200–800">section score</span> va ularning yigʻindisi. Bularning hammasi <span class="cn-word" data-tr="ball hisoboti: natija koʻrsatiladigan rasmiy hujjat">score report</span>da beriladi. Xom balldan <span class="cn-word" data-tr="shkalali ball: 200–800 shkalasiga oʻtkazilgan natija">scaled score</span>ga oʻtkazish har bir imtihon uchun alohida hisoblanadi — shuning uchun «nechta xato 700 ball beradi» degan savolning aniq javobi yoʻq.</p>

<p>Oxirgi bir tushunmovchilik: <span class="cn-word" data-tr="foizli oʻrin: sizdan past natija koʻrsatganlarning ulushi">percentile</span> va ball bir narsa emas. 90-<span class="cn-word" data-tr="foizli oʻrin">percentile</span> — bu «90 foiz savolga toʻgʻri javob berdim» degani emas, «test topshirganlarning 90 foizi mendan past ball oldi» degani.</p>

<p>Shuning uchun universitet talabini oʻqiyotganda ballga qarang, foizga emas.</p>''',
        "questions": [
            {
                "text": "SAT'da eng past va eng yuqori umumiy ball qanday?",
                "choices": ["0 dan 1,600 gacha", "400 dan 1,600 gacha", "200 dan 800 gacha"],
                "answer": 1,
                "explanation": "Har bir boʻlim 200 dan 800 gacha ball beradi. Ikkitasi "
                               "qoʻshilganda eng kami 200 + 200 = <b>400</b>, eng koʻpi "
                               "800 + 800 = <b>1,600</b>.",
            },
            {
                "text": "Vaqt tugay deb qolganda javob berilmagan savollar bilan nima qilish kerak?",
                "choices": [
                    "Boʻsh qoldirish kerak, chunki notoʻgʻri javob ball ayiradi.",
                    "Faqat ishonch bor savollarni belgilash kerak.",
                    "Hammasiga javob belgilash kerak — jarima yoʻq, boʻsh katakdan esa foyda yoʻq.",
                ],
                "answer": 2,
                "explanation": "Notoʻgʻri javob uchun jarima yoʻq. Belgilangan javobda "
                               "toʻrtdan bir ehtimol bor, boʻsh katakda esa nol — demak "
                               "taxmin qilish har doim foydali.",
            },
            {
                "text": "«90-percentile» nimani bildiradi?",
                "choices": [
                    "Test topshirganlarning 90 foizi undan past ball olganini.",
                    "Savollarning 90 foiziga toʻgʻri javob berilganini.",
                    "1,600 ballning 90 foizi olinganini.",
                ],
                "answer": 0,
                "explanation": "Percentile — boshqa topshiruvchilar orasidagi oʻrin, "
                               "toʻgʻri javoblar ulushi emas. Universitet talablari esa "
                               "odatda <b>ballda</b> beriladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # 3 — Desmos
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ekrandagi kalkulyator: Desmos nima qila oladi va nima qila olmaydi",
        "summary": (
            "Raqamli SAT'da grafik kalkulyator imtihonning ichida turadi. U qaysi "
            "savollarni bir zumda yopadi va qaysilarida umuman yordam bermaydi."
        ),
        "order":   3,
        "grammar": [
            {
                "pattern": "built-in graphing calculator",
                "meaning": "Imtihon ilovasining ichiga oʻrnatilgan grafik kalkulyator "
                           "(Desmos). Butun <b>Math</b> boʻlimida ochiq turadi — hech "
                           "narsa yuklab olish yoki sotib olish shart emas; xohlasa, "
                           "oʻquvchi oʻzining ruxsat etilgan kalkulyatorini ham olib "
                           "kelishi mumkin.",
                "examples": ["A graphing calculator is built into the app.",
                             "You may also bring your own approved calculator."],
            },
        ],
        "body": '''<p>Qogʻozli SAT'da matematikaning bir qismi kalkulyatorsiz yechilardi. Raqamli testda bunday boʻlim yoʻq: <span class="cn-word" data-tr="Desmos — ilovaga oʻrnatilgan grafik kalkulyator">Desmos</span> butun matematika boʻlimida ekranning yon tomonida turadi.</p>

<p>U nimani yaxshi qiladi? Birinchidan, <span class="cn-word" data-tr="grafik chizmoq">graph</span> chizadi. Ikkita chiziqni kiritsangiz, ularning kesishgan nuqtasini oʻzi topib beradi — sistema yechilgan boʻladi. Ikkinchidan, chirkin tenglamani grafik orqali yechadi: chap tomonni bitta <span class="cn-word" data-tr="funksiya: kiritilgan songa qarab qiymat beruvchi qoida">function</span>, oʻng tomonni ikkinchisi qilib kiriting va kesishgan nuqtaga qarang. Uchinchidan, <span class="cn-word" data-tr="slayder: nomaʼlum sonni surib oʻzgartirish">slider</span> yordamida nomaʼlum <span class="cn-word" data-tr="oʻzgarmas son (a, b, k kabi)">constant</span>li savollarni koʻz bilan koʻrsatadi. Toʻrtinchidan, qoʻlda topilgan javobni 10 soniyada tekshiradi.</p>

<p>Bitta aniq misol. <span class="cn-word" data-tr="tenglamalar sistemasi: ikki tenglama, ikki nomaʼlum">system of equations</span> berilgan boʻlsa, ikkala tenglamani ikkita qator qilib kiriting va <span class="cn-word" data-tr="kesishish nuqtasi">intersection</span> nuqtasini bosing — koordinatalari oʻzi chiqadi. Qoʻlda oʻrniga qoʻyish usuli bilan yechish bir daqiqa olardi; bu yerda oʻn besh soniya. Matematika boʻlimida yana bitta yordamchi bor: ekranda turadigan <span class="cn-word" data-tr="formula varagʻi: yuza, hajm, aylana va maxsus uchburchaklar formulalari">reference sheet</span>. Lekin unda qiyalik formulasi ham, kvadrat tenglama formulasi ham yoʻq — ular yod olinadi.</p>

<p>Endi muhimrogʻi — u nimani qila olmaydi. Desmos inglizcha jumlani oʻqimaydi. Savol nimani soʻrayotganini hal qilmaydi. Sizdan <i>x</i> emas, <i>x</i> + 4 soʻralganini bilmaydi. Grafikdagi qiyalik kontekstda nimani anglatishini ham aytmaydi. Yaʼni u hisoblashni tezlashtiradi, <b>tushunishni emas</b>.</p>

<p>Yana bitta amaliy gap: yozish ham vaqt oladi. Oddiy ikki qadamli tenglamani qoʻlda yechish deyarli har doim tezroq. Tajribali oʻquvchi Desmos'ni uch holatda ochadi: grafik kerak boʻlganda, javobni tekshirish uchun va algebra chalkashib ketganda.</p>

<p>Shuning uchun eng foydali mashq — Desmos'ni imtihon kuni emas, <b>hozir</b> ochib, uni kundalik ishga aylantirish.</p>''',
        "questions": [
            {
                "text": "Raqamli SAT'da kalkulyatorsiz yechiladigan matematika boʻlimi bormi?",
                "choices": [
                    "Ha, birinchi modul kalkulyatorsiz.",
                    "Yoʻq — kalkulyator butun matematika boʻlimida ochiq turadi.",
                    "Faqat oʻz kalkulyatorini olib kelganlar ishlata oladi.",
                ],
                "answer": 1,
                "explanation": "Qogʻozli testda bunday boʻlim bor edi; raqamli testda "
                               "esa yoʻq. Desmos butun boʻlim davomida ochiq, oʻz "
                               "kalkulyatorini olib kelish esa qoʻshimcha imkoniyat.",
            },
            {
                "text": "Quyidagilardan qaysi biri Desmos hal qila olmaydigan ish?",
                "choices": [
                    "Ikki chiziqning kesishgan nuqtasini topish.",
                    "Savol x ni emas, x + 4 ni soʻrayotganini payqash.",
                    "Grafik chizish.",
                ],
                "answer": 1,
                "explanation": "Kalkulyator hisoblaydi, lekin <b>savolni oʻqimaydi</b>. "
                               "Nima soʻralganini aniqlash — har doim oʻquvchining ishi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # 6 — test kuni
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Test kuni: soat sayin",
        "summary": (
            "Kirishdan chiqishgacha: qurilma, ilova, ikki boʻlim, oʻrtadagi 10 daqiqa "
            "va oxirgi besh daqiqada nima qilish kerakligi."
        ),
        "order":   6,
        "grammar": [
            {
                "pattern": "Bluebook",
                "meaning": "Imtihon topshiriladigan rasmiy ilova. Test <b>oldindan</b> "
                           "qurilmaga yuklab olinadi, imtihon kuni esa ilova har bir "
                           "modulning vaqtini oʻzi sanaydi. Qurilma toʻla quvvatlangan "
                           "boʻlishi kerak.",
                "examples": ["The exam is taken in the Bluebook app.",
                             "Download the exam before test day."],
            },
        ],
        "body": '''<p>Test kuni hech qanday sirli emas, lekin uni birinchi marta koʻrgan oʻquvchi ortiqcha asabiylashadi. Kunning tartibi mana bunday.</p>

<p><b>Kelishdan oldin.</b> Test <span class="cn-word" data-tr="Bluebook — imtihon topshiriladigan rasmiy ilova">Bluebook</span> ilovasiga bir necha kun oldin yuklab olinadi. Qurilma toʻla quvvatlangan boʻlsin; quvvat shnurini ham olib boring. Oʻzingiz bilan <span class="cn-word" data-tr="ruxsatnoma: roʻyxatdan oʻtgach chiqadigan hujjat">admission ticket</span> va rasmi bor hujjat olinadi.</p>

<p><b>Kirish.</b> Markazga erta yetib boring. Roʻyxatga olish (<span class="cn-word" data-tr="kirish qaydi: hujjat tekshiruvi va joyga oʻtqazish">check-in</span>) vaqt oladi, kechikkan oʻquvchi esa kiritilmasligi mumkin.</p>

<p><b>Birinchi boʻlim.</b> Avval <span class="cn-word" data-tr="oʻqish va yozish">Reading and Writing</span> topshiriladi: ikkita modul, har biri 27 savol va 32 daqiqa. Ilova vaqtni oʻzi sanaydi, ekranda taymer turadi.</p>

<p>Modul ichida ekranning yuqorisida <span class="cn-word" data-tr="taymer: qolgan vaqtni koʻrsatuvchi soat">timer</span> turadi; uni yashirib qoʻyish ham mumkin, oxirgi besh daqiqada esa oʻzi qaytib chiqadi. Shubhali savolni <span class="cn-word" data-tr="belgilab qoʻyish: keyin qaytish uchun">flag</span> qilib qoʻying va oldinga yuring — modul ichida qaytib kelish erkin. Texnik muammo chiqsa, qoʻl koʻtarib <span class="cn-word" data-tr="nazoratchi">proctor</span>ni chaqiring; vaqt toʻxtatiladi.</p>

<p><b>Tanaffus.</b> Ikki boʻlim orasida 10 daqiqa. Turing, yuring, suv iching. Tanaffusdan keyin oʻqish boʻlimiga <b>qaytib boʻlmaydi</b>.</p>

<p><b>Ikkinchi boʻlim.</b> <span class="cn-word" data-tr="matematika">Math</span>: yana ikkita modul, har biri 22 savol va 35 daqiqa. Desmos va formula varagʻi ekranning oʻzida.</p>

<p><b>Oxirgi besh daqiqa.</b> Bitta qoida: boʻsh katak qolmasin. Jarima yoʻq, demak taxmin qilingan javob har doim boʻshliqdan yaxshi.</p>

<p>Hammasi boʻlib taxminan 2 soat 14 daqiqa test va oʻrtada 10 daqiqa tanaffus. Bir necha hafta ichida natija <span class="cn-word" data-tr="hisob: ball koʻrinadigan shaxsiy kabinet">College Board account</span>ingizda paydo boʻladi.</p>''',
        "questions": [
            {
                "text": "Imtihonda qaysi boʻlim birinchi topshiriladi?",
                "choices": ["Matematika", "Reading and Writing", "Ikkalasi aralash"],
                "answer": 1,
                "explanation": "Avval <b>Reading and Writing</b> (2 × 32 daqiqa), keyin "
                               "10 daqiqa tanaffus, undan soʻng <b>Math</b> "
                               "(2 × 35 daqiqa).",
            },
            {
                "text": "Tanaffusdan keyin oʻqish boʻlimiga qaytish mumkinmi?",
                "choices": [
                    "Ha, agar vaqt qolgan boʻlsa.",
                    "Faqat nazoratchi ruxsat bersa.",
                    "Yoʻq — u boʻlim yopiladi.",
                ],
                "answer": 2,
                "explanation": "Har bir boʻlim oʻz vaqti bilan yopiladi. Shuning uchun "
                               "oʻqish boʻlimidagi boʻsh kataklarni <b>oʻsha yerda</b> "
                               "toʻldirib ketish kerak.",
            },
            {
                "text": "Matematika boʻlimida jami nechta savol bor?",
                "choices": ["44 ta", "54 ta", "27 ta"],
                "answer": 0,
                "explanation": "Ikkita modul, har birida 22 ta savol: 22 + 22 = "
                               "<b>44</b>. 54 ta — oʻqish va yozish boʻlimidagi savollar "
                               "soni (27 + 27).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # 9 — tarix
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Qogʻozdan ekranga: SAT qanday oʻzgardi",
        "summary": (
            "Uch soatlik qogʻozli imtihon qanday qilib 2 soat 14 daqiqalik raqamli "
            "testga aylandi — va nima oʻzgarmay qoldi."
        ),
        "order":   9,
        "grammar": [
            {
                "pattern": "the digital SAT",
                "meaning": "Raqamli SAT. Xalqaro markazlarda <b>2023-yil martdan</b>, "
                           "AQSHda esa <b>2024-yil martdan</b> qogʻozli testning oʻrnini "
                           "egalladi. Insho undan ham oldin — <b>2021-yilda</b> — bekor "
                           "qilingan edi.",
                "examples": ["The digital SAT replaced the paper test in 2023–2024.",
                             "The essay was discontinued in 2021."],
            },
        ],
        "body": '''<p>Bugungi oʻn yetti yoshli oʻquvchi topshiradigan SAT — bu uning akasi topshirgan SAT emas.</p>

<p>Qogʻozli test uch soatga yaqin davom etardi. Uzun matnlar, har biriga oʻntacha savol; matematikaning bir qismi <span class="cn-word" data-tr="kalkulyatorsiz">no-calculator</span> boʻlimi edi; 2021-yilgacha esa ixtiyoriy <span class="cn-word" data-tr="insho">essay</span> ham bor edi. Insho oʻsha yili butunlay bekor qilindi.</p>

<p>Keyingi qadam kattaroq boʻldi. Xalqaro markazlarda 2023-yil martdan, AQSHda 2024-yil martdan imtihon <span class="cn-word" data-tr="raqamli">digital</span> shaklga oʻtdi. Uch narsa birdan oʻzgardi. Test qisqardi: taxminan 2 soat 14 daqiqa. Matnlar qisqardi: endi har bir savolning oʻz kichik matni bor, oʻntalab savolli uzun parcha yoʻq. Kalkulyator butun matematika boʻlimiga ruxsat etildi.</p>

<p>Toʻrtinchi oʻzgarish esa eng chuquri: test <span class="cn-word" data-tr="moslashuvchan">adaptive</span> boʻldi. Endi ikkinchi modul birinchisidagi natijaga qarab tanlanadi. Aynan shu narsa testni qisqartirishga imkon berdi — kamroq savol bilan ham xuddi shunday aniq oʻlchash mumkin.</p>

<p>Oʻqish boʻlimidagi oʻzgarish esa mashqning oʻzini oʻzgartirdi. Ilgari bitta uzun <span class="cn-word" data-tr="parcha: bir necha savolga tegishli uzun matn">passage</span>ni oʻqib, oʻntacha savolga javob berilardi. Endi har bir savolning oʻz <span class="cn-word" data-tr="qisqa matn: bir savolga tegishli bir necha jumla">short passage</span>i bor — koʻpincha bir necha jumla. Bu degani: tez oʻqish emas, <b>aniq oʻqish</b> muhim boʻlib qoldi. Ilgari ixtiyoriy (<span class="cn-word" data-tr="ixtiyoriy">optional</span>) insho ham bor edi; endi u umuman yoʻq.</p>

<p>Nima oʻzgarmadi? Shkala oʻsha-oʻsha: 400 dan 1,600 gacha. Matematikaning <span class="cn-word" data-tr="mazmun: testda oʻlchanadigan mavzular">content</span>i ham deyarli oʻsha: algebra, ilgʻor matematika, maʼlumot tahlili, geometriya. Va eng asosiysi oʻzgarmadi — SAT hamon soat bosimi ostidagi <b>oʻqish</b> imtihoni, ustiga matematika kiyimi kiydirilgan.</p>

<p>Shuning uchun mashq ham oʻzgarmaydi: jumlani tushunish, tuzoq javobni tanish, vaqtni taqsimlash.</p>''',
        "questions": [
            {
                "text": "SAT inshosi qachon bekor qilingan?",
                "choices": ["2021-yilda", "2023-yilda", "2024-yilda"],
                "answer": 0,
                "explanation": "Insho <b>2021-yilda</b> bekor qilingan — raqamli testga "
                               "oʻtishdan oldin. 2023 va 2024 — raqamli shaklga oʻtish "
                               "sanalari (xalqaro va AQSH).",
            },
            {
                "text": "Test nega qisqara oldi?",
                "choices": [
                    "Savollar osonlashtirilgani uchun.",
                    "Adaptiv tuzilma kamroq savol bilan ham aniq oʻlchash imkonini bergani uchun.",
                    "Matematika boʻlimi olib tashlangani uchun.",
                ],
                "answer": 1,
                "explanation": "Matnda aytilganidek, aynan moslashuvchan tuzilma "
                               "qisqartirishga imkon berdi: ikkinchi modul oʻquvchining "
                               "darajasiga moslashadi, shuning uchun kamroq savol yetadi.",
            },
            {
                "text": "Raqamli testda nima oʻzgarmadi?",
                "choices": [
                    "Matnlarning uzunligi.",
                    "Kalkulyator qoidasi.",
                    "400–1,600 ball shkalasi.",
                ],
                "answer": 2,
                "explanation": "Matnlar qisqardi, kalkulyator butun boʻlimga ruxsat "
                               "etildi, lekin <b>shkala</b> oʻzgarmadi: 400 dan 1,600 "
                               "gacha.",
            },
        ],
    },
]
