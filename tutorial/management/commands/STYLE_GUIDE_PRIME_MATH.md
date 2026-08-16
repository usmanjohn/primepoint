# Prime Math — Writing Guide (for Claude)

How to write the **Prime Math** lessons (`PM-1 …`). This guide replaces `STYLE_GUIDE.md`
(that one is for the English-language SAT tutorials), `STYLE_GUIDE_PRIME_ENGLISH.md`,
`STYLE_GUIDE_PRIME_KOREAN.md` and `STYLE_GUIDE_PRIME_RUSSIAN.md` for this subject — the
lesson list lives in `toc_prime_math.txt`.

> The pupil is an **Uzbek school pupil (11–16)** whose maths is anywhere from shaky to
> good, sitting somewhere between 5-sinf and 9-sinf. Write like a favourite teacher: warm,
> plain, concrete, never professorial. Show the *why* before the rule.

---

## 0. The language rule

**Prime Math teaches in Uzbek.** Like Prime Korean and Prime Russian, and unlike Prime
English.

- **Every explanation, heading, instruction, hint and answer key is in Uzbek.**
- **No English in the running text.** Not in headings, not in the examples, not in the
  callouts.
- **One exception, and only one:** the `pe-gloss` key-words list at the end of each lesson
  gives the English equivalent beside the Uzbek term — `<li><b>Kasr</b><span>ulush;
  ingl. fraction</span></li>`. That is the bridge to the SAT Math course (`SAT-1 …`),
  which is written in English. Nowhere else.
- Terms: Uzbek word first. If the school textbook's Russian term is genuinely more familiar
  (*razryad*, *proporsiya*), the Uzbek word already **is** that word — use it and move on;
  do not print Cyrillic.

## 0.1 What this course must do that a textbook does not

1. **Explain the why.** A pupil who knows *why* you flip the second fraction when dividing
   never forgets it. A pupil who memorised "flip and multiply" forgets it in a month. Every
   rule in this course gets a reason, a picture, or both.
2. **Never leave a rule as a naked formula.** Show it working, in a `pm-solve` ladder where
   every line says *what was done and why*.
3. **Always land in the real world.** Every lesson has **at least one matnli masala** — a
   word problem — no matter what the topic is. This is the user's own requirement: pupils
   who can compute but cannot read a problem fail every exam that matters. Bozor, taksi
   narxi, telefon tarifi, dala, sinf, futbol, tugʻilgan kun, remont, non, choy.
4. **Refuse to be scary.** No wall of symbols. Short sentences. One idea per paragraph.
   `pm-est` ("javob mantiqiymi?") teaches the habit of estimating before computing — the
   single most useful exam skill there is.

## 0.2 Where Uzbek pupils actually go wrong — put a `.pe-uz` callout there

- **Amallar tartibi** — `2 + 3 × 4` read left to right.
- **Manfiy ishoralar** — `−3 − 5`, `−2 × (−4)`, minus in front of a bracket.
- **Foizning asosi** — 20% ошиб, keyin 20% kamaysa, boshlangʻich songa qaytmaydi.
- **Kasr qoʻshish** — maxrajlarni ham qoʻshib yuborish.
- **Birliklar** — km/soat va m/sekund, sm² va m², minut va soat aralashib ketishi.
- **"necha marta" va "nechtaga koʻp"** — koʻpaytirish bilan qoʻshish adashadi. This one is
  a *language* mistake, not a maths mistake, which is exactly why it belongs in this course.

## 1. Title, file, import

- Title: `PM-23: Sonning foizini topish` — prefix `PM`, number from the toc, exact topic
  wording from the toc.
- Category: `math`. Every lesson also carries `"order": <lesson number>` — its position
  inside the **Prime Math** playlist.
- File: `_tutorials_prime_math_<from>_<to>.py`, exposing `PLAYLIST = {...}` +
  `TUTORIALS = [...]`. Copy the `PLAYLIST` dict unchanged into every batch file — the
  importer creates it once and reuses it.
- Import: `python manage.py import_tutorials <file> --author=prime` (local) /
  `--author=powerty` (production). Add `--republish` to overwrite.
