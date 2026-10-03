# -*- coding: utf-8 -*-
"""Prime English Readings — PE-91 … PE-95 (batch 19). English that has a job to do.

PE-91 formal vs informal · PE-92 the 20 Uzbek-speaker mistakes · PE-93 the polite email ·
PE-94 narrative tenses · PE-95 opinion and polite disagreement.
Written register (the toc's rule from PE-83) — but the emails, the quoted speech and the
meeting keep their own voices, which is the point of 91, 93 and 95.

Shapes (varied on purpose):
  91 — TWO EMAILS: the right message sent to the wrong person at 1 a.m.
  92 — an ARTICLE by a teacher who kept a tally of every mistake in 312 essays
  93 — a STORY WITH EMAILS: eleven internship emails with no answer, and the twelfth
  94 — a MEMOIR: the winter night the whole street lost its power
  95 — a MEETING REPORT: the mahalla, the football pitch and the boy who disagreed politely

NARRATOR VOICE (see the toc's AUDIO section):
    91 en-US-GuyNeural   · 92 en-US-JennyNeural · 93 en-US-GuyNeural
    94 en-US-JennyNeural · 95 en-US-GuyNeural
(Batch 18 ran 2 male / 3 female, so this one flips to 3 male / 2 female.)
Generate one story at a time:
    python manage.py gen_corner_audio --collection="Prime English Readings" \
        --only 91 --voice en-US-GuyNeural

People and events are the stories' own (no real-world claims needing a source).
92's numbers are the narrator's own tally, presented as one teacher's count, not a study.

Cumulative rule: the whole course through each lesson is free. Nothing in 96–100 is a
grammar point that could leak (they are describing, charts, apologies, small talk, toolkit).
Length: 300–370 words. Vocabulary: 16–22 cn-word marks.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_91_95.py --author=prime
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
    # PE-91 — formal vs informal   (the wrong email)                  [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Two Emails, One Message",
        "summary": (
            "PE-91 matni. Jasur tunda ikkita xat yozdi: biri doʻstiga, biri "
            "universitetga. Bitta xabar, ikki xil ohang — va u ularni "
            "adashtirib yubordi."
        ),
        "order":   91,
        "grammar": [
            {
                "pattern":  "the four dials: words · contractions · sentence length · directness",
                "meaning":  "Rasmiy uslubda: lotin asosli soʻzlar (<b>receive</b>, "
                            "<b>request</b>, <b>regarding</b>), qisqartmasiz "
                            "(<b>I am</b>, <i>I'm</i> emas), toʻliq gaplar, "
                            "bilvosita soʻrov. Norasmiyda: phrasal verbs "
                            "(<b>get</b>, <b>sort out</b>), qisqartmalar, "
                            "<b>gonna</b>, emoji.",
                "examples": ["I am writing regarding my application. (formal)",
                             "Gonna be late with the docs, sorry! (informal)"],
            },
            {
                "pattern":  "formal alternatives: get → receive · ask for → request · tell → inform · sorry → I apologise",
                "meaning":  "Har bir kundalik soʻzning rasmiy jufti bor. Rasmiy "
                            "xatda kundalik soʻz xato emas, lekin <b>ohangni</b> "
                            "buzadi — xuddi kostyum ustidan shippak kiygandek.",
                "examples": ["I would like to request an extension.",
                             "Please accept my apologies for the delay."],
            },
        ],
        "body": '''<p>At one o'clock in the morning, Jasur had two emails open on his laptop and one problem. His <span class="cn-word" data-tr="hujjatlar toʻplami">application</span> to a university in Malaysia was <span class="cn-word" data-pos="adj" data-tr="topshirilishi kerak">due</span> on Friday, and the bank had not yet sent the <span class="cn-word" data-tr="maʼlumotnoma">statement</span> he needed. He would be three days late.</p>

<p>The first email was to his friend Timur, who had applied to the same university:</p>

<p><i>hey! gonna be late with the docs, bank still hasn't sent the thing 🙄 can u ask ur guy in admissions if it's ok?? thx</i></p>

<p>The second was to the <span class="cn-word" data-tr="qabul boʻlimi">admissions office</span>:</p>

<p><i>Dear Admissions Team, <strong>I am writing regarding</strong> my application for the Bachelor of Computer Science. Unfortunately, my bank has not yet <strong>provided</strong> the financial statement that is required. <strong>I would like to request</strong> a short <span class="cn-word" data-tr="muddatni uzaytirish">extension</span> of three working days. <strong>Please accept my apologies</strong> for any <span class="cn-word" data-tr="noqulaylik">inconvenience</span>. Yours faithfully, Jasur Karimov</i></p>

<p>It was the same message twice. One <span class="cn-word" data-pos="verb" data-tr="tirjaymoq">grinned</span>; the other wore a suit. The second had no <span class="cn-word" data-tr="qisqartmalar">contractions</span>, no <span class="cn-word" data-tr="jargon, koʻcha tili">slang</span> and no emoji. It said <strong>provided</strong> instead of <i>sent</i>, <strong>request</strong> instead of <i>ask</i>, and <strong>regarding</strong> instead of <i>about</i>.</p>

<p>He pressed "Send" on both and went to sleep.</p>

<p>In the morning he opened his "Sent" <span class="cn-word" data-tr="papka">folder</span> and felt the floor move. The <span class="cn-word" data-pos="adj" data-tr="tartibli, toʻgʻri">proper</span> email had gone to Timur. The admissions office had received <i>gonna be late with the docs</i> — with the eye-rolling emoji.</p>

<p>He wrote again <span class="cn-word" data-pos="adv" data-tr="darhol">immediately</span>, sent the formal email to the right address, and added one more sentence: <i>Please <span class="cn-word" data-pos="verb" data-tr="eʼtiborsiz qoldirmoq">disregard</span> my previous message, which was sent in error.</i></p>

<p>The reply came that afternoon. The extension was <span class="cn-word" data-pos="verb" data-tr="berilmoq (ruxsat)">granted</span>. Under the <span class="cn-word" data-tr="imzo">signature</span>, the admissions officer, a woman called Hannah, had added a short note of her own:</p>

<p><i>P.S. Your second email was excellent. Your first was more honest. We see both kinds every day — <span class="cn-word" data-pos="adv" data-tr="yaxshiyamki">luckily</span>, only one kind gets an extension.</i></p>

<p>Jasur printed it and kept it above his desk. He says it taught him the rule better than any textbook: the message can stay the same, but its clothes must match the room it walks into.</p>''',
        "questions": [
            {
                "text": "What went wrong with Jasur's emails?",
                "choices": [
                    "He forgot to attach his bank statement",
                    "He sent the informal email to the admissions office and the formal one to his friend",
                    "He wrote both emails in an informal style",
                ],
                "answer": 1,
                "explanation": "U xatlarni adashtirib yubordi: rasmiy xat — doʻstiga, "
                               "<i>gonna be late</i> esa — qabul boʻlimiga.",
            },
            {
                "text": "Which sentence is the most formal?",
                "choices": [
                    "I'd like to ask for a few more days.",
                    "I would like to request a short extension.",
                    "Can I get a few more days?",
                ],
                "answer": 1,
                "explanation": "<b>I would</b> (qisqartmasiz), <b>request</b> "
                               "(<i>ask for</i> oʻrniga), <b>extension</b> — uchala "
                               "«dastak» ham rasmiy tomonga burilgan.",
            },
            {
                "text": "In formal writing, which word is the best replacement for 'sent' in 'the bank has not sent the statement'?",
                "choices": ["provided", "gave out", "got"],
                "answer": 0,
                "explanation": "<b>provided</b> — rasmiy feʼl. <i>gave out</i> — phrasal verb, "
                               "<i>got</i> — kundalik va maʼnosi ham boshqa.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-92 — the 20 Uzbek-speaker mistakes   (a teacher's tally)   [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Mistakes We Keep Making",
        "summary": (
            "PE-92 matni. Ingliz tili oʻqituvchisi bir yil davomida 312 ta "
            "inshodagi har bir xatoni sanadi. Roʻyxatning tepasida nima "
            "turibdi — va eski qutidan chiqqan oʻzining 2009-yilgi inshosi "
            "nimani koʻrsatdi."
        ),
        "order":   92,
        "grammar": [
            {
                "pattern":  "mistakes that come from Uzbek: no articles · no 3rd-person -s · no 'to be' · SOV order",
                "meaning":  "Oʻzbek tilida artikl yoʻq (<i>I am student</i> ✗ → "
                            "<b>a student</b>), 3-shaxs uchun alohida qoʻshimcha "
                            "yoʻq (<i>she go</i> ✗ → <b>goes</b>), «boʻlmoq» "
                            "tushib qoladi (<i>he very clever</i> ✗ → <b>is</b>), "
                            "feʼl oxirida keladi (<i>I English study</i> ✗).",
                "examples": ["I am a student.", "She goes to school.", "My brother is very clever."],
            },
            {
                "pattern":  "present perfect with for / since — not the present",
                "meaning":  "Oʻzbekcha «oʻn yildan beri shu yerda <i>yashayman</i>» "
                            "— hozirgi zamon. Ingliz tilida esa <b>have lived</b>: "
                            "<i>I live here for ten years</i> ✗ → <b>I have lived "
                            "here for ten years</b>.",
                "examples": ["I have lived here for ten years.", "She has worked there since 2019."],
            },
        ],
        "body": '''<p>Last year I did something that every English teacher <span class="cn-word" data-pos="verb" data-tr="vaʼda bermoq">promises</span> to do and nobody does: I kept a <span class="cn-word" data-tr="hisob, sanoq">tally</span>. Every mistake in every essay got a mark. By June I had read 312 essays and counted just over four thousand mistakes.</p>

<p>This is one teacher's count, not a scientific study. But the list was short. Most of those four thousand mistakes were the same twenty, made again and again — and nearly every one was Uzbek <span class="cn-word" data-pos="adv" data-tr="jimgina">quietly</span> translating itself into English.</p>

<p>At the top, far ahead of everything else, were articles: <i>I am student. The life is hard.</i> Uzbek has no articles at all, so the brain does not look for them. Second came the missing <strong>-s</strong>: <i>She go to school.</i> Uzbek does not mark the third person that way, and under <span class="cn-word" data-tr="bosim">pressure</span> the ending <span class="cn-word" data-pos="verb" data-tr="yoʻqolmoq">disappears</span>. Third was the present perfect: <i>I live here for ten years</i>, a perfect copy of the Uzbek sentence and a perfect English mistake. Close behind came the missing <strong>is</strong> (<i>My brother very clever</i>) and <span class="cn-word" data-pos="adj" data-tr="sanalmaydigan">uncountable</span> nouns with an <strong>-s</strong> (<i>informations</i>).</p>

<p>What surprised me was how <span class="cn-word" data-pos="adj" data-tr="oldindan aytsa boʻladigan">predictable</span> it all was. The mistakes are not <span class="cn-word" data-pos="adj" data-tr="tasodifiy">random</span>; they follow the <span class="cn-word" data-tr="tuzilish">structure</span> of our own language. And anything predictable can be fixed <span class="cn-word" data-tr="ataylab">on purpose</span>.</p>

<p>So this year my students run a <span class="cn-word" data-tr="oʻz-oʻzini tekshirish">self-check</span> after every essay. First the articles: every <span class="cn-word" data-pos="adj" data-tr="sanaladigan">countable</span> singular noun needs <i>a</i>, <i>the</i> or <i>my</i>. Then every <i>he</i>, <i>she</i> and <i>it</i>: does the verb have its <strong>-s</strong>? Then every <i>for</i> and <i>since</i>. It takes ten minutes, and the marks went up in the first month.</p>

<p>One last <span class="cn-word" data-tr="eʼtirof">confession</span>. In December I found my own university essay from 2009 in a box of old papers. In the first paragraph alone there were two missing articles and one <i>I study English since 2003</i>.</p>

<p>I have <span class="cn-word" data-pos="verb" data-tr="ramkaga solmoq">framed</span> that page, and it hangs above the <span class="cn-word" data-tr="doska">whiteboard</span> in my classroom. It <span class="cn-word" data-pos="verb" data-tr="isbotlamoq">proves</span> what I most want my students to know. These mistakes are not a sign that you are bad at English. They are a sign that you speak Uzbek — and they can be <span class="cn-word" data-pos="verb" data-tr="oʻrganib tashlamoq">unlearned</span>.</p>''',
        "questions": [
            {
                "text": "According to the teacher, why are these mistakes so predictable?",
                "choices": [
                    "Because students do not study enough",
                    "Because they come from the structure of the Uzbek language",
                    "Because English grammar has no rules",
                ],
                "answer": 1,
                "explanation": "Xatolar tasodifiy emas — ular oʻzbek tilining "
                               "tuzilishidan kelib chiqadi: artikl yoʻq, 3-shaxs "
                               "qoʻshimchasi yoʻq, «-dan beri» hozirgi zamonda.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "I live here for ten years.",
                    "I am living here for ten years.",
                    "I have lived here for ten years.",
                ],
                "answer": 2,
                "explanation": "<b>for / since</b> bilan hozirgacha davom etayotgan "
                               "holat — <b>present perfect</b>: <i>I have lived</i>. "
                               "Oʻzbekchadan soʻzma-soʻz tarjima — <i>I live</i> ✗.",
            },
            {
                "text": "Which sentence has NO mistake?",
                "choices": ["My brother very clever.", "She go to school every day.", "I am a student."],
                "answer": 2,
                "explanation": "<b>I am a student</b> — artikl bor. Birinchisida "
                               "<b>is</b> yoʻq, ikkinchisida <b>goes</b> boʻlishi kerak.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-93 — the polite email   (the twelfth email)                  [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Email That Got a Reply",
        "summary": (
            "PE-93 matni. Sherbek amaliyot soʻrab oʻn bitta kompaniyaga xat "
            "yozdi — hech kim javob bermadi. Opasi xatni qayta yozdi: "
            "mavzu, salom, birinchi qator, xushmuomala soʻrov. Oʻn ikkinchi "
            "xatga ertasi kuni javob keldi."
        ),
        "order":   93,
        "grammar": [
            {
                "pattern":  "the polite request: I was wondering if you could… · I would be grateful if…",
                "meaning":  "Ingliz tilida soʻrov qanchalik <b>bilvosita</b> boʻlsa, "
                            "shunchalik xushmuomala: <i>Give me an internship</i> → "
                            "<i>Could you…?</i> → <b>I was wondering if you could…</b> → "
                            "<b>I would be grateful if you could…</b> Oʻtgan zamon shakli "
                            "(<i>was wondering</i>) bu yerda vaqtni emas, odobni bildiradi.",
                "examples": ["I was wondering if you could tell me about internships.",
                             "I would be grateful if you could spare ten minutes."],
            },
            {
                "pattern":  "greeting and closing must match; say why you are writing in the first line",
                "meaning":  "<b>Dear Ms Lee</b> → <b>Kind regards</b> / <b>Yours "
                            "sincerely</b>; ismini bilmasangiz <b>Dear Sir or Madam</b> → "
                            "<b>Yours faithfully</b>. Birinchi qatorda maqsad: <b>I am "
                            "writing to ask about…</b> — oʻqiydigan odam vaqtini tejaydi.",
                "examples": ["Dear Ms Lee, I am writing to ask about summer internships.",
                             "Kind regards, Sherbek Aliyev"],
            },
        ],
        "body": '''<p>Sherbek, a third-year economics student, wanted a summer <span class="cn-word" data-tr="amaliyot (stajirovka)">internship</span> at a <span class="cn-word" data-tr="logistika">logistics</span> company. In March he sent the same email to eleven companies. It began like this:</p>

<p><i>Hello. I am Sherbek. I am student of economics. Give me please internship in your company, I am very hard-working.</i></p>

<p>Nobody answered. After three weeks he showed it to his older sister Madina, who works in human resources at a bank. She read it once and laughed — not <span class="cn-word" data-pos="adv" data-tr="yomon niyat bilan">unkindly</span>.</p>

<p>"Every word is true," she said. "But a manager gets eighty emails a day. Yours has no <span class="cn-word" data-tr="mavzu (xat)">subject line</span>, no name, and it gives an order. You have asked for a <span class="cn-word" data-tr="yaxshilik, iltifot">favour</span> the way you would order a <span class="cn-word" data-tr="somsa">samsa</span>."</p>

<p>That evening they rebuilt it. First, a subject line: <i>Summer internship <span class="cn-word" data-tr="soʻrov">enquiry</span> — economics student</i>. Then a real name, found on the company's website, so the greeting became <strong>Dear Ms Lee</strong>. Then a first sentence that said why he was writing: <strong>I am writing to ask about</strong> summer internships in your logistics department.</p>

<p>The request took longest. In English, Madina explained, a polite request goes <span class="cn-word" data-pos="adv" data-tr="bilvosita">indirectly</span>, and the past tense here is about <span class="cn-word" data-tr="odob, xushmuomalalik">courtesy</span>, not time. So <i>Give me please internship</i> became <strong>I was wondering if you could</strong> tell me whether any places are still available. She added one more sentence: <strong>I would be grateful if you could</strong> look at the <span class="cn-word" data-pos="adj" data-tr="ilova qilingan">attached</span> CV.</p>

<p>The ending had to <span class="cn-word" data-pos="verb" data-tr="mos kelmoq">match</span> the beginning. A named person gets <strong>Kind regards</strong> or <strong>Yours sincerely</strong> — never <i>Bye</i>, and never nothing at all.</p>

<p>The new email was five sentences long, shorter than the old one. He sent it at nine the next morning, and Ms Lee replied at four. She thanked him for his clear message, <span class="cn-word" data-pos="verb" data-tr="taklif qilmoq">invited</span> him to an interview, and <span class="cn-word" data-pos="verb" data-tr="yuborib bermoq">forwarded</span> his CV to two <span class="cn-word" data-tr="hamkasblar">colleagues</span>.</p>

<p>He got the internship. In his first week, he helped to <span class="cn-word" data-pos="verb" data-tr="saralamoq">sort</span> the applications for the autumn <span class="cn-word" data-tr="dastur">programme</span>. On the second day he found an email that began: <i>Hello. I am student. Give me please job.</i></p>

<p>He did not <span class="cn-word" data-pos="verb" data-tr="oʻchirib tashlamoq">delete</span> it. He wrote back, kindly, and attached his sister's rules.</p>''',
        "questions": [
            {
                "text": "Why did nobody answer Sherbek's first eleven emails, according to Madina?",
                "choices": [
                    "Because the companies had no internships",
                    "Because the email had no subject line or name and sounded like an order",
                    "Because his English was too formal",
                ],
                "answer": 1,
                "explanation": "Mavzu yoʻq, ism yoʻq, va soʻrov buyruq kabi — "
                               "<i>Give me please internship</i>.",
            },
            {
                "text": "Which request is the most polite?",
                "choices": [
                    "Give me an internship, please.",
                    "Can you give me an internship?",
                    "I was wondering if you could tell me about internships.",
                ],
                "answer": 2,
                "explanation": "Qanchalik bilvosita — shunchalik xushmuomala. "
                               "<b>I was wondering if…</b> — oʻtgan zamon odob uchun.",
            },
            {
                "text": "An email begins 'Dear Ms Lee'. Which closing matches it?",
                "choices": ["Yours faithfully", "Kind regards", "Bye"],
                "answer": 1,
                "explanation": "Ism bilan murojaat → <b>Kind regards</b> yoki "
                               "<b>Yours sincerely</b>. <i>Yours faithfully</i> — faqat "
                               "<i>Dear Sir or Madam</i> bilan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-94 — narrative tenses   (a memoir: the blackout)            [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Night the Power Went Out",
        "summary": (
            "PE-94 matni. Esdalik: qishki kechada butun koʻchada chiroq oʻchdi. "
            "Telefonlar ham oʻchdi, va buvi qirq yil aytmagan hikoyasini aytdi. "
            "Chiroq qaytganda esa hech kim oʻrnidan turmadi."
        ),
        "order":   94,
        "grammar": [
            {
                "pattern":  "the four narrative tenses, each with its job",
                "meaning":  "<b>Past simple</b> — voqealar zanjiri (<i>the lights "
                            "went out</i>). <b>Past continuous</b> — fon, davom "
                            "etayotgan holat (<i>we were watching TV</i>). <b>Past "
                            "perfect</b> — undan ham oldin (<i>she had never told "
                            "us</i>). <b>Past perfect continuous</b> — oldin uzoq "
                            "davom etgan (<i>it had been snowing all day</i>).",
                "examples": ["It had been snowing all day.", "We were watching television when the lights went out.",
                             "She had never told anyone the story."],
            },
            {
                "pattern":  "time words that move a story forward: when · while · as soon as · by the time · suddenly",
                "meaning":  "Hikoyani oldinga surish uchun: <b>when</b> (qisqa "
                            "voqea), <b>while</b> (fon), <b>as soon as</b> (darhol "
                            "keyin), <b>by the time</b> (+ past perfect).",
                "examples": ["As soon as the screen went black, Grandmother laughed.",
                             "By the time the lights came back, she had finished."],
            },
        ],
        "body": '''<p>It <strong>had been snowing</strong> all day, the heavy, silent snow that Tashkent sees only a few times each winter.</p>

<p>We <strong>were watching</strong> a football match on television — my father, my two brothers and I — while my grandmother <strong>was sitting</strong> by the window with her <span class="cn-word" data-tr="toʻqish (ish)">knitting</span>. Ten minutes before half-time, the screen <strong>went</strong> black and every light in the house <strong>went out</strong> with it.</p>

<p>My brothers <span class="cn-word" data-pos="verb" data-tr="ingramoq, zorlanmoq">groaned</span> and reached for their phones, and my father went to look for candles. Outside, every window in the street was dark. The snow had brought down a <span class="cn-word" data-tr="elektr simi">power line</span>, and the whole <span class="cn-word" data-tr="mahalla, tuman">neighbourhood</span> was waiting in the cold together.</p>

<p>Within an hour the phone <span class="cn-word" data-tr="batareyalar">batteries</span> <strong>had died</strong> one by one, and there was nothing to do but sit in the kitchen around three candles and the gas <span class="cn-word" data-tr="pechka, plita">stove</span>. That was when my grandmother started to talk.</p>

<p>She told us about another winter, in 1969, when she <strong>was</strong> nineteen. She <strong>had</strong> just <strong>started</strong> work at a textile factory, and one night the lights <strong>failed</strong> while she <strong>was walking</strong> home along the <span class="cn-word" data-tr="kanal, ariq">canal</span>. In the dark she <span class="cn-word" data-pos="verb" data-tr="sirpanmoq">slipped</span> on the ice, and a young man who <strong>had been following</strong> her at a <span class="cn-word" data-pos="adj" data-tr="hurmatli, odobli">respectful</span> distance for three weeks — too shy to speak — <span class="cn-word" data-pos="verb" data-tr="tutib qolmoq">caught</span> her arm before she fell.</p>

<p>"That was your grandfather," she said. "If the lights <strong>had</strong> not <strong>gone out</strong>, he would still be following me."</p>

<p>In forty years she <strong>had</strong> never <strong>told</strong> the story to anyone, not even to my father, who sat listening with his mouth open like a boy. She told it slowly, with all the <span class="cn-word" data-tr="tafsilotlar">details</span>: the colour of his coat, the first words he said, the bread he <span class="cn-word" data-pos="verb" data-tr="ulashmoq">shared</span> with her the next day.</p>

<p>Just after eleven, the lights came back. The fridge <span class="cn-word" data-pos="verb" data-tr="gʻuvillamoq">hummed</span>, the television <span class="cn-word" data-pos="verb" data-tr="lip etib yonmoq">flickered</span> on in the next room, and the <span class="cn-word" data-tr="sharhlovchilar">commentators</span> started shouting about a match that <strong>had</strong> long since <strong>ended</strong>.</p>

<p>Nobody got up. My grandmother, smiling, began the story of the second time my grandfather spoke to her.</p>

<p>Whenever the <span class="cn-word" data-tr="elektr toki">electricity</span> goes off now, most people <span class="cn-word" data-pos="verb" data-tr="shikoyat qilmoq">complain</span>. I light a candle and wait to see who will start talking.</p>''',
        "questions": [
            {
                "text": "Why does the narrator say 'Nobody got up' when the lights came back?",
                "choices": [
                    "Because the family was asleep",
                    "Because they wanted to keep listening to the grandmother's stories",
                    "Because the television was broken",
                ],
                "answer": 1,
                "explanation": "Chiroq qaytdi, lekin hech kim televizorga qaytmadi — "
                               "buvining hikoyalari muhimroq boʻlib qoldi.",
            },
            {
                "text": "'It had been snowing all day.' Why is the past perfect continuous used here?",
                "choices": [
                    "To show a long action that continued up to the moment the story begins",
                    "To show an action that will happen later",
                    "To show a short action that interrupted another one",
                ],
                "answer": 0,
                "explanation": "<b>had been + -ing</b> — hikoya boshlanishidan "
                               "<b>oldin</b> uzoq davom etgan harakat: qor kun boʻyi yoqqan.",
            },
            {
                "text": "Which sentence uses the narrative tenses correctly?",
                "choices": [
                    "We watched television when the lights were going out.",
                    "We were watching television when the lights went out.",
                    "We had watched television when the lights were going out.",
                ],
                "answer": 1,
                "explanation": "Fon — <b>past continuous</b> (<i>were watching</i>), "
                               "uni toʻxtatgan qisqa voqea — <b>past simple</b> (<i>went out</i>).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-95 — opinion & polite disagreement   (the mahalla meeting)   [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "I See Your Point, But",
        "summary": (
            "PE-95 matni. Mahalla yigʻilishi: futbol maydonini avtoturargohga "
            "aylantirish taklifi. Kattalar bahslashdi, oʻn ikki yoshli Bekzod "
            "esa oʻz fikrini aytishdan oldin qarshisidagilarning fikrini takrorladi."
        ),
        "order":   95,
        "grammar": [
            {
                "pattern":  "giving an opinion: In my view · I'd say · As far as I'm concerned · I strongly believe",
                "meaning":  "Fikr bildirishning kuchli va yumshoq iboralari. "
                            "<b>I think</b> — oddiy; <b>In my view</b> — biroz rasmiy; "
                            "<b>I strongly believe</b> — kuchli. Bitta iborani har "
                            "gapda takrorlamang.",
                "examples": ["In my view, the pitch should stay.", "I strongly believe we need both."],
            },
            {
                "pattern":  "the polite disagreement formula: acknowledge + but + your point + reason",
                "meaning":  "Avval qarshi fikrni <b>tan oling</b>, keyin oʻzingiznikini "
                            "ayting: <b>I see your point, but…</b> · <b>That's true to "
                            "some extent, however…</b> · <b>I'm not sure I agree, "
                            "because…</b> <i>You are wrong</i> — bahsni toʻxtatadi.",
                "examples": ["I see your point, but the children have nowhere else to play.",
                             "That's true to some extent; however, there is another option."],
            },
        ],
        "body": '''<p>The meeting in our mahalla had one subject. The football pitch behind School No. 41, a square of <span class="cn-word" data-tr="tuproq">dirt</span> with two <span class="cn-word" data-pos="adj" data-tr="zanglagan">rusty</span> goals, was going to become a <span class="cn-word" data-tr="avtoturargoh">car park</span>.</p>

<p>The <span class="cn-word" data-tr="taklif">proposal</span> came from Mr Hamidov, who lives on the corner, and he spoke well. "<strong>In my view</strong>, we have no choice," he said. "There are twice as many cars in this street as ten years ago. People park on the <span class="cn-word" data-tr="yoʻlak, trotuar">pavement</span>, and last winter a fire engine was <span class="cn-word" data-pos="adj" data-tr="kechikkan">delayed</span> for six minutes."</p>

<p>Several people <span class="cn-word" data-pos="verb" data-tr="bosh irgʻamoq">nodded</span>. Another man stood up, red in the face, and called him wrong, and for a while the meeting was two men shouting.</p>

<p>Then a boy put up his hand. Bekzod is twelve. He plays on that pitch every evening, and most of the adults in the room had, at some time, <span class="cn-word" data-pos="verb" data-tr="baqirmoq">yelled</span> at him for kicking a ball against their gate.</p>

<p>He did not shout. He began by <span class="cn-word" data-pos="verb" data-tr="takrorlamoq">repeating</span> Mr Hamidov's <span class="cn-word" data-tr="dalil, fikr">argument</span>, carefully, as if it were his own. "Mr Hamidov says the street is full of cars. <strong>I see your point</strong>, and <strong>that's true</strong> — my grandmother needed an <span class="cn-word" data-tr="tez yordam mashinasi">ambulance</span> last year, and it was late."</p>

<p>The room went quiet.</p>

<p>"<strong>But</strong> if the pitch becomes a car park, forty children will play in the street instead, between the parked cars. <strong>As far as I'm concerned</strong>, that's more dangerous, not less." He took a <span class="cn-word" data-pos="adj" data-tr="buklangan">folded</span> paper out of his pocket. "There's also the empty land behind the old bakery. Nobody uses it. <strong>I'd say</strong> it could take thirty cars. I <span class="cn-word" data-pos="verb" data-tr="oʻlchamoq">measured</span> it with my brother's <span class="cn-word" data-tr="ruletka (oʻlchov tasmasi)">tape</span>."</p>

<p>Then Mr Hamidov did something <span class="cn-word" data-pos="adj" data-tr="kamdan-kam">rare</span> at mahalla meetings. He said, "I hadn't thought of that."</p>

<p>It took eight months and three more meetings. The land behind the bakery is now a car park for thirty-two cars, and the pitch is still a pitch, with new goals.</p>

<p>Bekzod told me later that the most useful thing he said that night was not about cars at all. It was the first <span class="cn-word" data-tr="ibora">phrase</span>. "If you start with <strong>I see your point</strong>," he explained, "people stop <span class="cn-word" data-pos="verb" data-tr="himoyalanmoq">defending</span> themselves and start listening. Then you can say <strong>but</strong>."</p>''',
        "questions": [
            {
                "text": "What did Bekzod do before giving his own opinion?",
                "choices": [
                    "He told Mr Hamidov that he was wrong",
                    "He repeated Mr Hamidov's argument and agreed with part of it",
                    "He asked the adults to vote",
                ],
                "answer": 1,
                "explanation": "U avval qarshi tomonning dalilini takrorladi va "
                               "qisman tan oldi — <b>I see your point, and that's true</b> — "
                               "keyin <b>But</b> bilan oʻz fikrini aytdi.",
            },
            {
                "text": "Which is the most polite way to disagree?",
                "choices": [
                    "You are wrong about the car park.",
                    "I see your point, but the children need somewhere to play.",
                    "That's a stupid idea.",
                ],
                "answer": 1,
                "explanation": "Formula: <b>tan olish + but + oʻz fikri + sabab</b>. "
                               "Qolgan ikkitasi bahsni toʻxtatadi.",
            },
            {
                "text": "What was Bekzod's alternative to using the football pitch?",
                "choices": [
                    "Parking on the pavement",
                    "Building a car park on the empty land behind the old bakery",
                    "Asking people to sell their cars",
                ],
                "answer": 1,
                "explanation": "Eski novvoyxona orqasidagi boʻsh yer — hech kim "
                               "foydalanmaydi, u yerga 30 ta mashina sigʻadi.",
            },
        ],
    },
]
