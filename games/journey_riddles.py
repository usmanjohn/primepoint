"""
The wayfarer's riddles — Prime Journey's own question bank.

The lesson practices make the road *teach*, but they cannot make it feel like a
road. A bridge keeper who demands "1,2 × 5 = ?" is absurd: the encounter promises
a riddle and hands over a worksheet. That is a problem of **genre**, not of
difficulty — a harder drill question is still a drill question.

So the guardians and the wise strangers ask from here instead: puzzles of the
kind that have been asked at bridges and crossroads for a thousand years. A
group collects $529 and each person gave as many dollars as there are people —
how many people? You cannot grind at that one. You either see that 529 is a
square, or you do not, and seeing it is the whole pleasure.

Three rules this bank keeps:

* **Nothing is hand-written twice.** Every riddle is a *generator*, the same
  trick as `mathchamp.py`, so the bank never runs dry and a pupil who meets the
  socks-in-the-dark puzzle twice meets different numbers.
* **The insight goes in the explanation, not the arithmetic.** A pupil who got it
  wrong should close the card knowing the trick, not the sum.
* **No riddle needs the lesson.** They are deliberately free of the course, so
  the same bank serves the maths road and the Korean one alike. Only the
  language changes: English on the Prime English road, Uzbek everywhere else.

Every answer in here is computed twice — once by the generator, once by
`check_riddles`, which is this bank's arithmetic gate. Run it after any edit.
"""
import math
import random


def _t(lang, uz, en):
    return en if lang == 'en' else uz


def _q(family, lang, topic, text, correct, wrongs, explanation, fmt=str):
    """Build the riddle dict: four options, one of them right.

    Shaped so a riddle is interchangeable with a practice question in the view —
    `choices` carry ids, exactly as `journey.pick_question` returns them.
    """
    seen, options = {correct}, [correct]
    for w in wrongs:
        if w not in seen:
            seen.add(w)
            options.append(w)
    n = 1
    while len(options) < 4:                      # never show fewer than four
        for cand in (correct + n, correct - n):
            if cand not in seen and cand > 0 and len(options) < 4:
                seen.add(cand)
                options.append(cand)
        n += 1

    options = options[:4]
    random.shuffle(options)
    return {
        'family':      family,
        'riddle':      True,
        'topic':       topic,
        'text':        text,
        'hint':        '',
        'choices':     [{'id': i, 'text': fmt(v)} for i, v in enumerate(options)],
        'correct':     options.index(correct),
        'explanation': explanation,
        'answer_value': correct,
    }


# ---------------------------------------------------------------------------
# The riddles
# ---------------------------------------------------------------------------
# Each takes (rng, lang) and returns a question. Keep the arithmetic exact and
# the numbers small enough to hold in the head — a riddle a pupil must reach for
# a calculator to finish is a drill question wearing a hat.


