"""Chempionat va duel savol generatorlari uchun regressiya testlari.

Ikki narsani qo'riqlaydi:

* **Shakl** — har bir savolda roppa-rosa 4 ta har xil variant, to'g'ri
  javobning indeksi joyida, matn va izoh bo'sh emas. Bitta noto'g'ri
  distraktor ("javob variantlar orasida ikki marta") o'yinni buzadi.
* **Javob** — bir nechta yangi generatorning javobi mustaqil yo'l bilan
  (sanab chiqish, kalendar, brute force) qayta hisoblanadi. To'liq tekshiruv
  scratchpad'dagi `verify_math_new.py` da, bu yerda esa eng qaltis
  joylarining doimiy nazorati turadi.
"""
import datetime
import itertools
import re
from fractions import Fraction

from django.test import TestCase
from django.urls import reverse

from . import duel, englishchamp, mathchamp


NEW_MATH = ['q_calendar', 'q_clock_angle', 'q_offbyone', 'q_combinatorics',
            'q_probability', 'q_age', 'q_find_error', 'q_true_statement',
            'q_odd_one_out', 'q_estimate', 'q_table', 'q_pyramid', 'q_magic',
            'q_riddle', 'q_pattern', 'q_temperature', 'q_scale', 'q_timetable']

NEW_ENGLISH = ['q_mini_reading', 'q_dialogue', 'q_sign', 'q_translate',
               'q_word_order', 'q_confusable', 'q_spelling', 'q_sound',
               'q_synonym', 'q_tag', 'q_so_neither', 'q_idiom',
               'q_time_english', 'q_date_ordinal', 'q_nationality',
               'q_measure', 'q_register', 'q_punctuation']


class QuestionShapeTests(TestCase):
    """Har bir generator ishlaydigan savol qaytaradimi."""

    def _assert_well_formed(self, q, where):
        self.assertEqual(len(q['choices']), 4, where)
        self.assertEqual(len(set(q['choices'])), 4, f'{where}: {q["choices"]}')
        self.assertIn(q['correct'], range(4), where)
        for key in ('topic', 'text', 'explanation'):
            self.assertTrue(str(q[key]).strip(), f'{where}: bo\'sh {key}')

    def test_every_math_generator(self):
        for name in NEW_MATH:
            gen = getattr(mathchamp, name)
            for grade in (5, 6, 7):
                for tier in (1, 2, 3):
                    for _ in range(40):
                        self._assert_well_formed(gen(grade, tier),
                                                 f'{name}/{grade}/{tier}')

    def test_every_english_generator(self):
        for name in NEW_ENGLISH:
            gen = getattr(englishchamp, name)
            for level in englishchamp.LEVELS:
                for tier in (1, 2, 3):
                    for _ in range(40):
                        self._assert_well_formed(gen(level, tier),
                                                 f'{name}/{level}/{tier}')

    def test_whole_pools(self):
        for grade in (5, 6, 7):
            for stage in range(1, 16):
                for _ in range(30):
                    self._assert_well_formed(
                        mathchamp.generate_question(grade, stage),
                        f'math/{grade}/{stage}')
        for level in englishchamp.LEVELS:
            for stage in range(1, 16):
                for _ in range(30):
                    self._assert_well_formed(
                        englishchamp.generate_question(level, stage),
                        f'english/{level}/{stage}')


