# Study abroad ("Xorijda oʻqish") — style guide

Read before adding or updating anything in `abroad`. Toc: `toc_abroad.txt`.

## 0. The one rule: never a confident wrong date
A pupil plans a year around a date. So:
- **Every date, amount and eligibility rule comes from the official source** (the scholarship's
  own site or its official announcement/guidelines PDF), read with WebSearch/WebFetch *on the day*.
  Secondary blogs are for finding the official page, never for the fact itself.
- Every `Scholarship` and `Deadline` carries `official_url`/`source_url` (https) and
  `last_checked`. The importer refuses one without them.
- A date not yet announced is `is_estimate: True` with a note saying what it is based on
  ("2026: 12–25 February"). Estimates never count down — the chip says *expected around*.
- A fact older than a year turns into "check the date on the official site" automatically.
- If sources disagree (e.g. the renamed apostille agency), say only what they agree on.
- No agency recommendations, no promised outcomes, no fee figures without a source. Never say
  Powerty is free (see the hand-out rule).

## 1. "Update the abroad deadlines"
1. `python manage.py abroad_check` — lists CLOSED (add the next cycle), ESTIM (confirm when
   announced) and STALE facts, each with the URL to re-read.
2. Research each from the official page. PDFs: WebFetch saves the binary; extract text with
   `pymupdf` (installed) and read the schedule, eligibility and benefits sections.
3. Edit the data file (`DEADLINES`, `last_checked`, the GKS body if rules changed), run the
   fact gate, `import_abroad <file> --author=prime --republish`, append the same line with
   `--author=powerty` to `temporary.txt`.

## 2. Language
Content is bilingual **in the data** (`title` / `title_uz`, …), like the Logic Arena — every
visible field has both. Uzbek is the default. Uzbek uses `ʻ` (oʻ, gʻ) and `ʼ`, never Cyrillic
(the fact gate checks). Sample *letters* stay in English (that is what gets submitted); their
margin notes and planner prompts are bilingual. Interface chrome is gettext.

## 3. Voice
A well-informed older sibling: direct, specific, calm. Short paragraphs, tables for comparisons,
the callouts for the three things a pupil must not miss:
`ab-tip` (a move), `ab-mistake` (a trap), `ab-uz` (what it means for a pupil in Uzbekistan),
`ab-fact` (an official rule worth quoting). `ab-steps` for ordered lists, `ab-toc` for long pages,
`ab-src` for the source line. Never invent an `ab-*` class — add it to the STUDY ABROAD section of
`style.css` first.

## 4. Samples
Fictional applicants only (Madina, Jasur…), clearly stamped "do not copy". A letter is written
in the language it is submitted in — usually English; set `letter_lang` (e.g. `"uz"` for the
El-Yurt Umidi essay) so the page marks it correctly. One `<p>` per
paragraph in `letter`; each note names its paragraph (`para`, 1-based). **A heading (`<h4>`)
is not a paragraph** — it is shown with the `<p>` after it, so count only `<p>`s. The importer
refuses a note that points past the last paragraph (it would never be shown). Every sample has a
planner (`prompts`, 4–6 questions, `lines` for writing space). The notes explain *why* a
paragraph works — structure, evidence, reflection — never just "good".

## 5. Universities
Only universities on the scholarship's official list, with that list's grouping (GKS Type A/B).
A rank only with `rank_label` + `rank_source` and a year. Strengths: one modest, true line.

## 6. The fact gate (throwaway, scratchpad `verify_abroad.py`)
Runs the importer's `validate()`, then checks balanced tags, no undefined `ab-*` class, no
`<script>`/`style=`, no Cyrillic inside `_uz` fields, a source on every deadline. Also fetch
every new official URL once — `curl` is bot-blocked by several (Chevening, DAAD, Campus China),
so confirm those with WebFetch or a search result instead.

## 7. The user's own tips
(none yet)
