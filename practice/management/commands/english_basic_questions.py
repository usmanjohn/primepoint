# -*- coding: utf-8 -*-
"""Mixed English grammar tests for beginner / pre-intermediate pupils.

test_english_1, test_english_2 — easy (elementary)
test_english_3 — medium (pre-intermediate)

Topics: tenses, articles, gerunds & infinitives, numbers, plurals, pronouns,
prepositions, quantifiers, modals, comparatives, question forms, relative
clauses, conditionals, passive.
Explanations are in English with an Uzbek translation, as in english_questions.py.
"""


# =====================================================================
# TEST 1 — EASY: to be, present tenses, articles, plurals, numbers
# =====================================================================

test_english_1 = [
    {
        "text": "<p>Choose the correct option.</p><p><strong>Sam and I ___ in the same class this year.</strong></p>",
        "explanation": "<p><strong>are</strong> is correct. The subject <em>Sam and I</em> is plural (= we), so we use <strong>are</strong>. <br><br><em>(<strong>are</strong> toʻgʻri. <em>Sam and I</em> egasi koʻplikda (= we), shuning uchun <strong>are</strong> ishlatiladi.)</em></p>",
        "correct": "are",
        "choices": ["am", "is", "are", "be"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>My brother ___ football every Sunday morning.</strong></p>",
        "explanation": "<p><strong>plays</strong> is correct. In the Present Simple we add <strong>-s</strong> after <em>he / she / it</em>. <br><br><em>(<strong>plays</strong> toʻgʻri. Present Simple da <em>he / she / it</em> dan keyin fe'lga <strong>-s</strong> qoʻshiladi.)</em></p>",
        "correct": "plays",
        "choices": ["play", "plays", "playing", "is play"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>Anna ___ like coffee. She always drinks tea.</strong></p>",
        "explanation": "<p><strong>doesn't</strong> is correct. For <em>he / she / it</em> the Present Simple negative is <strong>doesn't + verb</strong> (the main verb stays in its base form: <em>like</em>). <br><br><em>(<strong>doesn't</strong> toʻgʻri. <em>He / she / it</em> uchun Present Simple inkori <strong>doesn't + fe'l</strong> boʻladi, fe'l esa oʻzgarmaydi: <em>like</em>.)</em></p>",
        "correct": "doesn't",
        "choices": ["don't", "doesn't", "isn't", "not"],
    },
    {
        "text": "<p>Choose the correct article.</p><p><strong>My father is ___ engineer.</strong></p>",
        "explanation": "<p><strong>an</strong> is correct. We use <strong>an</strong> before a vowel sound, and <em>engineer</em> begins with the sound /e/. <br><br><em>(<strong>an</strong> toʻgʻri. Unli tovush bilan boshlanadigan soʻzlar oldidan <strong>an</strong> qoʻyiladi, <em>engineer</em> esa /e/ tovushi bilan boshlanadi.)</em></p>",
        "correct": "an",
        "choices": ["a", "an", "the", "— (no article)"],
    },
    {
        "text": "<p>Choose the correct article.</p><p><strong>I bought a book yesterday. ___ book is about space.</strong></p>",
        "explanation": "<p><strong>The</strong> is correct. We use <em>a</em> when we mention something for the first time, and <strong>the</strong> when we talk about it again. <br><br><em>(<strong>The</strong> toʻgʻri. Biror narsani birinchi marta tilga olganda <em>a</em>, keyin qayta eslatganda esa <strong>the</strong> ishlatiladi.)</em></p>",
        "correct": "The",
        "choices": ["A", "An", "The", "— (no article)"],
    },
    {
        "text": "<p>Choose the correct article.</p><p><strong>My little sister goes to ___ school by bus every morning.</strong></p>",
        "explanation": "<p><strong>— (no article)</strong> is correct. With places we use for their purpose we say <em>go to school, go to bed, go to work</em> — with no article. <br><br><em>(<strong>Artiklsiz</strong> toʻgʻri. Joyning asosiy vazifasi haqida gapirilganda artikl qoʻyilmaydi: <em>go to school, go to bed, go to work</em>.)</em></p>",
        "correct": "— (no article)",
        "choices": ["a", "an", "the", "— (no article)"],
    },
    {
        "text": "<p>Choose the correct plural form.</p><p><strong>There are three ___ on the kitchen table.</strong></p>",
        "explanation": "<p><strong>knives</strong> is correct. Nouns ending in <em>-f / -fe</em> change to <strong>-ves</strong>: knife → knives, wife → wives, leaf → leaves. <br><br><em>(<strong>knives</strong> toʻgʻri. <em>-f / -fe</em> bilan tugagan otlar koʻplikda <strong>-ves</strong> ga aylanadi: knife → knives, wife → wives.)</em></p>",
        "correct": "knives",
        "choices": ["knifes", "knives", "knifs", "knife"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>How many ___ are there in your family? — Four.</strong></p>",
        "explanation": "<p><strong>children</strong> is correct. <em>Child</em> has an irregular plural: child → <strong>children</strong> (never <em>childrens</em>). <br><br><em>(<strong>children</strong> toʻgʻri. <em>Child</em> soʻzining koʻpligi notoʻgʻri shaklda yasaladi: child → <strong>children</strong>.)</em></p>",
        "correct": "children",
        "choices": ["childs", "children", "childrens", "child"],
    },
    {
        "text": "<p>Numbers. Choose the correct word for <strong>15</strong>.</p>",
        "explanation": "<p><strong>fifteen</strong> is correct. Be careful: <em>fifteen</em> = 15, but <em>fifty</em> = 50. The <strong>-teen</strong> ending means 13–19. <br><br><em>(<strong>fifteen</strong> toʻgʻri. Diqqat: <em>fifteen</em> = 15, <em>fifty</em> esa = 50. <strong>-teen</strong> qoʻshimchasi 13–19 sonlarini bildiradi.)</em></p>",
        "correct": "fifteen",
        "choices": ["fifty", "fifteen", "five teen", "fifth"],
    },
    {
        "text": "<p>Ordinal numbers. Choose the correct option.</p><p><strong>Her birthday is on the ___ (12th) of May.</strong></p>",
        "explanation": "<p><strong>twelfth</strong> is correct. Note the spelling change: twelve → <strong>twelfth</strong> (the <em>-ve</em> becomes <em>-f</em>), like five → fifth. <br><br><em>(<strong>twelfth</strong> toʻgʻri. Imloga e'tibor bering: twelve → <strong>twelfth</strong> (<em>-ve</em> → <em>-f</em>), xuddi five → fifth kabi.)</em></p>",
        "correct": "twelfth",
        "choices": ["twelve", "twelveth", "twelfth", "twelth"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>___ shoes over there are too big for me.</strong></p>",
        "explanation": "<p><strong>Those</strong> is correct. <em>Shoes</em> is plural and <em>over there</em> means far from the speaker → <strong>those</strong>. (this = near + singular, these = near + plural, that = far + singular) <br><br><em>(<strong>Those</strong> toʻgʻri. <em>Shoes</em> koʻplikda, <em>over there</em> esa uzoqni bildiradi → <strong>those</strong>.)</em></p>",
        "correct": "Those",
        "choices": ["This", "That", "These", "Those"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>My friends ___ a new football.</strong></p>",
        "explanation": "<p><strong>have got</strong> is correct. <em>My friends</em> is plural, so we use <strong>have got</strong>; <em>has got</em> is only for he / she / it. <br><br><em>(<strong>have got</strong> toʻgʻri. <em>My friends</em> koʻplikda, shuning uchun <strong>have got</strong>; <em>has got</em> esa faqat he / she / it uchun.)</em></p>",
        "correct": "have got",
        "choices": ["has got", "have got", "is got", "are got"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>___ some milk in the fridge.</strong></p>",
        "explanation": "<p><strong>There is</strong> is correct. <em>Milk</em> is an uncountable noun, so it takes the singular form <strong>there is</strong>. <br><br><em>(<strong>There is</strong> toʻgʻri. <em>Milk</em> sanalmaydigan ot, shuning uchun birlikdagi <strong>there is</strong> ishlatiladi.)</em></p>",
        "correct": "There is",
        "choices": ["There is", "There are", "There have", "It has"],
    },
    {
        "text": "<p>Choose the correct preposition.</p><p><strong>We usually play basketball ___ Saturday afternoon.</strong></p>",
        "explanation": "<p><strong>on</strong> is correct. We use <strong>on</strong> with days and dates (<em>on Monday, on 5th May</em>), <em>in</em> with months and years, and <em>at</em> with clock times. <br><br><em>(<strong>on</strong> toʻgʻri. Kunlar va sanalar bilan <strong>on</strong>, oy va yillar bilan <em>in</em>, soatlar bilan esa <em>at</em> ishlatiladi.)</em></p>",
        "correct": "on",
        "choices": ["in", "on", "at", "to"],
    },
    {
        "text": "<p>Choose the correct pronoun.</p><p><strong>Maria is my classmate. I often help ___ with maths.</strong></p>",
        "explanation": "<p><strong>her</strong> is correct. After a verb we need an object pronoun: I, you, he, <em>she</em> → me, you, him, <strong>her</strong>. <br><br><em>(<strong>her</strong> toʻgʻri. Fe'ldan keyin toʻldiruvchi olmosh keladi: <em>she</em> → <strong>her</strong>.)</em></p>",
        "correct": "her",
        "choices": ["she", "her", "hers", "herself"],
    },
    {
        "text": "<p>Word order. Choose the <u>correct</u> sentence.</p>",
        "explanation": "<p><strong>He is always happy.</strong> is correct. Adverbs of frequency (always, usually, often, never) go <u>after</u> the verb <em>to be</em>, but <u>before</u> other main verbs (<em>He always works hard</em>). <br><br><em>(<strong>He is always happy</strong> toʻgʻri. Takrorlanish ravishlari <em>to be</em> fe'lidan <u>keyin</u>, boshqa fe'llardan esa <u>oldin</u> keladi.)</em></p>",
        "correct": "He is always happy.",
        "choices": ["He always is happy.", "He is always happy.", "Always he is happy.", "He is happy always."],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>Be quiet, please! The baby ___ in the next room.</strong></p>",
        "explanation": "<p><strong>is sleeping</strong> is correct. The action is happening <em>now</em>, so we use the Present Continuous: <strong>am / is / are + verb-ing</strong>. <br><br><em>(<strong>is sleeping</strong> toʻgʻri. Harakat <em>hozir</em> sodir boʻlyapti, shuning uchun Present Continuous: <strong>am / is / are + fe'l-ing</strong>.)</em></p>",
        "correct": "is sleeping",
        "choices": ["sleeps", "sleep", "is sleeping", "are sleeping"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>This is ___ bag. (the bag of my sister)</strong></p>",
        "explanation": "<p><strong>my sister's</strong> is correct. To show that something belongs to <u>one</u> person we add <strong>'s</strong>: <em>my sister's bag</em>. (For several sisters it would be <em>my sisters' bag</em>.) <br><br><em>(<strong>my sister's</strong> toʻgʻri. <u>Bitta</u> shaxsga tegishlilikni bildirish uchun <strong>'s</strong> qoʻshiladi.)</em></p>",
        "correct": "my sister's",
        "choices": ["my sister", "my sisters", "my sister's", "my sisters'"],
    },
]


# =====================================================================
# TEST 2 — EASY: past & future, gerund/infinitive, quantifiers, numbers
# =====================================================================

test_english_2 = [
    {
        "text": "<p>Choose the correct option.</p><p><strong>We ___ an interesting film last night.</strong></p>",
        "explanation": "<p><strong>watched</strong> is correct. <em>Last night</em> is a finished past time, so we use the Past Simple. Regular verbs take <strong>-ed</strong>. <br><br><em>(<strong>watched</strong> toʻgʻri. <em>Last night</em> — oʻtgan tugagan vaqt, shuning uchun Past Simple; toʻgʻri fe'llarga <strong>-ed</strong> qoʻshiladi.)</em></p>",
        "correct": "watched",
        "choices": ["watch", "watches", "watched", "watching"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>She ___ to London last summer.</strong></p>",
        "explanation": "<p><strong>went</strong> is correct. <em>Go</em> is an irregular verb: go → <strong>went</strong> → gone. We never say <em>goed</em>. <br><br><em>(<strong>went</strong> toʻgʻri. <em>Go</em> — notoʻgʻri fe'l: go → <strong>went</strong> → gone. <em>Goed</em> shakli mavjud emas.)</em></p>",
        "correct": "went",
        "choices": ["goed", "went", "gone", "going"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>He ___ come to the party yesterday because he was ill.</strong></p>",
        "explanation": "<p><strong>didn't</strong> is correct. The Past Simple negative is <strong>didn't + base verb</strong>. The past meaning is already in <em>didn't</em>, so we say <em>didn't come</em>, not <em>didn't came</em>. <br><br><em>(<strong>didn't</strong> toʻgʻri. Past Simple inkori: <strong>didn't + fe'lning boshlangʻich shakli</strong>, shuning uchun <em>didn't come</em>.)</em></p>",
        "correct": "didn't",
        "choices": ["doesn't", "didn't", "wasn't", "hasn't"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>My parents ___ at home when I called them.</strong></p>",
        "explanation": "<p><strong>were</strong> is correct. <em>My parents</em> is plural, and the sentence is in the past → <strong>were</strong>. (was = I / he / she / it) <br><br><em>(<strong>were</strong> toʻgʻri. <em>My parents</em> koʻplikda va gap oʻtgan zamonda → <strong>were</strong>.)</em></p>",
        "correct": "were",
        "choices": ["was", "were", "are", "is"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>That bag looks heavy. Don't worry, I ___ help you.</strong></p>",
        "explanation": "<p><strong>will</strong> is correct. We use <strong>will</strong> for a decision made at the moment of speaking (an offer). <br><br><em>(<strong>will</strong> toʻgʻri. Gapirayotgan paytda qabul qilingan qaror (taklif) uchun <strong>will</strong> ishlatiladi.)</em></p>",
        "correct": "will",
        "choices": ["will", "am going", "will to", "going"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>Look at those black clouds! It ___ rain.</strong></p>",
        "explanation": "<p><strong>is going to</strong> is correct. When we can <u>see evidence</u> now that something will happen, we use <strong>be going to</strong>, not <em>will</em>. <br><br><em>(<strong>is going to</strong> toʻgʻri. Hozirgi <u>dalil</u> asosida bashorat qilinsa, <em>will</em> emas, <strong>be going to</strong> ishlatiladi.)</em></p>",
        "correct": "is going to",
        "choices": ["will", "is going to", "rains", "is raining"],
    },
    {
        "text": "<p>Gerund. Choose the correct option.</p><p><strong>I enjoy ___ books in the evening.</strong></p>",
        "explanation": "<p><strong>reading</strong> is correct. After <em>enjoy, like, love, hate, finish, mind</em> we use the gerund (verb + <strong>-ing</strong>). <br><br><em>(<strong>reading</strong> toʻgʻri. <em>Enjoy, like, love, hate, finish, mind</em> fe'llaridan keyin gerundiy (fe'l + <strong>-ing</strong>) keladi.)</em></p>",
        "correct": "reading",
        "choices": ["read", "to read", "reading", "reads"],
    },
    {
        "text": "<p>Infinitive. Choose the correct option.</p><p><strong>My cousin wants ___ a doctor in the future.</strong></p>",
        "explanation": "<p><strong>to be</strong> is correct. After <em>want, hope, need, would like, decide</em> we use the infinitive with <strong>to</strong>. <br><br><em>(<strong>to be</strong> toʻgʻri. <em>Want, hope, need, would like, decide</em> fe'llaridan keyin <strong>to</strong> li infinitiv keladi.)</em></p>",
        "correct": "to be",
        "choices": ["be", "to be", "being", "is"],
    },
    {
        "text": "<p>Infinitive. Choose the correct option.</p><p><strong>It was raining, so we decided ___ at home.</strong></p>",
        "explanation": "<p><strong>to stay</strong> is correct. <em>Decide</em> is always followed by the infinitive with <strong>to</strong>: <em>decide to do something</em>. <br><br><em>(<strong>to stay</strong> toʻgʻri. <em>Decide</em> fe'lidan keyin doim <strong>to</strong> li infinitiv keladi.)</em></p>",
        "correct": "to stay",
        "choices": ["stay", "staying", "to stay", "stayed"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>How ___ students are there in your class?</strong></p>",
        "explanation": "<p><strong>many</strong> is correct. <em>Students</em> is a countable noun in the plural → <strong>how many</strong>. We use <em>how much</em> with uncountable nouns (<em>how much water</em>). <br><br><em>(<strong>many</strong> toʻgʻri. <em>Students</em> sanaladigan ot → <strong>how many</strong>; sanalmaydigan otlar bilan esa <em>how much</em>.)</em></p>",
        "correct": "many",
        "choices": ["much", "many", "long", "old"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>There isn't ___ sugar in my tea.</strong></p>",
        "explanation": "<p><strong>any</strong> is correct. We normally use <em>some</em> in positive sentences and <strong>any</strong> in negatives and questions. <br><br><em>(<strong>any</strong> toʻgʻri. Odatda <em>some</em> tasdiq gaplarda, <strong>any</strong> esa inkor va soʻroq gaplarda ishlatiladi.)</em></p>",
        "correct": "any",
        "choices": ["some", "any", "many", "a"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>Everest is ___ mountain in the world.</strong></p>",
        "explanation": "<p><strong>the highest</strong> is correct. When we compare one thing with <u>all</u> the others we use the superlative with <strong>the</strong>: high → higher → <strong>the highest</strong>. <br><br><em>(<strong>the highest</strong> toʻgʻri. Bir narsani <u>barchasi</u> bilan taqqoslaganda <strong>the</strong> li orttirma daraja ishlatiladi.)</em></p>",
        "correct": "the highest",
        "choices": ["high", "higher", "the highest", "more high"],
    },
    {
        "text": "<p>Choose the correct preposition.</p><p><strong>There is a beautiful picture ___ the wall.</strong></p>",
        "explanation": "<p><strong>on</strong> is correct. We use <strong>on</strong> for a surface (<em>on the wall, on the table, on the floor</em>), and <em>in</em> for something inside (<em>in the box</em>). <br><br><em>(<strong>on</strong> toʻgʻri. Sirt ustidagi narsa uchun <strong>on</strong> (<em>on the wall, on the table</em>), ichidagi narsa uchun esa <em>in</em>.)</em></p>",
        "correct": "on",
        "choices": ["in", "on", "at", "under"],
    },
    {
        "text": "<p>Telling the time. How do we usually say <strong>7:30</strong>?</p>",
        "explanation": "<p><strong>half past seven</strong> is correct. For 30 minutes we say <strong>half past + the hour</strong>; for 15 minutes we say <em>a quarter past</em> / <em>a quarter to</em>. <br><br><em>(<strong>half past seven</strong> toʻgʻri. 30 daqiqa uchun <strong>half past + soat</strong>, 15 daqiqa uchun esa <em>a quarter past / to</em> ishlatiladi.)</em></p>",
        "correct": "half past seven",
        "choices": ["half past seven", "half to seven", "seven and half", "thirty past seven"],
    },
    {
        "text": "<p>Numbers and prices. Choose the correct option.</p><p><strong>How much ___ these trainers? — They are 250 000 soʻm.</strong></p>",
        "explanation": "<p><strong>are</strong> is correct. <em>These trainers</em> is plural, so the verb <em>to be</em> is <strong>are</strong>. (Another correct way to ask: <em>How much <u>do</u> these trainers <u>cost</u>?</em>) <br><br><em>(<strong>are</strong> toʻgʻri. <em>These trainers</em> koʻplikda, shuning uchun <strong>are</strong>. Yana bir toʻgʻri variant: <em>How much do these trainers cost?</em>)</em></p>",
        "correct": "are",
        "choices": ["is", "are", "do", "cost"],
    },
    {
        "text": "<p>Modal verbs. Choose the correct option.</p><p><strong>You ___ wear a seatbelt in a car. It is the law.</strong></p>",
        "explanation": "<p><strong>must</strong> is correct. <strong>Must</strong> expresses a strong obligation or a rule. (<em>can</em> = ability, <em>might</em> = possibility, <em>would</em> = polite / unreal) <br><br><em>(<strong>must</strong> toʻgʻri. <strong>Must</strong> qat'iy majburiyat yoki qonun-qoidani bildiradi.)</em></p>",
        "correct": "must",
        "choices": ["must", "can", "might", "would"],
    },
    {
        "text": "<p>Question words. Choose the correct option.</p><p><strong>___ is your birthday? — In April.</strong></p>",
        "explanation": "<p><strong>When</strong> is correct. <strong>When</strong> asks about time; <em>where</em> asks about place, <em>who</em> about a person, <em>what</em> about a thing. <br><br><em>(<strong>When</strong> toʻgʻri. <strong>When</strong> vaqtni, <em>where</em> joyni, <em>who</em> shaxsni, <em>what</em> narsani soʻraydi.)</em></p>",
        "correct": "When",
        "choices": ["What", "When", "Where", "Who"],
    },
    {
        "text": "<p>Word order. Choose the <u>correct</u> question.</p>",
        "explanation": "<p><strong>Where are you going?</strong> is correct. In questions the auxiliary verb comes <u>before</u> the subject: question word + auxiliary + subject + verb. <br><br><em>(<strong>Where are you going?</strong> toʻgʻri. Soʻroq gapda yordamchi fe'l egadan <u>oldin</u> keladi: soʻroq soʻzi + yordamchi fe'l + ega + fe'l.)</em></p>",
        "correct": "Where are you going?",
        "choices": ["Where you are going?", "Where are you going?", "Where do you going?", "Where you going are?"],
    },
]


# =====================================================================
# TEST 3 — MEDIUM: perfect tenses, verb patterns, articles, conditionals
# =====================================================================

test_english_3 = [
    {
        "text": "<p>Choose the correct option.</p><p><strong>I can't open the door — I ___ my keys.</strong></p>",
        "explanation": "<p><strong>have lost</strong> is correct. The Present Perfect shows a past action with a <u>result now</u> (the keys are still missing). <br><br><em>(<strong>have lost</strong> toʻgʻri. Present Perfect oʻtmishdagi harakatning <u>hozirgi natijasini</u> koʻrsatadi — kalitlar hali ham yoʻq.)</em></p>",
        "correct": "have lost",
        "choices": ["lose", "have lost", "had lost", "am losing"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>We ___ in this house since 2019.</strong></p>",
        "explanation": "<p><strong>have lived</strong> is correct. An action that started in the past and <u>continues now</u> takes the Present Perfect, especially with <em>since</em> and <em>for</em>. <br><br><em>(<strong>have lived</strong> toʻgʻri. Oʻtmishda boshlanib <u>hozir ham davom etayotgan</u> harakat Present Perfect da beriladi, ayniqsa <em>since</em> va <em>for</em> bilan.)</em></p>",
        "correct": "have lived",
        "choices": ["live", "lived", "have lived", "are living"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>My aunt has worked at this hospital ___ five years.</strong></p>",
        "explanation": "<p><strong>for</strong> is correct. We use <strong>for</strong> with a <u>period</u> of time (<em>for five years, for two hours</em>) and <em>since</em> with a <u>starting point</u> (<em>since 2019, since Monday</em>). <br><br><em>(<strong>for</strong> toʻgʻri. <strong>For</strong> vaqt <u>davomiyligi</u> bilan, <em>since</em> esa <u>boshlanish nuqtasi</u> bilan ishlatiladi.)</em></p>",
        "correct": "for",
        "choices": ["since", "for", "from", "during"],
    },
    {
        "text": "<p>Gerund or infinitive? Choose the correct option.</p><p><strong>I clearly remember ___ the door before I left the house.</strong></p>",
        "explanation": "<p><strong>locking</strong> is correct. <em>Remember + -ing</em> = you have a memory of an action you <u>already did</u>. <em>Remember + to do</em> = you don't forget a duty (<em>Remember to lock the door!</em>). <br><br><em>(<strong>locking</strong> toʻgʻri. <em>Remember + -ing</em> — <u>allaqachon bajarilgan</u> ishni eslash; <em>remember + to do</em> — bajarish kerak boʻlgan ishni unutmaslik.)</em></p>",
        "correct": "locking",
        "choices": ["to lock", "locking", "lock", "locked"],
    },
    {
        "text": "<p>Gerund or infinitive? Choose the correct option.</p><p><strong>On the way to the village we stopped ___ some petrol.</strong></p>",
        "explanation": "<p><strong>to buy</strong> is correct. <em>Stop + to do</em> = stop in order to do something (purpose). <em>Stop + -ing</em> = finish an activity (<em>He stopped smoking</em> = he gave it up). <br><br><em>(<strong>to buy</strong> toʻgʻri. <em>Stop + to do</em> — biror maqsad uchun toʻxtash; <em>stop + -ing</em> — ish-harakatni butunlay toʻxtatish.)</em></p>",
        "correct": "to buy",
        "choices": ["buying", "to buy", "buy", "bought"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>My little brother is very good at ___ pictures of animals.</strong></p>",
        "explanation": "<p><strong>drawing</strong> is correct. After a <u>preposition</u> (<em>at, in, of, about, for</em>) we always use the gerund: <em>good at drawing, interested in reading, tired of waiting</em>. <br><br><em>(<strong>drawing</strong> toʻgʻri. <u>Predlogdan</u> keyin doim gerundiy keladi: <em>good at drawing, interested in reading</em>.)</em></p>",
        "correct": "drawing",
        "choices": ["draw", "to draw", "drawing", "drew"],
    },
    {
        "text": "<p>Verb patterns. Choose the correct option.</p><p><strong>My parents let me ___ out with friends at weekends.</strong></p>",
        "explanation": "<p><strong>go</strong> is correct. After <em>let</em> and <em>make</em> we use the bare infinitive (no <em>to</em>): <em>let me go, make him work</em>. But: <em>allow me <u>to</u> go</em>. <br><br><em>(<strong>go</strong> toʻgʻri. <em>Let</em> va <em>make</em> dan keyin <em>to</em> siz infinitiv keladi: <em>let me go, make him work</em>.)</em></p>",
        "correct": "go",
        "choices": ["to go", "go", "going", "went"],
    },
    {
        "text": "<p>Articles. Choose the correct option.</p><p><strong>___ Mount Everest is in ___ Himalayas.</strong></p>",
        "explanation": "<p><strong>— / the</strong> is correct. Single mountains take <u>no article</u> (<em>Mount Everest</em>), but mountain <u>ranges</u> take <strong>the</strong> (<em>the Himalayas, the Alps</em>) — like rivers and seas. <br><br><em>(<strong>— / the</strong> toʻgʻri. Yakka togʻ nomlari artiklsiz, togʻ <u>tizmalari</u> esa <strong>the</strong> bilan ishlatiladi.)</em></p>",
        "correct": "— / the",
        "choices": ["— / the", "the / the", "— / —", "the / —"],
    },
    {
        "text": "<p>Articles. Choose the correct option.</p><p><strong>He plays ___ guitar in ___ rock band.</strong></p>",
        "explanation": "<p><strong>the / a</strong> is correct. With musical instruments we use <strong>the</strong> (<em>play the guitar, play the piano</em>), and <strong>a</strong> because it is one band among many (mentioned for the first time). <br><br><em>(<strong>the / a</strong> toʻgʻri. Musiqa asboblari bilan <strong>the</strong> ishlatiladi, guruh esa birinchi marta tilga olinayotgani uchun <strong>a</strong>.)</em></p>",
        "correct": "the / a",
        "choices": ["the / a", "a / the", "— / a", "the / the"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>I ___ play tennis when I was a child, but now I don't.</strong></p>",
        "explanation": "<p><strong>used to</strong> is correct. <strong>Used to + verb</strong> describes a past habit that has stopped. (<em>be used to + -ing</em> means 'be accustomed to' — a different structure.) <br><br><em>(<strong>used to</strong> toʻgʻri. <strong>Used to + fe'l</strong> oʻtmishdagi, endi tugagan odatni bildiradi.)</em></p>",
        "correct": "used to",
        "choices": ["use to", "used to", "am used to", "was used to"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>My sister is only 16, so she isn't ___ to drive a car.</strong></p>",
        "explanation": "<p><strong>old enough</strong> is correct. <strong>Enough</strong> comes <u>after</u> an adjective (<em>old enough, strong enough</em>), while <em>too</em> comes <u>before</u> it (<em>too young</em>). <br><br><em>(<strong>old enough</strong> toʻgʻri. <strong>Enough</strong> sifatdan <u>keyin</u>, <em>too</em> esa sifatdan <u>oldin</u> keladi.)</em></p>",
        "correct": "old enough",
        "choices": ["enough old", "old enough", "too old", "so old"],
    },
    {
        "text": "<p>Choose the correct option.</p><p><strong>It was ___ a boring film that we left the cinema early.</strong></p>",
        "explanation": "<p><strong>such</strong> is correct. We use <strong>such + (a) + adjective + noun</strong>, but <em>so + adjective</em> alone (<em>The film was <u>so</u> boring</em>). <br><br><em>(<strong>such</strong> toʻgʻri. <strong>Such + (a) + sifat + ot</strong>, <em>so</em> esa faqat sifat bilan ishlatiladi.)</em></p>",
        "correct": "such",
        "choices": ["so", "such", "too", "very"],
    },
    {
        "text": "<p>Question tags. Choose the correct option.</p><p><strong>You have finished your homework, ___?</strong></p>",
        "explanation": "<p><strong>haven't you</strong> is correct. A positive sentence takes a negative tag, and the tag repeats the <u>auxiliary verb</u> of the sentence (<em>have</em> → <strong>haven't</strong>). <br><br><em>(<strong>haven't you</strong> toʻgʻri. Tasdiq gapga inkor tag qoʻshiladi va tagda gapdagi <u>yordamchi fe'l</u> takrorlanadi.)</em></p>",
        "correct": "haven't you",
        "choices": ["haven't you", "have you", "didn't you", "don't you"],
    },
    {
        "text": "<p>Relative pronouns. Choose the correct option.</p><p><strong>The man ___ lives next door is a pilot.</strong></p>",
        "explanation": "<p><strong>who</strong> is correct. We use <strong>who</strong> for people, <em>which</em> for things, <em>whose</em> for possession and <em>where</em> for places. <br><br><em>(<strong>who</strong> toʻgʻri. Odamlar uchun <strong>who</strong>, narsalar uchun <em>which</em>, egalik uchun <em>whose</em>, joy uchun <em>where</em>.)</em></p>",
        "correct": "who",
        "choices": ["who", "which", "whose", "where"],
    },
    {
        "text": "<p>Conditionals. Choose the correct option.</p><p><strong>If it ___ tomorrow, we will stay at home.</strong></p>",
        "explanation": "<p><strong>rains</strong> is correct. In the First Conditional the <em>if</em>-clause uses the Present Simple even though it talks about the future: <strong>If + Present Simple, will + verb</strong>. <br><br><em>(<strong>rains</strong> toʻgʻri. Birinchi shart gapda <em>if</em> qismi kelasi zamon haqida boʻlsa ham Present Simple da beriladi.)</em></p>",
        "correct": "rains",
        "choices": ["rain", "rains", "will rain", "would rain"],
    },
    {
        "text": "<p>Quantifiers. Choose the correct option.</p><p><strong>I have ___ friends in this city, so I often feel lonely.</strong></p>",
        "explanation": "<p><strong>few</strong> is correct. <strong>Few</strong> (without <em>a</em>) has a negative meaning: 'almost none'. <em>A few</em> means 'some, enough'. <em>Little / a little</em> are used with uncountable nouns. <br><br><em>(<strong>few</strong> toʻgʻri. <strong>Few</strong> (artiklsiz) 'deyarli yoʻq' degan salbiy ma'noni beradi; <em>a few</em> esa 'bir nechta' degani.)</em></p>",
        "correct": "few",
        "choices": ["few", "a few", "little", "a little"],
    },
    {
        "text": "<p>Numbers. How do we normally read the year <strong>1995</strong>?</p>",
        "explanation": "<p><strong>nineteen ninety-five</strong> is correct. Years are usually read in two pairs: 19 | 95 → <strong>nineteen ninety-five</strong> (like 1812 = eighteen twelve). <br><br><em>(<strong>nineteen ninety-five</strong> toʻgʻri. Yillar odatda ikki juftlikka boʻlib oʻqiladi: 19 | 95.)</em></p>",
        "correct": "nineteen ninety-five",
        "choices": ["one thousand nine hundred ninety-five", "nineteen ninety-five", "one nine nine five", "nineteen hundred ninety-five"],
    },
    {
        "text": "<p>Passive voice. Choose the correct option.</p><p><strong>This beautiful bridge ___ in 1990.</strong></p>",
        "explanation": "<p><strong>was built</strong> is correct. The bridge does not act — something was done <u>to</u> it, so we use the passive: <strong>was / were + past participle</strong>. <br><br><em>(<strong>was built</strong> toʻgʻri. Koʻprik oʻzi harakat qilmaydi — unga nisbatan ish bajarilgan, shuning uchun majhul nisbat: <strong>was / were + III shakl</strong>.)</em></p>",
        "correct": "was built",
        "choices": ["built", "was built", "has built", "is building"],
    },
]
