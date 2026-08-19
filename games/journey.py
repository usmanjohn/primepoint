"""
Prime Journey — the travelling adventure built on the Prime courses.

Every other game on the platform invents its own questions and forgets them.
This one spends what the courses already built: **320 Prime lessons, each
carrying a published 20-question practice bound to it by `Tutorial.practices`**.
The road *is* a course, an obstacle *is* one of that lesson's questions, and the
way out of a dead end is to go and read the lesson.

That last sentence is the whole design. One rule governs everything here:

    ── STUDYING MUST BE THE STRONGEST MOVE IN THE GAME. ──

Fail an obstacle twice and it *seals*. There are then two keys, and they are
deliberately worth different amounts, because one of them can be faked and the
other cannot:

* **Read the lesson** — `TutorialProgress`, which is a button a pupil presses.
  `prime/reading.py` makes that button cost a minute of dwell time, but it still
  proves nothing. So it buys exactly one thing: the gate opens. No strength.
* **Pass the lesson's practice** — a scored `PracticeAttempt` at or above
  `pass_score`. This cannot be faked, so it pays properly: the gate opens, you
  get strength back, and **the guard does not ask a question at all**. The gate
  existed to check they knew the lesson; a twenty-question test already checked,
  harder. Asking a twenty-first would be theatre — and the bank is only twenty
  deep, so it could not be a fresh question anyway.

The reading (a Corner story) is never a key: 33 lessons across the four roads
have no story, and gating on it would leave those gates with no key at all. It
pays a torch and coins instead.

Run out of hearts and the stage is **lost**: everything left on the road is
forfeited, and the big prize at the end with it. There is exactly one reprieve —
a *last stand*, once per stage, bought by going and passing a practice. Study is
the only thing standing between a traveller and the end of the road.

A leg's map is generated from a seed, the way `mathchamp.py` generates
questions, so no two runs look alike and there are no hand-drawn maps to keep.

Everything in here is pure logic and JSON-safe data — no database writes, no
request objects. Two consequences worth remembering when editing:

* **Nothing lazy goes into the map.** The map is stored in a JSONField (and in
  the session for guests), so nodes carry an encounter *slug* and the view
  resolves it to translated prose at render time. Putting a `gettext_lazy`
  object in a node would break JSON serialisation.
* The DB is touched by exactly three readers here (`road_lessons`, `leg_lessons`
  and `pick_question`), and they only read.
"""
import math
import random
import time

from django.utils.translation import gettext_lazy as _


# Bumped whenever the shape of the state dict changes, so a journey started on
# an older build is dropped instead of being resumed against a stale map.
STATE_VERSION = 2      # bumped when the heart economy changed

LEG_SIZE = 10          # lessons per leg — one journey is ten lessons of a course

# ── hearts ─────────────────────────────────────────────────────────────────
# Three hearts, handed out once at the start of a stage and **never refilled by
# resting**. Two wrong answers cost one heart, wherever on the road they fall —
# so a stage allows six slips in about fourteen obstacles. Run out and the stage
# is genuinely lost, which is the whole reason the prize you left behind is
# worth anything.
MAX_KUCH = 3
WRONGS_PER_HEART = 2
SEAL_AFTER = 2         # wrong answers at ONE node before it seals

# The single exception to "hearts never come back", and the reason it exists:
# passing a lesson's practice is the only claim about study on this platform
# that is scored rather than self-reported. Study is the only medicine.
PROOF_HEAL = 1
READ_HEAL = 0          # pressing "finished" on a lesson heals nothing
CAMP_HEAL = 0          # nor does resting — a camp forgives a half-heart instead

CAMP_TORCHES = 1       # what a camp is for now
CAMP_COINS = 20

# Reading the lesson's Corner story is a bonus, never a key — see the module
# docstring for why it cannot be one.
STORY_TORCHES = 1
STORY_COINS = 25

LOG_LIMIT = 40         # entries kept in the journey diary

# Coins by threat level, and the two nodes that pay differently.
COINS_BY_THREAT = {1: 10, 2: 20, 3: 30}
GUARD_COINS = 60
TWIN_MULTIPLIER = 2

# The wise stranger's riddle. It pays well and costs nothing to fail, because a
# riddle a pupil cannot crack should never end their journey — the reward for
# meeting one is the trick in the explanation, whether or not they got it.
ELDER_COINS = 70
ELDER_TORCHES = 1


# ---------------------------------------------------------------------------
# The roads — one per Prime course
# ---------------------------------------------------------------------------
# `playlist` matches TutorialPlaylist.title, so a road grows by itself as the
# course is written: Prime Russian has two legs today and will have ten when the
# hundredth lesson lands. Nothing here is ever hard-coded to a lesson count.
#
# `places` names the destination of each leg, and each road names them in the
# language its course is taught in — Prime English is taught in English, the
# other three in Uzbek. That is what stops the four roads feeling like one road
# with different question banks.

