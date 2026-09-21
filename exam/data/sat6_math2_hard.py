# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 6 · Math, Module 2 (UPPER)
#  22 questions · 35 minutes · taken by a pupil who scored 14 or more on math1.
#  Questions 18–22 are student-produced responses (grid-ins).

#
#  Load: python manage.py load_mock exam/data/sat6_math2_hard.py --expect-questions=22
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §2
# ──────────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'Digital SAT — PrimePoint Mock 6',
    'language': 'english',
    'exam_format': 'sat',
    'exam_number': 206,
    'is_published': True,
}

# Copied unchanged into all six files of mock 6.
MODULES = [
    {'code': 'rw1', 'kind': 'rw', 'stage': 1, 'order': 1, 'minutes': 32,
     'label': 'Reading and Writing — Module 1',
     'label_uz': 'Oʻqish va yozish', 'route_threshold': 18},
    {'code': 'rw2e', 'kind': 'rw', 'stage': 2, 'difficulty': 'easy', 'order': 1, 'minutes': 32,
     'label': 'Reading and Writing — Module 2',
     'label_uz': 'Oʻqish va yozish', 'break_minutes': 10},
    {'code': 'rw2h', 'kind': 'rw', 'stage': 2, 'difficulty': 'hard', 'order': 1, 'minutes': 32,
     'label': 'Reading and Writing — Module 2',
     'label_uz': 'Oʻqish va yozish', 'break_minutes': 10},
    {'code': 'math1', 'kind': 'math', 'stage': 1, 'order': 2, 'minutes': 35,
     'label': 'Math — Module 1', 'label_uz': 'Matematika',
     'route_threshold': 14, 'calculator': True, 'reference_sheet': True},
    {'code': 'math2e', 'kind': 'math', 'stage': 2, 'difficulty': 'easy', 'order': 2, 'minutes': 35,
     'label': 'Math — Module 2', 'label_uz': 'Matematika',
     'calculator': True, 'reference_sheet': True},
    {'code': 'math2h', 'kind': 'math', 'stage': 2, 'difficulty': 'hard', 'order': 2, 'minutes': 35,
     'label': 'Math — Module 2', 'label_uz': 'Matematika',
     'calculator': True, 'reference_sheet': True},
]

