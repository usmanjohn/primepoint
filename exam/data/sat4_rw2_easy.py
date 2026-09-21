# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 4 · Reading and Writing, Module 2 (LOWER)
#  27 questions · 32 minutes · taken by a pupil who scored under 18 on rw1.
#
#  Same domains, same counts, same order as the upper module — one-step
#  reasoning, familiar wording, the point in the opening sentence.
#
#  Load: python manage.py load_mock exam/data/sat4_rw2_easy.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §3
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
     'passage': '<p>Rachel Carson had written three popular books about the sea before '
                '<i>Silent Spring</i>, and the campaign mounted against her in 1962 '
                'attacked her ______ rather than her evidence: she was called an amateur, '
                'a hysteric and a spinster, but almost none of the published attacks '
                'disputed a measurement.</p>',
     'question_text': WORD_Q,
     'choices': ['character', 'employer', 'prose', 'publisher'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>character</strong>. Ikki nuqtadan keyingi '
                    'roʻyxat — havaskor, isterik, turmushga chiqmagan — '
                    'hammasi odamning oʻziga qaratilgan, dalilga emas. '
                    '<strong>prose</strong> chalgʻituvchi, chunki u ham kitobga '
                    'tegishlidek tuyuladi; lekin sanalgan soʻzlar yozuv uslubi haqida '
                    'emas.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>Some bamboos flower once, all together across a whole region, and then '
                'die. A grove grown from a single parent will flower on the same schedule '
                'even when pieces of it have been carried to other continents, which '
                'suggests that the timing is ______ rather than a response to local '
                'weather.</p>',
     'question_text': WORD_Q,
     'choices': ['accidental', 'gradual', 'inherited', 'recent'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>inherited</strong>. Kalit dalil shu: bir '
                    'ota-onadan olingan boʻlaklar boshqa qitʼada ham <em>bir vaqtda</em> '
                    'gullaydi — demak jadval iqlimda emas, oʻsimlikning oʻzida. '
                    '<strong>accidental</strong> aynan teskari: tasodif butun mintaqani '
                    'bir kunga tenglashtira olmaydi.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>The Miura fold turns a flat sheet into a pattern of parallelograms that '
                'collapses along every crease at once. Pull one corner and the whole sheet '
                'opens; push it and the sheet closes. A map folded this way needs only a '
                'single ______, which is why the pattern was sent into orbit on a solar '
                'panel.</p>',
     'question_text': WORD_Q,
     'choices': ['colour', 'material', 'motion', 'sheet'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>motion</strong>. Oldingi jumla aynan shuni '
                    'tasvirlaydi: bitta burchakni tortsang, butun varaq ochiladi — '
                    'bitta harakat yetarli. <strong>material</strong> notoʻgʻri: matn '
                    'materialni emas, buklash usulini muhokama qiladi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>Melted chocolate can set into six different crystal forms, and only one '
                'of them is glossy and snaps cleanly. A chocolatier reaches it by heating '
                'the chocolate, cooling it and warming it slightly again, so that the wrong '
                'crystals melt away and the right ones <u>seed</u> the rest.</p>',
     'question_text': 'As used in the text, what does the word <u>seed</u> most nearly '
                      'mean?',
     'choices': ['bury', 'plant', 'scatter', 'start'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>start</strong>. Toʻgʻri kristallar qolgan '
                    'massaning qotishini <em>boshlab beradi</em> — ular namuna '
                    'boʻlib xizmat qiladi. <strong>plant</strong> "seed" soʻzining '
                    'bogʻdorchilikdagi maʼnosi va eng kuchli tuzoq: bu yerda hech narsa '
                    'ekilmayapti.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'easy',
     'passage': '<p>Wheeled objects have been dug from Mesoamerican sites for a century: '
                'small clay animals on axles, plainly toys. No cart has ever been found. '
                'The usual explanation is that the wheel was never invented there, which '
                'the toys contradict. The better explanation is that there was nothing to '
                'pull a cart — no horse and no ox — and highland routes a wheel '
                'would have to be carried up rather than rolled.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that a familiar puzzle is explained by the absence of draught animals rather than of the idea',
         'To compare Mesoamerican transport technology with that of Eurasia',
         'To describe the clay toys that have been excavated at Mesoamerican sites',
         'To question whether the excavated objects were in fact toys',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>To argue that a</strong>… Matn odatdagi '
                    'izohni oʻyinchoqlar bilan yiqitadi va oʻrniga boshqasini qoʻyadi: '
                    'gʻoya bor edi, tortadigan hayvon yoʻq edi. <strong>To question '
                    'whether the excavated objects were in fact toys</strong>… matnga '
                    'zid — u ularni "plainly toys" deb ataydi.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>An emperor penguin standing alone in an Antarctic winter would lose '
                'heat faster than it could produce it. <u>The huddle is not a shelter but '
                'a circulation.</u> Birds on the windward edge shuffle down the side of the '
                'group and rejoin it at the back, so that over a few hours every bird '
                'spends time in the middle and time on the outside, and the whole mass '
                'creeps slowly downwind.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It corrects a likely assumption about the huddle, and the rest of the text explains the correction.',
         'It gives an example of the behaviour described in the first sentence.',
         'It offers evidence that a single penguin cannot survive the winter.',
         'It summarizes the conclusion the text reaches at its end.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>It corrects a likely</strong>… Jumla "boshpana '
                    'emas, aylanma" deb kutilgan tushunchani tuzatadi, keyingi jumla esa '
                    'aylanmaning qanday ishlashini tushuntiradi. <strong>It gives an '
                    'example of the behaviour</strong>… notoʻgʻri: misol undan keyin '
                    'keladi, jumlaning oʻzida xulq tasviri yoʻq.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'medium',
     'passage': '<p><b>Text 1</b><br>When a city takes a traffic lane and gives it to '
                'bicycles, drivers predict gridlock. The measurements usually disagree: on '
                'most corridors where this has been done, car journey times change by less '
                'than a minute, because the lane that was removed was never the constraint. '
                'Junctions are.</p>'
                '<p><b>Text 2</b><br>Marta Oliveira agrees about the junctions and warns '
                'against the generalisation. The corridors that get bike lanes are chosen '
                'because they are wide, flat and already busy with cyclists — exactly '
                'the places where a lane can be spared. What the measurements show is that '
                'the policy works where it has been tried, not that it would work '
                'anywhere.</p>',
     'question_text': 'Based on the texts, Oliveira’s reservation about the finding in '
                      'Text 1 concerns',
     'choices': [
         'how the corridors that produced the finding were selected.',
         'the number of cyclists who actually use the new lanes.',
         'whether car journey times were measured accurately.',
         'whether junctions are in fact the main constraint on traffic.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>how the corridors that</strong>… 2-matn '
                    'oʻlchovni ham, chorrahalar haqidagi xulosani ham qabul qiladi; u '
                    'faqat <em>tanlov</em>ga eʼtiroz bildiradi: keng va tekis yoʻllar '
                    'ataylab tanlangan. <strong>whether junctions are in fact the main '
                    'constraint</strong>… matn ochiq rad etadi — "agrees about the '
                    'junctions".'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>Florence Nightingale’s rose diagram of mortality in the Crimea was '
                'not made to be admired. She had figures showing that more soldiers were '
                'dying of preventable disease than of wounds, and she had a government that '
                'did not read tables. The diagram takes that single fact and makes it '
                'impossible to look away from: the wedges for disease dwarf the wedges for '
                'wounds, month after month, on one page.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'More soldiers in the Crimea died of their wounds than historians once believed.',
         'Nightingale designed the diagram as an instrument of persuasion for readers who would not read a table.',
         'Nightingale was the first person to display statistics in a circular chart.',
         'The government of the day had no mortality figures until Nightingale supplied them.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Nightingale designed the diagram</strong>… Matn '
                    'birinchi jumlada maqsadni rad etadi ("not made to be admired") va '
                    'ikkinchisida haqiqiy sababni beradi: jadval oʻqimaydigan hukumat. '
                    '<strong>Nightingale was the first person to display statistics in a '
                    'circular chart</strong>… matnda birinchilik haqida hech narsa '
                    'aytilmagan.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>Beethoven’s metronome marks have troubled performers for two '
                'centuries: taken literally, many are faster than most orchestras play. The '
                'explanations offered have included a faulty metronome, a misreading of the '
                'scale and plain carelessness. But the marks are consistent with each other '
                '— fast movements and slow movements are marked in the same '
                'proportion throughout — which is what makes the faulty-machine '
                'explanation hard to sustain.</p>',
     'question_text': 'According to the text, why is the faulty-metronome explanation '
                      'difficult to maintain?',
     'choices': [
         'Beethoven’s marks are consistent with one another across fast and slow movements.',
         'Modern orchestras play the marked tempos without any difficulty.',
         'No metronome from the period has survived to be tested.',
         'Other composers of the period used exactly the same marks.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Beethoven’s marks are consistent</strong>… '
                    'Matn sababni tiredan keyin oʻzi aytadi: belgilar oʻzaro mos. Buzuq '
                    'asbob tasodifiy xato berardi, izchil xato emas. <strong>Modern '
                    'orchestras play the marked tempos without any difficulty</strong>… '
                    'matnga zid: "faster than most orchestras play".'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A researcher proposes that the slow downwind drift of a penguin huddle '
                'is a by-product of individual birds rejoining at the back rather than a '
                'movement the group coordinates — which would mean the drift should '
                'appear even when no bird is responding to where the others are going.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'researcher’s proposal?',
     'choices': [
         'Emperor penguins can survive air temperatures below −40°C.',
         'Huddles are larger in colder weather than they are in milder weather.',
         'In a computer model where each bird moves only when the gap in front of it exceeds a fixed distance, the simulated huddle drifts downwind at the observed rate.',
         'Penguins on the outside of a huddle lose heat faster than those in the middle.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>In a computer model</strong>… Taklif '
                    'siljish <em>muvofiqlashtirishsiz</em> ham chiqadi deydi. Modelda har '
                    'bir qush faqat oldidagi boʻshliqqa qaraydi — va siljish baribir '
                    'paydo boʻladi. <strong>Penguins on the outside of a huddle lose heat '
                    'faster</strong>… nega toʻpga yigʻilishini izohlaydi, siljish sababini '
                    'emas.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A historian claims that Nightingale designed her diagram for one '
                'particular reader — that its shape was chosen to work on a minister '
                'who would never sit down with a table of figures.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'historian’s claim?',
     'choices': [
         'Nightingale trained as a nurse before she began collecting statistics.',
         'Nightingale’s covering letter asks that the diagram be framed and hung in the War Office where it could not be avoided.',
         'The diagram uses twelve wedges, one for each month of the year.',
         'The same figures appear in an appendix of tables later in the report.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Nightingale’s covering letter</strong>… '
                    'Daʼvo <em>maqsadli oʻquvchi</em> haqida, va xat aynan shuni '
                    'koʻrsatadi: qayerga osilishi va nega. <strong>The same figures appear '
                    'in an appendix of tables</strong>… aksincha ishlaydi — u '
                    'jadvalning ham berilganini koʻrsatadi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>Four corridors in one city gave a traffic lane over to bicycles. The '
                'table shows the change in average car journey time along each corridor and '
                'the change in the number of cyclists counted there each morning.</p>'
                '<table><tr><th>Corridor</th><th>Change in car journey time (min)</th>'
                '<th>Change in morning cyclists</th></tr>'
                '<tr><td>Rua Norte</td><td>+0.4</td><td>+310</td></tr>'
                '<tr><td>Avenida Sul</td><td>+0.9</td><td>+505</td></tr>'
                '<tr><td>Rua Velha</td><td>+0.3</td><td>+180</td></tr>'
                '<tr><td>Avenida Leste</td><td>+0.6</td><td>+420</td></tr></table>',
     'question_text': 'A student claims that car journey times changed very little while '
                      'cycling rose substantially. Which choice best describes data from '
                      'the table that support this claim?',
     'choices': [
         'Avenida Sul gained 505 morning cyclists.',
         'Every one of the four corridors gave a traffic lane over to bicycles.',
         'No corridor’s car journey time rose by as much as a minute, while every corridor gained at least 180 morning cyclists.',
         'Rua Velha had the smallest change in car journey time of the four.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>No corridor’s car journey</strong>… Daʼvo '
                    'ikki qismli — avtomobil vaqti <em>kam</em> oʻzgardi, velosiped '
                    '<em>koʻp</em> oshdi — demak dalil ikkala ustunni ham qamrashi '
                    'kerak. <strong>Avenida Sul gained 505 morning cyclists</strong>… '
                    'bitta katak: undan "juda kam oʻzgardi" degan yarmi chiqmaydi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>A bamboo that flowers once and dies leaves an enormous crop of seed on '
                'a forest floor that has just lost its bamboo. The animals that eat seed '
                'cannot get through it all in one season, because there is far more of it '
                'than usual and the glut does not come again for decades. The synchrony is '
                'therefore ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'a defence that works only if every plant does it at once.',
         'a response to the amount of rainfall in a given year.',
         'more common in bamboos that produce smaller seeds.',
         'unrelated to the survival of the seedlings.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>a defence that works</strong>… Matn '
                    'mexanizmni beradi: urugʻ shu qadar koʻp boʻladiki, hayvonlar '
                    'ulgurmaydi. Bu faqat hamma bir vaqtda gullaganda ishlaydi — '
                    'bitta oʻsimlik yakka gullasa, uni yeb qoʻyishadi. '
                    '<strong>unrelated to the survival of the seedlings</strong> matnning '
                    'butun mantiqiga zid.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>An ordinary road map has folds in two directions, and each set has to '
                'be worked separately; a corner tears because the user opens one direction '
                'before the other. The Miura pattern has a single degree of freedom: every '
                'crease moves together, or none of them moves. A map folded in the Miura '
                'pattern is therefore ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'cheaper to manufacture than an ordinary road map.',
         'impossible to open in the wrong order.',
         'larger when open than an ordinary road map.',
         'readable only when it has been fully opened.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>impossible to open in</strong>… Matn yirtilish '
                    'sababini aytadi: foydalanuvchi bir yoʻnalishni oldin ochadi. Miura '
                    'naqshida esa barcha burmalar birga harakatlanadi — demak '
                    '"notoʻgʻri tartib" degan narsaning oʻzi qolmaydi. Qolgan uchtasi '
                    'matnda umuman muhokama qilinmagan.'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>Florence Nightingale, the statistician who drew the rose diagram of '
                'mortality in the ______ wanted it hung where ministers could not avoid '
                'it.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['Crimea', 'Crimea,', 'Crimea:', 'Crimea;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Crimea,</strong>. "the statistician who…Crimea" '
                    '— <em>Florence Nightingale</em> ga izoh, vergul bilan ochilgan, '
                    'demak vergul bilan yopiladi. <strong>Crimea;</strong> notoʻgʻri: '
                    'nuqtali vergul ikki mustaqil gap orasida turadi, bu yerda esa ega '
                    'hali kesimini kutyapti.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Bamboo seed is extraordinarily abundant in a mast ______ however, the '
                'glut lasts only a single season.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['year', 'year and', 'year,', 'year;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>year;</strong>. <em>however</em> bogʻlovchi '
                    'emas, kirish soʻz: u ikki mustaqil gapni ulay olmaydi, shuning uchun '
                    'ular orasida nuqtali vergul kerak. <strong>year,</strong> — '
                    'comma splice, va bu savolning butun tuzogʻi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Because every crease in the Miura pattern moves ______ the sheet cannot '
                'be opened in the wrong order.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['together', 'together,', 'together:', 'together;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>together,</strong>. Gap "Because…" bilan '
                    'boshlangan ergash gapdan boshlanadi, va gap boshida turgan ergash gap '
                    'asosiy gapdan vergul bilan ajratiladi. <strong>together;</strong> '
                    'notoʻgʻri: nuqtali vergul ikki <em>mustaqil</em> gap orasida turadi.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The set of metronome marks that Beethoven left for his symphonies '
                '______ consistent from one movement to the next.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are', 'have been', 'is', 'were being'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>is</strong>. Ega — <em>set</em>, birlik; '
                    '"of metronome marks that Beethoven left for his symphonies" faqat '
                    'aniqlovchi. Feʼlga yaqin turgan "symphonies" koʻplik boʻlgani uchun '
                    'quloq <strong>are</strong> ga tortadi — oraliq iborani yoping va '
                    'egani toping.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time <i>Silent Spring</i> appeared in 1962, Carson ______ three '
                'books about the sea.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['had published', 'has published', 'publishes', 'will have published'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>had published</strong>. "By the time…appeared" '
                    'oʻtmishdagi nuqtani beradi, uchta kitob esa undan <em>oldin</em> '
                    'chiqqan — past perfect. <strong>has published</strong> hozirgi '
                    'paytga ulaydi, gap esa 1962-yilda tugagan.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>The four ______ journey times all rose by less than a minute.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['corridor’s', 'corridors', 'corridors’', 'corridors’s'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>corridors’</strong>. Yoʻnalishlar toʻrtta '
                    '("The four"), vaqtlar ularniki — koʻplikdagi egalik <em>-s</em> '
                    'dan keyin faqat apostrof qoʻyiladi. <strong>corridor’s</strong> '
                    'birlik egalik boʻlib, "four" bilan ziddiyatga kiradi.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>A chocolatier tempers chocolate by heating it, cooling it and '
                '______</p>',
     'question_text': CONVENTION_Q,
     'choices': ['it is warmed again.', 'warm it again.', 'warming again it.',
                 'warming it again.'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>warming it again.</strong> Qator "by heating '
                    'it, cooling it and ___" — ikkitasi ham <em>-ing</em> shaklida, '
                    'demak uchinchisi ham shunday boʻlishi shart (parallelizm). '
                    '<strong>it is warmed again.</strong> butun boshli gap qoʻshadi va '
                    'qatorning shaklini sindiradi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>An emperor penguin standing alone would lose heat faster than it could '
                'produce it. ______ the birds pack together so tightly that the air in the '
                'middle of a huddle can reach 37°C.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['By contrast,', 'For this reason,', 'Nevertheless,', 'Previously,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>For this reason,</strong>. Yolgʻiz qushning '
                    'issiqlik yoʻqotishi — sabab, zich yigʻilish — oʻsha sabab '
                    'tugʻdirgan xulq. <strong>Nevertheless,</strong> qarama-qarshilik '
                    'talab qiladi, bu yerda esa ikkala jumla bir tomonga qaraydi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>The campaign against Carson called her an amateur and a hysteric. '
                '______ almost none of the published attacks disputed a single measurement '
                'in her book.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'In contrast,', 'Likewise,', 'Therefore,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>In contrast,</strong>. Birinchi jumla shaxsga '
                    'qilingan hujum haqida, ikkinchisi esa dalilga <em>qilinmagan</em> '
                    'hujum haqida — ikki yoʻnalish qarama-qarshi. '
                    '<strong>Likewise,</strong> oʻxshashlik kutadi, lekin bu ikki holat '
                    'bir-biriga oʻxshamaydi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Junctions, not lanes, are what constrain traffic on most city '
                'corridors. ______ removing one lane between two junctions changes the '
                'journey very little.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'By contrast,', 'Nevertheless,', 'Previously,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Accordingly,</strong>. Agar toʻsiq chorrahada '
                    'boʻlsa, chorrahalar orasidagi qatorni olib tashlash deyarli hech '
                    'narsani oʻzgartirmaydi — bu toʻgʻridan-toʻgʻri natija. '
                    '<strong>Nevertheless,</strong> ziddiyat bildiradi, bu yerda esa '
                    'ikkinchi jumla birinchisidan kelib chiqadi.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Florence Nightingale collected mortality figures from the '
                'Crimea.</li>'
                '<li>More soldiers were dying of preventable disease than of wounds.</li>'
                '<li>The government of the day did not read statistical tables.</li>'
                '<li>Her rose diagram shows disease and wounds as wedges on one page.</li>'
                '<li>She asked that the diagram be hung in the War Office.</li></ul>',
     'question_text': 'The student wants to emphasize the purpose for which the diagram was '
                      'made. Which choice most effectively uses relevant information from '
                      'the notes to accomplish this goal?',
     'choices': [
         'Florence Nightingale collected mortality figures from the Crimean War.',
         'Nightingale had figures showing that disease killed more soldiers than wounds and a government that would not read a table; the diagram put the fact on one page, and she asked for it to be hung in the War Office.',
         'Nightingale’s rose diagram shows deaths from disease and from wounds as wedges on a single page.',
         'The government of the day did not read statistical tables.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Nightingale had figures showing</strong>… '
                    'Maqsadni koʻrsatish uchun uchta narsa kerak: nima aytmoqchi edi, kimga '
                    ', va nega aynan shu shaklda. Faqat shu variant uchalasini ham '
                    'ulaydi. <strong>The government of the day did not read statistical '
                    'tables</strong>… faqat toʻsiqni aytadi, javobni emas.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>An emperor penguin alone loses heat faster than it can produce '
                'it.</li>'
                '<li>In a huddle, birds on the windward edge shuffle down the side.</li>'
                '<li>They rejoin the group at the back.</li>'
                '<li>Every bird therefore spends time in the middle and time on the '
                'outside.</li>'
                '<li>The whole huddle creeps slowly downwind.</li></ul>',
     'question_text': 'The student wants to explain how the huddle works to an audience '
                      'unfamiliar with it. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'An emperor penguin standing alone would lose heat faster than it could produce it.',
         'Birds on the windward edge of a huddle shuffle down the side of the group.',
         'Birds on the windward edge shuffle down the side and rejoin at the back, so every bird takes a turn in the middle and on the outside — and the whole huddle drifts downwind as they do.',
         'The huddle creeps slowly downwind over the course of a few hours.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Birds on the windward</strong>… Maqsad '
                    '<em>ishlash tartibini</em> tushuntirish, demak javob harakatni '
                    'boshidan oxirigacha bersin: chetdan pastga → orqadan qoʻshilish → '
                    'har bir qushga navbat → butun toʻpning siljishi. Qolgan uchtasi '
                    'zanjirning bitta boʻgʻinini oladi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Wheeled clay animals on axles have been excavated at Mesoamerican '
                'sites.</li>'
                '<li>No wheeled cart has ever been found there.</li>'
                '<li>Mesoamerica had no horses and no oxen.</li>'
                '<li>Highland routes were steep and often stepped.</li>'
                '<li>The toys show that the wheel itself was known.</li></ul>',
     'question_text': 'The student wants to present the explanation together with the '
                      'evidence for it. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'Mesoamerica had neither horses nor oxen.',
         'No wheeled cart has ever been found at a Mesoamerican site.',
         'The toys show the wheel was known, but with no horse or ox and with steep, stepped highland routes there was nothing to pull a cart and nowhere easy to roll one.',
         'Wheeled clay animals on axles have been excavated at Mesoamerican sites.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>The toys show the</strong>… Maqsad ikki talabli: '
                    'izoh <em>va</em> uning dalili. Faqat shu variant oʻyinchoqni dalil '
                    'sifatida ishlatib (gʻoya bor edi), keyin sababni (hayvon va yoʻl) '
                    'beradi. <strong>No wheeled cart has ever been found</strong>… faqat '
                    'jumboqni takrorlaydi, uni yechmaydi.'},
]
