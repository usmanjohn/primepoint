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


# ---------------------------------------------------------------------------
# Choice assembly
# ---------------------------------------------------------------------------

def _pad_wrongs(correct, wrongs, lo=1):
    """Return exactly 3 unique wrong values ≠ correct (all ≥ lo)."""
    out = []
    for w in wrongs:
        if w != correct and w not in out and w >= lo:
            out.append(w)
        if len(out) == 3:
            return out
    delta = 1
    while len(out) < 3:
        for cand in (correct + delta, correct - delta):
            if cand != correct and cand not in out and cand >= lo:
                out.append(cand)
                if len(out) == 3:
                    break
        delta += 1
    return out[:3]


def _q(topic, text, correct, wrongs, explanation, unit='', lo=1, pad=True):
    """Build the final question dict from a correct value + wrong values."""
    if pad:
        wrongs = _pad_wrongs(correct, wrongs, lo=lo)
    else:
        wrongs = [w for w in dict.fromkeys(wrongs) if w != correct][:3]

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

_VEHICLES = [
    ("Piyoda", 4, 6),
    ("Velosipedchi", 10, 18),
    ("Avtobus", 40, 60),
    ("Avtomobil", 60, 90),
    ("Poyezd", 50, 80),
    ("Motorli qayiq", 15, 25),
]


def _pick_vehicle(tier):
    name, lo, hi = random.choice(_VEHICLES)
    v = random.randint(lo, hi)
    if v > 20:
        v = round(v / 5) * 5
    t = random.randint(2, 4 if tier == 1 else 6)
    return name, v, t


