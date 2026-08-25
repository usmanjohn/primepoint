# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-86 … PR-88.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_86_88.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Russian",
    "description": "Rus tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#b91c1c",
}

DEFAULTS = {
    "level":                "hard",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PR-86 — Soʻz yasalishi
# =====================================================================

Q_PR86 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Soʻzning oʻzakdan <strong>oldin</strong> "
                "keladigan qismi qanday ataladi?</p>",
        "choices": ["Су́ффикс", "Оконча́ние", "Приста́вка", "Осно́ва"],
        "correct": "Приста́вка",
        "explanation": "<p><strong>Приста́вка</strong> — oʻzakdan oldingi qism: "
                       "<em>пере</em>писа́ть, <em>под</em>сне́жник. Oʻzbek tilida bunday qism"
                       " umuman yoʻq — shuning uchun rus soʻzining <strong>boshiga</strong> "
                       "alohida eʼtibor berish kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Переписа́ть</strong> soʻzining "
                "oʻzagi qaysi?</p>",
        "choices": ["пис", "пере", "сать", "переп"],
        "correct": "пис",
        "explanation": "<p>Qarindosh soʻzlarni yigʻing: <em>писа́ть, письмо́, писа́тель, "
                       "по́дпись</em> — hammasida <strong>пис</strong> bor. <em>Пере-</em> "
                       "esa приста́вка, «qayta» degani.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bir oʻzakli soʻzlar ruschada qanday "
                "ataladi?</p>",
        "choices": ["Однокоренны́е слова́", "Анто́нимы", "Омо́нимы", "Синони́мы"],
        "correct": "Однокоренны́е слова́",
        "explanation": "<p><strong>Однокоренны́е слова́</strong> — «bir oʻzakli soʻzlar». "
                       "Oʻzakni topishning eng ishonchli yoʻli — shunday soʻzlarni yigʻib, "
                       "takrorlanayotgan qismni olish.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Подсне́жник</strong> soʻzi soʻzma-"
                "soʻz nimani anglatadi?</p>",
        "choices": ["Qor ustidagi", "Qorga oʻxshagan", "Qor tagidagi", "Qorsiz"],
        "correct": "Qor tagidagi",
        "explanation": "<p><strong>под</strong> (tagida) + <strong>снеж</strong> (qor) + "
                       "<strong>ник</strong> (narsa) = «qor tagidan chiquvchi». Bu — "
                       "boychechak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rus soʻzining toʻrtta qismi qaysi tartibda"
                " keladi?</p>",
        "choices": [
            "приста́вка + ко́рень + су́ффикс + оконча́ние",
            "приста́вка + су́ффикс + ко́рень + оконча́ние",
            "оконча́ние + ко́рень + су́ффикс + приста́вка",
            "ко́рень + приста́вка + су́ффикс + оконча́ние",
        ],
        "correct": "приста́вка + ко́рень + су́ффикс + оконча́ние",
        "explanation": "<p>Tartib hech qachon buzilmaydi: <strong>приста́вка + ко́рень + "
                       "су́ффикс + оконча́ние</strong>. Masalan <em>пере-пи́с-ыва-"
                       "ть</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri yozilgan variantni tanlang.</p><p><strong>без + "
                "поле́зный</strong></p>",
        "choices": ["безполе́зный", "бесполе́зный", "безпале́зный", "бэсполе́зный"],
        "correct": "бесполе́зный",
        "explanation": "<p><strong>Без-</strong> jarangsiz undosh oldida "
                       "<strong>бес-</strong> boʻladi. <em>П</em> — jarangsiz, demak "
                       "<strong>бесполе́зный</strong>. Bu — PR-4 dagi "
                       "<strong>оглуше́ние</strong> ning yozuvdagi koʻrinishi.</p>",
    },
    {
        "text": "<p>Toʻgʻri yozilgan variantni tanlang.</p><p><strong>без + "
                "рабо́тный</strong></p>",
        "choices": ["бесрабо́тный", "безрабо́тный", "бэзрабо́тный", "бесработный"],
        "correct": "безрабо́тный",
        "explanation": "<p><em>Р</em> — <strong>jarangli</strong> undosh, shuning uchun "
                       "<strong>з</strong> saqlanadi: <strong>безрабо́тный</strong> (ishsiz)."
                       " Qoida faqat jarangsiz undoshlar oldida ishlaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu soʻzlarning umumiy oʻzagi "
                "qaysi?</p><p><strong>учи́тель · учени́к · уче́бник · изуча́ть</strong></p>",
        "choices": ["-ник-", "-уче-", "-учи-", "-уч-"],
        "correct": "-уч-",
        "explanation": "<p>Toʻrttasida ham takrorlanayotgan eng qisqa qism — "
                       "<strong>-уч-</strong>. Qolgani suffiks va приста́вка: "
                       "<em>уч-и́-тель</em>, <em>уч-ени́к</em>, <em>из-уч-а́-ть</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Пишу́</strong> va "
                "<strong>писа́ть</strong> — oʻzaklari bir xilmi?</p>",
        "choices": [
            "Yoʻq, ikki xil oʻzak: пиш va пис",
            "Ha, bitta oʻzak; с/ш — чередова́ние",
            "Yoʻq, birinchisining oʻzagi yoʻq",
            "Ha, chunki ikkalasi ham feʼl",
        ],
        "correct": "Ha, bitta oʻzak; с/ш — чередова́ние",
        "explanation": "<p>Oʻzak bitta — <strong>-пис-</strong>. <strong>с/ш</strong> "
                       "almashinuvi <strong>чередова́ние</strong> deb ataladi va PR-22 da "
                       "tuslanishda uchragan edi: <em>писа́ть → пишу́</em>, <em>ходи́ть → "
                       "хожу́</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>Bu soʻzda «qochoq unli» bor: <strong>день"
                " → ___</strong> (Р.п.)</p>",
        "choices": ["де́ня", "дня", "де́ни", "дени́"],
        "correct": "дня",
        "explanation": "<p><strong>Дня</strong> — <em>е</em> tushib qoladi. Bu "
                       "<strong>бе́глая гла́сная</strong>. Oʻzbekchada ham shunday: <em>ogʻiz"
                       " → ogʻzim</em>, <em>burun → burni</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Парохо́д</strong> soʻzida "
                "<strong>о</strong> nima uchun turibdi?</p>",
        "choices": [
            "Bu су́ффикс",
            "Bu приста́вка",
            "Bu оконча́ние",
            "Bu ikki oʻzakni bogʻlovchi unli",
        ],
        "correct": "Bu ikki oʻzakni bogʻlovchi unli",
        "explanation": "<p><em>пар</em> + <strong>о</strong> + <em>ход</em> — ruschada ikkita"
                       " oʻzak qoʻshilganda oʻrtaga <strong>о</strong> yoki "
                       "<strong>е</strong> qoʻyiladi: <em>пеш<strong>е</strong>хо́д</em>, "
                       "<em>сам<strong>о</strong>лёт</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Siz bu soʻzni koʻrmagansiz: "
                "<strong>снегохо́д</strong>. Maʼnosi nima?</p>",
        "choices": [
            "Qor tozalovchi belkurak",
            "Qorda yuradigan mashina",
            "Qor yogʻishi",
            "Qorli togʻ",
        ],
        "correct": "Qorda yuradigan mashina",
        "explanation": "<p><em>снег</em> (qor) + <strong>о</strong> + <em>ход</em> (yurish) ="
                       " <strong>snegoxod</strong>. Xuddi <em>парохо́д</em> va "
                       "<em>вездехо́д</em> kabi qurilgan — lugʻat kerak boʻlmadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Учи́тель</strong> va "
                "<strong>учи́теля</strong> — bu nechta soʻz?</p>",
        "choices": [
            "Bitta soʻz, ikki oʻzak",
            "Ikki soʻz, chunki suffikslari boshqa",
            "Bitta soʻz, ikki shakl — farq оконча́ние da",
            "Ikki soʻz, chunki maʼnolari boshqa",
        ],
        "correct": "Bitta soʻz, ikki shakl — farq оконча́ние da",
        "explanation": "<p><strong>Оконча́ние</strong> yangi soʻz yasamaydi, faqat grammatik "
                       "shaklni oʻzgartiradi — bu yerda Р.п. Lugʻatda bitta maqola. "
                       "<em>Учи́ть → учи́тель</em> esa <strong>suffiks</strong> orqali ikki "
                       "xil soʻz.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi juftlikda <strong>yangi "
                "soʻz</strong> yasalgan?</p>",
        "choices": [
            "дом — до́ма",
            "перехо́д — перехо́да",
            "учи́тель — учи́телю",
            "перехо́д — перехо́дный",
        ],
        "correct": "перехо́д — перехо́дный",
        "explanation": "<p><em>Перехо́дный</em> da <strong>-н-</strong> suffiksi qoʻshilgan —"
                       " ot sifatga aylandi, demak <strong>yangi soʻz</strong>. Qolgan "
                       "uchtasida faqat оконча́ние oʻzgargan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi ikki soʻz <strong>qarindosh "
                "emas</strong>?</p>",
        "choices": [
            "вода́ — води́ть",
            "писа́ть — письмо́",
            "ходи́ть — вы́ход",
            "учи́ть — учени́к",
        ],
        "correct": "вода́ — води́ть",
        "explanation": "<p>Ular faqat <strong>shaklan</strong> oʻxshaydi: <em>вода́</em> ning"
                       " oʻzagi «suv», <em>води́ть</em> niki «yetaklamoq». Oʻzakni topishda "
                       "shaklga emas, <strong>maʼnoga ham</strong> qarash kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Дом</strong> soʻzining оконча́ние "
                "si qanday?</p>",
        "choices": ["Uning окончание si yoʻq", "-ом", "Boʻsh (nol)", "-м"],
        "correct": "Boʻsh (nol)",
        "explanation": "<p>И.п. da оконча́ние <strong>boʻsh</strong>, lekin u mavjud: "
                       "kelishik oʻzgarishi bilan darrov paydo boʻladi — "
                       "<em>до́м<strong>а</strong>, до́м<strong>у</strong>, "
                       "до́м<strong>ом</strong></em>.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "Он рассказа́л всю исто́рию.",
            "Э́то бесполе́зный разгово́р.",
            "Он безрабо́тный уже́ год.",
            "Она́ безпла́тно помога́ет сосе́дям.",
        ],
        "correct": "Она́ безпла́тно помога́ет сосе́дям.",
        "explanation": "<p>Toʻgʻrisi — <strong>беспла́тно</strong>. <em>П</em> jarangsiz, "
                       "demak <em>без-</em> → <strong>бес-</strong>. Qolgan uch gap toʻgʻri: "
                       "<em>бесполе́зный</em> (бес-), <em>безрабо́тный</em> (jarangli р), "
                       "<em>рассказа́л</em> (рас- + с).</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "Oʻzbek tilida ham приста́вка bor.",
            "«Пишу́» va «писа́ть» — turli oʻzakli soʻzlar.",
            "«Учи́тель» va «учи́теля» — turli soʻzlar.",
            "«Су́ффикс» yangi soʻz yasaydi, «оконча́ние» esa faqat shaklni.",
        ],
        "correct": "«Су́ффикс» yangi soʻz yasaydi, «оконча́ние» esa faqat shaklni.",
        "explanation": "<p>Bu — darsning asosiy farqi. Birinchisi xato (чередова́ние), "
                       "ikkinchisi xato (bitta soʻzning ikki shakli), toʻrtinchisi xato — "
                       "oʻzbekchada prefiks yoʻq, hamma qoʻshimcha oʻzakdan "
                       "<strong>keyin</strong> keladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>ish + chi + lar + imiz +"
                " ga</strong> qurilishiga rus tilidagi qaysi soʻz eng yaqin?</p>",
        "choices": ["пис-а́-тел-ям", "пере-пис-а́-ть", "под-снеж-ник", "дом"],
        "correct": "пис-а́-тел-ям",
        "explanation": "<p><em>Писа́телям</em> = oʻzak <strong>пис</strong> + suffiks "
                       "<strong>-тел-</strong> (odam, «-chi») + оконча́ние "
                       "<strong>-ям</strong> (Д.п. koʻplik, «-larga»). Ikkala tilda ham "
                       "gʻishtlar bir xil tartibda — chunki prefiks bu yerda yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki oʻzakdan bitta soʻz yasang: "
                "<strong>вод(а)</strong> + <strong>па́д(ать)</strong></p>",
        "choices": ["водъпа́д", "водапа́д", "водопа́д", "водепа́д"],
        "correct": "водопа́д",
        "explanation": "<p><strong>Водопа́д</strong> — «suv tushadigan joy», yaʼni sharshara."
                       " Bogʻlovchi unli — <strong>о</strong>. Yozuvda aynan <em>о</em> "
                       "turadi, garchi u urgʻusiz boʻlgani uchun [а] boʻlib eshitilsa ham "
                       "(<strong>аканье</strong>).</p>",
    },
]


