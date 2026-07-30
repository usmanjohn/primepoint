# -*- coding: utf-8 -*-
"""Prime English practices — PE-16 … PE-20.

Written with STYLE_GUIDE_PE_PRACTICE.md · lesson list in toc_pe_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_16_20.py --master=prime
"""

SUBJECT = {
    "name":        "English",
    "description": "English grammar and vocabulary practice",
    "icon":        "bi-translate",
    "color":       "#6366f1",
}

DEFAULTS = {
    "level":                "easy",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PE-16 — Prepositions of Place: in, on, at
# =====================================================================

Q_PE16 = [
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>The keys are ___ the table.</strong></p>",
        "choices": ["on", "in", "at", "to"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct — the keys are touching a flat surface."
                       "<br><br><em>(<strong>on</strong> toʻgʻri — kalitlar tekis sirtga tegib "
                       "turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>My money is ___ my bag.</strong></p>",
        "choices": ["in", "on", "at", "by"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct — inside something with walls or edges."
                       "<br><br><em>(<strong>in</strong> toʻgʻri — devor yoki chegarasi bor narsaning "
                       "ichida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Jasur is waiting ___ the gate.</strong></p>",
        "choices": ["at", "in", "on", "to"],
        "correct": "at",
        "explanation": "<p><strong>at</strong> is correct — a point on the map, an exact spot.<br><br>"
                       "<em>(<strong>at</strong> toʻgʻri — xaritadagi nuqta, aniq bir joy.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>My cousin lives ___ Samarkand.</strong></p>",
        "choices": ["in", "at", "on", "to"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct — cities, regions and countries are spaces you "
                       "are inside: <em>in Samarkand, in Uzbekistan</em>.<br><br>"
                       "<em>(<strong>in</strong> toʻgʻri — shahar, viloyat va davlatlar ichida "
                       "boʻlinadigan makonlar: <em>in Samarkand, in Uzbekistan</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>There is a big picture ___ the wall.</strong></p>",
        "choices": ["on", "in", "at", "over"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct — the picture touches the surface of the wall."
                       "<br><br><em>(<strong>on</strong> toʻgʻri — rasm devor sirtiga tegib "
                       "turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>We live ___ the fourth floor.</strong></p>",
        "choices": ["on", "in", "at", "over"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct. A floor is a level — a surface — so English "
                       "says <em>on the fourth floor</em>.<br><br>"
                       "<em>(<strong>on</strong> toʻgʻri. Qavat — bu satx, shuning uchun ingliz tilida "
                       "<em>on the fourth floor</em> deyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>I usually stay ___ home at the weekend.</strong></p>",
        "choices": ["at", "in", "on", "to"],
        "correct": "at",
        "explanation": "<p><strong>at</strong> is correct — <em>at home</em> is a fixed phrase, with no "
                       "<em>the</em> and no <em>in</em>.<br><br>"
                       "<em>(<strong>at</strong> toʻgʻri — <em>at home</em> qatʼiy ibora, <em>the</em> "
                       "ham, <em>in</em> ham qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Afsona is ___ school now — her lessons finish at two.</strong></p>",
        "choices": ["at", "in", "on", "by"],
        "correct": "at",
        "explanation": "<p><strong>at</strong> is correct. <em>At school</em> means she is there for its "
                       "purpose — studying. <em>In the school</em> would mean physically inside the "
                       "building.<br><br>"
                       "<em>(<strong>at</strong> toʻgʻri. <em>At school</em> — u oʻqish uchun oʻsha "
                       "yerda. <em>In the school</em> esa jismonan bino ichida degan maʼnoni "
                       "beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>My grandmother is ___ bed — she isn't feeling well.</strong></p>",
        "choices": ["in", "on", "at", "into"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct — <em>in bed</em> (fixed phrase, no article) "
                       "means lying in it to sleep or rest.<br><br>"
                       "<em>(<strong>in</strong> toʻgʻri — <em>in bed</em> (qatʼiy ibora, artiklsiz) "
                       "uxlash yoki dam olish uchun yotganini bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Write your name ___ the top of the page.</strong></p>",
        "choices": ["at", "in", "on", "over"],
        "correct": "at",
        "explanation": "<p><strong>at</strong> is correct — <em>at the top / at the bottom / at the "
                       "corner</em> are all points.<br><br>"
                       "<em>(<strong>at</strong> toʻgʻri — <em>at the top / at the bottom / at the "
                       "corner</em> — hammasi nuqta.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>The post office is ___ the left, next to the bank.</strong></p>",
        "choices": ["on", "in", "at", "to"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct — <em>on the left / on the right</em> are fixed "
                       "phrases.<br><br>"
                       "<em>(<strong>on</strong> toʻgʻri — <em>on the left / on the right</em> qatʼiy "
                       "iboralar.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>We went to Bukhara ___ a car.</strong></p>",
        "choices": ["in", "on", "at", "by the"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct. You sit inside a car, so <em>in a car</em> — "
                       "but you walk about inside a bus or a train, so <em>on the bus, on the "
                       "train</em>.<br><br>"
                       "<em>(<strong>in</strong> toʻgʻri. Mashinada ichida oʻtiriladi — <em>in a "
                       "car</em>, avtobus yoki poyezdda esa yurish mumkin, shuning uchun <em>on the bus, "
                       "on the train</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>I met my teacher ___ the bus this morning.</strong></p>",
        "choices": ["on", "in", "at", "by"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct — buses, trains and planes are big enough to "
                       "walk in, so English uses <em>on</em>.<br><br>"
                       "<em>(<strong>on</strong> toʻgʻri — avtobus, poyezd va samolyot ichida yurish "
                       "mumkin, shuning uchun ingliz tilida <em>on</em> ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>The cat is sleeping ___ the chair — you can't see it.</strong></p>",
        "choices": ["under", "on", "at", "in"],
        "correct": "under",
        "explanation": "<p><strong>under</strong> is correct — below something, out of sight.<br><br>"
                       "<em>(<strong>under</strong> toʻgʻri — biror narsaning ostida, koʻrinmaydigan "
                       "joyda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>The shop is ___ the bank and the pharmacy.</strong></p>",
        "choices": ["between", "among", "next", "in front"],
        "correct": "between",
        "explanation": "<p><strong>between</strong> is correct — with two things named. <em>Among</em> is "
                       "for a crowd of many.<br><br>"
                       "<em>(<strong>between</strong> toʻgʻri — ikki narsa aytilganda. <em>Among</em> esa "
                       "koʻp narsa orasida boʻlganda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Our school is ___ my house — I only cross the road.</strong></p>",
        "choices": ["opposite", "in front", "next", "between"],
        "correct": "opposite",
        "explanation": "<p><strong>opposite</strong> is correct — on the other side, facing it. "
                       "<em>In front of</em> and <em>next to</em> need the <em>of / to</em>.<br><br>"
                       "<em>(<strong>opposite</strong> toʻgʻri — roʻparasida, qarama-qarshi tomonda. "
                       "<em>In front of</em> va <em>next to</em> esa <em>of / to</em> ni talab "
                       "qiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I am in home now.", "I am at home now.",
                    "I am in my room now.", "I am at the bus stop now."],
        "correct": "I am in home now.",
        "explanation": "<p><strong>I am in home now.</strong> is the mistake — the fixed phrase is "
                       "<em>at home</em>. Uzbek <em>uyda</em> gives no clue, so this must be "
                       "learned.<br><br>"
                       "<em>(<strong>I am in home now.</strong> xato — qatʼiy ibora <em>at home</em>. "
                       "Oʻzbekcha <em>uyda</em> hech qanday ishora bermaydi, shuning uchun buni yodlash "
                       "kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["My books are on the shelf in my room.",
                    "My books are in the shelf on my room.",
                    "My books are at the shelf in my room.",
                    "My books are on the shelf at my room."],
        "correct": "My books are on the shelf in my room.",
        "explanation": "<p><strong>My books are on the shelf in my room.</strong> is correct — a shelf is "
                       "a surface (<em>on</em>), a room is a space (<em>in</em>).<br><br>"
                       "<em>(<strong>My books are on the shelf in my room.</strong> toʻgʻri — javon — "
                       "sirt (<em>on</em>), xona — makon (<em>in</em>).)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> Where shall we meet?</p>"
                "<p><strong>B:</strong> ___</p>",
        "choices": ["At the bus stop in front of the school.",
                    "In the bus stop at front of the school.",
                    "On the bus stop in front the school.",
                    "At the bus stop on front of the school."],
        "correct": "At the bus stop in front of the school.",
        "explanation": "<p><strong>At the bus stop in front of the school.</strong> is correct — a bus "
                       "stop is a point (<em>at</em>), and the full phrase is <em>in front "
                       "of</em>.<br><br>"
                       "<em>(<strong>At the bus stop in front of the school.</strong> toʻgʻri — bekat "
                       "nuqta (<em>at</em>), toʻliq ibora esa <em>in front of</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> preposition is correct.</p>",
        "choices": ["Sherbek is at the bus stop, his bag is on the ground and his phone is in his pocket.",
                    "Sherbek is on the bus stop, his bag is in the ground and his phone is at his pocket.",
                    "Sherbek is in the bus stop, his bag is at the ground and his phone is on his pocket.",
                    "Sherbek is at the bus stop, his bag is in the ground and his phone is on his pocket."],
        "correct": "Sherbek is at the bus stop, his bag is on the ground and his phone is in his pocket.",
        "explanation": "<p><strong>at the bus stop … on the ground … in his pocket</strong> is correct — "
                       "a point, a surface, an inside space: the zoom logic in one sentence.<br><br>"
                       "<em>(<strong>at the bus stop … on the ground … in his pocket</strong> toʻgʻri — "
                       "nuqta, sirt va ichki makon: bitta gapda butun mantiq.)</em></p>",
    },
]


# =====================================================================
# PE-17 — Prepositions of Time: in, on, at
# =====================================================================

Q_PE17 = [
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>The lesson starts ___ 8:30.</strong></p>",
        "choices": ["at", "in", "on", "by"],
        "correct": "at",
        "explanation": "<p><strong>at</strong> is correct — exact clock times are points in time."
                       "<br><br><em>(<strong>at</strong> toʻgʻri — aniq soat vaqti — vaqtdagi "
                       "nuqta.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>We have English ___ Monday.</strong></p>",
        "choices": ["on", "in", "at", "by"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct — days take <em>on</em>. If the idea contains a "
                       "day, <em>on</em> is your word.<br><br>"
                       "<em>(<strong>on</strong> toʻgʻri — kunlar <em>on</em> oladi. Agar maʼnoda kun "
                       "boʻlsa, <em>on</em> ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>My brother was born ___ 2010.</strong></p>",
        "choices": ["in", "on", "at", "by"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct — years, months and seasons are long periods."
                       "<br><br><em>(<strong>in</strong> toʻgʻri — yil, oy va fasllar — uzoq davrlar.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Navruz is ___ March.</strong></p>",
        "choices": ["in", "on", "at", "by"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct — a month alone takes <em>in</em>. With a date "
                       "it changes: <em>on 21 March</em>.<br><br>"
                       "<em>(<strong>in</strong> toʻgʻri — oy yolgʻiz kelsa <em>in</em> oladi. Sana bilan "
                       "kelsa oʻzgaradi: <em>on 21 March</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>My birthday is ___ 12 May.</strong></p>",
        "choices": ["on", "in", "at", "of"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct — a full date names a day, so <em>on</em>."
                       "<br><br><em>(<strong>on</strong> toʻgʻri — toʻliq sana kunni bildiradi, shuning "
                       "uchun <em>on</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>I do my homework ___ the evening.</strong></p>",
        "choices": ["in", "on", "at", "by"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct — <em>in the morning, in the afternoon, in the "
                       "evening</em> — but <em>at night</em> is the odd one out.<br><br>"
                       "<em>(<strong>in</strong> toʻgʻri — <em>in the morning, in the afternoon, in the "
                       "evening</em> — lekin <em>at night</em> istisno.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Cats can see well ___ night.</strong></p>",
        "choices": ["at", "in", "on", "by"],
        "correct": "at",
        "explanation": "<p><strong>at</strong> is correct — <em>at night</em> is the exception in the "
                       "family: <em>in the morning</em> but <em>at night</em>.<br><br>"
                       "<em>(<strong>at</strong> toʻgʻri — <em>at night</em> — bu guruhdagi istisno: "
                       "<em>in the morning</em>, lekin <em>at night</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>I always help my mother ___ Sunday morning.</strong></p>",
        "choices": ["on", "in", "at", "by"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct. Normally <em>in the morning</em>, but as soon "
                       "as a day is named the whole phrase takes <em>on</em>: <em>on Sunday "
                       "morning</em>.<br><br>"
                       "<em>(<strong>on</strong> toʻgʻri. Odatda <em>in the morning</em>, lekin kun "
                       "aytilishi bilan butun ibora <em>on</em> oladi: <em>on Sunday "
                       "morning</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>It is very hot here ___ summer.</strong></p>",
        "choices": ["in", "on", "at", "by"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct — seasons are long periods: <em>in summer, in "
                       "winter</em>.<br><br>"
                       "<em>(<strong>in</strong> toʻgʻri — fasllar uzoq davrlar: <em>in summer, in "
                       "winter</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I will call you ___ .</strong></p>",
        "choices": ["tomorrow", "on tomorrow", "in tomorrow", "at tomorrow"],
        "correct": "tomorrow",
        "explanation": "<p><strong>tomorrow</strong> is correct. <em>Yesterday, today, tomorrow, "
                       "tonight, next week, last year, every day</em> take <strong>no "
                       "preposition</strong> — a very common mistake.<br><br>"
                       "<em>(<strong>tomorrow</strong> toʻgʻri. <em>Yesterday, today, tomorrow, tonight, "
                       "next week, last year, every day</em> oldiga <strong>predlog "
                       "qoʻyilmaydi</strong> — juda koʻp uchraydigan xato.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We visited our grandparents ___ .</strong></p>",
        "choices": ["last week", "in last week", "on last week", "at last week"],
        "correct": "last week",
        "explanation": "<p><strong>last week</strong> is correct — <em>last / next / this</em> phrases "
                       "never take a preposition.<br><br>"
                       "<em>(<strong>last week</strong> toʻgʻri — <em>last / next / this</em> bilan "
                       "kelgan iboralar predlog olmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>I don't work ___ the weekend.</strong></p>",
        "choices": ["at", "in", "on the", "by"],
        "correct": "at",
        "explanation": "<p><strong>at</strong> is correct in British English: <em>at the weekend</em>. "
                       "(Americans say <em>on the weekend</em>.)<br><br>"
                       "<em>(<strong>at</strong> toʻgʻri — britancha uslubda <em>at the weekend</em>. "
                       "(Amerikada <em>on the weekend</em> deyiladi.))</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>The film starts ___ a quarter past seven.</strong></p>",
        "choices": ["at", "in", "on", "by"],
        "correct": "at",
        "explanation": "<p><strong>at</strong> is correct — still a clock time, however it is "
                       "written.<br><br>"
                       "<em>(<strong>at</strong> toʻgʻri — qanday yozilishidan qatʼi nazar, bu ham soat "
                       "vaqti.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>She was born ___ 2011, ___ a cold winter day.</strong></p>",
        "choices": ["in … on", "on … in", "at … on", "in … at"],
        "correct": "in … on",
        "explanation": "<p><strong>in … on</strong> is correct — the year is a long period, the day is a "
                       "day.<br><br>"
                       "<em>(<strong>in … on</strong> toʻgʻri — yil uzoq davr, kun esa kun.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which phrase needs <em>no</em> preposition?</strong></p>",
        "choices": ["next Monday", "9 o'clock", "the summer", "12 April"],
        "correct": "next Monday",
        "explanation": "<p><strong>next Monday</strong> is correct — <em>next</em> already fixes the "
                       "time, so no preposition is used.<br><br>"
                       "<em>(<strong>next Monday</strong> toʻgʻri — <em>next</em> vaqtni allaqachon "
                       "belgilab bergan, shuning uchun predlog kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Let's meet ___ lunchtime.</strong></p>",
        "choices": ["at", "in", "on", "by"],
        "correct": "at",
        "explanation": "<p><strong>at</strong> is correct — the culture treats <em>lunchtime</em> as one "
                       "point, like <em>at noon</em> and <em>at midnight</em>.<br><br>"
                       "<em>(<strong>at</strong> toʻgʻri — <em>lunchtime</em> bitta nuqta sifatida "
                       "qaraladi, xuddi <em>at noon</em> va <em>at midnight</em> kabi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I saw him in yesterday.", "I saw him yesterday.",
                    "I saw him on Monday.", "I saw him at six o'clock."],
        "correct": "I saw him in yesterday.",
        "explanation": "<p><strong>I saw him in yesterday.</strong> is the mistake — <em>yesterday</em> "
                       "takes no preposition at all.<br><br>"
                       "<em>(<strong>I saw him in yesterday.</strong> xato — <em>yesterday</em> hech "
                       "qanday predlog olmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["My exam is on 5 June at nine o'clock.",
                    "My exam is in 5 June on nine o'clock.",
                    "My exam is at 5 June in nine o'clock.",
                    "My exam is on 5 June in nine o'clock."],
        "correct": "My exam is on 5 June at nine o'clock.",
        "explanation": "<p><strong>My exam is on 5 June at nine o'clock.</strong> is correct — date → "
                       "<em>on</em>, clock time → <em>at</em>.<br><br>"
                       "<em>(<strong>My exam is on 5 June at nine o'clock.</strong> toʻgʻri — sana → "
                       "<em>on</em>, soat → <em>at</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> When does your holiday start?</p>"
                "<p><strong>B:</strong> ___</p>",
        "choices": ["On 1 June, so in two weeks.", "In 1 June, so on two weeks.",
                    "At 1 June, so in two weeks.", "On 1 June, so at two weeks."],
        "correct": "On 1 June, so in two weeks.",
        "explanation": "<p><strong>On 1 June, so in two weeks.</strong> is correct — a date takes "
                       "<em>on</em>, and <em>in two weeks</em> means “after two weeks from now”."
                       "<br><br><em>(<strong>On 1 June, so in two weeks.</strong> toʻgʻri — sana "
                       "<em>on</em> oladi, <em>in two weeks</em> esa “ikki haftadan keyin” "
                       "degani.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> preposition is correct.</p>",
        "choices": ["We have lessons on Monday at eight, and we rest in August.",
                    "We have lessons in Monday on eight, and we rest at August.",
                    "We have lessons at Monday in eight, and we rest on August.",
                    "We have lessons on Monday in eight, and we rest at August."],
        "correct": "We have lessons on Monday at eight, and we rest in August.",
        "explanation": "<p><strong>on Monday … at eight … in August</strong> is correct — day, clock "
                       "time, month: the zoom-out logic from smallest to biggest.<br><br>"
                       "<em>(<strong>on Monday … at eight … in August</strong> toʻgʻri — kun, soat, oy: "
                       "kichikdan kattaga qarab kengayish mantiqi.)</em></p>",
    },
]


# =====================================================================
# PE-18 — Question Words: who, what, where, when, why, how
# =====================================================================

Q_PE18 = [
    {
        "text": "<p>Choose the correct question word.</p>"
                "<p><strong>___ is your English teacher?</strong></p>",
        "choices": ["Who", "What", "Where", "How"],
        "correct": "Who",
        "explanation": "<p><strong>Who</strong> is correct — it asks about a person (<em>kim</em>)."
                       "<br><br><em>(<strong>Who</strong> toʻgʻri — u shaxs haqida soʻraydi "
                       "(<em>kim</em>).)</em></p>",
    },
    {
        "text": "<p>Choose the correct question word.</p>"
                "<p><strong>___ do you live?</strong></p>",
        "choices": ["Where", "What", "Who", "When"],
        "correct": "Where",
        "explanation": "<p><strong>Where</strong> is correct — it asks about a place "
                       "(<em>qayerda</em>).<br><br>"
                       "<em>(<strong>Where</strong> toʻgʻri — u joy haqida soʻraydi "
                       "(<em>qayerda</em>).)</em></p>",
    },
    {
        "text": "<p>Choose the correct question word.</p>"
                "<p><strong>___ does the film start? — At seven.</strong></p>",
        "choices": ["When", "Where", "Why", "Who"],
        "correct": "When",
        "explanation": "<p><strong>When</strong> is correct — it asks about time "
                       "(<em>qachon</em>).<br><br>"
                       "<em>(<strong>When</strong> toʻgʻri — u vaqt haqida soʻraydi "
                       "(<em>qachon</em>).)</em></p>",
    },
    {
        "text": "<p>Choose the correct question word.</p>"
                "<p><strong>___ are you late? — Because the bus didn't come.</strong></p>",
        "choices": ["Why", "How", "What", "When"],
        "correct": "Why",
        "explanation": "<p><strong>Why</strong> is correct — it asks for a reason, and the answer usually "
                       "starts with <em>because</em>.<br><br>"
                       "<em>(<strong>Why</strong> toʻgʻri — u sabab soʻraydi, javob esa koʻpincha "
                       "<em>because</em> bilan boshlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question word.</p>"
                "<p><strong>___ do you go to school? — By bus.</strong></p>",
        "choices": ["How", "What", "Where", "Who"],
        "correct": "How",
        "explanation": "<p><strong>How</strong> is correct — it asks about the way or the means "
                       "(<em>qanday</em>).<br><br>"
                       "<em>(<strong>How</strong> toʻgʻri — u usul yoki vosita haqida soʻraydi "
                       "(<em>qanday</em>).)</em></p>",
    },
    {
        "text": "<p>Choose the correct word order.</p>",
        "choices": ["Where does your father work?", "Where your father works?",
                    "Where works your father?", "Where does work your father?"],
        "correct": "Where does your father work?",
        "explanation": "<p><strong>Where does your father work?</strong> is correct — the order never "
                       "changes: <em>Wh- word + helper + subject + verb</em>.<br><br>"
                       "<em>(<strong>Where does your father work?</strong> toʻgʻri — tartib "
                       "oʻzgarmaydi: <em>Wh- soʻzi + yordamchi + subject + feʼl</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ old is your sister?</strong></p>",
        "choices": ["How", "What", "Which", "Who"],
        "correct": "How",
        "explanation": "<p><strong>How</strong> is correct — <em>how</em> joins an adjective to make a "
                       "family: <em>how old, how tall, how far, how often</em>.<br><br>"
                       "<em>(<strong>How</strong> toʻgʻri — <em>how</em> sifat bilan qoʻshilib butun "
                       "guruh yasaydi: <em>how old, how tall, how far, how often</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ is it from here to the bazaar?</strong></p>",
        "choices": ["How far", "How long", "How much", "How many"],
        "correct": "How far",
        "explanation": "<p><strong>How far</strong> is correct — distance. <em>How long</em> would ask "
                       "about time or length.<br><br>"
                       "<em>(<strong>How far</strong> toʻgʻri — masofa. <em>How long</em> esa vaqt yoki "
                       "uzunlik haqida soʻraydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ pupils are there in your class?</strong></p>",
        "choices": ["How many", "How much", "How far", "What"],
        "correct": "How many",
        "explanation": "<p><strong>How many</strong> is correct — countable plural. <em>How much</em> "
                       "goes with uncountables (PE-2).<br><br>"
                       "<em>(<strong>How many</strong> toʻgʻri — sanaladigan koʻplik. <em>How much</em> "
                       "esa sanalmaydiganlar bilan keladi (PE-2).)</em></p>",
    },
    {
        "text": "<p>Choose the correct question word.</p>"
                "<p><strong>___ bag is this? — It's mine.</strong></p>",
        "choices": ["Whose", "Who's", "Who", "Which"],
        "correct": "Whose",
        "explanation": "<p><strong>Whose</strong> is correct — it asks about the owner "
                       "(<em>kimning</em>). <em>Who's</em> means <em>who is</em>.<br><br>"
                       "<em>(<strong>Whose</strong> toʻgʻri — u egasini soʻraydi (<em>kimning</em>). "
                       "<em>Who's</em> esa <em>who is</em> degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question word.</p>"
                "<p><strong>___ do you prefer, tea or coffee?</strong></p>",
        "choices": ["Which", "What", "Who", "How"],
        "correct": "Which",
        "explanation": "<p><strong>Which</strong> is correct — a choice from a small, known group. "
                       "<em>What</em> is an open choice from everything.<br><br>"
                       "<em>(<strong>Which</strong> toʻgʻri — kichik, maʼlum guruhdan tanlov. "
                       "<em>What</em> esa cheklanmagan, ochiq tanlov.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ is your favourite colour?</strong></p>",
        "choices": ["What", "Which", "Who", "How"],
        "correct": "What",
        "explanation": "<p><strong>What</strong> is correct — the choice is open, from all colours."
                       "<br><br><em>(<strong>What</strong> toʻgʻri — tanlov ochiq, barcha ranglar "
                       "orasidan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Who ___ the window? (Somebody broke it.)</strong></p>",
        "choices": ["broke", "did break", "does break", "breaking"],
        "correct": "broke",
        "explanation": "<p><strong>broke</strong> is correct. When <em>who</em> is the subject of the "
                       "question, the helper disappears and the verb goes straight after it.<br><br>"
                       "<em>(<strong>broke</strong> toʻgʻri. <em>Who</em> savolning subjecti boʻlsa, "
                       "yordamchi tushib qoladi va feʼl darhol undan keyin keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Who ___ you invite to your birthday?</strong></p>",
        "choices": ["did", "does", "was", "is"],
        "correct": "did",
        "explanation": "<p><strong>did</strong> is correct. Here <em>who</em> is the <em>object</em> — "
                       "the person invited — so the normal helper comes back.<br><br>"
                       "<em>(<strong>did</strong> toʻgʻri. Bu yerda <em>who</em> — object, yaʼni taklif "
                       "qilingan shaxs, shuning uchun oddiy yordamchi qaytib keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ are you waiting for?</strong></p>",
        "choices": ["Who", "Whom is", "Who for", "For who is"],
        "correct": "Who",
        "explanation": "<p><strong>Who</strong> is correct. English leaves the preposition at the end of "
                       "the question: <em>Who are you waiting for?</em> — strange, but completely "
                       "normal.<br><br>"
                       "<em>(<strong>Who</strong> toʻgʻri. Ingliz tilida predlog savol oxirida qoladi: "
                       "<em>Who are you waiting for?</em> — gʻalati, lekin mutlaqo "
                       "tabiiy.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ are you talking about?</strong></p>",
        "choices": ["What", "About what is", "What about is", "Whats"],
        "correct": "What",
        "explanation": "<p><strong>What</strong> is correct — same pattern, with the preposition "
                       "<em>about</em> left at the end.<br><br>"
                       "<em>(<strong>What</strong> toʻgʻri — xuddi shu qolip, <em>about</em> predlogi "
                       "oxirida qoladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Where you live?", "Where do you live?",
                    "Where does she live?", "Where are you now?"],
        "correct": "Where you live?",
        "explanation": "<p><strong>Where you live?</strong> is the mistake — the helper <em>do</em> is "
                       "missing. Only <em>to be</em> may stand there alone.<br><br>"
                       "<em>(<strong>Where you live?</strong> xato — <em>do</em> yordamchisi yoʻq. Faqat "
                       "<em>to be</em> u yerda yolgʻiz turishi mumkin.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["How many brothers do you have?", "How much brothers do you have?",
                    "How many brothers you have?", "How many brothers does you have?"],
        "correct": "How many brothers do you have?",
        "explanation": "<p><strong>How many brothers do you have?</strong> is correct — countable noun → "
                       "<em>how many</em>, and <em>you</em> → <em>do</em>.<br><br>"
                       "<em>(<strong>How many brothers do you have?</strong> toʻgʻri — sanaladigan ot → "
                       "<em>how many</em>, <em>you</em> → <em>do</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> ___</p>"
                "<p><strong>B:</strong> Because I want to study in Korea.</p>",
        "choices": ["Why are you learning Korean?", "What are you learning Korean?",
                    "Why you are learning Korean?", "Why do you learning Korean?"],
        "correct": "Why are you learning Korean?",
        "explanation": "<p><strong>Why are you learning Korean?</strong> is correct — the answer with "
                       "<em>because</em> tells you the question was <em>why</em>, and the Continuous uses "
                       "<em>are</em> with no <em>do</em>.<br><br>"
                       "<em>(<strong>Why are you learning Korean?</strong> toʻgʻri — <em>because</em> "
                       "bilan javob savol <em>why</em> boʻlganini koʻrsatadi, Continuous esa "
                       "<em>do</em> siz <em>are</em> ni oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> question is correct.</p>",
        "choices": ["Where do you live? How old are you? What does your father do?",
                    "Where you live? How old you are? What your father does?",
                    "Where do you live? How old do you be? What does your father does?",
                    "Where does you live? How old are you? What do your father do?"],
        "correct": "Where do you live? How old are you? What does your father do?",
        "explanation": "<p><strong>Where do you live? How old are you? What does your father do?</strong> "
                       "is correct — an ordinary verb takes <em>do / does</em>, <em>to be</em> needs no "
                       "helper at all.<br><br>"
                       "<em>(<strong>Where do you live? How old are you? What does your father "
                       "do?</strong> toʻgʻri — oddiy feʼl <em>do / does</em> oladi, <em>to be</em> ga esa "
                       "yordamchi umuman kerak emas.)</em></p>",
    },
]


# =====================================================================
# PE-19 — Past Simple of "to be": was / were
# =====================================================================

Q_PE19 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ at home yesterday evening.</strong></p>",
        "choices": ["was", "were", "am", "is"],
        "correct": "was",
        "explanation": "<p><strong>was</strong> is correct — <em>I, he, she, it</em> take <em>was</em>."
                       "<br><br><em>(<strong>was</strong> toʻgʻri — <em>I, he, she, it</em> <em>was</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My parents ___ at work yesterday.</strong></p>",
        "choices": ["were", "was", "are", "is"],
        "correct": "were",
        "explanation": "<p><strong>were</strong> is correct — <em>you, we, they</em> and all plural "
                       "subjects take <em>were</em>.<br><br>"
                       "<em>(<strong>were</strong> toʻgʻri — <em>you, we, they</em> va barcha koʻplikdagi "
                       "subjectlar <em>were</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ ill last week, so she missed three lessons.</strong></p>",
        "choices": ["was", "were", "is", "did"],
        "correct": "was",
        "explanation": "<p><strong>was</strong> is correct — one person + a finished past time."
                       "<br><br><em>(<strong>was</strong> toʻgʻri — bitta shaxs + oʻtgan, tugagan "
                       "vaqt.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>You ___ very kind to me that day. Thank you.</strong></p>",
        "choices": ["were", "was", "are", "did"],
        "correct": "were",
        "explanation": "<p><strong>were</strong> is correct — <em>you</em> always takes <em>were</em>, "
                       "even for one person.<br><br>"
                       "<em>(<strong>were</strong> toʻgʻri — <em>you</em> doim <em>were</em> oladi, hatto "
                       "bir kishi haqida boʻlsa ham.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The weather ___ terrible last Sunday.</strong></p>",
        "choices": ["was", "were", "is", "are"],
        "correct": "was",
        "explanation": "<p><strong>was</strong> is correct — <em>the weather</em> is one uncountable "
                       "thing.<br><br>"
                       "<em>(<strong>was</strong> toʻgʻri — <em>the weather</em> bitta sanalmaydigan "
                       "tushuncha.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>I ___ at school yesterday — I was ill.</strong></p>",
        "choices": ["wasn't", "weren't", "didn't", "amn't"],
        "correct": "wasn't",
        "explanation": "<p><strong>wasn't</strong> is correct. <em>To be</em> makes its own negative in "
                       "the past too — no <em>didn't</em>.<br><br>"
                       "<em>(<strong>wasn't</strong> toʻgʻri. <em>To be</em> oʻtgan zamonda ham inkorni "
                       "oʻzi yasaydi — <em>didn't</em> kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>They ___ at the party — they stayed at home.</strong></p>",
        "choices": ["weren't", "wasn't", "didn't", "aren't"],
        "correct": "weren't",
        "explanation": "<p><strong>weren't</strong> is correct — plural subject → "
                       "<em>were not = weren't</em>.<br><br>"
                       "<em>(<strong>weren't</strong> toʻgʻri — koʻplikdagi subject → "
                       "<em>were not = weren't</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ you at the stadium last night?</strong></p>",
        "choices": ["Were", "Was", "Did", "Are"],
        "correct": "Were",
        "explanation": "<p><strong>Were</strong> is correct — the verb jumps in front of the subject, "
                       "exactly as in the present.<br><br>"
                       "<em>(<strong>Were</strong> toʻgʻri — feʼl subject oldiga chiqadi, xuddi hozirgi "
                       "zamondagidek.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ the film interesting?</strong></p>",
        "choices": ["Was", "Were", "Did", "Is"],
        "correct": "Was",
        "explanation": "<p><strong>Was</strong> is correct — <em>the film</em> is singular.<br><br>"
                       "<em>(<strong>Was</strong> toʻgʻri — <em>the film</em> birlikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ a lot of people at the wedding.</strong></p>",
        "choices": ["were", "was", "did", "are"],
        "correct": "were",
        "explanation": "<p><strong>were</strong> is correct — <em>there was / there were</em> follows the "
                       "same rule as the present: look at the noun, and <em>people</em> is plural."
                       "<br><br><em>(<strong>were</strong> toʻgʻri — <em>there was / there were</em> "
                       "hozirgi zamondagi qoidaga boʻysunadi: otga qarang, <em>people</em> esa "
                       "koʻplikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ a small shop on this corner ten years ago.</strong></p>",
        "choices": ["was", "were", "is", "did"],
        "correct": "was",
        "explanation": "<p><strong>was</strong> is correct — <em>a small shop</em> is singular.<br><br>"
                       "<em>(<strong>was</strong> toʻgʻri — <em>a small shop</em> birlikda.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Were you at the lesson yesterday? — Yes, ___ .</strong></p>",
        "choices": ["I was", "I were", "I did", "I am"],
        "correct": "I was",
        "explanation": "<p><strong>I was</strong> is correct — the answer changes the subject to "
                       "<em>I</em>, so <em>were</em> becomes <em>was</em>.<br><br>"
                       "<em>(<strong>I was</strong> toʻgʻri — javobda subject <em>I</em> ga oʻzgaradi, "
                       "shuning uchun <em>were</em> <em>was</em> ga aylanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which time expression shows the sentence is in the past?</strong></p>",
        "choices": ["last night", "at the moment", "usually", "tomorrow"],
        "correct": "last night",
        "explanation": "<p><strong>last night</strong> is correct — the Past Simple almost always names a "
                       "finished time: <em>yesterday, last week, two years ago, in 2019</em>.<br><br>"
                       "<em>(<strong>last night</strong> toʻgʻri — Past Simple deyarli doim tugagan "
                       "vaqtni aytadi: <em>yesterday, last week, two years ago, in 2019</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>I ___ at home, but my brothers ___ in the yard.</strong></p>",
        "choices": ["was … were", "were … was", "was … was", "were … were"],
        "correct": "was … were",
        "explanation": "<p><strong>was … were</strong> is correct — <em>I</em> → <em>was</em>, plural "
                       "<em>brothers</em> → <em>were</em>.<br><br>"
                       "<em>(<strong>was … were</strong> toʻgʻri — <em>I</em> → <em>was</em>, koʻplikdagi "
                       "<em>brothers</em> → <em>were</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Where ___ you last Saturday?</strong></p>",
        "choices": ["were", "was", "did", "are"],
        "correct": "were",
        "explanation": "<p><strong>were</strong> is correct — <em>you</em> + past, and a wh- question "
                       "needs no <em>did</em> with <em>to be</em>.<br><br>"
                       "<em>(<strong>were</strong> toʻgʻri — <em>you</em> + oʻtgan zamon, wh- savolda "
                       "esa <em>to be</em> bilan <em>did</em> kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My grandfather ___ a teacher for thirty years.</strong></p>",
        "choices": ["was", "were", "is", "did"],
        "correct": "was",
        "explanation": "<p><strong>was</strong> is correct — one person, and the period is finished."
                       "<br><br><em>(<strong>was</strong> toʻgʻri — bitta shaxs, davr esa "
                       "tugagan.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I didn't at home yesterday.", "I wasn't at home yesterday.",
                    "I was at home yesterday.", "Was I wrong?"],
        "correct": "I didn't at home yesterday.",
        "explanation": "<p><strong>I didn't at home yesterday.</strong> is the mistake — <em>to be</em> "
                       "never uses <em>didn't</em>. Say <em>I wasn't at home</em>.<br><br>"
                       "<em>(<strong>I didn't at home yesterday.</strong> xato — <em>to be</em> hech "
                       "qachon <em>didn't</em> ishlatmaydi. <em>I wasn't at home</em> "
                       "deyiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["There were many cars in the street.", "There was many cars in the street.",
                    "There were a car in the street.", "There did be many cars in the street."],
        "correct": "There were many cars in the street.",
        "explanation": "<p><strong>There were many cars in the street.</strong> is correct — plural noun "
                       "→ <em>were</em>.<br><br>"
                       "<em>(<strong>There were many cars in the street.</strong> toʻgʻri — koʻplikdagi "
                       "ot → <em>were</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> How was your weekend?</p>"
                "<p><strong>B:</strong> ___</p>",
        "choices": ["It was great! We were in the mountains.",
                    "It were great! We was in the mountains.",
                    "It was great! We did in the mountains.",
                    "It is great! We were in the mountains."],
        "correct": "It was great! We were in the mountains.",
        "explanation": "<p><strong>It was great! We were in the mountains.</strong> is correct — "
                       "<em>it</em> → <em>was</em>, <em>we</em> → <em>were</em>.<br><br>"
                       "<em>(<strong>It was great! We were in the mountains.</strong> toʻgʻri — "
                       "<em>it</em> → <em>was</em>, <em>we</em> → <em>were</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> form is correct.</p>",
        "choices": ["Yesterday I was at my cousin's house. His parents were away, "
                    "and there was nobody at home.",
                    "Yesterday I were at my cousin's house. His parents was away, "
                    "and there were nobody at home.",
                    "Yesterday I was at my cousin's house. His parents was away, "
                    "and there were nobody at home.",
                    "Yesterday I didn't at my cousin's house. His parents weren't away, "
                    "and there wasn't nobody at home."],
        "correct": "Yesterday I was at my cousin's house. His parents were away, "
                   "and there was nobody at home.",
        "explanation": "<p><strong>I was … his parents were … there was nobody …</strong> is correct — "
                       "<em>I</em> and <em>nobody</em> are singular, <em>parents</em> is plural.<br><br>"
                       "<em>(<strong>I was … his parents were … there was nobody …</strong> toʻgʻri — "
                       "<em>I</em> va <em>nobody</em> birlikda, <em>parents</em> esa "
                       "koʻplikda.)</em></p>",
    },
]


# =====================================================================
# PE-20 — Past Simple: Regular Verbs and the -ed Ending
# =====================================================================

Q_PE20 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ her homework last night.</strong></p>",
        "choices": ["finished", "finish", "finishes", "finishing"],
        "correct": "finished",
        "explanation": "<p><strong>finished</strong> is correct — a finished action at a named past time "
                       "→ verb + <em>-ed</em>.<br><br>"
                       "<em>(<strong>finished</strong> toʻgʻri — aytilgan oʻtgan vaqtda tugagan harakat "
                       "→ feʼl + <em>-ed</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ football in the yard yesterday.</strong></p>",
        "choices": ["played", "play", "plays", "playd"],
        "correct": "played",
        "explanation": "<p><strong>played</strong> is correct. Vowel + <em>y</em> → just add "
                       "<em>-ed</em>: <em>played, stayed, enjoyed</em>.<br><br>"
                       "<em>(<strong>played</strong> toʻgʻri. Unli + <em>y</em> → shunchaki <em>-ed</em> "
                       "qoʻshiladi: <em>played, stayed, enjoyed</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which form is correct for <em>every</em> subject in the Past "
                "Simple?</strong></p>",
        "choices": ["worked", "workeds", "worksed", "was worked"],
        "correct": "worked",
        "explanation": "<p><strong>worked</strong> is correct — <em>I worked, he worked, they "
                       "worked</em>. No <em>-s</em> ever, for anybody.<br><br>"
                       "<em>(<strong>worked</strong> toʻgʻri — <em>I worked, he worked, they "
                       "worked</em>. Hech kim uchun <em>-s</em> qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct spelling.</p>"
                "<p><strong>study → ___</strong></p>",
        "choices": ["studied", "studyed", "studeed", "studyd"],
        "correct": "studied",
        "explanation": "<p><strong>studied</strong> is correct — consonant + <em>y</em> → "
                       "<em>-ied</em>.<br><br>"
                       "<em>(<strong>studied</strong> toʻgʻri — undosh + <em>y</em> → "
                       "<em>-ied</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct spelling.</p>"
                "<p><strong>stop → ___</strong></p>",
        "choices": ["stopped", "stoped", "stopeed", "stopd"],
        "correct": "stopped",
        "explanation": "<p><strong>stopped</strong> is correct — one short vowel + one consonant → double "
                       "the consonant: <em>stopped, planned, shopped</em>.<br><br>"
                       "<em>(<strong>stopped</strong> toʻgʻri — bitta qisqa unli + bitta undosh → undosh "
                       "ikkilanadi: <em>stopped, planned, shopped</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct spelling.</p>"
                "<p><strong>live → ___</strong></p>",
        "choices": ["lived", "liveed", "livd", "liveded"],
        "correct": "lived",
        "explanation": "<p><strong>lived</strong> is correct — a verb ending in <em>-e</em> just adds "
                       "<em>-d</em>.<br><br>"
                       "<em>(<strong>lived</strong> toʻgʻri — <em>-e</em> bilan tugagan feʼl faqat "
                       "<em>-d</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My father ___ in a factory in 2015.</strong></p>",
        "choices": ["worked", "works", "working", "was work"],
        "correct": "worked",
        "explanation": "<p><strong>worked</strong> is correct — <em>in 2015</em> is a finished past "
                       "time.<br><br>"
                       "<em>(<strong>worked</strong> toʻgʻri — <em>in 2015</em> tugagan oʻtgan "
                       "vaqt.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sherbek ___ me two hours ago.</strong></p>",
        "choices": ["called", "calls", "call", "calling"],
        "correct": "called",
        "explanation": "<p><strong>called</strong> is correct — <em>ago</em> always points to the past."
                       "<br><br><em>(<strong>called</strong> toʻgʻri — <em>ago</em> doim oʻtgan zamonga "
                       "ishora qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>They ___ in Andijan when they were children.</strong></p>",
        "choices": ["lived", "live", "lives", "living"],
        "correct": "lived",
        "explanation": "<p><strong>lived</strong> is correct — a finished period of the past.<br><br>"
                       "<em>(<strong>lived</strong> toʻgʻri — oʻtgan zamonning tugagan davri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which time expression goes with the Past Simple?</strong></p>",
        "choices": ["two days ago", "at the moment", "every day", "next week"],
        "correct": "two days ago",
        "explanation": "<p><strong>two days ago</strong> is correct — <em>ago, yesterday, last …, in "
                       "2019</em> all name a finished time.<br><br>"
                       "<em>(<strong>two days ago</strong> toʻgʻri — <em>ago, yesterday, last …, in "
                       "2019</em> — hammasi tugagan vaqtni bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How is the <em>-ed</em> in “wanted” pronounced?</strong></p>",
        "choices": ["as an extra syllable /ɪd/", "as /t/", "as /d/", "it is silent"],
        "correct": "as an extra syllable /ɪd/",
        "explanation": "<p><strong>as an extra syllable /ɪd/</strong> is correct. After <em>-t</em> or "
                       "<em>-d</em> the ending becomes a whole new syllable: <em>wanted, needed, "
                       "started</em>.<br><br>"
                       "<em>(<strong>/ɪd/ — qoʻshimcha boʻgʻin</strong> toʻgʻri. <em>-t</em> yoki "
                       "<em>-d</em> dan keyin qoʻshimcha alohida boʻgʻin boʻlib eshitiladi: "
                       "<em>wanted, needed, started</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In which word is <em>-ed</em> pronounced /t/?</strong></p>",
        "choices": ["watched", "played", "needed", "opened"],
        "correct": "watched",
        "explanation": "<p><strong>watched</strong> is correct. After a voiceless sound "
                       "(<em>k, p, s, ʃ, tʃ, f</em>) the ending sounds like <em>/t/</em>: "
                       "<em>watched, stopped, worked</em>.<br><br>"
                       "<em>(<strong>watched</strong> toʻgʻri. Jarangsiz tovushdan keyin "
                       "(<em>k, p, s, ʃ, tʃ, f</em>) qoʻshimcha <em>/t/</em> boʻlib eshitiladi: "
                       "<em>watched, stopped, worked</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ the door and ___ into the room.</strong></p>",
        "choices": ["opened … walked", "opened … walk", "open … walked", "opens … walks"],
        "correct": "opened … walked",
        "explanation": "<p><strong>opened … walked</strong> is correct — two past actions in a story, "
                       "both with <em>-ed</em>.<br><br>"
                       "<em>(<strong>opened … walked</strong> toʻgʻri — hikoyadagi ikki oʻtgan harakat, "
                       "ikkisi ham <em>-ed</em> bilan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct spelling.</p>"
                "<p><strong>plan → ___</strong></p>",
        "choices": ["planned", "planed", "planeed", "pland"],
        "correct": "planned",
        "explanation": "<p><strong>planned</strong> is correct — short vowel + single consonant → the "
                       "consonant doubles.<br><br>"
                       "<em>(<strong>planned</strong> toʻgʻri — qisqa unli + bitta undosh → undosh "
                       "ikkilanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct spelling.</p>"
                "<p><strong>carry → ___</strong></p>",
        "choices": ["carried", "carryed", "carrys", "carreed"],
        "correct": "carried",
        "explanation": "<p><strong>carried</strong> is correct — consonant + <em>y</em> → "
                       "<em>-ied</em>.<br><br>"
                       "<em>(<strong>carried</strong> toʻgʻri — undosh + <em>y</em> → "
                       "<em>-ied</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Last summer we ___ our grandparents in the village and ___ there for "
                "a month.</strong></p>",
        "choices": ["visited … stayed", "visit … stayed", "visited … stay", "visits … stays"],
        "correct": "visited … stayed",
        "explanation": "<p><strong>visited … stayed</strong> is correct — one past time expression "
                       "(<em>last summer</em>) covers both verbs.<br><br>"
                       "<em>(<strong>visited … stayed</strong> toʻgʻri — bitta oʻtgan vaqt ifodasi "
                       "(<em>last summer</em>) ikki feʼlga ham tegishli.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["He worked hard and she workeds hard too.",
                    "He worked hard and she worked hard too.",
                    "They worked hard yesterday.",
                    "I worked hard last week."],
        "correct": "He worked hard and she workeds hard too.",
        "explanation": "<p><strong>He worked hard and she workeds hard too.</strong> is the mistake — the "
                       "Past Simple never takes <em>-s</em>. That worry belongs to the present.<br><br>"
                       "<em>(<strong>He worked hard and she workeds hard too.</strong> xato — Past "
                       "Simple hech qachon <em>-s</em> olmaydi. Bu tashvish hozirgi zamonga "
                       "tegishli.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["She studied English for two hours yesterday.",
                    "She studyed English for two hours yesterday.",
                    "She studied English for two hours tomorrow.",
                    "She study English for two hours yesterday."],
        "correct": "She studied English for two hours yesterday.",
        "explanation": "<p><strong>She studied English for two hours yesterday.</strong> is correct — "
                       "<em>-ied</em> spelling, and a past time word.<br><br>"
                       "<em>(<strong>She studied English for two hours yesterday.</strong> toʻgʻri — "
                       "<em>-ied</em> imlosi va oʻtgan zamon vaqt soʻzi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> What did you do at the weekend?</p>"
                "<p><strong>B:</strong> ___</p>",
        "choices": ["I helped my father and watched a film.",
                    "I helped my father and watch a film.",
                    "I help my father and watched a film.",
                    "I was helped my father and was watched a film."],
        "correct": "I helped my father and watched a film.",
        "explanation": "<p><strong>I helped my father and watched a film.</strong> is correct — both "
                       "verbs are in the Past Simple, and <em>to be</em> has no place here.<br><br>"
                       "<em>(<strong>I helped my father and watched a film.</strong> toʻgʻri — ikki feʼl "
                       "ham Past Simple da, <em>to be</em> ga esa bu yerda oʻrin yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> spelling is correct.</p>",
        "choices": ["stopped, studied, played, lived",
                    "stoped, studyed, playd, liveed",
                    "stopped, studyed, played, lived",
                    "stoped, studied, playd, lived"],
        "correct": "stopped, studied, played, lived",
        "explanation": "<p><strong>stopped, studied, played, lived</strong> is correct — double "
                       "consonant, consonant + y → <em>-ied</em>, vowel + y → <em>-ed</em>, and "
                       "<em>-e</em> → <em>-d</em>. All four rules in one line.<br><br>"
                       "<em>(<strong>stopped, studied, played, lived</strong> toʻgʻri — undosh "
                       "ikkilanishi, undosh + y → <em>-ied</em>, unli + y → <em>-ed</em> va <em>-e</em> → "
                       "<em>-d</em>. Bitta qatorda toʻrtala qoida.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-16 Practice: Prepositions of Place: in, on, at",
        "tutorial":    "PE-16:",
        "description": "PE-16 darsiga 20 savol: at = nuqta, on = sirt, in = ichida mantiqi, qatʼiy "
                       "iboralar (at home, in bed, on the left) va in a car / on the bus farqi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE16,
    },
    {
        "title":       "PE-17 Practice: Prepositions of Time: in, on, at",
        "tutorial":    "PE-17:",
        "description": "PE-17 darsiga 20 savol: at 7 o'clock → on Monday → in May mantiqi, at night "
                       "istisnosi va predlog olmaydigan vaqt soʻzlari. Javoblar ingliz va oʻzbek "
                       "tilida izohlangan.",
        "questions":   Q_PE17,
    },
    {
        "title":       "PE-18 Practice: Question Words: who, what, where, when, why, how",
        "tutorial":    "PE-18:",
        "description": "PE-18 darsiga 20 savol: soʻroq soʻzlari, Wh- + yordamchi + subject + feʼl "
                       "tartibi, how old / how many / how far va oxirida qoladigan predlog. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE18,
    },
    {
        "title":       "PE-19 Practice: Past Simple of \"to be\": was / were",
        "tutorial":    "PE-19:",
        "description": "PE-19 darsiga 20 savol: was va were, wasn't / weren't, savollar, "
                       "There was / There were va oʻtgan zamon vaqt soʻzlari. Javoblar ingliz va "
                       "oʻzbek tilida izohlangan.",
        "questions":   Q_PE19,
    },
    {
        "title":       "PE-20 Practice: Past Simple: Regular Verbs and the -ed Ending",
        "tutorial":    "PE-20:",
        "description": "PE-20 darsiga 20 savol: -ed qoʻshimchasi, imlo qoidalari (stop → stopped, "
                       "study → studied) va -ed ning uch xil talaffuzi. Javoblar ingliz va oʻzbek "
                       "tilida izohlangan.",
        "questions":   Q_PE20,
    },
]
