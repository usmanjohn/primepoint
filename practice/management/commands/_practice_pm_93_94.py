# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-93, PM-94 (yosh va sonlar masalalari;
oʻlchov birliklari va ortiqcha maʼlumot). Blok G ni yopadi.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: ikkalasi ham `hard`.

⚠️ `choices` EKRANLANADI — HTML teg yoʻq.
⚠️ Kumulyativ:
   • PM-93 — yoshlar farqining oʻzgarmasligi, «hozir/keyin/oldin»
     jadvali, ketma-ket sonlar, ikki xonali son 10a + b.
     ⛔ Kvadrat tenglamali yosh masalalari YOʻQ;
   • PM-94 — uzunlik, massa, sigʻim, vaqt va YUZA birliklari;
     ortiqcha va yetishmayotgan maʼlumot. ⛔ Hajm birliklari mashq
     qilinmaydi.
⚠️ Distraktorlar — haqiqiy xatolar: farqni oʻzgaruvchi deb hisoblash,
   «oldin» da faqat bittasidan ayirish, ketma-ket sonlarni x/x+2/x+4
   deb yozish, ikki xonali sonni a + b deb olish, 1 m² = 100 sm²,
   kichik birlikka oʻtganda boʻlish, ortiqcha sonni hisobga qoʻshish.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_93_94.py --master=prime \\
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
# PM-93 — yosh masalalari va sonlar haqidagi masalalar
# =====================================================================

