# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 6 · Reading and Writing, Module 1
#  27 questions · 32 minutes · every taker sits this one.
#
#  Route: 18 or more correct here sends the taker to the UPPER module 2.
#
#  Load: python manage.py load_mock exam/data/sat6_rw1.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md
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

S = 'rw1'

WORD_Q = ('Which choice completes the text with the most logical and precise '
          'word or phrase?')
TRANSITION_Q = ('Which choice completes the text with the most logical '
                'transition?')
CONVENTION_Q = ('Which choice completes the text so that it conforms to the '
                'conventions of Standard English?')

QUESTIONS = [

    # ── Craft and Structure: Words in Context (1–4) ────────────────────
    {'section': S, 'number': 1, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>Jeanne Baret sailed round the world on Bougainville’s expedition '
                'of 1766 as Jean Baret, valet to the ship’s botanist. She collected '
                'and pressed most of the six thousand specimens the voyage brought home. '
                'The botanist’s name is on all of them; hers is on ______.</p>',
     'question_text': WORD_Q,
     'choices': ['all', 'most', 'none', 'some'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>none</strong>. Nuqtali vergul ikki holatni '
                    'qarshi qoʻyadi: botanikning nomi <em>hammasida</em>, demak '
                    'Baretniki — hech birida. <strong>some</strong> ziddiyatni '
                    'yumshatadi va gapning butun maʼnosini yoʻqotadi.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>Some cicada broods spend thirteen years underground and some seventeen, '
                'and both numbers are prime. A predator with a two-, three- or four-year '
                'population cycle cannot ______ either brood: no short cycle divides '
                'thirteen or seventeen, so the predator’s peak and the emergence '
                'almost never line up.</p>',
     'question_text': WORD_Q,
     'choices': ['digest', 'outnumber', 'tolerate', 'track'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>track</strong> — izidan yurmoq, ritmiga '
                    'moslashmoq. Ikki nuqtadan keyingi qism maʼnoni beradi: davrlar bir-'
                    'biriga toʻgʻri kelmaydi. <strong>outnumber</strong> son haqida, matn '
                    'esa <em>vaqt</em> haqida.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>The Domesday survey of 1086 recorded who held what land across most of '
                'England, and what each holding was worth. It was not a census of people. '
                'It was an ______ of assets, compiled so that a new king could learn what '
                'he had conquered and what it could be made to yield.</p>',
     'question_text': WORD_Q,
     'choices': ['apology', 'imitation', 'inventory', 'objection'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>inventory</strong> — roʻyxat, hisob. '
                    'Birinchi jumla nima yozilganini aytadi (yer, egasi, qiymati), '
                    'ikkinchisi esa "aholi roʻyxati emas" deb yoʻnaltiradi: bu mulk '
                    'roʻyxati. <strong>imitation</strong> matnda umuman asossiz.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>Any measurement carries a component that is not the thing being '
                'measured: the instrument drifts, the air moves, the observer blinks. '
                'Statisticians call this <u>noise</u>, and the word is exact — it is '
                'not error in the sense of a mistake, but variation with no pattern in it '
                'and no single cause worth naming.</p>',
     'question_text': 'As used in the text, what does the word <u>noise</u> most nearly '
                      'mean?',
     'choices': ['bias', 'interference', 'randomness', 'sound'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>randomness</strong>. Taʼrif tiredan keyin '
                    'berilgan: naqshi ham, nomlashga arziydigan sababi ham yoʻq '
                    'oʻzgaruvchanlik. <strong>bias</strong> tizimli ogʻish — aynan '
                    'naqshi <em>bor</em> narsa, demak u toʻgʻri kelmaydi; '
                    '<strong>sound</strong> esa soʻzning kundalik maʼnosi.'},

    # ── Craft and Structure: Text Structure and Purpose (5–6) ──────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>When Joseph Bazalgette designed London’s sewers in the 1860s he '
                'calculated the volume the city then produced, allowed the most generous '
                'figure per head he could justify — and then doubled the diameter of '
                'every pipe. Asked why, he said that they were only going to do this once. '
                'The system he built was sized for a city of three million. It is still '
                'draining one of nine.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that Victorian engineering was more durable than modern engineering is',
         'To compare London’s sewers with those of other European capitals',
         'To describe the health crisis that prompted the building of the sewers',
         'To explain a design decision by showing what it made possible a century later',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To explain a design</strong>… Matn qarorni '
                    'aytadi (diametrni ikkilantirish), sababini keltiradi ("only going to '
                    'do this once") va natijasini koʻrsatadi (uch million uchun qurilgan '
                    'tizim toʻqqiz millionga xizmat qilyapti). <strong>To argue that '
                    'Victorian engineering was more durable</strong>… matn zamonaviy '
                    'muhandislik bilan taqqoslamaydi.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>Before 1830 a plant sent by sea usually died: months of salt spray, no '
                'fresh water to spare, and a crew with better things to do. <u>Nathaniel '
                'Ward’s contribution was a box.</u> Sealed glass standing over a tray '
                'of soil recycles its own moisture and needs no attention at all, and it '
                'turned a voyage that killed nineteen plants in twenty into one that killed '
                'one.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It concedes that Ward’s design was simpler than his contemporaries had expected.',
         'It gives an example of a plant that survived the voyage.',
         'It names the solution whose workings and effect the rest of the text sets out.',
         'It restates the difficulty described in the first sentence.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>It names the solution</strong>… Jumla '
                    'muammodan yechimga oʻtadi va uni bitta soʻz bilan ataydi; keyingi '
                    'jumla esa quti qanday ishlashini va nimaga olib kelganini aytadi. '
                    '<strong>It restates the difficulty</strong>… notoʻgʻri: qiyinchilik '
                    'ortda qoldi, jumla yangi narsani kiritadi.'},

    # ── Craft and Structure: Cross-Text Connections (7) ────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>If office workers come in two days a week instead of '
                'five, the lunch trade, the dry cleaners and the bus routes that served '
                'them lose three-fifths of their custom. Several city centres have reported '
                'exactly that. The conclusion drawn is that remote work hollows out the '
                'city.</p>'
                '<p><b>Text 2</b><br>Farida Nasr points out that the workers did not '
                'evaporate. They are having lunch somewhere — in the neighbourhoods '
                'they live in, which mostly had no lunch trade to speak of. What the data '
                'record is not a loss of activity but a move of it, and whether that counts '
                'as a hollowing-out depends on where you draw the boundary.</p>',
     'question_text': 'Based on the texts, Nasr’s response to the conclusion in Text 1 '
                      'is to argue that it',
     'choices': [
         'applies only to cities whose centres were already in decline.',
         'depends on treating the city centre rather than the wider city as the unit of account.',
         'ignores the possibility that office attendance will return to its former level.',
         'relies on figures that overstate the fall in city-centre custom.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>depends on treating the</strong>… Nasr '
                    'raqamlarni qabul qiladi va oxirgi jumlada aynan shuni aytadi: xulosa '
                    'chegarani qayerga chizishingizga bogʻliq. <strong>relies on figures '
                    'that overstate the fall</strong>… matnga zid — u raqamni '
                    'tortishmaydi, uning talqinini tortishadi.'},

    # ── Information and Ideas: Central Ideas and Details (8–9) ─────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>Hilma af Klint painted her first abstract canvases in 1906, four years '
                'before Kandinsky, and left instructions that the work was not to be shown '
                'until twenty years after her death. The usual reading is modesty, or '
                'mysticism. Her notebooks suggest something colder: she thought the '
                'paintings were unreadable by an audience that had never seen anything like '
                'them, and she was buying time for such an audience to exist.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Abstraction was arrived at independently by several artists in the early 1900s.',
         'Af Klint withheld her work as a judgement about when it could be understood, not out of modesty.',
         'Af Klint’s abstract paintings were technically more accomplished than Kandinsky’s.',
         'Af Klint’s notebooks have only recently been translated out of Swedish.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Af Klint withheld her</strong>… Matn ikki nuqta '
                    'bilan odatdagi talqinni (kamtarlik, mistika) daftarlardagi '
                    'dalilga qarshi qoʻyadi: u tomoshabin paydo boʻlishini kutgan. '
                    '<strong>Abstraction was arrived at independently</strong>… matnda '
                    'Kandinskiy eslatiladi, lekin bu qiyoslash asosiy fikr emas.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>The cave at Dunhuang had been sealed around the year 1000 and was '
                'opened in 1900 by a monk clearing sand. Inside were some fifty thousand '
                'manuscripts in seventeen languages, among them the oldest dated printed '
                'book in the world. Why the cave was sealed is unknown: the manuscripts are '
                'not treasure, and a great many are worn copies and scraps. The best guess '
                'is that they were sealed <i>because</i> they were worn — sacred '
                'writing that could not simply be thrown away.</p>',
     'question_text': 'According to the text, what is the best available explanation for '
                      'the sealing of the cave?',
     'choices': [
         'The cave was sealed in order to protect the oldest printed book in the world.',
         'The manuscripts were hidden from an approaching army.',
         'The monks who had used the cave were abandoning the site.',
         'The writings were too damaged to use but could not be discarded.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The writings were too</strong>… Matn oxirgi '
                    'jumlada taxminni oʻzi aytadi va sababini kursiv bilan taʼkidlaydi: '
                    'eskirgani <em>uchun</em>. <strong>The cave was sealed in order to '
                    'protect the oldest printed book</strong>… kitob matnda bor, lekin '
                    'sabab sifatida emas — bu oʻqilmagan bogʻlanish.'},

    # ── Information and Ideas: Command of Evidence (10–12) ─────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A biologist proposes that the thirteen- and seventeen-year cicada '
                'cycles are prime because a prime cycle is hard for a shorter-cycled '
                'predator to synchronise with — which would mean that broods on '
                'non-prime cycles ought to be preyed upon more heavily where they '
                'occur.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'biologist’s proposal?',
     'choices': [
         'Birds that feed on cicadas breed more successfully in emergence years.',
         'Cicada broods emerge within a few days of one another across a wide area.',
         'Cicadas spend their underground years feeding on the xylem of tree roots.',
         'Populations that have shifted to a twelve-year cycle suffer predation several times heavier than neighbouring thirteen-year broods.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Populations that have shifted</strong>… Taklif '
                    'oʻz sinovini matnda aytib qoʻygan: tub boʻlmagan davrdagi toʻda '
                    'koʻproq yeyilishi kerak. Oʻn ikki va oʻn uch yillik toʻdalarni '
                    'yonma-yon taqqoslash aynan shuni beradi. <strong>Birds that feed on '
                    'cicadas breed more successfully</strong>… yirtqichga foydani '
                    'koʻrsatadi, davr uzunligining taʼsirini emas.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A curator argues that af Klint’s twenty-year instruction was '
                'strategic rather than superstitious — that she was making a judgement '
                'about audiences rather than obeying an instruction she believed she had '
                'received from elsewhere.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'curator’s argument?',
     'choices': [
         'Her early abstract canvases were painted on the same linen as her botanical studies.',
         'Her notebooks weigh up which future exhibitions might be ready for the work and rule out the ones available in her lifetime.',
         'Her will left the paintings to her nephew rather than to a museum.',
         'She belonged to a group that held séances and wrote down the results.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Her notebooks weigh up</strong>… Argument '
                    'qarorning <em>hisob-kitobli</em> ekanini aytadi, va daftarlarda '
                    'variantlarni tortish aynan hisob-kitobning izi. <strong>She belonged '
                    'to a group that held séances</strong>… aksincha ishlaydi — u '
                    'rad etilayotgan "mistik koʻrsatma" talqinini quvvatlaydi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A shipping company recorded how many of the plants it carried from Asia '
                'to London survived the voyage, before and after it began using Wardian '
                'cases.</p>'
                '<table><tr><th>Voyage</th><th>Year</th><th>Cases used</th>'
                '<th>Plants shipped</th><th>Alive on arrival</th></tr>'
                '<tr><td>1</td><td>1827</td><td>No</td><td>200</td><td>11</td></tr>'
                '<tr><td>2</td><td>1831</td><td>No</td><td>180</td><td>8</td></tr>'
                '<tr><td>3</td><td>1836</td><td>Yes</td><td>190</td><td>167</td></tr>'
                '<tr><td>4</td><td>1841</td><td>Yes</td><td>210</td><td>191</td></tr></table>',
     'question_text': 'A student concludes that the cases transformed the survival rate. '
                      'Which choice best describes data from the table that support this '
                      'conclusion?',
     'choices': [
         'All four voyages carried between 180 and 210 plants.',
         'Survival rose from under 6% on the two voyages without cases to over 87% on the two with them.',
         'Voyage 2 had the fewest plants alive on arrival.',
         'Voyage 4 carried 210 plants, more than any other voyage.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Survival rose from</strong>… Xulosa '
                    '<em>ulush</em> haqida, demak dalil tirik qolganlar sonini '
                    'joʻnatilganlar soniga nisbatan olishi va ikki guruhni qarshi qoʻyishi '
                    'kerak. <strong>Voyage 2 had the fewest plants alive on arrival</strong> '
                    'rost, lekin yalangʻoch son: 2-reysda oʻsimlik ham eng kam '
                    'joʻnatilgan.'},

    # ── Information and Ideas: Inferences (13–14) ──────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>Bazalgette sized the pipes for a city of three million and then doubled '
                'them, which is why a city of nine million still drains. But the doubling '
                'was a single decision taken once, at the start; there is no second '
                'doubling available to a successor, because the tunnels are lined, buried '
                'and built over. A Victorian margin can therefore be spent ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'more cheaply than a modern one could be.',
         'on any purpose the city later chooses.',
         'once, and not replaced.',
         'only as quickly as the population grows.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>once, and not replaced.</strong> Matn sababni '
                    'oʻzi beradi: tunnellar qoplangan, koʻmilgan va ustiga qurilgan — '
                    'demak zaxirani qayta yaratib boʻlmaydi. <strong>only as quickly as the '
                    'population grows</strong> tuzoq: u sarflash <em>tezligi</em> haqida, '
                    'matn esa uning <em>bir martaligi</em> haqida.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>Fifty thousand manuscripts in seventeen languages, sealed together in '
                'one small room, is not what a library looks like. It is what a disposal '
                'looks like — the accumulated unusable writing of a place where '
                'writing was holy. That reading explains something a library would not: '
                'the cave contains ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'documents in languages nobody at Dunhuang could read.',
         'many duplicates, scraps and worn copies rather than a selected collection.',
         'more Buddhist texts than texts of any other kind.',
         'the oldest dated printed book anywhere in the world.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>many duplicates, scraps</strong>… Kutubxona '
                    '<em>tanlangan</em> toʻplamdir; tashlab boʻlmaydigan narsalar ombori '
                    'esa yirtiq va takroriy nusxalarga toʻladi. Faqat shu variant '
                    'kutubxona izohlay olmaydigan, "disposal" izohlaydigan narsani '
                    'nomlaydi. <strong>the oldest dated printed book</strong>… har ikkala '
                    'talqin uchun ham bir xil darajada kutilmagan — u tanlovni '
                    'ajratmaydi.'},

    # ── Standard English Conventions: Boundaries (15–17) ───────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>Jeanne Baret, the first woman known to have sailed round the ______ did '
                'it dressed as a man and listed as a valet.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['world', 'world,', 'world:', 'world;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>world,</strong>. "the first woman known…world" '
                    '— <em>Jeanne Baret</em> ga izoh, vergul bilan ochilgan, demak '
                    'vergul bilan yopiladi. <strong>world</strong> (belgisiz) izohni '
                    'kesimga yopishtirib yuboradi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>The cave was sealed around the year ______ it was not opened again '
                'until 1900.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['1000', '1000 and,', '1000,', '1000;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>1000;</strong>. Boʻshliqning ikki tomonida ham '
                    'toʻliq mustaqil gap turibdi, ularni nuqtali vergul ajratadi. '
                    '<strong>1000,</strong> — comma splice, ingliz tilidagi eng keng '
                    'tarqalgan punktuatsiya xatosi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>The only plants that ______ the voyage before 1830 were the few that '
                'happened to be unusually hardy.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['— survived', ', survived', 'survived', 'survived,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>survived</strong> — hech qanday belgi '
                    'kerak emas. "that survived the voyage before 1830" oʻsimliklarni '
                    '<em>aniqlaydigan</em> ergash gap: usiz "the only plants" iborasi '
                    'maʼnosiz qoladi, shuning uchun u ajratilmaydi.'},

    # ── Standard English Conventions: Form, Structure, and Sense (18–21)
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The collection of manuscripts that the monk found behind the wall '
                '______ some fifty thousand separate items.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are numbering', 'have numbered', 'number', 'numbers'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>numbers</strong>. Ega — '
                    '<em>collection</em>, birlik; "of manuscripts that the monk found '
                    'behind the wall" faqat aniqlovchi. Feʼlga yaqin turgan "wall" bilan '
                    'emas, egani bilan moslashtiring — oraliq iborani yopib koʻring.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time the cave was opened in 1900, the manuscripts ______ behind '
                'a sealed wall for nine hundred years.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['had been sitting', 'has been sitting', 'sit', 'will have sat'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>had been sitting</strong>. "By the time…was '
                    'opened" oʻtmishdagi nuqtani beradi, holat esa undan oldin boshlanib '
                    'oʻsha nuqtagacha davom etgan — past perfect continuous. '
                    '<strong>has been sitting</strong> hozirgi paytga ulaydi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>Neither the notebooks nor the will ______ any reason for the twenty-year '
                'delay.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are giving', 'give', 'gives', 'have given'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>gives</strong>. "Neither…nor" qurilishida feʼl '
                    'oʻziga <em>yaqin turgan</em> egaga moslashadi, "the will" esa birlik. '
                    '<strong>give</strong> tuzoq: ikki narsa sanalgani uchun quloq '
                    'koʻplikni kutadi, lekin "neither…nor" ularni birlashtirmaydi.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>______ the Wardian case turned a voyage that killed nineteen plants in '
                'twenty into one that killed a single plant.</p>',
     'question_text': CONVENTION_Q,
     'choices': [
         'Having sealed it against the salt air,',
         'Sealed against the salt air,',
         'Sealing it against the salt air,',
         'To seal it against the salt air,',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Sealed against the</strong>… Boshlanuvchi ibora '
                    'egani — <em>the case</em> — aniqlashi kerak, quti esa '
                    '<em>berkitilgan</em>: majhul maʼno, demak III shakl. '
                    '<strong>Sealing it against the</strong>… aniq nisbat beradi va '
                    'qutining oʻzi nimanidir berkitayotgan boʻlib chiqadi.'},

    # ── Expression of Ideas: Transitions (22–24) ───────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>A prime cycle cannot be divided evenly by any shorter cycle. ______ a '
                'predator that peaks every two, three or four years almost never meets an '
                'emergence.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'By contrast,', 'For example,', 'Nevertheless,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Accordingly,</strong>. Boʻlinmaslik — '
                    'sabab, uchrashuvning boʻlmasligi — undan kelib chiqadigan '
                    'natija. <strong>Nevertheless,</strong> qarama-qarshilik talab qiladi, '
                    'bu yerda esa ikkala jumla bir tomonga qaraydi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Af Klint’s instruction was that the work should wait twenty years '
                'after her death. ______ it waited more than forty.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'For example,', 'In fact,', 'Likewise,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>In fact,</strong>. Ikkinchi jumla birinchisini '
                    'tuzatadi va kuchaytiradi: yigirma emas, qirqdan ortiq. '
                    '<strong>Accordingly,</strong> koʻrsatma bajarilgandek koʻrsatadi, '
                    'aslida esa muddat ancha oshib ketgan.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>A margin of that kind is bought once and cannot be bought again. ______ '
                'every generation of Londoners since has been spending a decision taken in '
                'the 1860s.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['By contrast,', 'In effect,', 'Nevertheless,', 'Previously,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>In effect,</strong>. Ikkinchi jumla birinchisini '
                    'boshqa soʻz bilan, aniqroq qilib aytadi — qayta sotib '
                    'boʻlmaydigan zaxira demak, uni hamon sarflayapmiz. <strong>By '
                    'contrast,</strong> ziddiyat talab qiladi, bu yerda esa takroriy '
                    'ifoda bor.'},

    # ── Expression of Ideas: Rhetorical Synthesis (25–27) ──────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Jeanne Baret sailed on Bougainville’s 1766 expedition disguised '
                'as a man.</li>'
                '<li>She worked as valet to the ship’s botanist, Philibert '
                'Commerson.</li>'
                '<li>She collected and pressed most of the expedition’s six thousand '
                'specimens.</li>'
                '<li>The specimens are catalogued under Commerson’s name.</li>'
                '<li>A plant genus named <i>Baretia</i> in her honour was later '
                'renamed.</li></ul>',
     'question_text': 'The student wants to emphasize the gap between Baret’s '
                      'contribution and her credit. Which choice most effectively uses '
                      'relevant information from the notes to accomplish this goal?',
     'choices': [
         'A plant genus was named <i>Baretia</i> in her honour.',
         'Baret worked as valet to the expedition’s botanist, Philibert Commerson.',
         'Jeanne Baret sailed on Bougainville’s expedition of 1766 disguised as a man.',
         'She collected and pressed most of the six thousand specimens the voyage brought home, yet they are catalogued under Commerson’s name and the one genus named for her was later renamed.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>She collected and pressed</strong>… Tafovut '
                    'koʻrinishi uchun ikki tomon ham kerak: u nima qilgani va nomi '
                    'qayerda. Faqat shu variant ikkalasini bitta jumlaga qoʻyadi. '
                    '<strong>A plant genus was named <i>Baretia</i> in her honour</strong>… '
                    'hatto teskari taassurot qoldiradi — keyin bekor qilingani '
                    'aytilmagan.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Before 1830 most plants sent by sea died on the voyage.</li>'
                '<li>Nathaniel Ward’s case is a sealed glass box over a tray of '
                'soil.</li>'
                '<li>Water evaporates from the soil, condenses on the glass and runs back '
                'down.</li>'
                '<li>The case therefore needs no watering.</li>'
                '<li>Survival rose from about one plant in twenty to nineteen in '
                'twenty.</li></ul>',
     'question_text': 'The student wants to explain how the case works to an audience '
                      'unfamiliar with it. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'Before 1830 most plants sent by sea died before they arrived.',
         'Survival on long voyages rose from about one plant in twenty to nineteen in twenty.',
         'Ward’s case is a sealed glass box standing over a tray of soil.',
         'Water evaporates from the soil, condenses on the glass and runs back down, so a sealed box waters itself for months — which is why survival rose from one plant in twenty to nineteen.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Water evaporates from</strong>… Maqsad '
                    '<em>qanday ishlashini</em> tushuntirish, demak javob aylanani '
                    '(bugʻlanish → kondensatsiya → qaytish) va uning natijasini bersin. '
                    '<strong>Ward’s case is a sealed glass box</strong>… qutini '
                    'tasvirlaydi, lekin ichida nima sodir boʻlishini aytmaydi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>The cave at Dunhuang was sealed around the year 1000.</li>'
                '<li>It held some fifty thousand manuscripts in seventeen languages.</li>'
                '<li>Many of them are worn copies, duplicates and scraps.</li>'
                '<li>The manuscripts are not valuable objects in themselves.</li>'
                '<li>The leading explanation is that sacred writing could not be thrown '
                'away.</li></ul>',
     'question_text': 'The student wants to present the leading explanation together with '
                      'the evidence for it. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'Many of the manuscripts in the cave are worn copies, duplicates and scraps.',
         'The cave at Dunhuang was sealed around the year 1000 and opened in 1900.',
         'The cave held some fifty thousand manuscripts written in seventeen languages.',
         'The manuscripts are mostly worn copies and scraps rather than treasures — which fits the leading explanation, that this was sacred writing too damaged to use and too holy to discard.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The manuscripts are mostly</strong>… Maqsad '
                    'ikki talabli: izoh <em>va</em> uning dalili. Faqat shu variant '
                    'qoʻlyozmalarning holatini dalil sifatida ishlatib, keyin izohni '
                    'beradi. <strong>Many of the manuscripts in the cave are worn copies, '
                    'duplicates and scraps</strong>… faqat dalilni beradi, undan nima kelib '
                    'chiqishini aytmaydi.'},
]
