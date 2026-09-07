# SAT Reading & Writing — Writing Guide (for Claude)

How to write the **SAT Reading and Writing** lessons in `examprep`. This is the site's
third `ExamTrack`, beside TOPIK and IELTS, and the sixth course on the Prime machinery.
The lesson lists live in `toc_sat_reading.txt` and `toc_sat_writing.txt`. **Always follow
their order.**

> The pupil is an **Uzbek pupil, 15–18**, who is already doing Prime SAT Math and now has
> to score on the other half of the test. They read English well enough to follow a story
> and badly enough to lose ten marks to a semicolon. What actually costs them points is
> not vocabulary size — it is that they *guess from the general vibe of the passage*
> instead of finding the sentence that proves the answer. This course exists to replace
> guessing with proof.

**Why this track lives in `examprep` and not in `tutorial`** (decided 2026-09-06, do not
re-litigate): every digital-SAT R&W question comes with its *own* short passage and is
answered on the spot. That is exactly one `LessonBlock` — `rich_text` (passage + stem) +
`choices` + `explanation` — graded, scored and tracked. In `tutorial` the whole lesson is
one HTML field, so questions would be dead `<details>` boxes. Prime SAT **Math** stays in
`tutorial`; SAT R&W is here. `prime/subjects.py` and site search join them for the pupil.

---

## 0. THE LANGUAGE RULE — inherited from Prime SAT Math, unchanged

**The exam speaks English. The teacher speaks Uzbek.**

**In English, always, word for word as the test would print it:**
- the lesson **title** (`SAT R&W 12: Words in Context — Two Words, One Sentence of Proof`);
- every **passage** inside `.sr-passage`;
- every **question stem** and all **four answer choices**;
- the grammatical vocabulary being taught (*independent clause*, *antecedent*,
  *supplement*), glossed in Uzbek the first time it appears in a lesson.

**In Uzbek, always:**
- every `<h2>`/`<h3>` heading and every sentence of explanation;
- every `explanation` field — including the reason each wrong choice is wrong;
- every callout box, every tip, every warning;
- the `summary` field and the topic blurbs.

**Never** translate a passage into Uzbek and leave it at that. The pupil must meet the
English sentence, then be *walked through it* in Uzbek. A lesson whose questions are in
Uzbek has removed the exact difficulty the pupil is paying us to remove.

> Rule of thumb: if the sentence would appear on a real test screen, it is in English.
> If it is a human being explaining something to a nervous teenager, it is in Uzbek.

**A question *about* the test is the teacher speaking, so it is in Uzbek.** "How many
minutes does a module last?", "You have 40 seconds and two blanks — what do you do?" —
those stems and their four choices are Uzbek. A question that *simulates* the test is
English, stem and choices both. In practice the whole strategy topic is mostly Uzbek
questions; from the first question-type topic onward almost every question is English.

### 0.1 Numbers are written the American way

Same as Prime SAT Math, and the opposite of Prime Math: **`3.5`** (decimal point) and
**`1,200`** (comma thousands), **`$45`** for money. This matters less in R&W than in Math,
but the courses must not contradict each other — a pupil moves between them daily.

## 0.2 The facts about the test — get these right, every time

The digital SAT, taken in the **Bluebook** app. Do not print anything that contradicts this:

- **Reading and Writing = 2 modules × 27 questions × 32 minutes** — 54 questions, 64
  minutes. Math is a separate 70-minute section that follows it.
- Module 2 is **adaptive**: it gets harder or easier depending on how Module 1 went. Both
  modules count. There is no way to "skip ahead" to the easy module.
- **Every question is multiple choice with exactly four choices.** There are no grid-ins
  in R&W (those are Math only) and there is **no essay** — the optional essay is gone.
- **Every question has its own passage of about 25–150 words.** You never answer ten
  questions about one long text; each question is its own little world. This single fact
  drives the whole course — see §1.
- Passages are drawn from four subject areas: **literature, history/social studies,
  humanities, and science**. Some are poetry; some are pairs of texts; some come with a
  table or a bar chart.
- **No penalty for a wrong answer.** Never leave a blank. Say this often.
- Reading & Writing scaled score is **200–800**, added to Math's 200–800 for the
  **400–1600** total.
- Pacing target: **~71 seconds per question** (32 min ÷ 27). Put a realistic `.sr-time`
  on worked examples — 25–40 s for a Conventions question, 90 s for a Cross-Text one.