ROADS = [
    {
        'slug': 'math',
        'playlist': 'Prime Math',
        'name': _('Valley of Numbers'),
        'blurb': _('From the first arithmetic to algebra and geometry — the road every other road crosses.'),
        'emoji': '\U0001F3DC️',
        'gradient': ('#f59e0b', '#b45309'),
        'subject': 'math',
        'places': ["Birlar ko'prigi", "Kasrlar ko'li", "Foizlar bozori",
                   "Nomalum vodiysi", "Tenglama darvozasi", "Grafik tepaligi",
                   "Burchaklar qoyasi", "Yuzalar tekisligi", "Ehtimol cho'li",
                   "Mantiq qal'asi"],
    },
    {
        'slug': 'english',
        'playlist': 'Prime English',
        'name': _('Land of Words'),
        'blurb': _('A hundred lessons of English grammar, laid out as one long road west.'),
        'emoji': '\U0001F33F',
        'gradient': ('#0891b2', '#0e7490'),
        'subject': 'english',
        'places': ["Verb Hollow", "Tense Bridge", "Article Marsh",
                   "Question Crossing", "Modal Ridge", "Clause Forest",
                   "Perfect Pass", "Passive Hills", "Conditional Gorge",
                   "The Last Gate"],
    },
    {
        'slug': 'korean',
        'playlist': 'Prime Korean',
        'name': _('Hangul Mountains'),
        'blurb': _('A hundred lessons of Korean, from the Hangul letters up — mountain after mountain.'),
        'emoji': '⛰️',
        'gradient': ('#e11d48', '#9f1239'),
        'subject': 'korean',
        'places': ["Hangul dovoni", "Bo'g'inlar qoyasi", "Fe'llar so'qmog'i",
                   "Hurmat cho'qqisi", "O'tmish darasi", "Bog'lovchi ko'prigi",
                   "Sabab vodiysi", "Shart qoyasi", "Ko'chirma daryosi",
                   "Oxirgi dovon"],
    },
    {
        'slug': 'russian',
        'playlist': 'Prime Russian',
        'name': _('Snow Steppe'),
        'blurb': _('From the Cyrillic alphabet to the six cases — the long road across the snow.'),
        'emoji': '❄️',
        'gradient': ('#6366f1', '#3730a3'),
        'subject': 'russian',
        'places': ["Kirill chegarasi", "Rod o'rmoni", "Kelishik ko'prigi",
                   "Fe'l dashti", "Vid daryosi", "Sifat qishlog'i",
                   "Son tepaligi", "Ko'makchi darasi", "Ergash gap yo'li",
                   "Qorli qal'a"],
    },
]

ROAD_MAP = {r['slug']: r for r in ROADS}
ROAD_SLUGS = [r['slug'] for r in ROADS]


# ---------------------------------------------------------------------------
# Terrain — a leg is a passage, not a shuffle of scenery
# ---------------------------------------------------------------------------
# Every leg walks the same arc from open road to the final gate, so the middle
# of a journey *feels* like the middle of a journey.

TERRAIN_ARC = ['road', 'forest', 'river', 'mountain', 'cave', 'desert', 'gate']

TERRAINS = {
    'road':     {'name': _('The open road'), 'emoji': '\U0001F6E4️', 'color': '#a16207'},
    'forest':   {'name': _('The forest'),    'emoji': '\U0001F332',       'color': '#15803d'},
    'river':    {'name': _('The river'),     'emoji': '\U0001F3DE️', 'color': '#0369a1'},
    'mountain': {'name': _('The mountains'), 'emoji': '⛰️',     'color': '#57534e'},
    'cave':     {'name': _('The caves'),     'emoji': '\U0001F573️', 'color': '#4c1d95'},
    'desert':   {'name': _('The desert'),    'emoji': '\U0001F3DC️', 'color': '#b45309'},
    'gate':     {'name': _('The gate'),      'emoji': '\U0001F3F0',       'color': '#9f1239'},
}


# ---------------------------------------------------------------------------
# The cast — who and what stands in the road
# ---------------------------------------------------------------------------
# Written once, combined endlessly by the map builder: the same trick that lets
# `mathchamp.py` never repeat itself with thirty-odd generators. `kinds` says
# which node types an encounter can serve, `terrain` where it belongs.
#
# `intro` is what the traveller meets, `win` what happens when they answer, and
# `lose` what happens when they do not — `lose` is never mocking, because a
# pupil who just got a question wrong is about to be asked to go and read.

