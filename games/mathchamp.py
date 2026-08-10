"""
Matematika Chempionati — savol generatorlari.

Every question is generated on the fly, so no two championship runs are the
same. Each generator returns a dict:

    {
        'topic':       str   # badge shown above the question (Uzbek)
        'text':        str   # the question itself (Uzbek)
        'choices':     [str, str, str, str]
        'correct':     int   # 0-based index into choices
        'explanation': str   # worked solution shown after answering (Uzbek)
    }

`grade` is 5 / 6 / 7 and `tier` is 1 / 2 / 3 (championship round). Both scale
the number ranges; the tier also decides which topics are in play.
"""
import random
from math import gcd


# ---------------------------------------------------------------------------
# Number-theory helpers
# ---------------------------------------------------------------------------

def _divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def _is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def _prime_factorization(n):
    """Return e.g. '84 = 2 × 2 × 3 × 7'."""
    parts, m, d = [], n, 2
    while d * d <= m:
        while m % d == 0:
            parts.append(d)
            m //= d
        d += 1
    if m > 1:
        parts.append(m)
    return f"{n} = " + " × ".join(str(p) for p in parts)


def _largest_prime_factor(n):
    lpf, m, d = 1, n, 2
    while d * d <= m:
        while m % d == 0:
            lpf = d
            m //= d
        d += 1
    return max(lpf, m) if m > 1 else lpf


def _fmt_money(v):
    return f"{v:,}".replace(",", " ")


def _lcm(a, b):
    return a * b // gcd(a, b)


# ---------------------------------------------------------------------------
# Pupil names — the teacher's real students star in the word problems
# ---------------------------------------------------------------------------

_PUPILS = ['Jasur', 'Sherbek', 'Davron', 'Samandar', 'Kamron', 'Javohir',
           'Firdavs', "Ilg'or", 'Afsona', 'Madina', 'Charos', 'Bunyod']
_TEACHERS = ['Usman aka', 'Inom aka']


def _names(k=1):
    """k distinct pupil names (a single str for k=1, else a list)."""
    picked = random.sample(_PUPILS, k)
    return picked[0] if k == 1 else picked


# ---------------------------------------------------------------------------
# Choice assembly
# ---------------------------------------------------------------------------

def _pad_wrongs(correct, wrongs, lo=1):
    """Return exactly 3 unique wrong values ≠ correct (all ≥ lo; lo=None
    allows negatives)."""
    out = []
    for w in wrongs:
        if w != correct and w not in out and (lo is None or w >= lo):
            out.append(w)
        if len(out) == 3:
            return out
    delta = 1
    while len(out) < 3:
        for cand in (correct + delta, correct - delta):
            if cand != correct and cand not in out and (lo is None or cand >= lo):
                out.append(cand)
                if len(out) == 3:
                    break
        delta += 1
    return out[:3]


def _q(topic, text, correct, wrongs, explanation, unit='', lo=1, pad=True, fmt=None):
    """Build the final question dict from a correct value + wrong values."""
    if pad:
        wrongs = _pad_wrongs(correct, wrongs, lo=lo)
    else:
        wrongs = [w for w in dict.fromkeys(wrongs) if w != correct][:3]

    if fmt is None:
        def fmt(v):
            return f"{v} {unit}".strip() if unit else str(v)

    options = [(fmt(correct), True)] + [(fmt(w), False) for w in wrongs]
    random.shuffle(options)
    return {
        'topic':       topic,
        'text':        text,
        'choices':     [o[0] for o in options],
        'correct':     next(i for i, o in enumerate(options) if o[1]),
        'explanation': explanation,
    }


# ---------------------------------------------------------------------------
# Bo'linish belgilari (divisibility rules)
# ---------------------------------------------------------------------------

_DIV_RULES = {
    2:  "2 ga bo'linish belgisi: oxirgi raqami juft (0, 2, 4, 6, 8) bo'lishi kerak.",
    3:  "3 ga bo'linish belgisi: raqamlari yig'indisi 3 ga bo'linishi kerak.",
    4:  "4 ga bo'linish belgisi: oxirgi ikki raqamidan hosil bo'lgan son 4 ga bo'linishi kerak.",
    5:  "5 ga bo'linish belgisi: oxirgi raqami 0 yoki 5 bo'lishi kerak.",
    6:  "6 ga bo'linish belgisi: son ham 2 ga, ham 3 ga bo'linishi kerak.",
    8:  "8 ga bo'linish belgisi: oxirgi uch raqamidan hosil bo'lgan son 8 ga bo'linishi kerak.",
    9:  "9 ga bo'linish belgisi: raqamlari yig'indisi 9 ga bo'linishi kerak.",
    10: "10 ga bo'linish belgisi: oxirgi raqami 0 bo'lishi kerak.",
    25: "25 ga bo'linish belgisi: oxirgi ikki raqami 00, 25, 50 yoki 75 bo'lishi kerak.",
}

_DIV_POOL = {1: [2, 3, 5, 10], 2: [3, 4, 6, 9], 3: [4, 6, 8, 9, 25]}