- **Questions are grouped by domain**, and inside each group they run from easier to
  harder. In the Bluebook practice tests the groups appear in this order: Craft and
  Structure → Information and Ideas → Standard English Conventions → Expression of Ideas.
  Teach the *grouping* as the reliable fact — a pupil who notices the domain has changed
  knows the kind of thinking has changed too.
- The four domains and their official weights:

| Domain | Share | Questions | Our `skill` |
|---|---|---|---|
| Craft and Structure | ~28% | 13–15 | `reading` |
| Information and Ideas | ~26% | 12–14 | `reading` |
| Standard English Conventions | ~26% | 11–15 | `writing` |
| Expression of Ideas | ~20% | 8–12 | `writing` |

⛔ **Never invent registration fees, test dates, centre names or university cut-offs.**
Describe the process and send the reader to the official College Board source. Same rule
as the "SAT olami" Corner shelf.

## 0.3 Where an Uzbek pupil actually loses R&W points

Put a coloured callout on at least three of these per lesson, chosen honestly for the topic:

- **Answering from memory of the passage instead of from the passage.** The proof is
  always *on the screen*. Teach: point at the words.
- **Choosing the choice that is true instead of the choice that is asked for.** Three
  wrong choices are usually true statements about the world. Only one answers the stem.
- **Vibe-matching vocabulary.** *Words in Context* is decided by the grammar and logic of
  the sentence, not by which word "feels" cleverest. The hard word is rarely the answer.
- **Reading punctuation as decoration.** In Uzbek, comma rules are looser and there is no
  semicolon habit. On the SAT, a comma between two independent clauses is simply wrong,
  every time, with no exceptions to argue about.
- **The missing article and the missing plural.** Uzbek has no *a/the*, so *the data
  suggest* / *a study* are invisible to the pupil until it is pointed out.
- **Word order after a modifier.** Uzbek puts the modifier before its noun and never
  strands it, so a dangling modifier reads fine to an Uzbek ear.
- **Running out of time on the last five questions.** Conventions questions are the
  fastest marks on the test. Teach the pupil to bank them.

---

## 1. THE ONE FACT THAT SHAPES EVERY LESSON

**One passage, one question.** The digital SAT does not test "reading comprehension" in
the old sense. It tests, 54 times, whether you can find *one sentence of proof* in
about 60 words and use it. So:

- Every teaching point must land in a **question the pupil answers**, not in prose the
  pupil skims. A lesson with 900 words of Uzbek explanation and one question has failed,
  however beautiful the prose.
- **Minimum 4 real exam-shaped questions per lesson, 6 for a practice lesson.** They are
  `choices` blocks, so the pupil is graded instantly and gets points for the lesson.
- Passages must be **written to exam length (25–150 words) and exam register**. Do not
  write learner English, and do not write 400-word IELTS passages. A too-long passage is
  the most common way to write a lesson that does not train the real skill.
- **Write the passage last.** Decide the answer and the three traps first, then write the
  passage that makes exactly that answer provable and exactly those traps tempting. A
  passage written first almost always supports two answers — see §8.

## 2. Lesson structure (the `blocks` list)

The player renders each block in order: **image (+caption) → audio → rich text → choices →
explanation (after submit)**. Compose a lesson from several small blocks, never one giant
field. The shape of an R&W lesson:

1. **Kirish** (`rich_text`) — `<h2>` + 2–3 Uzbek sentences: what this question type looks
   like on screen, how many of them are on the test, and what it is really testing.
   Name the domain (`Craft and Structure`) and put an `.sr-time` chip on it.
2. **Usul** (`rich_text`) — the method, as numbered steps, ideally inside a `pp-steps`
   step-reveal so the pupil meets one move at a time. Three or four steps, never ten.
3. **Ishlangan namuna** (`rich_text`) — one full question *worked out loud* in Uzbek:
   passage in `.sr-passage`, stem, the four choices, then the reasoning. This one is not
   a `choices` block — the pupil is watching, not answering.
4. **Amaliyot bloklari** (`choices`) — **at least 4**, rising in difficulty, each with a
   full `.sr-why` autopsy in `explanation` (§6).
5. **Tuzoqlar** (`rich_text`) — the two or three distractor shapes this question type
   always uses, named, in a warning callout. The pupil should be able to recognise a trap
   by its *shape* by the end of the topic.
6. **Yakun** (`rich_text`) — `pp-flashcards` glossary (6–8 English terms/phrases with
   Uzbek on the back) + `<h3>Xulosa</h3>` and 3–4 bullets.

### Chuqurlik — minimal talab

