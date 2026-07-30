# Prime English Practices — Writing Guide (for Claude)

How to write the **Prime English practice tests** — one 20-question test per lesson,
`PE-1 … PE-100`, matched **one-to-one** to the tutorials in `tutorial/`. The list of
lessons lives in `toc_pe_practices.txt`.

> Same pupil as the tutorials: an **Uzbek school pupil (11–17)**, English from zero to
> intermediate. The test is not a trap — it is the lesson's last page. A pupil who
> actually read `PE-n` should score 70–90% on practice `n`.

---

## 1. Title, file, import

- Title: `PE-7 Practice: There is / There are` — same number, **same topic wording as the
  tutorial title** (drop the tutorial's own `PE-7:` prefix punctuation, keep the words).
- Every practice carries `"tutorial": "PE-7:"` — the importer matches that prefix and adds
  the practice to that tutorial's `practices` set, so the lesson page grows a **Practice**
  button. Never write the whole tutorial title in that key; the prefix with the colon is
  unambiguous.
- File: `_practice_pe_<from>_<to>.py`, exposing `SUBJECT = {...}` + `DEFAULTS = {...}` +
  `PRACTICES = [...]`. Copy `SUBJECT` and `DEFAULTS` unchanged into every batch file.
- Import: `python manage.py import_practices <file> --master=prime --expect-questions=20`
  (local) / `--master=powerty` (production). Add `--republish` to overwrite + rebuild
  questions. **Always pass `--expect-questions=20`** — it refuses the file if a test has
  drifted to 19 or 21 questions, which is otherwise easy to miss.
- Batches of **5 lessons** (100 questions). Mark the range `[done]` in the toc afterwards.

## 2. The shape of one test — exactly 20 questions

Fixed difficulty ramp, so every test in the course feels the same:

| Q | What it tests |
|---|---|
| 1–5   | **Recognition.** The core pattern in a plain, short sentence. Almost free marks. |
| 6–12  | **Application.** The same pattern in fuller sentences, plus the sub-rules the lesson taught (spelling changes, question/negative forms, exceptions). |
| 13–16 | **Contrast.** The pattern against the thing pupils confuse it with — the lesson's own "vs" section (a/an vs the, was vs were, since vs for…). |
| 17–18 | **Error spotting.** "Which sentence is correct?" / "Which sentence has a mistake?" — built from the lesson's `.pe-fix` wrong/right pairs. |
| 19–20 | **Production.** Word order (choose the correctly ordered sentence), or a short two-line dialogue / mini-context where the pupil picks the natural answer. |

Rules that hold for all 20:

- **4 choices**, exactly one correct. Choices are short and parallel in shape — never one
  long option among three tiny ones (that gives the answer away).
- **Distractors must be the real mistakes** an Uzbek pupil makes: the missing `-s`, the
  missing article, `he don't`, `since 3 years`, `I am agree`, Uzbek word order. Never
  filler like `plaies` or nonsense words.
- Vary the correct letter. Do not let the answer sit in the same slot repeatedly —
  across a test, spread the correct option roughly evenly over positions 1–4.
- No question may need grammar the course has not reached yet. `PE-9` may not test the
  present perfect. Recycling **earlier** lessons is welcome and good.
- Nothing depends on outside knowledge — no trivia, no rare vocabulary. If a word is
  above elementary level, it is not the thing being tested.

## 3. Question HTML

Keep it exactly this shape — it renders inside CKEditor fields, so plain tags only:

```python
{
    "text": "<p>Choose the correct option.</p>"
            "<p><strong>My brother ___ football every Sunday.</strong></p>",
    "choices": ["play", "plays", "playing", "is play"],
    "correct": "plays",
    "explanation": "<p><strong>plays</strong> is correct. In the Present Simple we add "
                   "<strong>-s</strong> after <em>he / she / it</em>.<br><br>"
                   "<em>(<strong>plays</strong> toʻgʻri. Present Simple da <em>he / she / it</em> "
                   "dan keyin fe'lga <strong>-s</strong> qoʻshiladi.)</em></p>",
},
```

- Line 1 of `text` is the **instruction** (`Choose the correct option.` /
  `Choose the correct article.` / `Which sentence is correct?` / `Complete the dialogue.`).
- Line 2 is the **item**, in `<strong>`, with `___` for the gap.
- Allowed tags: `<p> <strong> <em> <br> <ul> <li>`. No `<script>`, no `pe-*` classes —
  those belong to the tutorials, not here.
- Dialogues: one `<p>` per turn — `<p><strong>A:</strong> …</p><p><strong>B:</strong> ___</p>`.

## 4. Explanations — English first, Uzbek in italics (mandatory)

Every question gets an explanation in **both** languages, in this order:

1. **Name the answer and why it is right**, in plain English, one or two sentences,
   quoting the rule the tutorial used. Repeat the lesson's own wording — that is the point
   of a matching practice.
2. `<br><br>` then the **same explanation in Uzbek**, wrapped in `<em>( … )</em>`.
3. When a distractor is genuinely tempting, add one clause on *why it is wrong*
   ("`is` is for one thing, and *Sam and I* = we"). Do this for at least the harder half
   of the test, always in both languages.

Uzbek: use `oʻ` and `gʻ` (with the ʻ mark), never `o'` / `g'` / `ў`. Keep grammar terms in
English inside the Uzbek text (`Present Simple`, `article`, `subject`) — that is how the
tutorials do it and how the pupil's teacher says them.

## 5. Practice-level metadata

```python
{
    "title":       "PE-1 Practice: What Is a Sentence? Subject + Verb",
    "tutorial":    "PE-1:",
    "description": "PE-1 darsiga 20 savol: subject va verb, gap tuzilishi. "
                   "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
    "level":       "easy",
    "questions":   [...],
}
```

- `description` is in **Uzbek** (that is what pupils read on the practice card), one or two
  sentences: which lesson, which topics, and that answers are explained in both languages.
- `level`: lessons 1–31 → `easy`, 32–66 → `medium`, 67–100 → `hard`. Follow the toc; a
  lesson that is obviously harder than its neighbours may move up one step.
- `DEFAULTS` already sets published / free / unlimited attempts / answers shown after,
  `pass_score` 60 and no time limit. Do not set a `time_limit` unless the user asks.

## 6. Checklist before importing

- [ ] Exactly 20 questions, in the ramp of section 2.
- [ ] Every question: 4 choices, one `correct` **copied character-for-character** from
      `choices` (the importer refuses the file otherwise), no duplicate choices.
- [ ] Every explanation has both languages, English then Uzbek in `<em>( … )</em>`.
- [ ] Correct answers spread across positions, not stacked in one slot.
- [ ] No grammar from a later lesson; nothing the tutorial did not teach.
- [ ] `tutorial` prefix matches a real tutorial (`PE-n:`).
- [ ] Ran the import locally, then gave the user the `railway run …` line.

## 7. The user's own tips

These come from the user directly and **override anything above**.

### Use his real pupils' names (asked 2026-07-30)

Every test must be populated with his own class, not with generic names — the pupils enjoy
finding themselves in the questions.

**Pupils:** Afsona, Jasur, Sherbek, Davron, Samandar, Iroda, Shaxzoda, Marjona, Madina,
Charos, Firdavs, Ilgʻor, Javohir, Sirojiddin, Behruz, Elbek, Abdulloh.
**Teacher:** Rozimurod — refer to him as *Rozimurod teacher*, *our teacher Rozimurod* or
*Mr Rozimurod*, the way the class does.

- **Spread them out**: aim for 8–12 different names across a 20-question test, and change
  which names lead from one test to the next. Never lean on the same two or three.
- **Match the pronouns**: girls — Afsona, Iroda, Shaxzoda, Marjona, Madina, Charos
  (*she / her*); boys — Jasur, Sherbek, Davron, Samandar, Firdavs, Ilgʻor, Javohir,
  Sirojiddin, Behruz, Elbek, Abdulloh (*he / his*). A name with the wrong pronoun is worse
  than a generic name.
- Keep the ʻ (U+02BB) in **Ilgʻor**.
- Rozimurod teacher is useful for anything involving school: giving homework, asking
  questions, praising, being strict about being late.
- The same list lives as `PUPILS` in `practice/management/commands/math_questions.py`.
