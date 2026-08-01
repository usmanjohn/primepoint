# -*- coding: utf-8 -*-
"""Prime English practices — PE-91 … PE-95 (end of Block G + start of Block H).

Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_91_95.py --master=prime --expect-questions=20
"""

SUBJECT = {
    "name":        "English",
    "description": "English grammar and vocabulary practice",
    "icon":        "bi-translate",
    "color":       "#6366f1",
}

DEFAULTS = {
    "level":                "hard",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PE-91 — Formal vs Informal English
# =====================================================================
Q_PE91 = [
    {
        "text": "<p>Firdavs is rewriting his letter. Choose the formal alternative.</p>"
                "<p><strong>find out → ___</strong></p>",
        "choices": ["postpone", "discover", "request", "assist"],
        "correct": "discover",
        "explanation": "<p><strong>discover</strong> is correct. Formal English prefers a single verb to "
                       "a phrasal verb: <em>find out → discover</em>.<br><br>"
                       "<em>(Rasmiy ingliz tilida frazali feʼl oʻrniga bitta soʻzli feʼl afzal "
                       "koʻriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the formal alternative.</p>"
                "<p><strong>put off → ___</strong></p>",
        "choices": ["increase", "inform", "obtain", "postpone"],
        "correct": "postpone",
        "explanation": "<p><strong>postpone</strong> is correct — <em>put off the meeting</em> becomes "
                       "<em>postpone the meeting</em> in a formal letter.<br><br>"
                       "<em>(Rasmiy xatda <em>put off</em> oʻrniga <em>postpone</em> yoziladi — "
                       "\"keyinga qoldirmoq\".)</em></p>",
    },
    {
        "text": "<p>Choose the formal alternative.</p>"
                "<p><strong>ask for → ___</strong></p>",
        "choices": ["request", "require", "assist", "consider"],
        "correct": "request",
        "explanation": "<p><strong>request</strong> is correct. <em>I would like to request more "
                       "information</em> is the formal version of <em>I want to ask for more "
                       "info</em>.<br><br>"
                       "<em>(<em>request</em> — \"soʻramoq\" ning rasmiy shakli.)</em></p>",
    },
    {
        "text": "<p>Choose the formal alternative.</p>"
                "<p><strong>help → ___</strong></p>",
        "choices": ["inform", "demonstrate", "assist", "require"],
        "correct": "assist",
        "explanation": "<p><strong>assist</strong> is correct. Compare the rest of the family: "
                       "<em>tell → inform</em>, <em>show → demonstrate</em>, <em>need → "
                       "require</em>.<br><br>"
                       "<em>(Oilaning qolgan aʼzolari: <em>tell → inform</em>, <em>show → "
                       "demonstrate</em>, <em>need → require</em>.)</em></p>",
    },
    {
        "text": "<p>Sherbek is writing a formal letter. Which form should he use?</p>",
        "choices": ["can't", "don't can", "cannot", "not can"],
        "correct": "cannot",
        "explanation": "<p><strong>cannot</strong> is correct. Contractions are the first dial of "
                       "register: formal writing uses <em>I am, do not, cannot</em>, never <em>I'm, "
                       "don't, can't</em>.<br><br>"
                       "<em>(Qisqartmalar — uslubning birinchi belgisi. Rasmiy yozuvda <em>cannot</em> "
                       "kabi toʻliq shakllar ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Iroda is writing to a company. Which closing goes with <strong>Dear Sir or Madam,</strong>?</p>",
        "choices": ["Yours faithfully,", "Yours sincerely,", "Best wishes,", "See you soon!"],
        "correct": "Yours faithfully,",
        "explanation": "<p><strong>Yours faithfully,</strong> is correct. When you do not know the "
                       "person's name, the pair is <em>Dear Sir or Madam … Yours faithfully</em>.<br><br>"
                       "<em>(Ismni bilmasangiz, juftlik shunday boʻladi: <em>Dear Sir or Madam … Yours "
                       "faithfully</em>.)</em></p>",
    },
    {
        "text": "<p>Davron knows the manager's name. Which closing goes with <strong>Dear Mr Karimov,</strong>?</p>",
        "choices": ["Yours faithfully,", "Bye!", "Cheers!", "Yours sincerely,"],
        "correct": "Yours sincerely,",
        "explanation": "<p><strong>Yours sincerely,</strong> is correct — you know the name, so the "
                       "closing is <em>sincerely</em>, not <em>faithfully</em>.<br><br>"
                       "<em>(Ismni bilganingiz uchun <em>Yours sincerely</em> yoziladi, "
                       "<em>faithfully</em> emas.)</em></p>",
    },
    {
        "text": "<p>Choose the formal alternative.</p>"
                "<p><strong>a lot of → ___</strong></p>",
        "choices": ["loads of", "a great deal of", "lots of", "plenty of"],
        "correct": "a great deal of",
        "explanation": "<p><strong>a great deal of</strong> is correct — <em>numerous</em> also works "
                       "with countable nouns. <em>Loads of</em> and <em>lots of</em> are the informal "
                       "end of the scale.<br><br>"
                       "<em>(Sanaladigan otlar bilan <em>numerous</em> ham mos keladi. <em>loads of</em>, "
                       "<em>lots of</em> — norasmiy shakllar.)</em></p>",
    },
    {
        "text": "<p>Choose the formal alternative.</p>"
                "<p><strong>go up → ___</strong></p>",
        "choices": ["grow up", "get up", "raise up", "increase"],
        "correct": "increase",
        "explanation": "<p><strong>increase</strong> is correct, and its opposite <em>go down</em> "
                       "becomes <em>decrease</em>. Both are essential for describing charts "
                       "(PE-97).<br><br>"
                       "<em>(Uning teskarisi: <em>go down → decrease</em>. Ikkalasi ham diagramma "
                       "tasvirlashda juda kerak boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the formal alternative.</p>"
                "<p><strong>tell → ___</strong></p>",
        "choices": ["say", "inform", "speak", "talk"],
        "correct": "inform",
        "explanation": "<p><strong>inform</strong> is correct: <em>I am writing to inform you that…</em> "
                       "is a standard opening in official letters.<br><br>"
                       "<em>(<em>I am writing to inform you that…</em> — rasmiy xatlarning odatiy "
                       "boshlanishi.)</em></p>",
    },
    {
        "text": "<p>Which word is too informal for Shaxzoda to start a sentence with in her essay?</p>",
        "choices": ["However,", "In addition,", "But", "Therefore,"],
        "correct": "But",
        "explanation": "<p><strong>But</strong> is correct — starting a sentence with <em>But</em> or "
                       "<em>And</em> is too casual for an essay. Use <em>However,</em> or <em>In "
                       "addition,</em> instead.<br><br>"
                       "<em>(Gapni <em>But</em> yoki <em>And</em> bilan boshlash insho uchun juda "
                       "norasmiy. Oʻrniga <em>However,</em> yoki <em>In addition,</em> "
                       "ishlating.)</em></p>",
    },
    {
        "text": "<p>Which is the formal version of <strong>They cancelled the match</strong>?</p>",
        "choices": [
            "The match was cancelled.",
            "They cancelled the match.",
            "The match they cancelled.",
            "Cancelled was the match.",
        ],
        "correct": "The match was cancelled.",
        "explanation": "<p><strong>The match was cancelled.</strong> is correct. The passive voice is the "
                       "third dial of register — formal writing often prefers it because it keeps the "
                       "focus on the event, not on who did it.<br><br>"
                       "<em>(Majhul nisbat — uslubning uchinchi belgisi. Rasmiy yozuvda diqqat kim "
                       "qilganiga emas, voqeaning oʻziga qaratiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is formal?</p>",
        "choices": [
            "I am afraid I will be unable to attend, as I have a great deal of work to complete.",
            "Sorry, I can't come — I've got loads of homework.",
            "Can't come, too much homework!",
            "Hi! Sorry, no can do.",
        ],
        "correct": "I am afraid I will be unable to attend, as I have a great deal of work to complete.",
        "explanation": "<p>The first sentence is formal: no contractions, no slang, and <em>a great deal "
                       "of</em> instead of <em>loads of</em>. The others are all perfectly good — but "
                       "only when writing to a friend.<br><br>"
                       "<em>(Qisqartma yoʻq, jargon yoʻq, <em>loads of</em> oʻrniga <em>a great deal "
                       "of</em>. Qolganlari faqat doʻstga yozganda mos.)</em></p>",
    },
    {
        "text": "<p>Marjona is sending a message to a classmate about the homework. Which one is "
                "right?</p>",
        "choices": [
            "Dear Sir or Madam, I am writing regarding the mathematics assignment.",
            "I would be grateful if you could inform me of the assignment.",
            "Hi! What's the maths homework for tomorrow?",
            "To whom it may concern, please advise on the assignment.",
        ],
        "correct": "Hi! What's the maths homework for tomorrow?",
        "explanation": "<p><strong>Hi! What's the maths homework for tomorrow?</strong> is right. "
                       "Messages to friends and classmates are informal — writing <em>Dear Sir or "
                       "Madam</em> to a classmate would sound very strange.<br><br>"
                       "<em>(Doʻstlarga va sinfdoshlarga yozilgan xabarlar norasmiy boʻladi. "
                       "Sinfdoshingizga <em>Dear Sir or Madam</em> deb yozsangiz, juda gʻalati "
                       "eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Make it formal: <strong>We found out that a lot of students didn't come.</strong></p>",
        "choices": [
            "We found out that numerous students didn't attend.",
            "We discovered that numerous students did not attend.",
            "We discovered that a lot of students didn't come.",
            "We find out that numerous students did not attend.",
        ],
        "correct": "We discovered that numerous students did not attend.",
        "explanation": "<p><strong>We discovered that numerous students did not attend.</strong> is "
                       "correct. Three changes at once: phrasal verb → single verb, <em>a lot of → "
                       "numerous</em>, and no contraction.<br><br>"
                       "<em>(Bir vaqtda uchta oʻzgarish: frazali feʼl → bitta feʼl, <em>a lot of → "
                       "numerous</em>, va qisqartmasiz shakl.)</em></p>",
    },
    {
        "text": "<p>Make it informal: <strong>I regret that I am unable to assist you.</strong></p>",
        "choices": [
            "I regret I can't assist you.",
            "I am sorry that I cannot help you.",
            "Unable to assist you, regretfully.",
            "Sorry, I can't help you.",
        ],
        "correct": "Sorry, I can't help you.",
        "explanation": "<p><strong>Sorry, I can't help you.</strong> is correct — everything moves down "
                       "the scale at once: <em>regret → sorry</em>, <em>am unable → can't</em>, "
                       "<em>assist → help</em>.<br><br>"
                       "<em>(Hammasi bir vaqtda pastki darajaga tushadi: <em>regret → sorry</em>, "
                       "<em>am unable → can't</em>, <em>assist → help</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence uses the wrong register?</p>",
        "choices": [
            "Dear Sir or Madam, I would like to ask about the position.",
            "Dear Sir, I wanna ask about the job.",
            "Hi Jasur, are you free on Friday?",
            "Dear Ms Ahmedova, could you tell me when the course starts?",
        ],
        "correct": "Dear Sir, I wanna ask about the job.",
        "explanation": "<p><strong>Dear Sir, I wanna ask about the job.</strong> mixes registers — a "
                       "formal greeting followed by slang. Once you have chosen a register, keep it to "
                       "the end of the text.<br><br>"
                       "<em>(Rasmiy salomlashuvdan keyin jargon kelgan. Uslubni tanlagach, matn "
                       "oxirigacha shu uslubda davom eting.)</em></p>",
    },
    {
        "text": "<p>Which opening and closing go together correctly?</p>",
        "choices": [
            "Hi Mr Karimov, … Yours sincerely, Jasur",
            "Dear Mr Karimov, … See you! Jasur",
            "Hi Mr Karimov, … Yours faithfully, Jasur",
            "Dear Mr Karimov, … Yours sincerely, Jasur",
        ],
        "correct": "Dear Mr Karimov, … Yours sincerely, Jasur",
        "explanation": "<p><strong>Dear Mr Karimov, … Yours sincerely, Jasur</strong> is correct. The "
                       "greeting and the closing must sit at the same level — a formal opening cannot "
                       "end with <em>See you!</em>, and <em>Hi</em> cannot end with <em>Yours "
                       "faithfully</em>.<br><br>"
                       "<em>(Salomlashuv va xayrlashuv bir darajada boʻlishi kerak.)</em></p>",
    },
    {
        "text": "<p>Charos is finishing an essay. Choose the right word.</p>"
                "<p><strong>In conclusion, the film was ___</strong></p>",
        "choices": ["excellent.", "awesome!", "cool.", "super!"],
        "correct": "excellent.",
        "explanation": "<p><strong>excellent.</strong> is correct. <em>Awesome</em> and <em>cool</em> are "
                       "slang, and exclamation marks do not belong in an essay at all.<br><br>"
                       "<em>(<em>Awesome</em> va <em>cool</em> — jargon, undov belgisi esa inshoda "
                       "umuman ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Rozimurod teacher asks the class to write to a language school whose staff they "
                "do not know. Which pair is correct?</p>",
        "choices": [
            "Dear Sir or Madam, … Yours sincerely,",
            "Hi there, … Yours faithfully,",
            "Dear Sir or Madam, … Yours faithfully,",
            "Dear Sir or Madam, … Best wishes!",
        ],
        "correct": "Dear Sir or Madam, … Yours faithfully,",
        "explanation": "<p><strong>Dear Sir or Madam, … Yours faithfully,</strong> is correct. No name is "
                       "known, so both halves take the \"no name\" form.<br><br>"
                       "<em>(Ism nomaʼlum, shuning uchun ikkala qism ham \"ismsiz\" shaklda "
                       "boʻladi.)</em></p>",
    },
]


# =====================================================================
# PE-92 — The 20 Mistakes Uzbek Speakers Make Most
# =====================================================================
Q_PE92 = [
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Jasur English studies.",
            "English Jasur studies.",
            "Jasur studies English.",
            "Studies English Jasur.",
        ],
        "correct": "Jasur studies English.",
        "explanation": "<p><strong>Jasur studies English.</strong> is correct. Uzbek puts the verb last (SOV), "
                       "English puts it second (SVO) — this one habit produces more word-order errors "
                       "than anything else (PE-1, PE-72).<br><br>"
                       "<em>(Oʻzbek tilida kesim oxirida (SOV), ingliz tilida esa ikkinchi oʻrinda "
                       "(SVO). Aynan shu odat eng koʻp soʻz tartibi xatosini keltirib "
                       "chiqaradi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "It is raining today.",
            "Is raining today.",
            "It raining today.",
            "There is raining today.",
        ],
        "correct": "It is raining today.",
        "explanation": "<p><strong>It is raining today.</strong> is correct. Uzbek can drop the subject "
                       "(<em>yomgʻir yogʻyapti</em>), but an English sentence always needs one — even an "
                       "empty <em>it</em> (PE-1).<br><br>"
                       "<em>(Oʻzbekchada ega tushib qolishi mumkin, ingliz gapida esa ega doim boʻlishi "
                       "shart — hatto \"boʻsh\" <em>it</em> boʻlsa ham.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Sherbek very clever.",
            "Sherbek very clever is.",
            "Sherbek he is very clever.",
            "Sherbek is very clever.",
        ],
        "correct": "Sherbek is very clever.",
        "explanation": "<p><strong>Sherbek is very clever.</strong> is correct. Uzbek needs no verb "
                       "\"to be\" in this sentence, so it is easy to leave <em>is</em> out — but English "
                       "cannot (PE-6).<br><br>"
                       "<em>(Oʻzbekchada bu gapda \"boʻlmoq\" feʼli kerak emas, shuning uchun <em>is</em> "
                       "ni tushirib qoldirish oson. Ingliz tilida esa u shart.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I am student.",
            "I am a student.",
            "I am the student.",
            "I am one student.",
        ],
        "correct": "I am a student.",
        "explanation": "<p><strong>I am a student.</strong> is correct. Uzbek has no articles at all, so "
                       "this is the single commonest error on the list (PE-4).<br><br>"
                       "<em>(Oʻzbek tilida artikllar umuman yoʻq — shuning uchun bu roʻyxatdagi eng koʻp "
                       "uchraydigan xato.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Shaxzoda goes to school.",
            "Shaxzoda go to school.",
            "Shaxzoda goes school.",
            "Shaxzoda is go to school.",
        ],
        "correct": "Shaxzoda goes to school.",
        "explanation": "<p><strong>Shaxzoda goes to school.</strong> is correct. Uzbek verbs have no "
                       "special third-person ending, so the English <em>-s</em> is easy to forget "
                       "(PE-9).<br><br>"
                       "<em>(Oʻzbek feʼllarida alohida uchinchi shaxs qoʻshimchasi yoʻq, shuning uchun "
                       "inglizcha <em>-s</em> ni unutish oson.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I like very much tea.",
            "I like much tea very.",
            "Very much tea I like.",
            "I like tea very much.",
        ],
        "correct": "I like tea very much.",
        "explanation": "<p><strong>I like tea very much.</strong> is correct. Nothing may stand between a "
                       "verb and its object in English — the adverb has to move to the end "
                       "(PE-72).<br><br>"
                       "<em>(Ingliz tilida feʼl bilan toʻldiruvchi orasiga hech narsa qoʻyilmaydi — "
                       "ravish gap oxiriga koʻchadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Where you live?",
            "Where do you live?",
            "Where you are live?",
            "Where lives you?",
        ],
        "correct": "Where do you live?",
        "explanation": "<p><strong>Where do you live?</strong> is correct. Uzbek questions need no helper "
                       "verb, so it is easy to forget <em>do</em> in English (PE-18).<br><br>"
                       "<em>(Oʻzbekcha savolda yordamchi feʼl kerak emas, shuning uchun ingliz tilidagi "
                       "<em>do</em> ni unutish oson.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "The life is hard.",
            "A life is hard.",
            "Life is hard.",
            "Life it is hard.",
        ],
        "correct": "Life is hard.",
        "explanation": "<p><strong>Life is hard.</strong> is correct. When you speak about something in "
                       "general, English uses no article — the opposite trap to <em>I am a "
                       "student</em> (PE-4).<br><br>"
                       "<em>(Umumiy maʼnoda gapirganda ingliz tilida artikl qoʻyilmaydi — bu "
                       "<em>I am a student</em> ning teskari tuzogʻi.)</em></p>",
    },
    {
        "text": "<p>Which is correct?</p>",
        "choices": ["five book", "five books", "five of book", "the five book"],
        "correct": "five books",
        "explanation": "<p><strong>five books</strong> is correct. Uzbek keeps the singular after a "
                       "number (<em>besh kitob</em>), but English always makes the noun plural "
                       "(PE-3).<br><br>"
                       "<em>(Oʻzbekchada sondan keyin ot birlikda qoladi (<em>besh kitob</em>), ingliz "
                       "tilida esa doim koʻplikda boʻladi.)</em></p>",
    },
    {
        "text": "<p>Madina must write this correctly. Which is correct?</p>",
        "choices": [
            "many informations",
            "many information",
            "much information",
            "a lot of informations",
        ],
        "correct": "much information",
        "explanation": "<p><strong>much information</strong> is correct. <em>Information</em> is "
                       "uncountable in English, so it has no plural and takes <em>much</em>, not "
                       "<em>many</em> (PE-2).<br><br>"
                       "<em>(<em>Information</em> ingliz tilida sanalmaydigan ot — koʻpligi yoʻq va "
                       "<em>much</em> bilan keladi, <em>many</em> bilan emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I have lived here for ten years.",
            "I live here for ten years.",
            "I have lived here since ten years.",
            "I am living here since ten years.",
        ],
        "correct": "I have lived here for ten years.",
        "explanation": "<p><strong>I have lived here for ten years.</strong> is correct. Uzbek uses the "
                       "present for this idea, English uses the Present Perfect — and a length of time "
                       "takes <em>for</em>, not <em>since</em> (PE-33).<br><br>"
                       "<em>(Oʻzbekchada bu maʼno hozirgi zamon bilan beriladi, ingliz tilida esa "
                       "Present Perfect bilan. Davomiylik uchun <em>for</em> ishlatiladi, "
                       "<em>since</em> emas.)</em></p>",
    },
    {
        "text": "<p>Which is correct?</p>",
        "choices": ["Did you went?", "Did you gone?", "Did you going?", "Did you go?"],
        "correct": "Did you go?",
        "explanation": "<p><strong>Did you go?</strong> is correct. The past is marked once only — "
                       "<em>did</em> already carries it, so the main verb goes bare (PE-22).<br><br>"
                       "<em>(Oʻtganlik faqat bir marta belgilanadi: <em>did</em> uni koʻtargani uchun "
                       "asosiy feʼl asl shaklda qoladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I am knowing the answer.",
            "I am know the answer.",
            "I knowing the answer.",
            "I know the answer.",
        ],
        "correct": "I know the answer.",
        "explanation": "<p><strong>I know the answer.</strong> is correct. <em>Know, like, want, "
                       "understand</em> are stative verbs — they describe a state, not an action, so they "
                       "have no continuous form (PE-13).<br><br>"
                       "<em>(<em>know, like, want, understand</em> — holat feʼllari. Ular harakatni emas, "
                       "holatni bildiradi, shuning uchun davomli shakli yoʻq.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "When I will arrive, I will call.",
            "When I arrive, I will call.",
            "When I will arrive, I call.",
            "When I arriving, I will call.",
        ],
        "correct": "When I arrive, I will call.",
        "explanation": "<p><strong>When I arrive, I will call.</strong> is correct. After <em>when, if, "
                       "before, until</em> English uses the present, even though the meaning is future "
                       "(PE-26).<br><br>"
                       "<em>(<em>when, if, before, until</em> dan keyin ingliz tilida hozirgi zamon "
                       "ishlatiladi, garchi maʼno kelasi zamon boʻlsa ham.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "We discussed about the plan.",
            "We discussed on the plan.",
            "We discussed the plan.",
            "We discussed of the plan.",
        ],
        "correct": "We discussed the plan.",
        "explanation": "<p><strong>We discussed the plan.</strong> is correct. <em>Discuss</em> takes no "
                       "preposition at all — the Uzbek case ending tempts you into adding "
                       "<em>about</em> (PE-76).<br><br>"
                       "<em>(<em>Discuss</em> hech qanday predlog olmaydi. Oʻzbekchadagi kelishik "
                       "qoʻshimchasi <em>about</em> qoʻshishga undaydi — lekin bu xato.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I'm listening to music.",
            "I'm listening music.",
            "I'm listening the music.",
            "I'm listen to music.",
        ],
        "correct": "I'm listening to music.",
        "explanation": "<p><strong>I'm listening to music.</strong> is correct. The mirror image of "
                       "<em>discuss</em>: here English <em>needs</em> the preposition that Uzbek does not "
                       "have (PE-76).<br><br>"
                       "<em>(<em>discuss</em> ning teskarisi: bu yerda ingliz tili oʻzbekchada boʻlmagan "
                       "predlogni <strong>talab qiladi</strong>.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "I never smoke.",
            "Although I was tired, I never stopped.",
            "I never don't smoke.",
            "Behruz made a mistake.",
        ],
        "correct": "I never don't smoke.",
        "explanation": "<p><strong>I never don't smoke.</strong> is the mistake. Uzbek needs two negative "
                       "markers (<em>hech qachon chekmayman</em>), English allows only one — "
                       "<em>never</em> is already the negative (PE-11).<br><br>"
                       "<em>(Oʻzbekchada ikkita inkor belgisi kerak, ingliz tilida esa bittasi yetarli — "
                       "<em>never</em> ning oʻzi inkor.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Although Firdavs was tired, he never stopped.",
            "Although Firdavs was tired, but he never stopped.",
            "Although Firdavs was tired, but he didn't never stop.",
            "Although Firdavs was tired, however he never stopped.",
        ],
        "correct": "Although Firdavs was tired, he never stopped.",
        "explanation": "<p><strong>Although Firdavs was tired, he never stopped.</strong> is correct. The Uzbek "
                       "<em>garchi … lekin</em> pattern produces <em>although … but</em>, but English "
                       "uses one contrast word per sentence (PE-52).<br><br>"
                       "<em>(Oʻzbekchadagi \"garchi … lekin\" qolipi <em>although … but</em> xatosini "
                       "keltirib chiqaradi. Ingliz tilida bitta gapda bitta qarama-qarshilik soʻzi "
                       "boʻladi.)</em></p>",
    },
    {
        "text": "<p>Rebuild this sentence: <strong>My father work in hospital and he very "
                "busy.</strong></p>",
        "choices": [
            "My father works in hospital and he is very busy.",
            "My father work in a hospital and he is very busy.",
            "My father works in a hospital and he very busy.",
            "My father works in a hospital and he is very busy.",
        ],
        "correct": "My father works in a hospital and he is very busy.",
        "explanation": "<p>The last option fixes all three errors at once: the missing <em>-s</em>, the "
                       "missing article and the missing <em>is</em> — the three commonest of all. Each "
                       "of the other options still leaves one of them in.<br><br>"
                       "<em>(Oxirgi variant uchala xatoni ham tuzatadi: tushib qolgan <em>-s</em>, "
                       "artikl va <em>is</em>. Qolganlarida bittasi hamon qolgan.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> You wrote \"I study English since five years "
                "and I like very much it.\" Can you correct it, Iroda?</p>"
                "<p><strong>Iroda:</strong> ___</p>",
        "choices": [
            "I have studied English for five years and I like very much it.",
            "I have studied English for five years and I like it very much.",
            "I study English for five years and I like it very much.",
            "I have studied English since five years and I like it very much.",
        ],
        "correct": "I have studied English for five years and I like it very much.",
        "explanation": "<p><strong>I have studied English for five years and I like it very much.</strong> "
                       "is correct — three fixes together: Present Perfect, <em>for</em> instead of "
                       "<em>since</em>, and nothing between the verb and its object.<br><br>"
                       "<em>(Uchta tuzatish birga: Present Perfect, <em>since</em> oʻrniga <em>for</em>, "
                       "va feʼl bilan toʻldiruvchi orasida hech narsa yoʻq.)</em></p>",
    },
]


