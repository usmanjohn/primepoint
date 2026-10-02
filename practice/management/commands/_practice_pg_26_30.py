# -*- coding: utf-8 -*-
"""Prime GMAT mashqlar — GMAT-26 … GMAT-30: Data Sufficiency (100 questions).

Every question here is Data Sufficiency, so every question carries "fixed_order": True —
the five verdicts appear A–E in the written order, exactly as on the real test
(PracticeQuestion.fixed_order, migration 0007). Questions in English, explanations in Uzbek;
each explanation opens with the verdict's own text in bold, never a letter.

Import:
    python manage.py import_practices practice/management/commands/_practice_pg_26_30.py \\
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

DS = [
    "Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.",
    "Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.",
    "BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.",
    "EACH statement ALONE is sufficient.",
    "Statements (1) and (2) TOGETHER are NOT sufficient.",
]


def ds(question, s1, s2, key, why):
    """One Data Sufficiency item. `key` is A–E; `why` is the Uzbek reasoning (HTML)."""
    verdict = DS["ABCDE".index(key)]
    return {
        "text": f"<p>{question}</p><p>(1) {s1}</p><p>(2) {s2}</p>",
        "choices": list(DS),
        "correct": verdict,
        "fixed_order": True,
        "explanation": f"<p><strong>{verdict}</strong></p>{why}",
    }


X, Y = "<i>x</i>", "<i>y</i>"
SQ = "<sup>2</sup>"

# =====================================================================
# GMAT-26 — the section and DS basics
# =====================================================================
Q26 = [
    ds(f"What is the value of {X}?", f"{X} + 7 = 12", f"2{X} = 10", "D",
       "<p>Ikkalasi ham <i>x</i> = 5 beradi.</p><p>Har birini alohida tekshirish kerak — birgalikda ishlatish shart emas.</p>"),
    ds(f"What is the value of {X}?", f"{X}{SQ} = 25", f"{X} &gt; 0", "C",
       "<p>(1): 5 yoki −5. (2): istalgan musbat son. Birga: 5.</p><p>(1) yolgʻiz yetarli deb oʻylash — manfiy ildizni unutish.</p>"),
    ds("If <i>n</i> is an integer, what is the value of <i>n</i>?", "<i>n</i> is a prime number.", "20 &lt; <i>n</i> &lt; 30", "E",
       "<p>Birga: 23 yoki 29 — ikki qiymat.</p><p>Birga yetarli deb belgilashdan oldin oraliqdagi barcha tub sonlarni sanang.</p>"),
    ds("How many employees does a firm have?", "Exactly 60% of the employees, 42 people, work in sales.", "28 of the employees do not work in sales.", "A",
       "<p>(1): 42 ÷ 0.6 = 70. (2): sotuvdagilar soni nomaʼlum.</p><p>(2) ni tekshirishda (1) dagi 42 ni ishlatmang.</p>"),
    ds("What is the price of one ticket?", "4 tickets cost $48.", "6 tickets cost $72.", "D",
       "<p>Ikkalasi ham $12 beradi (barcha chiptalar bir xil narxda).</p><p>Ikkala maʼlumot bir xil javob berishi — D ning belgisi.</p>"),
    ds(f"What is the value of {Y}?", f"{Y} = 2{X}", f"{X} = 5", "C",
       "<p>(1): <i>x</i> nomaʼlum. (2): <i>y</i> haqida hech narsa yoʻq. Birga: 10.</p><p>Har biri yolgʻiz yetmaydi, birga yetadi.</p>"),
    ds("What is the value of <i>a</i> + <i>b</i>?", "<i>a</i> − <i>b</i> = −1", "2<i>a</i> + 2<i>b</i> = 14", "B",
       "<p>(2): <i>a</i> + <i>b</i> = 7. (1): faqat ayirma.</p><p>Soʻralgan ifodani bevosita beradigan maʼlumotni qidiring.</p>"),
    ds("What is the value of <i>a</i> + <i>b</i>?", "<i>a</i> + <i>b</i> + <i>c</i> = 10", "<i>c</i> is positive.", "E",
       "<p>Birga ham <i>c</i> aniq emas — <i>a</i> + <i>b</i> = 10 − <i>c</i> har xil.</p><p>«Musbat» — qiymat emas, oraliq.</p>"),
    ds(f"What is the value of {X}?", f"3{X} − 2 = 2{X} + 5", f"{X}/7 = 1", "D",
       "<p>Ikkalasi ham <i>x</i> = 7.</p><p>Chiziqli tenglama — bitta yechim; hisoblash shart emas.</p>"),
    ds(f"What is the value of {X}?", f"{X}({X} − 4) = 0", f"{X} is positive.", "C",
       "<p>(1): 0 yoki 4. Birga: 4.</p><p>Nol koʻpaytma ikki qiymat beradi.</p>"),
    ds("How many kilometers did a van travel on a trip?", "The trip took 3 hours.", "The van used 18 liters of fuel.", "E",
       "<p>Tezlik ham, sarf normasi ham nomaʼlum.</p><p>Masofa uchun tezlik × vaqt yoki litr ÷ sarf kerak.</p>"),
    ds("What was a company's profit in 2025?", "Its revenue in 2025 was $2 million.", "Its costs in 2025 were 80% of its revenue.", "C",
       "<p>Birga: 2 − 1.6 = $0.4 million.</p><p>(2) yolgʻiz — faqat foiz, summa yoʻq.</p>"),
    ds("How many shirts did a shop sell last week?", "Each shirt was sold for between $15 and $25.", "The shop's revenue from shirts was $1,800, and every shirt was sold for $20.", "B",
       "<p>(2): 1,800 ÷ 20 = 90. (1): narx oraligʻi — son emas.</p><p>Oraliq qiymat yagona javob bermaydi.</p>"),
    ds("What percent of a firm's employees are managers?", "The firm has 12 managers and 48 other employees.", "For every manager the firm has 4 other employees.", "D",
       "<p>(1): 12 ÷ 60 = 20%. (2): 1 ÷ 5 = 20%.</p><p>Foiz soʻralganda nisbat yetarli — jami son shart emas.</p>"),
    ds("What is the price of a coffee?", "A coffee and a cake cost $7, and a cake costs $3.", "Two coffees cost $8.", "D",
       "<p>Ikkalasi ham $4.</p><p>(1) ichida ikkala son bor — u yolgʻiz yetarli.</p>"),
    ds(f"What is the value of {X}?", f"{X}{SQ} = 4{X}", f"{X} − 4 = 0", "B",
       "<p>(1): 0 yoki 4. (2): 4.</p><p><i>x</i> ga boʻlib, 0 ni yoʻqotmang.</p>"),
    ds(f"What is the average (arithmetic mean) of {X} and {Y}?", f"{X} + {Y} = 18", f"{X} − {Y} = 4", "A",
       "<p>(1): oʻrtacha 9. (2): yigʻindi nomaʼlum.</p><p>Oʻrtacha uchun faqat yigʻindi kerak.</p>"),
    ds("What is the value of <i>n</i>?", "<i>n</i> is an even prime number.", f"<i>n</i>{SQ} = 4", "A",
       "<p>(1): yagona juft tub son — 2. (2): 2 yoki −2.</p><p>Kvadrat ikki ishorani beradi.</p>"),
    ds("A café sold 50 drinks, each a latte or a tea. How many lattes did it sell?", "Lattes cost $4 each and teas cost $3 each.", "The café's revenue from the 50 drinks was $180.", "C",
       "<p>Birga: 4<i>l</i> + 3(50 − <i>l</i>) = 180 → <i>l</i> = 30.</p><p>(2) yolgʻiz — narxlar nomaʼlum.</p>"),
    ds("How old is Aziz now?", "Aziz is 3 times as old as his son.", "In 10 years Aziz will be twice as old as his son.", "C",
       "<p>Birga: 3<i>s</i> + 10 = 2(<i>s</i> + 10) → <i>s</i> = 10, Aziz 30.</p><p>Har biri yolgʻiz — bitta tenglama, ikki nomaʼlum.</p>"),
]

# =====================================================================
# GMAT-27 — value questions
# =====================================================================
Q27 = [
    ds(f"What is the value of {X}?", f"5{X} − 3 = 17", f"{X}{SQ} = 16", "A",
       "<p>(1): 4. (2): 4 yoki −4.</p><p>Juft daraja — ikki ishora.</p>"),
    ds(f"What is the value of {X}?", f"{X}{SQ} = 4", f"{X}<sup>3</sup> = −8", "B",
       "<p>(2): toq daraja ishorani saqlaydi — −2. (1): ±2.</p><p>Toq va juft darajani farqlang.</p>"),
    ds(f"What is the value of {Y}?", f"3{Y} + 2{X} = 20", f"{X} = 4", "C",
       "<p>Birga: 3<i>y</i> = 12, <i>y</i> = 4.</p><p>Har biri yolgʻiz yetmaydi.</p>"),
    ds(f"What is the value of {X} + {Y}?", f"{X} + 2{Y} = 10", f"2{X} + {Y} = 14", "C",
       "<p>Birga qoʻshsak: 3(<i>x</i> + <i>y</i>) = 24 → 8.</p><p>Har biri yolgʻiz — yigʻindini bermaydi.</p>"),
    ds(f"What is the value of {X} − {Y}?", f"3{X} − 3{Y} = 12", f"{X} + {Y} = 10", "A",
       "<p>(1): <i>x</i> − <i>y</i> = 4.</p><p>Ifodani bevosita beradigan tenglamani koʻring.</p>"),
    ds(f"What is the value of {X}?", f"{X} + {Y} = 10", f"2{X} + 2{Y} = 20", "E",
       "<p>(2) — (1) ning ikki baravari; birga ham bitta tenglama.</p><p>Nusxa tenglama yangi maʼlumot emas.</p>"),
    ds("What is the value of 2<i>a</i> + 6<i>b</i>?", "<i>a</i> = 1", "<i>a</i> + 3<i>b</i> = 7", "B",
       "<p>(2) × 2 = 14. (1): <i>b</i> nomaʼlum.</p><p><i>a</i> va <i>b</i> ni alohida topish shart emas.</p>"),
    ds("What is the value of <i>n</i>?", f"<i>n</i>{SQ} = 49", "<i>n</i> is an integer.", "E",
       "<p>Birga: 7 yoki −7 — ikkalasi ham butun.</p><p>«Butun» cheklovi bu yerda hech narsani kesmaydi.</p>"),
    ds(f"What is the value of {X}?", f"|{X} − 2| = 5", f"{X} is negative.", "C",
       "<p>(1): 7 yoki −3. Birga: −3.</p><p>Modul — ikki nuqta.</p>"),
    ds(f"What is the value of {X}?", f"{X}{SQ} = 81", f"√{X} = 3", "B",
       "<p>(2): <i>x</i> = 9. (1): ±9.</p><p>Ildiz belgisi faqat manfiy boʻlmagan qiymatni bildiradi.</p>"),
    ds(f"If {Y} ≠ 0, what is the value of {X}/{Y}?", f"2{X} = 3{Y}", f"{X} + {Y} = 10", "A",
       "<p>(1): <i>x</i>/<i>y</i> = 3/2. (2): nisbat aniq emas.</p><p>Nisbat uchun qiymatlar shart emas.</p>"),
    ds(f"What is the value of {X}?", f"{X}{SQ} − 6{X} + 9 = 0", f"2{X} − 1 = 5", "D",
       "<p>(1): (<i>x</i> − 3)<sup>2</sup> = 0 → 3. (2): 3.</p><p>Toʻla kvadrat — bitta ildiz.</p>"),
    ds("What is the price of one pen?", "3 pens and 2 notebooks cost $19.", "2 pens and 3 notebooks cost $21.", "C",
       "<p>Birga: ikki mustaqil tenglama → ruchka $3.</p><p>Har biri yolgʻiz — ikki nomaʼlum.</p>"),
    ds("A phone plan charges a fixed monthly fee plus a charge for each gigabyte. What is the monthly fee?", "Each gigabyte costs $5.", "4 GB cost $30 in a month and 8 GB cost $50.", "B",
       "<p>(2): 4 GB farqi $20 → $5 dan; 30 − 20 = $10. (1): fee nomaʼlum.</p><p>Ikki nuqta — ikkala nomaʼlumni beradi.</p>"),
    ds("A museum had 300 visitors, each an adult or a child. How many adults visited?", "Children made up 40% of the visitors.", "There were 60 more adults than children.", "D",
       "<p>(1): 0.6 × 300 = 180. (2): <i>a</i> − <i>c</i> = 60, <i>a</i> + <i>c</i> = 300 → 180.</p><p>Savoldagi «300» ikkala maʼlumotga ham qoʻshiladi.</p>"),
    ds("What was the price of a jacket before a discount?", "After a 20% discount the jacket cost $64.", "The discount saved the buyer $16.", "A",
       "<p>(1): 64 ÷ 0.8 = 80. (2): chegirma foizi nomaʼlum.</p><p>Birga ham toʻgʻri, lekin (1) oʻzi yetarli.</p>"),
    ds(f"What is the value of {X}{Y}?", f"({X} + {Y}){SQ} = 25", f"{X}{SQ} + {Y}{SQ} = 13", "C",
       "<p>Birga: 2<i>xy</i> = 25 − 13 → <i>xy</i> = 6.</p><p>Har biri yolgʻiz — bitta tenglama.</p>"),
    ds(f"What is the value of {X}?", f"{X}{SQ} + {X} = 6", f"{X} is an integer.", "E",
       "<p>Birga: 2 yoki −3 — ikkalasi ham butun.</p><p>Ikki ildizni topib, cheklov ularni kesishini tekshiring.</p>"),
    ds("A rental company charges only a fixed amount per day. What does a 5-day rental cost?", "The daily rate is $40.", "A 3-day rental costs $120.", "D",
       "<p>(1): $200. (2): kunlik $40 → $200.</p><p>Savoldagi «only a fixed amount per day» (2) ni yetarli qiladi.</p>"),
    ds("A sum of money was divided between Bekzod and Laylo. How much did Laylo receive?", "Bekzod received $200 more than Laylo.", "Bekzod received 3/5 of the total.", "C",
       "<p>Birga: ayirma — jamining 1/5 qismi, $200 → jami $1,000, Laylo $400.</p><p>Har biri yolgʻiz — summa nomaʼlum.</p>"),
]

# =====================================================================
# GMAT-28 — yes/no questions
# =====================================================================
Q28 = [
    ds(f"Is {X} &gt; 5?", f"{X} &gt; 7", f"{X} &gt; 3", "A",
       "<p>(1): har doim «ha». (2): 4 — yoʻq, 6 — ha.</p><p>Bitta «ha» misol yetarli emas.</p>"),
    ds("If <i>n</i> is an integer, is <i>n</i> even?", "<i>n</i> + 3 is odd.", "3<i>n</i> is even.", "D",
       "<p>(1): toq − 3 = juft. (2): 3<i>n</i> juft → <i>n</i> juft.</p><p>Juft/toq qoidalari (GMAT-4).</p>"),
    ds(f"Is {X} &gt; 0?", f"{X}{SQ} &gt; 0", f"{X}<sup>3</sup> &gt; 0", "B",
       "<p>(2): toq daraja — ha. (1): −2 ham qanoatlantiradi.</p><p>Juft daraja ishorani yashiradi.</p>"),
    ds(f"Is {X}{Y} &gt; 0?", f"{X} &gt; 0", f"{Y} &lt; 0", "C",
       "<p>Birga: har doim manfiy — aniq «yoʻq».</p><p>Aniq «yoʻq» ham yetarli.</p>"),
    ds("If <i>n</i> is a positive integer, is <i>n</i> divisible by 6?", "<i>n</i> is divisible by 3.", "<i>n</i> is divisible by 2.", "C",
       "<p>Birga: 2 ga ham, 3 ga ham — 6 ga boʻlinadi.</p><p>Har biri yolgʻiz — 3 yoki 4 kabi qarshi misollar.</p>"),
    ds(f"Is {X} &lt; 0?", f"{X} + 2 &lt; 0", f"{X}{SQ} = 9", "A",
       "<p>(1): <i>x</i> &lt; −2 — ha. (2): ±3.</p><p>Modul/kvadrat ikki tomonni beradi.</p>"),
    ds("If <i>n</i> is an integer, is <i>n</i> odd?", f"<i>n</i>{SQ} is odd.", "2<i>n</i> is even.", "A",
       "<p>(1): toq kvadrat — toq son. (2): har qanday butun son uchun toʻgʻri.</p><p>Doim toʻgʻri boʻlgan maʼlumot — maʼlumot emas.</p>"),
    ds(f"Is {X} = {Y}?", f"{X}{SQ} = {Y}{SQ}", f"{X} − {Y} = 0", "B",
       "<p>(2): ha. (1): 2 va −2 ham mos.</p><p>Kvadratlar teng — sonlar teng emas boʻlishi mumkin.</p>"),
    ds("Is <i>a</i> &gt; <i>b</i>?", "<i>a</i> − <i>b</i> = 3", "<i>a</i> = <i>b</i> + 3", "D",
       "<p>Ikkalasi bir xil maʼlumot va har biri «ha».</p><p>D — har biri yolgʻiz yetarli.</p>"),
    ds("If <i>p</i> is a positive integer, is <i>p</i> prime?", "<i>p</i> is odd.", "20 &lt; <i>p</i> &lt; 23", "B",
       "<p>(2): 21 yoki 22 — ikkalasi tub emas, aniq «yoʻq». (1): 3 — ha, 9 — yoʻq.</p><p>Aniq «yoʻq» — yetarli.</p>"),
    ds("A company had positive revenue last year. Did it make a profit?", "Its revenue was $500,000.", "Its costs were 90% of its revenue.", "B",
       "<p>(2): xarajat tushumdan kam — har doim «ha». (1): xarajat nomaʼlum.</p><p>Savoldagi «positive revenue» (2) ni yetarli qiladi.</p>"),
    ds("Is the average monthly salary at a firm above $3,000?", "The firm's total monthly salaries are $40,000.", "The firm has more than 10 employees.", "E",
       "<p>Birga: 11 kishi — 3,636 (ha), 14 kishi — 2,857 (yoʻq).</p><p>«More than» — son emas.</p>"),
    ds("Every customer of a shop bought online, in the store, or both. Did more than half of the customers buy online?", "45% of the customers bought only online, and 20% bought both online and in the store.", "35% of the customers bought only in the store.", "D",
       "<p>(1): 65% onlayn. (2): 100 − 35 = 65% onlayn.</p><p>Savoldagi shart (2) ni yetarli qiladi.</p>"),
    ds("Will a project go over its budget?", "$80,000 has been spent on the project so far.", "The budget is $100,000, and the remaining work will cost $25,000.", "C",
       "<p>Birga: 80 + 25 = 105 &gt; 100 — ha.</p><p>Har biri yolgʻiz — bitta sonsiz.</p>"),
    ds(f"Is {X} &gt; {Y}?", f"{X}{SQ} &gt; {Y}{SQ}", f"{X} &gt; 0", "C",
       "<p>Birga: <i>x</i> &gt; |<i>y</i>| ≥ <i>y</i> — ha.</p><p>(1) yolgʻiz: −3 va 1 — yoʻq.</p>"),
    ds("If <i>n</i> is an integer, is <i>n</i> &gt; 0?", f"<i>n</i>{SQ} &gt; <i>n</i>", f"<i>n</i><sup>3</sup> &lt; <i>n</i>{SQ}", "B",
       "<p>(2): <i>n</i><sup>2</sup>(<i>n</i> − 1) &lt; 0 → <i>n</i> manfiy — aniq «yoʻq». (1): −1 ham, 5 ham.</p><p>Aniq «yoʻq» — yetarli.</p>"),
    ds(f"Is |{X}| &lt; 3?", f"{X}{SQ} &lt; 9", f"|{X} − 1| &lt; 2", "D",
       "<p>(1): −3 &lt; <i>x</i> &lt; 3. (2): −1 &lt; <i>x</i> &lt; 3 — ikkalasida «ha».</p><p>Oraliqlarni chizib solishtiring.</p>"),
    ds(f"Is {X}{Y}<i>z</i> &gt; 0?", f"{X}, {Y} and <i>z</i> are all negative.", f"{X}{Y} &gt; 0", "A",
       "<p>(1): uchta manfiy — manfiy, aniq «yoʻq». (2): <i>z</i> nomaʼlum.</p><p>Aniq «yoʻq» — yetarli.</p>"),
    ds("A shop must sell at least 500 units in June to break even. Did it break even in June?", "Its June sales were 40% higher than its May sales.", "Its May sales were more than 300 units.", "E",
       "<p>Birga: May 301 → June 421 (yoʻq); May 400 → 560 (ha).</p><p>«More than» oraliq beradi, son emas.</p>"),
    ds("Is Laylo older than Bekzod?", "Laylo is 2 years older than Kamola.", "Kamola is 3 years younger than Bekzod.", "C",
       "<p>Birga: Laylo = Kamola + 2, Bekzod = Kamola + 3 — aniq «yoʻq».</p><p>Har biri yolgʻiz — bitta yoshni bilmaymiz.</p>"),
]

# =====================================================================
# GMAT-29 — traps and hidden constraints
# =====================================================================
Q29 = [
    ds(f"What is the value of {X}?", f"2{X} + 3{Y} = 12 and {Y} = 2", f"{Y} = 2", "A",
       "<p>(1) oʻzida <i>y</i> bor: <i>x</i> = 3. (2): <i>x</i> haqida yoʻq.</p><p>C tuzogʻi — (1) oʻzi yetarli.</p>"),
    ds("What is the price of one notebook?", "3 notebooks and 2 pens cost $13.", "6 notebooks and 4 pens cost $26.", "E",
       "<p>(2) — (1) ning ikki baravari.</p><p>Ikki tenglama — mustaqil emas.</p>"),
    ds("A customer spent exactly $19 on pens that cost $3 each and notebooks that cost $5 each, buying at least one of each. How many pens did the customer buy?", "The customer bought at least 2 notebooks.", "The customer bought at least 2 pens.", "D",
       "<p>Savolning oʻzi: yagona butun yechim — 3 ruchka, 2 daftar.</p><p>Butunlik cheklovi hal qiladi.</p>"),
    ds(f"What is the value of {X}?", f"{X}{SQ} = 36", f"{X} is the number of people on a team.", "C",
       "<p>Birga: odamlar soni musbat — 6.</p><p>«Soni» — yashirin musbatlik.</p>"),
    ds(f"Is {X} &gt; 0?", f"{X} = |{Y}|", f"{Y} ≠ 0", "C",
       "<p>Birga: |<i>y</i>| &gt; 0 — ha. (1) yolgʻiz: <i>y</i> = 0 boʻlsa <i>x</i> = 0.</p><p>Modul ≥ 0, &gt; 0 emas.</p>"),
    ds("If <i>n</i> is an integer, what is the value of <i>n</i>?", "3 &lt; <i>n</i> &lt; 6", "4 &lt; <i>n</i> &lt; 7", "C",
       "<p>(1): 4 yoki 5. (2): 5 yoki 6. Birga: 5.</p><p>Har bir oraliqdagi butun sonlarni yozing.</p>"),
    ds(f"What is the value of {X}?", f"{X}{SQ} = {X} and {X} ≠ 0", f"{X}<sup>3</sup> = {X} and {X} &gt; 0", "D",
       "<p>(1): 1. (2): 1.</p><p>Har bir maʼlumot oʻz cheklovi bilan keladi.</p>"),
    ds(f"Is {X}{SQ} &gt; {X}?", f"{X} &gt; 1", f"|{X}| &gt; 2", "D",
       "<p>(1): ha. (2): <i>x</i> &gt; 2 yoki <i>x</i> &lt; −2 — ikkala holatda ham ha (manfiy sonning kvadrati musbat).</p><p>Ikki xil holat, bir xil javob.</p>"),
    ds("What is the ratio of boys to girls in a class?", "Boys make up 40% of the class.", "There are 1.5 girls for every boy in the class.", "D",
       "<p>Ikkalasi ham 2 : 3.</p><p>Nisbat uchun haqiqiy sonlar kerak emas.</p>"),
    ds("What is the average (arithmetic mean) of <i>a</i>, <i>b</i> and <i>c</i>?", "<i>a</i> + <i>b</i> + <i>c</i> = 15", "<i>a</i> + <i>b</i> = 10", "A",
       "<p>(1): oʻrtacha 5. (2): <i>c</i> nomaʼlum.</p><p>Oʻrtacha uchun yigʻindi yetarli.</p>"),
    ds("If <i>n</i> is an integer, is <i>n</i> odd?", f"<i>n</i>{SQ} + <i>n</i> is even.", "<i>n</i> + 1 is even.", "B",
       "<p>(2): ha. (1): <i>n</i>(<i>n</i> + 1) har doim juft — maʼlumot yoʻq.</p><p>Doim toʻgʻri maʼlumot — yetarli emas.</p>"),
    ds("If <i>n</i> is a positive integer, what is the remainder when <i>n</i> is divided by 6?", "When <i>n</i> is divided by 3, the remainder is 2.", "When <i>n</i> is divided by 2, the remainder is 1.", "C",
       "<p>(1): 2 yoki 5. (2): 1, 3 yoki 5. Birga: 5.</p><p>Qoldiqlarni roʻyxat qiling.</p>"),
    ds("How much did a firm spend on advertising this year?", "Its advertising spending rose by 20% from last year.", "Its total costs this year were $400,000.", "E",
       "<p>Oʻtgan yilgi summa ham, ulush ham nomaʼlum.</p><p>Foiz oʻzgarishi — summa emas.</p>"),
    ds("What is Malika's regular hourly wage?", "She earned $640 for a 40-hour week with no overtime.", "For overtime she earns 1.5 times her regular hourly wage.", "A",
       "<p>(1): $16. (2): faqat nisbat.</p><p>C tuzogʻi — (1) oʻzi yetarli.</p>"),
    ds("How many of 30 students passed both test A and test B?", "25 students passed test A.", "20 students passed test B.", "E",
       "<p>Birga: kesishma 15 dan 20 gacha.</p><p>«Hech biri» nomaʼlum — kesishma oraliqda.</p>"),
    ds("Kamola spent $44 on tickets that cost $8 or $12 each. How many $12 tickets did she buy?", "She bought at least one ticket of each price.", "She bought 5 tickets.", "B",
       "<p>Butun yechimlar: (4 ta, 1 ta) va (1 ta, 3 ta). (1): ikkalasi ham mos. (2): faqat (4, 1).</p><p>Butun yechimlarni sanang.</p>"),
    ds(f"Is {X} an integer?", f"2{X} is an integer.", f"{X}/2 is an integer.", "B",
       "<p>(2): ha. (1): 0.5 — yoʻq, 1 — ha.</p><p>Kasr misolini unutmang.</p>"),
    ds("What is the value of <i>k</i>?", f"<i>k</i> is a positive integer and <i>k</i>{SQ} &lt; 5.", "<i>k</i> is a positive integer and <i>k</i><sup>3</sup> &gt; 5.", "C",
       "<p>(1): 1 yoki 2. (2): 2, 3, … Birga: 2.</p><p>Har bir maʼlumot ichidagi cheklovni oʻqing.</p>"),
    ds("A shop sold 20 items, each a cake for $15 or a pie for $9, for a total of $252. How many cakes did it sell?", "It sold more cakes than pies.", "Its revenue from pies was $72.", "D",
       "<p>Savolning oʻzi: 15<i>c</i> + 9(20 − <i>c</i>) = 252 → 12 tort.</p><p>Savol yetarli boʻlsa — har bir maʼlumot ham yetarli.</p>"),
    ds("How many employees speak exactly one of English and Russian?", "40 employees speak English and 30 speak Russian.", "10 employees speak both English and Russian.", "C",
       "<p>Birga: (40 − 10) + (30 − 10) = 50.</p><p>«Exactly one» — kesishmasiz.</p>"),
]

# =====================================================================
# GMAT-30 — word problems
# =====================================================================
Q30 = [
    ds("By what percent did a store's revenue from a product change from 2024 to 2025?", "From 2024 to 2025 the product's price rose by 10% and the number of units sold fell by 10%.", "The store's revenue from the product in 2024 was $50,000.", "A",
       "<p>(1): 1.1 × 0.9 = 0.99 — 1% kamaydi.</p><p>Foiz oʻzgarishi uchun baza kerak emas.</p>"),
    ds("Of the 50 employees at a firm, how many speak both English and Korean?", "30 of the employees speak English and 25 speak Korean.", "5 of the employees speak neither language.", "C",
       "<p>Birga: 30 + 25 + 5 − 50 = 10.</p><p>Toʻplam formulasi — toʻrttadan uchtasi kerak.</p>"),
    ds("Working together at their constant rates, how many hours do machines A and B take to finish a job?", "Machine A alone takes 6 hours.", "Together the two machines complete one third of the job each hour.", "B",
       "<p>(2): 3 soat. (1): B nomaʼlum.</p><p>(2) birgalikdagi unumni bevosita beradi.</p>"),
    ds("What was a driver's average speed for a round trip?", "The driver drove at 60 kilometers per hour going.", "The trip was 120 kilometers each way.", "E",
       "<p>Qaytishdagi tezlik yoki vaqt nomaʼlum.</p><p>Oʻrtacha tezlik = umumiy masofa ÷ umumiy vaqt.</p>"),
    ds("What is the concentration of acid in a mixture?", "The mixture was made from 10 liters of a 20% acid solution and 30 liters of a 40% acid solution.", "The mixture contains 14 liters of acid.", "A",
       "<p>(1): (2 + 12) ÷ 40 = 35%. (2): hajm nomaʼlum.</p><p>Konsentratsiya = modda ÷ hajm.</p>"),
    ds("How much interest does a deposit earn in 2 years if interest is compounded annually?", "The deposit is $10,000.", "The annual interest rate is 10%.", "C",
       "<p>Birga: $2,100.</p><p>Summa va stavka — ikkalasi kerak.</p>"),
    ds("What was the original price of an item?", "After a 25% increase, the price was $150.", "The price increase was $30.", "A",
       "<p>(1): 150 ÷ 1.25 = 120. (2): oshish $30, lekin foiz ham, yangi narx ham nomaʼlum.</p><p>(2) ni (1) dagi $150 bilan birga oʻqish — eng koʻp uchraydigan xato.</p>"),
    ds("What was a store's profit on a lamp, as a percent of its cost?", "The lamp was sold for $120.", "The lamp's price was marked up 50% above cost, and it was then sold at 20% off the marked price.", "B",
       "<p>(2): 1.5 × 0.8 = 1.2 → 20%. (1): tannarx nomaʼlum.</p><p>Foiz uchun koʻpaytuvchilar yetarli.</p>"),
    ds("What is the average (arithmetic mean) of six numbers?", "The sum of the six numbers is 72.", "The average of the first three numbers is 10 and the average of the last three is 14.", "D",
       "<p>(1): 12. (2): (30 + 42) ÷ 6 = 12.</p><p>Oʻrtachalar teng guruhlarda — oddiy oʻrtacha.</p>"),
    ds("How many units must a company sell to break even?", "Its fixed costs are $12,000, and each unit sells for $25 and costs $10 to make.", "Each unit sells for $25.", "A",
       "<p>(1): 12,000 ÷ 15 = 800. (2): xarajatlar nomaʼlum.</p><p>Zararsizlik — doimiy xarajat ÷ farq.</p>"),
    ds("Working at the same rate, how many workers are needed to finish a job in 4 days?", "6 workers can finish the job in 10 days.", "20 workers can finish the job in 3 days.", "D",
       "<p>Ikkalasi ham 60 ishchi-kun → 15 ishchi.</p><p>Ish hajmi = ishchilar × kunlar.</p>"),
    ds("What fraction of a tank is full?", "The tank holds 120 liters.", "If 45 more liters were added, the tank would go from 3/8 full to 3/4 full.", "B",
       "<p>(2): hozir 3/8 — bevosita. (1): ichidagi miqdor nomaʼlum.</p><p>Kasrni bevosita bergan maʼlumot yetarli.</p>"),
    ds("What is the median monthly salary of a firm's 5 employees?", "The three lowest salaries are $3,000, $3,200 and $3,500.", "The mean salary is $5,740.", "A",
       "<p>(1): 5 ta maoshning medianasi — 3-chi, $3,500. (2): oʻrtacha medianani bermaydi.</p><p>Mediana — oʻrtadagi qiymat.</p>"),
    ds("How many guests attended both the morning and afternoon sessions of a conference?", "60 guests attended the morning session and 45 attended the afternoon session.", "The conference had 90 guests, 15 of whom attended neither session.", "C",
       "<p>Birga: 60 + 45 + 15 − 90 = 30.</p><p>Har biri yolgʻiz — formula toʻlmaydi.</p>"),
    ds("By what percent did an app's number of users increase from 2022 to 2024?", "The app had 4,000 users in 2022.", "The number of users tripled each year from 2022 to 2024.", "B",
       "<p>(2): × 9 → 800% oʻsish. (1): bitta son.</p><p>Foiz — koʻpaytuvchidan.</p>"),
    ds("How many liters of fuel did a car use on a trip?", "The car uses 6 liters of fuel per 100 kilometers.", "Fuel cost $1.20 per liter.", "E",
       "<p>Masofa ham, umumiy narx ham nomaʼlum.</p><p>Litr = masofa × sarf.</p>"),
    ds("Two chips are drawn at random, without replacement, from a box. What is the probability that both are defective?", "The box holds 10 chips, 2 of which are defective.", "The box holds 10 chips.", "A",
       "<p>(1): 2/10 × 1/9 = 1/45. (2): nuqsonlilar soni nomaʼlum.</p><p>Ehtimollik — qulay va jami kerak.</p>"),
    ds("A sum was divided between Bekzod and Laylo. How much did Laylo receive?", "Bekzod received $200 more than Laylo.", "Bekzod received 3/5 of the sum.", "C",
       "<p>Birga: $400.</p><p>Ayirma va ulush birga jamini beradi.</p>"),
    ds("Is an investment worth more than $12,000 after 2 years of interest compounded annually?", "The amount invested was $10,000.", "The annual interest rate is 10%.", "C",
       "<p>Birga: $12,100 — aniq «ha».</p><p>Har biri yolgʻiz — bittasi nomaʼlum.</p>"),
    ds("Did a store make a profit on a lamp?", "The lamp's price was marked up 50% above its cost.", "The lamp was sold at 40% off its marked price.", "C",
       "<p>Birga: 1.5 × 0.6 = 0.9 — aniq «yoʻq».</p><p>Aniq «yoʻq» — yetarli.</p>"),
]

PRACTICES = [
    {
        "title": "GMAT-26 Practice: The Data Insights Section and Data Sufficiency",
        "description": "20 ta Data Sufficiency savoli — AD / BCE usuli va beshta oʻzgarmas javob.",
        "tutorial": "GMAT-26:", "subject": "GMAT", "level": "medium", "questions": Q26,
    },
    {
        "title": "GMAT-27 Practice: Data Sufficiency — Value Questions",
        "description": "20 ta Data Sufficiency savoli — yagona qiymat, mustaqil tenglamalar va soʻralgan ifoda.",
        "tutorial": "GMAT-27:", "subject": "GMAT", "level": "medium", "questions": Q27,
    },
    {
        "title": "GMAT-28 Practice: Data Sufficiency — Yes/No Questions",
        "description": "20 ta Data Sufficiency savoli — har doim «ha» yoki har doim «yoʻq».",
        "tutorial": "GMAT-28:", "subject": "GMAT", "level": "medium", "questions": Q28,
    },
    {
        "title": "GMAT-29 Practice: Data Sufficiency — Traps and Hidden Constraints",
        "description": "20 ta Data Sufficiency savoli — C tuzogʻi, nusxa maʼlumot va yashirin cheklovlar.",
        "tutorial": "GMAT-29:", "subject": "GMAT", "level": "hard", "questions": Q29,
    },
    {
        "title": "GMAT-30 Practice: Data Sufficiency — Word Problems",
        "description": "20 ta Data Sufficiency savoli — foiz, toʻplam, tezlik, aralashma va foiz daromadi.",
        "tutorial": "GMAT-30:", "subject": "GMAT", "level": "hard", "questions": Q30,
    },
]
