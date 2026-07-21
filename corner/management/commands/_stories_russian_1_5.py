# Zamonaviy rus hikoyalari — stories 1-5 (Claude-authored modern short stories).
# Import: python manage.py import_corner corner/management/commands/_stories_russian_1_5.py --author=<AUTHOR>

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
        "title":   "Кофе на набережной",
        "summary": "Oʻn yildan keyin sohilboʻyida tasodifan uchrashib qolgan ikki maktabdosh haqida iliq hikoya.",
        "order":   1,
        "grammar": [
            {
                "pattern":  "Если бы ..., ... бы",
                "meaning":  "Real boʻlmagan shart (subjunktiv): agar ... boʻlganida edi, ... boʻlar edi.",
                "examples": ["Если бы у меня было время, я бы поехал с тобой.", "Если бы он знал правду, он бы не молчал."],
            },
            {
                "pattern":  "Чем ..., тем ...",
                "meaning":  "Qancha koʻp/koʻproq ..., shuncha koʻp/koʻproq ... (nisbiy qiyoslash konstruksiyasi).",
                "examples": ["Чем больше людей мы соберём, тем веселее будет вечер.", "Чем раньше ты начнёшь, тем быстрее закончишь."],
            },
            {
                "pattern":  "Ни ..., ни ...",
                "meaning":  "Na ..., na ... (ikkala tomonni ham inkor etuvchi bogʻlovchi).",
                "examples": ["Ни Анна, ни Виктор не заметили, как пролетело время.", "У меня нет ни времени, ни денег на это."],
            },
            {
                "pattern":  "деепричастие (-в / -я)",
                "meaning":  "Deepричастие — asosiy harakat bilan bir vaqtda yoki undan oldin sodir boʻlgan qoʻshimcha harakatni bildiradi.",
                "examples": ["Взглянув на часы, она вздохнула.", "Возвращаясь домой, он думал о разговоре."],
            },
        ],
        "body": '''<p>Анна <span class="cn-word" data-pos="verb" data-tr="yurardi (sekin)">шла</span> по набережной, <span class="cn-word" data-pos="verb" data-tr="zavqlanib, huzur qilib">наслаждаясь</span> <span class="cn-word" data-pos="adj" data-tr="toza, salqin">свежим</span> морским воздухом. Был субботний вечер, и город наконец-то <span class="cn-word" data-pos="verb" data-tr="sovib borardi">остывал</span> после жаркого дня. Она вышла из офиса <span class="cn-word" data-pos="adv" data-tr="kech">поздно</span> и решила прогуляться, прежде чем ехать домой.</p>
<p>Вдруг кто-то <span class="cn-word" data-pos="verb" data-tr="chaqirdi (orqadan)">окликнул</span> её по имени. Анна <span class="cn-word" data-pos="verb" data-tr="orqasiga oʻgirildi">обернулась</span> и не поверила своим глазам: перед ней стоял Виктор — её школьный друг, которого она не видела уже десять лет.</p>
<p>— Не может быть! — <span class="cn-word" data-pos="verb" data-tr="hayqirdi">воскликнула</span> она, улыбаясь. — Что ты здесь делаешь?</p>
<p>— <span class="cn-word" data-pos="verb" data-tr="koʻchib oʻtdi">Переехал</span> сюда полгода назад, — ответил Виктор. — Работаю в новой компании. А ты как?</p>
<p>Они сели за столик маленького кафе у моря и заказали кофе. Разговор <span class="cn-word" data-pos="verb" data-tr="erkin oqib ketdi">полился</span> сам собой, будто и не было этих десяти лет <span class="cn-word" data-tr="ayriliq">разлуки</span>. Виктор рассказал, что женился, у него растёт сын, и что он до сих пор вспоминает их школьные годы с <span class="cn-word" data-tr="iliqlik">теплотой</span>.</p>
<p>Анна <span class="cn-word" data-pos="verb" data-tr="tan oldi, aytib berdi">призналась</span>, что после университета она много путешествовала, <span class="cn-word" data-pos="verb" data-tr="almashtirdi">сменила</span> несколько профессий, пока наконец не нашла работу, которая ей действительно нравится.</p>
<p>— Знаешь, — сказал Виктор, — я часто думал о том, как сложились судьбы наших <span class="cn-word" data-tr="sinfdoshlar">одноклассников</span>. Интересно, где сейчас Марина, Олег...</p>
<p><strong>Если бы</strong> у нас было больше времени, мы <strong>могли бы</strong> <span class="cn-word" data-pos="verb" data-tr="tashkil qilmoq">устроить</span> встречу выпускников, — предложила Анна.</p>
<p>— <span class="cn-word" data-pos="adj" data-tr="ajoyib">Отличная</span> идея! <strong>Чем</strong> больше людей мы соберём, <strong>тем</strong> веселее будет вечер.</p>
<p>Пока они разговаривали, солнце медленно опускалось за горизонт, <span class="cn-word" data-pos="verb" data-tr="boʻyab, rang berib">окрашивая</span> небо в оранжевые и розовые тона. <strong>Ни</strong> Анна, <strong>ни</strong> Виктор не заметили, как <span class="cn-word" data-pos="verb" data-tr="chinakam tez oʻtib ketdi">пролетело</span> три часа.</p>
<p>Наконец, <strong>взглянув</strong> на часы, Анна <span class="cn-word" data-pos="verb" data-tr="xoʻrsindi">вздохнула</span>:</p>
<p>— Мне пора. Но я очень рада, что мы встретились.</p>
<p>— Давай <span class="cn-word" data-pos="verb" data-tr="almashamiz">обменяемся</span> номерами, — предложил Виктор. — Не хочу снова потерять с тобой связь.</p>
<p>Они обменялись телефонами и <span class="cn-word" data-pos="verb" data-tr="kelishib oldilar">договорились</span> созвониться на следующей неделе, чтобы начать планировать встречу одноклассников. <strong>Возвращаясь</strong> домой, Анна улыбалась про себя, думая о том, как порой одна <span class="cn-word" data-pos="adj" data-tr="tasodifiy">случайная</span> встреча может <span class="cn-word" data-pos="verb" data-tr="eslatmoq">напомнить</span> о том, что действительно важно в жизни.</p>''',
        "questions": [
            {
                "text": "Почему Анна и Виктор были так удивлены при встрече на набережной?",
                "choices": [
                    "Они случайно встретились после десяти лет без общения.",
                    "Они заранее договорились там встретиться.",
                    "Они никогда раньше не были знакомы.",
                ],
                "answer": 0,
                "explanation": "Matnda ular oldindan hech qanday kelishuvsiz tasodifan koʻrishib qolgani va oʻn yildan beri koʻrishmaganligi aytiladi.",
            },
            {
                "text": "Что предложила Анна в конце разговора?",
                "choices": [
                    "Никогда больше не встречаться.",
                    "Организовать встречу одноклассников.",
                    "Вместе переехать в другой город.",
                ],
                "answer": 1,
                "explanation": "Anna \"давайте устроим встречу выпускников\" deb taklif qiladi — sinfdoshlar bilan uchrashuv tashkil qilishni maʼqul koʻradi.",
            },
            {
                "text": "Что можно понять о характере их старой дружбы из этого текста?",
                "choices": [
                    "Их дружба легко возобновилась, будто разлуки и не было.",
                    "Им было трудно вспомнить друг друга.",
                    "Они поссорились из-за прошлого.",
                ],
                "answer": 0,
                "explanation": "\"Разговор полился сам собой, будто и не было этих десяти лет разлуки\" — bu ularning doʻstligi chuqur va tabiiy ravishda davom etganini koʻrsatadi.",
            },
        ],
    },
    {
        "title":   "Опоздавший поезд",
        "summary": "Bir xil poyezdga kechikkan ikki begona odam — kutilmagan uchrashuv yangi hayot boshlanishiga aylanadi.",
        "order":   2,
        "grammar": [
            {
                "pattern":  "Если бы ... не ..., ... бы не ...",
                "meaning":  "Oʻtmishda sodir boʻlmagan shart (manfiy subjunktiv): agar ... boʻlmaganida edi, ... boʻlmas edi.",
                "examples": ["Если бы я не опоздала, мы бы не встретились.", "Если бы он не позвонил, я бы не узнала новость."],
            },
            {
                "pattern":  "Придётся + infinitiv",
                "meaning":  "Majburiy zaruriyat: ...ishga toʻgʻri keladi (istaklardan qatʼi nazar).",
                "examples": ["Придётся ждать следующего поезда.", "Если не успеем, придётся возвращаться завтра."],
            },
            {
                "pattern":  "судя по всему",
                "meaning":  "Shundan koʻrinishicha, chamasi (kirish soʻz birikmasi — taxmin bildiradi).",
                "examples": ["Судя по всему, дождь начнётся к вечеру.", "Судя по всему, он тоже опоздал."],
            },
            {
                "pattern":  "деепричастие несовершенного вида (-я / -а)",
                "meaning":  "Nomukammal deepричастие — asosiy harakat bilan bir vaqtda davom etayotgan harakatni bildiradi.",
                "examples": ["Он говорил, улыбаясь.", "Рассказывая историю, она смеялась."],
            },
        ],
        "body": '''<p>Пётр <span class="cn-word" data-pos="verb" data-tr="yugurardi">бежал</span> по перрону, <strong>задыхаясь</strong> от быстрого бега. Часы показывали без одной минуты семь, а поезд на Казань отправлялся ровно в семь. Он не мог позволить себе опоздать — впереди была важная деловая встреча.</p>
<p>К сожалению, как только он подбежал к своему вагону, двери с шипением закрылись, и поезд <span class="cn-word" data-pos="verb" data-tr="qoʻzgʻaldi, joyidan jildi">тронулся</span>. Пётр остановился, тяжело <strong>дыша</strong>, и с <span class="cn-word" data-tr="afsus, xafagarchilik">досадой</span> посмотрел вслед уходящему составу.</p>
<p>— Не повезло, — <span class="cn-word" data-pos="verb" data-tr="eshitildi (ovoz haqida)">раздался</span> рядом женский голос.</p>
<p>Пётр обернулся и увидел девушку с большим рюкзаком, которая, <strong>судя по всему</strong>, тоже <span class="cn-word" data-pos="verb" data-tr="kechikdi">опоздала</span>.</p>
<p>— Да уж, — <span class="cn-word" data-pos="verb" data-tr="xoʻrsindi">вздохнул</span> он. — <strong>Придётся</strong> ждать следующего поезда. А он будет только через три часа.</p>
<p>— Зато у нас есть время выпить кофе, — улыбнулась девушка. — Меня зовут Оля, кстати.</p>
<p>Так они <span class="cn-word" data-pos="verb" data-tr="tanishib oldilar">познакомились</span>. Пока ждали следующий поезд, Пётр и Оля <span class="cn-word" data-pos="verb" data-tr="suhbatlashishdi">разговорились</span> в маленьком кафе на вокзале. Оказалось, что оба ехали в Казань по работе — он на переговоры, она на конференцию архитекторов.</p>
<p>Чем дольше они <span class="cn-word" data-pos="verb" data-tr="suhbatlashishdi">беседовали</span>, тем яснее становилось, что у них много <span class="cn-word" data-tr="umumiylik">общего</span>: оба любили путешествовать, оба выросли в маленьких городах и оба <span class="cn-word" data-pos="verb" data-tr="orzu qilishardi">мечтали</span> когда-нибудь переехать к морю.</p>
<p>— Знаешь, — сказала Оля, — <strong>если бы</strong> я <strong>не</strong> опоздала на тот поезд, мы <strong>бы</strong> никогда <strong>не</strong> встретились.</p>
<p>— Пожалуй, ты права, — засмеялся Пётр. — Иногда опоздание — это судьба.</p>
<p>Когда объявили посадку на следующий поезд, оба уже не хотели <span class="cn-word" data-pos="verb" data-tr="ajralishmoq">расставаться</span>. Они сели в один вагон, продолжая разговор всю дорогу до Казани.</p>
<p>Через полгода Пётр и Оля поженились. На свадьбе, <strong>рассказывая</strong> гостям историю своего знакомства, они всегда с улыбкой вспоминали тот самый опоздавший поезд, который на самом деле оказался не опозданием, а началом новой жизни.</p>''',
        "questions": [
            {
                "text": "Почему Пётр и Оля познакомились?",
                "choices": [
                    "Они оба опоздали на один и тот же поезд.",
                    "Их познакомили общие друзья.",
                    "Они работали в одной компании.",
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham bir xil poyezdga kechikib, stansiyada birga qolib ketishgan — shu tasodif ularni tanishtirgan.",
            },
            {
                "text": "Что реакция Оли на опоздание говорит о её характере?",
                "choices": [
                    "Она расстроилась и запаниковала.",
                    "Она отнеслась к ситуации спокойно, даже с юмором.",
                    "Она обиделась на Петра.",
                ],
                "answer": 1,
                "explanation": "\"Зато у нас есть время выпить кофе\" — bu gap Olyaning vaziyatga xotirjam va hazil bilan qaraganini koʻrsatadi.",
            },
            {
                "text": "Как в конце текста автор оценивает то опоздание на поезд?",
                "choices": [
                    "Как несчастье, которое всё испортило.",
                    "Как начало новой, счастливой жизни.",
                    "Как обычную неудачу без последствий.",
                ],
                "answer": 1,
                "explanation": "Matn oxirida \"оказался не опозданием, а началом новой жизни\" deyilgan — kechikish aslida yangi baxtli hayot boshlanishi boʻlgan.",
            },
        ],
    },
    {
        "title":   "Бабушкины блины",
        "summary": "Nabira video qoʻngʻiroq orqali buvisidan blin pishirishni oʻrganadi — masofa ortidagi oilaviy iliqlik.",
        "order":   3,
        "grammar": [
            {
                "pattern":  "Стоило только ..., как",
                "meaning":  "Faqat ... qilish yetarli boʻldi, shu zahoti (kutilmagan tezkor natija).",
                "examples": ["Стоило только повторить, как сразу получилось.", "Стоило только выйти на улицу, как начался дождь."],
            },
            {
                "pattern":  "Хотя ...",
                "meaning":  "Garchi ... boʻlsa-da (qarshi qoʻyish, ustuvor holatga qaramay).",
                "examples": ["Хотя их разделяли сотни километров, они чувствовали себя рядом.", "Хотя было поздно, она позвонила бабушке."],
            },
            {
                "pattern":  "будто",
                "meaning":  "Xuddi ..., goʻyo (oʻxshatish, taxmin bildiruvchi bogʻlovchi).",
                "examples": ["Казалось, будто они снова стоят рядом.", "Он молчал, будто ничего не случилось."],
            },
            {
                "pattern":  "Чем ..., тем ...",
                "meaning":  "Qancha ..., shuncha ... (nisbiy qiyoslash konstruksiyasi).",
                "examples": ["Чем тоньше блин, тем вкуснее.", "Чем больше практики, тем лучше результат."],
            },
        ],
        "body": '''<p>Каждое воскресенье ровно в десять утра у Кати звонил телефон — это бабушка Валентина Ивановна выходила на видеосвязь из своей деревни. Так <span class="cn-word" data-pos="verb" data-tr="shunday odat boʻlgan">повелось</span> с тех пор, как Катя переехала в город учиться, и бабушка, которая раньше и слышать не хотела о смартфонах, <span class="cn-word" data-pos="verb" data-tr="oʻrgandi">научилась</span> пользоваться видеозвонками специально ради внучки.</p>
<p>— Катенька, сегодня будем печь блины! — объявила бабушка, <span class="cn-word" data-pos="verb" data-tr="oʻrnatib">устанавливая</span> телефон на кухонный стол так, чтобы была видна плита.</p>
<p>Катя улыбнулась и достала муку, молоко и яйца — она знала это воскресное задание наизусть. Бабушка начала <span class="cn-word" data-pos="verb" data-tr="aytib turmoq (retsept)">диктовать</span> рецепт, как делала это уже много раз, но каждый раз добавляла что-то новое.</p>
<p>— Сначала взбей яйца с сахаром, а потом постепенно добавляй молоко, <span class="cn-word" data-pos="verb" data-tr="aralashtirib">помешивая</span>, чтобы не было комочков, — говорила бабушка, показывая движения руками перед камерой.</p>
<p>Пока тесто <span class="cn-word" data-pos="verb" data-tr="damlanardi (xamir haqida)">настаивалось</span>, бабушка рассказывала о том, как в детстве пекла блины вместе со своей мамой на <span class="cn-word" data-pos="adj" data-tr="oʻtinli (pech haqida)">дровяной</span> печи. Раньше, по её словам, блины пекли не абы как, а по особым случаям — на Масленицу, когда вся деревня собиралась вместе, пела песни и <span class="cn-word" data-pos="verb" data-tr="kuzatib qoʻyardi (qish)">провожала</span> зиму.</p>
<p><strong>Чем</strong> тоньше блин, <strong>тем</strong> вкуснее, — учила бабушка, наблюдая, как Катя <span class="cn-word" data-pos="adv" data-tr="ehtiyotkorlik bilan">аккуратно</span> наливает тесто на сковороду.</p>
<p>Первый блин, как всегда, получился комом — как гласит поговорка «<span class="cn-word" data-tr="birinchi urinish koʻpincha omadsiz chiqadi (maqol)">первый блин комом</span>», — но Катя, не <span class="cn-word" data-pos="verb" data-tr="xafa boʻlib">расстраиваясь</span>, вылила его обратно в миску и попробовала снова. Второй блин вышел <span class="cn-word" data-pos="adj" data-tr="oltinrang">золотистым</span> и тонким, ровно таким, каким его пекла бабушка.</p>
<p>— Вот видишь, — <span class="cn-word" data-pos="adv" data-tr="mamnun holda">довольно</span> сказала бабушка, — <strong>стоило только</strong> повторить, <strong>как</strong> сразу получилось!</p>
<p>Катя сложила стопку готовых блинов на тарелку, <span class="cn-word" data-pos="verb" data-tr="quydi (asal haqida)">полила</span> их мёдом и, откусив первый кусочек, почувствовала вкус <span class="cn-word" data-tr="bolalik">детства</span> — того самого, деревенского, бабушкиного. <strong>Хотя</strong> их <span class="cn-word" data-pos="verb" data-tr="ajratib turardi (masofa)">разделяли</span> сотни километров, в этот момент казалось, <strong>будто</strong> они снова стоят рядом, у одной плиты.</p>
<p>Закончив разговор, Катя написала бабушке короткое сообщение: «Спасибо, что научила меня не только печь блины, но и хранить традиции нашей семьи». Бабушка ответила одним смайликом-сердечком и <span class="cn-word" data-pos="verb" data-tr="vaʼda berdi">обещала</span> на следующей неделе научить внучку печь пироги.</p>''',
        "questions": [
            {
                "text": "Почему бабушка научилась пользоваться видеозвонками?",
                "choices": [
                    "Ей подарили новый телефон на день рождения.",
                    "Специально, чтобы общаться с внучкой, уехавшей учиться в город.",
                    "Потому что все соседи в деревне так делают.",
                ],
                "answer": 1,
                "explanation": "Matnda \"бабушка ... научилась пользоваться видеозвонками специально ради внучки\" deyilgan — sabab aynan nabirasi bilan aloqa saqlash.",
            },
            {
                "text": "Что, скорее всего, символизируют блины в этом рассказе?",
                "choices": [
                    "Просто блюдо, которое любит есть Катя.",
                    "Связь между поколениями и семейную традицию.",
                    "Способ бабушки заработать деньги.",
                ],
                "answer": 1,
                "explanation": "Retsept avloddan-avlodga oʻtayotgani, masofaga qaramay yaqinlik tuyulishi — hikoyaning asosiy gʻoyasi oilaviy anʼana va bogʻlanish ekanini koʻrsatadi.",
            },
            {
                "text": "Почему в тексте упоминается поговорка «первый блин комом»?",
                "choices": [
                    "Чтобы показать, что Катя готовит блины первый раз в жизни.",
                    "Чтобы показать, что неудача в начале — обычное дело, и не стоит расстраиваться.",
                    "Чтобы показать, что бабушка дала неправильный рецепт.",
                ],
                "answer": 1,
                "explanation": "Bu maqol umuman \"birinchi urinish koʻpincha muvaffaqiyatsiz chiqadi\" degan maʼnoni bildiradi — Katya xafa boʻlmay qayta urinib koʻrgani ham shuni tasdiqlaydi.",
            },
        ],
    },
    {
        "title":   "Новый сосед",
        "summary": "Yomgʻirli kechada adashib qolgan mushukcha ikki qoʻshnini haqiqiy doʻstlikka olib keladi.",
        "order":   4,
        "grammar": [
            {
                "pattern":  "не + деепричастие",
                "meaning":  "Ikkilanmasdan, oʻylab oʻtirmasdan — inkor shaklidagi deepричастие qoʻshimcha harakatning yoʻqligini bildiradi.",
                "examples": ["Не раздумывая, она занесла котёнка в квартиру.", "Не оглядываясь, он пошёл дальше."],
            },
            {
                "pattern":  "Несмотря на + Accusative",
                "meaning":  "...ga qaramasdan (qarshilik bildiruvchi konstruksiya, tushum kelishigi bilan).",
                "examples": ["Несмотря на разницу характеров, они подружились.", "Несмотря на дождь, мы пошли гулять."],
            },
            {
                "pattern":  "то ..., то ...",
                "meaning":  "Goh ..., goh ... (navbatlashib takrorlanadigan harakatlar).",
                "examples": ["То встречались у подъезда, то пили чай в гостях.", "Он то смеялся, то грустил."],
            },
            {
                "pattern":  "благодаря + Dative",
                "meaning":  "...ning tufayli, ...ga rahmat (ijobiy sabab, jo'nalish-qaratqich kelishigi bilan).",
                "examples": ["Благодаря котёнку соседи познакомились.", "Благодаря помощи друзей всё получилось."],
            },
        ],
        "body": '''<p>Когда в соседнюю квартиру <span class="cn-word" data-pos="verb" data-tr="koʻchib kirdi">въехал</span> новый жилец, Марина сразу заметила перемены: у входа появился велосипед, а по вечерам из-за стены <span class="cn-word" data-pos="verb" data-tr="eshitilib turardi">доносилась</span> тихая музыка. Соседа звали Игорь — высокий мужчина лет тридцати, который переехал сюда из другого города по работе.</p>
<p>Первое время они лишь коротко здоровались в лифте, не решаясь заговорить о чём-то большем. Марина, по натуре довольно <span class="cn-word" data-pos="adj" data-tr="yopiq, kamgap">замкнутая</span>, не спешила заводить новые знакомства, а Игорь, судя по всему, был слишком занят <span class="cn-word" data-tr="joylashib olish">обустройством</span> на новом месте.</p>
<p>Всё изменилось однажды дождливым вечером, когда Марина услышала <span class="cn-word" data-pos="adj" data-tr="zorlanuvchi, achinarli">жалобное</span> мяуканье за дверью. Открыв её, она обнаружила мокрого рыжего котёнка, <span class="cn-word" data-pos="adj" data-tr="titrayotgan">дрожащего</span> от холода. <strong>Не</strong> <strong>раздумывая</strong>, она занесла его в квартиру и завернула в полотенце.</p>
<p>Через несколько минут в дверь позвонили. На пороге стоял <span class="cn-word" data-pos="adj" data-tr="hayajonlangan">взволнованный</span> Игорь.</p>
<p>— Простите, вы не видели рыжего котёнка? Он выскочил, когда я открывал окно <span class="cn-word" data-pos="verb" data-tr="shamollatmoq">проветрить</span> комнату, — сказал он с тревогой в голосе.</p>
<p>— Заходите, он у меня, — улыбнулась Марина. — Промок, бедняга, но, кажется, уже согрелся.</p>
<p>Игорь с <span class="cn-word" data-tr="yengil tortish">облегчением</span> взял котёнка на руки, благодаря Марину за спасение своего <span class="cn-word" data-tr="uy hayvoni">питомца</span>. Так, <strong>благодаря</strong> маленькому рыжему котёнку по имени Рыжик, соседи наконец познакомились по-настоящему.</p>
<p>С того вечера они стали чаще общаться: <strong>то</strong> встречались у подъезда, <strong>то</strong> пили чай друг у друга в гостях, обсуждая книги, фильмы и, конечно же, забавные привычки Рыжика. <strong>Несмотря на</strong> разницу характеров — Марина была тихой и <span class="cn-word" data-pos="adj" data-tr="xayolchan">задумчивой</span>, а Игорь весёлым и <span class="cn-word" data-pos="adj" data-tr="ochiq muomalali, kirishimli">общительным</span>, — они быстро подружились.</p>
<p>Спустя месяц Марина призналась себе, что с нетерпением ждёт вечеров, когда сосед <span class="cn-word" data-pos="verb" data-tr="taqillatadi">стучится</span> в дверь, чтобы вместе выпить кофе. А Рыжик, довольный тем, что у него теперь два дома вместо одного, <span class="cn-word" data-pos="adv" data-tr="xotirjamgina">преспокойно</span> <span class="cn-word" data-pos="verb" data-tr="u yoqdan-bu yoqqa yurardi">расхаживал</span> между двумя квартирами, будто зная, что именно он <span class="cn-word" data-pos="verb" data-tr="yaqinlashtirdi, birlashtirdi">свёл</span> этих двоих вместе.</p>''',
        "questions": [
            {
                "text": "Что помогло Марине и Игорю по-настоящему познакомиться?",
                "choices": [
                    "Собрание жильцов дома.",
                    "Заблудившийся котёнок, который прибежал к Марине.",
                    "Игорь сам пригласил Марину на чай в первый же день.",
                ],
                "answer": 1,
                "explanation": "Aynan Igorning mushukchasi yomgʻirda adashib Marina eshigiga kelib qolgani ularni haqiqiy tanishuvga olib kelgan.",
            },
            {
                "text": "Как в тексте противопоставлены характеры Марины и Игоря?",
                "choices": [
                    "Марина тихая и задумчивая, а Игорь весёлый и общительный.",
                    "Оба одинаково молчаливы и замкнуты.",
                    "Марина более общительна, чем Игорь.",
                ],
                "answer": 0,
                "explanation": "Matnda toʻgʻridan-toʻgʻri qarshi qoʻyilgan: Marina — jim va xayolchan, Igor — quvnoq va kirishimli, ammo shunga qaramay tez doʻstlashishgan.",
            },
            {
                "text": "Что означает последняя фраза о том, что Рыжик «свёл этих двоих вместе»?",
                "choices": [
                    "Кот в буквальном смысле познакомил их, приведя друг к другу.",
                    "Кот на самом деле не имеет отношения к их дружбе.",
                    "Соседи поссорились из-за кота.",
                ],
                "answer": 0,
                "explanation": "Butun hikoya davomida aynan mushukcha ikki qoʻshnini bir-biriga yaqinlashtirgan sabab boʻlgani koʻrsatiladi — oxirgi jumla shu gʻoyani yakunlaydi.",
            },
        ],
    },
    {
        "title":   "Фотография из детства",
        "summary": "Eski surat bolalik doʻstini ijtimoiy tarmoq orqali qidirib topishga undaydi — unutilmagan doʻstlik haqida.",
        "order":   5,
        "grammar": [
            {
                "pattern":  "После того как",
                "meaning":  "...dan keyin (payt ergash gapini boshlovchi bogʻlovchi, toʻliq harakatdan soʻng).",
                "examples": ["После того как семья переехала, друзья потеряли связь.", "После того как он позвонил, всё изменилось."],
            },
            {
                "pattern":  "мало ли",
                "meaning":  "Kim biladi, qancha/qanaqasi boʻlishi mumkin (noaniqlik yoki eʼtiborsizlikni bildiruvchi ibora).",
                "examples": ["Мало ли сколько людей носят такое же имя.", "Мало ли что может случиться."],
            },
            {
                "pattern":  "действительное причастие (-ащ/-ущ)",
                "meaning":  "Faol sifatdosh — harakatni bajaruvchi predmet/shaxsning holatini tasvirlaydi (fe'ldan yasaladi).",
                "examples": ["Дрожащими от волнения пальцами он написал сообщение.", "Она смотрела на бегущих детей."],
            },
            {
                "pattern":  "Чем ..., тем ...",
                "meaning":  "Qancha ..., shuncha ... (nisbiy qiyoslash konstruksiyasi).",
                "examples": ["Чем дольше они переписывались, тем больше вспоминали.", "Чем позже ложишься, тем труднее вставать."],
            },
        ],
        "body": '''<p>Разбирая старые коробки на антресолях, Дмитрий <span class="cn-word" data-pos="verb" data-tr="duch keldi, koʻzi tushdi">наткнулся</span> на <span class="cn-word" data-pos="adj" data-tr="sargʻaygan">пожелтевшую</span> фотографию, которую не видел уже лет пятнадцать. На снимке — он сам, лет десяти, и его лучший друг детства Серёжа, оба <span class="cn-word" data-pos="adj" data-tr="iflos, changlangan">перепачканные</span> летним загаром, стоят у старого дома с <span class="cn-word" data-tr="qarmoqlar">удочками</span> в руках.</p>
<p>Дмитрий долго смотрел на фотографию, вспоминая, как они с Серёжей проводили каждое лето на реке, ловя рыбу и рассказывая друг другу <span class="cn-word" data-pos="adj" data-tr="oʻylab topilgan, xayoliy">выдуманные</span> истории о сокровищах. <strong>После того как</strong> семья Серёжи переехала в другой город, друзья постепенно потеряли связь, как это часто случается в детстве.</p>
<p>Не откладывая, Дмитрий достал телефон и открыл социальную сеть. Он ввёл в поиске имя друга, не особо <span class="cn-word" data-pos="verb" data-tr="umid qilib">надеясь</span> на успех — <strong>мало ли</strong> сколько людей носят такое же имя. К его удивлению, буквально через минуту он нашёл нужный профиль: Сергей, тот самый город, та же школа на аватарке.</p>
<p><strong>Дрожащими</strong> от волнения пальцами Дмитрий написал сообщение: «Серёга, это ты? Помнишь, как мы ловили рыбу на речке за домом?»</p>
<p>Ответ пришёл не сразу, но, когда пришёл, у Дмитрия перехватило дыхание от радости.</p>
<p>— Дима?! Не могу поверить! Конечно, помню — мы же там чуть не <span class="cn-word" data-pos="verb" data-tr="choʻkib ketishardi">утонули</span>, когда полезли за той <span class="cn-word" data-pos="adj" data-tr="baxtsiz, omadsiz">злополучной</span> удочкой в воду!</p>
<p>Так, спустя пятнадцать лет, друзья детства снова нашли друг друга. Оказалось, что Сергей тоже давно думал о том, чтобы <span class="cn-word" data-pos="verb" data-tr="qidirib topmoq">разыскать</span> старого приятеля, но всё как-то не доходили руки.</p>
<p><strong>Чем</strong> дольше они <span class="cn-word" data-pos="verb" data-tr="yozishib turishdi">переписывались</span>, <strong>тем</strong> больше вспоминали общих моментов, <span class="cn-word" data-pos="adj" data-tr="unutilgan">забытых</span>, казалось бы, навсегда. Через неделю они договорились созвониться по видеосвязи, а через месяц Сергей приехал в гости, и они вместе съездили на ту самую реку, у которой прошло их детство.</p>
<p>Стоя на берегу спустя столько лет, оба понимали: настоящая дружба, даже забытая на время, никогда не <span class="cn-word" data-pos="verb" data-tr="yoʻqolib ketadi">исчезает</span> полностью — она просто ждёт своего часа, чтобы снова напомнить о себе.</p>''',
        "questions": [
            {
                "text": "Как Дмитрий нашёл своего друга детства?",
                "choices": [
                    "Друг сам ему позвонил.",
                    "Через поиск в социальной сети по имени.",
                    "Они случайно встретились на улице.",
                ],
                "answer": 1,
                "explanation": "Dmitriy ijtimoiy tarmoqda doʻstining ismini qidirib, uning profilini topgan — bu tasodifiy koʻcha uchrashuvi emas.",
            },
            {
                "text": "Что именно вспомнили друзья, начав переписываться?",
                "choices": [
                    "Как они вместе ловили рыбу и чуть не утонули из-за удочки.",
                    "Как они учились в разных школах и никогда не встречались.",
                    "Как они однажды поссорились и больше не хотели общаться.",
                ],
                "answer": 0,
                "explanation": "Suhbatda ular baliq ovlashni va qarmoq ortidan suvga tushib, deyarli choʻkib ketishganini eslashadi — bu ularning umumiy bolalik xotirasi.",
            },
            {
                "text": "Какую главную мысль передаёт этот рассказ?",
                "choices": [
                    "Настоящая дружба не исчезает даже после долгой разлуки.",
                    "Социальные сети бесполезны для общения между людьми.",
                    "Детские воспоминания быстро забываются навсегда.",
                ],
                "answer": 0,
                "explanation": "Hikoya oxirida toʻgʻridan-toʻgʻri aytiladi: haqiqiy doʻstlik hatto vaqtinchalik unutilsa ham butunlay yoʻqolmaydi — bu matnning asosiy gʻoyasi.",
            },
        ],
    },
]
