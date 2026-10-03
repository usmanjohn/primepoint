# -*- coding: utf-8 -*-
"""GMAT Focus Edition — PrimePoint Mock 1 — Quantitative Reasoning (21 questions, 45 min).

Rules: exam/data/STYLE_GUIDE_GMAT_MOCK.md. Problem Solving only, five choices, no
calculator. Blueprint: Number Properties 4 · Percents, Ratios and Rates 5 · Algebra 4 ·
Word Problems 4 · Statistics and Counting 4. Difficulty climbs across the section.
Answer gate: verify_gmat_mock1_quant.py (scratchpad) recomputes every key by a second route.

    python manage.py load_mock exam/data/gmat1_quant.py --expect-questions=21
"""

EXAM_META = {
    'title': 'GMAT Focus Edition — PrimePoint Mock 1',
    'language': 'english',
    'exam_format': 'gmat',
    'exam_number': 301,
    'is_published': True,
}

MODULES = [
    {'code': 'quant', 'kind': 'quant', 'stage': 1, 'order': 1, 'minutes': 45,
     'label': 'Quantitative Reasoning', 'label_uz': 'Miqdoriy mulohaza'},
    {'code': 'verbal', 'kind': 'verbal', 'stage': 1, 'order': 2, 'minutes': 45,
     'label': 'Verbal Reasoning', 'label_uz': 'Ogʻzaki mulohaza'},
    {'code': 'di', 'kind': 'di', 'stage': 1, 'order': 3, 'minutes': 45, 'calculator': True,
     'label': 'Data Insights', 'label_uz': 'Maʼlumotlar tahlili'},
]

NP, PRR, ALG, WP, SC = ('Number Properties', 'Percents, Ratios and Rates', 'Algebra',
                        'Word Problems', 'Statistics and Counting')


def q(number, skill, difficulty, text, choices, correct, explanation):
    return {'section': 'quant', 'number': number, 'skill': skill, 'difficulty': difficulty,
            'question_text': text, 'choices': choices, 'correct': correct,
            'explanation': explanation}


