# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 5 · Reading and Writing, Module 2 (UPPER)
#  27 questions · 32 minutes · taken by a pupil who scored 18+ on rw1.
#
#  Same domains, same counts, same order as the lower module. What changes
#  is the disguise: two-step reasoning, longer syntax, harder vocabulary.
#
#  Load: python manage.py load_mock exam/data/sat5_rw2_hard.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §3
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
     'passage': '<p>Mansa Musa’s caravan to Mecca in 1324 spent and gave away so much '
                'gold in Cairo that the price of the metal there fell and did not recover '
                'for a decade. The episode is usually told as a display of wealth. It is '
                'also the clearest surviving ______ of how much gold the Mali empire '
                'controlled.</p>',
     'question_text': WORD_Q,
     'choices': ['denial', 'forecast', 'measure', 'rumour'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>measure</strong>. Narxning tushishi — '
                    'raqamli iz: u qancha oltin borligini <em>oʻlchab</em> beradi. '
                    '<strong>rumour</strong> chalgʻituvchi, chunki voqea afsonaga '
                    'aylangan; ammo matn uni ishonchli dalil sifatida qoʻyadi.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>Resistance to an antibiotic is not always inherited from a parent cell. '
                'Many of the genes ride on plasmids — small rings of DNA that one '
                'bacterium can hand to another, and across species at that — so a '
                'population can end up with a resistance it never ______.</p>',
     'question_text': WORD_Q,
     'choices': ['encountered', 'evolved', 'expressed', 'required'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>evolved</strong>. Birinchi jumla ziddiyatni '
                    'qoʻyadi: qarshilik ota-onadan <em>meros</em> boʻlmasligi mumkin. Demak '
                    'populyatsiya uni oʻzi <em>rivojlantirmagan</em>, tayyor holda olgan. '
                    '<strong>encountered</strong> notoʻgʻri: gen bor, demak uchrashuv '
                    'boʻlgan.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>Gödel’s first theorem is often paraphrased as saying that '
                'mathematics contains truths that cannot be proved. The paraphrase is not '
                'wrong, but it is ______: the theorem is about a particular kind of formal '
                'system, and what it shows is that any such system strong enough to '
                'describe arithmetic contains a statement it can neither prove nor '
                'disprove.</p>',
     'question_text': WORD_Q,
     'choices': ['false', 'loose', 'novel', 'technical'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>loose</strong> — aniq emas, '
                    'chala-yarim. "not wrong, but it is ___" qurilishi xato boʻlmagan, '
                    'lekin kamchiligi bor narsani talab qiladi, ikki nuqtadan keyingi qism '
                    'esa aniq shaklni beradi. <strong>false</strong> "not wrong" ga '
                    'toʻgʻridan-toʻgʻri zid.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>Mary Shelley’s 1831 preface to <i>Frankenstein</i> does in four '
                'pages what a modern author would need a chapter for: the wet summer, the '
                'ghost stories, the dream, the decision to write. The <u>economy</u> is not '
                'modesty. It is a writer who knows exactly which five facts the reader '
                'needs.</p>',
     'question_text': 'As used in the text, what does the word <u>economy</u> most nearly '
                      'mean?',
     'choices': ['concision', 'frugality', 'profit', 'system'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>concision</strong> — ixchamlik. Matn '
                    'toʻrt sahifani bir bobga qarshi qoʻyadi va oxirgi jumlada sababni '
                    'aytadi: kerakli beshta faktni bilish. <strong>frugality</strong> '
                    '"economy" soʻzining pul bilan bogʻliq maʼnosiga tortadi — bu '
                    'yerda esa soʻz miqdori haqida gap ketyapti.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>The Ise Grand Shrine is about 1,300 years old, and none of its timber '
                'is more than twenty. Every twenty years the shrine is rebuilt beside '
                'itself on an identical plot; the new building is consecrated, the old one '
                'is taken down, and the empty plot waits two decades for its own turn. What '
                'is preserved is not the material. It is the knowledge of how to turn that '
                'material into that building — knowledge that cannot survive a gap '
                'longer than a carpenter’s working life.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that the shrine ought to be dated from its most recent construction',
         'To compare Japanese and European approaches to architectural conservation',
         'To describe the religious ceremonies that accompany each rebuilding',
         'To explain that the shrine’s continuity is carried by transmitted craft rather than by surviving fabric',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To explain that the</strong>… Matn oxirgi ikki '
                    'jumlada fikrini ochiq aytadi: saqlanayotgani material emas, '
                    '<em>bilim</em>. <strong>To argue that the shrine ought to be dated '
                    'from its most recent construction</strong>… matn aynan buning '
                    'aksini qiladi — u 1,300 yilni oʻrinli deb hisoblaydi.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>A patient told that a drug may cause nausea is more likely to report '
                'nausea, whether or not the drug can cause it. <u>The effect is not a '
                'failure of honesty on the patient’s part.</u> Expectation changes '
                'what the nervous system does with a signal, and a symptom produced that '
                'way is as real to the person having it as one produced by a molecule.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It concedes a limitation in the evidence described before it.',
         'It forestalls a likely misreading of the previous sentence, which the rest of the text then explains.',
         'It offers an example of a drug that produces nausea.',
         'It restates the opening sentence in clinical language.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>It forestalls a likely</strong>… Oldingi jumlani '
                    'oʻqigan kishi bemorni oʻylab topyapti deb tushunishi mumkin; bu jumla '
                    'aynan shu oʻqishni oldindan rad etadi, keyingisi esa nega ramzning '
                    'haqiqiy ekanini tushuntiradi. <strong>It concedes a limitation in the '
                    'evidence</strong>… notoʻgʻri: dalilning emas, talqinning oldi '
                    'olinyapti.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>An offset lets an emitter pay for a tonne of carbon to '
                'be avoided or absorbed somewhere else. Done properly, the atmosphere '
                'cannot tell the difference between a tonne not emitted in Rotterdam and a '
                'tonne absorbed in Pará, and the money flows to whichever is '
                'cheaper.</p>'
                '<p><b>Text 2</b><br>Idris Bello’s objection is not to the accounting '
                'but to the counterfactual. Every offset rests on a claim about what would '
                'have happened otherwise — that this forest would have been felled, '
                'that this stove would not have been bought. The claim is unobservable in '
                'principle, and the market pays the seller to make it generous.</p>',
     'question_text': 'Based on the texts, Bello’s objection to offsets is best '
                      'described as concerning',
     'choices': [
         'the cost of buying offsets relative to reducing emissions directly.',
         'the difference between avoiding a tonne of carbon and absorbing one.',
         'the impossibility of verifying the baseline against which a saving is measured.',
         'whether the atmosphere responds differently to emissions in different places.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>the impossibility of verifying</strong>… 2-matn '
                    'birinchi jumladayoq hisob-kitobni chetga suradi va eʼtirozni '
                    '<em>taqqoslash nuqtasiga</em> qaratadi: boshqacha boʻlganda nima '
                    'boʻlardi. <strong>whether the atmosphere responds differently to '
                    'emissions in different places</strong>… Bello bunga tegmaydi — u '
                    'fizikani emas, asosni shubha ostiga oladi.'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>For most of his life the man who put Sputnik and Gagarin into orbit was '
                'referred to in the Soviet press only as the Chief Designer. Sergei '
                'Korolev’s name was a state secret, on the reasoning that a named man '
                'can be assassinated. The cost of that policy fell due in 1966: when he '
                'died on an operating table the programme lost not only an engineer but the '
                'only person with the standing to make rival design bureaux co-operate '
                '— and no successor inherited the standing, because nobody outside the '
                'programme knew it had existed.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Korolev was a more capable engineer than any of his contemporaries.',
         'Soviet design bureaux were more numerous than their American counterparts.',
         'The secrecy that protected Korolev also made his authority impossible to pass on.',
         'The Soviet space programme declined mainly because of a shortage of funding.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>The secrecy that protected</strong>… Matn '
                    '"the cost of that policy" iborasi bilan sababni oqibatga ulaydi: nom '
                    'yashirilgani uchun obroʻ ham koʻrinmas edi, koʻrinmas obroʻni esa '
                    'meros qilib boʻlmaydi. <strong>Korolev was a more capable '
                    'engineer</strong>… matn uni boshqalar bilan taqqoslamaydi.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>The Cairo episode is documented from the Egyptian side, by writers who '
                'watched the caravan arrive and recorded what it spent. It is barely '
                'documented from the Malian side at all: the empire’s own records were '
                'kept in Timbuktu and Gao in forms that have mostly not survived, and what '
                'does survive says little about the hajj. The event that made Mansa Musa '
                'famous in Europe is therefore known almost entirely through the eyes of a '
                'place he was passing through.</p>',
     'question_text': 'According to the text, why is the hajj known mainly from Egyptian '
                      'sources?',
     'choices': [
         'Egyptian writers of the period were more accurate than Malian ones.',
         'European writers copied their accounts from Egyptian originals.',
         'Malian records of the period have largely not survived.',
         'The Malian court forbade any written account of the journey.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Malian records of</strong>… Matn sababni ikki '
                    'nuqtadan keyin oʻzi aytadi: yozuvlar saqlanmagan. <strong>The Malian '
                    'court forbade any written account</strong>… taqiq haqida matnda bir '
                    'soʻz ham yoʻq — yoʻqolish va taqiqlanish bir narsa emas.'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A microbiologist claims that the speed at which resistance spreads '
                'through a hospital cannot be explained by mutation and selection alone '
                '— that it requires genes moving sideways between cells, which would '
                'mean resistance should turn up in species that were never exposed to the '
                'drug at all.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'microbiologist’s claim?',
     'choices': [
         'Bacteria exposed to low doses of an antibiotic acquire resistance faster than those exposed to high doses.',
         'Resistance genes with identical sequences are found in unrelated species sharing a ward, including species never treated with the drug.',
         'Resistant strains grow more slowly than susceptible ones when the drug is absent.',
         'The rate of mutation in bacteria rises when the cells are under stress.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Resistance genes with identical</strong>… '
                    'Daʼvoning sinovi matnda aytilgan: dori tegmagan turda ham qarshilik '
                    'chiqishi kerak. Ketma-ketliklarning <em>aynan bir xilligi</em> esa '
                    'mustaqil mutatsiyani deyarli imkonsiz qiladi. <strong>The rate of '
                    'mutation in bacteria rises when the cells are under stress</strong>… '
                    'aksincha, rad etilayotgan "mutatsiya" tushuntirishini quvvatlaydi.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A historian claims that the twenty-year cycle at Ise is calibrated to '
                'the transmission of skill — that the interval is set by how long a '
                'carpenter’s career can bridge rather than by how long the timber '
                'lasts.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'historian’s claim?',
     'choices': [
         'Carpenters are first admitted to the rebuild as apprentices and work on their third and last as masters instructing apprentices of their own.',
         'The cypress used at Ise comes from forests the shrine has managed for centuries.',
         'The rebuilding was suspended for more than a century during a period of civil war.',
         'The shrine’s timbers show no sign of decay after twenty years in place.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Carpenters are first admitted</strong>… Daʼvo '
                    'oraliq <em>inson umriga</em> moslangan deydi, va uch marta qatnashish '
                    '— shogirddan ustagacha — aynan bir kasb umrini beradi. '
                    '<strong>The shrine’s timbers show no sign of decay after twenty '
                    'years</strong> ham qoʻllab-quvvatlaydi, lekin faqat inkor yoʻli bilan: '
                    'u yogʻoch sababi emasligini koʻrsatadi, mahorat sababi ekanini emas.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>An auditor re-examined four forest-offset projects and compared the '
                'carbon saving each had claimed with the saving its own re-analysis '
                'supported.</p>'
                '<table><tr><th>Project</th><th>Claimed saving (thousand tonnes)</th>'
                '<th>Saving supported (thousand tonnes)</th></tr>'
                '<tr><td>P</td><td>480</td><td>420</td></tr>'
                '<tr><td>Q</td><td>610</td><td>310</td></tr>'
                '<tr><td>R</td><td>950</td><td>190</td></tr>'
                '<tr><td>S</td><td>1,400</td><td>140</td></tr></table>',
     'question_text': 'A student concludes that the larger a project’s claim, the '
                      'smaller the share of it the re-analysis supported. Which choice best '
                      'describes data from the table that support this conclusion?',
     'choices': [
         'Every project’s supported saving was lower than the saving it had claimed.',
         'Project R’s claim was more than one and a half times Project Q’s.',
         'Project S claimed a saving of 1,400 thousand tonnes.',
         'The share supported fell at every step, from about 88% at P (480 claimed) to 10% at S (1,400 claimed).',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The share supported fell</strong>… Xulosa '
                    '<em>ulush</em> haqida, yaʼni ikki ustunning nisbati haqida — '
                    'demak dalil ham oʻsha nisbatni butun jadval boʻylab kuzatishi kerak. '
                    '<strong>Every project’s supported saving was lower than the '
                    'saving it had claimed</strong>… rost, lekin u faqat "past" deydi, '
                    '"tobora pastroq" demaydi — tendensiya koʻrinmaydi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>Gödel’s theorem applies to any formal system that is '
                'consistent and strong enough to express arithmetic. Adding the unprovable '
                'statement to the system as a new axiom does not repair it: the enlarged '
                'system is still consistent and still strong enough, so the theorem applies '
                'again and yields a new statement it cannot settle. The incompleteness is '
                'therefore ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'a defect of the particular axioms that were first chosen.',
         'confined to systems that describe infinite sets.',
         'evidence that arithmetic itself must be inconsistent.',
         'not something that can be patched by adding further axioms.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>not something that</strong>… Matn tuzatish '
                    'urinishini bajarib koʻrsatadi va natija oʻsha-oʻsha boʻlib qolishini '
                    'aytadi — demak kamchilik aksiomalar toʻplamida emas. <strong>a '
                    'defect of the particular axioms that were first chosen</strong> aynan '
                    'matn rad etgan fikr.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>If the rate of a given side effect in a trial’s placebo arm is a '
                'quarter of the rate in the drug arm, then a quarter of what the drug '
                'appears to do to patients is not the drug. This has a consequence for how '
                'a medicine’s information leaflet should be written, because '
                '______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'listing a symptom makes some readers more likely to experience it.',
         'most patients do not read the leaflet in any case.',
         'placebo arms are not used in every clinical trial.',
         'the symptoms in the drug arm are more severe than those in the placebo arm.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>listing a symptom makes</strong>… Platsebo '
                    'guruhida ham alomat chiqadi, demak uni tugʻdiradigan narsa moddada '
                    'emas, <em>kutishda</em> — varaqa esa aynan kutish yaratadi. '
                    '<strong>most patients do not read the leaflet in any case</strong> '
                    'tuzoq: u varaqani muhimsiz qilib qoʻyadi, matn esa uni qanday yozish '
                    'kerakligi haqida.'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Korolev’s name — a state secret for the whole of his working '
                '______ appeared in print for the first time in his obituary.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['life', 'life —', 'life,', 'life;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>life —</strong>. Qoʻshimcha izoh tire '
                    'bilan <em>ochilgan</em>, demak tire bilan yopiladi: juftlik bir xil '
                    'belgilardan tuziladi. <strong>life,</strong> eng koʻp tanlanadigan '
                    'xato — vergul va tire juftlik hosil qilmaydi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>Shelley’s preface names four ______ the wet summer of 1816, which '
                'kept the party indoors; the ghost stories; the dream; and the decision to '
                'write.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['things', 'things,', 'things:', 'things;'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>things:</strong>. Ikki nuqta toʻliq gapdan keyin '
                    'sanashni kiritadi — va bu yerda ayniqsa zarur, chunki sanash '
                    'aʼzolarining ichida allaqachon vergul bor, shuning uchun aʼzolar '
                    'nuqtali vergul bilan ajratilgan. <strong>things,</strong> sanashni '
                    'oldingi vergullar bilan aralashtirib yuboradi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>Every twenty years the shrine is rebuilt on an identical plot beside '
                'the ______ which then stands empty for two decades awaiting its own '
                'turn.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['old one', 'old one,', 'old one:', 'old one;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>old one,</strong>. "which then stands empty…" '
                    '— ajratilgan (qoʻshimcha) aniqlovchi ergash gap: u qaysi uchastka '
                    'ekanini toraytirmaydi, faqat izoh beradi, shuning uchun vergul bilan '
                    'ajratiladi. <strong>old one;</strong> notoʻgʻri: "which…" mustaqil gap '
                    'emas.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Not until his obituary appeared ______ the Chief Designer’s name '
                'printed in the Soviet press.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['has been', 'is', 'was', 'were'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>was</strong>. "Not until…" bilan boshlangan gap '
                    'ingliz tilida teskari tartibni talab qiladi, ega esa — '
                    '<em>the name</em>, birlik va oʻtgan zamonda. <strong>were</strong> '
                    'koʻplik: bitta nom bor, uni "obituary" yoki "press" bilan '
                    'adashtirmang.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>The policy required that Korolev’s name ______ out of every '
                'published account of the programme.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['be kept', 'is kept', 'keeps', 'was kept'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>be kept</strong>. "require that" dan keyin '
                    'ingliz tilida buyruq-istak shakli keladi: feʼl asos shaklida turadi, '
                    'majhul nisbatda esa <em>be</em> + III shakl. <strong>was kept</strong> '
                    'quloqqa toʻgʻriroq eshitiladi va aynan shuning uchun eng koʻp '
                    'tanlanadi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>The saving supported by the auditor was far smaller than ______ claimed '
                'by the project itself.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['that', 'them', 'these', 'those'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>that</strong>. Taqqoslanayotgan narsa — '
                    '<em>the saving</em>, birlik, demak uning oʻrnini birlik olmosh bosadi. '
                    '<strong>those</strong> koʻplikni bildiradi va bu yerda egasi yoʻq.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Bello’s objection is not to the accounting, not to the price, but '
                '______</p>',
     'question_text': CONVENTION_Q,
     'choices': ['about the counterfactual.', 'counterfactually.', 'the counterfactual.',
                 'to the counterfactual.'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>to the counterfactual.</strong> Qator '
                    '"not to…, not to…, but ___" — ikkala inkor ham <em>to</em> '
                    'predlogi bilan qurilgan, demak uchinchi aʼzo ham shunday boʻlishi '
                    'shart. <strong>the counterfactual.</strong> predlogni tashlab ketadi '
                    'va muvozanatni buzadi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Adding the unprovable statement as a new axiom leaves the system '
                'consistent and still strong enough to express arithmetic. ______ the '
                'theorem applies to the enlarged system in its turn.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['By contrast,', 'Consequently,', 'Even so,', 'Previously,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Consequently,</strong>. Teorema aynan shu ikki '
                    'shart bajarilganda qoʻllanadi, va ikkalasi ham saqlanib qoldi — '
                    'demak natija majburiy. <strong>Even so,</strong> ziddiyat talab '
                    'qiladi, bu yerda esa ikkinchi jumla birinchisidan kelib chiqadi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>Plasmids can carry resistance across from one species to another in '
                'hours. ______ the genes they carry are often costly to the cell, and a '
                'population sheds them once the drug is withdrawn.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'For instance,', 'That said,', 'Therefore,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>That said,</strong>. Birinchi jumla xavotirni '
                    'kuchaytiradi, ikkinchisi esa uni yumshatadi — yon berish. '
                    '<strong>Accordingly,</strong> va <strong>Therefore,</strong> ikkalasi '
                    'ham natija bildiradi, lekin genlarning qimmatga tushishi plazmidlar '
                    'tezligidan kelib chiqmaydi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>The arithmetic behind an offset is straightforward enough. ______ the '
                'claim it rests on — that this forest would otherwise have been felled '
                '— can never be observed.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'For example,', 'Likewise,', 'Still,'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Still,</strong>. Birinchi jumla yon beradi '
                    '(hisob oson), ikkinchisi esa asosiy eʼtirozni qoʻyadi — '
                    'qarama-qarshilik. <strong>Accordingly,</strong> ikkinchi jumlani '
                    'birinchisidan chiqadi deb qoʻyadi, aslida u unga qarshi turadi.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Sergei Korolev directed the programme that launched Sputnik and '
                'Gagarin.</li>'
                '<li>His name was kept a state secret so that he could not be '
                'assassinated.</li>'
                '<li>He died during surgery in 1966.</li>'
                '<li>He had been the only person able to make rival design bureaux '
                'co-operate.</li>'
                '<li>Nobody outside the programme knew that authority had existed.</li></ul>',
     'question_text': 'The student wants to explain the cost of the secrecy. Which choice '
                      'most effectively uses relevant information from the notes to '
                      'accomplish this goal?',
     'choices': [
         'Korolev died during surgery in 1966.',
         'Korolev’s name was kept a state secret so that he could not be assassinated.',
         'Sergei Korolev directed the programme that launched Sputnik and Gagarin.',
         'The secrecy that kept Korolev safe meant that when he died in 1966 the authority he alone held over rival bureaux could not be handed on — nobody outside the programme knew it had existed.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The secrecy that kept</strong>… "Narx" '
                    'koʻrsatilishi uchun ikki tomon ham kerak: maxfiylik nimani bergani va '
                    'nimani olib qoʻygani. Faqat shu variant ularni bitta jumlada '
                    'bogʻlaydi. <strong>Korolev’s name was kept a state secret so that '
                    'he could not be assassinated</strong>… faqat foydasini aytadi.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>The Ise Grand Shrine is about 1,300 years old.</li>'
                '<li>None of its timber is more than twenty years old.</li>'
                '<li>The shrine is rebuilt every twenty years on an identical plot beside '
                'the old one.</li>'
                '<li>Carpenters join the work as apprentices and return to it as '
                'masters.</li>'
                '<li>What passes down is the knowledge of how to build it.</li></ul>',
     'question_text': 'The student wants to explain what the rebuilding actually preserves. '
                      'Which choice most effectively uses relevant information from the '
                      'notes to accomplish this goal?',
     'choices': [
         'None of the shrine’s timber is more than twenty years old.',
         'The shrine is rebuilt every twenty years, so none of its timber is old — what is 1,300 years old is the knowledge, carried by carpenters who join as apprentices and return as masters.',
         'The shrine is rebuilt on an identical plot beside the old one.',
         'The Ise Grand Shrine is about 1,300 years old.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>The shrine is rebuilt</strong>… Maqsad '
                    '<em>nima saqlanayotganini</em> aytish, demak javob yoshning '
                    'paradoksini (1,300 va 20) yechishi va saqlanayotgan narsani nomlashi '
                    'kerak. <strong>The Ise Grand Shrine is about 1,300 years old</strong>… '
                    'paradoksning faqat yarmini beradi va tushuntirmaydi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>An offset pays for a tonne of carbon to be avoided or absorbed '
                'elsewhere.</li>'
                '<li>The atmosphere does not distinguish where a tonne is saved.</li>'
                '<li>Every offset rests on a claim about what would otherwise have '
                'happened.</li>'
                '<li>That counterfactual cannot be observed.</li>'
                '<li>The market rewards sellers who make the counterfactual '
                'generous.</li></ul>',
     'question_text': 'The student wants to state the objection to offsets without '
                      'overstating it. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'An offset pays for a tonne of carbon to be avoided or absorbed somewhere else.',
         'The atmosphere does not distinguish between a tonne saved in one place and a tonne saved in another.',
         'The market rewards sellers who make their counterfactual claims generous.',
         'The physics of an offset is sound — the atmosphere does not care where a tonne is saved — but every offset rests on an unobservable claim about what would otherwise have happened, and the market rewards the seller for making it generous.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The physics of an</strong>… Maqsadda ikki talab '
                    'bor: eʼtirozni aytish <em>va</em> uni kuchaytirib yubormaslik. Faqat '
                    'shu variant fizikaning toʻgʻriligini tan olib, muammoni aniq joyga '
                    '— tekshirib boʻlmaydigan farazga — qoʻyadi. <strong>The '
                    'market rewards sellers who make their counterfactual claims '
                    'generous</strong>… eng ogʻir ayblovni yolgʻiz qoldiradi va offsetni '
                    'butunlay firibgarlikdek koʻrsatadi.'},
]
