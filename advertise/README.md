# «Ikki tun» — Istiqlol Mebel bed ad (started 2026-10-22)

The user's own ad idea (not a client job yet): a man sleeps badly → fails at work → calls a
number → sleeps on a new bed, dreams of his childhood and his mother → shines at work →
«Men emas... karavotim oʻzgardi.» → closing card. The number he dials in S5 is the SAME number
on the closing card — that is the twist's payoff. Hero = AI character made from the user's
brother's photo (brother consented). The bed itself is never shown before the closing card.

## Brand
- Istiqlol Mebel, Instagram @istiqlol.mebel, Toshkent, 09:00–19:00
- Number used everywhere: **+998 90 819 44 41** (user's choice; the page also lists
  +998 97 197 44 41 and +998 90 365 44 41)
- Slogan: **«Yaxshi yotib, yaxshi turing.»**
- Logo bg colour #311701; source screenshots in `bed/`

## Status (2026-10-22)
- ✅ Shots S1–S11 generated in Flow (Veo), in `~/Downloads/` as `S1_1080p_…`, `s2_…` … `s11_…`
  (8/6/6/6/8/6/8/4/6/6/6 s, 24 fps, with Veo's own audio)
- ✅ `endcard.mp4` — 5 s closing card (logo + bed photo with panel seams cut out + slogan + number + IG)
- ✅ `build/s5_number.mp4` — S5 with a "Qoʻngʻiroq qilinmoqda… +998 90 819 44 41" box at t=2–5 s
- ✅ Rough cut: `~/Downloads/istiqlol_rough_cut_v2.mp4` (1:15) — plain concat, loudnorm −14 LUFS, no music, no poems
- ⏳ **User is writing Poem A and Poem B** (his verse — fix meter/spelling only, list every change)
- ⏳ Then: ElevenLabs voice (eleven_v4, Jahongir storyteller) for both poems → music → final mix
  with crossfades; trim S2/S3/S8 if it needs to be shorter (target 50–75 s)

## Timeline of the rough cut
| Time | Shot | Audio |
|---|---|---|
| 0–8 | S1 gloomy dream (corridor, drifts into fog) | 🎙 Poem A, ~12–14 words |
| 8–14 | S2 wakes late | sfx |
| 14–20 | S3 dozing at desk | sfx |
| 20–26 | S4 boss | 🗣 «Bu nima? Yana-ya?» |
| 26–34 | S5 call (number overlay 28–31) | 🗣 «Yetar... Nimadir oʻzgarishi kerak.» … «Koʻramiz-chi, bu kecha...» |
| 34–40 | S6 falls asleep → courtyard, mother | 🎙 Poem B 1st half |
| 40–48 | S7 boy runs to mother, hug | 🎙 Poem B 2nd half (~22–26 words total) |
| 48–52 | S8 wakes rested | sfx |
| 52–58 | S9 presentation, boss | 🗣 «Barakalla!» |
| 58–64 | S10 colleagues | 🗣 «Nima boʻldi senga? Oʻzgarib ketding!» |
| 64–70 | S11 close-up, wink | 🗣 «Men emas... karavotim oʻzgardi.» |
| 70–75 | closing card | slogan / music |

## Lessons
- The first S1 prompt was refused by Flow's policy filter → softened: "nightmare" → "strange,
  gloomy dream", "falls into darkness / floor cracks" → "drifts backwards into blue fog like a
  feather", no "horror". Same caution for S2 ("sweating"), S4 ("slap", "ashamed"), S7 (a child).
- Mac screenshots in /var/folders/…/NSIRD_screencaptureui_* vanish within minutes — ask the user
  to save files into the repo/Downloads first.
- References used: R1 hero tired (wrinkled light-blue shirt), R1b hero rested (white shirt, navy
  blazer), R2 boy ~6, R3 mother (red-gold atlas dress, white headscarf), R4 boss (grey beard,
  glasses, grey suit), R5 colleague (beige blazer, bun), R6 Tashkent office, R7 hovli with
  blooming apricot tree. Look: cold blue-grey for the bad day, warm gold for the good one.
