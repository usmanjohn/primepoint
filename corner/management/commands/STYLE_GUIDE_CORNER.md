# Corner Story Writing Guide (for Claude)

This guide tells Claude HOW to write **Corner** stories (the resource library at `/corner/`).
Each collection has its own table-of-contents file (e.g. `toc_keimyung_korean.txt`) listing
the stories in order. **Always follow that order.**

> ⚠️ **This guide is written in English for Claude, but the STORIES YOU PRODUCE MUST BE IN
> THE TARGET LANGUAGE + UZBEK — never English.** For Korean collections: story text in
> Korean (한글), all translations/summaries in **Uzbek**. The audience is young Uzbek
> students. Goal: *yoshlar uchun oʻqishni qiziqarli qilamiz!*

The data model: a story is a single `body` HTML field. Vocabulary is marked **inline** in
the body; the word list and the end-of-story flashcards are generated automatically from
those marks — you never write a separate glossary.

---

## 1. The vocabulary mark (MOST IMPORTANT)

Mark key words exactly like this:

```html
<span class="cn-word" data-tr="doʻst">친구</span>
```

- `data-tr` = the **Uzbek** translation (short: 1–4 words). Never English.
- The visible text = the word as it appears in the sentence (particles attached are fine:
  `친구를` is OK — but prefer marking the dictionary form when natural).
- **8–15 marks per story.** Mark each word only the FIRST time it appears.
- Never nest other tags inside a `cn-word` span, and never split one across tags.
- Do not use double quotes inside `data-tr` (use commas: `data-tr="uy, xona"`).

Everything else about the word list is automatic: readers tap a highlighted word to see
the translation, and the same words become flip-flashcards under the story.

## 2. Story structure & length

- `title`: in the target language (e.g. Korean), as listed in the toc file.
- `summary`: 1 sentence in **Uzbek** — shown on the story card (≤300 chars).
- `body`: plain `<p>` paragraphs. Aim for **300–600 words** of story text
  (beginner collections may be shorter; keep the level of the collection consistent).
- Start the body directly with the first `<p>` — do NOT repeat the title as a heading
  (the page already shows it).
- Dialogue is welcome: keep each speaker's line in its own `<p>` (or use `<br>`).
- Optionally end with 1–3 comprehension questions as plain text in a styled box
  (see palette below) — questions in the target language, no answers needed.

## 3. Allowed HTML palette

The reader page has warm "paper" styling of its own — keep markup light:

- `<p>` — paragraphs (the default building block)
- `<br>` — line breaks inside dialogue
- `<strong>` / `<em>` — sparing emphasis
- `<span class="cn-word" data-tr="...">...</span>` — vocabulary (section 1)
- One optional callout box at the end (e.g. comprehension questions):

```html
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>❓ Savollar:</strong>
  <br>1. ...koreyscha savol...?
  <br>2. ...koreyscha savol...?
</div>
```

Do NOT use `<h1>`–`<h3>`, tables, images, or scripts inside the body.

## 4. Level & tone

- Match the collection's level (a beginner reader = short sentences, high-frequency
  vocabulary, present/past tense; an intermediate reader = longer, richer text).
- Stories should be warm, concrete and a little fun — daily life, small surprises,
  friendship, food, travel. Give characters names.
- Reuse marked vocabulary later in the story where natural — repetition teaches.

## 5. Data file shape

Write batches into `corner/management/commands/_stories_<collection>_<range>.py`:

```python
SUBJECT    = {...}   # copy from the toc header / previous batch
COLLECTION = {...}   # copy from the toc header / previous batch
STORIES    = [{"title": ..., "summary": ..., "order": N, "body": ...}, ...]
```

`order` = the story's number in the toc file. Import with:

```
python manage.py import_corner corner/management/commands/_stories_<...>.py --author=<AUTHOR>
```

(`--republish` overwrites existing stories and rebuilds their word lists.)

## 6. The user's own tips

(Once the user shares preferences for stories — level, themes, vocab count — record them
here. Their tips override the generic advice above.)
