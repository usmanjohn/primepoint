# Flow Studio — the daily video package

Every morning a cloud Claude routine reads this file, writes **two** complete production
packages for AI videos made in **Google Flow** (Nano Banana Pro + Veo), one for each of the
user's brothers — **Inom** and **Jonibek** — checks them with `send.py`, and sends both to the
private Telegram channel «Creative». The brothers make the videos; they do not touch this repo,
the terminal, or the site. Telegram is all they see. Each package opens with «👤 <name> uchun»
and carries `#Inom` / `#Jonibek`, so each finds his own; he presses 👍 on it when the video is made.

Not a Django app, never imported by Django, costs production nothing (like `storyvideo/`).

```
EXPLAIN_LANGUAGE: Uzbek          # everything the brother READS. Only the Flow/Veo prompts are English.
CHAT:             a private Telegram channel (the bot is an admin there); FLOW_CHAT_ID is -100…
SEND_TIME:        08:00 Tashkent (03:00 UTC), daily
PER_DAY:          2 — "for": "Inom" first, then "for": "Jonibek"; two DIFFERENT series
```

---

## 0. The run, step by step

1. **Read the history** so nothing repeats:
   ```
   git fetch origin claude/flowstudio-log 2>/dev/null && git show origin/claude/flowstudio-log:flowstudio/sent.tsv
   ```
   (Absent on the very first run — that is fine.) Also read the seed list in §6.
   The video's **№** = the number of lines in `sent.tsv` + 1 (line 1 is the Amudaryo episode, №1);
   the day's second package takes the next № after the first.
   Column 6 of `sent.tsv` says whose video it was (lines without it predate the two-brother split).
**Steps 2–5 run twice: first for Inom, then for Jonibek.** On a **Saturday** they run a third
time for the «Sonlar imperiyasi» episode (§2b, `"for": "Birga"`). Then log them all in step 6.

2. **Pick today's idea** by the rotation rule (§2) from the source pool (§3). Open the
   source file and read the actual text — the facts, numbers and answers come from there.
3. **Write the package** as JSON (§4) to `flowstudio/out/<id>.json`.
4. **Gate it**: `python3 flowstudio/send.py flowstudio/out/<id>.json --check`.
   Fix every error and re-run until it passes. Then re-read the package once as the brother
   will: would a stranger with Flow open be able to make this video from it alone?
5. **Send it**: `python3 flowstudio/send.py flowstudio/out/<id>.json`
   (needs `FLOW_BOT_TOKEN` and `FLOW_CHAT_ID` in the environment — never print them,
   never write them to a file, never put them in a commit).
6. **Log it** on the log branch (it always exists; never log on `main`):
   ```
   git fetch origin claude/flowstudio-log
   git worktree add -B claude/flowstudio-log /tmp/fslog origin/claude/flowstudio-log
   cp flowstudio/out/<id>.json /tmp/fslog/flowstudio/packages/
   printf '%s\t%s\t%s\t%s\t%s\t%s\n' "<№>" "<date>" "<id>" "<series>" "<source path>" "<Inom|Jonibek>" >> /tmp/fslog/flowstudio/sent.tsv
   git -C /tmp/fslog add flowstudio && git -C /tmp/fslog commit -m "flowstudio: №<№> <id>" \
     && git -C /tmp/fslog push origin claude/flowstudio-log
   ```
   If the push fails, the package has still been sent — say so in the final message.
   (one `cp` and one `printf` line per package, one commit for the day)
7. Finish with two lines, one per brother: the id, the title, and whether the send worked; then
   whether the push worked. If one package fails the gate or the send, still send the other.

If `send.py` fails to send (network, token), do **not** retry more than twice. Report it.

---

## 1. What the brother needs (the bar every package must clear)

**Short and doable.** The user's words (2026-10-03): *"No need to tell each stuff, like facts,
explanations. Just: generate these images, name them like that; attach that image, frame to
frame or ingredient; then the prompt."* So a package is four things, nothing else:

