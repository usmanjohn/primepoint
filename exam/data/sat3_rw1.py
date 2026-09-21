# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 3 · Reading and Writing, Module 1
#  27 questions · 32 minutes · every taker sits this one.
#
#  Route: 18 or more correct here sends the taker to the UPPER module 2.
#
#  Load: python manage.py load_mock exam/data/sat3_rw1.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md
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
     'passage': '<p>At the Bauhaus, women were steered into the weaving workshop whether or '
                'not they had asked to be there. Anni Albers, who had wanted to paint, '
                'treated the assignment as a ______: she spent the next fifty years showing '
                'that a woven surface could carry ideas as demanding as anything on a '
                'canvas.</p>',
     'question_text': WORD_Q,
     'choices': ['apology', 'challenge', 'rehearsal', 'setback'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>challenge</strong>. Ikki nuqtadan keyingi qism '
                    'javobni beradi: u ellik yil davomida toʻquvning imkoniyatini isbotladi '
                    '— bu qabul qilingan chaqiriq. <strong>setback</strong> eng kuchli '
                    'tuzoq, chunki tayinlov haqiqatan ham adolatsiz edi; lekin matn uning '
                    'javobini tasvirlaydi, holatning oʻzini emas.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>Cut an axolotl’s leg off and it grows another, complete with bone, '
                'muscle and nerve, and with no scar where the old limb ended. The animal '
                'does not so much heal the wound as ______ the limb.</p>',
     'question_text': WORD_Q,
     'choices': ['abandon', 'conceal', 'rebuild', 'strengthen'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>rebuild</strong>. Birinchi jumla natijani '
                    'sanaydi — suyak, mushak, nerv — yaʼni oyoq qaytadan '
                    'quriladi, yara shunchaki bitmaydi. <strong>conceal</strong> '
                    '(yashirish) chalgʻituvchi, chunki chandiq qolmaydi; lekin chandiqning '
                    'yoʻqligi yashirish emas, qayta qurishning belgisi.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>Ibn al-Haytham’s <i>Book of Optics</i>, written in Cairo around '
                '1020, does not merely assert that vision works by light entering the eye; '
                'it tells the reader how to ______ the claim for himself: darken a room, '
                'make a small aperture in one wall, and watch an image of the sun appear on '
                'the wall opposite.</p>',
     'question_text': WORD_Q,
     'choices': ['abandon', 'publish', 'translate', 'verify'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>verify</strong>. Ikki nuqtadan keyin '
                    'oʻquvchiga beriladigan koʻrsatma turibdi — xonani qorongʻi qil, '
                    'teshik och, natijani kuzat — bu tekshirish tartibi. '
                    '<strong>publish</strong> notoʻgʻri: koʻrsatma oʻquvchiga berilgan, '
                    'nashriyotga emas.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>Permafrost is not simply frozen soil; it is frozen soil with the last '
                'ice age’s plant matter still inside it, undecayed. Something like a '
                'thousand billion tonnes of carbon is <u>locked</u> there, and it stays '
                'that way only while the ground stays frozen.</p>',
     'question_text': 'As used in the text, what does the word <u>locked</u> most nearly '
                      'mean?',
     'choices': ['concealed', 'fastened', 'held', 'secured'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>held</strong> — saqlanib turgan. Oxirgi '
                    'qism shartni beradi: yer muzlab turganida. <strong>fastened</strong> '
                    'va <strong>secured</strong> "lock" soʻzining jismoniy maʼnosiga '
                    'tortadi — lekin uglerodni qulflab qoʻyib boʻlmaydi, u shunchaki '
                    'chiqa olmay turibdi.'},

    # ── Craft and Structure: Text Structure and Purpose (5–6) ──────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>A Polynesian navigator crossing open ocean carried no instrument. What '
                'he carried was a memorised star compass — the points on the horizon '
                'where particular stars rise and set — together with the swell '
                'patterns and the bird behaviour of a route learned from someone who had '
                'sailed it before him. European accounts long described these voyages as '
                'accidental drift. The voyages were repeatable, which is the one thing '
                'drift is not.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that a star compass is more accurate than a magnetic compass',
         'To compare Polynesian navigation with European navigation of the same period',
         'To describe the instruments Polynesian navigators carried on long voyages',
         'To explain how a memorised body of knowledge made the voyages deliberate rather than accidental',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To explain how a</strong>… Matn birinchi '
                    'jumlada asbob yoʻqligini aytadi, keyin uning oʻrnini nima bosganini '
                    'sanaydi, oxirida esa "drift" talqinini bitta dalil bilan yiqitadi: '
                    'sayohat takrorlanardi. <strong>To describe the instruments</strong>… '
                    'toʻgʻridan-toʻgʻri zid — matn aynan asbob <em>boʻlmaganini</em> '
                    'aytadi.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>The paintings in the Chauvet cave are about 36,000 years old, twice the '
                'age of those at Lascaux. <u>The surprise is not their age but their '
                'competence.</u> The horses are drawn with a confidence that took later '
                'European art thousands of years to recover, and the lions are set one '
                'behind another on a curved wall the artist has used rather than fought.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It concedes that the dating of the paintings remains uncertain.',
         'It gives an example of a technique used by the cave’s artists.',
         'It redirects attention from one feature of the paintings to another, which the rest of the text then describes.',
         'It summarizes a conclusion that the final sentence disputes.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>It redirects attention from</strong>… Jumla '
                    '"yosh emas, mahorat" deb eʼtiborni burib yuboradi, keyingi jumla esa '
                    'aynan mahoratni — otlar va sherlar — tasvirlaydi. '
                    '<strong>It gives an example of a technique</strong>… notoʻgʻri: misol '
                    'undan <em>keyin</em> keladi, jumlaning oʻzida texnika yoʻq.'},

    # ── Craft and Structure: Cross-Text Connections (7) ────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>Most research on microplastics has looked at the sea. '
                'Soil may matter more. Sludge from wastewater treatment is spread on '
                'farmland across Europe, and it carries the fibres that washing machines '
                'shed. Per hectare, some estimates put the plastic load on farmland above '
                'that on the ocean surface.</p>'
                '<p><b>Text 2</b><br>Teodora Lipska accepts the estimates but not the alarm '
                'that tends to follow them. Load is not exposure, she argues. A fibre bound '
                'into a soil aggregate is doing nothing to anybody, and the question that '
                'matters — how much of it moves into a plant, an earthworm or a '
                'person — has barely been measured.</p>',
     'question_text': 'Based on the texts, Lipska’s response to the case made in Text '
                      '1 is best described as',
     'choices': [
         'accepting its measurements while questioning what they tell us about harm.',
         'agreeing with its conclusion but proposing a different explanation for it.',
         'arguing that the ocean remains a more urgent priority than farmland.',
         'rejecting its measurements as too imprecise to support any conclusion.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>accepting its measurements while</strong>… '
                    '2-matn birinchi soʻzidayoq raqamni qabul qiladi ("accepts the '
                    'estimates"), keyin esa ulardan chiqariladigan <em>xulosani</em> '
                    'shubha ostiga oladi. <strong>rejecting its measurements as too '
                    'imprecise</strong>… eng keng tarqalgan xato: eʼtiroz bilan inkorni '
                    'aralashtirish.'},

    # ── Information and Ideas: Central Ideas and Details (8–9) ─────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>A white-crowned sparrow learns its song in its first summer, from the '
                'males singing around it, and keeps that version for the rest of its life. '
                'Because young birds rarely move far, one valley can hold a song audibly '
                'different from the song two valleys away, and the boundary between them '
                'can stay put for decades. The dialect is not in the species. It is in the '
                'neighbourhood.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Sparrow song varies from place to place because it is learned young and rarely carried far.',
         'The boundaries between sparrow dialects have shifted considerably in recent decades.',
         'White-crowned sparrows sing more complex songs than other sparrow species do.',
         'Young sparrows become unable to learn a new song once their first summer has ended.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Sparrow song varies from</strong>… Matn ikki '
                    'shartni ulaydi: qoʻshiq yoshlikda oʻrganiladi va qushlar uzoqqa '
                    'ketmaydi — shuning uchun sheva joyga bogʻlanadi. <strong>The '
                    'boundaries between sparrow dialects have shifted</strong>… matnga zid: '
                    'chegara "oʻn yillar davomida joyida turadi" deyilgan.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>A quipu is a set of knotted cords. The knots record numbers in base '
                'ten, and that much has been readable since the 1920s: position gives the '
                'power of ten, knot type gives the digit. What is not readable is '
                'everything else — the colour of a cord, the direction a knot is '
                'tied, the ply of the fibre — and Inca administrators used quipus for '
                'census, for tribute and, the chroniclers say, for narrative. The '
                'arithmetic survived. The rest did not.</p>',
     'question_text': 'According to the text, what distinguishes the parts of a quipu that '
                      'can be read from the parts that cannot?',
     'choices': [
         'Spanish chroniclers recorded the meaning of the numbers but not of the colours.',
         'The cords that recorded numbers were made of a more durable fibre than the others.',
         'The numerical knots follow a system that has been reconstructed, and the other features do not.',
         'The numerical knots were tied by trained specialists, while the other features were added later.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>The numerical knots follow</strong>… Matn ikki '
                    'nuqtadan keyin tiklangan tizimni aytadi (oʻrin — daraja, tugun '
                    'turi — raqam) va tiredan keyin tizimi yoʻq qolgan belgilarni '
                    'sanaydi. <strong>The cords that recorded numbers were made of a more '
                    'durable fibre</strong>… matnda umuman yoʻq — chidamlilik haqida '
                    'bir soʻz ham aytilmagan.'},

    # ── Information and Ideas: Command of Evidence (10–12) ─────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A biologist proposes that an axolotl regrows a limb because cells at '
                'the wound surface revert to a flexible, embryo-like state, rather than '
                'because a reserve of stem cells has been waiting in the tissue — '
                'which would mean the new limb is built by cells that were, until '
                'recently, ordinary muscle and skin.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'biologist’s proposal?',
     'choices': [
         'Axolotls can also regenerate parts of the heart and of the spinal cord.',
         'Axolotls regrow limbs more slowly as they grow older.',
         'Cells in the regrowing limb carry the molecular markers of the mature tissue they belonged to before the amputation.',
         'Salamanders of several other species can also regrow a limb.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Cells in the regrowing</strong>… Taklif ikki '
                    'yoʻlni ajratadi: kutib turgan ildiz hujayralar yoki <em>qaytgan</em> '
                    'yetuk hujayralar. Eski toʻqimaning belgisi yangi oyoqda topilsa, '
                    'hujayralar yaqinda mushak va teri boʻlgani chiqadi. <strong>Axolotls '
                    'can also regenerate parts of the heart</strong>… qobiliyat kengligini '
                    'koʻrsatadi, mexanizmni emas.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>An archaeologist claims that the animals at Chauvet were painted by '
                'people who had watched them closely and over a long period, rather than '
                'copied from an inherited stock of images — which would mean the '
                'painters were recording behaviour rather than repeating a convention.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'archaeologist’s claim?',
     'choices': [
         'Similar animals appear in painted caves elsewhere in southern Europe.',
         'The lions are shown in postures that occur only during a hunt, and the rhinoceroses in one used only when males fight.',
         'The paintings are concentrated in the parts of the cave furthest from the entrance.',
         'The pigments used at Chauvet were obtained from deposits close to the cave.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>The lions are shown</strong>… Daʼvo '
                    '<em>kuzatuv</em> haqida, demak dalil rasmlarda faqat tirik hayvonni '
                    'koʻrgan odam bilishi mumkin boʻlgan tafsilot borligini koʻrsatishi '
                    'kerak. <strong>Similar animals appear in painted caves '
                    'elsewhere</strong>… aksincha ishlaydi — u aynan "meros qolgan '
                    'anʼana" versiyasini quvvatlaydi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>Researchers measured the depth to which the ground thaws each summer at '
                'four Arctic sites, and the carbon released from each site over one '
                'year.</p>'
                '<table><tr><th>Site</th><th>Summer thaw depth (cm)</th>'
                '<th>Carbon released (g per m² per year)</th></tr>'
                '<tr><td>Tiksi</td><td>38</td><td>61</td></tr>'
                '<tr><td>Barrow</td><td>45</td><td>78</td></tr>'
                '<tr><td>Inuvik</td><td>71</td><td>132</td></tr>'
                '<tr><td>Abisko</td><td>96</td><td>171</td></tr></table>',
     'question_text': 'A student concludes that, among these sites, a deeper summer thaw '
                      'was associated with more carbon released. Which choice best '
                      'describes data from the table that support this conclusion?',
     'choices': [
         'Abisko released 171 grams of carbon per square metre over the year.',
         'All four sites released at least 60 grams of carbon per square metre.',
         'Carbon released rose with thaw depth across all four sites, from 61 grams at Tiksi (38 cm) to 171 grams at Abisko (96 cm).',
         'The thaw depth at Inuvik was almost twice the thaw depth at Tiksi.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Carbon released rose</strong>… Xulosa ikki '
                    'kattalikning birga oʻzgarishi haqida, shuning uchun dalil ham '
                    'ikkalasini butun jadval boʻylab olishi kerak. Qolgan uchtasi rost, '
                    'lekin bittagina katakni yoki bittagina ustunni gapiradi — '
                    '<strong>The thaw depth at Inuvik</strong>… uglerod haqida hech narsa '
                    'demaydi.'},

    # ── Information and Ideas: Inferences (13–14) ──────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>Ibn al-Haytham’s procedure was to state a claim, design a '
                'situation in which the claim would fail if it were false, and report what '
                'happened. The <i>Book of Optics</i> contains claims he inherited from '
                'Ptolemy and claims he arrived at himself, and it treats the two kinds '
                'identically. What made the method new was therefore not scepticism about '
                'authority but ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'a willingness to test any claim at all, including his own.',
         'the decision to write in Arabic rather than in Greek.',
         'the invention of instruments accurate enough to measure refraction.',
         'the use of geometry to describe the behaviour of light.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>a willingness to test</strong>… Kalit jumla '
                    '— "treats the two kinds identically": u nafaqat Ptolemeyni, '
                    'balki oʻzini ham sinaydi. Agar yangilik faqat obroʻga shubha boʻlsa, '
                    'oʻz daʼvolarini sinashning keragi yoʻq edi. Qolgan uchtasi matnda '
                    'umuman aytilmagan.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>A young sparrow raised in isolation produces a song that is '
                'recognisably a sparrow’s but belongs to no dialect: the '
                'species’ template is in the bird, the local version is not. A '
                'population in which every male had been raised in isolation would '
                'therefore ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'develop a dialect indistinguishable from its neighbours’.',
         'fail to produce any song at all.',
         'lose its dialect within a single generation.',
         'sing more loudly than a population raised in the ordinary way.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>lose its dialect within</strong>… Matn ikki '
                    'qismni ajratadi: tur andozasi qushning oʻzida, mahalliy shevasi esa '
                    'faqat eshitish orqali. Hech kim eshitmasa, sheva bir avlodda '
                    'yoʻqoladi. <strong>fail to produce any song at all</strong> '
                    'toʻgʻridan-toʻgʻri zid — yolgʻiz oʻsgan qush baribir kuylaydi.'},

    # ── Standard English Conventions: Boundaries (15–17) ───────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>Anni Albers, the first weaver given a solo exhibition at the Museum of '
                'Modern ______ had been steered into the Bauhaus weaving workshop against '
                'her wishes.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['Art', 'Art,', 'Art:', 'Art;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Art,</strong>. "the first weaver given…Art" '
                    '— <em>Anni Albers</em> ga izoh (appozitsiya) va u vergul bilan '
                    'ochilgan, demak vergul bilan yopiladi. <strong>Art</strong> '
                    '(belgisiz) izohni kesimga yopishtirib yuboradi va gap oʻqilmay '
                    'qoladi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>An axolotl’s regrown limb has bone, muscle and ______ there is no '
                'scar where the old limb ended.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['nerve', 'nerve and,', 'nerve,', 'nerve;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>nerve;</strong>. Boʻshliqning ikki tomonida ham '
                    'toʻliq mustaqil gap turibdi, ularni nuqtali vergul ajratadi. '
                    '<strong>nerve,</strong> — comma splice: sanashning oxiridagi '
                    'vergul yangi gapni ulay olmaydi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>The only part of a quipu that scholars ______ with confidence is its '
                'number system.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['— read', ', read', 'read', 'read,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>read</strong> — hech qanday belgi kerak '
                    'emas. "that scholars read with confidence" qismni <em>aniqlaydigan</em> '
                    'ergash gap: usiz "the only part" iborasi maʼnosini yoʻqotadi, shuning '
                    'uchun u ajratilmaydi. Ajratuvchi belgi qoʻyilsa, aniqlovchi '
                    'qoʻshimcha izohga aylanadi.'},

    # ── Standard English Conventions: Form, Structure, and Sense (18–21)
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The set of knotted cords that an Inca administrator carried ______ '
                'census figures, tribute owed and, the chroniclers say, narrative.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['are recording', 'have recorded', 'record', 'records'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>records</strong>. Ega — <em>set</em>, '
                    'birlik; "of knotted cords that an Inca administrator carried" faqat '
                    'aniqlovchi. Feʼlga eng yaqin turgan soʻz koʻplik ("cords…carried") '
                    'boʻlgani uchun quloq <strong>record</strong> ga tortadi — '
                    'tanlashdan oldin oraliq iborani yoping.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time the Chauvet paintings were dated in the 1990s, '
                'archaeologists ______ for decades that European cave art began much '
                'later.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['assume', 'had assumed', 'has assumed', 'will have assumed'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>had assumed</strong>. "By the time…were dated" '
                    'oʻtmishdagi nuqtani beradi, taxmin esa undan <em>oldin</em> oʻn '
                    'yillar davom etgan — past perfect. <strong>has assumed</strong> '
                    'hozirgi paytga ulaydi, gap esa 1990-yillarda tugagan.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>The paintings at Chauvet are roughly twice as old as ______ at '
                'Lascaux.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['that', 'them', 'they', 'those'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>those</strong>. Taqqoslashda rasmlar rasmlar '
                    'bilan solishtiriladi, <em>paintings</em> esa koʻplik — demak '
                    '"those". <strong>that</strong> birlikni bildiradi va eng koʻp '
                    'tanlanadigan xato; <strong>them</strong> esa taqqoslash emas, '
                    'toʻldiruvchi shakli.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>A navigator learned a route by sailing it with someone who already knew '
                'it, by memorising the star compass, and by ______</p>',
     'question_text': CONVENTION_Q,
     'choices': [
         'having watched the swell.',
         'the swell was watched.',
         'to watch the swell.',
         'watching the swell.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>watching the swell.</strong> Qator '
                    '"by sailing…by memorising…and by ___" — har bir aʼzo '
                    '<em>by</em> + <em>-ing</em> shaklida, demak uchinchisi ham shunday '
                    'boʻlishi shart. <strong>having watched the swell.</strong> maʼnoni '
                    'buzmaydi va aynan shuning uchun xavfli, lekin u qatorning shaklini '
                    'sindiradi.'},

    # ── Expression of Ideas: Transitions (22–24) ───────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>A young sparrow learns its song in its first summer and keeps that '
                'version for life. ______ one valley can hold a song audibly different from '
                'the song two valleys away.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['As a result,', 'In contrast,', 'Nevertheless,', 'Previously,'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>As a result,</strong>. Yoshlikda oʻrganib, umr '
                    'boʻyi saqlash — sabab; shevalarning joyga bogʻlanishi — '
                    'natija. <strong>In contrast,</strong> qarama-qarshilik talab qiladi, '
                    'bu yerda esa ikkala jumla bir tomonga qaraydi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Ibn al-Haytham designed experiments to test claims he had inherited '
                'from Ptolemy. ______ he designed experiments to test the claims he had '
                'arrived at himself.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['However,', 'Instead,', 'Similarly,', 'Therefore,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Similarly,</strong>. Ikki jumla bir xil '
                    'harakatni ikki xil obyektga qoʻllaydi — bu oʻxshashlik. '
                    '<strong>Instead,</strong> birinchisining oʻrnini bosishni bildiradi, '
                    'lekin u ikkalasini ham qilgan; <strong>However,</strong> esa '
                    'yoʻq boʻlgan ziddiyatni talab qiladi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>Microplastic loads on farmland may exceed those on the ocean surface. '
                '______ load is not exposure: a fibre bound into a soil aggregate reaches '
                'no plant, no earthworm and no person.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'For instance,', 'Moreover,', 'Still,'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Still,</strong>. Birinchi jumla xavotir '
                    'uygʻotadi, ikkinchisi esa uni yumshatadi — yon berish '
                    '(kontsessiya). <strong>Moreover,</strong> qoʻshimcha dalil kutadi va '
                    'eng koʻp tanlanadigan xato: talaba ikkinchi jumlani ham '
                    '"yomon xabar" deb oʻqiydi, aslida u teskari yoʻnalishda.'},

    # ── Expression of Ideas: Rhetorical Synthesis (25–27) ──────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Polynesian navigators crossed open ocean without instruments.</li>'
                '<li>They used a memorised star compass: the horizon points where '
                'particular stars rise and set.</li>'
                '<li>They also read swell patterns and bird behaviour.</li>'
                '<li>Routes were learned from navigators who had already sailed them.</li>'
                '<li>European accounts long described the voyages as accidental '
                'drift.</li></ul>',
     'question_text': 'The student wants to emphasize that the voyages were deliberate. '
                      'Which choice most effectively uses relevant information from the '
                      'notes to accomplish this goal?',
     'choices': [
         'European accounts long described the Polynesian voyages as accidental drift.',
         'Navigators used a memorised star compass, swell patterns and bird behaviour on routes learned from someone who had sailed them — these were not accidental voyages.',
         'Polynesian navigators crossed the open ocean without carrying any instrument.',
         'Routes were learned from navigators who had already sailed them.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Navigators used a memorised</strong>… Maqsad '
                    '— <em>ataylab</em> qilinganini taʼkidlash, demak javob bilimning '
                    'tizimliligini koʻrsatib, "drift" talqinini ochiq rad etishi kerak. '
                    '<strong>European accounts long described</strong>… faqat rad '
                    'etilayotgan fikrni takrorlaydi, uni yiqitmaydi.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>An axolotl can regrow an amputated limb.</li>'
                '<li>Cells at the wound surface revert to a flexible, embryo-like '
                'state.</li>'
                '<li>This mass of cells is called a blastema.</li>'
                '<li>The blastema rebuilds bone, muscle and nerve in the right order.</li>'
                '<li>No scar forms where the old limb ended.</li></ul>',
     'question_text': 'The student wants to explain the process to an audience unfamiliar '
                      'with it. Which choice most effectively uses relevant information '
                      'from the notes to accomplish this goal?',
     'choices': [
         'An axolotl is able to regrow a limb that has been amputated.',
         'At the wound surface, cells revert to a flexible embryo-like state, forming a blastema that rebuilds bone, muscle and nerve in order and leaves no scar.',
         'No scar forms at the place where an axolotl’s old limb ended.',
         'The mass of flexible cells at the wound surface is called a blastema.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>At the wound surface,</strong>… Maqsad '
                    '<em>jarayonni</em> tushuntirish, demak javob bosqichlarni ketma-ket '
                    'bersin: hujayralar qaytadi → blastema → qayta quriladi → chandiq '
                    'yoʻq. <strong>The mass of flexible cells at the wound surface is '
                    'called a blastema</strong>… faqat atamani beradi, jarayonni emas.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>A quipu records numbers in base ten through knot position and knot '
                'type.</li>'
                '<li>The number system has been readable since the 1920s.</li>'
                '<li>Cord colour, knot direction and fibre ply are not understood.</li>'
                '<li>Inca administrators used quipus for census, for tribute and for '
                'narrative.</li>'
                '<li>No quipu has been matched to a text in any other medium.</li></ul>',
     'question_text': 'The student wants to emphasize how much of the quipu record has been '
                      'lost. Which choice most effectively uses relevant information from '
                      'the notes to accomplish this goal?',
     'choices': [
         'A quipu records numbers in base ten through the position and the type of its knots.',
         'Inca administrators used quipus for census records, for tribute and for narrative.',
         'The arithmetic of a quipu has been readable since the 1920s, but cord colour, knot direction and fibre ply are not — and the Inca used quipus for narrative as well as for counting.',
         'The number system of a quipu has been readable since the 1920s.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>The arithmetic of a</strong>… Maqsad '
                    '<em>yoʻqolgan qismning hajmini</em> koʻrsatish, demak javob '
                    'oʻqiladigan yarmini va oʻqilmaydigan yarmini yonma-yon qoʻyishi, '
                    'hamda yoʻqolgan narsaning muhimligini (hikoya) aytishi kerak. '
                    '<strong>The number system of a quipu has been readable since the '
                    '1920s</strong>… faqat saqlangan qismni aytadi — yoʻqotish '
                    'koʻrinmaydi.'},
]
