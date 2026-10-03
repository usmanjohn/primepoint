# STYLE GUIDE — GMAT Focus Edition mock exams (`exam` app)

Started **2026-10-02** at the user's request, after the GMAT course was complete
(Quant + Data Insights in `tutorial` "Prime GMAT", Verbal in `examprep` track `gmat`).
Read `STYLE_GUIDE_SAT_MOCK.md` §0 first — its first principle is this one's too:
**a mock measures, it does not teach.** No teaching inside a section; the Uzbek
explanation is shown only on the result page.

## 0. The language split
Every passage, stem and choice in **English**; every `explanation` in **Uzbek**
(ʻ/ʼ, never `'`); `skill` in English. No Uzbek anywhere inside a section. Numbers the
GMAT way: `3.5`, `1,200`, `$45`.

## 1. The shape (official, mba.com — checked 2026-10-02)
```
Quantitative Reasoning   21 questions   45 min   Problem Solving only, no calculator
Verbal Reasoning         23 questions   45 min   Critical Reasoning + Reading Comprehension
Data Insights            20 questions   45 min   DS, Table, Graphics, Two-Part, Multi-Source;
                                                 basic on-screen calculator
```
- The taker **chooses the section order** (6 orders) on the exam page.
- **One optional 10-minute break**, offered after section 1 and — if skipped — after
  section 2. The engine does this; modules carry `break_minutes = 0`.
- **Five choices** on every question (`load_mock` refuses anything else for `gmat`).
- Scores: 60–90 per section, 205–805 total ending in 5, sections weigh equally
  (`exam/gmatscore.py`). The real test is adaptive per question and GMAC does not
  publish the conversion, so every number is labelled an **estimate**. Never claim more.

One mock = three files, each repeating `EXAM_META` + all three `MODULES` unchanged:
```
exam/data/gmat<N>_quant.py    21      exam_number = 300 + N  (SAT owns 200+N, TOPIK 96/101–110)
exam/data/gmat<N>_verbal.py   23
exam/data/gmat<N>_di.py       20
```

## 2. Blueprints (ours — GMAC publishes no per-type counts)
- **Quant 21**: Number Properties 4 · Percents, Ratios and Rates 5 · Algebra 4 ·
  Word Problems 4 · Statistics and Counting 4. Rough difficulty curve: easy → hard
  across the section (the real test adapts; a fixed paper climbs instead).
- **Verbal 23**: Critical Reasoning 11 (questions 1–11) then Reading Comprehension 12
  (4 passages × 3). Skills: `CR — Structure and Assumptions`, `CR — Strengthen and Weaken`,
  `CR — Inference and Paradox`, `RC — Main Idea and Structure`, `RC — Detail`,
  `RC — Inference and Application`.
- **DI 20**: Data Sufficiency 7 · Table Analysis 3 · Graphics Interpretation 4 ·
  Two-Part Analysis 3 · Multi-Source Reasoning 3. DS questions always carry the five
  standard verdicts in the standard order (choices are not shuffled in `exam`).

## 3. Material is new
Never reuse a question, argument or passage from Prime GMAT (GMAT-1…35 and its
practices/readings) or the examprep `gmat` track — a mock made of what the pupil has
seen measures memory. RC passages are about real things and every fact in them is true;
`toc_gmat_mocks.txt` lists every subject used.

## 4. The answer gates (three scratchpad scripts per mock)
- `verify_gmat_mock<N>_quant.py` — recomputes every key **by a different route**
  (brute force over integers/`Fraction`s, enumeration for counting/probability); checks
  five distinct choices, the key among them, numeric choice lists sorted.
- `verify_gmat_mock<N>_di.py` — DS verdicts derived from world models (see Prime GMAT's
  `verify_gmat_26_30.py`); tables and charts parsed back out of the HTML and every
  table/graphics/two-part/MSR key recomputed from the parsed numbers.
- `verify_gmat_mock<N>_verbal.py` — the examprep defensibility gate adapted: one key,
  five distinct choices, explanation names the key's opening words, no letters, CR
  arguments 25–100 words, RC passages 200–350 words with three questions each.
**Key positions** (mock 1 lesson): the `exam` engine shows choices in FILE ORDER (that is
what keeps Data Sufficiency A–E). Mock 1's first Verbal draft had every key first, and its
Quant had no key at E because sorted numeric choices put the key where its value falls.
So: Verbal/CR/RC set the key position explicitly (`KEY_POS`), Quant picks distractors that
spread the keys, and every gate plus `GmatMockContentTests` refuses a letter that is never
the key, a letter used more than 6 times, or the same letter three times running.
Prove each gate bites, then re-read every stem by eye: **a question a careful reader can
defend two answers to is a bug.**

## 5. Load
```
python manage.py load_mock exam/data/gmat<N>_quant.py  --expect-questions=21
python manage.py load_mock exam/data/gmat<N>_verbal.py --expect-questions=23
python manage.py load_mock exam/data/gmat<N>_di.py     --expect-questions=20
```
Then mark the mock `[done]` in `toc_gmat_mocks.txt` and append the three lines to
`temporary.txt`. `exam/tests.py` `GmatMockContentTests` checks every shipped file's shape.
