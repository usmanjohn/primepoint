# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 1 · Math, Module 2 (UPPER)
#  22 questions · 35 minutes · taken by a pupil who scored 14 or more on math1.
#  Questions 18–22 are student-produced responses (grid-ins).
#
#  Load: python manage.py load_mock exam/data/sat1_math2_hard.py --expect-questions=22
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §3
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

S = 'math2h'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>If 3(2<i>x</i> − 5) = 4<i>x</i> + 7, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['4', '8', '11', '22'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>11</strong>. Qavsni ochamiz: 6<i>x</i> − 15 '
                    '= 4<i>x</i> + 7. 4<i>x</i> ni ayirib, 15 ni qoʻshamiz: 2<i>x</i> = 22, '
                    'demak <i>x</i> = 11. <strong>22</strong> — 2<i>x</i> ning qiymati, '
                    'yaʼni oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 2, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>x</i><sup>2</sup> − 4<i>x</i>. Which expression is '
                      'equivalent to <i>f</i>(<i>x</i> + 1) − <i>f</i>(<i>x</i>)?</p>',
     'choices': [
         '−3',
         '2<i>x</i> − 5',
         '2<i>x</i> − 3',
         '2<i>x</i> + 1',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>2<i>x</i> − 3</strong>. '
                    '<i>f</i>(<i>x</i>+1) = (<i>x</i>+1)<sup>2</sup> − 4(<i>x</i>+1) = '
                    '<i>x</i><sup>2</sup> + 2<i>x</i> + 1 − 4<i>x</i> − 4 = '
                    '<i>x</i><sup>2</sup> − 2<i>x</i> − 3. Undan '
                    '<i>f</i>(<i>x</i>) = <i>x</i><sup>2</sup> − 4<i>x</i> ni '
                    'ayiramiz: (−2<i>x</i> − 3) − (−4<i>x</i>) = '
                    '2<i>x</i> − 3. <strong>−3</strong> — ayirishda '
                    '−4<i>x</i> ning ishorasini almashtirmagan javob.'},

    {'section': S, 'number': 3, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>The price of an item is increased by 20%. The new price is '
                      'then decreased by 20%. The final price is what percent of the '
                      'original price?</p>',
     'choices': ['80%', '96%', '100%', '104%'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>96%</strong>. Foiz har safar <em>joriy</em> '
                    'narxdan olinadi: 1.20 × 0.80 = 0.96, yaʼni 96%. <strong>100%</strong> '
                    'eng koʻp tanlanadigan javob — "+20% va −20% bir-birini yoʻqotadi" '
                    'degan tuygʻu; aslida ikkinchi 20% kattaroq sondan olinadi, shuning '
                    'uchun narx pasayadi.'},

    {'section': S, 'number': 4, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>2<i>x</i> + 3<i>y</i> = 12<br><i>x</i> − <i>y</i> = 1</p>'
                      '<p>The system of equations above has a unique solution. What is '
                      'the value of <i>y</i>?</p>',
     'choices': ['1', '2', '3', '5'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. Ikkinchi tenglamadan <i>x</i> = '
                    '<i>y</i> + 1; uni birinchisiga qoʻyamiz: 2(<i>y</i>+1) + 3<i>y</i> = '
                    '12, yaʼni 5<i>y</i> + 2 = 12 va <i>y</i> = 2. <strong>3</strong> — '
                    '<i>x</i> ning qiymati: qaysi nomaʼlum soʻralganini oxirida '
                    'tekshiring.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A right circular cylinder has a radius of 4 units and a height '
                      'of 9 units. What is the volume of the cylinder?</p>',
     'choices': ['36π', '72π', '144π', '288π'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>144π</strong>. Hajm π<i>r</i><sup>2</sup>'
                    '<i>h</i> = π × 4<sup>2</sup> × 9 = π × 16 × 9 = 144π. '
                    '<strong>36π</strong> — radiusni kvadratga koʻtarmay, 4 × 9 '
                    'hisoblagan javob.'},

    {'section': S, 'number': 6, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The equation <i>x</i><sup>2</sup> + <i>kx</i> + 25 = 0, where '
                      '<i>k</i> is a constant, has exactly one distinct real solution. '
                      'Which of the following is a possible value of <i>k</i>?</p>',
     'choices': ['−25', '−5', '10', '25'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>10</strong>. Bitta yechim boʻlishi uchun '
                    'diskriminant nolga teng: <i>k</i><sup>2</sup> − 4(1)(25) = 0, '
                    'yaʼni <i>k</i><sup>2</sup> = 100 va <i>k</i> = ±10. Variantlar '
                    'orasida 10 bor. <strong>−5</strong> — <i>k</i> ni ildizning '
                    'oʻzi bilan (<i>x</i> = −5) adashtirgan javob.'},

    {'section': S, 'number': 7, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>3<i>x</i> − <i>y</i> = 8<br>6<i>x</i> − 2<i>y</i> = '
                      '<i>c</i></p>'
                      '<p>In the system above, <i>c</i> is a constant. If the system has '
                      'infinitely many solutions, what is the value of <i>c</i>?</p>',
     'choices': ['4', '8', '16', '24'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>16</strong>. Cheksiz koʻp yechim boʻlishi uchun '
                    'ikkinchi tenglama birinchisining aynan koʻpaytmasi boʻlishi kerak. '
                    'Chap tomon 2 barobar (6<i>x</i> − 2<i>y</i> = 2(3<i>x</i> − '
                    '<i>y</i>)), demak oʻng tomon ham 2 barobar: <i>c</i> = 2 × 8 = 16. '
                    '<strong>8</strong> — oʻng tomonni oʻzgarishsiz qoldirgan javob, bu '
                    'esa yechimsiz sistema beradi.'},

    {'section': S, 'number': 8, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>A car travels 120 kilometres at an average speed of 60 '
                      'kilometres per hour and returns along the same route at an '
                      'average speed of 40 kilometres per hour. What is the car’s '
                      'average speed, in kilometres per hour, for the entire trip?</p>',
     'choices': ['45', '48', '50', '52'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>48</strong>. Oʻrtacha tezlik — <em>jami '
                    'masofa</em> ÷ <em>jami vaqt</em>, tezliklarning oʻrtachasi emas. '
                    'Masofa 240 km; vaqt 120/60 + 120/40 = 2 + 3 = 5 soat; 240 ÷ 5 = 48. '
                    '<strong>50</strong> — (60 + 40) ÷ 2, eng keng tarqalgan tuzoq: sekin '
                    'yoʻlda koʻproq vaqt sarflanadi, shuning uchun oʻrtacha 50 dan past '
                    'chiqadi.'},

    {'section': S, 'number': 9, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>What is the solution to the equation '
                      '√(<i>x</i> + 7) = <i>x</i> − 5?</p>',
     'choices': ['2', '4', '9', '11'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Ikki tomonni kvadratga koʻtaramiz: '
                    '<i>x</i> + 7 = <i>x</i><sup>2</sup> − 10<i>x</i> + 25, yaʼni '
                    '<i>x</i><sup>2</sup> − 11<i>x</i> + 18 = 0 va (<i>x</i> − 2)'
                    '(<i>x</i> − 9) = 0. <strong>2</strong> — begona ildiz: '
                    '<i>x</i> = 2 da chap tomon √9 = 3, oʻng tomon esa −3 '
                    'boʻladi. Kvadratga koʻtarganda topilgan ildizlarni har doim asl '
                    'tenglamaga qoʻyib tekshiring.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, a circle is given by the equation '
                      '<i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> − 6<i>x</i> + '
                      '8<i>y</i> = 0. What is the radius of the circle?</p>',
     'choices': ['3', '4', '5', '25'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Toʻliq kvadratga keltiramiz: '
                    '<i>x</i><sup>2</sup> − 6<i>x</i> = (<i>x</i> − 3)<sup>2</sup> '
                    '− 9 va <i>y</i><sup>2</sup> + 8<i>y</i> = (<i>y</i> + 4)<sup>2</sup> '
                    '− 16. Demak (<i>x</i> − 3)<sup>2</sup> + (<i>y</i> + 4)'
                    '<sup>2</sup> = 25 va radius √25 = 5. <strong>25</strong> — '
                    '<i>r</i><sup>2</sup> ning oʻzi: ildizni olish qolib ketgan.'},

    {'section': S, 'number': 11, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>A line in the <i>xy</i>-plane passes through the points '
                      '(−2, 7) and (4, −5). What is the <i>y</i>-coordinate of '
                      'the <i>y</i>-intercept of the line?</p>',
     'choices': ['−5', '1', '3', '7'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Burchak koeffitsiyenti '
                    '(−5 − 7) ÷ (4 − (−2)) = −12 ÷ 6 = −2. '
                    'Endi (4, −5) ni <i>y</i> = −2<i>x</i> + <i>b</i> ga '
                    'qoʻyamiz: −5 = −8 + <i>b</i>, demak <i>b</i> = 3. '
                    '<strong>7</strong> — (−2, 7) nuqtaning <i>y</i> qiymati: bu '
                    'nuqta <i>y</i> oʻqida emas, chunki uning <i>x</i> i noldan farqli.'},

    {'section': S, 'number': 12, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>If <i>x</i> + 1/<i>x</i> = 5, what is the value of '
                      '<i>x</i><sup>2</sup> + 1/<i>x</i><sup>2</sup>?</p>',
     'choices': ['10', '23', '25', '27'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>23</strong>. Ikki tomonni kvadratga koʻtaramiz: '
                    '(<i>x</i> + 1/<i>x</i>)<sup>2</sup> = <i>x</i><sup>2</sup> + 2 + '
                    '1/<i>x</i><sup>2</sup> = 25. Oʻrtadagi 2 ni ayiramiz: '
                    '<i>x</i><sup>2</sup> + 1/<i>x</i><sup>2</sup> = 23. '
                    '<strong>25</strong> — oʻrtadagi qoʻsh koʻpaytmani unutgan javob.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>The mean score of 12 students on a test is 78. When one more '
                      'student’s score is included, the mean of all 13 scores is '
                      '79. What was the thirteenth student’s score?</p>',
     'choices': ['79', '85', '91', '97'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>91</strong>. Yigʻindilar bilan ishlaymiz: '
                    'avval 12 × 78 = 936, keyin 13 × 79 = 1,027. Yangi ball — ikki '
                    'yigʻindining ayirmasi: 1,027 − 936 = 91. <strong>79</strong> — '
                    'yangi oʻrtachaning oʻzi: oʻrtachani bir ballga koʻtarish uchun 13 '
                    'ta ballni koʻtarish kerak, shuning uchun yangi ball ancha yuqori.'},

    {'section': S, 'number': 14, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>If 2<sup><i>x</i>+3</sup> = 8<sup><i>x</i>−1</sup>, what '
                      'is the value of <i>x</i>?</p>',
     'choices': ['2', '3', '4', '6'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Ikki tomonni bitta asosga '
                    'keltiramiz: 8 = 2<sup>3</sup>, demak oʻng tomon '
                    '2<sup>3(<i>x</i>−1)</sup> = 2<sup>3<i>x</i>−3</sup>. '
                    'Asoslar teng boʻlgani uchun darajalar teng: <i>x</i> + 3 = '
                    '3<i>x</i> − 3, bundan 2<i>x</i> = 6 va <i>x</i> = 3.'},

    {'section': S, 'number': 15, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>PQR</i>, angle <i>Q</i> is a right angle '
                      'and cos <i>P</i> = 5/13. What is the value of tan <i>P</i>?</p>',
     'choices': ['5/13', '5/12', '12/13', '12/5'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>12/5</strong>. cos <i>P</i> = yondosh ÷ '
                    'gipotenuza = 5/13, demak yondosh katet 5, gipotenuza 13. Pifagor '
                    'boʻyicha qarshi katet √(169 − 25) = √144 = 12. '
                    'tan <i>P</i> = qarshi ÷ yondosh = 12/5. <strong>12/13</strong> — bu '
                    'sin <i>P</i>: tangensning maxraji gipotenuza emas, yondosh katet.'},

    {'section': S, 'number': 16, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>a</i>(<i>x</i> − 2)<sup>2</sup> + 3, where <i>a</i> is a '
                      'constant. If <i>f</i>(0) = 11, what is the value of '
                      '<i>a</i>?</p>',
     'choices': ['1', '2', '4', '8'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>2</strong>. <i>x</i> = 0 ni qoʻyamiz: '
                    '<i>a</i>(0 − 2)<sup>2</sup> + 3 = 4<i>a</i> + 3 = 11, demak '
                    '4<i>a</i> = 8 va <i>a</i> = 2. <strong>8</strong> — 4<i>a</i> ning '
                    'qiymati: oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 17, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>The solution set of the inequality 5 − 2<i>x</i> &gt; '
                      '3<i>x</i> − 20 is <i>x</i> &lt; <i>k</i>, where <i>k</i> is '
                      'a constant. What is the value of <i>k</i>?</p>',
     'choices': ['−5', '1', '4', '5'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. 2<i>x</i> ni oʻngga, 20 ni chapga '
                    'oʻtkazamiz: 25 &gt; 5<i>x</i>, demak <i>x</i> &lt; 5 va '
                    '<i>k</i> = 5. Diqqat: tengsizlikni <em>musbat</em> 5 ga boʻlganimiz '
                    'uchun ishora oʻzgarmadi — ishora faqat manfiy songa boʻlganda '
                    'aylanadi.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 4(<i>x</i> − 3) = 2(<i>x</i> + 5), what is the value '
                      'of <i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['11'],
     'explanation': 'Toʻgʻri javob <strong>11</strong>. Ikki qavsni ochamiz: 4<i>x</i> '
                    '− 12 = 2<i>x</i> + 10. 2<i>x</i> ni ayirib, 12 ni qoʻshamiz: '
                    '2<i>x</i> = 22, demak <i>x</i> = 11. Tekshirish: 4(8) = 32 va '
                    '2(16) = 32.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>A chemist has 20 litres of a solution that is 40% salt by '
                      'volume. How many litres of pure water must be added so that the '
                      'resulting solution is 25% salt by volume?</p>' + GRID_NOTE,
     'accepted': ['12'],
     'explanation': 'Toʻgʻri javob <strong>12</strong>. Tuz miqdori oʻzgarmaydi: '
                    '20 × 0.40 = 8 litr. Yangi hajm 20 + <i>w</i> boʻlsa, '
                    '8 ÷ (20 + <i>w</i>) = 0.25, bundan 20 + <i>w</i> = 32 va '
                    '<i>w</i> = 12. Eritma masalasida har doim <em>oʻzgarmaydigan</em> '
                    'kattalikdan boshlang.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>2</sup> − 6<i>x</i> + 5 = 0 and '
                      '<i>x</i> ≠ 1, what is the value of <i>x</i>?</p>'
                      + GRID_NOTE,
     'accepted': ['5'],
     'explanation': 'Toʻgʻri javob <strong>5</strong>. (<i>x</i> − 1)(<i>x</i> '
                    '− 5) = 0 dan ildizlar 1 va 5; shart <i>x</i> ≠ 1 birinchisini '
                    'chiqarib tashlaydi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If (2<i>x</i> + 3) ÷ 5 = 7, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['16'],
     'explanation': 'Toʻgʻri javob <strong>16</strong>. Avval ikki tomonni 5 ga '
                    'koʻpaytiramiz: 2<i>x</i> + 3 = 35, keyin 3 ni ayirib 2 ga boʻlamiz: '
                    '<i>x</i> = 16. Kasr koʻrinishidagi tenglamada birinchi qadam har doim '
                    'maxrajdan qutulish.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 3<sup>2<i>x</i></sup> = 81, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['2'],
     'explanation': 'Toʻgʻri javob <strong>2</strong>. 81 = 3<sup>4</sup>, demak '
                    '2<i>x</i> = 4 va <i>x</i> = 2. Eng keng tarqalgan xato — 4 yozish: '
                    'u 2<i>x</i> ning qiymati, <i>x</i> niki emas.'},
]