# =====================================================================
# PR-87 — Suffikslar xaritasi
# =====================================================================

Q_PR87 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>-ость</strong> ga tugagan otlar "
                "qaysi jinsda boʻladi?</p>",
        "choices": ["Же́нский", "Сре́дний", "Soʻzga qarab turlicha", "Мужско́й"],
        "correct": "Же́нский",
        "explanation": "<p><strong>-ость</strong> — istisnosiz <strong>же́нский род</strong>,"
                       " va <em>дверь</em> kabi uchinchi turlanishga kiradi: <em>но́вость → "
                       "но́вости</em>. Bu qoidada bitta ham istisno yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>-ение</strong> ga tugagan otlar "
                "qaysi jinsda?</p>",
        "choices": ["Сре́дний", "Же́нский", "Мужско́й", "Faqat koʻplikda ishlatiladi"],
        "correct": "Сре́дний",
        "explanation": "<p><em>реше́ние, зна́ние, движе́ние</em> — hammasi <strong>сре́дний "
                       "род</strong>. Shuning uchun <em>пра́вильн<strong>ое</strong> "
                       "реше́ние</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Учи́ть</strong> feʼlidan kasb "
                "yasang.</p>",
        "choices": ["учени́к", "уче́бник", "учи́тель", "уче́ние"],
        "correct": "учи́тель",
        "explanation": "<p><strong>-тель</strong> odam yasaydi: <em>учи́тель</em> "
                       "(oʻqituvchi). <em>Учени́к</em> ham odam, lekin u "
                       "<strong>oʻrganuvchi</strong>; <em>уче́бник</em> — narsa "
                       "(darslik).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«-lik»</strong> "
                "qoʻshimchasiga rus tilida nima mos keladi?</p>",
        "choices": ["-тель", "-ость va -ство", "-ение", "-щик"],
        "correct": "-ость va -ство",
        "explanation": "<p><em>yangi<strong>lik</strong></em> → "
                       "<em>но́в<strong>ость</strong></em>, <em>boy<strong>lik</strong></em> "
                       "→ <em>бога́т<strong>ство</strong></em>. Oʻzbekchadagi bitta "
                       "qoʻshimcha ruschada ikkiga boʻlingan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi suffiks <strong>odam</strong> "
                "yasamaydi?</p>",
        "choices": ["-тель", "-щик", "-ник", "-ость"],
        "correct": "-ость",
        "explanation": "<p><strong>-ость</strong> sifatdan <strong>mavhum xususiyat</strong> "
                       "yasaydi: <em>сме́лость</em>, <em>че́стность</em>. Qolgan uchtasi odam"
                       " yasaydi va oʻzbekcha «-chi» ga toʻgʻri keladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У меня́ ___ но́вость!</strong></p>",
        "choices": ["хоро́ший", "хоро́шее", "хоро́шая", "хоро́шие"],
        "correct": "хоро́шая",
        "explanation": "<p><em>Но́вость</em> — <strong>же́нский род</strong>, chunki "
                       "<strong>-ость</strong>. Yumshoq belgiga aldanmang: <s>хоро́ший "
                       "но́вость</s> — koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri yozilgan variantni tanlang.</p><p>«Tarjimon» kasbi:</p>",
        "choices": ["перево́дщик", "перево́дчик", "перево́дник", "перево́дтель"],
        "correct": "перево́дчик",
        "explanation": "<p>Oʻzak <em>перевод</em> — <strong>д</strong> bilan tugagan, demak "
                       "<strong>-чик</strong>. Qoida: <strong>д · т · з · с · ж</strong> dan "
                       "keyin -чик, boshqa hollarda -щик (<em>ка́менщик, сва́рщик</em>).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то бы́л___ пра́вильн___ "
                "реше́ние.</strong></p>",
        "choices": [
            "был / пра́вильный",
            "была́ / пра́вильная",
            "бы́ло / пра́вильное",
            "бы́ли / пра́вильные",
        ],
        "correct": "бы́ло / пра́вильное",
        "explanation": "<p><em>Реше́ние</em> — <strong>сре́дний род</strong> "
                       "(<strong>-ение</strong>), shuning uchun feʼl ham, sifat ham oʻrta "
                       "jinsga moslashadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Возмо́жный</strong> sifatidan ot "
                "yasang.</p>",
        "choices": ["возможе́ние", "возмо́жство", "возмо́жник", "возмо́жность"],
        "correct": "возмо́жность",
        "explanation": "<p><strong>Возмо́жность</strong> — imkoniyat. Sifatdan mavhum ot "
                       "<strong>-ость</strong> bilan yasaladi, va natija har doim "
                       "<strong>же́нский род</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Реши́ть</strong> feʼlidan ot "
                "yasang.</p>",
        "choices": ["реши́тель", "реше́ние", "реши́мость", "реша́ние"],
        "correct": "реше́ние",
        "explanation": "<p><strong>Реше́ние</strong> — qaror, yechim. Feʼldan harakat oti "
                       "<strong>-ение</strong> bilan yasaladi va oʻzbekcha "
                       "<strong>«-(i)sh»</strong> ga toʻgʻri keladi: <em>yechish</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Учи́тельница</strong> qaysi "
                "suffiks yordamida yasalgan?</p>",
        "choices": ["-ка", "-ница", "-щица", "-ость"],
        "correct": "-ница",
        "explanation": "<p><em>учи́тель</em> + <strong>-ница</strong> = "
                       "<em>учи́тельница</em>. <s>Учи́телька</s> — xato. Boshqa misollar: "
                       "<em>писа́тельница, перево́дчица</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Siz bu soʻzni koʻrmagansiz: "
                "<strong>гото́вность</strong>. Maʼnosi va jinsi?</p>",
        "choices": [
            "tayyorlik — же́нский",
            "tayyorlamoq — feʼl",
            "tayyorlovchi — мужско́й",
            "tayyorlash — сре́дний",
        ],
        "correct": "tayyorlik — же́нский",
        "explanation": "<p>Oʻzak <em>гото́в-</em> («tayyor», PR-73 dagi qisqa sifat) + "
                       "<strong>-ость</strong> = <strong>tayyorlik</strong>, <strong>же́нский"
                       " род</strong>. Suffiks ikkala javobni ham birdan berdi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi soʻz <strong>сре́дний род</strong> "
                "da emas?</p>",
        "choices": ["ка́чество", "зна́ние", "бога́тство", "ско́рость"],
        "correct": "ско́рость",
        "explanation": "<p><em>Ско́рость</em> — <strong>-ость</strong>, demak "
                       "<strong>же́нский</strong>. Qolgan uchtasi <em>-ение</em> va "
                       "<em>-ство</em> bilan tugagan — ikkalasi ham "
                       "<strong>сре́дний</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>-тель</strong> va "
                "<strong>-щик</strong> orasidagi farq nimada?</p>",
        "choices": [
            "-тель ayol, -щик erkak",
            "-тель koʻproq kitobiy kasblarda, -щик koʻproq qoʻl mehnatida",
            "-тель feʼldan, -щик sifatdan yasaladi",
            "Ular butunlay bir xil",
        ],
        "correct": "-тель koʻproq kitobiy kasblarda, -щик koʻproq qoʻl mehnatida",
        "explanation": "<p><em>учи́тель, писа́тель, води́тель</em> ↔ <em>ка́менщик, сва́рщик,"
                       " убо́рщик</em>. Ikkalasi ham <strong>мужско́й род</strong> va "
                       "ikkalasi ham oʻzbekcha «-chi». Qaysi soʻzga qaysisi kelishi "
                       "yodlanadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu ikki soʻzning farqi "
                "nimada?</p><p><strong>сме́лость</strong> — <strong>бога́тство</strong></p>",
        "choices": [
            "Birinchisi sifatdan xususiyat, ikkinchisi holat; jinslari ham har xil",
            "Ikkalasi ham же́нский род",
            "Ikkalasi ham feʼldan yasalgan",
            "Farqi yoʻq, ikkalasi sinonim",
        ],
        "correct": "Birinchisi sifatdan xususiyat, ikkinchisi holat; jinslari ham har xil",
        "explanation": "<p><em>Сме́лость</em> (jasorat) — <strong>-ость</strong>, "
                       "<strong>ж.р.</strong>; <em>бога́тство</em> (boylik) — "
                       "<strong>-ство</strong>, <strong>ср.р.</strong> Oʻzbekchada ikkalasi "
                       "ham «-lik» boʻlardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Уче́бник</strong> — bu kim yoki "
                "nima?</p>",
        "choices": ["Oʻqish jarayoni", "Oʻqituvchi", "Oʻquvchi", "Darslik"],
        "correct": "Darslik",
        "explanation": "<p><strong>-ник</strong> odam ham, <strong>narsa</strong> ham yasashi"
                       " mumkin. <em>Уче́бник</em> — narsa (darslik), <em>учени́к</em> — odam"
                       " (oʻquvchi), <em>учи́тель</em> — oʻqituvchi.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "На́ша учи́тельница — Мари́на Петро́вна.",
            "Э́то была́ хоро́шая но́вость.",
            "Реше́ние бы́ло непра́вильным.",
            "Он рабо́тает перево́дщиком в банке.",
        ],
        "correct": "Он рабо́тает перево́дщиком в банке.",
        "explanation": "<p>Toʻgʻrisi — <strong>перево́дчиком</strong>. Oʻzak <em>д</em> bilan"
                       " tugagan, demak <strong>-чик</strong>. Talaffuzda farq deyarli "
                       "sezilmaydi, lekin yozuvda muhim.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "Реше́ние был тру́дный.",
            "Ско́рость был о́чень большо́й.",
            "У неё больша́я ско́рость печа́ти.",
            "Э́то ва́жный но́вость.",
        ],
        "correct": "У неё больша́я ско́рость печа́ти.",
        "explanation": "<p><em>Ско́рость</em> va <em>но́вость</em> — <strong>же́нский "
                       "род</strong>, <em>реше́ние</em> — <strong>сре́дний</strong>. Faqat "
                       "ikkinchi gapda moslashuv toʻgʻri bajarilgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bir oʻzakdan oila yasang: "
                "<strong>-строй-</strong> → odam · jarayon · narsa</p>",
        "choices": [
            "строи́тель · строи́тельство · стро́йка",
            "строи́тельство · стро́йка · строи́тель",
            "стро́йка · строи́тель · строи́тельство",
            "строи́тель · стро́йка · строи́тельство",
        ],
        "correct": "строи́тель · строи́тельство · стро́йка",
        "explanation": "<p><strong>Строи́тель</strong> — odam (<em>-тель</em>), "
                       "<strong>строи́тельство</strong> — jarayon (<em>-ство</em>), "
                       "<strong>стро́йка</strong> — joy yoki narsa (<em>-ка</em>). Bitta "
                       "oʻzak, uch suffiks, uch soʻz.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Кем рабо́тает твой "
                "брат?</strong></p><p><strong>— ___</strong></p>",
        "choices": [
            "Он рабо́тает строи́тель.",
            "Он рабо́тает строи́тельство.",
            "Он рабо́тает строи́телем.",
            "Он рабо́тает стро́йкой.",
        ],
        "correct": "Он рабо́тает строи́телем.",
        "explanation": "<p>Kasb haqida gapirganda <strong>Твори́тельный паде́ж</strong> kerak"
                       " (PR-40): <em>рабо́тать <strong>строи́телем</strong></em>. "
                       "<em>Строи́тельство</em> — jarayon, odam emas.</p>",
    },
]


