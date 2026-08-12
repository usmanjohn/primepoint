# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-51, PM-52, PM-53 (grafik oʻqish, sistema, oʻrniga qoʻyish).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: `medium` (Blok D).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq. Savol matnida <strong>, <sup> mumkin.
⚠️ Kumulyativ: qoʻshish usuli YOʻQ (PM-54), parabola YOʻQ (PM-56).
   PM-52 da sistema faqat TENGLASHTIRISH bilan, PM-53 da faqat OʻRNIGA QOʻYISH
   bilan yechiladi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_51_53.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Matematika",
    "description": "Matematika — Prime Math darslarining mashqlari",
    "icon":        "bi-calculator",
    "color":       "#f59e0b",
}

DEFAULTS = {
    "level":                "medium",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PM-51 — real hayot grafigini oʻqish
# =====================================================================

Q_PM51 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Masofa–vaqt grafigidagi "
                "gorizontal boʻlak nimani bildiradi?</strong></p>",
        "choices": [
            "Harakat toʻxtagan",
            "Uyga qarab qaytgan",
            "Tezlik oshgan",
            "Bosib oʻtilgan masofa kamaygan",
        ],
        "correct": "Harakat toʻxtagan",
        "explanation": "<p><strong>Harakat toʻxtagan.</strong> Gorizontal boʻlakda "
                       "vaqt oʻtyapti, lekin masofa oʻzgarmayapti — demak "
                       "yoʻlovchi bir joyda turibdi. <strong>Uyga qarab "
                       "qaytgan</strong> — bu chiziqning pastga tushishi "
                       "boʻlardi, tekis turishi emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Grafik oʻngga qarab "
                "tushib borsa, miqdor qanday oʻzgaryapti?</strong></p>",
        "choices": [
            "Oshib boradi",
            "Kamayib boradi",
            "Umuman oʻzgarmaydi",
            "Avval oshadi, keyin kamayadi",
        ],
        "correct": "Kamayib boradi",
        "explanation": "<p><strong>Kamayib boradi.</strong> Chiziq pastga tushsa, "
                       "vertikal oʻqdagi qiymat kichrayib boradi. PM-49 tilida "
                       "aytganda k manfiy.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bitta grafikda ikkita chiziq bor "
                "va biri ikkinchisidan tikroq koʻtarilgan.</p><p><strong>Bu nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Tikroq chiziqda miqdor tezroq oʻsgan",
            "Tikroq chiziqning qiymati doim kattaroq",
            "Tikroq chiziqda vaqt uzunroq oʻtgan",
            "Tikroq chiziqning shkalasi kichikroq",
        ],
        "correct": "Tikroq chiziqda miqdor tezroq oʻsgan",
        "explanation": "<p><strong>Tikroq chiziqda miqdor tezroq oʻsgan.</strong> "
                       "Tiklik — bir birlik vaqtdagi oʻzgarish, yaʼni PM-49 dagi "
                       "k. <strong>Qiymati doim kattaroq</strong> — notoʻgʻri: "
                       "tik chiziq pastdan boshlanib, ancha vaqt quyida "
                       "qolishi mumkin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Notanish grafikni "
                "oʻqishda birinchi navbatda nima aniqlanadi?</strong></p>",
        "choices": [
            "Oʻqlardagi birlik va bitta katakning qiymati",
            "Chiziqdagi nuqtalarning soni",
            "Grafikning rangi va sarlavhasi",
            "Eng baland nuqtaning oʻrni",
        ],
        "correct": "Oʻqlardagi birlik va bitta katakning qiymati",
        "explanation": "<p><strong>Oʻqlardagi birlik va bitta katakning "
                       "qiymati.</strong> Shkalani bilmasdan aytilgan har qanday "
                       "son taxmin boʻlib qoladi: bir katak 1 emas, 5, 10 yoki "
                       "1000 birlik boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Grafikning vertikal oʻqida 0 bilan 40 orasida "
                "8 ta teng katak bor.</p><p><strong>Bitta katak necha "
                "birlik?</strong></p>",
        "choices": ["5", "8", "32", "320"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Ikki qoʻshni son orasidagi farqni "
                       "kataklar soniga boʻlamiz: 40 ÷ 8 = 5. "
                       "<strong>8</strong> — kataklar sonining oʻzini javob deb "
                       "yozish; <strong>320</strong> — boʻlish oʻrniga "
                       "koʻpaytirish (40 × 8); <strong>32</strong> — 40 − 8.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p>Safarning masofa–vaqt grafigi: dastlabki "
                "2 soatda 90 km bosib oʻtilgan, keyingi 1 soat toʻxtash, "
                "soʻnggi 2 soatda yana 110 km.</p><p><strong>Jami qancha masofa "
                "bosib oʻtilgan?</strong></p>",
        "choices": ["20 km", "90 km", "110 km", "200 km"],
        "correct": "200 km",
        "explanation": "<p><strong>200 km.</strong> Toʻxtash paytida masofa "
                       "qoʻshilmaydi, shuning uchun 90 + 110 = 200 km. "
                       "<strong>110 km</strong> — faqat oxirgi boʻlakni sanash; "
                       "<strong>20 km</strong> — 110 − 90 farqi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Oʻsha safar: 2 soatda 90 km, 1 soat toʻxtash, "
                "yana 2 soatda 110 km.</p><p><strong>Butun yoʻl uchun oʻrtacha "
                "tezlik qancha?</strong></p>",
        "choices": ["40 km/soat", "45 km/soat", "50 km/soat", "55 km/soat"],
        "correct": "40 km/soat",
        "explanation": "<p><strong>40 km/soat.</strong> Oʻrtacha tezlik — butun "
                       "masofa butun vaqtga boʻlingani: 200 ÷ 5 = 40. "
                       "<strong>50</strong> — toʻxtagan soatni hisobga olmaslik "
                       "(200 ÷ 4); <strong>45</strong> va <strong>55</strong> — "
                       "faqat bitta boʻlakning tezligi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻsha safar: 2 soatda 90 km, "
                "1 soat toʻxtash, yana 2 soatda 110 km.</p><p><strong>Qaysi "
                "boʻlakda tezroq yurilgan?</strong></p>",
        "choices": [
            "Birinchi boʻlakda",
            "Uchinchi boʻlakda",
            "Ikkinchi boʻlakda",
            "Ikkala harakat boʻlagida bir xil",
        ],
        "correct": "Uchinchi boʻlakda",
        "explanation": "<p><strong>Uchinchi boʻlakda.</strong> Birinchi boʻlak: "
                       "90 ÷ 2 = 45 km/soat. Uchinchi boʻlak: 110 ÷ 2 = "
                       "55 km/soat. 55 &gt; 45, shuning uchun grafikning oxirgi "
                       "boʻlagi tikroq. Ikkinchi boʻlak — toʻxtash, u yerda "
                       "tezlik nol.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Telefon batareyasi soat 8:00 da 100%, soat "
                "12:00 da 40% edi.</p><p><strong>Har soatda oʻrtacha necha foiz "
                "kamaygan?</strong></p>",
        "choices": ["10%", "15%", "20%", "60%"],
        "correct": "15%",
        "explanation": "<p><strong>15%.</strong> Jami kamayish 100 − 40 = 60%, "
                       "vaqt esa 8:00 dan 12:00 gacha 4 soat: 60 ÷ 4 = 15. "
                       "<strong>60%</strong> — soatlik emas, umumiy kamayish; "
                       "<strong>20%</strong> — vaqtni 3 soat deb sanash; "
                       "<strong>10%</strong> — 40 ÷ 4.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Grafikda bitta katak 5 birlikka teng. Chiziq "
                "4 katak koʻtarildi.</p><p><strong>Miqdor necha birlikka "
                "oʻsgan?</strong></p>",
        "choices": ["4", "5", "9", "20"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> Kataklar soni shkalaga "
                       "koʻpaytiriladi: 4 × 5 = 20. <strong>4</strong> — "
                       "shkalani unutib, kataklar sonini javob deb yozish; "
                       "<strong>9</strong> — koʻpaytirish oʻrniga qoʻshish "
                       "(4 + 5).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Kunlik harorat: 6:00 da 4°, "
                "9:00 da 10°, 12:00 da 16°, 15:00 da 13°, 18:00 da 7°.</p>"
                "<p><strong>Qaysi oraliqda harorat eng koʻp pasaygan?</strong></p>",
        "choices": [
            "6:00 dan 9:00 gacha",
            "9:00 dan 12:00 gacha",
            "12:00 dan 15:00 gacha",
            "15:00 dan 18:00 gacha",
        ],
        "correct": "15:00 dan 18:00 gacha",
        "explanation": "<p><strong>15:00 dan 18:00 gacha.</strong> Oʻzgarishlar: "
                       "+6, +6, −3, −6. Pasayish faqat oxirgi ikkitasida bor va "
                       "eng kattasi −6. Birinchi ikki oraliqda harorat "
                       "koʻtarilgan, ular umuman pasayish emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Doʻkon daromadi (mln soʻm): "
                "1-oy 12, 2-oy 15, 3-oy 15, 4-oy 21, 5-oy 24, 6-oy 23.</p>"
                "<p><strong>Qaysi ikki oy orasida daromad eng koʻp "
                "oʻsgan?</strong></p>",
        "choices": ["1–2-oylar", "2–3-oylar", "3–4-oylar", "5–6-oylar"],
        "correct": "3–4-oylar",
        "explanation": "<p><strong>3–4-oylar.</strong> Oʻzgarishlar qatorini "
                       "yozamiz: +3, 0, +6, +3, −1. Eng kattasi +6 — uchinchi "
                       "oydan toʻrtinchisiga. <strong>5–6-oylar</strong> da "
                       "daromad oʻsmagan, aksincha 1 mln kamaygan.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻsha doʻkon daromadi (mln soʻm): "
                "12, 15, 15, 21, 24, 23.</p><p><strong>Eng katta daromad qaysi "
                "oyda boʻlgan?</strong></p>",
        "choices": ["3-oyda", "4-oyda", "5-oyda", "6-oyda"],
        "correct": "5-oyda",
        "explanation": "<p><strong>5-oyda</strong> — 24 mln soʻm, qatordagi eng "
                       "katta son. Diqqat: eng tez <em>oʻsish</em> 3–4-oylar "
                       "orasida edi, eng katta <em>qiymat</em> esa 5-oyda. "
                       "Balandlik va tiklik — ikki xil savol.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Masofa–vaqt grafigining bir "
                "boʻlagi pastga tushyapti.</p><p><strong>Bu nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Yoʻlovchi bir joyda turibdi",
            "Yoʻlovchi sekinlashgan, lekin oldinga ketyapti",
            "Yoʻlovchi boshlangʻich nuqtaga qarab qaytyapti",
            "Yoʻlovchi tezlashgan",
        ],
        "correct": "Yoʻlovchi boshlangʻich nuqtaga qarab qaytyapti",
        "explanation": "<p><strong>Boshlangʻich nuqtaga qarab qaytyapti.</strong> "
                       "Vertikal oʻqda uydan uzoqlik turibdi; u kamayayotgan "
                       "boʻlsa, yoʻlovchi orqaga kelyapti. <strong>Bir joyda "
                       "turibdi</strong> — gorizontal boʻlak; "
                       "<strong>sekinlashgan</strong> — kamroq tik, lekin hamon "
                       "koʻtarilayotgan boʻlak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi maʼlumotning "
                "nuqtalarini chiziq bilan bogʻlash notoʻgʻri boʻladi?</strong></p>",
        "choices": [
            "Kun davomidagi harorat",
            "Bakdagi suv miqdori",
            "Sotilgan chiptalar soni",
            "Bosib oʻtilgan masofa",
        ],
        "correct": "Sotilgan chiptalar soni",
        "explanation": "<p><strong>Sotilgan chiptalar soni.</strong> U diskret "
                       "miqdor — 2,5 ta chipta boʻlmaydi, shuning uchun nuqtalar "
                       "bogʻlanmaydi. Harorat, suv va masofa uzluksiz "
                       "oʻzgaradi: oraliq qiymatlari ham mavjud (PM-48).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bitta maʼlumot ikkita grafikda "
                "chizildi: birinchisida bir katak 1 birlik, ikkinchisida bir katak "
                "10 birlik.</p><p><strong>Qaysi grafikda haqiqiy oʻzgarish "
                "kattaroq?</strong></p>",
        "choices": [
            "Birinchisida — chiziq balandroq koʻtariladi",
            "Ikkinchisida — kataklar yirikroq",
            "Oʻzgarish ikkalasida bir xil, faqat koʻrinishi har xil",
            "Buni aniqlab boʻlmaydi",
        ],
        "correct": "Oʻzgarish ikkalasida bir xil, faqat koʻrinishi har xil",
        "explanation": "<p><strong>Oʻzgarish bir xil.</strong> Maʼlumot oʻzgargani "
                       "yoʻq — faqat shkala boshqa. Birinchi grafikda chiziq "
                       "tikroq koʻrinadi, chunki har birlik koʻproq joy egallaydi. "
                       "Shuning uchun grafik oʻqishda avval shkalaga qaraladi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Grafikda 2 soatda 120 km bosib "
                "oʻtilgan. Oʻquvchi shunday yozdi: «Tezlik = 120 × 2 = "
                "240 km/soat».</p><p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Masofani vaqtga boʻlish oʻrniga koʻpaytirgan",
            "Vaqtni grafikdan notoʻgʻri oʻqigan",
            "Shkalani hisobga olmagan",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Masofani vaqtga boʻlish oʻrniga koʻpaytirgan",
        "explanation": "<p><strong>Masofani vaqtga boʻlish oʻrniga "
                       "koʻpaytirgan.</strong> Tezlik = masofa ÷ vaqt (PM-35): "
                       "120 ÷ 2 = <strong>60 km/soat</strong>. Taxmin ham shuni "
                       "aytadi: bir soatda 240 km yurish mashina uchun "
                       "mantiqsiz.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Grafikda bitta katak 20 birlik. Chiziq "
                "3 katak koʻtarilgan. Oʻquvchi: «Demak miqdor 3 birlikka "
                "oʻsdi».</p><p><strong>Toʻgʻri javob qanday?</strong></p>",
        "choices": ["3 birlik", "20 birlik", "23 birlik", "60 birlik"],
        "correct": "60 birlik",
        "explanation": "<p><strong>60 birlik.</strong> Kataklar soni shkalaga "
                       "koʻpaytiriladi: 3 × 20 = 60. <strong>3 birlik</strong> — "
                       "shkalani butunlay eʼtiborsiz qoldirish; "
                       "<strong>23</strong> — koʻpaytirish oʻrniga qoʻshish.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Masalani yeching.</p><p>Sherbekning telefonida soat 13:00 da "
                "zaryad 90%, soat 14:00 da 70% edi. Zaryad shu tezlikda kamayishda "
                "davom etdi.</p><p><strong>Soat 16:00 da necha foiz "
                "qoladi?</strong></p>",
        "choices": ["10%", "20%", "30%", "50%"],
        "correct": "30%",
        "explanation": "<p><strong>30%.</strong> Bir soatda 90 − 70 = 20% "
                       "kamayadi. 14:00 dan 16:00 gacha ikki soat: "
                       "70 − 20 × 2 = 70 − 40 = 30%. <strong>50%</strong> — faqat "
                       "bitta soatni hisoblash; <strong>10%</strong> — uch soat "
                       "deb sanash.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bekzod velosipedda ketdi: 40 daqiqada "
                "12 km yurdi, keyin 20 daqiqa doʻstini kutib turdi, soʻng "
                "30 daqiqada yana 9 km yurdi.</p><p><strong>Butun yoʻl uchun "
                "oʻrtacha tezligi qancha?</strong></p>",
        "choices": ["10,5 km/soat", "14 km/soat", "18 km/soat", "21 km/soat"],
        "correct": "14 km/soat",
        "explanation": "<p><strong>14 km/soat.</strong> Jami masofa "
                       "12 + 9 = 21 km. Jami vaqt 40 + 20 + 30 = 90 daqiqa = "
                       "1,5 soat. 21 ÷ 1,5 = 14. Tekshirish: 14 × 1,5 = 21 ✓ "
                       "<strong>18 km/soat</strong> — kutish vaqtini hisobga "
                       "olmaslik (har ikki harakat boʻlagining tezligi ham 18); "
                       "<strong>21</strong> — masofani tezlik deb yozish.</p>",
    },
]


