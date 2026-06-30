# TOPIK Lesson Writing Guide (for Claude)

This guide tells Claude HOW to write **examprep** TOPIK lessons. It is the same for
every skill (Reading, Writing, Listening, …). Each skill has its own table-of-contents
file (e.g. `toc_topik_reading.txt`) that lists the lessons and their order.
**Always follow the table of contents order.**

> You (the user) do NOT need to repeat these rules each time. Just say which skill and
> how many to create (see "How to ask" at the bottom).

The data model is richer than tutorials: a lesson is a list of **blocks**. The lesson
player renders each block in this order: **image (+caption) → rich text → MCQ choices →
explanation (after submit)**. So you compose a lesson out of several blocks instead of
one big HTML field.

---

## 1. Title & ordering

Every lesson title starts with the track + skill and its number, then the topic:

```
TOPIK Reading 1: Skimming for the Main Idea
TOPIK Reading 2: Finding the Order of Sentences
TOPIK Writing 51: Describing a Chart (문제 53)
```

- The track name, skill, and author come from the top of each `toc_topik_<skill>.txt`.
- The number = the lesson number from the table of contents, and it is also written to the
  `order` field (this is how the playlist sequences lessons and how Claude knows where to
  continue next time).

## 2. Structure of a lesson (the `blocks` list)

Build each lesson from blocks, in this order:

1. **Intro block** (`rich_text`) — `<h2>TOPIK Reading 1: ...</h2>` + a 1–2 sentence
   description of what the lesson teaches and why it matters for the real TOPIK.
2. **Teaching blocks** (`rich_text`) — explain the strategy/concept step by step, easy →
   hard. Use a few smaller blocks (concept → method → worked example → common mistakes)
   rather than one giant block, so the player paginates nicely.
3. **Practice question blocks** — a block with `rich_text` (the question prompt) **and**
   `choices` (the MCQ options, exactly one `is_correct: True`) **and** `explanation`
   (revealed after the student answers — give the full reasoning, not just the letter).
4. **Wrap-up block** (`rich_text`) — a `<h3>Summary</h3>` with the key takeaways as a list,
   placed after the "Key words" glossary (section 5).

### Depth & length (minimum bar — do NOT write thin lessons)

Each lesson must be **detailed and thorough**. Across its blocks, every lesson must have:

- **At least ~500–800 words** of real explanation. Explain the *why* (what TOPIK is
  testing, how graders/question-writers think), not just the *how*.
- **At least 2 worked examples** showing the full approach on a TOPIK-style item.
- **At least 2 practice question blocks** (MCQ with `choices` + `explanation`).
- The 3–4 inline Uzbek explanations and the glossary from section 5.

## 3. Tools to make it high quality (mix them, don't overuse)

- **Highlights** for key ideas: `<mark>key strategy</mark>`
- **Emphasis**: `<strong>`, `<em>`, `<u>`
- **Quote boxes** for rules/tips: `<blockquote>Tip: read the question before the passage.</blockquote>`
- **Lists**: `<ul>` / `<ol>` for steps.
- **Korean text** is welcome and expected — write it directly (한글), and gloss it in
  English (and Uzbek for key words). Example:
  `<p>The word <strong>그러나</strong> (however) signals a contrast.</p>`
- **MCQ blocks** for practice: prompt in `rich_text`, options in `choices`, reasoning in
  `explanation`.

## 4. Korean & formatting notes

- Write Korean directly as Hangul (한글) — the editor supports Unicode. Don't romanize
  unless you're teaching pronunciation.
- When you quote a passage or example sentence, put it in a `<blockquote>` so it stands out.
- No LaTeX is needed for TOPIK; if a number/percentage appears (Writing 53 charts), write
  it plainly (e.g. `35%`, `2024년`).

## 5. Uzbek (required)

Keep **English as the main language**, but every lesson must include real Uzbek support:

1. **At least 3–4 short Uzbek explanations** on the key/hard parts, inline after the
   English idea, in italics:
   `<p>Read the question first. <em>(Oʻzbekcha: avval savolni oʻqing, keyin matnni.)</em></p>`
2. **A "Key words — Kalit soʻzlar" glossary** near the end (just before the Summary), with
   **at least 6–8 terms** — mix the lesson's English strategy terms and the important
   Korean vocabulary, each translated to Uzbek:
   ```
   <h3>Key words — Kalit soʻzlar</h3>
   <ul>
     <li><strong>Main idea</strong> — asosiy fikr</li>
     <li><strong>그러나 (however)</strong> — lekin / ammo</li>
     ...
   </ul>
   ```

## 6. The `summary` field (separate from blocks)

Each lesson dict has a short `summary` (max 300 chars) shown on listing/nav cards. Write
one clear sentence describing what the lesson teaches.

---

## 7. User's TOPIK tips / voice  ⟵ TO BE FILLED IN

> The user prepared for TOPIK themselves and will share their personal tips, strategies,
> and the order/phrasing they want. **Paste those tips here.** Until then, Claude writes
> solid general TOPIK strategy; once the tips land, this section overrides the generic
> advice — match the user's wording, emphasis, and recommended techniques.

_(empty — awaiting the user's tips)_

---

## How to ask (what the user types)

Just say, for example:

- **"Make the next 5 TOPIK reading lessons"** — Claude checks which Reading lessons
  already exist, continues in order, writes the batch, and imports them.
- **"Make TOPIK writing 1 to 6"** — Claude does that exact range.
- **"Redo TOPIK Reading 3"** — Claude rewrites that one (with `--republish`).

Claude will: read this guide → read the skill's `toc_topik_<skill>.txt` → check the
database for the highest `order` already done in that track+skill → write the next batch
into a `_lessons_topik_<skill>_<range>.py` file → run
`python manage.py import_examprep <file> --author=<username>`.
