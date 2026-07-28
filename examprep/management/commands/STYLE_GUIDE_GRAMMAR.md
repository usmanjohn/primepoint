# Grammar Bank Writing Guide (for Claude)

This guide tells Claude HOW to write **grammar-bank entries** — the rows of the summary
table at `/examprep/<track>/grammar/`. It is a **reference**, not a lesson: a student who
already met the pattern comes here to check "what was it again, and how is it different
from the other one?".

> ⚠️ **Written in English for Claude — the ENTRIES YOU PRODUCE ARE UZBEK + KOREAN, never
> English.** Korean is the material; Uzbek is the explanation. Same rule as the lesson
> style guide.

---

## 1. What one entry is

A `POINTS` item in a `_grammar_<track>_<group>.py` data file:

```python
{
    "pattern":   "-(으)니까",
    "category":  "connective",     # grammatical shape — see §2
    "function":  "reason",         # MEANING group — see §3 (this is what synonyms hang on)
    "level":     2,                # TOPIK 1-6, where it first appears
    "freq":      3,                # 1-3 — how often TOPIK actually tests it
    "register":  "both",           # written / formal / polite / casual / both
    "meaning":   "sabab — chunki, shuning uchun",
    "attach":    "동사/형용사 + -(으)니까",
    "form_rule": "받침 yo‘q → <b>-니까</b> · 받침 bor → <b>-으니까</b>",
    "note":      "<p>Keyingi gapda <b>buyruq yoki taklif</b> kelishi mumkin...</p>",
    "mistake":   "<p>❌ 늦어서 미안합니다 → ✅ ...</p>",
    "examples":  [
        ("시간이 없으니까 택시를 탑시다.", "Vaqt yo‘q, shuning uchun taksi olaylik."),
    ],
    "synonyms":  [
        ("-아서/어서", "sabab, lekin keyin buyruq/taklif KELMAYDI"),
    ],
},
```

Only `pattern` and `meaning` are required — but a thin row is a useless row. Write all of
them unless the field genuinely has nothing to say.

## 2. `category` — the grammatical shape (allowed values)

| value | meaning |
|---|---|
| `particle`   | 조사 — kelishik va yuklama qo‘shimchalari (은/는, 이/가, 을/를, 에서…) |
| `ending`     | 종결어미 — gapni tugatuvchi shakllar (-습니다, -(으)ㄹ까요?, -네요…) |
| `connective` | 연결어미 — gaplarni bog‘lovchi shakllar (-고, -지만, -(으)면…) |
| `tense`      | 시제 — zamon (-았/었-, -겠-, -(으)ㄹ 것이다…) |
| `modifier`   | 관형형 — otni aniqlovchi shakllar (-(으)ㄴ, -는, -(으)ㄹ) |
| `expression` | 문형 — turg‘un iboralar (-기 때문에, -(으)ㄹ 수 있다…) |
| `voice`      | 피동·사동 — majhul va orttirma nisbat |
| `quotation`  | 인용 — ko‘chirma gap (-다고 하다…) |
| `honorific`  | 높임 — hurmat shakllari (-(으)시-, 께서…) |
| `adverb`     | 접속부사 — bog‘lovchi ravishlar (그러나, 따라서…) |

## 3. `function` — the MEANING group (the important one)

This is the axis the whole page turns on. Grouping by meaning is what puts
`-아서` `-(으)니까` `-기 때문에` `-느라고` on screen together, which is the actual question
students have. **Choose it by what the pattern MEANS, not by its shape.**

`reason` · `contrast` · `condition` · `concession` · `time` · `purpose` · `intention` ·
`guess` · `ability` · `obligation` · `experience` · `change` · `comparison` · `listing` ·
`choice` · `quote` · `feeling` · `discovery` · `degree` · `case` · `politeness`

(Exact labels live in `GRAMMAR_FUNCTION_CHOICES` in `examprep/models.py`.)

## 4. `meaning` — the table gloss (≤200 chars)

The single most-read string on the page. Formula: **`ma'no turi — o‘zbekcha ekvivalenti`**.

- ✅ `"sabab — chunki, shuning uchun"`
- ✅ `"qarama-qarshilik — lekin, ammo"`
- ✅ `"taxmin — shekilli, ko‘rinishidan"`
- ❌ `"Bu grammatika sabab ma'nosini bildiradi va ..."` — a sentence, not a gloss.

