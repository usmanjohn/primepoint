# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-65 … PR-67.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 65 — kundalik daftar, 66 — ilmiy-ommabop, 67 — intervyu.
(62 ilmiy-ommabop, 63 mahalla portreti, 64 voqea edi — demak uchta bir xil
shakl ketma-ket kelmayapti va intervyu bu blokda birinchi marta ishlatilyapti.)

Grammatika chegarasi (kumulyativ qoida):
  65-matn: е́сли va когда́. Kelasi zamon qoidasi ikki joyda koʻrsatilgan
           («Е́сли ты найдёшь…, мы их зажжём», «Е́сли за́втра отключа́т…,
           я не бу́ду серди́ться») va когда́ + СВ ketma-ketligi.
  66-matn: потому́ что · так как · поэ́тому · из-за того́ что · благодаря́,
           oxirida darsdagi «не потому́, что… а потому́, что…» qurilishi.
  67-matn: а · но · зато́ · хотя́ · одна́ко · тем не ме́нее — oltalasi bir
           intervyuda, har biri oʻz oʻrnida.

⚠️ ATAY QOCHILGAN (keyingi darslar): ли (PR-68), тот/кто (PR-69),
причастие va деепричастие (PR-70…72), qisqa sifat (PR-73), СИФАТ
ДАРАЖАЛАРИ — бо́льше / ши́ре / быстре́е (PR-74), свой (PR-75),
кто́-то / кто́-нибудь (PR-78), никто́ … не (PR-79). Yagona istisno —
66-matndagi «са́мое глубо́кое», u Baykal haqidagi matnda muqarrar va
cn-word izohi bilan berilgan.

⚠️ FAKTLAR (66-matn tekshirilgan):
  · maksimal chuqurlik 1642 m; · yosh ~25 mln yil; · Baykal yorigʻi (rift)
    yiliga ~2 sm kengayadi; · 336 daryo quyiladi, faqat Angara oqib chiqadi;
  · dunyodagi suyuq holdagi chuchuk suvning ~1/5 qismi; · bahorda suv
    40 m gacha shaffof; · epishura raqchasi suvni filtrlaydi; · qishda muz
    1 m dan qalin, ustidan mashina yuradi; · nerpa — yagona chuchuk suv
    tyuleni. 65 va 67 — toʻqima voqealar, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_65_67.py --author=prime