ENCOUNTERS = [
    # ── the open road ──────────────────────────────────────────────────────
    {'slug': 'toll-post', 'kinds': ('gate',), 'terrain': 'road', 'emoji': '\U0001F6A7',
     'title': _('The Toll Post'),
     'intro': _('A striped pole blocks the road. The keeper leans out of his hut. "The toll is one right answer. I have no use for money out here."'),
     'win':   _('He lifts the pole and waves you through without another word.'),
     'lose':  _('The pole stays down. "Take your time," he says. "The road is not going anywhere."')},
    {'slug': 'caravan', 'kinds': ('gate', 'twin'), 'terrain': 'road', 'emoji': '\U0001F42A',
     'title': _('The Caravan Master'),
     'intro': _('A caravan has stopped across the whole width of the road. The master will only let you squeeze past if you are worth talking to.'),
     'win':   _('"Travel well," she says, and the camels shuffle aside.'),
     'lose':  _('She turns back to her animals. The road stays blocked.')},
    {'slug': 'milestone', 'kinds': ('gate',), 'terrain': 'road', 'emoji': '\U0001FAA8',
     'title': _('The Carved Milestone'),
     'intro': _('A stone stands at the roadside with writing cut deep into it. The road ahead blurs until the writing is read correctly.'),
     'win':   _('The letters settle. The road ahead comes back into focus.'),
     'lose':  _('The carving swims in front of your eyes and will not hold still.')},

    # ── the forest ─────────────────────────────────────────────────────────
    {'slug': 'woodcutter', 'kinds': ('gate',), 'terrain': 'forest', 'emoji': '\U0001FA93',
     'title': _('The Woodcutter'),
     'intro': _('A woodcutter rests her axe on a fallen trunk that lies across the path. "Help me think, and I will help you climb over."'),
     'win':   _('She rolls the trunk aside with one shove. She was never really stuck.'),
     'lose':  _('She shrugs and goes back to sharpening her axe.')},
    {'slug': 'talking-crow', 'kinds': ('gate', 'twin'), 'terrain': 'forest', 'emoji': '\U0001F426‍⬛',
     'title': _('The Talking Crow'),
     'intro': _('A crow drops onto the branch above you. "Two paths," it says. "I will tell you which — after you tell me this."'),
     'win':   _('The crow flaps ahead and waits at the right turning.'),
     'lose':  _('The crow says nothing at all, which is somehow worse.')},
    {'slug': 'thorn-wall', 'kinds': ('gate',), 'terrain': 'forest', 'emoji': '\U0001F33F',
     'title': _('The Thorn Wall'),
     'intro': _('Thorns have grown clean across the track. There is one gap, and only one, and finding it takes thinking rather than pushing.'),
     'win':   _('The gap opens exactly where the reasoning said it would.'),
     'lose':  _('The thorns hold. Pushing harder is not the answer here.')},
    {'slug': 'lost-child', 'kinds': ('gate',), 'terrain': 'forest', 'emoji': '\U0001F9D2',
     'title': _('The Lost Child'),
     'intro': _('A child sits crying on a stump. She has a homework page in her hand and cannot get past one question.'),
     'win':   _('She grins, folds the page away, and runs off shouting thanks.'),
     'lose':  _('She looks up at you hopefully. You will have to come back to this.')},

    # ── the river ──────────────────────────────────────────────────────────
    {'slug': 'bridge-keeper', 'kinds': ('gate', 'twin'), 'terrain': 'river', 'emoji': '\U0001F309',
     'title': _('The Bridge Keeper'),
     'intro': _('An old man sits at the head of a rope bridge. "Nobody crosses my bridge without paying," he says. "And I do not take money."'),
     'win':   _('He stands, bows, and steps aside. The planks hold.'),
     'lose':  _('He shakes his head slowly and does not move from the middle of the bridge.')},
    {'slug': 'ferryman', 'kinds': ('gate',), 'terrain': 'river', 'emoji': '\U0001F6F6',
     'title': _('The Ferryman'),
     'intro': _('The ferryman is already pushing off. "One question, quickly, or you wait for the next crossing."'),
     'win':   _('He swings the boat back around and holds it steady for you.'),
     'lose':  _('The boat glides out into the current without you.')},
    {'slug': 'stepping-stones', 'kinds': ('gate', 'twin'), 'terrain': 'river', 'emoji': '\U0001FAA8',
     'title': _('The Stepping Stones'),
     'intro': _('Stones cross the water, but only some of them are steady. Which ones — that has to be worked out from the bank.'),
     'win':   _('Every stone you chose holds firm. Dry feet on the far side.'),
     'lose':  _('The stone tilts under your foot and you jump back to the bank.')},
    {'slug': 'flooded-ford', 'kinds': ('gate',), 'terrain': 'river', 'emoji': '\U0001F30A',
     'title': _('The Flooded Ford'),
     'intro': _('The ford is deeper than it looks. A traveller waits on the bank, working out how deep — and she is stuck on the sum.'),
     'win':   _('The two of you wade across together, water at the knee, exactly as calculated.'),
     'lose':  _('Neither of you trusts the water. You both stay put.')},

    # ── the mountains ──────────────────────────────────────────────────────
    {'slug': 'rockfall', 'kinds': ('gate', 'twin'), 'terrain': 'mountain', 'emoji': '\U0001FAA8',
     'title': _('The Rockfall'),
     'intro': _('Boulders have come down across the pass. There is a way through them, but only one, and it has to be reasoned out.'),
     'win':   _('You thread the gap. The stones stay where they are.'),
     'lose':  _('Loose scree slides under your boots and you back away.')},
    {'slug': 'goat-path', 'kinds': ('gate',), 'terrain': 'mountain', 'emoji': '\U0001F410',
     'title': _('The Goat Path'),
     'intro': _('A goatherd blocks the narrow path with his flock. "This trail is dangerous. Prove you are thinking clearly today."'),
     'win':   _('He whistles; the goats part like water. "Go carefully."'),
     'lose':  _('He plants his staff. "Not today, then."')},
    {'slug': 'eagle', 'kinds': ('gate', 'twin'), 'terrain': 'mountain', 'emoji': '\U0001F985',
     'title': _('The Eagle'),
     'intro': _('An eagle drops onto the rock in front of you with something bright in its claws. It will trade — but not for food.'),
     'win':   _('It opens its claws, takes off, and shows you the ridge line from above.'),
     'lose':  _('It watches you for a long moment, then looks away.')},
    {'slug': 'snow-line', 'kinds': ('gate',), 'terrain': 'mountain', 'emoji': '\U0001F328️',
     'title': _('The Snow Line'),
     'intro': _('Above this point the snow starts. An old shepherd will lend you his coat, if you can keep up with him in conversation.'),
     'win':   _('The coat is heavy and warm and smells of woodsmoke. He waves you on.'),
     'lose':  _('He pulls the coat tighter around himself and says nothing.')},

    # ── the caves ──────────────────────────────────────────────────────────
    {'slug': 'stone-door', 'kinds': ('gate', 'twin'), 'terrain': 'cave', 'emoji': '\U0001F6AA',
     'title': _('The Stone Door'),
     'intro': _('A slab of rock seals the tunnel, and a question is cut into it. Doors like this have been opened by thinking for a thousand years.'),
     'win':   _('The slab grinds inward. Cold air comes out of the dark.'),
     'lose':  _('The stone does not move a hair. It has all the time in the world.')},
    {'slug': 'echo', 'kinds': ('gate',), 'terrain': 'cave', 'emoji': '\U0001F50A',
     'title': _('The Echo'),
     'intro': _('Something in the dark repeats every word you say — and then asks you a question in your own voice.'),
     'win':   _('The echo repeats your answer once, approvingly, and fades.'),
     'lose':  _('The echo repeats your answer, over and over, until you stop listening.')},
    {'slug': 'lantern-moth', 'kinds': ('gate',), 'terrain': 'cave', 'emoji': '\U0001FAB2',
     'title': _('The Lantern Moth'),
     'intro': _('One enormous moth glows in the passage. It only lights the way for travellers who are paying attention.'),
     'win':   _('It flares bright and drifts ahead of you down the tunnel.'),
     'lose':  _('Its light dims to almost nothing, and the tunnel closes in.')},
    {'slug': 'underground-river', 'kinds': ('gate', 'twin'), 'terrain': 'cave', 'emoji': '\U0001F4A7',
     'title': _('The Underground River'),
     'intro': _('Black water runs fast through the cave. Somewhere there is a ledge wide enough to walk — the trick is working out where.'),
     'win':   _('The ledge is exactly where the reasoning put it. You edge along it.'),
     'lose':  _('You cannot see the ledge, and guessing here would be foolish.')},

    # ── the desert ─────────────────────────────────────────────────────────
    {'slug': 'sandstorm', 'kinds': ('gate', 'twin'), 'terrain': 'desert', 'emoji': '\U0001F32A️',
     'title': _('The Sandstorm'),
     'intro': _('The horizon has gone brown. There is time to reach shelter, but only if you pick the right direction, and only right now.'),
     'win':   _('You reach the rock overhang as the first sand hits. Close.'),
     'lose':  _('The wind turns you around and pushes you back the way you came.')},
    {'slug': 'mirage', 'kinds': ('gate',), 'terrain': 'desert', 'emoji': '\U0001F4A0',
     'title': _('The Mirage'),
     'intro': _('There is water ahead. Or there is not. Only careful thinking tells the difference out here.'),
     'win':   _('The water is real. You drink, and fill the skin.'),
     'lose':  _('You walk toward it for an hour, and it walks away from you.')},
    {'slug': 'well-guard', 'kinds': ('gate',), 'terrain': 'desert', 'emoji': '\U0001F573️',
     'title': _('The Well Keeper'),
     'intro': _('The only well for a day\'s walk has a woman sitting on its lid. "Everyone drinks here," she says. "Everyone answers first."'),
     'win':   _('She slides the lid off and lowers the bucket herself.'),
     'lose':  _('She stays exactly where she is, and so does the lid.')},
    {'slug': 'salt-flat', 'kinds': ('gate',), 'terrain': 'desert', 'emoji': '\U0001F9C2',
     'title': _('The Salt Flat'),
     'intro': _('The crust is thin in places and will hold in others. A line of old footprints stops halfway across.'),
     'win':   _('Your route holds all the way. You do not look back at the footprints.'),
     'lose':  _('The crust creaks underfoot and you retreat to firm ground.')},

    # ── the final gate ─────────────────────────────────────────────────────
    {'slug': 'city-gate', 'kinds': ('gate',), 'terrain': 'gate', 'emoji': '\U0001F3EF',
     'title': _('The Outer Gate'),
     'intro': _('The city wall rises out of the plain. The outer gate is open, but a clerk with a ledger stands in it.'),
     'win':   _('He writes your name in the ledger and stands aside.'),
     'lose':  _('He closes the ledger. "Come back when you are ready."')},

    # ── camps ──────────────────────────────────────────────────────────────
    {'slug': 'campfire', 'kinds': ('camp',), 'terrain': 'forest', 'emoji': '\U0001F525',
     'title': _('A Fire in the Clearing'),
     'intro': _('Somebody has left a fire burning and a stack of dry wood beside it. Sit down. Nothing is chasing you.'),
     'win':   _('You rest until your legs stop aching, and bank the fire for the next traveller.'),
     'lose':  ''},
    {'slug': 'hot-spring', 'kinds': ('camp',), 'terrain': 'mountain', 'emoji': '♨️',
     'title': _('The Hot Spring'),
     'intro': _('Steam rises out of the rocks, and the water is exactly as hot as it should be. This is not a trap. Not everything is.'),
     'win':   _('You climb out warm to the bone and ready for the pass.'),
     'lose':  ''},
    {'slug': 'oasis', 'kinds': ('camp',), 'terrain': 'desert', 'emoji': '\U0001F334',
     'title': _('The Oasis'),
     'intro': _('Palms, shade, and water that is definitely water this time. Travellers sleep here in the heat of the day.'),
     'win':   _('You wake in the cool of the evening, water skin full.'),
     'lose':  ''},
    {'slug': 'shepherd-hut', 'kinds': ('camp',), 'terrain': 'road', 'emoji': '\U0001F6D6',
     'title': _("The Shepherd's Hut"),
     'intro': _('A one-room hut with the door on the latch, bread on the shelf, and a note that says: leave it as you found it.'),
     'win':   _('You sleep on the floor by the stove and leave bread for the next one.'),
     'lose':  ''},
    {'slug': 'ferry-inn', 'kinds': ('camp',), 'terrain': 'river', 'emoji': '\U0001F3E1',
     'title': _('The Inn at the Crossing'),
     'intro': _('An inn on the riverbank, full of people going the other way, all of them with advice.'),
     'win':   _('You eat, you listen, and you leave in the morning stronger than you arrived.'),
     'lose':  ''},

    # ── chests (Phase 2 uses these) ────────────────────────────────────────
    {'slug': 'buried-chest', 'kinds': ('chest',), 'terrain': 'forest', 'emoji': '\U0001F4E6',
     'title': _('Something Buried'),
     'intro': _('A corner of a wooden box shows through the leaf mould. It has been here a long time, and it is not locked.'),
     'win':   _('It comes out of the ground with a sucking sound. Heavier than it looks.'),
     'lose':  ''},
    {'slug': 'merchant-gift', 'kinds': ('chest',), 'terrain': 'road', 'emoji': '\U0001F381',
     'title': _("The Merchant's Thanks"),
     'intro': _('A merchant you helped at the last crossing catches up with you, out of breath, holding something out.'),
     'win':   _('"Take it, take it," he says, and is gone before you can argue.'),
     'lose':  ''},
    {'slug': 'sunken-crate', 'kinds': ('chest',), 'terrain': 'river', 'emoji': '\U0001F5DD️',
     'title': _('The Sunken Crate'),
     'intro': _('A crate is wedged under the bank, half in the water. Whatever is inside has stayed dry.'),
     'win':   _('You lever it loose and prise the lid up on the gravel.'),
     'lose':  ''},
    {'slug': 'cave-hoard', 'kinds': ('chest',), 'terrain': 'cave', 'emoji': '\U0001F48E',
     'title': _('The Little Hoard'),
     'intro': _('Somebody hid something in this crack in the wall and never came back for it. That was probably a long time ago.'),
     'win':   _('It fits in one hand, and it is worth carrying. Or worth leaving.'),
     'lose':  ''},

    # ── elders (Phase 3 uses these) ────────────────────────────────────────
    {'slug': 'old-woman', 'kinds': ('elder',), 'terrain': 'road', 'emoji': '\U0001F475',
     'title': _('The Woman at the Crossroads'),
     'intro': _('She has been sitting on that wall for longer than the wall has been there, and she has an opinion about your route.'),
     'win':   _('She tells you one true thing and goes back to watching the road.'),
     'lose':  ''},
    {'slug': 'wandering-poet', 'kinds': ('elder',), 'terrain': 'forest', 'emoji': '\U0001F3B5',
     'title': _('The Wandering Poet'),
     'intro': _('He is walking the other way and singing something with too many verses. He stops when he sees you.'),
     'win':   _('He gives you the last verse, which turns out to be directions.'),
     'lose':  ''},

    # ── the guardians (leg bosses) ─────────────────────────────────────────
    {'slug': 'gate-captain', 'kinds': ('guard',), 'terrain': 'gate', 'emoji': '\U0001F6E1️',
     'title': _('The Captain of the Gate'),
     'intro': _('The inner gate. The captain has your whole journey written on the page in front of her — and she asks about the road behind you, not the road ahead. "Three questions," she says. "You may miss one."'),
     'win':   _('She stamps the page and hauls the gate open herself. You are through.'),
     'lose':  _('She closes the ledger gently. "You know most of this. Go and find the rest."')},
    {'slug': 'stone-giant', 'kinds': ('guard',), 'terrain': 'gate', 'emoji': '\U0001F5FF',
     'title': _('The Stone Giant'),
     'intro': _('It has been sitting in the pass so long that trees grow on its shoulders. It opens one eye. It wants to know what you learned on the way here — all of it, not just the last bit.'),
     'win':   _('It stands, and the ground shakes, and the road behind it is open.'),
     'lose':  _('It closes its eye again. It is in no hurry, and it will be here when you return.')},
    {'slug': 'the-librarian', 'kinds': ('guard',), 'terrain': 'gate', 'emoji': '\U0001F4DA',
     'title': _('The Keeper of the Road Book'),
     'intro': _('Every traveller who ever walked this leg is written in his book. He turns to your page, which is nearly full, and asks about the beginning of it.'),
     'win':   _('He signs the bottom of your page and turns to a fresh one.'),
     'lose':  _('He leaves your page open. "Unfinished is not the same as failed."')},
    {'slug': 'river-dragon', 'kinds': ('guard',), 'terrain': 'gate', 'emoji': '\U0001F409',
     'title': _('The Dragon of the Last Crossing'),
     'intro': _('It is coiled around the last bridge, and it is far more interested in talking than in eating. It asks about the whole road, from the very first step.'),
     'win':   _('It uncoils, unhurried, and lets you walk the length of the bridge.'),
     'lose':  _('It settles back down across the planks. "Again, later. I am not going anywhere."')},
]