Give the Uzbek equivalent whenever one exists — that is what makes the table skimmable.

## 5. `attach` and `form_rule`

- `attach` — the attachment formula in Korean, **exactly as a textbook writes it**:
  `동사 + -(으)러`, `명사 + 때문에`, `동사/형용사 + -기 때문에`. Keep it short; it is a
  nowrap table cell.
- `form_rule` — the conjugation rule **in Uzbek**, HTML allowed. Cover 받침 alternation,
  ㄹ-irregulars, 이다 forms, past-tense combination:
  `"받침 yo‘q → <b>-니까</b> · 받침 bor → <b>-으니까</b> · ㄹ tushadi: 살다 → 사니까"`

## 6. `examples` — 2–4 per point

`(korean, uzbek)` tuples. Rules:

- **The first example is the one shown in the table**, so make it the clearest, shortest,
  most typical use. Put the exotic ones later.
- Sentences should be **TOPIK-flavoured**: everyday or exam topics (환경, 건강, 취업, 교육),
  not textbook nonsense.
- Uzbek translation is natural Uzbek, not word-for-word Korean.
- Use the user's pupils' names (Afsona, Jasur, Sherbek…) where a name is needed.

## 7. `synonyms` — the reason this page exists

`(pattern, farqi)` tuples. **The note must state the DIFFERENCE, not the similarity.**

- ✅ `("-아서/어서", "sabab, lekin keyin buyruq/taklif KELMAYDI: ❌ 늦어서 빨리 오세요")`
- ✅ `("-느라고", "faqat salbiy natija, ega bir xil bo‘lishi shart")`
- ❌ `("-아서/어서", "bu ham sabab bildiradi")` — says nothing.

Guidelines:
- 1–4 synonyms per point; every pattern that a student could confuse it with.
- **Write the pair from both sides.** If `-(으)니까` lists `-아서/어서`, then `-아서/어서`
  should list `-(으)니까` too, with the difference phrased from ITS side.
- Write the synonym pattern exactly as it appears in its own `pattern` field — the importer
  cross-links them into clickable pairs by matching the text (dash and spaces ignored).

## 8. `mistake` — what Uzbek learners actually get wrong

One short HTML block, `❌ wrong → ✅ right` shape. Skip it if there is no real trap.
Prefer mistakes that come from **Uzbek interference** (kelishik mismatches, 은/는 vs 이/가,
-에 vs -에서) or from the synonym confusion above.

## 9. `freq` — 1 to 3 stars

- `3` — appears on essentially every TOPIK paper (-기 때문에, -(으)면, -는데)
- `2` — regular but not guaranteed
- `1` — advanced / rare, TOPIK 5-6 reading only (-(으)ㄹ 라야, -더러…)

Be honest: if everything is 3 stars, the column stops meaning anything.

## 10. Coverage rule

Each data file is one group (particles, endings, connectives, …). Within a file, order
`POINTS` **easy → hard** (TOPIK 1 first). Give each file its own `order` decade so the
groups never collide in the table: particles 100+, endings 200+, connectives 300+,
tense/modifier 400+, expressions 500+, advanced 600+.

## 11. Workflow

1. Read this guide.
2. Read `toc_topik_grammar.txt` (header gives TRACK, AUTHOR; body is the group list).
3. Check where to continue:
   `GrammarPoint.objects.filter(track__name='TOPIK').order_by('-order').first()`
4. Write `_grammar_topik_<group>.py` with `TRACK = {...}` + `POINTS = [...]`.
5. Import: `python manage.py import_grammar <file> --author=<AUTHOR>` (`--republish` to
   overwrite; it rebuilds examples + synonyms and re-resolves every cross-link).
6. Give the `railway run python manage.py import_grammar ...` command for production —
   automatically, every time (see CLAUDE.md → Deployment).

## 12. Foydalanuvchining maslahatlari (user's own tips)

_(Foydalanuvchi grammatika bo‘yicha o‘z uslubini ulashganda — shu yerga yoz. Uning
so‘zlari umumiy tavsiyalardan ustun turadi.)_
