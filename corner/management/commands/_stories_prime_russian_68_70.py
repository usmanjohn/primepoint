# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-68 … PR-70.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 68 — sirli hikoya, 69 — hayot hikoyasi (haqiqiy odam),
70 — ilmiy-ommabop. (65 kundalik daftar, 66 ilmiy-ommabop, 67 intervyu edi —
uchta bir xil shakl ketma-ket kelmayapti.)

Grammatika chegarasi (kumulyativ qoida):
  68-matn: ли. Bilvosita savol beshta joyda («не знал, придёт ли», «спроси́л,
           зна́ют ли», «не по́мнил, ско́лько» — savol soʻzli variant ham
           qarshi qoʻyilgan) va oxirida «вряд ли».
  69-matn: тот, кто / то, что. Beshta shaklda: тот кто, то что, все кто,
           о том что, де́ло в том что.
  70-matn: действительные причастия — живу́щие, стоя́щие, рабо́тающие,
           иду́щие, вы́росший, изуча́ющие. Otdan keyin turganda vergul bilan.

⚠️ ATAY QOCHILGAN (keyingi darslar): страдательные причастия (PR-71),
деепричастие (PR-72), qisqa sifat — рад, готов, прав (PR-73), SIFAT
DARAJALARI — са́мый / бо́льше / лу́чше / глу́бже (PR-74), свой (PR-75),
себя́ (PR-76), кто́-то / кто́-нибудь (PR-78).
Yagona istisno — 68-matndagi sarlavha va matndagi «никто́ не знал»:
ikki inkor PR-79 da oʻrgatiladi, lekin bu ibora tocda oʻsha nom bilan
rejalashtirilgan va oldingi matnlarda ham lugʻat sifatida uchragan.
cn-word izohi berilgan.

