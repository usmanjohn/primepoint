# Prime SAT Practices — Writing Guide (for Claude)

How to write the **Prime SAT Math practice tests** — one test per lesson, `SAT-1 … SAT-100`,
matched **one-to-one** to the tutorials. The lesson list lives in `toc_ps_practices.txt`;
the tutorials' own guide is `tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md`.

> Same pupil as the tutorials: an **Uzbek pupil, 15–18**, sitting the digital SAT. The test
> is not a trap — it is the lesson's last page. A pupil who actually read `SAT-n` should
> score 70–90% on practice `n`. But it must *feel* like the SAT: English sentences, four
> choices, and distractors that punish the exact mistake the lesson warned about.

---

## 0. The language rule (inherited, and it is the point)

**Questions in English, explanations in Uzbek.** No exceptions.

- `text` — the exam question, in natural English, exactly as the SAT would print it.
  Variables italicised (`<i>x</i>`), figures inline SVG, no Uzbek inside it.
- `choices` — English / numbers only. Never a mixed-language option list.
- `explanation` — **entirely Uzbek**, starting with the key, then the reasoning, then the
  named mistake behind the tempting wrong choice.
- `hint` (optional) — Uzbek, one line, never gives the answer.

Numbers follow the SAT's own convention: **`3.5`, `1,200`, `$45`** — decimal point, comma
thousands. (Prime Math does the opposite; do not import that habit here.)

## 1. Title, file, import

