# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 2 · Math, Module 1
#  22 questions · 35 minutes · every taker sits this one.
#  Questions 18–22 are student-produced responses (grid-ins).
#
#  Route: 14 or more correct here sends the taker to the UPPER module 2.
#
#  Maths is HTML, never LaTeX; figures are inline SVG carrying their own
#  colours through currentColor (the exam page loads no pm-*/ps-* CSS).
#
#  Load: python manage.py load_mock exam/data/sat2_math1.py --expect-questions=22
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §2
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

S = 'math1'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 5<i>x</i> − 8 = 27, what is the value of <i>x</i>?</p>',
     'choices': ['5', '7', '9', '11'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. Ikki tomonga 8 ni qoʻshamiz: '
                    '5<i>x</i> = 35, soʻng 5 ga boʻlamiz: <i>x</i> = 7. Tekshirish: '
                    '5 × 7 − 8 = 27.'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>A shirt costs $35.00. A sales tax of 8% is added at the till. '
                      'What is the total amount paid?</p>',
     'choices': ['$2.80', '$35.08', '$37.80', '$43.00'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>$37.80</strong>. Soliq 35 × 0.08 = $2.80, '
                    'jami esa 35 + 2.80 = $37.80. Yoki bir qadamda: 35 × 1.08 = 37.80. '
                    '<strong>$2.80</strong> — soliqning oʻzi: savol jamini soʻraydi.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>A line passes through the points (2, −3) and (8, 9) in the '
                      '<i>xy</i>-plane. What is the slope of the line?</p>',
     'choices': ['1/2', '2', '3', '6'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. Burchak koeffitsiyenti — '
                    '(9 − (−3)) ÷ (8 − 2) = 12 ÷ 6 = 2. Ayirmada ikkita '
                    'minus qoʻshiluvga aylanishini unutmang: 9 + 3 = 12. '
                    '<strong>1/2</strong> — ayirmalarni teskari boʻlgan javob.'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>g</i> is defined by <i>g</i>(<i>x</i>) = '
                      '3<i>x</i><sup>2</sup> + 1. What is the value of '
                      '<i>g</i>(−2)?</p>',
     'choices': ['−11', '11', '13', '37'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>13</strong>. (−2)<sup>2</sup> = 4, chunki '
                    'manfiy sonning kvadrati musbat; keyin 3 × 4 + 1 = 13. '
                    '<strong>−11</strong> — kvadratni (−2)<sup>2</sup> = '
                    '−4 deb olgan javob va bu yerdagi eng keng tarqalgan xato.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>A triangle has a base of 14 units and a height of 9 units. What '
                      'is the area of the triangle?</p>',
     'choices': ['23', '63', '126', '252'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>63</strong>. Uchburchak yuzasi — '
                    '½ × asos × balandlik = ½ × 14 × 9 = 63. <strong>126</strong> — '
                    '14 × 9 ning oʻzi, yaʼni ikkiga boʻlishni unutgan javob.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p><i>x</i> + <i>y</i> = 10<br><i>x</i> − <i>y</i> = 4</p>'
                      '<p>The system of equations above has a unique solution. What is the '
                      'value of <i>y</i>?</p>',
     'choices': ['3', '4', '6', '7'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Ikki tenglamani ayiramiz: '
                    '2<i>y</i> = 6, demak <i>y</i> = 3. <strong>7</strong> — '
                    '<i>x</i> ning qiymati: sistemada qaysi nomaʼlum soʻralganini oxirida '
                    'yana bir bor tekshiring.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>A recipe for 6 servings uses 480 grams of rice. At the same '
                      'rate, how many grams of rice are needed for 15 servings?</p>',
     'choices': ['600', '960', '1,200', '1,440'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>1,200</strong>. Bir porsiyaga 480 ÷ 6 = 80 g '
                    'ketadi, demak 15 porsiyaga 80 × 15 = 1,200 g. Yoki proportsiya bilan: '
                    '480/6 = <i>x</i>/15.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>What is the positive solution to the equation '
                      '<i>x</i><sup>2</sup> + 5<i>x</i> − 24 = 0?</p>',
     'choices': ['−8', '−3', '3', '8'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Koʻpaytmasi −24, yigʻindisi 5 '
                    'boʻlgan ikki son — 8 va −3, demak (<i>x</i> + 8)'
                    '(<i>x</i> − 3) = 0 va ildizlar −8 hamda 3. Musbati '
                    'soʻralgan. <strong>8</strong> — koʻpaytuvchidagi sonni ishorasini '
                    'oʻzgartirmay olgan javob.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A phone plan costs $12 per month plus $0.05 for each minute of '
                      'calls. Which equation gives the total cost <i>C</i>, in dollars, for '
                      'a month in which <i>m</i> minutes of calls are made?</p>',
     'choices': [
         '<i>C</i> = 0.05<i>m</i> + 12',
         '<i>C</i> = 0.05(<i>m</i> + 12)',
         '<i>C</i> = 12<i>m</i> + 0.05',
         '<i>C</i> = 12.05<i>m</i>',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong><i>C</i> = 0.05<i>m</i> + 12</strong>. $0.05 '
                    'har bir daqiqaga tegishli, demak u <i>m</i> ga koʻpayadi; $12 esa oyiga '
                    'bir marta, demak oʻzgarmas qoʻshiluvchi. <strong><i>C</i> = '
                    '12.05<i>m</i></strong> ikkalasini ham daqiqaga bogʻlab yuboradi — '
                    'bir martalik toʻlovni hech qachon <i>m</i> ga koʻpaytirmang.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A square has a perimeter of 36 units. What is the area of the '
                      'square?</p>',
     'choices': ['18', '36', '81', '324'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>81</strong>. Kvadratning toʻrt tomoni teng, '
                    'demak tomoni 36 ÷ 4 = 9, yuzasi esa 9<sup>2</sup> = 81. '
                    '<strong>324</strong> — 36<sup>2</sup>, yaʼni perimetrni tomon deb '
                    'olgan javob.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>A sample contains 800 milligrams of a substance, and half of what '
                      'remains decays every 6 years. Which function gives the number of '
                      'milligrams, <i>A</i>, remaining after <i>t</i> years?</p>',
     'choices': [
         '<i>A</i>(<i>t</i>) = 800(1/2)<sup>6<i>t</i></sup>',
         '<i>A</i>(<i>t</i>) = 800(1/2)<sup><i>t</i>/6</sup>',
         '<i>A</i>(<i>t</i>) = 800(6)<sup><i>t</i>/2</sup>',
         '<i>A</i>(<i>t</i>) = 800 − (1/2)<i>t</i>',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>A</i>(<i>t</i>) = 800(1/2)'
                    '<sup><i>t</i>/6</sup></strong>. Boshlangʻich miqdor 800, koʻpaytuvchi '
                    '½, va u har 6 yilda bir marta qoʻllanadi — demak daraja '
                    '<i>t</i>/6. Tekshiring: <i>t</i> = 6 da 800 × ½ = 400. '
                    '<strong><i>A</i>(<i>t</i>) = 800(1/2)<sup>6<i>t</i></sup></strong> da '
                    '<i>t</i> = 6 boʻlsa daraja 36 chiqadi — davrni koʻpaytirib '
                    'yuborgan xato.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>What is the least integer value of <i>x</i> that satisfies the '
                      'inequality 4(<i>x</i> + 2) &gt; 3<i>x</i> + 15?</p>',
     'choices': ['6', '7', '8', '9'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Qavsni ochamiz: 4<i>x</i> + 8 &gt; '
                    '3<i>x</i> + 15, bundan <i>x</i> &gt; 7. Tengsizlik <em>qatʼiy</em> '
                    'boʻlgani uchun 7 ning oʻzi yaramaydi, eng kichik butun son — 8. '
                    '<strong>7</strong> aynan shu tuzoq: "&gt;" ni "≥" deb oʻqish.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>For the data set 5, 9, 9, 12, 20, what is the difference between '
                      'the mean and the median?</p>',
     'choices': ['1', '2', '3', '11'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. Oʻrta arifmetik — '
                    '(5 + 9 + 9 + 12 + 20) ÷ 5 = 55 ÷ 5 = 11; mediana — tartiblangan '
                    'beshta sonning uchinchisi, yaʼni 9. Ayirma 11 − 9 = 2. '
                    '<strong>11</strong> — oʻrta arifmetikning oʻzi: savol '
                    '<em>ayirmani</em> soʻraydi.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If <i>x</i><sup>2</sup> − 12<i>x</i> + <i>k</i> is the '
                      'square of a binomial, what is the value of the constant '
                      '<i>k</i>?</p>',
     'choices': ['6', '12', '24', '36'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>36</strong>. (<i>x</i> − <i>a</i>)'
                    '<sup>2</sup> = <i>x</i><sup>2</sup> − 2<i>ax</i> + '
                    '<i>a</i><sup>2</sup>, demak 2<i>a</i> = 12, <i>a</i> = 6 va '
                    '<i>k</i> = 6<sup>2</sup> = 36. <strong>6</strong> — <i>a</i> ning '
                    'oʻzi: savol <i>k</i> ni soʻraydi.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, the graph of 3<i>x</i> + <i>ky</i> = 9 '
                      'is perpendicular to the graph of <i>y</i> = ½<i>x</i> + 4, where '
                      '<i>k</i> is a constant. What is the value of <i>k</i>?</p>',
     'choices': ['−3/2', '−2/3', '2/3', '3/2'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>3/2</strong>. Perpendikulyar chiziqning burchak '
                    'koeffitsiyenti — manfiy teskari son: ½ ning teskarisi 2, manfiysi '
                    '−2. Endi 3<i>x</i> + <i>ky</i> = 9 ni yechamiz: <i>y</i> = '
                    '(9 − 3<i>x</i>) ÷ <i>k</i>, koeffitsiyent −3/<i>k</i>. '
                    '−3/<i>k</i> = −2 dan <i>k</i> = 3/2. '
                    '<strong>−3/2</strong> — ikkita minusni ikki marta hisobga '
                    'olgan javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>DEF</i> below, angle <i>E</i> is a right '
                      'angle, <i>DE</i> = 9, and <i>EF</i> = 12. What is the value of '
                      'cos <i>D</i>?</p>'
                      '<svg viewBox="0 0 200 135" width="210" height="142" role="img" '
                      'aria-label="Right triangle DEF with the right angle at E">'
                      '<polygon points="24,112 24,28 174,112" fill="none" '
                      'stroke="currentColor" stroke-width="2"/>'
                      '<rect x="24" y="98" width="14" height="14" fill="none" '
                      'stroke="currentColor" stroke-width="1.5"/>'
                      '<text x="12" y="24" font-size="13" fill="currentColor">D</text>'
                      '<text x="10" y="126" font-size="13" fill="currentColor">E</text>'
                      '<text x="176" y="126" font-size="13" fill="currentColor">F</text>'
                      '<text x="30" y="74" font-size="12" fill="currentColor">9</text>'
                      '<text x="94" y="128" font-size="12" fill="currentColor">12</text>'
                      '</svg>',
     'choices': ['3/5', '3/4', '4/5', '4/3'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>3/5</strong>. Avval gipotenuza: '
                    '<i>DF</i><sup>2</sup> = 9<sup>2</sup> + 12<sup>2</sup> = 81 + 144 = '
                    '225, demak <i>DF</i> = 15. cos <i>D</i> = yondosh ÷ gipotenuza = '
                    '<i>DE</i>/<i>DF</i> = 9/15 = 3/5. <strong>4/5</strong> — bu '
                    'sin <i>D</i>: <i>D</i> ga <em>qarshi</em> katetni olgan javob.'},

    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '(<i>x</i> + 2)(<i>x</i> − 6). In the <i>xy</i>-plane, the graph '
                      'of <i>y</i> = <i>f</i>(<i>x</i>) has its vertex at the point '
                      '(<i>h</i>, <i>k</i>). What is the value of <i>h</i>?</p>',
     'choices': ['−2', '2', '4', '6'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. Nollar <i>x</i> = −2 va '
                    '<i>x</i> = 6; parabola ular orasida simmetrik, demak uchning '
                    'abssissasi — oʻrta nuqta: (−2 + 6) ÷ 2 = 2. '
                    '<strong>4</strong> aynan shu savolning tuzogʻi: ishorani tashlab, '
                    '(2 + 6) ÷ 2 = 4 deb hisoblash.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 7(<i>x</i> + 3) = 4<i>x</i> + 39, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['6'],
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Qavsni ochamiz: 7<i>x</i> + 21 = '
                    '4<i>x</i> + 39. 4<i>x</i> ni ayirib, 21 ni ham ayiramiz: 3<i>x</i> = '
                    '18, demak <i>x</i> = 6. Tekshirish: 7 × 9 = 63 va 4 × 6 + 39 = 63.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>In a class of 32 students, the ratio of students who walk to '
                      'school to those who do not is 3 to 5. How many students in the class '
                      'walk to school?</p>' + GRID_NOTE,
     'accepted': ['12'],
     'explanation': 'Toʻgʻri javob <strong>12</strong>. Nisbat 3 : 5 jami 8 ulushni beradi, '
                    'demak bir ulush 32 ÷ 8 = 4 oʻquvchi. Piyoda keladiganlar 3 ulush: '
                    '3 × 4 = 12. Eng keng tarqalgan xato — 32 ni 3 ga boʻlish: '
                    'nisbatda maxraj <em>ulushlar yigʻindisi</em> boʻlishi kerak.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 2<sup><i>x</i></sup> = 1/8, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['-3'],
     'explanation': 'Toʻgʻri javob <strong>−3</strong>. 8 = 2<sup>3</sup>, demak '
                    '1/8 = 2<sup>−3</sup>. Asoslar teng boʻlgani uchun darajalar ham '
                    'teng: <i>x</i> = −3. Manfiy daraja kasrni bildiradi — minus '
                    'ishorasi ham javob qutichasiga kiradi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>A line passes through the points (0, 5) and (4, 17) in the '
                      '<i>xy</i>-plane. What is the slope of the line?</p>' + GRID_NOTE,
     'accepted': ['3'],
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Burchak koeffitsiyenti — '
                    '(17 − 5) ÷ (4 − 0) = 12 ÷ 4 = 3. Birinchi nuqtaning '
                    '<i>x</i> i nol boʻlgani uchun 5 bu chiziqning <i>y</i>-kesimi, lekin '
                    'savol koeffitsiyentni soʻraydi.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> − 4<i>x</i> + 7. What is the minimum value '
                      'of <i>f</i>(<i>x</i>)?</p>' + GRID_NOTE,
     'accepted': ['3'],
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Parabola yuqoriga ochilgani uchun '
                    'eng kichik qiymat uch nuqtasida. Uchning abssissasi <i>x</i> = '
                    '−(−4) ÷ 2 = 2, qiymati esa <i>f</i>(2) = 4 − 8 + 7 = 3. '
                    '<strong>2</strong> yozib yuborish oson — u uchning <i>x</i> i, '
                    'savol esa <em>qiymatni</em> soʻraydi.'},
]
