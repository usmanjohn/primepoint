# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 3 · Math, Module 2 (LOWER)
#  22 questions · 35 minutes · taken by a pupil who scored under 14 on math1.
#  Questions 18–22 are student-produced responses (grid-ins).

#
#  Load: python manage.py load_mock exam/data/sat3_math2_easy.py --expect-questions=22
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §2
# ──────────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'Digital SAT — PrimePoint Mock 3',
    'language': 'english',
    'exam_format': 'sat',
    'exam_number': 203,
    'is_published': True,
}

# Copied unchanged into all six files of mock 3.
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
     'question_text': '<p>If <i>x</i> + 7 = 3, what is the value of <i>x</i>?</p>',
     'choices': ['−10', '−4', '4', '10'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>−4</strong>. Ikki tomondan 7 ni ayiramiz: '
                    '<i>x</i> = 3 − 7 = −4. Tekshirish: −4 + 7 = 3. '
                    '<strong>10</strong> — ayirish oʻrniga qoʻshgan javob.'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>A team won 12 of the 20 games it played. What percent of its '
                      'games did the team win?</p>',
     'choices': ['12%', '40%', '60%', '80%'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>60%</strong>. 12 ÷ 20 = 0.6, yaʼni 60%. '
                    '<strong>40%</strong> — yutqazilgan oʻyinlar ulushi (8/20): savol '
                    'yutilganini soʻraydi.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 4<i>x</i> − 5 = 23, what is the value of <i>x</i>?</p>',
     'choices': ['4.5', '7', '9', '18'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. 5 ni qoʻshamiz: 4<i>x</i> = 28, '
                    'soʻng 4 ga boʻlamiz: <i>x</i> = 7. <strong>4.5</strong> — '
                    '5 ni qoʻshish oʻrniga ayirgan javob (18 ÷ 4).'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>q</i> is defined by <i>q</i>(<i>x</i>) = '
                      '2<i>x</i><sup>2</sup>. What is the value of <i>q</i>(3)?</p>',
     'choices': ['12', '18', '36', '81'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>18</strong>. Avval daraja, keyin koʻpaytirish: '
                    '3<sup>2</sup> = 9 va 2 × 9 = 18. <strong>36</strong> — avval '
                    '2 × 3 = 6 qilib, keyin kvadratga koʻtargan javob: amallar tartibida '
                    'daraja koʻpaytirishdan oldin keladi.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>Two angles of a triangle measure 55° and 65°. What is '
                      'the measure of the third angle?</p>',
     'choices': ['50°', '60°', '70°', '120°'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>60°</strong>. Uchburchak burchaklari '
                    'yigʻindisi 180°, demak 180 − 55 − 65 = 60°. '
                    '<strong>120°</strong> — 55 + 65 ning oʻzi, yaʼni ayirishni '
                    'unutgan javob.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>The value of <i>y</i> is 4 more than half the value of <i>x</i>. '
                      'Which equation represents this relationship?</p>',
     'choices': [
         '<i>y</i> = (<i>x</i> + 4) ÷ 2',
         '<i>y</i> = <i>x</i> ÷ 2 + 4',
         '<i>y</i> = 2<i>x</i> + 4',
         '<i>y</i> = 4 − <i>x</i> ÷ 2',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>y</i> = <i>x</i> ÷ 2 + 4</strong>. "Half the '
                    'value of <i>x</i>" — <i>x</i> ÷ 2, "4 more than" esa unga 4 '
                    'qoʻshish. <strong><i>y</i> = (<i>x</i> + 4) ÷ 2</strong> avval '
                    'qoʻshib, keyin boʻladi — amal tartibi boshqa.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>What is 25% of 84?</p>',
     'choices': ['16', '21', '42', '63'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>21</strong>. 25% — toʻrtdan bir, demak '
                    '84 ÷ 4 = 21. <strong>63</strong> — 84 dan 25% '
                    '<em>ayirilgan</em> qoldiq: savol qismni soʻraydi.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>If <i>x</i><sup>2</sup> = 81 and <i>x</i> &gt; 0, what is the '
                      'value of <i>x</i>?</p>',
     'choices': ['9', '18', '40.5', '162'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. 9 × 9 = 81, va shart <i>x</i> &gt; 0 '
                    'ikkinchi ildiz −9 ni chiqarib tashlaydi. <strong>40.5</strong> '
                    '— 81 ÷ 2: kvadrat ildiz olish ikkiga boʻlish emas.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>In the equation 4<i>x</i> + 3<i>y</i> = 26, if <i>x</i> = 5, what '
                      'is the value of <i>y</i>?</p>',
     'choices': ['2', '3', '4', '6'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. <i>x</i> = 5 ni qoʻyamiz: '
                    '20 + 3<i>y</i> = 26, demak 3<i>y</i> = 6 va <i>y</i> = 2. '
                    '<strong>6</strong> — 3<i>y</i> ning qiymati: oxirgi boʻlish '
                    'qolib ketgan.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A rectangle has a length of 9 units and a width of 4 units. What '
                      'is its perimeter?</p>',
     'choices': ['13', '26', '36', '72'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>26</strong>. Perimetr — 2(uzunlik + eni) = '
                    '2(9 + 4) = 26. <strong>36</strong> — yuza (9 × 4): perimetr '
                    'chetdan aylanadi, yuza esa ichini toʻldiradi.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>Which expression is equivalent to (<i>x</i> − 2)(<i>x</i> '
                      '+ 6)?</p>',
     'choices': [
         '<i>x</i><sup>2</sup> − 4<i>x</i> − 12',
         '<i>x</i><sup>2</sup> + 4<i>x</i> − 12',
         '<i>x</i><sup>2</sup> + 4<i>x</i> + 12',
         '<i>x</i><sup>2</sup> + 8<i>x</i> − 12',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>x</i><sup>2</sup> + 4<i>x</i> − 12'
                    '</strong>. Har bir aʼzoni koʻpaytiramiz: 6<i>x</i> − 2<i>x</i> '
                    '= 4<i>x</i>, va (−2)(6) = −12. <strong><i>x</i><sup>2</sup> '
                    '− 4<i>x</i> − 12</strong> — oʻrtadagi aʼzoning '
                    'ishorasini almashtirib yuborgan javob: katta son musbat edi.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>If 2(<i>x</i> + 7) = 30, what is the value of <i>x</i>?</p>',
     'choices': ['8', '15', '16', '23'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Ikki tomonni 2 ga boʻlamiz: '
                    '<i>x</i> + 7 = 15, demak <i>x</i> = 8. <strong>15</strong> — '
                    '<i>x</i> + 7 ning qiymati: oxirgi qadam qolib ketgan.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>What is the range of the data set 6, 11, 4, 19, 9?</p>',
     'choices': ['9', '11', '15', '19'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>15</strong>. Kenglik (range) — eng katta '
                    'va eng kichik sonning ayirmasi: 19 − 4 = 15. <strong>9</strong> '
                    '— tartiblangan qatorning oʻrtasidagi son, yaʼni mediana: kenglik '
                    'bilan medianani adashtirmang.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If 3<sup><i>x</i></sup> = 81, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['4', '9', '27', '78'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. 3 × 3 × 3 × 3 = 81, demak '
                    '81 = 3<sup>4</sup>. <strong>27</strong> — 81 ÷ 3: daraja '
                    'koʻrsatkichi boʻlish bilan topilmaydi.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A gym charges a one-time joining fee of $15 plus $6 for each '
                      'visit. What is the total cost of joining and making 7 visits?</p>',
     'choices': ['$42', '$57', '$63', '$105'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>$57</strong>. Tashriflar uchun 6 × 7 = $42, '
                    'ustiga bir martalik $15: 42 + 15 = $57. <strong>$105</strong> — '
                    '(15 + 6) × 7, yaʼni bir martalik toʻlovni ham har tashrifga qoʻshib '
                    'yuborgan javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A circle has a radius of 8 units. What is its circumference?</p>',
     'choices': ['8π', '16π', '64π', '256π'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>16π</strong>. Aylana uzunligi '
                    '2π<i>r</i> = 2 × π × 8 = 16π. '
                    '<strong>64π</strong> — yuza (π<i>r</i><sup>2</sup>): '
                    'ikki formulani ajratib turing.'},

    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>The functions <i>f</i> and <i>g</i> are defined by '
                      '<i>f</i>(<i>x</i>) = 3<i>x</i> and <i>g</i>(<i>x</i>) = <i>x</i> '
                      '− 2. What is the value of <i>f</i>(<i>g</i>(5))?</p>',
     'choices': ['9', '13', '15', '45'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Ichkaridan boshlaymiz: '
                    '<i>g</i>(5) = 5 − 2 = 3, keyin <i>f</i>(3) = 3 × 3 = 9. '
                    '<strong>13</strong> — tartibni teskari olgan javob: '
                    '<i>g</i>(<i>f</i>(5)) = <i>g</i>(15) = 13.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i> ÷ 5 = 8, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['40'],
     'explanation': 'Toʻgʻri javob <strong>40</strong>. Ikki tomonni 5 ga koʻpaytiramiz: '
                    '<i>x</i> = 8 × 5 = 40. Tekshirish: 40 ÷ 5 = 8.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>A box contains 6 blue pens and 9 yellow pens and no others. What '
                      'fraction of the pens in the box are blue?</p>' + GRID_NOTE,
     'accepted': ['2/5', '0.4', '6/15'],
     'explanation': 'Toʻgʻri javob <strong>2/5</strong> (0.4 ham qabul qilinadi). Jami '
                    '6 + 9 = 15 ta, koʻklari 6 ta, demak 6/15 = 2/5. Eng keng tarqalgan '
                    'xato — 6/9 yozish: maxraj <em>jami</em> son boʻlishi kerak.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>3</sup> = 64, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['4'],
     'explanation': 'Toʻgʻri javob <strong>4</strong>. 4 × 4 × 4 = 64. Kub ildizda son '
                    'uch marta koʻpaytiriladi — 8 emas (8 bu 64 ning kvadrat '
                    'ildizi).'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 7<i>x</i> + 5 = 54, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['7'],
     'explanation': 'Toʻgʻri javob <strong>7</strong>. 5 ni ayiramiz: 7<i>x</i> = 49, '
                    'soʻng 7 ga boʻlamiz: <i>x</i> = 7. Tekshirish: 7 × 7 + 5 = 54.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '6<i>x</i> − 4. If <i>f</i>(<i>a</i>) = 32, what is the value '
                      'of <i>a</i>?</p>' + GRID_NOTE,
     'accepted': ['6'],
     'explanation': 'Toʻgʻri javob <strong>6</strong>. 6<i>a</i> − 4 = 32 dan '
                    '6<i>a</i> = 36, demak <i>a</i> = 6. Tekshirish: 6 × 6 − 4 = 32.'},
]
