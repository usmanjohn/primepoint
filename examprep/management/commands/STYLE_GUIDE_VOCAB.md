# Vocabulary Bank Writing Guide (for Claude)

This guide tells Claude HOW to write **vocabulary-bank entries** — the rows of the table at
`/examprep/<track>/vocab/` and the families at `/examprep/<track>/vocab/roots/`.
Sibling of the grammar bank: a **reference**, not a lesson.

> ⚠️ **Written in English for Claude — the ENTRIES YOU PRODUCE ARE UZBEK + KOREAN, never
> English.** Korean is the material; Uzbek is the explanation.

---

## 1. The big idea: root families (한자 어근)

Most TOPIK II vocabulary is Sino-Korean, and each syllable carries meaning. A student who
learns **출(出) = chiqmoq** can decode 출구, 출근, 출발, 출석, 제출, 수출 — six words for the
price of one, plus the ability to *guess* unseen ones in 읽기. **This is the point of the
bank.** Prefer words that belong to a family; give every Sino-Korean word its `hanja` and
its `roots`.

A word may have two roots — 출입구 is 출(出) + 입(入) + 구(口). List all of the ones the bank
defines; the word then appears in each family.

**Homophone roots.** Several syllables carry more than one root: 소(所) "joy" vs 소(消)
"sarflash", 정(定)/정(政)/정(情), 경(經)/경(境), 자(者)/자(資), 기(技)/기(氣)/기(機). Those get
one `ROOTS` row each, and a word must name the one it means as `"소(所)"` — `import_vocab`
rejects the bare `"소"` as ambiguous rather than guessing. Before adding a new homophone
root, grep the earlier files for the bare syllable: adding it makes those references
ambiguous, and they all need the disambiguated form.

Native-Korean words (먹다, 예쁘다, 빨리) have no Hanja — leave `hanja` blank and `roots` empty.
They still belong in the bank, just under their theme.

## 2. `ROOTS` entries

```python
{
    "syllable": "출",
    "hanja":    "出",
    "meaning":  "chiqmoq — chiqish, tashqariga",       # Uzbek gloss, ≤200 chars
    "note":     "<p>Deyarli doim <b>ichkaridan tashqariga</b> harakati...</p>",
    "order":    100,
}
```

- `meaning` formula: **`asosiy ma'no — qo'shimcha ma'nolar`**.
- `note` (optional, HTML): what the root does to a word, and the trap to watch for —
  e.g. that 수(數) "son" and 수(水) "suv" are different roots with the same syllable.
- **Homophone roots are separate rows.** 수(數) and 수(水) share a syllable but not a
  meaning; the importer matches on `syllable` + `hanja`, so give both.
- Give each root file its own `order` decade so families group sensibly.

## 3. `WORDS` entries

```python
{
    "word":        "출근",
    "hanja":       "出勤",
    "roots":       ["출"],
    "pos":         "noun",       # noun / verb / adj / adv / phrase / count
    "topic":       "work",       # see §4
    "level":       2,            # TOPIK 1-6
    "freq":        3,            # 1-3 stars
    "meaning":     "ishga chiqish, ishga borish",
    "collocation": "출근하다 · 출근 시간 · 출근길",
    "note":        "<p>Teskarisi <b>퇴근</b> (ishdan qaytish)...</p>",
    "examples":    [("보통 여덟 시에 출근해요.", "Odatda soat sakkizda ishga boraman.")],
    "synonyms":    [],
    "antonyms":    [("퇴근", "ishdan chiqish — 出↔退")],
    "related":     [("출퇴근", "ishga borib-kelish")],
}
```

Only `word` and `meaning` are required, but a thin row is a useless row.

## 4. `topic` — the theme (allowed values)

`daily` · `person` · `emotion` · `body` · `food` · `home` · `shopping` · `transport` ·
`work` · `school` · `society` · `economy` · `environment` · `science` · `culture` ·
`media` · `time` · `place` · `abstract`

(Exact labels live in `VOCAB_TOPIC_CHOICES` in `examprep/models.py`.) Pick by what the word
is *about*, not by its grammar.

## 5. `meaning` — the table gloss (≤200 chars)

The most-read string on the page. Plain Uzbek, comma-separated senses, no sentence.

- ✅ `"ishga chiqish, ishga borish"`
- ✅ `"eksport — tashqariga sotish"`
- ❌ `"Bu so'z ishga borishni bildiradi va ..."`

If the word has a **Hanja-literal** sense worth showing, put it after an em-dash:
`"eksport — 'chiqarib sotish'"`. That is what makes the root click.

## 6. `collocation` — how the word actually appears

Middle-dot separated, 2–4 items: the 하다-form, the compounds, the verb it takes.
`"출근하다 · 출근 시간 · 출근길"`. TOPIK tests words in phrases, not alone — this column is
often more useful than the definition.

## 7. `examples` — 1–3 per word

`(korean, uzbek)` tuples. **The first is shown in the table**, so make it the shortest,
most typical sentence. TOPIK-flavoured topics (환경, 건강, 취업, 교육), natural Uzbek
translations, and the user's pupils' names (Afsona, Jasur, Sherbek) where a name is needed.

Level 1–2 words get a simple sentence; level 5–6 words should get a sentence in the
**written register** (`-(느)ㄴ다`), since that is where the student will meet them.

## 8. `synonyms` / `antonyms` / `related` — notes must state the DIFFERENCE

Same rule as the grammar bank. `(word, note)` tuples.

- ✅ `("퇴근", "ishdan chiqish — 出↔退")`
- ✅ `("값", "값 = og'zaki narx; 가격 = rasmiy/yozma")`
- ❌ `("가격", "bu ham narx")`

**Antonyms matter as much as synonyms for TOPIK** — 수출/수입, 증가/감소, 입구/출구 are
routinely the answer pair. Write the pair from both sides where both words are in the bank;
the importer cross-links them by exact word match.

## 9. `freq` — 1 to 3 stars

`3` = on essentially every paper · `2` = regular · `1` = advanced/rare (TOPIK 5-6 reading).
Be honest; if everything is 3 the column stops meaning anything.

## 10. Coverage rule

One data file per group (roots batch, or a theme). Give each file its own `order` decade so
the table's sections do not interleave. Order `WORDS` easy → hard within a file.

## 11. Workflow

1. Read this guide.
2. Read `toc_topik_vocab.txt` (header gives TRACK, AUTHOR; body is the group list).
3. Check where to continue:
   `VocabEntry.objects.filter(track__name='TOPIK').order_by('-order').first()`
   and `VocabRoot.objects.filter(track__name='TOPIK').values_list('syllable', flat=True)`
4. Write `_vocab_topik_<group>.py` with `TRACK` + optional `ROOTS` + `WORDS`.
5. Import: `python manage.py import_vocab <file> --author=<AUTHOR>` (`--republish` to
   overwrite; it rebuilds examples, roots and relations and re-resolves cross-links).
6. Give the `railway run python manage.py import_vocab ...` command for production —
   automatically, every time (see CLAUDE.md → Deployment).

## 12. Foydalanuvchining maslahatlari (user's own tips)

The user's Reading method already applies here and **overrides generic advice**:
**"Ko'p o'qing, kam tarjima qiling"** — recognising a word on sight beats writing it out;
train the eye, not the hand. Prefer **sifat (형용사), ravish (부사), fe'l (동사)** over nouns
when choosing what to add, since those decide the answers. Re-reading a text after a day or
two beats drilling a word list.

_(Foydalanuvchi lug'at bo'yicha boshqa maslahatlarini ulashganda — shu yerga yoz.)_