ENCOUNTER_MAP = {e['slug']: e for e in ENCOUNTERS}


def encounter(slug):
    """The cast member behind a node's `encounter` slug."""
    return ENCOUNTER_MAP.get(slug, ENCOUNTER_MAP['toll-post'])


# ---------------------------------------------------------------------------
# Branches — the forks in the road
# ---------------------------------------------------------------------------
# A fork is never a re-skin of the same walk: the branches carry the *same*
# lesson (so no fork lets a traveller skip content) but differ in how hard, how
# well paid and how long they are. `detour` costs nothing in strength — it eats
# into the speed bonus at the destination, which is how "the long way round"
# is made real without inventing a clock.
#
# And the reason forks matter most: **when a node seals, its siblings stay
# open.** Being stuck always has a way forward that is not "give up".

BRANCHES = {
    'hard': {
        'name':  _('The high road'),
        'note':  _('Shorter and meaner. Pays double.'),
        'emoji': '⚡',
        'threat_shift': 1, 'coin_multiplier': 2, 'detour': 0,
    },
    'safe': {
        'name':  _('The long way round'),
        'note':  _('Gentler, but you lose time. Pays less.'),
        'emoji': '\U0001F343',
        'threat_shift': -1, 'coin_multiplier': 1, 'detour': 1,
    },
    'torch': {
        'name':  _('The old track'),
        'note':  _('Middling — and somebody left a torch on it.'),
        'emoji': '\U0001F526',
        'threat_shift': 0, 'coin_multiplier': 1, 'detour': 0, 'torch': 1,
    },
}


