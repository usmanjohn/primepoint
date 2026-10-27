"""The Last Ones 2-qism «Koʻprik» (2026-10-25): the torch-and-bridge puzzle with eight people.
People are named ONLY by their Flow picture (@1.Qodir …), never described — the user's call
(descriptions tripped "prominent people"). Nobody talks into the lens."""
import json
import os

S = '/Users/abduraimovusmanjon/dev/primepoint/flowstudio/series'
CAST_PATH = os.path.join(S, 'the_last_ones_cast.json')
cast = json.load(open(CAST_PATH, encoding='utf-8'))

NEW = [
    {"id": "R15", "introduced": "02", "name_uz": "Jarlik va koʻprik",
     "prompt": "A deep jungle gorge at dusk: two steep cliff edges overgrown with ferns and hanging vines, and between them a long old suspension footbridge of grey weathered wooden planks hung on two rusted iron chains, many planks missing, sagging over a bottomless misty drop and vanishing into fog toward the far side. On the near edge, beside the bridge's iron anchor, a waist-high moss-covered standing stone. Cold blue dusk light, drifting mist. Seen from the near edge at eye level. No people."},
    {"id": "R16", "introduced": "02", "name_uz": "Qoida toshi va qum yuki",
     "prompt": "Close view of the bridge anchor on a jungle cliff at dusk: a waist-high standing stone covered in moss, carved with simple pictures only — two small human figures side by side, an old oil lantern, and a long row of short notches. Behind it, the rusted iron chain of the bridge runs over a big wooden wheel down to a huge round stone weight that rests on a wooden box full of sand, with a small wooden plug in a hole at the bottom of the box. An old iron oil lantern hangs from a hook on the stone. No letters, no text, no people."},
]
known = {r['id'] for r in cast['episode_refs']}
for r in NEW:
    if r['id'] not in known:
        cast['episode_refs'].append(r)
cast['_note'] = cast['_note'].replace('Next free id: R15.', 'Next free id: R17.')
with open(CAST_PATH, 'w', encoding='utf-8') as f:
    json.dump(cast, f, ensure_ascii=False, indent=1)
    f.write('\n')
VOICES = cast['voices']
ALL = {r['id']: {k: v for k, v in r.items() if k != 'introduced'} for r in cast['cast'] + cast['episode_refs']}

# the user's Flow picture names (1–9); 10+ keep their R id
AT = {'Qodir Bobo': '@1.Qodir', 'Sarang': '@2.Sarang', 'Anna': '@3.Anna', 'Jordan': '@4.Jordan',
      'Charli': '@5.Charli', 'Tagor': '@6.Tagor', 'Wei Yi': '@7.WeiYi', 'Maksim': '@8.Maksim',
      'Kapitan': '@9.Kapitan'}
A = AT
LANG = {'en': 'English', 'ru': 'Russian', 'ko': 'Korean', 'zh': 'Chinese', 'uz': 'Uzbek'}
GRADE = (" Look: a tense cinematic thriller — cold blue dusk turning to night, fog, deep shadows, warm "
         "lantern light the only colour; the acting is grounded and serious, no comedy, no mugging for the camera.")
END = " No subtitles, no on-screen text."
pz = lambda s: s.replace('ʻ', "'").replace('ʼ', "'")


