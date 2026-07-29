# Prime English — Writing Guide (for Claude)

How to write the **Prime English** grammar tutorials (`PE-1 …`). This guide replaces the
generic `STYLE_GUIDE.md` for this subject — the lesson list lives in `toc_prime_english.txt`.

> The pupil is an **Uzbek school pupil (11–17)** whose English is anywhere from zero to
> intermediate. Write like a favourite teacher: warm, plain, concrete, never professorial.
> English is the main language; Uzbek carries the hard moments.

---

## 1. Title, file, import

- Title: `PE-7: There is / There are` — prefix `PE`, number from the toc, exact topic name.
- Category: `english`. Every lesson also carries `"order": <lesson number>` — that is its
  position inside the **Prime English** playlist.
- File: `_tutorials_prime_english_<from>_<to>.py`, exposing `PLAYLIST = {...}` +
  `TUTORIALS = [...]`. Copy the `PLAYLIST` dict unchanged into every batch file — the
  importer creates it once and reuses it.
- Import: `python manage.py import_tutorials <file> --author=prime` (local) /
  `--author=powerty` (production). Add `--republish` to overwrite.

## 2. The shape of a lesson

Always in this order:

1. `<h2>PE-7: There is / There are</h2>`
2. **Hook** — 1–2 sentences that make the pupil *want* this grammar. Use a real situation
   ("You are describing your room to a friend…"), never "In this lesson we will study…".
3. `<div class="pe-goal">` — 3–4 checkmarked things they will be able to do.
4. **The pattern** — a `<div class="pe-formula">` strip, immediately after the goals.
5. **Body** — small `<h3>` sections, easy → harder. Each new idea gets an example
   (`.pe-ex`) with the Uzbek translation under it.
6. **Common mistakes** — `<h3>` + `.pe-fix` wrong/right pairs (at least 3 pairs).
7. **Practice** — `<h3>Practice</h3>` + at least **4** `.pe-quiz` items with hidden answers.
8. **Key words — Kalit soʻzlar** — `<ul class="pe-gloss">`, 8–10 terms.
9. `<div class="pe-recap">` — the takeaway list. This is the last thing in the content.

### Depth bar (do not write thin lessons)

- **900–1200 words** of real explanation (batch 1 sits at 1050–1225).
- **At least 3 `.pe-ex` example blocks**, every one carrying its Uzbek translation, plus
  further examples inside `.pe-vs` / `.pe-grid` / tables.
- **5 practice questions**, every answer explained (not just the key).
- **At least 3 Uzbek callouts** (`.pe-uz`) at the genuinely hard moments — not everywhere.
  The best ones contrast the two languages ("Uzbek keeps the noun singular after a number,
  English does not"), because that is where pupils actually go wrong.
- Explain the **why** ("*is* goes with one thing because…"), not only the rule.

## 3. Uzbek policy

English is the teaching language; Uzbek is the safety net.

- Every example sentence gets its Uzbek translation in `.pe-ex__uz`.
- The 4+ `.pe-uz` callouts explain the *idea* in Uzbek — where Uzbek grammar works
  differently, that is exactly where a callout belongs (articles, word order, perfect
  tenses, phrasal verbs…).
- Use `oʻ` and `gʻ` (with the ʻ mark), not `o'`/`g'` or `ў`.
- The glossary is always English term → Uzbek.

## 4. The component kit (`pe-*`, defined in `static/css/style.css`)

Pure CSS — **no `<script>`, ever**. Everything below is mobile-friendly already.

### Lesson goals
```html
<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul><li>…</li><li>…</li></ul>
</div>
```

### Pattern strip — the signature visual of Prime English
Colour-coded sentence roles. Use it for every structure you teach.
```html
<div class="pe-formula">
  <span class="pe-formula__label">Positive sentence</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb + s</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">object</span>
  <span class="pe-chip pe-chip--opt">(place / time)</span>
</div>
```
Chips: `--s` subject (blue) · `--v` verb (green) · `--o` object (orange) ·
`--aux` auxiliary (purple) · `--neg` negative (red) · `--adv` adverbial (teal) ·
`--opt` optional (dashed outline).

### Example sentence
The same colours highlight the words inside the sentence, so the pattern and the example
teach each other. Add a `.pe-legend` once, the first time colours appear in a lesson.
```html
<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">My sister</span>
     <span class="pe-hl pe-hl--v">works</span>
     <span class="pe-hl pe-hl--o">in a hospital</span>.</p>
  <p class="pe-ex__uz">Opam kasalxonada ishlaydi.</p>
  <p class="pe-ex__why">Optional: one line on why this form is used.</p>
</div>
```

### Callouts
```html
<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>…</div>
<div class="pe-call pe-rule"><span class="pe-call__t">Rule</span>…</div>
<div class="pe-call pe-tip"><span class="pe-call__t">Teacher's tip</span>…</div>
<div class="pe-call pe-warn"><span class="pe-call__t">Careful</span>…</div>
```

### Wrong → right
```html
<div class="pe-fix">
  <p class="pe-bad">She <s>go</s> to school every day.</p>
  <p class="pe-good">She <b>goes</b> to school every day.</p>
</div>
```

### Tense timeline
`left`/`width` are percentages of the track, set inline.
```html
<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:62%"></span>
    <span class="pe-tl-band" style="left:8%;width:48%"></span>
    <span class="pe-tl-dot" style="left:30%"></span>
    <span class="pe-tl-tag" style="left:30%">I lived here</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>
```

### Comparison, mini-cards, steps
```html
<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">Present Simple</p>…</div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">Present Continuous</p>…</div>
</div>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Habits</p>
    <p>I <em>drink</em> tea every morning.</p></div>
</div>

<ol class="pe-steps"><li>Find the subject.</li><li>…</li></ol>
```

### Practice (tap to reveal)
```html
<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Ali <span class="pe-blank">?</span> (play) football on Sundays.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a"><p><strong>plays</strong> — "Ali" is one person (he), so the
    verb takes <b>-s</b>. <em>(Oʻzbekcha: uchinchi shaxs birlikda -s qoʻshiladi.)</em></p></div>
  </details>
</div>
```
Inline reveal inside a sentence: `<details class="pe-peek"><summary>?</summary><span
class="pe-peek__a">goes</span></details>`.

### Glossary and recap
```html
<ul class="pe-gloss">
  <li><b>Subject</b><span>ega</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul><li>…</li></ul>
</div>
```

### Tables
Avoid tables where a `.pe-grid` or `.pe-vs` reads better. If a table is truly clearest
(irregular verbs, tense map), wrap it: `<div class="pe-table-wrap"><table>…</table></div>`.

## 5. Hard rules

- **No `<script>`, no `onclick`, no inline JS.** Interactivity = `<details>` only.
- Inline `style=` only for timeline positions (`left`, `width`). Everything else uses the
  kit classes, so the lessons restyle with the site.
- No LaTeX. Real symbols and `<sup>`/`<sub>` if ever needed.
- Never use a class that is not in this guide — add it to the CSS kit first.
- `summary` field (≤300 chars): one sentence, what the pupil will be able to do.
- Keep every lesson self-contained: a pupil landing on PE-40 from search still gets the
  pattern strip, examples and practice without reading PE-1.

## 6. The user's own tips

*(Empty for now — when the user shares how they want the grammar taught, it goes here and
overrides the generic advice above.)*

---

## How to ask

- **"Make the next 5 Prime English tutorials"** — Claude checks the highest `PE-` number,
  continues in toc order, writes the batch file, imports it, and gives the Railway command.
- **"Redo PE-3"** — rewrite that one with `--republish`.
