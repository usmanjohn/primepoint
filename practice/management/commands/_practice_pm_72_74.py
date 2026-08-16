# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-72, PM-73, PM-74 (oʻxshashlik va masshtab,
simmetriya, hajm va sirt yuzasi).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: uchalasi ham `hard` (PM-71 dan boshlab).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq: variantlarda x<sup>2</sup> emas,
   Unicode ², ³ yoziladi (m², sm³).
⚠️ Kumulyativ:
   • PM-72 — oʻxshashlik va masshtab. Yuza k² marta oʻsadi;
     ⛔ hajm va k³ YOʻQ (PM-74);
   • PM-73 — simmetriya, harakatlar, koordinatada aks ettirish;
     ⛔ hajm YOʻQ;
   • PM-74 — hajm, sirt yuzasi, litr, silindr. Silindr asosi PM-71 dan.
     ⛔ Konus, shar, piramida YOʻQ. Kub ildizi ATAMA sifatida yoʻq —
     125 = 5 × 5 × 5 tanlash yoʻli bilan topiladi.
⚠️ π ≈ 3,14 hamma joyda.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_72_74.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Matematika",
    "description": "Matematika — Prime Math darslarining mashqlari",
    "icon":        "bi-calculator",
    "color":       "#f59e0b",
}

DEFAULTS = {
    "level":                "hard",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PM-72 — oʻxshashlik va masshtab
# =====================================================================

Q_PM72 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>Oʻxshash uchburchaklarning "
                "kichigida tomon 5 sm, kattasida unga mos tomon 15 sm. "
                "Oʻxshashlik koeffitsienti qancha?</strong></p>",
        "choices": ["3", "5", "10", "75"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> k = katta ÷ kichik = "
                       "15 ÷ 5 = 3. <strong>10</strong> — tomonlar ayirilgan "
                       "(15 − 5); koeffitsient boʻlish bilan topiladi. "
                       "<strong>75</strong> — koʻpaytirilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Oʻxshashlik koeffitsienti k = 4. "
                "Kichik shaklning tomoni 7 sm boʻlsa, kattasiniki "
                "qancha?</strong></p>",
        "choices": ["1,75 sm", "11 sm", "28 sm", "112 sm"],
        "correct": "28 sm",
        "explanation": "<p><strong>28 sm.</strong> 7 × 4 = 28. "
                       "<strong>1,75 sm</strong> — koʻpaytirish oʻrniga "
                       "boʻlingan; katta shaklning tomoni kichigidan katta "
                       "boʻlishi kerak. <strong>11 sm</strong> — "
                       "qoʻshilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>1 : 100 masshtabli rejada "
                "devor 5 sm. Haqiqiy uzunligi qancha?</strong></p>",
        "choices": ["0,05 m", "5 m", "50 m", "500 m"],
        "correct": "5 m",
        "explanation": "<p><strong>5 m.</strong> Chizmadan hayotga "
                       "oʻtayotganda koʻpaytiriladi: 5 × 100 = 500 sm = 5 m. "
                       "<strong>500 m</strong> — santimetrni metrga "
                       "oʻgirish unutilgan. <strong>0,05 m</strong> — "
                       "boʻlingan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>1 : 50 masshtabli chizmada "
                "haqiqiy uzunligi 4 m boʻlgan devor necha santimetr boʻlib "
                "chiziladi?</strong></p>",
        "choices": ["0,08 sm", "8 sm", "80 sm", "200 sm"],
        "correct": "8 sm",
        "explanation": "<p><strong>8 sm.</strong> Avval bitta birlikka: "
                       "4 m = 400 sm. Keyin hayotdan chizmaga oʻtayotganda "
                       "boʻlinadi: 400 ÷ 50 = 8 sm. <strong>200 sm</strong> — "
                       "4 × 50 hisoblangan, yaʼni birlik almashtirilmay "
                       "koʻpaytirilgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki uchburchak "
                "oʻxshash ekanini bilish uchun nima yetarli?</strong></p>",
        "choices": [
            "Ikkita burchagi mos ravishda teng boʻlsa",
            "Bitta tomoni teng boʻlsa",
            "Yuzalari teng boʻlsa",
            "Perimetrlari teng boʻlsa",
        ],
        "correct": "Ikkita burchagi mos ravishda teng boʻlsa",
        "explanation": "<p><strong>Ikkita burchagi mos ravishda teng "
                       "boʻlsa.</strong> Uchburchakda burchaklar yigʻindisi "
                       "180° (PM-61), shuning uchun ikkitasi mos tushsa, "
                       "uchinchisi oʻz-oʻzidan mos tushadi. Teng yuza yoki "
                       "teng perimetr oʻxshashlikni umuman "
                       "kafolatlamaydi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Kichik uchburchakning tomonlari "
                "3 sm, 5 sm va 7 sm. Katta uchburchakda 3 sm ga mos tomon "
                "12 sm.</p><p><strong>Katta uchburchakning perimetri "
                "qancha?</strong></p>",
        "choices": ["15 sm", "30 sm", "60 sm", "240 sm"],
        "correct": "60 sm",
        "explanation": "<p><strong>60 sm.</strong> k = 12 ÷ 3 = 4. Tomonlar: "
                       "12, 20 va 28; perimetri 12 + 20 + 28 = 60 sm. "
                       "Tezroq yoʻl: perimetr ham k marta oshadi — "
                       "(3 + 5 + 7) × 4 = 15 × 4 = 60. <strong>15 sm</strong> "
                       "— kichigining perimetri.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ustunning balandligi 2 m, soyasi "
                "1,5 m. Shu payt binoning soyasi 9 m.</p><p><strong>Bino necha "
                "metr?</strong></p>",
        "choices": ["6,75 m", "12 m", "13,5 m", "18 m"],
        "correct": "12 m",
        "explanation": "<p><strong>12 m.</strong> Boʻy ÷ soya ikkalasida ham "
                       "bir xil: 2 ÷ 1,5 va h ÷ 9. Demak "
                       "h = 9 × 2 ÷ 1,5 = 18 ÷ 1,5 = 12 m. "
                       "<strong>6,75 m</strong> — nisbat teskari yozilgan "
                       "(9 × 1,5 ÷ 2); u holda bino soyasidan past chiqib "
                       "qoladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>1 : 50 000 masshtabli "
                "xaritada ikki shahar orasi 6 sm. Haqiqiy masofa necha "
                "kilometr?</strong></p>",
        "choices": ["0,3 km", "3 km", "30 km", "300 km"],
        "correct": "3 km",
        "explanation": "<p><strong>3 km.</strong> 6 × 50 000 = 300 000 sm. "
                       "Keyin bosqichma-bosqich: 300 000 sm = 3000 m = 3 km. "
                       "<strong>300 km</strong> — santimetr toʻgʻridan-toʻgʻri "
                       "kilometr deb oʻqilgan; birlikni ikki qadamda "
                       "oʻgiring.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Shaklning tomonlari "
                "4 marta oshdi. Yuzasi necha marta oshadi?</strong></p>",
        "choices": ["4 marta", "8 marta", "16 marta", "64 marta"],
        "correct": "16 marta",
        "explanation": "<p><strong>16 marta.</strong> Yuzada ikkita oʻlcham "
                       "bor va ikkalasi ham 4 marta oshadi: 4 × 4 = "
                       "4<sup>2</sup> = 16. <strong>4 marta</strong> — "
                       "tomonlar shunday oshadi, yuza emas. "
                       "<strong>64 marta</strong> — bu 4<sup>3</sup>.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Kichik toʻgʻri toʻrtburchak "
                "3 sm × 5 sm. U k = 2 koeffitsient bilan "
                "kattalashtirildi.</p><p><strong>Katta toʻrtburchakning yuzasi "
                "qancha?</strong></p>",
        "choices": ["15 sm²", "30 sm²", "60 sm²", "120 sm²"],
        "correct": "60 sm²",
        "explanation": "<p><strong>60 sm².</strong> Yangi tomonlar: 6 sm va "
                       "10 sm, yuzasi 6 × 10 = 60 sm². Tekshirish: kichigining "
                       "yuzasi 15 sm², va 15 × 2<sup>2</sup> = 60 ✓ "
                       "<strong>30 sm²</strong> — yuza ham 2 marta oshadi deb "
                       "hisoblangan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>1 : 200 masshtabli chizmada "
                "uzunligi 24 m boʻlgan bino necha santimetr boʻladi?</strong></p>",
        "choices": ["1,2 sm", "12 sm", "48 sm", "120 sm"],
        "correct": "12 sm",
        "explanation": "<p><strong>12 sm.</strong> 24 m = 2400 sm, keyin "
                       "2400 ÷ 200 = 12 sm. <strong>1,2 sm</strong> — "
                       "24 ÷ 200 hisoblangan, birlik almashtirilmagan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki shakl oʻxshash, k = 1,5. "
                "Kichigining perimetri 24 sm.</p><p><strong>Kattasining "
                "perimetri qancha?</strong></p>",
        "choices": ["16 sm", "25,5 sm", "36 sm", "54 sm"],
        "correct": "36 sm",
        "explanation": "<p><strong>36 sm.</strong> Perimetr — uzunlik, demak u "
                       "ham k marta oshadi: 24 × 1,5 = 36 sm. "
                       "<strong>16 sm</strong> — koʻpaytirish oʻrniga "
                       "boʻlingan. Diqqat: yuza boshqacha — u "
                       "1,5<sup>2</sup> = 2,25 marta oshardi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Fotosurat ikki marta "
                "kattalashtirildi.</p><p><strong>Qaysi jumla "
                "toʻgʻri?</strong></p>",
        "choices": [
            "Tomonlari 2 marta, yuzasi 4 marta oshdi",
            "Tomonlari ham, yuzasi ham 2 marta oshdi",
            "Tomonlari 4 marta, yuzasi 2 marta oshdi",
            "Tomonlari 2 marta oshdi, yuzasi oʻzgarmadi",
        ],
        "correct": "Tomonlari 2 marta, yuzasi 4 marta oshdi",
        "explanation": "<p><strong>Tomonlari 2 marta, yuzasi 4 marta "
                       "oshdi.</strong> Uzunlik k marta, yuza esa "
                       "k<sup>2</sup> marta oshadi. Masalan 8×12 li surat "
                       "16×24 boʻladi: 96 sm² dan 384 sm² ga, yaʼni roppa-rosa "
                       "4 marta.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>M 1 : 100 nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Chizma haqiqatdan 100 marta kichik",
            "Chizma haqiqatdan 100 marta katta",
            "Chizmadagi 100 sm hayotdagi 1 sm",
            "Yuza 100 marta kichik",
        ],
        "correct": "Chizma haqiqatdan 100 marta kichik",
        "explanation": "<p><strong>Chizma haqiqatdan 100 marta kichik.</strong> "
                       "Chapdagi 1 — chizma, oʻngdagi 100 — hayot: chizmadagi "
                       "1 sm hayotdagi 100 sm, yaʼni 1 metr. Yuza esa "
                       "100 marta emas, 100<sup>2</sup> = 10 000 marta "
                       "kichik boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Har qanday ikkita "
                "toʻgʻri toʻrtburchak oʻxshashmi?</strong></p>",
        "choices": [
            "Yoʻq — tomonlarining nisbati har xil boʻlishi mumkin",
            "Ha — hammasining burchagi 90°",
            "Ha, agar yuzalari teng boʻlsa",
            "Faqat kattalari oʻxshash boʻladi",
        ],
        "correct": "Yoʻq — tomonlarining nisbati har xil boʻlishi mumkin",
        "explanation": "<p><strong>Yoʻq.</strong> Burchaklar teng boʻlishi "
                       "yetarli emas — tomonlar ham bir xil nisbatda boʻlishi "
                       "shart. 2×3 va 2×6 toʻrtburchaklarning burchagi bir "
                       "xil, lekin biri ikkinchisining kattalashtirilgan "
                       "nusxasi emas. Kvadratlar esa har doim oʻxshash.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Xaritaning masshtabi "
                "1 : 1000.</p><p><strong>Xaritadagi 1 sm² qancha yuzani "
                "bildiradi?</strong></p>",
        "choices": ["10 m²", "100 m²", "1000 m²", "10 000 m²"],
        "correct": "100 m²",
        "explanation": "<p><strong>100 m².</strong> Avval uzunlik: xaritadagi "
                       "1 sm = 1000 sm = 10 m. Yuza esa kvadratga koʻtariladi: "
                       "10 × 10 = 100 m². <strong>1000 m²</strong> — "
                       "masshtab yuzaga toʻgʻridan-toʻgʻri qoʻllanilgan; "
                       "yuzada koeffitsient har doim kvadratlanadi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>Masshtab 1 : 50, chizmada devor "
                "14 sm.<br>Yechim: <strong>14 ÷ 50 = 0,28 sm</strong></p>",
        "choices": [
            "Boʻlingan; toʻgʻrisi 14 × 50 = 700 sm = 7 m",
            "Masshtab notoʻgʻri oʻqilgan; toʻgʻrisi 0,28 m",
            "Avval metrga oʻtish kerak edi; toʻgʻrisi 0,7 m",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Boʻlingan; toʻgʻrisi 14 × 50 = 700 sm = 7 m",
        "explanation": "<p><strong>Boʻlingan.</strong> Chizmadan hayotga "
                       "oʻtayotganda koʻpaytiriladi: 14 × 50 = 700 sm = 7 m. "
                       "Javobni mantiqqa soling — haqiqiy devor chizmadagidan "
                       "kichik (0,28 sm) boʻlishi mumkin emas.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Ustun 2 m, soyasi 5 m; daraxtning "
                "soyasi 20 m.<br>Yechim: <strong>h = 20 × 5 ÷ 2 = 50 m</strong></p>",
        "choices": [
            "Nisbat teskari; toʻgʻrisi 20 × 2 ÷ 5 = 8 m",
            "Soyalarni qoʻshish kerak edi",
            "Ustunning balandligi ishlatilmasligi kerak edi",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Nisbat teskari; toʻgʻrisi 20 × 2 ÷ 5 = 8 m",
        "explanation": "<p><strong>Nisbat teskari.</strong> Bu yerda soya "
                       "boʻydan uzun (5 &gt; 2), demak daraxt ham oʻz "
                       "soyasidan past boʻlishi kerak: h = 20 × 2 ÷ 5 = 8 m. "
                       "50 m — 20 m li soyaga umuman toʻgʻri kelmaydi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Sherbek 1 : 25 000 masshtabli "
                "xaritada uyidan bobosining qishlogʻigacha boʻlgan yoʻlni "
                "chizgʻich bilan oʻlchadi: 12 sm chiqdi.</p><p><strong>Haqiqiy "
                "masofa necha kilometr?</strong></p>",
        "choices": ["0,3 km", "3 km", "30 km", "300 km"],
        "correct": "3 km",
        "explanation": "<p><strong>3 km.</strong> 12 × 25 000 = 300 000 sm. "
                       "Keyin 300 000 sm = 3000 m = 3 km. "
                       "<strong>30 km</strong> — metrdan kilometrga oʻtishda "
                       "yana bir marta 1000 ga boʻlish unutilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Dilnoza sinf xonasining rejasini "
                "1 : 100 masshtabda chizdi. Chizmada xona 9 sm × 6 sm "
                "boʻldi.</p><p><strong>Haqiqiy sinfning yuzasi necha kvadrat "
                "metr?</strong></p>",
        "choices": ["0,54 m²", "5,4 m²", "54 m²", "540 m²"],
        "correct": "54 m²",
        "explanation": "<p><strong>54 m².</strong> Avval haqiqiy oʻlchamlar: "
                       "9 × 100 = 900 sm = 9 m va 6 × 100 = 600 sm = 6 m. "
                       "Keyin yuza: 9 × 6 = 54 m². <strong>0,54 m²</strong> — "
                       "chizmadagi yuza (54 sm²) toʻgʻridan-toʻgʻri metrga "
                       "oʻgirilgan; yuzani hisoblashdan oldin uzunliklarni "
                       "oʻgirish kerak.</p>",
    },
]


# =====================================================================
# PM-73 — simmetriya, koʻchirish va burilish
# =====================================================================

Q_PM73 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Kvadratning nechta "
                "simmetriya oʻqi bor?</strong></p>",
        "choices": ["1 ta", "2 ta", "4 ta", "8 ta"],
        "correct": "4 ta",
        "explanation": "<p><strong>4 ta.</strong> Ikkitasi qarama-qarshi "
                       "tomonlarning oʻrtasidan, ikkitasi diagonallar boʻylab. "
                       "<strong>2 ta</strong> — toʻgʻri toʻrtburchakniki; "
                       "kvadratda tomonlar teng boʻlgani uchun diagonallar "
                       "ham oʻq boʻla oladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Kvadrat boʻlmagan "
                "toʻgʻri toʻrtburchakda nechta simmetriya oʻqi bor?</strong></p>",
        "choices": ["0 ta", "2 ta", "4 ta", "Cheksiz koʻp"],
        "correct": "2 ta",
        "explanation": "<p><strong>2 ta.</strong> Faqat qarama-qarshi "
                       "tomonlarning oʻrtasidan oʻtuvchi ikkita chiziq. "
                       "Diagonal bu yerda oʻq emas: uni diagonal boʻylab "
                       "bukkanda uzun tomon qisqasining ustiga "
                       "tushmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Teng tomonli "
                "uchburchakda nechta simmetriya oʻqi bor?</strong></p>",
        "choices": ["0 ta", "1 ta", "3 ta", "6 ta"],
        "correct": "3 ta",
        "explanation": "<p><strong>3 ta.</strong> Har bir uchidan "
                       "qarama-qarshi tomonning oʻrtasiga bittadan. "
                       "<strong>1 ta</strong> — teng <em>yonli</em> "
                       "uchburchakniki, unda faqat ikkita tomon teng.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>A (4; 1) nuqtaning "
                "x oʻqiga nisbatan aksi qaysi nuqta?</strong></p>",
        "choices": ["(4; −1)", "(−4; 1)", "(−4; −1)", "(1; 4)"],
        "correct": "(4; −1)",
        "explanation": "<p><strong>(4; −1).</strong> x oʻqiga nisbatan aks "
                       "ettirilganda nuqta pastga tushadi, demak <b>y</b> ning "
                       "ishorasi almashadi, x oʻzgarmaydi. "
                       "<strong>(−4; 1)</strong> — bu y oʻqiga nisbatan "
                       "aks.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Doiraning nechta "
                "simmetriya oʻqi bor?</strong></p>",
        "choices": ["1 ta", "2 ta", "4 ta", "Cheksiz koʻp"],
        "correct": "Cheksiz koʻp",
        "explanation": "<p><strong>Cheksiz koʻp.</strong> Markazdan oʻtgan "
                       "<em>har qanday</em> chiziq doirani teng ikkiga "
                       "boʻladi. Shu sababli doiraning burilish simmetriyasi "
                       "ham cheksiz — uni istalgan burchakka bursangiz, "
                       "oʻzgarmaydi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Parallelogrammning "
                "nechta simmetriya oʻqi bor?</strong></p>",
        "choices": ["0 ta", "1 ta", "2 ta", "4 ta"],
        "correct": "0 ta",
        "explanation": "<p><strong>0 ta.</strong> Parallelogrammni hech qanday "
                       "chiziq boʻylab bukib boʻlmaydi — diagonali ham oʻq "
                       "emas. <strong>2 ta</strong> — rombniki (uning "
                       "diagonallari oʻq), lekin oddiy parallelogrammda "
                       "tomonlar teng emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Parallelogrammning "
                "burilish simmetriyasi tartibi qancha?</strong></p>",
        "choices": ["1", "2", "3", "4"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Markazi atrofida 180° ga "
                       "burilganda parallelogramm oʻzidek boʻlib qoladi, "
                       "360° da esa buni ikki marta bajaradi. Eʼtibor bering: "
                       "simmetriya oʻqi boʻlmasa ham, burilish simmetriyasi "
                       "boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Burilish simmetriyasining tartibi "
                "6 boʻlsa, naqsh necha gradusga burilganda "
                "oʻzgarmaydi?</strong></p>",
        "choices": ["30°", "60°", "72°", "120°"],
        "correct": "60°",
        "explanation": "<p><strong>60°.</strong> Burilish burchagi = "
                       "360° ÷ tartib = 360 ÷ 6 = 60°. <strong>72°</strong> — "
                       "tartibi 5 boʻlgan naqshniki, <strong>120°</strong> — "
                       "tartibi 3 boʻlganiniki.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Naqsh 72° ga burilganda "
                "oʻzgarmaydi. Uning burilish simmetriyasi tartibi "
                "qancha?</strong></p>",
        "choices": ["3", "4", "5", "72"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Tartib = 360° ÷ burchak = "
                       "360 ÷ 72 = 5. Yaʼni naqsh besh qirrali yulduz kabi "
                       "tuzilgan. Tekshirish: 72 × 5 = 360 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>B (−3; 5) nuqtaning "
                "y oʻqiga nisbatan aksi qaysi nuqta?</strong></p>",
        "choices": ["(3; 5)", "(−3; −5)", "(3; −5)", "(5; −3)"],
        "correct": "(3; 5)",
        "explanation": "<p><strong>(3; 5).</strong> y oʻqiga nisbatan aks "
                       "ettirilganda nuqta oʻngdan chapga (yoki aksincha) "
                       "oʻtadi, demak <b>x</b> ning ishorasi almashadi. "
                       "<strong>(−3; −5)</strong> — bu x oʻqiga nisbatan "
                       "aks.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>C (2; −4) nuqta "
                "koordinata boshi atrofida 180° ga burilsa, qayerga "
                "tushadi?</strong></p>",
        "choices": ["(−2; 4)", "(2; 4)", "(−2; −4)", "(−4; 2)"],
        "correct": "(−2; 4)",
        "explanation": "<p><strong>(−2; 4).</strong> 180° burilishda ikkala "
                       "ishora ham almashadi: (x; y) → (−x; −y). "
                       "<strong>(2; 4)</strong> — faqat y almashgan, bu x "
                       "oʻqiga nisbatan aks.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>A (1; 2) nuqta "
                "(4; −3) ga koʻchirilsa, qayerga tushadi?</strong></p>",
        "choices": ["(5; −1)", "(3; 5)", "(4; −6)", "(−3; 5)"],
        "correct": "(5; −1)",
        "explanation": "<p><strong>(5; −1).</strong> Koʻchirishda sonlar "
                       "qoʻshiladi: (1 + 4; 2 + (−3)) = (5; −1). "
                       "<strong>(3; 5)</strong> — ayirilgan. Koʻchirish "
                       "shaklning oʻlchamini oʻzgartirmaydi, faqat "
                       "siljitadi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Koʻchirish, burilish "
                "va aks ettirishdan qaysi biri shaklning oʻlchamini "
                "oʻzgartiradi?</strong></p>",
        "choices": [
            "Hech qaysisi — uchalasi ham oʻlchamni saqlaydi",
            "Faqat burilish",
            "Faqat aks ettirish",
            "Uchalasi ham oʻzgartiradi",
        ],
        "correct": "Hech qaysisi — uchalasi ham oʻlchamni saqlaydi",
        "explanation": "<p><strong>Hech qaysisi.</strong> Bu uchta harakat "
                       "shaklning faqat oʻrnini yoki holatini oʻzgartiradi; "
                       "tomonlar ham, burchaklar ham, yuza ham oʻsha-oʻsha "
                       "qoladi. Oʻlcham oʻzgarishi uchun oʻxshashlik kerak "
                       "(PM-72).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Rombning nechta "
                "simmetriya oʻqi bor?</strong></p>",
        "choices": ["0 ta", "2 ta", "4 ta", "Cheksiz koʻp"],
        "correct": "2 ta",
        "explanation": "<p><strong>2 ta — ikkala diagonali.</strong> Rombda "
                       "toʻrtala tomon teng, shuning uchun diagonal boʻylab "
                       "bukkanda ikki yarmi mos tushadi. Diqqat: toʻgʻri "
                       "toʻrtburchakda esa aksincha — oʻrta chiziqlar oʻq, "
                       "diagonallar emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Toʻgʻri "
                "toʻrtburchakning diagonali simmetriya oʻqimi?</strong></p>",
        "choices": [
            "Yoʻq — u faqat kvadratda oʻq boʻladi",
            "Ha — u shaklni teng ikkiga boʻladi",
            "Ha — har qanday diagonal simmetriya oʻqi",
            "Faqat yuzasi katta boʻlsa",
        ],
        "correct": "Yoʻq — u faqat kvadratda oʻq boʻladi",
        "explanation": "<p><strong>Yoʻq.</strong> Diagonal shaklni teng ikkita "
                       "<em>yuzaga</em> boʻladi, lekin bu yetarli emas: "
                       "simmetriya oʻqi uchun ikki yarim buklaganda "
                       "ustma-ust tushishi kerak. Bir varaq qogʻozni "
                       "diagonal boʻylab bukib koʻring — chekkasi osilib "
                       "qoladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi shaklda "
                "simmetriya oʻqi yoʻq, lekin burilish simmetriyasi "
                "bor?</strong></p>",
        "choices": ["Parallelogramm", "Kvadrat", "Romb", "Teng yonli trapetsiya"],
        "correct": "Parallelogramm",
        "explanation": "<p><strong>Parallelogramm.</strong> Uning bitta ham "
                       "oʻqi yoʻq, lekin 180° ga burilganda oʻzidek boʻladi "
                       "(tartibi 2). Kvadratda 4 ta oʻq, rombda 2 ta, teng "
                       "yonli trapetsiyada 1 ta oʻq bor.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>A (3; 5) nuqtaning y oʻqiga "
                "nisbatan aksi topilmoqchi.<br>Yechim: "
                "<strong>A′ (3; −5)</strong></p>",
        "choices": [
            "y oʻqida x almashadi; toʻgʻrisi (−3; 5)",
            "Ikkala ishora ham almashishi kerak edi; toʻgʻrisi (−3; −5)",
            "Nuqta oʻzgarmaydi; toʻgʻrisi (3; 5)",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "y oʻqida x almashadi; toʻgʻrisi (−3; 5)",
        "explanation": "<p><strong>y oʻqida x almashadi.</strong> Qoidani "
                       "shunday eslang: <em>oʻqning nomi emas, ikkinchisi "
                       "almashadi</em>. y oʻqiga nisbatan — x oʻzgaradi, "
                       "x oʻqiga nisbatan — y oʻzgaradi. Yozilgan (3; −5) — "
                       "x oʻqiga nisbatan aks.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>«Kvadratning 4 ta simmetriya oʻqi "
                "bor, demak toʻgʻri toʻrtburchakning ham 4 ta — u ham "
                "toʻrtburchak.»</p>",
        "choices": [
            "Toʻgʻri toʻrtburchakda diagonal oʻq emas; oʻqlari 2 ta",
            "Toʻgʻri toʻrtburchakda umuman oʻq yoʻq",
            "Kvadratda 2 ta oʻq bor, 4 ta emas",
            "Xato yoʻq, xulosa toʻgʻri",
        ],
        "correct": "Toʻgʻri toʻrtburchakda diagonal oʻq emas; oʻqlari 2 ta",
        "explanation": "<p><strong>Diagonal oʻq emas.</strong> Kvadratda "
                       "diagonal ishlaydi, chunki tomonlari teng. Kvadrat "
                       "boʻlmagan toʻgʻri toʻrtburchakda esa faqat ikkita "
                       "oʻrta chiziq qoladi — 2 ta oʻq. Bir turdagi shakl "
                       "boʻlishi xossalarning bir xil boʻlishini "
                       "anglatmaydi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Naqqosh hoshiyaga naqsh soladi. "
                "Naqshning takrorlanuvchi boʻlagi 30 sm, hoshiyaning uzunligi "
                "esa 4,5 metr.</p><p><strong>Boʻlak necha marta "
                "takrorlanadi?</strong></p>",
        "choices": ["12 marta", "15 marta", "135 marta", "150 marta"],
        "correct": "15 marta",
        "explanation": "<p><strong>15 marta.</strong> Avval birlik: 4,5 m = "
                       "450 sm. Keyin 450 ÷ 30 = 15. Bu — koʻchirish: bitta "
                       "boʻlak oʻzgarmagan holda 15 marta siljitib qoʻyiladi. "
                       "<strong>150 marta</strong> — 4,5 m 4500 sm deb "
                       "olingan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Usta kvadrat plitka uchun naqsh "
                "chizmoqchi. Plitkaning tomoni 50 sm, naqshning burilish "
                "simmetriyasi esa 4 — plitkani 90° ga bursa, naqsh "
                "oʻzgarmaydi.</p><p><strong>Usta naqshning necha kvadrat "
                "santimetrini chizsa yetarli?</strong></p>",
        "choices": ["625 sm²", "1250 sm²", "2500 sm²", "10 000 sm²"],
        "correct": "625 sm²",
        "explanation": "<p><strong>625 sm².</strong> Plitkaning yuzasi "
                       "50 × 50 = 2500 sm². Burilish simmetriyasi 4 boʻlgani "
                       "uchun chorak qismini chizish kifoya: 2500 ÷ 4 = "
                       "625 sm², qolgan uchtasi burib chiqiladi. "
                       "<strong>1250 sm²</strong> — yarmi; u faqat simmetriya "
                       "tartibi 2 boʻlganda toʻgʻri boʻlardi.</p>",
    },
]


# =====================================================================
# PM-74 — hajm va sirt yuzasi
# =====================================================================

Q_PM74 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>Qutining qirralari 3 sm, 4 sm va "
                "5 sm. Hajmi qancha?</strong></p>",
        "choices": ["12 sm³", "47 sm³", "60 sm³", "94 sm³"],
        "correct": "60 sm³",
        "explanation": "<p><strong>60 sm³.</strong> V = 3 × 4 × 5 = 60. "
                       "<strong>94 sm³</strong> — bu qutining sirt yuzasi "
                       "(94 sm²), hajmi emas; birlikka qarang. "
                       "<strong>12 sm³</strong> — qirralar qoʻshilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Kubning qirrasi 4 sm. Hajmi "
                "qancha?</strong></p>",
        "choices": ["12 sm³", "16 sm³", "64 sm³", "96 sm³"],
        "correct": "64 sm³",
        "explanation": "<p><strong>64 sm³.</strong> V = a<sup>3</sup> = "
                       "4 × 4 × 4 = 64. <strong>16 sm³</strong> — faqat "
                       "kvadratga koʻtarilgan (bu bitta yoqning yuzasi), "
                       "<strong>96 sm³</strong> — sirt yuzasi (6 × 16).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Kubning qirrasi 2 sm. Sirt yuzasi "
                "qancha?</strong></p>",
        "choices": ["8 sm²", "12 sm²", "24 sm²", "48 sm²"],
        "correct": "24 sm²",
        "explanation": "<p><strong>24 sm².</strong> S = 6 × a<sup>2</sup> = "
                       "6 × 4 = 24. <strong>8 sm²</strong> — bu hajm "
                       "(8 sm³). Kubda hamma yoq bir xil, shuning uchun "
                       "bittasini topib oltiga koʻpaytiriladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>5000 sm³ necha litr?</strong></p>",
        "choices": ["0,5 litr", "5 litr", "50 litr", "500 litr"],
        "correct": "5 litr",
        "explanation": "<p><strong>5 litr.</strong> 1 litr = 1000 sm³, demak "
                       "5000 ÷ 1000 = 5. Oson yoʻl: oxiridan uchta nolni "
                       "oʻchiring. <strong>50 litr</strong> — 100 ga "
                       "boʻlingan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>1 m³ necha "
                "litr?</strong></p>",
        "choices": ["10 litr", "100 litr", "1000 litr", "10 000 litr"],
        "correct": "1000 litr",
        "explanation": "<p><strong>1000 litr.</strong> 1 m³ — tomoni 1 metr, "
                       "yaʼni 10 dm boʻlgan kub: 10 × 10 × 10 = 1000 kub "
                       "detsimetr, va har bir kub detsimetr — 1 litr. "
                       "<strong>10 000 litr</strong> — bu yuzaning "
                       "koeffitsienti (1 m² = 10 000 sm²).</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p><strong>Qutining oʻlchamlari "
                "10 sm × 8 sm × 5 sm. Uning hajmi necha litr?</strong></p>",
        "choices": ["0,4 litr", "4 litr", "40 litr", "400 litr"],
        "correct": "0,4 litr",
        "explanation": "<p><strong>0,4 litr.</strong> V = 10 × 8 × 5 = "
                       "400 sm³, keyin 400 ÷ 1000 = 0,4 litr. "
                       "<strong>400 litr</strong> — sm³ toʻgʻridan-toʻgʻri "
                       "litr deb oʻqilgan; bunday quti bir yarim chelakdan "
                       "koʻp suv sigʻdira olmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Oʻsha 10 sm × 8 sm × 5 sm "
                "qutining sirt yuzasi qancha?</strong></p>",
        "choices": ["170 sm²", "340 sm²", "400 sm²", "680 sm²"],
        "correct": "340 sm²",
        "explanation": "<p><strong>340 sm².</strong> 10 × 8 = 80, 8 × 5 = 40, "
                       "10 × 5 = 50; yigʻindisi 170; S = 2 × 170 = 340 sm². "
                       "<strong>170 sm²</strong> — ikkiga koʻpaytirish "
                       "unutilgan (oltita yoq bor, uchta emas). "
                       "<strong>400 sm²</strong> — bu hajm.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Akvariumning oʻlchamlari "
                "50 sm × 20 sm × 25 sm. Toʻla toʻldirilsa, necha litr suv "
                "sigʻadi?</strong></p>",
        "choices": ["2,5 litr", "25 litr", "250 litr", "25 000 litr"],
        "correct": "25 litr",
        "explanation": "<p><strong>25 litr.</strong> V = 50 × 20 × 25 = "
                       "25 000 sm³, keyin 25 000 ÷ 1000 = 25 litr. "
                       "<strong>25 000 litr</strong> — birlik "
                       "oʻgirilmagan; bu bir necha xona suvga teng "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Silindrning radiusi 3 m, "
                "balandligi 2 m. Hajmi qancha? (π ≈ 3,14)</strong></p>",
        "choices": ["28,26 m³", "56,52 m³", "113,04 m³", "226,08 m³"],
        "correct": "56,52 m³",
        "explanation": "<p><strong>56,52 m³.</strong> Asos yuzasi: "
                       "3,14 × 9 = 28,26 m². Hajm: 28,26 × 2 = 56,52 m³. "
                       "<strong>28,26 m³</strong> — balandlikka "
                       "koʻpaytirish unutilgan, bu shunchaki asosning "
                       "yuzasi. <strong>113,04 m³</strong> — radius oʻrniga "
                       "diametr (6 m) qoʻyilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>0,6 m³ necha litr?</strong></p>",
        "choices": ["6 litr", "60 litr", "600 litr", "6000 litr"],
        "correct": "600 litr",
        "explanation": "<p><strong>600 litr.</strong> 1 m³ = 1000 litr, demak "
                       "0,6 × 1000 = 600. <strong>60 litr</strong> — 100 ga "
                       "koʻpaytirilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Kubning hajmi "
                "125 sm³. Qirrasi qancha?</strong></p>",
        "choices": ["5 sm", "15 sm", "25 sm", "41,7 sm"],
        "correct": "5 sm",
        "explanation": "<p><strong>5 sm.</strong> Qaysi son oʻziga uch marta "
                       "koʻpaytirilganda 125 beradi? 5 × 5 × 5 = 125 ✓ "
                       "<strong>41,7 sm</strong> — 125 uchga boʻlingan; "
                       "kubda qirralar qoʻshilmaydi, koʻpaytiriladi. "
                       "<strong>25 sm</strong> — faqat ikkita koʻpaytuvchi "
                       "olingan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Suv baki 2 m × 1 m × 0,5 m. "
                "Toʻla bakda necha litr suv boʻladi?</strong></p>",
        "choices": ["1 litr", "10 litr", "100 litr", "1000 litr"],
        "correct": "1000 litr",
        "explanation": "<p><strong>1000 litr.</strong> V = 2 × 1 × 0,5 = "
                       "1 m³, va 1 m³ = 1000 litr. <strong>1 litr</strong> — "
                       "kub metrni litr deb yozib yuborilgan; bitta shisha "
                       "suv uchun bunday bak qurilmaydi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Qutining oʻlchamlari "
                "6 sm × 4 sm × 3 sm.</p><p><strong>Uning SIRT YUZASI "
                "qancha?</strong></p>",
        "choices": ["54 sm²", "72 sm²", "108 sm²", "144 sm²"],
        "correct": "108 sm²",
        "explanation": "<p><strong>108 sm².</strong> 6 × 4 = 24, 4 × 3 = 12, "
                       "6 × 3 = 18; yigʻindisi 54; S = 2 × 54 = 108 sm². "
                       "<strong>72 sm²</strong> — bu hajm (72 sm³), savol "
                       "esa sirt yuzasini soʻragan. <strong>54 sm²</strong> — "
                       "ikkiga koʻpaytirilmagan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Akvarium yasash uchun necha "
                "kvadrat metr shisha kerakligini bilmoqchimiz.</p><p><strong>Qaysi "
                "kattalikni hisoblash kerak?</strong></p>",
        "choices": [
            "Sirt yuzasini",
            "Hajmni",
            "Qirralarning yigʻindisini",
            "Asos yuzasini",
        ],
        "correct": "Sirt yuzasini",
        "explanation": "<p><strong>Sirt yuzasini.</strong> Shisha yoqlarni "
                       "qoplaydi, demak yoqlarning yuzasi kerak — javob "
                       "kvadrat metrda. Hajm esa ichiga qancha suv "
                       "sigʻishini aytadi va litrda oʻlchanadi. Bitta "
                       "akvarium — ikki xil savol.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi biri hajm "
                "birligi EMAS?</strong></p>",
        "choices": ["sm²", "sm³", "m³", "litr"],
        "correct": "sm²",
        "explanation": "<p><strong>sm².</strong> Kvadrat santimetr — yuzaning "
                       "birligi, yaʼni ikkita oʻlchamning koʻpaytmasi. Hajmda "
                       "uchta oʻlcham bor, shuning uchun uning birliklari "
                       "sm³, m³ yoki litr boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Kubning qirrasi "
                "2 marta oshsa, hajmi necha marta oshadi?</strong></p>",
        "choices": ["2 marta", "4 marta", "6 marta", "8 marta"],
        "correct": "8 marta",
        "explanation": "<p><strong>8 marta.</strong> Hajmda uchta oʻlcham bor "
                       "va uchalasi ham 2 marta oshadi: 2 × 2 × 2 = 8. "
                       "Tekshiring: a = 2 → 8 sm³, a = 4 → 64 sm³, va "
                       "64 ÷ 8 = 8 ✓ <strong>4 marta</strong> — yuza shunday "
                       "oshadi (PM-72), hajm esa yoʻq.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>Akvarium 50 sm × 30 sm × 40 sm, "
                "suv yuqori chetidan 10 sm past quyildi.<br>Yechim: "
                "<strong>50 × 30 × 40 = 60 000 sm³ = 60 litr</strong></p>",
        "choices": [
            "Suvning balandligi 30 sm; toʻgʻrisi 45 litr",
            "Litrga oʻgirishda xato; toʻgʻrisi 600 litr",
            "10 sm ni qoʻshish kerak edi; toʻgʻrisi 75 litr",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Suvning balandligi 30 sm; toʻgʻrisi 45 litr",
        "explanation": "<p><strong>Suvning balandligi 30 sm.</strong> "
                       "Formulaga qutining emas, suvning balandligi qoʻyiladi: "
                       "40 − 10 = 30 sm. Demak 50 × 30 × 30 = 45 000 sm³ = "
                       "45 litr. Masaladagi «10 sm past» shunchaki "
                       "qoʻyilgan son emas.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Yechim: <strong>2500 sm³ = "
                "25 litr</strong></p>",
        "choices": [
            "1000 ga boʻlinadi; toʻgʻrisi 2,5 litr",
            "1000 ga koʻpaytiriladi; toʻgʻrisi 2 500 000 litr",
            "10 ga boʻlinadi; toʻgʻrisi 250 litr",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "1000 ga boʻlinadi; toʻgʻrisi 2,5 litr",
        "explanation": "<p><strong>1000 ga boʻlinadi.</strong> 1 litr = "
                       "1000 sm³, demak 2500 ÷ 1000 = 2,5 litr. Bu yerda "
                       "100 ga boʻlingan — yuzadagi koeffitsient bilan "
                       "adashtirilgan. Hajmda nollar uchtadan yuradi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Karim aka qurilish uchun qum "
                "buyurtma qildi. Mashinaning kuzovi 3 m uzunlikda, 2 m enda va "
                "0,5 m chuqurlikda; u toʻla toʻldiriladi. Bir kub metr qum "
                "180 000 soʻm.</p><p><strong>Qum necha soʻm boʻladi?</strong></p>",
        "choices": ["180 000 soʻm", "360 000 soʻm", "540 000 soʻm",
                    "1 080 000 soʻm"],
        "correct": "540 000 soʻm",
        "explanation": "<p><strong>540 000 soʻm.</strong> Avval hajm: "
                       "3 × 2 × 0,5 = 3 m³. Keyin narx: 3 × 180 000 = "
                       "540 000 soʻm. <strong>1 080 000 soʻm</strong> — "
                       "0,5 ga koʻpaytirish oʻrniga tashlab yuborilgan "
                       "(6 m³ chiqadi).</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Nodira opa silindr shaklidagi "
                "idishda kompot pishirdi. Idishning radiusi 20 sm, kompotning "
                "balandligi 40 sm. Kompot 1,5 litrli shishalarga "
                "quyiladi.</p><p><strong>Necha dona shisha toʻla "
                "toʻladi?</strong></p>",
        "choices": ["25 ta", "33 ta", "34 ta", "50 ta"],
        "correct": "33 ta",
        "explanation": "<p><strong>33 ta.</strong> Asos yuzasi: 3,14 × 400 = "
                       "1256 sm². Hajm: 1256 × 40 = 50 240 sm³ = 50,24 litr. "
                       "Shishalar: 50,24 ÷ 1,5 = 33,49… Bu yerda javob "
                       "<em>pastga</em> yaxlitlanadi: 34-shisha toʻlmay "
                       "qoladi. <strong>34 ta</strong> — odatdagicha "
                       "yuqoriga yaxlitlangan, lekin savol «toʻla toʻladi» "
                       "deb soʻragan.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-72 Mashq: Oʻxshashlik va masshtab",
        "tutorial":    "PM-72:",
        "description": (
            "Oʻxshash shakllar, oʻxshashlik koeffitsienti, soya usuli, "
            "masshtab va yuzaning k² qoidasi. 20 savol."
        ),
        "questions":   Q_PM72,
        **DEFAULTS,
    },
    {
        "title":       "PM-73 Mashq: Simmetriya, koʻchirish va burilish",
        "tutorial":    "PM-73:",
        "description": (
            "Simmetriya oʻqlari, burilish simmetriyasi tartibi, uchta harakat "
            "va koordinatada aks ettirish. 20 savol."
        ),
        "questions":   Q_PM73,
        **DEFAULTS,
    },
    {
        "title":       "PM-74 Mashq: Fazoviy shakllar: hajm va sirt yuzasi",
        "tutorial":    "PM-74:",
        "description": (
            "Hajm va sirt yuzasi, yoyilma, sm³ va litr, silindr hamda "
            "hajmning k³ qoidasi. 20 savol."
        ),
        "questions":   Q_PM74,
        **DEFAULTS,
    },
]
