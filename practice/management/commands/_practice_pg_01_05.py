# -*- coding: utf-8 -*-
"""Prime GMAT mashqlar — GMAT-1 … GMAT-5 (pilot).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan. Savollar INGLIZCHA (imtihon
tili), tushuntirishlar OʻZBEKCHA. Har savolda BESHTA variant, raqamli variantlar oʻsish
tartibida. Kalkulyatorsiz yechiladigan arifmetika.

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context · 15–16 trap-spotting ·
      17–18 harder · 19–20 word problems (har doim ikkita).

Subject `GMAT` — yangi fan. Telegram'ning kundalik testiga kirmaydi (ROTATION aniq roʻyxat).

Import:
    python manage.py import_practices practice/management/commands/_practice_pg_01_05.py \\
        --master=prime --expect-questions=20
"""

SUBJECT = {
    "name":        "GMAT",
    "description": "GMAT Quant — Prime GMAT darslarining mashqlari",
    "icon":        "bi-graph-up-arrow",
    "color":       "#0f766e",
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


def q(text, choices, correct, explanation):
    return {"text": f"<p>{text}</p>", "choices": choices, "correct": correct,
            "explanation": explanation}


# =====================================================================
# GMAT-1 — arithmetic without a calculator
# =====================================================================
Q1 = [
    q("What is 32 × 25?", ["640", "780", "800", "820", "8,000"], "800",
      "<p><strong>800.</strong> 32 ÷ 4 = 8, 8 × 100 = 800.</p><p><strong>8,000</strong> — 4 ga boʻlmasdan 32 ni 250 ga koʻpaytirgandek nol qoʻshilgan javob.</p>"),
    q("What is 15 × 14?", ["150", "195", "200", "210", "225"], "210",
      "<p><strong>210.</strong> 14 × 10 + 14 × 5 = 140 + 70.</p><p><strong>225</strong> — 15 × 15; yaqin kvadratni olib, tuzatishni unutgan javob.</p>"),
    q("What is 0.25 × 84?", ["2.1", "19", "21", "24", "210"], "21",
      "<p><strong>21.</strong> 0.25 = 1/4, demak 84 ÷ 4 = 21.</p><p><strong>2.1</strong> va <strong>210</strong> — vergul joyini adashtirgan javoblar.</p>"),
    q("What is 101 × 46?", ["4,546", "4,600", "4,646", "4,686", "4,746"], "4,646",
      "<p><strong>4,646.</strong> 100 × 46 + 1 × 46 = 4,600 + 46.</p><p><strong>4,600</strong> — 101 ni 100 deb olib, tuzatishni qoʻshmagan javob.</p>"),
    q("What is the value of 17 × 36 + 17 × 64?", ["1,070", "1,170", "1,600", "1,700", "1,770"], "1,700",
      "<p><strong>1,700.</strong> Umumiy koʻpaytuvchi: 17 × (36 + 64) = 17 × 100.</p><p><strong>1,600</strong> — 16 × 100; 17 ni notoʻgʻri koʻchirgan javob. Ikkita koʻpaytmani alohida hisoblash shart emas.</p>"),
    q("What is 49 × 51?", ["2,401", "2,450", "2,499", "2,500", "2,501"], "2,499",
      "<p><strong>2,499.</strong> (50 − 1)(50 + 1) = 50<sup>2</sup> − 1 = 2,499.</p><p><strong>2,500</strong> — ikkalasini 50 deb olgan javob; <strong>2,401</strong> — 49<sup>2</sup>.</p>"),
    q("What is 0.2 × 0.15?", ["0.003", "0.03", "0.3", "0.35", "3"], "0.03",
      "<p><strong>0.03.</strong> 2 × 15 = 30; jami uchta oʻnli xona (0.2 da bitta, 0.15 da ikkita), demak 0.030.</p><p><strong>0.35</strong> — qoʻshib yuborilgan javob.</p>"),
    q("What is 4,500 ÷ 25?", ["18", "112.5", "180", "225", "1,800"], "180",
      "<p><strong>180.</strong> 25 ga boʻlish = 4 ga koʻpaytirib, 100 ga boʻlish: 4,500 × 4 = 18,000, ÷ 100 = 180.</p><p><strong>1,800</strong> — 100 ga boʻlishni unutgan javob.</p>"),
    q("What is 1.5 × 2.4?", ["0.36", "2.6", "3.6", "3.9", "36"], "3.6",
      "<p><strong>3.6.</strong> 1.5 × 2.4 = 2.4 + 1.2 (2.4 ning yarmi).</p><p><strong>3.9</strong> — qoʻshib yuborilgan javob (1.5 + 2.4).</p>"),
    q("What is the value of (68 × 15) ÷ 34?", ["15", "20", "30", "34", "60"], "30",
      "<p><strong>30.</strong> Avval qisqartiring: 68 ÷ 34 = 2, keyin 2 × 15 = 30.</p><p><strong>15</strong> — qisqartirgandan keyin 2 ga koʻpaytirishni unutgan javob.</p>"),
    q("The value of 0.49 × 812 is closest to which of the following?", ["40", "160", "400", "800", "4,000"], "400",
      "<p><strong>400.</strong> 0.49 ≈ 1/2, 812 ≈ 800; yarmi ≈ 400.</p><p><strong>4,000</strong> — vergulni adashtirgan taxmin. «Closest to» — taxmin qilishga ruxsat.</p>"),
    q("The value of 3,021 ÷ 49.8 is closest to which of the following?", ["6", "15", "60", "150", "600"], "60",
      "<p><strong>60.</strong> 3,000 ÷ 50 = 60.</p><p><strong>600</strong> va <strong>6</strong> — nollarni adashtirgan javoblar; variantlar 10 barobar farq qilsa, faqat tartibni toping.</p>"),
    q("A box holds 24 cans. A store orders 125 boxes. How many cans does the store order?", ["2,400", "2,500", "2,900", "3,000", "3,125"], "3,000",
      "<p><strong>3,000.</strong> 125 = 1,000 ÷ 8; 24 ÷ 8 = 3, 3 × 1,000 = 3,000.</p><p><strong>3,125</strong> — 125 × 25 hisoblangan, 24 emas.</p>"),
    q("A consultant bills $45 per hour and works 36 hours on a project. What is the total bill?", ["$1,440", "$1,580", "$1,620", "$1,660", "$1,800"], "$1,620",
      "<p><strong>$1,620.</strong> 36 × 45 = 36 × 40 + 36 × 5 = 1,440 + 180.</p><p><strong>$1,440</strong> — faqat 36 × 40, ikkinchi boʻlak unutilgan.</p>"),
    q("What is the value of 75 × 12 − 75 × 2?", ["150", "750", "825", "900", "1,050"], "750",
      "<p><strong>750.</strong> 75 × (12 − 2) = 75 × 10.</p><p><strong>900</strong> — faqat 75 × 12; ikkinchi koʻpaytma ayirilmagan.</p>"),
    q("What is 299 × 4?", ["1,192", "1,196", "1,200", "1,204", "1,296"], "1,196",
      "<p><strong>1,196.</strong> 300 × 4 − 1 × 4 = 1,200 − 4.</p><p><strong>1,200</strong> — yaxlitlab tuzatmagan javob; <strong>1,204</strong> — tuzatishni qoʻshgan, ayirmagan.</p>"),
    q("What is the value of (0.5)(0.4)(250)?", ["5", "20", "50", "100", "500"], "50",
      "<p><strong>50.</strong> 0.4 × 250 = 100, 0.5 × 100 = 50. Qulay juftdan boshlang.</p><p><strong>500</strong> — bitta oʻnli xona yoʻqolgan.</p>"),
    q("If 1/8 of a number is 14, what is 3/4 of the number?", ["42", "56", "84", "96", "112"], "84",
      "<p><strong>84.</strong> Son = 14 × 8 = 112; 3/4 × 112 = 84.</p><p><strong>112</strong> — sonning oʻzi; savol esa uning 3/4 qismini soʻradi.</p>"),
    q("A firm buys 48 laptops at $625 each. What is the total cost?", ["$28,800", "$29,375", "$30,000", "$30,625", "$31,250"], "$30,000",
      "<p><strong>$30,000.</strong> 625 = 5,000 ÷ 8; 48 ÷ 8 = 6, 6 × 5,000 = 30,000.</p><p><strong>$31,250</strong> — 50 × 625; laptoplar sonini yaxlitlab, tuzatmagan javob.</p>"),
    q("An office uses 18 packs of paper per week, and each pack costs $12.50. How much does the office spend on paper over 8 weeks?", ["$1,350", "$1,500", "$1,800", "$2,025", "$2,250"], "$1,800",
      "<p><strong>$1,800.</strong> Haftada 18 × 12.5 = 225; 8 haftada 225 × 8 = 1,800.</p><p><strong>$2,250</strong> — 10 hafta deb, <strong>$1,350</strong> — 6 hafta deb hisoblangan javoblar. Haftalar sonini qayta oʻqing.</p>"),
]

# =====================================================================
# GMAT-2 — integers, factors, multiples
# =====================================================================
Q2 = [
    q("Which of the following is a factor of 91?", ["3", "6", "7", "9", "11"], "7",
      "<p><strong>7.</strong> 91 = 7 × 13.</p><p>91 toq, shuning uchun 6 boʻlolmaydi; raqamlar yigʻindisi 10, demak 3 va 9 ham emas.</p>"),
    q("Which of the following is divisible by 9?", ["2,345", "3,474", "4,513", "5,128", "6,203"], "3,474",
      "<p><strong>3,474.</strong> 3 + 4 + 7 + 4 = 18, u 9 ga boʻlinadi.</p><p>Qolganlarining raqamlari yigʻindisi 14, 13, 16 va 11 — hech biri 9 ga boʻlinmaydi.</p>"),
    q("How many positive factors does 18 have?", ["3", "4", "5", "6", "8"], "6",
      "<p><strong>6.</strong> 1 × 18, 2 × 9, 3 × 6 — juftlab: 1, 2, 3, 6, 9, 18.</p><p><strong>4</strong> — 1 va 18 ni unutgan javob.</p>"),
    q("Which of the following is a multiple of 6?", ["124", "146", "162", "175", "196"], "162",
      "<p><strong>162.</strong> Juft (2 ga) va raqamlar yigʻindisi 9 (3 ga) — demak 6 ga boʻlinadi.</p><p><strong>124</strong>, <strong>146</strong>, <strong>196</strong> juft, lekin 3 ga boʻlinmaydi.</p>"),
    q("How many positive integers less than 50 are multiples of 3?", ["15", "16", "17", "18", "50"], "16",
      "<p><strong>16.</strong> 50 ÷ 3 = 16.6…; eng katta karrali 3 × 16 = 48.</p><p><strong>17</strong> — yuqoriga yaxlitlangan; 3 × 17 = 51 > 50.</p>"),
    q("How many multiples of 4 are there from 12 to 60, inclusive?", ["11", "12", "13", "14", "15"], "13",
      "<p><strong>13.</strong> (60 − 12) ÷ 4 + 1 = 12 + 1.</p><p><strong>12</strong> — «+1» unutilgan: «inclusive» ikkala chetni ham sanashni bildiradi.</p>"),
    q("What is the smallest positive integer that is divisible by each of the integers 2, 3, 4 and 5?", ["30", "60", "90", "120", "240"], "60",
      "<p><strong>60.</strong> EKUK: 2<sup>2</sup> × 3 × 5 = 60.</p><p><strong>120</strong> — 2 × 3 × 4 × 5; 4 ichida 2 bor, uni ikki marta hisobga olish shart emas.</p>"),
    q("If <i>n</i> is a positive integer that is divisible by both 10 and 15, which of the following must be a factor of <i>n</i>?", ["20", "25", "30", "45", "150"], "30",
      "<p><strong>30.</strong> Eng kichik mos son — EKUK(10, 15) = 30. <i>n</i> = 30 da 20, 25, 45, 150 boʻluvchi emas.</p><p><strong>150</strong> — 10 × 15; umumiy karrali, lekin «must» emas.</p>"),
    q("What is the sum of all the positive factors of 12?", ["16", "22", "24", "28", "36"], "28",
      "<p><strong>28.</strong> 1 + 2 + 3 + 4 + 6 + 12 = 28.</p><p><strong>16</strong> — 12 ning oʻzini qoʻshmagan javob.</p>"),
    q("How many of the positive factors of 100 are even?", ["3", "4", "5", "6", "9"], "6",
      "<p><strong>6.</strong> Boʻluvchilar: 1, 2, 4, 5, 10, 20, 25, 50, 100; juftlari 2, 4, 10, 20, 50, 100.</p><p><strong>9</strong> — barcha boʻluvchilar soni; savol faqat juftlarini soʻradi.</p>"),
    q("Which of the following has an odd number of positive factors?", ["24", "32", "48", "64", "72"], "64",
      "<p><strong>64.</strong> Boʻluvchilari soni toq boʻlgan son — toʻliq kvadrat, 64 = 8 × 8.</p><p>Qolganlari toʻliq kvadrat emas, ularning boʻluvchilari juft-juft keladi.</p>"),
    q("If the four-digit number 73<i>k</i>2 is divisible by 4, where <i>k</i> is a digit, which of the following could be the value of <i>k</i>?", ["2", "4", "5", "6", "8"], "5",
      "<p><strong>5.</strong> 4 ga boʻlinish oxirgi ikki raqamga bogʻliq: <i>k</i>2. 52 = 4 × 13 ✓.</p><p>22, 42, 62, 82 — 4 ga boʻlinmaydi. Juft raqam yetarli deb oʻylash — tuzoq.</p>"),
    q("A gym sells passes in packs of 8. A school needs at least 100 passes. What is the least number of packs the school must buy?", ["11", "12", "13", "14", "15"], "13",
      "<p><strong>13.</strong> 12 paket = 96 — yetmaydi; 13 paket = 104.</p><p><strong>12</strong> — pastga yaxlitlangan. «At least» — yetarli boʻlishi kerak, shuning uchun bu safar yuqoriga.</p>"),
    q("A warehouse has 252 items to pack into boxes, each box holding the same number of items with none left over. If each box must hold from 10 to 20 items, inclusive, how many different box sizes are possible?", ["1", "2", "3", "4", "5"], "3",
      "<p><strong>3.</strong> 252 = 2<sup>2</sup> × 3<sup>2</sup> × 7. 10 dan 20 gacha boʻluvchilar: 12, 14, 18.</p><p><strong>2</strong> — 18 ni unutgan javob; boʻluvchilarni juftlab tekshiring.</p>"),
    q("How many positive integers less than 60 are multiples of 6?", ["8", "9", "10", "11", "54"], "9",
      "<p><strong>9.</strong> 6, 12, …, 54 — 54 = 6 × 9.</p><p><strong>10</strong> — 60 ni ham sanagan javob; «less than 60» uni chiqarib tashlaydi.</p>"),
    q("If <i>n</i> is a positive integer that is divisible by both 8 and 12, which of the following must be a factor of <i>n</i>?", ["16", "24", "32", "48", "96"], "24",
      "<p><strong>24.</strong> EKUK(8, 12) = 24 — eng kichik mos <i>n</i>; u 16, 32, 48, 96 ga boʻlinmaydi.</p><p><strong>96</strong> — 8 × 12, umumiy koʻpaytuvchi 4 ikki marta kirgan.</p>"),
    q("How many integers from 1 to 100, inclusive, are divisible by neither 2 nor 5?", ["30", "40", "45", "50", "60"], "40",
      "<p><strong>40.</strong> 2 ga: 50 ta, 5 ga: 20 ta, ikkalasiga (10 ga): 10 ta. 2 yoki 5 ga: 50 + 20 − 10 = 60. Hech biriga: 100 − 60 = 40.</p><p><strong>30</strong> — ikki marta sanalgan 10 ta qaytarib qoʻshilmagan.</p>"),
    q("What is the greatest two-digit integer that is a multiple of both 4 and 6?", ["84", "90", "92", "96", "98"], "96",
      "<p><strong>96.</strong> 4 va 6 ning umumiy karralilari — 12 ning karralilari; eng kattasi 12 × 8 = 96.</p><p><strong>92</strong> 4 ga boʻlinadi, 6 ga emas; <strong>90</strong> — 6 ga boʻlinadi, 4 ga emas.</p>"),
    q("A school has 84 students to divide into groups of equal size, with at least 2 and at most 12 students in each group. How many different group sizes are possible?", ["4", "5", "6", "7", "8"], "6",
      "<p><strong>6.</strong> 84 ning 2 dan 12 gacha boʻluvchilari: 2, 3, 4, 6, 7, 12.</p><p><strong>5</strong> — 12 ni chiqarib tashlagan javob; «at most 12» 12 ni ham qoʻshadi.</p>"),
    q("Pencils are sold in boxes of 12 and erasers in packs of 8. A teacher wants to buy exactly the same number of pencils and erasers. What is the smallest number of pencils she can buy?", ["4", "20", "24", "48", "96"], "24",
      "<p><strong>24.</strong> Umumiy karrali — EKUK(12, 8) = 24 (2 quti qalam, 3 paket oʻchirgʻich).</p><p><strong>96</strong> — 12 × 8; umumiy karrali, lekin eng kichigi emas.</p>"),
]

# =====================================================================
# GMAT-3 — primes, prime factorization, GCD and LCM
# =====================================================================
Q3 = [
    q("Which of the following is a prime number?", ["21", "27", "31", "33", "39"], "31",
      "<p><strong>31.</strong> Uning boʻluvchilari faqat 1 va 31.</p><p>21 = 3 × 7, 27 = 3 × 9, 33 = 3 × 11, 39 = 3 × 13 — toq boʻlsa ham tub emas.</p>"),
    q("How many prime numbers are less than 20?", ["7", "8", "9", "10", "11"], "8",
      "<p><strong>8.</strong> 2, 3, 5, 7, 11, 13, 17, 19.</p><p><strong>9</strong> — 1 ni tub deb sanagan javob.</p>"),
    q("What is the prime factorization of 84?", ["2 × 3 × 7", "2<sup>2</sup> × 3 × 7", "2<sup>2</sup> × 21", "2 × 42", "4 × 3 × 7"], "2<sup>2</sup> × 3 × 7",
      "<p><strong>2<sup>2</sup> × 3 × 7.</strong> 84 = 4 × 21 = 2 × 2 × 3 × 7.</p><p><strong>4 × 3 × 7</strong> — qiymati toʻgʻri, lekin 4 tub emas; <strong>2<sup>2</sup> × 21</strong> — 21 tub emas.</p>"),
    q("What is the greatest common divisor of 36 and 48?", ["4", "6", "12", "24", "144"], "12",
      "<p><strong>12.</strong> 36 = 2<sup>2</sup> × 3<sup>2</sup>, 48 = 2<sup>4</sup> × 3; umumiy: 2<sup>2</sup> × 3.</p><p><strong>144</strong> — EKUK; EKUB kichik sondan katta boʻlolmaydi.</p>"),
    q("What is the least common multiple of 9 and 12?", ["3", "18", "36", "72", "108"], "36",
      "<p><strong>36.</strong> 9 = 3<sup>2</sup>, 12 = 2<sup>2</sup> × 3; EKUK = 2<sup>2</sup> × 3<sup>2</sup>.</p><p><strong>108</strong> — 9 × 12; umumiy 3 ikki marta kirgan. <strong>3</strong> — EKUB.</p>"),
    q("How many positive factors does 200 have?", ["6", "8", "10", "12", "16"], "12",
      "<p><strong>12.</strong> 200 = 2<sup>3</sup> × 5<sup>2</sup>; (3 + 1)(2 + 1) = 12.</p><p><strong>6</strong> — darajalarga 1 qoʻshmasdan koʻpaytirgan javob (3 × 2).</p>"),
    q("How many distinct prime factors does 210 have?", ["2", "3", "4", "5", "6"], "4",
      "<p><strong>4.</strong> 210 = 2 × 3 × 5 × 7.</p><p><strong>5</strong> — 1 ni ham qoʻshgan javob; 1 tub emas.</p>"),
    q("What is the sum of the distinct prime factors of 60?", ["5", "10", "12", "15", "60"], "10",
      "<p><strong>10.</strong> 60 = 2<sup>2</sup> × 3 × 5; turli tub boʻluvchilar 2, 3, 5 — yigʻindisi 10.</p><p><strong>12</strong> — 2 ni ikki marta qoʻshgan javob (2 + 2 + 3 + 5); «distinct» — har biri bir marta.</p>"),
    q("The greatest common divisor of 24 and a positive integer <i>b</i> is 6, and their least common multiple is 120. What is <i>b</i>?", ["12", "20", "30", "36", "60"], "30",
      "<p><strong>30.</strong> EKUB × EKUK = ikki sonning koʻpaytmasi: 6 × 120 = 24 × <i>b</i>, <i>b</i> = 720 ÷ 24 = 30.</p><p>Tekshiruv: EKUB(24, 30) = 6, EKUK = 120 ✓.</p>"),
    q("What is the greatest prime factor of 255?", ["3", "5", "15", "17", "51"], "17",
      "<p><strong>17.</strong> 255 = 3 × 5 × 17.</p><p><strong>51</strong> — eng katta boʻluvchi, lekin 51 = 3 × 17, tub emas.</p>"),
    q("Two warning lights blink at the same moment. One blinks every 15 seconds and the other every 20 seconds. After how many seconds will they next blink at the same moment?", ["35", "45", "60", "150", "300"], "60",
      "<p><strong>60.</strong> «Yana bir vaqtda» — EKUK(15, 20) = 60.</p><p><strong>300</strong> — 15 × 20; <strong>35</strong> — qoʻshilgan.</p>"),
    q("Two ribbons, 42 centimeters and 70 centimeters long, are cut into pieces that are all the same length, with nothing left over. What is the greatest possible length of each piece, in centimeters?", ["7", "14", "21", "28", "35"], "14",
      "<p><strong>14.</strong> «Eng katta teng boʻlak» — EKUB(42, 70) = 14.</p><p><strong>7</strong> — umumiy boʻluvchi, lekin eng kattasi emas; <strong>21</strong> faqat 42 ni boʻladi.</p>"),
    q("What is the smallest integer greater than 1 that leaves a remainder of 1 when divided by 2, by 3 and by 4?", ["7", "11", "13", "25", "49"], "13",
      "<p><strong>13.</strong> Son − 1 ga 2, 3, 4 hammasi boʻlinishi kerak: EKUK = 12, son = 13.</p><p><strong>25</strong> ham shartni bajaradi (24 + 1), lekin eng kichigi emas.</p>"),
    q("If <i>p</i> is a prime number greater than 2, which of the following must be even?", ["<i>p</i>", "<i>p</i> + 1", "<i>p</i> + 2", "2<i>p</i> + 1", "<i>p</i><sup>2</sup>"], "<i>p</i> + 1",
      "<p><strong>p + 1.</strong> 2 dan katta tub son toq, toq + 1 — juft.</p><p><strong>p + 2</strong> va <strong>p<sup>2</sup></strong> — toq. Faqat 2 juft tub son, u shart bilan chiqarib tashlangan.</p>"),
    q("What is the sum of the prime numbers between 1 and 10?", ["15", "16", "17", "18", "25"], "17",
      "<p><strong>17.</strong> 2 + 3 + 5 + 7 = 17.</p><p><strong>18</strong> — 1 ni qoʻshgan javob; <strong>15</strong> — 2 ni tashlab ketgan javob. Ikkalasi ham eng koʻp uchraydigan tub son xatolari.</p>"),
    q("What is the least common multiple of 18 and 24?", ["6", "36", "72", "144", "432"], "72",
      "<p><strong>72.</strong> 18 = 2 × 3<sup>2</sup>, 24 = 2<sup>3</sup> × 3; EKUK = 2<sup>3</sup> × 3<sup>2</sup> = 72.</p><p><strong>432</strong> — 18 × 24; umumiy 6 ikki marta kirgan.</p>"),
    q("If <i>n</i> = 2<sup>3</sup> × 3<sup>2</sup> × 5, how many positive factors of <i>n</i> are odd?", ["4", "6", "8", "12", "24"], "6",
      "<p><strong>6.</strong> Toq boʻluvchida 2 qatnashmaydi: faqat 3<sup>2</sup> × 5 dan — (2 + 1)(1 + 1) = 6.</p><p><strong>24</strong> — barcha boʻluvchilar soni.</p>"),
    q("The greatest common divisor of two positive integers is 8 and their least common multiple is 96. If one of the integers is 32, what is the other?", ["12", "16", "24", "48", "64"], "24",
      "<p><strong>24.</strong> 8 × 96 = 32 × <i>x</i>, <i>x</i> = 768 ÷ 32 = 24. Tekshiruv: EKUB(32, 24) = 8, EKUK = 96 ✓.</p><p><strong>12</strong> — 96 ÷ 8, ikkinchi formulani adashtirgan javob.</p>"),
    q("In a factory, machine A is serviced every 6 days, machine B every 8 days and machine C every 12 days. All three were serviced today. In how many days will all three next be serviced on the same day?", ["12", "24", "26", "48", "576"], "24",
      "<p><strong>24.</strong> EKUK(6, 8, 12) = 2<sup>3</sup> × 3 = 24.</p><p><strong>576</strong> — 6 × 8 × 12; <strong>26</strong> — qoʻshilgan.</p>"),
    q("A manager has 48 pens and 72 notebooks to put into identical gift bags, using all of them. What is the greatest number of gift bags she can make?", ["6", "8", "12", "24", "144"], "24",
      "<p><strong>24.</strong> EKUB(48, 72) = 24 — har sumkada 2 ta ruchka va 3 ta daftar.</p><p><strong>144</strong> — EKUK; sumkalar soni buyumlardan koʻp boʻlolmaydi.</p>"),
]

# =====================================================================
# GMAT-4 — odd/even, positive/negative
# =====================================================================
Q4 = [
    q("Which of the following is even?", ["7 × 9", "5 + 8", "3 × 12", "11 + 6", "13 − 2"], "3 × 12",
      "<p><strong>3 × 12 = 36.</strong> Koʻpaytmada bitta juft son boʻlsa, natija juft.</p><p>Qolganlari: 63, 13, 17, 11 — toq. Juft + toq har doim toq.</p>"),
    q("If <i>x</i> &lt; 0 and <i>y</i> &gt; 0, which of the following must be negative?", ["<i>x</i> + <i>y</i>", "<i>xy</i>", "<i>y</i> − <i>x</i>", "<i>x</i><sup>2</sup>", "−<i>x</i>"], "<i>xy</i>",
      "<p><strong>xy.</strong> Manfiy × musbat = manfiy.</p><p><strong>x + y</strong> — <i>x</i> va <i>y</i> kattaligiga bogʻliq: −1 + 5 musbat, −5 + 1 manfiy.</p>"),
    q("Which of the following is NOT an even integer?", ["−4", "0", "2", "7", "12"], "7",
      "<p><strong>7.</strong></p><p><strong>0</strong> — juft son: 0 = 2 × 0. «0 na juft, na toq» — tuzoq.</p>"),
    q("The product of six negative numbers and three positive numbers is", ["always negative", "always positive", "always zero", "positive or negative, depending on the numbers", "undefined"], "always positive",
      "<p><strong>Always positive.</strong> Manfiy koʻpaytuvchilar soni juft (6), demak koʻpaytma musbat.</p><p>Musbat sonlar ishorani oʻzgartirmaydi — faqat manfiylar sanaladi.</p>"),
    q("If <i>n</i> is an odd integer, which of the following must be even?", ["<i>n</i> + 2", "2<i>n</i> + 1", "<i>n</i><sup>2</sup>", "3<i>n</i>", "<i>n</i> + 1"], "<i>n</i> + 1",
      "<p><strong>n + 1.</strong> Toq + toq (1) = juft.</p><p><strong>n<sup>2</sup></strong> va <strong>3n</strong> — toq × toq = toq.</p>"),
    q("If <i>x</i> and <i>y</i> are integers and <i>x</i> + <i>y</i> is odd, which of the following must be true?", ["<i>x</i> and <i>y</i> are both odd.", "<i>x</i> and <i>y</i> are both even.", "<i>xy</i> is even.", "<i>x</i> − <i>y</i> is even.", "<i>x</i> is odd."], "<i>xy</i> is even.",
      "<p><strong>xy is even.</strong> Yigʻindi toq — biri juft, biri toq; koʻpaytmada bitta juft bor.</p><p><strong>x is odd</strong> — mumkin, lekin shart emas: toq son <i>y</i> boʻlishi ham mumkin.</p>"),
    q("If <i>a</i> &lt; 0 &lt; <i>b</i>, which of the following must be positive?", ["<i>a</i> + <i>b</i>", "<i>ab</i>", "<i>a</i>/<i>b</i>", "<i>b</i> − <i>a</i>", "<i>a</i> − <i>b</i>"], "<i>b</i> − <i>a</i>",
      "<p><strong>b − a.</strong> Musbatdan manfiyni ayirish = musbat + musbat.</p><p><strong>a + b</strong> — kattaliklarga bogʻliq; <strong>ab</strong> va <strong>a/b</strong> — manfiy.</p>"),
    q("If <i>m</i> &lt; 0, which of the following has the greatest value?", ["<i>m</i>", "2<i>m</i>", "<i>m</i><sup>2</sup>", "−<i>m</i><sup>2</sup>", "<i>m</i><sup>3</sup>"], "<i>m</i><sup>2</sup>",
      "<p><strong>m<sup>2</sup>.</strong> Faqat u musbat: manfiy sonning kvadrati musbat.</p><p><strong>−m<sup>2</sup></strong> — kvadratning minus ishorasi, u manfiy; <strong>m<sup>3</sup></strong> — uchta manfiy koʻpaytuvchi, manfiy.</p>"),
    q("How many of the integers from 1 to 25, inclusive, are odd?", ["11", "12", "13", "14", "25"], "13",
      "<p><strong>13.</strong> 1, 3, …, 25 — 1 dan boshlanib toq son bilan tugaydi, shuning uchun toqlar bittaga koʻp: 13 toq, 12 juft.</p><p><strong>12</strong> — 25 ni teng ikkiga boʻlib, yaxlitlagan javob.</p>"),
    q("If <i>n</i> is an integer, which of the following must be even?", ["<i>n</i> + 2", "2<i>n</i> − 1", "<i>n</i><sup>2</sup>", "3<i>n</i> + 1", "<i>n</i>(<i>n</i> + 1)"], "<i>n</i>(<i>n</i> + 1)",
      "<p><strong>n(n + 1).</strong> Ikki ketma-ket butun sondan biri har doim juft.</p><p><strong>n<sup>2</sup></strong> — <i>n</i> toq boʻlsa toq; <strong>3n + 1</strong> — <i>n</i> = 2 da 7.</p>"),
    q("A shop recorded daily profits of −$40, $25, −$15 and $60 over four days. What was its total profit for the four days?", ["−$30", "−$10", "$10", "$30", "$140"], "$30",
      "<p><strong>$30.</strong> 25 + 60 = 85; −40 − 15 = −55; 85 − 55 = 30.</p><p><strong>$140</strong> — barcha sonlarni ishorasiz qoʻshgan javob.</p>"),
    q("At 6 a.m. the temperature was −8°C. It rose by 15°C by noon and then fell by 4°C by evening. What was the evening temperature?", ["−27°C", "−11°C", "−3°C", "3°C", "11°C"], "3°C",
      "<p><strong>3°C.</strong> −8 + 15 = 7; 7 − 4 = 3.</p><p><strong>−3°C</strong> — natijaning ishorasini adashtirgan javob: −8 dan 15 daraja yuqori — 7, keyin 7 − 4 = 3.</p>"),
    q("A company has an odd number of employees in each of its 3 offices. The total number of employees in the 3 offices is", ["always even", "always odd", "even or odd, depending on the offices", "always a multiple of 3", "always greater than 9"], "always odd",
      "<p><strong>Always odd.</strong> Toq + toq = juft, juft + toq = toq.</p><p><strong>Always even</strong> — ikkita toq qoʻshilganini oʻylab, uchinchisini unutgan javob.</p>"),
    q("An account had a balance of −$250. The owner deposited $400 and then withdrew $175. What is the new balance?", ["−$175", "−$25", "$25", "$175", "$825"], "−$25",
      "<p><strong>−$25.</strong> −250 + 400 = 150; 150 − 175 = −25.</p><p><strong>$25</strong> — ishorani yoʻqotgan javob.</p>"),
    q("For how many integers <i>n</i> from −2 to 2, inclusive, is <i>n</i><sup>2</sup> &gt; <i>n</i>?", ["1", "2", "3", "4", "5"], "3",
      "<p><strong>3.</strong> −2: 4 > −2 ✓; −1: 1 > −1 ✓; 0: 0 > 0 ✗; 1: 1 > 1 ✗; 2: 4 > 2 ✓.</p><p><strong>2</strong> yoki <strong>4</strong> — 0 va 1 ni shoshilib tekshirgan javoblar.</p>"),
    q("If <i>xy</i> &lt; 0 and <i>x</i> &gt; 0, which of the following must be true?", ["<i>y</i> &gt; 0", "<i>y</i> &lt; 0", "<i>xy</i><sup>2</sup> &lt; 0", "<i>x</i> + <i>y</i> &gt; 0", "<i>x</i> − <i>y</i> &lt; 0"], "<i>y</i> &lt; 0",
      "<p><strong>y < 0.</strong> Koʻpaytma manfiy va <i>x</i> musbat — demak <i>y</i> manfiy.</p><p><strong>x + y > 0</strong> — kattaliklarga bogʻliq; <strong>xy<sup>2</sup></strong> musbat, chunki <i>y</i><sup>2</sup> > 0.</p>"),
    q("If <i>a</i> is even and <i>b</i> is odd, which of the following must be odd?", ["<i>ab</i>", "<i>a</i> + <i>b</i>", "<i>a</i> + 2<i>b</i>", "<i>b</i> − 1", "3<i>a</i>"], "<i>a</i> + <i>b</i>",
      "<p><strong>a + b.</strong> Juft + toq = toq.</p><p><strong>a + 2b</strong> — 2<i>b</i> juft, juft + juft = juft.</p>"),
    q("If <i>abc</i> &lt; 0 and <i>ab</i> &gt; 0, which of the following must be true?", ["<i>a</i> &lt; 0", "<i>b</i> &lt; 0", "<i>c</i> &lt; 0", "<i>a</i> + <i>b</i> &gt; 0", "<i>bc</i> &gt; 0"], "<i>c</i> &lt; 0",
      "<p><strong>c < 0.</strong> <i>abc</i> = (<i>ab</i>) × <i>c</i>; <i>ab</i> musbat, koʻpaytma manfiy — <i>c</i> manfiy.</p><p><strong>a + b > 0</strong> — <i>a</i> va <i>b</i> ikkalasi manfiy boʻlishi ham mumkin.</p>"),
    q("In a game, a player gains 3 points for each win and loses 2 points for each loss. A player played 10 games, won 4 and lost the rest. What was the player's final score?", ["−8", "−4", "0", "4", "12"], "0",
      "<p><strong>0.</strong> 4 × 3 = 12; magʻlubiyatlar 10 − 4 = 6, 6 × (−2) = −12; 12 − 12 = 0.</p><p><strong>4</strong> — magʻlubiyatlarni 4 ta deb olgan javob (12 − 8).</p>"),
    q("Each hour, machine A produces an even number of units and machine B produces an odd number of units. Over 5 hours, the total number of units produced by the two machines together is", ["always even", "always odd", "even or odd, depending on the numbers", "always a multiple of 5", "always a multiple of 10"], "always odd",
      "<p><strong>Always odd.</strong> A: beshta juft — juft. B: beshta toq — toq (toq marta toq). Juft + toq = toq.</p><p><strong>Always even</strong> — B ning toq soni toq marta qoʻshilganini hisobga olmagan javob.</p>"),
]

# =====================================================================
# GMAT-5 — percentages and percent change
# =====================================================================
Q5 = [
    q("What is 20% of 350?", ["35", "70", "175", "280", "700"], "70",
      "<p><strong>70.</strong> 10% = 35, 20% = 70.</p><p><strong>280</strong> — 350 dan 20% ni ayirgan javob (80%).</p>"),
    q("30 is what percent of 120?", ["4%", "25%", "30%", "40%", "400%"], "25%",
      "<p><strong>25%.</strong> 30 ÷ 120 = 0.25.</p><p><strong>400%</strong> — teskari boʻlingan (120 ÷ 30).</p>"),
    q("18 is 15% of what number?", ["2.7", "27", "108", "120", "270"], "120",
      "<p><strong>120.</strong> 18 ÷ 0.15 = 120.</p><p><strong>2.7</strong> — boʻlish oʻrniga koʻpaytirilgan; butun qismdan katta boʻlishi kerak edi.</p>"),
    q("What is 120% of 85?", ["17", "68", "97", "102", "105"], "102",
      "<p><strong>102.</strong> 1.2 × 85 = 85 + 17.</p><p><strong>17</strong> — faqat 20% ni hisoblagan javob.</p>"),
    q("The price of an item increased from $60 to $75. By what percent did the price increase?", ["15%", "20%", "25%", "75%", "125%"], "25%",
      "<p><strong>25%.</strong> 15 ÷ 60 = 0.25.</p><p><strong>20%</strong> — oʻzgarish yangi narxga (75) boʻlingan.</p>"),
    q("The price of an item decreased from $75 to $60. By what percent did the price decrease?", ["15%", "20%", "25%", "80%", "125%"], "20%",
      "<p><strong>20%.</strong> 15 ÷ 75 = 0.2.</p><p><strong>25%</strong> — oldingi savoldagi javob: oʻzgarish bir xil, lekin baza endi 75.</p>"),
    q("After a 20% discount, a jacket costs $48. What was its price before the discount?", ["$38.40", "$57.60", "$60.00", "$64.00", "$68.00"], "$60.00",
      "<p><strong>$60.</strong> 0.8 × narx = 48, narx = 48 ÷ 0.8 = 60.</p><p><strong>$57.60</strong> — 48 ga 20% qoʻshilgan; chegirma eski narxdan olingan edi.</p>"),
    q("A price is increased by 10% and the new price is then increased by 10%. By what percent has the original price increased in total?", ["11%", "20%", "21%", "22%", "121%"], "21%",
      "<p><strong>21%.</strong> 1.1 × 1.1 = 1.21.</p><p><strong>20%</strong> — foizlar qoʻshilgan; ikkinchi 10% kattaroq bazadan olinadi.</p>"),
    q("What is 40% of 60% of 500?", ["100", "120", "200", "300", "500"], "120",
      "<p><strong>120.</strong> 0.6 × 500 = 300; 0.4 × 300 = 120.</p><p><strong>500</strong> — 40% + 60% = 100% deb qoʻshgan javob.</p>"),
    q("An interest rate rose from 4% to 5%. By what percent did the interest rate increase?", ["1%", "5%", "20%", "25%", "125%"], "25%",
      "<p><strong>25%.</strong> Oʻzgarish 1 punkt; 1 ÷ 4 = 0.25.</p><p><strong>1%</strong> — foiz punktini foiz oʻzgarishi bilan adashtirgan javob.</p>"),
    q("A company's annual revenue rose from $3.2 million to $4.0 million. By what percent did revenue increase?", ["0.8%", "20%", "25%", "80%", "125%"], "25%",
      "<p><strong>25%.</strong> 0.8 ÷ 3.2 = 0.25.</p><p><strong>20%</strong> — oʻzgarish yangi qiymatga (4.0) boʻlingan.</p>"),
    q("Of a company's 250 employees, 40% work remotely. Of the employees who work remotely, 30% live outside the city. How many employees work remotely and live outside the city?", ["30", "75", "100", "175", "250"], "30",
      "<p><strong>30.</strong> Masofadan: 0.4 × 250 = 100; ularning 30% i: 30.</p><p><strong>75</strong> — 30% barcha xodimlardan olingan; «of the employees who work remotely» bazani oʻzgartiradi.</p>"),
    q("A store buys a lamp for $40, marks the price up by 50%, and then sells the lamp at a 20% discount from the marked price. What is the selling price?", ["$44", "$48", "$52", "$60", "$72"], "$48",
      "<p><strong>$48.</strong> 40 × 1.5 = 60; 60 × 0.8 = 48.</p><p><strong>$52</strong> — +50% va −20% ni qoʻshib +30% qilgan javob.</p>"),
    q("A town's population of 80,000 grows by 5% each year. What will the population be after 2 years?", ["84,000", "88,000", "88,200", "88,400", "96,000"], "88,200",
      "<p><strong>88,200.</strong> 80,000 × 1.05 = 84,000; 84,000 × 1.05 = 88,200.</p><p><strong>88,000</strong> — ikki yilga 10% qoʻshilgan; ikkinchi yilning 5% i 84,000 dan olinadi.</p>"),
    q("A price is decreased by 25% and the new price is then increased by 25%. The final price is what percent of the original price?", ["93.75%", "95%", "100%", "106.25%", "125%"], "93.75%",
      "<p><strong>93.75%.</strong> 0.75 × 1.25 = 0.9375.</p><p><strong>100%</strong> — −25% va +25% bir-birini yoʻqotadi deb oʻylagan javob.</p>"),
    q("A sales tax rate increased from 8% to 10%. By how many percentage points did the rate increase?", ["2", "10", "18", "20", "25"], "2",
      "<p><strong>2.</strong> Foiz punktlari — oddiy ayirma: 10 − 8.</p><p><strong>25</strong> — foiz oʻzgarishi (2 ÷ 8); savol esa <i>percentage points</i> ni soʻradi.</p>"),
    q("If <i>x</i> is 20% greater than <i>y</i>, then <i>y</i> is what percent of <i>x</i>?", ["75%", "80%", "83⅓%", "120%", "125%"], "83⅓%",
      "<p><strong>83⅓%.</strong> <i>x</i> = 1.2<i>y</i>, demak <i>y</i> = <i>x</i> ÷ 1.2 = (5/6)<i>x</i>.</p><p><strong>80%</strong> — «20% koʻp boʻlsa, 20% kam» deb oʻylagan javob. Baza oʻzgaradi.</p>"),
    q("A's salary is 25% more than B's salary, and B's salary is 20% less than C's salary. A's salary is what percent of C's salary?", ["95%", "100%", "105%", "120%", "145%"], "100%",
      "<p><strong>100%.</strong> B = 0.8C, A = 1.25 × 0.8C = C.</p><p><strong>105%</strong> — foizlarni qoʻshgan javob (+25% − 20%).</p>"),
    q("A consultant raised her hourly fee from $80 to $92. By what percent did her fee increase?", ["12%", "13%", "15%", "87%", "115%"], "15%",
      "<p><strong>15%.</strong> 12 ÷ 80 = 0.15.</p><p><strong>13%</strong> — 12 ni yangi narxga (92) boʻlgan javob; <strong>12%</strong> — dollar oʻzgarishini foiz deb olgan.</p>"),
    q("A store bought 200 units of a product at $15 each and sold all of them at $18 each. The store's profit was what percent of its cost?", ["3%", "16⅔%", "20%", "30%", "120%"], "20%",
      "<p><strong>20%.</strong> Xarajat 200 × 15 = 3,000; foyda 200 × 3 = 600; 600 ÷ 3,000 = 20%.</p><p><strong>16⅔%</strong> — foyda tushumga (3,600) boʻlingan; savol xarajatga nisbatan soʻradi.</p>"),
]

PRACTICES = [
    {
        "title": "GMAT-1 Practice: The Quant Section and Arithmetic Without a Calculator",
        "description": "20 ta GMAT uslubidagi savol — kalkulyatorsiz koʻpaytirish, yaxlitlash va tuzatish, taxmin qilish.",
        "tutorial": "GMAT-1:", "subject": "GMAT", "level": "easy", "questions": Q1,
    },
    {
        "title": "GMAT-2 Practice: Number Properties — Integers, Factors and Multiples",
        "description": "20 ta GMAT uslubidagi savol — boʻluvchilar, karralilar, boʻlinish belgilari va «must be».",
        "tutorial": "GMAT-2:", "subject": "GMAT", "level": "medium", "questions": Q2,
    },
    {
        "title": "GMAT-3 Practice: Primes, Prime Factorization, GCD and LCM",
        "description": "20 ta GMAT uslubidagi savol — tub sonlar, boʻluvchilar soni, EKUB va EKUK masalalari.",
        "tutorial": "GMAT-3:", "subject": "GMAT", "level": "medium", "questions": Q3,
    },
    {
        "title": "GMAT-4 Practice: Odd and Even, Positive and Negative",
        "description": "20 ta GMAT uslubidagi savol — juft-toq, ishoralar qoidasi va «must be true».",
        "tutorial": "GMAT-4:", "subject": "GMAT", "level": "medium", "questions": Q4,
    },
    {
        "title": "GMAT-5 Practice: Percentages and Percent Change",
        "description": "20 ta GMAT uslubidagi savol — foiz oʻzgarishi, ketma-ket foizlar, teskari foiz va foiz punktlari.",
        "tutorial": "GMAT-5:", "subject": "GMAT", "level": "medium", "questions": Q5,
    },
]