def branch(key):
    return BRANCHES.get(key)


def terrain(key):
    return TERRAINS.get(key, TERRAINS['road'])


# ---------------------------------------------------------------------------
# Reading the courses
# ---------------------------------------------------------------------------

def road_lessons(road_slug):
    """The road's lessons, in course order, as light dicts.

    Only lessons that can actually supply a question are returned — a published
    lesson with a published practice that has questions. PK-1…8 and PR-1…5 have
    12-question reading drills rather than 20, which is fine; a lesson with none
    at all would be a hole in the road, so it is left out entirely.
    """
    from tutorial.models import TutorialPlaylist

    road = ROAD_MAP.get(road_slug)
    if not road:
        return []

    playlist = (TutorialPlaylist.objects
                .filter(title=road['playlist'], is_published=True)
                .first())
    if not playlist:
        return []

    lessons = []
    items = (playlist.items.select_related('tutorial')
             .prefetch_related('tutorial__practices')
             .order_by('order'))
    for item in items:
        tutorial = item.tutorial
        if not tutorial.is_published:
            continue
        practice = next(
            (p for p in tutorial.practices.all() if p.is_published), None)
        if practice is None:
            continue
        lessons.append({
            'id':       tutorial.id,
            'title':    tutorial.title,
            'order':    item.order,
            'practice': practice.id,
        })
    return lessons