# =====================================================================
# PE-93 — Writing an Email: Grammar That Sounds Polite
# =====================================================================
Q_PE93 = [
    {
        "text": "<p>Elbek does not know the name of the person he is writing to. Which closing goes with <strong>Dear Sir or Madam,</strong>?</p>",
        "choices": ["Yours sincerely,", "Yours faithfully,", "Best wishes,", "See you!"],
        "correct": "Yours faithfully,",
        "explanation": "<p><strong>Yours faithfully,</strong> is correct. Use <em>Yours sincerely</em> "
                       "only when you know the person's name.<br><br>"
                       "<em>(<em>Yours sincerely</em> ni faqat odamning ismini bilganingizda "
                       "ishlating.)</em></p>",
    },
    {
        "text": "<p>Charos knows the person's name. Which closing goes with <strong>Dear Mr Karimov,</strong>?</p>",
        "choices": ["Yours faithfully,", "Cheers!", "Bye for now,", "Yours sincerely,"],
        "correct": "Yours sincerely,",
        "explanation": "<p><strong>Yours sincerely,</strong> is correct — the name is known, so the "
                       "greeting and closing pair up.<br><br>"
                       "<em>(Ism maʼlum, shuning uchun salomlashuv va xayrlashuv juftlashadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I am writing to ___ about the summer course.</strong></p>",
        "choices": ["ask", "asking", "asked", "be asking"],
        "correct": "ask",
        "explanation": "<p><strong>ask</strong> is correct. <em>I am writing to + base verb</em> is the "
                       "fixed opening phrase that states your purpose in the very first "
                       "line.<br><br>"
                       "<em>(<em>I am writing to + asl feʼl</em> — birinchi qatordayoq maqsadni "
                       "bildiruvchi tayyor ibora.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I look forward to ___ from you.</strong></p>",
        "choices": ["hear", "heard", "hearing", "be hear"],
        "correct": "hearing",
        "explanation": "<p><strong>hearing</strong> is correct. That <em>to</em> is a preposition, not "
                       "part of an infinitive, so the verb takes <em>-ing</em> (PE-64). <em>Look forward "
                       "to hear</em> is one of the most frequent email errors.<br><br>"
                       "<em>(Bu yerdagi <em>to</em> — predlog, infinitiv emas. Shuning uchun feʼl "
                       "<em>-ing</em> oladi. <em>Look forward to hear</em> — xatlardagi eng koʻp "
                       "uchraydigan xatolardan biri.)</em></p>",
    },
    {
        "text": "<p>Iroda needs the application form. Choose the politest option.</p>"
                "<p><strong>___ you send me the application form, please?</strong></p>",
        "choices": ["Send", "Must", "Could", "Shall"],
        "correct": "Could",
        "explanation": "<p><strong>Could</strong> is correct. <em>Could you…?</em> turns an order into a "
                       "request — the modal is doing real politeness work here (PE-49).<br><br>"
                       "<em>(<em>Could you…?</em> buyruqni iltimosga aylantiradi — modal feʼl bu yerda "
                       "haqiqiy ish bajaryapti.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I would be grateful if you ___ confirm the date.</strong></p>",
        "choices": ["could", "can", "will", "shall"],
        "correct": "could",
        "explanation": "<p><strong>could</strong> is correct. <em>would … if you could</em> is the second "
                       "conditional (PE-54) doing the politeness work — the longer the structure, the "
                       "more polite it sounds.<br><br>"
                       "<em>(<em>would … if you could</em> — ikkinchi turdagi shart gap. Qurilma qancha "
                       "uzun boʻlsa, shuncha muloyim eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I would ___ it if you could reply by Friday.</strong></p>",
        "choices": ["grateful", "thankful", "pleased", "appreciate"],
        "correct": "appreciate",
        "explanation": "<p><strong>appreciate</strong> is correct — <em>I would appreciate it if…</em> is "
                       "a fixed phrase, and the little <em>it</em> is part of it.<br><br>"
                       "<em>(<em>I would appreciate it if…</em> — tayyor ibora, kichkina <em>it</em> ham "
                       "uning bir qismi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I am writing to ___ for the position of assistant teacher.</strong></p>",
        "choices": ["ask", "apply", "request", "demand"],
        "correct": "apply",
        "explanation": "<p><strong>apply</strong> is correct — <em>apply for a job / a position / a "
                       "course</em> is the fixed partnership (PE-90).<br><br>"
                       "<em>(<em>apply for a job / a position / a course</em> — qatʼiy "
                       "juftlik.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Please do not ___ to contact me if you need more information.</strong></p>",
        "choices": ["wait", "stop", "delay", "hesitate"],
        "correct": "hesitate",
        "explanation": "<p><strong>hesitate</strong> is correct. <em>Please do not hesitate to contact "
                       "me</em> is a standard closing line — learn it as one block.<br><br>"
                       "<em>(<em>Please do not hesitate to contact me</em> — standart yakuniy jumla, "
                       "uni butunligicha yodlang.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ for the late reply.</strong></p>",
        "choices": ["excuse", "apologise", "sorry", "pardon"],
        "correct": "apologise",
        "explanation": "<p><strong>apologise</strong> is correct. <em>I apologise for the late reply</em> "
                       "is the email version; <em>Sorry for late</em> is both informal and "
                       "ungrammatical.<br><br>"
                       "<em>(<em>I apologise for the late reply</em> — xat uchun toʻgʻri shakl. "
                       "<em>Sorry for late</em> ham norasmiy, ham grammatik jihatdan "
                       "notoʻgʻri.)</em></p>",
    },
    {
        "text": "<p>Which is the correct order of the five parts of an email?</p>",
        "choices": [
            "greeting → request → reason → details → closing",
            "details → greeting → reason → request → closing",
            "greeting → reason → details → request → closing",
            "reason → greeting → closing → details → request",
        ],
        "correct": "greeting → reason → details → request → closing",
        "explanation": "<p><strong>greeting → reason → details → request → closing</strong> is correct. "
                       "English emails state the purpose immediately — that is politeness, not "
                       "rudeness, because it saves the reader's time.<br><br>"
                       "<em>(Inglizcha xatlarda maqsad darhol aytiladi. Bu qoʻpollik emas — oʻqiyotgan "
                       "odamning vaqtini tejagani uchun hurmat belgisi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I am writing ___ my exam results.</strong></p>",
        "choices": ["regarding", "about of", "for about", "in regard"],
        "correct": "regarding",
        "explanation": "<p><strong>regarding</strong> is correct — a slightly more formal alternative to "
                       "<em>about</em>, very common at the start of official emails.<br><br>"
                       "<em>(<em>regarding</em> — <em>about</em> ning biroz rasmiyroq shakli, rasmiy "
                       "xatlarning boshida juda koʻp uchraydi.)</em></p>",
    },
    {
        "text": "<p>Madina is writing to Rozimurod teacher. Which sentence is polite enough?</p>",
        "choices": [
            "Could you send me the form, please?",
            "Send me the form.",
            "I want the form.",
            "Give me the form now.",
        ],
        "correct": "Could you send me the form, please?",
        "explanation": "<p><strong>Could you send me the form, please?</strong> is correct. A bare "
                       "imperative is an order; the modal question makes it a request.<br><br>"
                       "<em>(Yalangʻoch buyruq — bu buyruq; modal feʼlli savol esa uni iltimosga "
                       "aylantiradi.)</em></p>",
    },
    {
        "text": "<p>Which opening is right for an email to a teacher whose name you know?</p>",
        "choices": ["Hi teacher!", "Dear Sir or Madam,", "Dear Ms Ahmedova,", "Hello you,"],
        "correct": "Dear Ms Ahmedova,",
        "explanation": "<p><strong>Dear Ms Ahmedova,</strong> is correct. This is the middle register — "
                       "polite but not stiff, and the one you will use most in real life.<br><br>"
                       "<em>(Bu — oʻrta daraja: muloyim, lekin ogʻir emas. Amalda eng koʻp kerak "
                       "boʻladigan uslub aynan shu.)</em></p>",
    },
    {
        "text": "<p>What should the first line of a formal English email do?</p>",
        "choices": [
            "Ask how the reader and their family are.",
            "State clearly why you are writing.",
            "Apologise for writing at all.",
            "Describe yourself in detail.",
        ],
        "correct": "State clearly why you are writing.",
        "explanation": "<p><strong>State clearly why you are writing.</strong> is correct. This is a real "
                       "cultural difference: Uzbek letters often open with long greetings, while an "
                       "English one goes straight to <em>I am writing to…</em><br><br>"
                       "<em>(Bu — haqiqiy madaniy farq: oʻzbekcha xatlarda uzun salomlashish boʻladi, "
                       "inglizchada esa darhol <em>I am writing to…</em> deyiladi.)</em></p>",
    },
    {
        "text": "<p>Which is the most polite way to ask?</p>",
        "choices": [
            "Send the timetable.",
            "Please send the timetable now.",
            "I want the timetable.",
            "I would be grateful if you could send me the timetable.",
        ],
        "correct": "I would be grateful if you could send me the timetable.",
        "explanation": "<p><strong>I would be grateful if you could send me the timetable.</strong> is "
                       "the most polite. Notice the pattern: the longer and less direct the structure, "
                       "the more polite it sounds.<br><br>"
                       "<em>(Qoidaga eʼtibor bering: qurilma qancha uzun va bavosita boʻlsa, shuncha "
                       "muloyim eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "I look forward to hearing from you.",
            "I look forward to hear from you.",
            "I am writing to ask about the course.",
            "Could you send me the timetable, please?",
        ],
        "correct": "I look forward to hear from you.",
        "explanation": "<p><strong>I look forward to hear from you.</strong> is the mistake — after that "
                       "preposition <em>to</em>, the verb must take <em>-ing</em>: <em>hearing</em>.<br><br>"
                       "<em>(Predlog <em>to</em> dan keyin feʼl <em>-ing</em> olishi shart: "
                       "<em>hearing</em>.)</em></p>",
    },
    {
        "text": "<p>Which is correct?</p>",
        "choices": [
            "Dear Sir, … Best wishes, Jasur",
            "Hi Mr Karimov, … Yours faithfully, Jasur",
            "Dear teacher, how are you? I want ask something.",
            "Dear Sir or Madam, … Yours faithfully, Jasur Karimov",
        ],
        "correct": "Dear Sir or Madam, … Yours faithfully, Jasur Karimov",
        "explanation": "<p><strong>Dear Sir or Madam, … Yours faithfully, Jasur Karimov</strong> is "
                       "correct — matching greeting and closing, and the full name at the end of a "
                       "formal letter.<br><br>"
                       "<em>(Salomlashuv va xayrlashuv mos, rasmiy xat oxirida esa toʻliq ism "
                       "yoziladi.)</em></p>",
    },
    {
        "text": "<p>Sherbek missed a lesson and wants to write to his teacher about it. Which first "
                "line is correct?</p>",
        "choices": [
            "I am writing to ask about the lesson I missed on Monday.",
            "I want you tell me about the lesson I missed.",
            "I am writing for ask about the lesson I missed.",
            "I write you about lesson which I missed.",
        ],
        "correct": "I am writing to ask about the lesson I missed on Monday.",
        "explanation": "<p><strong>I am writing to ask about the lesson I missed on Monday.</strong> is "
                       "correct: the fixed phrase, <em>to + base verb</em>, and the reason given "
                       "immediately.<br><br>"
                       "<em>(Tayyor ibora, <em>to + asl feʼl</em>, va sabab darhol "
                       "aytilgan.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> How should you finish the email, Behruz?</p>"
                "<p><strong>Behruz:</strong> ___</p>",
        "choices": [
            "Thank you in advance. I look forward to hear from you.",
            "Thanks! See you!",
            "Thank you for your help. I look forward to hearing from you.",
            "Thank you for your help. I look forward for hearing from you.",
        ],
        "correct": "Thank you for your help. I look forward to hearing from you.",
        "explanation": "<p><strong>Thank you for your help. I look forward to hearing from you.</strong> "
                       "is correct — the two standard closing lines, with <em>to hearing</em> and not "
                       "<em>to hear</em> or <em>for hearing</em>.<br><br>"
                       "<em>(Ikkita standart yakuniy jumla, <em>to hearing</em> shaklida — <em>to "
                       "hear</em> ham, <em>for hearing</em> ham emas.)</em></p>",
    },
]


