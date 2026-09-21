# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 6 · Math, Module 1
#  22 questions · 35 minutes · every taker sits this one.
#  Questions 18–22 are student-produced responses (grid-ins).
#  Route: 14 or more correct here sends the taker to the UPPER module 2.
#
#  Load: python manage.py load_mock exam/data/sat6_math1.py --expect-questions=22
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

S = 'math1'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 8<i>x</i> − 11 = 45, what is the value of <i>x</i>?</p>',
     'choices': ['7', '9', '34', '56'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. 11 ni qoʻshamiz: 8<i>x</i> = 56, '
                    'soʻng 8 ga boʻlamiz: <i>x</i> = 7. <strong>56</strong> — '
                    '8<i>x</i> ning qiymati, yaʼni oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>A phone costs $320.00 and is then discounted by 15%. What is the '
                      'discounted price?</p>',
     'choices': ['$48.00', '$272.00', '$288.00', '$305.00'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>$272.00</strong>. Chegirma 320 × 0.15 = $48, '
                    'narx esa 320 − 48 = $272. Bir qadamda: 320 × 0.85 = 272. '
                    '<strong>$48.00</strong> — chegirmaning oʻzi.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>A line passes through the points (−5, 2) and (1, 20) in the '
                      '<i>xy</i>-plane. What is the slope of the line?</p>',
     'choices': ['1/3', '3', '6', '18'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Burchak koeffitsiyenti '
                    '(20 − 2) ÷ (1 − (−5)) = 18 ÷ 6 = 3. Maxrajdagi ikkita '
                    'minus qoʻshiluvga aylanadi: 1 + 5 = 6. <strong>18</strong> — '
                    'faqat suratni hisoblagan javob.'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>t</i> is defined by <i>t</i>(<i>x</i>) = 6 '
                      '− <i>x</i><sup>2</sup>. What is the value of '
                      '<i>t</i>(−4)?</p>',
     'choices': ['−10', '−2', '10', '22'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>−10</strong>. (−4)<sup>2</sup> = 16, '
                    'chunki manfiy sonning kvadrati musbat; keyin 6 − 16 = −10. '
                    '<strong>22</strong> — kvadratni −16 deb olib, '
                    '6 + 16 hisoblagan javob.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>A right triangle has legs of length 20 and 21. What is the length '
                      'of its hypotenuse?</p>',
     'choices': ['25', '29', '41', '841'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>29</strong>. Pifagor teoremasi boʻyicha '
                    '<i>c</i><sup>2</sup> = 400 + 441 = 841, demak <i>c</i> = 29. '
                    '<strong>41</strong> — ikki katetni shunchaki qoʻshgan javob: '
                    'gipotenuza yigʻindidan qisqa boʻladi.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p><i>x</i> − 2<i>y</i> = 4<br><i>x</i> = 3<i>y</i> − 1</p>'
                      '<p>The system of equations above has a unique solution. What is the '
                      'value of <i>y</i>?</p>',
     'choices': ['2', '4', '5', '14'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Ikkinchi tenglamadagi <i>x</i> ni '
                    'birinchisiga qoʻyamiz: (3<i>y</i> − 1) − 2<i>y</i> = 4, '
                    'yaʼni <i>y</i> − 1 = 4 va <i>y</i> = 5. <strong>14</strong> '
                    '— <i>x</i> ning qiymati.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>A recipe for 8 portions uses 600 grams of flour. At the same '
                      'rate, how many grams are needed for 14 portions?</p>',
     'choices': ['900', '1,050', '1,200', '1,400'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>1,050</strong>. Bir porsiyaga 600 ÷ 8 = 75 g '
                    'ketadi, demak 14 porsiyaga 75 × 14 = 1,050 g. Yoki proportsiya bilan: '
                    '600/8 = <i>x</i>/14.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>What is the negative solution to the equation '
                      '<i>x</i><sup>2</sup> − 3<i>x</i> − 40 = 0?</p>',
     'choices': ['−8', '−5', '5', '8'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>−5</strong>. Koʻpaytmasi −40, '
                    'yigʻindisi −3 boʻlgan ikki son — −8 va 5, demak '
                    '(<i>x</i> − 8)(<i>x</i> + 5) = 0 va ildizlar 8 hamda −5. '
                    '<strong>−8</strong> — koʻpaytuvchidagi sonning ishorasini '
                    'oʻzgartirmagan javob.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A van rental costs $45 plus $0.30 for each mile driven. Which '
                      'equation gives the total cost <i>C</i>, in dollars, for a rental of '
                      '<i>m</i> miles?</p>',
     'choices': [
         '<i>C</i> = 0.30<i>m</i> + 45',
         '<i>C</i> = 0.30(<i>m</i> + 45)',
         '<i>C</i> = 45<i>m</i> + 0.30',
         '<i>C</i> = 45.30<i>m</i>',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong><i>C</i> = 0.30<i>m</i> + 45</strong>. $0.30 '
                    'har bir milga tegishli, demak u <i>m</i> ga koʻpayadi; $45 esa bir '
                    'marta olinadi. <strong><i>C</i> = 45.30<i>m</i></strong> ikkalasini '
                    'ham milga bogʻlab yuboradi.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A circle has an area of 64π square units. What is its '
                      'circumference?</p>',
     'choices': ['8π', '16π', '32π', '64π'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>16π</strong>. Yuza '
                    'π<i>r</i><sup>2</sup> = 64π dan <i>r</i> = 8, aylana '
                    'uzunligi esa 2π<i>r</i> = 16π. <strong>8π</strong> '
                    '— radiusni topib, 2 ga koʻpaytirishni unutgan javob.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>A town of 5,000 people grows by 8% each year. Which function '
                      'gives the population <i>P</i> after <i>t</i> years?</p>',
     'choices': [
         '<i>P</i>(<i>t</i>) = 5,000(0.08)<sup><i>t</i></sup>',
         '<i>P</i>(<i>t</i>) = 5,000(0.92)<sup><i>t</i></sup>',
         '<i>P</i>(<i>t</i>) = 5,000(1.08)<sup><i>t</i></sup>',
         '<i>P</i>(<i>t</i>) = 5,000 + 1.08<i>t</i>',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong><i>P</i>(<i>t</i>) = 5,000(1.08)'
                    '<sup><i>t</i></sup></strong>. 8% oʻsish koʻpaytuvchini 1 + 0.08 = '
                    '1.08 qiladi. <strong><i>P</i>(<i>t</i>) = 5,000(0.92)'
                    '<sup><i>t</i></sup></strong> — aholini har yili 8% ga '
                    '<em>kamaytiradi</em>: oʻsish va kamayish koʻpaytuvchilarini '
                    'adashtirmang.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>What is the greatest integer value of <i>x</i> that satisfies '
                      'the inequality 8(<i>x</i> − 2) &lt; 7<i>x</i> + 3?</p>',
     'choices': ['17', '18', '19', '20'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>18</strong>. Qavsni ochamiz: 8<i>x</i> − 16 '
                    '&lt; 7<i>x</i> + 3, bundan <i>x</i> &lt; 19. Tengsizlik '
                    '<em>qatʼiy</em>, shuning uchun 19 ning oʻzi yaramaydi va eng katta '
                    'butun son 18. <strong>19</strong> aynan shu tuzoq.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>A set of 8 numbers has a mean of 22. One of the numbers, 15, is '
                      'removed. What is the mean of the remaining 7 numbers?</p>',
     'choices': ['21', '22', '23', '24'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>23</strong>. Yigʻindi 8 × 22 = 176; 15 ni olib '
                    'tashlasak 161 qoladi, va 161 ÷ 7 = 23. <strong>22</strong> — '
                    'eski oʻrtachaning oʻzi: olib tashlangan son oʻrtachadan past boʻlgani '
                    'uchun qolganlarning oʻrtachasi koʻtariladi.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If <i>x</i><sup>2</sup> − 22<i>x</i> + <i>c</i> is the '
                      'square of a binomial, what is the value of the constant '
                      '<i>c</i>?</p>',
     'choices': ['11', '44', '121', '484'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>121</strong>. (<i>x</i> − <i>a</i>)'
                    '<sup>2</sup> = <i>x</i><sup>2</sup> − 2<i>ax</i> + '
                    '<i>a</i><sup>2</sup>, demak 2<i>a</i> = 22, <i>a</i> = 11 va '
                    '<i>c</i> = 121. <strong>484</strong> — 22 ni kvadratga '
                    'koʻtargan javob: avval ikkiga boʻlish kerak.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, the graph of 4<i>x</i> + <i>ky</i> = 16 '
                      'is perpendicular to the graph of <i>y</i> = 2<i>x</i> − 9, '
                      'where <i>k</i> is a constant. What is the value of <i>k</i>?</p>',
     'choices': ['−8', '−2', '2', '8'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Perpendikulyar chiziqning '
                    'koeffitsiyenti — manfiy teskari son: 2 ning teskarisi ½, '
                    'manfiysi −½. Endi 4<i>x</i> + <i>ky</i> = 16 dan koeffitsiyent '
                    '−4/<i>k</i>, va −4/<i>k</i> = −½ dan <i>k</i> = 8. '
                    '<strong>−8</strong> — minusni ikki marta hisobga olgan '
                    'javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>ABC</i> below, angle <i>B</i> is a right '
                      'angle, <i>AB</i> = 16 and <i>BC</i> = 30. What is the value of '
                      'tan <i>A</i>?</p>'
                      '<svg viewBox="0 0 200 135" width="210" height="142" role="img" '
                      'aria-label="Right triangle ABC with the right angle at B">'
                      '<polygon points="24,112 24,28 174,112" fill="none" '
                      'stroke="currentColor" stroke-width="2"/>'
                      '<rect x="24" y="98" width="14" height="14" fill="none" '
                      'stroke="currentColor" stroke-width="1.5"/>'
                      '<text x="12" y="24" font-size="13" fill="currentColor">A</text>'
                      '<text x="10" y="126" font-size="13" fill="currentColor">B</text>'
                      '<text x="176" y="126" font-size="13" fill="currentColor">C</text>'
                      '<text x="30" y="74" font-size="12" fill="currentColor">16</text>'
                      '<text x="94" y="128" font-size="12" fill="currentColor">30</text>'
                      '</svg>',
     'choices': ['8/17', '8/15', '15/17', '15/8'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>15/8</strong>. Tangens gipotenuzani talab '
                    'qilmaydi: tan <i>A</i> = (<i>A</i> ga qarshi katet) ÷ (yondosh katet) '
                    '= <i>BC</i>/<i>AB</i> = 30/16 = 15/8. <strong>15/17</strong> — '
                    'bu sin <i>A</i>: gipotenuzani (34) hisoblab, uni maxrajga qoʻyib '
                    'yuborgan javob.'},

    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '(<i>x</i> + 5)(<i>x</i> − 1). In the <i>xy</i>-plane, the '
                      'graph of <i>y</i> = <i>f</i>(<i>x</i>) has its vertex at the point '
                      '(<i>h</i>, <i>k</i>). What is the value of <i>k</i>?</p>',
     'choices': ['−9', '−5', '−4', '1'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>−9</strong>. Nollar <i>x</i> = −5 va '
                    '<i>x</i> = 1, demak uchning abssissasi oʻrta nuqta: '
                    '(−5 + 1) ÷ 2 = −2. Endi <i>k</i> = <i>f</i>(−2) = '
                    '(3)(−3) = −9. <strong>−5</strong> — '
                    'koʻpaytuvchidagi sonni javob deb olgan javob.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 5(<i>x</i> − 6) = 2<i>x</i> + 9, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['13'],
     'explanation': 'Toʻgʻri javob <strong>13</strong>. Qavsni ochamiz: 5<i>x</i> − 30 '
                    '= 2<i>x</i> + 9. 2<i>x</i> ni ayirib, 30 ni qoʻshamiz: 3<i>x</i> = '
                    '39, demak <i>x</i> = 13. Tekshirish: 5 × 7 = 35 va 2 × 13 + 9 = 35.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>In a survey of 450 people, 62% said that they own a bicycle. How '
                      'many of the people surveyed own a bicycle?</p>' + GRID_NOTE,
     'accepted': ['279'],
     'explanation': 'Toʻgʻri javob <strong>279</strong>. 450 × 0.62 = 279. Boshqacha '
                    'hisoblash: 10% = 45, demak 60% = 270; 1% = 4.5, demak 2% = 9; '
                    '270 + 9 = 279.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 2<sup><i>x</i></sup> = 1/32, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['-5'],
     'explanation': 'Toʻgʻri javob <strong>−5</strong>. 32 = 2<sup>5</sup>, demak '
                    '1/32 = 2<sup>−5</sup>. Manfiy daraja kasrni bildiradi — '
                    'minus ishorasi ham javob qutichasiga kiradi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>A line passes through the points (0, 8) and (6, −4) in the '
                      '<i>xy</i>-plane. What is the slope of the line?</p>' + GRID_NOTE,
     'accepted': ['-2'],
     'explanation': 'Toʻgʻri javob <strong>−2</strong>. Burchak koeffitsiyenti '
                    '(−4 − 8) ÷ (6 − 0) = −12 ÷ 6 = −2. '
                    '<i>y</i> kamayganda koeffitsiyent manfiy boʻladi — minus '
                    'ishorasi ham javobga kiradi.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> + 14<i>x</i> + 53. What is the minimum value '
                      'of <i>f</i>(<i>x</i>)?</p>' + GRID_NOTE,
     'accepted': ['4'],
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Parabola yuqoriga ochilgani uchun '
                    'eng kichik qiymat uch nuqtasida. Uchning abssissasi <i>x</i> = '
                    '−14 ÷ 2 = −7, qiymati esa <i>f</i>(−7) = 49 − 98 '
                    '+ 53 = 4. <strong>−7</strong> yozib yuborish oson — u '
                    'uchning <i>x</i> i.'},
]
