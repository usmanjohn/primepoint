# STYLE GUIDE — Logic Arena puzzles

How to write a puzzle for `/logic/`. Read this before writing a batch, and read
`toc_logic_puzzles.txt` to see which puzzles exist and what comes next.

---

## 1. What this section is

A **sealed-answer** logic puzzle. A puzzle opens, everybody sends in an answer,
and **nobody is told whether they were right until the reveal date** — when the
solution and the wall of solvers appear for everyone at once.

That week of not knowing is the entire product. It is what makes a pupil check
their reasoning twice instead of guessing and immediately reading the answer.
Everything below exists to protect it.

Logic Arena is **not**:

- the Math Championship (auto-generated drill questions, instant marking);
- Prime Math (a course, in order, teaching a syllabus);
- a practice test (20 questions, a score out of 100).

It is **one hard, beautiful problem a week**, with a real explanation attached.
A pupil who solves four of these in a term has learned more about thinking than
one who does four hundred arithmetic drills.

---

## 2. Choosing a puzzle

Good candidates share three properties:

1. **The statement fits in a paragraph or two.** If it needs half a page of
   set-up, it is a maths problem, not a logic puzzle.
2. **The naive answer is wrong.** 19 minutes for the bridge, 34 cm for the
   bookworm, fifty-fifty for the three doors. A puzzle whose first guess is
   right has nothing to teach.
3. **The trick generalises.** Every solution ends by naming a transferable idea
   — parity, the pigeonhole principle, counting outcomes, working backwards.
   If you cannot write that closing line, pick a different puzzle.

**Rotate the categories** (`weighing`, `crossing`, `liars`, `cutting`,
`numbers`, `shapes`, `chance`, `strategy`). Never run the same category twice in
a round, and never three rounds in a row.

**Classics are welcome** — they are classics because they are good, and most
pupils have not met them. What must be original is the *telling*: the setting,
the names, and above all the explanation.

**Uzbek settings are encouraged**: Chorsu bazaar, a chaykhana, a dutar, som
rather than dollars. Use the real pupils' names (Afsona, Jasur, Sherbek…) in
puzzles that need people.

---

## 3. The difficulty curve

| ★ | Who it is for | Example |
|---|---|---|
| ★☆☆☆☆ | anybody, one minute | — |
| ★★☆☆☆ | a pupil new to logic puzzles | The Lighter Coin, Wolf/Goat/Cabbage |
| ★★★☆☆ | needs a real idea | The Torch and the Bridge, Ten Sacks |
| ★★★★☆ | needs an idea *and* care | 25 Horses, the Chessboard, the Bookworm |
| ★★★★★ | the flagship; a week is not too long | The Twelve Coins |

Each round carries **two puzzles: one gentler, one harder**, so a round always
has something for a pupil who is new to this and something for one who is not.
Points follow the difficulty automatically (8 / 12 / 16 / 22 / 30); set
`points` explicitly only to override.

---

## 4. The answer must be a short, checkable value

The auto-check only ever sees a typed string, so:

- **Ask for one value**: a number, a count, a distance, "the other road".
  Never "explain your method" — that is what the reasoning box is for.
- **Make it unguessable.** "How many weighings do you need?" invites a guess of
  2 and rewards it. "With four weighings, how many coins?" (81) can only be
  answered by someone who understood *why* two weighings sort out nine. When
  the natural question has a guessable answer, ask the **generalisation**
  instead — it is both harder to guess and better mathematics.
- **Avoid yes/no and 1-in-3 answers.** Half the section's pupils would score
  by luck.
- **State the required answer explicitly** in a `<p class="lg-ask">` block at
  the very end of the body: *"Answer to type: the shortest total time, in
  minutes."*
- Fill `answer_hint` / `answer_hint_uz` with the shape of the answer
  ("a number of minutes" / "necha daqiqa (son)"); it is printed next to the
  input.

### The `accepted` list

Comparison already ignores case, spacing, punctuation and Uzbek apostrophe
variants (`oʻ` = `o'` = `o‘`), and compares plain numbers numerically, so `17`,
`17.0`, `17 ` and `17.` all match on their own. What you must add by hand:

- **both languages** — `['7 crossings', '7 marta', 'yetti', 'seven']`;
- **the unit spelled out** — `['40 kg', '40 kilo']`;
- **any equivalent form** of a non-numeric answer — for "the other road":
  `['other', 'boshqa yoʻl', 'ikkinchi', ...]`.

⚠️ Normalisation strips spaces and commas, so `2,2,9` and `9,2,2` normalise to
*different* strings. When an answer is a set, either ask for one element of it
("how old is the eldest?") or list the permutations in `accepted`.

---

## 5. ⚠️ THE ANSWER GATE (the rule that matters most)

**A wrong answer key is the worst bug this section can ship** — worse here than
anywhere else on the platform, because the pupil is told they were wrong a week
after they were right, in public, on the solvers wall.

So: **every answer is computed twice, the second time by a throwaway script in
the scratchpad** (`verify_logic_<range>.py`) that derives each answer
independently — by brute-force search, BFS over states, or an explicit formula —
and prints a mismatch. Run it, fix, *then* import. See the existing script for
the pattern; it verifies all sixteen of season 1.