⚠️ FAKTLAR:
  69-matn — HAQIQIY ODAM: Жадав Пайенг (Jadav Payeng), Hindiston, Assam,
  Majuli oroli. 1979 da toshqindan keyin qumli orolda yalangʻoch yer qolgan;
  u yolgʻiz bambuk va daraxt ekishni boshlagan; qirq yildan keyin ~550
  gektar oʻrmon paydo boʻlgan, unga «Молаи» laqabidan «Молаи» oʻrmoni deb
  nom berilgan; u yerga fillar, karkidonlar va yoʻlbarslar keladi;
  2015-yilda «Падма Шри» davlat mukofotini olgan.
  70-matn — Norilsk qutb tuni ~45 kun; abadiy muzloq (ве́чная мерзлота́)
  ustidagi uylar «сваи» — ustunlar ustiga quriladi, aks holda uyning issigʻi
  yerni eritadi; nenetslar — kiyik boquvchi koʻchmanchilar, chumda yashaydi;
  Yakutskda qishda -50 gradusgacha sovuq boʻladi.
  68-matn — toʻqima voqea, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_68_70.py --author=prime
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
    # PR-68 — ли                                       SIRLI HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Никто́ не знал, придёт ли он",
        "summary": (
            "PR-68 matni. Har yili 1-sentabrda kichik qishloq maktabiga "
            "kitob toʻla posilka keladi, lekin joʻnatuvchisi yozilmagan. "
            "Qorovul Nikolay Ivanovich sirni ochadi — va sir ochilgach, "
            "savolning oʻzi keraksiz boʻlib qoladi."
        ),
        "order":   68,
        "grammar": [
            {
                "pattern":  "Bilvosita savol: ли",
                "meaning":  "Savolni boshqa gap ichiga solganda ли majburiy. U "
                            "soʻralayotgan soʻzdan keyin turadi — oʻzbekcha "
                            "«-mi» kabi.",
                "examples": ["Никто́ не знал, придёт ли посы́лка.",
                             "Он спроси́л, зна́ют ли на по́чте отправи́теля."],
            },
            {
                "pattern":  "Savol soʻzi bor boʻlsa — ли yoʻq",
                "meaning":  "«Кто присыла́ет», «отку́да прихо́дит» — bu gaplarda "
                            "savol soʻzi bor, shuning uchun ли qoʻyilmaydi. Matn "
                            "ikkala qurilishni yonma-yon koʻrsatadi.",
                "examples": ["Никто́ не знал, кто присыла́ет кни́ги.",
                             "Он посмотре́л, отку́да пришла́ посы́лка."],
            },
            {
                "pattern":  "Вряд ли",
                "meaning":  "«Dargumon» degan tayyor ibora. Ichida ли turibdi, "
                            "lekin u qotib qolgan — alohida tahlil qilinmaydi.",
                "examples": ["Вряд ли мы узна́ем, кто э́то."],
            },
        ],
        "body": '''<p>Ка́ждый год, пе́рвого сентября́, в шко́лу села́ Ивано́вка прихо́дит <span class="cn-word" data-tr="pochta posilkasi">посы́лка</span>. <span class="cn-word" data-tr="ichida">Внутри́</span> — кни́ги. Но́вые, хоро́шие кни́ги.</p>

<p><span class="cn-word" data-tr="joʻnatuvchi">Отправи́теля</span> в посы́лке нет. То́лько а́дрес шко́лы и <span class="cn-word" data-tr="sana">да́та</span>.</p>

<p>Пе́рвая посы́лка пришла́ в 2003 году́. Учителя́ тогда́ <span class="cn-word" data-pos="verb" data-tr="qaror qilishdi">реши́ли</span>, что э́то <span class="cn-word" data-tr="tasodif">случа́йность</span>. Но че́рез год посы́лка пришла́ сно́ва. И ещё че́рез год.</p>

<p>Ка́ждое ле́то в шко́ле начина́лся оди́н и тот же <span class="cn-word" data-tr="suhbat, gap">разгово́р</span>. <strong>Никто́ не знал, придёт ли</strong> посы́лка в э́том году́. И <strong>никто́ не знал, кто</strong> её присыла́ет.</p>

<p>Дире́ктор шко́лы не́сколько раз <span class="cn-word" data-pos="verb" data-tr="soʻradi">спра́шивал</span> на по́чте, <strong>зна́ют ли</strong> там отправи́теля. На по́чте отвеча́ли, что не зна́ют: посы́лку <span class="cn-word" data-pos="verb" data-tr="joʻnatishadi">присыла́ют</span> без и́мени.</p>

<p><span class="cn-word" data-tr="qorovul">Сто́рож</span> Никола́й Ива́нович рабо́тал в шко́ле три́дцать лет. <span class="cn-word" data-tr="bir kuni">Одна́жды</span> он взял ста́рые посы́лки и посмотре́л, <strong>отку́да они́ пришли́</strong>.</p>

<p>Все <span class="cn-word" data-tr="pochta shtempeli">шта́мпы</span> бы́ли из одного́ го́рода — из Ирку́тска.</p>

<p>Никола́й Ива́нович написа́л письмо́ на ирку́тскую по́чту. Он спроси́л, <strong>мо́жно ли</strong> узна́ть и́мя <span class="cn-word" data-tr="joʻnatuvchining">отправи́теля</span>. Он не <span class="cn-word" data-pos="verb" data-tr="umid qilmasdi">наде́ялся</span> на отве́т. «<strong>Вряд ли</strong> они́ <span class="cn-word" data-pos="verb" data-tr="qidira boshlaydi">ста́нут иска́ть</span>», — ду́мал он.</p>

<p>Отве́т пришёл че́рез два ме́сяца. Кни́ги присыла́ла <span class="cn-word" data-tr="ayol">же́нщина</span> по и́мени Ири́на Серге́евна. Она́ учи́лась в э́той шко́ле со́рок лет наза́д, пото́м <span class="cn-word" data-pos="verb" data-tr="ketib qoldi">уе́хала</span> и ста́ла врачо́м.</p>

<p>В 2003 году́ она́ позвони́ла в <span class="cn-word" data-tr="tuman markaziga">райо́н</span> и спроси́ла, <strong>рабо́тает ли</strong> ещё её ста́рая шко́ла. Ей отве́тили, что рабо́тает. <span class="cn-word" data-tr="oʻshandan beri">С тех пор</span> она́ присыла́ет кни́ги.</p>

<p>Тепе́рь в Ивано́вке зна́ют её и́мя. Но пе́рвого сентября́ никто́ уже́ не спра́шивает, придёт ли посы́лка.</p>

<p>Все <span class="cn-word" data-tr="allaqachon, shusiz ham">и так</span> зна́ют, что придёт.</p>''',
        "questions": [
            {
                "text": "Nikolay Ivanovich sirni qanday yechdi?",
                "choices": [
                    "Pochtachini kuzatib turdi",
                    "Eski posilkalardagi shtempellarga qaradi — hammasi Irkutskdan edi",
                    "Direktordan soʻradi",
                    "Kitoblarning ichidagi imzoni topdi"
                ],
                "answer": 1,
                "explanation": "«Он взял ста́рые посы́лки и посмотре́л, отку́да "
                               "они́ пришли́. Все шта́мпы бы́ли из одного́ "
                               "го́рода — из Ирку́тска». Shundan keyin u xat "
                               "yozdi.",
            },
            {
                "text": "Nega matnda «зна́ют ли там отправи́теля», lekin «кто её присыла́ет» — birida ли bor, ikkinchisida yoʻq?",
                "choices": [
                    "Chunki birinchisi oʻtgan zamonda",
                    "Chunki ikkinchisi inkor gap",
                    "Chunki ikkinchi gapda savol soʻzi «кто» bor — ли keraksiz",
                    "Chunki «присыла́ть» feʼli ли ni olmaydi"
                ],
                "answer": 2,
                "explanation": "Ли faqat «ha/yoʻq» savoli boʻlganda qoʻyiladi. "
                               "Gapda «кто», «где», «отку́да» kabi savol soʻzi "
                               "boʻlsa, ли ortiqcha — xuddi oʻzbekchada «kim "
                               "joʻnatadimi» deyilmagani kabi.",
            },
            {
                "text": "Hikoyaning oxiri nima demoqchi?",
                "choices": [
                    "Sir ochilgani yaxshi boʻlmadi",
                    "Irina Sergeyevna endi kitob joʻnatmaydi",
                    "Pochta xizmati yaxshi ishlaydi",
                    "Endi «keladimi?» degan savolning oʻzi kerak emas — hamma ishonadi"
                ],
                "answer": 3,
                "explanation": "«Никто́ уже́ не спра́шивает, придёт ли посы́лка. "
                               "Все и так зна́ют, что придёт». Yaʼni bilvosita "
                               "savol («придёт ли») oddiy tasdiqqa («что "
                               "придёт») aylandi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-69 — тот, кто / то, что                      HAYOT HIKOYASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Тот, кто са́жает дере́вья",
        "summary": (
            "PR-69 matni. Haqiqiy odam haqida: hindistonlik Jadav Payeng "
            "1979-yilda yalangʻoch qumli orolda yolgʻiz daraxt eka boshlagan "
            "va qirq yilda 550 gektarlik oʻrmon yaratgan. Faktlar haqiqiy."
        ),
        "order":   69,
        "grammar": [
            {
                "pattern":  "Тот, кто — odam haqida",
                "meaning":  "Ot boʻlmaganda «тот» otning oʻrnida turadi. Matnning "
                            "sarlavhasi ham, birinchi va oxirgi jumlasi ham shu "
                            "qurilishga qurilgan.",
                "examples": ["Тот, кто са́жает де́рево, ду́мает о други́х.",
                             "Тот, кого́ счита́ли стра́нным, оказа́лся прав."],
            },
            {
                "pattern":  "То, что — narsa yoki butun fikr haqida",
                "meaning":  "«То, что он сде́лал» — u qilgan ish. Predlogdan keyin "
                            "«то» hech qachon tushib qolmaydi: о том, что…",
                "examples": ["То, что он сде́лал, тепе́рь называ́ют ле́сом.",
                             "Никто́ не ду́мал о том, что бу́дет че́рез со́рок лет."],
            },
            {
                "pattern":  "Все, кто + birlik feʼl · де́ло в том, что",
                "meaning":  "«Кто» dan keyingi feʼl har doim birlikda turadi. "
                            "«Де́ло в том, что…» = «Gap shundaki…».",
                "examples": ["Все, кто ви́дел о́стров, говори́л одно́ и то же.",
                             "Де́ло в том, что земля́ была́ пуста́я."],
            },
        ],
        "body": '''<p>В Инди́и есть <span class="cn-word" data-tr="maqol">посло́вица</span>: <strong>тот, кто</strong> са́жает де́рево, ду́мает о други́х.</p>

<p>В 1979 году́ на реке́ Брахмапу́тра случи́лось большо́е <span class="cn-word" data-tr="toshqin">наводне́ние</span>. Вода́ ушла́ и оста́вила го́лый <span class="cn-word" data-tr="qumloq">песо́к</span>. На э́том песке́ уме́рло мно́го змей: там не́ было <span class="cn-word" data-tr="soya">те́ни</span>, и со́лнце уби́ло их за оди́н день.</p>

<p>Э́то уви́дел шестнадцатиле́тний ма́льчик. Его́ зва́ли Жада́в Па́йенг. Он жил на о́строве Маджу́ли и пас <span class="cn-word" data-tr="buyvollar">бу́йволов</span>.</p>

<p>Жада́в пошёл к <span class="cn-word" data-tr="kattalar">взро́слым</span> и спроси́л, что мо́жно сде́лать. Ему́ отве́тили, что на песке́ дере́вья не расту́т.</p>

<p>Тогда́ он взял два́дцать <span class="cn-word" data-tr="bambuk koʻchati">ростко́в бамбу́ка</span> и посади́л их сам.</p>

<p>Пото́м он приходи́л ка́ждый день. Он носи́л во́ду в вёдрах. Он де́лал <span class="cn-word" data-tr="soyabon, chodir">наве́сы</span> из ли́стьев, что́бы молоды́е дере́вья не сгоре́ли на со́лнце. Он приноси́л <span class="cn-word" data-tr="chumolilar">муравьёв</span>, что́бы они́ меня́ли <span class="cn-word" data-tr="tuproq">по́чву</span>.</p>

<p><strong>Все, кто</strong> ви́дел его́ в те го́ды, счита́л его́ стра́нным. <strong>Де́ло в том, что</strong> рабо́та была́ бесконе́чная, а <span class="cn-word" data-tr="natija">результа́т</span> никто́ не мог уви́деть.</p>

<p>Жада́в рабо́тал три́дцать лет. Оди́н.</p>

<p>В 2008 году́ на о́стров пришли́ <span class="cn-word" data-tr="mansabdorlar">чино́вники</span>. Они́ иска́ли <span class="cn-word" data-tr="fillar podasi">ста́до слоно́в</span>. И нашли́ лес.</p>

<p>Никто́ не знал <span class="cn-word" data-tr="bu haqda">об э́том</span> ле́се. На ка́рте его́ не́ было.</p>

<p>Сейча́с <strong>то, что</strong> посади́л Жада́в, занима́ет пятьсо́т пятьдеся́т гекта́ров. Там живу́т слоны́, <span class="cn-word" data-tr="karkidonlar">носоро́ги</span>, оле́ни и ти́гры. Лес называ́ют «Мола́и» — по <span class="cn-word" data-tr="laqab">про́звищу</span> Жада́ва.</p>

<p>В 2015 году́ Инди́я дала́ ему́ госуда́рственную <span class="cn-word" data-tr="mukofot">награ́ду</span>.</p>

<p>Журнали́сты спра́шивают его́ <strong>о том, что</strong> он чу́вствует. Жада́в отвеча́ет ко́ротко: он про́сто продолжа́ет сажа́ть.</p>

<p><strong>Тот, кого́</strong> счита́ли стра́нным, оказа́лся <span class="cn-word" data-tr="oddiygina">про́сто</span> терпели́вым.</p>''',
        "questions": [
            {
                "text": "Jadav Payeng nega daraxt eka boshladi?",
                "choices": [
                    "Hukumat undan shuni soʻradi",
                    "U orolda buyvollar uchun oʻtloq izlardi",
                    "Maktabda unga shunday topshiriq berishdi",
                    "Toshqindan keyin yalangʻoch qumda ilonlar soyasizlikdan qirilib ketdi"
                ],
                "answer": 3,
                "explanation": "«Там не́ было те́ни, и со́лнце уби́ло их за оди́н "
                               "день». Oʻn olti yoshli bola shuni koʻrgach, "
                               "yigirmata bambuk koʻchatini oʻzi ekdi.",
            },
            {
                "text": "Nega matnda «Все, кто ви́дел его́, счита́л» deyilgan — nega «счита́ли» emas?",
                "choices": [
                    "Chunki gap bitta odam haqida",
                    "Chunki bu oʻtgan zamon",
                    "Chunki feʼl «кто» ga tegishli, «кто» dan keyin esa birlik turadi",
                    "Bu matndagi xato"
                ],
                "answer": 2,
                "explanation": "«Кто» dan keyingi feʼl har doim birlikda boʻladi, "
                               "hatto «все» bilan ham. Asosiy gapga tegishli feʼl "
                               "esa koʻplikda turishi mumkin — bu ikki alohida "
                               "gap.",
            },
            {
                "text": "Matn oxirida Jadav haqida qanday xulosa chiqariladi?",
                "choices": [
                    "Uni gʻalati deb hisoblashardi, aslida esa u shunchaki sabrli edi",
                    "U mashhur boʻlishni xohlagan",
                    "U aslida gʻalati odam edi",
                    "U mukofot uchun ishlagan"
                ],
                "answer": 0,
                "explanation": "«Тот, кого́ счита́ли стра́нным, оказа́лся про́сто "
                               "терпели́вым». Bu yerda «тот» asosiy gapda ega "
                               "(И.п.), «кого́» esa oʻz gapida obyekt (В.п.) — "
                               "darsning ikki kelishik qoidasi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-70 — действительные причастия              ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Лю́ди, живу́щие на Се́вере",
        "summary": (
            "PR-70 matni. Rossiya Shimolida odamlar qanday yashaydi: qutb "
            "tuni, abadiy muzloq va ustunlar ustidagi uylar, kiyik boquvchi "
            "nenetslar. Sarlavhaning oʻzi — sifatdoshli oborot."
        ),
        "order":   70,
        "grammar": [
            {
                "pattern":  "Hozirgi zamon sifatdoshi: -ущ- / -ющ- / -ащ- / -ящ-",
                "meaning":  "«Они́» shaklidan yasaladi: живу́[т] → живу́щий. "
                            "Oʻzbekcha «-ayotgan / -adigan» ga toʻgʻri keladi.",
                "examples": ["лю́ди, живу́щие на Се́вере",
                             "учёные, изуча́ющие ве́чную мерзлоту́"],
            },
            {
                "pattern":  "Oʻtgan zamon sifatdoshi: -вш- / -ш-",
                "meaning":  "Oʻtgan zamon erkak shaklidan: вы́рос → вы́росший. "
                            "Oʻzbekcha «-gan».",
                "examples": ["челове́к, вы́росший в ту́ндре",
                             "по́езд, прише́дший у́тром"],
            },
            {
                "pattern":  "Vergul oʻringa bogʻliq",
                "meaning":  "Oborot otdan keyin tursa — ikki tomondan vergul. "
                            "Otdan oldin tursa (oʻzbekcha tartib) — vergulsiz.",
                "examples": ["дома́, стоя́щие на сва́ях",
                             "стоя́щие на сва́ях дома́"],
            },
        ],
        "body": '''<p>Над Поля́рным кру́гом со́лнце рабо́тает не так, как у нас. Зимо́й оно́ не встаёт, ле́том не сади́тся. В Нори́льске <span class="cn-word" data-tr="qutb tuni">поля́рная ночь</span> дли́тся со́рок пять дней.</p>

<p><strong>Лю́ди, живу́щие</strong> в таки́х города́х, привыка́ют к э́тому. Но <span class="cn-word" data-tr="tabiat, muhit">приро́да</span> ста́вит и други́е зада́чи.</p>

<p>Пе́рвая зада́ча — <span class="cn-word" data-tr="abadiy muzloq">ве́чная мерзлота́</span>. Э́то земля́, кото́рая не <span class="cn-word" data-pos="verb" data-tr="erimaydi">та́ет</span> да́же ле́том. Она́ начина́ется в одно́м ме́тре от пове́рхности и ухо́дит вниз на со́тни ме́тров.</p>

<p>Дом, <span class="cn-word" data-pos="verb" data-tr="turgan">стоя́щий</span> на тако́й земле́, гре́ет её. Мерзлота́ та́ет, и дом начина́ет па́дать.</p>

<p>Поэ́тому на Се́вере стро́ят ина́че. <strong>Дома́, стоя́щие</strong> в Яку́тске и Нори́льске, не каса́ются земли́: они́ стоя́т на <span class="cn-word" data-tr="ustunlar, qoziqlar">сва́ях</span>. Ме́жду до́мом и землёй хо́дит <span class="cn-word" data-tr="sovuq havo">холо́дный во́здух</span>. Земля́ остаётся <span class="cn-word" data-tr="sovuq">холо́дной</span>, и дом стои́т.</p>

<p>Втора́я зада́ча — <span class="cn-word" data-tr="masofa">расстоя́ние</span>. <strong>Не́нцы, живу́щие</strong> в ту́ндре, пасу́т <span class="cn-word" data-tr="bugʻular">оле́ней</span>. <span class="cn-word" data-tr="poda">Ста́до</span> идёт за <span class="cn-word" data-tr="yem, oziq">ко́рмом</span>, и лю́ди иду́т за ста́дом. За год семья́ прохо́дит со́тни киломе́тров.</p>

<p>Их дом называ́ется <span class="cn-word" data-tr="chum — kiyik terisidan chodir">чум</span>. Его́ мо́жно собра́ть за час и разобра́ть за час.</p>

<p>Челове́к, <span class="cn-word" data-pos="verb" data-tr="oʻsgan">вы́росший</span> в ту́ндре, чита́ет снег как кни́гу. Он ви́дит, где прошли́ оле́ни и когда́ бу́дет <span class="cn-word" data-tr="boʻron">пурга́</span>.</p>

<p>Тре́тья зада́ча — <span class="cn-word" data-tr="ovqat">еда́</span>. Овощи́ на Се́вере не расту́т. Но <strong>лю́ди, живу́щие</strong> здесь ты́сячи лет, нашли́ реше́ние: <span class="cn-word" data-tr="baliq">ры́ба</span> и оле́нина даю́т витами́н D, кото́рый в друго́м ме́сте даёт со́лнце.</p>

<p>Сейча́с в ту́ндре рабо́тают <strong>учёные, изуча́ющие</strong> мерзлоту́. Они́ говоря́т, что земля́ на́чала та́ять сли́шком бы́стро, и что дома́ на сва́ях тепе́рь на́до стро́ить ина́че.</p>

<p>Се́вер у́чит одному́: здесь выи́грывает не <span class="cn-word" data-tr="kuchli">си́льный</span>, а тот, кто <span class="cn-word" data-pos="verb" data-tr="dunyoni kuzatadi">смо́трит по сторона́м</span>.</p>''',
        "questions": [
            {
                "text": "Nega Shimolda uylar ustunlar ustiga quriladi?",
                "choices": [
                    "Uyning issigʻi abadiy muzloqni eritmasligi uchun",
                    "Qor uyni bosib qolmasligi uchun",
                    "Bugʻular uyning tagidan oʻtishi uchun",
                    "Toshqin suvi kirmasligi uchun"
                ],
                "answer": 0,
                "explanation": "«Дом, стоя́щий на тако́й земле́, гре́ет её. "
                               "Мерзлота́ та́ет, и дом начина́ет па́дать». "
                               "Ustunlar orasidan sovuq havo oʻtadi va yer "
                               "muzlagan holda qoladi.",
            },
            {
                "text": "«Челове́к, вы́росший в ту́ндре» — bu qanday shakl va nimani bildiradi?",
                "choices": [
                    "Hozirgi zamon sifatdoshi — «oʻsayotgan odam»",
                    "Oddiy sifat — «katta odam»",
                    "Oʻtgan zamon sifatdoshi — «oʻsgan odam»",
                    "Ravishdosh — «oʻsib»"
                ],
                "answer": 2,
                "explanation": "«Вы́рос» — oʻtgan zamon erkak shakli, unda -л "
                               "yoʻq, shuning uchun -ш- qoʻshilib «вы́росший» "
                               "hosil boʻlgan. Uni «кото́рый вы́рос» deb yoyish "
                               "mumkin.",
            },
            {
                "text": "Nega «Дома́, стоя́щие в Яку́тске…» da vergul bor, «стоя́щие на сва́ях дома́» da esa yoʻq?",
                "choices": [
                    "Chunki birinchisi koʻplikda",
                    "Chunki ikkinchisida oborot qisqaroq",
                    "Bu erkin tanlov, qoida yoʻq",
                    "Chunki vergul oborot otdan KEYIN turgandagina qoʻyiladi"
                ],
                "answer": 3,
                "explanation": "Oborot otdan keyin tursa — ikki tomondan vergul. "
                               "Otdan oldin tursa (oʻzbekcha tartib — «ustunlar "
                               "ustida turgan uylar») vergul umuman "
                               "qoʻyilmaydi.",
            },
        ],
    },
]
