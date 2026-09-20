# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 2 · Reading and Writing, Module 1
#  27 questions · 32 minutes · every taker sits this one.
#
#  Route: 18 or more correct here sends the taker to the UPPER module 2.
#
#  Load: python manage.py load_mock exam/data/sat2_rw1.py --expect-questions=27
#  Guide: exam/data/STYLE_GUIDE_SAT_MOCK.md
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
     'passage': '<p>When Wangari Maathai began the Green Belt Movement in Kenya in 1977, '
                'her proposal was ______: pay rural women a small sum for every seedling '
                'that survived. By 2007 the women of the movement had planted more than '
                'thirty million trees.</p>',
     'question_text': WORD_Q,
     'choices': ['ambitious', 'modest', 'reluctant', 'secretive'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>modest</strong>. Ikki nuqtadan keyin taklifning '
                    'oʻzi keltirilgan — kichik toʻlov, oddiy shart — va keyingi jumla '
                    'natijaning ulkanligini qoʻyadi. Qarama-qarshilik shu: kichik usul, '
                    'katta natija. <strong>ambitious</strong> aynan shu qarama-qarshilikni '
                    'buzadi va eng koʻp tanlanadigan javob, chunki talaba oʻttiz million '
                    'raqamiga qarab tanlaydi.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'easy',
     'passage': '<p>For three centuries the glassmakers of Murano were forbidden to leave '
                'the Venetian Republic. The recipe for cristallo, a glass so clear that it '
                'could be mistaken for rock crystal, was not merely a craft secret but a '
                'matter of state, and the penalties for ______ it were severe.</p>',
     'question_text': WORD_Q,
     'choices': ['divulging', 'perfecting', 'purchasing', 'recording'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>divulging</strong> — oshkor qilish. Matn '
                    'retseptni "secret" va "a matter of state" deb ataydi, ustalarga esa '
                    'chiqib ketish taqiqlangan: jazo sirni <em>aytib qoʻyganlik</em> uchun '
                    'boʻladi. <strong>perfecting</strong> notoʻgʻri: takomillashtirish '
                    'ustaning ishi, jinoyat emas.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>A cuttlefish changes colour in less than a second, matching the gravel '
                'it has settled on down to the size of the stones. What makes the '
                'performance ______ is that cuttlefish, so far as every test of their '
                'vision can show, are colour-blind: the animal is reproducing a pattern it '
                'cannot see.</p>',
     'question_text': WORD_Q,
     'choices': ['deliberate', 'gradual', 'puzzling', 'routine'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>puzzling</strong>. Ikki nuqtadan keyingi qism '
                    'ziddiyatni ochadi: hayvon oʻzi koʻra olmaydigan naqshni takrorlaydi — '
                    'bu tushuntirib boʻlmaydigan holat. <strong>routine</strong> aksincha '
                    'maʼno beradi; agar oddiy boʻlganda, matn "so far as every test can '
                    'show" deb taʼkidlamagan boʻlardi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'medium',
     'passage': '<p>Cement gains most of its strength in the first month, but the reaction '
                'that hardens it does not stop there. Decades later, water is still '
                'reaching unreacted grains deep inside a wall. Chemists say the process is '
                'not finished but merely <u>arrested</u> — slowed to a rate no human '
                'lifetime can register.</p>',
     'question_text': 'As used in the text, what does the word <u>arrested</u> most nearly '
                      'mean?',
     'choices': ['accelerated', 'checked', 'detained', 'reversed'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>checked</strong> — sekinlashtirilgan, '
                    'toʻxtatib turilgan. Tiredan keyingi qism maʼnoni oʻzi beradi: "slowed '
                    'to a rate no human lifetime can register". <strong>detained</strong> '
                    '"arrest" soʻzining huquqiy maʼnosi va shuning uchun eng kuchli tuzoq — '
                    'koʻp maʼnoli soʻzda lugʻat emas, kontekst hal qiladi.'},

    # ── Craft and Structure: Text Structure and Purpose (5–6) ──────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>The Antikythera mechanism was pulled from a shipwreck in 1901 and '
                'catalogued as a lump of corroded bronze. Only when it was X-rayed, seventy '
                'years later, did anyone count the gears: at least thirty of them, cut to '
                'model the motions of the sun and moon and the cycle on which eclipses '
                'return. Nothing of comparable complexity survives from the next fourteen '
                'centuries. The object is not evidence that the Greeks were ahead of their '
                'time. It is evidence of how much has been lost.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that the mechanism matters for what its survival implies about what did not survive',
         'To compare Greek astronomical knowledge with that of later European astronomers',
         'To describe the conditions in which the mechanism was recovered from the sea',
         'To explain how X-ray imaging is used to study corroded metal objects',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>To argue that the mechanism</strong>… Matn '
                    'oxirgi ikki jumlada oʻz fikrini ochiq aytadi: bu yunonlar oʻz '
                    'davridan oldinda edi degani emas, <em>qancha narsa yoʻqolganining</em> '
                    'dalili. <strong>To describe the conditions in which</strong>… birinchi '
                    'jumladan olingan detal; matnning birinchi jumlasi uning maqsadi emas.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'medium',
     'passage': '<p>Nüshu, a script used by women in Jiangyong County in Hunan, was '
                'written in a slanted rhomboid hand quite unlike standard Chinese '
                'characters. <u>It was not a secret language, whatever later accounts '
                'claim.</u> Men in the county knew the script existed and thought it '
                'beneath their notice, which is a different thing from not knowing — '
                'and it is why Nüshu survived in plain sight for generations.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It concedes a point that the rest of the text goes on to refute.',
         'It corrects a widespread claim, and the rest of the text explains why the distinction matters.',
         'It introduces the historical period in which the script was used.',
         'It offers evidence for the assertion made in the first sentence.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>It corrects a widespread</strong>… Jumla '
                    '"whatever later accounts claim" bilan keng tarqalgan fikrni rad etadi, '
                    'keyingi jumla esa farqning nima uchun muhimligini aytadi — bilmaslik '
                    'bilan eʼtiborsizlik bir narsa emas. <strong>It offers evidence for '
                    'the assertion</strong>… notoʻgʻri: birinchi jumla yozuvning '
                    'koʻrinishi haqida, bu jumla esa uning maqomi haqida.'},

    # ── Craft and Structure: Cross-Text Connections (7) ────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>When beavers were returned to the River Otter in '
                'Devon, flood peaks downstream fell measurably. For the project’s '
                'supporters the lesson generalizes: a beaver builds, at no cost to anyone, '
                'the kind of flood defence a water authority would spend millions to '
                'install.</p>'
                '<p><b>Text 2</b><br>Alastair Reed is wary of that arithmetic. The '
                'Otter’s beavers were released into a catchment whose shape suits '
                'them — narrow, wooded, gently sloping. On a straightened lowland '
                'channel with no trees along it, he notes, a beaver does not build the '
                'same structures, and in some places does not settle at all.</p>',
     'question_text': 'Based on the texts, Reed would most likely argue that the lesson '
                      'drawn in Text 1 is',
     'choices': [
         'incorrect, because flood peaks on the River Otter did not in fact fall.',
         'irrelevant, because water authorities do not build flood defences of that kind.',
         'overstated, because the effect observed may depend on features of that particular catchment.',
         'premature, because the beavers have not yet been monitored for long enough.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>overstated, because the effect</strong>… Reed '
                    'oʻlchovni inkor qilmaydi — u <em>umumlashtirishga</em> qarshi: natija '
                    'oʻsha daryoning shakliga bogʻliq boʻlishi mumkin. '
                    '<strong>incorrect, because flood peaks</strong>… eng keng tarqalgan '
                    'xato: "wary" soʻzini koʻrib, 2-matn hamma narsani rad etadi deb '
                    'oʻylash. Ikki matnli savolda avval nimaga <em>qoʻshiladi</em> deb '
                    'soʻrang.'},

    # ── Information and Ideas: Central Ideas and Details (8–9) ─────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>In 1942 Hedy Lamarr and the composer George Antheil patented a way of '
                'guiding a torpedo by radio on a signal that hopped between frequencies, so '
                'that jamming any one of them achieved nothing. The navy filed the patent '
                'away. The idea returned in the 1960s, and frequency hopping now sits in '
                'the hardware of every mobile phone. What the patent lacked in 1942 was not '
                'insight but a small enough component: Antheil’s mechanism for '
                'switching frequencies was a piano roll.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Antheil’s training as a composer was essential to the invention of frequency hopping.',
         'Frequency hopping was reinvented in the 1960s by engineers unaware of the 1942 patent.',
         'Lamarr’s system was set aside because the navy failed to grasp its military value.',
         'The patent described a workable idea whose adoption waited on technology it could not yet use.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The patent described a</strong>… Oxirgi jumla '
                    'butun matnning fikri: yetishmagani gʻoya emas, <em>yetarlicha kichik '
                    'detal</em> edi. <strong>Lamarr’s system was set aside because '
                    'the navy failed</strong>… tuzoq: matn hujjat "filed away" deb aytadi, '
                    'lekin sababni dengiz flotining tushunmasligiga bogʻlamaydi — bu '
                    'oʻqilmagan maʼlumot.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'medium',
     'passage': '<p>Nüshu was learned from women and passed between them, usually '
                'written on folding fans and on the cloth of the “third-day book” '
                'given to a bride. Because the script belonged to those occasions rather '
                'than to record-keeping, almost nothing was archived; what survived did so '
                'inside households. By the time the last fluent writer died in 2004, the '
                'known corpus amounted to a few hundred items.</p>',
     'question_text': 'According to the text, why did so few Nüshu documents survive?',
     'choices': [
         'Fluent writers of the script refused to let their work be copied.',
         'The fans and cloth it was written on decayed more quickly than paper.',
         'The script was destroyed by those in the county who opposed its use.',
         'The script belonged to occasions rather than to records, so its texts stayed in households.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>The script belonged to</strong>… Matn sababni '
                    'oʻzi aytadi: "Because the script belonged to those occasions rather '
                    'than to record-keeping, almost nothing was archived". <strong>The fans '
                    'and cloth it was written on decayed</strong>… mantiqan maʼqul '
                    'koʻrinadi va aynan shuning uchun xavfli — matnda chirish haqida bitta '
                    'ham soʻz yoʻq.'},

    # ── Information and Ideas: Command of Evidence (10–12) ─────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>A biologist proposes that a cuttlefish matches its background by '
                'sensing light through its skin rather than by seeing it, since every test '
                'of the animal’s vision suggests that it is colour-blind.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'biologist’s proposal?',
     'choices': [
         'Cuttlefish change colour more slowly in dim light than in bright light.',
         'Cuttlefish match a background more accurately when it lies directly beneath them.',
         'Cuttlefish skin contains the same light-sensitive protein that lines the retina of the eye.',
         'Several other cephalopods can also change colour within a second.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Cuttlefish skin contains the</strong>… Taklif '
                    'ikki yoʻlni ajratadi: koʻz orqali koʻrish yoki <em>teri</em> orqali '
                    'sezish. Faqat shu variant terida yorugʻlikni sezadigan mexanizm '
                    'borligini koʻrsatadi. <strong>Cuttlefish change colour more slowly in '
                    'dim light</strong>… yorugʻlik muhimligini aytadi, lekin sezgi qayerda '
                    'ekanini aytmaydi — ikki yoʻlni ham bir xil qoʻllab-quvvatlaydi.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A historian claims that the Antikythera mechanism was not a unique '
                'object but one surviving product of an established workshop '
                'tradition — that devices of the kind were designed, built and sold '
                'by craftsmen who had made others before it.</p>',
     'question_text': 'Which finding, if true, would most strongly support the '
                      'historian’s claim?',
     'choices': [
         'Ancient texts describe similar geared devices, and the mechanism’s teeth are cut to a standard shared with other Greek bronze fittings.',
         'No other geared device of comparable complexity has been found anywhere in the ancient world.',
         'The mechanism models the motions of the sun and moon more accurately than those of the planets.',
         'The mechanism was recovered from a wreck that was carrying luxury goods toward Rome.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Ancient texts describe similar</strong>… Daʼvo '
                    '"anʼana bor edi" degani, demak dalil <em>boshqa</em> buyumlarga '
                    'ishora qilishi kerak: yozma manbalar va umumiy ishlov standarti aynan '
                    'shuni beradi. <strong>No other geared device of comparable '
                    'complexity</strong>… toʻgʻridan-toʻgʻri teskari ishlaydi — u '
                    'buyumning yakka ekanini koʻrsatadi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'medium',
     'passage': '<p>Researchers tested seeds of four crops that had been held for twenty '
                'years in a vault at −18°C, and compared the result with the '
                'germination rate recorded when each sample was deposited.</p>'
                '<table><tr><th>Crop</th><th>Germination at deposit (%)</th>'
                '<th>Germination after 20 years (%)</th></tr>'
                '<tr><td>Barley</td><td>96</td><td>93</td></tr>'
                '<tr><td>Lettuce</td><td>94</td><td>71</td></tr>'
                '<tr><td>Pea</td><td>92</td><td>88</td></tr>'
                '<tr><td>Sorghum</td><td>98</td><td>96</td></tr></table>',
     'question_text': 'A student concludes that, among these four crops, lettuce seed loses '
                      'viability in storage considerably faster than the others. Which '
                      'choice best describes data from the table that support this '
                      'conclusion?',
     'choices': [
         'All four crops germinated at more than 90% when they were deposited.',
         'Lettuce fell by 23 percentage points over the twenty years, while no other crop fell by more than 5.',
         'Lettuce had the lowest germination rate of the four crops after twenty years.',
         'Sorghum had the highest germination rate of the four crops at deposit.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Lettuce fell by</strong>… Xulosa <em>yoʻqotish '
                    'tezligi</em> haqida, demak dalil ikki ustun orasidagi <em>farqni</em> '
                    'olishi kerak: 94 → 71 va boshqalarda koʻpi bilan 5 ball. '
                    '<strong>Lettuce had the lowest germination rate of the four crops '
                    'after twenty years</strong> rost, lekin u faqat oxirgi holatni '
                    'koʻrsatadi — past boshlagan urugʻ ham shunday chiqishi mumkin edi.'},

    # ── Information and Ideas: Inferences (13–14) ──────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'medium',
     'passage': '<p>The Namib receives almost no rain, but fog rolls in from the Atlantic '
                'before dawn. A darkling beetle that lives there climbs a dune at first '
                'light and tips its body forward; droplets gather on its back and run down '
                'grooves to its mouth. Engineers studying the beetle have been less '
                'interested in the grooves than in the surface between them, because '
                '______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'fog holds less water than rain does and is therefore harder to collect.',
         'the beetle’s posture matters more than the shape of its shell.',
         'the grooves are too small to be manufactured at an industrial scale.',
         'the surface has to make water condense before any channel has anything to carry.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>the surface has to</strong>… Matnda ikki bosqich '
                    'bor: tomchi <em>hosil boʻladi</em>, keyin oqib tushadi. Muhandislar '
                    'birinchisini oʻrganishadi, chunki ikkinchisi birinchisisiz maʼnosiz. '
                    '<strong>the grooves are too small to be manufactured</strong>… matn '
                    'ishlab chiqarish haqida hech narsa demaydi — bu oʻqilmagan sabab.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>A garment left at a charity shop in Europe is sorted and, more often '
                'than not, sold on in a bale to traders abroad. What a bale fetches depends '
                'on what the sorter believes a distant market will accept, and that '
                'judgement is made before the bale is ever opened at the other end. A shift '
                'in fashion in Accra therefore reaches the European sorting floor '
                '______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'as an immediate change in the price paid for donated clothing.',
         'more quickly than a shift in European fashion does.',
         'only after the clothes it affects have already been shipped.',
         'through the charity shops rather than through the traders.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>only after the clothes</strong>… Matn kalit '
                    'jumlani beradi: baho <em>ochilishidan oldin</em> qoʻyiladi. Demak '
                    'uzoqdagi bozorning yangi didi faqat keyingi aylanishda bilinadi — mol '
                    'allaqachon joʻnatilgan boʻladi. <strong>as an immediate change in the '
                    'price</strong> aynan shu jumlaga zid.'},

    # ── Standard English Conventions: Boundaries (15–17) ───────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'easy',
     'passage': '<p>The Green Belt Movement, founded by Wangari Maathai in ______ paid '
                'rural women a small sum for every seedling that lived.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['1977', '1977,', '1977:', '1977;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>1977,</strong>. "founded by…1977" — '
                    'ajratilgan aniqlovchi ibora va u vergul bilan ochilgan, demak vergul '
                    'bilan yopiladi. <strong>1977;</strong> notoʻgʻri: nuqtali vergul ikki '
                    'mustaqil gapni ajratadi, bu yerda esa bitta gapning ichidamiz.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>Deposits at the seed vault stay sealed in the depositor’s own '
                '______ they can be withdrawn only by the bank that sent them.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['boxes', 'boxes and,', 'boxes,', 'boxes;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>boxes;</strong>. Boʻshliqning ikki tomonida ham '
                    'toʻliq mustaqil gap turibdi, ularni nuqtali vergul ajratadi. '
                    '<strong>boxes,</strong> — comma splice: ikki mustaqil gapni '
                    'yolgʻiz vergul bilan ulash ingliz tilida xato.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>The only crop in the trial that ______ more than five percentage points '
                'of viability over the twenty years was lettuce.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['— lost', ', lost', 'lost', 'lost,'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>lost</strong> — hech qanday tinish belgisi '
                    'kerak emas. "that lost more than five percentage points" ekinni '
                    '<em>aniqlaydigan</em> ergash gap: usiz gap maʼnosini yoʻqotadi, '
                    'shuning uchun u vergul bilan ajratilmaydi. Ajratuvchi belgi qoʻyilsa, '
                    'aniqlovchi qoʻshimcha izohga aylanadi va "the only crop" iborasi '
                    'maʼnosiz qoladi.'},

    # ── Standard English Conventions: Form, Structure, and Sense (18–21)
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'easy',
     'passage': '<p>The corpus of Nüshu texts held by museums and by private families '
                '______ to a few hundred items.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['amount', 'amounts', 'are amounting', 'have amounted'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>amounts</strong>. Ega — <em>corpus</em>, '
                    'birlik; "of Nüshu texts held by museums and by private families" '
                    'faqat aniqlovchi. Feʼlga eng yaqin turgan soʻz koʻplik ("families") '
                    'boʻlgani uchun quloq <strong>amount</strong> ga tortadi — '
                    'tanlashdan oldin oraliq iborani yoping va egani toping.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>By the time the mechanism was X-rayed in the 1970s, it ______ in a '
                'museum case for seventy years.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['had been sitting', 'has been sitting', 'is sitting', 'will have sat'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>had been sitting</strong>. "By the time…was '
                    'X-rayed" oʻtmishdagi nuqtani beradi, holat esa undan oldin boshlanib '
                    'oʻsha nuqtagacha davom etgan — past perfect continuous. '
                    '<strong>has been sitting</strong> hozirgi paytga ulaydi, gap esa '
                    '1970-yillarda tugagan.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>Neither the sorter in Europe nor the traders abroad open a bale before '
                '______ has been priced.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['it', 'them', 'they', 'those'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>it</strong>. Olmosh <em>a bale</em> ga ishora '
                    'qiladi — birlik, shuning uchun "it". <strong>they</strong> tuzoq: '
                    'talaba yaqin turgan "the traders" ga bogʻlaydi, lekin baho qoʻyiladigan '
                    'narsa savdogarlar emas, tyuk.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>______ the Antikythera mechanism was catalogued as a lump of corroded '
                'bronze and left in a case for seventy years.</p>',
     'question_text': CONVENTION_Q,
     'choices': [
         'Having pulled it from a shipwreck in 1901,',
         'Pulled from a shipwreck in 1901,',
         'Pulling it from a shipwreck in 1901,',
         'To pull it from a shipwreck in 1901,',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Pulled from a</strong>… Boshlanuvchi ibora '
                    'egani — <em>the mechanism</em> — aniqlashi kerak, mexanizm '
                    'esa <em>tortib olingan</em>: majhul maʼno, demak III shakl. '
                    '<strong>Pulling it from a</strong>… aniq nisbat beradi va mexanizmning '
                    'oʻzi kimnidir tortib olgan boʻlib chiqadi — egasiga osilib '
                    'qolgan aniqlovchi.'},

    # ── Expression of Ideas: Transitions (22–24) ───────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'easy',
     'passage': '<p>A cuttlefish matches the gravel beneath it within a second, stone size '
                'and all. ______ every test of the animal’s vision says that it cannot '
                'see colour at all.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['For example,', 'However,', 'Similarly,', 'Therefore,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>However,</strong>. Naqshni aniq takrorlash va '
                    'ranglarni koʻra olmaslik — kutilmagan ziddiyat. '
                    '<strong>Therefore,</strong> aynan teskari bogʻlanish va eng koʻp '
                    'tanlanadigan xato: birinchi jumladagi muvaffaqiyat talabani natija '
                    'kutishga undaydi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>The navy filed Lamarr and Antheil’s patent away and built nothing '
                'from it. ______ the idea reappeared, this time in the hands of engineers '
                'who had components small enough to switch frequencies quickly.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Consequently,', 'In contrast,', 'Meanwhile,', 'Twenty years later,'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Twenty years later,</strong>. Ikki jumla '
                    'orasidagi bogʻ — <em>vaqt</em>: gʻoya yotib qoldi, keyin qaytdi. '
                    '<strong>Meanwhile,</strong> bir vaqtda sodir boʻlishni bildiradi, '
                    'bu yerda esa hodisalar ketma-ket.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>Beavers measurably lowered flood peaks on the River Otter. The result '
                'may not carry to every river, ______ a beaver on a straightened lowland '
                'channel with no trees along it often builds nothing at all.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['however,', 'in fact,', 'nevertheless,', 'on the other hand,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>in fact,</strong>. Ikkinchi qism birinchisiga '
                    'qarshi turmaydi — u uni <em>kuchaytiradi</em>: natija har joyda '
                    'takrorlanmasligi mumkin, va mana nega. Qolgan uchtasi ham '
                    'qarama-qarshilik bildiradi, shuning uchun ular bir vaqtda toʻgʻri '
                    'boʻla olmaydi. Bogʻlovchi savolida avval munosabatni aniqlang, keyin '
                    'variantga qarang.'},

    # ── Expression of Ideas: Rhetorical Synthesis (25–27) ──────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Wangari Maathai founded the Green Belt Movement in Kenya in 1977.</li>'
                '<li>The movement paid rural women a small sum for each seedling that '
                'survived.</li>'
                '<li>Payment depended on survival, not on planting.</li>'
                '<li>By 2007 more than 30 million trees had been planted.</li>'
                '<li>Maathai received the Nobel Peace Prize in 2004.</li></ul>',
     'question_text': 'The student wants to emphasize how much the movement achieved given '
                      'how simple its method was. Which choice most effectively uses '
                      'relevant information from the notes to accomplish this goal?',
     'choices': [
         'By paying rural women a small sum for each seedling that survived, the Green Belt Movement saw more than 30 million trees planted by 2007.',
         'Payment under the scheme depended on a seedling’s survival rather than on its being planted.',
         'The Green Belt Movement paid rural women a small sum for each seedling that survived.',
         'Wangari Maathai, who received the Nobel Peace Prize in 2004, founded the Green Belt Movement in 1977.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>By paying rural women</strong>… Maqsad ikki '
                    'narsani <em>bir jumlada</em> qarshi qoʻyishni talab qiladi: oddiy usul '
                    'va ulkan natija. Faqat shu variant ikkalasini ham beradi. '
                    '<strong>The Green Belt Movement paid rural women</strong>… usulni '
                    'aytadi, lekin natijani aytmaydi — yarmi bajarilgan javob '
                    'notoʻgʻri javobdir.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'medium',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>The Svalbard seed vault holds duplicates of collections from gene '
                'banks worldwide.</li>'
                '<li>Deposits stay sealed in the depositor’s own boxes.</li>'
                '<li>Nobody browses the collection.</li>'
                '<li>A deposit can be withdrawn only by the bank that sent it.</li>'
                '<li>A withdrawal happens only once that bank has lost its own copy.</li></ul>',
     'question_text': 'The student wants to explain to an audience unfamiliar with the '
                      'vault why it is not a library. Which choice most effectively uses '
                      'relevant information from the notes to accomplish this goal?',
     'choices': [
         'A gene bank that has lost its own collection can ask for its deposit back.',
         'Deposits at the vault stay sealed in the boxes in which they arrived.',
         'Nothing at the vault can be browsed or borrowed: a sealed deposit goes back only to the bank that sent it, and only once that bank has lost its own copy.',
         'The Svalbard vault holds duplicates of seed collections from gene banks around the world.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>Nothing at the vault</strong>… Maqsad ombor '
                    'nega kutubxona <em>emasligini</em> tushuntirish, demak javob '
                    'kutubxonaning ikki belgisini — koʻrib chiqish va olib turish — '
                    'inkor qilishi kerak. <strong>The Svalbard vault holds duplicates</strong>… '
                    'nima saqlanishini aytadi, tartibni emas.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>The Antikythera mechanism was recovered from a shipwreck in 1901.</li>'
                '<li>It was catalogued as a lump of corroded bronze.</li>'
                '<li>X-rays taken in the 1970s revealed at least thirty gears.</li>'
                '<li>The gears model the sun, the moon and the cycle on which eclipses '
                'return.</li>'
                '<li>Nothing of comparable complexity survives from the next fourteen '
                'centuries.</li></ul>',
     'question_text': 'The student wants to emphasize the gap between the mechanism and '
                      'everything that came after it. Which choice most effectively uses '
                      'relevant information from the notes to accomplish this goal?',
     'choices': [
         'The gears of the mechanism model the motions of the sun and of the moon.',
         'The mechanism was recovered from a shipwreck in 1901 and catalogued as a lump of corroded bronze.',
         'The mechanism’s thirty-odd gears model the sun, the moon and the eclipse cycle — and nothing of comparable complexity survives from the next fourteen centuries.',
         'X-rays taken in the 1970s revealed that the mechanism contains at least thirty gears.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>The mechanism’s thirty-odd gears</strong>… '
                    'Maqsad — <em>farqni</em> koʻrsatish, demak javob buyumning '
                    'murakkabligini va undan keyingi boʻshliqni yonma-yon qoʻyishi kerak. '
                    '<strong>X-rays taken in the 1970s</strong>… murakkablikni aytadi, '
                    'lekin taqqoslanadigan ikkinchi tomon yoʻq — farq hosil '
                    'boʻlmaydi.'},
]