# =====================================================================
# PR-88 — Kichraytiruvchi va erkalash shakllari
# =====================================================================

Q_PR88 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Дом → до́мик</strong> — qanday "
                "suffiks qoʻshildi?</p>",
        "choices": [
            "Kichraytiruvchi",
            "Kasb yasovchi",
            "Kattalashtiruvchi",
            "Mavhum ot yasovchi",
        ],
        "correct": "Kichraytiruvchi",
        "explanation": "<p><strong>-ик</strong> — kichraytiruvchi suffiks: <em>до́мик</em> "
                       "(kichik uy), <em>но́сик</em>, <em>клю́чик</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ма́мочка</strong> nimani "
                "anglatadi?</p>",
        "choices": ["Onajon — mehr bilan murojaat", "Yosh ona", "Oʻgay ona", "Kichkina ona"],
        "correct": "Onajon — mehr bilan murojaat",
        "explanation": "<p>Bu yerda suffiks <strong>kichraytirmaydi</strong>, "
                       "<strong>erkalaydi</strong>. Oʻzbekchada bu ikki maʼno ikki xil "
                       "qoʻshimchada: <em>-cha</em> kichraytiradi, <em>-jon</em> erkalaydi. "
                       "Ruschada esa bitta shakl.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ма́ша</strong> qaysi ismning qisqa"
                " shakli?</p>",
        "choices": ["Мари́я", "Ма́йя", "Мари́анна", "Мари́на"],
        "correct": "Мари́я",
        "explanation": "<p><strong>Мари́я → Ма́ша → Ма́шенька</strong> — uch pogʻona: rasmiy,"
                       " kundalik, mehrli. <em>Мари́на</em> esa boshqa ism va uning qisqa "
                       "shakli <em>Мари́нка</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi suffiks otni "
                "<strong>kattalashtiradi</strong>?</p>",
        "choices": ["-ик", "-очка", "-ище", "-ушка"],
        "correct": "-ище",
        "explanation": "<p><strong>-ище</strong>: <em>дом → доми́ще</em> (ulkan uy), "
                       "<em>рука́ → ручи́ща</em>, <em>глаза́ → глази́щи</em>. Qolgan uchtasi "
                       "kichraytiradi yoki erkalaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Со́лнце</strong> ning erkalash "
                "shakli qaysi?</p>",
        "choices": ["со́лнышко", "со́лнчик", "со́лнька", "солнцо́к"],
        "correct": "со́лнышко",
        "explanation": "<p><strong>Со́лнышко</strong> (<em>-ышко</em>). Odamga aytilganda "
                       "juda iliq murojaat: <em>Со́лнышко моё!</em> — «quyoshginam».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>Muloyim soʻrash: <strong>Подожди́те одну́"
                " ___, пожа́луйста.</strong></p>",
        "choices": ["мину́ту", "мину́точку", "мину́тище", "мину́тка"],
        "correct": "мину́точку",
        "explanation": "<p><strong>Мину́точку</strong> — «bir daqiqagina». <em>Мину́ту</em> "
                       "ham toʻgʻri, lekin quruqroq eshitiladi. Kichraytirish bu yerda "
                       "<strong>muloyimlik</strong> vositasi. Xuddi shunday: "
                       "<em>секу́ндочку</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Buvi ellik yoshli oʻgʻliga "
                "<strong>«Сыно́к»</strong> deydi. Bu nimani bildiradi?</p>",
        "choices": [
            "Oʻgʻli juda kichkina",
            "Bu iliq murojaat — yosh ahamiyatsiz",
            "Buvi xato qilyapti",
            "Bu qoʻpol murojaat",
        ],
        "correct": "Bu iliq murojaat — yosh ahamiyatsiz",
        "explanation": "<p><strong>Сыно́к</strong> — «oʻgʻlim», xuddi oʻzbekcha «bolam» kabi."
                       " Oʻlchamga ham, yoshga ham aloqasi yoʻq — bu "
                       "<strong>munosabat</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega <strong>кни́га → кни́жка</strong> da "
                "<strong>ж</strong> paydo boʻldi?</p>",
        "choices": ["Bu yozuv xatosi", "Чередова́ние г/ж", "Bu boshqa oʻzak", "Оглуше́ние"],
        "correct": "Чередова́ние г/ж",
        "explanation": "<p>PR-86 dagi qoida: suffiks oldida oʻzakning oxirgi undoshi "
                       "almashadi. <em>кни́га → кни́жка</em> (г/ж), <em>нога́ → но́жка</em> "
                       "(г/ж), <em>рука́ → ру́чка</em> (к/ч).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ру́чка</strong> bugungi rus tilida"
                " koʻpincha nimani anglatadi?</p>",
        "choices": ["Kichik qoʻl", "Ruchka yoki eshik dastasi", "Bolaning qoʻli", "Qoʻlqop"],
        "correct": "Ruchka yoki eshik dastasi",
        "explanation": "<p>Baʼzi kichraytirilgan shakllar <strong>mustaqil soʻzga</strong> "
                       "aylangan: <em>ру́чка</em> (ruchka, dasta), <em>ба́бушка</em> (buvi), "
                       "<em>де́вочка</em> (qizcha). Ular endi kichraytirilgan "
                       "hisoblanmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Са́ша</strong> — qaysi "
                "ism(lar)ning qisqa shakli?</p>",
        "choices": [
            "Faqat Алекса́ндр",
            "Faqat Алекса́ндра",
            "Алекса́ндр va Алекса́ндра — ikkalasi ham",
            "Серге́й",
        ],
        "correct": "Алекса́ндр va Алекса́ндра — ikkalasi ham",
        "explanation": "<p>Shuning uchun <em>Са́ша пришёл</em> va <em>Са́ша пришла́</em> — "
                       "ikkalasi ham toʻgʻri; jinsni <strong>feʼl</strong> koʻrsatadi. Xuddi "
                       "shunday: <em>Же́ня</em> (Евге́ний / Евге́ния).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Городи́шко</strong> qanday ohangda"
                " aytilgan?</p>",
        "choices": [
            "Iliq va mehrli",
            "Salbiy — kichik va ahamiyatsiz",
            "Hayratlanish bilan",
            "Rasmiy",
        ],
        "correct": "Salbiy — kichik va ahamiyatsiz",
        "explanation": "<p><strong>-ишко</strong> kamsitadi: <em>доми́шко</em> (xarob uycha),"
                       " <em>городи́шко</em> (arzimas shaharcha). <strong>-ище</strong> esa "
                       "kattalashtiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Хлеб → ___</strong> — erkalash "
                "shakli qaysi?</p>",
        "choices": ["хлебо́к", "хле́бик", "хле́бушек", "хле́бочка"],
        "correct": "хле́бушек",
        "explanation": "<p><strong>Хле́бушек</strong> (<em>-ушек / -ушка</em>). Bu shakl "
                       "nonni kichraytirmaydi — unga <strong>hurmat va mehr</strong> "
                       "qoʻshadi. Rus madaniyatida non haqida shunday gapiriladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi juftlikda haqiqatan ham "
                "<strong>oʻlcham</strong> haqida gap ketyapti?</p>",
        "choices": ["со́лнце → со́лнышко", "ма́ма → ма́мочка", "сын → сыно́к", "дом → до́мик"],
        "correct": "дом → до́мик",
        "explanation": "<p><strong>До́мик</strong> — chindan ham kichik uy. Qolgan uchtasida "
                       "shakl kichraytiruvchi, lekin maʼno — <strong>mehr</strong>: onajon, "
                       "oʻgʻlim, quyoshginam.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«onajon»</strong> "
                "ruschada qanday beriladi?</p>",
        "choices": ["ма́мка", "ма́ленькая ма́ма", "ма́мочка", "ма́мище"],
        "correct": "ма́мочка",
        "explanation": "<p>Oʻzbekcha <strong>-jon</strong> ruschada <strong>-очка / "
                       "-енька</strong> ga toʻgʻri keladi. <em>Ма́мка</em> esa qoʻpol "
                       "eshitiladi — <em>-ка</em> shu xavfni tugʻdiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Notanish katta yoshli ayolga qanday "
                "murojaat qilasiz?</p>",
        "choices": ["Маш", "Ма́шка", "Ма́шенька", "Мари́я Петро́вна"],
        "correct": "Мари́я Петро́вна",
        "explanation": "<p>Rasmiy holatda — <strong>ism + otasining ismi</strong>. "
                       "<em>Ма́шка</em> qoʻpol, <em>Ма́шенька</em> juda yaqin — ikkalasi ham "
                       "notanish odamga toʻgʻri kelmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu shakllar qayerda "
                "<strong>ishlatilmaydi</strong>?</p>",
        "choices": [
            "Bolalar kitobida",
            "Oila davrasida",
            "Doʻstlar bilan suhbatda",
            "Arizada va rasmiy xatda",
        ],
        "correct": "Arizada va rasmiy xatda",
        "explanation": "<p>Kichraytirish — <strong>ogʻzaki va oilaviy</strong> nutqning "
                       "belgisi. <s>Прошу́ дать о́тпуск на неде́льку</s> → <strong>на "
                       "неде́лю</strong>. Rasmiy matn, imtihon javobi, yangilik xabari — hech"
                       " qachon.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "Дилно́за, чайку́?",
            "Ма́мочка, я уже́ до́ма!",
            "Прошу́ предоста́вить о́тпуск на неде́льку.",
            "Подожди́те секу́ндочку, пожа́луйста.",
        ],
        "correct": "Прошу́ предоста́вить о́тпуск на неде́льку.",
        "explanation": "<p>Bu — <strong>ariza</strong>, ya'ni rasmiy matn. Toʻgʻrisi: "
                       "<strong>на неде́лю</strong>. Qolgan uch gap kundalik nutq va ularda "
                       "kichraytirish tabiiy.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "«Ма́шка» — eng hurmatli shakl.",
            "«До́мик» va «ма́мочка» — ikkalasi ham oʻlcham haqida.",
            "«Сыно́к» faqat kichik bolaga aytiladi.",
            "«-Ище» kattalashtiradi, «-ишко» esa kamsitadi.",
        ],
        "correct": "«-Ище» kattalashtiradi, «-ишко» esa kamsitadi.",
        "explanation": "<p><em>Доми́ще</em> — ulkan uy, <em>доми́шко</em> — xarob uycha. "
                       "Qolgan uchta gap xato: <em>ма́мочка</em> oʻlcham emas, "
                       "<em>сыно́к</em> yoshdan qatʼi nazar aytiladi, <em>Ма́шка</em> esa eng"
                       " familyar shakl.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Афсо́на, ты уже́ "
                "гото́ва?</strong></p><p><strong>— ___</strong></p>",
        "choices": [
            "Одну́ мину́точку, я сейча́с!",
            "Одну́ мину́тище, я сейча́с!",
            "Одну́ мину́тишко, я сейча́с!",
            "Одну́ мину́тник, я сейча́с!",
        ],
        "correct": "Одну́ мину́точку, я сейча́с!",
        "explanation": "<p><strong>Мину́точку</strong> — kundalik nutqning eng koʻp "
                       "ishlatiladigan iboralaridan biri. Qolgan uchta variant mavjud emas: "
                       "<em>-ище</em> va <em>-ишко</em> vaqt soʻzlariga qoʻshilmaydi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Mashenka, choy "
                "ichasizmi?</strong></p>",
        "choices": ["Ма́ша, чаи́ще?", "Ма́шенька, чаёк?", "Ма́шка, чай?", "Ма́шенька, чайку́?"],
        "correct": "Ма́шенька, чайку́?",
        "explanation": "<p><strong>Чайку́</strong> — <em>чаёк</em> ning Роди́тельный shakli, "
                       "taklifda aynan shu ishlatiladi (<em>Чайку́? Ко́фейку?</em>). "
                       "<em>Ма́шенька</em> — iliq murojaat, <em>Ма́шка</em> esa bu ohangga "
                       "toʻgʻri kelmaydi.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-86 Mashq: Soʻz yasalishi",
        "description": (
            "Приста́вка + ко́рень + су́ффикс + оконча́ние. Oʻzakni topish, "
            "без-/бес- qoidasi, чередова́ние va notanish soʻzni taxmin qilish."
        ),
        "tutorial": "PR-86:",
        "questions": Q_PR86,
    },
    {
        "title": "PR-87 Mashq: Suffikslar xaritasi",
        "description": (
            "Suffiks maʼnoni ham, jinsni ham aytadi: -тель м.р., -ость ж.р., "
            "-ение va -ство ср.р. -чик/-щик tanlash qoidasi bilan."
        ),
        "tutorial": "PR-87:",
        "questions": Q_PR87,
    },
    {
        "title": "PR-88 Mashq: Kichraytiruvchi va erkalash shakllari",
        "description": (
            "До́мик kichik uy, ma'mochka esa kichik ona emas. Ismlarning uch "
            "pogʻonasi, -ище/-ишко va «Одну́ мину́точку!» muloyimligi."
        ),
        "tutorial": "PR-88:",
        "questions": Q_PR88,
    },
]
