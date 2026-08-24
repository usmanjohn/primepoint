# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-71 … PR-73.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 71 — biografiya, 72 — hikoya, 73 — maktub-javob.
(68 sirli hikoya, 69 hayot hikoyasi, 70 ilmiy-ommabop edi. Maktub-javob
bu blokda birinchi marta ishlatilyapti.)

Grammatika chegarasi (kumulyativ qoida):
  71-matn: страдательные причастия — toʻliq shaklda (напи́санная,
           за́писанная, переведённая) va qisqa shaklda (напи́сана,
           изда́на, забы́та). «Кем?» Твори́тельный bilan ikki joyda.
  72-matn: деепричастия — возвраща́ясь, уви́дев, не зна́я, купи́в,
           улыба́ясь, вы́йдя. Har birida ega asosiy feʼlniki bilan bir xil —
           darsning qatʼiy qoidasi matnda buzilmagan.
  73-matn: qisqa sifatlar — прав, винова́т, рад, до́лжен, за́нят,
           согла́сен, ну́жен, свобо́ден. Xat janri bu toʻplam uchun ideal.

⚠️ ATAY QOCHILGAN (keyingi darslar): SIFAT DARAJALARI — са́мый /
бо́льше / лу́чше / ху́же (PR-74), свой (PR-75), себя́ / сам (PR-76),
ка́ждый / весь ning nozik farqi (PR-77), кто́-то / кто́-нибудь (PR-78),
никто́ … не (PR-79), шахссиз gaplar (PR-81), жамловчи sonlar — о́ба,
тро́е (PR-82).

