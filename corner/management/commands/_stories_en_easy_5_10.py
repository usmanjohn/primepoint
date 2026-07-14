# English "Wonder" Readings — EASY level, stories 5-10 (brings Easy Reads to a pack of 10).
# NEW: the grammar pattern is shown in BOLD (<strong>) right where it appears in the story,
# so learners can find it easily. Vocab marks are kept OFF the bolded grammar words to avoid
# tag conflicts. Story text = English; vocab/grammar/explanations in Uzbek. ~6-8 marks each.
# Import: python manage.py import_corner corner/management/commands/_stories_en_easy_5_10.py --author=<AUTHOR>

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
    # ── 5 ────────────────────────────────────────────────────────────────
    {
        "title":   "Sea Otters Hold Hands",
        "summary": "Dengiz suvsarlari suvda uxlaganda oqib ketmaslik uchun bir-birining panjasidan ushlab oladi.",
        "order":   5,
        "body": '''<p>Sea otters are one of the <span class="cn-word" data-pos="adj" data-tr="eng yoqimtoy">cutest</span> animals in the ocean. They spend most of their lives in the water, and they even sleep there, <span class="cn-word" data-pos="verb" data-tr="suzib yotib">floating</span> on their backs. But there is a problem: <strong>while they sleep</strong>, the water can slowly <span class="cn-word" data-pos="verb" data-tr="olib ketmoq">carry</span> them away from each other.</p>
<p>So how do sea otters stay together? The answer is very sweet: they hold hands while they sleep! By holding <span class="cn-word" data-tr="panjalar">paws</span>, a group of otters does not <span class="cn-word" data-pos="verb" data-tr="uzoqlashib ketmoq">drift apart</span>. Sometimes they also wrap their bodies in <span class="cn-word" data-tr="dengiz oʻti">seaweed</span> to stay in one place. <strong>Thanks to</strong> this <span class="cn-word" data-pos="adj" data-tr="aqlli, topqir">clever</span> <span class="cn-word" data-tr="odat">habit</span>, a family of otters can rest safely and wake up close together.</p>''',
        "grammar": [
            {
                "pattern":  "while + clause",
                "meaning":  "...ayotgan paytda, ... vaqtida (bir vaqtda sodir boʻlayotgan ish).",
                "examples": ["While they sleep, the water can carry them away.", "I listen to music while I study."],
            },
            {
                "pattern":  "thanks to + noun",
                "meaning":  "... tufayli, ... sharofati bilan (ijobiy sabab).",
                "examples": ["Thanks to this habit, otters stay together.", "Thanks to your help, I finished early."],
            },
        ],
        "questions": [
            {
                "text": "Where do sea otters sleep?",
                "choices": ["On the beach", "In the water, floating on their backs", "In trees near the sea"],
                "answer": 1,
                "explanation": "Matnda dengiz suvsarlari suvda, chalqancha suzib yotib uxlashi aytilgan.",
            },
            {
                "text": "Why do sea otters hold hands while they sleep?",
                "choices": [
                    "So they do not drift apart in the water",
                    "Because they are cold",
                    "To catch fish more easily",
                ],
                "answer": 0,
                "explanation": "Panjadan ushlab olish orqali suvsarlar uxlayotganda bir-biridan oqib uzoqlashmaydi.",
            },
            {
                "text": "What else do otters sometimes do to stay in one place?",
                "choices": ["Tie themselves to rocks", "Wrap themselves in seaweed", "Sleep on the shore"],
                "answer": 1,
                "explanation": "Baʼzan ular bir joyda qolish uchun tanasini dengiz oʻtiga oʻrab oladi.",
            },
        ],
    },
    # ── 6 ────────────────────────────────────────────────────────────────
    {
        "title":   "Ants Are Very Strong",
        "summary": "Chumoli oʻz vaznidan 50 barobar ogʻirni koʻtaradi, birgalikda ishlaydi va hiddan uyini topadi.",
        "order":   6,
        "body": '''<p>Ants may be <span class="cn-word" data-pos="adj" data-tr="mitti, juda kichik">tiny</span>, but they are <span class="cn-word" data-pos="adv" data-tr="aql bovar qilmas darajada">incredibly</span> strong. An ant can <span class="cn-word" data-pos="verb" data-tr="koʻtarmoq">lift</span> something that is about fifty times heavier than its own body. Just <span class="cn-word" data-pos="verb" data-tr="tasavvur qilmoq">imagine</span> a person lifting a car above their head — that is how strong an ant is!</p>
<p>Ants are also great team workers. <strong>When</strong> one ant is too <span class="cn-word" data-pos="adj" data-tr="zaif">weak</span> to move something big, many ants work together and carry it as a group. And <strong>no matter how</strong> far they travel from home, ants can always find their way back by <span class="cn-word" data-pos="verb" data-tr="ergashib, izidan borib">following</span> a smell. Such a small <span class="cn-word" data-tr="hasharot">insect</span>, yet such an amazing power!</p>''',
        "grammar": [
            {
                "pattern":  "when + clause (time)",
                "meaning":  "...ganda, ... paytida (biror holat yuz berganda).",
                "examples": ["When one ant is too weak, others help.", "When it rains, we stay inside."],
            },
            {
                "pattern":  "no matter how + adjective/adverb",
                "meaning":  "Qanchalik ... boʻlmasin (yon berish).",
                "examples": ["No matter how far they go, ants find their way home.", "No matter how hard it is, don't give up."],
            },
        ],
        "questions": [
            {
                "text": "How much can an ant lift?",
                "choices": ["About twice its body weight", "About fifty times its body weight", "About the same as its body weight"],
                "answer": 1,
                "explanation": "Matnda chumoli oʻz vaznidan taxminan 50 barobar ogʻir narsani koʻtara olishi aytilgan.",
            },
            {
                "text": "What do ants do when something is too big for one ant?",
                "choices": ["They leave it", "They work together and carry it as a group", "They break it into pieces"],
                "answer": 1,
                "explanation": "Bitta chumoliga ogʻirlik qilsa, koʻp chumoli birlashib uni guruh boʻlib koʻtaradi.",
            },
            {
                "text": "How do ants find their way back home?",
                "choices": ["By following a smell", "By listening for sounds", "By looking at the sun"],
                "answer": 0,
                "explanation": "Chumolilar hid izidan borib uyini topadi.",
            },
        ],
    },
    # ── 7 ────────────────────────────────────────────────────────────────
    {
        "title":   "Why Do We Yawn?",
        "summary": "Kimningdir esnashini koʻrsak biz ham esnaymiz — olimlar buni bir-birimizga yaqinlik hissi bilan bogʻlaydi.",
        "order":   7,
        "body": '''<p>Have you ever seen someone <span class="cn-word" data-pos="verb" data-tr="esnamoq">yawn</span> and then yawned yourself? Yawning is very easy to <span class="cn-word" data-pos="verb" data-tr="yuqmoq">catch</span>. <strong>Even</strong> reading about yawning can make you yawn. Maybe you are yawning right now!</p>
<p>Why does yawning <span class="cn-word" data-pos="verb" data-tr="tarqaladi">spread</span> so easily? Scientists think it is <span class="cn-word" data-pos="adj" data-tr="bogʻliq">connected</span> to how we feel about others. We tend to <span class="cn-word" data-pos="verb" data-tr="taqlid qilmoq">copy</span> the actions of people we feel close to. <strong>In fact</strong>, yawning spreads more easily between good friends than between <span class="cn-word" data-tr="notanish odamlar">strangers</span>. It is a funny little <span class="cn-word" data-tr="sir">secret</span> about the human body.</p>''',
        "grammar": [
            {
                "pattern":  "even + word/phrase (emphasis)",
                "meaning":  "Hatto ... ham — kutilmagan yoki kuchli holatni taʼkidlaydi.",
                "examples": ["Even reading about yawning can make you yawn.", "Even a child can understand this."],
            },
            {
                "pattern":  "in fact",
                "meaning":  "Aslida, haqiqatda (fikrni kuchaytirish yoki aniqlashtirish).",
                "examples": ["In fact, yawning spreads more between friends.", "It looks easy, but in fact it is hard."],
            },
        ],
        "questions": [
            {
                "text": "According to the text, what can make you yawn?",
                "choices": [
                    "Only being very tired",
                    "Seeing someone yawn, or even reading about yawning",
                    "Drinking cold water",
                ],
                "answer": 1,
                "explanation": "Birovning esnashini koʻrish yoki hatto esnash haqida oʻqish ham esnashga sabab boʻladi.",
            },
            {
                "text": "Why does yawning spread, scientists think?",
                "choices": [
                    "It is a kind of illness",
                    "It is connected to feeling close to others and copying them",
                    "It happens only in the morning",
                ],
                "answer": 1,
                "explanation": "Olimlar esnash boshqalarga yaqinlik hissi bilan bogʻliq boʻlib, ularga taqlid qilinishini aytadi.",
            },
            {
                "text": "Between whom does yawning spread more easily?",
                "choices": ["Between strangers", "Between good friends", "Between people who dislike each other"],
                "answer": 1,
                "explanation": "Matnda esnash yaqin doʻstlar orasida notanishlarga qaraganda osonroq yuqishi aytilgan.",
            },
        ],
    },
    # ── 8 ────────────────────────────────────────────────────────────────
    {
        "title":   "Flamingos Turn Pink From Their Food",
        "summary": "Flamingolar kulrang tugʻiladi; ular yeydigan krevetka va suvoʻtdagi tabiiy rang tufayli pushti boʻladi.",
        "order":   8,
        "body": '''<p>Flamingos are <span class="cn-word" data-pos="adj" data-tr="mashhur">famous</span> for their beautiful pink colour. But here is a <span class="cn-word" data-tr="ajablanarli narsa">surprise</span>: baby flamingos are not pink at all. They are born grey or white. So where does the pink colour come from?</p>
<p>The answer is their food. Flamingos eat tiny <span class="cn-word" data-tr="krevetka">shrimp</span> and <span class="cn-word" data-tr="suvoʻt">algae</span> that <span class="cn-word" data-pos="verb" data-tr="ichida boʻladi">contain</span> a natural pink colour. <strong>As</strong> they eat more of this food, their <span class="cn-word" data-tr="patlar">feathers</span> slowly turn pink. <strong>If</strong> a flamingo stops eating this food, it slowly <span class="cn-word" data-pos="verb" data-tr="yoʻqotadi">loses</span> its lovely colour. So a flamingo really is what it eats!</p>''',
        "grammar": [
            {
                "pattern":  "as + clause (as they eat more)",
                "meaning":  "...gani sari, ...ga qarab (ikki narsa birga oʻzgaradi).",
                "examples": ["As they eat more, their feathers turn pink.", "As it got dark, the air became cold."],
            },
            {
                "pattern":  "if + present, present (first conditional)",
                "meaning":  "Agar ...sa, ... (real, mumkin boʻlgan shart).",
                "examples": ["If a flamingo stops eating this food, it loses its colour.", "If you heat ice, it melts."],
            },
        ],
        "questions": [
            {
                "text": "What colour are baby flamingos?",
                "choices": ["Bright pink", "Grey or white", "Black"],
                "answer": 1,
                "explanation": "Matnda flamingo bolalari pushti emas, kulrang yoki oq tugʻilishi aytilgan.",
            },
            {
                "text": "Why do flamingos turn pink?",
                "choices": [
                    "Because of the hot sun",
                    "Because they eat shrimp and algae with a natural pink colour",
                    "Because they swim in pink water",
                ],
                "answer": 1,
                "explanation": "Ular yeydigan krevetka va suvoʻtda tabiiy pushti rang boʻlgani uchun patlari pushti boʻladi.",
            },
            {
                "text": "What happens if a flamingo stops eating this food?",
                "choices": ["It grows bigger", "It slowly loses its pink colour", "It turns blue"],
                "answer": 1,
                "explanation": "Agar flamingo bu ovqatni yeyishni toʻxtatsa, asta-sekin pushti rangini yoʻqotadi.",
            },
        ],
    },
    # ── 9 ────────────────────────────────────────────────────────────────
    {
        "title":   "Sloths: The Slowest Animals",
        "summary": "Leniviyets shunchalik sekinki, junida yashil suvoʻt oʻsadi — bu unga barglar orasida yashirinishga yordam beradi.",
        "order":   9,
        "body": '''<p>The sloth is one of the <span class="cn-word" data-pos="adj" data-tr="eng sekin">slowest</span> animals in the world. It moves <strong>so slowly that</strong> green <span class="cn-word" data-tr="suvoʻt">algae</span> can grow on its <span class="cn-word" data-tr="jun, moʻyna">fur</span>! This may sound strange, but the green colour actually helps the sloth <span class="cn-word" data-pos="verb" data-tr="yashirinmoq">hide</span> among the <span class="cn-word" data-tr="barglar">leaves</span>.</p>
<p>Sloths spend almost their whole lives <span class="cn-word" data-pos="verb" data-tr="osilib turib">hanging</span> in trees. They sleep for many hours and eat leaves very slowly. <strong>Because</strong> they move so little, they do not need much <span class="cn-word" data-tr="energiya, quvvat">energy</span>. In fact, a sloth comes down to the ground only about once a week. Being slow may look <span class="cn-word" data-pos="adj" data-tr="dangasa">lazy</span>, but for the sloth, it is the perfect way to stay safe.</p>''',
        "grammar": [
            {
                "pattern":  "so + adjective/adverb + that",
                "meaning":  "Shu qadar ...ki (natijani bildiradi).",
                "examples": ["It moves so slowly that algae grows on it.", "He was so tired that he fell asleep."],
            },
            {
                "pattern":  "because + clause",
                "meaning":  "Chunki, ... sababli (sabab ergash gapi).",
                "examples": ["Because they move so little, they need little energy.", "We stayed home because it was raining."],
            },
        ],
        "questions": [
            {
                "text": "Why can algae grow on a sloth?",
                "choices": ["Because it lives in water", "Because it moves so slowly", "Because it is always wet"],
                "answer": 1,
                "explanation": "Leniviyets shu qadar sekin harakatlanadiki, shu sabab junida yashil suvoʻt oʻsib chiqadi.",
            },
            {
                "text": "How does the green colour help the sloth?",
                "choices": ["It keeps it warm", "It helps it hide among the leaves", "It makes it look beautiful"],
                "answer": 1,
                "explanation": "Yashil rang leniviyetsga barglar orasida yashirinishga yordam beradi.",
            },
            {
                "text": "How often does a sloth come down to the ground?",
                "choices": ["Every day", "About once a week", "Never"],
                "answer": 1,
                "explanation": "Matnda leniviyets yerga taxminan haftada bir marta tushishi aytilgan.",
            },
        ],
    },
    # ── 10 ───────────────────────────────────────────────────────────────
    {
        "title":   "Your Amazing Heart",
        "summary": "Yurak kuniga 100 000 marta uradi va hech qachon toʻxtamaydi — tanadagi eng mehnatkash mushak.",
        "order":   10,
        "body": '''<p>Right now, without you even thinking about it, your heart is working hard. The heart is a strong <span class="cn-word" data-tr="mushak">muscle</span> that <span class="cn-word" data-pos="verb" data-tr="haydaydi">pumps</span> blood to every part of your body. It <span class="cn-word" data-pos="verb" data-tr="uradi">beats</span> about 100,000 times every single day!</p>
<p><strong>Even while</strong> you sleep, your heart never stops. In one year, it beats around 35 million times. The blood it pumps <span class="cn-word" data-pos="verb" data-tr="olib boradi">carries</span> <span class="cn-word" data-tr="kislorod">oxygen</span> and food to your body and keeps you <span class="cn-word" data-pos="adj" data-tr="tirik">alive</span>. <strong>So</strong> the next time you feel your <span class="cn-word" data-tr="yurak urishi">heartbeat</span>, remember that this small muscle is one of the hardest workers in your body.</p>''',
        "grammar": [
            {
                "pattern":  "even while + clause",
                "meaning":  "Hatto ...ayotganda ham (kutilmagan holatni taʼkidlaydi).",
                "examples": ["Even while you sleep, your heart works.", "Even while it rained, they kept playing."],
            },
            {
                "pattern":  "so + result (sentence connector)",
                "meaning":  "Shuning uchun, shu sababli (natijani bogʻlaydi).",
                "examples": ["So the next time you feel your heartbeat, remember this.", "It was late, so we went home."],
            },
        ],
        "questions": [
            {
                "text": "How many times does the heart beat each day?",
                "choices": ["About 1,000 times", "About 100,000 times", "About 10 times"],
                "answer": 1,
                "explanation": "Matnda yurak kuniga taxminan 100 000 marta urishi aytilgan.",
            },
            {
                "text": "Does the heart rest while you sleep?",
                "choices": ["Yes, it stops for a few hours", "No, it never stops", "Only sometimes"],
                "answer": 1,
                "explanation": "Siz uxlayotganingizda ham yurak hech qachon toʻxtamaydi.",
            },
            {
                "text": "What does the blood carry to your body?",
                "choices": ["Only water", "Oxygen and food", "Nothing important"],
                "answer": 1,
                "explanation": "Yurak haydaydigan qon tanaga kislorod va oziq olib boradi.",
            },
        ],
    },
]
