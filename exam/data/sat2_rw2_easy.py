# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 2 · Reading and Writing, Module 2 (LOWER)
#  27 questions · 32 minutes · taken by a pupil who scored under 18 on rw1.
#
#  Same domains, same counts, same order as the upper module — one-step
#  reasoning, familiar wording, the point in the opening sentence.
#
#  Load: python manage.py load_mock exam/data/sat2_rw2_easy.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §3
# ──────────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'Digital SAT — PrimePoint Mock 2',
    'language': 'english',
    'exam_format': 'sat',
    'exam_number': 202,
    'is_published': True,
}

# Copied unchanged into all six files of mock 2.
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
     'passage': '<p>Harry Beck’s diagram of the London Underground, drawn in 1933, is '
                'not ______: the distances on it match no distance above ground. What it '
                'shows is the order of the stations and the places where the lines '
                'cross.</p>',
     'question_text': WORD_Q,
     'choices': ['colourful', 'complete', 'geographic', 'popular'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>geographic</strong>. Ikki nuqtadan keyingi qism '
                    'maʼnoni oʻzi beradi: chizmadagi masofalar yer yuzidagi masofalarga mos '
                    'kelmaydi. <strong>popular</strong> notoʻgʻri — matn '
                    'mashhurlik haqida hech narsa demaydi, va chizma aslida juda mashhur.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>When Grace Hopper suggested in the early 1950s that a computer could '
                'translate English-like instructions into machine code by itself, she was '
                'told that it could not be done. She wrote the translator anyway, and the '
                '______ was the first working compiler.</p>',
     'question_text': WORD_Q,
     'choices': ['delay', 'objection', 'result', 'rumour'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>result</strong>. "She wrote the translator '
                    'anyway, and the ______ was…" — boʻshliqqa ishning <em>natijasi</em> '
                    'keladi. <strong>objection</strong> eʼtirozni bildiradi, eʼtiroz esa '
                    'undan oldin aytilgan va u kompilyator boʻla olmaydi.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>A lichen is not one organism but two living as one: a fungus that '
                'supplies the structure and an alga that supplies the food. The arrangement '
                'is so ______ that for two hundred years botanists catalogued lichens as '
                'single species.</p>',
     'question_text': WORD_Q,
     'choices': ['fragile', 'recent', 'seamless', 'unusual'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>seamless</strong> — chok koʻrinmaydigan. '
                    'Agar ikki organizm bir butundek koʻrinmaganda, botaniklar ikki asr '
                    'davomida ularni bitta tur deb yozmagan boʻlardi. '
                    '<strong>unusual</strong> tuzoq: gʻayrioddiylik xatoga sabab emas — '
                    'aksincha, gʻalati narsa eʼtiborni tortadi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>No two faces in the terracotta army are alike. The heads were pressed '
                'from a small number of moulds and then <u>worked</u> by hand — ears, '
                'brows and mouths added or altered — until every figure had a face of '
                'its own.</p>',
     'question_text': 'As used in the text, what does the word <u>worked</u> most nearly '
                      'mean?',
     'choices': ['employed', 'exercised', 'shaped', 'strained'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>shaped</strong>. Tiredan keyingi qism nima '
                    'qilinganini sanaydi: quloq, qosh va ogʻiz qoʻshilgan yoki '
                    'oʻzgartirilgan — yaʼni shakl berilgan. <strong>employed</strong> '
                    '"work" soʻzining eng koʻp uchraydigan maʼnosiga tortadi va shuning '
                    'uchun eng kuchli tuzoq.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'easy',
     'passage': '<p>A homing pigeon released three hundred kilometres from its loft will '
                'usually find its way back. For a long time the obvious explanation was '
                'landmarks. But pigeons carried to places they have never seen, in covered '
                'baskets, still go home, and they do it on overcast days when the sun gives '
                'them nothing to steer by. Whatever the pigeon is using, it is not a memory '
                'of the route.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that pigeons navigate by the position of the sun',
         'To compare the navigation of pigeons with that of other birds',
         'To describe the ways in which homing pigeons have been used to carry messages',
         'To explain why the obvious account of pigeon homing cannot be the whole answer',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To explain why the</strong>… Matn tuzilishi '
                    'shu: ochiq izoh (belgilar) qoʻyiladi, keyin ikki dalil bilan '
                    'yiqitiladi. <strong>To argue that pigeons navigate by the position of '
                    'the sun</strong> matnga zid — bulutli kunlarda quyosh yoʻq, lekin '
                    'kaptarlar baribir uyiga qaytadi.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>Teenagers fall asleep later than children or adults do; the shift is '
                'biological, not a matter of discipline. <u>Moving a school day forward '
                'does not move a teenager’s body clock with it.</u> Districts that '
                'shifted the first bell later reported that their students slept about half '
                'an hour longer on school nights, and that attendance rose.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It defines a term that was introduced in the first sentence.',
         'It gives an example of a change that school districts have made.',
         'It raises an objection that the text does not go on to answer.',
         'It states the point that the evidence in the final sentence supports.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>It states the point</strong>… Jumla daʼvoni '
                    'qoʻyadi — dars vaqtini surish tana soatini surmaydi — va '
                    'oxirgi jumla aynan shuni tasdiqlovchi raqamlarni beradi. <strong>It '
                    'gives an example of a change</strong>… notoʻgʻri: misol keyingi '
                    'jumlada, bu yerda esa umumiy qoida.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'medium',
     'passage': '<p><b>Text 1</b><br>Meltwater on a glacier’s surface drains into '
                'shafts called moulins and reaches the bed of the ice. There it acts as a '
                'lubricant, and the glacier speeds up. Warmer summers should therefore mean '
                'faster glaciers and faster loss of ice.</p>'
                '<p><b>Text 2</b><br>That was the expectation. Measurements on several '
                'Greenland outlet glaciers show something else: when the melt is large and '
                'steady, the water cuts efficient channels beneath the ice and drains away '
                'harmlessly. It is the sudden pulse early in the season that lifts a '
                'glacier, not the total.</p>',
     'question_text': 'Based on the texts, the measurements described in Text 2 complicate '
                      'the expectation in Text 1 by suggesting that',
     'choices': [
         'glaciers in Greenland behave differently from glaciers elsewhere in the world.',
         'how quickly the meltwater arrives matters more than how much of it there is.',
         'meltwater does not in fact reach the bed of a glacier through moulins.',
         'warmer summers produce less meltwater than had previously been assumed.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>how quickly the meltwater</strong>… 2-matn '
                    'oxirgi jumlada farqni oʻzi aytadi: koʻtaradigan narsa jami miqdor '
                    'emas, mavsum boshidagi keskin oqim. <strong>meltwater does not in fact '
                    'reach the bed</strong>… notoʻgʻri: 2-matn suvning tubga yetishini '
                    'inkor qilmaydi, u faqat oqibatni boshqacha tushuntiradi.'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>Maria Sibylla Merian’s 1705 book on the insects of Surinam broke '
                'with the natural history of her day in one simple respect: she drew each '
                'insect on the plant it fed on, and every stage of its life on the same '
                'page. Other naturalists pinned a specimen and drew it on its own. Merian '
                'was recording relationships, and the page itself is her argument.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Insects were rarely studied by European naturalists before the eighteenth century.',
         'Merian travelled to Surinam in order to collect specimens unavailable in Europe.',
         'Merian’s illustrations were more accurate than those of other naturalists of her time.',
         'Merian’s way of arranging a page recorded how an insect lived, not only how it looked.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Merian’s way of arranging</strong>… Matn '
                    'farqni sahifaning <em>tuzilishida</em> koʻradi: oziq oʻsimlik bilan '
                    'birga, hamma bosqich bitta sahifada. <strong>Merian’s '
                    'illustrations were more accurate</strong>… aniqlik haqida matn hech '
                    'narsa demaydi — gap aniqlikda emas, tartibda.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>In ebru, the marbler floats pigment on thickened water and draws it '
                'into a pattern with a single horsehair, then lays a sheet of paper on the '
                'surface. The paper takes the whole design at once. Because lifting the '
                'sheet disturbs the water that held it, the pattern cannot be made again: '
                'every sheet is the only print of itself.</p>',
     'question_text': 'According to the text, why can an ebru pattern not be reproduced?',
     'choices': [
         'Each marbler mixes the thickened water to a private recipe.',
         'Lifting the paper disturbs the water that held the design.',
         'The horsehair leaves a different mark on every attempt.',
         'The pigments fade unless the sheet is lifted immediately.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Lifting the paper</strong>… Matn sababni '
                    '"Because" bilan ochiq aytadi. <strong>The horsehair leaves a different '
                    'mark on every attempt</strong> mantiqan maʼqul koʻrinadi va shuning '
                    'uchun xavfli — matn ot qilini faqat naqsh chizish vositasi '
                    'sifatida eslatadi, takrorlanmaslik sababi sifatida emas.'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A researcher hypothesizes that homing pigeons find their way using the '
                'Earth’s magnetic field rather than the landmarks below them '
                '— which would explain why a bird carried in a covered basket to '
                'country it has never seen can still set a course for home.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'researcher’s hypothesis?',
     'choices': [
         'Pigeons can be trained to recognize individual human faces.',
         'Pigeons fitted with small magnets on their heads lose their bearings on overcast days but navigate normally in sunshine.',
         'Pigeons released close to their loft return more quickly than pigeons released far from it.',
         'Pigeons released over unfamiliar country circle for several minutes before setting a course.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Pigeons fitted with small</strong>… Magnit '
                    'maydonni buzsak, yoʻnalish yoʻqoladi — lekin faqat boshqa '
                    'orientir (quyosh) boʻlmaganda. Bu aynan magnit sezgisining '
                    'ishlatilayotganini koʻrsatadi. <strong>Pigeons released close to their '
                    'loft return more quickly</strong>… masofa haqida, yoʻl topish usuli '
                    'haqida emas.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A curator argues that Merian’s Surinam plates were made as '
                'scientific records rather than as decorative prints for collectors to hang '
                'on a wall, and that the way each page is composed was a choice about '
                'evidence rather than about ornament.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'curator’s argument?',
     'choices': [
         'Merian’s book was printed in Amsterdam, then a centre of the luxury book trade.',
         'Merian’s notes name the plant each insect was found on and the month each stage was observed.',
         'Merian’s plates are larger than those in most natural history books of the period.',
         'Merian’s plates were hand-coloured and sold to wealthy collectors.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Merian’s notes name</strong>… Ilmiy '
                    'yozuvning belgisi — kuzatuv sharoitini qayd etish: qaysi '
                    'oʻsimlik, qaysi oy. <strong>Merian’s plates were hand-coloured '
                    'and sold to wealthy collectors</strong>… aksincha ishlaydi — u '
                    'bezak nashri versiyasini quvvatlaydi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>Four school districts moved their first bell later and reported how '
                'much extra sleep their students got on school nights.</p>'
                '<table><tr><th>District</th><th>First bell moved later by (min)</th>'
                '<th>Extra sleep on school nights (min)</th></tr>'
                '<tr><td>Ashford</td><td>20</td><td>8</td></tr>'
                '<tr><td>Bell Creek</td><td>40</td><td>19</td></tr>'
                '<tr><td>Carlow</td><td>60</td><td>27</td></tr>'
                '<tr><td>Denham</td><td>75</td><td>30</td></tr></table>',
     'question_text': 'A student claims that, among these districts, a larger shift in the '
                      'first bell was associated with more extra sleep. Which choice best '
                      'describes data from the table that support this claim?',
     'choices': [
         'Carlow’s students slept 27 minutes longer on school nights.',
         'Denham moved its first bell later than any of the other three districts.',
         'Every district in the table reported at least some extra sleep.',
         'Extra sleep rose steadily as the shift grew, from 8 minutes at Ashford to 30 at Denham.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Extra sleep rose</strong>… Daʼvo ikki kattalik '
                    'orasidagi bogʻliqlik haqida, shuning uchun dalil ham ikkalasini butun '
                    'jadval boʻylab birga olishi kerak. Qolgan uchtasi rost, lekin har biri '
                    'faqat bitta katakni yoki bitta ustunni gapiradi — '
                    '<strong>Denham moved its first bell later</strong>… uyqu haqida hech '
                    'narsa demaydi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>Fresh cod does not keep, but salt cod does. A fish that has been split, '
                'salted and dried loses most of its water and will last a year without ice. '
                'For the fishing ports of the North Atlantic this meant that the market for '
                'a catch was no longer the town the boat landed in, and so a boat could '
                'fish ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'closer to the shore than it had before.',
         'for a shorter season in each year.',
         'further from home than it had before.',
         'only during the coldest months of the year.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>further from home than</strong>… Agar baliq bir '
                    'yil buzilmasa va xaridor yaqin shahar boʻlishi shart boʻlmasa, qayiqni '
                    'portga tez qaytishga majbur qiladigan sabab yoʻqoladi. '
                    '<strong>closer to the shore than it had before</strong> aynan teskari '
                    'xulosa va eng koʻp tanlanadigan javob.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>A lichen grows slowly, cannot move, and takes its minerals from '
                'whatever settles on it out of the air. It has no mechanism for shedding '
                'what it has absorbed. In an industrial valley, therefore, a lichen '
                '______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'grows faster than it would in clean air.',
         'holds a record of what the air has been carrying.',
         'is replaced by species that grow on soil instead.',
         'loses its algal partner within a single season.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>holds a record of</strong>… Uch shart birga '
                    'yigʻiladi: havodan oladi, chiqarib tashlay olmaydi, sekin oʻsadi — '
                    'demak ichida yillar davomida toʻplanadi. <strong>grows faster than it '
                    'would in clean air</strong> matnda umuman aytilmagan.'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>Harry Beck, the engineering draughtsman who drew the first diagram of '
                'the London ______ was paid five guineas for the work.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['Underground', 'Underground,', 'Underground:', 'Underground;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Underground,</strong>. "the engineering '
                    'draughtsman who…Underground" — <em>Harry Beck</em> ga izoh, va u '
                    'vergul bilan ochilgan: juftlik ochilgan belgi bilan yopiladi. '
                    '<strong>Underground</strong> (belgisiz) izohni kesimga yopishtirib '
                    'yuboradi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>A lichen takes its minerals from the ______ it has no mechanism for '
                'shedding what it absorbs.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['air', 'air and,', 'air,', 'air;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>air;</strong>. Boʻshliqning ikki tomonida ham '
                    'toʻliq mustaqil gap bor, ularni nuqtali vergul ajratadi. '
                    '<strong>air,</strong> — comma splice, ingliz tilidagi eng keng '
                    'tarqalgan punktuatsiya xatosi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Because lifting the sheet disturbs the water that held the ______ an '
                'ebru pattern can never be printed twice.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['design', 'design,', 'design:', 'design;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>design,</strong>. Gap "Because…" bilan '
                    'boshlangan ergash gapdan boshlanadi, va gap boshida turgan ergash gap '
                    'asosiy gapdan vergul bilan ajratiladi. <strong>design;</strong> '
                    'notoʻgʻri: nuqtali vergul ikki <em>mustaqil</em> gap orasida turadi, '
                    '"Because…" esa mustaqil emas.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The collection of plates that Merian brought back from Surinam ______ '
                'sixty engravings.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are containing', 'contain', 'contains', 'have contained'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>contains</strong>. Ega — '
                    '<em>collection</em>, birlik; "of plates that Merian brought back from '
                    'Surinam" faqat aniqlovchi. Feʼlga yaqin turgan "plates" koʻplik '
                    'boʻlgani uchun quloq <strong>contain</strong> ga tortadi.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time Hopper’s team demonstrated the compiler, she ______ on '
                'the problem for several years.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['had been working', 'has been working', 'is working', 'will have worked'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>had been working</strong>. "By the time…'
                    'demonstrated" oʻtmishdagi nuqtani beradi, ish esa undan oldin '
                    'boshlanib oʻsha nuqtagacha davom etgan — past perfect continuous. '
                    '<strong>has been working</strong> hozirgi paytga ulaydi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>Each of the four districts reported ______ results to the state '
                'board.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['it’s', 'its', 'their', 'they’re'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>its</strong>. <em>Each</em> har doim birlik, '
                    'shuning uchun "their" mos kelmaydi. <strong>it’s</strong> = '
                    '"it is" qisqartmasi: ingliz tilida apostrof egalikni emas, tushib '
                    'qolgan harfni bildiradi.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>A homing pigeon can find its loft across unfamiliar country, in thick '
                'cloud, and ______</p>',
     'question_text': CONVENTION_Q,
     'choices': ['after dark.', 'being dark.', 'darkness falls.', 'when it is dark.'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>after dark.</strong> Qator '
                    '"across unfamiliar country, in thick cloud, and ___" — ikkitasi '
                    'ham predlogli ibora, demak uchinchisi ham shunday boʻlishi kerak '
                    '(parallelizm). <strong>when it is dark.</strong> maʼno jihatdan '
                    'toʻgʻri va aynan shuning uchun chalgʻituvchi, lekin u ergash gap — '
                    'qatorning shaklini buzadi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>Salt cod keeps for a year without ice. ______ a boat could sell its '
                'catch in a market a thousand kilometres from the port it landed in.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['As a result,', 'However,', 'Instead,', 'Similarly,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>As a result,</strong>. Baliqning buzilmasligi '
                    '— sabab, uzoq bozorda sotish — natija. '
                    '<strong>However,</strong> qarama-qarshilik talab qiladi, bu yerda esa '
                    'ikkala jumla bir tomonga qaraydi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Beck’s diagram matches no distance above ground. ______ it has '
                'been copied by transit systems on every continent.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Consequently,', 'Even so,', 'For instance,', 'Likewise,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Even so,</strong>. Chizma masofani '
                    'koʻrsatmaydi — shunga qaramay, hamma joyda nusxa koʻchirilgan: '
                    'kutilmagan burilish. <strong>Consequently,</strong> aynan teskari '
                    'bogʻlanish — u "aniq emasligi uchun nusxa koʻchirildi" degan '
                    'maʼnoni beradi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Lichens absorb minerals from the air and cannot shed them again. '
                '______ surveyors measure the metals in a lichen’s tissue to map how '
                'far a smelter’s plume has travelled.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['By contrast,', 'For this reason,', 'Nevertheless,', 'Previously,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>For this reason,</strong>. Lishaynikning xossasi '
                    '— sabab, uni oʻlchov vositasi sifatida ishlatish — oʻsha '
                    'xossadan kelib chiqadigan natija. <strong>Nevertheless,</strong> '
                    'qarama-qarshilik bildiradi, bu yerda esa hech qanday ziddiyat yoʻq.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Harry Beck drew the first diagram of the London Underground in '
                '1933.</li>'
                '<li>The diagram shows the order of the stations and where the lines '
                'meet.</li>'
                '<li>Distances on the diagram match no distance above ground.</li>'
                '<li>Beck was an engineering draughtsman, not a cartographer.</li>'
                '<li>The design has been copied by transit systems on every '
                'continent.</li></ul>',
     'question_text': 'The student wants to emphasize what Beck gave up in order to make '
                      'the map clear. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'Beck gave up geographic distance altogether, keeping only the order of the stations and the points where the lines meet.',
         'Beck’s design has since been copied by transit systems on every continent.',
         'Beck’s diagram shows the order of the stations and the places at which the lines meet.',
         'Harry Beck, an engineering draughtsman rather than a cartographer, drew the diagram in 1933.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Beck gave up</strong>… Maqsad — nimadan '
                    '<em>voz kechilganini</em> koʻrsatish, demak javobda yoʻqotilgan narsa '
                    '(masofa) ham, saqlangan narsa (tartib) ham boʻlishi kerak. '
                    '<strong>Beck’s diagram shows the order of the stations</strong>… '
                    'faqat saqlangan yarmini aytadi, voz kechilganini emas.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>A lichen takes its minerals from whatever falls on it out of the '
                'air.</li>'
                '<li>It has no way of shedding what it absorbs.</li>'
                '<li>It grows slowly and cannot move.</li>'
                '<li>Metals build up in its tissue over years.</li>'
                '<li>Surveyors measure those metals to map a smelter’s plume.</li></ul>',
     'question_text': 'The student wants to explain to an audience unfamiliar with the '
                      'method why lichens are used to monitor air. Which choice most '
                      'effectively uses relevant information from the notes to accomplish '
                      'this goal?',
     'choices': [
         'A lichen takes its minerals from whatever falls out of the air onto it.',
         'Because a lichen absorbs from the air and cannot shed what it takes in, metals build up in its tissue over years — which is why surveyors measure them to map a smelter’s plume.',
         'Lichens grow slowly and cannot move from the place where they started.',
         'Surveyors measure the metals held in the tissue of a lichen.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Because a lichen</strong>… Maqsad <em>nega</em> '
                    'shunday qilinishini tushuntirish, demak javob sababni (yutadi, '
                    'chiqarmaydi) va natijani (oʻlchash mumkin) birga bersin. '
                    '<strong>Surveyors measure the metals held</strong>… nima qilinishini '
                    'aytadi, lekin nega ishlashini emas.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Maria Sibylla Merian published a book on the insects of Surinam in '
                '1705.</li>'
                '<li>She drew each insect on the plant that it fed on.</li>'
                '<li>She drew every stage of an insect’s life on one page.</li>'
                '<li>Other naturalists pinned specimens and drew them on their own.</li>'
                '<li>Her notes record the month in which each stage was observed.</li></ul>',
     'question_text': 'The student wants to emphasize how Merian’s pages differed from '
                      'those of other naturalists. Which choice most effectively uses '
                      'relevant information from the notes to accomplish this goal?',
     'choices': [
         'Merian drew each of the insects on the plant that it fed on.',
         'Merian published her book on the insects of Surinam in 1705.',
         'Merian’s notes record the month in which she observed each stage of an insect’s life.',
         'Where other naturalists pinned a specimen and drew it alone, Merian drew every stage of an insect’s life on the plant it fed on, all on one page.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Where other naturalists</strong>… Maqsad '
                    '<em>farqni</em> koʻrsatish, demak javobda ikkala tomon ham boʻlishi '
                    'shart: boshqalar qanday qilgani va Merian qanday qilgani. '
                    '<strong>Merian drew each of the insects on the plant</strong>… faqat '
                    'bir tomonni beradi — taqqoslanadigan ikkinchi tomonsiz farq hosil '
                    'boʻlmaydi.'},
]
