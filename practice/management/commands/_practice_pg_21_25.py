# -*- coding: utf-8 -*-
"""Prime GMAT mashqlar — GMAT-21 … GMAT-25 (sequences, counting, probability, statistics,
and a 20-question mixed review for the strategy lesson).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan. Savollar INGLIZCHA (imtihon
tili), tushuntirishlar OʻZBEKCHA. Har savolda BESHTA variant, raqamli variantlar oʻsish
tartibida. Kalkulyatorsiz yechiladigan arifmetika.

GMAT-25 Practice is a MIXED REVIEW of the whole Quant block (one question per topic, then
two word problems), and each explanation names the fastest route: backsolving, picking
numbers, or a logic check.

Import:
    python manage.py import_practices practice/management/commands/_practice_pg_21_25.py \\
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
# GMAT-21 — sequences
# =====================================================================
Q21 = [
    q("What is the 8th term of the sequence 5, 9, 13, 17, …?", ["29", "32", "33", "37", "40"], "33",
      "<p><strong>33.</strong> 5 + 7 × 4.</p><p><strong>37</strong> — 8 ta qadam olgan javob; birinchidan sakkizinchigacha 7 ta qadam.</p>"),
    q("What is the 6th term of the sequence 3, 6, 12, 24, …?", ["18", "36", "48", "96", "192"], "96",
      "<p><strong>96.</strong> 3 × 2<sup>5</sup>.</p><p><strong>192</strong> — bitta ortiqcha ikkilantirish (3 × 2<sup>6</sup>).</p>"),
    q("What is the sum of the integers from 1 to 100, inclusive?", ["4,950", "5,000", "5,050", "5,100", "10,100"], "5,050",
      "<p><strong>5,050.</strong> 100 × 101 ÷ 2.</p><p><strong>10,100</strong> — ikkiga boʻlishni unutgan javob.</p>"),
    q("How many terms are in the sequence 7, 11, 15, …, 99?", ["22", "23", "24", "25", "92"], "24",
      "<p><strong>24.</strong> (99 − 7) ÷ 4 + 1 = 23 + 1.</p><p><strong>23</strong> — qadamlar soni; hadlar bittaga koʻp.</p>"),
    q("In an arithmetic sequence the first term is 4 and the 10th term is 31. What is the common difference?", ["2.7", "3", "3.1", "3.5", "27"], "3",
      "<p><strong>3.</strong> 9 ta qadam: 27 ÷ 9.</p><p><strong>2.7</strong> — 27 ni 10 ga boʻlgan javob.</p>"),
    q("What is the sum of the first 15 positive odd integers?", ["196", "210", "225", "240", "256"], "225",
      "<p><strong>225.</strong> Birinchi <i>n</i> ta toq son yigʻindisi <i>n</i><sup>2</sup>.</p><p><strong>256</strong> — 16 ta toq son yigʻindisi.</p>"),
    q("What is the sum of the arithmetic sequence 10, 13, 16, …, 70?", ["800", "820", "840", "860", "1,680"], "840",
      "<p><strong>840.</strong> 21 ta had, oʻrtacha 40: 21 × 40.</p><p><strong>800</strong> — hadlarni 20 ta deb sanagan javob.</p>"),
    q("In a geometric sequence the first term is 81 and each term after the first is one third of the term before it. What is the 5th term?", ["1/3", "1", "3", "9", "27"], "1",
      "<p><strong>1.</strong> 81, 27, 9, 3, 1.</p><p><strong>1/3</strong> — bitta ortiqcha qadam.</p>"),
    q("In a sequence, <i>a</i><sub>1</sub> = 2 and each term after the first equals the square of the previous term minus 1. What is <i>a</i><sub>4</sub>?", ["15", "48", "63", "64", "80"], "63",
      "<p><strong>63.</strong> 2, 3, 8, 63.</p><p><strong>64</strong> — 1 ni ayirishni unutgan javob.</p>"),
    q("What is the sum of the integers from 20 to 60, inclusive?", ["1,600", "1,620", "1,640", "1,660", "3,280"], "1,640",
      "<p><strong>1,640.</strong> 41 ta had, oʻrtacha 40.</p><p><strong>1,600</strong> — hadlarni 40 ta deb sanagan javob.</p>"),
    q("A company earned $120,000 in its first year, and its revenue grows by $15,000 each year. What does it earn in its 8th year?", ["$210,000", "$225,000", "$240,000", "$255,000", "$1,380,000"], "$225,000",
      "<p><strong>$225,000.</strong> 120,000 + 7 × 15,000.</p><p><strong>$240,000</strong> — 8 ta oʻsish qoʻshilgan.</p>"),
    q("Using the same figures, what is the company's total revenue over its first 8 years?", ["$1,200,000", "$1,320,000", "$1,380,000", "$1,440,000", "$1,800,000"], "$1,380,000",
      "<p><strong>$1,380,000.</strong> 8 × (120,000 + 225,000) ÷ 2.</p><p><strong>$1,440,000</strong> — 8-yilni 240,000 deb olgan javob.</p>"),
    q("A savings plan deposits $100 in month 1, $110 in month 2, and $10 more each month after that. What is the total deposited in the first 12 months?", ["$1,320", "$1,800", "$1,860", "$1,920", "$2,520"], "$1,860",
      "<p><strong>$1,860.</strong> 12-oy 210; 12 × (100 + 210) ÷ 2.</p><p><strong>$1,920</strong> — 12-oyni 220 deb olgan javob.</p>"),
    q("A theater has 15 rows. The first row has 20 seats and each row has 2 more seats than the row in front of it. How many seats are there in total?", ["480", "495", "510", "525", "600"], "510",
      "<p><strong>510.</strong> Oxirgi qator 20 + 14 × 2 = 48; 15 × 68 ÷ 2.</p><p><strong>525</strong> — oxirgi qatorni 50 deb olgan javob.</p>"),
    q("How many multiples of 3 are there between 10 and 100?", ["27", "29", "30", "31", "33"], "30",
      "<p><strong>30.</strong> 12 dan 99 gacha: (99 − 12) ÷ 3 + 1.</p><p><strong>29</strong> — «+1» unutilgan.</p>"),
    q("The first term of a sequence is 5 and each term is 4 more than the term before it. Which term is equal to 101?", ["23rd", "24th", "25th", "26th", "96th"], "25th",
      "<p><strong>25th.</strong> 5 + (<i>n</i> − 1) × 4 = 101 → <i>n</i> − 1 = 24.</p><p><strong>24th</strong> — qadamlar sonini had raqami deb olgan javob.</p>"),
    q("What is the sum of all even integers from 2 to 200, inclusive, minus the sum of all odd integers from 1 to 199, inclusive?", ["1", "50", "100", "200", "10,100"], "100",
      "<p><strong>100.</strong> Juftlab: (2 − 1) + (4 − 3) + … — 100 ta juftning har biri 1.</p><p><strong>200</strong> — juftlar sonini 200 deb olgan javob.</p>"),
    q("In a sequence, each term after the second is the sum of the two terms before it. If the 5th term is 18 and the 6th term is 29, what is the 2nd term?", ["3", "4", "5", "7", "11"], "4",
      "<p><strong>4.</strong> Orqaga: 4-had 29 − 18 = 11, 3-had 18 − 11 = 7, 2-had 11 − 7 = 4.</p><p><strong>7</strong> — 3-had.</p>"),
    q("A bakery sells 150 loaves on its first day and 6 more loaves each day than the day before. How many loaves does it sell in total over the first 10 days?", ["1,500", "1,740", "1,770", "1,800", "2,040"], "1,770",
      "<p><strong>1,770.</strong> 10-kun 204; 10 × (150 + 204) ÷ 2.</p><p><strong>1,800</strong> — 10-kunni 210 deb olgan javob.</p>"),
    q("A startup had 500 users in its first month, and the number of users doubled every month after that. In which month did it first have more than 30,000 users?", ["5", "6", "7", "8", "60"], "7",
      "<p><strong>7.</strong> 500, 1,000, 2,000, 4,000, 8,000, 16,000, 32,000.</p><p><strong>60</strong> — 30,000 ni 500 ga boʻlgan javob: ikki baravar oshish qoʻshish emas.</p>"),
]

# =====================================================================
# GMAT-22 — counting
# =====================================================================
Q22 = [
    q("A restaurant offers 3 starters, 5 main courses and 2 desserts. How many different three-course meals are possible?", ["10", "15", "30", "60", "120"], "30",
      "<p><strong>30.</strong> 3 × 5 × 2.</p><p><strong>10</strong> — qoʻshilgan javob.</p>"),
    q("What is the value of 6! (6 factorial)?", ["36", "120", "360", "720", "5,040"], "720",
      "<p><strong>720.</strong> 6 × 5 × 4 × 3 × 2 × 1.</p><p><strong>5,040</strong> — 7!.</p>"),
    q("In how many ways can 2 people be chosen from 7?", ["14", "21", "42", "49", "5,040"], "21",
      "<p><strong>21.</strong> 7 × 6 ÷ 2.</p><p><strong>42</strong> — tartibni hisobga olgan javob.</p>"),
    q("In how many different orders can 4 different books be arranged on a shelf?", ["4", "16", "24", "64", "256"], "24",
      "<p><strong>24.</strong> 4!.</p><p><strong>256</strong> — takrorlanish mumkin deb hisoblangan (4<sup>4</sup>).</p>"),
    q("From 10 candidates, a president and a vice president are to be chosen. In how many ways can this be done?", ["20", "45", "90", "100", "200"], "90",
      "<p><strong>90.</strong> Lavozimlar har xil — tartib muhim: 10 × 9.</p><p><strong>45</strong> — tartib muhim emas deb hisoblangan javob.</p>"),
    q("From 10 candidates, a team of 2 is to be chosen. In how many ways can this be done?", ["20", "45", "90", "100", "200"], "45",
      "<p><strong>45.</strong> Jamoada oʻrin yoʻq: 10 × 9 ÷ 2.</p><p><strong>90</strong> — tartibni hisobga olgan javob.</p>"),
    q("How many 4-digit PINs can be formed from the digits 0 to 9 if digits may be repeated?", ["40", "5,040", "6,561", "9,000", "10,000"], "10,000",
      "<p><strong>10,000.</strong> 10<sup>4</sup>.</p><p><strong>5,040</strong> — takrorlanmasdan hisoblangan javob.</p>"),
    q("How many 4-digit PINs can be formed from the digits 0 to 9 if no digit may be repeated?", ["210", "3,024", "5,040", "6,561", "10,000"], "5,040",
      "<p><strong>5,040.</strong> 10 × 9 × 8 × 7.</p><p><strong>210</strong> — tartib muhim emas deb hisoblangan javob; PIN da tartib muhim.</p>"),
    q("How many different arrangements of the letters of the word BANANA are possible?", ["20", "60", "120", "360", "720"], "60",
      "<p><strong>60.</strong> 6! ÷ (3! × 2!) = 720 ÷ 12.</p><p><strong>720</strong> — bir xil harflarni hisobga olmagan javob.</p>"),
    q("A team is formed with 2 of 5 men and 2 of 4 women. How many different teams are possible?", ["20", "36", "60", "120", "126"], "60",
      "<p><strong>60.</strong> C(5, 2) × C(4, 2) = 10 × 6.</p><p><strong>126</strong> — 9 kishidan istalgan 4 tasini olgan javob.</p>"),
    q("An ice-cream shop has 8 flavors. A cup holds 2 different flavors, and the order of the scoops does not matter. How many different cups are possible?", ["16", "28", "56", "64", "72"], "28",
      "<p><strong>28.</strong> 8 × 7 ÷ 2.</p><p><strong>56</strong> — tartibni hisobga olgan javob.</p>"),
    q("A license plate has 2 letters (from 26) followed by 3 digits (from 0 to 9), and repetition is allowed. How many plates are possible?", ["6,760", "67,600", "676,000", "6,760,000", "17,576,000"], "676,000",
      "<p><strong>676,000.</strong> 26 × 26 × 10 × 10 × 10.</p><p><strong>67,600</strong> — bitta raqam oʻrnini unutgan javob.</p>"),
    q("A manager must schedule 5 different presentations in 5 time slots, and the budget presentation must be first. In how many ways can the presentations be scheduled?", ["4", "20", "24", "60", "120"], "24",
      "<p><strong>24.</strong> Birinchi oʻrin band; qolgan 4 tasi 4! usulda.</p><p><strong>120</strong> — shartni eʼtiborsiz qoldirgan javob.</p>"),
    q("A team of 3 is to be chosen from 6 analysts and 4 managers. In how many ways can the team include exactly 1 manager?", ["24", "36", "60", "80", "120"], "60",
      "<p><strong>60.</strong> 4 × C(6, 2) = 4 × 15.</p><p><strong>120</strong> — tahlilchilarni tartib bilan tanlagan javob (4 × 6 × 5).</p>"),
    q("In how many ways can 5 people sit in a row if two particular people must sit next to each other?", ["24", "48", "60", "96", "120"], "48",
      "<p><strong>48.</strong> Ikkalasi bitta blok: 4! = 24, blok ichida 2 tartib.</p><p><strong>24</strong> — blok ichidagi tartibni unutgan javob.</p>"),
    q("At a meeting of 8 people, each person shakes hands once with every other person. How many handshakes are there?", ["8", "16", "28", "56", "64"], "28",
      "<p><strong>28.</strong> C(8, 2) = 8 × 7 ÷ 2.</p><p><strong>56</strong> — har bir qoʻl siqish ikki marta sanalgan.</p>"),
    q("How many three-digit numbers have three different digits?", ["504", "648", "720", "729", "900"], "648",
      "<p><strong>648.</strong> Birinchi raqam 0 boʻlolmaydi: 9 × 9 × 8.</p><p><strong>720</strong> — 0 ni birinchi oʻringa ham qoʻygan javob (10 × 9 × 8).</p>"),
    q("A committee of 4 is chosen from 5 men and 3 women. How many committees include at least one woman?", ["5", "30", "60", "65", "70"], "65",
      "<p><strong>65.</strong> Hammasi: C(8, 4) = 70; ayolsiz: C(5, 4) = 5; 70 − 5.</p><p><strong>70</strong> — shartni eʼtiborsiz qoldirgan javob.</p>"),
    q("A café offers 4 kinds of bread, 5 fillings and 3 sauces. A sandwich has 1 bread, 2 different fillings and 1 sauce. How many different sandwiches are possible?", ["60", "120", "180", "240", "300"], "120",
      "<p><strong>120.</strong> 4 × C(5, 2) × 3 = 4 × 10 × 3.</p><p><strong>240</strong> — ichliklar tartibini hisobga olgan javob (4 × 20 × 3).</p>"),
    q("A marketing team of 9 must send 3 people to a conference in Seoul and 2 other people to a conference in Tokyo. In how many ways can this be done?", ["126", "420", "1,260", "2,520", "15,120"], "1,260",
      "<p><strong>1,260.</strong> C(9, 3) × C(6, 2) = 84 × 15.</p><p><strong>126</strong> — 9 tadan 5 kishilik guruhni bir martada tanlagan javob; kim qayerga ketishi ham muhim.</p>"),
]

# =====================================================================
# GMAT-23 — probability
# =====================================================================
Q23 = [
    q("A fair die is rolled. What is the probability of rolling an even number?", ["1/6", "1/3", "1/2", "2/3", "5/6"], "1/2",
      "<p><strong>1/2.</strong> 2, 4, 6 — 6 tadan 3 tasi.</p><p><strong>1/3</strong> — juft sonlarni 2 ta deb sanagan javob.</p>"),
    q("A bag contains 4 red and 6 blue marbles. One marble is drawn at random. What is the probability that it is red?", ["1/5", "1/3", "2/5", "3/5", "2/3"], "2/5",
      "<p><strong>2/5.</strong> 4 ÷ 10.</p><p><strong>2/3</strong> — qizilni koʻkka boʻlgan javob (4 ÷ 6).</p>"),
    q("If the probability of event A is 0.35, what is the probability that A does not occur?", ["0.35", "0.5", "0.65", "0.7", "1.35"], "0.65",
      "<p><strong>0.65.</strong> 1 − 0.35.</p><p><strong>1.35</strong> — ehtimollik 1 dan oshmaydi.</p>"),
    q("Two fair coins are tossed. What is the probability that both show heads?", ["1/8", "1/4", "1/3", "1/2", "3/4"], "1/4",
      "<p><strong>1/4.</strong> 1/2 × 1/2.</p><p><strong>1/3</strong> — natijalarni 3 ta (0, 1, 2 gerb) deb sanagan javob; ular teng ehtimolli emas.</p>"),
    q("Two fair dice are rolled. What is the probability that the sum is 8?", ["1/12", "5/36", "1/6", "2/9", "1/4"], "5/36",
      "<p><strong>5/36.</strong> (2,6), (3,5), (4,4), (5,3), (6,2).</p><p><strong>1/12</strong> — (4,4) dan tashqari juftlarni bir marta sanagan javob.</p>"),
    q("A bag contains 5 red and 3 green balls. Two balls are drawn at random without replacement. What is the probability that both are green?", ["3/56", "3/28", "9/64", "15/56", "3/8"], "3/28",
      "<p><strong>3/28.</strong> 3/8 × 2/7.</p><p><strong>9/64</strong> — qaytarib olgan deb hisoblangan javob.</p>"),
    q("Independent events A and B have probabilities 0.6 and 0.5. What is the probability that both occur?", ["0.1", "0.3", "0.55", "0.8", "1.1"], "0.3",
      "<p><strong>0.3.</strong> 0.6 × 0.5.</p><p><strong>0.8</strong> — kamida bittasi.</p>"),
    q("A fair die is rolled twice. What is the probability of getting at least one 6?", ["1/36", "1/6", "11/36", "1/3", "25/36"], "11/36",
      "<p><strong>11/36.</strong> 1 − (5/6)<sup>2</sup> = 1 − 25/36.</p><p><strong>1/3</strong> — ehtimollarni qoʻshgan javob; (6,6) ikki marta sanaldi.</p>"),
    q("An integer from 1 to 20 is chosen at random. What is the probability that it is a multiple of 3 or a multiple of 5?", ["7/20", "2/5", "9/20", "1/2", "11/20"], "9/20",
      "<p><strong>9/20.</strong> 3 ning karralilari 6 ta, 5 niki 4 ta, ikkalasi (15) 1 ta: 6 + 4 − 1 = 9.</p><p><strong>1/2</strong> — 15 ni ikki marta sanagan javob.</p>"),
    q("A fair coin is tossed 3 times. What is the probability of getting exactly 2 heads?", ["1/8", "1/4", "3/8", "1/2", "7/8"], "3/8",
      "<p><strong>3/8.</strong> GGR, GRG, RGG — 8 tadan 3 tasi.</p><p><strong>1/8</strong> — faqat bitta tartibni hisoblagan javob.</p>"),
    q("15% of a factory's products are defective. Two products are chosen at random, independently. What is the probability that both are free of defects?", ["0.0225", "0.255", "0.7", "0.7225", "0.85"], "0.7225",
      "<p><strong>0.7225.</strong> 0.85 × 0.85.</p><p><strong>0.7</strong> — 15% ni ikki marta ayirgan javob.</p>"),
    q("A firm has 12 men and 8 women. One employee is chosen at random for an award. What is the probability that the employee is a woman?", ["1/5", "1/3", "2/5", "1/2", "2/3"], "2/5",
      "<p><strong>2/5.</strong> 8 ÷ 20.</p><p><strong>2/3</strong> — ayollarni erkaklarga boʻlgan javob.</p>"),
    q("Two of 5 candidates, one of whom is Aziz, are chosen at random for interviews. What is the probability that Aziz is chosen?", ["1/10", "1/5", "1/4", "2/5", "1/2"], "2/5",
      "<p><strong>2/5.</strong> Juftlar 10 ta, Aziz 4 tasida.</p><p><strong>1/5</strong> — faqat bitta oʻrin bor deb hisoblangan javob.</p>"),
    q("Each sales call succeeds with probability 0.2, independently of the others. What is the probability of at least one success in 3 calls?", ["0.008", "0.2", "0.488", "0.6", "0.8"], "0.488",
      "<p><strong>0.488.</strong> 1 − 0.8<sup>3</sup> = 1 − 0.512.</p><p><strong>0.6</strong> — 3 × 0.2 deb qoʻshgan javob.</p>"),
    q("The probability of rain is 0.4 on Saturday and 0.4 on Sunday, independently. What is the probability that it rains on at least one of the two days?", ["0.16", "0.4", "0.48", "0.64", "0.8"], "0.64",
      "<p><strong>0.64.</strong> 1 − 0.6 × 0.6.</p><p><strong>0.8</strong> — ehtimollarni qoʻshgan javob.</p>"),
    q("A box contains 2 defective and 8 good chips. Two chips are chosen at random without replacement. What is the probability that exactly one is defective?", ["4/25", "8/45", "8/25", "16/45", "2/5"], "16/45",
      "<p><strong>16/45.</strong> Ikki tartib: 2/10 × 8/9 + 8/10 × 2/9 = 32/90.</p><p><strong>8/45</strong> — faqat bitta tartibni hisoblagan javob.</p>"),
    q("Three people each choose an integer from 1 to 3 at random, independently. What is the probability that all three choose different numbers?", ["1/27", "1/9", "2/9", "1/3", "2/3"], "2/9",
      "<p><strong>2/9.</strong> 3! = 6 ta qulay natija, jami 27.</p><p><strong>1/27</strong> — faqat bitta tartibni hisoblagan javob.</p>"),
    q("A committee of 2 is chosen at random from 4 men and 3 women. What is the probability that it includes at least one woman?", ["2/7", "3/7", "4/7", "5/7", "6/7"], "5/7",
      "<p><strong>5/7.</strong> 1 − C(4, 2)/C(7, 2) = 1 − 6/21.</p><p><strong>2/7</strong> — faqat erkaklar ehtimoli.</p>"),
    q("At an online shop, 30% of visitors add an item to their basket, and 40% of those visitors complete a purchase. What percent of all visitors complete a purchase?", ["10%", "12%", "28%", "40%", "70%"], "12%",
      "<p><strong>12%.</strong> 0.3 × 0.4.</p><p><strong>70%</strong> — foizlarni qoʻshgan javob.</p>"),
    q("A machine has two independent alarms, and each works with probability 0.9. What is the probability that at least one alarm works when needed?", ["0.81", "0.9", "0.95", "0.99", "1"], "0.99",
      "<p><strong>0.99.</strong> Ikkalasi ham ishlamasligi: 0.1 × 0.1 = 0.01.</p><p><strong>0.81</strong> — ikkalasi ham ishlashi.</p>"),
]

# =====================================================================
# GMAT-24 — statistics
# =====================================================================
Q24 = [
    q("What is the mean of 4, 8, 15, 16, 23 and 42?", ["15", "15.5", "18", "19", "23"], "18",
      "<p><strong>18.</strong> 108 ÷ 6.</p><p><strong>15.5</strong> — mediana.</p>"),
    q("What is the median of 4, 8, 15, 16, 23 and 42?", ["15", "15.5", "16", "18", "19"], "15.5",
      "<p><strong>15.5.</strong> Oʻrtadagi ikki son: (15 + 16) ÷ 2.</p><p><strong>18</strong> — oʻrtacha.</p>"),
    q("What is the range of 12, 7, 25, 3, 18?", ["15", "18", "22", "25", "28"], "22",
      "<p><strong>22.</strong> 25 − 3.</p><p><strong>25</strong> — eng katta qiymatning oʻzi.</p>"),
    q("What is the mode of 2, 3, 3, 5, 7, 7, 7, 9?", ["3", "5", "5.375", "7", "9"], "7",
      "<p><strong>7.</strong> Uch marta uchraydi.</p><p><strong>5.375</strong> — oʻrtacha.</p>"),
    q("What is the median of 9, 2, 14, 6, 11, 3, 8?", ["6", "7.57", "8", "9", "11"], "8",
      "<p><strong>8.</strong> 2, 3, 6, 8, 9, 11, 14.</p><p><strong>6</strong> — yozilgan tartibdagi oʻrtadagi son; avval tartiblash kerak.</p>"),
    q("The mean of 3, 5, 7 and <i>x</i> is 6. What is the value of <i>x</i>?", ["5", "6", "8", "9", "24"], "9",
      "<p><strong>9.</strong> Yigʻindi 24; 24 − 15.</p><p><strong>24</strong> — yigʻindining oʻzi.</p>"),
    q("Every number in a data set with standard deviation 4 is multiplied by 3. What is the standard deviation of the new data set?", ["4", "7", "12", "16", "36"], "12",
      "<p><strong>12.</strong> Koʻpaytirilsa, chetlanish ham shuncha marta oshadi.</p><p><strong>36</strong> — 3<sup>2</sup> ga koʻpaytirgan javob.</p>"),
    q("Every number in a data set with standard deviation 4 is increased by 5. What is the standard deviation of the new data set?", ["0", "4", "5", "9", "20"], "4",
      "<p><strong>4.</strong> Hamma qiymat birga suriladi — tarqoqlik oʻzgarmaydi.</p><p><strong>9</strong> — 5 ni chetlanishga ham qoʻshgan javob.</p>"),
    q("Which of the following data sets has the smallest standard deviation?", ["2, 4, 6, 8", "4, 5, 6, 7", "5, 5, 6, 6", "1, 5, 6, 10", "0, 5, 6, 11"], "5, 5, 6, 6",
      "<p><strong>5, 5, 6, 6.</strong> Barcha qiymatlar oʻrtachadan (5.5) atigi 0.5 uzoqda.</p><p><strong>4, 5, 6, 7</strong> — oraliq 3, chetlanish kattaroq.</p>"),
    q("What is the median of the integers from 11 to 50, inclusive?", ["30", "30.5", "31", "39", "40"], "30.5",
      "<p><strong>30.5.</strong> 40 ta son — oʻrtadagi ikkitasi 30 va 31.</p><p><strong>30</strong> — juft sonli toʻplamda bitta oʻrta sonni olgan javob.</p>"),
    q("Five employees earn $3,000, $3,200, $3,500, $4,000 and $15,000 a month. By how much does the mean salary exceed the median salary?", ["$0", "$500", "$2,240", "$5,740", "$11,500"], "$2,240",
      "<p><strong>$2,240.</strong> Oʻrtacha 28,700 ÷ 5 = 5,740; mediana 3,500.</p><p><strong>$5,740</strong> — oʻrtachaning oʻzi.</p>"),
    q("A shop's daily sales for one week were 40, 52, 38, 61, 45, 52 and 70 units. What was the median daily sales figure?", ["45", "51.14", "52", "61", "70"], "52",
      "<p><strong>52.</strong> 38, 40, 45, 52, 52, 61, 70.</p><p><strong>51.14</strong> — oʻrtacha.</p>"),
    q("Delivery times, in minutes, were 25, 30, 30, 35, 40 and 50. By how many minutes does the mean exceed the median?", ["0", "2.5", "5", "7.5", "10"], "2.5",
      "<p><strong>2.5.</strong> Oʻrtacha 210 ÷ 6 = 35; mediana (30 + 35) ÷ 2 = 32.5.</p><p><strong>5</strong> — medianani 30 deb olgan javob.</p>"),
    q("Branch A's monthly sales were 50, 50 and 50; branch B's were 20, 50 and 80. Which of the following is true?", ["A has the greater standard deviation.", "B has the greater standard deviation.", "They have the same standard deviation.", "B has the greater mean.", "A has the greater range."], "B has the greater standard deviation.",
      "<p><strong>B has the greater standard deviation.</strong> Oʻrtachalar teng (50), lekin B ning qiymatlari undan 30 uzoqda, A niki — 0.</p><p><strong>B has the greater mean</strong> — ikkalasining oʻrtachasi 50.</p>"),
    q("If the number 20 is added to the data set {10, 20, 30}, which of the following changes?", ["The mean", "The median", "The standard deviation", "The range", "None of these"], "The standard deviation",
      "<p><strong>The standard deviation.</strong> 20 oʻrtachaga teng — oʻrtacha, mediana va oraliq oʻzgarmaydi, lekin tipik uzoqlik kamayadi.</p><p><strong>None of these</strong> — chetlanishni eʼtiborsiz qoldirgan javob.</p>"),
    q("What is the median of 7, 3, 9 and 1?", ["3", "5", "6", "7", "8"], "5",
      "<p><strong>5.</strong> 1, 3, 7, 9 → (3 + 7) ÷ 2.</p><p><strong>6</strong> — tartiblamasdan oʻrtadagi 3 va 9 ni olgan javob.</p>"),
    q("A set of 5 positive integers, not necessarily different, has a median of 10 and a mean of 12. What is the greatest possible value of the largest integer?", ["26", "36", "37", "38", "48"], "38",
      "<p><strong>38.</strong> Yigʻindi 60; qolganlar iloji boricha kichik: 1, 1, 10, 10; 60 − 22.</p><p><strong>37</strong> — ikki eng kichik sonni 1 va 2 deb olgan javob; sonlar takrorlanishi mumkin.</p>"),
    q("The mean of 10 numbers is 15. If the largest number, 42, is removed, what is the mean of the remaining numbers?", ["12", "13", "13.5", "15", "16.2"], "12",
      "<p><strong>12.</strong> (150 − 42) ÷ 9 = 108 ÷ 9.</p><p><strong>13.5</strong> — qolgan yigʻindini 9 ga emas, 8 ga boʻlgan javob (108 ÷ 8); olib tashlangandan keyin 9 ta son qoladi.</p>"),
    q("A team has 4 people earning $2,000 a month and 1 person earning $7,000. A new hire earning $2,000 joins. What happens to the median monthly salary?", ["It falls by $1,000.", "It stays the same.", "It rises by $500.", "It rises by $1,000.", "It doubles."], "It stays the same.",
      "<p><strong>It stays the same.</strong> Oldin ham, keyin ham oʻrtadagi maosh $2,000.</p><p><strong>It falls by $1,000.</strong> — oʻrtacha haqida oʻylagan javob: oʻrtacha 3,000 dan taxminan 2,833 ga tushadi (17,000 ÷ 6).</p>"),
    q("A shop recorded weekly sales of 120, 135, 150, 165 and 180 units. If sales rise by 10 units in every week, what is the new range?", ["6", "60", "66", "70", "180"], "60",
      "<p><strong>60.</strong> Hamma qiymat 10 ga suriladi — oraliq oʻzgarmaydi: 190 − 130.</p><p><strong>70</strong> — oraliqqa ham 10 qoʻshgan javob.</p>"),
]

# =====================================================================
# GMAT-25 — mixed review (one per topic, then two word problems)
# =====================================================================
Q25 = [
    q("What is 0.25 × 360?", ["9", "72", "90", "900", "1,440"], "90",
      "<p><strong>90.</strong> 0.25 = 1/4: 360 ÷ 4. Tez yoʻl — kasr jadvali (GMAT-6).</p><p><strong>900</strong> — vergulni adashtirgan javob.</p>"),
    q("A price rises from $50 to $65. By what percent did it rise?", ["15%", "23%", "30%", "65%", "130%"], "30%",
      "<p><strong>30%.</strong> 15 ÷ 50 — eski narxga boʻlinadi (GMAT-5).</p><p><strong>23%</strong> — yangi narxga boʻlingan javob.</p>"),
    q("How many positive divisors does 60 have?", ["6", "8", "10", "12", "16"], "12",
      "<p><strong>12.</strong> 60 = 2<sup>2</sup> × 3 × 5; (2 + 1)(1 + 1)(1 + 1) (GMAT-3).</p><p><strong>8</strong> — 2 ning darajasini 1 deb olgan javob.</p>"),
    q("What is the remainder when 2<sup>15</sup> is divided by 5?", ["0", "1", "2", "3", "4"], "3",
      "<p><strong>3.</strong> 2 ning darajalari 5 ga boʻlganda qoldiqlar 2, 4, 3, 1 takrorlanadi; 15 ÷ 4 qoldiq 3 → uchinchisi, 3 (GMAT-7, GMAT-9).</p><p><strong>2</strong> — siklning birinchi elementini olgan javob.</p>"),
    q("Three numbers are in the ratio 3 : 4 : 5, and their sum is 96. What is the largest number?", ["24", "32", "36", "40", "48"], "40",
      "<p><strong>40.</strong> 12 qism, bir qism 8 (GMAT-10).</p><p><strong>32</strong> — oʻrtadagi son.</p>"),
    q("The average of five numbers is 14. Four of them are 10, 12, 15 and 18. What is the fifth number?", ["12", "14", "15", "16", "18"], "15",
      "<p><strong>15.</strong> 70 − 55 (GMAT-11).</p><p><strong>14</strong> — oʻrtachaning oʻzi.</p>"),
    q("Machine A can do a job in 3 hours and machine B in 6 hours. How many hours do they take working together?", ["1.5", "2", "3", "4.5", "9"], "2",
      "<p><strong>2.</strong> 1/3 + 1/6 = 1/2. Mantiqiy tekshiruv: javob 3 dan kam boʻlishi shart — 3, 4.5 va 9 darrov chiqib ketadi (GMAT-13).</p><p><strong>4.5</strong> — vaqtlarni oʻrtachalagan javob.</p>"),
    q("An item that cost a store $50 was sold for $60 after a 20% discount on its marked price. What was the marked price?", ["$62.50", "$70", "$72", "$75", "$80"], "$75",
      "<p><strong>$75.</strong> 0.8 × narx = 60. Orqaga yechish: 75 × 0.8 = 60 ✓ (GMAT-14).</p><p><strong>$72</strong> — 60 ga 20% qoʻshgan javob.</p>"),
    q("How much interest does $2,000 earn in 2 years at 10% compounded annually?", ["$200", "$400", "$420", "$441", "$2,420"], "$420",
      "<p><strong>$420.</strong> 2,000 → 2,200 → 2,420 (GMAT-15).</p><p><strong>$400</strong> — oddiy foiz; <strong>$2,420</strong> — jami summa.</p>"),
    q("Of 70 people, 40 belong to club A, 35 belong to club B and 10 belong to neither. How many belong to both clubs?", ["5", "10", "15", "20", "25"], "15",
      "<p><strong>15.</strong> 40 + 35 + 10 − 70 (GMAT-16).</p><p><strong>5</strong> — «hech biri»ni unutgan javob.</p>"),
    q("If <i>x</i> + 2<i>y</i> = 11 and 2<i>x</i> + <i>y</i> = 13, what is the value of <i>x</i> − <i>y</i>?", ["1", "2", "3", "5", "8"], "2",
      "<p><strong>2.</strong> Ikkinchisidan birinchisini ayiramiz — <i>x</i> va <i>y</i> ni alohida topish shart emas (GMAT-17).</p><p><strong>5</strong> — <i>x</i> ning qiymati.</p>"),
    q("How many integers <i>x</i> satisfy |<i>x</i> + 2| ≤ 3?", ["5", "6", "7", "8", "9"], "7",
      "<p><strong>7.</strong> −5 ≤ <i>x</i> ≤ 1: 1 − (−5) + 1 (GMAT-18).</p><p><strong>6</strong> — chetlardan birini unutgan javob.</p>"),
    q("What is the positive solution of <i>x</i><sup>2</sup> − <i>x</i> − 12 = 0?", ["2", "3", "4", "6", "12"], "4",
      "<p><strong>4.</strong> (<i>x</i> − 4)(<i>x</i> + 3) = 0. Orqaga yechish ham tez: 16 − 4 − 12 = 0 ✓ (GMAT-19).</p><p><strong>3</strong> — manfiy ildizning ishorasini oʻzgartirgan javob.</p>"),
    q("If <i>f</i>(<i>x</i>) = <i>x</i><sup>2</sup> − 2<i>x</i>, what is <i>f</i>(<i>f</i>(3))?", ["−3", "0", "3", "9", "15"], "3",
      "<p><strong>3.</strong> <i>f</i>(3) = 3, demak <i>f</i>(<i>f</i>(3)) = <i>f</i>(3) = 3 (GMAT-20).</p><p><strong>9</strong> — <i>f</i>(3) ni 9 deb (faqat <i>x</i><sup>2</sup>) hisoblagan javob.</p>"),
    q("What is the sum 3 + 6 + 9 + … + 60?", ["600", "610", "630", "660", "1,260"], "630",
      "<p><strong>630.</strong> 20 ta had, oʻrtacha 31.5 (GMAT-21).</p><p><strong>1,260</strong> — ikkiga boʻlishni unutgan javob.</p>"),
    q("In how many ways can a chair and a secretary be chosen from 5 people?", ["10", "20", "25", "60", "120"], "20",
      "<p><strong>20.</strong> Lavozimlar har xil: 5 × 4 (GMAT-22).</p><p><strong>10</strong> — tartib muhim emas deb hisoblangan javob.</p>"),
    q("Two fair dice are rolled. What is the probability that the sum is at most 4?", ["1/12", "1/9", "1/6", "2/9", "1/4"], "1/6",
      "<p><strong>1/6.</strong> Yigʻindi 2: 1 ta, 3: 2 ta, 4: 3 ta — 36 tadan 6 tasi (GMAT-23).</p><p><strong>1/12</strong> — faqat yigʻindi 4 ni sanagan javob.</p>"),
    q("What is the median of 12, 5, 8, 20, 15, 9?", ["9", "10.5", "11.5", "12", "15"], "10.5",
      "<p><strong>10.5.</strong> 5, 8, 9, 12, 15, 20 → (9 + 12) ÷ 2 (GMAT-24).</p><p><strong>11.5</strong> — oʻrtacha.</p>"),
    q("A shop raised a price by 20% and then lowered the new price by 25%. The final price was $90. What was the original price?", ["$90", "$95", "$100", "$105", "$120"], "$100",
      "<p><strong>$100.</strong> Orqaga yechish oʻrtadagi variantdan: 100 → 120 → 90 ✓. Koʻpaytuvchi: 1.2 × 0.75 = 0.9.</p><p><strong>$95</strong> — foizlarni qoʻshib, −5% deb hisoblagan javob.</p>"),
    q("This year a firm's revenue is 20% higher than last year and its costs are 10% lower. Last year its revenue was twice its costs. By what percent did its profit increase?", ["10%", "30%", "40%", "50%", "60%"], "50%",
      "<p><strong>50%.</strong> Qulay son: oʻtgan yil xarajat 100, tushum 200, foyda 100. Bu yil: 240 − 90 = 150.</p><p><strong>30%</strong> — foizlarni qoʻshgan javob (20 + 10).</p>"),
]

PRACTICES = [
    {
        "title": "GMAT-21 Practice: Sequences and Series",
        "description": "20 ta GMAT uslubidagi savol — arifmetik va geometrik ketma-ketlik, hadlar soni, yigʻindi.",
        "tutorial": "GMAT-21:", "subject": "GMAT", "level": "medium", "questions": Q21,
    },
    {
        "title": "GMAT-22 Practice: Counting — Permutations and Combinations",
        "description": "20 ta GMAT uslubidagi savol — koʻpaytirish qoidasi, oʻrin almashtirish, guruhlash.",
        "tutorial": "GMAT-22:", "subject": "GMAT", "level": "medium", "questions": Q22,
    },
    {
        "title": "GMAT-23 Practice: Probability",
        "description": "20 ta GMAT uslubidagi savol — oddiy ehtimollik, kamida bittasi, mustaqil hodisalar, qaytarmasdan olish.",
        "tutorial": "GMAT-23:", "subject": "GMAT", "level": "medium", "questions": Q23,
    },
    {
        "title": "GMAT-24 Practice: Statistics — Median, Range and Standard Deviation",
        "description": "20 ta GMAT uslubidagi savol — mediana, moda, oraliq va standart chetlanish.",
        "tutorial": "GMAT-24:", "subject": "GMAT", "level": "medium", "questions": Q24,
    },
    {
        "title": "GMAT-25 Practice: Mixed Quant Review",
        "description": "20 ta aralash savol — butun Quant kursidan bittadan; tushuntirishlar eng tez yoʻlni koʻrsatadi.",
        "tutorial": "GMAT-25:", "subject": "GMAT", "level": "hard", "questions": Q25,
    },
]