- `summary` (≤300 chars): one Uzbek sentence — what the pupil will be able to do.
- `"stories": ["<reading title>"]` links the lesson to its Corner reading; add it before
  `"content"` and re-run the import with `--republish` once the story exists.

## 2. The shape of a lesson

Always in this order:

1. `<h2>PM-23: Sonning foizini topish</h2>`
2. **Ilgak (hook)** — 1–2 Uzbek sentences with a real situation that needs this maths.
   Never "Bu darsda biz … oʻrganamiz".
3. `<div class="pe-goal">` — 3–4 checkmarked Uzbek lines ("Bu darsda siz…").
4. **Qoida / formula** — a `<div class="pe-formula">` strip right after the goals.
5. **Asosiy qism** — small `<h3>` sections, oson → qiyin. Every new idea gets a worked
   example in a `pm-solve` ladder or a `pe-ex` block with `pe-ex__math`.
6. **Matnli masala** — `<h3>Matnli masala</h3>`, at least one, fully worked: the text, then
   *what is asked*, then the plan, then the ladder, then `pm-check`.
7. **Koʻp uchraydigan xatolar** — `<h3>` + at least **3** `.pe-fix` wrong/right pairs.
8. **Mashq** — `<h3>Mashq</h3>` + at least **5** `.pe-quiz` items with hidden answers.
   The last one is always a word problem.
9. **Kalit soʻzlar** — `<ul class="pe-gloss">`, 8–10 terms, English equivalent included.
10. `<div class="pe-recap">` — the takeaway list. Last thing in the content.

### Depth bar (do not write thin lessons)

- **900–1200 words** of real Uzbek explanation.
- **At least 3 fully worked examples**, oson → oʻrta → qiyin, every step justified in the
  `pm-solve__why` column. Never jump two steps at once.
- **At least 1 matnli masala** worked end to end (section 6 above), plus one in the practice.
- **5 practice questions**, every answer explained — the reasoning, not just the number.
- **At least 3 `.pe-uz` callouts** at the genuinely hard moments (see 0.2).
- **At least 1 picture** wherever the idea is visual: `pm-num`, `pm-model`, `pm-fig` (SVG),
  `pm-col`. Geometry lessons: an SVG figure is compulsory.

## 3. Maths as HTML — never LaTeX

The editor has no formula support. Raw LaTeX (`$\frac{a}{b}$`, `x^2`) renders as literal
ugly text. Write maths as clean HTML:

| Kerak | Yozing | Emas |
|---|---|---|
| daraja | `x<sup>2</sup>`, `10<sup>−3</sup>` | `x^2` |
| indeks | `x<sub>1</sub>` | `x_1` |
| koʻpaytirish | `3 × 4`, `3·a` | `3*4` |
| boʻlish | `12 ÷ 4`, or a `pm-frac` | `12/4` in display maths |
| kasr (inline) | `pm-frac` (see kit) or `3/4` in plain running text | LaTeX |
| ildiz | `√49` inline; `<span class="pm-root">49</span>` when the bar matters (it draws the √ *and* the overline itself — do not type √ inside it) | `sqrt(49)` |
| taqqoslash | `≤ ≥ ≠ ≈ ±` | `<=`, `>=`, `!=` |
| boshqa | `π ° ∞ → ∠ △ ⊥ ∥ ° %` | ASCII imitations |

Decimal separator: **vergul** (`3,5`) — that is how Uzbek school maths writes it. Thousands
get a thin space or nothing (`240 000 soʻm`). Be consistent inside a lesson.

## 4. Figures — inline SVG, never an image file

Lesson bodies render through `|safe`, so an inline `<svg>` works and needs no JavaScript and
no upload. Rules:

- Always `viewBox="0 0 320 200"`-style with **no fixed width/height** — `.pm-fig svg` makes
  it responsive.
- Use the helper classes so the drawing follows the site's light/dark theme; never hardcode
  `stroke="black"`:
  `class="pm-ln"` (chiziq) · `pm-ln--dash` (yordamchi chiziq) · `pm-ln--hl` (asosiy, rangli) ·
  `pm-fill` (shakl ichi) · `pm-fill--hl` (boʻrttirilgan yuza) · `pm-pt` (nuqta) ·
  `pm-lbl` (yozuv) · `pm-lbl--hl` (muhim yozuv).
