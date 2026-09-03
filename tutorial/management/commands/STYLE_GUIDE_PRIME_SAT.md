# Prime SAT Math — Writing Guide (for Claude)

How to write the **Prime SAT Math** lessons (`SAT-1 … SAT-100`). This guide replaces the
old `STYLE_GUIDE.md` for this subject — that one described the first, thinner generation of
SAT tutorials, written in English with a few Uzbek asides and no practice attached. Those
same 100 titles are now being **rewritten** on the Prime machinery. The lesson list lives in
`toc_prime_sat_math.txt`.

> The pupil is an **Uzbek pupil, 15–18**, aiming at a university that reads SAT scores.
> Their maths is usually better than their score suggests. What actually costs them points
> is the **English sentence** wrapped around the maths, the clock, and the four answer
> choices that were designed by people who knew exactly which mistake they would make.
> Write like a coach who has sat the test: warm, specific, unhurried in the explanation and
> ruthless about the clock.

---

## 0. THE LANGUAGE RULE — the one that defines this course

**The exam speaks English. The teacher speaks Uzbek.** Prime SAT is the only bilingual
course on the site, and the split is not decorative — it is the whole pedagogy.

**In English, always, word for word as the test would print it:**
- the lesson **title** (`SAT-7: Slope-Intercept Form (y = mx + b) in Depth`);
- every **exam question stem** and its four **answer choices** inside `.ps-stem`;
- the **mathematical vocabulary** being taught (*slope*, *y-intercept*, *constant term*),
  which is then glossed in Uzbek the first time it appears;
- the phrases in a `.ps-phrase` book.

**In Uzbek, always:**
- every `<h3>` heading, every sentence of explanation, every hint;
- the reasoning inside `.ps-sol__body`, every `pm-solve__why` line;
- every callout (`pe-uz`, `pe-tip`, `pe-warn`), `.ps-tactic`, `.ps-trap`, `.ps-desmos__read`;
- the `summary`, the `pe-recap`, and every explanation in the practice test
  (the practice's *questions* are exam questions, so they are in English — see
  `practice/management/commands/STYLE_GUIDE_PS_PRACTICE.md`).

**Never** translate an exam stem into Uzbek and leave it at that. The pupil must meet the
English sentence, then be *walked through it* in Uzbek. A lesson whose questions are in
Uzbek has removed the exact difficulty the pupil is paying us to remove.

> Rule of thumb: if the sentence would appear on a real test paper, it is in English.
> If it is a human being explaining something to a nervous teenager, it is in Uzbek.

### 0.1 Numbers are written the American way — everywhere

This is the **one place Prime SAT deliberately contradicts Prime Math**, and lessons must
not drift:

| | Prime SAT (this course) | Prime Math |
|---|---|---|
| decimal | `3.5`, `0.375` | `3,5` |
| thousands | `1,200` or `1200` | `1 200` |
| money | `$45` | `45 000 soʻm` |

Reason: a pupil who types `3,5` into a grid-in loses the mark. The comma habit has to be
broken *inside the course*, not on test day. So Uzbek sentences in this course also write
`3.5` — the number belongs to the exam, not to the language around it. Say so out loud in
`SAT-1` and again in `SAT-90` (the grid-in lesson).

## 0.2 The facts about the test — get these right, every time

The digital SAT (Bluebook app). Do not print anything that contradicts this:

- **Math section = 2 modules × 22 questions × 35 minutes** (70 minutes, 44 questions).
- Module 2 is **adaptive**: it gets harder or easier depending on Module 1. Both count.
- **~75% multiple choice (4 choices), ~25% student-produced response (grid-in).**
- **Desmos graphing calculator is built into the app** and allowed on the whole Math
  section. A pupil may also bring their own approved calculator.
- A **reference sheet** (areas, volumes, special right triangles, circle facts, 360° = 2π)
  is on screen the whole time. Teach *what it does not contain* — slope, quadratic formula,
  averages, probability, the ones they must actually know.
- **No penalty for a wrong answer.** Never leave a blank. Say this often.
- Math scaled score **200–800**.
- The four content domains and their weight — a lesson may name its own domain:
  **Algebra ≈ 35%** · **Advanced Math ≈ 35%** · **Problem-Solving and Data Analysis ≈ 15%**
  · **Geometry and Trigonometry ≈ 15%**.
