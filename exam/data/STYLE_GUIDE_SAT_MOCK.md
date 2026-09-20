# STYLE GUIDE — Digital SAT mock exams (`exam` app)

This is the guide for a **mock test**, not a lesson. The difference decides
almost every question below it.

A lesson explains, then asks. A mock asks, and only explains afterwards. The
pupil sitting one of these is not here to learn a pattern — they are here to
find out what they would score on a Saturday morning, under a clock, with no
help. Everything that makes a lesson good (the aside, the Uzbek hint beside
the hard word, the worked example first) makes a mock **dishonest**.

Prime SAT Math (`tutorial`, `SAT-1…100`) and SAT R&W (`examprep`) teach.
These files measure. Keep the two jobs apart.

---

## 0. The language split

Inherited from Prime SAT Math and not negotiable:

| Where | Language |
|---|---|
| Every passage, stem and answer choice | **English** — this is the test |
| Every `explanation` | **Uzbek** — this is the teacher |
| `skill` (the domain label) | **English** — it is the College Board's own name |

The explanation is the only Uzbek a pupil sees, and they only see it after
they have finished. Inside a module there is **no Uzbek at all**: not a gloss,
not a hint, not a bracket. A word they do not know is part of the measurement.

Numbers use the SAT's own convention — `3.5` and `1,200`, decimal point and
comma thousands. The opposite of Prime Math's `3,5`.

---

## 1. The shape of one mock

```
Reading and Writing — Module 1      27 questions   32 min   everyone
        ↓  ≥ route_threshold correct → upper,  else lower
Reading and Writing — Module 2      27 questions   32 min   one of two
        ↓  BREAK 10 min
Math — Module 1                     22 questions   35 min   everyone
        ↓  ≥ route_threshold correct → upper,  else lower
Math — Module 2                     22 questions   35 min   one of two
```

98 questions **seen**, 147 questions **written** — the two module-2 branches
both have to exist for the routing to mean anything.

Six data files per mock, one per module:

```
exam/data/sat<N>_rw1.py          27
exam/data/sat<N>_rw2_easy.py     27
exam/data/sat<N>_rw2_hard.py     27
exam/data/sat<N>_math1.py        22
exam/data/sat<N>_math2_easy.py   22
exam/data/sat<N>_math2_hard.py   22
```

Every file repeats `EXAM_META` and `MODULES` unchanged — copy them from the
previous file of the same mock. The loader `update_or_create`s both, so the
order the six files are loaded in does not matter.

---

## 2. What goes in each module

### Reading and Writing — 27 questions, in the test's own order

| # | Domain (`skill`) | Count |
|---|---|---|
| 1–4 | Words in Context | 4 |
| 5–6 | Text Structure and Purpose | 2 |
| 7 | Cross-Text Connections | 1 |
| 8–9 | Central Ideas and Details | 2 |
| 10–12 | Command of Evidence | 3 (one from a table or graph) |
| 13–14 | Inferences | 2 |
| 15–17 | Boundaries | 3 |
| 18–21 | Form, Structure, and Sense | 4 |
| 22–24 | Transitions | 3 |
| 25–27 | Rhetorical Synthesis | 3 |

Bluebook groups by domain and goes roughly easy→hard inside each group. Keep
that order: a pupil who has practised on the real thing will notice if the
grammar questions are scattered.

**One passage, one question.** Never two questions on the same text — that is
the old paper SAT. Each passage is **25–150 words** and lives in the
question's own `passage` key.

### Math — 22 questions, 35 minutes

| # | Domain (`skill`) | Count |
|---|---|---|
| — | Algebra | 8 |
| — | Advanced Math | 7 |
| — | Problem-Solving and Data Analysis | 4 |
| — | Geometry and Trigonometry | 3 |

Ordered easy→hard across the whole module, not grouped by domain — that is
how the real Math module runs.

**Questions 18–22 are grid-ins** (`answer_type: 'grid'`), which is the real
test's ~23%. They come at the end of the module, exactly as in Bluebook.

Maths is **HTML, never LaTeX** (`x<sup>2</sup>`, × ÷ √ ≤ ≥ π °). Figures are
**inline SVG**, never an uploaded image. Both rules are inherited from Prime
Math and Prime SAT Math, and the `pm-*`/`ps-*` CSS is *not* loaded on the exam
page — a figure here has to carry its own inline styles.

---

## 3. The difference between the two module 2s

This is the part that is easy to get wrong, because "harder" does not mean
"nastier".

The **lower** module tests whether the pupil can do the ordinary thing:
one step, familiar wording, numbers that come out whole, a passage whose main
idea is in its first sentence. A pupil who belongs in this module should be
able to finish it and get most of it right — that is what makes the score
underneath it trustworthy.

The **upper** module tests whether they can do the ordinary thing *when it is
disguised*: two steps instead of one, an unfamiliar context for a familiar
equation, a passage whose point is made by its last clause. The vocabulary is
harder, the syntax is longer, the traps are better.

