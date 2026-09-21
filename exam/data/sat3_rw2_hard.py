# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 3 · Reading and Writing, Module 2 (UPPER)
#  27 questions · 32 minutes · taken by a pupil who scored 18+ on rw1.
#
#  Same domains, same counts, same order as the lower module. What changes
#  is the disguise: two-step reasoning, longer syntax, harder vocabulary.
#
#  Load: python manage.py load_mock exam/data/sat3_rw2_hard.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md §3
# ──────────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'Digital SAT — PrimePoint Mock 3',
    'language': 'english',
    'exam_format': 'sat',
    'exam_number': 203,
    'is_published': True,
}

# Copied unchanged into all six files of mock 3.
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
     'passage': '<p>Henrietta Leavitt’s 1912 paper reports a relation between the '
                'period of a Cepheid variable and its brightness, and then stops. The paper '
                'does not ______ the result: it was not her place, under the terms of her '
                'employment at the observatory, to say what the relation implied about '
                'distance.</p>',
     'question_text': WORD_Q,
     'choices': ['defend', 'describe', 'pursue', 'repeat'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>pursue</strong>. Maqola natijani beradi, ammo '
                    'undan keyingi qadamni — masofa haqidagi xulosani — '
                    'tashlamaydi. <strong>describe</strong> notoʻgʻri va matnga zid: '
                    'birinchi jumla aynan maqola natijani <em>tasvirlaganini</em> aytadi.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>For fifty years the Dead Sea Scrolls were held by a small editorial '
                'team that published slowly and refused access to everyone outside it. The '
                'monopoly ended not by agreement but by ______: a library in California '
                'released its own photographs of the scrolls, and within a year the text '
                'was everywhere.</p>',
     'question_text': WORD_Q,
     'choices': ['consensus', 'defiance', 'litigation', 'negotiation'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>defiance</strong>. "not by agreement but by" '
                    'qurilishi boʻshliqqa kelishuvning <em>teskarisini</em> talab qiladi, '
                    'ikki nuqtadan keyingi voqea esa aynan shu: kutubxona ruxsatsiz eʼlon '
                    'qildi. <strong>consensus</strong> va <strong>negotiation</strong> '
                    'ikkalasi ham kelishuvning sinonimi — qurilishning oʻzi ularni '
                    'chiqarib tashlaydi.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>An ordinary mutation that harms the animal carrying it disappears '
                'within a few generations. A gene drive does not: it copies itself onto the '
                'matching chromosome, so that nearly every offspring inherits it, and it '
                'can spread through a population even while it is making that population '
                '______.</p>',
     'question_text': WORD_Q,
     'choices': ['healthier', 'larger', 'older', 'smaller'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>smaller</strong>. Birinchi jumla zararli '
                    'mutatsiya haqida, "even while" esa ziddiyatni kutadi: drayv tarqaladi '
                    '<em>va shu bilan birga</em> populyatsiyaga zarar yetkazadi. '
                    '<strong>larger</strong> ziddiyatni yoʻqotadi — agar populyatsiya '
                    'oʻssa, "even while" qurilishining maʼnosi qolmaydi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>Tycho Brahe measured planetary positions for twenty years and guarded '
                'the results; Kepler, hired as his assistant, was given them a few at a '
                'time. Kepler later wrote that eight minutes of arc, which Tycho’s '
                'instruments could <u>resolve</u> and earlier ones could not, were what '
                'made the circle impossible to keep.</p>',
     'question_text': 'As used in the text, what does the word <u>resolve</u> most nearly '
                      'mean?',
     'choices': ['decide', 'dissolve', 'distinguish', 'settle'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>distinguish</strong>. Gap asboblar haqida, '
                    'obyekt esa burchakning sakkiz daqiqasi: asbob shu qadar kichik farqni '
                    '<em>ajrata oladi</em>. <strong>decide</strong> va '
                    '<strong>settle</strong> "resolve" ning kundalik maʼnolari va shuning '
                    'uchun eng kuchli tuzoqlar — koʻp maʼnoli soʻzda egani va '
                    'toʻldiruvchini qarang.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>Frederick Douglass was invited to speak in Rochester on the fifth of '
                'July, 1852, and he opened by praising the men of 1776 at length and '
                'without irony. Only then did he turn: “This Fourth of July is yours, '
                'not mine.” The speech is remembered for the second half. The first '
                'half is what makes the second half land — an audience that has spent '
                'twenty minutes agreeing cannot easily stop.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that the second half of the speech has been consistently misremembered',
         'To compare Douglass’s oratory with that of other nineteenth-century speakers',
         'To describe the circumstances of Douglass’s invitation to speak in Rochester',
         'To explain how the structure of the speech is what makes its argument effective',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To explain how the</strong>… Matn oxirgi ikki '
                    'jumlada fikrini aytadi: esda qolgani ikkinchi yarmi, lekin uni '
                    'ishlatadigan narsa birinchi yarmi. <strong>To describe the '
                    'circumstances</strong>… birinchi jumladan olingan detal — '
                    'matnning ochilishi uning maqsadi emas.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>Maxwell imagined a creature at a trapdoor between two chambers of gas, '
                'letting the fast molecules through one way and the slow ones the other, '
                'and so making one side hot without any work being done. <u>The demon is '
                'not a thought about gases; it is a thought about information.</u> Leó '
                'Szilárd showed in 1929 that the demon must measure each molecule '
                'before it can sort it, and that the measurement costs precisely what the '
                'sorting gains.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It introduces an example of a system that violates the second law of thermodynamics.',
         'It raises an objection to Maxwell’s argument that the text leaves unanswered.',
         'It restates the description in the previous sentence in more technical vocabulary.',
         'It states the reinterpretation that the rest of the text goes on to support.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>It states the reinterpretation</strong>… Jumla '
                    'mavzuni gazdan axborotga koʻchiradi, keyingi jumla esa aynan shu '
                    'koʻchishni asoslaydi — oʻlchash, yaʼni axborot olish, narx '
                    'talab qiladi. <strong>It restates the description</strong>… '
                    'notoʻgʻri: bu takror emas, yangi daʼvo.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>Economists long used the lighthouse as the standard '
                'example of a good the market cannot supply: a ship that has not paid still '
                'sees the beam, so nobody will build one and everybody wants one. The state '
                'must step in.</p>'
                '<p><b>Text 2</b><br>Ronald Coase went to the archives. English lighthouses '
                'in the seventeenth and eighteenth centuries were built by private parties '
                'under patent and paid for by dues collected at whatever port a ship docked '
                'in. Coase did not claim the market had solved the problem unaided — '
                'the collection of dues was backed by law — but the example, he '
                'argued, had been repeated for two centuries without anyone checking '
                'it.</p>',
     'question_text': 'Based on the texts, Coase’s objection to the standard account '
                      'is best described as',
     'choices': [
         'historical rather than theoretical: the case chosen to illustrate the argument does not fit it.',
         'moral: private provision of safety at sea is preferable to provision by the state.',
         'practical: port dues are cheaper to collect than general taxation is.',
         'theoretical: the concept of a public good is incoherent as economists define it.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>historical rather than theoretical:</strong>… '
                    '2-matn nazariyani rad etmaydi — u arxivga boradi va '
                    '<em>misolning oʻzi</em> notoʻgʻri tanlanganini koʻrsatadi. '
                    '<strong>theoretical: the concept of a public good</strong>… matn buni '
                    'ochiq inkor qiladi: Coase bozor muammoni oʻzi yechgan demaydi.'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>Sor Juana Inés de la Cruz answered the bishop who had told her to '
                'stop writing by writing him a letter of some ten thousand words. The '
                '<i>Respuesta</i> is usually read as a defence of women’s education, '
                'which it is. It is also a demonstration: every claim in it is supported '
                'from scripture, from the church fathers and from the classical authors, by '
                'a woman arguing that women should be permitted to read the very books she '
                'is quoting.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Sor Juana preferred the classical authors to the church fathers as sources.',
         'Sor Juana’s letter persuaded the bishop to withdraw his instruction.',
         'The <i>Respuesta</i> makes its case as much by its manner as by its argument.',
         'The <i>Respuesta</i> was the first defence of women’s education written in the Americas.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>The <i>Respuesta</i> makes its</strong>… Matn '
                    '"is usually read as…which it is. It is <em>also</em>" tuzilishi bilan '
                    'aynan shuni qoʻyadi: xat nafaqat nima deyishi, balki qanday '
                    'yozilgani bilan ham isbotlaydi. <strong>Sor Juana’s letter '
                    'persuaded the bishop</strong>… natija haqida matnda bir soʻz ham '
                    'yoʻq.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>The working group spent fourteen years looking for a boundary: a layer '
                'in rock, ice or mud at which the Anthropocene could be said to begin. They '
                'settled on the plutonium from atmospheric bomb tests, which appears '
                'worldwide within a year or two of 1952 and will stay detectable for a '
                'hundred thousand years. In 2024 the wider commission voted the proposal '
                'down. The objection was not that the layer is absent. It is that a single '
                'mid-century line makes a poor name for a process that began with '
                'agriculture.</p>',
     'question_text': 'According to the text, on what grounds was the proposal rejected?',
     'choices': [
         'The chosen date marks a process that had already been under way for millennia.',
         'The plutonium layer cannot be detected in every part of the world.',
         'The plutonium signal will not remain detectable for long enough.',
         'The working group had taken too long to reach a conclusion.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>The chosen date marks</strong>… Matn oxirgi '
                    'jumlada eʼtirozni oʻzi aytadi: dehqonchilikdan boshlangan jarayonga '
                    'XX asr oʻrtasidagi chiziq nom boʻla olmaydi. <strong>The plutonium '
                    'layer cannot be detected in every part of the world</strong>… '
                    'toʻgʻridan-toʻgʻri zid — matn qatlam butun dunyoda '
                    '<em>borligini</em> aytadi va eʼtiroz unda emasligini taʼkidlaydi.'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A geneticist claims that a gene drive released into a wild population '
                'would be checked not by selection against the drive itself but by the '
                'appearance of resistant sequences the drive cannot cut — which would '
                'mean a drive fails where its molecular target varies, rather than where '
                'its cost to the organism is high.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'geneticist’s claim?',
     'choices': [
         'Drives have been shown to spread through caged populations within ten generations.',
         'Drives spread more slowly in populations that have a longer generation time.',
         'In caged populations, drives collapse first in the cages whose founding mosquitoes carried the greatest variety at the target sequence.',
         'Mosquitoes carrying a drive lay fewer eggs than mosquitoes without one.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>In caged populations, drives</strong>… Daʼvo '
                    'ikki sababni ajratadi: organizmga zarar yoki nishondagi xilma-xillik. '
                    'Faqat shu variant qulashni xilma-xillik bilan bogʻlaydi. '
                    '<strong>Mosquitoes carrying a drive lay fewer eggs</strong>… aksincha '
                    'ishlaydi — u rad etilayotgan "zarar" tushuntirishini '
                    'quvvatlaydi.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A historian argues that Leavitt’s exclusion from interpretation '
                'was institutional rather than personal: the observatory’s women were '
                'hired to measure, and the rule was enforced whatever any individual '
                'computer happened to be capable of seeing.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'historian’s argument?',
     'choices': [
         'Leavitt was deaf, which limited her participation in the observatory’s seminars.',
         'Leavitt’s relation was used within three years to estimate the distance to the Andromeda nebula.',
         'Leavitt’s paper appeared under the name of the observatory’s director.',
         'Observatory records show the same restriction applied to every woman on the staff, including those holding doctorates.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Observatory records show</strong>… Argument '
                    'qoida <em>shaxsga bogʻliq emas</em> deydi, demak dalil uning hammaga, '
                    'jumladan eng malakalilarga ham qoʻllanganini koʻrsatishi kerak. '
                    '<strong>Leavitt was deaf, which limited her participation</strong>… '
                    'aynan teskari yoʻnalish — u chetlatishni shaxsiy holat bilan '
                    'izohlaydi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>In four caged mosquito populations, researchers recorded the number of '
                'distinct sequences present at the drive’s target site when the cage '
                'was founded, and the generation at which the drive stopped spreading.</p>'
                '<table><tr><th>Cage</th><th>Distinct target sequences at start</th>'
                '<th>Generation at which the drive stalled</th></tr>'
                '<tr><td>A</td><td>2</td><td>19</td></tr>'
                '<tr><td>B</td><td>5</td><td>12</td></tr>'
                '<tr><td>C</td><td>9</td><td>8</td></tr>'
                '<tr><td>D</td><td>14</td><td>5</td></tr></table>',
     'question_text': 'A student concludes that the more variety a cage began with at the '
                      'target site, the sooner its drive stalled. Which choice best '
                      'describes data from the table that support this conclusion?',
     'choices': [
         'Cage C began with nine distinct sequences at the target site.',
         'Every drive in the experiment stalled before generation 20.',
         'The drive in cage D stalled at generation 5.',
         'The drive stalled earlier as the number of distinct sequences rose, from generation 19 in cage A (2 sequences) to generation 5 in cage D (14).',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The drive stalled earlier</strong>… Xulosa ikki '
                    'kattalikning teskari bogʻliqligi haqida, shuning uchun dalil ham '
                    'ikkalasini butun jadval boʻylab olishi kerak. Qolgan uchtasi rost, '
                    'lekin har biri bitta katakda qoladi — <strong>The drive in cage '
                    'D stalled at generation 5</strong> xilma-xillik haqida hech narsa '
                    'demaydi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>Szilárd’s result is that the demon’s measurement carries '
                'a thermodynamic cost, and Landauer later located that cost precisely: not '
                'in the measuring but in the erasing, at the moment the demon clears its '
                'memory to make room for the next molecule. A demon with unlimited memory '
                'would therefore ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'be unable to sort the molecules at all.',
         'cool both chambers rather than heating one of them.',
         'need to measure each molecule twice over.',
         'violate the second law for as long as its memory lasted.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>violate the second law</strong>… Matn narxni '
                    'aniq joyga qoʻyadi: oʻchirishga. Xotira tugamasa, oʻchirish ham '
                    'boʻlmaydi — demak narx toʻlanmaydi, va u toʻlanmaguncha qonun '
                    'buziladi. <strong>be unable to sort the molecules at all</strong> '
                    'matnga zid: saralashga xalaqit beradigan narsa xotira emas.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>An orator who denounces an audience at the opening has, by the second '
                'paragraph, an audience that is defending itself. Douglass spent the first '
                'half of the Rochester speech granting everything his listeners believed '
                'about 1776, so that when the turn finally came they had no position left '
                'to retreat into: the ground they would have argued from was ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'ground he had explicitly refused to occupy.',
         'ground they had just heard him praise.',
         'unfamiliar to most of those present.',
         'weaker than the ground he had chosen for himself.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>ground they had</strong>… Matn mexanizmni '
                    'beradi: Douglass tinglovchilar ishonadigan hamma narsani <em>oʻzi</em> '
                    'maqtagan, shuning uchun ular chekinadigan joy uning oʻz soʻzlari '
                    'boʻlib qoladi. <strong>ground he had explicitly refused to '
                    'occupy</strong> aynan teskari — u undan voz kechmagan, uni egallab '
                    'olgan.'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Leavitt’s relation — the link between a Cepheid’s period '
                'and its true ______ made it possible for the first time to measure the '
                'distance to another galaxy.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['brightness', 'brightness —', 'brightness,', 'brightness;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>brightness —</strong>. Qoʻshimcha izoh tire '
                    'bilan <em>ochilgan</em>, demak tire bilan yopilishi kerak: juftlik bir '
                    'xil belgilardan tuziladi. <strong>brightness,</strong> eng koʻp '
                    'tanlanadigan xato — vergul va tire juftlik hosil qilmaydi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>Sor Juana supports every claim from three ______ scripture, which she '
                'quotes at length; the church fathers; and the classical authors.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['sources', 'sources,', 'sources:', 'sources;'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>sources:</strong>. Ikki nuqta toʻliq gapdan '
                    'keyin sanashni kiritadi — va bu yerda u ayniqsa zarur, chunki '
                    'sanash aʼzolarining ichida allaqachon vergul bor, shuning uchun '
                    'aʼzolar nuqtali vergul bilan ajratilgan. <strong>sources,</strong> '
                    'sanashni oldingi vergullar bilan aralashtirib yuboradi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>In 2024 the commission voted the proposal ______ which had taken the '
                'working group fourteen years to prepare.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['down', 'down,', 'down:', 'down;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>down,</strong>. "which had taken…to prepare" '
                    '— ajratilgan (qoʻshimcha) aniqlovchi ergash gap: u gapning '
                    'maʼnosini toraytirmaydi, faqat izoh beradi, shuning uchun vergul bilan '
                    'ajratiladi. <strong>down;</strong> notoʻgʻri: nuqtali vergul ikki '
                    'mustaqil gap orasida turadi, "which…" esa mustaqil emas.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Among the objections raised against the proposal ______ one the working '
                'group had anticipated from the beginning.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are', 'have been', 'was', 'were'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>was</strong>. Gap teskari tartibda: ega feʼldan '
                    'keyin keladi va u — <em>one</em>, birlik. Boshdagi "Among the '
                    'objections…proposal" faqat oʻrin holi. <strong>were</strong> eng koʻp '
                    'tanlanadigan xato: quloq yaqin turgan koʻplik "objections" ga '
                    'moslashadi, lekin u ega emas.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>The bishop’s instruction was that Sor Juana ______ from writing '
                'altogether.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['is refraining', 'refrain', 'refrained', 'refrains'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>refrain</strong>. Buyruq-talab bildiruvchi '
                    'otdan keyin ("the instruction was that…") ingliz tilida '
                    'buyruq-istak shakli keladi: feʼl asos shaklida turadi, shaxs va '
                    'sondan qatʼi nazar. <strong>refrained</strong> quloqqa toʻgʻriroq '
                    'eshitiladi va aynan shuning uchun eng koʻp tanlanadi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>The plutonium signal is more widely distributed than ______ of any '
                'other candidate marker.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['that', 'them', 'they', 'those'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>that</strong>. Taqqoslanayotgan narsa — '
                    '<em>signal</em>, birlik, demak uning oʻrnini birlik olmosh bosadi. '
                    '<strong>those</strong> koʻplikni bildiradi va bu yerda egasi yoʻq; '
                    '<strong>them</strong> esa taqqoslash emas, toʻldiruvchi shakli.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Coase’s method was to name the example that everyone repeated, to '
                'go to the archives, and ______</p>',
     'question_text': CONVENTION_Q,
     'choices': ['a check of what he found there.', 'checking what he found there.',
                 'he checked what he found there.', 'to check what he found there.'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>to check what</strong>… Qator "to name…to go…'
                    'and ___" — ikkitasi ham <em>to</em> + feʼl, demak uchinchisi ham '
                    'shunday boʻlishi shart (parallelizm). <strong>checking what he found '
                    'there.</strong> maʼnoni buzmaydi va aynan shuning uchun xavfli, lekin '
                    'u qatorning shaklini sindiradi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>A gene drive spreads through a population even when it harms the '
                'animals carrying it. ______ it can be stopped by a single change in the '
                'sequence it is built to cut.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['All the same,', 'Consequently,', 'In other words,', 'Similarly,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>All the same,</strong>. Birinchi jumla '
                    'drayvning kuchi haqida, ikkinchisi esa kutilmagan zaifligi haqida '
                    '— qarama-qarshilik. <strong>Consequently,</strong> aynan teskari '
                    'bogʻlanish va eng koʻp tanlanadigan xato.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>Kepler tried for years to fit a circle to Tycho’s observations of '
                'Mars. ______ he gave the circle up, and found that an ellipse fitted at '
                'once.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Eventually,', 'Likewise,', 'Meanwhile,', 'Therefore,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Eventually,</strong>. Ikki jumla orasidagi bogʻ '
                    '— <em>vaqt</em>: uzoq urinishdan keyin voz kechish. '
                    '<strong>Meanwhile,</strong> bir vaqtda sodir boʻlishni bildiradi, bu '
                    'yerda esa hodisalar ketma-ket; <strong>Therefore,</strong> esa '
                    'urinishni voz kechishning sababi qilib qoʻyadi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>For two centuries the lighthouse served as the textbook case of a good '
                'the market cannot supply. ______ Coase found in the archives that English '
                'lighthouses had been built and run by private parties for much of that '
                'time.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'Consequently,', 'However,', 'Similarly,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>However,</strong>. Darslikdagi daʼvo va '
                    'arxivdagi fakt bir-biriga zid. <strong>Accordingly,</strong> va '
                    '<strong>Consequently,</strong> ikkalasi ham natija bildiradi — '
                    'ular ikkinchi jumlani birinchisidan <em>kelib chiqadi</em> deb '
                    'qoʻyadi, aslida u uni yiqitadi.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Henrietta Leavitt worked as a computer at the Harvard College '
                'Observatory.</li>'
                '<li>The observatory’s women were hired to measure, not to '
                'interpret.</li>'
                '<li>Her 1912 paper reports a relation between a Cepheid’s period and '
                'its brightness.</li>'
                '<li>The paper does not draw out what the relation implies about '
                'distance.</li>'
                '<li>Within a decade the relation was being used to measure the distance to '
                'other galaxies.</li></ul>',
     'question_text': 'The student wants to emphasize the gap between what Leavitt found '
                      'and what she was permitted to say. Which choice most effectively '
                      'uses relevant information from the notes to accomplish this goal?',
     'choices': [
         'Henrietta Leavitt worked as a computer at the Harvard College Observatory.',
         'Leavitt found the relation that would be used within a decade to measure the distance to other galaxies, but her paper stops short of saying so: the observatory’s women were hired to measure, not to interpret.',
         'Leavitt’s 1912 paper reports a relation between a Cepheid’s period and its brightness.',
         'The women employed at the observatory were hired to measure rather than to interpret.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Leavitt found the relation</strong>… Maqsad '
                    '<em>tafovutni</em> koʻrsatish, demak javobda ikkala tomon ham '
                    'boʻlishi shart: kashfiyotning qiymati va aytishga ruxsat '
                    'yoʻqligi. <strong>The women employed at the observatory were hired to '
                    'measure</strong>… faqat cheklovni aytadi — taqqoslanadigan '
                    'ikkinchi tomonsiz tafovut hosil boʻlmaydi.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Maxwell imagined a creature sorting fast and slow molecules through a '
                'trapdoor.</li>'
                '<li>Sorting them would make one chamber hot without any work being '
                'done.</li>'
                '<li>Szilárd showed in 1929 that the demon must measure each '
                'molecule.</li>'
                '<li>Landauer showed that the cost lies in erasing the memory, not in '
                'measuring.</li>'
                '<li>The erasure costs exactly what the sorting gains.</li></ul>',
     'question_text': 'The student wants to explain the resolution of the puzzle to a '
                      'reader who already knows the puzzle itself. Which choice most '
                      'effectively uses relevant information from the notes to accomplish '
                      'this goal?',
     'choices': [
         'Maxwell imagined a creature sorting fast and slow molecules through a trapdoor between two chambers.',
         'Sorting the molecules would make one chamber hot without any work being done.',
         'Szilárd showed in 1929 that the demon must measure each molecule before it can sort it.',
         'The demon must store what it measures, and erasing that memory to make room costs exactly what the sorting gains — which is how the second law survives.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The demon must store</strong>… Oʻquvchi '
                    'jumboqni biladi, demak takrorlash kerak emas — kerak boʻlgani '
                    '<em>yechim</em>: narx qayerda va u nimani qutqaradi. '
                    '<strong>Szilárd showed in 1929 that the demon must '
                    'measure</strong>… yechimning faqat birinchi yarmini beradi va eng '
                    'kuchli tuzoq; oʻchirish bahosi aytilmasa, ikkinchi qonun nega '
                    'saqlanib qolgani noaniq qoladi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>The lighthouse was the standard textbook example of a good the market '
                'cannot supply.</li>'
                '<li>Coase went to the archives of the English lighthouses.</li>'
                '<li>Seventeenth- and eighteenth-century lighthouses were built by private '
                'parties under patent.</li>'
                '<li>They were paid for by dues collected at the port a ship docked in.</li>'
                '<li>Coase noted that the collection of the dues was backed by law.</li></ul>',
     'question_text': 'The student wants to state Coase’s objection precisely, without '
                      'overstating it. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'Coase found that English lighthouses were built privately and paid for by port dues — though the dues were collected with the backing of law, so the example was chosen carelessly rather than the state being unnecessary.',
         'Coase went to the archives of the English lighthouses to see how they had been paid for.',
         'English lighthouses were built by private parties under patent and paid for by dues collected at port.',
         'The lighthouse was the standard textbook example of a good that the market cannot supply.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Coase found that</strong>… Maqsadda ikki talab '
                    'bor: eʼtirozni aytish <em>va</em> uni kuchaytirib yubormaslik. Faqat '
                    'shu variant qonun tayanchini ham eslatib, xulosani "misol notoʻgʻri '
                    'tanlangan" darajasida ushlab turadi. <strong>English lighthouses were '
                    'built by private parties under patent</strong>… qonun haqidagi '
                    'shartni tashlab ketadi va shu bilan eʼtirozni bozor davlatni '
                    'butunlay almashtiradi degan darajaga koʻtaradi.'},
]