- Pacing target: **~95 seconds per question**. Put a realistic `.ps-time` on worked
  examples — 30–45 s for a routine one, 2 minutes for a hard multi-step one.

## 0.3 Where an Uzbek pupil actually loses SAT points — put a `.pe-uz` callout there

These are the recurring ones. Every lesson should hit at least three, chosen honestly for
its own topic:

- **The sentence, not the sum.** *must be true* vs *could be true*; *in terms of x*;
  *which of the following is equivalent*; *not*, *except*, *least*, *greatest*.
- **Answering the wrong question.** Solving for `x` when the question asked for `x + 4`, or
  for the *number of* when it asked for the *cost of*. This is the single biggest source of
  lost marks and the reason `.ps-trap` exists.
- **Percent language.** *increased by 20%* vs *increased to 20%*; two successive changes;
  *what percent of what*.
- **Units.** minutes vs hours, feet vs inches, per hour vs per minute — the SAT switches
  units inside the sentence on purpose.
- **The decimal comma** (0.1 above) and writing a fraction as a mixed number.
- **Interpretation questions.** *What does the 12 represent in the context?* — an Uzbek
  pupil who computes perfectly can still miss every one of these.
- **Trusting the picture.** SAT figures are drawn to scale *unless it says otherwise*;
  when it says "Note: Figure not drawn to scale", eyeballing becomes a trap.

## 1. Title, file, import

- Title: `SAT-7: Slope-Intercept Form (y = mx + b) in Depth` — prefix `SAT`, the number from
  the toc, the topic wording **exactly** as the toc prints it, in English.
  ⚠️ The title is how the importer finds the old lesson to overwrite. **Do not reword a
  title**, or you create a duplicate instead of upgrading the lesson.
- Category: `math`. Every lesson carries `"order": <lesson number>` — its place in the
  **Prime SAT Math** playlist.
- File: `_tutorials_prime_sat_<from>_<to>.py`, exposing `PLAYLIST = {...}` +
  `TUTORIALS = [...]`. Copy the `PLAYLIST` dict unchanged into every batch file.
- Import: `python manage.py import_tutorials <file> --author=prime --republish` (local) /
  `--author=powerty --republish` (production). **`--republish` is not optional here** — the
  old-generation lesson already exists under that title and must be overwritten.
- `summary` (≤300 chars): one **Uzbek** sentence — what the pupil will be able to do on test
  day. Not a topic label.
- `"practices": ["SAT-7 Practice:"]` is **not** used — the practice file links itself to the
  lesson through its own `"tutorial": "SAT-7:"` key. Leave `practices` out.

## 2. The shape of a lesson

Always in this order:

1. `<h2>SAT-7: Slope-Intercept Form (y = mx + b) in Depth</h2>` (English, from the toc)
2. **Ilgak** — 1–2 Uzbek sentences putting this idea on the test: where it shows up, how
   many questions it is worth, what it looks like. Never "Bu darsda biz … oʻrganamiz".
3. `<div class="pe-goal">` — 3–4 checkmarked **Uzbek** lines ("Bu darsdan keyin siz…"),
   with the English term in brackets where it is the term being learned.
4. **Qoida / formula** — a `<div class="pe-formula">` strip, the formula in symbols with an
   English label.
5. **Asosiy qism** — small Uzbek `<h3>` sections, oson → qiyin. Every new idea gets a
   `pm-solve` ladder or a `pe-ex` with `pe-ex__math`.
6. **Exam English** — a `<ul class="ps-phrase">` with 4–6 real phrasings this topic is asked
   in, each with its Uzbek meaning. Compulsory from `SAT-3` onward.
7. **SAT savoli** — at least **two** `.ps-stem` cards, in English, answer inside `.ps-sol`.
   The first is routine, the second is the hard version the test actually asks. At least one
   `.ps-time`.
8. **Taktika** — one `.ps-tactic`: the move, not the maths. From `SAT-83` on, a `.ps-desmos`
   block whenever Desmos genuinely beats hand algebra.
9. **Tuzoq javoblar** — at least **2** `.ps-trap` blocks naming the planted wrong answers,
   plus at least 2 `.pe-fix` wrong/right pairs with a filled `pe-fix__why`.