Per lesson, across the blocks: **~600–900 words of real Uzbek explanation**, **at least 4
answerable questions**, **at least 5 English passages** (worked example + practice), and a
flashcard glossary. Do not ship a thin lesson.

## 3. The `sr-*` component kit

Lives in the **SAT READING & WRITING** section at the bottom of `static/css/examprep-kit.css`.
Pure CSS, no JavaScript. **Never invent an `sr-*` class without adding it to that section
and to this guide first.**

**`.sr-passage` — the passage pane.** Everything the test would print, and nothing else.
Serif, so it never blends into the Uzbek teaching around it.
```html
<div class="sr-passage">
  <p>Marine biologist Kakani Katija studies the ocean's "twilight zone," a layer of water
  too deep for sunlight but teeming with animals. Because these creatures are fragile,
  Katija's team designed a robot that captures them in a soft gel rather than a net.</p>
  <span class="sr-passage__src">Adapted from a 2019 article on deep-sea imaging.</span>
</div>
```
Add `sr-passage--verse` when line breaks matter (poetry): `<div class="sr-passage sr-passage--verse">`.
Use `<p>Text 1</p>` / `<p>Text 2</p>` headings inside two stacked panes for Cross-Text.

**`.sr-blank` — the gap** in a Transitions / Conventions / Inferences stem:
`the results were <span class="sr-blank"></span> convincing.`

**`.sr-focus` — the stretch the question points at** (the underlined word or clause):
`the finding was <span class="sr-focus">unprecedented</span>.`

**`.sr-notes` — the research-notes card**, mandatory for Rhetorical Synthesis:
```html
<div class="sr-notes">
  <p class="sr-notes__head">While researching a topic, a student has taken the following notes:</p>
  <ul>
    <li>Kintsugi is a Japanese method of repairing broken pottery.</li>
    <li>The cracks are filled with lacquer mixed with powdered gold.</li>
    <li>The repair is made visible rather than hidden.</li>
  </ul>
</div>
```

**`.sr-data` — a table or chart** for Command of Evidence (Quantitative). Always inside
`.sr-data__scroll` so a wide table scrolls itself on a phone:
```html
<div class="sr-data">
  <p class="sr-data__title">Average Daily Water Use per Person, 2020</p>
  <div class="sr-data__scroll">
    <table><thead><tr><th>City</th><th>Litres</th></tr></thead>
    <tbody><tr><td>Tashkent</td><td>240</td></tr></tbody></table>
  </div>
</div>
```
Charts are **inline SVG**, never an uploaded image — same rule as Prime Math figures.

**`.sr-why` — the choice autopsy.** See §6; it is where the teaching actually happens.

**`.sr-time` — the pacing chip.** `<span class="sr-time">⏱ ~45 soniya</span>`

### The shared examprep kit (`pp-*`) — use it too
- **MCQ**: nothing to mark up. A block with `choices` + `explanation` is already
  interactive — the pupil clicks and it goes green/red and opens the explanation.
- **`pp-steps`** step-reveal for the method block:
  `<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸"><div class="pp-step">…</div></div>`
- **`pp-flashcards`** for the closing glossary:
  `<div class="pp-flashcards" data-pp-flashcards><div class="pp-card"><div class="pp-card-front">antecedent</div><div class="pp-card-back">olmosh ishora qilayotgan ot</div></div></div>`
- Inline-styled callouts, exactly as TOPIK and IELTS use them:
```html
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;"><strong>💡 Maslahat:</strong> …</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;"><strong>⚠️ Tuzoq:</strong> …</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;"><strong>📌 Eslatma:</strong> …</div>
<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;"><strong>📝 Namuna:</strong> …</div>
```
Highlights: `<mark>`, `<mark style="background:#dcfce7;">to‘g‘ri</mark>`,
`<mark style="background:#fee2e2;">xato</mark>`.

## 4. Writing an exam question

A question block is:
```python
{
    "rich_text": (
        "<div class=\"sr-passage\"><p>…25–150 words of exam English…</p></div>"
        "<p><strong>Which choice completes the text with the most logical transition?</strong></p>"
    ),
    "choices": [
        {"text": "Therefore,",   "is_correct": False},
        {"text": "However,",     "is_correct": True},
        {"text": "For example,", "is_correct": False},
        {"text": "Similarly,",   "is_correct": False},
    ],
    "explanation": "<div class=\"sr-why\">…</div>",
}
```

**Always exactly four choices, exactly one correct.** The real test has four; three is an
IELTS habit and must not leak in here.

