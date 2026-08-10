# Prime Math Practices — Writing Guide (for Claude)

How to write the **Prime Math practice tests** — one test per lesson, `PM-1 … PM-100`,
matched **one-to-one** to the tutorials. The lesson list lives in `toc_pm_practices.txt`.

> Same pupil as the tutorials: an **Uzbek school pupil (11–16)** working through school
> maths in order. The test is not a trap — it is the lesson's last page. A pupil who
> actually read `PM-n` should score 70–90% on practice `n`.

---

## 0. The language rule (same as the tutorials)

**Everything is in Uzbek.** Instructions, questions, choices, explanations. No English
anywhere — not even "Practice" in the title, and not in the explanations. (The English
term equivalents live only in the tutorial's `pe-gloss` list.) No LaTeX, no Cyrillic.

## 1. Title, file, import

- Title: `PM-23 Mashq: Sonning foizini topish` — same number and same topic wording as the
  tutorial (drop the tutorial's `PM-23:` colon, keep the words). `Mashq`, not `Practice`.
- Every practice carries `"tutorial": "PM-23:"` — the importer matches that prefix and adds
  the practice to the tutorial's `practices` set, so the lesson page grows a **Mashq**
  button. Never write the whole title there.
- Subject: `Matematika` — the practice Subject that **already exists** (the older mixed math
  tests use it). Do not create a new one, and do not use the English-named `Math` subject,
  which belongs to the SAT drills.
- File: `_practice_pm_<from>_<to>.py`, exposing `SUBJECT = {...}` + `DEFAULTS = {...}` +
  `PRACTICES = [...]`. Copy `SUBJECT` and `DEFAULTS` unchanged into every batch file.
- Import: `python manage.py import_practices <file> --master=prime --expect-questions=20`
  (local) / `--master=powerty` (production). `--republish` overwrites and rebuilds
  questions. **Always pass `--expect-questions=20`** — it refuses the file if a test has
  drifted off its length.
- Levels: PM-1 … PM-30 `easy` · PM-31 … PM-70 `medium` · PM-71 … PM-100 `hard`.

## 2. The ramp — 20 questions, every test

| Q | What it tests |
|---|---|
| 1–5   | **Tanish** — the rule applied directly to bare numbers. Nearly free marks: one step, small numbers, no traps. |
| 6–12  | **Qoʻllash** — two-step work, bigger or uglier numbers, the lesson's sub-rules (qavs, ishora, umumiy maxraj, birlik almashtirish). |
| 13–16 | **Farqlash** — the lesson's idea against what pupils confuse it with: `2 + 3 × 4` vs `(2 + 3) × 4`, EKUB vs EKUK, foiz vs foizli nuqta, yuza vs perimetr, mediana vs oʻrta arifmetik. |
| 17–18 | **Xato topish** — "Qaysi yechim toʻgʻri?" / "Qayerda xato qilingan?", built from the lesson's `.pe-fix` pairs; show a short wrong solution and ask which line broke. |
| 19–20 | **Matnli masala — always two, in every single test, whatever the topic.** A real situation, 1–3 sentences, the numbers doing the lesson's own work. |

**Questions 19 and 20 are not optional and are not padding.** They are the reason this
course exists (the user's rule: "please do not just give numerical questions, text also is
important"). Rotate their settings so a hundred tests do not read like one test: bozor,
taksi, telefon tarifi, dala, non yopish, futbol hisobi, sinf jadvali, remont, ish haqi,
sayohat, tugʻilgan kun, kutubxona.

## 3. Rules that hold for every question

- **4 choices**, exactly one correct, all four the same shape and roughly the same length.
  Numeric options are sorted or naturally ordered — never scrambled to hide the answer.
- **Distractors are the real mistakes**, and every one must be *reachable* by a wrong move
  you could name:
  - amallar tartibini buzish (`2 + 3 × 4 = 20`);
  - ishora xatosi (`−3 − 5 = −2`, `−2 × (−4) = −8`);
  - kasr qoʻshishda maxrajlarni ham qoʻshish;
  - foizni notoʻgʻri asosdan olish (yangi narxdan emas, eskisidan);
  - birlik almashtirmaslik (km va m, soat va minut, sm² va m²);
  - yuza oʻrniga perimetr (va aksincha);
  - "necha marta koʻp" ni "nechtaga koʻp" deb oʻqish;
  - off-by-one (nechta ustun / nechta oraliq).
- **Choice order does not need shuffling here.** `PracticeQuestion.display_choices()`
  (`practice/models.py`) re-orders the four options with a shuffle seeded by the question
  id, everywhere a pupil sees them — taking, results, review and print. So write the
  options in whatever order reads best (numeric options: ascending). ⚠️ This is *not* true
  of the Corner readings' questions, which render in stored order — there the answer
  position must be varied by hand.
- **Nothing from a later lesson.** PM-17 may not need foiz. Recycling **earlier** lessons is
  welcome and good — that is how the course stays alive in the pupil's head.
- Numbers stay pupil-sized: mental arithmetic where possible, nothing that needs a
  calculator unless the lesson is about approximation.

## 4. Question HTML

Plain tags only — this renders inside CKEditor fields:

```python
{
    "text": "<p>Hisoblang.</p><p><strong>2 + 3 × 4 = ?</strong></p>",
    "choices": ["14", "20", "24", "9"],
    "correct": "14",
    "explanation": "<p><strong>14</strong> toʻgʻri. Amallar tartibiga koʻra avval "
                   "koʻpaytirish bajariladi: 3 × 4 = 12, keyin 2 + 12 = 14. "
                   "<strong>20</strong> — chapdan oʻngga qarab hisoblaganda chiqadi "
                   "(2 + 3 = 5, 5 × 4 = 20); bu eng koʻp uchraydigan xato.</p>",
},
```

- Line 1 of `text` is the **instruction** in Uzbek — `Hisoblang.` / `Toʻgʻri javobni
  tanlang.` / `Boʻsh joyga nima tushadi?` / `Qaysi yechim toʻgʻri?` / `Qayerda xato bor?` /
  `Masalani yeching.`
- Line 2 is the **item**, in `<strong>`, with `___` for a gap.
- Maths is HTML, exactly as in the tutorials: `x<sup>2</sup>`, `√49`, `≤ ≥ ≠ ≈ ±`, `π`,
  `240 000`, decimals with a comma (`3,5`). Never LaTeX.
- Word problems (19–20) get the situation in a normal `<p>`, then the question in
  `<strong>`:
  `"<p>Afsonaning 240 000 soʻmi bor edi. U pulining 30 foiziga kitob oldi.</p>"
   "<p><strong>Kitob necha soʻm turdi?</strong></p>"`
- Allowed tags: `<p> <strong> <em> <br> <sup> <sub> <ul> <li>`. Simple `<table>` only when
  the question really is a table (jadval, diagramma maʼlumoti). No `pe-*` / `pm-*` classes
  and no SVG — those belong to the tutorials.

## 5. Explanations

One paragraph, Uzbek, and it must **teach**:

1. Name the answer in `<strong>` and show the **work**, not just the result — the two or
   three lines the pupil should have written.
2. Name the tempting distractor and the exact wrong move that produces it. This is where a
   practice test earns its keep.
3. Quote the lesson's own wording for the rule ("amallar tartibi", "umumiy maxraj",
   "ishoralar qoidasi") so the test and the lesson reinforce each other.
4. For word problems, say what the sentence turned into: "«3 marta koʻp» — koʻpaytirish,
   qoʻshish emas: 3x."

## 6. The arithmetic gate

**Every answer is computed twice.** Before importing, run the scratchpad script
`verify_pm_<range>.py` that recomputes each question's answer independently and prints any
mismatch with the question number. A practice test with one wrong key is worse than no
practice test at all.

Check as well that:
- the correct option is present in `choices` exactly as written in `correct`;
- no two choices are equal;
- word problems have enough data to be solvable, and only one reading is possible.

## 7. The user's own tips

*(Empty for now — when the user shares how they want these tested, it goes here and
overrides the generic advice above.)*

---

## How to ask

- **"Make the practices for PM-1 … PM-3"** — Claude checks the toc, writes the batch file,
  verifies the arithmetic, imports it with `--expect-questions=20`, and gives the Railway
  command.
- Normal rhythm is **3 lessons at a time, all three legs together**: tutorial → practice →
  reading. See the Prime Math section of `CLAUDE.md`.