- Label everything the text mentions. A figure whose sides are not named teaches nothing.
- One idea per figure. Two small figures beat one crowded one.

```html
<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img" aria-label="Toʻgʻri burchakli uchburchak">
    <polygon class="pm-fill" points="40,170 240,170 40,50"/>
    <polyline class="pm-ln" points="40,50 40,170 240,170" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="40" y1="50" x2="240" y2="170"/>
    <rect class="pm-ln" x="40" y="150" width="20" height="20" fill="none"/>
    <text class="pm-lbl" x="25" y="115">a = 3</text>
    <text class="pm-lbl" x="130" y="190">b = 4</text>
    <text class="pm-lbl pm-lbl--hl" x="150" y="100">c = ?</text>
  </svg>
  <figcaption>Katetlar 3 va 4, gipotenuza nomaʼlum.</figcaption>
</figure>
```

## 5. The component kit

Prime Math **reuses the whole `pe-*` kit** documented in `STYLE_GUIDE_PRIME_ENGLISH.md`
section 4 — `pe-goal`, `pe-formula` + `pe-chip`, `pe-ex`, `pe-call` (`pe-uz` / `pe-rule` /
`pe-tip` / `pe-warn`), `pe-fix`, `pe-vs`, `pe-grid`, `pe-steps`, `pe-quiz` + `pe-reveal` +
`pe-blank` + `pe-peek`, `pe-gloss`, `pe-recap`, `pe-table-wrap`, `pe-badge`, `pe-legend`.
Do not re-invent any of those.

On top of them, the **PRIME MATH** section at the bottom of `static/css/style.css` adds the
pieces maths needs. Everything is pure CSS.

### Solving ladder — the workhorse of this course
Left column = the line of maths, right column = **why that line happened**. Never write a
solution as a paragraph when it can be a ladder.
```html
<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 5 = 20</span>
    <span class="pm-solve__why">Berilgan tenglama</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x = 15</span>
    <span class="pm-solve__why">Ikki tomondan 5 ni ayirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 5</span>
    <span class="pm-solve__why">Ikki tomonni 3 ga boʻldik</span>
  </div>
</div>
```

### Wrong ✗ / right ✓ pair — with the reason line
The language courses put a bare `.pe-bad` / `.pe-good` pair inside `.pe-fix`. Maths needs a
third line: **why** the wrong line is wrong. Use the maths variant — the same red/green
chips plus a muted reason line — and always fill the `__why`:
```html
<div class="pe-fix">
  <p class="pe-fix__bad">240 ning 30% i = 240 ÷ 30 = 8</p>
  <p class="pe-fix__good">240 ning 30% i = 240 × 0,3 = 72</p>
  <p class="pe-fix__why">Foizga boʻlingan. Boʻlish faqat <b>100</b> ga qilinadi.</p>
</div>
```

### Fraction, written properly
```html
<span class="pm-frac"><span class="pm-frac__n">3</span><span class="pm-frac__d">4</span></span>
<span class="pm-frac pm-frac--big">…</span>   <!-- display size, inside pe-formula -->
```

### Example with an expression line
`.pe-ex__math` is the maths line; `.pe-ex__uz` reads it out in words — the habit that makes
word problems possible.
```html
<div class="pe-ex">
  <p class="pe-ex__math">240 000 × 0,3 = 72 000</p>
  <p class="pe-ex__uz">240 000 soʻmning 30 foizi — 72 000 soʻm.</p>
  <p class="pe-ex__why">Ixtiyoriy: nega aynan shunday hisoblandi.</p>
</div>
```

### Number line
`left` / `width` are percentages of the track, set inline — the only place inline `style=`
is allowed in this course (same exception as `pe-timeline`).
```html
<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:50%;width:30%"></span>
    <span class="pm-num__tick" style="left:0%"><i>−4</i></span>
    <span class="pm-num__tick" style="left:50%"><i>0</i></span>
    <span class="pm-num__tick" style="left:100%"><i>4</i></span>
    <span class="pm-num__dot" style="left:65%"><i>x</i></span>
  </div>
</div>
```