def sc(n, title, attach, secs, body, said=(), to='', after='', camera='', sound='', overlays=None, only=False):
    """said = [(who, lang, [(direction, line, sub_uz), …]), …] — one speaker per scene."""
    p = f"A self-contained {secs}-second shot. {body}"
    if only:
        k = sum(1 for r in attach if int(r[1:]) <= 9)
        p += (f" Only the {'person' if k == 1 else f'{k} people'} from the attached pictures "
              f"{'is' if k == 1 else 'are'} in this shot — no extra people, no crowd, nobody else."
              if k else " No people in this shot.")
        if k:
            p += " Keep each person exactly as in their picture: the same face, hair, glasses, hat and clothes."
    lines = []
    if said:
        who = said[0][0]
        bits = []
        for w, lang, parts in said:
            q = ' Then, '.join(f'{d}: "{pz(t)}"' for d, t, _ in parts)
            bits.append(f"speaks in {LANG[lang]} with {VOICES[w]} — {q}")
            lines.append({"who": w, "lang": lang, "text": '\n'.join(t for _, t, _ in parts)}
                         | ({"sub_uz": '\n'.join(u for _, _, u in parts)} if lang != 'uz' else {}))
        p += f" {A[who]} " + f' Then {A[who]} '.join(bits) + after
        p += " Delivery: grounded, low, real, never theatrical."
        p += (f" Eyes: {A[who]} talks to {to}, never to the camera — never looks into the lens; "
              "we see the face in three-quarter profile or past someone's shoulder.")
        p += (f" Lip-sync: only {A[who]} moves the mouth and speaks, one line at a time; everyone else keeps "
              "the mouth closed; no background voices or murmur.")
    else:
        p += " Lip-sync: nobody speaks — every mouth stays closed the whole time. Nobody looks into the lens."
    p += GRADE + f" Camera: {camera} Sound: {sound}; no music." + END
    d = dict(n=n, title_uz=title, method="Ingredients to Video", attach=attach, seconds=secs, prompt=p)
    if lines:
        d['lines'] = lines
    if overlays:
        d['overlays'] = overlays
    return d


def clock(m, t=0.6, d=4.0):
    return {"t": t, "d": d, "y": 0.14, "size": 76, "text": f"{m:02d}:00 / 38:00"}


