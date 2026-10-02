# GMAT Verbal Reasoning — Writing Guide (for Claude)

The fourth `ExamTrack` in `examprep` (name **GMAT**, slug `gmat`), started **2026-10-02** at the
user's request. It is the third section of the GMAT Focus Edition; the other two — Quant and
Data Insights — are the tutorial course **Prime GMAT** (GMAT-1…35). Lesson list:
`toc_gmat_verbal.txt`.

**Read `STYLE_GUIDE_SAT_RW.md` first.** Everything there applies — the language rule (exam
English, teacher Uzbek), the lesson shape (intro → method → worked example → ≥ 4 answerable
questions → traps → flashcards + xulosa), the `sr-*` and `pp-*` kits, the inline callouts,
the `.sr-why` autopsy, "never cite a choice letter" (choices are shuffled), and the
defensibility gate. This guide lists only the differences.

**Why examprep and not tutorial** (user's decision 2026-10-02, same reasoning as SAT R&W):
every Verbal question is a passage + a question answered on the spot — one graded
`LessonBlock`. In `tutorial` it would be a dead `<details>` box.

## 0. The pupil
An **adult** — a graduate heading to an MBA or a business master's, often working, reading
English well enough for work and badly enough to lose points to an unstated assumption.
Write to a colleague. Passages are business, economics, science and public policy — a bank
branch, a bakery's prices, a city's traffic plan — not teenage school stories.

## 0.2 The facts about the section (mba.com / gmac.com, checked 2026-10-02)
- **23 questions in 45 minutes** — just under 2 minutes each.
- Two question families: **Critical Reasoning** (a short argument, usually **fewer than 100
  words**, and one question) and **Reading Comprehension** (a longer passage with several
  questions; the skills tested are main idea, supporting idea, inference, application,
  logical structure and style).
- **No Sentence Correction** — removed in the Focus Edition. Never teach grammar-correction
  items as part of this track.
- **Five answer choices** on every question (SAT R&W has four — do not copy that number).
- Section score 60–90; total 205–805 across three equally weighted sections; the candidate
  chooses the section order; one optional 10-minute break; Question Review & Edit allows up
  to 3 answer changes per section. Never state fees, dates or school cut-offs.

## 1. Question blocks
- **Critical Reasoning**: one block = `.sr-passage` (the argument, 25–100 words) + the stem in
  `<p><strong>…</strong></p>` + **five** choices + an `.sr-why` autopsy naming all five.
- **Reading Comprehension**: the passage goes in its own `rich_text` block (200–350 words,
  `.sr-passage`), followed by **two to four** question blocks that refer to "the passage
  above". Do not repeat the passage inside each question block.
- A question *about* the test (strategy topic) is the teacher speaking — Uzbek stem and
  choices, as in SAT R&W §0.

## 1.0 Reading Comprehension lessons (30–36)
- Two real passages per lesson, each 200–350 words, built with `passage()` from
  `_lessons_gmat_verbal_30_32.py`; 3 + 2 questions after them, stems saying "the passage above".
  A worked-example block (the reading map) may sit between a passage and its questions.
- **Every fact in a passage is true** (real people, dates, numbers) — hedge what is disputed
  ("about a thousand stars", "McLean later estimated"). Prefer subjects an Uzbek pupil will meet
  again (Ulugh Beg, the Aral Sea). The toc lists the subjects used; never reuse one.
- Questions are answerable from the passage alone; a choice that is true in the world but not in
  the passage is a trap to name, never a key.
- Gate: in a topic-4 lesson every standalone passage must be 200–350 words and be followed by
  ≥ 2 question blocks; a question block without its own passage must mention "passage".

## 1.1 Boldface / role choices
Their five choices share a first half ("The first is …; the second is …"), so a 7-word autopsy
label leaves two rows looking identical. Use `crf()` (defined in `_lessons_gmat_verbal_23_26.py`),
which names every choice in full. The gate requires each choice's **shortest unique prefix**
(≥ 4 words) in the autopsy, so a truncated label on a boldface question fails it.

## 2. The five CR traps (name them in every CR lesson)
1. **Out of scope** — true or interesting, but not about the gap.
2. **Opposite** — strengthens when asked to weaken (or the reverse).
3. **Too strong** — "always", "no", "all" where the argument needs only "some".
4. **Restated premise** — repeats evidence instead of naming the conclusion/assumption.
5. **Cost, not effect** — for plans: a downside that does not show the plan fails its goal.

## 2.1 The negation test (assumption questions)
A necessary assumption, **negated**, destroys the argument. Teach it in every assumption
lesson and use it in the autopsies: "inkor qilsak — argument yiqiladimi?"

## 3. The gate (defensibility, inherited)
`verify_gmat_verbal_<range>.py` in the scratchpad checks mechanically:
- every question block has **exactly five** distinct choices and exactly one key;
- an `.sr-why` with **five** rows, each naming a choice at its opening words, exactly one
  marked TO‘G‘RI and that one is the key;
- no choice letters; no Uzbek inside `.sr-passage`; CR passages 25–100 words, RC passages
  200–350; balanced `<div>`s; every `sr-*`/`pp-*` class defined in `examprep-kit.css`;
- ≥ 4 answerable blocks per lesson (≥ 5 outside the strategy topic).
Then **re-argue every distractor by eye**: a CR question a careful reader can defend two
answers to is a bug. Write the key and the four traps first, the argument last.
Uzbek letters are `ʻ`/`ʼ` (oʻ, gʻ, yaʼni), never `'` — the older SAT files use `'`; this track
does not.

## 4. Import
```
python manage.py import_examprep examprep/management/commands/_lessons_gmat_verbal_<range>.py --author=prime
```
`--republish` to rebuild. Mark the range `[done]` in the toc and append the production line
(`--author=powerty`) to `temporary.txt`.

## 5. Foydalanuvchining maslahatlari (user's own tips)
_(Foydalanuvchi keyin oʻz maslahatlarini shu yerga qoʻshadi — ular umumiy tavsiyalardan ustun.)_
