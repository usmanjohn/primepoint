# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 4 · Math, Module 2 (LOWER)
#  22 questions · 35 minutes · taken by a pupil who scored under 14 on math1.
#  Questions 18–22 are student-produced responses (grid-ins).

#
#  Load: python manage.py load_mock exam/data/sat4_math2_easy.py --expect-questions=22
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

S = 'math2e'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If <i>x</i> + 12 = 5, what is the value of <i>x</i>?</p>',
     'choices': ['−17', '−7', '7', '17'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>−7</strong>. Ikki tomondan 12 ni ayiramiz: '
                    '<i>x</i> = 5 − 12 = −7. Tekshirish: −7 + 12 = 5. '
                    '<strong>17</strong> — ayirish oʻrniga qoʻshgan javob.'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>Of the 40 students in a class, 14 cycle to school. What percent '
                      'of the class cycles to school?</p>',
     'choices': ['14%', '26%', '35%', '65%'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>35%</strong>. 14 ÷ 40 = 0.35, yaʼni 35%. '
                    '<strong>65%</strong> — velosipedda kelmaydiganlar ulushi: savol '
                    'kelganlarni soʻraydi.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 5<i>x</i> + 6 = 41, what is the value of <i>x</i>?</p>',
     'choices': ['7', '9', '35', '47'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. 6 ni ayiramiz: 5<i>x</i> = 35, '
                    'soʻng 5 ga boʻlamiz: <i>x</i> = 7. <strong>35</strong> — '
                    '5<i>x</i> ning qiymati: oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>m</i> is defined by <i>m</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> + 5. What is the value of <i>m</i>(6)?</p>',
     'choices': ['17', '23', '41', '65'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>41</strong>. 6<sup>2</sup> = 36, keyin '
                    '36 + 5 = 41. <strong>17</strong> — kvadratni koʻpaytirish deb '
                    'tushunib, 6 × 2 + 5 = 17 hisoblagan javob.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>A square has sides of length 7 units. What is its area?</p>',
     'choices': ['14', '28', '49', '343'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>49</strong>. Kvadratning yuzasi tomonning '
                    'kvadrati: 7<sup>2</sup> = 49. <strong>28</strong> — perimetr '
                    '(4 × 7): yuza bilan perimetrni adashtirmang.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>The value of <i>y</i> is 6 less than four times the value of '
                      '<i>x</i>. Which equation represents this relationship?</p>',
     'choices': [
         '<i>y</i> = 4(<i>x</i> − 6)',
         '<i>y</i> = 4<i>x</i> − 6',
         '<i>y</i> = 6 − 4<i>x</i>',
         '<i>y</i> = 6<i>x</i> − 4',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>y</i> = 4<i>x</i> − 6</strong>. "Four '
                    'times <i>x</i>" — 4<i>x</i>, "6 less than" esa undan 6 ni '
                    'ayirish. <strong><i>y</i> = 6 − 4<i>x</i></strong> ayirishni '
                    'teskari yoʻnalishda qiladi: "6 less than A" A − 6 degani.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>What is 40% of 95?</p>',
     'choices': ['22', '38', '55', '57'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>38</strong>. 95 × 0.4 = 38. Yoki: 10% = 9.5, '
                    'demak 40% = 38. <strong>57</strong> — 95 dan 40% '
                    '<em>ayirilgan</em> qoldiq.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>If <i>x</i><sup>2</sup> = 100 and <i>x</i> &gt; 0, what is the '
                      'value of <i>x</i>?</p>',
     'choices': ['10', '20', '50', '200'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>10</strong>. 10 × 10 = 100, va shart '
                    '<i>x</i> &gt; 0 ikkinchi ildiz −10 ni chiqarib tashlaydi. '
                    '<strong>50</strong> — 100 ÷ 2: kvadrat ildiz olish ikkiga '
                    'boʻlish emas.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>In the equation 5<i>x</i> + 2<i>y</i> = 38, if <i>x</i> = 4, what '
                      'is the value of <i>y</i>?</p>',
     'choices': ['4', '6', '9', '18'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. <i>x</i> = 4 ni qoʻyamiz: '
                    '20 + 2<i>y</i> = 38, demak 2<i>y</i> = 18 va <i>y</i> = 9. '
                    '<strong>18</strong> — 2<i>y</i> ning qiymati: oxirgi boʻlish '
                    'qolib ketgan.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A triangle has a base of 12 units and a height of 5 units. What '
                      'is its area?</p>',
     'choices': ['17', '30', '34', '60'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>30</strong>. Uchburchak yuzasi — '
                    '½ × asos × balandlik = ½ × 12 × 5 = 30. <strong>60</strong> — '
                    '12 × 5 ning oʻzi: ikkiga boʻlishni unutgan javob.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>Which expression is equivalent to (<i>x</i> + 7)(<i>x</i> '
                      '− 3)?</p>',
     'choices': [
         '<i>x</i><sup>2</sup> − 4<i>x</i> − 21',
         '<i>x</i><sup>2</sup> + 4<i>x</i> − 21',
         '<i>x</i><sup>2</sup> + 4<i>x</i> + 21',
         '<i>x</i><sup>2</sup> + 10<i>x</i> − 21',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>x</i><sup>2</sup> + 4<i>x</i> − 21'
                    '</strong>. Har bir aʼzoni koʻpaytiramiz: 7<i>x</i> − 3<i>x</i> = '
                    '4<i>x</i>, va 7 × (−3) = −21. <strong><i>x</i><sup>2</sup> '
                    '+ 10<i>x</i> − 21</strong> — oʻrtadagi aʼzolarni ayirish '
                    'oʻrniga qoʻshgan javob.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>If 4(<i>x</i> − 3) = 28, what is the value of <i>x</i>?</p>',
     'choices': ['7', '10', '16', '31'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>10</strong>. Ikki tomonni 4 ga boʻlamiz: '
                    '<i>x</i> − 3 = 7, demak <i>x</i> = 10. <strong>7</strong> '
                    '— <i>x</i> − 3 ning qiymati: oxirgi qadam qolib ketgan.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>What is the mean of the data set 6, 9, 13, 16?</p>',
     'choices': ['9', '11', '12', '13'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>11</strong>. Yigʻindi 6 + 9 + 13 + 16 = 44, '
                    'sonlar soni 4, demak 44 ÷ 4 = 11. <strong>11</strong> ni topgach '
                    'tekshiring: ikkitasi undan kichik, ikkitasi katta — oʻrtacha '
                    'qatorning ichida boʻlishi kerak.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If 2<sup><i>x</i></sup> = 64, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['6', '8', '32', '128'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. 2 ni oltita koʻpaytiramiz: '
                    '2·4·8·16·32·64 — demak 64 = 2<sup>6</sup>. '
                    '<strong>32</strong> — 64 ÷ 2: daraja koʻrsatkichi boʻlish bilan '
                    'topilmaydi.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A plumber charges a call-out fee of $40 plus $25 for each hour of '
                      'work. What is the total charge for a job that takes 3 hours?</p>',
     'choices': ['$75', '$105', '$115', '$195'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>$115</strong>. Ish uchun 25 × 3 = $75, ustiga '
                    'bir martalik $40: 75 + 40 = $115. <strong>$195</strong> — '
                    '(40 + 25) × 3, yaʼni chaqiruv haqini ham har soatga qoʻshib yuborgan '
                    'javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>Two angles are supplementary. If one of them measures '
                      '128°, what is the measure of the other?</p>',
     'choices': ['38°', '52°', '62°', '232°'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>52°</strong>. Qoʻshni (supplementary) '
                    'burchaklar yigʻindisi 180°, demak 180 − 128 = 52°. '
                    '<strong>38°</strong> — 90 dan ayirgan javob: u '
                    'komplementar burchaklarga tegishli.'},

    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>The functions <i>f</i> and <i>g</i> are defined by '
                      '<i>f</i>(<i>x</i>) = <i>x</i> − 6 and <i>g</i>(<i>x</i>) = '
                      '4<i>x</i>. What is the value of <i>f</i>(<i>g</i>(2))?</p>',
     'choices': ['2', '8', '14', '32'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. Ichkaridan boshlaymiz: '
                    '<i>g</i>(2) = 4 × 2 = 8, keyin <i>f</i>(8) = 8 − 6 = 2. '
                    '<strong>32</strong> — <i>g</i> ni ikki marta qoʻllagan javob: '
                    '<i>g</i>(<i>g</i>(2)) = <i>g</i>(8) = 32. Tashqi funksiya '
                    'qaysi ekanini qavslardan oʻqing.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i> ÷ 7 = 6, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['42'],
     'explanation': 'Toʻgʻri javob <strong>42</strong>. Ikki tomonni 7 ga koʻpaytiramiz: '
                    '<i>x</i> = 6 × 7 = 42. Tekshirish: 42 ÷ 7 = 6.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>A bag contains 9 white counters and 6 black counters and no '
                      'others. What fraction of the counters in the bag are white?</p>'
                      + GRID_NOTE,
     'accepted': ['3/5', '0.6', '9/15'],
     'explanation': 'Toʻgʻri javob <strong>3/5</strong> (0.6 ham qabul qilinadi). Jami '
                    '9 + 6 = 15 ta, oqlari 9 ta, demak 9/15 = 3/5. Eng keng tarqalgan '
                    'xato — 9/6 yozish: maxraj <em>jami</em> son boʻlishi kerak.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>2</sup> = 121 and <i>x</i> &gt; 0, what is the '
                      'value of <i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['11'],
     'explanation': 'Toʻgʻri javob <strong>11</strong>. 11 × 11 = 121, va shart '
                    '<i>x</i> &gt; 0 manfiy ildizni chiqarib tashlaydi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 9<i>x</i> − 8 = 46, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['6'],
     'explanation': 'Toʻgʻri javob <strong>6</strong>. 8 ni qoʻshamiz: 9<i>x</i> = 54, '
                    'soʻng 9 ga boʻlamiz: <i>x</i> = 6. Tekshirish: 9 × 6 − 8 = 46.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '7<i>x</i> + 3. If <i>f</i>(<i>a</i>) = 52, what is the value of '
                      '<i>a</i>?</p>' + GRID_NOTE,
     'accepted': ['7'],
     'explanation': 'Toʻgʻri javob <strong>7</strong>. 7<i>a</i> + 3 = 52 dan '
                    '7<i>a</i> = 49, demak <i>a</i> = 7. Tekshirish: 7 × 7 + 3 = 52.'},
]
