# -*- coding: utf-8 -*-
"""Prime GMAT mashqlar — GMAT-6 … GMAT-10.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan. Savollar INGLIZCHA (imtihon
tili), tushuntirishlar OʻZBEKCHA. Har savolda BESHTA variant, raqamli variantlar oʻsish
tartibida. Kalkulyatorsiz yechiladigan arifmetika.

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context · 15–16 trap-spotting ·
      17–18 harder · 19–20 word problems (har doim ikkita).

Import:
    python manage.py import_practices practice/management/commands/_practice_pg_06_10.py \\
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


DAYS5 = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# =====================================================================
# GMAT-6 — fractions and decimals
# =====================================================================
Q6 = [
    q("What is 3/8 expressed as a decimal?", ["0.038", "0.375", "0.38", "0.6", "2.67"], "0.375",
      "<p><strong>0.375.</strong> 1/8 = 0.125, uchtasi 0.375.</p><p><strong>0.38</strong> — 3 va 8 ni yonma-yon yozgan javob; <strong>2.67</strong> — teskari boʻlingan (8 ÷ 3).</p>"),
    q("What is 0.125 × 48?", ["0.6", "4", "6", "8", "60"], "6",
      "<p><strong>6.</strong> 0.125 = 1/8, demak 48 ÷ 8 = 6.</p><p><strong>0.6</strong> va <strong>60</strong> — vergulni adashtirgan javoblar.</p>"),
    q("What is 2/3 + 3/4?", ["5/12", "5/7", "1", "17/12", "2"], "17/12",
      "<p><strong>17/12.</strong> Umumiy maxraj 12: 8/12 + 9/12 = 17/12.</p><p><strong>5/7</strong> — suratlar va maxrajlarni alohida qoʻshgan javob.</p>"),
    q("What is 0.36 ÷ 0.12?", ["0.03", "0.3", "3", "30", "300"], "3",
      "<p><strong>3.</strong> Ikkalasini 100 ga koʻpaytiramiz: 36 ÷ 12 = 3.</p><p><strong>0.3</strong> — vergulni faqat bitta songa surgan javob.</p>"),
    q("Which of the following is greatest?", ["4/9", "5/11", "6/13", "7/15", "8/17"], "8/17",
      "<p><strong>8/17.</strong> Har bir kasr 1/2 dan kichik, va ularning 1/2 dan farqi kamayib boradi: 4/9 da 1/18, 8/17 da 1/34. Farq eng kichigi — eng katta kasr.</p><p><strong>4/9</strong> — «kichik maxraj — katta kasr» deb oʻylagan javob.</p>"),
    q("What is (3/4) ÷ (3/8)?", ["9/32", "1/2", "2", "8/3", "4"], "2",
      "<p><strong>2.</strong> 3/4 × 8/3 = 2.</p><p><strong>9/32</strong> — boʻlish oʻrniga koʻpaytirilgan; <strong>1/2</strong> — teskari tomonga boʻlingan.</p>"),
    q("What is 1/4 + 0.15 + 3/5, expressed as a decimal?", ["0.5", "0.7", "0.9", "1", "1.15"], "1",
      "<p><strong>1.</strong> 0.25 + 0.15 + 0.6 = 1.</p><p><strong>0.7</strong> — 3/5 ni 0.3 deb oʻqigan javob.</p>"),
    q("Which of the following fractions, written as a decimal, terminates?", ["1/6", "1/3", "7/20", "5/12", "3/7"], "7/20",
      "<p><strong>7/20.</strong> 20 = 2 × 2 × 5 — maxrajda faqat 2 va 5, demak 0.35 chekli.</p><p>6, 3, 12 va 7 da 3 yoki 7 bor — ular cheksiz takrorlanadi.</p>"),
    q("What is 0.2 × 0.3 × 0.5?", ["0.0003", "0.003", "0.03", "0.3", "1"], "0.03",
      "<p><strong>0.03.</strong> 2 × 3 × 5 = 30; uchta oʻnli xona → 0.030.</p><p><strong>1</strong> — qoʻshilgan javob (0.2 + 0.3 + 0.5).</p>"),
    q("If 2/5 of a number is 18, what is 3/10 of the number?", ["9", "12", "13.5", "15", "27"], "13.5",
      "<p><strong>13.5.</strong> Son = 18 ÷ 2/5 = 45; 3/10 × 45 = 13.5.</p><p><strong>27</strong> — 18 ni 3/2 ga koʻpaytirib, sonning oʻzini topmasdan oʻtib ketgan javob.</p>"),
    q("A company spends 1/4 of its budget on rent and 2/5 on salaries. What fraction of the budget remains?", ["3/20", "1/4", "7/20", "3/5", "13/20"], "7/20",
      "<p><strong>7/20.</strong> 1/4 + 2/5 = 5/20 + 8/20 = 13/20; qolgani 7/20.</p><p><strong>13/20</strong> — sarflangan qism; savol qolganini soʻradi.</p>"),
    q("A bonus of $360 is shared so that Aziz receives 5/12 of it. How much does Aziz receive?", ["$30", "$72", "$144", "$150", "$210"], "$150",
      "<p><strong>$150.</strong> 360 ÷ 12 = 30, 30 × 5 = 150.</p><p><strong>$210</strong> — qolgan ulush (7/12).</p>"),
    q("A tank is 3/8 full. After 45 liters are added, it is 3/4 full. What is the capacity of the tank, in liters?", ["60", "90", "120", "150", "180"], "120",
      "<p><strong>120.</strong> 3/4 − 3/8 = 3/8; 45 litr — sigʻimning 3/8 qismi, demak 45 ÷ 3/8 = 120.</p><p><strong>60</strong> — 45 ni 3/4 ga boʻlgan javob.</p>"),
    q("The value of 0.249 × 0.81 is closest to which of the following?", ["0.002", "0.02", "0.2", "2", "20"], "0.2",
      "<p><strong>0.2.</strong> 0.249 ≈ 1/4, 0.81 ≈ 0.8; 0.8 ÷ 4 = 0.2.</p><p><strong>0.02</strong> — oʻnli xonalarni ortiqcha sanagan javob.</p>"),
    q("What is the value of 1 ÷ (1/2 + 1/3)?", ["1/5", "5/6", "6/5", "5", "6"], "6/5",
      "<p><strong>6/5.</strong> 1/2 + 1/3 = 5/6; 1 ÷ 5/6 = 6/5.</p><p><strong>5</strong> — 1/2 + 1/3 ni 1/5 deb, keyin teskarisini olgan javob.</p>"),
    q("Which of the following is NOT equal to 0.6?", ["3/5", "6/10", "12/20", "9/15", "18/25"], "18/25",
      "<p><strong>18/25.</strong> 18/25 = 72/100 = 0.72.</p><p>Qolganlari qisqartirilsa, hammasi 3/5 = 0.6.</p>"),
    q("If <i>x</i> = 0.4 and <i>y</i> = 0.25, what is the value of <i>x</i>/<i>y</i> + <i>y</i>/<i>x</i>?", ["0.65", "1.6", "2.225", "2.5", "4"], "2.225",
      "<p><strong>2.225.</strong> 0.4 ÷ 0.25 = 1.6; 0.25 ÷ 0.4 = 0.625; yigʻindisi 2.225.</p><p><strong>1.6</strong> — faqat birinchi hadni hisoblagan javob.</p>"),
    q("What is the value of (1 − 1/2)(1 − 1/3)(1 − 1/4) … (1 − 1/10)?", ["1/100", "1/10", "1/9", "9/10", "1"], "1/10",
      "<p><strong>1/10.</strong> 1/2 × 2/3 × 3/4 × … × 9/10 — har bir surat oldingi maxraj bilan qisqaradi, qoladi 1/10.</p><p><strong>1/9</strong> — oxirgi hadni (9/10) tashlab ketgan javob.</p>"),
    q("A team finished 2/5 of a project in the first month and 1/3 of the remaining work in the second month. What fraction of the project is still unfinished?", ["1/5", "4/15", "2/5", "7/15", "3/5"], "2/5",
      "<p><strong>2/5.</strong> Birinchi oydan keyin 3/5 qoldi; uning 1/3 qismi 1/5. Qoldi 3/5 − 1/5 = 2/5.</p><p><strong>4/15</strong> — 1/3 ni butun loyihadan olgan javob (1 − 2/5 − 1/3).</p>"),
    q("A café buys 2.4 kilograms of coffee at $12.50 per kilogram. How much does it pay?", ["$24.00", "$28.50", "$30.00", "$31.25", "$36.00"], "$30.00",
      "<p><strong>$30.00.</strong> 12.5 × 2.4 = 12.5 × 2 + 12.5 × 0.4 = 25 + 5.</p><p><strong>$31.25</strong> — 2.5 kg deb yaxlitlab, tuzatmagan javob.</p>"),
]

# =====================================================================
# GMAT-7 — remainders
# =====================================================================
Q7 = [
    q("What is the remainder when 100 is divided by 7?", ["1", "2", "3", "4", "5"], "2",
      "<p><strong>2.</strong> 7 × 14 = 98; 100 − 98 = 2.</p><p><strong>4</strong> — 96 ni 7 ning karralisi deb olgan javob; 96 = 7 × 13 + 5, u 7 ga boʻlinmaydi. Avval 100 dan kichik eng katta karralini toping.</p>"),
    q("What is the remainder when 7 is divided by 12?", ["0", "1", "5", "7", "12"], "7",
      "<p><strong>7.</strong> 12 soni 7 ning ichiga bir marta ham sigʻmaydi — boʻlinma 0, qoldiq 7.</p><p><strong>5</strong> — 12 − 7 ni hisoblagan javob.</p>"),
    q("When the positive integer <i>n</i> is divided by 5, the remainder is 3. Which of the following could be <i>n</i>?", ["15", "18", "20", "22", "24"], "18",
      "<p><strong>18.</strong> 18 = 5 × 3 + 3.</p><p>22 va 24 ning qoldiqlari 2 va 4; 15 va 20 — qoldiqsiz.</p>"),
    q("What is the remainder when 1,000 is divided by 9?", ["0", "1", "2", "3", "8"], "1",
      "<p><strong>1.</strong> 9 ga boʻlishdagi qoldiq raqamlar yigʻindisining qoldigʻiga teng: 1 + 0 + 0 + 0 = 1.</p><p><strong>0</strong> — 1,000 ni yumaloq son deb, boʻlinadi deb oʻylagan javob.</p>"),
    q("When the positive integer <i>n</i> is divided by 4, the remainder is 3. What is the remainder when 3<i>n</i> is divided by 4?", ["0", "1", "2", "3", "9"], "1",
      "<p><strong>1.</strong> 3 × 3 = 9, 9 = 4 × 2 + 1.</p><p><strong>9</strong> — koʻpaytirib, qayta boʻlmagan javob; qoldiq 4 dan kichik boʻlishi shart.</p>"),
    q("When the positive integer <i>n</i> is divided by 7, the remainder is 5. What is the remainder when <i>n</i> + 10 is divided by 7?", ["1", "2", "3", "5", "15"], "1",
      "<p><strong>1.</strong> 5 + 10 = 15 = 7 × 2 + 1.</p><p><strong>3</strong> — 10 ni 7 ga boʻlib, qoldiqlarni qoʻshmagan javob (10 ÷ 7 qoldiq 3).</p>"),
    q("How many integers from 1 to 50, inclusive, leave a remainder of 1 when divided by 4?", ["11", "12", "13", "14", "25"], "13",
      "<p><strong>13.</strong> 1, 5, 9, …, 49: (49 − 1) ÷ 4 + 1 = 13.</p><p><strong>12</strong> — «+1» unutilgan javob; 1 ning oʻzi ham shartni bajaradi.</p>"),
    q("What is the smallest positive integer that leaves a remainder of 2 when divided by 3 and a remainder of 3 when divided by 4?", ["5", "7", "11", "14", "23"], "11",
      "<p><strong>11.</strong> 4 ga boʻlganda qoldiq 3: 3, 7, 11, … Ulardan 3 ga boʻlganda qoldiq 2 beradigan birinchisi — 11.</p><p><strong>23</strong> ham shartni bajaradi, lekin eng kichigi emas.</p>"),
    q("If today is Thursday, what day of the week will it be 30 days from today?", ["Friday", "Saturday", "Sunday", "Monday", "Tuesday"], "Saturday",
      "<p><strong>Saturday.</strong> 30 = 7 × 4 + 2; payshanba + 2 kun = shanba.</p><p><strong>Friday</strong> — bugunni birinchi kun deb sanagan javob.</p>"),
    q("When 75 is divided by the positive integer <i>d</i>, the remainder is 3. Which of the following could be <i>d</i>?", ["2", "3", "5", "8", "10"], "8",
      "<p><strong>8.</strong> 75 = 8 × 9 + 3. Qoldiq 3 boʻlishi uchun <i>d</i> 72 ni boʻlishi va 3 dan katta boʻlishi kerak.</p><p><strong>3</strong> — 72 ni boʻladi, lekin qoldiq boʻluvchiga teng boʻlolmaydi.</p>"),
    q("A printer packs 250 brochures into boxes of 12. How many brochures are left over after all full boxes are packed?", ["2", "4", "8", "10", "12"], "10",
      "<p><strong>10.</strong> 12 × 20 = 240; 250 − 240 = 10.</p><p><strong>12</strong> — qoldiq boʻluvchiga teng boʻlolmaydi: 12 ta boʻlsa, yana bitta quti toʻladi.</p>"),
    q("A year of 365 days begins on a Sunday. On what day of the week does it end?", ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"], "Sunday",
      "<p><strong>Sunday.</strong> Oxirgi kun birinchisidan 364 kun keyin; 364 = 7 × 52, qoldiq 0 — yana yakshanba.</p><p><strong>Monday</strong> — 365 ÷ 7 qoldigʻini (1) olgan javob; birinchi kunning oʻzi sanalib ketgan.</p>"),
    q("Tickets numbered 1 to 200 are handed out in rotation to 6 desks: ticket 1 to desk 1, ticket 2 to desk 2, and so on, with ticket 7 going to desk 1 again. Which desk receives ticket 200?", ["1", "2", "3", "4", "6"], "2",
      "<p><strong>2.</strong> 200 = 6 × 33 + 2 — qoldiq 2, demak 2-stol.</p><p><strong>6</strong> — qoldiq 0 boʻlganda toʻgʻri boʻlardi (masalan, 198-chipta).</p>"),
    q("A batch of 1,000 bolts is packed 24 to a box. How many more bolts are needed to fill the last, partly filled box?", ["4", "8", "12", "16", "24"], "8",
      "<p><strong>8.</strong> 24 × 41 = 984; ortib qolgani 16, toʻldirish uchun 24 − 16 = 8.</p><p><strong>16</strong> — qoldiqning oʻzi; savol qancha <i>yetishmasligini</i> soʻradi.</p>"),
    q("When the positive integer <i>n</i> is divided by 8, the remainder is 6. What is the remainder when <i>n</i> is divided by 4?", ["0", "1", "2", "3", "6"], "2",
      "<p><strong>2.</strong> <i>n</i> = 8<i>k</i> + 6; 8<i>k</i> 4 ga boʻlinadi, 6 ni 4 ga boʻlsak qoldiq 2.</p><p><strong>6</strong> — qoldiqni koʻchirib qoʻygan javob; 4 ga boʻlganda qoldiq 4 dan kichik.</p>"),
    q("When the positive integer <i>n</i> is divided by 6, the remainder is 4. What is the remainder when <i>n</i><sup>2</sup> is divided by 6?", ["0", "2", "3", "4", "16"], "4",
      "<p><strong>4.</strong> 4<sup>2</sup> = 16 = 6 × 2 + 4. Tekshiruv: <i>n</i> = 10, 100 = 6 × 16 + 4 ✓.</p><p><strong>16</strong> — kvadratni olib, qayta boʻlmagan javob.</p>"),
    q("When the positive integer <i>m</i> is divided by 5, the remainder is 2, and when the positive integer <i>n</i> is divided by 5, the remainder is 4. What is the remainder when <i>mn</i> is divided by 5?", ["1", "2", "3", "4", "8"], "3",
      "<p><strong>3.</strong> 2 × 4 = 8 = 5 + 3.</p><p><strong>1</strong> — qoldiqlarni qoʻshib (6) boʻlgan javob; savol koʻpaytmani soʻradi.</p>"),
    q("What is the remainder when 2<sup>20</sup> is divided by 7?", ["1", "2", "3", "4", "6"], "4",
      "<p><strong>4.</strong> 2<sup>3</sup> = 8 ni 7 ga boʻlsak qoldiq 1. 2<sup>20</sup> = (2<sup>3</sup>)<sup>6</sup> × 2<sup>2</sup> → 1 × 4 = 4.</p><p><strong>1</strong> — 20 ni 3 ga boʻlinadi deb hisoblagan javob.</p>"),
    q("A supervisor divides 87 tasks among 5 workers as evenly as possible. How many of the workers receive one more task than the others?", ["1", "2", "3", "4", "17"], "2",
      "<p><strong>2.</strong> 87 = 5 × 17 + 2: har biriga 17 ta, ortib qolgan 2 ta vazifa ikki ishchiga beriladi.</p><p><strong>17</strong> — boʻlinma; savol qoldiqni soʻradi.</p>"),
    q("Shipments arrive every 6 days. The first shipment arrives on a Monday. On what day of the week does the 10th shipment arrive?", DAYS5, "Saturday",
      "<p><strong>Saturday.</strong> 10-yuk birinchisidan 9 × 6 = 54 kun keyin keladi; 54 = 7 × 7 + 5, dushanba + 5 kun = shanba.</p><p><strong>Friday</strong> — 10 × 6 = 60 kun deb hisoblagan javob; birinchi yuk 0-kunda keladi.</p>"),
]

# =====================================================================
# GMAT-8 — exponents and roots
# =====================================================================
Q8 = [
    q("What is 2<sup>3</sup> × 2<sup>4</sup>?", ["64", "128", "256", "4,096", "16,384"], "128",
      "<p><strong>128.</strong> 2<sup>3 + 4</sup> = 2<sup>7</sup> = 128.</p><p><strong>4,096</strong> — darajalarni koʻpaytirgan javob (2<sup>12</sup>).</p>"),
    q("What is (3<sup>2</sup>)<sup>3</sup>?", ["81", "243", "729", "2,187", "6,561"], "729",
      "<p><strong>729.</strong> 3<sup>2 × 3</sup> = 3<sup>6</sup> = 729.</p><p><strong>243</strong> — darajalarni qoʻshgan javob (3<sup>5</sup>).</p>"),
    q("What is 5<sup>0</sup> + 5<sup>−1</sup>?", ["0.2", "1", "1.2", "5", "6"], "1.2",
      "<p><strong>1.2.</strong> 5<sup>0</sup> = 1, 5<sup>−1</sup> = 1/5 = 0.2.</p><p><strong>0.2</strong> — 5<sup>0</sup> ni 0 deb olgan javob.</p>"),
    q("Which of the following is equal to √50?", ["2√5", "5√2", "10√5", "25√2", "50"], "5√2",
      "<p><strong>5√2.</strong> √50 = √(25 × 2) = 5√2.</p><p><strong>25√2</strong> — 25 ni ildizdan chiqarmasdan koʻchirgan javob.</p>"),
    q("If 3<sup><i>x</i></sup> = 81, what is the value of <i>x</i>?", ["3", "4", "9", "27", "77"], "4",
      "<p><strong>4.</strong> 81 = 3 × 3 × 3 × 3 = 3<sup>4</sup>.</p><p><strong>27</strong> — 81 ni 3 ga boʻlgan javob.</p>"),
    q("If 4<sup><i>x</i></sup> = 2<sup>10</sup>, what is the value of <i>x</i>?", ["2.5", "5", "6", "8", "20"], "5",
      "<p><strong>5.</strong> 4<sup><i>x</i></sup> = 2<sup>2<i>x</i></sup>, demak 2<i>x</i> = 10.</p><p><strong>2.5</strong> — 10 ni 4 ga boʻlgan javob; asos 4 — bu 2<sup>2</sup>, demak 2 ga boʻlinadi.</p>"),
    q("What is the value of (−2)<sup>5</sup>?", ["−32", "−10", "10", "25", "32"], "−32",
      "<p><strong>−32.</strong> Beshta manfiy koʻpaytuvchi — natija manfiy.</p><p><strong>32</strong> — ishorani yoʻqotgan javob; <strong>−10</strong> — asosni darajaga koʻpaytirgan.</p>"),
    q("What is the value of −3<sup>2</sup> + (−3)<sup>2</sup>?", ["−18", "−9", "0", "9", "18"], "0",
      "<p><strong>0.</strong> −3<sup>2</sup> = −9 (minus darajaga kirmaydi), (−3)<sup>2</sup> = 9.</p><p><strong>18</strong> — ikkalasini ham 9 deb olgan javob.</p>"),
    q("What is the value of √(9 + 16)?", ["5", "7", "12.5", "25", "144"], "5",
      "<p><strong>5.</strong> √25 = 5.</p><p><strong>7</strong> — √9 + √16 = 3 + 4 deb yigʻindini boʻlib yuborgan javob.</p>"),
    q("What is the value of 2<sup>−3</sup>?", ["−8", "−1/8", "1/8", "1/6", "8"], "1/8",
      "<p><strong>1/8.</strong> 2<sup>−3</sup> = 1/2<sup>3</sup>.</p><p><strong>−8</strong> — manfiy darajani manfiy son deb oʻqigan javob; <strong>1/6</strong> — 2 × 3 ga boʻlgan.</p>"),
    q("An investment of $3,000 doubles in value every 8 years. What is it worth after 32 years?", ["$12,000", "$24,000", "$48,000", "$96,000", "$768,000"], "$48,000",
      "<p><strong>$48,000.</strong> 32 ÷ 8 = 4 marta ikki baravar: 3,000 × 2<sup>4</sup> = 48,000.</p><p><strong>$12,000</strong> — 4 ga koʻpaytirgan javob (3,000 × 4), 2<sup>4</sup> ga emas.</p>"),
    q("A file takes up 2<sup>12</sup> kilobytes. How many files of that size fit into 2<sup>20</sup> kilobytes of storage?", ["8", "32", "128", "256", "512"], "256",
      "<p><strong>256.</strong> 2<sup>20</sup> ÷ 2<sup>12</sup> = 2<sup>8</sup> = 256.</p><p><strong>8</strong> — darajalar ayirmasini javob deb qoldirgan.</p>"),
    q("What is the value of (2<sup>5</sup> × 3<sup>4</sup>) ÷ (2<sup>3</sup> × 3<sup>2</sup>)?", ["6", "12", "18", "36", "72"], "36",
      "<p><strong>36.</strong> 2<sup>2</sup> × 3<sup>2</sup> = 4 × 9.</p><p><strong>6</strong> — 2 × 3: daraja koʻrsatkichlarini koʻchirmasdan qoldirgan javob.</p>"),
    q("What is the value of √12 × √3?", ["3", "6", "9", "15", "36"], "6",
      "<p><strong>6.</strong> √(12 × 3) = √36 = 6.</p><p><strong>36</strong> — ildizni olishni unutgan javob.</p>"),
    q("Which of the following is equal to 2<sup>3</sup> + 2<sup>3</sup>?", ["2<sup>4</sup>", "2<sup>6</sup>", "2<sup>9</sup>", "4<sup>6</sup>", "8<sup>6</sup>"], "2<sup>4</sup>",
      "<p><strong>2<sup>4</sup>.</strong> 8 + 8 = 16 = 2<sup>4</sup>, yaʼni 2 × 2<sup>3</sup>.</p><p><strong>2<sup>6</sup></strong> — qoʻshishda darajalarni qoʻshgan javob; bu faqat koʻpaytirishda ishlaydi.</p>"),
    q("If 0 &lt; <i>x</i> &lt; 1, which of the following has the greatest value?", ["<i>x</i><sup>3</sup>", "<i>x</i><sup>2</sup>", "<i>x</i>", "√<i>x</i>", "<i>x</i>/2"], "√<i>x</i>",
      "<p><strong>√x.</strong> 0 va 1 orasidagi son darajaga koʻtarilsa kichrayadi, ildiz olinsa kattalashadi: <i>x</i> = 1/4 da √<i>x</i> = 1/2.</p><p><strong>x<sup>3</sup></strong> — «katta daraja — katta son» deb oʻylagan javob; bu faqat 1 dan katta sonlarda toʻgʻri.</p>"),
    q("If 2<sup><i>x</i> + 1</sup> = 4<sup><i>x</i> − 1</sup>, what is the value of <i>x</i>?", ["1", "2", "3", "4", "5"], "3",
      "<p><strong>3.</strong> 4<sup><i>x</i> − 1</sup> = 2<sup>2<i>x</i> − 2</sup>; <i>x</i> + 1 = 2<i>x</i> − 2, <i>x</i> = 3.</p><p>Tekshiruv: 2<sup>4</sup> = 16 va 4<sup>2</sup> = 16 ✓. Asosni almashtirganda daraja ikkiga koʻpaytiriladi: 4<sup><i>x</i> − 1</sup> = 2<sup>2<i>x</i> − 2</sup>, 2<sup><i>x</i> − 1</sup> emas.</p>"),
    q("What is the value of 2<sup>10</sup> − 2<sup>9</sup>?", ["1", "2", "256", "512", "1,024"], "512",
      "<p><strong>512.</strong> 2<sup>9</sup>(2 − 1) = 2<sup>9</sup>.</p><p><strong>2</strong> — darajalarni ayirgan javob (2<sup>10 − 9</sup>); bu boʻlishda ishlaydi, ayirishda emas.</p>"),
    q("The number of users of an app tripled every year. At the end of 2022 the app had 4,000 users. How many users did it have at the end of 2025?", ["12,000", "36,000", "48,000", "108,000", "324,000"], "108,000",
      "<p><strong>108,000.</strong> 3 yil — 3 marta uch baravar: 4,000 × 3<sup>3</sup> = 4,000 × 27.</p><p><strong>36,000</strong> — ikki yil deb hisoblagan javob (4,000 × 9); 2022 dan 2025 gacha uch yil.</p>"),
    q("A company's revenue grew from $2 million to $18 million over two years, growing by the same factor each year. By what factor did revenue grow each year?", ["3", "4", "6", "8", "9"], "3",
      "<p><strong>3.</strong> Ikki yilda 9 baravar: har yilgi koeffitsiyent <i>k</i> uchun <i>k</i><sup>2</sup> = 9, <i>k</i> = 3. Tekshiruv: 2 → 6 → 18 ✓.</p><p><strong>9</strong> — ikki yillik koeffitsiyent, bir yillik emas.</p>"),
]

# =====================================================================
# GMAT-9 — units digits and cyclicity
# =====================================================================
Q9 = [
    q("What is the units digit of 47 × 83?", ["1", "3", "4", "7", "9"], "1",
      "<p><strong>1.</strong> 7 × 3 = 21 — oxirgi raqam 1.</p><p><strong>4</strong> — oʻnlar raqamlarini koʻpaytirgan javob.</p>"),
    q("What is the units digit of 2<sup>6</sup>?", ["0", "2", "4", "6", "8"], "4",
      "<p><strong>4.</strong> 2<sup>6</sup> = 64. Siklda: 6 ÷ 4 qoldiq 2 → ikkinchi oʻrin, 4.</p><p><strong>2</strong> — siklning birinchi oʻrnini olgan javob.</p>"),
    q("What is the units digit of 5<sup>17</sup>?", ["0", "1", "5", "7", "9"], "5",
      "<p><strong>5.</strong> 5 ning har qanday musbat darajasi 5 bilan tugaydi.</p><p><strong>7</strong> — darajaning oxirgi raqamini olgan javob.</p>"),
    q("What is the units digit of 9<sup>25</sup>?", ["1", "3", "5", "7", "9"], "9",
      "<p><strong>9.</strong> 9 ning sikli 9, 1: toq daraja — 9.</p><p><strong>1</strong> — juft darajadagi qiymat.</p>"),
    q("What is the units digit of 3<sup>22</sup>?", ["1", "3", "5", "7", "9"], "9",
      "<p><strong>9.</strong> Sikl 3, 9, 7, 1; 22 ÷ 4 qoldiq 2 → 9.</p><p><strong>1</strong> — «juft daraja — 1» deb oʻylagan javob.</p>"),
    q("What is the units digit of 8<sup>13</sup>?", ["0", "2", "4", "6", "8"], "8",
      "<p><strong>8.</strong> Sikl 8, 4, 2, 6; 13 ÷ 4 qoldiq 1 → 8.</p><p><strong>6</strong> — qoldiqni 0 deb olgan javob.</p>"),
    q("What is the units digit of 1,234 × 5,678?", ["0", "2", "4", "6", "8"], "2",
      "<p><strong>2.</strong> 4 × 8 = 32.</p><p><strong>8</strong> — ikkinchi sonning oxirgi raqamini koʻchirib qoʻygan javob; koʻpaytmaning oxiri ikkala oxirgi raqamning koʻpaytmasidan chiqadi.</p>"),
    q("What is the units digit of 6<sup>41</sup> + 4<sup>3</sup>?", ["0", "2", "4", "6", "8"], "0",
      "<p><strong>0.</strong> 6<sup>41</sup> → 6; 4<sup>3</sup> = 64 → 4; 6 + 4 = 10 → 0.</p><p><strong>4</strong> — faqat ikkinchi hadning oxirgi raqami.</p>"),
    q("How many zeros are at the end of 25!, the product of the integers from 1 to 25?", ["2", "5", "6", "7", "25"], "6",
      "<p><strong>6.</strong> 25 ÷ 5 = 5, 25 ÷ 25 = 1; jami 6.</p><p><strong>5</strong> — 25 dagi ikkinchi 5 ni unutgan javob; <strong>2</strong> — faqat 10 va 20 ni sanagan.</p>"),
    q("What is the units digit of 7<sup>100</sup>?", ["1", "3", "5", "7", "9"], "1",
      "<p><strong>1.</strong> Sikl 7, 9, 3, 1; 100 ÷ 4 qoldiq 0 → toʻrtinchi oʻrin, 1.</p><p><strong>7</strong> — qoldiq 0 da birinchi oʻrinni olgan javob.</p>"),
    q("An analyst multiplies the prices $17, $23 and $39 together. What is the units digit of the product?", ["1", "3", "5", "7", "9"], "9",
      "<p><strong>9.</strong> 7 × 3 = 21 → 1; 1 × 9 = 9.</p><p><strong>1</strong> — uchinchi koʻpaytuvchini tashlab ketgan javob.</p>"),
    q("A spreadsheet adds 2<sup>1</sup> + 2<sup>2</sup> + 2<sup>3</sup> + … + 2<sup>10</sup>. What is the units digit of the total?", ["0", "2", "4", "6", "8"], "6",
      "<p><strong>6.</strong> Oxirgi raqamlar 2, 4, 8, 6 takrorlanadi; har toʻrttasining yigʻindisi 20 → 0. Ikki toʻliq sikl (8 had) → 0, qolgan 2<sup>9</sup> va 2<sup>10</sup>: 2 + 4 = 6.</p><p><strong>4</strong> — faqat oxirgi hadning (2<sup>10</sup>) oxirgi raqami.</p>"),
    q("What is the units digit of 13<sup>4</sup> × 22<sup>3</sup>?", ["1", "2", "4", "6", "8"], "8",
      "<p><strong>8.</strong> 3<sup>4</sup> → 1; 2<sup>3</sup> = 8; 1 × 8 = 8.</p><p><strong>6</strong> — 2<sup>4</sup> ni olgan javob (darajani adashtirgan).</p>"),
    q("How many zeros are at the end of 100!?", ["10", "20", "21", "24", "25"], "24",
      "<p><strong>24.</strong> 100 ÷ 5 = 20, 100 ÷ 25 = 4; jami 24.</p><p><strong>20</strong> — 25, 50, 75, 100 dagi ikkinchi 5 larni unutgan javob.</p>"),
    q("What is the units digit of 4<sup>15</sup>?", ["0", "2", "4", "6", "8"], "4",
      "<p><strong>4.</strong> 4 ning sikli 4, 6: toq daraja — 4.</p><p><strong>6</strong> — juft darajadagi qiymat; 15 esa toq.</p>"),
    q("What is the units digit of 2<sup>40</sup>?", ["0", "2", "4", "6", "8"], "6",
      "<p><strong>6.</strong> 40 ÷ 4 qoldiq 0 → siklning toʻrtinchi oʻrni, 6.</p><p><strong>2</strong> — qoldiq 0 ni birinchi oʻrin deb oʻqigan javob.</p>"),
    q("What is the units digit of 3<sup>33</sup> × 7<sup>22</sup>?", ["1", "3", "5", "7", "9"], "7",
      "<p><strong>7.</strong> 3<sup>33</sup>: 33 ÷ 4 qoldiq 1 → 3. 7<sup>22</sup>: qoldiq 2 → 9. 3 × 9 = 27 → 7.</p><p><strong>1</strong> — 3 va 7 ni «bir-birini 1 ga keltiradi» deb oʻylagan javob; bu faqat bir xil darajada ishlaydi.</p>"),
    q("How many zeros are at the end of the product 2<sup>10</sup> × 5<sup>7</sup>?", ["3", "7", "10", "17", "70"], "7",
      "<p><strong>7.</strong> 2<sup>10</sup> × 5<sup>7</sup> = 2<sup>3</sup> × 10<sup>7</sup> = 8 × 10<sup>7</sup> — yettita nol.</p><p><strong>10</strong> — 2 larni sanagan javob; nollar soni 2 va 5 ning kami bilan belgilanadi.</p>"),
    q("A warehouse has 19 aisles. Each aisle has 19 shelves, each shelf holds 19 boxes, and each box contains 19 items. What is the units digit of the total number of items?", ["1", "3", "5", "7", "9"], "1",
      "<p><strong>1.</strong> Jami 19<sup>4</sup>; 9 ning sikli 9, 1 — juft daraja → 1.</p><p><strong>9</strong> — 19<sup>3</sup> ni hisoblagan javob: toʻrt daraja bor (yoʻlak, javon, quti, buyum).</p>"),
    q("A factory produced 3 units on day 1, and its output doubled every day after that. What is the units digit of the number of units it produced on day 20?", ["0", "2", "4", "6", "8"], "4",
      "<p><strong>4.</strong> 20-kun: 3 × 2<sup>19</sup>. 19 ÷ 4 qoldiq 3 → 2<sup>19</sup> oxiri 8; 3 × 8 = 24 → 4.</p><p><strong>8</strong> — 3 × 2<sup>20</sup> deb hisoblagan javob: birinchi kunda hali ikki baravar oshmagan.</p>"),
]

# =====================================================================
# GMAT-10 — ratios and proportions
# =====================================================================
Q10 = [
    q("What is the ratio of 18 to 24 in lowest terms?", ["2 : 3", "3 : 4", "6 : 8", "4 : 3", "3 : 2"], "3 : 4",
      "<p><strong>3 : 4.</strong> Ikkalasini 6 ga boʻlamiz.</p><p><strong>6 : 8</strong> — teng, lekin eng sodda koʻrinishda emas; <strong>4 : 3</strong> — tartib almashgan.</p>"),
    q("The ratio of red pens to blue pens in a box is 3 to 5. If the box contains 40 pens, how many are blue?", ["8", "15", "24", "25", "40"], "25",
      "<p><strong>25.</strong> 8 qism, bir qism 5; koʻklari 5 × 5.</p><p><strong>15</strong> — qizillar soni.</p>"),
    q("If 3/<i>x</i> = 12/20, what is the value of <i>x</i>?", ["4", "5", "8", "15", "80"], "5",
      "<p><strong>5.</strong> 12<i>x</i> = 60, <i>x</i> = 5. Yoki: 12/20 = 3/5.</p><p><strong>80</strong> — 20 × 12 ÷ 3: kasrni agʻdarib, oʻzaro koʻpaytirishni teskari bajargan javob.</p>"),
    q("On a map, 1 centimeter represents 50 kilometers. Two cities are 3.5 centimeters apart on the map. How far apart are they?", ["14.3 km", "53.5 km", "150 km", "175 km", "200 km"], "175 km",
      "<p><strong>175 km.</strong> 3.5 × 50 = 175.</p><p><strong>14.3 km</strong> — boʻlgan javob (50 ÷ 3.5).</p>"),
    q("Two partners split a profit of $16,000 in the ratio 5 to 3. By how much does the larger share exceed the smaller share?", ["$2,000", "$4,000", "$6,000", "$10,000", "$16,000"], "$4,000",
      "<p><strong>$4,000.</strong> 8 qism, bir qism 2,000; farq 2 qism = 4,000.</p><p><strong>$6,000</strong> — kichik ulush; <strong>$10,000</strong> — katta ulush.</p>"),
    q("If the ratio of <i>a</i> to <i>b</i> is 3 to 4 and the ratio of <i>b</i> to <i>c</i> is 6 to 7, what is the ratio of <i>a</i> to <i>c</i>?", ["3 : 7", "1 : 2", "9 : 14", "3 : 4", "6 : 7"], "9 : 14",
      "<p><strong>9 : 14.</strong> <i>b</i> ni 12 ga keltiramiz: <i>a</i> : <i>b</i> = 9 : 12, <i>b</i> : <i>c</i> = 12 : 14.</p><p><strong>3 : 7</strong> — chetki sonlarni toʻgʻridan-toʻgʻri olgan javob.</p>"),
    q("If 6 machines produce 480 units in 4 hours, how many units do 9 such machines produce in 4 hours?", ["320", "540", "640", "720", "960"], "720",
      "<p><strong>720.</strong> Bitta mashina 4 soatda 80 dona; 9 × 80 = 720.</p><p><strong>320</strong> — teskari proporsiya deb hisoblangan javob; mashinalar koʻpaysa, mahsulot ham koʻpayadi.</p>"),
    q("If 8 workers can finish a job in 15 days, how many days would 12 workers need to finish the same job, working at the same rate?", ["8", "10", "12", "18", "22.5"], "10",
      "<p><strong>10.</strong> Ish = 8 × 15 = 120 ishchi-kun; 120 ÷ 12 = 10.</p><p><strong>22.5</strong> — toʻgʻri proporsiya deb hisoblangan javob; ishchi koʻpaysa, kun kamayadi.</p>"),
    q("The ratio of <i>x</i> to <i>y</i> is 2 to 5, and <i>x</i> + <i>y</i> = 63. What is the value of <i>y</i> − <i>x</i>?", ["9", "18", "27", "36", "45"], "27",
      "<p><strong>27.</strong> 7 qism, bir qism 9; <i>y</i> = 45, <i>x</i> = 18; farq 27.</p><p><strong>45</strong> — <i>y</i> ning oʻzi.</p>"),
    q("A 40-liter mixture contains water and juice in the ratio 3 to 2. How many liters of juice must be added to make the ratio of water to juice 1 to 1?", ["4", "6", "8", "12", "16"], "8",
      "<p><strong>8.</strong> Suv 24 l, sharbat 16 l. 1 : 1 boʻlishi uchun sharbat 24 l boʻlishi kerak — 8 l qoʻshiladi.</p><p><strong>16</strong> — mavjud sharbat miqdori.</p>"),
    q("At a company, the ratio of employees who work remotely to employees who work in the office is 2 to 3. If 60 employees work remotely, how many employees does the company have?", ["90", "120", "150", "180", "300"], "150",
      "<p><strong>150.</strong> Bir qism 30; jami 5 qism = 150.</p><p><strong>90</strong> — faqat ofisdagilar (3 qism).</p>"),
    q("An exchange office gives 12,500 sum for 1 dollar. How many dollars does 875,000 sum buy?", ["7", "35", "70", "175", "700"], "70",
      "<p><strong>70.</strong> 875,000 ÷ 12,500 = 70.</p><p><strong>7</strong> va <strong>700</strong> — nollarni adashtirgan javoblar; tekshiruv: 70 × 12,500 = 875,000.</p>"),
    q("A recipe for 6 servings uses 450 grams of rice. How many grams of rice are needed for 10 servings?", ["270", "600", "700", "750", "900"], "750",
      "<p><strong>750.</strong> Bir porsiyaga 75 g; 10 × 75.</p><p><strong>270</strong> — teskari proporsiya deb hisoblangan javob.</p>"),
    q("The ratio of a manager's monthly salary to an analyst's monthly salary is 7 to 4. If the manager earns $2,100 more per month than the analyst, what does the analyst earn per month?", ["$1,200", "$2,800", "$3,000", "$3,675", "$4,900"], "$2,800",
      "<p><strong>$2,800.</strong> Farq 3 qism = 2,100, bir qism 700; analitik 4 × 700.</p><p><strong>$4,900</strong> — menejerning maoshi.</p>"),
    q("The ratio of cats to dogs at a shelter is 4 to 3. If 6 more dogs arrive, the ratio becomes 1 to 1. How many cats are at the shelter?", ["6", "18", "24", "28", "42"], "24",
      "<p><strong>24.</strong> Mushuklar 4<i>k</i>, itlar 3<i>k</i>; 4<i>k</i> = 3<i>k</i> + 6, <i>k</i> = 6. Mushuklar 24.</p><p><strong>18</strong> — itlar soni (oldin).</p>"),
    q("Two numbers are in the ratio 2 to 3. If 4 is added to each number, the ratio becomes 3 to 4. What is the smaller of the original numbers?", ["4", "6", "8", "12", "16"], "8",
      "<p><strong>8.</strong> 2<i>k</i> + 4 va 3<i>k</i> + 4: 4(2<i>k</i> + 4) = 3(3<i>k</i> + 4), <i>k</i> = 4. Kichigi 8.</p><p><strong>4</strong> — <i>k</i> ning oʻzi; savol sonni soʻradi.</p>"),
    q("The ratio <i>a</i> : <i>b</i> : <i>c</i> is 2 : 3 : 5, and <i>a</i> + <i>b</i> + <i>c</i> = 150. What is the value of <i>c</i> − <i>a</i>?", ["30", "45", "50", "75", "105"], "45",
      "<p><strong>45.</strong> 10 qism, bir qism 15; <i>c</i> = 75, <i>a</i> = 30.</p><p><strong>75</strong> — <i>c</i> ning oʻzi.</p>"),
    q("If 5 machines produce 5 parts in 5 minutes, how many minutes do 100 such machines need to produce 100 parts?", ["1", "5", "20", "100", "500"], "5",
      "<p><strong>5.</strong> Bitta mashina 5 daqiqada bitta detal yasaydi; 100 ta mashina birga 5 daqiqada 100 ta.</p><p><strong>100</strong> — «hammasi 100 ga oshdi» deb oʻylagan javob.</p>"),
    q("A company divides a bonus pool of $54,000 among three teams in the ratio 2 : 3 : 4. How much does the team with the largest share receive?", ["$12,000", "$18,000", "$24,000", "$27,000", "$36,000"], "$24,000",
      "<p><strong>$24,000.</strong> 9 qism, bir qism 6,000; eng katta ulush 4 × 6,000.</p><p><strong>$27,000</strong> — yarmini olgan javob.</p>"),
    q("A car uses 6 liters of fuel per 100 kilometers, and fuel costs $1.20 per liter. What is the fuel cost of a 450-kilometer trip?", ["$27.00", "$32.40", "$36.00", "$54.00", "$64.80"], "$32.40",
      "<p><strong>$32.40.</strong> 450 km uchun 4.5 × 6 = 27 litr; 27 × 1.2 = 32.40.</p><p><strong>$27.00</strong> — litrlar soni, narx emas.</p>"),
]

PRACTICES = [
    {
        "title": "GMAT-6 Practice: Fractions and Decimals Without a Calculator",
        "description": "20 ta GMAT uslubidagi savol — kasr va oʻnli kasrlar, solishtirish, boʻlish va qism masalalari.",
        "tutorial": "GMAT-6:", "subject": "GMAT", "level": "medium", "questions": Q6,
    },
    {
        "title": "GMAT-7 Practice: Remainders and Divisibility Patterns",
        "description": "20 ta GMAT uslubidagi savol — qoldiqlar, qoldiqlar bilan hisoblash va hafta kunlari.",
        "tutorial": "GMAT-7:", "subject": "GMAT", "level": "medium", "questions": Q7,
    },
    {
        "title": "GMAT-8 Practice: Exponents and Roots",
        "description": "20 ta GMAT uslubidagi savol — daraja qoidalari, bir xil asos, ildizlar va darajali oʻsish.",
        "tutorial": "GMAT-8:", "subject": "GMAT", "level": "medium", "questions": Q8,
    },
    {
        "title": "GMAT-9 Practice: Units Digits and Cyclicity",
        "description": "20 ta GMAT uslubidagi savol — oxirgi raqam, sikllar va faktorialdagi nollar.",
        "tutorial": "GMAT-9:", "subject": "GMAT", "level": "medium", "questions": Q9,
    },
    {
        "title": "GMAT-10 Practice: Ratios and Proportions",
        "description": "20 ta GMAT uslubidagi savol — nisbatlar, toʻgʻri va teskari proporsiya, nisbat oʻzgarishi.",
        "tutorial": "GMAT-10:", "subject": "GMAT", "level": "medium", "questions": Q10,
    },
]