Q_PM93 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>Aka 15, uka 9 yoshda.</p>"
                "<p><strong>10 yildan keyin ularning yoshlari farqi "
                "qancha boʻladi?</strong></p>",
        "choices": ["6 yosh", "10 yosh", "16 yosh", "26 yosh"],
        "correct": "6 yosh",
        "explanation": "<p><strong>6 yosh.</strong> Yoshlar farqi hech "
                       "qachon oʻzgarmaydi: 15 − 9 = 6. Oʻn yildan "
                       "keyin 25 va 19 — farqi hamon 6. "
                       "<strong>16</strong> — farqqa 10 ni qoʻshganda "
                       "chiqadi, lekin 10 yil ikkalasiga ham "
                       "qoʻshiladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Ota 40, oʻgʻli 12 yoshda. "
                "Ularning yoshlari farqi qancha?</strong></p>",
        "choices": ["12 yosh", "28 yosh", "40 yosh", "52 yosh"],
        "correct": "28 yosh",
        "explanation": "<p><strong>28 yosh.</strong> 40 − 12 = 28. Bu son "
                       "umr boʻyi oʻzgarmaydi — yosh masalalarida "
                       "eng ishonchli tayanch shu.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>Ketma-ket uchta "
                "sondan birinchisi x.</p><p><strong>Qolgan ikkitasi ___ "
                "koʻrinishda yoziladi.</strong></p>",
        "choices": ["x + 1 va x + 2", "x + 2 va x + 4",
                    "2x va 3x", "x − 1 va x − 2"],
        "correct": "x + 1 va x + 2",
        "explanation": "<p><strong>x + 1 va x + 2.</strong> Ketma-ket "
                       "sonlar bittadan farq qiladi. "
                       "<strong>x + 2 va x + 4</strong> — bu ketma-ket "
                       "<strong>juft</strong> yoki <strong>toq</strong> "
                       "sonlar.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>Ikki xonali sonning "
                "oʻnliklar raqami a, birliklar raqami b.</p>"
                "<p><strong>Bu son ___ koʻrinishida yoziladi.</strong></p>",
        "choices": ["a + b", "ab", "10a + b", "a + 10b"],
        "correct": "10a + b",
        "explanation": "<p><strong>10a + b.</strong> Oʻnliklar raqamining "
                       "qiymati 10 barobar (PM-1): 57 = 10 × 5 + 7. "
                       "<strong>a + b</strong> — raqamlar yigʻindisi, "
                       "sonning oʻzi emas: 5 + 7 = 12 ≠ 57.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Masalada «5 yil oldin» "
                "deyilgan.</p><p><strong>Jadvalda nima "
                "qilinadi?</strong></p>",
        "choices": [
            "Faqat kattaning yoshidan 5 ayiriladi",
            "Ikkalasining yoshidan ham 5 ayiriladi",
            "Ikkalasining yoshiga ham 5 qoʻshiladi",
            "Farqdan 5 ayiriladi",
        ],
        "correct": "Ikkalasining yoshidan ham 5 ayiriladi",
        "explanation": "<p><strong>Ikkalasining yoshidan ham 5 "
                       "ayiriladi.</strong> Vaqt hamma uchun bir xil "
                       "oʻtadi. Faqat bittasidan ayirish — juda koʻp "
                       "uchraydigan xato; u farqni ham buzib "
                       "yuboradi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Ota 36, oʻgʻli 6 yoshda.</p>"
                "<p><strong>Necha yildan keyin ota oʻgʻlidan 3 marta "
                "katta boʻladi?</strong></p>",
        "choices": ["6 yildan keyin", "9 yildan keyin", "12 yildan keyin",
                    "15 yildan keyin"],
        "correct": "9 yildan keyin",
        "explanation": "<p><strong>9 yildan keyin.</strong> "
                       "36 + x = 3(6 + x) → 36 + x = 18 + 3x → 18 = 2x "
                       "→ x = 9. Tekshirish: 45 va 15, 45 ÷ 15 = 3 ✓ "
                       "Farqi hamon 30.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ona 30, qizi 5 yoshda.</p>"
                "<p><strong>Necha yildan keyin ona qizidan 2 marta katta "
                "boʻladi?</strong></p>",
        "choices": ["15 yildan keyin", "20 yildan keyin",
                    "25 yildan keyin", "30 yildan keyin"],
        "correct": "20 yildan keyin",
        "explanation": "<p><strong>20 yildan keyin.</strong> "
                       "30 + x = 2(5 + x) → 30 + x = 10 + 2x → x = 20. "
                       "Tekshirish: 50 va 25, 50 ÷ 25 = 2 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Hozir ota oʻgʻlidan 4 marta "
                "katta. 5 yildan keyin 3 marta katta boʻladi.</p>"
                "<p><strong>Oʻgʻil hozir necha yoshda?</strong></p>",
        "choices": ["8 yoshda", "10 yoshda", "12 yoshda", "15 yoshda"],
        "correct": "10 yoshda",
        "explanation": "<p><strong>10 yoshda.</strong> x — oʻgʻil, ota 4x. "
                       "4x + 5 = 3(x + 5) → 4x + 5 = 3x + 15 → x = 10, "
                       "ota 40. Tekshirish: 5 yildan keyin 45 va 15, "
                       "45 ÷ 15 = 3 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ketma-ket uchta sonning "
                "yigʻindisi 96.</p><p><strong>Oʻrtadagi son "
                "qanday?</strong></p>",
        "choices": ["31", "32", "33", "48"],
        "correct": "32",
        "explanation": "<p><strong>32.</strong> x + (x+1) + (x+2) = 96 → "
                       "3x + 3 = 96 → x = 31, sonlar 31, 32, 33. "
                       "Oʻrtadagisi 32 — u har doim yigʻindining uchdan "
                       "biriga, yaʼni oʻrtacha arifmetikka teng "
                       "(PM-78).</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ketma-ket ikkita toq sonning "
                "yigʻindisi 36.</p><p><strong>Bu sonlar "
                "qanday?</strong></p>",
        "choices": ["15 va 21", "16 va 20", "17 va 19", "18 va 18"],
        "correct": "17 va 19",
        "explanation": "<p><strong>17 va 19.</strong> Ketma-ket toq sonlar "
                       "ikkitadan farq qiladi: x + (x + 2) = 36 → "
                       "2x = 34 → x = 17. Tekshirish: 17 + 19 = 36 ✓ "
                       "«16 va 20» — juft sonlar, «18 va 18» esa "
                       "ketma-ket emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki xonali sonning oʻnliklar "
                "raqami 7, birliklar raqami 2.</p><p><strong>Raqamlar "
                "almashtirilsa, son qanchaga kamayadi?</strong></p>",
        "choices": ["27 ga", "45 ga", "50 ga", "54 ga"],
        "correct": "45 ga",
        "explanation": "<p><strong>45 ga.</strong> Son 72, almashgach 27. "
                       "72 − 27 = 45. Raqamlar almashganda farq har "
                       "doim 9 ning karralisi boʻladi — bu yerda "
                       "9 × (7 − 2) = 45.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki xonali sonning raqamlari "
                "yigʻindisi 11. Raqamlar almashtirilsa, son 27 ga "
                "ortadi.</p><p><strong>Bu son qanday?</strong></p>",
        "choices": ["29", "38", "47", "56"],
        "correct": "47",
        "explanation": "<p><strong>47.</strong> a + b = 11; "
                       "10b + a = 10a + b + 27 → 9b − 9a = 27 → "
                       "b − a = 3. Yigʻindisi 11, farqi 3 → a = 4, "
                       "b = 7 (PM-87 usuli). Tekshirish: 4 + 7 = 11 ✓, "
                       "74 − 47 = 27 ✓</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ota oʻgʻlidan 25 yosh "
                "katta.</p><p><strong>10 yildan keyin necha yosh katta "
                "boʻladi?</strong></p>",
        "choices": ["15 yosh", "25 yosh", "35 yosh", "Aniqlab boʻlmaydi"],
        "correct": "25 yosh",
        "explanation": "<p><strong>25 yosh.</strong> Farq oʻzgarmas. "
                       "Oʻzgaradigan narsa — «necha marta katta» degan "
                       "nisbat. <strong>35</strong> — farqqa 10 "
                       "qoʻshilganda chiqadigan eng koʻp uchraydigan "
                       "xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ketma-ket "
                "uchta juft son qanday yoziladi?</strong></p>",
        "choices": [
            "x, x + 1, x + 2",
            "x, x + 2, x + 4",
            "x, 2x, 4x",
            "2x, 4x, 6x",
        ],
        "correct": "x, x + 2, x + 4",
        "explanation": "<p><strong>x, x + 2, x + 4.</strong> Juft sonlar "
                       "ikkitadan farq qiladi: 10, 12, 14. Toq sonlar "
                       "ham xuddi shunday yoziladi (7, 9, 11) — farq "
                       "faqat x ning oʻzida.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Yosh masalasining "
                "javobi x = −6 chiqdi.</p><p><strong>Bu nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Masala notoʻgʻri yechilgan",
            "Hodisa 6 yil oldin boʻlgan",
            "Hodisa 6 yildan keyin boʻladi",
            "Masalaning yechimi yoʻq",
        ],
        "correct": "Hodisa 6 yil oldin boʻlgan",
        "explanation": "<p><strong>Hodisa 6 yil oldin boʻlgan.</strong> "
                       "Manfiy javob xato emas — u vaqt oʻqining "
                       "teskari tomonini koʻrsatadi. Javobni oʻsha "
                       "paytga qoʻyib tekshirsa, shart bajarilgani "
                       "koʻrinadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>49 soni haqida "
                "qaysi yozuv toʻgʻri?</strong></p>",
        "choices": [
            "49 = 4 + 9",
            "49 = 4 × 9",
            "49 = 10 × 4 + 9",
            "49 = 10 × 9 + 4",
        ],
        "correct": "49 = 10 × 4 + 9",
        "explanation": "<p><strong>49 = 10 × 4 + 9.</strong> Oʻnliklar "
                       "raqami 4, birliklar raqami 9. "
                       "<strong>10 × 9 + 4</strong> = 94 — bu raqamlar "
                       "almashgan son.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>«Ota 40, oʻgʻil 10 "
                "yoshda» masalasida oʻquvchi yozdi: «5 yil oldin ota "
                "40 − 5 = 35, oʻgʻil esa 10 yoshda edi».</p>"
                "<p><strong>Nima notoʻgʻri?</strong></p>",
        "choices": [
            "Otaning yoshi notoʻgʻri hisoblangan",
            "Oʻgʻilning yoshidan ham 5 ayirilishi kerak edi",
            "Ayirish oʻrniga qoʻshish kerak edi",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Oʻgʻilning yoshidan ham 5 ayirilishi kerak edi",
        "explanation": "<p><strong>Oʻgʻilning yoshidan ham 5 ayirilishi "
                       "kerak edi.</strong> Toʻgʻrisi: 35 va 5. Xatoni "
                       "farq bilan tekshirish oson — 35 − 10 = 25 "
                       "chiqdi, holbuki farq har doim 30 boʻlishi "
                       "kerak.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Ketma-ket uchta "
                "sonning yigʻindisi 60. Eng kichigini toping.</strong></p>",
        "choices": [
            "3x = 60 → x = 20",
            "3x + 3 = 60 → x = 19",
            "3x + 6 = 60 → x = 18",
            "x + 3 = 60 → x = 57",
        ],
        "correct": "3x + 3 = 60 → x = 19",
        "explanation": "<p><strong>3x + 3 = 60 → x = 19.</strong> "
                       "x + (x+1) + (x+2) = 3x + 3. Sonlar 19, 20, 21; "
                       "yigʻindisi 60 ✓ <strong>3x = 60</strong> — "
                       "qoʻshimcha 1 va 2 unutilgan; "
                       "<strong>3x + 6</strong> — sonlar x, x+2, x+4 "
                       "deb olingan.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Aka ukasidan 3 marta katta. "
                "Ikkalasining yoshlari yigʻindisi 32.</p><p><strong>Aka "
                "necha yoshda?</strong></p>",
        "choices": ["8 yoshda", "16 yoshda", "24 yoshda", "26 yoshda"],
        "correct": "24 yoshda",
        "explanation": "<p><strong>24 yoshda.</strong> x — uka, aka 3x. "
                       "x + 3x = 32 → 4x = 32 → x = 8, aka 3 × 8 = 24. "
                       "Tekshirish: 8 + 24 = 32 ✓ va 24 ÷ 8 = 3 ✓ "
                       "<strong>8</strong> — ukaning yoshi, savol esa "
                       "akani soʻragan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Hozir bobo nevarasidan 6 marta "
                "katta. 12 yildan keyin 3 marta katta boʻladi.</p>"
                "<p><strong>Bobo hozir necha yoshda?</strong></p>",
        "choices": ["8 yoshda", "36 yoshda", "48 yoshda", "60 yoshda"],
        "correct": "48 yoshda",
        "explanation": "<p><strong>48 yoshda.</strong> x — nevara, bobo 6x. "
                       "6x + 12 = 3(x + 12) → 6x + 12 = 3x + 36 → "
                       "3x = 24 → x = 8, bobo 48. Tekshirish: 12 yildan "
                       "keyin 60 va 20, 60 ÷ 20 = 3 ✓ Farqi ikkala "
                       "paytda ham 40.</p>",
    },
]


