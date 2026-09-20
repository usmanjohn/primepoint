# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 1 · Reading and Writing, Module 1
#  27 questions · 32 minutes · every taker sits this one.
#
#  Route: 18 or more correct here sends the taker to the UPPER module 2.
#
#  Load: python manage.py load_mock exam/data/sat1_rw1.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md
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

S = 'rw1'

# The three stems the digital SAT repeats verbatim, so they are written once.
WORD_Q = ('Which choice completes the text with the most logical and precise '
          'word or phrase?')
TRANSITION_Q = ('Which choice completes the text with the most logical '
                'transition?')
CONVENTION_Q = ('Which choice completes the text so that it conforms to the '
                'conventions of Standard English?')

QUESTIONS = [

    # ── Craft and Structure: Words in Context (1–4) ────────────────────
    {'section': S, 'number': 1, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>When no American flight school would admit her, Bessie Coleman '
                'did not abandon her ambition; she ______ it. She learned French, '
                'sailed to Paris, and in June 1921 earned a licence from the '
                'Fédération Aéronautique Internationale, becoming the first Black '
                'woman in the world to hold an international pilot’s licence.</p>',
     'question_text': WORD_Q,
     'choices': ['concealed', 'inherited', 'questioned', 'redirected'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>redirected</strong>. Nuqtali vergul qarama-qarshilik '
                    'qoʻyadi: u maqsadidan voz kechmadi — uni <em>boshqa yoʻlga burdi</em> '
                    '(fransuz tilini oʻrgandi, Parijga ketdi). <strong>questioned</strong> '
                    'chalgʻituvchi, chunki u ham "voz kechmadi"ga zid emasdek koʻrinadi, lekin '
                    'matnda shubha emas, harakat tasvirlangan.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>Uzbek suzani embroideries were traditionally made by a bride and '
                'her female relatives, each woman stitching a separate panel in her '
                'own household. Because the panels were joined only at the end, small '
                '______ in colour and stitch run across a single finished cloth — '
                'evidence of many hands rather than one.</p>',
     'question_text': WORD_Q,
     'choices': ['commissions', 'discrepancies', 'embellishments', 'replicas'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>discrepancies</strong> — nomuvofiqliklar. Matn '
                    'sababni oʻzi aytadi: panellar alohida uylarda tikilgan, shuning uchun rang '
                    'va chok bir xil chiqmagan. <strong>embellishments</strong> (bezaklar) '
                    'chalgʻituvchi, chunki mavzu kashtachilik; lekin bezak "koʻp qoʻl" dalili '
                    'emas, farq dalil.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>Suzanne Simard’s early reports of carbon moving between trees '
                'through fungal threads were met with ______: reviewers asked whether '
                'the isotopes could have reached the second tree through the soil '
                'instead, and several would not accept the result until the experiment '
                'had been repeated.</p>',
     'question_text': WORD_Q,
     'choices': ['acclaim', 'bewilderment', 'indifference', 'skepticism'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>skepticism</strong>. Ikki nuqtadan keyingi jumla '
                    'maʼnoni ochib beradi: retsenzentlar muqobil sababni soʻrashdi va takroriy '
                    'tajriba talab qilishdi — bu shubha. <strong>indifference</strong> '
                    '(befarqlik) notoʻgʻri: befarq odam savol bermaydi va takror talab qilmaydi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>The researchers were careful to <u>qualify</u> their conclusion. '
                'The fungal network, they wrote, had moved carbon between trees in the '
                'plots they studied; whether it did so in every forest, or in amounts '
                'large enough to matter to a seedling’s survival, remained open.</p>',
     'question_text': 'As used in the text, what does the word <u>qualify</u> most nearly mean?',
     'choices': ['certify', 'dispute', 'limit', 'restate'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>limit</strong>. Keyingi jumla xulosaning '
                    'chegarasini koʻrsatadi: "oʻrgangan uchastkalarda" — boshqa joyda '
                    'nomaʼlum. <strong>certify</strong> (tasdiqlash) aynan teskari maʼno va eng '
                    'kuchli tuzoq, chunki "qualify" soʻzi kundalik ingliz tilida "malakaga ega '
                    'boʻlmoq" maʼnosida ham ishlatiladi. Kontekst hal qiladi, lugʻat emas.'},

    # ── Craft and Structure: Text Structure and Purpose (5–6) ──────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>Katsushika Hokusai was seventy when he began <i>Thirty-Six Views of '
                'Mount Fuji</i>, the series that contains <i>The Great Wave off '
                'Kanagawa</i>. The print is usually read as a study of the sea. But '
                'Fuji appears in every image in the series, and in <i>The Great Wave</i> '
                'it sits small and still at the centre of the composition while the '
                'water rears above it. The wave is what the eye finds first; the '
                'mountain is what the series is about.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that a familiar print is better understood as part of the series containing it',
         'To compare <i>The Great Wave</i> with other Japanese depictions of Mount Fuji',
         'To describe the technique by which Hokusai produced colour woodblock prints',
         'To explain why Hokusai waited until late in life to begin a major series',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>To argue that a familiar print</strong>… Matnning '
                    'butun harakati shu: mashhur asar odatda dengiz haqida deb oʻqiladi, '
                    'ammo turkumda Fuji har rasmda bor — demak asarni turkum ichida koʻrish '
                    'kerak. <strong>To explain why Hokusai waited</strong>… tuzoq: yetmish yosh '
                    'birinchi jumlada aytilgan, lekin matn buni tushuntirmaydi, faqat eslatadi. '
                    'Birinchi jumlada uchragan fakt matnning maqsadi emas.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>Cities are hotter than the countryside around them, sometimes by as '
                'much as 7°C on a summer night. <u>The cause is not the people but '
                'the pavement.</u> Asphalt and concrete absorb sunlight through the day '
                'and release it slowly after dark, so an urban surface can still be '
                'radiating heat at midnight, long after a nearby field has cooled.</p>',
     'question_text': 'Which choice best describes the function of the underlined '
                      'sentence in the text as a whole?',
     'choices': [
         'It identifies a likely misconception and corrects it, setting up the explanation that follows.',
         'It introduces an exception to the pattern described in the first sentence.',
         'It offers evidence for a claim that the text goes on to qualify.',
         'It summarizes the conclusion the text reaches in its final sentence.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>It identifies a likely misconception</strong>… '
                    'Jumla "odamlar emas, asfalt" deb notoʻgʻri tasavvurni rad etadi va keyingi '
                    'jumla aynan asfalt qanday ishlashini tushuntiradi. <strong>It offers '
                    'evidence</strong>… notoʻgʻri: bu jumla dalil keltirmaydi — dalil undan '
                    'keyin keladi.'},

    # ── Craft and Structure: Cross-Text Connections (7) ────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>Since the Kokaral Dam was completed in 2005, the '
                'North Aral Sea has risen by several metres and commercial fishing has '
                'returned to the port of Aralsk. For many observers the recovery shows '
                'what a single well-placed piece of engineering can accomplish: the '
                'water came back faster than almost anyone had predicted.</p>'
                '<p><b>Text 2</b><br>Others are less willing to generalize. The North '
                'Aral is a small fraction of the original sea, and it was refilled by '
                'holding back flow that had been reaching the far larger southern '
                'basin. What happened at Kokaral, they argue, was not the recovery of '
                'the Aral Sea but a decision about which part of it to save.</p>',
     'question_text': 'Based on the texts, how would the authors described in Text 2 '
                      'most likely respond to the characterization of the Kokaral Dam '
                      'in Text 1?',
     'choices': [
         'By agreeing that the dam raised the northern basin but adding that the gain was confined to one part of the sea and came at the southern basin’s expense',
         'By arguing that the recovery described in Text 1 proceeded more slowly than observers had expected',
         'By disputing the claim that water levels in the North Aral Sea have risen since 2005',
         'By suggesting that engineering projects rarely produce measurable environmental change',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>By agreeing that the dam raised</strong>… 2-matn '
                    'faktni inkor qilmaydi — u faktning <em>maʼnosi</em> bilan bahslashadi: '
                    'shimol koʻtarildi, lekin janub hisobiga. <strong>By disputing the '
                    'claim</strong>… eng keng tarqalgan xato: talaba "less willing" degan '
                    'soʻzni koʻrib, 2-matn hamma narsani rad etadi deb oʻylaydi. Ikki matnli '
                    'savolda avval <em>nimaga qoʻshiladi</em>, keyin nimaga qoʻshilmaydi deb '
                    'ajrating.'},

    # ── Information and Ideas: Central Ideas and Details (8–9) ─────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>Rosalind Franklin’s X-ray diffraction images of DNA were made '
                'with an apparatus she had rebuilt herself. She fitted a finer '
                'collimator, redesigned the camera’s humidity control, and learned '
                'to draw the fibre so that a single orientation dominated the pattern. '
                'Photograph 51 is often described as a lucky exposure. It took one '
                'hundred hours.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Franklin was more interested in designing instruments than in the structure of DNA.',
         'Franklin’s apparatus was more advanced than any other in use at the time.',
         'Franklin’s most famous image was the product of deliberate technical work rather than of luck.',
         'Photograph 51 required a longer exposure than Franklin had originally planned.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Franklin’s most famous image was the '
                    'product</strong>… Oxirgi ikki jumla butun matnning maqsadi: "omadli kadr" '
                    'deyishadi — aslida yuz soat. Undan oldingi jumlalar esa u asbobni oʻzi '
                    'qayta qurganini sanaydi. <strong>Photograph 51 required a longer '
                    'exposure than Franklin had originally planned</strong> notoʻgʻri: matnda '
                    'reja haqida bir soʻz ham yoʻq — bu oʻqilmagan maʼlumot.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>In her 1843 notes on Charles Babbage’s Analytical Engine, Ada '
                'Lovelace wrote out a sequence of operations for computing Bernoulli '
                'numbers — an example often called the first published computer '
                'program. But the notes go further than the example. The engine, she '
                'argued, need not work on numbers at all: if the relations between '
                'pitched sounds could be expressed in its symbols, it could compose '
                'music. Babbage had designed a calculator. Lovelace described a machine '
                'that manipulates symbols, of which arithmetic is only one case.</p>',
     'question_text': 'According to the text, what distinguished Lovelace’s '
                      'understanding of the Analytical Engine from Babbage’s?',
     'choices': [
         'She believed the machine could be built more cheaply than Babbage had estimated.',
         'She recognized that the machine could operate on symbols other than numbers.',
         'She was the first person to calculate Bernoulli numbers using the machine.',
         'She thought the machine’s chief value lay in its speed rather than its accuracy.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>She recognized that the machine could operate on '
                    'symbols</strong>… Matn oxirgi ikki jumlada farqni ochiq qoʻyadi: Babbage '
                    'kalkulyator, Lovelace esa belgilar bilan ishlaydigan mashina koʻrdi. '
                    '<strong>She was the first person to calculate Bernoulli numbers</strong>… '
                    'tuzoq: Bernulli sonlari matnda bor, lekin u <em>farq</em> emas — matn '
                    'buni "misol" deb ataydi va "notes go further than the example" deydi.'},

    # ── Information and Ideas: Command of Evidence (10–12) ─────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>Seedlings growing in the shade of a mature tree often survive better '
                'than seedlings in open ground. One researcher hypothesizes that this '
                'is because carbon reaches them through fungal threads connecting their '
                'roots to the mature tree, rather than because the canopy shelters them '
                'from wind and frost.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'researcher’s hypothesis?',
     'choices': [
         'Fungal threads can be traced between the roots of trees belonging to different species.',
         'Mature trees growing in dense forest have more extensive fungal networks than mature trees growing alone.',
         'Seedlings growing in full sunlight accumulate carbon more quickly than seedlings growing in shade.',
         'Shaded seedlings joined to a mature tree by fungal threads accumulate more carbon than shaded seedlings whose threads have been cut.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Shaded seedlings joined to a mature tree</strong>… '
                    'Gipoteza ikki sababni ajratmoqchi: soya (shamol-sovuqdan himoya) yoki '
                    'zamburugʻ orqali uglerod. Bu variantda ikkala guruh ham soyada — faqat '
                    'zamburugʻ ipi farq qiladi, demak sabab ajraladi. <strong>Fungal threads '
                    'can be traced</strong>… faqat ip borligini koʻrsatadi, uglerod oʻtishini '
                    'emas: dalil gipotezani emas, uning shart-sharoitini tasdiqlaydi.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>Textile historian Dilnoza Rakhimova argues that the irregularities '
                'in nineteenth-century suzani cloths were not merely tolerated but '
                'intended — that a maker deliberately left one visible break in the '
                'border of a finished piece.</p>',
     'question_text': 'Which finding, if true, would most strongly support '
                      'Rakhimova’s argument?',
     'choices': [
         'In cloths stitched by a single maker, a break in the border pattern still appears, always in one corner.',
         'Nineteenth-century suzanis were completed more quickly than twentieth-century examples.',
         'Panels stitched in different households vary in the exact shade of silk thread used.',
         'Suzani borders are stitched more tightly than the central medallions they surround.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>In cloths stitched by a single maker</strong>… '
                    'Rakhimova "ataylab" deydi. Bitta usta ishlagan matoda ham uzilish '
                    'chiqsa, uni "turli uylar" bilan izohlab boʻlmaydi — bitta usta xohlasa '
                    'uzluksiz qila olardi. <strong>Panels stitched in different '
                    'households</strong>… aynan teskari ishlaydi: u uzilishni <em>tasodif</em> '
                    'bilan izohlaydi, yaʼni argumentni zaiflashtiradi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>On a single August night, researchers recorded air temperature at '
                'four sites in Tashkent at 1:00 a.m., together with the share of each '
                'site’s area shaded by tree canopy.</p>'
                '<table><tr><th>Site</th><th>Tree canopy (%)</th>'
                '<th>Temperature at 1:00 a.m. (°C)</th></tr>'
                '<tr><td>Chilonzor</td><td>8</td><td>31.4</td></tr>'
                '<tr><td>Yunusobod</td><td>16</td><td>30.1</td></tr>'
                '<tr><td>Mirzo Ulugʻbek</td><td>24</td><td>29.3</td></tr>'
                '<tr><td>Botanical Garden</td><td>47</td><td>27.2</td></tr></table>',
     'question_text': 'A student concludes that, among these four sites, greater tree '
                      'canopy cover is associated with a lower night-time temperature. '
                      'Which choice best describes data from the table that support '
                      'this conclusion?',
     'choices': [
         'All four sites recorded a temperature above 27°C.',
         'Chilonzor had the smallest share of tree canopy of the four sites.',
         'The Botanical Garden had more than five times the canopy cover of Chilonzor.',
         'The site with the most canopy, the Botanical Garden, was the coolest, and the site with the least, Chilonzor, was the warmest.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The site with the most canopy</strong>… Xulosa '
                    'ikki kattalik orasidagi bogʻliqlik haqida, shuning uchun dalil ham '
                    '<em>ikkalasini</em> birga aytishi shart. Qolgan uchtasi jadvalga koʻra '
                    'toʻgʻri, lekin har biri faqat bitta ustunni gapiradi — <strong>Chilonzor '
                    'had the smallest share</strong> harorat haqida hech narsa demaydi. '
                    'Jadval savolida "rost" yetarli emas, "xulosani tutadi" kerak.'},

    # ── Information and Ideas: Inferences (13–14) ──────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>Conventional concrete cracks as it ages, and water entering a crack '
                'corrodes the steel inside. One remedy mixes dormant bacteria and a '
                'calcium compound into the concrete: when a crack lets water in, the '
                'bacteria wake, consume the compound, and deposit limestone that seals '
                'the gap. The repair therefore depends on the very condition it is '
                'meant to prevent, since ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'steel reinforcement is unnecessary in concrete of this kind.',
         'the bacteria must be replaced at regular intervals by maintenance crews.',
         'the concrete must crack and admit water before the bacteria can act.',
         'the limestone deposited is stronger than the concrete surrounding it.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>the concrete must crack and admit water</strong>… '
                    '"the very condition it is meant to prevent" — oldini olinmoqchi boʻlgan '
                    'holat aynan yoriq va suv, va bakteriya faqat oʻsha holatda uygʻonadi. '
                    'Qolgan uchtasi matnda umuman aytilmagan: <strong>the limestone '
                    'deposited</strong>… mustahkamlik haqida matn hech narsa demaydi. '
                    'Xulosa faqat matndagi soʻzlardan chiqishi kerak.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>Languages with very large speaker populations tend to have simpler '
                'inflectional morphology than languages with small ones. One explanation '
                'points to adult learners: an adult acquiring a second language '
                'regularizes what a child would simply memorize, and a language that '
                'many adults learn is pushed, generation after generation, toward its '
                'regular patterns. If this explanation is correct, a language’s '
                'grammatical complexity should depend less on the number of its '
                'speakers than on ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'how long the language has existed in written form.',
         'how many of its speakers acquired it as adults.',
         'the number of other languages spoken in neighbouring regions.',
         'whether its speakers are geographically concentrated.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>how many of its speakers acquired it as '
                    'adults</strong>. Izohda sabab kattalar emas, <em>kattalar soni</em>: '
                    'katta til oddiylashadi, chunki uni koʻp kattalar oʻrganadi. Demak haqiqiy '
                    'omil — kattalar ulushi, soʻzlovchilar soni esa faqat uning belgisi. '
                    '<strong>whether its speakers are geographically concentrated</strong> '
                    'tuzoq: mantiqan maʼqul koʻrinadi, lekin matn geografiyani tilga olmaydi.'},

    # ── Standard English Conventions: Boundaries (15–17) ───────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>Photograph 51, the X-ray diffraction image that first revealed the '
                'helical structure of ______ was made by Rosalind Franklin and her '
                'student Raymond Gosling in May 1952.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['DNA', 'DNA,', 'DNA:', 'DNA;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>DNA,</strong>. "the X-ray diffraction image…DNA" — '
                    'bu <em>Photograph 51</em> ga izoh (appozitsiya) va u vergul bilan '
                    'boshlangan, demak vergul bilan yopilishi shart: juftlik ochilgan joyda '
                    'yopiladi. <strong>DNA;</strong> notoʻgʻri, chunki nuqtali vergul ikki '
                    'mustaqil gapni ajratadi — bu yerda esa bitta gap bor.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Simard’s team injected two isotopes of carbon into neighbouring '
                '______ one into a Douglas fir and the other into a paper birch — '
                'and then traced where each isotope appeared.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['trees', 'trees —', 'trees,', 'trees;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>trees —</strong>. Gapda yopuvchi tire allaqachon '
                    'turibdi ("birch — and then"), demak ochuvchisi ham tire boʻlishi kerak: '
                    'qoʻshimcha izoh <em>bir xil</em> belgilar orasiga olinadi. '
                    '<strong>trees,</strong> eng koʻp tanlanadigan xato — vergul va tire '
                    'juftlik hosil qilmaydi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>Lovelace’s notes appeared in print under the initials ______ she '
                'was not publicly named as their author for another forty years.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['A.A.L. and,', 'A.A.L.', 'A.A.L.,', 'A.A.L.;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>A.A.L.;</strong>. Boʻshliqning ikki tomonida ham '
                    'toʻliq mustaqil gap bor ("notes appeared…" va "she was not…"), '
                    'ularni faqat nuqtali vergul (yoki nuqta, yoki vergul+bogʻlovchi) ajratadi. '
                    '<strong>A.A.L.,</strong> — comma splice, ingliz tilidagi eng keng '
                    'tarqalgan punktuatsiya xatosi va aynan shu savolning tuzogʻi.'},

    # ── Standard English Conventions: Form, Structure, and Sense (18–21)
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The collection of suzani panels held by the museum in Bukhara ______ '
                'more than four hundred pieces, many of them unfinished.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are including', 'have included', 'include', 'includes'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>includes</strong>. Ega — <em>collection</em>, '
                    'birlik; "of suzani panels held by the museum" faqat aniqlovchi. SAT bu '
                    'savolni doim shunday quradi: ega bilan feʼl orasiga uzun ibora qoʻyib, '
                    'quloqni <strong>include</strong> ga tortadi. Feʼlni tanlashdan oldin '
                    'oraliq iborani yopib, egani toping.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time Coleman returned to the United States in September 1921, '
                'she ______ the only licensed Black woman pilot in the world.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['becomes', 'had become', 'has become', 'will have become'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>had become</strong>. "By the time…returned" '
                    'oʻtmishdagi nuqtani beradi, hodisa esa undan <em>oldin</em> sodir '
                    'boʻlgan — bu past perfect. <strong>has become</strong> tuzoq: present '
                    'perfect hozirgi paytga bogʻlanadi, gap esa 1921-yilda.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>Each of the four measurement sites recorded ______ lowest temperature '
                'shortly before dawn.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['it’s', 'its', 'their', 'they’re'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>its</strong>. <em>Each</em> har doim birlik, '
                    'shuning uchun "their" mos kelmaydi; <em>its</em> esa egalik olmoshi. '
                    '<strong>it’s</strong> = "it is" — qisqartma, egalik emas: apostrof '
                    'ingliz tilida egalikni emas, tushib qolgan harfni bildiradi.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Hokusai signed his prints under more than thirty different names, '
                'changing his signature whenever he changed his style, his subject, or '
                '______</p>',
     'question_text': CONVENTION_Q,
     'choices': ['he moved house.', 'his place of residence.', 'living somewhere new.', 'where he was living.'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>his place of residence</strong>. Ketma-ketlik '
                    '"his style, his subject, or ___" — ikkitasi ham <em>egalik + ot</em>, '
                    'demak uchinchisi ham shunday boʻlishi kerak (parallelizm). '
                    '<strong>where he was living</strong> maʼno jihatdan toʻgʻri va shuning '
                    'uchun chalgʻituvchi, lekin bu ergash gap — qatorning shaklini buzadi.'},

    # ── Expression of Ideas: Transitions (22–24) ───────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>Asphalt and concrete absorb sunlight through the day and give it up '
                'only slowly after dark. ______ a city street can still be radiating '
                'heat at midnight, long after a field on the edge of town has cooled.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['As a result,', 'For example,', 'In contrast,', 'Nevertheless,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>As a result,</strong>. Birinchi jumla sabab '
                    '(sekin sovish), ikkinchisi natija (yarim tunda ham issiq). '
                    '<strong>For example,</strong> tuzoq: ikkinchi jumla birinchisining '
                    'misoli emas, oqibati — misol boʻlsa, u xuddi shu fikrni takrorlagan '
                    'boʻlardi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Franklin’s diffraction images were the clearest then in '
                'existence. ______ she did not publish a structural model of DNA before '
                'Watson and Crick did; her notebooks show her testing a helix against '
                'the data rather than proposing one ahead of it.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Likewise,', 'Nevertheless,', 'Therefore,', 'That is,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Nevertheless,</strong>. Eng yaxshi rasmlarga ega '
                    'boʻlish modelni birinchi eʼlon qilishni kutilgan qiladi — lekin '
                    'boʻlmadi. Demak qarama-qarshilik. <strong>Therefore,</strong> aynan '
                    'teskari bogʻlanish va eng koʻp tanlanadigan xato: "clearest" soʻzi '
                    'talabani natija kutishga undaydi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>Since 2005 the North Aral Sea has risen by several metres and its '
                'fishery has recovered. The southern basin, ______ has gone on '
                'shrinking: the water that refilled the north is water that no longer '
                'reaches it.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['as a result,', 'by contrast,', 'for instance,', 'in addition,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>by contrast,</strong>. Shimol koʻtarildi, janub '
                    'qurishda davom etdi — ikki qarama-qarshi taqdir. <strong>as a '
                    'result,</strong> juda kuchli tuzoq, chunki oxirgi qism haqiqatan ham '
                    'sababni aytadi; ammo bogʻlovchi <em>ikki jumla</em> munosabatini '
                    'bildiradi, ikkinchi jumla ichidagi izohni emas.'},

    # ── Expression of Ideas: Rhetorical Synthesis (25–27) ──────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Bessie Coleman was born in Atlanta, Texas, in 1892.</li>'
                '<li>No American flight school would admit her.</li>'
                '<li>She learned French and travelled to Paris in 1920.</li>'
                '<li>In June 1921 she earned a licence from the Fédération '
                'Aéronautique Internationale.</li>'
                '<li>She was the first Black woman in the world to hold an '
                'international pilot’s licence.</li></ul>',
     'question_text': 'The student wants to emphasize the obstacle Coleman overcame. '
                      'Which choice most effectively uses relevant information from the '
                      'notes to accomplish this goal?',
     'choices': [
         'Bessie Coleman, who was born in Atlanta, Texas, in 1892, earned her pilot’s licence in June 1921.',
         'Coleman earned her licence from the Fédération Aéronautique Internationale, an organization based in Europe.',
         'In 1920 Coleman travelled to Paris, where she remained until June of the following year.',
         'Refused admission by every American flight school, Coleman learned French, sailed to Paris, and earned an international pilot’s licence in 1921.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Refused admission by every American flight '
                    'school</strong>… Maqsad — <em>toʻsiqni</em> taʼkidlash, va faqat shu '
                    'variant toʻsiqni (rad javobi) hamda uning yengilishini birga beradi. '
                    'Qolganlari ham qaydlardan olingan va rost, lekin toʻsiqni tilga olmaydi. '
                    'Sintez savolida "rost" yetarli emas — berilgan <em>maqsad</em> hal '
                    'qiladi.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Conventional concrete cracks as it ages.</li>'
                '<li>Water entering a crack corrodes the steel inside.</li>'
                '<li>Self-healing concrete contains dormant bacteria and a calcium '
                'compound.</li>'
                '<li>Water entering a crack activates the bacteria.</li>'
                '<li>The bacteria deposit limestone, which seals the crack.</li></ul>',
     'question_text': 'The student wants to explain the process of self-healing concrete '
                      'to an audience unfamiliar with it. Which choice most effectively '
                      'uses relevant information from the notes to accomplish this goal?',
     'choices': [
         'Because conventional concrete cracks as it ages, water reaches the steel inside it.',
         'In self-healing concrete, water entering a crack wakes dormant bacteria, which consume a calcium compound and deposit limestone that seals the crack.',
         'Self-healing concrete contains dormant bacteria as well as a calcium compound.',
         'Water is the chief enemy of conventional concrete and the chief tool of self-healing concrete.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>In self-healing concrete, water entering a '
                    'crack</strong>… Maqsad — <em>jarayonni</em> tushuntirish, demak javob '
                    'bosqichlarni ketma-ket bersin: suv → bakteriya → ohaktosh → yoriq yopiladi. '
                    '<strong>Water is the chief enemy</strong>… chiroyli jumla va shuning '
                    'uchun xavfli: u jarayonni emas, qarama-qarshilikni beradi — tinglovchi '
                    'baribir nima sodir boʻlishini bilmaydi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Suzanne Simard published a study in the journal <i>Nature</i> in '
                '1997.</li>'
                '<li>She injected two different isotopes of carbon into neighbouring '
                'trees.</li>'
                '<li>One isotope went into a Douglas fir, the other into a paper '
                'birch.</li>'
                '<li>Each isotope was later found in the other tree.</li>'
                '<li>The transfer took place through fungal threads linking the two '
                'root systems.</li></ul>',
     'question_text': 'The student wants to introduce the study and its result to an '
                      'audience unfamiliar with it. Which choice most effectively uses '
                      'relevant information from the notes to accomplish this goal?',
     'choices': [
         'Douglas fir and paper birch are two of the commonest species in the forests where Simard worked.',
         'In a 1997 study, Simard injected different carbon isotopes into a Douglas fir and a paper birch and later found each isotope in the other tree, carried there by fungal threads linking their roots.',
         'Simard’s study appeared in <i>Nature</i>, one of the most widely read scientific journals, in 1997.',
         'Two isotopes of carbon were used in the study rather than one.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>In a 1997 study, Simard injected</strong>… '
                    'Maqsad ikki qismli: tadqiqotni <em>tanishtirish</em> va <em>natijani</em> '
                    'aytish. Faqat shu variant ikkalasini ham bajaradi. <strong>Simard’s '
                    'study appeared in <i>Nature</i></strong>… tadqiqotni tanishtiradi, lekin '
                    'natijani aytmaydi — yarim maqsad bajarilgan javob notoʻgʻri javobdir.'},
]