QUESTIONS = [
    q(1, PRR, 'easy',
      '<p>A jacket priced at $80 is discounted by 15 percent, and an 8 percent sales tax is then '
      'charged on the discounted price. What is the final price of the jacket?</p>',
      ['$72.80', '$73.44', '$74.00', '$74.40', '$75.44'], 2,
      '<p>Chegirma: 80 × 0.85 = 68. Soliq <b>chegirmadan keyingi</b> narxga: 68 × 1.08 = 73.44. '
      'Javob — <strong>$73.44</strong>. Tuzoq: foizlarni qoʻshib (−15% + 8% = −7%) 80 × 0.93 = '
      '$74.40 hisoblash — ketma-ket foizlar qoʻshilmaydi, koʻpaytiriladi.</p>'),

    q(2, NP, 'easy',
      '<p>What is the remainder when 7<sup>23</sup> is divided by 5?</p>',
      ['0', '1', '2', '3', '4'], 4,
      '<p>5 ga boʻlgandagi qoldiq faqat oxirgi raqamga bogʻliq. 7 ning darajalari oxirgi raqami: '
      '7, 9, 3, 1 — har 4 qadamda takrorlanadi. 23 = 4 × 5 + 3, demak oxirgi raqam uchinchi: 3. '
      '3 ni 5 ga boʻlsak qoldiq <strong>3</strong>.</p>'),

    q(3, ALG, 'easy',
      '<p>If 3x − 7 = 2x + 5, what is the value of x<sup>2</sup> − 10x?</p>',
      ['6', '12', '18', '20', '24'], 5,
      '<p>3x − 2x = 5 + 7, demak x = 12. Keyin 12<sup>2</sup> − 10 × 12 = 144 − 120 = '
      '<strong>24</strong>.</p>'),

    q(4, PRR, 'easy',
      '<p>In a training group, the ratio of men to women is 4 to 5. If 6 more men join the group '
      'and no one leaves, the ratio of men to women becomes 1 to 1. How many women are in the group?</p>',
      ['24', '25', '30', '36', '45'], 3,
      '<p>Erkaklar 4k, ayollar 5k. 4k + 6 = 5k, demak k = 6 va ayollar 5 × 6 = '
      '<strong>30</strong>. Tuzoq: 24 — erkaklar soni.</p>'),

    q(5, WP, 'easy',
      '<p>Working alone, Aziz can paint a fence in 6 hours and Lola can paint the same fence in '
      '3 hours. Working together at these rates, how many hours will they take to paint the fence?</p>',
      ['1.5', '2', '2.25', '2.5', '4.5'], 2,
      '<p>Bir soatda: 1/6 + 1/3 = 1/2 qism. Butun devor uchun <strong>2</strong> soat. '
      'Tuzoq: 4.5 — vaqtlarning oʻrtachasi; birga ishlaganda vaqt eng tez ishchinikidan ham kam boʻladi.</p>'),

    q(6, SC, 'easy',
      '<p>The average (arithmetic mean) of five numbers is 18. When one of the numbers is removed, '
      'the average of the remaining four numbers is 16. What number was removed?</p>',
      ['14', '16', '18', '22', '26'], 5,
      '<p>Beshta sonning yigʻindisi 5 × 18 = 90, qolgan toʻrttasiniki 4 × 16 = 64. '
      'Olib tashlangan son 90 − 64 = <strong>26</strong>.</p>'),

    q(7, PRR, 'medium',
      '<p>A company\'s revenue rose by 20 percent in 2024 and then fell by 20 percent in 2025. '
      'Compared with its revenue in 2023, the company\'s revenue in 2025 was</p>',
      ['4 percent lower', '2 percent lower', 'the same', '2 percent higher', '4 percent higher'], 1,
      '<p>1.2 × 0.8 = 0.96 — 2023-yildagidan <strong>4 foiz past</strong>. +20% va −20% bir-birini '
      'yoʻqotmaydi: ikkinchi foiz kattaroq asosdan olinadi.</p>'),

    q(8, NP, 'medium',
      '<p>How many positive integers less than 100 are divisible by 3 or by 5, or by both?</p>',
      ['40', '43', '46', '49', '52'], 3,
      '<p>1–99 orasida: 3 ga boʻlinadiganlar 33 ta, 5 ga — 19 ta, ikkalasiga (15 ga) — 6 ta. '
      'Ikki marta sanalganlarni ayiramiz: 33 + 19 − 6 = <strong>46</strong>. Tuzoq: 52 — '
      '15 ga boʻlinadiganlarni ayirmaslik.</p>'),

    q(9, ALG, 'medium',
      '<p>If x<sup>2</sup> − 2x − 15 = 0 and x &lt; 0, what is the value of x<sup>3</sup> + x?</p>',
      ['−30', '−24', '−6', '30', '120'], 1,
      '<p>x<sup>2</sup> − 2x − 15 = (x − 5)(x + 3) = 0, ildizlar 5 va −3; shartga koʻra x = −3. '
      '(−3)<sup>3</sup> + (−3) = −27 − 3 = <strong>−30</strong>.</p>'),

    q(10, WP, 'medium',
      '<p>A driver travels 120 kilometers from one city to another at an average speed of '
      '60 kilometers per hour and returns along the same road at an average speed of '
      '40 kilometers per hour. What is the driver\'s average speed, in kilometers per hour, '
      'for the whole round trip?</p>',
      ['45', '48', '50', '52', '55'], 2,
      '<p>Borish 120 ÷ 60 = 2 soat, qaytish 120 ÷ 40 = 3 soat. Jami 240 km ÷ 5 soat = '
      '<strong>48</strong>. Tuzoq: 50 — tezliklarning oddiy oʻrtachasi; sekin qismda koʻproq vaqt '
      'oʻtgani uchun oʻrtacha tezlik pastroq.</p>'),

    q(11, PRR, 'medium',
      '<p>A 30-liter solution is 20 percent acid. How many liters of pure acid must be added to '
      'make a solution that is 40 percent acid?</p>',
      ['6', '7.5', '8', '9', '10'], 5,
      '<p>Kislota 30 × 0.2 = 6 litr. a litr qoʻshilsa: (6 + a) / (30 + a) = 0.4 → 6 + a = 12 + 0.4a → '
      '0.6a = 6 → a = <strong>10</strong>. Tekshiruv: 16 / 40 = 40%.</p>'),

    q(12, SC, 'medium',
      '<p>A committee of 3 people is to be chosen from 5 managers and 4 analysts. How many '
      'different committees include at least one analyst?</p>',
      ['60', '64', '70', '74', '80'], 4,
      '<p>Barcha qoʻmitalar C(9.3) = 84; faqat menejerlardan iborat — C(5.3) = 10. '
      'Kamida bitta tahlilchi: 84 − 10 = <strong>74</strong>. «Kamida bitta» — koʻpincha '
      '«hammasi» minus «birortasi ham yoʻq».</p>'),

    q(13, ALG, 'medium',
      '<p>How many integers n satisfy the inequality |2n − 3| &lt; 9?</p>',
      ['8', '9', '10', '11', '12'], 1,
      '<p>−9 &lt; 2n − 3 &lt; 9 → −6 &lt; 2n &lt; 12 → −3 &lt; n &lt; 6. Butun sonlar: '
      '−2, −1, 0, 1, 2, 3, 4, 5 — <strong>8</strong> ta. Tuzoq: chegaralarni (−3 va 6) qoʻshib sanash.</p>'),

    q(14, NP, 'medium',
      '<p>If n is a positive integer and n<sup>2</sup> is divisible by 72, what is the largest '
      'positive integer that must divide n?</p>',
      ['6', '12', '18', '24', '36'], 2,
      '<p>72 = 2<sup>3</sup> × 3<sup>2</sup>. n<sup>2</sup> da 2 ning darajasi juft, demak u kamida '
      '4 — n da kamida 2<sup>2</sup>. 3<sup>2</sup> uchun n da kamida 3. Demak n doim '
      '4 × 3 = <strong>12</strong> ga boʻlinadi (n = 12 da n<sup>2</sup> = 144 = 72 × 2). '
      'Tuzoq: 6 — 2<sup>3</sup> uchun n da 2<sup>2</sup> kerakligini unutish.</p>'),

    q(15, PRR, 'medium',
      '<p>A shop buys 200 umbrellas at $15 each. It sells 75 percent of them at $24 each and the '
      'rest at $12 each. The shop\'s profit is what percent of its total cost?</p>',
      ['25%', '30%', '35%', '40%', '45%'], 4,
      '<p>Xarajat 200 × 15 = 3,000. Tushum: 150 × 24 + 50 × 12 = 3,600 + 600 = 4,200. '
      'Foyda 1,200, bu xarajatning 1,200 ÷ 3,000 = <strong>40%</strong>. Tuzoq: foydani tushumga '
      'boʻlish — savol xarajatga nisbatan soʻraydi.</p>'),

    q(16, SC, 'hard',
      '<p>The list 3, 7, 7, 10, x has an average (arithmetic mean) equal to its median. '
      'What is the value of x?</p>',
      ['3', '5', '6', '7', '8'], 5,
      '<p>x qayerda turmasin, beshta sonning oʻrtasi (mediana) 7 boʻlib qoladi: x ≤ 7 boʻlsa ham, '
      '7 ≤ x boʻlsa ham tartiblangan roʻyxatning uchinchi soni 7. Demak oʻrtacha ham 7: '
      '(27 + x) / 5 = 7 → x = <strong>8</strong>.</p>'),

    q(17, WP, 'hard',
      '<p>Pipe A alone can fill an empty tank in 12 hours. Pipe B alone can empty the full tank in '
      '18 hours. If both pipes are opened at the same time when the tank is empty, how many hours '
      'will it take to fill the tank?</p>',
      ['24', '30', '32', '36', '42'], 4,
      '<p>Bir soatda: +1/12 − 1/18 = 3/36 − 2/36 = 1/36. Toʻldirish <strong>36</strong> soat. '
      'Tuzoq: 30 — vaqtlarni qoʻshib yuborish (12 + 18).</p>'),

    q(18, ALG, 'hard',
      '<p>If f(x) = 2x + 3 and g(x) = x<sup>2</sup> − 1, and f(g(a)) = 19 for some positive '
      'number a, what is the value of a?</p>',
      ['2', '3', '4', '5', '9'], 2,
      '<p>f(g(a)) = 2(a<sup>2</sup> − 1) + 3 = 2a<sup>2</sup> + 1 = 19 → a<sup>2</sup> = 9 → '
      'a = <strong>3</strong> (musbat). Tuzoq: 9 — a<sup>2</sup> ni a deb olish.</p>'),

    q(19, SC, 'hard',
      '<p>Two fair six-sided dice are rolled. What is the probability that the product of the two '
      'numbers rolled is even?</p>',
      ['1/4', '1/2', '2/3', '3/4', '5/6'], 4,
      '<p>Koʻpaytma toq boʻlishi uchun ikkala son ham toq boʻlishi kerak: (3/6) × (3/6) = 1/4. '
      'Juft koʻpaytma: 1 − 1/4 = <strong>3/4</strong>.</p>'),

    q(20, NP, 'hard',
      '<p>What is the units digit of 3<sup>47</sup> + 7<sup>29</sup>?</p>',
      ['0', '2', '4', '6', '8'], 3,
      '<p>3 ning darajalari oxiri: 3, 9, 7, 1; 47 = 4 × 11 + 3 → 7. 7 ning darajalari: 7, 9, 3, 1; '
      '29 = 4 × 7 + 1 → 7. 7 + 7 = 14, oxirgi raqam <strong>4</strong>.</p>'),

    q(21, WP, 'hard',
      '<p>An investment grows by 10 percent each year, with the growth added at the end of each year. '
      'After how many full years will the value of the investment first be more than double its '
      'initial value?</p>',
      ['6', '7', '8', '9', '10'], 3,
      '<p>1.1<sup>7</sup> ≈ 1.949 (hali ikki barobar emas), 1.1<sup>8</sup> ≈ 2.144 — birinchi marta '
      'ikki barobardan oshadi: <strong>8</strong> yil. Tuzoq: 10 — oddiy foiz (10% × 10 yil); '
      'murakkab foizda oʻsish tezroq.</p>'),
]