# =====================================================================
# PE-94 — Telling a Story: Narrative Tenses in Action
# =====================================================================
Q_PE94 = [
    {
        "text": "<p>Choose the correct tense.</p>"
                "<p><strong>Charos ___ TV when the lights went out.</strong> (watch)</p>",
        "choices": ["watched", "have watched", "was watching", "had watched"],
        "correct": "was watching",
        "explanation": "<p><strong>was watching</strong> is correct. The Past Continuous paints the "
                       "background; the short event that interrupts it goes into the Past Simple "
                       "(PE-24).<br><br>"
                       "<em>(Past Continuous fonni chizadi; uni boʻlgan qisqa voqea esa Past Simple da "
                       "beriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tense.</p>"
                "<p><strong>Suddenly, somebody ___ at the door.</strong> (knock)</p>",
        "choices": ["knocked", "was knocking", "had knocked", "knocks"],
        "correct": "knocked",
        "explanation": "<p><strong>knocked</strong> is correct. The Past Simple is the tense that moves "
                       "the action forward — it is the engine of the story.<br><br>"
                       "<em>(Past Simple — voqealarni oldinga siljituvchi zamon, hikoyaning "
                       "dvigateli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tense.</p>"
                "<p><strong>When we got to the station, the train ___.</strong> (leave)</p>",
        "choices": ["left", "was leaving", "has left", "had left"],
        "correct": "had left",
        "explanation": "<p><strong>had left</strong> is correct. The train left <em>before</em> we "
                       "arrived, so the earlier action goes into the Past Perfect.<br><br>"
                       "<em>(Poyezd biz yetib borishimizdan <strong>oldin</strong> ketgan, shuning uchun "
                       "oldingi harakat Past Perfect da beriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tense.</p>"
                "<p><strong>Sirojiddin ___ for an hour when she finally arrived.</strong> (wait)</p>",
        "choices": ["waited", "had been waiting", "was waiting", "has waited"],
        "correct": "had been waiting",
        "explanation": "<p><strong>had been waiting</strong> is correct. The Past Perfect Continuous "
                       "answers \"how long had it been going on before that moment?\"<br><br>"
                       "<em>(Past Perfect Continuous \"oʻsha paytgacha qancha vaqtdan beri davom "
                       "etayotgan edi?\" degan savolga javob beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tense.</p>"
                "<p><strong>The sun ___ and the birds were singing.</strong> (set)</p>",
        "choices": ["was setting", "set", "had set", "sets"],
        "correct": "was setting",
        "explanation": "<p><strong>was setting</strong> is correct — this is pure scene-painting, and "
                       "scene-painting is the job of the Past Continuous.<br><br>"
                       "<em>(Bu — sof fon tasviri, fon tasviri esa Past Continuous ning "
                       "vazifasi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tense.</p>"
                "<p><strong>Yesterday I was going to school when I ___ an accident.</strong> (see)</p>",
        "choices": ["was seeing", "had seen", "have seen", "saw"],
        "correct": "saw",
        "explanation": "<p><strong>saw</strong> is correct. The long action is already in the Continuous, "
                       "so the sudden one that cuts across it must be Past Simple — and <em>see</em> is "
                       "a stative verb anyway (PE-13).<br><br>"
                       "<em>(Uzoq davom etgan harakat allaqachon Continuous da, shuning uchun uni kesib "
                       "oʻtgan toʻsatdan boʻlgan voqea Past Simple da boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>When Elbek arrived, the film ___ already started.</strong></p>",
        "choices": ["has", "had", "was", "did"],
        "correct": "had",
        "explanation": "<p><strong>had</strong> is correct. The story is in the past, so \"earlier than "
                       "the story\" is <em>had</em> + V3, not <em>has</em>.<br><br>"
                       "<em>(Hikoya oʻtgan zamonda, shuning uchun \"hikoyadan ham oldin\" maʼnosi "
                       "<em>had</em> + V3 bilan beriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tense.</p>"
                "<p><strong>Last summer I ___ with my grandparents in the village.</strong> (stay)</p>",
        "choices": ["stayed", "had stayed", "was staying", "stay"],
        "correct": "was staying",
        "explanation": "<p><strong>was staying</strong> is correct. This is how a story opens: set the "
                       "scene with the Past Continuous, plus where and when.<br><br>"
                       "<em>(Hikoya aynan shunday boshlanadi: Past Continuous bilan fonni chizing va joy "
                       "hamda vaqtni ayting.)</em></p>",
    },
    {
        "text": "<p>Choose the correct time word.</p>"
                "<p><strong>___ morning, Jasur decided to walk to the river.</strong></p>",
        "choices": ["A", "One", "Some", "The"],
        "correct": "One",
        "explanation": "<p><strong>One</strong> is correct. <em>One morning, One day, Last summer, It all "
                       "began when…</em> — these are the phrases that start the action.<br><br>"
                       "<em>(<em>One morning, One day, Last summer</em> — voqeani boshlab beruvchi "
                       "iboralar.)</em></p>",
    },
    {
        "text": "<p>Choose the correct time word.</p>"
                "<p><strong>___, the weather changed and the sky went dark.</strong></p>",
        "choices": ["Meanwhile", "After that", "Suddenly", "In the end"],
        "correct": "Suddenly",
        "explanation": "<p><strong>Suddenly</strong> is correct — it belongs to the \"surprise\" family, "
                       "with <em>All of a sudden</em>, <em>Without warning</em> and <em>To my "
                       "surprise</em>.<br><br>"
                       "<em>(<em>Suddenly</em> \"hayrat\" oilasiga kiradi: <em>All of a sudden</em>, "
                       "<em>Without warning</em>, <em>To my surprise</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct time word.</p>"
                "<p><strong>___, we had to turn back and go home.</strong></p>",
        "choices": ["In the end", "One day", "Suddenly", "Meanwhile"],
        "correct": "In the end",
        "explanation": "<p><strong>In the end</strong> is correct — the ending family also holds "
                       "<em>Finally</em>, <em>Luckily</em> and <em>Since then</em>.<br><br>"
                       "<em>(Yakunlovchi oilada <em>Finally</em>, <em>Luckily</em>, <em>Since then</em> "
                       "ham bor.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tense.</p>"
                "<p><strong>When I got to the river, I realised I ___ to bring water.</strong> "
                "(forget)</p>",
        "choices": ["forgot", "was forgetting", "have forgotten", "had forgotten"],
        "correct": "had forgotten",
        "explanation": "<p><strong>had forgotten</strong> is correct. The forgetting happened before the "
                       "realising, so it reaches back one step into the Past Perfect.<br><br>"
                       "<em>(Unutish anglashdan oldin boʻlgan, shuning uchun u bir qadam orqaga — Past "
                       "Perfect ga oʻtadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I had woken up, I had eaten breakfast and I had gone out.",
            "I was waking up, was eating breakfast and was going out.",
            "I had woken up, ate breakfast and had gone out.",
            "I woke up, ate breakfast and went out.",
        ],
        "correct": "I woke up, ate breakfast and went out.",
        "explanation": "<p><strong>I woke up, ate breakfast and went out.</strong> is correct. A simple "
                       "sequence of events in order needs only the Past Simple — the Past Perfect is for "
                       "reaching <em>back</em>, not for listing (PE-38).<br><br>"
                       "<em>(Tartib bilan ketayotgan oddiy voqealar ketma-ketligiga faqat Past Simple "
                       "kerak. Past Perfect esa <strong>orqaga</strong> qaytish uchun, sanash uchun "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>Rozimurod teacher asks: which tense paints the background scene of a story?</p>",
        "choices": ["Past Simple", "Past Continuous", "Past Perfect", "Present Perfect"],
        "correct": "Past Continuous",
        "explanation": "<p><strong>Past Continuous</strong> is correct. The three jobs: <em>was -ing</em> "
                       "= the scene, <em>V2</em> = the events, <em>had + V3</em> = what happened "
                       "earlier.<br><br>"
                       "<em>(Uchta vazifa: <em>was -ing</em> — fon, <em>V2</em> — voqealar, <em>had + "
                       "V3</em> — undan oldin boʻlgani.)</em></p>",
    },
    {
        "text": "<p>Which sentence has the \"dangling participle\" problem?</p>",
        "choices": [
            "Walking home, I had my bag stolen.",
            "Hearing the noise, Afsona ran to the window.",
            "Walking home, my bag was stolen.",
            "Seeing nothing, she went back to bed.",
        ],
        "correct": "Walking home, my bag was stolen.",
        "explanation": "<p><strong>Walking home, my bag was stolen.</strong> is the problem — it says the "
                       "bag was walking home. The participle must belong to the subject of the main "
                       "clause (PE-86).<br><br>"
                       "<em>(Bu gap \"sumka uyga ketayotgan edi\" degan maʼnoni beradi. Ravishdosh "
                       "asosiy gapning egasiga tegishli boʻlishi kerak.)</em></p>",
    },
    {
        "text": "<p>Which version is better style?</p>",
        "choices": [
            "It started to rain, so we ran. Finally we arrived.",
            "Suddenly it was raining and suddenly we ran and suddenly we arrived.",
            "Suddenly it rained. Suddenly we ran. Suddenly we arrived.",
            "It suddenly rained and suddenly we suddenly ran home.",
        ],
        "correct": "It started to rain, so we ran. Finally we arrived.",
        "explanation": "<p><strong>It started to rain, so we ran. Finally we arrived.</strong> is better. "
                       "<em>Suddenly</em> is powerful once and weak three times — keep one surprise per "
                       "story.<br><br>"
                       "<em>(<em>Suddenly</em> bir marta ishlatilsa kuchli, uch marta ishlatilsa "
                       "kuchsiz. Bitta hikoyada bitta hayratli lahza yetarli.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "Yesterday I was going to school when I saw an accident.",
            "When I arrived, the film had already started.",
            "Yesterday I was going to school and I was seeing an accident.",
            "Davron had been waiting for an hour.",
        ],
        "correct": "Yesterday I was going to school and I was seeing an accident.",
        "explanation": "<p><strong>Yesterday I was going to school and I was seeing an accident.</strong> "
                       "is the mistake — the sudden event must be Past Simple (<em>saw</em>), and "
                       "<em>see</em> has no continuous form anyway.<br><br>"
                       "<em>(Toʻsatdan boʻlgan voqea Past Simple da boʻlishi kerak (<em>saw</em>), "
                       "qolaversa <em>see</em> ning davomli shakli yoʻq.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "When we got to the station, the train had left.",
            "When we got to the station, the train has left.",
            "When we got to the station, the train have left.",
            "When we got to the station, the train left before.",
        ],
        "correct": "When we got to the station, the train had left.",
        "explanation": "<p><strong>When we got to the station, the train had left.</strong> is correct. "
                       "<em>Has left</em> would put the story in the present; the whole narrative is in "
                       "the past.<br><br>"
                       "<em>(<em>Has left</em> hikoyani hozirgi zamonga olib oʻtardi; butun bayon esa "
                       "oʻtgan zamonda.)</em></p>",
    },
    {
        "text": "<p>Improve this: <strong>I went out. I saw a dog. I was afraid. I ran home.</strong></p>",
        "choices": [
            "I went out and I saw a dog and I was afraid and I ran home.",
            "Going out, the dog saw me afraid and I ran home.",
            "I had gone out. I had seen a dog. I had been afraid. I had run home.",
            "As I was going out, I saw a large dog in the yard. Feeling afraid, I ran straight back home.",
        ],
        "correct": "As I was going out, I saw a large dog in the yard. Feeling afraid, I ran straight back home.",
        "explanation": "<p>The last version is best: the same events, but with a background tense, a "
                       "participle clause and varied sentence length. That is what turns a list into a "
                       "story.<br><br>"
                       "<em>(Voqealar oʻsha-oʻsha, lekin fon zamoni, ravishdosh oborot va turli "
                       "uzunlikdagi jumlalar bor. Aynan shu roʻyxatni hikoyaga aylantiradi.)</em></p>",
    },
    {
        "text": "<p>Complete the story with the correct pair of tenses.</p>"
                "<p><strong>Last winter Madina ___ to Samarkand by train. She fell asleep and woke up "
                "at the wrong station — she ___ to set an alarm.</strong></p>",
        "choices": [
            "travelled / forgot",
            "was travelling / had forgotten",
            "had travelled / was forgetting",
            "was travelling / was forgetting",
        ],
        "correct": "was travelling / had forgotten",
        "explanation": "<p><strong>was travelling / had forgotten</strong> is correct. The Past "
                       "Continuous sets the scene, and the Past Perfect reaches back to the cause — the "
                       "two tenses doing exactly the jobs they were made for.<br><br>"
                       "<em>(Past Continuous fonni chizadi, Past Perfect esa sababga qaytadi — ikkala "
                       "zamon ham oʻz vazifasini bajaryapti.)</em></p>",
    },
]


