"""Logic Arena — puzzles 9-16 (season 1, rounds 5-8).

Round 6 is the flagship: #11 is the twelve-coin problem, which only makes sense
to a pupil who has already met #1 in the archive — the season is built so the
hard weighing puzzle arrives after the easy one has been revealed and explained.

Every answer key was recomputed independently by `verify_logic_01_16.py` before
import. SCHEDULE is copied unchanged from `_puzzles_logic_01_08.py`; the two
files describe one season and must agree on when round 1 opened.
"""
from logic.figures import balance, bookshelf, coins, fig, row

SCHEDULE = {
    'start':  '2026-07-13 09:00',
    'days':   7,
    'window': 7,
}


PUZZLES = [

    # ── Round 5 ─────────────────────────────────────────────────────────────
    {
        'number': 9, 'round': 5, 'category': 'weighing', 'difficulty': 3,
        'title':    'Ten Sacks, One Weighing',
        'title_uz': 'Oʻnta qop, bitta tortish',
        'teaser':    'One sack is full of forgeries. You may use the scale once.',
        'teaser_uz': 'Bitta qop toʻla soxta tanga. Tarozidan bir marta foydalanasiz.',

        'body':
            '<p>Ten sacks stand in a row, numbered 1 to 10. Nine of them are full of real '
            'coins weighing <strong>10 grams</strong> each. One sack — you do not know '
            'which — is full of forgeries, and every forged coin weighs '
            '<strong>9 grams</strong>: exactly one gram light.</p>'
            '<p>This time the scale is a modern one with a display: it tells you a '
            '<strong>weight in grams</strong>, not just which side is heavier. Each sack '
            'holds hundreds of coins, and you may take out as many as you like from any '
            'sack.</p>'
            + fig(row(['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟'],
                      box=True, glyph_size=20),
                  'Ten sacks. One is fake, and nothing on the outside says which.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⚖️</span>'
              '<span>You may switch the scale on <strong>once</strong>. One weighing, '
              'one number, and you must name the sack.</span></div>'
            '<p>Here is the beautiful part: it can be done, and the plan does not depend '
            'on luck at all. Work out what to put on the scale — then use the reading '
            'below.</p>'
            '<p>Following your own plan, the display reads <strong>543 grams</strong>.</p>'
            '<p class="lg-ask">Answer to type: the <strong>number of the fake sack</strong>.</p>',

        'body_uz':
            '<p>Bir qatorda oʻnta qop turibdi, 1 dan 10 gacha raqamlangan. Toʻqqiztasi '
            'haqiqiy tangalarga toʻla, har biri <strong>10 gramm</strong>. Bitta qop — '
            'qaysi biri ekanini bilmaysiz — soxta tangalarga toʻla va har bir soxta tanga '
            '<strong>9 gramm</strong>: aniq bir gramm yengil.</p>'
            '<p>Bu safar tarozi zamonaviy, ekranli: u qaysi tomon ogʻir ekanini emas, '
            '<strong>grammdagi ogʻirlikni</strong> koʻrsatadi. Har bir qopda yuzlab tanga '
            'bor va istalgan qopdan xohlagancha tanga olishingiz mumkin.</p>'
            + fig(row(['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟'],
                      box=True, glyph_size=20),
                  'Oʻnta qop. Bittasi soxta, tashqarisidan bilib boʻlmaydi.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⚖️</span>'
              '<span>Tarozini <strong>bir marta</strong> yoqasiz. Bitta tortish, bitta '
              'raqam — va qopni aytishingiz shart.</span></div>'
            '<p>Eng chiroyli tomoni shundaki, buni uddalash mumkin va reja umuman omadga '
            'bogʻliq emas. Taroziga nima qoʻyishni oʻylab toping — keyin quyidagi '
            'koʻrsatkichdan foydalaning.</p>'
            '<p>Oʻz rejangiz boʻyicha ish tutdingiz va ekranda <strong>543 gramm</strong> '
            'chiqdi.</p>'
            '<p class="lg-ask">Javob sifatida yozing: <strong>soxta qopning '
            'raqami</strong>.</p>',

        'hint':    'If you take the same number of coins from every sack, the total tells '
                   'you nothing about which sack it was. So take a different number from '
                   'each.',
        'hint_uz': 'Har qopdan bir xil miqdorda tanga olsangiz, umumiy ogʻirlik qaysi qop '
                   'ekanini aytmaydi. Demak har biridan har xil miqdorda oling.',

        'answer_key': '7',
        'accepted': ['sack 7', '7-qop', '7 qop', 'seven', 'yetti'],
        'answer_hint':    'a sack number, 1-10',
        'answer_hint_uz': 'qop raqami, 1-10',

        'solution':
            '<ol class="lg-steps">'
            '<li>Take <strong>1 coin from sack 1, 2 coins from sack 2, 3 from sack 3</strong> '
            '… and 10 coins from sack 10. That is 1 + 2 + … + 10 = <strong>55 coins</strong> '
            'in one heap.</li>'
            '<li>If every coin were real, the heap would weigh 55 × 10 = '
            '<strong>550 grams</strong>.</li>'
            '<li>But the coins from the fake sack are 1 gram light each — and you took '
            'exactly as many of them as the sack\'s number. So the heap is short by '
            'exactly <strong>the number of the fake sack</strong>, in grams.</li>'
            '<li>The display reads 543. The shortfall is 550 − 543 = '
            '<strong>7 grams</strong>.</li>'
            '<li>So the forgeries are in <strong>sack 7</strong>. One weighing, no luck '
            'involved.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> a single number can carry a '
            'lot of information if you arrange for each possibility to change it by a '
            'different amount. Taking a different count from each sack turns "which one?" '
            'into arithmetic. This is exactly how a checksum works — one number that '
            'quietly tells you <em>where</em> something went wrong.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li><strong>1-qopdan 1 ta, 2-qopdan 2 ta, 3-qopdan 3 ta</strong> … '
            '10-qopdan 10 ta tanga oling. Jami 1 + 2 + … + 10 = <strong>55 ta '
            'tanga</strong> bitta uyumda.</li>'
            '<li>Agar hamma tanga haqiqiy boʻlsa, uyum 55 × 10 = '
            '<strong>550 gramm</strong> tortardi.</li>'
            '<li>Ammo soxta qopdagi tangalarning har biri 1 gramm yengil — siz esa '
            'ulardan aynan qop raqamiga teng miqdorda oldingiz. Demak uyum aniq '
            '<strong>soxta qop raqamiga teng</strong> gramm kam chiqadi.</li>'
            '<li>Ekranda 543. Kamomad: 550 − 543 = <strong>7 gramm</strong>.</li>'
            '<li>Demak soxta tangalar <strong>7-qopda</strong>. Bitta tortish, omadning '
            'aloqasi yoʻq.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> agar har bir ehtimol raqamni '
            'har xil miqdorda oʻzgartiradigan qilib tuzsangiz, bitta son juda koʻp '
            'axborot tashiy oladi. Har qopdan har xil son olish "qaysi biri?" degan '
            'savolni oddiy arifmetikaga aylantiradi. Nazorat yigʻindisi (checksum) aynan '
            'shunday ishlaydi — bitta son xato <em>qayerda</em> boʻlganini aytib '
            'beradi.</p>',
    },

    {
        'number': 10, 'round': 5, 'category': 'shapes', 'difficulty': 4,
        'title':    "The Bookworm's Journey",
        'title_uz': 'Kitob qurtining yoʻli',
        'teaser':    'Ten volumes on a shelf. The worm eats straight through. How far?',
        'teaser_uz': 'Javonda oʻnta jild. Qurt toʻgʻriga teshib oʻtadi. Necha santimetr?',

        'body':
            '<p>A ten-volume encyclopaedia stands on a shelf in the usual way: volume 1 on '
            'the left, volume 10 on the right, spines facing you, each book the right way '
            'up and the right way round.</p>'
            '<p>Every volume is built the same: <strong>3 cm of pages</strong> between two '
            'covers, and each cover is <strong>2 mm</strong> thick.</p>'
            '<p>A bookworm starts at <strong>page 1 of volume 1</strong> and eats in a '
            'perfectly straight horizontal line until it reaches the <strong>last page of '
            'volume 10</strong>.</p>'
            + fig(bookshelf(10),
                  'Volume 1 on the left. The red marks show where page 1 and the last '
                  'page actually are once the books are shelved.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">📚</span>'
              '<span>Before you multiply anything: take a real book off a shelf and check '
              'which side page 1 is on. That is the whole puzzle.</span></div>'
            '<p class="lg-ask">Answer to type: the distance the worm travels, in '
            '<strong>centimetres</strong>.</p>',

        'body_uz':
            '<p>Oʻn jildli qomus javonda odatdagidek turibdi: 1-jild chapda, 10-jild '
            'oʻngda, muqovalari sizga qaragan, har bir kitob toʻgʻri holatda.</p>'
            '<p>Har bir jild bir xil: ikki muqova orasida <strong>3 sm sahifa</strong>, '
            'har bir muqova esa <strong>2 mm</strong> qalinlikda.</p>'
            '<p>Kitob qurti <strong>1-jildning 1-sahifasidan</strong> boshlab, aniq '
            'toʻgʻri chiziq boʻylab <strong>10-jildning oxirgi sahifasigacha</strong> '
            'teshib boradi.</p>'
            + fig(bookshelf(10),
                  'Chapda 1-jild. Qizil chiziqlar kitoblar javonga terilganda 1-sahifa '
                  'va oxirgi sahifa aslida qayerda ekanini koʻrsatadi.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">📚</span>'
              '<span>Koʻpaytirishdan oldin: javondan haqiqiy kitob olib, 1-sahifa qaysi '
              'tomonda ekanini tekshiring. Butun jumboq shunda.</span></div>'
            '<p class="lg-ask">Javob sifatida yozing: qurt bosib oʻtgan masofa, '
            '<strong>santimetrda</strong>.</p>',

        'hint':    'When a book stands on a shelf with its spine towards you, its first '
                   'page is on the side nearest the *next* volume, not the previous one.',
        'hint_uz': 'Kitob javonda muqovasi sizga qarab tursa, uning birinchi sahifasi '
                   'oldingi emas, *keyingi* jildga yaqin tomonda boʻladi.',

        'answer_key': '27.6',
        'accepted': ['27,6', '27.6 cm', '27,6 sm', '27.6cm', '276 mm', '276mm'],
        'answer_hint':    'a distance in cm (a decimal)',
        'answer_hint_uz': 'sm dagi masofa (oʻnli son)',

        'solution':
            '<ol class="lg-steps">'
            '<li>Stand a book on a shelf, spine towards you. Its pages run from the front '
            'cover backwards — and the <strong>front cover of volume 1 faces volume '
            '2</strong>, to the right. So <strong>page 1 of volume 1 is at the right-hand '
            'edge of volume 1</strong>, right up against volume 2.</li>'
            '<li>By the same reasoning, the <strong>last page of volume 10 is at its '
            'left-hand edge</strong>, right up against volume 9.</li>'
            '<li>So the worm never crosses the pages of volume 1 or volume 10 at all! It '
            'crosses only volume 1\'s front cover, then volumes 2 to 9 completely, then '
            'volume 10\'s back cover.</li>'
            '<li>Each whole volume is 3 cm + 2 × 0,2 cm = <strong>3,4 cm</strong>. Volumes '
            '2 to 9 is <strong>eight</strong> volumes: 8 × 3,4 = 27,2 cm.</li>'
            '<li>Add the two covers at the ends: 27,2 + 0,2 + 0,2 = '
            '<strong>27,6 cm</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> the arithmetic here is easy — '
            'the difficulty is entirely in noticing that the books are the wrong way round '
            'from what you imagined. Most people answer 34 cm (all ten volumes) and never '
            'doubt it. Before you calculate, draw the situation: half of all mistakes in '
            'word problems are made before the first multiplication.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Kitobni javonga muqovasi sizga qaratib qoʻying. Sahifalar old muqovadan '
            'orqaga qarab boradi — <strong>1-jildning old muqovasi esa 2-jildga</strong>, '
            'yaʼni oʻngga qaraydi. Demak <strong>1-jildning 1-sahifasi uning oʻng '
            'chetida</strong>, 2-jildga tegib turibdi.</li>'
            '<li>Xuddi shu mulohaza bilan, <strong>10-jildning oxirgi sahifasi uning chap '
            'chetida</strong>, 9-jildga tegib turadi.</li>'
            '<li>Demak qurt 1-jild va 10-jildning sahifalarini umuman kesib '
            'oʻtmaydi! U faqat 1-jildning old muqovasini, keyin 2-9-jildlarni toʻliq, '
            'soʻng 10-jildning orqa muqovasini teshadi.</li>'
            '<li>Bitta toʻliq jild: 3 sm + 2 × 0,2 sm = <strong>3,4 sm</strong>. '
            '2-jilddan 9-jildgacha — <strong>sakkizta</strong> jild: 8 × 3,4 = 27,2 sm.</li>'
            '<li>Chetlardagi ikki muqovani qoʻshamiz: 27,2 + 0,2 + 0,2 = '
            '<strong>27,6 sm</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> bu yerdagi hisob juda oson — '
            'butun qiyinchilik kitoblar siz tasavvur qilgandan teskari turganini '
            'payqashda. Koʻpchilik 34 sm (oʻnala jild) deb javob beradi va shubhalanmaydi '
            'ham. Hisoblashdan oldin vaziyatni chizing: matnli masalalardagi xatolarning '
            'yarmi birinchi koʻpaytirishgacha qilinadi.</p>',
    },

    # ── Round 6 — LIVE ──────────────────────────────────────────────────────
    {
        'number': 11, 'round': 6, 'category': 'weighing', 'difficulty': 5,
        'title':    'The Twelve Coins',
        'title_uz': 'Oʻn ikki tanga',
        'teaser':    'One coin is wrong — but nobody will tell you whether it is heavy '
                     'or light.',
        'teaser_uz': 'Bitta tanga notoʻgʻri — ammo u ogʻirmi yoki yengilmi, hech kim '
                     'aytmaydi.',

        'body':
            '<p>This is the hardest and most famous weighing puzzle there is. If you have '
            'read <em>The Lighter Coin</em> (puzzle #1) and its solution, you have exactly '
            'the tool you need — and you will still find this one difficult.</p>'
            '<p>There are <strong>twelve coins</strong>. Eleven are identical. One is '
            'different: it might be <strong>heavier</strong>, or it might be '
            '<strong>lighter</strong>, and <strong>you are not told which</strong>.</p>'
            '<p>You have a two-pan balance again — three outcomes, no numbers.</p>'
            + fig(coins(12, groups=[4, 4, 4], labels=['4 coins', '4 coins', '4 coins']),
                  'Twelve coins. One of them is wrong in an unknown direction.')
            + fig(balance('4', '4', tilt=-1, caption_left='heavier?',
                          caption_right='or is the other side lighter?'),
                  'The difficulty in one picture: a tilt does not tell you which side is '
                  'lying.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⛔</span>'
              '<span><strong>Three weighings.</strong> And you must not only point at the '
              'odd coin — you must also say whether it is heavy or light.</span></div>'
            '<p>It really can be done, every time. Work out how, then count what the '
            'method is worth: each weighing still has three outcomes, but now every coin '
            'has <em>two</em> possible faults, and one outcome has to be spent on the case '
            'where nothing is wrong.</p>'
            '<p class="lg-ask">Answer to type: with <strong>four</strong> weighings instead '
            'of three, what is the largest number of coins you could handle under these '
            'same rules — finding the odd coin <em>and</em> saying whether it is heavy or '
            'light?</p>',

        'body_uz':
            '<p>Bu — tarozi haqidagi eng qiyin va eng mashhur jumboq. Agar '
            '<em>Yengil tanga</em> (1-jumboq) va uning yechimini oʻqigan boʻlsangiz, kerakli '
            'qurol sizda bor — shunda ham bu oson boʻlmaydi.</p>'
            '<p><strong>Oʻn ikkita tanga</strong> bor. Oʻn bittasi bir xil. Bittasi farq '
            'qiladi: u <strong>ogʻirroq</strong> boʻlishi ham, <strong>yengilroq</strong> '
            'boʻlishi ham mumkin va <strong>qaysi biri ekani aytilmaydi</strong>.</p>'
            '<p>Sizda yana ikki pallali tarozi — uchta javob, raqam yoʻq.</p>'
            + fig(coins(12, groups=[4, 4, 4], labels=['4 ta', '4 ta', '4 ta']),
                  'Oʻn ikki tanga. Bittasi nomaʼlum tomonga "notoʻgʻri".')
            + fig(balance('4', '4', tilt=-1, caption_left='ogʻirroqmi?',
                          caption_right='yoki narigi tomon yengilroqmi?'),
                  'Qiyinchilik bitta rasmda: ogʻish qaysi tomon "aldayotganini" '
                  'aytmaydi.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⛔</span>'
              '<span><strong>Uch marta tortish.</strong> Va siz nafaqat notoʻgʻri tangani '
              'koʻrsatishingiz, balki u ogʻirmi yoki yengilmi — buni ham aytishingiz '
              'shart.</span></div>'
            '<p>Buni har safar uddalash mumkin. Usulini toping, keyin usul nimaga '
            'arziyotganini sanang: har bir tortishda hamon uchta natija bor, lekin endi '
            'har bir tanganing <em>ikkita</em> mumkin boʻlgan nuqsoni bor va bitta natijani '
            '"hech narsa notoʻgʻri emas" holatiga sarflash kerak.</p>'
            '<p class="lg-ask">Javob sifatida yozing: uch emas, <strong>toʻrt</strong> '
            'marta tortish mumkin boʻlsa, xuddi shu shartlar bilan — notoʻgʻri tangani '
            'topib, <em>ustiga</em> ogʻirmi yoki yengilmi deb ayta olgan holda — eng koʻpi '
            'bilan nechta tangani uddalar edingiz?</p>',

        'hint':    'Count the possible answers, not the coins. With n coins there are 2n '
                   'possible situations, and n weighings can tell apart 3ⁿ things — but '
                   'not every one of those outcomes is usable.',
        'hint_uz': 'Tangalarni emas, mumkin boʻlgan javoblarni sanang. n ta tanga uchun '
                   '2n xil holat bor, n marta tortish esa 3ⁿ narsani ajrata oladi — lekin '
                   'bu natijalarning hammasi ishga yaramaydi.',

        'answer_key': '39',
        'accepted': ['39 coins', '39 ta', '39 tanga', '(3^4-3)/2'],
        'answer_hint':    'a number',
        'answer_hint_uz': 'son',

        'solution':
            '<p>First, that three weighings really do settle twelve coins. Label them '
            '1-12 and weigh <strong>1,2,3,4 against 5,6,7,8</strong>.</p>'
            '<ol class="lg-steps">'
            '<li><strong>If they balance</strong>, the odd coin is among 9-12 and you have '
            'eight coins you know are genuine. Weigh <strong>9,10,11 against three genuine '
            'coins</strong>: if it balances, coin 12 is the odd one (weigh it against a '
            'genuine coin to learn heavy or light); if it tips, you know both the group of '
            'three <em>and</em> the direction, and one more weighing of 9 against 10 finds '
            'it.</li>'
            '<li><strong>If they tip</strong> — say the left side sinks — then either one '
            'of 1-4 is heavy or one of 5-8 is light. Eight suspects, each with a known '
            'direction. Now weigh <strong>1,2,5 against 3,4,6</strong>, mixing the two '
            'groups deliberately. Whichever way this goes, only two or three suspects '
            'survive, and the third weighing separates them.</li>'
            '<li>So twelve coins, three weighings, direction included. Now count why '
            'twelve is the limit.</li>'
            '<li>With <strong>n</strong> coins there are <strong>2n</strong> possible '
            'answers: any coin could be the odd one, heavy or light. Three weighings give '
            '3 × 3 × 3 = <strong>27</strong> distinguishable outcomes.</li>'
            '<li>But three of those outcomes are unusable: if every weighing balances you '
            'learn nothing, and the balance can never distinguish "all coins genuine" '
            'cases. The usable count is <strong>27 − 3 = 24</strong>, and 2n ≤ 24 gives '
            '<strong>n ≤ 12</strong>. Exactly twelve — the puzzle is tight to the '
            'bone.</li>'
            '<li>For four weighings: (3⁴ − 3) / 2 = (81 − 3) / 2 = '
            '<strong>39 coins</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> counting <em>answers</em> '
            'instead of trying arrangements. Before you invent a method, ask how much '
            'information you need (2n possibilities) and how much your tool can supply '
            '(3ⁿ outcomes). That comparison tells you whether to keep looking for a '
            'method or to stop and prove it is impossible — and it is the founding idea '
            'of information theory.</p>',

        'solution_uz':
            '<p>Avval uch marta tortish oʻn ikki tangani haqiqatan hal qilishini '
            'koʻrsatamiz. Ularni 1-12 deb raqamlab, <strong>1,2,3,4 ni 5,6,7,8 ga</strong> '
            'qarshi torting.</p>'
            '<ol class="lg-steps">'
            '<li><strong>Teng kelsa</strong>, notoʻgʻri tanga 9-12 orasida va sizda '
            'haqiqiyligi maʼlum sakkizta tanga bor. <strong>9,10,11 ni uchta haqiqiy '
            'tangaga</strong> qarshi torting: teng kelsa — 12-tanga notoʻgʻri (uni haqiqiy '
            'tangaga qarshi tortib, ogʻir yoki yengilligini bilasiz); ogʻsa — uchlik ham, '
            'yoʻnalish ham maʼlum, 9 ni 10 ga qarshi tortish esa aniqlab beradi.</li>'
            '<li><strong>Ogʻsa</strong> — masalan chap tomon pastga tushsa — demak yo '
            '1-4 dan biri ogʻir, yo 5-8 dan biri yengil. Sakkiz gumondor, har birining '
            'yoʻnalishi maʼlum. Endi ikki guruhni ataylab aralashtirib, <strong>1,2,5 ni '
            '3,4,6 ga</strong> qarshi torting. Qaysi tomonga ogʻishidan qatʼi nazar, '
            'faqat ikki-uchta gumondor qoladi va uchinchi tortish ularni ajratadi.</li>'
            '<li>Demak oʻn ikki tanga, uch tortish, yoʻnalishi bilan. Endi nega aynan oʻn '
            'ikki ekanini sanaymiz.</li>'
            '<li><strong>n</strong> ta tanga uchun <strong>2n</strong> xil javob bor: '
            'istalgan tanga notoʻgʻri boʻlishi, hamda ogʻir yoki yengil boʻlishi mumkin. '
            'Uch tortish 3 × 3 × 3 = <strong>27</strong> xil natija beradi.</li>'
            '<li>Ammo shu natijalardan uchtasi ishga yaramaydi: hamma tortish teng kelsa, '
            'siz hech narsa bilmaysiz. Foydali natijalar soni <strong>27 − 3 = 24</strong>, '
            '2n ≤ 24 dan esa <strong>n ≤ 12</strong>. Aynan oʻn ikki — jumboq soʻnggi '
            'tomchisigacha zich.</li>'
            '<li>Toʻrt tortish uchun: (3⁴ − 3) / 2 = (81 − 3) / 2 = '
            '<strong>39 ta tanga</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> variantlarni sinash oʻrniga '
            '<em>javoblarni</em> sanash. Usul oʻylab topishdan oldin soʻrang: menga qancha '
            'axborot kerak (2n ta ehtimol) va qurolim qancha bera oladi (3ⁿ ta natija)? '
            'Shu taqqoslash usulni izlashda davom etish kerakmi yoki toʻxtab, imkonsizligini '
            'isbotlash kerakmi — buni aytib beradi. Bu axborot nazariyasining asosiy '
            'gʻoyasi.</p>',
    },

    {
        'number': 12, 'round': 6, 'category': 'numbers', 'difficulty': 4,
        'title':    'The Three Daughters',
        'title_uz': 'Uch qiz',
        'teaser':    'Multiply to 36, add to the gate number — and it still is not enough.',
        'teaser_uz': 'Koʻpaytmasi 36, yigʻindisi darvoza raqami — shunda ham yetmaydi.',

        'body':
            '<p>Two old friends meet in the street after many years.</p>'
            '<p>"I have three daughters," says the first. "Multiply their ages together '
            'and you get <strong>36</strong>."</p>'
            '<p>"That is not enough," says the second.</p>'
            '<p>"Add their ages together," says the first, "and you get '
            '<strong>the number on that gate over there</strong>."</p>'
            '<p>The second friend looks at the gate, thinks for a while, and says: '
            '<strong>"That is still not enough."</strong></p>'
            '<p>"Ah, of course," says the first. "<strong>My eldest daughter plays the '
            'dutar.</strong>"</p>'
            '<p>"Now I know," says the second — and he is right.</p>'
            + '<div class="lg-rule"><span class="lg-rule__glyph">🔎</span>'
              '<span>Every sentence in this story carries information — including the two '
              'where somebody says they do <em>not</em> know something. Ages are whole '
              'numbers.</span></div>'
            + '<p class="lg-ask">Answer to type: the <strong>age of the eldest '
            'daughter</strong>.</p>',

        'body_uz':
            '<p>Ikki eski doʻst koʻp yillardan keyin koʻchada uchrashib qoladi.</p>'
            '<p>— Mening uchta qizim bor, — deydi birinchisi. — Yoshlarini koʻpaytirsang, '
            '<strong>36</strong> chiqadi.</p>'
            '<p>— Bu yetarli emas, — deydi ikkinchisi.</p>'
            '<p>— Yoshlarini qoʻshsang, — deydi birinchisi, — <strong>ana u darvozadagi '
            'raqam</strong> chiqadi.</p>'
            '<p>Ikkinchi doʻst darvozaga qaraydi, bir oz oʻylanadi va: '
            '<strong>— Bu ham yetarli emas</strong>, — deydi.</p>'
            '<p>— Ha, albatta, — deydi birinchisi. — <strong>Katta qizim dutor '
            'chaladi.</strong></p>'
            '<p>— Endi bildim, — deydi ikkinchisi. Va u haq.</p>'
            + '<div class="lg-rule"><span class="lg-rule__glyph">🔎</span>'
              '<span>Bu hikoyadagi har bir gap axborot tashiydi — jumladan kimdir '
              'bir narsani <em>bilmasligini</em> aytgan ikki gap ham. Yoshlar — butun '
              'sonlar.</span></div>'
            + '<p class="lg-ask">Javob sifatida yozing: <strong>katta qizning '
            'yoshi</strong>.</p>',

        'hint':    'Write out every triple of whole numbers whose product is 36, and put '
                   'their sums beside them. Then ask: why would knowing the sum not be '
                   'enough?',
        'hint_uz': 'Koʻpaytmasi 36 boʻlgan barcha butun sonlar uchligini yozib chiqing va '
                   'yoniga yigʻindisini qoʻying. Keyin soʻrang: yigʻindini bilish nega '
                   'yetarli boʻlmaydi?',

        'answer_key': '9',
        'accepted': ['9 years', '9 yosh', 'nine', 'toʻqqiz', '2,2,9', '2 2 9', '9,2,2',
                     '9 2 2', '2-2-9'],
        'answer_hint':    'an age (a number)',
        'answer_hint_uz': 'yosh (son)',

        'solution':
            '<p>Every triple of whole numbers multiplying to 36, with its sum:</p>'
            '<ul>'
            '<li>1, 1, 36 → 38</li><li>1, 2, 18 → 21</li><li>1, 3, 12 → 16</li>'
            '<li>1, 4, 9 → 14</li><li>1, 6, 6 → <strong>13</strong></li>'
            '<li>2, 2, 9 → <strong>13</strong></li><li>2, 3, 6 → 11</li>'
            '<li>3, 3, 4 → 10</li>'
            '</ul>'
            '<ol class="lg-steps">'
            '<li>The second friend can <em>see</em> the gate, so he knows the sum. If the '
            'sum had been 14, or 21, or any of the others, it would have appeared exactly '
            'once in the list and he would have known the ages at once.</li>'
            '<li>He says it is <strong>still not enough</strong>. That sentence is the key '
            'to the whole puzzle: the sum he is looking at must be one that appears '
            '<strong>twice</strong>. Only <strong>13</strong> does — so the ages are '
            'either 1, 6, 6 or 2, 2, 9.</li>'
            '<li>Then the father says "my <strong>eldest</strong> daughter". For 1, 6, 6 '
            'there is no single eldest — there are two six-year-olds. So that possibility '
            'is out.</li>'
            '<li>The ages are <strong>2, 2 and 9</strong>, and the eldest is '
            '<strong>9</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> "I do not know" is a fact, '
            'and a very sharp one. It rules out every case in which the person <em>would</em> '
            'have known. Learning to squeeze information out of somebody\'s ignorance — '
            'not just out of what they state — is what separates this puzzle from an '
            'ordinary equation.</p>',

        'solution_uz':
            '<p>Koʻpaytmasi 36 boʻlgan barcha butun sonlar uchligi va yigʻindisi:</p>'
            '<ul>'
            '<li>1, 1, 36 → 38</li><li>1, 2, 18 → 21</li><li>1, 3, 12 → 16</li>'
            '<li>1, 4, 9 → 14</li><li>1, 6, 6 → <strong>13</strong></li>'
            '<li>2, 2, 9 → <strong>13</strong></li><li>2, 3, 6 → 11</li>'
            '<li>3, 3, 4 → 10</li>'
            '</ul>'
            '<ol class="lg-steps">'
            '<li>Ikkinchi doʻst darvozani <em>koʻrib turibdi</em>, demak yigʻindini biladi. '
            'Agar yigʻindi 14 yoki 21 yoki boshqasi boʻlganida, u roʻyxatda bir marta '
            'uchrardi va doʻst yoshlarni darrov bilib olardi.</li>'
            '<li>U esa <strong>hamon yetarli emas</strong> deydi. Butun jumboqning kaliti '
            'shu gapda: u qarab turgan yigʻindi roʻyxatda <strong>ikki marta</strong> '
            'uchraydigan son boʻlishi shart. Faqat <strong>13</strong> shunday — demak '
            'yoshlar yo 1, 6, 6 yoki 2, 2, 9.</li>'
            '<li>Keyin ota "<strong>katta</strong> qizim" deydi. 1, 6, 6 da yagona katta '
            'qiz yoʻq — ikkita olti yoshli bor. Demak bu variant chiqib ketadi.</li>'
            '<li>Yoshlar — <strong>2, 2 va 9</strong>, kattasi esa '
            '<strong>9</strong> yoshda.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> "bilmayman" — bu ham dalil, '
            'juda oʻtkir dalil. U odam <em>bilishi mumkin boʻlgan</em> barcha holatlarni '
            'inkor qiladi. Aytilganidan emas, bilmasligidan axborot siqib chiqarishni '
            'oʻrganish — bu jumboqni oddiy tenglamadan ajratib turadigan narsa.</p>',
    },

    # ── Round 7 ─────────────────────────────────────────────────────────────
    {
        'number': 13, 'round': 7, 'category': 'numbers', 'difficulty': 3,
        'title':    'The Missing Thousand',
        'title_uz': 'Yoʻqolgan ming soʻm',
        'teaser':    'Three friends, one hotel bill, and a thousand som that is not there.',
        'teaser_uz': 'Uch doʻst, bitta mehmonxona hisobi va yoʻq boʻlgan ming soʻm.',

        'body':
            '<p>Three friends take a room. The receptionist asks for '
            '<strong>30 000 som</strong>, so each of them puts in '
            '<strong>10 000</strong>.</p>'
            '<p>Later the manager notices the room is only <strong>25 000</strong> that '
            'night, and sends a porter up with <strong>5 000 som</strong>.</p>'
            '<p>On the stairs the porter thinks: five thousand does not divide evenly by '
            'three. So he gives each friend <strong>1 000 som</strong> back and quietly '
            'keeps <strong>2 000</strong> for himself.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🧮</span><span>'
            'Now the trap. Each friend paid 10 000 and got 1 000 back, so each paid '
            '<strong>9 000</strong>. Three times 9 000 is <strong>27 000</strong>. '
            'The porter has <strong>2 000</strong>. And 27 000 + 2 000 = '
            '<strong>29 000</strong> — but they started with 30 000. '
            '<strong>Where is the missing 1 000 som?</strong></span></div>'
            '<p>There is no missing money, of course. The sum above adds two numbers that '
            'must never be added together. Find the false step — and then prove you have '
            'found it by following the money properly.</p>'
            '<p class="lg-ask">Answer to type: of the 27 000 som the friends actually '
            'paid, how many som ended up <strong>in the hotel\'s till</strong>?</p>',

        'body_uz':
            '<p>Uch doʻst xona oladi. Administrator <strong>30 000 soʻm</strong> soʻraydi, '
            'shuning uchun har biri <strong>10 000</strong> dan qoʻshadi.</p>'
            '<p>Keyinroq menejer oʻsha kecha xona atigi <strong>25 000</strong> turishini '
            'payqaydi va koridorbon bilan <strong>5 000 soʻm</strong> joʻnatadi.</p>'
            '<p>Zinada koridorbon oʻylaydi: besh ming uchga bir tekis boʻlinmaydi. Shuning '
            'uchun u har bir doʻstga <strong>1 000 soʻm</strong> qaytaradi va indamay '
            '<strong>2 000</strong> ni oʻziga oladi.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🧮</span><span>'
            'Endi tuzoq. Har bir doʻst 10 000 toʻlab, 1 000 qaytarib oldi, demak har biri '
            '<strong>9 000</strong> toʻladi. Uch marta 9 000 — <strong>27 000</strong>. '
            'Koridorbonda <strong>2 000</strong>. 27 000 + 2 000 = '
            '<strong>29 000</strong> — holbuki ular 30 000 dan boshlagan edi. '
            '<strong>Yoʻqolgan 1 000 soʻm qayerda?</strong></span></div>'
            '<p>Albatta, hech qanday pul yoʻqolgani yoʻq. Yuqoridagi hisob hech qachon '
            'qoʻshilmasligi kerak boʻlgan ikki sonni qoʻshmoqda. Xato qadamni toping — '
            'va pulni toʻgʻri kuzatib, topganingizni isbotlang.</p>'
            '<p class="lg-ask">Javob sifatida yozing: doʻstlar haqiqatda toʻlagan '
            '27 000 soʻmdan qanchasi <strong>mehmonxona kassasiga</strong> tushdi?</p>',

        'hint':    'Ask what the 27 000 is made of. Does the porter\'s 2 000 sit inside '
                   'it, or outside it?',
        'hint_uz': '27 000 nimalardan tashkil topganini soʻrang. Koridorbondagi 2 000 '
                   'uning ichidami yoki tashqarisidami?',

        'answer_key': '25000',
        'accepted': ['25 000', '25000 som', '25 000 som', "25 000 so'm", '25000 soʻm',
                     '25 ming', '25000som'],
        'answer_hint':    'an amount in som',
        'answer_hint_uz': 'soʻmdagi miqdor',

        'solution':
            '<ol class="lg-steps">'
            '<li>Follow the money instead of the story. Thirty thousand som left the '
            'friends\' pockets and went to exactly three places: '
            '<strong>25 000</strong> to the hotel, <strong>2 000</strong> to the porter, '
            'and <strong>3 000</strong> back into the friends\' hands. '
            '25 000 + 2 000 + 3 000 = <strong>30 000</strong>. Nothing is missing.</li>'
            '<li>Now the false step. The 27 000 the friends paid is what left them '
            '<em>for good</em> — and it is made of the hotel\'s 25 000 '
            '<strong>plus the porter\'s 2 000</strong>, which is already inside it.</li>'
            '<li>So adding the porter\'s 2 000 to the 27 000 counts his money '
            '<strong>twice</strong>. That is the whole trick — the sum 27 000 + 2 000 is '
            'meaningless, and it lands one thousand short of 30 000 purely by '
            'coincidence.</li>'
            '<li>The correct sentence is <strong>27 000 − 2 000 = 25 000</strong>: what '
            'the friends paid, minus what the porter kept, is what the hotel got. '
            '<strong>The answer is 25 000 som.</strong></li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> money paid and money received '
            'are two directions, and you can only add numbers pointing the same way. The '
            'puzzle works on almost everybody because it asks its question so confidently '
            'that you start hunting for the thousand instead of asking whether the '
            'question makes sense. When an argument produces something impossible, suspect '
            'the question before you suspect the arithmetic.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Hikoyani emas, pulni kuzating. Doʻstlarning choʻntagidan chiqqan '
            'oʻttiz ming soʻm aniq uchta joyga bordi: mehmonxonaga '
            '<strong>25 000</strong>, koridorbonga <strong>2 000</strong> va doʻstlarning '
            'oʻz qoʻliga qaytib <strong>3 000</strong>. '
            '25 000 + 2 000 + 3 000 = <strong>30 000</strong>. Hech narsa yoʻqolgani '
            'yoʻq.</li>'
            '<li>Endi xato qadam. Doʻstlar toʻlagan 27 000 — bu ulardan '
            '<em>butunlay</em> chiqib ketgan pul, va u mehmonxonaning 25 000 i '
            '<strong>ustiga koridorbonning 2 000 i</strong>dan iborat; oʻsha 2 000 allaqachon '
            'uning ichida.</li>'
            '<li>Demak koridorbonning 2 000 ini 27 000 ga qoʻshish uning pulini '
            '<strong>ikki marta</strong> sanaydi. Butun hiyla shu — 27 000 + 2 000 degan '
            'yigʻindining maʼnosi yoʻq va uning 30 000 dan mingga kam chiqishi shunchaki '
            'tasodif.</li>'
            '<li>Toʻgʻri gap: <strong>27 000 − 2 000 = 25 000</strong> — doʻstlar '
            'toʻlagan puldan koridorbon olib qolgani ayirilsa, mehmonxona olgani chiqadi. '
            '<strong>Javob: 25 000 soʻm.</strong></li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> toʻlangan pul va olingan pul — '
            'ikki yoʻnalish, siz esa faqat bir tomonga qaragan sonlarni qoʻsha olasiz. Bu '
            'jumboq deyarli hammani chalgʻitadi, chunki savolini shunday ishonch bilan '
            'beradiki, siz savolning oʻzi maʼnolimi deb soʻrash oʻrniga oʻsha mingni '
            'qidirib ketasiz. Mulohaza imkonsiz natija bersa, arifmetikadan oldin '
            'savolning oʻzidan shubhalaning.</p>',
    },

    {
        'number': 14, 'round': 7, 'category': 'chance', 'difficulty': 4,
        'title':    'Three Doors',
        'title_uz': 'Uch eshik',
        'teaser':    'A car, two goats, and the most argued-about question in probability.',
        'teaser_uz': 'Bitta mashina, ikkita echki va ehtimollikdagi eng koʻp bahs '
                     'qilingan savol.',

        'body':
            '<p>A television game. There are <strong>three closed doors</strong>. Behind '
            'one of them is a <strong>car</strong>; behind each of the other two is a '
            '<strong>goat</strong>. You pick a door — say door 1 — but it stays shut.</p>'
            '<p>The presenter <strong>knows where the car is</strong>. He opens one of the '
            'two doors you did not pick — always one with a goat behind it, always a door '
            'you did not choose — and shows you the goat.</p>'
            + fig(row(['🚪', '🐐', '🚪'], ['your door', 'opened', 'the third door'],
                      box=True),
                  'The presenter never opens your door, and never opens the car.')
            + '<p>Then he offers: <strong>stay with your door, or switch to the other '
            'closed one?</strong></p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🎲</span>'
            '<span>Nearly everybody says it makes no difference — two doors left, so it '
            'must be fifty-fifty. That answer is wrong, and the reason is worth more than '
            'the puzzle.</span></div>'
            '<p class="lg-ask">Answer to type: if you play this game <strong>300 '
            'times</strong> and <strong>always switch</strong>, how many cars do you win '
            'on average?</p>',

        'body_uz':
            '<p>Televizion oʻyin. <strong>Uchta yopiq eshik</strong> bor. Bittasining '
            'orqasida <strong>mashina</strong>, qolgan ikkitasining orqasida '
            '<strong>echki</strong>. Siz bitta eshikni tanlaysiz — masalan, 1-eshikni — '
            'lekin u yopiq qoladi.</p>'
            '<p>Boshlovchi <strong>mashina qayerdaligini biladi</strong>. U siz '
            'tanlamagan ikki eshikdan bittasini ochadi — har doim orqasida echki '
            'boʻlganini, har doim siz tanlamaganini — va echkini koʻrsatadi.</p>'
            + fig(row(['🚪', '🐐', '🚪'], ['sizning eshigingiz', 'ochildi', 'uchinchi eshik'],
                      box=True),
                  'Boshlovchi hech qachon sizning eshigingizni ham, mashinani ham '
                  'ochmaydi.')
            + '<p>Keyin taklif qiladi: <strong>oʻz eshigingizda qolasizmi yoki '
            'ikkinchi yopiq eshikka almashasizmi?</strong></p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🎲</span>'
            '<span>Deyarli hamma "farqi yoʻq" deydi — ikki eshik qoldi, demak ellikka '
            'ellik. Bu javob notoʻgʻri va sababi jumboqning oʻzidan qimmatroq.</span></div>'
            '<p class="lg-ask">Javob sifatida yozing: bu oʻyinni <strong>300 marta</strong> '
            'oʻynab, <strong>har safar almashsangiz</strong>, oʻrtacha nechta mashina '
            'yutasiz?</p>',

        'hint':    'Forget the doors for a moment and ask a simpler question: how often is '
                   'your very first pick the car? Switching wins in exactly the opposite '
                   'cases.',
        'hint_uz': 'Bir lahza eshiklarni unuting va soddaroq savol bering: birinchi '
                   'tanlovingiz qanchalik tez-tez mashina boʻladi? Almashish esa aynan '
                   'qarama-qarshi holatlarda yutadi.',

        'answer_key': '200',
        'accepted': ['200 cars', '200 ta', '200 marta', '2/3', 'ikki yuz'],
        'answer_hint':    'a number out of 300',
        'answer_hint_uz': '300 tadan nechta (son)',

        'solution':
            '<ol class="lg-steps">'
            '<li>When you first pick a door, you have <strong>1 chance in 3</strong> of '
            'pointing at the car. Nothing the presenter does afterwards can change what '
            'already happened — your door was, and stays, a 1-in-3 door.</li>'
            '<li>So <strong>2 times in 3</strong>, the car is behind one of the other two '
            'doors.</li>'
            '<li>The presenter then removes one of those two — and he never removes the '
            'car, because he knows where it is. All of that 2-in-3 chance therefore piles '
            'up on the <strong>single remaining closed door</strong>.</li>'
            '<li>Switching wins exactly when your first pick was wrong, which is 2 times '
            'in 3. Staying wins only when your first pick was right: 1 time in 3.</li>'
            '<li>Over 300 games, always switching wins '
            '<strong>300 × 2/3 = 200 cars</strong> — against 100 for always '
            'staying.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> the presenter is not a random '
            'event, he is an informed one. Because he would never open the car, opening a '
            'goat tells you something real about the door he left shut. Test it with three '
            'coins and a friend: switch twenty times and count. And notice what makes it '
            'click — imagine <strong>100 doors</strong>, you pick one, and he opens 98 '
            'goats. Would you still stay?</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Birinchi eshikni tanlaganingizda mashinani koʻrsatish ehtimoli '
            '<strong>3 tadan 1</strong>. Boshlovchining keyingi harakati allaqachon '
            'boʻlib oʻtgan narsani oʻzgartira olmaydi — sizning eshigingiz "3 dan 1" '
            'eshigi boʻlgan va shunday qoladi.</li>'
            '<li>Demak <strong>3 tadan 2 holatda</strong> mashina qolgan ikki eshikning '
            'orqasida.</li>'
            '<li>Keyin boshlovchi oʻsha ikkitadan bittasini olib tashlaydi — va hech '
            'qachon mashinani ochmaydi, chunki qayerdaligini biladi. Shu "3 dan 2" '
            'ehtimolning hammasi <strong>yolgʻiz qolgan yopiq eshikka</strong> '
            'toʻplanadi.</li>'
            '<li>Almashish aynan birinchi tanlovingiz notoʻgʻri boʻlganda yutadi — bu '
            '3 tadan 2 holat. Qolish esa faqat birinchi tanlov toʻgʻri boʻlganda: '
            '3 tadan 1.</li>'
            '<li>300 oʻyinda har safar almashish '
            '<strong>300 × 2/3 = 200 ta mashina</strong> yutadi — har safar qolish esa '
            'atigi 100 ta.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> boshlovchi tasodifiy hodisa '
            'emas, u <em>biladigan</em> hodisa. U hech qachon mashinani ochmagani uchun, '
            'echkini ochishi yopiq qoldirgan eshik haqida haqiqiy axborot beradi. Uch '
            'tanga va bitta doʻst bilan tekshiring: yigirma marta almashib, sanang. Va '
            'nima uni tushunarli qilishiga eʼtibor bering — <strong>100 ta eshik</strong>ni '
            'tasavvur qiling, siz bittasini tanladingiz, u 98 ta echkini ochdi. Hamon '
            'oʻzingiznikida qolasizmi?</p>',
    },

    # ── Round 8 ─────────────────────────────────────────────────────────────
    {
        'number': 15, 'round': 8, 'category': 'strategy', 'difficulty': 3,
        'title':    'The Dark Room Drawer',
        'title_uz': 'Qorongʻi xonadagi tortma',
        'teaser':    'Thirty socks, three colours, no light. Guarantee a black pair.',
        'teaser_uz': 'Oʻttiz paypoq, uch rang, yorugʻlik yoʻq. Qora juftni kafolatlang.',

        'body':
            '<p>A drawer holds <strong>30 socks</strong>, jumbled together:</p>'
            '<ul>'
            '<li><strong>10 black</strong> socks,</li>'
            '<li><strong>12 white</strong> socks,</li>'
            '<li><strong>8 grey</strong> socks.</li>'
            '</ul>'
            '<p>The power is out and the room is completely dark. You cannot tell the '
            'colours apart by touch, and once a sock is out of the drawer you may not put '
            'it back.</p>'
            + fig(row(['🧦', '🧦', '🧦'], ['10 black', '12 white', '8 grey'], box=True),
                  'All the same to the hand. Only the count is on your side.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🌑</span>'
              '<span>You need <strong>two black socks</strong> — and you must be '
              '<em>certain</em>, not lucky. Assume the worst possible order of '
              'draws.</span></div>'
            '<p class="lg-ask">Answer to type: the <strong>smallest number of socks</strong> '
            'you must take out to be sure of holding two black ones.</p>',

        'body_uz':
            '<p>Tortmada <strong>30 ta paypoq</strong> aralash yotibdi:</p>'
            '<ul>'
            '<li><strong>10 ta qora</strong>,</li>'
            '<li><strong>12 ta oq</strong>,</li>'
            '<li><strong>8 ta kulrang</strong>.</li>'
            '</ul>'
            '<p>Chiroq oʻchgan, xona zim-ziyo. Ranglarni paypaslab ajratib boʻlmaydi va '
            'tortmadan chiqqan paypoqni qaytarib solish mumkin emas.</p>'
            + fig(row(['🧦', '🧦', '🧦'], ['10 qora', '12 oq', '8 kulrang'], box=True),
                  'Qoʻlga hammasi bir xil. Sizning tomoningizda faqat sanoq bor.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🌑</span>'
              '<span>Sizga <strong>ikkita qora paypoq</strong> kerak — va omad bilan emas, '
              '<em>aniq ishonch</em> bilan. Eng yomon tartibni faraz qiling.</span></div>'
            '<p class="lg-ask">Javob sifatida yozing: ikkita qora paypoq qoʻlingizda '
            'boʻlishiga ishonch hosil qilish uchun olish kerak boʻlgan '
            '<strong>eng kam paypoqlar soni</strong>.</p>',

        'hint':    'Do not ask what is likely. Ask what the unluckiest possible hand looks '
                   'like — and then take one more sock than that.',
        'hint_uz': 'Nima ehtimolliroq deb soʻramang. Eng omadsiz holat qanday boʻlishini '
                   'soʻrang — va oʻshandan bitta koʻproq oling.',

        'answer_key': '22',
        'accepted': ['22 socks', '22 ta', '22 paypoq', 'twenty two', 'yigirma ikki'],
        'answer_hint':    'a number of socks',
        'answer_hint_uz': 'necha paypoq (son)',

        'solution':
            '<ol class="lg-steps">'
            '<li>Certainty means planning for the worst hand the drawer could possibly '
            'deal you — not the likely one.</li>'
            '<li>The worst case is that you pull out <strong>every single white sock</strong> '
            'first (12), then <strong>every single grey sock</strong> (8). That is 20 socks '
            'and not one of them is black. Unlikely, but perfectly possible.</li>'
            '<li>Now the drawer contains nothing but black socks. The next sock is black, '
            'and the one after it is black too.</li>'
            '<li>So <strong>12 + 8 + 2 = 22 socks</strong> guarantee a black pair. With 21 '
            'you could still be holding just one black sock, so 22 is genuinely the '
            'smallest number.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> notice how little the black '
            'socks matter — the answer barely depends on there being ten of them. When a '
            'puzzle says <em>guarantee</em> or <em>be certain</em>, stop thinking about '
            'chances and start playing against an opponent who hands you the worst sock '
            'every time. Incidentally, a mere <strong>4 socks</strong> guarantee a matching '
            'pair of <em>some</em> colour — three colours, four socks, so two must '
            'match.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Ishonch degani — tortma sizga bera oladigan eng yomon holatni hisobga '
            'olish, ehtimolligini emas.</li>'
            '<li>Eng yomon holat: avval <strong>hamma oq paypoqni</strong> tortib '
            'olasiz (12 ta), keyin <strong>hamma kulrangni</strong> (8 ta). Bu 20 ta '
            'paypoq va bittasi ham qora emas. Ehtimoli kam, lekin mumkin.</li>'
            '<li>Endi tortmada faqat qora paypoqlar qoldi. Keyingi paypoq qora, undan '
            'keyingisi ham qora.</li>'
            '<li>Demak <strong>12 + 8 + 2 = 22 ta paypoq</strong> qora juftni kafolatlaydi. '
            '21 tada hamon bitta qora paypoq bilan qolishingiz mumkin, shuning uchun 22 '
            'haqiqatan ham eng kichik son.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> qora paypoqlar javobga deyarli '
            'taʼsir qilmasligiga eʼtibor bering — ularning oʻntaligi zoʻrgʻa ahamiyatli. '
            'Jumboqda <em>kafolatlang</em> yoki <em>ishonch hosil qiling</em> deyilsa, '
            'ehtimol haqida oʻylashni bas qiling va sizga har safar eng yomon paypoqni '
            'uzatadigan raqib bilan oʻynang. Aytgancha, <em>istalgan</em> rangdagi juftni '
            'olish uchun atigi <strong>4 ta paypoq</strong> yetadi — uch rang, toʻrt '
            'paypoq, demak ikkitasi albatta mos keladi.</p>',
    },

    {
        'number': 16, 'round': 8, 'category': 'weighing', 'difficulty': 4,
        'title':    'Four Weights for the Bazaar',
        'title_uz': 'Bozor uchun toʻrtta tosh',
        'teaser':    'A balance, four weights, and every whole number of kilos to weigh.',
        'teaser_uz': 'Bitta tarozi, toʻrtta tosh va har qanday butun kilogramm.',

        'body':
            '<p>A trader at Chorsu bazaar has an old <strong>two-pan balance</strong> and '
            'wants to buy a set of <strong>four weights</strong>, so that he can weigh out '
            '<strong>any whole number of kilograms</strong>, starting from 1 kg, with no '
            'gaps.</p>'
            '<p>The clever part: on a two-pan balance a weight may be placed '
            '<strong>on either pan</strong>. Put a weight next to the goods and it '
            '<em>subtracts</em>; put it on the far pan and it <em>adds</em>. With a 1 kg '
            'and a 3 kg weight he can already do 2 kg: goods + 1 on one side, 3 on the '
            'other.</p>'
            + fig(balance('goods + 1', '3', tilt=0, caption_left='the load pan',
                          caption_right='the weights pan'),
                  '3 − 1 = 2. A weight beside the goods works backwards.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⚖️</span>'
              '<span>Exactly <strong>four</strong> weights, each a whole number of kilos. '
              'Every whole weight from 1 kg upwards must be measurable — no gaps '
              'anywhere.</span></div>'
            '<p>Find the four weights first. Then answer this:</p>'
            '<p class="lg-ask">Answer to type: the <strong>heaviest load, in kilograms</strong>, '
            'that the best set of four weights can measure.</p>',

        'body_uz':
            '<p>Chorsu bozoridagi savdogarda eski <strong>ikki pallali tarozi</strong> bor '
            'va u <strong>toʻrtta tosh</strong> sotib olmoqchi — 1 kg dan boshlab '
            '<strong>har qanday butun kilogrammni</strong>, hech qanday uzilishsiz '
            'tortadigan qilib.</p>'
            '<p>Eng qiziq joyi: ikki pallali tarozida toshni <strong>istalgan pallaga</strong> '
            'qoʻyish mumkin. Toshni mol yoniga qoʻysangiz u <em>ayiriladi</em>; narigi '
            'pallaga qoʻysangiz <em>qoʻshiladi</em>. 1 kg va 3 kg tosh bilan u allaqachon '
            '2 kg ni tortadi: bir tomonda mol + 1, ikkinchi tomonda 3.</p>'
            + fig(balance('mol + 1', '3', tilt=0, caption_left='mol pallasi',
                          caption_right='tosh pallasi'),
                  '3 − 1 = 2. Mol yonidagi tosh teskari ishlaydi.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⚖️</span>'
              '<span>Aniq <strong>toʻrtta</strong> tosh, har biri butun kilogramm. 1 kg dan '
              'yuqoriga qarab har bir butun ogʻirlikni oʻlchash mumkin boʻlishi kerak — '
              'hech qayerda uzilish boʻlmasin.</span></div>'
            '<p>Avval toʻrt toshni toping. Keyin shunga javob bering:</p>'
            '<p class="lg-ask">Javob sifatida yozing: eng yaxshi toʻrtlik oʻlchay '
            'oladigan <strong>eng ogʻir yuk, kilogrammda</strong>.</p>',

        'hint':    'Each weight can be on the far pan (+), beside the goods (−), or left '
                   'in the box (0). Three choices per weight — where have you seen that '
                   'before?',
        'hint_uz': 'Har bir tosh narigi pallada (+), mol yonida (−) yoki qutida (0) '
                   'boʻlishi mumkin. Har toshga uchta variant — buni qayerda '
                   'koʻrgansiz?',

        'answer_key': '40',
        'accepted': ['40 kg', '40kg', '40 kilo', 'qirq'],
        'answer_hint':    'a number of kilograms',
        'answer_hint_uz': 'necha kilogramm (son)',

        'solution':
            '<ol class="lg-steps">'
            '<li>Every weight has <strong>three</strong> possible roles: on the far pan '
            '(counts as +), beside the goods (counts as −), or not used at all (0). That '
            'is the same three-way choice as puzzle #1 — powers of three again.</li>'
            '<li>Four weights therefore give 3 × 3 × 3 × 3 = <strong>81</strong> '
            'combinations. One of them is "all weights in the box" (zero), and the other '
            '80 split into 40 positive values and their 40 negatives. So at most '
            '<strong>40</strong> different loads are measurable.</li>'
            '<li>The set that actually achieves it is <strong>1, 3, 9 and 27 kg</strong> — '
            'the powers of three.</li>'
            '<li>Check a few: 2 = 3 − 1. 5 = 9 − 3 − 1. 6 = 9 − 3. 11 = 9 + 3 − 1. '
            '20 = 27 − 9 + 3 − 1. 40 = 1 + 3 + 9 + 27. Every whole number from 1 to 40 '
            'appears exactly once, with no gaps and nothing wasted.</li>'
            '<li>So the heaviest measurable load is <strong>40 kg</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> this is counting in base '
            'three — but a strange base three, where the digits are +1, 0 and −1 instead '
            'of 0, 1 and 2. Ordinary weights of 1, 2, 4, 8 kg (powers of two) only reach '
            '15 kg, because they can only ever be added. Being allowed to '
            '<em>subtract</em> is what upgrades you from powers of two to powers of three '
            '— the same jump the balance gave you in the very first puzzle of this '
            'season.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Har bir toshning <strong>uchta</strong> mumkin boʻlgan roli bor: narigi '
            'pallada (+), mol yonida (−) yoki umuman ishlatilmaydi (0). Bu 1-jumboqdagi '
            'oʻsha uch tomonlama tanlov — yana uchning darajalari.</li>'
            '<li>Demak toʻrt tosh 3 × 3 × 3 × 3 = <strong>81</strong> xil birikma beradi. '
            'Bittasi — "hamma tosh qutida" (nol), qolgan 80 tasi esa 40 ta musbat qiymat '
            'va ularning 40 ta manfiyiga boʻlinadi. Demak koʻpi bilan <strong>40</strong> '
            'xil yukni oʻlchash mumkin.</li>'
            '<li>Buni haqiqatan uddalaydigan toʻplam — <strong>1, 3, 9 va 27 kg</strong>, '
            'yaʼni uchning darajalari.</li>'
            '<li>Bir nechtasini tekshiring: 2 = 3 − 1. 5 = 9 − 3 − 1. 6 = 9 − 3. '
            '11 = 9 + 3 − 1. 20 = 27 − 9 + 3 − 1. 40 = 1 + 3 + 9 + 27. 1 dan 40 gacha '
            'har bir butun son aynan bir marta chiqadi — uzilish ham, isrof ham '
            'yoʻq.</li>'
            '<li>Demak eng ogʻir oʻlchanadigan yuk — <strong>40 kg</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> bu — uchlik sanoq sistemasi, '
            'lekin gʻalati uchlik: raqamlari 0, 1, 2 emas, +1, 0 va −1. Oddiy 1, 2, 4, 8 kg '
            'toshlar (ikkining darajalari) atigi 15 kg gacha yetadi, chunki ular faqat '
            'qoʻshila oladi. <em>Ayirishga</em> ruxsat berilishi sizni ikkining '
            'darajalaridan uchning darajalariga koʻtaradi — bu mavsumning eng birinchi '
            'jumbogʻida tarozi bergan oʻsha sakrashning oʻzi.</p>',
    },
]
