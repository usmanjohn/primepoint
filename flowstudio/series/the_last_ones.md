# «The Last Ones» — series bible

> **Name (2026-10-24):** was «Ters dunyo»; renamed after the captain's line "Because the last ones
> took too much" — the user let me choose and may change it later.

> **v2, 2026-10-24 (the user's rework).** Eight strangers are left on an island by a ship; the
> captain lets each take ONE item. The earlier pilot (Bobo/Lola/Vera, «Quduq» + «Supurgi») is
> obsolete and deleted. Not for Telegram — he films it himself (local kit).
> Cast and picture ids: `the_last_ones_cast.json` (global ids, never reused; next free R15).

## 1. Shape
- **Day episodes (N-qism)** — a story told in order: solving problems on the island, and one
  person's identity/backstory and hidden item revealed per episode.
- **Night episodes** — a poem by the fire, **chosen by the user** (Sonlar imperiyasi, Uzbek
  writers…); NOT tied to the day. Start only after 1- and 2-qism are filmed. Check copyright of
  any poem by a 20th-century writer (Uzbek law ≈ life + 50 years).
- **THRILLER, *Lost* level** (user, 2026-10-24): mystery and fear, no gore. Cold teal-grey grade in every
  scene prompt (pictures unchanged), grounded acting, jokes only as nervous relief.
- **English is the common language** (Uzbek in Veo sounded unserious). Each person slips into their own
  language under stress (Maksim Russian, Sarang Korean, Wei Yi Chinese, Qodir Bobo Uzbek proverbs).
  Every non-Uzbek line carries `lang` + `sub_uz`; `assemble.py` burns the Uzbek subtitles in, timed
  by ElevenLabs speech-to-text (`--no-subs` to skip). The gate demands both.
- Night tales: **Uzbek, Qodir Bobo** as voice-over — the others don't understand, they just listen.

## 2. The eight (+ the captain)
| | who | role | look (colour) | secret item |
|---|---|---|---|---|
| R1 | Qodir Bobo, ~60, Uzbek | the wise one | skullcap, short dark-**green** chapan | nay |
| R2 | Sarang (최사랑), Korean, woman | scientist | crisp **white** field jacket, high bun | ruler with a protractor |
| R3 | Anna, European, woman | alert, agent-like | **black** leather jacket, auburn ponytail | knife |
| R4 | Jordan, African | the strong one | dark-**red** sleeveless shirt, shaved head | rope |
| R5 | Charlz «Charli», 9, American | the child | **yellow** cap backwards, dungarees | a book (contents a mystery) |
| R6 | Tagor, Indian | programmer | round glasses, **grey** hoodie | mechanical watch |
| R7 | Wei Yi, Chinese | drunken-kung-fu master | faded **orange** kung-fu jacket, topknot | gourd flask — "just tea" |
| R8 | Maksim, Russian, blind | the listener | **striped** sailor shirt, grey coat, dark glasses | **nothing** — "quloqlarimni" |
| R9 | Kapitan | brought them; why is the mystery | face always in shadow | — |

Items are **never shown** before their owner's episode — keep them out of every picture.
Group pictures R10 (Jordan, Anna, Qodir, Sarang) and R11 (Maksim, Charli, Tagor, Wei Yi) stand in
for "everyone" in wide shots; most scenes show 2–3 people.

## 3. Item ideas for later (not decided)
Watch = compass (hour hand at the sun, halfway to 12 = south) · ruler-protractor = height of a
tree/cliff by its shadow, width of a river · nay = signal, a hollow tube to breathe through ·
rope, knife = obvious, so they pay off in a surprising way · the book could hold tales/poems and
bring the night poems into the story · the gourd: "tea" nobody believes; fire starter/disinfectant.

## 4. Episodes
- **1-qism. Bitta narsa** (`the_last_ones_01.json`, 22 scenes ~2:40): cold open — night jungle, Anna's
  torch dies, Jordan shouts «Charlie!», «3 kun oldin»; the captain: "Eight of you. Chosen…", "Only one",
  Charli "Why only one?" → "Because the last ones took too much"; Tagor "Where are they now?"; the
  secret choosing; Wei Yi in Chinese «这个岛……不对劲»; "Good luck. You'll need it."; still-warm ashes,
  bare footprints not theirs, Sarang measures 30 cm in Korean → ~2 m tall; Maksim in Russian «Тихо» —
  the birds stop; "My ears"; "If we stay, we wait. If we walk, we find out."; Qodir's proverb + "We
  walk."; into the jungle — a very tall figure watches them.
- **2-qism. Koʻprik** (`the_last_ones_02.json`, 24 scenes ~3:00): the torch-and-bridge puzzle
  (Logic Arena #2) with all eight. Carved stone: two at a time, always the lantern, 38 notches; a sand
  box under the counterweight starts to run at the first step. Cards nobody put in their pockets — each
  one's speed/weight/strength ("Someone measured us"). Times 1 Anna · 2 Wei Yi · 3 Charli · 4 Tagor ·
  5 Sarang · 7 Jordan · 8 Qodir · 10 Maksim. Tagor: Anna walks everyone = 45 → someone stays (without
  Maksim 34); Maksim «Я самый медленный… Leave me»; Sarang: the two slowest together, Anna and Wei Yi
  carry the lantern = **38, the true minimum (brute-forced)**. Bridge falls behind Anna and Tagor; across
  the gorge the tall figure lights a lantern of its own. Weight/strength on the cards = seeds for later.
- Open threads: who is the giant (now with a lantern), who measured them, the last ones, the smoke,
  Charli lost at night (the cold open). Jordan's rope is reserved — the user has an idea for it.

## 5. Writing rules (from 2-qism)
- An episode is a **logical problem solved by thinking** (combined knowledge, experience), still a thriller.
  Not every episode reveals an item. Whoever set the tests did NOT know what they would bring.
- No «Siz qanday yechardingiz?» on screen — it plays like a film.
- People are named in prompts by their Flow picture: @1.Qodir @2.Sarang @3.Anna @4.Jordan
  @5.Charli @6.Tagor @7.WeiYi @8.Maksim @9.Kapitan (10+ keep @R10…). Body descriptions ("bald,
  muscular") tripped Flow's "prominent people" filter — keep the look tag to clothes and glasses.
- **Only people whose pictures are attached may be in the shot** — never "the others do X" (Veo invents
  strangers). Max 2 people + the place per scene; avoid the group pictures R10/R11 (Veo drifts: Maksim
  loses his glasses, Qodir his skullcap). Introduce each person once with a short look tag after the @
  (clothes, glasses, blindness — never body/skin words), and say "keep each person exactly as in their picture".
- Nobody talks into the lens: every speaking scene says whom they talk to; three-quarter profile.