s = [
    # ── the gorge ──
    sc(1, "Jarlik", ["R15", "R10", "R11"], 8,
       "Dusk. The eight people from @R10 and @R11 push out of the dark jungle one by one and stop dead at the edge of the gorge from @R15. The old bridge hangs on its rusted chains over the misty drop and disappears into fog. Somebody's foot sends a pebble over the edge; it falls and falls, no sound of landing.",
       camera="from behind the group, slow push past their shoulders to the bridge.",
       sound="wind in the gorge, the chains creaking, the jungle loud behind them"),
    sc(2, "Qoidalar", ["R16", "R2"], 8,
       f"At the standing stone from @R16, {A['Sarang']} wipes the moss off the carved pictures with her sleeve and traces them with one finger: two figures, the lantern, the long row of notches.",
       said=[("Sarang", "en", [("reading, careful", "Two at a time. Always with the lantern.", "Bir vaqtda ikki kishi. Doim chiroq bilan."),
                               ("quieter, touching the notches", "And thirty-eight marks.", "Va oʻttiz sakkizta belgi.")])],
       to="the others standing behind her", camera="close on her hand on the stone, then her face in profile.",
       sound="wind, moss tearing, the chains creaking",
       overlays=[{"t": 1.2, "d": 3.0, "y": 0.14, "size": 76, "text": "2 kishi · 1 chiroq"},
                 {"t": 4.6, "d": 3.0, "y": 0.14, "size": 76, "text": "38"}]),
    sc(3, "Qum", ["R16", "R8"], 8,
       f"Behind the stone from @R16, {A['Maksim']} kneels by the huge stone weight on its box of sand, lays his palm on the wood and listens with his head tilted.",
       said=[("Maksim", "en", [("quietly", "There's sand under this stone.", "Bu toshning tagida qum bor."),
                               ("slowly", "When the first of us steps on the bridge — it starts to run.", "Birinchimiz koʻprikka qadam qoʻyganda — u oqa boshlaydi.")])],
       to="the people behind him, his face turned toward their voices",
       camera="low, side-on, the weight and the chain above him.", sound="a faint dry hiss of sand, wind"),
    # ── the cards ──
    sc(4, "Kartochka", ["R15", "R5"], 6,
       f"At the cliff edge, {A['Charli']} pulls a small worn card with smudged unreadable handwriting out of his pocket and frowns at it.",
       said=[("Charli", "en", [("puzzled, a little scared", "This isn't mine. I never had this.", "Bu meniki emas. Menda bunaqasi yoʻq edi.")])],
       to="the adults beside him, holding the card up to them", camera="medium close-up from the side, the fog behind.",
       sound="wind, paper rustling"),
    sc(5, "Kim oʻlchagan?", ["R15", "R3"], 8,
       f"At the cliff edge, {A['Anna']} finds the same small worn card inside her jacket, reads it, and her face goes cold. Around her the others are pulling identical cards from their own pockets.",
       said=[("Anna", "en", [("flat", "My speed. My weight. My strength.", "Tezligim. Vaznim. Kuchim."),
                             ("very low", "Someone measured us.", "Kimdir bizni oʻlchagan.")])],
       to="the others, looking from face to face", camera="over a shoulder onto Anna, slow push-in.",
       sound="wind, paper rustling, the chains"),
    sc(6, "Raqamlar", ["R15", "R6"], 8,
       f"At the cliff edge, {A['Tagor']} crouches with all eight cards fanned in his hand and reads them out fast, tapping each card.",
       said=[("Tagor", "en", [("fast, nervous", "Anna, one. Wei Yi, two. Charlie, three. Me — four.", "Anna — bir. Wei Yi — ikki. Charli — uch. Men — toʻrt."),
                              ("faster", "Sarang, five. Jordan, seven. Qodir, eight. Maksim — ten.", "Sarang — besh. Jordan — yetti. Qodir — sakkiz. Maksim — oʻn.")])],
       to="the group standing around him", camera="high angle over the group onto him, then close on the cards.",
       sound="wind, cards tapping",
       overlays=[{"t": 0.5, "d": 7.2, "y": 0.08, "size": 60, "text": "Anna 1 · Wei Yi 2"},
                 {"t": 0.5, "d": 7.2, "y": 0.13, "size": 60, "text": "Charli 3 · Tagor 4"},
                 {"t": 0.5, "d": 7.2, "y": 0.18, "size": 60, "text": "Sarang 5 · Jordan 7"},
                 {"t": 0.5, "d": 7.2, "y": 0.23, "size": 60, "text": "Qodir 8 · Maksim 10"}]),
    # ── Tagor's plan ──
    sc(7, "Tagorning rejasi", ["R15", "R6", "R3"], 8,
       f"At the cliff edge, {A['Tagor']} stands up and turns to {A['Anna']}, pointing across the bridge and back with the cards.",
       said=[("Tagor", "en", [("quick, thinking aloud", "You're the fastest. You walk each of us over —", "Siz eng tezsiz. Har birimizni olib oʻtasiz —"),
                              ("then", "and bring the lantern back.", "va chiroqni qaytarib kelasiz.")])],
       to=f"{A['Anna']}", camera="two-shot from the side, both in profile.", sound="wind, chains"),
    sc(8, "Qirq besh", ["R15", "R6"], 8,
       f"At the cliff edge, {A['Tagor']} counts on his fingers, lips moving, and stops. The colour drains from his face.",
       said=[("Tagor", "en", [("barely a whisper", "Forty-five minutes.", "Qirq besh daqiqa."),
                              ("swallowing", "We have thirty-eight.", "Bizda oʻttiz sakkiz bor.")])],
       to="the group, looking down at his fingers", camera="slow push-in, his face in three-quarter profile.",
       sound="wind dropping, the faint hiss of sand"),
    sc(9, "Bittamiz qolamiz", ["R15", "R4"], 6,
       f"At the cliff edge, {A['Jordan']} looks at the bridge, then at the others, jaw tight.",
       said=[("Jordan", "en", [("low, heavy", "So one of us stays behind.", "Demak, bittamiz shu yerda qolamiz.")])],
       to="the group, not meeting anyone's eyes", camera="medium shot from the side, the fog behind him.",
       sound="wind, a distant branch snapping in the jungle"),
    sc(10, "Meni qoldiring", ["R15", "R8"], 8,
       f"At the cliff edge, {A['Maksim']} is silent for a beat, then turns his face toward the sound of their breathing, calm.",
       said=[("Maksim", "ru", [("quietly", "Я самый медленный.", "Men eng sekiniman.")]),
             ("Maksim", "en", [("simply", "Leave me. Go.", "Meni qoldiring. Ketinglar.")])],
       to="the group", camera="close-up in profile, very slow push-in.", sound="wind, nothing else"),
    sc(11, "Shoshma", ["R15", "R1", "R8"], 8,
       f"At the cliff edge, {A['Qodir Bobo']} puts a hand on the shoulder of {A['Maksim']} and nods toward someone off to the side, crouched on the ground.",
       said=[("Qodir Bobo", "uz", [("softly", "Shoshma, ukam.", "")]),
             ("Qodir Bobo", "en", [("to the others, nodding aside", "Let her think.", "Qoʻyinglar, oʻylasin.")])],
       to=f"{A['Maksim']}, then the others", camera="two-shot from the side.", sound="wind"),
    # ── Sarang ──
    sc(12, "Hisob", ["R15", "R2"], 8,
       f"Crouched at the cliff edge, {A['Sarang']} arranges small stones on the ground in two rows, moving them across and back, lips moving fast. She stops, looks up.",
       said=[("Sarang", "ko", [("to herself, counting", "둘이 같이… 그래.", "Ikkovi birga… ha.")]),
             ("Sarang", "en", [("clear, certain", "Nobody stays.", "Hech kim qolmaydi.")])],
       to="the group above her", camera="top shot of her hands and the stones, then her face from below in profile.",
       sound="stones clicking, wind"),
    sc(13, "Eng sekinlar birga", ["R15", "R2"], 8,
       f"At the cliff edge, {A['Sarang']} rises and speaks fast and precise, holding up two fingers, then pointing at two people off-screen.",
       said=[("Sarang", "en", [("precise", "The two slowest cross together — we pay for their time once.", "Eng sekin ikkitasi birga oʻtadi — vaqtini bir marta toʻlaymiz."),
                               ("pointing", "Anna and Wei Yi carry the lantern back. Every time.", "Chiroqni Anna va Wei Yi qaytaradi. Har safar.")])],
       to="the group in a half circle around her", camera="past the shoulders of the listeners onto her, then a side angle.",
       sound="wind, chains"),
    sc(14, "Aytganimni qiling", ["R15", "R2", "R3"], 8,
       f"At the cliff edge, {A['Sarang']} turns to {A['Anna']} and holds her eyes.",
       said=[("Sarang", "en", [("firm", "Thirty-eight minutes. Not one more.", "Oʻttiz sakkiz daqiqa. Bir daqiqa ham koʻp emas."),
                               ("low", "Do exactly as I say — and nobody dies.", "Aytganimni aniq qiling — hech kim oʻlmaydi.")])],
       to=f"{A['Anna']}", camera="two-shot in profile, faces close.", sound="wind, the chains groaning"),
    # ── the crossing ──
    sc(15, "Boshladik", ["R15", "R7", "R3"], 8,
       f"At the head of the bridge, {A['Wei Yi']} lights the old lantern, lifts it, and looks at {A['Anna']}.",
       said=[("Wei Yi", "zh", [("calm", "走。", "Ketdik.")])],
       to=f"{A['Anna']}", after=" They step onto the first plank together — and behind them, with a dull clunk, something gives way.",
       camera="from behind the two of them onto the swaying bridge and the fog.",
       sound="the lantern's hiss, a heavy wooden clunk, then the start of a dry pouring sound",
       overlays=[clock(0, 4.0, 3.6)]),
    sc(16, "Qum oqmoqda", ["R16"], 6,
       "At the anchor from @R16, the wooden plug has dropped out: a thin steady stream of sand pours from the hole in the box, and the huge stone weight sinks a finger's width with a creak.",
       camera="close and low on the falling sand, then up to the weight.",
       sound="pouring sand, the chain groaning on the wheel", overlays=[clock(2)]),
    sc(17, "Chiroq qaytadi", ["R15", "R3"], 8,
       f"Alone on the bridge in thick fog, {A['Anna']} hurries back toward the near side with the lantern, stepping over the gaps without looking down. Behind her, deep in the fog on the far side, something large shifts and is gone.",
       camera="from the near end, the lantern a small warm light coming out of the fog.",
       sound="planks knocking, her fast breathing, the chains", overlays=[clock(3)]),
    sc(18, "Jordanning qadami", ["R15", "R4", "R2"], 8,
       f"Halfway across, a plank cracks under {A['Jordan']} and he freezes, gripping the chain. Ahead of him with the lantern, {A['Sarang']} turns back.",
       said=[("Sarang", "en", [("calm, steady", "Don't stop. Don't look down.", "Toʻxtamang. Pastga qaramang.")])],
       to=f"{A['Jordan']}", after=" He breathes out and takes the next step.",
       camera="side-on from the fog, both small on the long bridge.",
       sound="wood splitting, a piece falling into the gorge, the chains swinging", overlays=[clock(7)]),
    sc(19, "Wei Yi yolgʻiz", ["R15", "R7"], 6,
       f"Alone on the bridge, {A['Wei Yi']} runs back with the lantern, light and silent, and jumps clean over a gap of three missing planks without breaking stride.",
       camera="tracking alongside him through the fog.", sound="quick light steps, the lantern swinging, wind",
       overlays=[clock(11)]),
    sc(20, "Koʻr va keksa", ["R15", "R1", "R8"], 8,
       f"On the bridge, {A['Qodir Bobo']} walks slowly with the lantern; {A['Maksim']} follows with one hand on his shoulder, testing every plank with his foot.",
       said=[("Qodir Bobo", "uz", [("softly, step by step", "Qadam… yana bir qadam.", "")])],
       to=f"{A['Maksim']} behind him", after=" A faint smile on the blind man's face.",
       camera="from in front, slowly moving back as they come.", sound="careful steps, creaking planks, wind",
       overlays=[clock(21)]),
    sc(21, "Yuring!", ["R16", "R3", "R6"], 8,
       f"At the near end, the sand box from @R16 is almost empty and the stone weight hangs low. {A['Anna']} stumbles off the bridge, exhausted, and grabs the hand of {A['Tagor']}, the last one left.",
       said=[("Anna", "en", [("gasping", "Now. Run.", "Hozir. Yuguring.")])],
       to=f"{A['Tagor']}", camera="handheld, close, the weight looming behind them.",
       sound="the last trickle of sand, the chain straining, her breathing", overlays=[clock(34)]),
    sc(22, "Koʻprik qulaydi", ["R15", "R3", "R6"], 8,
       f"{A['Anna']} and {A['Tagor']} sprint across the last planks with the lantern as the bridge collapses behind them plank by plank; they dive onto the far ledge as the whole bridge falls away into the gorge.",
       camera="tracking ahead of them, the collapse chasing them.",
       sound="chains snapping, wood tearing, a long fall, then silence",
       overlays=[clock(37, 0.4, 3.0), clock(38, 4.6, 3.2)]),
    sc(23, "Aniq", ["R15", "R6"], 6,
       f"On the far ledge in the dark, {A['Tagor']} lies on his back next to the lantern, gasping, then lets out one shaky laugh.",
       said=[("Tagor", "en", [("breathless", "Thirty-eight. Exactly.", "Oʻttiz sakkiz. Aynan.")])],
       to="someone standing over him, off-screen", camera="top shot, then side-on.", sound="breathing, wind in the gorge"),
    sc(24, "Narigi tomonda", ["R15", "R10", "R11"], 10,
       "Night. The eight from @R10 and @R11 stand at the far ledge in their one circle of lantern light, looking back across the empty gorge where the bridge used to be. On the side they left, in the fog, a very tall dark figure steps out of the jungle to the edge and stands perfectly still. Then, slowly, it raises a lantern of its own — and lights it.",
       camera="from behind the group across the gorge, slow push toward the far light; the figure stays a silhouette, never clear.",
       sound="wind, the drip of the gorge, then a match striking far away and one low drum",
       overlays=[{"t": 6.6, "d": 3.2, "y": 0.22, "text": "THE LAST ONES"},
                 {"t": 7.6, "d": 2.2, "y": 0.30, "text": "Davomi bor…"}]),
]

