# Prime Korean Workbook — style guide (the fourth leg, "Ish daftari")

Read this before writing a batch. Toc: `toc_pk_workbook.txt`. Pilot: `_workbook_prime_korean_01_09_10.py`
— copy its shape.

## 0. Why this leg exists
The tutorial is read, the practice is four choices, the reading is read — all **recognition**.
The workbook is **production**: the pupil types the form, builds the sentence, writes five of
their own and goes and uses it. A pupil who can pick 먹어요 out of four may still be unable to
write it. Every task should make them *make* something.

Language policy = Prime Korean's: instructions, explanations, checklists in **Uzbek**; the
material in **Korean**. **No English anywhere.** Uzbek uses `ʻ` (oʻ, gʻ) and `ʼ`.

## 1. The five sections — always this order, ~15–20 minutes total

| § | Name | What goes in it | Marked by | Size |
|---|---|---|---|---|
| A | **Isinish** | 3–4 items from lessons **n-1, n-3, n-7** (spaced retrieval). Tag each with `<small>(PK-x)</small>`. None for PK-1. | auto | 3–4 |
| B | **Mashq** | controlled drill of *today's* pattern: `gap`, `conj`, `pick` | auto | 12–18 |
| C | **Qoʻllash** | `transform`, `build`, `translate` (uz→ko), `fix`. One task ⭐ (`stars: 2`) | auto | 12–16 |
| D | **Ijod** | one `write` everyone does + optionally a ⭐⭐ `write` (`stars: 3`). Hangul lessons: a `copy` task too | self + teacher | 1–2 |
| E | **Missiya** | 2–3 real-world acts, done *today*, outside the screen | ticked | 2–3 |

A workbook is complete when every section it has has been sent once; that is what ticks off a homework.

## 2. Task kinds

| kind | pupil does | required keys |
|---|---|---|
| `gap` | types the missing piece inside the sentence | `stem` with `___`, `answers` |
| `conj` | types a conjugated form | `stem` with `___`, `answers` |
| `pick` | chooses from a `<select>` (no typing — use when the choice *is* the skill: 이/가, 계세요/가세요) | `options` (2–4), `answers[0]` ∈ options |
| `transform` | rewrites a sentence (해요→합니다, statement→question, →negative) | `answers` |
| `build` | orders loose words into a sentence | `words` (shuffled!), `answers` |
| `translate` | uz → ko | `answers` (all natural variants) |
| `fix` | rewrites a sentence with one planted error | `answers` |
| `hangul` | letters ⇄ blocks. Spaces and `+` are ignored when marking (the IME fuses ㅎㅏㄴ into 한, so the pupil separates letters) | `answers` |
| `write` | free writing + a checklist they tick before sending; model answer after | `stem`, `checklist` (3–4), `model_answer` |
| `mission` | a real act; ticks "Bajardim", optional note | `stem`, optional `model_answer` as "Misol" |
| `copy` | handwriting: online a tick, on paper a 원고지 trace row per syllable | `words` |

Item `size`: `s` (one syllable), `m` (a word, default), `l` (a sentence). It sets the box online and the line on paper.

## 3. Accepted answers — the fairness rules
The marker (`workbook/grading.py`) already forgives: case, trailing `. ? !`, extra spaces,
NFC/NFD, `ʻ`/`'`. **Spacing and punctuation mistakes are marked RIGHT with a "check your
띄어쓰기" note** — so do **not** list spaceless variants, or the pupil loses the note.
You MUST list every *grammatically* different correct answer:
- subject drop: «Men talabaman» → `저는 학생입니다.` **and** `학생입니다.`;
- synonyms the lesson taught: 감사합니다 / 고맙습니다, 네 / 예;
- nothing the lesson has not taught (`제` before it is taught is not a variant, it is a spoiler).
The first answer is the one shown as "Javob:" — make it the textbook one.
A missed variant is not a disaster: pupils appeal ("Menimcha, mening javobim ham toʻgʻri"),
staff accept at `/workbook/appeals/`, and everyone who typed it is re-marked.

## 4. Explanations
Every auto item has one — 1–2 Uzbek sentences that say **why**, naming the rule
(받침 bor → 이). It is shown when the pupil is wrong (open) and behind "Nega?" when right.
⚠️ **Never cite an option's position** — say the text: «<strong>가</strong>», not "ikkinchisi".

## 5. The cumulative rule (same as the readings)
Only vocabulary and patterns from lessons ≤ n (and their readings). Names are free — use the
reading's characters (Afsona, Jiyoung xola, Jasur, Dilnoza) and the pupils' names
(Sherbek…), in Hangul: 아프소나, 자수르, 딜노자, 셰르벡, 지영. The gate prints every Hangul
token not found in lessons/readings ≤ n — read that list and justify each one.

## 6. Missions — what makes a good one
Real, small, today, and checkable by the pupil: say it aloud at dinner, find it in a drama
scene and note who said it, record a 20-second voice note and listen tomorrow, label five
things at home, send a message in Korean. Not "study more". Use emoji as the first glyph.

## 7. The ANSWER GATE (run before every import)
A throwaway `verify_pk_workbook_<range>.py` in the scratchpad (copy the pilot's). It:
1. runs the importer's `validate()` (gaps present, pick key among options, every key passes its own marker…);
2. **re-derives every key it can from the rules** with `tutorial/management/commands/_hangul.py`
   (blocks ⇄ letters, 이/가 + 아닙니다, 은/는, 을/를, 아/어요, 았/었어요, ㅂ/습니다, [pronunciation]);
   extend its regexes when a batch adds a new shape, and keep the "N keys re-derived" count honest;
3. prints Hangul tokens outside the cumulative corpus;
4. checks balanced tags, no `<script>`/`style=`, no English in the prose, no undefined `wb-*` class.
Prove it bites: inject one wrong key into a copy and watch it fail. Run `python3
tutorial/management/commands/_hangul.py` first; when you add a rule to it, first add the
case that fails without it.

## 8. Import, PDFs, deploy
```
python manage.py import_workbook workbook/management/commands/_workbook_prime_korean_<range>.py --author=prime --expect-items=<N>
python manage.py gen_worksheet_pdfs --only PK-x PK-y     # dev-only, headless Chrome; commit static/workbook/pdf/
```
`--republish` updates in place, so pupils' answers survive a fix. After any republish,
regenerate that PDF — `CommittedDataTests` fails until you do, and the site hides a stale PDF.
Then mark the range `[done]` in the toc and append the `import_workbook` line to `temporary.txt`
(`--author=powerty`).

## 9. The user's own tips
(none yet — add them here when shared; they override everything above)
