# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 1 · Reading and Writing, Module 2 (LOWER)
#  27 questions · 32 minutes · taken by a pupil who scored under 18 on rw1.
#
#  This is a complete SAT module, not a gentler one: same domains, same
#  counts, same order. What changes is the disguise — one-step reasoning,
#  familiar wording, a passage whose point is in its opening sentence.
#
#  Load: python manage.py load_mock exam/data/sat1_rw2_easy.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §3
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
     'passage': '<p>Mary Anning found her first complete ichthyosaur skeleton on the '
                'Dorset coast when she was twelve years old. Over the next thirty years '
                'she found so many more that geologists who had never visited Dorset '
                'came to ______ on her for the specimens they studied.</p>',
     'question_text': WORD_Q,
     'choices': ['agree', 'insist', 'rely', 'report'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>rely</strong>. Olimlar Dorsetga bormagan, lekin '
                    'namunalarni oʻrgangan — demak ular Anningga <em>tayangan</em>: "rely on" '
                    'aynan shu maʼnoni beradi. <strong>report</strong> chalgʻituvchi, chunki '
                    'olimlar haqiqatan ham maqola yozgan; ammo "report on her" "u haqida '
                    'yozmoq" degani, namuna olmoq emas.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>A honeybee that has found flowers tells the rest of the hive where '
                'they are by dancing. The angle of the dance shows the direction and its '
                'length shows the distance, so the dance is best understood as a simple '
                '______ rather than as a celebration.</p>',
     'question_text': WORD_Q,
     'choices': ['decoration', 'message', 'rehearsal', 'warning'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>message</strong> — xabar. Raqsning ikki qismi ikki '
                    'aniq maʼlumotni (yoʻnalish va masofa) uzatadi, bu esa xabarning taʼrifi. '
                    '<strong>warning</strong> (ogohlantirish) notoʻgʻri: gul xavf emas, oziq.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>Before his orbital flight in 1962, John Glenn asked that Katherine '
                'Johnson check by hand the trajectory the electronic computer had '
                'produced. The machine was far faster, but its results were new and not '
                'yet ______; Johnson’s figures were the ones the astronauts had '
                'learned to believe.</p>',
     'question_text': WORD_Q,
     'choices': ['available', 'recorded', 'required', 'trusted'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>trusted</strong>. Nuqtali verguldan keyingi qism '
                    'maʼnoni ochadi: astronavtlar Johnsonning raqamlariga <em>ishonardi</em>, '
                    'demak mashinanikiga hali ishonch yoʻq edi. <strong>available</strong> '
                    'notoʻgʻri — mashina bor va ishlagan, natija mavjud edi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>A tardigrade that dries out does not die. It expels almost all of the '
                'water in its body and its chemistry slows until it can no longer be '
                'measured. In this state the animal is not dead but <u>suspended</u>, '
                'and a drop of water can bring it back after decades.</p>',
     'question_text': 'As used in the text, what does the word <u>suspended</u> most '
                      'nearly mean?',
     'choices': ['discarded', 'hung', 'paused', 'protected'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>paused</strong>. Matn "chemistry slows until it '
                    'can no longer be measured" va "a drop of water can bring it back" deydi — '
                    'yaʼni hayot toʻxtagan, lekin tugamagan. <strong>hung</strong> — '
                    '"suspend" soʻzining asl, jismoniy maʼnosi va shuning uchun eng kuchli '
                    'tuzoq: koʻp maʼnoli soʻzda lugʻat emas, kontekst hal qiladi.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'easy',
     'passage': '<p>When Johannes Gutenberg began printing in the 1450s, the scribes of a '
                'large European workshop might copy a few dozen books in a year. Within '
                'fifty years, presses had produced more than eight million volumes. The '
                'change was not that reading became possible — people had read for '
                'centuries. The change was that a book stopped being something a reader '
                'had to travel to.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that literacy rates rose more quickly than historians have recognized',
         'To compare the output of scribal workshops in different European cities',
         'To describe the mechanism by which Gutenberg’s press printed a page',
         'To identify what actually changed when printing spread through Europe',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To identify what actually</strong>… Matn oxirgi '
                    'ikki jumlada oʻz maqsadini aytadi: oʻzgargan narsa oʻqish emas, '
                    'kitobning <em>yetib kelishi</em>. <strong>To describe the mechanism</strong>… '
                    'notoʻgʻri: matbaa mashinasi qanday ishlashi haqida matnda bitta ham '
                    'jumla yoʻq.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>Snow that falls on Antarctica never melts; it is buried by the next '
                'year’s snow, compressed, and turned to ice. <u>Trapped inside that '
                'ice are bubbles of the air that was falling with the snow.</u> Drilling '
                'down through the sheet and measuring those bubbles gives a direct '
                'reading of the atmosphere as it was in the year that snow fell.</p>',
     'question_text': 'Which choice best describes the function of the underlined '
                      'sentence in the text as a whole?',
     'choices': [
         'It gives an example of a measurement that scientists have already taken.',
         'It identifies the feature of the ice that makes the method described afterward possible.',
         'It raises an objection that the rest of the text goes on to answer.',
         'It restates the first sentence in more technical language.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>It identifies the feature</strong>… Jumla havo '
                    'pufakchalari haqida — usul (burgʻulash va oʻlchash) aynan shu '
                    'pufakchalarga asoslanadi va u keyin tushuntiriladi. <strong>It gives an '
                    'example</strong>… notoʻgʻri: bu yerda hali hech qanday oʻlchov '
                    'oʻtkazilmagan, faqat imkoniyat aytilgan.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'medium',
     'passage': '<p><b>Text 1</b><br>A study of twelve city blocks found fewer reported '
                'thefts on streets with a community garden than on streets without one. '
                'The garden, the authors suggest, puts people outdoors at hours when the '
                'street would otherwise be empty.</p>'
                '<p><b>Text 2</b><br>Gardens are not placed at random. Neighbours who '
                'organize one are often organized already: they know each other, they '
                'attend meetings, they notice a stranger on the street. The garden may '
                'be a sign of those ties rather than their cause.</p>',
     'question_text': 'Based on the texts, the author of Text 2 would most likely '
                      'describe the explanation offered in Text 1 as',
     'choices': [
         'inaccurate, because streets with gardens do not in fact report fewer thefts.',
         'incomplete, because it treats as a cause something that may instead be a sign of ties already present.',
         'persuasive, because it accounts for the hours at which thefts are reported.',
         'unnecessary, because the difference between the two kinds of street is too small to explain.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>incomplete, because it</strong>… 2-matn raqamni '
                    'rad etmaydi — u <em>sababni</em> shubha ostiga oladi: bogʻ sabab emas, '
                    'allaqachon mavjud qoʻshnichilikning belgisi boʻlishi mumkin. '
                    '<strong>inaccurate, because streets</strong>… notoʻgʻri: 2-matn '
                    'oʻgʻriliklar sonini hech qayerda inkor qilmaydi.'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>A sourdough starter is not one organism. It is a stable community of '
                'wild yeasts and lactic acid bacteria that suit each other: the bacteria '
                'make the mixture too acidic for most competing microbes, and the yeasts '
                'live comfortably in acid that would stop other fungi. A baker who feeds '
                'a starter is feeding that arrangement.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'A sourdough starter works because two kinds of organism create conditions that suit each other.',
         'Bakers must feed a sourdough starter regularly or the yeasts in it will die.',
         'Sourdough bread is more acidic than bread made with commercial yeast.',
         'Wild yeasts grow more slowly than the yeasts sold for baking.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>A sourdough starter works</strong>… Matnning '
                    'butun tuzilishi shu: bakteriya kislota chiqaradi → raqobatchilar '
                    'oʻladi → xamirturush oʻsha kislotada bemalol yashaydi. '
                    '<strong>Bakers must feed a sourdough starter</strong>… oxirgi jumladan '
                    'olingan detal, asosiy fikr emas.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'easy',
     'passage': '<p>Frida Kahlo painted fifty-five self-portraits, roughly a third of '
                'her output. She explained the number plainly. After the bus accident '
                'that broke her spine she spent long stretches in bed, with a mirror '
                'fixed above it. “I paint myself because I am so often alone,” '
                'she said, “and because I am the subject I know best.”</p>',
     'question_text': 'According to the text, what reason does Kahlo give for the number '
                      'of self-portraits she painted?',
     'choices': [
         'Her injuries prevented her from working at a large scale.',
         'Portraits of other people sold less well than her self-portraits.',
         'She believed that self-portraiture was undervalued by other artists.',
         'She was often alone, and she considered herself the subject she knew best.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>She was often alone</strong>… Kahloning oʻz '
                    'soʻzlari matnda keltirilgan va savol aynan <em>u qanday sabab '
                    'aytgan</em>ini soʻraydi. <strong>Her injuries prevented her from '
                    'working at a large scale</strong> mantiqan maʼqul koʻrinadi — baxtsiz '
                    'hodisa matnda bor — lekin rasm oʻlchami haqida matn hech narsa demaydi.'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A researcher claims that a honeybee’s waggle dance tells other '
                'bees how far away the food is, rather than simply exciting them to go '
                'and search.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'researcher’s claim?',
     'choices': [
         'Bees that watch a longer dance fly, on average, a greater distance before they begin searching.',
         'Bees that watch no dance at all still leave the hive to forage.',
         'Bees dance more vigorously when the food they have found is richer.',
         'A hive with more foragers produces more dances each day.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Bees that watch a longer</strong>… Daʼvo '
                    'raqs <em>masofani</em> uzatishi haqida, demak dalil raqsning uzunligini '
                    'uchish masofasi bilan bogʻlashi kerak — aynan shu variant shuni qiladi. '
                    '<strong>Bees dance more vigorously</strong>… boshqa narsani (oziq '
                    'sifatini) koʻrsatadi va masofa haqida hech narsa demaydi.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>Historians have argued that Mary Anning’s contribution to '
                'geology was obscured during her own lifetime because she was not '
                'permitted to publish her findings or to join the scientific '
                'societies whose members did.</p>',
     'question_text': 'Which finding, if true, would most strongly support this argument?',
     'choices': [
         'Anning corresponded regularly with geologists about what she had found.',
         'Anning earned enough from selling fossils to support her family for many years.',
         'Anning’s fossils were displayed in museums in London and in Paris.',
         'Papers describing specimens Anning had found and prepared appeared under the names of the men who bought them.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Papers describing specimens Anning</strong>… '
                    'Argument ikki qismli: hissa <em>bor edi</em> va u <em>koʻrinmay '
                    'qoldi</em>. Faqat shu variant ikkalasini ham koʻrsatadi — topgan u, nom '
                    'esa boshqaniki. <strong>Anning’s fossils were displayed in '
                    'museums</strong>… aksincha, uning ishi koʻrinib turganini bildiradi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>Researchers rehydrated groups of tardigrades that had been kept dry '
                'for different lengths of time and recorded the percentage of each group '
                'that revived.</p>'
                '<table><tr><th>Time kept dry</th><th>Revived (%)</th></tr>'
                '<tr><td>1 month</td><td>96</td></tr>'
                '<tr><td>1 year</td><td>84</td></tr>'
                '<tr><td>5 years</td><td>61</td></tr>'
                '<tr><td>10 years</td><td>38</td></tr></table>',
     'question_text': 'A student claims that a tardigrade’s chance of reviving falls '
                      'as the time it has spent dried out increases. Which choice best '
                      'describes data from the table that support this claim?',
     'choices': [
         'Fewer than half of the tardigrades kept dry for 10 years revived.',
         'Some tardigrades revived after every length of time that was tested.',
         'The longest period of drying that was tested was 10 years.',
         'The share that revived fell steadily, from 96% after 1 month to 38% after 10 years.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The share that revived</strong>… Daʼvo '
                    '<em>tendensiya</em> haqida, shuning uchun dalil ham butun jadval '
                    'boʻylab pasayishni koʻrsatishi kerak. Qolgan uchtasi jadvalga koʻra '
                    'rost, lekin bittagina qatorni yoki faqat tajriba shartini gapiradi — '
                    '<strong>Fewer than half of the tardigrades</strong> pasayish borligini '
                    'isbotlamaydi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>A printer in the 1470s set type by hand, letter by letter, and a '
                'single page could take hours to compose. Once the page was set, however, '
                'the press could pull a fresh sheet every few seconds. The economics of '
                'early printing therefore favoured ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'books containing more illustrations than text.',
         'long print runs of a small number of titles.',
         'printing many different titles in small quantities.',
         'workshops that employed fewer trained compositors.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>long print runs of</strong>… Qimmat qism — '
                    'terish, arzon qism — bosish. Qimmat ishni bir marta qilib, arzon ishni '
                    'koʻp takrorlash foydali, yaʼni kam nomdagi kitobni koʻp nusxada bosish. '
                    '<strong>printing many different titles in small quantities</strong> — '
                    'aynan teskari xulosa va eng koʻp tanlanadigan javob.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>Ice near the top of the Antarctic sheet is young; ice at the bottom, '
                'pressed by everything above it, is very old. But the deepest ice has '
                'also been thinned and folded by that weight and by the slow movement of '
                'the sheet, so its layers are no longer neatly stacked. A core drilled '
                'all the way to the bedrock therefore ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'contains no air bubbles at its lowest depths.',
         'gives a less reliable year-by-year record at its lowest depths.',
         'must be drilled more quickly than a shorter core.',
         'records a shorter span of time than a shallower core does.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>gives a less reliable</strong>… Yillik yozuv '
                    'qatlamlarning tartibli turishiga asoslanadi; matn eng chuqur muzda '
                    'qatlamlar buzilganini aytadi, demak oʻsha chuqurlikda yozuv ishonchsiz. '
                    '<strong>contains no air bubbles at its lowest depths</strong> notoʻgʻri: '
                    'pufakchalar yoʻqolgani emas, qatlamlar aralashgani aytilgan.'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>Anning’s discoveries included the first complete ichthyosaur '
                'skeleton known to ______ two complete plesiosaurs, and the first '
                'pterosaur found outside Germany.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['science', 'science,', 'science:', 'science;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>science,</strong>. Gapda uch aʼzoli sanash bor '
                    'va qolgan aʼzolar allaqachon vergul bilan ajratilgan, demak birinchisidan '
                    'keyin ham vergul kerak. <strong>science;</strong> notoʻgʻri: nuqtali '
                    'vergul sanashda faqat aʼzolarning oʻzida vergul boʻlganda ishlatiladi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Cryptobiosis, the state in which a tardigrade expels almost all of '
                'the water in its ______ can last for decades without harming the '
                'animal.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['body', 'body,', 'body;', 'body:'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>body,</strong>. "the state in which…body" — bu '
                    '<em>Cryptobiosis</em> ga izoh va u vergul bilan ochilgan, demak vergul '
                    'bilan yopiladi. Juftlik qoidasi: ochilgan belgi bilan yopiladi. '
                    '<strong>body</strong> (belgisiz) izohni gapga yopishtirib yuboradi va ega '
                    'bilan kesim orasini buzadi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Karl von Frisch published his account of the waggle dance in ______ '
                'it was years before other researchers accepted that the dance carried '
                'information at all.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['1946 and,', '1946', '1946,', '1946;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>1946;</strong>. Boʻshliqning ikki tomonida ham '
                    'toʻliq mustaqil gap turibdi, ularni nuqtali vergul ajratadi. '
                    '<strong>1946,</strong> — comma splice: ikki mustaqil gapni yolgʻiz '
                    'vergul bilan ulash ingliz tilida xato, va bu SAT ning eng sevimli '
                    'tuzogʻi.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The community of wild yeasts and bacteria in a sourdough starter '
                '______ remarkably stable once it has formed.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are remaining', 'have remained', 'remain', 'remains'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>remains</strong>. Ega — <em>community</em>, '
                    'birlik; "of wild yeasts and bacteria" faqat aniqlovchi. Feʼlga eng yaqin '
                    'turgan soʻz koʻplik ("bacteria") boʻlgani uchun quloq '
                    '<strong>remain</strong> ga tortadi — tanlashdan oldin oraliq iborani '
                    'yoping.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time von Frisch received the Nobel Prize in 1973, he ______ '
                'the behaviour of bees for more than fifty years.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['had been studying', 'has been studying', 'studies', 'will have studied'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>had been studying</strong>. "By the time…received" '
                    'oʻtmishdagi nuqta beradi, ish esa undan oldin boshlanib davom etgan — '
                    'past perfect continuous. <strong>has been studying</strong> hozirgi '
                    'paytga ulaydi, gap esa 1973-yilda tugagan.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>The three ______ lids were sealed with tape so that the ice cores '
                'inside would stay frozen during the flight north.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['containers', 'containers’', 'container’s', 'containers’s'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>containers’</strong>. Idishlar uchta '
                    '("The three"), qopqoqlar ularniki — koʻplikdagi egalik <em>-s</em> dan '
                    'keyin faqat apostrof qoʻyiladi. <strong>container’s</strong> birlik '
                    'egalik boʻlib, "three" bilan ziddiyatga kiradi.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>Anning collected the fossils, cleaned them, identified them, and '
                '______ to the scientists who bought them.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['a description of them', 'described them', 'describing them', 'she described them'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>described them</strong>. Qator '
                    '"collected…cleaned…identified…" — hammasi oddiy oʻtgan zamon feʼli, '
                    'demak toʻrtinchisi ham shunday boʻlishi shart. <strong>describing '
                    'them</strong> maʼnoni buzmaydi va aynan shuning uchun xavfli, ammo u '
                    'qatorning shaklini sindiradi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>A tardigrade in cryptobiosis uses almost no energy at all. ______ it '
                'can wait out conditions that would kill an active animal within '
                'minutes.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['As a result,', 'For example,', 'However,', 'In contrast,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>As a result,</strong>. Energiya sarflamaslik — '
                    'sabab, uzoq chidash — natija. <strong>For example,</strong> tuzoq: '
                    'ikkinchi jumla birinchisining misoli emas, oqibati; misol boʻlsa, u '
                    'energiya sarfiga <em>namuna</em> berishi kerak edi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Gutenberg’s press spread across Europe within a single '
                'generation. ______ the technology reached the Ottoman Empire much '
                'later, and printing in Arabic script did not become common there until '
                'the eighteenth century.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['However,', 'In other words,', 'Similarly,', 'Therefore,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>However,</strong>. Bir avlodda tarqalish va ancha '
                    'kech yetib borish — qarama-qarshilik. <strong>Similarly,</strong> eng '
                    'koʻp tanlanadigan xato: ikkala jumla ham matbaa haqida boʻlgani uchun '
                    '"oʻxshash" tuyuladi, lekin mavzuning bir xilligi munosabatning bir '
                    'xilligi emas.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Johnson’s hand calculations and the computer’s output '
                'agreed to the decimal place. ______ Glenn flew the mission exactly as it '
                'had been planned.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'By contrast,', 'For instance,', 'Nevertheless,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Accordingly,</strong>. Ikki hisob mos tushdi — '
                    'shuning uchun parvoz rejadagidek oʻtdi: sabab va natija. '
                    '<strong>Nevertheless,</strong> qarama-qarshilik bildiradi, bu yerda esa '
                    'hech qanday kutilmagan burilish yoʻq.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Mary Anning was born in Lyme Regis, Dorset, in 1799.</li>'
                '<li>At twelve she found the first complete ichthyosaur skeleton known '
                'to science.</li>'
                '<li>She later found the first two complete plesiosaur skeletons.</li>'
                '<li>She found the first pterosaur skeleton discovered outside '
                'Germany.</li>'
                '<li>She was never permitted to join the Geological Society of '
                'London.</li></ul>',
     'question_text': 'The student wants to emphasize the scale of Anning’s '
                      'discoveries. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'Anning found the first complete ichthyosaur known to science, the first two complete plesiosaurs, and the first pterosaur found outside Germany.',
         'Anning made her finds along the stretch of coast near the town where she was born.',
         'Anning was never permitted to join the Geological Society of London.',
         'Mary Anning was born in Lyme Regis, Dorset, in 1799, and made her first major find at the age of twelve.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Anning found the first</strong>… Maqsad — '
                    'kashfiyotlarning <em>koʻlamini</em> taʼkidlash, demak javob ularni birga '
                    'sanashi kerak. <strong>Anning was never permitted to join</strong>… rost '
                    'va kuchli jumla, lekin u toʻsiq haqida — berilgan maqsad esa boshqa. '
                    'Sintez savolida maqsad hal qiladi.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Tardigrades are animals less than a millimetre long.</li>'
                '<li>In dry conditions they enter a state called cryptobiosis.</li>'
                '<li>In cryptobiosis they expel almost all of their water.</li>'
                '<li>Their metabolism becomes almost undetectable.</li>'
                '<li>When water returns, they revive.</li></ul>',
     'question_text': 'The student wants to explain what cryptobiosis is to an audience '
                      'unfamiliar with it. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'Cryptobiosis is a state that tardigrades enter when conditions become dry.',
         'In cryptobiosis a tardigrade expels almost all of its water and its metabolism becomes almost undetectable, until water returns and the animal revives.',
         'Tardigrades are animals less than a millimetre long that can survive being dried out.',
         'Tardigrades can survive conditions that would kill almost any other animal.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>In cryptobiosis a tardigrade</strong>… Maqsad — '
                    'holatning <em>nima ekanini</em> tushuntirish, demak javob uning ichida '
                    'nima sodir boʻlishini aytsin. <strong>Cryptobiosis is a state '
                    'that</strong>… faqat nom beradi: tinglovchi baribir nima boʻlishini '
                    'bilmaydi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>A sourdough starter contains wild yeasts and lactic acid '
                'bacteria.</li>'
                '<li>The bacteria produce acid.</li>'
                '<li>Most competing microbes cannot grow in that acid.</li>'
                '<li>The wild yeasts tolerate the acid easily.</li>'
                '<li>The two groups stay stable together for years.</li></ul>',
     'question_text': 'The student wants to emphasize the relationship between the two '
                      'kinds of organism. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'A sourdough starter contains both wild yeasts and lactic acid bacteria.',
         'Lactic acid bacteria are found in a sourdough starter alongside wild yeasts.',
         'Sourdough starters can stay stable for years at a time.',
         'The bacteria produce an acid that keeps competitors out and that the yeasts tolerate easily, so the two groups stay stable together for years.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The bacteria produce an</strong>… Maqsad — ikki '
                    'organism <em>orasidagi munosabatni</em> koʻrsatish, demak javob bittasi '
                    'ikkinchisiga nima berishini aytsin. <strong>A sourdough starter contains '
                    'both</strong>… ikkalasini sanaydi, lekin ular orasida hech qanday '
                    'bogʻliqlik yoʻq — birga turish munosabat emas.'},
]