def q_divisibility(grade, tier):
    d = random.choice(_DIV_POOL[tier])
    lo, hi = {1: (100, 999), 2: (100, 9999), 3: (1000, 99999)}[tier]

    if random.random() < 0.5:
        # Which of these numbers is divisible by d?
        correct = random.randint(lo // d, hi // d) * d
        wrongs, guard = [], 0
        while len(wrongs) < 3 and guard < 200:
            guard += 1
            cand = random.randint(lo, hi)
            if cand % d != 0 and cand != correct and cand not in wrongs:
                wrongs.append(cand)
        expl = (f"{_DIV_RULES[d]} Berilganlardan faqat {correct} bu shartni "
                f"bajaradi: {correct} ÷ {d} = {correct // d}.")
        return _q("Bo'linish belgilari",
                  f"Quyidagi sonlardan qaysi biri {d} ga qoldiqsiz bo'linadi?",
                  correct, wrongs, expl, pad=False)

    # n is divisible by which of these?
    others = [x for x in (2, 3, 4, 5, 6, 8, 9, 10, 25) if x != d]
    n, guard = None, 0
    while guard < 300:
        guard += 1
        cand = random.randint(lo // d, hi // d) * d
        bad = [x for x in others if cand % x != 0]
        if len(bad) >= 3:
            n, wrongs = cand, random.sample(bad, 3)
            break
    if n is None:                                   # extremely unlikely
        return q_remainder(grade, tier)
    expl = (f"{_DIV_RULES[d]} {n} ÷ {d} = {n // d}, demak {n} soni {d} ga "
            f"qoldiqsiz bo'linadi.")
    return _q("Bo'linish belgilari",
              f"{n} soni quyidagilardan qaysi biriga qoldiqsiz bo'linadi?",
              d, wrongs, expl, pad=False)


# ---------------------------------------------------------------------------
# EKUB / EKUK
# ---------------------------------------------------------------------------

_COPRIME_PAIRS = [(2, 3), (2, 5), (3, 4), (3, 5), (4, 5), (2, 7), (3, 7),
                  (5, 6), (5, 7), (4, 7), (3, 8), (5, 8), (2, 9), (4, 9)]

_G_POOL = {1: [2, 3, 4, 5, 6], 2: [6, 8, 9, 10, 12, 15], 3: [12, 14, 15, 16, 18, 20, 24]}


def _ekub_pair(grade, tier):
    g = random.choice(_G_POOL[tier])
    if grade >= 7 and tier == 3:
        g = random.choice([15, 18, 20, 24, 25])
    m1, m2 = random.choice(_COPRIME_PAIRS)
    return g, g * m1, g * m2, m1, m2


def q_ekub(grade, tier):
    g, a, b, m1, m2 = _ekub_pair(grade, tier)
    lcm = g * m1 * m2
    expl = (f"{a} = {g} × {m1}, {b} = {g} × {m2}. {m1} va {m2} o'zaro tub, "
            f"shuning uchun EKUB({a}; {b}) = {g}.")
    wrongs = [lcm, g * 2, min(a, b), g // 2, g + m1]
    return _q("EKUB", f"EKUB({a}; {b}) nechaga teng?", g, wrongs, expl)


def q_ekuk(grade, tier):
    g, a, b, m1, m2 = _ekub_pair(grade, tier)
    lcm = g * m1 * m2
    expl = (f"EKUB({a}; {b}) = {g}. EKUK({a}; {b}) = {a} × {b} ÷ EKUB = "
            f"{a * b} ÷ {g} = {lcm}.")
    wrongs = [g, a * b, lcm // 2, lcm + g, max(a, b)]
    return _q("EKUK", f"EKUK({a}; {b}) nechaga teng?", lcm, wrongs, expl)


def q_common_divisors(grade, tier):
    g = random.choice({2: [6, 8, 10, 12], 3: [12, 16, 18, 20, 24]}.get(tier, [6, 8, 12]))
    m1, m2 = random.choice(_COPRIME_PAIRS)
    a, b = g * m1, g * m2
    count = len(_divisors(g))
    div_str = ", ".join(str(d) for d in _divisors(g))
    expl = (f"Ikki sonning umumiy bo'luvchilari — bu ularning EKUBining "
            f"bo'luvchilaridir. EKUB({a}; {b}) = {g}, uning bo'luvchilari: "
            f"{div_str} — jami {count} ta.")
    wrongs = [count + 1, count - 1, count + 2, len(_divisors(a))]
    return _q("Umumiy bo'luvchilar",
              f"{a} va {b} sonlarining nechta umumiy bo'luvchisi bor?",
              count, wrongs, expl)


# ---------------------------------------------------------------------------
# Bo'luvchilar (number / sum of divisors, prime factors)
# ---------------------------------------------------------------------------

_TAU_POOL = {1: [12, 16, 18, 20, 28], 2: [24, 32, 36, 40, 45, 48], 3: [60, 72, 84, 90, 96, 100]}
_SIGMA_POOL = {1: [6, 8, 10, 12, 15], 2: [16, 18, 20, 24, 28], 3: [30, 32, 36, 40, 45, 48]}


def q_num_divisors(grade, tier):
    n = random.choice(_TAU_POOL[tier])
    divs = _divisors(n)
    count = len(divs)
    expl = (f"{n} ning bo'luvchilari: {', '.join(str(d) for d in divs)} — "
            f"jami {count} ta.")
    wrongs = [count - 1, count + 1, count - 2, count + 2]
    return _q("Bo'luvchilar soni",
              f"{n} sonining nechta bo'luvchisi bor?",
              count, wrongs, expl)


def q_sum_divisors(grade, tier):
    n = random.choice(_SIGMA_POOL[tier])
    divs = _divisors(n)
    total = sum(divs)
    expl = (f"{n} ning bo'luvchilari: {', '.join(str(d) for d in divs)}. "
            f"Yig'indisi: {' + '.join(str(d) for d in divs)} = {total}.")
    wrongs = [total - n, total - 1, total + n // 2, total + 2]
    return _q("Bo'luvchilar yig'indisi",
              f"{n} sonining barcha bo'luvchilari yig'indisini toping.",
              total, wrongs, expl)


def q_largest_prime(grade, tier):
    pool = {1: [30, 42, 45, 50, 54, 56],
            2: [66, 70, 78, 84, 90, 102, 105],
            3: [110, 120, 132, 154, 165, 182, 195, 231]}[tier]
    n = random.choice(pool)
    lpf = _largest_prime_factor(n)
    expl = (f"{_prime_factorization(n)}. Tub ko'paytuvchilar ichida eng "
            f"kattasi — {lpf}.")
    other_primes = [p for p in (2, 3, 5, 7, 11, 13, 17, 19) if p != lpf]
    wrongs = random.sample(other_primes, 2) + [lpf + 2, n // lpf]
    return _q("Tub bo'luvchilar",
              f"{n} sonining eng katta tub bo'luvchisini toping.",
              lpf, wrongs, expl)


_PRIME_PICK = {
    1: {'primes': [11, 13, 17, 19, 23, 29, 31, 37],
        'composites': [9, 15, 21, 25, 27, 33, 35, 39, 49]},
    2: {'primes': [41, 43, 47, 53, 59, 61, 67, 71],
        'composites': [51, 55, 57, 63, 65, 69, 77, 81, 85, 87]},
    3: {'primes': [73, 79, 83, 89, 97, 101, 103, 107, 109, 113],
        'composites': [91, 111, 117, 119, 121, 123, 129, 133, 141, 143]},
}


def q_prime_pick(grade, tier):
    pool = _PRIME_PICK[tier]
    p = random.choice(pool['primes'])
    comps = random.sample(pool['composites'], 3)
    facts = "; ".join(f"{_prime_factorization(c)}" for c in comps)
    expl = (f"{facts}. {p} esa faqat 1 ga va o'zining o'ziga bo'linadi — "
            f"demak {p} tub son.")
    return _q("Tub sonlar",
              "Quyidagi sonlardan qaysi biri tub son?",
              p, comps, expl, pad=False)


# ---------------------------------------------------------------------------
# Qoldiqli bo'lish (division with remainder)
# ---------------------------------------------------------------------------

def q_remainder(grade, tier):
    b = random.randint(*{1: (3, 9), 2: (6, 12), 3: (11, 25)}[tier])
    quot = random.randint(*{1: (5, 12), 2: (8, 25), 3: (12, 45)}[tier])
    r = random.randint(1, b - 1)
    a = b * quot + r
    expl = f"{a} = {b} × {quot} + {r}, demak qoldiq {r} ga teng."
    wrongs = [r + 1, r - 1, b - r, quot % 10 or quot]
    return _q("Qoldiqli bo'lish",
              f"{a} ni {b} ga bo'lganda qoldiq nechaga teng bo'ladi?",
              r, wrongs, expl, lo=0)


# ---------------------------------------------------------------------------
# Tezlik · Masofa · Vaqt
# ---------------------------------------------------------------------------

# (subject phrase, personal?, min speed, max speed) — personal subjects get a
# pupil's name in front: "Madina velosipedda …".
_VEHICLES = [
    ("piyoda", True, 4, 6),
    ("velosipedda", True, 10, 18),
    ("Avtobus", False, 40, 60),
    ("Avtomobil", False, 60, 90),
    ("Poyezd", False, 50, 80),
    ("Motorli qayiq", False, 15, 25),
]


def _pick_vehicle(tier):
    phrase, personal, lo, hi = random.choice(_VEHICLES)
    v = random.randint(lo, hi)
    if v > 20:
        v = round(v / 5) * 5
    t = random.randint(2, 4 if tier == 1 else 6)
    subj = f"{_names()} {phrase}" if personal else phrase
    return subj, v, t


def q_speed_basic(grade, tier):
    subj, v, t = _pick_vehicle(tier)
    s = v * t
    kind = random.choice(('dist', 'speed', 'time'))
    if kind == 'dist':
        expl = f"Masofa = tezlik × vaqt = {v} × {t} = {s} km."
        return _q("Tezlik va masofa",
                  f"{subj} {v} km/soat tezlik bilan {t} soat yurdi. "
                  f"Qancha masofa bosib o'tilgan?",
                  s, [v * (t + 1), v * (t - 1), s + v // 2 or s + 1, v + t], expl, unit="km")
    if kind == 'speed':
        expl = f"Tezlik = masofa ÷ vaqt = {s} ÷ {t} = {v} km/soat."
        return _q("Tezlik va masofa",
                  f"{subj} {s} km masofani {t} soatda bosib o'tdi. "
                  f"Tezlikni toping.",
                  v, [v + 5, v - 5, v + 10, s - t], expl, unit="km/soat")
    expl = f"Vaqt = masofa ÷ tezlik = {s} ÷ {v} = {t} soat."
    return _q("Tezlik va masofa",
              f"{subj} {s} km masofani {v} km/soat tezlik bilan bosib o'tdi. "
              f"Bunga qancha vaqt ketgan?",
              t, [t + 1, t - 1, t + 2], expl, unit="soat")


def q_speed_hard(grade, tier):
    n1, n2 = _names(2)
    if random.random() < 0.5:
        # Two pupils moving towards each other.
        if random.random() < 0.5:
            ride, v1, v2 = "velosipedlarida", random.randint(12, 20), random.randint(8, 14)
            place = "Ikki qishloq"
        else:
            ride, v1, v2 = "avtomobillarda", random.randint(9, 18) * 5, random.randint(6, 12) * 5
            place = "Ikki shahar"
        t = random.randint(2, 4)
        s = (v1 + v2) * t
        expl = (f"Yaqinlashish tezligi: {v1} + {v2} = {v1 + v2} km/soat. "
                f"Vaqt = {s} ÷ {v1 + v2} = {t} soat.")
        return _q("Tezlik va masofa",
                  f"{place} orasidagi masofa {s} km. {n1} va {n2} bir vaqtda "
                  f"{ride} bir-biriga qarab yo'lga chiqishdi. {n1}ning tezligi "
                  f"{v1} km/soat, {n2}ning tezligi {v2} km/soat. Ular necha "
                  f"soatdan keyin uchrashadi?",
                  t, [t + 1, t - 1, t + 2], expl, unit="soat")
    # Catch-up problem.
    v1 = random.randint(2, 5) * 5
    v2 = v1 + random.choice((5, 10, 15))
    t = random.randint(2, 4)
    gap = (v2 - v1) * t
    expl = (f"Tezliklar farqi: {v2} − {v1} = {v2 - v1} km/soat. "
            f"Quvib yetish vaqti = {gap} ÷ {v2 - v1} = {t} soat.")
    return _q("Tezlik va masofa",
              f"{n1} velosipedda {v1} km/soat tezlik bilan yo'lga chiqdi. "
              f"Undan {gap} km orqada bo'lgan {n2} mopedda {v2} km/soat "
              f"tezlik bilan uni quvib ketdi. {n2} {n1}ni necha soatda "
              f"quvib yetadi?",
              t, [t + 1, t - 1, t + 2], expl, unit="soat")


# ---------------------------------------------------------------------------
# Matnli masalalar (word problems)
# ---------------------------------------------------------------------------

def q_word_easy(grade, tier):
    kind = random.choice(('class', 'age', 'rect', 'candy'))
    if kind == 'class':
        b = random.randint(8, 16)
        d = random.randint(2, 6)
        total = 2 * b + d
        expl = (f"Qizlar soni: {b} + {d} = {b + d}. Jami o'quvchilar: "
                f"{b} + {b + d} = {total} ta.")
        return _q("Matnli masala",
                  f"Sinfda {b} nafar o'g'il bola bor, qizlar esa o'g'il "
                  f"bolalardan {d} nafar ko'p. Sinfda jami nechta o'quvchi bor?",
                  total, [b + d, total - d, total + d, 2 * b], expl)
    if kind == 'age':
        name = _names()
        a = random.randint(6, 12)
        k = random.choice((3, 4, 5))
        father = k * a
        expl = f"Dadasining yoshi: {a} × {k} = {father} yosh."
        return _q("Matnli masala",
                  f"{name} {a} yoshda. Uning dadasi {name}dan {k} marta "
                  f"katta. Dadasi necha yoshda?",
                  father, [father + a, father - a, a + k, father + k], expl, unit="yoshda")
    if kind == 'rect':
        a = random.randint(6, 15)
        b = random.randint(3, a - 1)
        if random.random() < 0.5:
            p = 2 * (a + b)
            expl = f"Perimetr = 2 × (bo'yi + eni) = 2 × ({a} + {b}) = {p} sm."
            return _q("Matnli masala",
                      f"To'g'ri to'rtburchakning bo'yi {a} sm, eni {b} sm. "
                      f"Uning perimetrini toping.",
                      p, [a * b, a + b, 2 * a + b], expl, unit="sm")
        yuza = a * b
        expl = f"Yuza = bo'yi × eni = {a} × {b} = {yuza} sm²."
        return _q("Matnli masala",
                  f"To'g'ri to'rtburchakning bo'yi {a} sm, eni {b} sm. "
                  f"Uning yuzini toping.",
                  yuza, [2 * (a + b), a + b, yuza + a], expl, unit="sm²")
    name = _names()
    per = random.randint(3, 9)
    k = random.randint(4, 8)
    n = per * k
    expl = f"Har bir do'stiga: {n} ÷ {k} = {per} tadan konfet tegadi."
    return _q("Matnli masala",
              f"{name} {n} ta konfetni {k} nafar do'stiga teng bo'lib "
              f"tarqatdi. Har bir do'stiga nechtadan konfet tegdi?",
              per, [per + 1, per - 1, per + 2], expl)


def q_word_mid(grade, tier):
    roll = random.random()
    if roll < 0.35:
        # Sum & difference (abstract).
        small = random.randint(8, 30)
        diff = random.randint(2, 12) * 2
        big = small + diff
        s = big + small
        expl = (f"Katta son = (yig'indi + ayirma) ÷ 2 = ({s} + {diff}) ÷ 2 = "
                f"{big}. Tekshiruv: {big} + {small} = {s}, {big} − {small} = {diff}.")
        return _q("Matnli masala",
                  f"Ikki sonning yig'indisi {s}, ayirmasi esa {diff} ga teng. "
                  f"Katta sonni toping.",
                  big, [small, s // 2, big + 1, big - diff], expl)
    if roll < 0.7:
        # Sum & difference (story: two pupils fishing).
        n1, n2 = _names(2)
        small = random.randint(4, 15)
        diff = random.randint(1, 5) * 2
        big = small + diff
        s = big + small
        expl = (f"{n1} = (jami + farq) ÷ 2 = ({s} + {diff}) ÷ 2 = {big}. "
                f"Tekshiruv: {n2}: {small} ta, {big} + {small} = {s}.")
        return _q("Matnli masala",
                  f"{n1} va {n2} birgalikda {s} ta baliq tutishdi. {n1} "
                  f"{n2}dan {diff} ta ko'p baliq tutdi. {n1} nechta baliq "
                  f"tutgan?",
                  big, [small, s // 2, big + 1, big - diff], expl)
    # Shopping.
    name = _names()
    p = random.choice((2000, 2500, 3000, 3500, 4000))
    q = random.choice((1000, 1500, 2000, 2500))
    n = random.randint(2, 5)
    m = random.randint(2, 5)
    total = n * p + m * q
    expl = (f"Daftarlar: {n} × {_fmt_money(p)} = {_fmt_money(n * p)} so'm. "
            f"Ruchkalar: {m} × {_fmt_money(q)} = {_fmt_money(m * q)} so'm. "
            f"Jami: {_fmt_money(total)} so'm.")
    return _q("Matnli masala",
              f"{name} {n} ta daftar va {m} ta ruchka sotib oldi. Bitta "
              f"daftar {_fmt_money(p)} so'm, bitta ruchka {_fmt_money(q)} "
              f"so'm turadi. {name} qancha pul to'lagan?",
              total, [total + q, total - q, total + p, n * p + q], expl,
              lo=500, fmt=lambda v: f"{_fmt_money(v)} so'm")


def q_word_hard(grade, tier):
    if random.random() < 0.5:
        # Sum & multiple: one number k times the other.
        small = random.randint(6, 20)
        k = random.choice((2, 3, 4))
        big = k * small
        s = big + small
        expl = (f"Kichik son x bo'lsa, katta son {k}x. x + {k}x = {k + 1}x = {s}, "
                f"demak x = {s} ÷ {k + 1} = {small}. Katta son: {k} × {small} = {big}.")
        return _q("Matnli masala",
                  f"Ikki sonning yig'indisi {s} ga teng. Katta son kichik "
                  f"sondan {k} marta katta. Katta sonni toping.",
                  big, [small, s - small * 2, big + k, s // 2], expl)
    # Three consecutive numbers.
    mid = random.randint(15, 60)
    s = 3 * mid
    expl = (f"Uchta ketma-ket sonning yig'indisi o'rtadagi sonning 3 barobariga "
            f"teng: {s} ÷ 3 = {mid}. Demak eng kattasi {mid + 1}.")
    return _q("Matnli masala",
              f"Uchta ketma-ket natural sonning yig'indisi {s} ga teng. "
              f"Ularning eng kattasini toping.",
              mid + 1, [mid, mid - 1, mid + 2], expl)


# ---------------------------------------------------------------------------
# Kasrlar (fractions)
# ---------------------------------------------------------------------------

def _simplify(n, d):
    g = gcd(n, d)
    return n // g, d // g


def _uniq_str_wrongs(correct, cands, fallback):
    """3 unique wrong strings ≠ correct; `fallback(i)` fills any gap."""
    out = []
    for c in cands:
        if c != correct and c not in out:
            out.append(c)
    i = 0
    while len(out) < 3 and i < 50:
        f = fallback(i)
        if f != correct and f not in out:
            out.append(f)
        i += 1
    return out[:3]


def q_fraction_of(grade, tier):
    """Fraction of a number: '48 ning 3/4 qismi'."""
    d = random.choice((2, 3, 4, 5, 6, 8, 10))
    n = random.randint(1, d - 1)
    n, d = _simplify(n, d)
    base = d * random.randint(3, 12 if tier == 1 else 25)
    ans = base // d * n
    expl = f"Avval {d} dan bir qismini topamiz: {base} ÷ {d} = {base // d}."
    if n > 1:
        expl += f" So'ngra {n} ga ko'paytiramiz: {base // d} × {n} = {ans}."
    return _q("Kasrlar",
              f"{base} sonining {n}/{d} qismini toping.",
              ans, [base // d, base - ans, ans + base // d, ans - base // d], expl)


_FRAC_DEN_PAIRS = [(2, 3), (3, 4), (2, 5), (3, 5), (4, 6), (2, 7), (4, 5), (6, 8), (3, 8)]


def q_fraction_add(grade, tier):
    """Add/subtract fractions. Grade 5 keeps a common denominator; grades 6–7
    get unlike denominators — with the classic 'add tops and bottoms' trap."""
    sub = random.random() < 0.4
    if grade <= 5:
        d = random.choice((5, 7, 8, 9, 10, 12))
        n1 = random.randint(2, d - 2)
        n2 = random.randint(1, (n1 - 1) if sub else (d - n1 - 1) or 1)
        raw = n1 - n2 if sub else n1 + n2
        rn, rd = _simplify(raw, d)
        op = '−' if sub else '+'
        correct = f"{rn}/{rd}"
        cands = [f"{raw}/{d * 2}", f"{raw + 1}/{d}", f"{n1 * n2}/{d}"]
        if (rn, rd) != (raw, d):
            cands.insert(0, f"{raw + 2}/{d}")
        expl = (f"Maxrajlar bir xil, suratlarni {'ayiramiz' if sub else 'qoʻshamiz'}: "
                f"{n1} {op} {n2} = {raw}. Javob: {raw}/{d}"
                + (f" = {rn}/{rd} (qisqartirdik)." if (rn, rd) != (raw, d) else "."))
        wrongs = _uniq_str_wrongs(correct, cands, lambda i: f"{rn + i + 1}/{rd}")
        return _q("Kasrlar", f"Hisoblang: {n1}/{d} {op} {n2}/{d}",
                  correct, wrongs, expl, pad=False)

    d1, d2 = random.choice(_FRAC_DEN_PAIRS)
    L = _lcm(d1, d2)
    n1 = random.randint(1, d1 - 1)
    n2 = random.randint(1, d2 - 1)
    a, b = n1 * L // d1, n2 * L // d2
    if sub and a <= b:
        sub = False
    raw = a - b if sub else a + b
    rn, rd = _simplify(raw, L)
    op = '−' if sub else '+'
    correct = f"{rn}/{rd}"
    trap_num = n1 - n2 if sub else n1 + n2               # classic error:
    if trap_num <= 0:                                    # tops/bottoms combined
        trap_num = n1 + n2
    trap = f"{trap_num}/{d1 + d2}"
    cands = [trap, f"{raw}/{L}" if (rn, rd) != (raw, L) else f"{raw + 1}/{L}",
             f"{n1 + n2}/{L}"]
    expl = (f"Umumiy maxraj: EKUK({d1}; {d2}) = {L}. "
            f"{n1}/{d1} = {a}/{L}, {n2}/{d2} = {b}/{L}. "
            f"{a}/{L} {op} {b}/{L} = {raw}/{L}"
            + (f" = {rn}/{rd}." if (rn, rd) != (raw, L) else ".")
            + " (Maxrajlarni qo'shib bo'lmaydi!)")
    wrongs = _uniq_str_wrongs(correct, cands, lambda i: f"{rn + i + 1}/{rd}")
    return _q("Kasrlar", f"Hisoblang: {n1}/{d1} {op} {n2}/{d2}",
              correct, wrongs, expl, pad=False)


_CMP_FRACTIONS = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 6), (5, 6),
                  (1, 8), (3, 8), (5, 8), (7, 8), (5, 12), (7, 12), (11, 12)]


def q_fraction_compare(grade, tier):
    picks = random.sample(_CMP_FRACTIONS, 4)
    biggest = random.random() < 0.6
    key = max if biggest else min
    target = key(picks, key=lambda f: f[0] / f[1])
    L = 24
    conv = ", ".join(f"{n}/{d} = {n * L // d}/{L}" for n, d in picks)
    word = "kattasi" if biggest else "kichigi"
    expl = (f"Umumiy maxraj {L} ga keltiramiz: {conv}. Eng {word}: "
            f"{target[0]}/{target[1]} = {target[0] * L // target[1]}/{L}.")
    correct = f"{target[0]}/{target[1]}"
    wrongs = [f"{n}/{d}" for n, d in picks if (n, d) != target]
    return _q("Kasrlar", f"Qaysi kasr eng {word}?", correct, wrongs, expl, pad=False)


# ---------------------------------------------------------------------------
# Tenglamalar (equations with x)
# ---------------------------------------------------------------------------

def _sgn(b):
    return f"+ {b}" if b >= 0 else f"− {-b}"


def _cx(a):
    return "x" if a == 1 else f"{a}x"


def q_equation(grade, tier):
    x0 = random.randint(2, 12)
    if grade <= 5:
        form = 'one'
    elif grade == 6:
        form = 'two' if tier <= 2 else random.choice(('two', 'both', 'both'))
    else:
        form = 'both' if tier <= 2 else random.choice(('both', 'bracket'))

    if form == 'one':
        if random.random() < 0.5:
            b = random.randint(5, 40)
            eq = f"x + {b} = {x0 + b}"
            expl = f"x = {x0 + b} − {b} = {x0}."
        else:
            a = random.randint(3, 9)
            eq = f"{a}x = {a * x0}"
            expl = f"x = {a * x0} ÷ {a} = {x0}."
    elif form == 'two':
        a = random.randint(2, 7)
        b = random.randint(-15, 15) or 5
        c = a * x0 + b
        eq = f"{_cx(a)} {_sgn(b)} = {c}"
        move = f"{c} − {b}" if b >= 0 else f"{c} + {-b}"
        expl = f"{a}x = {move} = {a * x0}, demak x = {a * x0} ÷ {a} = {x0}."
    elif form == 'both':
        a2 = random.randint(1, 4)
        da = random.randint(1, 3)
        a1 = a2 + da
        b1 = random.choice([b for b in range(-9, 10) if b != 0 and b != -da * x0])
        b2 = b1 + da * x0
        eq = f"{_cx(a1)} {_sgn(b1)} = {_cx(a2)} {_sgn(b2)}"
        b1s = f"({b1})" if b1 < 0 else f"{b1}"
        expl = (f"x larni bir tomonga o'tkazamiz: {a1}x − {a2}x = {b2} − {b1s}, "
                f"ya'ni {_cx(da)} = {da * x0}, demak x = {x0}.")
    else:  # bracket
        a = random.randint(2, 6)
        b = random.choice([b for b in range(1 - x0, 9) if b != 0])
        c = a * (x0 + b)
        eq = f"{a}(x {_sgn(b)}) = {c}"
        inner = f"{c} ÷ {a} = {x0 + b}"
        back = f"{x0 + b} − {b}" if b >= 0 else f"{x0 + b} + {-b}"
        expl = f"x {_sgn(b)} = {inner}, demak x = {back} = {x0}."

    return _q("Tenglamalar", f"Tenglamani yeching: {eq}",
              x0, [x0 + 1, x0 - 1, x0 + 2, x0 * 2], expl, lo=None)


# ---------------------------------------------------------------------------
# Oqim va shamol (boat with/against current, plane with/against wind)
# ---------------------------------------------------------------------------

def q_boat_wind(grade, tier):
    if random.random() < 0.6:
        subj, medium = "Qayiqning turg'un suvdagi", "daryo oqimining"
        with_txt, against_txt = "oqim bo'ylab", "oqimga qarshi"
        verb = "suzadi"
        v = random.randint(12, 20)
        c = random.randint(2, 4)
    else:
        subj, medium = "Samolyotning o'z", "shamolning"
        with_txt, against_txt = "shamol yo'nalishida", "shamolga qarshi"
        verb = "uchadi"
        v = random.randint(20, 30) * 10
        c = random.randint(2, 5) * 10
    t = random.randint(2, 4)
    downstream = random.random() < 0.5
    eff = v + c if downstream else v - c
    direction = with_txt if downstream else against_txt
    op = '+' if downstream else '−'

    if random.random() < 0.5:
        s = eff * t
        expl = (f"{direction.capitalize()} tezlik: {v} {op} {c} = {eff} km/soat. "
                f"Masofa: {eff} × {t} = {s} km.")
        return _q("Oqim va shamol",
                  f"{subj} tezligi {v} km/soat, {medium} tezligi {c} km/soat. "
                  f"{direction.capitalize()} {t} soatda qancha masofa {verb}?",
                  s, [(v - c if downstream else v + c) * t, v * t, eff * (t + 1)],
                  expl, unit="km")
    s = eff * t
    other_t = s // (v + c) if not downstream and s % (v + c) == 0 else t + 1
    expl = (f"{direction.capitalize()} tezlik: {v} {op} {c} = {eff} km/soat. "
            f"Vaqt: {s} ÷ {eff} = {t} soat.")
    return _q("Oqim va shamol",
              f"{subj} tezligi {v} km/soat, {medium} tezligi {c} km/soat. "
              f"{direction.capitalize()} {s} km masofani necha soatda bosib o'tadi?",
              t, [other_t, t - 1, t + 2], expl, unit="soat")


# ---------------------------------------------------------------------------
# Ayniyatlar (7th grade: a² − b² and (a+b)² shortcuts)
# ---------------------------------------------------------------------------

_SUP = {2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶'}


def q_square_diff(grade, tier):
    roll = random.random()
    if roll < 0.4:
        # Clever computation: a² − b² where a+b and a−b are friendly.
        s = random.choice((20, 40, 50, 60, 100))
        m = random.choice((2, 4, 6, 10))
        a, b = (s + m) // 2, (s - m) // 2
        ans = m * s
        expl = (f"a² − b² = (a − b)(a + b) ayniyatidan: "
                f"({a} − {b})({a} + {b}) = {m} × {s} = {ans}.")
        return _q("Ayniyatlar",
                  f"Qulay usul bilan hisoblang: {a}² − {b}²",
                  ans, [m * m, s, ans + s, ans - m], expl)
    if roll < 0.75:
        # Given a+b and a−b, find a² − b².
        s = random.randint(6, 15)
        m = random.randint(1, 5)
        ans = s * m
        expl = (f"a² − b² = (a + b)(a − b) = {s} × {m} = {ans}. "
                f"a va b ni alohida topish shart emas!")
        return _q("Ayniyatlar",
                  f"Agar a + b = {s} va a − b = {m} bo'lsa, a² − b² nechaga teng?",
                  ans, [s + m, s * s, ans * 2, s - m], expl)
    # (a+b)² shortcut: 41² = (40+1)².
    base = random.choice((21, 31, 41, 51, 61, 29, 39, 49))
    t, u = (base // 10) * 10, base % 10
    if u > 5:
        t, u = t + 10, u - 10   # 29 = 30 − 1
    ans = base * base
    op = '+' if u >= 0 else '−'
    expl = (f"{base}² = ({t} {op} {abs(u)})² = {t}² {op} 2·{t}·{abs(u)} + {abs(u)}² = "
            f"{t * t} {op} {2 * t * abs(u)} + {u * u} = {ans}.")
    return _q("Ayniyatlar",
              f"Qulay usul bilan hisoblang: {base}²",
              ans, [ans - 2 * t * abs(u) if u > 0 else ans + 2 * t * abs(u),
                    ans + 10, ans - 1], expl)


# ---------------------------------------------------------------------------
# Foizlar (percentages)
# ---------------------------------------------------------------------------

def q_percent(grade, tier):
    p = random.choice((10, 20, 25, 50))
    if tier >= 3 and random.random() < 0.5:
        name = _names()
        price = random.randint(8, 40) * 1000
        up = random.random() < 0.4
        ans = price * (100 + p) // 100 if up else price * (100 - p) // 100
        change = "qimmatlashdi" if up else "arzonlashdi"
        op = '+' if up else '−'
        delta = price * p // 100
        expl = (f"{p}% = {_fmt_money(delta)} so'm. Yangi narx: "
                f"{_fmt_money(price)} {op} {_fmt_money(delta)} = {_fmt_money(ans)} so'm.")
        return _q("Foizlar",
                  f"{name} olmoqchi bo'lgan kitob {_fmt_money(price)} so'm edi. "
                  f"Narx {p}% ga {change}. Kitobning yangi narxi qancha?",
                  ans, [delta, price * (100 + (p if not up else -p)) // 100,
                        price - p, ans + 1000],
                  expl, lo=100, fmt=lambda v: f"{_fmt_money(v)} so'm")
    n = (100 // p) * random.randint(2, 12)
    ans = n * p // 100
    expl = f"{p}% — bu {p}/100 qism. {n} × {p} ÷ 100 = {ans}."
    return _q("Foizlar", f"{n} sonining {p}% ini toping.",
              ans, [n * p // 10, ans * 2, ans // 2, n - ans], expl)


# ---------------------------------------------------------------------------
# Butun sonlar (operations with negative numbers)
# ---------------------------------------------------------------------------

def q_integers(grade, tier):
    a = random.randint(2, 12)
    b = random.randint(2, 12)
    form = random.choice(('add', 'sub_neg', 'mul_neg', 'mul_both'))
    if form == 'add':
        big = max(a, b) + random.randint(1, 6)
        ans = -big + a
        expl = (f"(−{big}) + {a}: ishoralar har xil, kattasidan kichigini "
                f"ayiramiz: {big} − {a} = {big - a}, ishora kattanikidan — javob {ans}.")
        text = f"Hisoblang: (−{big}) + {a}"
    elif form == 'sub_neg':
        ans = a + b
        expl = f"Manfiy sonni ayirish — qo'shish bilan bir xil: {a} − (−{b}) = {a} + {b} = {ans}."
        text = f"Hisoblang: {a} − (−{b})"
    elif form == 'mul_neg':
        ans = -(a * b)
        expl = f"Musbat × manfiy = manfiy: {a} × {b} = {a * b}, javob {ans}."
        text = f"Hisoblang: {a} × (−{b})"
    else:
        ans = a * b
        expl = f"Manfiy × manfiy = musbat: {a} × {b} = {ans}."
        text = f"Hisoblang: (−{a}) × (−{b})"
    return _q("Butun sonlar", text, ans, [-ans, ans + 2, ans - 2, abs(ans) + 1],
              expl, lo=None)


# ---------------------------------------------------------------------------
# Darajalar (powers)
# ---------------------------------------------------------------------------

def q_power(grade, tier):
    if tier >= 2 and random.random() < 0.4:
        base = random.choice((2, 3, 5, 7, 10))
        e1 = random.randint(2, 4)
        e2 = random.randint(2, 6 - e1)          # keep e1+e2 ≤ 6 (superscript map)
        correct = f"{base}{_SUP[e1 + e2]}"
        expl = (f"Bir xil asosli darajalarni ko'paytirganda ko'rsatkichlar "
                f"qo'shiladi: {base}{_SUP[e1]} × {base}{_SUP[e2]} = "
                f"{base}{_SUP[e1 + e2]}. (Ko'rsatkichlar ko'paytirilmaydi!)")
        wrongs = _uniq_str_wrongs(
            correct,
            [f"{base}{_SUP[min(e1 * e2, 6)]}", f"{base * base}{_SUP[e1 + e2]}",
             f"{base}{_SUP[2]}"],
            lambda i: f"{base + i + 1}{_SUP[e1 + e2]}")
        return _q("Darajalar",
                  f"Natijani daraja ko'rinishida yozing: {base}{_SUP[e1]} × {base}{_SUP[e2]}",
                  correct, wrongs, expl, pad=False)
    base, e = random.choice(((2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (4, 3), (5, 3), (10, 3)))
    ans = base ** e
    expl = (f"{base}{_SUP[e]} = {' × '.join([str(base)] * e)} = {ans}. "
            f"({base} × {e} = {base * e} emas!)")
    return _q("Darajalar", f"Hisoblang: {base}{_SUP[e]}",
              ans, [base * e, base ** (e - 1), ans * base, ans - base], expl)


# ---------------------------------------------------------------------------
# Ikki bosqichli masalalar (two-step reasoning problems)
# ---------------------------------------------------------------------------

_MEETING_PAIRS = {2: [(2, 3), (3, 4), (4, 6), (3, 5), (4, 5), (6, 8), (2, 5)],
                  3: [(4, 6), (6, 8), (6, 9), (5, 7), (8, 12), (10, 15), (9, 12), (12, 18)]}
_MEETING_TRIPLES = [(2, 3, 4), (3, 4, 6), (4, 6, 8), (2, 5, 6), (3, 5, 6), (2, 4, 5)]
_MEETING_PLACES = ["kutubxonaga", "sport zaliga", "shaxmat to'garagiga",
                   "suzish mashg'ulotiga", "matematika to'garagiga"]


def _multiples_str(a, upto):
    return ", ".join(str(m) for m in range(a, upto + 1, a))


def q_ekuk_meeting(grade, tier):
    """The classic 'one goes every a days, the other every b days' problem —
    spotting that it's an EKUK question is the first step."""
    place = random.choice(_MEETING_PLACES)
    if tier == 3 and random.random() < 0.4:
        a, b, c = random.choice(_MEETING_TRIPLES)
        l = _lcm(_lcm(a, b), c)
        n1, n2, n3 = _names(3)
        expl = (f"Uchalasi EKUK({a}; {b}; {c}) kundan keyin yana birga "
                f"boradi. EKUK({a}; {b}; {c}) = {l}.")
        return _q("EKUK",
                  f"{n1} {place} har {a} kunda, {n2} har {b} kunda, {n3} esa "
                  f"har {c} kunda boradi. Bugun uchalasi birga bordi. Ular "
                  f"yana necha kundan keyin birga boradilar?",
                  l, [l * 2, l // 2, a * b * c, a + b + c], expl, unit="kun")
    a, b = random.choice(_MEETING_PAIRS[min(tier, 3) if tier >= 2 else 2])
    l = _lcm(a, b)
    n1, n2 = _names(2)
    expl = (f"Bu — EKUK masalasi. {n1}ning kunlari: {_multiples_str(a, l)}; "
            f"{n2}ning kunlari: {_multiples_str(b, l)}. Birinchi umumiy kun: "
            f"EKUK({a}; {b}) = {l}.")
    return _q("EKUK",
              f"{n1} {place} har {a} kunda, {n2} esa har {b} kunda boradi. "
              f"Bugun ular u yerda uchrashishdi. Ular yana necha kundan "
              f"keyin uchrashadilar?",
              l, [a * b, a + b, l * 2, l // 2], expl, unit="kun")


_SHARE_ITEMS = [("daftar", "ruchka"), ("olma", "nok"), ("konfet", "pechene")]


def q_ekub_sharing(grade, tier):
    """Fair-sharing problem: the number of pupils must divide both amounts,
    so the answer is the EKUB — a two-step 'spot it, then compute' task."""
    g = random.choice({2: [6, 8, 9, 12], 3: [12, 15, 16, 18, 24]}.get(tier, [6, 8, 12]))
    m1, m2 = random.choice(_COPRIME_PAIRS)
    a, b = g * m1, g * m2
    i1, i2 = random.choice(_SHARE_ITEMS)
    teacher = random.choice(_TEACHERS)
    expl = (f"O'quvchilar soni ham {a} ni, ham {b} ni qoldiqsiz bo'lishi "
            f"kerak — demak bu EKUB masalasi. EKUB({a}; {b}) = {g}. Har bir "
            f"o'quvchiga {m1} ta {i1} va {m2} ta {i2} tegadi.")
    return _q("EKUB",
              f"{teacher} {a} ta {i1} va {b} ta {i2}ni o'quvchilarga teng "
              f"taqsimlamoqchi: har biriga bir xil miqdorda tegishi va hech "
              f"narsa ortib qolmasligi kerak. Eng ko'pi bilan nechta "
              f"o'quvchiga taqsimlash mumkin?",
              g, [_lcm(a, b) // g, m1 + m2, g * 2, g // 2], expl)


def q_money_compare(grade, tier):
    """Comparison money problem: first find the second amount, then combine."""
    n1, n2 = _names(2)
    x = random.randint(4, 20) * 500
    if random.random() < 0.5:
        k = random.choice((2, 3, 4))
        other, total = k * x, x + k * x
        cmp_txt = f"{n2}da esa undan {k} marta ko'p pul bor"
        step1 = f"{n2}da: {k} × {_fmt_money(x)} = {_fmt_money(other)} so'm."
    else:
        d = random.randint(1, x // 1000) * 500
        other, total = x - d, x + (x - d)
        cmp_txt = f"{n2}da esa undan {_fmt_money(d)} so'm kam pul bor"
        step1 = f"{n2}da: {_fmt_money(x)} − {_fmt_money(d)} = {_fmt_money(other)} so'm."
    expl = (f"{step1} Jami: {_fmt_money(x)} + {_fmt_money(other)} = "
            f"{_fmt_money(total)} so'm.")
    return _q("Matnli masala",
              f"{n1}da {_fmt_money(x)} so'm bor, {cmp_txt}. Ikkalasida "
              f"birgalikda qancha pul bor?",
              total, [other, total + x, total - x // 2, x * 2], expl,
              lo=500, fmt=lambda v: f"{_fmt_money(v)} so'm")


def q_work_compare(grade, tier):
    """Rates: either 'who finishes their book first?' (compare two divisions)
    or 'how long working together?' (combine two rates)."""
    n1, n2 = _names(2)
    if random.random() < 0.5:
        # Reading race — answer cards name the winner AND the day count.
        r1, r2 = random.sample((6, 8, 9, 10, 12, 15), 2)
        d1, d2 = random.sample(range(4, 10), 2)
        p1, p2 = r1 * d1, r2 * d2
        winner, wd, loser, ld = (n1, d1, n2, d2) if d1 < d2 else (n2, d2, n1, d1)
        expl = (f"{n1}: {p1} ÷ {r1} = {d1} kun. {n2}: {p2} ÷ {r2} = {d2} kun. "
                f"{wd} < {ld}, demak {winner} oldinroq tugatadi.")
        return _q("Matnli masala",
                  f"{n1} {p1} betlik kitobni har kuni {r1} betdan o'qiydi. "
                  f"{n2} esa {p2} betlik kitobni har kuni {r2} betdan "
                  f"o'qiydi. Qaysi biri kitobini oldinroq tugatadi?",
                  f"{winner} ({wd} kunda)",
                  [f"{loser} ({ld} kunda)", f"{winner} ({ld} kunda)",
                   f"{loser} ({wd} kunda)"],
                  expl, pad=False)
    # Working together.
    r1 = random.randint(3, 8)
    r2 = random.randint(3, 8)
    while r2 == r1:
        r2 = random.randint(3, 8)
    t = random.randint(2, 5)
    total = (r1 + r2) * t
    expl = (f"Birgalikda bir soatda: {r1} + {r2} = {r1 + r2} ta masala. "
            f"Vaqt: {total} ÷ {r1 + r2} = {t} soat.")
    return _q("Matnli masala",
              f"{n1} bir soatda {r1} ta, {n2} esa {r2} ta masala yechadi. "
              f"Ular birgalikda {total} ta masalani necha soatda yechishadi?",
              t, [t + 1, t - 1, t + 2], expl, unit="soat")


# ---------------------------------------------------------------------------
# Foizlar — teskari masalalar (percent: find the number, find the percent)
# ---------------------------------------------------------------------------

_PCT_EASY = (10, 20, 25, 50)
_PCT_ALL  = (5, 10, 20, 25, 40, 50, 60, 75, 80)


def _pct_number(p, lo=2, hi=14):
    """A number n such that p% of n is a whole number."""
    return (100 // gcd(p, 100)) * random.randint(lo, hi)


def q_percent_reverse(grade, tier):
    """The 'if 20% of a number is 40, what is the number?' family — the pupil
    has to go backwards from the part to the whole."""
    p = random.choice(_PCT_ALL if tier >= 2 else _PCT_EASY)
    roll = random.random()

    if roll < 0.35:
        n = _pct_number(p)
        val = n * p // 100
        expl = (f"Noma'lum son x bo'lsin: x ning {p}% i = x × {p} ÷ 100 = {val}. "
                f"Bundan x = {val} × 100 ÷ {p} = {n}. "
                f"Tekshiruv: {n} ning {p}% i = {val}.")
        return _q("Foizlar", f"Sonning {p}% i {val} ga teng. Shu sonni toping.",
                  n, [val * p, val + p, val * 100, n // 2], expl)

    if roll < 0.65:
        # Same idea wrapped in a story — a class where only 5% are girls would
        # be a strange thing to ask about, so the story uses big shares only.
        p = random.choice((20, 25, 40, 50, 60, 75, 80))
        step = 100 // gcd(p, 100)
        total = step * random.randint(max(2, 20 // step), 50 // step)
        part = total * p // 100
        expl = (f"Jami o'quvchilar soni x bo'lsa, x ning {p}% i = {part}. "
                f"x = {part} × 100 ÷ {p} = {total} ta.")
        return _q("Foizlar",
                  f"Sinf o'quvchilarining {p}% i, ya'ni {part} nafari qiz bola. "
                  f"Sinfda jami nechta o'quvchi bor?",
                  total, [part * p, total - part, part * 2, total + part], expl)

    # Reverse of a discount: the price AFTER the cut is given.
    name = _names()
    p = random.choice((10, 20, 25, 40, 50))     # a realistic sale
    step = 100 // gcd(p, 100)
    price = step * random.randint(2, 12) * 1000
    new = price * (100 - p) // 100
    expl = (f"Chegirmadan keyingi narx avvalgi narxning {100 - p}% ini tashkil "
            f"qiladi: x × {100 - p} ÷ 100 = {_fmt_money(new)}. Bundan "
            f"x = {_fmt_money(new)} × 100 ÷ {100 - p} = {_fmt_money(price)} so'm.")
    return _q("Foizlar",
              f"{name} sotib olgan krossovka {p}% chegirmadan keyin "
              f"{_fmt_money(new)} so'm bo'ldi. Chegirmagacha uning narxi "
              f"qancha edi?",
              price, [new * (100 + p) // 100, new + p * 100, new * 2,
                      new + price // 10],
              expl, lo=500, fmt=lambda v: f"{_fmt_money(v)} so'm")


def q_percent_of_what(grade, tier):
    """'What percent is a of b?' — including percent increase / decrease."""
    if tier >= 3 and random.random() < 0.45:
        p = random.choice((10, 20, 25, 50))
        # The new price must come out whole, or the percentage printed in the
        # question would no longer match the price printed next to it.
        old = random.choice([v for v in (20000, 30000, 40000, 50000, 60000,
                                         80000, 100000, 120000)
                             if v * (100 + p) % 100 == 0
                             and v * (100 - p) % 100 == 0])
        up = random.random() < 0.5
        new = old * (100 + p) // 100 if up else old * (100 - p) // 100
        delta = abs(new - old)
        word = "qimmatlashdi" if up else "arzonlashdi"
        expl = (f"O'zgarish: {delta} so'm. Foiz HAR DOIM avvalgi narxdan "
                f"hisoblanadi: {delta} × 100 ÷ {old} = {p}%.")
        return _q("Foizlar",
                  f"Tovarning narxi {_fmt_money(old)} so'mdan "
                  f"{_fmt_money(new)} so'mga o'zgardi. Narx necha foizga "
                  f"{word}?",
                  p, [delta * 100 // new, 100 - p, delta, p * 2], expl,
                  fmt=lambda v: f"{v}%")

    p = random.choice(_PCT_ALL if tier >= 2 else _PCT_EASY)
    b = _pct_number(p, 2, 10)
    a = b * p // 100
    expl = (f"{a} ni {b} ga bo'lib, 100 ga ko'paytiramiz: "
            f"{a} ÷ {b} × 100 = {p}%.")
    return _q("Foizlar", f"{a} soni {b} sonining necha foizini tashkil qiladi?",
              p, [100 - p, b - a, p * 2, a], expl, fmt=lambda v: f"{v}%")


# ---------------------------------------------------------------------------
# Aralashmalar va eritmalar (mixtures: concentration changes)
# ---------------------------------------------------------------------------

# (mixture, the dissolved part, unit, masses to start from, amounts to add)
_MIXTURES = [
    ("tuzli eritma", "tuz",     "g", (200, 250, 300, 400, 500, 600), (50, 100, 150, 200, 250, 300, 400)),
    ("shakarli suv", "shakar",  "g", (200, 250, 300, 400, 500),      (50, 100, 150, 200, 250, 300)),
    ("limonad",      "sharbat", "l", (4, 5, 6, 8, 10, 12),           (1, 2, 3, 4, 5, 6, 8, 10)),
    ("bo'yoq",       "rang",    "l", (4, 5, 6, 8, 10),               (1, 2, 3, 4, 5, 6, 10)),
]


def _mixture_start():
    """A mixture whose 'p% of M' is a whole amount."""
    mix, sol, unit, masses, adds = random.choice(_MIXTURES)
    for _ in range(50):
        p = random.choice((10, 20, 25, 40, 50, 60, 75, 80))
        m = random.choice(masses)
        if m * p % 100 == 0:
            return mix, sol, unit, adds, m, p, m * p // 100
    return mix, sol, unit, adds, 200, 20, 40


def q_mixture(grade, tier):
    """Concentration problems: how much of the mixture is the dissolved part,
    and what happens to the percentage when you pour in more water (the part
    stays the same, the whole grows) or more of the substance."""
    mix, sol, unit, adds, m, p, part = _mixture_start()
    water = "suv"

    if tier == 1 or random.random() < 0.25:
        expl = (f"{m} {unit} ning {p}% i: {m} × {p} ÷ 100 = {part} {unit}.")
        return _q("Aralashmalar",
                  f"{m} {unit} {mix}ning {p}% i {sol}dan iborat. Unda necha "
                  f"{unit} {sol} bor?",
                  part, [m - part, part * 2, m * p // 10, part // 2], expl,
                  unit=unit)

    if random.random() < 0.5:
        # Pour in more water: the dissolved part does not change.
        cands = [(w, part * 100 // (m + w)) for w in adds
                 if part * 100 % (m + w) == 0 and 1 <= part * 100 // (m + w) < p]
        if cands:
            w, newp = random.choice(cands)
            total = m + w
            expl = (f"{sol.capitalize()} miqdori o'zgarmaydi: {m} × {p} ÷ 100 = {part} "
                    f"{unit}. Faqat umumiy massa ortadi: {m} + {w} = {total} "
                    f"{unit}. Yangi foiz: {part} × 100 ÷ {total} = {newp}%.")
            return _q("Aralashmalar",
                      f"{m} {unit} {mix}ning {p}% i {sol}. Unga yana {w} "
                      f"{unit} {water} qo'shildi. Endi {sol} aralashmaning "
                      f"necha foizini tashkil qiladi?",
                      newp, [p, p - w, part, newp * 2], expl,
                      fmt=lambda v: f"{v}%")

    # Pour in more of the substance: both the part and the whole grow.
    cands = [(s, (part + s) * 100 // (m + s)) for s in adds
             if (part + s) * 100 % (m + s) == 0 and p < (part + s) * 100 // (m + s) <= 100]
    if cands:
        s, newp = random.choice(cands)
        expl = (f"Yangi {sol} miqdori: {part} + {s} = {part + s} {unit}. "
                f"Bu safar {sol} ham, umumiy massa ham ortadi. "
                f"Yangi umumiy massa: {m} + {s} = {m + s} {unit}. "
                f"Yangi foiz: {part + s} × 100 ÷ {m + s} = {newp}%.")
        return _q("Aralashmalar",
                  f"{m} {unit} {mix}ning {p}% i {sol}. Unga yana {s} {unit} "
                  f"{sol} qo'shildi. Endi {sol} aralashmaning necha foizini "
                  f"tashkil qiladi?",
                  newp, [p + s, p, 100 - newp, newp + 10], expl,
                  fmt=lambda v: f"{v}%")

    expl = f"{m} {unit} ning {p}% i: {m} × {p} ÷ 100 = {part} {unit}."
    return _q("Aralashmalar",
              f"{m} {unit} {mix}ning {p}% i {sol}dan iborat. Unda necha "
              f"{unit} {sol} bor?",
              part, [m - part, part * 2, m * p // 10, part // 2], expl,
              unit=unit)


def q_percent_chain(grade, tier):
    """Two percentage changes one after the other — the trap is adding the two
    percentages together."""
    price = random.choice((20000, 30000, 40000, 50000, 60000, 80000, 100000))
    p, d = random.sample((10, 20, 25, 50), 2)
    mid = price * (100 + p) // 100
    final = mid * (100 - d) // 100
    naive = price * (100 + p - d) // 100
    expl = (f"Avval qimmatlashish: {_fmt_money(price)} × {100 + p} ÷ 100 = "
            f"{_fmt_money(mid)} so'm. Chegirma esa ESKI emas, YANGI narxdan "
            f"olinadi: {_fmt_money(mid)} × {100 - d} ÷ 100 = "
            f"{_fmt_money(final)} so'm. Shuning uchun {p}% va {d}% ni "
            f"shunchaki ayirib bo'lmaydi.")
    return _q("Foizlar",
              f"Tovarning narxi avval {p}% ga qimmatlashdi, keyin yangi "
              f"narxidan {d}% ga arzonlashdi. Tovarning oxirgi narxi qancha "
              f"bo'ldi? (Boshlang'ich narx {_fmt_money(price)} so'm)",
              final, [naive, price, mid, price * (100 - d) // 100], expl,
              lo=500, fmt=lambda v: f"{_fmt_money(v)} so'm")


# ---------------------------------------------------------------------------
# Tezlik — qiyinroq turlari (speed: average speed, units, trains)
# ---------------------------------------------------------------------------

# Pairs whose harmonic mean is a whole number — "half the way at v1, half at v2".
_HARMONIC_PAIRS = [(60, 40, 48), (30, 20, 24), (80, 20, 32), (60, 30, 40),
                   (20, 5, 8), (12, 4, 6), (10, 15, 12), (24, 8, 12),
                   (90, 45, 60), (100, 25, 40)]


def q_speed_average(grade, tier):
    """Average speed = total distance ÷ total time, never the average of the
    two speeds. Both versions here are built to expose that mistake."""
    if grade >= 7 and tier >= 3 and random.random() < 0.5:
        v1, v2, avg = random.choice(_HARMONIC_PAIRS)
        half = _lcm(v1, v2)
        s = 2 * half
        t1, t2 = half // v1, half // v2
        expl = (f"Yo'lning yarmi {half} km bo'lsin. Birinchi yarmi: "
                f"{half} ÷ {v1} = {t1} soat, ikkinchi yarmi: {half} ÷ {v2} = "
                f"{t2} soat. O'rtacha tezlik = butun masofa ÷ butun vaqt = "
                f"{s} ÷ {t1 + t2} = {avg} km/soat — tezliklarning o'rta "
                f"arifmetigi ({(v1 + v2) // 2}) EMAS!")
        return _q("O'rtacha tezlik",
                  f"Avtomobil yo'lning birinchi yarmini {v1} km/soat, "
                  f"ikkinchi yarmini esa {v2} km/soat tezlik bilan bosib "
                  f"o'tdi. Butun yo'ldagi o'rtacha tezligi qancha?",
                  avg, [(v1 + v2) // 2, v1, v2, avg + 5], expl, unit="km/soat")

    for _ in range(200):
        t1, t2 = random.randint(1, 4), random.randint(1, 4)
        v1 = random.randrange(20, 91, 10)
        v2 = random.randrange(20, 91, 10)
        s = v1 * t1 + v2 * t2
        if v1 != v2 and s % (t1 + t2) == 0 and (v1 + v2) % 2 == 0:
            avg = s // (t1 + t2)
            if avg != (v1 + v2) // 2:
                break
    else:
        v1, v2, t1, t2, s, avg = 60, 40, 1, 3, 180, 45

    name = _names()
    expl = (f"Butun masofa: {v1} × {t1} + {v2} × {t2} = {s} km. Butun vaqt: "
            f"{t1} + {t2} = {t1 + t2} soat. O'rtacha tezlik = {s} ÷ "
            f"{t1 + t2} = {avg} km/soat. Diqqat: bu tezliklarning o'rta "
            f"arifmetigi ({(v1 + v2) // 2}) emas!")
    return _q("O'rtacha tezlik",
              f"{name}ning otasi yo'lning birinchi qismini {v1} km/soat "
              f"tezlik bilan {t1} soat, qolgan qismini esa {v2} km/soat "
              f"tezlik bilan {t2} soat bosib o'tdi. Butun yo'ldagi o'rtacha "
              f"tezlik qancha?",
              avg, [(v1 + v2) // 2, s, avg + 10, avg - 10], expl, unit="km/soat")


def q_speed_units(grade, tier):
    """km/soat ↔ m/s — one of the most common exam slips."""
    kmh, ms = random.choice(((18, 5), (36, 10), (54, 15), (72, 20), (90, 25),
                             (108, 30), (144, 40), (180, 50)))
    if random.random() < 0.5:
        expl = (f"1 km/soat = 1000 m ÷ 3600 s, ya'ni km/soat ni m/s ga "
                f"aylantirish uchun 3,6 ga bo'linadi: {kmh} ÷ 3,6 = {ms} m/s.")
        return _q("Birliklar",
                  f"{kmh} km/soat tezlik necha m/s ga teng?",
                  ms, [kmh // 6, ms * 2, ms + 5, kmh // 2], expl, unit="m/s")
    expl = (f"m/s ni km/soat ga aylantirish uchun 3,6 ga ko'paytiriladi: "
            f"{ms} × 3,6 = {kmh} km/soat.")
    return _q("Birliklar",
              f"{ms} m/s tezlik necha km/soat ga teng?",
              kmh, [ms * 6, ms // 2 or 1, kmh + 10, ms * 10], expl, unit="km/soat")


def q_train(grade, tier):
    """A train has its own length — the classic 'bridge / tunnel / pole'
    problem where forgetting that length is the whole trap."""
    v = random.choice((10, 15, 20, 25, 30))
    lengths = [x for x in (100, 120, 150, 180, 200, 250, 300) if x % v == 0]
    L = random.choice(lengths) if lengths else v * random.randint(6, 12)

    if tier <= 2 and random.random() < 0.4:
        t = L // v
        expl = (f"Ustun yonidan o'tish uchun poyezd o'zining butun uzunligicha "
                f"yo'l bosishi kerak: {L} ÷ {v} = {t} s.")
        return _q("Poyezd masalasi",
                  f"Uzunligi {L} m bo'lgan poyezd {v} m/s tezlik bilan "
                  f"harakatlanmoqda. U yo'l chetidagi ustun yonidan necha "
                  f"sekundda butunlay o'tadi?",
                  t, [t + 2, t - 2, t * 2], expl, unit="s")

    obj, objname = random.choice((("ko'prik", "ko'prikdan"), ("tunnel", "tunneldan"),
                                  ("platforma", "platformadan")))
    cands = [b for b in range(200, 901, 50) if (L + b) % v == 0]
    B = random.choice(cands) if cands else v * 20 - L
    t = (L + B) // v
    expl = (f"Poyezd {objname} BUTUNLAY o'tishi uchun {obj} uzunligi + o'z "
            f"uzunligi = {B} + {L} = {B + L} m yo'l bosadi. Vaqt: "
            f"{B + L} ÷ {v} = {t} s. (Faqat {B} ÷ {v} deb hisoblash — eng "
            f"ko'p uchraydigan xato.)")
    return _q("Poyezd masalasi",
              f"Uzunligi {L} m bo'lgan poyezd {v} m/s tezlik bilan uzunligi "
              f"{B} m bo'lgan {obj}dan o'tmoqda. U {objname} butunlay o'tishi "
              f"uchun necha sekund kerak?",
              t, [B // v, L // v, t + 5, t - 5], expl, unit="s")


# ---------------------------------------------------------------------------
# Nisbat va proporsiya (ratio & proportion)
# ---------------------------------------------------------------------------

_RATIO_PAIRS = [(2, 3), (3, 4), (2, 5), (3, 5), (4, 5), (1, 3), (2, 7),
                (3, 7), (5, 6), (1, 4), (5, 7), (3, 8)]

_RATIO_STORIES = [
    ("konfet", "ta", "ikki bola o'rtasida"),
    ("olma", "ta", "ikki savatga"),
    ("so'm", "so'm", "ikki aka-uka o'rtasida"),
    ("kitob", "ta", "ikki javonga"),
]


def q_ratio(grade, tier):
    if tier >= 3 and random.random() < 0.35:
        a, b, c = random.choice([(1, 2, 3), (2, 3, 4), (1, 3, 5), (2, 3, 5),
                                 (1, 2, 4), (3, 4, 5)])
        k = random.randint(3, 12)
        total = (a + b + c) * k
        big = c * k
        expl = (f"Jami ulushlar soni: {a} + {b} + {c} = {a + b + c}. "
                f"Bitta ulush: {total} ÷ {a + b + c} = {k}. "
                f"Eng katta qism: {c} × {k} = {big}.")
        return _q("Nisbat",
                  f"{total} ta konfet uchta bolaga {a} : {b} : {c} nisbatda "
                  f"taqsimlandi. Eng ko'p konfet olgan bola nechta konfet oldi?",
                  big, [a * k, b * k, total // 3, big + k], expl)

    a, b = random.choice(_RATIO_PAIRS)
    k = random.randint(3, 15)
    total = (a + b) * k

    if random.random() < 0.45:
        # The small part is given; find the total.
        small = a * k
        expl = (f"Nisbatning kichik qismi {a} ulush = {small}, demak bitta "
                f"ulush = {small} ÷ {a} = {k}. Jami: ({a} + {b}) × {k} = {total}.")
        return _q("Nisbat",
                  f"Ikki son {a} : {b} nisbatda. Kichik son {small} ga teng "
                  f"bo'lsa, bu ikki sonning yig'indisi nechaga teng?",
                  total, [small + b, b * k, total - small, small * 2], expl)

    big = b * k
    expl = (f"Jami ulushlar soni: {a} + {b} = {a + b}. Bitta ulush: "
            f"{total} ÷ {a + b} = {k}. Katta qism: {b} × {k} = {big}.")
    return _q("Nisbat",
              f"{total} ta olma ikki savatga {a} : {b} nisbatda solindi. "
              f"Ko'proq olma solingan savatda nechta olma bor?",
              big, [a * k, total // 2, big - k, big + k], expl)


def q_proportion(grade, tier):
    """Direct and inverse proportion — and naming which is which is half the
    lesson."""
    if random.random() < 0.5:
        # Direct: more goods, more money.
        per = random.choice((1500, 2000, 2500, 3000, 4000, 5000))
        n = random.randint(2, 6)
        m = n + random.randint(1, 6)
        cost = n * per
        ans = m * per
        expl = (f"Bittasining narxi: {_fmt_money(cost)} ÷ {n} = "
                f"{_fmt_money(per)} so'm. {m} tasi: {m} × {_fmt_money(per)} = "
                f"{_fmt_money(ans)} so'm. Miqdor ortsa, narx ham ortadi — "
                f"to'g'ri proporsionallik.")
        return _q("Proporsiya",
                  f"{n} ta daftar {_fmt_money(cost)} so'm turadi. Xuddi "
                  f"shunday {m} ta daftar qancha turadi?",
                  ans, [cost + per, ans - per, ans + per, cost * 2], expl,
                  lo=500, fmt=lambda v: f"{_fmt_money(v)} so'm")

    # Inverse: more workers, fewer days.
    total_work = random.choice((24, 36, 48, 60, 72, 120))
    divs = [d for d in _divisors(total_work) if 2 <= d <= 20]
    w1, w2 = random.sample(divs, 2)
    d1, d2 = total_work // w1, total_work // w2
    expl = (f"Butun ish hajmi: {w1} × {d1} = {total_work} ishchi-kun. "
            f"{w2} ta ishchi uchun: {total_work} ÷ {w2} = {d2} kun. "
            f"Ishchilar soni ortsa, kunlar soni kamayadi — teskari "
            f"proporsionallik.")
    return _q("Proporsiya",
              f"{w1} ta ishchi bir ishni {d1} kunda bajaradi. Xuddi shu ishni "
              f"{w2} ta ishchi necha kunda bajaradi?",
              d2, [d1, d1 + w2, total_work // (w1 + w2) or 1, d2 + 1], expl,
              unit="kun")


# ---------------------------------------------------------------------------
# O'rta arifmetik (averages)
# ---------------------------------------------------------------------------

def q_average(grade, tier):
    roll = random.random()

    if roll < 0.3:
        n = random.choice((4, 5, 6))
        m = random.randint(5, 30)
        s = n * m
        expl = (f"O'rta arifmetik = yig'indi ÷ sonlar soni. Demak yig'indi = "
                f"o'rtacha × soni = {m} × {n} = {s}.")
        return _q("O'rta arifmetik",
                  f"{n} ta sonning o'rta arifmetigi {m} ga teng. Bu sonlarning "
                  f"yig'indisi nechaga teng?",
                  s, [m + n, s // 2, s + m, m * (n - 1)], expl)

    if roll < 0.6:
        a = random.randint(5, 25)
        b = random.randint(5, 25)
        m = random.randint(max(a, b) // 2 + 5, 30)
        third = 3 * m - a - b
        if third < 1:
            third, m = 1, (a + b + 1) // 3 or 1
        expl = (f"Uchta sonning yig'indisi: {m} × 3 = {3 * m}. Uchinchi son: "
                f"{3 * m} − {a} − {b} = {third}.")
        return _q("O'rta arifmetik",
                  f"Uchta sonning o'rta arifmetigi {m} ga teng. Ulardan "
                  f"ikkitasi {a} va {b} bo'lsa, uchinchi sonni toping.",
                  third, [m, 3 * m, third + a, abs(a + b - m)], expl)

    # A new value joins the set and moves the mean. Building x from the new
    # mean (instead of guessing one) keeps the division exact by construction.
    name = _names()
    n = random.choice((3, 4, 5))
    m = random.randint(6, 20)
    delta = random.choice((1, 2, 3))
    newm = m + delta
    x = newm * (n + 1) - n * m          # = m + delta × (n + 1)
    expl = (f"Avvalgi {n} ta o'yindagi ballar yig'indisi: {n} × {m} = {n * m}. "
            f"Oxirgi o'yin bilan: {n * m} + {x} = {n * m + x}. Yangi o'rtacha: "
            f"{n * m + x} ÷ {n + 1} = {newm}.")
    return _q("O'rta arifmetik",
              f"{name} birinchi {n} ta o'yinda o'rtacha {m} tadan ball to'pladi. "
              f"{n + 1}-o'yinda esa {x} ball to'pladi. Endi uning barcha "
              f"o'yinlaridagi o'rtacha bali nechaga teng?",
              newm, [m, x, (m + x) // 2, newm + 1], expl, unit="ball")


# ---------------------------------------------------------------------------
# Sonlar ketma-ketligi (sequences)
# ---------------------------------------------------------------------------

def q_sequence(grade, tier):
    kind = random.choice(('arith', 'geom', 'square', 'arith'))
    if tier >= 3:
        kind = random.choice(('arith_n', 'geom', 'square', 'rect', 'arith_n'))

    if kind == 'arith':
        a1 = random.randint(2, 15)
        d = random.randint(2, 9)
        seq = [a1 + i * d for i in range(4)]
        ans = a1 + 4 * d
        expl = (f"Har bir keyingi son avvalgisidan {d} ta ortib bormoqda "
                f"(arifmetik ketma-ketlik): {seq[-1]} + {d} = {ans}.")
    elif kind == 'geom':
        a1 = random.randint(1, 5)
        r = random.choice((2, 3))
        seq = [a1 * r ** i for i in range(4)]
        ans = a1 * r ** 4
        expl = (f"Har bir keyingi son avvalgisidan {r} marta katta "
                f"(geometrik ketma-ketlik): {seq[-1]} × {r} = {ans}.")
    elif kind == 'square':
        start = random.randint(1, 5)
        seq = [(start + i) ** 2 for i in range(4)]
        ans = (start + 4) ** 2
        expl = (f"Bular kvadratlar: {start}², {start + 1}², {start + 2}², "
                f"{start + 3}². Keyingisi {start + 4}² = {ans}.")
    elif kind == 'rect':
        start = random.randint(1, 4)
        seq = [(start + i) * (start + i + 1) for i in range(4)]
        ans = (start + 4) * (start + 5)
        expl = (f"Har bir had n × (n + 1) ko'rinishida: {start}×{start + 1}, "
                f"{start + 1}×{start + 2}, … Keyingisi: {start + 4} × "
                f"{start + 5} = {ans}.")
    else:  # arith_n — the n-th term, not the next one
        a1 = random.randint(2, 12)
        d = random.randint(2, 8)
        n = random.choice((10, 12, 15, 20, 25))
        ans = a1 + (n - 1) * d
        expl = (f"Arifmetik ketma-ketlikning n-hadi: aₙ = a₁ + (n − 1)·d = "
                f"{a1} + ({n} − 1) × {d} = {a1} + {(n - 1) * d} = {ans}.")
        return _q("Ketma-ketlik",
                  f"Arifmetik ketma-ketlikning birinchi hadi {a1}, ayirmasi "
                  f"{d} ga teng. Uning {n}-hadini toping.",
                  ans, [a1 + n * d, a1 * n, ans - d, ans + d], expl)

    shown = ", ".join(str(x) for x in seq)
    return _q("Ketma-ketlik",
              f"Ketma-ketlikni davom ettiring: {shown}, ...",
              ans, [ans + 1, ans - 1, seq[-1] * 2, ans + seq[0]], expl)


# ---------------------------------------------------------------------------
# To'plamlar (two overlapping groups — the classic Venn problem)
# ---------------------------------------------------------------------------

_VENN_PAIRS = [("futbol", "shaxmat"), ("ingliz tili", "koreys tili"),
               ("suzish", "yugurish"), ("rasm to'garagi", "musiqa to'garagi")]


def q_venn(grade, tier):
    act1, act2 = random.choice(_VENN_PAIRS)
    both = random.randint(2, 7)
    only1 = random.randint(3, 12)
    only2 = random.randint(3, 12)
    neither = random.randint(1, 8)
    a, b = only1 + both, only2 + both
    n = only1 + only2 + both + neither

    if random.random() < 0.5:
        expl = (f"Kamida bittasi bilan shug'ullanadiganlar: {a} + {b} − {both} = "
                f"{a + b - both} ta (ikkalasi bilan shug'ullanadiganlar ikki "
                f"marta sanalgani uchun ayiriladi). Qolganlari: {n} − "
                f"{a + b - both} = {neither} ta.")
        return _q("To'plamlar",
                  f"Sinfdagi {n} o'quvchidan {a} tasi {act1}ga, {b} tasi "
                  f"{act2}ga qatnaydi, {both} tasi esa ikkalasiga ham "
                  f"qatnaydi. Nechta o'quvchi ularning birortasiga ham "
                  f"qatnamaydi?",
                  neither, [n - a - b, both, only1, neither + both], expl)

    expl = (f"Faqat {act1}ga qatnaydiganlar = {act1}ga qatnaydiganlarning "
            f"hammasidan ikkalasiga qatnaydiganlarni ayiramiz: {a} − {both} = "
            f"{only1} ta.")
    return _q("To'plamlar",
              f"Sinfda {a} o'quvchi {act1}ga, {b} o'quvchi {act2}ga qatnaydi. "
              f"Ulardan {both} tasi ikkala to'garakka ham qatnaydi. Nechta "
              f"o'quvchi FAQAT {act1}ga qatnaydi?",
              only1, [a, only2, both, a + both], expl)


# ---------------------------------------------------------------------------
# Geometriya (perimeter, area, volume — beyond the simple rectangle)
# ---------------------------------------------------------------------------

def q_geometry(grade, tier):
    roll = random.random()

    if roll < 0.2:
        side = random.randint(3, 15)
        p = 4 * side
        expl = (f"Kvadratning tomoni: {p} ÷ 4 = {side} sm. "
                f"Yuzi: {side} × {side} = {side * side} sm².")
        return _q("Geometriya",
                  f"Kvadratning perimetri {p} sm ga teng. Uning yuzini toping.",
                  side * side, [p * p, side * 4, p * 2, side * side // 2], expl,
                  unit="sm²")

    if roll < 0.4:
        a = random.randint(4, 15)
        b = random.randint(2, a - 1)
        s = a * b
        p = 2 * (a + b)
        expl = (f"Eni: {s} ÷ {a} = {b} sm. Perimetr: 2 × ({a} + {b}) = {p} sm.")
        return _q("Geometriya",
                  f"To'g'ri to'rtburchakning yuzi {s} sm², bo'yi esa {a} sm. "
                  f"Uning perimetrini toping.",
                  p, [s + a, a + b, p * 2, s // 2], expl, unit="sm")

    if roll < 0.6:
        base = random.randint(3, 16)
        h = random.choice([x for x in range(2, 15) if base * x % 2 == 0])
        s = base * h // 2
        expl = (f"Uchburchakning yuzi = asos × balandlik ÷ 2 = {base} × {h} ÷ 2 "
                f"= {s} sm².")
        return _q("Geometriya",
                  f"Uchburchakning asosi {base} sm, shu asosga tushirilgan "
                  f"balandligi {h} sm. Uchburchakning yuzini toping.",
                  s, [base * h, base + h, s * 2, s // 2], expl, unit="sm²")

    if roll < 0.8:
        a = random.randint(2, 9)
        if random.random() < 0.5:
            v = a ** 3
            expl = f"Kubning hajmi = qirra³ = {a} × {a} × {a} = {v} sm³."
            return _q("Geometriya",
                      f"Kubning qirrasi {a} sm. Uning hajmini toping.",
                      v, [6 * a * a, a * a, a * 3, v + a], expl, unit="sm³")
        s = 6 * a * a
        expl = (f"Kubning 6 ta bir xil yog'i bor: to'la sirt = 6 × qirra² = "
                f"6 × {a}² = {s} sm².")
        return _q("Geometriya",
                  f"Kubning qirrasi {a} sm. Uning to'la sirtini toping.",
                  s, [a ** 3, a * a, 4 * a * a, s + a], expl, unit="sm²")

    # Scaling — a favourite 7th-grade trap.
    k = random.choice((2, 3, 4))
    expl = (f"Tomoni {k} marta ortsa, yuza {k} × {k} = {k * k} marta ortadi "
            f"(chunki yuza = tomon × tomon). Yuza {k} marta emas!")
    return _q("Geometriya",
              f"Kvadratning tomoni {k} marta uzaytirildi. Uning yuzi necha "
              f"marta ortadi?",
              k * k, [k, k * k * k, k + k, k * 2], expl, unit="marta")


# ---------------------------------------------------------------------------
# O'lchov birliklari (unit conversion)
# ---------------------------------------------------------------------------

def q_units(grade, tier):
    kind = random.choice(('mass', 'length', 'time', 'area', 'volume'))
    if kind == 'mass':
        t, kg = random.randint(2, 9), random.randint(1, 9) * 50
        ans = t * 1000 + kg
        expl = f"1 t = 1000 kg. {t} t = {t * 1000} kg, {t * 1000} + {kg} = {ans} kg."
        return _q("Birliklar", f"{t} t {kg} kg necha kilogrammga teng?",
                  ans, [t * 100 + kg, t + kg, t * 1000, ans + 100], expl, unit="kg")
    if kind == 'length':
        km, m = random.randint(2, 9), random.randint(1, 9) * 50
        ans = km * 1000 + m
        expl = f"1 km = 1000 m. {km} km = {km * 1000} m, {km * 1000} + {m} = {ans} m."
        return _q("Birliklar", f"{km} km {m} m necha metrga teng?",
                  ans, [km * 100 + m, km + m, km * 1000, ans + 100], expl, unit="m")
    if kind == 'time':
        h, mi = random.randint(2, 6), random.choice((5, 10, 15, 20, 25, 40, 45))
        ans = h * 60 + mi
        expl = f"1 soat = 60 daqiqa. {h} soat = {h * 60} daqiqa, {h * 60} + {mi} = {ans}."
        return _q("Birliklar", f"{h} soat {mi} daqiqa necha daqiqaga teng?",
                  ans, [h * 100 + mi, h + mi, h * 60, ans + 10], expl, unit="daqiqa")
    if kind == 'area':
        a = random.randint(2, 9)
        ans = a * 10000
        expl = (f"1 m² = 100 sm × 100 sm = 10 000 sm². Demak {a} m² = "
                f"{a} × 10 000 = {ans} sm². (100 emas — bu eng ko'p "
                f"uchraydigan xato!)")
        return _q("Birliklar", f"{a} m² necha sm² ga teng?",
                  ans, [a * 100, a * 1000, a * 100000, ans // 2], expl, unit="sm²")
    a = random.randint(2, 9)
    ans = a * 1000
    expl = f"1 m³ = 1000 l. Demak {a} m³ = {a} × 1000 = {ans} litr."
    return _q("Birliklar", f"{a} m³ suv necha litrga teng?",
              ans, [a * 100, a * 10000, a * 10, ans // 2], expl, unit="l")


# ---------------------------------------------------------------------------
# Raqamlar bilan masalalar (digit puzzles)
# ---------------------------------------------------------------------------

def q_digits(grade, tier):
    if random.random() < 0.5:
        t = random.randint(1, 6)
        u = t + random.randint(1, min(3, 9 - t))
        num, rev = 10 * t + u, 10 * u + t
        s, diff = t + u, rev - num
        expl = (f"O'nlar raqami t, birlar raqami b bo'lsin. t + b = {s}. "
                f"O'rni almashganda son 9 × (b − t) ga ortadi: 9 × (b − t) = "
                f"{diff}, demak b − t = {diff // 9}. Bundan t = {t}, b = {u} — "
                f"son {num}. Tekshiruv: {rev} − {num} = {diff}.")
        return _q("Raqamlar",
                  f"Ikki xonali sonning raqamlari yig'indisi {s} ga teng. "
                  f"Uning raqamlari o'rni almashtirilsa, hosil bo'lgan son "
                  f"berilgan sondan {diff} ga katta bo'ladi. Berilgan sonni "
                  f"toping.",
                  num, [rev, s * 10, num + 9, u * 10], expl)

    u = random.randint(1, 5)
    d = random.randint(1, min(4, 9 - u))
    t = u + d
    num = 10 * t + u
    s = t + u
    expl = (f"O'nlar raqami birlar raqamidan {d} ta katta, yig'indisi {s}. "
            f"Demak birlar raqami: ({s} − {d}) ÷ 2 = {u}, o'nlar raqami: "
            f"{u} + {d} = {t}. Son: {num}.")
    return _q("Raqamlar",
              f"Ikki xonali sonning o'nlar raqami birlar raqamidan {d} ta "
              f"katta, raqamlari yig'indisi esa {s} ga teng. Shu sonni toping.",
              num, [10 * u + t, s * 10, num + d, num - 9], expl)


# ---------------------------------------------------------------------------
# Topic registry — which generators play in which round (tier)
# ---------------------------------------------------------------------------

# Shared base pool for every grade…
_TIER_GENERATORS = {
    1: [q_divisibility, q_prime_pick, q_remainder, q_word_easy, q_speed_basic,
        q_num_divisors, q_sequence, q_units, q_average, q_ratio, q_geometry],
    2: [q_divisibility, q_ekub, q_ekuk, q_num_divisors, q_sum_divisors,
        q_common_divisors, q_speed_basic, q_word_mid, q_remainder,
        q_ekuk_meeting, q_ekub_sharing, q_money_compare, q_ratio, q_average,
        q_venn, q_sequence, q_geometry, q_proportion, q_units],
    3: [q_ekub, q_ekuk, q_num_divisors, q_sum_divisors, q_largest_prime,
        q_prime_pick, q_speed_hard, q_word_hard, q_common_divisors,
        q_divisibility, q_ekuk_meeting, q_ekub_sharing, q_work_compare,
        q_proportion, q_venn, q_sequence, q_geometry, q_average],
}

# …plus grade-exclusive topics, so 6th genuinely plays harder than 5th and
# 7th harder than 6th. Signature topics appear twice for extra weight.
_GRADE_EXTRAS = {
    5: {
        1: [q_sequence],
        2: [q_fraction_of, q_percent],
        3: [q_fraction_of, q_fraction_add, q_equation, q_percent_reverse],
    },
    6: {
        1: [q_integers, q_fraction_of, q_percent],
        2: [q_equation, q_equation, q_fraction_add, q_percent,
            q_fraction_compare, q_percent_reverse, q_percent_of_what,
            q_speed_units],
        3: [q_equation, q_equation, q_boat_wind, q_boat_wind, q_fraction_add,
            q_percent, q_percent_reverse, q_percent_of_what, q_mixture,
            q_speed_average, q_train, q_digits],
    },
    7: {
        1: [q_integers, q_fraction_of, q_power, q_percent, q_speed_units],
        2: [q_equation, q_square_diff, q_percent, q_fraction_add, q_boat_wind,
            q_power, q_percent_reverse, q_percent_of_what, q_mixture,
            q_speed_average, q_train, q_digits, q_proportion],
        3: [q_square_diff, q_square_diff, q_equation, q_equation, q_boat_wind,
            q_fraction_compare, q_percent, q_percent_reverse, q_mixture,
            q_mixture, q_percent_chain, q_percent_chain, q_speed_average,
            q_speed_average, q_train, q_digits, q_percent_of_what, q_sequence],
    },
}

def stage_tier(stage):
    """Championship round (1–3) for a 1-based stage number (1–15)."""
    return min(3, (stage - 1) // 5 + 1)


def generate_question(grade, stage, last_topic=None):
    """Generate a fresh question for this grade + stage, avoiding an
    immediate topic repeat when possible."""
    tier = stage_tier(stage)
    pool = _TIER_GENERATORS[tier] + _GRADE_EXTRAS.get(grade, {}).get(tier, [])
    for _ in range(10):
        gen = random.choice(pool)
        q = gen(grade, tier)
        if q['topic'] != last_topic:
            return q
    return q