# =====================================================================
# PM-52 — ikki chiziqning kesishishi, sistema
# =====================================================================

Q_PM52 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki nomaʼlumli "
                "sistemaning yechimi nima?</strong></p>",
        "choices": [
            "Ikkala tenglamani ham bajaradigan (x; y) juftligi",
            "Birinchi tenglamani bajaradigan istalgan son",
            "Chiziqning eng baland nuqtasi",
            "x ning istalgan qiymati",
        ],
        "correct": "Ikkala tenglamani ham bajaradigan (x; y) juftligi",
        "explanation": "<p><strong>Ikkala tenglamani ham bajaradigan (x; y) "
                       "juftligi.</strong> Bitta tenglamani bajaradigan juftliklar "
                       "cheksiz koʻp; ikkinchi tenglama ulardan bittasini "
                       "tanlaydi. Shuning uchun yechim — juftlik, bitta son "
                       "emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 2x + 1 chizigʻi "
                "qaysi nuqtadan oʻtadi?</strong></p>",
        "choices": ["(1; 5)", "(2; 4)", "(2; 5)", "(5; 2)"],
        "correct": "(2; 5)",
        "explanation": "<p><strong>(2; 5).</strong> x = 2 qoʻyamiz: "
                       "2 × 2 + 1 = 5 ✓ <strong>(5; 2)</strong> — koordinatalar "
                       "oʻrni almashgan javob; <strong>(1; 5)</strong> da "
                       "2 × 1 + 1 = 3 ≠ 5.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki chiziq kesishgan "
                "nuqta haqida nima toʻgʻri?</strong></p>",
        "choices": [
            "U faqat birinchi chiziqda yotadi",
            "U ikkala chiziqda ham yotadi",
            "U doim koordinata boshida boʻladi",
            "U doim Oy oʻqida boʻladi",
        ],
        "correct": "U ikkala chiziqda ham yotadi",
        "explanation": "<p><strong>U ikkala chiziqda ham yotadi.</strong> Aynan "
                       "shu sababdan uning koordinatalari ikkala tenglamani ham "
                       "toʻgʻri qiladi — butun mavzu shu jumladan oʻsib "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = 3x va y = x + 4 chiziqlari "
                "kesishgan nuqtaning abssissasi nechaga teng?</strong></p>",
        "choices": ["1", "2", "3", "6"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Kesishuvda ikkala y teng: "
                       "3x = x + 4 → 2x = 4 → x = 2. <strong>6</strong> — bu "
                       "ordinata (y = 3 × 2 = 6), abssissa emas: savolni "
                       "diqqat bilan oʻqing.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Parallel chiziqlardan "
                "tuzilgan sistemaning nechta yechimi bor?</strong></p>",
        "choices": ["Bitta ham yoʻq", "Bitta", "Ikkita", "Cheksiz koʻp"],
        "correct": "Bitta ham yoʻq",
        "explanation": "<p><strong>Bitta ham yoʻq.</strong> Parallel chiziqlarning "
                       "k si bir xil (PM-50), ular hech qachon uchrashmaydi. "
                       "Tenglashtirsak yolgʻon tenglik chiqadi — masalan "
                       "1 = 4 — bu «yechim yoʻq» degan javob.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Sistemani yeching.</p><p><strong>y = 2x + 3 va y = 5x − 3. "
                "Kesishgan nuqta qaysi?</strong></p>",
        "choices": ["(1; 5)", "(2; 7)", "(3; 9)", "(7; 2)"],
        "correct": "(2; 7)",
        "explanation": "<p><strong>(2; 7).</strong> 2x + 3 = 5x − 3 → 6 = 3x → "
                       "x = 2. Keyin y = 2 × 2 + 3 = 7. Tekshirish ikkinchisida: "
                       "5 × 2 − 3 = 7 ✓ <strong>(7; 2)</strong> — juftlik teskari "
                       "yozilgan.</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>y = 4x − 5 va y = x + 4. "
                "Kesishgan nuqta qaysi?</strong></p>",
        "choices": ["(2; 3)", "(3; 7)", "(4; 8)", "(7; 3)"],
        "correct": "(3; 7)",
        "explanation": "<p><strong>(3; 7).</strong> 4x − 5 = x + 4 → 3x = 9 → "
                       "x = 3. y = 3 + 4 = 7. Tekshirish: 4 × 3 − 5 = 7 ✓ "
                       "<strong>(7; 3)</strong> — koordinatalar oʻrni "
                       "almashgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sistema: x + y = 5 va "
                "2x − y = 7.</p><p><strong>Quyidagilardan qaysi biri uning "
                "yechimi?</strong></p>",
        "choices": ["(1; 4)", "(2; 3)", "(3; 2)", "(4; 1)"],
        "correct": "(4; 1)",
        "explanation": "<p><strong>(4; 1).</strong> 4 + 1 = 5 ✓ va "
                       "2 × 4 − 1 = 8 − 1 = 7 ✓ Diqqat: qolgan uchtasi ham "
                       "birinchi tenglamani bajaradi, lekin ikkinchisini emas "
                       "((3; 2): 6 − 2 = 4 ≠ 7). <strong>Juftlikni ikkala "
                       "tenglamada ham tekshirish shart.</strong></p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = 6x va y = 2x + 12 chiziqlari "
                "kesishgan nuqtaning ordinatasi nechaga teng?</strong></p>",
        "choices": ["3", "12", "15", "18"],
        "correct": "18",
        "explanation": "<p><strong>18.</strong> 6x = 2x + 12 → 4x = 12 → x = 3, "
                       "keyin y = 6 × 3 = 18. <strong>3</strong> — bu abssissa; "
                       "ordinata deb y soʻralgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki tarif: A tarifda "
                "y = 2 000x + 30 000, B tarifda y = 5 000x.</p><p><strong>Necha "
                "birlikda narxlar tenglashadi?</strong></p>",
        "choices": ["6", "10", "15", "30"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 5 000x = 2 000x + 30 000 → "
                       "3 000x = 30 000 → x = 10. <strong>15</strong> — "
                       "30 000 ÷ 2 000, yaʼni notoʻgʻri koeffitsientga "
                       "boʻlish; <strong>6</strong> — 30 000 ÷ 5 000.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Oʻsha ikki tarif: A da y = 2 000x + 30 000, "
                "B da y = 5 000x; ular x = 10 da tenglashadi.</p><p><strong>Oʻsha "
                "nuqtada narx qancha?</strong></p>",
        "choices": ["30 000 soʻm", "50 000 soʻm", "60 000 soʻm", "80 000 soʻm"],
        "correct": "50 000 soʻm",
        "explanation": "<p><strong>50 000 soʻm.</strong> B tarifda: "
                       "5 000 × 10 = 50 000. A tarifda ham: 20 000 + 30 000 = "
                       "50 000 ✓ <strong>80 000</strong> — javobga abonent haqini "
                       "yana bir marta qoʻshish.</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>y = x + 1 va y = 3x − 5. "
                "Yechim qaysi?</strong></p>",
        "choices": ["(2; 3)", "(3; 4)", "(4; 5)", "(5; 6)"],
        "correct": "(3; 4)",
        "explanation": "<p><strong>(3; 4).</strong> x + 1 = 3x − 5 → 6 = 2x → "
                       "x = 3. y = 3 + 1 = 4. Tekshirish: 3 × 3 − 5 = 4 ✓ "
                       "Qolgan juftliklar birinchi tenglamani bajaradi, "
                       "ikkinchisini esa yoʻq.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 3x + 2 va "
                "y = 3x + 9 sistemasining nechta yechimi bor?</strong></p>",
        "choices": [
            "Bitta: (0; 2)",
            "Bitta: (0; 9)",
            "Cheksiz koʻp",
            "Yechim yoʻq — chiziqlar parallel",
        ],
        "correct": "Yechim yoʻq — chiziqlar parallel",
        "explanation": "<p><strong>Yechim yoʻq.</strong> k lari bir xil (3), b "
                       "lari har xil (2 va 9) — parallel chiziqlar. "
                       "Tenglashtirsak 2 = 9 chiqadi, bu yolgʻon. "
                       "<strong>(0; 2)</strong> — faqat birinchi chiziqning Oy "
                       "oʻqini kesish nuqtasi, sistemaning yechimi emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 2x + 5 va "
                "2y = 4x + 10 sistemasining nechta yechimi bor?</strong></p>",
        "choices": ["Yechim yoʻq", "Bitta yechim", "Ikkita yechim",
                    "Cheksiz koʻp yechim"],
        "correct": "Cheksiz koʻp yechim",
        "explanation": "<p><strong>Cheksiz koʻp yechim.</strong> Ikkinchi "
                       "tenglamaning ikkala tomonini 2 ga boʻlsak, y = 2x + 5 "
                       "chiqadi — bu birinchisining oʻzi. Chiziqlar ustma-ust "
                       "tushgan, demak har bir nuqtasi yechim.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>y = 2x − 5 va y = x − 1 "
                "sistemasi yechildi va x = 4 topildi.</p><p><strong>Toʻliq javob "
                "qanday yoziladi?</strong></p>",
        "choices": ["x = 4", "y = 4", "(3; 4)", "(4; 3)"],
        "correct": "(4; 3)",
        "explanation": "<p><strong>(4; 3).</strong> x = 4 ni qoʻyamiz: "
                       "y = 4 − 1 = 3 (tekshirish: 2 × 4 − 5 = 3 ✓). Sistemaning "
                       "yechimi — juftlik; <strong>x = 4</strong> deb toʻxtash "
                       "masalani yarmida qoldirish, <strong>(3; 4)</strong> esa "
                       "juftlikni teskari yozish demakdir.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki chiziqning kesishuvi "
                "(2,5; 6,25) kabi kasr sonlarda joylashgan.</p><p><strong>Qaysi "
                "usul ishonchli javob beradi?</strong></p>",
        "choices": [
            "Grafik usul, chunki nuqta koʻrinib turadi",
            "Hisob usuli, chunki javob aniq chiqadi",
            "Ikkala usul ham bir xil aniq",
            "Bunday sistemani umuman yechib boʻlmaydi",
        ],
        "correct": "Hisob usuli, chunki javob aniq chiqadi",
        "explanation": "<p><strong>Hisob usuli.</strong> Chizmadan 2,5 ni 2 yoki "
                       "3 dan ajratish qiyin, 6,25 ni esa umuman oʻqib "
                       "boʻlmaydi. Grafik usul vaziyatni tushuntirish uchun "
                       "yaxshi, aniq javob uchun esa tenglashtirish kerak.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Oʻquvchi y = 2x + 1 va y = 2x + 6 "
                "sistemasini yechdi: «2x + 1 = 2x + 6 → 1 = 6 → x = 0».</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Tenglamalarni tenglashtirish notoʻgʻri qilingan",
            "1 = 6 yolgʻon, demak yechim yoʻq — x = 0 emas",
            "Javob x = 0 emas, x = 5 boʻladi",
            "Xato yoʻq, yechim toʻgʻri topilgan",
        ],
        "correct": "1 = 6 yolgʻon, demak yechim yoʻq — x = 0 emas",
        "explanation": "<p><strong>1 = 6 yolgʻon, demak yechim yoʻq.</strong> "
                       "Nomaʼlum ikkala tomondan qisqarib ketib, yolgʻon tenglik "
                       "qolsa, javob «yechim yoʻq» boʻladi. Chiziqlar parallel: "
                       "k lari bir xil (2), b lari har xil.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Sistema: x + y = 7 va 2x − y = 2. "
                "Oʻquvchi: «(5; 2) yechim, chunki 5 + 2 = 7».</p><p><strong>Xato "
                "qayerda?</strong></p>",
        "choices": [
            "Juftlikni faqat birinchi tenglamada tekshirgan",
            "Birinchi tenglamani notoʻgʻri hisoblagan",
            "Juftlikni teskari yozgan",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Juftlikni faqat birinchi tenglamada tekshirgan",
        "explanation": "<p><strong>Faqat birinchi tenglamada tekshirgan.</strong> "
                       "Ikkinchisida: 2 × 5 − 2 = 8 ≠ 2 ✗ Demak (5; 2) yechim "
                       "emas. Toʻgʻri yechim — (3; 4): 3 + 4 = 7 ✓ va "
                       "2 × 3 − 4 = 2 ✓</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Masalani yeching.</p><p>«Nur» bosmaxonasi buyurtma uchun "
                "50 000 soʻm tayyorlash haqi oladi va har varaq uchun 500 soʻm "
                "qoʻshadi. «Ziyo» bosmaxonasida tayyorlash haqi yoʻq, lekin har "
                "varaq 1 000 soʻm.</p><p><strong>Necha varaqda ikkala "
                "bosmaxonaning narxi tenglashadi?</strong></p>",
        "choices": ["50 varaq", "100 varaq", "150 varaq", "200 varaq"],
        "correct": "100 varaq",
        "explanation": "<p><strong>100 varaq.</strong> Nur: y = 500x + 50 000. "
                       "Ziyo: y = 1 000x. Tenglashtiramiz: "
                       "1 000x = 500x + 50 000 → 500x = 50 000 → x = 100. "
                       "Ikkalasi ham 100 000 soʻm ✓ <strong>50 varaq</strong> — "
                       "50 000 ni 1 000 ga boʻlish, farqni emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Jasurda 40 000 soʻm bor va u har hafta "
                "15 000 soʻmdan qoʻshadi. Sherbekda 100 000 soʻm bor, lekin u har "
                "hafta 5 000 soʻmdan qoʻshadi.</p><p><strong>Necha haftadan keyin "
                "pullari tenglashadi va qancha boʻladi?</strong></p>",
        "choices": [
            "4 haftada, 100 000 soʻm",
            "6 haftada, 130 000 soʻm",
            "6 haftada, 140 000 soʻm",
            "10 haftada, 190 000 soʻm",
        ],
        "correct": "6 haftada, 130 000 soʻm",
        "explanation": "<p><strong>6 haftada, 130 000 soʻm.</strong> Jasur: "
                       "y = 15 000x + 40 000. Sherbek: y = 5 000x + 100 000. "
                       "Tenglashtiramiz: 10 000x = 60 000 → x = 6. Pul: "
                       "15 000 × 6 + 40 000 = 130 000, tekshirish "
                       "5 000 × 6 + 100 000 = 130 000 ✓ Boshlangʻich farq "
                       "60 000 soʻm, har haftada 10 000 soʻmga yopiladi.</p>",
    },
]


