# -*- coding: utf-8 -*-
"""Prime English Readings — PE-61 … PE-65 (batch 13). Passive → reported speech → -ing/to.

PE-61 passive in all tenses + the by-agent · PE-62 reported speech and backshift ·
PE-63 reported questions, commands and reporting verbs · PE-64 gerunds and infinitives ·
PE-65 verbs that change meaning (stop / remember / forget / try).

Shapes:
  61 — how one book was made, in the passive: a 1978 school reader, two hundred thousand
       copies, and the illustrator whose name was left off the cover
  62 — a newspaper line that has followed a man for thirty years, and the sentence he
       actually said
  63 — a girl comes home at one in the morning with every answer ready, and the
       questions her father asks are not the ones she rehearsed
  64 — the plov man of a Tashkent courtyard: he does not have to cook, he wants to
  65 — a lorry driver's rule, learned from a father who stopped helping in 1998

NARRATOR VOICE (see the toc's AUDIO section):
    61 en-US-JennyNeural · 62 en-US-GuyNeural · 63 en-US-JennyNeural
    64 en-US-GuyNeural   · 65 en-US-JennyNeural
Generate one story at a time:
    python manage.py gen_corner_audio --collection="Prime English Readings" \
        --only 62 --voice en-US-GuyNeural

Cumulative rule: PE-61 uses the passive freely but NO reported speech with backshift
(that is PE-62 — direct quotes only). PE-64 stays away from the `stop doing / stop to do`
family, which is PE-65's whole lesson. No `as … as` / `too` / `enough` / `much +
comparative` (PE-67/68), no inversion or cleft sentences (PE-83+).
Length: 300–360 words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_61_65.py --author=prime
"""

SUBJECT = {
    "name":    "English",
    "summary": "Ingliz tili: IELTS uslubidagi qiziqarli oʻqish matnlari — lugʻat va grammatika bilan.",
    "icon":    "bi-globe2",
    "color":   "#2563eb",
    "order":   2,
}

