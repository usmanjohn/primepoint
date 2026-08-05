# -*- coding: utf-8 -*-
"""Prime English Readings — PE-66 … PE-70 (batch 14). The causative → precision.

PE-66 the causative (have / get something done) · PE-67 comparatives and superlatives ·
PE-68 as … as / too / enough · PE-69 quantifiers (some/any/much/many/a lot of) ·
PE-70 few vs a few, little vs a little.

Shapes:
  66 — a woman brings a smashed 2014 phone to a repair shop and refuses a new one; what
       is on it is worth more than the phone
  67 — two villages, one river and forty centimetres: the argument about whose bridge is
       the longest, settled with a rope
  68 — "she is too young to know what she wants" — and the one person in the family who
       says she is old enough is the one nobody asked at sixteen
  69 — a wedding kitchen, four cooks, one pot, and how much salt is too much salt
  70 — the difference between `few friends` and `a few friends`, told by a man who has
       been both

NARRATOR VOICE (see the toc's AUDIO section):
    66 en-US-JennyNeural · 67 en-US-GuyNeural · 68 en-US-JennyNeural
    69 en-US-GuyNeural   · 70 en-US-GuyNeural
Generate one story at a time:
    python manage.py gen_corner_audio --collection="Prime English Readings" \
        --only 67 --voice en-US-GuyNeural

Cumulative rule: PE-66 and PE-67 use NO `as … as` / `too` / `enough` (PE-68). PE-68 keeps
off the quantifier fine points (much/many is PE-69, few/a few/little/a little is PE-70),
and PE-69 keeps off few/a few/little/a little. Nothing from Block G (PE-83+): no
inversion, no cleft sentences, no participle clauses.
Length: 300–360 words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_66_70.py --author=prime
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
    # PE-66 — the causative  (the 2014 phone)                  [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "I Had My Phone Repaired",
        "summary": (
            "PE-66 matni. U singan telefonini taʼmirlashga olib bordi "
            "va yangisini olishdan bosh tortdi. Usta sababini "
            "tushunmadi — tushunganda esa hisobga bitta ishni "
            "yozmadi."
        ),
        "order":   66,
        "grammar": [
            {
                "pattern":  "have + something + V3",
                "meaning":  "Ishni <b>oʻzim qilmadim, qildirdim</b>: "
                            "<i>I <b>had</b> my phone <b>repaired</b></i> "
                            "— telefonni ustaga tuzattirdim. Soʻz "
                            "tartibi hamma narsani belgilaydi: "
                            "<b>have + obyekt + V3</b> "
                            "(<i>I had repaired my phone</i> esa "
                            "butunlay boshqa gap — past perfect).",
                "examples": ["I had the screen replaced.",
                             "She had the battery changed at the same time."],
            },
            {
                "pattern":  "get instead of have, in every tense",
                "meaning":  "Kundalik nutqda <b>get</b> ham xuddi "
                            "shunday ishlaydi: <i>I <b>got</b> the "
                            "photographs <b>copied</b></i>. Formula "
                            "har qanday zamonda yashaydi: "
                            "<i>I <b>am having</b> it done</i>, "
                            "<i>I <b>will have</b> it done</i>, "
                            "<i>I <b>have had</b> it done twice</i>.",
                "examples": ["I am having the messages copied this week.",
                             "She has had that phone repaired three times."],
            },
            {
                "pattern":  "The second meaning: something bad happened to you",
                "meaning":  "Xuddi shu shakl <b>boshingizga tushgan "
                            "ish</b>ni ham bildiradi: <i>He <b>had</b> "
                            "his bag <b>stolen</b></i> — sumkasini "
                            "oʻgʻirlab ketdilar. Bunda hech qanday "
                            "“qildirish” yoʻq. Odamni ishga "
                            "koʻndirish esa <b>have / get somebody "
                            "to do</b>: <i>I <b>got</b> my son <b>to "
                            "write</b> it down</i>.",
                "examples": ["She had her phone knocked out of her hand on a bus.",
                             "I got my son to write the numbers down for me."],
            },
        ],
        "body": '''<p>A woman came into the repair shop under our block in March with a phone from about 2014, in two pieces, in a plastic bag.</p>

<p>The <span class="cn-word" data-tr="ekran">screen</span> was in <span class="cn-word" data-tr="boʻlaklar">pieces</span> — she <strong>had had</strong> it <strong>knocked</strong> out of her hand on a bus near Chorsu. She wanted the screen <strong>replaced</strong> and the <span class="cn-word" data-tr="batareya">battery</span> <strong>changed</strong>, and she asked what the whole thing would cost.</p>

<p>My cousin Timur, who has been repairing phones there for nine years, told her the truth: the <span class="cn-word" data-tr="qismlar, detallar">parts</span> for that model are hard to find, the repair would cost more than the phone, and for that money she could buy a working <span class="cn-word" data-pos="adj" data-tr="ishlatilgan">second-hand</span> one that afternoon with a <span class="cn-word" data-tr="kafolat">guarantee</span>.</p>

<p>She said no. He explained it again, in a different order, the way men do when they think somebody has not understood the numbers.</p>

<p>She let him finish and then she said: "There are forty-one <span class="cn-word" data-tr="ovozli xabarlar">voice messages</span> from my mother on that phone. She died in 2021. I do not know how to get them off it, and I have been afraid to give it to anybody."</p>

<p>Timur is not a <span class="cn-word" data-pos="adj" data-tr="hissiyotli">sentimental</span> man. He <span class="cn-word" data-pos="verb" data-tr="tuzatdi, almashtirdi">replaced</span> the screen in forty minutes and put in a new battery. Then he asked her to sit down and <strong>got</strong> her <strong>to unlock</strong> it, and he spent an hour and a half on something she had not asked for.</p>

<p>He <strong>had</strong> all forty-one files <strong>copied</strong> onto a memory card, and then onto a second card, and then he uploaded them to an account he made for her while she watched, and he wrote the <span class="cn-word" data-tr="parol">password</span> on a card in <span class="cn-word" data-pos="adj" data-tr="yirik">large</span> letters because she is sixty-four.</p>

<p>She paid for the screen and the battery. That is all that was on the paper.</p>

<p>She came back in April with a bag of <span class="cn-word" data-tr="somsa">somsa</span> for the whole shop, and now she comes about every two months for no reason at all, and Timur <span class="cn-word" data-pos="verb" data-tr="shikoyat qiladi">complains</span> about it to everybody, and he has never once told her not to come.</p>

<p>She still uses that phone. She <strong>had</strong> the <span class="cn-word" data-tr="tugmalar">buttons</span> <strong>cleaned</strong> in June, and she <strong>is having</strong> a <span class="cn-word" data-tr="chexol">case</span> <strong>made</strong> for it by a man in the market who works with leather, because she is not going to be on a bus with it in her hand again.</p>''',
        "questions": [
            {
                "text": "Why did the woman refuse a working second-hand phone?",
                "choices": [
                    "It was more expensive than the repair",
                    "Her mother's forty-one voice messages were on the old phone and she did not know how to move them",
                    "She did not trust the guarantee",
                ],
                "answer": 1,
                "explanation": "Telefonda 2021-yilda vafot etgan onasining "
                               "41 ta ovozli xabari bor edi, va u ularni "
                               "koʻchirishni bilmagan.",
            },
            {
                "text": "\"She had the battery changed.\" Who changed it?",
                "choices": [
                    "She did it herself",
                    "Somebody else did it — she arranged it",
                    "Nobody changed it",
                ],
                "answer": 1,
                "explanation": "<b>have + obyekt + V3</b> — ishni "
                               "boshqa odam bajaradi, gapiruvchi esa "
                               "uni tashkil qiladi.",
            },
            {
                "text": "Which sentence means somebody knocked her phone out of her hand?",
                "choices": [
                    "She had knocked her phone out of her hand.",
                    "She had her phone knocked out of her hand.",
                    "She has knocked out her phone.",
                ],
                "answer": 1,
                "explanation": "Xuddi shu shakl (<b>have + obyekt + "
                               "V3</b>) boshiga tushgan ishni ham "
                               "bildiradi. Soʻz tartibi oʻzgarsa, "
                               "maʼno ham oʻzgaradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-67 — comparatives & superlatives  (forty centimetres)   [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Longest Bridge in the Region",
        "summary": (
            "PE-67 matni. Ikki qishloq oʻn yildan beri tortishadi: "
            "qaysi birining koʻprigi uzunroq? 2018-yilda ular arqon "
            "olib, oʻlchashga qaror qildilar. Farqi qirq santimetr "
            "chiqdi — va yutqazgan qishloq eng yaxshi javobni topdi."
        ),
        "order":   67,
        "grammar": [
            {
                "pattern":  "Where the border runs",
                "meaning":  "Bir boʻgʻinli soʻz — <b>-er / -est</b> "
                            "(<i>long → longer → the longest</i>), "
                            "uch va undan koʻp boʻgʻinli — "
                            "<b>more / the most</b> (<i>expensive → "
                            "more expensive</i>). Ikki boʻgʻinli: "
                            "<i>-y</i> bilan tugasa <b>-ier</b> "
                            "(<i>busy → busier</i>), qolganlari "
                            "koʻpincha <b>more</b>.",
                "examples": ["Our bridge is longer than theirs.",
                             "It is the longest bridge in the region.",
                             "Their tea is more expensive than ours."],
            },
            {
                "pattern":  "The five irregulars, and than / the",
                "meaning":  "<i>good → better → the best</i> · "
                            "<i>bad → worse → the worst</i> · "
                            "<i>far → further → the furthest</i> · "
                            "<i>many → more → the most</i> · "
                            "<i>little → less → the least</i>. "
                            "Qiyoslashda <b>than</b>, eng yuqori "
                            "darajada esa <b>the</b> — "
                            "<i>the second longest</i> ham shunday.",
                "examples": ["Their tea is better than ours.",
                             "That was the worst summer for the river."],
            },
            {
                "pattern":  "Stronger and weaker comparisons",
                "meaning":  "Kuchaytirish: <b>much / far / a lot</b> "
                            "+ comparative (<i><b>much</b> longer</i>, "
                            "<i><b>far</b> better</i>). Yumshatish: "
                            "<b>a bit / slightly / a little</b> "
                            "(<i><b>slightly</b> shorter</i>). "
                            "Ikki chiroyli qolip: "
                            "<i><b>the more</b> they argued, "
                            "<b>the louder</b> it got</i> va "
                            "<i>it got <b>longer and longer</b></i>.",
                "examples": ["Their bridge is only slightly longer.",
                             "The more they argued, the longer both bridges got."],
            },
        ],
        "body": '''<p>There are two villages on our part of the river, and between them there is an argument that is older than my father.</p>

<p>Both of them have a bridge. Both of them say that theirs is <strong>the longest</strong> bridge in the region.</p>

<p>Ours <strong>was built</strong> in 1957 and it carries a road. Theirs is a <span class="cn-word" data-tr="piyodalar koʻprigi">footbridge</span> from the 1970s on two concrete <span class="cn-word" data-tr="ustunlar, tayanchlar">piers</span>, and it goes across at a wider, <span class="cn-word" data-pos="adj" data-tr="sekinroq">slower</span> place.</p>

<p>For about thirty years the two numbers got <strong>bigger and bigger</strong>. In 1994 ours was thirty-one metres. By 2005 men at our tea-house were saying thirty-four. Their side went from thirty-two to thirty-eight in the same period, and one of them once said forty in front of eleven witnesses. <strong>The more</strong> they argued, <strong>the longer</strong> both bridges got.</p>

<p>In August 2018 a <span class="cn-word" data-tr="kadastr, yer oʻlchov">land survey</span> was done in the district for a new gas <span class="cn-word" data-tr="quvur">pipe</span>, and two young men with a <span class="cn-word" data-tr="lazerli oʻlchov asbobi">laser measure</span> came through both villages in one week. That was <span class="cn-word" data-pos="adj" data-tr="bardosh berolmaydigan">unbearable</span>. Somebody had to know before they did.</p>

<p>So on a Sunday morning about twenty men from our village walked down to the water with a <span class="cn-word" data-tr="arqon">rope</span> and a <span class="cn-word" data-tr="oʻlchov lentasi">tape measure</span>, and about the same number came down from theirs, and they measured both bridges together, twice, from the concrete at one end to the concrete at the other.</p>

<p>Ours: 31 metres 20.</p>

<p>Theirs: 31 metres 60.</p>

<p>Forty centimetres. Thirty years of argument, and the difference was <strong>shorter</strong> than a man's arm.</p>

<p>Their side was <span class="cn-word" data-pos="adj" data-tr="nihoyatda xursand">delighted</span>, and they were <strong>the loudest</strong> people in the district for about a month. Then, in September, our tea-house <span class="cn-word" data-pos="verb" data-tr="oʻrnatdi">put up</span> a board by the road, painted blue, with white letters, and it is still there:</p>

<p><i><strong>THE SECOND LONGEST</strong> BRIDGE IN THE REGION — <strong>THE BEST</strong> TEA.</i></p>

<p>It is now the most photographed object in either village. Their footbridge is <strong>slightly longer</strong>, ours is <strong>much busier</strong>, and on Saturdays about half the cars that stop at that board belong to people from the other side of the river, who come for the tea and pretend they are just passing.</p>''',
        "questions": [
            {
                "text": "How was the argument settled?",
                "choices": [
                    "The two villages measured both bridges together, and the difference was forty centimetres",
                    "The gas company published the numbers",
                    "Nobody ever measured them",
                ],
                "answer": 0,
                "explanation": "2018-yil avgustda ikki qishloq odamlari "
                               "arqon va oʻlchov lentasi bilan birga "
                               "oʻlchadilar: 31,20 va 31,60 metr.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "Their bridge is more long than ours.",
                    "Their bridge is longer than ours.",
                    "Their bridge is longer that ours.",
                ],
                "answer": 1,
                "explanation": "Bir boʻgʻinli soʻz <b>-er</b> oladi "
                               "(<i>more long</i> ✗), va qiyoslash "
                               "soʻzi <b>than</b> — <i>that</i> emas.",
            },
            {
                "text": "\"Their bridge is only slightly longer\" means the difference is:",
                "choices": [
                    "very big",
                    "very small",
                    "impossible to measure",
                ],
                "answer": 1,
                "explanation": "<b>slightly</b> qiyoslashni "
                               "yumshatadi — farq juda kichik "
                               "(bu yerda 40 sm). Kuchaytirish uchun "
                               "<b>much</b> yoki <b>far</b> ishlatilar edi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-68 — as … as / too / enough  (old enough)             [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Old Enough to Decide",
        "summary": (
            "PE-68 matni. “U hali juda yosh, nima xohlayotganini "
            "bilmaydi”, dedi hamma. Uni katta deb aytgan yagona odam "
            "— oʻn olti yoshida hech kim soʻramagan buvisi edi."
        ),
        "order":   68,
        "grammar": [
            {
                "pattern":  "as … as — they are equal",
                "meaning":  "<b>as + sifat + as</b> — teng: "
                            "<i>She is <b>as stubborn as</b> I was</i>. "
                            "Inkori — <b>not as / not so … as</b>: "
                            "<i>The college is <b>not as far as</b> "
                            "they say</i>. Miqdor uchun ham "
                            "ishlaydi: <b>as much as</b>, "
                            "<b>as many as</b>.",
                "examples": ["She is as stubborn as her grandmother was.",
                             "It is not as far as everybody says."],
            },
            {
                "pattern":  "too = more than you want",
                "meaning":  "<b>too</b> + sifat — meʼyordan "
                            "ortiq, salbiy maʼno: <i>She is "
                            "<b>too young</b></i>. Diqqat: "
                            "<i>too</i> hech qachon “juda ham "
                            "yaxshi” maʼnosida ishlatilmaydi — "
                            "buning uchun <b>very</b> bor. "
                            "<i>She is too clever</i> = "
                            "aqli ortiqcha (muammo).",
                "examples": ["Seventeen is too young, they said.",
                             "The bus was too full to get on."],
            },
            {
                "pattern":  "enough — just the right amount",
                "meaning":  "Sifatdan <b>keyin</b>, otdan "
                            "<b>oldin</b>: <i>old <b>enough</b></i>, "
                            "lekin <i><b>enough</b> money</i>. "
                            "Qoliplar: <b>too … to</b> "
                            "(<i>too young to decide</i>) va "
                            "<b>… enough to</b> (<i>old enough to "
                            "decide</i>) — bir xil fikrni ikki "
                            "tomondan aytadi.",
                "examples": ["She is old enough to decide.",
                             "There was not enough time to argue."],
            },
        ],
        "body": '''<p>In the spring of her last school year, Kamila told the family at the table that she was going to the medical college in Andijon, four hundred kilometres away, and that she had already sent the papers.</p>

<p>The table said what tables say. She was <strong>too young</strong>. It was <strong>too far</strong>. There was <strong>not enough</strong> money for a room. Her mother said, quietly, that a girl of seventeen does not know what she wants, and that in two years she would want something else.</p>

<p>Her uncle said that the college in our own city is <strong>not as bad as</strong> people think, which is true, and that it is <strong>not as far as</strong> Andijon, which is <span class="cn-word" data-pos="adj" data-tr="ravshan">obvious</span>.</p>

<p>Kamila did not <span class="cn-word" data-pos="verb" data-tr="baqirmadi">shout</span>. She had come with a <span class="cn-word" data-tr="papka">folder</span>: the <span class="cn-word" data-tr="hujjatlar roʻyxati">list of documents</span>, the <span class="cn-word" data-tr="yotoqxona">hostel</span> price, the <span class="cn-word" data-tr="avtobus jadvali">bus timetable</span>, and a page of her own arithmetic in two <span class="cn-word" data-tr="ustunlar">columns</span>. She is <strong>as stubborn as</strong> a gate.</p>

<p>My grandmother was at the end of the table and she had not said anything at all. She is seventy-nine. She cannot read, and she was married in the spring of 1962, at sixteen, to a man she had met twice.</p>

<p>She put her hand flat on the table, which in our family means the same thing as a <span class="cn-word" data-tr="sudya">judge</span> and a <span class="cn-word" data-tr="bolgʻacha">hammer</span>.</p>

<p>"She is <strong>old enough</strong>," she said.</p>

<p>Her son started to say something about money and she did not let him finish.</p>

<p>"I was <strong>not as old as</strong> she is now," she said. "Nobody at this table asked me one question. Not one. They asked my father, and my father was <strong>too tired</strong> to argue with anybody that year, and I stood in the kitchen and heard the whole thing through the door."</p>

<p>Then she said the sentence that ended it. "I have had fifty-seven years to decide whether I was <strong>old enough</strong>. She has a folder. Give her the money."</p>

<p>Kamila went to Andijon in September 2021. The room was <strong>too cold</strong> in January and the food was <strong>not as good as</strong> home, and she came back for two weeks in February with a <span class="cn-word" data-tr="yoʻtal">cough</span> and did not complain once, in <span class="cn-word" data-tr="asosan">the main</span> because she is stubborn.</p>

<p>She is in her fourth year now. She has <strong>enough money</strong> from a scholarship, and she telephones my grandmother every Sunday and describes the <span class="cn-word" data-tr="kasalxona">hospital</span> to her, slowly, in <span class="cn-word" data-tr="tafsilotlar">detail</span>, because that is the only payment my grandmother will take.</p>''',
        "questions": [
            {
                "text": "Why did the grandmother support Kamila?",
                "choices": [
                    "Because she had money to give her",
                    "Because at sixteen nobody had asked her one question about her own life",
                    "Because the college in Andijon is cheaper",
                ],
                "answer": 1,
                "explanation": "1962-yilda uni hech kim soʻramagan — "
                               "otasidan soʻrashgan. U buni butun "
                               "umr eslab yurdi.",
            },
            {
                "text": "\"She is old enough to decide.\" Where does `enough` go?",
                "choices": [
                    "after the adjective, but before a noun",
                    "always before the adjective",
                    "always at the end of the sentence",
                ],
                "answer": 0,
                "explanation": "Sifatdan keyin — <i>old <b>enough</b></i>; "
                               "otdan oldin — <i><b>enough</b> money</i>. "
                               "<i>enough old</i> ✗.",
            },
            {
                "text": "Which sentence says the two things are equal?",
                "choices": [
                    "Andijon is too far.",
                    "The food was not as good as home.",
                    "She is as stubborn as a gate.",
                ],
                "answer": 2,
                "explanation": "<b>as … as</b> — tenglik. "
                               "<i>not as good as</i> tenglikni rad "
                               "etadi, <i>too far</i> esa meʼyordan "
                               "ortiqligini aytadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-69 — quantifiers  (four cooks, one pot)                 [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Too Much Salt, Too Many Cooks",
        "summary": (
            "PE-69 matni. Toʻyda toʻrt kishi bitta qozonga tuz "
            "soldi — har biri boshqasi solmagan deb oʻyladi. "
            "Osh yaramaydi, mehmonlar bir soatda keladi, va "
            "buvim faqat bitta savol beradi."
        ),
        "order":   69,
        "grammar": [
            {
                "pattern":  "some / any, and the offer exception",
                "meaning":  "<b>some</b> — tasdiqda, <b>any</b> — "
                            "inkor va savolda: <i>We have <b>some</b> "
                            "rice</i> · <i>There isn't <b>any</b> "
                            "salt left</i> · <i>Is there <b>any</b> "
                            "yoghurt?</i>. Istisno — taklif va "
                            "iltimos: <i>Would you like <b>some</b> "
                            "tea?</i>, <i>Can I have <b>some</b> "
                            "water?</i>",
                "examples": ["There isn't any salt left in the bag.",
                             "Would you like some tea while we fix it?"],
            },
            {
                "pattern":  "much / many / a lot of",
                "meaning":  "<b>many</b> — sanaladigan "
                            "(<i>many cooks</i>), <b>much</b> — "
                            "sanalmaydigan (<i>much salt</i>). "
                            "<b>much</b> va <b>many</b> asosan "
                            "inkor va savolda yashaydi; tasdiqda "
                            "<b>a lot of / lots of / plenty of</b> "
                            "tabiiyroq: <i>We put <b>a lot of</b> "
                            "salt in</i> — <i>much salt</i> emas.",
                "examples": ["How much salt did you put in?",
                             "There were a lot of people in that kitchen."],
            },
            {
                "pattern":  "too much / too many, and no",
                "meaning":  "<b>too much</b> + sanalmaydigan, "
                            "<b>too many</b> + sanaladigan: "
                            "<i><b>too much</b> salt</i>, "
                            "<i><b>too many</b> cooks</i>. "
                            "<b>no</b> + ot = <b>not any</b>: "
                            "<i>There was <b>no</b> time</i> = "
                            "<i>there wasn't <b>any</b> time</i>.",
                "examples": ["Too much salt and too many cooks.",
                             "There was no time to start again."],
            },
        ],
        "body": '''<p>My cousin's wedding, September, two hundred and ten guests, and one <span class="cn-word" data-tr="qozon">cauldron</span> of plov standing over the fire in the yard at half past ten in the morning.</p>

<p>There were four men round that fire. This is the whole problem in one sentence.</p>

<p>Ravshan aka had put the salt in at nine. Then my uncle came out, looked at the rice, and put in <strong>some</strong> more, because he has been putting salt in that cauldron since 1998 and nobody told him not to. Then a <span class="cn-word" data-tr="qoʻshni">neighbour</span> arrived with the meat and added <strong>a lot of</strong> salt "for the meat". Then a fourth man, who I still cannot <span class="cn-word" data-pos="verb" data-tr="aniqlay">identify</span>, went past with a <span class="cn-word" data-tr="qoshiq, choʻmich">ladle</span>.</p>

<p>Nobody asked <strong>any</strong> questions, because in a wedding yard everybody thinks somebody else knows.</p>

<p>At eleven Ravshan aka tasted it and went completely quiet, which <span class="cn-word" data-pos="verb" data-tr="qoʻrqitdi">frightened</span> everybody <strong>much</strong> more than shouting.</p>

<p>There was <strong>too much</strong> salt in twelve kilos of rice. There was <strong>no</strong> time to start again — the guests were coming at one — and there wasn't <strong>any</strong> rice left in the house, and the shop at the corner had <strong>plenty of</strong> sugar and <strong>not many</strong> other things on a Sunday.</p>

<p>My grandmother came out with her <span class="cn-word" data-tr="yenglar">sleeves</span> already up and asked one question: "How <strong>many</strong> of you put salt in?"</p>

<p>Four hands went up, slowly, in the way that men's hands go up when they are about to be told something by a woman of seventy-nine.</p>

<p>"<strong>Too many</strong> cooks," she said. "Bring me six <span class="cn-word" data-tr="kartoshka">potatoes</span>, <strong>a lot of</strong> water and the big <span class="cn-word" data-tr="choyshab, doka">cloth</span>."</p>

<p>She cut the potatoes in half, <span class="cn-word" data-pos="verb" data-tr="koʻmdi">buried</span> them in the rice, put the wet cloth over the top and made everybody leave the fire alone for forty minutes. Potatoes take up salt. It is not <span class="cn-word" data-tr="jodu">magic</span> and it does not fix everything, and it fixed <strong>enough</strong> of that plov.</p>

<p>Two hundred and ten people ate it. Eleven of them said it was the best plov they had eaten that year, which tells you something about weddings.</p>

<p>There is a rule in our yard now, and my grandmother says it before every big cooking day, the same six words: <i>one pot, one hand, no <span class="cn-word" data-tr="yordamchilar">helpers</span></i>. The four men still argue about who put in the third lot of salt, and none of them has ever <span class="cn-word" data-pos="verb" data-tr="tan olmadi">admitted</span> anything.</p>''',
        "questions": [
            {
                "text": "How was the plov saved?",
                "choices": [
                    "They cooked more rice",
                    "The grandmother buried six halved potatoes in the rice to take up the salt",
                    "They added sugar from the shop",
                ],
                "answer": 1,
                "explanation": "Kartoshka tuzni tortib oladi. Buvisi "
                               "oltita kartoshkani yarimlab, guruch "
                               "ichiga koʻmib, ustiga hoʻl mato "
                               "yopdi.",
            },
            {
                "text": "Which pair is correct?",
                "choices": [
                    "too many salt / too much cooks",
                    "too much salt / too many cooks",
                    "too much salt / too much cooks",
                ],
                "answer": 1,
                "explanation": "<b>much</b> — sanalmaydigan "
                               "(tuz), <b>many</b> — sanaladigan "
                               "(oshpazlar).",
            },
            {
                "text": "Which sentence uses `some` correctly?",
                "choices": [
                    "There wasn't some rice left in the house.",
                    "Would you like some tea while we fix it?",
                    "Did they put some salt in? — no, they didn't put any.",
                ],
                "answer": 1,
                "explanation": "Inkorda <b>any</b> ishlatiladi, lekin "
                               "taklifda <b>some</b> — "
                               "<i>Would you like some…?</i> Bu "
                               "qoidaning asosiy istisnosi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-70 — few / a few / little / a little  (one letter)      [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "A Little Money, A Few Friends",
        "summary": (
            "PE-70 matni. 2016-yilda u Toshkentga toʻrt yuz ming soʻm "
            "va ikkita telefon raqami bilan keldi. Toʻqqiz yildan "
            "keyin uning gapida faqat bitta harf oʻzgardi — "
            "va oʻsha harf hammasini aytadi."
        ),
        "order":   70,
        "grammar": [
            {
                "pattern":  "The grid: four words, two ideas",
                "meaning":  "Sanaladigan: <b>few</b> (deyarli "
                            "yoʻq, salbiy) — <b>a few</b> (bir "
                            "nechta, yetarli). Sanalmaydigan: "
                            "<b>little</b> (deyarli yoʻq) — "
                            "<b>a little</b> (ozgina, bor). "
                            "Bitta <b>a</b> harfi maʼnoni "
                            "teskarisiga oʻgiradi.",
                "examples": ["I had few friends in that city.",
                             "I have a few friends there now.",
                             "There was little money and little time."],
            },
            {
                "pattern":  "Making it stronger, and quite a few",
                "meaning":  "Kuchaytirish: <b>very few</b>, "
                            "<b>very little</b> (<i>very little "
                            "money</i>). Ajablanadigan qolip — "
                            "<b>quite a few</b> “ancha koʻp” "
                            "degani, “kam” emas: <i>I have "
                            "<b>quite a few</b> workers now</i>. "
                            "Javob sifatida yolgʻiz ham ishlaydi: "
                            "“How many?” — “<b>A few</b>.”",
                "examples": ["There was very little work that winter.",
                             "Quite a few of them are still with me."],
            },
            {
                "pattern":  "Countable or not — check the noun first",
                "meaning":  "<b>few / a few</b> + koʻplik "
                            "(<i>friends</i>, <i>machines</i>, "
                            "<i>days</i>) · <b>little / a little</b> "
                            "+ sanalmaydigan (<i>money</i>, "
                            "<i>time</i>, <i>work</i>, <i>bread</i>). "
                            "Shuning uchun <i>a few money</i> ✗ va "
                            "<i>a little friends</i> ✗.",
                "examples": ["a few machines, a few days",
                             "a little money, a little time"],
            },
        ],
        "body": '''<p>Otabek came to Tashkent from a village near Kosonsoy in March 2016 with four hundred thousand soʻm, one bag, and two telephone numbers written on the back of a <span class="cn-word" data-tr="ariza blankasi">form</span>.</p>

<p>He describes that spring in one sentence, and he chooses the words carefully, because he is the kind of man who chooses words carefully.</p>

<p>"I had <strong>little</strong> money and <strong>few</strong> friends."</p>

<p>Not <i>a little</i>. Not <i>a few</i>. The first number he called did not <span class="cn-word" data-pos="verb" data-tr="javob bermadi">answer</span> in three days. The second one belonged to a man who had left for Russia in January. He slept in a room with five other men above a <span class="cn-word" data-tr="avtomobil ustaxonasi">car workshop</span> in Sergeli and paid by the week, and in the second month he had <strong>very little</strong> work and he ate bread and <span class="cn-word" data-tr="pomidor pastasi">tomato paste</span> for eleven days, which he mentions the way other people mention the weather.</p>

<p>He can <span class="cn-word" data-pos="verb" data-tr="payvandlaydi">weld</span>. That is the whole reason this story does not end there.</p>

<p>A man from the workshop below <span class="cn-word" data-pos="verb" data-tr="soʻradi">asked</span> him to fix a <span class="cn-word" data-tr="darvoza">gate</span> in April for <span class="cn-word" data-tr="haq, toʻlov">payment</span> in food. He did it in one evening and did it properly, and the neighbour of that man had a <span class="cn-word" data-tr="soyabon, navis">canopy</span> that needed <span class="cn-word" data-pos="verb" data-tr="taʼmirlash">mending</span>, and that is how work moves in this city: sideways, one gate at a time.</p>

<p>He has a workshop of his own in Yangihayot now. It is not big. There are three <span class="cn-word" data-tr="payvand apparatlari">welding machines</span>, a <span class="cn-word" data-tr="kran, koʻtargich">hoist</span> he bought <span class="cn-word" data-pos="adj" data-tr="ishlatilgan">used</span> in 2022, and a sign he made himself and hung <span class="cn-word" data-pos="adj" data-tr="qiyshiq">crooked</span> on purpose, because a straight sign, he says, looks like somebody else made it.</p>

<p><strong>Quite a few</strong> men have worked for him — eleven or twelve — and four of them are still there. Two of them came from his own district with numbers written on paper, and he answered his phone both times, on the first day, within an hour.</p>

<p>Last winter he was <span class="cn-word" data-pos="verb" data-tr="soʻroq qilindi">interviewed</span> for about six minutes on a local radio programme about small businesses, and the woman asked him how he had started.</p>

<p>He said the same sentence he always says, and then he said the other one, and you can hear him stop for a second in the middle of it, because he was working out whether he had earned it yet.</p>

<p>"In 2016 I had <strong>little</strong> money and <strong>few</strong> friends. Now I have <strong>a little</strong> money and <strong>a few</strong> friends. In English that is one letter. It took me nine years."</p>''',
        "questions": [
            {
                "text": "What is the difference between his two sentences?",
                "choices": [
                    "The first means he had almost nothing; the second means he has some — and that is the whole story",
                    "The second sentence means he is now rich",
                    "There is no real difference",
                ],
                "answer": 0,
                "explanation": "<i>little / few</i> — deyarli yoʻq; "
                               "<i>a little / a few</i> — ozgina bor. "
                               "Bitta <b>a</b> harfi toʻqqiz yillik "
                               "mehnatni ifodalaydi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "I had a few money and a little friends.",
                    "I had a little money and a few friends.",
                    "I had few money and little friends.",
                ],
                "answer": 1,
                "explanation": "<b>a little</b> + sanalmaydigan "
                               "(<i>money</i>), <b>a few</b> + "
                               "koʻplik (<i>friends</i>). Otni "
                               "birinchi tekshiriladi.",
            },
            {
                "text": "\"Quite a few men have worked for him\" means:",
                "choices": [
                    "almost nobody has worked for him",
                    "a fairly large number of men have worked for him",
                    "exactly four men have worked for him",
                ],
                "answer": 1,
                "explanation": "<b>quite a few</b> — “ancha koʻp”. "
                               "Shakli “kam” degandek koʻrinadi, "
                               "maʼnosi esa teskari — bu tilning "
                               "eng ayyor qoliplaridan biri.",
            },
        ],
    },
]
