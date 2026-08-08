# Prime Russian Practices — Writing Guide (for Claude)

How to write the **Prime Russian practice tests** — one test per lesson, `PR-1 … PR-100`,
matched **one-to-one** to the tutorials. The lesson list lives in `toc_pr_practices.txt`.

> Same pupil as the tutorials: an **Uzbek learner starting Russian from zero**.
> The test is not a trap — it is the lesson's last page. A pupil who actually read `PR-n`
> should score 70–90% on practice `n`.

---

## 0. The language rule (same as the tutorials)

**Everything the pupil reads is in Uzbek. Russian appears only as the material being
tested.** Instructions, questions, choices-that-aren't-Russian, and every explanation:
Uzbek. **No English anywhere** — not even "Practice" in the title.

This is the same policy as `STYLE_GUIDE_PK_PRACTICE.md` and the opposite of
`STYLE_GUIDE_PE_PRACTICE.md`. There is only one teaching language here, so **no italic
second copy** — write the explanation once, in Uzbek, properly.

⚠️ Do not confuse these with the **older standalone Russian tests** (`Часть 61:
Действительные причастия` …) built by `create_russian_practices_new.py`. Those are written
*in Russian* and belong to no lesson. Prime Russian practices are in Uzbek and every one of
them carries a `"tutorial"` key.

## 1. Title, file, import

