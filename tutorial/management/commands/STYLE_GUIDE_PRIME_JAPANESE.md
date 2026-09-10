# Prime Japanese — Writing Guide (for Claude)

How to write the **Prime Japanese** grammar tutorials (`PJ-1 …`). This guide replaces
`STYLE_GUIDE.md`, `STYLE_GUIDE_PRIME_ENGLISH.md` and `STYLE_GUIDE_PRIME_KOREAN.md` for
this subject — the lesson list lives in `toc_prime_japanese.txt`.

> The pupil is an **Uzbek school pupil (11–17)** starting Japanese from zero and aiming at
> a solid **N4, opening into N3**. Write like a favourite teacher: warm, plain, concrete,
> never professorial.

---

## 0. The one rule that makes this different from Prime English

**Prime English teaches in English. Prime Japanese teaches in Uzbek.**

The pupil cannot read a single character in lesson 1, so:

- **Every explanation, heading, instruction, hint and answer key is in Uzbek.**
- **Japanese appears only as the material being taught** — example sentences, patterns,
  words, endings, characters.
- **No English anywhere.** Not in headings, not in grammar terms, not in glosses. Same
  policy as Prime Korean and Prime Russian.
- Grammar terms: Uzbek word first, Japanese term in brackets the first time it appears in a
  lesson — *ega (主語)*, *kesim (述語)*, *qoʻshimcha (助詞)*, *oʻzak (語幹)*,
  *tuslanish (活用)*, *feʼl (動詞)*, *sifat (形容詞)*, *ot (名詞)*.

### 0.1 Prime Japanese's biggest teaching lever

Japanese and Uzbek are **both SOV and both agglutinative**, and the resemblance is closer
than Korean's in some places and further in others. Lean on it constantly:

| Uzbek | Japanese | The lever |
|---|---|---|
| kitob**ni** oʻqiyman | 本**を**読みます | Both glue the object marker to the noun, verb last |
| maktab**ga** boraman | 学校**へ**行きます | Direction marker, same slot |
| Men **talabaman** | 私は**学生です** | Copula at the end, no "to be" in the middle |
| bor**moqchiman** | 行き**たいです** | Desire is a suffix on the verb, not a separate word |
| oʻqi**b** boʻldim | 読**んで**しまいました | A converb chains actions in both languages |

Where they part company, say so plainly — that is where an Uzbek pupil actually goes wrong:
Japanese has no future tense, no gender, no plural, no articles, but it does have
**politeness levels baked into the verb** and **counters for every kind of object**.

---

## 1. Title, file, import

- Title: `PJ-14: は va が — mavzu va ega orasidagi farq` — prefix `PJ`, number from the toc,
  exact topic name from the toc.
- Category: `japanese`. Every lesson also carries `"order": <lesson number>` — its position
  inside the **Prime Japanese** playlist.
- File: `_tutorials_prime_japanese_<from>_<to>.py`, exposing `PLAYLIST = {...}` +
  `TUTORIALS = [...]`. Copy the `PLAYLIST` dict unchanged into every batch file — the
  importer creates it once and reuses it.
- Import: `python manage.py import_tutorials <file> --author=prime` (local) /
  `--author=powerty` (production). `--republish` to overwrite.
- `summary` (≤300 chars): one Uzbek sentence — what the pupil will be able to do.

## 2. The shape of a lesson

Always in this order:

1. `<h2>PJ-14: は va が — mavzu va ega orasidagi farq</h2>`
2. **Ilgak (hook)** — 1–2 Uzbek sentences that make the pupil *want* this grammar. A real
   situation, never "Bu darsda biz … oʻrganamiz".
3. `<div class="pe-goal">` — 3–4 checkmarked Uzbek lines ("Bu darsda siz…").
4. **Qolip** — a `<div class="pe-formula">` strip right after the goals.
5. **Asosiy qism** — small `<h3>` sections, oson → qiyin. Every new idea gets a `.pe-ex`
   example with its Uzbek translation.
6. **Koʻp uchraydigan xatolar** — `<h3>` + at least **3** `.pe-fix` wrong/right pairs.
7. **Mashq** — `<h3>Mashq</h3>` + at least **5** `.pe-quiz` items with hidden answers.
8. **Kalit soʻzlar** — `<ul class="pe-gloss">`, 8–10 Japanese → Uzbek entries.
9. `<div class="pe-recap">` — the takeaway list. Last thing in the content.

### Depth bar (do not write thin lessons)

- **900–1200 words** of real Uzbek explanation.
- **At least 3 `.pe-ex` example blocks**, every one carrying its Uzbek translation, plus
  more examples inside `.pj-conj` / `.pe-vs` / `.pe-grid` / `.pj-joshi`.