1. **Gʻoya** — 2–3 Uzbek sentences (`concept_uz`) + the format (`format_uz`, "7 sahna × 8 soniya = 56 soniya").
2. **Rasmlar** — reference images R1, R2 … for Nano Banana Pro, each with a short Uzbek name.
3. **Ssenariy** — who says what in each scene (built from the scenes' `lines`).
4. **Sahnalar** — per scene: the Flow mode, which R-images to use, and the Veo prompt.

Facts and sources still go in the JSON (`facts`, `sources`) and are checked, but they are
**not sent** — he does not need them. No emotion charts, no checklists, no explanations.

- **Uzbek for him, English for the machines.** Everything he reads (`title_uz`, `concept_uz`,
  `format_uz`, `name_uz`, scene `title_uz`, `lines`, `post_text_uz`) is simple spoken Uzbek
  (Latin, `ʻ` in oʻ gʻ, `ʼ` for the tutuq belgisi). Prompts are English.
- **Characters SPEAK UZBEK inside the video.** The line goes into the Veo prompt, word for word:
  `The farmer says in Uzbek with a warm, husky middle-aged male voice: "Faqat men va yana bittasi sig'adi."`
  Inside a prompt write Uzbek with a plain `'` (sig'adi, to'g'ri) — never ʻ. Give every speaker a
  voice description (age, warmth, mood) and keep it identical across scenes. Lines are short —
  one or two sentences per 8-second scene, at most two speakers per scene. An off-screen narrator
  is allowed ("An off-screen man says in Uzbek …"). Every prompt ends with
  `No subtitles, no on-screen text.` The gate checks each line is in its prompt.
- **Uzbek only — no foreign-language lines, ever.** Even when the source text is Korean (the
  Wonders shelf) or English (Life Stories), the video retells it in Uzbek.
- **Copy-paste ready.** Base refs get the `style_line` appended by `send.py`; edit refs
  (`from`) and scene prompts are sent exactly as written.

### The Flow rules (keep them)

- **Nano Banana Pro builds pictures, Veo moves them.** Anything whose exact content matters
  (who stands where, how many) gets its own reference image → **Frames to Video** with
  `start` (and `end` when the shot must land on a picture, e.g. a transformation).
- **Edit chains keep faces.** A ref with `"from": "R2"` (or a list) means: attach R2 in Nano
  Banana and give the edit prompt ("Transform this character into …, same face, same scene").
  Build character variants and key scenes this way instead of from scratch.
- **Ingredients to Video** for free movement with 1–3 refs (`attach`).
- **Text to Video** only for empty landscape. **Extend** at most once a video.
- **No text in the picture** (style line + "No subtitles, no on-screen text.").
- **9:16, 8-second scenes, 5–10 scenes.**
- **One continuity tag per character** (an eye patch, a red scarf) written into its ref prompt.
- **No violence shown, no real living person, no brand logos, no real institution's branding.**
  Historical figures are fine as respectful reconstructions.
- **Style is free per video**: photoreal cinema, or premium 3D animated feature film
  (characters can be shapes, letters, numbers, animals). Animation suits maths and grammar
  ideas — a crooked quadrilateral that grows into a square teaches more than a diagram.

---

## 2. Rotation — never the same shape two days running

**The channel is about thinking: logic, maths, science and the stories behind them** (the
user's decision, 2026-10-05). ⛔ **No language-learning videos** — no Korean, Japanese,
Russian or English lessons, proverbs, mistakes or politeness sketches. Mixing those in loses
the viewer who came for the puzzles. The old language series (Tutilgan xato LIVE, Bir maqol
ikki til, Bitta sahna toʻrt til) and Xorijda oʻqish are retired; do not bring them back unless asked.

A brother never gets the same series two days running; across any 7 days each brother gets at
least 4 different ones, and the two packages of one day are always different series. Check
`sent.tsv` (column 6) before choosing. Lines in `sent.tsv` from the retired series are history only.

| series | shape | source pool (§3) |
|---|---|---|
| **Mantiq maydoni** | puzzle drama → freeze → "Javobni izohda yozing"; answer video next week | Logic Arena |
| **Bobolar sirri** | a real scholar, a real problem, the method on screen, "you can do this too" | Matematika olami — Buyuk matematiklar |
| **Buyuk kashfiyot** | the same shape for a scholar from ELSEWHERE (Fales, Arximed, Gauss, Ramanujan) | Matematika olami — Buyuk matematiklar |
| **Nega shunday?** | a wonder of nature/science made visible, one mechanism | Wonders shelf, Matematika olami (tabiat / kundalik hayot) |
| **Hayotdagi matematika** | an everyday object hides a clever idea: why the manhole cover is round, the barcode's last digit, interest on interest, the A4 sheet | Matematika olami — kundalik hayot |
| **Hayot hikoyasi** | a quiet human story with a twist, retold in Uzbek | Life Stories shelf |
| **Special** | once a week at most: a bigger 60–90 s film (al-Xorazmiy and the birth of algebra, the twelve-coin problem as a thriller, a Powerty brand film) | any pool above |

**Bobolar sirri is only for our own region's scholars** (al-Xorazmiy, Beruniy, Ulugʻbek, Ibn Sino,
Ali Qushchi, al-Fargʻoniy…) — «bobolar» means *our* ancestors. Anyone else is «Buyuk kashfiyot».
A famous legend (Fales' shadow, Arximed's «Evrika!») is called a legend in the voice-over too.

A **Mantiq maydoni** package is the QUESTION video and ends on the question. Exactly 7 days
later (check `sent.tsv`) the ANSWER video goes to **the same brother** who made the question —
that takes priority over the rotation for his package that day.

---

## 2b. «Sonlar imperiyasi» — the ordered series (weekly, «Birga»)

A comic fairy-tale series about the number system (the user's own tale). It is **not part of
the rotation** and does not replace either brother's package: on its day it is a **third**
package, `"for": "Birga"` (one brother films the whole season; the user chose not to name him).

- **When:** every **Saturday** (Tashkent date), and only then — unless the user asks.
- **Which episode:** count the `Sonlar imperiyasi` rows in `sent.tsv`; send episode
  count + 1. Season 1 has 10 episodes; after episode 10, stop and say so in the final message.
  Never skip, never send two in one week, never send out of order.
- **Read first:** `flowstudio/series/sonlar_imperiyasi.md` (the bible: cast, catchphrases, the
  two laws — mathematically true AND funny, the joke is the maths) and the episode's text in
  `corner/management/commands/_stories_sonlar_imperiyasi_*.py` (`order` = episode).
- **Episode 1 is already written:** `flowstudio/series/sonlar_imperiyasi_ep01.json`. Copy it to
  `flowstudio/out/`, set `number` and `date`, gate, send. Episodes 2-10: write them in the same
  shape and depth.
- **The cast never changes:** take refs **verbatim** from `flowstudio/series/sonlar_imperiyasi_cast.json`
  (same id, `name_uz`, `prompt`, and the style line and voices from there). A cast ref first
  generated in an EARLIER episode (`introduced` < this episode) gets `"saved": true` — the
  brother reuses his saved image instead of making a new face. Episode-only refs use ids
  **R11 and up** and are named «N-qism: …».
- Every video ends on the episode's cliffhanger image with the off-screen line
  «Davomi — powerty.uz da.»; `post_text_uz` starts «Sonlar imperiyasi · N-qism» and carries
  `#SonlarImperiyasi`. Uzbek only, as everywhere.
- Log it like any package (`sent.tsv` column 6 = `Birga`, column 4 = `Sonlar imperiyasi`).

---

## 3. The source pool — where true content lives

Read the file; never write a fact, date, number or answer from memory.

| pool | path | notes |
|---|---|---|
| Logic Arena (32 puzzles) | `logic/management/commands/_puzzles_logic_*.py` | `answer_key` is brute-force verified; `solution_uz` holds the Uzbek steps. ⛔ **Never spoil a sealed puzzle:** compute each puzzle's dates from its file's `SCHEDULE` + `round` (opens = start + 7×(round−1) days, reveal = opens + 7). Use only puzzles already OPEN; a QUESTION video may say «javobni powerty.uz/logic da yuboring»; the ANSWER video is sent no earlier than the puzzle's reveal date. |
| Matematika olami | `corner/management/commands/_stories_matematika_olami_*.py`, toc `toc_matematika_olami.txt` | history, nature, daily-life maths, puzzles — Uzbek, facts checked |
| Wonders | `corner/management/commands/_stories_wonders_*.py`, `toc_wonders.txt` | Korean texts with Uzbek titles; use the FACT, tell it in Uzbek |
| Life Stories | `corner/management/commands/_stories_life_*.py` | English narratives, quiet twist |
| Existing animatics | `storyvideo/stories/pm*.py`, `mo*.py` (maths only — never `ko*`) | ideas already proven as paper animatics; a cinematic remake is welcome |

If a pool runs dry, say so in the final message — the user writes new Logic Arena puzzles and
Corner stories for this; never invent a fact to fill the gap.

Put the file path(s) you used in `sources`, and every checkable claim in `facts`.

---

## 4. The package JSON

`flowstudio/example.json` is a complete, passing package (the Amudaryo episode, №1).
Match its shape; do not copy its content.

```json
{
  "id": "2026-10-05-kashfiyot-fales",
  "number": 3,
  "for": "Inom",
  "date": "2026-10-05",
  "series": "Buyuk kashfiyot",
  "title_uz": "Soya va piramida",
  "concept_uz": "2–3 sentences: who, where, the turn.",
  "format_uz": "7 sahna × 8 soniya = 56 soniya",
  "sources": ["corner/management/commands/_stories_matematika_olami_13_15.py (story 6)"],
  "facts": [{"claim": "…", "source": "…"}],
  "style_line": "Premium 3D animated feature film style, … No text, no letters, no watermark.",
  "refs": [
    {"id": "R1", "name_uz": "Muhit: Giza", "prompt": "Vertical 9:16 …"},
    {"id": "R2", "name_uz": "Fales", "prompt": "Vertical 9:16 …"},
    {"id": "R3", "name_uz": "Fales tayoq bilan", "from": "R2", "prompt": "Change the scene: …"},
    {"id": "R4", "name_uz": "Hammasi", "from": ["R1", "R2"], "prompt": "Combine the attached …"}
  ],
  "scenes": [
    {"n": 1, "title_uz": "Savol", "method": "Frames to Video", "start": "R4", "end": "",
     "prompt": "… He says in Uzbek with a calm old male voice: \"Bu piramida qanchalik baland?\" No subtitles, no on-screen text.",
     "lines": [{"who": "Fales", "text": "Bu piramida qanchalik baland?"}]},
    {"n": 2, "title_uz": "…", "method": "Ingredients to Video", "attach": ["R2", "R1"], "prompt": "…", "lines": []},
    {"n": 3, "title_uz": "…", "method": "Extend", "extends": "2", "prompt": "…", "lines": []}
  ],
  "post_text_uz": "Instagram/Telegram caption, Uzbek, hashtags at the end"
}
```

Field rules (`send.py --check` enforces them):

- `for` = `Inom` or `Jonibek` (whose video it is). `number` = the video's №. Refs are `R1, R2 …`; a `from` points only at EARLIER refs.
- `method` ∈ `Frames to Video` (needs `start`, optional `end`) · `Ingredients to Video`
  (`attach` 1–3 refs) · `Text to Video` · `Extend` (`extends` = an earlier scene's `n`).
- Every scene prompt is English, contains each of its `lines` word for word (apostrophes
  aside), says "in Uzbek" when anyone speaks, and ends with "No subtitles, no on-screen text."
- At least half the scenes have Uzbek lines. 4–12 scenes. `concept_uz` under 500 characters.

## 5. Quality bar — read before writing

- **The hook is in the first 2 seconds**, with a sound. Not a title card.
- **One idea per video.** If the logline needs "and", cut.
- **A turn**: something the viewer did not expect (the goat goes *back*; Beruniy only
  needed one triangle; the polite word was the rude one).
- **The ending asks for something**: a comment, a guess, a share. Puzzles always freeze
  on a question.
- **Uzbek that sounds spoken**, not translated — short sentences, a storyteller's rhythm.
- **Facts are true and sourced.** A legend is called a legend.
- **Never the price**: do not say Powerty is free; the end card says «powerty.uz».
- **A hook for the next episode** in the last line when it fits (the old circle's wink:
  "Endi… doira boʻlishni oʻrgan").

---

## 6. Already made (do not repeat)

- `2026-10-03-mantiq-amudaryo` — Mantiq maydoni #1, wolf/goat/cabbage on the Amudaryo
  (Logic puzzle 3). Written by hand as a Claude doc, not sent by the bot.

---

## 7. How it arrives (`send.py` does this — do not imitate it in the JSON)

Five or six messages, all replies to the first (pinned) one, each tagged `№N · k/total`:
👤 whose + 🎬 title + Gʻoya + Format → 1️⃣ Rasmlar → 2️⃣ Ssenariy → 3️⃣ Flowʼda yaratish → 4️⃣ Post matni,
then the whole package as a `.txt` file. In a Telegram group with Topics each video gets its
own topic instead.