# ── v2 (2026-10-25, after S1–S13 were filmed): S10 and S13–S24 rewritten — only attached people in
# the shot, no group pictures, each person introduced once by a short, safe look tag ──
TAG = {'Qodir Bobo': "the older man in the black-and-white skullcap and the short green robe",
       'Sarang': "the young woman with a high bun in the white field jacket",
       'Anna': "the woman with the auburn ponytail in the black leather jacket",
       'Jordan': "the very tall man in the dark-red sleeveless shirt",
       'Charli': "the boy in the backwards yellow cap",
       'Tagor': "the young man in round black glasses and a grey hoodie",
       'Wei Yi': "the man with a messy topknot in the faded orange kung-fu jacket",
       'Maksim': "the blind man in dark round glasses, his eyes always hidden behind them"}
T = lambda w: f"{A[w]} ({TAG[w]})"


def sc2(*a, **k):
    return sc(*a, only=True, **k)


V2 = [
    sc2(10, "Meni qoldiring", ["R15", "R8"], 8,
        f"Dusk at the edge of the gorge from @R15. {T('Maksim')} stands alone near the edge, the misty drop behind him. He is silent for a beat, then turns his face toward the voices of people who are off-screen, calm.",
        said=[("Maksim", "ru", [("quietly", "Я самый медленный.", "Men eng sekiniman.")]),
              ("Maksim", "en", [("simply", "Leave me. Go.", "Meni qoldiring. Ketinglar.")])],
        to="the people off-screen", camera="close-up in profile, very slow push-in.", sound="wind, nothing else"),
    sc2(13, "Eng sekinlar birga", ["R15", "R2"], 8,
        f"Dusk at the edge of the gorge from @R15. {T('Sarang')} stands up from the ground and speaks fast and precise to listeners off-screen, holding up two fingers, then pointing off-screen twice.",
        said=[("Sarang", "en", [("precise", "The two slowest cross together — we pay for their time once.", "Eng sekin ikkitasi birga oʻtadi — vaqtini bir marta toʻlaymiz."),
                                ("pointing", "Anna and Wei Yi carry the lantern back. Every time.", "Chiroqni Anna va Wei Yi qaytaradi. Har safar.")])],
        to="the listeners off-screen", camera="medium close-up from the side, the bridge and fog behind her.",
        sound="wind, chains"),
    sc2(14, "Aytganimni qiling", ["R15", "R2", "R3"], 8,
        f"At the edge of the gorge from @R15, {T('Sarang')} turns to {T('Anna')} and holds her eyes.",
        said=[("Sarang", "en", [("firm", "Thirty-eight minutes. Not one more.", "Oʻttiz sakkiz daqiqa. Bir daqiqa ham koʻp emas."),
                                ("low", "Do exactly as I say — and nobody dies.", "Aytganimni aniq qiling — hech kim oʻlmaydi.")])],
        to=A['Anna'], after=f" {A['Anna']} nods once.",
        camera="two-shot in profile, faces close.", sound="wind, the chains groaning"),
    sc2(15, "Boshladik", ["R15", "R7", "R3"], 8,
        f"At the head of the bridge from @R15, {T('Wei Yi')} lights an old iron oil lantern, lifts it, and looks at {T('Anna')}.",
        said=[("Wei Yi", "zh", [("calm", "走。", "Ketdik.")])],
        to=A['Anna'], after=" The two of them step onto the first plank together — and behind them, with a dull wooden clunk, something gives way.",
        camera="from behind the two of them onto the swaying bridge and the fog.",
        sound="the lantern's hiss, a heavy wooden clunk, then the start of a dry pouring sound",
        overlays=[clock(0, 4.0, 3.6)]),
    sc2(16, "Qum oqmoqda", ["R16"], 6,
        "At the anchor from @R16, the wooden plug has dropped out: a thin steady stream of sand pours from the hole in the box, and the huge stone weight sinks a finger's width with a creak.",
        camera="close and low on the falling sand, then up to the weight.",
        sound="pouring sand, the chain groaning on the wheel", overlays=[clock(2)]),
    sc2(17, "Chiroq qaytadi", ["R15", "R3"], 8,
        f"On the bridge from @R15 in thick fog, {T('Anna')} hurries back alone with the lantern, stepping over the gaps without looking down. Deep in the fog behind her, a large dark shape shifts and is gone.",
        camera="from the near end, the lantern a small warm light coming out of the fog.",
        sound="planks knocking, her fast breathing, the chains", overlays=[clock(3)]),
    sc2(18, "Jordanning qadami", ["R15", "R4", "R2"], 8,
        f"Halfway across the bridge from @R15, a plank cracks under {T('Jordan')} and he freezes, gripping the chain. Ahead of him, {T('Sarang')} holds the lantern and turns back to him.",
        said=[("Sarang", "en", [("calm, steady", "Don't stop. Don't look down.", "Toʻxtamang. Pastga qaramang.")])],
        to=A['Jordan'], after=f" {A['Jordan']} breathes out and takes the next step.",
        camera="side-on from the fog, the two of them small on the long bridge.",
        sound="wood splitting, a piece falling into the gorge, the chains swinging", overlays=[clock(7)]),
    sc2(19, "Wei Yi yolgʻiz", ["R15", "R7"], 6,
        f"On the bridge from @R15, {T('Wei Yi')} runs back alone with the lantern, light and silent, and jumps clean over a gap of three missing planks without breaking stride.",
        camera="tracking alongside him through the fog.", sound="quick light steps, the lantern swinging, wind",
        overlays=[clock(11)]),
    sc2(20, "Koʻr va keksa", ["R15", "R1", "R8"], 8,
        f"On the bridge from @R15, {T('Qodir Bobo')} walks slowly with the lantern; behind him {T('Maksim')} keeps one hand on his shoulder and tests every plank with his foot.",
        said=[("Qodir Bobo", "uz", [("softly, step by step", "Qadam… yana bir qadam.", "")])],
        to=f"{A['Maksim']} behind him, glancing back over his shoulder", after=f" A faint smile on the face of {A['Maksim']}.",
        camera="from in front, slowly moving back as they come.", sound="careful steps, creaking planks, wind",
        overlays=[clock(21)]),
    sc2(21, "Yuring!", ["R16", "R3", "R6"], 8,
        f"At the anchor from @R16, the sand box is almost empty and the stone weight hangs low. {T('Anna')} stumbles off the bridge, exhausted, and grabs the hand of {T('Tagor')}, who has been waiting there alone.",
        said=[("Anna", "en", [("gasping", "Now. Run.", "Hozir. Yuguring.")])],
        to=A['Tagor'], camera="handheld, close, the weight looming behind them.",
        sound="the last trickle of sand, the chain straining, her breathing", overlays=[clock(34)]),
    sc2(22, "Koʻprik qulaydi", ["R15", "R3", "R6"], 8,
        f"{T('Anna')} and {T('Tagor')} sprint across the last planks of the bridge from @R15 with the lantern as it collapses behind them plank by plank; they dive onto the far rocky ledge as the whole bridge falls away into the gorge.",
        camera="tracking ahead of them, the collapse chasing them.",
        sound="chains snapping, wood tearing, a long fall, then silence",
        overlays=[clock(37, 0.4, 3.0), clock(38, 4.6, 3.2)]),
    sc2(23, "Aniq", ["R15", "R6"], 6,
        f"On the far rocky ledge of the gorge from @R15, in the dark, {T('Tagor')} lies on his back next to the lantern, gasping, then lets out one shaky laugh.",
        said=[("Tagor", "en", [("breathless", "Thirty-eight. Exactly.", "Oʻttiz sakkiz. Aynan.")])],
        to="someone standing over him, off-screen", camera="top shot, then side-on.", sound="breathing, wind in the gorge"),
    sc2(24, "Narigi tomonda", ["R15", "R8", "R3"], 10,
        f"Night on the far ledge of the gorge from @R15; the bridge is gone, only broken chains hang into the mist. {T('Maksim')} suddenly lifts his head toward the other side. Next to him, {T('Anna')} turns to look.",
        said=[("Maksim", "ru", [("a whisper", "Там кто-то есть.", "U yerda kimdir bor.")])],
        to=A['Anna'],
        after=" Across the gorge, on the side they came from, far away and only a silhouette in the fog, a very tall dark shape stands at the edge, perfectly still — and slowly lights a lantern of its own.",
        camera="from behind the two of them across the gorge, slow push toward the far light; the far shape stays a silhouette, never clear.",
        sound="wind, the drip of the gorge, then a match striking far away and one low drum",
        overlays=[{"t": 6.6, "d": 3.2, "y": 0.22, "text": "THE LAST ONES"},
                  {"t": 7.6, "d": 2.2, "y": 0.30, "text": "Davomi bor…"}]),
]
by_n = {d['n']: d for d in V2}
s = [by_n.get(d['n'], d) for d in s]

