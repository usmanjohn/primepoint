# -*- coding: utf-8 -*-
"""Prime English Readings — PE-6 … PE-10 (batch 2).

PE-6 to be · PE-7 there is/are · PE-8 this/that/these/those ·
PE-9 present simple (habits, facts, timetables) · PE-10 negatives and questions.

Cumulative rule: PE-1…PE-5 (subject+verb, countable/uncountable, plurals,
articles, pronouns) are free. PE-6…PE-8 still use the toc's narrative-frame
exception. Two traps this batch:
  * PE-9 teaches POSITIVE present simple only — negatives and questions arrive in
    PE-10, so the PE-9 reading contains no "doesn't" and no "do you…?" at all.
  * PE-10 may then use them everywhere, and does: the whole story is questions.
No past tense anywhere (PE-19+), no continuous (PE-12+), no modals (PE-42+).

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_06_10.py --author=prime
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
    # PE-6 — the verb "to be": am / is / are
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "We Are the New Team",
        "summary": (
            "PE-6 matni. Shanba kuni hovlida oltita oʻquvchi va bitta murabbiy. "
            "Darvozabon yoʻq — lekin jamoa bor. Butun matn am / is / are ustida."
        ),
        "order":   6,
        "grammar": [
            {
                "pattern":  "I am · he/she/it is · we/you/they are",
                "meaning":  "“Boʻlmoq” feʼli shaxsga qarab uch shaklga "
                            "boʻlinadi. Oʻzbekchada bu qoʻshimcha ichida "
                            "yashiringan (<i>tayyorman</i>, <i>tayyormiz</i>), "
                            "inglizchada esa alohida soʻz boʻlib turadi.",
                "examples": ["I am Sherbek.", "Bekzod is our goalkeeper.",
                             "Six pupils are in the school yard."],
            },
            {
                "pattern":  "Negative: is not / isn't · are not / aren't",
                "meaning":  "Inkor uchun feʼldan keyin <b>not</b> qoʻyiladi — "
                            "boshqa hech narsa kerak emas. Qisqa shakl "
                            "gapirishda odatiy: <i>isn't</i>, <i>aren't</i>, "
                            "<i>I'm not</i>.",
                "examples": ["We are not ready.", "He isn't here."],
            },
            {
                "pattern":  "Question: Are you ready? · It is cold.",
                "meaning":  "Savolda ega va feʼl <b>joy almashadi</b>: "
                            "<i>You are ready</i> → <i>Are you ready?</i> "
                            "Va ob-havo, vaqt, masofa haqida gapirilsa, "
                            "inglizcha gap <b>it</b> talab qiladi: "
                            "<i>It is cold</i> — “Sovuq”.",
                "examples": ["Are you the new team?", "It is Saturday. It is cold."],
            },
        ],
        "body": '''<p>It <strong>is</strong> Saturday. It <strong>is</strong> cold. Six pupils <strong>are</strong> in the school yard with one ball.</p>

<p>"<strong>Are</strong> you the new team?" the <span class="cn-word" data-tr="murabbiy">coach</span> asks.</p>

<p>"We <strong>are</strong>," Jasur says. "But we <strong>are not</strong> <span class="cn-word" data-pos="adj" data-tr="tayyor">ready</span>."</p>

<p>"Why?"</p>

<p>"Bekzod <strong>is</strong> our <span class="cn-word" data-tr="darvozabon">goalkeeper</span>, and he <strong>isn't</strong> here. He is at the doctor."</p>

<p>The coach looks at the six faces. Two boys are <span class="cn-word" data-pos="adj" data-tr="baland boʻyli">tall</span>, four are small, and all six are cold.</p>

<p>"I <strong>am</strong> Sherbek," the smallest boy says. "I <strong>am not</strong> a goalkeeper. But my hands are big."</p>

<p>"Good," the coach says. "Today you <strong>are</strong> the goalkeeper."</p>

<p>After an hour their shirts <strong>are</strong> <span class="cn-word" data-pos="adj" data-tr="hoʻl">wet</span> and their faces <strong>are</strong> red. The <span class="cn-word" data-tr="hisob">score</span> is three–three. Nobody <strong>is</strong> <span class="cn-word" data-pos="adj" data-tr="jahli chiqqan">angry</span>.</p>

<p>"<strong>Are</strong> we a team now?" Sherbek asks.</p>

<p>"You <strong>are</strong>," the coach says. "A team <strong>is not</strong> eleven good players. It <strong>is</strong> eleven players in one place, every Saturday."</p>''',
        "questions": [
            {
                "text": "Why are the boys not ready at the beginning?",
                "choices": [
                    "Their goalkeeper is not there",
                    "They have no ball",
                    "The coach is late",
                ],
                "answer": 0,
                "explanation": "“Bekzod is our goalkeeper, and he isn't here.” "
                               "Darvozabon shifokorda — shuning uchun jamoa "
                               "tayyor emas.",
            },
            {
                "text": "Which sentence is correct English?",
                "choices": [
                    "We not ready.",
                    "We are not ready.",
                    "We are not are ready.",
                ],
                "answer": 1,
                "explanation": "Inkor <b>are + not</b> tarzida yasaladi. "
                               "Oʻzbekcha “tayyor emasmiz” da feʼl "
                               "koʻrinmaydi, inglizchada esa <i>are</i> "
                               "tushib qolmaydi.",
            },
            {
                "text": "What does the coach say a team is?",
                "choices": [
                    "Eleven good players",
                    "Eleven players in one place every Saturday",
                    "A goalkeeper with big hands",
                ],
                "answer": 1,
                "explanation": "Oxirgi gap: “A team is not eleven good players. "
                               "It is eleven players in one place, every "
                               "Saturday.” Yaʼni muhimi — mahorat emas, "
                               "davomiylik.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-7 — there is / there are
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "There Is a Cat on the Roof",
        "summary": (
            "PE-7 matni. Tomda bir mushuk qoladi va koʻchada besh kishi "
            "yigʻiladi. Faqat keksa ayol haqiqatni biladi — mushuklar oʻzi "
            "tushadi."
        ),
        "order":   7,
        "grammar": [
            {
                "pattern":  "There is + singular · There are + plural",
                "meaning":  "Biror narsaning <b>borligini</b> aytish uchun "
                            "ishlatiladi. Bu <i>there</i> — “u yerda” degani "
                            "emas, shunchaki qolipning bir qismi. "
                            "Oʻzbekchada bu — “bor”.",
                "examples": ["There is a cat on our roof.",
                             "There are five people in the street."],
            },
            {
                "pattern":  "There isn't … · Is there …?",
                "meaning":  "Inkor: <i>There isn't a ladder</i>. Savol: "
                            "<i>Is there a ladder?</i> — <b>is</b> oldinga "
                            "chiqadi, <i>there</i> orqada qoladi.",
                "examples": ["There isn't a ladder.",
                             "Is there a ladder in your house?"],
            },
            {
                "pattern":  "The FIRST noun decides",
                "meaning":  "Roʻyxat kelsa, feʼl birinchi otga qarab "
                            "tanlanadi: <i>There <b>is</b> a table and four "
                            "chairs</i>, lekin <i>There <b>are</b> four "
                            "chairs and a table</i>.",
                "examples": ["There is a loud noise, and then there is nothing."],
            },
        ],
        "body": '''<p>There <strong>is</strong> a cat on our <span class="cn-word" data-tr="tom">roof</span>. It is white and it does not <span class="cn-word" data-pos="verb" data-tr="harakat qiladi">move</span>.</p>

<p>"<strong>Is there</strong> a <span class="cn-word" data-tr="narvon">ladder</span> in your house?" my father asks the <span class="cn-word" data-tr="qoʻshni">neighbour</span>.</p>

<p>"<strong>There isn't</strong> a ladder," he says. "But <strong>there are</strong> two long <span class="cn-word" data-tr="taxta">boards</span> behind the garage."</p>

<p>Soon <strong>there are</strong> five people in the street: my father, the neighbour, two small boys, and an old woman with bread in her hand.</p>

<p>"<strong>There is</strong> no <span class="cn-word" data-tr="xavf">danger</span>," the old woman says. "<strong>There are</strong> cats on that roof every spring. They come down at night."</p>

<p>Nobody listens to her. The boys hold the boards and my father <span class="cn-word" data-pos="verb" data-tr="chiqadi">climbs</span>. <strong>There is</strong> a loud <span class="cn-word" data-tr="shovqin">noise</span>, and then <strong>there is</strong> nothing.</p>

<p>The cat is on the <span class="cn-word" data-tr="yer">ground</span>. It walks to the old woman and eats her bread.</p>

<p>"<strong>Are there</strong> any questions?" my father says from the roof.</p>

<p><strong>There are</strong> none.</p>''',
        "questions": [
            {
                "text": "Who is right about the cat?",
                "choices": [
                    "The father",
                    "The neighbour with the boards",
                    "The old woman with the bread",
                ],
                "answer": 2,
                "explanation": "“There are cats on that roof every spring. They "
                               "come down at night.” Mushuk haqiqatan oʻzi "
                               "tushadi — va uning nonini yeydi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "There are a table and four chairs in the kitchen.",
                    "There is a table and four chairs in the kitchen.",
                    "There is four chairs and a table in the kitchen.",
                ],
                "answer": 1,
                "explanation": "Feʼl <b>birinchi</b> otga qarab tanlanadi: "
                               "<i>a table</i> birlik → <b>is</b>. Agar "
                               "roʻyxat <i>four chairs</i> bilan boshlansa, "
                               "<b>are</b> boʻladi.",
            },
            {
                "text": "Where is the father at the end of the story?",
                "choices": [
                    "On the ground with the cat",
                    "Still on the roof",
                    "In the garage",
                ],
                "answer": 1,
                "explanation": "Mushuk yerda, ota esa tomda: “…my father says "
                               "<b>from the roof</b>.” Shuning uchun uning "
                               "savoliga hech kim javob bermaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-8 — this / that / these / those
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "This Is My Desk",
        "summary": (
            "PE-8 matni. Dushanba kuni yangi oʻquvchi Afsonaning partasida "
            "oʻtiradi. Bahs “bu” va “u” ustida boradi — va gullar bilan "
            "hal boʻladi."
        ),
        "order":   8,
        "grammar": [
            {
                "pattern":  "this / these = near · that / those = far",
                "meaning":  "Yaqindagi narsa — <b>this</b> (birlik), "
                            "<b>these</b> (koʻplik). Uzoqdagi narsa — "
                            "<b>that</b>, <b>those</b>. Oʻzbekchadagi "
                            "“bu / bular” va “u / ular” bilan aynan bir xil.",
                "examples": ["This is my desk.", "Those desks at the back are empty."],
            },
            {
                "pattern":  "With a noun, or alone",
                "meaning":  "Otdan oldin turishi mumkin — <i>this desk</i>, "
                            "<i>these flowers</i> — yoki otni butunlay "
                            "almashtirib, yolgʻiz turishi mumkin: "
                            "<i>This is mine</i>, <i>Those are dead</i>.",
                "examples": ["I water these flowers every morning.",
                             "Those are dead. These are not."],
            },
            {
                "pattern":  "these / those + plural noun",
                "meaning":  "Koʻplik shakl ikki joyda koʻrinadi: "
                            "koʻrsatish olmoshida ham, otda ham — "
                            "<i>these desk<b>s</b></i>, <i>those plant<b>s</b></i>. "
                            "“These desk” — xato.",
                "examples": ["These desks have no names."],
            },
        ],
        "body": '''<p><strong>This</strong> is Afsona's desk. It is near the window. <strong>That</strong> desk, near the door, is Dilnoza's.</p>

<p>On Monday morning a new boy sits at Afsona's desk. His bag is on her chair.</p>

<p>"Excuse me," she says. "<strong>This</strong> is my desk."</p>

<p>"<strong>These</strong> desks have no names," the boy says.</p>

<p>He is <span class="cn-word" data-pos="adj" data-tr="haq">right</span>. <strong>These</strong> desks are old and <span class="cn-word" data-pos="adj" data-tr="kulrang">grey</span>, and <strong>those</strong> desks at the back are old and grey too.</p>

<p>"<strong>This</strong> is my <span class="cn-word" data-tr="joy, oʻrindiq">seat</span> because <strong>this</strong> window is my window," Afsona says. "I <span class="cn-word" data-pos="verb" data-tr="suv quyaman">water</span> <strong>these</strong> flowers every morning."</p>

<p>The boy looks at the flowers on the <span class="cn-word" data-tr="deraza tokchasi">windowsill</span>. Then he looks at the two old <span class="cn-word" data-tr="tuvak">pots</span> on the <span class="cn-word" data-tr="orqa tomon">back</span> windowsill.</p>

<p>"<strong>Those</strong> are <span class="cn-word" data-pos="adj" data-tr="qurigan">dead</span>," he says. "<strong>These</strong> are not."</p>

<p>"Yes," Afsona says. "Nobody sits at <strong>that</strong> desk."</p>

<p>The boy takes his bag and walks to the back of the room. On Friday there is water in the two old pots, and one small green <span class="cn-word" data-tr="barg">leaf</span>.</p>

<p>Now <strong>this</strong> class has two windows with flowers: <strong>this</strong> one and <strong>that</strong> one.</p>''',
        "questions": [
            {
                "text": "Where does the new boy sit in the end?",
                "choices": [
                    "At Afsona's desk near the window",
                    "At the empty desk at the back",
                    "At Dilnoza's desk near the door",
                ],
                "answer": 1,
                "explanation": "“The boy takes his bag and walks to the back of "
                               "the room.” Va u yerdagi qurigan gullarni "
                               "sugʻorishni boshlaydi.",
            },
            {
                "text": "You point at plants far away from you. What do you say?",
                "choices": ["These are dead.", "Those are dead.", "This are dead."],
                "answer": 1,
                "explanation": "Uzoqda + koʻplik = <b>those</b>. Yaqinda "
                               "boʻlsa <i>these</i>, birlik boʻlsa "
                               "<i>that</i> / <i>this</i>.",
            },
            {
                "text": "Why does Afsona say the desk is hers?",
                "choices": [
                    "Because her name is on it",
                    "Because she looks after the window and the flowers",
                    "Because the teacher gives it to her",
                ],
                "answer": 1,
                "explanation": "Partalarda ism yoʻq — bola haq. Afsonaning "
                               "dalili boshqa: “this window is my window… I "
                               "water these flowers every morning.”",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-9 — present simple: habits, facts, timetables (POSITIVE only)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Every Morning at Six",
        "summary": (
            "PE-9 matni. Bekzodning kuni oltida boshlanadi: non, patnis, "
            "7:20 dagi avtobus. Odat, haqiqat va jadval — hammasi oddiy "
            "hozirgi zamonda."
        ),
        "order":   9,
        "grammar": [
            {
                "pattern":  "Habits: every morning + present simple",
                "meaning":  "Har kuni takrorlanadigan ish oddiy hozirgi "
                            "zamonda aytiladi. <b>he / she / it</b> bilan "
                            "feʼlga <b>-s</b> qoʻshiladi: <i>Bekzod "
                            "wash<b>es</b></i>, <i>his father work<b>s</b></i>.",
                "examples": ["Bekzod washes his face and drinks tea.",
                             "His father starts at four."],
            },
            {
                "pattern":  "Facts: Water boils at 100 degrees",
                "meaning":  "Hamisha toʻgʻri boʻlgan haqiqatlar ham shu "
                            "zamonda: tabiat qonunlari, qoidalar, "
                            "oʻzgarmas holatlar.",
                "examples": ["Water boils at one hundred degrees.",
                             "Bread needs twenty minutes in this oven."],
            },
            {
                "pattern":  "Timetables: The bus leaves at 7:20",
                "meaning":  "Jadval bilan belgilangan kelasi zamon "
                            "harakati hozirgi zamonda aytiladi — "
                            "avtobus, poyezd, dars, kino. "
                            "<i>will leave</i> shart emas.",
                "examples": ["The shop opens at seven.",
                             "The bus to school leaves at 7:20."],
            },
        ],
        "body": '''<p>Bekzod's day starts at six. The <span class="cn-word" data-tr="hid">smell</span> of bread wakes him.</p>

<p>Every morning at six the light in the bakery is already on. Bekzod's father <strong>works</strong> there. He <strong>starts</strong> at four.</p>

<p>Bekzod <strong>washes</strong> his face, <strong>drinks</strong> one cup of tea and <strong>walks</strong> two hundred steps to the bakery. His father <strong>gives</strong> him a <span class="cn-word" data-tr="patnis">tray</span> of hot bread. Bekzod <span class="cn-word" data-pos="verb" data-tr="koʻtarib boradi">carries</span> it to the shop on the corner.</p>

<p>The shop <strong>opens</strong> at seven. The bus to school <strong>leaves</strong> at 7:20. Bekzod always <span class="cn-word" data-pos="verb" data-tr="ulguradi">catches</span> it.</p>

<p>Water <strong>boils</strong> at one hundred <span class="cn-word" data-tr="daraja">degrees</span>. Bread <strong>needs</strong> twenty minutes in this <span class="cn-word" data-tr="tandir, pech">oven</span>. Bekzod <strong>knows</strong> these facts like his own name.</p>

<p>On Fridays the bakery <strong>closes</strong> early and the family <strong>eats</strong> together at three.</p>

<p>Every evening his father <strong>says</strong> the same sentence: "Bread <span class="cn-word" data-pos="verb" data-tr="koʻtariladi">rises</span> <span class="cn-word" data-pos="adv" data-tr="sekin">slowly</span>. People rise slowly too."</p>''',
        "questions": [
            {
                "text": "What time does Bekzod's father start work?",
                "choices": ["At four", "At six", "At seven"],
                "answer": 0,
                "explanation": "“He starts at four.” Bekzod oltida turadi, "
                               "otasi esa ikki soat oldin ishni boshlagan "
                               "boʻladi.",
            },
            {
                "text": "Why does the story say \"The bus leaves at 7:20\" and not \"The bus will leave at 7:20\"?",
                "choices": [
                    "Because it is a fact of nature",
                    "Because it is a timetable",
                    "Because it happens right now",
                ],
                "answer": 1,
                "explanation": "Jadval bilan belgilangan harakat — avtobus, "
                               "poyezd, dars — oddiy hozirgi zamonda "
                               "aytiladi, garchi kelasi zamon haqida boʻlsa "
                               "ham.",
            },
            {
                "text": "What does the father mean by \"People rise slowly too\"?",
                "choices": [
                    "People also need time to grow",
                    "People get up late in the morning",
                    "Bread and people are the same weight",
                ],
                "answer": 0,
                "explanation": "Non sekin koʻtariladi — odam ham. Bu "
                               "otaning har kuni takrorlaydigan gapi, "
                               "yaʼni odat, va shuning uchun "
                               "<i>says</i> — oddiy hozirgi zamon.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-10 — present simple: negatives and questions
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Does Anyone Know Where the Key Is?",
        "summary": (
            "PE-10 matni. 12-xona qulflangan, kalit yoʻq va yigirma "
            "oʻquvchi koridorda. Matn boshdan-oyoq savol va inkorlardan "
            "iborat — va yechim derazadan chiqadi."
        ),
        "order":   10,
        "grammar": [
            {
                "pattern":  "don't / doesn't + bare verb",
                "meaning":  "Inkor <b>do not</b> / <b>does not</b> "
                            "yordamchisi bilan yasaladi, feʼl esa "
                            "<b>-s siz</b> asosiy shaklda qoladi: "
                            "<i>he doesn't work</i>, hech qachon "
                            "<i>doesn't works</i> emas.",
                "examples": ["I don't have it.",
                             "He doesn't work on Tuesday mornings."],
            },
            {
                "pattern":  "Do / Does + subject + verb?",
                "meaning":  "Savolda <b>do</b> yoki <b>does</b> gap boshiga "
                            "chiqadi va <b>-s</b> ni oʻziga oladi. "
                            "Oʻzbekchada bu vazifani “-mi” bajaradi.",
                "examples": ["Do you have it?",
                             "Does the caretaker keep a second key?"],
            },
            {
                "pattern":  "Wh- + do/does + subject + verb?",
                "meaning":  "Soʻroq soʻzi eng oldinga chiqadi, keyin "
                            "oʻsha qolip takrorlanadi: "
                            "<i>Where does he keep it?</i>, "
                            "<i>What time does he arrive?</i>",
                "examples": ["Where does he keep it?",
                             "Why do we need the key?"],
            },
        ],
        "body": '''<p>The door of Room 12 is <span class="cn-word" data-pos="adj" data-tr="qulflangan">locked</span>, and nobody has the key.</p>

<p>"<strong>Do you have</strong> it?" Afsona asks Jasur.</p>

<p>"I <strong>don't have</strong> it," he says. "I <strong>don't even come</strong> to this room on Tuesdays."</p>

<p>"<strong>Does</strong> the <span class="cn-word" data-tr="mudir, qorovul">caretaker</span> <strong>keep</strong> a second key?" Dilnoza asks. "<strong>Where does</strong> he <span class="cn-word" data-pos="verb" data-tr="saqlaydi">keep</span> it?"</p>

<p>"He <strong>doesn't work</strong> on Tuesday mornings," the teacher says.</p>

<p>"<strong>What time does</strong> he <span class="cn-word" data-pos="verb" data-tr="keladi">arrive</span>?"</p>

<p>"At eleven."</p>

<p>Twenty pupils stand in the <span class="cn-word" data-tr="yoʻlak">corridor</span>. Some read, some talk, and one boy <span class="cn-word" data-pos="verb" data-tr="uxlaydi">sleeps</span> on his bag.</p>

<p>Then Sherbek asks a <span class="cn-word" data-pos="adj" data-tr="gʻalati">strange</span> question. "<strong>Why do we need</strong> the key? <strong>Does</strong> the window of Room 12 <strong>open</strong>?"</p>

<p>The window of Room 12 opens.</p>

<p>At eleven the caretaker arrives with his key. The room is <span class="cn-word" data-pos="adj" data-tr="toʻla">full</span>, and the lesson is already on page forty.</p>

<p>"<strong>How do</strong> you <strong>open</strong> a locked room without a key?" he asks.</p>

<p>Nobody <strong>answers</strong>. Sherbek looks at the window and <strong>doesn't say</strong> a word.</p>''',
        "questions": [
            {
                "text": "Why can't the pupils get the caretaker's key at first?",
                "choices": [
                    "He doesn't work on Tuesday mornings",
                    "He doesn't have a second key",
                    "He is in Room 12",
                ],
                "answer": 0,
                "explanation": "“He doesn't work on Tuesday mornings… "
                               "— What time does he arrive? — At eleven.”",
            },
            {
                "text": "Which question is correct English?",
                "choices": [
                    "Does he keeps a second key?",
                    "Does he keep a second key?",
                    "Does he keeping a second key?",
                ],
                "answer": 1,
                "explanation": "<b>-s</b> allaqachon <i>does</i> da bor, "
                               "shuning uchun asosiy feʼl <b>keep</b> "
                               "shaklida qoladi.",
            },
            {
                "text": "How do the pupils get into Room 12?",
                "choices": [
                    "Through the window",
                    "With the teacher's key",
                    "They wait until eleven",
                ],
                "answer": 0,
                "explanation": "Sherbekning savoli javobning oʻzi edi: "
                               "“Does the window of Room 12 open?” — va "
                               "u ochiladi. Soat oʻn birda xona allaqachon "
                               "toʻla.",
            },
        ],
    },
]
