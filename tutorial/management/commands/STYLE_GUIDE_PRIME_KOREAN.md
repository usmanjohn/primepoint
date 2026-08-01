# Prime Korean — Writing Guide (for Claude)

How to write the **Prime Korean** grammar tutorials (`PK-1 …`). This guide replaces both
`STYLE_GUIDE.md` and `STYLE_GUIDE_PRIME_ENGLISH.md` for this subject — the lesson list
lives in `toc_prime_korean.txt`.

> The pupil is an **Uzbek school pupil (11–17)** who is starting Korean from zero and wants
> to reach TOPIK II. Write like a favourite teacher: warm, plain, concrete, never
> professorial.

---

## 0. The one rule that makes this different from Prime English

**Prime English teaches in English. Prime Korean teaches in Uzbek.**

In Prime English the pupil can already read the target language, so English carries the
explanation. In Prime Korean the pupil cannot read a single letter in lesson 1. So:

- **Every explanation, heading, instruction, hint and answer key is in Uzbek.**
- **Korean appears only as the material being taught** — example sentences, patterns,
  words, endings.
- **No English anywhere.** Not in headings, not in grammar terms, not in glosses. Same
  policy as the TOPIK `examprep` lessons.
- Grammar terms: use the Uzbek word first, then the Korean term in brackets the first time
  it appears in a lesson — *ega (주어)*, *kesim (서술어)*, *qoʻshimcha (조사)*,
  *aniqlovchi (관형사형)*, *oʻzak (어간)*, *tuslanish (활용)*.

## 1. Title, file, import

- Title: `PK-12: 은/는 va 이/가 — mavzu va ega orasidagi farq` — prefix `PK`, number from
  the toc, exact topic name from the toc.
- Category: `korean`. Every lesson also carries `"order": <lesson number>` — that is its
  position inside the **Prime Korean** playlist.
- File: `_tutorials_prime_korean_<from>_<to>.py`, exposing `PLAYLIST = {...}` +
  `TUTORIALS = [...]`. Copy the `PLAYLIST` dict unchanged into every batch file — the
  importer creates it once and reuses it.
- Import: `python manage.py import_tutorials <file> --author=prime` (local) /
  `--author=powerty` (production). Add `--republish` to overwrite.
- `summary` (≤300 chars): one Uzbek sentence — what the pupil will be able to do.

## 2. The shape of a lesson

Always in this order:

1. `<h2>PK-12: 은/는 va 이/가 — mavzu va ega orasidagi farq</h2>`
2. **Ilgak (hook)** — 1–2 Uzbek sentences that make the pupil *want* this grammar. A real
   situation ("Doʻstingiz sizdan ismingizni soʻradi…"), never "Bu darsda biz … oʻrganamiz".
3. `<div class="pe-goal">` — 3–4 checkmarked Uzbek lines ("Bu darsda siz…").
4. **Qolip** — a `<div class="pe-formula">` strip right after the goals.
5. **Asosiy qism** — small `<h3>` sections, oson → qiyin. Every new idea gets a `.pe-ex`
   example with its Uzbek translation.
6. **Koʻp uchraydigan xatolar** — `<h3>` + at least **3** `.pe-fix` wrong/right pairs.
7. **Mashq** — `<h3>Mashq</h3>` + at least **5** `.pe-quiz` items with hidden answers.
8. **Kalit soʻzlar** — `<ul class="pe-gloss">`, 8–10 Korean → Uzbek entries.
9. `<div class="pe-recap">` — the takeaway list. Last thing in the content.

### Depth bar (do not write thin lessons)

- **900–1200 words** of real Uzbek explanation.
- **At least 3 `.pe-ex` example blocks**, every one carrying its Uzbek translation, plus
  more examples inside `.pk-conj` / `.pe-vs` / `.pe-grid`.
