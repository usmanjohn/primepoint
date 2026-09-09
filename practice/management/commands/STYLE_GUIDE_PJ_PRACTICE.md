# Prime Japanese Practices — Writing Guide (for Claude)

How to write the **Prime Japanese practice tests** — one test per lesson, `PJ-1 … PJ-100`,
matched **one-to-one** to the tutorials. The lesson list lives in `toc_pj_practices.txt`.

> Same pupil as the tutorials: an **Uzbek school pupil (11–17)** starting Japanese from
> zero. The test is not a trap — it is the lesson's last page. A pupil who actually read
> `PJ-n` should score 70–90% on practice `n`.

---

## 0. The language rule (same as the tutorials)

**Everything the pupil reads is in Uzbek. Japanese appears only as the material being
tested.** Instructions, questions, choices-that-aren't-Japanese, and every explanation:
Uzbek. **No English anywhere** — not even "Practice" in the title.

This is the opposite of `STYLE_GUIDE_PE_PRACTICE.md`, where explanations are English first
with Uzbek in italics after. Here there is only one language, so **no italic second copy** —
write the explanation once, in Uzbek, properly.

## 1. Title, file, import

- Title: `PJ-7 Mashq: Katakana 1 va ismingizni yozish` — same number, same topic wording as
  the tutorial (drop the tutorial's `PJ-7:` punctuation, keep the words). `Mashq`, not
  `Practice`.
- Every practice carries `"tutorial": "PJ-7:"` — the importer matches that prefix and adds
  the practice to that tutorial's `practices` set, so the lesson page grows a **Mashq**
  button. Never write the whole title there.
- Subject: `日本語`. The batch file's `SUBJECT` dict creates it on first import; copy that
  dict unchanged into every later batch file.
- File: `_practice_pj_<from>_<to>.py`, exposing `SUBJECT = {...}` + `DEFAULTS = {...}` +
  `PRACTICES = [...]`.
- Import: `python manage.py import_practices <file> --master=prime --expect-questions=<n>`
  (local) / `--master=powerty` (production). `--republish` overwrites and rebuilds
  questions. **Always pass `--expect-questions`** — it refuses the file if a test has
  drifted off its length.

## 2. Two test lengths

| Lessons | Questions | Why |
|---|---|---|
| **PJ-1 … PJ-12** (yozuv) | **12** | These teach characters, not grammar. A 20-question kana test is padding. `--expect-questions=12` |
| **PJ-13 … PJ-100** (grammatika) | **20** | Full grammar tests, same ramp as Prime Korean. `--expect-questions=20` |

### Ramp for the script tests (12 questions)

| Q | What it tests |
|---|---|
| 1–3   | **Tanish** — name the character, name its sound, which row (行) it belongs to. Nearly free marks. |
| 4–7   | **Oʻqish** — read a word written in the kana taught so far, or build a word from loose characters. This is the core: the pupil must actually *read*. |
| 8–10  | **Farqlash** — the lesson's own contrast: シ vs ツ, ソ vs ン, さ vs ち, ぬ vs め, は as "ha" vs は as "wa". |
| 11–12 | **Qoʻllash** — spot the wrong reading, or pick the correctly written word. Built from the lesson's `.pe-fix` pairs. |

### Ramp for the grammar tests (20 questions)

| Q | What it tests |
|---|---|
| 1–5   | **Tanish** — the pattern in a short, plain sentence. |
| 6–12  | **Qoʻllash** — the pattern in fuller sentences, plus the lesson's sub-rules (verb group, particle choice, い/な adjective branching, politeness level). |
| 13–16 | **Farqlash** — the pattern against what pupils confuse it with (は vs が, に vs で, たら vs ば vs と, あげる vs くれる). |
| 17–18 | **Xato topish** — "Qaysi gap toʻgʻri?" / "Qaysi gapda xato bor?", from the lesson's `.pe-fix` pairs. |
| 19–20 | **Tuzish** — word order (Japanese is SOV — put the verb last), or a two-line dialogue where the pupil picks the natural reply. |

## 3. Rules that hold for every question

- **4 choices**, exactly one correct, short and parallel in shape. Never one long option
  among three tiny ones.
- **Distractors must be the real mistakes an Uzbek pupil makes**:
  シ/ツ and ソ/ン flipped, つ read as "tu" instead of "tsu", ふ read as "hu", the ん before
  a b/p read as "n" instead of "m", は read as "ha" when it is the topic particle,
  を read as "wo" instead of "o", the wrong verb group (帰る treated as 一段), を where に
  belongs, a な-adjective conjugated as an い-adjective (きれいくない), a sentence with the
  verb in the Uzbek/Russian middle position. Never nonsense syllables as filler.
- **Never cite a choice by letter or position in an explanation.**
  `PracticeQuestion.display_choices()` shuffles the choices with a seed from the question
  id, so "javob B" is meaningless — the pupil's order is not the file's order. Quote the
  choice's own **text** in `<strong>` instead. (For the same reason you need not bother
  spreading the key over positions 1–4 in the source: the shuffle already does it.)