used = sorted({r for d in s for r in d['attach']} | {'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8'},
              key=lambda r: int(r[1:]))
refs = []
for rid in used:
    r = dict(ALL[rid])
    if rid not in ('R15', 'R16'):
        r['saved'] = True
    refs.append(r)

pkg = {
    "_note": "2-qism (2026-10-25): the torch-and-bridge puzzle (Logic Arena #2) with all eight. People are named only by their Flow picture (@1.Qodir …), no looks. Minimum 38 min checked by brute force. LOCAL kit — the user films it himself.",
    "id": "the-last-ones-02", "number": 34, "for": "Birga", "date": "2026-10-25", "series": "The Last Ones",
    "title_uz": "2-qism. Koʻprik",
    "concept_uz": "Togʻ yoʻlini chuqur jarlik toʻsadi: eski koʻprik, bir vaqtda ikki kishi, chiroq doim qaytishi kerak va 38 daqiqadan keyin koʻprik qulaydi. Choʻntaklarida kimdir yozgan kartochkalar — har birining tezligi. Tagor hisoblaydi: kimdir qolishi shart. Sarang boshqacha hisoblaydi — hech kim qolmaydi.",
    "format_uz": "24 sahna, ingliz tilida (baʼzan rus, koreys, xitoy, oʻzbek), oʻzbekcha subtitr va taymer montajda avtomatik",
    "sources": ["flowstudio/series/the_last_ones.md", "logic/management/commands/toc_logic_puzzles.txt"],
    "facts": [{"claim": "Vaqtlar 1,2,3,4,5,7,8,10 daq, ikki kishidan, chiroq qaytadi: eng kam vaqt 38 daqiqa (Anna+Wei Yi tashiydi); Anna har birini olib oʻtsa 45, Maksimsiz 34",
               "source": "toʻliq qidiruv (Dijkstra, scratchpad bridge.py); Logic Arena #2 «The Torch and the Bridge»"}],
    "style_line": cast['style_line'],
    "post_text_uz": "The Last Ones · 2-qism 🌉\nIkki kishi. Bitta chiroq. 38 daqiqa.\nSakkiz kishi oʻtishi kerak — hech kim qolmasligi kerak.\nSiz qanday oʻtkazardingiz? 👇\n#TheLastOnes #triller #mantiq #powerty",
    "refs": refs,
    "scenes": s,
    "inserts": [{"after": 7, "file": "A1-tagor.mp4"}, {"after": 13, "file": "A2-sarang.mp4"}],
}
with open(os.path.join(S, 'the_last_ones_02.json'), 'w', encoding='utf-8') as f:
    json.dump(pkg, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(s), 'scenes', sum(x['seconds'] for x in s), 's')