# =====================================================================
# PM-94 — oʻlchov birliklari; ortiqcha maʼlumot
# =====================================================================

Q_PM94 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>5 m 30 sm — "
                "bu ___ sm.</strong></p>",
        "choices": ["35", "80", "530", "5030"],
        "correct": "530",
        "explanation": "<p><strong>530.</strong> 5 × 100 + 30 = 530 sm. "
                       "<strong>35</strong> — sonlar shunchaki "
                       "qoʻshilganda chiqadi, lekin metr va santimetr "
                       "har xil birlik.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>4,2 kg — bu "
                "___ g.</strong></p>",
        "choices": ["42", "420", "4200", "42 000"],
        "correct": "4200",
        "explanation": "<p><strong>4200.</strong> 1 kg = 1000 g, demak "
                       "4,2 × 1000 = 4200. Kichik birlikka oʻtilyapti — "
                       "son kattalashishi kerak ✓</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>1 m² — bu ___ "
                "sm².</strong></p>",
        "choices": ["100", "1000", "10 000", "1 000 000"],
        "correct": "10 000",
        "explanation": "<p><strong>10 000.</strong> Yuza — ikkita "
                       "uzunlikning koʻpaytmasi, shuning uchun "
                       "koeffitsiyent kvadratga koʻtariladi: "
                       "100 × 100 = 10 000. <strong>100</strong> — bu "
                       "darsning eng koʻp uchraydigan xatosi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>3 litr — bu "
                "___ ml.</strong></p>",
        "choices": ["30", "300", "3000", "30 000"],
        "correct": "3000",
        "explanation": "<p><strong>3000.</strong> 1 l = 1000 ml, demak "
                       "3 × 1000 = 3000 ml.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>2 soat "
                "15 minut — bu ___ minut.</strong></p>",
        "choices": ["17", "35", "135", "215"],
        "correct": "135",
        "explanation": "<p><strong>135.</strong> 2 × 60 + 15 = 135. "
                       "<strong>215</strong> — sonlar yonma-yon "
                       "yozilganda chiqadi; soatda 100 emas, 60 minut "
                       "bor.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>6 m² necha kvadrat "
                "santimetr?</strong></p>",
        "choices": ["600 sm²", "6000 sm²", "60 000 sm²", "600 000 sm²"],
        "correct": "60 000 sm²",
        "explanation": "<p><strong>60 000 sm².</strong> "
                       "6 × 10 000 = 60 000. <strong>600</strong> — "
                       "1 m² = 100 sm² deb olinganda chiqadi va javob "
                       "yuz barobar kichik boʻlib qoladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>7500 g necha "
                "kilogramm?</strong></p>",
        "choices": ["0,75 kg", "7,5 kg", "75 kg", "750 kg"],
        "correct": "7,5 kg",
        "explanation": "<p><strong>7,5 kg.</strong> 7500 ÷ 1000 = 7,5. "
                       "Katta birlikka oʻtilyapti — son kichrayishi "
                       "kerak ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1 km 250 m necha "
                "metr?</strong></p>",
        "choices": ["251 m", "1250 m", "1025 m", "125 000 m"],
        "correct": "1250 m",
        "explanation": "<p><strong>1250 m.</strong> 1 × 1000 + 250 = 1250. "
                       "Bu 1,25 km ga ham teng — ikkala yozuv "
                       "toʻgʻri, faqat birligini adashtirmaslik "
                       "kerak.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1 sm² necha kvadrat "
                "millimetr?</strong></p>",
        "choices": ["10 mm²", "100 mm²", "1000 mm²", "10 000 mm²"],
        "correct": "100 mm²",
        "explanation": "<p><strong>100 mm².</strong> 1 sm = 10 mm, demak "
                       "1 sm² = 10 × 10 = 100 mm². Yana oʻsha kvadrat "
                       "qoidasi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>0,8 tonna necha "
                "kilogramm?</strong></p>",
        "choices": ["8 kg", "80 kg", "800 kg", "8000 kg"],
        "correct": "800 kg",
        "explanation": "<p><strong>800 kg.</strong> 1 t = 1000 kg, demak "
                       "0,8 × 1000 = 800 kg.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2,5 m² necha kvadrat "
                "santimetr?</strong></p>",
        "choices": ["250 sm²", "2500 sm²", "25 000 sm²", "250 000 sm²"],
        "correct": "25 000 sm²",
        "explanation": "<p><strong>25 000 sm².</strong> "
                       "2,5 × 10 000 = 25 000. <strong>250</strong> — "
                       "yuz barobar kichik javob, yaʼni kvadrat qoidasi "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>350 sm necha metr?</strong>"
                "</p>",
        "choices": ["0,35 m", "3,5 m", "35 m", "35 000 m"],
        "correct": "3,5 m",
        "explanation": "<p><strong>3,5 m.</strong> 350 ÷ 100 = 3,5. Bu "
                       "3 m 50 sm ga teng.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nima uchun "
                "1 m² = 10 000 sm², 100 sm² emas?</strong></p>",
        "choices": [
            "Chunki yuza ikkita uzunlikning koʻpaytmasi",
            "Chunki metr santimetrdan 10 000 marta katta",
            "Chunki yuzada har doim nol qoʻshiladi",
            "Chunki kvadratning toʻrtta tomoni bor",
        ],
        "correct": "Chunki yuza ikkita uzunlikning koʻpaytmasi",
        "explanation": "<p><strong>Yuza ikkita uzunlikning "
                       "koʻpaytmasi.</strong> Har ikkala tomon 100 "
                       "barobar kattaradi, demak yuza "
                       "100 × 100 = 10 000 barobar kattaradi. Shu sabab "
                       "hajmda kubga koʻtariladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Katta birlikdan "
                "kichik birlikka oʻtganda nima qilinadi?</strong></p>",
        "choices": [
            "Boʻlinadi",
            "Koʻpaytiriladi",
            "Qoʻshiladi",
            "Hech narsa oʻzgarmaydi",
        ],
        "correct": "Koʻpaytiriladi",
        "explanation": "<p><strong>Koʻpaytiriladi.</strong> Kichik birlikda "
                       "son kattaroq chiqadi: 2,5 kg = 2500 g. "
                       "Shubhalansangiz oʻzingizdan soʻrang — javob "
                       "kattaroq boʻlishi kerakmi yoki kichikroq?</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Sherbek 20 daqiqada "
                "6 ta masala yechdi. Sinfida 28 oʻquvchi bor. Bitta "
                "masalaga oʻrtacha necha daqiqa ketgan?»</p>"
                "<p><strong>Qaysi son ortiqcha?</strong></p>",
        "choices": ["20 daqiqa", "6 ta masala", "28 oʻquvchi",
                    "Ortiqcha son yoʻq"],
        "correct": "28 oʻquvchi",
        "explanation": "<p><strong>28 oʻquvchi.</strong> Javob "
                       "20 ÷ 6 ≈ 3,3 daqiqa. Sinfdagi oʻquvchilar soni "
                       "Sherbekning tezligiga hech qanday aloqasi "
                       "yoʻq — u ataylab qoʻyilgan ortiqcha "
                       "maʼlumot.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Masalada yechish uchun "
                "zarur boʻlgan bir son berilmagan.</p><p><strong>Nima "
                "qilish kerak?</strong></p>",
        "choices": [
            "Yetishmayotgan sonni taxmin qilib yechish",
            "Maʼlumot yetarli emasligini aytish",
            "Masalani nolga teng deb olish",
            "Berilgan sonlarni qoʻshib qoʻyish",
        ],
        "correct": "Maʼlumot yetarli emasligini aytish",
        "explanation": "<p><strong>Maʼlumot yetarli emasligini "
                       "aytish.</strong> Oʻylab topilgan son bilan "
                       "chiqarilgan javob — xato javob. "
                       "Yetishmayotgan maʼlumotni tanib olish va uni "
                       "aytishning oʻzi toʻgʻri javobdir.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>Oʻquvchi yozdi: "
                "«2,5 kg = 250 g».</p><p><strong>Nima notoʻgʻri?</strong>"
                "</p>",
        "choices": [
            "1000 ga emas, 100 ga koʻpaytirilgan",
            "Koʻpaytirish oʻrniga boʻlingan",
            "Vergul notoʻgʻri qoʻyilgan",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "1000 ga emas, 100 ga koʻpaytirilgan",
        "explanation": "<p><strong>1000 ga emas, 100 ga "
                       "koʻpaytirilgan.</strong> Toʻgʻrisi: "
                       "2,5 × 1000 = 2500 g. Xatoni tez ushlash yoʻli: "
                       "250 g — bir kilodan ham kam, holbuki bizda "
                       "2,5 kg bor edi.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>4 m² necha kvadrat "
                "santimetr?</strong></p>",
        "choices": [
            "4 × 100 = 400 sm²",
            "4 × 1000 = 4000 sm²",
            "4 × 10 000 = 40 000 sm²",
            "4 × 100 × 100 × 100 = 4 000 000 sm²",
        ],
        "correct": "4 × 10 000 = 40 000 sm²",
        "explanation": "<p><strong>4 × 10 000 = 40 000 sm².</strong> "
                       "1 m² = 100 × 100 = 10 000 sm². "
                       "<strong>4 × 100</strong> — uzunlik "
                       "koeffitsiyenti yuzaga qoʻllangan; oxirgi "
                       "variant esa hajm koeffitsiyentini "
                       "ishlatgan.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Xonaning uzunligi 6 m, eni "
                "5 m. Polga tomoni 50 sm boʻlgan kvadrat plitka "
                "yotqiziladi. Xonaning balandligi 3 m.</p><p><strong>Nechta "
                "plitka kerak?</strong></p>",
        "choices": ["60 ta", "120 ta", "300 ta", "600 ta"],
        "correct": "120 ta",
        "explanation": "<p><strong>120 ta.</strong> Pol yuzasi "
                       "6 × 5 = 30 m². Plitka 50 sm = 0,5 m, yuzasi "
                       "0,5 × 0,5 = 0,25 m². 30 ÷ 0,25 = 120. "
                       "Santimetrda tekshiramiz: 600 × 500 = "
                       "300 000 sm²; 50 × 50 = 2500 sm²; "
                       "300 000 ÷ 2500 = 120 ✓ «3 m balandlik» — "
                       "ortiqcha maʼlumot.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bekzod kilosi 12 000 soʻmdan "
                "3 kg olma oldi. Doʻkonda 15 xil meva bor edi. U "
                "50 000 soʻm berdi.</p><p><strong>Qancha qaytim "
                "oldi?</strong></p>",
        "choices": ["14 000 soʻm", "22 000 soʻm", "36 000 soʻm",
                    "38 000 soʻm"],
        "correct": "14 000 soʻm",
        "explanation": "<p><strong>14 000 soʻm.</strong> Olma "
                       "12 000 × 3 = 36 000 soʻm. Qaytim: "
                       "50 000 − 36 000 = 14 000. «15 xil meva» — "
                       "ortiqcha maʼlumot; u hisobga umuman "
                       "kirmaydi. <strong>36 000</strong> — toʻlangan "
                       "pul, savol esa qaytimni soʻragan.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-93 Mashq: Yosh masalalari va sonlar haqidagi masalalar",
        "tutorial":    "PM-93:",
        "description": (
            "Yoshlar farqining oʻzgarmasligi, «hozir/keyin/oldin» jadvali, "
            "ketma-ket sonlar va ikki xonali son 10a + b. 20 savol."
        ),
        "questions":   Q_PM93,
        **DEFAULTS,
    },
    {
        "title":       "PM-94 Mashq: Oʻlchov birliklari; ortiqcha maʼlumot",
        "tutorial":    "PM-94:",
        "description": (
            "Uzunlik, massa, sigʻim, vaqt va yuza birliklari; ortiqcha va "
            "yetishmayotgan maʼlumotni tanib olish. 20 savol."
        ),
        "questions":   Q_PM94,
        **DEFAULTS,
    },
]