- **Nothing from a later lesson.** `PJ-20` may not test the て-shakli. Recycling **earlier**
  lessons is welcome and good.
- **Furigana in every question that contains a kanji**, exactly as in the tutorials — a
  pupil must never be blocked by a character rather than by the grammar. The one exception
  is a question whose *point* is the reading; there the choices carry the readings.
- Romaji follows the tutorial policy: fine through PJ-12, rare to PJ-20, gone from PJ-21.
- Japanese punctuation: 。 、 「」 — never . , "".

## 4. Question HTML

Plain tags only — this renders inside CKEditor fields:

```python
{
    "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>ふじさん</strong></p>",
    "choices": ["hujisan", "fujisan", "huzisan", "fudzisan"],
    "correct": "fujisan",
    "explanation": "<p><strong>fujisan</strong> toʻgʻri. ふ — yaponchada oddiy "
                   "«hu» ham, «fu» ham emas: lablar deyarli tegmaydi, shamdagi "
                   "olovni puflagandek chiqadi. Hepburn yozuvida u <strong>fu</strong> "
                   "deb yoziladi. じ esa «ji» — «zi» emas.</p>",
},
```

- Line 1 of `text` is the **instruction** in Uzbek — `Toʻgʻri javobni tanlang.` /
  `Bu soʻz qanday oʻqiladi?` / `Qaysi belgi?` / `Qaysi gap toʻgʻri?` /
  `Boʻsh joyga nima tushadi?`
- Line 2 is the **item**, in `<strong>`, with `___` for a gap.
- Allowed tags: `<p> <strong> <em> <br> <ul> <li> <ruby> <rt>`. No `<script>`, no
  `pe-*`/`pj-*` classes — those belong to the tutorials. `<ruby>` is allowed **because
  furigana is not decoration on this course**; it is how the sentence is legible at all.
- Dialogues: one `<p>` per turn — `<p><strong>A:</strong> …</p><p><strong>B:</strong> ___</p>`.
  Japanese has no 가/나 convention; A/B is fine, or use two names (田中 / ゆき).

## 5. Explanations

One paragraph, Uzbek, and it must **teach**, not just announce:

1. Name the answer in `<strong>` and say **why** it is right, quoting the rule the tutorial
   used — repeating the lesson's own wording is the whole point of a matched practice.
2. When a distractor is genuinely tempting, add a clause on why it is wrong
   ("ツ emas — シ ning chiziqlari yon tomondan, ツ niki tepadan tushadi").
   Do this for at least the harder half of the test.
3. Name the Japanese term when the lesson named it (助詞, 五段, て形, 尊敬語) — the pupil
   should leave the test knowing what to call the thing.

## 6. The user's own tips

*(Empty for now — when the user shares how they want these tested, it goes here and
overrides the generic advice above.)*

---

## How to ask

- **"Make the practices for PJ-13 … PJ-15"** — Claude checks the toc, writes the batch
  file, imports it with the right `--expect-questions`, and gives the Railway command.
- Normal rhythm is **3 lessons at a time, all three legs together**: tutorial → practice →
  reading. See the Prime Japanese section of `CLAUDE.md`.
