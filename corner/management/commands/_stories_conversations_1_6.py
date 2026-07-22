# English "Everyday Conversations" — easy-level (A2-B1) DIALOGUE readings, a new format
# for the English subject: two named characters, strictly alternating turns (one <p> per
# turn, no narration lines), so each speaker can be voiced with a distinct TTS voice via
# gen_corner_audio's --speaker-voices. Topics have real emotional substance (apology,
# grief, encouragement, distance, mental health) rather than shallow "where do you study"
# textbook small talk, while staying grammatically simple/elementary. ~10-14 vocab marks,
# 2 grammar points (basic/elementary structures used naturally in the dialogue), 3
# inference questions per story.
# Import: python manage.py import_corner corner/management/commands/_stories_conversations_1_6.py --author=<AUTHOR>

SUBJECT = {
    "name":    "English",
    "summary": "Ingliz tili: IELTS uslubidagi qiziqarli oʻqish matnlari — lugʻat va grammatika bilan.",
    "icon":    "bi-globe2",
    "color":   "#2563eb",
    "order":   2,
}

COLLECTION = {
    "title":       "Everyday Conversations",
    "description": "Boshlangʻich/oʻrta daraja (A2-B1) — chuqurroq maʼnoli, hayotiy suhbatlar orqali tabiiy grammatikani oʻrganish.",
    "order":       5,
}

