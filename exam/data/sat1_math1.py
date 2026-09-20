# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 1 · Math, Module 1
#  22 questions · 35 minutes · every taker sits this one.
#  Questions 18–22 are student-produced responses (grid-ins).
#
#  Route: 14 or more correct here sends the taker to the UPPER module 2.
#
#  Maths is HTML, never LaTeX; figures are inline SVG. The exam page does
#  NOT load the pm-*/ps-* stylesheets, so a figure carries its own colours
#  through currentColor.
#
#  Load: python manage.py load_mock exam/data/sat1_math1.py --expect-questions=22
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §2
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

S = 'math1'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 3<i>x</i> + 7 = 25, what is the value of <i>x</i>?</p>',
     'choices': ['4', '6', '9', '18'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Ikki tomondan 7 ni ayiramiz: '
                    '3<i>x</i> = 18, soʻng 3 ga boʻlamiz: <i>x</i> = 6. '
                    '<strong>18</strong> — 3<i>x</i> ning qiymati, yaʼni oxirgi qadamni '
                    'unutgan talabaning javobi.'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>A jacket normally costs $48. During a sale, its price is '
                      'reduced by 25%. What is the sale price of the jacket?</p>',
     'choices': ['$12', '$23', '$36', '$38'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>$36</strong>. Chegirma 48 × 0.25 = $12, narx esa '
                    '48 − 12 = $36. Yoki bir qadamda: 48 × 0.75 = 36. <strong>$12</strong> '
                    '— chegirmaning oʻzi: savol narxni soʻraydi, chegirmani emas.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>Line <i>ℓ</i> passes through the points (2, 5) and (6, 17) '
                      'in the <i>xy</i>-plane. What is the slope of line <i>ℓ</i>?</p>',
     'choices': ['1/3', '2', '3', '4'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Burchak koeffitsiyenti — '
                    '(17 − 5) ÷ (6 − 2) = 12 ÷ 4 = 3. <strong>1/3</strong> — ayirmalarni '
                    'teskari boʻlgan javob (Δ<i>x</i> ÷ Δ<i>y</i>): har doim <em>y</em> '
                    'yuqorida turishini eslang.'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '2<i>x</i><sup>2</sup> − 5. What is the value of '
                      '<i>f</i>(−3)?</p>',
     'choices': ['−23', '−13', '13', '23'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>13</strong>. (−3)<sup>2</sup> = 9, chunki '
                    'manfiy sonning kvadrati musbat; keyin 2 × 9 − 5 = 13. '
                    '<strong>−23</strong> — kvadratni (−3)<sup>2</sup> = −9 '
                    'deb olgan talabaning javobi va bu bu yerdagi eng keng tarqalgan xato.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>In triangle <i>ABC</i>, the measure of angle <i>A</i> is '
                      '42° and the measure of angle <i>B</i> is 73°. What is '
                      'the measure of angle <i>C</i>?</p>',
     'choices': ['45°', '65°', '75°', '115°'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>65°</strong>. Uchburchak burchaklari '
                    'yigʻindisi 180°, demak <i>C</i> = 180 − 42 − 73 = '
                    '65°. <strong>115°</strong> — 42 + 73 ning oʻzi, yaʼni '
                    'ayirishni unutgan javob.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>2<i>x</i> + <i>y</i> = 11<br>'
                      '<i>x</i> − <i>y</i> = 1</p>'
                      '<p>The system of equations above has a unique solution. What is '
                      'the value of <i>x</i>?</p>',
     'choices': ['3', '4', '5', '7'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Ikki tenglamani qoʻshsak, '
                    '<i>y</i> qisqaradi: 3<i>x</i> = 12, demak <i>x</i> = 4. '
                    '<strong>3</strong> — <i>y</i> ning qiymati: sistemada qaysi '
                    'nomaʼlum soʻralganini oxirida yana bir bor tekshiring.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>A printer produces pages at a constant rate of 18 pages per '
                      'minute. How many minutes will the printer take to produce 486 '
                      'pages?</p>',
     'choices': ['24', '27', '30', '36'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>27</strong>. Vaqt = umumiy son ÷ tezlik = '
                    '486 ÷ 18 = 27 daqiqa. Tekshirish: 18 × 27 = 486. Tezlik masalasida '
                    'boʻlish yoʻnalishini birlik bilan aniqlang — sahifa ÷ (sahifa/daqiqa) '
                    '= daqiqa.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>What is the sum of the solutions to the equation '
                      '<i>x</i><sup>2</sup> − 7<i>x</i> + 12 = 0?</p>',
     'choices': ['−12', '−7', '7', '12'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. Koʻpaytuvchilarga ajratsak '
                    '(<i>x</i> − 3)(<i>x</i> − 4) = 0, ildizlar 3 va 4, '
                    'yigʻindisi 7. Tezroq yoʻl: <i>x</i><sup>2</sup> + <i>bx</i> + <i>c</i> '
                    'da ildizlar yigʻindisi −<i>b</i>. <strong>12</strong> — '
                    'ildizlarning <em>koʻpaytmasi</em>.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A gym charges a one-time joining fee of $30 plus $8 for each '
                      'class a member attends. Which equation gives the total cost '
                      '<i>C</i>, in dollars, for a member who attends <i>n</i> '
                      'classes?</p>',
     'choices': [
         '<i>C</i> = 8<i>n</i> + 30',
         '<i>C</i> = 8(<i>n</i> + 30)',
         '<i>C</i> = 30<i>n</i> + 8',
         '<i>C</i> = 38<i>n</i>',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong><i>C</i> = 8<i>n</i> + 30</strong>. $8 har bir '
                    'darsga tegishli, demak u <i>n</i> ga koʻpayadi; $30 esa bir marta '
                    'toʻlanadi, demak u oʻzgarmas qoʻshiluvchi. <strong><i>C</i> = '
                    '38<i>n</i></strong> ikkalasini ham darsga bogʻlab yuboradi — bir marta '
                    'toʻlanadigan toʻlovni hech qachon <i>n</i> ga koʻpaytirmang.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A circle in the <i>xy</i>-plane has an area of 49π square '
                      'units. What is the circumference of the circle?</p>',
     'choices': ['7π', '14π', '28π', '49π'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>14π</strong>. Yuza π<i>r</i><sup>2</sup> '
                    '= 49π dan <i>r</i><sup>2</sup> = 49, demak <i>r</i> = 7; aylana '
                    'uzunligi 2π<i>r</i> = 14π. <strong>7π</strong> — radiusni '
                    'topib, 2 ga koʻpaytirishni unutgan javob.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>A colony of 400 bacteria doubles in size every 3 hours. Which '
                      'function gives the number of bacteria, <i>P</i>, after <i>t</i> '
                      'hours?</p>',
     'choices': [
         '<i>P</i>(<i>t</i>) = 2(400)<sup><i>t</i>/3</sup>',
         '<i>P</i>(<i>t</i>) = 400(2)<sup>3<i>t</i></sup>',
         '<i>P</i>(<i>t</i>) = 400(2)<sup><i>t</i>/3</sup>',
         '<i>P</i>(<i>t</i>) = 400(3)<sup><i>t</i>/2</sup>',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong><i>P</i>(<i>t</i>) = 400(2)<sup><i>t</i>/3</sup>'
                    '</strong>. Boshlangʻich son — 400, koʻpaytuvchi — 2 (ikki barobar), '
                    'va u har 3 soatda bir marta qoʻllanadi, demak daraja <i>t</i>/3. '
                    'Tekshiring: <i>t</i> = 3 da 400 × 2 = 800. <strong><i>P</i>(<i>t</i>) = '
                    '400(2)<sup>3<i>t</i></sup></strong> da <i>t</i> = 3 boʻlsa 400 × '
                    '2<sup>9</sup> chiqadi — davrni koʻpaytirib yuborgan xato.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>What is the greatest integer value of <i>x</i> that satisfies '
                      'the inequality 3(<i>x</i> − 4) ≤ 2<i>x</i> + 1?</p>',
     'choices': ['11', '12', '13', '14'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>13</strong>. Qavsni ochamiz: 3<i>x</i> − 12 '
                    '≤ 2<i>x</i> + 1, ikki tomondan 2<i>x</i> ni ayiramiz: <i>x</i> '
                    '− 12 ≤ 1, demak <i>x</i> ≤ 13. Eng katta butun son — '
                    '13 ning oʻzi, chunki tengsizlik qatʼiy emas (≤). '
                    '<strong>12</strong> — "≤" ni "&lt;" deb oʻqigan javob.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>The mean of five numbers is 12. Four of the numbers are 8, 10, '
                      '14, and 16. What is the fifth number?</p>',
     'choices': ['10', '11', '12', '14'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>12</strong>. Oʻrta arifmetik 12 boʻlsa, beshta '
                    'sonning yigʻindisi 5 × 12 = 60. Berilgan toʻrttasining yigʻindisi '
                    '8 + 10 + 14 + 16 = 48, demak beshinchisi 60 − 48 = 12. Oʻrta '
                    'arifmetik masalasida har doim avval <em>yigʻindini</em> tiklang.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If <i>x</i><sup>2</sup> + 6<i>x</i> + <i>c</i> is the square '
                      'of a binomial, what is the value of the constant <i>c</i>?</p>',
     'choices': ['3', '6', '9', '12'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. (<i>x</i> + <i>a</i>)<sup>2</sup> = '
                    '<i>x</i><sup>2</sup> + 2<i>ax</i> + <i>a</i><sup>2</sup>, demak '
                    '2<i>a</i> = 6, <i>a</i> = 3 va <i>c</i> = <i>a</i><sup>2</sup> = 9. '
                    '<strong>3</strong> — <i>a</i> ning oʻzi: savol <i>c</i> ni soʻraydi.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, the graph of 4<i>x</i> + <i>ky</i> = 12 '
                      'is parallel to the graph of <i>y</i> = 2<i>x</i> − 5, where '
                      '<i>k</i> is a constant. What is the value of <i>k</i>?</p>',
     'choices': ['−4', '−2', '2', '4'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>−2</strong>. 4<i>x</i> + <i>ky</i> = 12 ni '
                    '<i>y</i> ga nisbatan yechamiz: <i>y</i> = (12 − 4<i>x</i>) ÷ '
                    '<i>k</i>, burchak koeffitsiyenti −4/<i>k</i>. Parallellik uni 2 ga '
                    'tenglaydi: −4/<i>k</i> = 2, demak <i>k</i> = −2. '
                    '<strong>2</strong> — minus ishorasini tushirib qoldirgan javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>ABC</i> below, angle <i>B</i> is a right '
                      'angle, <i>AB</i> = 8, and <i>BC</i> = 15. What is the value of '
                      'sin <i>A</i>?</p>'
                      '<svg viewBox="0 0 200 135" width="210" height="142" role="img" '
                      'aria-label="Right triangle ABC with the right angle at B">'
                      '<polygon points="24,112 24,28 174,112" fill="none" '
                      'stroke="currentColor" stroke-width="2"/>'
                      '<rect x="24" y="98" width="14" height="14" fill="none" '
                      'stroke="currentColor" stroke-width="1.5"/>'
                      '<text x="12" y="24" font-size="13" fill="currentColor">A</text>'
                      '<text x="10" y="126" font-size="13" fill="currentColor">B</text>'
                      '<text x="176" y="126" font-size="13" fill="currentColor">C</text>'
                      '<text x="30" y="74" font-size="12" fill="currentColor">8</text>'
                      '<text x="94" y="128" font-size="12" fill="currentColor">15</text>'
                      '</svg>',
     'choices': ['8/17', '8/15', '15/17', '15/8'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>15/17</strong>. Avval gipotenuzani topamiz: '
                    '<i>AC</i><sup>2</sup> = 8<sup>2</sup> + 15<sup>2</sup> = 64 + 225 = '
                    '289, demak <i>AC</i> = 17. sin <i>A</i> = (<i>A</i> ga qarshi katet) ÷ '
                    'gipotenuza = <i>BC</i>/<i>AC</i> = 15/17. <strong>8/17</strong> — bu '
                    'cos <i>A</i>: <i>A</i> ga <em>yondosh</em> katetni olgan javob.'},

    # ── Student-produced responses (18–22 on the real test) ────────────
    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '(<i>x</i> \u2212 3)(<i>x</i> + 5). In the <i>xy</i>-plane, the '
                      'graph of <i>y</i> = <i>f</i>(<i>x</i>) has its vertex at the '
                      'point (<i>h</i>, <i>k</i>). What is the value of <i>k</i>?</p>',
     'choices': ['\u221216', '\u221212', '\u22128', '1'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>\u221216</strong>. Nollar <i>x</i> = 3 va '
                    '<i>x</i> = \u22125; parabola ular orasida simmetrik, demak uchning '
                    'abssissasi \u2014 oʻrta nuqta: <i>h</i> = (3 + (\u22125)) ÷ 2 = '
                    '\u22121. Endi <i>k</i> = <i>f</i>(\u22121) = (\u22121 \u2212 3)'
                    '(\u22121 + 5) = (\u22124)(4) = \u221216. '
                    '<strong>\u221212</strong> aynan shu savolning tuzogʻi: ishoraga '
                    'eʼtibor bermay, oʻrta nuqtani (3 + 5) ÷ 2 = 1 deb olgan talaba '
                    '<i>f</i>(1) = (\u22122)(6) = \u221212 ni yozadi.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 5(<i>x</i> − 2) = 3<i>x</i> + 8, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['9'],
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Qavsni ochamiz: 5<i>x</i> − 10 '
                    '= 3<i>x</i> + 8. Ikki tomondan 3<i>x</i> ni ayiramiz va 10 ni '
                    'qoʻshamiz: 2<i>x</i> = 18, demak <i>x</i> = 9. Tekshirish: '
                    '5(9 − 2) = 35 va 3 × 9 + 8 = 35.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>In a survey of 240 students, 35% said that they walk to '
                      'school. How many of the students surveyed said that they walk to '
                      'school?</p>' + GRID_NOTE,
     'accepted': ['84'],
     'explanation': 'Toʻgʻri javob <strong>84</strong>. 240 × 0.35 = 84. Boshqacha '
                    'hisoblash: 10% = 24, demak 30% = 72; 5% = 12; 72 + 12 = 84. Javob '
                    'quticha faqat sonni kutadi — "84%" yoki "84 students" deb yozilsa, '
                    'haqiqiy imtihonda ham xato boʻladi.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>2</sup> − 10<i>x</i> + 21 = 0 and '
                      '<i>x</i> &gt; 5, what is the value of <i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['7'],
     'explanation': 'Toʻgʻri javob <strong>7</strong>. (<i>x</i> − 3)(<i>x</i> − 7) '
                    '= 0 dan ildizlar 3 va 7. Shart <i>x</i> &gt; 5 ikkinchisini tanlaydi. '
                    'Shartni oxirida emas, ildizlarni topgan zahoti qoʻllang — aks holda '
                    '3 yozib yuborish oson.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>Line <i>ℓ</i> has a slope of 2/3 and passes through the '
                      'point (6, 1) in the <i>xy</i>-plane. What is the '
                      '<i>y</i>-coordinate of the <i>y</i>-intercept of line '
                      '<i>ℓ</i>?</p>' + GRID_NOTE,
     'accepted': ['-3'],
     'explanation': 'Toʻgʻri javob <strong>−3</strong>. <i>y</i> = (2/3)<i>x</i> + '
                    '<i>b</i> ga nuqtani qoʻyamiz: 1 = (2/3)(6) + <i>b</i> = 4 + <i>b</i>, '
                    'demak <i>b</i> = −3. Manfiy javobni yozishda minus ishorasi ham '
                    'qutichaga kiradi.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If <i>f</i>(<i>x</i>) = 3<sup><i>x</i></sup> and '
                      '<i>f</i>(<i>a</i>) = 81, what is the value of <i>a</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['4'],
     'explanation': 'Toʻgʻri javob <strong>4</strong>. 81 ni 3 ning darajasi sifatida '
                    'yozamiz: 81 = 3 × 3 × 3 × 3 = 3<sup>4</sup>, demak <i>a</i> = 4. '
                    'Asoslar teng boʻlganda darajalar ham teng boʻladi.'},
]
