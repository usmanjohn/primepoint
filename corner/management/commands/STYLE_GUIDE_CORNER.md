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
- Also give each story a short **grammar** list (section 5c) — the intermediate/advanced
  patterns that actually appear in the text. Like vocab and questions, this is structured
  data, never body text; it renders as its own styled section between the flashcards and
  the quiz.

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
STORIES    = [{"title": ..., "summary": ..., "order": N, "body": ...,
               "grammar": [...], "questions": [...]}, ...]
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

### 5c. The `grammar` list (grammar points)

Each story carries a short list of the grammar patterns that appear in its text. Each is a dict:

```python
"grammar": [
    {
        "pattern":  "-길래",                                  # the grammar form
        "meaning":  "sabab/asos: bir narsani koʻrib/eshitib, shunga asoslanib ish qildim.",
        "examples": [
            "날씨가 좋길래 산책을 나갔다.",                     # Korean example
            "친구가 맛있다고 하길래 저도 시켰어요.",
        ],
    },
    ...
]
```

Rules:
- **Pick real patterns from THIS text** — the grammar a reader actually meets in the passage,
  not a generic list. Write the `pattern` in Korean (dictionary form of the ending/expression,
  with a leading `-` for verb/adjective endings: `-는 바람에`, `-을 뿐만 아니라`, `-더라도`).
- **Level: intermediate/advanced only (TOPIK II).** Skip beginner grammar (`-아요/어요`, `-고
  싶다`, `-았/었-`). Choose the ones that are genuinely worth a note.
- `meaning` = a **short Uzbek** explanation (1–2 sentences: what it means + when it's used).
- `examples` = **1–2 short Korean example sentences** that show the pattern in use (fresh
  sentences are fine; they don't have to be lifted verbatim from the story).
- **How many:** longer readings → **3–4** grammar points; short passages → **1–2**.
- **Bold the pattern in the body.** Wrap the grammar phrase where it appears in the story in
  `<strong>…</strong>` so the reader can find it easily and connect it to this list (e.g. a
  story whose grammar is `whereas (contrast)` has `…a woody trunk, <strong>whereas</strong>
  the banana plant…` in its body). Keep the `<strong>` on the *structural* words of the
  pattern, and **do not vocab-mark those same words** — a `cn-word` span and a `<strong>` must
  not overlap (never nest tags inside a `cn-word` span). Mark vocab on *other* words.
- The whole `grammar` list is rebuilt on every `--republish`, so it is safe to edit.

Import with:

```
python manage.py import_corner corner/management/commands/_stories_<...>.py --author=<AUTHOR>
```

(`--republish` overwrites existing stories and rebuilds their word lists.)

## 5d. Proverb stories (속담 collections)

The `속담 이야기 (Koreys maqollari)` collection: **one story = one proverb**, title = the
proverb itself. Body structure (all Korean, Uzbek glosses via cn-word as usual):

1. **Emoji banner** — the visual placeholder until a real image is uploaded. First element
   of the body; 2–4 emoji that "draw" the proverb:
   ```html
   <div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🐒 🌳 💥</div>
   ```
2. **The proverb + literal meaning** — quote it in a `<p>`, explain word-for-word what it
   paints.
3. **뜻 (real meaning)** — when Koreans actually say it.
4. **유래 / 이야기** — the origin story if it has an accessible one (우물 안 개구리 → 장자);
   otherwise a short everyday mini-story showing the situation. This is the heart — tell it
   warmly, like the other corner stories.
5. **Dialogue** — 2–4 lines of natural usage.
6. **Uzbek-equivalent callout** — the standard amber box, giving the closest Uzbek proverb:
   ```html
   <div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
     <strong>💡 Oʻzbekchada:</strong> «Otning toʻrt oyogʻi ham qoqiladi» — ...
   </div>
   ```

Counts: ~200–350 Korean words → **12–18 vocab marks**, **2 grammar points**, **2–3 questions**
(meaning / when-to-use / origin inference).

**Images.** `Story.image` (added July 2026) renders above the body in the reader. Two ways
to attach: per-story in the admin (Image section), or in bulk with
`python manage.py import_corner_images <folder> --collection="<exact title>"` where files
are named by story order (`1.png`, `2.jpg`, `3_원숭이.webp`). The emoji banner stays as
decoration either way — remove it from the body only if it clashes with the image.

## 6. The user's own tips

(These override the generic advice above.)

- **Grammar section is expected.** Every story should surface the not-beginner grammar the
  reader meets in the text, with a **short Uzbek explanation and 1–2 examples** each — see 5c.
- **Vocab & grammar counts depend on length:**
  - *Full readings* (the long Keimyung passages): the usual ~30–40 vocab marks, and
    **3–4 grammar** points.
  - *Short passages* (the `keimyung_short_story.txt` collection — a few sentences each):
    keep it light — **5–10 vocab marks** and **1–2 grammar** points. Don't over-mark a
    short text.