COLLECTION = {
    "title":       "Prime English Readings",
    "description": (
        "Prime English darslarining oʻqish matnlari — har bir matn oʻz darsining "
        "grammatikasini jonli holda koʻrsatadi. Lugʻat izohlari va audio bilan."
    ),
    "order":       6,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PE-61 — passive in all tenses  (the book and the cover)  [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "How a Book Is Made",
        "summary": (
            "PE-61 matni. 1978-yilda bir kitob chop etildi — ikki yuz "
            "ming nusxada. Rasmlarni bir kishi chizgan edi, lekin "
            "muqovada uning ismi yoʻq edi. Qirq bir yildan keyin "
            "yangi nashr chiqdi."
        ),
        "order":   61,
        "grammar": [
            {
                "pattern":  "The passive in every tense",
                "meaning":  "Formula bir xil — <b>be + V3</b> — faqat "
                            "<i>be</i> zamonga qarab oʻzgaradi: "
                            "<i>is printed</i> (hozirgi) · "
                            "<i>is being printed</i> (hozir davom "
                            "etayotgan) · <i>was printed</i> · "
                            "<i>was being printed</i> · <i>has been "
                            "printed</i> · <i>had been printed</i> · "
                            "<i>will be printed</i> · <i>will have "
                            "been printed</i>.",
                "examples": ["The book is being reprinted this month.",
                             "Two hundred thousand copies had been printed by June.",
                             "The new edition will be delivered in August."],
            },
            {
                "pattern":  "Passives with modals, and two objects",
                "meaning":  "Modal + <b>be + V3</b>: <i>Every page "
                            "<b>must be checked</b></i>, <i>the paper "
                            "<b>can be cut</b> by machine</i>. "
                            "Ikki obyektli feʼllarda esa odam "
                            "boshiga chiqadi: <i>She <b>was given</b> "
                            "eleven roubles a drawing</i> — "
                            "<i>Eleven roubles was given to her</i> "
                            "dan tabiiyroq.",
                "examples": ["Every page must be checked twice.",
                             "She was given eleven roubles for each drawing."],
            },
            {
                "pattern":  "by or with, and It is said that…",
                "meaning":  "<b>by</b> — bajaruvchi (<i>drawn <b>by</b> "
                            "a young woman</i>), <b>with</b> — asbob "
                            "(<i>drawn <b>with</b> a steel pen</i>). "
                            "Manbasi aniq boʻlmagan gap uchun "
                            "shaxssiz passiv: <i><b>It is said that</b> "
                            "the first copies were carried by "
                            "train</i>.",
                "examples": ["The pictures were drawn with a steel pen.",
                             "It is said that the whole edition was sold in five weeks."],
            },
        ],
        "body": '''<p>A book is not written by one person. That sentence sounds wrong, and it is the most useful thing my aunt ever told me.</p>

<p>Here is how her book was made.</p>

<p>In 1976 a school reader for eight-year-olds <strong>was ordered</strong> by a publishing house in Tashkent. The stories <strong>were chosen</strong> by a <span class="cn-word" data-tr="komissiya">committee</span> of four people, and two of them <strong>were rewritten</strong> because a word in them <strong>was not liked</strong>. The <span class="cn-word" data-tr="qoʻlyozma">manuscript</span> <strong>was typed</strong> twice. Then somebody remembered that the book had no pictures in it.</p>

<p>My aunt Zulfiya was twenty-four, she <strong>had been trained</strong> at the art college in Samarkand, and she <strong>was paid</strong> eleven roubles for each drawing. There are forty-one drawings in that book. A goat on a roof. A boy asleep on a sack of <span class="cn-word" data-tr="oʻrik">apricots</span>. The <span class="cn-word" data-tr="chinor">plane tree</span> outside her own window, which is still standing in Chilonzor.</p>

<p>The <span class="cn-word" data-tr="bosma plastinalar, klishe">plates</span> <strong>were cut</strong> with a knife, one line at a time, and the pages <strong>were being set</strong> in <span class="cn-word" data-tr="qoʻrgʻoshin harflar">metal type</span> while she was still working on the last three pictures. Two hundred thousand copies <strong>had been printed</strong> by the autumn of 1978. It <strong>is said that</strong> the whole edition <strong>was sold</strong> in five weeks, and that some of it <strong>was carried</strong> to the districts by train in <span class="cn-word" data-tr="poyabzal qutilari">shoe boxes</span>, because the proper boxes had not arrived.</p>

<p>Her name is not on the cover.</p>

<p>The <span class="cn-word" data-tr="muharrir">editor</span> and the committee <strong>are named</strong> there, in three lines, in gold. The <span class="cn-word" data-tr="rassom">illustrator</span> <strong>was left off</strong> — not out of <span class="cn-word" data-tr="yovuzlik">malice</span>, she says. It <strong>was simply not thought about</strong> by anybody in the building.</p>

<p>In 2017 a small publisher in Tashkent decided to bring the reader back, and a young <span class="cn-word" data-tr="dizayner">designer</span> spent four months looking for the woman who had made the goat on the roof.</p>

<p>The new edition <strong>was published</strong> in 2019. The pictures <strong>had been scanned</strong> from a copy of the 1978 book, because the original plates <strong>have been lost</strong>. My aunt was sixty-five at the <span class="cn-word" data-tr="taqdimot">launch</span>, in a bookshop on Amir Temur, and she <strong>was given</strong> the first copy off the pile.</p>

<p>Her name is on the cover of that one. It <strong>is printed</strong> under the title, in the same size as the title, and every copy that <strong>will be printed</strong> from now on will carry it.</p>''',
        "questions": [
            {
                "text": "Why was Zulfiya's name not on the 1978 cover?",
                "choices": [
                    "The committee refused to put it there",
                    "Nobody in the publishing house thought about it — illustrators were simply left off",
                    "She asked them not to print it",
                ],
                "answer": 1,
                "explanation": "Uning oʻzi aytadi: bu yovuzlik emas edi. "
                               "Rassomning ismini muqovaga yozish "
                               "haqida shunchaki hech kim oʻylamagan.",
            },
            {
                "text": "\"The pages were being set in metal type while she was still working.\" This tense is:",
                "choices": [
                    "past continuous passive — it was in progress at that time",
                    "present perfect passive",
                    "future passive",
                ],
                "answer": 0,
                "explanation": "<b>was/were being + V3</b> — oʻtgan "
                               "zamonda davom etayotgan passiv: "
                               "u rasm chizayotganda sahifalar terilib "
                               "turgan edi.",
            },
            {
                "text": "Which sentence uses `by` and `with` correctly?",
                "choices": [
                    "The pictures were drawn with a young woman by a steel pen.",
                    "The pictures were drawn by a young woman with a steel pen.",
                    "The pictures were drawn from a young woman by a steel pen.",
                ],
                "answer": 1,
                "explanation": "<b>by</b> — ishni bajargan odam, "
                               "<b>with</b> — ishlatilgan asbob. "
                               "Ikkisini almashtirib boʻlmaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-62 — reported speech & backshift  (the newspaper line)  [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "What He Actually Said",
        "summary": (
            "PE-62 matni. 1994-yilda gazeta yozdi: “u qoʻrqmaganini "
            "aytdi”. Oʻsha bir gap otamning orqasidan oʻttiz yil "
            "yurdi. U esa butunlay boshqa gapni aytgan edi — va "
            "farqi juda muhim."
        ),
        "order":   62,
        "grammar": [
            {
                "pattern":  "say or tell, and the backshift",
                "meaning":  "<b>tell</b> dan keyin darhol odam keladi "
                            "(<i>he <b>told me</b></i>), <b>say</b> dan "
                            "keyin — yoʻq (<i>he <b>said</b> that…</i>). "
                            "Gap koʻchirilganda zamon bir qadam "
                            "orqaga suriladi: <i>am → was</i>, "
                            "<i>ran → had run</i>, <i>will → would</i>, "
                            "<i>can → could</i>.",
                "examples": ['He said that he was not afraid.',
                             'He told the journalist that he had simply run.'],
            },
            {
                "pattern":  "Pronouns, times and places move too",
                "meaning":  "<i>I → he</i>, <i>my → his</i>, "
                            "<i>now → then</i>, <i>today → that day</i>, "
                            "<i>yesterday → the day before</i>, "
                            "<i>here → there</i>, <i>this → that</i>. "
                            "Bir gapda hammasi birga siljiydi: "
                            "<i>“I saw it here yesterday”</i> → "
                            "<i>he said he <b>had seen</b> it "
                            "<b>there the day before</b></i>.",
                "examples": ['"I am afraid now." → He said that he was afraid then.',
                             '"I heard it here." → He said he had heard it there.'],
            },
            {
                "pattern":  "When you do NOT backshift",
                "meaning":  "Gap <b>hozir ham rost</b> boʻlsa yoki "
                            "umumiy haqiqat boʻlsa, zamonni "
                            "surmaslik mumkin: <i>He says he "
                            "<b>is</b> afraid of fire</i>. Shuning "
                            "uchun jurnalistning tanlovi bekor "
                            "emas — <b>qaysi shaklni tanlashi "
                            "maʼnoni oʻzgartiradi</b>.",
                "examples": ["He still says that he is afraid of fire.",
                             "She says that the paper was wrong."],
            },
        ],
        "body": '''<p>There is a <span class="cn-word" data-tr="qirqim, kesib olingan maqola">cutting</span> from a newspaper in our house, in a plastic <span class="cn-word" data-tr="fayl, papka">folder</span>, from June 1994. Nine <span class="cn-word" data-tr="satrlar">lines</span> and no photograph. It is about my father, who was nineteen then, and about a fire in a two-storey house on our street.</p>

<p>What happened is not complicated. Smoke came out of a window at about two in the afternoon. There was a child of four in the back room, alone, because her mother had gone to the shop at the corner for bread and had been talking to somebody for six minutes. My father went in through the kitchen door with a wet <span class="cn-word" data-tr="paltso">coat</span> over his head, and he came out with her.</p>

<p>The last line of the cutting says this: <i>He <strong>said</strong> that he <strong>was not afraid</strong>.</i></p>

<p>He has been correcting that sentence for thirty years, to anybody who brings it up, in exactly the same words.</p>

<p>"I <strong>told</strong> the man from the paper that I <strong>had been</strong> very afraid," he says. "I <strong>said</strong> that my hands <strong>were shaking</strong> in the yard afterwards and that I <strong>had not</strong> thought about anything at all. He wrote something else."</p>

<p>I asked him once why it matters. He was <span class="cn-word" data-pos="verb" data-tr="taʼmirlayotgan">mending</span> a chair at the time and he did not look up.</p>

<p>He <strong>said</strong> that a man who is not afraid teaches nobody anything. He <strong>said</strong> that every boy on our street had read that line, and that every one of them <strong>had understood</strong> from it that you have to be a special kind of person to go through a kitchen door.</p>

<p>"And that is a <span class="cn-word" data-tr="yolgʻon">lie</span>," he said. "I was an ordinary <span class="cn-word" data-pos="adj" data-tr="qoʻrqoq">frightened</span> boy of nineteen. That is the useful part. They printed the useless part."</p>

<p>The girl is thirty-five now. She teaches <span class="cn-word" data-tr="kimyo">chemistry</span> in Nurafshon and she has two sons, and she comes with a cake every June, which my father finds <span class="cn-word" data-pos="adj" data-tr="noqulay">embarrassing</span> and my mother does not.</p>

<p>Last summer my cousin put the cutting on the internet, and about four thousand people read it, and the comments <span class="cn-word" data-pos="verb" data-tr="takrorladilar">repeated</span> the same nine lines back to us with hearts under them.</p>

<p>My father asked me to write something under it. I did, in one line, and I did not <span class="cn-word" data-pos="verb" data-tr="oʻzgartirmadim">change</span> a word of what he gave me:</p>

<p><i>He <strong>says</strong> that he <strong>was</strong> afraid, that he <strong>is</strong> still afraid of fire, and that he <strong>went in anyway</strong>, and he would like the second part printed this time.</i></p>''',
        "questions": [
            {
                "text": "Why does the father keep correcting one line of the newspaper?",
                "choices": [
                    "Because he did not go into the house at all",
                    "Because \"he was not afraid\" teaches boys that only special people help — and he was an ordinary frightened boy",
                    "Because the paper spelled his name wrong",
                ],
                "answer": 1,
                "explanation": "Uning fikri: qoʻrqmagan odam hech kimga "
                               "hech narsa oʻrgatmaydi. Foydali qismi — "
                               "qoʻrqqan, lekin kirgan. Gazeta esa "
                               "foydasiz qismini bosgan.",
            },
            {
                "text": "He said: \"I was very afraid.\" Which report is correct?",
                "choices": [
                    "He said that he had been very afraid.",
                    "He said that he is very afraid.",
                    "He told that he was very afraid.",
                ],
                "answer": 0,
                "explanation": "<i>was</i> bir qadam orqaga suriladi va "
                               "<b>had been</b> boʻladi. <b>tell</b> "
                               "dan keyin esa darhol odam kerak "
                               "(<i>told me</i>).",
            },
            {
                "text": "In the last line, why is \"he is still afraid of fire\" NOT backshifted?",
                "choices": [
                    "Because it is a mistake",
                    "Because it is still true now",
                    "Because `afraid` is an adjective",
                ],
                "answer": 1,
                "explanation": "Gap hozir ham rost boʻlsa, zamonni "
                               "surish shart emas. Shakl tanlovi "
                               "maʼno beradi: u hozir ham "
                               "olovdan qoʻrqadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-63 — reported questions & commands  (one in the morning) [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "He Asked Where I Had Been",
        "summary": (
            "PE-63 matni. Taksida uyga qaytayotib, men otamning "
            "beradigan har bir savoliga javob tayyorlab qoʻydim. "
            "U esa butunlay boshqa savollarni berdi — va oxirgisi "
            "menikiga umuman oʻxshamas edi."
        ),
        "order":   63,
        "grammar": [
            {
                "pattern":  "Reported questions: no inversion, no ?",
                "meaning":  "Koʻchirilgan savolda soʻz tartibi "
                            "<b>oddiy gap</b>ga aylanadi va "
                            "savol belgisi yoʻqoladi. "
                            "Wh- savol: <i>“Where were you?”</i> → "
                            "<i>He asked <b>where I had been</b></i> "
                            "(<i>where had I been</i> ✗). "
                            "Yes/no savol: <i>“Did you eat?”</i> → "
                            "<i>He asked <b>if / whether</b> I had "
                            "eaten</i>.",
                "examples": ["He asked where I had been.",
                             "He asked if I had eaten anything."],
            },
            {
                "pattern":  "Orders and requests: tell / ask + to + V1",
                "meaning":  "Buyruq: <i>“Sit down.”</i> → <i>He "
                            "<b>told me to sit</b> down</i>. "
                            "Iltimos: <i>“Please close the door.”</i> "
                            "→ <i>He <b>asked me to close</b> the "
                            "door</i>. Inkor: <i>He told me "
                            "<b>not to</b> shout</i>.",
                "examples": ["He told me to sit down.",
                             "He asked me not to wake my mother."],
            },
            {
                "pattern":  "Reporting verbs beyond say and tell",
                "meaning":  "Feʼlning oʻzi ohangni tashiydi: "
                            "<b>explain</b>, <b>admit</b>, "
                            "<b>promise</b>, <b>warn</b>, "
                            "<b>advise</b>, <b>suggest</b>, "
                            "<b>refuse</b>. <i>He <b>admitted</b> "
                            "that he had been waiting since eleven</i> "
                            "— <i>said</i> dan ancha koʻp maʼlumot "
                            "beradi.",
                "examples": ["He admitted that he had been sitting there since eleven.",
                             "He advised me to keep my phone charged."],
            },
        ],
        "body": '''<p>The taxi came down our street at ten past one in the morning, and I had eleven answers ready.</p>

<p>I knew the questions. Everybody knows them. <i>Where were you? Who was with you? Why didn't you call? Do you know what time it is?</i> I had worked out the order of them somewhere around Beruniy, and I had an answer for each one that was true, mostly.</p>

<p>The <span class="cn-word" data-tr="ayvon">veranda</span> light was on. My father was sitting on the step in his coat with a cold glass of tea beside him, and he did not stand up when I came through the gate.</p>

<p>He <strong>asked where I had been</strong>. I told him. Dilnoza's brother's wedding, the second bus had not come, four of us had waited and then <span class="cn-word" data-pos="verb" data-tr="baham koʻrdik">split</span> a taxi.</p>

<p>He <strong>asked if</strong> I <strong>had eaten</strong> anything. I said I had.</p>

<p>He <strong>asked whether</strong> the driver <strong>had taken</strong> the main road, because of the <span class="cn-word" data-tr="yoʻl ishlari">roadworks</span> at the bridge, and I said he had.</p>

<p>Then he <strong>asked me to sit down</strong>, which was not on my list at all.</p>

<p>I sat on the <span class="cn-word" data-tr="zinapoya">step</span>. He <strong>admitted</strong> that he <strong>had been sitting</strong> there since eleven, and that my mother <strong>did not know</strong> he was outside. He <strong>told me not to wake</strong> her when we went in.</p>

<p>Then he <strong>explained</strong> that my mother's <span class="cn-word" data-tr="tahlil natijalari">test results</span> <strong>had come back</strong> from the <span class="cn-word" data-tr="poliklinika">clinic</span> on Thursday, two days before, and that she <strong>had asked him not to tell</strong> anybody until after the wedding, because Dilnoza's family had waited nine years for that wedding.</p>

<p>He <strong>said</strong> the word. He <strong>said</strong> that the doctors <strong>had used</strong> the <span class="cn-word" data-tr="ibora">phrase</span> "early", twice, and that there <strong>would be</strong> an <span class="cn-word" data-tr="operatsiya">operation</span> in Tashkent in eleven days.</p>

<p>I asked him three or four things. I do not remember them in order. He answered all of them, and then he <strong>warned</strong> me not to look at my mother in the morning "like a nurse", because she would understand in one second.</p>

<p>We sat on that step until about two. He <strong>asked</strong> me twice <strong>whether</strong> I <strong>was cold</strong>, and the second time he <strong>told me to take</strong> his <span class="cn-word" data-tr="palto">coat</span>, and I did, and he sat there in a shirt because he is like that.</p>

<p>The operation was in April 2023. My mother is fine. She <span class="cn-word" data-pos="verb" data-tr="oʻstiradi">grows</span> <span class="cn-word" data-tr="pomidor">tomatoes</span> and she <span class="cn-word" data-pos="verb" data-tr="janjallashadi">argues</span> with the <span class="cn-word" data-tr="qassob">butcher</span>, and none of the family photographs from that spring show anything at all.</p>

<p>I still come home late sometimes. He still asks where I have been. I answer properly now, every time, in full sentences, and I have never told him why.</p>''',
        "questions": [
            {
                "text": "What was the question the narrator had not prepared for?",
                "choices": [
                    "\"Do you know what time it is?\"",
                    "Being asked to sit down — because her father had news about her mother's test results",
                    "\"Who was with you?\"",
                ],
                "answer": 1,
                "explanation": "U tayyorlagan savollar odatdagi "
                               "savollar edi. “Oʻtir” — roʻyxatda "
                               "yoʻq edi: otasi onasining tahlil "
                               "natijalarini kutib oʻtirgan edi.",
            },
            {
                "text": "\"Where were you?\" reported correctly is:",
                "choices": [
                    "He asked where had I been.",
                    "He asked where I had been.",
                    "He asked where was I?",
                ],
                "answer": 1,
                "explanation": "Koʻchirilgan savolda inversiya "
                               "yoʻqoladi — soʻz tartibi oddiy gapdek "
                               "boʻladi va savol belgisi qoʻyilmaydi.",
            },
            {
                "text": "Which sentence reports a command?",
                "choices": [
                    "He asked if I had eaten.",
                    "He admitted that he had been waiting.",
                    "He told me not to wake her.",
                ],
                "answer": 2,
                "explanation": "Buyruq va iltimos <b>tell / ask + "
                               "(not) to + V1</b> shaklida "
                               "koʻchiriladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-64 — gerunds and infinitives  (the plov man)          [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "I Enjoy Cooking, I Want to Cook",
        "summary": (
            "PE-64 matni. Hovlimizda har shanba osh damlaydigan odam "
            "bor. U pul uchun ham, majburiyat uchun ham qilmaydi. "
            "Nima uchun qilishini bir kuni oʻzi aytdi — bitta gap bilan."
        ),
        "order":   64,
        "grammar": [
            {
                "pattern":  "-ing after a preposition — the rule that never fails",
                "meaning":  "Har qanday predlogdan keyin "
                            "<b>V-ing</b>: <i>good <b>at</b> "
                            "cooking</i>, <i>tired <b>of</b> "
                            "explaining</i>, <i><b>without</b> "
                            "saying</i>, <i><b>instead of</b> "
                            "sleeping</i>. <i>to</i> ham baʼzan "
                            "predlog boʻladi: <i>look forward "
                            "<b>to seeing</b> you</i>.",
                "examples": ["He is good at counting people.",
                             "He left without saying goodbye."],
            },
            {
                "pattern":  "Verbs that take -ing vs verbs that take to + V1",
                "meaning":  "<b>-ing</b>: enjoy · like · love · hate · "
                            "mind · avoid · finish · keep · suggest · "
                            "practise. <b>to + V1</b>: want · need · "
                            "decide · hope · promise · agree · learn · "
                            "refuse · seem · manage. Shuning uchun "
                            "<i>I <b>enjoy cooking</b></i> va "
                            "<i>I <b>want to cook</b></i> — ikkisi "
                            "ham toʻgʻri, lekin joyi almashmaydi.",
                "examples": ["I enjoy cooking for forty people.",
                             "I have never wanted to cook for money."],
            },
            {
                "pattern":  "The gerund as a noun, and the -ing subject",
                "meaning":  "<b>V-ing</b> gapda ega ham boʻladi: "
                            "<i><b>Cooking</b> for one person is "
                            "boring</i>, <i><b>Waiting</b> is the "
                            "hard part</i>. Xato: <i>Cook for one "
                            "person is boring</i> ✗. Baʼzi feʼllar "
                            "bilan ikkisi ham boʻladi: "
                            "<i>It started <b>to rain</b> / "
                            "<b>raining</b></i>.",
                "examples": ["Cooking for one person is boring.",
                             "Counting the guests is his job, not mine."],
            },
        ],
        "body": '''<p>Every Saturday at about six in the morning, Ravshan aka comes down into our <span class="cn-word" data-tr="hovli">courtyard</span> with a bag of <span class="cn-word" data-tr="sabzi">carrots</span> and starts a fire under a <span class="cn-word" data-tr="qozon">cauldron</span> that does not belong to him.</p>

<p>He is fifty-eight. He works in a bank — thirty-one years in the same building, four floors, numbers all day.</p>

<p>He is very good <strong>at counting</strong> people, which is the part everybody forgets about <strong>cooking</strong> for a courtyard. Forty-two people live in our block. He knows who is away, who is fasting, who does not eat meat since her operation, and who will say no and then come down at two o'clock <strong>without saying</strong> anything.</p>

<p><strong>Cooking</strong> for one person is boring, he says. <strong>Cooking</strong> for forty-two is <span class="cn-word" data-tr="arifmetika">arithmetic</span>, and he likes arithmetic.</p>

<p>He does not <strong>need to</strong> do it. Nobody pays him. Twice a family has tried <strong>to give</strong> him money for the meat and he has <strong>refused to take</strong> it, politely, and once <span class="cn-word" data-pos="adv" data-tr="qoʻpol tarzda">rudely</span>, because the second time they <span class="cn-word" data-pos="verb" data-tr="qatʼiy turdilar">insisted</span>.</p>

<p>Two years ago a <span class="cn-word" data-tr="restoran">restaurant</span> on our road <span class="cn-word" data-pos="verb" data-tr="taklif qildi">offered</span> him work on Saturdays and Sundays. Real money — more than his bank pays him for a week. He <span class="cn-word" data-pos="verb" data-tr="rad etdi">turned</span> it down in about four seconds and he did not tell his wife for a month, and when she found out she did not speak to him for two days, which he <span class="cn-word" data-pos="verb" data-tr="tan oladi">admits</span> was fair.</p>

<p>My grandmother asked him about it in front of everybody last spring, in the way that only a woman of eighty can ask a man of fifty-eight.</p>

<p>He was <span class="cn-word" data-pos="verb" data-tr="tozalayotgan">washing</span> rice at the time. He did not stop <span class="cn-word" data-pos="verb" data-tr="ishlashdan">working</span>, and he did not look at her.</p>

<p>"I <strong>enjoy cooking</strong>," he said. "I do not <strong>want to be paid for cooking</strong>. In 1991 my mother and I ate in this courtyard for two months from other people's <span class="cn-word" data-tr="qozonlar">pots</span>, and nobody <span class="cn-word" data-pos="verb" data-tr="eslatib qoʻymadi">mentioned</span> it once, and I have decided <strong>to pay</strong> that back in <span class="cn-word" data-tr="guruch">rice</span> for the rest of my life. It is <span class="cn-word" data-pos="adj" data-tr="arzon">cheap</span> at the price."</p>

<p>Then he <span class="cn-word" data-pos="verb" data-tr="soʻradi">asked</span> my grandmother <strong>to taste</strong> the salt, because she is the only person in the building he trusts with that, and she took it very seriously, and the two of them argued about it for a while.</p>''',
        "questions": [
            {
                "text": "Why does Ravshan aka refuse money for cooking?",
                "choices": [
                    "He is paid well at the bank and does not need it",
                    "In 1991 the courtyard fed him and his mother for two months, and he is paying it back in rice",
                    "He does not think his cooking is good enough",
                ],
                "answer": 1,
                "explanation": "1991-yilda u va onasi ikki oy shu "
                               "hovlining qozonlaridan ovqatlangan, va "
                               "hech kim buni eslatmagan. U qarzni "
                               "guruch bilan qaytaryapti.",
            },
            {
                "text": "Which pair is correct?",
                "choices": [
                    "I enjoy to cook, but I don't want cooking for money.",
                    "I enjoy cooking, but I don't want to cook for money.",
                    "I enjoy cook, but I don't want cook for money.",
                ],
                "answer": 1,
                "explanation": "<b>enjoy</b> dan keyin har doim "
                               "<b>-ing</b>, <b>want</b> dan keyin har "
                               "doim <b>to + V1</b>. Bu ikki roʻyxat "
                               "almashmaydi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "He is good at count people.",
                    "He is good at counting people.",
                    "He is good at to count people.",
                ],
                "answer": 1,
                "explanation": "Predlogdan keyin (<i>at</i>) doim "
                               "<b>V-ing</b> keladi — bu qoida hech "
                               "qachon buzilmaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-65 — stop doing vs stop to do  (the lorry driver)    [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "He Stopped to Help",
        "summary": (
            "PE-65 matni. Bobom 1998-yilda odamlarga yordam berishni "
            "toʻxtatdi. Otam esa 2016-yilda toʻxtab, yordam berdi — "
            "va bu unga bitta telefon va toʻrt soatga tushdi. "
            "Ikki gap, bitta soʻz — va butunlay boshqa maʼno."
        ),
        "order":   65,
        "grammar": [
            {
                "pattern":  "stop doing vs stop to do",
                "meaning":  "<b>stop + V-ing</b> — ishning oʻzini "
                            "tugatish: <i>He <b>stopped helping</b> "
                            "people</i> (endi yordam bermaydi). "
                            "<b>stop + to + V1</b> — boshqa ish uchun "
                            "toʻxtash: <i>He <b>stopped to help</b> "
                            "somebody</i> (mashinani toʻxtatdi, "
                            "yordam berdi). Bir soʻz farqi — "
                            "teskari maʼno.",
                "examples": ["My grandfather stopped helping strangers in 1998.",
                             "My father stopped to help a woman on the Guliston road."],
            },
            {
                "pattern":  "remember / forget: which order?",
                "meaning":  "<b>remember to do</b> — kerakli ishni "
                            "yodda tutib qilish (<i>Remember <b>to "
                            "lock</b> the cab</i>). <b>remember "
                            "doing</b> — oʻtgan voqeani eslash "
                            "(<i>I remember <b>standing</b> on that "
                            "road</i>). <b>forget</b> ham xuddi "
                            "shunday ishlaydi.",
                "examples": ["Remember to take water in July.",
                             "I remember sitting in that cab at midnight."],
            },
            {
                "pattern":  "try, go on, and need + -ing",
                "meaning":  "<b>try to do</b> — urinib koʻrish "
                            "(qiyin ish), <b>try doing</b> — "
                            "tajriba qilib koʻrish (boshqa yoʻl). "
                            "<b>go on doing</b> — davom etish, "
                            "<b>go on to do</b> — keyin boshqa "
                            "ishga oʻtish. <b>need + -ing</b> esa "
                            "passiv maʼno beradi: <i>The tyre "
                            "<b>needs changing</b></i> = "
                            "<i>needs to be changed</i>.",
                "examples": ["He tried to push the car and then tried putting stones under the wheel.",
                             "The spare tyre needs changing."],
            },
        ],
        "body": '''<p>My grandfather <strong>stopped helping</strong> <span class="cn-word" data-tr="notanish odamlar">strangers</span> on the road in the autumn of 1998, and he had a reason.</p>

<p>He drove a <span class="cn-word" data-tr="yuk mashinasi">lorry</span> between Tashkent and Termez for twenty-six years. In September that year he <strong>stopped to help</strong> two men with a <span class="cn-word" data-tr="ochilgan gʻildirak">flat tyre</span> south of Guliston, at night, and while he was under their car with their <span class="cn-word" data-tr="domkrat">jack</span>, one of them took his bag, his <span class="cn-word" data-tr="hujjatlar">documents</span> and eleven months of saved money out of his <span class="cn-word" data-tr="kabina">cab</span>.</p>

<p>He walked into the <span class="cn-word" data-tr="militsiya boʻlimi">police station</span> in Guliston at four in the morning and he never got any of it back.</p>

<p>After that he drove past everybody. My grandmother says he would go quiet for about a kilometre afterwards, every time, and then talk about something else. He <strong>went on driving</strong> that road for another eleven years like that.</p>

<p>My father took over the lorry in 2011, and he has a different rule, and it is written on a piece of card above the <span class="cn-word" data-tr="old oyna">windscreen</span> in <span class="cn-word" data-tr="qoʻl yozuvi">handwriting</span> I know: <i>Always stop. Lock the cab.</i> My grandfather wrote that card himself, which took me years to understand.</p>

<p>In February 2016 my father <strong>stopped to help</strong> a woman with two children and a dead <span class="cn-word" data-tr="akkumulyator">battery</span> on the Guliston road, at eleven at night, in the rain, at almost exactly the same place.</p>

<p>He <strong>tried to start</strong> her car from his own battery and it did not work. Then he <strong>tried putting</strong> the children in his cab with the <span class="cn-word" data-tr="pech">heater</span> on while he waited with her, because a woman does not get into a lorry with a stranger at eleven at night and he understood that <span class="cn-word" data-pos="adv" data-tr="darhol">immediately</span>.</p>

<p>They waited four hours for her brother to come from Sirdaryo. My father lost half a night and, somewhere in those four hours, a phone that he had left on the <span class="cn-word" data-tr="oʻrindiq">seat</span> with the door open.</p>

<p>He <strong>remembers standing</strong> in that rain and thinking about his father under the other car in 1998, eighteen years and about two hundred metres away.</p>

<p>He <strong>did not stop helping</strong> people. That is the whole story, and my grandfather knew it would go that way, which is why he wrote the card instead of the rule he actually lived by.</p>

<p>My father is fifty-one. He tells me two things every time I take a car anywhere: <strong>remember to lock</strong> it, and do not <strong>stop being</strong> the kind of person who stops.</p>''',
        "questions": [
            {
                "text": "What is the difference between the grandfather and the father?",
                "choices": [
                    "The grandfather stopped helping strangers; the father goes on stopping to help them",
                    "The father never helps anybody",
                    "The grandfather never drove that road again",
                ],
                "answer": 0,
                "explanation": "Bobo 1998-yildan keyin yordam berishni "
                               "butunlay toʻxtatdi. Otasi esa "
                               "toʻxtab yordam berishni davom "
                               "ettirdi — hatto telefonini yoʻqotib "
                               "ham.",
            },
            {
                "text": "\"He stopped to help a woman\" means:",
                "choices": [
                    "he did not help her any more",
                    "he stopped his lorry in order to help her",
                    "he tried to help but could not",
                ],
                "answer": 1,
                "explanation": "<b>stop + to + V1</b> — maqsad uchun "
                               "toʻxtash. Ishni tugatish "
                               "<b>stop + V-ing</b> boʻlar edi: "
                               "<i>stopped helping</i>.",
            },
            {
                "text": "Which sentence is about a memory of the past?",
                "choices": [
                    "Remember to lock the cab.",
                    "He remembers standing in that rain.",
                    "He remembered to take water.",
                ],
                "answer": 1,
                "explanation": "<b>remember + V-ing</b> — oʻtgan "
                               "voqeani eslash. <b>remember + to "
                               "V1</b> esa qilinishi kerak boʻlgan "
                               "ishni yodda tutish.",
            },
        ],
    },
]
