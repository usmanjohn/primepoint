# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 6 · Reading and Writing, Module 2 (UPPER)
#  27 questions · 32 minutes · taken by a pupil who scored 18+ on rw1.
#
#  Same domains, same counts, same order as the lower module. What changes
#  is the disguise: two-step reasoning, longer syntax, harder vocabulary.
#
#  Load: python manage.py load_mock exam/data/sat6_rw2_hard.py --expect-questions=27
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
     'passage': '<p>Shannon’s 1948 paper takes the word <i>information</i> away from '
                'meaning and attaches it to surprise. A message saying what the receiver '
                'already expects carries almost none; a message that could have been any of '
                'a million things carries a great deal. The definition is ______ on '
                'purpose: it had to be measurable, and meaning is not.</p>',
     'question_text': WORD_Q,
     'choices': ['narrow', 'poetic', 'provisional', 'traditional'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>narrow</strong>. Ikki nuqtadan keyingi qism '
                    'sababni aytadi: oʻlchash mumkin boʻlishi uchun maʼno chiqarib '
                    'tashlangan — yaʼni taʼrif ataylab <em>toraytirilgan</em>. '
                    '<strong>provisional</strong> (vaqtinchalik) notoʻgʻri: matnda taʼrif '
                    'keyinroq kengaytiriladi deb aytilmagan.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>In June 1908 something flattened two thousand square kilometres of '
                'Siberian forest and left no crater. The absence of a crater is the fact '
                'that ______ the explanations: a body that struck the ground would have '
                'made one, so whatever it was must have burst in the air.</p>',
     'question_text': WORD_Q,
     'choices': ['confirms', 'constrains', 'multiplies', 'postpones'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>constrains</strong> — chegaralaydi. Ikki '
                    'nuqtadan keyingi qism koʻrsatadi: bitta fakt izohlarning bir qismini '
                    'kesib tashlaydi. <strong>multiplies</strong> aynan teskari yoʻnalish: '
                    'krater yoʻqligi variantlarni koʻpaytirmaydi, kamaytiradi.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>A prion carries no genetic material of any kind. It is a protein in the '
                'wrong shape, and it spreads by ______: a misfolded molecule meeting a '
                'correctly folded one persuades the second into the shape of the first, and '
                'then there are two.</p>',
     'question_text': WORD_Q,
     'choices': ['conversion', 'division', 'mutation', 'reproduction'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>conversion</strong> — shaklni '
                    'oʻzgartirish. Ikki nuqtadan keyingi jumla jarayonni tasvirlaydi: '
                    'mavjud molekula boshqasini oʻziga oʻxshatadi. '
                    '<strong>reproduction</strong> va <strong>division</strong> yangi '
                    'nusxa yaratishni bildiradi — lekin birinchi jumla genetik '
                    'material yoʻqligini aytib, bu yoʻlni yopib qoʻygan.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>A climate model is not a prediction machine and does not pretend to be '
                'one. It is an <u>argument</u> made in code: these are the processes we '
                'think matter, this is how we think they interact, and this is what follows '
                'if we have got them right.</p>',
     'question_text': 'As used in the text, what does the word <u>argument</u> most nearly '
                      'mean?',
     'choices': ['case', 'dispute', 'outline', 'summary'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>case</strong> — asoslangan daʼvo. Ikki '
                    'nuqtadan keyingi uchta band dalil zanjirini beradi: shartlar, '
                    'bogʻlanish, xulosa. <strong>dispute</strong> "argument" soʻzining '
                    'kundalik maʼnosi (janjal) va shuning uchun eng kuchli tuzoq — bu '
                    'yerda hech kim bahslashmayapti.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>Of the sixty-three clauses of Magna Carta, three are still on the '
                'English statute book. The rest deal with fish weirs, forest law and the '
                'debts of the Jewish community, and were repealed over centuries without '
                'anyone much minding. What survives is not the document but a sentence in '
                'it — that no free man shall be imprisoned except by the lawful '
                'judgement of his peers or by the law of the land — and the use later '
                'generations made of that sentence, most of which its authors would not '
                'have recognised.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that the repealed clauses were more significant than historians allow',
         'To compare English constitutional history with that of other countries',
         'To describe the circumstances under which Magna Carta was sealed in 1215',
         'To explain that the charter’s standing rests on the later use of one clause rather than on the document as a whole',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To explain that the</strong>… Matn hujjatning '
                    'katta qismini ataylab pastga tushiradi ("without anyone much minding") '
                    'va oxirgi jumlada omon qolgan narsani aniq nomlaydi: bitta jumla va '
                    'keyingi avlodlar undan qilgan foydalanish. <strong>To argue that the '
                    'repealed clauses were more significant</strong>… aynan aksi.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>A university is sued for discrimination: across the institution as a '
                'whole, men are admitted at a higher rate than women. Department by '
                'department, every single department admits women at a higher rate than '
                'men. <u>Both statements are true, and they are true of the same '
                'numbers.</u> Women applied in greater proportion to the departments that '
                'reject most applicants, and the aggregate buries that.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It concedes that the data behind the case were incomplete.',
         'It forestalls the assumption that one of the two claims must be false, which the final sentence then explains.',
         'It offers evidence that the university did discriminate against women.',
         'It restates the two claims in more precise statistical language.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>It forestalls the assumption</strong>… '
                    'Oʻquvchi ikki daʼvoni oʻqib, biri yolgʻon deb oʻylaydi; jumla aynan shu '
                    'yoʻlni yopadi, oxirgi jumla esa ikkalasi qanday birga rost '
                    'boʻlishini tushuntiradi. <strong>It offers evidence that the '
                    'university did discriminate</strong>… notoʻgʻri: jumla hech qaysi '
                    'tomonni tanlamaydi.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>The Finnish basic income trial paid two thousand '
                'unemployed people a monthly sum, with no conditions attached, for two '
                'years. Employment among them was no worse than in the control group, and '
                'self-reported wellbeing was markedly better. The money did not stop people '
                'looking for work.</p>'
                '<p><b>Text 2</b><br>Wiremu Tane accepts both results and notes what a '
                'trial of this kind cannot test. Two thousand people receiving an income is '
                'not the same experiment as everyone receiving one: prices do not move, '
                'employers do not adjust wages, and nobody’s neighbour is in the '
                'scheme. A pilot measures the effect on a participant, not the effect of a '
                'policy.</p>',
     'question_text': 'Based on the texts, Tane’s objection to generalising from the '
                      'trial is that',
     'choices': [
         'a small trial cannot produce the economy-wide effects a universal scheme would.',
         'the control group was not properly comparable to the group receiving payments.',
         'the wellbeing measures relied on what the participants reported themselves.',
         'two years is too short a period over which to judge any employment effect.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>a small trial cannot</strong>… Tane ikki '
                    'nuqtadan keyin aynan shu roʻyxatni beradi: narx qimirlamaydi, ish haqi '
                    'oʻzgarmaydi, qoʻshni sxemada emas. <strong>the wellbeing measures '
                    'relied on what the participants reported</strong>… oʻlchov usuliga '
                    'eʼtiroz boʻlardi, Tane esa birinchi jumladayoq natijalarni qabul '
                    'qiladi.'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>When Duchamp submitted a urinal to the 1917 Independents exhibition, '
                'signed with a name that was not his, the committee — which had '
                'promised to hang anything submitted with the fee — hid it. The object '
                'itself is lost; what survives is a photograph and the argument. '
                'Duchamp’s claim was that the artist’s act is choosing rather '
                'than making, and the committee proved the claim by behaving as though a '
                'choice were the sort of thing that could be refused.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Duchamp submitted the work under a false name in order to avoid controversy.',
         'The committee’s suppression of the work demonstrated the very point the work was making.',
         'The photograph is now held to be more valuable than the original object was.',
         'The urinal was the first mass-produced object ever exhibited as a work of art.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>The committee’s suppression of</strong>… '
                    'Matn oxirgi jumlada aylanani yopadi: daʼvo — sanʼat tanlashdir; '
                    'qoʻmita tanlovni rad etib, uni tanlov deb tan olgan boʻladi. '
                    '<strong>Duchamp submitted the work under a false name in order to '
                    'avoid controversy</strong>… soxta nom matnda bor, lekin sabab '
                    'aytilmagan — bu oʻqilmagan bogʻlanish.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>Alice Kober never claimed to have deciphered Linear B and never tried '
                'to. She spent a decade building, on cards cut by hand from cigarette '
                'cartons, a record of which signs appeared with which others, and from it '
                'she showed that the language inflected — that certain signs were '
                'endings. Ventris read the script two years after she died, working from '
                'her grids. What Kober produced was not an answer but the shape of '
                'one.</p>',
     'question_text': 'According to the text, what did Kober’s work establish?',
     'choices': [
         'That Linear B had been used chiefly for administrative records.',
         'That Linear B was an early form of the Greek language.',
         'That the language written in Linear B changed its word endings.',
         'That the script contained more signs than had previously been thought.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>That the language written</strong>… Matn tiredan '
                    'keyin aniq aytadi: "the language inflected — that certain signs '
                    'were endings". <strong>That Linear B was an early form of the Greek '
                    'language</strong>… bu Ventrisning natijasi, Koberniki emas — matn '
                    'ikkisini ataylab ajratadi.'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A biochemist claims that a prion disease spreads by shape alone — '
                'that no nucleic acid is involved at any stage — which would mean an '
                'agent stripped of every trace of DNA and RNA ought to remain infectious.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'biochemist’s claim?',
     'choices': [
         'Preparations treated with enzymes that destroy nucleic acids, and with radiation at doses that destroy them, remain fully infectious.',
         'Prion diseases have incubation periods measured in years or decades.',
         'Some individuals carry a genetic variant that makes them resistant to infection.',
         'The misfolded protein accumulates in brain tissue rather than elsewhere in the body.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Preparations treated with enzymes</strong>… '
                    'Daʼvoning sinovi matnda aytilgan: nuklein kislotani yoʻq qilib '
                    'koʻring. Ikki mustaqil usul (ferment va nurlanish) bir xil natija '
                    'bersa, sabab shaklda qoladi. <strong>Some individuals carry a genetic '
                    'variant</strong>… genetika rol oʻynashini koʻrsatadi va daʼvoni '
                    'zaiflashtiradi.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A critic argues that the significance of the 1917 submission lies in '
                'the committee’s response rather than in the object itself — that '
                'without the refusal the piece would have been a joke rather than an '
                'argument.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'critic’s argument?',
     'choices': [
         'Duchamp had exhibited other readymade objects before 1917.',
         'The Independents had advertised that any work submitted with the fee would be hung, with no jury at all.',
         'The photograph of the work was taken by Alfred Stieglitz.',
         'The urinal was a standard model available from a New York supplier.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>The Independents had advertised</strong>… '
                    'Tanqidchi maʼno <em>rad javobida</em> deydi, va rad javobi faqat '
                    'qoʻmita oʻz vaʼdasini buzganda maʼnoga aylanadi. <strong>The urinal '
                    'was a standard model available from a New York supplier</strong>… '
                    'buyumning oʻzi haqida — tanqidchi esa aynan buyum muhim emas '
                    'deydi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>Four basic-income pilots reported the number of people enrolled and the '
                'change in the employment rate among them.</p>'
                '<table><tr><th>Pilot</th><th>People enrolled</th>'
                '<th>Change in employment rate (percentage points)</th></tr>'
                '<tr><td>Finland</td><td>2,000</td><td>+0.3</td></tr>'
                '<tr><td>Stockton</td><td>125</td><td>+12.0</td></tr>'
                '<tr><td>Kenya</td><td>20,000</td><td>+1.1</td></tr>'
                '<tr><td>Ontario</td><td>4,000</td><td>−0.4</td></tr></table>',
     'question_text': 'A student claims that the largest reported employment effect came '
                      'from the smallest pilot. Which choice best describes data from the '
                      'table that support this claim?',
     'choices': [
         'Ontario reported the only negative change in the employment rate.',
         'Stockton, with 125 people enrolled, reported the largest change in employment rate, at +12.0 percentage points.',
         'The Kenyan pilot enrolled 20,000 people, more than any of the others.',
         'Three of the four pilots reported a positive change in employment.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Stockton, with 125</strong>… Daʼvo ikki '
                    '<em>oʻta</em> qiymatni bogʻlaydi — eng kichik namuna va eng katta '
                    'taʼsir — demak dalil ham ikkalasini bitta qatordan olishi kerak. '
                    '<strong>Three of the four pilots reported a positive change</strong>… '
                    'rost, lekin oʻlcham haqida hech narsa demaydi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>On Shannon’s definition the information in a message is a function '
                'of how surprising it is, which means the same sentence can carry different '
                'amounts to different receivers. A forecast of rain carries almost nothing '
                'in a place where it rains every day. It follows that information, in this '
                'sense, is not a property of ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'the channel through which the message travels.',
         'the language in which the message is written.',
         'the message alone.',
         'the speed at which the message is sent.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>the message alone.</strong> Matn kalit faktni '
                    'beradi: <em>bir xil</em> jumla turli qabul qiluvchilarga turlicha '
                    'axborot beradi — demak miqdor jumlaning ichida emas, jumla bilan '
                    'qabul qiluvchi orasida. <strong>the language in which the message is '
                    'written</strong> tuzoq: til ham jumlaning xossasi, lekin matn uni '
                    'oʻzgartirmaydi — u <em>qabul qiluvchini</em> oʻzgartiradi.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>The aggregate rate and the departmental rates disagree because the '
                'departments differ in how hard they are to enter and the two groups '
                'applied to them in different proportions. Nothing about this is peculiar '
                'to admissions. Whenever a population is pooled across groups that differ '
                'both in outcome and in composition, the pooled number ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'becomes impossible to calculate accurately.',
         'can point the opposite way from every group inside it.',
         'should be weighted by the size of each group.',
         'will always favour the larger of the two groups.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>can point the opposite</strong>… Matn aynan '
                    'shunday holatni endigina koʻrsatdi: har bir boʻlim bir tomonga, '
                    'umumiy raqam esa teskari tomonga. Oxirgi jumla uni umumlashtiradi. '
                    '<strong>will always favour the larger of the two groups</strong> '
                    'juda kuchli daʼvo — matn "har doim" deydigan hech narsa '
                    'bermaydi.'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Kober’s grids — built by hand on cards cut from cigarette '
                '______ are what Ventris eventually worked from.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['cartons', 'cartons —', 'cartons,', 'cartons;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>cartons —</strong>. Qoʻshimcha izoh tire '
                    'bilan <em>ochilgan</em>, demak tire bilan yopiladi: juftlik bir xil '
                    'belgilardan tuziladi. <strong>cartons,</strong> eng koʻp tanlanadigan '
                    'xato — vergul va tire juftlik hosil qilmaydi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>The clauses still in force cover three ______ the liberties of the '
                'Church; the customs of the City of London, which are set out at length; '
                'and judgement by one’s peers.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['subjects', 'subjects,', 'subjects:', 'subjects;'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>subjects:</strong>. Ikki nuqta toʻliq gapdan '
                    'keyin sanashni kiritadi — va bu yerda ayniqsa zarur, chunki '
                    'sanash aʼzolarining ichida allaqachon vergul bor, shuning uchun '
                    'aʼzolar nuqtali vergul bilan ajratilgan. <strong>subjects,</strong> '
                    'sanashni oldingi vergullar bilan aralashtirib yuboradi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>The committee quietly hid the ______ which it had promised to hang '
                'without any jury at all.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['submission', 'submission,', 'submission:', 'submission;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>submission,</strong>. "which it had promised to '
                    'hang…" — ajratilgan (qoʻshimcha) aniqlovchi ergash gap: u qaysi '
                    'asar ekanini toraytirmaydi, faqat izoh beradi va kinoyani qoʻshadi. '
                    '<strong>submission;</strong> notoʻgʻri: "which…" mustaqil gap emas.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Among the sixty-three clauses of the charter ______ one that is still '
                'cited in English courts.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are', 'have been', 'is', 'were'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>is</strong>. Gap teskari tartibda: ega feʼldan '
                    'keyin keladi va u — <em>one</em>, birlik. Boshdagi "Among the '
                    'sixty-three clauses" faqat oʻrin holi. <strong>are</strong> eng koʻp '
                    'tanlanadigan xato: quloq yaqin turgan "clauses" ga moslashadi.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>The rules of the exhibition required that every work submitted with the '
                'fee ______ hung.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['be', 'is', 'was', 'were'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>be</strong>. "require that" dan keyin ingliz '
                    'tilida buyruq-istak shakli keladi: feʼl asos shaklida turadi, majhul '
                    'nisbatda esa <em>be</em> + III shakl. <strong>was</strong> quloqqa '
                    'toʻgʻriroq eshitiladi va aynan shuning uchun eng koʻp tanlanadi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>The employment effect reported by the Finnish pilot was far smaller '
                'than ______ reported by Stockton.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['that', 'these', 'them', 'those'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>that</strong>. Taqqoslanayotgan narsa — '
                    '<em>the effect</em>, birlik, demak uning oʻrnini birlik olmosh bosadi. '
                    '<strong>those</strong> koʻplikni bildiradi va bu yerda egasi yoʻq.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Kober’s method was to record every sign, to note which signs '
                'occurred together, and ______</p>',
     'question_text': CONVENTION_Q,
     'choices': ['a grid built from the pattern.', 'building a grid from the pattern.',
                 'she built a grid from the pattern.', 'to build a grid from the pattern.'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>to build a grid</strong>… Qator "to record…to '
                    'note…and ___" — ikkitasi ham <em>to</em> + feʼl, demak uchinchisi '
                    'ham shunday boʻlishi shart. <strong>building a grid from the '
                    'pattern.</strong> maʼnoni buzmaydi va aynan shuning uchun xavfli, '
                    'lekin u qatorning shaklini sindiradi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>A message that says what the receiver already expects carries almost no '
                'information. ______ a forecast of rain tells you less in a rainforest than '
                'the same word tells you in a desert.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['By contrast,', 'Nevertheless,', 'Previously,', 'Thus,'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Thus,</strong>. Ikkinchi jumla birinchisidagi '
                    'qoidaning aniq holati — undan kelib chiqadigan xulosa. '
                    '<strong>By contrast,</strong> ziddiyat talab qiladi, bu yerda esa '
                    'ikkinchi jumla birinchisini tasdiqlaydi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>Kober never attempted a decipherment and said so plainly. ______ '
                'Ventris could not have made one without her grids.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'Even so,', 'For example,', 'Likewise,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Even so,</strong>. Birinchi jumla uning '
                    'daʼvosizligini aytadi, ikkinchisi esa hissasining hal qiluvchi '
                    'ekanini — kutilmagan burilish. <strong>Accordingly,</strong> '
                    'teskari bogʻlanish: u "daʼvo qilmagani uchun Ventris yecha oldi" degan '
                    'maʼnoni beradi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>A pilot pays a few thousand people while prices, wages and social norms '
                'stay exactly where they were. ______ what it measures is the effect on a '
                'participant, not the effect of a policy.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['By contrast,', 'For instance,', 'In other words,', 'Nevertheless,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>In other words,</strong>. Ikkinchi jumla '
                    'birinchisini boshqa soʻzlar bilan, aniqroq qilib aytadi — '
                    'atrofdagi hech narsa oʻzgarmasa, oʻlchanayotgani faqat '
                    'qatnashchining oʻzi. <strong>Nevertheless,</strong> ziddiyat talab '
                    'qiladi, bu yerda esa qayta ifoda bor.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Shannon’s paper on communication appeared in 1948.</li>'
                '<li>He defined information in terms of how surprising a message is.</li>'
                '<li>A message saying what the receiver expects carries almost none.</li>'
                '<li>The definition deliberately leaves meaning out.</li>'
                '<li>Meaning cannot be measured; surprise can.</li></ul>',
     'question_text': 'The student wants to explain what Shannon changed about the word '
                      '<i>information</i>. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'A message that says what the receiver already expects carries almost no information.',
         'Shannon cut meaning out of the word deliberately and defined information as surprise — because surprise can be measured and meaning cannot.',
         'Shannon defined information in terms of how surprising a message is.',
         'Shannon’s paper on communication appeared in 1948.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Shannon cut meaning</strong>… Maqsad '
                    '<em>nima oʻzgarganini</em> aytish, demak javobda olib tashlangan narsa '
                    '(maʼno), oʻrniga qoʻyilgan narsa (kutilmaganlik) va sabab boʻlishi '
                    'kerak. <strong>Shannon defined information in terms of how surprising '
                    'a message is</strong>… faqat yangi taʼrifni beradi — undan nima '
                    'oʻzgargani koʻrinmaydi.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>A prion is a protein that has taken the wrong shape.</li>'
                '<li>It carries no DNA or RNA of any kind.</li>'
                '<li>A misfolded molecule meeting a correctly folded one changes its '
                'shape.</li>'
                '<li>There are then two misfolded molecules.</li>'
                '<li>The process repeats.</li></ul>',
     'question_text': 'The student wants to explain how a prion spreads to an audience '
                      'unfamiliar with it. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'A misfolded molecule changes the shape of a correctly folded one it meets, so there are then two — and the process repeats, which is how something carrying no genetic material can spread.',
         'A prion carries no DNA or RNA of any kind.',
         'A prion is a protein that has taken the wrong shape.',
         'The process by which a prion spreads repeats itself indefinitely.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>A misfolded molecule changes</strong>… Maqsad '
                    '<em>tarqalish yoʻlini</em> tushuntirish, demak javob zanjirni bersin: '
                    'uchrashuv → shakl oʻzgarishi → ikkita → takror. Va u eng gʻalati '
                    'faktni (genetik material yoʻq) mantiqqa bogʻlaydi. <strong>A prion '
                    'carries no DNA or RNA</strong>… jumboqni qoʻyadi, yechmaydi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Magna Carta had sixty-three clauses.</li>'
                '<li>Three of them are still on the statute book.</li>'
                '<li>Most of the rest concern fish weirs, forest law and debts.</li>'
                '<li>One surviving clause promises judgement by peers or by the law of the '
                'land.</li>'
                '<li>Later generations used that clause in ways its authors would not have '
                'recognised.</li></ul>',
     'question_text': 'The student wants to state what survives of the charter without '
                      'overstating it. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'Magna Carta originally had sixty-three clauses, of which three remain law.',
         'Most of the charter’s clauses concern fish weirs, forest law and debts.',
         'One surviving clause promises judgement by one’s peers or by the law of the land.',
         'Three clauses remain law, and what carries the charter’s reputation is one of them — a promise of judgement by peers — put to uses its authors would not have recognised.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Three clauses remain law</strong>… Maqsadda '
                    'ikki talab bor: omon qolganini aytish <em>va</em> uni '
                    'kattalashtirmaslik. Faqat shu variant uchta banddan bittasini '
                    'ajratadi va shuhrat hujjatning oʻzidan emas, keyingi '
                    'foydalanishdan ekanini qoʻshadi. <strong>One surviving clause promises '
                    'judgement by one’s peers</strong>… bandni aytadi, lekin uni '
                    'kimlar va qanday ishlatganini aytmaydi.'},
]