- **5 practice questions**, every answer explained — not just the key.
- **At least 3 `.pe-uz` callouts** at the genuinely hard moments. The best ones contrast the
  two languages, because that is where Uzbek pupils actually go wrong. Korean and Uzbek are
  both SOV agglutinative languages, so **lean on that** — it is Prime Korean's biggest
  teaching advantage over an English-language Korean course. Examples:
  *"kitob**ni** oʻqiyman" → "책**을** 읽어요"* — both languages glue the object marker onto
  the noun, and both put the verb last.
- Explain the **why**, not only the rule.

## 3. Uzbek policy

- Use `oʻ` and `gʻ` (with the ʻ mark), not `o'`/`g'` or `ў`.
- Uzbek is the teaching language, so it must be *good* Uzbek — not translated-from-English
  Uzbek. Short sentences. Everyday words.
- The glossary is always Korean term → Uzbek meaning.
- Names in examples: use the user's real pupils — **Afsona, Jasur, Sherbek, Dilnoza,
  Bekzod** — alongside common Korean names (민수, 지영, 수진, 하나).

## 4. Romanisation policy

Romanisation is a crutch that must be thrown away early.

- **PK-1 … PK-8 (Hangul block):** every Korean example gets a `.pe-ex__rom` line.
- **PK-9 … PK-16:** romanisation only for a brand-new word or a tricky pronunciation.
- **PK-17 onwards:** no romanisation at all. The pupil reads Hangul.
- Use Revised Romanisation (국어의 로마자 표기법), but write it the way an Uzbek reads it
  where the two clash — note the difference in a `.pe-uz` callout rather than inventing a
  private system.

## 5. The component kit

Prime Korean **reuses the whole `pe-*` kit** documented in
`STYLE_GUIDE_PRIME_ENGLISH.md` section 4 — `pe-goal`, `pe-formula` + `pe-chip`, `pe-ex`,
`pe-call` (`pe-uz` / `pe-rule` / `pe-tip` / `pe-warn`), `pe-fix`, `pe-vs`, `pe-grid`,
`pe-steps`, `pe-quiz` + `pe-reveal` + `pe-blank` + `pe-peek`, `pe-gloss`, `pe-recap`,
`pe-table-wrap`, `pe-badge`, `pe-timeline`. Do not re-invent any of those.

On top of them, the **PRIME KOREAN** section at the bottom of `static/css/style.css` adds
the pieces Korean needs and English does not:

### Korean example sentence
`.pe-ex__ko` replaces `.pe-ex__en`. `.pe-ex__rom` is the optional romanisation line.
```html
<div class="pe-ex">
  <p class="pe-ex__ko">저는 <span class="pe-hl pe-hl--o">한국어를</span>
     <span class="pe-hl pe-hl--v">배워요</span>.</p>
  <p class="pe-ex__rom">jeoneun hangugeoreul baewoyo</p>
  <p class="pe-ex__uz">Men koreys tilini oʻrganaman.</p>
  <p class="pe-ex__why">Ixtiyoriy: bir qatorda nega shu shakl ishlatilgani.</p>
</div>
```

### Alphabet cards
```html
<div class="pk-hangul">
  <div class="pk-hangul__c">
    <span class="pk-hangul__ch">ㅏ</span>
    <span class="pk-hangul__rom">a</span>
    <span class="pk-hangul__uz">"ota" dagi a</span>
  </div>
</div>
```

### Syllable block — 초성 / 중성 / 종성
```html
<div class="pk-block">
  <span class="pk-block__cell pk-block__cell--i">ㅎ<small>초성</small></span>
  <span class="pk-block__cell pk-block__cell--m">ㅏ<small>중성</small></span>
  <span class="pk-block__cell pk-block__cell--f">ㄴ<small>종성</small></span>
  <span class="pk-block__eq">=</span>
  <span class="pk-block__out">한</span>
</div>
```