def leg_count(road_slug):
    """How many legs this road has today. Grows as the course is written."""
    return max(1, math.ceil(len(road_lessons(road_slug)) / LEG_SIZE))


def leg_lessons(road_slug, leg):
    """The (up to) ten lessons of one leg. `leg` is 1-based."""
    lessons = road_lessons(road_slug)
    start = (leg - 1) * LEG_SIZE
    return lessons[start:start + LEG_SIZE]


def leg_place(road_slug, leg):
    """The name of a leg's destination."""
    road = ROAD_MAP.get(road_slug)
    if not road:
        return ''
    places = road['places']
    return places[(leg - 1) % len(places)]


# ---------------------------------------------------------------------------
# Building a map
# ---------------------------------------------------------------------------

def _terrain_for(step_index, total_steps):
    """Where on the terrain arc this step falls."""
    if total_steps <= 1:
        return TERRAIN_ARC[0]
    pos = step_index / (total_steps - 1)
    idx = min(len(TERRAIN_ARC) - 1, int(pos * len(TERRAIN_ARC)))
    return TERRAIN_ARC[idx]


def _pick_encounter(rng, kind, terrain_key, used):
    """An encounter of this kind, preferring one that belongs to this terrain
    and one that has not been seen yet on this leg."""
    same = [e for e in ENCOUNTERS if kind in e['kinds'] and e['terrain'] == terrain_key]
    any_terrain = [e for e in ENCOUNTERS if kind in e['kinds']]
    # Belonging to the terrain beats being new: an inn on a riverbank reads
    # better than a riverbank inn found halfway down a cave.
    for pool in (
        [e for e in same if e['slug'] not in used],
        same,
        [e for e in any_terrain if e['slug'] not in used],
        any_terrain,
    ):
        if pool:
            choice = rng.choice(pool)
            used.add(choice['slug'])
            return choice['slug']
    return 'toll-post'


def _threat_for(index, total):
    """Obstacles get harder as the leg goes on: 1 → 2 → 3.

    This is where the questions become *thoughtful* without a word of new
    content being written. The practice banks are authored easy→hard and the
    Prime Math guide puts word problems at Q19–20, so a threat-3 node reaching
    into the tail of the bank is reaching for the word problems.
    """
    if total <= 1:
        return 2
    pos = index / (total - 1)
    if pos < 0.35:
        return 1
    if pos < 0.75:
        return 2
    return 3


def node_coins(node):
    """What passing this node pays."""
    if node['kind'] == 'elder':
        return ELDER_COINS
    if node['kind'] == 'guard':
        return GUARD_COINS
    base = COINS_BY_THREAT.get(node.get('threat', 1), 10)
    if node['kind'] == 'twin':
        base *= TWIN_MULTIPLIER
    return base * node.get('coin_multiplier', 1)


# A prize does not wait at the end of every stage — that handed out far too many.
# One turns up on the first stage of a road (an early hook is worth a lot) and
# then every third: stages 1, 4, 7, 10. On the rest, the guardian is simply the
# last thing standing between the traveller and the destination.
PRIZE_EVERY = 3


def has_prize(leg):
    """True when this stage ends with a chest before its guardian."""
    return (leg - 1) % PRIZE_EVERY == 0


