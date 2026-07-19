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
           'Firdavs', "Ilg'or", 'Afsona', 'Madina', 'Charos']
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
# Topic registry — which generators play in which round (tier)
# ---------------------------------------------------------------------------

# Shared base pool for every grade…
_TIER_GENERATORS = {
    1: [q_divisibility, q_prime_pick, q_remainder, q_word_easy, q_speed_basic,
        q_num_divisors],
    2: [q_divisibility, q_ekub, q_ekuk, q_num_divisors, q_sum_divisors,
        q_common_divisors, q_speed_basic, q_word_mid, q_remainder,
        q_ekuk_meeting, q_ekub_sharing, q_money_compare],
    3: [q_ekub, q_ekuk, q_num_divisors, q_sum_divisors, q_largest_prime,
        q_prime_pick, q_speed_hard, q_word_hard, q_common_divisors,
        q_divisibility, q_ekuk_meeting, q_ekub_sharing, q_work_compare],
}

# …plus grade-exclusive topics, so 6th genuinely plays harder than 5th and
# 7th harder than 6th. Signature topics appear twice for extra weight.
_GRADE_EXTRAS = {
    5: {
        2: [q_fraction_of],
        3: [q_fraction_of, q_fraction_add, q_equation],
    },
    6: {
        1: [q_integers, q_fraction_of],
        2: [q_equation, q_equation, q_fraction_add, q_percent, q_fraction_compare],
        3: [q_equation, q_equation, q_boat_wind, q_boat_wind, q_fraction_add,
            q_percent],
    },
    7: {
        1: [q_integers, q_fraction_of, q_power],
        2: [q_equation, q_square_diff, q_percent, q_fraction_add, q_boat_wind,
            q_power],
        3: [q_square_diff, q_square_diff, q_equation, q_equation, q_boat_wind,
            q_fraction_compare, q_percent],
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
