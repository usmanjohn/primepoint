"""Logic Arena — puzzles 17-24 (season 2, rounds 1-4).

Season 1 ended on 2026-09-07 and the Arena stood empty for four weeks, so
season 2 has its own schedule rather than continuing season 1's: round 1 opens
on Monday 2026-10-05. Puzzles 25-32 (rounds 5-8) are in
`_puzzles_logic_25_32.py`, which carries the same SCHEDULE.

Weighing is rested this season (season 1 used it four times). Every answer key
was recomputed independently by `verify_logic_17_32.py` before import.
"""
from logic.figures import clockface, fig, river, row, tiles

SCHEDULE = {
    'start':  '2026-10-05 09:00',
    'days':   7,
    'window': 7,
}


PUZZLES = [

    # ── Round 1 ─────────────────────────────────────────────────────────────
    {
        'number': 17, 'round': 1, 'category': 'numbers', 'difficulty': 2,
        'title':    'Seventeen Camels',
        'title_uz': 'Oʻn yetti tuya',
        'teaser':    'Half, a third and a ninth of 17 camels — and nobody wants to cut a camel.',
        'teaser_uz': '17 tuyaning yarmi, uchdan biri va toʻqqizdan biri — tuyani esa hech kim kesmoqchi emas.',

        'body':
            '<p>An old story told in every caravanserai from Bukhara to Baghdad: a merchant '
            'dies and leaves <strong>17 camels</strong> to his three sons. His will is clear. '
            'The eldest gets <strong>half</strong> of the camels, the middle son a '
            '<strong>third</strong>, and the youngest a <strong>ninth</strong>.</p>'
            '<p>The brothers stare at the number. Half of 17 is eight and a half. A third is '
            'five and two thirds. Nobody is going to cut a camel.</p>'
            + fig(row(['🐪'] * 9, box=False, glyph_size=26),
                  'Seventeen camels (only nine fit in the picture). None of them divides.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">📜</span>'
              '<span>Every son must receive a <strong>whole number</strong> of camels, no son may '
              'get <strong>less</strong> than the will promises him, and no camel may be '
              'harmed.</span></div>'
            '<p>A wise old woman rides past on her own camel, listens, and settles it in a '
            'minute — and she rides home on the same camel she came on.</p>'
            '<p class="lg-ask">Answer to type: how many camels the <strong>middle '
            'son</strong> receives.</p>',

        'body_uz':
            '<p>Buxorodan Bagʻdodgacha har bir karvonsaroyda aytiladigan eski rivoyat: bir '
            'savdogar vafot etib, uch oʻgʻliga <strong>17 ta tuya</strong> qoldiradi. Vasiyati '
            'aniq: katta oʻgʻilga tuyalarning <strong>yarmi</strong>, oʻrtanchaga '
            '<strong>uchdan biri</strong>, kenjasiga esa <strong>toʻqqizdan biri</strong>.</p>'
            '<p>Aka-ukalar songa tikilib qolishadi. 17 ning yarmi — sakkiz yarim. Uchdan biri '
            '— besh butun uchdan ikki. Tuyani hech kim kesmaydi-ku.</p>'
            + fig(row(['🐪'] * 9, box=False, glyph_size=26),
                  'Oʻn yetti tuya (rasmga faqat toʻqqiztasi sigʻdi). Hech biri boʻlinmaydi.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">📜</span>'
              '<span>Har bir oʻgʻil <strong>butun son</strong> miqdorida tuya olishi, hech bir '
              'oʻgʻil vasiyatda vaʼda qilinganidan <strong>kam</strong> olmasligi va birorta '
              'tuyaga zarar yetmasligi shart.</span></div>'
            '<p>Yonidan oʻz tuyasida keksa, dono bir ayol oʻtib qoladi. U gapni eshitib, bir '
            'daqiqada masalani hal qiladi — va uyiga oʻzi kelgan tuyada qaytib ketadi.</p>'
            '<p class="lg-ask">Javob sifatida yozing: <strong>oʻrtancha oʻgʻil</strong> nechta '
            'tuya oladi.</p>',

        'hint':    'Add the three fractions of the will together before you divide anything.',
        'hint_uz': 'Biror narsani boʻlishdan oldin vasiyatdagi uchta kasrni qoʻshib koʻring.',

        'answer_key': '6',
        'accepted': ['6 camels', '6 ta', '6 tuya', '6 ta tuya', 'olti', 'six'],
        'answer_hint':    'a number of camels',
        'answer_hint_uz': 'tuyalar soni',

        'solution':
            '<ol class="lg-steps">'
            '<li>The woman <strong>lends her own camel</strong>. Now there are '
            '<strong>18</strong>.</li>'
            '<li>Half of 18 is <strong>9</strong> — to the eldest.</li>'
            '<li>A third of 18 is <strong>6</strong> — to the middle son.</li>'
            '<li>A ninth of 18 is <strong>2</strong> — to the youngest.</li>'
            '<li>9 + 6 + 2 = <strong>17</strong>. One camel is left over: her own. She takes '
            'it back and rides home.</li>'
            '<li>Why does it work? Add the will: ½ + ⅓ + ⅑ = 9/18 + 6/18 + 2/18 = '
            '<strong>17/18</strong>. The father never gave away the whole herd — exactly '
            'one eighteenth was always spare. With 18 camels that spare part is one whole '
            'camel, and it is the borrowed one.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> before you fight with the '
            'numbers, check whether the parts really add up to the whole. Here they add up '
            'to 17/18, and that missing eighteenth is the entire puzzle. Each son even gets a '
            'little <em>more</em> than the will literally says (9 instead of 8½), and nobody '
            'complains — and since 9 + 6 + 2 is already 17, no other split could give everyone '
            'at least their promise. Checking that the pieces add up is the first step in every budget, '
            'every recipe and every pie chart.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Ayol <strong>oʻz tuyasini qarzga beradi</strong>. Endi tuyalar '
            '<strong>18 ta</strong>.</li>'
            '<li>18 ning yarmi — <strong>9</strong>, katta oʻgʻilga.</li>'
            '<li>18 ning uchdan biri — <strong>6</strong>, oʻrtanchaga.</li>'
            '<li>18 ning toʻqqizdan biri — <strong>2</strong>, kenjaga.</li>'
            '<li>9 + 6 + 2 = <strong>17</strong>. Bitta tuya ortib qoladi — oʻsha ayolning '
            'oʻzi. U tuyasini qaytarib olib, uyiga ketadi.</li>'
            '<li>Nega bu ishlaydi? Vasiyatni qoʻshib koʻring: ½ + ⅓ + ⅑ = 9/18 + 6/18 + 2/18 '
            '= <strong>17/18</strong>. Ota butun podani hech qachon taqsimlamagan — aniq '
            'oʻn sakkizdan bir qismi doim ortiqcha edi. 18 ta tuyada oʻsha qism roppa-rosa '
            'bitta tuya boʻladi, u ham qarzga olingani.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> sonlar bilan olishishdan oldin, '
            'qismlar haqiqatan ham butunni tashkil etadimi — tekshiring. Bu yerda ular 17/18 '
            'ni beradi va yetishmayotgan oʻsha oʻn sakkizdan bir butun jumboqning oʻzi. Har '
            'bir oʻgʻil vasiyatda yozilganidan hatto biroz <em>koʻproq</em> oladi (8½ oʻrniga '
            '9) va hech kim norozi boʻlmaydi — 9 + 6 + 2 allaqachon 17 boʻlgani uchun, hammaga '
            'vaʼdasidan kam bermaydigan boshqa taqsimot yoʻq. Qismlar yigʻindisini tekshirish — har qanday '
            'byudjet, retsept va doiraviy diagrammaning birinchi qadami.</p>',
    },

    {
        'number': 18, 'round': 1, 'category': 'strategy', 'difficulty': 4,
        'title':    'Two Bowls from Rishton',
        'title_uz': 'Rishtondan ikki kosa',
        'teaser':    'A hundred heights, only two test bowls. How few drops guarantee the answer?',
        'teaser_uz': 'Yuzta balandlik, faqat ikkita sinov kosasi. Kamida necha marta tashlash kerak?',

        'body':
            '<p>A potter in Rishton has invented a new, extra-hard glaze. To prove it, she '
            'builds a test frame with <strong>100 shelves</strong>, numbered 1 (lowest) to '
            '100 (highest), and drops bowls onto a stone floor.</p>'
            '<p>There is some lowest shelf from which the bowl breaks — or perhaps it '
            'survives even from shelf 100. A bowl that breaks from one shelf would also break '
            'from every higher shelf. A bowl that survives a drop is unharmed and can be '
            'dropped again.</p>'
            + fig(row(['🏺', '🏺'], ['bowl 1', 'bowl 2'], glyph_size=30),
                  'Only two bowls of the new glaze exist. Once both are broken, the test is over.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🏺</span>'
              '<span>She has only <strong>two</strong> test bowls. She must find the exact '
              'lowest breaking shelf (or learn that there is none) with certainty, however '
              'unlucky she is.</span></div>'
            '<p>With one bowl she would have to climb shelf by shelf: up to 100 drops. With '
            'two bowls she can be much smarter — but how much?</p>'
            '<p class="lg-ask">Answer to type: the smallest number of drops that is '
            '<strong>guaranteed</strong> to be enough, in the worst case.</p>',

        'body_uz':
            '<p>Rishtonlik bir kulolchi ayol yangi, oʻta mustahkam sir (kosa ustidagi yaltiroq '
            'qoplama) ixtiro qildi. Buni isbotlash uchun u <strong>100 ta tokchali</strong> '
            'sinov javonini yasadi: tokchalar pastdan 1 dan 100 gacha raqamlangan. Kosalar '
            'tosh polga tashlanadi.</p>'
            '<p>Shunday eng past tokcha borki, undan tashlangan kosa sinadi — yoki kosa hatto '
            '100-tokchadan ham butun qolar. Biror tokchadan sinadigan kosa undan baland har '
            'qanday tokchadan ham sinadi. Butun qolgan kosaga hech narsa boʻlmaydi, uni yana '
            'tashlash mumkin.</p>'
            + fig(row(['🏺', '🏺'], ['1-kosa', '2-kosa'], glyph_size=30),
                  'Yangi sirli kosadan atigi ikkitasi bor. Ikkalasi ham sinsa, sinov tugaydi.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🏺</span>'
              '<span>Uning atigi <strong>ikkita</strong> sinov kosasi bor. U kosa sinadigan '
              'eng past tokchani (yoki bunday tokcha yoʻqligini) aniq topishi shart — omadi '
              'qanchalik kelmasa ham.</span></div>'
            '<p>Bitta kosa bilan u tokchama-tokcha koʻtarilishi kerak edi: 100 martagacha '
            'tashlash. Ikkita kosa bilan ancha aqlliroq ish tutish mumkin — lekin qanchalik?</p>'
            '<p class="lg-ask">Javob sifatida yozing: eng yomon holatda ham '
            '<strong>albatta</strong> yetadigan eng kam tashlashlar soni.</p>',

        'hint':    'If your first drop is from shelf k and the bowl breaks, the second bowl '
                   'must climb one shelf at a time below k. So make each jump one shelf '
                   'shorter than the last.',
        'hint_uz': 'Birinchi marta k-tokchadan tashlasangiz va kosa sinsa, ikkinchi kosa k '
                   'dan pastda bittadan koʻtarilishi kerak. Demak har bir sakrash oldingisidan '
                   'bir tokcha qisqa boʻlsin.',

        'answer_key': '14',
        'accepted': ['14 drops', '14 marta', '14 ta', 'oʻn toʻrt', "o'n to'rt", 'fourteen'],
        'answer_hint':    'a number of drops',
        'answer_hint_uz': 'tashlashlar soni',

        'solution':
            '<ol class="lg-steps">'
            '<li>Think about the first bowl as a <strong>scout</strong> that jumps upward, '
            'and the second as a <strong>searcher</strong> that walks one shelf at a time '
            'through the gap the scout leaves behind.</li>'
            '<li>Suppose you are allowed <strong>n</strong> drops. Drop the scout first from '
            'shelf <strong>n</strong>. If it breaks, the searcher checks shelves 1, 2, … , '
            'n − 1: at most n drops in total.</li>'
            '<li>If it survives, you have used one drop, so the next jump may only be '
            '<strong>n − 1</strong> shelves high: drop from n + (n − 1). Then jump n − 2, '
            'then n − 3 … Each time the total stays within n.</li>'
            '<li>So n drops can cover n + (n − 1) + … + 2 + 1 = n(n + 1)/2 shelves.</li>'
            '<li>With n = 13 that is 91 shelves — not enough. With n = 14 it is '
            '<strong>105 ≥ 100</strong>. So 14 drops suffice: first from 14, then 27, 39, 50, '
            '60, 69, 77, 84, 90, 95, 99, 100.</li>'
            '<li>And 13 can never be enough: whatever plan you use, 13 drops with two bowls '
            'can tell apart at most 91 shelves, as the same counting shows. So the answer is '
            '<strong>14</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> balance the worst cases. Jumping '
            'by a fixed 10 (10, 20, 30…) feels sensible but costs up to 19 drops, because a '
            'break late in the climb leaves you as much walking as a break early on. Making '
            'each jump one shorter means that whenever the scout breaks, the total is the '
            'same. Engineers use exactly this idea to test a long list of software versions '
            'for the one where a bug first appeared.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Birinchi kosani yuqoriga sakrab boradigan <strong>razvedkachi</strong>, '
            'ikkinchisini esa razvedkachi qoldirgan oraliqni bittadan tekshiradigan '
            '<strong>izlovchi</strong> deb tasavvur qiling.</li>'
            '<li>Sizga <strong>n</strong> marta tashlash ruxsat berilgan boʻlsin. Razvedkachini '
            'avval <strong>n</strong>-tokchadan tashlang. Sinsa, izlovchi 1, 2, … , n − 1 '
            'tokchalarni tekshiradi: jami koʻpi bilan n marta.</li>'
            '<li>Agar butun qolsa, bitta urinish sarflandi, demak keyingi sakrash atigi '
            '<strong>n − 1</strong> tokcha boʻlishi mumkin: n + (n − 1) dan tashlang. Keyin '
            'n − 2, keyin n − 3 … Har safar jami n dan oshmaydi.</li>'
            '<li>Demak n marta tashlash n + (n − 1) + … + 2 + 1 = n(n + 1)/2 ta tokchani '
            'qamraydi.</li>'
            '<li>n = 13 da bu 91 tokcha — yetmaydi. n = 14 da <strong>105 ≥ 100</strong>. Demak '
            '14 marta yetadi: avval 14 dan, keyin 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, '
            '100 dan.</li>'
            '<li>13 marta esa hech qachon yetmaydi: qanday reja tuzmang, ikki kosa bilan 13 '
            'marta tashlash koʻpi bilan 91 ta tokchani ajrata oladi — xuddi shu sanash '
            'koʻrsatadi. Javob: <strong>14</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> eng yomon holatlarni tenglashtiring. '
            'Har safar 10 tadan sakrash (10, 20, 30…) maʼqul tuyuladi, lekin 19 martagacha '
            'tashlashga olib keladi: yuqorida sinsa, pastda singandagidek koʻp yurish qoladi. '
            'Har sakrashni bittaga qisqartirsangiz, razvedkachi qayerda sinmasin, jami bir xil '
            'boʻladi. Muhandislar xuddi shu gʻoya bilan dasturning uzun versiyalar roʻyxatidan '
            'xato birinchi paydo boʻlgan versiyani topishadi.</p>',
    },

    # ── Round 2 ─────────────────────────────────────────────────────────────
    {
        'number': 19, 'round': 2, 'category': 'shapes', 'difficulty': 3,
        'title':    'Rectangles in the Tile Panel',
        'title_uz': 'Koshin panodagi toʻrtburchaklar',
        'teaser':    'Twenty-five blue tiles. How many rectangles are hiding in them?',
        'teaser_uz': 'Yigirma beshta koʻk koshin. Ularda nechta toʻgʻri toʻrtburchak yashiringan?',

        'body':
            '<p>A master tiler sets a square panel of <strong>25 blue tiles</strong>, five by '
            'five, into the wall of a new madrasa courtyard. His apprentice, bored, starts '
            'counting rectangles.</p>'
            '<p>A rectangle here means any block of whole tiles that forms a rectangle: a '
            'single tile counts, a row of three counts, a 2 × 4 block counts, and the whole '
            '5 × 5 panel counts. Squares are rectangles too.</p>'
            + fig(tiles(5, 5, mark=(1, 1, 2, 3)),
                  'The 5 × 5 panel. The highlighted 2 × 3 block is one rectangle out of many.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🟦</span>'
              '<span>Count every rectangle made of whole tiles, of every size and in every '
              'position. Two rectangles are different if they cover a different set of '
              'tiles.</span></div>'
            '<p>The apprentice gave up somewhere past eighty. There is a way to count them '
            'all without listing a single one.</p>'
            '<p class="lg-ask">Answer to type: the total <strong>number of '
            'rectangles</strong>.</p>',

        'body_uz':
            '<p>Usta koshinkor yangi madrasa hovlisi devoriga beshga besh, '
            '<strong>25 ta koʻk koshindan</strong> iborat kvadrat pano oʻrnatdi. Zerikkan '
            'shogirdi toʻgʻri toʻrtburchaklarni sanay boshladi.</p>'
            '<p>Bu yerda toʻgʻri toʻrtburchak — butun koshinlardan tuzilgan, toʻgʻri '
            'toʻrtburchak shaklidagi har qanday blok: bitta koshin ham, uchta koshinli qator '
            'ham, 2 × 4 blok ham, butun 5 × 5 pano ham hisoblanadi. Kvadratlar ham toʻgʻri '
            'toʻrtburchak.</p>'
            + fig(tiles(5, 5, mark=(1, 1, 2, 3)),
                  '5 × 5 pano. Ajratilgan 2 × 3 blok — koʻplab toʻrtburchaklardan biri.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🟦</span>'
              '<span>Butun koshinlardan tuzilgan har bir toʻgʻri toʻrtburchakni sanang — '
              'har qanday oʻlchamda va har qanday joyda. Ikki toʻrtburchak turli koshinlarni '
              'egallasa, ular har xil hisoblanadi.</span></div>'
            '<p>Shogird saksondan oʻtganda taslim boʻldi. Ularni bittasini ham roʻyxatga '
            'olmasdan sanashning yoʻli bor.</p>'
            '<p class="lg-ask">Javob sifatida yozing: <strong>toʻgʻri toʻrtburchaklarning '
            'umumiy soni</strong>.</p>',

        'hint':    'Do not look at the tiles — look at the lines between them. A rectangle is '
                   'decided by which lines form its edges.',
        'hint_uz': 'Koshinlarga emas, ular orasidagi chiziqlarga qarang. Toʻrtburchakni qaysi '
                   'chiziqlar uning chegarasi ekani belgilaydi.',

        'answer_key': '225',
        'accepted': ['225 rectangles', '225 ta', 'ikki yuz yigirma besh', 'two hundred twenty five',
                     'two hundred and twenty-five'],
        'answer_hint':    'a whole number',
        'answer_hint_uz': 'butun son',

        'solution':
            '<ol class="lg-steps">'
            '<li>A 5 × 5 panel is drawn with <strong>6 vertical lines</strong> and '
            '<strong>6 horizontal lines</strong> (five tiles need six lines).</li>'
            '<li>Every rectangle has a left edge and a right edge — two of the 6 vertical '
            'lines — and a top and a bottom — two of the 6 horizontal lines.</li>'
            '<li>And every such choice gives exactly one rectangle. So we only need to count '
            'choices.</li>'
            '<li>Two lines out of six: 6 × 5 ÷ 2 = <strong>15</strong> ways. That holds for the '
            'vertical pair and for the horizontal pair.</li>'
            '<li>15 × 15 = <strong>225</strong> rectangles.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> when the objects are hard to '
            'count, count the <em>decisions</em> that make them. A rectangle is not 1, 2 or 6 '
            'tiles — it is a choice of two lines and two lines. Turning "list everything" '
            'into "count the choices" is the heart of combinatorics, and it is how a '
            'programmer knows a search will take a second or a century before running it.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>5 × 5 pano <strong>6 ta tik</strong> va <strong>6 ta yotiq chiziq</strong> '
            'bilan chiziladi (beshta koshinga oltita chiziq kerak).</li>'
            '<li>Har bir toʻrtburchakning chap va oʻng cheti bor — 6 ta tik chiziqdan '
            'ikkitasi — hamda usti va osti bor — 6 ta yotiq chiziqdan ikkitasi.</li>'
            '<li>Va har bir bunday tanlov aynan bitta toʻrtburchakni beradi. Demak faqat '
            'tanlovlarni sanash kifoya.</li>'
            '<li>Oltitadan ikkita chiziq: 6 × 5 ÷ 2 = <strong>15</strong> usul. Bu tik juftlik '
            'uchun ham, yotiq juftlik uchun ham shunday.</li>'
            '<li>15 × 15 = <strong>225</strong> ta toʻgʻri toʻrtburchak.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> narsalarni sanash qiyin boʻlsa, '
            'ularni yaratadigan <em>qarorlarni</em> sanang. Toʻrtburchak — 1, 2 yoki 6 ta '
            'koshin emas, u ikkita chiziq va yana ikkita chiziqning tanlovi. «Hammasini '
            'roʻyxatga ol»ni «tanlovlarni sana»ga aylantirish — kombinatorikaning yuragi. '
            'Dasturchi qidiruv bir soniya yoki bir asr davom etishini ishga tushirmasdan '
            'oldin shunday biladi.</p>',
    },

    {
        'number': 20, 'round': 2, 'category': 'liars', 'difficulty': 4,
        'title':    'Six Sellers at Chorsu',
        'title_uz': 'Chorsudagi olti sotuvchi',
        'teaser':    'Some always tell the truth, the rest always lie. Six sentences decide which.',
        'teaser_uz': 'Baʼzilari doim rost, qolganlari doim yolgʻon gapiradi. Olti gap kimligini hal qiladi.',

        'body':
            '<p>Six sellers stand in a row in the Chorsu bazaar, stalls numbered 1 to 6. '
            'Each of them is either <strong>honest</strong> (every sentence true) or a '
            '<strong>liar</strong> (every sentence false). You ask each one a single question '
            'and get one sentence back:</p>'
            + fig(row(['🌶️', '🍈', '🫓', '🍇', '🍯', '🔪'],
                      ['1', '2', '3', '4', '5', '6'], glyph_size=26),
                  'Spices, melons, bread, dried fruit, honey and Chust knives.')
            + '<ol>'
              '<li><strong>Spice seller (1):</strong> “The melon seller is a liar.”</li>'
              '<li><strong>Melon seller (2):</strong> “The spice seller and the honey seller '
              'are the same kind as each other.”</li>'
              '<li><strong>Bread seller (3):</strong> “The knife seller is a liar.”</li>'
              '<li><strong>Dried-fruit seller (4):</strong> “The spice seller is honest.”</li>'
              '<li><strong>Honey seller (5):</strong> “Exactly three of us six are honest.”</li>'
              '<li><strong>Knife seller (6):</strong> “The melon seller and the dried-fruit '
              'seller are different kinds.”</li>'
              '</ol>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🗣️</span>'
            '<span>“The same kind” means both honest or both liars. There is exactly one way '
            'to sort the six that makes every sentence consistent.</span></div>'
            '<p class="lg-ask">Answer to type: the <strong>sum of the stall numbers</strong> '
            'of all the honest sellers.</p>',

        'body_uz':
            '<p>Chorsu bozorida olti sotuvchi bir qatorda turibdi, rastalar 1 dan 6 gacha '
            'raqamlangan. Har biri yo <strong>rostgoʻy</strong> (har bir gapi rost), yo '
            '<strong>yolgʻonchi</strong> (har bir gapi yolgʻon). Har biriga bitta savol berib, '
            'bittadan gap eshitasiz:</p>'
            + fig(row(['🌶️', '🍈', '🫓', '🍇', '🍯', '🔪'],
                      ['1', '2', '3', '4', '5', '6'], glyph_size=26),
                  'Ziravor, qovun, non, quruq meva, asal va Chust pichoqlari.')
            + '<ol>'
              '<li><strong>Ziravorchi (1):</strong> «Qovunchi — yolgʻonchi.»</li>'
              '<li><strong>Qovunchi (2):</strong> «Ziravorchi bilan asalchi bir xil '
              'toifada.»</li>'
              '<li><strong>Novvoy (3):</strong> «Pichoqchi — yolgʻonchi.»</li>'
              '<li><strong>Quruq mevachi (4):</strong> «Ziravorchi — rostgoʻy.»</li>'
              '<li><strong>Asalchi (5):</strong> «Oltovimizdan roppa-rosa uchtasi '
              'rostgoʻy.»</li>'
              '<li><strong>Pichoqchi (6):</strong> «Qovunchi bilan quruq mevachi har xil '
              'toifada.»</li>'
              '</ol>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🗣️</span>'
            '<span>«Bir xil toifada» — ikkalasi ham rostgoʻy yoki ikkalasi ham yolgʻonchi '
            'degani. Oltovini har bir gap mos keladigan qilib ajratishning yagona yoʻli '
            'bor.</span></div>'
            '<p class="lg-ask">Javob sifatida yozing: barcha rostgoʻy sotuvchilar rasta '
            'raqamlarining <strong>yigʻindisi</strong>.</p>',

        'hint':    'Two of the sentences tie sellers together in pairs. Use them to show that '
                   'one sentence is true no matter what.',
        'hint_uz': 'Ikki gap sotuvchilarni juft-juft bogʻlaydi. Shular yordamida bitta gap har '
                   'qanday holatda ham rost ekanini koʻrsating.',

        'answer_key': '8',
        'accepted': ['sakkiz', 'eight'],
        'answer_hint':    'a sum of stall numbers',
        'answer_hint_uz': 'rasta raqamlari yigʻindisi',

        'solution':
            '<ol class="lg-steps">'
            '<li>Seller 4 says “1 is honest”. If 4 is honest, 1 is honest; if 4 is a liar, 1 '
            'is a liar. So <strong>1 and 4 are the same kind</strong>.</li>'
            '<li>Seller 1 says “2 is a liar”. By the same reasoning, <strong>1 and 2 are '
            'different kinds</strong>. So 2 and 4 are different kinds too.</li>'
            '<li>That is exactly what seller 6 claims. Seller 6’s sentence is true, so '
            '<strong>6 is honest</strong>.</li>'
            '<li>Seller 3 says “6 is a liar” — false. So <strong>3 is a liar</strong>.</li>'
            '<li>Now try <strong>1 honest</strong>: then 4 honest, 2 a liar. Liar 2’s sentence '
            'is false, so 1 and 5 differ: 5 is a liar. Honest: 1, 4, 6 — exactly three. But '
            'then 5’s sentence is true, and 5 is a liar. <strong>Contradiction.</strong></li>'
            '<li>So <strong>1 is a liar</strong>: 4 a liar, 2 honest. Honest 2 says 1 and 5 '
            'match, so 5 is a liar. Honest: <strong>2 and 6</strong> — two people, so 5’s '
            '“exactly three” is indeed false. Everything fits.</li>'
            '<li>2 + 6 = <strong>8</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> a sentence about another person '
            'is really a <em>link</em>: “X is honest” spoken by Y means X and Y are the same '
            'kind, and “X is a liar” means they differ. Turn the sentences into links and the '
            'crowd falls into two teams; then one test case finishes it. The same idea — '
            'tracking “same” and “different” — is how a computer checks whether a map can be '
            'coloured with two colours.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>4-sotuvchi «1 rostgoʻy» deydi. 4 rostgoʻy boʻlsa, 1 ham rostgoʻy; 4 '
            'yolgʻonchi boʻlsa, 1 ham yolgʻonchi. Demak <strong>1 va 4 bir xil '
            'toifada</strong>.</li>'
            '<li>1-sotuvchi «2 yolgʻonchi» deydi. Xuddi shu mulohaza bilan <strong>1 va 2 har '
            'xil toifada</strong>. Demak 2 va 4 ham har xil.</li>'
            '<li>6-sotuvchi aynan shuni aytyapti. Uning gapi rost, demak <strong>6 '
            'rostgoʻy</strong>.</li>'
            '<li>3-sotuvchi «6 yolgʻonchi» deydi — bu yolgʻon. Demak <strong>3 '
            'yolgʻonchi</strong>.</li>'
            '<li>Endi <strong>1 rostgoʻy</strong> deb faraz qilaylik: unda 4 rostgoʻy, 2 '
            'yolgʻonchi. Yolgʻonchi 2 ning gapi yolgʻon, demak 1 va 5 har xil: 5 yolgʻonchi. '
            'Rostgoʻylar: 1, 4, 6 — roppa-rosa uchta. Unda 5 ning gapi rost boʻlib chiqadi, '
            'vaholanki 5 yolgʻonchi. <strong>Qarama-qarshilik.</strong></li>'
            '<li>Demak <strong>1 yolgʻonchi</strong>: 4 yolgʻonchi, 2 rostgoʻy. Rostgoʻy 2 '
            '«1 va 5 bir xil» deydi, demak 5 yolgʻonchi. Rostgoʻylar: <strong>2 va 6</strong> '
            '— ikki kishi, shuning uchun 5 ning «roppa-rosa uchta» degani haqiqatan yolgʻon. '
            'Hammasi mos keldi.</li>'
            '<li>2 + 6 = <strong>8</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> boshqa odam haqidagi gap aslida '
            '<em>bogʻlanish</em>: Y aytgan «X rostgoʻy» — X va Y bir xil toifada degani, '
            '«X yolgʻonchi» esa ular har xil degani. Gaplarni bogʻlanishlarga aylantirsangiz, '
            'olomon ikki jamoaga boʻlinadi; keyin bitta sinov hammasini hal qiladi. «Bir xil» '
            'va «har xil»ni kuzatib borish gʻoyasi bilan kompyuter xaritani ikki rangda '
            'boʻyash mumkinmi-yoʻqmi, tekshiradi.</p>',
    },

    # ── Round 3 ─────────────────────────────────────────────────────────────
    {
        'number': 21, 'round': 3, 'category': 'crossing', 'difficulty': 2,
        'title':    'The Little Boat',
        'title_uz': 'Kichkina qayiq',
        'teaser':    'Three grown-ups, two children, a boat that holds 80 kg.',
        'teaser_uz': 'Uchta katta, ikkita bola va 80 kg koʻtaradigan qayiq.',

        'body':
            '<p>A family on holiday in the mountains needs to cross a river. The only boat '
            'is a little rowing boat that carries at most <strong>80 kg</strong>.</p>'
            '<p>Grandpa weighs 80 kg, Dad 76 kg and Mum 64 kg. Jasur weighs 40 kg and his '
            'sister Afsona 36 kg. Everybody can row.</p>'
            + fig(river(['👴', '👨', '👩', '👦', '👧'], [], '🚣',
                        'start', 'goal'),
                  'Five people, one small boat. The boat cannot cross by itself.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⚖️</span>'
              '<span>At most <strong>80 kg</strong> in the boat on each crossing, and at least '
              'one person must be in it to row. Each one-way trip counts as one '
              'crossing.</span></div>'
            '<p>Check the numbers: no grown-up can share the boat with anybody. That sounds '
            'hopeless — it is not.</p>'
            '<p class="lg-ask">Answer to type: the smallest number of '
            '<strong>crossings</strong> needed to get all five across.</p>',

        'body_uz':
            '<p>Togʻda dam olayotgan oila daryodan oʻtishi kerak. Yagona qayiq — koʻpi bilan '
            '<strong>80 kg</strong> koʻtaradigan kichkina eshkak qayiq.</p>'
            '<p>Bobo 80 kg, dada 76 kg, oyi 64 kg. Jasur 40 kg, singlisi Afsona esa 36 kg. '
            'Hamma eshkak eshishni biladi.</p>'
            + fig(river(['👴', '👨', '👩', '👦', '👧'], [], '🚣',
                        'boshlanish', 'manzil'),
                  'Besh kishi, bitta kichkina qayiq. Qayiq oʻz-oʻzidan suzmaydi.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⚖️</span>'
              '<span>Har bir suzishda qayiqda koʻpi bilan <strong>80 kg</strong> boʻladi va '
              'eshkak eshish uchun kamida bitta odam boʻlishi shart. Bir tomonga har bir '
              'suzish — bitta oʻtish.</span></div>'
            '<p>Sonlarni tekshiring: birorta katta odam qayiqqa hech kim bilan sigʻmaydi. '
            'Umidsiz tuyuladi — lekin unday emas.</p>'
            '<p class="lg-ask">Javob sifatida yozing: beshovini ham narigi qirgʻoqqa '
            'oʻtkazish uchun kerak boʻladigan eng kam <strong>oʻtishlar</strong> soni.</p>',

        'hint':    'The two children together weigh 76 kg. Somebody has to bring the boat '
                   'back every time a grown-up crosses.',
        'hint_uz': 'Ikki bola birgalikda 76 kg. Har safar katta odam oʻtganda, qayiqni kimdir '
                   'qaytarib olib kelishi kerak.',

        'answer_key': '13',
        'accepted': ['13 crossings', '13 marta', '13 ta', 'oʻn uch', "o'n uch", 'thirteen'],
        'answer_hint':    'a number of crossings',
        'answer_hint_uz': 'oʻtishlar soni',

        'solution':
            '<ol class="lg-steps">'
            '<li>Jasur and Afsona cross together (76 kg). <em>1</em></li>'
            '<li>Afsona rows back. <em>2</em></li>'
            '<li>Grandpa crosses alone. <em>3</em></li>'
            '<li>Jasur rows back. Both children are again on the start bank. <em>4</em></li>'
            '<li>Those four crossings moved one grown-up. Repeat them for Dad (crossings '
            '5-8) and for Mum (9-12).</li>'
            '<li>Finally the children cross together. <em>13</em></li>'
            '<li>Why not fewer? A grown-up always crosses alone, so after each grown-up’s '
            'trip somebody must bring the boat back — and it cannot be a grown-up, or that '
            'trip was wasted. So each grown-up costs four crossings: children over, a child '
            'back, grown-up over, a child back. 3 × 4 + 1 = <strong>13</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> find the <em>shuttle</em> — a '
            'small repeated move that brings you back to the same position with one more job '
            'done — and count how many times it must run. This is how you plan anything done '
            'in rounds: a lift moving furniture, a ferry timetable, a loop in a '
            'program.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Jasur va Afsona birga oʻtadi (76 kg). <em>1</em></li>'
            '<li>Afsona qayiqni qaytarib keladi. <em>2</em></li>'
            '<li>Bobo yolgʻiz oʻtadi. <em>3</em></li>'
            '<li>Jasur qayiqni qaytarib keladi. Ikki bola yana boshlangʻich qirgʻoqda. '
            '<em>4</em></li>'
            '<li>Bu toʻrt oʻtish bitta kattani oʻtkazdi. Ularni dada uchun (5-8) va oyi uchun '
            '(9-12) takrorlang.</li>'
            '<li>Oxirida bolalar birga oʻtadi. <em>13</em></li>'
            '<li>Nega bundan kam boʻlmaydi? Katta odam doim yolgʻiz oʻtadi, demak har '
            'kattadan keyin qayiqni kimdir qaytarishi kerak — va bu katta odam boʻlolmaydi, '
            'aks holda uning suzishi behuda ketadi. Shuning uchun har bir katta toʻrt oʻtishga '
            'tushadi: bolalar oʻtadi, bitta bola qaytadi, katta oʻtadi, bitta bola qaytadi. '
            '3 × 4 + 1 = <strong>13</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> <em>mokini</em> toping — sizni '
            'avvalgi holatga qaytaradigan, lekin bitta ishni bajarib qoʻyadigan kichik '
            'takroriy harakatni — va u necha marta aylanishi kerakligini sanang. Bosqichma-'
            'bosqich bajariladigan har qanday ish shunday rejalashtiriladi: mebel tashiyotgan '
            'lift, parom jadvali, dasturdagi sikl.</p>',
    },

    {
        'number': 22, 'round': 3, 'category': 'chance', 'difficulty': 4,
        'title':    'The Shared Birthday',
        'title_uz': 'Bir kunda tugʻilganlar',
        'teaser':    'How small can a class be and still probably share a birthday?',
        'teaser_uz': 'Sinf qanchalik kichik boʻlsa ham, ehtimol ikki kishining tugʻilgan kuni bir kunga toʻgʻri keladi?',

        'body':
            '<p>Sherbek’s class has 30 pupils. One morning the teacher says: “I bet two of '
            'you share a birthday.” Sherbek laughs — there are 365 days in a year and only '
            '30 of them. Surely the teacher is likely to lose?</p>'
            '<p>They check. Afsona and a boy from the back row were both born on '
            '14 March.</p>'
            + fig(row(['🎂', '📅', '🎂'], box=False, glyph_size=30),
                  'Not the same year — just the same day and month.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🎲</span>'
              '<span>Assume every birthday is equally likely to fall on any of '
              '<strong>365</strong> days (ignore 29 February) and the pupils’ birthdays are '
              'independent.</span></div>'
            '<p>The teacher was not lucky. In fact, she would have been more likely than not '
            'to win her bet with far fewer than 30 pupils.</p>'
            '<p class="lg-ask">Answer to type: the <strong>smallest class size</strong> for '
            'which the chance that at least two pupils share a birthday is greater than '
            '50%.</p>',

        'body_uz':
            '<p>Sherbekning sinfida 30 nafar oʻquvchi bor. Bir kuni ertalab oʻqituvchi: '
            '«Garov oʻynayman, ikkitangizning tugʻilgan kuningiz bir kunga toʻgʻri keladi», '
            'deydi. Sherbek kuladi — yilda 365 kun bor, ular esa atigi 30 kishi. Oʻqituvchi '
            'yutqazsa kerak-ku?</p>'
            '<p>Tekshirishadi. Afsona va orqa partadagi bir bola ikkalasi ham 14-martda '
            'tugʻilgan ekan.</p>'
            + fig(row(['🎂', '📅', '🎂'], box=False, glyph_size=30),
                  'Bir yilda emas — faqat kuni va oyi bir xil.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🎲</span>'
              '<span>Har bir tugʻilgan kun <strong>365</strong> kunning istalganiga bir xil '
              'ehtimol bilan tushadi (29-fevralni hisobga olmang) va oʻquvchilarning tugʻilgan '
              'kunlari bir-biriga bogʻliq emas, deb hisoblang.</span></div>'
            '<p>Oʻqituvchiga omad kulib boqmadi. Aslida u 30 dan ancha kam oʻquvchi bilan ham '
            'garovni yutish ehtimoli yutqazishdan yuqori boʻlardi.</p>'
            '<p class="lg-ask">Javob sifatida yozing: kamida ikki oʻquvchining tugʻilgan kuni '
            'bir xil boʻlish ehtimoli 50% dan oshadigan <strong>eng kichik sinf '
            'hajmi</strong>.</p>',

        'hint':    'Work out the chance that nobody shares a birthday — pupil by pupil, each '
                   'one has to avoid all the birthdays before them.',
        'hint_uz': 'Hech kimning tugʻilgan kuni mos kelmaslik ehtimolini hisoblang — oʻquvchi '
                   'ketidan oʻquvchi, har biri oʻzidan oldingi barcha kunlardan qochishi kerak.',

        'answer_key': '23',
        'accepted': ['23 pupils', '23 ta', '23 nafar', '23 kishi', 'yigirma uch', 'twenty three',
                     'twenty-three'],
        'answer_hint':    'a number of pupils',
        'answer_hint_uz': 'oʻquvchilar soni',

        'solution':
            '<ol class="lg-steps">'
            '<li>Count the opposite: the chance that <strong>all birthdays are '
            'different</strong>.</li>'
            '<li>Pupil 1 can have any day. Pupil 2 must avoid one day: chance 364/365. Pupil 3 '
            'must avoid two: 363/365. And so on.</li>'
            '<li>For n pupils, “all different” = 365/365 × 364/365 × … × (366 − n)/365.</li>'
            '<li>For n = 22 this product is about 0.524 — so a shared birthday has only about '
            '47.6%.</li>'
            '<li>For n = 23 it falls to about 0.493 — a shared birthday now has about '
            '<strong>50.7%</strong>. So the answer is <strong>23</strong>. (With 30 pupils the '
            'teacher wins about 70.6% of the time.)</li>'
            '<li>Why so few? Because we are not asking about <em>your</em> birthday. 23 people '
            'make 23 × 22 ÷ 2 = <strong>253 pairs</strong>, and every pair is a fresh chance '
            'to match.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> when “at least one” is hard, '
            'compute “none” and subtract from 1. And count pairs, not people — pairs grow '
            'much faster than people. That is why computer scientists worry about two files '
            'getting the same fingerprint far sooner than intuition says.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Teskarisini hisoblaymiz: <strong>barcha tugʻilgan kunlar har xil</strong> '
            'boʻlish ehtimoli.</li>'
            '<li>1-oʻquvchi istalgan kunda tugʻilgan boʻlishi mumkin. 2-oʻquvchi bitta kundan '
            'qochishi kerak: ehtimol 364/365. 3-oʻquvchi ikkita kundan: 363/365. Va hokazo.</li>'
            '<li>n ta oʻquvchi uchun «hammasi har xil» = 365/365 × 364/365 × … × '
            '(366 − n)/365.</li>'
            '<li>n = 22 da bu koʻpaytma taxminan 0,524 — demak mos kelish ehtimoli atigi '
            'taxminan 47,6%.</li>'
            '<li>n = 23 da u taxminan 0,493 gacha tushadi — mos kelish ehtimoli endi taxminan '
            '<strong>50,7%</strong>. Javob: <strong>23</strong>. (30 oʻquvchi bilan oʻqituvchi '
            'taxminan 70,6% hollarda yutadi.)</li>'
            '<li>Nega bunchalik kam? Chunki gap <em>sizning</em> tugʻilgan kuningiz haqida '
            'emas. 23 kishi 23 × 22 ÷ 2 = <strong>253 ta juftlik</strong> hosil qiladi va '
            'har bir juftlik — mos kelish uchun yangi imkoniyat.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> «kamida bittasi»ni hisoblash qiyin '
            'boʻlsa, «hech biri»ni hisoblab, 1 dan ayiring. Va odamlarni emas, juftliklarni '
            'sanang — juftliklar odamlardan ancha tez koʻpayadi. Shuning uchun informatiklar '
            'ikki faylning «barmoq izi» bir xil chiqib qolishidan sezgi aytganidan ancha '
            'oldinroq xavotirlanishadi.</p>',
    },

    # ── Round 4 ─────────────────────────────────────────────────────────────
    {
        'number': 23, 'round': 4, 'category': 'numbers', 'difficulty': 3,
        'title':    'When the Hands Meet',
        'title_uz': 'Millar uchrashganda',
        'teaser':    'Midnight to midnight: how often does the minute hand cover the hour hand?',
        'teaser_uz': 'Yarim tundan yarim tungacha: minut mili soat milini necha marta yopadi?',

        'body':
            '<p>The Tashkent chiming clock near Amir Temur Square strikes midnight. At that '
            'moment its two hands lie exactly on top of each other, both pointing at 12.</p>'
            + fig(clockface(12, 0), 'Midnight: the hands overlap.')
            + '<p>Afsona decides to count every moment in the next day when the minute hand '
            'lies exactly on top of the hour hand.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🕛</span>'
            '<span>Count from <strong>00:00 today</strong> (that overlap counts) up to but '
            '<strong>not including 00:00 tomorrow</strong>. Only exact overlaps count — '
            '“nearly” does not.</span></div>'
            '<p>“Easy,” says Jasur. “Once an hour — 24.” He is wrong.</p>'
            '<p class="lg-ask">Answer to type: the <strong>number of overlaps</strong>.</p>',

        'body_uz':
            '<p>Amir Temur xiyoboni yonidagi Toshkent kurantlari yarim tunni chaladi. Shu '
            'paytda ikkala mil bir-birining ustida, ikkalasi ham 12 ni koʻrsatib turibdi.</p>'
            + fig(clockface(12, 0), 'Yarim tun: millar ustma-ust.')
            + '<p>Afsona keyingi bir sutka davomida minut mili soat milining aynan ustiga '
            'tushgan har bir lahzani sanashga qaror qildi.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🕛</span>'
            '<span><strong>Bugun soat 00:00</strong> dan (bu uchrashuv hisobga olinadi) '
            '<strong>ertaga soat 00:00</strong> gacha (u hisobga olinmaydi) sanang. Faqat '
            'aniq ustma-ust tushish sanaladi — «deyarli» hisob emas.</span></div>'
            '<p>«Oson, — deydi Jasur. — Har soatda bir marta, 24.» U adashyapti.</p>'
            '<p class="lg-ask">Javob sifatida yozing: <strong>ustma-ust tushishlar '
            'soni</strong>.</p>',

        'hint':    'Look at what happens between 11:00 and 1:00. Or count laps: how many times '
                   'does the minute hand go round while the hour hand goes round once?',
        'hint_uz': 'Soat 11:00 bilan 1:00 orasida nima boʻlishiga qarang. Yoki aylanishlarni '
                   'sanang: soat mili bir aylanganda minut mili necha marta aylanadi?',

        'answer_key': '22',
        'accepted': ['22 times', '22 marta', '22 ta', 'yigirma ikki', 'twenty two', 'twenty-two'],
        'answer_hint':    'a number of overlaps',
        'answer_hint_uz': 'ustma-ust tushishlar soni',

        'solution':
            '<ol class="lg-steps">'
            '<li>Jasur’s “once an hour” fails between 11 and 1: the next overlap after 11:00 '
            'is not at 11-something — it is at exactly <strong>12:00</strong>. The hour from '
            '11 to 12 has no overlap of its own.</li>'
            '<li>Count laps instead. In 12 hours the hour hand goes round <strong>once</strong> '
            'and the minute hand goes round <strong>12 times</strong>.</li>'
            '<li>Like two runners on a track, the faster one passes the slower one once for '
            'every lap it gains: 12 − 1 = <strong>11 overlaps every 12 hours</strong>.</li>'
            '<li>So they meet every 12/11 hours ≈ 1 hour 5 minutes 27 seconds: 00:00, '
            'about 1:05, 2:11, 3:16 … and next at 12:00.</li>'
            '<li>In 24 hours: 2 × 11 = <strong>22</strong> overlaps (counting the midnight at '
            'the start, not the one at the end).</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> when two things go round at '
            'different speeds, count the <em>difference</em> in laps. The minute hand gains '
            '11 laps on the hour hand every 12 hours, so it catches it 11 times. The same '
            'idea gives you how often runners lap each other, when planets line up, and '
            'why the Moon’s phases repeat every 29½ days instead of 27⅓.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Jasurning «har soatda bir marta»si 11 bilan 1 orasida buziladi: 11:00 dan '
            'keyingi uchrashuv 11 dan keyin emas, aynan <strong>12:00</strong> da. 11 dan 12 '
            'gacha boʻlgan soatning oʻz uchrashuvi yoʻq.</li>'
            '<li>Buning oʻrniga aylanishlarni sanang. 12 soatda soat mili <strong>bir marta'
            '</strong>, minut mili esa <strong>12 marta</strong> aylanadi.</li>'
            '<li>Yoʻlakdagi ikki yuguruvchi kabi, tezrogʻi sekinrogʻidan har bir orttirgan '
            'aylanasida bir marta oʻzib ketadi: 12 − 1 = <strong>har 12 soatda 11 '
            'uchrashuv</strong>.</li>'
            '<li>Demak ular har 12/11 soatda ≈ 1 soat 5 daqiqa 27 soniyada uchrashadi: 00:00, '
            'taxminan 1:05, 2:11, 3:16 … va keyingisi 12:00 da.</li>'
            '<li>24 soatda: 2 × 11 = <strong>22</strong> ta uchrashuv (boshidagi yarim tun '
            'hisobga olinadi, oxiridagisi olinmaydi).</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> ikki narsa har xil tezlikda '
            'aylansa, aylanishlar <em>farqini</em> sanang. Minut mili har 12 soatda soat '
            'milidan 11 aylana oʻzib ketadi, demak uni 11 marta quvib yetadi. Xuddi shu gʻoya '
            'yuguruvchilar bir-birini qanchalik tez-tez quvib oʻtishini, sayyoralar qachon bir '
            'chiziqqa kelishini va nega Oy fazalari 27⅓ emas, 29½ kunda takrorlanishini '
            'tushuntiradi.</p>',
    },

    {
        'number': 24, 'round': 4, 'category': 'strategy', 'difficulty': 4,
        'title':    'The Walnut Game',
        'title_uz': 'Yongʻoq oʻyini',
        'teaser':    'Take one to six walnuts. Whoever takes the last one wins. Which piles are traps?',
        'teaser_uz': 'Birdan oltitagacha yongʻoq oling. Oxirgisini olgan yutadi. Qaysi uyumlar tuzoq?',

        'body':
            '<p>Afsona and Jasur play a game with a pile of walnuts. They take turns, '
            '<strong>Afsona first</strong>. On each turn a player must take '
            '<strong>1, 2, 3, 4, 5 or 6</strong> walnuts from the pile. Whoever takes the '
            '<strong>last walnut wins</strong> — and gets to eat the lot.</p>'
            + fig(row(['🌰'] * 8, box=False, glyph_size=24),
                  'A pile of walnuts. Each turn: take between one and six.')
            + '<p>Both play perfectly. For some starting piles Afsona can always win, however '
            'well Jasur plays. For others she is doomed before she touches a walnut.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🌰</span>'
            '<span>Consider every starting pile from <strong>1 to 100</strong> walnuts. '
            'Perfect play on both sides.</span></div>'
            '<p class="lg-ask">Answer to type: for <strong>how many</strong> of the starting '
            'piles from 1 to 100 does Jasur (the second player) win?</p>',

        'body_uz':
            '<p>Afsona va Jasur bir uyum yongʻoq bilan oʻynashmoqda. Ular navbatma-navbat '
            'yurishadi, <strong>birinchi Afsona</strong>. Har bir yurishda oʻyinchi uyumdan '
            '<strong>1, 2, 3, 4, 5 yoki 6</strong> ta yongʻoq olishi shart. <strong>Oxirgi '
            'yongʻoqni olgan yutadi</strong> — va hammasini yeydi.</p>'
            + fig(row(['🌰'] * 8, box=False, glyph_size=24),
                  'Bir uyum yongʻoq. Har yurishda: birdan oltitagacha oling.')
            + '<p>Ikkalasi ham bequsur oʻynaydi. Baʼzi boshlangʻich uyumlarda Afsona Jasur '
            'qanchalik yaxshi oʻynamasin, doim yutadi. Boshqalarida esa u birorta yongʻoqqa '
            'qoʻl tekkizmasdan yutqazib boʻlgan.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🌰</span>'
            '<span><strong>1 dan 100 gacha</strong> boʻlgan har bir boshlangʻich uyumni '
            'koʻrib chiqing. Ikki tomon ham bequsur oʻynaydi.</span></div>'
            '<p class="lg-ask">Javob sifatida yozing: 1 dan 100 gacha boʻlgan boshlangʻich '
            'uyumlarning <strong>nechtasida</strong> Jasur (ikkinchi oʻyinchi) yutadi?</p>',

        'hint':    'Work backwards from small piles. If you can leave your opponent a pile of '
                   '7, can they ever win?',
        'hint_uz': 'Kichik uyumlardan orqaga qarab ishlang. Raqibingizga 7 ta yongʻoq '
                   'qoldirsangiz, u yuta oladimi?',

        'answer_key': '14',
        'accepted': ['14 piles', '14 ta', '14 ta uyum', 'oʻn toʻrt', "o'n to'rt", 'fourteen'],
        'answer_hint':    'a count of piles',
        'answer_hint_uz': 'uyumlar soni',

        'solution':
            '<ol class="lg-steps">'
            '<li>With 1 to 6 walnuts, Afsona takes them all and wins.</li>'
            '<li>With <strong>7</strong>, whatever she takes (1-6) leaves 1-6 for Jasur, and he '
            'takes the rest. <strong>7 is a losing pile</strong> for the player to move.</li>'
            '<li>With 8 to 13, Afsona takes just enough to leave Jasur exactly 7 — and now '
            '<em>he</em> is stuck.</li>'
            '<li>With <strong>14</strong>, any move leaves 8-13, from which Jasur leaves her 7. '
            'Losing again.</li>'
            '<li>The pattern: the losing piles are exactly the <strong>multiples of 7</strong>. '
            'Whatever the first player takes (k), the second takes 7 − k, and every round '
            'removes exactly 7.</li>'
            '<li>Multiples of 7 from 1 to 100: 7, 14, … , 98 — that is '
            '<strong>14</strong> piles.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> in a game with no luck, label '
            'every position winning or losing, starting from the end and working backwards. '
            'A position is losing if every move leads to a winning one. Here the labels '
            'repeat every 7 — and once you see that, you can win any pile that is not a '
            'multiple of 7 by always “completing the seven”. Chess engines use the same '
            'backwards labelling on endgames.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>1 tadan 6 tagacha yongʻoq boʻlsa, Afsona hammasini olib yutadi.</li>'
            '<li><strong>7</strong> ta boʻlsa, u nechta olmasin (1-6), Jasurga 1-6 ta qoladi '
            'va u qolganini oladi. <strong>7 — yurayotgan oʻyinchi uchun yutqazadigan '
            'uyum</strong>.</li>'
            '<li>8 tadan 13 tagacha boʻlsa, Afsona Jasurga roppa-rosa 7 ta qoladigan qilib '
            'oladi — endi tuzoqqa <em>u</em> tushadi.</li>'
            '<li><strong>14</strong> ta boʻlsa, har qanday yurish 8-13 ta qoldiradi, Jasur esa '
            'undan unga 7 ta qoldiradi. Yana yutqazish.</li>'
            '<li>Qonuniyat: yutqazadigan uyumlar aynan <strong>7 ga karralilar</strong>. '
            'Birinchi oʻyinchi nechta olsa (k), ikkinchisi 7 − k ta oladi va har bir aylanma '
            'roppa-rosa 7 tani olib ketadi.</li>'
            '<li>1 dan 100 gacha 7 ga karrali sonlar: 7, 14, … , 98 — bu '
            '<strong>14</strong> ta uyum.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> omad aralashmaydigan oʻyinda har bir '
            'holatni oxiridan boshlab orqaga qarab «yutuq» yoki «yutqazish» deb belgilang. '
            'Har bir yurish yutuq holatga olib borsa — holat yutqazish. Bu yerda belgilar har 7 '
            'da takrorlanadi; buni koʻrganingizdan keyin 7 ga karrali boʻlmagan har qanday '
            'uyumda doim «yettini toʻldirib» yutasiz. Shaxmat dasturlari ham endshpillarni '
            'xuddi shunday orqaga qarab belgilaydi.</p>',
    },
]