- **5 practice questions**, every answer explained — not just the key.
- **At least 3 `.pe-uz` callouts** at the genuinely hard moments. The best ones contrast the
  two languages (see §0.1).
- Explain the **why**, not only the rule.

## 3. Uzbek policy

- Use `oʻ` and `gʻ` (with the ʻ mark), not `o'`/`g'` or `ў`.
- Good Uzbek, not translated-from-English Uzbek. Short sentences. Everyday words.
- The glossary is always Japanese term → Uzbek meaning.
- Names in examples: the user's real pupils, alongside common Japanese names
  (田中, 佐藤, ゆき, けん, はるか). An Uzbek name written in Japanese goes in **katakana** —
  and that is itself a teaching moment from PJ-7 on.

  **Use these five first** (the user asked for them by name, 2026-09-10 — the earlier
  regulars Afsona / Jasur / Sherbek / Dilnoza / Bekzod had taken over the shelf):

  | Uzbek | Katakana | |
  |---|---|---|
  | Rano   | ラノ    | qiz |
  | Pari   | パリ    | qiz |
  | Munira | ムニラ  | qiz |
  | Inom   | イノム  | oʻgʻil |
  | Imron  | イムロン | oʻgʻil |

  Rotate them — a batch that uses only two of the five is doing the same thing the old
  set did. The wider class list is still fine for variety; these five lead.

## 4. Script policy — the three ladders

This is Prime Japanese's equivalent of Prime Korean's romanisation rule, and it has three
separate ladders that must not be confused.

### 4.1 Romaji — a crutch, thrown away early
- **PJ-1 … PJ-12 (script block):** every Japanese example gets a `.pe-ex__rom` line.
- **PJ-13 … PJ-20:** romaji only for a brand-new word or a tricky pronunciation.
- **PJ-21 onwards:** no romaji at all.
- Use **Hepburn** (しんぶん → shinbun, つ → tsu, し → shi, ふ → fu), and write long vowels
  with a macron (とうきょう → Tōkyō). Where Hepburn clashes with how an Uzbek reads Latin
  letters, note it in a `.pe-uz` callout rather than inventing a private system.

### 4.2 Furigana — never thrown away
Every kanji in every lesson carries its reading in `<ruby>`, for the whole 100 lessons.
This is not a crutch; it is how Japanese learner material is actually printed.
```html
<ruby>学校<rt>がっこう</rt></ruby>
```
From **PJ-40** you may wrap a sentence in `.pj-dim` so the readings are faint until the
pupil hovers or taps — a self-test that still lets them read on. Never simply drop the
furigana.

### 4.3 Kanji load — the ramp
- **PJ-1 … PJ-12:** kana only, plus the ~80 characters introduced in PJ-10 … PJ-12.
- **PJ-13 … PJ-40:** N5 kanji as they come up in the grammar, 5–8 new ones per lesson.
- **PJ-41 … PJ-75:** N4 kanji, same rate.
- **PJ-76 … PJ-100:** into N3. By PJ-100 the pupil has met roughly **600** characters.
Every genuinely new kanji gets a `.pj-kanji` card the first time it appears in a lesson.
**Write real Japanese**: a word normally written in kanji is written in kanji (with
furigana), not spelled out in kana to be kind. Kindness is the ruby text.

## 5. The component kit

Prime Japanese **reuses the whole `pe-*` kit** documented in
`STYLE_GUIDE_PRIME_ENGLISH.md` section 4 — `pe-goal`, `pe-formula` + `pe-chip`, `pe-ex`,
`pe-call` (`pe-uz` / `pe-rule` / `pe-tip` / `pe-warn`), `pe-fix`, `pe-vs`, `pe-grid`,
`pe-steps`, `pe-quiz` + `pe-reveal` + `pe-blank` + `pe-peek`, `pe-gloss`, `pe-recap`,
`pe-table-wrap`, `pe-badge`, `pe-timeline`. Do not re-invent any of those.

On top of them, the **PRIME JAPANESE** section at the bottom of `static/css/style.css` adds
the pieces Japanese needs and neither English nor Korean has:

### Japanese example sentence
`.pe-ex__ja` replaces `.pe-ex__en`. `.pe-ex__rom` is the optional romaji line.
```html
<div class="pe-ex">
  <p class="pe-ex__ja">わたしは <span class="pe-hl pe-hl--o"><ruby>日本語<rt>にほんご</rt></ruby>を</span>
     <span class="pe-hl pe-hl--v"><ruby>勉強<rt>べんきょう</rt></ruby>します</span>。</p>
  <p class="pe-ex__rom">watashi wa nihongo o benkyō shimasu</p>
  <p class="pe-ex__uz">Men yapon tilini oʻrganaman.</p>
  <p class="pe-ex__why">Ixtiyoriy: bir qatorda nega shu shakl ishlatilgani.</p>
</div>
```

