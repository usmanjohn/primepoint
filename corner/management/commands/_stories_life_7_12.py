# English "Life Stories" — narrative readings, batch 2 (stories 7-12). Same style as
# batch 1 (_stories_life_1_6.py): first-person human-interest narratives with a quiet
# twist/life lesson, in the spirit of Keimyung story 20. ~18-22 vocab marks, 3-4 grammar
# structures (fresh patterns, not repeated from batch 1), 3 inference questions each.
# Import: python manage.py import_corner corner/management/commands/_stories_life_7_12.py --author=<AUTHOR>

SUBJECT = {
    "name":    "English",
    "summary": "Ingliz tili: IELTS uslubidagi qiziqarli oʻqish matnlari — lugʻat va grammatika bilan.",
    "icon":    "bi-globe2",
    "color":   "#2563eb",
    "order":   2,
}

COLLECTION = {
    "title":       "Life Stories",
    "description": "Yuqori oʻrta/yuqori daraja (B2-C1) — hayotiy hikoyalar, boy lugʻat, grammatika va chuqur saboqlar bilan.",
    "order":       4,
}

STORIES = [
    # ── 7 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Photograph in the Wallet",
        "summary": "Metroda topilgan hamyondagi eski fotosurat oʻn yilliklar davomida ajralgan opa-uka qayta topishishiga sabab boʻladi.",
        "order":   7,
        "body": '''<p>I found the wallet on the subway floor, <span class="cn-word" data-pos="verb" data-tr="qisilib qolgan">wedged</span> between two seats, its leather <span class="cn-word" data-pos="adj" data-tr="yumshoq boʻlib qolgan">worn soft</span> from years of use. Inside was a <span class="cn-word" data-pos="adj" data-tr="unchalik katta boʻlmagan">modest</span> amount of cash, an old <span class="cn-word" data-tr="shaxsni tasdiqlovchi hujjat">identification card</span>, and, tucked behind it, a small black-and-white photograph so <span class="cn-word" data-pos="adj" data-tr="burishgan, gʻijim boʻlgan">creased</span> it had nearly split in two.</p>
<p>The address on the card led me to a quiet apartment building near the river. An elderly man opened the door, and the moment he saw the wallet in my hand, his whole face changed — <span class="cn-word" data-tr="yengillik">relief</span>, then something closer to <span class="cn-word" data-tr="ishonmaslik">disbelief</span>. He <span class="cn-word" data-pos="verb" data-tr="rahmat aytdi">thanked</span> me more times than necessary and <span class="cn-word" data-pos="verb" data-tr="taklif qildi">invited</span> me in for tea, <span class="cn-word" data-pos="verb" data-tr="qatʼiy talab qildi">insisting</span> he could not let me leave without at least that much.</p>
<p>Over tea, he told me about the photograph. It showed a young girl of perhaps six, standing in front of a <span class="cn-word" data-tr="qishloq uyi">farmhouse</span> that no longer existed. She was his younger sister. Their family had been <span class="cn-word" data-pos="verb" data-tr="ajratib yuborilgan edi">separated</span> during a difficult move decades earlier, and in the <span class="cn-word" data-tr="chalkashlik">confusion</span>, they lost each other's addresses entirely. He had <span class="cn-word" data-pos="verb" data-tr="olib yurgan edi">carried</span> her photograph in his wallet ever since, <span class="cn-word" data-pos="adj" data-tr="rozi boʻlmagan, tan olmaydigan">unwilling</span> to give up hope that he might one day find her again, even though every <span class="cn-word" data-tr="urinish, harakat">attempt</span> so far had led nowhere.</p>
<p><strong>Little did I know</strong> that returning a simple wallet would turn into something much bigger. <span class="cn-word" data-pos="adj" data-tr="taʼsirlangan, hayajonlangan">Moved</span> by his story, I offered to help search online, and together we spent the following weeks searching old records and social media groups for people from their <span class="cn-word" data-tr="tugʻilib oʻsgan shahar">hometown</span>. <strong>Were it not for</strong> a <span class="cn-word" data-pos="adj" data-tr="uzoq (qarindoshlik)">distant</span> cousin who <span class="cn-word" data-pos="verb" data-tr="tanidi">recognized</span> the farmhouse in an old post, we might never have found her at all.</p>
<p>The story was <strong>so</strong> moving <strong>that</strong> when the two siblings finally spoke on a video call, tears in both of their eyes after more than fifty years <span class="cn-word" data-pos="adv" data-tr="bir-biridan uzoqda, ajralib">apart</span>, I found myself crying too, a stranger who had simply picked up a wallet from a subway floor. <strong>Not until</strong> that moment <strong>did</strong> I truly understand that the photograph, not the cash, had been the only thing worth returning.</p>''',
        "grammar": [
            {
                "pattern":  "little did I know (inversion)",
                "meaning":  "Men bilmagan edim ki... — kutilmagan voqeani urgu bilan bildirish uchun feʼl-ega joyi almashadi.",
                "examples": ["Little did I know that returning a wallet would change two lives.", "Little did she know that the letter would arrive too late."],
            },
            {
                "pattern":  "were it not for + noun (formal inversion conditional)",
                "meaning":  "Agar ... boʻlmaganida (rasmiy uslub, 'if' siz shart gap).",
                "examples": ["Were it not for a distant cousin, we might never have found her.", "Were it not for his help, I would have failed."],
            },
            {
                "pattern":  "so + adjective + that",
                "meaning":  "Shunchalik ... ki, natijada ... (natija ergash gapi).",
                "examples": ["The story was so moving that I cried.", "It was so cold that the lake froze overnight."],
            },
            {
                "pattern":  "not until + time + did (inversion)",
                "meaning":  "Faqat ... paytdagina — vaqtni urgu bilan bildirish uchun inversiya ishlatiladi.",
                "examples": ["Not until that moment did I truly understand.", "Not until the next morning did we learn the news."],
            },
        ],
        "questions": [
            {
                "text": "What made the narrator realize the wallet was more than just cash?",
                "choices": [
                    "The amount of money inside was very large",
                    "A worn photograph inside told a decades-old family story",
                    "The wallet had a designer brand name",
                ],
                "answer": 1,
                "explanation": "Sumkadagi eski fotosurat orqasida yillar davomida ajralib qolgan opa-uka haqidagi hikoya bor edi — bu pulning qiymatidan koʻra muhimroq edi.",
            },
            {
                "text": "How did the narrator help the old man?",
                "choices": [
                    "By giving him more money",
                    "By helping search old records and social media for his lost sister",
                    "By introducing him to a lawyer",
                ],
                "answer": 1,
                "explanation": "Muallif chol bilan birga eski hujjatlar va ijtimoiy tarmoqlarda uning yoʻqolgan singlisini qidirishga yordam bergan.",
            },
            {
                "text": "What is the main idea of the story?",
                "choices": [
                    "Lost wallets are usually never returned to their owners",
                    "A small returned object can reconnect people separated for decades",
                    "Subway trains are the best place to find lost items",
                ],
                "answer": 1,
                "explanation": "Oddiy qaytarilgan hamyon orqali oʻn yilliklar davomida ajralgan opa-uka qayta topishishdi — bu hikoyaning asosiy gʻoyasi.",
            },
        ],
    },
    # ── 8 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Bicycle Doctor",
        "summary": "Parkda bepul velosiped taʼmirlaydigan chol aslida halok boʻlgan oʻgʻli xotirasi uchun shunday qiladi.",
        "order":   8,
        "body": '''<p>Every Saturday morning, <span class="cn-word" data-pos="adv" data-tr="istisnosiz">without fail</span>, an old man sets up a small folding table beside the park's bike path, a toolbox open in front of him and a hand-painted sign that reads simply: "Free bike repairs." I first met him the week my chain <span class="cn-word" data-pos="verb" data-tr="uzilib ketdi">snapped</span> halfway through my ride, leaving me <span class="cn-word" data-pos="adj" data-tr="qolib ketgan, iloji yoʻq">stranded</span> with a bicycle I had to push the rest of the way home.</p>
<p>He fixed the chain in minutes, <span class="cn-word" data-pos="verb" data-tr="rad etib, chetga surib">waving off</span> my offer to pay, and told me to come back anytime something else broke. <span class="cn-word" data-pos="adj" data-tr="qiziqib">Curious</span>, I asked why he did it for free. He explained that he <strong>used to</strong> repair bicycles for a small shop decades ago, long before retiring, and fixing them was simply something he had always been good at.</p>
<p>I became a <span class="cn-word" data-tr="doimiy mijoz">regular</span> at his little table, stopping by most weekends even when nothing on my bike needed fixing, just to talk. It was another regular, an older woman who brought her grandchildren every week, who eventually told me the rest of the story. Years earlier, the man's only son had been <span class="cn-word" data-pos="verb" data-tr="halok boʻlgan">killed</span> in a cycling <span class="cn-word" data-tr="baxtsiz hodisa">accident</span>, <span class="cn-word" data-pos="verb" data-tr="urib ketilgan">struck</span> by a car on this very path. He had never gotten the chance to teach his son how to fix his own bike, something the boy had always asked him to do.</p>
<p><strong>No matter how</strong> busy the park gets, he never turns a single person away, and <strong>despite</strong> carrying a <span class="cn-word" data-tr="qayg'u, gʻam">grief</span> most of us can hardly <span class="cn-word" data-pos="verb" data-tr="tasavvur qilmoq">imagine</span>, he greets every child at his table with the same <span class="cn-word" data-pos="adj" data-tr="sabrli">patient</span> warmth. He arrives early each Saturday, rain or shine, <strong>so as to</strong> have everything ready before the first <span class="cn-word" data-tr="velosipedchi">rider</span> stops by.</p>
<p>I never mentioned to him what I had learned, and he never brought it up. But I noticed, after that, how <span class="cn-word" data-pos="adv" data-tr="ehtiyotkorlik bilan">carefully</span> he taught the <span class="cn-word" data-tr="mahalla">neighborhood</span> kids to fix their own chains and <span class="cn-word" data-tr="tormoz">brakes</span>, <span class="cn-word" data-pos="verb" data-tr="rad etib">refusing</span> to simply fix things for them, <span class="cn-word" data-pos="verb" data-tr="qatʼiy talab qilib">insisting</span> they learn to do it with their own hands — the one lesson he never got the chance to give his son, given <span class="cn-word" data-pos="adv" data-tr="ochiqchasiga, bepul">freely</span> now to every child who stops at his table.</p>''',
        "grammar": [
            {
                "pattern":  "used to + verb",
                "meaning":  "Ilgari ... qilardim (hozir esa qilmayman) — oʻtmishdagi odatni bildiradi.",
                "examples": ["He used to repair bicycles for a small shop.", "I used to live in that neighborhood."],
            },
            {
                "pattern":  "despite + noun/-ing",
                "meaning":  "...ga qaramay (qarama-qarshilikni bildiradi).",
                "examples": ["Despite carrying a grief most of us can hardly imagine, he still smiles.", "Despite losing the match, the team stayed positive."],
            },
            {
                "pattern":  "no matter how/what",
                "meaning":  "Qanchalik ... boʻlmasin (shart-sharoitdan qatʼi nazar).",
                "examples": ["No matter how busy the park gets, he never turns anyone away.", "No matter what happens, I will keep trying."],
            },
            {
                "pattern":  "so as to + verb",
                "meaning":  "...ish uchun, shu maqsadda (maqsad ergash gapi, 'in order to' ga oʻxshash).",
                "examples": ["He arrives early so as to have everything ready.", "Speak clearly so as to be understood."],
            },
        ],
        "questions": [
            {
                "text": "Why does the old man fix bikes for free every Saturday?",
                "choices": [
                    "He is paid by the city government",
                    "Fixing bikes is something he is good at, and it also connects him to a memory of his son",
                    "He is training to open his own bike shop",
                ],
                "answer": 1,
                "explanation": "U velosiped taʼmirlashni yaxshi koʻradi, bundan tashqari bu ish uning halok boʻlgan oʻgʻli xotirasi bilan bogʻliq.",
            },
            {
                "text": "What did the narrator learn from another regular visitor?",
                "choices": [
                    "The old man used to be a professional cyclist",
                    "The old man's son died in a cycling accident on that same path",
                    "The old man was planning to retire soon",
                ],
                "answer": 1,
                "explanation": "Boshqa doimiy mijoz — bir kampir — chol yolgʻiz oʻgʻlining aynan shu yoʻlda avtohalokatda halok boʻlganini aytib bergan.",
            },
            {
                "text": "Why does the man insist on teaching children to fix their own bikes rather than doing it for them?",
                "choices": [
                    "He does not have enough time to fix every bike himself",
                    "It is the one lesson he never had the chance to give his own son",
                    "The park rules require children to learn basic repairs",
                ],
                "answer": 1,
                "explanation": "Bu — u oʻz oʻgʻliga bera olmagan yagona saboq, endi uni har bir bolaga bepul oʻrgatmoqda.",
            },
        ],
    },
    # ── 9 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Recipe with No Name",
        "summary": "Buvisining sirli retsept kartochkasidagi 'bir chimdim sabr' soʻzlari aslida shoshilmasdan oʻtkazilgan vaqt haqida ekan.",
        "order":   9,
        "body": '''<p>My grandmother left behind a small tin box of recipe cards when she passed, each one written in her <span class="cn-word" data-pos="adj" data-tr="ehtiyotkor, sinchkov">careful</span>, looping <span class="cn-word" data-tr="qoʻlyozma">handwriting</span>. Most were <span class="cn-word" data-pos="adj" data-tr="oddiy">ordinary</span> — soup, bread, a holiday cake — but one card had no name at all, just a short list of ingredients ending, <span class="cn-word" data-pos="adv" data-tr="gʻalati tarzda">strangely</span>, with the words "a pinch of <span class="cn-word" data-tr="sabr">patience</span>."</p>
<p>It was <strong>such a</strong> strange line <strong>that</strong> I laughed the first time I read it, <span class="cn-word" data-pos="verb" data-tr="taxmin qilib">assuming</span> it was simply her sense of humor. I tried the recipe anyway, following every <span class="cn-word" data-tr="oʻlchov">measurement</span> exactly, and the dish came out fine — <span class="cn-word" data-pos="adj" data-tr="yoqimli">pleasant</span>, even — but nothing like the version I remembered from childhood Sundays at her table.</p>
<p>I tried again the following week, <span class="cn-word" data-pos="verb" data-tr="shoshib">rushing</span> between phone calls and emails, <span class="cn-word" data-pos="verb" data-tr="aralashtirib">stirring</span> the pot with one hand while typing with the other. <strong>As long as</strong> I treated it like just another task to finish quickly, the result stayed the same: fine, but <span class="cn-word" data-pos="adj" data-tr="unutiladigan, eslab qolinmaydigan">forgettable</span>. I couldn't even taste the difference the recipe <span class="cn-word" data-pos="verb" data-tr="vada qilgan edi">promised</span>, <strong>let alone</strong> understand what "patience" had to do with cooking at all.</p>
<p>It was my aunt, visiting for the weekend, who finally showed me what I had been <span class="cn-word" data-pos="verb" data-tr="sogʻinib, qadrlamay yurgan edim">missing</span>. She turned off my phone, pulled a chair to the stove, and told me stories about our grandmother while we cooked together <span class="cn-word" data-pos="adv" data-tr="shoshilmasdan, sekin">slowly</span>, tasting as we went, <span class="cn-word" data-pos="verb" data-tr="toʻgʻirlab">correcting</span> as we went. <strong>The moment</strong> I stopped checking the time, the kitchen felt entirely different — <span class="cn-word" data-pos="adj" data-tr="issiqroq">warmer</span>, somehow, though nothing about the <span class="cn-word" data-tr="harorat">temperature</span> had changed.</p>
<p>When the dish was finally <span class="cn-word" data-pos="adj" data-tr="tayyor">ready</span>, it tasted exactly the way I remembered, and I understood, at last, what the card had been trying to tell me all along. The missing <span class="cn-word" data-tr="ingredient, tarkibiy qism">ingredient</span> was never a spice or a measurement. It was the <span class="cn-word" data-pos="adj" data-tr="shoshilmagan, xotirjam">unhurried</span> hours at the stove, spent with someone who loved you enough to stay.</p>''',
        "grammar": [
            {
                "pattern":  "such a/an + noun + that",
                "meaning":  "Shunchalik ... (narsa) ki, natijada ... (natija ergash gapi, sifatdosh oʻrniga otga bogʻlanadi).",
                "examples": ["It was such a strange line that I laughed.", "It was such a busy day that I forgot to eat."],
            },
            {
                "pattern":  "as long as + clause",
                "meaning":  "...gan ekan, ...gan sharti bilan (davom etayotgan shart).",
                "examples": ["As long as I rushed through it, the dish never tasted the same.", "You can stay as long as you like."],
            },
            {
                "pattern":  "let alone",
                "meaning":  "...haqida gapirmasa ham boʻladi (kuchli qarshi qoʻyish — kichik narsa ham boʻlmasa, kattasi haqida gap yoʻq).",
                "examples": ["I couldn't taste the difference, let alone understand it.", "She can't cook rice, let alone a full dinner."],
            },
            {
                "pattern":  "the moment + clause",
                "meaning":  "...gan zahoti, ...gan paytdayoq ('as soon as' bilan bir xil maʼnoda).",
                "examples": ["The moment I stopped checking the time, the kitchen felt different.", "The moment she walked in, everyone smiled."],
            },
        ],
        "questions": [
            {
                "text": "Why didn't the dish taste right the first few times the narrator cooked it?",
                "choices": [
                    "She used the wrong ingredients",
                    "She rushed through cooking it instead of taking her time",
                    "The recipe card was missing several steps",
                ],
                "answer": 1,
                "explanation": "U ovqatni shoshilib, telefon va emaillar bilan band boʻlgan holda tayyorlagan, shu sabab taʼm bir xil boʻlmagan.",
            },
            {
                "text": "What did the narrator's aunt do differently?",
                "choices": [
                    "She used a completely different recipe",
                    "She cooked slowly with the narrator, telling stories without any distractions",
                    "She ordered the dish from a restaurant instead",
                ],
                "answer": 1,
                "explanation": "Xola telefonni oʻchirib, ular birga sekin-asta pishirib, buvisi haqida hikoyalar aytib bergan.",
            },
            {
                "text": "What does the story suggest the 'pinch of patience' really meant?",
                "choices": [
                    "A rare spice that is hard to find",
                    "Taking unhurried time and sharing it with someone who cares",
                    "Following the measurements exactly without changing anything",
                ],
                "answer": 1,
                "explanation": "Sirli tarkibiy qism aslida aniq oʻlchov emas, balki sevgan odam bilan shoshilmasdan oʻtkazilgan vaqt ekan.",
            },
        ],
    },
    # ── 10 ───────────────────────────────────────────────────────────────
    {
        "title":   "The Wrong Number",
        "summary": "Xato raqamga yuborilgan xabar oylab davom etgan notanish suhbatga aylanadi — va ular bir yildan beri bir kafeda yonma-yon oʻtirishgan ekan.",
        "order":   10,
        "body": '''<p>The text was meant for an old friend, a <span class="cn-word" data-pos="adj" data-tr="charchagan">tired</span> <span class="cn-word" data-tr="shikoyat">complaint</span> about a delayed flight and a <span class="cn-word" data-tr="yoʻqolgan ulanish, oʻtkazib yuborilgan reys">missed connection</span>, typed quickly while I sat on an airport floor with a dead phone charger and a worse mood. <strong>Not that</strong> I meant to send it to a stranger — I had simply typed the wrong <span class="cn-word" data-tr="raqam">digit</span>, one number off from the contact I intended.</p>
<p>A reply came within minutes anyway. "Sounds like a <span class="cn-word" data-pos="adj" data-tr="ogʻir, mushkul">rough</span> night. Hope it gets better," it said, followed by a small joke about airport coffee. I typed back an apology for the wrong number, expecting silence after that. Instead, the stranger kept the <span class="cn-word" data-tr="suhbat">conversation</span> going, and somehow, an hour and a delayed flight later, we were still texting.</p>
<p>We never <span class="cn-word" data-pos="verb" data-tr="almashmadik">exchanged</span> photographs. <strong>Neither</strong> of us ever gave a real name, <strong>nor</strong> did either of us ask for one — and somehow that made it easier to be honest. Over the following months, we texted through hard days at work, family <span class="cn-word" data-tr="janjal, kelishmovchilik">arguments</span>, small <span class="cn-word" data-tr="gʻalaba, yutuq">victories</span> neither of us had anyone else to tell. <strong>Much as</strong> I wanted to know who they were, I never quite <span class="cn-word" data-pos="verb" data-tr="jazm etmadim, jur'at qilmadim">dared</span> to ask directly, <span class="cn-word" data-pos="adj" data-tr="xavotirlangan">worried</span> it might <span class="cn-word" data-pos="verb" data-tr="buzib qoʻyishi mumkin">break</span> whatever strange, easy thing we had built.</p>
<p>It was the stranger who finally <span class="cn-word" data-pos="verb" data-tr="taklif qildi">suggested</span> meeting, months later, at a coffee shop near my apartment. <strong>Given that</strong> neither of us had ever used our real names, walking in that afternoon felt like meeting someone from a dream. I <span class="cn-word" data-pos="verb" data-tr="koʻzdan kechirdim">scanned</span> the room for an <span class="cn-word" data-pos="adj" data-tr="notanish">unfamiliar</span> face, someone I had never seen before.</p>
<p>I never found one. The barista, laughing, pointed to the man three tables away who had been coming in every single morning for the past year, same time as me, both of us always too tired and too <span class="cn-word" data-pos="adj" data-tr="band, mashgʻul">focused</span> on our phones to notice each other. We had been sitting closer than either of us ever <span class="cn-word" data-pos="verb" data-tr="tasavvur qilgan edik">imagined</span>, the whole time.</p>''',
        "grammar": [
            {
                "pattern":  "not that + clause",
                "meaning":  "...gani uchun emas — oldingi fikrga kiritilgan tuzatish yoki inkorni bildiradi.",
                "examples": ["Not that I meant to text a stranger — I just typed the wrong digit.", "Not that I mind, but you're late."],
            },
            {
                "pattern":  "neither ... nor (with inversion)",
                "meaning":  "Na ..., na ... (ikkalasi ham emas); 'nor' dan keyin feʼl-ega joyi almashadi.",
                "examples": ["Neither of us gave a real name, nor did we ask for one.", "Neither did I call, nor did I write."],
            },
            {
                "pattern":  "much as + clause",
                "meaning":  "...gancha xohlasam ham (kuchli istak, lekin qarshi harakat qilinmagani).",
                "examples": ["Much as I wanted to know who they were, I never asked.", "Much as I enjoy travelling, I always miss home."],
            },
            {
                "pattern":  "given that + clause",
                "meaning":  "...ekanligini hisobga olganda, ...boʻlgani sababli.",
                "examples": ["Given that neither of us used real names, meeting felt strange.", "Given that it's raining, let's stay inside."],
            },
        ],
        "questions": [
            {
                "text": "How did the narrator first contact the stranger?",
                "choices": [
                    "By calling a customer service number by mistake",
                    "By texting the wrong number instead of an old friend",
                    "By replying to a social media post",
                ],
                "answer": 1,
                "explanation": "U eski doʻstiga yubormoqchi boʻlgan xabarni xato raqamga yuborib yuborgan.",
            },
            {
                "text": "What did the narrator and the stranger avoid doing for months?",
                "choices": [
                    "Meeting in person or sharing their real names",
                    "Talking about anything serious",
                    "Texting more than once a week",
                ],
                "answer": 0,
                "explanation": "Ular oylar davomida hech qachon uchrashmagan yoki haqiqiy ismlarini aytishmagan.",
            },
            {
                "text": "What is the twist at the end of the story?",
                "choices": [
                    "The stranger turned out to be a famous person",
                    "The stranger had been sitting near the narrator at the same coffee shop for a year without either noticing",
                    "The stranger never actually existed",
                ],
                "answer": 1,
                "explanation": "Ikkalasi ham bir yil davomida bir xil kafeda, bir-biriga yaqin oʻtirishgan, lekin telefonlariga band boʻlgani uchun bir-birini payqamagan ekan.",
            },
        ],
    },
    # ── 11 ───────────────────────────────────────────────────────────────
    {
        "title":   "The Last Lecture",
        "summary": "Talabalar sovuq va talabchan deb bilgan professor aslida har bir talabasining hayotini yillar davomida sezdirmasdan kuzatib yurgan ekan.",
        "order":   11,
        "body": '''<p>Professor Hall had a <span class="cn-word" data-tr="obroʻ, shuhrat">reputation</span> that followed him through every hallway of the engineering building: <span class="cn-word" data-pos="adj" data-tr="daho, ajoyib">brilliant</span>, <span class="cn-word" data-pos="adj" data-tr="talabchan, qattiqqoʻl">exacting</span>, and almost impossible to please. Students <span class="cn-word" data-pos="verb" data-tr="almashishardi">traded</span> warnings about him the way sailors trade warnings about storms. I took his course because I had no choice, sat in the back row for an entire semester, and left the day of the final exam <span class="cn-word" data-pos="verb" data-tr="qasam ichib">vowing</span> never to see him again.</p>
<p>He graded essays with a red pen so sharp it seemed personal, and he gave full marks <strong>provided that</strong> a student's reasoning, not just the final answer, held up under questioning. Few students ever earned his <span class="cn-word" data-tr="maqtov">praise</span>. I certainly never did, and for years afterward, whenever his name came up, I described him the same way everyone else did: cold, <span class="cn-word" data-pos="adj" data-tr="sovuq, begona">distant</span>, impossible to <span class="cn-word" data-pos="verb" data-tr="qoniqtirmoq">satisfy</span>.</p>
<p>Fifteen years later, I attended his <span class="cn-word" data-tr="nafaqaga chiqish">retirement</span> dinner mostly out of <span class="cn-word" data-tr="majburiyat, qarz">obligation</span>, expecting a short, <span class="cn-word" data-pos="adj" data-tr="qulaysiz, noqulay">awkward</span> evening among people I <span class="cn-word" data-pos="adv" data-tr="arang, deyarli...emas">barely</span> remembered. <strong>Hardly had</strong> the speeches ended <strong>when</strong> a former <span class="cn-word" data-tr="hamkasb">colleague</span> of his stood up holding a worn leather notebook. Inside, she explained, Professor Hall had written a paragraph about every single student who had ever passed through his classroom — what they <span class="cn-word" data-pos="verb" data-tr="qiynalganlar">struggled with</span>, what surprised him about them, and, whenever he could find out, what they had gone on to do with their lives.</p>
<p><strong>Far from</strong> being the cold, <span class="cn-word" data-pos="adj" data-tr="beparvo, loqayd">indifferent</span> man his reputation suggested, he had spent three decades <span class="cn-word" data-pos="adv" data-tr="jimgina, sezdirmasdan">quietly</span> following his former students' careers, often without their knowledge, simply because he wanted to know whether the <span class="cn-word" data-tr="urugʻlar">seeds</span> he had <span class="cn-word" data-pos="verb" data-tr="ekkan edi">planted</span> had grown into anything. He was <strong>not only</strong> strict <strong>but also</strong>, it turned out, more <span class="cn-word" data-pos="adj" data-tr="qiziqqan, eʼtibor bergan">invested</span> in us than any professor I had ever known.</p>
<p>When the colleague read my own paragraph aloud, written more than a decade before that evening, I heard him describe a quiet student in the back row who asked better questions than he <span class="cn-word" data-pos="verb" data-tr="koʻrsatib turgan edi (tashqi koʻrinishda)">let on</span>, and who he <span class="cn-word" data-pos="verb" data-tr="taxmin qilardi">suspected</span> would end up doing something interesting with his life. I sat there in the middle of a room full of strangers, finally understanding a man I had spent fifteen years getting completely wrong.</p>''',
        "grammar": [
            {
                "pattern":  "hardly had ... when (inversion)",
                "meaning":  "...gan zahoti, deyarli ...gan hamono — ikki voqea orasidagi juda qisqa vaqtni urgu bilan bildiradi.",
                "examples": ["Hardly had the speeches ended when a colleague stood up.", "Hardly had I sat down when the phone rang."],
            },
            {
                "pattern":  "provided that + clause",
                "meaning":  "...sharti bilan, agar ... boʻlsa (shart ergash gapi).",
                "examples": ["He gave full marks provided that the reasoning was correct.", "You may leave early, provided that the work is finished."],
            },
            {
                "pattern":  "far from + -ing",
                "meaning":  "...dan yiroq, aslo ... emas (kuchli qarama-qarshilik).",
                "examples": ["Far from being cold, he cared deeply about every student.", "Far from giving up, she worked even harder."],
            },
            {
                "pattern":  "not only ... but also",
                "meaning":  "Nafaqat ..., balki ... ham (ikki fikrni bogʻlab kuchaytiradi).",
                "examples": ["He was not only strict but also deeply devoted.", "She is not only smart but also kind."],
            },
        ],
        "questions": [
            {
                "text": "What reputation did Professor Hall have among students?",
                "choices": [
                    "He was known as an easy grader who never failed anyone",
                    "He was known as brilliant but cold, exacting, and hard to please",
                    "He was known for never attending class",
                ],
                "answer": 1,
                "explanation": "U daho, ammo sovuq va talabchan professor sifatida tanilgan, uni qoniqtirish deyarli mumkin emas edi.",
            },
            {
                "text": "What did the narrator learn at the retirement dinner?",
                "choices": [
                    "The professor had secretly failed most of his students on purpose",
                    "The professor had kept a private notebook following the lives of former students for decades",
                    "The professor was planning to write a book about teaching",
                ],
                "answer": 1,
                "explanation": "Professor oʻttiz yildan ortiq vaqt davomida talabalarining hayoti va faoliyatini kuzatib, ular haqida daftarga yozib borgan ekan.",
            },
            {
                "text": "What is the main lesson of the story?",
                "choices": [
                    "Strict teachers are always right about their students",
                    "A person's cold outward behavior does not always reflect how much they truly care",
                    "Students should always trust their first impression of a teacher",
                ],
                "answer": 1,
                "explanation": "Professorning sovuq tashqi koʻrinishi uning talabalariga chuqur eʼtibor va gʻamxoʻrligini yashirib turgan — tashqi koʻrinish har doim ham haqiqatni aks ettirmaydi.",
            },
        ],
    },
    # ── 12 ───────────────────────────────────────────────────────────────
    {
        "title":   "The Empty Chair",
        "summary": "Restoranda har kuni boʻsh qoladigan stol aslida ochilishdan oldin vafot etgan doʻstga bagʻishlangan kichik marosim ekan.",
        "order":   12,
        "body": '''<p>The restaurant was small, family-run, and always full by seven, except for one table near the window that stayed empty every single night, even when a <span class="cn-word" data-tr="navbat">line</span> of <span class="cn-word" data-pos="adj" data-tr="ochqagan, ochlikdan">hungry</span> customers <span class="cn-word" data-pos="verb" data-tr="choʻzilib ketgan edi">stretched</span> out the door. I asked about it my third visit, half expecting an <span class="cn-word" data-tr="kechirim soʻrash">apology</span> about a broken chair or a <span class="cn-word" data-tr="bron qilish tizimi">reservation system</span> error.</p>
<p>The owner, a <span class="cn-word" data-pos="adj" data-tr="mayin ovozli, kamgap">soft-spoken</span> man named Marco, only smiled and changed the subject, <strong>unless</strong> a customer <span class="cn-word" data-pos="verb" data-tr="qistab soʻradi">pressed</span> him further, which I did, more out of curiosity than <span class="cn-word" data-tr="xushmuomalalik">politeness</span>. Eventually, standing by that table one slow Tuesday evening, he told me the story.</p>
<p>He and his best friend, Enzo, had planned to open the restaurant together, <span class="cn-word" data-pos="verb" data-tr="jamgʻarib">saving</span> money for years, choosing the paint colors and the menu side by side. Enzo died of a <span class="cn-word" data-pos="adj" data-tr="toʻsatdan, kutilmagan">sudden</span> <span class="cn-word" data-tr="kasallik">illness</span> three weeks before opening night, having never once seen the <span class="cn-word" data-pos="adj" data-tr="tugallangan, tayyor">finished</span> <span class="cn-word" data-tr="ovqatlanish zali">dining room</span>. Marco opened anyway, <strong>albeit</strong> with a <span class="cn-word" data-tr="vada">promise</span> he made himself that first morning: one table, always set, always waiting, as though Enzo might still walk through the door.</p>
<p>Every evening before <span class="cn-word" data-pos="verb" data-tr="qulfdan ochish">unlocking</span> the front door, Marco stops at that table for exactly one minute, alone, before the first customer arrives. He does this <strong>so that</strong> he never <span class="cn-word" data-pos="verb" data-tr="unutadi">forgets</span> why he started the restaurant in the first place, and so that some <span class="cn-word" data-pos="adj" data-tr="jimgina, sokin">quiet</span> part of the evening always belongs to his old friend.</p>
<p><strong>The fact that</strong> he never once broke this small <span class="cn-word" data-tr="rasm-rusm, odat">ritual</span>, not on his <span class="cn-word" data-pos="adj" data-tr="eng band">busiest</span> night, not on his hardest one, told me everything I needed to know about the empty chair. It was never really empty at all.</p>''',
        "grammar": [
            {
                "pattern":  "unless + clause",
                "meaning":  "Agar ... boʻlmasa (salbiy shart, 'if not' bilan bir xil).",
                "examples": ["He never explained, unless a customer asked directly.", "I won't go, unless you come with me."],
            },
            {
                "pattern":  "albeit + adjective/phrase",
                "meaning":  "Garchi..., biroq (rasmiy uslubda qisqa qarshi qoʻyish, 'although' oʻrniga).",
                "examples": ["The restaurant thrived, albeit with one table forever empty.", "The plan worked, albeit slowly."],
            },
            {
                "pattern":  "the fact that + clause",
                "meaning":  "...ekanligi (fakti) — ot ergash gapi sifatida ishlatiladi.",
                "examples": ["The fact that he never broke the ritual told me everything.", "The fact that she came at all meant a lot."],
            },
            {
                "pattern":  "so that + clause",
                "meaning":  "...ishi uchun, shu maqsadda (maqsad ergash gapi).",
                "examples": ["He keeps the chair there so that his friend is never forgotten.", "Speak up so that everyone can hear you."],
            },
        ],
        "questions": [
            {
                "text": "Why did the narrator ask about the empty table?",
                "choices": [
                    "It was blocking the entrance to the restaurant",
                    "It stayed empty every night even during the busiest hours",
                    "The waiter refused to seat anyone else",
                ],
                "answer": 1,
                "explanation": "Restoran hamma joyi toʻla boʻlsa ham, bu stol har kuni boʻsh qolar edi, bu muallifning qiziqishini uygʻotdi.",
            },
            {
                "text": "Why does Marco keep one table empty every night?",
                "choices": [
                    "It is required by a city law for restaurants",
                    "It honors his best friend and business partner who died before the restaurant opened",
                    "He is saving it for VIP customers",
                ],
                "answer": 1,
                "explanation": "Stol Marko bilan birga restoran ochishni rejalashtirgan, ammo ochilishdan oldin vafot etgan doʻsti Enzo xotirasiga bagʻishlangan.",
            },
            {
                "text": "What does Marco's nightly ritual at the table represent?",
                "choices": [
                    "A superstition to bring good luck to the restaurant",
                    "A quiet way of remembering why he started the restaurant and honoring his friend",
                    "A marketing strategy to attract curious customers",
                ],
                "answer": 1,
                "explanation": "Har kuni bir daqiqa stol yonida turishi — bu doʻstini eslash va restoranni nima uchun ochganini unutmaslik uchun kichik marosim.",
            },
        ],
    },
]
