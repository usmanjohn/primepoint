# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 1 · Math, Module 2 (LOWER)
#  22 questions · 35 minutes · taken by a pupil who scored under 14 on math1.
#  Questions 18–22 are student-produced responses (grid-ins).
#
#  Load: python manage.py load_mock exam/data/sat1_math2_easy.py --expect-questions=22
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §3
# ──────────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'Digital SAT — PrimePoint Mock 1',
    'language': 'english',
    'exam_format': 'sat',
    'exam_number': 201,
    'is_published': True,
}

# Copied unchanged into all six files of mock 1.
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
     'question_text': '<p>If <i>x</i> + 9 = 4, what is the value of <i>x</i>?</p>',
     'choices': ['−13', '−5', '5', '13'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>−5</strong>. Ikki tomondan 9 ni ayiramiz: '
                    '<i>x</i> = 4 − 9 = −5. Tekshirish: −5 + 9 = 4. '
                    '<strong>5</strong> — minus ishorasini tushirib qoldirgan javob.'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>A recipe uses 3 cups of flour to make 12 cookies. At this '
                      'rate, how many cups of flour are needed to make 20 cookies?</p>',
     'choices': ['4', '5', '6', '8'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Bitta pechenyega 3 ÷ 12 = 0.25 '
                    'stakan un ketadi, demak 20 tasiga 20 × 0.25 = 5 stakan. Yoki '
                    'proportsiya bilan: 3/12 = <i>x</i>/20, bundan <i>x</i> = 5.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 2<i>x</i> − 3 = 11, what is the value of <i>x</i>?</p>',
     'choices': ['4', '7', '8', '14'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. Avval 3 ni qoʻshamiz: 2<i>x</i> = 14, '
                    'soʻng 2 ga boʻlamiz: <i>x</i> = 7. <strong>14</strong> — 2<i>x</i> '
                    'ning qiymati, yaʼni oxirgi boʻlishni unutgan javob.'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> + 4. What is the value of '
                      '<i>f</i>(5)?</p>',
     'choices': ['9', '14', '29', '54'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>29</strong>. 5<sup>2</sup> = 25, keyin '
                    '25 + 4 = 29. <strong>14</strong> — kvadratni koʻpaytirish deb tushunib, '
                    '5 × 2 + 4 = 14 hisoblagan javob: <i>x</i><sup>2</sup> = <i>x</i> × '
                    '<i>x</i>, 2<i>x</i> emas.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>A rectangle has a length of 12 units and a width of 7 units. '
                      'What is the perimeter of the rectangle?</p>',
     'choices': ['19', '38', '42', '84'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>38</strong>. Perimetr — 2(uzunlik + eni) = '
                    '2(12 + 7) = 2 × 19 = 38. <strong>84</strong> — yuza (12 × 7), yaʼni '
                    'perimetr bilan yuzani almashtirib yuborgan javob.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>The value of <i>y</i> is 3 more than twice the value of '
                      '<i>x</i>. Which equation represents this relationship?</p>',
     'choices': [
         '<i>y</i> = 2(<i>x</i> + 3)',
         '<i>y</i> = 2<i>x</i> + 3',
         '<i>y</i> = 3<i>x</i> + 2',
         '<i>y</i> = 3(<i>x</i> + 2)',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>y</i> = 2<i>x</i> + 3</strong>. "Twice the '
                    'value of <i>x</i>" — 2<i>x</i>, "3 more than" esa unga 3 qoʻshish. '
                    '<strong><i>y</i> = 2(<i>x</i> + 3)</strong> avval qoʻshib, keyin '
                    'ikkilantiradi — bu boshqa amal tartibi.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>What is 20% of 350?</p>',
     'choices': ['30', '70', '175', '280'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>70</strong>. 350 × 0.20 = 70. Yoki: 10% = 35, '
                    'demak 20% = 70. <strong>280</strong> — 350 dan 20% <em>ayirilgan</em> '
                    'qiymat: savol qismni soʻraydi, qoldiqni emas.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>If <i>x</i><sup>2</sup> = 64 and <i>x</i> &gt; 0, what is the '
                      'value of <i>x</i>?</p>',
     'choices': ['4', '8', '16', '32'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. 8 × 8 = 64, va shart <i>x</i> &gt; 0 '
                    'ikkinchi ildiz −8 ni chiqarib tashlaydi. <strong>32</strong> — '
                    '64 ni 2 ga boʻlgan javob: kvadrat ildiz olish ikkiga boʻlish emas.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>In the equation 3<i>x</i> + 2<i>y</i> = 18, if <i>y</i> = 3, '
                      'what is the value of <i>x</i>?</p>',
     'choices': ['2', '4', '6', '8'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. <i>y</i> = 3 ni qoʻyamiz: '
                    '3<i>x</i> + 6 = 18, demak 3<i>x</i> = 12 va <i>x</i> = 4. '
                    '<strong>6</strong> — 18 ÷ 3 ni hisoblab, 2<i>y</i> ni ayirishni '
                    'unutgan javob.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A circle has a radius of 5 units. What is the area of the '
                      'circle?</p>',
     'choices': ['10π', '25π', '50π', '100π'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>25π</strong>. Yuza π<i>r</i><sup>2</sup> '
                    '= π × 5<sup>2</sup> = 25π. <strong>10π</strong> — '
                    'aylana uzunligi 2π<i>r</i>: ikki formulani ajratib turing, yuzada '
                    'radius kvadratga koʻtariladi.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>Which expression is equivalent to (<i>x</i> + 4)(<i>x</i> '
                      '− 2)?</p>',
     'choices': [
         '<i>x</i><sup>2</sup> − 2<i>x</i> − 8',
         '<i>x</i><sup>2</sup> + 2<i>x</i> − 8',
         '<i>x</i><sup>2</sup> + 2<i>x</i> + 8',
         '<i>x</i><sup>2</sup> + 6<i>x</i> − 8',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>x</i><sup>2</sup> + 2<i>x</i> − 8</strong>. '
                    'Har bir aʼzoni koʻpaytiramiz: <i>x</i>·<i>x</i> = <i>x</i><sup>2</sup>, '
                    '<i>x</i>·(−2) = −2<i>x</i>, 4·<i>x</i> = 4<i>x</i>, '
                    '4·(−2) = −8. Oʻrtadagilar: −2<i>x</i> + 4<i>x</i> = '
                    '2<i>x</i>. <strong><i>x</i><sup>2</sup> + 6<i>x</i> − 8</strong> '
                    '— oʻrta aʼzolarni qoʻshishda ishorani hisobga olmagan javob.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>If 2(<i>x</i> + 5) = 26, what is the value of <i>x</i>?</p>',
     'choices': ['3', '8', '13', '16'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Ikki tomonni 2 ga boʻlamiz: '
                    '<i>x</i> + 5 = 13, demak <i>x</i> = 8. <strong>13</strong> — '
                    '<i>x</i> + 5 ning qiymati: oxirgi qadam qolib ketgan.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>What is the median of the data set 4, 7, 9, 12, 15?</p>',
     'choices': ['7', '9', '9.4', '12'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Sonlar allaqachon oʻsib boradi va '
                    'ularning soni beshta, demak mediana — uchinchisi, yaʼni 9. '
                    '<strong>9.4</strong> — oʻrta arifmetik (47 ÷ 5): mediana oʻrtadagi '
                    '<em>son</em>, oʻrtacha qiymat emas.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If 2<sup><i>x</i></sup> = 32, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['4', '5', '6', '16'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. 2 × 2 × 2 × 2 × 2 = 32, demak '
                    '32 = 2<sup>5</sup> va <i>x</i> = 5. <strong>16</strong> — 32 ÷ 2 '
                    'ning natijasi: daraja koʻrsatkichi boʻlish bilan topilmaydi.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A taxi charges a flat fee of $4 plus $2 for each mile '
                      'travelled. What is the total charge for a 9-mile ride?</p>',
     'choices': ['$13', '$18', '$22', '$54'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>$22</strong>. Masofa uchun 2 × 9 = $18, ustiga '
                    'bir martalik $4: 18 + 4 = $22. <strong>$54</strong> — (4 + 2) × 9, '
                    'yaʼni bir martalik toʻlovni ham har milga qoʻshib yuborgan javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>Two angles are supplementary. If one of the angles measures '
                      '115°, what is the measure of the other angle?</p>',
     'choices': ['25°', '65°', '75°', '245°'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>65°</strong>. Qoʻshni (supplementary) '
                    'burchaklar yigʻindisi 180°, demak 180 − 115 = 65°. '
                    '<strong>25°</strong> — 90 − 115 emas, balki komplementar '
                    'burchak bilan aralashtirish natijasi: 90° emas, 180°.'},

    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>The functions <i>f</i> and <i>g</i> are defined by '
                      '<i>f</i>(<i>x</i>) = 2<i>x</i> + 1 and <i>g</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup>. What is the value of '
                      '<i>f</i>(<i>g</i>(3))?</p>',
     'choices': ['7', '13', '19', '49'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>19</strong>. Ichkaridan boshlaymiz: '
                    '<i>g</i>(3) = 3<sup>2</sup> = 9, keyin <i>f</i>(9) = 2 × 9 + 1 = 19. '
                    '<strong>49</strong> — tartibni teskari olgan javob: '
                    '<i>g</i>(<i>f</i>(3)) = <i>g</i>(7) = 49.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i> ÷ 4 = 7, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['28'],
     'explanation': 'Toʻgʻri javob <strong>28</strong>. Ikki tomonni 4 ga koʻpaytiramiz: '
                    '<i>x</i> = 7 × 4 = 28. Tekshirish: 28 ÷ 4 = 7.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>A bag contains 5 red marbles and 15 blue marbles and no '
                      'others. What fraction of the marbles in the bag are red?</p>'
                      + GRID_NOTE,
     'accepted': ['1/4', '0.25', '5/20'],
     'explanation': 'Toʻgʻri javob <strong>1/4</strong> (0.25 ham qabul qilinadi). '
                    'Jami 5 + 15 = 20 ta, qizillari 5 ta, demak 5/20 = 1/4. Eng keng '
                    'tarqalgan xato — 5/15 yozish: maxraj <em>jami</em> son boʻlishi kerak, '
                    'boshqa rang emas.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>2</sup> = 49 and <i>x</i> &lt; 0, what is the '
                      'value of <i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['-7'],
     'explanation': 'Toʻgʻri javob <strong>−7</strong>. 49 ning ikkita kvadrat ildizi '
                    'bor: 7 va −7; <i>x</i> &lt; 0 sharti manfiysini tanlaydi. Minus '
                    'ishorasi ham javob qutichasiga yoziladi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 6<i>x</i> + 4 = 40, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['6'],
     'explanation': 'Toʻgʻri javob <strong>6</strong>. 4 ni ayiramiz: 6<i>x</i> = 36, '
                    'soʻng 6 ga boʻlamiz: <i>x</i> = 6. Tekshirish: 6 × 6 + 4 = 40.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '5<i>x</i> − 3. If <i>f</i>(<i>a</i>) = 22, what is the value '
                      'of <i>a</i>?</p>' + GRID_NOTE,
     'accepted': ['5'],
     'explanation': 'Toʻgʻri javob <strong>5</strong>. 5<i>a</i> − 3 = 22 dan '
                    '5<i>a</i> = 25, demak <i>a</i> = 5. Tekshirish: 5 × 5 − 3 = 22.'},
]