- Title: `PR-7 Mashq: Salomlashish, tanishuv va murojaat` — same number, same topic wording
  as the tutorial (drop the tutorial's `PR-7:` punctuation, keep the words). `Mashq`, not
  `Practice`, not `Практика`.
- Every practice carries `"tutorial": "PR-7:"` — the importer matches that prefix and adds
  the practice to that tutorial's `practices` set, so the lesson page grows a **Practice**
  button. Never write the whole title there.
- Subject: `Russian` — the practice Subject that already exists (the old Russian drills use
  it too). Do not create a new one.
- File: `_practice_pr_<from>_<to>.py`, exposing `SUBJECT = {...}` + `DEFAULTS = {...}` +
  `PRACTICES = [...]`. Copy `SUBJECT` and `DEFAULTS` unchanged into every batch file.
- Import: `python manage.py import_practices <file> --master=prime --expect-questions=<n>`
  (local) / `--master=powerty` (production). `--republish` overwrites and rebuilds
  questions. **Always pass `--expect-questions`** — it refuses the file if a test has
  drifted off its length.

## 2. Two test lengths

| Lessons | Questions | Why |
|---|---|---|
| **PR-1 … PR-5** (alifbo) | **12** | These teach letters and sounds, not grammar. A 20-question alphabet test is padding. `--expect-questions=12` |
| **PR-6 … PR-100** (grammatika) | **20** | Full grammar tests, same ramp as Prime English and Prime Korean. `--expect-questions=20` |

### Ramp for the alphabet tests (12 questions)

| Q | What it tests |
|---|---|
| 1–3   | **Tanish** — name the letter, name its sound, which family it belongs to (bir xil / soxta doʻst / yangi). Nearly free marks. |
| 4–7   | **Oʻqish** — read a real word aloud, pick the right pronunciation, count the syllables, find the stressed vowel. This is the core: the pupil must actually *read*. |
| 8–10  | **Farqlash** — the lesson's own contrast: В vs B, Ы vs И, Ш vs Щ, Ъ vs Ь, ж vs ш. |
| 11–12 | **Qoʻllash** — spot the wrong reading, or pick the correctly written word. Built from the lesson's `.pe-fix` pairs. |

### Ramp for the grammar tests (20 questions)

| Q | What it tests |
|---|---|
| 1–5   | **Tanish** — the pattern in a short, plain sentence. |
| 6–12  | **Qoʻllash** — the pattern in fuller sentences, plus the lesson's sub-rules (gender branching, stress shift, hard/soft stem, irregular forms). |
| 13–16 | **Farqlash** — the pattern against what pupils confuse it with (в vs на, ты vs вы, -ый vs -ой, НСВ vs СВ, Р.п. vs В.п.). |
| 17–18 | **Xato topish** — "Qaysi gap toʻgʻri?" / "Qaysi gapda xato bor?", from the lesson's `.pe-fix` pairs. |
| 19–20 | **Tuzish** — word order, or a two-line dialogue where the pupil picks the natural reply. |

## 3. Rules that hold for every question

- **4 choices**, exactly one correct, short and parallel in shape. Never one long option
  among three tiny ones.
- **Distractors must be the real mistakes an Uzbek pupil makes**, not filler:
  - reading В as "b", Р as "p", С as "s→k", Н as "h", У as "u→y" (the false friends);
  - Ы pronounced as И; Щ as Ш; a released Ь ("kitab-i");
  - forgetting оглушение: `хлеб` read as [хлеб] instead of [хлеп];
  - **gender agreement**, since Uzbek has none: `новый книга`, `моя брат`, `она сказал`;
  - the wrong case after a preposition: `в школа`, `у меня есть брата`;
  - Uzbek word order pushed onto Russian;
  - **aspect**: using НСВ where the result matters (`Вчера я читал книгу до конца`).
- **Vary the correct letter** — spread the answer roughly evenly over positions 1–4.
- **Nothing from a later lesson.** `PR-12` may not test the родительный падеж. Recycling
  **earlier** lessons is welcome and good.
- Stress marks in questions follow the tutorial policy (section 4 of
  `STYLE_GUIDE_PRIME_RUSSIAN.md`): everywhere through PR-20, then only on new or shifting
  words.

## 4. Question HTML

Plain tags only — this renders inside CKEditor fields:

```python
{
    "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>молоко́</strong></p>",
    "choices": ["[мълако́]", "[молоко́]", "[мулуко́]", "[малако]"],
    "correct": "[мълако́]",
    "explanation": "<p><strong>[мълако́]</strong> toʻgʻri. Urgʻu oxirgi <strong>о</strong> "
                   "da, shuning uchun undan oldingi ikkala <strong>о</strong> ham "
                   "qisqaradi — bu <strong>аканье</strong>. Urgʻudan bir boʻgʻin oldingi "
                   "о [a] boʻlib, undan ham oldingisi esa deyarli eshitilmaydigan "
                   "[ъ] boʻlib chiqadi.</p>",
},
```

- Line 1 of `text` is the **instruction** in Uzbek — `Toʻgʻri javobni tanlang.` /
  `Bu soʻz qanday oʻqiladi?` / `Qaysi harf?` / `Qaysi gap toʻgʻri?` /
  `Boʻsh joyga nima tushadi?` / `Qaysi jinsda?`
- Line 2 is the **item**, in `<strong>`, with `___` for a gap.
- Allowed tags: `<p> <strong> <em> <br> <ul> <li>`. No `<script>`, no `pe-*`/`pr-*`
  classes — those belong to the tutorials.
- Dialogues: one `<p>` per turn — `<p><strong>— </strong>…</p>`. Russian marks dialogue
  with a dash, not with A/B letters; keep that habit.

## 5. Explanations

One paragraph, Uzbek, and it must **teach**, not just announce:

1. Name the answer in `<strong>` and say **why** it is right, quoting the rule the tutorial
   used — repeating the lesson's own wording is the whole point of a matched practice.
2. When a distractor is genuinely tempting, add a clause on why it is wrong
   ("книга — ayol jinsi, shuning uchun новый emas, новая").
3. Name the Russian term when the lesson named it (аканье, оглушение, род, падеж, вид) —
   the pupil should leave the test knowing what to call the thing.
4. Where Uzbek helps, use it: "xuddi oʻzbekchadagi *kitob**ni*** kabi — В.п. ham otga
   qoʻshimcha qoʻshadi".

## 6. The user's own tips

*(Empty for now — when the user shares how they want these tested, it goes here and
overrides the generic advice above.)*

---

## How to ask

- **"Make the practices for PR-6 … PR-8"** — Claude checks the toc, writes the batch file,
  imports it with the right `--expect-questions`, and gives the Railway command.
- Normal rhythm from PR-6 is **3 lessons at a time, all three legs together**: tutorial →
  practice → reading. See the Prime Russian section of `CLAUDE.md`.
