# Flow Studio — the daily video package

Every morning a cloud Claude routine reads this file, writes **one** complete production
package for an AI video made in **Google Flow** (Nano Banana Pro + Veo), checks it with
`send.py`, and sends it to a private Telegram channel. The reader is the user's brother: he makes
the videos, he does not touch this repo, the terminal, or the site. Telegram is all he sees.

Not a Django app, never imported by Django, costs production nothing (like `storyvideo/`).

```
EXPLAIN_LANGUAGE: Uzbek          # everything the brother READS. Only the Flow/Veo prompts are English.
CHAT:             the user's own Telegram (the brother uses it); FLOW_CHAT_ID is a number
SEND_TIME:        08:00 Tashkent (03:00 UTC), daily
```

---

## 0. The run, step by step

1. **Read the history** so nothing repeats:
   ```
   git fetch origin claude/flowstudio-log 2>/dev/null && git show origin/claude/flowstudio-log:flowstudio/sent.tsv
   ```
   (Absent on the very first run — that is fine.) Also read the seed list in §6.
   The video's **№** = the number of lines in `sent.tsv` + 1 (line 1 is the Amudaryo episode, №1).
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
   printf '%s\t%s\t%s\t%s\t%s\n' "<№>" "<date>" "<id>" "<series>" "<source path>" >> /tmp/fslog/flowstudio/sent.tsv
   git -C /tmp/fslog add flowstudio && git -C /tmp/fslog commit -m "flowstudio: №<№> <id>" \
     && git -C /tmp/fslog push origin claude/flowstudio-log
   ```
   If the push fails, the package has still been sent — say so in the final message.
7. Finish with one line: the id, the title, and whether the send and the push worked.

If `send.py` fails to send (network, token), do **not** retry more than twice. Report it.

---

## 1. What the brother needs (the bar every package must clear)

- **Uzbek for him, English for the machines.** He reads little English. Everything he *reads* —
  `logline`, `what`, `emotion`, `check`, ingredient `check`, `emotion_arc`, `facts[].claim`, every
  `edit` field, `voice_uz`, `title_uz` — is natural, simple Uzbek (Latin, `ʻ` in oʻ gʻ, `ʼ` for
  the tutuq belgisi and after foreign names: Veoʼga, CapCutʼda). Only `prompt`, `frame_prompt`,
  `end_frame_prompt`, `video_prompt` and `style_line` are English. Flow's button names stay as
  they are in Flow (Frames to Video, Extend…); `send.py` adds the Uzbek gloss.
- **Copy-paste ready.** Every prompt is complete — the style line is appended by `send.py`,
  so do not paste it in yourself. He should never have to write a prompt.
- **The method on every shot**, said plainly: Frames to Video / Ingredients to Video /
  Text to Video / Extend / Editor-only, and **which ingredients to attach**.
- **The model on every shot**: Lite (blocking tests) · Fast (all drafts) · Quality (only
  the hero shots, 3–6 per video). Credits are finite: Ultra ≈ 25,000/month, Quality ≈ 100
  a clip, Fast ≈ 10 with the Ultra discount. Aim for ≤ 1,500 credits a video.
- **Emotion per shot** — what the viewer should feel, and what on screen produces it.
- **Uzbek voice lines** per shot, ready to record. Nobody on screen speaks (Veo cannot do
  Uzbek speech or lip-sync), a narrator tells. A character may speak a *foreign* line
  (Korean, Japanese, English, Russian) only if the language IS the point — and then say in
  `check` that he must listen for gibberish.
- **A check per shot**: the one thing to look at before keeping the clip.

### The Flow rules (learned on episode 1, keep them)

- **Nano Banana Pro builds pictures, Veo moves them.** Anything whose *exact content*
  matters (who stands where, how many of something, what the board says) gets a still
  start frame first → **Frames to Video**. A wrong extra animal ruins a puzzle.
- **Ingredients to Video** only when ≤ 3 subjects must keep their faces while moving freely.
  `attach` lists 1–3 ingredient names.
- **Text to Video** only for empty landscape / atmosphere.
- **Extend** at most once or twice in a video (quality drifts).
- **No text in the picture.** Veo and Nano Banana garble letters. All words — captions,
  numbers, labels, counters — go in the edit (CapCut). Every prompt says so via the style line.
- **Every video prompt ends with an audio line containing "No speech, no music."** Veo
  invents gibberish voices otherwise; music goes in the edit. Keep its SFX.
- **9:16, 8 s clips, 1080p upscale.** Most clips are trimmed to 3–6 s in the edit.
- **One continuity tag per character** (a patch over one eye, a red scarf, a chipped cup)
  so a wrong duplicate is spotted at a glance. Name it in the ingredient's `check`.
- **No violence shown, no real living person's face, no brand logos, no real
  institution's branding** (no fake GKS letterhead, no university crest). Historical
  figures (Beruniy, Ulugʻbek, Sejong) are fine as respectful reconstructions.
- **Cover = frame 0.** Describe the cover still (Nano Banana) and its overlay words.

---

## 2. Rotation — never the same shape two days running

Cycle through these series; across any 7 days at least 5 different ones. Check
`sent.tsv` before choosing.

| series | shape | source pool (§3) |
|---|---|---|
| **Mantiq maydoni** | puzzle drama → freeze → "Javobni izohda yozing"; answer video next week | Logic Arena |
| **Bobolar sirri** | a real scholar, a real problem, the method on screen, "you can do this too" | Matematika olami — Buyuk matematiklar |
| **Tutilgan xato LIVE** | live-action comedy: mistake → social cost → rewind → correct line → rule | storyvideo ko04–ko15, Prime course lessons |
| **Bir maqol, ikki til** | the proverb shown literally, then its Uzbek twin | Korean proverbs shelf, storyvideo ko16–ko27 |
| **Nega shunday?** | a wonder of nature/science made visible, one mechanism | Wonders shelf, Matematika olami (tabiat / kundalik hayot) |
| **Xorijda oʻqish** | a pupil's path abroad as a short drama; facts only from the data | abroad/ |
| **Bitta sahna, toʻrt til** | one everyday scene replayed in Korean / Japanese / Russian / English | Prime courses (greetings, politeness levels) |
| **Hayot hikoyasi** | a quiet human story with a twist, retold in Uzbek | Life Stories shelf, Koreya olami |
| **Special** | once a week at most: a bigger 60–90 s film (Hangul's birth, the SAT module thriller, a Powerty brand film) | any |

A **Mantiq maydoni** package must contain BOTH parts (question + answer) in one package,
because the answer is posted a week later and must be planned from day one.

---

## 3. The source pool — where true content lives

Read the file; never write a fact, date, number or answer from memory.

| pool | path | notes |
|---|---|---|
| Logic Arena (16 puzzles) | `logic/management/commands/_puzzles_logic_*.py` | `answer_key` is brute-force verified; `solution_uz` holds the Uzbek steps |
| Matematika olami | `corner/management/commands/_stories_matematika_olami_*.py`, toc `toc_matematika_olami.txt` | history, nature, daily-life maths, puzzles — Uzbek, facts checked |
| Koreya olami | `corner/management/commands/_stories_koreya_olami_*.py` | Uzbek prose about Korean |
| Korean proverbs | `corner/management/commands/_stories_proverbs_*.py`, `toc_korean_proverbs.txt` | |
| Wonders | `corner/management/commands/_stories_wonders_*.py`, `toc_wonders.txt` | Korean texts with Uzbek titles; wow-facts |
| Life Stories | `corner/management/commands/_stories_life_*.py` | English narratives, quiet twist |
| SAT olami | `corner/management/commands/_stories_sat_olami_*.py` | the exam itself |
| Study abroad | `abroad/management/commands/_abroad_*.py`, `STYLE_GUIDE_ABROAD.md` | every fact has `source_url` + `last_checked`; ⛔ never a deadline or amount not in the file, and never a countdown on an `is_estimate` date |
| Existing animatics | `storyvideo/SERIES.md`, `storyvideo/stories/` | ideas already proven as paper animatics; a cinematic remake is welcome |
| Prime courses | `tutorial/management/commands/toc_prime_*.txt` | lesson topics for language sketches |

Put the file path(s) you used in `sources`, and every checkable claim in `facts`.

---

## 4. The package JSON

`flowstudio/example.json` is a complete, passing package (the Amudaryo episode, Part 1
only, №1) — Uzbek explanations, English prompts. Match its depth and tone; do not copy its content.

```json
{
  "id": "2026-10-05-bobolar-beruniy-earth",
  "number": 2,
  "date": "2026-10-05",
  "series": "Bobolar sirri",
  "title_uz": "Beruniy Yerni oʻlchaydi",
  "logline": "One or two sentences: who, where, what goes wrong or what is discovered.",
  "parts": [ { "name": "Part 1", "length": "45 s" } ],
  "sources": ["corner/management/commands/_stories_matematika_olami_04.py"],
  "facts": [ { "claim": "…", "source": "path or URL" } ],
  "emotion_arc": [ { "time": "0-4 s", "beat": "Hook", "feel": "curiosity" } ],
  "style_line": "Cinematic photoreal, … No text, no letters, no watermark.",
  "ingredients": [
    { "name": "FARMER", "prompt": "Character reference sheet of …", "check": "same face in all four views" }
  ],
  "shots": [
    {
      "n": "1", "part": "Part 1", "time": "0:00-0:04",
      "what": "What the viewer sees, one sentence.",
      "method": "Frames to Video",
      "model": "Fast",
      "attach": ["FARMER", "BOAT", "NEAR BANK"],
      "frame_prompt": "…", "end_frame_prompt": "",
      "video_prompt": "… Audio: water, oars. No speech, no music.",
      "extends": "",
      "emotion": "tension → laugh",
      "voice_uz": "Boʻrini olsa… karam ketdi.",
      "check": "goat still on the near bank"
    }
  ],
  "edit": {
    "captions": "…", "music": "…", "cover": "…",
    "post_text_uz": "…",
    "checklist": ["…", "…"]
  }
}
```

Field rules (`send.py --check` enforces the mechanical ones):

- `number` = the video's №, shown on every message (`📦 №2 · 5/15`) and as `#video002`.
- `method` ∈ `Frames to Video` · `Ingredients to Video` · `Text to Video` · `Extend` · `Editor`.
- `model` ∈ `Lite` · `Fast` · `Quality` · `Fast→Quality` · `—` (Editor shots).
- Frames → `frame_prompt` required, `attach` = the ingredients to give Nano Banana Pro
  (any number). `end_frame_prompt` when the shot must land on a specific picture.
