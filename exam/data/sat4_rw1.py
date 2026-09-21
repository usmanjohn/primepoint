# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 4 · Reading and Writing, Module 1
#  27 questions · 32 minutes · every taker sits this one.
#
#  Route: 18 or more correct here sends the taker to the UPPER module 2.
#
#  Load: python manage.py load_mock exam/data/sat4_rw1.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md
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
     'passage': '<p>In 1847 Ignaz Semmelweis found that deaths from childbed fever on his '
                'ward fell by nine-tenths once doctors washed their hands in chlorinated '
                'lime before entering it. His colleagues did not ______ the finding; they '
                'resented it, because it implied that they had been carrying the disease '
                'themselves.</p>',
     'question_text': WORD_Q,
     'choices': ['dispute', 'publish', 'repeat', 'understand'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>dispute</strong>. Nuqtali vergul '
                    'qarama-qarshilik qoʻyadi: ular raqamga qarshi <em>bahslashmadi</em>, '
                    'ular undan gʻashlandi. <strong>understand</strong> chalgʻituvchi, '
                    'chunki tushunmaslik ham rad etishga oʻxshaydi; ammo matn aksincha '
                    'aytadi — ular juda yaxshi tushunishgan, shuning uchun '
                    'gʻashlanishgan.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>A naked mole rat lives for thirty years, ten times as long as a mouse '
                'of the same size, and almost never develops a tumour. Biologists study the '
                'animal not because it is typical of mammals but because it is so '
                'thoroughly ______.</p>',
     'question_text': WORD_Q,
     'choices': ['domesticated', 'exceptional', 'fragile', 'social'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>exceptional</strong>. "not because it is '
                    'typical but because it is so thoroughly ___" qurilishi boʻshliqqa '
                    '<em>typical</em> ning teskarisini talab qiladi. <strong>social</strong> '
                    'kalamush haqida rost boʻlishi mumkin, lekin gap qurilishi rostlikni '
                    'emas, qarama-qarshilikni soʻraydi.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>A bowl repaired by kintsugi is mended with lacquer and powdered gold, '
                'so that the break is not hidden but ______: the seams run gold across the '
                'glaze, and the object carries its own history where anyone can see it.</p>',
     'question_text': WORD_Q,
     'choices': ['concealed', 'declared', 'repeated', 'smoothed'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>declared</strong>. "not hidden but ___" '
                    'qurilishi yashirishning teskarisini talab qiladi, ikki nuqtadan '
                    'keyingi qism esa buni ochadi: oltin chok koʻrinib turadi. '
                    '<strong>concealed</strong> aynan "hidden" ning sinonimi — gap '
                    'qurilishining oʻzi uni chiqarib tashlaydi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>The mantle is not liquid. Seismic shear waves pass through it, and '
                'shear waves do not travel in a liquid. Over a human lifetime the mantle is '
                'rock; over a million years it is <u>plastic</u>, flowing slowly enough '
                'that continents ride on it and fast enough that they move.</p>',
     'question_text': 'As used in the text, what does the word <u>plastic</u> most nearly '
                      'mean?',
     'choices': ['artificial', 'brittle', 'deformable', 'molten'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>deformable</strong> — shaklini '
                    'oʻzgartira oladigan. Vergul ortidagi ibora maʼnoni beradi: sekin '
                    'oqadi. <strong>molten</strong> (suyuqlangan) eng kuchli tuzoq va '
                    'matnning birinchi jumlasiga toʻgʻridan-toʻgʻri zid — mantiya '
                    'suyuq emas.'},

    # ── Craft and Structure: Text Structure and Purpose (5–6) ──────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>The Voyager record carries greetings in fifty-five languages, the sound '
                'of a kiss, and ninety minutes of music. It also carries, etched on its '
                'cover, the diagram of a hydrogen atom and a map of fourteen pulsars — '
                'the only two things on board that a finder could check against the sky. '
                'The greetings are for us. The cover is for them.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that the record is unlikely ever to be found by anyone',
         'To describe the process by which the contents of the record were chosen',
         'To distinguish the parts of the record addressed to a finder from the parts addressed to ourselves',
         'To explain how a map of pulsars can be used to locate the solar system',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>To distinguish the parts</strong>… Matn oxirgi '
                    'ikki jumlada boʻlinishni ochiq qoʻyadi: salomlar bizga, muqova ularga. '
                    '<strong>To explain how a map of pulsars can be used</strong>… xaritani '
                    'eslatadi, lekin uning qanday ishlashini tushuntirmaydi — matndagi '
                    'detal uning maqsadi emas.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>When Nicaragua opened its first schools for deaf children in 1977, the '
                'pupils arrived with home signs and no language in common. <u>What happened '
                'next is the closest thing linguistics has to a controlled '
                'experiment.</u> The first cohort built a rough pidgin out of what they '
                'had; the children who arrived a few years later, learning that pidgin '
                'young, regularised it into a grammar the first cohort had never used and '
                'could not fully follow.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It concedes that the evidence from Nicaragua is incomplete.',
         'It introduces a disagreement between linguists about the case.',
         'It restates the first sentence in more technical vocabulary.',
         'It states the claim that the rest of the text then supports with what the two cohorts produced.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>It states the claim</strong>… Jumla kuchli '
                    'daʼvo qoʻyadi ("nazorat qilinadigan tajribaga eng yaqin narsa"), '
                    'keyingi jumla esa aynan shu daʼvoni ikki avlodning natijasi bilan '
                    'asoslaydi. <strong>It concedes that the evidence from Nicaragua is '
                    'incomplete</strong>… teskari: jumla kamchilikni emas, qimmatni '
                    'taʼkidlaydi.'},

    # ── Craft and Structure: Cross-Text Connections (7) ────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>A team is editing elephant cells toward a cold-adapted '
                'genome, aiming at an animal that could graze the Siberian tundra as '
                'mammoths once did. The claim made for the project is ecological rather '
                'than sentimental: grazing compacts the snow, compacted snow insulates less '
                'well, and the permafrost below therefore stays colder.</p>'
                '<p><b>Text 2</b><br>Aigerim Sultanova does not dispute the grazing '
                'mechanism. She disputes the arithmetic of getting there. The herds that '
                'compacted Pleistocene snow numbered in the millions; a proof-of-concept '
                'calf in the 2030s implies a breeding programme running for centuries '
                'before any effect could be measured. Whatever else the project is, she '
                'argues, it is not a climate policy.</p>',
     'question_text': 'Based on the texts, Sultanova’s objection to the project is '
                      'that',
     'choices': [
         'editing elephant cells is unlikely to produce a viable animal at all.',
         'permafrost thaw is not in fact accelerated by the absence of grazing animals.',
         'the ecological mechanism the project relies on has never been demonstrated.',
         'the scale and the time required make it useless as a response to warming.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>the scale and the</strong>… 2-matn birinchi '
                    'jumladayoq mexanizmni qabul qiladi va eʼtirozni <em>arifmetikaga</em> '
                    'koʻchiradi: millionlab hayvon va asrlar kerak. <strong>the ecological '
                    'mechanism the project relies on has never been demonstrated</strong>… '
                    'matn ochiq rad etadigan javob — "does not dispute the grazing '
                    'mechanism".'},

    # ── Information and Ideas: Central Ideas and Details (8–9) ─────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>The Bayeux Tapestry is not a tapestry — it is embroidery, wool '
                'worked onto linen — and it was almost certainly made in England, by '
                'English needleworkers, for a Norman patron, within a generation of the '
                'conquest it depicts. That combination explains its oddities. The Normans '
                'win, as they must. But Harold dies with dignity, the English fight well, '
                'and the borders fill with small figures doing things the main story does '
                'not sanction.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Embroidery was a more common medium than weaving in eleventh-century England.',
         'The Tapestry is the most reliable surviving account of the Norman conquest.',
         'The Tapestry’s borders were added later by a different workshop.',
         'The Tapestry’s divided sympathies follow from its having been made by the defeated for the victors.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The Tapestry’s divided sympathies</strong>… '
                    'Matn kalit jumlani oʻrtaga qoʻyadi — "That combination explains '
                    'its oddities" — va keyin gʻaliz joylarni sanaydi. <strong>The '
                    'Tapestry’s borders were added later by a different '
                    'workshop</strong>… matnda aytilmagan: hoshiyalar eslatiladi, lekin '
                    'ularning keyin qoʻshilgani haqida hech narsa yoʻq.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>Nikolai Vavilov collected seed on five continents and built, in '
                'Leningrad, the largest crop collection in the world. He was arrested in '
                '1940 and died of starvation in prison in 1943. During the siege of '
                'Leningrad his staff stayed with the collection through the winter of 1941, '
                'in an unheated building, surrounded by edible seed, by rice and by '
                'potatoes. Several of them starved. Nothing was eaten.</p>',
     'question_text': 'According to the text, what did Vavilov’s staff do during the '
                      'siege?',
     'choices': [
         'They distributed part of the collection to the population of the city.',
         'They moved the collection out of the city before the siege closed.',
         'They remained with the collection and ate none of it, and several of them died.',
         'They replanted the collection in the spring of 1942.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>They remained with the</strong>… Matnning '
                    'oxirgi uch jumlasi aynan shu: qolishdi, ochlikdan oʻlishdi, va hech '
                    'narsa yeyilmadi. <strong>They distributed part of the collection to '
                    'the population</strong>… matnga zid — "Nothing was eaten" hech '
                    'qanday istisno qoldirmaydi.'},

    # ── Information and Ideas: Command of Evidence (10–12) ─────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A biologist proposes that the naked mole rat’s resistance to '
                'tumours comes from a sugar its cells secrete, which crowds the cells apart '
                'and stops them piling up, rather than from an unusually vigilant immune '
                'system — which would mean the protection ought to survive outside the '
                'animal, in a dish.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'biologist’s proposal?',
     'choices': [
         'Mice given transplanted mole rat tissue reject it within a few days.',
         'Mole rat cells grown in culture stop dividing at a much lower density than mouse cells, and lose that behaviour when the sugar is removed.',
         'Naked mole rats live in large underground colonies with a single breeding female.',
         'Naked mole rats can tolerate very low oxygen for long periods.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Mole rat cells grown</strong>… Taklif ikki '
                    'yoʻlni ajratadi: immunitet yoki hujayraning oʻz xossasi. Idishdagi '
                    'hujayrada immunitet yoʻq, demak uning ishlashi ikkinchi yoʻlni '
                    'tasdiqlaydi — va shakar olib tashlanganda xossa yoʻqoladi. '
                    '<strong>Naked mole rats can tolerate very low oxygen</strong>… boshqa '
                    'qobiliyat haqida, oʻsma haqida emas.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A historian claims that the Tapestry’s borders were used to say '
                'what the main register could not — that the needleworkers put into '
                'the margins a commentary the Norman patron would never have '
                'commissioned.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'historian’s claim?',
     'choices': [
         'Several border scenes show unarmed figures being robbed or burned out by soldiers, at points where the main register shows the Norman army advancing in good order.',
         'The borders are worked in the same eight wool colours as the main register.',
         'The borders contain animals drawn from Aesop’s fables, a common decorative source of the period.',
         'The final section of the Tapestry is missing.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Several border scenes show</strong>… Daʼvo '
                    'hoshiya asosiy hikoyaga <em>qarshi</em> gapirishi haqida, demak dalil '
                    'aynan shu ziddiyatni bir joyda koʻrsatishi kerak: yuqorida tartibli '
                    'yurish, chetida talon-taroj. <strong>The borders contain animals drawn '
                    'from Aesop’s fables</strong>… aksincha ishlaydi — u '
                    'hoshiyani odatdagi bezak deb tushuntiradi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>Researchers recorded the song of great tits at four sites in and around '
                'a city and measured the background noise at each.</p>'
                '<table><tr><th>Site</th><th>Background noise (dB)</th>'
                '<th>Minimum song frequency (Hz)</th></tr>'
                '<tr><td>Woodland</td><td>42</td><td>2,800</td></tr>'
                '<tr><td>Suburb</td><td>51</td><td>3,100</td></tr>'
                '<tr><td>Park</td><td>58</td><td>3,400</td></tr>'
                '<tr><td>Ring road</td><td>67</td><td>3,900</td></tr></table>',
     'question_text': 'A student concludes that, among these sites, birds at noisier '
                      'locations sang at a higher minimum frequency. Which choice best '
                      'describes data from the table that support this conclusion?',
     'choices': [
         'All four sites recorded a minimum song frequency above 2,500 Hz.',
         'Minimum song frequency rose with background noise across all four sites, from 2,800 Hz in woodland (42 dB) to 3,900 Hz at the ring road (67 dB).',
         'The park was 16 dB noisier than the woodland.',
         'The ring road was the noisiest of the four sites.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Minimum song frequency</strong>… Xulosa ikki '
                    'kattalikning birga oʻsishi haqida, demak dalil ham ikkalasini butun '
                    'jadval boʻylab olishi kerak. Qolgan uchtasi rost, lekin har biri '
                    'bittagina ustunda qoladi — <strong>The ring road was the '
                    'noisiest</strong>… qoʻshiq haqida hech narsa demaydi.'},

    # ── Information and Ideas: Inferences (13–14) ──────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>An ice sheet presses the crust down; when the ice melts, the crust '
                'rises again — slowly, because the mantle beneath it has to flow out '
                'of the way. Scandinavia is still rising at about a centimetre a year, ten '
                'thousand years after its ice went. The rate of that rebound therefore '
                'tells a geologist less about the ice than about ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'how much water the melting of the ice released.',
         'how stiff the mantle underneath it is.',
         'the age of the rock beneath the ice sheet.',
         'the thickness the ice sheet reached at its maximum.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>how stiff the</strong>… Matn sekinlikning '
                    'sababini oʻzi aytadi: mantiya chetga <em>oqishi</em> kerak. Demak '
                    'tezlikni belgilaydigan narsa muz emas, mantiyaning qanchalik qiyin '
                    'oqishi. <strong>the thickness the ice sheet reached</strong> tuzoq: '
                    'qalinlik <em>qancha</em> koʻtarilishini belgilaydi, <em>qanchalik '
                    'tez</em> koʻtarilishini emas.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>The pulsar map on the Voyager cover works by triangulation: each line '
                'gives the direction of one pulsar and its period, and a finder who can '
                'measure those periods can place the sun. But a pulsar’s period '
                'lengthens by a known amount every year, which means the map is also a '
                'clock — a finder could read from the periods ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'how far the probe had travelled from the sun.',
         'how long ago the probe was launched.',
         'what language the greetings on the record are in.',
         'which of the fourteen pulsars lies nearest to the sun.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>how long ago</strong>… Matn kalit faktni '
                    'beradi: davr har yili maʼlum miqdorda uzayadi. Demak topuvchi hozirgi '
                    'davrni muqovadagisi bilan solishtirib, <em>qancha vaqt oʻtganini</em> '
                    'hisoblaydi. <strong>how far the probe had travelled</strong> tuzoq: '
                    'vaqtni bilish masofani bermaydi — buning uchun tezlik ham kerak, '
                    'u esa muqovada emas.'},

    # ── Standard English Conventions: Boundaries (15–17) ───────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>Nikolai Vavilov, the botanist who assembled the world’s largest '
                'collection of crop ______ died of starvation in a Soviet prison in '
                '1943.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['seed', 'seed,', 'seed:', 'seed;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>seed,</strong>. "the botanist who…seed" — '
                    '<em>Nikolai Vavilov</em> ga izoh, vergul bilan ochilgan, demak vergul '
                    'bilan yopiladi. <strong>seed</strong> (belgisiz) izohni kesimga '
                    'yopishtirib yuboradi va gap oʻqilmay qoladi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>The mantle transmits shear ______ shear waves do not travel through a '
                'liquid.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['waves', 'waves and,', 'waves,', 'waves;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>waves;</strong>. Boʻshliqning ikki tomonida ham '
                    'toʻliq mustaqil gap turibdi, ularni nuqtali vergul ajratadi. '
                    '<strong>waves,</strong> — comma splice: ikki mustaqil gapni '
                    'yolgʻiz vergul bilan ulash ingliz tilida xato.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>The only object on the Voyager cover that a finder ______ against the '
                'sky is the map of the pulsars.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['— could check', ', could check', 'could check', 'could check,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>could check</strong> — hech qanday belgi '
                    'kerak emas. "that a finder could check against the sky" obyektni '
                    '<em>aniqlaydigan</em> ergash gap: usiz "the only object" iborasi '
                    'maʼnosiz qoladi, shuning uchun u ajratilmaydi.'},

    # ── Standard English Conventions: Form, Structure, and Sense (18–21)
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The collection of seed that Vavilov assembled from five continents '
                '______ more than two hundred thousand samples today.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are containing', 'contain', 'contains', 'have contained'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>contains</strong>. Ega — '
                    '<em>collection</em>, birlik; "of seed that Vavilov assembled from five '
                    'continents" faqat aniqlovchi. Feʼlga yaqin turgan "continents" koʻplik '
                    'boʻlgani uchun quloq <strong>contain</strong> ga tortadi.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time the siege of Leningrad was lifted in 1944, several of the '
                'collection’s keepers ______ of starvation.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['died', 'had died', 'have died', 'will have died'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>had died</strong>. "By the time…was lifted" '
                    'oʻtmishdagi nuqtani beradi, oʻlimlar esa undan <em>oldin</em> sodir '
                    'boʻlgan — past perfect. <strong>died</strong> oddiy oʻtgan zamon '
                    'ikki hodisani bir qatorga qoʻyadi va qaysi biri oldin boʻlganini '
                    'yoʻqotadi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>Neither the borders nor the main register ______ how the raid that '
                'opens the story began.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are explaining', 'explain', 'explains', 'have explained'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>explains</strong>. "Neither…nor" qurilishida '
                    'feʼl oʻziga <em>yaqin turgan</em> egaga moslashadi, "the main '
                    'register" esa birlik. <strong>explain</strong> tuzoq: ikki narsa '
                    'sanalgani uchun quloq koʻplikni kutadi, lekin "neither…nor" ularni '
                    'birlashtirmaydi.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>______ the Bayeux Tapestry shows the conquest from the side that lost '
                'it.</p>',
     'question_text': CONVENTION_Q,
     'choices': [
         'Embroidered in England for a Norman patron,',
         'Embroidering it in England for a Norman patron,',
         'Having embroidered it in England for a Norman patron,',
         'To embroider it in England for a Norman patron,',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Embroidered in England</strong>… Boshlanuvchi '
                    'ibora egani — <em>the Tapestry</em> — aniqlashi kerak, '
                    'gilam esa <em>tikilgan</em>: majhul maʼno, demak III shakl. '
                    '<strong>Embroidering it in England</strong>… aniq nisbat beradi va '
                    'gilamning oʻzi kimnidir tikayotgan boʻlib chiqadi.'},

    # ── Expression of Ideas: Transitions (22–24) ───────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>Semmelweis’s ward recorded a tenth of the deaths it had recorded '
                'before the washing began. ______ the hospital did not adopt the practice, '
                'and Semmelweis was dismissed from his post.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'For example,', 'Nonetheless,', 'Similarly,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Nonetheless,</strong>. Natija ajoyib edi, '
                    'oqibat esa kutilganning aksi — qarama-qarshilik. '
                    '<strong>Accordingly,</strong> aynan teskari bogʻlanish va eng koʻp '
                    'tanlanadigan xato: raqam talabani mantiqiy davomni kutishga undaydi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>A pulsar’s period lengthens by a known amount every year. ______ '
                'the map etched on the Voyager cover records not only where the sun is but '
                'when the probe left it.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['As a result,', 'By contrast,', 'Nevertheless,', 'Previously,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>As a result,</strong>. Davrning oʻzgarishi '
                    '— sabab, xaritaning soatga aylanishi — oʻsha sababdan kelib '
                    'chiqadigan natija. <strong>Nevertheless,</strong> qarama-qarshilik '
                    'talab qiladi, bu yerda esa ikkala jumla bir tomonga qaraydi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>The children of the second cohort learned the pidgin young and made it '
                'regular. ______ they ended up with a grammar that the older pupils who had '
                'taught it to them could not fully follow.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Even so,', 'In the process,', 'On the contrary,', 'Previously,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>In the process,</strong>. Ikkinchi jumla '
                    'birinchisiga qarshi turmaydi va yangi voqea ham qoʻshmaydi — u '
                    'oʻsha ishning <em>ichida</em> sodir boʻlgan natijani aytadi. '
                    '<strong>Even so,</strong> ziddiyat talab qiladi; aslida bu yerda '
                    'ziddiyat emas, oqibat bor.'},

    # ── Expression of Ideas: Rhetorical Synthesis (25–27) ──────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Nikolai Vavilov assembled the world’s largest crop seed '
                'collection in Leningrad.</li>'
                '<li>He was arrested in 1940 and died in prison in 1943.</li>'
                '<li>During the siege of 1941–42 his staff stayed with the '
                'collection.</li>'
                '<li>The building was unheated and the collection held edible rice and '
                'potatoes.</li>'
                '<li>Several of the staff starved; nothing was eaten.</li></ul>',
     'question_text': 'The student wants to emphasize the choice the staff made. Which '
                      'choice most effectively uses relevant information from the notes to '
                      'accomplish this goal?',
     'choices': [
         'Nikolai Vavilov assembled the world’s largest collection of crop seed in Leningrad.',
         'Several members of the collection’s staff starved during the siege of Leningrad.',
         'Through the siege winter the staff stayed in an unheated building surrounded by edible rice and potatoes; several of them starved, and nothing was eaten.',
         'Vavilov was arrested in 1940 and died in prison three years afterwards.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Through the siege winter</strong>… Tanlov '
                    'boʻlishi uchun ikki tomon ham koʻrinishi shart: yeyish mumkin edi '
                    '<em>va</em> yeyilmadi. Faqat shu variant ikkalasini yonma-yon qoʻyadi. '
                    '<strong>Several members of the collection’s staff starved</strong>… '
                    'faqat oqibatni aytadi — undan tanlov borligi koʻrinmaydi.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Nicaragua opened its first schools for deaf children in 1977.</li>'
                '<li>The pupils arrived with home signs and no language in common.</li>'
                '<li>The first cohort built a rough pidgin.</li>'
                '<li>Children arriving later learned that pidgin young.</li>'
                '<li>The later children regularised it into a grammar the first cohort '
                'could not fully follow.</li></ul>',
     'question_text': 'The student wants to explain to an audience unfamiliar with the case '
                      'what the two cohorts showed. Which choice most effectively uses '
                      'relevant information from the notes to accomplish this goal?',
     'choices': [
         'Children who arrived at the schools later learned the pidgin at a younger age.',
         'Nicaragua opened its first schools for deaf children in 1977.',
         'The first pupils built a rough pidgin from their home signs; the children who came later, learning it young, turned it into a full grammar the first cohort could not follow.',
         'The pupils arrived at the schools with home signs and no language in common.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>The first pupils built</strong>… Maqsad ikki '
                    'avlod <em>nimani koʻrsatganini</em> tushuntirish, demak javobda '
                    'ikkalasi ham va ular orasidagi farq ham boʻlishi kerak. '
                    '<strong>Children who arrived at the schools later learned the pidgin '
                    'at a younger age</strong>… faqat bitta qaydni takrorlaydi va natijani '
                    'aytmaydi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>The Voyager record carries greetings in 55 languages and 90 minutes of '
                'music.</li>'
                '<li>Its cover is etched with a hydrogen diagram and a map of 14 '
                'pulsars.</li>'
                '<li>The hydrogen diagram and the pulsar map can be checked against the '
                'sky.</li>'
                '<li>The greetings and the music cannot be decoded without knowing a human '
                'language.</li>'
                '<li>The probe will take tens of thousands of years to reach another '
                'star.</li></ul>',
     'question_text': 'The student wants to emphasize the distinction between the record’s '
                      'two audiences. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'The cover carries the two things a finder could check against the sky, while the greetings inside cannot be decoded without a human language — the outside is addressed to them, the inside to us.',
         'The probe will take tens of thousands of years to reach another star.',
         'The record’s cover is etched with a hydrogen diagram and a map of fourteen pulsars.',
         'The Voyager record carries greetings in fifty-five languages and ninety minutes of music.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>The cover carries the</strong>… Maqsad ikki '
                    'auditoriyani <em>ajratish</em>, demak javobda ikkala qism ham va '
                    'ularning kimga qaratilgani ham boʻlishi shart. Qolgan uchtasi rost, '
                    'lekin har biri faqat bir tomonni yoki umuman boshqa faktni aytadi '
                    '— bitta tomonni aytgan javob farqni koʻrsata olmaydi.'},
]