S = 'math2h'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>If 8(2<i>x</i> − 7) = 11<i>x</i> + 4, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['6', '12', '20', '60'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>12</strong>. Qavsni ochamiz: 16<i>x</i> '
                    '− 56 = 11<i>x</i> + 4. 11<i>x</i> ni ayirib, 56 ni qoʻshamiz: '
                    '5<i>x</i> = 60, demak <i>x</i> = 12. <strong>60</strong> — '
                    '5<i>x</i> ning qiymati, yaʼni oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 2, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '4<i>x</i><sup>2</sup> − <i>x</i>. Which expression is '
                      'equivalent to <i>f</i>(<i>x</i> + 1) − <i>f</i>(<i>x</i>)?</p>',
     'choices': [
         '4<i>x</i> + 3',
         '8<i>x</i> − 3',
         '8<i>x</i> + 1',
         '8<i>x</i> + 3',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>8<i>x</i> + 3</strong>. '
                    '<i>f</i>(<i>x</i>+1) = 4(<i>x</i>+1)<sup>2</sup> − (<i>x</i>+1) '
                    '= 4<i>x</i><sup>2</sup> + 8<i>x</i> + 4 − <i>x</i> − 1 = '
                    '4<i>x</i><sup>2</sup> + 7<i>x</i> + 3. Undan '
                    '4<i>x</i><sup>2</sup> − <i>x</i> ni ayiramiz: 8<i>x</i> + 3. '
                    '<strong>8<i>x</i> + 1</strong> — (<i>x</i>+1) ni ayirishda '
                    'faqat <i>x</i> ni hisobga olgan javob.'},

    {'section': S, 'number': 3, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>A price rises by 25% and the new price then falls by 36%. The '
                      'final price is what percent of the original price?</p>',
     'choices': ['80%', '89%', '100%', '111%'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>80%</strong>. Foiz har safar <em>joriy</em> '
                    'narxdan olinadi: 1.25 × 0.64 = 0.80, yaʼni 80%. '
                    '<strong>89%</strong> — foizlarni qoʻshib-ayirgan javob '
                    '(+25 − 36 = −11): foizlar qoʻshilmaydi, koʻpaytiriladi.'},

    {'section': S, 'number': 4, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>6<i>x</i> − 4<i>y</i> = 14<br>5<i>x</i> + 4<i>y</i> = 41</p>'
                      '<p>The system of equations above has a unique solution. What is the '
                      'value of <i>x</i>?</p>',
     'choices': ['4', '5', '7', '9'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Ikki tenglamani qoʻshsak '
                    '<i>y</i> qisqaradi: 11<i>x</i> = 55, demak <i>x</i> = 5. Qoʻshish '
                    'usuli aynan shunday holat uchun: bir xil koeffitsiyent qarama-qarshi '
                    'ishorada turibdi. <strong>4</strong> — <i>y</i> ning qiymati.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A right circular cone has a radius of 6 units and a height of 5 '
                      'units. What is its volume?</p>',
     'choices': ['30π', '60π', '180π', '900π'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>60π</strong>. Konus hajmi '
                    '⅓π<i>r</i><sup>2</sup><i>h</i> = ⅓ × π × 36 × 5 '
                    '= 60π. <strong>180π</strong> — ⅓ ni unutgan '
                    'javob: u silindrning hajmi.'},

    {'section': S, 'number': 6, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The equation <i>x</i><sup>2</sup> + <i>kx</i> + 49 = 0, where '
                      '<i>k</i> is a constant, has exactly one distinct real solution. '
                      'Which of the following is a possible value of <i>k</i>?</p>',
     'choices': ['−49', '−7', '14', '49'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>14</strong>. Bitta yechim boʻlishi uchun '
                    'diskriminant nolga teng: <i>k</i><sup>2</sup> − 4(1)(49) = 0, '
                    'yaʼni <i>k</i><sup>2</sup> = 196 va <i>k</i> = ±14. '
                    '<strong>−7</strong> — <i>k</i> ni ildizning oʻzi '
                    '(<i>x</i> = −7) bilan adashtirgan javob.'},

    {'section': S, 'number': 7, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>6<i>x</i> + 9<i>y</i> = 21<br>8<i>x</i> + 12<i>y</i> = '
                      '<i>c</i></p>'
                      '<p>In the system above, <i>c</i> is a constant. If the system has '
                      'infinitely many solutions, what is the value of <i>c</i>?</p>',
     'choices': ['21', '24', '28', '32'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>28</strong>. Cheksiz koʻp yechim boʻlishi uchun '
                    'ikkinchi tenglama birinchisining koʻpaytmasi boʻlishi kerak. '
                    '8 ÷ 6 = 4/3 va 12 ÷ 9 = 4/3 — koʻpaytuvchi 4/3, demak '
                    '<i>c</i> = 21 × 4/3 = 28. <strong>21</strong> — oʻng tomonni '
                    'oʻzgarishsiz qoldiradi, bu esa yechimsiz sistema beradi.'},

    {'section': S, 'number': 8, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>A cyclist rides 18 kilometres at an average speed of 18 '
                      'kilometres per hour and returns along the same route at an average '
                      'speed of 9 kilometres per hour. What is the average speed, in '
                      'kilometres per hour, for the whole ride?</p>',
     'choices': ['11', '12', '13.5', '15'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>12</strong>. Oʻrtacha tezlik — <em>jami '
                    'masofa</em> ÷ <em>jami vaqt</em>. Masofa 36 km; vaqt 18/18 + 18/9 = '
                    '1 + 2 = 3 soat; 36 ÷ 3 = 12. <strong>13.5</strong> — '
                    '(18 + 9) ÷ 2, eng keng tarqalgan tuzoq: sekin yoʻlda ikki barobar '
                    'koʻp vaqt ketadi.'},

    {'section': S, 'number': 9, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>What is the solution to the equation √(2<i>x</i> + 7) = '
                      '<i>x</i> − 4?</p>',
     'choices': ['1', '3', '9', '11'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Ikki tomonni kvadratga koʻtaramiz: '
                    '2<i>x</i> + 7 = <i>x</i><sup>2</sup> − 8<i>x</i> + 16, yaʼni '
                    '<i>x</i><sup>2</sup> − 10<i>x</i> + 9 = 0 va (<i>x</i> − 1)'
                    '(<i>x</i> − 9) = 0. <strong>1</strong> — begona ildiz: '
                    '<i>x</i> = 1 da oʻng tomon −3 chiqadi, kvadrat ildiz esa manfiy '
                    'boʻla olmaydi.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, a circle is given by the equation '
                      '<i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> + 12<i>x</i> − '
                      '4<i>y</i> = 60. What is the radius of the circle?</p>',
     'choices': ['8', '10', '40', '100'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>10</strong>. Toʻliq kvadratga keltiramiz: '
                    '<i>x</i><sup>2</sup> + 12<i>x</i> = (<i>x</i> + 6)<sup>2</sup> '
                    '− 36 va <i>y</i><sup>2</sup> − 4<i>y</i> = (<i>y</i> '
                    '− 2)<sup>2</sup> − 4. Demak (<i>x</i> + 6)<sup>2</sup> + '
                    '(<i>y</i> − 2)<sup>2</sup> = 60 + 36 + 4 = 100 va radius '
                    '√100 = 10. <strong>100</strong> — <i>r</i><sup>2</sup> '
                    'ning oʻzi.'},

    {'section': S, 'number': 11, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>A line in the <i>xy</i>-plane passes through the points '
                      '(−3, 14) and (3, −10). What is the <i>y</i>-coordinate of '
                      'the <i>y</i>-intercept of the line?</p>',
     'choices': ['−10', '2', '12', '14'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. Burchak koeffitsiyenti '
                    '(−10 − 14) ÷ (3 − (−3)) = −24 ÷ 6 = '
                    '−4. Endi (3, −10) ni <i>y</i> = −4<i>x</i> + <i>b</i> '
                    'ga qoʻyamiz: −10 = −12 + <i>b</i>, demak <i>b</i> = 2. '
                    '<strong>14</strong> — (−3, 14) nuqtaning <i>y</i> qiymati: '
                    'bu nuqta <i>y</i> oʻqida emas.'},

    {'section': S, 'number': 12, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>If <i>x</i> − 1/<i>x</i> = 4, what is the value of '
                      '<i>x</i><sup>2</sup> + 1/<i>x</i><sup>2</sup>?</p>',
     'choices': ['14', '16', '18', '20'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>18</strong>. Ikki tomonni kvadratga '
                    'koʻtaramiz: (<i>x</i> − 1/<i>x</i>)<sup>2</sup> = '
                    '<i>x</i><sup>2</sup> − 2 + 1/<i>x</i><sup>2</sup> = 16. '
                    'Oʻrtadagi −2 ni qoʻshamiz: <i>x</i><sup>2</sup> + '
                    '1/<i>x</i><sup>2</sup> = 18. <strong>14</strong> — 2 ni '
                    'qoʻshish oʻrniga ayirgan javob: ayirmada oʻrtadagi had manfiy, '
                    'shuning uchun uni qoʻshamiz.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>The mean of 15 numbers is 40. Five of the numbers, which total '
                      '150, are then removed. What is the mean of the remaining 10 '
                      'numbers?</p>',
     'choices': ['40', '42', '45', '48'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>45</strong>. Yigʻindilar bilan ishlaymiz: '
                    'avval 15 × 40 = 600, olib tashlanganlar 150, qolgani 600 − 150 '
                    '= 450. Endi 450 ÷ 10 = 45. Olib tashlanganlarning oʻrtachasi (30) '
                    'umumiy oʻrtachadan past boʻlgani uchun qolganlarniki koʻtariladi.'},

    {'section': S, 'number': 14, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>If 25<sup><i>x</i></sup> = 125<sup><i>x</i>−1</sup>, what is '
                      'the value of <i>x</i>?</p>',
     'choices': ['1', '2', '3', '5'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Ikki tomonni 5 asosiga keltiramiz: '
                    '25 = 5<sup>2</sup> va 125 = 5<sup>3</sup>, demak '
                    '5<sup>2<i>x</i></sup> = 5<sup>3(<i>x</i>−1)</sup>. Asoslar teng '
                    'boʻlgani uchun darajalar teng: 2<i>x</i> = 3<i>x</i> − 3, '
                    'bundan <i>x</i> = 3.'},

    {'section': S, 'number': 15, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>ABC</i>, angle <i>C</i> is a right angle and '
                      'tan <i>A</i> = 15/8. What is the value of cos <i>A</i>?</p>',
     'choices': ['8/17', '8/15', '15/17', '15/8'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>8/17</strong>. tan <i>A</i> = qarshi ÷ yondosh '
                    '= 15/8, demak qarshi katet 15, yondosh katet 8. Pifagor boʻyicha '
                    'gipotenuza √(225 + 64) = √289 = 17, va cos <i>A</i> = '
                    'yondosh ÷ gipotenuza = 8/17. <strong>15/17</strong> — bu '
                    'sin <i>A</i>.'},

    {'section': S, 'number': 16, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>a</i>(<i>x</i> − 2)<sup>2</sup> − 3, where <i>a</i> is '
                      'a constant. If <i>f</i>(5) = 42, what is the value of '
                      '<i>a</i>?</p>',
     'choices': ['3', '5', '9', '15'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. <i>x</i> = 5 ni qoʻyamiz: '
                    '<i>a</i>(5 − 2)<sup>2</sup> − 3 = 9<i>a</i> − 3 = 42, '
                    'demak 9<i>a</i> = 45 va <i>a</i> = 5. <strong>15</strong> — '
                    '(5 − 2) ni kvadratga koʻtarmay, 3<i>a</i> − 3 = 42 deb '
                    'hisoblagan javob.'},

    {'section': S, 'number': 17, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>The solution set of the inequality 21 − 4<i>x</i> ≥ '
                      '3<i>x</i> − 14 is <i>x</i> ≤ <i>k</i>, where <i>k</i> is a '
                      'constant. What is the value of <i>k</i>?</p>',
     'choices': ['−5', '3', '5', '7'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. 4<i>x</i> ni oʻngga, 14 ni chapga '
                    'oʻtkazamiz: 35 ≥ 7<i>x</i>, demak <i>x</i> ≤ 5 va '
                    '<i>k</i> = 5. Diqqat: tengsizlikni <em>musbat</em> 7 ga boʻlganimiz '
                    'uchun ishora oʻzgarmadi.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 8(<i>x</i> − 3) = 5(<i>x</i> + 3), what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['13'],
     'explanation': 'Toʻgʻri javob <strong>13</strong>. Ikki qavsni ochamiz: 8<i>x</i> '
                    '− 24 = 5<i>x</i> + 15. 5<i>x</i> ni ayirib, 24 ni qoʻshamiz: '
                    '3<i>x</i> = 39, demak <i>x</i> = 13. Tekshirish: 8(10) = 80 va '
                    '5(16) = 80.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>A 25-litre mixture is 16% salt by volume. How many litres of pure '
                      'salt must be added so that the mixture becomes 30% salt by '
                      'volume?</p>' + GRID_NOTE,
     'accepted': ['5'],
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Boshida tuz 25 × 0.16 = 4 litr. Sof '
                    'tuz qoʻshilganda <em>ham</em> tuz, <em>ham</em> umumiy hajm oshadi: '
                    '(4 + <i>a</i>) ÷ (25 + <i>a</i>) = 0.30. Bundan 4 + <i>a</i> = 7.5 + '
                    '0.3<i>a</i>, yaʼni 0.7<i>a</i> = 3.5 va <i>a</i> = 5. Eng keng '
                    'tarqalgan xato — maxrajni 25 deb qoldirish.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>2</sup> − 17<i>x</i> + 72 = 0 and '
                      '<i>x</i> ≠ 8, what is the value of <i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['9'],
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Koʻpaytmasi 72, yigʻindisi 17 '
                    'boʻlgan ikki son — 8 va 9, demak (<i>x</i> − 8)(<i>x</i> '
                    '− 9) = 0. Shart <i>x</i> ≠ 8 birinchi ildizni chiqarib '
                    'tashlaydi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If (4<i>x</i> + 9) ÷ 5 = 9, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['9'],
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Avval ikki tomonni 5 ga '
                    'koʻpaytiramiz: 4<i>x</i> + 9 = 45, keyin 9 ni ayirib 4 ga boʻlamiz: '
                    '<i>x</i> = 9. Kasr koʻrinishidagi tenglamada birinchi qadam har doim '
                    'maxrajdan qutulish.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 8<sup>2<i>x</i></sup> = 4,096, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['2'],
     'explanation': 'Toʻgʻri javob <strong>2</strong>. 8<sup>4</sup> = 4,096, demak '
                    '2<i>x</i> = 4 va <i>x</i> = 2. Eng keng tarqalgan xato — 4 '
                    'yozish: u 2<i>x</i> ning qiymati, <i>x</i> niki emas.'},
]
