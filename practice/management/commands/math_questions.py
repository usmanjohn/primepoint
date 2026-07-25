# -*- coding: utf-8 -*-
"""Aralash matematika testlari (5-7 sinf) — EKUB/EKUK, boʻlinish alomatlari,
boʻluvchilar, tub va murakkab sonlar, ratsional (kasr) sonlar, harakat masalalari.

Masalalarda ishlatiladigan oʻquvchilar ismlari (keyingi testlarda ham shulardan foydalaning):
Afsona, Jasur, Sherbek, Davron, Samandar, Iroda, Shaxzoda, Marjona, Madina,
Charos, Firdavs, Ilgʻor, Javohir, Sirojiddin, Behruz, Elbek, Abdulloh.
"""

PUPILS = [
    "Afsona", "Jasur", "Sherbek", "Davron", "Samandar", "Iroda", "Shaxzoda",
    "Marjona", "Madina", "Charos", "Firdavs", "Ilgʻor", "Javohir",
    "Sirojiddin", "Behruz", "Elbek", "Abdulloh",
]


# =====================================================================
# 1-TEST — Oʻrta daraja: EKUB, EKUK, boʻlinish, kasrlar, harakat
# =====================================================================

test_math_1 = [
    {
        "text": "<p><strong>EKUB — mantiqiy masala.</strong> Afsonada 36 ta qizil va 60 ta koʻk munchoq bor. U shu munchoqlardan bir xil bilaguzuklar yasamoqchi, har bir bilaguzukda qizil munchoqlar soni ham, koʻk munchoqlar soni ham teng boʻlishi va bitta ham munchoq ortib qolmasligi kerak. <u>Eng koʻpi bilan</u> nechta bilaguzuk yasay oladi?</p>",
        "explanation": "<p><strong>12</strong> — toʻgʻri javob. Bilaguzuklar soni 36 ni ham, 60 ni ham qoldiqsiz boʻlishi kerak, ya'ni u umumiy boʻluvchi. Eng koʻp boʻlishi uchun EKUB ni olamiz: 36 = 2²·3², 60 = 2²·3·5 → EKUB(36, 60) = 2²·3 = <strong>12</strong>. Har bir bilaguzukka 36:12 = 3 ta qizil va 60:12 = 5 ta koʻk munchoq tushadi.</p>",
        "correct": "12",
        "choices": ["6", "12", "18", "24"],
    },
    {
        "text": "<p><strong>EKUK — mantiqiy masala.</strong> Charos kutubxonaga har 4 kunda, Afsona esa har 6 kunda keladi. Bugun ikkalasi ham kutubxonada uchrashdi. Ular keyingi safar eng kamida necha kundan soʻng yana birga uchrashadi?</p>",
        "explanation": "<p><strong>12 kun</strong> — toʻgʻri javob. Uchrashuv kuni 4 ga ham, 6 ga ham boʻlinishi kerak, demak bu umumiy karrali. Eng yaqin kun — EKUK: 4 = 2², 6 = 2·3 → EKUK(4, 6) = 2²·3 = <strong>12</strong>. (Charos 4, 8, 12-kunlari; Afsona 6, 12-kunlari keladi.)</p>",
        "correct": "12 kundan keyin",
        "choices": ["8 kundan keyin", "10 kundan keyin", "12 kundan keyin", "24 kundan keyin"],
    },
    {
        "text": "<p><strong>EKUK (uchta son).</strong> Jasur sport zaliga har 6 kunda, Sherbek har 8 kunda, Davron esa har 12 kunda boradi. Bugun uchalasi ham zalda uchrashdi. Ular keyingi safar necha kundan keyin uchalasi birga uchrashadi?</p>",
        "explanation": "<p><strong>24 kun</strong> — toʻgʻri javob. 6 = 2·3, 8 = 2³, 12 = 2²·3. Har bir tub koʻpaytuvchini eng katta darajada olamiz: EKUK = 2³·3 = <strong>24</strong>. 24 soni 6 ga ham (24:6=4), 8 ga ham (24:8=3), 12 ga ham (24:12=2) boʻlinadi.</p>",
        "correct": "24",
        "choices": ["12", "24", "36", "48"],
    },
    {
        "text": "<p><strong>Boʻlinish alomatlari.</strong> Toʻrt xonali <em>253X</em> soni 6 ga qoldiqsiz boʻlinadi. X raqami qabul qilishi mumkin boʻlgan barcha qiymatlarning yigʻindisini toping.</p>",
        "explanation": "<p><strong>10</strong> — toʻgʻri javob. 6 ga boʻlinish = 2 ga <u>va</u> 3 ga boʻlinish. 2 ga boʻlinishi uchun X juft: 0, 2, 4, 6, 8. 3 ga boʻlinishi uchun raqamlar yigʻindisi 2+5+3+X = 10+X uchga boʻlinsin → X = 2, 5, 8. Ikkala shartni ham qanoatlantiruvchilar: X = 2 va X = 8. Yigʻindisi: 2 + 8 = <strong>10</strong>.</p>",
        "correct": "10",
        "choices": ["8", "10", "12", "14"],
    },
    {
        "text": "<p><strong>Boʻlinish alomatlari.</strong> Quyidagi sonlarning barchasi 9 ga boʻlinadi. Ulardan qaysi biri <u>ham 9 ga, ham 4 ga</u> boʻlinadi?</p>",
        "explanation": "<p><strong>396</strong> — toʻgʻri javob. Son 4 ga boʻlinishi uchun oxirgi ikki raqamdan tuzilgan son 4 ga boʻlinishi kerak: 34:4 — qoldiqli, <strong>96:4 = 24</strong> ✓, 22:4 — qoldiqli, 38:4 — qoldiqli. Demak faqat 396 mos keladi (396 = 36·11, 396:4 = 99, 396:9 = 44).</p>",
        "correct": "396",
        "choices": ["234", "396", "522", "738"],
    },
    {
        "text": "<p><strong>Boʻluvchilar soni.</strong> 180 sonining nechta natural boʻluvchisi bor?</p>",
        "explanation": "<p><strong>18</strong> — toʻgʻri javob. Sonni tub koʻpaytuvchilarga ajratamiz: 180 = 2²·3²·5¹. Boʻluvchilar soni formulasi boʻyicha darajalarga 1 qoʻshib koʻpaytiramiz: (2+1)·(2+1)·(1+1) = 3·3·2 = <strong>18</strong>.</p>",
        "correct": "18",
        "choices": ["12", "16", "18", "20"],
    },
    {
        "text": "<p><strong>Boʻluvchilar yigʻindisi.</strong> 28 sonining barcha natural boʻluvchilari yigʻindisini toping.</p>",
        "explanation": "<p><strong>56</strong> — toʻgʻri javob. 28 ning boʻluvchilari: 1, 2, 4, 7, 14, 28. Yigʻindisi: 1+2+4+7+14+28 = <strong>56</strong>. Diqqat: yigʻindi sonning oʻzidan 2 marta katta (56 = 2·28) — bunday sonlar <em>mukammal sonlar</em> deyiladi.</p>",
        "correct": "56",
        "choices": ["28", "42", "56", "60"],
    },
    {
        "text": "<p><strong>Oʻzaro tub sonlar.</strong> Quyidagi juftliklardan qaysi biri oʻzaro tub sonlardan iborat?</p>",
        "explanation": "<p><strong>15 va 28</strong> — toʻgʻri javob. Oʻzaro tub sonlarning EKUBi 1 ga teng. Tekshiramiz: EKUB(14, 21) = 7; <strong>EKUB(15, 28) = 1</strong> ✓ (15 = 3·5, 28 = 2²·7 — umumiy tub koʻpaytuvchi yoʻq); EKUB(18, 24) = 6; EKUB(26, 39) = 13.</p>",
        "correct": "15 va 28",
        "choices": ["14 va 21", "15 va 28", "18 va 24", "26 va 39"],
    },
    {
        "text": "<p><strong>Kasrlar — masala.</strong> Irodaning kitobi 90 betdan iborat. U birinchi kuni kitobning 2/5 qismini, ikkinchi kuni esa 1/3 qismini oʻqidi. Unga yana necha bet oʻqish qoldi?</p>",
        "explanation": "<p><strong>24 bet</strong> — toʻgʻri javob. Oʻqilgan qism: 2/5 + 1/3 = 6/15 + 5/15 = 11/15. Qolgan qism: 1 − 11/15 = 4/15. Betlarda: 90 · 4/15 = 6 · 4 = <strong>24 bet</strong>.</p>",
        "correct": "24 bet",
        "choices": ["18 bet", "24 bet", "30 bet", "36 bet"],
    },
    {
        "text": "<p><strong>Kasrlar ustida amallar.</strong> Hisoblang: 2/3 + 3/4 − 1/2</p>",
        "explanation": "<p><strong>11/12</strong> — toʻgʻri javob. Umumiy maxraj 12 ga keltiramiz: 2/3 = 8/12, 3/4 = 9/12, 1/2 = 6/12. Endi: 8/12 + 9/12 − 6/12 = <strong>11/12</strong>.</p>",
        "correct": "11/12",
        "choices": ["5/12", "7/12", "11/12", "13/12"],
    },
    {
        "text": "<p><strong>Harakat — quvib yetish.</strong> Iroda soat 8:00 da uydan piyoda 5 km/soat tezlik bilan chiqdi. Soat 9:00 da esa Jasur xuddi shu yoʻl boʻylab velosipedda 15 km/soat tezlik bilan uning ortidan chiqdi. Jasur Irodani yoʻlga chiqqanidan necha minut keyin quvib yetadi?</p>",
        "explanation": "<p><strong>30 minut</strong> — toʻgʻri javob. Jasur chiqqan paytda Iroda 1 soat yurgan boʻladi, ya'ni oralaridagi masofa 5·1 = 5 km. Yaqinlashish tezligi: 15 − 5 = 10 km/soat. Vaqt = 5 : 10 = 0,5 soat = <strong>30 minut</strong> (ya'ni soat 9:30 da).</p>",
        "correct": "30 minut",
        "choices": ["20 minut", "30 minut", "40 minut", "45 minut"],
    },
    {
        "text": "<p><strong>Harakat — qarama-qarshi yoʻnalish.</strong> Ikki qishloq orasidagi masofa 30 km. Samandar birinchi qishloqdan 4 km/soat, Shaxzoda esa ikkinchi qishloqdan 6 km/soat tezlik bilan bir vaqtda bir-biriga qarab yoʻlga chiqdi. Ular necha soatdan keyin uchrashadi?</p>",
        "explanation": "<p><strong>3 soat</strong> — toʻgʻri javob. Bir-biriga qarab harakatlanganda tezliklar qoʻshiladi: 4 + 6 = 10 km/soat. Uchrashish vaqti = masofa : yaqinlashish tezligi = 30 : 10 = <strong>3 soat</strong>.</p>",
        "correct": "3 soat",
        "choices": ["2 soat", "3 soat", "4 soat", "5 soat"],
    },
    {
        "text": "<p><strong>Tezlik, vaqt, masofa.</strong> Madina 45 km yoʻlni 3 soatda bosib oʻtdi. Xuddi shu tezlik bilan u 75 km yoʻlni necha soatda bosib oʻtadi?</p>",
        "explanation": "<p><strong>5 soat</strong> — toʻgʻri javob. Avval tezlikni topamiz: v = 45 : 3 = 15 km/soat. Endi vaqtni topamiz: t = 75 : 15 = <strong>5 soat</strong>.</p>",
        "correct": "5 soat",
        "choices": ["4 soat", "5 soat", "6 soat", "7 soat"],
    },
    {
        "text": "<p><strong>Tub sonlar.</strong> 1 dan 50 gacha boʻlgan sonlar ichida nechta tub son bor?</p>",
        "explanation": "<p><strong>15 ta</strong> — toʻgʻri javob. Ular: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 — jami <strong>15 ta</strong>. Esda tuting: 1 soni na tub, na murakkab son; 2 esa yagona juft tub son.</p>",
        "correct": "15 ta",
        "choices": ["14 ta", "15 ta", "16 ta", "17 ta"],
    },
    {
        "text": "<p><strong>Murakkab sonlar.</strong> Quyidagi sonlardan qaysi biri murakkab son?</p>",
        "explanation": "<p><strong>87</strong> — toʻgʻri javob. 87 raqamlari yigʻindisi 8+7 = 15, u 3 ga boʻlinadi, demak 87 = 3·29 — murakkab son. Qolganlari (61, 71, 97) faqat 1 ga va oʻziga boʻlinadi, ya'ni tub sonlar.</p>",
        "correct": "87",
        "choices": ["61", "71", "87", "97"],
    },
    {
        "text": "<p><strong>Mantiq + boʻluvchilar.</strong> Aynan <u>6 ta</u> natural boʻluvchiga ega boʻlgan eng kichik natural sonni toping.</p>",
        "explanation": "<p><strong>12</strong> — toʻgʻri javob. 12 = 2²·3 → boʻluvchilar soni (2+1)·(1+1) = 6 ta: 1, 2, 3, 4, 6, 12. Kichikroq sonlarni tekshiramiz: 6 ning 4 ta, 8 ning 4 ta, 9 ning 3 ta, 10 ning 4 ta boʻluvchisi bor. Demak eng kichigi — <strong>12</strong>.</p>",
        "correct": "12",
        "choices": ["12", "18", "24", "36"],
    },
]


