"""Logic Arena — puzzles 25-32 (season 2, rounds 5-8).

The second half of season 2. Rounds 7 and 8 close the season with two ★★★★★
flagships: the hundred boxes (#30), whose answer nobody believes until they
see the loops, and the five merchants (#32), the caravanserai version of the
famous monkey-and-coconuts problem.

SCHEDULE is copied unchanged from `_puzzles_logic_17_24.py`: the two files
describe one season. Every answer key was recomputed independently by
`verify_logic_17_32.py` before import.
"""
from logic.figures import chain, fig, flatbread, rings, row

SCHEDULE = {
    'start':  '2026-10-05 09:00',
    'days':   7,
    'window': 7,
}


PUZZLES = [

    # ── Round 5 ─────────────────────────────────────────────────────────────
    {
        'number': 25, 'round': 5, 'category': 'cutting', 'difficulty': 3,
        'title':    'Five Cuts in a Non',
        'title_uz': 'Nonni besh marta kesish',
        'teaser':    'A round non, a long knife, five straight cuts. How many pieces at most?',
        'teaser_uz': 'Dumaloq non, uzun pichoq, besh marta toʻgʻri kesish. Koʻpi bilan necha boʻlak?',

        'body':
            '<p>Grandma puts a big round <strong>non</strong> on the dastarkhan and hands '
            'Sherbek a long knife. “Five cuts,” she says. “Straight ones, right across. Let us '
            'see how many pieces you can make.”</p>'
            '<p>Sherbek cuts through the middle five times, like the spokes of a wheel, and '
            'gets 10 pieces. Grandma smiles. “You can do much better.”</p>'
            + fig(flatbread([(90, 270), (150, 330), (210, 30)]),
                  'Three cuts through the centre give six pieces. There is a better way.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🔪</span>'
              '<span>Exactly <strong>five straight cuts</strong>, each from edge to edge. The '
              'non lies flat: no folding, no stacking, no moving pieces between '
              'cuts.</span></div>'
            '<p>The pieces do not have to be the same size — Grandma only wants as many as '
            'possible.</p>'
            '<p class="lg-ask">Answer to type: the <strong>largest number of pieces</strong> '
            'five cuts can make.</p>',

        'body_uz':
            '<p>Buvi dasturxonga katta dumaloq <strong>non</strong> qoʻyib, Sherbekka uzun '
            'pichoq tutqazadi. «Besh marta kes, — deydi u. — Toʻgʻri, bir chetidan ikkinchi '
            'chetigacha. Koʻraylik-chi, necha boʻlak qilarkansan.»</p>'
            '<p>Sherbek nonni gʻildirak kegaylaridek besh marta oʻrtasidan kesib, 10 boʻlak '
            'hosil qiladi. Buvi jilmayadi: «Bundan ancha yaxshiroq qilsa boʻladi.»</p>'
            + fig(flatbread([(90, 270), (150, 330), (210, 30)]),
                  'Markazdan uch marta kesish olti boʻlak beradi. Yaxshiroq yoʻli bor.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🔪</span>'
              '<span>Roppa-rosa <strong>besh marta toʻgʻri kesish</strong>, har biri chetdan '
              'chetga. Non tekis yotadi: buklash, ustma-ust qoʻyish yoki kesishlar orasida '
              'boʻlaklarni surish mumkin emas.</span></div>'
            '<p>Boʻlaklar bir xil boʻlishi shart emas — buvi faqat iloji boricha koʻp '
            'boʻlishini xohlaydi.</p>'
            '<p class="lg-ask">Javob sifatida yozing: besh marta kesish bilan hosil qilish '
            'mumkin boʻlgan <strong>eng koʻp boʻlaklar soni</strong>.</p>',

        'hint':    'Each new cut adds one piece, plus one more for every earlier cut it '
                   'crosses. So let it cross all of them — but not where two others already '
                   'meet.',
        'hint_uz': 'Har bir yangi kesish bitta boʻlak qoʻshadi, plyus u kesib oʻtgan har bir '
                   'oldingi kesish uchun yana bitta. Demak u hammasini kesib oʻtsin — lekin '
                   'ikkitasi allaqachon kesishgan joydan emas.',

        'answer_key': '16',
        'accepted': ['16 pieces', '16 ta', '16 boʻlak', '16 ta boʻlak', 'oʻn olti', "o'n olti",
                     'sixteen'],
        'answer_hint':    'a number of pieces',
        'answer_hint_uz': 'boʻlaklar soni',

        'solution':
            '<ol class="lg-steps">'
            '<li>Watch what one cut does. It runs across the non and splits every piece it '
            'passes through into two. So it adds as many pieces as the number of pieces it '
            'passes through.</li>'
            '<li>A cut that crosses <strong>k</strong> earlier cuts is broken by them into '
            '<strong>k + 1</strong> stretches, and each stretch splits one piece. So it adds '
            '<strong>k + 1</strong> pieces.</li>'
            '<li>To add the most, every new cut must cross every earlier one, at a fresh point '
            '(not through a place where two cuts already meet). Spokes through the centre '
            'waste this: they all cross at one point.</li>'
            '<li>Start with 1 piece. Cut 1 adds 1 → 2. Cut 2 adds 2 → 4. Cut 3 adds 3 → 7. '
            'Cut 4 adds 4 → 11. Cut 5 adds 5 → <strong>16</strong>.</li>'
            '<li>In general n cuts give 1 + (1 + 2 + … + n) = 1 + n(n + 1)/2 pieces — and a '
            'slightly tilted set of lines, no two parallel and no three through one point, '
            'achieves it.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> do not count the final picture — '
            'count what <em>each step adds</em>. A new line adds one more than the number of '
            'lines it crosses, so the totals grow 2, 4, 7, 11, 16. Building a count step by '
            'step like this is called a recurrence, and it is how you count almost anything '
            'that grows: handshakes, tournament games, the moves in a puzzle.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Bitta kesish nima qilishini kuzating. U nonni kesib oʻtib, yoʻlida uchragan '
            'har bir boʻlakni ikkiga ajratadi. Demak u oʻzi kesib oʻtgan boʻlaklar soniga '
            'teng boʻlak qoʻshadi.</li>'
            '<li><strong>k</strong> ta oldingi kesishni kesib oʻtgan kesish ular tomonidan '
            '<strong>k + 1</strong> ta qismga boʻlinadi va har bir qism bitta boʻlakni ajratadi. '
            'Demak u <strong>k + 1</strong> ta boʻlak qoʻshadi.</li>'
            '<li>Eng koʻp qoʻshish uchun har bir yangi kesish barcha oldingilarini yangi '
            'nuqtada kesib oʻtishi kerak (ikki kesish allaqachon uchrashgan joydan emas). '
            'Markazdan oʻtgan kegaylar buni behuda sarflaydi: ular hammasi bir nuqtada '
            'kesishadi.</li>'
            '<li>1 boʻlakdan boshlaymiz. 1-kesish 1 qoʻshadi → 2. 2-kesish 2 qoʻshadi → 4. '
            '3-kesish 3 qoʻshadi → 7. 4-kesish 4 qoʻshadi → 11. 5-kesish 5 qoʻshadi → '
            '<strong>16</strong>.</li>'
            '<li>Umuman, n ta kesish 1 + (1 + 2 + … + n) = 1 + n(n + 1)/2 ta boʻlak beradi — va '
            'hech ikkitasi parallel boʻlmagan, hech uchtasi bir nuqtadan oʻtmaydigan biroz '
            'qiyshiq chiziqlar bunga erishadi.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> oxirgi rasmni sanamang — <em>har bir '
            'qadam nima qoʻshishini</em> sanang. Yangi chiziq oʻzi kesib oʻtgan chiziqlardan '
            'bitta koʻp boʻlak qoʻshadi, shuning uchun jami 2, 4, 7, 11, 16 boʻlib oʻsadi. '
            'Sanoqni shunday qadamma-qadam qurish rekurrent munosabat deyiladi va oʻsadigan '
            'deyarli hamma narsa shunday sanaladi: qoʻl berib koʻrishishlar, turnirdagi '
            'oʻyinlar, jumboqdagi yurishlar.</p>',
    },

    {
        'number': 26, 'round': 5, 'category': 'strategy', 'difficulty': 4,
        'title':    'Thirty Hats in a Line',
        'title_uz': 'Qatordagi oʻttizta qalpoq',
        'teaser':    'Red, white or blue — nobody sees their own. How many can be sure to guess right?',
        'teaser_uz': 'Qizil, oq yoki koʻk — hech kim oʻzinikini koʻrmaydi. Nechtasi albatta toʻgʻri topadi?',

        'body':
            '<p>On the school’s game day, <strong>30 pupils</strong> stand in a single line, '
            'one behind another, all facing forward. A teacher puts a hat on each head: '
            '<strong>red, white or blue</strong>, chosen any way she likes. Each pupil can '
            'see the hats of everyone in front of them — but not their own, and not those '
            'behind.</p>'
            + fig(row(['🧢', '🧢', '🧢', '🧢', '🧢', '…'], ['30', '29', '28', '27', '26', ''],
                      glyph_size=26),
                  'Pupil 30 stands at the back and sees all 29 hats in front.')
            + '<p>Starting from the <strong>back</strong>, each pupil in turn says exactly one '
            'word out loud — “red”, “white” or “blue” — and everybody hears it. A pupil who '
            'names their own hat colour scores a point for the class.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🎩</span>'
            '<span>The class may agree on a plan beforehand. During the game: one colour word '
            'each, no tone of voice, no pauses, no signals. The teacher may know the plan and '
            'will choose the worst hats for it.</span></div>'
            '<p class="lg-ask">Answer to type: the largest number of pupils who can be '
            '<strong>guaranteed</strong> to name their own colour.</p>',

        'body_uz':
            '<p>Maktabdagi oʻyinlar kunida <strong>30 nafar oʻquvchi</strong> bir qatorga, '
            'birining ortida biri, hammasi oldinga qarab turibdi. Oʻqituvchi har birining '
            'boshiga qalpoq kiydiradi: <strong>qizil, oq yoki koʻk</strong> — xohlaganicha '
            'tanlaydi. Har bir oʻquvchi oʻzidan oldindagilarning qalpogʻini koʻradi — oʻzinikini '
            'ham, orqadagilarnikini ham koʻrmaydi.</p>'
            + fig(row(['🧢', '🧢', '🧢', '🧢', '🧢', '…'], ['30', '29', '28', '27', '26', ''],
                      glyph_size=26),
                  '30-oʻquvchi eng orqada turib, oldidagi 29 ta qalpoqni koʻradi.')
            + '<p><strong>Orqadan</strong> boshlab har bir oʻquvchi navbat bilan ovoz chiqarib '
            'roppa-rosa bitta soʻz aytadi — «qizil», «oq» yoki «koʻk» — va buni hamma '
            'eshitadi. Oʻz qalpogʻining rangini toʻgʻri aytgan oʻquvchi sinfga bir ochko '
            'olib keladi.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🎩</span>'
            '<span>Sinf oldindan reja kelishib olishi mumkin. Oʻyin paytida: har kim bitta rang '
            'soʻzi, ohang yoʻq, pauza yoʻq, ishora yoʻq. Oʻqituvchi rejani bilishi va unga eng '
            'yomon qalpoqlarni tanlashi mumkin.</span></div>'
            '<p class="lg-ask">Javob sifatida yozing: oʻz rangini <strong>albatta</strong> '
            'toʻgʻri aytadigan oʻquvchilarning eng koʻp soni.</p>',

        'hint':    'Number the colours 0, 1 and 2. The pupil at the back cannot help '
                   'themselves — but one word from them can carry a total.',
        'hint_uz': 'Ranglarni 0, 1 va 2 deb raqamlang. Eng orqadagi oʻquvchi oʻziga yordam '
                   'berolmaydi — lekin uning bitta soʻzi yigʻindini yetkaza oladi.',

        'answer_key': '29',
        'accepted': ['29 pupils', '29 ta', '29 nafar', '29 kishi', 'yigirma toʻqqiz',
                     "yigirma to'qqiz", 'twenty nine', 'twenty-nine'],
        'answer_hint':    'a number of pupils',
        'answer_hint_uz': 'oʻquvchilar soni',

        'solution':
            '<ol class="lg-steps">'
            '<li>Give the colours numbers: red = 0, white = 1, blue = 2. All arithmetic is '
            '“remainder after dividing by 3”.</li>'
            '<li>Pupil 30 (at the back) adds up the 29 hats in front and says the colour '
            'whose number equals that total’s remainder. Their own hat is a gamble — so they '
            'are the one pupil who cannot be guaranteed.</li>'
            '<li>Pupil 29 now knows the total of hats 1-29. They can see hats 1-28. The '
            'difference is their own hat: they say it, correctly.</li>'
            '<li>Pupil 28 knows the same total, has <em>heard</em> pupil 29’s correct colour, '
            'and sees hats 1-27. Again only one hat is missing — their own.</li>'
            '<li>And so on to the front: every pupil from 29 down to 1 is right. That is '
            '<strong>29</strong> guaranteed.</li>'
            '<li>All 30 is impossible: pupil 30 sees nothing that depends on their own hat, '
            'so whatever they say, the teacher can give them a different colour.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> one word can carry a whole '
            'summary if everyone agrees what it means. Here it is a <em>check digit</em>: the '
            'total of all the hats, modulo 3. Every bank card number ends with exactly such a '
            'digit, so a machine notices when one figure is mistyped — the same idea that '
            'saves 29 pupils here.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Ranglarga son beramiz: qizil = 0, oq = 1, koʻk = 2. Barcha hisob «3 ga '
            'boʻlgandagi qoldiq» boʻyicha.</li>'
            '<li>30-oʻquvchi (eng orqadagi) oldidagi 29 ta qalpoqni qoʻshadi va soni shu '
            'yigʻindining qoldigʻiga teng rangni aytadi. Uning oʻz qalpogʻi — tavakkal; '
            'shuning uchun kafolat berib boʻlmaydigan yagona oʻquvchi aynan u.</li>'
            '<li>29-oʻquvchi endi 1-29 qalpoqlarning yigʻindisini biladi. U 1-28 qalpoqlarni '
            'koʻradi. Farqi — uning oʻz qalpogʻi: u toʻgʻri aytadi.</li>'
            '<li>28-oʻquvchi xuddi shu yigʻindini biladi, 29-oʻquvchining toʻgʻri rangini '
            '<em>eshitgan</em> va 1-27 qalpoqlarni koʻradi. Yana bitta qalpoq yetishmaydi — '
            'oʻziniki.</li>'
            '<li>Va shu tarzda eng oldigacha: 29 dan 1 gacha barcha oʻquvchi toʻgʻri topadi. '
            'Bu <strong>29</strong> ta kafolat.</li>'
            '<li>30 tasi ham mumkin emas: 30-oʻquvchi oʻz qalpogʻiga bogʻliq hech narsani '
            'koʻrmaydi, shuning uchun u nima demasin, oʻqituvchi unga boshqa rang kiydira '
            'oladi.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> hamma bir xil maʼnoni kelishib olsa, '
            'bitta soʻz butun xulosani tashiy oladi. Bu yerda u — <em>nazorat raqami</em>: '
            'barcha qalpoqlar yigʻindisining 3 ga boʻlgandagi qoldigʻi. Har bir bank kartasi '
            'raqami xuddi shunday raqam bilan tugaydi, shuning uchun bitta raqam xato '
            'kiritilsa, mashina buni sezadi — bu yerda 29 oʻquvchini qutqargan oʻsha '
            'gʻoya.</p>',
    },

    # ── Round 6 ─────────────────────────────────────────────────────────────
    {
        'number': 27, 'round': 6, 'category': 'shapes', 'difficulty': 3,
        'title':    'A Rope Around the Earth',
        'title_uz': 'Yerni oʻragan arqon',
        'teaser':    'Raise a rope one metre all the way round the equator. How much extra rope?',
        'teaser_uz': 'Ekvator boʻylab arqonni hamma joyda bir metr koʻtaring. Qancha arqon qoʻshiladi?',

        'body':
            '<p>Imagine a rope tied tightly around the Earth along the equator — about '
            '<strong>40,075 kilometres</strong> of rope, lying on the ground and the sea all '
            'the way round. (Pretend the Earth is a perfectly smooth ball.)</p>'
            '<p>Now we want the rope to float exactly <strong>1 metre</strong> above the '
            'surface everywhere, all the way round, so a child could walk underneath it. We '
            'cut the rope and splice in an extra piece.</p>'
            + fig(rings('R', 'R + 1 m'),
                  'The Earth (solid) and the lifted rope (dashed): only the radius grew, by 1 metre.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">📏</span>'
              '<span>The new rope is a circle 1 metre higher than the old one at every '
              'point. How long is the <strong>extra piece</strong>?</span></div>'
            '<p>Most people guess thousands of kilometres. Some guess the whole length of '
            'the country. Calculate before you guess.</p>'
            '<p class="lg-ask">Answer to type: the length of the extra piece in '
            '<strong>centimetres</strong>, rounded to the nearest whole centimetre.</p>',

        'body_uz':
            '<p>Ekvator boʻylab Yerni mahkam oʻrab olgan arqonni tasavvur qiling — taxminan '
            '<strong>40 075 kilometr</strong> arqon, butun aylana boʻylab yer va dengiz ustida '
            'yotibdi. (Yerni mutlaqo silliq shar deb hisoblang.)</p>'
            '<p>Endi biz arqon hamma joyda, butun aylana boʻylab yer yuzasidan roppa-rosa '
            '<strong>1 metr</strong> balandlikda turishini, tagidan bola oʻtib keta olishini '
            'xohlaymiz. Arqonni kesib, unga qoʻshimcha boʻlak ulaymiz.</p>'
            + fig(rings('R', 'R + 1 m'),
                  'Yer (yaxlit) va koʻtarilgan arqon (uzuq chiziq): faqat radius 1 metrga oʻsdi.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">📏</span>'
              '<span>Yangi arqon — har bir nuqtada eskisidan 1 metr baland aylana. '
              '<strong>Qoʻshimcha boʻlak</strong> qancha uzun?</span></div>'
            '<p>Koʻpchilik minglab kilometr deb taxmin qiladi. Baʼzilar butun mamlakat '
            'uzunligicha deydi. Taxmin qilishdan oldin hisoblang.</p>'
            '<p class="lg-ask">Javob sifatida yozing: qoʻshimcha boʻlakning uzunligi, '
            '<strong>santimetrda</strong>, butun santimetrgacha yaxlitlangan.</p>',

        'hint':    'Call the Earth’s radius R. Write the old length and the new length, and '
                   'subtract before you put any numbers in.',
        'hint_uz': 'Yer radiusini R deb belgilang. Eski va yangi uzunlikni yozib, son '
                   'qoʻyishdan oldin ayiring.',

        'answer_key': '628',
        'accepted': ['628 cm', '628 sm', '628cm', '628sm', '6.28 m', '6,28 m', '6.28m', '6,28m',
                     'olti yuz yigirma sakkiz', 'six hundred twenty eight'],
        'answer_hint':    'a length in centimetres',
        'answer_hint_uz': 'santimetrdagi uzunlik',

        'solution':
            '<ol class="lg-steps">'
            '<li>The old rope is a circle of radius R: its length is <strong>2πR</strong>.</li>'
            '<li>The new rope is 1 metre higher everywhere: a circle of radius R + 1. Its '
            'length is <strong>2π(R + 1) = 2πR + 2π</strong>.</li>'
            '<li>The extra piece is the difference: 2πR + 2π − 2πR = <strong>2π metres</strong>. '
            'R has cancelled out completely.</li>'
            '<li>2π ≈ 6.2832 m ≈ <strong>628 cm</strong>. About the length of a small '
            'car and a half.</li>'
            '<li>The size of the Earth never mattered. A rope around a football, lifted '
            '1 metre, needs exactly the same 6.28 metres extra.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> write the problem with letters '
            'first and let them cancel. A huge number (40,075 km) frightens intuition into '
            'a huge answer, but circumference grows in step with radius: every extra metre of '
            'radius adds 2π metres of length, whether the circle is a coin or a planet. '
            'Algebra’s great gift is showing you which numbers a question never needed.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Eski arqon — radiusi R boʻlgan aylana: uzunligi <strong>2πR</strong>.</li>'
            '<li>Yangi arqon hamma joyda 1 metr baland: radiusi R + 1 boʻlgan aylana. '
            'Uzunligi <strong>2π(R + 1) = 2πR + 2π</strong>.</li>'
            '<li>Qoʻshimcha boʻlak — ayirma: 2πR + 2π − 2πR = <strong>2π metr</strong>. R '
            'butunlay qisqarib ketdi.</li>'
            '<li>2π ≈ 6,2832 m ≈ <strong>628 sm</strong>. Taxminan bir yarim kichik '
            'avtomobil uzunligi.</li>'
            '<li>Yerning kattaligi umuman ahamiyatsiz ekan. Futbol toʻpini oʻragan arqonni '
            '1 metr koʻtarish uchun ham aynan shu 6,28 metr kerak.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> masalani avval harflar bilan yozing '
            'va ularning qisqarishiga imkon bering. Ulkan son (40 075 km) sezgini choʻchitib, '
            'ulkan javobga undaydi, lekin aylana uzunligi radius bilan bir maromda oʻsadi: '
            'radiusning har bir qoʻshimcha metri uzunlikka 2π metr qoʻshadi — aylana tanga '
            'boʻladimi yoki sayyora. Algebraning buyuk sovgʻasi — savolga qaysi sonlar umuman '
            'kerak emasligini koʻrsatib berishi.</p>',
    },

    {
        'number': 28, 'round': 6, 'category': 'chance', 'difficulty': 4,
        'title':    'Six Cities in the Wafers',
        'title_uz': 'Vafli ichidagi olti shahar',
        'teaser':    'One sticker in every wafer, six to collect. How many wafers on average?',
        'teaser_uz': 'Har vaflida bitta stiker, yigʻish kerak boʻlgan oltita. Oʻrtacha nechta vafli?',

        'body':
            '<p>A new wafer at the school kiosk comes with a sticker inside: one of '
            '<strong>six cities</strong> — Tashkent, Samarkand, Bukhara, Khiva, Termez or '
            'Kokand. Every wafer is equally likely to hold any of the six, whatever the '
            'previous wafers held.</p>'
            + fig(row(['🏙️', '🕌', '🏛️', '🧱', '🏜️', '🌳'],
                      ['TAS', 'SAM', 'BUX', 'XIV', 'TER', 'QOʻQ'], glyph_size=24),
                  'Six stickers. Afsona buys one wafer a day until she has all six.')
            + '<p>Afsona buys wafers one at a time until her album has all six cities. Some '
            'days she gets lucky; often she gets a third Bukhara.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🎲</span>'
            '<span>Each wafer: one sticker, each city with chance <strong>1/6</strong>, '
            'independent of all the others. She stops the moment the sixth city '
            'arrives.</span></div>'
            '<p>Six cities — surely about six wafers? No: much more.</p>'
            '<p class="lg-ask">Answer to type: the <strong>average</strong> (expected) number '
            'of wafers she needs to buy, as an exact decimal.</p>',

        'body_uz':
            '<p>Maktab kioskidagi yangi vafli ichida stiker bor: <strong>oltita shahardan</strong> '
            'biri — Toshkent, Samarqand, Buxoro, Xiva, Termiz yoki Qoʻqon. Oldingi vaflilarda '
            'nima chiqqanidan qatʼi nazar, har bir vaflida oltitadan istalgani bir xil ehtimol '
            'bilan chiqadi.</p>'
            + fig(row(['🏙️', '🕌', '🏛️', '🧱', '🏜️', '🌳'],
                      ['TAS', 'SAM', 'BUX', 'XIV', 'TER', 'QOʻQ'], glyph_size=24),
                  'Oltita stiker. Afsona oltitasi ham yigʻilguncha har kuni bitta vafli oladi.')
            + '<p>Afsona albomida oltita shahar ham yigʻilguncha vaflini bittadan sotib oladi. '
            'Baʼzi kunlari omadi keladi; koʻpincha esa uchinchi Buxoro chiqadi.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🎲</span>'
            '<span>Har bir vafli: bitta stiker, har bir shahar ehtimoli <strong>1/6</strong>, '
            'boshqalariga bogʻliq emas. Oltinchi shahar chiqqan zahoti u toʻxtaydi.</span></div>'
            '<p>Oltita shahar — taxminan oltita vafli boʻlsa kerak? Yoʻq: ancha koʻp.</p>'
            '<p class="lg-ask">Javob sifatida yozing: u sotib olishi kerak boʻlgan vaflilarning '
            '<strong>oʻrtacha</strong> (kutilgan) soni, aniq oʻnli kasr koʻrinishida.</p>',

        'hint':    'Split the job into six stages: waiting for a new city when she has 0, 1, '
                   '2 … 5 already. If a success has chance p, you wait 1/p tries on average.',
        'hint_uz': 'Ishni olti bosqichga boʻling: qoʻlida 0, 1, 2 … 5 ta shahar boʻlganda yangi '
                   'shaharni kutish. Muvaffaqiyat ehtimoli p boʻlsa, oʻrtacha 1/p marta '
                   'urinasiz.',

        'answer_key': '14.7',
        'accepted': ['14,7', '14.7 wafers', '14,7 ta', '14,7 vafli'],
        'answer_hint':    'an average, a decimal',
        'answer_hint_uz': 'oʻrtacha qiymat, oʻnli kasr',

        'solution':
            '<ol class="lg-steps">'
            '<li><strong>The rule:</strong> if each try succeeds with chance p, you need '
            '<strong>1/p</strong> tries on average. (A die shows a six on average once every '
            '6 rolls.)</li>'
            '<li>Stage 1: with no stickers, any city is new: p = 6/6, wait <strong>1</strong> '
            'wafer.</li>'
            '<li>Stage 2: 5 of 6 cities are new: p = 5/6, wait <strong>6/5</strong>. Stage 3: '
            'wait <strong>6/4</strong>. Stage 4: <strong>6/3</strong>. Stage 5: '
            '<strong>6/2</strong>.</li>'
            '<li>Stage 6: only one city is missing: p = 1/6, wait <strong>6</strong> wafers on '
            'average — the last sticker alone costs as much as the naive guess for all '
            'six!</li>'
            '<li>Add the stages: 1 + 1.2 + 1.5 + 2 + 3 + 6 = <strong>14.7</strong> wafers.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> break a long wait into stages and '
            'add the averages — averages always add, even when the chances do not. And notice '
            'where the cost sits: almost half of it is the last sticker. Collecting the final '
            'few of anything — rare stickers, the last bug in a program, the last pupil to '
            'hand in homework — always takes the longest.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li><strong>Qoida:</strong> har bir urinish p ehtimol bilan muvaffaqiyatli '
            'boʻlsa, oʻrtacha <strong>1/p</strong> marta urinish kerak. (Zar oʻrtacha har 6 '
            'tashlashda bir marta oltini koʻrsatadi.)</li>'
            '<li>1-bosqich: stiker yoʻq, har qanday shahar yangi: p = 6/6, <strong>1</strong> '
            'vafli kutiladi.</li>'
            '<li>2-bosqich: 6 tadan 5 ta shahar yangi: p = 5/6, <strong>6/5</strong> kutiladi. '
            '3-bosqich: <strong>6/4</strong>. 4-bosqich: <strong>6/3</strong>. 5-bosqich: '
            '<strong>6/2</strong>.</li>'
            '<li>6-bosqich: faqat bitta shahar yetishmaydi: p = 1/6, oʻrtacha <strong>6</strong> '
            'vafli — birgina oxirgi stiker oltitasi uchun qilingan sodda taxminchalik '
            'turadi!</li>'
            '<li>Bosqichlarni qoʻshamiz: 1 + 1,2 + 1,5 + 2 + 3 + 6 = <strong>14,7</strong> '
            'vafli.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> uzoq kutishni bosqichlarga boʻling '
            'va oʻrtachalarni qoʻshing — ehtimollar qoʻshilmasa ham, oʻrtachalar doim qoʻshiladi. '
            'Va xarajat qayerda ekaniga eʼtibor bering: deyarli yarmi — oxirgi stiker. Har '
            'qanday narsaning oxirgi bir nechtasini yigʻish — kamyob stikerlar, dasturdagi '
            'oxirgi xato, uy vazifasini topshiradigan oxirgi oʻquvchi — doim eng koʻp vaqt '
            'oladi.</p>',
    },

    # ── Round 7 ─────────────────────────────────────────────────────────────
    {
        'number': 29, 'round': 7, 'category': 'numbers', 'difficulty': 3,
        'title':    'The 2026 Lockers',
        'title_uz': '2026 ta shkafcha',
        'teaser':    '2026 pupils open and close 2026 lockers. How many stay open?',
        'teaser_uz': '2026 oʻquvchi 2026 ta shkafchani ochib-yopadi. Nechtasi ochiq qoladi?',

        'body':
            '<p>A new sports centre has a corridor of <strong>2026 lockers</strong>, numbered '
            '1 to 2026, all closed. To celebrate the opening, 2026 pupils walk down the '
            'corridor one after another.</p>'
            + fig(row(['🚪', '🚪', '🚪', '🚪', '🚪', '🚪'], ['1', '2', '3', '4', '5', '6'],
                      glyph_size=26),
                  'The first six lockers of 2026. Each one is flipped many times.')
            + '<p>Pupil 1 changes <strong>every</strong> locker (opens each one). Pupil 2 '
            'changes every 2nd locker (2, 4, 6 …). Pupil 3 changes every 3rd (3, 6, 9 …). In '
            'general, pupil k changes every locker whose number is a multiple of k.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🔁</span>'
            '<span>“Change” means: open it if it is closed, close it if it is open. All 2026 '
            'pupils take their turn.</span></div>'
            '<p class="lg-ask">Answer to type: <strong>how many lockers are open</strong> '
            'after the last pupil has passed.</p>',

        'body_uz':
            '<p>Yangi sport majmuasining yoʻlagida 1 dan 2026 gacha raqamlangan '
            '<strong>2026 ta shkafcha</strong> bor, hammasi yopiq. Ochilishni nishonlash uchun '
            '2026 nafar oʻquvchi birin-ketin yoʻlakdan oʻtadi.</p>'
            + fig(row(['🚪', '🚪', '🚪', '🚪', '🚪', '🚪'], ['1', '2', '3', '4', '5', '6'],
                      glyph_size=26),
                  '2026 tadan dastlabki oltitasi. Har biri koʻp marta ochib-yopiladi.')
            + '<p>1-oʻquvchi <strong>har bir</strong> shkafchani oʻzgartiradi (hammasini '
            'ochadi). 2-oʻquvchi har 2-shkafchani (2, 4, 6 …). 3-oʻquvchi har 3-sini '
            '(3, 6, 9 …). Umuman, k-oʻquvchi raqami k ga karrali boʻlgan har bir shkafchani '
            'oʻzgartiradi.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🔁</span>'
            '<span>«Oʻzgartirish» — yopiq boʻlsa ochish, ochiq boʻlsa yopish. 2026 '
            'oʻquvchining hammasi navbat bilan oʻtadi.</span></div>'
            '<p class="lg-ask">Javob sifatida yozing: oxirgi oʻquvchi oʻtgandan keyin '
            '<strong>nechta shkafcha ochiq</strong> qoladi.</p>',

        'hint':    'Locker n is changed once for every divisor of n. Which numbers have an odd '
                   'number of divisors?',
        'hint_uz': 'n-shkafcha n ning har bir boʻluvchisi uchun bir martadan oʻzgartiriladi. '
                   'Qaysi sonlarning boʻluvchilari soni toq?',

        'answer_key': '45',
        'accepted': ['45 lockers', '45 ta', '45 ta shkafcha', 'qirq besh', 'forty five',
                     'forty-five'],
        'answer_hint':    'a number of lockers',
        'answer_hint_uz': 'shkafchalar soni',

        'solution':
            '<ol class="lg-steps">'
            '<li>Locker n is changed by pupil k exactly when k divides n. So it is changed '
            'once for <strong>each divisor</strong> of n.</li>'
            '<li>It starts closed, so it ends <strong>open</strong> exactly when it was '
            'changed an <strong>odd</strong> number of times.</li>'
            '<li>Divisors come in pairs: 12 = 1 × 12 = 2 × 6 = 3 × 4. Pairs make an even '
            'count — unless one pair is a number with itself: 36 = 6 × 6, where 6 is counted '
            'once. That happens only for <strong>perfect squares</strong>.</li>'
            '<li>So the open lockers are 1, 4, 9, 16, 25 … — the squares.</li>'
            '<li>44² = 1936 ≤ 2026 and 45² = 2025 ≤ 2026, but 46² = 2116 is too big. So '
            'there are <strong>45</strong> open lockers, the last one being 2025.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> a back-and-forth switch only '
            'remembers whether it was flipped an odd or even number of times — its '
            '<em>parity</em>. Turn the story into “how many divisors?”, pair the divisors up, '
            'and only the squares are left without a partner. Pairing things up to find the '
            'odd one out is one of the most useful moves in all of mathematics.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>n-shkafchani k-oʻquvchi aynan k soni n ni boʻlganda oʻzgartiradi. Demak u n '
            'ning <strong>har bir boʻluvchisi</strong> uchun bir marta oʻzgaradi.</li>'
            '<li>U yopiq holda boshlanadi, shuning uchun aynan <strong>toq</strong> marta '
            'oʻzgartirilganda oxirida <strong>ochiq</strong> qoladi.</li>'
            '<li>Boʻluvchilar juft-juft keladi: 12 = 1 × 12 = 2 × 6 = 3 × 4. Juftliklar juft '
            'son beradi — agar biror juftlik sonning oʻzi bilan oʻzi boʻlmasa: 36 = 6 × 6, '
            'bu yerda 6 bir marta sanaladi. Bu faqat <strong>toʻla kvadratlarda</strong> '
            'boʻladi.</li>'
            '<li>Demak ochiq shkafchalar 1, 4, 9, 16, 25 … — kvadratlar.</li>'
            '<li>44² = 1936 ≤ 2026 va 45² = 2025 ≤ 2026, lekin 46² = 2116 juda katta. Demak '
            '<strong>45</strong> ta shkafcha ochiq, oxirgisi — 2025.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> u yoqqa-bu yoqqa almashadigan '
            'tugma faqat toq yoki juft marta bosilganini — uning <em>juft-toqligini</em> — '
            'eslab qoladi. Hikoyani «nechta boʻluvchi?» savoliga aylantiring, boʻluvchilarni '
            'juftlang va jufti yoʻq qolgani faqat kvadratlar boʻladi. Ortiqchasini topish '
            'uchun narsalarni juftlash — butun matematikadagi eng foydali usullardan biri.</p>',
    },

    {
        'number': 30, 'round': 7, 'category': 'chance', 'difficulty': 5,
        'title':    'The Hundred Boxes',
        'title_uz': 'Yuzta quti',
        'teaser':    'A hundred pupils, a hundred boxes, fifty looks each. Everybody must succeed.',
        'teaser_uz': 'Yuz oʻquvchi, yuz quti, har kimga ellikta qarash. Hamma uddalashi shart.',

        'body':
            '<p>A school offers a class of <strong>100 pupils</strong>, numbered 1 to 100, a '
            'trip to Samarkand — on one condition. In a closed room stand '
            '<strong>100 boxes</strong>, numbered 1 to 100. Inside them, shuffled at random, '
            'are cards with the pupils’ numbers: one card per box.</p>'
            '<p>One pupil at a time enters the room, may open <strong>at most 50 '
            'boxes</strong>, and must find the card with their own number. Then they leave by '
            'another door, the boxes are closed again exactly as they were, and they may not '
            'speak to anyone still waiting.</p>'
            + fig(row(['📦', '📦', '📦', '📦', '📦', '…'], ['1', '2', '3', '4', '5', '100'],
                      glyph_size=26),
                  'A hundred boxes, a hundred hidden cards. Fifty looks per pupil.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🎟️</span>'
              '<span>The trip happens only if <strong>every one</strong> of the 100 pupils '
              'finds their own number. The class may agree on a plan beforehand, but no '
              'messages once it begins.</span></div>'
            '<p>If each pupil opens 50 boxes at random, each succeeds with chance ½, and all '
            '100 together with chance (½)<sup>100</sup> — practically zero. Yet there is a '
            'plan that wins astonishingly often.</p>'
            '<p class="lg-ask">Answer to type: the class’s chance of success with the best '
            'plan, as a <strong>percentage rounded down</strong> to a whole number.</p>',

        'body_uz':
            '<p>Maktab 1 dan 100 gacha raqamlangan <strong>100 nafar oʻquvchidan</strong> '
            'iborat sinfga Samarqandga sayohat taklif qiladi — bitta shart bilan. Yopiq xonada '
            '1 dan 100 gacha raqamlangan <strong>100 ta quti</strong> turibdi. Ularning ichida, '
            'tasodifiy aralashtirilgan holda, oʻquvchilar raqamlari yozilgan kartochkalar bor: '
            'har qutida bittadan.</p>'
            '<p>Oʻquvchilar xonaga bittadan kiradi, <strong>koʻpi bilan 50 ta qutini</strong> '
            'ochishi mumkin va oʻz raqami yozilgan kartochkani topishi shart. Keyin u boshqa '
            'eshikdan chiqib ketadi, qutilar avvalgidek yopiladi va u hali navbatda turganlar '
            'bilan gaplasha olmaydi.</p>'
            + fig(row(['📦', '📦', '📦', '📦', '📦', '…'], ['1', '2', '3', '4', '5', '100'],
                      glyph_size=26),
                  'Yuzta quti, yuzta yashirin kartochka. Har oʻquvchiga ellikta qarash.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🎟️</span>'
              '<span>Sayohat faqat 100 oʻquvchining <strong>har biri</strong> oʻz raqamini '
              'topsagina boʻladi. Sinf oldindan reja kelishib olishi mumkin, lekin boshlangandan '
              'keyin hech qanday xabar yoʻq.</span></div>'
            '<p>Agar har kim 50 ta qutini tasodifan ochsa, har biri ½ ehtimol bilan topadi, '
            '100 tasi birgalikda esa (½)<sup>100</sup> ehtimol bilan — amalda nol. Lekin '
            'hayratlanarli darajada tez-tez yutadigan reja bor.</p>'
            '<p class="lg-ask">Javob sifatida yozing: eng yaxshi reja bilan sinfning '
            'muvaffaqiyat ehtimoli, <strong>foizda, butun songacha pastga '
            'yaxlitlangan</strong>.</p>',

        'hint':    'Pupil k opens box k first, then the box whose number was on the card '
                   'inside, and so on. Follow the loops.',
        'hint_uz': 'k-oʻquvchi avval k-qutini ochadi, keyin ichidagi kartochkada yozilgan '
                   'raqamli qutini va hokazo. Halqalarni kuzating.',

        'answer_key': '31',
        'accepted': ['31%', '31 %', '31 foiz', '31 percent', 'oʻttiz bir', "o'ttiz bir",
                     'thirty one', 'thirty-one'],
        'answer_hint':    'a percentage, a whole number',
        'answer_hint_uz': 'foiz, butun son',

        'solution':
            '<ol class="lg-steps">'
            '<li><strong>The plan:</strong> pupil k opens box k. If the card inside says j, '
            'they open box j next, and keep following the cards.</li>'
            '<li>Following cards like this walks around a <strong>loop</strong>: the boxes '
            'and cards form closed chains, and pupil k’s chain is the one that ends at the '
            'card “k” — because the card “k” points back to box k, where they started.</li>'
            '<li>So pupil k succeeds exactly when <strong>their loop has at most 50 '
            'boxes</strong>. And then everyone on that loop succeeds too.</li>'
            '<li>The whole class fails only if the shuffle contains <strong>one loop longer '
            'than 50</strong> (there can be at most one). The chance that a random shuffle of '
            '100 has a loop of exactly length L (for L &gt; 50) is exactly '
            '<strong>1/L</strong>.</li>'
            '<li>Chance of failure = 1/51 + 1/52 + … + 1/100 ≈ 0.6882. Chance of success ≈ '
            '1 − 0.6882 = <strong>0.3118</strong>, that is 31.18%, rounded down '
            '<strong>31%</strong>.</li>'
            '<li>From practically 0 to almost one in three: the pupils’ fates are now '
            'tied together. They succeed or fail as a group.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> you cannot change any single '
            'pupil’s chance — it is still ½ — but you can make their successes '
            '<em>happen together</em>. Correlating risks instead of leaving them independent '
            'turns a hopeless bet into a good one. Insurance, team plans and backups in '
            'engineering all play with this same lever.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li><strong>Reja:</strong> k-oʻquvchi k-qutini ochadi. Ichidagi kartochkada j '
            'yozilgan boʻlsa, keyin j-qutini ochadi va kartochkalarga ergashib boraveradi.</li>'
            '<li>Kartochkalarga shunday ergashish <strong>halqa</strong> boʻylab aylanadi: '
            'qutilar va kartochkalar yopiq zanjirlar hosil qiladi va k-oʻquvchining zanjiri '
            '«k» kartochkasida tugaydi — chunki «k» kartochkasi u boshlagan k-qutiga qaytib '
            'ishora qiladi.</li>'
            '<li>Demak k-oʻquvchi aynan <strong>uning halqasida koʻpi bilan 50 ta quti '
            'boʻlsa</strong> topadi. Unda shu halqadagi hamma ham topadi.</li>'
            '<li>Butun sinf faqat aralashtirishda <strong>50 dan uzun bitta halqa</strong> '
            'boʻlsa yutqazadi (bunday halqa koʻpi bilan bitta boʻladi). 100 tani tasodifiy '
            'aralashtirishda uzunligi aynan L boʻlgan halqa boʻlish ehtimoli (L &gt; 50 uchun) '
            'roppa-rosa <strong>1/L</strong>.</li>'
            '<li>Yutqazish ehtimoli = 1/51 + 1/52 + … + 1/100 ≈ 0,6882. Muvaffaqiyat '
            'ehtimoli ≈ 1 − 0,6882 = <strong>0,3118</strong>, yaʼni 31,18%, pastga '
            'yaxlitlansa <strong>31%</strong>.</li>'
            '<li>Amalda noldan deyarli uchdan birgacha: endi oʻquvchilarning taqdiri bir-biriga '
            'bogʻlangan. Ular birga yutadi yoki birga yutqazadi.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> birorta oʻquvchining ehtimolini '
            'oʻzgartirib boʻlmaydi — u baribir ½ — lekin ularning omadini <em>birga sodir '
            'boʻladigan</em> qilish mumkin. Xavflarni mustaqil qoldirish oʻrniga bir-biriga '
            'bogʻlash umidsiz garovni yaxshi garovga aylantiradi. Sugʻurta, jamoaviy rejalar '
            'va muhandislikdagi zaxira tizimlar ham aynan shu richag bilan ishlaydi.</p>',
    },

    # ── Round 8 ─────────────────────────────────────────────────────────────
    {
        'number': 31, 'round': 8, 'category': 'cutting', 'difficulty': 3,
        'title':    'The Silver Chain',
        'title_uz': 'Kumush zanjir',
        'teaser':    'One link a night, change allowed, only three links may be opened.',
        'teaser_uz': 'Har kecha bitta halqa, qaytim mumkin, faqat uchta halqani ochish mumkin.',

        'body':
            '<p>A traveller on the Silk Road reaches a caravanserai with no money — only a '
            '<strong>silver chain</strong> of links. The keeper agrees: one link per night, '
            'paid every morning. After night 1 the keeper must hold exactly 1 link, after '
            'night 2 exactly 2 links, and so on — every morning, never in advance.</p>'
            '<p>The keeper is happy to <strong>give change</strong>: the traveller may hand '
            'over a long piece and take back pieces the keeper already holds. But opening a '
            'link is the jeweller’s work, and the traveller can only afford to have '
            '<strong>three links opened</strong>. An opened link is a loose single link; the '
            'chain on either side of it falls into two pieces.</p>'
            + fig(chain(7, cut=(3,)),
                  'With 7 links, opening only link 3 leaves pieces of 1, 2 and 4: enough for '
                  'seven nights.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⛓️</span>'
              '<span>At most <strong>three</strong> links opened, all before night 1. He must '
              'pay correctly every single morning until the whole chain is used up.</span></div>'
            '<p class="lg-ask">Answer to type: the <strong>longest chain</strong> (number of '
            'links) that lets him do this.</p>',

        'body_uz':
            '<p>Ipak yoʻlidagi bir sayyoh karvonsaroyga pulsiz yetib keladi — qoʻlida faqat '
            'halqalardan iborat <strong>kumush zanjir</strong> bor. Karvonsaroy egasi rozi '
            'boʻladi: har kecha uchun bitta halqa, har kuni ertalab toʻlanadi. 1-kechadan '
            'keyin egada roppa-rosa 1 ta halqa, 2-kechadan keyin roppa-rosa 2 ta halqa '
            'boʻlishi kerak va hokazo — har kuni ertalab, hech qachon oldindan emas.</p>'
            '<p>Ega bajonidil <strong>qaytim beradi</strong>: sayyoh uzun boʻlakni berib, '
            'egada allaqachon bor boʻlaklarni qaytarib olishi mumkin. Lekin halqani ochish — '
            'zargarning ishi va sayyoh faqat <strong>uchta halqani ochtirishga</strong> '
            'qurbi yetadi. Ochilgan halqa — alohida yakka halqa; uning ikki yonidagi zanjir '
            'ikki boʻlakka ajraladi.</p>'
            + fig(chain(7, cut=(3,)),
                  '7 halqada faqat 3-halqani ochish 1, 2 va 4 lik boʻlaklarni beradi: yetti kecha '
                  'uchun yetarli.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⛓️</span>'
              '<span>Koʻpi bilan <strong>uchta</strong> halqa ochiladi, hammasi 1-kechadan '
              'oldin. U butun zanjir tugaguncha har kuni ertalab toʻgʻri toʻlashi shart.</span></div>'
            '<p class="lg-ask">Javob sifatida yozing: bunga imkon beradigan <strong>eng uzun '
            'zanjir</strong> (halqalar soni).</p>',

        'hint':    'Three opened links give three loose singles. Then the pieces between them '
                   'should each be as long as everything smaller can still pay for, plus one.',
        'hint_uz': 'Uchta ochilgan halqa uchta yakka halqa beradi. Ular orasidagi har bir boʻlak '
                   'esa undan kichiklari bilan toʻlash mumkin boʻlgan hamma narsadan bitta '
                   'uzun boʻlsin.',

        'answer_key': '63',
        'accepted': ['63 links', '63 ta', '63 halqa', '63 ta halqa', 'oltmish uch', 'sixty three',
                     'sixty-three'],
        'answer_hint':    'a number of links',
        'answer_hint_uz': 'halqalar soni',

        'solution':
            '<ol class="lg-steps">'
            '<li>Change makes this a question about <strong>pieces</strong>: on morning d, '
            'the keeper must hold some pieces adding up to exactly d. So every number from 1 '
            'to the chain length must be a sum of some of the pieces.</li>'
            '<li>Three opened links give <strong>three singles</strong>: they pay nights 1, '
            '2 and 3.</li>'
            '<li>The next piece should be as long as possible while night 4 is still payable: '
            '<strong>4</strong> links. With 3 singles and a 4 you can pay anything up to 7.</li>'
            '<li>The next piece: <strong>8</strong> (now up to 15). Then <strong>16</strong> '
            '(up to 31). Then <strong>32</strong> (up to 63).</li>'
            '<li>Three opened links split the chain into at most four pieces: 4, 8, 16 and '
            '32. Total: 3 + 4 + 8 + 16 + 32 = <strong>63</strong> links. Open links 5, 14 and '
            '31 and the chain falls into exactly these pieces.</li>'
            '<li>No longer chain works: with three singles and four pieces, each piece can be '
            'at most one more than everything smaller added together, so 4, 8, 16, 32 are '
            'already the biggest possible.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> with change allowed, a set of '
            'pieces pays every amount as long as each piece is at most “everything smaller, '
            'plus one”. That is why the pieces double — the same reason coins and banknotes '
            'come in 1, 2, 5, 10, and why computers count in powers of 2. Doubling is the '
            'cheapest way to reach every number.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Qaytim tufayli bu <strong>boʻlaklar</strong> haqidagi savolga aylanadi: '
            'd-kuni ertalab egadagi baʼzi boʻlaklar yigʻindisi roppa-rosa d boʻlishi kerak. '
            'Demak 1 dan zanjir uzunligigacha boʻlgan har bir son baʼzi boʻlaklar yigʻindisi '
            'boʻlishi shart.</li>'
            '<li>Uchta ochilgan halqa <strong>uchta yakka halqa</strong> beradi: ular 1, 2 va '
            '3-kechalarni toʻlaydi.</li>'
            '<li>Keyingi boʻlak 4-kechani toʻlash mumkin boʻlgan holda iloji boricha uzun '
            'boʻlsin: <strong>4</strong> halqa. Uchta yakka va 4 lik bilan 7 gacha har qanday '
            'summani toʻlash mumkin.</li>'
            '<li>Keyingi boʻlak: <strong>8</strong> (endi 15 gacha). Keyin <strong>16</strong> '
            '(31 gacha). Keyin <strong>32</strong> (63 gacha).</li>'
            '<li>Uchta ochilgan halqa zanjirni koʻpi bilan toʻrt boʻlakka ajratadi: 4, 8, 16 va '
            '32. Jami: 3 + 4 + 8 + 16 + 32 = <strong>63</strong> halqa. 5, 14 va 31-halqalarni '
            'oching — zanjir aynan shu boʻlaklarga ajraladi.</li>'
            '<li>Undan uzun zanjir ishlamaydi: uchta yakka va toʻrtta boʻlak bilan har bir '
            'boʻlak oʻzidan kichiklar yigʻindisidan koʻpi bilan bitta uzun boʻla oladi, demak '
            '4, 8, 16, 32 — mumkin boʻlgan eng kattalari.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> qaytim mumkin boʻlsa, har bir boʻlak '
            '«oʻzidan kichiklarning hammasi, plyus bir»dan oshmasa, boʻlaklar har qanday '
            'summani toʻlaydi. Shuning uchun boʻlaklar ikki baravar oʻsadi — tangalar va pullar '
            '1, 2, 5, 10 boʻlib chiqarilishi va kompyuterlar 2 ning darajalarida sanashining '
            'sababi ham shu. Ikki baravar oshirish — har bir songa yetishning eng arzon '
            'yoʻli.</p>',
    },

    {
        'number': 32, 'round': 8, 'category': 'numbers', 'difficulty': 5,
        'title':    'Five Merchants and the Apples',
        'title_uz': 'Besh savdogar va olmalar',
        'teaser':    'Five secret night-time shares, one apple to the donkey each time. How many apples?',
        'teaser_uz': 'Tunda besh marta yashirincha ulush, har safar bitta olma eshakka. Nechta olma boʻlgan?',

        'body':
            '<p>Five merchants share a room in a caravanserai, with a great pile of apples '
            'they bought together. They agree to divide it in the morning and go to sleep.</p>'
            '<p>In the night the first merchant wakes up, does not trust the others, and '
            'divides the pile into five equal heaps — with <strong>one apple left '
            'over</strong>, which he throws to the donkey at the door. He hides his own heap, '
            'pushes the other four back together, and goes to sleep.</p>'
            '<p>Then the second merchant wakes and does exactly the same with what is left: '
            'five equal heaps, one apple over to the donkey, hides one heap. Then the third, '
            'the fourth and the fifth — each finds exactly one apple left over.</p>'
            + fig(row(['🍎', '🍎', '🍎', '🍎', '🍎', '🫏'], box=False, glyph_size=26),
                  'Five equal heaps every time, and one apple to the donkey.')
            + '<p>In the morning the five, looking innocent, divide what remains into five '
            'equal heaps — and this time it divides <strong>exactly</strong>, with nothing '
            'left for the donkey.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🍎</span>'
            '<span>Apples are never cut. Every division is into five equal whole heaps, with '
            'one left over at night and none left over in the morning.</span></div>'
            '<p class="lg-ask">Answer to type: the <strong>smallest number of apples</strong> '
            'the pile could have had at the start.</p>',

        'body_uz':
            '<p>Besh savdogar karvonsaroyda bitta xonada tunashmoqda, yonlarida birgalikda '
            'sotib olgan katta uyum olma bor. Ular ertalab boʻlishga kelishib, uxlashga '
            'yotishadi.</p>'
            '<p>Tunda birinchi savdogar uygʻonadi, boshqalarga ishonmay, uyumni beshta teng '
            'uyumchaga boʻladi — <strong>bitta olma ortib qoladi</strong>, uni eshik oldidagi '
            'eshakka tashlaydi. Oʻz ulushini yashiradi, qolgan toʻrttasini yana birlashtirib, '
            'uxlaydi.</p>'
            '<p>Keyin ikkinchi savdogar uygʻonib, qolgani bilan aynan shunday qiladi: beshta '
            'teng uyumcha, bitta olma eshakka, bitta uyumchani yashiradi. Keyin uchinchi, '
            'toʻrtinchi va beshinchisi — har biri roppa-rosa bitta ortiqcha olma topadi.</p>'
            + fig(row(['🍎', '🍎', '🍎', '🍎', '🍎', '🫏'], box=False, glyph_size=26),
                  'Har safar beshta teng uyumcha va bitta olma eshakka.')
            + '<p>Ertalab beshovlon oʻzini hech narsa boʻlmagandek tutib, qolganini beshta teng '
            'uyumchaga boʻlishadi — bu safar u <strong>qoldiqsiz</strong> boʻlinadi, eshakka '
            'hech narsa qolmaydi.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🍎</span>'
            '<span>Olmalar hech qachon kesilmaydi. Har bir boʻlish beshta teng butun '
            'uyumchaga: tunda bitta qoldiq bilan, ertalab qoldiqsiz.</span></div>'
            '<p class="lg-ask">Javob sifatida yozing: uyumda boshida boʻlishi mumkin boʻlgan '
            '<strong>eng kam olmalar soni</strong>.</p>',

        'hint':    'Lend the pile four imaginary apples. Then every night-time division is '
                   'exact, and each merchant takes exactly a fifth of the bigger pile.',
        'hint_uz': 'Uyumga toʻrtta xayoliy olmani qarzga bering. Shunda tungi har bir boʻlish '
                   'qoldiqsiz boʻladi va har bir savdogar kattaroq uyumning roppa-rosa beshdan '
                   'birini oladi.',

        'answer_key': '3121',
        'accepted': ['3121 apples', '3121 ta', '3121 olma', '3121 ta olma',
                     'uch ming bir yuz yigirma bir', 'three thousand one hundred twenty one',
                     'three thousand one hundred and twenty-one'],
        'answer_hint':    'a number of apples',
        'answer_hint_uz': 'olmalar soni',

        'solution':
            '<ol class="lg-steps">'
            '<li>Call the starting pile N. Each night a merchant needs “N − 1 divisible by 5”, '
            'then leaves four fifths of N − 1.</li>'
            '<li><strong>The ghost apples:</strong> add 4 imaginary apples, making N + 4. If '
            'N leaves remainder 1 when divided by 5, then N + 4 divides exactly. And what is '
            'left after the merchant’s turn, plus the 4 ghosts, is exactly '
            '<strong>⅘ of (N + 4)</strong>. Check: ⅘(N − 1) + 4 = ⅘(N + 4).</li>'
            '<li>So with the ghosts, every night simply multiplies the pile by ⅘. After five '
            'nights the pile plus ghosts is (N + 4) × (⅘)<sup>5</sup> = (N + 4) × '
            '1024/3125.</li>'
            '<li>That must be a whole number, and 1024 shares no factor with 3125, so '
            '<strong>N + 4 must be a multiple of 3125</strong>. The smallest: N + 4 = 3125, '
            'N = <strong>3121</strong>.</li>'
            '<li>Check the morning: 3125 × 1024/3125 = 1024, minus the 4 ghosts = '
            '<strong>1020</strong> apples, and 1020 ÷ 5 = 204 exactly. ✔ (Night by night: '
            '3121 → 2496 → 1996 → 1596 → 1276 → 1020.)</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> when every step has an annoying '
            '“minus one”, shift the whole problem by a constant until the annoyance '
            'disappears. Four ghost apples turn five messy divisions into one clean '
            'multiplication. Mathematicians call this a change of variable; it is the same '
            'move as measuring temperatures from absolute zero, and it cracks problems that '
            'look like pure trial and error.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Boshlangʻich uyumni N deylik. Har kecha savdogarga «N − 1 beshga boʻlinadi» '
            'kerak, keyin u N − 1 ning beshdan toʻrtini qoldiradi.</li>'
            '<li><strong>Xayoliy olmalar:</strong> 4 ta xayoliy olma qoʻshing — N + 4 boʻladi. '
            'Agar N ni beshga boʻlganda 1 qoldiq qolsa, N + 4 qoldiqsiz boʻlinadi. Savdogar '
            'navbatidan keyin qolgani plyus 4 ta xayoliy olma esa roppa-rosa '
            '<strong>(N + 4) ning ⅘ qismi</strong>. Tekshiring: ⅘(N − 1) + 4 = ⅘(N + 4).</li>'
            '<li>Demak xayoliy olmalar bilan har kecha uyum shunchaki ⅘ ga koʻpaytiriladi. '
            'Besh kechadan keyin uyum plyus xayoliylar (N + 4) × (⅘)<sup>5</sup> = (N + 4) × '
            '1024/3125.</li>'
            '<li>Bu butun son boʻlishi shart, 1024 bilan 3125 ning esa umumiy boʻluvchisi yoʻq, '
            'demak <strong>N + 4 soni 3125 ga karrali</strong> boʻlishi kerak. Eng kichigi: '
            'N + 4 = 3125, N = <strong>3121</strong>.</li>'
            '<li>Ertalabni tekshiramiz: 3125 × 1024/3125 = 1024, minus 4 ta xayoliy = '
            '<strong>1020</strong> ta olma, 1020 ÷ 5 = 204 — qoldiqsiz. ✔ (Kechama-kecha: '
            '3121 → 2496 → 1996 → 1596 → 1276 → 1020.)</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> har bir qadamda gʻashga tegadigan '
            '«minus bir» boʻlsa, butun masalani u yoʻqolguncha biror oʻzgarmas songa suring. '
            'Toʻrtta xayoliy olma beshta chalkash boʻlishni bitta toza koʻpaytirishga '
            'aylantiradi. Matematiklar buni oʻzgaruvchini almashtirish deydi; bu haroratni '
            'mutlaq noldan oʻlchash bilan bir xil harakat va sof tanlash bilan yechiladigandek '
            'koʻringan masalalarni ochib beradi.</p>',
    },
]