10. **Mashq** — `<h3>Mashq</h3>` + at least **5** `.pe-quiz` items with hidden answers.
    Stems in English, explanations in Uzbek. The last one is a word problem or a grid-in.
11. **Key words** — `<ul class="pe-gloss">`, 8–10 entries, **English term first**, Uzbek
    meaning second (`<li><b>slope</b><span>qiyalik; chiziq qanchalik tik</span></li>`).
    This is the mirror image of Prime Math's gloss, on purpose.
12. `<div class="pe-recap">` — Uzbek takeaways. Last thing in the content.

### Depth bar (do not write thin lessons)

- **900–1300 words** of real Uzbek explanation (the English stems do not count).
- **At least 3 fully worked examples**, oson → oʻrta → SAT-qiyin, every step justified in
  the `pm-solve__why` column.
- **At least 2 `.ps-stem` exam questions** with full Uzbek reasoning in the reveal.
- **At least 2 `.ps-trap`** blocks and **2 `.pe-fix`** pairs.
- **At least 3 `.pe-uz` callouts** at the genuinely hard moments (0.3).
- **5 `.pe-quiz`** questions, every answer explained — the reasoning, not the number.
- **At least 1 picture** wherever the idea is visual (`pm-fig` SVG, `pm-num`, `pm-model`).
  Geometry and graph lessons: an SVG figure is compulsory.

## 3. Maths as HTML — never LaTeX

Same rules as Prime Math (`STYLE_GUIDE_PRIME_MATH.md` §3): `x<sup>2</sup>`, `x<sub>1</sub>`,
`3 × 4`, `√49` or `<span class="pm-root">49</span>`, `≤ ≥ ≠ ≈ ± π ° ∞ → ∠ △ ⊥ ∥`, real
fractions with `pm-frac`. **No LaTeX, ever** — the editor has no formula support and `$x^2$`
renders as literal ugly text. Numbers follow §0.1 (decimal point, comma thousands).

## 4. Figures — inline SVG, never an image file

Same as Prime Math (`STYLE_GUIDE_PRIME_MATH.md` §4): responsive `viewBox`, no fixed
width/height, and the theme-aware helper classes `pm-ln` / `pm-ln--dash` / `pm-ln--hl` /
`pm-fill` / `pm-fill--hl` / `pm-pt` / `pm-lbl` / `pm-lbl--hl`. Label everything the text
mentions.

**One SAT-only addition:** when the real test would print *"Note: Figure not drawn to
scale"*, print it too, in English, in the `figcaption` — and then teach what changes.

A figure that belongs to an exam question goes **inside** `.ps-stem__q`, before the choices.

## 5. The component kit

Prime SAT **reuses the whole `pe-*` kit** (`STYLE_GUIDE_PRIME_ENGLISH.md` §4) and the whole
`pm-*` maths kit (`STYLE_GUIDE_PRIME_MATH.md` §5) — `pe-goal`, `pe-formula` + `pe-chip`,
`pe-ex` + `pe-ex__math`, `pe-call` (`pe-uz` / `pe-rule` / `pe-tip` / `pe-warn`), `pe-fix`,
`pe-vs`, `pe-grid`, `pe-steps`, `pe-quiz` + `pe-reveal`, `pe-gloss`, `pe-recap`,
`pe-table-wrap`, `pm-solve`, `pm-frac`, `pm-root`, `pm-num`, `pm-model`, `pm-fig`,
`pm-check`, `pm-est`, `pm-word`. **Do not re-invent any of those.**

On top of them, the **PRIME SAT** section at the bottom of `static/css/style.css` adds the
six pieces an exam course needs. All pure CSS.

### The exam question — the signature visual
English inside the card, Uzbek inside the reveal. The `A) B) C) D)` letters are drawn by
CSS, so never type them.
```html
<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If 3<i>x</i> + 7 = 22, what is the value of <i>x</i> + 4?</p>
  </div>
  <ol class="ps-ch">
    <li>5</li>
    <li>9</li>
    <li>15</li>
    <li>19</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: B) 9</p>
      <div class="pm-solve">…</div>
      <p>Savol <b>x</b> ni emas, <b>x + 4</b> ni soʻradi — shuning uchun 5 javob emas.</p>
    </div>
  </details>
</div>
```
Add `class="ps-ch--key"` to the correct `<li>` **only** in a worked example that reveals the
answer immediately — never on a question the pupil is meant to try.