# =====================================================================
# 2-TEST — Oʻrta daraja: aralash mavzular
# =====================================================================

test_math_2 = [
    {
        "text": "<p><strong>EKUB — masala.</strong> Firdavs 48 ta qalam va 36 ta daftarni oʻquvchilarga teng boʻlib bermoqchi. Har bir oʻquvchi bir xil miqdorda qalam va bir xil miqdorda daftar olishi, hech narsa ortib qolmasligi kerak. <u>Eng koʻpi bilan</u> nechta oʻquvchiga boʻlib bera oladi?</p>",
        "explanation": "<p><strong>12 ta</strong> — toʻgʻri javob. 48 = 2⁴·3, 36 = 2²·3² → EKUB(48, 36) = 2²·3 = <strong>12</strong>. Har bir oʻquvchiga 48:12 = 4 ta qalam va 36:12 = 3 ta daftar tushadi.</p>",
        "correct": "12 ta",
        "choices": ["6 ta", "9 ta", "12 ta", "18 ta"],
    },
    {
        "text": "<p><strong>EKUK — vaqt masalasi.</strong> Bekatdan Ilgʻor kutayotgan avtobus har 15 minutda, Javohir kutayotgan avtobus esa har 25 minutda joʻnaydi. Ikkala avtobus ham soat 7:00 da birga joʻnadi. Ular keyingi safar soat nechada birga joʻnaydi?</p>",
        "explanation": "<p><strong>8:15</strong> — toʻgʻri javob. 15 = 3·5, 25 = 5² → EKUK(15, 25) = 3·5² = 75 minut = 1 soat 15 minut. 7:00 + 1 soat 15 minut = <strong>8:15</strong>.</p>",
        "correct": "8:15",
        "choices": ["8:05", "8:15", "8:30", "9:00"],
    },
    {
        "text": "<p><strong>EKUK (uchta son).</strong> Sirojiddin basseynga har 3 kunda, Behruz har 4 kunda, Elbek esa har 6 kunda boradi. Bugun uchalasi basseynda uchrashdi. Ular necha kundan keyin yana birga uchrashadi?</p>",
        "explanation": "<p><strong>12 kun</strong> — toʻgʻri javob. 3 = 3, 4 = 2², 6 = 2·3 → EKUK = 2²·3 = <strong>12</strong>. 12 soni 3 ga ham, 4 ga ham, 6 ga ham qoldiqsiz boʻlinadi va bundan kichik bunday son yoʻq.</p>",
        "correct": "12",
        "choices": ["12", "24", "36", "72"],
    },
    {
        "text": "<p><strong>EKUB va EKUK bogʻliqligi.</strong> Ikki natural sonning koʻpaytmasi 360 ga, EKUBi esa 6 ga teng. Bu sonlarning EKUKini toping.</p>",
        "explanation": "<p><strong>60</strong> — toʻgʻri javob. Muhim qoida: <strong>EKUB(a,b) · EKUK(a,b) = a · b</strong>. Demak EKUK = 360 : 6 = <strong>60</strong>. (Masalan, bu sonlar 6 va 60 boʻlishi mumkin: 6·60 = 360, EKUB = 6, EKUK = 60.)</p>",
        "correct": "60",
        "choices": ["30", "60", "72", "120"],
    },
    {
        "text": "<p><strong>Boʻlinish alomati (8 ga).</strong> Uch xonali <em>7X2</em> soni 8 ga qoldiqsiz boʻlinadi. X raqamining eng katta qiymatini toping.</p>",
        "explanation": "<p><strong>9</strong> — toʻgʻri javob. Uch xonali sonda 8 ga boʻlinishni toʻgʻridan-toʻgʻri tekshiramiz: 712:8 = 89 ✓, 752:8 = 94 ✓, 792:8 = 99 ✓. Demak X = 1, 5 yoki 9. Eng kattasi — <strong>9</strong>.</p>",
        "correct": "9",
        "choices": ["1", "5", "7", "9"],
    },
    {
        "text": "<p><strong>Boʻlinish alomati (12 ga).</strong> Quyidagi sonlardan qaysi biri 12 ga qoldiqsiz boʻlinadi?</p>",
        "explanation": "<p><strong>348</strong> — toʻgʻri javob. 12 ga boʻlinish = 3 ga <u>va</u> 4 ga boʻlinish. 348: raqamlar yigʻindisi 3+4+8 = 15 → 3 ga boʻlinadi ✓; oxirgi ikki raqam 48:4 = 12 ✓. Demak 348:12 = 29. Qolganlarida 4 ga boʻlinish sharti bajarilmaydi (46, 22, 14 — 4 ga boʻlinmaydi).</p>",
        "correct": "348",
        "choices": ["246", "348", "522", "714"],
    },
    {
        "text": "<p><strong>Boʻluvchilar soni.</strong> 360 sonining nechta natural boʻluvchisi bor?</p>",
        "explanation": "<p><strong>24 ta</strong> — toʻgʻri javob. 360 = 2³·3²·5¹. Boʻluvchilar soni: (3+1)·(2+1)·(1+1) = 4·3·2 = <strong>24</strong>.</p>",
        "correct": "24 ta",
        "choices": ["20 ta", "24 ta", "28 ta", "30 ta"],
    },
    {
        "text": "<p><strong>Boʻluvchilar yigʻindisi.</strong> 60 sonining barcha natural boʻluvchilari yigʻindisini toping.</p>",
        "explanation": "<p><strong>168</strong> — toʻgʻri javob. 60 = 2²·3·5. Boʻluvchilar yigʻindisi formulasi: (1+2+4)·(1+3)·(1+5) = 7·4·6 = <strong>168</strong>. Tekshirish: 1+2+3+4+5+6+10+12+15+20+30+60 = 168 ✓.</p>",
        "correct": "168",
        "choices": ["108", "144", "168", "180"],
    },
    {
        "text": "<p><strong>Oʻzaro tub sonlar.</strong> Quyidagi sonlardan qaysi biri 24 bilan oʻzaro tub?</p>",
        "explanation": "<p><strong>25</strong> — toʻgʻri javob. 24 = 2³·3. Son 24 bilan oʻzaro tub boʻlishi uchun unda 2 ham, 3 ham koʻpaytuvchi boʻlmasligi kerak. 15 = 3·5 (3 bor ✗), 18 = 2·3² ✗, 32 = 2⁵ ✗, <strong>25 = 5²</strong> ✓ → EKUB(24, 25) = 1.</p>",
        "correct": "25",
        "choices": ["15", "18", "25", "32"],
    },
    {
        "text": "<p><strong>Kasrlar — masala.</strong> Charosda 60 000 soʻm bor edi. U pulining 1/3 qismiga kitob, <u>qolgan pulining</u> 1/4 qismiga sharbat sotib oldi. Unda qancha pul qoldi?</p>",
        "explanation": "<p><strong>30 000 soʻm</strong> — toʻgʻri javob. Kitobga: 60 000 · 1/3 = 20 000 soʻm, qoldi 40 000 soʻm. Sharbatga <u>qolganining</u> 1/4 qismi: 40 000 · 1/4 = 10 000 soʻm. Qoldi: 40 000 − 10 000 = <strong>30 000 soʻm</strong>.</p>",
        "correct": "30 000 soʻm",
        "choices": ["25 000 soʻm", "30 000 soʻm", "35 000 soʻm", "40 000 soʻm"],
    },
    {
        "text": "<p><strong>Kasrlar ustida amallar.</strong> Hisoblang: (2/3 · 9/8) : 3/4</p>",
        "explanation": "<p><strong>1</strong> — toʻgʻri javob. Avval koʻpaytiramiz: 2/3 · 9/8 = 18/24 = 3/4. Soʻng boʻlamiz: 3/4 : 3/4 = 3/4 · 4/3 = <strong>1</strong>. (Bir xil sonni oʻziga boʻlsak, natija har doim 1.)</p>",
        "correct": "1",
        "choices": ["3/4", "1", "4/3", "9/8"],
    },
    {
        "text": "<p><strong>Kasrlarni taqqoslash.</strong> Quyidagi kasrlardan qaysi biri eng katta?</p>",
        "explanation": "<p><strong>2/3</strong> — toʻgʻri javob. Oʻnli kasrga aylantiramiz: 5/8 = 0,625; 7/12 ≈ 0,583; <strong>2/3 ≈ 0,667</strong>; 3/5 = 0,6. Eng kattasi — 2/3.</p>",
        "correct": "2/3",
        "choices": ["5/8", "7/12", "2/3", "3/5"],
    },
    {
        "text": "<p><strong>Harakat — qarama-qarshi tomonga.</strong> Davron va Sherbek bir nuqtadan bir vaqtda qarama-qarshi tomonlarga yoʻlga chiqdi. Davronning tezligi 5 km/soat, Sherbekniki 7 km/soat. Ular orasidagi masofa necha soatdan keyin 36 km boʻladi?</p>",
        "explanation": "<p><strong>3 soat</strong> — toʻgʻri javob. Qarama-qarshi tomonga harakatlanganda uzoqlashish tezligi tezliklar yigʻindisiga teng: 5 + 7 = 12 km/soat. Vaqt = 36 : 12 = <strong>3 soat</strong>.</p>",
        "correct": "3 soat",
        "choices": ["2 soat", "3 soat", "4 soat", "6 soat"],
    },
    {
        "text": "<p><strong>Harakat — quvib yetish.</strong> Marjona 6 km/soat tezlik bilan yoʻlga chiqdi. Oradan 2 soat oʻtgach, Abdulloh xuddi shu yoʻldan velosipedda 14 km/soat tezlik bilan uning ortidan chiqdi. Abdulloh Marjonani qancha vaqtdan keyin quvib yetadi?</p>",
        "explanation": "<p><strong>1 soat 30 minut</strong> — toʻgʻri javob. Abdulloh chiqqanda oradagi masofa: 6·2 = 12 km. Yaqinlashish tezligi: 14 − 6 = 8 km/soat. Vaqt = 12 : 8 = 1,5 soat = <strong>1 soat 30 minut</strong>.</p>",
        "correct": "1 soat 30 minut",
        "choices": ["1 soat 30 minut", "2 soat", "2 soat 30 minut", "3 soat"],
    },
    {
        "text": "<p><strong>Tezlik va vaqt.</strong> Poyezd 240 km yoʻlni 3 soatda bosib oʻtdi. Agar u tezligini 20 km/soatga oshirsa, xuddi shu yoʻlni qancha vaqtda bosib oʻtadi?</p>",
        "explanation": "<p><strong>2 soat 24 minut</strong> — toʻgʻri javob. Dastlabki tezlik: 240 : 3 = 80 km/soat. Yangi tezlik: 80 + 20 = 100 km/soat. Yangi vaqt: 240 : 100 = 2,4 soat = 2 soat + 0,4·60 minut = <strong>2 soat 24 minut</strong>.</p>",
        "correct": "2 soat 24 minut",
        "choices": ["2 soat", "2 soat 24 minut", "2 soat 30 minut", "2 soat 40 minut"],
    },
    {
        "text": "<p><strong>Tub sonlar — mantiq.</strong> Ikkita tub sonning yigʻindisi 2019 ga teng. Ulardan <u>kichigi</u> nechaga teng?</p>",
        "explanation": "<p><strong>2</strong> — toʻgʻri javob. 2019 — toq son. Ikki sonning yigʻindisi toq boʻlishi uchun ulardan biri juft, biri toq boʻlishi kerak. Yagona juft tub son — bu 2. Demak kichigi <strong>2</strong>, kattasi esa 2017 (u tub son).</p>",
        "correct": "2",
        "choices": ["2", "3", "5", "7"],
    },
]


