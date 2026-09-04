# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-46 … SAT-50.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context & interpretation ·
      15–16 trap-spotting · 17–18 Module 2 level · 19–20 word problems.

⚠️ SAT-49 dan Blok C: har testda interpretatsiya savollari koʻproq —
   hisoblash emas, jumlani oʻqish tekshiriladi.
⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_46_50.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Math",
    "description": "SAT Math — Prime SAT darslarining mashqlari",
    "icon":        "bi-calculator",
    "color":       "#4f46e5",
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
# SAT-46 — compound interest
# =====================================================================

Q_SAT46 = [
    {
        "text": "<p>1,000 dollars earns 10% interest compounded annually. How much is "
                "there after 2 years?</p>",
        "choices": ["1,210 dollars", "1,200 dollars", "1,100 dollars", "1,220 dollars"],
        "correct": "1,210 dollars",
        "explanation": "<p><strong>1,210.</strong> 1,000 → 1,100 → 1,210.</p>"
                       "<p><strong>1,200</strong> — oddiy foiz: har yili 100 dan. "
                       "Ikkinchi yilda 110 qoʻshilishi kerak edi.</p>",
    },
    {
        "text": "<p>2,000 dollars earns 5% simple interest for 3 years. How much "
                "interest is earned?</p>",
        "choices": ["300 dollars", "315.25 dollars", "100 dollars", "2,300 dollars"],
        "correct": "300 dollars",
        "explanation": "<p><strong>300.</strong> Oddiy foiz har doim 2,000 dan: "
                       "3 × 100.</p>"
                       "<p><strong>2,300</strong> — jami summa, foizning oʻzi "
                       "emas.</p>",
    },
    {
        "text": "<p>A rate of 12% compounded monthly means what rate per month?</p>",
        "choices": ["1%", "12%", "0.12%", "144%"],
        "correct": "1%",
        "explanation": "<p><strong>1%.</strong> 12 ÷ 12 = 1.</p>"
                       "<p>Yillik stavka davrlar soniga boʻlinadi.</p>",
    },
    {
        "text": "<p>A rate of 8% compounded quarterly, over 3 years, uses how many "
                "compounding periods?</p>",
        "choices": ["12", "3", "4", "8"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 3 yil × 4 chorak.</p>"
                       "<p>Stavka boʻlinadi va davrlar soni koʻpayadi — ikkalasi "
                       "birga.</p>",
    },
    {
        "text": "<p>Which expression gives the value of 500 dollars at 6% compounded "
                "monthly after <i>t</i> years?</p>",
        "choices": ["500(1.005)^(12t)", "500(1.06)^(12t)", "500(1.005)^t",
                    "500(1.5)^t"],
        "correct": "500(1.005)^(12t)",
        "explanation": "<p><strong>500(1.005)^(12t).</strong> 6 ÷ 12 = 0.5 foiz, "
                       "yaʼni 0.005.</p>"
                       "<p><strong>500(1.005)^t</strong> — koʻrsatkich "
                       "koʻpaytirilmagan; u yilda atigi 0.5 foiz beradi.</p>",
    },
    {
        "text": "<p>Which expression gives the value of 4,000 dollars at 10% "
                "compounded annually after <i>t</i> years?</p>",
        "choices": ["4,000(1.1)^t", "4,000(0.1)^t", "4,000(1.1)(t)", "4,000 + 400t"],
        "correct": "4,000(1.1)^t",
        "explanation": "<p><strong>4,000(1.1)^t.</strong> b = 1 + 0.1.</p>"
                       "<p><strong>4,000 + 400t</strong> — bu oddiy foiz, chiziqli "
                       "model.</p>",
    },
    {
        "text": "<p>1,000 dollars at 4% compounded annually. What is the value after "
                "2 years, to the nearest cent?</p>",
        "choices": ["1,081.60 dollars", "1,080.00 dollars", "1,040.00 dollars",
                    "1,160.00 dollars"],
        "correct": "1,081.60 dollars",
        "explanation": "<p><strong>1,081.60.</strong> 1,040, keyin 1,081.60.</p>"
                       "<p><strong>1,080</strong> — oddiy foiz; farqi 1.60.</p>",
    },
    {
        "text": "<p>An investment doubles every 8 years. Which expression gives its "
                "value after <i>t</i> years, starting from 5,000 dollars?</p>",
        "choices": ["5,000(2)^(t/8)", "5,000(2)^(8t)", "5,000(8)^t", "5,000(2)^t"],
        "correct": "5,000(2)^(t/8)",
        "explanation": "<p><strong>5,000(2)^(t/8).</strong> 8 yilda bir marta "
                       "ikkilanadi, demak vaqt 8 ga boʻlinadi.</p>"
                       "<p>Tekshiruv: t = 8 da koʻrsatkich 1 — bir marta "
                       "ikkilanadi ✓</p>",
    },
    {
        "text": "<p>A 20,000-dollar car depreciates 10% a year. What is it worth "
                "after 2 years?</p>",
        "choices": ["16,200 dollars", "16,000 dollars", "18,000 dollars",
                    "4,000 dollars"],
        "correct": "16,200 dollars",
        "explanation": "<p><strong>16,200.</strong> 18,000, keyin 16,200.</p>"
                       "<p><strong>16,000</strong> — har yili 2,000 ayirilgan, yaʼni "
                       "chiziqli hisob.</p>",
    },
    {
        "text": "<p>Which earns more over 5 years: 6% compounded annually, or 6% "
                "simple interest?</p>",
        "choices": ["Compounded — interest earns interest",
                    "Simple — it is a higher rate",
                    "They are equal",
                    "It depends on the starting amount"],
        "correct": "Compounded — interest earns interest",
        "explanation": "<p><strong>Murakkab foiz.</strong> Qoʻshilgan foiz oʻzi ham "
                       "foiz keltira boshlaydi.</p>"
                       "<p><strong>It depends</strong> — yoʻq: nisbat boshlangʻich "
                       "summaga bogʻliq emas.</p>",
    },
    {
        "text": "<p>In the model <i>V</i> = 3,000(1.07)^<i>t</i>, what does 1.07 "
                "tell you?</p>",
        "choices": ["The value grows 7% each year",
                    "The value grows 107% each year",
                    "The value grows by 1.07 dollars a year",
                    "The starting value"],
        "correct": "The value grows 7% each year",
        "explanation": "<p><strong>Yiliga 7 foiz.</strong> b = 1 + r, demak "
                       "r = 0.07.</p>"
                       "<p><strong>107%</strong> — bu qolgan qism, oʻsish emas: "
                       "qiymat 107 foizga aylanadi, 107 foizga oshmaydi.</p>",
    },
    {
        "text": "<p>Two accounts pay 8%. One compounds annually, the other quarterly. "
                "After one year, which is larger and why?</p>",
        "choices": ["Quarterly — earlier interest earns interest sooner",
                    "Annually — fewer calculations",
                    "They are the same after one year",
                    "Quarterly — the rate is four times larger"],
        "correct": "Quarterly — earlier interest earns interest sooner",
        "explanation": "<p><strong>Choraklab.</strong> Birinchi chorakning foizi "
                       "qolgan uch chorak davomida ishlaydi.</p>"
                       "<p><strong>rate is four times larger</strong> — aksincha, "
                       "stavka toʻrt marta kichik.</p>",
    },
    {
        "text": "<p>A bank advertises 6% compounded quarterly. What is the effective "
                "yearly increase, approximately?</p>",
        "choices": ["Slightly more than 6%", "Exactly 6%", "24%", "Slightly less than 6%"],
        "correct": "Slightly more than 6%",
        "explanation": "<p><strong>6 dan bir oz koʻp</strong> — taxminan 6.14 foiz.</p>"
                       "<p><strong>24%</strong> — stavka koʻpaytirilgan, aslida u "
                       "boʻlinadi.</p>",
    },
    {
        "text": "<p>A population of 10,000 grows 2% a year. Which is closest to its "
                "size after 10 years?</p>",
        "choices": ["12,190", "12,000", "10,200", "20,000"],
        "correct": "12,190",
        "explanation": "<p><strong>12,190.</strong> 1.02 oʻn marta ≈ 1.219.</p>"
                       "<p><strong>12,000</strong> — har yili 200 qoʻshilgan, "
                       "chiziqli hisob.</p>",
    },
    {
        "text": "<p>A student computes 1,000 dollars at 5% compounded annually for "
                "2 years as 1,100. What is the correct value?</p>",
        "choices": ["1,102.50 dollars", "1,100 dollars", "1,050 dollars",
                    "1,105 dollars"],
        "correct": "1,102.50 dollars",
        "explanation": "<p><strong>1,102.50.</strong> Ikkinchi yilda 5 foiz 1,050 "
                       "dan olinadi: 52.50.</p>"
                       "<p>Oʻquvchi oddiy foizni hisoblagan.</p>",
    },
    {
        "text": "<p>A student writes 8% compounded quarterly as (1.08)^(4t). What is "
                "the correct base?</p>",
        "choices": ["1.02", "1.08", "1.32", "0.02"],
        "correct": "1.02",
        "explanation": "<p><strong>1.02.</strong> Stavka ham boʻlinishi kerak edi: "
                       "8 ÷ 4 = 2 foiz.</p>"
                       "<p>Oʻquvchining modeli yiliga 36 foizdan koʻp beradi — "
                       "bank bunday vaʼda qilmagan.</p>",
    },
    {
        "text": "<p>How long does 1,000 dollars at 100% interest compounded annually "
                "take to reach 8,000 dollars?</p>",
        "choices": ["3 years", "8 years", "7 years", "4 years"],
        "correct": "3 years",
        "explanation": "<p><strong>3 yil.</strong> 100 foiz — har yili ikkilanish: "
                       "2,000, 4,000, 8,000.</p>"
                       "<p><strong>8 years</strong> — 8 marta 1,000 qoʻshilgan, "
                       "chiziqli fikr.</p>",
    },
    {
        "text": "<p>An account grows from 1,000 to 1,331 dollars in 3 years, "
                "compounded annually. What is the yearly rate?</p>",
        "choices": ["10%", "11%", "33%", "31%"],
        "correct": "10%",
        "explanation": "<p><strong>10%.</strong> 1,100, 1,210, 1,331 ✓</p>"
                       "<p><strong>33%</strong> — bu uch yillik umumiy oʻsish, "
                       "yillik emas.</p>",
    },
    {
        "text": "<p>A shop's takings grow 5% a month. If they are 2,000 dollars in "
                "January, what are they in March?</p>",
        "choices": ["2,205 dollars", "2,200 dollars", "2,100 dollars", "3,000 dollars"],
        "correct": "2,205 dollars",
        "explanation": "<p><strong>2,205.</strong> Fevral 2,100, mart 2,205 — ikki "
                       "oʻsish.</p>"
                       "<p>Yanvardan martgacha <b>ikki</b> oy oʻtadi, uch emas.</p>",
    },
    {
        "text": "<p>A family saves 5,000 dollars at 4% compounded annually for a "
                "child's education in 3 years. How much will they have, to the "
                "nearest dollar?</p>",
        "choices": ["5,624 dollars", "5,600 dollars", "5,200 dollars", "6,000 dollars"],
        "correct": "5,624 dollars",
        "explanation": "<p><strong>5,624.</strong> 5,200, 5,408, 5,624.32.</p>"
                       "<p><strong>5,600</strong> — oddiy foiz, har yili 200 dan; "
                       "farqi 24 dollar.</p>",
    },
]


# =====================================================================
# SAT-47 — functions
# =====================================================================

Q_SAT47 = [
    {
        "text": "<p>If <i>f</i>(<i>x</i>) = 4<i>x</i> − 5, what is <i>f</i>(3)?</p>",
        "choices": ["7", "12", "−5", "17"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 4(3) − 5 = 12 − 5.</p>"
                       "<p><strong>12</strong> — oxirgi had unutilgan.</p>",
    },
    {
        "text": "<p>If <i>f</i>(<i>x</i>) = <i>x</i><sup>2</sup> + 2<i>x</i>, what is "
                "<i>f</i>(−3)?</p>",
        "choices": ["3", "−3", "15", "−15"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> 9 + (−6) = 3.</p>"
                       "<p><strong>−3</strong> — (−3)<sup>2</sup> ni −9 deb olgan "
                       "javob. Qavs ishlating.</p>",
    },
    {
        "text": "<p>What is the domain of <i>f</i>(<i>x</i>) = 1 ÷ (<i>x</i> − 7)?</p>",
        "choices": ["All real numbers except 7", "All real numbers except −7",
                    "x ≥ 7", "All real numbers"],
        "correct": "All real numbers except 7",
        "explanation": "<p><strong>7 dan tashqari hamma sonlar.</strong> Maxraj nolga "
                       "aylanmasligi kerak.</p>"
                       "<p>Ishoraga eʼtibor: (x − 7) noli +7.</p>",
    },
    {
        "text": "<p>What is the domain of <i>g</i>(<i>x</i>) = √(<i>x</i> + 4)?</p>",
        "choices": ["x ≥ −4", "x ≥ 4", "x ≤ −4", "All real numbers"],
        "correct": "x ≥ −4",
        "explanation": "<p><strong>x ≥ −4.</strong> x + 4 ≥ 0.</p>"
                       "<p><strong>x ≥ 4</strong> — ishora almashtirilmagan.</p>",
    },
    {
        "text": "<p>If <i>f</i>(<i>x</i>) = 2<i>x</i><sup>2</sup> − 3<i>x</i> + 1, "
                "what is <i>f</i>(−1)?</p>",
        "choices": ["6", "0", "−4", "4"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 2(1) + 3 + 1 = 6.</p>"
                       "<p>−3(−1) = +3 — ikkinchi minus qoʻshishga aylandi.</p>",
    },
    {
        "text": "<p>What is the range of <i>f</i>(<i>x</i>) = <i>x</i><sup>2</sup> "
                "− 9?</p>",
        "choices": ["y ≥ −9", "y ≥ 9", "y ≥ 0", "All real numbers"],
        "correct": "y ≥ −9",
        "explanation": "<p><strong>y ≥ −9.</strong> Uch (0, −9) — eng past nuqta.</p>"
                       "<p>Kvadrat manfiy boʻlmaydi, demak natija hech qachon −9 "
                       "dan kichik boʻlmaydi.</p>",
    },
    {
        "text": "<p>What is the range of <i>f</i>(<i>x</i>) = −<i>x</i><sup>2</sup> "
                "+ 4?</p>",
        "choices": ["y ≤ 4", "y ≥ 4", "y ≥ −4", "All real numbers"],
        "correct": "y ≤ 4",
        "explanation": "<p><strong>y ≤ 4.</strong> a manfiy, demak uch maksimum.</p>"
                       "<p>Bu parabola 4 dan yuqoriga chiqmaydi.</p>",
    },
    {
        "text": "<p>If <i>f</i>(<i>x</i>) = 3<i>x</i> + 2, for which value of <i>x</i> "
                "is <i>f</i>(<i>x</i>) = 17?</p>",
        "choices": ["5", "17", "53", "3"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 3x + 2 = 17 → x = 5.</p>"
                       "<p>Bu savol teskari yoʻnalishda: chiqish berilgan, kirish "
                       "soʻralgan.</p>",
    },
    {
        "text": "<p>If <i>f</i>(<i>x</i>) = <i>x</i> − 1 and <i>g</i>(<i>x</i>) = "
                "3<i>x</i>, what is <i>f</i>(<i>g</i>(4))?</p>",
        "choices": ["11", "9", "12", "15"],
        "correct": "11",
        "explanation": "<p><strong>11.</strong> g(4) = 12, keyin f(12) = 11.</p>"
                       "<p><strong>9</strong> — teskari tartibda hisoblangan: "
                       "g(f(4)) = g(3) = 9.</p>",
    },
    {
        "text": "<p>A table gives <i>f</i>(1) = 4, <i>f</i>(2) = 7, <i>f</i>(3) = 10. "
                "What is <i>f</i>(2) + <i>f</i>(3)?</p>",
        "choices": ["17", "5", "21", "14"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> 7 + 10.</p>"
                       "<p><strong>5</strong> — 2 + 3 qoʻshilgan, ya'ni kirishlar; "
                       "savol chiqishlarni soʻragan.</p>",
    },
    {
        "text": "<p>A function gives the cost <i>C</i>(<i>n</i>) of printing <i>n</i> "
                "books. What is a reasonable domain in context?</p>",
        "choices": ["Whole numbers from 0 upward", "All real numbers",
                    "All positive and negative integers", "Only numbers above 100"],
        "correct": "Whole numbers from 0 upward",
        "explanation": "<p><strong>Butun, manfiy boʻlmagan sonlar.</strong> Yarim "
                       "kitob bosib boʻlmaydi va soni manfiy boʻlmaydi.</p>"
                       "<p>Kontekstli masalada aniqlanish sohasini hayot "
                       "belgilaydi.</p>",
    },
    {
        "text": "<p>The height of a ball is <i>h</i>(<i>t</i>) for <i>t</i> seconds "
                "after it is thrown, until it lands at <i>t</i> = 4. What is the "
                "domain in context?</p>",
        "choices": ["0 ≤ t ≤ 4", "All real numbers", "t ≥ 0", "0 ≤ t ≤ 20"],
        "correct": "0 ≤ t ≤ 4",
        "explanation": "<p><strong>0 dan 4 gacha.</strong> Toʻp tashlanishidan "
                       "tushishigacha.</p>"
                       "<p>Formula boshqa qiymatlarni ham qabul qiladi, lekin "
                       "ular vaziyatda maʼnosiz.</p>",
    },
    {
        "text": "<p>In <i>P</i>(<i>t</i>) = 500 + 20<i>t</i>, where <i>t</i> is years, "
                "what does <i>P</i>(0) mean?</p>",
        "choices": ["The starting population, 500",
                    "The yearly increase", "The population after 20 years",
                    "The population is zero"],
        "correct": "The starting population, 500",
        "explanation": "<p><strong>Boshlangʻich soni.</strong> t = 0 — kuzatuv "
                       "boshlangan payt.</p>"
                       "<p>20 esa har yilgi oʻsish.</p>",
    },
    {
        "text": "<p>A graph shows <i>y</i> = <i>f</i>(<i>x</i>) passing through "
                "(2, 5). What does this tell you?</p>",
        "choices": ["f(2) = 5", "f(5) = 2", "f(2) = 2", "The domain is 2"],
        "correct": "f(2) = 5",
        "explanation": "<p><strong>f(2) = 5.</strong> x koordinatasi kirish, "
                       "y koordinatasi chiqish.</p>"
                       "<p>Tartibni almashtirmang: (kirish, chiqish).</p>",
    },
    {
        "text": "<p>A student computes <i>f</i>(−2) for <i>f</i>(<i>x</i>) = "
                "<i>x</i><sup>2</sup> + <i>x</i> as −4 − 2 = −6. What is the correct "
                "value?</p>",
        "choices": ["2", "−6", "6", "−2"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> (−2)<sup>2</sup> = +4, demak "
                       "4 − 2 = 2.</p>"
                       "<p>Oʻquvchi kvadratni qavssiz hisoblagan.</p>",
    },
    {
        "text": "<p>A student says the domain of √(<i>x</i> − 5) is all real numbers "
                "except 5. What is the correct domain?</p>",
        "choices": ["x ≥ 5", "x ≠ 5", "x ≤ 5", "All real numbers"],
        "correct": "x ≥ 5",
        "explanation": "<p><strong>x ≥ 5.</strong> Ildiz uchun ichi manfiy "
                       "boʻlmasligi kerak; bu maxraj qoidasi emas.</p>"
                       "<p>x = 5 da √0 = 0 — bu ruxsat etilgan.</p>",
    },
    {
        "text": "<p>If <i>f</i>(<i>x</i>) = <i>x</i><sup>2</sup> − 6<i>x</i> + 5, for "
                "which values of <i>x</i> is <i>f</i>(<i>x</i>) = 0?</p>",
        "choices": ["1 and 5", "−1 and −5", "0 and 6", "5 only"],
        "correct": "1 and 5",
        "explanation": "<p><strong>1 va 5.</strong> (x − 1)(x − 5) = 0 (SAT-31).</p>"
                       "<p>Bu funksiyaning nollari — grafik x oʻqini shu ikki "
                       "nuqtada kesadi.</p>",
    },
    {
        "text": "<p>What is the domain of <i>f</i>(<i>x</i>) = (<i>x</i> + 1) ÷ "
                "(<i>x</i><sup>2</sup> − 4)?</p>",
        "choices": ["All real numbers except 2 and −2", "All real numbers except −1",
                    "All real numbers except 4", "x ≥ 2"],
        "correct": "All real numbers except 2 and −2",
        "explanation": "<p><strong>2 va −2 dan tashqari.</strong> Maxraj "
                       "(x − 2)(x + 2).</p>"
                       "<p>Surat nolga aylanishi muammo emas — faqat maxraj "
                       "tekshiriladi (SAT-40).</p>",
    },
    {
        "text": "<p>A taxi charges <i>C</i>(<i>k</i>) = 5,000 + 2,000<i>k</i> som for "
                "<i>k</i> kilometres. What is the cost of an 8-kilometre trip?</p>",
        "choices": ["21,000 som", "16,000 som", "56,000 som", "7,000 som"],
        "correct": "21,000 som",
        "explanation": "<p><strong>21,000.</strong> 5,000 + 16,000.</p>"
                       "<p><strong>16,000</strong> — chaqirish haqi unutilgan.</p>",
    },
    {
        "text": "<p>For that taxi, how many kilometres can be travelled for exactly "
                "25,000 som?</p>",
        "choices": ["10", "12.5", "8", "5"],
        "correct": "10",
        "explanation": "<p><strong>10 km.</strong> 25,000 − 5,000 = 20,000, va "
                       "20,000 ÷ 2,000 = 10.</p>"
                       "<p><strong>12.5</strong> — 5,000 ayirilmagan.</p>",
    },
]


# =====================================================================
# SAT-48 — transformations
# =====================================================================

Q_SAT48 = [
    {
        "text": "<p>How is the graph of <i>y</i> = <i>f</i>(<i>x</i>) + 4 related to "
                "<i>y</i> = <i>f</i>(<i>x</i>)?</p>",
        "choices": ["Shifted 4 units up", "Shifted 4 units down",
                    "Shifted 4 units right", "Shifted 4 units left"],
        "correct": "Shifted 4 units up",
        "explanation": "<p><strong>4 birlik yuqoriga.</strong> Qavsdan tashqaridagi "
                       "oʻzgarish vertikal va toʻgʻri ishlaydi.</p>",
    },
    {
        "text": "<p>How is the graph of <i>y</i> = <i>f</i>(<i>x</i> − 6) related to "
                "<i>y</i> = <i>f</i>(<i>x</i>)?</p>",
        "choices": ["Shifted 6 units right", "Shifted 6 units left",
                    "Shifted 6 units down", "Shifted 6 units up"],
        "correct": "Shifted 6 units right",
        "explanation": "<p><strong>6 birlik oʻngga.</strong> Qavs ichidagi oʻzgarish "
                       "gorizontal va teskari.</p>"
                       "<p>Qavs ichi nol boʻlishi uchun x = 6 kerak.</p>",
    },
    {
        "text": "<p>How is the graph of <i>y</i> = <i>f</i>(<i>x</i> + 2) related to "
                "<i>y</i> = <i>f</i>(<i>x</i>)?</p>",
        "choices": ["Shifted 2 units left", "Shifted 2 units right",
                    "Shifted 2 units up", "Reflected across the y-axis"],
        "correct": "Shifted 2 units left",
        "explanation": "<p><strong>2 birlik chapga.</strong> Plyus qavs ichida "
                       "chapga suradi.</p>",
    },
    {
        "text": "<p>Which equation reflects <i>y</i> = <i>f</i>(<i>x</i>) across the "
                "<i>y</i>-axis?</p>",
        "choices": ["y = f(−x)", "y = −f(x)", "y = f(x) − 1", "y = −f(−x)"],
        "correct": "y = f(−x)",
        "explanation": "<p><strong>f(−x).</strong> Minus qavs ichida — kirish "
                       "oʻzgaradi, grafik chap-oʻng agʻdariladi.</p>"
                       "<p><strong>−f(x)</strong> esa x oʻqiga nisbatan aks "
                       "ettiradi.</p>",
    },
    {
        "text": "<p>The point (3, 8) is on <i>y</i> = <i>f</i>(<i>x</i>). Which point "
                "is on <i>y</i> = <i>f</i>(<i>x</i>) − 5?</p>",
        "choices": ["(3, 3)", "(−2, 8)", "(8, 3)", "(3, 13)"],
        "correct": "(3, 3)",
        "explanation": "<p><strong>(3, 3).</strong> Vertikal siljish faqat y ni "
                       "oʻzgartiradi: 8 − 5.</p>",
    },
    {
        "text": "<p>The point (2, 7) is on <i>y</i> = <i>f</i>(<i>x</i>). Which point "
                "is on <i>y</i> = <i>f</i>(<i>x</i> − 3)?</p>",
        "choices": ["(5, 7)", "(−1, 7)", "(2, 4)", "(2, 10)"],
        "correct": "(5, 7)",
        "explanation": "<p><strong>(5, 7).</strong> Gorizontal siljish faqat x ni "
                       "oʻzgartiradi, va oʻngga suradi.</p>"
                       "<p><strong>(−1, 7)</strong> — chapga surilgan, ishora "
                       "teskari.</p>",
    },
    {
        "text": "<p>The point (4, −6) is on <i>y</i> = <i>f</i>(<i>x</i>). Which "
                "point is on <i>y</i> = −<i>f</i>(<i>x</i>)?</p>",
        "choices": ["(4, 6)", "(−4, −6)", "(−4, 6)", "(6, 4)"],
        "correct": "(4, 6)",
        "explanation": "<p><strong>(4, 6).</strong> Chiqishning ishorasi almashadi, "
                       "kirish oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>The point (−3, 5) is on <i>y</i> = <i>f</i>(<i>x</i>). Which "
                "point is on <i>y</i> = <i>f</i>(−<i>x</i>)?</p>",
        "choices": ["(3, 5)", "(−3, −5)", "(3, −5)", "(5, −3)"],
        "correct": "(3, 5)",
        "explanation": "<p><strong>(3, 5).</strong> Kirishning ishorasi almashadi, "
                       "chiqish oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>How is <i>y</i> = <i>f</i>(<i>x</i> + 1) − 4 related to "
                "<i>y</i> = <i>f</i>(<i>x</i>)?</p>",
        "choices": ["1 unit left and 4 units down", "1 unit right and 4 units down",
                    "1 unit left and 4 units up", "4 units left and 1 unit down"],
        "correct": "1 unit left and 4 units down",
        "explanation": "<p><strong>1 chapga, 4 pastga.</strong> Qavs ichi teskari, "
                       "tashqarisi toʻgʻri.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = <i>x</i><sup>2</sup> is shifted 3 units "
                "right. What is the new equation?</p>",
        "choices": ["y = (x − 3)²", "y = (x + 3)²", "y = x² − 3", "y = x² + 3"],
        "correct": "y = (x − 3)²",
        "explanation": "<p><strong>(x − 3)².</strong> Uchi (3, 0) ga koʻchadi "
                       "(SAT-35).</p>"
                       "<p>Ikki dars bir xil qoidani oʻrgatadi.</p>",
    },
    {
        "text": "<p>The vertex of <i>y</i> = <i>f</i>(<i>x</i>) is at (1, 2). Where is "
                "the vertex of <i>y</i> = <i>f</i>(<i>x</i> − 2) + 3?</p>",
        "choices": ["(3, 5)", "(−1, 5)", "(3, −1)", "(1, 5)"],
        "correct": "(3, 5)",
        "explanation": "<p><strong>(3, 5).</strong> x ga 2 qoʻshiladi, y ga 3.</p>"
                       "<p>Uch ham oddiy nuqta — u ham xuddi shunday koʻchadi.</p>",
    },
    {
        "text": "<p>Which transformation leaves the graph of <i>y</i> = "
                "<i>x</i><sup>2</sup> unchanged?</p>",
        "choices": ["Reflection across the y-axis", "Reflection across the x-axis",
                    "A shift 1 unit up", "A shift 1 unit right"],
        "correct": "Reflection across the y-axis",
        "explanation": "<p><strong>y oʻqiga nisbatan aks.</strong> Parabola "
                       "allaqachon shu oʻqqa nisbatan simmetrik.</p>"
                       "<p>x oʻqiga nisbatan aks esa uni agʻdaradi.</p>",
    },
    {
        "text": "<p>A profit curve <i>P</i>(<i>x</i>) is replaced by "
                "<i>P</i>(<i>x</i>) + 1,000 after a grant. What does this mean?</p>",
        "choices": ["Profit rises by 1,000 at every level of x",
                    "Profit rises by 1,000 only at the peak",
                    "The best value of x moves by 1,000",
                    "Profit is multiplied by 1,000"],
        "correct": "Profit rises by 1,000 at every level of x",
        "explanation": "<p><strong>Har bir x da 1,000 ga oshadi.</strong> Vertikal "
                       "siljish butun grafikni koʻtaradi.</p>"
                       "<p>Eng yaxshi x <b>oʻzgarmaydi</b> — faqat foyda "
                       "koʻtariladi.</p>",
    },
    {
        "text": "<p>A temperature model <i>T</i>(<i>t</i>) is replaced by "
                "<i>T</i>(<i>t</i> − 2). What has happened?</p>",
        "choices": ["Every reading now happens 2 hours later",
                    "Every reading is 2 degrees higher",
                    "Every reading happens 2 hours earlier",
                    "The temperatures are doubled"],
        "correct": "Every reading now happens 2 hours later",
        "explanation": "<p><strong>2 soat kechroq.</strong> Gorizontal siljish "
                       "vaqtga taʼsir qiladi, qiymatga emas.</p>"
                       "<p>Qavs ichidagi minus grafikni oʻngga, yaʼni kechroqqa "
                       "suradi.</p>",
    },
    {
        "text": "<p>A student says <i>y</i> = <i>f</i>(<i>x</i> − 5) moves the graph "
                "5 units left. What is correct?</p>",
        "choices": ["5 units right", "5 units left", "5 units up", "5 units down"],
        "correct": "5 units right",
        "explanation": "<p><strong>Oʻngga.</strong> Qavs ichi nol boʻlishi uchun "
                       "x = 5 kerak.</p>"
                       "<p>Bu darsdagi yagona qiyin qoida — va SAT undan har "
                       "safar tuzoq yasaydi.</p>",
    },
    {
        "text": "<p>A student says −<i>f</i>(<i>x</i>) reflects the graph across the "
                "<i>y</i>-axis. What is correct?</p>",
        "choices": ["Across the x-axis", "Across the y-axis", "Across the line y = x",
                    "No reflection at all"],
        "correct": "Across the x-axis",
        "explanation": "<p><strong>x oʻqiga nisbatan.</strong> Minus qavsdan "
                       "tashqarida — u chiqishni oʻzgartiradi.</p>"
                       "<p>Minus qayerda ekaniga qarang: ichida — y oʻqi, "
                       "tashqarisida — x oʻqi.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = <i>f</i>(<i>x</i>) has an "
                "<i>x</i>-intercept at 6. Where is the <i>x</i>-intercept of "
                "<i>y</i> = <i>f</i>(<i>x</i> + 2)?</p>",
        "choices": ["4", "8", "6", "−2"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Grafik 2 birlik chapga surildi, demak "
                       "kesishish ham chapga koʻchdi.</p>"
                       "<p>Tekshiruv: x = 4 da qavs ichi 6 boʻladi ✓</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = <i>f</i>(<i>x</i>) has a maximum value of "
                "9. What is the maximum of <i>y</i> = −<i>f</i>(<i>x</i>)?</p>",
        "choices": ["There is no maximum — it becomes a minimum of −9",
                    "9", "−9", "0"],
        "correct": "There is no maximum — it becomes a minimum of −9",
        "explanation": "<p><strong>Maksimum minimumga aylanadi.</strong> Agʻdarilgan "
                       "grafikda eng yuqori nuqta eng past nuqtaga oʻtadi.</p>"
                       "<p>Yangi grafikning eng past qiymati −9.</p>",
    },
    {
        "text": "<p>A shop's daily sales are <i>S</i>(<i>d</i>). After moving to a "
                "busier street, sales become <i>S</i>(<i>d</i>) + 40 every day. Which "
                "describes the change?</p>",
        "choices": ["A vertical shift of 40 units up",
                    "A horizontal shift of 40 days",
                    "Sales multiplied by 40",
                    "A reflection across the x-axis"],
        "correct": "A vertical shift of 40 units up",
        "explanation": "<p><strong>40 birlik yuqoriga.</strong> Har kuni bir xil "
                       "miqdor qoʻshiladi.</p>"
                       "<p>Grafikning shakli oʻzgarmaydi — u faqat "
                       "koʻtariladi.</p>",
    },
    {
        "text": "<p>A tide model <i>H</i>(<i>t</i>) is redrawn as "
                "<i>H</i>(<i>t</i>) − 1 after the measuring post is raised by 1 metre. "
                "What does the new model show?</p>",
        "choices": ["Every height reading is 1 metre lower",
                    "Every reading happens 1 hour earlier",
                    "The tide is 1 hour later",
                    "The tide range has halved"],
        "correct": "Every height reading is 1 metre lower",
        "explanation": "<p><strong>Har bir balandlik 1 metrga kam.</strong> Oʻlchov "
                       "nuqtasi koʻtarilsa, oʻsha suv sathi pastroq deb "
                       "yoziladi.</p>"
                       "<p>Vaqt umuman oʻzgarmaydi — bu vertikal siljish.</p>",
    },
]


# =====================================================================
# SAT-49 — ratios, rates, proportions   (Blok C — koʻproq interpretatsiya)
# =====================================================================

Q_SAT49 = [
    {
        "text": "<p>The ratio of cats to dogs is 2 to 3. If there are 30 animals in "
                "total, how many are dogs?</p>",
        "choices": ["18", "12", "3", "20"],
        "correct": "18",
        "explanation": "<p><strong>18.</strong> 5 qism, har biri 6 ta; 3 × 6.</p>"
                       "<p><strong>12</strong> — mushuklar soni. Savol itlarni "
                       "soʻragan.</p>",
    },
    {
        "text": "<p>Solve the proportion: 4 ÷ 9 = <i>x</i> ÷ 36</p>",
        "choices": ["16", "9", "81", "4"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> 9 ga 4 koʻpaytirildi, demak 4 ga "
                       "ham.</p>"
                       "<p>Tekshiruv: 16 ÷ 36 = 4 ÷ 9 ✓</p>",
    },
    {
        "text": "<p>A printer prints 24 pages in 3 minutes. How many pages in 8 "
                "minutes?</p>",
        "choices": ["64", "48", "8", "72"],
        "correct": "64",
        "explanation": "<p><strong>64.</strong> Daqiqasiga 8 bet, va 8 × 8.</p>"
                       "<p>Avval birlik tezlikni toping, keyin koʻpaytiring.</p>",
    },
    {
        "text": "<p>The ratio of red to blue tiles is 5 to 4. If there are 20 red "
                "tiles, how many blue tiles are there?</p>",
        "choices": ["16", "25", "4", "36"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> 5 qism 20 ta boʻlsa, bir qism 4 ta; "
                       "4 × 4 = 16.</p>"
                       "<p>Bu yerda jami berilmagan — faqat bir tomon.</p>",
    },
    {
        "text": "<p>In a survey, 3 out of every 8 people prefer tea. In a group of "
                "160, how many prefer tea?</p>",
        "choices": ["60", "48", "100", "20"],
        "correct": "60",
        "explanation": "<p><strong>60.</strong> «out of» — qismga butun: "
                       "160 ÷ 8 = 20, va 3 × 20.</p>"
                       "<p><strong>48</strong> — nisbat 3 : 8 deb olingan, yaʼni "
                       "jami 11 qism.</p>",
    },
    {
        "text": "<p>The ratio of boys to girls in a club is 4 to 7. What fraction of "
                "the club are boys?</p>",
        "choices": ["4 out of 11", "4 out of 7", "7 out of 11", "4 out of 4"],
        "correct": "4 out of 11",
        "explanation": "<p><strong>11 dan 4 tasi.</strong> Jami qismlar 4 + 7.</p>"
                       "<p><strong>4 out of 7</strong> — bu qismga qism nisbatini "
                       "ulush deb olgan javob.</p>",
    },
    {
        "text": "<p>A map uses a scale of 1 centimetre to 5 kilometres. Two towns are "
                "7 centimetres apart on the map. How far apart are they really?</p>",
        "choices": ["35 kilometres", "12 kilometres", "1.4 kilometres",
                    "5 kilometres"],
        "correct": "35 kilometres",
        "explanation": "<p><strong>35 km.</strong> 7 × 5.</p>"
                       "<p><strong>1.4</strong> — boʻlingan; xarita masofasi "
                       "haqiqiy masofadan kichik boʻlgani uchun koʻpaytirish "
                       "kerak.</p>",
    },
    {
        "text": "<p>A worker paints 3 rooms in 5 hours. At this rate, how long does "
                "12 rooms take?</p>",
        "choices": ["20 hours", "15 hours", "4 hours", "60 hours"],
        "correct": "20 hours",
        "explanation": "<p><strong>20 soat.</strong> Xonalar 4 barobar oshdi, demak "
                       "vaqt ham 4 barobar.</p>"
                       "<p>Tekshiruv: 3 ÷ 5 = 12 ÷ 20 ✓</p>",
    },
    {
        "text": "<p>The ratio of flour to sugar in a recipe is 5 to 2. If a baker "
                "uses 15 cups of flour, how much sugar is needed?</p>",
        "choices": ["6 cups", "30 cups", "12 cups", "3 cups"],
        "correct": "6 cups",
        "explanation": "<p><strong>6 stakan.</strong> Un 3 barobar oshdi (5 dan 15 "
                       "ga), demak shakar ham.</p>"
                       "<p>Shakar undan kam boʻlishi kerak — 30 mantiqan "
                       "notoʻgʻri.</p>",
    },
    {
        "text": "<p>A car uses 6 litres of fuel per 100 kilometres. How much fuel for "
                "250 kilometres?</p>",
        "choices": ["15 litres", "12 litres", "24 litres", "1,500 litres"],
        "correct": "15 litres",
        "explanation": "<p><strong>15 litr.</strong> 250 ÷ 100 = 2.5, va "
                       "6 × 2.5.</p>"
                       "<p>Birlikni oʻqing: «per 100 kilometres», bir kilometrga "
                       "emas.</p>",
    },
    {
        "text": "<p>The ratio of adults to children at an event is 3 to 5, and there "
                "are 120 people. How many more children than adults are there?</p>",
        "choices": ["30", "75", "45", "2"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> 8 qism, har biri 15: 45 kattalar va "
                       "75 bolalar; farqi 30.</p>"
                       "<p><strong>75</strong> — bolalar soni. «How many more» "
                       "farqni soʻraydi.</p>",
    },
    {
        "text": "<p>A recipe for 4 people needs 600 grams of rice. How much rice for "
                "10 people?</p>",
        "choices": ["1,500 grams", "1,200 grams", "240 grams", "6,000 grams"],
        "correct": "1,500 grams",
        "explanation": "<p><strong>1,500 gramm.</strong> Bir kishiga 150 gramm, va "
                       "10 × 150.</p>"
                       "<p>Yoki proporsiya: 600 ÷ 4 = x ÷ 10.</p>",
    },
    {
        "text": "<p>A shop sells pens at 3 for 12,000 som. What does one pen "
                "cost?</p>",
        "choices": ["4,000 som", "36,000 som", "9,000 som", "12,000 som"],
        "correct": "4,000 som",
        "explanation": "<p><strong>4,000 som.</strong> 12,000 ÷ 3.</p>"
                       "<p>Bir birlikka narx — «unit rate» deyiladi va SAT uni "
                       "juda koʻp soʻraydi.</p>",
    },
    {
        "text": "<p>Machine A makes 40 parts an hour and machine B makes 60. What is "
                "the ratio of A's output to B's, in simplest form?</p>",
        "choices": ["2 to 3", "3 to 2", "40 to 60", "4 to 6"],
        "correct": "2 to 3",
        "explanation": "<p><strong>2 : 3.</strong> Ikkalasini 20 ga qisqartiring.</p>"
                       "<p>40 : 60 ham toʻgʻri nisbat, lekin savol «simplest form» "
                       "degan.</p>",
    },
    {
        "text": "<p>A student reads 'the ratio of boys to girls is 2 to 3' as '2 boys "
                "and 3 girls'. In a class of 25, what is the correct number of "
                "girls?</p>",
        "choices": ["15", "3", "10", "5"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> 5 qism, har biri 5 ta; 3 × 5.</p>"
                       "<p>Nisbat sonlarni emas, <b>ulushni</b> beradi.</p>",
    },
    {
        "text": "<p>A student solves '2 cups of oil per 5 cups of water; how much oil "
                "for 20 cups of water?' as 50 cups. What is correct?</p>",
        "choices": ["8 cups", "50 cups", "10 cups", "4 cups"],
        "correct": "8 cups",
        "explanation": "<p><strong>8 stakan.</strong> Suv 4 barobar oshdi, demak "
                       "yogʻ ham: 2 × 4.</p>"
                       "<p>Oʻquvchi proporsiyani teskari yozgan — yogʻ suvdan koʻp "
                       "chiqib qolgan.</p>",
    },
    {
        "text": "<p>Three workers build a wall in 8 days. At the same rate, how long "
                "would 4 workers take?</p>",
        "choices": ["6 days", "10.7 days", "8 days", "12 days"],
        "correct": "6 days",
        "explanation": "<p><strong>6 kun.</strong> Jami ish 24 ishchi-kun; "
                       "24 ÷ 4 = 6.</p>"
                       "<p>Bu <b>teskari</b> proporsiya: ishchi koʻpaysa, vaqt "
                       "kamayadi.</p>",
    },
    {
        "text": "<p>The ratio of A to B is 3 to 4, and the ratio of B to C is 4 to 5. "
                "What is the ratio of A to C?</p>",
        "choices": ["3 to 5", "3 to 4", "4 to 5", "12 to 20"],
        "correct": "3 to 5",
        "explanation": "<p><strong>3 : 5.</strong> B ikkala nisbatda ham 4 — demak "
                       "zanjir toʻgʻridan-toʻgʻri ulanadi: 3 : 4 : 5.</p>"
                       "<p><strong>12 to 20</strong> — bu ham 3 : 5, lekin "
                       "qisqartirilmagan.</p>",
    },
    {
        "text": "<p>A tank fills at 45 litres per hour. A gardener needs 30 litres. "
                "How many minutes does that take?</p>",
        "choices": ["40 minutes", "30 minutes", "45 minutes", "67 minutes"],
        "correct": "40 minutes",
        "explanation": "<p><strong>40 daqiqa.</strong> Daqiqasiga 0.75 litr, va "
                       "30 ÷ 0.75 = 40.</p>"
                       "<p>Yoki: 30 ÷ 45 = 2/3 soat, va 2/3 × 60 = 40.</p>",
    },
    {
        "text": "<p>A bus travels 180 kilometres in 2.5 hours. A train covers the same "
                "distance in 1.5 hours. What is the ratio of the bus's speed to the "
                "train's, in simplest form?</p>",
        "choices": ["3 to 5", "5 to 3", "2.5 to 1.5", "180 to 180"],
        "correct": "3 to 5",
        "explanation": "<p><strong>3 : 5.</strong> Avtobus 72 km/soat, poyezd 120; "
                       "72 : 120 = 3 : 5.</p>"
                       "<p>Masofa bir xil boʻlgani uchun tezliklar nisbati "
                       "vaqtlarning teskari nisbati: 1.5 : 2.5 = 3 : 5.</p>",
    },
]


# =====================================================================
# SAT-50 — unit conversions
# =====================================================================

Q_SAT50 = [
    {
        "text": "<p>Convert 4 kilometres to metres.</p>",
        "choices": ["4,000", "400", "0.004", "40"],
        "correct": "4,000",
        "explanation": "<p><strong>4,000.</strong> Katta birlikdan kichigiga — son "
                       "oshadi.</p>",
    },
    {
        "text": "<p>Convert 240 minutes to hours.</p>",
        "choices": ["4", "240", "14,400", "40"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 240 ÷ 60.</p>"
                       "<p><strong>14,400</strong> — koʻpaytirilgan; kichik "
                       "birlikdan kattasiga oʻtganda son kamayadi.</p>",
    },
    {
        "text": "<p>Convert 3.5 metres to centimetres.</p>",
        "choices": ["350", "35", "0.035", "3,500"],
        "correct": "350",
        "explanation": "<p><strong>350.</strong> 3.5 × 100.</p>",
    },
    {
        "text": "<p>Convert 2,500 grams to kilograms.</p>",
        "choices": ["2.5", "250", "25", "2,500,000"],
        "correct": "2.5",
        "explanation": "<p><strong>2.5.</strong> 2,500 ÷ 1,000.</p>",
    },
    {
        "text": "<p>A car travels 72 kilometres per hour. What is this in metres per "
                "second?</p>",
        "choices": ["20", "72", "1.2", "259"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> 72,000 ÷ 3,600.</p>"
                       "<p><strong>1.2</strong> — faqat daqiqaga aylantirilgan.</p>",
    },
    {
        "text": "<p>A runner moves at 30 miles per hour. What is this in feet per "
                "second? (1 mile = 5,280 feet)</p>",
        "choices": ["44", "88", "30", "158,400"],
        "correct": "44",
        "explanation": "<p><strong>44.</strong> 30 × 5,280 = 158,400 fut soatiga, "
                       "va ÷ 3,600.</p>"
                       "<p><strong>158,400</strong> — faqat birinchi almashtirish "
                       "qilingan.</p>",
    },
    {
        "text": "<p>Which expression converts <i>x</i> kilometres per hour to metres "
                "per second?</p>",
        "choices": ["x × 1,000 ÷ 3,600", "x × 3,600 ÷ 1,000", "x × 1,000 × 3,600",
                    "x ÷ 1,000 ÷ 3,600"],
        "correct": "x × 1,000 ÷ 3,600",
        "explanation": "<p><strong>x × 1,000 ÷ 3,600.</strong> Kilometr metrga "
                       "koʻpayadi, soat sekundga boʻlinadi.</p>"
                       "<p>Birliklarni yozing — qaysi tomonga qoʻyish oʻz-oʻzidan "
                       "koʻrinadi.</p>",
    },
    {
        "text": "<p>How many square centimetres are in 5 square metres?</p>",
        "choices": ["50,000", "500", "5,000", "50"],
        "correct": "50,000",
        "explanation": "<p><strong>50,000.</strong> Har kvadrat metrda 10,000, "
                       "chunki koeffitsient ikki marta qoʻllanadi.</p>"
                       "<p><strong>500</strong> — 100 ga bir marta "
                       "koʻpaytirilgan.</p>",
    },
    {
        "text": "<p>How many cubic centimetres are in 2 cubic metres?</p>",
        "choices": ["2,000,000", "200", "20,000", "2,000"],
        "correct": "2,000,000",
        "explanation": "<p><strong>2,000,000.</strong> Hajmda koeffitsient uch marta: "
                       "100 × 100 × 100.</p>",
    },
    {
        "text": "<p>A tap fills 5 litres per minute. How many litres in 3 hours?</p>",
        "choices": ["900", "15", "180", "300"],
        "correct": "900",
        "explanation": "<p><strong>900.</strong> 5 × 60 × 3.</p>"
                       "<p><strong>15</strong> — daqiqa soatga aylantirilmagan.</p>",
    },
    {
        "text": "<p>A recipe needs 250 millilitres of milk per person. How many litres "
                "for 12 people?</p>",
        "choices": ["3", "3,000", "30", "0.3"],
        "correct": "3",
        "explanation": "<p><strong>3 litr.</strong> 3,000 millilitr, va "
                       "3,000 ÷ 1,000.</p>"
                       "<p>Savol litrni soʻragan — javobning birligini "
                       "tekshiring.</p>",
    },
    {
        "text": "<p>A field is 200 metres by 150 metres. What is its area in "
                "hectares? (1 hectare = 10,000 square metres)</p>",
        "choices": ["3", "30", "300", "0.3"],
        "correct": "3",
        "explanation": "<p><strong>3 gektar.</strong> 30,000 m², va "
                       "30,000 ÷ 10,000.</p>"
                       "<p>Avval yuzani hisoblang, keyin almashtiring.</p>",
    },
    {
        "text": "<p>A phone charges at 2% per minute. How long to go from 0 to "
                "100%?</p>",
        "choices": ["50 minutes", "2 hours", "100 minutes", "20 minutes"],
        "correct": "50 minutes",
        "explanation": "<p><strong>50 daqiqa.</strong> 100 ÷ 2.</p>"
                       "<p>Bu ham nisbat: foiz har daqiqaga.</p>",
    },
    {
        "text": "<p>A pipe delivers 12 litres in 45 minutes. How many litres per "
                "hour?</p>",
        "choices": ["16", "9", "12", "540"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> 12 × 60 ÷ 45 = 720 ÷ 45.</p>"
                       "<p><strong>9</strong> — kasr teskari yozilgan: "
                       "12 × 45 ÷ 60.</p>",
    },
    {
        "text": "<p>A student converts 90 kilometres per hour to metres per second by "
                "computing 90 × 3,600 ÷ 1,000 = 324. What is correct?</p>",
        "choices": ["25", "324", "90", "2.5"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Kasrlar teskari yozilgan.</p>"
                       "<p>Aql bilan tekshiring: sekund soatdan kichik, demak "
                       "sekunddagi masofa kichikroq boʻlishi kerak.</p>",
    },
    {
        "text": "<p>A student says 1 square metre is 100 square centimetres. What is "
                "correct?</p>",
        "choices": ["10,000", "100", "1,000", "1,000,000"],
        "correct": "10,000",
        "explanation": "<p><strong>10,000.</strong> Yuzada koeffitsient ikki marta "
                       "qoʻllanadi.</p>"
                       "<p>Chizib koʻring: 100 ta 100 ta katakcha.</p>",
    },
    {
        "text": "<p>A tank holds 3 cubic metres of water. A pump removes 50 litres a "
                "minute. How long to empty it? (1 cubic metre = 1,000 litres)</p>",
        "choices": ["60 minutes", "6 minutes", "600 minutes", "150 minutes"],
        "correct": "60 minutes",
        "explanation": "<p><strong>60 daqiqa.</strong> 3,000 litr ÷ 50.</p>"
                       "<p>Almashtirish birinchi qadam — bir xil birlikda "
                       "ishlang.</p>",
    },
    {
        "text": "<p>A printer uses 4 millilitres of ink per 50 pages. How many litres "
                "for 25,000 pages?</p>",
        "choices": ["2", "2,000", "0.2", "20"],
        "correct": "2",
        "explanation": "<p><strong>2 litr.</strong> 25,000 ÷ 50 = 500 marta, "
                       "500 × 4 = 2,000 ml = 2 litr.</p>"
                       "<p>Ikkita qadam: nisbat, keyin birlik.</p>",
    },
    {
        "text": "<p>A shop sells cloth at 45,000 som per metre. What is the cost of "
                "250 centimetres?</p>",
        "choices": ["112,500 som", "11,250,000 som", "45,000 som", "18,000 som"],
        "correct": "112,500 som",
        "explanation": "<p><strong>112,500 som.</strong> 250 sm = 2.5 m, va "
                       "2.5 × 45,000.</p>"
                       "<p>Santimetrni metrga aylantirmasdan hisoblash javobni "
                       "100 barobar buzadi.</p>",
    },
    {
        "text": "<p>A lorry burns 30 litres of fuel per 100 kilometres. Fuel costs "
                "9,000 som a litre. What is the fuel cost of a 450-kilometre trip?</p>",
        "choices": ["1,215,000 som", "135,000 som", "270,000 som", "12,150,000 som"],
        "correct": "1,215,000 som",
        "explanation": "<p><strong>1,215,000 som.</strong> 450 ÷ 100 = 4.5, "
                       "4.5 × 30 = 135 litr, 135 × 9,000.</p>"
                       "<p><strong>135,000</strong> — litr soni narx deb "
                       "olingan; oxirgi qadam qilinmagan.</p>",
    },
]


# =====================================================================
# Testlar
# =====================================================================

PRACTICES = [
    {
        "title":       "SAT-46 Practice: Compound Interest and Percent Growth",
        "description": "20 ta SAT uslubidagi savol — oddiy va murakkab foiz, davrni "
                       "boʻlish va koʻrsatkichni koʻpaytirish.",
        "tutorial":    "SAT-46:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT46,
    },
    {
        "title":       "SAT-47 Practice: Functions — Domain, Range, and Evaluation",
        "description": "20 ta SAT uslubidagi savol — f(a) ni hisoblash, aniqlanish va "
                       "qiymatlar sohasi, kontekstdagi cheklovlar.",
        "tutorial":    "SAT-47:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT47,
    },
    {
        "title":       "SAT-48 Practice: Function Transformations — Shifts and Reflections",
        "description": "20 ta SAT uslubidagi savol — gorizontal va vertikal siljish, "
                       "ikki aks ettirish, nuqtani kuzatish.",
        "tutorial":    "SAT-48:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT48,
    },
    {
        "title":       "SAT-49 Practice: Ratios, Rates, and Proportions",
        "description": "20 ta SAT uslubidagi savol — nisbat qismlari, «to» va «out "
                       "of» farqi, proporsiya va birlik tezlik.",
        "tutorial":    "SAT-49:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT49,
    },
    {
        "title":       "SAT-50 Practice: Unit Conversions and Dimensional Analysis",
        "description": "20 ta SAT uslubidagi savol — birliklarni qisqartirish, "
                       "ketma-ket almashtirish, yuza va hajm koeffitsientlari.",
        "tutorial":    "SAT-50:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT50,
    },
]
