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
<span class="cn-word" data-pos="verb" data-tr="uchrashmoq">만나다</span>
```

- `data-tr` = the **Uzbek** translation (short: 1–4 words). Never English.
- `data-pos` = the part of speech, which **colour-codes** the highlight. Use one of:
  - `verb` — 동사 (green)      → the biggest group; verbs carry the meaning.
  - `adj`  — 형용사 (blue)     → descriptive words (예쁘다, 급하다, 다양하다).
  - `adv`  — 부사 (purple)     → adverbs & manner words (마침내, 흔히, 재빨리, 제법).
  - **omit `data-pos` entirely** for anything else — nouns, idioms, set expressions
    (they keep the neutral amber highlight). The reader page shows this as "Expression".
- The visible text = the word as it appears in the sentence (particles attached are fine:
  `친구를` is OK — but prefer marking the dictionary form when natural).
- **30–40 marks per story**, and **focus on TOPIK-relevant words: verbs, adjectives,
  adverbs.** Avoid translating plain nouns — mark a noun only when it is a key TOPIK word
  or genuinely aids comprehension, and leave its `data-pos` off. Roughly aim for a mix like
  ~half verbs, and the rest split between adverbs, adjectives, and a few neutral nouns.
- Mark each word only the FIRST time it appears.
- Never nest other tags inside a `cn-word` span, and never split one across tags.
- Do not use double quotes inside `data-tr` or `data-pos` (use commas: `data-tr="uy, xona"`).

Everything else about the word list is automatic: readers tap a highlighted word to see
the translation, the highlight colour shows its part of speech (with a legend at the top),
and the same words become colour-tagged flip-flashcards under the story.

## 2. Story structure & length

- `title`: in the target language (e.g. Korean), as listed in the toc file.
- `summary`: 1 sentence in **Uzbek** — shown on the story card (≤300 chars).
- `body`: plain `<p>` paragraphs. Aim for **300–600 words** of story text
  (beginner collections may be shorter; keep the level of the collection consistent).
- Start the body directly with the first `<p>` — do NOT repeat the title as a heading
  (the page already shows it).
- Dialogue is welcome: keep each speaker's line in its own `<p>` (or use `<br>`).
- End with **2–3 comprehension questions** — but author these as structured data in the
  `questions` list (section 5b), NOT as text in the body. They render as interactive,
  self-grading MCQs under the story.

## 3. Allowed HTML palette

The reader page has warm "paper" styling of its own — keep markup light:

- `<p>` — paragraphs (the default building block)
- `<br>` — line breaks inside dialogue
- `<strong>` / `<em>` — sparing emphasis
- `<span class="cn-word" data-pos="..." data-tr="...">...</span>` — vocabulary (section 1)
- One optional callout box for a short note / cultural tip (NOT for questions — those are
  structured data now, see section 5b):

```html
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Eslatma:</strong> ...qisqa madaniy izoh...
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
STORIES    = [{"title": ..., "summary": ..., "order": N, "body": ..., "questions": [...]}, ...]
```

`order` = the story's number in the toc file.

### 5b. The `questions` list (comprehension MCQs)

Each story SHOULD carry 2–3 questions. Each is a dict:

```python
"questions": [
    {
        "text":        "이 글의 중심 생각은 무엇입니까?",   # question in the target language
        "choices":     ["...", "...", "..."],              # 3 choices (2–4 allowed)
        "answer":      1,                                   # 0-based index of the correct one
        "explanation": "Nega toʻgʻri ekanini oʻzbekcha izohlang.",  # Uzbek, shown after answering
    },
    ...
]
```

Rules:
- Questions in the **target language** (Korean); the `explanation` in **Uzbek**.
- Make them **inference / logical** questions — the answer should be *reasoned* from the
  story (main idea, cause, character's motive, "what is true according to the text"), not a
  word-lookup. This is the TOPIK reading skill we are training.
- Keep exactly one clearly-correct choice; make the distractors plausible but refutable
  from the text. The explanation should say why the right answer is right AND briefly why
  the tempting wrong ones fail.
- The whole `questions` list is rebuilt on every `--republish`, so it is safe to edit.

Import with:

```
python manage.py import_corner corner/management/commands/_stories_<...>.py --author=<AUTHOR>
```

(`--republish` overwrites existing stories and rebuilds their word lists.)

## 6. The user's own tips

(Once the user shares preferences for stories — level, themes, vocab count — record them
here. Their tips override the generic advice above.)
