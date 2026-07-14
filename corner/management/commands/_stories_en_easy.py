# English "Wonder" Readings — EASY level (A2-B1). IELTS-style engaging short reads, adapted
# from the Korean wonder stories but re-written for English learners. Story text = English,
# all vocab/grammar/explanations glossed in Uzbek. Deliberately simple: short sentences,
# high-frequency words, ~6 vocab marks, 1-2 easy grammar points, 3 questions.
# Import: python manage.py import_corner corner/management/commands/_stories_en_easy.py --author=<AUTHOR>

SUBJECT = {
    "name":    "English",
    "summary": "Ingliz tili: IELTS uslubidagi qiziqarli oʻqish matnlari — lugʻat va grammatika bilan.",
    "icon":    "bi-globe2",
    "color":   "#2563eb",
    "order":   2,
}

COLLECTION = {
    "title":       "Easy Reads",
    "description": "Boshlangʻich daraja (A2-B1) — sodda til bilan qiziqarli qisqa matnlar.",
    "order":       1,
}

STORIES = [
    # ── 1 ────────────────────────────────────────────────────────────────
    {
        "title":   "Cats Sleep All Day",
        "summary": "Mushuklar kuniga 15 soatdan koʻp uxlaydi — ovchi ajdodlari kabi kuch tejash uchun.",
        "order":   1,
        "body": '''<p>Have you ever <span class="cn-word" data-pos="verb" data-tr="sezmoq, payqamoq">noticed</span> that cats seem to sleep all the time? It is true. A cat sleeps for about fifteen hours every day. That is <strong>more than</strong> half of its life! So why do cats sleep so much?</p>
<p>Long ago, <span class="cn-word" data-pos="adj" data-tr="yovvoyi">wild</span> cats had to <span class="cn-word" data-pos="verb" data-tr="ov qilmoq">hunt</span> for their food. Hunting takes a lot of <span class="cn-word" data-tr="quvvat, energiya">energy</span>. <strong>To <span class="cn-word" data-pos="verb" data-tr="tejamoq, ayamoq">save</span> energy</strong>, cats rest and sleep for many hours. Even when a cat looks like it is sleeping, it can wake up very <span class="cn-word" data-pos="adv" data-tr="tez">quickly</span> if it hears a small sound. A cat that sleeps well and plays well is happy — and that is why so many people love cats.</p>''',
        "grammar": [
            {
                "pattern":  "to + verb (purpose)",
                "meaning":  "Maqsad: ...ish uchun. Feʼlning boshlangʻich shakli oldidan ‘to’ qoʻyiladi.",
                "examples": ["To save energy, cats sleep a lot.", "She went out to buy some milk."],
            },
            {
                "pattern":  "more than",
                "meaning":  "...dan ortiq, ...dan koʻp (miqdorni taʼkidlaydi).",
                "examples": ["A cat sleeps more than fifteen hours a day.", "There were more than 100 people."],
            },
        ],
        "questions": [
            {
                "text": "How many hours does a cat sleep each day?",
                "choices": ["About five hours", "About fifteen hours", "About twenty-two hours"],
                "answer": 1,
                "explanation": "Matnda mushuk kuniga taxminan 15 soat uxlashi aytilgan — bu uning umrining yarmidan koʻpi.",
            },
            {
                "text": "Why do cats sleep so much?",
                "choices": [
                    "Because they are always sick",
                    "To save energy, like their wild ancestors that had to hunt",
                    "Because they cannot see at night",
                ],
                "answer": 1,
                "explanation": "Yovvoyi ajdodlari ov qilishi kerak boʻlgan, ov esa koʻp quvvat talab qiladi — shuning uchun mushuklar kuch tejash uchun koʻp uxlaydi.",
            },
            {
                "text": "What can a cat do even while it looks like it is sleeping?",
                "choices": [
                    "Wake up quickly at a small sound",
                    "Run and jump in its sleep",
                    "Eat its food",
                ],
                "answer": 0,
                "explanation": "Matnda uxlayotgandek koʻrinsa ham, mushuk kichik tovushni eshitsa tez uygʻonishi aytilgan.",
            },
        ],
    },
    # ── 2 ────────────────────────────────────────────────────────────────
    {
        "title":   "Honey Never Goes Bad",
        "summary": "Arxeologlar Misr maqbarasidan 3000 yillik asalni topgan — u hali ham yeyishga yaroqli edi.",
        "order":   2,
        "body": '''<p>Most food goes bad after some time. But there is one food that can <span class="cn-word" data-pos="verb" data-tr="saqlanib turadi, buzilmaydi">last</span> for thousands of years: honey. Scientists once found honey in an old <span class="cn-word" data-tr="qabr, maqbara">tomb</span> in Egypt. The honey was more than 3,000 years old, but it was <span class="cn-word" data-pos="adv" data-tr="hamon, hali ham">still</span> safe to eat!</p>
<p>Why does honey last so long? Honey has very little water and a lot of sugar. <strong>Because of this</strong>, <span class="cn-word" data-tr="mikroblar, bakteriya">bacteria</span> cannot live in it. Bees also make honey in a way that stops <span class="cn-word" data-tr="mikroblar">germs</span> from growing. <strong>So</strong> if you keep the <span class="cn-word" data-tr="qopqoq">lid</span> <span class="cn-word" data-pos="adj" data-tr="yopiq">closed</span>, honey will almost never go bad.</p>''',
        "grammar": [
            {
                "pattern":  "because of + noun",
                "meaning":  "... tufayli, ... sababli. Otdan (yoki ot iborasidan) oldin keladi.",
                "examples": ["Because of the sugar, honey does not go bad.", "The game was cancelled because of the rain."],
            },
            {
                "pattern":  "so + result",
                "meaning":  "Shuning uchun, shu sababli (natijani bogʻlaydi).",
                "examples": ["Honey has little water, so bacteria cannot live in it.", "It was late, so we went home."],
            },
        ],
        "questions": [
            {
                "text": "What did scientists find in an old tomb in Egypt?",
                "choices": [
                    "Honey that was more than 3,000 years old and still safe to eat",
                    "A jar of fresh milk",
                    "A box of sugar",
                ],
                "answer": 0,
                "explanation": "Olimlar Misr maqbarasidan 3000 yildan oshgan, hali ham yeyish mumkin boʻlgan asalni topgan.",
            },
            {
                "text": "Why can't bacteria live in honey?",
                "choices": [
                    "Because honey is always kept cold",
                    "Because honey has very little water and a lot of sugar",
                    "Because honey is very salty",
                ],
                "answer": 1,
                "explanation": "Asalda suv juda kam, shakar esa koʻp boʻlgani uchun bakteriya unda yashay olmaydi.",
            },
            {
                "text": "What should you do to keep honey from going bad?",
                "choices": ["Put it in the sun", "Add water to it", "Keep the lid closed"],
                "answer": 2,
                "explanation": "Matnda qopqogʻini yopiq saqlasangiz, asal deyarli hech qachon buzilmasligi aytilgan.",
            },
        ],
    },
    # ── 3 ────────────────────────────────────────────────────────────────
    {
        "title":   "Every Snowflake Is Different",
        "summary": "Har bir qor uchqunida oltita tomon bor, ammo bir xil boʻlgan ikkitasi yoʻq.",
        "order":   3,
        "body": '''<p>In winter, snow falls quietly from the sky. <strong>Have you ever looked</strong> at a <span class="cn-word" data-tr="qor uchquni">snowflake</span> <span class="cn-word" data-pos="adv" data-tr="diqqat bilan, sinchiklab">closely</span>? Every snowflake has six sides and a beautiful <span class="cn-word" data-tr="shakl">shape</span>. But here is something <span class="cn-word" data-pos="adj" data-tr="ajoyib, hayratlanarli">amazing</span>: no two snowflakes are exactly the same.</p>
<p>A snowflake is born inside a cloud and then falls to the ground. On the way down, the <span class="cn-word" data-tr="harorat">temperature</span> changes a little. Because of these small changes, <strong>each snowflake</strong> <span class="cn-word" data-pos="verb" data-tr="oʻsadi, shakllanadi">grows</span> into a different shape. <span class="cn-word" data-tr="millionlab">Millions</span> of snowflakes fall every winter, but not one of them is the same. Next time it snows, look at a single snowflake — it is the only one like it in the whole world.</p>''',
        "grammar": [
            {
                "pattern":  "Have you ever + past participle?",
                "meaning":  "Hayotingizda hech ...ganmisiz? — tajriba haqida savol.",
                "examples": ["Have you ever looked at a snowflake closely?", "Have you ever eaten Korean food?"],
            },
            {
                "pattern":  "each + singular noun",
                "meaning":  "Har bir ... — doim birlik ot va birlik feʼl bilan keladi.",
                "examples": ["Each snowflake grows into a different shape.", "Each student has a book."],
            },
        ],
        "questions": [
            {
                "text": "What shape does every snowflake have?",
                "choices": ["Four sides", "Six sides", "A perfect circle"],
                "answer": 1,
                "explanation": "Matnda har bir qor uchquni oltita tomonli va goʻzal shaklga ega ekani aytilgan.",
            },
            {
                "text": "Why does each snowflake have a different shape?",
                "choices": [
                    "Because the temperature changes a little as it falls",
                    "Because people paint them",
                    "Because they are made of different colours",
                ],
                "answer": 0,
                "explanation": "Qor uchquni tushayotganda yoʻldagi harorat biroz oʻzgargani uchun har biri boshqa shakl oladi.",
            },
            {
                "text": "What is the main idea of the text?",
                "choices": [
                    "All snowflakes are exactly the same size",
                    "Every snowflake has six sides, but no two are the same",
                    "Snowflakes only fall at night",
                ],
                "answer": 1,
                "explanation": "Barcha qor uchqunlari oltita tomonli, biroq bir xil boʻlgani yoʻq — bu matnning asosiy gʻoyasi.",
            },
        ],
    },
    # ── 4 ────────────────────────────────────────────────────────────────
    {
        "title":   "Laughter Is Catching",
        "summary": "Yoningizdagi odam kulganda siz ham kulasiz — kulgi yuqadi va sogʻliqqa foydali.",
        "order":   4,
        "body": '''<p>When someone near you laughs, do you feel like laughing too? Laughter is easy to <span class="cn-word" data-pos="verb" data-tr="yuqmoq, yuqtirmoq">catch</span>. <strong>Even if</strong> you do not know why the person is laughing, you often <span class="cn-word" data-pos="verb" data-tr="jilmaymoq">smile</span> or laugh with them. This happens because our <span class="cn-word" data-tr="miya">brain</span> feels good when it hears the sound of laughter.</p>
<p>Laughing is also <strong>good for</strong> your <span class="cn-word" data-tr="salomatlik">health</span>. When you laugh a lot, your stress goes down and your heart gets <span class="cn-word" data-pos="adj" data-tr="kuchliroq">stronger</span>. There is an old saying: “Laughter brings good luck.” So if you are having a bad day, try laughing — you may feel much <span class="cn-word" data-pos="adv" data-tr="ancha, birmuncha">better</span>.</p>''',
        "grammar": [
            {
                "pattern":  "even if",
                "meaning":  "Hatto ...sa ham (yon berish, qarama-qarshilik).",
                "examples": ["Even if you don't know why, you laugh too.", "Even if it rains, we will go."],
            },
            {
                "pattern":  "good for + noun",
                "meaning":  "... uchun foydali (foyda bildiradi).",
                "examples": ["Laughing is good for your health.", "Fruit is good for you."],
            },
        ],
        "questions": [
            {
                "text": "Why do we often laugh when other people laugh?",
                "choices": [
                    "Because our brain feels good when it hears laughter",
                    "Because we are afraid of them",
                    "Because it is polite to copy people",
                ],
                "answer": 0,
                "explanation": "Miya kulgi ovozini eshitganda oʻzini yaxshi his qiladi, shuning uchun biz ham kulamiz.",
            },
            {
                "text": "How is laughing good for your health?",
                "choices": [
                    "It makes you taller",
                    "Your stress goes down and your heart gets stronger",
                    "It makes your eyes better",
                ],
                "answer": 1,
                "explanation": "Koʻp kulganda stress kamayadi va yurak mustahkamlanadi.",
            },
            {
                "text": "What does the writer suggest you do on a bad day?",
                "choices": ["Stay in bed all day", "Try laughing to feel better", "Avoid other people"],
                "answer": 1,
                "explanation": "Muallif kayfiyat yomon boʻlsa, bir kulib koʻrishni maslahat beradi — shunda oʻzingizni ancha yaxshi his qilasiz.",
            },
        ],
    },
]
