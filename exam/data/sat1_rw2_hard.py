# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 1 · Reading and Writing, Module 2 (UPPER)
#  27 questions · 32 minutes · taken by a pupil who scored 18+ on rw1.
#
#  Same domains, same counts, same order as the lower module. What changes
#  is the disguise: two-step reasoning, longer syntax, harder vocabulary,
#  and a passage whose point is made by its last clause.
#
#  Load: python manage.py load_mock exam/data/sat1_rw2_hard.py --expect-questions=27
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
     'passage': '<p>An octopus arm contains more neurons than the animal’s central '
                'brain, and an arm severed from the body will still reach for food and '
                'pass it toward a mouth that is no longer there. Neuroscientists '
                'therefore describe octopus cognition as ______: the deciding is spread '
                'through the body rather than issued from one place.</p>',
     'question_text': WORD_Q,
     'choices': ['decentralized', 'hierarchical', 'instinctive', 'rudimentary'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>decentralized</strong>. Ikki nuqtadan keyingi '
                    'qism taʼrifni oʻzi beradi: qaror bitta markazdan chiqmaydi, tanaga '
                    'tarqalgan. <strong>hierarchical</strong> aynan teskari maʼno va eng '
                    'kuchli tuzoq, chunki "nerv tizimi" mavzusi talabaga tartib-ierarxiyani '
                    'eslatadi.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>Zora Neale Hurston trained as an anthropologist under Franz Boas, and '
                'the folklore she collected in Florida entered her fiction largely '
                '______ — not smoothed into standard English for an outside reader, '
                'but set down in the cadences in which she had heard it spoken.</p>',
     'question_text': WORD_Q,
     'choices': ['inadvertently', 'posthumously', 'reluctantly', 'unaltered'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>unaltered</strong>. Tiredan keyingi qism '
                    'boʻshliqni izohlaydi: "not smoothed into standard English" — yaʼni '
                    '<em>oʻzgartirilmagan</em> holda. <strong>inadvertently</strong> '
                    '(beixtiyor) notoʻgʻri: matn buni ongli tanlov sifatida koʻrsatadi.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>Ulugʻbek’s star catalogue remained the most accurate in the '
                'world for nearly two centuries. European astronomers who had never read '
                'a word of Persian nevertheless ______ its figures, which reached them '
                'through a Latin translation printed at Oxford in 1665.</p>',
     'question_text': WORD_Q,
     'choices': ['adopted', 'commissioned', 'disputed', 'overlooked'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>adopted</strong>. "nevertheless" tilni bilmaslik '
                    'bilan foydalanishni qarama-qarshi qoʻyadi — demak ular raqamlarni '
                    '<em>qabul qilgan</em>. <strong>commissioned</strong> (buyurtma bergan) '
                    'notoʻgʻri: katalog ulardan ikki asr oldin tuzilgan, buyurtma qilib '
                    'boʻlmaydi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>Reef-building corals live with algae inside their own cells, and the '
                'arrangement is usually called a partnership. Under prolonged heat, '
                'though, the algae begin releasing compounds that damage the coral’s '
                'tissue, and the coral expels them. What looks like a collapse of '
                'cooperation is better read as the coral <u>terminating</u> an '
                'arrangement that has stopped paying.</p>',
     'question_text': 'As used in the text, what does the word <u>terminating</u> most '
                      'nearly mean?',
     'choices': ['concealing', 'ending', 'renegotiating', 'resuming'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>ending</strong>. Matn "the coral expels them" '
                    'deydi — sherikchilik davom etmaydi, tugatiladi. '
                    '<strong>renegotiating</strong> juda jozibali tuzoq, chunki "arrangement" '
                    'va "stopped paying" shartnoma tilini eslatadi; ammo marjon qayta '
                    'kelishmaydi, u chiqarib tashlaydi.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>In <i>The Federalist</i> No. 51, James Madison defends the separation '
                'of powers not by appealing to the virtue of officeholders but by '
                'assuming its absence. “If men were angels,” he writes, '
                '“no government would be necessary.” The remedy he proposes is '
                'structural rather than moral: “Ambition must be made to counteract '
                'ambition.” A constitution, on this view, should be built to work '
                'even when the people running it are not trying to make it work.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To contrast Madison’s view of government with the views held by his contemporaries',
         'To explain the assumption about human nature on which Madison’s argument for separated powers rests',
         'To question whether structural safeguards can in fact restrain ambitious officeholders',
         'To trace the influence of <i>The Federalist</i> on later constitutional practice',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>To explain the assumption</strong>… Matn '
                    'Madisonning dalilini emas, uning <em>asosidagi farazni</em> ochadi: '
                    'odamlar farishta emas, shuning uchun tuzilma kerak. <strong>To question '
                    'whether structural safeguards</strong>… notoʻgʻri: matn hech qayerda '
                    'shubha bildirmaydi, u tushuntiradi.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>For most of the twentieth century, laboratory work on invertebrate '
                'behaviour proceeded on the assumption that a nervous system without a '
                'cortex could not support anything worth calling cognition. <u>The '
                'octopus was the standing exception that no one could quite explain '
                'away.</u> It solves mechanical problems it has never met before, it '
                'tells one keeper from another, and it does both with a nervous system '
                'built on a plan nothing like a vertebrate’s.</p>',
     'question_text': 'Which choice best describes the function of the underlined '
                      'sentence in the text as a whole?',
     'choices': [
         'It concedes a limitation in the laboratory work described in the previous sentence.',
         'It draws a conclusion from the evidence presented in the final sentence.',
         'It identifies the case that resisted the assumption just described, which the rest of the text then illustrates.',
         'It offers a hypothesis that the evidence in the final sentence goes on to disprove.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>It identifies the case</strong>… Jumla ikki '
                    'qismni ulaydi: oldida faraz, keyin esa oʻsha farazga sigʻmagan '
                    'misolning dalillari. <strong>It draws a conclusion from the evidence '
                    'presented in the final sentence</strong> notoʻgʻri, chunki tartib '
                    'teskari — dalil jumladan <em>keyin</em> keladi, demak u xulosa emas, '
                    'daʼvo.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>Economists long predicted that volunteer software '
                'would be undersupplied. Writing code is costly, and the result is free '
                'to everyone, including those who contribute nothing. By the standard '
                'account of public goods, projects on the scale of the Linux kernel '
                'should be rare.</p>'
                '<p><b>Text 2</b><br>Rebecca Ottinger argues that the prediction '
                'mismodelled the cost. For the firms that supply most kernel code, the '
                'software is not a donation but an input they need in any case; '
                'releasing it spreads the work of maintaining it across everyone who '
                'uses it. The puzzle is not why such firms give the code away. It is why '
                'they would keep it.</p>',
     'question_text': 'Based on the texts, Ottinger would most likely characterize the '
                      'prediction described in Text 1 as resting on',
     'choices': [
         'a failure to distinguish between software licences of different kinds.',
         'a mistaken assumption that releasing code is a net cost to the contributor.',
         'an overestimate of the number of firms willing to support volunteer projects.',
         'an underestimate of how difficult a large software project is to maintain.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>a mistaken assumption that</strong>… 1-matn '
                    '"writing code is costly" deb boshlaydi; Ottinger aynan shu xarajat '
                    'hisobini notoʻgʻri deydi — firma uchun kod baribir kerak, tarqatish esa '
                    'yukni <em>kamaytiradi</em>. <strong>an underestimate of how '
                    'difficult</strong>… teskari yoʻnalish: Ottinger qiyinchilikni emas, '
                    'xarajatning kimga tushishini qayta hisoblaydi.'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>Toni Morrison often said that she wrote the books she wanted to read '
                'and could not find. The remark is usually quoted as a statement about '
                'whose lives appear in fiction. It is also a statement about form. The '
                'novels do not explain their world to an outsider: <i>Beloved</i> opens '
                'in the middle of a household’s private knowledge and expects the '
                'reader to catch up, because a book written for a reader who already '
                'belongs does not stop to translate.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         '<i>Beloved</i> proved more difficult for critics to interpret than Morrison’s earlier novels.',
         'Morrison believed that questions of representation in fiction had been insufficiently studied.',
         'Morrison’s familiar remark describes a choice about form as much as a choice of subject.',
         'Morrison wrote chiefly for readers unfamiliar with the communities her novels depict.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Morrison’s familiar remark describes</strong>… '
                    'Matn "usually quoted as…It is <em>also</em>" tuzilishi bilan aynan shuni '
                    'aytadi: gap faqat mavzu emas, shakl haqida ham. <strong>Morrison wrote '
                    'chiefly for readers unfamiliar</strong>… toʻgʻridan-toʻgʻri teskari: '
                    'matn "a reader who already belongs" deydi.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>Ibn Sina’s <i>Canon of Medicine</i> was a teaching text, and its '
                'arrangement shows it. Symptoms are grouped not by the organ affected '
                'but by the reasoning a physician must perform to tell one cause from '
                'another: two diseases that present alike sit side by side, with the '
                'single sign that separates them set out between them. The book was used '
                'in European universities into the seventeenth century, long after much '
                'of its physiology had been abandoned. The method outlasted the '
                'content.</p>',
     'question_text': 'According to the text, what accounts for the <i>Canon</i>’s '
                      'long use in European universities?',
     'choices': [
         'It covered a wider range of diseases than any competing text.',
         'Its arrangement trained physicians to distinguish between conditions that resemble each other.',
         'Its physiological claims were confirmed by later anatomical research.',
         'It was one of the few medical works available in Latin translation.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Its arrangement trained physicians</strong>… '
                    'Oxirgi jumla javobni beradi: "the method outlasted the content" — yaʼni '
                    'saqlanib qolgani usul, yaʼni tuzilish. <strong>Its physiological claims '
                    'were confirmed</strong>… matnga toʻgʻridan-toʻgʻri zid: fiziologiya '
                    '<em>rad etilgan</em> deyilgan.'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A marine biologist hypothesizes that a coral expels its algae under '
                'heat stress because the algae have become harmful to it, rather than '
                'because the heat has destroyed the coral’s ability to hold on to '
                'them.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'biologist’s hypothesis?',
     'choices': [
         'Algae removed from a bleached coral remain alive in seawater for several days.',
         'Bleached corals can be recolonized by algae once the surrounding water cools.',
         'Colonies hosting algae engineered to release fewer damaging compounds keep them at temperatures that make other colonies bleach.',
         'Corals in shaded parts of a reef begin to bleach later than corals in direct sunlight.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Colonies hosting algae engineered</strong>… '
                    'Gipoteza ikki sababni ajratadi: suv oʻti zararli boʻlib qoldimi yoki '
                    'marjon ushlay olmay qoldimi. Bu tajribada harorat bir xil, faqat suv '
                    'oʻtining zarari oʻzgargan — va natija oʻzgaradi, demak sabab suv oʻtida. '
                    '<strong>Bleached corals can be recolonized</strong>… qaytish haqida, '
                    'chiqarib tashlash sababi haqida emas.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A scholar claims that Hurston’s fieldwork shaped the <i>form</i> '
                'of her fiction and not only its content — that she built scenes the '
                'way a story is told aloud, with a listener present and answering.</p>',
     'question_text': 'Which feature of Hurston’s novel <i>Their Eyes Were Watching '
                      'God</i> would, if accurately described, most directly support the '
                      'scholar’s claim?',
     'choices': [
         'The novel is set in Eatonville, Florida, the town where Hurston herself grew up.',
         'The novel reproduces the dialect Hurston recorded during her fieldwork.',
         'The novel was published in 1937, several years after her fieldwork had ended.',
         'The novel’s events reach the reader as a story Janie tells to a single listener, who responds as she speaks.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The novel’s events reach</strong>… Daʼvo '
                    'aynan <em>shakl</em> haqida: sahna ogʻzaki hikoya kabi, tinglovchi bilan '
                    'qurilgan. <strong>The novel reproduces the dialect</strong>… eng kuchli '
                    'tuzoq — u ham dala ishidan kelgan, lekin bu <em>til</em>, yaʼni mazmun '
                    'tomoni; olim esa uni ataylab "not only its content" deb chiqarib '
                    'tashlagan.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>After a marine heatwave, researchers surveyed four reefs, recording '
                'the mean daily temperature range each reef normally experiences and the '
                'share of its colonies that bleached.</p>'
                '<table><tr><th>Reef</th><th>Mean daily temperature range (°C)</th>'
                '<th>Colonies bleached (%)</th></tr>'
                '<tr><td>A</td><td>0.4</td><td>71</td></tr>'
                '<tr><td>B</td><td>1.1</td><td>48</td></tr>'
                '<tr><td>C</td><td>2.3</td><td>22</td></tr>'
                '<tr><td>D</td><td>3.0</td><td>19</td></tr></table>',
     'question_text': 'A student concludes that corals living where the daily temperature '
                      'swing is larger were more resistant to bleaching. Which choice '
                      'best describes data from the table that support this conclusion?',
     'choices': [
         'All four reefs had at least some colonies that bleached.',
         'Fewer than a quarter of the colonies at Reef C bleached.',
         'Reef B experienced a mean daily temperature range of 1.1°C.',
         'Reef D, with the largest daily range, had the smallest share of bleached colonies, and Reef A, with the smallest range, had the largest.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Reef D, with the</strong>… Xulosa ikki kattalik '
                    'orasidagi bogʻliqlik haqida, shuning uchun dalil ham ikkalasini birga '
                    'olishi shart — bu yerda ikki chekka nuqta qarama-qarshi qoʻyilgan. '
                    '<strong>Fewer than a quarter of the colonies at Reef C</strong>… '
                    'jadvalga koʻra rost, lekin bitta qator hech qanday bogʻliqlikni '
                    'koʻrsatmaydi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>A model that predicts reoffending can be <i>calibrated</i> — '
                'meaning that of the people it scores at 40 per cent, about 40 per cent '
                'do reoffend — and can at the same time produce different '
                'false-positive rates for two groups. Where the underlying rates of '
                'reoffending differ between the groups, the two properties cannot both '
                'hold. A designer who insists on calibration is therefore ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'accepting, as a consequence, unequal false-positive rates between the groups.',
         'ensuring that the model will not take group membership as an input.',
         'guaranteeing that the model’s predictions will be accurate for every group.',
         'removing the need to measure the model’s error rates separately.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>accepting, as a consequence,</strong>… Matn '
                    '"cannot both hold" deydi: ikki xossa bir vaqtda boʻlmaydi, demak '
                    'birini tanlagan odam ikkinchisidan voz kechadi. <strong>guaranteeing '
                    'that the model’s predictions</strong>… kalibrlanganlikni '
                    '"aniqlik" deb tushunish — bu matn bergan taʼrifga mos emas.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>The rock record is not a film but a set of stills. Sediment gathers '
                'only where it is not being scoured away, and the surfaces where nothing '
                'was laid down — or where what was laid down has since been removed '
                '— look, in a cliff face, exactly like the ordinary surfaces between '
                'one bed and the next. A geologist reading a cliff therefore cannot '
                'assume that ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'the beds were laid down by the same process throughout.',
         'the oldest rocks in the sequence lie at its base.',
         'the sequence contains any fossils at all.',
         'the thickness of a bed is proportional to the length of time it represents.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>the thickness of a</strong>… Matnning butun '
                    'gapi shu: koʻrinmas yuzada millionlab yil yoʻqolgan boʻlishi mumkin, '
                    'demak qalinlikni vaqtga aylantirib boʻlmaydi. <strong>the oldest rocks '
                    'in the sequence lie at its base</strong> tuzoq: bu geologiyaning haqiqiy '
                    'qoidasi va matn uni buzmaydi — matn <em>vaqt</em> haqida gapiradi, '
                    'tartib haqida emas.'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Morrison’s <i>Beloved</i>, which opens in the middle of a '
                'household’s private ______ expects the reader to catch up rather '
                'than pausing to explain.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['knowledge', 'knowledge,', 'knowledge:', 'knowledge;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>knowledge,</strong>. "which opens…knowledge" — '
                    'ajratilgan aniqlovchi ergash gap, u vergul bilan ochilgan, demak vergul '
                    'bilan yopiladi. <strong>knowledge;</strong> notoʻgʻri: nuqtali vergul '
                    'ikki mustaqil gapni ajratadi, bu yerda esa ergash gap tugayapti.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>Hurston’s Florida fieldwork ended in the early ______ however, '
                'the notebooks she had filled went on feeding her fiction for another '
                'decade.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['1930s', '1930s,', '1930s;', '1930s and'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>1930s;</strong>. <em>however</em> bogʻlovchi emas, '
                    'kirish soʻz: u ikki mustaqil gapni ulay olmaydi, shuning uchun ular '
                    'orasida nuqtali vergul kerak (keyin esa vergul). <strong>1930s,</strong> '
                    '— comma splice va bu savolning butun tuzogʻi: "however" quloqqa '
                    'bogʻlovchidek eshitiladi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>Ulugʻbek’s catalogue recorded, for each of its 1,018 stars, '
                'three ______ its longitude, measured along the ecliptic; its latitude; '
                'and its magnitude.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['quantities', 'quantities,', 'quantities:', 'quantities;'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>quantities:</strong>. Ikki nuqta toʻliq gapdan '
                    'keyin sanashni kiritadi — va bu yerda u ayniqsa zarur, chunki sanash '
                    'aʼzolari ichida allaqachon vergul bor, shuning uchun ular nuqtali vergul '
                    'bilan ajratilgan. <strong>quantities,</strong> sanashni oldingi vergullar '
                    'bilan aralashtirib yuboradi.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Among the manuscripts recovered from the observatory library ______ '
                'three copies of the catalogue, each in a different hand.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['has been', 'is', 'was', 'were'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>were</strong>. Gap teskari tartibda: ega feʼldan '
                    'keyin keladi va u — <em>three copies</em>, koʻplik. Boshdagi "Among the '
                    'manuscripts…library" faqat oʻrin holi, ega emas. SAT bu savolni aynan '
                    'shu teskari tartib uchun quradi.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>Madison argues that if men ______ angels, no government would be '
                'necessary at all.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are', 'had been', 'was', 'were'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>were</strong>. Bu haqiqatga zid shart '
                    '(odamlar farishta emas), ingliz tilida esa bunday shart ikkinchi turdagi '
                    'shart gapda <em>were</em> ni talab qiladi — shaxsdan qatʼi nazar. '
                    'Ikkinchi qismdagi "would be" shu turni koʻrsatib turibdi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>A reef-building coral and ______ algae exchange nutrients '
                'continuously, each supplying what the other cannot make for itself.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['it’s', 'its', 'their', 'they’re'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>its</strong>. Suv oʻtlari bitta marjonga tegishli, '
                    'marjon esa birlikda ("A reef-building coral"), demak egalik olmoshi ham '
                    'birlik. <strong>their</strong> tuzoq: talaba feʼlni ("exchange") koʻplik '
                    'deb koʻradi — lekin feʼl <em>ikkala</em> tomonga tegishli, olmosh esa '
                    'faqat marjonga.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>______ the octopus’s nervous system challenges the long-held '
                'assumption that intelligence requires a cortex.</p>',
     'question_text': CONVENTION_Q,
     'choices': [
         'Having organized on a plan nothing like a vertebrate’s,',
         'Organized on a plan nothing like a vertebrate’s,',
         'Organizing on a plan nothing like a vertebrate’s,',
         'To organize on a plan nothing like a vertebrate’s,',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Organized on a</strong>… Boshlanuvchi ibora '
                    'egani ("nervous system") aniqlashi kerak, tizim esa <em>qurilgan</em> — '
                    'majhul maʼno, demak III shakl. <strong>Organizing on a</strong>… aniq '
                    'nisbatni bildiradi, yaʼni nerv tizimi kimnidir tashkil qilayotgan boʻlib '
                    'chiqadi — mantiqan notoʻgʻri egaga osilib qolgan aniqlovchi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>A calibrated model tells the truth on average about the population it '
                'scores. ______ it can still be wrong in systematically different ways '
                'about two groups inside that population.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['For instance,', 'Nevertheless,', 'Similarly,', 'Therefore,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Nevertheless,</strong>. Birinchi jumla '
                    'ishonchlilik, ikkinchisi esa kutilmagan kamchilik haqida — qarama-'
                    'qarshilik. <strong>Therefore,</strong> aynan teskari bogʻlanish va eng '
                    'koʻp tanlanadigan xato: "tells the truth" talabani ijobiy natija '
                    'kutishga undaydi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>Ottinger argues that for the firms supplying most kernel code the '
                'software is an input they need in any case. ______ a company running '
                'thousands of servers must have a working kernel whether or not anyone '
                'outside it ever sees the patches.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['For example,', 'In contrast,', 'Nevertheless,', 'Previously,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>For example,</strong>. Ikkinchi jumla umumiy '
                    'fikrni takrorlamaydi va unga qarshi turmaydi — u bitta aniq holatni '
                    'koʻrsatadi, yaʼni misol. <strong>Nevertheless,</strong> qarama-qarshilik '
                    'talab qiladi, bu yerda esa ikkala jumla bir tomonga qaraydi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>Ibn Sina grouped diseases by the reasoning needed to tell them apart '
                'rather than by the organ affected. ______ a student working through the '
                '<i>Canon</i> was practising diagnosis, not memorizing a catalogue.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['As a result,', 'By contrast,', 'For example,', 'Nevertheless,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>As a result,</strong>. Kitobning tuzilishi — '
                    'sabab, talabaning tashxis mashq qilishi — oʻsha tuzilishdan kelib '
                    'chiqadigan natija. <strong>By contrast,</strong> tuzoq, chunki jumlada '
                    '"not memorizing" degan zidlov bor; lekin u <em>jumla ichidagi</em> '
                    'zidlov, ikki jumla orasidagi munosabat emas.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Ulugʻbek built an observatory at Samarkand in the 1420s.</li>'
                '<li>Its main instrument was a stone sextant about 40 metres in '
                'radius.</li>'
                '<li>The observatory had no lenses of any kind; the telescope had not '
                'yet been invented.</li>'
                '<li>Its catalogue gave positions for 1,018 stars.</li>'
                '<li>Its value for the length of the year differs from the modern one by '
                'less than a minute.</li></ul>',
     'question_text': 'The student wants to emphasize the accuracy the astronomers '
                      'achieved relative to the instruments available to them. Which '
                      'choice most effectively uses relevant information from the notes '
                      'to accomplish this goal?',
     'choices': [
         'The observatory’s main instrument was a stone sextant about 40 metres in radius.',
         'The telescope had not yet been invented when the observatory at Samarkand was built.',
         'Ulugʻbek’s observatory, built at Samarkand in the 1420s, catalogued the positions of 1,018 stars.',
         'Working without a lens of any kind, Ulugʻbek’s astronomers measured the length of the year to within a minute of the value accepted today.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Working without a lens</strong>… Maqsad ikki '
                    'narsani <em>bir jumlada</em> qarshi qoʻyishni talab qiladi: vosita '
                    '(linza yoʻq) va natija (bir daqiqagacha aniq). Qolgan uchtasi qaydlardan '
                    'faqat bittasini oladi — <strong>The telescope had not yet been '
                    'invented</strong> vositani aytadi, lekin natijani aytmaydi, shuning '
                    'uchun taqqoslash hosil boʻlmaydi.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Reef-building corals host algae inside their own cells.</li>'
                '<li>The algae supply much of the coral’s energy.</li>'
                '<li>Under prolonged heat the algae release compounds that damage coral '
                'tissue.</li>'
                '<li>The coral then expels the algae.</li>'
                '<li>A coral without its algae looks pale, and is described as '
                'bleached.</li></ul>',
     'question_text': 'The student wants to emphasize that bleaching is something the '
                      'coral does rather than something that simply happens to it. Which '
                      'choice most effectively uses relevant information from the notes '
                      'to accomplish this goal?',
     'choices': [
         'A coral that has expelled its algae looks pale, which is why the process is called bleaching.',
         'Prolonged heat changes the compounds that algae release inside a coral’s cells.',
         'Reef-building corals host algae in their own cells, and those algae supply much of the coral’s energy.',
         'Under prolonged heat the algae begin damaging the coral’s tissue, and the coral expels them.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Under prolonged heat the</strong>… Maqsad '
                    '<em>kim harakat qilayotganini</em> koʻrsatish, va faqat shu variantda '
                    'marjon ega boʻlib turibdi: u chiqarib tashlaydi. <strong>A coral that '
                    'has expelled its algae looks pale</strong>… nomni izohlaydi, harakatni '
                    'emas; <strong>Prolonged heat changes the compounds</strong>… esa egani '
                    'issiqlikka beradi — aynan taʼkidlanmasligi kerak boʻlgan narsa.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>A model is <i>calibrated</i> if, of those it scores at 40 per cent, '
                'about 40 per cent reoffend.</li>'
                '<li>Two groups may reoffend at different underlying rates.</li>'
                '<li>A single model can be calibrated for both groups at once.</li>'
                '<li>Where the underlying rates differ, a calibrated model gives the two '
                'groups different false-positive rates.</li>'
                '<li>No model can meet both conditions when the underlying rates '
                'differ.</li></ul>',
     'question_text': 'The student wants to explain to a general audience why the two '
                      'fairness measures conflict. Which choice most effectively uses '
                      'relevant information from the notes to accomplish this goal?',
     'choices': [
         'A model is calibrated if, of the people it scores at 40 per cent, about 40 per cent go on to reoffend.',
         'No model can meet both of the two conditions at the same time.',
         'When two groups reoffend at different underlying rates, a model calibrated for both must give them different false-positive rates — so the two goals cannot both be met.',
         'Whether a model is calibrated depends on how often the people it scores go on to reoffend.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>When two groups reoffend</strong>… Maqsad '
                    '<em>nima uchun</em> ziddiyat borligini tushuntirish, demak javob sababni '
                    '(turli bazaviy koeffitsiyentlar) va oqibatni birga bersin. <strong>No '
                    'model can meet</strong>… xulosaning oʻzini takrorlaydi, lekin sababni '
                    'aytmaydi — tinglovchi baribir nima uchunligini bilmaydi.'},
]