class AnswerGateTests(TestCase):
    """Javoblarni boshqa yo'l bilan qayta hisoblab tekshiramiz."""

    WEEKDAYS = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma',
                'shanba', 'yakshanba']

    def answer(self, q):
        return q['choices'][q['correct']]

    def number(self, q):
        return int(re.search(r'-?\d+', self.answer(q).replace('−', '-')).group())

    def test_calendar_matches_a_real_calendar(self):
        for _ in range(200):
            q = mathchamp.q_calendar(6, 2)
            m = re.match(r"Bugun (\w+)\. (\d+) kundan keyin", q['text'])
            if not m:
                continue
            day, n = m.group(1), int(m.group(2))
            base = next(d for d in (datetime.date(2026, 3, 1)
                                    + datetime.timedelta(days=i)
                                    for i in range(7))
                        if self.WEEKDAYS[d.weekday()] == day)
            want = self.WEEKDAYS[(base + datetime.timedelta(days=n)).weekday()]
            self.assertEqual(self.answer(q), want, q['text'])

    def test_handshakes_match_enumeration(self):
        for _ in range(300):
            q = mathchamp.q_combinatorics(7, 2)
            m = re.search(r"Xonada (\d+) ta o'quvchi", q['text'])
            if not m:
                continue
            n = int(m.group(1))
            want = len(list(itertools.combinations(range(n), 2)))
            self.assertEqual(self.number(q), want, q['text'])

    def test_riddle_has_exactly_one_solution(self):
        for _ in range(200):
            q = mathchamp.q_riddle(6, 2)
            a, b, c, res = map(int, re.search(
                r"shu sonni (\d+) ga ko'paytirdi, natijaga (\d+) ni qo'shdi, "
                r"hosil bo'lgan sonni (\d+) ga bo'ldi va (\d+) ni oldi",
                q['text']).groups())
            sols = [x for x in range(-200, 1000)
                    if Fraction(x * a + b, c) == res]
            self.assertEqual(sols, [self.number(q)], q['text'])

    def test_magic_square_has_exactly_one_solution(self):
        for _ in range(100):
            q = mathchamp.q_magic(7, 3)
            rows = [l.split() for l in q['text'].split('\n')
                    if re.match(r'^\s*(\?|\d+)(\s+(\?|\d+)){2}\s*$', l)]
            self.assertEqual(len(rows), 3, q['text'])
            sols = []
            for x in range(1, 300):
                g = [[x if c == '?' else int(c) for c in row] for row in rows]
                sums = ([sum(r) for r in g] + [sum(c) for c in zip(*g)]
                        + [g[0][0] + g[1][1] + g[2][2],
                           g[0][2] + g[1][1] + g[2][0]])
                if len(set(sums)) == 1:
                    sols.append(x)
            self.assertEqual(sols, [self.number(q)], q['text'])

    def test_exactly_one_statement_is_true(self):
        """`q_true_statement` da faqat bitta rost gap bo'lishi shart."""
        def truth(s):
            fixed = {t: v for t, v, _ in mathchamp._PARITY_RULES}
            if s in fixed:
                return fixed[s]
            m = re.match(r"^(\d+) soni (\d+) ga qoldiqsiz bo'linadi$", s)
            if m:
                n, d = map(int, m.groups()); return n % d == 0
            m = re.match(r"^(\d+) — tub son$", s)
            if m:
                n = int(m.group(1))
                return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
            m = re.match(r"^(\d+)/(\d+) kasri (\d+)/(\d+) kasridan katta$", s)
            if m:
                a, b, c, d = map(int, m.groups())
                return Fraction(a, b) > Fraction(c, d)
            m = re.match(r"^−(\d+) soni −(\d+) sonidan katta$", s)
            if m:
                a, b = map(int, m.groups()); return -a > -b
            m = re.match(r"^(\d+) sonining (\d+)% i (\d+) ga teng$", s)
            if m:
                n, p, v = map(int, m.groups())
                return Fraction(n * p, 100) == v
            m = re.match(r"^(\d+) — biror natural sonning kvadrati$", s)
            if m:
                n = int(m.group(1))
                return any(k * k == n for k in range(1, n + 1))
            self.fail(f'tanilmagan tasdiq: {s!r}')
        for _ in range(200):
            q = mathchamp.q_true_statement(6, 2)
            truths = [truth(c) for c in q['choices']]
            self.assertEqual(truths.count(True), 1, q['choices'])
            self.assertTrue(truths[q['correct']], q['choices'])

    def test_odd_one_out_intruder_is_unique(self):
        for _ in range(300):
            q = mathchamp.q_odd_one_out(6, 2)
            vals = [int(c) for c in q['choices']]
            t = q['text']
            if 'TUB SON EMAS' in t:
                prop = lambda n: n > 1 and all(n % d
                                               for d in range(2, int(n ** .5) + 1))
            elif 'KVADRATI EMAS' in t:
                prop = lambda n: any(k * k == n for k in range(1, n + 1))
            elif "BO'LINMAYDI" in t:
                d = int(re.search(r"qaysi biri (\d+) ga", t).group(1))
                prop = lambda n: n % d == 0
            else:
                b = int(re.search(r"qaysi biri (\d+) ning", t).group(1))
                pows = {b ** k for k in range(1, 12)}
                prop = lambda n: n in pows
            self.assertEqual([prop(v) for v in vals].count(False), 1, t)
            self.assertFalse(prop(int(self.answer(q))), t)


class TopicRotationTests(TestCase):
    """Bir mavzu tez qaytmasligi — o'yin zerikarli bo'lib qolmasligi uchun."""

    def test_engines_avoid_the_remembered_topics(self):
        for _ in range(300):
            recent = ['Kalendar', 'Ehtimollik', 'Geometriya', 'Kasrlar']
            self.assertNotIn(
                mathchamp.generate_question(6, 8, recent)['topic'], recent)
            recent_en = ['Muloqot', 'Imlo', 'Tarjima', 'So\'z tartibi']
            self.assertNotIn(
                englishchamp.generate_question('a2', 8, recent_en)['topic'],
                recent_en)

    def test_a_whole_duel_never_repeats_a_topic_within_the_memory(self):
        for _ in range(60):
            plan = duel.build_plan(duel.MODE_DUEL,
                                   [duel.SUBJECT_BOTH, duel.SUBJECT_BOTH])
            seen = {}
            for stage in range(1, duel.STAGES + 1):
                subject = plan[stage - 1]['subject']
                memory = seen.get(subject, [])
                q = duel.make_question(subject, 6, 'a2',
                                       duel.stage_tier(stage), memory)
                self.assertNotIn(q['topic'], memory)
                seen[subject] = (memory + [q['topic']])[-4:]


class DuelPageTests(TestCase):
    """Duel sahifasi yangi savollar bilan ham ochilishi kerak."""

    def test_a_duel_can_be_started_and_answered(self):
        start = self.client.post(reverse('duel_home'), {
            'action': 'start', 'mode': duel.MODE_DUEL,
            'grade': 6, 'level': 'a2',
            'name_a': 'Afsona', 'name_b': 'Jasur',
            'subject_a': duel.SUBJECT_BOTH, 'subject_b': duel.SUBJECT_BOTH,
        })
        self.assertRedirects(start, reverse('duel_play'))
        for _ in range(6):
            page = self.client.get(reverse('duel_play'))
            self.assertEqual(page.status_code, 200)
            self.client.post(reverse('duel_play'),
                             {'action': 'answer', 'choice': '0'})
