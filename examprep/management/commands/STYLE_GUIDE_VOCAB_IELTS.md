# IELTS Vocabulary Bank Writing Guide (for Claude)

This guide tells Claude HOW to write **IELTS vocabulary-bank entries** — the rows of the
table at `/examprep/ielts/vocab/` and the families at `/examprep/ielts/vocab/roots/`.
English-track sibling of `STYLE_GUIDE_VOCAB.md` (TOPIK's): identical data format, importer
and page; different language and different roots.

> ⚠️ **Written in English for Claude — the ENTRIES YOU PRODUCE ARE UZBEK + ENGLISH.**
> English is the material (the word, its collocations, its example sentences); **Uzbek is
> every word of explanation** — meaning, note, and the "how it differs" notes. Never Russian.

---

## 1. The big idea: root families (Latin & Greek)

Roughly 60% of academic English comes from Latin and Greek, and each root carries meaning.
A student who learns **spect = qaramoq** can decode *inspect, spectator, perspective,
prospect, spectacular, retrospective* — six words for the price of one, plus the ability to
*guess* unseen ones in Reading. **This is the point of the bank**, exactly as Hanja roots
are for TOPIK.

Give every Latin/Greek-derived word its `roots`, and use `hanja` for how the word is built.

A word may have two roots — *international* is `inter` + `nat`; *telephone* is `tele` +
`phon`. List all of the ones the bank defines; the word then appears in each family.

**Prefixes and suffixes are roots too** on this track: `re-`, `pre-`, `sub-`, `inter-`,
`bene-`, `-able`, `-ology`. Store them with the hyphen in place (`"re-"`, `"-ology"`) so the
family page reads correctly, and use them when the affix is what actually unlocks the word.

Germanic everyday words (*get, keep, hard, quite*) have no classical root — leave `roots`
empty and `hanja` blank. They still belong in the bank under their theme, especially the
phrasal verbs and collocations Speaking needs.

**Homograph roots.** A few forms carry more than one meaning — `mod` (measure/manner),
`sol` (sun / alone), `pen` (hang / punish), `port` (carry) vs `port` (harbour). Give each a
separate `ROOTS` row with its own origin in `hanja`, and name the one you mean as
`"sol(sun)"` in a word's `roots` list — `import_vocab` rejects the bare form as ambiguous
rather than guessing. Before adding a second sense of an existing root, grep the earlier
files for the bare form: every reference to it must become the disambiguated one.

## 2. `ROOTS` entries

```python
{
    "syllable": "spect",                       # the root itself (max 20 chars)
    "hanja":    "specere (lat.) — qaramoq",    # ORIGIN — see below
    "meaning":  "qaramoq — ko‘rmoq, kuzatmoq",  # Uzbek gloss, ≤200 chars
    "note":     "<p>Ko‘pincha old qo‘shimcha ma’noni burad: <b>in-</b>spect (ichiga qaramoq)…</p>",
    "order":    100,
}
```

- `syllable` holds the root as students meet it: `spect`, `duc`, `graph`, `bene`, `re-`.
  When a root has two spellings, write the pair: `"duc / duct"`, `"vert / vers"`.
- `hanja` is the **origin column** (`Kelib chiqishi` on the page): the Latin/Greek source
  and its literal sense — `"specere (lat.) — qaramoq"`, `"graphein (yun.) — yozmoq"`.
  It is never Hanja on this track; the column is shared, the content is per-track.
- `meaning` formula: **`asosiy ma'no — qo'shimcha ma'nolar`**.
- `note` (optional, HTML): what the root does inside a word, and the trap — a false friend
  (*material* ≠ *materialistic*), or a lookalike that is NOT from this root.
- Give each root file its own `order` decade so families group sensibly.

## 3. `WORDS` entries

```python
{
    "word":        "inspect",
    "hanja":       "in- + spect",     # how the word is BUILT — see §5
    "roots":       ["spect"],
    "pos":         "verb",            # noun / verb / adj / adv / phrase / count
    "topic":       "academic",        # see §4
    "level":       4,                 # 1-6 → Band 5 … Band 7.5+
    "freq":        2,                 # 1-3 stars
    "meaning":     "sinchiklab tekshirmoq, ko‘zdan kechirmoq",
    "collocation": "inspect a building · inspect the data · a routine inspection",
    "note":        "<p><b>examine</b> ga yaqin, lekin rasmiy tekshiruv ma’nosi kuchliroq…</p>",
    "examples":    [("Officials inspect the factories twice a year.",
                     "Rasmiylar zavodlarni yiliga ikki marta tekshiradi.")],
    "synonyms":    [("examine", "examine = umumiy o‘rganish; inspect = rasmiy, qoidaga muvofiqlikni tekshirish")],
    "antonyms":    [],
    "related":     [("inspection", "ot shakli")],
}
```

Only `word` and `meaning` are required, but a thin row is a useless row.

**What to include.** Prefer words that pay in the exam over words that merely exist:
- academic verbs and their noun forms (*analyse/analysis*, *acquire/acquisition*);
- Task 1 trend language (*soar, plummet, level off, marginal, threefold*);
- Task 2 topic vocabulary (education, environment, crime, technology, health);
- precise adjectives and adverbs that replace *very + weak word* (*substantial*,
  *widespread*, *markedly*);
- phrases and collocations — `pos: "phrase"` — because IELTS marks *Lexical Resource* on
  collocation, not on rare single words.

Avoid the "impressive word" trap: *plethora*, *myriad* and *ameliorate* used wrongly lose
more marks than plain words used well. If a word is easy to misuse, say so in `note`.

## 4. `topic` — the theme (allowed values on IELTS)

`academic` · `data` · `school` · `work` · `society` · `economy` · `environment` ·
`science` · `health` · `crime` · `government` · `culture` · `media` · `tourism` ·
`person` · `daily` · `abstract`

Two of these are IELTS-specific and carry a lot of weight:
- **`data`** — Task 1 language: trends, quantities, comparison, chart nouns.
- **`academic`** — the subject-neutral verbs, nouns and adverbs that hold an essay
  together (*constitute, undermine, arguably, a considerable proportion*).

(Exact labels live in `banklabels.VOCAB_TOPIC_LABELS['ielts']`.) Pick by what the word is
*about*, not by its grammar.

## 5. `hanja` — the build column

On IELTS this column shows **how the word is assembled**, which is what makes the root
click: `"in- + spect"`, `"trans- + port"`, `"bio- + graph + -y"`. Leave it blank for
Germanic words. Keep it ≤ 60 characters.

## 6. `meaning` — the table gloss (≤200 chars)

The most-read string on the page. Plain Uzbek, comma-separated senses, no sentence.

- ✅ `"sinchiklab tekshirmoq, ko‘zdan kechirmoq"`
- ✅ `"keskin ko‘tarilmoq — juda tez o‘smoq"`
- ❌ `"Bu so'z tekshirishni bildiradi va ..."`

If the **literal root sense** is worth showing, put it after an em-dash:
`"istiqbol — 'oldinga qarash'"`. That is what makes the family memorable.

## 7. `collocation` — how the word actually appears

Middle-dot separated, 2–4 items, **in English**: the verb it takes, the noun it modifies,
the fixed phrase. `"a sharp increase · increase sharply · a steady rise"`.
IELTS marks collocation directly, so this column is often more useful than the definition —
and it is where you show the grammar pattern too (`"result IN" vs "result FROM"`).

## 8. `examples` — 1–3 per word

`(english, uzbek)` tuples — the same field the TOPIK files use for Korean. **The first is
shown in the table**, so make it the shortest, most typical sentence.

- IELTS-flavoured topics; Task 1 words get a real data sentence
  (*"Car ownership rose sharply between 2000 and 2010."*).
- English at genuine exam register — Band 7 academic for writing words, natural spoken
  English for Speaking words.
- Natural Uzbek translations, not word-for-word.
- The user's pupils' names (Afsona, Jasur, Sherbek) where a name is needed — Speaking
  examples only; writing examples stay impersonal.

## 9. `synonyms` / `antonyms` / `related` — notes must state the DIFFERENCE

Same rule as the grammar bank. `(word, note)` tuples.

- ✅ `("examine", "examine = umumiy o‘rganish; inspect = rasmiy tekshiruv")`
- ✅ `("plummet", "plummet = keskin PASAYISH; soar = keskin KO‘TARILISH")`
- ❌ `("increase", "bu ham o‘sish")`

**Antonym pairs matter as much as synonyms on IELTS** — *rise/fall*, *soar/plummet*,
*majority/minority*, *urban/rural* are how Task 1 sentences get built and how Reading
paraphrases work. Write the pair from both sides where both words are in the bank; the
importer cross-links them by exact word match.

For near-synonyms, say **which register or collocation** separates them — that is the real
difference in English: `"take part in = neytral; participate in = rasmiy/akademik"`.

## 10. `freq` — 1 to 3 stars

`3` = you will use it in almost every test · `2` = regularly useful · `1` = advanced polish.
Be honest; if everything is 3 the column stops meaning anything.

## 11. Coverage rule

One data file per group (a roots batch, or a theme). Give each file its own `order` decade
so the table's sections do not interleave. Order `WORDS` easy → hard within a file.

⚠️ **Each root is defined in exactly one file, and files are imported in the order
`toc_ielts_vocab.txt` gives.** A later file may reference any root defined above it, never
below; `import_vocab` errors out on an unknown root rather than silently dropping the word
from its family. Never copy a root definition into a second file.

## 12. Workflow

1. Read this guide.
2. Read `toc_ielts_vocab.txt` (header gives TRACK, AUTHOR and the required import order).
3. Check where to continue:
   `VocabEntry.objects.filter(track__name='IELTS').order_by('-order').first()`
   and `VocabRoot.objects.filter(track__name='IELTS').values_list('syllable', flat=True)`
4. Write `_vocab_ielts_<group>.py` with `TRACK` + optional `ROOTS` + `WORDS`.
   `TRACK` must be `{"name": "IELTS", …}` — the importer matches the track by name.
5. Import: `python manage.py import_vocab <file> --author=<AUTHOR>` (`--republish` to
   overwrite; it rebuilds examples, root links and relations and re-resolves cross-links).
6. Give the `railway run python manage.py import_vocab ...` commands **in toc order** for
   production — automatically, every time (see CLAUDE.md → Deployment).

## 13. Foydalanuvchining maslahatlari (user's own tips)

The user's method carries over from the TOPIK bank and **overrides generic advice**:
**"Ko'p o'qing, kam tarjima qiling"** — recognising a word on sight beats writing it out.
Prefer **sifat, ravish, fe'l** over nouns when choosing what to add: they decide the
answers, and on IELTS they are also what lifts *Lexical Resource*. Re-reading a text after a
day or two beats drilling a word list.

_(Foydalanuvchi IELTS lug'ati bo'yicha boshqa maslahatlarini ulashganda — shu yerga yoz.)_