# =====================================================================
# 3-TEST — Qiyin daraja: chuqurlashtirilgan mantiq
# =====================================================================

test_math_3 = [
    {
        "text": "<p><strong>EKUB — qoldiqli masala.</strong> Shunday <u>eng katta</u> natural sonni topingki, 62 ni unga boʻlganda 2 qoldiq, 100 ni boʻlganda esa 4 qoldiq qolsin.</p>",
        "explanation": "<p><strong>12</strong> — toʻgʻri javob. Agar 62 ni boʻlganda 2 qoldiq qolsa, demak (62 − 2) = 60 qoldiqsiz boʻlinadi. Xuddi shunday (100 − 4) = 96 ham qoldiqsiz boʻlinadi. Izlanayotgan son 60 va 96 ning umumiy boʻluvchisi, eng kattasi — EKUB(60, 96) = <strong>12</strong>. Tekshirish: 62 = 12·5 + 2 ✓, 100 = 12·8 + 4 ✓.</p>",
        "correct": "12",
        "choices": ["6", "12", "15", "24"],
    },
    {
        "text": "<p><strong>EKUK — qoldiqli masala.</strong> 6 ga ham, 8 ga ham, 9 ga ham boʻlganda 3 qoldiq qoladigan eng kichik <u>uch xonali</u> sonni toping.</p>",
        "explanation": "<p><strong>147</strong> — toʻgʻri javob. Izlanayotgan son n boʻlsin. (n − 3) soni 6, 8 va 9 ga boʻlinadi, ya'ni u EKUK(6, 8, 9) = 72 ga karrali. Demak n = 72k + 3: 75, 147, 219, ... Uch xonalilaridan eng kichigi — <strong>147</strong> (147 = 72·2 + 3).</p>",
        "correct": "147",
        "choices": ["75", "111", "147", "219"],
    },
    {
        "text": "<p><strong>EKUB va EKUK.</strong> Ikki sonning EKUBi 12 ga, EKUKi esa 180 ga teng. Sonlardan biri 36 boʻlsa, ikkinchisini toping.</p>",
        "explanation": "<p><strong>60</strong> — toʻgʻri javob. EKUB·EKUK = a·b qoidasidan: a·b = 12·180 = 2160. Ikkinchi son: 2160 : 36 = <strong>60</strong>. Tekshirish: EKUB(36, 60) = 12 ✓, EKUK(36, 60) = 180 ✓.</p>",
        "correct": "60",
        "choices": ["48", "60", "72", "90"],
    },
    {
        "text": "<p><strong>Boʻlinish — mantiq.</strong> <em>abab</em> koʻrinishidagi har qanday toʻrt xonali son (masalan, 2323 yoki 7171) albatta qaysi songa boʻlinadi?</p>",
        "explanation": "<p><strong>101</strong> — toʻgʻri javob. Sonni yoyib yozamiz: abab = 1000a + 100b + 10a + b = 1010a + 101b = <strong>101·(10a + b)</strong>. Demak u har doim 101 ga boʻlinadi. Masalan: 2323 = 101·23, 7171 = 101·71.</p>",
        "correct": "101",
        "choices": ["7", "11", "13", "101"],
    },
    {
        "text": "<p><strong>Boʻluvchilar — mantiq.</strong> N = 2⁵·3⁴·5² sonining nechta natural boʻluvchisi 10 ga qoldiqsiz boʻlinadi?</p>",
        "explanation": "<p><strong>50 ta</strong> — toʻgʻri javob. Boʻluvchi d = 2ᵃ·3ᵇ·5ᶜ koʻrinishida. U 10 = 2·5 ga boʻlinishi uchun a ≥ 1 va c ≥ 1 boʻlishi shart. Demak a ∈ {1..5} — 5 ta, b ∈ {0..4} — 5 ta, c ∈ {1, 2} — 2 ta. Jami: 5·5·2 = <strong>50</strong>.</p>",
        "correct": "50 ta",
        "choices": ["30 ta", "45 ta", "50 ta", "60 ta"],
    },
    {
        "text": "<p><strong>Boʻluvchilar — mantiq.</strong> 720 sonining nechta natural boʻluvchisi <u>toʻliq kvadrat</u> (ya'ni biror natural sonning kvadrati)?</p>",
        "explanation": "<p><strong>6 ta</strong> — toʻgʻri javob. 720 = 2⁴·3²·5. Boʻluvchi toʻliq kvadrat boʻlishi uchun uning barcha darajalari juft boʻlishi kerak: 2 ning darajasi ∈ {0, 2, 4} — 3 ta, 3 niki ∈ {0, 2} — 2 ta, 5 niki faqat {0} — 1 ta. Jami 3·2·1 = <strong>6</strong> ta: 1, 4, 16, 9, 36, 144.</p>",
        "correct": "6 ta",
        "choices": ["4 ta", "5 ta", "6 ta", "8 ta"],
    },
    {
        "text": "<p><strong>Boʻluvchilar yigʻindisi.</strong> 96 sonining barcha natural boʻluvchilari yigʻindisini toping.</p>",
        "explanation": "<p><strong>252</strong> — toʻgʻri javob. 96 = 2⁵·3. Formuladan: (1+2+4+8+16+32)·(1+3) = 63·4 = <strong>252</strong>. Tekshirish: 1+2+3+4+6+8+12+16+24+32+48+96 = 252 ✓.</p>",
        "correct": "252",
        "choices": ["192", "240", "252", "256"],
    },
    {
        "text": "<p><strong>Boʻluvchilar — mantiq.</strong> 600 sonining nechta natural boʻluvchisi <u>toq son</u>?</p>",
        "explanation": "<p><strong>6 ta</strong> — toʻgʻri javob. 600 = 2³·3·5². Toq boʻluvchida 2 umuman qatnashmaydi, ya'ni ular 3·5² = 75 sonining boʻluvchilari: (1+1)·(2+1) = <strong>6</strong> ta — 1, 3, 5, 15, 25, 75.</p>",
        "correct": "6 ta",
        "choices": ["4 ta", "6 ta", "8 ta", "12 ta"],
    },
    {
        "text": "<p><strong>Oʻzaro tub sonlar.</strong> 1 dan 30 gacha boʻlgan natural sonlar ichida 30 bilan oʻzaro tub boʻlgan nechta son bor?</p>",
        "explanation": "<p><strong>8 ta</strong> — toʻgʻri javob. 30 = 2·3·5, demak 2, 3 yoki 5 ga boʻlinadigan sonlarni tashlab yuboramiz. Qoladi: 1, 7, 11, 13, 17, 19, 23, 29 — jami <strong>8 ta</strong>.</p>",
        "correct": "8 ta",
        "choices": ["6 ta", "8 ta", "10 ta", "12 ta"],
    },
    {
        "text": "<p><strong>Kasrlar — mantiqiy koʻpaytma.</strong> Hisoblang: (1 − 1/2)·(1 − 1/3)·(1 − 1/4)· ... ·(1 − 1/10)</p>",
        "explanation": "<p><strong>1/10</strong> — toʻgʻri javob. Har bir qavsni kasrga aylantiramiz: 1/2 · 2/3 · 3/4 · ... · 9/10. Qoʻshni kasrlarning surat va maxrajlari qisqaradi (2 bilan 2, 3 bilan 3, ...), faqat birinchi surat 1 va oxirgi maxraj 10 qoladi: natija <strong>1/10</strong>.</p>",
        "correct": "1/10",
        "choices": ["1/10", "1/5", "1/2", "9/10"],
    },
    {
        "text": "<p><strong>Kasrlar ustida amallar.</strong> Hisoblang: ((2/3 + 3/4) : (5/6 − 1/2)) · 2/17</p>",
        "explanation": "<p><strong>1/2</strong> — toʻgʻri javob. Qavslarni alohida hisoblaymiz: 2/3 + 3/4 = 8/12 + 9/12 = 17/12; 5/6 − 1/2 = 5/6 − 3/6 = 2/6 = 1/3. Boʻlamiz: 17/12 : 1/3 = 17/12 · 3 = 17/4. Koʻpaytiramiz: 17/4 · 2/17 = 2/4 = <strong>1/2</strong>.</p>",
        "correct": "1/2",
        "choices": ["1/4", "1/2", "3/4", "2"],
    },
    {
        "text": "<p><strong>Kasrlar — masala.</strong> Jasur pulining 3/8 qismiga kitob oldi, <u>qolgan pulining</u> 2/5 qismini esa ovqatga sarfladi. Natijada unda 45 000 soʻm qoldi. Boshida uning qancha puli bor edi?</p>",
        "explanation": "<p><strong>120 000 soʻm</strong> — toʻgʻri javob. Kitobdan keyin 1 − 3/8 = 5/8 qism qoldi. Undan 2/5 sarflandi, ya'ni 3/5 qismi qoldi: 5/8 · 3/5 = 3/8. Demak boshlangʻich pulning 3/8 qismi 45 000 soʻm. Butun pul: 45 000 : 3/8 = 45 000 · 8/3 = <strong>120 000 soʻm</strong>.</p>",
        "correct": "120 000 soʻm",
        "choices": ["96 000 soʻm", "108 000 soʻm", "120 000 soʻm", "150 000 soʻm"],
    },
    {
        "text": "<p><strong>Harakat — quvib yetish.</strong> Iroda soat 8:00 da piyoda 5 km/soat tezlik bilan yoʻlga chiqdi. Jasur esa soat 9:30 da xuddi shu yoʻldan velosipedda 15 km/soat tezlik bilan uning ortidan chiqdi. Jasur Irodani soat nechada quvib yetadi?</p>",
        "explanation": "<p><strong>10:15</strong> — toʻgʻri javob. Jasur chiqqanda Iroda 1,5 soat yurgan: 5·1,5 = 7,5 km oldinda. Yaqinlashish tezligi: 15 − 5 = 10 km/soat. Vaqt: 7,5 : 10 = 0,75 soat = 45 minut. 9:30 + 45 minut = <strong>10:15</strong>.</p>",
        "correct": "10:15",
        "choices": ["10:00", "10:15", "10:30", "11:00"],
    },
    {
        "text": "<p><strong>Oʻrtacha tezlik — tuzoqli savol.</strong> Samandar shaharga 60 km/soat tezlik bilan bordi va xuddi shu yoʻldan 40 km/soat tezlik bilan qaytdi. Uning butun yoʻldagi <u>oʻrtacha tezligi</u> qancha?</p>",
        "explanation": "<p><strong>48 km/soat</strong> — toʻgʻri javob. Diqqat: (60+40):2 = 50 <u>notoʻgʻri</u>, chunki vaqtlar teng emas! Yoʻl uzunligini 120 km deb olamiz: borish 120:60 = 2 soat, qaytish 120:40 = 3 soat. Umumiy yoʻl 240 km, umumiy vaqt 5 soat. Oʻrtacha tezlik = 240 : 5 = <strong>48 km/soat</strong>.</p>",
        "correct": "48 km/soat",
        "choices": ["45 km/soat", "48 km/soat", "50 km/soat", "52 km/soat"],
    },
    {
        "text": "<p><strong>Harakat — uchrashuv nuqtasi.</strong> A va B shaharlar orasidagi masofa 90 km. Behruz A dan 30 km/soat, Elbek esa B dan 15 km/soat tezlik bilan bir vaqtda bir-biriga qarab yoʻlga chiqdi. Ular uchrashgan nuqta A shahardan necha km uzoqlikda boʻladi?</p>",
        "explanation": "<p><strong>60 km</strong> — toʻgʻri javob. Yaqinlashish tezligi: 30 + 15 = 45 km/soat. Uchrashish vaqti: 90 : 45 = 2 soat. Shu vaqtda Behruz A dan 30·2 = <strong>60 km</strong> yurgan boʻladi (Elbek esa 15·2 = 30 km; 60 + 30 = 90 ✓).</p>",
        "correct": "60 km",
        "choices": ["45 km", "50 km", "60 km", "70 km"],
    },
    {
        "text": "<p><strong>Harakat — poyezd masalasi.</strong> Uzunligi 200 m boʻlgan poyezd 20 m/s tezlik bilan harakatlanmoqda. U uzunligi 400 m boʻlgan koʻprikdan toʻliq oʻtib boʻlishi uchun necha sekund kerak boʻladi?</p>",
        "explanation": "<p><strong>30 sekund</strong> — toʻgʻri javob. Poyezd koʻprikdan <u>toʻliq</u> oʻtishi uchun oʻz uzunligini ham qoʻshib bosib oʻtishi kerak: 400 + 200 = 600 m. Vaqt = 600 : 20 = <strong>30 sekund</strong>.</p>",
        "correct": "30 sekund",
        "choices": ["20 sekund", "25 sekund", "30 sekund", "35 sekund"],
    },
]


