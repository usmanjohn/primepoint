# -*- coding: utf-8 -*-
"""Prime GMAT mashqlar — GMAT-11 … GMAT-15 (word problems, part one).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan. Savollar INGLIZCHA (imtihon
tili), tushuntirishlar OʻZBEKCHA. Har savolda BESHTA variant, raqamli variantlar oʻsish
tartibida. Kalkulyatorsiz yechiladigan arifmetika.

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context · 15–16 trap-spotting ·
      17–18 harder · 19–20 word problems (har doim ikkita).

Import:
    python manage.py import_practices practice/management/commands/_practice_pg_11_15.py \\
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


RATIOS5 = ["1 : 3", "1 : 2", "1 : 1", "2 : 1", "3 : 1"]

# =====================================================================
# GMAT-11 — averages
# =====================================================================
Q11 = [
    q("What is the average (arithmetic mean) of 6, 10, 14 and 22?", ["11", "12", "13", "14", "52"], "13",
      "<p><strong>13.</strong> Yigʻindi 52, 4 ga boʻlamiz.</p><p><strong>52</strong> — yigʻindining oʻzi; <strong>12</strong> — oʻrtadagi ikki sonning oʻrtachasi (mediana).</p>"),
    q("The average of five numbers is 18. What is the sum of the five numbers?", ["18", "23", "72", "90", "108"], "90",
      "<p><strong>90.</strong> Yigʻindi = oʻrtacha × soni = 18 × 5.</p><p><strong>23</strong> — 18 ga 5 ni qoʻshgan javob.</p>"),
    q("If the average of 3, 7 and <i>x</i> is 8, what is the value of <i>x</i>?", ["6", "8", "10", "14", "24"], "14",
      "<p><strong>14.</strong> Yigʻindi 3 × 8 = 24; 24 − 3 − 7 = 14.</p><p><strong>24</strong> — yigʻindining oʻzi.</p>"),
    q("What is the average of the integers from 11 to 29, inclusive?", ["19", "19.5", "20", "20.5", "29"], "20",
      "<p><strong>20.</strong> Teng oraliqli toʻplam: (11 + 29) ÷ 2.</p><p><strong>19.5</strong> — oʻrtachani taxmin bilan topishga urinish; teng oraliqli toʻplamda aniq javob — birinchi va oxirgisining oʻrtachasi.</p>"),
    q("The average of four numbers is 30. When a fifth number, 50, is added, what is the new average?", ["32", "34", "35", "40", "50"], "34",
      "<p><strong>34.</strong> (120 + 50) ÷ 5 = 34.</p><p><strong>40</strong> — 30 va 50 ning oddiy oʻrtachasi; 30 — toʻrtta sonning oʻrtachasi, bitta son emas.</p>"),
    q("The average of six numbers is 15. When one number is removed, the average of the remaining five numbers is 14. What number was removed?", ["1", "14", "15", "19", "20"], "20",
      "<p><strong>20.</strong> 6 × 15 − 5 × 14 = 90 − 70 = 20.</p><p><strong>1</strong> — oʻrtachalar farqi; olib tashlangan son = yigʻindilar farqi.</p>"),
    q("If the average of <i>x</i>, 2<i>x</i> and 3<i>x</i> is 24, what is the value of <i>x</i>?", ["4", "6", "8", "12", "24"], "12",
      "<p><strong>12.</strong> 6<i>x</i> ÷ 3 = 2<i>x</i> = 24.</p><p><strong>4</strong> — 24 ni 6 ga boʻlib, 3 ga boʻlishni unutgan javob.</p>"),
    q("A class of 10 students has an average score of 60, and another class of 15 students has an average score of 80. What is the average score of all 25 students?", ["68", "70", "72", "74", "75"], "72",
      "<p><strong>72.</strong> (600 + 1,200) ÷ 25 = 72.</p><p><strong>70</strong> — ikki oʻrtachaning oddiy oʻrtachasi; katta sinf 80 tomonga tortadi.</p>"),
    q("The average of seven consecutive integers is 20. What is the largest of the seven integers?", ["20", "21", "22", "23", "26"], "23",
      "<p><strong>23.</strong> Ketma-ket sonlarda oʻrtacha — oʻrtadagi son: 17, …, 20, …, 23.</p><p><strong>26</strong> — 20 dan 6 qadam yuqori; oʻrtadagi sondan 3 ta yuqorida turadi.</p>"),
    q("The average of <i>a</i> and <i>b</i> is 40, and the average of <i>b</i> and <i>c</i> is 55. What is the value of <i>c</i> − <i>a</i>?", ["15", "30", "40", "55", "95"], "30",
      "<p><strong>30.</strong> <i>a</i> + <i>b</i> = 80, <i>b</i> + <i>c</i> = 110; ayirsak, <i>c</i> − <i>a</i> = 30.</p><p><strong>15</strong> — oʻrtachalar farqi; yigʻindilar farqi ikki baravar katta.</p>"),
    q("A store sold 120 items on Monday, 150 on Tuesday, 90 on Wednesday and 160 on Thursday. What was the average number of items sold per day?", ["120", "125", "130", "135", "140"], "130",
      "<p><strong>130.</strong> 520 ÷ 4.</p><p><strong>125</strong> — eng katta va eng kichik sonning oʻrtachasi (90 va 160).</p>"),
    q("A salesperson needs average monthly sales of $5,000 over four months. Sales in the first three months were $4,200, $5,100 and $4,700. What must sales be in the fourth month?", ["$4,667", "$5,000", "$5,600", "$6,000", "$6,400"], "$6,000",
      "<p><strong>$6,000.</strong> Kerakli yigʻindi 20,000; uch oyda 14,000.</p><p><strong>$5,000</strong> — maqsad oʻrtachaning oʻzi; kamomadni qoplash uchun undan koʻp kerak.</p>"),
    q("A company's 30 employees have an average age of 32. Ten new employees with an average age of 24 join. What is the new average age?", ["26", "28", "29", "30", "31"], "30",
      "<p><strong>30.</strong> (960 + 240) ÷ 40 = 30.</p><p><strong>28</strong> — oʻrtachalarning oddiy oʻrtachasi; eski guruh uch baravar katta.</p>"),
    q("The average score of 25 students on a test was 72. Later the teacher found that one score had been recorded as 46 instead of 96. What is the correct average?", ["70", "72", "73", "74", "76"], "74",
      "<p><strong>74.</strong> Yigʻindi 50 ga ortadi; 50 ÷ 25 = 2; 72 + 2.</p><p><strong>72</strong> — xatoni tuzatmagan javob; yigʻindidagi 50 lik farq 25 ta oʻquvchiga boʻlinadi.</p>"),
    q("A driver travels from city A to city B at 60 kilometers per hour and returns along the same road at 40 kilometers per hour. What is the average speed for the round trip, in kilometers per hour?", ["45", "48", "50", "52", "55"], "48",
      "<p><strong>48.</strong> Masofani 120 km deb olaylik: borish 2 soat, qaytish 3 soat; 240 ÷ 5 = 48.</p><p><strong>50</strong> — tezliklarni oʻrtachalagan javob; sekin yoʻlda koʻproq vaqt oʻtadi.</p>"),
    q("The average of 10 numbers is 50. If 5 is added to each of the numbers, what is the new average?", ["50", "55", "60", "100", "500"], "55",
      "<p><strong>55.</strong> Har bir son 5 ga oshsa, oʻrtacha ham 5 ga oshadi.</p><p><strong>100</strong> — yigʻindiga qoʻshilgan 50 ni oʻrtachaga qoʻshgan javob.</p>"),
    q("The average of five different positive integers is 10. What is the greatest possible value of the largest of these integers?", ["14", "26", "36", "40", "46"], "40",
      "<p><strong>40.</strong> Yigʻindi 50; qolgan toʻrttasi iloji boricha kichik: 1 + 2 + 3 + 4 = 10; 50 − 10 = 40.</p><p><strong>46</strong> — sonlar har xil boʻlishini unutib, toʻrtta 1 olgan javob.</p>"),
    q("Group A has an average score of 70 and group B has an average score of 85. The combined average of the two groups is 79. What is the ratio of the number of people in group A to the number in group B?", ["1 : 2", "2 : 3", "1 : 1", "3 : 2", "2 : 1"], "2 : 3",
      "<p><strong>2 : 3.</strong> Uzoqliklar: 79 − 70 = 9, 85 − 79 = 6. Nisbat teskari: A : B = 6 : 9 = 2 : 3.</p><p><strong>3 : 2</strong> — uzoqliklarni toʻgʻridan-toʻgʻri olgan javob; 79 — 85 ga yaqin, demak B guruh katta.</p>"),
    q("A shop sold 30 shirts at $20 each and 20 shirts at $35 each. What was the average price per shirt sold?", ["$24", "$26", "$27.50", "$28", "$30"], "$26",
      "<p><strong>$26.</strong> (600 + 700) ÷ 50 = 26.</p><p><strong>$27.50</strong> — ikki narxning oddiy oʻrtachasi; arzon koʻylak koʻproq sotilgan.</p>"),
    q("A team's average score over its first 8 games is 75. What score must it make in the ninth game to raise its average to 77?", ["77", "79", "85", "91", "93"], "93",
      "<p><strong>93.</strong> 9 × 77 − 8 × 75 = 693 − 600 = 93.</p><p><strong>79</strong> — oʻrtachaga 2 ni qoʻshgan javob; yangi oʻyin oldingi 8 ta oʻyinning har biriga 2 tadan «qarz uzishi» kerak.</p>"),
]

# =====================================================================
# GMAT-12 — mixtures
# =====================================================================
Q12 = [
    q("How many liters of acid are in 25 liters of a 12% acid solution?", ["0.3", "2.5", "3", "12", "13"], "3",
      "<p><strong>3.</strong> 0.12 × 25 = 3.</p><p><strong>2.5</strong> — 10% bilan hisoblagan taxmin.</p>"),
    q("A 40-liter drink contains 8 liters of juice. What percent of the drink is juice?", ["5%", "8%", "20%", "32%", "40%"], "20%",
      "<p><strong>20%.</strong> 8 ÷ 40 = 0.2.</p><p><strong>5%</strong> — teskari boʻlingan (40 ÷ 8).</p>"),
    q("10 liters of a 10% solution are mixed with 30 liters of a 30% solution. What is the concentration of the mixture?", ["15%", "20%", "25%", "27.5%", "40%"], "25%",
      "<p><strong>25%.</strong> (1 + 9) ÷ 40 = 0.25.</p><p><strong>20%</strong> — foizlarning oddiy oʻrtachasi; 30% li eritma uch baravar koʻp.</p>"),
    q("5 liters of water are added to 20 liters of a 25% salt solution. What is the concentration of the new solution?", ["5%", "15%", "20%", "25%", "30%"], "20%",
      "<p><strong>20%.</strong> Tuz 5 L, hajm 25 L.</p><p><strong>25%</strong> — suv qoʻshilganda foiz oʻzgarmaydi deb oʻylagan javob.</p>"),
    q("How many liters of water must be added to 12 liters of a 50% solution to produce a 30% solution?", ["4", "6", "8", "12", "20"], "8",
      "<p><strong>8.</strong> Modda 6 L; 30% da hajm 6 ÷ 0.3 = 20 L; 20 − 12 = 8.</p><p><strong>20</strong> — yangi umumiy hajm.</p>"),
    q("How many liters of pure alcohol must be added to 30 liters of a 10% alcohol solution to produce a 25% solution?", ["4.5", "5", "6", "7.5", "9"], "6",
      "<p><strong>6.</strong> (3 + <i>a</i>) ÷ (30 + <i>a</i>) = 0.25 → 3 + <i>a</i> = 7.5 + 0.25<i>a</i> → <i>a</i> = 6. Tekshiruv: 9 ÷ 36 = 25% ✓.</p><p><strong>4.5</strong> — qoʻshilgan spirt hajmni ham oshirishini unutgan javob (7.5 − 3).</p>"),
    q("10 liters of water evaporate from 40 liters of a 20% salt solution. What is the concentration of the remaining solution?", ["20%", "25%", "26⅔%", "30%", "40%"], "26⅔%",
      "<p><strong>26⅔%.</strong> Tuz 8 L qoladi, hajm 30 L: 8 ÷ 30 = 4/15.</p><p><strong>25%</strong> — foizga 5 punkt qoʻshib taxmin qilgan javob; aniq hisob: 8 ÷ 30.</p>"),
    q("How many liters of a 20% solution must be mixed with 10 liters of a 50% solution to produce a 30% solution?", ["5", "10", "15", "20", "25"], "20",
      "<p><strong>20.</strong> 0.2<i>x</i> + 5 = 0.3(<i>x</i> + 10) → 0.1<i>x</i> = 2. Chalishtirish: (50 − 30) : (30 − 20) = 2 : 1.</p><p><strong>5</strong> — nisbatni teskari olgan javob (1 : 2).</p>"),
    q("Coffee costing $8 per kilogram is mixed with coffee costing $14 per kilogram in the ratio 2 to 1 by weight. What is the cost per kilogram of the mixture?", ["$10", "$11", "$11.50", "$12", "$13"], "$10",
      "<p><strong>$10.</strong> (2 × 8 + 1 × 14) ÷ 3 = 30 ÷ 3.</p><p><strong>$11</strong> — narxlarning oddiy oʻrtachasi.</p>"),
    q("In what ratio by weight must rice costing $5 per kilogram be mixed with rice costing $9 per kilogram to make a mixture costing $6 per kilogram?", RATIOS5, "3 : 1",
      "<p><strong>3 : 1.</strong> Chalishtirish: arzon : qimmat = (9 − 6) : (6 − 5) = 3 : 1.</p><p><strong>1 : 3</strong> — uzoqliklarni chalishtirmasdan qoʻygan javob; $6 arzonga yaqin, demak arzon koʻp.</p>"),
    q("A cleaning product is sold as a 60% concentrate. A worker dilutes 2 liters of it with 10 liters of water. What is the concentration of the diluted cleaner?", ["6%", "10%", "12%", "20%", "50%"], "10%",
      "<p><strong>10%.</strong> Modda 1.2 L, hajm 12 L.</p><p><strong>12%</strong> — 1.2 ni 10 L suvga boʻlgan javob; hajm 2 + 10 = 12.</p>"),
    q("A juice factory mixes 300 liters of juice that is 80% fruit with 200 liters that is 30% fruit. What percent of the mixture is fruit?", ["50%", "55%", "60%", "65%", "70%"], "60%",
      "<p><strong>60%.</strong> (240 + 60) ÷ 500 = 0.6.</p><p><strong>55%</strong> — foizlarning oddiy oʻrtachasi.</p>"),
    q("A jeweler has 40 grams of an alloy that is 75% gold. How many grams of pure gold must be added to make the alloy 80% gold?", ["2", "5", "8", "10", "12"], "10",
      "<p><strong>10.</strong> (30 + <i>g</i>) ÷ (40 + <i>g</i>) = 0.8 → 0.2<i>g</i> = 2. Tekshiruv: 40 ÷ 50 = 80% ✓.</p><p><strong>2</strong> — qoʻshilgan oltin umumiy vaznni ham oshirishini unutgan javob (32 − 30).</p>"),
    q("A farmer mixes 50 kilograms of feed costing $0.80 per kilogram with 30 kilograms costing $1.20 per kilogram. What is the cost per kilogram of the mixture?", ["$0.90", "$0.95", "$1.00", "$1.05", "$1.10"], "$0.95",
      "<p><strong>$0.95.</strong> (40 + 36) ÷ 80 = 0.95.</p><p><strong>$1.00</strong> — narxlarning oddiy oʻrtachasi.</p>"),
    q("A 30-liter solution is 40% alcohol. If 10 liters of the solution are removed and replaced with 10 liters of water, what percent of the new solution is alcohol?", ["13⅓%", "20%", "26⅔%", "30%", "33⅓%"], "26⅔%",
      "<p><strong>26⅔%.</strong> 20 L qoldi, unda 8 L spirt; suv qoʻshilgach 8 ÷ 30.</p><p><strong>30%</strong> — 40% dan 10 punkt ayirgan javob; olib tashlangan eritmada ham spirt bor edi.</p>"),
    q("How many liters of a 20% solution must be mixed with 10 liters of a 60% solution to produce a 30% solution?", ["10", "15", "20", "30", "40"], "30",
      "<p><strong>30.</strong> Chalishtirish: 20% : 60% = (60 − 30) : (30 − 20) = 3 : 1; 60% li 10 L, demak 20% li 30 L.</p><p><strong>10</strong> — teng miqdor; u 40% beradi.</p>"),
    q("Container A holds 10 liters of a 30% solution and container B holds 20 liters of a 60% solution. Half of the solution in A is poured into B. What is the concentration of the solution in B now?", ["45%", "50%", "54%", "55%", "60%"], "54%",
      "<p><strong>54%.</strong> B ga 5 L (1.5 L modda) qoʻshiladi: (12 + 1.5) ÷ 25 = 0.54.</p><p><strong>45%</strong> — 30% va 60% ning oddiy oʻrtachasi.</p>"),
    q("A 50-liter tank holds a 16% salt solution. How many liters of water must evaporate to make the solution 20% salt?", ["2", "4", "8", "10", "12.5"], "10",
      "<p><strong>10.</strong> Tuz 8 L; 20% da hajm 40 L; 50 − 40 = 10.</p><p><strong>4</strong> — foiz farqini (4 punkt) litr deb olgan javob.</p>"),
    q("A café blends 12 kilograms of coffee costing $15 per kilogram with 8 kilograms costing $20 per kilogram, and sells the blend at $21 per kilogram. What is the café's profit per kilogram of the blend?", ["$1.00", "$3.50", "$4.00", "$4.50", "$6.00"], "$4.00",
      "<p><strong>$4.00.</strong> Tannarx (180 + 160) ÷ 20 = 17; 21 − 17 = 4.</p><p><strong>$3.50</strong> — tannarxni oddiy oʻrtacha (17.50) bilan olgan javob.</p>"),
    q("A company has 2,400 liters of fuel that is 5% ethanol. How many liters of pure ethanol must be added to make the fuel 20% ethanol?", ["120", "360", "400", "450", "480"], "450",
      "<p><strong>450.</strong> (120 + <i>e</i>) ÷ (2,400 + <i>e</i>) = 0.2 → 0.8<i>e</i> = 360. Tekshiruv: 570 ÷ 2,850 = 20% ✓.</p><p><strong>360</strong> — qoʻshilgan etanol hajmni ham oshirishini unutgan javob (480 − 120).</p>"),
]

# =====================================================================
# GMAT-13 — rates, work, distance
# =====================================================================
Q13 = [
    q("A car travels 150 kilometers in 2.5 hours. What is its average speed in kilometers per hour?", ["37.5", "50", "60", "75", "375"], "60",
      "<p><strong>60.</strong> 150 ÷ 2.5.</p><p><strong>375</strong> — koʻpaytirilgan javob (150 × 2.5).</p>"),
    q("How many hours does it take to travel 210 kilometers at 70 kilometers per hour?", ["2", "2.5", "3", "3.5", "4"], "3",
      "<p><strong>3.</strong> 210 ÷ 70.</p><p><strong>3.5</strong> — 210 ni 60 ga boʻlgan javob.</p>"),
    q("How many kilometers does a car travel in 40 minutes at 90 kilometers per hour?", ["36", "45", "60", "90", "3,600"], "60",
      "<p><strong>60.</strong> 40 daqiqa = 2/3 soat; 90 × 2/3.</p><p><strong>3,600</strong> — daqiqani soatga oʻtkazmagan javob (90 × 40).</p>"),
    q("A printer prints 30 pages per minute. How many minutes does it take to print 1,200 pages?", ["4", "36", "40", "120", "400"], "40",
      "<p><strong>40.</strong> 1,200 ÷ 30.</p><p><strong>400</strong> — bitta nolni ortiqcha qoldirgan javob.</p>"),
    q("Machine A can complete a job in 4 hours and machine B can complete the same job in 6 hours. Working together at these rates, how many hours will they take?", ["2", "2.4", "2.5", "5", "10"], "2.4",
      "<p><strong>2.4.</strong> 1/4 + 1/6 = 5/12; 12/5 = 2.4.</p><p><strong>5</strong> — vaqtlarni oʻrtachalagan javob; u A ning yolgʻiz vaqtidan ham koʻp.</p>"),
    q("Three workers can paint a house in 8 days. Working at the same rate, how many days would four workers need?", ["4", "5", "6", "9", "12"], "6",
      "<p><strong>6.</strong> Ish = 3 × 8 = 24 ishchi-kun; 24 ÷ 4.</p><p><strong>9</strong> — toʻgʻri proporsiya deb, kunlarni oshirgan javob (ishchi koʻpaysa, kun kamayadi).</p>"),
    q("A driver travels 100 kilometers at 50 kilometers per hour and the next 100 kilometers at 100 kilometers per hour. What is the average speed for the whole trip, in kilometers per hour?", ["60", "66⅔", "70", "75", "80"], "66⅔",
      "<p><strong>66⅔.</strong> Vaqt 2 + 1 = 3 soat, masofa 200 km.</p><p><strong>75</strong> — tezliklarni oʻrtachalagan javob.</p>"),
    q("Two cyclists start from the same point and ride in opposite directions at 12 and 18 kilometers per hour. After how many hours are they 75 kilometers apart?", ["1.5", "2", "2.5", "4", "12.5"], "2.5",
      "<p><strong>2.5.</strong> Oraliq soatiga 30 km oshadi; 75 ÷ 30.</p><p><strong>12.5</strong> — tezliklarni ayirgan javob (75 ÷ 6); qarama-qarshi yoʻnalishda qoʻshiladi.</p>"),
    q("A truck leaves a depot at 60 kilometers per hour. One hour later a car leaves the same depot on the same road at 80 kilometers per hour. How many hours after the car leaves will it catch up with the truck?", ["0.75", "1", "3", "4", "6"], "3",
      "<p><strong>3.</strong> Bir soatda yuk mashinasi 60 km oldinda; oraliq soatiga 20 km qisqaradi.</p><p><strong>4</strong> — yuk mashinasining umumiy vaqti; savol avtomobil yoʻlga chiqqandan keyingi vaqtni soʻradi.</p>"),
    q("One pipe can fill a tank in 6 hours and a drain can empty the full tank in 9 hours. If both are open, how many hours will it take to fill the empty tank?", ["3.6", "7.5", "15", "18", "54"], "18",
      "<p><strong>18.</strong> 1/6 − 1/9 = 1/18.</p><p><strong>3.6</strong> — boʻshatuvchini ham toʻldiruvchi deb qoʻshgan javob.</p>"),
    q("A courier makes 12 deliveries per hour. How many hours does she need to make 90 deliveries?", ["6", "7", "7.5", "8", "10.8"], "7.5",
      "<p><strong>7.5.</strong> 90 ÷ 12.</p><p><strong>10.8</strong> — 90 × 12 ÷ 100 deb koʻpaytirgan javob; vaqt = ish ÷ unum.</p>"),
    q("One clerk enters 50 records per hour and a second clerk enters 30 records per hour. Working together, how many hours will they need to enter 640 records?", ["6", "8", "10", "12.8", "16"], "8",
      "<p><strong>8.</strong> Birgalikda soatiga 80; 640 ÷ 80.</p><p><strong>12.8</strong> — faqat birinchi xodim (640 ÷ 50).</p>"),
    q("A flight of 1,800 kilometers takes 2 hours 15 minutes. What is the plane's average speed, in kilometers per hour?", ["720", "750", "800", "837", "900"], "800",
      "<p><strong>800.</strong> 2 soat 15 daqiqa = 2.25 soat; 1,800 ÷ 2.25.</p><p><strong>837</strong> — vaqtni 2.15 soat deb yozgan javob; 15 daqiqa = 0.25 soat.</p>"),
    q("Working alone, Dilshod can process a month's invoices in 10 hours. With Feruza helping, the two of them take 6 hours. How many hours would Feruza take working alone?", ["4", "8", "12", "15", "16"], "15",
      "<p><strong>15.</strong> 1/6 − 1/10 = 1/15.</p><p><strong>4</strong> — vaqtlarni ayirgan javob (10 − 6).</p>"),
    q("A car drives uphill at 30 kilometers per hour and returns downhill along the same road at 60 kilometers per hour. What is its average speed for the round trip, in kilometers per hour?", ["40", "42", "45", "48", "50"], "40",
      "<p><strong>40.</strong> Masofa 60 km: yuqoriga 2 soat, pastga 1 soat; 120 ÷ 3.</p><p><strong>45</strong> — tezliklarning oddiy oʻrtachasi.</p>"),
    q("A runs 100 meters in 12 seconds and B runs 100 meters in 15 seconds. When A finishes a 100-meter race, how many meters behind is B?", ["3", "15", "20", "25", "80"], "20",
      "<p><strong>20.</strong> 12 soniyada B 100 × 12/15 = 80 m yuguradi.</p><p><strong>25</strong> — A ning 3 soniyadagi masofasi; savol B ning ortda qolishini soʻradi.</p>"),
    q("Machines A and B working together finish a job in 4 hours. Machine A alone takes 6 hours. How many hours would machine B take alone?", ["2", "5", "10", "12", "24"], "12",
      "<p><strong>12.</strong> 1/4 − 1/6 = 1/12.</p><p><strong>2</strong> — vaqtlarni ayirgan javob; birgalikdagi vaqtdan kam boʻlishi mumkin emas.</p>"),
    q("A boat travels 36 kilometers downstream in 2 hours and the same distance upstream in 3 hours. What is the speed of the current, in kilometers per hour?", ["2", "3", "5", "6", "15"], "3",
      "<p><strong>3.</strong> Pastga 18, yuqoriga 12 km/soat; oqim = (18 − 12) ÷ 2.</p><p><strong>15</strong> — qayiqning oʻz tezligi; <strong>6</strong> — ikkiga boʻlishni unutgan javob.</p>"),
    q("A factory has two packing lines. Line A packs 400 boxes per hour and line B packs 600 boxes per hour. Both lines start an order of 7,500 boxes at 8:00 a.m. At what time is the order finished?", ["2:30 p.m.", "3:00 p.m.", "3:30 p.m.", "4:00 p.m.", "4:30 p.m."], "3:30 p.m.",
      "<p><strong>3:30 p.m.</strong> Birgalikda soatiga 1,000; 7.5 soat; 8:00 + 7:30.</p><p><strong>3:00 p.m.</strong> — 7 soat deb yaxlitlagan javob.</p>"),
    q("Two delivery vans leave a depot at 9:00 a.m., one driving east at 50 kilometers per hour and the other driving west at 70 kilometers per hour. At what time will they be 300 kilometers apart?", ["11:00 a.m.", "11:30 a.m.", "12:00 p.m.", "12:30 p.m.", "3:00 p.m."], "11:30 a.m.",
      "<p><strong>11:30 a.m.</strong> Oraliq soatiga 120 km oshadi; 300 ÷ 120 = 2.5 soat.</p><p><strong>3:00 p.m.</strong> — faqat bitta furgonning tezligini olgan javob (300 ÷ 50).</p>"),
]

# =====================================================================
# GMAT-14 — profit, markup, discount
# =====================================================================
Q14 = [
    q("An item costs a store $40 and is sold for $52. What is the store's profit?", ["$8", "$12", "$13", "$40", "$92"], "$12",
      "<p><strong>$12.</strong> 52 − 40.</p><p><strong>$92</strong> — qoʻshilgan javob.</p>"),
    q("An item that costs $50 is sold for $65. What is the profit as a percent of cost?", ["15%", "23%", "30%", "65%", "130%"], "30%",
      "<p><strong>30%.</strong> 15 ÷ 50.</p><p><strong>23%</strong> — foydani sotish narxiga boʻlgan javob (15 ÷ 65).</p>"),
    q("An $80 item is discounted by 25%. What is the sale price?", ["$20", "$55", "$60", "$65", "$100"], "$60",
      "<p><strong>$60.</strong> 80 × 0.75.</p><p><strong>$20</strong> — chegirmaning oʻzi.</p>"),
    q("An item that costs $120 is marked up by 40%. What is the marked price?", ["$48", "$160", "$168", "$172", "$180"], "$168",
      "<p><strong>$168.</strong> 120 × 1.4.</p><p><strong>$48</strong> — ustamaning oʻzi.</p>"),
    q("An item was sold for $90 at a loss of 20% of its cost. What was the cost?", ["$72", "$108", "$110", "$112.50", "$118"], "$112.50",
      "<p><strong>$112.50.</strong> 0.8 × tannarx = 90; 90 ÷ 0.8.</p><p><strong>$108</strong> — 90 ga 20% qoʻshgan javob; zarar tannarxdan olingan.</p>"),
    q("Successive discounts of 30% and 20% are equivalent to a single discount of what percent?", ["44%", "46%", "48%", "50%", "56%"], "44%",
      "<p><strong>44%.</strong> 0.7 × 0.8 = 0.56 — narx 56% ga tushdi, chegirma 44%.</p><p><strong>50%</strong> — foizlarni qoʻshgan javob; <strong>56%</strong> — qolgan narx, chegirma emas.</p>"),
    q("An item sold for $150 earned a 25% profit on cost. What was the cost?", ["$112.50", "$115", "$120", "$125", "$187.50"], "$120",
      "<p><strong>$120.</strong> 150 ÷ 1.25.</p><p><strong>$112.50</strong> — sotish narxidan 25% ayirgan javob.</p>"),
    q("A company had revenue of $500,000 and costs of $420,000. What was its profit as a percent of revenue?", ["8%", "16%", "19%", "80%", "84%"], "16%",
      "<p><strong>16%.</strong> 80,000 ÷ 500,000.</p><p><strong>19%</strong> — foydani xarajatga boʻlgan javob (taxminan 80 ÷ 420).</p>"),
    q("A company's fixed costs are $9,000. Each unit sells for $30 and costs $12 to make. How many units must be sold to break even?", ["300", "500", "750", "900", "1,000"], "500",
      "<p><strong>500.</strong> 9,000 ÷ (30 − 12).</p><p><strong>300</strong> — butun narxga boʻlgan javob (9,000 ÷ 30).</p>"),
    q("An item is marked at 25% above its cost and is then sold at a 10% discount from the marked price. What is the profit as a percent of cost?", ["10%", "12.5%", "15%", "25%", "35%"], "12.5%",
      "<p><strong>12.5%.</strong> 1.25 × 0.9 = 1.125.</p><p><strong>15%</strong> — foizlarni qoʻshgan javob (25 − 10).</p>"),
    q("A bakery sells 400 loaves a day at $1.50 each. Each loaf costs $0.90 to make, and the bakery's other costs are $150 a day. What is the bakery's daily profit?", ["$90", "$150", "$240", "$390", "$600"], "$90",
      "<p><strong>$90.</strong> 400 × 0.60 = 240; 240 − 150.</p><p><strong>$240</strong> — boshqa xarajatlarni ayirmagan javob.</p>"),
    q("A store bought 50 lamps at $30 each. It sold 40 of them at $45 each and the rest at $25 each. What was its total profit?", ["$450", "$500", "$550", "$600", "$750"], "$550",
      "<p><strong>$550.</strong> Tushum 1,800 + 250 = 2,050; xarajat 1,500.</p><p><strong>$600</strong> — faqat 40 ta chiroqning foydasi; qolgan 10 tasi $5 dan zararga sotilgan.</p>"),
    q("A phone priced at $600 goes on sale at 15% off, and members receive a further 10% off the sale price. What does a member pay?", ["$450", "$459", "$465", "$500", "$510"], "$459",
      "<p><strong>$459.</strong> 600 × 0.85 = 510; 510 × 0.9 = 459.</p><p><strong>$450</strong> — 25% bitta chegirma deb hisoblagan javob.</p>"),
    q("A wholesaler sells a product to a retailer at a 20% profit, and the retailer sells it to a customer at a 25% profit. The customer pays $90. What did the product cost the wholesaler?", ["$50", "$54", "$58.50", "$60", "$63"], "$60",
      "<p><strong>$60.</strong> 90 ÷ 1.25 = 72; 72 ÷ 1.2 = 60.</p><p><strong>$58.50</strong> — 90 dan 35% ayirgan javob (foizlarni qoʻshib, sotish narxidan olgan).</p>"),
    q("The price of a $100 item is raised by 20%, and the new price is then discounted by 20%. What is the final price?", ["$80", "$96", "$100", "$104", "$120"], "$96",
      "<p><strong>$96.</strong> 100 × 1.2 × 0.8.</p><p><strong>$100</strong> — ±20% bir-birini yoʻqotadi deb oʻylagan javob.</p>"),
    q("Selling an item for $84 gives a 40% profit on cost. At what price should it be sold to give a 60% profit on cost?", ["$90", "$96", "$100.80", "$104", "$112"], "$96",
      "<p><strong>$96.</strong> Tannarx 84 ÷ 1.4 = 60; 60 × 1.6 = 96.</p><p><strong>$100.80</strong> — 84 ga 20% qoʻshgan javob; foiz tannarxdan olinadi.</p>"),
    q("A dealer marks goods 50% above cost and then offers a discount on the marked price, still making a 20% profit on cost. What is the discount?", ["10%", "20%", "25%", "30%", "33⅓%"], "20%",
      "<p><strong>20%.</strong> 1.5 × (1 − <i>d</i>) = 1.2 → 1 − <i>d</i> = 0.8.</p><p><strong>30%</strong> — foizlarni ayirgan javob (50 − 20).</p>"),
    q("A company's fixed costs are $20,000. Each unit costs $15 to produce and sells for $40. How many units must be sold to make a profit of $30,000?", ["800", "1,200", "1,250", "2,000", "3,333"], "2,000",
      "<p><strong>2,000.</strong> (20,000 + 30,000) ÷ 25.</p><p><strong>1,200</strong> — doimiy xarajatni qoplashni unutgan javob (30,000 ÷ 25).</p>"),
    q("A café buys coffee beans for $12 per kilogram. Each kilogram makes 80 cups, which sell for $1.50 each, and other costs are $0.60 per cup. What is the café's profit per kilogram of beans?", ["$48", "$60", "$72", "$108", "$120"], "$60",
      "<p><strong>$60.</strong> Tushum 120; xarajat 12 + 80 × 0.6 = 60; foyda 60.</p><p><strong>$72</strong> — donning narxini ayirmagan javob (120 − 48).</p>"),
    q("A retailer wants a 25% profit on cost after giving customers a 20% discount on the marked price. If an item costs $64, what should its marked price be?", ["$80", "$96", "$100", "$105", "$115.20"], "$100",
      "<p><strong>$100.</strong> Sotish narxi 64 × 1.25 = 80; 0.8 × belgilangan = 80.</p><p><strong>$80</strong> — sotish narxi; chegirma hali hisobga olinmagan.</p>"),
]

# =====================================================================
# GMAT-15 — simple and compound interest
# =====================================================================
Q15 = [
    q("What is the simple interest on $3,000 at 4% per year for 2 years?", ["$24", "$120", "$240", "$244.80", "$3,240"], "$240",
      "<p><strong>$240.</strong> 3,000 × 0.04 × 2.</p><p><strong>$244.80</strong> — murakkab foiz; <strong>$3,240</strong> — jami summa.</p>"),
    q("What does $1,000 grow to in 2 years at 10% interest compounded annually?", ["$1,020", "$1,100", "$1,200", "$1,210", "$1,331"], "$1,210",
      "<p><strong>$1,210.</strong> 1,000 × 1.1 × 1.1.</p><p><strong>$1,200</strong> — oddiy foiz; <strong>$1,331</strong> — uch yil.</p>"),
    q("A deposit of $4,000 earned $600 in simple interest over 3 years. What was the annual interest rate?", ["3%", "4.5%", "5%", "7.5%", "15%"], "5%",
      "<p><strong>5%.</strong> 600 ÷ (4,000 × 3).</p><p><strong>15%</strong> — uch yillik foizni yillik deb olgan javob.</p>"),
    q("What is the simple interest on $2,000 at 5% per year for 6 months?", ["$10", "$50", "$60", "$100", "$600"], "$50",
      "<p><strong>$50.</strong> 6 oy = 0.5 yil; 2,000 × 0.05 × 0.5.</p><p><strong>$600</strong> — 6 oyni 6 yil deb olgan javob.</p>"),
    q("How much interest does $5,000 earn in 2 years at 4% compounded annually?", ["$400", "$404", "$408", "$416", "$5,408"], "$408",
      "<p><strong>$408.</strong> 5,000 × 1.0816 = 5,408.</p><p><strong>$400</strong> — oddiy foiz; <strong>$5,408</strong> — jami summa.</p>"),
    q("What is the difference between the compound interest (compounded annually) and the simple interest on $10,000 at 6% per year for 2 years?", ["$6", "$36", "$60", "$360", "$1,236"], "$36",
      "<p><strong>$36.</strong> Farq = summa × stavka<sup>2</sup> = 10,000 × 0.0036.</p><p><strong>$360</strong> — vergulni adashtirgan javob.</p>"),
    q("What does $8,000 grow to in 1 year at 10% per year compounded semiannually?", ["$8,400", "$8,800", "$8,820", "$8,840", "$9,600"], "$8,820",
      "<p><strong>$8,820.</strong> Har yarim yil 5%: 8,000 × 1.05 × 1.05.</p><p><strong>$8,800</strong> — yillik kapitallashuv bilan hisoblangan javob.</p>"),
    q("How many years will it take $2,500 to earn $1,000 in simple interest at 8% per year?", ["2.5", "4", "5", "8", "12.5"], "5",
      "<p><strong>5.</strong> Yiliga 200; 1,000 ÷ 200.</p><p><strong>12.5</strong> — 1,000 ni 80 ga boʻlgan javob.</p>"),
    q("A sum of money doubles in 8 years at simple interest. What is the annual interest rate?", ["8%", "10%", "12.5%", "16%", "25%"], "12.5%",
      "<p><strong>12.5%.</strong> 8 yilda 100% foiz; 100 ÷ 8.</p><p><strong>8%</strong> — yillarni stavka deb olgan javob.</p>"),
    q("A deposit grows to $1,452 in 2 years at 10% compounded annually. What was the deposit?", ["$1,089", "$1,152", "$1,200", "$1,210", "$1,320"], "$1,200",
      "<p><strong>$1,200.</strong> 1,452 ÷ 1.21.</p><p><strong>$1,320</strong> — faqat bir yilga boʻlgan javob.</p>"),
    q("A bank loan of $20,000 charges 9% simple interest per year. What is the total amount repaid after 3 years?", ["$5,400", "$21,800", "$25,400", "$25,900.58", "$74,000"], "$25,400",
      "<p><strong>$25,400.</strong> Foiz 20,000 × 0.09 × 3 = 5,400; jami 25,400.</p><p><strong>$25,900.58</strong> — murakkab foiz; <strong>$5,400</strong> — faqat foiz.</p>"),
    q("A savings account pays 4% interest compounded annually. A client deposits $25,000. What is the balance after 2 years?", ["$26,000", "$27,000", "$27,040", "$28,000", "$29,000"], "$27,040",
      "<p><strong>$27,040.</strong> 25,000 × 1.04 = 26,000; × 1.04 = 27,040.</p><p><strong>$27,000</strong> — oddiy foiz.</p>"),
    q("Ozoda borrows $6,000 at 7% simple annual interest for 18 months. How much interest does she pay?", ["$126", "$420", "$630", "$756", "$1,260"], "$630",
      "<p><strong>$630.</strong> 18 oy = 1.5 yil; 6,000 × 0.07 × 1.5.</p><p><strong>$420</strong> — faqat bir yil.</p>"),
    q("An investment grew from $40,000 to $48,400 in two years with interest compounded annually at a fixed rate. What was the annual rate?", ["5%", "9.5%", "10%", "10.5%", "21%"], "10%",
      "<p><strong>10%.</strong> 48,400 ÷ 40,000 = 1.21 = 1.1 × 1.1.</p><p><strong>10.5%</strong> — 21% ni ikkiga boʻlgan javob; murakkab foizda ildiz olinadi.</p>"),
    q("How much interest does $1,000 earn in 3 years at 20% compounded annually?", ["$600", "$640", "$728", "$1,600", "$1,728"], "$728",
      "<p><strong>$728.</strong> 1,000 × 1.2<sup>3</sup> = 1,728; foiz 728.</p><p><strong>$600</strong> — oddiy foiz; <strong>$1,728</strong> — jami summa.</p>"),
    q("$10,000 is invested for 2 years at 10% per year. How much more does it earn if interest is compounded semiannually rather than annually?", ["$0", "$5.06", "$25.00", "$55.06", "$100.00"], "$55.06",
      "<p><strong>$55.06.</strong> Yarim yillik: 10,000 × 1.05<sup>4</sup> = 12,155.06; yillik: 12,100.</p><p><strong>$0</strong> — stavka bir xil boʻlgani uchun natija ham bir xil deb oʻylagan javob.</p>"),
    q("At what simple annual interest rate will $4,000 earn, in 5 years, the same interest that $5,000 earns in 3 years at 8% simple annual interest?", ["4.8%", "5%", "6%", "7.5%", "8%"], "6%",
      "<p><strong>6%.</strong> 5,000 × 0.08 × 3 = 1,200; 1,200 ÷ (4,000 × 5) = 0.06.</p><p><strong>4.8%</strong> — 8% ni 3/5 ga koʻpaytirib, summalar nisbatini unutgan javob.</p>"),
    q("A deposit earns 10% interest compounded annually. The interest earned in the second year alone is $1,320. What was the deposit?", ["$11,000", "$12,000", "$12,100", "$13,200", "$14,520"], "$12,000",
      "<p><strong>$12,000.</strong> Ikkinchi yil foizi = deposit × 1.1 × 0.1 = 0.11 × deposit.</p><p><strong>$13,200</strong> — 1,320 ni 0.1 ga boʻlgan javob; ikkinchi yil foizi oʻsgan summadan olinadi.</p>"),
    q("A company invests $200,000 in a bond paying 5% simple annual interest and $100,000 in a fund that returns 10% compounded annually. What is the total interest after 2 years?", ["$30,000", "$40,000", "$41,000", "$42,000", "$45,500"], "$41,000",
      "<p><strong>$41,000.</strong> Obligatsiya: 20,000; fond: 100,000 × 0.21 = 21,000.</p><p><strong>$40,000</strong> — fondni ham oddiy foiz bilan hisoblagan javob.</p>"),
    q("A family deposits $10,000 at 6% compounded annually. Using the rule of 72, approximately how many years will it take the deposit to double?", ["6", "10", "12", "16.7", "72"], "12",
      "<p><strong>12.</strong> 72 ÷ 6.</p><p><strong>16.7</strong> — oddiy foiz bilan hisoblangan javob (100 ÷ 6); murakkab foiz tezroq ikki baravar oshiradi.</p>"),
]

PRACTICES = [
    {
        "title": "GMAT-11 Practice: Averages and Weighted Averages",
        "description": "20 ta GMAT uslubidagi savol — yigʻindi orqali oʻrtacha, tortilgan oʻrtacha va oʻrtacha tezlik.",
        "tutorial": "GMAT-11:", "subject": "GMAT", "level": "medium", "questions": Q11,
    },
    {
        "title": "GMAT-12 Practice: Mixtures and Concentrations",
        "description": "20 ta GMAT uslubidagi savol — eritmalar, suyultirish, bugʻlatish va chalishtirish.",
        "tutorial": "GMAT-12:", "subject": "GMAT", "level": "medium", "questions": Q12,
    },
    {
        "title": "GMAT-13 Practice: Rates, Work and Distance",
        "description": "20 ta GMAT uslubidagi savol — tezlik, oʻrtacha tezlik, nisbiy harakat va birgalikdagi ish.",
        "tutorial": "GMAT-13:", "subject": "GMAT", "level": "medium", "questions": Q13,
    },
    {
        "title": "GMAT-14 Practice: Profit, Cost, Markup and Discount",
        "description": "20 ta GMAT uslubidagi savol — ustama, chegirma, foyda foizi va zararsizlik nuqtasi.",
        "tutorial": "GMAT-14:", "subject": "GMAT", "level": "medium", "questions": Q14,
    },
    {
        "title": "GMAT-15 Practice: Simple and Compound Interest",
        "description": "20 ta GMAT uslubidagi savol — oddiy va murakkab foiz, kapitallashuv davrlari, 72 qoidasi.",
        "tutorial": "GMAT-15:", "subject": "GMAT", "level": "medium", "questions": Q15,
    },
]
