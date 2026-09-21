# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 4 · Math, Module 1
#  22 questions · 35 minutes · every taker sits this one.
#  Questions 18–22 are student-produced responses (grid-ins).
#  Route: 14 or more correct here sends the taker to the UPPER module 2.
#
#  Load: python manage.py load_mock exam/data/sat4_math1.py --expect-questions=22
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

S = 'math1'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>If 7<i>x</i> − 4 = 31, what is the value of <i>x</i>?</p>',
     'choices': ['4', '5', '7', '27'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Ikki tomonga 4 ni qoʻshamiz: '
                    '7<i>x</i> = 35, soʻng 7 ga boʻlamiz: <i>x</i> = 5. '
                    '<strong>27</strong> — 4 ni qoʻshish oʻrniga ayirgan javob '
                    '(31 − 4).'},

    {'section': S, 'number': 2, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'easy',
     'question_text': '<p>A book costs $24.00. Its price then rises by 12.5%. What is the '
                      'new price?</p>',
     'choices': ['$3.00', '$26.40', '$27.00', '$36.00'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>$27.00</strong>. 12.5% — sakkizdan bir, '
                    'demak oʻsish 24 ÷ 8 = $3.00 va yangi narx 24 + 3 = $27.00. '
                    '<strong>$3.00</strong> — oʻsishning oʻzi: savol yangi narxni '
                    'soʻraydi.'},

    {'section': S, 'number': 3, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>A line passes through the points (−2, 9) and (4, −3) in '
                      'the <i>xy</i>-plane. What is the slope of the line?</p>',
     'choices': ['−2', '−1/2', '1/2', '2'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>−2</strong>. Burchak koeffitsiyenti '
                    '(−3 − 9) ÷ (4 − (−2)) = −12 ÷ 6 = −2. '
                    '<strong>2</strong> — minus ishorasini tushirib qoldirgan javob: '
                    '<i>y</i> kamayganda koeffitsiyent manfiy boʻladi.'},

    {'section': S, 'number': 4, 'skill': 'Advanced Math', 'difficulty': 'easy',
     'question_text': '<p>The function <i>r</i> is defined by <i>r</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> − 5<i>x</i>. What is the value of '
                      '<i>r</i>(−2)?</p>',
     'choices': ['−14', '−6', '6', '14'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>14</strong>. (−2)<sup>2</sup> = 4 va '
                    '−5 × (−2) = +10, demak 4 + 10 = 14. '
                    '<strong>−6</strong> — ikkinchi hadning ishorasini '
                    'almashtirmagan javob (4 − 10): manfiy songa manfiyni '
                    'koʻpaytirsangiz, musbat chiqadi.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'easy',
     'question_text': '<p>A parallelogram has a base of 15 units and a height of 8 units. '
                      'What is its area?</p>',
     'choices': ['23', '46', '60', '120'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>120</strong>. Parallelogramm yuzasi — '
                    'asos × balandlik = 15 × 8 = 120. <strong>60</strong> — '
                    'uchburchak formulasini (½bh) qoʻllagan javob: parallelogrammda ikkiga '
                    'boʻlinmaydi.'},

    {'section': S, 'number': 6, 'skill': 'Algebra', 'difficulty': 'easy',
     'question_text': '<p>2<i>x</i> − <i>y</i> = 9<br><i>y</i> = <i>x</i> − 4</p>'
                      '<p>The system of equations above has a unique solution. What is the '
                      'value of <i>y</i>?</p>',
     'choices': ['1', '3', '5', '9'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>1</strong>. Ikkinchi tenglamadagi <i>y</i> ni '
                    'birinchisiga qoʻyamiz: 2<i>x</i> − (<i>x</i> − 4) = 9, '
                    'yaʼni <i>x</i> + 4 = 9 va <i>x</i> = 5; demak <i>y</i> = 5 − 4 = '
                    '1. <strong>5</strong> — <i>x</i> ning qiymati.'},

    {'section': S, 'number': 7, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>A machine fills 240 bottles in 8 minutes. At this rate, how many '
                      'bottles will it fill in 25 minutes?</p>',
     'choices': ['600', '720', '750', '800'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>750</strong>. Tezlik 240 ÷ 8 = 30 shisha/daqiqa, '
                    'demak 30 × 25 = 750. Yoki proportsiya bilan: 240/8 = <i>x</i>/25.'},

    {'section': S, 'number': 8, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>What is the negative solution to the equation '
                      '<i>x</i><sup>2</sup> + 2<i>x</i> − 35 = 0?</p>',
     'choices': ['−7', '−5', '5', '7'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>−7</strong>. Koʻpaytmasi −35, '
                    'yigʻindisi 2 boʻlgan ikki son — 7 va −5, demak '
                    '(<i>x</i> + 7)(<i>x</i> − 5) = 0 va ildizlar −7 hamda 5. '
                    '<strong>−5</strong> — koʻpaytuvchidagi sonlarning '
                    'ishorasini almashtirib olgan javob.'},

    {'section': S, 'number': 9, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>A tank already holds 20 litres of water and is filled at a '
                      'constant rate of 3 litres per minute. Which equation gives the '
                      'volume <i>V</i>, in litres, after <i>m</i> minutes?</p>',
     'choices': [
         '<i>V</i> = 3<i>m</i> + 20',
         '<i>V</i> = 3(<i>m</i> + 20)',
         '<i>V</i> = 20<i>m</i> + 3',
         '<i>V</i> = 23<i>m</i>',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong><i>V</i> = 3<i>m</i> + 20</strong>. Har '
                    'daqiqada 3 litr qoʻshiladi, demak u <i>m</i> ga koʻpayadi; 20 litr '
                    'esa boshidan bor, demak oʻzgarmas qoʻshiluvchi. <strong><i>V</i> = '
                    '23<i>m</i></strong> boshlangʻich hajmni ham har daqiqaga qoʻshib '
                    'yuboradi.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A circle has a circumference of 18π units. What is the area '
                      'of the circle?</p>',
     'choices': ['9π', '18π', '81π', '324π'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>81π</strong>. 2π<i>r</i> = 18π '
                    'dan <i>r</i> = 9, yuza esa π<i>r</i><sup>2</sup> = 81π. '
                    '<strong>324π</strong> — radius oʻrniga diametrni (18) '
                    'kvadratga koʻtargan javob.'},

    {'section': S, 'number': 11, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>A car worth $18,000 loses 20% of its value each year. Which '
                      'function gives its value <i>V</i>, in dollars, after <i>t</i> '
                      'years?</p>',
     'choices': [
         '<i>V</i>(<i>t</i>) = 18,000(0.2)<sup><i>t</i></sup>',
         '<i>V</i>(<i>t</i>) = 18,000(0.8)<sup><i>t</i></sup>',
         '<i>V</i>(<i>t</i>) = 18,000(1.2)<sup><i>t</i></sup>',
         '<i>V</i>(<i>t</i>) = 18,000 − 0.2<i>t</i>',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong><i>V</i>(<i>t</i>) = 18,000(0.8)'
                    '<sup><i>t</i></sup></strong>. Har yili 20% yoʻqolsa, 80% '
                    '<em>qoladi</em>, demak koʻpaytuvchi 0.8. '
                    '<strong><i>V</i>(<i>t</i>) = 18,000(0.2)<sup><i>t</i></sup></strong> '
                    'eng keng tarqalgan xato: u har yili qiymatning beshdan toʻrtini emas, '
                    'toʻrtdan beshini yoʻqotadi.'},

    {'section': S, 'number': 12, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>What is the greatest integer value of <i>x</i> that satisfies '
                      'the inequality 6(<i>x</i> − 2) &lt; 5<i>x</i> + 4?</p>',
     'choices': ['14', '15', '16', '17'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>15</strong>. Qavsni ochamiz: 6<i>x</i> − 12 '
                    '&lt; 5<i>x</i> + 4, bundan <i>x</i> &lt; 16. Tengsizlik '
                    '<em>qatʼiy</em>, shuning uchun 16 ning oʻzi yaramaydi va eng katta '
                    'butun son 15. <strong>16</strong> aynan shu tuzoq.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'question_text': '<p>What is the median of the data set 3, 8, 8, 10, 11, 14?</p>',
     'choices': ['8', '9', '9.5', '10'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Sonlar juft (oltita), demak mediana '
                    '— oʻrtadagi ikki sonning oʻrtachasi: (8 + 10) ÷ 2 = 9. '
                    '<strong>8</strong> — uchinchi sonni mediana deb olgan javob: '
                    'juft sonlarda oʻrtada bitta emas, ikkita son turadi.'},

    {'section': S, 'number': 14, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'question_text': '<p>If <i>x</i><sup>2</sup> − 16<i>x</i> + <i>c</i> is the '
                      'square of a binomial, what is the value of the constant '
                      '<i>c</i>?</p>',
     'choices': ['4', '8', '32', '64'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>64</strong>. (<i>x</i> − <i>a</i>)'
                    '<sup>2</sup> = <i>x</i><sup>2</sup> − 2<i>ax</i> + '
                    '<i>a</i><sup>2</sup>, demak 2<i>a</i> = 16, <i>a</i> = 8 va '
                    '<i>c</i> = 8<sup>2</sup> = 64. <strong>8</strong> — <i>a</i> '
                    'ning oʻzi: savol <i>c</i> ni soʻraydi.'},

    {'section': S, 'number': 15, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, the graph of 5<i>x</i> + <i>ky</i> = 20 '
                      'is perpendicular to the graph of <i>y</i> = ⅓<i>x</i> + 2, '
                      'where <i>k</i> is a constant. What is the value of <i>k</i>?</p>',
     'choices': ['−5/3', '−3/5', '3/5', '5/3'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>5/3</strong>. Perpendikulyar chiziqning '
                    'koeffitsiyenti — manfiy teskari son: ⅓ ning teskarisi 3, '
                    'manfiysi −3. Endi 5<i>x</i> + <i>ky</i> = 20 dan koeffitsiyent '
                    '−5/<i>k</i>, va −5/<i>k</i> = −3 dan <i>k</i> = 5/3. '
                    '<strong>−5/3</strong> — minusni ikki marta hisobga olgan '
                    'javob.'},

    {'section': S, 'number': 16, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>ABC</i> below, angle <i>B</i> is a right '
                      'angle, <i>AB</i> = 7 and <i>BC</i> = 24. What is the value of '
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
                      '<text x="30" y="74" font-size="12" fill="currentColor">7</text>'
                      '<text x="94" y="128" font-size="12" fill="currentColor">24</text>'
                      '</svg>',
     'choices': ['7/25', '7/24', '24/25', '24/7'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>24/25</strong>. Avval gipotenuza: '
                    '<i>AC</i><sup>2</sup> = 7<sup>2</sup> + 24<sup>2</sup> = 49 + 576 = '
                    '625, demak <i>AC</i> = 25. sin <i>A</i> = (<i>A</i> ga qarshi katet) '
                    '÷ gipotenuza = <i>BC</i>/<i>AC</i> = 24/25. <strong>7/25</strong> '
                    '— bu cos <i>A</i>: yondosh katetni olgan javob.'},

    {'section': S, 'number': 17, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '(<i>x</i> + 3)(<i>x</i> − 9). In the <i>xy</i>-plane, the '
                      'graph of <i>y</i> = <i>f</i>(<i>x</i>) has its vertex at the point '
                      '(<i>h</i>, <i>k</i>). What is the value of <i>h</i>?</p>',
     'choices': ['−3', '3', '6', '9'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Nollar <i>x</i> = −3 va '
                    '<i>x</i> = 9; parabola ular orasida simmetrik, demak uchning '
                    'abssissasi oʻrta nuqta: (−3 + 9) ÷ 2 = 3. <strong>6</strong> '
                    'aynan shu savolning tuzogʻi: ishorani tashlab, (3 + 9) ÷ 2 = 6 deb '
                    'hisoblash.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 8(<i>x</i> − 5) = 5<i>x</i> + 8, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['16'],
     'explanation': 'Toʻgʻri javob <strong>16</strong>. Qavsni ochamiz: 8<i>x</i> − 40 '
                    '= 5<i>x</i> + 8. 5<i>x</i> ni ayirib, 40 ni qoʻshamiz: 3<i>x</i> = '
                    '48, demak <i>x</i> = 16. Tekshirish: 8 × 11 = 88 va 5 × 16 + 8 = 88.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>In a survey of 320 people, 45% said that they prefer tea. How '
                      'many of the people surveyed said that they prefer tea?</p>'
                      + GRID_NOTE,
     'accepted': ['144'],
     'explanation': 'Toʻgʻri javob <strong>144</strong>. 320 × 0.45 = 144. Boshqacha '
                    'hisoblash: 10% = 32, demak 40% = 128; 5% = 16; 128 + 16 = 144.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>If 3<sup><i>x</i></sup> = 1/9, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['-2'],
     'explanation': 'Toʻgʻri javob <strong>−2</strong>. 9 = 3<sup>2</sup>, demak '
                    '1/9 = 3<sup>−2</sup>. Asoslar teng boʻlgani uchun darajalar ham '
                    'teng. Manfiy daraja kasrni bildiradi — minus ishorasi ham javob '
                    'qutichasiga kiradi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'medium',
     'answer_type': 'grid',
     'question_text': '<p>A line passes through the points (0, −4) and (5, 11) in the '
                      '<i>xy</i>-plane. What is the slope of the line?</p>' + GRID_NOTE,
     'accepted': ['3'],
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Burchak koeffitsiyenti '
                    '(11 − (−4)) ÷ (5 − 0) = 15 ÷ 5 = 3. Ayirmadagi '
                    'ikkita minus qoʻshiluvga aylanadi: 11 + 4 = 15.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> + 10<i>x</i> + 29. What is the minimum value '
                      'of <i>f</i>(<i>x</i>)?</p>' + GRID_NOTE,
     'accepted': ['4'],
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Parabola yuqoriga ochilgani uchun '
                    'eng kichik qiymat uch nuqtasida. Uchning abssissasi <i>x</i> = '
                    '−10 ÷ 2 = −5, qiymati esa <i>f</i>(−5) = 25 − 50 '
                    '+ 29 = 4. <strong>−5</strong> yozib yuborish oson — u '
                    'uchning <i>x</i> i, savol esa qiymatni soʻraydi.'},
]
