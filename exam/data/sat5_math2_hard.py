# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 5 · Math, Module 2 (UPPER)
#  22 questions · 35 minutes · taken by a pupil who scored 14 or more on math1.
#  Questions 18–22 are student-produced responses (grid-ins).

#
#  Load: python manage.py load_mock exam/data/sat5_math2_hard.py --expect-questions=22
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §2
# ──────────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'Digital SAT — PrimePoint Mock 5',
    'language': 'english',
    'exam_format': 'sat',
    'exam_number': 205,
    'is_published': True,
}

# Copied unchanged into all six files of mock 5.
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
     'question_text': '<p>If 7(2<i>x</i> − 3) = 9<i>x</i> + 19, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['4', '8', '12', '40'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Qavsni ochamiz: 14<i>x</i> − 21 '
                    '= 9<i>x</i> + 19. 9<i>x</i> ni ayirib, 21 ni qoʻshamiz: 5<i>x</i> = '
                    '40, demak <i>x</i> = 8. <strong>40</strong> — 5<i>x</i> ning '
                    'qiymati, yaʼni oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 2, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> + 5<i>x</i>. Which expression is equivalent to '
                      '<i>f</i>(<i>x</i> + 2) − <i>f</i>(<i>x</i>)?</p>',
     'choices': [
         '2<i>x</i> + 14',
         '4<i>x</i> + 4',
         '4<i>x</i> + 10',
         '4<i>x</i> + 14',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>4<i>x</i> + 14</strong>. '
                    '<i>f</i>(<i>x</i>+2) = (<i>x</i>+2)<sup>2</sup> + 5(<i>x</i>+2) = '
                    '<i>x</i><sup>2</sup> + 4<i>x</i> + 4 + 5<i>x</i> + 10 = '
                    '<i>x</i><sup>2</sup> + 9<i>x</i> + 14. Undan '
                    '<i>x</i><sup>2</sup> + 5<i>x</i> ni ayiramiz: 4<i>x</i> + 14. '
                    '<strong>4<i>x</i> + 4</strong> — 5(<i>x</i>+2) ni ochishda '
                    '10 ni tushirib qoldirgan javob.'},

    {'section': S, 'number': 3, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>The price of an item falls by 30% and the reduced price then '
                      'rises by 30%. The final price is what percent of the original '
                      'price?</p>',
     'choices': ['85%', '91%', '100%', '109%'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>91%</strong>. Foiz har safar <em>joriy</em> '
                    'narxdan olinadi: 0.70 × 1.30 = 0.91, yaʼni 91%. '
                    '<strong>100%</strong> eng koʻp tanlanadigan javob — '
                    '"−30% va +30% bir-birini yoʻqotadi" degan tuygʻu; aslida '
                    'ikkinchi 30% kichikroq sondan olinadi.'},

    {'section': S, 'number': 4, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>4<i>x</i> − 5<i>y</i> = 5<br>3<i>x</i> + 5<i>y</i> = 30</p>'
                      '<p>The system of equations above has a unique solution. What is the '
                      'value of <i>x</i>?</p>',
     'choices': ['3', '5', '7', '9'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Ikki tenglamani qoʻshsak '
                    '<i>y</i> qisqaradi: 7<i>x</i> = 35, demak <i>x</i> = 5. Qoʻshish '
                    'usuli aynan shunday holat uchun: bir xil koeffitsiyent '
                    'qarama-qarshi ishorada turibdi. <strong>3</strong> — <i>y</i> '
                    'ning qiymati.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A sphere has a radius of 6 units. What is its volume?</p>',
     'choices': ['72π', '144π', '288π', '864π'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>288π</strong>. Shar hajmi '
                    '⁴⁄₃π<i>r</i><sup>3</sup> = '
                    '⁴⁄₃ × π × 216 = 288π. '
                    '<strong>864π</strong> — ⁴⁄₃ ni unutgan '
                    'javob (π<i>r</i><sup>3</sup> ning 4 barobari emas, oʻzi).'},

    {'section': S, 'number': 6, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The equation <i>x</i><sup>2</sup> + <i>kx</i> + 81 = 0, where '
                      '<i>k</i> is a constant, has exactly one distinct real solution. '
                      'Which of the following is a possible value of <i>k</i>?</p>',
     'choices': ['−81', '−9', '18', '81'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>18</strong>. Bitta yechim boʻlishi uchun '
                    'diskriminant nolga teng: <i>k</i><sup>2</sup> − 4(1)(81) = 0, '
                    'yaʼni <i>k</i><sup>2</sup> = 324 va <i>k</i> = ±18. '
                    '<strong>−9</strong> — <i>k</i> ni ildizning oʻzi '
                    '(<i>x</i> = −9) bilan adashtirgan javob.'},

    {'section': S, 'number': 7, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>5<i>x</i> − 2<i>y</i> = 9<br>15<i>x</i> − 6<i>y</i> = '
                      '<i>c</i></p>'
                      '<p>In the system above, <i>c</i> is a constant. If the system has '
                      'infinitely many solutions, what is the value of <i>c</i>?</p>',
     'choices': ['18', '27', '36', '45'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>27</strong>. Cheksiz koʻp yechim boʻlishi uchun '
                    'ikkinchi tenglama birinchisining aynan koʻpaytmasi boʻlishi kerak. '
                    'Chap tomon 3 barobar, demak oʻng tomon ham 3 barobar: <i>c</i> = '
                    '27. <strong>18</strong> — koʻpaytuvchini 2 deb olgan javob.'},

    {'section': S, 'number': 8, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>A train covers 90 kilometres at an average speed of 45 kilometres '
                      'per hour and a further 90 kilometres at an average speed of 90 '
                      'kilometres per hour. What is its average speed, in kilometres per '
                      'hour, for the whole journey?</p>',
     'choices': ['55', '60', '67.5', '70'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>60</strong>. Oʻrtacha tezlik — <em>jami '
                    'masofa</em> ÷ <em>jami vaqt</em>, tezliklarning oʻrtachasi emas. '
                    'Masofa 180 km; vaqt 90/45 + 90/90 = 2 + 1 = 3 soat; 180 ÷ 3 = 60. '
                    '<strong>67.5</strong> — (45 + 90) ÷ 2, eng keng tarqalgan '
                    'tuzoq.'},

    {'section': S, 'number': 9, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>What is the solution to the equation √(5<i>x</i> + 6) = '
                      '<i>x</i>?</p>',
     'choices': ['−1', '1', '6', '11'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Ikki tomonni kvadratga koʻtaramiz: '
                    '5<i>x</i> + 6 = <i>x</i><sup>2</sup>, yaʼni <i>x</i><sup>2</sup> '
                    '− 5<i>x</i> − 6 = 0 va (<i>x</i> − 6)(<i>x</i> + 1) = '
                    '0. <strong>−1</strong> — begona ildiz: kvadrat ildiz manfiy '
                    'son bera olmaydi, shuning uchun uni asl tenglamaga qoʻyib '
                    'tekshirish shart.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, a circle is given by the equation '
                      '<i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> − 4<i>x</i> + '
                      '10<i>y</i> = 20. What is the radius of the circle?</p>',
     'choices': ['5', '7', '20', '49'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. Toʻliq kvadratga keltiramiz: '
                    '<i>x</i><sup>2</sup> − 4<i>x</i> = (<i>x</i> − 2)'
                    '<sup>2</sup> − 4 va <i>y</i><sup>2</sup> + 10<i>y</i> = '
                    '(<i>y</i> + 5)<sup>2</sup> − 25. Demak (<i>x</i> − 2)'
                    '<sup>2</sup> + (<i>y</i> + 5)<sup>2</sup> = 20 + 4 + 25 = 49 va '
                    'radius √49 = 7. <strong>49</strong> — '
                    '<i>r</i><sup>2</sup> ning oʻzi.'},

    {'section': S, 'number': 11, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>A line in the <i>xy</i>-plane passes through the points '
                      '(−4, 13) and (2, −5). What is the <i>y</i>-coordinate of '
                      'the <i>y</i>-intercept of the line?</p>',
     'choices': ['−5', '1', '5', '13'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>1</strong>. Burchak koeffitsiyenti '
                    '(−5 − 13) ÷ (2 − (−4)) = −18 ÷ 6 = '
                    '−3. Endi (2, −5) ni <i>y</i> = −3<i>x</i> + <i>b</i> '
                    'ga qoʻyamiz: −5 = −6 + <i>b</i>, demak <i>b</i> = 1. '
                    '<strong>13</strong> — (−4, 13) nuqtaning <i>y</i> qiymati: '
                    'bu nuqta <i>y</i> oʻqida emas.'},

    {'section': S, 'number': 12, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>If <i>x</i> + 1/<i>x</i> = 3, what is the value of '
                      '<i>x</i><sup>3</sup> + 1/<i>x</i><sup>3</sup>?</p>',
     'choices': ['12', '18', '21', '27'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>18</strong>. Kubga koʻtaramiz: (<i>x</i> + '
                    '1/<i>x</i>)<sup>3</sup> = <i>x</i><sup>3</sup> + '
                    '1/<i>x</i><sup>3</sup> + 3(<i>x</i> + 1/<i>x</i>) = 27. Demak '
                    '<i>x</i><sup>3</sup> + 1/<i>x</i><sup>3</sup> = 27 − 3 × 3 = '
                    '18. <strong>27</strong> — oʻrtadagi 3(<i>x</i> + 1/<i>x</i>) '
                    'hadini unutgan javob.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>The mean of 12 numbers is 25. Three of the numbers, which total '
                      '30, are then removed. What is the mean of the remaining 9 '
                      'numbers?</p>',
     'choices': ['27', '28', '30', '32'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>30</strong>. Yigʻindilar bilan ishlaymiz: '
                    'avval 12 × 25 = 300, olib tashlanganlar 30, qolgani 300 − 30 = '
                    '270. Endi 270 ÷ 9 = 30. Olib tashlangan sonlarning oʻrtachasi (10) '
                    'umumiy oʻrtachadan past boʻlgani uchun qolganlarning oʻrtachasi '
                    'koʻtariladi.'},

    {'section': S, 'number': 14, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>If 16<sup><i>x</i></sup> = 8<sup><i>x</i>+1</sup>, what is the '
                      'value of <i>x</i>?</p>',
     'choices': ['1', '2', '3', '5'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Ikki tomonni 2 asosiga keltiramiz: '
                    '16 = 2<sup>4</sup> va 8 = 2<sup>3</sup>, demak '
                    '2<sup>4<i>x</i></sup> = 2<sup>3(<i>x</i>+1)</sup>. Asoslar teng '
                    'boʻlgani uchun darajalar teng: 4<i>x</i> = 3<i>x</i> + 3, bundan '
                    '<i>x</i> = 3.'},

    {'section': S, 'number': 15, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>ABC</i>, angle <i>C</i> is a right angle and '
                      'sin <i>A</i> = 9/41. What is the value of cos <i>A</i>?</p>',
     'choices': ['9/41', '9/40', '40/41', '40/9'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>40/41</strong>. sin <i>A</i> = qarshi ÷ '
                    'gipotenuza = 9/41, demak qarshi katet 9, gipotenuza 41. Pifagor '
                    'boʻyicha yondosh katet √(1,681 − 81) = √1,600 = 40, '
                    'va cos <i>A</i> = 40/41. <strong>9/40</strong> — bu '
                    'tan <i>A</i>: kosinusning maxrajida gipotenuza turadi.'},

    {'section': S, 'number': 16, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>a</i>(<i>x</i> − 5)<sup>2</sup> + 4, where <i>a</i> is a '
                      'constant. If <i>f</i>(8) = 31, what is the value of <i>a</i>?</p>',
     'choices': ['3', '4', '6', '9'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. <i>x</i> = 8 ni qoʻyamiz: '
                    '<i>a</i>(8 − 5)<sup>2</sup> + 4 = 9<i>a</i> + 4 = 31, demak '
                    '9<i>a</i> = 27 va <i>a</i> = 3. <strong>9</strong> — '
                    '(8 − 5) ni kvadratga koʻtarmay, 3<i>a</i> + 4 = 31 deb '
                    'hisoblagan javob.'},

    {'section': S, 'number': 17, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>The solution set of the inequality 17 − 3<i>x</i> &gt; '
                      '5<i>x</i> − 15 is <i>x</i> &lt; <i>k</i>, where <i>k</i> is a '
                      'constant. What is the value of <i>k</i>?</p>',
     'choices': ['−4', '2', '4', '8'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. 3<i>x</i> ni oʻngga, 15 ni chapga '
                    'oʻtkazamiz: 32 &gt; 8<i>x</i>, demak <i>x</i> &lt; 4 va <i>k</i> = '
                    '4. Diqqat: tengsizlikni <em>musbat</em> 8 ga boʻlganimiz uchun ishora '
                    'oʻzgarmadi.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 9(<i>x</i> − 2) = 6(<i>x</i> + 3), what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['12'],
     'explanation': 'Toʻgʻri javob <strong>12</strong>. Ikki qavsni ochamiz: 9<i>x</i> '
                    '− 18 = 6<i>x</i> + 18. 6<i>x</i> ni ayirib, 18 ni qoʻshamiz: '
                    '3<i>x</i> = 36, demak <i>x</i> = 12. Tekshirish: 9(10) = 90 va '
                    '6(15) = 90.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>A 30-litre solution is 20% acid by volume. How many litres of '
                      'pure acid must be added so that the solution becomes 36% acid by '
                      'volume?</p>' + GRID_NOTE,
     'accepted': ['7.5', '15/2'],
     'explanation': 'Toʻgʻri javob <strong>7.5</strong>. Boshida kislota 30 × 0.20 = 6 '
                    'litr. Sof kislota qoʻshilganda <em>ham</em> kislota, <em>ham</em> '
                    'umumiy hajm oshadi: (6 + <i>a</i>) ÷ (30 + <i>a</i>) = 0.36. Bundan '
                    '6 + <i>a</i> = 10.8 + 0.36<i>a</i>, yaʼni 0.64<i>a</i> = 4.8 va '
                    '<i>a</i> = 7.5. Eng keng tarqalgan xato — maxrajni 30 deb '
                    'qoldirish.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>2</sup> − 15<i>x</i> + 56 = 0 and '
                      '<i>x</i> ≠ 7, what is the value of <i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['8'],
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Koʻpaytmasi 56, yigʻindisi 15 '
                    'boʻlgan ikki son — 7 va 8, demak (<i>x</i> − 7)(<i>x</i> '
                    '− 8) = 0. Shart <i>x</i> ≠ 7 birinchi ildizni chiqarib '
                    'tashlaydi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If (6<i>x</i> + 5) ÷ 7 = 5, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['5'],
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Avval ikki tomonni 7 ga '
                    'koʻpaytiramiz: 6<i>x</i> + 5 = 35, keyin 5 ni ayirib 6 ga boʻlamiz: '
                    '<i>x</i> = 5. Kasr koʻrinishidagi tenglamada birinchi qadam har doim '
                    'maxrajdan qutulish.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 9<sup>2<i>x</i></sup> = 6,561, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['2'],
     'explanation': 'Toʻgʻri javob <strong>2</strong>. 9<sup>4</sup> = 6,561, demak '
                    '2<i>x</i> = 4 va <i>x</i> = 2. Eng keng tarqalgan xato — 4 '
                    'yozish: u 2<i>x</i> ning qiymati, <i>x</i> niki emas.'},
]