Anything that cannot be computed (a "which road" answer) must be argued through
both cases in writing before it goes in.

---

## 6. Writing the body

Structure, in order:

1. **One or two short paragraphs** setting the scene. Present tense, concrete
   nouns, a real place.
2. **A figure**, if a picture helps (see §7).
3. **The constraint**, in a `lg-rule` box — the thing that makes it a puzzle:
   *"He may use the balance twice. Not three times — twice."*
4. Optionally a **nudge toward the interesting part** — *"The obvious plan takes
   19 minutes. It is not the best."* Telling them the naive answer is wrong is
   generous, not a spoiler; it saves a pupil from confidently stopping early.
5. **The `lg-ask` block** saying exactly what to type.

Keep it short. The body of a good puzzle is 120-200 words plus a figure.

`hint` / `hint_uz` is one sentence, hidden behind a toggle. It should point at
the *kind* of idea needed, never at the answer: *"The balance does not answer
yes or no. Count how many different things it can tell you in one go."*

---

## 7. Figures — inline SVG only

Never an uploaded image. Build figures with the helpers in `logic/figures.py`:

```python
from logic.figures import fig, coins, balance, river, bridge, jugs, ropes, row, \
    chessboard, bookshelf

fig(coins(9, groups=[3, 3, 3], labels=['A', 'B', 'C']),
    'Nine coins. Nothing on the outside tells them apart.')
```

Rules:

- **Structure is drawn, objects are emoji.** Lines and boxes carry the geometry
  the solver reasons about; a wolf is a `<text>` emoji. This keeps a figure to a
  few hundred bytes.
- **No colours in the markup** — use the `lg-ln`, `lg-fill`, `lg-lbl` classes.
  The one exception is the chessboard, where colour *is* the argument.
- **Call `fig()` twice**, once per language, around the same SVG — the caption
  is translated, the drawing is not.
- Needing a new shape means **adding a builder to `logic/figures.py`**, never
  inlining raw SVG in a data file, and never adding JavaScript.

---

## 8. Writing the solution

This is the part pupils actually come back for. Format:

```html
<ol class="lg-steps">
  <li>…one move per step, in order…</li>
</ol>
<p class="lg-moral"><strong>The trick:</strong> …</p>
```

- **Steps are moves, not sentences of prose.** Numbered, one action each.
- **Explain the wrong answer** where there is a famous one. "Most people answer
  34 cm and never doubt it" teaches more than the correct calculation does.
- **The `lg-moral` line is compulsory.** Name the transferable idea and say
  where else it turns up: parity, counting outcomes before inventing a method,
  playing against a worst case rather than an average one. One paragraph.
- Where the answer is a bound, **show it is tight** — that the method achieves
  it *and* that nothing better exists.

---

## 9. Both languages, always

Every puzzle ships with `title_uz`, `teaser_uz`, `body_uz`, `hint_uz`,
`answer_hint_uz` and `solution_uz`. The importer **refuses** a puzzle missing
the Uzbek title, body or solution — a half-translated puzzle silently falls back
to English for an Uzbek reader, which is the kind of bug nobody notices for
months.

The Uzbek is a real translation, not a gloss: Latin script with `ʻ` (`oʻ`,
`gʻ`), decimals with a comma (`27,6`), and Uzbek mathematical vocabulary
(*juftlik*, *ehtimol*, *koʻpaytma*, *yigʻindi*). No English words in the Uzbek
column at all.

The interface strings are separate — those go through gettext into
`locale/uz/LC_MESSAGES/django.po`. **Remove the fuzzy flag** on anything you
translate there or Django silently ignores it.

---

## 10. The schedule

Rounds, not hand-written dates:

```python
SCHEDULE = {'start': '2026-07-13 09:00', 'days': 7, 'window': 7}
```

Each puzzle carries `'round': n`; `opens_at` is `start + 7 × (n − 1)` and
`reveal_at` is a week later, so a round is revealed exactly as the next one
opens and there is always precisely one live round. Moving the whole season is
one line. A puzzle may state explicit `opens_at` / `reveal_at`, which win.

When a season runs out, the Arena says "no puzzle is open right now" and the
archive carries the section — so **keep at least four rounds ahead of today**.

---

## 11. The workflow

1. Read this guide and `toc_logic_puzzles.txt`.
2. Find where to continue:
   `LogicPuzzle.objects.order_by('-number').first()`.
3. Write `_puzzles_logic_<range>.py` — `SCHEDULE` (copied unchanged from the
   previous file: one season, one schedule) + `PUZZLES = [...]`, two per round.
4. **Write and run `verify_logic_<range>.py` in the scratchpad. Fix, then
   import.**
5. `python manage.py import_logic <file> --author=prime` (`--republish` to
   overwrite, `--draft` to import unpublished for preview).
6. Mark the range `[done]` in the toc.
7. Give the `railway run python manage.py import_logic …` command for
   production — automatically, every time.

---

## 12. The user's own tips

*(Empty for now — as the user says what they want from these puzzles, write it
here. Anything in this section overrides the generic advice above.)*
