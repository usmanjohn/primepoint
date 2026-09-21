# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 5 · Math, Module 1
#  22 questions · 35 minutes · every taker sits this one.
#  Questions 18–22 are student-produced responses (grid-ins).
#  Route: 14 or more correct here sends the taker to the UPPER module 2.
#
#  Load: python manage.py load_mock exam/data/sat5_math1.py --expect-questions=22
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

S = 'math1'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 9<i>x</i> + 5 = 50, what is the value of <i>x</i>?</p>',
     'choices': ['5', '6', '45', '55'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. 5 ni ayiramiz: 9<i>x</i> = 45, '
                    'soʻng 9 ga boʻlamiz: <i>x</i> = 5. <strong>45</strong> — '
                    '9<i>x</i> ning qiymati, yaʼni oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>A meal costs $45.00 and a tip of 20% is added to the bill. What '
                      'is the total amount paid?</p>',
     'choices': ['$9.00', '$36.00', '$54.00', '$65.00'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>$54.00</strong>. Choychaqa 45 × 0.20 = $9.00, '
                    'jami esa 45 + 9 = $54.00. <strong>$9.00</strong> — '
                    'choychaqaning oʻzi: savol jamini soʻraydi.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>A line passes through the points (3, 4) and (7, 20) in the '
                      '<i>xy</i>-plane. What is the slope of the line?</p>',
     'choices': ['1/4', '4', '5', '16'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Burchak koeffitsiyenti — '
                    '(20 − 4) ÷ (7 − 3) = 16 ÷ 4 = 4. <strong>16</strong> '
                    '— faqat suratni hisoblab, boʻlishni unutgan javob.'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>s</i> is defined by <i>s</i>(<i>x</i>) = '
                      '4<i>x</i><sup>2</sup> + 2. What is the value of '
                      '<i>s</i>(−3)?</p>',
     'choices': ['−34', '−22', '26', '38'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>38</strong>. (−3)<sup>2</sup> = 9, chunki '
                    'manfiy sonning kvadrati musbat; keyin 4 × 9 + 2 = 38. '
                    '<strong>−34</strong> — kvadratni (−3)<sup>2</sup> = '
                    '−9 deb olgan javob.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>A right triangle has legs of length 9 and 40. What is the length '
                      'of its hypotenuse?</p>',
     'choices': ['31', '41', '49', '1,681'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>41</strong>. Pifagor teoremasi boʻyicha '
                    '<i>c</i><sup>2</sup> = 81 + 1,600 = 1,681, demak <i>c</i> = '
                    '√1,681 = 41. <strong>1,681</strong> — '
                    '<i>c</i><sup>2</sup> ning oʻzi: ildizni olish qolib ketgan.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p><i>x</i> + 3<i>y</i> = 20<br><i>x</i> = 2<i>y</i></p>'
                      '<p>The system of equations above has a unique solution. What is the '
                      'value of <i>x</i>?</p>',
     'choices': ['4', '5', '8', '12'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Ikkinchi tenglamadagi <i>x</i> ni '
                    'birinchisiga qoʻyamiz: 2<i>y</i> + 3<i>y</i> = 20, yaʼni <i>y</i> = 4; '
                    'demak <i>x</i> = 2 × 4 = 8. <strong>4</strong> — <i>y</i> ning '
                    'qiymati: qaysi nomaʼlum soʻralganini oxirida tekshiring.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>A printer produces 96 pages in 3 minutes. At this rate, how many '
                      'pages will it produce in 11 minutes?</p>',
     'choices': ['288', '320', '352', '384'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>352</strong>. Tezlik 96 ÷ 3 = 32 sahifa/daqiqa, '
                    'demak 32 × 11 = 352. Yoki proportsiya bilan: 96/3 = <i>x</i>/11.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>What is the positive solution to the equation '
                      '<i>x</i><sup>2</sup> − 4<i>x</i> − 45 = 0?</p>',
     'choices': ['−9', '−5', '5', '9'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Koʻpaytmasi −45, yigʻindisi '
                    '−4 boʻlgan ikki son — −9 va 5, demak (<i>x</i> − '
                    '9)(<i>x</i> + 5) = 0 va ildizlar 9 hamda −5. <strong>5</strong> '
                    '— koʻpaytuvchilardagi sonlarni ishorasiz olgan javob.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A club membership costs $60 for the year plus $9 for each visit. '
                      'Which equation gives the total cost <i>C</i>, in dollars, for a '
                      'member who makes <i>v</i> visits in the year?</p>',
     'choices': [
         '<i>C</i> = 9<i>v</i> + 60',
         '<i>C</i> = 9(<i>v</i> + 60)',
         '<i>C</i> = 60<i>v</i> + 9',
         '<i>C</i> = 69<i>v</i>',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong><i>C</i> = 9<i>v</i> + 60</strong>. $9 har bir '
                    'tashrifga tegishli, demak u <i>v</i> ga koʻpayadi; $60 esa yiliga bir '
                    'marta. <strong><i>C</i> = 69<i>v</i></strong> ikkalasini ham tashrifga '
                    'bogʻlab yuboradi — bir martalik toʻlovni hech qachon <i>v</i> ga '
                    'koʻpaytirmang.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A cube has a total surface area of 96 square units. What is its '
                      'volume?</p>',
     'choices': ['16', '48', '64', '216'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>64</strong>. Kubning oltita yogʻi bor, demak '
                    'bitta yoqning yuzi 96 ÷ 6 = 16 va qirrasi √16 = 4. Hajmi '
                    '4<sup>3</sup> = 64. <strong>16</strong> — bitta yoqning yuzi: '
                    'savol hajmni soʻraydi.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>A colony of 60 bacteria triples in size every 4 hours. Which '
                      'function gives the number of bacteria, <i>P</i>, after <i>t</i> '
                      'hours?</p>',
     'choices': [
         '<i>P</i>(<i>t</i>) = 3(60)<sup><i>t</i>/4</sup>',
         '<i>P</i>(<i>t</i>) = 60(3)<sup>4<i>t</i></sup>',
         '<i>P</i>(<i>t</i>) = 60(3)<sup><i>t</i>/4</sup>',
         '<i>P</i>(<i>t</i>) = 60(4)<sup><i>t</i>/3</sup>',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong><i>P</i>(<i>t</i>) = 60(3)<sup><i>t</i>/4</sup>'
                    '</strong>. Boshlangʻich son 60, koʻpaytuvchi 3, va u har 4 soatda bir '
                    'marta qoʻllanadi — demak daraja <i>t</i>/4. Tekshiring: '
                    '<i>t</i> = 4 da 60 × 3 = 180. <strong><i>P</i>(<i>t</i>) = '
                    '60(3)<sup>4<i>t</i></sup></strong> davrni koʻpaytirib yuboradi.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>What is the least integer value of <i>x</i> that satisfies the '
                      'inequality 7(<i>x</i> − 1) ≥ 6<i>x</i> + 5?</p>',
     'choices': ['10', '11', '12', '13'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>12</strong>. Qavsni ochamiz: 7<i>x</i> − 7 '
                    '≥ 6<i>x</i> + 5, bundan <i>x</i> ≥ 12. Tengsizlik qatʼiy '
                    'emas, shuning uchun 12 ning oʻzi ham yaraydi va u eng kichik butun '
                    'son. <strong>13</strong> — "≥" ni "&gt;" deb oʻqigan '
                    'javob.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>The mean of a set of five numbers is 16. If every number in the '
                      'set is increased by 4, what is the mean of the new set?</p>',
     'choices': ['16', '18', '20', '36'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>20</strong>. Har bir songa 4 qoʻshilsa, '
                    'yigʻindiga 5 × 4 = 20 qoʻshiladi, oʻrtachaga esa 20 ÷ 5 = 4 '
                    'qoʻshiladi: 16 + 4 = 20. <strong>36</strong> — oʻrtachaga '
                    'yigʻindidagi butun oʻsishni (20) qoʻshgan javob.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If <i>x</i><sup>2</sup> + 20<i>x</i> + <i>c</i> is the square of '
                      'a binomial, what is the value of the constant <i>c</i>?</p>',
     'choices': ['10', '20', '40', '100'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>100</strong>. (<i>x</i> + <i>a</i>)<sup>2</sup> '
                    '= <i>x</i><sup>2</sup> + 2<i>ax</i> + <i>a</i><sup>2</sup>, demak '
                    '2<i>a</i> = 20, <i>a</i> = 10 va <i>c</i> = 10<sup>2</sup> = 100. '
                    '<strong>10</strong> — <i>a</i> ning oʻzi: savol <i>c</i> ni '
                    'soʻraydi.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, the graph of 6<i>x</i> + <i>ky</i> = 24 '
                      'is parallel to the graph of <i>y</i> = 3<i>x</i> − 7, where '
                      '<i>k</i> is a constant. What is the value of <i>k</i>?</p>',
     'choices': ['−3', '−2', '2', '3'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>−2</strong>. 6<i>x</i> + <i>ky</i> = 24 ni '
                    '<i>y</i> ga nisbatan yechamiz: burchak koeffitsiyenti '
                    '−6/<i>k</i>. Parallellik uni 3 ga tenglaydi: −6/<i>k</i> = '
                    '3, demak <i>k</i> = −2. <strong>2</strong> — minus '
                    'ishorasini tushirib qoldirgan javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>ABC</i> below, angle <i>B</i> is a right '
                      'angle, <i>AB</i> = 12 and <i>BC</i> = 35. What is the value of '
                      'cos <i>A</i>?</p>'
                      '<svg viewBox="0 0 200 135" width="210" height="142" role="img" '
                      'aria-label="Right triangle ABC with the right angle at B">'
                      '<polygon points="24,112 24,28 174,112" fill="none" '
                      'stroke="currentColor" stroke-width="2"/>'
                      '<rect x="24" y="98" width="14" height="14" fill="none" '
                      'stroke="currentColor" stroke-width="1.5"/>'
                      '<text x="12" y="24" font-size="13" fill="currentColor">A</text>'
                      '<text x="10" y="126" font-size="13" fill="currentColor">B</text>'
                      '<text x="176" y="126" font-size="13" fill="currentColor">C</text>'
                      '<text x="30" y="74" font-size="12" fill="currentColor">12</text>'
                      '<text x="94" y="128" font-size="12" fill="currentColor">35</text>'
                      '</svg>',
     'choices': ['12/37', '12/35', '35/37', '35/12'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>12/37</strong>. Avval gipotenuza: '
                    '<i>AC</i><sup>2</sup> = 144 + 1,225 = 1,369, demak <i>AC</i> = 37. '
                    'cos <i>A</i> = yondosh ÷ gipotenuza = <i>AB</i>/<i>AC</i> = 12/37. '
                    '<strong>35/37</strong> — bu sin <i>A</i>: qarshi katetni olgan '
                    'javob.'},

    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '(<i>x</i> − 4)(<i>x</i> + 10). In the <i>xy</i>-plane, the '
                      'graph of <i>y</i> = <i>f</i>(<i>x</i>) has its vertex at the point '
                      '(<i>h</i>, <i>k</i>). What is the value of <i>h</i>?</p>',
     'choices': ['−3', '3', '6', '7'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>−3</strong>. Nollar <i>x</i> = 4 va '
                    '<i>x</i> = −10; parabola ular orasida simmetrik, demak uchning '
                    'abssissasi oʻrta nuqta: (4 + (−10)) ÷ 2 = −3. '
                    '<strong>7</strong> aynan shu savolning tuzogʻi: ishorani tashlab, '
                    '(4 + 10) ÷ 2 = 7 deb hisoblash.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 6(<i>x</i> + 3) = 4<i>x</i> + 30, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['6'],
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Qavsni ochamiz: 6<i>x</i> + 18 = '
                    '4<i>x</i> + 30. 4<i>x</i> ni ayirib, 18 ni ayiramiz: 2<i>x</i> = 12, '
                    'demak <i>x</i> = 6. Tekshirish: 6 × 9 = 54 va 4 × 6 + 30 = 54.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>A shop reduces the price of a coat from $250 by 36%. What is the '
                      'new price, in dollars?</p>' + GRID_NOTE,
     'accepted': ['160'],
     'explanation': 'Toʻgʻri javob <strong>160</strong>. 36% chegirma 250 × 0.36 = $90 ni '
                    'beradi, yangi narx esa 250 − 90 = $160. Bir qadamda: '
                    '250 × 0.64 = 160. Javob qutichasiga faqat sonni yozing.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 5<sup><i>x</i></sup> = 1/125, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['-3'],
     'explanation': 'Toʻgʻri javob <strong>−3</strong>. 125 = 5<sup>3</sup>, demak '
                    '1/125 = 5<sup>−3</sup>. Manfiy daraja kasrni bildiradi — '
                    'minus ishorasi ham javob qutichasiga kiradi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>A line passes through the points (1, 7) and (4, 1) in the '
                      '<i>xy</i>-plane. What is the <i>y</i>-coordinate of its '
                      '<i>y</i>-intercept?</p>' + GRID_NOTE,
     'accepted': ['9'],
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Burchak koeffitsiyenti '
                    '(1 − 7) ÷ (4 − 1) = −6 ÷ 3 = −2. Endi (1, 7) ni '
                    '<i>y</i> = −2<i>x</i> + <i>b</i> ga qoʻyamiz: 7 = −2 + '
                    '<i>b</i>, demak <i>b</i> = 9.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> − 12<i>x</i> + 40. What is the minimum '
                      'value of <i>f</i>(<i>x</i>)?</p>' + GRID_NOTE,
     'accepted': ['4'],
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Parabola yuqoriga ochilgani uchun '
                    'eng kichik qiymat uch nuqtasida. Uchning abssissasi <i>x</i> = '
                    '12 ÷ 2 = 6, qiymati esa <i>f</i>(6) = 36 − 72 + 40 = 4. '
                    '<strong>6</strong> yozib yuborish oson — u uchning <i>x</i> i, '
                    'savol esa qiymatni soʻraydi.'},
]
