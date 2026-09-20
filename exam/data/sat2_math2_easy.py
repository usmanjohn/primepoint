# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 2 · Math, Module 2 (LOWER)
#  22 questions · 35 minutes · taken by a pupil who scored under 14 on math1.
#  Questions 18–22 are student-produced responses (grid-ins).
#
#  Load: python manage.py load_mock exam/data/sat2_math2_easy.py --expect-questions=22
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §3
# ──────────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'Digital SAT — PrimePoint Mock 2',
    'language': 'english',
    'exam_format': 'sat',
    'exam_number': 202,
    'is_published': True,
}

# Copied unchanged into all six files of mock 2.
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
     'question_text': '<p>If <i>x</i> − 6 = −2, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['−8', '−4', '4', '8'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Ikki tomonga 6 ni qoʻshamiz: '
                    '<i>x</i> = −2 + 6 = 4. Tekshirish: 4 − 6 = −2. '
                    '<strong>−8</strong> — qoʻshish oʻrniga ayirgan javob.'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>A class contains 18 boys and 12 girls and no other students. What '
                      'fraction of the class are girls?</p>',
     'choices': ['1/3', '2/5', '1/2', '3/5'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>2/5</strong>. Jami 18 + 12 = 30 oʻquvchi, '
                    'qizlar 12 ta, demak 12/30 = 2/5. <strong>1/3</strong> — '
                    '12/18 dan chiqadi: maxraj <em>jami</em> son boʻlishi kerak, boshqa '
                    'guruh emas.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 3<i>x</i> + 4 = 19, what is the value of <i>x</i>?</p>',
     'choices': ['3', '5', '7', '15'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. 4 ni ayiramiz: 3<i>x</i> = 15, '
                    'soʻng 3 ga boʻlamiz: <i>x</i> = 5. <strong>15</strong> — '
                    '3<i>x</i> ning qiymati, yaʼni oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>h</i> is defined by <i>h</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> − 3. What is the value of '
                      '<i>h</i>(4)?</p>',
     'choices': ['5', '13', '16', '19'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>13</strong>. 4<sup>2</sup> = 16, keyin '
                    '16 − 3 = 13. <strong>5</strong> — kvadratni koʻpaytirish '
                    'deb tushunib, 4 × 2 − 3 = 5 hisoblagan javob: '
                    '<i>x</i><sup>2</sup> = <i>x</i> × <i>x</i>.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>A rectangle has an area of 48 square units and a width of 6 '
                      'units. What is its length?</p>',
     'choices': ['6', '8', '42', '288'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Yuza = uzunlik × eni, demak uzunlik '
                    '= 48 ÷ 6 = 8. <strong>42</strong> — 48 − 6: yuza koʻpaytma '
                    'orqali topiladi, ayirma orqali emas.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>The value of <i>y</i> is 5 less than three times the value of '
                      '<i>x</i>. Which equation represents this relationship?</p>',
     'choices': [
         '<i>y</i> = 3(<i>x</i> − 5)',
         '<i>y</i> = 3<i>x</i> − 5',
         '<i>y</i> = 5 − 3<i>x</i>',
         '<i>y</i> = 5<i>x</i> − 3',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>y</i> = 3<i>x</i> − 5</strong>. "Three '
                    'times <i>x</i>" — 3<i>x</i>, "5 less than" esa undan 5 ni '
                    'ayirish. <strong><i>y</i> = 5 − 3<i>x</i></strong> ayirishni '
                    'teskari yoʻnalishda qiladi — "5 less than A" A − 5 degani, '
                    '5 − A emas.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>What is 15% of 60?</p>',
     'choices': ['4', '9', '45', '51'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. 60 × 0.15 = 9. Yoki: 10% = 6 va '
                    '5% = 3, demak 15% = 9. <strong>51</strong> — 60 dan 15% '
                    '<em>ayirilgan</em> qiymat: savol qismni soʻraydi, qoldiqni emas.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>If <i>x</i><sup>3</sup> = 27, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['3', '9', '24', '81'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. 3 × 3 × 3 = 27. <strong>9</strong> '
                    '— 27 ÷ 3 ning natijasi: kub ildiz olish uchga boʻlish emas.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>In the equation 2<i>x</i> + 5<i>y</i> = 24, if <i>x</i> = 2, what '
                      'is the value of <i>y</i>?</p>',
     'choices': ['2', '4', '5', '10'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. <i>x</i> = 2 ni qoʻyamiz: '
                    '4 + 5<i>y</i> = 24, demak 5<i>y</i> = 20 va <i>y</i> = 4. '
                    '<strong>5</strong> — 24 ÷ 5 ni yaxlitlagan javob: avval '
                    '2<i>x</i> ni ayirish kerak.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A circle has a diameter of 14 units. What is its '
                      'circumference?</p>',
     'choices': ['7π', '14π', '49π', '196π'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>14π</strong>. Aylana uzunligi — '
                    'π × diametr = 14π. (Yoki 2π<i>r</i>, bunda '
                    '<i>r</i> = 7.) <strong>49π</strong> — yuza: '
                    'π<i>r</i><sup>2</sup> boshqa formula.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>Which expression is equivalent to (<i>x</i> + 3)(<i>x</i> + '
                      '5)?</p>',
     'choices': [
         '<i>x</i><sup>2</sup> + 8<i>x</i> + 15',
         '<i>x</i><sup>2</sup> + 15<i>x</i> + 8',
         '<i>x</i><sup>2</sup> + 15',
         '<i>x</i><sup>2</sup> + 8<i>x</i> + 8',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong><i>x</i><sup>2</sup> + 8<i>x</i> + 15</strong>. '
                    'Har bir aʼzoni koʻpaytiramiz: <i>x</i>·<i>x</i> = '
                    '<i>x</i><sup>2</sup>, 5<i>x</i> + 3<i>x</i> = 8<i>x</i>, va '
                    '3 × 5 = 15. <strong><i>x</i><sup>2</sup> + 15</strong> oʻrtadagi ikki '
                    'aʼzoni butunlay tashlab ketadi — qavslarni alohida-alohida '
                    'kvadratga koʻtargan javob.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>If 3(<i>x</i> − 4) = 18, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['6', '10', '14', '22'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>10</strong>. Ikki tomonni 3 ga boʻlamiz: '
                    '<i>x</i> − 4 = 6, demak <i>x</i> = 10. <strong>6</strong> — '
                    '<i>x</i> − 4 ning qiymati: oxirgi qadam qolib ketgan.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>What is the mode of the data set 3, 7, 7, 9, 12, 7, 5?</p>',
     'choices': ['5', '6', '7', '9'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. Moda — eng koʻp takrorlangan '
                    'son, va 7 uch marta uchraydi, qolganlari bir martadan. '
                    '<strong>9</strong> — tartiblangan qatorning oʻrtasidagi son, '
                    'yaʼni mediana: moda bilan medianani adashtirmang.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If 10<sup><i>x</i></sup> = 10,000, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['3', '4', '100', '1,000'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. 10,000 da noldan keyin toʻrtta nol '
                    'bor: 10 × 10 × 10 × 10 = 10,000 = 10<sup>4</sup>. '
                    '<strong>1,000</strong> — 10,000 ÷ 10: daraja koʻrsatkichi '
                    'boʻlish bilan topilmaydi.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A bus fare is $2.00 plus $0.50 for each stop travelled. What is '
                      'the fare for a journey of 12 stops?</p>',
     'choices': ['$6.00', '$8.00', '$14.00', '$26.00'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>$8.00</strong>. Bekatlar uchun 0.50 × 12 = '
                    '$6.00, ustiga bir martalik $2.00: 6 + 2 = $8.00. '
                    '<strong>$6.00</strong> — faqat bekatlar qismi: bir martalik '
                    'toʻlovni qoʻshishni unutgan javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>Two angles are complementary. If one of them measures '
                      '37°, what is the measure of the other?</p>',
     'choices': ['53°', '63°', '143°', '323°'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>53°</strong>. Komplementar burchaklar '
                    'yigʻindisi 90°, demak 90 − 37 = 53°. '
                    '<strong>143°</strong> — 180 − 37: u qoʻshni '
                    '(supplementary) burchaklarga tegishli, komplementarga emas.'},

    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>The functions <i>f</i> and <i>g</i> are defined by '
                      '<i>f</i>(<i>x</i>) = <i>x</i> + 4 and <i>g</i>(<i>x</i>) = '
                      '2<i>x</i>. What is the value of <i>g</i>(<i>f</i>(1))?</p>',
     'choices': ['6', '10', '12', '14'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>10</strong>. Ichkaridan boshlaymiz: '
                    '<i>f</i>(1) = 1 + 4 = 5, keyin <i>g</i>(5) = 2 × 5 = 10. '
                    '<strong>6</strong> — tartibni teskari olgan javob: '
                    '<i>f</i>(<i>g</i>(1)) = <i>f</i>(2) = 6.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i> ÷ 3 = 9, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['27'],
     'explanation': 'Toʻgʻri javob <strong>27</strong>. Ikki tomonni 3 ga koʻpaytiramiz: '
                    '<i>x</i> = 9 × 3 = 27. Tekshirish: 27 ÷ 3 = 9.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>A jar contains 8 red marbles and 12 green marbles and no others. '
                      'What fraction of the marbles in the jar are red?</p>' + GRID_NOTE,
     'accepted': ['2/5', '0.4', '8/20'],
     'explanation': 'Toʻgʻri javob <strong>2/5</strong> (0.4 ham qabul qilinadi). Jami '
                    '8 + 12 = 20 ta, qizillari 8 ta, demak 8/20 = 2/5. Eng keng tarqalgan '
                    'xato — 8/12 yozish: maxraj <em>jami</em> son boʻlishi kerak.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>2</sup> = 36 and <i>x</i> &gt; 0, what is the '
                      'value of <i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['6'],
     'explanation': 'Toʻgʻri javob <strong>6</strong>. 36 ning ikkita kvadrat ildizi bor: '
                    '6 va −6; <i>x</i> &gt; 0 sharti musbatini tanlaydi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 5<i>x</i> − 7 = 33, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['8'],
     'explanation': 'Toʻgʻri javob <strong>8</strong>. 7 ni qoʻshamiz: 5<i>x</i> = 40, '
                    'soʻng 5 ga boʻlamiz: <i>x</i> = 8. Tekshirish: 5 × 8 − 7 = 33.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '4<i>x</i> + 2. If <i>f</i>(<i>a</i>) = 30, what is the value of '
                      '<i>a</i>?</p>' + GRID_NOTE,
     'accepted': ['7'],
     'explanation': 'Toʻgʻri javob <strong>7</strong>. 4<i>a</i> + 2 = 30 dan '
                    '4<i>a</i> = 28, demak <i>a</i> = 7. Tekshirish: 4 × 7 + 2 = 30.'},
]
