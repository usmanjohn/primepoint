# Prime Russian — Writing Guide (for Claude)

How to write the **Prime Russian** grammar tutorials (`PR-1 …`). This guide replaces
`STYLE_GUIDE.md`, `STYLE_GUIDE_PRIME_ENGLISH.md` and `STYLE_GUIDE_PRIME_KOREAN.md` for this
subject — the lesson list lives in `toc_prime_russian.txt`.

> The pupil is an **Uzbek learner starting Russian from zero** and aiming at confident,
> real B2 Russian. Write like a favourite teacher: warm, plain, concrete, never professorial.

---

## 0. The language rule

**Prime Russian teaches in Uzbek.** Exactly like Prime Korean, and the opposite of
Prime English.

- **Every explanation, heading, instruction, hint and answer key is in Uzbek.**
- **Russian appears only as the material being taught** — example sentences, patterns,
  words, endings.
- **No English anywhere.** Not in headings, not in grammar terms, not in glosses.
- Grammar terms: Uzbek word first, then the Russian term in brackets the first time it
  appears in a lesson — *jins (род)*, *kelishik (падеж)*, *oʻzak (основа)*,
  *qoʻshimcha (окончание)*, *tuslanish (спряжение)*, *turlanish (склонение)*,
  *feʼl turi (вид)*, *urgʻu (ударение)*, *predlog (предлог)*.

## 0.1 The one advantage Prime Russian has — use it in every lesson

The Uzbek pupil arrives with **three things already in their pocket**. A Russian course
written for an English speaker cannot use any of them. Prime Russian must:

1. **They can already read Cyrillic.** Uzbek was written in Cyrillic and still is, half the
   time. So PR-1 is not "here is a new alphabet" — it is *"you know 26 of these 33 letters;
   here are the seven that will trip you and the four Uzbek letters Russian does not have."*
   That is why the alphabet block is **5 lessons, not 8** like Hangul.
2. **Uzbek has cases too.** Uzbek's six kelishik map onto Russian's six падежи astonishingly
   well — *kitob**ni** oʻqidim* → *я прочитал книг**у***. Both languages glue an ending onto
   the noun to say its job in the sentence. This is Prime Russian's single biggest teaching
   lever: **never introduce a падеж without showing the Uzbek kelishik beside it.**
3. **They already know hundreds of Russian words** — *stol, kitob (книга), samolyot, zavod,
   direktor, dovon*… Point this out; it buys the pupil confidence cheaply and honestly.

And **two places Uzbek actively fights them**, which need a `.pe-uz` callout every time:

- **Jins (род).** Uzbek has no grammatical gender at all. This is genuinely new and it
  infects nouns, adjectives, past-tense verbs and possessives. Do not rush it.
- **Feʼl turi (вид).** Uzbek marks completion with helper verbs (*oʻqib chiqdim*), Russian
  marks it inside the verb itself. Closer than English is, but not the same.

## 1. Title, file, import

- Title: `PR-12: Sifat otga moslashadi — новый, новая, новое, новые` — prefix `PR`, number
  from the toc, exact topic name from the toc.
- Category: `russian`. Every lesson also carries `"order": <lesson number>` — its position
  inside the **Prime Russian** playlist.
- File: `_tutorials_prime_russian_<from>_<to>.py`, exposing `PLAYLIST = {...}` +
  `TUTORIALS = [...]`. Copy the `PLAYLIST` dict unchanged into every batch file — the
  importer creates it once and reuses it.
- Import: `python manage.py import_tutorials <file> --author=prime` (local) /
  `--author=powerty` (production). Add `--republish` to overwrite.
- `summary` (≤300 chars): one Uzbek sentence — what the pupil will be able to do.

## 2. The shape of a lesson

Always in this order:

1. `<h2>PR-12: Sifat otga moslashadi — новый, новая, новое, новые</h2>`
2. **Ilgak (hook)** — 1–2 Uzbek sentences that make the pupil *want* this grammar. A real
   situation, never "Bu darsda biz … oʻrganamiz".
3. `<div class="pe-goal">` — 3–4 checkmarked Uzbek lines ("Bu darsda siz…").
4. **Qolip** — a `<div class="pe-formula">` strip right after the goals.
5. **Asosiy qism** — small `<h3>` sections, oson → qiyin. Every new idea gets a `.pe-ex`
   example with its Uzbek translation.
6. **Koʻp uchraydigan xatolar** — `<h3>` + at least **3** `.pe-fix` wrong/right pairs.
7. **Mashq** — `<h3>Mashq</h3>` + at least **5** `.pe-quiz` items with hidden answers.
8. **Kalit soʻzlar** — `<ul class="pe-gloss">`, 8–10 Russian → Uzbek entries.
9. `<div class="pe-recap">` — the takeaway list. Last thing in the content.

### Depth bar (do not write thin lessons)

