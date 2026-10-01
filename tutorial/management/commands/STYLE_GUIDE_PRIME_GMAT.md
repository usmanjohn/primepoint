# Prime GMAT — style guide

Prime GMAT is the seventh course on the Prime machinery (tutorial + practice + Corner
reading, playlist "Prime GMAT", titles `GMAT-1: …`, category `math`). It started
**2026-10-01** as a 5-lesson pilot of the **Quant** section.

**It is built on Prime SAT Math.** Read `STYLE_GUIDE_PRIME_SAT.md` first. Its language
split, lesson shape, depth bar, `pe-*`/`pm-*`/`ps-*` kit, HTML-not-LaTeX rule and the
answer gate all apply here unchanged. This guide lists only the differences.

## 0. The pupil and the language
- The pupil is an **adult**: a graduate heading to an MBA or a business master's,
  often working. Write to a colleague, not to a schoolchild: no "bolajonlar", no
  school-grade framing. Worked examples are business-shaped: invoices, prices, schedules,
  inventory, revenue.
- **The exam speaks English, the teacher speaks Uzbek** — exactly as in Prime SAT. Stems,
  choices and Exam-English phrases are in English; every explanation, callout and recap
  is in Uzbek. The `pe-gloss` lists the English term first.
- Numbers are written the American way: `3.5`, `1,200`, `$45`.

## 0.1 Facts about the test (GMAT Focus Edition — mba.com / gmac.com, checked 2026-10-01)
- **Quantitative Reasoning**: 21 questions in 45 minutes, all **Problem Solving**, with
  **five** answer choices. Content is **arithmetic and algebra only**: no geometry.
  **No calculator.**
- **Data Sufficiency is NOT in Quant** any more; it moved to **Data Insights**, which
  also has the on-screen calculator. Never teach DS or geometry in a Quant lesson.
- Scores: each section is 60–90; the total is **205–805**, and the three sections
  (Quant, Verbal, Data Insights) are weighted equally.
- The candidate picks the section order. There is one optional 10-minute break, and
  **Question Review & Edit** allows changing up to **3** answers per section.
- Never state a fee, a test date or a school's score cut-off. Send the reader to mba.com.

## 1. Differences from Prime SAT, item by item
| Prime SAT Math | Prime GMAT |
|---|---|
| 4 choices (A–D) | **5 choices (A–E)**: `.ps-ch` letters come from a CSS counter, so a fifth `<li>` just works |
| `ps-desmos` keystroke blocks | **never**: there is no calculator. Teach mental-arithmetic moves instead (÷4 × 100 for 25, 198 = 200 − 2, split 15 = 10 + 5) |
| grid-in answers (`ps-gridin`) | **never**: every GMAT Quant question is multiple choice |
| `.ps-stem__tag` "SAT-style question" | **"GMAT-style question"**, with a `ps-time` chip (45–120 s; the section's average is ~2 min) |
| geometry, trigonometry | **out of scope** |
| school-age examples | business examples |

The lesson shape and depth bar are SAT's: goal, explanation, ≥ 3 `pm-solve` worked
examples, an Exam-English `ps-phrase` list, ≥ 2 `ps-stem` with their `ps-trap`s, a
`ps-tactic`, ≥ 2 `pe-fix`, ≥ 3 `pe-uz` callouts, 5 `pe-quiz`, `pe-gloss`, and `pe-recap`.
The recap title class is **`pe-recap__t`**, not `__title`; the gate catches it.

## 2. The GMAT's favourite moves (name them in the lessons)
- **"Must be true"**: break each choice with a counter-example drawn from even, odd,
  negative, 0, 1 and fractions. The choice nothing can break is the answer.
- **Smallest-case test**: "divisible by 6 and 4" → test n = 12 (the LCM), not 24.
- **Base trap in percents**: percent change ÷ the *original*; successive changes
  *multiply*.
- **The half-way answer**: the GMAT nearly always lists the value you have after one
  step of a two-step problem. Name it in a `ps-trap`.

## 3. Practices (`practice/management/commands/_practice_pg_<range>.py`)
- Subject **`GMAT`** (icon `bi-graph-up-arrow`, colour `#0f766e`). It is **not** in the
  Telegram `ROTATION`. Add it there only if the user asks.
- 20 questions, **5 choices each**, numeric choices in increasing order. The ramp is
  `STYLE_GUIDE_PS_PRACTICE.md`'s (warm-up, exam shape, context, traps, hard, and two
  word problems at 19–20).
- Each explanation opens with the bold key `<p><strong>…</strong>`, then the reasoning,
  then names the planted wrong answer by its **text**. Never cite a letter: choices are
  shuffled.
- Import with `--expect-questions=20`.

## 4. The answer gate
`verify_gmat_<range>.py` in the scratchpad re-derives every key by a **different route**:
- direct `Fraction` arithmetic;
- `math.gcd` / `lcm` and divisor lists;
- **brute force** for every "must be" question. The gate turns each choice into a Python
  expression and evaluates it over negatives, 0, 1, fractions and positives that satisfy
  the stem. Exactly the key may survive.

It also checks:
- 5 distinct choices with the key among them, sorted numeric lists, the bold-key
  opening, and no choice letters;
- in the lessons, that each `ps-sol__ans` letter points at the choice whose text it
  repeats, and every `pe-quiz` answer;
- that every class is defined in `style.css`, tags are balanced, and there is no
  `<script>`/`style=`;
- in the readings: words, gloss count, no notation, and computed keys.

**Prove it bites** before trusting it: plant one wrong key in a copy and watch it fail.
The pilot's gate caught a recap class that does not exist.

## 5. Lessons from batch 2 (GMAT-6…10, 2026-10-02)
- **The gate measures the depth bar**: ≥ 900 words of prose (tags stripped), ≥ 3 `pe-uz`,
  ≥ 3 `pm-solve`, 2 `ps-stem`, 2 `ps-trap`, 2 `pe-fix`, 5 `pe-quiz`. The pilot's gate
  did not, so GMAT-4 and GMAT-5 shipped one callout short and GMAT-5 at 767 words.
- **`pm-word` table cells do not wrap** (`white-space: nowrap`). A table with sentences in
  its cells, or more than two text columns, runs off a 390px screen. Keep tables to short
  values (fractions, digit cycles); write comparisons as paragraphs.
- **Uzbek letters are `ʻ` and `ʼ`** (oʻ, gʻ, yaʼni), never `'` or `‘`. The gate refuses
  ASCII apostrophes in Uzbek explanations.
- Days of the week are verified against `datetime`, not by counting on fingers. "100 days
  from Monday" is the remainder of 100 ÷ 7; today is day 0.
- **`pe-tip` is not a `pe-uz`.** The depth bar wants three `pe-uz` callouts *besides* the
  teacher's tip. Batches 2–5 each came up exactly one short because the tip was counted as a
  callout. Write three Uzbek callouts from the start.
- **Write long data files in one piece.** Twice a readings file was closed early, in the
  middle of a story's body. Load the module and count the stories before running the gate.

## 6. Course status
Quant block **complete 2026-10-02** (GMAT-1…25). Verbal Reasoning and Data Insights are not
started; the user decides whether they are built and where (`tutorial` or `examprep`).
