# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 4 · Reading and Writing, Module 2 (UPPER)
#  27 questions · 32 minutes · taken by a pupil who scored 18+ on rw1.
#
#  Same domains, same counts, same order as the lower module. What changes
#  is the disguise: two-step reasoning, longer syntax, harder vocabulary.
#
#  Load: python manage.py load_mock exam/data/sat4_rw2_hard.py --expect-questions=27
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

S = 'rw2h'

WORD_Q = ('Which choice completes the text with the most logical and precise '
          'word or phrase?')
TRANSITION_Q = ('Which choice completes the text with the most logical '
                'transition?')
CONVENTION_Q = ('Which choice completes the text so that it conforms to the '
                'conventions of Standard English?')

QUESTIONS = [

    # ── Words in Context (1–4) ─────────────────────────────────────────
    {'section': S, 'number': 1, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>Ramanujan sent G. H. Hardy a letter in 1913 containing some hundred and '
                'twenty theorems, most of them stated without proof. Hardy’s first '
                'reaction was that the letter must be a hoax; his second was that nobody '
                'would have the ______ to invent such things, since a forger clever enough '
                'to produce them would have produced them under his own name.</p>',
     'question_text': WORD_Q,
     'choices': ['imagination', 'patience', 'resources', 'training'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>imagination</strong>. Hardyning ikkinchi '
                    'fikri "since" bilan izohlanadi: bunday natijalarni <em>oʻylab '
                    'topa</em> oladigan odam ularni oʻz nomidan chiqargan boʻlardi — '
                    'gap qobiliyat haqida. <strong>patience</strong> chalgʻituvchi, chunki '
                    'yuz yigirma teorema mehnat talab qiladi; lekin soxtakorni '
                    'toʻxtatadigan narsa mehnat emas, ijod.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>For centuries the Justinianic plague was known only from Procopius and '
                'a handful of chronicles, and historians argued about whether the death '
                'toll had been ______ by writers who had every reason to make a catastrophe '
                'of it. In 2013 the question moved: <i>Yersinia pestis</i> DNA was '
                'recovered from sixth-century teeth in a Bavarian graveyard.</p>',
     'question_text': WORD_Q,
     'choices': ['concealed', 'exaggerated', 'overlooked', 'recorded'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>exaggerated</strong>. Izoh boʻshliqdan keyin '
                    'darhol keladi: yozuvchilarning falokatni kattalashtirishga sababi bor '
                    'edi. <strong>concealed</strong> aynan teskari yoʻnalish — '
                    'yashirish emas, boʻrttirish.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>A superconductor does not merely carry current without resistance; it '
                'expels the magnetic field from its interior altogether. That second '
                'property is not a ______ of the first — a hypothetical perfect '
                'conductor would trap whatever field was present when it cooled, rather '
                'than push it out.</p>',
     'question_text': WORD_Q,
     'choices': ['cause', 'consequence', 'measure', 'substitute'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>consequence</strong>. Tiredan keyingi qism '
                    'dalilni beradi: qarshiliksiz oʻtkazgichning oʻzi maydonni chiqarib '
                    'tashlamaydi — demak ikkinchi xossa birinchisidan '
                    '<em>kelib chiqmaydi</em>. <strong>cause</strong> yoʻnalishni teskari '
                    'qoʻyadi va shuning uchun eng koʻp tanlanadi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>A literary canon is usually described as a list, which makes it sound '
                'settled. It behaves more like a <u>current</u>: works drift in as they '
                'come to be taught and drift out as they stop being taught, and the drift '
                'is slow enough that from inside any one decade the thing looks fixed.</p>',
     'question_text': 'As used in the text, what does the word <u>current</u> most nearly '
                      'mean?',
     'choices': ['fashion', 'flow', 'opinion', 'standard'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>flow</strong>. Ikki nuqtadan keyin ikki marta '
                    '"drift" soʻzi keladi — asarlar oqim bilan kelib, oqim bilan '
                    'ketadi. <strong>fashion</strong> eng kuchli tuzoq, chunki "current" '
                    'sifat sifatida "hozirgi, zamonaviy" maʼnosini beradi; bu yerda esa u '
                    'ot va harakatni bildiradi.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>Aphra Behn spent 1666 as a spy in Antwerp, was never paid for it, and '
                'came home to debt. What she did next is the fact that matters: she wrote '
                'for the commercial stage, and she was paid for it — nineteen plays, a '
                'novel, translations. Virginia Woolf wrote that all women should let '
                'flowers fall on Behn’s grave, because it was she who “earned '
                'them the right to speak their minds.” The right Woolf names is not '
                'the right to write. It is the right to be paid for writing.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that Woolf misunderstood the nature of Behn’s achievement',
         'To compare Behn’s plays with those of her male contemporaries',
         'To describe Behn’s employment as a spy in Antwerp in 1666',
         'To explain why Behn’s significance lies in having earned a living by writing rather than simply in having written',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To explain why Behn’s</strong>… Matn '
                    'oxirgi ikki jumlada farqni ochiq qoʻyadi: yozish huquqi emas, '
                    '<em>yozgani uchun haq olish</em> huquqi. <strong>To argue that Woolf '
                    'misunderstood</strong>… notoʻgʻri: matn Wulfni tuzatmaydi, uning '
                    'jumlasini oʻqib beradi.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>Joseph Weizenbaum wrote ELIZA in 1966 to demonstrate how little was '
                'needed to produce the appearance of understanding: the program matched '
                'patterns in a sentence and turned them round. <u>What unsettled him was '
                'not the program but his secretary.</u> She had watched him build it, knew '
                'exactly what it did, and still asked him to leave the room so that she '
                'could talk to it in private.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It concedes a technical limitation of the program described before it.',
         'It introduces the observation that the rest of the text uses to redirect the point of the demonstration.',
         'It offers evidence that the program understood more than Weizenbaum had expected.',
         'It restates the description of the program in non-technical language.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>It introduces the observation</strong>… Jumla '
                    'eʼtiborni dasturdan <em>odamga</em> burib yuboradi, keyingi jumla esa '
                    'aynan kotibaning xatti-harakatini bayon qiladi — va namoyishning '
                    'maʼnosi shu bilan oʻzgaradi. <strong>It offers evidence that the '
                    'program understood more</strong>… matnga zid: dastur faqat naqsh '
                    'moslaydi.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>The textbook prediction is straightforward: raise the '
                'price of labour and employers will buy less of it. Card and Krueger’s '
                '1994 study of fast-food restaurants on either side of the '
                'New Jersey–Pennsylvania border found no such effect, and a generation '
                'of similar studies has mostly agreed with them.</p>'
                '<p><b>Text 2</b><br>Halyna Petrenko takes the empirical result seriously '
                'and takes the theory seriously too. A minimum wage that binds in a '
                'competitive market must cost jobs; a minimum wage that binds in a market '
                'where employers have wage-setting power need not, and may raise '
                'employment. The finding does not refute the theory, she argues. It tells '
                'you which market you are in.</p>',
     'question_text': 'Based on the texts, Petrenko’s treatment of the Card and '
                      'Krueger result differs from the textbook account in that she',
     'choices': [
         'argues that a minimum wage always raises employment.',
         'disputes the accuracy of the employment figures the study used.',
         'holds that the border comparison was not a valid method.',
         'reads the result as evidence about the structure of the labour market rather than as a refutation of theory.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>reads the result as</strong>… Petrenko ikkala '
                    'tomonni ham qabul qiladi va natijani tashxis sifatida oʻqiydi: bozor '
                    'qanday tuzilgan. <strong>argues that a minimum wage always raises '
                    'employment</strong>… matnga zid — u raqobatli bozorda ish '
                    'oʻrni <em>yoʻqoladi</em> deb aniq aytadi.'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>For the Paris Exposition of 1900, W. E. B. Du Bois and his students '
                'prepared sixty hand-drawn charts of Black American life: income, literacy, '
                'property, occupation. The graphic invention is startling — spirals, '
                'stacked areas, a long falling line for the slave trade — but the '
                'invention is not the point. The charts were made for a hall in which other '
                'exhibits argued, with skulls and measurements, that the people in Du '
                'Bois’s data were a lesser kind. He answered a pseudoscience in its '
                'own register.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Du Bois invented several chart forms that had not been used anywhere before 1900.',
         'Du Bois’s charts were made as a rebuttal delivered in the visual language of the science they opposed.',
         'Du Bois’s students carried out most of the drafting work on the charts.',
         'The Paris Exposition of 1900 was the first to include statistical exhibits.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Du Bois’s charts were</strong>… Matn '
                    '"the invention is not the point" deb ixtironi ataylab chetga suradi va '
                    'oxirgi jumlada maqsadni aytadi: soxta ilmga uning oʻz tilida javob. '
                    '<strong>Du Bois invented several chart forms</strong>… matn aynan '
                    'shuni asosiy fikr <em>emas</em> deb belgilaydi.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>The Bavarian teeth settled one question and opened another. They '
                'establish that <i>Yersinia pestis</i> was present in sixth-century Europe, '
                'which the textual sceptics had doubted. They say nothing at all about how '
                'many people it killed — a genome from one graveyard is evidence of '
                'presence, not of scale — and the estimates of mortality still rest on '
                'the same handful of chroniclers they always did.</p>',
     'question_text': 'According to the text, what do the Bavarian teeth <i>not</i> '
                      'establish?',
     'choices': [
         'How many people the plague killed.',
         'How widely the plague spread beyond Bavaria.',
         'Whether the chroniclers had read one another’s work.',
         'Whether <i>Yersinia pestis</i> was present in sixth-century Europe.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>How many people the</strong>… Matn buni ochiq '
                    'aytadi: "They say nothing at all about how many people it killed". '
                    '<strong>Whether <i>Yersinia pestis</i> was present in sixth-century '
                    'Europe</strong>… aynan tishlar <em>hal qilgan</em> savol — savol '
                    '"nimani hal qilmaydi" deb soʻraladi, shuning uchun uni oxirigacha '
                    'oʻqing.'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A physicist claims that the expulsion of a magnetic field from a '
                'superconductor is a distinct property and not a consequence of zero '
                'resistance — which would mean the field is pushed out even when the '
                'material is cooled through its transition while it is already sitting in a '
                'field.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'physicist’s claim?',
     'choices': [
         'A sample cooled below its transition temperature while inside a magnetic field expels that field as it crosses the transition.',
         'A superconducting ring carries a current with no measurable loss for years.',
         'Some materials become superconducting only under very high pressure.',
         'The transition temperature falls as the applied magnetic field is increased.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>A sample cooled below</strong>… Daʼvoning '
                    'sinov holati matnda aynan koʻrsatilgan: maydon <em>ichida</em> '
                    'sovutilganda ham chiqarib tashlansa, bu qarshiliksizlikdan kelib '
                    'chiqmaydi — ideal oʻtkazgich maydonni ushlab qolardi. '
                    '<strong>A superconducting ring carries a current with no measurable '
                    'loss</strong>… faqat nol qarshilikni tasdiqlaydi, ikkinchi xossani '
                    'emas.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A curator argues that the Paris charts were designed for one particular '
                'room rather than for a general readership — that their scale, their '
                'colour and their abstraction are answers to the exhibits they were hung '
                'among.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'curator’s argument?',
     'choices': [
         'Du Bois published some of the same data in written form the following year.',
         'The charts are lettered large enough to read at a distance, and several invert the colour conventions used by the anthropometric displays in the same hall.',
         'The charts were drawn in ink and gouache on board by Du Bois’s students.',
         'The Paris Exposition attracted some fifty million visitors.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>The charts are lettered</strong>… Argument '
                    'shakl <em>qoʻshnilariga</em> javob deydi, demak dalil ikkala tomonni '
                    'bogʻlashi kerak: xonaga moʻljallangan oʻlcham va oʻsha stendlarning '
                    'rang tizimiga qarama-qarshilik. <strong>Du Bois published some of the '
                    'same data in written form</strong>… aksincha ishlaydi — u '
                    'maʼlumotning xonadan tashqarida ham yashaganini koʻrsatadi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>Four states raised their minimum wage in the same year. The table shows '
                'the size of each rise and the change in teenage employment over the '
                'following twelve months.</p>'
                '<table><tr><th>State</th><th>Rise in minimum wage (%)</th>'
                '<th>Change in teenage employment (%)</th></tr>'
                '<tr><td>A</td><td>4</td><td>+0.6</td></tr>'
                '<tr><td>B</td><td>9</td><td>+0.2</td></tr>'
                '<tr><td>C</td><td>15</td><td>−0.3</td></tr>'
                '<tr><td>D</td><td>22</td><td>−1.4</td></tr></table>',
     'question_text': 'A student concludes that larger rises were associated with worse '
                      'employment outcomes. Which choice best describes data from the table '
                      'that support this conclusion?',
     'choices': [
         'State A had the smallest rise in its minimum wage of the four.',
         'State D’s teenage employment fell by 1.4%.',
         'Teenage employment moved from +0.6% to −1.4% as the rise grew from 4% to 22%, falling at every step.',
         'Two of the four states saw teenage employment fall.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Teenage employment moved</strong>… Xulosa ikki '
                    'kattalikning birga harakatlanishi haqida, demak dalil ham ikkalasini '
                    'butun jadval boʻylab kuzatishi kerak. <strong>Two of the four states '
                    'saw teenage employment fall</strong>… rost, lekin qaysi ikkitasi '
                    'ekani aytilmagan — undan bogʻliqlik chiqmaydi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>A work enters the canon by being taught, and it comes to be taught '
                'partly because it is in the canon. The loop is not vicious — new '
                'works do get in — but it is slow, and it means that the strongest '
                'evidence that a work has entered is not a critic’s verdict but '
                '______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'its appearance on a second generation of syllabuses.',
         'the length of time that has passed since it was written.',
         'the number of copies that it has sold.',
         'the prizes it was awarded when it first appeared.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>its appearance on a</strong>… Matn kanonni '
                    'oʻqitish orqali taʼriflaydi va halqaning sekinligini taʼkidlaydi — '
                    'demak dalil oʻqitishning <em>takrorlanishi</em> boʻladi. '
                    '<strong>the number of copies that it has sold</strong> tuzoq: sotuv '
                    'mashhurlikni oʻlchaydi, matndagi taʼrif esa dastur haqida.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>Weizenbaum’s secretary knew that the program matched patterns and '
                'turned them round; she asked for privacy anyway. What the episode suggests '
                'is that the impression of being understood does not depend on any belief '
                'that one is being understood — which means a system’s designers '
                'cannot dispel the effect by ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'explaining to users how the system works.',
         'making the system’s responses longer.',
         'restricting who is allowed to use the system.',
         'training the system on a larger set of conversations.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>explaining to users</strong>… Kotiba '
                    '<em>bilardi</em> va baribir shunday his qildi, demak bilim taassurotni '
                    'yoʻq qilmaydi — tushuntirish ham. Qolgan uchtasi matnda '
                    'muhokama qilinmagan; ularning hech biri "bilish" masalasiga '
                    'tegmaydi.'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Du Bois’s charts — sixty of them, drawn in ink and gouache by '
                'his ______ were hung in a hall full of anthropometric exhibits.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['students', 'students —', 'students,', 'students;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>students —</strong>. Qoʻshimcha izoh tire '
                    'bilan <em>ochilgan</em>, demak tire bilan yopiladi: juftlik bir xil '
                    'belgilardan tuziladi. <strong>students,</strong> eng koʻp '
                    'tanlanadigan xato — vergul va tire juftlik hosil qilmaydi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>Behn produced work in three ______ nineteen plays, several of them '
                'hits; a novel; and translations from the French.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['forms', 'forms,', 'forms:', 'forms;'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>forms:</strong>. Ikki nuqta toʻliq gapdan keyin '
                    'sanashni kiritadi — va bu yerda ayniqsa zarur, chunki sanash '
                    'aʼzolarining ichida allaqachon vergul bor, shuning uchun aʼzolar '
                    'nuqtali vergul bilan ajratilgan. <strong>forms,</strong> sanashni '
                    'oldingi vergullar bilan aralashtirib yuboradi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>In 2013 researchers sequenced <i>Yersinia pestis</i> from sixth-century '
                '______ which settled a question the texts alone never could.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['teeth', 'teeth,', 'teeth:', 'teeth;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>teeth,</strong>. "which settled a question…" '
                    '— ajratilgan (qoʻshimcha) aniqlovchi ergash gap: u tishlarning '
                    'qaysi biri ekanini toraytirmaydi, faqat izoh beradi, shuning uchun '
                    'vergul bilan ajratiladi. <strong>teeth;</strong> notoʻgʻri: "which…" '
                    'mustaqil gap emas.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Among the sixty charts Du Bois brought to Paris ______ one that plots '
                'the whole Atlantic slave trade as a single falling line.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are', 'have been', 'is', 'were'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>is</strong>. Gap teskari tartibda: ega feʼldan '
                    'keyin keladi va u — <em>one</em>, birlik. Boshdagi "Among the '
                    'sixty charts…Paris" faqat oʻrin holi. <strong>are</strong> eng koʻp '
                    'tanlanadigan xato: quloq yaqin turgan "charts" ga moslashadi, lekin u '
                    'ega emas.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Hardy’s condition was that Ramanujan ______ to Cambridge before '
                'any of the theorems were published.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['came', 'come', 'comes', 'is coming'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>come</strong>. Talab bildiruvchi otdan keyin '
                    '("the condition was that…") ingliz tilida buyruq-istak shakli keladi: '
                    'feʼl asos shaklida turadi, shaxs va sondan qatʼi nazar. '
                    '<strong>came</strong> quloqqa toʻgʻriroq eshitiladi va aynan shuning '
                    'uchun eng koʻp tanlanadi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>The mortality estimates for the sixth century rest on thinner evidence '
                'than ______ for the fourteenth.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['that', 'these', 'them', 'those'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>those</strong>. Taqqoslanayotgan narsa — '
                    '<em>estimates</em>, koʻplik, demak uning oʻrnini koʻplik olmosh '
                    'bosadi. <strong>that</strong> birlikni bildiradi; '
                    '<strong>these</strong> esa yaqindagi narsaga ishora qiladi, uzoqdagi '
                    'taqqoslanuvchiga emas.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Petrenko’s argument is that the finding tells you not that the '
                'theory is wrong but ______</p>',
     'question_text': CONVENTION_Q,
     'choices': ['a different market.', 'about being in a different market.',
                 'being in a different market.', 'that you are in a different market.'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>that you are</strong>… "not that…but ___" '
                    'qurilishida ikkala tomon ham bir xil shaklda boʻlishi kerak, birinchi '
                    'tomoni esa <em>that</em> bilan boshlangan ergash gap. '
                    '<strong>being in a different market.</strong> maʼnoni saqlaydi va '
                    'aynan shuning uchun xavfli, lekin u qurilishning muvozanatini '
                    'buzadi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>A perfect conductor would trap whatever magnetic field happened to be '
                'present when it cooled. ______ a superconductor pushes the field out of '
                'itself entirely.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'By contrast,', 'For example,', 'In short,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>By contrast,</strong>. Ikki material ikki xil '
                    'ish qiladi: biri ushlab qoladi, ikkinchisi chiqarib tashlaydi. '
                    '<strong>Accordingly,</strong> ikkinchi jumlani birinchisidan kelib '
                    'chiqadi deb qoʻyadi — aslida u undan farq qiladi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>Petrenko accepts the empirical finding and she accepts the theory. '
                '______ she reads the result as a statement about which kind of labour '
                'market the study happened to be measuring.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['By contrast,', 'Instead,', 'Nevertheless,', 'Previously,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Instead,</strong>. Birinchi jumla nima '
                    'qilmasligini aytadi (biri ikkinchisini rad etmaydi), ikkinchisi esa '
                    'uning <em>oʻrniga</em> nima qilishini. <strong>Nevertheless,</strong> '
                    'ziddiyat talab qiladi, bu yerda esa almashtirish bor.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>ELIZA did nothing but match patterns in a sentence and turn them round. '
                '______ the people who used it described the experience as being '
                'listened to.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'For instance,', 'Nonetheless,', 'Similarly,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Nonetheless,</strong>. Dasturning '
                    'soddaligi va foydalanuvchilarning tuygʻusi bir-biriga toʻgʻri '
                    'kelmaydi — kutilmagan burilish. <strong>Accordingly,</strong> '
                    'eng koʻp tanlanadigan xato: u "sodda boʻlgani uchun tinglangandek '
                    'tuyuldi" degan maʼnoni beradi.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Du Bois and his students made sixty hand-drawn charts for the Paris '
                'Exposition of 1900.</li>'
                '<li>The charts show income, literacy, property and occupation among Black '
                'Americans.</li>'
                '<li>They use spirals, stacked areas and other invented forms.</li>'
                '<li>They were hung in a hall containing anthropometric exhibits.</li>'
                '<li>Those exhibits argued that the people in the data were a lesser '
                'kind.</li></ul>',
     'question_text': 'The student wants to explain the charts’ purpose to a reader '
                      'who knows only that they are beautiful. Which choice most '
                      'effectively uses relevant information from the notes to accomplish '
                      'this goal?',
     'choices': [
         'Du Bois and his students made sixty hand-drawn charts for the Paris Exposition of 1900.',
         'The charts show income, literacy, property and occupation among Black Americans.',
         'The charts use spirals, stacked areas and other forms invented for the purpose.',
         'The charts hung in a hall where anthropometric exhibits argued that Black Americans were a lesser kind; their invented forms answer that argument in its own visual language.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The charts hung in</strong>… Oʻquvchi '
                    'goʻzallikni allaqachon koʻrgan, demak kerak boʻlgani — '
                    '<em>nega</em> shunday qilingani: qaysi xonada va qaysi daʼvoga qarshi. '
                    '<strong>The charts use spirals, stacked areas</strong>… aynan '
                    'oʻquvchi bilgan narsani takrorlaydi va maqsadni ochmaydi.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>The Justinianic plague was known mainly from Procopius and a few '
                'chronicles.</li>'
                '<li>Historians disputed whether the death toll had been exaggerated.</li>'
                '<li>In 2013 <i>Yersinia pestis</i> DNA was recovered from sixth-century '
                'teeth in Bavaria.</li>'
                '<li>The DNA establishes that the pathogen was present in sixth-century '
                'Europe.</li>'
                '<li>Mortality estimates still rest on the same chroniclers.</li></ul>',
     'question_text': 'The student wants to state both what the DNA settled and what it did '
                      'not. Which choice most effectively uses relevant information from '
                      'the notes to accomplish this goal?',
     'choices': [
         'Historians had disputed whether the death toll of the plague was exaggerated.',
         'In 2013 <i>Yersinia pestis</i> DNA was recovered from sixth-century teeth in Bavaria.',
         'The DNA settles that the pathogen was in sixth-century Europe, which the sceptics had doubted; it says nothing about how many died, and those estimates still rest on the same chroniclers.',
         'The Justinianic plague was known mainly from Procopius and a handful of chronicles.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>The DNA settles that</strong>… Maqsadda ikki '
                    'talab bor — nima hal boʻldi <em>va</em> nima hal boʻlmadi — '
                    'va faqat shu variant ikkalasini ham beradi. <strong>In 2013 '
                    '<i>Yersinia pestis</i> DNA was recovered</strong>… voqeani aytadi, '
                    'lekin uning ikki tomonlama natijasini emas.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Ramanujan sent Hardy a letter in 1913 with about 120 theorems.</li>'
                '<li>Most of them were stated without proof.</li>'
                '<li>Hardy’s first thought was that the letter was a hoax.</li>'
                '<li>Some results Hardy already knew; others he could not prove '
                'himself.</li>'
                '<li>Hardy concluded that a forger able to invent them would have published '
                'them himself.</li></ul>',
     'question_text': 'The student wants to convey why Hardy came to take the letter '
                      'seriously. Which choice most effectively uses relevant information '
                      'from the notes to accomplish this goal?',
     'choices': [
         'Hardy could not prove some of the results and recognised others — and concluded that anyone able to invent such theorems would have published them under his own name.',
         'Hardy’s first thought was that the letter must be a hoax.',
         'Most of the theorems in Ramanujan’s letter were stated without any proof.',
         'Ramanujan sent Hardy a letter in 1913 containing about a hundred and twenty theorems.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Hardy could not prove</strong>… Maqsad '
                    '<em>nega ishondi</em> degan savolga javob beradi, demak javobda '
                    'dalil (isbotlay olmadi, baʼzilarini tanidi) va undan chiqarilgan '
                    'xulosa boʻlishi kerak. <strong>Hardy’s first thought was that '
                    'the letter must be a hoax</strong>… aynan teskari holatni beradi: bu '
                    'ishonchning emas, shubhaning bosqichi.'},
]