- Ingredients → `attach` has 1–3 names; `video_prompt` required, no `frame_prompt`.
- Text → `video_prompt` only. Extend → `extends` = the shot number it continues.
- Every `attach` name exists in `ingredients`. Every `video_prompt` contains "No speech".
- **Uzbek fields** (`title_uz`, `voice_uz`, `post_text_uz`): proper `ʻ` (U+02BB) in oʻ gʻ
  and the tutuq belgisi `ʼ` — never `'`, `‘`, `’` or a backtick; no Cyrillic.
- Prompts are in **English** (the models follow it best). No Uzbek inside prompts.
- 8–16 shots per part. Total Quality clips ≤ 6 per part.

---

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
- End card: the series name + «powerty.uz», in the subject's accent colour from
  `storyvideo/SERIES.md` §2 (logic olive `#5f7d3a`, math gold `#c9923a`, korean blue `#3b6ea5`,
  japanese indigo `#3d4a7d`, russian violet `#7a5aa0`, english teal `#2e7d7a`,
  sat graphite `#24405e`, story wood `#c08a52`).

---

## 6. Already made (do not repeat)

- `2026-10-03-mantiq-amudaryo` — Mantiq maydoni #1, wolf/goat/cabbage on the Amudaryo
  (Logic puzzle 3). Written by hand as a Claude doc, not sent by the bot.

---

## 7. How it arrives (`send.py` does this — do not imitate it in the JSON)

1. A **contents message** (pinned): №, title, hashtags `#video00N #SeriesName`, logline, the
   numbered contents, and a short Uzbek legend of the Flow methods and models.
2. Every other message is a **reply to it** and starts `📦 №N · k/total`, so a package stays
   one thread even when the brother is a week behind. In a Telegram group with Topics, each
   video gets its own topic instead.
3. Last, the whole package as a `.txt` file.