def r_square_collect(rng, lang):
    """n people, each gives n — the total is a square."""
    n = rng.randint(12, 40)
    total = n * n
    return _q('square_collect', lang,
              _t(lang, 'Sonlar siri', 'A trick of numbers'),
              _t(lang,
                 f"Bir guruh odam {total} dollar yig'di. Har bir odam guruhdagi "
                 f"odamlar soniga teng miqdorda dollar bergan. Guruhda necha kishi bor?",
                 f"A group of people collected ${total}. Each person gave as many "
                 f"dollars as there are people in the group. How many people are there?"),
              n, [n + 1, n - 1, total // 10, n * 2],
              _t(lang,
                 f"Har biri n dollardan bergan va ular n kishi — demak jami n × n. "
                 f"Ya'ni n² = {total}. Kvadrat ildiz: n = {n}. Tekshirish: "
                 f"{n} × {n} = {total}. Hiyla shunda: «har biri odamlar soniga teng» "
                 f"degani — bu ko'paytirish emas, bu kvadrat.",
                 f"Each of the n people gave n dollars, so the total is n × n. "
                 f"That is n² = {total}, so n = {n}. Check: {n} × {n} = {total}. "
                 f"The trick is the phrase 'as many as there are people' — it does "
                 f"not mean multiply by something, it means square."))


def r_handshakes(rng, lang):
    """Everyone greets everyone once."""
    n = rng.randint(6, 16)
    shakes = n * (n - 1) // 2
    return _q('handshakes', lang,
              _t(lang, 'Uchrashuv', 'The meeting'),
              _t(lang,
                 f"Xonaga kirgan har bir odam boshqa har bir odam bilan bir martadan "
                 f"qo'l berib ko'rishdi. Jami {shakes} marta qo'l berishildi. "
                 f"Xonada necha kishi bor edi?",
                 f"Everyone in a room shook hands with everyone else exactly once. "
                 f"There were {shakes} handshakes in all. How many people were there?"),
              n, [n + 1, n - 1, shakes // 2, n + 2],
              _t(lang,
                 f"Har bir odam qolgan (n − 1) kishi bilan ko'rishadi — bu n × (n − 1). "
                 f"Lekin har bir ko'rishish ikki marta sanaldi (men senga, sen menga), "
                 f"shuning uchun 2 ga bo'lamiz: n(n − 1)/2 = {shakes}. "
                 f"n = {n}: {n} × {n - 1} ÷ 2 = {shakes}. "
                 f"Eng ko'p uchraydigan xato — 2 ga bo'lishni unutish.",
                 f"Each person shakes hands with the other (n − 1), which is n × (n − 1). "
                 f"But that counts every handshake twice — once from each side — so "
                 f"divide by 2: n(n − 1)/2 = {shakes}. With n = {n}: "
                 f"{n} × {n - 1} ÷ 2 = {shakes}. Forgetting to halve is the usual slip."))


def r_ages(rng, lang):
    """Father and son. Chosen so the answer is always whole."""
    son = rng.randint(6, 15)
    k = rng.choice((3, 4, 5))
    father = k * son
    years = son * (k - 2)            # makes father + years == 2 × (son + years)
    return _q('ages', lang,
              _t(lang, 'Yosh jumbog\'i', 'A question of age'),
              _t(lang,
                 f"Ota o'g'lidan {k} marta katta. {years} yildan keyin ota o'g'lidan "
                 f"atigi 2 marta katta bo'ladi. O'g'il hozir necha yoshda?",
                 f"A father is {k} times as old as his son. In {years} years he will be "
                 f"only twice as old. How old is the son now?"),
              son, [son + 1, son - 1, father, son + years],
              _t(lang,
                 f"O'g'il x yoshda bo'lsin, ota {k}x. {years} yildan keyin: "
                 f"{k}x + {years} = 2(x + {years}). Ochamiz: {k}x + {years} = 2x + {2 * years}, "
                 f"demak {k - 2}x = {years}, x = {son}. Ota hozir {father} yoshda; "
                 f"{years} yildan keyin {father + years} va {son + years} — rostdan ham 2 marta. "
                 f"Diqqat: yillar ikkalasiga ham qo'shiladi, faqat otaga emas.",
                 f"Let the son be x, so the father is {k}x. In {years} years: "
                 f"{k}x + {years} = 2(x + {years}), which gives {k - 2}x = {years}, so x = {son}. "
                 f"The father is {father} now; in {years} years they are {father + years} "
                 f"and {son + years} — exactly double. The catch: the years are added to "
                 f"*both* of them, not only to the father."))


def r_socks(rng, lang):
    """Pigeonhole, in a dark room."""
    colours = rng.randint(2, 5)
    each = rng.choice((8, 10, 12, 20))
    names_uz = ['qora', 'oq', 'ko\'k', 'qizil', 'yashil']
    names_en = ['black', 'white', 'blue', 'red', 'green']
    listing = ', '.join(f"{each} {n}" for n in
                        (names_uz if lang != 'en' else names_en)[:colours])
    answer = colours + 1
    return _q('socks', lang,
              _t(lang, 'Qorong\'ida', 'In the dark'),
              _t(lang,
                 f"Qorong'i xonadagi tortmada paypoqlar bor: {listing}. Chiroq yo'q, "
                 f"rangini ko'rib bo'lmaydi. Bir xil rangdagi juftlik chiqishi ANIQ "
                 f"bo'lishi uchun kamida nechta paypoq olish kerak?",
                 f"A drawer in a dark room holds socks: {listing}. There is no light and "
                 f"you cannot see the colours. What is the smallest number you must take "
                 f"out to be CERTAIN of a matching pair?"),
              answer, [colours, each, answer + 1, colours * 2],
              _t(lang,
                 f"«Aniq» so'zi omadni taqiqlaydi — eng yomon holatni o'ylash kerak. "
                 f"Eng yomoni: birinchi {colours} ta paypoqning hammasi turli rangda chiqadi. "
                 f"Ana shunda keyingi — {answer}-paypoq — qaysi rang bo'lsa ham, "
                 f"albatta allaqachon bor rangga to'g'ri keladi. Javob: {answer}. "
                 f"Paypoqlar soni ({each}) bu yerda umuman ahamiyatsiz.",
                 f"The word 'certain' rules luck out — you must plan for the worst case. "
                 f"The worst is that your first {colours} socks all come out different "
                 f"colours. Then sock number {answer}, whatever colour it is, must match "
                 f"one you already hold. The answer is {answer}. How many socks of each "
                 f"colour there are ({each}) makes no difference at all."))


def r_heads_legs(rng, lang):
    """Chickens and rabbits in one pen."""
    chickens = rng.randint(4, 20)
    rabbits = rng.randint(3, 18)
    heads = chickens + rabbits
    legs = 2 * chickens + 4 * rabbits
    return _q('heads_legs', lang,
              _t(lang, 'Hovlidagi hisob', 'A count in the yard'),
              _t(lang,
                 f"Hovlida tovuq va quyonlar bor. Jami {heads} ta bosh va {legs} ta oyoq "
                 f"sanaldi. Hovlida nechta quyon bor?",
                 f"A yard holds chickens and rabbits. There are {heads} heads and "
                 f"{legs} legs in all. How many rabbits are there?"),
              rabbits, [chickens, rabbits + 1, rabbits - 1, heads - rabbits],
              _t(lang,
                 f"Ayyor yo'l: hammasi tovuq deb faraz qilaylik. Unda oyoq soni "
                 f"2 × {heads} = {2 * heads} bo'lardi. Aslida {legs} ta — "
                 f"{legs - 2 * heads} ta ortiqcha. Har bir quyon tovuqdan 2 ta ortiq oyoq "
                 f"qo'shadi, demak quyonlar: {legs - 2 * heads} ÷ 2 = {rabbits} ta. "
                 f"Tovuqlar esa {chickens} ta. Tekshirish: "
                 f"{2 * chickens} + {4 * rabbits} = {legs}.",
                 f"The sly way: pretend they are all chickens. Then there would be "
                 f"2 × {heads} = {2 * heads} legs. There are {legs} — that is "
                 f"{legs - 2 * heads} too many. Every rabbit adds 2 legs over a chicken, "
                 f"so there are {legs - 2 * heads} ÷ 2 = {rabbits} rabbits, and "
                 f"{chickens} chickens. Check: {2 * chickens} + {4 * rabbits} = {legs}."))


def r_calendar(rng, lang):
    """Counting days round a seven-day wheel."""
    days_uz = ['dushanba', 'seshanba', 'chorshanba', 'payshanba',
               'juma', 'shanba', 'yakshanba']
    days_en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
               'Friday', 'Saturday', 'Sunday']
    days = days_en if lang == 'en' else days_uz
    start = rng.randint(0, 6)
    ahead = rng.choice((45, 60, 75, 100, 123, 150, 200, 365))
    end = (start + ahead) % 7
    return _q('calendar', lang,
              _t(lang, 'Kunlar g\'ildiragi', 'The wheel of days'),
              _t(lang,
                 f"Bugun — {days[start]}. Bugundan {ahead} kun keyin hafta"
                 f"ning qaysi kuni bo'ladi?",
                 f"Today is {days[start]}. What day of the week will it be "
                 f"{ahead} days from today?"),
              end, [(end + 1) % 7, (end - 1) % 7, (end + 3) % 7, (end + 2) % 7],
              _t(lang,
                 f"Hafta 7 kunda takrorlanadi, shuning uchun faqat 7 ga bo'lgandagi "
                 f"QOLDIQ muhim. {ahead} ÷ 7 = {ahead // 7} ta to'liq hafta va "
                 f"{ahead % 7} kun qoldiq. To'liq haftalar kunni o'zgartirmaydi — "
                 f"{days[start]} dan {ahead % 7} kun oldinga sanaymiz: {days[end]}.",
                 f"The week repeats every 7 days, so only the REMAINDER matters. "
                 f"{ahead} ÷ 7 = {ahead // 7} whole weeks and {ahead % 7} left over. "
                 f"Whole weeks change nothing, so count {ahead % 7} days on from "
                 f"{days[start]}: {days[end]}."),
              fmt=lambda v: days[v % 7])


def r_stairs(rng, lang):
    """Floors are not the same thing as flights."""
    per = rng.randint(2, 6)
    from_floor = rng.choice((3, 4, 5, 6))
    to_floor = rng.choice((7, 9, 10, 11, 13))
    if to_floor <= from_floor:
        to_floor = from_floor + 5
    time_known = (from_floor - 1) * per
    answer = (to_floor - 1) * per
    return _q('stairs', lang,
              _t(lang, 'Zinapoya', 'The staircase'),
              _t(lang,
                 f"Bir bolaning 1-qavatdan {from_floor}-qavatgacha ko'tarilishiga "
                 f"{time_known} daqiqa ketadi. Xuddi shu tezlikda 1-qavatdan "
                 f"{to_floor}-qavatgacha necha daqiqada ko'tariladi?",
                 f"It takes a boy {time_known} minutes to climb from floor 1 to "
                 f"floor {from_floor}. At the same speed, how many minutes to climb "
                 f"from floor 1 to floor {to_floor}?"),
              answer, [to_floor * per, answer + per, answer - per,
                       time_known * to_floor // from_floor],
              _t(lang,
                 f"Tuzoq shu yerda: u {from_floor} ta qavatga emas, "
                 f"{from_floor - 1} ta ORALIQQA ko'tariladi. Demak bitta oraliq "
                 f"{time_known} ÷ {from_floor - 1} = {per} daqiqa. "
                 f"{to_floor}-qavatgacha {to_floor - 1} ta oraliq bor: "
                 f"{to_floor - 1} × {per} = {answer} daqiqa. "
                 f"Qavatlarni emas, oraliqlarni sanang.",
                 f"Here is the trap: he does not climb {from_floor} floors, he climbs "
                 f"{from_floor - 1} FLIGHTS between them. So one flight takes "
                 f"{time_known} ÷ {from_floor - 1} = {per} minutes. Reaching floor "
                 f"{to_floor} means {to_floor - 1} flights: {to_floor - 1} × {per} = "
                 f"{answer} minutes. Count the gaps, not the floors."))


def r_snail(rng, lang):
    """Up by day, down by night — and the last day it does not slip."""
    climb = rng.randint(3, 7)
    slip = rng.randint(1, climb - 1)
    days = rng.randint(4, 12)
    height = (days - 1) * (climb - slip) + climb
    return _q('snail', lang,
              _t(lang, 'Quduqdagi shilliqqurt', 'The snail in the well'),
              _t(lang,
                 f"Chuqurligi {height} metr quduqning tubida shilliqqurt bor. "
                 f"Kunduzi u {climb} metr ko'tariladi, kechasi esa {slip} metr pastga "
                 f"sirg'aladi. U necha kunda quduqdan chiqadi?",
                 f"A snail is at the bottom of a well {height} metres deep. Each day it "
                 f"climbs {climb} metres, and each night it slips back {slip} metres. "
                 f"On which day does it get out?"),
              days, [days + 1, days - 1, height // (climb - slip), days + 2],
              _t(lang,
                 f"Har bir to'liq kecha-kunduzda u {climb} − {slip} = {climb - slip} metr "
                 f"yutadi. Lekin OXIRGI kuni u chiqib ketadi va kechasi sirg'almaydi — "
                 f"mana shu butun jumboqning kaliti. Oxirgi kuni {climb} metrni bosib o'tadi, "
                 f"demak undan oldin {height} − {climb} = {height - climb} metrga "
                 f"chiqib olishi kerak: {height - climb} ÷ {climb - slip} = {days - 1} kun. "
                 f"Ustiga oxirgi kun: jami {days} kun.",
                 f"Over a full day and night it gains {climb} − {slip} = {climb - slip} "
                 f"metres. But on the LAST day it climbs out and never slips back — that "
                 f"is the whole puzzle. The last day covers {climb} metres, so before it "
                 f"must have reached {height} − {climb} = {height - climb} metres, which "
                 f"takes {height - climb} ÷ {climb - slip} = {days - 1} days. Add the last "
                 f"one: {days} days."))


def r_log_cuts(rng, lang):
    """Cuts and pieces differ by one."""
    per = rng.randint(2, 8)
    pieces = rng.randint(5, 12)
    answer = (pieces - 1) * per
    return _q('log_cuts', lang,
              _t(lang, 'Arra', 'The saw'),
              _t(lang,
                 f"Yog'ochni bir marta arralashga {per} daqiqa ketadi. Bitta uzun "
                 f"yog'ochni {pieces} ta bo'lakka bo'lish uchun necha daqiqa kerak?",
                 f"One cut through a log takes {per} minutes. How many minutes does it "
                 f"take to cut a single long log into {pieces} pieces?"),
              answer, [pieces * per, answer + per, answer - per, per * (pieces + 1)],
              _t(lang,
                 f"{pieces} ta bo'lak olish uchun {pieces} marta emas, "
                 f"{pieces - 1} marta arralash kerak — birinchi arralash 2 ta bo'lak beradi, "
                 f"har bir keyingisi yana bittadan qo'shadi. "
                 f"{pieces - 1} × {per} = {answer} daqiqa. "
                 f"Bir chekkasini arralashning hojati yo'q!",
                 f"Getting {pieces} pieces needs {pieces - 1} cuts, not {pieces} — the "
                 f"first cut makes 2 pieces and each cut after that adds one more. "
                 f"So {pieces - 1} × {per} = {answer} minutes. There is no need to saw "
                 f"the far end off!"))


def r_boxes(rng, lang):
    """Three boxes, every label wrong."""
    pairs_uz = [('olma', 'nok'), ('yong\'oq', 'shakar'), ('tuz', 'un'), ('mix', 'vint')]
    pairs_en = [('apples', 'pears'), ('nuts', 'sugar'), ('salt', 'flour'), ('nails', 'screws')]
    a, b = rng.choice(pairs_en if lang == 'en' else pairs_uz)
    return _q('boxes', lang,
              _t(lang, 'Uch quti', 'Three boxes'),
              _t(lang,
                 f"Uchta yopiq quti bor. Birinchisida «{a}», ikkinchisida «{b}», "
                 f"uchinchisida «{a} va {b} aralash» deb yozilgan. MA'LUMKI, "
                 f"uchala yozuv ham NOTO'G'RI. Qutilarda nima borligini aniq bilish uchun "
                 f"kamida nechta quti ochib, bittadan narsa olib ko'rish kerak?",
                 f"Three closed boxes are labelled '{a}', '{b}', and '{a} and {b} mixed'. "
                 f"You are told that ALL THREE labels are wrong. What is the smallest "
                 f"number of boxes you must open — taking out just one item from each — "
                 f"to know for certain what is in every box?"),
              1, [2, 3, 4],
              _t(lang,
                 f"Bitta yetadi — lekin faqat TO'G'RI qutidan olsangiz. "
                 f"«Aralash» yozuvli qutini oching: yozuv noto'g'ri, demak u aralash EMAS, "
                 f"ya'ni faqat bitta narsa bor. Bittasini olsangiz — masalan {a} chiqdi — "
                 f"demak bu quti to'liq {a}. Endi «{a}» yozuvli quti {a} ham bo'la olmaydi "
                 f"(yozuvi noto'g'ri), aralash ham bo'la olmaydi (aralashni topdik) — "
                 f"demak u {b}. Oxirgisi esa aralash. Hammasi bitta olishdan kelib chiqdi.",
                 f"One is enough — but only if you open the RIGHT box. Open the one "
                 f"labelled 'mixed'. Its label is wrong, so it is NOT mixed: it holds only "
                 f"one thing. Take out one item — say it is {a} — so that box is all {a}. "
                 f"Now the box labelled '{a}' cannot be {a} (its label is wrong) and cannot "
                 f"be mixed (we just found the pure one), so it must be {b}. The last one "
                 f"is the mixture. All of it follows from a single item."))


def r_digit_reverse(rng, lang):
    """Two digits that change places."""
    tens = rng.randint(1, 5)
    units = tens + rng.randint(1, min(4, 9 - tens))
    num = 10 * tens + units
    rev = 10 * units + tens
    total = tens + units
    diff = rev - num
    return _q('digit_reverse', lang,
              _t(lang, 'Raqamlar o\'rin almashdi', 'The digits change places'),
              _t(lang,
                 f"Ikki xonali sonning raqamlari yig'indisi {total} ga teng. Agar "
                 f"raqamlarning o'rni almashtirilsa, son {diff} ga ortadi. Bu qaysi son?",
                 f"The digits of a two-digit number add up to {total}. If the digits swap "
                 f"places, the number grows by {diff}. What is the number?"),
              num, [rev, num + 9, num - 9, total * 10],
              _t(lang,
                 f"Son 10a + b bo'lsin. O'rni almashsa 10b + a bo'ladi, farq esa "
                 f"(10b + a) − (10a + b) = 9(b − a). Demak 9(b − a) = {diff}, "
                 f"ya'ni b − a = {diff // 9}. Yana a + b = {total}. Ikkitasidan: "
                 f"a = {tens}, b = {units} — son {num}. Tekshirish: {rev} − {num} = {diff}. "
                 f"Sirli joyi: farq HAR DOIM 9 ga bo'linadi.",
                 f"Let the number be 10a + b. Swapped it is 10b + a, and the difference is "
                 f"(10b + a) − (10a + b) = 9(b − a). So 9(b − a) = {diff}, giving "
                 f"b − a = {diff // 9}. With a + b = {total} we get a = {tens}, b = {units}, "
                 f"so the number is {num}. Check: {rev} − {num} = {diff}. The hidden fact: "
                 f"that difference is ALWAYS a multiple of 9."))


def r_triangular(rng, lang):
    """1 + 2 + … + n, the way Gauss did it."""
    n = rng.choice((20, 30, 40, 50, 60, 80, 100))
    total = n * (n + 1) // 2
    return _q('triangular', lang,
              _t(lang, 'Gauss usuli', "Gauss's trick"),
              _t(lang,
                 f"1 dan {n} gacha bo'lgan barcha butun sonlarni qo'shing. "
                 f"Yig'indi nechaga teng?",
                 f"Add up every whole number from 1 to {n}. What is the total?"),
              total, [total + n, total - n, n * n, n * (n + 1)],
              _t(lang,
                 f"Gauss bolaligida topgan usul: sonlarni chetlaridan juftlab chiqing. "
                 f"1 + {n} = {n + 1}, 2 + {n - 1} = {n + 1}, va hokazo — har bir juft "
                 f"{n + 1} ga teng, juftlar soni esa {n} ÷ 2 = {n // 2}. "
                 f"Demak {n // 2} × {n + 1} = {total}. Formula: n(n + 1)/2.",
                 f"The trick Gauss found as a schoolboy: pair the numbers from the two "
                 f"ends. 1 + {n} = {n + 1}, 2 + {n - 1} = {n + 1}, and so on — every pair "
                 f"makes {n + 1}, and there are {n} ÷ 2 = {n // 2} pairs. So "
                 f"{n // 2} × {n + 1} = {total}. The formula is n(n + 1)/2."))


def r_shared_work(rng, lang):
    """Two workers, one job. Chosen so the answer is whole."""
    a, b = rng.choice(((3, 6), (4, 12), (6, 12), (10, 15), (12, 24),
                       (20, 30), (6, 3), (15, 10)))
    together = a * b // (a + b)
    return _q('shared_work', lang,
              _t(lang, 'Birgalikda ish', 'Working together'),
              _t(lang,
                 f"Bir usta devorni {a} soatda bo'yaydi, ikkinchisi esa xuddi shu devorni "
                 f"{b} soatda bo'yaydi. Ikkalasi birga ishlasa, devor necha soatda bo'yaladi?",
                 f"One painter paints a wall in {a} hours; another paints the same wall in "
                 f"{b} hours. Working together, how many hours does the wall take?"),
              together, [(a + b) // 2, a + b, together + 1, abs(b - a)],
              _t(lang,
                 f"Soatlarni qo'shib bo'lmaydi — TEZLIKlarni qo'shish kerak. "
                 f"Birinchi usta bir soatda devorning 1/{a} qismini, ikkinchisi 1/{b} "
                 f"qismini bo'yaydi. Birgalikda bir soatda 1/{a} + 1/{b} = "
                 f"{a + b}/{a * b} qismini bo'yashadi. To'liq devor uchun teskarisi: "
                 f"{a * b}/{a + b} = {together} soat. Diqqat: javob ikkala sondan ham "
                 f"KICHIK bo'lishi shart — birga ishlash tezroq.",
                 f"You cannot add the hours — you add the RATES. The first painter does "
                 f"1/{a} of the wall in an hour, the second 1/{b}. Together that is "
                 f"1/{a} + 1/{b} = {a + b}/{a * b} of the wall per hour, so the whole wall "
                 f"takes {a * b}/{a + b} = {together} hours. Sanity check: the answer must "
                 f"be SMALLER than either time on its own — two people are faster."))


def r_balance(rng, lang):
    """Swapping one thing for another."""
    x = rng.choice((2, 3, 4))
    y = rng.choice((2, 3))
    apples = x * y * rng.randint(1, 2)
    pears = apples // x * 2          # x apples = 2 pears
    plums = pears * y                # 1 pear = y plums
    return _q('balance', lang,
              _t(lang, 'Tarozi', 'The balance'),
              _t(lang,
                 f"Tarozida {x} ta olma {2} ta nokka teng keladi, "
                 f"1 ta nok esa {y} ta olxo'riga teng. "
                 f"{apples} ta olma nechta olxo'riga teng keladi?",
                 f"On a balance, {x} apples weigh the same as {2} pears, and 1 pear "
                 f"weighs the same as {y} plums. How many plums balance {apples} apples?"),
              plums, [plums + y, plums - y, apples * y, plums * 2],
              _t(lang,
                 f"Bosqichma-bosqich almashtiring. {apples} ta olma = "
                 f"{apples} ÷ {x} = {apples // x} ta guruh, har biri {2} nok — "
                 f"demak {pears} ta nok. Har bir nok {y} ta olxo'ri, "
                 f"demak {pears} × {y} = {plums} ta olxo'ri. "
                 f"Bunday jumboqlarda har doim bitta «valyuta»ga o'ting.",
                 f"Convert one step at a time. {apples} apples make "
                 f"{apples} ÷ {x} = {apples // x} groups of {2} pears, so {pears} pears. "
                 f"Each pear is {y} plums, so {pears} × {y} = {plums} plums. "
                 f"With puzzles like this, always convert everything into one 'currency'."))


def r_fake_coin(rng, lang):
    """How few weighings can be enough."""
    n = rng.choice((9, 12, 27, 8, 18))
    answer = math.ceil(math.log(n, 3) - 1e-9)
    return _q('fake_coin', lang,
              _t(lang, 'Soxta tanga', 'The false coin'),
              _t(lang,
                 f"{n} ta bir xil ko'rinishdagi tanga bor, ulardan bittasi qolganlaridan "
                 f"YENGIL. Sizda pallali tarozi bor (tosh yo'q, faqat qaysi tomon "
                 f"og'irroq ekanini ko'rsatadi). Soxta tangani ANIQ topish uchun kamida "
                 f"necha marta tortish kerak?",
                 f"You have {n} identical-looking coins, one of which is LIGHTER than the "
                 f"rest. You have a balance scale with two pans (no weights — it only "
                 f"shows which side is heavier). What is the smallest number of weighings "
                 f"that is certain to find the false coin?"),
              answer, [answer + 1, answer - 1, n // 2, answer + 2],
              _t(lang,
                 f"Har bir tortish UCHTA javob beradi: chap og'ir, o'ng og'ir, yoki teng. "
                 f"Shuning uchun tangalarni ikkiga emas, UCHGA bo'lish kerak. "
                 f"Bir marta tortish 3 tagacha, ikki marta 9 tagacha, uch marta 27 tagacha "
                 f"tangani ajratadi. {n} ta uchun {answer} marta yetarli "
                 f"(3^{answer} = {3 ** answer} ≥ {n}), {answer - 1} marta esa kamlik qiladi "
                 f"(3^{answer - 1} = {3 ** (answer - 1)} < {n}).",
                 f"Each weighing has THREE outcomes: left heavier, right heavier, or "
                 f"balanced. So you split the coins into three groups, not two. One "
                 f"weighing settles up to 3 coins, two settles 9, three settles 27. For "
                 f"{n} coins, {answer} weighings are enough (3^{answer} = {3 ** answer} ≥ "
                 f"{n}) and {answer - 1} cannot be (3^{answer - 1} = {3 ** (answer - 1)} "
                 f"< {n})."))


def r_sequence(rng, lang):
    """A pattern with something hidden in it."""
    kind = rng.choice(('squares_plus', 'triangular', 'double_plus', 'gaps'))
    if kind == 'squares_plus':
        seq = [n * n + n for n in range(1, 6)]
        nxt = 6 * 6 + 6
        why = _t(lang,
                 "Har bir had n² + n: 1+1, 4+2, 9+3, 16+4, 25+5. "
                 "Oltinchisi: 36 + 6 = 42. Boshqacha ko'rish ham mumkin — "
                 "farqlar 4, 6, 8, 10 … ya'ni har safar 2 ga ortadi.",
                 "Each term is n² + n: 1+1, 4+2, 9+3, 16+4, 25+5. The sixth is "
                 "36 + 6 = 42. Another way to see it: the gaps are 4, 6, 8, 10 … "
                 "growing by 2 each time.")
    elif kind == 'triangular':
        seq = [n * (n + 1) // 2 for n in range(1, 6)]
        nxt = 6 * 7 // 2
        why = _t(lang,
                 "Bular uchburchak sonlar: 1, 1+2, 1+2+3, … Har safar keyingi butun son "
                 "qo'shiladi. Oltinchisi: 15 + 6 = 21.",
                 "These are the triangular numbers: 1, 1+2, 1+2+3, … each time you add "
                 "the next whole number. The sixth is 15 + 6 = 21.")
    elif kind == 'double_plus':
        start = rng.randint(1, 4)
        seq, v = [], start
        for _ in range(5):
            seq.append(v)
            v = v * 2 + 1
        nxt = v
        why = _t(lang,
                 f"Qoida: har bir hadni 2 ga ko'paytirib, 1 qo'shing. "
                 f"{seq[-1]} × 2 + 1 = {nxt}. Faqat ko'paytirishga qarasangiz, "
                 f"naqsh to'g'ri kelmaydi — qo'shimcha 1 ni sezish kerak.",
                 f"The rule is: double, then add 1. {seq[-1]} × 2 + 1 = {nxt}. "
                 f"If you only look for a multiplier the pattern will not fit — "
                 f"the extra 1 is the thing to spot.")
    else:
        start = rng.randint(2, 6)
        step = rng.randint(2, 4)
        seq, v, g = [], start, step
        for _ in range(5):
            seq.append(v)
            v += g
            g += step
        nxt = v
        why = _t(lang,
                 f"Hadlar orasidagi farqlar o'zi ketma-ketlik hosil qiladi: "
                 f"{step}, {2 * step}, {3 * step}, {4 * step} … Keyingi farq {5 * step}, "
                 f"demak {seq[-1]} + {5 * step} = {nxt}. Naqshni topolmasangiz — "
                 f"FARQLARGA qarang.",
                 f"The gaps between the terms form their own pattern: "
                 f"{step}, {2 * step}, {3 * step}, {4 * step} … The next gap is {5 * step}, "
                 f"so {seq[-1]} + {5 * step} = {nxt}. When a pattern will not show itself, "
                 f"look at the GAPS.")
    shown = ', '.join(str(v) for v in seq)
    return _q('sequence', lang,
              _t(lang, 'Naqsh', 'The pattern'),
              _t(lang,
                 f"Ketma-ketlikni davom ettiring: {shown}, ?",
                 f"Continue the sequence: {shown}, ?"),
              nxt, [nxt + 1, nxt - 1, seq[-1] * 2, nxt + seq[-1] - seq[-2]], why)


def r_clock(rng, lang):
    """The angle between the hands."""
    hour = rng.randint(1, 11)
    half = rng.random() < 0.5
    if half:
        angle = abs((30 * hour + 15) - 180)
        when = f"{hour}:30"
        why_uz = (f"Soat mili bir soatda 30° yuradi, {hour}:30 da u {hour} va {hour + 1} "
                  f"orasida — ya'ni {30 * hour} + 15 = {30 * hour + 15}°. "
                  f"Daqiqa mili 30 daqiqada aynan pastga, 180° ga boradi. "
                  f"Farq: |{30 * hour + 15} − 180| = {angle}°.")
        why_en = (f"The hour hand moves 30° an hour, and at {hour}:30 it sits halfway "
                  f"between {hour} and {hour + 1} — that is {30 * hour} + 15 = "
                  f"{30 * hour + 15}°. The minute hand at 30 minutes points straight down, "
                  f"at 180°. The difference is |{30 * hour + 15} − 180| = {angle}°.")
    else:
        angle = min(30 * hour, 360 - 30 * hour)
        when = f"{hour}:00"
        why_uz = (f"Butun aylana 360°, siferblatda 12 ta bo'linma — demak har bir soat "
                  f"360 ÷ 12 = 30°. Soat {when} da millar orasida {hour} ta bo'linma bor: "
                  f"{hour} × 30 = {30 * hour}°. Burchak sifatida kichigini olamiz: {angle}°.")
        why_en = (f"A full circle is 360° and the dial has 12 divisions, so each hour is "
                  f"360 ÷ 12 = 30°. At {when} the hands are {hour} divisions apart: "
                  f"{hour} × 30 = {30 * hour}°. We take the smaller of the two angles: "
                  f"{angle}°.")
    return _q('clock', lang,
              _t(lang, 'Soat millari', 'The hands of the clock'),
              _t(lang,
                 f"Soat {when} bo'lganda, soat mili bilan daqiqa mili orasidagi kichik "
                 f"burchak necha gradusga teng?",
                 f"At {when}, what is the smaller angle between the hour hand and the "
                 f"minute hand?"),
              angle, [angle + 15, abs(angle - 15), 360 - angle if angle else 30,
                      angle + 30],
              _t(lang, why_uz, why_en),
              fmt=lambda v: f"{v}°")


# ---------------------------------------------------------------------------
# The bank
# ---------------------------------------------------------------------------

RIDDLES = [
    r_square_collect, r_handshakes, r_ages, r_socks, r_heads_legs, r_calendar,
    r_stairs, r_snail, r_log_cuts, r_boxes, r_digit_reverse, r_triangular,
    r_shared_work, r_balance, r_fake_coin, r_sequence, r_clock,
]

FAMILIES = [f.__name__.replace('r_', '') for f in RIDDLES]


def language_for(road_slug):
    """Riddles speak the language the road's course is taught in."""
    return 'en' if road_slug == 'english' else 'uz'


def generate(lang='uz', avoid=(), rng=None):
    """One riddle, preferring a family this traveller has not met on this stage."""
    rng = rng or random
    fresh = [f for f in RIDDLES if f.__name__.replace('r_', '') not in set(avoid)]
    return rng.choice(fresh or RIDDLES)(rng, lang)
