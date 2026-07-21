# Zamonaviy rus hikoyalari — stories 6-10 (Claude-authored modern short stories).
# Import: python manage.py import_corner corner/management/commands/_stories_russian_6_10.py --author=<AUTHOR>
# Narration voice alternates by story (male/female) — see gen_corner_audio calls per story order
# (6 Dmitry, 7 Svetlana, 8 Dmitry, 9 Svetlana, 10 Dmitry).

SUBJECT = {
    "name":    "Russian",
    "summary": "Rus tili: zamonaviy hikoyalar, lugʻat va grammatika bilan.",
    "icon":    "bi-translate",
    "color":   "#b91c1c",
}

COLLECTION = {
    "title":       "Zamonaviy rus hikoyalari",
    "description": "Zamonaviy rus tilida qiziqarli hikoyalar — lugʻat, grammatika, savollar va audio bilan.",
    "order":       1,
}

STORIES = [
    {
        "title":   "Дождь в чужом городе",
        "summary": "Notanish shaharda kutilmagan jaladan yashiringan safarchi mehribon doʻkonchi ayol bilan tanishadi.",
        "order":   6,
        "grammar": [
            {
                "pattern":  "как только",
                "meaning":  "...ishi bilanoq, shu zahoti (ikki harakat orasidagi tezkor bogʻliqlik).",
                "examples": ["Как только он вышел из вокзала, начался ливень.", "Как только придёшь, позвони мне."],
            },
            {
                "pattern":  "вместо того чтобы",
                "meaning":  "...ish oʻrniga (bir harakatni boshqasiga almashtirish, qarama-qarshi tanlov).",
                "examples": ["Присядьте, вместо того чтобы нервничать на улице.", "Он занялся делом, вместо того чтобы жаловаться."],
            },
            {
                "pattern":  "тем более что",
                "meaning":  "Ayniqsa shuning uchunki, qolaversa (qoʻshimcha sabab keltiruvchi kirish birikma).",
                "examples": ["Тем более что здесь у меня есть море под окном.", "Останься на ужин, тем более что уже поздно."],
            },
            {
                "pattern":  "Как бы ... ни",
                "meaning":  "...qancha harakat qilmasin (kuchli qarshilik/urinishga qaramay natija oʻzgarmasligi).",
                "examples": ["Как бы дождь ни старался, он всё же стих.", "Как бы он ни спешил, автобус он не догнал."],
            },
        ],
        "body": '''<p>Максим впервые оказался в этом небольшом приморском городке — командировка на два дня, не более. Он <span class="cn-word" data-pos="verb" data-tr="hisoblagan, moʻljallagan edi">рассчитывал</span> успеть на встречу, быстро всё обсудить и вечером уехать обратно, но, <strong>как только</strong> он вышел из вокзала, начался <span class="cn-word" data-tr="kuchli jala">ливень</span>, какого он никогда раньше не видел.</p>
<p>Зонта у него, конечно же, не оказалось. Максим побежал под <span class="cn-word" data-tr="soyabon, ayvoncha">навес</span> ближайшего магазина, <span class="cn-word" data-pos="verb" data-tr="hoʻl boʻlib">промокнув</span> насквозь за те несколько секунд, что бежал через площадь.</p>
<p>— Заходите, не стойте под дождём, — послышался голос из-за <span class="cn-word" data-tr="peshtaxta">прилавка</span>.</p>
<p>Пожилая женщина, хозяйка маленькой лавки с сувенирами, жестом пригласила его внутрь. Пока он <span class="cn-word" data-pos="verb" data-tr="silkinardi, tozalanardi">отряхивался</span>, она уже наливала горячий чай в <span class="cn-word" data-pos="adj" data-tr="sopol">глиняную</span> кружку.</p>
<p>— Спасибо, — <span class="cn-word" data-pos="adv" data-tr="andisha bilan, uyalibgina">смущённо</span> сказал Максим, — но я, кажется, опоздаю на встречу, если дождь не прекратится.</p>
<p>— Такой ливень здесь редко идёт больше часа, — <span class="cn-word" data-pos="verb" data-tr="tinchlantirdi">успокоила</span> его женщина. — Присядьте, <strong>вместо того чтобы</strong> нервничать под дождём на улице.</p>
<p>Максим послушался. Он сел у окна и, пока пил чай, разговорился с хозяйкой лавки. Оказалось, она живёт в этом городке всю жизнь и знает здесь буквально каждый камень.</p>
<p>— Вы, наверное, скучаете по большим городам, шуму, — <span class="cn-word" data-pos="verb" data-tr="taxmin qildi">предположил</span> Максим.</p>
<p>— Ничуть, — <span class="cn-word" data-tr="boshini chayqadi">покачала головой</span> она. — <strong>Тем более что</strong> здесь у меня есть море под окном и соседи, которые знают меня с детства. Разве что зимой немного <span class="cn-word" data-pos="adv" data-tr="yolgʻiz, sokin">одиноко</span>, когда туристов нет.</p>
<p><strong>Как бы</strong> дождь <strong>ни</strong> старался испортить его планы, он всё же <span class="cn-word" data-pos="verb" data-tr="tindi, bosildi">стих</span> через сорок минут, ровно как и предсказывала хозяйка лавки. Максим, поблагодарив женщину за чай и <span class="cn-word" data-tr="mehmondoʻstlik">гостеприимство</span>, <span class="cn-word" data-pos="verb" data-tr="shoshildi">поспешил</span> на встречу — и, как ни странно, успел вовремя.</p>
<p>Уже сидя в поезде вечером, он вспоминал не саму деловую встречу, а тёплую лавку с сувенирами, запах чая и голос женщины, для которой маленький городок был <span class="cn-word" data-tr="butun bir olam">целым миром</span>. Может быть, подумал Максим, в следующий раз он приедет сюда не по работе, а просто в гости — к морю и к той самой лавке.</p>''',
        "questions": [
            {
                "text": "Почему Максим зашёл в лавку с сувенирами?",
                "choices": [
                    "Он хотел купить подарок домой.",
                    "Он спрятался от внезапного сильного дождя.",
                    "Он заранее договорился встретиться там с хозяйкой.",
                ],
                "answer": 1,
                "explanation": "Kutilmagan kuchli jaladan qochib, u eng yaqin doʻkon peshayvoni ostiga yugurib kirgan.",
            },
            {
                "text": "Как хозяйка лавки относится к жизни в маленьком городке?",
                "choices": [
                    "Она жалеет, что не живёт в большом шумном городе.",
                    "Она довольна жизнью здесь и не скучает по большим городам.",
                    "Она мечтает как можно скорее переехать.",
                ],
                "answer": 1,
                "explanation": "\"Ничуть\" — bu javob va \"море под окном\", \"соседи с детства\" haqidagi gaplar u kichkina shaharchada baxtli yashayotganini koʻrsatadi.",
            },
            {
                "text": "Что, скорее всего, запомнилось Максиму больше всего из этой поездки?",
                "choices": [
                    "Сама деловая встреча и подписанные документы.",
                    "Тёплая беседа и гостеприимство хозяйки лавки во время дождя.",
                    "Долгая дорога на поезде.",
                ],
                "answer": 1,
                "explanation": "Matn oxirida \"он вспоминал не саму деловую встречу, а тёплую лавку ... и голос женщины\" deyilgan — demak, eng yodda qolgani aynan shu iliq muloqot boʻlgan.",
            },
        ],
    },
    {
        "title":   "Экзамен по вождению",
        "summary": "Uchinchi marta haydovchilik imtihonini topshirayotgan qiz oʻziga ishonishni oʻrganadi.",
        "order":   7,
        "grammar": [
            {
                "pattern":  "Едва ..., как",
                "meaning":  "Deyarli ...gan edi, birdaniga (ikki harakat orasidagi juda qisqa oraliq).",
                "examples": ["Едва она начала сдавать назад, как руки задрожали.", "Едва он вошёл, как зазвонил телефон."],
            },
            {
                "pattern":  "Стоило только ..., и",
                "meaning":  "Faqat ... qilish kifoya boʻldi va (кutilmagan tezkor natija — «как» oʻrniga «и» bilan variant).",
                "examples": ["Стоило только поверить в себя, и всё получилось.", "Стоило только попробовать, и страх прошёл."],
            },
            {
                "pattern":  "чего бы это ни стоило",
                "meaning":  "Har qanday narsaga arzisa ham, nima boʻlsa ham (qatʼiy niyat bildiruvchi turgʻun ibora).",
                "examples": ["У меня получится, чего бы это ни стоило.", "Мы закончим проект вовремя, чего бы это ни стоило."],
            },
            {
                "pattern":  "Пока ..., ... будет ...",
                "meaning":  "Bir holat davom etar ekan, unga parallel boshqa holat ham davom etadi (oʻzaro bogʻliq parallel jarayon).",
                "examples": ["Пока ты будешь бояться руля, руль будет бояться тебя.", "Пока ты будешь сомневаться, другие будут действовать."],
            },
        ],
        "body": '''<p>Настя третий раз <span class="cn-word" data-pos="verb" data-tr="qayta topshirardi">пересдавала</span> экзамен по вождению, и с каждым разом <span class="cn-word" data-pos="verb" data-tr="hayajonlanardi">волновалась</span> всё сильнее. Первые две попытки закончились неудачей: один раз она <span class="cn-word" data-pos="verb" data-tr="dvigatel oʻchib qoldi">заглохла</span> на перекрёстке, во второй — <span class="cn-word" data-pos="verb" data-tr="dovdirab qoldi">растерялась</span> при развороте и задела бордюр.</p>
<p>— Не переживай так сильно, — сказал инструктор Алексей Петрович перед третьей попыткой. — <strong>Пока</strong> ты будешь бояться руля, руль будет бояться тебя.</p>
<p>Настя <span class="cn-word" data-pos="adv" data-tr="beixtiyor">невольно</span> улыбнулась этой шутке, хотя ладони у неё всё равно были <span class="cn-word" data-pos="adj" data-tr="nam">влажными</span> от волнения. Она села за руль, пристегнулась и завела двигатель, стараясь дышать ровно.</p>
<p>Экзаменатор, строгая женщина средних лет, села на переднее сиденье и начала диктовать маршрут. Первые пять минут всё шло <span class="cn-word" data-pos="adv" data-tr="silliq, muammosiz">гладко</span>: Настя аккуратно <span class="cn-word" data-pos="verb" data-tr="qatorni almashtirardi">перестраивалась</span>, <span class="cn-word" data-pos="verb" data-tr="rioya qilardi">соблюдала</span> дистанцию, вовремя включала <span class="cn-word" data-tr="burilish chiroqlari">поворотники</span>.</p>
<p>Затем начался самый сложный участок — параллельная парковка между двумя машинами. Именно на ней Настя <span class="cn-word" data-pos="verb" data-tr="yiqilgan edi (imtihondan)">срезалась</span> в первый раз. <strong>Едва</strong> она начала сдавать назад, <strong>как</strong> почувствовала, что руки <span class="cn-word" data-pos="adv" data-tr="xoinlarcha, oʻzidan-oʻzi">предательски</span> задрожали.</p>
<p>«Спокойно, — сказала она себе мысленно, — у меня получится, <strong>чего бы это ни стоило</strong>».</p>
<p>Она медленно, сантиметр за сантиметром, завела машину в промежуток, <span class="cn-word" data-pos="verb" data-tr="qarab-qarab qoʻyib">поглядывая</span> то в зеркало, то через плечо. Наконец, машина встала ровно между двумя автомобилями, не задев ни один из них.</p>
<p>— Неплохо, — <span class="cn-word" data-pos="adv" data-tr="vazmin holda">сдержанно</span> заметила экзаменатор, делая пометку в бланке.</p>
<p>Оставшуюся часть маршрута Настя проехала почти без единой ошибки, лишь слегка <span class="cn-word" data-pos="verb" data-tr="bir zum ikkilanib">замешкавшись</span> перед пешеходным переходом. Когда они вернулись на площадку и экзаменатор наконец произнесла: «Поздравляю, вы сдали», — Настя не сразу поверила своим ушам.</p>
<p>Инструктор, ждавший её у входа, широко улыбнулся:</p>
<p>— Ну что я говорил? <strong>Стоило только</strong> поверить в себя, <strong>и</strong> всё получилось.</p>
<p>Возвращаясь домой в тот вечер за рулём отцовской машины, Настя впервые почувствовала, что дорога больше не <span class="cn-word" data-pos="verb" data-tr="qoʻrqitadi">пугает</span> её, а, наоборот, зовёт вперёд.</p>''',
        "questions": [
            {
                "text": "Почему Настя так нервничала перед третьей попыткой сдать экзамен?",
                "choices": [
                    "Потому что первые две попытки закончились неудачей.",
                    "Потому что инструктор впервые с ней разговаривал.",
                    "Потому что она никогда раньше не садилась за руль.",
                ],
                "answer": 0,
                "explanation": "Matnda avvalgi ikki urinish muvaffaqiyatsiz tugagani (svetofor oldida oʻchib qolgan, bordyurga tegib ketgan) aytiladi — shuning uchun uchinchi marta yana hayajonlanadi.",
            },
            {
                "text": "Что помогло Насте успешно выполнить параллельную парковку?",
                "choices": [
                    "Она полностью перестала волноваться и действовала машинально.",
                    "Она сосредоточилась, действовала медленно и подбадривала себя мысленно.",
                    "Экзаменатор сама помогла ей припарковаться.",
                ],
                "answer": 1,
                "explanation": "\"Спокойно, у меня получится\" deb ichida oʻziga dalda berib, sekin-asta mashinani joyiga qoʻygani muvaffaqiyat sababi boʻlgan.",
            },
            {
                "text": "Какую главную мысль передаёт слова инструктора «Пока ты будешь бояться руля, руль будет бояться тебя»?",
                "choices": [
                    "Руль — это опасная часть машины, которую нужно бояться.",
                    "Внутренний страх мешает справиться с трудной задачей, а уверенность помогает.",
                    "Настоящий водитель никогда не должен садиться за руль.",
                ],
                "answer": 1,
                "explanation": "Bu gap oʻziga ishonchsizlikning oʻzi xato qilishga sabab boʻlishini, aksincha, ichki qoʻrquvni yengish muvaffaqiyat kalitini bildiradi.",
            },
        ],
    },
    {
        "title":   "Сосед по общежитию",
        "summary": "Ikki xil xarakterli talaba yotoqxonada birga yashab, kutilmagan doʻstlikka aylanadi.",
        "order":   8,
        "grammar": [
            {
                "pattern":  "тогда как",
                "meaning":  "...boʻlsa-da, aksincha (ikki holatni qarama-qarshi qoʻyuvchi bogʻlovchi).",
                "examples": ["Артём любил тишину, тогда как Стас мог работать только под музыку.", "Она любит горы, тогда как он предпочитает море."],
            },
            {
                "pattern":  "не выдержал",
                "meaning":  "Chidab turolmadi, sabri chidamadi (kutilgan vaziyatga qarshilik koʻrsatib gapirib yuborish).",
                "examples": ["Не выдержал, — сказал Артём через неделю.", "Он молчал два дня, но потом не выдержал и всё рассказал."],
            },
            {
                "pattern":  "хотя бы",
                "meaning":  "Kamida, hech boʻlmaganda (eng kam talab qilinadigan darajani bildiruvchi zarracha).",
                "examples": ["Стас стал убирать за собой хотя бы иногда.", "Позвони мне хотя бы вечером."],
            },
            {
                "pattern":  "не + деепричастие",
                "meaning":  "...masdan, ...may (inkor shaklidagi deepричастие qoʻshimcha harakatning yoʻqligini bildiradi).",
                "examples": ["Подарок бабушки сломался, — тихо ответил Стас, не поднимая головы.", "Он вышел, не сказав ни слова."],
            },
        ],
        "body": '''<p>Артём заселился в общежитие первого сентября и сразу понял: с соседом по комнате ему не повезло. Пока сам Артём аккуратно <span class="cn-word" data-pos="verb" data-tr="terib qoʻyardi">раскладывал</span> книги по полкам и <span class="cn-word" data-pos="verb" data-tr="toʻshardi (karavot)">застилал</span> кровать ровными углами, его сосед Стас, будущий инженер, <span class="cn-word" data-pos="verb" data-tr="sochib tashlardi">разбрасывал</span> вещи по всей комнате, будто жил один.</p>
<p>— Слушай, — <strong>не выдержал</strong> Артём через неделю, — может, договоримся хотя бы посуду мыть сразу, а не <span class="cn-word" data-pos="verb" data-tr="yigʻib qoʻymoq, toʻplab qoʻymoq">копить</span> её на подоконнике?</p>
<p>Стас <span class="cn-word" data-tr="yelka qisdi">пожал плечами</span>:</p>
<p>— Да я как-то не привык обращать на это внимание. Дома мама всегда убирала.</p>
<p>Первый месяц прошёл в постоянных <span class="cn-word" data-pos="adj" data-tr="mayda-chuyda">мелких</span> спорах: то из-за громкой музыки по ночам, то из-за <span class="cn-word" data-pos="adj" data-tr="sochilib yotgan">разбросанных</span> проводов от наушников. Артём, студент филологического факультета, любил тишину для чтения, <strong>тогда как</strong> Стас, наоборот, мог заниматься <span class="cn-word" data-tr="chizmalar">чертежами</span> только под музыку.</p>
<p>Однажды, вернувшись поздно вечером, Артём застал Стаса за странным занятием: тот сидел на полу, <span class="cn-word" data-pos="adj" data-tr="oʻralgan">окружённый</span> деталями старого будильника, и пытался его починить.</p>
<p>— Что случилось? — спросил Артём, стараясь не показывать раздражения из-за очередного <span class="cn-word" data-tr="tartibsizlik">беспорядка</span>.</p>
<p>— Подарок бабушки сломался, — тихо ответил Стас, <strong>не поднимая головы</strong>. — Хочу успеть починить до её звонка в воскресенье, чего бы это ни стоило.</p>
<p>Артём, до этого момента считавший соседа просто <span class="cn-word" data-tr="tartibsiz odam">неряхой</span>, вдруг увидел его совсем другим человеком. Он молча сел рядом и, вспомнив, что неплохо разбирается в электронике, начал помогать.</p>
<p>Они <span class="cn-word" data-pos="verb" data-tr="band boʻlib oʻtirishdi">провозились</span> с будильником до глубокой ночи, зато к утру механизм снова тикал <span class="cn-word" data-pos="adv" data-tr="yaxshi ishlab, nosozliksiz">исправно</span>. С того вечера что-то в их отношениях изменилось: Стас стал убирать за собой <strong>хотя бы</strong> иногда, а Артём — <span class="cn-word" data-pos="adj" data-tr="sabrliroq, chidamliroq">терпимее</span> относиться к беспорядку соседа, помня, что за каждой мелочью может <span class="cn-word" data-pos="verb" data-tr="yashiringan boʻlishi mumkin">скрываться</span> история.</p>
<p>К концу семестра они уже не <span class="cn-word" data-pos="verb" data-tr="tasavvur qilishardi">представляли</span> себе комнату без шуток друг друга по утрам, и оба решили остаться в одной комнате и на следующий год.</p>''',
        "questions": [
            {
                "text": "Почему Артём и Стас часто спорили в начале учебного года?",
                "choices": [
                    "У них были совершенно разные привычки и образ жизни.",
                    "Они учились на одном факультете и соревновались за оценки.",
                    "Их родители не разрешали им дружить.",
                ],
                "answer": 0,
                "explanation": "Artyom tartib va sukunatni yaxshi koʻrsa, Stas aksincha tartibsiz va musiqa ostida ishlaydi — bu farq mayda-chuyda janjallarga sabab boʻlgan.",
            },
            {
                "text": "Что изменило отношение Артёма к Стасу?",
                "choices": [
                    "Он увидел, как Стас старается починить сломанный подарок бабушки.",
                    "Комендант общежития заставил их подружиться.",
                    "Стас переехал в другую комнату.",
                ],
                "answer": 0,
                "explanation": "Buvisining sinigan sovgʻasini tuzatishga urinayotgan Stasni koʻrib, Artyom uni butunlay boshqa odam sifatida koʻra boshlaydi.",
            },
            {
                "text": "Как изменились оба соседа к концу семестра, согласно тексту?",
                "choices": [
                    "Ничего не изменилось — они остались такими же, как раньше.",
                    "Они стали терпимее друг к другу и захотели остаться соседями и дальше.",
                    "Они поссорились окончательно и разъехались.",
                ],
                "answer": 1,
                "explanation": "Matn oxirida Stas hech boʻlmaganda vaqti-vaqti bilan tozalik saqlashni boshlagani, Artyom esa sabrliroq boʻlgani va ikkalasi keyingi yil ham birga qolishga qaror qilgani aytiladi.",
            },
        ],
    },
    {
        "title":   "Утренняя пробежка",
        "summary": "Yugurishni yangi boshlagan ayol parkdagi keksa yuguruvchidan taslim boʻlmaslikni oʻrganadi.",
        "order":   9,
        "grammar": [
            {
                "pattern":  "до того как",
                "meaning":  "...dan oldin (payt ergash gapini boshlovchi, keyingi voqeadan ilgarigi payt).",
                "examples": ["Начал ещё до того, как это стало модным.", "Позвони мне до того, как выйдешь из дома."],
            },
            {
                "pattern":  "Чем ..., тем ...",
                "meaning":  "Qancha ..., shuncha ... (nisbiy qiyoslash konstruksiyasi).",
                "examples": ["Чем дольше бегаешь, тем легче становится.", "Чем раньше начнёшь, тем быстрее привыкнешь."],
            },
            {
                "pattern":  "иначе бы",
                "meaning":  "Aks holda, ...gan boʻlar edi (shart bajarilmasa nima sodir boʻlishi mumkinligini bildiruvchi konstruksiya).",
                "examples": ["Иначе бы я давно бросил, как и большинство новичков.", "Поторопись, иначе бы мы опоздали."],
            },
            {
                "pattern":  "не только потому, что ..., но и потому, что ...",
                "meaning":  "Nafaqat ... sababli, balki ... sababli ham (ikkita sababni parallel keltiruvchi konstruksiya).",
                "examples": ["Она бегала не только потому, что так велел врач, но и потому, что хотела бежать легко.", "Он учится не только потому, что нужно, но и потому, что ему интересно."],
            },
        ],
        "body": '''<p>Каждое утро в шесть тридцать Лена выходила на <span class="cn-word" data-tr="yugurish, kross">пробежку</span> в парк неподалёку от дома — привычка, которую она <span class="cn-word" data-pos="verb" data-tr="boshlab yubordi (odat haqida)">завела</span> всего месяц назад, после того как врач посоветовал ей больше двигаться. Первые недели дались тяжело: уже через пятьсот метров у неё начинало <span class="cn-word" data-tr="biqinida sanchiq turmoq">колоть в боку</span>, а ноги наливались свинцом.</p>
<p>Именно тогда она заметила пожилого мужчину, который бегал в парке в одно и то же время. Ему, судя по <span class="cn-word" data-tr="oqargan soch">седине</span>, было не меньше семидесяти, но бежал он ровным, <span class="cn-word" data-pos="adj" data-tr="ishonchli">уверенным</span> шагом, будто вообще не замечал <span class="cn-word" data-tr="charchoq">усталости</span>.</p>
<p>Однажды, остановившись <span class="cn-word" data-pos="verb" data-tr="nafasini rostlab olmoq">отдышаться</span> на скамейке, Лена невольно спросила:</p>
<p>— Простите, а вы давно бегаете?</p>
<p>— Тридцать два года, — улыбнулся мужчина, присаживаясь рядом. — Начал ещё <strong>до того, как</strong> это стало модным.</p>
<p>— А не тяжело в вашем возрасте? — <span class="cn-word" data-pos="verb" data-tr="andisha qilib, uyalib">смутившись</span> своего вопроса, спросила Лена.</p>
<p>— Тяжело было в первый год, когда я только начинал, — ответил он. — Ровно как вам сейчас. Но <strong>чем</strong> дольше бегаешь, <strong>тем</strong> легче становится, только не <span class="cn-word" data-pos="verb" data-tr="taslim boʻlmang">сдавайтесь</span> в первые месяцы, <strong>иначе бы</strong> я давно бросил, как и большинство <span class="cn-word" data-tr="yangi boshlovchilar">новичков</span>.</p>
<p>С того дня Лена стала выходить на пробежку <strong>не только потому, что</strong> так велел врач, <strong>но и потому, что</strong> ей хотелось однажды бежать так же легко, как этот мужчина. Она перестала обращать внимание на боль в боку, научилась дышать правильно и постепенно начала замечать, как меняется её тело.</p>
<p>Через два месяца, встретив своего утреннего знакомого снова, она пробежала рядом с ним весь <span class="cn-word" data-pos="adj" data-tr="odatdagi">привычный</span> круг, ни разу не остановившись.</p>
<p>— Ну вот, — сказал он <span class="cn-word" data-pos="adv" data-tr="maʼqullab, hayrixoh boʻlib">одобрительно</span>, — теперь вы одна из нас, из тех сумасшедших, кто бегает в любую погоду.</p>
<p>Лена <span class="cn-word" data-pos="verb" data-tr="kulib yubordi">рассмеялась</span>, но в глубине души почувствовала <span class="cn-word" data-tr="faxr">гордость</span>. Она поняла: дело было не в беге как таковом, а в том, чтобы не сдаваться, когда кажется, что сил больше нет.</p>''',
        "questions": [
            {
                "text": "Почему Лена начала бегать по утрам?",
                "choices": [
                    "Врач посоветовал ей больше двигаться.",
                    "Она готовилась к спортивным соревнованиям.",
                    "Пожилой мужчина из парка уговорил её начать.",
                ],
                "answer": 0,
                "explanation": "Matn boshida shifokor unga koʻproq harakatlanishni maslahat bergani aytiladi — shu sabab u yugurishni boshlagan.",
            },
            {
                "text": "Какой совет дал пожилой мужчина Лене?",
                "choices": [
                    "Бегать только по вечерам, а не по утрам.",
                    "Не сдаваться в первые трудные месяцы, потому что дальше становится легче.",
                    "Сразу бегать на длинные дистанции без подготовки.",
                ],
                "answer": 1,
                "explanation": "\"Чем дольше бегаешь, тем легче становится, только не сдавайтесь в первые месяцы\" — bu uning asosiy maslahati.",
            },
            {
                "text": "В чём, по мнению Лены в конце рассказа, было главное достижение?",
                "choices": [
                    "В том, что она пробежала быстрее пожилого мужчины.",
                    "В том, чтобы не сдаваться, когда кажется, что сил больше нет.",
                    "В том, что она купила новую спортивную одежду.",
                ],
                "answer": 1,
                "explanation": "Matn oxirida aynan shu jumla bilan yakunlanadi — asosiy narsa yugurishning oʻzida emas, balki taslim boʻlmaslikda ekani taʼkidlanadi.",
            },
        ],
    },
    {
        "title":   "Старый велосипед",
        "summary": "Ota eski velosipedni oʻgʻli bilan birga taʼmirlab, unga sabr va mehnat qadrini oʻrgatadi.",
        "order":   10,
        "grammar": [
            {
                "pattern":  "пока ... не",
                "meaning":  "...magunicha, ...ishga qadar (biror harakat sodir boʻlmagunicha davom etadigan holat).",
                "examples": ["Пока мы с тобой не починим его вместе, он и не поедет.", "Не уходи, пока не доешь ужин."],
            },
            {
                "pattern":  "Чем ..., тем ...",
                "meaning":  "Qancha ..., shuncha ... (nisbiy qiyoslash konstruksiyasi).",
                "examples": ["Чем лучше ты за чем-то ухаживаешь, тем дольше оно служит.", "Чем чаще практикуешься, тем увереннее становишься."],
            },
            {
                "pattern":  "прежде чем",
                "meaning":  "...dan oldin, ...gacha (bir voqeadan avvalgi payt oralig'ini bildiruvchi bogʻlovchi).",
                "examples": ["Прошёл месяц, прежде чем велосипед обрёл прежний вид.", "Подумай хорошо, прежде чем решать."],
            },
            {
                "pattern":  "сам того не замечая",
                "meaning":  "Oʻzi sezmay qolib, beixtiyor ravishda (turgʻun deepричastie ibora).",
                "examples": ["Мальчик, сам того не замечая, проехал несколько метров самостоятельно.", "Сам того не замечая, он начал улыбаться."],
            },
        ],
        "body": '''<p>В гараже, среди старых коробок и запчастей, отец Дениса нашёл велосипед, на котором сам катался в детстве. Рама была <span class="cn-word" data-pos="adj" data-tr="zanglagan">ржавой</span>, цепь <span class="cn-word" data-pos="verb" data-tr="ishlamay qolardi, tirishib qolardi">заедала</span>, а одно колесо давно <span class="cn-word" data-pos="verb" data-tr="havosi chiqib ketgan edi">спустило</span>, но Сергей Николаевич, разглядывая находку, вдруг решил: он отремонтирует этот велосипед для сына, вместо того чтобы покупать новый.</p>
<p>Денису было шесть лет, и он давно просил купить ему велосипед, глядя, как соседские дети катаются во дворе. Узнав о находке отца, мальчик <span class="cn-word" data-pos="adv" data-tr="ishonchsiz holda">недоверчиво</span> покосился на ржавую раму:</p>
<p>— Он вообще ездит?</p>
<p>— Пока нет, — честно ответил отец. — Но <strong>пока</strong> мы с тобой <strong>не</strong> починим его вместе, он и не поедет сам по себе.</p>
<p>Каждые выходные они вдвоём выходили в гараж: отец объяснял, как снять цепь, <span class="cn-word" data-pos="verb" data-tr="tozalamoq">зачистить</span> ржавчину и смазать механизм, а Денис, хоть и был ещё мал, старательно подавал инструменты и задавал бесконечные вопросы.</p>
<p>— А зачем смазывать? — спрашивал он.</p>
<p>— Чтобы части двигались легко и не скрипели, — <span class="cn-word" data-pos="adv" data-tr="sabr bilan">терпеливо</span> объяснял отец. — Как и в жизни: <strong>чем</strong> лучше ты за чем-то ухаживаешь, <strong>тем</strong> дольше оно служит.</p>
<p>Прошёл месяц, <strong>прежде чем</strong> велосипед наконец обрёл прежний вид: рама блестела свежей краской, цепь щёлкала ровно, а оба колеса крутились без единого скрипа.</p>
<p>Настал день первой поездки. Сергей Николаевич <span class="cn-word" data-pos="verb" data-tr="ushlab turardi">придерживал</span> сиденье, пока Денис неуверенно крутил педали, <span class="cn-word" data-pos="verb" data-tr="tebranib, u yoq-bu yoqqa moyillanib">виляя</span> из стороны в сторону. Как только отец отпустил руки, мальчик, <strong>сам того не замечая</strong>, проехал несколько метров самостоятельно — и радостно закричал от <span class="cn-word" data-tr="zavq, hayajon">восторга</span>.</p>
<p>— Папа, я еду! Я сам еду!</p>
<p>Сергей Николаевич стоял посреди двора, глядя вслед сыну, и думал о том, что этот велосипед, который когда-то был его собственным детством, теперь становится частью детства Дениса. Иногда, подумал он, самые ценные подарки — это не новые вещи, а то время, что ты вложил в старые.</p>''',
        "questions": [
            {
                "text": "Почему отец решил отремонтировать старый велосипед, а не купить новый?",
                "choices": [
                    "У семьи не было денег на новый велосипед.",
                    "Он хотел провести время с сыном и передать ему свою вещь из детства.",
                    "В магазинах не было велосипедов нужного размера.",
                ],
                "answer": 1,
                "explanation": "Matn oxirida otaning fikri aniq aytiladi: eng qimmatli sovgʻa — bu yangi narsa emas, balki eskisiga sarflangan vaqt va eʼtibor.",
            },
            {
                "text": "Как отец объясняет сыну, зачем нужно смазывать механизм велосипеда?",
                "choices": [
                    "Чтобы велосипед выглядел красивее.",
                    "Проводя параллель с жизнью: чем лучше заботишься о чём-то, тем дольше оно служит.",
                    "Просто потому, что так написано в инструкции.",
                ],
                "answer": 1,
                "explanation": "Ota bu gapni hayotga oʻxshatib tushuntiradi: nimagadir yaxshi gʻamxoʻrlik qilsang, u shuncha uzoq xizmat qiladi.",
            },
            {
                "text": "Что символизирует последняя фраза о «времени, вложенном в старые вещи»?",
                "choices": [
                    "Что старые вещи всегда лучше новых по качеству.",
                    "Что забота и совместно проведённое время ценнее денег, потраченных на новую вещь.",
                    "Что новые велосипеды опасны для маленьких детей.",
                ],
                "answer": 1,
                "explanation": "Butun hikoya ota-oʻgʻilning birga oʻtkazgan vaqti va mehnati eng qimmatli sovgʻa ekanini koʻrsatadi — bu asosiy gʻoya.",
            },
        ],
    },
]