### Column arithmetic
```html
<table class="pm-col">
  <tr class="pm-col__carry"><td></td><td>1</td><td></td></tr>
  <tr><td></td><td>4</td><td>7</td></tr>
  <tr class="pm-col__op"><td>+</td><td>2</td><td>8</td></tr>
  <tr class="pm-col__res"><td></td><td>7</td><td>5</td></tr>
</table>
```

### Bar model — seeing a word problem
The picture that turns "Jasur Afsonadan 2 marta koʻp yigʻdi" into an equation.
```html
<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Afsona</span>
    <span class="pm-model__bar" style="width:30%">x</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Jasur</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:60%">2x</span>
  </div>
  <p class="pm-model__tot">Jami: x + 2x = 120</p>
</div>
```

### Word → symbol table — the signature piece of the text side
Use it in every lesson of Block G, and whenever a new phrase appears.
```html
<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Matnda shunday deyiladi</th><th>Matematikada</th><th>Misol</th></tr>
  <tr><td>…dan 5 ta koʻp</td><td class="pm-word__sym">+ 5</td><td>x + 5</td></tr>
  <tr><td>…dan 3 marta koʻp</td><td class="pm-word__sym">× 3</td><td>3x</td></tr>
  <tr><td>…dan kam emas</td><td class="pm-word__sym">≥</td><td>x ≥ 12</td></tr>
</table></div>
```

### Check and estimate
```html
<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>3 × 5 + 5 = 20 ✓ — javob toʻgʻri.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>198 × 4 ≈ 200 × 4 = 800. Javob 800 atrofida boʻlishi kerak.</span>
</div>
```

### Diagrammalar (Blok F, PM-75…84)

Charts are inline SVG inside a `.pm-fig`, using the `pm-ch__*` classes. **The colour
rules below are computed, not chosen — do not "improve" them by hand.**

- **Ustunli (bar) va chiziqli (line) — one series, one colour.** Every bar is
  `.pm-ch__bar` (the same blue). The bar's *length* already encodes the number;
  colouring bars by their value spends the identity channel on something the length
  already says, and forces a legend nobody needs. Use `.pm-ch__bar--hl` for **one**
  bar only, when the text singles that bar out.
- **Doiraviy (pie) — one hue, four ordinal steps.** Slices are sorted **largest
  first** and take `.pm-ch__s1 … .pm-ch__s4` in that order. Four different *hues*
  were rejected: under protanopia/deuteranopia four hues do not all stay apart, and
  the A5 printed book is greyscale — lightness survives both. Max 4 slices; a fifth
  category folds into "boshqalar".
- **Every bar and every slice is directly labelled** (`.pm-ch__lbl` for the name,
  `.pm-ch__val` for the number). Colour is never the only thing telling two marks
  apart, so no chart here needs a legend box.
- **Reference lines** (`.pm-ch__ref`) mark a *statistic* over the data — the mean, the
  median. They are deliberately not the series colour and not solid: they are a comment on
  the data, not data. Put the label where no bar value can reach it — above the plot when
  the bars are tall, on the left when they are short. Two reference lines close together
  (mean vs median) get staggered heights, never the same y.
- **Dot plots** (a `.pm-ch__ax` axis with `.pm-ch__dot` circles stacked at repeated values)
  are the right form for showing *spread*, and the only honest way to draw two datasets
  with the same mean side by side. Give each row ≥ 92px so the lower row's labels clear the
  upper row's tick numbers.
- **No dual axis, ever.** Two quantities with different scales = two diagrams.
- Axis `.pm-ch__ax`, gridlines `.pm-ch__grid` (recessive — the data is the loudest
  thing on the page). Label text uses text colours, never the series colour.
- Bar chart geometry: bars anchored on the baseline, a gap of roughly a third of the
  bar width between them, and the value written above the bar.