- **900–1200 words** of real Uzbek explanation.
- **At least 3 `.pe-ex` example blocks**, every one carrying its Uzbek translation, plus
  more examples inside `.pr-decl` / `.pr-gender` / `.pe-vs` / `.pe-grid`.
- **5 practice questions**, every answer explained — not just the key.
- **At least 3 `.pe-uz` callouts** at the genuinely hard moments. The best ones contrast the
  two languages (see 0.1) — that is where Uzbek pupils actually go wrong.
- Explain the **why**, not only the rule.

## 3. Uzbek policy

- Use `oʻ` and `gʻ` (with the ʻ mark), not `o'`/`g'` or `ў`.
- Uzbek is the teaching language, so it must be *good* Uzbek — not translated-from-Russian
  Uzbek. Short sentences. Everyday words.
- The glossary is always Russian term → Uzbek meaning.
- Names in examples: the user's real pupils — **Afsona, Jasur, Sherbek, Dilnoza, Bekzod** —
  alongside common Russian names (Анна, Дмитрий, Марина, Олег, Катя).

## 4. Stress (ударение) policy — the Russian equivalent of romanisation

Russian's crutch is not transliteration, it is the **stress mark**. Stress decides how every
unstressed vowel is pronounced, so a beginner who does not know where the stress falls
cannot say the word at all.

- **PR-1 … PR-20:** mark the stress on **every** multi-syllable Russian word, everywhere —
  examples, tables, glossary, practice items. Use the combining acute: `рабо́та`, `молоко́`.
- **PR-21 … PR-50:** mark it on **new words and on words where the stress shifts**
  (рука́ → ру́ки, окно́ → о́кна). Not on words the pupil has met ten times.
- **PR-51 onwards:** mark it only when the lesson is *about* the stress, or the word is
  genuinely new and hard, or a minimal pair is at stake.
- **Never** put a stress mark on a one-syllable word, and never on ё — ё is always stressed.
- Add a `.pe-ex__rom` line for the *pronunciation* (not transliteration) whenever the
  spelling lies to the reader: `<p class="pe-ex__rom">[мълако́]</p>`. Through PR-20 do this
  for every аканье / оглушение word; after that only when it surprises.

## 5. The component kit

Prime Russian **reuses the whole `pe-*` kit** documented in
`STYLE_GUIDE_PRIME_ENGLISH.md` section 4 — `pe-goal`, `pe-formula` + `pe-chip`, `pe-ex`,
`pe-call` (`pe-uz` / `pe-rule` / `pe-tip` / `pe-warn`), `pe-fix`, `pe-vs`, `pe-grid`,
`pe-steps`, `pe-quiz` + `pe-reveal` + `pe-blank` + `pe-peek`, `pe-gloss`, `pe-recap`,
`pe-table-wrap`, `pe-badge`, `pe-timeline`, `pe-legend`. Do not re-invent any of those.
`.pe-ex__rom` is borrowed from the Korean kit for the pronunciation line.

On top of them, the **PRIME RUSSIAN** section at the bottom of `static/css/style.css` adds
the pieces Russian needs and the other two courses do not:

### Russian example sentence
`.pe-ex__ru` replaces `.pe-ex__en` / `.pe-ex__ko`.
```html
<div class="pe-ex">
  <p class="pe-ex__ru">Я <span class="pe-hl pe-hl--v">чита́ю</span>
     <span class="pe-hl pe-hl--o">кни́гу</span>.</p>
  <p class="pe-ex__rom">[йа чита́йу кни́гу]</p>
  <p class="pe-ex__uz">Men kitob oʻqiyapman.</p>
  <p class="pe-ex__why">Ixtiyoriy: bir qatorda nega shu shakl ishlatilgani.</p>
</div>
```

### Alphabet cards — three families
The signature visual of the alphabet block. `--same` = looks Latin and sounds Latin;
`--false` = **soxta doʻst**, looks Latin but sounds different (В Н Р С У Х);
`--new` = a brand-new shape. The false-friend cards get an automatic ⚠ before the sound.
```html
<div class="pr-cyr">
  <div class="pr-cyr__c pr-cyr__c--false">
    <span class="pr-cyr__ch">Р р</span>
    <span class="pr-cyr__rom">r</span>
    <span class="pr-cyr__uz">"P" emas! — "rahmat"dagi r</span>
  </div>
</div>
```

### Gender fork — the Russian 받침 switch
Russian branches on gender more than on anything else. Use this **every time** a form has an
-ый / -ая / -ое choice, or a past tense -л / -ла / -ло.
```html
<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">но́в<span class="pr-end">ый</span> дом</p>
    <p>Undosh bilan tugaydi: дом, стол, брат.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">но́в<span class="pr-end">ая</span> кни́га</p>
    <p>-а / -я bilan tugaydi: кни́га, шко́ла, семья́.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний — oʻrta</p>
    <p class="pr-gender__form">но́в<span class="pr-end">ое</span> окно́</p>
    <p>-о / -е bilan tugaydi: окно́, мо́ре, сло́во.</p>
  </div>
</div>
```