# =====================================================================
# PE-95 — Giving Your Opinion and Disagreeing Politely
# =====================================================================
Q_PE95 = [
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>___ my opinion, learning a language should start early.</strong></p>",
        "choices": ["To", "In", "By", "At"],
        "correct": "In",
        "explanation": "<p><strong>In</strong> is correct. <em>To my opinion</em> and <em>by my "
                       "opinion</em> are very common errors — the preposition is always <em>in</em>.<br><br>"
                       "<em>(<em>To my opinion</em> va <em>by my opinion</em> — juda koʻp uchraydigan "
                       "xatolar. Predlog doim <em>in</em> boʻladi.)</em></p>",
    },
    {
        "text": "<p>Elbek is replying to Charos. Choose the correct option.</p>"
                "<p><strong>I ___ with you about that.</strong></p>",
        "choices": ["am agree", "am agreed", "agreeing", "agree"],
        "correct": "agree",
        "explanation": "<p><strong>agree</strong> is correct. <em>Agree</em> is already a verb, so it "
                       "needs no <em>am</em> — <em>I am agree</em> is one of the most persistent errors "
                       "of all (PE-6).<br><br>"
                       "<em>(<em>Agree</em> ning oʻzi feʼl, shuning uchun <em>am</em> kerak emas. "
                       "<em>I am agree</em> — eng oʻjar xatolardan biri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ seems to me that children learn faster than adults.</strong></p>",
        "choices": ["It", "That", "This", "There"],
        "correct": "It",
        "explanation": "<p><strong>It</strong> is correct. <em>It seems to me that…</em> is a fixed "
                       "neutral opener, useful when you want to sound thoughtful rather than "
                       "certain.<br><br>"
                       "<em>(<em>It seems to me that…</em> — tayyor betaraf ibora, qatʼiy emas, oʻylangan "
                       "ohangda gapirmoqchi boʻlganda foydali.)</em></p>",
    },
    {
        "text": "<p>Choose the correct softener.</p>"
                "<p><strong>I'm ___ I don't quite agree with that.</strong></p>",
        "choices": ["sorry for", "fear", "afraid", "scared"],
        "correct": "afraid",
        "explanation": "<p><strong>afraid</strong> is correct. <em>I'm afraid…</em> has nothing to do "
                       "with fear here — it simply softens what comes next, like the Uzbek "
                       "\"afsuski\".<br><br>"
                       "<em>(Bu yerda <em>I'm afraid…</em> qoʻrquvga aloqador emas — u shunchaki keyingi "
                       "gapni yumshatadi, oʻzbekchadagi \"afsuski\" kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>On the one hand… ___ the other hand…</strong></p>",
        "choices": ["from", "in", "on", "by"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct. The phrase is <em>on the one hand … on the "
                       "other hand</em> — <em>from one hand</em> is a direct translation and is "
                       "wrong.<br><br>"
                       "<em>(Toʻgʻri shakl: <em>on the one hand … on the other hand</em>. <em>From one "
                       "hand</em> — soʻzma-soʻz tarjima va notoʻgʻri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz:</strong> I agree ___ a point, but there is another side to it.</p>",
        "choices": ["up to", "until", "till", "on"],
        "correct": "up to",
        "explanation": "<p><strong>up to</strong> is correct. <em>I agree up to a point</em> is the most "
                       "useful phrase in any discussion — it lets you accept part of an argument before "
                       "you challenge it.<br><br>"
                       "<em>(<em>I agree up to a point</em> — har qanday munozarada eng foydali ibora: "
                       "eʼtiroz bildirishdan oldin fikrning bir qismini tan olasiz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>You're absolutely right — I ___ agree more.</strong></p>",
        "choices": ["could", "don't", "wouldn't", "couldn't"],
        "correct": "couldn't",
        "explanation": "<p><strong>couldn't</strong> is correct. <em>I couldn't agree more</em> looks "
                       "negative but means the strongest possible agreement — \"toʻliq "
                       "qoʻshilaman\".<br><br>"
                       "<em>(<em>I couldn't agree more</em> tashqi koʻrinishidan inkor, lekin maʼnosi — "
                       "eng kuchli rozilik.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I see your ___, however I think the opposite is true.</strong></p>",
        "choices": ["opinion", "point", "idea", "thought"],
        "correct": "point",
        "explanation": "<p><strong>point</strong> is correct. <em>I see your point</em> is the "
                       "acknowledging step of the polite-disagreement formula.<br><br>"
                       "<em>(<em>I see your point</em> — muloyim eʼtiroz qolipidagi \"tan olish\" "
                       "bosqichi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option for an essay.</p>"
                "<p><strong>Iroda's essay:</strong> It could be ___ that phones distract students during lessons.</p>",
        "choices": ["agreed", "said to", "told", "argued"],
        "correct": "argued",
        "explanation": "<p><strong>argued</strong> is correct. <em>It could be argued that…</em> is the "
                       "formal, essay-level way to introduce a view without claiming it as your "
                       "own.<br><br>"
                       "<em>(<em>It could be argued that…</em> — fikrni oʻzingizniki deb daʼvo "
                       "qilmasdan keltirishning rasmiy, insho darajasidagi usuli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs:</strong> I am ___ that this is the best solution.</p>",
        "choices": ["convince", "convinced", "convincing", "conviction"],
        "correct": "convinced",
        "explanation": "<p><strong>convinced</strong> is correct. <em>I am convinced that…</em> and "
                       "<em>I strongly believe that…</em> are the strong end of the opinion scale — use "
                       "them for your main point only.<br><br>"
                       "<em>(<em>I am convinced that…</em> va <em>I strongly believe that…</em> — "
                       "fikr bildirishning eng kuchli shakllari. Ularni faqat asosiy fikringiz uchun "
                       "ishlating.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir:</strong> I ___ to think that reading is more useful than watching films.</p>",
        "choices": ["want", "like", "tend", "use"],
        "correct": "tend",
        "explanation": "<p><strong>tend</strong> is correct. <em>I tend to think…</em> is a careful "
                       "opener, alongside <em>As far as I know…</em> and <em>I may be wrong, "
                       "but…</em><br><br>"
                       "<em>(<em>I tend to think…</em> — ehtiyotkor ibora, <em>As far as I know…</em> va "
                       "<em>I may be wrong, but…</em> bilan bir qatorda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda:</strong> As ___ as I know, the course starts in June.</p>",
        "choices": ["far", "long", "much", "soon"],
        "correct": "far",
        "explanation": "<p><strong>far</strong> is correct. <em>As far as I know</em> marks information "
                       "you are not completely sure about — an honest and very useful hedge.<br><br>"
                       "<em>(<em>As far as I know</em> — toʻliq ishonchingiz komil boʻlmagan "
                       "maʼlumotni bildiradi; halol va juda foydali ibora.)</em></p>",
    },
    {
        "text": "<p>Which is too direct for a discussion in Sherbek's English club?</p>",
        "choices": [
            "That's nonsense.",
            "I'm not sure about that.",
            "I see it differently.",
            "I'm afraid I don't quite agree.",
        ],
        "correct": "That's nonsense.",
        "explanation": "<p><strong>That's nonsense.</strong> is too direct — it sounds aggressive in "
                       "English, even though the same words feel normal in Uzbek. This is a cultural "
                       "norm, not weakness.<br><br>"
                       "<em>(Bu ibora ingliz tilida qoʻpol eshitiladi, garchi oʻzbekchada oʻsha soʻzlar "
                       "odatiy tuyulsa ham. Bu — madaniy norma, zaiflik emas.)</em></p>",
    },
    {
        "text": "<p>Which phrase shows <strong>partial</strong> agreement?</p>",
        "choices": [
            "I completely agree.",
            "I couldn't agree more.",
            "I agree up to a point.",
            "You're absolutely right.",
        ],
        "correct": "I agree up to a point.",
        "explanation": "<p><strong>I agree up to a point.</strong> is partial agreement — the other three "
                       "are all full agreement. <em>That's true, but…</em> and <em>There is some truth "
                       "in that, although…</em> belong to the same group.<br><br>"
                       "<em>(Qolgan uchtasi — toʻliq rozilik. <em>That's true, but…</em> va <em>There is "
                       "some truth in that, although…</em> ham qismiy rozilik guruhiga kiradi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "To my opinion, it is wrong.",
            "In my opinion, it is wrong.",
            "By my opinion, it is wrong.",
            "At my opinion, it is wrong.",
        ],
        "correct": "In my opinion, it is wrong.",
        "explanation": "<p><strong>In my opinion, it is wrong.</strong> is correct — and in an essay use "
                       "the phrase once, not in every paragraph.<br><br>"
                       "<em>(Inshoda bu iborani bir marta ishlating, har bir xatboshida "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>What is the correct order of the polite-disagreement formula?</p>",
        "choices": [
            "your view → soften → acknowledge",
            "acknowledge → your view → soften",
            "soften → your view → acknowledge",
            "soften → acknowledge → your view",
        ],
        "correct": "soften → acknowledge → your view",
        "explanation": "<p><strong>soften → acknowledge → your view</strong> is correct: <em>I'm "
                       "afraid…</em> then <em>I can see why you think that, but…</em> then your own "
                       "opinion. Three steps and not one rude word.<br><br>"
                       "<em>(Yumshating, keyin tan oling, keyin oʻz fikringizni ayting — uch bosqich va "
                       "birorta ham qoʻpol soʻz yoʻq.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "I agree that this is good.",
            "I agree with your opinion about that this is good.",
            "In my view, phones should be allowed at break time.",
            "I see your point, but I don't quite agree.",
        ],
        "correct": "I agree with your opinion about that this is good.",
        "explanation": "<p><strong>I agree with your opinion about that this is good.</strong> is the "
                       "mistake — it stacks up words that are doing the same job. <em>I agree that this "
                       "is good</em> says it all.<br><br>"
                       "<em>(Bu gapda bir vazifani bajaradigan soʻzlar uyum boʻlib ketgan. <em>I agree "
                       "that this is good</em> — hammasi shu.)</em></p>",
    },
    {
        "text": "<p>Which is correct?</p>",
        "choices": [
            "From one hand… from other hand…",
            "In one hand… in other hand…",
            "At one hand… at other hand…",
            "On the one hand… on the other hand…",
        ],
        "correct": "On the one hand… on the other hand…",
        "explanation": "<p><strong>On the one hand… on the other hand…</strong> is correct. This pair "
                       "plus <em>In my view…</em> gives any essay or speaking answer a clear, balanced "
                       "shape.<br><br>"
                       "<em>(Bu juftlik va <em>In my view…</em> har qanday insho yoki ogʻzaki javobga "
                       "aniq, muvozanatli tuzilish beradi.)</em></p>",
    },
    {
        "text": "<p>Samandar says: \"Students shouldn't have any homework at all.\" "
                "Which reply disagrees politely?</p>",
        "choices": [
            "I see your point, but I'm afraid I don't quite agree. A little homework helps us remember the lesson.",
            "No, you are wrong. Homework is necessary.",
            "That's nonsense — homework helps us.",
            "You don't understand. Homework is important.",
        ],
        "correct": "I see your point, but I'm afraid I don't quite agree. A little homework helps us remember the lesson.",
        "explanation": "<p>The first reply is the polite one — it acknowledges, softens and only then "
                       "gives the opposite view. The other three would sound aggressive to an English "
                       "speaker.<br><br>"
                       "<em>(Birinchi javob tan oladi, yumshatadi va shundan keyingina qarama-qarshi "
                       "fikrni aytadi. Qolgan uchtasi ingliz tilida qoʻpol eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Learning grammar is boring, isn't it?</p>"
                "<p><strong>Marjona:</strong> ___</p>",
        "choices": [
            "I am agree, to my opinion it is boring.",
            "No, you are wrong.",
            "I agree up to a point — some exercises are dull. However, grammar makes everything else easier.",
            "I agree up to point, but grammar make everything easier.",
        ],
        "correct": "I agree up to a point — some exercises are dull. However, grammar makes everything else easier.",
        "explanation": "<p>Marjona's reply is the model answer: partial agreement first, then her own "
                       "view, joined by a linking word (PE-88). Polite, balanced and grammatically "
                       "clean.<br><br>"
                       "<em>(Avval qismiy rozilik, keyin oʻz fikri — bogʻlovchi soʻz bilan. Muloyim, "
                       "muvozanatli va grammatik jihatdan toza javob.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-91 Practice: Formal vs Informal English",
        "tutorial":    "PE-91:",
        "description": "PE-91 darsiga 20 savol: uslubning toʻrt belgisi, kundalik feʼllarning rasmiy "
                       "muqobillari, salomlashuv va xayrlashuv juftliklari, qaysi vazifa qaysi uslubni "
                       "talab qilishi. Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE91,
    },
    {
        "title":       "PE-92 Practice: The 20 Mistakes Uzbek Speakers Make Most",
        "tutorial":    "PE-92:",
        "description": "PE-92 darsiga 20 savol: oʻzbek tilidan kelib chiqadigan eng koʻp uchraydigan "
                       "20 xato — soʻz tartibi, artikllar, zamonlar, predloglar va qoʻsh inkor. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE92,
    },
    {
        "title":       "PE-93 Practice: Writing an Email: Grammar That Sounds Polite",
        "tutorial":    "PE-93:",
        "description": "PE-93 darsiga 20 savol: xatning besh qismi, mos salomlashuv va xayrlashuv, "
                       "muloyim iltimos grammatikasi va tayyor iboralar. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE93,
    },
    {
        "title":       "PE-94 Practice: Telling a Story: Narrative Tenses in Action",
        "tutorial":    "PE-94:",
        "description": "PE-94 darsiga 20 savol: Past Continuous (fon), Past Simple (voqealar), "
                       "Past Perfect (undan oldingi sabab), hikoyaning toʻrt qismi va vaqt soʻzlari. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE94,
    },
    {
        "title":       "PE-95 Practice: Giving Your Opinion and Disagreeing Politely",
        "tutorial":    "PE-95:",
        "description": "PE-95 darsiga 20 savol: fikr bildirish iboralari, toʻliq va qismiy rozilik, "
                       "muloyim eʼtiroz qolipi (yumshatish + tan olish + oʻz fikri) va muvozanatli "
                       "insho tuzilishi. Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE95,
    },
]
