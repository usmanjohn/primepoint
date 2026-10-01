# -*- coding: utf-8 -*-
"""Prime GMAT mashqlar — GMAT-16 … GMAT-20 (sets, then the algebra block).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan. Savollar INGLIZCHA (imtihon
tili), tushuntirishlar OʻZBEKCHA. Har savolda BESHTA variant, raqamli variantlar oʻsish
tartibida. Kalkulyatorsiz yechiladigan arifmetika.

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context · 15–16 trap-spotting ·
      17–18 harder · 19–20 word problems (har doim ikkita).

Import:
    python manage.py import_practices practice/management/commands/_practice_pg_16_20.py \\
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


X = "<i>x</i>"
SQ = "<sup>2</sup>"

# =====================================================================
# GMAT-16 — overlapping sets
# =====================================================================
Q16 = [
    q("Set A has 40 members and set B has 30 members. If 10 members belong to both sets, how many members belong to at least one of the sets?", ["50", "60", "70", "80", "90"], "60",
      "<p><strong>60.</strong> 40 + 30 − 10.</p><p><strong>70</strong> — kesishmani ayirmagan javob.</p>"),
    q("Of 120 people surveyed, 70 drink tea, 60 drink coffee and 25 drink both. How many drink neither?", ["5", "10", "15", "25", "35"], "15",
      "<p><strong>15.</strong> 120 − (70 + 60 − 25) = 120 − 105.</p><p><strong>35</strong> — «ikkalasi»ni ikki marta ayirgan javob.</p>"),
    q("Of 50 students, 30 study French, 25 study Spanish and 10 study both. How many study only French?", ["10", "15", "20", "25", "30"], "20",
      "<p><strong>20.</strong> 30 − 10.</p><p><strong>30</strong> — «faqat» soʻzini eʼtiborsiz qoldirgan javob.</p>"),
    q("Of 60 employees, 35 own a car, 15 own both a car and a bicycle, and 10 own neither. How many own a bicycle?", ["15", "20", "25", "30", "40"], "30",
      "<p><strong>30.</strong> Kamida bittasi: 60 − 10 = 50; 50 = 35 + <i>B</i> − 15 → <i>B</i> = 30.</p><p><strong>15</strong> — faqat velosiped egalari (30 − 15).</p>"),
    q("Of 200 customers, 120 shopped online, 100 shopped in the store and 40 did neither. How many shopped both online and in the store?", ["20", "40", "60", "80", "100"], "60",
      "<p><strong>60.</strong> 120 + 100 + 40 − 200.</p><p><strong>20</strong> — «hech biri»ni hisobga olmagan javob (120 + 100 − 200).</p>"),
    q("Of 100 people, 65 use product A and 55 use product B. What is the least possible number who use both?", ["0", "10", "20", "35", "55"], "20",
      "<p><strong>20.</strong> 65 + 55 − 100 — ortiqchasi kamida ikki marta sanalgan.</p><p><strong>0</strong> — toʻplamlar bir-biriga tegmasligi mumkin deb oʻylagan javob.</p>"),
    q("Of 100 people, 65 use product A and 55 use product B. What is the greatest possible number who use both?", ["20", "35", "45", "55", "65"], "55",
      "<p><strong>55.</strong> B toʻliq A ning ichida boʻlganda.</p><p><strong>65</strong> — kesishma kichik toʻplamdan katta boʻlolmaydi.</p>"),
    q("Of 100 people, 65 use product A and 55 use product B. What is the greatest possible number who use neither product?", ["0", "10", "20", "35", "45"], "35",
      "<p><strong>35.</strong> Kesishma eng katta (55) boʻlsa, birlashma 65; 100 − 65.</p><p><strong>45</strong> — kichik toʻplamni ayirgan javob (100 − 55).</p>"),
    q("Of 300 applicants, 180 are women and 120 have an MBA. If 70 of the women have an MBA, how many of the men do not have an MBA?", ["50", "70", "110", "130", "180"], "70",
      "<p><strong>70.</strong> Erkaklar 120; MBA'li erkaklar 120 − 70 = 50; MBA'siz erkaklar 120 − 50.</p><p><strong>50</strong> — MBA'li erkaklar.</p>"),
    q("In a class, 60% of students study math, 50% study economics and 20% study neither. What percent study both?", ["10%", "20%", "30%", "40%", "50%"], "30%",
      "<p><strong>30%.</strong> 60 + 50 + 20 − 100.</p><p><strong>10%</strong> — «hech biri»ni unutgan javob.</p>"),
    q("Of a company's 400 employees, 250 attended training A, 180 attended training B and 90 attended both. How many attended neither?", ["30", "60", "90", "150", "240"], "60",
      "<p><strong>60.</strong> 400 − (250 + 180 − 90) = 400 − 340.</p><p><strong>150</strong> — faqat A treningiga bormaganlar (400 − 250); ular orasida B ga borganlar ham bor.</p>"),
    q("In a survey of households, 320 own a car, 210 own a bicycle and 130 own both. How many own exactly one of the two?", ["190", "270", "330", "400", "530"], "270",
      "<p><strong>270.</strong> Faqat avtomobil 190, faqat velosiped 80.</p><p><strong>400</strong> — kamida bittasi (birlashma); «exactly one» kesishmani chiqarib tashlaydi.</p>"),
    q("Of 90 conference guests, 2/3 attended the morning session, 1/2 attended the afternoon session and 15 attended neither. How many attended both sessions?", ["15", "20", "25", "30", "45"], "30",
      "<p><strong>30.</strong> 60 + 45 + 15 − 90.</p><p><strong>15</strong> — «hech biri»ni kesishma bilan adashtirgan javob.</p>"),
    q("At a firm, 40% of the staff work in sales. Of the sales staff, 25% work remotely; of the other staff, 30% work remotely. What percent of all staff work remotely?", ["25%", "27.5%", "28%", "30%", "55%"], "28%",
      "<p><strong>28%.</strong> 0.4 × 0.25 + 0.6 × 0.3 = 0.10 + 0.18.</p><p><strong>27.5%</strong> — ikki foizning oddiy oʻrtachasi; guruhlar teng emas.</p>"),
    q("Of 80 people, 50 like product X, 45 like product Y and 10 like neither. How many like only product X?", ["10", "15", "20", "25", "40"], "25",
      "<p><strong>25.</strong> Ikkalasi: 50 + 45 + 10 − 80 = 25; faqat X: 50 − 25.</p><p><strong>40</strong> — X dan «hech biri»ni ayirgan javob.</p>"),
    q("A group of 60 people contains 30 members of club A and 40 members of club B. If every person is in at least one club, how many are in both?", ["0", "10", "20", "30", "70"], "10",
      "<p><strong>10.</strong> 30 + 40 − 60.</p><p><strong>0</strong> — «hech biri» yoʻqligi kesishma yoʻq degani emas.</p>"),
    q("Of 100 employees, 45 speak English, 35 speak Russian and 30 speak Korean. Exactly 12 employees speak exactly two of these languages, and 4 speak all three. How many speak none of the three?", ["6", "10", "14", "18", "22"], "10",
      "<p><strong>10.</strong> Kamida bittasi: 110 − 12 − 2 × 4 = 90; 100 − 90.</p><p><strong>14</strong> — uchalasini faqat bir marta ayirgan javob.</p>"),
    q("In a group of 50 people, 30 have a laptop and 35 have a tablet. What is the difference between the greatest and least possible numbers of people who have both?", ["5", "10", "15", "20", "30"], "15",
      "<p><strong>15.</strong> Eng kami 30 + 35 − 50 = 15, eng koʻpi 30; farq 15.</p><p><strong>30</strong> — faqat eng katta qiymat.</p>"),
    q("A bank surveyed 600 small businesses: 380 have a business loan, 250 use the bank's mobile app, and 120 have neither. How many have a loan but do not use the app?", ["150", "230", "250", "260", "380"], "230",
      "<p><strong>230.</strong> Ikkalasi: 380 + 250 + 120 − 600 = 150; faqat kredit 380 − 150.</p><p><strong>150</strong> — ikkalasi bor bizneslar.</p>"),
    q("Of 240 MBA applicants, 3/4 took the GMAT and 1/3 took the GRE. If 30 applicants took neither test, how many took both?", ["20", "40", "50", "60", "80"], "50",
      "<p><strong>50.</strong> GMAT 180, GRE 80; 180 + 80 + 30 − 240.</p><p><strong>20</strong> — «hech biri»ni hisobga olmagan javob.</p>"),
]

# =====================================================================
# GMAT-17 — linear equations and systems
# =====================================================================
Q17 = [
    q(f"If 4{X} − 7 = 13, what is the value of {X}?", ["1.5", "4", "5", "6", "20"], "5",
      "<p><strong>5.</strong> 4<i>x</i> = 20.</p><p><strong>1.5</strong> — 7 ni qoʻshish oʻrniga ayirgan javob (4<i>x</i> = 6).</p>"),
    q(f"If 3({X} + 2) = 21, what is the value of {X}?", ["3", "5", "6.33", "7", "19"], "5",
      "<p><strong>5.</strong> <i>x</i> + 2 = 7.</p><p><strong>6.33</strong> — qavsni 3<i>x</i> + 2 deb ochgan javob.</p>"),
    q(f"If {X}/4 + 3 = 8, what is the value of {X}?", ["2", "5", "11", "20", "44"], "20",
      "<p><strong>20.</strong> <i>x</i>/4 = 5.</p><p><strong>44</strong> — 3 ni ayirishdan oldin 4 ga koʻpaytirgan javob.</p>"),
    q(f"If 5{X} − 3 = 2{X} + 9, what is the value of {X}?", ["2", "3", "4", "6", "12"], "4",
      "<p><strong>4.</strong> 3<i>x</i> = 12.</p><p><strong>2</strong> — 3 ning ishorasini adashtirgan javob (3<i>x</i> = 6).</p>"),
    q(f"If {X} + <i>y</i> = 15 and {X} − <i>y</i> = 3, what is the value of <i>y</i>?", ["3", "6", "9", "12", "18"], "6",
      "<p><strong>6.</strong> Ayirsak: 2<i>y</i> = 12.</p><p><strong>9</strong> — <i>x</i> ning qiymati.</p>"),
    q(f"If 2{X} + <i>y</i> = 10 and {X} − <i>y</i> = 2, what is the value of {X}<i>y</i>?", ["4", "6", "8", "10", "12"], "8",
      "<p><strong>8.</strong> Qoʻshsak 3<i>x</i> = 12, <i>x</i> = 4, <i>y</i> = 2.</p><p><strong>6</strong> — <i>x</i> + <i>y</i>.</p>"),
    q(f"How many solutions does the system 3{X} + 2<i>y</i> = 12 and 6{X} + 4<i>y</i> = 24 have?", ["None", "Exactly one", "Exactly two", "Exactly three", "Infinitely many"], "Infinitely many",
      "<p><strong>Infinitely many.</strong> Ikkinchi tenglama — birinchisining ikki baravari, yaʼni bitta toʻgʻri chiziq.</p><p><strong>Exactly one</strong> — ikki tenglama doim bitta yechim beradi deb oʻylagan javob.</p>"),
    q("If 4<i>a</i> + 3<i>b</i> = 25 and 3<i>a</i> + 4<i>b</i> = 24, what is the value of <i>a</i> − <i>b</i>?", ["1", "2", "3", "7", "49"], "1",
      "<p><strong>1.</strong> Ayirsak: <i>a</i> − <i>b</i> = 1.</p><p><strong>7</strong> — <i>a</i> + <i>b</i> (qoʻshib, 7 ga boʻlinadi).</p>"),
    q(f"If {X} = 2<i>y</i> and {X} + <i>y</i> = 24, what is the value of {X}?", ["8", "12", "16", "18", "24"], "16",
      "<p><strong>16.</strong> 3<i>y</i> = 24, <i>y</i> = 8.</p><p><strong>8</strong> — <i>y</i> ning qiymati.</p>"),
    q(f"If 3{X} − 2<i>y</i> = 7 and 3{X} + 2<i>y</i> = 17, what is the value of <i>y</i>?", ["1.5", "2", "2.5", "4", "5"], "2.5",
      "<p><strong>2.5.</strong> Ayirsak: 4<i>y</i> = 10.</p><p><strong>4</strong> — <i>x</i> ning qiymati.</p>"),
    q("A museum sold 50 tickets for a total of $520. Adult tickets cost $12 and child tickets cost $8. How many adult tickets were sold?", ["15", "20", "25", "30", "35"], "30",
      "<p><strong>30.</strong> Hammasi bolalar uchun boʻlsa 400; ortiqcha 120, har bir katta +4.</p><p><strong>20</strong> — bolalar chiptalari.</p>"),
    q("A plumber charges a fixed call-out fee plus an hourly rate. A 2-hour job costs $110 and a 5-hour job costs $230. What is the call-out fee?", ["$15", "$25", "$30", "$40", "$55"], "$30",
      "<p><strong>$30.</strong> 3 soat farqi $120 → soatiga $40; 110 − 80.</p><p><strong>$40</strong> — soatlik narx.</p>"),
    q("Aziz is four times as old as his son. In 20 years, Aziz will be twice as old as his son. How old is the son now?", ["5", "8", "10", "12", "20"], "10",
      "<p><strong>10.</strong> 4<i>s</i> + 20 = 2(<i>s</i> + 20) → 2<i>s</i> = 20.</p><p><strong>20</strong> — 20 yil keyingi «ikki baravar» sharti bilan adashtirilgan javob.</p>"),
    q("A company buys 30 chairs and desks for a total of $3,840. Each chair costs $80 and each desk costs $200. How many desks does it buy?", ["10", "12", "15", "18", "20"], "12",
      "<p><strong>12.</strong> Hammasi stul boʻlsa 2,400; ortiqcha 1,440, har bir stol +120.</p><p><strong>18</strong> — stullar soni.</p>"),
    q(f"If 2{X} + 2<i>y</i> = 18, what is the value of {X} + <i>y</i>?", ["6", "9", "16", "18", "36"], "9",
      "<p><strong>9.</strong> 2 ga boʻlamiz.</p><p><strong>18</strong> — 2(<i>x</i> + <i>y</i>) ning oʻzi.</p>"),
    q(f"If 3{X} + <i>y</i> = 10 and {X} + 3<i>y</i> = 14, what is the average (arithmetic mean) of {X} and <i>y</i>?", ["3", "4", "6", "12", "24"], "3",
      "<p><strong>3.</strong> Qoʻshsak: 4(<i>x</i> + <i>y</i>) = 24, <i>x</i> + <i>y</i> = 6, oʻrtacha 3.</p><p><strong>6</strong> — yigʻindi; savol oʻrtachani soʻradi.</p>"),
    q(f"If {X}/<i>y</i> = 3/4 and {X} + <i>y</i> = 21, what is the value of <i>y</i> − {X}?", ["3", "7", "9", "12", "21"], "3",
      "<p><strong>3.</strong> 7 qism = 21; <i>x</i> = 9, <i>y</i> = 12.</p><p><strong>12</strong> — <i>y</i> ning oʻzi.</p>"),
    q("If <i>a</i> + <i>b</i> = 10, <i>b</i> + <i>c</i> = 14 and <i>a</i> + <i>c</i> = 12, what is the value of <i>a</i> + <i>b</i> + <i>c</i>?", ["12", "14", "18", "24", "36"], "18",
      "<p><strong>18.</strong> Uchalasini qoʻshsak 2(<i>a</i> + <i>b</i> + <i>c</i>) = 36.</p><p><strong>36</strong> — 2 ga boʻlishni unutgan javob.</p>"),
    q("A coffee shop sold 120 drinks for a total of $510. Lattes cost $5 and teas cost $3. How many lattes did it sell?", ["45", "60", "75", "85", "102"], "75",
      "<p><strong>75.</strong> Hammasi choy boʻlsa 360; ortiqcha 150, har bir latte +2.</p><p><strong>45</strong> — choylar soni.</p>"),
    q("Two printing jobs together cost $1,400. The larger job cost $200 more than twice the cost of the smaller job. What did the larger job cost?", ["$400", "$600", "$800", "$1,000", "$1,200"], "$1,000",
      "<p><strong>$1,000.</strong> <i>S</i> + (2<i>S</i> + 200) = 1,400 → <i>S</i> = 400.</p><p><strong>$400</strong> — kichik ishning narxi.</p>"),
]

# =====================================================================
# GMAT-18 — inequalities and absolute value
# =====================================================================
Q18 = [
    q(f"Which of the following is the solution of 2{X} + 3 &gt; 11?", [f"{X} &gt; 4", f"{X} &gt; 7", f"{X} &lt; 4", f"{X} &gt; 5.5", f"{X} &lt; 7"], f"{X} &gt; 4",
      "<p><strong>x &gt; 4.</strong> 2<i>x</i> &gt; 8.</p><p><strong>x &gt; 7</strong> — 2 ga boʻlishni unutgan javob.</p>"),
    q(f"Which of the following is the solution of −3{X} ≥ 12?", [f"{X} ≥ −4", f"{X} ≤ −4", f"{X} ≥ 4", f"{X} ≤ 4", f"{X} ≤ −36"], f"{X} ≤ −4",
      "<p><strong>x ≤ −4.</strong> −3 ga boʻlganda belgi oʻgiriladi.</p><p><strong>x ≥ −4</strong> — belgini oʻgirishni unutgan javob.</p>"),
    q(f"How many values of {X} satisfy |{X}| = 9?", ["0", "1", "2", "9", "18"], "2",
      "<p><strong>2.</strong> 9 va −9.</p><p><strong>1</strong> — manfiy yechimni unutgan javob.</p>"),
    q(f"What is the product of the solutions of |{X} − 4| = 6?", ["−20", "−10", "2", "10", "20"], "−20",
      "<p><strong>−20.</strong> Yechimlar 10 va −2.</p><p><strong>20</strong> — ishorani yoʻqotgan javob.</p>"),
    q(f"How many integers {X} satisfy |{X}| ≤ 3?", ["3", "4", "6", "7", "8"], "7",
      "<p><strong>7.</strong> −3 dan 3 gacha, 0 bilan.</p><p><strong>6</strong> — 0 ni unutgan javob.</p>"),
    q(f"How many integers {X} satisfy |{X} − 2| &lt; 4?", ["5", "6", "7", "8", "9"], "7",
      "<p><strong>7.</strong> −2 &lt; <i>x</i> &lt; 6: −1 dan 5 gacha.</p><p><strong>9</strong> — chetlarni ham qoʻshgan javob.</p>"),
    q(f"How many integers {X} satisfy −5 &lt; 3{X} + 1 &lt; 10?", ["3", "4", "5", "6", "15"], "4",
      "<p><strong>4.</strong> −2 &lt; <i>x</i> &lt; 3: −1, 0, 1, 2.</p><p><strong>5</strong> — chetdagi 3 ni ham sanagan javob.</p>"),
    q(f"If {X} is a positive integer and 4 − 2{X} &gt; −6, what is the greatest possible value of {X}?", ["2", "3", "4", "5", "6"], "4",
      "<p><strong>4.</strong> −2<i>x</i> &gt; −10 → <i>x</i> &lt; 5.</p><p><strong>5</strong> — qatʼiy belgini ≤ deb oʻqigan javob.</p>"),
    q(f"Which of the following is equivalent to |{X} + 1| ≤ 5?", [f"−6 ≤ {X} ≤ 4", f"−4 ≤ {X} ≤ 6", f"{X} ≤ 4", f"−5 ≤ {X} ≤ 5", f"{X} ≥ −6"], f"−6 ≤ {X} ≤ 4",
      "<p><strong>−6 ≤ x ≤ 4.</strong> Markaz −1, har ikki tomonga 5.</p><p><strong>−4 ≤ x ≤ 6</strong> — markazni +1 deb olgan javob.</p>"),
    q(f"If <i>a</i> &lt; <i>b</i> &lt; 0, which of the following must be true?", ["<i>ab</i> &lt; 0", "<i>a</i>/<i>b</i> &lt; 1", f"<i>a</i>{SQ} &gt; <i>b</i>{SQ}", "<i>a</i> + <i>b</i> &gt; 0", "<i>b</i> − <i>a</i> &lt; 0"], f"<i>a</i>{SQ} &gt; <i>b</i>{SQ}",
      "<p><strong>a² &gt; b².</strong> <i>a</i> nolga nisbatan uzoqroq, demak kvadrati katta: −4 va −2 → 16 &gt; 4.</p><p><strong>a/b &lt; 1</strong> — musbat sonlardagi odat; −4/−2 = 2.</p>"),
    q("A phone plan costs $20 a month plus $0.10 per minute. What is the greatest number of minutes a customer can use if the monthly bill must be at most $35?", ["100", "150", "200", "350", "550"], "150",
      "<p><strong>150.</strong> 20 + 0.1<i>m</i> ≤ 35 → <i>m</i> ≤ 150.</p><p><strong>350</strong> — 20 ni ayirmagan javob.</p>"),
    q("A factory's daily output must be within 50 units of 1,000 units. Which of the following describes all allowed outputs <i>n</i>?", ["|<i>n</i> − 1,000| ≤ 50", "|<i>n</i> − 50| ≤ 1,000", "|<i>n</i> + 1,000| ≤ 50", "<i>n</i> ≤ 1,050", "<i>n</i> ≥ 950"], "|<i>n</i> − 1,000| ≤ 50",
      "<p><strong>|n − 1,000| ≤ 50.</strong> Markaz 1,000, chetlanish 50.</p><p><strong>n ≤ 1,050</strong> — faqat yuqori chegara; pastki chegara yoʻqolgan.</p>"),
    q("A courier earns $40 a day plus $3 per parcel delivered. What is the least number of parcels she must deliver to earn more than $100 in a day?", ["18", "20", "21", "33", "47"], "21",
      "<p><strong>21.</strong> 3<i>p</i> &gt; 60 → <i>p</i> &gt; 20.</p><p><strong>20</strong> — «more than» qatʼiy: 20 ta posilka aynan 100 beradi.</p>"),
    q("A thermostat keeps a room within 2 degrees of 21 degrees. What is the lowest temperature it allows?", ["17", "19", "20", "21", "23"], "19",
      "<p><strong>19.</strong> 21 − 2.</p><p><strong>23</strong> — eng yuqori chegara.</p>"),
    q(f"If −2{X} &lt; 8, which of the following must be true?", [f"{X} &lt; −4", f"{X} &gt; −4", f"{X} &lt; 4", f"{X} &gt; 4", f"{X} &lt; −16"], f"{X} &gt; −4",
      "<p><strong>x &gt; −4.</strong> −2 ga boʻlganda belgi oʻgiriladi.</p><p><strong>x &lt; −4</strong> — belgini oʻgirishni unutgan javob.</p>"),
    q(f"Which of the following is equivalent to {X}{SQ} &lt; 16?", [f"{X} &lt; 4", f"−4 &lt; {X} &lt; 4", f"{X} &gt; −4", f"0 &lt; {X} &lt; 4", f"{X} &lt; −4"], f"−4 &lt; {X} &lt; 4",
      "<p><strong>−4 &lt; x &lt; 4.</strong> |<i>x</i>| &lt; 4.</p><p><strong>x &lt; 4</strong> — manfiy tomonni unutgan javob: <i>x</i> = −5 da 25 &gt; 16.</p>"),
    q(f"How many integers {X} satisfy |{X} − 3| + |{X} + 2| = 5?", ["0", "2", "5", "6", "7"], "6",
      "<p><strong>6.</strong> −2 va 3 orasidagi har bir nuqtadan ikki chetgacha masofalar yigʻindisi 5: −2 dan 3 gacha 6 ta butun son.</p><p><strong>2</strong> — faqat chetlarni olgan javob.</p>"),
    q(f"What is the sum of all integers {X} that satisfy |2{X} − 5| ≤ 7?", ["14", "18", "20", "21", "28"], "20",
      "<p><strong>20.</strong> −1 ≤ <i>x</i> ≤ 6: −1 + 0 + 1 + … + 6 = 20.</p><p><strong>21</strong> — −1 ni tashlab ketgan javob.</p>"),
    q("A team dinner may cost at most $2,000. The restaurant charges a fixed room fee of $350 plus $55 per guest. What is the greatest number of guests?", ["25", "29", "30", "31", "36"], "30",
      "<p><strong>30.</strong> 55<i>g</i> ≤ 1,650.</p><p><strong>36</strong> — xona narxini ayirmagan javob (2,000 ÷ 55).</p>"),
    q("A part must be 40 millimeters long, with an error of no more than 0.15 millimeters. Which of the following lengths, in millimeters, is NOT acceptable?", ["39.85", "39.9", "40.1", "40.15", "40.2"], "40.2",
      "<p><strong>40.2.</strong> |40.2 − 40| = 0.2 &gt; 0.15.</p><p><strong>39.85</strong> va <strong>40.15</strong> — aynan chegarada; «no more than» ularni qoʻshadi.</p>"),
]

# =====================================================================
# GMAT-19 — quadratics
# =====================================================================
Q19 = [
    q(f"If {X}{SQ} = 64 and {X} &gt; 0, what is the value of {X}?", ["4", "8", "16", "32", "64"], "8",
      "<p><strong>8.</strong> 8 × 8 = 64.</p><p><strong>32</strong> — 64 ni ikkiga boʻlgan javob.</p>"),
    q(f"What is the sum of the solutions of ({X} − 4)({X} + 6) = 0?", ["−24", "−10", "−2", "2", "10"], "−2",
      "<p><strong>−2.</strong> Yechimlar 4 va −6.</p><p><strong>2</strong> — qavsdagi sonlarni ishorasi bilan koʻchirgan javob (−4 + 6).</p>"),
    q(f"Which of the following is equal to {X}{SQ} − 9?", [f"({X} − 3){SQ}", f"({X} − 3)({X} + 3)", f"({X} − 9)({X} + 1)", f"({X} + 3){SQ}", f"({X} − 1)({X} + 9)"], f"({X} − 3)({X} + 3)",
      "<p><strong>(x − 3)(x + 3).</strong> Kvadratlar ayirmasi.</p><p><strong>(x − 3)²</strong> — oʻrta had −6<i>x</i> ni qoʻshib yuborgan javob.</p>"),
    q(f"What is the greater solution of {X}{SQ} − 7{X} + 10 = 0?", ["2", "3", "5", "7", "10"], "5",
      "<p><strong>5.</strong> (<i>x</i> − 2)(<i>x</i> − 5) = 0.</p><p><strong>10</strong> — ildizlar koʻpaytmasi.</p>"),
    q(f"If {X}{SQ} + 6{X} + 9 = 0, what is the value of {X}?", ["−9", "−6", "−3", "3", "9"], "−3",
      "<p><strong>−3.</strong> (<i>x</i> + 3)<sup>2</sup> = 0.</p><p><strong>3</strong> — ishorani adashtirgan javob.</p>"),
    q(f"What is the product of the solutions of {X}{SQ} − 3{X} − 28 = 0?", ["−28", "−11", "−3", "3", "28"], "−28",
      "<p><strong>−28.</strong> Yechimlar 7 va −4.</p><p><strong>3</strong> — ildizlar yigʻindisi.</p>"),
    q(f"What is the value of 101{SQ} − 99{SQ}?", ["4", "200", "400", "2,000", "4,000"], "400",
      "<p><strong>400.</strong> (101 + 99)(101 − 99) = 200 × 2.</p><p><strong>200</strong> — 2 ga koʻpaytirishni unutgan javob.</p>"),
    q(f"If {X} + <i>y</i> = 7 and {X}<i>y</i> = 10, what is the value of {X}{SQ} + <i>y</i>{SQ}?", ["19", "29", "39", "49", "69"], "29",
      "<p><strong>29.</strong> 49 − 2 × 10.</p><p><strong>49</strong> — (<i>x</i> + <i>y</i>)<sup>2</sup> ning oʻzi; 2<i>xy</i> ayirilmagan.</p>"),
    q(f"If {X}{SQ} − <i>y</i>{SQ} = 48 and {X} + <i>y</i> = 12, what is the value of {X} − <i>y</i>?", ["2", "4", "6", "12", "36"], "4",
      "<p><strong>4.</strong> 48 ÷ 12.</p><p><strong>36</strong> — 48 dan 12 ni ayirgan javob.</p>"),
    q(f"When (2{X} − 3)({X} + 4) is expanded, what is the coefficient of {X}?", ["−12", "−5", "1", "5", "11"], "5",
      "<p><strong>5.</strong> 8<i>x</i> − 3<i>x</i>.</p><p><strong>−12</strong> — ozod had.</p>"),
    q("A company's daily profit, in dollars, from selling <i>n</i> units is <i>n</i>(60 − <i>n</i>). Which of the following numbers of units gives a daily profit of $800?", ["10", "20", "25", "30", "50"], "20",
      "<p><strong>20.</strong> <i>n</i><sup>2</sup> − 60<i>n</i> + 800 = 0 → <i>n</i> = 20 yoki 40.</p><p><strong>30</strong> — eng katta foyda (900) beradigan son, 800 emas.</p>"),
    q("The revenue from selling a product at <i>p</i> dollars is <i>p</i>(100 − <i>p</i>) dollars. Which price gives the greatest revenue?", ["25", "40", "50", "60", "100"], "50",
      "<p><strong>50.</strong> Ildizlar 0 va 100 — eng yuqori nuqta ularning oʻrtasida.</p><p><strong>100</strong> — tushum nolga teng boʻladigan narx.</p>"),
    q("The product of two consecutive positive integers is 132. What is the larger integer?", ["10", "11", "12", "13", "66"], "12",
      "<p><strong>12.</strong> 11 × 12 = 132.</p><p><strong>11</strong> — kichigi.</p>"),
    q("When each of <i>n</i> people shakes hands once with every other person, there are <i>n</i>(<i>n</i> − 1)/2 handshakes. If there were 45 handshakes, how many people were there?", ["9", "10", "11", "15", "45"], "10",
      "<p><strong>10.</strong> <i>n</i>(<i>n</i> − 1) = 90 = 10 × 9.</p><p><strong>9</strong> — <i>n</i> − 1 ning qiymati.</p>"),
    q(f"If {X}{SQ} = 4{X}, which of the following gives all possible values of {X}?", ["4 only", "0 only", "0 and 4", "−4 and 4", "2 only"], "0 and 4",
      "<p><strong>0 and 4.</strong> <i>x</i>(<i>x</i> − 4) = 0.</p><p><strong>4 only</strong> — <i>x</i> ga boʻlib, 0 ni yoʻqotgan javob.</p>"),
    q(f"If ({X} − 2){SQ} = 25, what is the sum of all possible values of {X}?", ["−3", "4", "7", "10", "27"], "4",
      "<p><strong>4.</strong> <i>x</i> − 2 = 5 yoki −5 → 7 yoki −3.</p><p><strong>7</strong> — faqat musbat ildizni olgan javob.</p>"),
    q(f"If {X} + 1/{X} = 4, what is the value of {X}{SQ} + 1/{X}{SQ}?", ["12", "14", "16", "18", "20"], "14",
      "<p><strong>14.</strong> Kvadratga koʻtaramiz: <i>x</i><sup>2</sup> + 2 + 1/<i>x</i><sup>2</sup> = 16.</p><p><strong>16</strong> — oʻrta had 2 ni ayirmagan javob.</p>"),
    q(f"For how many integers <i>n</i> is <i>n</i>{SQ} − 10<i>n</i> + 21 negative?", ["2", "3", "4", "5", "7"], "3",
      "<p><strong>3.</strong> (<i>n</i> − 3)(<i>n</i> − 7) &lt; 0 → 3 &lt; <i>n</i> &lt; 7: 4, 5, 6.</p><p><strong>5</strong> — 3 va 7 ni ham sanagan javob; ularda ifoda nolga teng.</p>"),
    q("A bakery finds that if it charges <i>p</i> dollars per cake, it sells 40 − <i>p</i> cakes per day. Daily revenue is $300 at two different prices. What is the lower of these two prices?", ["5", "10", "15", "20", "30"], "10",
      "<p><strong>10.</strong> <i>p</i>(40 − <i>p</i>) = 300 → (<i>p</i> − 10)(<i>p</i> − 30) = 0.</p><p><strong>30</strong> — yuqori narx.</p>"),
    q("A firm's monthly profit, in thousands of dollars, is −<i>m</i><sup>2</sup> + 12<i>m</i> − 20 when it makes <i>m</i> hundred units. For how many whole-number values of <i>m</i> is the profit positive?", ["6", "7", "8", "9", "10"], "7",
      "<p><strong>7.</strong> <i>m</i><sup>2</sup> − 12<i>m</i> + 20 &lt; 0 → (<i>m</i> − 2)(<i>m</i> − 10) &lt; 0 → <i>m</i> = 3, …, 9.</p><p><strong>9</strong> — 2 va 10 ni ham qoʻshgan javob; ularda foyda nol.</p>"),
]

# =====================================================================
# GMAT-20 — functions and custom operations
# =====================================================================
Q20 = [
    q(f"If <i>f</i>({X}) = 4{X} − 1, what is <i>f</i>(5)?", ["9", "19", "20", "21", "24"], "19",
      "<p><strong>19.</strong> 20 − 1.</p><p><strong>21</strong> — 1 ni qoʻshgan javob.</p>"),
    q(f"If <i>f</i>({X}) = {X}{SQ} + 3, what is <i>f</i>(−3)?", ["−6", "0", "6", "9", "12"], "12",
      "<p><strong>12.</strong> (−3)<sup>2</sup> + 3 = 9 + 3.</p><p><strong>−6</strong> — (−3)<sup>2</sup> ni −9 deb olgan javob.</p>"),
    q(f"If <i>g</i>({X}) = 10 − 2{X} and <i>g</i>({X}) = 4, what is {X}?", ["3", "4", "6", "7", "14"], "3",
      "<p><strong>3.</strong> 10 − 2<i>x</i> = 4.</p><p><strong>7</strong> — 2<i>x</i> = 14 deb ishorani adashtirgan javob.</p>"),
    q("For all numbers <i>a</i> and <i>b</i>, <i>a</i> ◆ <i>b</i> = 2<i>a</i> + 3<i>b</i>. What is 4 ◆ 5?", ["9", "20", "22", "23", "26"], "23",
      "<p><strong>23.</strong> 8 + 15.</p><p><strong>22</strong> — <i>a</i> va <i>b</i> ni almashtirgan javob (10 + 12).</p>"),
    q(f"If <i>f</i>({X}) = {X} + 2 and <i>g</i>({X}) = 3{X}, what is <i>f</i>(<i>g</i>(4))?", ["9", "12", "14", "18", "24"], "14",
      "<p><strong>14.</strong> <i>g</i>(4) = 12, <i>f</i>(12) = 14.</p><p><strong>18</strong> — <i>g</i>(<i>f</i>(4)): tartib almashgan.</p>"),
    q(f"If <i>f</i>({X}) = 2{X} − 1, what is <i>f</i>(<i>f</i>(3))?", ["5", "9", "10", "11", "25"], "9",
      "<p><strong>9.</strong> <i>f</i>(3) = 5, <i>f</i>(5) = 9.</p><p><strong>25</strong> — <i>f</i>(3) ni kvadratga koʻtargan javob.</p>"),
    q(f"If <i>f</i>({X}) = {X}{SQ} − {X}, which of the following is equal to <i>f</i>(<i>a</i> + 1) − <i>f</i>(<i>a</i>)?", ["1", "2<i>a</i>", "2<i>a</i> + 1", f"<i>a</i>{SQ}", f"2<i>a</i>{SQ}"], "2<i>a</i>",
      "<p><strong>2a.</strong> (<i>a</i> + 1)<sup>2</sup> − (<i>a</i> + 1) − <i>a</i><sup>2</sup> + <i>a</i> = 2<i>a</i>. Tekshiruv: <i>a</i> = 3 → <i>f</i>(4) − <i>f</i>(3) = 12 − 6 = 6 ✓.</p><p><strong>2a + 1</strong> — −(<i>a</i> + 1) dagi −1 ni unutgan javob.</p>"),
    q(f"For all numbers {X} and <i>y</i> with {X} ≠ <i>y</i>, {X} ⊗ <i>y</i> = ({X} + <i>y</i>)/({X} − <i>y</i>). What is 5 ⊗ 3?", ["0.25", "1", "2", "4", "8"], "4",
      "<p><strong>4.</strong> 8 ÷ 2.</p><p><strong>0.25</strong> — kasrni agʻdarib hisoblagan javob.</p>"),
    q(f"If <i>f</i>({X}) = <i>k</i>{X} + 3 and <i>f</i>(2) = 11, what is the value of <i>k</i>?", ["2", "4", "5.5", "7", "8"], "4",
      "<p><strong>4.</strong> 2<i>k</i> + 3 = 11.</p><p><strong>5.5</strong> — 3 ni ayirmagan javob (11 ÷ 2).</p>"),
    q(f"If <i>f</i>({X}) = 3{X} + <i>c</i> and <i>f</i>(4) = 20, what is <i>f</i>(−1)?", ["−5", "2", "5", "8", "11"], "5",
      "<p><strong>5.</strong> <i>c</i> = 8; <i>f</i>(−1) = −3 + 8.</p><p><strong>8</strong> — <i>c</i> ning qiymati.</p>"),
    q("A taxi fare, in dollars, for a trip of <i>d</i> kilometers is <i>F</i>(<i>d</i>) = 2.50 + 1.20<i>d</i>. What is the fare for a 15-kilometer trip?", ["$18.00", "$19.50", "$20.50", "$21.00", "$37.50"], "$20.50",
      "<p><strong>$20.50.</strong> 2.50 + 18.</p><p><strong>$18.00</strong> — boshlangʻich toʻlovni unutgan javob.</p>"),
    q("A company's cost of making <i>n</i> units is <i>C</i>(<i>n</i>) = 800 + 15<i>n</i> dollars, and its revenue is <i>R</i>(<i>n</i>) = 25<i>n</i> dollars. What is its profit when <i>n</i> = 200?", ["$1,200", "$2,000", "$2,200", "$3,000", "$5,000"], "$1,200",
      "<p><strong>$1,200.</strong> 5,000 − 3,800.</p><p><strong>$2,000</strong> — doimiy 800 ni ayirmagan javob.</p>"),
    q("A machine's value <i>t</i> years after purchase is <i>V</i>(<i>t</i>) = 24,000 − 3,000<i>t</i> dollars. After how many years is its value $9,000?", ["3", "4", "5", "8", "11"], "5",
      "<p><strong>5.</strong> 3,000<i>t</i> = 15,000.</p><p><strong>3</strong> — 9,000 ni 3,000 ga boʻlgan javob.</p>"),
    q("A subscription costs <i>S</i>(<i>m</i>) = 15<i>m</i> − 5 dollars for <i>m</i> months. What is <i>S</i>(12) − <i>S</i>(10)?", ["$10", "$20", "$30", "$175", "$305"], "$30",
      "<p><strong>$30.</strong> 175 − 145.</p><p><strong>$175</strong> — faqat <i>S</i>(12).</p>"),
    q(f"If <i>f</i>({X}) = 2{X}{SQ}, which of the following is equal to <i>f</i>(3{X})?", [f"6{X}{SQ}", f"9{X}{SQ}", f"18{X}{SQ}", f"36{X}{SQ}", f"6{X}"], f"18{X}{SQ}",
      "<p><strong>18x².</strong> 2(3<i>x</i>)<sup>2</sup> = 2 × 9<i>x</i><sup>2</sup>.</p><p><strong>6x²</strong> — 3 ni kvadratga koʻtarmagan javob.</p>"),
    q(f"If <i>f</i>({X}) = {X} + 3 and <i>g</i>({X}) = {X}{SQ}, for what value of {X} is <i>f</i>(<i>g</i>({X})) = <i>g</i>(<i>f</i>({X}))?", ["−3", "−1", "0", "1", "3"], "−1",
      "<p><strong>−1.</strong> <i>x</i><sup>2</sup> + 3 = <i>x</i><sup>2</sup> + 6<i>x</i> + 9 → 6<i>x</i> = −6.</p><p><strong>0</strong> — har ikkala tomonda <i>x</i><sup>2</sup> qisqargach, qolganini tekshirmagan taxmin.</p>"),
    q("For all numbers <i>a</i> and <i>b</i>, <i>a</i> Δ <i>b</i> = <i>a</i><sup>2</sup> − <i>b</i><sup>2</sup>. What is (3 Δ 2) Δ 4?", ["1", "5", "9", "21", "65"], "9",
      "<p><strong>9.</strong> 3 Δ 2 = 5; 5 Δ 4 = 25 − 16.</p><p><strong>5</strong> — faqat qavs ichidagi natija.</p>"),
    q(f"If <i>f</i>({X}) = 1/({X} − 2), for which of the following values of {X} is <i>f</i>(<i>f</i>({X})) undefined?", ["0", "1.5", "2.5", "3", "4"], "2.5",
      "<p><strong>2.5.</strong> <i>f</i>(<i>f</i>(<i>x</i>)) aniqlanmagan, agar <i>f</i>(<i>x</i>) = 2: 1/(<i>x</i> − 2) = 2 → <i>x</i> = 2.5.</p><p><strong>3</strong> — <i>f</i>(3) = 1 hisoblangan, lekin <i>f</i>(1) = −1 aniqlangan.</p>"),
    q("Plan A charges 12 dollars a month plus 5 cents per minute; plan B charges 9 cents per minute and no monthly fee. For how many minutes in a month do the two plans cost the same?", ["120", "133", "240", "300", "400"], "300",
      "<p><strong>300.</strong> 12 + 0.05<i>m</i> = 0.09<i>m</i> → 0.04<i>m</i> = 12.</p><p><strong>133</strong> — 12 ni 0.09 ga boʻlgan javob.</p>"),
    q("A factory's daily output, in units, is <i>P</i>(<i>w</i>) = 50<i>w</i> − <i>w</i><sup>2</sup> when <i>w</i> workers are on shift. How many more units are produced with 20 workers than with 10 workers?", ["100", "200", "300", "400", "600"], "200",
      "<p><strong>200.</strong> <i>P</i>(20) = 600, <i>P</i>(10) = 400.</p><p><strong>600</strong> — faqat <i>P</i>(20).</p>"),
]

PRACTICES = [
    {
        "title": "GMAT-16 Practice: Overlapping Sets and Venn Tables",
        "description": "20 ta GMAT uslubidagi savol — ikki va uch toʻplam, 2 × 2 jadval, eng kichik va eng katta kesishma.",
        "tutorial": "GMAT-16:", "subject": "GMAT", "level": "medium", "questions": Q16,
    },
    {
        "title": "GMAT-17 Practice: Linear Equations and Systems",
        "description": "20 ta GMAT uslubidagi savol — chiziqli tenglamalar, sistemalar va matnli masalalar.",
        "tutorial": "GMAT-17:", "subject": "GMAT", "level": "medium", "questions": Q17,
    },
    {
        "title": "GMAT-18 Practice: Inequalities and Absolute Value",
        "description": "20 ta GMAT uslubidagi savol — tengsizliklar, modul, butun yechimlar va ruxsat etilgan chetlanish.",
        "tutorial": "GMAT-18:", "subject": "GMAT", "level": "medium", "questions": Q18,
    },
    {
        "title": "GMAT-19 Practice: Quadratics and Factoring",
        "description": "20 ta GMAT uslubidagi savol — koʻpaytuvchilarga ajratish, maxsus koʻpaytmalar va kvadrat tenglamalar.",
        "tutorial": "GMAT-19:", "subject": "GMAT", "level": "medium", "questions": Q19,
    },
    {
        "title": "GMAT-20 Practice: Functions and Custom Operations",
        "description": "20 ta GMAT uslubidagi savol — funksiyalar, kompozitsiya, oʻylab topilgan amallar va biznes formulalari.",
        "tutorial": "GMAT-20:", "subject": "GMAT", "level": "medium", "questions": Q20,
    },
]
