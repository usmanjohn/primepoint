# Tutorial Writing Guide (for Claude)

This guide tells Claude HOW to write tutorials. It is the same for every subject.
Each subject has its own table-of-contents file (e.g. `toc_sat_math.txt`) that lists
the topics and the order. **Always follow the table of contents order.**

> You (the user) do NOT need to repeat these rules each time. Just say which subject
> and how many to create (see "How to ask" at the bottom).

---

## 1. Title format

Every tutorial title MUST start with the subject prefix and its number, then the topic:

```
SAT-1: Introduction to the Variable and Combining Like Terms
SAT-2: Solving Single-Variable Linear Equations
```

- The prefix and category come from the top of each table-of-contents file.
- The number = the lesson number from the table of contents (so order is always kept).
- This number prefix is also how Claude knows where to continue next time.

## 2. Structure of each tutorial (the `content` HTML)

Write in this order, every time:

1. **Heading** — `<h2>SAT-1: Introduction to the Variable...</h2>`
2. **Description** — a short 1–2 sentence intro of what the lesson covers.
3. **Body** — explain the concept clearly, step by step, from easy to harder.
4. **Summary** — ALWAYS end with a `<h3>Summary</h3>` and the key points as a list.

### Depth & length (minimum bar — do NOT write thin lessons)

Each tutorial must be **detailed and thorough**, not a quick summary. Concretely, every tutorial's
`content` must have:

- **At least ~600 words** of real explanation (aim 600–900). Explain the *why*, not just the *how*;
  add a "common mistakes" or "why this works" note where it helps.
- **At least 3 fully worked examples**, going from easy → medium → harder (an SAT-style one).
  Show every step, not just the answer.
- **At least 2 practice questions**, each in its own `<details><summary>Show answer</summary>…</details>`
  with the full reasoning revealed (not just the final number).
- The 3–4 Uzbek explanations and the glossary from section 5 (these are on top of the above).

Prefer more, smaller `<h3>` sections (concept → method → examples → common mistakes → practice) so
the lesson is easy to follow. When in doubt, explain more, not less.

## 3. Tools to make it high quality (use a mix, not all at once)

- **Highlights** for key terms: `<mark>important idea</mark>`
- **Colored emphasis**: `<strong>`, `<em>`, `<u>`
- **Quote boxes** for rules/tips: `<blockquote>Rule: ...</blockquote>`
- **Comparisons** (e.g. "Parallel vs Perpendicular"): use two short lists or a quote box.
- **Use cases / real-world examples**: short, relatable.
- **Worked examples**: show the problem, then the steps, then the answer.
- **Practice question + answer + explanation**: question, then reveal the answer with
  the reasoning. Use `<details><summary>Show answer</summary>...</details>` so students
  can think first.
- **Lists**: `<ul>` / `<ol>` for steps.

## 4. Math — VERY IMPORTANT

The editor has **no LaTeX / equation support**. Never write raw LaTeX like `$\frac{a}{b}$`
or `x^2` — it would show as ugly literal text. Write math as clean HTML instead:

- Powers: `x<sup>2</sup>`, `a<sup>n</sup>`
- Subscripts: `y<sub>2</sub>`, `x<sub>1</sub>`
- Fractions inline: write as `(y₂ − y₁) / (x₂ − x₁)` or use words; for display, a small
  styled line is fine.
- Use real symbols: × ÷ √ ≤ ≥ ≠ ± π ° ∞ → … (not `*`, `<=`, `sqrt`).
- Slope example done right:
  `<p>Slope <em>m</em> = (y<sub>2</sub> − y<sub>1</sub>) / (x<sub>2</sub> − x<sub>1</sub>)</p>`

## 5. Uzbek

Keep English as the **main** language, but every tutorial must include real Uzbek support:

1. **At least 3–4 short Uzbek explanations** spread across the key/hard parts (not everywhere).
   Put them inline right after the English idea, in italics:
   `<p>The slope tells you steepness. <em>(Oʻzbekcha: nishablik chiziqning qiyaligini bildiradi.)</em></p>`
2. **A "Key words — Kalit soʻzlar" glossary** near the end (just before the Summary) with
   **at least 8–9 key English terms translated to Uzbek**. Use this format:
   ```
   <h3>Key words — Kalit soʻzlar</h3>
   <ul>
     <li><strong>Coefficient</strong> — koeffitsiyent</li>
     <li><strong>Quadratic</strong> — kvadrat tenglama</li>
     ...
   </ul>
   ```
   Pick the terms that actually appear in that lesson so the glossary is useful.

## 6. Tables

**Avoid tables when possible** (not strict). Prefer lists, quote boxes, and comparisons.
Use a table only if it is truly the clearest way.

## 7. The `summary` field (separate from content)

The import data also has a short `summary` field (max 300 chars). This is the small blurb
shown on the listing card. Write one clear sentence describing the lesson.

---

## How to ask (what the user types)

Just say, for example:

- **"Make the next 5 SAT tutorials"** — Claude checks which SAT numbers already exist,
  continues in order, writes the batch, and imports them.
- **"Make SAT 1 to 10"** — Claude does that exact range.
- **"Redo SAT-7"** — Claude rewrites that one (with `--republish`).

Claude will: read this guide → read the subject's `toc_*.txt` → check the database for the
highest number already done → write the next batch into a `_tutorials_*.py` file → run
`python manage.py import_tutorials <file> --author=<username>`.
