# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 3 · Reading and Writing, Module 2 (LOWER)
#  27 questions · 32 minutes · taken by a pupil who scored under 18 on rw1.
#
#  Same domains, same counts, same order as the upper module — one-step
#  reasoning, familiar wording, the point in the opening sentence.
#
#  Load: python manage.py load_mock exam/data/sat3_rw2_easy.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §3
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
     'passage': '<p>Marie Tharp was not allowed aboard the research ships that gathered the '
                'soundings she worked from; the rule of the time kept women ashore. She '
                'drew the first map of the Atlantic sea floor from measurements she had '
                'never ______ herself.</p>',
     'question_text': WORD_Q,
     'choices': ['collected', 'doubted', 'published', 'understood'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>collected</strong>. Birinchi jumla sababni '
                    'aytadi: u kemaga chiqa olmagan, demak oʻlchovlarni <em>oʻzi '
                    'olmagan</em>. <strong>understood</strong> notoʻgʻri va matnga zid '
                    '— u oʻsha raqamlardan xaritani chizgan, demak tushungan.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>Where sea otters were hunted out, sea urchins multiplied and grazed the '
                'kelp down to bare rock. The otter had been the only thing ______ the '
                'urchins, and once it was gone the forest went with it.</p>',
     'question_text': WORD_Q,
     'choices': ['attracting', 'feeding', 'limiting', 'protecting'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>limiting</strong>. Kalanlar yoʻqolgach, dengiz '
                    'kirpilari koʻpaydi — demak kalan ularning sonini '
                    '<em>ushlab turgan</em>. <strong>protecting</strong> aynan teskari: '
                    'kalan kirpini himoya qilmaydi, yeydi.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>A skilled user of a soroban stops moving the beads long before the '
                'answer is needed. With enough practice the abacus becomes ______: the user '
                'pictures the beads and shifts them in the mind, faster than a hand could '
                'shift them.</p>',
     'question_text': WORD_Q,
     'choices': ['decorative', 'internal', 'obsolete', 'shared'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>internal</strong>. Ikki nuqtadan keyingi qism '
                    'maʼnoni oʻzi beradi: hisoblash <em>ongda</em> kechadi. '
                    '<strong>obsolete</strong> (eskirgan) chalgʻituvchi, chunki qoʻl '
                    'ishlatilmay qoladi; lekin asbob keraksiz boʻlib qolmaydi — u '
                    'ichkariga koʻchadi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>No single monarch butterfly makes the round trip. Those that leave '
                'Mexico in spring die in Texas; their offspring carry on north, and it is '
                'the third or fourth generation that reaches Canada. The journey is '
                '<u>inherited</u> rather than remembered.</p>',
     'question_text': 'As used in the text, what does the word <u>inherited</u> most nearly '
                      'mean?',
     'choices': ['earned', 'imagined', 'passed down', 'shortened'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>passed down</strong>. Matn avlodlar zanjirini '
                    'tasvirlaydi va "remembered" ga qarshi qoʻyadi: hech bir kapalak '
                    'yoʻlni koʻrmagan, u nasldan naslga oʻtadi. <strong>earned</strong> '
                    'soʻzning meros-mulk maʼnosiga tortadi — lekin bu yerda oʻtayotgan '
                    'narsa xulq, mulk emas.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'easy',
     'passage': '<p>The Eiffel Tower is usually described as a tower with a decorative '
                'lattice. It is better described as a wind diagram. Eiffel’s engineers '
                'calculated the curve of the legs so that the pressure of wind on the '
                'structure would be carried straight down into the foundations, and the '
                'lattice exists because a solid surface would have caught the very wind the '
                'curve was designed to shed.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that the tower was unpopular with Parisians when it first opened',
         'To compare the tower with other structures built for the 1889 exposition',
         'To describe the materials from which the tower was built',
         'To explain that the tower’s shape and openwork are answers to wind rather than ornament',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To explain that the</strong>… Matn ikkinchi '
                    'jumlada oʻz fikrini qoʻyadi ("a wind diagram"), uchinchisi esa ikkala '
                    'belgini — egrilik va panjara — shamol bilan izohlaydi. '
                    '<strong>To describe the materials</strong>… notoʻgʻri: material '
                    'haqida matnda bitta ham soʻz yoʻq.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>Hildegard of Bingen wrote music, medicine, theology and a private '
                'alphabet, and she wrote all of it after the age of forty-two. <u>Her '
                'output is not a late flowering but a late permission.</u> She had been '
                'having the visions since childhood and had told almost nobody; what '
                'changed in 1141 was that she was told, by a voice she trusted, to write '
                'them down.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It introduces a disagreement among Hildegard’s biographers.',
         'It offers evidence for a claim made in the previous sentence.',
         'It reframes the fact stated before it, and the rest of the text explains the reframing.',
         'It restates the opening sentence in more precise language.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>It reframes the fact</strong>… Oldingi jumla '
                    'faktni beradi (hammasi 42 yoshdan keyin), bu jumla uni boshqacha '
                    'oʻqiydi ("kech gullash emas, kech ruxsat"), keyingisi esa nega '
                    'shundayligini aytadi. <strong>It offers evidence</strong>… notoʻgʻri: '
                    'dalil undan keyin keladi.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'medium',
     'passage': '<p><b>Text 1</b><br>A cork oak is stripped of its bark every nine years '
                'and lives for two centuries. The bark grows back, the tree is never '
                'felled, and the montado woodlands of Portugal have been worked this way '
                'for generations. Cork is often held up as the model of a harvest that '
                'costs the forest nothing.</p>'
                '<p><b>Text 2</b><br>Nuno Ferreira points out that the model depends on a '
                'price. Cork is stripped by hand by skilled workers, and when screw caps '
                'take a share of the wine market the montado stops paying for itself. '
                'Landowners then clear it for pasture. The threat to the woodland is not '
                'the harvest; it is the absence of one.</p>',
     'question_text': 'Based on the texts, Ferreira’s view of the cork harvest differs '
                      'from the view in Text 1 in that he',
     'choices': [
         'argues that cork oaks live for a shorter time than Text 1 claims.',
         'believes that screw caps are better suited to wine than cork stoppers are.',
         'denies that the bark of a cork oak grows back after stripping.',
         'treats the harvest as the thing that keeps the woodland standing, not as a cost it absorbs.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>treats the harvest as</strong>… 2-matn oxirgi '
                    'jumlada aynan shuni aytadi: xavf yigʻim emas, yigʻimning '
                    '<em>yoʻqligi</em>. 1-matn uchun yigʻim daraxt koʻtaradigan yuk, '
                    'Ferreira uchun esa uni saqlab turgan narsa. <strong>denies that the '
                    'bark of a cork oak grows back</strong>… 2-matn bu faktga umuman '
                    'tegmaydi.'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>The rice terraces of Banaue are usually praised as engineering, and the '
                'walls are the visible part of it. The invisible part is the water: a '
                'system of channels takes a stream from high ground and passes it down '
                'through every terrace in turn, so that the field at the bottom receives '
                'what the field above has already used. The terraces are not a set of '
                'farms. They are one farm with two thousand floors.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Rice grown on the terraces yields more than rice grown on flat ground.',
         'The terraces function as a single connected system rather than as separate fields.',
         'The terraces were built without the use of metal tools.',
         'The walls of the terraces need constant repair by the families who farm them.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>The terraces function as</strong>… Matn oxirgi '
                    'ikki jumlada fikrini ochiq aytadi: bu alohida dalalar emas, ikki ming '
                    'qavatli bitta xoʻjalik. <strong>The walls of the terraces need '
                    'constant repair</strong>… matnda umuman yoʻq — devorlar faqat '
                    '"koʻrinadigan qism" sifatida eslatiladi.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>Before the twentieth century an orchestra’s A was whatever the '
                'local organ or wind band had settled on, and it drifted upward: a brighter '
                'sound carried better in a hall, so each ensemble tuned a little above the '
                'last. By the 1850s some European orchestras stood a semitone apart, which '
                'meant that a singer could not take a part from one city to another without '
                'transposing it. The conference that fixed A at 440 hertz in 1939 was not '
                'an acoustic discovery. It was a treaty.</p>',
     'question_text': 'According to the text, what problem did fixing the pitch at 440 '
                      'hertz solve?',
     'choices': [
         'Halls built in the nineteenth century absorbed high frequencies unevenly.',
         'Organ builders disagreed about the correct temperament for keyboards.',
         'Singers could not move a part from one orchestra to another without rewriting it.',
         'Instruments built in different countries could not be played together in tune.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Singers could not move</strong>… Matn muammoni '
                    'aynan shu soʻzlar bilan beradi: "a singer could not take a part from '
                    'one city to another without transposing it". <strong>Instruments '
                    'built in different countries</strong>… mantiqan maʼqul koʻrinadi va '
                    'shuning uchun xavfli — matn cholgʻular haqida hech narsa '
                    'demaydi, faqat xonanda haqida.'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>An ecologist proposes that the collapse of the kelp forests along one '
                'stretch of coast was caused by the loss of sea otters rather than by '
                'warming water — which would mean the kelp should return where otters '
                'return, even if the temperature does not fall.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'ecologist’s proposal?',
     'choices': [
         'Kelp grows more slowly in warm water than it does in cold water.',
         'Kelp returned within five years along sections where otters were reintroduced, while nearby sections without otters stayed bare at the same temperature.',
         'Otter populations declined along the whole of the coast during the same period.',
         'Sea urchins are eaten by several predators besides otters.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Kelp returned within five</strong>… Taklif '
                    'ikki sababni ajratadi: kalan yoki harorat. Bu tajribada harorat ikki '
                    'uchastkada bir xil, faqat kalan farq qiladi — demak sabab '
                    'ajraladi. <strong>Kelp grows more slowly in warm water</strong>… '
                    'aksincha, harorat versiyasini quvvatlaydi.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A historian claims that Tharp’s exclusion from the ships shaped '
                'her map rather than merely delaying it: cut off from the act of sounding, '
                'she worked only with the numbers, and that distance is what let her see a '
                'pattern the ship crews had missed.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'historian’s claim?',
     'choices': [
         'Tharp had trained in geology and in mathematics before joining the laboratory.',
         'Tharp plotted every sounding as a profile and saw a rift valley down the centre of the ridge, which the crews taking the soundings had never reported.',
         'Tharp’s map was published under a colleague’s name as well as her own.',
         'The soundings Tharp used had been gathered over a period of several years.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Tharp plotted every sounding</strong>… Daʼvoning '
                    'ikki qismi bor: u raqamlar bilan ishlagan, <em>va</em> shu tufayli '
                    'ekipaj koʻrmagan narsani koʻrgan. Faqat shu variant ikkalasini ham '
                    'beradi. <strong>Tharp had trained in geology and in '
                    'mathematics</strong>… uning malakasini koʻrsatadi, masofaning '
                    'taʼsirini emas.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A survey recorded the share of montado woodland cleared for pasture in '
                'four Portuguese districts, together with the average price paid per '
                'kilogram of cork in each.</p>'
                '<table><tr><th>District</th><th>Cork price (€ per kg)</th>'
                '<th>Woodland cleared (%)</th></tr>'
                '<tr><td>Grândola</td><td>3.40</td><td>2</td></tr>'
                '<tr><td>Avis</td><td>2.75</td><td>6</td></tr>'
                '<tr><td>Ponte de Sor</td><td>2.10</td><td>11</td></tr>'
                '<tr><td>Nisa</td><td>1.60</td><td>19</td></tr></table>',
     'question_text': 'A student claims that, among these districts, more woodland was '
                      'cleared where cork paid less. Which choice best describes data from '
                      'the table that support this claim?',
     'choices': [
         'All four districts cleared at least some of their woodland.',
         'Clearance rose as the cork price fell, from 2% at Grândola (€3.40) to 19% at Nisa (€1.60).',
         'Nisa cleared 19% of its montado woodland.',
         'The cork price in Grândola was more than twice the price in Nisa.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Clearance rose as</strong>… Daʼvo ikki '
                    'kattalikning teskari bogʻliqligi haqida, demak dalil ham ikkalasini '
                    'butun jadval boʻylab olishi kerak. <strong>The cork price in '
                    'Grândola was more than twice</strong>… rost, lekin faqat narx '
                    'ustunida qoladi — kesilgan maydon haqida hech narsa demaydi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>Mental calculation on an imagined soroban is fast because the user is '
                'not really doing arithmetic; they are moving a picture. Experiments find '
                'that a skilled user can hold a conversation while calculating but cannot '
                'calculate while watching a moving object. The interference is therefore '
                '______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'caused by fatigue rather than by distraction.',
         'greater in children than it is in adults.',
         'the same for every form of mental arithmetic.',
         'visual rather than verbal.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>visual rather than verbal.</strong> Tajriba ikki '
                    'holatni qarshi qoʻyadi: gapirish xalaqit bermaydi, qarash beradi '
                    '— demak ziddiyat koʻrish kanalida. <strong>caused by fatigue '
                    'rather than by distraction</strong>… matnda charchoq haqida bir soʻz '
                    'ham yoʻq.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>A dandelion sets seed without being pollinated, so each seed is a copy '
                'of the parent plant. A meadow of dandelions can therefore look uniform and '
                'be uniform — which means that a fungus one plant cannot survive '
                '______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'is one its neighbours cannot survive either.',
         'is unlikely to reach the rest of the meadow.',
         'will kill only the plants that flowered earliest.',
         'will spread more slowly there than through a mixed meadow.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>is one its neighbours</strong>… Matn kalit '
                    'soʻzni beradi: har bir oʻsimlik nusxa, demak ularning zaifligi ham '
                    'bir xil. <strong>will spread more slowly there than through a mixed '
                    'meadow</strong> aynan teskari xulosa va eng koʻp tanlanadigan javob '
                    '— bir xillik kasallikni sekinlashtirmaydi, tezlashtiradi.'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>Marie Tharp, the geologist who drew the first map of the Atlantic sea '
                '______ was not permitted aboard the ships that took the soundings.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['floor', 'floor,', 'floor:', 'floor;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>floor,</strong>. "the geologist who…floor" '
                    '— <em>Marie Tharp</em> ga izoh, vergul bilan ochilgan, demak '
                    'vergul bilan yopiladi. <strong>floor;</strong> notoʻgʻri: nuqtali '
                    'vergul ikki mustaqil gapni ajratadi, bu yerda esa ega hali kesimini '
                    'kutib turibdi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>A cork oak is stripped every nine ______ however, the bark grows back '
                'and the tree itself is never felled.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['years', 'years and', 'years,', 'years;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>years;</strong>. <em>however</em> bogʻlovchi '
                    'emas, kirish soʻz: u ikki mustaqil gapni ulay olmaydi, shuning uchun '
                    'ular orasida nuqtali vergul kerak. <strong>years,</strong> — '
                    'comma splice, va bu savolning butun tuzogʻi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Because each seed is an exact copy of the ______ a meadow of dandelions '
                'can be genetically uniform.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['parent', 'parent,', 'parent:', 'parent;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>parent,</strong>. Gap "Because…" bilan '
                    'boshlangan ergash gapdan boshlanadi, va gap boshida turgan ergash gap '
                    'asosiy gapdan vergul bilan ajratiladi. <strong>parent;</strong> '
                    'notoʻgʻri: nuqtali vergul ikki <em>mustaqil</em> gap orasida turadi, '
                    '"Because…" esa mustaqil emas.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The system of channels that carries water down through the terraces '
                '______ every field in turn.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are reaching', 'have reached', 'reach', 'reaches'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>reaches</strong>. Ega — <em>system</em>, '
                    'birlik; "of channels that carries water down through the terraces" '
                    'faqat aniqlovchi. Feʼlga yaqin turgan "terraces" koʻplik boʻlgani '
                    'uchun quloq <strong>reach</strong> ga tortadi.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time the conference met in 1939, orchestras ______ their pitch '
                'upward for more than a century.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are drifting', 'had been drifting', 'has been drifting', 'will have drifted'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>had been drifting</strong>. "By the time…met" '
                    'oʻtmishdagi nuqtani beradi, jarayon esa undan oldin boshlanib oʻsha '
                    'nuqtagacha davom etgan — past perfect continuous. <strong>has '
                    'been drifting</strong> hozirgi paytga ulaydi, gap esa 1939-yilda '
                    'tugagan.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>The four ______ cork prices differed by more than a euro per '
                'kilogram.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['district’s', 'districts', 'districts’', 'districts’s'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>districts’</strong>. Tumanlar toʻrtta '
                    '("The four"), narxlar ularniki — koʻplikdagi egalik <em>-s</em> '
                    'dan keyin faqat apostrof qoʻyiladi. <strong>district’s</strong> '
                    'birlik egalik boʻlib, "four" bilan ziddiyatga kiradi.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>______ the Eiffel Tower carries the pressure of the wind straight down '
                'into its foundations.</p>',
     'question_text': CONVENTION_Q,
     'choices': [
         'Curved along a line the engineers calculated,',
         'Curving it along a line the engineers calculated,',
         'Having curved it along a line the engineers calculated,',
         'To curve along a line the engineers calculated,',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Curved along a</strong>… Boshlanuvchi ibora '
                    'egani — <em>the Eiffel Tower</em> — aniqlashi kerak, minora '
                    'esa <em>egilgan</em>: majhul maʼno, demak III shakl. '
                    '<strong>Curving it along a</strong>… aniq nisbat beradi va minoraning '
                    'oʻzi nimanidir egayotgan boʻlib chiqadi — egasiga osilib qolgan '
                    'aniqlovchi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>A skilled soroban user stops moving the beads long before the answer is '
                'needed. ______ the calculation has moved into the mind, where beads can be '
                'shifted faster than a hand could shift them.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['By then,', 'In contrast,', 'Nevertheless,', 'Previously,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>By then,</strong>. Ikki jumla orasidagi bogʻ '
                    '— <em>vaqt</em>: qoʻl toʻxtagan payt, hisob allaqachon ichkarida. '
                    '<strong>Previously,</strong> teskari yoʻnalishni bildiradi va eng '
                    'koʻp tanlanadigan xato.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Otters eat sea urchins, and sea urchins eat kelp. ______ removing the '
                'otters from a stretch of coast removes the kelp as well.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['For example,', 'However,', 'In effect,', 'Meanwhile,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>In effect,</strong>. Ikkinchi jumla birinchisida '
                    'berilgan zanjirning <em>oqibatini</em> chiqaradi. <strong>For '
                    'example,</strong> misol kutadi, lekin bu misol emas, xulosa; '
                    '<strong>Meanwhile,</strong> esa bir vaqtda sodir boʻlishni bildiradi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Cork is often held up as a harvest that costs the forest nothing. '
                '______ the woodland survives only while the harvest pays: when it stops '
                'paying, the land is cleared.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'In fact,', 'Likewise,', 'Similarly,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>In fact,</strong>. Ikkinchi jumla birinchisidagi '
                    'chiroyli tasavvurni tuzatadi — oʻrmon bepul emas, u yigʻim '
                    'hisobiga turadi. <strong>Likewise,</strong> va '
                    '<strong>Similarly,</strong> oʻxshashlik kutadi, <strong>Accordingly,'
                    '</strong> esa natija — uchalasi ham tuzatishni bildirmaydi.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Marie Tharp was not permitted aboard the research ships.</li>'
                '<li>She worked from soundings gathered by other people.</li>'
                '<li>She plotted every sounding as a profile of the sea floor.</li>'
                '<li>She identified a rift valley down the centre of the Mid-Atlantic '
                'Ridge.</li>'
                '<li>The rift valley became evidence for sea-floor spreading.</li></ul>',
     'question_text': 'The student wants to emphasize what Tharp achieved despite being '
                      'excluded. Which choice most effectively uses relevant information '
                      'from the notes to accomplish this goal?',
     'choices': [
         'Barred from the ships, Tharp worked only from other people’s soundings and found in them a rift valley down the centre of the Mid-Atlantic Ridge — evidence for sea-floor spreading.',
         'Marie Tharp was not permitted aboard the research ships that gathered the soundings.',
         'Tharp plotted every sounding she was given as a profile of the sea floor.',
         'The rift valley that Tharp identified became evidence for sea-floor spreading.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Barred from the ships,</strong>… Maqsad ikki '
                    'narsani <em>bir jumlada</em> qarshi qoʻyishni talab qiladi: toʻsiq va '
                    'yutuq. Faqat shu variant ikkalasini ham beradi. <strong>Marie Tharp '
                    'was not permitted aboard</strong>… faqat toʻsiqni aytadi, yutuqni '
                    'emas — yarim maqsad bajarilgan javob notoʻgʻri javobdir.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>The legs of the Eiffel Tower follow a calculated curve.</li>'
                '<li>The curve carries wind pressure down into the foundations.</li>'
                '<li>The structure is a lattice rather than a solid surface.</li>'
                '<li>A solid surface would catch the wind.</li>'
                '<li>The lattice lets the wind pass through it.</li></ul>',
     'question_text': 'The student wants to explain to an audience unfamiliar with the '
                      'tower why it has the shape it does. Which choice most effectively '
                      'uses relevant information from the notes to accomplish this goal?',
     'choices': [
         'A solid surface would have caught the wind.',
         'The legs of the Eiffel Tower follow a curve that its engineers calculated.',
         'The structure of the tower is a lattice rather than a solid surface.',
         'The tower’s curve carries wind pressure down into the foundations, and its lattice lets the wind through instead of catching it — both are answers to wind.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The tower’s curve carries</strong>… Maqsad '
                    'minoraning <em>shakli</em>ni tushuntirish, va shakl ikki belgidan '
                    'iborat: egrilik hamda panjara. Faqat shu variant ikkalasini ham bitta '
                    'sababga bogʻlaydi. Qolganlari bitta qaydni takrorlaydi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Before the twentieth century each ensemble set its own A.</li>'
                '<li>Pitch drifted upward because a brighter sound carried better in a '
                'hall.</li>'
                '<li>By the 1850s some orchestras stood a semitone apart.</li>'
                '<li>A singer could not move a part between cities without transposing '
                'it.</li>'
                '<li>A conference in 1939 fixed A at 440 hertz.</li></ul>',
     'question_text': 'The student wants to emphasize that the standard was an agreement '
                      'rather than a discovery. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'A conference held in 1939 fixed the note A at 440 hertz.',
         'Before the twentieth century, each ensemble set its own A.',
         'Orchestras had drifted a semitone apart, so that a singer could not move a part between cities; the 1939 conference did not discover 440 hertz, it agreed on it.',
         'Pitch drifted upward because a brighter sound carried better in a hall.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Orchestras had drifted a</strong>… Maqsad '
                    '— "kashfiyot emas, kelishuv" ekanini koʻrsatish, demak javob '
                    'hal qilinayotgan <em>muammoni</em> aytishi va farqni ochiq qoʻyishi '
                    'kerak. <strong>A conference held in 1939 fixed the note A</strong>… '
                    'faqat voqeani aytadi — undan kashfiyot boʻlmaganini oʻqib '
                    'boʻlmaydi.'},
]
