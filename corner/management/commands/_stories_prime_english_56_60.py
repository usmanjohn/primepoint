# -*- coding: utf-8 -*-
"""Prime English Readings — PE-56 … PE-60 (batch 12). Mixed conditionals → the passive.

PE-56 mixed conditionals · PE-57 wish / if only · PE-58 relative clauses (who/which/
that) · PE-59 defining vs non-defining · PE-60 passive present & past.

Shapes:
  56 — a life story told by the man himself: the son who left medical institute in his
       third year, and the two mixed conditionals he lives between
  57 — a notebook of one wish a week, kept from the age of twelve, read out loud at a
       wedding by the brother it complains about
  58 — the man who fixed everything on the street, and the one gate he never fixed
  59 — a comedy of one missing comma: two cousins, one message, and a room prepared
       for the wrong man
  60 — a village bridge and the name that is not on its plaque

NARRATOR VOICE (see the toc's AUDIO section): the readings alternate male and female
narrators from batch 12 on, at the user's request. This batch:
    56 en-US-GuyNeural · 57 en-US-JennyNeural · 58 en-US-GuyNeural
    59 en-US-JennyNeural · 60 en-US-GuyNeural
Generate one story at a time so each gets its own voice:
    python manage.py gen_corner_audio --collection="Prime English Readings" \
        --only 56 --voice en-US-GuyNeural

Cumulative rule: PE-56…PE-59 use NO passive at all — it arrives in PE-60. `wish` starts
in PE-57, `which` and non-defining commas in PE-59 (PE-58 keeps to defining who/that).
PE-60 uses the present and past passive only, never `has been + V3` (PE-61). No reported
speech with backshift (PE-62 — direct quotes only), no `as … as` / `too` / `enough`
(PE-67/68).
Length: 280–330 words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_56_60.py --author=prime
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
    # PE-56 — mixed conditionals  (the ambulance driver)   [voice: Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "If He Had Studied, He Would Be a Doctor Now",
        "summary": (
            "PE-56 matni. Qishlogʻimizda hamma bir gapni aytadi: "
            "“oʻqishni tashlamasa, hozir shifokor boʻlardi”. "
            "Uning oʻzi esa boshqa gapni aytadi — va oʻsha gap "
            "fevral kechasida bitta bolaning hayotini saqlab qoldi."
        ),
        "order":   56,
        "grammar": [
            {
                "pattern":  "Mix 1: past cause → present result",
                "meaning":  "<b>If + had + V3 → would + V1</b>. "
                            "Sabab oʻtgan zamonda, natija esa "
                            "<b>hozir</b>: <i><b>If</b> he <b>had "
                            "finished</b> the institute, he "
                            "<b>would be</b> a doctor now</i>. "
                            "“Hozir” soʻzi — bu aralash shartning "
                            "eng aniq belgisi.",
                "examples": ["If he had finished the institute, he would be a doctor now.",
                             "If she had taken that job, she would live in Almaty."],
            },
            {
                "pattern":  "Mix 2: present cause → past result",
                "meaning":  "<b>If + past simple → would have + V3</b>. "
                            "Sabab — hozirgi doimiy holat yoki xarakter, "
                            "natija — oʻtgan zamonda: <i><b>If</b> I "
                            "<b>were</b> the kind of man who can sit in "
                            "one room for six years, I <b>wouldn't have "
                            "left</b></i>.",
                "examples": ["If I were a patient man, I wouldn't have left in the third year.",
                             "If he were a doctor, he wouldn't have been on that road at three."],
            },
            {
                "pattern":  "How to choose",
                "meaning":  "Ikki savol: <b>sabab</b> qachon? "
                            "<b>natija</b> qachon? Oʻtgan sabab + "
                            "hozirgi natija → <i>had V3 … would V1</i>. "
                            "Hozirgi sabab + oʻtgan natija → "
                            "<i>past simple … would have V3</i>. "
                            "Sof uchinchi shartdan farqi shu — "
                            "aralash shartda ikki qism ikki xil "
                            "zamonda yashaydi.",
                "examples": ["If I had slept, I wouldn't be tired now.",
                             "If I didn't work nights, I would have come to the wedding."],
            },
        ],
        "body": '''<p>My uncle Sardor left the medical <span class="cn-word" data-tr="institut">institute</span> in the middle of his third year, in 1999, and everybody in our family has an opinion about it.</p>

<p>My grandmother says it every autumn, quietly, when the <span class="cn-word" data-tr="qabul, kirish imtihonlari">admissions</span> are in the news: "<strong>If</strong> he <strong>had finished</strong>, he <strong>would be</strong> a doctor now." She is right. He was the best in his year at <span class="cn-word" data-tr="anatomiya">anatomy</span> and he has hands that do not shake.</p>

<p>He drives an <span class="cn-word" data-tr="tez yordam">ambulance</span> instead. Twenty-one years, mostly nights, on roads that <span class="cn-word" data-pos="verb" data-tr="muzlaydi">freeze</span> from November.</p>

<p>He answers his mother with a different sentence, and I have heard it four or five times: "<strong>If</strong> I <strong>were</strong> the kind of man who can sit in one room for six years, I <strong>wouldn't have left</strong> in the third year."</p>

<p>Last February a boy of nine went through the ice on the <span class="cn-word" data-tr="suv ombori">reservoir</span> near Bogʻishamol at twenty past three in the morning. His brother ran to the road and stopped the first thing that had <span class="cn-word" data-tr="chiroqlar">lights</span>.</p>

<p>The nearest hospital is nineteen minutes from that <span class="cn-word" data-tr="qirgʻoq">shore</span>. Sardor did the first eleven of those minutes in the back of his own ambulance with the boy on the <span class="cn-word" data-tr="zambil">stretcher</span> and a young nurse driving, and the boy's heart started again somewhere near the <span class="cn-word" data-tr="yoqilgʻi shoxobchasi">petrol station</span>.</p>

<p>The boy is ten now. He came to our <span class="cn-word" data-tr="hayit">holiday</span> table in March with his father, and he ate more than anybody.</p>

<p>My grandmother said her sentence again that evening, because she always does. Sardor put down his tea.</p>

<p>"<strong>If</strong> I <strong>had stayed</strong> at the institute, I <strong>would be</strong> a doctor now," he said. "That is true, ona. And <strong>if</strong> I <strong>were</strong> a doctor, I <strong>would have been</strong> asleep in Tashkent at three in the morning in February, and somebody else <strong>would have been</strong> on that road. Maybe a good man. Maybe nineteen minutes."</p>

<p>Nobody argued with him, which in our family is <span class="cn-word" data-pos="adj" data-tr="kamdan-kam">rare</span>.</p>

<p>His own son is in his third year at that institute now. Sardor drove him to the door in September and did not go inside the building, and he has never explained why, and I have never asked him.</p>''',
        "questions": [
            {
                "text": "What is Sardor's answer to his mother's sentence?",
                "choices": [
                    "That he regrets leaving the institute every single day",
                    "That if he were a doctor, he would have been asleep in Tashkent that February night instead of on that road",
                    "That he was never good at anatomy",
                ],
                "answer": 1,
                "explanation": "U onasining gapini rad etmaydi — "
                               "“shifokor boʻlardim” degani toʻgʻri. "
                               "Lekin shifokor boʻlsa, oʻsha kechasi "
                               "Toshkentda uxlab yotgan boʻlardi.",
            },
            {
                "text": "\"If he had finished, he would be a doctor now.\" The cause and the result are:",
                "choices": [
                    "cause in the past, result in the present",
                    "both in the past",
                    "both in the present",
                ],
                "answer": 0,
                "explanation": "Sabab — 1999-yil (oʻtgan zamon, "
                               "<i>had finished</i>), natija — "
                               "<b>hozir</b> (<i>would be … now</i>). "
                               "Shuning uchun bu aralash shart.",
                        },
            {
                "text": "Which sentence has a PRESENT cause and a PAST result?",
                "choices": [
                    "If I had slept, I wouldn't be tired now.",
                    "If I don't sleep, I will be tired.",
                    "If I didn't work nights, I would have come to the wedding.",
                ],
                "answer": 2,
                "explanation": "“Tunda ishlaydigan odam boʻlmasam” — "
                               "hozirgi doimiy holat; “toʻyga kelardim” "
                               "— oʻtgan natija. Formula: "
                               "<i>past simple … would have + V3</i>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-57 — wish / if only  (the notebook)              [voice: Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Wishing Notebook",
        "summary": (
            "PE-57 matni. Oʻn ikki yoshida u daftar oldi va har hafta "
            "bitta “I wish…” yozdi. Oʻn yildan keyin oʻsha daftarni "
            "ukasi topdi — va toʻyda ovoz chiqarib oʻqidi."
        ),
        "order":   57,
        "grammar": [
            {
                "pattern":  "wish + past simple — a different present",
                "meaning":  "Hozirgi haqiqat boshqacha boʻlishini "
                            "istash: <i>I <b>wish</b> I <b>had</b> a "
                            "bicycle</i> — velosipedim yoʻq. "
                            "<i>I <b>wish</b> I <b>were</b> taller</i> "
                            "— bu shakl xayoliy, oʻtgan zamon emas. "
                            "<b>wish</b> dan keyin bir qadam orqaga "
                            "suriladi, xuddi ikkinchi shartda.",
                "examples": ["I wish I had a bicycle.",
                             "I wish I were braver."],
            },
            {
                "pattern":  "wish + past perfect — a different past",
                "meaning":  "Oʻtgan voqea uchun afsus: "
                            "<i>I <b>wish</b> I <b>hadn't shouted</b> "
                            "at her</i>. <b>if only</b> — xuddi shu "
                            "maʼno, kuchliroq: <i><b>If only</b> I "
                            "<b>had said</b> it out loud</i>.",
                "examples": ["I wish I hadn't lost that notebook.",
                             "If only I had told her that year."],
            },
            {
                "pattern":  "wish + would — the complaint, and wish ≠ hope",
                "meaning":  "Boshqa odamning xatti-harakatidan "
                            "shikoyat: <i>I <b>wish</b> my brother "
                            "<b>would stop</b> reading my things</i>. "
                            "Diqqat: kelasi zamon uchun <b>hope</b> "
                            "ishlatiladi — <i>I <b>hope</b> you pass</i> "
                            "(<i>I wish you pass</i> ✗). Tilak "
                            "aytishda esa <i>I wish you a happy "
                            "birthday</i> — bu butunlay boshqa "
                            "<b>wish</b>.",
                "examples": ["I wish he would knock before he comes in.",
                             "I hope you pass the exam tomorrow."],
            },
        ],
        "body": '''<p>In 2014, when I was twelve, my mother gave me a thin green <span class="cn-word" data-tr="daftar">notebook</span> because I <span class="cn-word" data-pos="verb" data-tr="shikoyat qilardim">complained</span> about everything. She said I could write one wish in it every Sunday, and that she would never read it.</p>

<p>She never did. I <span class="cn-word" data-pos="verb" data-tr="toʻldirdim">filled</span> forty pages in three years.</p>

<p><i>I <strong>wish</strong> I <strong>had</strong> a bicycle. I <strong>wish</strong> my brother <strong>would stop</strong> coming into my room. I <strong>wish</strong> I <strong>were</strong> the girl who is not afraid to read out loud in class. I <strong>wish</strong> we <strong>lived</strong> nearer to the school. I <strong>wish</strong> Sunday <strong>were</strong> two days.</i></p>

<p>Some of them are <span class="cn-word" data-pos="adj" data-tr="ahmoqona">silly</span> and I am not going to write them here. One of them, in March 2016, is <i>I <strong>wish</strong> somebody <strong>knew</strong> what I want to do, because I do not.</i></p>

<p>I forgot the notebook completely. It stayed in a box of school things in my grandmother's house through two <span class="cn-word" data-tr="koʻchishlar">moves</span> and one <span class="cn-word" data-tr="taʼmirlash">renovation</span>.</p>

<p>My brother Bekzod found it in April, three weeks before my wedding, and he did not say one word about it for twenty days.</p>

<p>Then he stood up between the tables with a green notebook in his hand, and my whole family went quiet, and I understood everything one second before it started.</p>

<p>He read six wishes. He read the one about the bicycle, and my father laughed until he had to put his glass down, because the bicycle came in 2015 and it was <span class="cn-word" data-pos="adj" data-tr="ishlatilgan">second-hand</span> and blue. He read the one about the girl who is not afraid to read out loud — and I teach thirty children in a school in Yunusobod, and I read out loud for a living.</p>

<p>Then he read: <i>"I <strong>wish</strong> my brother <strong>would stop</strong> coming into my room and reading my things."</i></p>

<p>Two hundred people looked at Bekzod. He <span class="cn-word" data-pos="verb" data-tr="yelkasini qisdi">shrugged</span> and said one sentence: "Some wishes are not <span class="cn-word" data-pos="verb" data-tr="berilmaydi">granted</span>, and it is <span class="cn-word" data-pos="adj" data-tr="omadli">lucky</span> for everybody in this room."</p>

<p>The notebook is on a <span class="cn-word" data-tr="polka">shelf</span> in our flat. There is one thing in it I am still ashamed of: in 2016 I wrote <i>I <strong>wish</strong> we <strong>weren't</strong> this family</i>, after an <span class="cn-word" data-tr="janjal, tortishuv">argument</span> about money on a Thursday.</p>

<p><strong>If only</strong> I <strong>had written</strong> the next line as well. I remember the rest of that evening. My father sold his <span class="cn-word" data-tr="qoʻl soati">watch</span> that week and nobody was supposed to know.</p>''',
        "questions": [
            {
                "text": "Why did the wedding guests look at Bekzod?",
                "choices": [
                    "Because he read out a wish that was a complaint about him",
                    "Because he lost the notebook",
                    "Because he had bought the blue bicycle",
                ],
                "answer": 0,
                "explanation": "U oʻqigan tilaklardan biri — “ukam "
                               "narsalarimni oʻqishni toʻxtatsa edi”. "
                               "Va u aynan shu daftarni oʻqib turgan edi.",
            },
            {
                "text": "\"I wish I were the girl who is not afraid to read out loud.\" This means:",
                "choices": [
                    "she was that girl in the past",
                    "at that time she was NOT that girl, and wanted to be",
                    "she hopes to become that girl tomorrow",
                ],
                "answer": 1,
                "explanation": "<b>wish + past</b> — hozirgi haqiqatning "
                               "teskarisi. Yozgan paytda u oʻsha qiz "
                               "emas edi. Shakl oʻtgan zamonda, maʼno "
                               "esa oʻsha kunning oʻzida.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "I wish you pass the exam tomorrow.",
                    "I hope you pass the exam tomorrow.",
                    "I wish you would pass the exam tomorrow.",
                ],
                "answer": 1,
                "explanation": "Kelajakdagi yaxshilik uchun <b>hope</b> "
                               "ishlatiladi. <b>wish</b> — hozir yoki "
                               "oʻtganning teskarisi, yoki boshqa "
                               "odamning odatidan shikoyat.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-58 — relative clauses  (the man who fixed everything) [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Man Who Fixed Everything",
        "summary": (
            "PE-58 matni. Koʻchamizda hamma narsani tuzatadigan odam "
            "bor edi: nasos, telefon, eshik, tikuv mashinasi. "
            "Faqat bitta narsa — oʻzining darvozasi — yigirma yil "
            "singan holda turdi. Bir kuni oʻn bir kishi kelib "
            "oʻshani tuzatdi."
        ),
        "order":   58,
        "grammar": [
            {
                "pattern":  "who for people, that for both",
                "meaning":  "Ergash gap oʻzi izohlayotgan soʻzdan "
                            "<b>keyin</b> keladi — oʻzbekchada esa "
                            "oldin (“hamma narsani tuzatadigan "
                            "odam”). Odam uchun <b>who</b>, narsa "
                            "uchun <b>that</b>: <i>the man <b>who</b> "
                            "fixed everything</i>, <i>the pump "
                            "<b>that</b> stopped in June</i>.",
                "examples": ["He was the man who fixed everything on our street.",
                             "It was the only gate that he never touched."],
            },
            {
                "pattern":  "When you can leave it out",
                "meaning":  "Agar <i>who / that</i> dan keyin "
                            "<b>yangi ega</b> kelsa, uni tashlab "
                            "ketish mumkin: <i>the sewing machine "
                            "(<b>that</b>) my mother uses</i>. "
                            "Ega oʻzi boʻlsa — tashlab boʻlmaydi: "
                            "<i>the man <b>who</b> came at six</i>.",
                "examples": ["the sewing machine my mother still uses",
                             "the boy who carried his bag"],
            },
            {
                "pattern":  "The double-object mistake",
                "meaning":  "Ergash gap ichida <b>ikkinchi olmosh</b> "
                            "qoʻyilmaydi: <i>the pump that he fixed "
                            "<s>it</s></i> ✗ → <i>the pump that he "
                            "fixed</i> ✓. Oʻzbekchada obyekt "
                            "takrorlanadi, inglizchada esa "
                            "<i>that</i> allaqachon oʻsha obyekt.",
                "examples": ["the notebook that he kept in his pocket",
                             "the houses that he visited on Sundays"],
            },
        ],
        "body": '''<p>Anvar aka was the man <strong>who</strong> fixed everything on our street. He had been an <span class="cn-word" data-tr="muhandis">engineer</span> at the tractor <span class="cn-word" data-tr="zavod">factory</span> until 1993, and after that he was simply the man <strong>who</strong> came.</p>

<p>The <span class="cn-word" data-tr="nasos">pump</span> <strong>that</strong> stopped in every June. The gas <span class="cn-word" data-tr="pech, kolonka">heater</span> in the house at number 4 <strong>that</strong> nobody else would touch. The sewing machine <strong>that</strong> my mother still uses. Somebody's <span class="cn-word" data-tr="televizor antennasi">TV aerial</span>, in wind, on a roof, at sixty-three years old.</p>

<p>He kept a small <span class="cn-word" data-tr="daftarcha">notebook</span> in his shirt pocket <strong>that</strong> nobody ever read. He wrote a line in it at every house: a date, a house number, and two or three words.</p>

<p>The only thing in that street <strong>that</strong> he never fixed was his own <span class="cn-word" data-tr="darvoza">gate</span>. It hung on one <span class="cn-word" data-tr="petlya, sharnir">hinge</span> from about 2001, and it made a sound <strong>that</strong> everybody on our street could recognise from three houses away. His wife asked. His daughter asked. He said the same thing every time: he would do it on Sunday.</p>

<p>In November 2019 he had a <span class="cn-word" data-tr="insult">stroke</span>, on a Tuesday, in his own yard, and he spent nine days in the hospital in Chirchiq.</p>

<p>On the Saturday of that week eleven men came to his gate. Two of them were men <strong>who</strong> had not spoken to each other since a <span class="cn-word" data-tr="janjal">quarrel</span> about a wall in 2015. One was the boy from number 12 <strong>who</strong> is a <span class="cn-word" data-tr="payvandchi">welder</span> in Angren now, and he came with his own machine in the back of a car.</p>

<p>They took the gate off, they cut new hinges, they <span class="cn-word" data-pos="verb" data-tr="boʻyadilar">painted</span> it green, and they finished at half past four. Nobody organised it. Nobody was in charge.</p>

<p>Anvar aka came home in a taxi on the Thursday. He stood in front of that gate for a long time with his hand on the new hinge and he did not say anything at all, and my mother was watching all of it from our window, and she cried into a <span class="cn-word" data-tr="sochiq">towel</span>.</p>

<p>He is eighty-one. He walks with a stick now, and the notebook is still in his shirt pocket, and the last line in it is our house number.</p>''',
        "questions": [
            {
                "text": "Why did eleven men come to Anvar aka's gate?",
                "choices": [
                    "He asked them to help him",
                    "He was in hospital, and the street repaired the one thing he had never repaired himself",
                    "The city sent them",
                ],
                "answer": 1,
                "explanation": "U kasalxonada edi. Hech kim uyushtirmadi, "
                               "hech kim boshliq boʻlmadi — koʻcha uning "
                               "oʻzi hech qachon tuzatmagan yagona "
                               "narsani tuzatdi.",
            },
            {
                "text": "In which sentence can you leave out `that`?",
                "choices": [
                    "the pump that stopped in June",
                    "the sewing machine that my mother uses",
                    "the man that came at six",
                ],
                "answer": 1,
                "explanation": "<i>that</i> dan keyin yangi ega "
                               "(<i>my mother</i>) kelgani uchun uni "
                               "tashlab ketish mumkin. Qolgan "
                               "ikkitasida <i>that</i> ning oʻzi ega — "
                               "tashlab boʻlmaydi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "the gate that he never fixed it",
                    "the gate what he never fixed",
                    "the gate that he never fixed",
                ],
                "answer": 2,
                "explanation": "Ergash gap ichida obyekt ikki marta "
                               "aytilmaydi (<i>fixed it</i> ✗), va "
                               "inglizchada <i>what</i> ergash gap "
                               "boshlamaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-59 — defining vs non-defining  (one missing comma)  [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "My Sister, Who Lives in Almaty",
        "summary": (
            "PE-59 matni. Bitta vergul tushib qoldi — va oila "
            "notoʻgʻri jiyan uchun xona tayyorladi. Oʻsha kecha "
            "bizning oilada oʻn yildan beri aytiladigan hazil "
            "tugʻildi."
        ),
        "order":   59,
        "grammar": [
            {
                "pattern":  "Defining — it tells you WHICH one",
                "meaning":  "Verguldan xoli ergash gap "
                            "<b>qaysi</b> ekanini aytadi va gapdan "
                            "olib tashlab boʻlmaydi: <i>My cousin "
                            "<b>who works in Moscow</b> is coming</i> "
                            "— bir necha jiyan bor, kelayotgani "
                            "Moskvada ishlaydigani.",
                "examples": ["My cousin who works in Moscow is coming.",
                             "The room that faces the street is warmer."],
            },
            {
                "pattern":  "Non-defining — it just adds a fact",
                "meaning":  "Ikki vergul orasidagi ergash gap "
                            "<b>qoʻshimcha maʼlumot</b>: "
                            "<i>My sister<b>,</b> who lives in "
                            "Almaty<b>,</b> is coming</i> — opam "
                            "bitta, Olmatida yashashi shunchaki "
                            "qoʻshimcha. Uni olib tashlasa ham gap "
                            "butun qoladi.",
                "examples": ["My sister, who lives in Almaty, phones every Sunday.",
                             "Our neighbour, who is eighty-one, still walks to the market."],
            },
            {
                "pattern":  "Three rules change with the commas",
                "meaning":  "Vergul bilan: <b>that</b> ishlatilmaydi "
                            "(faqat <i>who</i> / <i>which</i>), "
                            "olmosh tashlab ketilmaydi, va "
                            "<b>which</b> butun bir fikrga ham "
                            "ishora qiladi: <i>He came on the "
                            "Tuesday<b>, which</b> nobody expected</i>.",
                "examples": ["The bed, which we had made up for Jahongir, stayed empty.",
                             "He slept on the floor, which he has never forgotten."],
            },
        ],
        "body": '''<p>We have two cousins with the same name. Jahongir <span class="cn-word" data-pos="verb" data-tr="katta">the elder</span> works in Moscow and has done for nine years. Jahongir the younger was twenty-two that spring and had never been <span class="cn-word" data-pos="adv" data-tr="uzoqroq">further</span> than Guliston.</p>

<p>In April 2016 my brother sent one message to the family group: <i>My cousin who works in Moscow is coming on Tuesday for two weeks.</i></p>

<p>He <span class="cn-word" data-pos="verb" data-tr="moʻljallagan edi">meant</span> to write: <i>My cousin, who works in Moscow, is coming.</i> Two commas. He was on a bus.</p>

<p>Without the commas the sentence tells you <strong>which</strong> cousin: the Moscow one. And that is exactly what my mother read, at half past nine at night, standing in the kitchen.</p>

<p>So the house prepared for Jahongir the elder, <strong>who</strong> is thirty-four, <strong>who</strong> drinks <span class="cn-word" data-tr="qora choy">black tea</span> with no sugar, and <strong>who</strong> cannot sleep in a room with a window on the street.</p>

<p>The good bed came out of the back room. The <span class="cn-word" data-tr="karavot">bed</span>, <strong>which</strong> we had made up with the new <span class="cn-word" data-tr="choyshab">sheets</span>, went into the quiet room at the back. My father bought a kilo of the <span class="cn-word" data-tr="quruq mevalar">dried fruit</span> that Jahongir the elder likes. My mother cooked for a man of thirty-four, <strong>which</strong> in our house means meat twice.</p>

<p>At eight on Tuesday evening Jahongir the younger arrived at the gate with a <span class="cn-word" data-tr="paket">plastic bag</span> and a football <span class="cn-word" data-tr="futbolka">shirt</span> in it.</p>

<p>Nobody said one word about the room for about ten seconds, <strong>which</strong> is a long time in a family of eleven people.</p>

<p>He stayed nineteen days. He slept in the back room on the good sheets for one night, and then he moved to the floor of the boys' room because it was <span class="cn-word" data-pos="adj" data-tr="qiziqarli">more fun</span>, <strong>which</strong> nobody argued with. He ate the dried fruit. He put sugar in everything.</p>

<p>My aunt, <strong>who</strong> notices everything, <span class="cn-word" data-pos="verb" data-tr="fahmladi, aniqladi">worked out</span> what had happened on the Thursday and read the message out loud twice, slowly, once with the commas and once without them.</p>

<p>The other Jahongir came in August, in a taxi from the <span class="cn-word" data-tr="aeroport">airport</span>, and my brother met him at the gate with the sentence our family now says instead of hello: "Which cousin are you?"</p>''',
        "questions": [
            {
                "text": "Why did the family prepare for the wrong cousin?",
                "choices": [
                    "The message had no commas, so it said WHICH cousin — the Moscow one",
                    "Both cousins live in Moscow",
                    "The younger cousin arrived a day early",
                ],
                "answer": 0,
                "explanation": "Vergulsiz ergash gap “qaysi jiyan” "
                               "ekanini aniqlaydi. Vergul bilan boʻlsa, "
                               "u shunchaki qoʻshimcha maʼlumot boʻlar "
                               "edi.",
            },
            {
                "text": "\"My sister, who lives in Almaty, phones every Sunday\" tells us:",
                "choices": [
                    "the speaker has several sisters",
                    "the speaker has one sister, and Almaty is extra information",
                    "the sister does not live in Almaty",
                ],
                "answer": 1,
                "explanation": "Ikki vergul — qoʻshimcha maʼlumot "
                               "belgisi. Opa bitta; Olmatida "
                               "yashashini olib tashlasa ham gap "
                               "toʻliq qoladi.",
            },
            {
                "text": "Which sentence is WRONG?",
                "choices": [
                    "My aunt, who notices everything, worked it out.",
                    "My aunt, that notices everything, worked it out.",
                    "He slept on the floor, which nobody argued with.",
                ],
                "answer": 1,
                "explanation": "Vergul bilan kelgan ergash gapda "
                               "<b>that</b> ishlatilmaydi — faqat "
                               "<i>who</i> yoki <i>which</i>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-60 — passive present & past  (the bridge)            [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Bridge Was Built in 1957",
        "summary": (
            "PE-60 matni. Koʻprikdagi lavhada 1957-yil yozilgan. "
            "Lekin qishloq uni lavhadagi nom bilan emas, bir ayolning "
            "ismi bilan chaqiradi — va buning sababi koʻprik "
            "qurilishidan toʻqqiz yil oldin boshlangan."
        ),
        "order":   60,
        "grammar": [
            {
                "pattern":  "How the passive is built",
                "meaning":  "<b>be + V3</b>. Hozirgi: <i>The bridge "
                            "<b>is repaired</b> every spring</i>. "
                            "Oʻtgan: <i>The bridge <b>was built</b> in "
                            "1957</i>. Koʻplikda <i>are / were</i>: "
                            "<i>The stones <b>were brought</b> from "
                            "Angren</i>.",
                "examples": ["The bridge was built in 1957.",
                             "It is repaired every spring.",
                             "The stones were brought from the hills."],
            },
            {
                "pattern":  "Why choose the passive?",
                "meaning":  "Ish bajaruvchisi <b>muhim emas</b>, "
                            "<b>maʼlum emas</b>, yoki gapning "
                            "diqqati <b>obyektda</b>: koʻprik haqida "
                            "gapiryapmiz, quruvchilar haqida emas. "
                            "Shuning uchun passiv — hisobot, yangilik "
                            "va tarix tili.",
                "examples": ["The road was closed for three days.",
                             "My grandfather's name is not written on it."],
            },
            {
                "pattern":  "by + the doer, when it matters",
                "meaning":  "Bajaruvchi kerak boʻlsa — <b>by</b>: "
                            "<i>The bridge <b>was designed by</b> a "
                            "young engineer</i>. Kerak boʻlmasa "
                            "aytilmaydi. Aktivdan passivga: obyekt "
                            "boshiga chiqadi, feʼl <b>be + V3</b> "
                            "boʻladi, ega esa <b>by</b> bilan oxirga "
                            "koʻchadi (yoki yoʻqoladi).",
                "examples": ["The plan was signed by the district engineer.",
                             "The name was given by the village, not by the office."],
            },
        ],
        "body": '''<p>The bridge over the Chirchiq at the end of our village <strong>was built</strong> in 1957. The date <strong>is written</strong> on a grey concrete <span class="cn-word" data-tr="lavha">plaque</span> at the northern end, under two lines that nobody reads: the name of a district office and the name of an <span class="cn-word" data-tr="muhandis">engineer</span>.</p>

<p>It is thirty-one metres long. The <span class="cn-word" data-tr="beton">concrete</span> <strong>was poured</strong> in October, and some of the <span class="cn-word" data-tr="temir armatura">iron</span> <strong>was brought</strong> from a factory in Angren on two <span class="cn-word" data-tr="yuk mashinalari">lorries</span>. It <strong>is repaired</strong> every spring, because the river <strong>is fed</strong> by <span class="cn-word" data-tr="qor suvi">snow water</span> and it takes the <span class="cn-word" data-tr="qirgʻoq">bank</span> away in April. Three of the <span class="cn-word" data-tr="ustunlar">posts</span> <strong>were replaced</strong> in 2011, and the road on top <strong>was covered</strong> with new <span class="cn-word" data-tr="asfalt">asphalt</span> in 2019.</p>

<p>All of that <strong>is recorded</strong> in the district <span class="cn-word" data-tr="arxiv">archive</span>, and none of it is the interesting part.</p>

<p>The bridge <strong>is not called</strong> by the name on the plaque. On both sides of the river it <strong>is called</strong> Oysha koʻprik — Oysha's bridge — and it always has been.</p>

<p>Before 1957 there was no bridge here at all. Between the two villages there was a <span class="cn-word" data-tr="kechuv joyi">crossing place</span> where the water is wide and slow, and in summer a boy could walk it. In April and May he could not.</p>

<p>Oysha opa was born in 1919. From 1948, when the school on this side opened, she stood at that crossing place every school morning from March to June, and she carried the small children across on her back, two at a time, one on each arm when they were very small. Nine years. Her own children first, then everybody's.</p>

<p>She <strong>was never paid</strong> anything and she never asked. In 1955 a girl of six <strong>was pulled</strong> out of the water forty metres below the crossing by two men cutting <span class="cn-word" data-tr="qamish">reeds</span>, alive, and that story <strong>was told</strong> in the district centre by somebody who mattered.</p>

<p>The bridge <strong>was finished</strong> two years later.</p>

<p>Oysha opa died in 1991. Her name <strong>is not written</strong> anywhere on the concrete, and nobody in the village has ever suggested writing it there. It <strong>is kept</strong> in the only place that lasts: two hundred people say it every day without thinking about it, when they tell somebody where to turn.</p>''',
        "questions": [
            {
                "text": "Why is the bridge called Oysha koʻprik?",
                "choices": [
                    "Because Oysha opa designed it",
                    "Because for nine years she carried the schoolchildren across the river on her back",
                    "Because her name is written on the plaque",
                ],
                "answer": 1,
                "explanation": "1948-yildan 1957-yilgacha u har bahor "
                               "maktabga boradigan kichkina bolalarni "
                               "yelkasida suvdan oʻtkazgan. Lavhada esa "
                               "uning ismi yoʻq.",
            },
            {
                "text": "\"The concrete was poured in October.\" Why is the passive used here?",
                "choices": [
                    "Because we do not know or care who poured it — the concrete is the subject",
                    "Because it happened a long time ago",
                    "Because the sentence has no verb",
                ],
                "answer": 0,
                "explanation": "Passiv diqqatni obyektga qaratadi. "
                               "Kim quygani muhim emas — gap koʻprik "
                               "haqida, quruvchilar haqida emas.",
            },
            {
                "text": "Change to the passive: \"Two lorries brought the iron.\"",
                "choices": [
                    "The iron was brought by two lorries.",
                    "The iron is brought by two lorries.",
                    "The iron was bring by two lorries.",
                ],
                "answer": 0,
                "explanation": "Obyekt boshiga chiqadi, feʼl "
                               "<b>was + V3</b> boʻladi, ega esa "
                               "<b>by</b> bilan oxirga koʻchadi. "
                               "<i>bring</i> ning V3 shakli — "
                               "<i>brought</i>.",
            },
        ],
    },
]
