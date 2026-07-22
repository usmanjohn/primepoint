# English "Life Stories" — narrative readings, batch 3 (stories 13-18). Same style as
# batch 1/2: first-person human-interest narratives with a quiet twist/life lesson, in the
# spirit of Keimyung story 20. ~18-22 vocab marks, 3-4 fresh grammar structures per story
# (not repeated from earlier batches — see toc_life_stories.txt header for the used list),
# 3 inference questions each.
# Import: python manage.py import_corner corner/management/commands/_stories_life_13_18.py --author=<AUTHOR>

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
    # ── 13 ───────────────────────────────────────────────────────────────
    {
        "title":   "The Substitute",
        "summary": "Bir kunlik oʻrinbosar oʻqituvchi maktabni tashlab ketishga yaqinlashgan oʻquvchining hayotini oʻzgartirib yuboradi.",
        "order":   13,
        "body": '''<p>I was seventeen and <strong>on the verge of</strong> quitting school altogether the week Mr. Reyes <span class="cn-word" data-pos="verb" data-tr="oʻrniga dars berdi">substituted</span> for our math teacher, though nobody in that classroom knew it, <span class="cn-word" data-pos="adv" data-tr="ayniqsa, eng kamida">least of all</span> him. I had stopped raising my hand months earlier, stopped doing homework, stopped <span class="cn-word" data-pos="verb" data-tr="qiziqmoq, ahamiyat bermoq">caring</span> whether the numbers on the board made sense.</p>
<p>He <span class="cn-word" data-pos="verb" data-tr="payqadi">noticed</span> within the first ten minutes, the way certain teachers just do. When he called on me and I <span class="cn-word" data-pos="verb" data-tr="tuturuqsiz aytdim">muttered</span> that I didn't get it and never would, he didn't move on the way most substitutes did. He walked over, pulled up a chair beside my desk, and worked through the problem with me, slowly, out loud, until something <span class="cn-word" data-pos="verb" data-tr="anglashildi, tushundim">clicked</span> that had <span class="cn-word" data-pos="verb" data-tr="rad etgan edi">refused</span> to click for months.</p>
<p><strong>Before long</strong>, he was doing the same for two other students who had <span class="cn-word" data-pos="verb" data-tr="chetga chiqib ketgan edi">drifted</span> to the back of the room the way I had. He never once made it feel like <span class="cn-word" data-tr="rahm-shafqat, sadaqa">charity</span>. He just kept saying the same thing, <span class="cn-word" data-pos="adv" data-tr="jimgina, sekin">quietly</span>, every time someone got something wrong: "Good, now we know what it isn't. Try again." Class ended, he packed up his single bag of chalk and worksheets, and I never saw him again — our regular teacher came back the next day, and Mr. Reyes <span class="cn-word" data-pos="verb" data-tr="jo'nab ketdi">moved on</span> to whichever school needed him next.</p>
<p>I finished that semester. Then the next one, and eventually a degree in engineering I am fairly sure I would never have finished if not for that one afternoon. <strong>If only</strong> I had asked his first name that day, finding him again wouldn't have taken decades. <strong>Had I known</strong>, at seventeen, that I would spend years <span class="cn-word" data-pos="verb" data-tr="oʻylab yurish">wondering</span> about a substitute teacher's full story, I might have asked more questions while I had the chance.</p>
<p>I finally found him again at a <span class="cn-word" data-tr="hudud, mintaqa">district</span> retirement ceremony decades later, <span class="cn-word" data-pos="verb" data-tr="hurmat bajo keltirib">honoring</span> substitute teachers who had served for twenty-five years or more. Talking with him afterward, I learned he had nearly dropped out himself at sixteen, <span class="cn-word" data-pos="verb" data-tr="qutqargan">saved</span> by a teacher who did exactly what he later made a <span class="cn-word" data-tr="odat">habit</span> of doing for strangers' classrooms for the rest of his career. He didn't <span class="cn-word" data-pos="verb" data-tr="eslay olmadi">remember</span> me <span class="cn-word" data-pos="adv" data-tr="aynan, xususan">specifically</span>, not out of thousands of students over the years, but he smiled anyway when I told him the story, and said it was, in his words, exactly why he kept <span class="cn-word" data-pos="verb" data-tr="kelib turish, qatnashish">showing up</span>.</p>''',
        "grammar": [
            {
                "pattern":  "on the verge of + -ing",
                "meaning":  "...ish arafasida, ...ishga yaqin (biror holatga juda yaqinlashganini bildiradi).",
                "examples": ["I was on the verge of quitting school.", "She was on the verge of tears."],
            },
            {
                "pattern":  "before long",
                "meaning":  "Koʻp oʻtmay, tez orada (vaqt oralig'i qisqaligini bildiruvchi idioma).",
                "examples": ["Before long, he was helping other students too.", "Before long, the rain stopped."],
            },
            {
                "pattern":  "if only + past perfect",
                "meaning":  "Koshki ... boʻlganida (oʻtmishdagi ish uchun afsus/pushaymonlik).",
                "examples": ["If only I had asked his name that day.", "If only I had studied harder."],
            },
            {
                "pattern":  "had I known (inversion, 3rd conditional without 'if')",
                "meaning":  "Bilganimda edi... — rasmiy uslubda 'if I had known' oʻrniga inversiya ishlatiladi.",
                "examples": ["Had I known, I would have asked more questions.", "Had I known the truth, I wouldn't have gone."],
            },
        ],
        "questions": [
            {
                "text": "Why was the narrator on the verge of quitting school before Mr. Reyes substituted the class?",
                "choices": [
                    "He had failed every subject already",
                    "He had stopped caring and disengaged from class months earlier",
                    "His family was moving to another city",
                ],
                "answer": 1,
                "explanation": "Muallif oylar oldin darsga qiziqishni yoʻqotib, faolligini toʻxtatgan edi — bu uni maktabni tashlashga yaqinlashtirgan.",
            },
            {
                "text": "What did Mr. Reyes do differently from other substitutes?",
                "choices": [
                    "He gave the class extra homework",
                    "He sat down with struggling students and worked through problems with them patiently",
                    "He canceled the lesson and let students talk freely",
                ],
                "answer": 1,
                "explanation": "U boshqa oʻrinbosar oʻqituvchilardan farqli oʻlaroq, qiynalayotgan oʻquvchilar bilan sabr-toqat bilan oʻtirib, masalalarni birga yechgan.",
            },
            {
                "text": "What did the narrator learn about Mr. Reyes years later?",
                "choices": [
                    "He had never actually been a real teacher",
                    "He had almost dropped out himself as a teenager and was helped the same way",
                    "He had become a famous mathematician",
                ],
                "answer": 1,
                "explanation": "Mister Reyes oʻzi ham oʻsmirlik davrida maktabni deyarli tashlab ketgan, ammo bir oʻqituvchi xuddi shunday yordam bergani uchun davom ettirgan — keyin shu anʼanani boshqalarga davom ettirgan.",
            },
        ],
    },
    # ── 14 ───────────────────────────────────────────────────────────────
    {
        "title":   "The Music Box",
        "summary": "Buvidan qolgan musiqa qutisidagi tanish boʻlmagan ohang aslida uch avlod davomida oʻtkazilgan oilaviy alla ekan.",
        "order":   14,
        "body": '''<p>The music box <span class="cn-word" data-pos="verb" data-tr="kelib yetdi, keltirildi">arrived</span> in a box of my grandmother's <span class="cn-word" data-tr="mol-mulk, buyumlar">belongings</span>, wrapped <span class="cn-word" data-pos="adv" data-tr="beparvolik bilan">carelessly</span> in a dish towel, as if whoever packed it hadn't understood what it was. It was small, wooden, slightly <span class="cn-word" data-pos="adj" data-tr="egilgan, qiyshaygan">warped</span> at one corner, and when I <span class="cn-word" data-pos="verb" data-tr="burab qoʻydim">wound</span> the tiny key, it played a simple, slightly off-key <span class="cn-word" data-tr="ohang, kuy">melody</span> I did not <span class="cn-word" data-pos="verb" data-tr="tanimadim">recognize</span> at all.</p>
<p>I kept it on a <span class="cn-word" data-tr="javon">shelf</span> mostly for <span class="cn-word" data-tr="sentimental hurmat">sentiment</span>, not thinking much more about the tune itself. <strong>Little by little</strong>, though, I started noticing something strange. My mother, visiting one weekend, <span class="cn-word" data-pos="verb" data-tr="oʻzicha kuylardi">hummed</span> a melody while washing dishes that stopped me completely — the same tune, note for note, though she <span class="cn-word" data-pos="verb" data-tr="qasam ichib aytdi">swore</span> she had never heard the music box play.</p>
<p><span class="cn-word" data-pos="adj" data-tr="qiziqib">Curious</span>, I asked my aunt, the oldest of my mother's <span class="cn-word" data-tr="aka-uka, opa-singillar">siblings</span>, whether the melody meant anything to her. She went quiet for a moment, then said of course it did — it was the <span class="cn-word" data-tr="alla">lullaby</span> every baby in our family had been sung to sleep with for at least three generations, <span class="cn-word" data-pos="verb" data-tr="avloddan-avlodga oʻtkazilgan">passed down</span> by ear, never written anywhere, <strong>not to mention</strong> never once mentioned to any of us directly as anything special.</p>
<p><strong>As good as</strong> forgotten, <span class="cn-word" data-pos="adv" data-tr="shekilli, koʻrinishidan">apparently</span>, since none of us <span class="cn-word" data-pos="verb" data-tr="anglaganmiz">realized</span> we already carried it somewhere. My aunt explained that our grandmother had sung it to my mother, who — without ever <span class="cn-word" data-pos="adv" data-tr="ongli ravishda">consciously</span> learning it — must have <span class="cn-word" data-pos="verb" data-tr="oʻzlashtirgan, singdirgan">absorbed</span> it deeply enough to sing it back to dishes, decades later, without knowing why.</p>
<p><strong>Come to think of it</strong>, I realized I had likely been sung the very same melody as an <span class="cn-word" data-tr="chaqaloq, goʻdak">infant</span> myself, long before I could form any memory of it at all. When my own daughter was born the following spring, I found myself humming it too, without deciding to, the tune arriving before the memory of where it came from ever did.</p>''',
        "grammar": [
            {
                "pattern":  "little by little",
                "meaning":  "Asta-sekin, bir oz-bir oz (bosqichma-bosqich oʻzgarishni bildiradi).",
                "examples": ["Little by little, I started noticing something strange.", "Little by little, her health improved."],
            },
            {
                "pattern":  "as good as + adjective/past participle",
                "meaning":  "Deyarli ..., ... bilan barobar (toʻliq boʻlmasa-da, deyarli shunday holatni bildiradi).",
                "examples": ["The melody was as good as forgotten.", "The work is as good as finished."],
            },
            {
                "pattern":  "not to mention",
                "meaning":  "...ni aytmasa ham boʻladi (qoʻshimcha faktni taʼkidlash uchun).",
                "examples": ["It was never written down, not to mention never explained.", "She's smart, not to mention hardworking."],
            },
            {
                "pattern":  "come to think of it",
                "meaning":  "Rostini aytsam, shunday oʻylab qarasam (birdan xayolga kelgan fikrni kiritish uchun idioma).",
                "examples": ["Come to think of it, I had heard that tune before.", "Come to think of it, we never asked her name."],
            },
        ],
        "questions": [
            {
                "text": "What did the narrator notice about their mother while she was washing dishes?",
                "choices": [
                    "She was singing a song from the radio",
                    "She was humming the exact same melody as the music box, without realizing it",
                    "She was complaining about the old music box",
                ],
                "answer": 1,
                "explanation": "Ona idish yuvayotganda xuddi shu ohangni, oʻzi bilmagan holda kuylayotgan edi — bu muallifni hayratga soldi.",
            },
            {
                "text": "What did the aunt explain about the melody?",
                "choices": [
                    "It was a song their grandmother had made up randomly",
                    "It was the family's lullaby, passed down by ear for at least three generations",
                    "It came from a popular movie their grandmother loved",
                ],
                "answer": 1,
                "explanation": "Bu — kamida uch avlod davomida ogʻzaki tarzda oʻtkazib kelingan oilaviy alla ekan.",
            },
            {
                "text": "What is the main idea of the story?",
                "choices": [
                    "Old music boxes are usually broken and out of tune",
                    "A melody can be carried in memory across generations, even without anyone realizing it",
                    "Grandmothers always leave behind valuable antiques",
                ],
                "answer": 1,
                "explanation": "Ohang hech kim bilmagan holda avloddan-avlodga oʻtib kelgan — bu xotira qanchalik chuqur va sezilmas tarzda saqlanib qolishi mumkinligini koʻrsatadi.",
            },
        ],
    },
    # ── 15 ───────────────────────────────────────────────────────────────
    {
        "title":   "The Rooftop Garden",
        "summary": "Tomdagi bogʻdan hech kim bilmagan holda savatlarda sabzavot tarqatib yuruvchi qoʻshni, oʻzi ham och qolgan bolalikni eslab shunday qiladi.",
        "order":   15,
        "body": '''<p>For two summers, someone had been growing vegetables on the roof of our apartment building, though nobody seemed to know exactly who. Tomatoes <span class="cn-word" data-pos="verb" data-tr="chirmashib oʻsardi">climbed</span> <span class="cn-word" data-pos="adj" data-tr="vaqtinchalik yasalgan">makeshift</span> wooden frames between the water tanks, herbs filled old paint buckets along the <span class="cn-word" data-tr="parapet, chekka">ledge</span>, and every few days, a basket of whatever was <span class="cn-word" data-pos="adj" data-tr="pishgan">ripe</span> appeared near the mailboxes downstairs with a small <span class="cn-word" data-tr="qoʻlda yozilgan">handwritten</span> note: "Take what you need."</p>
<p>I had <strong>all but</strong> given up trying to find out who was <span class="cn-word" data-pos="adj" data-tr="javobgar, aybdor">responsible</span>, <span class="cn-word" data-pos="verb" data-tr="taxmin qilib">assuming</span> it was probably the building manager, or maybe a group of <span class="cn-word" data-tr="ijarachilar">tenants</span> working together. Nobody I asked seemed to know for <span class="cn-word" data-pos="adj" data-tr="aniq, ishonchli">certain</span>, and the baskets kept appearing <span class="cn-word" data-pos="adv" data-tr="baribir, qatʼi nazar">regardless</span>, rain or shine, <span class="cn-word" data-pos="verb" data-tr="gʻoyib boʻlardi">disappearing</span> again within hours.</p>
<p>I finally found out by accident, climbing the roof stairs one early morning to watch the <span class="cn-word" data-tr="quyosh chiqishi">sunrise</span>, something I rarely did. Mrs. Okafor from the fourth floor was already up there, <span class="cn-word" data-pos="verb" data-tr="tizzalab oʻtirib">kneeling</span> beside a <span class="cn-word" data-tr="qator">row</span> of pepper plants, filling a basket <strong>so much so that</strong> tomatoes kept rolling out the sides.</p>
<p>She seemed almost <span class="cn-word" data-pos="adj" data-tr="uyalgan, noqulay">embarrassed</span> to be <span class="cn-word" data-pos="verb" data-tr="fosh qilingan, topilgan">discovered</span>, waving off my questions at first. Eventually, though, she told me she had grown up without always having enough to eat, and gardening now was, <strong>for the sake of</strong> remembering that feeling, her quiet way of making sure nobody nearby ever had to feel it the same way. <strong>Under no circumstances</strong> did she want her name <span class="cn-word" data-pos="verb" data-tr="bogʻlanishi, ulanishi">attached</span> to the baskets, <span class="cn-word" data-pos="adj" data-tr="xavotirlangan">worried</span> it would turn a simple gift into something people felt they had to thank her for, or worse, feel embarrassed accepting.</p>
<p>I never told anyone what I saw that morning, though I did start leaving a small bag of coffee near her door <span class="cn-word" data-pos="adv" data-tr="vaqti-vaqti bilan, goho">occasionally</span>, <span class="cn-word" data-pos="adj" data-tr="imzosiz">unsigned</span>, the same way she left her baskets. Neither of us has ever mentioned it directly. Some mornings, walking past the mailboxes, I still see a fresh basket sitting there, and I think about how much quiet care can hide behind four simple words: take what you need.</p>''',
        "grammar": [
            {
                "pattern":  "all but + verb",
                "meaning":  "Deyarli, aytarli darajada (toʻliq emas, lekin unga juda yaqin holatni bildiradi).",
                "examples": ["I had all but given up finding out who it was.", "The project is all but finished."],
            },
            {
                "pattern":  "so much so that",
                "meaning":  "Shunchalik ...ki, hatto ... (kuchli natijani taʼkidlaydi).",
                "examples": ["She filled the basket so much so that tomatoes rolled out.", "He was tired, so much so that he fell asleep standing."],
            },
            {
                "pattern":  "for the sake of",
                "meaning":  "...ning hotirasi/manfaati uchun, ...deb (maqsad yoki sabab).",
                "examples": ["She gardens for the sake of remembering that feeling.", "He stayed quiet for the sake of peace."],
            },
            {
                "pattern":  "under no circumstances (inversion when fronted)",
                "meaning":  "Hech qanday sharoitda ham ...(emas) — kuchli inkor, gap boshida kelsa ega-feʼl joyi almashadi.",
                "examples": ["Under no circumstances did she want her name attached to it.", "Under no circumstances should you open that door."],
            },
        ],
        "questions": [
            {
                "text": "What had been appearing near the mailboxes for two summers?",
                "choices": [
                    "Advertisements for a local farm",
                    "Baskets of fresh vegetables with a note saying 'Take what you need'",
                    "Complaints about the rooftop garden",
                ],
                "answer": 1,
                "explanation": "Ikki yoz davomida pochta qutilari yonida 'Kerak boʻlgan narsangizni oling' degan yozuv bilan sabzavot savatlari paydo boʻlib turardi.",
            },
            {
                "text": "Why did Mrs. Okafor keep her identity a secret?",
                "choices": [
                    "She was not allowed to garden on the roof officially",
                    "She didn't want people to feel they had to thank her or feel embarrassed accepting the food",
                    "She was planning to sell the vegetables later",
                ],
                "answer": 1,
                "explanation": "U odamlar unga rahmat aytishga majbur his qilishlarini yoki qabul qilishdan uyalib qolishlarini istamagan.",
            },
            {
                "text": "What is the main idea of the story?",
                "choices": [
                    "Rooftop gardens are the best way to save money on food",
                    "Quiet generosity can be given without needing recognition or thanks",
                    "Building managers should organize community gardens",
                ],
                "answer": 1,
                "explanation": "Hikoya hech qanday eʼtirof yoki minnatdorchiliksiz koʻrsatilgan sokin saxovat haqida — bu asosiy gʻoya.",
            },
        ],
    },
    # ── 16 ───────────────────────────────────────────────────────────────
    {
        "title":   "The Voicemail I Never Deleted",
        "summary": "Vafot etgan otasidan qolgan qisqa ovozli xabarni yoʻqotishdan qoʻrqqan muallif, opasi ham xuddi shunday qilganini bilib qoladi.",
        "order":   16,
        "body": '''<p>I switched phones three times in the past decade, and each time, the very first thing I did before anything else was make sure one particular voicemail <span class="cn-word" data-pos="verb" data-tr="omon qoldi, saqlanib qoldi">survived</span> the transfer. It is eleven seconds long, my father's voice <span class="cn-word" data-pos="verb" data-tr="eslatib">reminding</span> me to bring an umbrella before a trip, recorded less than a month before he <span class="cn-word" data-pos="verb" data-tr="vafot etdi">passed away</span> <span class="cn-word" data-pos="adv" data-tr="kutilmaganda">unexpectedly</span>.</p>
<p><strong>On</strong> hearing that my phone <span class="cn-word" data-tr="aloqa operatori">carrier</span> was shutting down its old voicemail system entirely, I felt something close to <span class="cn-word" data-tr="vahima, qoʻrquv">panic</span>. <strong>For fear of</strong> losing those eleven seconds forever, I spent an entire weekend <span class="cn-word" data-pos="verb" data-tr="tadqiq qilib">researching</span> how to <span class="cn-word" data-pos="verb" data-tr="chiqarib olmoq">extract</span> and save the file <span class="cn-word" data-pos="adv" data-tr="doimiy ravishda, butunlay">permanently</span>, calling customer service twice, restarting the process three times when nothing seemed to work.</p>
<p>It felt, at moments, <strong>next to impossible</strong>. The system was <span class="cn-word" data-pos="adj" data-tr="eskirgan">outdated</span>, the export tools barely <span class="cn-word" data-pos="adj" data-tr="ishlaydigan">functional</span>, and every failed <span class="cn-word" data-tr="urinish">attempt</span> made the eleven seconds feel more <span class="cn-word" data-pos="adj" data-tr="nozik, mo'rt">fragile</span> than before, as though I might lose my father's voice a second time simply through some technical error.</p>
<p>I finally <span class="cn-word" data-pos="verb" data-tr="muvaffaqiyatga erishdim">succeeded</span> late that night and, <span class="cn-word" data-pos="adj" data-tr="yengil tortgan">relieved</span> beyond words, called my sister to tell her the whole <span class="cn-word" data-pos="adj" data-tr="murakkab">complicated</span> story. There was a long <span class="cn-word" data-tr="tanaffus, sukut">pause</span> on the line. She admitted, quietly, that she had done the exact same thing herself two years earlier, saving the very same voicemail, and had never once mentioned it to me, <span class="cn-word" data-pos="verb" data-tr="taxmin qilib">assuming</span> I wouldn't understand or would think it strange.</p>
<p><strong>To this day</strong>, we have never actually listened to it together in the same room, though we both still have it saved, <span class="cn-word" data-pos="verb" data-tr="zaxira nusxa qilingan">backed up</span> in three different places each, just in case. Somehow, knowing she carries it too makes the eleven seconds feel less like something fragile I am <span class="cn-word" data-pos="verb" data-tr="himoya qilib, asrab">protecting</span> alone, and more like something we are quietly, separately, still keeping safe for each other.</p>''',
        "grammar": [
            {
                "pattern":  "on + -ing",
                "meaning":  "...gan zahoti, ...gan paytda (bir ish qilinishi bilanoq boshqasi sodir boʻlishini bildiradi).",
                "examples": ["On hearing the news, I felt panic.", "On arriving home, she called her sister."],
            },
            {
                "pattern":  "for fear of/that",
                "meaning":  "...dan qoʻrqib, ...masligi uchun (salbiy oqibatdan qochish sababini bildiradi).",
                "examples": ["For fear of losing it forever, I spent the weekend saving the file.", "She whispered for fear of waking the baby."],
            },
            {
                "pattern":  "next to impossible",
                "meaning":  "Deyarli imkonsiz (kuchli qiyinchilikni bildiruvchi idioma).",
                "examples": ["It felt next to impossible to save the file.", "Finding a parking spot downtown is next to impossible."],
            },
            {
                "pattern":  "to this day",
                "meaning":  "Hozirgacha, shu kungacha (oʻtmishdan hozirgi kungacha davom etayotgan holatni bildiradi).",
                "examples": ["To this day, we have never listened to it together.", "To this day, nobody knows what really happened."],
            },
        ],
        "questions": [
            {
                "text": "Why did the narrator panic when the phone carrier announced it was shutting down the old voicemail system?",
                "choices": [
                    "He was worried about losing important business messages",
                    "He was afraid of losing his late father's eleven-second voicemail forever",
                    "He didn't know how to use a new phone",
                ],
                "answer": 1,
                "explanation": "U otasidan qolgan oʻn bir soniyalik ovozli xabarni abadiy yoʻqotib qoʻyishdan qoʻrqqan.",
            },
            {
                "text": "What did the narrator discover when he called his sister?",
                "choices": [
                    "She had already deleted the voicemail years ago",
                    "She had secretly saved the exact same voicemail herself, two years earlier",
                    "She didn't remember their father's voice at all",
                ],
                "answer": 1,
                "explanation": "Opasi ham xuddi shu ovozli xabarni ikki yil oldin saqlab qoʻygan ekan, lekin buni hech kimga aytmagan.",
            },
            {
                "text": "What is the main idea of the story?",
                "choices": [
                    "Old technology should always be upgraded quickly",
                    "Grief can be carried quietly and separately, yet still connect people who share it",
                    "Voicemail messages are the best way to remember someone",
                ],
                "answer": 1,
                "explanation": "Ikkala aka-uka/opa-uka ham bir xil narsani sezdirmasdan saqlab yurishgan — bu gʻam-alam sezilmasa ham odamlarni birlashtirishi mumkinligini koʻrsatadi.",
            },
        ],
    },
    # ── 17 ───────────────────────────────────────────────────────────────
    {
        "title":   "The Interpreter Who Couldn't Translate Everything",
        "summary": "Kasalxonada tarjimonlik qilayotgan muallif bir soʻzni ingliz tiliga toʻgʻri tarjima qila olmaydi, lekin soʻzsiz tushunish yetarli ekanini anglaydi.",
        "order":   17,
        "body": '''<p>The hospital called me in as an interpreter for Mrs. Petrova, an elderly patient who had been <span class="cn-word" data-pos="verb" data-tr="yotqizilgan, qabul qilingan">admitted</span> after a fall, speaking almost no English and understanding, <strong>as far as</strong> I could tell, only slightly more. I had studied her language for years but had never actually <span class="cn-word" data-pos="verb" data-tr="tarjima qilganman">interpreted</span> in a hospital before, and I arrived <span class="cn-word" data-pos="adj" data-tr="asabiy, xavotirli">nervous</span>, notebook in hand, unsure what to expect.</p>
<p>The medical terms were <span class="cn-word" data-pos="adj" data-tr="oddiy, tushunarli">straightforward</span> enough — I had prepared a list <strong>in case</strong> anything unfamiliar came up, and mostly, my preparation held. What I had not prepared for was the moment the doctor gently explained that her hip <span class="cn-word" data-tr="sinish, singan joy">fracture</span> would likely mean months of difficult <span class="cn-word" data-tr="tuzalish, davolanish">recovery</span>, and Mrs. Petrova, instead of asking a medical question, said a single word in her language that had no direct English <span class="cn-word" data-tr="ekvivalent, muqobil">equivalent</span> at all, something closer to a specific, <span class="cn-word" data-pos="adj" data-tr="achinarli, sizlovchi">aching</span> kind of <span class="cn-word" data-tr="yolgʻizlik">loneliness</span> that dictionaries only <span class="cn-word" data-pos="verb" data-tr="taxminan ifodalaydi">approximate</span>.</p>
<p><strong>No sooner had</strong> I <span class="cn-word" data-pos="verb" data-tr="duduqlanib, qiynalib oʻtdim">stumbled</span> through an attempted <span class="cn-word" data-tr="tarjima">translation</span> <strong>than</strong> I realized how <span class="cn-word" data-pos="adj" data-tr="quruq, sayoz">flat</span> it sounded compared to what she had actually said. The doctor, <span class="cn-word" data-pos="verb" data-tr="sezib, angab">sensing</span> the <span class="cn-word" data-tr="boʻshliq, farq">gap</span>, simply reached over and held her hand for a moment before <span class="cn-word" data-pos="verb" data-tr="davom etishdan oldin">continuing</span>. Mrs. Petrova's shoulders <span class="cn-word" data-pos="verb" data-tr="boʻshashdi">relaxed</span> slightly, and something passed between them that had nothing to do with any language at all.</p>
<p>I kept returning to visit her over the following weeks, less as an <span class="cn-word" data-pos="adj" data-tr="rasmiy">official</span> interpreter and more, <strong>if anything</strong>, as someone who had <span class="cn-word" data-pos="adv" data-tr="tasodifan">accidentally</span> become a friend. Some days we barely spoke; I simply sat with her, translating small comments about the weather or the hospital food, in case she needed anyone at all during the long hours between visits from her family, who lived several hours away.</p>
<p>I never did find an exact English word for what she said that first day. But I <span class="cn-word" data-pos="verb" data-tr="tushundim">understood</span>, eventually, that some of the most important things said in that room were never really about the words at all — they were about someone choosing to stay, to listen, and to hold a hand, whether or not a perfect translation existed.</p>''',
        "grammar": [
            {
                "pattern":  "as far as + clause",
                "meaning":  "...bilishimcha, ...gacha (bilim yoki daraja chegarasini bildiradi).",
                "examples": ["As far as I could tell, she understood only a little.", "As far as I know, the meeting is still on."],
            },
            {
                "pattern":  "in case + clause",
                "meaning":  "...boʻlib qolmasin deb, ehtiyot shart (ehtimoliy holatga tayyorgarlik).",
                "examples": ["I prepared a list in case anything unfamiliar came up.", "Take an umbrella in case it rains."],
            },
            {
                "pattern":  "no sooner had ... than (inversion)",
                "meaning":  "...gan zahoti (ikki voqea orasidagi juda qisqa vaqtni urgu bilan bildiradi, inversiya bilan).",
                "examples": ["No sooner had I finished translating than I realized it sounded flat.", "No sooner had we sat down than the phone rang."],
            },
            {
                "pattern":  "if anything",
                "meaning":  "Aksincha, aslida (oldingi fikrni kuchaytirish yoki biroz qarshi qoʻyish uchun).",
                "examples": ["I became, if anything, more like a friend than an interpreter.", "The situation is, if anything, getting better."],
            },
        ],
        "questions": [
            {
                "text": "What made the moment with Mrs. Petrova difficult to interpret?",
                "choices": [
                    "She spoke too quietly to be heard",
                    "She used a word for a feeling that had no direct English equivalent",
                    "The doctor spoke too quickly to translate",
                ],
                "answer": 1,
                "explanation": "U oʻz tilida ingliz tilida toʻgʻridan-toʻgʻri muqobili yoʻq, alohida bir yolgʻizlik tuygʻusini ifodalovchi soʻz ishlatgan.",
            },
            {
                "text": "What did the doctor do when the translation felt inadequate?",
                "choices": [
                    "He asked the narrator to try translating again more carefully",
                    "He simply held Mrs. Petrova's hand for a moment without needing words",
                    "He called for another interpreter",
                ],
                "answer": 1,
                "explanation": "Doktor tarjima yetarli emasligini his qilib, shunchaki bir lahza uning qoʻlini ushlab turdi — soʻzsiz tushunish.",
            },
            {
                "text": "What is the main idea of the story?",
                "choices": [
                    "Professional interpreters should always find an exact word for every feeling",
                    "Real connection between people can happen even when perfect translation is impossible",
                    "Hospitals should hire more interpreters",
                ],
                "answer": 1,
                "explanation": "Hikoya soʻzlar yetarli boʻlmasa ham, odamlar orasida haqiqiy aloqa paydo boʻlishi mumkinligini koʻrsatadi — bu asosiy gʻoya.",
            },
        ],
    },
    # ── 18 ───────────────────────────────────────────────────────────────
    {
        "title":   "The Spare Key",
        "summary": "Yillar oldin 'ehtiyot shart' berilgan zaxira kalit, aynan kerak boʻlgan kunda qoʻshnining hayotini saqlab qoladi.",
        "order":   18,
        "body": '''<p>Mrs. Yamada gave me a <span class="cn-word" data-tr="zaxira, ortiqcha">spare</span> key to her apartment the same week I moved in next door, <span class="cn-word" data-pos="verb" data-tr="qistirdi, tutqazdi">pressing</span> it into my palm before I had even finished <span class="cn-word" data-pos="verb" data-tr="tanishtirish">introducing</span> myself. "Just in case," she said, <span class="cn-word" data-pos="verb" data-tr="rad etib, chetga surib">waving off</span> my <span class="cn-word" data-pos="adj" data-tr="hayron, chalkash">confused</span> thanks, "<strong>otherwise</strong>, what's the point of having a neighbor at all?"</p>
<p>I dropped the key into a kitchen drawer and, if I am honest, <span class="cn-word" data-pos="verb" data-tr="unutib qoʻydim">forgot</span> about it almost entirely for the next four years. We waved at each other in the hallway, occasionally shared vegetables from her small balcony garden, and lived the <span class="cn-word" data-pos="adj" data-tr="qulay, oddiy">comfortable</span>, mostly <span class="cn-word" data-pos="adj" data-tr="alohida">separate</span> lives of neighbors in a busy building.</p>
<p>Then, one ordinary Tuesday, I noticed her newspaper had <span class="cn-word" data-pos="verb" data-tr="uyilib qolgan edi">piled up</span> outside her door for two straight days, something that had never happened before in all the years I had known her. I knocked. No answer. I called her number, <span class="cn-word" data-pos="verb" data-tr="roʻyxatga olingan, yozilgan">listed</span> on a card she had given me alongside the key. No answer there either.</p>
<p><strong>As luck would have it</strong>, I happened to be working from home that <span class="cn-word" data-pos="adj" data-tr="aynan shu, oʻsha">particular</span> week instead of traveling for work, the way I usually was on weekdays. I found the spare key exactly where I had left it years earlier, <span class="cn-word" data-pos="verb" data-tr="oʻzim kirdim">let myself in</span>, and found her on the kitchen floor, having <span class="cn-word" data-pos="verb" data-tr="yiqilgan edi">fallen</span> the previous evening, <span class="cn-word" data-pos="adj" data-tr="ojiz, qodir emas">unable</span> to reach her phone.</p>
<p>The <span class="cn-word" data-tr="tez yordam mashinasi">ambulance</span> arrived <strong>in no time</strong> once I called, and she <span class="cn-word" data-pos="verb" data-tr="tuzaldi">recovered</span> fully within a few weeks, though she likes to <span class="cn-word" data-pos="verb" data-tr="eslatadi">remind</span> me, only half-joking, that she gave me that key for exactly this reason and had simply been waiting four years for me to finally prove <span class="cn-word" data-pos="adj" data-tr="foydali">useful</span>. I have kept a spare key of my own ready for her ever since, <span class="cn-word" data-pos="verb" data-tr="yashiringan, qoʻyilgan">tucked</span> in the same drawer, <span class="cn-word" data-pos="adv" data-tr="endi ... emas">no longer</span> forgotten.</p>''',
        "grammar": [
            {
                "pattern":  "otherwise",
                "meaning":  "Aks holda, boʻlmasa (agar oldingi shart bajarilmasa nima boʻlishini bogʻlaydi).",
                "examples": ["Otherwise, what's the point of having a neighbor?", "Hurry up, otherwise we'll be late."],
            },
            {
                "pattern":  "as luck would have it",
                "meaning":  "Baxtga qarshi/baxtdanmi (tasodifiy, kutilmagan mos kelishni bildiruvchi idioma).",
                "examples": ["As luck would have it, I was home that week.", "As luck would have it, the shop was still open."],
            },
            {
                "pattern":  "in no time",
                "meaning":  "Juda tez, koʻz ochib-yumguncha (juda qisqa vaqt ichida sodir boʻlishini bildiradi).",
                "examples": ["The ambulance arrived in no time.", "The work was finished in no time."],
            },
            {
                "pattern":  "no longer",
                "meaning":  "Endi ...emas (avval boʻlgan, hozir esa toʻxtagan holatni bildiradi).",
                "examples": ["The key was no longer forgotten.", "She no longer lives in that city."],
            },
        ],
        "questions": [
            {
                "text": "Why did Mrs. Yamada give the narrator a spare key when they first moved in?",
                "choices": [
                    "She was going on a long vacation and needed someone to check her mail",
                    "She said it was simply what neighbors do, 'just in case'",
                    "She was too old to use her own key anymore",
                ],
                "answer": 1,
                "explanation": "U kalitni oddiygina 'ehtiyot shart, qoʻshni boʻlishning maʼnosi shunda' deb tutqazgan edi.",
            },
            {
                "text": "What made the narrator realize something was wrong?",
                "choices": [
                    "Mrs. Yamada called asking for help",
                    "Her newspaper had piled up outside her door for two days, unlike her usual habits",
                    "A neighbor told the narrator directly",
                ],
                "answer": 1,
                "explanation": "Uning gazetasi eshigi oldida ikki kun davomida uyilib qolgani — bu hech qachon boʻlmagan holat — muallifni xavotirga solgan.",
            },
            {
                "text": "What is the main idea of the story?",
                "choices": [
                    "Elderly neighbors should always live with family instead of alone",
                    "A small act of trust between neighbors, kept for years, can matter enormously when an emergency finally comes",
                    "Spare keys should never be given to neighbors for safety reasons",
                ],
                "answer": 1,
                "explanation": "Yillar davomida saqlangan kichik ishonch — zaxira kalit — favqulodda vaziyatda judayam muhim ahamiyat kasb etdi.",
            },
        ],
    },
]
