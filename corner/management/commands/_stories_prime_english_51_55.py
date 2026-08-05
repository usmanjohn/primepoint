# -*- coding: utf-8 -*-
"""Prime English Readings — PE-51 … PE-55 (batch 11). Modal capstone + conditionals.

PE-51 the full modal strength scale · PE-52 conjunctions (and/but/or/so/because/
although) · PE-53 zero & first conditional · PE-54 second conditional · PE-55 third
conditional.

Shapes:
  51 — a mountain search at dusk: every modal on the certainty scale, and the smallest
       voice in the group holds the only good deduction
  52 — a life story with one hinge: a boy runs six kilometres with his brother's exam
       papers, arrives four minutes late, and a whole family comes out of it
  53 — a repair-shop master with a taped-over button and a hand-written notice; the
       button is not a machine test, it is a test of the apprentice
  54 — thirty papers from 2009, "what would you do with a thousand dollars", and the
       one sentence that stopped being imaginary
  55 — nine minutes, one missed flight in 2011, and a doctorate that thanks a traffic jam

Cumulative rule: PE-51 and PE-52 use NO conditionals at all (they arrive in PE-53) —
PE-51 keeps to modals and PE-52 to conjunctions. PE-53 uses zero + first only, PE-54
adds the second, PE-55 the third. No `wish` (PE-57), no `which` / non-defining relative
clauses (PE-58/59), no passive (PE-60), no reported speech with backshift (PE-62 —
direct quotes only), no `as … as` / `too` / `enough` (PE-67/68).
Length: 270–310 words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_51_55.py --author=prime
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
    # PE-51 — the full modal scale  (the search on the mountain)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   'From "Maybe" to "Definitely"',
        "summary": (
            "PE-51 matni. Chimyonda kech kirdi va bitta bola yoʻq. "
            "Yigirma kishi taxmin qiladi: “boʻlishi mumkin emas”, "
            "“boʻlsa kerak”, “balki”. Toʻgʻri taxminni esa eng kichkina "
            "ovoz aytdi — chunki u bitta faktni bilardi."
        ),
        "order":   51,
        "grammar": [
            {
                "pattern":  "The certainty scale in one line",
                "meaning":  "Bir xil gap, ishonchning besh darajasi: "
                            "<i>He <b>can't be</b> up there</i> (0%) → "
                            "<i>He <b>might / may / could be</b> up "
                            "there</i> (50%) → <i>He <b>should be</b> "
                            "up there</i> (kutilgan) → <i>He <b>must "
                            "be</b> up there</i> (95%) → <i>He <b>is</b> "
                            "up there</i> (100%).",
                "examples": ["He can't be on the top road.",
                             "He might be at the spring.",
                             "He must be somewhere below the ridge."],
            },
            {
                "pattern":  "One word, two different jobs",
                "meaning":  "Modal soʻzning maʼnosi gapdan chiqadi: "
                            "<i>You <b>must</b> stay together</i> — "
                            "majburiyat, <i>He <b>must</b> be cold</i> "
                            "— taxmin. <i><b>Could</b> you shout?</i> — "
                            "iltimos, <i>He <b>could</b> climb it at "
                            "nine</i> — imkoniyat, <i>He <b>could</b> "
                            "be there</i> — taxmin. Shuning uchun "
                            "modalni yodlamaydi — uni <b>ishi</b> bilan "
                            "tushunadi.",
                "examples": ["You must stay together.",
                             "He must be cold by now.",
                             "She could read a map at nine."],
            },
            {
                "pattern":  "Moving the whole scale into the past",
                "meaning":  "Bitta formula hammasini oʻtgan zamonga "
                            "koʻchiradi: <b>modal + have + V3</b>. "
                            "<i>He <b>must have gone</b> down</i> "
                            "(taxmin), <i>He <b>can't have climbed</b> "
                            "it</i> (rad), <i>He <b>should have told</b> "
                            "somebody</i> (afsus), <i>She <b>could have "
                            "shouted</b></i> (imkon boʻlgan, boʻlmagan).",
                "examples": ["He must have gone down towards the water.",
                             "He should have told somebody.",
                             "He can't have walked past the bridge."],
            },
        ],
        "body": '''<p>It gets dark in the mountains above Chimyon at about eight in September, and it gets dark quickly. At ten past eight the teacher counted twenty-one heads and found twenty.</p>

<p>Jasur was fourteen and he had been at the back of the line an hour before.</p>

<p>"Nobody moves alone. You <strong>must</strong> stay in threes," the teacher said, and then, quietly, to the two drivers: "He <strong>must be</strong> tired by now. He <strong>must be</strong> cold."</p>

<p>The <span class="cn-word" data-tr="taxminlar">guesses</span> started, and every one of them had a different weight.</p>

<p>"He <strong>could be</strong> up on the top road."</p>

<p>"He <strong>can't be</strong> up there — his <span class="cn-word" data-tr="ryukzak">rucksack</span> is here, on this stone."</p>

<p>"He <strong>might be</strong> at the bus. Or he <strong>may be</strong> asleep somewhere under the trees."</p>

<p>"He <strong>should be</strong> at the bus. That is where we told everybody to wait."</p>

<p>The drivers <span class="cn-word" data-pos="verb" data-tr="qichqirmoqchi">shouted</span> his name into the dark for twenty minutes and the mountain gave it back to them. Somebody said the sentence that everybody was thinking: "He <strong>should have told</strong> one of us."</p>

<p>Then Dilnoza, who is twelve and his sister, pulled the teacher's <span class="cn-word" data-tr="yeng">sleeve</span>.</p>

<p>"He <strong>can't have gone</strong> up," she said. "He is afraid of the <span class="cn-word" data-tr="qir, choʻqqi qirrasi">ridge</span> — he <strong>wouldn't</strong> walk along it even in the daytime. And he <strong>must be</strong> near water. He gave his bottle to Sherbek at four o'clock, so he has no water. He <strong>can't</strong> go two hours without water."</p>

<p>Nobody had thought about the bottle.</p>

<p>They found him at the <span class="cn-word" data-tr="buloq">spring</span> below the second <span class="cn-word" data-tr="burilish">bend</span>, sitting with his shoes off and one <span class="cn-word" data-pos="adj" data-tr="shishgan">swollen</span> ankle, forty minutes later. He had <span class="cn-word" data-pos="verb" data-tr="oyogʻini burab olgan">twisted</span> it, and he had come down to the water on purpose, because water goes down and down leads to a road.</p>

<p>Twenty people <span class="cn-word" data-pos="verb" data-tr="taxmin qildilar">guessed</span> that evening. The best deduction in the group came from the smallest person in it, and it was not <span class="cn-word" data-tr="omad">luck</span>: she was the only one who knew about the bottle.</p>''',
        "questions": [
            {
                "text": "How did Dilnoza work out where her brother was?",
                "choices": [
                    "She knew he had given his water bottle away, and that he was afraid of the ridge",
                    "She saw him walking down to the spring",
                    "She found his rucksack near the water",
                ],
                "answer": 0,
                "explanation": "Ikkita fakt: akasi suvsiz qolgan edi va "
                               "qirdan qoʻrqadi. Shuning uchun “yuqoriga "
                               "chiqqan boʻlishi mumkin emas, suv "
                               "yonida boʻlsa kerak” degan xulosa chiqdi.",
            },
            {
                "text": "\"He can't be up there — his rucksack is here.\" This shows the speaker is:",
                "choices": [
                    "about fifty per cent sure",
                    "sure that it is impossible",
                    "giving him permission",
                ],
                "answer": 1,
                "explanation": "<b>can't be</b> — shkalaning eng past "
                               "nuqtasi: 0%, “boʻlishi mumkin emas”. "
                               "Dalil — ryukzak shu yerda.",
            },
            {
                "text": "In \"You must stay in threes\" and \"He must be cold\", `must` means:",
                "choices": [
                    "obligation in the first, deduction in the second",
                    "deduction in both",
                    "obligation in both",
                ],
                "answer": 0,
                "explanation": "Bitta modal ikki ishni bajaradi: "
                               "birinchisi — majburiyat (buyruq), "
                               "ikkinchisi — taxmin (“sovqotgan boʻlsa "
                               "kerak”). Maʼnoni gap belgilaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-52 — conjunctions  (six kilometres, four minutes late)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "He Was Late, So He Ran",
        "summary": (
            "PE-52 matni. 1998-yil: onasi kichik oʻgʻlini akasining "
            "hujjatlari bilan shaharga yubordi. U olti kilometr yugurdi "
            "va toʻrt daqiqaga kechikdi. Butun bir oila shu toʻrt "
            "daqiqadan chiqdi."
        ),
        "order":   52,
        "grammar": [
            {
                "pattern":  "so and because — same idea, opposite order",
                "meaning":  "<b>because</b> + sabab, <b>so</b> + natija. "
                            "<i>He ran <b>because</b> he was late</i> = "
                            "<i>He was late, <b>so</b> he ran</i>. "
                            "Bir voqea, ikki tartib — ikkisini bir "
                            "gapda takrorlamaydi (<i>Because he was "
                            "late, so he ran</i> ✗).",
                "examples": ["He was late, so he ran.",
                             "He ran because the office shut at twelve."],
            },
            {
                "pattern":  "but / although — the contrast pair",
                "meaning":  "<b>but</b> ikki gapni tenglashtiradi: "
                            "<i>He ran fast, <b>but</b> he was late</i>. "
                            "<b>Although</b> esa gap boshida ham "
                            "kelaveradi: <i><b>Although</b> he ran "
                            "fast, he was late</i>. Oʻzbekchadan "
                            "koʻchadigan xato — ikkisini birga qoʻyish: "
                            "<i>Although he ran, but he was late</i> ✗.",
                "examples": ["Although he ran the whole way, the gate was shut.",
                             "He knocked, but nobody came."],
            },
            {
                "pattern":  "and / or — adding and choosing",
                "meaning":  "<b>and</b> qoʻshadi, <b>or</b> tanlaydi: "
                            "<i>He could wait <b>or</b> go home</i>. "
                            "Vergul: uzun ikki gap orasida <i>, and</i> "
                            "/ <i>, but</i> / <i>, so</i> — qisqa "
                            "boʻlaklar orasida esa vergul kerak emas "
                            "(<i>bread and tea</i>).",
                "examples": ["He had two som and a bus ticket.",
                             "He could knock again or sit down on the step."],
            },
        ],
        "body": '''<p>In July 1998 my grandmother stood at the gate with an <span class="cn-word" data-tr="konvert">envelope</span> in her hand and one instruction. The <span class="cn-word" data-tr="hujjatlar">documents</span> for my uncle Rustam's university <span class="cn-word" data-tr="ariza">application</span> had to be at the office in the district centre before twelve o'clock, <strong>and</strong> Rustam himself was in the field with the water, six hours from a road.</p>

<p>So she sent my father, who was thirteen.</p>

<p>The bus came at half past ten <strong>and</strong> it stopped after two kilometres, <strong>because</strong> something in the <span class="cn-word" data-tr="dvigatel">engine</span> had had enough of 1998. The driver opened everything, looked inside, <strong>and</strong> lit a cigarette. Some passengers waited. Others walked back.</p>

<p>My father was late, <strong>so</strong> he ran.</p>

<p>He ran the six kilometres in the middle of the day in July, with the envelope inside his shirt <strong>because</strong> his hands were <span class="cn-word" data-pos="adj" data-tr="terlab ketgan">sweating</span>, <strong>and</strong> he arrived at the office at four minutes past twelve.</p>

<p><strong>Although</strong> he knocked for ten minutes, nobody opened the door. A <span class="cn-word" data-tr="qorovul">guard</span> came round the corner <strong>and</strong> told him the truth: the papers were <span class="cn-word" data-pos="adj" data-tr="joyida, yaxshi">fine</span>, the boy was fine, <strong>but</strong> the clock was the clock.</p>

<p>So Rustam did not go to that university. He went to the <span class="cn-word" data-tr="pedagogika instituti">teacher training institute</span> in Samarkand instead, <strong>because</strong> it was the only place that still took <span class="cn-word" data-tr="hujjatlar topshirish">applications</span> in August.</p>

<p>In his second year there he sat next to a girl from Urgut in a <span class="cn-word" data-tr="kutubxona">library</span>, <strong>and</strong> they argued about a <span class="cn-word" data-tr="xarita">map</span> of the Silk Road for an hour <strong>and</strong> a half.</p>

<p>They have four children. The oldest one is a doctor in Tashkent, <strong>and</strong> the youngest one is my favourite cousin.</p>

<p>My father tells this story at every family table, <strong>and</strong> he always finishes it in the same way. He is fifty now, <strong>and</strong> he still runs — three mornings a week, along the <span class="cn-word" data-tr="kanal, ariq">canal</span>.</p>

<p>"I lost by four minutes," he says, "<strong>so</strong> I got a whole family. <strong>Although</strong> I did not know it that day, that was the fastest six kilometres anybody in this house has ever run."</p>''',
        "questions": [
            {
                "text": "Why did Rustam go to the institute in Samarkand?",
                "choices": [
                    "Because it was closer to the village",
                    "Because the papers arrived four minutes late at the first office, and Samarkand still took applications in August",
                    "Because he wanted to be a teacher",
                ],
                "answer": 1,
                "explanation": "Hujjatlar 12:04 da yetib bordi va eshik "
                               "yopiq edi. Avgustda ariza qabul "
                               "qilayotgan yagona joy — Samarqanddagi "
                               "institut boʻlgan.",
            },
            {
                "text": "Which sentence is correct English?",
                "choices": [
                    "Because he was late, so he ran.",
                    "Although he ran fast, but he was late.",
                    "He was late, so he ran.",
                ],
                "answer": 2,
                "explanation": "<b>because</b> va <b>so</b> bir gapda "
                               "takrorlanmaydi; <b>although</b> va "
                               "<b>but</b> ham. Bitta bogʻlovchi — "
                               "bitta ish.",
            },
            {
                "text": "\"Although he knocked for ten minutes, nobody opened the door.\" The same idea with `but`:",
                "choices": [
                    "He knocked for ten minutes, but nobody opened the door.",
                    "He knocked for ten minutes, so nobody opened the door.",
                    "Because he knocked for ten minutes, nobody opened the door.",
                ],
                "answer": 0,
                "explanation": "<b>Although</b> — qarama-qarshilik, "
                               "demak uning juftligi <b>but</b>. "
                               "<i>so</i> natija, <i>because</i> sabab "
                               "bildiradi va maʼnoni butunlay "
                               "oʻzgartiradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-53 — zero & first conditional  (the taped-over button)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "If You Press This Button",
        "summary": (
            "PE-53 matni. Ustaxonadagi eski stanokda skotch bilan "
            "yopilgan tugma va qoʻlda yozilgan eʼlon bor: “Bu tugmani "
            "bossang, hech narsa boʻlmaydi. Ikki marta bossang, kelib "
            "menga aytasan.” Yigirma yil davomida bu tugma stanokni "
            "emas, shogirdni sinaydi."
        ),
        "order":   53,
        "grammar": [
            {
                "pattern":  "Zero conditional — always true",
                "meaning":  "<b>If + present simple → present simple</b>. "
                            "Doim, har safar sodir boʻladigan narsa: "
                            "qonun, qoida, mashinaning ishlashi. "
                            "<i><b>If</b> you press this button, the "
                            "machine <b>stops</b></i>. Bunda "
                            "<i>if</i> = <i>when</i>.",
                "examples": ["If you press the green button, the belt starts.",
                             "If metal gets hot, it grows."],
            },
            {
                "pattern":  "First conditional — one real future",
                "meaning":  "<b>If + present simple → will + V1</b>. "
                            "Kelasi zamondagi haqiqiy ehtimol: "
                            "<i><b>If</b> you <b>come</b> and tell me, "
                            "I <b>will teach</b> you</i>. Diqqat: "
                            "<i>if</i> dan keyin <b>will</b> qoʻyilmaydi "
                            "(<i>If you will come</i> ✗) — bu "
                            "oʻzbekchadan koʻchadigan eng koʻp xato.",
                "examples": ["If you tell me the truth, I will teach you everything.",
                             "If you say nothing, you will stay at the door."],
            },
            {
                "pattern":  "unless = if … not",
                "meaning":  "<b>unless</b> — “agar … boʻlmasa”: "
                            "<i>You <b>won't</b> learn this trade "
                            "<b>unless</b> you ask questions</i> = "
                            "<i>if you don't ask questions</i>. "
                            "<b>unless</b> dan keyin inkor qoʻyilmaydi "
                            "— inkor allaqachon soʻzning ichida.",
                "examples": ["Unless you ask, nobody will explain.",
                             "The machine won't start unless the door is shut."],
            },
        ],
        "body": '''<p>Karim aka has repaired <span class="cn-word" data-tr="kir yuvish mashinalari">washing machines</span> in the same yard in Chirchiq since 1994. In the corner there is an old green machine with a <span class="cn-word" data-tr="tugma">button</span> covered in yellow <span class="cn-word" data-tr="skotch">tape</span>, and above it a card in his own handwriting:</p>

<p><i><strong>If you press this button, nothing happens. If you press it twice, come and find me.</strong></i></p>

<p>Every new <span class="cn-word" data-tr="shogird">apprentice</span> reads that card in his first week. Karim aka explains the yard, the <span class="cn-word" data-tr="asboblar">tools</span>, the <span class="cn-word" data-tr="hisob kitob daftari">accounts book</span>, and the ordinary rules of the trade: <strong>if</strong> you hold a <span class="cn-word" data-tr="vintqaytargich, tornavort">screwdriver</span> like that, you <strong>break</strong> the head. <strong>If</strong> water <strong>gets</strong> into that box, the whole board <strong>dies</strong>. Then he goes to lunch and leaves the boy alone with the green machine for an hour.</p>

<p>They all press it. Every single one, in twenty years, has pressed it — because the card says nothing happens, and a boy of sixteen has to know.</p>

<p>Nothing happens.</p>

<p>Then, of course, they press it again.</p>

<p>The second press does nothing either. The button has not been <span class="cn-word" data-pos="adj" data-tr="ulangan">connected</span> to anything since 1996.</p>

<p>Bekzod pressed it twice on a Tuesday in March, put the tape back exactly as it had been, and said nothing for two days. On Thursday he came into the office and stood there with his hands behind his back.</p>

<p>"I pressed it twice," he said.</p>

<p>"Good," Karim aka said. "<strong>If</strong> you <strong>tell</strong> me the truth about a small thing, I <strong>will believe</strong> you about a big one. So <strong>if</strong> you <strong>break</strong> something next month, you <strong>will come</strong> and tell me the same day, and I <strong>will not</strong> <span class="cn-word" data-pos="verb" data-tr="baqirmayman">shout</span>. That is the whole <span class="cn-word" data-tr="shartnoma, kelishuv">deal</span>."</p>

<p>Two boys in twenty years never came. They did good work and they left in the autumn, and Karim aka did not keep them, and he did not explain why.</p>

<p><strong>Unless</strong> a man tells you about a button, he says, he <strong>will not</strong> tell you about a <span class="cn-word" data-tr="isitgich">heater</span> that he has <span class="cn-word" data-pos="verb" data-tr="notoʻgʻri ulagan">wired wrong</span> in somebody's kitchen.</p>

<p>Bekzod has his own workshop in Yangiyoʻl now. There is a green machine in the corner of it, with a button under yellow tape, and a card above it in his handwriting.</p>''',
        "questions": [
            {
                "text": "What does the button really test?",
                "choices": [
                    "Whether the machine still works",
                    "Whether the apprentice will admit a small mistake",
                    "Whether the apprentice can repair a wire",
                ],
                "answer": 1,
                "explanation": "Tugma 1996-yildan hech narsaga ulanmagan. "
                               "U stanokni emas, shogirdning "
                               "rostgoʻyligini sinaydi.",
            },
            {
                "text": "\"If you press this button, nothing happens.\" This is:",
                "choices": [
                    "a zero conditional — it is always true, every time",
                    "a first conditional — one future possibility",
                    "advice",
                ],
                "answer": 0,
                "explanation": "<b>If + present → present</b> — har safar "
                               "shunday boʻladi. Shuning uchun bu nol "
                               "shart, va bu yerda <i>if</i> = "
                               "<i>when</i>.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "If you will tell me the truth, I will believe you.",
                    "If you tell me the truth, I will believe you.",
                    "If you tell me the truth, I believe you tomorrow.",
                ],
                "answer": 1,
                "explanation": "Birinchi shartda <i>if</i> dan keyin "
                               "<b>will</b> ishlatilmaydi — shart "
                               "qismida hozirgi zamon, natija qismida "
                               "<b>will</b>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-54 — second conditional  (thirty papers from 2009)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "If I Had a Thousand Dollars",
        "summary": (
            "PE-54 matni. 2009-yilda oʻqituvchi oʻttiz oʻquvchiga "
            "bitta savol berdi: “Ming dollaring boʻlsa, nima "
            "qilardingiz?” Qogʻozlarni saqlab qoʻydi. Oʻn besh yildan "
            "keyin ulardan bittasi endi xayoliy gap emas edi."
        ),
        "order":   54,
        "grammar": [
            {
                "pattern":  "If + past simple → would + V1",
                "meaning":  "Ikkinchi shart — <b>xayoliy hozir</b>: "
                            "<i><b>If</b> I <b>had</b> a thousand "
                            "dollars, I <b>would buy</b> a bus</i>. "
                            "Shakl oʻtgan zamonda, maʼno esa hozirgi "
                            "— chunki bu haqiqat emas. Mingi yoʻq, "
                            "shuning uchun avtobus ham yoʻq.",
                "examples": ["If I had a thousand dollars, I would buy a bus.",
                             "If she lived in the city, she would walk to school."],
            },
            {
                "pattern":  "First or second? Real or imaginary?",
                "meaning":  "Bitta savol yechadi: bu <b>haqiqiy "
                            "ehtimol</b>mi? <i>If I <b>get</b> the "
                            "money, I <b>will</b> buy it</i> — pul "
                            "kelishi mumkin (haqiqiy). <i>If I "
                            "<b>had</b> the money, I <b>would</b> buy "
                            "it</i> — pulim yoʻq (xayoliy). Shakl "
                            "oʻzgarishi maʼnoni oʻzgartiradi.",
                "examples": ["If I get a scholarship, I will study in Tashkent.",
                             "If I had a scholarship, I would study in Tashkent."],
            },
            {
                "pattern":  "If I were you — one fixed phrase",
                "meaning":  "Ikkinchi shartda <i>I / he / she</i> bilan "
                            "ham <b>were</b> ishlatiladi, va "
                            "<b>If I were you, I would…</b> — maslahat "
                            "berishning eng koʻp uchraydigan yoʻli. "
                            "Natija qismida <b>could</b> va "
                            "<b>might</b> ham keladi: <i>we <b>could "
                            "buy</b> a bus</i>.",
                "examples": ["If I were you, I would keep that paper.",
                             "If we collected the money, we could buy a bus."],
            },
        ],
        "body": '''<p>In October 2009 a teacher in a village school near Denov gave her class one question and one sheet of paper each. Thirty pupils, thirty <span class="cn-word" data-tr="varaq">sheets</span>, twenty minutes.</p>

<p><i>What <strong>would</strong> you do <strong>if</strong> you <strong>had</strong> a thousand dollars?</i></p>

<p>She read them at home that evening and she did not throw them away. She put them in a brown <span class="cn-word" data-tr="papka">folder</span> in the bottom <span class="cn-word" data-tr="tortma">drawer</span> of her desk, and there they stayed through two <span class="cn-word" data-tr="taʼmirlash">repairs</span> of the school building.</p>

<p>Most of them are what you expect from thirteen-year-olds, and they are wonderful. "<strong>If</strong> I <strong>had</strong> a thousand dollars, I <strong>would buy</strong> a telephone with a camera and a motorbike, and I <strong>would give</strong> my mother the rest." "I <strong>would buy</strong> a <span class="cn-word" data-tr="muzlatgich">fridge</span> and eleven kilos of ice cream." "I <strong>would go</strong> to Dubai for one day and come back the same night, because my grandmother <strong>would worry</strong>."</p>

<p>One of them, in careful <span class="cn-word" data-tr="qoʻl yozuvi">handwriting</span>, says this:</p>

<p><i>"<strong>If</strong> I <strong>had</strong> a thousand dollars, I <strong>would buy</strong> a bus for our street. Not a new one. Then the small children <strong>would not walk</strong> seven kilometres in February, and my sister <strong>would not miss</strong> school when it rains. <strong>If</strong> the bus <strong>were</strong> ours, we <strong>could take</strong> the old women to the hospital in Denov on Fridays."</i> — Nilufar S., 13.</p>

<p>Nilufar did not get a thousand dollars. She got a job in a bank in Termez, eleven years of it, and a <span class="cn-word" data-tr="mahalla qoʻmitasi">neighbourhood committee</span> that she joined and then <span class="cn-word" data-pos="verb" data-tr="qiynadi, tinim bermadi">bothered</span> for two and a half years.</p>

<p>The bus is a 1998 <span class="cn-word" data-tr="dizel">diesel</span> with a hundred and one thousand kilometres on it. It is white, it is <span class="cn-word" data-pos="adj" data-tr="shovqinli">noisy</span>, and it has been carrying children along that road every school morning since March 2024, and old women to Denov on Fridays.</p>

<p>Her old teacher is seventy-one. In April she came to the school with a brown folder, found the paper, and read the last sentence out loud on the bus, standing between the <span class="cn-word" data-tr="oʻrindiqlar">seats</span>, while thirty children looked at the floor and said nothing at all.</p>

<p>"<strong>If I were you</strong>," she told them afterwards, "I <strong>would keep</strong> that piece of paper. Somebody in this bus is <span class="cn-word" data-pos="verb" data-tr="yozayotgan">writing</span> one now."</p>''',
        "questions": [
            {
                "text": "What happened to Nilufar's answer?",
                "choices": [
                    "She received a thousand dollars and bought a bus",
                    "She spent years working and pushing the neighbourhood committee until a real bus came in 2024",
                    "Her teacher bought the bus for the street",
                ],
                "answer": 1,
                "explanation": "Ming dollar hech qachon kelmadi. Bank, "
                               "oʻn bir yil ish va mahalla qoʻmitasi "
                               "bilan ikki yarim yillik urinish keldi — "
                               "avtobus 2024-yil martda yoʻlga chiqdi.",
            },
            {
                "text": "\"If I had a thousand dollars, I would buy a bus.\" The past form `had` shows:",
                "choices": [
                    "that it happened in the past",
                    "that the situation is imaginary — she does not have the money",
                    "that she will get the money soon",
                ],
                "answer": 1,
                "explanation": "Ikkinchi shartda oʻtgan zamon shakli "
                               "vaqtni emas, <b>xayoliylikni</b> "
                               "bildiradi: puli yoʻq, shuning uchun "
                               "avtobus ham yoʻq.",
            },
            {
                "text": "Which sentence talks about a REAL future possibility?",
                "choices": [
                    "If I had a scholarship, I would study in Tashkent.",
                    "If I get a scholarship, I will study in Tashkent.",
                    "If I were you, I would study in Tashkent.",
                ],
                "answer": 1,
                "explanation": "Haqiqiy ehtimol — birinchi shart: "
                               "<b>if + present → will</b>. Qolgan "
                               "ikkitasi xayoliy (ikkinchi shart).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-55 — third conditional  (nine minutes in 2011)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "If She Had Not Missed the Flight",
        "summary": (
            "PE-55 matni. 2011-yil, Toshkent aeroporti: toʻqqiz "
            "daqiqa. Oʻsha toʻqqiz daqiqa uchun u samolyotga "
            "kirmadi — va oʻn uch yildan keyin dissertatsiya himoyasida "
            "tirbandlikka rahmat aytdi."
        ),
        "order":   55,
        "grammar": [
            {
                "pattern":  "If + had + V3 → would have + V3",
                "meaning":  "Uchinchi shart — <b>oʻtgan zamon "
                            "haqiqatining teskarisi</b>. "
                            "<i><b>If</b> she <b>had not missed</b> the "
                            "flight, she <b>would never have met</b> "
                            "him</i>. Voqea allaqachon boʻlib "
                            "oʻtgan, oʻzgartirib boʻlmaydi — shuning "
                            "uchun bu afsus yoki (bu yerda) "
                            "minnatdorchilik tili.",
                "examples": ["If she had not missed that flight, she would never have met him.",
                             "If the road had been empty, she would have been at the gate at seven."],
            },
            {
                "pattern":  "could have / might have in the result",
                "meaning":  "Natija qismida <b>would have</b> oʻrniga "
                            "<b>could have</b> (imkoni boʻlar edi) yoki "
                            "<b>might have</b> (ehtimol) keladi: "
                            "<i>She <b>might have finished</b> her "
                            "studies in Ankara</i>. Maʼno kuchi "
                            "shu bilan pasayadi.",
                "examples": ["She could have taken a taxi from the bridge.",
                             "She might have given up that year."],
            },
            {
                "pattern":  "The three conditionals as one system",
                "meaning":  "<b>1</b>: <i>If it rains, I will stay</i> "
                            "(haqiqiy kelajak) · <b>2</b>: <i>If it "
                            "rained, I would stay</i> (xayoliy hozir) · "
                            "<b>3</b>: <i>If it <b>had rained</b>, I "
                            "<b>would have stayed</b></i> (oʻtgan "
                            "zamonning teskarisi). Har bir shakl bir "
                            "qadam orqaga suriladi — shuning uchun "
                            "uchinchisi eng “uzoq”.",
                "examples": ["If it rains, I will stay at home.",
                             "If it rained, I would stay at home.",
                             "If it had rained, I would have stayed at home."],
            },
        ],
        "body": '''<p>Kamola was twenty-three in the autumn of 2011, and she had one <span class="cn-word" data-tr="stipendiya">scholarship</span>, one suitcase and a Tashkent–Istanbul <span class="cn-word" data-tr="parvoz">flight</span> at ten past nine in the morning.</p>

<p>A water pipe had <span class="cn-word" data-pos="verb" data-tr="yorilgan edi">burst</span> under the road near the bridge that night. The taxi sat in one place for thirty-five minutes, and she watched the clock on the driver's <span class="cn-word" data-tr="asboblar paneli">dashboard</span> the whole time.</p>

<p>She reached the <span class="cn-word" data-tr="qabul stoli">check-in desk</span> nine minutes after it closed. Nine.</p>

<p>She has told me twice that she sat on the floor by the window, next to her suitcase, and cried in front of about two hundred people, and that a woman selling <span class="cn-word" data-tr="SIM kartalar">SIM cards</span> brought her tea and did not say anything at all.</p>

<p>The airline put her on the same flight the next morning, seat 14C.</p>

<p>In 14B there was a man of about sixty with a folder of <span class="cn-word" data-tr="jadvallar">tables</span> and numbers on his knees, and he was making <span class="cn-word" data-tr="tuzatishlar">corrections</span> with a red pen. Kamola looked at the folder for forty minutes, and somewhere over the Black Sea she asked him one question about a <span class="cn-word" data-tr="ustun">column</span> she did not understand.</p>

<p>He was a <span class="cn-word" data-tr="professor">professor</span> of <span class="cn-word" data-tr="suv resurslari">water resources</span> at a university in Ankara. They talked until the plane landed. He gave her a card, told her to write in November, and then <span class="cn-word" data-pos="verb" data-tr="unutdi">forgot</span> her completely, which she knew he would.</p>

<p>She wrote in November. She wrote again in February. In 2013 he became her <span class="cn-word" data-tr="ilmiy rahbar">supervisor</span>.</p>

<p><strong>If</strong> she <strong>had arrived</strong> nine minutes earlier, she <strong>would have flown</strong> to Istanbul on the Tuesday, in seat 8A, next to nobody. She <strong>would have finished</strong> her <span class="cn-word" data-tr="magistratura">master's</span>, come home, and taught in a school, and she <strong>might have been</strong> happy — she says that part herself, and she means it.</p>

<p>She <strong>could have taken</strong> the <span class="cn-word" data-tr="metro">metro</span> from the bridge that morning. She did not think of it. Nobody thinks of it at twenty-three, with a suitcase.</p>

<p>Her <span class="cn-word" data-tr="himoya">defence</span> was in June 2024, in Ankara, on water in the Amu Darya basin. She began the way nobody begins: "<strong>If</strong> a pipe under a road in Tashkent <strong>had not burst</strong> in 2011, none of you <strong>would have read</strong> this work."</p>''',
        "questions": [
            {
                "text": "Why does Kamola thank a burst water pipe?",
                "choices": [
                    "It made her miss her flight, and on the next day's plane she met the professor who became her supervisor",
                    "It stopped the taxi so she saved money",
                    "It happened at her university in Ankara",
                ],
                "answer": 0,
                "explanation": "Quvur yorilgani → tirbandlik → toʻqqiz "
                               "daqiqa kechikish → ertasi kungi "
                               "samolyot → 14B dagi professor → ilmiy "
                               "rahbar. Butun zanjir shu quvurdan "
                               "boshlanadi.",
            },
            {
                "text": "\"If she had arrived nine minutes earlier, she would have flown on the Tuesday.\" What is true?",
                "choices": [
                    "She arrived earlier and flew on Tuesday",
                    "She did not arrive earlier, and she did not fly on Tuesday",
                    "She may still fly on Tuesday",
                ],
                "answer": 1,
                "explanation": "Uchinchi shart har doim haqiqatning "
                               "teskarisi: kechikdi, demak seshanba "
                               "kungi parvozga ham chiqmadi.",
            },
            {
                "text": "Which sentence is a THIRD conditional?",
                "choices": [
                    "If it rains, I will stay at home.",
                    "If it rained, I would stay at home.",
                    "If it had rained, I would have stayed at home.",
                ],
                "answer": 2,
                "explanation": "Uchinchi shartning formulasi — "
                               "<b>if + had + V3 → would have + V3</b>. "
                               "Birinchisi haqiqiy kelajak, "
                               "ikkinchisi xayoliy hozir.",
            },
        ],
    },
]