**Use the exam's own stems, word for word.** These are the real ones — do not paraphrase:
- *Which choice completes the text with the most logical and precise word or phrase?*
- *As used in the text, what does the word "___" most nearly mean?*
- *Which choice best states the main idea of the text?*
- *Which choice best describes the overall structure of the text?*
- *What is the main purpose of the underlined sentence?*
- *Based on the texts, how would the author of Text 2 most likely respond to the claim in Text 1?*
- *Which quotation from ___ most effectively illustrates the claim?*
- *Which choice most effectively uses data from the table to complete the text?*
- *Which finding, if true, would most directly weaken the researchers' hypothesis?*
- *Which choice most logically completes the text?*
- *Which choice completes the text so that it conforms to the conventions of Standard English?*
- *Which choice most logically completes the text with the most logical transition?*
- *The student wants to ___. Which choice most effectively uses relevant information from the notes to accomplish this goal?*

**The three wrong choices are not filler.** Each must be a *named* trap the real test uses:

| Trap | What it looks like |
|---|---|
| **True but not asked** | A correct statement about the passage that does not answer the stem. |
| **Right idea, wrong scope** | Too broad (covers the whole field) or too narrow (one detail). |
| **Word-match bait** | Repeats a striking word from the passage while reversing its meaning. |
| **Half-right** | The first half is supported, the second half is invented. |
| **Outside knowledge** | True in the world, unsupported by these 60 words. |
| **Grammatically fine, logically wrong** | Conventions and Transitions specialty: it reads smoothly and says the opposite. |

Name the trap in the explanation (§6) using the same words each time, so the pupil learns
the vocabulary of being tricked.

**Facts must be true.** Passages may be invented, but the science, history and people in
them may not be. If a passage names a real researcher, a real study or a real date, it
must be right; if you are not sure, write an unnamed researcher instead. Never attribute
an invented quotation to a real person.

## 5. Vocabulary glossing

The passage stays clean — no glosses inside `.sr-passage`, because the real test has none
and the pupil must survive without them. Gloss instead in the **explanation** and in the
closing flashcards. When a passage leans on one hard word, put it in a `📌 Eslatma`
callout *before* the passage: *"Bu parchada `unprecedented` so‘zi bor — «hech qachon bo‘lmagan»."*

## 6. Explanations — the choice autopsy

The `explanation` is the lesson. Every one uses `.sr-why` and accounts for **all four
choices**, in Uzbek:

```html
<div class="sr-why">
  <div class="sr-why__row sr-why__row--ok">
    <span class="sr-why__tag">TO‘G‘RI</span>
    <span class="sr-why__text"><b>However,</b> — matnning birinchi qismida olimlar
    ishonchli deb hisoblashgan, ikkinchi qismida esa aksi chiqqan. Ikki gap
    <u>qarama-qarshi</u>, shuning uchun qarshilik bog‘lovchisi kerak.</span>
  </div>
  <div class="sr-why__row sr-why__row--no">
    <span class="sr-why__tag">TUZOQ</span>
    <span class="sr-why__text"><b>Therefore,</b> — <i>natija</i> bog‘lovchisi. Grammatik
    jihatdan to‘g‘ri o‘qiladi, lekin mantiqni teskari qiladi: bu «grammatikasi joyida,
    mantiqi xato» tuzog‘i.</span>
  </div>
  …qolgan ikkitasi ham shu tarzda…
</div>
<p>⏱ Bu savol ~30 soniyada yechiladi: bog‘lovchini o‘qimang, avval ikki gapning
<u>munosabatini</u> aniqlang.</p>
```

> ⚠️ **Anchor each row at the choice's OPENING words.** The pupil finds the row by
> scanning the bold text against the list on screen, so `<b>The movement performed by
> returning honeybees…</b>` works and `<b>The movement … is the most complex</b>` does
> not. Elide the middle of a long choice if you must; never the start. The verifier
> in §8 checks this.
>
> ⚠️ **NEVER write "Choice A", "B variant", "(C)" or any letter.** `LessonBlock.display_choices()`
> **shuffles the choices** with a seed from the block id, so the pupil's screen shows them in
> an order you cannot know. Quote the choice's **text** in bold instead — `<b>However,</b>`.
> This is the single easiest way to ship a broken lesson.

## 7. `summary` and titles

- **Title**: `SAT R&W <order>: <English title>` — English, exam register, and it is the
  importer's match key, so **never reword a title** once imported; a changed title creates
  a duplicate lesson instead of updating the old one.
- **`summary`** (≤300 chars): one clear **Uzbek** sentence saying what the lesson teaches.

