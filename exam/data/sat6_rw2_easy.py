# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 6 · Reading and Writing, Module 2 (LOWER)
#  27 questions · 32 minutes · taken by a pupil who scored under 18 on rw1.
#
#  Same domains, same counts, same order as the upper module — one-step
#  reasoning, familiar wording, the point in the opening sentence.
#
#  Load: python manage.py load_mock exam/data/sat6_rw2_easy.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §3
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
     'passage': '<p>Sequoyah could not read English, or any other language, when he set out '
                'to write down Cherokee. He had seen that marks on paper carried messages, '
                'and that was all he had to go on. Working alone for twelve years, he '
                '______ a syllabary of eighty-six characters.</p>',
     'question_text': WORD_Q,
     'choices': ['borrowed', 'devised', 'memorised', 'translated'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>devised</strong> — oʻylab topdi. Birinchi '
                    'jumla shartni qoʻyadi: u hech qanday yozuvni oʻqiy olmasdi, demak '
                    'tayyor tizimni olishi mumkin emas edi. <strong>borrowed</strong> aynan '
                    'shu sababga zid.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>Some coffee and citrus flowers put caffeine into their nectar, at doses '
                'far too low for a bee to taste. Bees that drink it come back to the same '
                'flowers more often and remember where they are for longer. The plant is '
                'not feeding the bee; it is ______ it.</p>',
     'question_text': WORD_Q,
     'choices': ['poisoning', 'repelling', 'training', 'watering'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>training</strong>. Nuqtali vergul '
                    'qarama-qarshilik qoʻyadi, oldingi jumla esa natijani aytadi: ari '
                    'qaytadi va eslab qoladi — bu oʻrgatishning taʼrifi. '
                    '<strong>repelling</strong> matnga zid: ari uzoqlashmaydi, qaytadi.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>Whitcomb Judson’s clasp locker of 1893 was shown at the Chicago '
                'World’s Fair and sold badly: it jammed, it came apart, and nobody '
                'trusted it on clothing. The ______ for the jamming came from Gideon '
                'Sundback, who gave every tooth a scoop and a nib so that each one locked '
                'into the tooth opposite.</p>',
     'question_text': WORD_Q,
     'choices': ['complaint', 'motive', 'remedy', 'warning'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>remedy</strong> — chora, yechim. Ikki '
                    'nuqtadan keyingi roʻyxat muammoni beradi, vergul ortidagi qism esa '
                    'Sundback nima qilganini aytadi: tishlarni bir-biriga qulflagan. '
                    '<strong>complaint</strong> muammoni takrorlaydi, uni yechmaydi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>A map is useless without its <u>key</u>: the small panel that says what '
                'a dashed line means, what blue stands for, how many kilometres an inch '
                'covers. Everything else on the sheet is a claim; the key is the agreement '
                'that lets you read it.</p>',
     'question_text': 'As used in the text, what does the word <u>key</u> most nearly '
                      'mean?',
     'choices': ['answer', 'explanation', 'lock', 'tone'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>explanation</strong>. Ikki nuqtadan keyingi '
                    'qism taʼrifni beradi: nima nimani anglatishini aytadigan kichik '
                    'panel. <strong>lock</strong> va <strong>tone</strong> "key" soʻzining '
                    'boshqa maʼnolari — qulf va musiqa — va aynan shuning uchun '
                    'tuzoq.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'easy',
     'passage': '<p>Franklin’s lightning rod is usually described as attracting '
                'lightning, which is nearly the opposite of what it does. A grounded metal '
                'point bleeds charge off a building continuously, so that the difference '
                'between the roof and the cloud stays small. When a strike does come, the '
                'rod gives it a path to earth that does not run through the building. The '
                'rod’s first job is to make a strike less likely; its second is to '
                'survive one.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that lightning rods are no longer necessary on modern buildings',
         'To compare Franklin’s design with the improvements made to it later',
         'To correct a common description of the rod by setting out what it actually does',
         'To describe the experiments by which Franklin established the nature of lightning',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>To correct a common</strong>… Matn birinchi '
                    'jumladayoq keng tarqalgan taʼrifni "deyarli teskari" deb rad etadi va '
                    'qolgan qismda haqiqiy vazifani ikki bosqichda bayon qiladi. '
                    '<strong>To describe the experiments</strong>… tajribalar haqida matnda '
                    'bir soʻz ham yoʻq.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>Elephants make sounds below the range of human hearing, and those '
                'sounds travel through the ground as well as through the air. <u>The feet '
                'are part of the ear.</u> Vibration passes up the leg bones to the middle '
                'ear, and a herd can pick up a call — or the footfall of another herd '
                '— from several kilometres away, long before anything is '
                'audible.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It concedes a limitation in what elephants are able to hear.',
         'It gives an example of a sound that elephants make.',
         'It restates the first sentence using anatomical terms.',
         'It states the claim about elephant anatomy that the rest of the text explains.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>It states the claim</strong>… Jumla gʻalati va '
                    'qisqa daʼvo qoʻyadi, keyingi jumla esa uni anatomiya orqali '
                    'asoslaydi: tebranish oyoq suyaklaridan oʻrta quloqqa oʻtadi. '
                    '<strong>It restates the first sentence</strong>… notoʻgʻri: birinchi '
                    'jumla tovush haqida, bu jumla esa tana haqida.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'medium',
     'passage': '<p><b>Text 1</b><br>Where a charge or a ban on single-use plastic bags has '
                'been introduced, the number handed out falls by eighty or ninety per cent '
                'within a year. Shoppers bring their own instead. The policy is among the '
                'cheapest and most reliable interventions in environmental '
                'regulation.</p>'
                '<p><b>Text 2</b><br>Hana Petrić does not dispute the fall. She notes '
                'what replaces the bags: thicker reusable ones, which take far more '
                'material to make and are often used only a handful of times. Counting bags '
                'is easy and counting material is not, so the measure that gets reported is '
                'the one that flatters the policy.</p>',
     'question_text': 'Based on the texts, Petrić’s reservation about the policy '
                      'is that',
     'choices': [
         'bans are more expensive to enforce than Text 1 suggests.',
         'reusable bags are no more durable than single-use ones.',
         'shoppers do not in fact bring their own bags after a ban.',
         'the quantity that is easiest to measure may not be the quantity that matters.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>the quantity that is</strong>… Petrić '
                    'birinchi jumladayoq pasayishni tan oladi va oxirgi jumlada eʼtirozni '
                    'aniq aytadi: sanash oson boʻlgan narsa hisobga olinadi, muhimi esa '
                    'emas. <strong>shoppers do not in fact bring their own bags</strong>… '
                    'matnga zid.'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>The metre was defined in 1793 as one ten-millionth of the distance from '
                'the North Pole to the equator along the meridian through Paris — a '
                'quantity nobody could measure exactly and everybody could agree was not '
                'French property. The definition has been changed three times since, and is '
                'now fixed by the speed of light. What has not changed is the reason: a '
                'unit that belongs to no one is the only kind everyone will use.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'France was the first country to adopt a decimal system of measurement.',
         'The metre has been defined in terms of nature so that no country owns it.',
         'The original definition of the metre was inaccurate by modern standards.',
         'The speed of light is easier to measure than the meridian is.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>The metre has been</strong>… Matn oxirgi '
                    'jumlada sababni ochiq aytadi: hech kimga tegishli boʻlmagan birlikni '
                    'hamma ishlatadi. <strong>The original definition of the metre was '
                    'inaccurate</strong>… matn aniqlik haqida emas, <em>egalik</em> haqida '
                    'gapiradi.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>For two centuries the sound of a Stradivarius was credited to its '
                'varnish, and chemists took instruments apart to find out what was in it. '
                'The answer, when it came, was oil, resin and pigment — the ordinary '
                'furniture varnish of eighteenth-century Cremona. The question has since '
                'moved to the wood, the arching and the graduation of the plates, which is '
                'where the luthiers had been pointing all along.</p>',
     'question_text': 'According to the text, what did the analysis of the varnish '
                      'establish?',
     'choices': [
         'That the varnish contained a pigment unavailable elsewhere in Europe.',
         'That the varnish had been applied more thinly than on other instruments.',
         'That the varnish had decayed and been replaced on most surviving instruments.',
         'That the varnish was an ordinary material of its own time and place.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>That the varnish was</strong>… Matn javobni '
                    'tiredan keyin beradi: Kremonaning oddiy mebel laki. <strong>That the '
                    'varnish contained a pigment unavailable elsewhere</strong>… aynan '
                    'teskari: pigment bor, lekin u hech qanday sir emas.'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A researcher proposes that the caffeine in some nectars works on a '
                'bee’s memory rather than on its sense of taste — which would '
                'mean bees should return more often to a caffeinated flower even when they '
                'cannot tell it apart from an uncaffeinated one.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'researcher’s proposal?',
     'choices': [
         'Bees prefer nectar that has a higher concentration of sugar.',
         'Caffeine is toxic to bees at concentrations a hundred times higher than those found in nectar.',
         'Caffeine occurs in the nectar of several unrelated plant families.',
         'In tests where the two nectars are made identical in scent and sugar, bees still return more often to the caffeinated feeder.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>In tests where the</strong>… Taklifning sinovi '
                    'matnda aytilgan: ari ikki gulni <em>ajrata olmasa ham</em> koʻproq '
                    'qaytishi kerak. Hid va shakarni tenglashtirish aynan shu holatni '
                    'yaratadi. <strong>Caffeine occurs in the nectar of several unrelated '
                    'plant families</strong>… tarqalishini koʻrsatadi, mexanizmni emas.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A historian claims that Sequoyah’s syllabary was invented '
                'independently rather than adapted from English writing — that the '
                'resemblance of some of its characters to Latin letters is a resemblance of '
                'shape only.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'historian’s claim?',
     'choices': [
         'Characters that look like Latin letters carry sounds unrelated to the ones those letters stand for in English.',
         'Sequoyah had seen printed English documents before he began work.',
         'The syllabary has eighty-six characters, far more than the Latin alphabet.',
         'The syllabary was first printed on a press imported from the eastern states.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Characters that look like</strong>… Daʼvo '
                    'oʻxshashlik faqat <em>shaklda</em> deydi, demak dalil tovushlarning '
                    'bogʻliq emasligini koʻrsatishi kerak: shakl koʻchirilgan boʻlsa ham, '
                    'tizim koʻchirilmagan. <strong>Sequoyah had seen printed English '
                    'documents</strong>… aksincha, moslashtirish versiyasiga yordam '
                    'beradi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>Four cities introduced a charge on single-use bags. The table shows the '
                'fall in single-use bags handed out and the rise in thicker reusable bags '
                'sold in the year that followed.</p>'
                '<table><tr><th>City</th><th>Fall in single-use bags (millions)</th>'
                '<th>Rise in reusable bags sold (millions)</th></tr>'
                '<tr><td>A</td><td>210</td><td>34</td></tr>'
                '<tr><td>B</td><td>160</td><td>29</td></tr>'
                '<tr><td>C</td><td>95</td><td>18</td></tr>'
                '<tr><td>D</td><td>60</td><td>11</td></tr></table>',
     'question_text': 'A student claims that every city saw a large fall in single-use bags '
                      'and a much smaller rise in reusable ones. Which choice best '
                      'describes data from the table that support this claim?',
     'choices': [
         'All four cities introduced their charge in the same year.',
         'City A’s fall in single-use bags was the largest of the four.',
         'City D sold 11 million more reusable bags than before.',
         'In every city the fall in single-use bags was more than five times the rise in reusable bags.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>In every city the</strong>… Daʼvo ikki '
                    'kattalikni <em>taqqoslaydi</em> ("katta pasayish, ancha kichik '
                    'oʻsish"), demak dalil ham ularning nisbatini olishi va toʻrttala '
                    'shaharni qamrashi kerak. <strong>City A’s fall in single-use bags '
                    'was the largest</strong>… bitta ustunda qoladi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>A rod that is bleeding charge away from a building all day is doing its '
                'main work in weather that nobody notices. The strike it survives is the '
                'rare event; the strikes it prevented cannot be counted at all. Judging a '
                'lightning rod by the strikes it has taken is therefore ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'a way of measuring its failures rather than its successes.',
         'impossible without records going back many years.',
         'less accurate than measuring the height of the building.',
         'the only measure available to an insurer.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>a way of measuring</strong>… Matn ikki holatni '
                    'ajratadi: oldini olingan zarbalar sanalmaydi, tushgan zarba esa '
                    'asosiy ish bajarilmagan holat. Demak zarbalarni sanash — '
                    'muvaffaqiyatni emas, aksini oʻlchash. <strong>the only measure '
                    'available to an insurer</strong>… matn sugʻurta haqida hech narsa '
                    'demaydi.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>A unit tied to a metal bar in a vault in Paris is only as stable as the '
                'bar: it can be scratched, it expands in heat, and a country that wants to '
                'check its own copy has to send it to France. A unit defined by the speed '
                'of light can be rebuilt in any laboratory that can measure time. The change '
                'of definition therefore made the metre ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'easier to measure in everyday use.',
         'independent of any single object or place.',
         'shorter than it had previously been.',
         'useful for the first time outside Europe.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>independent of any</strong>… Matn eski '
                    'taʼrifning ikki kamchiligini sanaydi — buyum va joy — va '
                    'yangi taʼrif ikkalasini ham yoʻq qiladi. <strong>shorter than it had '
                    'previously been</strong> notoʻgʻri: taʼrif oʻzgardi, uzunlik emas.'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>Sequoyah, the silversmith who worked out a way of writing ______ could '
                'not read a word of English.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['Cherokee', 'Cherokee,', 'Cherokee:', 'Cherokee;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Cherokee,</strong>. "the silversmith who…'
                    'Cherokee" — <em>Sequoyah</em> ga izoh, vergul bilan ochilgan, '
                    'demak vergul bilan yopiladi. <strong>Cherokee;</strong> notoʻgʻri: '
                    'nuqtali vergul ikki mustaqil gapni ajratadi, bu yerda esa ega hali '
                    'kesimini kutyapti.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>A grounded rod bleeds charge off a building all ______ the difference '
                'between the roof and the cloud therefore stays small.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['day', 'day and,', 'day,', 'day;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>day;</strong>. Boʻshliqning ikki tomonida ham '
                    'toʻliq mustaqil gap turibdi, ularni nuqtali vergul ajratadi. '
                    '<strong>day,</strong> — comma splice, ingliz tilidagi eng keng '
                    'tarqalgan punktuatsiya xatosi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Because the caffeine in nectar is far below the concentration a bee can '
                '______ the effect cannot be a matter of taste at all.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['taste', 'taste,', 'taste:', 'taste;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>taste,</strong>. Gap "Because…" bilan '
                    'boshlangan ergash gapdan boshlanadi, va gap boshida turgan ergash gap '
                    'asosiy gapdan vergul bilan ajratiladi. <strong>taste;</strong> '
                    'notoʻgʻri: nuqtali vergul ikki <em>mustaqil</em> gap orasida turadi.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The set of eighty-six characters that Sequoyah worked out ______ every '
                'syllable in the language.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are covering', 'cover', 'covers', 'have covered'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>covers</strong>. Ega — <em>set</em>, '
                    'birlik; "of eighty-six characters that Sequoyah worked out" faqat '
                    'aniqlovchi. Feʼlga yaqin turgan "characters" koʻplik boʻlgani uchun '
                    'quloq <strong>cover</strong> ga tortadi.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time the syllabary was adopted in 1825, Sequoyah ______ on it '
                'for twelve years.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['had been working', 'has been working', 'will have worked', 'works'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>had been working</strong>. "By the time…was '
                    'adopted" oʻtmishdagi nuqtani beradi, ish esa undan oldin boshlanib '
                    'oʻsha nuqtagacha davom etgan — past perfect continuous. '
                    '<strong>has been working</strong> hozirgi paytga ulaydi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>The four ______ charges all came into force within the same '
                'twelve months.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['cities', 'cities’', 'cities’s', 'city’s'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>cities’</strong>. Shaharlar toʻrtta ("The '
                    'four"), yigʻimlar ularniki — koʻplikdagi egalik <em>-s</em> dan '
                    'keyin faqat apostrof qoʻyiladi. <strong>city’s</strong> birlik '
                    'egalik boʻlib, "four" bilan ziddiyatga kiradi.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>A lightning rod protects a building by bleeding charge away, by keeping '
                'the difference in potential small, and by ______</p>',
     'question_text': CONVENTION_Q,
     'choices': ['a path to earth.', 'it offers a path to earth.',
                 'offering a path to earth.', 'offers a path to earth.'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>offering a path to earth.</strong> Qator '
                    '"by bleeding…by keeping…and by ___" — har bir aʼzo <em>by</em> + '
                    '<em>-ing</em> shaklida, demak uchinchisi ham shunday boʻlishi shart. '
                    '<strong>it offers a path to earth.</strong> butun boshli gap qoʻshadi '
                    'va qatorning shaklini sindiradi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>The caffeine in nectar is far too dilute for a bee to taste. ______ '
                'bees that drink it remember the flower’s position for longer than '
                'bees that do not.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'For example,', 'Likewise,', 'Nonetheless,'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Nonetheless,</strong>. Sezilmaydigan modda '
                    'baribir taʼsir qiladi — kutilmagan burilish. '
                    '<strong>Accordingly,</strong> aynan teskari bogʻlanish: u "sezilmagani '
                    'uchun yaxshi eslab qoladi" degan maʼnoni beradi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Chemists found nothing unusual in the varnish of a Stradivarius. ______ '
                'the question moved on to the wood and the arching of the plates.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'By contrast,', 'For instance,', 'Nevertheless,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Accordingly,</strong>. Bir yoʻl yopilgani '
                    '— sabab, izlanishning boshqa tomonga burilishi — natija. '
                    '<strong>Nevertheless,</strong> ziddiyat talab qiladi, bu yerda esa '
                    'ikkinchi jumla birinchisidan kelib chiqadi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Counting the bags handed out in a city is straightforward. ______ '
                'counting the material those bags are made of is not, and it is the '
                'material that ends up mattering.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'For example,', 'However,', 'Likewise,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>However,</strong>. Bir narsa oson, ikkinchisi '
                    'qiyin — qarama-qarshilik. <strong>Likewise,</strong> oʻxshashlik '
                    'kutadi va eng koʻp tanlanadigan xato: ikkala jumla ham sanash haqida, '
                    'lekin mavzuning bir xilligi munosabatning bir xilligi emas.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Sequoyah could not read English or any other language.</li>'
                '<li>He worked on the syllabary alone for twelve years.</li>'
                '<li>The finished syllabary has eighty-six characters.</li>'
                '<li>The Cherokee Nation adopted it in 1825.</li>'
                '<li>Within a few years Cherokee literacy was higher than that of the '
                'settlers nearby.</li></ul>',
     'question_text': 'The student wants to emphasize what makes the achievement unusual. '
                      'Which choice most effectively uses relevant information from the '
                      'notes to accomplish this goal?',
     'choices': [
         'Sequoyah worked on the syllabary alone for twelve years.',
         'The Cherokee Nation adopted the syllabary in 1825.',
         'The finished syllabary has eighty-six characters.',
         'Unable to read any language himself, Sequoyah worked out a system of eighty-six characters — and within a few years of its adoption Cherokee literacy was higher than that of the settlers nearby.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Unable to read any</strong>… Gʻayrioddiylikni '
                    'koʻrsatish uchun ikki tomon kerak: qanday sharoitda boshlangani va '
                    'nimaga olib kelgani. Faqat shu variant ikkalasini birga beradi. '
                    '<strong>Sequoyah worked on the syllabary alone for twelve '
                    'years</strong>… mehnatni aytadi, lekin natijasini emas.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>A lightning rod is a grounded metal point fixed to a building.</li>'
                '<li>It bleeds electric charge off the building continuously.</li>'
                '<li>This keeps the difference between building and cloud small.</li>'
                '<li>A strike that does come is carried to earth along the rod.</li>'
                '<li>That path does not run through the roof.</li></ul>',
     'question_text': 'The student wants to explain what the rod does to an audience '
                      'unfamiliar with it. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'A lightning rod is a grounded metal point fixed to a building.',
         'A strike that does come is carried to earth along the rod.',
         'The path a strike takes does not run through the roof.',
         'The rod bleeds charge off the building all the time, keeping the difference between roof and cloud small — and if a strike does come, it travels to earth along the rod instead of through the roof.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The rod bleeds charge</strong>… Maqsad '
                    'tayoqning ishini tushuntirish, ish esa ikki qismdan iborat: har kuni '
                    'oldini olish va kamdan-kam hollarda yoʻl berish. Faqat shu variant '
                    'ikkalasini ham beradi. <strong>A strike that does come is carried to '
                    'earth along the rod</strong>… faqat ikkinchi yarmini.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>The metre was defined in 1793 as one ten-millionth of the pole-to-'
                'equator distance.</li>'
                '<li>The definition has been changed three times since.</li>'
                '<li>It is now fixed by the speed of light.</li>'
                '<li>Each definition was chosen so that no country owns the unit.</li>'
                '<li>A unit defined by nature can be rebuilt in any laboratory.</li></ul>',
     'question_text': 'The student wants to emphasize why the definition keeps changing. '
                      'Which choice most effectively uses relevant information from the '
                      'notes to accomplish this goal?',
     'choices': [
         'Each definition has been chosen so the unit belongs to no country and can be rebuilt in any laboratory — which is why the metre has been redefined three times without ever changing length.',
         'The definition of the metre has been changed three times since 1793.',
         'The metre is now defined by the speed of light.',
         'The metre was defined in 1793 as one ten-millionth of the distance from the pole to the equator.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Each definition has been</strong>… Maqsad '
                    '<em>nega</em> oʻzgarishini tushuntirish, demak javob har safar '
                    'saqlanadigan tamoyilni nomlashi kerak. <strong>The definition of the '
                    'metre has been changed three times since 1793</strong>… faqat faktni '
                    'aytadi — undan sabab koʻrinmaydi.'},
]