### Tactic — the move, not the maths
```html
<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Javoblar son boʻlsa, ularni tenglamaga qoʻyib koʻring…</p>
  <ol><li>…</li><li>…</li></ol>
</div>
```

### Trap — the planted wrong answer
Name the value, then name the mistake that produces it. One block per trap.
```html
<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">5</span>
  <span class="ps-trap__why">Bu — <b>x</b> ning qiymati. Savol esa <b>x + 4</b> ni
  soʻradi. Test har doim yarim yoʻlda toʻxtagan javobni ham qoʻyadi.</span>
</div>
```

### Desmos — the keystrokes, typed exactly
`__keys` are the literal keystrokes (English/symbols), `__read` says in Uzbek what to read
off the screen.
```html
<div class="ps-desmos">
  <p class="ps-desmos__t">Desmos bilan</p>
  <ol class="ps-desmos__keys">
    <li>y = 3x + 7</li>
    <li>y = 22</li>
  </ol>
  <p class="ps-desmos__read">Ikki chiziq kesishgan nuqtani bosing: (5, 22). Demak x = 5.</p>
</div>
```

### Grid-in — the answer box
```html
<figure class="ps-gridin ps-gridin--ok">
  <span class="ps-gridin__boxes"><span>3</span><span>/</span><span>2</span></span>
  <figcaption>Toʻgʻri: 3/2 yoki 1.5 — ikkalasi ham qabul qilinadi.</figcaption>
</figure>
```
`--ok` green, `--no` red (show the rejected form beside the accepted one).

### Phrase book — exam English → what it is asking
```html
<ul class="ps-phrase">
  <li><b>in terms of x</b><span>javob x orqali ifodalansin — son emas, ifoda</span></li>
  <li><b>which must be true</b><span>har doim toʻgʻri — bitta qarshi misol yetarli</span></li>
</ul>
```

## 6. Hard rules

- **No JavaScript.** Ever. Every interaction is `<details>` or `:hover`.
- **Never invent a `ps-*` class** without first adding it to the PRIME SAT section of
  `static/css/style.css` and to §5 of this guide.
- **No inline `style=`**, except the percentage positions on `pm-num` / `pe-timeline`.
- No `<img>`. Figures are inline SVG.
- No Cyrillic, no Korean, no LaTeX.
- Titles are never reworded (§1).
- Every English stem is a *grammatical, natural* exam sentence. If it reads like a
  translation, rewrite it. Italicise variables (`<i>x</i>`) inside English prose, as the
  test does.

## 7. ⚠️ THE ANSWER GATE — the rule that matters most

A wrong answer key is the worst bug this course can ship: the pupil trusts it against their
own correct work. Prime Math's arithmetic gate applies here **and is extended**, because an
SAT question can be wrong in a second way — the English can admit two answers.

Before importing a batch, write a throwaway script in the scratchpad,
`verify_sat_<range>.py`, that:

1. **Recomputes every numeric answer independently** — every `.ps-stem`, every `.pe-quiz`,
   every worked example's final line, and all 20 questions of each practice — and prints any
   mismatch. Derive it a *different way* than the lesson does (solve it with `sympy`, brute
   force over a range, or an explicit formula), never by copying the lesson's own steps.
2. **Checks every distractor is distinct from the key** and that no two choices are equal.
3. **Checks the trap values are reachable** — a `.ps-trap__val` must be a number some named
   wrong move actually produces.

Then read each English stem once more and ask: *could a careful reader defend a second
answer?* Ambiguity is a bug. Fix, then import.

## 8. The user's own tips

*(Empty for now — the user's own SAT teaching tips go here as they share them, and they
override the generic advice above.)*

---

## How to ask

> "make the next 5 Prime SAT lessons"

Claude then: reads this guide → reads `toc_prime_sat_math.txt` → finds where to continue →
writes `_tutorials_prime_sat_<range>.py` **and** `_practice_ps_<range>.py` → runs the answer
gate → imports both → marks the range `[done]` in both tocs → prints the two
`railway run python manage.py …` commands for production.
