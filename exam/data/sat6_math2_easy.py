# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 6 · Math, Module 2 (LOWER)
#  22 questions · 35 minutes · taken by a pupil who scored under 14 on math1.
#  Questions 18–22 are student-produced responses (grid-ins).

#
#  Load: python manage.py load_mock exam/data/sat6_math2_easy.py --expect-questions=22
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

S = 'math2e'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If <i>x</i> − 13 = −4, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['−17', '−9', '9', '17'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Ikki tomonga 13 ni qoʻshamiz: '
                    '<i>x</i> = −4 + 13 = 9. Tekshirish: 9 − 13 = −4. '
                    '<strong>−17</strong> — qoʻshish oʻrniga ayirgan javob.'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>Of the 50 questions on a test, a student answered 42 correctly. '
                      'What percent did the student answer correctly?</p>',
     'choices': ['8%', '16%', '42%', '84%'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>84%</strong>. 42 ÷ 50 = 0.84, yaʼni 84%. '
                    '<strong>16%</strong> — xato javoblar ulushi (8/50): savol '
                    'toʻgʻrilarini soʻraydi.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 7<i>x</i> + 8 = 64, what is the value of <i>x</i>?</p>',
     'choices': ['8', '9', '56', '72'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. 8 ni ayiramiz: 7<i>x</i> = 56, '
                    'soʻng 7 ga boʻlamiz: <i>x</i> = 8. <strong>56</strong> — '
                    '7<i>x</i> ning qiymati: oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>p</i> is defined by <i>p</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> − 8. What is the value of '
                      '<i>p</i>(7)?</p>',
     'choices': ['6', '41', '49', '57'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>41</strong>. 7<sup>2</sup> = 49, keyin '
                    '49 − 8 = 41. <strong>6</strong> — kvadratni koʻpaytirish '
                    'deb tushunib, 7 × 2 − 8 = 6 hisoblagan javob.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>A square has a perimeter of 48 units. What is the length of one '
                      'of its sides?</p>',
     'choices': ['12', '24', '144', '192'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>12</strong>. Kvadratning toʻrt tomoni teng, '
                    'demak tomon 48 ÷ 4 = 12. <strong>24</strong> — perimetrni 2 ga '
                    'boʻlgan javob: kvadratda toʻrt tomon bor.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>The value of <i>y</i> is 9 less than five times the value of '
                      '<i>x</i>. Which equation represents this relationship?</p>',
     'choices': [
         '<i>y</i> = 5(<i>x</i> − 9)',
         '<i>y</i> = 5<i>x</i> − 9',
         '<i>y</i> = 9 − 5<i>x</i>',
         '<i>y</i> = 9<i>x</i> − 5',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>y</i> = 5<i>x</i> − 9</strong>. "Five '
                    'times <i>x</i>" — 5<i>x</i>, "9 less than" esa undan 9 ni '
                    'ayirish. <strong><i>y</i> = 9 − 5<i>x</i></strong> ayirishni '
                    'teskari yoʻnalishda qiladi: "9 less than A" A − 9 degani.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>What is 35% of 80?</p>',
     'choices': ['24', '28', '45', '52'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>28</strong>. 80 × 0.35 = 28. Yoki: 10% = 8, '
                    'demak 30% = 24; 5% = 4; 24 + 4 = 28. <strong>52</strong> — '
                    'qolgan 65%.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>If <i>x</i><sup>2</sup> = 169 and <i>x</i> &gt; 0, what is the '
                      'value of <i>x</i>?</p>',
     'choices': ['13', '26', '84.5', '338'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>13</strong>. 13 × 13 = 169, va shart '
                    '<i>x</i> &gt; 0 ikkinchi ildiz −13 ni chiqarib tashlaydi. '
                    '<strong>84.5</strong> — 169 ÷ 2: kvadrat ildiz olish ikkiga '
                    'boʻlish emas.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>In the equation 6<i>x</i> + 4<i>y</i> = 46, if <i>x</i> = 3, what '
                      'is the value of <i>y</i>?</p>',
     'choices': ['4', '7', '10', '28'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. <i>x</i> = 3 ni qoʻyamiz: '
                    '18 + 4<i>y</i> = 46, demak 4<i>y</i> = 28 va <i>y</i> = 7. '
                    '<strong>28</strong> — 4<i>y</i> ning qiymati: oxirgi boʻlish '
                    'qolib ketgan.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A triangle has a base of 16 units and a height of 7 units. What '
                      'is its area?</p>',
     'choices': ['23', '46', '56', '112'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>56</strong>. Uchburchak yuzasi — '
                    '½ × asos × balandlik = ½ × 16 × 7 = 56. <strong>112</strong> — '
                    '16 × 7 ning oʻzi: ikkiga boʻlishni unutgan javob.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>Which expression is equivalent to (<i>x</i> + 8)(<i>x</i> '
                      '− 4)?</p>',
     'choices': [
         '<i>x</i><sup>2</sup> − 4<i>x</i> − 32',
         '<i>x</i><sup>2</sup> + 4<i>x</i> − 32',
         '<i>x</i><sup>2</sup> + 4<i>x</i> + 32',
         '<i>x</i><sup>2</sup> + 12<i>x</i> − 32',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>x</i><sup>2</sup> + 4<i>x</i> − 32'
                    '</strong>. Har bir aʼzoni koʻpaytiramiz: 8<i>x</i> − 4<i>x</i> = '
                    '4<i>x</i>, va 8 × (−4) = −32. '
                    '<strong><i>x</i><sup>2</sup> + 12<i>x</i> − 32</strong> — '
                    'oʻrtadagi aʼzolarni ayirish oʻrniga qoʻshgan javob.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>If 6(<i>x</i> − 5) = 42, what is the value of <i>x</i>?</p>',
     'choices': ['7', '12', '37', '47'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>12</strong>. Ikki tomonni 6 ga boʻlamiz: '
                    '<i>x</i> − 5 = 7, demak <i>x</i> = 12. <strong>7</strong> '
                    '— <i>x</i> − 5 ning qiymati: oxirgi qadam qolib ketgan.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>What is the mode of the data set 4, 6, 6, 9, 11, 6, 13?</p>',
     'choices': ['4', '6', '9', '11'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Moda — eng koʻp takrorlangan '
                    'son, va 6 uch marta uchraydi, qolganlari bir martadan. '
                    '<strong>9</strong> — tartiblangan qatorning oʻrtasidagi son, '
                    'yaʼni mediana: moda bilan medianani adashtirmang.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If 5<sup><i>x</i></sup> = 25, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['2', '5', '20', '125'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. 5 × 5 = 25, demak 25 = '
                    '5<sup>2</sup>. <strong>5</strong> — 25 ÷ 5: daraja koʻrsatkichi '
                    'boʻlish bilan topilmaydi.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A courier charges a flat fee of $8 plus $3 for each package '
                      'delivered. What is the total charge for delivering 9 packages?</p>',
     'choices': ['$27', '$35', '$72', '$99'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>$35</strong>. Paketlar uchun 3 × 9 = $27, '
                    'ustiga bir martalik $8: 27 + 8 = $35. <strong>$99</strong> — '
                    '(8 + 3) × 9, yaʼni bir martalik toʻlovni ham har paketga qoʻshib '
                    'yuborgan javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>Two angles are complementary. If one of them measures '
                      '24°, what is the measure of the other?</p>',
     'choices': ['56°', '66°', '156°', '336°'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>66°</strong>. Komplementar burchaklar '
                    'yigʻindisi 90°, demak 90 − 24 = 66°. '
                    '<strong>156°</strong> — 180 − 24: u qoʻshni '
                    '(supplementary) burchaklarga tegishli.'},

    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>The functions <i>f</i> and <i>g</i> are defined by '
                      '<i>f</i>(<i>x</i>) = <i>x</i> + 7 and <i>g</i>(<i>x</i>) = '
                      '5<i>x</i>. What is the value of <i>f</i>(<i>g</i>(2))?</p>',
     'choices': ['17', '19', '45', '70'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>17</strong>. Ichkaridan boshlaymiz: '
                    '<i>g</i>(2) = 5 × 2 = 10, keyin <i>f</i>(10) = 10 + 7 = 17. '
                    '<strong>45</strong> — tartibni teskari olgan javob: '
                    '<i>g</i>(<i>f</i>(2)) = <i>g</i>(9) = 45.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i> ÷ 8 = 7, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['56'],
     'explanation': 'Toʻgʻri javob <strong>56</strong>. Ikki tomonni 8 ga koʻpaytiramiz: '
                    '<i>x</i> = 7 × 8 = 56. Tekshirish: 56 ÷ 8 = 7.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>A shelf holds 5 novels and 15 textbooks and no other books. What '
                      'fraction of the books on the shelf are novels?</p>' + GRID_NOTE,
     'accepted': ['1/4', '0.25', '5/20'],
     'explanation': 'Toʻgʻri javob <strong>1/4</strong> (0.25 ham qabul qilinadi). Jami '
                    '5 + 15 = 20 ta, romanlar 5 ta, demak 5/20 = 1/4. Eng keng tarqalgan '
                    'xato — 5/15 yozish: maxraj <em>jami</em> son boʻlishi kerak.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>3</sup> = 216, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['6'],
     'explanation': 'Toʻgʻri javob <strong>6</strong>. 6 × 6 × 6 = 216. Kub ildizda son '
                    'uch marta koʻpaytiriladi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 4<i>x</i> − 9 = 31, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['10'],
     'explanation': 'Toʻgʻri javob <strong>10</strong>. 9 ni qoʻshamiz: 4<i>x</i> = 40, '
                    'soʻng 4 ga boʻlamiz: <i>x</i> = 10. Tekshirish: 4 × 10 − 9 = '
                    '31.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '8<i>x</i> + 6. If <i>f</i>(<i>a</i>) = 62, what is the value of '
                      '<i>a</i>?</p>' + GRID_NOTE,
     'accepted': ['7'],
     'explanation': 'Toʻgʻri javob <strong>7</strong>. 8<i>a</i> + 6 = 62 dan '
                    '8<i>a</i> = 56, demak <i>a</i> = 7. Tekshirish: 8 × 7 + 6 = 62.'},
]