def build_map(road_slug, leg, seed):
    """The whole leg, decided up front and JSON-safe.

    Returns a list of **steps**; each step is a list of **nodes**. A step with
    more than one node is a fork, and the traveller walks exactly one of them.
    """
    lessons = leg_lessons(road_slug, leg)
    if not lessons:
        return []

    rng = random.Random(seed)
    used = set()

    # ── the beat sheet ──────────────────────────────────────────────────
    # One beat per lesson, with camps and chests threaded between them, and
    # the guardian at the end. Positions are jittered by the seed so two runs
    # of the same leg do not rest in the same places.
    beats = []                                   # (kind, lesson index or None)
    rest_after = {rng.choice((2, 3)), rng.choice((6, 7))}

    elder_after = rng.choice((3, 4, 5))

    for i in range(len(lessons)):
        beats.append(('lesson', i))
        if i in rest_after:
            beats.append(('camp', None))
        if i == elder_after:
            beats.append(('elder', None))

    # When this stage carries a prize it stands immediately before the guardian —
    # the only placement that makes "take it or leave it" a real decision. A
    # chest after the guardian would be free (nothing left to risk); a chest in
    # the middle asks the traveller to guess at dangers they cannot see. Here
    # they know exactly what they are gambling against: the guardian, next.
    if has_prize(leg):
        beats.append(('chest', None))
    beats.append(('guard', None))

    # Two of the lesson beats become forks — one early, one late — and one
    # becomes a twin obstacle. Never the first beat: nobody should meet a
    # choice before they have met the road.
    lesson_positions = [n for n, (kind, _i) in enumerate(beats) if kind == 'lesson']
    forkable = lesson_positions[1:-1] or lesson_positions
    fork_positions = set()
    if len(forkable) >= 4:
        fork_positions.add(rng.choice(forkable[:len(forkable) // 2]))
        fork_positions.add(rng.choice(forkable[len(forkable) // 2:]))
    elif forkable:
        fork_positions.add(rng.choice(forkable))

    twin_pool = [p for p in forkable if p not in fork_positions]
    twin_positions = {rng.choice(twin_pool)} if twin_pool else set()

    # ── the map ─────────────────────────────────────────────────────────
    steps = []
    total = len(beats)
    for n, (kind, lesson_index) in enumerate(beats):
        terrain_key = _terrain_for(n, total)

        if kind == 'camp':
            steps.append([{
                'id': f's{n}n0', 'kind': 'camp', 'terrain': terrain_key,
                'encounter': _pick_encounter(rng, 'camp', terrain_key, used),
            }])
            continue

        if kind == 'chest':
            steps.append([{
                'id': f's{n}n0', 'kind': 'chest', 'terrain': terrain_key,
                'encounter': _pick_encounter(rng, 'chest', terrain_key, used),
            }])
            continue

        if kind == 'elder':
            # No lesson attached, on purpose: the riddle bank is free of the
            # course, so the same stranger can stop a maths traveller and a
            # Korean one with the same puzzle.
            steps.append([{
                'id': f's{n}n0', 'kind': 'elder', 'terrain': terrain_key,
                'encounter': _pick_encounter(rng, 'elder', terrain_key, used),
            }])
            continue

        if kind == 'guard':
            # The boss asks about the road *behind* you: three questions drawn
            # from earlier lessons of this same leg. Spaced repetition in a
            # costume, and the single most valuable node on the map.
            sources = [l['id'] for l in lessons]
            rng.shuffle(sources)
            steps.append([{
                'id': f's{n}n0', 'kind': 'guard', 'terrain': 'gate',
                'encounter': _pick_encounter(rng, 'guard', 'gate', used),
                'lesson': lessons[-1]['id'],
                'lesson_title': lessons[-1]['title'],
                'sources': sources[:3] or [lessons[-1]['id']],
                'threat': 3,
            }])
            continue

        lesson = lessons[lesson_index]
        base_threat = _threat_for(lesson_index, len(lessons))
        node_kind = 'twin' if n in twin_positions else 'gate'

        if n in fork_positions:
            keys = ['hard', 'safe'] if rng.random() < 0.6 else ['hard', 'safe', 'torch']
            nodes = []
            for m, key in enumerate(keys):
                spec = BRANCHES[key]
                nodes.append({
                    'id': f's{n}n{m}', 'kind': 'gate', 'terrain': terrain_key,
                    'encounter': _pick_encounter(rng, 'gate', terrain_key, used),
                    'lesson': lesson['id'], 'lesson_title': lesson['title'],
                    'threat': min(3, max(1, base_threat + spec['threat_shift'])),
                    'branch': key,
                    'coin_multiplier': spec['coin_multiplier'],
                    'detour': spec['detour'],
                    'torch': spec.get('torch', 0),
                })
            steps.append(nodes)
            continue

        steps.append([{
            'id': f's{n}n0', 'kind': node_kind, 'terrain': terrain_key,
            'encounter': _pick_encounter(rng, node_kind, terrain_key, used),
            'lesson': lesson['id'], 'lesson_title': lesson['title'],
            'threat': base_threat,
        }])

    return steps


# ---------------------------------------------------------------------------
# Questions — spending what the courses already wrote
# ---------------------------------------------------------------------------

def pick_question(lesson_id, threat, seen_ids):
    """One question from this lesson's practice, sliced by threat.

    The threat slice is the whole trick: your banks are written easy→hard, so
    a hard obstacle simply reaches into the tail of the bank and comes back
    with the word problems.

    `seen_ids` is everything this traveller has met before — twenty questions
    per lesson means a retry is genuinely a different question. The pool is
    widened rather than allowed to come back empty, so a 12-question alphabet
    drill still works.
    """
    from tutorial.models import Tutorial

    tutorial = (Tutorial.objects
                .filter(id=lesson_id, is_published=True)
                .prefetch_related('practices')
                .first())
    if tutorial is None:
        return None
    practice = next((p for p in tutorial.practices.all() if p.is_published), None)
    if practice is None:
        return None

    questions = list(practice.questions.order_by('order', 'id'))
    if not questions:
        return None

    n = len(questions)
    if threat >= 3:
        pool = questions[int(n * 0.7):]
    elif threat == 2:
        pool = questions[int(n * 0.4):]
    else:
        pool = questions[:max(1, int(n * 0.6))]

    seen = set(seen_ids or ())
    # Narrow slice first, then the whole bank, then give up on freshness —
    # never come back empty and strand a traveller at a node.
    for candidates in (
        [q for q in pool if q.id not in seen],
        [q for q in questions if q.id not in seen],
        pool,
        questions,
    ):
        if candidates:
            question = random.choice(candidates)
            break

    return {
        'qid':         question.id,
        'text':        str(question.question_text),
        'hint':        str(question.hint or ''),
        'explanation': str(question.explanation or ''),
        'choices':     [{'id': c.id, 'text': c.text}
                        for c in question.display_choices()],
        'correct':     next((c.id for c in question.choices.all() if c.is_correct), None),
        'lesson':      tutorial.id,
        'lesson_title': tutorial.title,
    }


# ---------------------------------------------------------------------------
# The state of one journey
# ---------------------------------------------------------------------------

def new_state(road_slug, leg, seed=None):
    """A fresh journey. Everything in here is JSON-safe."""
    seed = seed if seed is not None else random.randrange(1, 10 ** 9)
    game_map = build_map(road_slug, leg, seed)
    return {
        'v':         STATE_VERSION,
        'road':      road_slug,
        'leg':       leg,
        'seed':      seed,
        'map':       game_map,
        'step':      0,
        'node':      0,
        'chosen':    {},          # str(step index) -> node index, for the map trail
        'kuch':      MAX_KUCH,
        'max_kuch':  MAX_KUCH,
        'coins':     0,
        'detours':   0,
        'torches':   0,
        'wrong_here': 0,          # wrong answers at the node they stand on
        'wrong_total': 0,         # …and over the whole stage: every 2nd costs a heart
        'last_stand': False,      # the one reprieve, once used
        'sealed':    [],
        'q':         None,
        'twin_done': 0,
        'guard_right': 0,
        'guard_wrong': 0,
        'feedback':  None,
        'seen':      [],          # guests keep their seen list here
        'status':    'travelling',
        'paused_at': 0,
        'started':   int(time.time()),
        'elapsed':   0,
        'log':       [],
    }


def current_step(state):
    """The nodes offered at the traveller's current position, or None at the end."""
    game_map = state.get('map') or []
    if state['step'] >= len(game_map):
        return None
    return game_map[state['step']]


def current_node(state):
    """The node the traveller is standing on, or None if a fork is unresolved."""
    step = current_step(state)
    if not step:
        return None
    if len(step) > 1 and str(state['step']) not in state.get('chosen', {}):
        return None
    index = state.get('node', 0)
    if index >= len(step):
        index = 0
    return step[index]


def at_fork(state):
    """True when the traveller must choose a branch before anything else."""
    step = current_step(state)
    return bool(step) and len(step) > 1 and str(state['step']) not in state.get('chosen', {})


def choose_branch(state, index):
    """Walk into one of a fork's branches."""
    step = current_step(state)
    if not step or index < 0 or index >= len(step):
        return False
    state['chosen'][str(state['step'])] = index
    state['node'] = index
    state['wrong_here'] = 0
    state['twin_done'] = 0
    state['q'] = None
    node = step[index]
    state['detours'] += node.get('detour', 0)
    if node.get('torch'):
        state['torches'] += node['torch']
        add_log(state, _('You find a torch left on the old track.'))
    return True


def is_sealed(state, node):
    return node and node.get('id') in state.get('sealed', [])


def seal(state, node):
    if node and node['id'] not in state['sealed']:
        state['sealed'].append(node['id'])


def unseal(state, node):
    if node and node['id'] in state.get('sealed', []):
        state['sealed'].remove(node['id'])


def siblings_open(state):
    """True when the current step still has a branch that is not sealed —
    i.e. being stuck here has a way forward that is not "give up"."""
    step = current_step(state)
    if not step or len(step) < 2:
        return False
    sealed = set(state.get('sealed', []))
    return any(n['id'] not in sealed for n in step)


def advance(state):
    """Move on to the next step of the road."""
    state['step'] += 1
    state['node'] = 0
    state['wrong_here'] = 0
    state['twin_done'] = 0
    state['guard_right'] = 0
    state['guard_wrong'] = 0
    state['q'] = None
    if state['step'] >= len(state.get('map') or []):
        finish(state)


def finish(state):
    state['status'] = 'finished'
    state['elapsed'] = int(time.time()) - state.get('started', int(time.time()))
    state['coins'] += arrival_bonus(state)


def arrival_bonus(state):
    """What reaching the destination is worth on top of the road itself.

    Strength left over and a road walked without detours both pay — so the
    traveller who studied and went straight there earns more than the one who
    wandered, without either of them being punished.
    """
    bonus = 50
    bonus += 10 * state.get('kuch', 0)
    bonus -= 5 * state.get('detours', 0)
    return max(0, bonus)


def add_log(state, line):
    """One line in the journey diary. Lazy strings are resolved here, because
    the log is stored as JSON alongside the map."""
    log = state.setdefault('log', [])
    log.append(str(line))
    del log[:-LOG_LIMIT]


def out_of_hearts(state):
    """The last heart is gone.

    Not the end yet — not the first time. A traveller who has not spent their
    *last stand* is stopped rather than finished, and the only thing that will
    get them moving again is passing a practice from this stage. Spend it, run
    out a second time, and the road is over.
    """
    if state.get('last_stand'):
        fail(state)
    else:
        state['status'] = 'stopped'
        add_log(state, _('Your last heart is gone. Only proving a lesson will '
                         'get you back on your feet.'))


def fail(state):
    """The stage is lost. Whatever was left on the road is left there."""
    state['status'] = 'failed'
    state['elapsed'] = int(time.time()) - state.get('started', int(time.time()))
    state['lost'] = len(state.get('left_behind', []))
    state['left_behind'] = []
    add_log(state, _('The road beat you this time. What you left behind stays '
                     'where it lies.'))


def last_stand(state):
    """Bought with a passed practice: one heart, one more chance, once."""
    state['status'] = 'travelling'
    state['last_stand'] = True
    state['kuch'] = max(1, state['kuch'])
    state['wrong_here'] = 0
    state['q'] = None
    add_log(state, _('You proved a lesson and got back on your feet. There is '
                     'no second reprieve.'))


def spend_kuch(state, amount=1):
    state['kuch'] = max(0, state['kuch'] - amount)
    return state['kuch']


def count_wrong(state):
    """Record a wrong answer; every second one costs a heart.

    Counted over the whole stage rather than per node, so two slips at two
    different obstacles cost exactly what two slips at one obstacle cost.
    Returns True if this was the answer that took a heart.
    """
    state['wrong_total'] = state.get('wrong_total', 0) + 1
    if state['wrong_total'] % WRONGS_PER_HEART == 0:
        spend_kuch(state, 1)
        return True
    return False


def wrong_until_heart(state):
    """Wrong answers left before the next heart goes — for the warning line."""
    return WRONGS_PER_HEART - (state.get('wrong_total', 0) % WRONGS_PER_HEART)


def heal(state, amount):
    state['kuch'] = min(state['max_kuch'], state['kuch'] + amount)


def progress_row(state):
    """One dot per step, for the trail strip above the encounter card."""
    row = []
    game_map = state.get('map') or []
    for n, step in enumerate(game_map):
        if n < state['step']:
            cls = 'done'
        elif n == state['step']:
            cls = 'current'
        else:
            cls = 'todo'
        chosen = state.get('chosen', {}).get(str(n), 0)
        node = step[chosen] if chosen < len(step) else step[0]
        row.append({
            'cls':   cls,
            'kind':  node['kind'],
            'fork':  len(step) > 1,
            'emoji': encounter(node['encounter'])['emoji'],
        })
    return row
