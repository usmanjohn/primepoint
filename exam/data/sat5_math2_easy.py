# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 5 · Math, Module 2 (LOWER)
#  22 questions · 35 minutes · taken by a pupil who scored under 14 on math1.
#  Questions 18–22 are student-produced responses (grid-ins).

#
#  Load: python manage.py load_mock exam/data/sat5_math2_easy.py --expect-questions=22
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

S = 'math2e'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If <i>x</i> + 8 = 2, what is the value of <i>x</i>?</p>',
     'choices': ['−10', '−6', '6', '10'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>−6</strong>. Ikki tomondan 8 ni ayiramiz: '
                    '<i>x</i> = 2 − 8 = −6. Tekshirish: −6 + 8 = 2. '
                    '<strong>10</strong> — ayirish oʻrniga qoʻshgan javob.'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>Of the 36 students who took a test, 27 passed. What percent of '
                      'the students passed?</p>',
     'choices': ['25%', '27%', '75%', '90%'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>75%</strong>. 27 ÷ 36 = 0.75, yaʼni 75%. '
                    '<strong>25%</strong> — yiqilganlar ulushi (9/36): savol '
                    'oʻtganlarni soʻraydi.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 6<i>x</i> − 5 = 37, what is the value of <i>x</i>?</p>',
     'choices': ['5', '7', '32', '42'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. 5 ni qoʻshamiz: 6<i>x</i> = 42, '
                    'soʻng 6 ga boʻlamiz: <i>x</i> = 7. <strong>42</strong> — '
                    '6<i>x</i> ning qiymati: oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>n</i> is defined by <i>n</i>(<i>x</i>) = '
                      '3<i>x</i><sup>2</sup>. What is the value of <i>n</i>(4)?</p>',
     'choices': ['24', '36', '48', '144'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>48</strong>. Avval daraja, keyin koʻpaytirish: '
                    '4<sup>2</sup> = 16 va 3 × 16 = 48. <strong>144</strong> — avval '
                    '3 × 4 = 12 qilib, keyin kvadratga koʻtargan javob: amallar tartibida '
                    'daraja oldin keladi.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>A rectangle has a length of 11 units and a width of 6 units. What '
                      'is its area?</p>',
     'choices': ['17', '34', '66', '121'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>66</strong>. Toʻgʻri toʻrtburchak yuzasi '
                    'uzunlik × eni = 11 × 6 = 66. <strong>34</strong> — perimetr '
                    '(2 × 17): yuza koʻpaytma orqali topiladi.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>The value of <i>y</i> is 7 more than three times the value of '
                      '<i>x</i>. Which equation represents this relationship?</p>',
     'choices': [
         '<i>y</i> = 3(<i>x</i> + 7)',
         '<i>y</i> = 3<i>x</i> + 7',
         '<i>y</i> = 7 − 3<i>x</i>',
         '<i>y</i> = 7<i>x</i> + 3',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>y</i> = 3<i>x</i> + 7</strong>. "Three times '
                    '<i>x</i>" — 3<i>x</i>, "7 more than" esa unga 7 qoʻshish. '
                    '<strong><i>y</i> = 3(<i>x</i> + 7)</strong> avval qoʻshib, keyin '
                    'uchlaydi — amal tartibi boshqa.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>What is 60% of 45?</p>',
     'choices': ['18', '25', '27', '30'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>27</strong>. 45 × 0.6 = 27. Yoki: 10% = 4.5, '
                    'demak 60% = 27. <strong>18</strong> — qolgan 40%: savol '
                    'soʻralgan qismni beradi.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>If <i>x</i><sup>2</sup> = 144 and <i>x</i> &gt; 0, what is the '
                      'value of <i>x</i>?</p>',
     'choices': ['12', '24', '72', '288'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>12</strong>. 12 × 12 = 144, va shart '
                    '<i>x</i> &gt; 0 ikkinchi ildiz −12 ni chiqarib tashlaydi. '
                    '<strong>72</strong> — 144 ÷ 2: kvadrat ildiz olish ikkiga '
                    'boʻlish emas.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>In the equation 3<i>x</i> + 5<i>y</i> = 41, if <i>x</i> = 7, what '
                      'is the value of <i>y</i>?</p>',
     'choices': ['4', '6', '8', '20'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. <i>x</i> = 7 ni qoʻyamiz: '
                    '21 + 5<i>y</i> = 41, demak 5<i>y</i> = 20 va <i>y</i> = 4. '
                    '<strong>20</strong> — 5<i>y</i> ning qiymati: oxirgi boʻlish '
                    'qolib ketgan.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>Two angles of a triangle measure 40° and 95°. What is '
                      'the measure of the third angle?</p>',
     'choices': ['35°', '45°', '55°', '135°'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>45°</strong>. Uchburchak burchaklari '
                    'yigʻindisi 180°, demak 180 − 40 − 95 = 45°. '
                    '<strong>135°</strong> — 40 + 95 ning oʻzi, yaʼni ayirishni '
                    'unutgan javob.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>Which expression is equivalent to (<i>x</i> − 5)(<i>x</i> '
                      '+ 2)?</p>',
     'choices': [
         '<i>x</i><sup>2</sup> − 7<i>x</i> − 10',
         '<i>x</i><sup>2</sup> − 3<i>x</i> − 10',
         '<i>x</i><sup>2</sup> + 3<i>x</i> − 10',
         '<i>x</i><sup>2</sup> − 3<i>x</i> + 10',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>x</i><sup>2</sup> − 3<i>x</i> − 10'
                    '</strong>. Har bir aʼzoni koʻpaytiramiz: 2<i>x</i> − 5<i>x</i> = '
                    '−3<i>x</i>, va (−5)(2) = −10. '
                    '<strong><i>x</i><sup>2</sup> + 3<i>x</i> − 10</strong> — '
                    'oʻrtadagi aʼzoning ishorasini almashtirib yuborgan javob: katta son '
                    'manfiy edi.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>If 5(<i>x</i> + 4) = 45, what is the value of <i>x</i>?</p>',
     'choices': ['5', '9', '25', '41'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Ikki tomonni 5 ga boʻlamiz: '
                    '<i>x</i> + 4 = 9, demak <i>x</i> = 5. <strong>9</strong> — '
                    '<i>x</i> + 4 ning qiymati: oxirgi qadam qolib ketgan.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>What is the median of the data set 2, 5, 8, 11, 14, 17?</p>',
     'choices': ['8', '9.5', '10', '11'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>9.5</strong>. Sonlar juft (oltita), demak '
                    'mediana oʻrtadagi ikki sonning oʻrtachasi: (8 + 11) ÷ 2 = 9.5. '
                    '<strong>8</strong> — uchinchi sonni mediana deb olgan javob.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If 4<sup><i>x</i></sup> = 16, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['2', '4', '8', '12'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. 4 × 4 = 16, demak 16 = '
                    '4<sup>2</sup>. <strong>4</strong> — 16 ÷ 4: daraja koʻrsatkichi '
                    'boʻlish bilan topilmaydi.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A taxi charges a flat fee of $3.00 plus $1.50 for each kilometre '
                      'travelled. What is the fare for a journey of 8 kilometres?</p>',
     'choices': ['$12.00', '$15.00', '$24.00', '$36.00'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>$15.00</strong>. Masofa uchun 1.50 × 8 = '
                    '$12.00, ustiga bir martalik $3.00: 12 + 3 = $15.00. '
                    '<strong>$36.00</strong> — (3 + 1.50) × 8, yaʼni bir martalik '
                    'toʻlovni ham har kilometrga qoʻshib yuborgan javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A circle has a diameter of 20 units. What is its area?</p>',
     'choices': ['20π', '40π', '100π', '400π'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>100π</strong>. Diametr 20 boʻlsa radius '
                    '10, yuza esa π<i>r</i><sup>2</sup> = 100π. '
                    '<strong>400π</strong> — radius oʻrniga diametrni kvadratga '
                    'koʻtargan javob.'},

    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>The functions <i>f</i> and <i>g</i> are defined by '
                      '<i>f</i>(<i>x</i>) = 2<i>x</i> and <i>g</i>(<i>x</i>) = <i>x</i> + '
                      '5. What is the value of <i>f</i>(<i>g</i>(3))?</p>',
     'choices': ['11', '13', '16', '30'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>16</strong>. Ichkaridan boshlaymiz: '
                    '<i>g</i>(3) = 3 + 5 = 8, keyin <i>f</i>(8) = 2 × 8 = 16. '
                    '<strong>11</strong> — tartibni teskari olgan javob: '
                    '<i>g</i>(<i>f</i>(3)) = <i>g</i>(6) = 11.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i> ÷ 6 = 9, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['54'],
     'explanation': 'Toʻgʻri javob <strong>54</strong>. Ikki tomonni 6 ga koʻpaytiramiz: '
                    '<i>x</i> = 9 × 6 = 54. Tekshirish: 54 ÷ 6 = 9.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>A tray holds 7 apples and 13 pears and no other fruit. What '
                      'fraction of the fruit on the tray are apples?</p>' + GRID_NOTE,
     'accepted': ['7/20', '0.35'],
     'explanation': 'Toʻgʻri javob <strong>7/20</strong> (0.35 ham qabul qilinadi). Jami '
                    '7 + 13 = 20 ta, olmalar 7 ta, demak 7/20. Eng keng tarqalgan xato '
                    '— 7/13 yozish: maxraj <em>jami</em> son boʻlishi kerak.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>3</sup> = 125, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['5'],
     'explanation': 'Toʻgʻri javob <strong>5</strong>. 5 × 5 × 5 = 125. Kub ildizda son '
                    'uch marta koʻpaytiriladi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 8<i>x</i> + 9 = 65, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['7'],
     'explanation': 'Toʻgʻri javob <strong>7</strong>. 9 ni ayiramiz: 8<i>x</i> = 56, '
                    'soʻng 8 ga boʻlamiz: <i>x</i> = 7. Tekshirish: 8 × 7 + 9 = 65.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '9<i>x</i> − 5. If <i>f</i>(<i>a</i>) = 49, what is the value '
                      'of <i>a</i>?</p>' + GRID_NOTE,
     'accepted': ['6'],
     'explanation': 'Toʻgʻri javob <strong>6</strong>. 9<i>a</i> − 5 = 49 dan '
                    '9<i>a</i> = 54, demak <i>a</i> = 6. Tekshirish: 9 × 6 − 5 = 49.'},
]
