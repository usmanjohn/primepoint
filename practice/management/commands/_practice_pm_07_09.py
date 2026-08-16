# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-7 … PM-9 (tub sonlar, EKUB/EKUK, manfiy sonlar).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_07_09.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Matematika",
    "description": "Matematika — Prime Math darslarining mashqlari",
    "icon":        "bi-calculator",
    "color":       "#f59e0b",
}

DEFAULTS = {
    "level":                "easy",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PM-7 — tub va murakkab sonlar
# =====================================================================

Q_PM7 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Eng kichik tub son "
                "qaysi?</strong></p>",
        "choices": ["1", "2", "3", "0"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Uning roppa-rosa ikkita boʻluvchisi bor: "
                       "1 va 2. <strong>1</strong> tub emas — uning bitta boʻluvchisi "
                       "bor.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>1 soni qanday son?</strong></p>",
        "choices": ["Tub son", "Murakkab son", "Na tub, na murakkab", "Juft son"],
        "correct": "Na tub, na murakkab",
        "explanation": "<p><strong>Na tub, na murakkab.</strong> Tub son uchun roppa-rosa "
                       "ikkita boʻluvchi kerak, 1 da esa bittasi bor. Agar 1 tub "
                       "boʻlganda, sonni tub koʻpaytuvchilarga ajratish yoʻli yagona "
                       "boʻlmay qolardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son tub?</strong></p>",
        "choices": ["9", "15", "17", "21"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> 9 = 3 × 3, 15 = 3 × 5, 21 = 3 × 7 — "
                       "hammasi murakkab. 17 esa faqat 1 va 17 ga boʻlinadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2 soni nimasi bilan "
                "maxsus?</strong></p>",
        "choices": ["U yagona juft tub son", "U eng katta tub son",
                    "U ham tub, ham murakkab", "U hech qaysi songa boʻlinmaydi"],
        "correct": "U yagona juft tub son",
        "explanation": "<p><strong>Yagona juft tub son.</strong> Boshqa har qanday juft "
                       "son 2 ga boʻlinadi, demak uning kamida uchta boʻluvchisi bor va "
                       "u murakkab boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>7 sonining boʻluvchilari "
                "qaysilar?</strong></p>",
        "choices": ["1 va 7", "1, 3 va 7", "7 va 14", "Faqat 7"],
        "correct": "1 va 7",
        "explanation": "<p><strong>1 va 7.</strong> Har bir sonning kamida shu ikkita "
                       "boʻluvchisi bor; agar boshqasi boʻlmasa — son tub.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>51 tub sonmi?</strong></p>",
        "choices": ["Ha, chunki u toq", "Yoʻq, chunki 51 = 3 × 17",
                    "Ha, chunki 2 ga boʻlinmaydi", "Yoʻq, chunki u juft"],
        "correct": "Yoʻq, chunki 51 = 3 × 17",
        "explanation": "<p><strong>Yoʻq.</strong> Raqamlar yigʻindisi 5 + 1 = 6 uchga "
                       "boʻlinadi (PM-6), demak 51 ham boʻlinadi: 51 = 3 × 17. Toqlik "
                       "tublikni bildirmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>60 ning tub "
                "koʻpaytuvchilarga ajratmasi qaysi?</strong></p>",
        "choices": ["2 × 2 × 3 × 5", "4 × 15", "2 × 30", "2 × 3 × 5"],
        "correct": "2 × 2 × 3 × 5",
        "explanation": "<p><strong>2 × 2 × 3 × 5.</strong> Qolganlarida murakkab sonlar "
                       "qolib ketgan (4, 15, 30), oxirgisining koʻpaytmasi esa 30 — "
                       "60 emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>84 ning tub koʻpaytuvchilarga "
                "ajratmasi qaysi?</strong></p>",
        "choices": ["2 × 2 × 3 × 7", "2 × 42", "2 × 2 × 21", "3 × 4 × 7"],
        "correct": "2 × 2 × 3 × 7",
        "explanation": "<p><strong>2 × 2 × 3 × 7.</strong> 84 = 2 × 42 = 2 × 2 × 21 = "
                       "2 × 2 × 3 × 7. Qolgan variantlarda 42, 21 va 4 hali "
                       "murakkab.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>91 soni tubmi?</strong></p>",
        "choices": ["Ha", "Yoʻq, 91 = 7 × 13", "Yoʻq, 91 = 3 × 31", "Yoʻq, 91 juft"],
        "correct": "Yoʻq, 91 = 7 × 13",
        "explanation": "<p><strong>Yoʻq: 91 = 7 × 13.</strong> Tub sonlarga navbat bilan "
                       "boʻlamiz: 2 ✗, 3 ✗ (9 + 1 = 10), 5 ✗, 7 ✓. 91 koʻpincha tub deb "
                       "oʻylanadi — shuning uchun 7 ga tekshirishni unutmang.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>50 gacha (50 ni ham qoʻshib) "
                "nechta tub son bor?</strong></p>",
        "choices": ["10 ta", "12 ta", "15 ta", "25 ta"],
        "correct": "15 ta",
        "explanation": "<p><strong>15 ta:</strong> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, "
                       "31, 37, 41, 43, 47. Ularni Eratosfen gʻalviri bilan topish "
                       "mumkin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>45 ning ajratmasi "
                "qaysi?</strong></p>",
        "choices": ["3 × 3 × 5", "5 × 9", "3 × 15", "3 × 5 × 5"],
        "correct": "3 × 3 × 5",
        "explanation": "<p><strong>3 × 3 × 5 = 45.</strong> 5 × 9 va 3 × 15 da murakkab "
                       "son qolgan; 3 × 5 × 5 esa 75 ga teng.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son roppa-rosa ikkita "
                "tub sonning koʻpaytmasi?</strong></p>",
        "choices": ["15", "12", "16", "20"],
        "correct": "15",
        "explanation": "<p><strong>15 = 3 × 5</strong> — ikkalasi ham tub. 12 = 2 × 2 × 3 "
                       "(uchta koʻpaytuvchi), 16 = 2 × 2 × 2 × 2, 20 = 2 × 2 × 5.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>“Har qanday toq son tub "
                "boʻladi” — bu fikr toʻgʻrimi?</strong></p>",
        "choices": ["Yoʻq, masalan 9 = 3 × 3", "Ha, doim toʻgʻri",
                    "Ha, faqat 100 gacha", "Yoʻq, chunki toq sonlar juft boʻladi"],
        "correct": "Yoʻq, masalan 9 = 3 × 3",
        "explanation": "<p><strong>Yoʻq.</strong> 9, 15, 21, 25, 27 — hammasi toq va "
                       "murakkab. Teskarisi esa deyarli toʻgʻri: 2 dan boshqa hamma tub "
                       "sonlar toq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>8 va 9 sonlari haqida nima "
                "deyish mumkin?</strong></p>",
        "choices": ["Ikkalasi ham murakkab, lekin umumiy boʻluvchisi 1 dan boshqa yoʻq",
                    "Ikkalasi ham tub",
                    "8 tub, 9 murakkab",
                    "Ular teng sonlar"],
        "correct": "Ikkalasi ham murakkab, lekin umumiy boʻluvchisi 1 dan boshqa yoʻq",
        "explanation": "<p><strong>Ikkalasi murakkab, lekin oʻzaro tub.</strong> "
                       "8 = 2 × 2 × 2, 9 = 3 × 3 — umumiy tub koʻpaytuvchisi yoʻq. "
                       "“Oʻzaro tub” degani “ikkalasi ham tub” degani emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>72 ning ajratmasi "
                "qaysi?</strong></p>",
        "choices": ["2 × 2 × 2 × 3 × 3", "2 × 2 × 3 × 3", "8 × 9", "2 × 3 × 12"],
        "correct": "2 × 2 × 2 × 3 × 3",
        "explanation": "<p><strong>2 × 2 × 2 × 3 × 3 = 72.</strong> 2 × 2 × 3 × 3 = 36 "
                       "(bitta ikkilik yetishmayapti), qolgan ikkitasida esa murakkab "
                       "sonlar qolgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>100 ning ajratmasi "
                "qaysi?</strong></p>",
        "choices": ["2 × 2 × 5 × 5", "10 × 10", "2 × 50", "4 × 25"],
        "correct": "2 × 2 × 5 × 5",
        "explanation": "<p><strong>2 × 2 × 5 × 5 = 100.</strong> 10 × 10, 2 × 50 va "
                       "4 × 25 toʻgʻri koʻpaytmalar, lekin ularda tub boʻlmagan sonlar "
                       "bor — ajratma tugallanmagan.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Oʻquvchi: “60 ni ajratdim: <strong>60 = 4 × 15</strong>”, dedi.</p>"
                "<p><strong>Nima notoʻgʻri?</strong></p>",
        "choices": ["4 va 15 hali murakkab — ajratish davom etishi kerak",
                    "Koʻpaytma 60 ga teng emas",
                    "Ajratmada faqat juft sonlar boʻlishi kerak",
                    "Xato yoʻq"],
        "correct": "4 va 15 hali murakkab — ajratish davom etishi kerak",
        "explanation": "<p><strong>4 va 15 murakkab.</strong> 4 = 2 × 2, 15 = 3 × 5, "
                       "demak 60 = <strong>2 × 2 × 3 × 5</strong>. Koʻpaytma toʻgʻri, "
                       "lekin ajratma tugallanmagan.</p>",
    },
    {
        "text": "<p>Oʻquvchi: “Tub sonlar roʻyxati <strong>1, 2, 3, 5, 7…</strong>”, "
                "deb boshladi.</p><p><strong>Qayerda xato?</strong></p>",
        "choices": ["1 tub son emas, roʻyxat 2 dan boshlanadi",
                    "2 tub emas, chunki u juft",
                    "3 tushib qolgan",
                    "Xato yoʻq"],
        "correct": "1 tub son emas, roʻyxat 2 dan boshlanadi",
        "explanation": "<p><strong>1 tub emas.</strong> Toʻgʻri roʻyxat: 2, 3, 5, 7, 11, "
                       "13… 2 esa juft boʻlishiga qaramay tub — chunki uning boshqa "
                       "boʻluvchisi yoʻq.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Sinfga 13 ta stul keltirildi. Ularni teng qatorlarga tizmoqchimiz: "
                "har qatorda bittadan koʻp va bitta qatordan koʻp boʻlsin.</p>"
                "<p><strong>Bu mumkinmi?</strong></p>",
        "choices": ["Mumkin emas, chunki 13 — tub son",
                    "Mumkin: 2 qatorda 6 tadan va 1 ta ortadi",
                    "Mumkin: 3 qatorda 4 tadan",
                    "Mumkin: 13 qatorda 1 tadan"],
        "correct": "Mumkin emas, chunki 13 — tub son",
        "explanation": "<p><strong>Mumkin emas.</strong> 13 ning boʻluvchilari faqat "
                       "1 va 13, demak yo bitta qatorda 13 ta, yo 13 qatorda bittadan — "
                       "ikkalasi ham shartga toʻgʻri kelmaydi. “1 ta ortadi” degan "
                       "variant esa teng boʻlish emas.</p>",
    },
    {
        "text": "<p>Bogʻbonda 60 ta koʻchat bor va u ularni teng qatorlarga ekmoqchi "
                "(har qatorda bir xil sondan, hech narsa ortmasin).</p><p><strong>Necha "
                "xil variant bor?</strong></p>",
        "choices": ["12 xil", "6 xil", "4 xil", "10 xil"],
        "correct": "12 xil",
        "explanation": "<p><strong>12 xil.</strong> Har bir variant — 60 ning "
                       "boʻluvchisi: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60. Ularni "
                       "juftlab topish qulay: 1×60, 2×30, 3×20, 4×15, 5×12, 6×10 — "
                       "oltita juft, jami 12 ta boʻluvchi.</p>",
    },
]


# =====================================================================
# PM-8 — EKUB va EKUK
# =====================================================================

Q_PM8 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUB(8, 12) = ?</strong></p>",
        "choices": ["2", "4", "8", "24"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 8 = 2 × 2 × 2, 12 = 2 × 2 × 3. "
                       "Umumiylari: 2 va 2 → 2 × 2 = 4. Tekshirish: 8 ÷ 4 = 2 ✓, "
                       "12 ÷ 4 = 3 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUK(3, 4) = ?</strong></p>",
        "choices": ["1", "7", "12", "24"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 3 ning karralilari: 3, 6, 9, 12… "
                       "4 niki: 4, 8, 12… Birinchi uchrashuv — 12. Ular oʻzaro tub, "
                       "shuning uchun EKUK = 3 × 4.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUB nima degani?</strong></p>",
        "choices": ["Eng katta umumiy boʻluvchi", "Eng kichik umumiy boʻluvchi",
                    "Eng katta umumiy karrali", "Eng kichik umumiy karrali"],
        "correct": "Eng katta umumiy boʻluvchi",
        "explanation": "<p><strong>Eng katta umumiy boʻluvchi.</strong> U ikkala sonni "
                       "ham qoldiqsiz boʻladi, demak sonlardan kichik yoki ularga "
                       "teng.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUB(5, 15) = ?</strong></p>",
        "choices": ["1", "3", "5", "15"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 15 allaqachon 5 ga boʻlinadi, demak eng "
                       "katta umumiy boʻluvchi — kichik sonning oʻzi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUK(5, 15) = ?</strong></p>",
        "choices": ["5", "15", "20", "75"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> 15 ikkala sonning ham karralisi. Kichik "
                       "son katta sonning boʻluvchisi boʻlsa, EKUK — katta sonning "
                       "oʻzi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUB(18, 24) = ?</strong></p>",
        "choices": ["3", "6", "12", "72"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 18 = 2 × 3 × 3, 24 = 2 × 2 × 2 × 3. "
                       "Umumiylari 2 va 3 → 6. <strong>72</strong> — bu EKUK, "
                       "EKUB emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUK(4, 6) = ?</strong></p>",
        "choices": ["2", "12", "24", "10"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 4 = 2 × 2, 6 = 2 × 3 → EKUK = "
                       "2 × 2 × 3 = 12. <strong>24</strong> — bu koʻpaytma, lekin "
                       "eng kichik umumiy karrali emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUB(24, 36) = ?</strong></p>",
        "choices": ["6", "12", "18", "72"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 24 = 2 × 2 × 2 × 3, 36 = 2 × 2 × 3 × 3. "
                       "Umumiylari: 2, 2 va 3 → 2 × 2 × 3 = 12.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUK(24, 36) = ?</strong></p>",
        "choices": ["36", "72", "144", "864"],
        "correct": "72",
        "explanation": "<p><strong>72.</strong> Umumiy qism 2 × 2 × 3 ga har bir "
                       "sonning ortiqchasi qoʻshiladi: × 2 va × 3 → 72. Tekshirish: "
                       "EKUB × EKUK = 12 × 72 = 864 = 24 × 36 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUB(7, 13) = ?</strong></p>",
        "choices": ["1", "7", "13", "91"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> Ikkalasi ham tub va har xil, demak umumiy "
                       "boʻluvchisi faqat 1 — ular oʻzaro tub. EKUK i esa "
                       "7 × 13 = 91.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUK(9, 12) = ?</strong></p>",
        "choices": ["3", "36", "72", "108"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> 9 = 3 × 3, 12 = 2 × 2 × 3 → "
                       "EKUK = 2 × 2 × 3 × 3 = 36. Tekshirish: 36 ÷ 9 = 4 ✓, "
                       "36 ÷ 12 = 3 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>EKUB(16, 24) = ?</strong></p>",
        "choices": ["4", "8", "16", "48"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> 16 = 2 × 2 × 2 × 2, 24 = 2 × 2 × 2 × 3. "
                       "Uchta umumiy ikkilik: 2 × 2 × 2 = 8.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki son uchun EKUB va EKUK "
                "dan qaysi biri kattaroq boʻladi?</strong></p>",
        "choices": ["EKUK", "EKUB", "Ular doim teng", "Sonlarga bogʻliq emas"],
        "correct": "EKUK",
        "explanation": "<p><strong>EKUK.</strong> EKUB — boʻluvchi, shuning uchun "
                       "sonlardan kichik yoki teng. EKUK — karrali, shuning uchun "
                       "sonlardan katta yoki teng. Javobingiz shu chegaradan chiqsa, "
                       "xato bor.</p>",
    },
    {
        "text": "<p>Masala: “24 ta olma va 36 ta nokni bir xil paketlarga solamiz. Eng "
                "koʻpi bilan nechta paket chiqadi?”</p><p><strong>Nima topish "
                "kerak?</strong></p>",
        "choices": ["EKUB(24, 36)", "EKUK(24, 36)", "24 × 36", "24 + 36"],
        "correct": "EKUB(24, 36)",
        "explanation": "<p><strong>EKUB.</strong> Bor narsani <em>boʻlib</em> "
                       "tashlayapmiz, paketlar soni esa ikkala sonni ham boʻlishi "
                       "kerak. Javob 12 ta paket.</p>",
    },
    {
        "text": "<p>Masala: “Bir avtobus har 12 daqiqada, ikkinchisi har 18 daqiqada "
                "keladi. Qachon yana birga keladi?”</p><p><strong>Nima topish "
                "kerak?</strong></p>",
        "choices": ["EKUK(12, 18)", "EKUB(12, 18)", "12 + 18", "18 − 12"],
        "correct": "EKUK(12, 18)",
        "explanation": "<p><strong>EKUK.</strong> Takrorlanadigan hodisalar “qachon "
                       "uchrashadi” degan savol har doim EKUK ni talab qiladi: "
                       "EKUK(12, 18) = 36 daqiqa.</p>",
    },
    {
        "text": "<p>Maʼlum: EKUB(6, 8) = 2.</p><p><strong>Unda EKUK(6, 8) "
                "qancha?</strong></p>",
        "choices": ["12", "24", "48", "16"],
        "correct": "24",
        "explanation": "<p><strong>24.</strong> EKUB × EKUK = a × b qoidasidan: "
                       "2 × EKUK = 6 × 8 = 48, demak EKUK = 48 ÷ 2 = 24. Bu tekshiruv "
                       "har doim ishlaydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Oʻquvchi <strong>EKUB(24, 36) = 72</strong> deb yozdi.</p>"
                "<p><strong>Qayerda xato?</strong></p>",
        "choices": ["72 — bu EKUK; boʻluvchi sonlardan katta boʻlolmaydi",
                    "Ajratmalar notoʻgʻri topilgan",
                    "24 va 36 ning umumiy boʻluvchisi yoʻq",
                    "Xato yoʻq"],
        "correct": "72 — bu EKUK; boʻluvchi sonlardan katta boʻlolmaydi",
        "explanation": "<p><strong>72 — bu EKUK.</strong> EKUB 24 dan ham, 36 dan ham "
                       "kichik yoki ularga teng boʻlishi shart. Toʻgʻri javob — "
                       "<strong>12</strong>.</p>",
    },
    {
        "text": "<p>Oʻquvchi <strong>EKUK(4, 6) = 24</strong> deb topdi: “ularni "
                "koʻpaytirdim”.</p><p><strong>Nima notoʻgʻri?</strong></p>",
        "choices": ["Koʻpaytma faqat oʻzaro tub sonlarda EKUK boʻladi",
                    "EKUK har doim koʻpaytmaga teng",
                    "4 va 6 ning umumiy karralisi yoʻq",
                    "Javob toʻgʻri"],
        "correct": "Koʻpaytma faqat oʻzaro tub sonlarda EKUK boʻladi",
        "explanation": "<p><strong>Faqat oʻzaro tub sonlarda.</strong> 4 va 6 da umumiy "
                       "koʻpaytuvchi (2) bor, shuning uchun uni ikki marta hisoblamaymiz: "
                       "EKUK = 2 × 2 × 3 = <strong>12</strong>. 24 ham umumiy karrali, "
                       "lekin eng kichigi emas.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Dilnozada 24 ta olma va 36 ta nok bor. Har paketda olma ham, nok ham "
                "teng miqdorda boʻlsin va hech narsa ortmasin.</p><p><strong>Eng koʻpi "
                "bilan nechta paket chiqadi va har birida nechtadan meva "
                "boʻladi?</strong></p>",
        "choices": ["12 paket: 2 olma va 3 nok", "6 paket: 4 olma va 6 nok",
                    "12 paket: 3 olma va 2 nok", "72 paket: 1 olma va 1 nok"],
        "correct": "12 paket: 2 olma va 3 nok",
        "explanation": "<p><strong>12 paket: 2 olma va 3 nok.</strong> "
                       "EKUB(24, 36) = 12; 24 ÷ 12 = 2 olma, 36 ÷ 12 = 3 nok. "
                       "6 paket ham chiqadi, lekin savol <em>eng koʻpi bilan</em> deb "
                       "soʻragan.</p>",
    },
    {
        "text": "<p>Bekatga birinchi avtobus har 12 daqiqada, ikkinchisi har 18 daqiqada "
                "keladi. Ular soat 8:00 da birga keldi.</p><p><strong>Keyingi safar "
                "qachon birga keladi?</strong></p>",
        "choices": ["8:30 da", "8:36 da", "9:00 da", "8:24 da"],
        "correct": "8:36 da",
        "explanation": "<p><strong>8:36 da.</strong> EKUK(12, 18): 12 = 2 × 2 × 3, "
                       "18 = 2 × 3 × 3 → 2 × 2 × 3 × 3 = 36 daqiqa. Tekshirish: "
                       "36 ÷ 12 = 3 ✓, 36 ÷ 18 = 2 ✓</p>",
    },
]


# =====================================================================
# PM-9 — manfiy sonlar va son oʻqi
# =====================================================================

Q_PM9 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son katta: −3 yoki "
                "−9?</strong></p>",
        "choices": ["−3", "−9", "Ular teng", "Taqqoslab boʻlmaydi"],
        "correct": "−3",
        "explanation": "<p><strong>−3.</strong> U nolga yaqinroq, demak son oʻqida "
                       "oʻngroqda turibdi. Harorat tilida: −3° −9° dan issiqroq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>0 va −5 sonlaridan qaysi biri "
                "katta?</strong></p>",
        "choices": ["0", "−5", "Ular teng", "Nol bilan taqqoslash mumkin emas"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Nol har qanday manfiy sondan katta: son "
                       "oʻqida u hamma manfiylardan oʻngda turadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>−6 ning qarama-qarshi soni "
                "qaysi?</strong></p>",
        "choices": ["6", "−6", "0", "1"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Ikkalasi ham noldan olti qadam uzoqda, "
                       "lekin turli tomonlarda.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi harorat "
                "sovuqroq?</strong></p>",
        "choices": ["−4°", "−9°", "0°", "+2°"],
        "correct": "−9°",
        "explanation": "<p><strong>−9°.</strong> Son oʻqida u eng chapda turadi. "
                       "Manfiy sonlarda «katta raqam» sovuqroq haroratni bildiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nol qanday son?</strong></p>",
        "choices": ["Na musbat, na manfiy", "Musbat", "Manfiy", "Ham musbat, ham manfiy"],
        "correct": "Na musbat, na manfiy",
        "explanation": "<p><strong>Na musbat, na manfiy.</strong> Nol — chegara, sanoq "
                       "boshlanadigan nuqta. Uning qarama-qarshisi ham oʻzi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Sonlarni oʻsish tartibida joylashtiring.</p><p><strong>−5, 2, −1, "
                "0</strong></p>",
        "choices": ["−5, −1, 0, 2", "−1, −5, 0, 2", "0, −1, 2, −5", "2, 0, −1, −5"],
        "correct": "−5, −1, 0, 2",
        "explanation": "<p><strong>−5, −1, 0, 2.</strong> Son oʻqida chapdan oʻngga "
                       "qarab yozamiz. Manfiylar orasida −5 chaproqda, demak "
                       "kichikroq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Son oʻqida 3 dan chapga besh "
                "qadam yursak, qaysi songa yetamiz?</strong></p>",
        "choices": ["−2", "−1", "2", "−3"],
        "correct": "−2",
        "explanation": "<p><strong>−2.</strong> Sanaymiz: 2, 1, 0, −1, −2. Nolni "
                       "sanashni unutmaslik kerak — koʻpchilik shu yerda bittaga "
                       "adashadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Son oʻqida −11 va +4 "
                "orasida necha qadam bor?</strong></p>",
        "choices": ["7", "14", "15", "11"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> −11 dan 0 gacha 11 qadam, 0 dan 4 gacha "
                       "yana 4 qadam: 11 + 4 = 15. <strong>7</strong> — raqamlarni "
                       "ayirib yuborganda chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son kichik: −100 yoki "
                "−1?</strong></p>",
        "choices": ["−100", "−1", "Ular teng", "−1, chunki unda raqam kichik"],
        "correct": "−100",
        "explanation": "<p><strong>−100.</strong> U noldan juda uzoqda, chap tomonda. "
                       "Manfiy sonlarda “raqami katta” degani “soni kichik” degani.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Bankdagi hisobda 50 000 soʻm "
                "qarz bor. Buni qanday yozamiz?</strong></p>",
        "choices": ["−50 000", "50 000", "0", "+50 000"],
        "correct": "−50 000",
        "explanation": "<p><strong>−50 000.</strong> Qarz — noldan pastdagi holat. "
                       "Hisobga 50 000 soʻm qoʻyilsa, u nolga qaytadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Lift −2-qavatda turibdi va "
                "toʻrt qavat yuqoriga koʻtarildi. U qaysi qavatda?</strong></p>",
        "choices": ["2-qavatda", "4-qavatda", "−6-qavatda", "6-qavatda"],
        "correct": "2-qavatda",
        "explanation": "<p><strong>2-qavatda.</strong> Son oʻqida −2 dan oʻngga toʻrt "
                       "qadam: −1, 0, 1, 2. Yertoʻladan chiqib, kirish qavatidan ham "
                       "oʻtdi.</p>",
    },
    {
        "text": "<p>Sonlarni kamayish tartibida joylashtiring.</p><p><strong>0, −7, 3, "
                "−2</strong></p>",
        "choices": ["3, 0, −2, −7", "−7, −2, 0, 3", "3, 0, −7, −2", "0, 3, −2, −7"],
        "correct": "3, 0, −2, −7",
        "explanation": "<p><strong>3, 0, −2, −7.</strong> Kamayish tartibi — son "
                       "oʻqining oʻng chekkasidan chapga qarab yurish.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi tenglik "
                "toʻgʻri?</strong></p>",
        "choices": ["−8 < −3", "−8 > −3", "−8 = 8", "0 < −1"],
        "correct": "−8 < −3",
        "explanation": "<p><strong>−8 &lt; −3.</strong> Son oʻqida −8 chaproqda. "
                       "<strong>−8 &gt; −3</strong> — sezgi aldaydigan eng koʻp "
                       "uchraydigan xato; <strong>0 &lt; −1</strong> ham notoʻgʻri, "
                       "chunki nol hamma manfiylardan katta.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>−7 va 7 sonlari haqida nima "
                "deyish mumkin?</strong></p>",
        "choices": ["Ikkalasi ham noldan yetti qadam uzoqda",
                    "Ikkalasi ham noldan kichik",
                    "Ular teng sonlar",
                    "−7 nolga yaqinroq"],
        "correct": "Ikkalasi ham noldan yetti qadam uzoqda",
        "explanation": "<p><strong>Ikkalasi noldan yetti qadam uzoqda</strong>, lekin "
                       "turli tomonlarda — ular qarama-qarshi sonlar. Kattaligi "
                       "boʻyicha esa 7 &gt; −7.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Eng katta manfiy butun son "
                "qaysi?</strong></p>",
        "choices": ["−1", "0", "−100", "Bunday son yoʻq"],
        "correct": "−1",
        "explanation": "<p><strong>−1.</strong> U manfiylar orasida nolga eng yaqini. "
                       "Nolning oʻzi manfiy emas, shuning uchun javob boʻlolmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>“Har qanday musbat son har "
                "qanday manfiy sondan katta” — bu fikr toʻgʻrimi?</strong></p>",
        "choices": ["Ha, doim toʻgʻri", "Yoʻq, masalan 1 < −100",
                    "Faqat butun sonlar uchun toʻgʻri", "Faqat haroratda toʻgʻri"],
        "correct": "Ha, doim toʻgʻri",
        "explanation": "<p><strong>Ha.</strong> Musbatlar noldan oʻngda, manfiylar "
                       "chapda. Shuning uchun eng kichik musbat ham eng katta "
                       "manfiydan katta: 1 &gt; −100.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Jasur: “Ertalab −7°, tushda −2° edi, demak <strong>sovuq "
                "kuchaydi</strong>”, dedi.</p><p><strong>Nima notoʻgʻri?</strong></p>",
        "choices": ["−2 son oʻqida −7 dan oʻngda — demak havo isidi",
                    "Haroratni taqqoslab boʻlmaydi",
                    "−7 va −2 teng haroratlar",
                    "Fikr toʻgʻri"],
        "correct": "−2 son oʻqida −7 dan oʻngda — demak havo isidi",
        "explanation": "<p><strong>Havo isidi.</strong> −7 &lt; −2. Minus belgisi "
                       "“noldan qancha uzoq” degani emas, “qaysi tomonda” degani. "
                       "Harorat besh daraja koʻtarilgan.</p>",
    },
    {
        "text": "<p>Oʻquvchi <strong>0 &lt; −3</strong> deb yozdi: “nol — hech "
                "narsa”.</p><p><strong>Qayerda xato?</strong></p>",
        "choices": ["Nol har qanday manfiy sondan katta",
                    "Nol manfiy son hisoblanadi",
                    "Nolni taqqoslashda ishlatib boʻlmaydi",
                    "Xato yoʻq"],
        "correct": "Nol har qanday manfiy sondan katta",
        "explanation": "<p><strong>0 &gt; −3.</strong> Nol — chegara: undan oʻngdagilar "
                       "musbat, chapdagilar manfiy. Hisobda 0 soʻm boʻlish −3 000 soʻm "
                       "qarzdan yaxshiroq.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Dilnoza ertalabki haroratni yozib bordi: dushanba −3°, seshanba −8°, "
                "chorshanba 0°, payshanba +2°, juma −5°.</p><p><strong>Eng sovuq kun "
                "qaysi?</strong></p>",
        "choices": ["Seshanba", "Juma", "Dushanba", "Chorshanba"],
        "correct": "Seshanba",
        "explanation": "<p><strong>Seshanba (−8°).</strong> Son oʻqida barcha "
                       "haroratlarni joylashtiramiz: −8 &lt; −5 &lt; −3 &lt; 0 &lt; +2. "
                       "Eng chapdagisi — eng sovugʻi.</p>",
    },
    {
        "text": "<p>Uch shaharda harorat: Toshkentda −2°, Nukusda −11°, Termizda "
                "+4°.</p><p><strong>Termiz Nukusdan necha daraja issiq?</strong></p>",
        "choices": ["15 daraja", "7 daraja", "11 daraja", "13 daraja"],
        "correct": "15 daraja",
        "explanation": "<p><strong>15 daraja.</strong> Son oʻqida sanaymiz: −11 dan "
                       "0 gacha 11 qadam, 0 dan +4 gacha yana 4 qadam — jami 15. "
                       "<strong>7</strong> — 11 dan 4 ni ayirib yuborganda chiqadigan "
                       "javob.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-7 Mashq: Tub va murakkab sonlar",
        "description": "20 savol — tub va murakkab sonlar, 1 ning oʻrni, Eratosfen "
                       "gʻalviri va tub koʻpaytuvchilarga ajratish.",
        "tutorial":    "PM-7:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM7,
    },
    {
        "title":       "PM-8 Mashq: EKUB va EKUK",
        "description": "20 savol — EKUB va EKUK ni topish, ularni ajrata bilish va "
                       "hayotdagi masalalarda qoʻllash.",
        "tutorial":    "PM-8:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM8,
    },
    {
        "title":       "PM-9 Mashq: Manfiy sonlar va son oʻqi",
        "description": "20 savol — manfiy sonning maʼnosi, son oʻqi, qarama-qarshi "
                       "sonlar, taqqoslash va tartiblash.",
        "tutorial":    "PM-9:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM9,
    },
]