# =====================================================================
# PM-53 — oʻrniga qoʻyish usuli
# =====================================================================

Q_PM53 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Oʻrniga qoʻyish "
                "usulining birinchi qadami qaysi?</strong></p>",
        "choices": [
            "Bitta tenglamadan bitta nomaʼlumni ifodalash",
            "Ikkala tenglamani qoʻshish",
            "Ikkala chiziqni grafikda chizish",
            "Ikkala tenglamani bir-biriga koʻpaytirish",
        ],
        "correct": "Bitta tenglamadan bitta nomaʼlumni ifodalash",
        "explanation": "<p><strong>Bitta nomaʼlumni ifodalash.</strong> Toʻrt "
                       "qadam: ifodala → qoʻy → yech → qaytar. Ifoda ikkinchi "
                       "tenglamaga qoʻyilgach, u yerda bitta nomaʼlum qoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>x + y = 9 "
                "tenglamasidan y ni ifodalang: y = ___</strong></p>",
        "choices": ["9 − x", "9 + x", "x − 9", "9x"],
        "correct": "9 − x",
        "explanation": "<p><strong>y = 9 − x.</strong> Ikki tomondan x ni "
                       "ayiramiz. <strong>x − 9</strong> — ayirish tartibi "
                       "almashgan (bu −y ni beradi); <strong>9 + x</strong> — "
                       "ishora xatosi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>x − y = 4 "
                "tenglamasidan x ni ifodalang: x = ___</strong></p>",
        "choices": ["4 − y", "4y", "y − 4", "y + 4"],
        "correct": "y + 4",
        "explanation": "<p><strong>x = y + 4.</strong> Ikki tomonga y qoʻshamiz. "
                       "<strong>4 − y</strong> — eng koʻp uchraydigan ishora "
                       "xatosi; tekshiring: y = 1 boʻlsa x = 5, chunki "
                       "5 − 1 = 4 ✓</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>y = x + 1 va x + y = 7. "
                "Yechim qaysi?</strong></p>",
        "choices": ["(2; 3)", "(3; 4)", "(4; 3)", "(4; 5)"],
        "correct": "(3; 4)",
        "explanation": "<p><strong>(3; 4).</strong> y ning oʻrniga x + 1 "
                       "qoʻyamiz: x + (x + 1) = 7 → 2x + 1 = 7 → x = 3, "
                       "y = 3 + 1 = 4. Tekshirish: 3 + 4 = 7 ✓ "
                       "<strong>(4; 3)</strong> — juftlik teskari yozilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3x + 2y = 16 va y = 2 boʻlsa, x "
                "nechaga teng?</strong></p>",
        "choices": ["2", "4", "6", "8"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> y = 2 ni qoʻyamiz: "
                       "3x + 4 = 16 → 3x = 12 → x = 4. <strong>6</strong> — "
                       "2y = 4 ni ayirmasdan 18 ÷ 3 hisoblash.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Sistemani yeching.</p><p><strong>x + y = 12 va 3x + y = 26. "
                "Yechim qaysi?</strong></p>",
        "choices": ["(5; 7)", "(6; 6)", "(7; 5)", "(8; 4)"],
        "correct": "(7; 5)",
        "explanation": "<p><strong>(7; 5).</strong> y = 12 − x → "
                       "3x + (12 − x) = 26 → 2x + 12 = 26 → 2x = 14 → x = 7, "
                       "y = 5. Tekshirish: 3 × 7 + 5 = 26 ✓ Qolgan juftliklar "
                       "birinchi tenglamani bajaradi, ikkinchisini emas.</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>2x + y = 11 va x − y = 1. "
                "Yechim qaysi?</strong></p>",
        "choices": ["(3; 4)", "(4; 3)", "(5; 1)", "(6; 5)"],
        "correct": "(4; 3)",
        "explanation": "<p><strong>(4; 3).</strong> Ikkinchisidan x = y + 1 "
                       "(koeffitsienti 1 — ifodalash oson). Qoʻyamiz: "
                       "2(y + 1) + y = 11 → 3y + 2 = 11 → y = 3, x = 4. "
                       "Tekshirish: 2 × 4 + 3 = 11 ✓ va 4 − 3 = 1 ✓</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>y = 2x − 3 va 3x + y = 12. "
                "Yechim qaysi?</strong></p>",
        "choices": ["(2; 1)", "(3; 3)", "(4; 5)", "(5; 7)"],
        "correct": "(3; 3)",
        "explanation": "<p><strong>(3; 3).</strong> Ifoda tayyor: "
                       "3x + (2x − 3) = 12 → 5x − 3 = 12 → 5x = 15 → x = 3, "
                       "y = 2 × 3 − 3 = 3. Tekshirish: 9 + 3 = 12 ✓</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>x = 3y va x + y = 20. "
                "Yechim qaysi?</strong></p>",
        "choices": ["(5; 15)", "(12; 8)", "(15; 5)", "(18; 2)"],
        "correct": "(15; 5)",
        "explanation": "<p><strong>(15; 5).</strong> 3y + y = 20 → 4y = 20 → "
                       "y = 5, x = 3 × 5 = 15. <strong>(5; 15)</strong> — "
                       "«x y dan 3 marta katta» shartini teskari oʻqish: "
                       "tekshiring, 5 = 3 × 15 emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>15 000(20 − x) = "
                "___</strong></p>",
        "choices": [
            "300 000 − 15 000x",
            "300 000 + 15 000x",
            "20 − 300 000x",
            "285 000x",
        ],
        "correct": "300 000 − 15 000x",
        "explanation": "<p><strong>300 000 − 15 000x.</strong> Koʻpaytuvchi qavs "
                       "ichidagi <em>har bir</em> hadga tarqatiladi va ishora "
                       "saqlanadi (PM-33): 15 000 × 20 = 300 000, "
                       "15 000 × (−x) = −15 000x. <strong>300 000 + "
                       "15 000x</strong> — minusni yoʻqotib qoʻyish, sistemalarda "
                       "eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>2x + 3y = 19 va x = y + 2. "
                "Yechim qaysi?</strong></p>",
        "choices": ["(3; 5)", "(4; 4)", "(5; 3)", "(7; 1)"],
        "correct": "(5; 3)",
        "explanation": "<p><strong>(5; 3).</strong> 2(y + 2) + 3y = 19 → "
                       "2y + 4 + 3y = 19 → 5y = 15 → y = 3, x = 3 + 2 = 5. "
                       "Tekshirish: 10 + 9 = 19 ✓ va 5 = 3 + 2 ✓ "
                       "<strong>(3; 5)</strong> — juftlik teskari.</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>4x + y = 14 va 2x + 3y = 22. "
                "Yechim qaysi?</strong></p>",
        "choices": ["(1; 10)", "(2; 6)", "(3; 2)", "(4; −2)"],
        "correct": "(2; 6)",
        "explanation": "<p><strong>(2; 6).</strong> Birinchisidan y = 14 − 4x "
                       "(koeffitsienti 1). Qoʻyamiz: 2x + 3(14 − 4x) = 22 → "
                       "2x + 42 − 12x = 22 → −10x = −20 → x = 2, "
                       "y = 14 − 8 = 6. Tekshirish: 4 + 18 = 22 ✓</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi sistemada oʻrniga "
                "qoʻyish usuli eng oson ishlaydi?</strong></p>",
        "choices": [
            "3x + 5y = 17 va 4x + 7y = 23",
            "y = 2x + 1 va 3x + y = 16",
            "6x + 4y = 20 va 9x + 8y = 34",
            "7x − 3y = 11 va 5x + 2y = 19",
        ],
        "correct": "y = 2x + 1 va 3x + y = 16",
        "explanation": "<p><strong>y = 2x + 1 va 3x + y = 16.</strong> Bu yerda y "
                       "allaqachon ifodalangan — birinchi qadam qilib "
                       "qoʻyilgan. Qolgan sistemalarda hamma koeffitsientlar 1 "
                       "dan katta, ifodalash kasr chiqaradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sistema: x + 4y = 18 va "
                "3x + 5y = 26.</p><p><strong>Qaysi nomaʼlumni, qaysi tenglamadan "
                "ifodalash eng oson?</strong></p>",
        "choices": [
            "Birinchi tenglamadan x ni",
            "Birinchi tenglamadan y ni",
            "Ikkinchi tenglamadan x ni",
            "Ikkinchi tenglamadan y ni",
        ],
        "correct": "Birinchi tenglamadan x ni",
        "explanation": "<p><strong>Birinchi tenglamadan x ni.</strong> Faqat "
                       "oʻshaning koeffitsienti 1: x = 18 − 4y, kasr yoʻq. "
                       "Yechimi: 3(18 − 4y) + 5y = 26 → 54 − 7y = 26 → y = 4, "
                       "x = 2. Boshqa yoʻllar 4y = 18 − x ÷ 4 kabi kasrlarga "
                       "olib boradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sistema yechilayotganda "
                "y = 10 − x ifodasi tuzildi va x = 5 topildi.</p><p><strong>Toʻliq "
                "javob qanday yoziladi?</strong></p>",
        "choices": ["x = 5", "(5; 5)", "(5; 10)", "(10; 5)"],
        "correct": "(5; 5)",
        "explanation": "<p><strong>(5; 5).</strong> Toʻrtinchi qadam — qaytarish: "
                       "y = 10 − 5 = 5. <strong>x = 5</strong> deb toʻxtash "
                       "javobning yarmini bermaslik; <strong>(5; 10)</strong> — "
                       "ifodaga qoʻymasdan 10 ni y deb yozish.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻquvchi x + y = 10 dan "
                "y = 10 − x ni chiqardi va uni <em>oʻsha</em> tenglamaga qaytarib "
                "qoʻydi.</p><p><strong>Nima chiqadi?</strong></p>",
        "choices": [
            "Sistemaning yechimi topiladi",
            "10 = 10 kabi hech narsa bermaydigan tenglik",
            "Xato javob chiqadi",
            "Sistema yechimsiz boʻlib qoladi",
        ],
        "correct": "10 = 10 kabi hech narsa bermaydigan tenglik",
        "explanation": "<p><strong>10 = 10 chiqadi.</strong> x + (10 − x) = 10 → "
                       "10 = 10 — toʻgʻri, lekin foydasiz: ifoda oʻsha "
                       "tenglamadan olingan edi. Yangi maʼlumot faqat "
                       "<em>ikkinchi</em> tenglamada bor, ifodani oʻsha yerga "
                       "qoʻyish kerak.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Sistema: x + y = 20 va "
                "25x + 15y = 380. Oʻquvchi y = 20 − x deb topdi va shunday yozdi: "
                "«25x + 15 × 20 − x = 380».</p><p><strong>Xato "
                "qayerda?</strong></p>",
        "choices": [
            "Ifodani qavsga olmagan",
            "y ni notoʻgʻri ifodalagan",
            "Ikkinchi tenglamani notoʻgʻri koʻchirgan",
            "Xato yoʻq, yozuv toʻgʻri",
        ],
        "correct": "Ifodani qavsga olmagan",
        "explanation": "<p><strong>Ifodani qavsga olmagan.</strong> Toʻgʻrisi "
                       "25x + 15(20 − x) = 380, yaʼni 25x + 300 − 15x = 380. "
                       "Qavssiz yozuvda 15 faqat 20 ga koʻpaydi va −x yolgʻiz "
                       "qoldi — bu butunlay boshqa tenglama.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Sistema: x + y = 10 va 2x + y = 16. "
                "Oʻquvchi x = 6 ni topdi va «javob: 6» deb yozdi.</p>"
                "<p><strong>Kamchilik nimada?</strong></p>",
        "choices": [
            "y ni topmagan — javob (6; 4) boʻlishi kerak",
            "x ni notoʻgʻri topgan, x = 4 boʻladi",
            "Sistemani notoʻgʻri yozgan",
            "Kamchilik yoʻq, javob toʻliq",
        ],
        "correct": "y ni topmagan — javob (6; 4) boʻlishi kerak",
        "explanation": "<p><strong>y ni topmagan.</strong> x = 6 toʻgʻri, lekin "
                       "sistemaning yechimi — juftlik: y = 10 − 6 = 4. "
                       "Tekshirish: 6 + 4 = 10 ✓ va 2 × 6 + 4 = 16 ✓ Javob "
                       "(6; 4).</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Masalani yeching.</p><p>Kafeda 2 ta choy va 3 ta non uchun "
                "26 000 soʻm toʻlandi. Boshqa stolda 1 ta choy va 1 ta non uchun "
                "10 000 soʻm toʻlandi.</p><p><strong>Bitta choy necha "
                "soʻm?</strong></p>",
        "choices": ["3 000 soʻm", "4 000 soʻm", "5 000 soʻm", "6 000 soʻm"],
        "correct": "4 000 soʻm",
        "explanation": "<p><strong>4 000 soʻm.</strong> c — choy, n — non narxi. "
                       "Shartlar: c + n = 10 000 va 2c + 3n = 26 000. "
                       "c = 10 000 − n ni qoʻyamiz: 20 000 − 2n + 3n = 26 000 → "
                       "n = 6 000, demak c = 4 000. Tekshirish: "
                       "8 000 + 18 000 = 26 000 ✓ <strong>6 000</strong> — non "
                       "narxi: qaysi nomaʼlum soʻralganini eʼtibordan "
                       "chiqarish.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Hovlida velosiped va yengil mashinalar "
                "turibdi — jami 20 ta transport va 56 ta gʻildirak. Velosipedning "
                "2 ta, mashinaning 4 ta gʻildiragi bor.</p><p><strong>Nechta "
                "mashina bor?</strong></p>",
        "choices": ["6 ta", "8 ta", "12 ta", "14 ta"],
        "correct": "8 ta",
        "explanation": "<p><strong>8 ta.</strong> v — velosiped, m — mashina. "
                       "v + m = 20 va 2v + 4m = 56. v = 20 − m ni qoʻyamiz: "
                       "40 − 2m + 4m = 56 → 2m = 16 → m = 8, v = 12. "
                       "Tekshirish: 8 + 12 = 20 ✓ va 32 + 24 = 56 ✓ "
                       "<strong>12 ta</strong> — velosipedlar soni.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-51 Mashq: Real hayot grafigini oʻqish",
        "description": "20 savol — oʻqlar va shkala, koʻtarilish/tekis/pasayish, "
                       "masofa–vaqt grafigi va oʻrtacha tezlik.",
        "tutorial":    "PM-51:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM51,
    },
    {
        "title":       "PM-52 Mashq: Ikki chiziqning kesishishi",
        "description": "20 savol — sistema nima, yechimni tekshirish, "
                       "tenglashtirish usuli va uchta mumkin boʻlgan hol.",
        "tutorial":    "PM-52:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM52,
    },
    {
        "title":       "PM-53 Mashq: Sistema: oʻrniga qoʻyish usuli",
        "description": "20 savol — nomaʼlumni ifodalash, qavs bilan qoʻyish, "
                       "qaytarish va tekshirish.",
        "tutorial":    "PM-53:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM53,
    },
]
