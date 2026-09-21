# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 3 · Math, Module 1
#  22 questions · 35 minutes · every taker sits this one.
#  Questions 18–22 are student-produced responses (grid-ins).
#  Route: 14 or more correct here sends the taker to the UPPER module 2.
#
#  Load: python manage.py load_mock exam/data/sat3_math1.py --expect-questions=22
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

S = 'math1'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 4<i>x</i> + 9 = 33, what is the value of <i>x</i>?</p>',
     'choices': ['6', '8', '10', '24'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Ikki tomondan 9 ni ayiramiz: '
                    '4<i>x</i> = 24, soʻng 4 ga boʻlamiz: <i>x</i> = 6. '
                    '<strong>24</strong> — 4<i>x</i> ning qiymati, yaʼni oxirgi '
                    'boʻlish qolib ketgan.'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>A jacket is marked down from $80.00 to $68.00. What is the '
                      'percent decrease in the price?</p>',
     'choices': ['12%', '15%', '18%', '85%'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>15%</strong>. Pasayish 80 − 68 = $12, '
                    'foizi esa 12 ÷ 80 = 0.15 = 15%. Maxraj har doim <em>asl</em> narx. '
                    '<strong>12%</strong> — pasayish summasini foiz deb olgan javob.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>A line passes through the points (1, −2) and (5, 10) in the '
                      '<i>xy</i>-plane. What is the slope of the line?</p>',
     'choices': ['1/3', '3', '4', '12'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Burchak koeffitsiyenti — '
                    '(10 − (−2)) ÷ (5 − 1) = 12 ÷ 4 = 3. Ayirmadagi ikkita '
                    'minus qoʻshiluvga aylanadi: 10 + 2 = 12. <strong>12</strong> — '
                    'faqat suratni hisoblab, boʻlishni unutgan javob.'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>p</i> is defined by <i>p</i>(<i>x</i>) = 5 '
                      '− 2<i>x</i><sup>2</sup>. What is the value of '
                      '<i>p</i>(3)?</p>',
     'choices': ['−31', '−13', '13', '31'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>−13</strong>. Avval daraja: '
                    '3<sup>2</sup> = 9, keyin 2 × 9 = 18, va 5 − 18 = −13. '
                    '<strong>13</strong> — ayirishni teskari yoʻnalishda '
                    '(18 − 5) qilgan javob: amallar tartibini buzmang.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>Three angles of a quadrilateral measure 85°, 95° and '
                      '110°. What is the measure of the fourth angle?</p>',
     'choices': ['70°', '80°', '90°', '110°'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>70°</strong>. Toʻrtburchak burchaklari '
                    'yigʻindisi 360°, demak 360 − (85 + 95 + 110) = 360 − '
                    '290 = 70°. <strong>90°</strong> — yigʻindini '
                    '180° deb olgan javob: 180° uchburchakka tegishli.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>3<i>x</i> + <i>y</i> = 17<br><i>y</i> = 2<i>x</i> − 3</p>'
                      '<p>The system of equations above has a unique solution. What is the '
                      'value of <i>x</i>?</p>',
     'choices': ['2', '4', '5', '7'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Ikkinchi tenglamadagi <i>y</i> ni '
                    'birinchisiga qoʻyamiz: 3<i>x</i> + (2<i>x</i> − 3) = 17, yaʼni '
                    '5<i>x</i> = 20 va <i>x</i> = 4. <strong>5</strong> — <i>y</i> '
                    'ning qiymati: qaysi nomaʼlum soʻralganini oxirida tekshiring.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>A car uses 6 litres of fuel for every 100 kilometres it travels. '
                      'At this rate, how many litres will it use over 350 kilometres?</p>',
     'choices': ['18', '21', '24', '58'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>21</strong>. Har 100 km ga 6 litr, demak 350 km '
                    'ga 6 × 3.5 = 21 litr. Yoki proportsiya bilan: 6/100 = <i>x</i>/350. '
                    '<strong>58</strong> — 350 ÷ 6 ni yaxlitlagan javob: boʻlish '
                    'yoʻnalishini birlik bilan tekshiring.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>What is the sum of the solutions to the equation '
                      '<i>x</i><sup>2</sup> − 9<i>x</i> + 20 = 0?</p>',
     'choices': ['−20', '−9', '9', '20'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. (<i>x</i> − 4)(<i>x</i> '
                    '− 5) = 0 dan ildizlar 4 va 5, yigʻindisi 9. Tezroq yoʻl: '
                    '<i>x</i><sup>2</sup> + <i>bx</i> + <i>c</i> da ildizlar yigʻindisi '
                    '−<i>b</i>. <strong>20</strong> — ildizlarning '
                    '<em>koʻpaytmasi</em>.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A pool contains 500 litres of water and is drained at a constant '
                      'rate of 25 litres per minute. Which equation gives the volume '
                      '<i>V</i>, in litres, remaining after <i>m</i> minutes?</p>',
     'choices': [
         '<i>V</i> = 25<i>m</i> − 500',
         '<i>V</i> = 500 − 25<i>m</i>',
         '<i>V</i> = 500<i>m</i> − 25',
         '<i>V</i> = 525 − <i>m</i>',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>V</i> = 500 − 25<i>m</i></strong>. '
                    'Boshlangʻich hajm 500 oʻzgarmas qoʻshiluvchi, har daqiqada esa 25 '
                    'litr <em>kamayadi</em>, demak 25<i>m</i> ayiriladi. '
                    '<strong><i>V</i> = 25<i>m</i> − 500</strong> ishoralarni '
                    'almashtiradi va manfiy hajm beradi.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A cube has a volume of 125 cubic units. What is its total '
                      'surface area?</p>',
     'choices': ['25', '75', '150', '750'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>150</strong>. Hajmi 125 boʻlgan kubning qirrasi '
                    '∛125 = 5; bitta yogʻining yuzi 5<sup>2</sup> = 25, yoqlar esa '
                    'oltita: 6 × 25 = 150. <strong>25</strong> — bitta yoq: kubning '
                    'oltita yogʻi borligini unutmang.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>An investment of $2,000 increases in value by 5% each year. '
                      'Which function gives the value <i>V</i>, in dollars, after <i>t</i> '
                      'years?</p>',
     'choices': [
         '<i>V</i>(<i>t</i>) = 2,000(0.05)<sup><i>t</i></sup>',
         '<i>V</i>(<i>t</i>) = 2,000(1.05)<sup><i>t</i></sup>',
         '<i>V</i>(<i>t</i>) = 2,000(5)<sup><i>t</i></sup>',
         '<i>V</i>(<i>t</i>) = 2,000 + 1.05<i>t</i>',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>V</i>(<i>t</i>) = 2,000(1.05)'
                    '<sup><i>t</i></sup></strong>. 5% oʻsish koʻpaytuvchini 1 + 0.05 = '
                    '1.05 qiladi. <strong><i>V</i>(<i>t</i>) = 2,000(0.05)'
                    '<sup><i>t</i></sup></strong> eng keng tarqalgan xato: u har yili '
                    'summani 95% ga <em>kamaytiradi</em>, yaʼni deyarli hammasini yoʻqotadi.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>What is the greatest integer value of <i>x</i> that satisfies '
                      'the inequality 5(<i>x</i> − 3) ≤ 4<i>x</i> + 2?</p>',
     'choices': ['15', '16', '17', '18'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>17</strong>. Qavsni ochamiz: 5<i>x</i> − 15 '
                    '≤ 4<i>x</i> + 2, bundan <i>x</i> ≤ 17. Tengsizlik qatʼiy '
                    'emas (≤), shuning uchun 17 ning oʻzi ham yaraydi. '
                    '<strong>16</strong> — "≤" ni "&lt;" deb oʻqigan javob.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>The mean of six numbers is 9. Five of the numbers are 4, 7, 8, 11 '
                      'and 13. What is the sixth number?</p>',
     'choices': ['9', '10', '11', '12'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>11</strong>. Oʻrta arifmetik 9 boʻlsa, oltita '
                    'sonning yigʻindisi 6 × 9 = 54. Berilgan beshtasining yigʻindisi '
                    '4 + 7 + 8 + 11 + 13 = 43, demak oltinchisi 54 − 43 = 11. '
                    'Oʻrtacha masalasida har doim avval <em>yigʻindini</em> tiklang.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If <i>x</i><sup>2</sup> + <i>bx</i> + 49 is the square of a '
                      'binomial and <i>b</i> &gt; 0, what is the value of <i>b</i>?</p>',
     'choices': ['7', '14', '21', '49'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>14</strong>. (<i>x</i> + <i>a</i>)<sup>2</sup> '
                    '= <i>x</i><sup>2</sup> + 2<i>ax</i> + <i>a</i><sup>2</sup>, va '
                    '<i>a</i><sup>2</sup> = 49 dan <i>a</i> = 7 (musbat shart boʻyicha), '
                    'demak <i>b</i> = 2<i>a</i> = 14. <strong>7</strong> — <i>a</i> '
                    'ning oʻzi: savol <i>b</i> ni soʻraydi.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, the graph of 2<i>x</i> + <i>ky</i> = 10 '
                      'is parallel to the graph of <i>y</i> = −4<i>x</i> + 1, where '
                      '<i>k</i> is a constant. What is the value of <i>k</i>?</p>',
     'choices': ['−2', '−1/2', '1/2', '2'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>1/2</strong>. 2<i>x</i> + <i>ky</i> = 10 ni '
                    '<i>y</i> ga nisbatan yechamiz: <i>y</i> = (10 − 2<i>x</i>) ÷ '
                    '<i>k</i>, burchak koeffitsiyenti −2/<i>k</i>. Parallellik uni '
                    '−4 ga tenglaydi: −2/<i>k</i> = −4, demak <i>k</i> = '
                    '1/2. <strong>−1/2</strong> — ikkita minusni bir marta '
                    'ortiqcha hisobga olgan javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>ABC</i> below, angle <i>B</i> is a right '
                      'angle, <i>AB</i> = 20 and <i>BC</i> = 21. What is the value of '
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
                      '<text x="30" y="74" font-size="12" fill="currentColor">20</text>'
                      '<text x="92" y="128" font-size="12" fill="currentColor">21</text>'
                      '</svg>',
     'choices': ['20/29', '21/29', '20/21', '21/20'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>21/20</strong>. Tangens gipotenuzani talab '
                    'qilmaydi: tan <i>A</i> = (<i>A</i> ga qarshi katet) ÷ (yondosh katet) '
                    '= <i>BC</i>/<i>AB</i> = 21/20. <strong>21/29</strong> — bu '
                    'sin <i>A</i>: gipotenuzani (√(400 + 441) = 29) hisoblab, uni '
                    'maxrajga qoʻyib yuborgan javob.'},

    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '(<i>x</i> − 1)(<i>x</i> − 11). In the <i>xy</i>-plane, '
                      'the graph of <i>y</i> = <i>f</i>(<i>x</i>) has its vertex at the '
                      'point (<i>h</i>, <i>k</i>). What is the value of <i>k</i>?</p>',
     'choices': ['−30', '−25', '−11', '6'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>−25</strong>. Nollar <i>x</i> = 1 va '
                    '<i>x</i> = 11; parabola ular orasida simmetrik, demak <i>h</i> = '
                    '(1 + 11) ÷ 2 = 6. Endi <i>k</i> = <i>f</i>(6) = (5)(−5) = '
                    '−25. <strong>6</strong> — uchning <i>x</i> koordinatasi: '
                    'savol <i>k</i> ni, yaʼni <i>y</i> ni soʻraydi.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 9(<i>x</i> − 4) = 6<i>x</i> + 3, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['13'],
     'explanation': 'Toʻgʻri javob <strong>13</strong>. Qavsni ochamiz: 9<i>x</i> − 36 '
                    '= 6<i>x</i> + 3. 6<i>x</i> ni ayirib, 36 ni qoʻshamiz: 3<i>x</i> = '
                    '39, demak <i>x</i> = 13. Tekshirish: 9 × 9 = 81 va 6 × 13 + 3 = 81.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>A shop sold 45 items on Monday, which was 30% of the total it '
                      'sold that week. How many items did the shop sell that week?</p>'
                      + GRID_NOTE,
     'accepted': ['150'],
     'explanation': 'Toʻgʻri javob <strong>150</strong>. 30% = 45 boʻlsa, 1% = 45 ÷ 30 = '
                    '1.5, demak 100% = 150. Yoki tenglama bilan: 0.30<i>T</i> = 45. '
                    'Bu yerda butun son <em>soʻralayotgan</em> kattalik — 45 emas.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 4<sup><i>x</i></sup> = 256, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['4'],
     'explanation': 'Toʻgʻri javob <strong>4</strong>. 4 × 4 = 16, 16 × 4 = 64, '
                    '64 × 4 = 256 — toʻrtta koʻpaytiruvchi, demak 256 = '
                    '4<sup>4</sup> va <i>x</i> = 4.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>A line passes through the points (2, 9) and (6, 1) in the '
                      '<i>xy</i>-plane. What is the <i>y</i>-coordinate of its '
                      '<i>y</i>-intercept?</p>' + GRID_NOTE,
     'accepted': ['13'],
     'explanation': 'Toʻgʻri javob <strong>13</strong>. Burchak koeffitsiyenti '
                    '(1 − 9) ÷ (6 − 2) = −8 ÷ 4 = −2. Endi (2, 9) ni '
                    '<i>y</i> = −2<i>x</i> + <i>b</i> ga qoʻyamiz: 9 = −4 + '
                    '<i>b</i>, demak <i>b</i> = 13.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> + 6<i>x</i> + 11. What is the minimum value '
                      'of <i>f</i>(<i>x</i>)?</p>' + GRID_NOTE,
     'accepted': ['2'],
     'explanation': 'Toʻgʻri javob <strong>2</strong>. Parabola yuqoriga ochilgani uchun '
                    'eng kichik qiymat uch nuqtasida. Uchning abssissasi <i>x</i> = '
                    '−6 ÷ 2 = −3, qiymati esa <i>f</i>(−3) = 9 − 18 + '
                    '11 = 2. <strong>−3</strong> yozib yuborish oson — u uchning '
                    '<i>x</i> i, savol esa qiymatni soʻraydi.'},
]
