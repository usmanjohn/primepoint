# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 4 · Math, Module 2 (UPPER)
#  22 questions · 35 minutes · taken by a pupil who scored 14 or more on math1.
#  Questions 18–22 are student-produced responses (grid-ins).

#
#  Load: python manage.py load_mock exam/data/sat4_math2_hard.py --expect-questions=22
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §2
# ──────────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'Digital SAT — PrimePoint Mock 4',
    'language': 'english',
    'exam_format': 'sat',
    'exam_number': 204,
    'is_published': True,
}

# Copied unchanged into all six files of mock 4.
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
     'question_text': '<p>If 6(2<i>x</i> − 5) = 7<i>x</i> + 20, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['5', '10', '15', '50'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>10</strong>. Qavsni ochamiz: 12<i>x</i> '
                    '− 30 = 7<i>x</i> + 20. 7<i>x</i> ni ayirib, 30 ni qoʻshamiz: '
                    '5<i>x</i> = 50, demak <i>x</i> = 10. <strong>50</strong> — '
                    '5<i>x</i> ning qiymati, yaʼni oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 2, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '3<i>x</i><sup>2</sup> + <i>x</i>. Which expression is equivalent to '
                      '<i>f</i>(<i>x</i> + 1) − <i>f</i>(<i>x</i>)?</p>',
     'choices': [
         '3<i>x</i> + 4',
         '6<i>x</i> − 2',
         '6<i>x</i> + 2',
         '6<i>x</i> + 4',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>6<i>x</i> + 4</strong>. '
                    '<i>f</i>(<i>x</i>+1) = 3(<i>x</i>+1)<sup>2</sup> + (<i>x</i>+1) = '
                    '3<i>x</i><sup>2</sup> + 6<i>x</i> + 3 + <i>x</i> + 1 = '
                    '3<i>x</i><sup>2</sup> + 7<i>x</i> + 4. Undan <i>f</i>(<i>x</i>) = '
                    '3<i>x</i><sup>2</sup> + <i>x</i> ni ayiramiz: 6<i>x</i> + 4. '
                    '<strong>6<i>x</i> + 2</strong> — (<i>x</i>+1)<sup>2</sup> ni '
                    'ochishda oxirgi 3 ni tushirib qoldirgan javob.'},

    {'section': S, 'number': 3, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>A quantity increases by 50% and the result then decreases by 40%. '
                      'The final quantity is what percent of the original?</p>',
     'choices': ['85%', '90%', '100%', '110%'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>90%</strong>. Foiz har safar <em>joriy</em> '
                    'qiymatdan olinadi: 1.50 × 0.60 = 0.90, yaʼni 90%. '
                    '<strong>110%</strong> — foizlarni qoʻshib-ayirgan javob '
                    '(+50 − 40 = +10): foizlarni bir-biriga qoʻshib boʻlmaydi, '
                    'ular koʻpaytiriladi.'},

    {'section': S, 'number': 4, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>7<i>x</i> − 3<i>y</i> = 25<br>2<i>x</i> + 3<i>y</i> = 38</p>'
                      '<p>The system of equations above has a unique solution. What is the '
                      'value of <i>x</i>?</p>',
     'choices': ['5', '7', '8', '9'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. Ikki tenglamani qoʻshsak '
                    '<i>y</i> qisqaradi: 9<i>x</i> = 63, demak <i>x</i> = 7. Qoʻshish '
                    'usuli aynan shunday holat uchun: bir xil koeffitsiyent qarama-qarshi '
                    'ishorada turibdi. <strong>8</strong> — <i>y</i> ning qiymati.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A right circular cylinder has a radius of 5 units and a height of '
                      '6 units. What is its volume?</p>',
     'choices': ['30π', '60π', '150π', '900π'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>150π</strong>. Silindr hajmi '
                    'π<i>r</i><sup>2</sup><i>h</i> = π × 25 × 6 = 150π. '
                    '<strong>30π</strong> — radiusni kvadratga koʻtarmay, '
                    '5 × 6 hisoblagan javob.'},

    {'section': S, 'number': 6, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The equation <i>x</i><sup>2</sup> + <i>kx</i> + 9 = 0, where '
                      '<i>k</i> is a constant, has exactly one distinct real solution. '
                      'Which of the following is a possible value of <i>k</i>?</p>',
     'choices': ['−9', '−3', '6', '9'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Bitta yechim boʻlishi uchun '
                    'diskriminant nolga teng: <i>k</i><sup>2</sup> − 4(1)(9) = 0, '
                    'yaʼni <i>k</i><sup>2</sup> = 36 va <i>k</i> = ±6. '
                    '<strong>−3</strong> — <i>k</i> ni ildizning oʻzi '
                    '(<i>x</i> = −3) bilan adashtirgan javob.'},

    {'section': S, 'number': 7, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>4<i>x</i> + 6<i>y</i> = 10<br>10<i>x</i> + 15<i>y</i> = '
                      '<i>c</i></p>'
                      '<p>In the system above, <i>c</i> is a constant. If the system has '
                      'infinitely many solutions, what is the value of <i>c</i>?</p>',
     'choices': ['15', '20', '25', '30'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>25</strong>. Cheksiz koʻp yechim boʻlishi uchun '
                    'ikkinchi tenglama birinchisining koʻpaytmasi boʻlishi kerak. '
                    '10 ÷ 4 = 2.5 va 15 ÷ 6 = 2.5 — koʻpaytuvchi 2.5, demak '
                    '<i>c</i> = 2.5 × 10 = 25. <strong>20</strong> — koʻpaytuvchini '
                    '2 deb olgan javob: koeffitsiyentlarni tekshiring.'},

    {'section': S, 'number': 8, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>A boat travels 24 kilometres upstream at an average speed of 4 '
                      'kilometres per hour and returns downstream at an average speed of 12 '
                      'kilometres per hour. What is its average speed, in kilometres per '
                      'hour, for the whole journey?</p>',
     'choices': ['5', '6', '7', '8'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Oʻrtacha tezlik — <em>jami '
                    'masofa</em> ÷ <em>jami vaqt</em>. Masofa 48 km; vaqt 24/4 + 24/12 = '
                    '6 + 2 = 8 soat; 48 ÷ 8 = 6. <strong>8</strong> — (4 + 12) ÷ 2, '
                    'eng keng tarqalgan tuzoq: sekin yoʻlda uch barobar koʻp vaqt '
                    'ketadi.'},

    {'section': S, 'number': 9, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>What is the solution to the equation √(4<i>x</i> + 9) = '
                      '<i>x</i> + 1?</p>',
     'choices': ['−2', '2', '4', '8'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Ikki tomonni kvadratga koʻtaramiz: '
                    '4<i>x</i> + 9 = <i>x</i><sup>2</sup> + 2<i>x</i> + 1, yaʼni '
                    '<i>x</i><sup>2</sup> − 2<i>x</i> − 8 = 0 va (<i>x</i> '
                    '− 4)(<i>x</i> + 2) = 0. <strong>−2</strong> — begona '
                    'ildiz: <i>x</i> = −2 da oʻng tomon −1 boʻladi, kvadrat '
                    'ildiz esa manfiy boʻla olmaydi.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, a circle is given by the equation '
                      '<i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> + 8<i>x</i> − '
                      '6<i>y</i> = 11. What is the radius of the circle?</p>',
     'choices': ['5', '6', '11', '36'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Toʻliq kvadratga keltiramiz: '
                    '<i>x</i><sup>2</sup> + 8<i>x</i> = (<i>x</i> + 4)<sup>2</sup> '
                    '− 16 va <i>y</i><sup>2</sup> − 6<i>y</i> = (<i>y</i> '
                    '− 3)<sup>2</sup> − 9. Demak (<i>x</i> + 4)<sup>2</sup> + '
                    '(<i>y</i> − 3)<sup>2</sup> = 11 + 16 + 9 = 36 va radius '
                    '√36 = 6. <strong>36</strong> — <i>r</i><sup>2</sup> ning '
                    'oʻzi.'},

    {'section': S, 'number': 11, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>A line in the <i>xy</i>-plane passes through the points '
                      '(−1, 10) and (3, −6). What is the <i>y</i>-coordinate of '
                      'the <i>y</i>-intercept of the line?</p>',
     'choices': ['−6', '4', '6', '10'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Burchak koeffitsiyenti '
                    '(−6 − 10) ÷ (3 − (−1)) = −16 ÷ 4 = '
                    '−4. Endi (3, −6) ni <i>y</i> = −4<i>x</i> + <i>b</i> '
                    'ga qoʻyamiz: −6 = −12 + <i>b</i>, demak <i>b</i> = 6. '
                    '<strong>10</strong> — (−1, 10) nuqtaning <i>y</i> qiymati: '
                    'bu nuqta <i>y</i> oʻqida emas.'},

    {'section': S, 'number': 12, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>If <i>x</i> − 1/<i>x</i> = 5, what is the value of '
                      '<i>x</i><sup>3</sup> − 1/<i>x</i><sup>3</sup>?</p>',
     'choices': ['110', '125', '140', '155'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>140</strong>. Kubga koʻtaramiz: (<i>x</i> '
                    '− 1/<i>x</i>)<sup>3</sup> = <i>x</i><sup>3</sup> − '
                    '1/<i>x</i><sup>3</sup> − 3(<i>x</i> − 1/<i>x</i>) = 125. '
                    'Demak <i>x</i><sup>3</sup> − 1/<i>x</i><sup>3</sup> = 125 + '
                    '3 × 5 = 140. <strong>125</strong> — oʻrtadagi hadni unutgan '
                    'javob. Diqqat: ayirmada u <em>manfiy</em>, shuning uchun uni '
                    'qoʻshamiz.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>The mean of 10 numbers is 30. Two of the numbers, 12 and 18, are '
                      'then removed. What is the mean of the remaining 8 numbers?</p>',
     'choices': ['32', '33.75', '34', '35'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>33.75</strong>. Yigʻindilar bilan ishlaymiz: '
                    'avval 10 × 30 = 300, olib tashlanganlar 12 + 18 = 30, qolgani '
                    '300 − 30 = 270. Endi 270 ÷ 8 = 33.75. <strong>32</strong> '
                    '— taxminiy yaxlitlash: oʻrtacha masalasini har doim yigʻindi '
                    'orqali yeching.'},

    {'section': S, 'number': 14, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>If 27<sup><i>x</i></sup> = 9<sup><i>x</i>+2</sup>, what is the '
                      'value of <i>x</i>?</p>',
     'choices': ['1', '2', '4', '6'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Ikki tomonni 3 asosiga keltiramiz: '
                    '27 = 3<sup>3</sup> va 9 = 3<sup>2</sup>, demak '
                    '3<sup>3<i>x</i></sup> = 3<sup>2(<i>x</i>+2)</sup>. Asoslar teng '
                    'boʻlgani uchun darajalar teng: 3<i>x</i> = 2<i>x</i> + 4, bundan '
                    '<i>x</i> = 4.'},

    {'section': S, 'number': 15, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>ABC</i>, angle <i>C</i> is a right angle and '
                      'cos <i>A</i> = 20/29. What is the value of tan <i>A</i>?</p>',
     'choices': ['20/29', '21/29', '20/21', '21/20'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>21/20</strong>. cos <i>A</i> = yondosh ÷ '
                    'gipotenuza = 20/29, demak yondosh katet 20, gipotenuza 29. Pifagor '
                    'boʻyicha qarshi katet √(841 − 400) = √441 = 21. '
                    'tan <i>A</i> = qarshi ÷ yondosh = 21/20. <strong>21/29</strong> '
                    '— bu sin <i>A</i>: tangensning maxrajida gipotenuza emas, '
                    'yondosh katet turadi.'},

    {'section': S, 'number': 16, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>a</i>(<i>x</i> + 1)<sup>2</sup> − 7, where <i>a</i> is a '
                      'constant. If <i>f</i>(3) = 25, what is the value of <i>a</i>?</p>',
     'choices': ['2', '3', '4', '8'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. <i>x</i> = 3 ni qoʻyamiz: '
                    '<i>a</i>(3 + 1)<sup>2</sup> − 7 = 16<i>a</i> − 7 = 25, '
                    'demak 16<i>a</i> = 32 va <i>a</i> = 2. <strong>8</strong> — '
                    '(3 + 1) ni kvadratga koʻtarmay, 4<i>a</i> − 7 = 25 deb '
                    'hisoblagan javob.'},

    {'section': S, 'number': 17, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>The solution set of the inequality 13 − 2<i>x</i> ≤ '
                      '4<i>x</i> − 17 is <i>x</i> ≥ <i>k</i>, where <i>k</i> is a '
                      'constant. What is the value of <i>k</i>?</p>',
     'choices': ['−5', '3', '5', '7'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. 2<i>x</i> ni oʻngga, 17 ni chapga '
                    'oʻtkazamiz: 30 ≤ 6<i>x</i>, demak <i>x</i> ≥ 5 va '
                    '<i>k</i> = 5. Diqqat: tengsizlikni <em>musbat</em> 6 ga '
                    'boʻlganimiz uchun ishora oʻzgarmadi — ishora faqat manfiy songa '
                    'boʻlganda aylanadi.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 7(<i>x</i> − 2) = 4(<i>x</i> + 4), what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['10'],
     'explanation': 'Toʻgʻri javob <strong>10</strong>. Ikki qavsni ochamiz: 7<i>x</i> '
                    '− 14 = 4<i>x</i> + 16. 4<i>x</i> ni ayirib, 14 ni qoʻshamiz: '
                    '3<i>x</i> = 30, demak <i>x</i> = 10. Tekshirish: 7(8) = 56 va '
                    '4(14) = 56.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>A 20-litre mixture is 30% juice by volume. How many litres of '
                      'pure juice must be added so that the mixture is 44% juice by '
                      'volume?</p>' + GRID_NOTE,
     'accepted': ['5'],
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Boshida sharbat 20 × 0.30 = 6 litr. '
                    'Sof sharbat qoʻshilganda <em>ham</em> sharbat, <em>ham</em> umumiy '
                    'hajm oshadi: (6 + <i>a</i>) ÷ (20 + <i>a</i>) = 0.44. Bundan '
                    '6 + <i>a</i> = 8.8 + 0.44<i>a</i>, yaʼni 0.56<i>a</i> = 2.8 va '
                    '<i>a</i> = 5. Eng keng tarqalgan xato — maxrajni 20 deb '
                    'qoldirish.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>2</sup> − 13<i>x</i> + 40 = 0 and '
                      '<i>x</i> ≠ 5, what is the value of <i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['8'],
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Koʻpaytmasi 40, yigʻindisi 13 '
                    'boʻlgan ikki son — 5 va 8, demak (<i>x</i> − 5)(<i>x</i> '
                    '− 8) = 0. Shart <i>x</i> ≠ 5 birinchi ildizni chiqarib '
                    'tashlaydi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If (5<i>x</i> − 4) ÷ 6 = 6, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['8'],
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Avval ikki tomonni 6 ga '
                    'koʻpaytiramiz: 5<i>x</i> − 4 = 36, keyin 4 ni qoʻshib 5 ga '
                    'boʻlamiz: <i>x</i> = 8. Kasr koʻrinishidagi tenglamada birinchi '
                    'qadam har doim maxrajdan qutulish.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 4<sup>3<i>x</i></sup> = 4,096, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['2'],
     'explanation': 'Toʻgʻri javob <strong>2</strong>. 4<sup>6</sup> = 4,096, demak '
                    '3<i>x</i> = 6 va <i>x</i> = 2. Eng keng tarqalgan xato — 6 '
                    'yozish: u 3<i>x</i> ning qiymati, <i>x</i> niki emas.'},
]