- Title: `SAT-7 Practice: Slope-Intercept Form (y = mx + b) in Depth` — same number and same
  topic wording as the tutorial (drop the tutorial's colon, insert `Practice:`). **English**
  — `Practice`, not `Mashq`; this is the one Prime course whose practice titles are English,
  because its lesson titles are.
- Every practice carries `"tutorial": "SAT-7:"` — the importer matches that prefix and adds
  the practice to the tutorial's `practices` set, so the lesson page grows a Practice button.
  Never write the whole title there.
- Subject: **`Math`** — the practice Subject that **already exists** (Telegram's daily quiz
  reads it as *"Matematika (SAT)"*, `telegrambot/content.py`). Do **not** create a new one,
  and do **not** use `Matematika`, which belongs to Prime Math.
- File: `_practice_ps_<from>_<to>.py`, exposing `SUBJECT = {...}` + `DEFAULTS = {...}` +
  `PRACTICES = [...]`. Copy `SUBJECT` and `DEFAULTS` unchanged into every batch file.
- Import: `python manage.py import_practices <file> --master=prime --expect-questions=20`
  (local) / `--master=powerty` (production). `--republish` overwrites and rebuilds the
  questions. **Always pass `--expect-questions=20`.**
- Levels, by domain difficulty rather than by number:
  `SAT-1 … 22` **easy** · `SAT-23 … 48` **hard** · `SAT-49 … 65` **medium** ·
  `SAT-66 … 80` **hard** · `SAT-81 … 100` **medium**.

## 2. The ramp — 20 questions, every test

| Q | What it tests |
|---|---|
| 1–4   | **Warm-up.** The rule applied directly, short English stem, small numbers. Nearly free marks — the pupil must feel the lesson worked. |
| 5–10  | **Exam shape.** Full SAT sentences: *which of the following*, *in terms of x*, *equivalent to*, a table or a figure. One idea, but wrapped the way the test wraps it. |
| 11–14 | **Context and interpretation.** A real situation with units, and at least one *"What does the 12 represent in this context?"* — the question type Uzbek pupils lose most often, and it needs no computation at all. |
| 15–16 | **Trap-spotting.** The stem asks for `x + 4`, not `x`; *must be true* vs *could be true*; the percent base; the wrong unit. The lesson's own `.ps-trap` values become choices here. |
| 17–18 | **Module 2 level.** Multi-step, two ideas combined, or a grid-in-style value the pupil must produce before looking at the choices. |
| 19–20 | **Word problems — always two, in every single test, whatever the topic.** A real situation in 1–3 English sentences, the numbers doing the lesson's own work. |

**Questions 19 and 20 are not optional and are not padding** — same rule the user set for
Prime Math, and it matters more here: the SAT *is* a reading test wearing a maths costume.
Rotate their settings so a hundred tests do not read like one: part-time job pay, phone
plan, gym membership, delivery fees, a lab experiment, a school fundraiser, ticket sales,
a road trip, temperature over a week, a plant growing, savings accounts, taxi fares.

## 3. Rules that hold for every question

- **4 choices**, exactly one correct, all four the same shape and roughly the same length.
  Numeric options are in **increasing order** — never scrambled to hide the key. Algebraic
  options are ordered by how similar they look, not randomly.
- **Distractors are the real mistakes**, and every one must be *reachable* by a wrong move
  you could name in one clause:
  - solved for the wrong thing (`x` instead of `x + 4`, one item instead of the total);
  - sign error when moving a term across, or distributing a minus;
  - flipped the slope, or read `b` as the slope;
  - forgot to convert the units (minutes/hours, feet/inches, per week/per year);
  - percent of the wrong base, or added two percentages;
  - answered the *increase* when asked for the *new value*;
  - used the diameter as the radius;
  - stopped one step early.
- **Never** use "None of the above", "Both A and B", or a joke option. The SAT does not.
- The whole test must be solvable **without a calculator being necessary**, even though one
  is allowed: keep the arithmetic clean.
- No question depends on a previous question's answer.
- Figures: inline SVG with the `pm-*` classes, inside the `text`. No `<img>`, no LaTeX.

## 4. Question HTML

Plain, exam-like. No instruction line in Uzbek — the SAT prints none.

```python
{
    "text": "<p>The function <i>f</i> is defined by <i>f</i>(<i>x</i>) = 3<i>x</i> − 5. "
            "What is the value of <i>f</i>(4)?</p>",
    "choices": ["2", "7", "12", "17"],
    "correct": "7",
    "explanation": "<p><strong>7.</strong> <i>x</i> oʻrniga 4 qoʻyamiz: "
                   "3 × 4 − 5 = 12 − 5 = 7.</p>"
                   "<p><strong>12</strong> — koʻpaytirib toʻxtab qolgan javob: −5 ni "
                   "unutmang. Test har doim yarim yoʻlda toʻxtagan javobni qoʻyadi.</p>",
},
```

For a question with a figure, put the `<figure class="pm-fig">…</figure>` between the
sentence and the choices, exactly as in the tutorial.

## 5. Explanations

Every explanation, in Uzbek, does three things in this order:

1. **The key, in bold, first** — `<strong>7.</strong>`. The pupil checking an answer should
   see it in the first two words.
2. **The reasoning**, short and complete. A `pm-solve` ladder is allowed when the steps
   matter; otherwise 1–3 sentences.
3. **The named mistake** behind the most tempting wrong choice — *which* choice, and *what
   move* produces it. This is the part that actually raises a score, and it is why an
   explanation is never one line.

For interpretation questions (11–14), the explanation must translate the English phrase
that carried the difficulty: *"«per additional hour» — har bir qoʻshimcha soat uchun, yaʼni
qiyalik."*

## 6. ⚠️ The answer gate

Same gate as the tutorials (`STYLE_GUIDE_PRIME_SAT.md` §7), and it applies to all 20
questions of every test. Before importing, the throwaway `verify_sat_<range>.py` in the
scratchpad recomputes **every** key independently, checks no two choices are equal, checks
the key is among the choices, and checks each numeric option list is sorted. Run it, fix,
then import.

Then read each English stem once more: *could a careful reader defend a second answer?*
Ambiguity is a bug — on a test that hides the verdict behind a score, it is the worst kind.

## 7. The user's own tips

*(Empty for now — the user's own SAT tips go here as they share them, and they override the
generic advice above.)*

---

## How to ask

> "make the next 5 Prime SAT lessons"

The practice is written **in the same breath as the tutorial**, never afterwards: writing
them side by side is what keeps the test drilling that lesson's own examples, its own traps
and its own English.