### Kana cards — the gojūon grid
Five columns, read **left to right** — あ い う え お. A real 五十音図 runs vertically
right to left, but every textbook written for foreigners lays it out this way and the pupil
reads left to right everywhere else on the site. Use `.pj-kana--free` for an odd-sized set
(dakuten, yōon). `.pj-kana__gap` fills the holes in the や and わ rows.
```html
<div class="pj-kana">
  <div class="pj-kana__c">
    <span class="pj-kana__ch">あ</span>
    <span class="pj-kana__rom">a</span>
    <span class="pj-kana__uz">"ota" dagi a</span>
  </div>
  <div class="pj-kana__gap"></div>
</div>
```
Add `pj-kana__c--kata` for katakana tiles, `pj-kana__c--new` to mark the ones being taught
right now.

### Hiragana ⇄ katakana pair — "bir tovush, ikki kiyim"
```html
<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">HIRAGANA</p>
    <p class="pj-pair__form">か</p>
    <p>Yaponcha soʻzlar va grammatik qoʻshimchalar.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">KATAKANA</p>
    <p class="pj-pair__form">カ</p>
    <p>Chet soʻzlar, ismlar, tovush taqlidi.</p>
  </div>
</div>
```

### Kanji card
```html
<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">学</span>
    <span class="pj-kanji__uz">oʻqimoq, ilm</span>
    <span class="pj-kanji__on">オン: ガク</span>
    <span class="pj-kanji__kun">KUN: まな(ぶ)</span>
    <span class="pj-kanji__note">学生 (がくせい) — talaba · 学校 (がっこう) — maktab</span>
  </div>
</div>
```

### on'yomi / kun'yomi fork — the signature visual of Prime Japanese
Japanese reading forks on "is this character alone, or glued to another kanji?" more than
on anything else. Use it every time a lesson introduces a compound.
```html
<div class="pj-yomi">
  <div class="pj-yomi__side">
    <p class="pj-yomi__h">ON'YOMI — kanji + kanji</p>
    <p class="pj-yomi__ex"><ruby>学校<rt>がっこう</rt></ruby> · <ruby>大学<rt>だいがく</rt></ruby></p>
    <p>Ikki kanji yopishsa, xitoycha oʻqilish ishlaydi.</p>
  </div>
  <div class="pj-yomi__side pj-yomi__side--kun">
    <p class="pj-yomi__h">KUN'YOMI — kanji + kana</p>
    <p class="pj-yomi__ex"><ruby>学<rt>まな</rt></ruby>ぶ</p>
    <p>Kanji yolgʻiz yoki hiragana bilan tugasa, yaponcha oʻqilish ishlaydi.</p>
  </div>
</div>
```

### Particle strip — the sentence as its joshi
The single most useful diagram in the course. Use it whenever a lesson adds a particle.
```html
<div class="pj-joshi">
  <span class="pj-joshi__n">わたし</span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n"><ruby>本<rt>ほん</rt></ruby></span>
  <span class="pj-joshi__p">を<small>TOʻLDIRUVCHI</small></span>
  <span class="pj-joshi__v"><ruby>読<rt>よ</rt></ruby>みます</span>
  <span class="pj-joshi__uz">Men kitob oʻqiyman. — oʻzbekcha ham: kitob-NI oʻqiyman.</span>
</div>
```

### Conjugation ladder
```html
<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-stem">食べ</td>
      <td class="pj-end">ます</td><td class="pj-res">食べます</td>
      <td class="pj-uz">yeyman / yeydi</td></tr>
</table></div>
```

### Verb-group fork — 一段 / 五段 / 不規則
```html
<div class="pj-group">
  <div class="pj-group__c">
    <p class="pj-group__h">I — 五段 (godan)</p>
    <p class="pj-group__ex"><ruby>読<rt>よ</rt></ruby>む → 読みます</p>
    <p>Oxirgi う qatori い qatoriga tushadi.</p>
  </div>
  <div class="pj-group__c pj-group__c--2">
    <p class="pj-group__h">II — 一段 (ichidan)</p>
    <p class="pj-group__ex"><ruby>食<rt>た</rt></ruby>べる → 食べます</p>
    <p>る tushadi, ます qoʻyiladi. Xolos.</p>
  </div>
  <div class="pj-group__c pj-group__c--3">
    <p class="pj-group__h">III — 不規則</p>
    <p class="pj-group__ex">する → します · <ruby>来<rt>く</rt></ruby>る → <ruby>来<rt>き</rt></ruby>ます</p>
    <p>Faqat ikkita. Yodlab qoʻying.</p>
  </div>
</div>
```

