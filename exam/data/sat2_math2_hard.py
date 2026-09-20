# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 2 · Math, Module 2 (UPPER)
#  22 questions · 35 minutes · taken by a pupil who scored 14 or more on math1.
#  Questions 18–22 are student-produced responses (grid-ins).
#
#  Load: python manage.py load_mock exam/data/sat2_math2_hard.py --expect-questions=22
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

S = 'math2h'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>If 5(2<i>x</i> − 3) = 3<i>x</i> + 20, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['3', '5', '7', '35'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Qavsni ochamiz: 10<i>x</i> − 15 '
                    '= 3<i>x</i> + 20. 3<i>x</i> ni ayirib, 15 ni qoʻshamiz: 7<i>x</i> = '
                    '35, demak <i>x</i> = 5. <strong>35</strong> — 7<i>x</i> ning '
                    'qiymati, yaʼni oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 2, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> + 2<i>x</i>. Which expression is equivalent to '
                      '<i>f</i>(<i>x</i> − 1) − <i>f</i>(<i>x</i>)?</p>',
     'choices': [
         '−2<i>x</i> − 1',
         '−2<i>x</i> + 1',
         '2<i>x</i> − 1',
         '2<i>x</i> + 1',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>−2<i>x</i> − 1</strong>. '
                    '<i>f</i>(<i>x</i>−1) = (<i>x</i>−1)<sup>2</sup> + '
                    '2(<i>x</i>−1) = <i>x</i><sup>2</sup> − 2<i>x</i> + 1 + '
                    '2<i>x</i> − 2 = <i>x</i><sup>2</sup> − 1. Undan '
                    '<i>f</i>(<i>x</i>) = <i>x</i><sup>2</sup> + 2<i>x</i> ni ayiramiz: '
                    '(<i>x</i><sup>2</sup> − 1) − (<i>x</i><sup>2</sup> + '
                    '2<i>x</i>) = −2<i>x</i> − 1. <strong>2<i>x</i> − '
                    '1</strong> — ayirishda qavsdagi ikkala aʼzoning ishorasini '
                    'almashtirmagan javob.'},

    {'section': S, 'number': 3, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>The price of an item is reduced by 25%. The reduced price is then '
                      'increased by 25%. The final price is what percent of the original '
                      'price?</p>',
     'choices': ['87.5%', '93.75%', '100%', '106.25%'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>93.75%</strong>. Foiz har safar <em>joriy</em> '
                    'narxdan olinadi: 0.75 × 1.25 = 0.9375, yaʼni 93.75%. '
                    '<strong>100%</strong> eng koʻp tanlanadigan javob — '
                    '"−25% va +25% bir-birini yoʻqotadi" degan tuygʻu; aslida '
                    'ikkinchi 25% kichikroq sondan olinadi, shuning uchun narx tiklanmaydi.'},

    {'section': S, 'number': 4, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>3<i>x</i> + 2<i>y</i> = 16<br><i>x</i> − 2<i>y</i> = 0</p>'
                      '<p>The system of equations above has a unique solution. What is the '
                      'value of <i>x</i>?</p>',
     'choices': ['2', '4', '6', '8'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Ikki tenglamani qoʻshsak '
                    '<i>y</i> qisqaradi: 4<i>x</i> = 16, demak <i>x</i> = 4. '
                    '<strong>2</strong> — <i>y</i> ning qiymati (chunki <i>x</i> = '
                    '2<i>y</i>): qaysi nomaʼlum soʻralganini oxirida tekshiring.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A right circular cone has a radius of 3 units and a height of 8 '
                      'units. What is its volume?</p>',
     'choices': ['8π', '24π', '72π', '216π'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>24π</strong>. Konus hajmi — '
                    '⅓π<i>r</i><sup>2</sup><i>h</i> = ⅓ × π × 9 × 8 = '
                    '24π. <strong>72π</strong> — ⅓ ni unutgan javob: '
                    'u silindrning hajmi.'},

    {'section': S, 'number': 6, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The equation <i>x</i><sup>2</sup> + <i>kx</i> + 36 = 0, where '
                      '<i>k</i> is a constant, has exactly one distinct real solution. '
                      'Which of the following is a possible value of <i>k</i>?</p>',
     'choices': ['−36', '−6', '12', '36'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>12</strong>. Bitta yechim boʻlishi uchun '
                    'diskriminant nolga teng: <i>k</i><sup>2</sup> − 4(1)(36) = 0, '
                    'yaʼni <i>k</i><sup>2</sup> = 144 va <i>k</i> = ±12. Variantlar '
                    'orasida 12 bor. <strong>−6</strong> — <i>k</i> ni ildizning '
                    'oʻzi (<i>x</i> = −6) bilan adashtirgan javob.'},

    {'section': S, 'number': 7, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>2<i>x</i> − 5<i>y</i> = 7<br>4<i>x</i> − 10<i>y</i> = '
                      '<i>c</i></p>'
                      '<p>In the system above, <i>c</i> is a constant. If the system has '
                      'infinitely many solutions, what is the value of <i>c</i>?</p>',
     'choices': ['7', '10', '14', '28'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>14</strong>. Cheksiz koʻp yechim boʻlishi uchun '
                    'ikkinchi tenglama birinchisining aynan koʻpaytmasi boʻlishi kerak. '
                    'Chap tomon 2 barobar (4<i>x</i> − 10<i>y</i> = 2(2<i>x</i> '
                    '− 5<i>y</i>)), demak oʻng tomon ham 2 barobar: <i>c</i> = 14. '
                    '<strong>7</strong> — oʻng tomonni oʻzgarishsiz qoldiradi, bu esa '
                    'yechimsiz sistema beradi.'},

    {'section': S, 'number': 8, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>A cyclist rides 30 kilometres at an average speed of 15 '
                      'kilometres per hour and returns along the same route at an average '
                      'speed of 10 kilometres per hour. What is the cyclist’s average '
                      'speed, in kilometres per hour, for the whole trip?</p>',
     'choices': ['11', '12', '12.5', '13'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>12</strong>. Oʻrtacha tezlik — <em>jami '
                    'masofa</em> ÷ <em>jami vaqt</em>, tezliklarning oʻrtachasi emas. '
                    'Masofa 60 km; vaqt 30/15 + 30/10 = 2 + 3 = 5 soat; 60 ÷ 5 = 12. '
                    '<strong>12.5</strong> — (15 + 10) ÷ 2, eng keng tarqalgan tuzoq: '
                    'sekin yoʻlda koʻproq vaqt sarflanadi, shuning uchun oʻrtacha 12.5 dan '
                    'past chiqadi.'},

    {'section': S, 'number': 9, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>What is the solution to the equation √(<i>x</i> + 5) = '
                      '<i>x</i> − 1?</p>',
     'choices': ['−1', '1', '4', '5'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Ikki tomonni kvadratga koʻtaramiz: '
                    '<i>x</i> + 5 = <i>x</i><sup>2</sup> − 2<i>x</i> + 1, yaʼni '
                    '<i>x</i><sup>2</sup> − 3<i>x</i> − 4 = 0 va (<i>x</i> '
                    '− 4)(<i>x</i> + 1) = 0. <strong>−1</strong> — begona '
                    'ildiz: <i>x</i> = −1 da chap tomon √4 = 2, oʻng tomon esa '
                    '−2. Kvadratga koʻtarganda ildizlarni har doim asl tenglamaga '
                    'qoʻyib tekshiring.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, a circle is given by the equation '
                      '<i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> + 6<i>x</i> − '
                      '4<i>y</i> = 23. What is the radius of the circle?</p>',
     'choices': ['4', '6', '13', '36'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Toʻliq kvadratga keltiramiz: '
                    '<i>x</i><sup>2</sup> + 6<i>x</i> = (<i>x</i> + 3)<sup>2</sup> − 9 '
                    'va <i>y</i><sup>2</sup> − 4<i>y</i> = (<i>y</i> − 2)'
                    '<sup>2</sup> − 4. Demak (<i>x</i> + 3)<sup>2</sup> + (<i>y</i> '
                    '− 2)<sup>2</sup> = 23 + 9 + 4 = 36 va radius √36 = 6. '
                    '<strong>36</strong> — <i>r</i><sup>2</sup> ning oʻzi: ildizni '
                    'olish qolib ketgan.'},

    {'section': S, 'number': 11, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>A line in the <i>xy</i>-plane passes through the points '
                      '(−3, 8) and (5, −8). What is the <i>y</i>-coordinate of '
                      'the <i>y</i>-intercept of the line?</p>',
     'choices': ['−8', '2', '6', '8'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. Burchak koeffitsiyenti '
                    '(−8 − 8) ÷ (5 − (−3)) = −16 ÷ 8 = −2. '
                    'Endi (−3, 8) ni <i>y</i> = −2<i>x</i> + <i>b</i> ga '
                    'qoʻyamiz: 8 = 6 + <i>b</i>, demak <i>b</i> = 2. <strong>8</strong> '
                    '— (−3, 8) nuqtaning <i>y</i> qiymati: bu nuqta '
                    '<i>y</i> oʻqida emas, chunki uning <i>x</i> i noldan farqli.'},

    {'section': S, 'number': 12, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>If <i>x</i> − 1/<i>x</i> = 3, what is the value of '
                      '<i>x</i><sup>2</sup> + 1/<i>x</i><sup>2</sup>?</p>',
     'choices': ['7', '9', '11', '13'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>11</strong>. Ikki tomonni kvadratga koʻtaramiz: '
                    '(<i>x</i> − 1/<i>x</i>)<sup>2</sup> = <i>x</i><sup>2</sup> '
                    '− 2 + 1/<i>x</i><sup>2</sup> = 9. Oʻrtadagi −2 ni '
                    'qoʻshamiz: <i>x</i><sup>2</sup> + 1/<i>x</i><sup>2</sup> = 11. '
                    '<strong>9</strong> — oʻrtadagi qoʻsh koʻpaytmani unutgan javob. '
                    'Diqqat: ayirmada oʻrtadagi had <em>manfiy</em>, shuning uchun uni '
                    'qoʻshamiz.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>The mean of 9 numbers is 14. When one of the numbers is removed, '
                      'the mean of the remaining 8 numbers is 15. What was the number that '
                      'was removed?</p>',
     'choices': ['6', '9', '14', '21'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Yigʻindilar bilan ishlaymiz: '
                    'avval 9 × 14 = 126, keyin 8 × 15 = 120. Olib tashlangan son — '
                    'ikki yigʻindining ayirmasi: 126 − 120 = 6. <strong>14</strong> '
                    '— eski oʻrtachaning oʻzi: oʻrtacha <em>koʻtarilgani</em> uchun '
                    'olib tashlangan son oʻrtachadan past boʻlishi kerak.'},

    {'section': S, 'number': 14, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>If 9<sup><i>x</i>−1</sup> = 27<sup><i>x</i>+1</sup>, what is '
                      'the value of <i>x</i>?</p>',
     'choices': ['−5', '−1', '1', '5'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>−5</strong>. Ikki tomonni 3 asosiga '
                    'keltiramiz: 9 = 3<sup>2</sup> va 27 = 3<sup>3</sup>, demak '
                    '3<sup>2(<i>x</i>−1)</sup> = 3<sup>3(<i>x</i>+1)</sup>. Asoslar '
                    'teng boʻlgani uchun darajalar teng: 2<i>x</i> − 2 = 3<i>x</i> + '
                    '3, bundan <i>x</i> = −5.'},

    {'section': S, 'number': 15, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>ABC</i>, angle <i>B</i> is a right angle and '
                      'sin <i>A</i> = 7/25. What is the value of tan <i>A</i>?</p>',
     'choices': ['7/25', '7/24', '24/25', '24/7'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>7/24</strong>. sin <i>A</i> = qarshi ÷ '
                    'gipotenuza = 7/25, demak qarshi katet 7, gipotenuza 25. Pifagor '
                    'boʻyicha yondosh katet √(625 − 49) = √576 = 24. '
                    'tan <i>A</i> = qarshi ÷ yondosh = 7/24. <strong>24/7</strong> — '
                    'kasrni agʻdarib yuborgan javob, yaʼni tan <i>C</i>.'},

    {'section': S, 'number': 16, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>a</i>(<i>x</i> + 3)<sup>2</sup> − 5, where <i>a</i> is a '
                      'constant. If <i>f</i>(−1) = 7, what is the value of '
                      '<i>a</i>?</p>',
     'choices': ['1', '3', '4', '12'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. <i>x</i> = −1 ni qoʻyamiz: '
                    '<i>a</i>(−1 + 3)<sup>2</sup> − 5 = 4<i>a</i> − 5 = 7, '
                    'demak 4<i>a</i> = 12 va <i>a</i> = 3. <strong>12</strong> — '
                    '4<i>a</i> ning qiymati: oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 17, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>The solution set of the inequality 7 − 3<i>x</i> ≥ '
                      '2<i>x</i> − 8 is <i>x</i> ≤ <i>k</i>, where <i>k</i> is a '
                      'constant. What is the value of <i>k</i>?</p>',
     'choices': ['−3', '1', '3', '5'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. 3<i>x</i> ni oʻngga, 8 ni chapga '
                    'oʻtkazamiz: 15 ≥ 5<i>x</i>, demak <i>x</i> ≤ 3 va '
                    '<i>k</i> = 3. Diqqat: tengsizlikni <em>musbat</em> 5 ga boʻlganimiz '
                    'uchun ishora oʻzgarmadi — ishora faqat manfiy songa boʻlganda '
                    'aylanadi.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 6(<i>x</i> − 2) = 3(<i>x</i> + 4), what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['8'],
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Ikki qavsni ochamiz: 6<i>x</i> '
                    '− 12 = 3<i>x</i> + 12. 3<i>x</i> ni ayirib, 12 ni qoʻshamiz: '
                    '3<i>x</i> = 24, demak <i>x</i> = 8. Tekshirish: 6(6) = 36 va '
                    '3(12) = 36.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>A chemist has 10 litres of a solution that is 60% acid by volume. '
                      'How many litres of pure acid must be added so that the resulting '
                      'solution is 75% acid by volume?</p>' + GRID_NOTE,
     'accepted': ['6'],
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Boshida kislota 10 × 0.60 = 6 litr. '
                    'Sof kislota qoʻshilganda <em>ham</em> kislota, <em>ham</em> umumiy '
                    'hajm oshadi: (6 + <i>a</i>) ÷ (10 + <i>a</i>) = 0.75. Bundan '
                    '6 + <i>a</i> = 7.5 + 0.75<i>a</i>, yaʼni 0.25<i>a</i> = 1.5 va '
                    '<i>a</i> = 6. Eng keng tarqalgan xato — maxrajni 10 deb '
                    'qoldirish.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>2</sup> − 8<i>x</i> + 12 = 0 and '
                      '<i>x</i> ≠ 2, what is the value of <i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['6'],
     'explanation': 'Toʻgʻri javob <strong>6</strong>. (<i>x</i> − 2)(<i>x</i> '
                    '− 6) = 0 dan ildizlar 2 va 6; shart <i>x</i> ≠ 2 '
                    'birinchisini chiqarib tashlaydi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If (3<i>x</i> − 5) ÷ 4 = 7, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['11'],
     'explanation': 'Toʻgʻri javob <strong>11</strong>. Avval ikki tomonni 4 ga '
                    'koʻpaytiramiz: 3<i>x</i> − 5 = 28, keyin 5 ni qoʻshib 3 ga '
                    'boʻlamiz: <i>x</i> = 11. Kasr koʻrinishidagi tenglamada birinchi '
                    'qadam har doim maxrajdan qutulish.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 2<sup>3<i>x</i></sup> = 64, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['2'],
     'explanation': 'Toʻgʻri javob <strong>2</strong>. 64 = 2<sup>6</sup>, demak '
                    '3<i>x</i> = 6 va <i>x</i> = 2. Eng keng tarqalgan xato — 6 '
                    'yozish: u 3<i>x</i> ning qiymati, <i>x</i> niki emas.'},
]
