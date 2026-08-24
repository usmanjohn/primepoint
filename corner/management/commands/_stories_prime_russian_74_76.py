# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-74 … PR-76.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 74 — ilmiy-ommabop, 75 — biografik hikoya,
76 — portret (usta haqida). (71 biografiya, 72 hikoya, 73 maktub-javob
edi — uchta bir xil shakl ketma-ket kelmayapti.)

Grammatika chegarasi (kumulyativ qoida):
  74-matn: sifat darajalari — самая длинная, длиннее, больше, меньше,
           хуже, гораздо, всех/всего hamda «чем» va Родительный li
           solishtirishning ikkalasi ham.
  75-matn: свой — beshta kelishikda va ikkala maʼnoda («oʻzining» va
           «ijara emas, oʻziniki»). Ataylab bitta «его» ham qoʻyilgan,
           farq koʻrinib tursin uchun.
  76-matn: себя / себе / собой va сам / сама / сами yonma-yon, plus
           iboralar: у себя, про себя, взять себя в руки, сделай сам.

⚠️ ATAY QOCHILGAN (keyingi darslar): каждый / весь / любой ning nozik
farqi (PR-77), кто-то / кто-нибудь (PR-78), никто … не (PR-79),
shaxssiz gaplar (PR-81), жамловчи sonlar — оба, трое (PR-82),
благодаря / несмотря на (PR-83).

