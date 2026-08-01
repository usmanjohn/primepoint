# Prime Korean Practices — Writing Guide (for Claude)

How to write the **Prime Korean practice tests** — one test per lesson, `PK-1 … PK-100`,
matched **one-to-one** to the tutorials. The lesson list lives in `toc_pk_practices.txt`.

> Same pupil as the tutorials: an **Uzbek school pupil (11–17)** starting Korean from zero.
> The test is not a trap — it is the lesson's last page. A pupil who actually read `PK-n`
> should score 70–90% on practice `n`.

---

## 0. The language rule (same as the tutorials)

**Everything the pupil reads is in Uzbek. Korean appears only as the material being
tested.** Instructions, questions, choices-that-aren't-Korean, and every explanation:
Uzbek. **No English anywhere** — not even "Practice" in the title.

This is the opposite of `STYLE_GUIDE_PE_PRACTICE.md`, where explanations are English first
with Uzbek in italics after. Here there is only one language, so **no italic second copy** —
write the explanation once, in Uzbek, properly.

## 1. Title, file, import

- Title: `PK-7 Mashq: Boʻgʻin bloklari va 받침` — same number, same topic wording as the
  tutorial (drop the tutorial's `PK-7:` punctuation, keep the words). `Mashq`, not
  `Practice`.
- Every practice carries `"tutorial": "PK-7:"` — the importer matches that prefix and adds
  the practice to that tutorial's `practices` set, so the lesson page grows a **Practice**
  button. Never write the whole title there.
- Subject: `한국어` — the practice Subject that already exists. Do not create a new one.
- File: `_practice_pk_<from>_<to>.py`, exposing `SUBJECT = {...}` + `DEFAULTS = {...}` +
  `PRACTICES = [...]`. Copy `SUBJECT` and `DEFAULTS` unchanged into every batch file.
- Import: `python manage.py import_practices <file> --master=prime --expect-questions=<n>`
  (local) / `--master=powerty` (production). `--republish` overwrites and rebuilds
  questions. **Always pass `--expect-questions`** — it refuses the file if a test has
  drifted off its length.

## 2. Two test lengths

| Lessons | Questions | Why |
|---|---|---|
| **PK-1 … PK-8** (Hangul) | **12** | These teach letters, not grammar. There is less to drill, and a 20-question alphabet test is padding. `--expect-questions=12` |
| **PK-9 … PK-100** (grammar) | **20** | Full grammar tests, same ramp as Prime English. `--expect-questions=20` |

### Ramp for the Hangul tests (12 questions)

| Q | What it tests |
|---|---|
| 1–3   | **Tanish** — name the letter, name its sound, which row it belongs to. Nearly free marks. |
| 4–7   | **Oʻqish** — read a block, split a block into 초성/중성/종성, build a block from letters. This is the core: the pupil must actually *read*. |
| 8–10  | **Farqlash** — the lesson's own contrast: ㅓ vs ㅗ, 달/탈/딸, ㅅ vs ㅆ, which 받침 sound. |
| 11–12 | **Qoʻllash** — spot the wrong reading, or pick the correctly written word. Built from the lesson's `.pe-fix` pairs. |

### Ramp for the grammar tests (20 questions)

| Q | What it tests |
|---|---|
| 1–5   | **Tanish** — the pattern in a short, plain sentence. |
| 6–12  | **Qoʻllash** — the pattern in fuller sentences, plus the lesson's sub-rules (받침 branching, irregular stems, question/negative forms). |
| 13–16 | **Farqlash** — the pattern against what pupils confuse it with (은/는 vs 이/가, 에 vs 에서, (으)니까 vs 기 때문에). |
| 17–18 | **Xato topish** — "Qaysi gap toʻgʻri?" / "Qaysi gapda xato bor?", from the lesson's `.pe-fix` pairs. |
| 19–20 | **Tuzish** — word order (Korean is SOV — put the verb last), or a two-line dialogue where the pupil picks the natural reply. |

## 3. Rules that hold for every question

- **4 choices**, exactly one correct, short and parallel in shape. Never one long option
  among three tiny ones.
- **Distractors must be the real mistakes an Uzbek pupil makes**: 어/오 mixed up, ㅡ read
  as ㅣ, 받침 released ("pabı"), 입니다 read as "ip-ni-da", the wrong side of the 받침
  fork (학교은 instead of 학교는), Uzbek word order with the verb in the middle. Never
  nonsense syllables as filler.
- **Vary the correct letter** — spread the answer roughly evenly over positions 1–4.
- **Nothing from a later lesson.** `PK-12` may not test 았/었어요. Recycling **earlier**
  lessons is welcome and good.
- Romanisation in questions follows the tutorial policy: fine through PK-8, rare to PK-16,
  gone from PK-17.

## 4. Question HTML

Plain tags only — this renders inside CKEditor fields:

```python
{
    "text": "<p>Bu boʻgʻin qanday oʻqiladi?</p><p><strong>학교</strong></p>",
    "choices": ["[학교]", "[학꾜]", "[하교]", "[학교오]"],
    "correct": "[학꾜]",
    "explanation": "<p><strong>[학꾜]</strong> toʻgʻri. Toʻxtovchi 받침 (ㄱ) dan keyin "
                   "kelgan oddiy undosh qattiqlashadi — bu <strong>경음화</strong>. "
                   "Tomoq 받침da tarang qolgani uchun keyingi ㄱ oʻz-oʻzidan ㄲ boʻlib "
                   "chiqadi.</p>",
},
```

- Line 1 of `text` is the **instruction** in Uzbek — `Toʻgʻri javobni tanlang.` /
  `Bu soʻz qanday oʻqiladi?` / `Qaysi harf?` / `Qaysi gap toʻgʻri?` /
  `Boʻsh joyga nima tushadi?`
- Line 2 is the **item**, in `<strong>`, with `___` for a gap.
- Allowed tags: `<p> <strong> <em> <br> <ul> <li>`. No `<script>`, no `pe-*`/`pk-*`
  classes — those belong to the tutorials.
- Dialogues: one `<p>` per turn — `<p><strong>가:</strong> …</p><p><strong>나:</strong> ___</p>`
  (Korean uses 가/나, not A/B).

## 5. Explanations

One paragraph, Uzbek, and it must **teach**, not just announce:

1. Name the answer in `<strong>` and say **why** it is right, quoting the rule the tutorial
   used — repeating the lesson's own wording is the whole point of a matched practice.
2. When a distractor is genuinely tempting, add a clause on why it is wrong
   ("어 emas — u yerda lablar yoyilgan"). Do this for at least the harder half of the test.
3. Name the Korean term when the lesson named it (연음화, 받침, 경음화) — the pupil should
   leave the test knowing what to call the thing.

## 6. The user's own tips

*(Empty for now — when the user shares how they want these tested, it goes here and
overrides the generic advice above.)*

---

## How to ask

- **"Make the practices for PK-9 … PK-11"** — Claude checks the toc, writes the batch file,
  imports it with the right `--expect-questions`, and gives the Railway command.
- Normal rhythm is **3 lessons at a time, all three legs together**: tutorial → practice →
  reading. See the Prime Korean section of `CLAUDE.md`.
