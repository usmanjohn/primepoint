# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 5 · Reading and Writing, Module 1
#  27 questions · 32 minutes · every taker sits this one.
#
#  Route: 18 or more correct here sends the taker to the UPPER module 2.
#
#  Load: python manage.py load_mock exam/data/sat5_rw1.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md
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
     'passage': '<p>When the body in the Ötztal ice was found in 1991 it was taken for '
                'a modern casualty, and the axe lying beside it for a recent tool. The axe '
                'is what ______ the question: copper of that purity, hafted in that way, '
                'belongs to about 3300 BC and to nothing since.</p>',
     'question_text': WORD_Q,
     'choices': ['complicated', 'delayed', 'raised', 'settled'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>settled</strong>. Ikki nuqtadan keyingi qism '
                    'hech qanday shubha qoldirmaydi: "belongs to about 3300 BC and to '
                    'nothing since" — masala yopildi. <strong>raised</strong> aynan '
                    'teskari yoʻnalish: bolta savol tugʻdirmadi, javob berdi.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>In parts of Southeast Asia thousands of male fireflies in one stand of '
                'mangrove flash together, on and off, for hours. No individual is leading. '
                'Each insect simply nudges its own rhythm toward the flashes around it, and '
                'out of that small local rule the whole riverbank becomes ______.</p>',
     'question_text': WORD_Q,
     'choices': ['brighter', 'silent', 'still', 'synchronised'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>synchronised</strong>. Birinchi jumla natijani '
                    'allaqachon tasvirlagan — "flash together" — va oxirgi jumla '
                    'uni bitta soʻzga yigʻadi. <strong>brighter</strong> chalgʻituvchi, '
                    'chunki yorugʻlik mavzuda; lekin matnda yorqinlik emas, '
                    '<em>vaqt</em> muvofiqligi haqida gap ketyapti.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>Ashurbanipal’s library at Nineveh survives because the city was '
                'sacked and burned in 612 BC. Papyrus and parchment would have gone with '
                'it; the clay tablets were ______ by the fire, which baked them hard. The '
                'destruction of the library is the reason we can read it.</p>',
     'question_text': WORD_Q,
     'choices': ['preserved', 'scattered', 'softened', 'translated'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>preserved</strong>. Matn paradoksni ochiq '
                    'quradi: yongʻin lavhalarni pishirib qattiqlashtirgan, oxirgi jumla esa '
                    '"vayronagarchilik — oʻqiy olishimiz sababi" deydi. '
                    '<strong>softened</strong> matndagi "baked them hard" iborasiga '
                    'toʻgʻridan-toʻgʻri zid.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>The air is four-fifths nitrogen and almost no plant can use any of it: '
                'the N≡N bond is among the hardest in chemistry to break. Legumes do '
                'not break it themselves. They house bacteria that do, and the bacteria '
                '<u>fix</u> the nitrogen — turn it into a form the plant can take up '
                '— in exchange for sugar.</p>',
     'question_text': 'As used in the text, what does the word <u>fix</u> most nearly '
                      'mean?',
     'choices': ['convert', 'mend', 'secure', 'stabilise'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>convert</strong>. Taʼrif tirelar orasida '
                    'berilgan: "turn it into a form the plant can take up". '
                    '<strong>mend</strong> va <strong>secure</strong> "fix" soʻzining '
                    'kundalik maʼnolari va shuning uchun eng kuchli tuzoqlar — koʻp '
                    'maʼnoli soʻzda lugʻat emas, jumlaning oʻz izohi hal qiladi.'},

    # ── Craft and Structure: Text Structure and Purpose (5–6) ──────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>A qanat is a tunnel, dug by hand, that carries water from an aquifer '
                'under a mountain to a village on the plain, sometimes forty kilometres '
                'away, on a gradient of a metre or two per kilometre. It is the gradient '
                'that matters. Too steep and the tunnel scours itself out; too shallow and '
                'the water stops moving. The vertical shafts along the line, which from the '
                'air look like the striking feature, are spoil holes — the by-product, '
                'not the design.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that qanats are no longer used anywhere in the region',
         'To compare qanats with other systems of ancient irrigation',
         'To describe how qanats were financed by the villages that used them',
         'To explain that a qanat’s essential engineering is its gradient rather than the shafts that are most visible',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To explain that a</strong>… Matn ikkinchi '
                    'jumlada fikrini qoʻyadi ("It is the gradient that matters") va oxirgi '
                    'jumlada eng koʻrinadigan belgini ataylab pastga tushiradi. '
                    '<strong>To describe how qanats were financed</strong>… matnda pul '
                    'haqida bitta ham soʻz yoʻq.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>A dead whale that sinks to the abyssal floor brings down more carbon '
                'than the seabed beneath it would receive in two thousand years. <u>What '
                'arrives is not a meal but a habitat.</u> Scavengers strip the flesh within '
                'months; then bone-eating worms and the bacterial mats that follow them '
                'work the skeleton for decades, and a community assembles that exists '
                'nowhere else on the sea floor.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It corrects the impression left by the previous sentence and frames what the rest of the text describes.',
         'It introduces an exception to the process described after it.',
         'It offers evidence that the abyssal floor receives very little carbon.',
         'It summarizes the sequence set out in the final sentence.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>It corrects the impression</strong>… Oldingi '
                    'jumla uglerodni oziq sifatida koʻrsatadi; bu jumla "oziq emas, yashash '
                    'muhiti" deb tuzatadi, keyingisi esa oʻsha muhitning necha oʻn yil '
                    'yashashini bayon qiladi. <strong>It summarizes the sequence set out in '
                    'the final sentence</strong>… tartib teskari: xulosa dalildan oldin '
                    'kelmaydi, u uni <em>boshlaydi</em>.'},

    # ── Craft and Structure: Cross-Text Connections (7) ────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>The largest trial of a four-day week, run across some '
                'seventy British firms in 2022, reported that output held steady while sick '
                'days fell and resignations dropped by more than half. When the trial '
                'ended, almost every firm chose to keep the arrangement.</p>'
                '<p><b>Text 2</b><br>Kwame Asante reads the same report and notes what it '
                'cannot show. The firms volunteered; they were mostly small, mostly in '
                'services, and they knew they were being watched. A result drawn from '
                'employers who wanted the policy to work, he argues, measures enthusiasm at '
                'least as much as it measures hours.</p>',
     'question_text': 'Based on the texts, Asante’s reservation about the trial '
                      'concerns',
     'choices': [
         'how the firms in the sample came to be in it.',
         'the number of firms that chose to keep the arrangement afterwards.',
         'whether output was measured over a long enough period.',
         'whether sick days genuinely fell during the trial.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>how the firms in</strong>… Asante raqamlarni '
                    'rad etmaydi — u <em>kim oʻlchanganini</em> koʻrsatadi: firmalar '
                    'oʻzlari xohlab kelgan. <strong>whether sick days genuinely '
                    'fell</strong>… matn hech qayerda raqamni shubha ostiga olmaydi; '
                    'eʼtiroz natijaning oʻzida emas, uni umumlashtirishda.'},

    # ── Information and Ideas: Central Ideas and Details (8–9) ─────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>A Gothic cathedral’s walls are mostly glass, which a stone wall '
                'cannot be unless something else is carrying the load. The flying buttress '
                'is that something: a half-arch reaching from a pier outside the building '
                'to the point on the wall where the vault pushes outward, returning the '
                'push to the ground. The buttress is often read as decoration added to a '
                'finished form. It is the condition of the form.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Flying buttresses made the glass walls of Gothic cathedrals possible rather than merely ornamenting them.',
         'Gothic cathedrals contain more glass than any other kind of medieval building.',
         'Stone vaults exert their force downward rather than outward.',
         'The flying buttress was invented later than the pointed arch was.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Flying buttresses made the</strong>… Matn '
                    'oxirgi ikki jumlada oʻz fikrini qoʻyadi: kontrfors bezak emas, '
                    'shaklning <em>sharti</em>. <strong>Stone vaults exert their force '
                    'downward rather than outward</strong>… matnga zid — gumbaz aynan '
                    'yon tomonga itaradi, shuning uchun kontrfors kerak.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>The manuscripts of Timbuktu were never a single library. They were '
                'family property, kept in houses, lent between scholars and passed down, '
                'and that is why so many survived invasion, colonisation and the '
                'archive-building of two empires: there was no one building to seize. When '
                'the city was occupied in 2012 the same dispersal worked again — the '
                'manuscripts left in ordinary trunks on ordinary boats, a few hundred at a '
                'time.</p>',
     'question_text': 'According to the text, what accounts for the survival of the '
                      'manuscripts?',
     'choices': [
         'They were catalogued by the empires that ruled the city.',
         'They were copied repeatedly by scholars over several centuries.',
         'They were held in private hands rather than in one central collection.',
         'They were written on a material more durable than paper.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>They were held</strong>… Matn sababni ikki '
                    'nuqtadan keyin oʻzi aytadi: "there was no one building to seize". '
                    '<strong>They were copied repeatedly by scholars</strong>… mantiqan '
                    'maʼqul koʻrinadi va aynan shuning uchun xavfli — matn '
                    'koʻchirish haqida hech narsa demaydi, faqat qarz berish va meros '
                    'haqida.'},

    # ── Information and Ideas: Command of Evidence (10–12) ─────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A researcher proposes that the synchrony of a firefly swarm needs no '
                'leader and no signal from any central source — that it emerges from '
                'each insect nudging its own rhythm toward its immediate neighbours, which '
                'would mean synchrony should appear even in a group where no individual can '
                'see more than a few others.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'researcher’s proposal?',
     'choices': [
         'Fireflies of different species flash at measurably different rates.',
         'In a simulation in which each firefly adjusts only to the two insects nearest it, the whole swarm falls into step within minutes.',
         'Male fireflies flash more brightly when females are present.',
         'Synchrony breaks down when the mangrove is disturbed by wind.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>In a simulation in</strong>… Taklifning butun '
                    'gapi shu: <em>mahalliy</em> qoida global tartib beradi. Modelda har '
                    'bir hasharot faqat ikkita qoʻshnisini koʻradi — va butun toʻda '
                    'baribir moslashadi. <strong>Synchrony breaks down when the mangrove is '
                    'disturbed</strong>… hodisaning mavjudligini tasdiqlaydi, uning '
                    'mexanizmini emas.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>An archaeologist claims that the Iceman was not travelling casually but '
                'equipped for a long stay in high country — that the kit he carried '
                'was assembled for conditions he expected rather than picked up out of '
                'habit.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'archaeologist’s claim?',
     'choices': [
         'He carried an axe of a copper purity consistent with a date around 3300 BC.',
         'He carried two species of birch fungus, one antiseptic and one a fire-starter, and a repair kit for his bow that had not yet been used.',
         'He was found at an altitude of about 3,200 metres.',
         'His last meal included both ibex meat and einkorn wheat.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>He carried two species</strong>… Daʼvo '
                    'jihozning <em>rejalashtirilganini</em> aytadi, demak dalil '
                    'har bir buyum aniq ehtimolga tayyorlanganini koʻrsatishi kerak — '
                    'dori, olov, hali ishlatilmagan taʼmirlash toʻplami. <strong>He was '
                    'found at an altitude of about 3,200 metres</strong>… qayerda '
                    'boʻlganini aytadi, nima uchun shunday jihozlanganini emas.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>Researchers surveyed four whale falls at different stages of decay and '
                'counted the number of species present at each.</p>'
                '<table><tr><th>Site</th><th>Years since the carcass landed</th>'
                '<th>Species recorded</th></tr>'
                '<tr><td>A</td><td>1</td><td>19</td></tr>'
                '<tr><td>B</td><td>4</td><td>43</td></tr>'
                '<tr><td>C</td><td>12</td><td>78</td></tr>'
                '<tr><td>D</td><td>30</td><td>112</td></tr></table>',
     'question_text': 'A student concludes that the number of species at a whale fall rises '
                      'with the time since the carcass landed. Which choice best describes '
                      'data from the table that support this conclusion?',
     'choices': [
         'All four of the sites recorded more than fifteen species.',
         'Site C had been on the seabed for twelve years.',
         'Site D recorded 112 species, the most of the four.',
         'Species counts rose at every step, from 19 after one year at Site A to 112 after thirty years at Site D.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Species counts rose</strong>… Xulosa ikki '
                    'kattalikning birga oʻsishi haqida, demak dalil ham ikkalasini butun '
                    'jadval boʻylab olishi kerak. <strong>Site D recorded 112 species, the '
                    'most of the four</strong>… rost, lekin bitta katak: undan oʻsish '
                    'yoʻnalishi koʻrinmaydi.'},

    # ── Information and Ideas: Inferences (13–14) ──────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>A field that has grown wheat for several seasons is short of nitrogen; '
                'a field that has grown clover is not, because the bacteria in the '
                'clover’s roots have been converting nitrogen out of the air all '
                'summer. A farmer who rotates the two crops is therefore using the clover '
                'year ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'to make use of a wetter part of the season.',
         'to manufacture fertiliser in place.',
         'to rest the soil from cultivation altogether.',
         'to suppress the weeds that follow a wheat crop.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>to manufacture fertiliser</strong>… Matn '
                    'mexanizmni beradi: beda ildizidagi bakteriyalar havodagi azotni '
                    'oʻsimlik ola oladigan holga oʻtkazadi — yaʼni dala oʻzi uchun '
                    'oʻgʻit ishlab chiqaradi. <strong>to rest the soil from cultivation '
                    'altogether</strong> tuzoq: dala boʻsh turmaydi, unda ekin oʻsadi.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>A collection held in one building can be catalogued, conserved and '
                'searched. A collection held in four hundred houses cannot — but it '
                'also cannot be seized in an afternoon. The scholars now gathering the '
                'Timbuktu manuscripts into a single conserved archive are therefore '
                '______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'copying a method that has already failed elsewhere.',
         'following the practice of the empires that once ruled the city.',
         'making the manuscripts harder for researchers to consult.',
         'undoing the arrangement that kept the manuscripts alive.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>undoing the arrangement that</strong>… Matn '
                    'tarqoqlikning bahosini aniq qoʻyadi: katalog yoʻq, lekin bir kunda '
                    'olib ketib ham boʻlmaydi. Hammasini bitta arxivga yigʻish ikkinchi '
                    'xususiyatni yoʻq qiladi. <strong>making the manuscripts harder for '
                    'researchers to consult</strong> aynan teskari — arxiv izlashni '
                    'osonlashtiradi.'},

    # ── Standard English Conventions: Boundaries (15–17) ───────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>The Iceman, the body found in a glacier in the Ötztal Alps in '
                '______ was carrying a copper axe made about 3300 BC.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['1991', '1991,', '1991:', '1991;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>1991,</strong>. "the body found…1991" — '
                    '<em>The Iceman</em> ga izoh, vergul bilan ochilgan, demak vergul bilan '
                    'yopiladi. <strong>1991</strong> (belgisiz) izohni kesimga yopishtirib '
                    'yuboradi va gap oʻqilmay qoladi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Papyrus would have burned with the ______ the clay tablets were baked '
                'hard and survived.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['city', 'city and,', 'city,', 'city;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>city;</strong>. Boʻshliqning ikki tomonida ham '
                    'toʻliq mustaqil gap turibdi, ularni nuqtali vergul ajratadi. '
                    '<strong>city,</strong> — comma splice: ikki mustaqil gapni '
                    'yolgʻiz vergul bilan ulash ingliz tilida xato.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>The only feature of a qanat that the engineering actually ______ is the '
                'gradient of the tunnel.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['— depends on', ', depends on', 'depends on', 'depends on,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>depends on</strong> — hech qanday belgi '
                    'kerak emas. "that the engineering actually depends on" belgini '
                    '<em>aniqlaydigan</em> ergash gap: usiz "the only feature" iborasi '
                    'maʼnosiz qoladi, shuning uchun u ajratilmaydi.'},

    # ── Standard English Conventions: Form, Structure, and Sense (18–21)
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The network of tunnels and shafts that brings water down to a village '
                '______ maintained by families who inherit the work.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are', 'have been', 'is', 'were'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>is</strong>. Ega — <em>network</em>, '
                    'birlik; "of tunnels and shafts that brings water down to a village" '
                    'faqat aniqlovchi. Feʼlga yaqin turgan "village" bilan emas, egani '
                    'bilan moslashtiring — oraliq iborani yopib koʻring.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time the manuscripts left Timbuktu in 2012, families ______ them '
                'in their own houses for six hundred years.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['had been keeping', 'has been keeping', 'keep', 'will have kept'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>had been keeping</strong>. "By the time…left" '
                    'oʻtmishdagi nuqtani beradi, saqlash esa undan oldin boshlanib oʻsha '
                    'nuqtagacha davom etgan — past perfect continuous. <strong>has '
                    'been keeping</strong> hozirgi paytga ulaydi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>Neither the shafts nor the tunnel itself ______ the feature that makes '
                'a qanat work.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are', 'have been', 'is', 'were'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>is</strong>. "Neither…nor" qurilishida feʼl '
                    'oʻziga <em>yaqin turgan</em> egaga moslashadi, "the tunnel itself" esa '
                    'birlik. <strong>are</strong> tuzoq: ikki narsa sanalgani uchun quloq '
                    'koʻplikni kutadi, lekin "neither…nor" ularni birlashtirmaydi.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>______ the whale’s skeleton goes on supporting a community that '
                'exists nowhere else on the sea floor.</p>',
     'question_text': CONVENTION_Q,
     'choices': [
         'Having stripped it of its flesh within months,',
         'Stripped of its flesh within months,',
         'Stripping it of its flesh within months,',
         'To strip it of its flesh within months,',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Stripped of its</strong>… Boshlanuvchi ibora '
                    'egani — <em>the skeleton</em> — aniqlashi kerak, skelet esa '
                    '<em>tozalangan</em>: majhul maʼno, demak III shakl. '
                    '<strong>Stripping it of its</strong>… aniq nisbat beradi va skeletning '
                    'oʻzi kimnidir tozalayotgan boʻlib chiqadi.'},

    # ── Expression of Ideas: Transitions (22–24) ───────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>No firefly in the swarm can see more than a few of its neighbours. '
                '______ the synchrony that results is not organised by any one of them.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'By contrast,', 'For example,', 'Previously,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Accordingly,</strong>. Agar hech kim butun '
                    'toʻdani koʻrmasa, hech kim uni boshqara olmaydi — bu '
                    'toʻgʻridan-toʻgʻri natija. <strong>By contrast,</strong> ziddiyat '
                    'talab qiladi, bu yerda esa ikkinchi jumla birinchisidan kelib '
                    'chiqadi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Papyrus and parchment would not have survived the burning of Nineveh. '
                '______ the clay tablets were baked hard by the same fire.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'By contrast,', 'For instance,', 'Likewise,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>By contrast,</strong>. Bitta hodisa ikki '
                    'materialga ikki xil taʼsir qiladi: biri yoʻq boʻlardi, ikkinchisi '
                    'mustahkamlandi. <strong>Likewise,</strong> oʻxshashlik kutadi va eng '
                    'koʻp tanlanadigan xato — ikkala jumla ham yongʻin haqida, lekin '
                    'mavzuning bir xilligi munosabatning bir xilligi emas.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>The seventy firms in the trial had volunteered to take part in it. '
                '______ their result tells you what happens when an employer wants a '
                'four-day week to succeed, which is a different question from the one the '
                'headline asks.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'Even so,', 'For example,', 'Nevertheless,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Accordingly,</strong>. Namunaning qanday '
                    'yigʻilgani — sabab, xulosaning torayishi — oʻsha sababdan '
                    'kelib chiqadigan natija. <strong>Even so,</strong> va '
                    '<strong>Nevertheless,</strong> ikkalasi ham ziddiyat talab qiladi, '
                    'bu yerda esa ikkinchi jumla birinchisiga qarshi turmaydi — undan '
                    'oʻsib chiqadi.'},

    # ── Expression of Ideas: Rhetorical Synthesis (25–27) ──────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>A qanat is a hand-dug tunnel carrying water from an aquifer to a '
                'village.</li>'
                '<li>Some qanats run for as much as forty kilometres.</li>'
                '<li>The gradient is a metre or two per kilometre.</li>'
                '<li>Too steep and the tunnel scours out; too shallow and the water '
                'stops.</li>'
                '<li>The vertical shafts visible from the air are spoil holes.</li></ul>',
     'question_text': 'The student wants to emphasize what is easy to mistake about a '
                      'qanat’s design. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'A qanat is a hand-dug tunnel that carries water from an aquifer to a village.',
         'Some qanats run for as much as forty kilometres across the plain.',
         'The gradient of a qanat is a metre or two per kilometre.',
         'The shafts that are most visible from the air are only spoil holes; the engineering is the gradient, steep enough to move the water and shallow enough not to scour the tunnel out.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The shafts that are</strong>… Xato qilish '
                    'mumkin boʻlgan joyni koʻrsatish uchun ikki tomon ham kerak: '
                    'koʻzga tashlanadigan narsa <em>va</em> haqiqiy muhim narsa. Faqat shu '
                    'variant ikkalasini qarshi qoʻyadi. <strong>The gradient of a qanat is '
                    'a metre or two per kilometre</strong>… raqamni beradi, lekin '
                    'adashish xavfini koʻrsatmaydi.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>A dead whale sinking to the abyssal floor brings down a great deal of '
                'carbon.</li>'
                '<li>Scavengers strip the flesh within months.</li>'
                '<li>Bone-eating worms then work on the skeleton.</li>'
                '<li>Bacterial mats follow the worms.</li>'
                '<li>The community that forms lasts for decades.</li></ul>',
     'question_text': 'The student wants to explain the sequence to an audience unfamiliar '
                      'with it. Which choice most effectively uses relevant information '
                      'from the notes to accomplish this goal?',
     'choices': [
         'A dead whale brings a great deal of carbon down to the abyssal floor.',
         'Bacterial mats follow the bone-eating worms onto the skeleton.',
         'Scavengers strip the flesh within months; bone-eating worms then work the skeleton, bacterial mats follow them, and the community lasts for decades.',
         'The community that forms at a whale fall lasts for decades.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Scavengers strip the flesh</strong>… Maqsad '
                    '<em>ketma-ketlikni</em> tushuntirish, demak javob bosqichlarni tartib '
                    'bilan bersin. Qolgan uchtasi zanjirning bitta boʻgʻinini oladi — '
                    '<strong>Bacterial mats follow the bone-eating worms</strong> '
                    'oʻrtadan boshlaydi va tinglovchi boshini bilmaydi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>The Timbuktu manuscripts were family property kept in private '
                'houses.</li>'
                '<li>They were lent between scholars and passed down by inheritance.</li>'
                '<li>No single building held them, so none could be seized at once.</li>'
                '<li>They survived invasion, colonisation and two empires’ '
                'archive-building.</li>'
                '<li>A dispersed collection cannot be catalogued, conserved or '
                'searched.</li></ul>',
     'question_text': 'The student wants to emphasize the trade-off that the dispersal '
                      'involved. Which choice most effectively uses relevant information '
                      'from the notes to accomplish this goal?',
     'choices': [
         'A collection spread across many houses cannot be catalogued, conserved or searched.',
         'Because no single building held them, the manuscripts survived invasion, colonisation and two empires — but a collection spread across hundreds of houses cannot be catalogued, conserved or searched.',
         'The manuscripts were lent between scholars and passed down by inheritance.',
         'The Timbuktu manuscripts were family property kept in private houses.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Because no single building</strong>… '
                    'Murosa (trade-off) boʻlishi uchun ikki tomon ham koʻrinishi shart: '
                    'yutuq va uning narxi. Faqat shu variant ikkalasini bitta jumlaga '
                    'qoʻyadi. <strong>A collection spread across many houses cannot be '
                    'catalogued</strong>… faqat narxni aytadi — yutuqsiz bu murosa '
                    'emas, kamchilik boʻlib qoladi.'},
]