# =====================================================================
# 4-TEST — Qiyin daraja: olimpiada uslubidagi mantiq
# =====================================================================

test_math_4 = [
    {
        "text": "<p><strong>EKUB — mantiqiy tanlov.</strong> Ikki natural sonning yigʻindisi 96 ga, EKUBi esa 16 ga teng. Bu qanday sonlar?</p>",
        "explanation": "<p><strong>16 va 80</strong> — toʻgʻri javob. EKUB 16 boʻlsa, sonlar 16a va 16b koʻrinishida, bunda EKUB(a, b) = 1. Yigʻindidan: 16a + 16b = 96 → a + b = 6, oʻzaro tublardan: a = 1, b = 5. Demak sonlar 16 va 80. Boshqa variantlarni tekshiring: EKUB(32, 64) = 32 ✗, EKUB(48, 48) = 48 ✗, EKUB(24, 72) = 24 ✗.</p>",
        "correct": "16 va 80",
        "choices": ["16 va 80", "24 va 72", "32 va 64", "48 va 48"],
    },
    {
        "text": "<p><strong>EKUK + kalendar mantigʻi.</strong> Charos kutubxonaga har 2 kunda, Afsona har 5 kunda, Marjona esa har 6 kunda keladi. Bugun — <u>dushanba</u> va uchalasi ham kutubxonada uchrashdi. Ular keyingi safar birga qaysi kuni uchrashadi?</p>",
        "explanation": "<p><strong>Chorshanba</strong> — toʻgʻri javob. Avval EKUK(2, 5, 6) ni topamiz: 2 = 2, 5 = 5, 6 = 2·3 → EKUK = 2·3·5 = 30 kun. Endi hafta kunini aniqlaymiz: 30 = 7·4 + 2, ya'ni 4 ta toʻliq hafta va yana 2 kun. Dushanbadan 2 kun keyin — <strong>chorshanba</strong>.</p>",
        "correct": "Chorshanba",
        "choices": ["Seshanba", "Chorshanba", "Payshanba", "Juma"],
    },
    {
        "text": "<p><strong>EKUB — amaliy masala.</strong> Uzunligi 3 m 30 sm, eni 2 m 10 sm boʻlgan pol bir xil oʻlchamli kvadrat plitkalar bilan kesmasdan toʻliq qoplanadi. Buning uchun <u>eng kamida</u> nechta plitka kerak boʻladi?</p>",
        "explanation": "<p><strong>77 ta</strong> — toʻgʻri javob. Plitkalar soni eng kam boʻlishi uchun ular eng katta boʻlsin: kvadrat tomoni = EKUB(330, 210) = 30 sm. Uzunlik boʻyicha 330:30 = 11 ta, en boʻyicha 210:30 = 7 ta. Jami: 11·7 = <strong>77 ta</strong>.</p>",
        "correct": "77 ta",
        "choices": ["63 ta", "72 ta", "77 ta", "84 ta"],
    },
    {
        "text": "<p><strong>Boʻlinish — olimpiada masalasi.</strong> N soni faqat 0 va 1 raqamlaridan tuzilgan va 45 ga qoldiqsiz boʻlinadi. Eng kichik shunday son nechta raqamdan iborat?</p>",
        "explanation": "<p><strong>10 ta</strong> — toʻgʻri javob. 45 = 9·5. 5 ga boʻlinishi uchun son 0 yoki 5 bilan tugashi kerak → faqat 0 boʻlishi mumkin. 9 ga boʻlinishi uchun raqamlar yigʻindisi 9 ga karrali boʻlsin → kamida <u>toʻqqizta</u> 1 raqami kerak. Demak eng kichik son: 1111111110 — <strong>10 ta</strong> raqam (1111111110 : 45 = 24691358).</p>",
        "correct": "10 ta",
        "choices": ["9 ta", "10 ta", "11 ta", "12 ta"],
    },
    {
        "text": "<p><strong>Mantiq — qonuniyat.</strong> 2¹⁰⁰ sonining oxirgi raqami qanday?</p>",
        "explanation": "<p><strong>6</strong> — toʻgʻri javob. 2 ning darajalari oxirgi raqamlarini kuzatamiz: 2, 4, 8, 6, soʻng yana 2, 4, 8, 6 — davr 4 ga teng. 100 : 4 = 25, qoldiq 0 → demak 2¹⁰⁰ davrning oxirgi (4-chi) raqami bilan tugaydi, ya'ni <strong>6</strong>.</p>",
        "correct": "6",
        "choices": ["2", "4", "6", "8"],
    },
    {
        "text": "<p><strong>Boʻluvchilar — mantiq.</strong> 100 dan kichik boʻlgan nechta natural sonning aynan <u>3 ta</u> boʻluvchisi bor?</p>",
        "explanation": "<p><strong>4 ta</strong> — toʻgʻri javob. Boʻluvchilar soni 3 boʻlishi uchun son p² koʻrinishida (p — tub) boʻlishi kerak, chunki (2+1) = 3. Bunda boʻluvchilar: 1, p, p². 100 dan kichiklari: 2² = 4, 3² = 9, 5² = 25, 7² = 49 — jami <strong>4 ta</strong> (11² = 121 juda katta).</p>",
        "correct": "4 ta",
        "choices": ["3 ta", "4 ta", "5 ta", "6 ta"],
    },
    {
        "text": "<p><strong>Boʻluvchilar yigʻindisi — teskari masala.</strong> Quyidagi sonlardan qaysi birining barcha natural boʻluvchilari yigʻindisi 39 ga teng?</p>",
        "explanation": "<p><strong>18</strong> — toʻgʻri javob. 18 ning boʻluvchilari: 1, 2, 3, 6, 9, 18 → yigʻindisi 1+2+3+6+9+18 = <strong>39</strong> ✓. Qolganlari: 16 → 31; 24 → 60; 30 → 72.</p>",
        "correct": "18",
        "choices": ["16", "18", "24", "30"],
    },
    {
        "text": "<p><strong>Tub sonlar — mantiq.</strong> p va p+2 egizak tub sonlar boʻlsin (p > 3). U holda ular orasidagi p+1 soni albatta nechaga boʻlinadi?</p>",
        "explanation": "<p><strong>6 ga</strong> — toʻgʻri javob. p toq tub son, demak p+1 juft → 2 ga boʻlinadi. Ketma-ket kelgan uch sondan (p, p+1, p+2) biri albatta 3 ga boʻlinadi; p va p+2 tub va 3 dan katta, demak ular 3 ga boʻlinmaydi → faqat p+1 boʻlinadi. 2 ga ham, 3 ga ham boʻlingani uchun p+1 soni <strong>6 ga</strong> boʻlinadi. Masalan: 11 va 13 → 12; 17 va 19 → 18.</p>",
        "correct": "6 ga",
        "choices": ["4 ga", "5 ga", "6 ga", "12 ga"],
    },
    {
        "text": "<p><strong>Tub va murakkab sonlar.</strong> p — tub son va p² + 2 ham tub son boʻlsa, p nechaga teng?</p>",
        "explanation": "<p><strong>3</strong> — toʻgʻri javob. Tekshiramiz: p = 2 → 4+2 = 6 = 2·3 murakkab ✗; <strong>p = 3 → 9+2 = 11 tub ✓</strong>; p = 5 → 25+2 = 27 = 3³ ✗; p = 7 → 49+2 = 51 = 3·17 ✗. Sababi: p ≠ 3 boʻlsa p² soni 3 ga boʻlinganda 1 qoldiq beradi, shuning uchun p²+2 har doim 3 ga boʻlinadi va tub boʻlolmaydi.</p>",
        "correct": "3",
        "choices": ["2", "3", "5", "7"],
    },
    {
        "text": "<p><strong>Ratsional sonlar.</strong> 0,4(6) davriy oʻnli kasrni oddiy kasr koʻrinishida yozing.</p>",
        "explanation": "<p><strong>7/15</strong> — toʻgʻri javob. 0,4(6) = 0,4666... = 0,4 + 0,0666... Bunda 0,4 = 2/5, 0,0666... = (1/10)·0,666... = (1/10)·(2/3) = 1/15. Yigʻamiz: 2/5 + 1/15 = 6/15 + 1/15 = <strong>7/15</strong>. Tekshirish: 7 : 15 = 0,4666... ✓</p>",
        "correct": "7/15",
        "choices": ["2/5", "7/15", "5/9", "23/50"],
    },
    {
        "text": "<p><strong>Kasrlar — mantiqiy yigʻindi.</strong> Hisoblang: 1/2 + 1/6 + 1/12 + 1/20 + 1/30</p>",
        "explanation": "<p><strong>5/6</strong> — toʻgʻri javob. Har bir had 1/(n·(n+1)) koʻrinishida va uni 1/n − 1/(n+1) shaklida yozish mumkin: (1/1 − 1/2) + (1/2 − 1/3) + (1/3 − 1/4) + (1/4 − 1/5) + (1/5 − 1/6). Oʻrtadagi hadlar qisqaradi, qoladi: 1 − 1/6 = <strong>5/6</strong>.</p>",
        "correct": "5/6",
        "choices": ["1/6", "4/5", "5/6", "6/5"],
    },
    {
        "text": "<p><strong>Birgalikdagi ish — kasrlar.</strong> Sherbek bir ishni 6 kunda, Davron esa xuddi shu ishni 12 kunda bajaradi. Ular birgalikda ishlasa, bu ishni necha kunda tugatadi?</p>",
        "explanation": "<p><strong>4 kun</strong> — toʻgʻri javob. Butun ishni 1 deb olamiz. Sherbek bir kunda 1/6 qismini, Davron 1/12 qismini bajaradi. Birgalikda bir kunda: 1/6 + 1/12 = 2/12 + 1/12 = 3/12 = 1/4 qism. Demak butun ish uchun 1 : 1/4 = <strong>4 kun</strong> kerak.</p>",
        "correct": "4 kun",
        "choices": ["3 kun", "4 kun", "8 kun", "9 kun"],
    },
    {
        "text": "<p><strong>Harakat — kechikish masalasi.</strong> Firdavs uyidan maktabgacha 4 km/soat tezlik bilan yursa darsga 5 minut kechikadi, 6 km/soat tezlik bilan yursa 5 minut oldin yetib boradi. Uy bilan maktab orasidagi masofani toping.</p>",
        "explanation": "<p><strong>2 km</strong> — toʻgʻri javob. Kerakli vaqt t soat, masofa s km boʻlsin. Sekin yurganda: s/4 = t + 5/60 = t + 1/12. Tez yurganda: s/6 = t − 1/12. Birinchidan ikkinchisini ayiramiz: s/4 − s/6 = 2/12 = 1/6. Chap tomon: 3s/12 − 2s/12 = s/12. Demak s/12 = 1/6 → s = <strong>2 km</strong>. (Tekshirish: 2:4 = 30 min, 2:6 = 20 min — farq 10 minut ✓)</p>",
        "correct": "2 km",
        "choices": ["1,5 km", "2 km", "2,5 km", "3 km"],
    },
    {
        "text": "<p><strong>Harakat — daryo masalasi.</strong> Qayiq daryo oqimi boʻyicha 30 km yoʻlni 2 soatda, oqimga qarshi esa xuddi shu 30 km yoʻlni 3 soatda bosib oʻtdi. Daryo oqimining tezligini toping.</p>",
        "explanation": "<p><strong>2,5 km/soat</strong> — toʻgʻri javob. Oqim boʻyicha tezlik: 30:2 = 15 km/soat (bu qayiq tezligi + oqim). Oqimga qarshi: 30:3 = 10 km/soat (qayiq tezligi − oqim). Ayirma ikkilangan oqim tezligini beradi: 15 − 10 = 5 → oqim = 5:2 = <strong>2,5 km/soat</strong> (qayiqning oʻz tezligi esa 12,5 km/soat).</p>",
        "correct": "2,5 km/soat",
        "choices": ["2 km/soat", "2,5 km/soat", "3 km/soat", "5 km/soat"],
    },
    {
        "text": "<p><strong>Harakat — uchrashuv mantigʻi.</strong> Ilgʻor A punktdan 12 km/soat, Javohir esa ayni vaqtda B punktdan 8 km/soat tezlik bilan bir-biriga qarab yoʻlga chiqdi. Uchrashgan paytda Ilgʻor Javohirdan 12 km koʻproq masofa bosib oʻtgan edi. AB masofani toping.</p>",
        "explanation": "<p><strong>60 km</strong> — toʻgʻri javob. Ikkalasi ham bir xil t vaqt yurdi. Masofalar farqi: 12t − 8t = 12 → 4t = 12 → t = 3 soat. Umumiy masofa = ikkalasining yoʻli: (12 + 8)·3 = <strong>60 km</strong>. (Ilgʻor 36 km, Javohir 24 km; 36 − 24 = 12 ✓)</p>",
        "correct": "60 km",
        "choices": ["40 km", "48 km", "60 km", "72 km"],
    },
    {
        "text": "<p><strong>Mantiq — sanash.</strong> Sirojiddin 1 dan 100 gacha boʻlgan barcha natural sonlarni yozdi. Ular ichida <u>na 3 ga, na 5 ga</u> boʻlinadigan nechta son bor?</p>",
        "explanation": "<p><strong>53 ta</strong> — toʻgʻri javob. 3 ga boʻlinadiganlar: 100:3 → 33 ta. 5 ga boʻlinadiganlar: 100:5 = 20 ta. Ikkalasiga ham (ya'ni 15 ga) boʻlinadiganlar: 100:15 → 6 ta — ular ikki marta sanaldi. Kamida bittasiga boʻlinadiganlar: 33 + 20 − 6 = 47 ta. Demak javob: 100 − 47 = <strong>53 ta</strong>.</p>",
        "correct": "53 ta",
        "choices": ["47 ta", "53 ta", "54 ta", "60 ta"],
    },
]