## 8. THE DEFENSIBILITY GATE — the rule that matters most

Prime SAT Math has an arithmetic gate. R&W's equivalent is harder and matters just as
much: **a question a careful reader can defend two answers to is a bug**, and it teaches
the pupil that the test is arbitrary — the opposite of everything this course says.

Before importing a batch, re-read every question and answer these out loud:

1. **Is the proof in the passage?** Point at the exact words that make the key correct.
   If you cannot quote them, the question is unfixable — rewrite the passage.
2. **Is each wrong choice wrong for a *nameable* reason?** Write the name (§4 table). "It
   just sounds worse" is not a reason and means the choice is defensible.
3. **Could a strong reader argue for a second choice?** Read each distractor as an
   advocate trying to win. If you can make the case, weaken the distractor — do not
   strengthen the explanation.
4. **Does the stem ask what you think it asks?** *main purpose* ≠ *main idea*;
   *structure* ≠ *summary*; *weaken* ≠ *does not support*.
5. **Conventions questions only — is the key the *only* grammatical option?** Three
   choices must be genuinely, checkably wrong (comma splice, wrong tense, agreement
   error), not merely clumsier. Say which rule each one breaks.
6. **Four choices, exactly one `is_correct: True`, no two choices identical.**
7. **No letters in the explanation** (§6) and no Uzbek inside `.sr-passage`.

Run the mechanical half of this with a throwaway script in the scratchpad
(`verify_sat_rw_<range>.py`) that loads the data file and checks, across every block:
four choices with exactly one key and no duplicates · an explanation on every question
block · no choice letters in it · every choice named in the autopsy at its opening words ·
no Uzbek inside `.sr-passage` · passages inside the 25–150-word band · balanced `<div>`s ·
and no `sr-*`/`pp-*` class that is not defined in `examprep-kit.css`. The reading half
(1–5) is done by eye, question by question. Run it, fix, then import.

On the first batch that script caught twelve autopsies anchored mid-choice and nothing
else — which is exactly the split to expect: the machine finds the shuffled-choice and
markup faults, and only re-reading finds a defensible second answer.

### A Python gotcha that bites every batch

Blocks are built by concatenating string literals with `+ CALLOUT.format(…)` pieces.
Python allows *implicit* concatenation between adjacent string literals, but **not**
between a call's `)` and a following literal:

```python
"<p>text</p>"          # fine — implicit concatenation
"<p>more</p>"
+ TIP.format("…")      # fine — explicit +
"<p>next</p>"          # ❌ SyntaxError: needs a leading +
```

The error is reported at the *start* of the enclosing block, dozens of lines above the
real fault, so it reads like a missing comma in `LESSONS`. Import the data file with
`importlib` before doing anything else — it is a one-second check that localises this
instantly.

## 9. Import

```
python manage.py import_examprep examprep/management/commands/_lessons_sat_<skill>_<range>.py --author=prime
```
`--republish` to overwrite existing lessons (it rebuilds their blocks). No new importer is
needed and no audio pipeline exists for this track — R&W has no listening component.

Then mark the range `[done]` in the toc and give the production line — automatically,
every time:
```
railway run python manage.py import_examprep examprep/management/commands/_lessons_sat_<skill>_<range>.py --author=powerty
```

## 10. What this course is not

- Not **Prime SAT Math** (`tutorial`, `SAT-1…100`, finished) — that is the other half of
  the same test, and lessons may cross-refer to it.
- Not the **"SAT olami"** Corner shelf — Uzbek prose *about* the exam, no questions.
- Not the **`exam`** app — that is the timed, scored mock simulator. Questions here are
  practice: the correct answer is visible in the page source, and that is fine.

## 11. Foydalanuvchining SAT R&W maslahatlari (user's own tips)

_(Foydalanuvchi keyin o‘z maslahatlarini shu yerga qo‘shadi — ular yuqoridagi umumiy
tavsiyalardan **ustun turadi**.)_

---

## How to ask

- **"Make the next 5 SAT reading lessons"** — Claude checks the DB, continues in order,
  writes the batch, runs the gate, imports.
- **"Make SAT writing 30 to 35"** — that exact range.
- **"Redo SAT R&W 12"** — rewrite and `--republish`.

Claude does: read this guide → read the right `toc_sat_<skill>.txt` → find the highest
`order` in `SAT` + that skill → write `_lessons_sat_<skill>_<range>.py` → run the
defensibility gate → import → mark `[done]` → give the `railway run` line.
