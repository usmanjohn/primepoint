# ──────────────────────────────────────────────────────────────────────
#  Digital SAT — PrimePoint Mock 2 · Reading and Writing, Module 2 (UPPER)
#  27 questions · 32 minutes · taken by a pupil who scored 18+ on rw1.
#
#  Same domains, same counts, same order as the lower module. What changes
#  is the disguise: two-step reasoning, longer syntax, harder vocabulary.
#
#  Load: python manage.py load_mock exam/data/sat2_rw2_hard.py --expect-questions=27
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
     'passage': '<p>Noether’s theorem is usually stated as a link between symmetry and '
                'conservation: wherever a physical law does not change under some '
                'transformation, some quantity is conserved. The result is ______ rather '
                'than experimental — it follows from the structure of the theory, not '
                'from any measurement anyone has taken.</p>',
     'question_text': WORD_Q,
     'choices': ['accidental', 'formal', 'provisional', 'statistical'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>formal</strong>. Tiredan keyingi qism maʼnoni '
                    'oʻzi beradi: natija nazariyaning <em>tuzilishidan</em> kelib chiqadi, '
                    'oʻlchovdan emas. <strong>statistical</strong> eng kuchli tuzoq, chunki '
                    'u ham "eksperimental emas"dek tuyuladi — lekin statistika ham '
                    'oʻlchovga tayanadi.'},

    {'section': S, 'number': 2, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>Fewer than five hundred signs are known from the seals of the Indus '
                'cities, and the longest inscription runs to seventeen characters. The '
                'corpus is not merely small; every text in it is ______, and a decipherment '
                'needs long inscriptions in which a wrong guess has room to fail.</p>',
     'question_text': WORD_Q,
     'choices': ['brief', 'damaged', 'disputed', 'ornamental'],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>brief</strong>. Nuqtali vergul "kichik" dan '
                    'boshqa xususiyatga oʻtadi, oxirgi qism esa aynan uzunlik haqida: '
                    '"needs long inscriptions". <strong>damaged</strong> mantiqan maʼqul '
                    'koʻrinadi — qadimgi buyum axir — lekin matn shikast haqida '
                    'bir soʻz ham aytmaydi.'},

    {'section': S, 'number': 3, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p><i>Deinococcus radiodurans</i> survives doses of radiation that shatter '
                'its chromosome into hundreds of pieces. The bacterium does not resist the '
                'damage; it ______ it, reassembling the fragments in the right order within '
                'a few hours.</p>',
     'question_text': WORD_Q,
     'choices': ['accumulates', 'prevents', 'repairs', 'tolerates'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>repairs</strong>. Nuqtali vergul '
                    'qarama-qarshilik qoʻyadi (qarshilik emas), vergul ortidagi ibora esa '
                    'nimani anglatishini aytadi: boʻlaklarni toʻgʻri tartibda yigʻish. '
                    '<strong>tolerates</strong> eng kuchli tuzoq — chidash passiv '
                    'holat, matn esa faol ishni tasvirlaydi.'},

    {'section': S, 'number': 4, 'skill': 'Words in Context', 'difficulty': 'hard',
     'passage': '<p>Hardin’s parable of the commons assumes herders who cannot talk to '
                'one another. Elinor Ostrom spent decades documenting commons where they '
                'could: irrigation systems in Spain, forests in Japan, fisheries in Turkey, '
                'each with rules the users had written and could <u>police</u> '
                'themselves.</p>',
     'question_text': 'As used in the text, what does the word <u>police</u> most nearly '
                      'mean?',
     'choices': ['detect', 'enforce', 'guard', 'restrict'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>enforce</strong>. Obyekt — <em>rules</em>, '
                    'va qoidani "amalga oshirish, bajarilishini taʼminlash" mumkin. '
                    '<strong>guard</strong> "police" soʻzining kundalik maʼnosiga yaqin va '
                    'shuning uchun chalgʻituvchi, lekin qoʻriqlanadigan narsa joy yoki '
                    'buyum boʻladi, qoida emas.'},

    # ── Text Structure and Purpose (5–6) ───────────────────────────────
    {'section': S, 'number': 5, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>The Declaration of Sentiments, adopted at Seneca Falls in 1848, opens '
                'by borrowing a sentence everyone in the room already knew: “We hold '
                'these truths to be self-evident: that all men and women are created '
                'equal.” The addition of two words is the whole argument. The document '
                'does not ask for a new principle. It asks that an old one be read as '
                'written.</p>',
     'question_text': 'Which choice best states the main purpose of the text?',
     'choices': [
         'To argue that the delegates at Seneca Falls disagreed about the document’s wording',
         'To compare the style of the Declaration of Sentiments with that of the Declaration of Independence',
         'To describe the circumstances under which the Declaration of Sentiments was adopted',
         'To explain how the document argues by amending a familiar sentence rather than proposing a new principle',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>To explain how the</strong>… Matn oxirgi ikki '
                    'jumlada oʻz fikrini aytadi: hujjat yangi tamoyil soʻramaydi, eskisini '
                    'yozilganidek oʻqishni soʻraydi — va butun dalil ikki soʻzning '
                    'qoʻshilishida. <strong>To compare the style</strong>… tuzoq: matn '
                    'mashhur jumladan foydalanadi, lekin ikki hujjatning <em>uslubini</em> '
                    'taqqoslamaydi.'},

    {'section': S, 'number': 6, 'skill': 'Text Structure and Purpose', 'difficulty': 'hard',
     'passage': '<p>Between 2011 and 2015 several large projects set out to reproduce '
                'well-known findings in psychology and succeeded less than half the time. '
                '<u>The number is usually read as a verdict on the field, which is the '
                'least useful thing to do with it.</u> A failed replication is a measurement '
                'too, and its value lies in telling you which of the original effects were '
                'small enough to vanish under a different sample.</p>',
     'question_text': 'Which choice best describes the function of the underlined sentence '
                      'in the text as a whole?',
     'choices': [
         'It anticipates an objection that the final sentence goes on to dismiss.',
         'It concedes a limitation in the replication projects described in the previous sentence.',
         'It provides statistical context for the figure given in the previous sentence.',
         'It rejects a common reading of the finding and prepares the alternative that follows.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>It rejects a common</strong>… Jumla ikki ish '
                    'qiladi: keng tarqalgan talqinni rad etadi ("the least useful thing"), '
                    'va oxirgi jumla oʻrniga nimani taklif qilishini tayyorlaydi. '
                    '<strong>It concedes a limitation</strong>… notoʻgʻri: jumla '
                    'loyihalarning kamchiligini emas, <em>oʻquvchilarning</em> talqinini '
                    'tanqid qiladi.'},

    # ── Cross-Text Connections (7) ─────────────────────────────────────
    {'section': S, 'number': 7, 'skill': 'Cross-Text Connections', 'difficulty': 'hard',
     'passage': '<p><b>Text 1</b><br>Stars at the edge of a spiral galaxy orbit about as '
                'fast as stars near its centre. The visible matter cannot hold them there, '
                'so something unseen must. Dark matter is the simplest account, and it has '
                'held up across cluster masses, gravitational lensing and the cosmic '
                'microwave background.</p>'
                '<p><b>Text 2</b><br>Modified Newtonian dynamics proposes instead that '
                'gravity itself departs from Newton’s law at very low accelerations. '
                'Its defenders concede that the idea struggles with clusters and with the '
                'microwave background. They answer that it predicts individual rotation '
                'curves with a single parameter, where dark matter needs a halo fitted to '
                'each galaxy in turn.</p>',
     'question_text': 'Based on the texts, the defenders described in Text 2 would most '
                      'likely respond to the case made in Text 1 by arguing that',
     'choices': [
         'dark matter’s reach across several kinds of evidence is bought by fitting each galaxy separately.',
         'gravitational lensing provides no evidence about how mass is distributed.',
         'stars at the edge of a spiral galaxy do not in fact orbit as fast as stars near its centre.',
         'the cosmic microwave background has been measured too imprecisely to settle the question.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>dark matter’s reach across</strong>… '
                    '2-matn himoyachilari 1-matnning dalillarini inkor qilmaydi — '
                    'ular <em>narxini</em> koʻrsatadi: har bir galaktikaga alohida gardish '
                    'moslanadi. <strong>stars at the edge of a spiral galaxy do not in '
                    'fact</strong>… ikkala matn ham bu faktni qabul qiladi: ziddiyat '
                    'kuzatuvda emas, tushuntirishda.'},

    # ── Central Ideas and Details (8–9) ────────────────────────────────
    {'section': S, 'number': 8, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>James Baldwin wrote most of his work about America while living in '
                'France, and he was asked about it often enough to have an answer ready: '
                'the distance was not escape but instrument. In Paris he was read first as '
                'a writer and only afterwards as a Black man, and that reversal let him see '
                'which parts of what he had taken for his own character were in fact the '
                'shape of the pressure he had grown up under.</p>',
     'question_text': 'Which choice best states the main idea of the text?',
     'choices': [
         'Baldwin left the United States because he found it impossible to publish his work there.',
         'Baldwin wrote about France as frequently as he wrote about the United States.',
         'Baldwin’s French readers understood his work better than his American readers did.',
         'Baldwin’s years abroad were a method: distance showed him which of his traits were his and which were his circumstances’.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Baldwin’s years abroad</strong>… Matn '
                    'kalit soʻzni oʻzi beradi — "not escape but instrument" — va '
                    'oxirgi jumla asbob nimani koʻrsatganini aytadi. <strong>Baldwin’s '
                    'French readers understood his work better</strong>… tuzoq: matn '
                    'fransuz oʻquvchilarining <em>tartibini</em> (avval yozuvchi, keyin '
                    'qora tanli) aytadi, tushunish darajasini emas.'},

    {'section': S, 'number': 9, 'skill': 'Central Ideas and Details', 'difficulty': 'hard',
     'passage': '<p>Ibn Battuta dictated the <i>Rihla</i> years after he returned, to a '
                'young scholar who shaped it into the form we read. Some passages match '
                'other sources closely; others describe places in the wrong order, or '
                'repeat an earlier traveller’s account almost word for word. '
                'Historians who use the book therefore treat it as two things at once: a '
                'record of a journey, and a record of what a fourteenth-century audience '
                'expected a journey to contain.</p>',
     'question_text': 'According to the text, why do historians treat the <i>Rihla</i> as '
                      'two kinds of record?',
     'choices': [
         'It combines material from the journey itself with material shaped by what readers of the time expected.',
         'It survives only in copies made several centuries after it was composed.',
         'It was dictated in more than one language and later translated.',
         'Its author disowned parts of it once they had been written down.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>It combines material from</strong>… Matn '
                    'ikkiligini ikki nuqtadan keyin oʻzi sanaydi, oʻrtadagi jumla esa '
                    'sababini beradi: baʼzi parchalar boshqa manbaga mos, baʼzilari '
                    'koʻchirma. <strong>It was dictated in more than one language</strong>… '
                    'matnda umuman yoʻq — diktovka bor, tillar haqida hech narsa '
                    'aytilmagan.'},

    # ── Command of Evidence (10–12) ────────────────────────────────────
    {'section': S, 'number': 10, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A microbiologist proposes that <i>Deinococcus radiodurans</i> owes its '
                'radiation tolerance not to an unusually tough chromosome but to an '
                'unusually effective repair system — which would mean that its DNA '
                'breaks as readily as any other organism’s and is simply put back '
                'together faster.</p>',
     'question_text': 'Which finding, if true, would most directly support the '
                      'microbiologist’s proposal?',
     'choices': [
         'Immediately after irradiation, the bacterium’s chromosome is in as many fragments as that of a radiation-sensitive species given the same dose.',
         'The bacterium can also survive prolonged desiccation.',
         'The bacterium carries several copies of its genome at once.',
         'The bacterium grows more slowly than most species kept in laboratories.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Immediately after irradiation, the</strong>… '
                    'Taklifning ikki qismi bor, va bu variant birinchisini toʻgʻridan-'
                    'toʻgʻri sinaydi: DNK <em>xuddi shunday</em> parchalanadimi. '
                    '<strong>The bacterium carries several copies of its genome</strong> '
                    'kuchli tuzoq — u taʼmirlash mexanizmini qoʻllaydi, lekin '
                    '"parchalanish boshqalarnikidek" degan yarmi tekshirilmay qoladi.'},

    {'section': S, 'number': 11, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>A political scientist claims that Ostrom’s cases show '
                'self-governance succeeding not because the users happened to be unusually '
                'cooperative but because the rules they wrote were cheap to monitor — '
                'which would make the decisive variable the design of the rule rather than '
                'the character of the group.</p>',
     'question_text': 'Which finding, if true, would most strongly support the political '
                      'scientist’s claim?',
     'choices': [
         'Commons governed by an outside authority failed more often than those governed by their own users.',
         'In commons that failed, the rules in force required information that users could not gather without cost.',
         'Ostrom’s cases were drawn from several continents and from many kinds of resource.',
         'Users in Ostrom’s successful cases reported high levels of trust in their neighbours.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>In commons that failed,</strong>… Daʼvo '
                    'ikki sababni ajratadi: odamlarning fazilati yoki qoidaning '
                    'arzonligi. Muvaffaqiyatsiz holatlarda aynan nazorat qimmat boʻlgani '
                    'koʻrsatilsa, oʻzgaruvchi qoidada ekani chiqadi. <strong>Users in '
                    'Ostrom’s successful cases reported high levels of trust</strong>… '
                    'aksincha, raqib tushuntirishni quvvatlaydi.'},

    {'section': S, 'number': 12, 'skill': 'Command of Evidence', 'difficulty': 'hard',
     'passage': '<p>Four replication projects each reported the share of original findings '
                'they were able to reproduce, together with the median statistical power of '
                'the studies they had tried to repeat.</p>'
                '<table><tr><th>Field</th><th>Median power of originals (%)</th>'
                '<th>Findings reproduced (%)</th></tr>'
                '<tr><td>Cancer biology</td><td>33</td><td>26</td></tr>'
                '<tr><td>Psychology</td><td>41</td><td>36</td></tr>'
                '<tr><td>Economics</td><td>62</td><td>61</td></tr>'
                '<tr><td>Social science</td><td>75</td><td>62</td></tr></table>',
     'question_text': 'A student concludes that the share of findings a project could '
                      'reproduce tracked the statistical power of the original studies. '
                      'Which choice best describes data from the table that support this '
                      'conclusion?',
     'choices': [
         'Cancer biology had both the lowest median power and the lowest share reproduced, and the four fields fall in the same order on each measure.',
         'Economics reproduced 61% of the original findings it tested.',
         'No field in the table reproduced more than 62% of its original findings.',
         'The median power of the original studies was below 50% in two of the four fields.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Cancer biology had both</strong>… Xulosa ikki '
                    'kattalikning <em>birga harakatlanishi</em> haqida, va faqat shu '
                    'variant ikkala ustunni butun jadval boʻylab bogʻlaydi: tartib bir xil '
                    '(33·26 &lt; 41·36 &lt; 62·61 &lt; 75·62). Qolgan uchtasi rost, lekin '
                    'har biri bitta ustunda qolib ketadi — bogʻliqlik haqida hech '
                    'narsa demaydi.'},

    # ── Inferences (13–14) ─────────────────────────────────────────────
    {'section': S, 'number': 13, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>A conservation law, on Noether’s account, is not an extra fact '
                'about the world but a consequence of a symmetry in the laws that describe '
                'it: energy is conserved because those laws do not change from one moment '
                'to the next. A physicist who found a system in which energy was genuinely '
                'not conserved would therefore be obliged to conclude that ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'Noether’s theorem applies only to idealized systems.',
         'energy is not a well-defined quantity in that system.',
         'the laws governing that system change with time.',
         'the measurement must have been carried out incorrectly.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>the laws governing that</strong>… Matn '
                    'bogʻlanishni bir tomonlama emas, shartli qilib qoʻyadi: energiya '
                    'saqlanadi <em>chunki</em> qonunlar vaqt boʻyicha oʻzgarmaydi. '
                    'Saqlanmasa, sabab ham yoʻq — demak qonunlar oʻzgaradi. '
                    '<strong>the measurement must have been carried out incorrectly</strong> '
                    'tuzoq: matn "genuinely" deb aynan bu yoʻlni yopib qoʻygan.'},

    {'section': S, 'number': 14, 'skill': 'Inferences', 'difficulty': 'hard',
     'passage': '<p>A decipherment is tested by prediction: you propose values for the '
                'signs, apply them to a text you did not use in building the proposal, and '
                'see whether the result is a sentence. Where the longest inscription runs '
                'to seventeen signs and most are under six, almost any proposal can be made '
                'to yield something. The obstacle to reading the Indus script is therefore '
                'not that scholars have too few hypotheses but that ______</p>',
     'question_text': 'Which choice most logically completes the text?',
     'choices': [
         'the seals were made over too long a period to record a single language.',
         'the signs were probably never intended to record speech at all.',
         'the texts are too short for a wrong hypothesis to fail.',
         'too few seals have survived to make up a usable corpus.',
     ],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>the texts are too</strong>… Matn sinovning '
                    'shartini beradi — taxmin <em>notoʻgʻri chiqishi</em> mumkin '
                    'boʻlishi kerak — va qisqa matnda deyarli har qanday taxmin '
                    '"ishlaydi". <strong>too few seals have survived</strong> tuzoq: matn '
                    'muammoni soni emas, <em>uzunligi</em>da deb ataydi ("not merely '
                    'small").'},

    # ── Boundaries (15–17) ─────────────────────────────────────────────
    {'section': S, 'number': 15, 'skill': 'Boundaries', 'difficulty': 'medium',
     'passage': '<p>The <i>Rihla</i>, dictated years after Ibn Battuta returned and shaped '
                'into its finished form by a young ______ survives in no copy made during '
                'his lifetime.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['scholar', 'scholar,', 'scholar:', 'scholar;'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>scholar,</strong>. "dictated…and shaped…scholar" '
                    '— ajratilgan aniqlovchi ibora, vergul bilan ochilgan, demak '
                    'vergul bilan yopiladi. <strong>scholar;</strong> notoʻgʻri: nuqtali '
                    'vergul ikki mustaqil gapni ajratadi, bu yerda esa ega hali kesimini '
                    'kutib turibdi.'},

    {'section': S, 'number': 16, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>Modified Newtonian dynamics predicts individual rotation curves from a '
                'single ______ however, it struggles badly with the masses of galaxy '
                'clusters.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['parameter', 'parameter and', 'parameter,', 'parameter;'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>parameter;</strong>. <em>however</em> bogʻlovchi '
                    'emas, kirish soʻz: u ikki mustaqil gapni ulay olmaydi, shuning uchun '
                    'ular orasida nuqtali vergul kerak. <strong>parameter,</strong> — '
                    'comma splice, va bu savolning butun tuzogʻi: "however" quloqqa '
                    'bogʻlovchidek eshitiladi.'},

    {'section': S, 'number': 17, 'skill': 'Boundaries', 'difficulty': 'hard',
     'passage': '<p>Ostrom documented commons on three ______ irrigation systems in Spain, '
                'where some of the rules were centuries old; forests in Japan; and '
                'fisheries along the Turkish coast.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['continents', 'continents,', 'continents:', 'continents;'],
     'correct': 3,
     'explanation': 'Toʻgʻri javob <strong>continents:</strong>. Ikki nuqta toʻliq gapdan '
                    'keyin sanashni kiritadi — va bu yerda u ayniqsa zarur, chunki '
                    'sanash aʼzolarining ichida allaqachon vergul bor, shuning uchun '
                    'aʼzolar nuqtali vergul bilan ajratilgan. <strong>continents,</strong> '
                    'sanashni oldingi vergullar bilan aralashtirib yuboradi.'},

    # ── Form, Structure, and Sense (18–21) ─────────────────────────────
    {'section': S, 'number': 18, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Among the findings that the replication projects could not reproduce '
                '______ several that had been cited hundreds of times.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['has been', 'is', 'was', 'were'],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>were</strong>. Gap teskari tartibda: ega '
                    'feʼldan keyin keladi va u — <em>several</em>, koʻplik. Boshdagi '
                    '"Among the findings…reproduce" faqat oʻrin holi, ega emas. SAT bu '
                    'savolni aynan shu teskari tartib uchun quradi.'},

    {'section': S, 'number': 19, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Noether’s argument requires that the law in question ______ '
                'unchanged under the transformation being considered.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['is', 'remain', 'remained', 'remains'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>remain</strong>. "require that" dan keyin '
                    'ingliz tilida buyruq-istak shakli (subjunctive) keladi: feʼl asos '
                    'shaklida turadi, shaxs va sondan qatʼi nazar. <strong>remains</strong> '
                    'quloqqa toʻgʻriroq eshitiladi va aynan shuning uchun eng koʻp '
                    'tanlanadi.'},

    {'section': S, 'number': 20, 'skill': 'Form, Structure, and Sense', 'difficulty': 'medium',
     'passage': '<p>Neither the psychology project nor the cancer-biology project '
                'reproduced even half of ______ target findings.</p>',
     'question_text': CONVENTION_Q,
     'choices': ['it’s', 'its', 'their', 'they’re'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>its</strong>. "Neither…nor" qurilishida olmosh '
                    'oʻziga <em>yaqin turgan</em> egaga moslashadi, "the cancer-biology '
                    'project" esa birlik. <strong>their</strong> tuzoq: ikkita loyiha '
                    'sanalgani uchun quloq koʻplikni kutadi, lekin "neither…nor" ularni '
                    'birlashtirmaydi — u ularni navbat bilan oladi.'},

    {'section': S, 'number': 21, 'skill': 'Form, Structure, and Sense', 'difficulty': 'hard',
     'passage': '<p>Baldwin said that the distance let him separate what belonged to him '
                'from what belonged to the country, and what he had chosen from '
                '______</p>',
     'question_text': CONVENTION_Q,
     'choices': [
         'being imposed on him.',
         'the imposition.',
         'things imposed on him.',
         'what had been imposed on him.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>what had been</strong>… Gapda "what…from '
                    'what…" qurilishi ikki marta takrorlangan, demak uchinchisi ham '
                    '<em>what</em> bilan boshlanishi kerak (parallelizm). <strong>things '
                    'imposed on him.</strong> maʼno jihatdan toʻgʻri va shuning uchun '
                    'chalgʻituvchi, lekin u qatorning shaklini sindiradi.'},

    # ── Transitions (22–24) ────────────────────────────────────────────
    {'section': S, 'number': 22, 'skill': 'Transitions', 'difficulty': 'medium',
     'passage': '<p>Dark matter accounts for rotation curves, for cluster masses, for '
                'lensing and for the microwave background. ______ it has never been '
                'detected directly, despite forty years of experiments built to catch '
                'it.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['Accordingly,', 'Even so,', 'For instance,', 'Likewise,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Even so,</strong>. Birinchi jumla uzun '
                    'muvaffaqiyatlar roʻyxati, ikkinchisi esa kutilmagan kamchilik — '
                    'qarama-qarshilik. <strong>Accordingly,</strong> aynan teskari '
                    'bogʻlanish va eng koʻp tanlanadigan xato: roʻyxat talabani ijobiy '
                    'davomni kutishga undaydi.'},

    {'section': S, 'number': 23, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>A failed replication is not a verdict on the honesty of the original '
                'authors. ______ most failures involve effects that were real but far '
                'smaller than the first sample had suggested.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['By contrast,', 'In fact,', 'Nevertheless,', 'Therefore,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>In fact,</strong>. Ikkinchi jumla birinchisiga '
                    'qarshi turmaydi — u uni <em>kuchaytiradi</em>: halollik masalasi '
                    'emas, oʻlcham masalasi. <strong>Nevertheless,</strong> va <strong>By '
                    'contrast,</strong> ikkalasi ham ziddiyat talab qiladi, bu yerda esa '
                    'ikkala jumla bir tomonga qaraydi.'},

    {'section': S, 'number': 24, 'skill': 'Transitions', 'difficulty': 'hard',
     'passage': '<p>Ostrom’s commons were governed by rules the users had written for '
                'themselves. ______ those rules were cheap to check: a farmer could see '
                'from his own field whether his neighbour had taken water out of turn.</p>',
     'question_text': TRANSITION_Q,
     'choices': ['By contrast,', 'Just as important,', 'Nevertheless,', 'Previously,'],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Just as important,</strong>. Ikkinchi jumla '
                    'birinchisiga <em>ikkinchi shartni qoʻshadi</em> — qoidalar '
                    'oʻzlariniki edi <em>va</em> arzon tekshirilardi. '
                    '<strong>Nevertheless,</strong> ziddiyat talab qiladi, lekin bu ikki '
                    'xususiyat bir-biriga qarshi emas, bir-birini toʻldiradi.'},

    # ── Rhetorical Synthesis (25–27) ───────────────────────────────────
    {'section': S, 'number': 25, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Emmy Noether published her theorem in 1918.</li>'
                '<li>It links a symmetry in physical laws to a conserved quantity.</li>'
                '<li>Energy is conserved because the laws do not change from moment to '
                'moment.</li>'
                '<li>Momentum is conserved because the laws do not change from place to '
                'place.</li>'
                '<li>Before the theorem, conservation laws were treated as facts '
                'established by experiment.</li></ul>',
     'question_text': 'The student wants to emphasize what the theorem explained that had '
                      'previously been taken as a brute fact. Which choice most effectively '
                      'uses relevant information from the notes to accomplish this goal?',
     'choices': [
         'Conservation laws had been treated as brute experimental facts; Noether showed that each follows from a symmetry — energy from laws that do not change with time, momentum from laws that do not change with place.',
         'Emmy Noether published the theorem that bears her name in 1918.',
         'Momentum is conserved because physical laws do not change from one place to another.',
         'Noether’s theorem links a symmetry in physical laws to a conserved quantity.',
     ],
     'correct': 1,
     'explanation': 'Toʻgʻri javob <strong>Conservation laws had been</strong>… Maqsad '
                    '<em>oldin va keyin</em>ni yonma-yon qoʻyishni talab qiladi: ilgari '
                    'tajriba fakti, endi simmetriyaning oqibati. Faqat shu variant ikkala '
                    'tomonni ham beradi. <strong>Noether’s theorem links a '
                    'symmetry</strong>… yangi holatni aytadi, lekin eski qarash '
                    'aytilmagani uchun taqqoslash hosil boʻlmaydi.'},

    {'section': S, 'number': 26, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Stars at the edge of a spiral galaxy orbit as fast as stars near its '
                'centre.</li>'
                '<li>Dark matter explains this by adding unseen mass.</li>'
                '<li>Dark matter also accounts for cluster masses, lensing and the '
                'microwave background.</li>'
                '<li>Modified Newtonian dynamics instead alters the law of gravity at low '
                'accelerations.</li>'
                '<li>Modified gravity fits individual rotation curves with one parameter '
                'but struggles with clusters.</li></ul>',
     'question_text': 'The student wants to present the disagreement fairly to a reader who '
                      'knows neither side. Which choice most effectively uses relevant '
                      'information from the notes to accomplish this goal?',
     'choices': [
         'Dark matter accounts for cluster masses, gravitational lensing and the cosmic microwave background.',
         'Dark matter explains rotation curves by adding unseen mass and also accounts for clusters, lensing and the microwave background; modified gravity fits rotation curves with a single parameter but struggles with clusters.',
         'Modified Newtonian dynamics alters the law of gravity at very low accelerations.',
         'Stars at the edge of a spiral galaxy orbit as fast as stars near its centre.',
     ],
     'correct': 2,
     'explanation': 'Toʻgʻri javob <strong>Dark matter explains rotation</strong>… Maqsad '
                    '— bahsni <em>adolatli</em> berish, demak javobda ikkala tomon '
                    'ham, har birining kuchli va kuchsiz yeri bilan turishi kerak. Qolgan '
                    'uchtasi faqat bitta tomonni yoki umumiy kuzatuvni aytadi — bir '
                    'tomonni tashlab ketgan javob "adolatli" boʻla olmaydi.'},

    {'section': S, 'number': 27, 'skill': 'Rhetorical Synthesis', 'difficulty': 'hard',
     'passage': '<p>While researching a topic, a student has taken the following '
                'notes:</p><ul>'
                '<li>Ibn Battuta dictated the <i>Rihla</i> years after he returned.</li>'
                '<li>A young scholar shaped the dictation into its finished form.</li>'
                '<li>Some passages repeat an earlier traveller’s account almost word '
                'for word.</li>'
                '<li>Some passages describe places in the wrong order.</li>'
                '<li>Historians read it as a record of what a fourteenth-century audience '
                'expected a journey to contain.</li></ul>',
     'question_text': 'The student wants to explain why the <i>Rihla</i> is useful to '
                      'historians even where it is unreliable. Which choice most '
                      'effectively uses relevant information from the notes to accomplish '
                      'this goal?',
     'choices': [
         'A young scholar shaped Ibn Battuta’s dictation into the form in which the book is now read.',
         'Ibn Battuta dictated the <i>Rihla</i> some years after he returned from his travels.',
         'Some passages in the <i>Rihla</i> repeat an earlier traveller’s account almost word for word.',
         'Where the <i>Rihla</i> borrows or misorders, it still records what a fourteenth-century audience expected a journey to contain — which is itself evidence.',
     ],
     'correct': 4,
     'explanation': 'Toʻgʻri javob <strong>Where the <i>Rihla</i> borrows</strong>… Maqsad '
                    'ikki qismli: kitob <em>qayerda ishonchsiz</em> va shunda ham '
                    '<em>nega foydali</em>. Faqat shu variant ikkalasini ulaydi. '
                    '<strong>Some passages in the <i>Rihla</i> repeat an earlier '
                    'traveller</strong>… faqat ishonchsizlikni aytadi, foydasini emas — '
                    'yarim maqsad bajarilgan javob notoʻgʻri javobdir.'},
]
