# English "Life Stories" — narrative, human-interest readings in the style of the
# Keimyung Korean readings (long-form, first-person/close narratives with a life lesson
# or a quiet twist), NOT the short "wow-fact" style of Easy/Medium/Advanced Reads.
# Story text = English; vocab/grammar/explanations in Uzbek. Richer vocabulary (~20-25
# marks), 3-4 real grammar structures per story, 3 inference questions per story.
# Import: python manage.py import_corner corner/management/commands/_stories_life_1_6.py --author=<AUTHOR>

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
    # ── 1 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Umbrella at Gate 14",
        "summary": "Yomgʻirli kechada notanish ayoldan olingan soyabon muallifga kichik yaxshilikni davom ettirishni oʻrgatadi.",
        "order":   1,
        "body": '''<p>I <span class="cn-word" data-pos="verb" data-tr="sayohat qilaman, borib turaman">travel</span> for work more than I would like to admit, and after ten years of layovers and delayed flights, very little still <span class="cn-word" data-pos="verb" data-tr="ajablantiradi">surprises</span> me. But one evening at Gate 14, something happened that I still think about whenever it rains.</p>
<p>My connecting flight had been <span class="cn-word" data-pos="verb" data-tr="bekor qilingan edi">cancelled</span> without warning, and the airport staff could only tell me to wait for the next available seat. Outside, rain <span class="cn-word" data-pos="verb" data-tr="taqillatib urardi">hammered</span> against the windows, and inside, the terminal grew <span class="cn-word" data-pos="adj" data-tr="jimjit, sokin">quieter</span> as flight after flight <span class="cn-word" data-pos="verb" data-tr="yoʻqolib bordi">disappeared</span> from the board. I found a seat near Gate 14 and tried to calm down, though <span class="cn-word" data-tr="asabiylashish, xafagarchilik">frustration</span> kept <span class="cn-word" data-pos="verb" data-tr="qaytib kelaverardi">creeping back</span>.</p>
<p>An elderly woman was sitting a few seats away, <span class="cn-word" data-pos="adv" data-tr="xotirjam, sokin">calmly</span> knitting as if the <span class="cn-word" data-tr="tartibsizlik, notinchlik">chaos</span> around her did not exist. When I finally <span class="cn-word" data-pos="verb" data-tr="tan oldim">admitted</span>, mostly to myself, that I might be <span class="cn-word" data-pos="adj" data-tr="qolib ketgan">stuck</span> here all night, she looked up and asked whether I had a way home once I <span class="cn-word" data-pos="verb" data-tr="qoʻndim">landed</span>. I told her no — my car was at a different airport entirely, and by the time I arrived it would surely be pouring.</p>
<p><strong>Without</strong> <span class="cn-word" data-pos="verb" data-tr="ikkilanmoq">hesitating</span>, she reached into her bag and pulled out a small folding umbrella. "Take this," she said, "so that you don't arrive home <span class="cn-word" data-pos="adj" data-tr="hoʻl boʻlgan">soaked</span>." I tried to <span class="cn-word" data-pos="verb" data-tr="rad etmoq">refuse</span>, but she <span class="cn-word" data-pos="verb" data-tr="qistab, majburlab tutqazdi">pressed</span> it into my hands and told me a story instead. Years earlier, <span class="cn-word" data-pos="adj" data-tr="qolib ketgan, garovda qolgan">stranded</span> in a storm herself, a stranger had lent her an umbrella and refused to take it back, saying only, "Give it to someone else someday." She had <span class="cn-word" data-pos="verb" data-tr="olib yurgan">carried</span> a <span class="cn-word" data-pos="adj" data-tr="zaxira, ortiqcha">spare</span> umbrella in her bag ever since, waiting for her turn.</p>
<p>I did fly out that night, hours late, and I did use her umbrella in the rain. But what stayed with me was <strong>not</strong> the umbrella itself — <strong>it was</strong> the idea that a small <span class="cn-word" data-tr="mehribonlik, yaxshilik">kindness</span>, <strong>once received</strong>, does not have to end with you. Since that evening at Gate 14, I have kept a spare umbrella in my own bag. So far I have <span class="cn-word" data-pos="verb" data-tr="berib yubordim, hadya qildim">given</span> it away twice, both times to <span class="cn-word" data-tr="notanish odamlar">strangers</span> as wet and <span class="cn-word" data-pos="adj" data-tr="charchagan">tired</span> as I once was.</p>''',
        "grammar": [
            {
                "pattern":  "without + -ing",
                "meaning":  "Biror narsani qilmasdan turib (holat ergash gapi).",
                "examples": ["Without hesitating, she reached into her bag.", "He left without saying goodbye."],
            },
            {
                "pattern":  "not X but Y",
                "meaning":  "X emas, balki Y — urgu berish/qarama-qarshi qoʻyish uchun ishlatiladi.",
                "examples": ["What stayed with me was not the umbrella itself — it was the idea.", "It was not luck but hard work that saved them."],
            },
            {
                "pattern":  "once + past participle",
                "meaning":  "...langach, ...boʻlgach — qisqargan ergash gap (once + it is/was received kabi qismlar tushirilgan).",
                "examples": ["A kindness, once received, does not have to end with you.", "Once finished, the report was sent immediately."],
            },
        ],
        "questions": [
            {
                "text": "Why did the elderly woman give the narrator her umbrella?",
                "choices": [
                    "Because she had two umbrellas and did not need both",
                    "Because a stranger once gave her an umbrella and told her to pass on the kindness",
                    "Because the airport asked passengers to share umbrellas",
                ],
                "answer": 1,
                "explanation": "Ayol yillar oldin oʻzi bir notanish odamdan soyabon olgan, u esa buni birovga berishni aytgan — ayol shu anʼanani davom ettirmoqda.",
            },
            {
                "text": "What does the narrator do now because of that evening?",
                "choices": [
                    "He avoids taking flights when it rains",
                    "He always carries a spare umbrella and has given it away twice",
                    "He collects umbrellas from different airports",
                ],
                "answer": 1,
                "explanation": "Voqeadan keyin muallif oʻzi ham sumkasida zaxira soyabon olib yuradi va uni ikki marta boshqalarga bergan.",
            },
            {
                "text": "What is the main idea of the story?",
                "choices": [
                    "Flight delays are always someone's fault",
                    "A small act of kindness can be passed from person to person",
                    "It is better to travel without an umbrella",
                ],
                "answer": 1,
                "explanation": "Hikoya kichik yaxshilik bir odamdan ikkinchisiga oʻtib, davom etib borishi mumkinligini koʻrsatadi.",
            },
        ],
    },
    # ── 2 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Silent Piano",
        "summary": "Buzuq deb oʻylangan pianino aslida hech qachon buzilmagan edi — u faqat kutayotgan edi.",
        "order":   2,
        "body": '''<p>My grandmother's piano stood in the same corner of the living room <strong>for as long as</strong> I could remember, but nobody ever <span class="cn-word" data-pos="verb" data-tr="tegmoq, qoʻl tekkizmoq">touched</span> it. Its lid stayed closed, a thin layer of <span class="cn-word" data-tr="chang">dust</span> <span class="cn-word" data-pos="verb" data-tr="toʻplanib borardi">settling</span> over the wood every year. My mother always said it was <span class="cn-word" data-pos="adj" data-tr="buzuq, ishlamaydigan">broken</span>, and none of us thought to <span class="cn-word" data-pos="verb" data-tr="shubha ostiga olmoq">question</span> her.</p>
<p>When my grandmother <span class="cn-word" data-pos="verb" data-tr="vafot etdi">passed away</span> last spring, my mother and I spent a weekend <span class="cn-word" data-pos="verb" data-tr="tozalab, boʻshatib">clearing out</span> the old house. I found myself standing in front of the piano, <span class="cn-word" data-pos="adj" data-tr="qiziqib qolgan">curious</span> for the first time in my life. I lifted the lid, half expecting broken strings or missing keys. Instead, the keys looked <span class="cn-word" data-pos="adj" data-tr="tegilmagan, sof">untouched</span>, almost new. I <span class="cn-word" data-pos="verb" data-tr="bosdim">pressed</span> one down, <span class="cn-word" data-pos="adv" data-tr="ohista, ehtiyotkorlik bilan">gently</span>, <span class="cn-word" data-pos="verb" data-tr="tayyorlanib, taxminan kutib">bracing</span> for silence or an ugly, out-of-tune sound.</p>
<p>A soft, clear <span class="cn-word" data-tr="ohang, tovush">note</span> <span class="cn-word" data-pos="verb" data-tr="toʻldirdi">filled</span> the room. I pressed another, and another. Nothing was broken at all. <span class="cn-word" data-pos="adj" data-tr="hayron, aqli shoshgan">Confused</span>, I called my mother over, and she stood <span class="cn-word" data-pos="adj" data-tr="qotib qolgan, muzlab qolgan">frozen</span> in the doorway, staring at the piano <strong>as though</strong> she were seeing a <span class="cn-word" data-tr="arvoh">ghost</span>.</p>
<p>She finally <span class="cn-word" data-pos="verb" data-tr="tushuntirdi">explained</span>. My grandmother had stopped playing the day my grandfather died, more than twenty years earlier. It had been his favorite sound in the house, and after he was gone, she could not <span class="cn-word" data-pos="verb" data-tr="oʻzini majburlay olmadi">bring herself</span> to fill the <span class="cn-word" data-tr="sukunat, jimlik">silence</span> he had left behind. <strong>Rather than</strong> <span class="cn-word" data-pos="verb" data-tr="sotmoq">sell</span> the piano or give it away, she simply closed the lid and let everyone believe it no longer <span class="cn-word" data-pos="verb" data-tr="ishlardi">worked</span>. It was <span class="cn-word" data-pos="adj" data-tr="osonroq">easier</span>, my mother said, than explaining why she never wanted to hear it again.</p>
<p>I sat down and played the only song I <span class="cn-word" data-pos="verb" data-tr="esladim, xotirladim">remembered</span> from childhood lessons, slowly, with my mother standing beside me. The piano had never been broken. It had only been <span class="cn-word" data-pos="verb" data-tr="kutib turgan edi">waiting</span>, all those years, for someone <span class="cn-word" data-pos="adj" data-tr="jasur, botir">brave</span> <strong>enough to</strong> open the lid — and for a house <span class="cn-word" data-pos="adj" data-tr="tayyor">ready</span> to hear music again.</p>''',
        "grammar": [
            {
                "pattern":  "for as long as + clause",
                "meaning":  "Eslay olganimcha, hamisha — bir holat qachondan buyon davom etganini bildiradi.",
                "examples": ["The piano stood there for as long as I could remember.", "For as long as I've known her, she has loved music."],
            },
            {
                "pattern":  "as though + past (subjunctive)",
                "meaning":  "Xuddi ...dagandek (aslida unday emasligini bildiradi).",
                "examples": ["She stared at the piano as though she were seeing a ghost.", "He acted as though nothing had happened."],
            },
            {
                "pattern":  "rather than + verb/-ing",
                "meaning":  "...dan koʻra, ...ish oʻrniga (tanlov, qarshilik).",
                "examples": ["Rather than sell the piano, she simply closed the lid.", "Rather than complaining, try to fix it."],
            },
            {
                "pattern":  "adjective + enough to + verb",
                "meaning":  "...ish uchun yetarlicha ... (imkoniyat yoki qobiliyatni bildiradi).",
                "examples": ["It had waited for someone brave enough to open the lid.", "She was strong enough to carry the box alone."],
            },
        ],
        "questions": [
            {
                "text": "Why did everyone believe the piano was broken?",
                "choices": [
                    "Because the grandmother told them it no longer worked",
                    "Because the piano was missing several keys",
                    "Because a repairman said it could not be fixed",
                ],
                "answer": 0,
                "explanation": "Buvi hammani pianino buzuq deb ishontirgan, aslida u shunchaki uni chalishni toʻxtatgan edi.",
            },
            {
                "text": "Why had the grandmother really stopped playing the piano?",
                "choices": [
                    "She could not remember how to play anymore",
                    "It had been her husband's favorite sound, and she could not bear the silence after he died",
                    "The piano was too old and out of tune",
                ],
                "answer": 1,
                "explanation": "Bobo vafot etgach, uning sevimli tovushini eshitishga toqati yetmagani uchun buvi pianinoni chalmay qoʻygan.",
            },
            {
                "text": "What is the main idea of the story?",
                "choices": [
                    "Old pianos are usually impossible to repair",
                    "Something that looks broken may only be waiting, hiding a story behind its silence",
                    "Grandmothers should always teach their grandchildren piano",
                ],
                "answer": 1,
                "explanation": "Pianino hech qachon buzilmagan — u faqat kutgan; buzuqlik faqat tashqi koʻrinish, ortida chuqur hikoya yashiringan.",
            },
        ],
    },
    # ── 3 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Wrong Building",
        "summary": "Notoʻgʻri binoga kirib qolgan yigit umidini yoʻqotadi, biroq aynan shu xato unga kutilmagan ish taklif qiladi.",
        "order":   3,
        "body": '''<p>I was twenty minutes early for the most important interview of my life, standing outside a glass office tower downtown, <span class="cn-word" data-pos="verb" data-tr="qayta koʻrib chiqmoq">going over</span> my answers one last time. The <span class="cn-word" data-tr="qabul xodimi">receptionist</span> on the fourteenth floor looked at me <span class="cn-word" data-pos="adv" data-tr="gʻalati tarzda">strangely</span> when I gave the company name. "I'm sorry," she said, "nobody by that name works in this building." My <span class="cn-word" data-tr="yuragim orqaga tortib ketdi">stomach dropped</span>.</p>
<p>I <span class="cn-word" data-pos="verb" data-tr="tekshirdim">checked</span> the address again. I had <span class="cn-word" data-pos="verb" data-tr="koʻchirib olgan edim">copied</span> it correctly from the email, but somehow I had walked into the wrong tower — there were two buildings with <span class="cn-word" data-pos="adj" data-tr="deyarli bir xil">identical</span> names on the same street, three blocks apart. <strong>By the time</strong> I <span class="cn-word" data-pos="verb" data-tr="anglab yetdim">realized</span> my mistake, I had exactly six minutes to get to the right one. I ran the whole way, arriving <span class="cn-word" data-pos="adj" data-tr="nafasi qisilgan">out of breath</span>, my shirt sticking to my back, my carefully <span class="cn-word" data-pos="adj" data-tr="mashq qilingan, tayyorlangan">rehearsed</span> answers <span class="cn-word" data-pos="verb" data-tr="tarqalib ketgan">scattered</span> somewhere in my head.</p>
<p>The actual interview was a <span class="cn-word" data-tr="ofat, falokat">disaster</span>. I <span class="cn-word" data-pos="verb" data-tr="duduqlanib qoldim">stumbled</span> over basic questions and could not stop <span class="cn-word" data-pos="verb" data-tr="uzr soʻrash">apologizing</span> for being late. I left certain I had <span class="cn-word" data-pos="verb" data-tr="barbod qilgan edim">ruined</span> my only chance.</p>
<p><strong>What I did not expect was</strong> a phone call two days later — not from that company, but from a small design studio on the fourteenth floor of the wrong building. The receptionist there had <span class="cn-word" data-pos="verb" data-tr="tilga olgan edi">mentioned</span> my visit to her manager, who <strong>happened to</strong> be looking for someone with <span class="cn-word" data-pos="adv" data-tr="aynan">exactly</span> my <span class="cn-word" data-tr="tajriba, malaka">background</span>. Would I be <strong>willing to</strong> come in for a conversation, no interview required?</p>
<p>I took the job at that <span class="cn-word" data-pos="adj" data-tr="mitti, juda kichik">tiny</span> studio instead, and five years later I still work there. Every time someone asks how I found the place, I tell them the truth: I got <span class="cn-word" data-pos="adv" data-tr="umidsizlarcha, mutlaqo">hopelessly</span> lost, walked into the wrong building, and somehow <span class="cn-word" data-pos="verb" data-tr="oxir-oqibat topib oldim">ended up</span> exactly where I was supposed to be.</p>''',
        "grammar": [
            {
                "pattern":  "by the time + clause",
                "meaning":  "...gunga qadar, ...gan paytga kelib (bir voqea tugagunga qadar boshqasi sodir boʻlishi).",
                "examples": ["By the time I realized my mistake, I had exactly six minutes left.", "By the time we arrived, the meeting had already started."],
            },
            {
                "pattern":  "what + clause + was ... (cleft sentence)",
                "meaning":  "Urgu berish uchun ishlatiladigan tuzilma: '...gan narsa shu edi ki...'.",
                "examples": ["What I did not expect was a phone call two days later.", "What surprised me most was how calm she was."],
            },
            {
                "pattern":  "happen to + verb",
                "meaning":  "Tasodifan ...moq, ...gan ekan (kutilmagan mos kelish).",
                "examples": ["The manager happened to be looking for someone with my background.", "I happened to meet an old friend on the street."],
            },
            {
                "pattern":  "willing to + verb",
                "meaning":  "...ishga tayyor, rozi (istak/roziliкni bildiradi).",
                "examples": ["Would I be willing to come in for a conversation?", "She was willing to help without being asked."],
            },
        ],
        "questions": [
            {
                "text": "Why couldn't the narrator find the company at first?",
                "choices": [
                    "The company had moved to a different city",
                    "There were two buildings with almost identical names nearby",
                    "The interview had been cancelled",
                ],
                "answer": 1,
                "explanation": "Bir xil nomga yaqin nomli ikkita bino koʻchada bor edi, u shulardan notoʻgʻrisiga kirib ketgan.",
            },
            {
                "text": "How did the narrator end up getting a job?",
                "choices": [
                    "The original company hired him despite being late",
                    "A manager at the wrong building heard about his visit and called him",
                    "He applied to the design studio online later",
                ],
                "answer": 1,
                "explanation": "Notoʻgʻri binodagi qabul xodimi uning tashrifini menejerga aytib bergan, u esa aynan shunday tajribaga ega odam qidirayotgan edi.",
            },
            {
                "text": "What is the main lesson of the story?",
                "choices": [
                    "Always double-check an address before an interview",
                    "A mistake can accidentally lead to an unexpected opportunity",
                    "Interviews are not important for getting a job",
                ],
                "answer": 1,
                "explanation": "Xato bino orqali kelib chiqqan tanishuv kutilmagan ish imkoniyatiga olib keldi — xato baʼzan yaxshilikka aylanadi.",
            },
        ],
    },
    # ── 4 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Last Bus Home",
        "summary": "Oxirgi avtobusdan qolgan yigitga bekatda notanish erkak yordam beradi — bu voqea unga notanishlarga ishonishni oʻrgatadi.",
        "order":   4,
        "body": '''<p>It was almost midnight when I ran for the last bus and <strong>watched</strong> it <strong>pull away</strong> from the <span class="cn-word" data-tr="yoʻlning chekkasi">curb</span> without me. I stood there in the cold, phone battery nearly <span class="cn-word" data-pos="adj" data-tr="oʻlgan, tugagan">dead</span>, wallet nearly <span class="cn-word" data-pos="adj" data-tr="boʻsh">empty</span> after a long trip, and no clear way to get across the city before morning.</p>
<p>I sat down on the bench at the empty <span class="cn-word" data-tr="bekat">station</span>, trying to think of someone I could call. That was when a man about my father's age sat down at the other end of the bench, holding two coffees. He <span class="cn-word" data-pos="verb" data-tr="taklif qildi">offered</span> me one without a word of <span class="cn-word" data-tr="tushuntirish">explanation</span>, as if it were the most <span class="cn-word" data-pos="adj" data-tr="oddiy, tabiiy">normal</span> thing in the world.</p>
<p>We talked for a while — about nothing important, really, just the kind of conversation <span class="cn-word" data-tr="notanish odamlar">strangers</span> have when there is nothing else to do but wait. <span class="cn-word" data-pos="adv" data-tr="oxir-oqibat">Eventually</span> he asked where I needed to go, and when I told him, he said it was on his way and offered me a <span class="cn-word" data-tr="mashinada olib borish">ride</span>. I <span class="cn-word" data-pos="verb" data-tr="ikkilandim">hesitated</span>, <strong>the way</strong> anyone would with a stranger at midnight, but something about him <span class="cn-word" data-pos="verb" data-tr="tinchlantirdi, hotirjam qildi">put me at ease</span>, and I <span class="cn-word" data-pos="verb" data-tr="qabul qildim, rozi boʻldim">accepted</span>.</p>
<p>He <span class="cn-word" data-pos="verb" data-tr="tushirib qoʻydi">dropped</span> me <span class="cn-word" data-pos="adv" data-tr="aynan">exactly</span> where I needed to be, <span class="cn-word" data-pos="verb" data-tr="rad etdi">refused</span> any money for gas, and drove off before I had even finished thanking him. I never <span class="cn-word" data-pos="verb" data-tr="bilib oldim">learned</span> his name or saw him again. For years <span class="cn-word" data-pos="adv" data-tr="keyinchalik">afterward</span>, whenever someone <span class="cn-word" data-pos="verb" data-tr="shikoyat qildi">complained</span> that people in big cities were cold and <span class="cn-word" data-pos="adj" data-tr="yordam berishni istamaydigan">unwilling</span> to help each other, I thought of that stranger and his two coffees, and I said nothing, because I knew better.</p>
<p>Now, whenever I see someone <span class="cn-word" data-pos="adj" data-tr="qolib ketgan, iloji yoʻq">stranded</span> late at night, I try to do for them what he did for me — <strong>not because</strong> I expect anything back, <strong>but because</strong> I still remember exactly how it felt to be the one waiting alone in the cold.</p>''',
        "grammar": [
            {
                "pattern":  "watch/see/hear + object + base verb",
                "meaning":  "Sezish feʼllaridan (watch, see, hear) keyin infinitiv 'to' siz keladi — jarayonni toʻliq koʻrish/eshitishni bildiradi.",
                "examples": ["I watched it pull away.", "She heard him close the door."],
            },
            {
                "pattern":  "the way + clause",
                "meaning":  "...gandek, xuddi ...dagidek (tarz ergash gapi).",
                "examples": ["I hesitated, the way anyone would with a stranger.", "She smiled the way her mother used to."],
            },
            {
                "pattern":  "not because ... but because ...",
                "meaning":  "... uchun emas, balki ... uchun (sabab qarama-qarshiligi).",
                "examples": ["I help them not because I expect anything back, but because I remember how it felt.", "He studied not because he had to, but because he wanted to."],
            },
            {
                "pattern":  "whenever + clause",
                "meaning":  "Har safar ...ganda (takrorlanuvchi holat).",
                "examples": ["Whenever I see someone stranded at night, I try to help.", "Whenever it rains, I think of that evening."],
            },
        ],
        "questions": [
            {
                "text": "What did the man do when he sat down next to the narrator?",
                "choices": [
                    "He asked the narrator for money",
                    "He offered the narrator one of his two coffees without explanation",
                    "He called the police",
                ],
                "answer": 1,
                "explanation": "U hech qanday tushuntirishsiz ikkita qahvadan birini muallifga taklif qilgan.",
            },
            {
                "text": "Why did the narrator accept the ride even though he hesitated?",
                "choices": [
                    "He had no other choice at all",
                    "Something about the man made him feel at ease",
                    "The man showed him official identification",
                ],
                "answer": 1,
                "explanation": "Matnda erkak haqida nimadir uni tinchlantirgani va shu sabab taklifni qabul qilgani aytiladi.",
            },
            {
                "text": "What does the narrator do now, and why?",
                "choices": [
                    "He avoids talking to strangers at bus stations",
                    "He helps stranded strangers at night because he remembers how it felt to wait alone",
                    "He always carries two coffees with him",
                ],
                "answer": 1,
                "explanation": "Muallif oʻzi yolgʻiz kutib turishni qanday his qilganini eslab, endi tunda qolib ketganlarga yordam berishga harakat qiladi.",
            },
        ],
    },
    # ── 5 ────────────────────────────────────────────────────────────────
    {
        "title":   "My Neighbor's Garden",
        "summary": "Qoʻshnisining tartibsiz bogʻini beparvolik deb hukm qilgan muallif, aslida u koʻzi ojiza ekanini bilib, xatosini anglaydi.",
        "order":   5,
        "body": '''<p>For the first few months after I moved in, I could not understand my next-door neighbor's garden. Every other yard on the street was <span class="cn-word" data-pos="adj" data-tr="tekis kesilgan, ozoda">trimmed</span>, the <span class="cn-word" data-tr="butalar (toʻsiq shaklidagi)">hedges</span> cut into straight lines, the grass <span class="cn-word" data-pos="verb" data-tr="oʻrilgan">mowed</span> in <span class="cn-word" data-pos="adj" data-tr="ozoda, tartibli">tidy</span> rows. Hers looked <span class="cn-word" data-pos="adj" data-tr="yovvoyi, tartibsiz">wild</span> — flowers growing wherever they pleased, tall grass <span class="cn-word" data-pos="verb" data-tr="tegib turardi">brushing</span> against the fence, <span class="cn-word" data-tr="chirmovuq oʻsimliklar">vines</span> climbing in every direction.</p>
<p>I <span class="cn-word" data-pos="verb" data-tr="taxmin qildim">assumed</span> she simply did not care, and honestly, I <span class="cn-word" data-pos="verb" data-tr="hukm chiqardim">judged</span> her for it. One evening I saw her kneeling among the flowers, running her hands slowly over the leaves <strong>rather than</strong> looking at them, and I realized something was different. <strong>It was only later</strong>, from another neighbor, that I learned she had <span class="cn-word" data-pos="verb" data-tr="koʻrish qobiliyatini yoʻqotgan">lost her sight</span> almost a decade earlier.</p>
<p><span class="cn-word" data-pos="adj" data-tr="qiziquvchan">Curious</span> and <strong>more than a little</strong> <span class="cn-word" data-pos="adj" data-tr="uyalgan, xijolatda">ashamed</span> of my earlier <span class="cn-word" data-tr="hukm, xulosa">judgment</span>, I introduced myself properly the following weekend. She laughed <span class="cn-word" data-pos="adv" data-tr="samimiy, iliq">warmly</span> when I admitted that I had assumed the garden was <span class="cn-word" data-pos="adj" data-tr="eʼtiborsiz qoldirilgan, qarovsiz">neglected</span>. "I don't grow it to look a certain way," she explained. "I grow it to smell and feel a certain way." She walked me through the yard, naming each plant by its <span class="cn-word" data-tr="hid">scent</span> — mint here, jasmine there, roses further along the fence — <span class="cn-word" data-pos="verb" data-tr="joylashtirgan, tartibga solgan">arranging</span> them not for how they would <span class="cn-word" data-pos="verb" data-tr="koʻrinishi uchun">appear</span> from the street but for how they would <span class="cn-word" data-pos="verb" data-tr="ochilib, his qilinishi uchun">unfold</span> to someone who could only touch and smell them.</p>
<p>What had looked <span class="cn-word" data-pos="adj" data-tr="beparvo qilingan, eʼtiborsiz">careless</span> to me was, in fact, <span class="cn-word" data-pos="adv" data-tr="ehtiyotkorlik bilan">carefully</span> planned around <span class="cn-word" data-tr="sezgilar">senses</span> I rarely thought to <span class="cn-word" data-pos="verb" data-tr="tayanmoq">rely on</span>. I had judged an entire garden by a single sense, forgetting that the person who built it was not seeing it the same way I was.</p>
<p>I still cut my own grass in straight lines, out of <span class="cn-word" data-tr="odat">habit</span> more than anything else. But I never again assume that something looks wrong <strong>just because</strong> it is not what I expected to see.</p>''',
        "grammar": [
            {
                "pattern":  "it was only later that + clause",
                "meaning":  "Faqat keyinroq ...ekanini bildim — kechikkan tushunishni urgu bilan bildiradi.",
                "examples": ["It was only later that I learned she had lost her sight.", "It was only later that he understood his mistake."],
            },
            {
                "pattern":  "rather than + -ing",
                "meaning":  "...dan koʻra, ...ish oʻrniga.",
                "examples": ["She was running her hands over the leaves rather than looking at them.", "Rather than judging, I decided to ask her directly."],
            },
            {
                "pattern":  "just because + clause",
                "meaning":  "Faqat ...boʻlgani uchun — asossiz xulosaga qarshi ogohlantirish uchun ishlatiladi.",
                "examples": ["I never assume something looks wrong just because it is not what I expected.", "Don't judge a book just because its cover looks old."],
            },
            {
                "pattern":  "more than a little + adjective",
                "meaning":  "Ancha, kam emas — his-tuygʻuni kuchaytirish uchun.",
                "examples": ["I was more than a little ashamed of my judgment.", "She was more than a little surprised by the news."],
            },
        ],
        "questions": [
            {
                "text": "Why did the narrator's neighbor's garden look different from the others on the street?",
                "choices": [
                    "She could not afford a gardener",
                    "She is blind and arranged the garden by scent and touch rather than appearance",
                    "She was growing it for a competition",
                ],
                "answer": 1,
                "explanation": "U koʻrish qobiliyatini yoʻqotgan va bogʻni koʻrinishiga emas, hid va teginish tuygʻusiga qarab tartibga solgan.",
            },
            {
                "text": "What did the narrator assume before learning the truth?",
                "choices": [
                    "That his neighbor simply did not care about her garden",
                    "That his neighbor was too busy to garden",
                    "That his neighbor was planning to move away",
                ],
                "answer": 0,
                "explanation": "Muallif dastlab qoʻshnisi bogʻga eʼtibor bermayapti, deb notoʻgʻri xulosa chiqargan edi.",
            },
            {
                "text": "What is the main lesson the narrator learns?",
                "choices": [
                    "Gardens should always be trimmed and tidy",
                    "Something can look wrong simply because it was not made for the same senses the viewer relies on",
                    "Blind people cannot take care of gardens",
                ],
                "answer": 1,
                "explanation": "Muallif bir narsani faqat oʻzi koʻrgan tarzda baholab, uni yaratgan odam boshqa sezgilarga tayangan ekanini unutgani haqida saboq oladi.",
            },
        ],
    },
    # ── 6 ────────────────────────────────────────────────────────────────
    {
        "title":   "Two Left Gloves",
        "summary": "Xato sotib olingan ikkita chap qoʻlqop yigitni yangi doʻstlar va jamiyat topishga olib keladi.",
        "order":   6,
        "body": '''<p>The winter market was crowded and <span class="cn-word" data-pos="adj" data-tr="muzdek, ayozli">freezing</span>, and my hands had gone <span class="cn-word" data-pos="adj" data-tr="qotib qolgan, sezgisi yoʻqolgan">numb</span> long before I found the glove <span class="cn-word" data-tr="doʻkoncha, rasta">stall</span> tucked between a bread seller and a man selling <span class="cn-word" data-pos="adj" data-tr="qovurilgan">roasted</span> chestnuts. I <span class="cn-word" data-pos="verb" data-tr="ushlab oldim">grabbed</span> the first pair that looked warm enough, paid quickly, and <span class="cn-word" data-pos="verb" data-tr="shoshildim">hurried</span> home without checking them <span class="cn-word" data-pos="adv" data-tr="diqqat bilan, toʻliq">properly</span>.</p>
<p>It was only that evening, pulling them on to take out the trash, that I <span class="cn-word" data-pos="verb" data-tr="payqadim">noticed</span> something was wrong. Both gloves were meant for the left hand. I <span class="cn-word" data-pos="verb" data-tr="titkiladim, axtardim">dug through</span> the bag and the <span class="cn-word" data-tr="chek">receipt</span>, <span class="cn-word" data-pos="adj" data-tr="jahli chiqqan, achchiqlangan">annoyed</span> at myself for not looking closely, and decided to go back the next morning to <span class="cn-word" data-pos="verb" data-tr="almashtirmoq">exchange</span> them.</p>
<p>The market was <span class="cn-word" data-pos="adj" data-tr="tinchroq, jimroq">quieter</span> the next day, and the same <span class="cn-word" data-tr="rasta egasi, sotuvchi">stallholder</span> <span class="cn-word" data-pos="verb" data-tr="tanidi">recognized</span> me immediately. <strong>Before</strong> I could even explain, he <span class="cn-word" data-pos="verb" data-tr="uzr soʻradi">apologized</span> and began searching through his boxes for a matching pair. While he searched, an <span class="cn-word" data-pos="adj" data-tr="keksa">elderly</span> customer beside me laughed and said she had made the exact same mistake the week before — apparently the stallholder <span class="cn-word" data-pos="verb" data-tr="aralashtirib yuborgan">mixed up</span> his boxes <strong>often enough that</strong> it had become something of a joke among his <span class="cn-word" data-pos="adj" data-tr="doimiy, muntazam">regular</span> customers.</p>
<p>We ended up talking while we waited, and by the time my new gloves were found, she had <span class="cn-word" data-pos="verb" data-tr="taklif qildi">invited</span> me to a weekly <span class="cn-word" data-tr="yigʻilish, uchrashuv">gathering</span> at the community center nearby, one I had walked past a hundred times without ever going inside. I went that Saturday mostly out of <span class="cn-word" data-tr="qiziqish">curiosity</span>, and I am still going, years later. I have made closer friends there than anywhere else in this city.</p>
<p>I sometimes think about how none of it <strong>would have happened if</strong> I had simply checked my gloves before leaving the stall that first evening. The mistake that annoyed me for one cold night <strong>turned out to be</strong> the reason I found a second home in this city.</p>''',
        "grammar": [
            {
                "pattern":  "before + subject + could + verb",
                "meaning":  "...ulgurmasdanoq, ...dan oldin (tezkor voqealar ketma-ketligi).",
                "examples": ["Before I could even explain, he apologized.", "Before she could answer, the phone rang."],
            },
            {
                "pattern":  "adjective/adverb + enough that + clause",
                "meaning":  "Shunchalik ...ki, natijada ... (natija ergash gapi).",
                "examples": ["He mixed up his boxes often enough that it became a joke.", "It was cold enough that the lake froze."],
            },
            {
                "pattern":  "would have + past participle + if + past perfect (3rd conditional)",
                "meaning":  "Agar ...boʻlganida edi, ...boʻlmas edi — oʻtmishdagi noreal shartni bildiradi.",
                "examples": ["None of it would have happened if I had simply checked my gloves.", "I would have called you if I had known you were in town."],
            },
            {
                "pattern":  "turn out to be",
                "meaning":  "...ekan boʻlib chiqdi, natijada ... boʻldi (kutilmagan natija).",
                "examples": ["The mistake turned out to be the reason I found a second home.", "The stranger turned out to be an old classmate."],
            },
        ],
        "questions": [
            {
                "text": "What mistake did the narrator make at the market?",
                "choices": [
                    "He paid too much money for the gloves",
                    "He bought two gloves for the same hand without checking them",
                    "He forgot his wallet at home",
                ],
                "answer": 1,
                "explanation": "U qoʻlqoplarni tekshirmasdan sotib olgan va ikkalasi ham chap qoʻl uchun ekan.",
            },
            {
                "text": "How did the narrator end up meeting new friends?",
                "choices": [
                    "Through a friend who already knew them",
                    "By chance, while waiting to exchange his mismatched gloves at the market",
                    "At a job interview",
                ],
                "answer": 1,
                "explanation": "U qoʻlqoplarni almashtirish uchun qaytib borganda, kutib turgan paytida keksa xaridor bilan suhbatlashib, uni yigʻilishga taklif qilgan.",
            },
            {
                "text": "What is the main idea of the story?",
                "choices": [
                    "Always double-check items before leaving a shop",
                    "A small mistake can unexpectedly lead to something valuable, like new friendships",
                    "Winter markets are dangerous places to shop",
                ],
                "answer": 1,
                "explanation": "Kichik xato (notoʻgʻri qoʻlqop) muallifni yangi doʻstlar va jamiyat topishga olib kelgan — xatolar goho yaxshilikka aylanadi.",
            },
        ],
    },
]