"""

SUBJECT = {
    "name":    "Russian",
    "summary": "Rus tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#b91c1c",
}

COLLECTION = {
    "title":       "Prime Russian Readings",
    "description": (
        "Prime Russian darslarining oʻqish matnlari — har biri oʻz darsining "
        "grammatikasini matn ichida koʻrsatadi. Lugʻat izohlari bilan."
    ),
    "order": 3,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PR-65 — если / когда                        KUNDALIK DAFTAR
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Когда́ отключи́ли свет",
        "summary": (
            "PR-65 matni. Kundalik daftar sahifasi: seshanba kuni uyda chiroq "
            "oʻchdi va oila uch soat sham yorugʻida birga oʻtirdi. Matn "
            "«когда́» bilan «е́сли» ni yonma-yon koʻrsatadi."
        ),
        "order":   65,
        "grammar": [
            {
                "pattern":  "Когда́ + oʻtgan zamon (СВ) — ketma-ketlik",
                "meaning":  "Avval bir ish tugaydi, keyin ikkinchisi boshlanadi: "
                            "«Когда́ ста́ло темно́, я испуга́лась», «Когда́ свет "
                            "включи́ли, все замолча́ли».",
                "examples": ["Когда́ ста́ло темно́, я испуга́лась.",
                             "Когда́ свет включи́ли, все замолча́ли."],
            },
            {
                "pattern":  "Е́сли + kelasi zamon",
                "meaning":  "Real shart. Voqea kelajakda boʻlgani uchun ikkala "
                            "qismda ham kelasi zamon turadi — oʻzbekcha «topsang» "
                            "zamonsiz, ruschada esa «найдёшь».",
                "examples": ["Е́сли ты найдёшь спи́чки, мы их зажжём.",
                             "Е́сли за́втра отключа́т свет, я не бу́ду серди́ться."],
            },
            {
                "pattern":  "Когда́ + hozirgi zamon — umumiy haqiqat",
                "meaning":  "Oxirgi jumlada «когда́» bir marta boʻlgan voqeani "
                            "emas, har doim takrorlanadigan holatni bildiradi.",
                "examples": ["Когда́ в до́ме темно́, лю́ди начина́ют говори́ть."],
            },
        ],
        "body": '''<p><em>Вто́рник, во́семь часо́в ве́чера.</em></p>

<p>Сего́дня в на́шем до́ме <span class="cn-word" data-pos="verb" data-tr="oʻchirishdi">отключи́ли</span> свет. Э́то <span class="cn-word" data-pos="verb" data-tr="sodir boʻldi">случи́лось</span> ро́вно в семь. Я сиде́ла за столо́м и де́лала уро́ки.</p>

<p><strong>Когда́ ста́ло</strong> <span class="cn-word" data-tr="qorongʻi">темно́</span>, я снача́ла <span class="cn-word" data-pos="verb" data-tr="qoʻrqib ketdim">испуга́лась</span>. Пото́м я <span class="cn-word" data-pos="verb" data-tr="esladim">вспо́мнила</span>, что на ку́хне лежа́т <span class="cn-word" data-tr="shamlar">све́чи</span>.</p>

<p>Ма́ма сказа́ла: «<strong>Е́сли ты найдёшь</strong> <span class="cn-word" data-tr="gugurt">спи́чки</span>, мы их <span class="cn-word" data-pos="verb" data-tr="yoqamiz">зажжём</span>». Я нашла́ спи́чки в <span class="cn-word" data-tr="quti, tortma">я́щике</span>.</p>

<p>Мы зажгли́ три свечи́ и се́ли вме́сте на ку́хне. Телефо́ны оста́лись в ко́мнате.</p>

<p>Ба́бушка начала́ расска́зывать о <span class="cn-word" data-tr="bolalik">де́тстве</span>. Она́ говори́ла, что ра́ньше свет отключа́ли ка́ждую неде́лю. Тогда́ лю́ди выходи́ли во двор и <span class="cn-word" data-pos="verb" data-tr="suhbatlashardilar">разгова́ривали</span>.</p>

<p>Мы слу́шали ба́бушку два часа́. Обы́чно ве́чером мы сиди́м в <span class="cn-word" data-tr="turli">ра́зных</span> ко́мнатах.</p>

<p><strong>Когда́ свет включи́ли</strong>, все <span class="cn-word" data-pos="verb" data-tr="jim boʻlishdi">замолча́ли</span>. Ба́бушка <span class="cn-word" data-pos="verb" data-tr="kulib yubordi">засмея́лась</span> и сказа́ла: «Ну вот, <span class="cn-word" data-tr="ertak">ска́зка</span> <span class="cn-word" data-pos="verb" data-tr="tugadi">ко́нчилась</span>».</p>

<p>Тепе́рь я ду́маю так. <strong>Е́сли за́втра сно́ва отключа́т</strong> свет, я не бу́ду <span class="cn-word" data-pos="verb" data-tr="jahlim chiqmoq">серди́ться</span>. <strong>Когда́</strong> в до́ме темно́, лю́ди начина́ют говори́ть <span class="cn-word" data-tr="bir-biri bilan">друг с дру́гом</span>.</p>''',
        "questions": [
            {
                "text": "Chiroq oʻchgach, oila nima qildi?",
                "choices": [
                    "Hamma oʻz xonasiga tarqaldi",
                    "Uch shamni yoqib, oshxonada birga oʻtirishdi",
                    "Telefon chirogʻida darsni davom ettirishdi",
                    "Qoʻshnilarnikiga chiqib ketishdi"
                ],
                "answer": 1,
                "explanation": "«Мы зажгли́ три свечи́ и се́ли вме́сте на ку́хне. "
                               "Телефо́ны оста́лись в ко́мнате». Aynan shundan keyin "
                               "buvining hikoyasi boshlanadi.",
            },
            {
                "text": "Nega matnda «Е́сли ты найдёшь спи́чки» deyilgan, «е́сли ты нахо́дишь» emas?",
                "choices": [
                    "Chunki bu buyruq gap",
                    "Chunki «е́сли» har doim kelasi zamon talab qiladi degan qoida bor",
                    "Chunki voqea kelajakda — shuning uchun ikkala qismda ham kelasi zamon",
                    "Chunki «найти́» feʼlining hozirgi zamoni yoʻq"
                ],
                "answer": 2,
                "explanation": "Gugurtni topish ham, shamni yoqish ham hali "
                               "boʻlmagan — ikkalasi ham kelajakda. Rus tilida "
                               "bunday holatda ergash gapda ham kelasi zamon "
                               "turadi: найдёшь … зажжём. Oʻzbekcha «topsang» "
                               "zamonni koʻrsatmaydi, shuning uchun bu joy "
                               "oʻzbek oʻquvchisi uchun tuzoq.",
            },
            {
                "text": "Kundalikning oxirgi xulosasi nima?",
                "choices": [
                    "Chiroq oʻchsa, dars qilib boʻlmaydi",
                    "Sham chiroqdan koʻra xavfsizroq",
                    "Buvining hikoyalari juda uzun edi",
                    "Uy qorongʻi boʻlganda odamlar bir-biri bilan gaplasha boshlaydi"
                ],
                "answer": 3,
                "explanation": "«Когда́ в до́ме темно́, лю́ди начина́ют говори́ть "
                               "друг с дру́гом». Bu yerdagi «когда́» bir kechani "
                               "emas, umumiy qoidani bildiradi — shuning uchun "
                               "feʼl hozirgi zamonda.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-66 — sabab va natija                       ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Почему́ Байка́л тако́й глубо́кий",
        "summary": (
            "PR-66 matni. Baykal nega dunyodagi eng chuqur koʻl ekanini "
            "tushuntiradi: u suv toʻlgan chuqurlik emas, yer poʻstlogʻidagi "
            "yoriq. Barcha faktlar haqiqiy. Oxirida darsning «не потому́, "
            "что… а потому́, что…» qurilishi."
        ),
        "order":   66,
        "grammar": [
            {
                "pattern":  "Потому́ что / так как — sabab",
                "meaning":  "Ikkalasi ham sababni aytadi. Farqi oʻrnida: «так как» "
                            "gapni boshlaydi, «потому́ что» esa asosiy gapdan keyin "
                            "turadi.",
                "examples": ["Байка́л глубо́кий, потому́ что он лежи́т в тре́щине.",
                             "Так как кора́ расхо́дится, берега́ Байка́ла отдаля́ются."],
            },
            {
                "pattern":  "Поэ́тому — natija",
                "meaning":  "Sababdan keyin xulosa chiqaradi: «shuning uchun». "
                            "Matnda uch marta uchraydi.",
                "examples": ["Лёд то́лстый, поэ́тому по о́зеру е́здят маши́ны."],
            },
            {
                "pattern":  "Из-за того́ что + gap · благодаря́ + Д.п.",
                "meaning":  "«Из-за» — yomon natija, «благодаря́» — yaxshi natija. "
                            "«Из-за того́ что» butun gap bilan, «благодаря́» esa "
                            "Да́тельный kelishigidagi ot bilan keladi.",
                "examples": ["Из-за того́ что ре́ки прино́сят песо́к, дно поднима́ется.",
                             "Благодаря́ э́тому рачку́ вода́ остаётся чи́стой."],
            },
        ],
        "body": '''<p>Байка́л — <span class="cn-word" data-tr="eng chuqur">са́мое глубо́кое</span> о́зеро на Земле́. Его́ <span class="cn-word" data-tr="chuqurlik">глубина́</span> — 1642 ме́тра. Почему́ так?</p>

<p>Мно́гие ду́мают, что Байка́л — э́то про́сто больша́я <span class="cn-word" data-tr="chuqurlik, oʻra">я́ма</span> с водо́й. Но э́то не так.</p>

<p>Байка́л глубо́кий, <strong>потому́ что</strong> он лежи́т в <span class="cn-word" data-tr="yoriq">тре́щине</span> земно́й <span class="cn-word" data-tr="poʻstloq">коры́</span>. Здесь кора́ <span class="cn-word" data-pos="verb" data-tr="ikki tomonga ajraladi">расхо́дится</span> в ра́зные сто́роны. Э́то происхо́дит уже́ два́дцать пять миллио́нов лет.</p>

<p><strong>Так как</strong> кора́ расхо́дится ка́ждый год приме́рно на два сантиме́тра, <span class="cn-word" data-tr="qirgʻoqlar">берега́</span> Байка́ла ме́дленно отдаля́ются друг от дру́га. <strong>Поэ́тому</strong> учёные говоря́т, что че́рез миллио́ны лет здесь бу́дет океа́н.</p>

<p>В Байка́л <span class="cn-word" data-pos="verb" data-tr="quyiladi">впада́ют</span> 336 рек, а <span class="cn-word" data-pos="verb" data-tr="oqib chiqadi">вытека́ет</span> то́лько одна́ — Ангара́. <strong>Из-за того́ что</strong> ре́ки прино́сят мно́го <span class="cn-word" data-tr="qum">песка́</span>, дно о́зера ме́дленно поднима́ется. Но тре́щина продолжа́ет <span class="cn-word" data-pos="verb" data-tr="chuqurlashmoq">углубля́ться</span>, <strong>поэ́тому</strong> Байка́л остаётся глубо́ким.</p>

<p>Воды́ в Байка́ле о́чень мно́го — приме́рно <span class="cn-word" data-tr="beshdan bir qismi">пя́тая часть</span> всей жи́дкой <span class="cn-word" data-tr="chuchuk">пре́сной</span> воды́ на Земле́.</p>

<p>Вода́ здесь <span class="cn-word" data-tr="toza">чи́стая</span>. Весно́й в ней ви́дно на со́рок ме́тров <span class="cn-word" data-tr="chuqurlikka">вглубь</span>. <strong>Так как</strong> в о́зере живёт кро́шечный <span class="cn-word" data-tr="qisqichbaqacha">рачо́к</span> — эпишу́ра, вода́ постоя́нно <span class="cn-word" data-pos="verb" data-tr="tozalanadi">очища́ется</span>. Э́тот рачо́к <span class="cn-word" data-pos="verb" data-tr="filtrlaydi">фильтру́ет</span> во́ду, и <strong>благодаря́</strong> ему́ Байка́л остаётся прозра́чным.</p>

<p>Зимо́й о́зеро <span class="cn-word" data-pos="verb" data-tr="muzlaydi">замерза́ет</span>. Лёд стано́вится о́чень <span class="cn-word" data-tr="qalin">то́лстым</span> — от одного́ до двух ме́тров. <strong>Поэ́тому</strong> зимо́й по Байка́лу е́здят маши́ны.</p>

<p>Ещё в Байка́ле живёт <span class="cn-word" data-tr="Baykal tyuleni">не́рпа</span> — еди́нственный в ми́ре пре́сноводный <span class="cn-word" data-tr="tyulen">тюле́нь</span>.</p>

<p>Ита́к, Байка́л глубо́кий <strong>не потому́, что</strong> он ста́рый. Он глубо́кий <strong>потому́, что</strong> земля́ под ним до сих пор дви́жется.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra, Baykal nega bunchalik chuqur?",
                "choices": [
                    "U yer poʻstlogʻidagi yoriqda yotadi va yoriq hamon kengaymoqda",
                    "Unga 336 ta daryo quyiladi",
                    "U juda qadimiy koʻl, shuning uchun choʻkib ketgan",
                    "Qishda muz uning tubini bosib turadi"
                ],
                "answer": 0,
                "explanation": "«Байка́л глубо́кий, потому́ что он лежи́т в "
                               "тре́щине земно́й коры́». Matnning oxirgi jumlasi "
                               "buni yana bir bor taʼkidlaydi: yosh emas, harakat "
                               "sabab.",
            },
            {
                "text": "Nega matnda «благодаря́ ему́» deyilgan, «из-за него́» emas?",
                "choices": [
                    "Chunki «из-за» faqat odamlar haqida ishlatiladi",
                    "Chunki rachok kichkina",
                    "Chunki natija yaxshi — suv toza qoladi",
                    "Chunki «эпишу́ра» ayol jinsida"
                ],
                "answer": 2,
                "explanation": "«Благодаря́» ijobiy natijaga ishlatiladi va "
                               "Да́тельный kelishigini oladi (ему́). Rachok suvni "
                               "tozalaydi — bu yaxshi natija, shuning uchun «из-за» "
                               "toʻgʻri kelmaydi.",
            },
            {
                "text": "Daryolar olib keladigan qum bilan yoriq oʻrtasida qanday kurash bor?",
                "choices": [
                    "Qum yoriqni butunlay toʻldirib boʻlgan",
                    "Qum tubni koʻtaradi, yoriq esa chuqurlashishda davom etadi",
                    "Yoriq qumni Angaraga surib chiqaradi",
                    "Qum faqat qishda toʻplanadi"
                ],
                "answer": 1,
                "explanation": "«Из-за того́ что ре́ки прино́сят мно́го песка́, дно "
                               "о́зера ме́дленно поднима́ется. Но тре́щина "
                               "продолжа́ет углубля́ться, поэ́тому Байка́л "
                               "остаётся глубо́ким». Bir sabab tubni koʻtaradi, "
                               "ikkinchisi tushiradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-67 — qarama-qarshilik                            INTERVYU
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ма́ленький го́род, больша́я библиоте́ка",
        "summary": (
            "PR-67 matni. Sakkiz ming aholili kichik shaharda qirq ming kitobli "
            "kutubxona bor. Kutubxonachi Nina Petrovna bilan suhbat — har bir "
            "javobda kamchilik va uning oʻrnini bosadigan narsa yonma-yon turadi."
        ),
        "order":   67,
        "grammar": [
            {
                "pattern":  "Зато́ — kamchilikning oʻrnini bosadigan yaxshilik",
                "meaning":  "Avval minus, keyin plus. Oʻzbekchada bitta soʻzli "
                            "tarjimasi yoʻq: «buning evaziga», «buning oʻrniga».",
                "examples": ["Го́род ма́ленький, зато́ у нас со́рок ты́сяч книг.",
                             "Зимо́й здесь прохла́дно, зато́ ти́хо и светло́."],
            },
            {
                "pattern":  "А — solishtirish · но — kutilganga zid",
                "meaning":  "«А» oʻzbekcha «esa» ning oʻrnida turadi va ikki "
                            "toʻgʻri gapni yonma-yon qoʻyadi. «Но» esa kutilgan "
                            "narsani buzadi.",
                "examples": ["Шко́льники прихо́дят по́сле уро́ков, а пенсионе́ры — у́тром.",
                             "Де́нег бы́ло ма́ло, но лю́ди приноси́ли кни́ги са́ми."],
            },
            {
                "pattern":  "Хотя́ · одна́ко · тем не ме́нее",
                "meaning":  "«Хотя́» ergash gap boshlaydi (oʻzbekcha «…sa ham»). "
                            "«Одна́ко» va «тем не ме́нее» — shu maʼnoning kitobiy "
                            "va rasmiy variantlari.",
                "examples": ["Хотя́ зда́ние ста́рое, кры́ша не протека́ет.",
                             "Тем не ме́нее я рабо́таю здесь три́дцать лет."],
            },
        ],
        "body": '''<p><em>Ни́на Петро́вна рабо́тает в библиоте́ке три́дцать лет. Её го́род о́чень ма́ленький, <strong>зато́</strong> библиоте́ка в нём больша́я. Мы поговори́ли с ней.</em></p>

<p>— Ни́на Петро́вна, ско́лько люде́й живёт в ва́шем го́роде?</p>

<p>— Во́семь ты́сяч. Го́род ма́ленький, <strong>зато́</strong> у нас со́рок ты́сяч книг.</p>

<p>— Со́рок ты́сяч? Отку́да?</p>

<p>— Мы <span class="cn-word" data-pos="verb" data-tr="toʻpladik">собира́ли</span> их со́рок лет. Де́нег всегда́ бы́ло ма́ло, <strong>но</strong> лю́ди <span class="cn-word" data-pos="verb" data-tr="olib kelishardi">приноси́ли</span> кни́ги са́ми. Оди́н <span class="cn-word" data-tr="muhandis">инжене́р</span> <span class="cn-word" data-pos="verb" data-tr="berib yubordi">отда́л</span> нам всю дома́шнюю библиоте́ку.</p>

<p>— У вас но́вое <span class="cn-word" data-tr="bino">зда́ние</span>?</p>

<p>— Нет. <strong>Хотя́</strong> зда́ние ста́рое, <span class="cn-word" data-tr="tom, tomi">кры́ша</span> не <span class="cn-word" data-pos="verb" data-tr="oqmaydi">протека́ет</span>. Зимо́й здесь <span class="cn-word" data-tr="salqin">прохла́дно</span>, <strong>зато́</strong> ти́хо и <span class="cn-word" data-tr="yorugʻ">светло́</span>.</p>

<p>— Кто к вам хо́дит?</p>

<p>— Ра́зные лю́ди. Шко́льники прихо́дят по́сле уро́ков, <strong>а</strong> <span class="cn-word" data-tr="nafaqaxoʻrlar">пенсионе́ры</span> — у́тром. По вечера́м прихо́дят <span class="cn-word" data-tr="kattalar">взро́слые</span>.</p>

<p>— Сейча́с все чита́ют в телефо́не. Вам не <span class="cn-word" data-tr="qoʻrqinchli">стра́шно</span>?</p>

<p>— Мне говори́ли, что че́рез де́сять лет библиоте́ки <span class="cn-word" data-pos="verb" data-tr="yopiladi">закро́ются</span>. <strong>Одна́ко</strong> лю́ди прихо́дят к нам ка́ждый день.</p>

<p>— Почему́?</p>

<p>— Кни́гу мо́жно <span class="cn-word" data-pos="verb" data-tr="buyurtma qilmoq">заказа́ть</span> в интерне́те. <strong>Но</strong> в интерне́те нельзя́ сесть <span class="cn-word" data-tr="yonida">ря́дом</span> с челове́ком и поговори́ть с ним о кни́ге. Лю́ди прихо́дят сюда́ не то́лько за кни́гами.</p>

<p>— А что вам <span class="cn-word" data-tr="qiyin">тру́дно</span>?</p>

<p>— <span class="cn-word" data-tr="maosh">Зарпла́та</span> ма́ленькая. Рабо́ты мно́го. <strong>Тем не ме́нее</strong> я рабо́таю здесь три́дцать лет и не хочу́ уходи́ть.</p>

<p>— Почему́?</p>

<p>— Потому́ что ка́ждый день здесь челове́к нахо́дит кни́гу, кото́рую до́лго <span class="cn-word" data-pos="verb" data-tr="qidirgan edi">иска́л</span>.</p>''',
        "questions": [
            {
                "text": "Kutubxonaga qirq ming kitob qayerdan kelgan?",
                "choices": [
                    "Davlat yangi bino bilan birga sovgʻa qilgan",
                    "Odamlar oʻzlari olib kelgan — qirq yil davomida toʻplangan",
                    "Boshqa shahardan koʻchirib keltirilgan",
                    "Nina Petrovna ularni internetdan buyurtma qilgan"
                ],
                "answer": 1,
                "explanation": "«Мы собира́ли их со́рок лет. Де́нег всегда́ бы́ло "
                               "ма́ло, но лю́ди приноси́ли кни́ги са́ми». Bitta "
                               "muhandis butun uy kutubxonasini bergan.",
            },
            {
                "text": "Nega matnda «Шко́льники прихо́дят по́сле уро́ков, а пенсионе́ры — у́тром» deyilgan, «но» emas?",
                "choices": [
                    "Chunki bu ikki fikr solishtirilyapti — oʻzbekcha «esa»",
                    "Chunki «но» faqat inkor gaplarda ishlatiladi",
                    "Chunki «пенсионе́ры» koʻplikda",
                    "Chunki gapda kesim tushirilgan"
                ],
                "answer": 0,
                "explanation": "Ikkala gap ham toʻgʻri va ular shunchaki yonma-yon "
                               "qoʻyilgan — hech qanday zidlik yoʻq. Oʻzbekcha "
                               "«nafaqaxoʻrlar esa ertalab» degan joyda ruschada "
                               "har doim «а» turadi.",
            },
            {
                "text": "Nina Petrovna kutubxonaning kelajagi haqida nima deydi?",
                "choices": [
                    "Oʻn yildan keyin kutubxona yopiladi deb hisoblaydi",
                    "Yangi bino qurilishini kutmoqda",
                    "Kitoblarni internetga koʻchirmoqchi",
                    "Unga kutubxonalar yopiladi deyishgan, lekin odamlar har kuni kelmoqda"
                ],
                "answer": 3,
                "explanation": "«Мне говори́ли, что че́рез де́сять лет библиоте́ки "
                               "закро́ются. Одна́ко лю́ди прихо́дят к нам ка́ждый "
                               "день». «Одна́ко» — bu «но» ning kitobiy varianti va "
                               "aynan kutilganga zid narsani kiritadi.",
            },
        ],
    },
]