⚠️ FAKTLAR (71-matn — HAQIQIY ODAM):
  Marko Polo (Marco Polo), venetsiyalik savdogar, taxminan 1271–1295
  yillarda Osiyoda boʻlgan va Xubilayxon xizmatida yigirma yilga yaqin
  yashagan. 1298-yil atrofida Venetsiya–Genuya urushida asirga tushib,
  Genuyada qamoqqa olingan. Kamerada u bilan birga yozuvchi Rustikello
  da Piza oʻtirgan va Markoning hikoyalarini yozib olgan — shu tariqa
  «Dunyoning xilma-xilligi haqida kitob» paydo boʻlgan. Marko 1299-yilda
  ozod qilingan. Kitob koʻp tillarga tarjima qilingan; Xristofor Kolumbning
  shaxsiy nusxasi chetlariga yozgan izohlari bilan Sevilyada saqlanadi.
  72 va 73 — toʻqima voqealar, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_71_73.py --author=prime
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
    # PR-71 — страдательные причастия                    BIOGRAFIYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Кни́га, напи́санная в тюрьме́",
        "summary": (
            "PR-71 matni. Marko Polo Genuya qamoqxonasida kamerdoshiga oʻz "
            "sayohatlarini aytib bergan — shundan dunyoning eng mashhur "
            "sayohat kitobi tugʻilgan. Faktlar haqiqiy."
        ),
        "order":   71,
        "grammar": [
            {
                "pattern":  "Toʻliq shakl: -нн- / -енн- / -т-",
                "meaning":  "Otni aniqlaydi va unga moslashadi. Sarlavhaning oʻzi "
                            "shunday: «кни́га, напи́санная в тюрьме́».",
                "examples": ["кни́га, напи́санная в тюрьме́",
                             "исто́рии, за́писанные Рустикелло"],
            },
            {
                "pattern":  "Qisqa shakl: bitta Н",
                "meaning":  "Gapning kesimi boʻladi: «кни́га изда́на», «Ма́рко "
                            "был освобождён». Toʻliqda ikkita Н, qisqada bitta.",
                "examples": ["Кни́га была́ переведена́ на мно́гие языки́.",
                             "Ма́рко был освобождён в 1299 году́."],
            },
            {
                "pattern":  "Кем? — Твори́тельный",
                "meaning":  "Ishni kim bajarganini predlogsiz Твори́тельный "
                            "bildiradi — oʻzbekcha «tomonidan».",
                "examples": ["за́писанные Рустикелло",
                             "прочи́танная Колу́мбом"],
            },
        ],
        "body": '''<p>В 1298 году́ в <span class="cn-word" data-tr="Genuya (shahar)">Ге́нуе</span> сиде́л в тюрьме́ челове́к по и́мени Ма́рко По́ло.</p>

<p>До э́того он два́дцать лет <span class="cn-word" data-pos="verb" data-tr="sayohat qilgan">путеше́ствовал</span>. Он вы́ехал из Вене́ции ещё <span class="cn-word" data-tr="oʻsmir">подро́стком</span>, дошёл до Кита́я и мно́го лет служи́л при <span class="cn-word" data-tr="saroy">дворе́</span> Хубила́й-ха́на. Он ви́дел бума́жные де́ньги, <span class="cn-word" data-tr="koʻmir">у́голь</span>, кото́рый гори́т как де́рево, и города́, <strong>постро́енные</strong> на воде́.</p>

<p>Когда́ Ма́рко верну́лся домо́й, начала́сь война́ ме́жду Вене́цией и Ге́нуей. Ма́рко пошёл на войну́, и его́ <span class="cn-word" data-pos="verb" data-tr="asirga olishdi">взя́ли в плен</span>.</p>

<p>В ка́мере с ним сиде́л <span class="cn-word" data-tr="pizalik">пиза́нец</span> Рустике́лло — писа́тель. Ему́ бы́ло <span class="cn-word" data-tr="zerikarli">ску́чно</span>. Ма́рко на́чал расска́зывать.</p>

<p>Так появи́лась кни́га, <strong>напи́санная в тюрьме́</strong>. То́чнее — <strong>расска́занная</strong> одни́м челове́ком и <strong>за́писанная</strong> други́м.</p>

<p>В 1299 году́ Ма́рко был <strong>освобождён</strong> и верну́лся в Вене́цию. А кни́га начала́ <span class="cn-word" data-pos="verb" data-tr="dunyo boʻylab tarqalmoq">расходи́ться по ми́ру</span>.</p>

<p>Она́ была́ <strong>переведена́</strong> на <span class="cn-word" data-tr="oʻnlab">деся́тки</span> языко́в. Её <span class="cn-word" data-pos="verb" data-tr="koʻchirib yozishardi">переписывали</span> от руки́ две́сти лет, пока́ не появи́лась печа́ть.</p>

<p>Мно́гие ей не ве́рили. Расска́зы о Кита́е каза́лись <span class="cn-word" data-tr="uydirma">вы́думкой</span>, и кни́га получи́ла <span class="cn-word" data-tr="masxaralab qoʻyilgan laqab">насме́шливое про́звище</span> — «Миллио́н».</p>

<p>Но одна́ ко́пия попа́ла к <span class="cn-word" data-tr="genuyalik">генуэ́зскому</span> моряку́. Его́ зва́ли Христофо́р Колу́мб. Э́тот <span class="cn-word" data-tr="nusxa">экземпля́р</span>, <strong>прочи́танный</strong> им от нача́ла до конца́, сохрани́лся до на́ших дней. На <span class="cn-word" data-tr="chetlarida">поля́х</span> — со́тни <span class="cn-word" data-tr="izohlar">заме́ток</span>, <strong>сде́ланных</strong> его́ руко́й.</p>

<p>Кни́га, <strong>напи́санная</strong> в ка́мере от <span class="cn-word" data-tr="zerikkanlikdan">ску́ки</span>, че́рез две́сти лет отпра́вила челове́ка че́рез океа́н.</p>''',
        "questions": [
            {
                "text": "Kitob qanday paydo boʻldi?",
                "choices": [
                    "Marko Polo uni Xitoyda yozgan",
                    "Rustikello Markoning hikoyalarini qamoqxona kamerasida yozib olgan",
                    "Kolumb uni Markoning xatlaridan tuzgan",
                    "Venetsiya hukumati uni buyurtma qilgan"
                ],
                "answer": 1,
                "explanation": "«Расска́занная одни́м челове́ком и за́писанная "
                               "други́м». Marko gapirdi, yozuvchi Rustikello "
                               "yozdi — ikkalasi ham asirlikda edi.",
            },
            {
                "text": "Nega matnda «кни́га была́ переведена́», lekin «кни́га, переведённая…» emas?",
                "choices": [
                    "Chunki bu koʻplik shakli",
                    "Chunki gap oʻtgan zamonda",
                    "Ikkalasi ham bir xil, farqi yoʻq",
                    "Chunki bu yerda kesim kerak — demak qisqa shakl, bitta Н bilan"
                ],
                "answer": 3,
                "explanation": "Toʻliq shakl otni aniqlaydi («qanday kitob?»), "
                               "qisqa shakl esa gapning kesimi boʻladi («kitob "
                               "nima boʻldi?»). Toʻliqda ikkita Н, qisqada "
                               "bitta.",
            },
            {
                "text": "Matnning oxirgi jumlasi nima demoqchi?",
                "choices": [
                    "Zerikish har doim yomon",
                    "Kolumb Markoni shaxsan bilgan",
                    "Zerikkanlikdan aytilgan hikoya ikki asrdan keyin Kolumbni okeanga joʻnatdi",
                    "Kitob juda uzoq yozilgan"
                ],
                "answer": 2,
                "explanation": "«Кни́га, напи́санная в ка́мере от ску́ки, че́рез "
                               "две́сти лет отпра́вила челове́ка че́рез океа́н». "
                               "Kolumbning oʻz nusxasi, chetlariga yozgan "
                               "izohlari bilan, hozir ham saqlanadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-72 — деепричастия                                    HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Возвраща́ясь домо́й",
        "summary": (
            "PR-72 matni. Marina har kuni ishdan qaytayotib bir xil skameykani "
            "koʻradi. Bir kuni skameyka boʻsh qoladi — va u nima qilish "
            "kerakligini biladi."
        ),
        "order":   72,
        "grammar": [
            {
                "pattern":  "НСВ → -я / -ясь: bir vaqtda",
                "meaning":  "Ikki ish bir paytda ketadi — oʻzbekcha «-ib»: "
                            "возвраща́ясь (qaytayotib), улыба́ясь (jilmayib).",
                "examples": ["Возвраща́ясь домо́й, Мари́на прохо́дит ми́мо скаме́йки.",
                             "Он корми́л голубе́й, ти́хо разгова́ривая с ни́ми."],
            },
            {
                "pattern":  "СВ → -в / -вшись: avval bu, keyin u",
                "meaning":  "Bir ish tugab, keyin ikkinchisi boshlanadi — "
                            "oʻzbekcha «-gach»: уви́дев (koʻrgach), купи́в "
                            "(sotib olgach).",
                "examples": ["Уви́дев пусту́ю скаме́йку, Мари́на останови́лась.",
                             "Купи́в хлеб, она́ пошла́ в парк."],
            },
            {
                "pattern":  "Ega bir xil boʻlishi shart",
                "meaning":  "Ravishdoshning egasi asosiy feʼlning egasi bilan bir "
                            "xil. Matndagi har bir oborot shu qoidaga boʻysunadi: "
                            "kim qaytdi — oʻsha koʻrdi, oʻsha toʻxtadi.",
                "examples": ["Не зна́я, что сказа́ть, Мари́на про́сто се́ла ря́дом."],
            },
        ],
        "body": '''<p>Мари́на рабо́тает в апте́ке. <strong>Возвраща́ясь домо́й</strong>, она́ ка́ждый день прохо́дит ми́мо ма́ленького <span class="cn-word" data-tr="skver, boqcha">скве́ра</span>.</p>

<p>На кра́йней <span class="cn-word" data-tr="skameyka">скаме́йке</span> всегда́ сиди́т стари́к. Его́ зову́т Пётр Ильи́ч. Он <span class="cn-word" data-pos="verb" data-tr="boqadi">ко́рмит</span> <span class="cn-word" data-tr="kaptarlar">голубе́й</span>, ти́хо <span class="cn-word" data-pos="verb" data-tr="gaplashib">разгова́ривая</span> с ни́ми.</p>

<p>Снача́ла Мари́на про́сто <span class="cn-word" data-pos="verb" data-tr="bosh irgʻardi">кива́ла</span>. Пото́м начала́ здоро́ваться. Пото́м — остана́вливаться на мину́ту.</p>

<p>В четве́рг на скаме́йке не́ было старика́.</p>

<p><strong>Уви́дев</strong> пусту́ю скаме́йку, Мари́на останови́лась. Голуби́ ходи́ли ря́дом и <span class="cn-word" data-pos="verb" data-tr="kutishardi">жда́ли</span>.</p>

<p>Она́ зашла́ в <span class="cn-word" data-tr="doʻkoncha">кио́ск</span> на углу́ и спроси́ла про старика́. Продавщи́ца сказа́ла, что Пётр Ильи́ч в больни́це: он <span class="cn-word" data-pos="verb" data-tr="yiqilib tushdi">упа́л</span> и <span class="cn-word" data-pos="verb" data-tr="shikastladi">повреди́л</span> <span class="cn-word" data-tr="oyogʻini">но́гу</span>. Врачи́ сказа́ли, что че́рез две неде́ли он бу́дет до́ма.</p>

<p><strong>Купи́в</strong> буха́нку хле́ба, Мари́на верну́лась в сквер. Она́ се́ла на кра́йнюю скаме́йку и начала́ <span class="cn-word" data-pos="verb" data-tr="maydalamoq">лома́ть</span> хлеб на ма́ленькие <span class="cn-word" data-tr="boʻlaklar">кусо́чки</span>.</p>

<p>Голуби́ <span class="cn-word" data-pos="verb" data-tr="uchib tushishdi">слете́лись</span> сра́зу. Они́ не удиви́лись: хлеб есть хлеб.</p>

<p>Так она́ де́лала де́сять дней. В дождь то́же.</p>

<p>В понеде́льник, <strong>подходя́</strong> к скве́ру, Мари́на уви́дела на скаме́йке знако́мую <span class="cn-word" data-tr="qomat, siluet">фигу́ру</span>.</p>

<p>Пётр Ильи́ч сиде́л с <span class="cn-word" data-tr="hassa">па́лкой</span>. Голуби́ уже́ бы́ли вокру́г него́.</p>

<p><strong>Не зна́я</strong>, что сказа́ть, Мари́на про́сто се́ла ря́дом.</p>

<p>Стари́к посмотре́л на неё и сказа́л: «Спаси́бо. Они́ не <span class="cn-word" data-pos="verb" data-tr="ozib ketishdi">похуде́ли</span>».</p>

<p>Мари́на засмея́лась. И, <strong>улыба́ясь</strong>, доста́ла из су́мки <span class="cn-word" data-tr="yarim non">полбуха́нки</span> хле́ба.</p>''',
        "questions": [
            {
                "text": "Marina Pyotr Ilyich kasalxonaga tushganini bilgach nima qildi?",
                "choices": [
                    "Uni kasalxonada ziyorat qildi",
                    "Boshqa yoʻldan yura boshladi",
                    "Non sotib olib, oʻn kun kaptarlarni oʻzi boqdi",
                    "Qoʻshnilarga xabar berdi"
                ],
                "answer": 2,
                "explanation": "«Купи́в буха́нку хле́ба, Мари́на верну́лась в "
                               "сквер… Так она́ де́лала де́сять дней». Chol "
                               "qaytgach, buni «они́ не похуде́ли» degan "
                               "hazil bilan tan oladi.",
            },
            {
                "text": "Nega matnda «Уви́дев пусту́ю скаме́йку», lekin «разгова́ривая с ни́ми» — biri -в, ikkinchisi -я?",
                "choices": [
                    "Chunki birinchisi СВ (avval koʻrdi, keyin toʻxtadi), ikkinchisi НСВ (bir vaqtda)",
                    "Chunki birinchisi koʻplik",
                    "Chunki ikkinchisi inkor gap",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "СВ → -в: bir ish tugaydi, keyin ikkinchisi "
                               "boshlanadi. НСВ → -я: ikkala ish bir paytda "
                               "ketadi. Chol bir vaqtning oʻzida ham boqadi, "
                               "ham gaplashadi.",
            },
            {
                "text": "Hikoyaning oxirgi jumlasi nimani koʻrsatadi?",
                "choices": [
                    "Marina kaptarlarni yoqtirmaydi",
                    "Pyotr Ilyich yana kasal boʻladi",
                    "Marina non olib kelishni unutgan",
                    "Endi kaptarlarni ikkovlashib boqishadi — Marina bekorga oʻtirmagan"
                ],
                "answer": 3,
                "explanation": "U sumkasidan yarim non chiqaradi — demak "
                               "kelishga tayyorlanib kelgan. Oʻn kunlik odat "
                               "endi ikki kishining odatiga aylandi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-73 — qisqa sifatlar                            MAKTUB-JAVOB
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Он был прав",
        "summary": (
            "PR-73 matni. Jasur Samarqandga koʻchib ketishidan oldin ikki "
            "doʻst janjallashib qolgan. Endi xat va unga javob keladi. "
            "Qisqa sifatlar — прав, винова́т, рад, до́лжен — shu yerda yashaydi."
        ),
        "order":   73,
        "grammar": [
            {
                "pattern":  "Прав · винова́т · рад",
                "meaning":  "Kundalik nutqda faqat qisqa shaklda keladi: «ты был "
                            "прав», «я винова́т», «я рад». «Ра́дый» degan soʻz "
                            "umuman yoʻq.",
                "examples": ["Ты был прав, а я винова́т.",
                             "Я о́чень рад, что ты написа́л."],
            },
            {
                "pattern":  "До́лжен — odamga moslashadi",
                "meaning":  "Erkak «до́лжен», ayol «должна́», koʻplik «должны́». "
                            "Oʻzbekcha «…ishim kerak» dagi shaxs qoʻshimchasi "
                            "kabi.",
                "examples": ["Я до́лжен был позвони́ть тебе́ ра́ньше.",
                             "Мы должны́ бы́ли поговори́ть, а не молча́ть."],
            },
            {
                "pattern":  "Ну́жен — narsaga moslashadi",
                "meaning":  "«Мне ну́жен сове́т» (erkak), «мне нужна́ по́мощь» "
                            "(ayol). До́лжен bilan aynan teskari tomonga qaraydi.",
                "examples": ["Мне ну́жен был твой сове́т.",
                             "Мне нужна́ была́ твоя́ по́мощь."],
            },
        ],
        "body": '''<p><em>Самарка́нд, 12 ма́рта</em></p>

<p>Бекзо́д, приве́т.</p>

<p>Я до́лго не писа́л. <span class="cn-word" data-pos="verb" data-tr="kechir">Прости́</span>. Снача́ла был <strong>за́нят</strong>, пото́м <strong>не гото́в</strong>. Тепе́рь пишу́.</p>

<p>Ты был <strong>прав</strong>. Тогда́, в апре́ле, ты сказа́л, что я <span class="cn-word" data-pos="verb" data-tr="shoshilyapman">спешу́</span> и что <span class="cn-word" data-tr="koʻchish, joy oʻzgartirish">перее́зд</span> — э́то не <span class="cn-word" data-tr="yechim">реше́ние</span>. Я <span class="cn-word" data-pos="verb" data-tr="jahlim chiqdi">разозли́лся</span> и уе́хал, не отве́тив на твоё <span class="cn-word" data-tr="xabar">сообще́ние</span>.</p>

<p>Я <strong>винова́т</strong>. Я <strong>до́лжен</strong> был позвони́ть тебе́ ещё в ма́е.</p>

<p>Здесь <span class="cn-word" data-tr="yomon emas">непло́хо</span>. Рабо́та есть, кварти́ра ма́ленькая, зато́ <span class="cn-word" data-tr="tinch">ти́хая</span>. Но в тот ве́чер мне <strong>ну́жен</strong> был не биле́т на по́езд, а <span class="cn-word" data-tr="suhbat">разгово́р</span>. Я тогда́ э́того не понима́л.</p>

<p>В апре́ле у меня́ бу́дет неде́ля <span class="cn-word" data-tr="taʼtil">о́тпуска</span>. Ты <strong>свобо́ден</strong> в пе́рвых чи́слах?</p>

<p>Жасу́р</p>

<p>———</p>

<p><em>Ташке́нт, 19 ма́рта</em></p>

<p>Жасу́р!</p>

<p>Я о́чень <strong>рад</strong>, что ты написа́л. <span class="cn-word" data-tr="rostini aytsam">Че́стно говоря́</span>, я <span class="cn-word" data-pos="verb" data-tr="kutgandim">ждал</span> э́того письма́ оди́ннадцать ме́сяцев.</p>

<p>И я <strong>не согла́сен</strong> с одни́м. Ты пи́шешь, что <strong>винова́т</strong> ты. Но я тогда́ говори́л <span class="cn-word" data-tr="qattiq, qoʻpol">ре́зко</span>. Я был <strong>прав</strong> по <span class="cn-word" data-tr="mohiyat">су́ти</span>, но <strong>непра́в</strong> по <span class="cn-word" data-tr="ohang, uslub">то́ну</span>. Э́то то́же <span class="cn-word" data-tr="xato">оши́бка</span>, и она́ моя́.</p>

<p>Так что <strong>винова́ты</strong> и ты, и я. <span class="cn-word" data-pos="verb" data-tr="boʻlishamiz">Разде́лим</span> <span class="cn-word" data-tr="teng ikkiga">по́ровну</span>.</p>

<p>В апре́ле я <strong>свобо́ден</strong> с пе́рвого числа́. <span class="cn-word" data-pos="verb" data-tr="kel, kelib qol">Приезжа́й</span>. Ма́ма уже́ спра́шивает, ско́лько дней ты бу́дешь у нас.</p>

<p>И ещё. Мне <strong>нужна́</strong> твоя́ по́мощь с одни́м де́лом. Расскажу́ при встре́че.</p>

<p>Бекзо́д</p>''',
        "questions": [
            {
                "text": "Nega Jasur Bekzodga xat yozdi?",
                "choices": [
                    "Yangi ish soʻrash uchun",
                    "Samarqandga koʻchishni maslahat berish uchun",
                    "Bir yil oldingi janjal uchun uzr soʻrash va uchrashuvni taklif qilish uchun",
                    "Bekzodning onasidan xabar olish uchun"
                ],
                "answer": 2,
                "explanation": "«Ты был прав… Я винова́т. Я до́лжен был позвони́ть "
                               "тебе́ ещё в ма́е». Xat oxirida u aprel oyida "
                               "taʼtilga chiqishini aytib, uchrashuvni taklif "
                               "qiladi.",
            },
            {
                "text": "Nega Bekzod «Я не согла́сен» deydi?",
                "choices": [
                    "Chunki u Jasurni koʻrmoqchi emas",
                    "Chunki aybni faqat Jasur oʻz ustiga olayotganiga qarshi — u ham xato qilgan",
                    "Chunki Jasur notoʻgʻri sanani yozgan",
                    "Chunki u Samarqandga koʻchishni maʼqullamaydi"
                ],
                "answer": 1,
                "explanation": "«Я был прав по су́ти, но непра́в по то́ну. Э́то "
                               "то́же оши́бка, и она́ моя́». Shuning uchun "
                               "«винова́ты и ты, и я».",
            },
            {
                "text": "Nega «мне ну́жен был не биле́т», lekin «мне нужна́ твоя́ по́мощь»?",
                "choices": [
                    "Chunki birinchisi oʻtgan zamon, ikkinchisi hozirgi",
                    "Chunki birinchisi inkor gap",
                    "Chunki ikkinchi xatni boshqa odam yozgan",
                    "Chunki «ну́жен» kerak boʻlgan NARSAGA moslashadi: биле́т erkak, по́мощь ayol jinsida"
                ],
                "answer": 3,
                "explanation": "Bu darsning eng katta tuzogʻi. «Ну́жен» odamga "
                               "emas, kerak boʻlgan narsaga qaraydi. «До́лжен» "
                               "esa aksincha — odamga: «я до́лжен был "
                               "позвони́ть».",
            },
        ],
    },
]