def q_speed_basic(grade, tier):
    name, v, t = _pick_vehicle(tier)
    s = v * t
    kind = random.choice(('dist', 'speed', 'time'))
    if kind == 'dist':
        expl = f"Masofa = tezlik × vaqt = {v} × {t} = {s} km."
        return _q("Tezlik va masofa",
                  f"{name} {v} km/soat tezlik bilan {t} soat yurdi. "
                  f"U qancha masofa bosib o'tgan?",
                  s, [v * (t + 1), v * (t - 1), s + v // 2 or s + 1, v + t], expl, unit="km")
    if kind == 'speed':
        expl = f"Tezlik = masofa ÷ vaqt = {s} ÷ {t} = {v} km/soat."
        return _q("Tezlik va masofa",
                  f"{name} {s} km masofani {t} soatda bosib o'tdi. "
                  f"Uning tezligini toping.",
                  v, [v + 5, v - 5, v + 10, s - t], expl, unit="km/soat")
    expl = f"Vaqt = masofa ÷ tezlik = {s} ÷ {v} = {t} soat."
    return _q("Tezlik va masofa",
              f"{name} {s} km masofani {v} km/soat tezlik bilan bosib o'tdi. "
              f"Bunga qancha vaqt ketgan?",
              t, [t + 1, t - 1, t + 2], expl, unit="soat")


def q_speed_hard(grade, tier):
    if random.random() < 0.5:
        # Two vehicles moving towards each other.
        v1 = random.randint(9, 18) * 5
        v2 = random.randint(6, 12) * 5
        t = random.randint(2, 4)
        s = (v1 + v2) * t
        expl = (f"Yaqinlashish tezligi: {v1} + {v2} = {v1 + v2} km/soat. "
                f"Vaqt = {s} ÷ {v1 + v2} = {t} soat.")
        return _q("Tezlik va masofa",
                  f"Ikki shahar orasidagi masofa {s} km. Ikki avtomobil bir "
                  f"vaqtda bir-biriga qarab yo'lga chiqdi. Ularning tezliklari "
                  f"{v1} km/soat va {v2} km/soat. Ular necha soatdan keyin "
                  f"uchrashadi?",
                  t, [t + 1, t - 1, t + 2], expl, unit="soat")
    # Catch-up problem.
    v1 = random.randint(2, 5) * 5
    v2 = v1 + random.choice((5, 10, 15))
    t = random.randint(2, 4)
    gap = (v2 - v1) * t
    expl = (f"Tezliklar farqi: {v2} − {v1} = {v2 - v1} km/soat. "
            f"Quvib yetish vaqti = {gap} ÷ {v2 - v1} = {t} soat.")
    return _q("Tezlik va masofa",
              f"Velosipedchi {v1} km/soat tezlik bilan yo'lga chiqdi. Undan "
              f"{gap} km orqada turgan avtomobil {v2} km/soat tezlik bilan "
              f"uni quvib ketdi. Avtomobil velosipedchini necha soatda quvib "
              f"yetadi?",
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
        a = random.randint(6, 12)
        k = random.choice((3, 4, 5))
        father = k * a
        expl = f"Otaning yoshi: {a} × {k} = {father} yosh."
        return _q("Matnli masala",
                  f"Otaning yoshi o'g'lining yoshidan {k} marta katta. O'g'li "
                  f"{a} yoshda bo'lsa, ota necha yoshda?",
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
    per = random.randint(3, 9)
    k = random.randint(4, 8)
    n = per * k
    expl = f"Har bir bolaga: {n} ÷ {k} = {per} tadan konfet tegadi."
    return _q("Matnli masala",
              f"{n} ta konfet {k} nafar bolaga teng bo'lib tarqatildi. Har "
              f"bir bolaga nechtadan konfet tegdi?",
              per, [per + 1, per - 1, per + 2], expl)


def q_word_mid(grade, tier):
    if random.random() < 0.5:
        # Sum & difference.
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
    # Shopping.
    p = random.choice((2000, 2500, 3000, 3500, 4000))
    q = random.choice((1000, 1500, 2000, 2500))
    n = random.randint(2, 5)
    m = random.randint(2, 5)
    total = n * p + m * q
    expl = (f"Daftarlar: {n} × {_fmt_money(p)} = {_fmt_money(n * p)} so'm. "
            f"Ruchkalar: {m} × {_fmt_money(q)} = {_fmt_money(m * q)} so'm. "
            f"Jami: {_fmt_money(total)} so'm.")
    wrongs = [total + q, total - q, total + p, n * p + q]
    wrongs = _pad_wrongs(total, wrongs, lo=500)
    options = [(f"{_fmt_money(total)} so'm", True)] + \
              [(f"{_fmt_money(w)} so'm", False) for w in wrongs]
    random.shuffle(options)
    return {
        'topic': "Matnli masala",
        'text': (f"Bitta daftar {_fmt_money(p)} so'm, bitta ruchka "
                 f"{_fmt_money(q)} so'm turadi. {n} ta daftar va {m} ta "
                 f"ruchka uchun qancha pul to'lash kerak?"),
        'choices': [o[0] for o in options],
        'correct': next(i for i, o in enumerate(options) if o[1]),
        'explanation': expl,
    }


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
# Topic registry — which generators play in which round (tier)
# ---------------------------------------------------------------------------

_TIER_GENERATORS = {
    1: [q_divisibility, q_prime_pick, q_remainder, q_word_easy, q_speed_basic,
        q_num_divisors],
    2: [q_divisibility, q_ekub, q_ekuk, q_num_divisors, q_sum_divisors,
        q_common_divisors, q_speed_basic, q_word_mid, q_remainder],
    3: [q_ekub, q_ekuk, q_num_divisors, q_sum_divisors, q_largest_prime,
        q_prime_pick, q_speed_hard, q_word_hard, q_common_divisors,
        q_divisibility],
}


def stage_tier(stage):
    """Championship round (1–3) for a 1-based stage number (1–12)."""
    return min(3, (stage - 1) // 4 + 1)


def generate_question(grade, stage, last_topic=None):
    """Generate a fresh question for this grade + stage, avoiding an
    immediate topic repeat when possible."""
    tier = stage_tier(stage)
    for _ in range(10):
        gen = random.choice(_TIER_GENERATORS[tier])
        q = gen(grade, tier)
        if q['topic'] != last_topic:
            return q
    return q
