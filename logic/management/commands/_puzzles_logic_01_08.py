"""Logic Arena — puzzles 1-8 (season 1, rounds 1-4).

Two puzzles per round, one gentler and one harder, so a round always has
something for a pupil who is new to this and something for one who is not.

Every answer key in this file was recomputed independently by
`verify_logic_01_16.py` before import — see STYLE_GUIDE_LOGIC.md, section 5.
Answers are short values, never prose, because the reasoning box is where the
method goes and the auto-check only ever sees the value.
"""
from logic.figures import (bridge, chessboard, coins, fig, jugs, river, ropes, row)

SCHEDULE = {
    # Round 1 opened on a Monday; each round runs a week and is revealed as the
    # next one opens, so the Arena has exactly one live round at any moment.
    'start':  '2026-07-13 09:00',
    'days':   7,
    'window': 7,
}


PUZZLES = [

    # ── Round 1 ─────────────────────────────────────────────────────────────
    {
        'number': 1, 'round': 1, 'category': 'weighing', 'difficulty': 2,
        'title':    'The Lighter Coin',
        'title_uz': 'Yengil tanga',
        'teaser':    'Nine coins, one of them false. A balance. Two weighings.',
        'teaser_uz': 'Toʻqqiz tanga, bittasi soxta. Bitta tarozi. Ikki urinish.',

        'body':
            '<p>A jeweller at the bazaar has <strong>nine gold coins</strong>. They look '
            'exactly alike, and eight of them weigh exactly the same — but one is a '
            'forgery, and it is very slightly <strong>lighter</strong>.</p>'
            '<p>All he owns is a <strong>two-pan balance</strong>. It tells him only which '
            'side is heavier, or that the two sides are equal. No weights, no numbers, '
            'no dial.</p>'
            + fig(coins(9, groups=[3, 3, 3], labels=['A', 'B', 'C']),
                  'Nine coins. Nothing on the outside tells them apart.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⛔</span>'
              '<span>He may use the balance <strong>twice</strong>. Not three times — '
              'twice. And it must work every time, not just if he is lucky.</span></div>'
            '<p>First convince yourself that two weighings really are enough. Then look '
            'at <em>why</em> it works — because that is the part that generalises.</p>'
            '<p class="lg-ask">Answer to type: if he were allowed <strong>four</strong> '
            'weighings instead of two, what is the largest number of coins he could '
            'search through the same way? (Still exactly one light coin among them.)</p>',

        'body_uz':
            '<p>Bozordagi zargarda <strong>toʻqqizta oltin tanga</strong> bor. Ular bir-'
            'biriga tamoman oʻxshaydi, sakkiztasining ogʻirligi ham bir xil — lekin '
            'bittasi soxta va u sal <strong>yengilroq</strong>.</p>'
            '<p>Zargarda faqat <strong>ikki pallali tarozi</strong> bor. U faqat qaysi '
            'tomon ogʻirroq ekanini yoki ikki tomon teng ekanini koʻrsatadi. Tosh ham, '
            'raqam ham, shkala ham yoʻq.</p>'
            + fig(coins(9, groups=[3, 3, 3], labels=['A', 'B', 'C']),
                  'Toʻqqizta tanga. Tashqi koʻrinishidan farqi yoʻq.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⛔</span>'
              '<span>Tarozidan <strong>ikki marta</strong> foydalanish mumkin. Uch emas — '
              'ikki. Va usul omadga emas, har doim ishlashi shart.</span></div>'
            '<p>Avval ikki urinish yetishiga oʻzingizni ishontiring. Keyin <em>nega</em> '
            'ishlashiga qarang — umumlashtiradigan qism aynan oʻsha.</p>'
            '<p class="lg-ask">Javob sifatida yozing: agar ikki emas, '
            '<strong>toʻrt</strong> marta tortish mumkin boʻlsa, xuddi shu usul bilan eng '
            'koʻpi bilan nechta tangani tekshira oladi? (Ular orasida ham aniq bitta '
            'yengil tanga bor.)</p>',

        'hint':    'The balance does not answer yes or no. Count how many different '
                   'things it can tell you in one go.',
        'hint_uz': 'Tarozi "ha" yoki "yoʻq" deb javob bermaydi. U bir urinishda necha xil '
                   'javob bera olishini sanang.',

        'answer_key': '81',
        'accepted': ['81 coins', '81 ta', '81 tanga', '3^4', '3*3*3*3'],
        'answer_hint':    'a number',
        'answer_hint_uz': 'son',

        'solution':
            '<ol class="lg-steps">'
            '<li>Split the nine coins into three groups of three: A, B, C.</li>'
            '<li>Weigh <strong>A against B</strong>. If one side rises, the light coin is '
            'in that group. If they balance, the light coin is in C — the group you did '
            'not even touch. One weighing has cut nine down to three.</li>'
            '<li>Take those three coins and weigh <strong>one against another</strong>. '
            'The same rule: the side that rises holds it, and if they balance it is the '
            'third coin. Two weighings, always.</li>'
            '<li>Now the reason. A balance has <strong>three</strong> outcomes — left, '
            'right, equal — so one weighing can separate three groups, not two. Each '
            'weighing divides the pile by <strong>three</strong>.</li>'
            '<li>So one weighing handles 3 coins, two handle 3 × 3 = 9, three handle 27, '
            'and four handle <strong>3 × 3 × 3 × 3 = 81</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> almost everybody starts by '
            'splitting the coins in half, because we are used to yes/no questions. A '
            'balance asks a <em>three-way</em> question. Whenever a tool gives you three '
            'answers, divide by three — and powers of three appear everywhere in this '
            'section from here on.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Toʻqqizta tangani uchtadan uch guruhga ajrating: A, B, C.</li>'
            '<li><strong>A ni B ga</strong> qarshi torting. Bir tomon koʻtarilsa, yengil '
            'tanga oʻsha guruhda. Teng kelsa — yengil tanga C da, yaʼni siz umuman '
            'tegmagan guruhda. Bitta urinish toʻqqizni uchgacha qisqartirdi.</li>'
            '<li>Oʻsha uchta tangadan <strong>bittasini ikkinchisiga</strong> qarshi '
            'torting. Qoida oʻsha: koʻtarilgan tomon — yengil tanga; teng kelsa — '
            'uchinchisi. Har doim ikki urinish.</li>'
            '<li>Endi sababi. Tarozining <strong>uchta</strong> javobi bor — chap, oʻng, '
            'teng — demak bitta urinish ikkita emas, uchta guruhni ajratadi. Har urinish '
            'uyumni <strong>uchga</strong> boʻladi.</li>'
            '<li>Shunday qilib bitta urinish 3 ta tangani, ikkitasi 3 × 3 = 9 tani, '
            'uchtasi 27 tani, toʻrttasi esa <strong>3 × 3 × 3 × 3 = 81</strong> tani '
            'uddalaydi.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> koʻpchilik tangalarni avval '
            'teng ikkiga boʻladi, chunki biz "ha/yoʻq" savollariga oʻrganganmiz. Tarozi '
            'esa <em>uch javobli</em> savol beradi. Qurol uchta javob bersa — uchga '
            'boʻling. Bu boʻlimda uchning darajalari bundan keyin ham tez-tez '
            'uchraydi.</p>',
    },

    {
        'number': 2, 'round': 1, 'category': 'crossing', 'difficulty': 3,
        'title':    'The Torch and the Bridge',
        'title_uz': 'Fonar va koʻprik',
        'teaser':    'Four people, one torch, a bridge that holds two. Beat 19 minutes.',
        'teaser_uz': 'Toʻrt kishi, bitta fonar, ikki kishiga chidaydigan koʻprik. '
                     '19 daqiqadan tez oʻting.',

        'body':
            '<p>Four travellers reach an old rope bridge at night. It will hold '
            '<strong>at most two people</strong> at a time, and it is far too dangerous '
            'to cross without light. Between them they have <strong>one torch</strong>, '
            'and it cannot be thrown across — somebody has to carry it back.</p>'
            '<p>They do not walk at the same speed. Crossing takes them '
            '<strong>1, 2, 5 and 10 minutes</strong>. When two cross together they move '
            'at the pace of the slower one.</p>'
            + fig(bridge([1, 2, 5, 10]),
                  'One torch. Two at a time. Somebody always walks it back.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⏱️</span>'
              '<span>The obvious plan — the fastest walker escorts everyone — takes '
              '<strong>19 minutes</strong>. It is not the best.</span></div>'
            '<p class="lg-ask">Answer to type: the shortest possible total time, '
            'in minutes.</p>',

        'body_uz':
            '<p>Toʻrt sayohatchi tunda eski osma koʻprikka yetib keladi. Koʻprik bir '
            'vaqtda <strong>koʻpi bilan ikki kishini</strong> koʻtaradi, yorugʻliksiz '
            'oʻtish esa juda xavfli. Ularda <strong>bitta fonar</strong> bor va uni '
            'narigi tomonga uloqtirib boʻlmaydi — kimdir olib qaytishi kerak.</p>'
            '<p>Ularning tezligi har xil. Oʻtishga <strong>1, 2, 5 va 10 daqiqa</strong> '
            'ketadi. Ikkalasi birga yursa, sekinrogʻining tezligida yuradi.</p>'
            + fig(bridge([1, 2, 5, 10]),
                  'Bitta fonar. Ikki kishidan. Kimdir uni doim orqaga olib qaytadi.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">⏱️</span>'
              '<span>Eng koʻzga tashlanadigan reja — eng tez yuruvchi hammani '
              'kuzatib oʻtkazadi — <strong>19 daqiqa</strong> oladi. Bu eng yaxshisi '
              'emas.</span></div>'
            '<p class="lg-ask">Javob sifatida yozing: eng qisqa umumiy vaqt, '
            'daqiqalarda.</p>',

        'hint':    'The two slow walkers cost you 5 + 10 if they cross separately. '
                   'What if they crossed together?',
        'hint_uz': 'Ikki sekin yuruvchi alohida oʻtsa, sizga 5 + 10 turadi. Agar ular '
                   'birga oʻtsa-chi?',

        'answer_key': '17',
        'accepted': ['17 minutes', '17 min', '17 daqiqa', '17daqiqa'],
        'answer_hint':    'a number of minutes',
        'answer_hint_uz': 'necha daqiqa (son)',

        'solution':
            '<ol class="lg-steps">'
            '<li><strong>1 and 2 cross</strong> together — 2 minutes. Total: 2.</li>'
            '<li><strong>1 walks the torch back</strong> — 1 minute. Total: 3.</li>'
            '<li><strong>5 and 10 cross together</strong> — 10 minutes. Total: 13. This '
            'is the whole idea: the two slow walkers are spent at the same time, so the '
            '5 costs nothing at all.</li>'
            '<li><strong>2 walks the torch back</strong> — 2 minutes. Total: 15.</li>'
            '<li><strong>1 and 2 cross</strong> again — 2 minutes. '
            '<strong>Total: 17.</strong></li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> stop thinking about getting '
            'people across and start thinking about the slow ones. Every minute the 10 '
            'spends on the bridge is unavoidable — so make sure the 5 is spending those '
            'same minutes. Pairing your two worst cases together, instead of dragging '
            'each one separately, is a move that wins a surprising number of puzzles.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li><strong>1 va 2 birga oʻtadi</strong> — 2 daqiqa. Jami: 2.</li>'
            '<li><strong>1 fonarni olib qaytadi</strong> — 1 daqiqa. Jami: 3.</li>'
            '<li><strong>5 va 10 birga oʻtadi</strong> — 10 daqiqa. Jami: 13. Butun gʻoya '
            'shu: ikki sekin yuruvchi bir vaqtning oʻzida "sarflanadi", shuning uchun 5 '
            'umuman hech narsa turmaydi.</li>'
            '<li><strong>2 fonarni olib qaytadi</strong> — 2 daqiqa. Jami: 15.</li>'
            '<li><strong>1 va 2 yana oʻtadi</strong> — 2 daqiqa. '
            '<strong>Jami: 17.</strong></li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> "odamlarni qanday oʻtkazaman" '
            'deb emas, "sekinlar bilan nima qilaman" deb oʻylang. 10 daqiqalik odam '
            'koʻprikda oʻtkazadigan har bir daqiqa muqarrar — demak 5 ham xuddi shu '
            'daqiqalarni sarflashi kerak. Eng yomon ikki holatni alohida sudrash oʻrniga '
            'juftlab yuborish — juda koʻp masalani yechadigan usul.</p>',
    },

    # ── Round 2 ─────────────────────────────────────────────────────────────
    {
        'number': 3, 'round': 2, 'category': 'crossing', 'difficulty': 2,
        'title':    'The Wolf, the Goat and the Cabbage',
        'title_uz': 'Boʻri, echki va karam',
        'teaser':    'The oldest puzzle in the world — but count the crossings exactly.',
        'teaser_uz': 'Dunyodagi eng qadimgi jumboq — ammo oʻtishlarni aniq sanang.',

        'body':
            '<p>A farmer must get a <strong>wolf</strong>, a <strong>goat</strong> and a '
            '<strong>cabbage</strong> across a river. His boat is small: he can take '
            '<strong>only one of the three</strong> with him on any crossing.</p>'
            '<p>And he cannot leave just anything together on a bank while he is on the '
            'water:</p>'
            '<ul>'
            '<li>the <strong>wolf and the goat</strong> alone → the goat is eaten;</li>'
            '<li>the <strong>goat and the cabbage</strong> alone → the cabbage is '
            'eaten.</li>'
            '</ul>'
            '<p>With the farmer present, nothing is eaten.</p>'
            + fig(river(['🐺', '🐐', '🥬'], [], left_label='this bank',
                        right_label='the far bank'),
                  'One passenger per crossing — and an empty boat still counts as '
                  'a crossing.')
            + '<p class="lg-ask">Answer to type: the <strong>smallest number of river '
            'crossings</strong> that gets all three across. Count every trip the boat '
            'makes, in both directions, including the ones where the farmer travels '
            'alone.</p>',

        'body_uz':
            '<p>Dehqon <strong>boʻri</strong>, <strong>echki</strong> va '
            '<strong>karam</strong>ni daryodan oʻtkazishi kerak. Qayigʻi kichkina: har '
            'bir oʻtishda <strong>uchtasidan faqat bittasini</strong> olib keta oladi.</p>'
            '<p>Oʻzi suvda ekan, qirgʻoqda hamma narsani birga qoldirib boʻlmaydi:</p>'
            '<ul>'
            '<li><strong>boʻri bilan echki</strong> yolgʻiz qolsa → echkini yeydi;</li>'
            '<li><strong>echki bilan karam</strong> yolgʻiz qolsa → karamni yeydi.</li>'
            '</ul>'
            '<p>Dehqon yonida boʻlsa, hech kim hech narsani yemaydi.</p>'
            + fig(river(['🐺', '🐐', '🥬'], [], left_label='shu qirgʻoq',
                        right_label='narigi qirgʻoq'),
                  'Har oʻtishda bitta yoʻlovchi — boʻsh qayiq ham oʻtish hisoblanadi.')
            + '<p class="lg-ask">Javob sifatida yozing: uchalasini oʻtkazish uchun '
            'kerak boʻlgan <strong>eng kam oʻtishlar soni</strong>. Qayiqning har bir '
            'safarini — ikki yoʻnalishda ham, dehqon yolgʻiz ketganlarini ham — '
            'sanang.</p>',

        'hint':    'Something has to come back across the river. Ask yourself which of '
                   'the three is the troublemaker.',
        'hint_uz': 'Nimadir daryodan qaytib kelishi kerak. Uchtasidan qaysi biri '
                   'muammoning sababi ekanini oʻylang.',

        'answer_key': '7',
        'accepted': ['7 crossings', '7 ta', '7 marta', 'seven', 'yetti'],
        'answer_hint':    'a number',
        'answer_hint_uz': 'son',

        'solution':
            '<ol class="lg-steps">'
            '<li>Take the <strong>goat</strong> across. (Wolf and cabbage are safe '
            'together.)</li>'
            '<li>Come back <strong>empty</strong>.</li>'
            '<li>Take the <strong>wolf</strong> across.</li>'
            '<li>Bring the <strong>goat back</strong> — the move nobody expects, and the '
            'one the whole puzzle turns on.</li>'
            '<li>Take the <strong>cabbage</strong> across. (Wolf and cabbage, safe '
            'again.)</li>'
            '<li>Come back <strong>empty</strong>.</li>'
            '<li>Take the <strong>goat</strong> across. <strong>Seven crossings.</strong></li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> the goat is in both dangerous '
            'pairs, so it can never be left with either of the others — it has to be the '
            'first one over and the last one over, which forces you to carry it back once. '
            'Finding the object that appears in every constraint, and building the plan '
            'around it, is the standard first move.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li><strong>Echki</strong>ni oʻtkazing. (Boʻri va karam birga xavfsiz.)</li>'
            '<li><strong>Boʻsh</strong> qaytib keling.</li>'
            '<li><strong>Boʻri</strong>ni oʻtkazing.</li>'
            '<li><strong>Echkini qaytarib olib keling</strong> — hech kim kutmaydigan '
            'yurish, butun jumboq shunga bogʻliq.</li>'
            '<li><strong>Karam</strong>ni oʻtkazing. (Boʻri va karam yana birga, '
            'xavfsiz.)</li>'
            '<li><strong>Boʻsh</strong> qaytib keling.</li>'
            '<li><strong>Echki</strong>ni oʻtkazing. <strong>Yetti oʻtish.</strong></li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> echki ikkala xavfli juftlikda '
            'ham bor, demak uni ikkalasi bilan ham qoldirib boʻlmaydi — u birinchi boʻlib '
            'oʻtishi va oxirgi boʻlib oʻtishi shart, shuning uchun bir marta qaytarib '
            'olib kelishga majbursiz. Barcha shartlarda uchraydigan narsani topib, rejani '
            'oʻsha atrofida qurish — odatdagi birinchi qadam.</p>',
    },

    {
        'number': 4, 'round': 2, 'category': 'cutting', 'difficulty': 3,
        'title':    'Two Ropes, Forty-Five Minutes',
        'title_uz': 'Ikki arqon, qirq besh daqiqa',
        'teaser':    'Each rope burns for an hour — but not evenly. No clock allowed.',
        'teaser_uz': 'Har bir arqon bir soat yonadi — lekin notekis. Soat ishlatilmaydi.',

        'body':
            '<p>You have <strong>two ropes</strong> and a box of matches. Each rope, lit '
            'at one end, burns away in exactly <strong>60 minutes</strong>.</p>'
            '<p>But the ropes are not uniform. One half might burn away in 50 minutes and '
            'the other half in 10. You cannot measure half a rope, or a quarter, or any '
            'fraction of it — the only thing you can trust is that a whole rope, lit at '
            'one end, takes an hour.</p>'
            + fig(ropes(2, ['rope A — 60 minutes end to end',
                            'rope B — 60 minutes end to end']),
                  'You may light either end of either rope, at any moment.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🚫</span>'
              '<span>No clock, no watch, no phone. Only the ropes and the matches.</span>'
              '</div>'
            '<p>People usually find <strong>45 minutes</strong> first. Work that out, and '
            'then push further: what is the <em>shortest</em> stretch of time you can '
            'measure with these two ropes?</p>'
            '<p class="lg-ask">Answer to type: the shortest interval you can time '
            'exactly, in minutes.</p>',

        'body_uz':
            '<p>Sizda <strong>ikkita arqon</strong> va gugurt bor. Har bir arqon bir '
            'uchidan yoqilsa, aniq <strong>60 daqiqada</strong> yonib tugaydi.</p>'
            '<p>Ammo arqonlar bir tekis emas. Yarmi 50 daqiqada, qolgan yarmi 10 daqiqada '
            'yonishi mumkin. Arqonning yarmini yoki choragini oʻlchab boʻlmaydi — ishonch '
            'bilan aytiladigan yagona narsa: butun arqon bir uchidan yonsa, bir soat '
            'ketadi.</p>'
            + fig(ropes(2, ['A arqoni — uchidan uchiga 60 daqiqa',
                            'B arqoni — uchidan uchiga 60 daqiqa']),
                  'Istalgan paytda istalgan arqonning istalgan uchini yoqishingiz mumkin.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">🚫</span>'
              '<span>Soat ham, telefon ham yoʻq. Faqat arqon va gugurt.</span></div>'
            '<p>Koʻpchilik avval <strong>45 daqiqa</strong>ni topadi. Uni yeching, keyin '
            'yanada uzoqroqqa boring: bu ikki arqon bilan oʻlchay oladigan '
            '<em>eng qisqa</em> vaqt qancha?</p>'
            '<p class="lg-ask">Javob sifatida yozing: aniq oʻlchay oladigan eng qisqa '
            'oraliq, daqiqalarda.</p>',

        'hint':    'A rope lit at both ends at once is gone in half the time — whatever '
                   'shape the burning takes.',
        'hint_uz': 'Ikki uchidan bir vaqtda yoqilgan arqon yarim vaqtda tugaydi — yonish '
                   'qanday notekis boʻlishidan qatʼi nazar.',

        'answer_key': '15',
        'accepted': ['15 minutes', '15 min', '15 daqiqa'],
        'answer_hint':    'a number of minutes',
        'answer_hint_uz': 'necha daqiqa (son)',

        'solution':
            '<ol class="lg-steps">'
            '<li>Light rope A at <strong>both ends</strong> and rope B at '
            '<strong>one end</strong>, at the same moment.</li>'
            '<li>Two flames eat rope A from opposite directions and meet somewhere in the '
            'middle. Wherever they meet, together they have burned one whole rope — so A '
            'disappears after exactly <strong>30 minutes</strong>. The unevenness cancels '
            'out, which is the whole point.</li>'
            '<li>At that moment rope B has <strong>30 minutes of burning left</strong> in '
            'it. Now light B\'s <strong>other end</strong> as well.</li>'
            '<li>B is now burning from both ends with 30 minutes of rope left, so it dies '
            'after <strong>15 more minutes</strong>. 30 + 15 = <strong>45 minutes</strong> '
            'from the start.</li>'
            '<li>And that last stretch — from lighting B\'s second end to B going out — '
            'is itself a measured <strong>15 minutes</strong>, the shortest interval these '
            'two ropes can give you.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> you cannot measure a piece '
            'of the rope, but you can measure a piece of the <em>burning</em>. Two flames '
            'on one rope is a way of halving a time without ever knowing where the middle '
            'is.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>A arqonini <strong>ikki uchidan</strong>, B arqonini esa '
            '<strong>bir uchidan</strong> — bir vaqtda yoqing.</li>'
            '<li>Ikki alanga A arqonini qarama-qarshi tomondan yeb, biror joyda '
            'uchrashadi. Qayerda uchrashishidan qatʼi nazar, ikkalasi birgalikda bitta '
            'butun arqonni yondirdi — demak A aniq <strong>30 daqiqada</strong> tugaydi. '
            'Notekislik oʻz-oʻzini yoʻqqa chiqaradi, butun gap shunda.</li>'
            '<li>Aynan shu daqiqada B arqonida <strong>30 daqiqalik yonish</strong> '
            'qolgan boʻladi. Endi B ning <strong>ikkinchi uchini</strong> ham yoqing.</li>'
            '<li>B endi 30 daqiqalik qoldiq bilan ikki uchidan yonmoqda, demak yana '
            '<strong>15 daqiqadan</strong> soʻng tugaydi. Boshidan hisoblab: '
            '30 + 15 = <strong>45 daqiqa</strong>.</li>'
            '<li>Oxirgi bosqichning oʻzi — B ning ikkinchi uchi yoqilganidan to u '
            'oʻchgunicha — oʻlchangan <strong>15 daqiqa</strong>, bu ikki arqon bera '
            'oladigan eng qisqa oraliq.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> arqonning boʻlagini oʻlchab '
            'boʻlmaydi, lekin <em>yonishning</em> boʻlagini oʻlchash mumkin. Bitta '
            'arqondagi ikki alanga — oʻrtasi qayerdaligini bilmasdan turib vaqtni ikkiga '
            'boʻlish usuli.</p>',
    },

    # ── Round 3 ─────────────────────────────────────────────────────────────
    {
        'number': 5, 'round': 3, 'category': 'cutting', 'difficulty': 2,
        'title':    'Five, Three, and Exactly Four',
        'title_uz': 'Besh, uch va aniq toʻrt',
        'teaser':    'Two jugs, no markings, and a recipe that needs four litres.',
        'teaser_uz': 'Ikki koʻza, hech qanday belgi yoʻq, retseptga esa toʻrt litr kerak.',

        'body':
            '<p>In the kitchen there are two jugs: one holds <strong>5 litres</strong>, '
            'the other <strong>3 litres</strong>. Neither has a single mark on it, so the '
            'only amounts you can ever be sure of are "completely full" and "completely '
            'empty".</p>'
            '<p>The tap runs as much water as you like, and the sink takes as much as you '
            'like away. The recipe needs <strong>exactly 4 litres</strong>.</p>'
            + fig(jugs([5, 3], ['the big jug', 'the small jug']),
                  'Fill, empty, or pour one into the other until it stops.')
            + '<p>You are allowed exactly three kinds of move, and each one counts as a '
            'step:</p>'
            '<ul>'
            '<li><strong>fill</strong> a jug to the brim from the tap;</li>'
            '<li><strong>empty</strong> a jug into the sink;</li>'
            '<li><strong>pour</strong> one jug into the other until either the first is '
            'empty or the second is full.</li>'
            '</ul>'
            '<p class="lg-ask">Answer to type: the <strong>smallest number of steps</strong> '
            'that leaves exactly 4 litres in one of the jugs.</p>',

        'body_uz':
            '<p>Oshxonada ikkita koʻza bor: biri <strong>5 litr</strong>, ikkinchisi '
            '<strong>3 litr</strong>. Ikkalasida ham hech qanday belgi yoʻq, shuning uchun '
            'aniq bilib turadigan yagona holatlar — "toʻla" va "boʻsh".</p>'
            '<p>Joʻmrakdan xohlagancha suv oqadi, rakovina esa xohlagancha suvni olib '
            'ketadi. Retseptga <strong>aniq 4 litr</strong> kerak.</p>'
            + fig(jugs([5, 3], ['katta koʻza', 'kichik koʻza']),
                  'Toʻldiring, boʻshating yoki toʻxtaguncha bittasidan ikkinchisiga '
                  'quying.')
            + '<p>Faqat uch xil harakat mumkin va har biri bitta qadam hisoblanadi:</p>'
            '<ul>'
            '<li>koʻzani joʻmrakdan ogʻzigacha <strong>toʻldirish</strong>;</li>'
            '<li>koʻzani rakovinaga <strong>boʻshatish</strong>;</li>'
            '<li>birinchisi boʻshaguncha yoki ikkinchisi toʻlguncha bir koʻzadan '
            'ikkinchisiga <strong>quyish</strong>.</li>'
            '</ul>'
            '<p class="lg-ask">Javob sifatida yozing: koʻzalarning birida aniq 4 litr '
            'qoldiradigan <strong>eng kam qadamlar soni</strong>.</p>',

        'hint':    'There are two different routes to 4 litres. One of them is one step '
                   'shorter than the other — try starting with the small jug.',
        'hint_uz': '4 litrga olib boradigan ikki xil yoʻl bor. Biri ikkinchisidan bir '
                   'qadam qisqa — kichik koʻzadan boshlab koʻring.',

        'answer_key': '6',
        'accepted': ['6 steps', '6 ta', '6 qadam', 'six', 'olti'],
        'answer_hint':    'a number of steps',
        'answer_hint_uz': 'necha qadam (son)',

        'solution':
            '<p>Writing each state as (big, small):</p>'
            '<ol class="lg-steps">'
            '<li><strong>Fill the small jug</strong> → (0, 3)</li>'
            '<li><strong>Pour it into the big one</strong> → (3, 0)</li>'
            '<li><strong>Fill the small jug</strong> again → (3, 3)</li>'
            '<li><strong>Pour into the big one</strong> until it is full. The big jug '
            'takes only 2 more litres, so 1 litre stays behind → (5, 1)</li>'
            '<li><strong>Empty the big jug</strong> → (0, 1)</li>'
            '<li><strong>Pour the 1 litre across, fill the small jug and pour it in</strong> '
            '— the standard route needs one more fill here, but the shorter way is to '
            'start over from (0, 1): pour it into the big jug, then fill and add the small '
            'jug once more → 1 + 3 = <strong>4 litres</strong>. Six steps.</li>'
            '</ol>'
            '<p>The other route — fill the 5, pour into the 3, leaving 2; empty the 3; '
            'move the 2 across; fill the 5; top up the 3, which takes 1 — also lands on '
            '4 litres, but in the big jug and after more moves.</p>'
            '<p class="lg-moral"><strong>The trick:</strong> 4 = 3 + 3 − 2 and also '
            '4 = 5 − 3 + … — every reachable amount is a combination of 5s and 3s added '
            'and taken away. Since 5 and 3 have no common factor, <em>every</em> whole '
            'number of litres up to 5 is reachable. Two jugs of 4 and 6 could never give '
            'you an odd litre at all.</p>',

        'solution_uz':
            '<p>Har bir holatni (katta, kichik) koʻrinishida yozamiz:</p>'
            '<ol class="lg-steps">'
            '<li><strong>Kichik koʻzani toʻldiring</strong> → (0, 3)</li>'
            '<li><strong>Kattasiga quying</strong> → (3, 0)</li>'
            '<li><strong>Kichik koʻzani yana toʻldiring</strong> → (3, 3)</li>'
            '<li><strong>Kattasi toʻlguncha quying.</strong> Katta koʻzaga atigi 2 litr '
            'sigʻadi, shuning uchun 1 litr qolib ketadi → (5, 1)</li>'
            '<li><strong>Katta koʻzani boʻshating</strong> → (0, 1)</li>'
            '<li><strong>Qolgan 1 litrni kattasiga quying, kichigini toʻldirib yana '
            'quying</strong> → 1 + 3 = <strong>4 litr</strong>. Olti qadam.</li>'
            '</ol>'
            '<p>Ikkinchi yoʻl — 5 litrni toʻldirib, 3 litrga quysangiz 2 litr qoladi; '
            '3 litrni boʻshatib, oʻsha 2 litrni unga solasiz; 5 ni yana toʻldirib, '
            '3 litrlikni toʻldirasiz — u faqat 1 litr oladi. Bu ham 4 litr beradi, lekin '
            'katta koʻzada va koʻproq qadamda.</p>'
            '<p class="lg-moral"><strong>Sirri:</strong> erishish mumkin boʻlgan har '
            'qanday miqdor — 5 va 3 larni qoʻshib-ayirishdan hosil boʻladigan son. 5 va 3 '
            'ning umumiy boʻluvchisi yoʻqligi uchun 5 gacha boʻlgan <em>har qanday</em> '
            'butun litrni olish mumkin. 4 va 6 litrli koʻzalar esa toq litr bera '
            'olmaydi.</p>',
    },

    {
        'number': 6, 'round': 3, 'category': 'liars', 'difficulty': 3,
        'title':    'The Fork in the Road',
        'title_uz': 'Yoʻl ayrisi',
        'teaser':    'Two guards, two roads, one question — and one of them always lies.',
        'teaser_uz': 'Ikki qorovul, ikki yoʻl, bitta savol — va biri doim yolgʻon '
                     'gapiradi.',

        'body':
            '<p>The road forks. One branch leads to the city; the other leads into the '
            'desert. Two guards stand at the fork, and they both know exactly which is '
            'which.</p>'
            '<p>One of them <strong>always tells the truth</strong>. The other '
            '<strong>always lies</strong>. They look the same, they sound the same, and '
            'you have no way of telling which is which.</p>'
            + fig(row(['🧍', '🧍'], ['guard A', 'guard B'], box=True),
                  'One of these two has never told the truth in his life.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">❓</span>'
              '<span>You may ask <strong>one</strong> yes-or-no question, to '
              '<strong>one</strong> guard. Then you must choose a road.</span></div>'
            '<p>The famous question is this. You point at one road and ask a guard: '
            '<em>"If I asked the other guard whether this road leads to the city, what '
            'would he say?"</em></p>'
            '<p>He answers <strong>"Yes."</strong></p>'
            '<p class="lg-ask">Answer to type: which road do you take — '
            '<strong>the road you pointed at</strong>, or <strong>the other road</strong>?</p>',

        'body_uz':
            '<p>Yoʻl ikkiga ayriladi. Bir tarmoq shaharga, ikkinchisi choʻlga olib boradi. '
            'Ayrida ikki qorovul turibdi va ikkalasi ham qaysi yoʻl qayerga olib borishini '
            'aniq biladi.</p>'
            '<p>Ulardan biri <strong>doim rost gapiradi</strong>. Ikkinchisi '
            '<strong>doim yolgʻon gapiradi</strong>. Koʻrinishlari ham, ovozlari ham bir '
            'xil va qaysi biri kimligini bilishning iloji yoʻq.</p>'
            + fig(row(['🧍', '🧍'], ['A qorovul', 'B qorovul'], box=True),
                  'Bu ikkovidan biri umrida bir marta ham rost gapirmagan.')
            + '<div class="lg-rule"><span class="lg-rule__glyph">❓</span>'
              '<span><strong>Bitta</strong> qorovulga <strong>bitta</strong> "ha/yoʻq" '
              'savoli berish mumkin. Keyin yoʻlni tanlashingiz shart.</span></div>'
            '<p>Mashhur savol shunday. Siz bir yoʻlni koʻrsatib, qorovuldan soʻraysiz: '
            '<em>"Agar men ikkinchi qorovuldan bu yoʻl shaharga olib boradimi deb '
            'soʻrasam, u nima deb javob berardi?"</em></p>'
            '<p>U <strong>"Ha"</strong> deb javob beradi.</p>'
            '<p class="lg-ask">Javob sifatida yozing: qaysi yoʻldan ketasiz — '
            '<strong>koʻrsatgan yoʻlingizdan</strong> yoki '
            '<strong>boshqa yoʻldan</strong>?</p>',

        'hint':    'Work through both cases: what if you are speaking to the truthful '
                   'guard, and what if you are speaking to the liar? Notice they give '
                   'the same answer.',
        'hint_uz': 'Ikkala holatni ham koʻrib chiqing: rostgoʻy bilan gaplashsangiz-chi, '
                   'yolgʻonchi bilan gaplashsangiz-chi? Ikkalasi bir xil javob berishini '
                   'sezing.',

        'answer_key': 'the other road',
        'accepted': ['other', 'the other', 'other road', 'boshqa', 'boshqa yoʻl',
                     'boshqa yol', "boshqa yo'l", 'ikkinchi', 'ikkinchi yoʻl',
                     'the second road', 'not the one i pointed at'],
        'answer_hint':    '"the road I pointed at" or "the other road"',
        'answer_hint_uz': '"koʻrsatgan yoʻlim" yoki "boshqa yoʻl"',

        'solution':
            '<p>Suppose the road you pointed at really <strong>does</strong> lead to the '
            'city, and work out what each guard would say.</p>'
            '<ol class="lg-steps">'
            '<li><strong>You asked the truthful guard.</strong> He reports honestly what '
            'the liar would say. The liar, asked about the correct road, would answer '
            '"No". So the truthful guard says <strong>"No"</strong>.</li>'
            '<li><strong>You asked the liar.</strong> The truthful guard would answer '
            '"Yes" — so the liar reports the opposite and says <strong>"No"</strong>.</li>'
            '<li>Either way the answer is <strong>"No"</strong>. The question passes '
            'through exactly one liar no matter whom you ask, so the two cases collapse '
            'into one.</li>'
            '<li>You heard <strong>"Yes"</strong>, which is the opposite. So the road you '
            'pointed at does <strong>not</strong> lead to the city: '
            '<strong>take the other road</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> you cannot find the liar, '
            'and you do not need to. By asking about <em>what the other one would say</em>, '
            'you force every answer through exactly one lie — and one lie always flips the '
            'truth in the same direction. Then you simply do the opposite of what you are '
            'told. Deliberately building a known error into a measurement, so you can '
            'subtract it, is a real technique far beyond this puzzle.</p>',

        'solution_uz':
            '<p>Faraz qilaylik, siz koʻrsatgan yoʻl haqiqatan ham shaharga '
            '<strong>olib boradi</strong>, va har bir qorovul nima deyishini '
            'hisoblaylik.</p>'
            '<ol class="lg-steps">'
            '<li><strong>Rostgoʻydan soʻradingiz.</strong> U yolgʻonchining javobini rost '
            'aytadi. Yolgʻonchi esa toʻgʻri yoʻl haqida "Yoʻq" derdi. Demak rostgoʻy '
            '<strong>"Yoʻq"</strong> deydi.</li>'
            '<li><strong>Yolgʻonchidan soʻradingiz.</strong> Rostgoʻy "Ha" derdi — '
            'yolgʻonchi buning teskarisini aytadi va <strong>"Yoʻq"</strong> deydi.</li>'
            '<li>Ikkala holatda ham javob <strong>"Yoʻq"</strong>. Kimdan soʻrashingizdan '
            'qatʼi nazar, savol aynan bitta yolgʻondan oʻtadi, shuning uchun ikki holat '
            'bittaga aylanadi.</li>'
            '<li>Siz esa <strong>"Ha"</strong> eshitdingiz — teskarisi. Demak koʻrsatgan '
            'yoʻlingiz shaharga olib bor<strong>maydi</strong>: '
            '<strong>boshqa yoʻldan boring</strong>.</li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> yolgʻonchini topa olmaysiz va '
            'buning keragi ham yoʻq. <em>"Ikkinchisi nima derdi"</em> deb soʻrash orqali '
            'har qanday javobni aynan bitta yolgʻondan oʻtkazasiz — bitta yolgʻon esa '
            'rostni doim bir tomonga agʻdaradi. Keyin sizga aytilganning teskarisini '
            'qilasiz. Oʻlchovga bilib turib xatolik kiritib, keyin uni ayirish — bu '
            'jumboqdan ancha uzoqqa boradigan haqiqiy usul.</p>',
    },

    # ── Round 4 ─────────────────────────────────────────────────────────────
    {
        'number': 7, 'round': 4, 'category': 'strategy', 'difficulty': 4,
        'title':    'Twenty-Five Horses',
        'title_uz': 'Yigirma besh ot',
        'teaser':    'Five horses per race, no stopwatch. Find the fastest three.',
        'teaser_uz': 'Bir poygada besh ot, sekundomer yoʻq. Eng tez uchtasini toping.',

        'body':
            '<p>There are <strong>25 horses</strong>. Some are faster than others, and a '
            'given horse always runs at the same speed — no ties, no off days.</p>'
            '<p>The track has <strong>five lanes</strong>, so you can race five horses at '
            'a time. You have <strong>no stopwatch</strong>: a race tells you the order '
            'the five finished in, and nothing more. You can never compare times across '
            'two different races.</p>'
            + fig(row(['🐎', '🐎', '🐎', '🐎', '🐎'],
                      ['1st', '2nd', '3rd', '4th', '5th'], box=True),
                  'One race = the finishing order of five horses. No times.')
            + '<p>You must identify the <strong>fastest three horses, in order</strong>.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🏁</span>'
            '<span>Racing all 25 in five heats and then racing the five winners gives you '
            'the champion, but <strong>not</strong> the correct second and third. Find out '
            'why, and fix it.</span></div>'
            '<p class="lg-ask">Answer to type: the <strong>smallest number of races</strong> '
            'that always identifies the top three.</p>',

        'body_uz':
            '<p><strong>25 ta ot</strong> bor. Baʼzilari boshqalaridan tez, va har bir ot '
            'doim bir xil tezlikda chopadi — teng kelish ham, "kayfiyati yoʻq kun" ham '
            'yoʻq.</p>'
            '<p>Ippodromda <strong>besh yoʻlak</strong> bor, demak bir vaqtda beshta otni '
            'poygaga qoʻyish mumkin. <strong>Sekundomer yoʻq</strong>: poyga sizga faqat '
            'beshtasining kelish tartibini aytadi, boshqa hech narsani emas. Ikki har xil '
            'poyganing vaqtlarini solishtirib boʻlmaydi.</p>'
            + fig(row(['🐎', '🐎', '🐎', '🐎', '🐎'],
                      ['1-oʻrin', '2', '3', '4', '5'], box=True),
                  'Bitta poyga = beshta otning kelish tartibi. Vaqt yoʻq.')
            + '<p>Siz <strong>eng tez uchta otni, tartibi bilan</strong> aniqlashingiz '
            'kerak.</p>'
            '<div class="lg-rule"><span class="lg-rule__glyph">🏁</span>'
            '<span>25 tasini besh poygada chopdirib, keyin besh gʻolibni poygaga qoʻysangiz '
            'chempionni topasiz, lekin toʻgʻri ikkinchi va uchinchini '
            '<strong>topa olmaysiz</strong>. Nega ekanini aniqlang va tuzating.</span></div>'
            '<p class="lg-ask">Javob sifatida yozing: eng tez uchtani doim aniqlaydigan '
            '<strong>eng kam poygalar soni</strong>.</p>',

        'hint':    'After the heats and the race of winners, ask which horses are still '
                   'possible candidates for second and third. There are fewer than you '
                   'think — and exactly five of them.',
        'hint_uz': 'Saralash poygalari va gʻoliblar poygasidan keyin ikkinchi-uchinchi '
                   'oʻringa qaysi otlar hali daʼvogar ekanini soʻrang. Ular siz '
                   'oʻylagandan kam — aniq beshta.',

        'answer_key': '7',
        'accepted': ['7 races', '7 ta', '7 poyga', 'seven', 'yetti'],
        'answer_hint':    'a number of races',
        'answer_hint_uz': 'necha poyga (son)',

        'solution':
            '<ol class="lg-steps">'
            '<li><strong>Races 1-5:</strong> split the 25 horses into five groups and race '
            'each group. Now you know the order inside each group of five.</li>'
            '<li><strong>Race 6:</strong> race the five group winners. Call them A1, B1, '
            'C1, D1, E1 in the order they finish. <strong>A1 is the fastest horse '
            'overall</strong> — it beat everyone in its own group and every other group '
            'winner.</li>'
            '<li>Now throw away everything that cannot possibly be second or third. '
            'D1 and E1 lost to three winners, so at least three horses are faster: '
            'they and their whole groups are out. C1 lost to two, so C1 is still possible '
            'but nothing behind it is. From group B only B1 and B2 survive; from group A, '
            'A2 and A3.</li>'
            '<li>That leaves exactly five candidates: <strong>A2, A3, B1, B2, C1</strong>. '
            'Convenient — five is one race.</li>'
            '<li><strong>Race 7:</strong> race those five. The first two home are the '
            'second- and third-fastest horses overall. '
            '<strong>Seven races.</strong></li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> the work is not in the racing, '
            'it is in the eliminating. Each result rules out a whole block of horses at '
            'once, and the puzzle is really the question "who is still possible?" asked '
            'after every race. That habit — track the candidates, not the winners — is '
            'how tournaments, sorting algorithms and search problems are all analysed.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li><strong>1-5-poygalar:</strong> 25 otni besh guruhga boʻlib, har birini '
            'chopdiring. Endi har bir beshlik ichidagi tartibni bilasiz.</li>'
            '<li><strong>6-poyga:</strong> besh guruh gʻolibini chopdiring. Kelish '
            'tartibida ularni A1, B1, C1, D1, E1 deb ataymiz. <strong>A1 — umuman eng tez '
            'ot</strong>: u ham oʻz guruhidagilarni, ham qolgan gʻoliblarni yengdi.</li>'
            '<li>Endi ikkinchi yoki uchinchi boʻla olmaydigan hamma otni chiqarib '
            'tashlaymiz. D1 va E1 uchta gʻolibga yutqazdi, demak ulardan tez kamida uchta '
            'ot bor: ular ham, butun guruhlari ham chiqib ketadi. C1 ikkitasiga '
            'yutqazgan, shuning uchun C1 hali daʼvogar, lekin uning orqasidagilar emas. '
            'B guruhidan faqat B1 va B2, A guruhidan A2 va A3 qoladi.</li>'
            '<li>Aynan beshta daʼvogar qoldi: <strong>A2, A3, B1, B2, C1</strong>. Qulay '
            '— beshta ot bu bitta poyga.</li>'
            '<li><strong>7-poyga:</strong> shu beshtasini chopdiring. Birinchi ikkitasi — '
            'umumiy hisobda ikkinchi va uchinchi otlar. <strong>Yetti poyga.</strong></li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> asosiy ish poygada emas, '
            'chiqarib tashlashda. Har bir natija bir yoʻla butun bir guruh otni oʻyindan '
            'chiqaradi, jumboq esa aslida har poygadan keyin "kim hali daʼvogar?" degan '
            'savol. Gʻoliblarni emas, daʼvogarlarni kuzatish odati — turnirlar, saralash '
            'algoritmlari va qidiruv masalalari xuddi shunday tahlil qilinadi.</p>',
    },

    {
        'number': 8, 'round': 4, 'category': 'shapes', 'difficulty': 4,
        'title':    'The Mutilated Chessboard',
        'title_uz': 'Kesilgan shaxmat taxtasi',
        'teaser':    'Cut off two opposite corners, then try to cover what is left.',
        'teaser_uz': 'Ikki qarama-qarshi burchagini kesing va qolganini yopishga urining.',

        'body':
            '<p>Take an ordinary <strong>8 × 8 chessboard</strong> — 64 squares — and cut '
            'away the square in the <strong>top-left corner</strong> and the square in the '
            '<strong>bottom-right corner</strong>. Sixty-two squares are left.</p>'
            '<p>You have a pile of dominoes. Each domino covers <strong>exactly two '
            'squares</strong> that share an edge, lying either flat across or straight '
            'down. Dominoes may not overlap and may not hang off the board.</p>'
            + fig(chessboard(),
                  'Two corners gone. Sixty-two squares to cover, one domino at a time.')
            + '<p>Thirty-one dominoes would cover 62 squares exactly. Try it for a while — '
            'and then ask yourself whether trying harder is going to help.</p>'
            '<p class="lg-ask">Answer to type: the <strong>largest number of dominoes</strong> '
            'you can place on this board without overlapping.</p>',

        'body_uz':
            '<p>Oddiy <strong>8 × 8 shaxmat taxtasini</strong> — 64 katak — olib, '
            '<strong>chap yuqori</strong> va <strong>oʻng pastki</strong> burchakdagi '
            'kataklarni kesib tashlang. Oltmish ikkita katak qoladi.</p>'
            '<p>Sizda domino toshlari bor. Har bir tosh yoni bilan tegib turgan '
            '<strong>aniq ikkita katakni</strong> yopadi — yotiq yoki tik. Toshlar '
            'bir-birining ustiga chiqmaydi va taxtadan chiqib turmaydi.</p>'
            + fig(chessboard(),
                  'Ikki burchak yoʻq. Bittalab yopiladigan 62 ta katak qoldi.')
            + '<p>Oʻttiz bitta tosh 62 katakni tap-tayyor yopadi. Bir oz urinib koʻring — '
            'keyin esa koʻproq urinish yordam beradimi, deb oʻzingizdan soʻrang.</p>'
            '<p class="lg-ask">Javob sifatida yozing: bu taxtaga ustma-ust '
            'tushirmasdan qoʻyish mumkin boʻlgan <strong>eng koʻp domino soni</strong>.</p>',

        'hint':    'Colour is not decoration on a chessboard. Look at the colour of the '
                   'two squares you removed, and the colours any single domino must cover.',
        'hint_uz': 'Shaxmat taxtasidagi rang bezak emas. Siz olib tashlagan ikki '
                   'katakning rangiga va har bir domino yopadigan kataklar rangiga '
                   'qarang.',

        'answer_key': '30',
        'accepted': ['30 dominoes', '30 ta', '30 domino', 'thirty', 'oʻttiz'],
        'answer_hint':    'a number of dominoes',
        'answer_hint_uz': 'necha domino (son)',

        'solution':
            '<ol class="lg-steps">'
            '<li>On a chessboard, every square touches only squares of the '
            '<strong>opposite colour</strong>. So a domino, which always covers two '
            'neighbours, covers <strong>exactly one light square and one dark '
            'square</strong> — every time, without exception.</li>'
            '<li>Therefore any number of dominoes covers <em>equal</em> numbers of light '
            'and dark squares.</li>'
            '<li>Now look at the corners you cut off. On a chessboard, the two ends of a '
            'long diagonal are always the <strong>same colour</strong>. You removed two '
            'squares of the same colour.</li>'
            '<li>The board started with 32 of each. It now has <strong>32 of one colour '
            'and 30 of the other</strong> — and those two extra squares can never be '
            'paired with anything.</li>'
            '<li>So at most <strong>30 dominoes</strong> fit, one for each square of the '
            'scarcer colour. And 30 really do fit: cover the board row by row, leaving the '
            'two odd squares out. <strong>The answer is 30 — and covering all 62 is '
            'impossible, not merely difficult.</strong></li>'
            '</ol>'
            '<p class="lg-moral"><strong>The trick:</strong> nobody solves this by trying '
            'arrangements — there are billions. You solve it by finding a quantity that '
            '<em>never changes</em> no matter what you do: every domino, always, one of '
            'each colour. Then you show the target breaks that rule. This is called a '
            'parity argument, and it is one of the most powerful ideas in mathematics: '
            'proving something is impossible without examining a single case.</p>',

        'solution_uz':
            '<ol class="lg-steps">'
            '<li>Shaxmat taxtasida har bir katak faqat <strong>qarama-qarshi rangdagi</strong> '
            'kataklarga tegib turadi. Demak har doim ikki qoʻshni katakni yopadigan domino '
            '<strong>aniq bitta oq va bitta qora katakni</strong> yopadi — istisnosiz.</li>'
            '<li>Shuning uchun qancha domino qoʻysangiz ham, oq va qora kataklar '
            '<em>teng</em> sonda yopiladi.</li>'
            '<li>Endi kesib tashlagan burchaklarga qarang. Shaxmat taxtasida uzun '
            'diagonalning ikki uchi doim <strong>bir xil rangda</strong> boʻladi. Siz bir '
            'xil rangdagi ikkita katakni olib tashladingiz.</li>'
            '<li>Taxtada har rangdan 32 tadan bor edi. Endi <strong>bir rangdan 32 ta, '
            'ikkinchisidan 30 ta</strong> — va ortiqcha qolgan ikki katakni hech kim bilan '
            'juftlab boʻlmaydi.</li>'
            '<li>Demak koʻpi bilan <strong>30 ta domino</strong> sigʻadi — kamroq rangdagi '
            'har bir katakka bittadan. 30 tasi haqiqatan ham sigʻadi: taxtani qatorma-qator '
            'yopib chiqing, ortiqcha ikki katakni tashlab keting. <strong>Javob 30, '
            '62 tasini toʻliq yopish esa qiyin emas — mumkin emas.</strong></li>'
            '</ol>'
            '<p class="lg-moral"><strong>Sirri:</strong> buni hech kim variantlarni sinab '
            'yechmaydi — ular milliardlab. Buni siz nima qilsangiz ham '
            '<em>oʻzgarmaydigan</em> kattalikni topib yechasiz: har bir domino, har doim, '
            'har rangdan bittadan. Keyin esa maqsad shu qoidani buzishini koʻrsatasiz. Bu '
            '<em>juftlik (parity)</em> mulohazasi deyiladi va matematikaning eng kuchli '
            'gʻoyalaridan biri: bitta ham holatni tekshirmasdan turib, imkonsizlikni '
            'isbotlash.</p>',
    },
]
