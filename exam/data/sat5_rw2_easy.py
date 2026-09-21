# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 5 · Reading and Writing, Module 2 (LOWER)
#  27 questions · 32 minutes · taken by a pupil who scored under 18 on rw1.
#
#  Same domains, same counts, same order as the upper module — one-step
#  reasoning, familiar wording, the point in the opening sentence.
#
#  Load: python manage.py load_mock exam/data/sat5_rw2_easy.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §3
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

S = 'rw2e'

WORD_Q = ('Which choice completes the text with the most logical and precise '
          'word or phrase?')
TRANSITION_Q = ('Which choice completes the text with the most logical '
                'transition?')
CONVENTION_Q = ('Which choice completes the text so that it conforms to the '
                'conventions of Standard English?')

QUESTIONS = [

    # ── Words in Context (1–4) ─────────────────────────────────────────
    {'section': S, 'number': 1, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>The first Shinkansen line opened in 1964 and has carried more than ten '
                'billion passengers since. In sixty years of service not one has died in a '
                'derailment or a collision, a record that owes less to luck than to a '
                '______ decision: the line shares no track with anything slower.</p>',
     'question_text': WORD_Q,
     'choices': ['commercial', 'design', 'political', 'recent'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>design</strong>. Ikki nuqtadan keyingi qism '
                    'qanday qaror ekanini aytadi — yoʻl boshqa poyezdlar bilan '
                    'boʻlishilmaydi, bu muhandislik yechimi. <strong>recent</strong> matnga '
                    'zid: qaror 1964-yildan beri amalda.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>A New Caledonian crow given a straight piece of wire and a bucket at '
                'the bottom of a tube will bend the wire into a hook and lift the bucket '
                'out. The bird has never seen wire before. What the experiment tests is '
                'therefore not memory but ______.</p>',
     'question_text': WORD_Q,
     'choices': ['endurance', 'imitation', 'invention', 'patience'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>invention</strong>. Qush simni birinchi marta '
                    'koʻryapti, demak u yodlagan usulni qoʻllamaydi — yechimni '
                    'oʻzi topadi. <strong>imitation</strong> eng kuchli tuzoq va matnga '
                    'toʻgʻridan-toʻgʻri zid: nusxa koʻchirish uchun avval koʻrish kerak.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>A pencil contains no lead at all. The grey material is graphite, which '
                'was called black lead when a large deposit was found in Cumbria in the '
                '1560s, and the name ______ long after the chemistry had been sorted '
                'out.</p>',
     'question_text': WORD_Q,
     'choices': ['changed', 'persisted', 'spread', 'vanished'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>persisted</strong>. Birinchi jumla natijani '
                    'allaqachon koʻrsatadi: bugun ham "lead" deymiz, garchi qoʻrgʻoshin '
                    'boʻlmasa ham. <strong>vanished</strong> aynan teskari va matnning '
                    'birinchi jumlasi uni rad etadi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>A bell cannot be hammered into shape: the note depends on a thickness '
                'that varies by millimetres from lip to crown. It has to be <u>cast</u> '
                '— poured as molten bronze into a mould built to exactly those '
                'thicknesses, and then left to cool slowly.</p>',
     'question_text': 'As used in the text, what does the word <u>cast</u> most nearly '
                      'mean?',
     'choices': ['discarded', 'moulded', 'thrown', 'tuned'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>moulded</strong>. Taʼrif tiredan keyin darhol '
                    'keladi: "poured as molten bronze into a mould". '
                    '<strong>thrown</strong> "cast" soʻzining eng keng tarqalgan kundalik '
                    'maʼnosi va shuning uchun eng kuchli tuzoq.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'easy',
     'passage': '<p>Braille’s system uses six dots because Louis Braille had used '
                'twelve and found it wrong. The twelve-dot code he learned from an army '
                'officer could carry more characters, but a cell that tall cannot be read '
                'without running the fingertip up and down it. Six dots fit under a finger '
                'that does not move. The reduction is what made the system fast.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that twelve-dot codes can carry more information than six-dot codes',
         'To compare Braille with other tactile writing systems of the period',
         'To describe the military code from which Braille’s system was adapted',
         'To explain that the system’s key feature is a cell small enough to read without moving the finger',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To explain that the</strong>… Matn oxirgi ikki '
                    'jumlada fikrini aytadi: olti nuqta qimirlamaydigan barmoq ostiga '
                    'sigʻadi, va aynan qisqartirish tezlik bergan. <strong>To argue that '
                    'twelve-dot codes can carry more information</strong>… matnda bu rost '
                    'deb aytiladi, lekin u dalil, maqsad emas — matn uni yon berish '
                    'sifatida ishlatadi.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>No two snowflakes are alike, which is true and slightly beside the '
                'point. <u>The interesting fact is that the six arms of one flake are '
                'alike.</u> Each arm grows at its own tip, in response to the temperature '
                'and the humidity it is passing through — and because all six pass '
                'through the same conditions at the same moments, they record the same '
                'history in the same order.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It concedes that the familiar claim about snowflakes is false.',
         'It gives an example of the process described in the final sentence.',
         'It redirects the text from a familiar claim to the one it goes on to explain.',
         'It restates the first sentence in more precise terms.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>It redirects the text</strong>… Birinchi jumla '
                    'mashhur faktni "beside the point" deb chetga suradi, bu jumla esa '
                    'oʻrniga boshqasini qoʻyadi, keyingi jumla esa aynan shuni '
                    'tushuntiradi. <strong>It concedes that the familiar claim about '
                    'snowflakes is false</strong>… notoʻgʻri: matn uni "true" deb '
                    'ataydi.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'medium',
     'passage': '<p><b>Text 1</b><br>Meta-analyses find almost no relation between homework '
                'and achievement in primary school. The correlation appears only in '
                'secondary school, and even there it is modest. Several districts have '
                'concluded that homework before the age of eleven is time spent for no '
                'measurable return.</p>'
                '<p><b>Text 2</b><br>Ingrid Solberg accepts the finding on achievement and '
                'thinks the conclusion drawn from it is too quick. Test scores are not the '
                'only thing a school is trying to produce. If twenty minutes of reading at '
                'home builds a habit that pays off at fourteen, a study measuring maths '
                'scores at nine will not see it.</p>',
     'question_text': 'Based on the texts, Solberg’s objection to the conclusion in '
                      'Text 1 is that',
     'choices': [
         'homework does in fact raise achievement in primary school.',
         'secondary-school homework has been studied less carefully than primary.',
         'the meta-analyses were carried out on too small a sample.',
         'the outcome being measured may not be the outcome that matters.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>the outcome being measured</strong>… Solberg '
                    'birinchi jumladayoq natijani qabul qiladi va eʼtirozni '
                    '<em>oʻlchanayotgan narsaga</em> koʻchiradi: ball emas, odat. '
                    '<strong>homework does in fact raise achievement in primary '
                    'school</strong>… matnga zid — u "accepts the finding on '
                    'achievement" deydi.'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>In 1995 the Hubble telescope was pointed for ten days at a patch of sky '
                'the size of a grain of sand held at arm’s length, chosen because it '
                'appeared to contain nothing at all. The exposure returned about three '
                'thousand galaxies. The image is usually described as a picture of deep '
                'space. It is better described as a measurement of how wrong '
                '“nothing” was.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Astronomers in 1995 did not know how many galaxies the universe contained.',
         'The Hubble telescope requires very long exposures to detect distant galaxies.',
         'The image’s significance lies in what it revealed about an apparently empty patch of sky.',
         'The patch of sky chosen for the exposure was smaller than any studied before.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>The image’s significance lies</strong>… '
                    'Matn oxirgi jumlada oʻz fikrini aytadi: bu chuqur fazo surati emas, '
                    '"hech narsa" degan soʻz qanchalik notoʻgʻri ekanining oʻlchovi. '
                    '<strong>The Hubble telescope requires very long exposures</strong>… '
                    'matndagi detal (oʻn kun), asosiy fikr emas.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>A Venus flytrap does not close when it is touched. It closes when a '
                'trigger hair is bent twice within about twenty seconds, and it does not '
                'seal and begin digesting until it has been bent three more times. The '
                'plant is counting, and the count is a check: a raindrop bends one hair '
                'once, while an insect walking across the lobe bends several, '
                'repeatedly.</p>',
     'question_text': 'According to the text, what does the trap’s counting '
                      'accomplish?',
     'choices': [
         'It allows the plant to close more quickly than it otherwise could.',
         'It distinguishes prey from things that cannot be eaten.',
         'It ensures that the trap reopens if nothing has been caught.',
         'It measures the size of the insect that has landed on the lobe.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>It distinguishes prey</strong>… Matn sanashni '
                    '"a check" deb ataydi va ikki nuqtadan keyin nimani nimadan '
                    'ajratishini aytadi: bir marta tegadigan tomchi va bir necha marta '
                    'tegadigan hasharot. <strong>It measures the size of the insect</strong>… '
                    'oʻlcham haqida matnda bir soʻz ham yoʻq.'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A researcher proposes that a crow’s hook-making is not a stored '
                'recipe but a solution worked out on the spot — which would mean a '
                'bird ought to produce a different tool when the shape of the problem '
                'changes.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'researcher’s proposal?',
     'choices': [
         'Crows can be trained to drop stones into a water tube to raise a floating reward.',
         'Crows in the wild use twigs to extract grubs from holes in trees.',
         'Given a tube too narrow for a hook, the same birds flatten the wire into a blade instead.',
         'Young crows watch adults handling tools before they try for themselves.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Given a tube too</strong>… Taklifning sinovi '
                    'matnda aytilgan: muammo shakli oʻzgarsa, qurol ham oʻzgarishi kerak. '
                    'Ilgak oʻrniga tigʻ — aynan shu. <strong>Young crows watch adults '
                    'handling tools</strong>… aksincha ishlaydi: u yodlangan usul '
                    'versiyasini quvvatlaydi.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>An astronomer claims that the value of the Deep Field lies in the way '
                'the patch was chosen — that the result would mean much less if the '
                'field had been picked for something already known to be in it.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'astronomer’s claim?',
     'choices': [
         'The exposure lasted for ten consecutive days.',
         'The field lies within the constellation Ursa Major.',
         'The field was selected for containing no bright stars, no known galaxies and no radio sources, so that whatever appeared had not been selected for.',
         'The image has since been superseded by longer exposures of other fields.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>The field was selected</strong>… Daʼvo '
                    '<em>tanlov usuli</em> haqida, demak dalil maydonning qanday '
                    'tanlanganini va bu nega muhimligini koʻrsatishi kerak. <strong>The '
                    'exposure lasted for ten consecutive days</strong>… texnik detal: u '
                    'suratning qanchalik chuqurligini aytadi, tanlovning halolligini '
                    'emas.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>Four studies reported the correlation between time spent on homework '
                'and test scores among pupils of different ages.</p>'
                '<table><tr><th>Study</th><th>Median age of pupils</th>'
                '<th>Correlation with test score</th></tr>'
                '<tr><td>Study 1</td><td>8</td><td>0.02</td></tr>'
                '<tr><td>Study 2</td><td>11</td><td>0.08</td></tr>'
                '<tr><td>Study 3</td><td>14</td><td>0.21</td></tr>'
                '<tr><td>Study 4</td><td>17</td><td>0.29</td></tr></table>',
     'question_text': 'A student claims that the correlation grows with the age of the '
                      'pupils. Which choice best describes data from the table that support '
                      'this claim?',
     'choices': [
         'All four of the studies reported a positive correlation.',
         'Study 1’s pupils had a median age of 8.',
         'Study 4 reported a correlation of 0.29.',
         'The correlation rose at every step, from 0.02 at a median age of 8 to 0.29 at a median age of 17.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The correlation rose</strong>… Daʼvo ikki '
                    'kattalikning birga oʻsishi haqida, demak dalil ham ikkalasini butun '
                    'jadval boʻylab olishi kerak. <strong>All four of the studies reported '
                    'a positive correlation</strong>… rost, lekin u oʻsishni emas, faqat '
                    'ishorani koʻrsatadi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>A reading finger takes in what lies under its pad without moving. A '
                'six-dot cell fits there; a twelve-dot cell does not, and the finger has to '
                'travel up and down each character before moving on to the next. The speed '
                'of a tactile code therefore depends less on how many characters it can '
                'encode than on ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'how many dots are raised in each character.',
         'how quickly the reader was able to learn the code.',
         'the material the page has been printed on.',
         'whether a whole cell fits under a stationary fingertip.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>whether a whole</strong>… Matn sekinlikning '
                    'sababini aniq koʻrsatadi: barmoq har bir belgi boʻylab yurishga majbur '
                    'boʻladi. Demak tezlikni belgilaydigan narsa — katak barmoq ostiga '
                    'sigʻadimi. <strong>how many dots are raised in each character</strong> '
                    'tuzoq: masala nuqtalar sonida emas, katakning balandligida.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>Each arm of a snowflake grows at its own tip, and what it grows depends '
                'on the temperature and the humidity at that moment. The six arms are '
                'carried through the cloud together. A flake whose six arms did not match '
                'would therefore be evidence that ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'snowflakes have more than six arms in some clouds.',
         'the arms had not travelled through the same conditions.',
         'the flake had begun to melt before it was photographed.',
         'the flake had formed at an unusually low temperature.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>the arms had not</strong>… Matn sababni beradi: '
                    'qoʻllar bir xil boʻladi, chunki birga sayohat qiladi. Agar ular bir '
                    'xil boʻlmasa, sayohat ham bir xil boʻlmagan. <strong>the flake had '
                    'begun to melt</strong> matnda muhokama qilinmagan — erish haqida '
                    'bir soʻz ham yoʻq.'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>Louis Braille, the student who cut the military code down from twelve '
                'dots to ______ was fifteen years old when he finished the system.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['six', 'six,', 'six:', 'six;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>six,</strong>. "the student who…to six" — '
                    '<em>Louis Braille</em> ga izoh, vergul bilan ochilgan, demak vergul '
                    'bilan yopiladi. <strong>six;</strong> notoʻgʻri: nuqtali vergul ikki '
                    'mustaqil gapni ajratadi, bu yerda esa ega hali kesimini kutyapti.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>A bell cannot be hammered into ______ the note depends on thicknesses '
                'that vary by millimetres.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['shape', 'shape and,', 'shape,', 'shape;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>shape;</strong>. Boʻshliqning ikki tomonida ham '
                    'toʻliq mustaqil gap turibdi, ularni nuqtali vergul ajratadi. '
                    '<strong>shape,</strong> — comma splice, ingliz tilidagi eng keng '
                    'tarqalgan punktuatsiya xatosi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Because all six arms pass through the same air at the same ______ they '
                'record the same history in the same order.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['moments', 'moments,', 'moments:', 'moments;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>moments,</strong>. Gap "Because…" bilan '
                    'boshlangan ergash gapdan boshlanadi, va gap boshida turgan ergash gap '
                    'asosiy gapdan vergul bilan ajratiladi. <strong>moments;</strong> '
                    'notoʻgʻri: nuqtali vergul ikki <em>mustaqil</em> gap orasida turadi.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The series of trigger hairs on the inner face of a flytrap’s lobes '
                '______ the plant to count.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['allow', 'allows', 'are allowing', 'have allowed'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>allows</strong>. Ega — <em>series</em>, '
                    'birlik; "of trigger hairs on the inner face of a flytrap’s lobes" '
                    'faqat aniqlovchi. Feʼlga yaqin turgan "lobes" koʻplik boʻlgani uchun '
                    'quloq <strong>allow</strong> ga tortadi.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time the Deep Field image was released in 1996, the telescope '
                '______ at the same patch of sky for ten days.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['had been pointing', 'has been pointing', 'points', 'will have pointed'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>had been pointing</strong>. "By the time…was '
                    'released" oʻtmishdagi nuqtani beradi, kuzatuv esa undan oldin '
                    'boshlanib oʻsha nuqtagacha davom etgan — past perfect '
                    'continuous. <strong>has been pointing</strong> hozirgi paytga '
                    'ulaydi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>The four ______ correlations, one for each age group that was '
                'studied, ranged from 0.02 up to 0.29.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['studies', 'studies’', 'studies’s', 'study’s'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>studies’</strong>. Tadqiqotlar toʻrtta '
                    '("The four"), korrelyatsiyalar ularniki — koʻplikdagi egalik '
                    '<em>-s</em> dan keyin faqat apostrof qoʻyiladi. '
                    '<strong>study’s</strong> birlik egalik boʻlib, "four" bilan '
                    'ziddiyatga kiradi.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>A crow solves the problem by inspecting the tube, by choosing a piece '
                'of wire, and by ______</p>',
     'question_text': CONVENTION_Q,
     'choices': ['a bend into a hook.', 'bend it into a hook.', 'bending it into a hook.',
                 'it is bent into a hook.'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>bending it into a hook.</strong> Qator '
                    '"by inspecting…by choosing…and by ___" — har bir aʼzo '
                    '<em>by</em> + <em>-ing</em> shaklida, demak uchinchisi ham shunday '
                    'boʻlishi shart. <strong>it is bent into a hook.</strong> butun '
                    'boshli gap qoʻshadi va qatorning shaklini sindiradi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>A Shinkansen line shares no track with slower trains. ______ no '
                'Shinkansen has been derailed in a collision in sixty years of '
                'service.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['By contrast,', 'Nevertheless,', 'Partly as a result,', 'Previously,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Partly as a result,</strong>. Alohida yoʻl '
                    '— sabab, toʻqnashuvsiz oltmish yil — natija. '
                    '<strong>Nevertheless,</strong> qarama-qarshilik talab qiladi, bu yerda '
                    'esa ikkala jumla bir tomonga qaraydi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Graphite is not lead, and chemists had established as much by the end '
                'of the eighteenth century. ______ the name “pencil lead” is '
                'still in everyday use.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'Even now,', 'For instance,', 'Likewise,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Even now,</strong>. Ikki asr oldingi bilim va '
                    'bugungi odat bir-biriga mos kelmaydi — vaqt orqali berilgan '
                    'ziddiyat. <strong>Accordingly,</strong> aynan teskari: u "shuning '
                    'uchun nom saqlanib qoldi" degan maʼnoni beradi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>A meta-analysis of primary-school homework finds almost no effect on '
                'test scores. ______ test scores are not the only thing a school sets out '
                'to produce.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'For example,', 'However,', 'Similarly,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>However,</strong>. Birinchi jumla xulosaga olib '
                    'boradi, ikkinchisi esa oʻsha xulosani cheklaydi — qarama-'
                    'qarshilik. <strong>Accordingly,</strong> ikkinchi jumlani '
                    'birinchisidan kelib chiqadi deb qoʻyadi, aslida u uni '
                    'toʻxtatib turadi.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Louis Braille learned a twelve-dot code from an army officer.</li>'
                '<li>A twelve-dot cell cannot be read without moving the fingertip.</li>'
                '<li>Braille reduced the cell to six dots.</li>'
                '<li>A six-dot cell fits under a stationary fingertip.</li>'
                '<li>Braille finished the system at the age of fifteen.</li></ul>',
     'question_text': 'The student wants to emphasize why reducing the cell mattered. Which '
                      'choice most effectively uses relevant information from the notes to '
                      'accomplish this goal?',
     'choices': [
         'A six-dot cell fits under a fingertip that does not move.',
         'Braille cut the cell from twelve dots to six, so that a whole character fits under a fingertip that need not move — which is what made the system fast to read.',
         'Braille finished the system when he was fifteen years old.',
         'Louis Braille learned a twelve-dot code from an army officer.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Braille cut the cell</strong>… Maqsad '
                    '<em>nega muhim</em> ekanini koʻrsatish, demak javobda oʻzgarish '
                    '(12 → 6) ham, uning oqibati (barmoq qimirlamaydi, oʻqish tez) ham '
                    'boʻlishi kerak. <strong>A six-dot cell fits under a fingertip that '
                    'does not move</strong>… faqat natijani aytadi, nimadan oʻzgarganini '
                    'emas.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>A Venus flytrap has trigger hairs on the inner face of each lobe.</li>'
                '<li>The trap closes when a hair is bent twice within about twenty '
                'seconds.</li>'
                '<li>It seals and digests only after three more bends.</li>'
                '<li>A raindrop bends one hair once.</li>'
                '<li>An insect bends several hairs repeatedly.</li></ul>',
     'question_text': 'The student wants to explain how the trap avoids closing on nothing. '
                      'Which choice most effectively uses relevant information from the '
                      'notes to accomplish this goal?',
     'choices': [
         'A raindrop bends one hair once, while an insect bends several repeatedly — so requiring two bends to close and three more to digest lets the trap tell one from the other.',
         'A Venus flytrap has trigger hairs on the inner face of each of its lobes.',
         'The trap closes when a trigger hair is bent twice within about twenty seconds.',
         'The trap seals and begins digesting only after three further bends.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>A raindrop bends one</strong>… Maqsad tuzoq '
                    '<em>qanday ajratishini</em> tushuntirish, demak javobda ikki holat '
                    'ham (tomchi va hasharot) va ularni ajratadigan qoida ham boʻlishi '
                    'kerak. <strong>The trap closes when a trigger hair is bent '
                    'twice</strong>… qoidaning yarmini beradi, lekin nimani nimadan '
                    'ajratayotgani koʻrinmaydi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>In 1995 Hubble was pointed at a patch of sky the size of a grain of '
                'sand held at arm’s length.</li>'
                '<li>The patch was chosen because it appeared to contain nothing.</li>'
                '<li>The field held no bright stars and no previously known galaxies.</li>'
                '<li>The exposure lasted ten days.</li>'
                '<li>The image returned about three thousand galaxies.</li></ul>',
     'question_text': 'The student wants to emphasize why the choice of an empty field '
                      'mattered. Which choice most effectively uses relevant information '
                      'from the notes to accomplish this goal?',
     'choices': [
         'In 1995 Hubble was pointed at a patch of sky the size of a grain of sand held at arm’s length.',
         'The exposure lasted ten days and returned about three thousand galaxies.',
         'The field held no bright stars and no previously known galaxies.',
         'The patch was chosen precisely because it seemed to hold nothing — no bright stars, no known galaxies — so the three thousand galaxies that appeared had not been selected for.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The patch was chosen</strong>… Maqsad tanlovning '
                    '<em>ahamiyatini</em> koʻrsatish, demak javobda maydonning boʻshligi '
                    'ham, natija ham, va ularning bogʻi ham boʻlishi kerak. <strong>The '
                    'exposure lasted ten days and returned about three thousand '
                    'galaxies</strong>… natijani aytadi, lekin nega u ishonarli ekanini '
                    'aytmaydi.'},
]
