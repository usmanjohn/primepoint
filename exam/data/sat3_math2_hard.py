# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 3 · Math, Module 2 (UPPER)
#  22 questions · 35 minutes · taken by a pupil who scored 14 or more on math1.
#  Questions 18–22 are student-produced responses (grid-ins).

#
#  Load: python manage.py load_mock exam/data/sat3_math2_hard.py --expect-questions=22
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

S = 'math2h'

GRID_NOTE = ('<p style="font-size:0.85rem;opacity:0.75;">Enter your answer in the '
             'box. It may be an integer, a fraction or a decimal.</p>')

QUESTIONS = [

    {'section': S, 'number': 1, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>If 4(3<i>x</i> − 2) = 5<i>x</i> + 41, what is the value of '
                      '<i>x</i>?</p>',
     'choices': ['3', '5', '7', '49'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>7</strong>. Qavsni ochamiz: 12<i>x</i> − 8 '
                    '= 5<i>x</i> + 41. 5<i>x</i> ni ayirib, 8 ni qoʻshamiz: 7<i>x</i> = '
                    '49, demak <i>x</i> = 7. <strong>49</strong> — 7<i>x</i> ning '
                    'qiymati, yaʼni oxirgi boʻlish qolib ketgan.'},

    {'section': S, 'number': 2, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '2<i>x</i><sup>2</sup> − <i>x</i>. Which expression is '
                      'equivalent to <i>f</i>(<i>x</i> + 1) − <i>f</i>(<i>x</i>)?</p>',
     'choices': [
         '2<i>x</i> + 1',
         '4<i>x</i> − 1',
         '4<i>x</i> + 1',
         '4<i>x</i> + 3',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>4<i>x</i> + 1</strong>. '
                    '<i>f</i>(<i>x</i>+1) = 2(<i>x</i>+1)<sup>2</sup> − (<i>x</i>+1) '
                    '= 2<i>x</i><sup>2</sup> + 4<i>x</i> + 2 − <i>x</i> − 1 = '
                    '2<i>x</i><sup>2</sup> + 3<i>x</i> + 1. Undan <i>f</i>(<i>x</i>) = '
                    '2<i>x</i><sup>2</sup> − <i>x</i> ni ayiramiz: 3<i>x</i> + 1 '
                    '− (−<i>x</i>) = 4<i>x</i> + 1. <strong>2<i>x</i> + '
                    '1</strong> — ayirishda −<i>x</i> ning ishorasini '
                    'almashtirmagan javob.'},

    {'section': S, 'number': 3, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>A population increases by 10% in one year and then decreases by '
                      '10% the next. The final population is what percent of the original '
                      'population?</p>',
     'choices': ['80%', '99%', '100%', '101%'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>99%</strong>. Foiz har safar <em>joriy</em> '
                    'sondan olinadi: 1.10 × 0.90 = 0.99, yaʼni 99%. '
                    '<strong>100%</strong> eng koʻp tanlanadigan javob — "+10% va '
                    '−10% bir-birini yoʻqotadi" degan tuygʻu; aslida ikkinchi 10% '
                    'kattaroq sondan olinadi.'},

    {'section': S, 'number': 4, 'skill': 'Algebra', 'difficulty': 'medium',
     'question_text': '<p>5<i>x</i> − 2<i>y</i> = 22<br><i>x</i> + 2<i>y</i> = 14</p>'
                      '<p>The system of equations above has a unique solution. What is the '
                      'value of <i>x</i>?</p>',
     'choices': ['2', '4', '6', '8'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>6</strong>. Ikki tenglamani qoʻshsak '
                    '<i>y</i> qisqaradi: 6<i>x</i> = 36, demak <i>x</i> = 6. Qoʻshish '
                    'usuli aynan shunday holat uchun: bir xil koeffitsiyent qarama-qarshi '
                    'ishorada turibdi.'},

    {'section': S, 'number': 5, 'skill': 'Geometry and Trigonometry', 'difficulty': 'medium',
     'question_text': '<p>A sphere has a radius of 3 units. What is its volume?</p>',
     'choices': ['12π', '36π', '108π', '972π'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>36π</strong>. Shar hajmi — '
                    '⁴⁄₃π<i>r</i><sup>3</sup> = '
                    '⁴⁄₃ × π × 27 = 36π. '
                    '<strong>108π</strong> — ⁴⁄₃ ni unutgan '
                    'javob (π<i>r</i><sup>3</sup> ning oʻzi).'},

    {'section': S, 'number': 6, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The equation <i>x</i><sup>2</sup> + <i>kx</i> + 16 = 0, where '
                      '<i>k</i> is a constant, has exactly one distinct real solution. '
                      'Which of the following is a possible value of <i>k</i>?</p>',
     'choices': ['−16', '−4', '8', '16'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Bitta yechim boʻlishi uchun '
                    'diskriminant nolga teng: <i>k</i><sup>2</sup> − 4(1)(16) = 0, '
                    'yaʼni <i>k</i><sup>2</sup> = 64 va <i>k</i> = ±8. '
                    '<strong>−4</strong> — <i>k</i> ni ildizning oʻzi '
                    '(<i>x</i> = −4) bilan adashtirgan javob.'},

    {'section': S, 'number': 7, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>3<i>x</i> + 4<i>y</i> = 12<br>9<i>x</i> + 12<i>y</i> = '
                      '<i>c</i></p>'
                      '<p>In the system above, <i>c</i> is a constant. If the system has '
                      'infinitely many solutions, what is the value of <i>c</i>?</p>',
     'choices': ['12', '24', '36', '48'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>36</strong>. Cheksiz koʻp yechim boʻlishi uchun '
                    'ikkinchi tenglama birinchisining aynan koʻpaytmasi boʻlishi kerak. '
                    'Chap tomon 3 barobar (9<i>x</i> + 12<i>y</i> = 3(3<i>x</i> + '
                    '4<i>y</i>)), demak oʻng tomon ham 3 barobar: <i>c</i> = 36. '
                    '<strong>12</strong> — oʻng tomonni oʻzgarishsiz qoldiradi, bu '
                    'esa yechimsiz sistema beradi.'},

    {'section': S, 'number': 8, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>A runner covers 12 kilometres at an average speed of 12 '
                      'kilometres per hour and a further 12 kilometres at an average speed '
                      'of 6 kilometres per hour. What is the runner’s average speed, '
                      'in kilometres per hour, for the whole distance?</p>',
     'choices': ['7', '8', '9', '10'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Oʻrtacha tezlik — <em>jami '
                    'masofa</em> ÷ <em>jami vaqt</em>, tezliklarning oʻrtachasi emas. '
                    'Masofa 24 km; vaqt 12/12 + 12/6 = 1 + 2 = 3 soat; 24 ÷ 3 = 8. '
                    '<strong>9</strong> — (12 + 6) ÷ 2, eng keng tarqalgan tuzoq: '
                    'sekin qismda koʻproq vaqt ketadi, shuning uchun javob 9 dan past.'},

    {'section': S, 'number': 9, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>What is the solution to the equation √(3<i>x</i> + 4) = '
                      '<i>x</i>?</p>',
     'choices': ['−1', '1', '4', '7'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. Ikki tomonni kvadratga koʻtaramiz: '
                    '3<i>x</i> + 4 = <i>x</i><sup>2</sup>, yaʼni <i>x</i><sup>2</sup> '
                    '− 3<i>x</i> − 4 = 0 va (<i>x</i> − 4)(<i>x</i> + 1) = '
                    '0. <strong>−1</strong> — begona ildiz: kvadrat ildiz '
                    'manfiy son bera olmaydi, shuning uchun uni asl tenglamaga qoʻyib '
                    'tekshirish shart.'},

    {'section': S, 'number': 10, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In the <i>xy</i>-plane, a circle is given by the equation '
                      '<i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> − 10<i>x</i> + '
                      '2<i>y</i> = 38. What is the radius of the circle?</p>',
     'choices': ['5', '6', '8', '64'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>8</strong>. Toʻliq kvadratga keltiramiz: '
                    '<i>x</i><sup>2</sup> − 10<i>x</i> = (<i>x</i> − 5)'
                    '<sup>2</sup> − 25 va <i>y</i><sup>2</sup> + 2<i>y</i> = '
                    '(<i>y</i> + 1)<sup>2</sup> − 1. Demak (<i>x</i> − 5)'
                    '<sup>2</sup> + (<i>y</i> + 1)<sup>2</sup> = 38 + 25 + 1 = 64 va '
                    'radius √64 = 8. <strong>64</strong> — '
                    '<i>r</i><sup>2</sup> ning oʻzi: ildizni olish qolib ketgan.'},

    {'section': S, 'number': 11, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>A line in the <i>xy</i>-plane passes through the points '
                      '(−2, 11) and (4, −7). What is the <i>y</i>-coordinate of '
                      'the <i>y</i>-intercept of the line?</p>',
     'choices': ['−7', '5', '6', '11'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Burchak koeffitsiyenti '
                    '(−7 − 11) ÷ (4 − (−2)) = −18 ÷ 6 = '
                    '−3. Endi (4, −7) ni <i>y</i> = −3<i>x</i> + <i>b</i> '
                    'ga qoʻyamiz: −7 = −12 + <i>b</i>, demak <i>b</i> = 5. '
                    '<strong>11</strong> — (−2, 11) nuqtaning <i>y</i> qiymati: '
                    'bu nuqta <i>y</i> oʻqida emas.'},

    {'section': S, 'number': 12, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>If <i>x</i> + 1/<i>x</i> = 4, what is the value of '
                      '<i>x</i><sup>3</sup> + 1/<i>x</i><sup>3</sup>?</p>',
     'choices': ['40', '52', '58', '64'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>52</strong>. Kubga koʻtaramiz: (<i>x</i> + '
                    '1/<i>x</i>)<sup>3</sup> = <i>x</i><sup>3</sup> + '
                    '1/<i>x</i><sup>3</sup> + 3(<i>x</i> + 1/<i>x</i>) = 64. Demak '
                    '<i>x</i><sup>3</sup> + 1/<i>x</i><sup>3</sup> = 64 − 3 × 4 = '
                    '52. <strong>64</strong> — oʻrtadagi 3(<i>x</i> + 1/<i>x</i>) '
                    'hadini unutgan javob.'},

    {'section': S, 'number': 13, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'question_text': '<p>The mean of 7 numbers is 20. When one more number is included, '
                      'the mean of all 8 numbers is 22. What is the number that was '
                      'included?</p>',
     'choices': ['22', '28', '36', '44'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>36</strong>. Yigʻindilar bilan ishlaymiz: '
                    'avval 7 × 20 = 140, keyin 8 × 22 = 176. Yangi son — ikki '
                    'yigʻindining ayirmasi: 176 − 140 = 36. <strong>22</strong> '
                    '— yangi oʻrtachaning oʻzi: oʻrtachani ikki ballga koʻtarish '
                    'uchun yangi son undan ancha yuqori boʻlishi kerak.'},

    {'section': S, 'number': 14, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>If 8<sup><i>x</i>+1</sup> = 4<sup>2<i>x</i></sup>, what is the '
                      'value of <i>x</i>?</p>',
     'choices': ['1', '2', '3', '6'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>3</strong>. Ikki tomonni 2 asosiga keltiramiz: '
                    '8 = 2<sup>3</sup> va 4 = 2<sup>2</sup>, demak '
                    '2<sup>3(<i>x</i>+1)</sup> = 2<sup>4<i>x</i></sup>. Asoslar teng '
                    'boʻlgani uchun darajalar teng: 3<i>x</i> + 3 = 4<i>x</i>, bundan '
                    '<i>x</i> = 3.'},

    {'section': S, 'number': 15, 'skill': 'Geometry and Trigonometry', 'difficulty': 'hard',
     'question_text': '<p>In right triangle <i>ABC</i>, angle <i>C</i> is a right angle '
                      'and tan <i>A</i> = 8/15. What is the value of sin <i>A</i>?</p>',
     'choices': ['8/17', '8/15', '15/17', '15/8'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>8/17</strong>. tan <i>A</i> = qarshi ÷ yondosh '
                    '= 8/15, demak qarshi katet 8, yondosh katet 15. Pifagor boʻyicha '
                    'gipotenuza √(64 + 225) = √289 = 17, va sin <i>A</i> = '
                    'qarshi ÷ gipotenuza = 8/17. <strong>15/17</strong> — bu '
                    'cos <i>A</i>: sinusning suratida yondosh emas, qarshi katet turadi.'},

    {'section': S, 'number': 16, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'question_text': '<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = '
                      '<i>a</i>(<i>x</i> − 4)<sup>2</sup> + 2, where <i>a</i> is a '
                      'constant. If <i>f</i>(6) = 18, what is the value of <i>a</i>?</p>',
     'choices': ['2', '4', '6', '8'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. <i>x</i> = 6 ni qoʻyamiz: '
                    '<i>a</i>(6 − 4)<sup>2</sup> + 2 = 4<i>a</i> + 2 = 18, demak '
                    '4<i>a</i> = 16 va <i>a</i> = 4. <strong>8</strong> — '
                    '(6 − 4) ni kvadratga koʻtarmay, 2<i>a</i> + 2 = 18 deb '
                    'hisoblagan javob.'},

    {'section': S, 'number': 17, 'skill': 'Algebra', 'difficulty': 'hard',
     'question_text': '<p>The solution set of the inequality 9 − 4<i>x</i> &lt; '
                      '2<i>x</i> − 15 is <i>x</i> &gt; <i>k</i>, where <i>k</i> is a '
                      'constant. What is the value of <i>k</i>?</p>',
     'choices': ['−4', '2', '4', '6'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>4</strong>. 4<i>x</i> ni oʻngga, 15 ni chapga '
                    'oʻtkazamiz: 24 &lt; 6<i>x</i>, demak <i>x</i> &gt; 4 va <i>k</i> = '
                    '4. Diqqat: tengsizlikni <em>musbat</em> 6 ga boʻlganimiz uchun ishora '
                    'oʻzgarmadi — ishora faqat manfiy songa boʻlganda aylanadi.'},

    {'section': S, 'number': 18, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 5(<i>x</i> − 3) = 2(<i>x</i> + 6), what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['9'],
     'explanation': 'Toʻgʻri javob <strong>9</strong>. Ikki qavsni ochamiz: 5<i>x</i> '
                    '− 15 = 2<i>x</i> + 12. 2<i>x</i> ni ayirib, 15 ni qoʻshamiz: '
                    '3<i>x</i> = 27, demak <i>x</i> = 9. Tekshirish: 5(6) = 30 va '
                    '2(15) = 30.'},

    {'section': S, 'number': 19, 'skill': 'Problem-Solving and Data Analysis', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>A chemist has 12 litres of a solution that is 25% salt by volume. '
                      'How many litres of water must evaporate so that the remaining '
                      'solution is 40% salt by volume?</p>' + GRID_NOTE,
     'accepted': ['4.5', '9/2'],
     'explanation': 'Toʻgʻri javob <strong>4.5</strong>. Tuz miqdori oʻzgarmaydi: '
                    '12 × 0.25 = 3 litr. Suv bugʻlanganda faqat <em>umumiy hajm</em> '
                    'kamayadi: 3 ÷ (12 − <i>w</i>) = 0.40, bundan 12 − '
                    '<i>w</i> = 7.5 va <i>w</i> = 4.5. Eritma masalasida har doim '
                    'oʻzgarmaydigan kattalikdan boshlang.'},

    {'section': S, 'number': 20, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If <i>x</i><sup>2</sup> − 11<i>x</i> + 28 = 0 and '
                      '<i>x</i> ≠ 4, what is the value of <i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['7'],
     'explanation': 'Toʻgʻri javob <strong>7</strong>. Koʻpaytmasi 28, yigʻindisi 11 '
                    'boʻlgan ikki son — 4 va 7, demak (<i>x</i> − 4)(<i>x</i> '
                    '− 7) = 0. Shart <i>x</i> ≠ 4 birinchi ildizni chiqarib '
                    'tashlaydi.'},

    {'section': S, 'number': 21, 'skill': 'Algebra', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If (4<i>x</i> + 7) ÷ 3 = 9, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['5'],
     'explanation': 'Toʻgʻri javob <strong>5</strong>. Avval ikki tomonni 3 ga '
                    'koʻpaytiramiz: 4<i>x</i> + 7 = 27, keyin 7 ni ayirib 4 ga boʻlamiz: '
                    '<i>x</i> = 5. Kasr koʻrinishidagi tenglamada birinchi qadam har doim '
                    'maxrajdan qutulish.'},

    {'section': S, 'number': 22, 'skill': 'Advanced Math', 'difficulty': 'hard',
     'answer_type': 'grid',
     'question_text': '<p>If 5<sup>2<i>x</i></sup> = 625, what is the value of '
                      '<i>x</i>?</p>' + GRID_NOTE,
     'accepted': ['2'],
     'explanation': 'Toʻgʻri javob <strong>2</strong>. 625 = 5<sup>4</sup>, demak '
                    '2<i>x</i> = 4 va <i>x</i> = 2. Eng keng tarqalgan xato — 4 '
                    'yozish: u 2<i>x</i> ning qiymati, <i>x</i> niki emas.'},
]
