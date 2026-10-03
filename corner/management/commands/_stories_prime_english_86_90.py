# -*- coding: utf-8 -*-
"""Prime English Readings — PE-86 … PE-90 (batch 18). Written English, built and joined.

PE-86 participle clauses · PE-87 the unreal past · PE-88 linking words for writing ·
PE-89 prefixes & suffixes · PE-90 collocations. All five are WRITTEN English (see the
toc's register rule from PE-83): a biography, an opinion column, a report, an essay,
a guide's notebook.

Shapes (varied on purpose):
  86 — a TRUE BIOGRAPHY: Emily Warren Roebling and the Brooklyn Bridge (1869–1883)
  87 — an OPINION COLUMN: the tap that dripped for three years, and the neighbour's bucket
  88 — a REPORT WITH NUMBERS: the 2022 UK four-day-week pilot
  89 — an ESSAY by a translator: his grandfather's Uzbek suffixes and the English ones
  90 — a GUIDE'S NOTEBOOK: a Bukhara tour guide and the words that live together

NARRATOR VOICE (see the toc's AUDIO section):
    86 en-US-JennyNeural · 87 en-US-GuyNeural · 88 en-US-JennyNeural
    89 en-US-GuyNeural   · 90 en-US-JennyNeural
(Batch 17 ran 3 male / 2 female, so this one flips to 2 male / 3 female.)
Generate one story at a time:
    python manage.py gen_corner_audio --collection="Prime English Readings" \
        --only 86 --voice en-US-JennyNeural

Facts are true as written. 86: John A. Roebling's foot was crushed by a ferry in 1869 and
he died of tetanus; Washington Roebling was disabled by caisson disease in 1872 and
watched the work through a telescope from Brooklyn Heights; Emily studied the engineering
and carried his instructions; she was the first to cross the bridge, carrying a rooster,
before it opened on 24 May 1883; its main span (486 m) was then the longest of any
suspension bridge. 88: the UK pilot ran June–December 2022 with 61 companies and about
2,900 workers; 56 continued afterwards, 18 permanently; revenue was broadly unchanged.
89: Uzbek -siz / -chi / -lik and the Persian prefixes be- / no- are as described.

Cumulative rule: everything through each reading's own lesson is free. 86 adds
participle clauses; 87 the unreal past; 88 however / therefore / although; 89 word
formation; 90 collocations. Nothing from 91+ is a grammar point that could leak.
Length: 300–360 words. Vocabulary: 16–22 cn-word marks.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_86_90.py --author=prime
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
    # PE-86 — participle clauses   (Emily Roebling, 1869–1883)     [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Standing on the Bridge, She Understood",
        "summary": (
            "PE-86 matni. Haqiqiy hayot hikoyasi: Bruklin koʻprigini otasi "
            "loyihalagan, oʻgʻli qurgan — lekin oʻn bir yil davomida "
            "muhandislarga buyruqlarni Emili Roebling yetkazgan. Koʻprikdan "
            "birinchi boʻlib u oʻtgani bejiz emas."
        ),
        "order":   86,
        "grammar": [
            {
                "pattern":  "-ing clause (active) and -ed clause (passive) at the start of a sentence",
                "meaning":  "Ikki gapni bittaga siqish: <i>She stood on the bridge. "
                            "She understood.</i> → <b>Standing</b> on the bridge, she "
                            "understood. Ega oʻzi harakat qilsa — <b>-ing</b>; unga "
                            "nisbatan qilinsa — <b>V3</b>: <b>Crushed</b> by a ferry, "
                            "his foot… Bu yozma uslub.",
                "examples": ["Watching through a telescope, he followed every cable.",
                             "Crushed between a ferry and the pier, his foot never healed.",
                             "Trained by her husband, Emily learned the mathematics."],
            },
            {
                "pattern":  "Having + V3 — the earlier action",
                "meaning":  "Bir ish ikkinchisidan <b>oldin</b> tugagan boʻlsa: "
                            "<b>Having lost</b> his father, Washington took over. "
                            "Qoida bitta: ikkala qismning <b>egasi bir xil</b> boʻlishi "
                            "shart — aks holda gap kulgili boʻlib qoladi.",
                "examples": ["Having lost his father, Washington took over the work.",
                             "Having studied for months, she could argue with engineers."],
            },
        ],
        "body": '''<p>The Brooklyn Bridge was designed by one Roebling, built by a second and finished by a third — and for a long time only two of them were remembered.</p>

<p>The first was John Roebling, the engineer who drew the plans. In 1869, <strong>surveying</strong> the site from a <span class="cn-word" data-tr="iskala, prichal">pier</span>, he was hit by a <span class="cn-word" data-tr="parom">ferry</span>. <strong>Crushed</strong> between the boat and the wood, his foot never healed, and he died of <span class="cn-word" data-tr="qoqshol (kasallik)">tetanus</span> a few weeks later.</p>

<p><strong>Having lost</strong> his father, Washington Roebling took over the work at the age of thirty-two. He spent long days in the <span class="cn-word" data-tr="kesson (suv ostidagi kamera)">caissons</span>, the airtight chambers sunk into the riverbed, and in 1872 he was struck by the <span class="cn-word" data-tr="kesson kasalligi">caisson disease</span> that killed several of his workers. <span class="cn-word" data-pos="adj" data-tr="qisman falaj">Partly paralysed</span>, often in great pain, he could no longer visit the site.</p>

<p>The bridge did not stop, and the reason was his wife. <strong>Watching</strong> through a <span class="cn-word" data-tr="teleskop">telescope</span> from his window in Brooklyn Heights, Washington followed every cable and every stone; Emily carried his instructions to the site. To do this well, she had to understand them. <strong>Trained</strong> by her husband and by her own reading, she studied higher mathematics, the strength of materials and the <span class="cn-word" data-tr="hisob-kitob">calculation</span> of cables. Within a few years engineers were bringing their questions to her, and some of them <span class="cn-word" data-pos="verb" data-tr="shubha qilmoq">suspected</span> that she, not her husband, was now the real chief engineer.</p>

<p>It was not an easy position. Politicians tried to <span class="cn-word" data-pos="verb" data-tr="ishdan olmoq">remove</span> Washington from the project, and it was Emily who spoke for him to the men who wanted him gone. <strong>Having heard</strong> her, they let him stay.</p>

<p>In May 1883, shortly before the bridge opened, Emily Roebling became the first person to cross it, riding in a carriage and carrying a <span class="cn-word" data-tr="xoroz">rooster</span> as a sign of victory. Its main <span class="cn-word" data-tr="oraliq (koʻprik)">span</span>, 486 metres long, was then the longest of any <span class="cn-word" data-tr="osma (koʻprik)">suspension</span> bridge in the world.</p>

<p><strong>Standing</strong> on that bridge, she understood something that took the city much longer to <span class="cn-word" data-pos="verb" data-tr="tan olmoq">admit</span>: <span class="cn-word" data-pos="adj" data-tr="oʻtkir, puxta">sharp</span> work can be done by someone whose name is not on the plans. A <span class="cn-word" data-tr="lavha">plaque</span> on the bridge today names all three Roeblings.</p>''',
        "questions": [
            {
                "text": "Why did Emily Roebling learn engineering?",
                "choices": [
                    "Because she wanted to design her own bridge",
                    "Because she had to understand her husband's instructions to carry them to the site",
                    "Because the politicians asked her to replace her husband",
                ],
                "answer": 1,
                "explanation": "Vashington kasal edi va qurilishga bora olmasdi — "
                               "Emili uning buyruqlarini yetkazar edi, buning uchun "
                               "ularni tushunishi kerak edi.",
            },
            {
                "text": "Which sentence uses a participle clause correctly?",
                "choices": [
                    "Watching through a telescope, Washington followed every cable.",
                    "Watching through a telescope, every cable was followed.",
                    "Watched through a telescope, Washington followed every cable.",
                ],
                "answer": 0,
                "explanation": "Ega bir xil boʻlishi kerak: teleskopdan <b>Vashington</b> "
                               "qaradi va kuzatdi. Ikkinchi gapda «kabel teleskopdan "
                               "qaradi» boʻlib qoladi; uchinchisida «Vashingtonga qarashdi».",
            },
            {
                "text": "'Having lost his father, Washington took over.' What does 'Having lost' show?",
                "choices": [
                    "The two things happened at exactly the same time",
                    "Losing his father came before taking over",
                    "Washington took over before his father died",
                ],
                "answer": 1,
                "explanation": "<b>Having + V3</b> — oldin tugagan harakat: avval otasi "
                               "vafot etdi, keyin u ishni oʻz qoʻliga oldi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-87 — the unreal past   (an opinion column)                 [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "It's Time We Talked About Water",
        "summary": (
            "PE-87 matni. Gazeta ustuni: muallifning uyidagi kran uch yil "
            "tomchilab turdi. Qoʻshni kampir esa shu tomchilarni chelakda "
            "yigʻib, gullarini sugʻorgan — va muallifga bir gap aytgan."
        ),
        "order":   87,
        "grammar": [
            {
                "pattern":  "It's (high) time + subject + past simple",
                "meaning":  "Ish allaqachon qilinishi kerak edi: <i>It's time we "
                            "<b>talked</b></i> — oʻtgan zamon shakli, lekin maʼnosi "
                            "<b>hozir</b>. <b>high</b> — tanqidni kuchaytiradi. "
                            "Muqobili: <i>It's time <b>to talk</b>.</i>",
                "examples": ["It's time we talked about water.",
                             "It's high time somebody fixed that tap."],
            },
            {
                "pattern":  "would rather + subject + past; as if / as though + past",
                "meaning":  "Boshqa odam haqida xohish: <i>I'd rather you <b>fixed</b> "
                            "the tap</i>. Haqiqatga zid taqqoslash: <i>We live <b>as "
                            "if</b> water <b>were</b> endless</i> (lekin u cheksiz emas). "
                            "Rasmiy yozuvda <b>were</b> barcha shaxslar uchun.",
                "examples": ["I'd rather you fixed the tap than praised my bucket.",
                             "We use water as if it were free."],
            },
        ],
        "body": '''<p>For three years the tap in the <span class="cn-word" data-tr="hovli">courtyard</span> of my building <span class="cn-word" data-pos="verb" data-tr="tomchilamoq">dripped</span>. Everybody walked past it. Somebody would fix it. It belonged to the building, which meant that it belonged to nobody.</p>

<p>Last month I finally did the <span class="cn-word" data-tr="hisob-kitob">arithmetic</span>. One drop every two seconds is about forty litres a day. Over three years, that small sound had <span class="cn-word" data-pos="verb" data-tr="oqizib yubormoq">poured away</span> more than forty thousand litres of clean water, <span class="cn-word" data-pos="adj" data-tr="tozalangan">treated</span>, pumped and paid for.</p>

<p>Only then did I notice the bucket. Standing under the tap, half hidden by a <span class="cn-word" data-tr="atirgul buta">rosebush</span>, was an old blue bucket. It belonged to Nodira opa on the ground floor, who is eighty-one. For three years she had been collecting the drip and <span class="cn-word" data-pos="verb" data-tr="sugʻormoq">watering</span> her roses with it.</p>

<p>I told her, with some <span class="cn-word" data-tr="hayrat">admiration</span>, that she was the only person in the building who had treated the leak seriously. She looked at me as if I were a slow pupil. "I'd rather you <strong>fixed</strong> the tap," she said, "than <strong>praised</strong> my bucket."</p>

<p>She is right, and it is not only about one tap. Most of this country's water goes to the fields, and much of it is lost on the way, through open <span class="cn-word" data-tr="ariq, kanal">channels</span> and old pipes. Our homes use a smaller share, yet we behave <strong>as if</strong> the supply <strong>were</strong> endless: we wash cars with <span class="cn-word" data-tr="shlang">hoses</span>, leave taps running while we brush our teeth, and <span class="cn-word" data-pos="verb" data-tr="eʼtibor bermaslik">ignore</span> drips that we would never ignore if each drop cost us a coin.</p>

<p><strong>It's time we talked</strong> about water as what it is: a <span class="cn-word" data-tr="resurs, boylik">resource</span> that runs out. <strong>It's high time</strong> buildings had someone <span class="cn-word" data-pos="adj" data-tr="masʼul">responsible</span> for their shared taps and pipes. And I would rather the city <strong>spent</strong> money on fixing leaks than on another <span class="cn-word" data-tr="favvora">fountain</span>.</p>

<p>A <span class="cn-word" data-tr="santexnik">plumber</span> came on Tuesday. The repair took eleven minutes and cost less than a taxi ride. The courtyard is silent now, and Nodira opa waters her roses from a <span class="cn-word" data-tr="koʻza">jug</span>.</p>

<p>She told me yesterday that the roses do not seem to mind. Then she asked me when I was going to write about the pipe behind the school. It drips too, she said.</p>''',
        "questions": [
            {
                "text": "What did Nodira opa mean by 'I'd rather you fixed the tap than praised my bucket'?",
                "choices": [
                    "She wanted the writer to buy her a new bucket",
                    "She preferred action on the leak to compliments about her bucket",
                    "She thought the roses needed more water",
                ],
                "answer": 1,
                "explanation": "U maqtovni emas, harakatni xohlaydi: kranni tuzatish — "
                               "chelakni maqtashdan muhimroq.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "It's time we talk about water.",
                    "It's time we talked about water.",
                    "It's time we will talk about water.",
                ],
                "answer": 1,
                "explanation": "<b>It's time + ega + oʻtgan zamon</b>: "
                               "<i>we talked</i>. Shakl oʻtgan, maʼno esa hozirgi — "
                               "«allaqachon gaplashishimiz kerak edi».",
            },
            {
                "text": "'We behave as if the supply were endless.' What does this tell us?",
                "choices": [
                    "The supply is endless",
                    "The supply is not endless, but we behave as though it is",
                    "The supply was endless in the past",
                ],
                "answer": 1,
                "explanation": "<b>as if + were</b> — haqiqatga zid taqqoslash: "
                               "suv cheksiz emas, biz esa uni shunday deb ishlatamiz.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-88 — linking words   (a report: the four-day week)        [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "However, Therefore, Although",
        "summary": (
            "PE-88 matni. Hisobot: 2022-yilda Buyuk Britaniyada 61 ta kompaniya "
            "olti oy davomida haftada toʻrt kun ishladi. Natijalar — va nima "
            "uchun ularni ehtiyotkorlik bilan oʻqish kerak."
        ),
        "order":   88,
        "grammar": [
            {
                "pattern":  "contrast: however (new sentence) · although (inside the sentence) · despite + noun",
                "meaning":  "<b>However</b> — yangi gap boshida, keyin vergul. "
                            "<b>Although</b> — bitta gap ichida, oʻzidan keyin toʻliq "
                            "gap. <b>Despite</b> — faqat ot yoki -ing: <i>despite the "
                            "shorter week</i>, <i>despite working less</i> "
                            "(<i>despite of</i> ✗).",
                "examples": ["However, the companies were not chosen at random.",
                             "Although they worked one day less, revenue did not fall.",
                             "Despite the shorter week, output held steady."],
            },
            {
                "pattern":  "result and addition: therefore, as a result, moreover, in addition",
                "meaning":  "Natija: <b>therefore</b> (rasmiy), <b>as a result</b>. "
                            "Qoʻshimcha: <b>moreover</b>, <b>in addition</b>. "
                            "Hammasi gap boshida vergul bilan, yoki "
                            "<i>; therefore,</i> bilan ikki gap orasida. Ortiqcha "
                            "ishlatmang — har jumlada bitta yetarli.",
                "examples": ["As a result, 56 of the 61 companies continued.",
                             "Moreover, fewer staff left their jobs.",
                             "The sample was small; therefore, the results need care."],
            },
        ],
        "body": '''<p>Between June and December 2022, sixty-one companies in the United Kingdom took part in the largest <span class="cn-word" data-tr="sinov loyihasi">pilot</span> of a four-day working week at that time. About 2,900 employees moved to a <span class="cn-word" data-tr="qisqartirilgan">reduced</span> <span class="cn-word" data-tr="ish jadvali">schedule</span> with no loss of pay. The companies ranged from a fish-and-chip shop to software and <span class="cn-word" data-tr="marketing">marketing</span> firms, and the results were studied by researchers from the universities of Cambridge and Boston College.</p>

<p>The headline result was <span class="cn-word" data-pos="adj" data-tr="aniq, yaqqol">striking</span>. Of the sixty-one companies, fifty-six decided to continue the four-day week after the trial ended, and eighteen made the change <span class="cn-word" data-pos="adv" data-tr="doimiy ravishda">permanently</span>. <strong>Although</strong> employees worked one day less, the companies' <span class="cn-word" data-tr="tushum, daromad">revenue</span> stayed broadly the same over the trial period. <strong>Moreover</strong>, the number of staff who left their jobs fell sharply compared with the same period a year earlier, and the number of sick days fell too.</p>

<p><strong>However</strong>, the results need careful reading. The companies <span class="cn-word" data-pos="verb" data-tr="koʻngilli boʻlmoq">volunteered</span> for the pilot; they were not chosen at random. A firm that expects a shorter week to work is more likely to sign up for one, and more likely to make it succeed. <strong>Therefore</strong>, the pilot shows that a four-day week can work in some companies, not that it would work in every company.</p>

<p><strong>In addition</strong>, six months is a short time. Some <span class="cn-word" data-tr="foydalar">benefits</span> of a new routine fade when it stops being new, and some costs appear only later. <strong>Despite</strong> these <span class="cn-word" data-tr="cheklovlar">limitations</span>, the pilot <span class="cn-word" data-pos="verb" data-tr="oʻzgartirmoq">shifted</span> the debate. Before 2022, critics argued that a shorter week would simply mean less work done. <strong>As a result</strong> of trials like this one, the question has changed: it is now less whether a four-day week is possible than for whom, and on what <span class="cn-word" data-tr="shartlar">terms</span>.</p>

<p>For readers who write reports themselves, the pilot also offers a <span class="cn-word" data-pos="adj" data-tr="kichik, sezilmas">quieter</span> lesson. A good report <span class="cn-word" data-pos="verb" data-tr="ajratmoq">separates</span> what the data show from what we would like them to show. <strong>Although</strong> the first is less exciting, it is the part that <span class="cn-word" data-pos="verb" data-tr="chidamoq, saqlanib qolmoq">survives</span> the next <span class="cn-word" data-tr="tadqiqot">study</span>.</p>''',
        "questions": [
            {
                "text": "Why does the report say the results 'need careful reading'?",
                "choices": [
                    "Because the companies lost a lot of money",
                    "Because the companies chose to take part, so they may not represent all companies",
                    "Because only one company continued after the trial",
                ],
                "answer": 1,
                "explanation": "Kompaniyalar oʻzlari qatnashishni tanlagan — tasodifiy "
                               "tanlanmagan. Shuning uchun natija «hamma kompaniyada "
                               "ishlaydi» degani emas.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "Despite of the shorter week, revenue did not fall.",
                    "Despite the shorter week, revenue did not fall.",
                    "Despite the week was shorter, revenue did not fall.",
                ],
                "answer": 1,
                "explanation": "<b>despite + ot</b> (<i>the shorter week</i>), <i>of</i> "
                               "siz. Toʻliq gap kerak boʻlsa — <b>although</b>: "
                               "<i>Although the week was shorter…</i>",
            },
            {
                "text": "Which linking word best fills the gap: 'The companies volunteered. ___, the results may not apply to every company.'",
                "choices": ["Therefore", "Although", "Moreover"],
                "answer": 0,
                "explanation": "Ikkinchi gap birinchisining <b>natijasi</b> — "
                               "<b>Therefore</b>. <i>Although</i> gap boshida yangi gap "
                               "boshlay olmaydi; <i>Moreover</i> — qoʻshimcha, natija emas.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-89 — prefixes & suffixes   (a translator's essay)          [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Word Factory",
        "summary": (
            "PE-89 matni. Tarjimonning esesi: bobosi ingliz tilini bilmasdi, "
            "lekin oʻzbekcha -siz, -chi, -lik qoʻshimchalarini oʻyin qilib "
            "oʻrgatgan edi. Yillar oʻtib nevara inglizcha -less, -er, -ness da "
            "xuddi shu zavodni tanidi."
        ),
        "order":   89,
        "grammar": [
            {
                "pattern":  "prefixes that mean 'not': un- · in- / im- / il- / ir- · dis-",
                "meaning":  "Old qoʻshimcha soʻzning <b>maʼnosini</b> teskari qiladi, "
                            "turkumini emas: <i>happy → <b>un</b>happy</i>, "
                            "<i>possible → <b>im</b>possible</i>, <i>legal → "
                            "<b>il</b>legal</i>, <i>agree → <b>dis</b>agree</i>. "
                            "Oʻzbekchadagi <b>be-</b> (<i>bebaxt</i>) va <b>no-</b> "
                            "(<i>noqonuniy</i>) xuddi shu ishni qiladi.",
                "examples": ["unhappy, impossible, illegal, irregular, disagree"],
            },
            {
                "pattern":  "suffixes change the word's job: -er · -ness · -less · -ful · -able · -ly",
                "meaning":  "Oxirgi qoʻshimcha soʻz <b>turkumini</b> oʻzgartiradi: "
                            "<i>work → work<b>er</b></i> (ot), <i>kind → kind<b>ness</b></i> "
                            "(ot), <i>home → home<b>less</b></i> (sifat), "
                            "<i>believe → believ<b>able</b></i> → <i><b>un</b>believ"
                            "<b>ably</b></i>. Oʻzbekcha -chi, -lik, -siz bilan solishtiring.",
                "examples": ["ishchi — worker", "doʻstlik — friendship", "uysiz — homeless",
                             "believe → believable → unbelievable → unbelievably"],
            },
        ],
        "body": '''<p>My grandfather never learned a word of English. He was a <span class="cn-word" data-tr="etikdoʻz">shoemaker</span> in Namangan, and he left school at twelve. Yet he taught me how an English word is built.</p>

<p>He played a game with me in his <span class="cn-word" data-tr="ustaxona">workshop</span>. He would say a <span class="cn-word" data-tr="ildiz (soʻz)">root</span> — <i>ish</i>, <i>uy</i>, <i>doʻst</i> — and I had to build as many words from it as I could. <i>Ish</i> gave me <i>ishchi</i>, <i>ishsiz</i>, <i>ishlamoq</i>. <i>Uy</i> gave me <i>uysiz</i> and <i>uychi</i>, which made him laugh, because it is not a word. <i>Doʻst</i> gave me <i>doʻstlik</i>. "A word is not a stone," he used to say. "It is a piece of <span class="cn-word" data-tr="charm, teri">leather</span>. You cut it and <span class="cn-word" data-pos="verb" data-tr="tikmoq">sew</span> it, and it becomes a shoe."</p>

<p>Twenty years later, <span class="cn-word" data-pos="verb" data-tr="tayyorgarlik koʻrmoq">preparing</span> for my first translation exam, I opened an English grammar and found his workshop inside it. <i>Work</i> became <strong>worker</strong>, just as <i>ish</i> became <i>ishchi</i>. <i>Home</i> became <strong>homeless</strong>, as <i>uy</i> became <i>uysiz</i>. <i>Friend</i> became <strong>friendship</strong>, and <i>kind</i> became <strong>kindness</strong>, the way <i>doʻst</i> becomes <i>doʻstlik</i>. Even the negatives were <span class="cn-word" data-pos="adj" data-tr="tanish">familiar</span>. Our <i>be-</i>, <span class="cn-word" data-pos="adj" data-tr="oʻzlashtirilgan">borrowed</span> from Persian, makes <i>baxtli</i> into <i>bebaxt</i>; English <strong>un-</strong> makes <i>happy</i> into <strong>unhappy</strong>. Our <i>no-</i> makes <i>qonuniy</i> into <i>noqonuniy</i>; English uses <strong>il-</strong> and turns <i>legal</i> into <strong>illegal</strong>.</p>

<p>The two factories are not <span class="cn-word" data-pos="adj" data-tr="bir xil">identical</span>. English has more prefixes than Uzbek. It also has traps. <strong>Hardly</strong> does not mean "in a hard way"; it means "almost not". And <span class="cn-word" data-tr="koʻplab, juda koʻp">plenty</span> of English words take <strong>in-</strong> before some roots and <strong>im-</strong> before others for reasons of sound: <strong>impossible</strong>, <strong>immature</strong>, but <strong>inactive</strong>.</p>

<p>Still, the habit he gave me works. When I meet an <span class="cn-word" data-pos="adj" data-tr="notanish">unfamiliar</span> word now, I take it apart before I reach for a dictionary. <strong>Unbelievably</strong> is <i>un-</i> + <i>believe</i> + <i>-able</i> + <i>-ly</i>: four pieces, one meaning. Most long English words, it turns out, are only short ones wearing several <span class="cn-word" data-tr="qoʻshimchalar">attachments</span>.</p>

<p>My grandfather died before I passed that exam. I like to think he would have found English <span class="cn-word" data-pos="adj" data-tr="tushunarli">understandable</span>, perhaps even <span class="cn-word" data-pos="adj" data-tr="yoqimli">likeable</span> — a language built, like his shoes, from <span class="cn-word" data-tr="boʻlaklar">pieces</span> that fit together if you know where the <span class="cn-word" data-tr="choklar">seams</span> go.</p>''',
        "questions": [
            {
                "text": "What did the grandfather's game teach the writer?",
                "choices": [
                    "How to make shoes from leather",
                    "How words are built from a root and added pieces",
                    "How to translate Uzbek words into English",
                ],
                "answer": 1,
                "explanation": "Bobo ildizdan qoʻshimchalar bilan soʻz yasashni "
                               "oʻyin qilib oʻrgatgan — «soʻz tosh emas, teri boʻlagi».",
            },
            {
                "text": "Which English word works like Uzbek 'uysiz'?",
                "choices": ["homeless", "homely", "unhome"],
                "answer": 0,
                "explanation": "<b>-siz</b> ↔ <b>-less</b> («…siz»): <i>uysiz</i> — "
                               "<i>homeless</i>, <i>ishsiz</i> — <i>jobless</i>. "
                               "<i>homely</i> boshqa maʼno, <i>unhome</i> — mavjud emas.",
            },
            {
                "text": "Which word is built correctly?",
                "choices": ["inpossible", "impossible", "unpossible"],
                "answer": 1,
                "explanation": "<b>p, b, m</b> dan oldin <b>in-</b> → <b>im-</b>: "
                               "<i>impossible, immature, imbalance</i>. Talaffuz qulayligi uchun.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-90 — collocations   (a Bukhara guide's notebook)          [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Words That Live Together",
        "summary": (
            "PE-90 matni. Buxorolik gid Dilnoza bir yil davomida sayyohlardan "
            "eshitgan «birga yashaydigan soʻzlarni» daftarga yozdi. Daftarning "
            "oxirgi sahifasida esa oʻzining birinchi qoʻllanmasidagi xatolar turibdi."
        ),
        "order":   90,
        "grammar": [
            {
                "pattern":  "make or do? · take / have / pay / give",
                "meaning":  "Feʼl ot bilan <b>juft</b> boʻlib yashaydi, mantiq bilan "
                            "emas: <b>make</b> a mistake, a decision, a noise; "
                            "<b>do</b> homework, business, your best; <b>take</b> a "
                            "photo, a break; <b>pay</b> attention; <b>give</b> advice. "
                            "Oʻzbekchadan tarjima qilsak («xato qilmoq») — <i>do a "
                            "mistake</i> ✗ chiqadi.",
                "examples": ["You made a mistake.", "Can I take a photo?", "Please pay attention."],
            },
            {
                "pattern":  "adjective + noun partnerships: heavy rain, strong tea, a big mistake",
                "meaning":  "Sifat ham oʻz otini tanlaydi: <b>heavy</b> rain "
                            "(<i>strong rain</i> ✗ — «kuchli yomgʻir» tarjimasi), "
                            "<b>strong</b> tea (<i>powerful tea</i> ✗), <b>fast</b> food, "
                            "<b>high</b> price (<i>expensive price</i> ✗). Yakka soʻz "
                            "emas — juftlik yodlanadi.",
                "examples": ["It was heavy rain, not strong rain.", "a cup of strong tea",
                             "a high price"],
            },
        ],
        "body": '''<p>Dilnoza has been a tour guide in Bukhara for nine years. Her English was <span class="cn-word" data-pos="adj" data-tr="ravon">fluent</span> from the start: she knew the words, the grammar and the dates of every <span class="cn-word" data-tr="madrasa">madrasa</span> on Lyabi-Hauz. Yet in her second year, a <span class="cn-word" data-pos="adj" data-tr="nafaqadagi">retired</span> teacher from Manchester told her, kindly, that she spoke "very correct English that nobody actually speaks".</p>

<p>She asked him what he meant. He gave her three examples from that morning. She had told the group to "<i>do a photo</i>" by the pool, warned them about "<i>strong rain</i>" in the afternoon, and recommended a café with "<i>powerful tea</i>". Every word was correct; none of the <span class="cn-word" data-tr="juftliklar">pairs</span> was. English speakers <strong>take a photo</strong>, expect <strong>heavy rain</strong>, and drink <strong>strong tea</strong>.</p>

<p>That evening Dilnoza bought a notebook and wrote a title on the first page: <i>Words That Live Together</i>. For a year she listened to her tourists the way she listened to music, <span class="cn-word" data-pos="verb" data-tr="yozib olmoq">noting</span> down every pair that sounded natural. She sorted them into families. The <strong>make</strong> family: <strong>make a mistake</strong>, <strong>make a decision</strong>, <strong>make a reservation</strong>. The <strong>do</strong> family: <strong>do business</strong>, <strong>do your best</strong>, <strong>do the shopping</strong>. Then the <span class="cn-word" data-pos="adj" data-tr="kichik, ozgina">smaller</span> families: <strong>pay attention</strong>, <strong>give advice</strong>, <strong>have a rest</strong>, <strong>a high price</strong>, <strong>a deep sleep</strong>, <strong>a slight problem</strong>.</p>

<p>She did not try to <span class="cn-word" data-pos="verb" data-tr="yod olmoq">memorise</span> lists. Instead, she used each new pair the next day, on purpose, in front of a group. Some pairs <span class="cn-word" data-pos="verb" data-tr="qolib ketmoq, oʻrnashmoq">stuck</span> at once; others took weeks. By the end of the year, the notebook had over six hundred <span class="cn-word" data-tr="yozuvlar">entries</span>, and the teacher from Manchester, who came back a year later, <span class="cn-word" data-pos="verb" data-tr="tan olmoq">admitted</span> that her English now sounded "<span class="cn-word" data-pos="adv" data-tr="xavotirli darajada">worryingly</span> like a native's".</p>

<p>The last page of the notebook, however, is the one she shows new guides. On it she copied five sentences from the first <span class="cn-word" data-tr="qoʻllanma (kitob)">guidebook</span> she ever wrote, printed in three hundred copies. The first sentence reads: <i>Here the emir <strong>did a big mistake</strong>.</i></p>

<p>"Grammar gets you <span class="cn-word" data-pos="adj" data-tr="tushunilgan">understood</span>," she tells them. "<span class="cn-word" data-tr="kollokatsiyalar">Collocations</span> get you <span class="cn-word" data-pos="verb" data-tr="ishonmoq">believed</span>." Then she gives them a notebook of their own, with the first page left <span class="cn-word" data-pos="adj" data-tr="boʻsh">blank</span>.</p>''',
        "questions": [
            {
                "text": "What did the teacher from Manchester mean by 'very correct English that nobody actually speaks'?",
                "choices": [
                    "Her grammar was full of mistakes",
                    "Her words were correct, but they were not the pairs that English speakers use together",
                    "She spoke too fast for tourists",
                ],
                "answer": 1,
                "explanation": "Har bir soʻz toʻgʻri edi, lekin juftliklar emas: "
                               "<i>do a photo</i> emas — <b>take a photo</b>, "
                               "<i>strong rain</i> emas — <b>heavy rain</b>.",
            },
            {
                "text": "Which sentence uses the natural collocation?",
                "choices": ["I did a big mistake.", "I made a big mistake.", "I took a big mistake."],
                "answer": 1,
                "explanation": "<b>make a mistake</b> — qatʼiy juftlik. Oʻzbekcha «xato "
                               "qilmoq» dan tarjima qilsak, <i>do a mistake</i> ✗ chiqadi.",
            },
            {
                "text": "Which pair is correct?",
                "choices": ["strong rain", "heavy rain", "powerful rain"],
                "answer": 1,
                "explanation": "Yomgʻir <b>heavy</b> boʻladi. «Kuchli yomgʻir» ni "
                               "soʻzma-soʻz tarjima qilish — <i>strong rain</i> ✗ — eng koʻp "
                               "uchraydigan xatolarimizdan biri.",
            },
        ],
    },
]