### Case table — the six падежи
Add `class="pr-case__on"` to the row the lesson is about, so the pupil sees where they are
inside the whole system. Show the Uzbek kelishik in the `pr-case__uz` cell — always.
```html
<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Savoli</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-case__q">кто? что?</td>
      <td class="pr-case__word">кни́га</td><td class="pr-case__uz">bosh kelishik — kitob</td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">Вини́тельный</td>
      <td class="pr-case__q">кого́? что?</td>
      <td class="pr-case__word">кни́г<span class="pr-end">у</span></td>
      <td class="pr-case__uz">tushum kelishigi — kitob<b>ni</b></td></tr>
</table></div>
```

### Declension / conjugation ladder — oʻzak + qoʻshimcha → natija
Works for nouns, adjectives and verbs alike. This is Prime Russian's workhorse table.
```html
<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>я</td><td class="pr-stem">чита́</td><td class="pr-end">ю</td>
      <td class="pr-res">чита́ю</td><td class="pr-uz">men oʻqiyman</td></tr>
</table></div>
```

### Aspect pair — НСВ (jarayon) vs СВ (natija)
```html
<div class="pr-aspect">
  <div class="pr-aspect__side">
    <p class="pr-aspect__h">НСВ — что де́лать?</p>
    <p class="pr-aspect__v">чита́ть</p>
    <p>Jarayon, takror, odat. "Oʻqirdim, oʻqiyapman."</p>
  </div>
  <div class="pr-aspect__side pr-aspect__side--sv">
    <p class="pr-aspect__h">СВ — что сде́лать?</p>
    <p class="pr-aspect__v">прочита́ть</p>
    <p>Natija, bir marta, oxirigacha. "Oʻqib chiqdim."</p>
  </div>
</div>
```

### Pronunciation arrow — yozilishi → oʻqilishi
```html
<div class="pr-say">
  <span class="pr-say__from">молоко́</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[мълако́]</span>
  <span class="pr-say__why">аканье — urgʻusiz о [a] boʻlib oʻqiladi</span>
</div>
```

### Stress and minimal pairs
```html
<p>за<span class="pr-stress">́о</span>мок</p>   <!-- inline, rare -->

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">за́мок</span>
    <span class="pr-pair__uz">qulf</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">замо́к</span>
    <span class="pr-pair__uz">qalʼa, saroy</span>
  </div>
</div>
```

### Inline word with gloss
```html
<span class="pr-w"><b>шко́ла</b><span>maktab</span></span>
```

### Colour meanings on this course
`pe-chip--s` / `pe-hl--s` = **ega (подлежащее)** · `--o` = **toʻldiruvchi (дополнение)** ·
`--v` = **kesim (сказуемое)** · `--adv` = **hol** · `--neg` = **inkor** ·
`--opt` = ixtiyoriy qism. Inline in running text you may also use `.pr-stem` (oʻzak),
`.pr-end` (окончание) and `.pr-prep` (предлог). Drop a `.pe-legend` once, the first time
colours appear in a lesson.

## 6. Hard rules

- **No `<script>`, no `onclick`, no inline JS.** Interactivity = `<details>` only.
- Inline `style=` only for `pe-timeline` positions. Everything else uses kit classes.
- **No English.** If a term has no Uzbek equivalent, use the Russian one and gloss it.
- Never use a class that is not in this guide or the Prime English one — add it to the
  **PRIME RUSSIAN** CSS section and to this guide first.
- Russian text must be **real, natural, modern Russian**. Check gender agreement, case
  endings and aspect every single time. A wrong ending in a lesson that teaches endings is
  the worst bug this course can have.
- Keep every lesson self-contained: a pupil landing on PR-52 from search still gets the
  pattern strip, examples and practice without reading PR-1.

## 7. Relationship to the rest of the site

- `corner` "Zamonaviy / Oson / Oʻrta rus hikoyalari" = free reading practice, no lesson
  attached.
- `practice` "Часть 61 …" Russian tests = older standalone drills, written **in Russian**.
  Prime Russian practices are different: they are written **in Uzbek** and each one is
  bolted to its lesson.
- **Prime Russian = the language itself, from zero, in order.**

## 8. The user's own tips

*(Empty for now — when the user shares how they want Russian taught, it goes here and
overrides the generic advice above.)*

---

## How to ask

- **"Make the next 3 Prime Russian tutorials"** — Claude checks the highest `PR-` number,
  continues in toc order, writes the batch file, imports it, and gives the Railway command.
- The working rhythm from PR-6 is **3 lessons at a time, all three legs together**:
  tutorial → practice → reading → audio. See the Prime Russian section of `CLAUDE.md`.
- **"Redo PR-3"** — rewrite that one with `--republish`.