⚠️ FAKTLAR (74-matn tekshirilgan):
  · Nil anʼanaviy ravishda ~6650 km, Amazonka ~6400 km deb hisoblanadi;
  · 2007-yilda Braziliya ekspeditsiyasi Amazonkaning boshini Peru
    janubidan topib, uzunligini ~6992 km deb eʼlon qilgan — bahs hamon
    tugamagan;
  · nizoning sababi — daryo QAYERDA boshlanadi va QAYERDA tugaydi degan
    savolga yagona javob yoʻqligi;
  · Amazonka suv miqdori boʻyicha shubhasiz birinchi: okeanga quyiladigan
    daryo suvining taxminan beshdan bir qismini u olib boradi;
  · Volga — Yevropaning eng uzun daryosi, ~3530 km.
  75 va 76 — toʻqima voqealar, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_74_76.py --author=prime
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
    # PR-74 — sifat darajalari                        ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Самая длинная река",
        "summary": (
            "PR-74 matni. Dunyodagi eng uzun daryo qaysi — Nilmi yoki "
            "Amazonkami? Savol oddiy koʻrinadi, lekin javob yoʻq: chunki "
            "daryo qayerda boshlanishini hech kim aniq ayta olmaydi."
        ),
        "order":   74,
        "grammar": [
            {
                "pattern":  "Самый + sifat — orttirma daraja",
                "meaning":  "Oʻzbekcha «eng». Diqqat: «самый» sifat kabi "
                            "turlanadi — самая река, самое озеро.",
                "examples": ["самая длинная река в мире",
                             "самый известный ответ"],
            },
            {
                "pattern":  "Ikki xil solishtirish: чем va Родительный",
                "meaning":  "«Нил длиннее, чем Амазонка» = «Нил длиннее "
                            "Амазонки». Ikkinchisi oʻzbekcha «-dan» ning aynan "
                            "oʻzi.",
                "examples": ["Амазонка длиннее Нила.",
                             "Она шире, чем все другие реки."],
            },
            {
                "pattern":  "Всех va всего",
                "meaning":  "«Всех» — sanaladigan narsalardan, «всего» — umuman "
                            "hamma narsadan. Matnda ikkalasi ham bor.",
                "examples": ["Эта река несёт больше всех.",
                             "Больше всего учёных интересует начало реки."],
            },
        ],
        "body": '''<p>Какой вопрос может быть <span class="cn-word" data-tr="oddiyroq">проще</span>: какая река в мире <strong>самая длинная</strong>?</p>

<p>В школе многие годы отвечали: Нил. Его <span class="cn-word" data-tr="uzunligi">длина</span> — примерно 6650 километров. Амазонка <span class="cn-word" data-pos="verb" data-tr="hisoblanardi">считалась</span> второй: около 6400.</p>

<p>Но в 2007 году бразильская <span class="cn-word" data-tr="ekspeditsiya">экспедиция</span> <span class="cn-word" data-pos="verb" data-tr="koʻtarildi">поднялась</span> высоко в горы на юге Перу и нашла другой <span class="cn-word" data-tr="manba, boshlanish joyi">исток</span> Амазонки. Если считать оттуда, Амазонка получается <strong>длиннее</strong> — почти 6992 километра.</p>

<p><span class="cn-word" data-tr="bahs">Спор</span> идёт до сих пор. И дело не в <span class="cn-word" data-tr="oʻlchov asboblari">приборах</span>.</p>

<p>Дело в том, что у большой реки нет одной точки начала. У большой реки <span class="cn-word" data-tr="oʻnlab">десятки</span> <span class="cn-word" data-tr="irmoqlar">притоков</span>. Который из них считать <span class="cn-word" data-tr="asosiy">главным</span>? Тот, что <strong>длиннее</strong>? Тот, что <span class="cn-word" data-pos="verb" data-tr="olib boradi">несёт</span> <strong>больше</strong> воды? Тот, что <strong>выше</strong> в горах? Каждый ответ даёт другую цифру.</p>

<p>С <span class="cn-word" data-tr="quyilish joyi, deltasi">устьем</span> ещё <strong>хуже</strong>. Амазонка <span class="cn-word" data-pos="verb" data-tr="quyiladi">впадает</span> в океан широкой <span class="cn-word" data-tr="daryo ogʻzi, keng quyilish">дельтой</span>, и границу между рекой и океаном каждый учёный проводит <span class="cn-word" data-tr="har xil, boshqacha">по-разному</span>.</p>

<p>Зато в одном спора нет. По <span class="cn-word" data-tr="suv miqdori">количеству воды</span> Амазонка — первая, и <strong>гораздо</strong> впереди <strong>всех</strong> остальных. Она одна несёт в океан примерно <strong>пятую часть</strong> всей речной воды Земли.</p>

<p>Для <span class="cn-word" data-tr="solishtirish uchun">сравнения</span>: Волга, <strong>самая длинная</strong> река Европы, короче Амазонки почти в два раза — 3530 километров.</p>

<p>Так какая река <strong>самая длинная</strong>? <span class="cn-word" data-tr="halol, rostini aytganda">Честный</span> ответ: <span class="cn-word" data-tr="qarab turadi">зависит</span> от того, где вы решите, что река началась.</p>

<p><strong>Больше всего</strong> здесь интересно другое. Вопрос был не о реке. Он был о том, как мы <span class="cn-word" data-pos="verb" data-tr="oʻlchaymiz">измеряем</span>.</p>''',
        "questions": [
            {
                "text": "Nega «eng uzun daryo qaysi?» degan savolga aniq javob yoʻq?",
                "choices": [
                    "Chunki oʻlchov asboblari aniq emas",
                    "Chunki daryolar har yili uzunligini oʻzgartiradi",
                    "Chunki daryoning qayerda boshlanishi va tugashini har kim boshqacha belgilaydi",
                    "Chunki Nil bilan Amazonka bir xil uzunlikda"
                ],
                "answer": 2,
                "explanation": "«Дело не в приборах» deb matn ochiq aytadi. "
                               "Irmoqlarning qaysi biri asosiy sanalishi va "
                               "delta qayerda tugashi — ikkalasi ham "
                               "kelishilmagan.",
            },
            {
                "text": "Nega matnda «короче Амазонки», lekin «длиннее, чем Амазонка» ham boʻlishi mumkin edi?",
                "choices": [
                    "Chunki ikkalasi ham toʻgʻri — bu solishtirishning ikki yoʻli",
                    "Chunki «короче» faqat Родительный bilan ishlatiladi",
                    "Chunki «чем» faqat odamlar haqida ishlatiladi",
                    "Chunki bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "«Чем + Именительный» (vergul bilan) va «чем» siz "
                               "Родительный — ikkalasi ham meʼyorda. Ikkinchisi "
                               "oʻzbekcha «Amazonka<b>dan</b> qisqa» ga aynan "
                               "toʻgʻri keladi.",
            },
            {
                "text": "Amazonka nimasi bilan shubhasiz birinchi?",
                "choices": [
                    "Uzunligi bilan",
                    "Irmoqlari soni bilan",
                    "Balandligi bilan",
                    "Okeanga olib boradigan suv miqdori bilan — dunyo daryo suvining beshdan bir qismi"
                ],
                "answer": 3,
                "explanation": "«По количеству воды Амазонка — первая, и "
                               "гораздо впереди всех остальных». Uzunlik "
                               "boʻyicha bahs ketadi, suv boʻyicha esa "
                               "yoʻq.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-75 — свой                                  BIOGRAFIK HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Свой дом",
        "summary": (
            "PR-75 matni. Olga yigirma yilda oʻn bir marta koʻchdi va bir "
            "quti hech qachon ochilmadi. Nihoyat oʻz kvartirasi paydo "
            "boʻlganda, u birinchi navbatda oʻsha qutini ochdi."
        ),
        "order":   75,
        "grammar": [
            {
                "pattern":  "Свой — gapning egasiga tegishli",
                "meaning":  "Oʻzbekcha «oʻz». Matnda beshta kelishikda uchraydi: "
                            "свои вещи, своей комнаты, своего угла, "
                            "своим, о своём.",
                "examples": ["Она возила свои вещи из квартиры в квартиру.",
                             "У неё не было своего угла."],
            },
            {
                "pattern":  "Свой ↔ её",
                "meaning":  "Matnda ataylab bittasi «её» qoʻyilgan — u boshqa "
                            "odamning narsasini bildiradi. Farqni koʻring.",
                "examples": ["Она открыла свою коробку. (oʻzinikini)",
                             "Она помнила её слова. (buvisining soʻzlarini)"],
            },
            {
                "pattern":  "Свой = «ijara emas, oʻziniki»",
                "meaning":  "Ikkinchi maʼnosi. Sarlavhaning oʻzi shu haqda: "
                            "«свой дом» — ijaraga olingan emas.",
                "examples": ["Наконец у неё появился свой дом."],
            },
        ],
        "body": '''<p>За двадцать лет Ольга <span class="cn-word" data-pos="verb" data-tr="koʻchdi">переезжала</span> одиннадцать раз.</p>

<p>Она <span class="cn-word" data-pos="verb" data-tr="ijaraga olardi">снимала</span> комнаты, потом <span class="cn-word" data-tr="ijaraga olingan">съёмные</span> квартиры. Каждый раз она возила из квартиры в квартиру <strong>свои</strong> вещи: две сумки одежды, лампу и коробку.</p>

<p>Коробку она <span class="cn-word" data-pos="verb" data-tr="ochmasdi">не открывала</span>.</p>

<p>Внутри лежали шесть <span class="cn-word" data-tr="tarelkalar, likopchalar">тарелок</span>. Их дала ей бабушка, когда Ольге было девятнадцать. Бабушка тогда сказала: «Откроешь, когда будет <strong>свой</strong> дом». Ольга помнила <strong>её</strong> слова точно, <span class="cn-word" data-tr="soʻzma-soʻz">слово в слово</span>.</p>

<p>В первой квартире тарелки было <span class="cn-word" data-tr="qoʻyadigan joy yoʻq">некуда ставить</span>. Во второй <span class="cn-word" data-tr="uy egasi (ayol)">хозяйка</span> не разрешала менять <span class="cn-word" data-tr="idish-tovoq">посуду</span>. В третьей Ольга <span class="cn-word" data-pos="verb" data-tr="yashadi">прожила</span> только восемь месяцев.</p>

<p>Потом она <span class="cn-word" data-pos="verb" data-tr="toʻxtatdi">перестала</span> <span class="cn-word" data-pos="verb" data-tr="ochishga urinmoq">пытаться</span>. Коробка просто переехала ещё восемь раз.</p>

<p>Ольга работала <span class="cn-word" data-tr="buxgalter">бухгалтером</span>, потом открыла <strong>своё</strong> маленькое дело. Деньги <span class="cn-word" data-pos="verb" data-tr="yigʻildi">копились</span> медленно — четырнадцать лет.</p>

<p>В сорок два года она купила квартиру. Одна комната, кухня, седьмой <span class="cn-word" data-tr="qavat">этаж</span>.</p>

<p>В день <span class="cn-word" data-tr="koʻchib oʻtish">переезда</span> Ольга не стала <span class="cn-word" data-pos="verb" data-tr="ochib joylashtirmoq">разбирать</span> сумки. Она села на пол посреди <strong>своей</strong> комнаты и открыла коробку.</p>

<p>Все шесть тарелок были <span class="cn-word" data-tr="butun, sinmagan">целые</span>.</p>

<p>Она <span class="cn-word" data-pos="verb" data-tr="yuvdi">вымыла</span> их и поставила в <span class="cn-word" data-tr="shkaf">шкаф</span>. Потом долго сидела на полу и смотрела на них.</p>

<p>Бабушка была права в одном, но не совсем. <strong>Свой</strong> дом — это не стены и не <span class="cn-word" data-tr="hujjatlar">документы</span>. Это место, где можно <span class="cn-word" data-pos="verb" data-tr="ochib, joyiga qoʻymoq">распаковать</span> последнюю коробку.</p>''',
        "questions": [
            {
                "text": "Nega Olga qutini yigirma yil davomida ochmadi?",
                "choices": [
                    "Quti qulflangan edi",
                    "U buvisining «oʻz uying boʻlganda ochasan» degan gapini eslardi",
                    "U tarelkalarni yoqtirmasdi",
                    "Quti juda ogʻir edi"
                ],
                "answer": 1,
                "explanation": "«Откроешь, когда будет свой дом». Yigirma yil "
                               "va oʻn bir koʻchish davomida bu shart "
                               "bajarilmagan edi.",
            },
            {
                "text": "Nega matnda «свои вещи», lekin «её слова»?",
                "choices": [
                    "Chunki «слова» koʻplikda",
                    "Chunki «её» qisqaroq",
                    "Bu matndagi xato",
                    "Chunki narsalar Olganiki — u gapning egasi; soʻzlar esa buvisiniki"
                ],
                "answer": 3,
                "explanation": "«Свой» faqat gapning egasiga tegishli narsani "
                               "bildiradi. Buvi boshqa odam, shuning uchun uning "
                               "soʻzlari «её слова». Agar «свои слова» "
                               "deyilsa, Olganing oʻz soʻzlari chiqardi.",
            },
            {
                "text": "Hikoya oxirida «свой дом» qanday taʼriflanadi?",
                "choices": [
                    "Devorlar va hujjatlar",
                    "Yettinchi qavatdagi kvartira",
                    "Oxirgi qutini ochish mumkin boʻlgan joy",
                    "Buvidan qolgan olti tarelka"
                ],
                "answer": 2,
                "explanation": "«Это место, где можно распаковать последнюю "
                               "коробку». Yaʼni «oʻz uy» — mulk emas, "
                               "koʻchmaslikka ishonch.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-76 — себя va сам                                    PORTRET
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Сделай сам",
        "summary": (
            "PR-76 matni. Viktor Stepanovichning ustaxonasi buzilgan narsalarni "
            "tuzatmaydi — u odamlarga oʻzlari tuzatishni oʻrgatadi. Va aslida "
            "u butunlay boshqa narsani tuzatadi."
        ),
        "order":   76,
        "grammar": [
            {
                "pattern":  "Сам — taʼkid, egaga moslashadi",
                "meaning":  "«Hech kim yordam bermadi, oʻzi qildi»: сам, сама, "
                            "сами. Ustaxonaning nomi ham shu — «Сделай сам».",
                "examples": ["Она сама починила кран.",
                             "Мальчик сам собрал велосипед."],
            },
            {
                "pattern":  "Себя / себе / собой — toʻldiruvchi",
                "meaning":  "Har doim gapning egasiga qaytadi va hamma shaxs "
                            "uchun bitta shakl. Matnda uchala kelishikda ham bor.",
                "examples": ["Он не верил в себя.",
                             "Виктор Степанович был недоволен собой."],
            },
            {
                "pattern":  "Iboralar: у себя · про себя · взять себя в руки",
                "meaning":  "Kundalik nutqning tayyor boʻlaklari. «У себя» — oʻz "
                            "joyida, «про себя» — ichida, ovoz chiqarmay.",
                "examples": ["Мастер всегда у себя с восьми утра.",
                             "Она считала про себя до десяти."],
            },
        ],
        "body": '''<p>На двери маленькой <span class="cn-word" data-tr="ustaxona">мастерской</span> <span class="cn-word" data-pos="verb" data-tr="osilib turibdi">висит</span> <span class="cn-word" data-tr="taxtacha, yozuv">табличка</span>: «Сделай <strong>сам</strong>».</p>

<p>Хозяина зовут Виктор Степанович. Он <strong>у себя</strong> с восьми утра до шести вечера.</p>

<p>Люди приносят ему <span class="cn-word" data-tr="buzilgan">сломанные</span> вещи: <span class="cn-word" data-tr="choynaklar">чайники</span>, лампы, велосипеды, <span class="cn-word" data-tr="stullar">стулья</span>. Виктор Степанович смотрит на вещь, <span class="cn-word" data-pos="verb" data-tr="bosh irgʻaydi">кивает</span> — и не берёт <span class="cn-word" data-tr="asboblar">инструменты</span>.</p>

<p>Вместо этого он <span class="cn-word" data-pos="verb" data-tr="oʻtqizadi">сажает</span> человека за стол и говорит: «Давайте вместе. <span class="cn-word" data-pos="verb" data-tr="ushlang">Держите</span> вот здесь».</p>

<p>Первые десять минут люди <span class="cn-word" data-pos="verb" data-tr="jahllari chiqadi">сердятся</span>. Они пришли <span class="cn-word" data-tr="tayyor natija uchun">за готовым результатом</span>, а не за уроком.</p>

<p>Потом всё <span class="cn-word" data-pos="verb" data-tr="oʻzgaradi">меняется</span>.</p>

<p>Наталья, <span class="cn-word" data-tr="oʻqituvchi ayol">учительница</span> из <span class="cn-word" data-tr="qoʻshni">соседней</span> школы, принесла старую лампу. Через сорок минут она <strong>сама</strong> нашла <span class="cn-word" data-tr="uzilgan sim">обрыв в проводе</span>. Она долго смотрела на свои руки и <span class="cn-word" data-pos="verb" data-tr="takrorlardi">повторяла</span> <strong>про себя</strong>: «Я это <strong>сама</strong>».</p>

<p>Один мальчик, Тимур, приходил четыре раза <span class="cn-word" data-tr="bitta velosiped bilan">с одним велосипедом</span>. На четвёртый раз он <strong>сам</strong> поменял <span class="cn-word" data-tr="zanjir">цепь</span>. Виктор Степанович даже не встал со <span class="cn-word" data-tr="stuldan">стула</span>.</p>

<p>Я спросил мастера, почему он работает так медленно. Он мог бы починить лампу за пять минут.</p>

<p>Виктор Степанович <span class="cn-word" data-pos="verb" data-tr="qoʻlini siltadi">махнул рукой</span> на табличку.</p>

<p>«Человек приносит лампу, — сказал он. — А уходит с мыслью, что <span class="cn-word" data-pos="verb" data-tr="uddalay oladi">справится</span>. В следующий раз он не пойдёт к мастеру. Он возьмёт <strong>себя</strong> в руки и попробует».</p>

<p>Он <span class="cn-word" data-pos="verb" data-tr="jim qoldi">помолчал</span> и <span class="cn-word" data-pos="verb" data-tr="qoʻshib qoʻydi">добавил</span>: «Я не чиню вещи. Я чиню то, что люди думают о <strong>себе</strong>».</p>''',
        "questions": [
            {
                "text": "Viktor Stepanovich buzilgan narsalarni nima qiladi?",
                "choices": [
                    "Tez va arzon tuzatib beradi",
                    "Ularni umuman qabul qilmaydi",
                    "Egasini stol yoniga oʻtqizib, birga tuzatishga oʻrgatadi",
                    "Yangisini sotadi"
                ],
                "answer": 2,
                "explanation": "«Давайте вместе. Держите вот здесь». Shuning "
                               "uchun eshikdagi yozuv — «Сделай сам».",
            },
            {
                "text": "Nega matnda «она сама нашла», lekin «он возьмёт себя в руки»?",
                "choices": [
                    "Chunki birinchisi ayol, ikkinchisi erkak haqida",
                    "Chunki birinchisi «kim?» degan taʼkid, ikkinchisi «kimni?» degan toʻldiruvchi",
                    "Chunki «себя» faqat kelasi zamonda ishlatiladi",
                    "Bu matndagi xato"
                ],
                "answer": 1,
                "explanation": "«Сама нашла» — hech kim yordam bermadi (taʼkid). "
                               "«Возьмёт себя в руки» — «kimni?» degan savolga "
                               "javob (toʻldiruvchi). Oʻzbekchada ikkalasi ham "
                               "«oʻzi», ruschada esa ikki xil soʻz.",
            },
            {
                "text": "Usta oʻz ishini qanday tushuntiradi?",
                "choices": [
                    "U narsalarni emas, odamlarning oʻzlari haqidagi fikrini tuzatadi",
                    "U shunchaki sekin ishlashni yoqtiradi",
                    "U yordamchi topa olmaydi",
                    "U asboblarini hech kimga bermaydi"
                ],
                "answer": 0,
                "explanation": "«Я не чиню вещи. Я чиню то, что люди думают о "
                               "себе». Timur toʻrtinchi safar zanjirni oʻzi "
                               "almashtirgani — shuning isboti.",
            },
        ],
    },
]
