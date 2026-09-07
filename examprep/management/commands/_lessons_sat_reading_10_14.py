# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — Reading lessons 10-14
Topic: "So'z ma'nosi kontekstda (Words in Context)".
See toc_sat_reading.txt and STYLE_GUIDE_SAT_RW.md.

Words in Context is the largest single question type on the test. From this topic
onward almost every question is a real exam question, so stems and choices are in
English and every explanation is in Uzbek (guide §0).
"""

TRACK = {
    "name":    "SAT",
    "summary": "Digital SAT — Reading and Writing bo'limiga savol turlari bo'yicha "
               "tayyorgarlik. Imtihonning matematik yarmi Prime SAT Math kursida.",
    "icon":    "bi-mortarboard",
    "color":   "#7c3aed",
    "order":   3,
}

TOPIC_WIC = {
    "title":   "So'z ma'nosi kontekstda (Words in Context)",
    "summary": "Imtihondagi eng ko'p uchraydigan savol turi: bo'sh joyga so'z tanlash "
               "va berilgan so'zning shu gapdagi ma'nosini aniqlash.",
    "icon":    "bi-fonts",
    "order":   2,
}

TIP   = ('<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>💡 Maslahat:</strong> {}</div>')
WARN  = ('<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>⚠️ Tuzoq:</strong> {}</div>')
NOTE  = ('<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>📌 Eslatma:</strong> {}</div>')
EXAMP = ('<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>📝 Namuna:</strong> {}</div>')


def why(rows):
    """Build an .sr-why choice autopsy. rows = [(ok, choice_text, uzbek_reason), ...]

    The choice text MUST start with the choice's own opening words — the pupil finds
    the row by scanning it against a shuffled list (guide §6).
    """
    out = ['<div class="sr-why">']
    for ok, choice, reason in rows:
        kind = 'ok' if ok else 'no'
        tag = "TO‘G‘RI" if ok else "TUZOQ"
        out.append(
            f'<div class="sr-why__row sr-why__row--{kind}">'
            f'<span class="sr-why__tag">{tag}</span>'
            f'<span class="sr-why__text"><b>{choice}</b> — {reason}</span></div>'
        )
    out.append('</div>')
    return ''.join(out)


def blank_q(passage, stem="Which choice completes the text with the most logical and "
                          "precise word or phrase?"):
    return (f'<div class="sr-passage">{passage}</div>'
            f'<p><strong>{stem}</strong></p>')


def means_q(passage, word):
    return (f'<div class="sr-passage">{passage}</div>'
            f'<p><strong>As used in the text, what does the word “{word}” most nearly '
            f'mean?</strong></p>')


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 10
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_WIC,
    "title": "SAT R&W 10: Words in Context — The Two Shapes: Fill the Blank and “Most Nearly Means”",
    "summary": "Imtihondagi eng ko'p uchraydigan savol turining ikki shakli va ularning "
               "bitta umumiy qoidasi: javobni lug'at emas, gap belgilaydi.",
    "order": 10,
    "blocks": [
        {"rich_text": (
            "<h2>Eng ko'p uchraydigan savol turi</h2>"
            "<p><strong>Words in Context</strong> — <em>Craft and Structure</em> "
            "domenidagi eng katta bo'lak. Craft and Structure butun bo'limning "
            "~28 foizini (13–15 savol) tashkil qiladi, va Words in Context o'sha "
            "guruhdagi eng ko'p uchraydigan tur. Bluebook mashq testlarida bu guruh "
            "modul boshida keladi — ya'ni siz ularni odatda birinchi ko'rasiz.</p>"
            "<p>Yaxshi yangilik: bu <mark>lug'at imtihoni emas</mark>. Yomon yangilik: "
            "ko'p o'quvchi uni lug'at imtihoni deb o'ylab, noto'g'ri narsaga "
            "tayyorlanadi — minglab so'z yodlaydi va baribir yiqiladi.</p>"
            '<span class="sr-time">⏱ Maqsad: ~40 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ikki shakl</h3>"
            "<p>Bu savol turi ekranda faqat ikki xil ko'rinishda keladi:</p>"
            + EXAMP.format(
                "<p><strong>1-shakl — bo'sh joyni to'ldirish.</strong> Matn ichida "
                "bo'shliq bor, savol esa har doim bir xil:</p>"
                "<p><em>Which choice completes the text with the most logical and "
                "precise word or phrase?</em></p>"
                "<p>To'rtta variant — odatda bir so'z yoki qisqa ibora.</p>")
            + EXAMP.format(
                "<p><strong>2-shakl — berilgan so'zning ma'nosi.</strong> Matndagi bitta "
                "so'z ostiga chizilgan, savol esa:</p>"
                "<p><em>As used in the text, what does the word “X” most nearly "
                "mean?</em></p>"
                "<p>To'rtta variant — o'sha so'zning turli ma'nolari.</p>")
            + "<p>Ikkalasi bir xil ko'nikmani tekshiradi va bir xil usul bilan "
            "yechiladi. Farqi shundaki, birinchisida so'zni <u>siz topasiz</u>, "
            "ikkinchisida so'z berilgan va siz uning <u>shu gapdagi</u> ma'nosini "
            "topasiz.</p>"
        )},

        {"rich_text": (
            "<h3>Aslida nima tekshirilyapti</h3>"
            "<p>Ikkala shaklda ham savol bitta: <mark>shu gap qanday ma'noni talab "
            "qilyapti?</mark> Lug'atdagi ma'no emas — <u>shu gapdagi</u> ma'no.</p>"
            "<p>Buni ko'rsatadigan eng oddiy dalil: «most nearly means» savollarida "
            "so'zlar deyarli har doim <strong>siz biladigan</strong> so'zlar bo'ladi — "
            "<em>sound</em>, <em>reserved</em>, <em>bound</em>, <em>figure</em>. "
            "Qiyinligi so'zda emas, o'sha so'zning kutilmagan ma'nosida.</p>"
            "<p>Va bo'sh joyli savollarda to'rtta variantning hammasi grammatik "
            "jihatdan to'g'ri o'tiradi. Grammatika bu savolni hech qachon "
            "hal qilmaydi — faqat ma'no hal qiladi.</p>"
            + NOTE.format(
                "Shuning uchun bu turga tayyorgarlik — <u>so'z yodlash emas</u>. "
                "Tayyorgarlik: gapning mantiqini o'qishni mashq qilish. "
                "Lug'at yordam beradi, lekin u ikkinchi darajali. "
                "12-darsda gapning mantiqini ochib beradigan <strong>signal "
                "so'zlar</strong>ni o'rganamiz — asosiy quroling o'sha bo'ladi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna — 1-shakl</h3>"
            "<p><u>Hozircha javob bermang</u> — birgalikda yechamiz.</p>"
            + blank_q(
                "<p>The suzani embroideries of Bukhara were produced by several hands "
                "at once. A designer drew the pattern in ink, and the women of a "
                "household stitched separate panels that were sewn together only at the "
                "end. Because each panel was finished independently, small differences "
                "in dye lot and stitch tension survive in the completed cloth. Far from "
                "treating these differences as flaws, specialists now use them to "
                "<span class=\"sr-blank\"></span> individual makers within a single "
                "piece.</p>")
            + "<ol type=\"A\"><li>conceal</li><li>identify</li><li>commission</li>"
              "<li>standardise</li></ol>"
            '<span class="sr-time">⏱ ~40 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Qanday yechamiz</h3>"
            "<p><strong>1-qadam. Variantlarni yoping.</strong> Rostdan ham — barmog'ingiz "
            "bilan yoping. Ular hozir sizga faqat xalaqit beradi.</p>"
            "<p><strong>2-qadam. Bo'sh joy atrofidagi mantiqni o'qing.</strong> "
            "Ikki tayanch bor: farqlar <em>saqlanib qolgan</em> (<em>survive</em>), va "
            "mutaxassislar ularni <em>kamchilik deb hisoblamaydi</em> "
            "(<em>Far from treating these differences as flaws</em>). Demak farqlar "
            "ularga <u>foydali</u>. Nima uchun foydali? Har panelni boshqa odam "
            "tikkan.</p>"
            "<p><strong>3-qadam. O'z so'zingizni ayting</strong> — o'zbekcha bo'lsa "
            "ham bo'ladi: «farqlar yordamida <mark>kim tikkanini ajratish</mark> "
            "mumkin».</p>"
            "<p><strong>4-qadam. Endi variantlarni oching va solishtiring.</strong></p>"
            + why([
                (True, "identify",
                 "«aniqlash, kimligini bilish». Bashoratimizga aynan mos: farqlar "
                 "ustalarni bir-biridan ajratadi. Isbot ekranda — <em>Far from … "
                 "flaws</em> farqlar foydali ekanini aytadi."),
                (False, "conceal",
                 "«yashirish» — mantiqni teskari qiladi. Agar farqlar ustalarni "
                 "yashirsa, mutaxassislar ulardan foydalana olmasdi."),
                (False, "commission",
                 "«buyurtma bermoq» — mutaxassislar bugun asrlar oldingi ustalarga "
                 "buyurtma berolmaydi. Gapga mantiqan sig'maydi, garchi grammatik "
                 "jihatdan bemalol o'tirsa ham."),
                (False, "standardise",
                 "«bir xil qilib standartlashtirmoq» — farqlarning mavjudligiga zid. "
                 "Bu matndagi kuchli tushunchani (farqlar) olib, uni yo'q qiladigan "
                 "so'z: <strong>so'z-tuzoq</strong>."),
            ])
            + TIP.format(
                "1-qadam — variantlarni yopish — bepul va eng ko'p ball qutqaradi. "
                "Bo'sh bosh bilan to'rt so'zni o'qigan odam «eng chiroylisi»ni "
                "tanlaydi. Tayyor bashorat bilan o'qigan odam esa shunchaki "
                "<u>mosini topadi</u>.")
        )},

        {
            "rich_text": blank_q(
                "<p>Tardigrades, the microscopic animals sometimes called water bears, "
                "can survive being dried until almost no water remains in their tissues. "
                "In this state their metabolism falls to levels that instruments cannot "
                "detect, and they may remain so for years. A few hours in water restores "
                "them. The dried state is therefore not a form of death but a "
                "<span class=\"sr-blank\"></span> one: the animal has been suspended "
                "rather than ended.</p>"),
            "choices": [
                {"text": "reversible", "is_correct": True},
                {"text": "permanent", "is_correct": False},
                {"text": "gradual", "is_correct": False},
                {"text": "contagious", "is_correct": False},
            ],
            "explanation": (
                "<p>Ikki nuqta (<em>:</em>) dan keyingi qism bo'sh joyning ma'nosini "
                "qaytaradi: <em>suspended rather than ended</em> — «to'xtatilgan, "
                "tugatilmagan». To'xtatilgan narsani qayta ishga tushirish mumkin. "
                "Bashoratimiz: <mark>«qaytariladigan»</mark>.</p>"
                + why([
                    (True, "reversible",
                     "«orqaga qaytariladigan». <em>A few hours in water restores "
                     "them</em> — bu javobning to'g'ridan-to'g'ri isboti."),
                    (False, "permanent",
                     "«doimiy» — <em>not a form of death but a ___ one</em> "
                     "qurilishini buzadi. <em>but</em> qarama-qarshilik talab qilyapti, "
                     "«doimiy» esa o'limga qarshi emas, unga yaqin."),
                    (False, "gradual",
                     "«bosqichma-bosqich» — tezlik haqida. Matn quriyish tezligini "
                     "emas, holatning <u>qaytarilishini</u> muhokama qilyapti. "
                     "Rost bo'lishi mumkin, lekin so'ralmagan."),
                    (False, "contagious",
                     "«yuqumli» — matnda kasallik ham, boshqa hayvonga o'tish ham "
                     "umuman yo'q. <strong>Tashqi bilim</strong> tuzog'i: «hayvon + "
                     "biologiya» degan assotsiatsiya."),
                ])
            ),
        },

        {
            "rich_text": means_q(
                "<p>Al-Khwarizmi's treatise on calculation with Hindu numerals did not "
                "invent the decimal system it described; it carried that system westward. "
                "Latin translators, working from copies made centuries after his death, "
                "rendered his name as <em>Algoritmi</em>, and in time the word came to "
                "<span class=\"sr-focus\">stand for</span> any step-by-step procedure of "
                "calculation whatever.</p>", "stand for"),
            "choices": [
                {"text": "represent", "is_correct": True},
                {"text": "tolerate", "is_correct": False},
                {"text": "replace", "is_correct": False},
                {"text": "defend", "is_correct": False},
            ],
            "explanation": (
                "<p><em>stand for</em> — o'zingiz biladigan ibora, lekin uning kamida "
                "uchta ma'nosi bor. Gap qaysinisini talab qilyapti? "
                "<em>the word came to ___ any step-by-step procedure</em> — so'z "
                "biror narsani <u>bildiradi</u>, ya'ni nom bo'lib xizmat qiladi.</p>"
                + why([
                    (True, "represent",
                     "«bildirmoq, anglatmoq». So'z va u anglatgan tushuncha — aynan shu "
                     "munosabat. Isbot: <em>the word came to ___ any … procedure</em>."),
                    (False, "tolerate",
                     "«chidamoq» — <em>I won't stand for it</em> iborasidagi ma'no. "
                     "Real ma'no, lekin bu gapda so'z chidamaydi, balki nom bo'ladi. "
                     "<strong>Eng ko'p tanlanadigan noto'g'ri javob.</strong>"),
                    (False, "replace",
                     "«o'rnini bosmoq» — <em>Algoritmi</em> so'zi protseduralarning "
                     "o'rnini bosmaydi, ularni nomlaydi."),
                    (False, "defend",
                     "«himoya qilmoq» — <em>stand for a cause</em> ma'nosi. Matnda "
                     "hech kim hech nimani himoya qilmayapti."),
                ])
                + NOTE.format(
                    "Al-Xorazmiy (IX asr) o'nlik sanoq tizimini ixtiro qilmagan — u "
                    "Hindistondan kelgan tizimni tasvirlagan va u orqali G'arbga "
                    "yetkazgan. Uning nomining lotincha shakli — <em>Algoritmi</em> — "
                    "«algoritm» so'ziga aylangan. Mavzu tanish bo'lsa ham, javob "
                    "faqat matndan olinadi.")
            ),
        },

        {
            "rich_text": means_q(
                "<p>The house had belonged to the family for four generations, and "
                "Dilnoza had grown up hearing it discussed the way one discusses a "
                "difficult relative. Her grandmother spoke of its leaking roof with "
                "something close to pride. So when the notary asked whether she intended "
                "to sell, Dilnoza found that she could not "
                "<span class=\"sr-focus\">entertain</span> the question at all — not for "
                "a moment, not even long enough to refuse it.</p>", "entertain"),
            "choices": [
                {"text": "consider", "is_correct": True},
                {"text": "amuse", "is_correct": False},
                {"text": "answer", "is_correct": False},
                {"text": "welcome", "is_correct": False},
            ],
            "explanation": (
                "<p>Tiredan keyingi qism savolni hal qiladi: <em>not even long enough to "
                "refuse it</em>. Rad etish ham javobning bir turi — demak u javob "
                "berish bosqichiga <u>yetib ham bormagan</u>. Undan oldingi bosqich "
                "nima? Savol ustida <mark>o'ylab ko'rish</mark>.</p>"
                + why([
                    (True, "consider",
                     "«o'ylab ko'rmoq». <em>entertain an idea / a question</em> — bu "
                     "iboraning eng ko'p uchraydigan kitobiy ma'nosi, va tiredan "
                     "keyingi izoh aynan shuni ko'rsatadi."),
                    (False, "amuse",
                     "«ko'ngil ochmoq» — so'zning eng mashhur ma'nosi, va shuning uchun "
                     "eng xavfli variant. Savol odamni qiziqtirmaydi; bu yerda "
                     "<u>hech kim ko'ngil ochmayapti</u>."),
                    (False, "answer",
                     "«javob bermoq» — matn buni <strong>ataylab</strong> istisno "
                     "qiladi: <em>not even long enough to refuse it</em>. Agar tire "
                     "bo'lmasa, bu variant himoya qilinardi — SAT shuning uchun o'sha "
                     "izohni qo'shgan."),
                    (False, "welcome",
                     "«mamnuniyat bilan qabul qilmoq» — hissiyot qo'shadi, matnda esa "
                     "Dilnoza savoldan xursand ham, xafa ham emas: u shunchaki "
                     "savolni qabul qila olmayapti."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>Public libraries were once defended chiefly as engines of "
                "self-improvement for working readers. Surveys of urban branches point "
                "to a second function that the original argument never anticipated: the "
                "buildings are among the few indoor places a person may sit all day "
                "without spending money. Librarians increasingly describe this role as "
                "<span class=\"sr-blank\"></span> rather than incidental, and it now "
                "shapes staffing, opening hours and the design of new branches.</p>"),
            "choices": [
                {"text": "central", "is_correct": True},
                {"text": "obsolete", "is_correct": False},
                {"text": "temporary", "is_correct": False},
                {"text": "theoretical", "is_correct": False},
            ],
            "explanation": (
                "<p><em>rather than incidental</em> — bu ikki so'z javobni sovg'a "
                "qilyapti. <em>incidental</em> = «tasodifiy, ikkinchi darajali». "
                "<em>rather than</em> qarama-qarshilik talab qiladi, demak bo'sh joyga "
                "<mark>«ikkinchi darajali»ning aksi</mark> kerak.</p>"
                "<p>Ikkinchi isbot ham bor: <em>it now shapes staffing, opening hours "
                "and the design of new branches</em> — kadr, ish vaqti va binoni "
                "belgilaydigan narsa ikkinchi darajali emas.</p>"
                + why([
                    (True, "central",
                     "«markaziy, asosiy» — <em>incidental</em>ning to'g'ridan-to'g'ri "
                     "aksi, va ikkinchi jumla buni tasdiqlaydi."),
                    (False, "obsolete",
                     "«eskirgan» — matn bu rolning <u>yangi</u> va o'sib borayotganini "
                     "aytyapti. Aynan teskari."),
                    (False, "temporary",
                     "«vaqtinchalik» — <em>all day</em> iborasidan ilinib qolgan "
                     "<strong>so'z-tuzoq</strong>. Odam kun bo'yi o'tiradi, lekin "
                     "kutubxonaning <u>roli</u> vaqtinchalik emas."),
                    (False, "theoretical",
                     "«nazariy» — <em>it now shapes staffing, opening hours</em> "
                     "amaliy, real oqibatlarni sanayapti. Nazariy narsa ish vaqtini "
                     "o'zgartirmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Uchta doimiy tuzoq</h3>"
            "<p>Words in Context savollarida noto'g'ri variantlar deyarli har doim "
            "shu uch shakldan biri bo'ladi:</p>"
            '<div class="sr-data"><div class="sr-data__scroll">'
            "<table>"
            "<thead><tr><th>Tuzoq</th><th>Qanday ishlaydi</th></tr></thead>"
            "<tbody>"
            "<tr><td>Eng mashhur ma'no</td><td>So'zning siz biladigan birinchi ma'nosi — "
            "lekin bu gapda boshqa ma'no ishlayapti (<em>entertain</em> = ko'ngil ochmoq)</td></tr>"
            "<tr><td>Teskari yo'nalish</td><td>Ma'nosi to'g'ri sohadan, lekin "
            "qarama-qarshi tomonga (<em>conceal</em> ↔ <em>identify</em>)</td></tr>"
            "<tr><td>Matndan ilingan so'z</td><td>Matndagi biror so'zga bog'lanadi-yu, "
            "bo'sh joyning mantiqiga aloqasi yo'q (<em>temporary</em> ← <em>all day</em>)</td></tr>"
            "</tbody></table>"
            "</div></div>"
            + WARN.format(
                "To'rtta variantning hammasi grammatik jihatdan joyiga tushadi — "
                "SAT buni ataylab shunday qiladi. «Qaysi biri chiroyli o'qiladi?» "
                "degan savol sizni har safar noto'g'ri javobga olib boradi. "
                "Yagona savol: <u>gap qaysi ma'noni talab qilyapti?</u>")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            '<div class="pp-flashcards" data-pp-flashcards>'
            '<div class="pp-card"><div class="pp-card-front">to stand for</div><div class="pp-card-back">bildirmoq, anglatmoq (nom bo\'lib xizmat qilmoq)</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to entertain (an idea)</div><div class="pp-card-back">(fikrni) o\'ylab ko\'rmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">reversible</div><div class="pp-card-back">orqaga qaytariladigan</div></div>'
            '<div class="pp-card"><div class="pp-card-front">incidental</div><div class="pp-card-back">tasodifiy, ikkinchi darajali</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to anticipate</div><div class="pp-card-back">oldindan ko\'zda tutmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to render (a name)</div><div class="pp-card-back">(nomni) shu shaklda yetkazmoq, o\'girmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">flaw</div><div class="pp-card-back">nuqson, kamchilik</div></div>'
            '<div class="pp-card"><div class="pp-card-front">far from ~</div><div class="pp-card-back">~ o\'rniga, aksincha (kuchli qarama-qarshilik signali)</div></div>'
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Ikki shakl: <strong>bo'sh joyni to'ldirish</strong> va <strong>«most "
            "nearly means»</strong>. Usul bir xil.</li>"
            "<li>Bu <u>lug'at imtihoni emas</u>: so'zlar tanish, ma'nolari "
            "kutilmagan.</li>"
            "<li><strong>Variantlarni yoping</strong>, mantiqni o'qing, o'z so'zingizni "
            "ayting — keyingina variantlarni oching.</li>"
            "<li>To'rtala variant ham grammatik jihatdan to'g'ri o'tiradi; "
            "faqat <u>ma'no</u> hal qiladi.</li>"
            "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 11
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_WIC,
    "title": "SAT R&W 11: Read the Sentence, Not the Word — Predicting Before You Look",
    "summary": "Variantlarni ochishdan oldin javobni o'zingiz aytish usuli: bashorat "
               "aniq so'z bo'lishi shart emas, to'g'ri yo'nalish va ma'no yetarli.",
    "order": 11,
    "blocks": [
        {"rich_text": (
            "<h2>Avval bashorat, keyin variantlar</h2>"
            "<p>10-darsda ko'rdik: to'rtala variant ham grammatik jihatdan joyiga "
            "tushadi. Demak variantlar sizga <u>hech qanday</u> ma'lumot bermaydi — "
            "ular faqat chalg'itadi. Bu darsda o'sha chalg'itishdan qutuladigan bitta "
            "odatni o'rnatamiz.</p>"
            "<p>Odat oddiy: <mark>variantlarni ochishdan oldin javobni o'zingiz "
            "ayting</mark>. Ko'pchilik buni «vaqt yo'qotish» deb o'ylaydi. Aslida u "
            "vaqt <u>tejaydi</u>: tayyor bashorat bilan to'rtta variantni ajratish "
            "besh soniya oladi, bashoratsiz esa ikki variant orasida yarim daqiqa "
            "ikkilanasiz.</p>"
            '<span class="sr-time">⏱ Bashorat bilan: ~35 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Bashorat qanday bo'lishi kerak</h3>"
            "<p>Eng katta noto'g'ri tushuncha: «men to'g'ri inglizcha so'zni topishim "
            "kerak». <strong>Yo'q.</strong> Bashoratingiz:</p>"
            '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            "<div class=\"pp-step\"><p><strong>O'zbekcha bo'lishi mumkin.</strong> "
            "«bu yerda “ajratish” ma'nosi kerak» — bu to'liq yaroqli bashorat. Uni "
            "inglizchaga tarjima qilish shart emas; variantlar orasidan mos "
            "ma'nolisini topasiz.</p></div>"
            "<div class=\"pp-step\"><p><strong>Bir so'z emas, ibora bo'lishi "
            "mumkin.</strong> «kutilganidan kichikroq», «hammaga ma'lum emas» — "
            "bular ham yetarli.</p></div>"
            "<div class=\"pp-step\"><p><strong>Ba'zan faqat “+” yoki “−” yetadi.</strong> "
            "Agar gapdan shu qadar aniq bo'lsaki, bo'sh joyga <u>ijobiy</u> yoki "
            "<u>salbiy</u> ma'no kerak — ko'pincha shuning o'zi ikki-uchta variantni "
            "o'chiradi.</p></div>"
            "<div class=\"pp-step\"><p><strong>Matndagi so'zning o'zi bo'lishi "
            "mumkin.</strong> Ko'p savolda javob matnning boshqa joyida boshqa "
            "so'z bilan allaqachon aytilgan. Bashoratingiz o'sha ibora bo'lsin.</p></div>"
            "</div>"
            + TIP.format(
                "Bashoratingiz variantlarning hech biriga to'g'ri kelmasa — "
                "<u>bu ham ma'lumot</u>. Demak gapni noto'g'ri o'qigansiz. "
                "Variantlardan birini «majburan» tanlash o'rniga, matnga qayting va "
                "mantiqni qayta o'qing. Bu holat kamdan-kam, lekin bo'lganda "
                "deyarli har doim xato o'qishdan chiqadi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + blank_q(
                "<p>A coral reef looks like stone, and most of a reef is stone: the "
                "calcium carbonate skeletons of polyps that died long ago. Only the "
                "outermost film, a few millimetres thick, is alive at any moment. The "
                "apparent solidity of a reef is therefore "
                "<span class=\"sr-blank\"></span> — what appears to be a single ancient "
                "organism is a thin living layer resting on its own remains.</p>")
            + "<ol type=\"A\"><li>permanent</li><li>misleading</li><li>accidental</li>"
              "<li>recent</li></ol>"
            "<p><strong>Bashorat (variantlarni ochmasdan):</strong> gapning ikki qismi "
            "bir-biriga qarshi turibdi — <em>looks like stone / appears to be a single "
            "ancient organism</em> ↔ <em>a thin living layer</em>. Ya'ni ko'rinish bilan "
            "haqiqat bir xil emas. Bashoratim: <mark>«aldaydi», «ko'rinishi "
            "chalg'ituvchi»</mark>. Endi variantlarga qaraymiz.</p>"
            + why([
                (True, "misleading",
                 "«chalg'ituvchi» — bashoratga aynan mos. Tiredan keyingi qism "
                 "(<em>what appears to be … is …</em>) ko'rinish va haqiqat "
                 "o'rtasidagi farqni ochiq aytadi."),
                (False, "permanent",
                 "«doimiy» — tiredan keyingi izohga aloqasi yo'q. U rifning "
                 "<u>qanchalik uzoq yashashi</u> haqida, matn esa uning "
                 "<u>ko'rinishi</u> haqida gapiryapti."),
                (False, "accidental",
                 "«tasodifiy» — rifning qattiqligi tasodif emas, u skeletlardan "
                 "tuzilgan. Matn buni aynan tushuntirib beryapti."),
                (False, "recent",
                 "«yaqinda paydo bo'lgan» — matndagi <em>ancient</em> so'ziga "
                 "yopishgan <strong>so'z-tuzoq</strong>. Rifning yoshi emas, "
                 "ko'rinishining rostligi muhokama qilinyapti."),
            ])
            + NOTE.format(
                "Diqqat qiling: bashoratim inglizcha <em>misleading</em> emas edi — "
                "o'zbekcha «aldaydi» edi. Shu yetarli bo'ldi.")
        )},

        {
            "rich_text": blank_q(
                "<p>Before standardised time zones, every town kept its own clock, set "
                "by the sun at local noon. The railways made this arrangement "
                "<span class=\"sr-blank\"></span>: a train leaving one town at midday "
                "might arrive in the next at an hour that no timetable could state, "
                "because the two towns did not agree on what hour it was. Pressure for a "
                "shared standard came less from astronomers than from schedulers.</p>"),
            "choices": [
                {"text": "untenable", "is_correct": True},
                {"text": "convenient", "is_correct": False},
                {"text": "traditional", "is_correct": False},
                {"text": "inexpensive", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bashorat:</strong> ikki nuqtadan keyin muammo tasvirlangan "
                "— jadval tuzib bo'lmaydi, chunki shaharlar vaqt haqida "
                "kelisha olmaydi. Demak eski tartib <mark>«ishlamay qoldi»</mark>.</p>"
                + why([
                    (True, "untenable",
                     "«saqlab bo'lmaydigan, chidab bo'lmas holatga kelgan». Ikki "
                     "nuqtadan keyingi butun jumla — bu so'zning izohi."),
                    (False, "convenient",
                     "«qulay» — mantiqni teskari qiladi. Ikki nuqtadan keyin "
                     "noqulaylik tasvirlangan, qulaylik emas."),
                    (False, "traditional",
                     "«an'anaviy» — mahalliy vaqt haqiqatan an'anaviy edi, va shuning "
                     "uchun bu variant jozibali. Lekin temir yo'l uni an'anaviy "
                     "<u>qilmadi</u> — u allaqachon an'anaviy edi. Gap "
                     "<em>made this arrangement ___</em> deyapti: temir yo'l uni "
                     "<u>nimaga aylantirdi</u>? <strong>Rost, lekin so'ralmagan.</strong>"),
                    (False, "inexpensive",
                     "«arzon» — matnda pul haqida bir og'iz ham yo'q."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>A film editor's most consequential decisions are the ones an audience "
                "never notices. A cut placed two frames earlier can make a character seem "
                "decisive rather than hesitant, and almost no viewer will trace the "
                "impression back to the edit; they will say the actor was good. The craft "
                "is thus <span class=\"sr-blank\"></span> by design — its success is "
                "measured by how completely it escapes attention.</p>"),
            "choices": [
                {"text": "invisible", "is_correct": True},
                {"text": "collaborative", "is_correct": False},
                {"text": "improvised", "is_correct": False},
                {"text": "expensive", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bashorat:</strong> tiredan keyingi qism to'g'ridan-to'g'ri "
                "izoh: <em>its success is measured by how completely it escapes "
                "attention</em> — «sezilmasligi bilan o'lchanadi». Bashoratim: "
                "<mark>«ko'rinmas»</mark>.</p>"
                + why([
                    (True, "invisible",
                     "«ko'rinmas». <em>escapes attention</em> va birinchi jumladagi "
                     "<em>an audience never notices</em> — ikkita mustaqil isbot."),
                    (False, "collaborative",
                     "«hamkorlikdagi» — kino haqiqatan jamoaviy ish, va bu "
                     "<strong>tashqi bilim</strong> shuning uchun jozibali. Lekin matn "
                     "montajchi bilan boshqalarning hamkorligi haqida emas, "
                     "tomoshabinning sezmasligi haqida."),
                    (False, "improvised",
                     "«ekspromt» — aksincha, matn juda aniq hisoblangan qarorni "
                     "tasvirlaydi (<em>two frames earlier</em>)."),
                    (False, "expensive",
                     "«qimmat» — matnda xarajat umuman muhokama qilinmaydi."),
                ])
                + TIP.format(
                    "Tire (—), ikki nuqta (:) va nuqtali vergul (;) — Words in Context "
                    "savollarining eng saxiy do'sti. Ular ko'pincha bo'sh joyni "
                    "keyingi jumlada <u>boshqa so'zlar bilan qaytaradi</u>. Bo'sh joy "
                    "ko'rsangiz, avval shu belgilarni qidiring.")
            ),
        },

        {
            "rich_text": blank_q(
                "<p>Mycorrhizal fungi thread through soil and link the roots of separate "
                "plants. Sugars made by one tree can be detected days later in a "
                "neighbour, and seedlings growing in deep shade survive at rates their "
                "own photosynthesis cannot <span class=\"sr-blank\"></span>. Whether the "
                "transfer benefits the donor, or is simply leakage that the fungus "
                "happens to carry, remains disputed.</p>"),
            "choices": [
                {"text": "account for", "is_correct": True},
                {"text": "measure", "is_correct": False},
                {"text": "increase", "is_correct": False},
                {"text": "prevent", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bashorat:</strong> soyada o'sgan niholning omon qolish "
                "darajasi o'z fotosintezidan kutilganidan yuqori. Ya'ni fotosintez bu "
                "raqamni <mark>«tushuntira olmaydi»</mark> — shuning uchun olimlar "
                "boshqa manbani (qo'shni daraxtning shakarini) qidiryapti.</p>"
                + why([
                    (True, "account for",
                     "«tushuntirmoq, izohlab bermoq». Butun jumlaning mantiqi shunga "
                     "qurilgan: raqam tushuntirilmagani uchun uchinchi jumla sabab "
                     "izlaydi."),
                    (False, "measure",
                     "«o'lchamoq» — fotosintez o'lchov asbobi emas, jarayon. Bu variant "
                     "ilmiy matn muhitidan ilinib qolgan: matnda o'lchov bor "
                     "(<em>detected</em>), lekin uni fotosintez qilmaydi."),
                    (False, "increase",
                     "«oshirmoq» — grammatik jihatdan chiroyli o'tiradi va shuning "
                     "uchun xavfli. Lekin ma'nosi teskari: fotosintez omon qolishni "
                     "oshiradi, «oshira olmaydi» degani mantiqni buzadi."),
                    (False, "prevent",
                     "«oldini olmoq» — fotosintez omon qolishga yordam beradi, "
                     "unga to'sqinlik qilmaydi."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>Aziz had rehearsed the apology for three days, and it was, he "
                "thought, a good one: it admitted the fault, explained nothing and asked "
                "for nothing in return. What he had not rehearsed was his sister's "
                "silence afterwards, which <span class=\"sr-blank\"></span> every "
                "sentence he had prepared and left him standing in the doorway with "
                "nothing to add.</p>"),
            "choices": [
                {"text": "outlasted", "is_correct": True},
                {"text": "echoed", "is_correct": False},
                {"text": "interrupted", "is_correct": False},
                {"text": "improved", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bashorat:</strong> oxirgi bo'lak hal qiladi — "
                "<em>left him standing in the doorway with nothing to add</em>. "
                "Tayyorlagan gaplari <u>tugab qoldi</u>, sukunat esa davom etdi. "
                "Bashoratim: <mark>«gaplaridan uzoqroq cho'zildi»</mark>.</p>"
                + why([
                    (True, "outlasted",
                     "«undan uzoqroq davom etdi». Sukunat tayyorlangan jumlalarning "
                     "hammasidan uzun bo'ldi — shuning uchun aytadigan gap qolmadi. "
                     "Oxirgi bo'lak buning isboti."),
                    (False, "echoed",
                     "«aks-sado berdi, takrorladi» — sukunat gaplarni takrorlay "
                     "olmaydi, va bu Azizni gapsiz qoldirmasdi."),
                    (False, "interrupted",
                     "«bo'ldi, to'xtatdi» — vaqt bo'yicha imkonsiz: matn "
                     "<em>silence <u>afterwards</u></em> deydi. Kechikkan narsa "
                     "bo'la olmaydi. <strong>Grammatikasi joyida, mantiqi xato.</strong>"),
                    (False, "improved",
                     "«yaxshiladi» — hikoyaning kayfiyatiga ham, oxirgi bo'lakka ham "
                     "zid."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Bashorat qilmaganda nima bo'ladi</h3>"
            "<p>Yuqoridagi to'rt savolning noto'g'ri variantlarini yana bir marta "
            "ko'zdan kechiring. <em>traditional</em>, <em>collaborative</em>, "
            "<em>increase</em>, <em>interrupted</em> — bularning hammasi "
            "<u>gapga chiroyli o'tiradigan</u> so'zlar. Bashoratsiz o'qiganda ular "
            "«to'g'ridek» tuyuladi.</p>"
            "<p>Bashorat ularni bir zumda ochib tashlaydi: agar sizda tayyor ma'no "
            "bo'lsa, «chiroyli» so'z sizni qiziqtirmaydi — siz faqat "
            "<mark>mos</mark> so'zni qidirayapsiz.</p>"
            + WARN.format(
                "Ikki variant orasida ikkilanib qolsangiz — bu deyarli har doim "
                "bashorat qilmaganingiz belgisi. Variantlarni yana yoping, gapni "
                "qaytadan o'qing va o'z so'zingizni ayting. Shundan keyin ikkitasidan "
                "biri odatda o'z-o'zidan tushib qoladi.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            '<div class="pp-flashcards" data-pp-flashcards>'
            '<div class="pp-card"><div class="pp-card-front">misleading</div><div class="pp-card-back">chalg\'ituvchi, aldamchi</div></div>'
            '<div class="pp-card"><div class="pp-card-front">untenable</div><div class="pp-card-back">saqlab bo\'lmaydigan, chidab bo\'lmas</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to account for</div><div class="pp-card-back">tushuntirib bermoq, izohlamoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to outlast</div><div class="pp-card-back">undan uzoqroq davom etmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">consequential</div><div class="pp-card-back">oqibati katta, muhim</div></div>'
            '<div class="pp-card"><div class="pp-card-front">apparent (solidity)</div><div class="pp-card-back">ko\'rinib turgan, zohiriy (qattiqlik)</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to remain disputed</div><div class="pp-card-back">bahsligicha qolmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to escape attention</div><div class="pp-card-back">e\'tibordan chetda qolmoq</div></div>'
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li><strong>Variantlarni yoping</strong> — ular ma'lumot bermaydi, "
            "chalg'itadi.</li>"
            "<li>Bashorat <u>o'zbekcha</u>, ibora yoki hatto shunchaki «+/−» bo'lishi "
            "mumkin.</li>"
            "<li>Tire, ikki nuqta va nuqtali vergulni qidiring — javob ko'pincha "
            "o'sha yerda qaytarilgan.</li>"
            "<li>Bashorat hech qaysi variantga tushmasa — matnni qayta o'qing, "
            "majburan tanlamang.</li>"
            "<li>Ikki variant orasida ikkilanish = bashorat qilinmagan.</li>"
            "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 12
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_WIC,
    "title": "SAT R&W 12: The Signal Words That Decide the Blank (but, because, although, and)",
    "summary": "Uch oila signal — bir yo'nalish, qarama-qarshilik, sabab-natija — va "
               "tinish belgilari: bo'sh joyning ma'nosini deyarli har doim shular ochadi.",
    "order": 12,
    "blocks": [
        {"rich_text": (
            "<h2>Gapning yo'nalishini ko'rsatadigan so'zlar</h2>"
            "<p>11-darsda bashorat qilishni o'rgandik. Endi savol: bashoratni "
            "<u>nimadan</u> olamiz? Javob deyarli har doim bitta — matndagi "
            "<strong>signal so'zlar</strong>dan.</p>"
            "<p>Signal so'z — gapning yo'nalishini aytadigan kichik so'z: "
            "<em>but</em>, <em>because</em>, <em>although</em>, <em>and</em>. Ular "
            "mavzuni bilishni talab qilmaydi. Termitlar, rif, temir yo'l — farqi yo'q: "
            "<mark><em>but</em> ko'rsangiz, yo'nalish o'zgaradi</mark>, mavzu qanday "
            "bo'lishidan qat'i nazar.</p>"
            '<span class="sr-time">⏱ Signal topilsa: ~25 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Uch oila</h3>"
            '<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">'
            '<summary style="cursor:pointer;font-weight:600;">🟢 Bir yo\'nalish — bo\'sh joy atrofdagi ma\'noni TAKRORLAYDI</summary>'
            "<div style=\"margin-top:10px;\"><p><em>and · also · moreover · furthermore · "
            "indeed · in fact · similarly · likewise · that is · in other words</em></p>"
            "<p>Bu signallardan keyin bo'sh joy oldingi fikrning <u>o'sha tomonida</u> "
            "turadi. Bashorat: yaqin atrofdagi biror so'zning sinonimi.</p></div></details>"
            '<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">'
            '<summary style="cursor:pointer;font-weight:600;">🔴 Qarama-qarshilik — bo\'sh joy ma\'noni AG\'DARADI</summary>'
            "<div style=\"margin-top:10px;\"><p><em>but · however · yet · although · "
            "though · while · whereas · despite · in spite of · nevertheless · "
            "nonetheless · rather than · far from · on the contrary · unlike</em></p>"
            "<p>Bu eng ko'p ishlatiladigan oila. Bashorat: yaqin atrofdagi biror "
            "so'zning <u>antonimi</u>.</p></div></details>"
            '<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">'
            '<summary style="cursor:pointer;font-weight:600;">🔵 Sabab va natija — bo\'sh joy MANTIQIY DAVOMI</summary>'
            "<div style=\"margin-top:10px;\"><p><em>because · since · as · therefore · "
            "thus · so · hence · consequently · as a result · which is why</em></p>"
            "<p>Bashorat: sababdan kelib chiqadigan natija (yoki aksincha). Bu oilada "
            "bo'sh joy ko'pincha «shuning uchun mantiqan shunday bo'ladi» degan "
            "so'zni talab qiladi.</p></div></details>"
            + NOTE.format(
                "Bu ro'yxatlarni <u>yodlash shart emas</u>. Faqat uchta savolni "
                "so'rashni odat qiling: <strong>bir xilmi? qarama-qarshimi? "
                "sabab-natijami?</strong>")
        )},

        {"rich_text": (
            "<h3>Tinish belgilari ham signal</h3>"
            "<p>SAT matnlarida uchta belgi signal so'z bilan bir xil kuchga ega, va "
            "ular ko'pincha e'tibordan chetda qoladi:</p>"
            '<div class="sr-data"><div class="sr-data__scroll">'
            "<table>"
            "<thead><tr><th>Belgi</th><th>Nima deydi</th><th>Bashorat</th></tr></thead>"
            "<tbody>"
            "<tr><td><strong>:</strong> (ikki nuqta)</td><td>«endi tushuntiraman»</td>"
            "<td>Keyingi qism bo'sh joyning ta'rifi</td></tr>"
            "<tr><td><strong>;</strong> (nuqtali vergul)</td><td>«yana o'sha haqda»</td>"
            "<td>Ikki tomon bir xil yo'nalishda (ba'zan qarama-qarshi)</td></tr>"
            "<tr><td><strong>—</strong> (tire)</td><td>«boshqacha aytganda»</td>"
            "<td>Keyingi qism bo'sh joyni qayta aytadi</td></tr>"
            "</tbody></table>"
            "</div></div>"
            + TIP.format(
                "Amaliy tartib: bo'sh joyli savolni ochganingizda ko'zingiz "
                "<u>birinchi navbatda</u> shu belgilarni va signal so'zlarni qidirsin. "
                "Ko'p savolda matnning yarmini o'qimasdanoq bashorat tayyor bo'ladi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + blank_q(
                "<p>For most of the twentieth century, planners treated a city street as "
                "a channel for moving vehicles, and its success was measured in traffic "
                "volume. Recent design guidance reverses the emphasis: it treats the "
                "street as a place where people stop, and measures success by how long "
                "they stay. Far from being a minor adjustment, this is a "
                "<span class=\"sr-blank\"></span> of what a street is for.</p>")
            + "<ol type=\"A\"><li>confirmation</li><li>redefinition</li>"
              "<li>simplification</li><li>postponement</li></ol>"
            "<p><strong>Signalni toping:</strong> <mark><em>Far from being a minor "
            "adjustment</em></mark> — qarama-qarshilik oilasidan, va juda kuchlisi. "
            "«Kichik tuzatish emas» degani — bo'sh joyga <u>kichik tuzatishning "
            "aksi</u> kerak: katta, tubdan o'zgarish.</p>"
            "<p><strong>Ikkinchi isbot:</strong> <em>reverses the emphasis</em> — "
            "«urg'uni teskari qiladi». Bashorat: <mark>«qayta belgilash»</mark>.</p>"
            + why([
                (True, "redefinition",
                 "«qaytadan ta'riflash» — <em>a minor adjustment</em>ning aniq aksi, va "
                 "<em>reverses the emphasis</em> hamda <em>what a street is for</em> "
                 "(ko'chaning maqsadi) buni tasdiqlaydi."),
                (False, "confirmation",
                 "«tasdiq» — teskari yo'nalish. Yangi qo'llanma eski qarashni "
                 "tasdiqlamayapti, uni ag'daryapti."),
                (False, "simplification",
                 "«soddalashtirish» — o'zgarishning <u>kattaligi</u> emas, "
                 "<u>turi</u> haqida, va matn hech qayerda soddalashtirish demaydi. "
                 "Yangi yondashuv soddaroq ham emas."),
                (False, "postponement",
                 "«kechiktirish» — matnda vaqt bo'yicha kechiktirish yo'q. "
                 "<em>Recent</em> so'ziga ilinib qolgan <strong>so'z-tuzoq</strong>."),
            ])
        )},

        {
            "rich_text": blank_q(
                "<p>The Arctic tern breeds close to the North Pole and spends the "
                "northern winter near Antarctica; tracking devices have put the round "
                "trip beyond seventy thousand kilometres in some years. Because the bird "
                "follows looping routes shaped by prevailing winds instead of flying "
                "straight, its actual path is considerably "
                "<span class=\"sr-blank\"></span> than the distance between its two "
                "homes.</p>"),
            "choices": [
                {"text": "longer", "is_correct": True},
                {"text": "shorter", "is_correct": False},
                {"text": "safer", "is_correct": False},
                {"text": "straighter", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Signal:</strong> <mark><em>Because</em></mark> — sabab va "
                "natija oilasi. Sabab: qush to'g'ri emas, <u>halqa</u> bo'lib uchadi. "
                "Natija: bosib o'tgan yo'li ikki nuqta orasidagi masofadan "
                "<mark>uzunroq</mark>.</p>"
                + why([
                    (True, "longer",
                     "«uzunroq» — halqa bo'lib uchish to'g'ri chiziqdan uzun. Sabab "
                     "ergash gapidan bevosita chiqadi."),
                    (False, "shorter",
                     "«qisqaroq» — geometriyaga zid: to'g'ri chiziq eng qisqa yo'l, "
                     "shuning uchun burilishlar yo'lni qisqartira olmaydi."),
                    (False, "safer",
                     "«xavfsizroq» — shamolga ergashish xavfsizroq bo'lishi mumkin, "
                     "va shuning uchun bu variant jozibali. Lekin gap "
                     "<em>its actual <u>path</u> is ___ than the <u>distance</u></em> "
                     "deyapti — bu masofa bilan masofani solishtiryapti, xavf bilan "
                     "emas. <strong>Rost bo'lishi mumkin, lekin so'ralmagan.</strong>"),
                    (False, "straighter",
                     "«to'g'riroq» — matnning o'zi <em>instead of flying straight</em> "
                     "deb rad etadi. Matndagi so'zni qaytarib, ma'nosini ag'daradi."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>Although the printing press is usually credited with spreading new "
                "ideas, its earliest and largest output was thoroughly "
                "<span class=\"sr-blank\"></span> material: indulgences, calendars, "
                "Latin grammars and editions of texts that had circulated in manuscript "
                "for centuries. The novelty lay in the quantity, not in the "
                "content.</p>"),
            "choices": [
                {"text": "conventional", "is_correct": True},
                {"text": "controversial", "is_correct": False},
                {"text": "experimental", "is_correct": False},
                {"text": "illegible", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki signal, bir xil javob.</strong></p>"
                "<p>Birinchisi: <mark><em>Although</em></mark> — qarama-qarshilik. "
                "«Yangi g'oyalar tarqatgan deb hisoblanadi, <u>lekin</u>…» — demak "
                "bo'sh joyga <em>new</em>ning aksi kerak.</p>"
                "<p>Ikkinchisi: oxirgi jumla — <em>The novelty lay in the quantity, not "
                "in the content</em>. Yangilik miqdorda edi, mazmunida emas. "
                "Bashorat: <mark>«eskicha, odatdagi»</mark>.</p>"
                + why([
                    (True, "conventional",
                     "«an'anaviy, odatdagi» — <em>new</em>ning aksi, va ikki nuqtadan "
                     "keyingi ro'yxat (indulgentsiya, taqvim, grammatika) buni "
                     "ko'rsatib turibdi: hammasi allaqachon mavjud bo'lgan janrlar."),
                    (False, "controversial",
                     "«bahsli» — indulgentsiyalar keyinchalik haqiqatan bahsga sabab "
                     "bo'lgan, shuning uchun bu <strong>tashqi bilim</strong> tuzog'i "
                     "kuchli. Lekin matn bahs haqida hech nima demaydi, va bahslilik "
                     "<em>new</em>ning aksi ham emas."),
                    (False, "experimental",
                     "«tajribaviy» — <em>Although</em> talab qilgan yo'nalishga zid: "
                     "bu <em>new</em>ning sinonimi, aksi emas."),
                    (False, "illegible",
                     "«o'qib bo'lmaydigan» — bosma matnning sifati muhokama "
                     "qilinmayapti, va bu oxirgi jumlaga ham to'g'ri kelmaydi."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>The octopus has a talent that its own eyes appear unable to support: "
                "the animal matches the colour of its background almost instantly, yet "
                "its retinas carry only one kind of light-sensitive pigment, which should "
                "make it colour-blind. Researchers have since found pigments of the same "
                "family in the skin itself. The finding does not show that an octopus "
                "sees with its skin, but it makes the animal's colour matching rather "
                "less <span class=\"sr-blank\"></span> than it had seemed.</p>"),
            "choices": [
                {"text": "puzzling", "is_correct": True},
                {"text": "rapid", "is_correct": False},
                {"text": "common", "is_correct": False},
                {"text": "deliberate", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Signal:</strong> <mark><em>but</em></mark> — qarama-qarshilik. "
                "Chap tomon: kashfiyot hamma narsani isbotlamaydi. O'ng tomon: "
                "<u>lekin baribir</u> nimadir yaxshilandi. Nima yaxshilandi? "
                "Matnning boshida qo'yilgan jumboq: ko'zi rangni ajratmaydi-yu, hayvon "
                "rang tanlaydi.</p>"
                "<p>Bashorat: <mark>«sirli emas» tomonga</mark> — <em>less ___</em> "
                "qurilishi bilan birga «avvalgidek tushunarsiz emas» degani.</p>"
                + why([
                    (True, "puzzling",
                     "«hayron qoldiradigan, tushunarsiz» — birinchi jumladagi "
                     "<em>a talent that its own eyes appear unable to support</em> "
                     "aynan jumboqni qo'yadi, kashfiyot esa uni yumshatadi."),
                    (False, "rapid",
                     "«tez» — matndagi <em>almost instantly</em> so'zidan ilingan. "
                     "Lekin teri pigmentlari topilgani hayvonning <u>tezligini</u> "
                     "kamaytirmaydi — bu mantiqiy bo'lmagan gap."),
                    (False, "common",
                     "«keng tarqalgan» — kashfiyot boshqa hayvonlarni muhokama "
                     "qilmaydi, shuning uchun «kamroq uchraydigan bo'lib qoldi» "
                     "degan ma'no matndan chiqmaydi."),
                    (False, "deliberate",
                     "«ataylab qilingan» — jozibali, chunki ilmiy matnlar ba'zan "
                     "ixtiyoriylikni muhokama qiladi. Lekin bu matn hayvonning "
                     "niyati haqida emas, <u>mexanizmi</u> haqida."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>A census counts people, but it also creates categories; the boxes it "
                "offers <span class=\"sr-blank\"></span> the population it claims merely "
                "to describe. When a national form first added a box for people of more "
                "than one background, the number of such people did not suddenly rise. "
                "The number who could say so did.</p>"),
            "choices": [
                {"text": "shape", "is_correct": True},
                {"text": "undercount", "is_correct": False},
                {"text": "ignore", "is_correct": False},
                {"text": "verify", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Signal:</strong> nuqtali vergul (<em>;</em>) — o'ng tomon "
                "chap tomonni boshqa so'zlar bilan qaytaradi. Chap tomon: sanoq "
                "<em>creates categories</em> — kategoriyalarni <u>yaratadi</u>. Demak "
                "bo'sh joyga «yaratish/o'zgartirish» oilasidan so'z kerak.</p>"
                "<p><strong>Ikkinchi signal:</strong> <em>claims <u>merely</u> to "
                "describe</em> — «faqat tasvirlayman deb da'vo qiladi». <em>merely</em> "
                "bu yerda kinoya: demak aslida tasvirlashdan <u>ko'proq</u> qiladi.</p>"
                + why([
                    (True, "shape",
                     "«shakllantiradi, ko'rinishini belgilaydi» — <em>creates "
                     "categories</em>ning takrori, va oxirgi ikki jumla misol bo'lib "
                     "turibdi: katakcha qo'shilgach, odamlar soni emas, "
                     "<u>o'zini shunday atay oladiganlar</u> soni o'zgardi."),
                    (False, "undercount",
                     "«kam sanaydi» — jozibali, chunki misolda raqam o'zgaryapti. "
                     "Lekin matn <em>the number of such people did not suddenly "
                     "rise</em> deb aniq aytadi: bu kam sanash haqidagi hikoya emas, "
                     "kategoriyaning odamni <u>yaratishi</u> haqidagi hikoya."),
                    (False, "ignore",
                     "«e'tiborsiz qoldiradi» — <em>creates categories</em>ga zid va "
                     "misolga ham to'g'ri kelmaydi: forma katakcha qo'shdi, "
                     "e'tiborsiz qoldirmadi."),
                    (False, "verify",
                     "«tasdiqlaydi, tekshiradi» — <em>merely to describe</em> bilan "
                     "bir tomonda turadi, ya'ni kinoyaning yo'nalishiga zid."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>Malika's teacher returned the essay with a single line at the bottom, "
                "and Malika read it four times before she understood that it was praise. "
                "The remark noted, rather than corrected, the place where the argument "
                "had <span class=\"sr-blank\"></span>: the teacher had seen the gap and "
                "left it there, as an invitation.</p>"),
            "choices": [
                {"text": "faltered", "is_correct": True},
                {"text": "concluded", "is_correct": False},
                {"text": "improved", "is_correct": False},
                {"text": "begun", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Signal:</strong> ikki nuqta (<em>:</em>) — keyingi qism "
                "bo'sh joyni izohlaydi, va u bitta so'z sovg'a qiladi: "
                "<mark><em>the gap</em></mark>. Bo'sh joy «bo'shliq paydo bo'lgan joy» "
                "degan ma'noni talab qilyapti.</p>"
                + why([
                    (True, "faltered",
                     "«oqsadi, uzilib qoldi». <em>the gap</em> — dalilning uzilgan "
                     "joyi. Ikki nuqtadan keyingi izoh boshqa hech qanday variantga "
                     "to'g'ri kelmaydi."),
                    (False, "concluded",
                     "«yakunlandi» — dalilning tugagan joyi bo'shliq emas. Va o'qituvchi "
                     "xulosani «taklif» sifatida qoldirmaydi."),
                    (False, "improved",
                     "«yaxshilandi» — matn maqtov haqida (<em>it was praise</em>), "
                     "shuning uchun bu variant jozibali. Lekin maqtov o'qituvchining "
                     "<u>usuliga</u> tegishli, dalilning o'sha joyiga emas: "
                     "bo'shliq bor joy yaxshilangan joy emas."),
                    (False, "begun",
                     "«boshlandi» — dalil boshlangan joyda bo'shliq bo'lmaydi, va "
                     "bu «taklif» tasviriga hech qanday ma'no bermaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Signalni topolmaganda</h3>"
            "<p>Ba'zan gapda ochiq signal so'z ham, foydali tinish belgisi ham "
            "bo'lmaydi. Bunday holatda ikkita zaxira usul bor:</p>"
            "<ul>"
            "<li><strong>Ma'no takrorini qidiring.</strong> SAT matnlari qisqa, shuning "
            "uchun ular fikrni boshqa so'zlar bilan takrorlashga majbur. Bo'sh joyning "
            "javobi ko'pincha matnning boshqa joyida boshqa ibora bilan aytilgan.</li>"
            "<li><strong>Faqat «+» yoki «−» ni aniqlang.</strong> Bo'sh joyga ijobiy "
            "ma'no kerakmi yoki salbiy? Bu ko'pincha ikki variantni darrov "
            "o'chiradi, qolgan ikkitasini esa sinchiklab solishtirasiz.</li>"
            "</ul>"
            + WARN.format(
                "<em>and</em> har doim ham «bir yo'nalish» degani emas: "
                "<em>simple and effective</em> — bir yo'nalish, lekin "
                "<em>cheap and yet durable</em> da <em>yet</em> yo'nalishni buradi. "
                "Signal so'zni <u>ko'rish</u> kifoya emas — u qaysi ikki fikrni "
                "bog'layotganini tekshiring.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            '<div class="pp-flashcards" data-pp-flashcards>'
            '<div class="pp-card"><div class="pp-card-front">far from ~</div><div class="pp-card-back">~ o\'rniga, aksincha (kuchli qarshilik signali)</div></div>'
            '<div class="pp-card"><div class="pp-card-front">rather than</div><div class="pp-card-back">~ emas, balki (qarshilik signali)</div></div>'
            '<div class="pp-card"><div class="pp-card-front">merely</div><div class="pp-card-back">faqatgina, shunchaki</div></div>'
            '<div class="pp-card"><div class="pp-card-front">conventional</div><div class="pp-card-back">an\'anaviy, odatdagi</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to falter</div><div class="pp-card-back">oqsamoq, uzilib qolmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">puzzling</div><div class="pp-card-back">hayron qoldiradigan, tushunarsiz</div></div>'
            '<div class="pp-card"><div class="pp-card-front">prevailing winds</div><div class="pp-card-back">hukmron shamollar</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to reverse the emphasis</div><div class="pp-card-back">urg\'uni teskari qilmoq</div></div>'
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Uch savol: <strong>bir xilmi? qarama-qarshimi? sabab-natijami?</strong></li>"
            "<li><em>but · however · although · yet · rather than · far from</em> — "
            "yo'nalishni ag'daradi.</li>"
            "<li><em>because · therefore · thus · as a result</em> — mantiqiy davomini "
            "talab qiladi.</li>"
            "<li><strong>:</strong> tushuntiradi · <strong>;</strong> davom ettiradi · "
            "<strong>—</strong> qayta aytadi.</li>"
            "<li>Signal yo'q bo'lsa: ma'no takrorini qidiring yoki faqat «+/−» ni "
            "aniqlang.</li>"
            "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 13
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_WIC,
    "title": "SAT R&W 13: “Most Nearly Means” — Common Words With Uncommon Uses",
    "summary": "Bu shaklda SAT noyob so'zlarni emas, oddiy so'zlarning kam uchraydigan "
               "ma'nolarini tekshiradi; tuzoq har doim so'zning eng mashhur ma'nosi.",
    "order": 13,
    "blocks": [
        {"rich_text": (
            "<h2>Tanish so'z, notanish ma'no</h2>"
            "<p><em>As used in the text, what does the word “X” most nearly mean?</em> — "
            "Words in Context'ning ikkinchi shakli. Bu yerda bitta qonuniyat bor va u "
            "deyarli hech qachon buzilmaydi:</p>"
            + EXAMP.format(
                "<p style=\"font-size:1.08em;margin:0;\"><strong>Tagi chizilgan so'z "
                "deyarli har doim siz biladigan oddiy so'z bo'ladi</strong> — "
                "<em>sound</em>, <em>reserved</em>, <em>bound</em>, <em>figure</em>, "
                "<em>qualify</em>, <em>hard</em>. Qiyinlik so'zda emas: "
                "so'z bu gapda <u>odatdagidan boshqa</u> ma'noda ishlatilgan.</p>")
            + "<p>Va to'rtta variantning ichida <mark>so'zning eng mashhur ma'nosi har "
            "doim bor</mark> — u aynan siz uchun qo'yilgan.</p>"
            '<span class="sr-time">⏱ Maqsad: ~35 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Usul — uch qadam</h3>"
            '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            "<div class=\"pp-step\"><p><strong>1. So'zni gapdan olib tashlang.</strong> "
            "Uning o'rniga bo'shliq qo'ying va o'zingizga ayting: shu bo'shliqqa qanday "
            "ma'no kerak? Ya'ni bu shaklni <u>1-shaklga aylantiring</u> — 11-darsda "
            "o'rgangan bashorat usuli o'shanda ishlay boshlaydi.</p></div>"
            "<div class=\"pp-step\"><p><strong>2. So'zning mashhur ma'nosini "
            "ataylab bir chetga suring.</strong> «Bu so'z odatda nimani anglatadi?» "
            "degan savol bu yerda sizga <u>qarshi</u> ishlaydi. Yagona savol: "
            "shu gapda nima ishlayapti?</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Har variantni gapga qo'yib o'qing.</strong> "
            "Bir necha so'zni emas — <u>butun gapni</u>. Noto'g'ri variantlar "
            "ko'pincha gapni grammatik jihatdan ham buzadi: <em>reserve X <u>to</u> Y</em> "
            "bo'ladi, lekin <em>protect X <u>to</u> Y</em> bo'lmaydi.</p></div>"
            "</div>"
            + TIP.format(
                "3-qadamdagi predlog hiylasi juda foydali: ingliz tilida ko'p fe'l "
                "o'z predlogini «olib yuradi». Agar variantni qo'yganingizda predlog "
                "g'alati eshitilsa — bu variant deyarli har doim noto'g'ri.")
        )},

        {"rich_text": (
            "<h3>SAT eng ko'p sinaydigan so'zlar</h3>"
            "<p>Bularni yodlash shart emas, lekin <u>ikkinchi ma'nosi borligini</u> "
            "bilib qo'yish foydali:</p>"
            '<div class="sr-data"><div class="sr-data__scroll">'
            "<table>"
            "<thead><tr><th>So'z</th><th>Mashhur ma'no (tuzoq)</th><th>SAT sevadigan ma'no</th></tr></thead>"
            "<tbody>"
            "<tr><td>sound</td><td>ovoz</td><td>sog'lom, buzilmagan, ishonchli</td></tr>"
            "<tr><td>reserved</td><td>kamgap</td><td>ajratib qo'yilgan, cheklangan</td></tr>"
            "<tr><td>bound</td><td>sakramoq</td><td>bog'langan, cheklangan</td></tr>"
            "<tr><td>figure</td><td>shakl, gavda</td><td>raqam, ko'rsatkich</td></tr>"
            "<tr><td>qualify</td><td>huquq bermoq</td><td>cheklamoq, aniqlashtirmoq</td></tr>"
            "<tr><td>novel</td><td>roman</td><td>yangi, ilgari bo'lmagan</td></tr>"
            "<tr><td>arrest</td><td>hibsga olmoq</td><td>to'xtatmoq</td></tr>"
            "<tr><td>address</td><td>manzil</td><td>(masalaga) murojaat qilmoq, hal qilmoq</td></tr>"
            "<tr><td>yield</td><td>yon bermoq</td><td>hosil bermoq, natija bermoq</td></tr>"
            "<tr><td>sustain</td><td>quvvatlamoq</td><td>davom ettirmoq, ko'tarib turmoq</td></tr>"
            "<tr><td>credit</td><td>kredit</td><td>ishonmoq; (kashfiyotni) kimgadir bog'lamoq</td></tr>"
            "<tr><td>appreciate</td><td>qadrlamoq</td><td>tushunib yetmoq; qiymati oshmoq</td></tr>"
            "</tbody></table>"
            "</div></div>"
            + NOTE.format(
                "Bu jadval «javoblar ro'yxati» emas. U faqat bitta odatni "
                "o'rnatish uchun: tagi chizilgan so'zni ko'rganda "
                "<u>«men bu so'zni bilaman»</u> degan hisni to'xtating — aynan o'sha "
                "his sizni tuzoqqa olib boradi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + means_q(
                "<p>The city's early charters <span class=\"sr-focus\">reserved</span> "
                "the right to hold a market to a handful of families, and for two "
                "centuries no one else could lawfully sell grain inside the walls. The "
                "monopoly ended not by decree but by neglect: the families died out, and "
                "the restriction was simply never enforced again.</p>", "reserved")
            + "<ol type=\"A\"><li>postponed</li><li>restricted</li><li>protected</li>"
              "<li>doubted</li></ol>"
            "<p><strong>1-qadam.</strong> So'zni olib tashlaymiz: <em>the charters ___ "
            "the right to hold a market <u>to</u> a handful of families</em>. Bo'shliqqa "
            "qanday ma'no kerak? Keyingi jumla aytadi: <em>no one else could lawfully "
            "sell grain</em> — <mark>faqat o'sha oilalarga ruxsat, boshqalarga "
            "yo'q</mark>.</p>"
            "<p><strong>2-qadam.</strong> <em>reserved</em>ning mashhur ma'nosi — "
            "«kamgap, o'ziga yopiq odam». Uni bir chetga suramiz: bu yerda odam emas, "
            "hujjat gapiryapti.</p>"
            "<p><strong>3-qadam.</strong> Har variantni predlog bilan birga sinaymiz.</p>"
            + why([
                (True, "restricted",
                 "«chekladi, faqat shularga qoldirdi». <em>restrict X <u>to</u> Y</em> "
                 "— predlog joyida, va keyingi jumla («boshqa hech kim sotolmasdi») "
                 "bu ma'noning to'g'ridan-to'g'ri isboti."),
                (False, "protected",
                 "«himoya qildi» — eng kuchli tuzoq, chunki nizom haqiqatan o'sha "
                 "oilalarning manfaatini himoya qilgan. Lekin gapni to'liq o'qing: "
                 "<em>protected the right … <u>to</u> a handful of families</em> — "
                 "predlog buziladi. Ingliz tilida «kimnidir himoya qilish» "
                 "<em>protect <u>for</u></em> yoki predlogsiz bo'ladi. "
                 "<strong>Rost bo'lishi mumkin, lekin so'ralmagan — va grammatikasi "
                 "ham sotib qo'yadi.</strong>"),
                (False, "postponed",
                 "«kechiktirdi» — vaqt ma'nosi. Nizom bozor huquqini kechiktirmagan, "
                 "u kimga tegishli ekanini belgilagan."),
                (False, "doubted",
                 "«shubhalandi» — hujjat shubhalanmaydi, va matnda hech qanday "
                 "ishonchsizlik yo'q."),
            ])
        )},

        {
            "rich_text": means_q(
                "<p>The engineer worked along the length of the old beam, tapping it "
                "every few centimetres and listening. A hollow note meant rot somewhere "
                "beneath the surface. A <span class=\"sr-focus\">sound</span> beam "
                "answered with a short, dense knock that he said could be felt in the "
                "wrist as much as heard.</p>", "sound"),
            "choices": [
                {"text": "undamaged", "is_correct": True},
                {"text": "audible", "is_correct": False},
                {"text": "loud", "is_correct": False},
                {"text": "sensible", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>1-qadam.</strong> <em>A ___ beam answered with a short, "
                "dense knock</em>. Undan oldingi jumla juftlikni beradi: "
                "<em>A hollow note meant <u>rot</u></em> — bo'sh ovoz chirishni "
                "bildiradi. Demak bu jumla <mark>qarama-qarshi holatni</mark> "
                "tasvirlayapti: chirimagan, sog'lom yog'och.</p>"
                "<p><strong>2-qadam.</strong> <em>sound</em> = «ovoz» degan ma'no "
                "shu qadar kuchliki, matn ham ovoz haqida — bu SAT'ning eng ustalik "
                "bilan qo'yilgan tuzoqlaridan biri. Ataylab bir chetga suramiz.</p>"
                + why([
                    (True, "undamaged",
                     "«shikastlanmagan, sog'lom» — <em>sound</em> sifatining aynan shu "
                     "ma'nosi (<em>a sound structure</em>, <em>safe and sound</em>). "
                     "Isbot — oldingi jumladagi <em>rot</em> bilan qarama-qarshilik."),
                    (False, "audible",
                     "«eshitiladigan» — matn ovoz haqida bo'lgani uchun juda jozibali. "
                     "Lekin mantiqan bema'ni: chirigan yog'och ham ovoz chiqaradi "
                     "(<em>a hollow note</em>). «Eshitiladigan to'sin» hech nimani "
                     "ajratmaydi."),
                    (False, "loud",
                     "«baland ovozli» — matn aksincha, <em>short, dense</em> deydi va "
                     "ovozning balandligini emas, sifatini tasvirlaydi."),
                    (False, "sensible",
                     "«oqilona» — <em>sound</em>ning yana bir real ma'nosi "
                     "(<em>sound advice</em> = oqilona maslahat), lekin u odamlar va "
                     "fikrlar haqida. To'sin oqilona bo'lolmaydi."),
                ])
                + TIP.format(
                    "E'tibor bering: to'rtta variantning uchtasi <em>sound</em>ning "
                    "<u>haqiqiy</u> ma'nolari edi. SAT «noto'g'ri ma'no» "
                    "o'ylab topmaydi — u so'zning boshqa rost ma'nolarini qo'yadi. "
                    "Shuning uchun «bu ma'no bormi?» deb so'rash foydasiz; "
                    "«<u>shu gapda</u> qaysi ma'no ishlayapti?» deb so'rash kerak.")
            ),
        },

        {
            "rich_text": means_q(
                "<p>Early attempts to date archaeological timber by counting growth rings "
                "went wrong whenever a sample came from a species that does not lay down "
                "exactly one ring a year. Dendrochronologists now "
                "<span class=\"sr-focus\">qualify</span> their results accordingly: a "
                "date is published as a range rather than a single year, and the species "
                "is named beside it.</p>", "qualify"),
            "choices": [
                {"text": "limit", "is_correct": True},
                {"text": "certify", "is_correct": False},
                {"text": "explain", "is_correct": False},
                {"text": "translate", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>1-qadam.</strong> Ikki nuqtadan keyingi qism — bu so'zning "
                "izohi: <em>a date is published as a <u>range</u> rather than a single "
                "year</em>. Aniq yil o'rniga oraliq berish — bu da'voni "
                "<mark>kuchsizlantirish, chegaralab qo'yish</mark>.</p>"
                "<p><strong>2-qadam.</strong> <em>qualify</em>ning mashhur ma'nosi — "
                "«huquq bermoq, malakaga ega bo'lmoq» (<em>to qualify for a "
                "scholarship</em>). Bu yerda u ishlamaydi.</p>"
                + why([
                    (True, "limit",
                     "«cheklamoq, chegara qo'ymoq» — <em>to qualify a statement</em> "
                     "aynan shu: da'voni ehtiyotkorroq qilish. Ikki nuqtadan keyingi "
                     "misol boshqa hech qanday ma'noga to'g'ri kelmaydi."),
                    (False, "certify",
                     "«rasman tasdiqlamoq» — <em>qualify</em>ning mashhur ma'nosiga "
                     "eng yaqin variant, va shuning uchun eng ko'p tanlanadi. Lekin "
                     "mantiqni teskari qiladi: natijani tasdiqlash uni "
                     "<u>kuchaytiradi</u>, matn esa uni kuchsizlantirishni "
                     "tasvirlayapti."),
                    (False, "explain",
                     "«tushuntirmoq» — olimlar sababni birinchi jumlada tushuntirgan, "
                     "lekin <em>qualify</em> fe'lining ob'ekti <em>their results</em>. "
                     "Natijani tushuntirish emas, uni chegaralash muhokama qilinyapti."),
                    (False, "translate",
                     "«tarjima qilmoq» — matnda til ham, o'girish ham yo'q."),
                ])
            ),
        },

        {
            "rich_text": means_q(
                "<p>A jazz soloist who repeats a phrase exactly has usually made a "
                "mistake; one who repeats it a step higher has made a decision. What "
                "sounds to an outsider like pure spontaneity is "
                "<span class=\"sr-focus\">bound</span> by conventions as strict as those "
                "of any written form: which chords may be implied, when a chorus ends, "
                "how one phrase answers the phrase before it.</p>", "bound"),
            "choices": [
                {"text": "constrained", "is_correct": True},
                {"text": "leaping", "is_correct": False},
                {"text": "headed", "is_correct": False},
                {"text": "certain", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>1-qadam.</strong> Ikki nuqtadan keyingi ro'yxat — qoidalar "
                "ro'yxati. Va ulardan oldin <em>conventions as strict as those of any "
                "written form</em> turibdi. Demak improvizatsiya <mark>qoidalar bilan "
                "chegaralangan</mark>.</p>"
                "<p><strong>2-qadam.</strong> <em>bound</em> — ingliz tilidagi eng "
                "ko'p ma'noli so'zlardan biri, va bu yerda uchta boshqa ma'nosi variant "
                "sifatida qo'yilgan.</p>"
                + why([
                    (True, "constrained",
                     "«chegaralangan» — <em>bound by rules / bound by convention</em> "
                     "iborasining ma'nosi. Ikki nuqtadan keyingi qoidalar ro'yxati "
                     "bevosita isbot."),
                    (False, "leaping",
                     "«sakrayotgan» — <em>bound</em> fe'lining «sakramoq» ma'nosi "
                     "(<em>the deer bounded away</em>). Musiqa mavzusi «sakrash»ni "
                     "ishonarli qiladi, lekin <em>bound <u>by</u> conventions</em> "
                     "qurilishiga umuman tushmaydi."),
                    (False, "headed",
                     "«yo'l olgan» — <em>bound for London</em> iborasidagi ma'no. "
                     "Predlog buzadi: <em>bound <u>for</u></em> bo'ladi, "
                     "<em>bound <u>by</u></em> emas."),
                    (False, "certain",
                     "«albatta bo'ladigan» — <em>bound to happen</em> iborasidan. "
                     "Bu ma'no <em>to</em> + fe'l talab qiladi, bu yerda esa "
                     "<em>by</em> + ot bor."),
                ])
            ),
        },

        {
            "rich_text": means_q(
                "<p>Her father had a way of receiving news that gave nothing away. When "
                "Nodira told him she had been offered the place in Tashkent, he set down "
                "his cup, looked at the window for a while, and said only that the "
                "winters there were <span class=\"sr-focus\">hard</span>. It was three "
                "days before she learned, from her mother, that he had told everyone in "
                "the mahalla.</p>", "hard"),
            "choices": [
                {"text": "severe", "is_correct": True},
                {"text": "solid", "is_correct": False},
                {"text": "confusing", "is_correct": False},
                {"text": "unfair", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>1-qadam.</strong> <em>the winters there were ___</em>. "
                "Qish haqida gap ketyapti, va ota qizini ogohlantiryapti (o'z uslubida). "
                "Bashorat: <mark>«qattiq, og'ir»</mark>.</p>"
                + why([
                    (True, "severe",
                     "«qattiq, shafqatsiz» — ob-havo haqida gapirganda "
                     "<em>hard</em>ning aynan shu ma'nosi ishlaydi "
                     "(<em>a hard winter</em>)."),
                    (False, "solid",
                     "«qattiq (jismonan)» — <em>hard</em>ning eng birinchi lug'aviy "
                     "ma'nosi, va shuning uchun tuzoq. Lekin qish jismonan qattiq "
                     "bo'lolmaydi — bu sifat toshga, muzga tegishli, faslga emas."),
                    (False, "confusing",
                     "«tushunish qiyin» — <em>a hard question</em> ma'nosi. Real, "
                     "lekin qish tushunarli yoki tushunarsiz bo'lmaydi."),
                    (False, "unfair",
                     "«adolatsiz» — <em>hard on someone</em> iborasiga yaqin ma'no. "
                     "Bu yerda esa <em>hard</em> qishning o'z xususiyatini "
                     "ta'riflayapti, kimgadir munosabatini emas."),
                ])
                + NOTE.format(
                    "Adabiy parchalarda <em>most nearly means</em> savoli ko'pincha "
                    "juda oddiy so'z ustida quriladi. Matnning hissiy ohangi "
                    "sizni chalg'itmasin: ota o'z sevgisini yashiryapti, lekin savol "
                    "faqat <em>hard</em> so'zining <u>qishga</u> nisbatan ma'nosini "
                    "so'rayapti.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            '<div class="pp-flashcards" data-pp-flashcards>'
            '<div class="pp-card"><div class="pp-card-front">sound (adj.)</div><div class="pp-card-back">sog\'lom, buzilmagan; oqilona</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to reserve X to Y</div><div class="pp-card-back">X ni faqat Y ga qoldirmoq, cheklamoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to qualify (a claim)</div><div class="pp-card-back">(da\'voni) chegaralamoq, ehtiyotkor qilmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">bound by ~</div><div class="pp-card-back">~ bilan chegaralangan, bog\'langan</div></div>'
            '<div class="pp-card"><div class="pp-card-front">a hard winter</div><div class="pp-card-back">qattiq, og\'ir qish</div></div>'
            '<div class="pp-card"><div class="pp-card-front">spontaneity</div><div class="pp-card-back">o\'z-o\'zidan, tayyorgarliksiz paydo bo\'lish</div></div>'
            '<div class="pp-card"><div class="pp-card-front">a monopoly</div><div class="pp-card-back">yakka hukmronlik, monopoliya</div></div>'
            '<div class="pp-card"><div class="pp-card-front">by neglect</div><div class="pp-card-back">e\'tiborsizlik tufayli (o\'z-o\'zidan)</div></div>'
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Tagi chizilgan so'z <strong>oddiy so'z</strong> bo'ladi — qiyinligi "
            "uning kutilmagan ma'nosida.</li>"
            "<li>So'zni <u>olib tashlang</u> va bo'shliqqa bashorat qiling — shunda bu "
            "shakl 1-shaklga aylanadi.</li>"
            "<li>Variantlarning uchtasi ham so'zning <strong>rost</strong> ma'nolari "
            "bo'ladi; savol «bu ma'no bormi?» emas, «shu gapda qaysi ishlayapti?»</li>"
            "<li>Har variantni <u>butun gapga</u> qo'yib o'qing — predlog ko'pincha "
            "javobni ochib beradi.</li>"
            "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 14
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_WIC,
    "title": "SAT R&W 14: The Vocabulary Trap — The Impressive Word Is Bait, Not a Signal",
    "summary": "So'zni ta'sirli ko'ringani uchun tanlash ham, rad etish ham xato: "
               "qaysi variant qiyin ekani hech nimani bildirmaydi, faqat gap hal qiladi.",
    "order": 14,
    "blocks": [
        {"rich_text": (
            "<h2>Qiyin so'z — belgi emas, tuzoq</h2>"
            "<p>Ko'p o'quvchida bir xil odat bor: to'rtta variantdan eng "
            "<u>ilmiy eshitiladiganini</u> tanlash. Mantiq shunday: «SAT qiyin imtihon, "
            "demak javob ham qiyin so'z bo'lsa kerak».</p>"
            "<p>Bu odatni SAT tuzuvchilari juda yaxshi biladi va undan <strong>foydalanadi</strong> "
            "— chalg'ituvchi variantlar ataylab ta'sirli qilib tanlanadi.</p>"
            "<p>Lekin teskari odat ham xuddi shunday xato: «qiyin so'z — demak tuzoq, uni "
            "tashlayman». Ba'zan javob <u>aynan</u> eng qiyin so'z bo'ladi.</p>"
            + EXAMP.format(
                "<p style=\"font-size:1.08em;margin:0;\"><strong>Halol qoida:</strong> "
                "so'zni <u>ta'sirli ko'ringani uchun tanlamang</u> va "
                "<u>ta'sirli ko'ringani uchun rad etmang</u>. Variantning qiyinligi "
                "hech qanday ma'lumot bermaydi. Faqat gap hal qiladi.</p>")
            + '<span class="sr-time">⏱ ~40 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Nega qiyinlik ma'lumot bermaydi</h3>"
            "<p>Buni tekshirish oson. SAT'ning bo'sh joyli savollarida to'rtta variant "
            "odatda <mark>bir xil qiyinlik darajasida</mark> bo'ladi — hammasi "
            "o'rta-akademik ingliz tili. Ular orasidan «eng qiyinini» tanlash "
            "tanga tashlashdan farq qilmaydi.</p>"
            "<p>Va shuni ham unutmang: <em>most logical and <strong>precise</strong></em> "
            "— savolning o'zi «aniq» so'zni so'rayapti. Aniqlik bilan ta'sirlilik "
            "bir narsa emas. Ko'pincha eng aniq so'z — eng sodda so'z.</p>"
            '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            "<div class=\"pp-step\"><p><strong>Almashtirish sinovi.</strong> Har "
            "variantni gapga qo'ying va butun gapni o'qing. Noto'g'ri variant "
            "gapni <u>matn aytmagan narsaga</u> aylantiradi — buni ovoz chiqarib "
            "o'qiganda darrov sezasiz.</p></div>"
            "<div class=\"pp-step\"><p><strong>«Bu matnda aytilganmi?» sinovi.</strong> "
            "Variantni tanlaganingizdan keyin so'rang: matnning qaysi so'zlari buni "
            "isbotlaydi? Ta'sirli so'zlar ko'pincha shu savolda qulaydi — "
            "ular chiroyli, lekin isbotsiz.</p></div>"
            "<div class=\"pp-step\"><p><strong>Ikki yaqin variant qolganda.</strong> "
            "Ular deyarli sinonim bo'lsa, farqni qidiring: biri kuchliroqmi? biri "
            "baho beryaptimi? biri sababni nazarda tutyaptimi? Matn qaysinisini "
            "<u>ko'taradi</u>?</p></div>"
            "</div>"
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + blank_q(
                "<p>The seed vault cut into a mountainside inside the Arctic Circle holds "
                "duplicates of samples that are kept in national collections elsewhere. "
                "It is not a library that researchers visit; it is a backup, opened only "
                "when a collection somewhere else has been damaged or lost. Its designers "
                "therefore treated <span class=\"sr-blank\"></span> rather than access as "
                "the governing problem, and the door is opened as seldom as it can "
                "be.</p>")
            + "<ol type=\"A\"><li>secrecy</li><li>preservation</li><li>ownership</li>"
              "<li>transport</li></ol>"
            "<p><strong>Signal:</strong> <em>rather than access</em> — qarama-qarshilik. "
            "Bo'sh joyga <u>kirish imkoniyatining aksi</u> kerak. Va oxirgi bo'lak "
            "buni takrorlaydi: <em>the door is opened as seldom as it can be</em>.</p>"
            "<p><strong>Bashorat:</strong> <mark>«saqlash»</mark> — eshikni yopiq "
            "tutishning sababi.</p>"
            + why([
                (True, "preservation",
                 "«saqlab qolish» — <em>access</em>ning aksi va omborning butun "
                 "maqsadi (<em>it is a backup</em>). Eng sodda so'z, va eng aniq."),
                (False, "secrecy",
                 "«maxfiylik» — eng «jiddiy» eshitiladigan variant, va aynan shuning "
                 "uchun qo'yilgan. Lekin maxfiylik <em>access</em>ning aksi emas: "
                 "ombor yashirin emas, shunchaki kamdan-kam ochiladi. "
                 "Matnda sir haqida bir og'iz ham yo'q."),
                (False, "ownership",
                 "«egalik» — namunalar boshqa mamlakatlarga tegishli ekani "
                 "matndan sezilib turibdi (<em>national collections</em>), shuning "
                 "uchun bu <strong>tashqi bilim</strong> tuzog'i kuchli. Lekin egalik "
                 "eshikning kamdan-kam ochilishini tushuntirmaydi."),
                (False, "transport",
                 "«tashish» — namunalarni olib kelish kerak bo'lgan, bu rost. Lekin "
                 "matn transportni umuman muhokama qilmaydi va u ham "
                 "<em>access</em>ning aksi emas."),
            ])
        )},

        {
            "rich_text": blank_q(
                "<p>A translator working from a language that marks no future tense must "
                "decide, sentence by sentence, how much certainty the original implied. "
                "Two translations of one paragraph may both be defensible and still leave "
                "a reader with different impressions of how confident the speaker was. "
                "The difficulty is not that the translator has too little information "
                "about the language; it is that the original is genuinely "
                "<span class=\"sr-blank\"></span>.</p>"),
            "choices": [
                {"text": "ambiguous", "is_correct": True},
                {"text": "archaic", "is_correct": False},
                {"text": "careless", "is_correct": False},
                {"text": "untranslated", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Signal:</strong> nuqtali vergul va <em>not … it is that …</em> "
                "qurilishi. Chap tomon rad etilyapti (ma'lumot yetishmasligi), o'ng "
                "tomonda esa haqiqiy sabab. Haqiqiy sabab nima? Ikkinchi jumla: "
                "<em>both be defensible … different impressions</em> — "
                "<mark>asl matnning o'zi ikki xil o'qishga ochiq</mark>.</p>"
                + why([
                    (True, "ambiguous",
                     "«ikki ma'noli, noaniq» — <em>both defensible / different "
                     "impressions</em> ta'rifining aynan o'zi. Bu javob sodda ham, "
                     "qiyin ham emas — u shunchaki to'g'ri."),
                    (False, "archaic",
                     "«eskirgan» — eng «akademik» eshitiladigan variant. Lekin matn "
                     "tilning yoshi haqida hech nima demaydi: kelasi zamon shakli "
                     "yo'qligi eskilik emas, tuzilish xususiyati."),
                    (False, "careless",
                     "«beparvo» — asl muallifni ayblaydi, matn esa hech kimni "
                     "ayblamaydi. Aksincha, <em>genuinely</em> so'zi bu holat "
                     "kamchilik emas, xususiyat ekanini bildiryapti."),
                    (False, "untranslated",
                     "«tarjima qilinmagan» — matnning o'zi ikki tarjimadan gapiryapti, "
                     "demak tarjima qilingan. <strong>So'z-tuzoq</strong>: "
                     "<em>translator</em>, <em>translations</em> so'zlariga yopishadi."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>A compound that clears a disease in mice and fails in people has not "
                "necessarily been tested badly. Laboratory mice are bred for uniformity, "
                "and they respond uniformly; a human population does not. A result that "
                "holds across a genetically identical colony may simply not "
                "<span class=\"sr-blank\"></span> to a group that varies in a thousand "
                "ways at once.</p>"),
            "choices": [
                {"text": "generalise", "is_correct": True},
                {"text": "appeal", "is_correct": False},
                {"text": "belong", "is_correct": False},
                {"text": "submit", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu savol darsning ikkinchi yarmini isbotlaydi: <mark>bu yerda "
                "javob — eng qiyin so'z</mark>. Agar siz «qiyin so'z = tuzoq» qoidasi "
                "bilan ishlasangiz, aynan shu savolni yo'qotasiz.</p>"
                "<p><strong>Mantiq:</strong> bir xil sichqonlarda ishlagan natija "
                "har xil odamlarga <u>ko'chmasligi</u> mumkin. Bashorat: "
                "«kengroq guruhga tarqalmoq».</p>"
                + why([
                    (True, "generalise",
                     "«umumlashmoq, kengroq guruhga tatbiq bo'lmoq» — ilmiy matnning "
                     "aniq atamasi va gapning aniq ma'nosi. "
                     "<em>generalise <u>to</u> a group</em> — predlog ham joyida."),
                    (False, "appeal",
                     "«yoqmoq, murojaat qilmoq» — natija guruhga «yoqmaydi». Bu odamlar "
                     "didi haqida, ilmiy tatbiq haqida emas."),
                    (False, "belong",
                     "«tegishli bo'lmoq» — grammatik jihatdan <em>belong to</em> "
                     "joyiga tushadi va shuning uchun jozibali. Lekin natija guruhga "
                     "«tegishli» bo'lmaydi: u guruhda <u>kuchini saqlaydi</u> yoki "
                     "saqlamaydi. Ma'no biroz yonida — <em>precise</em> emas."),
                    (False, "submit",
                     "«bo'ysunmoq, taqdim etmoq» — ikkala ma'nosi ham bu gapga "
                     "mantiqan sig'maydi."),
                ])
                + TIP.format(
                    "Shu savolni va oldingi ikkitasini solishtiring: birida javob "
                    "eng sodda so'z edi (<em>preservation</em>), bunisida eng qiyini "
                    "(<em>generalise</em>). Qiyinlik hech qanday yo'nalish bermaydi — "
                    "shuning uchun uni <u>umuman hisobga olmang</u>.")
            ),
        },

        {
            "rich_text": blank_q(
                "<p>Reformers argued that the new registration rules would raise turnout, "
                "and turnout did rise in the first election held under them. But turnout "
                "rose by a similar amount in neighbouring districts that had adopted no "
                "reform at all, which makes the rules a poor "
                "<span class=\"sr-blank\"></span> for the change: something else appears "
                "to have moved both sets of districts at once.</p>"),
            "choices": [
                {"text": "explanation", "is_correct": True},
                {"text": "substitute", "is_correct": False},
                {"text": "precedent", "is_correct": False},
                {"text": "measurement", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Signal:</strong> ikki nuqta — keyingi qism bo'sh joyni "
                "izohlaydi: <em>something else appears to have moved both sets of "
                "districts</em>. «Boshqa nimadir <u>sabab</u> bo'lgan» — demak yangi "
                "qoidalar yomon <mark>sabab/izoh</mark>.</p>"
                + why([
                    (True, "explanation",
                     "«tushuntirish, izoh» — ikki nuqtadan keyingi jumla aynan sababni "
                     "izlayapti. Islohot o'tkazmagan tumanlarda ham bir xil o'sish "
                     "bo'lgani uchun qoidalar o'sishni tushuntirmaydi."),
                    (False, "substitute",
                     "«o'rnini bosuvchi» — qoidalar o'zgarishning o'rnini bosmaydi. "
                     "Ma'no gapga umuman tushmaydi."),
                    (False, "precedent",
                     "«oldingi namuna, pretsedent» — huquqiy-siyosiy matnda juda "
                     "ta'sirli eshitiladi va shuning uchun qo'yilgan. Lekin pretsedent "
                     "<u>keyingi</u> ishlar uchun namuna bo'ladi; bu yerda esa "
                     "o'tgan o'zgarishning sababi qidirilyapti."),
                    (False, "measurement",
                     "«o'lchov» — saylovda qatnashish darajasi o'lchangan, shuning "
                     "uchun bu so'z matn muhitidan ilinib qoladi. Lekin qoidalar "
                     "o'lchov asbobi emas — ular taxmin qilingan sabab edi."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>The letter was polite. It thanked him for eleven years of work, "
                "praised two projects by name, and regretted that the department could "
                "not renew his contract. Sobir read it twice and found that the "
                "politeness was the part he <span class=\"sr-blank\"></span> most: a "
                "blunt refusal would have cost him an afternoon, and this would cost him "
                "a month.</p>"),
            "choices": [
                {"text": "resented", "is_correct": True},
                {"text": "admired", "is_correct": False},
                {"text": "expected", "is_correct": False},
                {"text": "doubted", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Signal:</strong> ikki nuqta. Izoh: qo'pol rad javob bir "
                "kunga tushardi, muloyim xat esa <u>bir oyga</u>. Ya'ni muloyimlik "
                "unga qimmatga tushdi. Bashorat: <mark>«undan g'ashi keldi»</mark>.</p>"
                + why([
                    (True, "resented",
                     "«g'ashi keldi, ichida norozi bo'ldi» — ikki nuqtadan keyingi "
                     "taqqoslash aynan shuni tushuntiradi: muloyimlik og'riqni "
                     "cho'zdi."),
                    (False, "admired",
                     "«qoyil qoldi» — <em>The letter was polite</em> va "
                     "<em>praised two projects</em> ijobiy ohang beradi, shuning uchun "
                     "bu variant jozibali. Lekin ikki nuqtadan keyingi qism "
                     "shikoyat: qoyil qolgan odam narxdan gapirmaydi."),
                    (False, "expected",
                     "«kutgan edi» — <em>the part he expected most</em> mumkin gap, "
                     "lekin izoh unga hech qanday ma'no bermaydi. Kutish narxdan "
                     "gapirmaydi."),
                    (False, "doubted",
                     "«shubhalandi» — Sobir xatning rostligiga shubha qilmayapti; "
                     "u xatning uslubidan aziyat chekyapti."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>Popular accounts describe the immune system as an army, and the "
                "metaphor is useful until it is not. Armies have commanders and a chain "
                "of command; the immune system has neither. Its coordination emerges from "
                "very large numbers of cells following local rules, which makes the whole "
                "response, in the strict sense, <span class=\"sr-blank\"></span> — "
                "organised, but by nobody.</p>"),
            "choices": [
                {"text": "leaderless", "is_correct": True},
                {"text": "sophisticated", "is_correct": False},
                {"text": "defensive", "is_correct": False},
                {"text": "unreliable", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Signal:</strong> tire — keyingi qism bo'sh joyni "
                "boshqa so'zlar bilan qaytaradi: <mark><em>organised, but by "
                "nobody</em></mark>. Bundan aniqroq sovg'a bo'lmaydi.</p>"
                + why([
                    (True, "leaderless",
                     "«rahbarsiz» — <em>by nobody</em> ning bir so'zdagi tarjimasi, va "
                     "<em>Armies have commanders … the immune system has neither</em> "
                     "buni ikkinchi marta isbotlaydi. Sodda so'z, mukammal aniq."),
                    (False, "sophisticated",
                     "«murakkab, nozik tuzilgan» — darsning asosiy tuzog'i: eng "
                     "ta'sirli eshitiladigan variant. Immunitet tizimi haqiqatan "
                     "murakkab, shuning uchun bu <u>rost</u> — lekin tiredan keyingi "
                     "izoh murakkablik haqida emas, rahbarning yo'qligi haqida. "
                     "<strong>Rost, lekin so'ralmagan.</strong>"),
                    (False, "defensive",
                     "«himoya qiluvchi» — immunitet tizimi, albatta, himoya qiladi. "
                     "Yana bir rost-lekin-so'ralmagan variant, va u qo'shimcha "
                     "<em>army</em> metaforasidan quvvat oladi."),
                    (False, "unreliable",
                     "«ishonchsiz» — matn tizimni tanqid qilmayapti. "
                     "<em>organised</em> so'zi ijobiy baho beryapti."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Uch savolni har safar bering</h3>"
            "<p>Bu darsdagi to'g'ri javoblarni yana ko'zdan kechiring: "
            "<em>preservation</em>, <em>ambiguous</em>, <em>generalise</em>, "
            "<em>explanation</em>, <em>resented</em>, <em>leaderless</em>. Ular orasida "
            "qiyini ham, soddasi ham bor — <mark>hech qanday qonuniyat yo'q</mark>. "
            "Bo'lishi ham mumkin emas: SAT javobni qiyinlik bo'yicha tanlamaydi.</p>"
            "<p>Uch savol — hammasi shu:</p>"
            "<ol>"
            "<li><strong>Gap qanday ma'no talab qilyapti?</strong> (signal so'z, tinish "
            "belgisi, ma'no takrori)</li>"
            "<li><strong>Bu variantni matnning qaysi so'zlari isbotlaydi?</strong> "
            "Ko'rsatolmasangiz — bu javob emas.</li>"
            "<li><strong>Qolgan uchtasi nega xato?</strong> Har biriga nom bering.</li>"
            "</ol>"
            + WARN.format(
                "Eng ko'p uchraydigan noto'g'ri javob turi bu darsda ikki marta "
                "chiqdi: <strong>rost, lekin so'ralmagan</strong> "
                "(<em>sophisticated</em>, <em>defensive</em>). Immunitet tizimi "
                "murakkab ham, himoyachi ham — ikkovi ham to'g'ri gap. Lekin gap "
                "«murakkabmi?» deb so'ramayapti. <u>Rostlik yetarli emas.</u>")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            '<div class="pp-flashcards" data-pp-flashcards>'
            '<div class="pp-card"><div class="pp-card-front">ambiguous</div><div class="pp-card-back">ikki ma\'noli, noaniq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to generalise to ~</div><div class="pp-card-back">~ ga umumlashmoq, kengroq guruhga tatbiq bo\'lmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to resent</div><div class="pp-card-back">ichida norozi bo\'lmoq, g\'ashi kelmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">defensible</div><div class="pp-card-back">himoya qilsa bo\'ladigan, asosli</div></div>'
            '<div class="pp-card"><div class="pp-card-front">blunt (refusal)</div><div class="pp-card-back">qo\'pol, to\'g\'ridan-to\'g\'ri (rad javob)</div></div>'
            '<div class="pp-card"><div class="pp-card-front">uniformity</div><div class="pp-card-back">bir xillik</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to emerge from ~</div><div class="pp-card-back">~ dan o\'z-o\'zidan kelib chiqmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">precise</div><div class="pp-card-back">aniq (savolning o\'zi shuni so\'raydi)</div></div>'
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>So'zni <strong>ta'sirli ko'ringani uchun tanlamang</strong> — va "
            "shu sababdan <strong>rad ham etmang</strong>.</li>"
            "<li>Savolning o'zi <em>most logical and <u>precise</u></em> deydi: "
            "aniqlik ≠ ta'sirlilik.</li>"
            "<li>Har variantni butun gapga qo'yib o'qing (almashtirish sinovi).</li>"
            "<li>«Bu matnda isbotlanganmi?» — ta'sirli so'zlar ko'pincha shu savolda "
            "quladi.</li>"
            "<li>Eng ko'p tuzoq: <strong>rost, lekin so'ralmagan</strong>.</li>"
            "</ul>"
        )},
    ],
},

]