STORIES = [
    # ── 1 ────────────────────────────────────────────────────────────────
    {
        "title":   "I'm Sorry I Said That",
        "summary": "Mia jahl ustida Jeykka nohaq gap aytib qoʻyadi — uzr soʻrash va kechirish orqali doʻstlik tiklanadi.",
        "order":   1,
        "body": '''<p><strong>Mia:</strong> Jake, can we talk? I've been <span class="cn-word" data-pos="verb" data-tr="oʻylab yurgan edim">thinking</span> about what I said yesterday.</p>
<p><strong>Jake:</strong> Okay. I'm listening.</p>
<p><strong>Mia:</strong> I <strong>didn't mean to</strong> say you don't <span class="cn-word" data-pos="verb" data-tr="gʻamxoʻrlik qilmoq, ahamiyat bermoq">care</span> about the team. That wasn't <span class="cn-word" data-pos="adj" data-tr="adolatli">fair</span>.</p>
<p><strong>Jake:</strong> It really <span class="cn-word" data-pos="verb" data-tr="ogʻritdi">hurt</span>, Mia. I work hard for this team too.</p>
<p><strong>Mia:</strong> I know. I was <span class="cn-word" data-pos="adj" data-tr="jahli chiqqan">angry</span> about losing the game, and I said something I shouldn't have.</p>
<p><strong>Jake:</strong> I get it. Losing is hard for you. But you can't <span class="cn-word" data-pos="verb" data-tr="ayblamoq">blame</span> me for every mistake.</p>
<p><strong>Mia:</strong> You're right. I'm <span class="cn-word" data-pos="adj" data-tr="afsusda, uzr soʻrayotgan">sorry</span> for <span class="cn-word" data-pos="verb" data-tr="baqirganim uchun">yelling</span> at you in front of everyone.</p>
<p><strong>Jake:</strong> Thank you for saying that. It <span class="cn-word" data-pos="verb" data-tr="ahamiyatga ega">means</span> a lot.</p>
<p><strong>Mia:</strong> Can we <span class="cn-word" data-pos="verb" data-tr="qaytadan boshlamoq">start over</span>? I really want us to be okay.</p>
<p><strong>Jake:</strong> Yeah. <strong>It's okay to</strong> make <span class="cn-word" data-tr="xatolar">mistakes</span> sometimes. Friends <span class="cn-word" data-pos="verb" data-tr="kechirmoq">forgive</span> each other.</p>
<p><strong>Mia:</strong> So... are we good?</p>
<p><strong>Jake:</strong> We're good. Just don't do that again, okay?</p>
<p><strong>Mia:</strong> I <span class="cn-word" data-pos="verb" data-tr="vada beraman">promise</span>. Next time, I'll talk to you first, not yell.</p>
<p><strong>Jake:</strong> Deal. Now let's go get some pizza. I'm <span class="cn-word" data-pos="adj" data-tr="juda ochqagan">starving</span>.</p>
<p><strong>Mia:</strong> Now that sounds like the Jake I know.</p>''',
        "grammar": [
            {
                "pattern":  "I didn't mean to + verb",
                "meaning":  "Bilib-bilmay ...moqchi emas edim (nohaqlikni yumshatish, uzr soʻrash uchun).",
                "examples": ["I didn't mean to say that.", "I didn't mean to hurt you."],
            },
            {
                "pattern":  "It's okay to + verb",
                "meaning":  "...moq yaxshi, ...moqning gʻalati joyi yoʻq (ruxsat yoki tasalli berish uchun).",
                "examples": ["It's okay to make mistakes.", "It's okay to ask for help."],
            },
        ],
        "questions": [
            {
                "text": "Why is Mia apologizing to Jake?",
                "choices": [
                    "She lost the game on purpose",
                    "She said something unfair and yelled at him in front of everyone",
                    "She forgot his birthday",
                ],
                "answer": 1,
                "explanation": "Mia oʻyinni yutqazgani uchun jahli chiqib, Jeykka nohaq gap aytib, hamma oldida baqirgan edi, shuning uchun uzr soʻrayapti.",
            },
            {
                "text": "How does Jake respond to Mia's apology?",
                "choices": [
                    "He refuses to forgive her",
                    "He accepts her apology and says friends forgive each other",
                    "He tells her to leave the team",
                ],
                "answer": 1,
                "explanation": "Jeyk uzrni qabul qiladi va doʻstlar goho xato qilib, bir-birini kechirishini aytadi.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "Winning games is more important than friendship",
                    "Saying sorry and forgiving each other can repair a friendship",
                    "You should never get angry with your friends",
                ],
                "answer": 1,
                "explanation": "Suhbat uzr soʻrash va kechirish doʻstlikni qanday tiklashi mumkinligini koʻrsatadi.",
            },
        ],
    },
    # ── 2 ────────────────────────────────────────────────────────────────
    {
        "title":   "The New Kid",
        "summary": "Yangi maktabda yolgʻiz oʻtirgan Noahga sinfdoshi Zoening kichik samimiy taklifi katta yordam beradi.",
        "order":   2,
        "body": '''<p><strong>Zoe:</strong> Hi, you're new, right? I saw you <span class="cn-word" data-pos="adj" data-tr="yolgʻiz">standing alone</span> at lunch.</p>
<p><strong>Noah:</strong> Yeah... I just <span class="cn-word" data-pos="verb" data-tr="koʻchib keldim">moved</span> here last week. I don't really know anyone yet.</p>
<p><strong>Zoe:</strong> That must be hard. <strong>Have you ever</strong> moved to a new school before?</p>
<p><strong>Noah:</strong> No, never. My old school, I knew everyone since <span class="cn-word" data-tr="bogʻcha">kindergarten</span>.</p>
<p><strong>Zoe:</strong> Wow, that's a big <span class="cn-word" data-tr="oʻzgarish">change</span> then. <strong>Why don't we</strong> sit together tomorrow? My friends are pretty <span class="cn-word" data-pos="adj" data-tr="yaxshi, mehribon">nice</span>.</p>
<p><strong>Noah:</strong> Really? You don't have to do that just because I'm new.</p>
<p><strong>Zoe:</strong> I want to. Everyone needs a <span class="cn-word" data-pos="adj" data-tr="samimiy, doʻstona">friendly</span> face on a hard day.</p>
<p><strong>Noah:</strong> Thanks. <span class="cn-word" data-pos="adv" data-tr="rostini aytsam">Honestly</span>, I was thinking about eating lunch in the library alone again.</p>
<p><strong>Zoe:</strong> Don't do that! Come find me by the big tree near the <span class="cn-word" data-tr="sport zali">gym</span>.</p>
<p><strong>Noah:</strong> Okay. What if your friends don't <span class="cn-word" data-pos="verb" data-tr="yoqtirmasa">like</span> me, though?</p>
<p><strong>Zoe:</strong> Then they're not really my friends. But <span class="cn-word" data-pos="verb" data-tr="ishonmoq">trust</span> me, they will.</p>
<p><strong>Noah:</strong> You're kind of <span class="cn-word" data-pos="adj" data-tr="qatʼiyatli, oʻz fikrida turadigan">persistent</span>, you know that?</p>
<p><strong>Zoe:</strong> My mom calls it "friendly and <span class="cn-word" data-pos="adj" data-tr="qaysar">stubborn</span>." I <span class="cn-word" data-pos="verb" data-tr="afzal koʻraman">prefer</span> "friendly."</p>
<p><strong>Noah:</strong> Well, friendly and stubborn Zoe, I'll see you at the tree tomorrow.</p>
<p><strong>Zoe:</strong> See you there, new kid.</p>''',
        "grammar": [
            {
                "pattern":  "Have you ever + past participle",
                "meaning":  "Hech qachon ...ganmisiz? (hayotiy tajriba haqida savol berish uchun).",
                "examples": ["Have you ever moved to a new school?", "Have you ever tried Korean food?"],
            },
            {
                "pattern":  "Why don't we + verb",
                "meaning":  "Nega ...maylik? (taklif berish uchun soʻzlashuv shakli).",
                "examples": ["Why don't we sit together tomorrow?", "Why don't we ask the teacher?"],
            },
        ],
        "questions": [
            {
                "text": "Why does Zoe talk to Noah?",
                "choices": [
                    "The teacher told her to",
                    "She noticed he was sitting alone and wanted to be kind",
                    "She needed help with homework",
                ],
                "answer": 1,
                "explanation": "Zoe Noahning yolgʻiz oʻtirganini koʻrib, unga doʻstona munosabatda boʻlishni xohlagan.",
            },
            {
                "text": "How does Noah feel about being new?",
                "choices": [
                    "Excited to meet new people right away",
                    "A little lonely, since he doesn't know anyone yet",
                    "Angry about moving to a new school",
                ],
                "answer": 1,
                "explanation": "Noah yangi maktabda hech kimni tanimagani uchun biroz yolgʻiz his qilmoqda.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "New students should always eat lunch alone at first",
                    "A small, kind gesture can make a new student feel welcome",
                    "Friends should always agree with each other",
                ],
                "answer": 1,
                "explanation": "Kichik, samimiy imo-ishora yangi oʻquvchini oʻzini kerakli his qilishga yordam berishi mumkinligini koʻrsatadi.",
            },
        ],
    },
    # ── 3 ────────────────────────────────────────────────────────────────
    {
        "title":   "We Lost Max",
        "summary": "Ella va Sam itlari Maksni yoʻqotgach, xotiralarni birga eslab, gʻam-alamni birga yengishga harakat qilishadi.",
        "order":   3,
        "body": '''<p><strong>Ella:</strong> Sam? Are you okay? You've been in your room all day.</p>
<p><strong>Sam:</strong> Not really. I keep <span class="cn-word" data-pos="verb" data-tr="eshitayotganday tuyulmoq">thinking I hear</span> Max's <span class="cn-word" data-tr="panjalar">paws</span> on the floor.</p>
<p><strong>Ella:</strong> Me too. I almost put food in his <span class="cn-word" data-tr="idish, kosa">bowl</span> this morning without thinking.</p>
<p><strong>Sam:</strong> He <strong>used to</strong> wait by the door every day when we came home from school.</p>
<p><strong>Ella:</strong> I know. The house feels so <span class="cn-word" data-pos="adj" data-tr="jimjit">quiet</span> without him <span class="cn-word" data-pos="verb" data-tr="hurishi">barking</span> at everything.</p>
<p><strong>Sam:</strong> I keep <span class="cn-word" data-pos="verb" data-tr="oʻylab yuraman">wondering</span> if we could have done something different at the vet.</p>
<p><strong>Ella:</strong> Sam, the vet said there was nothing more we could do. <strong>It's okay to feel</strong> sad, but it's not your <span class="cn-word" data-tr="ayb, aybdorlik">fault</span>.</p>
<p><strong>Sam:</strong> It just doesn't feel <span class="cn-word" data-pos="adj" data-tr="haqiqiy">real</span> yet. Twelve years is a long time.</p>
<p><strong>Ella:</strong> It really is. He was <span class="cn-word" data-pos="adv" data-tr="aslida, deyarli">basically</span> part of our family since before I could walk.</p>
<p><strong>Sam:</strong> Remember how he used to <span class="cn-word" data-pos="verb" data-tr="oʻgʻirlamoq">steal</span> socks and <span class="cn-word" data-pos="verb" data-tr="yashirmoq">hide</span> them under the couch?</p>
<p><strong>Ella:</strong> Every single time! Dad was so mad, but it was always <span class="cn-word" data-pos="adj" data-tr="kulgili">funny</span>.</p>
<p><strong>Sam:</strong> I think I want to keep one of his old toys, if that's okay.</p>
<p><strong>Ella:</strong> Of course it is. I already put his <span class="cn-word" data-tr="boʻyinbogʻ (it uchun)">collar</span> in my drawer.</p>
<p><strong>Sam:</strong> We'll be okay, right? <span class="cn-word" data-pos="adv" data-tr="oxir-oqibat">Eventually</span>?</p>
<p><strong>Ella:</strong> Eventually, yeah. It'll always hurt a little, but that's because we loved him a lot.</p>''',
        "grammar": [
            {
                "pattern":  "used to + verb",
                "meaning":  "Ilgari ...gan, avval ...ar edi (oʻtmishdagi odat, hozir yoʻq).",
                "examples": ["He used to wait by the door every day.", "He used to steal socks."],
            },
            {
                "pattern":  "It's okay to feel + adjective",
                "meaning":  "...his qilish yaxshi, ...his qilishning gʻalati joyi yoʻq (his-tuygʻuni tasdiqlash uchun).",
                "examples": ["It's okay to feel sad.", "It's okay to feel nervous before a test."],
            },
        ],
        "questions": [
            {
                "text": "Why does Ella almost put food in Max's bowl?",
                "choices": [
                    "She forgot Max had already eaten",
                    "Out of habit, because she isn't fully used to him being gone",
                    "She wanted to feed a new pet",
                ],
                "answer": 1,
                "explanation": "U hali ham odat boʻyicha, Maksning yoʻqligiga toʻliq koʻnikmagani uchun idishga ovqat solmoqchi boʻlgan.",
            },
            {
                "text": "What does Ella tell Sam about the vet?",
                "choices": [
                    "They should have gone to a different vet",
                    "There was nothing more that could have been done, and it's not his fault",
                    "The vet made a mistake",
                ],
                "answer": 1,
                "explanation": "Ella Samga veterinar hech narsa qila olmasligini va bu uning aybi emasligini aytadi.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "Pets should not be allowed in the house",
                    "Grieving a pet is normal, and sharing memories together can help",
                    "It is better to get a new pet immediately after losing one",
                ],
                "answer": 1,
                "explanation": "Suhbat uy hayvonini yoʻqotish tabiiy holat ekanini va xotiralarni birga eslash yordam berishini koʻrsatadi.",
            },
        ],
    },
    # ── 4 ────────────────────────────────────────────────────────────────
    {
        "title":   "You Can Do This",
        "summary": "Ertangi imtihondan xavotirlangan Leoni onasi tinchlantirib, xavotirlanish tabiiy ekanini tushuntiradi.",
        "order":   4,
        "body": '''<p><strong>Mom:</strong> Leo, you've been <span class="cn-word" data-pos="verb" data-tr="tikilib oʻtiribsan">staring</span> at that book for two hours. Take a <span class="cn-word" data-tr="tanaffus, dam">break</span>.</p>
<p><strong>Leo:</strong> I can't, Mom. <strong>What if</strong> I fail the exam tomorrow?</p>
<p><strong>Mom:</strong> You won't <span class="cn-word" data-pos="verb" data-tr="yiqilmoq (imtihonda)">fail</span>. You've studied every night this week.</p>
<p><strong>Leo:</strong> What if I forget everything the <span class="cn-word" data-tr="zahoti, oʻsha lahzada">second</span> I sit down? That happens sometimes.</p>
<p><strong>Mom:</strong> It might, a little. That's <span class="cn-word" data-pos="adj" data-tr="tabiiy, odatiy">normal</span>. But your brain <span class="cn-word" data-pos="verb" data-tr="eslab qoladi">remembers</span> more than you think.</p>
<p><strong>Leo:</strong> I don't know. Everyone else seems so much more <span class="cn-word" data-pos="adj" data-tr="ishonchli">confident</span> than me.</p>
<p><strong>Mom:</strong> They probably feel exactly like you do. Nobody shows their <span class="cn-word" data-tr="xavotir, tashvish">nerves</span> on the outside.</p>
<p><strong>Leo:</strong> Really? Even Amir? He always looks so <span class="cn-word" data-pos="adj" data-tr="xotirjam">calm</span>.</p>
<p><strong>Mom:</strong> Even Amir. Trust me, confidence is mostly just good <span class="cn-word" data-tr="aktyorlik, oʻzini tutish">acting</span>.</p>
<p><strong>Leo:</strong> That actually helps a little.</p>
<p><strong>Mom:</strong> You <strong>should</strong> get some sleep now. Your brain needs <span class="cn-word" data-tr="dam olish">rest</span> more than more studying tonight.</p>
<p><strong>Leo:</strong> What if I still do <span class="cn-word" data-pos="adv" data-tr="yomon">badly</span>, though, even after all this?</p>
<p><strong>Mom:</strong> Then we'll <span class="cn-word" data-pos="verb" data-tr="hal qilamiz">figure out</span> the next step together, like we always do. But I don't think that's going to happen.</p>
<p><strong>Leo:</strong> Okay. Thanks, Mom.</p>
<p><strong>Mom:</strong> You've got this, Leo. I mean it.</p>''',
        "grammar": [
            {
                "pattern":  "should + verb",
                "meaning":  "...ish kerak, tavsiya etiladi (maslahat berish uchun modal feʼl).",
                "examples": ["You should get some sleep.", "You should ask for help if you need it."],
            },
            {
                "pattern":  "What if + clause",
                "meaning":  "Agar ... boʻlsa-chi? (tashvish yoki ehtimolni bildirish uchun soʻzlashuv shakli).",
                "examples": ["What if I fail the exam?", "What if it rains tomorrow?"],
            },
        ],
        "questions": [
            {
                "text": "Why is Leo staring at his book for so long?",
                "choices": [
                    "He is bored and doesn't want to talk to his mom",
                    "He is nervous and worried about failing his exam tomorrow",
                    "He lost his phone and has nothing else to do",
                ],
                "answer": 1,
                "explanation": "Leo ertangi imtihondan qoʻrqib, xavotirlanib, kitobga uzoq tikilib oʻtiribdi.",
            },
            {
                "text": "What does Leo's mom say about other students like Amir?",
                "choices": [
                    "They never feel nervous before exams",
                    "They probably feel just as nervous, even if they don't show it",
                    "They don't study as hard as Leo does",
                ],
                "answer": 1,
                "explanation": "Ona Amir kabi oʻquvchilar ham xuddi shunday xavotirlanishi mumkinligini, faqat buni tashqariga chiqarmasligini aytadi.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "Studying all night is the best way to prepare for an exam",
                    "It is normal to feel nervous, and rest and encouragement can help before a big challenge",
                    "Parents should always do their children's homework for them",
                ],
                "answer": 1,
                "explanation": "Suhbat xavotirlanish tabiiy ekanini, dam olish va qoʻllab-quvvatlash katta sinovdan oldin yordam berishini koʻrsatadi.",
            },
        ],
    },
    # ── 5 ────────────────────────────────────────────────────────────────
    {
        "title":   "I Miss You Already",
        "summary": "Boshqa shaharga koʻchib ketgan Sofi bilan Greys video qoʻngʻiroqda sogʻinchini ulashib, masofaga qaramay doʻstlikni davom ettirishga qaror qilishadi.",
        "order":   5,
        "body": '''<p><strong>Grace:</strong> Can you hear me okay? The <span class="cn-word" data-tr="aloqa, ulanish">connection</span> keeps <span class="cn-word" data-pos="verb" data-tr="muzlab qolyapti">freezing</span>.</p>
<p><strong>Sophie:</strong> Yeah, I can hear you now. Hi! I miss you already, and it's only been three days.</p>
<p><strong>Grace:</strong> I know. My room feels so <span class="cn-word" data-pos="adj" data-tr="boʻsh">empty</span> without you next door.</p>
<p><strong>Sophie:</strong> <strong>Even though</strong> we talk every day online, it's not the same as walking to your house.</p>
<p><strong>Grace:</strong> Tell me about it. I keep <span class="cn-word" data-pos="adv" data-tr="deyarli">almost</span> texting you to come over, then I remember.</p>
<p><strong>Sophie:</strong> How's the new school, by the way? Have you made any friends yet?</p>
<p><strong>Grace:</strong> Actually, focus on you first. How's the new city <span class="cn-word" data-pos="verb" data-tr="munosabatda boʻlyapti, taʼsir qilyapti">treating</span> you?</p>
<p><strong>Sophie:</strong> Honestly? It's beautiful, but <strong>I wish</strong> I knew more people here.</p>
<p><strong>Grace:</strong> You will. You made friends with me in like five minutes, remember?</p>
<p><strong>Sophie:</strong> True. You <span class="cn-word" data-pos="adv" data-tr="aslida, deyarli">basically</span> <span class="cn-word" data-pos="verb" data-tr="majburladi">forced</span> me to be your friend in third grade.</p>
<p><strong>Grace:</strong> Best <span class="cn-word" data-tr="qaror">decision</span> I ever made, if I do say so myself.</p>
<p><strong>Sophie:</strong> Same here. Okay, tell me everything about school, <span class="cn-word" data-pos="adv" data-tr="jiddiy ravishda">seriously</span>.</p>
<p><strong>Grace:</strong> It's fine. Different, but fine. It's just <span class="cn-word" data-pos="adj" data-tr="gʻalati">weird</span> without you at lunch.</p>
<p><strong>Sophie:</strong> We'll <span class="cn-word" data-pos="verb" data-tr="tashrif buyuramiz">visit</span> each other, right? <span class="cn-word" data-tr="masofa">Distance</span> doesn't end a real friendship.</p>
<p><strong>Grace:</strong> Definitely. Same time next week?</p>
<p><strong>Sophie:</strong> Same time next week. I love you, weirdo.</p>''',
        "grammar": [
            {
                "pattern":  "I wish + past simple",
                "meaning":  "Koshki ... boʻlsa edi (hozirgi holatdan norozilik yoki istakni bildiradi).",
                "examples": ["I wish I knew more people here.", "I wish I had more time."],
            },
            {
                "pattern":  "Even though + clause",
                "meaning":  "...boʻlishiga qaramay (kuchli qarama-qarshilikni bildiradi).",
                "examples": ["Even though we talk every day, it's not the same.", "Even though it was raining, we went outside."],
            },
        ],
        "questions": [
            {
                "text": "Why does Sophie say 'I wish I knew more people here'?",
                "choices": [
                    "She doesn't like her new city at all",
                    "She misses having friends nearby, even though the city is nice",
                    "She wants to move back immediately",
                ],
                "answer": 1,
                "explanation": "Sofi yangi shahar chiroyli boʻlsa-da, atrofida koʻproq odam tanishini istaydi — u yolgʻizlik his qilmoqda.",
            },
            {
                "text": "How did Grace and Sophie become friends?",
                "choices": [
                    "They met online recently",
                    "Sophie basically forced Grace to be friends with her in third grade",
                    "They are cousins",
                ],
                "answer": 1,
                "explanation": "Sofi uchinchi sinfda Greysni deyarli 'majburlab' doʻst qilib olgan.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "Video calls can never replace real friendship",
                    "Even with distance, a real friendship can stay strong through regular connection",
                    "Moving to a new city always ruins old friendships",
                ],
                "answer": 1,
                "explanation": "Suhbat masofaga qaramay, muntazam aloqa orqali haqiqiy doʻstlik davom etishi mumkinligini koʻrsatadi.",
            },
        ],
    },
    # ── 6 ────────────────────────────────────────────────────────────────
    {
        "title":   "It's Okay to Not Be Okay",
        "summary": "Aleks qiynalayotganini yashirsa-da, doʻsti Ben buni sezib, uni tinglab, yoniga tayanch boʻlishini bildiradi.",
        "order":   6,
        "body": '''<p><strong>Ben:</strong> Hey, you've been quiet <span class="cn-word" data-pos="adv" data-tr="soʻnggi paytlarda">lately</span>. Everything good?</p>
<p><strong>Alex:</strong> Yeah, I'm fine. Just tired, I <span class="cn-word" data-pos="verb" data-tr="shekilli, oʻylaymanki">guess</span>.</p>
<p><strong>Ben:</strong> You've said "I'm fine" like five times this week. That's usually not <span class="cn-word" data-pos="adj" data-tr="toʻgʻri, haqiqiy">true</span> with you.</p>
<p><strong>Alex:</strong> I don't know, man. I don't really want to talk about it.</p>
<p><strong>Ben:</strong> You <strong>don't have to</strong> <span class="cn-word" data-pos="verb" data-tr="tushuntirmoq">explain</span> everything. I just want you to know I'm here.</p>
<p><strong>Alex:</strong> It's just... a lot, lately. School, home, everything at once.</p>
<p><strong>Ben:</strong> That sounds <span class="cn-word" data-pos="adj" data-tr="ogʻir">heavy</span>. You don't have to <span class="cn-word" data-pos="verb" data-tr="koʻtarib yurmoq">carry</span> all of that alone.</p>
<p><strong>Alex:</strong> I feel like I should be <span class="cn-word" data-pos="verb" data-tr="uddalamoq, boshqarmoq">handling</span> it better, though. Everyone else seems fine.</p>
<p><strong>Ben:</strong> Everyone <span class="cn-word" data-pos="verb" data-tr="qiynalmoq, kurashmoq">struggles</span> sometimes, even if it doesn't look that way from outside.</p>
<p><strong>Alex:</strong> Maybe. It's hard to <span class="cn-word" data-pos="verb" data-tr="tan olmoq, eʼtirof etmoq">admit</span> when things aren't okay.</p>
<p><strong>Ben:</strong> <strong>It's okay not to</strong> be okay, seriously. That's not <span class="cn-word" data-tr="ojizlik, zaiflik">weakness</span>.</p>
<p><strong>Alex:</strong> Thanks. I think I needed someone to actually say that <span class="cn-word" data-pos="adv" data-tr="ovoz chiqarib">out loud</span>.</p>
<p><strong>Ben:</strong> Anytime. Want to just hang out tonight? No <span class="cn-word" data-tr="bosim, majburiyat">pressure</span> to talk about anything.</p>
<p><strong>Alex:</strong> Yeah, actually. That sounds really good right now.</p>
<p><strong>Ben:</strong> Cool. I'll come by after dinner.</p>''',
        "grammar": [
            {
                "pattern":  "don't have to + verb",
                "meaning":  "...ishing shart emas (majburiyat yoʻqligini bildiradi).",
                "examples": ["You don't have to explain everything.", "You don't have to carry all of that alone."],
            },
            {
                "pattern":  "It's okay not to + verb",
                "meaning":  "...maslik ham yaxshi, ...masangiz ham boʻlaveradi (bosimni yumshatish, tasalli berish uchun).",
                "examples": ["It's okay not to be okay.", "It's okay not to know the answer right away."],
            },
        ],
        "questions": [
            {
                "text": "Why does Ben say Alex's 'I'm fine' isn't convincing?",
                "choices": [
                    "Alex is smiling too much",
                    "Alex has said it many times this week, which isn't usually how he acts",
                    "Alex told him directly that he was lying",
                ],
                "answer": 1,
                "explanation": "Aleks bu haftada besh marta 'yaxshiman' deb aytgan, bu esa odatda uning holatiga mos kelmaydi, shuning uchun Ben shubhalanadi.",
            },
            {
                "text": "What does Ben tell Alex about struggling?",
                "choices": [
                    "He should hide his feelings from everyone",
                    "Everyone struggles sometimes, even if it's not visible from outside",
                    "Only weak people struggle with problems",
                ],
                "answer": 1,
                "explanation": "Ben hamma ham baʼzan qiynalishini, garchi bu tashqaridan koʻrinmasa ham, aytadi.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "Friends should always solve each other's problems immediately",
                    "It's okay to admit you're struggling, and having someone who listens can help",
                    "Talking about feelings is a sign of weakness",
                ],
                "answer": 1,
                "explanation": "Suhbat qiynalayotganingizni tan olish yaxshi ekanini va sizni tinglaydigan doʻst yordam berishi mumkinligini koʻrsatadi.",
            },
        ],
    },
]