```html
<figure class="pm-fig">
  <svg viewBox="0 0 320 210" role="img" aria-label="Sevimli meva — ustunli diagramma">
    <line class="pm-ch__grid" x1="46" y1="40" x2="300" y2="40"/>
    <line class="pm-ch__ax" x1="46" y1="160" x2="300" y2="160"/>
    <rect class="pm-ch__bar" x="60" y="80" width="38" height="80"/>
    <text class="pm-ch__val" x="70" y="72">8</text>
    <text class="pm-ch__lbl" x="62" y="176">olma</text>
  </svg>
  <figcaption>20 oʻquvchidan 8 tasi olmani tanladi.</figcaption>
</figure>
```

⚠️ Pie slices are **generated**, never hand-typed: an arc path whose angles are
wrong is a lying figure. Use the batch's `gen_pm<range>.py` and let
`verify_pm_<range>.py` re-measure every slice angle back to the data
(`ulush ÷ jami × 360°`, and the four angles must sum to exactly 360).

### Colour meanings on this course
`pe-chip--s` / `pe-hl--s` = **nomaʼlum (x)** · `--o` = **berilgan son** · `--v` = **amal** ·
`--aux` = **birlik (kg, km, soʻm)** · `--neg` = **manfiy yoki xato** · `--adv` = **shart** ·
`--opt` = ixtiyoriy qism. Drop a `.pe-legend` once, the first time colours appear.

## 6. Hard rules

- **No `<script>`, no `onclick`, no inline JS.** Interactivity = `<details>` only.
- Inline `style=` only for `pm-num` / `pm-model` positions and widths.
- **No English** outside the `pe-gloss` list. No LaTeX. No Cyrillic.
- Never use a class that is not in this guide or the Prime English one — add it to the
  **PRIME MATH** CSS section and to this guide first.
- **Every number must be right.** See section 7 — this is the rule that matters most.
- Nothing from a later lesson. PM-30 may not use foiz (PM-23) if the toc puts it later than
  the lesson you are writing; check `toc_prime_math.txt` before reaching for a tool.
  Recycling **earlier** lessons is welcome and good.
- Keep every lesson self-contained: a pupil landing on PM-64 from search still gets the
  rule, the worked examples and the practice without reading PM-1.

## 7. The arithmetic gate — the rule that matters most

A wrong answer key is the worst bug this course can ship. A pupil who trusts us and gets a
wrong "correct answer" loses more than a lesson.

1. Work every example twice, the second time by a different route (or by substituting the
   answer back — that is what `pm-check` is for).
2. Before importing a batch, write a throwaway script in the scratchpad
   (`verify_pm_<range>.py`) that recomputes **every** numeric answer in the tutorials, the
   practice and the readings, and prints a line per mismatch. Run it. Fix, then import.
3. Numbers in a story must be internally consistent — prices, distances, times, totals.
4. Distractors in the practice are the **real** mistakes (see 0.2), never random numbers,
   and every distractor must be *reachable* by a specific wrong move you can name in the
   explanation.

## 8. Relationship to the rest of the site

- **`tutorial` SAT-… ** = SAT Math prep, in English, exam-shaped. Prime Math is the school
  course underneath it; a pupil who finishes PM-100 is ready for SAT-1.
- **Math Championship** (`/games/championship/`) = auto-generated 5–7-sinf quiz. Fun and
  fast; no explanations. Prime Math is where the explanation lives.
- **`corner` "Prime Math Readings"** = the third leg of every lesson (see
  `corner/management/commands/toc_prime_math_readings.txt`).
- **`corner` "Matematika olami"** = the free shelf: mathematicians, puzzles, popular
  science. Attached to no lesson (see `toc_matematika_olami.txt`).
- **`practice` "Matematika"** = this course's tests, one per lesson, plus the older
  standalone mixed math tests, which stay as they are.

## 9. The user's own tips

*(Empty for now — when the user shares how they want maths taught, it goes here and
overrides the generic advice above.)*

---

## How to ask

- **"Make the next 3 Prime Math lessons"** — Claude checks the highest `PM-` number,
  continues in toc order, writes the tutorial + practice + reading batch, verifies the
  arithmetic, imports, and gives the Railway commands.
- The working rhythm is **3 lessons at a time, all three legs together**.
- **"Redo PM-7"** — rewrite that one with `--republish`.
