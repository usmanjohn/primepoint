# -*- coding: utf-8 -*-
"""Prime English Readings — PE-71 … PE-75 (batch 15). Precision: the small words.

PE-71 each / every / both / either / neither / all · PE-72 word order (SVOMPT) ·
PE-73 question tags · PE-74 subject–verb agreement · PE-75 possession ('s, s', of).

Shapes:
  71 — two brothers, one wall and a village elder's single question, which neither of
       them will answer
  72 — a hand-painted shop sign with the words in the wrong order, and the son who grew
       up to teach word order for a living
  73 — a grandmother's Sunday tag question, and the week she stopped asking it
  74 — March 2020: "the news is not good", and what a guesthouse family did with the year
  75 — a brass plate for a school room, and one apostrophe in the wrong place

NARRATOR VOICE (see the toc's AUDIO section):
    71 en-US-GuyNeural   · 72 en-US-GuyNeural · 73 en-US-JennyNeural
    74 en-US-JennyNeural · 75 en-US-GuyNeural
Generate one story at a time:
    python manage.py gen_corner_audio --collection="Prime English Readings" \
        --only 71 --voice en-US-GuyNeural

Cumulative rule: everything through PE-70 is now free (including comparison, `as … as`,
too/enough — the toc's third standing exception expired at PE-67/68). Still ahead, so
still forbidden: verb/adjective + preposition drills and phrasal verbs as a *subject*
(PE-76…78 — ordinary phrasal verbs in narration are fine), the advanced article cases
(PE-80), and all of Block G (PE-83+): emphatic `do`, inversion, cleft sentences,
participle clauses.
Length: 300–360 words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_71_75.py --author=prime
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
    # PE-71 — each / every / both / neither / all   (the wall)     [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Both Brothers, Neither Answer",
        "summary": (
            "PE-71 matni. Ikki aka-uka devor ustida yetti oy "
            "tortishdi. Oqsoqol ularga bittagina savol berdi — "
            "va ikkisi ham javob bermadi. Aynan shu javobsizlik "
            "hammasini hal qildi."
        ),
        "order":   71,
        "grammar": [
            {
                "pattern":  "every / each — singular, always",
                "meaning":  "<b>every</b> — butun guruhga birga "
                            "qaraydi, <b>each</b> — bittalab. "
                            "Ikkisidan keyin ham <b>birlik</b>: "
                            "<i><b>Every</b> man in that yard "
                            "<b>knew</b></i>, <i><b>Each</b> of them "
                            "<b>was</b> asked one question</i> "
                            "(<i>every men</i> ✗, <i>each of them "
                            "were</i> ✗).",
                "examples": ["Every man in the yard knew the answer.",
                             "Each of them was asked the same question."],
            },
            {
                "pattern":  "both / either / neither — the words for two",
                "meaning":  "<b>both</b> — ikkisi ham "
                            "(koʻplik feʼl): <i><b>Both</b> brothers "
                            "<b>were</b> silent</i>. <b>either</b> — "
                            "ikkisidan biri, <b>neither</b> — "
                            "ikkisi ham emas, va ikkisi ham "
                            "<b>birlik</b> feʼl oladi: "
                            "<i><b>Neither</b> brother <b>said</b> "
                            "a word</i>. <b>neither</b> ichida inkor "
                            "bor — <i>didn't</i> qoʻshilmaydi.",
                "examples": ["Both brothers were in the yard.",
                             "Neither of them answered.",
                             "Either answer would have cost him something."],
            },
            {
                "pattern":  "all, and the -body words",
                "meaning":  "<b>all</b> + koʻplik yoki "
                            "sanalmaydigan (<i><b>all</b> the "
                            "neighbours</i>, <i><b>all</b> the "
                            "land</i>) va feʼldan oldin ham keladi: "
                            "<i>They <b>all</b> stood up</i>. "
                            "<b>everybody / nobody / somebody</b> "
                            "esa <b>birlik</b>: <i><b>Nobody</b> "
                            "<b>was</b> surprised</i>.",
                "examples": ["All the neighbours came out.",
                             "Nobody was surprised by the ruling."],
            },
        ],
        "body": '''<p>The wall between Anvar and Tolib runs down the middle of a <span class="cn-word" data-tr="tomorqa">plot</span> of land behind their houses, and it has been in the wrong place since 1974.</p>

<p><strong>Both</strong> brothers know this. That is what makes the story worth telling.</p>

<p>They argued about it for seven months. The <span class="cn-word" data-tr="yigʻin, majlis">meeting</span> in the mahalla office in February was the third one, and by then <strong>every</strong> family on that street had an opinion, and <strong>all</strong> the neighbours came out to watch the two of them walk in.</p>

<p>Hamid aka, who is eighty-four and has been the <span class="cn-word" data-tr="oqsoqol">elder</span> of that street since 2001, let them talk for twenty minutes. <strong>Each</strong> of them said the same thing in a different order: the wall is two metres inside my land.</p>

<p>Then he asked one question, and he asked it once.</p>

<p>"<strong>Both</strong> of you were boys in 1974. Who built that wall?"</p>

<p><strong>Neither</strong> of them answered.</p>

<p>The room waited. Anvar looked at the table. Tolib looked at the window. <strong>Nobody</strong> in that office was <span class="cn-word" data-pos="adj" data-tr="hayron">surprised</span>, because <strong>every</strong> man over sixty in the room already knew the answer, and the answer was their father.</p>

<p>He built it in the summer he came back from the army, by himself, in three weeks, and he built it two metres out of line because he had no <span class="cn-word" data-tr="oʻlchov, ip">line</span> and a <span class="cn-word" data-tr="yomon koʻz, koʻzi xira">bad eye</span>. <strong>Either</strong> brother could have said his name in one second, and <strong>either</strong> answer would have won him the land.</p>

<p><strong>Neither</strong> of them was going to do it in front of forty people.</p>

<p>Hamid aka waited until the silence became <span class="cn-word" data-pos="adj" data-tr="noqulay">uncomfortable</span> and then he made his <span class="cn-word" data-tr="qaror, hukm">ruling</span>, and it took eleven words: the wall stays, <strong>each</strong> of them pays half of a new gate in it, and the gate is never locked.</p>

<p>The gate was hung in April. It is <span class="cn-word" data-pos="adj" data-tr="oddiy">plain</span>, it is grey, and it has no lock on it at all.</p>

<p><strong>Both</strong> families use it every day. <strong>Neither</strong> brother has ever mentioned the wall again, and Hamid aka has told this story at four <span class="cn-word" data-tr="toʻylar">weddings</span>, always finishing with the same line: a man who will not <span class="cn-word" data-pos="verb" data-tr="ayblash">blame</span> his father in public will not <span class="cn-word" data-pos="verb" data-tr="ayblash">blame</span> his brother in private.</p>''',
        "questions": [
            {
                "text": "Why did neither brother answer the elder's question?",
                "choices": [
                    "Neither of them knew who had built the wall",
                    "The answer was their father, and neither would say his name in front of forty people",
                    "They had agreed not to speak at the meeting",
                ],
                "answer": 1,
                "explanation": "Devorni otalari 1974-yilda qiyshiq "
                               "qurgan edi. Ikkisi ham buni bilardi, "
                               "lekin qirq kishi oldida otasining "
                               "ismini aytmadi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "Neither of them didn't answer.",
                    "Neither of them answered.",
                    "Neither of them were answer.",
                ],
                "answer": 1,
                "explanation": "<b>neither</b> ichida inkor bor, "
                               "shuning uchun <i>didn't</i> "
                               "qoʻshilmaydi va feʼl birlikda "
                               "boʻladi.",
            },
            {
                "text": "Which sentence uses `every` correctly?",
                "choices": [
                    "Every man in the room knew the answer.",
                    "Every men in the room knew the answer.",
                    "Every men in the room knows the answer.",
                ],
                "answer": 0,
                "explanation": "<b>every</b> dan keyin birlikdagi ot "
                               "va birlikdagi feʼl keladi — maʼnosi "
                               "koʻplik boʻlsa ham.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-72 — word order SVOMPT  (the sign)                       [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Sentence That Sounded Wrong",
        "summary": (
            "PE-72 matni. 2004-yilda oʻn uch yoshli bola doʻkon "
            "peshtoqiga inglizcha yozuv chizdi. Soʻzlarning tartibi "
            "notoʻgʻri edi. Yigirma yildan keyin u soʻz tartibidan "
            "dars beradi — va oʻsha yozuvni hech kim oʻzgartirmadi."
        ),
        "order":   72,
        "grammar": [
            {
                "pattern":  "The SVOMPT chain",
                "meaning":  "Ingliz gapining tabiiy tartibi: "
                            "<b>S</b>ubject – <b>V</b>erb – "
                            "<b>O</b>bject – <b>M</b>anner – "
                            "<b>P</b>lace – <b>T</b>ime. "
                            "<i>We bake bread <b>slowly</b> "
                            "<b>here</b> <b>every morning</b></i>. "
                            "Oʻzbekcha tartib teskari boʻlgani "
                            "uchun aynan shu zanjir eng koʻp "
                            "buziladi.",
                "examples": ["We sell fresh bread here every morning.",
                             "He painted the sign carefully on the wall in 2004."],
            },
            {
                "pattern":  "The forbidden place: between verb and object",
                "meaning":  "Feʼl va obyekt <b>ajratilmaydi</b>: "
                            "<i>We have <s>always</s> fresh bread</i> "
                            "✗ → <i>We <b>always have</b> fresh "
                            "bread</i> ✓. Xuddi shunday: "
                            "<i>I like <s>very much</s> plov</i> ✗ → "
                            "<i>I like plov <b>very much</b></i> ✓.",
                "examples": ["We always have fresh bread.",
                             "I like this street very much."],
            },
            {
                "pattern":  "Which links can move",
                "meaning":  "Vaqt (<b>T</b>) gap boshiga chiqishi "
                            "mumkin: <i><b>Every morning</b> we bake "
                            "bread here</i>. Takrorlanish "
                            "ravishlari (<i>always, never, "
                            "usually</i>) esa oddiy feʼldan "
                            "<b>oldin</b>, <i>be</i> dan <b>keyin</b>: "
                            "<i>He <b>never</b> closes</i> · "
                            "<i>He <b>is never</b> late</i>.",
                "examples": ["Every morning the queue starts at six.",
                             "The shop is never closed on a Sunday."],
            },
        ],
        "body": '''<p>In 2004 my uncle painted the front of his shop in Samarkand blue and asked his youngest son to write something in English on it, because the street had started to fill up with <span class="cn-word" data-tr="turistlar">tourists</span> and the boy had the best marks in his class.</p>

<p>The boy was thirteen. He worked on it for two evenings with a <span class="cn-word" data-tr="qalam, moʻyqalam">brush</span> and a dictionary, and this is what has been on that wall for twenty-one years:</p>

<p><i>WE HAVE ALWAYS FRESH BREAD IN MORNING HERE.</i></p>

<p><span class="cn-word" data-tr="har bir soʻz">Every word</span> in it is a real English word. <span class="cn-word" data-tr="hech biri">None of them</span> is in the right place. <i>Always</i> has walked in between the verb and its object, where nothing is allowed to stand; <i>in morning</i> has lost its article and arrived before <i>here</i>; and the whole time-and-place end of the sentence is <span class="cn-word" data-pos="adj" data-tr="teskari">back to front</span>. In proper order it is eight words: <i>We always have fresh bread here in the morning.</i></p>

<p>Tourists have been photographing that sign since about 2006. There is a <span class="cn-word" data-tr="turizm boʻyicha qoʻllanma">guidebook</span> from 2013 with a photograph of it in the Samarkand chapter, and a Polish woman once came in and asked to be photographed <span class="cn-word" data-pos="adv" data-tr="ostida">underneath</span> it with a <span class="cn-word" data-tr="non">loaf</span> in each hand.</p>

<p>The boy is thirty-four. He teaches English in a school in the same district, and he has been teaching word order to fourteen-year-olds for nine years.</p>

<p>In 2019 he came with a tin of paint and a plan to fix it.</p>

<p>His mother stood in the doorway with her arms folded and asked him one question: how many people had come into the shop because of the sign, and how many had come in because of the grammar?</p>

<p>He put the tin down.</p>

<p>The sign is still there. He <span class="cn-word" data-pos="verb" data-tr="rasmga oldi">photographed</span> it that afternoon, and it lives on the second slide of the <span class="cn-word" data-tr="taqdimot">presentation</span> he uses in class. He puts the wrong sentence on the board, and then the right one under it, and then he tells his pupils that the man who wrote the wrong one has fed a family for twenty years with it.</p>

<p>"<span class="cn-word" data-tr="tartib">Order</span> matters," he says. "Courage matters more. Now open your books, and do not write <i>I like very much English</i> in my class again."</p>''',
        "questions": [
            {
                "text": "Why is the wrong sign still on the wall?",
                "choices": [
                    "Nobody has noticed the mistakes",
                    "His mother pointed out that people came into the shop because of the sign, not because of the grammar",
                    "The paint was the wrong colour",
                ],
                "answer": 1,
                "explanation": "Onasi bitta savol berdi: yozuv sababli "
                               "kelganlar koʻpmi, grammatika sababli "
                               "kelganlar koʻpmi? Shundan keyin u "
                               "boʻyoqni qoʻydi.",
            },
            {
                "text": "What is the correct order of the sign's sentence?",
                "choices": [
                    "We have always fresh bread in morning here.",
                    "We always have fresh bread here in the morning.",
                    "We have fresh bread always in the morning here.",
                ],
                "answer": 1,
                "explanation": "<i>always</i> feʼldan oldin, keyin "
                               "obyekt, keyin joy (<i>here</i>), "
                               "oxirida vaqt (<i>in the morning</i>) — "
                               "SVOMPT zanjiri.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "I like very much this street.",
                    "I very like this street.",
                    "I like this street very much.",
                ],
                "answer": 2,
                "explanation": "Feʼl va obyekt orasiga hech narsa "
                               "qoʻyilmaydi — <i>very much</i> "
                               "obyektdan keyin keladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-73 — question tags  (the Sunday question)              [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "You're Coming, Aren't You?",
        "summary": (
            "PE-73 matni. Buvim har payshanba kuni bitta savol "
            "berardi: “kelasan-a?” Bir kuni u soʻrashni toʻxtatdi — "
            "va men savolning oʻzi nima degani boʻlganini shundagina "
            "tushundim."
        ),
        "order":   73,
        "grammar": [
            {
                "pattern":  "The two-part rule",
                "meaning":  "Gap tasdiq boʻlsa — quyruq inkor, "
                            "gap inkor boʻlsa — quyruq tasdiq: "
                            "<i>You're coming, <b>aren't you?</b></i> · "
                            "<i>You aren't busy, <b>are you?</b></i> "
                            "Quyruqda gapdagi yordamchi feʼl "
                            "qaytariladi, ega esa olmoshga "
                            "aylanadi.",
                "examples": ["You're coming, aren't you?",
                             "She wasn't at home, was she?"],
            },
            {
                "pattern":  "No helper verb? Use do / does / did",
                "meaning":  "Yordamchi feʼl boʻlmasa, "
                            "<b>do / does / did</b> olinadi: "
                            "<i>You come every Sunday, "
                            "<b>don't you?</b></i> · <i>She "
                            "telephoned, <b>didn't she?</b></i> "
                            "Maxsus holatlar: <i>I am → <b>aren't "
                            "I?</b></i>, <i>Let's… → <b>shall we?</b></i>, "
                            "buyruq → <i><b>will you?</b></i>",
                "examples": ["You come every Sunday, don't you?",
                             "Let's go on Thursday, shall we?"],
            },
            {
                "pattern":  "A tag is not really a question",
                "meaning":  "Ohang hammasini oʻzgartiradi. "
                            "Ovoz <b>pasaysa</b> — javob kutilmaydi, "
                            "bu roziligini soʻrash yoki "
                            "yaqinlik belgisi. Ovoz "
                            "<b>koʻtarilsa</b> — bu haqiqiy savol, "
                            "gapiruvchi ishonmaydi. Shuning uchun "
                            "quyruqli savol koʻpincha "
                            "<b>iltimos</b>ni yashiradi.",
                "examples": ["You won't forget, will you?",
                             "You're not angry with me, are you?"],
            },
        ],
        "body": '''<p>My grandmother telephoned every Thursday evening at about eight, for years, and the conversation had a shape you could set a clock by. My health. Her <span class="cn-word" data-tr="qoʻshnilar">neighbours</span>. The price of things. And then, at the end, always the same sentence:</p>

<p>"You're coming on Sunday, <strong>aren't you?</strong>"</p>

<p>I said yes about eighty per cent of the time and came about sixty. I was twenty-four, I was working in an office in Tashkent that I <span class="cn-word" data-pos="verb" data-tr="yomon koʻrardim">hated</span>, and Sunday was the only day that belonged to me.</p>

<p>She never <span class="cn-word" data-pos="verb" data-tr="bahslashmadi">argued</span> when I did not come. She would say, "You're busy, <strong>aren't you?</strong>" and then talk about the neighbours again.</p>

<p>In October she stopped asking.</p>

<p>The Thursday call still came. My health, her neighbours, the price of <span class="cn-word" data-tr="kartoshka">potatoes</span>. Then: "Well. <span class="cn-word" data-tr="xudo xohlasa">God willing</span>, we will see you." And she put the phone down.</p>

<p>I noticed it the third week, in a bus, on a Tuesday, and I sat there with my bag on my knees and understood the whole thing at once.</p>

<p>That tag had never been a question. Her voice went <strong>down</strong> at the end of it, every time — <i>aren't you</i>, not <i>aren't you?</i> — and a tag that goes down is not asking for information. She had known the answer before she asked. She was asking me to say yes.</p>

<p>And she had stopped asking because a woman of eighty-one does not go on asking for something she has been <span class="cn-word" data-pos="verb" data-tr="rad etilgan">refused</span> forty times.</p>

<p>I went that Sunday. She was <span class="cn-word" data-pos="adj" data-tr="hayron">surprised</span>, and she hid it badly, and she had cooked nothing, and we ate bread and jam and a very old <span class="cn-word" data-tr="pishiriq">cake</span> from a tin.</p>

<p>"You're not staying, <strong>are you?</strong>" she said, at about four.</p>

<p>"I am," I said. "Let's do the <span class="cn-word" data-tr="quvurcha, jild">gutter</span> at the back, <strong>shall we?</strong>"</p>

<p>She is ninety-one. She telephones on Thursdays. She asks the question again, at the end, in exactly the old way, and her voice goes down, and she is not asking for information — she is asking me to say yes, and I say yes, and now I go.</p>

<p>You do not hear those two words in a grammar book. You hear them in somebody's voice, and then one week you do not hear them, <span class="cn-word" data-pos="verb" data-tr="hisoblaysan">and you count</span> what that means.</p>''',
        "questions": [
            {
                "text": "Why did the grandmother stop asking her question?",
                "choices": [
                    "She had become too ill to telephone",
                    "She had been refused so many times that she stopped asking for something she was not going to get",
                    "She was angry with her grandchild",
                ],
                "answer": 1,
                "explanation": "Savol hech qachon maʼlumot soʻrash "
                               "emas edi — iltimos edi. Qirq marta "
                               "rad javobidan keyin u soʻrashni "
                               "toʻxtatdi.",
            },
            {
                "text": "\"You're coming, aren't you?\" with the voice going DOWN means:",
                "choices": [
                    "the speaker really does not know and wants information",
                    "the speaker expects agreement — it is closer to a request than a question",
                    "the speaker is angry",
                ],
                "answer": 1,
                "explanation": "Ohang pasaysa, quyruqli savol javob "
                               "soʻramaydi — rozilik soʻraydi. "
                               "Koʻtarilsa, u haqiqiy savolga "
                               "aylanadi.",
            },
            {
                "text": "Which tag is correct: \"Let's do the gutter, ___\"",
                "choices": [
                    "don't we?",
                    "shall we?",
                    "will you?",
                ],
                "answer": 1,
                "explanation": "<b>Let's</b> dan keyin doim "
                               "<b>shall we?</b>. Buyruqdan keyin "
                               "<i>will you?</i>, <i>I am</i> dan "
                               "keyin <i>aren't I?</i>",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-74 — subject–verb agreement  (March 2020)              [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The News Is Not Good",
        "summary": (
            "PE-74 matni. 2020-yil mart: otam telefonni qoʻydi va "
            "bitta gap aytdi. Oʻsha yil bizning mehmon uyimizni "
            "yopdi — va oʻzgartirdi ham."
        ),
        "order":   74,
        "grammar": [
            {
                "pattern":  "The singular nouns that look plural",
                "meaning":  "<b>news</b>, <b>information</b>, "
                            "<b>advice</b>, <b>money</b>, "
                            "<b>furniture</b>, <b>work</b>, "
                            "<b>mathematics</b> — birlik: "
                            "<i>The news <b>is</b> not good</i>, "
                            "<i>The information <b>was</b> clear</i>. "
                            "Teskari tomondan <b>people</b> va "
                            "<b>police</b> — koʻplik: "
                            "<i>The police <b>were</b> at the "
                            "bridge</i>.",
                "examples": ["The news is not good.",
                             "The information from the ministry was clear.",
                             "People were cancelling every hour."],
            },
            {
                "pattern":  "Ignore what comes between",
                "meaning":  "Feʼl <b>egaga</b> qaraydi, ega bilan "
                            "feʼl orasidagi soʻzlarga emas: "
                            "<i>The <b>list</b> of forty-one "
                            "bookings <b>was</b> on the table</i> "
                            "(<i>were</i> ✗ — ega <i>list</i>). "
                            "<i>and</i> koʻplik yasaydi, lekin "
                            "<i>with</i> yasamaydi.",
                "examples": ["The list of bookings was on the table.",
                             "My father and my aunt were in the kitchen."],
            },
            {
                "pattern":  "Amounts, and there is / there are",
                "meaning":  "Pul, vaqt va masofa <b>bir "
                            "butun</b> sanaladi: <i>Nine months "
                            "<b>is</b> a long time</i>, "
                            "<i>Two million soʻm <b>was</b> "
                            "everything we had</i>. "
                            "<i>There is / there are</i> esa "
                            "keyingi otga qarab tanlanadi: "
                            "<i>There <b>were</b> four rooms</i>, "
                            "<i>There <b>is</b> one room left</i>.",
                "examples": ["Nine months is a long time to wait.",
                             "There were four rooms and there is a fifth now."],
            },
        ],
        "body": '''<p>My father put the telephone down in the kitchen on the sixteenth of March 2020 and said five words: "The news <strong>is</strong> not good."</p>

<p>We have a guesthouse in a village outside Bukhara — four rooms, a yard, a <span class="cn-word" data-tr="tut daraxti">mulberry tree</span>, and my mother's cooking, which is the actual business.</p>

<p>The information from the ministry <strong>was</strong> clear enough. The <span class="cn-word" data-tr="chegaralar">borders</span> <strong>were</strong> closing. The list of our spring bookings — forty-one of them, from nine countries — <strong>was</strong> on the table under a bowl, and by the end of that week most of it <strong>had been</strong> cancelled by email, politely, in short sentences.</p>

<p>Two million soʻm <strong>was</strong> what we had in the tin. Nine months with no guests <strong>is</strong> a long time in a business like ours.</p>

<p>People <strong>were</strong> frightened that spring and everybody's plans <strong>were</strong> finished, and my father, who is fifty-nine, did the only thing he knows how to do with a bad year: he made a list of work.</p>

<p>The <span class="cn-word" data-tr="tom">roof</span> over the two back rooms <strong>was</strong> repaired in April, by him and my brother, with money that <strong>was</strong> supposed to buy new beds. My mother <span class="cn-word" data-pos="verb" data-tr="yozdi">wrote down</span> thirty-one <span class="cn-word" data-tr="retseptlar">recipes</span> that <strong>had</strong> never <strong>been</strong> written down in this family, and my aunt <span class="cn-word" data-pos="verb" data-tr="tarjima qildi">translated</span> the whole <span class="cn-word" data-tr="menyu">menu</span> into English properly, because our old menu <strong>was</strong> a page of mistakes that guests <strong>had been</strong> laughing at kindly for six years.</p>

<p>And I sat in that yard from May to December with a <span class="cn-word" data-tr="noutbuk">laptop</span> and a bad connection and learned English — one hundred and forty <span class="cn-word" data-tr="darslar">lessons</span>, four evenings a week, with a <span class="cn-word" data-tr="daftar">notebook</span> that I still have.</p>

<p>The police <strong>were</strong> on the road at the end of our street until June. Mathematics <strong>was</strong> my worst subject at school and I did the accounts that year anyway, because there <strong>was</strong> nobody else to do them.</p>

<p>Our first guests after all of it came in July 2021: a family of five from Poland who stayed nine days and ate in the yard under the mulberry tree every evening.</p>

<p>There <strong>are</strong> six rooms now. The <span class="cn-word" data-tr="menyu">menu</span> <strong>is</strong> correct. My mother's recipes <strong>are</strong> in a green book on a shelf in the kitchen, and I am the one who talks to the guests.</p>''',
        "questions": [
            {
                "text": "What did the family do with the year without guests?",
                "choices": [
                    "They closed the guesthouse and moved to the city",
                    "They repaired the roof, wrote down the recipes, fixed the English menu, and the narrator learned English",
                    "They waited for the borders to open and did nothing",
                ],
                "answer": 1,
                "explanation": "Otasi ish roʻyxati tuzdi: tom, "
                               "retseptlar, menyu tarjimasi — va "
                               "hikoya qiluvchi bir yilda 140 dars "
                               "ingliz tilini oʻrgandi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "The news are not good.",
                    "The news is not good.",
                    "The news were not good.",
                ],
                "answer": 1,
                "explanation": "<b>news</b> — <i>s</i> bilan tugasa "
                               "ham birlik ot. Xuddi shunday: "
                               "<i>information</i>, <i>advice</i>, "
                               "<i>money</i>.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "The list of forty-one bookings were on the table.",
                    "The list of forty-one bookings was on the table.",
                    "The list of forty-one bookings are on the table.",
                ],
                "answer": 1,
                "explanation": "Ega — <b>list</b> (birlik). Ega bilan "
                               "feʼl orasidagi <i>of forty-one "
                               "bookings</i> feʼlga taʼsir qilmaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-75 — possession  (the brass plate)                       [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Teacher's Desk and the Teachers' Room",
        "summary": (
            "PE-75 matni. Maktab bir xonaga qirq bir yil dars bergan "
            "muallim nomidan lavha buyurtma qildi. Ustaxona "
            "apostrofni boshqa joyga qoʻyib yubordi — va muallimning "
            "oʻzi uni tuzatishga qoʻymadi."
        ),
        "order":   75,
        "grammar": [
            {
                "pattern":  "Where the apostrophe goes",
                "meaning":  "Birlik → <b>'s</b>: <i>the "
                            "<b>teacher's</b> desk</i> (bitta "
                            "oʻqituvchi). Koʻplik <i>-s</i> bilan "
                            "tugasa → faqat <b>'</b>: <i>the "
                            "<b>teachers'</b> room</i> (bir necha "
                            "oʻqituvchi). Nostandart koʻplik → "
                            "yana <b>'s</b>: <i>the "
                            "<b>children's</b> books</i>.",
                "examples": ["the teacher's desk (one teacher)",
                             "the teachers' room (all of them)",
                             "the children's names"],
            },
            {
                "pattern":  "'s or of?",
                "meaning":  "<b>'s</b> — odam, hayvon, guruh va "
                            "vaqt uchun: <i>Nodira opa's class</i>, "
                            "<i>today's lesson</i>. <b>of</b> — "
                            "jonsiz narsalar uchun: <i>the corner "
                            "<b>of</b> the room</i>, <i>the name "
                            "<b>of</b> the school</i> "
                            "(<i>the room's corner</i> gʻalati "
                            "eshitiladi).",
                "examples": ["the corner of the room",
                             "forty-one years of teaching"],
            },
            {
                "pattern":  "a friend of mine, and the plural trap",
                "meaning":  "Ikki egalik birga: <b>a … of "
                            "mine / hers / theirs</b> — "
                            "<i>a pupil <b>of hers</b></i> "
                            "(<i>her pupil</i> ham toʻgʻri, lekin "
                            "<i>a her pupil</i> ✗). Va eng koʻp "
                            "uchraydigan xato: oddiy koʻplikka "
                            "apostrof qoʻyish — <i>photo's</i> ✗, "
                            "<i>photos</i> ✓.",
                "examples": ["a pupil of hers from 1998",
                             "two photos, four desks, three teachers"],
            },
        ],
        "body": '''<p>Nodira opa taught mathematics in room 12 of our school for forty-one years, in the same room, at the same desk, from 1979 until she retired in June 2020.</p>

<p>In 2022 a group of her old pupils — there are a lot of us, and some of us have money now — decided to pay for a <span class="cn-word" data-tr="misdan yasalgan lavha">brass plate</span> for the door of that room.</p>

<p>The text went to the <span class="cn-word" data-tr="ustaxona">workshop</span> in an email, in English and Uzbek, because two of the pupils live abroad and one of them <span class="cn-word" data-pos="verb" data-tr="pul yubordi">sent the money</span> from Canada. The English line was supposed to read: <i>THE TEACHER'S ROOM — NODIRA KARIMOVA, 1979–2020.</i></p>

<p>The plate arrived in March. It is beautiful. It says:</p>

<p><i>THE TEACHERS' ROOM — NODIRA KARIMOVA, 1979–2020.</i></p>

<p>One apostrophe, moved one letter to the right, and the room stopped being hers and became <span class="cn-word" data-tr="hammasining">everybody's</span>.</p>

<p>The group chat that evening had four hundred messages in it. Half of us wanted a new plate. The man in Canada offered to pay for it twice. A <span class="cn-word" data-tr="shogird">pupil</span> of hers from 1998, who is a lawyer, wrote a long message about the <span class="cn-word" data-tr="shartnoma">contract</span> with the workshop.</p>

<p>Somebody sent a photograph of the plate to Nodira opa, who is seventy-two and reads messages slowly and answers them completely.</p>

<p>Her answer came the next morning, and it ended the argument in three sentences.</p>

<p>"Leave it. I was one of many. In that room there were <span class="cn-word" data-tr="oʻttiz toʻqqizta">thirty-nine</span> other teachers before me, and Zuhra opa taught at that desk for eleven years before I ever walked into the building, and somebody will teach at it after me."</p>

<p>Then she wrote one more line, because she is a mathematics teacher and she has never let a mistake go past without naming it: "The <span class="cn-word" data-tr="apostrof">apostrophe</span> is in the wrong place for what you meant, and in the right place for what is true. Both things can be correct at once. That is unusual. Keep it."</p>

<p>The plate is on the door of room 12. Nobody has changed it.</p>

<p>Every September the new mathematics teacher — a man of twenty-six, a pupil of hers from 2014 — takes a <span class="cn-word" data-tr="latta">cloth</span> and cleans it before the first lesson, and he tells his class the story of the apostrophe, which takes about four minutes and is the only grammar lesson he ever gives.</p>''',
        "questions": [
            {
                "text": "What was the mistake on the plate?",
                "choices": [
                    "Her name was spelled wrong",
                    "The apostrophe made it \"the teachers' room\" (all of them) instead of \"the teacher's room\" (hers)",
                    "The dates were wrong",
                ],
                "answer": 1,
                "explanation": "Apostrof bir harf oʻngga koʻchdi: "
                               "<i>teacher's</i> (bitta) → "
                               "<i>teachers'</i> (hammasi). Xona "
                               "uning emas, hammaning xonasiga "
                               "aylandi.",
            },
            {
                "text": "Why did she want to keep it?",
                "choices": [
                    "A new plate would cost too much",
                    "Because thirty-nine teachers taught in that room before her, so the plural is actually true",
                    "Because she did not notice the mistake",
                ],
                "answer": 1,
                "explanation": "U “men koʻplardan biri edim” deb "
                               "yozdi — undan oldin oʻsha xonada "
                               "39 ta oʻqituvchi dars bergan. "
                               "Xato — maqsad uchun xato, haqiqat "
                               "uchun toʻgʻri.",
            },
            {
                "text": "Which is correct for one teacher's desk and several teachers' room?",
                "choices": [
                    "the teachers's desk / the teacher's room",
                    "the teacher's desk / the teachers' room",
                    "the teachers desk / the teachers room",
                ],
                "answer": 1,
                "explanation": "Birlik — <b>'s</b>; <i>-s</i> bilan "
                               "tugagan koʻplik — faqat "
                               "<b>apostrof</b>.",
            },
        ],
    },
]
