# English "Everyday Conversations" — batch 2 (stories 7-12). Same format as batch 1
# (_stories_conversations_1_6.py): two named characters, strictly alternating turns (one
# <p> per turn, no narration lines) so gen_corner_audio's --speaker-voices can voice each
# speaker distinctly. Easy/elementary level (A2-B1), real emotional substance (social
# comparison, bullying, sportsmanship, a grandparent's decline, honesty, immigrant pride)
# rather than shallow textbook small talk. ~10-14 vocab marks, 2 fresh grammar points
# (not repeated from batch 1), 3 inference questions per story.
# Import: python manage.py import_corner corner/management/commands/_stories_conversations_7_12.py --author=<AUTHOR>

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
    # ── 7 ────────────────────────────────────────────────────────────────
    {
        "title":   "You Don't Have to Be Perfect",
        "summary": "Ijtimoiy tarmoqlarda oʻzini boshqalar bilan solishtirib qiynalayotgan Emmaga doʻsti Liam tanaffus olishni maslahat beradi.",
        "order":   7,
        "body": '''<p><strong>Emma:</strong> Liam, can I ask you something? Do you ever look at Instagram and just feel... not <span class="cn-word" data-pos="adj" data-tr="yetarli, munosib">good enough</span>?</p>
<p><strong>Liam:</strong> Honestly? All the time. Why, what's going on?</p>
<p><strong>Emma:</strong> Everyone in my class looks so <span class="cn-word" data-pos="adj" data-tr="mukammal">perfect</span> online. Perfect grades, perfect vacations, perfect everything.</p>
<p><strong>Liam:</strong> Emma, nobody's life is <strong>as</strong> perfect <strong>as</strong> it looks in photos. You know that, right?</p>
<p><strong>Emma:</strong> I know that, <span class="cn-word" data-pos="adv" data-tr="mantiqan">logically</span>. But it doesn't stop me from <span class="cn-word" data-pos="verb" data-tr="taqqoslamoq">comparing</span> myself to them.</p>
<p><strong>Liam:</strong> Have you thought about just taking a <span class="cn-word" data-tr="tanaffus">break</span> from it for a while?</p>
<p><strong>Emma:</strong> Maybe. I guess I should <strong>stop scrolling</strong> every time I feel <span class="cn-word" data-pos="adj" data-tr="zerikkan">bored</span> or sad.</p>
<p><strong>Liam:</strong> That might actually help. My sister <span class="cn-word" data-pos="verb" data-tr="oʻchirib tashladi">deleted</span> the app for a month last year.</p>
<p><strong>Emma:</strong> Really? What happened?</p>
<p><strong>Liam:</strong> She said she felt so much happier. <span class="cn-word" data-pos="adv" data-tr="maʼlum boʻlishicha">Turns out</span> comparing yourself to strangers all day isn't great for anyone.</p>
<p><strong>Emma:</strong> That <span class="cn-word" data-pos="verb" data-tr="mantiqqa toʻgʻri keladi">makes sense</span>. I just feel like I'm <span class="cn-word" data-pos="verb" data-tr="qoldirib ketmoq (imkoniyatni)">missing out</span> if I'm not on it.</p>
<p><strong>Liam:</strong> You're not missing much, trust me. Real life is way more <span class="cn-word" data-pos="adj" data-tr="qiziqarli">interesting</span> than a feed.</p>
<p><strong>Emma:</strong> Okay, I'll try it. One week without checking, starting tomorrow.</p>
<p><strong>Liam:</strong> I'm <span class="cn-word" data-pos="adj" data-tr="faxrlanadigan">proud</span> of you for even trying. Call me if you get bored, we'll do something fun.</p>
<p><strong>Emma:</strong> Deal. Thanks for listening, Liam.</p>''',
        "grammar": [
            {
                "pattern":  "as + adjective + as",
                "meaning":  "...dek, ...kabi (ikki narsani solishtirish uchun ishlatiladi).",
                "examples": ["Nobody's life is as perfect as it looks in photos.", "This test wasn't as hard as I expected."],
            },
            {
                "pattern":  "stop + -ing",
                "meaning":  "...ishni toʻxtatmoq (davom etayotgan harakatni toʻxtatishni bildiradi).",
                "examples": ["I should stop scrolling when I feel bored.", "Stop worrying about it."],
            },
        ],
        "questions": [
            {
                "text": "Why does Emma feel bad when she looks at Instagram?",
                "choices": [
                    "She doesn't have any followers",
                    "She compares her life to the 'perfect' lives she sees online",
                    "Her phone is too old to use the app well",
                ],
                "answer": 1,
                "explanation": "Emma sinfdoshlarining internetdagi 'mukammal' hayotini oʻzi bilan solishtirib, oʻzini yetarli emasday his qiladi.",
            },
            {
                "text": "What did Liam's sister do, and what happened?",
                "choices": [
                    "She got more followers by posting every day",
                    "She deleted the app for a month and felt much happier",
                    "She started a new social media account",
                ],
                "answer": 1,
                "explanation": "Liamning singlisi ilovani bir oyga oʻchirib tashlagan va ancha baxtliroq his qilgan.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "Everyone's life on social media is completely real",
                    "Comparing yourself to others online can hurt your happiness, and taking a break can help",
                    "You should never use social media at all",
                ],
                "answer": 1,
                "explanation": "Suhbat internetda oʻzini boshqalar bilan solishtirish baxtga zarar yetkazishi mumkinligini va tanaffus foydali boʻlishini koʻrsatadi.",
            },
        ],
    },
    # ── 8 ────────────────────────────────────────────────────────────────
    {
        "title":   "I Saw What Happened",
        "summary": "Do'stlarini uyalatgan voqeani koʻrgan Priya va Marcus jim turish oʻrniga birga oʻqituvchiga xabar berishga qaror qilishadi.",
        "order":   8,
        "body": '''<p><strong>Priya:</strong> Marcus, did you see what happened at lunch today? With Tommy?</p>
<p><strong>Marcus:</strong> Yeah... those guys were pretty <span class="cn-word" data-pos="adj" data-tr="qattiqqoʻl, shafqatsiz">harsh</span> with him. I saw it too.</p>
<p><strong>Priya:</strong> I <strong>should have said</strong> something. I just stood there and did nothing.</p>
<p><strong>Marcus:</strong> I felt the same way. It happened so fast, I didn't know what to do.</p>
<p><strong>Priya:</strong> Tommy looked really <span class="cn-word" data-pos="adj" data-tr="xafa boʻlgan">upset</span> walking away. I keep thinking about it.</p>
<p><strong>Marcus:</strong> Should we <span class="cn-word" data-pos="verb" data-tr="xabar bermoq">tell</span> someone? Like a teacher?</p>
<p><strong>Priya:</strong> I think we're <strong>supposed to</strong> <span class="cn-word" data-pos="verb" data-tr="xabar qilmoq, maʼlum qilmoq">report</span> things like that, actually. It's in the school <span class="cn-word" data-tr="qoidalar">rules</span>.</p>
<p><strong>Marcus:</strong> You're right. It felt <span class="cn-word" data-pos="adj" data-tr="notoʻgʻri">wrong</span> just watching and not doing anything.</p>
<p><strong>Priya:</strong> Let's go talk to Mrs. Alvarez together, right now, before we <span class="cn-word" data-pos="verb" data-tr="jasoratimizni yoʻqotmoq">lose our nerve</span>.</p>
<p><strong>Marcus:</strong> Okay. What if the other guys find out we <span class="cn-word" data-pos="verb" data-tr="ustidan shikoyat qildik">told on</span> them, though?</p>
<p><strong>Priya:</strong> Honestly, I'd rather <span class="cn-word" data-pos="verb" data-tr="hal qilmoq, yuzlashmoq">deal with</span> that than watch someone get hurt again and stay <span class="cn-word" data-pos="adj" data-tr="jim, sukut saqlagan">silent</span>.</p>
<p><strong>Marcus:</strong> That's fair. Tommy would probably do the same for us.</p>
<p><strong>Priya:</strong> Exactly. Come on, she's still in her classroom.</p>
<p><strong>Marcus:</strong> Okay, let's go. I'm <span class="cn-word" data-pos="adj" data-tr="xursand">glad</span> we're doing this together.</p>
<p><strong>Priya:</strong> Me too. It's easier when you're not the only one <span class="cn-word" data-pos="verb" data-tr="ovoz koʻtarmoq, gapirmoq">speaking up</span>.</p>''',
        "grammar": [
            {
                "pattern":  "should have + past participle",
                "meaning":  "...ishim kerak edi (oʻtmishda qilinmagan ish uchun afsusni bildiradi).",
                "examples": ["I should have said something.", "You should have called me."],
            },
            {
                "pattern":  "be supposed to + verb",
                "meaning":  "...ishi kerak, shunday kutiladi (qoida yoki kutilgan majburiyatni bildiradi).",
                "examples": ["We're supposed to report things like that.", "You're supposed to wear a helmet."],
            },
        ],
        "questions": [
            {
                "text": "How did Priya and Marcus feel about not helping Tommy right away?",
                "choices": [
                    "They felt proud of staying out of it",
                    "They felt they should have said something instead of just watching",
                    "They didn't notice what happened at all",
                ],
                "answer": 1,
                "explanation": "Ular Tommyga darhol yordam bermaganidan afsusda, nimadir deyishlari kerak edi deb his qilishadi.",
            },
            {
                "text": "What do Priya and Marcus decide to do?",
                "choices": [
                    "Ignore what happened and move on",
                    "Report what they saw to a teacher together",
                    "Confront the bullies themselves",
                ],
                "answer": 1,
                "explanation": "Ular birga oʻqituvchi Alvarezga borib, koʻrganlarini xabar qilishga qaror qilishadi.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "It's always safer to stay silent about bullying",
                    "Speaking up about bullying is easier and more meaningful when done together",
                    "Teachers cannot help with bullying problems",
                ],
                "answer": 1,
                "explanation": "Suhbat birgalikda ovoz koʻtarish yolgʻiz jim turishdan koʻra osonroq va maʼnoliroq ekanini koʻrsatadi.",
            },
        ],
    },
    # ── 9 ────────────────────────────────────────────────────────────────
    {
        "title":   "It Wasn't Fair, But...",
        "summary": "Muhim oʻyinni notoʻgʻri hakamlik tufayli yutqazgan Jordan va Casey, hafsalasi pir boʻlishni tabiiy qabul qilib, jamoadagi yutuqlarni ham eslashadi.",
        "order":   9,
        "body": '''<p><strong>Jordan:</strong> I still can't believe we lost. That last call was completely <span class="cn-word" data-pos="adj" data-tr="notoʻgʻri">wrong</span>.</p>
<p><strong>Casey:</strong> I know, that <span class="cn-word" data-tr="qoida buzilishi">foul</span> definitely should have been called on their player, not us.</p>
<p><strong>Jordan:</strong> Exactly! Now we're out of the <span class="cn-word" data-tr="turnir">tournament</span> because of one bad <span class="cn-word" data-tr="qaror">decision</span>.</p>
<p><strong>Casey:</strong> It's <span class="cn-word" data-pos="adj" data-tr="asabga tegadigan">frustrating</span>. But <strong>even if</strong> the ref made a mistake, we still had chances to win.</p>
<p><strong>Jordan:</strong> I guess. We did <span class="cn-word" data-pos="verb" data-tr="oʻtkazib yubordik">miss</span> those two easy shots in the second half.</p>
<p><strong>Casey:</strong> Right. <strong>No matter what</strong>, blaming the referee won't <span class="cn-word" data-pos="verb" data-tr="oʻzgartirmoq">change</span> the result now.</p>
<p><strong>Jordan:</strong> You're right, I know. I'm just really <span class="cn-word" data-pos="adj" data-tr="hafsalasi pir boʻlgan">disappointed</span>. We worked so hard all season.</p>
<p><strong>Casey:</strong> Me too. But losing like this doesn't <span class="cn-word" data-pos="verb" data-tr="oʻchirib tashlamoq">erase</span> everything good we did this year.</p>
<p><strong>Jordan:</strong> I know that logically, it just doesn't feel that way right now.</p>
<p><strong>Casey:</strong> That's okay. It's <span class="cn-word" data-pos="adj" data-tr="ruxsat etilgan, joiz">allowed</span> to hurt for a while.</p>
<p><strong>Jordan:</strong> Thanks for not just telling me to <span class="cn-word" data-pos="verb" data-tr="unutib, oʻtib ketmoq">get over it</span> immediately.</p>
<p><strong>Casey:</strong> Never. Feelings take time. But I really am proud of this team, win or lose.</p>
<p><strong>Jordan:</strong> Same here, honestly. Let's get some food, my treat. We <span class="cn-word" data-pos="verb" data-tr="munosib boʻldik">earned</span> it either way.</p>
<p><strong>Casey:</strong> Now that's the best idea you've had all day.</p>''',
        "grammar": [
            {
                "pattern":  "even if + clause",
                "meaning":  "... boʻlsa ham (kuchli shart; natija baribir oʻzgarmasligini bildiradi).",
                "examples": ["Even if the ref made a mistake, we still had chances to win.", "Even if it's hard, keep trying."],
            },
            {
                "pattern":  "no matter what",
                "meaning":  "Nima boʻlishidan qatʼi nazar (shart-sharoitdan qatʼi nazar bir xil natija/munosabatni bildiradi).",
                "examples": ["No matter what, blaming the referee won't change the result.", "No matter what happens, I'll support you."],
            },
        ],
        "questions": [
            {
                "text": "What do Jordan and Casey disagree about at first, and then agree on?",
                "choices": [
                    "Whether the referee's call was fair",
                    "Whether blaming the referee will actually change what happened",
                    "Whether they should quit the team",
                ],
                "answer": 1,
                "explanation": "Ular avval hakamning notoʻgʻri qarori haqida gaplashishadi, lekin oxir-oqibat hakamni ayblash natijani oʻzgartirmasligiga kelishib olishadi.",
            },
            {
                "text": "What does Casey say about Jordan's disappointment?",
                "choices": [
                    "He should get over it immediately",
                    "It's allowed to hurt for a while, and feelings take time",
                    "He is overreacting about a small loss",
                ],
                "answer": 1,
                "explanation": "Keysi Jordanga hafsalasi pir boʻlishi tabiiy, his-tuygʻular vaqt talab qilishini aytadi.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "Losing a game means the whole season was wasted",
                    "It's okay to feel disappointed after a loss, but it doesn't erase the good things achieved",
                    "Blaming the referee is the best way to deal with a loss",
                ],
                "answer": 1,
                "explanation": "Suhbat yutqazishdan keyin hafsalasi pir boʻlish tabiiy ekanini, lekin bu yil davomida erishilgan yutuqlarni oʻchirmasligini koʻrsatadi.",
            },
        ],
    },
    # ── 10 ───────────────────────────────────────────────────────────────
    {
        "title":   "Grandpa's Not the Same",
        "summary": "Bobosining xotirasi zaiflashganini koʻrgan Yuki va Kenji, kichik baliq ovlash suratlari orqali unga yaqinlashishga harakat qilishadi.",
        "order":   10,
        "body": '''<p><strong>Yuki:</strong> Kenji, did Grandpa <span class="cn-word" data-pos="verb" data-tr="tanimoq">recognize</span> you today? He seemed <span class="cn-word" data-pos="adj" data-tr="gangib qolgan">confused</span> when I said hi.</p>
<p><strong>Kenji:</strong> Not really, no. He called me by Dad's name twice.</p>
<p><strong>Yuki:</strong> That happened to me last time too. <strong>It's really hard to see</strong> him <span class="cn-word" data-pos="verb" data-tr="unutayotgan">forgetting</span> things.</p>
<p><strong>Kenji:</strong> He's just <strong>not as sharp as before</strong>. The doctor said that's <span class="cn-word" data-pos="adj" data-tr="odatiy, tabiiy">normal</span> with his <span class="cn-word" data-tr="ahvol, holat">condition</span>.</p>
<p><strong>Yuki:</strong> I know it's normal, but it still <span class="cn-word" data-pos="verb" data-tr="ogʻritadi">hurts</span> every time we visit.</p>
<p><strong>Kenji:</strong> Yeah. I keep <span class="cn-word" data-pos="verb" data-tr="eslab yuraman">remembering</span> how he used to tell those long fishing stories at dinner.</p>
<p><strong>Yuki:</strong> He still <span class="cn-word" data-pos="verb" data-tr="yorishib ketadi, jonlanadi">lights up</span> a little when we mention fishing, though. Did you notice that?</p>
<p><strong>Kenji:</strong> I did, actually. For a second there, he seemed <span class="cn-word" data-pos="adv" data-tr="deyarli">almost</span> like himself again.</p>
<p><strong>Yuki:</strong> Maybe we should bring old photos next time. Things that might help him remember.</p>
<p><strong>Kenji:</strong> That's a good idea. Even small moments like that seem to <span class="cn-word" data-pos="verb" data-tr="ahamiyatga ega boʻlmoq">matter</span> to him.</p>
<p><strong>Yuki:</strong> It's hard to see someone you love <span class="cn-word" data-pos="verb" data-tr="oʻzgarmoq">changing</span> like this.</p>
<p><strong>Kenji:</strong> It really is. But I'd still <span class="cn-word" data-pos="adv" data-tr="afzalroq">rather</span> visit and have those small moments than stay away.</p>
<p><strong>Yuki:</strong> Me too. Even confused, he's still our grandpa.</p>
<p><strong>Kenji:</strong> Exactly. Let's plan that photo visit for this weekend.</p>
<p><strong>Yuki:</strong> Deal. I'll bring the old fishing <span class="cn-word" data-tr="albom">album</span> from the garage.</p>''',
        "grammar": [
            {
                "pattern":  "not as + adjective + as before",
                "meaning":  "Avvalgidek ...emas (oʻzgarish yoki pasayishni bildiradi).",
                "examples": ["He's not as sharp as before.", "The city isn't as quiet as before."],
            },
            {
                "pattern":  "It's hard to see + someone + -ing",
                "meaning":  "Kimningdir ...ganini koʻrish qiyin (his-tuygʻu bilan bogʻliq qiyin holatni bildiradi).",
                "examples": ["It's hard to see someone you love changing like this.", "It's hard to see him struggling."],
            },
        ],
        "questions": [
            {
                "text": "What has changed about Grandpa?",
                "choices": [
                    "He has moved to a new house",
                    "He is having memory problems and sometimes doesn't recognize his grandchildren",
                    "He no longer likes fishing",
                ],
                "answer": 1,
                "explanation": "Bobo xotira muammolariga duch kelmoqda va baʼzan nevaralarini tanimay qolmoqda.",
            },
            {
                "text": "What idea do Yuki and Kenji come up with?",
                "choices": [
                    "To stop visiting Grandpa because it's too painful",
                    "To bring old photos, like fishing pictures, that might help him remember",
                    "To ask the doctor for a different treatment",
                ],
                "answer": 1,
                "explanation": "Ular Boboga eslab qolishga yordam berishi mumkin boʻlgan eski suratlarni, jumladan baliq ovlash suratlarini olib borishga qaror qilishadi.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "It's better to avoid visiting relatives who are struggling with memory loss",
                    "Even as a loved one changes, small shared moments still matter and are worth holding onto",
                    "Doctors should be able to cure all memory problems",
                ],
                "answer": 1,
                "explanation": "Suhbat sevimli inson oʻzgarsa ham, kichik birgalikdagi lahzalar hali ham qadrli ekanini koʻrsatadi.",
            },
        ],
    },
    # ── 11 ───────────────────────────────────────────────────────────────
    {
        "title":   "I Didn't Study, I Lied",
        "summary": "Matematika testida koʻchirib, tayyorlangan deb yolgʻon gapirgan Diego onasiga haqiqatni aytadi va xatosini toʻgʻrilashga harakat qiladi.",
        "order":   11,
        "body": '''<p><strong>Diego:</strong> Mom, can I talk to you about something? I need to tell you the <span class="cn-word" data-tr="haqiqat">truth</span>.</p>
<p><strong>Mom:</strong> Okay, you're <span class="cn-word" data-pos="verb" data-tr="xavotirlantiryapsan">worrying</span> me a little. What's going on?</p>
<p><strong>Diego:</strong> Remember when I said I studied for the math test last week? I didn't. I <span class="cn-word" data-pos="verb" data-tr="koʻchirdim">copied</span> answers from a friend.</p>
<p><strong>Mom:</strong> Diego. Why would you do that <strong>instead of</strong> just asking for help?</p>
<p><strong>Diego:</strong> I was <span class="cn-word" data-pos="adj" data-tr="qoʻrqqan">scared</span> of failing, and I <span class="cn-word" data-pos="verb" data-tr="vahima bosdi">panicked</span> the night before. It was a stupid decision.</p>
<p><strong>Mom:</strong> I'm <span class="cn-word" data-pos="adj" data-tr="afsusda, hafsalasi pir boʻlgan">disappointed</span>, I won't <span class="cn-word" data-pos="verb" data-tr="oʻzini qilib koʻrsatmoq">pretend</span> I'm not. But I'm glad you're telling me now.</p>
<p><strong>Diego:</strong> I've felt <span class="cn-word" data-pos="adj" data-tr="juda yomon">awful</span> about it all week. I couldn't even look at my grade without feeling sick.</p>
<p><strong>Mom:</strong> What do you think you should do about it?</p>
<p><strong>Diego:</strong> I already told my teacher today, actually. She's letting me <span class="cn-word" data-pos="verb" data-tr="qayta topshirmoq">retake</span> it honestly this time.</p>
<p><strong>Mom:</strong> That took real <span class="cn-word" data-tr="jasorat">courage</span>, Diego. I'm proud of you for that part, at least.</p>
<p><strong>Diego:</strong> <strong>From now on</strong>, I promise I'll ask for help instead of lying about it.</p>
<p><strong>Mom:</strong> I'll <span class="cn-word" data-pos="verb" data-tr="soʻzingda turishingni kutaman">hold you to that</span>. Do you need help studying for the retake?</p>
<p><strong>Diego:</strong> Actually, yeah. Could we go over it together tonight?</p>
<p><strong>Mom:</strong> Of course. That's what I'm here for.</p>
<p><strong>Diego:</strong> Thanks, Mom. For not just being angry the whole time.</p>
<p><strong>Mom:</strong> We all make <span class="cn-word" data-tr="xatolar">mistakes</span>. What matters is what you do after.</p>''',
        "grammar": [
            {
                "pattern":  "instead of + -ing",
                "meaning":  "...ish oʻrniga (bir tanlovni boshqasiga almashtirishni bildiradi).",
                "examples": ["Why would you do that instead of asking for help?", "Let's walk instead of driving."],
            },
            {
                "pattern":  "from now on",
                "meaning":  "Bundan buyon, shu kundan boshlab (kelajakdagi qarorni bildiradi).",
                "examples": ["From now on, I'll ask for help instead of lying.", "From now on, I'll study every night."],
            },
        ],
        "questions": [
            {
                "text": "What did Diego actually do on the math test, instead of studying?",
                "choices": [
                    "He skipped the test entirely",
                    "He copied answers from a friend and lied about studying",
                    "He asked the teacher for extra time",
                ],
                "answer": 1,
                "explanation": "Diego imtihonga tayyorlanmagan, buning oʻrniga doʻstidan koʻchirib, onasiga tayyorlangan deb yolgʻon gapirgan.",
            },
            {
                "text": "What did Diego already do before talking to his mom?",
                "choices": [
                    "Nothing, he was hoping no one would find out",
                    "He told his teacher the truth and is retaking the test honestly",
                    "He blamed his friend for the cheating",
                ],
                "answer": 1,
                "explanation": "U onasiga aytishdan oldin allaqachon oʻqituvchisiga haqiqatni aytib, testni halol qayta topshirishga rozi boʻlgan.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "Lying is always the easiest way to avoid punishment",
                    "Admitting a mistake honestly, even when it's hard, matters more than the mistake itself",
                    "Parents should never be told about cheating",
                ],
                "answer": 1,
                "explanation": "Suhbat xatoni ochiq tan olish, garchi bu qiyin boʻlsa ham, xatoning oʻzidan koʻra muhimroq ekanini koʻrsatadi.",
            },
        ],
    },
    # ── 12 ───────────────────────────────────────────────────────────────
    {
        "title":   "New Country, New Words",
        "summary": "Yangi mamlakatda ingliz tilida buyurtma berishdan uyalgan onasiga qizi Aisha oʻzi ham ilgari uyalganini aytib, uni qoʻllab-quvvatlaydi.",
        "order":   12,
        "body": '''<p><strong>Aisha:</strong> Mom, are you sure you don't want me to just order for you at the <span class="cn-word" data-tr="peshtaxta, kassa">counter</span>?</p>
<p><strong>Mom:</strong> I want to try it myself this time, Aisha. My English is getting better, right?</p>
<p><strong>Aisha:</strong> It really is. You've <span class="cn-word" data-pos="verb" data-tr="yaxshilanmoq">improved</span> so much since we <span class="cn-word" data-pos="verb" data-tr="koʻchib keldik">moved</span> here.</p>
<p><strong>Mom:</strong> Thank you for saying that. Sometimes I still feel <span class="cn-word" data-pos="adj" data-tr="uyalgan, noqulay">embarrassed</span> when I make mistakes.</p>
<p><strong>Aisha:</strong> You shouldn't be. Everyone makes mistakes when they're <span class="cn-word" data-pos="verb" data-tr="oʻrganmoq">learning</span> a new language.</p>
<p><strong>Mom:</strong> I know, but <strong>at first</strong>, I worried people were <span class="cn-word" data-pos="verb" data-tr="hukm qilmoq, baholamoq">judging</span> me.</p>
<p><strong>Aisha:</strong> I remember that. <strong>At first</strong>, I used to feel embarrassed too, honestly, when you needed help at stores. <strong>But now</strong> I'm <strong>proud of</strong> how hard you're <span class="cn-word" data-pos="verb" data-tr="harakat qilyapsan">trying</span>.</p>
<p><strong>Mom:</strong> Did you feel that way? I never knew that.</p>
<p><strong>Aisha:</strong> I did, when I was younger. I'm sorry I never told you.</p>
<p><strong>Mom:</strong> It's okay. That <span class="cn-word" data-pos="verb" data-tr="ahamiyat kasb etadi">means</span> more to me than you know, hearing it now.</p>
<p><strong>Aisha:</strong> Go order, Mom. I'll be right here if you need me, but I <span class="cn-word" data-pos="verb" data-tr="ishonaman">bet</span> you won't.</p>
<p><strong>Mom:</strong> Okay... wish me <span class="cn-word" data-tr="omad">luck</span>.</p>
<p><strong>Aisha:</strong> You don't need luck, Mom. You've got this.</p>
<p><strong>Mom:</strong> I did it! She <span class="cn-word" data-pos="verb" data-tr="tushundi">understood</span> me <span class="cn-word" data-pos="adv" data-tr="toʻliq, butunlay">completely</span>!</p>
<p><strong>Aisha:</strong> See? I told you. I'm so proud of you.</p>''',
        "grammar": [
            {
                "pattern":  "be proud of + -ing/noun",
                "meaning":  "...ligidan faxrlanmoq (biror ish yoki holat uchun faxrlanishni bildiradi).",
                "examples": ["I'm proud of how hard you're trying.", "She's proud of her daughter's courage."],
            },
            {
                "pattern":  "at first... but now",
                "meaning":  "Dastlab ..., lekin hozir ... (vaqt oʻtishi bilan oʻzgargan holatni bildiradi).",
                "examples": ["At first, I worried people were judging me. But now I feel more confident.", "At first, I hated the city. But now I love it here."],
            },
        ],
        "questions": [
            {
                "text": "Why did Aisha's mom feel embarrassed at first about speaking English in stores?",
                "choices": [
                    "She didn't like the food at the store",
                    "She worried people were judging her when she made mistakes",
                    "She didn't want to spend money",
                ],
                "answer": 1,
                "explanation": "U xato qilganda odamlar uni hukm qilishidan xavotirlangan.",
            },
            {
                "text": "What surprising thing does Aisha admit to her mom?",
                "choices": [
                    "She also used to feel embarrassed when her mom needed help at stores, but never said it",
                    "She doesn't want to live in this country anymore",
                    "She thinks her mom's English hasn't improved at all",
                ],
                "answer": 0,
                "explanation": "Aisha ilgari onasiga yordam kerak boʻlganda oʻzi ham uyalganini, lekin buni hech qachon aytmaganini tan oladi.",
            },
            {
                "text": "What is the main idea of the dialogue?",
                "choices": [
                    "Learning a new language is easy and doesn't require support from family",
                    "Supporting and being proud of a family member's effort to learn a new language matters, even through embarrassment",
                    "Children should always order food for their parents in a new country",
                ],
                "answer": 1,
                "explanation": "Suhbat oila aʼzosining yangi til oʻrganishdagi saʼy-harakatlarini qoʻllab-quvvatlash va bundan faxrlanish muhimligini koʻrsatadi, garchi bu jarayon uyatchanlik bilan kechsa ham.",
            },
        ],
    },
]
