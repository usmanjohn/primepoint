# IELTS Grammar Bank Writing Guide (for Claude)

This guide tells Claude HOW to write **IELTS grammar-bank entries** — the rows of the
summary table at `/examprep/ielts/grammar/`. It is the English-track sibling of
`STYLE_GUIDE_GRAMMAR.md` (which is TOPIK's); the data format, the importer and the page
are identical, only the language and the sections differ.

It is a **reference**, not a lesson: a student who already met the structure comes here to
check "what was it again, and how is it different from the other one?". Teaching a
structure in depth still belongs in an examprep Lesson.

> ⚠️ **Written in English for Claude — the ENTRIES YOU PRODUCE ARE UZBEK + ENGLISH.**
> English is the material (patterns, example sentences, model phrases); **Uzbek is every
> word of explanation** — meanings, notes, mistakes, synonym differences. Never Russian.
> Same rule as `STYLE_GUIDE_IELTS.md`.

**The IELTS angle.** Every row must answer "what does this buy me in the exam?". Grammar
is a quarter of the Writing and Speaking mark (*Grammatical Range and Accuracy*), so each
entry should say where it earns marks — Task 1 trends, Task 2 argument, Speaking Part 3,
or accuracy traps that cost band points.

---

## 1. What one entry is

A `POINTS` item in a `_grammar_ielts_<group>.py` data file:

```python
{
    "pattern":   "the third conditional",
    "category":  "en_condition",   # grammatical shape — see §2
    "function":  "condition",      # MEANING group — see §3 (synonyms hang on this)
    "level":     4,                # 1-6 → Band 5 … Band 7.5+ — see §9
    "freq":      3,                # 1-3 — how often IELTS actually rewards it
    "register":  "both",           # written / formal / polite / casual / both
    "meaning":   "o‘tmishdagi xayoliy shart — «agar ... bo‘lganida, ... bo‘lardi»",
    "attach":    "If + past perfect, would have + V3",
    "form_rule": "<b>If</b> + had (not) + V3, <b>would/could/might have</b> + V3 …",
    "note":      "<p>Task 2 da <b>sabab-natija tahlili</b> uchun …</p>",
    "mistake":   "<p>❌ If I <u>would have</u> known → ✅ If I <b>had</b> known …</p>",
    "examples":  [
        ("If governments had acted earlier, the crisis would have been less severe.",
         "Agar hukumatlar erta harakat qilganida, inqiroz kamroq og‘ir bo‘lardi."),
    ],
    "synonyms":  [
        ("the second conditional", "second = hozir/kelajakdagi xayoliy; third = o‘tmish, "
                                   "endi o‘zgartirib bo‘lmaydi"),
    ],
    "order": 403,
},
```

Only `pattern` and `meaning` are required — but a thin row is a useless row. Write all of
them unless the field genuinely has nothing to say.

### `pattern` — how to name an English structure

Korean patterns name themselves (`-(으)니까`). English ones do not, so use the name a
student would search for, in **lowercase English**, optionally with the formula:

- ✅ `"present perfect"`, `"the third conditional"`, `"despite / in spite of"`,
  `"reduced relative clause"`, `"it is often argued that …"`
- ❌ `"O‘tgan tugallangan zamon"` — the pattern field is the English name; the Uzbek goes
  in `meaning`. (Uzbek learners look for both, so put the Uzbek term in `meaning`.)
- Keep it ≤ ~50 characters — it is a table cell and a URL slug.

## 2. `category` — the grammatical shape (allowed values)

English tracks use the `en_` values. **Never use TOPIK's** (`particle`, `ending`, …).

| value | section |
|---|---|
| `en_tense`     | Zamonlar — tenses & aspect (present perfect, past simple, future forms) |
| `en_modal`     | Modal fe’llar — modals and semi-modals (must, should, may, be likely to) |
| `en_clause`    | Ergash gaplar — relative, noun and adverbial clauses |
| `en_condition` | Shart gaplar — conditionals, wish, unless, provided that |
| `en_passive`   | Majhul nisbat va nominalizatsiya — passive, causative, nominalisation |
| `en_article`   | Artikl va aniqlovchilar — a/an/the/∅, quantifiers, countability |
| `en_prep`      | Predloglar — prepositions, including the Task 1 data prepositions |
| `en_compare`   | Qiyoslash — comparatives, superlatives, as…as, degree |
| `en_verbpat`   | Fe’l qoliplari — gerunds, infinitives, verb + preposition patterns |
| `en_cohesion`  | Bog‘lash vositalari — linkers, referencing, substitution |
| `en_advanced`  | Murakkab tuzilmalar — inversion, cleft, participle clauses, subjunctive |

## 3. `function` — the MEANING group (the important one)

This is the axis the whole page turns on: grouping by meaning is what puts `because` /
`due to` / `owing to` / `as a result of` on screen together, which is the actual question
a student has. **Choose it by what the structure MEANS, not by its shape.**

IELTS uses: `reason` · `result` · `contrast` · `concession` · `condition` · `time` ·
`purpose` · `comparison` · `change` · `degree` · `hedging` · `emphasis` · `example` ·
`summary` · `reference` · `listing` · `guess` · `obligation` · `ability` · `quote` ·
`feeling` · `case`

Three of these carry most of the IELTS weight:

- **`hedging`** — the band-7 skill. `tend to`, `may well`, `it appears that`, `arguably`,
  `in most cases`. Overstated claims ("this always causes…") cost marks; hedged ones earn.
- **`change`** — Task 1's whole vocabulary of trends (`rise steadily`, `level off`).
- **`reference`** — `this trend`, `such measures`, `the former/the latter`, `doing so`:
  cohesion without repeating yourself, which is a Coherence & Cohesion descriptor.

(Exact labels live in `banklabels.GRAMMAR_FUNCTION_LABELS['ielts']`.)

## 4. `meaning` — the table gloss (≤200 chars)

The single most-read string on the page. Formula: **`ma'no turi — o‘zbekcha ekvivalenti`**.

- ✅ `"sabab — chunki, sababli"`
- ✅ `"o‘tmishdagi xayoliy shart — «agar ... bo‘lganida»"`
- ✅ `"ehtiyotkor fikr — «ehtimol, ko‘p hollarda»"`
- ❌ `"Bu grammatika sabab ma'nosini bildiradi va ..."` — a sentence, not a gloss.

Where the structure has an Uzbek equivalent, name it (`-sa edi`, `-gan bo‘lardi`) — that is
what makes the table skimmable for an Uzbek learner.

## 5. `attach` and `form_rule`

- `attach` — the **formula in English**, exactly as a grammar book writes it:
  `If + past perfect, would have + V3` · `have/has + V3` · `noun + which/that + verb` ·
  `despite + noun/-ing`. Keep it short; it is a nowrap table cell.
- `form_rule` — the rule **in Uzbek**, HTML allowed. Cover the things Uzbek learners get
  wrong: auxiliary choice, word order, what follows the linker (noun vs clause), irregular
  forms, contraction in speech vs writing:
  `"<b>despite</b> + ot yoki -ing (❌ despite <u>he was</u> …) · <b>although</b> + to‘liq gap"`

## 6. `examples` — 2–4 per point

`(english, uzbek)` tuples — the same field the TOPIK files use for Korean.

- **The first example is the one shown in the table**, so make it the clearest, shortest,
  most typical use. Put the exotic ones later.
- Sentences must be **IELTS-flavoured**: exam topics (education, environment, technology,
  urbanisation, health, work) and Task 1 data sentences — not textbook nonsense about
  Tom's cat.
- Write English at real exam register (Band 7+ academic), not learner English.
- The Uzbek translation is natural Uzbek, not word-for-word English.
- Use the user's pupils' names (Afsona, Jasur, Sherbek…) where a name is needed, and only
  in Speaking-flavoured examples — Writing examples stay impersonal.

## 7. `synonyms` — the reason this page exists

`(pattern, farqi)` tuples. **The note must state the DIFFERENCE, not the similarity.**

- ✅ `("although", "although + TO‘LIQ GAP; despite + ot yoki -ing")`
- ✅ `("present perfect", "past simple = tugagan vaqt aytilgan (in 2019); present perfect = "
       "vaqt aytilmagan, natijasi hozir muhim")`
- ❌ `("however", "bu ham qarshilik bildiradi")` — says nothing.

Guidelines:
- 1–4 synonyms per point; every structure a student could confuse it with.
- **Write the pair from both sides.** If `despite` lists `although`, then `although`
  should list `despite`, with the difference phrased from ITS side.
- Write the synonym exactly as it appears in its own `pattern` field — the importer
  cross-links them into clickable pairs by matching the text (dash and spaces ignored),
  so `"present perfect"` links, `"the present perfect tense"` does not.

## 8. `mistake` — what Uzbek learners actually get wrong

One short HTML block, `❌ wrong → ✅ right` shape. Skip it only if there is genuinely no
trap. Prefer mistakes that come from **Uzbek/Russian interference**, because those are the
ones that repeat in every essay:

- articles — Uzbek has none: `❌ Government should ban the cars` → `✅ Governments should ban cars`
- plural + countability: `❌ many informations` → `✅ much information`
- `-ing` after preposition: `❌ instead of to build` → `✅ instead of building`
- word order in questions/embedded clauses: `❌ I don't know where is it`
- verb agreement after long subjects: `❌ the number of students are rising`

## 9. `level` — 1–6, rendered as a band

The bank shows `level` as the **band the structure starts paying off at**, not a
difficulty rating in the abstract (see `banklabels.LEVEL_LABELS['ielts']`):

| level | shown as | means |
|---|---|---|
| 1 | Band 5   | basic accuracy — without it the sentence is wrong |
| 2 | Band 5.5 | expected in any answer |
| 3 | Band 6   | the standard structures a 6 uses correctly |
| 4 | Band 6.5 | range that lifts an answer above 6 |
| 5 | Band 7   | complex structures used naturally |
| 6 | Band 7.5+| sophisticated/marked structures — inversion, cleft, subjunctive |

## 10. `freq` — 1 to 3 stars

- `3` — you cannot write a good answer without it (present perfect, `although`, passive)
- `2` — regularly useful, appears in strong answers
- `1` — advanced polish, one or two per essay at most (inversion, cleft)

Be honest: if everything is 3 stars, the column stops meaning anything.

## 11. `register` — where it belongs

`written` = academic writing · `formal` = formal speech/letter · `polite` = neutral, safe
anywhere · `casual` = informal/spoken only · `both` = anywhere.

This column earns its place on IELTS: contractions, `get`-passives and phrasal verbs are
fine in Speaking and cost marks in Task 2. Mark them `casual` and say so in `note`.

## 12. Coverage rule

Each data file is one group. Within a file, order `POINTS` **easy → hard** (Band 5 first).
Give each file its own `order` decade so the groups never collide in the table — see
`toc_ielts_grammar.txt`, which owns the decade allocation.

## 13. Workflow

1. Read this guide.
2. Read `toc_ielts_grammar.txt` (header gives TRACK, AUTHOR; body is the group list).
3. Check where to continue:
   `GrammarPoint.objects.filter(track__name='IELTS').order_by('-order').first()`
4. Write `_grammar_ielts_<group>.py` with `TRACK = {...}` + `POINTS = [...]`.
   `TRACK` must be `{"name": "IELTS", …}` — the importer matches the track by name.
5. Import: `python manage.py import_grammar <file> --author=<AUTHOR>` (`--republish` to
   overwrite; it rebuilds examples + synonyms and re-resolves every cross-link).
6. Give the `railway run python manage.py import_grammar ...` command for production —
   automatically, every time (see CLAUDE.md → Deployment).

## 14. Foydalanuvchining maslahatlari (user's own tips)

_(Foydalanuvchi IELTS grammatikasi bo‘yicha o‘z uslubini ulashganda — shu yerga yoz. Uning
so‘zlari umumiy tavsiyalardan ustun turadi.)_