### 받침 switch — the signature visual of Prime Korean
Korean grammar forks on "does the noun/stem end in a consonant?" more than on anything
else. Use this every single time a pattern has an 은/는, 이/가, (으) or 아/어 choice.
```html
<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">명사 + <span class="pk-par">은</span></p>
    <p>선생님<b>은</b> · 학생<b>은</b> · 책<b>은</b></p>
    <p>Soʻz undosh bilan tugasa.</p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">명사 + <span class="pk-par">는</span></p>
    <p>저<b>는</b> · 학교<b>는</b> · 친구<b>는</b></p>
    <p>Soʻz unli bilan tugasa.</p>
  </div>
</div>
```

### Conjugation ladder
```html
<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>먹다</td><td class="pk-stem">먹</td><td class="pk-end">어요</td>
      <td class="pk-res">먹어요</td><td class="pk-uz">yeyman / yeydi</td></tr>
</table></div>
```

### Speech-level ladder
```html
<div class="pk-level">
  <div class="pk-level__row pk-level__row--1">
    <span class="pk-level__name">반말</span>
    <span class="pk-level__ko">먹어</span>
    <span class="pk-level__who">yaqin doʻst, tengdosh</span>
  </div>
  <div class="pk-level__row pk-level__row--3">
    <span class="pk-level__name">해요체</span>
    <span class="pk-level__ko">먹어요</span>
    <span class="pk-level__who">kundalik hurmat — eng koʻp ishlatiladi</span>
  </div>
</div>
```

### Pronunciation arrow — yozilishi → oʻqilishi
```html
<div class="pk-say">
  <span class="pk-say__from">한국어</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[한구거]</span>
  <span class="pk-say__why">연음화 — 받침 keyingi unliga koʻchadi</span>
</div>
```

### Inline word with gloss
```html
<span class="pk-w"><b>학교</b><span>maktab</span></span>
```

### Colour meanings on this course
`pe-chip--s` / `pe-hl--s` = **ega (주어)** · `--o` = **toʻldiruvchi (목적어)** ·
`--v` = **kesim (서술어)** · `--adv` = **hol** · `--neg` = **inkor** ·
`--opt` = ixtiyoriy qism. Inline in running text you may also use `.pk-stem` (oʻzak),
`.pk-end` (qoʻshimcha shakl) and `.pk-par` (조사). Drop a `.pe-legend` once, the first time
colours appear in a lesson.

## 6. Hard rules

- **No `<script>`, no `onclick`, no inline JS.** Interactivity = `<details>` only.
- Inline `style=` only for `pe-timeline` positions. Everything else uses kit classes.
- **No English.** If a term has no Uzbek equivalent, use the Korean one and gloss it.
- Never use a class that is not in this guide or the Prime English one — add it to the
  **PRIME KOREAN** CSS section and to this guide first.
- Korean text must be real, natural Korean — check particle choice against 받침 every time.
- Keep every lesson self-contained: a pupil landing on PK-52 from search still gets the
  pattern strip, examples and practice without reading PK-1.

## 7. Relationship to the rest of the site

- `examprep` TOPIK lessons = **imtihon koʻnikmalari** (question types, timing, strategy).
- `examprep` grammar/vocab banks = **maʼlumotnoma** (a table you look things up in).
- `corner` Korean stories = **oʻqish amaliyoti**.
- **Prime Korean = the language itself, from zero, in order.** When a lesson overlaps a
  grammar-bank entry, teach it properly here and let the bank stay a summary.

## 8. The user's own tips

*(Empty for now — when the user shares how they want Korean taught, it goes here and
overrides the generic advice above.)*

---

## How to ask

- **"Make the next 5 Prime Korean tutorials"** — Claude checks the highest `PK-` number,
  continues in toc order, writes the batch file, imports it, and gives the Railway command.
- **"Now the practices for those"** — see `practice/management/commands/
  STYLE_GUIDE_PK_PRACTICE.md`; the working rhythm is 5 tutorials → those same 5 practices
  → next 5 tutorials.
- **"Redo PK-3"** — rewrite that one with `--republish`.