### Politeness ladder
```html
<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name">普通体</span>
    <span class="pj-level__ja"><ruby>食<rt>た</rt></ruby>べる</span>
    <span class="pj-level__who">yaqin doʻst, oila, kundalik daftar</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name">丁寧体</span>
    <span class="pj-level__ja">食べます</span>
    <span class="pj-level__who">kundalik hurmat — eng koʻp ishlatiladi</span>
  </div>
</div>
```

### Pronunciation arrow — yozilishi → oʻqilishi
```html
<div class="pj-say">
  <span class="pj-say__from">です</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[des]</span>
  <span class="pj-say__why">soʻz oxiridagi う deyarli eshitilmaydi</span>
</div>
```

### One character, large
For a shape comparison — two lookalike kana side by side inside a `.pe-vs` card.
```html
<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">は — ha</p>
    <p class="pj-big">は</p>
    <p>Chap tomonda tik chiziq, oʻngda halqa ochiq qoladi.</p></div>
</div>
```

### Stroke order
```html
<div class="pj-stroke">
  <span class="pj-stroke__s" data-n="1">丿</span>
  <span class="pj-stroke__s" data-n="2">人</span>
</div>
```

### Inline word with gloss
```html
<span class="pj-w"><b>学校</b><span>maktab</span></span>
```

### Colour meanings on this course
`pe-chip--s` / `pe-hl--s` = **ega (主語)** · `--o` = **toʻldiruvchi (目的語)** ·
`--v` = **kesim (述語)** · `--adv` = **hol** · `--neg` = **inkor** ·
`--opt` = ixtiyoriy qism. Inline in running text you may also use `.pj-stem` (oʻzak),
`.pj-end` (qoʻshimcha shakl) and `.pj-par` (助詞). Drop a `.pe-legend` once, the first time
colours appear in a lesson.

## 6. Hard rules

- **No `<script>`, no `onclick`, no inline JS.** Interactivity = `<details>` only.
- Inline `style=` only for `pe-timeline` positions. Everything else uses kit classes.
- **No English.** If a term has no Uzbek equivalent, use the Japanese one and gloss it.
- Never use a class that is not in this guide or the Prime English one — add it to the
  **PRIME JAPANESE** CSS section and to this guide first.
- **Japanese punctuation is Japanese**: 。 and 、 not . and , ; 「」 not "". A full stop
  inside a Japanese sentence is a bug.
- **Every kanji carries furigana.** No exceptions before PJ-40, and after that only inside
  a deliberate `.pj-dim`.
- Japanese must be real, natural Japanese — check the particle, check the verb group, check
  the politeness level is consistent inside one example.
- Keep every lesson self-contained: a pupil landing on PJ-52 from search still gets the
  pattern strip, examples and practice without reading PJ-1.

## 7. The three legs

**Each Prime Japanese lesson from PJ-13 has three legs, written together in batches of 3:**

1. the **tutorial** (`tutorial`, PJ-n) — teaches the pattern;
2. the **practice** (`practice`, 20 questions; **12** for the script lessons PJ-1 … PJ-12),
   subject `日本語`. Guide: `practice/management/commands/STYLE_GUIDE_PJ_PRACTICE.md`;
3. the **reading** (`corner`, collection "Prime Japanese Readings", `order` = lesson
   number) — the pattern living in a text, with `cn-word` tappable vocab, a `grammar`
   block, 2–3 comprehension questions and **generated audio**. Guide: the overrides in
   `corner/management/commands/toc_prime_japanese_readings.txt`.

PJ-1 … PJ-12 have **no reading** — there is no grammar yet to embed.

Import order per batch: tutorials → practices → readings → audio → re-run
`import_tutorials --republish` so the `"stories": [...]` links resolve (the story must
exist first).

## 8. Relationship to the rest of the site

- **Prime Japanese = the language itself, from zero, in order.** There is no Japanese
  `examprep` track and no Japanese exam simulator yet; if a JLPT track is ever added, it
  takes the exam skills and this course keeps the language.
- `corner`'s "Prime Japanese Readings" = the reading leg, bound to the lessons.
- Prime Japanese is **not** Prime Korean. The two look similar on the page and are
  genuinely similar languages, but never copy a Korean lesson across — the particles, the
  verb groups and the politeness system are different systems that happen to rhyme.

## 9. The user's own tips

*(Empty for now — when the user shares how they want Japanese taught, it goes here and
overrides the generic advice above.)*

---

## How to ask

- **"Make the next 3 Prime Japanese lessons"** — Claude checks the highest `PJ-` number,
  continues in toc order, writes the batch file (tutorials + practices + readings),
  imports, and gives the Railway commands.
- **"Redo PJ-3"** — rewrite that one with `--republish`.