What must **not** change between them: the domains, their counts, and the
order. Both are complete SAT modules. The lower one is not a shorter or
gentler test — it is the same test, lower down.

---

## 4. Writing an explanation

Every question carries one, in Uzbek, and it is the only teaching in the whole
file. Three sentences is usually right:

1. **why the key is right** — name the evidence, quote the words;
2. **why the tempting wrong one is wrong** — name it by its **opening text**,
   never by a letter;
3. for maths, the arithmetic, written out.

> `'explanation'`: `'Toʻgʻri javob <strong>undermine</strong>. Matn "the data '
> `'contradicted his earlier claim" deydi — yaʼni dalil fikrni zaiflashtiradi. '`
> `'<strong>reinforce</strong> teskari maʼno beradi va aynan shuning uchun '`
> `'chalgʻituvchi: talaba "contradicted" soʻzini oʻqimay, mavzuni umumiy '`
> `'tushunib tanlaydi.'`

**⛔ Never write "Choice A", "(B)", "variant C" or a position.** The exam page
renders choices in the order they were authored, but the result page, the
print sheet and any future shuffle do not owe you that order — and the habit
has already shipped a broken lesson once in this project. Quote the choice's
own opening words inside `<strong>`.

**⛔ Never explain a question inside the module.** The `explanation` field is
shown only on the result page. Nothing in `passage` or `question_text` hints.

---

## 5. THE ANSWER GATE

Two answer gates apply here, the arithmetic one from Prime Math and the
defensibility one from SAT R&W, and a mock needs both because there is no
teacher standing beside the pupil to say "ah, that one was badly worded".

Before importing a batch, write a throwaway `verify_sat_mock<N>_<module>.py`
in the scratchpad that checks:

**Mechanical (script):**
- exactly 4 choices, exactly one key, no two choices equal;
- numeric choice lists sorted;
- every grid-in `accepted` value parses through `exam.gridin.parse`, and the
  first one is the answer a pupil would most naturally type;
- every question has a non-empty `explanation` and a `skill` from the table
  in §2, with the counts in §2 matching;
- no choice letter anywhere in any explanation;
- no Uzbek inside `passage` or `question_text` (the module is English-only);
- passages between 25 and 150 words;
- balanced `<div>`, `<svg>`, `<sup>`; no `<script>`, no `style=` on a passage;
- every maths answer **recomputed by a different route** — brute force over
  `Fraction`s, or a numeric fingerprint at three sample points. Never by
  re-reading your own working.

**By eye (you, afterwards):**
- re-read every English stem and argue for each distractor. If a careful
  reader can defend a second answer, the question is **a bug**, not a hard
  question;
- check the grid-in keys are things a pupil would actually type. If the
  answer is `0.6666…`, `accepted` must carry the fraction and the truncated
  and rounded decimals.

Run, fix, then import.

---

## 6. Loading a mock

```
python manage.py load_mock exam/data/sat1_rw1.py        --expect-questions=27
python manage.py load_mock exam/data/sat1_rw2_easy.py   --expect-questions=27
python manage.py load_mock exam/data/sat1_rw2_hard.py   --expect-questions=27
python manage.py load_mock exam/data/sat1_math1.py      --expect-questions=22
python manage.py load_mock exam/data/sat1_math2_easy.py --expect-questions=22
python manage.py load_mock exam/data/sat1_math2_hard.py --expect-questions=22
```

`--expect-questions` is not optional. A file that silently loses a question
produces a mock that still runs, still scores, and is quietly wrong.

The loader refuses, before writing anything: a question without an
explanation, a grid-in without an accepted answer, a grid-in whose accepted
answer is not a legal entry, two identical choices, a `correct` outside 1–4,
a duplicate question number, and a choice letter inside an explanation.

Then give the six `railway run python manage.py load_mock …` lines — the user
runs them after pushing. Always, without being asked.

---

## 7. Scoring — and why the route is shown

`exam/satscore.py` converts raw correct (0–54 RW, 0–44 Math) into 200–800 by
two curves per section: one for a taker who reached the upper module 2, one
for a taker who did not. The lower route cannot pass about 600.

That ceiling is the single most useful thing on the score report, so the
report says it out loud rather than hiding it: two pupils with the same number
of correct answers can finish on different scores, and the way up is module 1.

The curves are an approximation of the published tables for the released
digital practice tests. College Board equates every real form separately and
publishes no formula, so the report calls the number a band, not a promise.
Do not quietly "improve" a curve to make a score look kinder.

---

## 8. What a mock is not

- not a lesson — no teaching inside a module, ever;
- not the `examprep` SAT track (93 lessons, practice questions, explanations
  as you go) and not Prime SAT Math (`tutorial`, `SAT-1…100`);
- not reused content. A mock made of questions the pupil has already met in a
  lesson measures their memory, not their reading. Write fresh passages and
  fresh numbers for every mock;
- not a place for a `cn-word` gloss, a `pe-*` component or a `ps-*` card. The
  exam page loads none of that CSS. A question here is plain HTML plus, for
  maths, inline SVG.
