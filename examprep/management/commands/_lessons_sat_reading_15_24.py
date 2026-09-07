# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — Reading lessons 15-16 and 20-24.

Closes the "Words in Context" topic (15-16) and covers the whole of
"Matn tuzilishi va maqsadi (Text Structure and Purpose)" (20-24).
See toc_sat_reading.txt and STYLE_GUIDE_SAT_RW.md.
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

TOPIC_TSP = {
    "title":   "Matn tuzilishi va maqsadi (Text Structure and Purpose)",
    "summary": "Matn qanday qurilgan va u nima ish qilyapti: umumiy tuzilish, matnning "
               "maqsadi va bitta jumlaning vazifasi.",
    "icon":    "bi-diagram-2",
    "order":   3,
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


def q(passage, stem):
    """Passage pane + a bolded exam stem."""
    return f'<div class="sr-passage">{passage}</div><p><strong>{stem}</strong></p>'


def blank_q(passage):
    return q(passage, "Which choice completes the text with the most logical and "
                      "precise word or phrase?")


def means_q(passage, word):
    return q(passage, f"As used in the text, what does the word “{word}” most nearly "
                      f"mean?")


def choices_html(items):
    """The static A/B/C/D list used in a WORKED example (not a shuffled choices block)."""
    return '<ol type="A">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 15
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_WIC,
    "title": "SAT R&W 15: Second Meanings in Literature and History Passages",
    "summary": "Eski matnlarda oddiy so'zlar bugungidan boshqa ma'noda ishlatiladi — "
               "want, suffer, close, nice, sensible; matnning yoshini aniqlash usuli.",
    "order": 15,
    "blocks": [
        {"rich_text": (
            "<h2>So'zning ma'nosi ham eskiradi</h2>"
            "<p>13-darsda oddiy so'zlarning ikkinchi ma'nolarini ko'rdik. Endi eng "
            "qiyin holatga o'tamiz: <mark>matn eski bo'lganda</mark>.</p>"
            "<p>SAT'ning to'rt mavzu sohasidan ikkitasi — <strong>literature</strong> va "
            "<strong>history / social studies</strong> — sizni muntazam ravishda "
            "XVIII–XIX asr nasri bilan uchrashtiradi: xartiyalar, nutqlar, maktublar, "
            "romanlar. O'sha davrda ko'p oddiy so'z bugungidan <u>boshqa</u> ma'noda "
            "ishlatilgan.</p>"
            "<p>Bu o'zbek o'quvchi uchun alohida xavfli. Siz so'zni maktabda "
            "o'rgangansiz, ma'nosini bilasiz — va aynan shu bilim sizni "
            "yiqitadi, chunki matn boshqa asrdan gapiryapti.</p>"
            + '<span class="sr-time">⏱ ~45 soniya (eski matn sekinroq o\'qiladi)</span>'
        )},

        {"rich_text": (
            "<h3>Avval matnning yoshini aniqlang</h3>"
            "<p>Bu bitta qadam savolning yarmini yechadi. Matn eski ekanini "
            "quyidagilardan bilasiz:</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>Manba qatori.</strong> SAT ko'pincha "
              "parcha ostida yoki tepasida <em>Adapted from … 1847</em> deb yozadi. "
              "Sana bo'lsa — birinchi navbatda shuni o'qing.</p></div>"
            + "<div class=\"pp-step\"><p><strong>Grammatik shakl.</strong> "
              "<em>should</em>, <em>shall</em>, <em>such … as</em>, <em>whereof</em>, "
              "<em>hath</em>, uzun ergashgan qo'shma gaplar, nuqtali vergul bilan "
              "bog'langan uzun ro'yxatlar.</p></div>"
            + "<div class=\"pp-step\"><p><strong>Mavzu.</strong> Xartiya, gildiya, "
              "parish, komissarlar, ot-arava, sham va lampa — bularning hammasi "
              "sana o'rnini bosadi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>Va keyin — shubha rejimi.</strong> "
              "Tagi chizilgan oddiy so'zni ko'rganingizda o'zingizga ayting: "
              "«bu so'z o'shanda boshqa narsani anglatgan bo'lishi mumkin». "
              "Bu shubhaning o'zi sizni tuzoqdan chiqaradi.</p></div>"
            + '</div>'
            + NOTE.format(
                "Adabiy parchada matn yangi bo'lsa ham ehtiyot bo'ling: yozuvchilar "
                "ataylab kitobiy, eskiroq so'z tanlashadi. <em>He was sensible of "
                "the honour</em> — bu jumlani bugungi yozuvchi ham yozishi mumkin.")
        )},

        {"rich_text": (
            "<h3>SAT eng ko'p sinaydigan eski ma'nolar</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>So'z</th><th>Bugungi ma'no (tuzoq)</th><th>Eski ma'no</th></tr></thead>"
              "<tbody>"
              "<tr><td>want</td><td>xohlamoq</td><td>yetishmaslik, muhtojlik</td></tr>"
              "<tr><td>suffer</td><td>azob chekmoq</td><td>ruxsat bermoq, yo'l qo'ymoq</td></tr>"
              "<tr><td>close</td><td>yaqin; yopmoq</td><td>dim, havosiz (xona haqida)</td></tr>"
              "<tr><td>nice</td><td>yoqimli</td><td>nozik, mayda, aniq (farq haqida)</td></tr>"
              "<tr><td>sensible</td><td>oqilona</td><td>his qilayotgan, xabardor</td></tr>"
              "<tr><td>mean</td><td>ziqna; anglatmoq</td><td>oddiy, past martabali</td></tr>"
              "<tr><td>several</td><td>bir nechta</td><td>alohida, har biri o'ziniki</td></tr>"
              "<tr><td>party</td><td>bazm; partiya</td><td>tomon, ishtirokchi</td></tr>"
              "<tr><td>artificial</td><td>sun'iy (yomon ma'noda)</td><td>mahorat bilan yasalgan</td></tr>"
              "<tr><td>success</td><td>muvaffaqiyat</td><td>oqibat, natija (yaxshi yoki yomon)</td></tr>"
              "<tr><td>still</td><td>hali ham</td><td>doim, muttasil</td></tr>"
              "<tr><td>prevent</td><td>oldini olmoq</td><td>oldinroq kelmoq, oldindan qilmoq</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "Bu jadvalni yodlab, imtihonda «eski ma'noni tanlayman» deb "
                "qo'ymang — bu yangi tuzoq bo'ladi. Ko'p eski matnda "
                "<em>want</em> haqiqatan «xohlamoq» ma'nosida keladi. "
                "Jadval faqat <u>shubhani yoqish</u> uchun; javobni baribir "
                "gapning o'zi beradi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + means_q(
                "<p>The commissioners reported that the northern parishes were in great "
                "<span class=\"sr-focus\">want</span> of grain, the harvest having failed "
                "in two successive years, and that such stores as remained were held in "
                "three towns only. They recommended that the roads be put in repair "
                "before winter, so that what could be spared might be carried where it "
                "was needed.</p>"
                "<span class=\"sr-passage__src\">Adapted from a county report of 1817.</span>",
                "want")
            + choices_html(["desire", "need", "refusal", "abundance"])
            + "<p><strong>1-qadam — yoshi.</strong> Manba qatori 1817 deb turibdi, "
            "va til ham buni tasdiqlaydi: <em>such stores as remained</em>, "
            "<em>be put in repair</em>. Shubha rejimi yoqildi.</p>"
            + "<p><strong>2-qadam — so'zni olib tashlang.</strong> "
            "<em>the parishes were in great ___ of grain</em>, va sabab darhol "
            "aytilgan: <em>the harvest having failed in two successive years</em>. "
            "Hosil ikki yil ketma-ket bitmagan. Demak donga <mark>muhtojlik</mark>.</p>"
            + "<p><strong>3-qadam — variantlarni gapga qo'ying.</strong></p>"
            + why([
                (True, "need",
                 "«ehtiyoj, muhtojlik» — <em>in want of</em> iborasining eski (va hozir "
                 "ham kitobiy) ma'nosi. Isbot: hosil ikki yil bitmagan, zaxira faqat "
                 "uch shaharda qolgan, va donni yetishmayotgan joyga tashish taklif "
                 "qilinyapti."),
                (False, "desire",
                 "«istak» — bugungi ma'no, va aynan shuning uchun qo'yilgan. "
                 "Ma'nosiz emas, lekin mantiqan bo'sh: qishloqlar donni "
                 "«xohlagani» hisobotga tushmaydi, ochlik tushadi. "
                 "<strong>Eng ko'p tanlanadigan noto'g'ri javob.</strong>"),
                (False, "abundance",
                 "«mo'l-ko'lchilik» — mantiqni teskari qiladi. Agar don ko'p bo'lsa, "
                 "uni boshqa joyga tashish shart emasdi."),
                (False, "refusal",
                 "«rad etish» — matnda hech kim hech nimadan bosh tortmayapti."),
            ])
        )},

        {
            "rich_text": means_q(
                "<p>The charter did not grant the guild a monopoly outright. It provided "
                "instead that the mayor should not "
                "<span class=\"sr-focus\">suffer</span> any stranger to sell cloth within "
                "the market on the days appointed for the guild's own trading, and that "
                "offenders should be put out at the gates without further penalty.</p>"
                "<span class=\"sr-passage__src\">Adapted from a study of medieval town "
                "charters.</span>", "suffer"),
            "choices": [
                {"text": "permit", "is_correct": True},
                {"text": "endure", "is_correct": False},
                {"text": "undergo", "is_correct": False},
                {"text": "regret", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Qurilish javobni beradi.</strong> "
                "<em>suffer <u>any stranger</u> <u>to sell</u></em> — fe'ldan keyin "
                "ot, keyin <em>to</em> + fe'l keladi. Ingliz tilida bu qurilish "
                "<mark>«ruxsat bermoq»</mark> ma'nosini talab qiladi "
                "(<em>allow someone to do</em> kabi). «Azob chekmoq» ma'nosi bunday "
                "qurilishda kelmaydi.</p>"
                "<p><strong>Mantiq ham shuni aytadi:</strong> gap merning nimaga "
                "<u>yo'l qo'ymasligi</u> haqida, va qoidani buzganlar darvozadan "
                "chiqarib yuborilgan.</p>"
                + why([
                    (True, "permit",
                     "«ruxsat bermoq, yo'l qo'ymoq». <em>should not suffer any "
                     "stranger to sell</em> = «begonaning sotishiga yo'l qo'ymasin». "
                     "Jazo haqidagi bo'lak buni tasdiqlaydi."),
                    (False, "endure",
                     "«chidamoq» — bugungi asosiy ma'no. Mer begonani «chiday "
                     "olmaydi» degan o'qish qurilishga sig'maydi va xartiyaning "
                     "huquqiy ohangiga ham mos emas."),
                    (False, "undergo",
                     "«boshdan kechirmoq» — bu ham «azob chekmoq» oilasidan, va u "
                     "odamni ob'ekt sifatida qabul qilmaydi."),
                    (False, "regret",
                     "«afsuslanmoq» — hujjat hech kimning hissiyotini tartibga "
                     "solmaydi."),
                ])
            ),
        },

        {
            "rich_text": means_q(
                "<p>The room was small and very <span class=\"sr-focus\">close</span>, "
                "for the window had been shut since morning against the dust of the road "
                "and the lamp had been burning some hours. Zuhra found that she could not "
                "attend to what her aunt was saying, and twice caught herself looking at "
                "the door.</p>", "close"),
            "choices": [
                {"text": "stuffy", "is_correct": True},
                {"text": "nearby", "is_correct": False},
                {"text": "secretive", "is_correct": False},
                {"text": "crowded", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Sabab ergash gapi hamma narsani aytadi:</strong> "
                "<em><u>for</u> the window had been shut since morning … and the lamp "
                "had been burning some hours</em>. Deraza ertalabdan yopiq, lampa bir "
                "necha soat yonyapti — xona <mark>dim, havosiz</mark>.</p>"
                "<p>Uchinchi isbot ham bor: Zuhra e'tiborini jamlay olmayapti va "
                "eshikka qarayapti — havosiz xonaning odatiy ta'siri.</p>"
                + why([
                    (True, "stuffy",
                     "«dim, havosiz» — <em>a close room</em> iborasining ma'nosi. "
                     "<em>for</em> bilan boshlangan sabab bevosita isbot."),
                    (False, "nearby",
                     "«yaqin» — bugungi asosiy ma'no va shuning uchun eng kuchli "
                     "tuzoq. Lekin «yaqin xona» degani yo'q: xona nimaga yaqin? "
                     "Va yaqinlik deraza bilan lampani tushuntirmaydi."),
                    (False, "secretive",
                     "«sirli, yopiq» — <em>close</em> odamlar haqida bunday ma'no "
                     "berishi mumkin (<em>a close man</em>), lekin bu yerda ega — "
                     "xona."),
                    (False, "crowded",
                     "«odam ko'p» — matnda ikki kishi bor, xolos. Xona "
                     "<em>small</em> ekani bu variantni jozibali qiladi, lekin "
                     "kichiklik gavjumlik degani emas."),
                ])
            ),
        },

        {
            "rich_text": means_q(
                "<p>The dispute between the two cartographers was not about the coastline, "
                "which both had surveyed and agreed upon, but about a "
                "<span class=\"sr-focus\">nice</span> distinction in the projection: "
                "whether a line of constant bearing ought to be drawn straight or curved. "
                "To a sailor within sight of land the difference came to a few hundred "
                "metres; to a mathematician it was the whole question.</p>", "nice"),
            "choices": [
                {"text": "subtle", "is_correct": True},
                {"text": "pleasant", "is_correct": False},
                {"text": "generous", "is_correct": False},
                {"text": "recent", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Oxirgi jumla ta'rif beradi:</strong> dengizchi uchun farq "
                "bir necha yuz metr, matematik uchun butun masala. Ya'ni farq "
                "<mark>juda mayda, lekin muhim</mark> — bu <em>nice</em> so'zining "
                "eski (hozir ham ilmiy nasrda saqlanib qolgan) ma'nosi.</p>"
                + why([
                    (True, "subtle",
                     "«nozik, mayda» — <em>a nice distinction</em> iborasining aynan "
                     "ma'nosi. Oxirgi jumladagi qarama-qarshilik (bir necha yuz metr ↔ "
                     "butun masala) buning to'g'ridan-to'g'ri isboti."),
                    (False, "pleasant",
                     "«yoqimli» — bugungi asosiy ma'no. Lekin ikki olimning "
                     "<em>dispute</em> (bahs)i yoqimli farq ustida bo'lmaydi, va "
                     "«yoqimli farq» iborasining o'zi ma'nosiz."),
                    (False, "generous",
                     "«saxiy» — farq saxiy bo'lolmaydi; bu sifat odamlarga tegishli."),
                    (False, "recent",
                     "«yaqinda paydo bo'lgan» — matnda vaqt umuman muhokama "
                     "qilinmaydi."),
                ])
            ),
        },

        {
            "rich_text": means_q(
                "<p>Bahodir had not expected to be asked, and he was "
                "<span class=\"sr-focus\">sensible</span> of the honour, though he showed "
                "nothing of it. He thanked the elder, said that he would give his answer "
                "in the morning, and walked home the long way, past the canal, where "
                "there was nobody to see his face.</p>", "sensible"),
            "choices": [
                {"text": "aware", "is_correct": True},
                {"text": "reasonable", "is_correct": False},
                {"text": "noticeable", "is_correct": False},
                {"text": "emotional", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Qurilishga qarang:</strong> <em>sensible <u>of</u> the "
                "honour</em>. <em>of</em> predlogi bu yerda hal qiladi — "
                "<em>sensible of X</em> = «X ni his qilayotgan, X dan xabardor». "
                "Bugungi <em>sensible</em> («oqilona») predlogsiz ishlatiladi.</p>"
                "<p><strong>Ikkinchi isbot:</strong> <em>though he showed nothing of "
                "it</em> — «buni sirtiga chiqarmadi». Demak ichida <mark>his "
                "qilgan</mark> narsa bor edi. Oxirgi jumla ham shu haqda: u yuzini "
                "hech kim ko'rmaydigan yo'ldan yurdi.</p>"
                + why([
                    (True, "aware",
                     "«xabardor, his qilayotgan» — <em>sensible of</em> qurilishining "
                     "ma'nosi, va <em>though he showed nothing of it</em> uni "
                     "tasdiqlaydi."),
                    (False, "reasonable",
                     "«oqilona» — bugungi asosiy ma'no va eng ko'p tanlanadigan "
                     "variant. Lekin <em>he was reasonable of the honour</em> "
                     "grammatik jihatdan ham buziladi: predlog bu ma'noga tushmaydi."),
                    (False, "noticeable",
                     "«sezilarli» — ma'noni teskari qiladi: matn u hech nimani "
                     "ko'rsatmaganini aytyapti."),
                    (False, "emotional",
                     "«hissiyotli» — hikoyaning ohangiga mos keladi va shuning uchun "
                     "jozibali, lekin <em>sensible</em> bu ma'noni hech qachon "
                     "bermaydi. Bu — matnning kayfiyatini so'zning ma'nosi bilan "
                     "adashtirish."),
                ])
                + TIP.format(
                    "Uchta savolda ham javobni <u>predlog yoki qurilish</u> berdi: "
                    "<em>in want <b>of</b></em>, <em>suffer X <b>to</b> do</em>, "
                    "<em>sensible <b>of</b></em>. Eski matnda ma'nodan oldin "
                    "<strong>qurilishga</strong> qarang — u ko'pincha bitta ma'noni "
                    "majburlaydi.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">in want of ~</div><div class="pp-card-back">~ ga muhtoj, ~ yetishmaydi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to suffer X to do</div><div class="pp-card-back">X ning qilishiga yo\'l qo\'ymoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a close room</div><div class="pp-card-back">dim, havosiz xona</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a nice distinction</div><div class="pp-card-back">nozik, mayda farq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">sensible of ~</div><div class="pp-card-back">~ ni his qilayotgan, ~ dan xabardor</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a party to an agreement</div><div class="pp-card-back">kelishuv tomoni, ishtirokchisi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to put in repair</div><div class="pp-card-back">ta\'mirlamoq, tuzatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">outright</div><div class="pp-card-back">to\'g\'ridan-to\'g\'ri, butunlay</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Avval matnning yoshini aniqlang</strong> — manba qatori, "
              "grammatika, mavzu.</li>"
              "<li>Eski matnda tanish so'z ko'rsangiz — <u>shubha rejimini yoqing</u>.</li>"
              "<li>Javobni ko'pincha <strong>predlog yoki qurilish</strong> beradi "
              "(<em>in want of</em>, <em>suffer X to do</em>, <em>sensible of</em>).</li>"
              "<li>Jadvalni yodlab «har doim eski ma'no» demang — gap baribir "
              "o'zi hal qiladi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 16
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_WIC,
    "title": "SAT R&W 16: Words in Context — Mixed Practice Under Time",
    "summary": "Ikkala shakl aralash, oltita savol, imtihon tezligida: 10–15-darslarda "
               "o'rganilgan usulni soatga qarshi mustahkamlash.",
    "order": 16,
    "blocks": [
        {"rich_text": (
            "<h2>Endi soatga qarshi</h2>"
            "<p>Bu — <strong>Words in Context</strong> mavzusining yakuniy darsi. "
            "Yangi qoida yo'q; oltita savol bor, ikkala shakl aralash, va ular "
            "imtihondagidek ketma-ket keladi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Qanday ishlash kerak:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li>Telefoningizda taymer qo'ying: <strong>4 daqiqa</strong> "
                "(6 × 40 soniya).</li>"
                "<li>Oltitasini <u>to'xtamasdan</u> yeching. Qiynalsangiz — belgilang "
                "va keting, xuddi imtihondagidek.</li>"
                "<li>Shundan keyingina tushuntirishlarni o'qing.</li>"
                "</ol>")
            + "<p>Vaqt tugagach javob bermaganlaringiz bo'lsa — bu ham natija. "
            "Oxirgi blokda xatolarni <u>turi bo'yicha</u> tahlil qilamiz.</p>"
            + '<span class="sr-time">⏱ 6 savol · 4 daqiqa</span>'
        )},

        {"rich_text": (
            "<h3>Yodda tutiladigan uchta harakat</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>Variantlarni yoping</strong>, mantiqni "
              "o'qing, o'z so'zingizni ayting (11-dars).</p></div>"
            + "<div class=\"pp-step\"><p><strong>Signalni toping</strong>: "
              "<em>but · because · although · far from · rather than</em>, yoki "
              "<strong>: ; —</strong> (12-dars).</p></div>"
            + "<div class=\"pp-step\"><p><strong>Qiyinlikni e'tiborsiz qoldiring</strong> "
              "— so'zni ta'sirli ko'ringani uchun na tanlang, na rad eting "
              "(14-dars).</p></div>"
            + '</div>'
        )},

        {
            "rich_text": blank_q(
                "<p>Permafrost is defined by temperature rather than by ice: ground that "
                "has stayed below freezing for two years running qualifies, whether or "
                "not any water is present. The definition matters because thawing "
                "releases carbon that has been <span class=\"sr-blank\"></span> for "
                "millennia — plant material that froze before it could decay, and has "
                "neither rotted nor moved since.</p>"),
            "choices": [
                {"text": "immobilised", "is_correct": True},
                {"text": "escaping", "is_correct": False},
                {"text": "diluted", "is_correct": False},
                {"text": "measured", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Signal:</strong> tire — keyingi qism bo'sh joyni qaytaradi: "
                "<mark><em>has neither rotted nor moved since</em></mark>. Ikkalasi "
                "ham inkor: uglerod na chirigan, na joyidan qimirlagan.</p>"
                + why([
                    (True, "immobilised",
                     "«qimirlamas holga keltirilgan, qotib qolgan» — "
                     "<em>neither rotted nor moved</em> ning bir so'zdagi ifodasi."),
                    (False, "escaping",
                     "«chiqib ketayotgan» — mantiqni buzadi: uglerod eriganda "
                     "chiqadi, ming yillar davomida emas. Matndagi <em>releases</em> "
                     "so'ziga yopishgan <strong>so'z-tuzoq</strong>."),
                    (False, "diluted",
                     "«suyultirilgan» — muzlagan tuproqda suyultirish jarayoni "
                     "muhokama qilinmaydi, va bu <em>rotted</em> yoki <em>moved</em> "
                     "bilan bog'lanmaydi."),
                    (False, "measured",
                     "«o'lchangan» — olimlar o'lchaydi, uglerod emas; va o'lchov "
                     "ming yillar davom etmaydi."),
                ])
            ),
        },

        {
            "rich_text": means_q(
                "<p>The register lists each <span class=\"sr-focus\">party</span> to the "
                "agreement by name, occupation and parish, and requires two witnesses for "
                "every signature. Where a signatory could not write, the clerk drew a "
                "cross and noted beside it the name of the man who had guided the "
                "hand.</p>", "party"),
            "choices": [
                {"text": "participant", "is_correct": True},
                {"text": "celebration", "is_correct": False},
                {"text": "political group", "is_correct": False},
                {"text": "group of travellers", "is_correct": False},
            ],
            "explanation": (
                "<p><em>party <u>to</u> the agreement</em> — predlog yana javobni "
                "beradi. Kelishuvga «tomon» bo'lgan odam. Va davomi tasdiqlaydi: "
                "har bir <em>party</em> ismi, kasbi va mahallasi bilan yozilgan, "
                "ya'ni bu <mark>bitta odam</mark>.</p>"
                + why([
                    (True, "participant",
                     "«ishtirokchi, tomon» — <em>a party to an agreement</em> huquqiy "
                     "iborasining ma'nosi. Ism-kasb-mahalla ro'yxati buni isbotlaydi."),
                    (False, "celebration",
                     "«bazm» — bugungi eng mashhur ma'no va shuning uchun tuzoq. "
                     "Bazmning kasbi va mahallasi bo'lmaydi."),
                    (False, "political group",
                     "«siyosiy partiya» — real ma'no, lekin matn shaxsiy kelishuv "
                     "va guvohlar haqida; siyosat umuman yo'q."),
                    (False, "group of travellers",
                     "«yo'lovchilar guruhi» — <em>a search party</em> kabi iboralardan "
                     "kelib chiqadigan ma'no, lekin bu yerda hech kim hech qayerga "
                     "bormayapti."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>The architect's drawings for the reading room show it lit entirely "
                "from above. Windows at eye level were rejected deliberately: a reader who "
                "can see the street will look at it. The design therefore "
                "<span class=\"sr-blank\"></span> the two demands that usually compete in "
                "such a building — daylight and sustained attention — by admitting the "
                "first from a direction that offers nothing to watch.</p>"),
            "choices": [
                {"text": "reconciles", "is_correct": True},
                {"text": "confuses", "is_correct": False},
                {"text": "postpones", "is_correct": False},
                {"text": "exaggerates", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kalit ibora:</strong> <em>the two demands that usually "
                "<u>compete</u></em>. Odatda qarama-qarshi bo'lgan ikki talab, va "
                "loyiha ularni bitta yechim bilan qondiryapti "
                "(<em>by admitting the first from a direction that offers nothing to "
                "watch</em>). Bashorat: <mark>«ikkovini yarashtiradi»</mark>.</p>"
                + why([
                    (True, "reconciles",
                     "«yarashtiradi, ikkovini birga imkonli qiladi» — "
                     "<em>compete</em> bilan aniq juftlik hosil qiladi, va tiredan "
                     "keyingi bo'lak mexanizmini tushuntiradi."),
                    (False, "confuses",
                     "«chalkashtiradi» — loyiha ikki talabni ajratmayapti ham, "
                     "chalkashtirmayapti ham; u ikkovini <u>bir vaqtda</u> "
                     "bajaryapti."),
                    (False, "postpones",
                     "«kechiktiradi» — talablarni kechiktirib bo'lmaydi, va vaqt "
                     "matnda umuman yo'q."),
                    (False, "exaggerates",
                     "«bo'rttiradi» — grammatik jihatdan o'tiradi, lekin gapning "
                     "mantiqiga hech qanday aloqasi yo'q. Bo'sh joyning javobi "
                     "<em>compete</em> so'ziga javob berishi kerak."),
                ])
            ),
        },

        {
            "rich_text": means_q(
                "<p>From the ridge the old fort <span class=\"sr-focus\">commands</span> "
                "the whole of the valley road: a sentry on its wall could see a rider a "
                "full hour before he arrived. The garrison was never large enough to stop "
                "anyone, and the walls themselves are unremarkable. What mattered was "
                "always the position.</p>", "commands"),
            "choices": [
                {"text": "overlooks", "is_correct": True},
                {"text": "controls", "is_correct": False},
                {"text": "orders", "is_correct": False},
                {"text": "deserves", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki nuqta izoh beradi:</strong> <em>a sentry on its wall "
                "could see a rider a full hour before he arrived</em>. Gap "
                "<mark>ko'rish</mark> haqida — qal'a yo'lni <u>ko'rib turadi</u>.</p>"
                + why([
                    (True, "overlooks",
                     "«yuqoridan ko'rib turadi, nazorat qiladi (ko'z bilan)» — "
                     "<em>a fort commanding a view</em> iborasining ma'nosi. Ikki "
                     "nuqtadan keyingi izoh boshqa hech nimaga to'g'ri kelmaydi."),
                    (False, "controls",
                     "«boshqaradi, nazorat qiladi (kuch bilan)» — eng jozibali "
                     "noto'g'ri javob, chunki qal'a haqiqatan strategik. Lekin matn "
                     "buni <strong>ataylab</strong> rad etadi: <em>The garrison was "
                     "never large enough to stop anyone</em>. Kuch bilan nazorat "
                     "qilolmagan."),
                    (False, "orders",
                     "«buyruq beradi» — <em>command</em>ning eng mashhur ma'nosi. "
                     "Lekin qal'a yo'lga buyruq berolmaydi; buyruq odamlarga "
                     "beriladi."),
                    (False, "deserves",
                     "«loyiq» — ma'no jihatdan gapga umuman tushmaydi."),
                ])
            ),
        },

        {
            "rich_text": blank_q(
                "<p>Cities that publish their budgets in machine-readable form do not "
                "thereby become more accountable. Someone has to open the files, and "
                "reading them usefully takes skills that are scarce and unevenly "
                "distributed. Publication is therefore a "
                "<span class=\"sr-blank\"></span> of accountability rather than a "
                "guarantee of it: necessary, and nowhere near sufficient.</p>"),
            "choices": [
                {"text": "precondition", "is_correct": True},
                {"text": "substitute", "is_correct": False},
                {"text": "consequence", "is_correct": False},
                {"text": "measurement", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki nuqta yana javobni yozib qo'ygan:</strong> "
                "<mark><em>necessary, and nowhere near sufficient</em></mark> — "
                "«zarur, lekin yetarli emas». Mantiqda bunday narsaning nomi bor: "
                "shart.</p>"
                + why([
                    (True, "precondition",
                     "«dastlabki shart» — <em>necessary … not sufficient</em> ta'rifini "
                     "bir so'zga jamlaydi, va <em>rather than a guarantee</em> bilan "
                     "ham to'g'ri juftlik hosil qiladi."),
                    (False, "substitute",
                     "«o'rnini bosuvchi» — matn nashrni hisobdorlikning o'rniga "
                     "qo'ymayapti; aksincha, u yetarli emas deyapti."),
                    (False, "consequence",
                     "«oqibat» — vaqt bo'yicha teskari: nashr hisobdorlikdan kelib "
                     "chiqmaydi, unga <u>yo'l ochadi</u>."),
                    (False, "measurement",
                     "«o'lchov» — byudjet va raqamlar mavzusidan ilinib qolgan "
                     "<strong>so'z-tuzoq</strong>. Nashr hisobdorlikni o'lchamaydi."),
                ])
            ),
        },

        {
            "rich_text": means_q(
                "<p>A hectare of the new variety <span class=\"sr-focus\">yields</span> "
                "about a fifth more grain than the older one in a season with good rain, "
                "and about the same in a dry one. Farmers who cannot irrigate therefore "
                "gain least from the change — a fact the promotional literature tends to "
                "leave out.</p>", "yields"),
            "choices": [
                {"text": "produces", "is_correct": True},
                {"text": "surrenders", "is_correct": False},
                {"text": "bends", "is_correct": False},
                {"text": "admits", "is_correct": False},
            ],
            "explanation": (
                "<p>Ega — <em>a hectare</em>, ob'ekt — <em>grain</em>. Bir gektar don "
                "<mark>beradi</mark>. Qolgan uchta variant <em>yield</em> so'zining "
                "haqiqiy ma'nolari, lekin ularning hech biri yer va donni "
                "bog'lamaydi.</p>"
                + why([
                    (True, "produces",
                     "«hosil beradi» — qishloq xo'jaligidagi asosiy ma'no "
                     "(<em>crop yield</em> = hosildorlik). Taqqoslash "
                     "(<em>a fifth more … about the same</em>) miqdor haqida, ya'ni "
                     "hosil haqida."),
                    (False, "surrenders",
                     "«taslim bo'ladi, topshiradi» — <em>yield to the enemy</em> "
                     "ma'nosi. Real, lekin yer taslim bo'lmaydi."),
                    (False, "bends",
                     "«egiladi» — <em>the branch yielded under his weight</em> "
                     "ma'nosi. Bu yerda hech narsa egilmayapti."),
                    (False, "admits",
                     "«tan oladi» — <em>yield the point in an argument</em> ma'nosiga "
                     "yaqin, lekin gektar bahslashmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Xatoni turi bo'yicha tahlil qiling</h3>"
            "<p>Bu darsdagi natijangizni <u>nechta to'g'ri</u> deb emas, "
            "<u>qanday xato</u> deb o'qing. Har bir noto'g'ri javobingizni shu to'rt "
            "qutidan biriga soling:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Xato turi</th><th>Nima qilish kerak</th></tr></thead>"
              "<tbody>"
              "<tr><td>So'zning mashhur ma'nosini tanladim "
              "(<em>party</em>, <em>commands</em>)</td>"
              "<td>13 va 15-darsni qayta o'qing. Tagi chizilgan so'z ko'rsangiz — "
              "shubha rejimi.</td></tr>"
              "<tr><td>Signalni ko'rmadim (<strong>:</strong> <strong>—</strong> "
              "<em>compete</em>)</td>"
              "<td>12-dars. Bo'sh joyli savolda avval tinish belgilarini qidiring.</td></tr>"
              "<tr><td>Matndagi so'zga yopishdim (<em>escaping</em>, "
              "<em>measurement</em>)</td>"
              "<td>Bashorat qilmagansiz. 11-dars: variantlarni yoping.</td></tr>"
              "<tr><td>Vaqt yetmadi</td>"
              "<td>Sekinlik odatda ikkilanishdan chiqadi, o'qishdan emas. Ikkilanish "
              "esa bashorat qilmaslikdan chiqadi.</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Oltitadan 4–5 tasini to'g'ri yechsangiz — bu mavzu bo'yicha "
                "yaxshi darajadasiz. 3 va undan kam bo'lsa, 11 va 12-darslarga "
                "qayting: deyarli har doim muammo lug'atda emas, "
                "<u>bashorat qilmaslikda</u>.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to immobilise</div><div class="pp-card-back">qimirlamas holga keltirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to reconcile (two demands)</div><div class="pp-card-back">(ikki talabni) yarashtirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to command a view</div><div class="pp-card-back">yuqoridan ko\'rib turmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a precondition</div><div class="pp-card-back">dastlabki shart</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to yield (a crop)</div><div class="pp-card-back">(hosil) bermoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">necessary but not sufficient</div><div class="pp-card-back">zarur, lekin yetarli emas</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">unevenly distributed</div><div class="pp-card-back">notekis taqsimlangan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to leave out</div><div class="pp-card-back">tushirib qoldirmoq, aytmaslik</div></div>'
            + "</div>"
            + "<h3>Xulosa — Words in Context mavzusi yakuni</h3>"
            + "<ul>"
              "<li>Bu <u>lug'at imtihoni emas</u>: so'zlar tanish, ma'nolari "
              "kutilmagan (10-dars).</li>"
              "<li>Variantlarni yoping va <strong>bashorat qiling</strong> "
              "(11-dars).</li>"
              "<li><strong>Signal so'z va tinish belgisi</strong> javobni beradi "
              "(12-dars).</li>"
              "<li>«Most nearly means» da so'zni <u>olib tashlang</u> (13-dars).</li>"
              "<li>Qiyinlik hech nimani bildirmaydi (14-dars).</li>"
              "<li>Eski matnda <strong>qurilishga</strong> qarang (15-dars).</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 20
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_TSP,
    "title": "SAT R&W 20: Overall Structure vs Main Purpose — Two Different Questions",
    "summary": "Tuzilish savoli matnning shaklini so'raydi, maqsad savoli uning vazifasini; "
               "javoblarning shakli ham har xil — «avval…, keyin…» va «To …».",
    "order": 20,
    "blocks": [
        {"rich_text": (
            "<h2>Ikki savol, ikki xil javob</h2>"
            "<p><em>Craft and Structure</em> domenining ikkinchi turi — "
            "<strong>Text Structure and Purpose</strong>. U ikki xil savol beradi, va "
            "ko'p o'quvchi ularni <mark>bir xil savol deb o'ylab</mark> ball "
            "yo'qotadi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 6px;\"><strong>Tuzilish savoli:</strong></p>"
                "<p style=\"margin:0 0 10px;\"><em>Which choice best describes the "
                "overall structure of the text?</em></p>"
                "<p style=\"margin:0 0 6px;\"><strong>Maqsad savoli:</strong></p>"
                "<p style=\"margin:0;\"><em>What is the main purpose of the text?</em> "
                "yoki <em>What is the main purpose of the underlined sentence?</em></p>")
            + "<p>Farq bitta so'zda, lekin javob butunlay boshqacha bo'ladi.</p>"
            + '<span class="sr-time">⏱ ~60 soniya (bu tur sekinroq)</span>'
        )},

        {"rich_text": (
            "<h3>Tuzilish = shakl. Maqsad = vazifa.</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th></th><th>Structure</th><th>Purpose</th></tr></thead>"
              "<tbody>"
              "<tr><td>Savol</td><td><em>overall structure</em></td>"
              "<td><em>main purpose</em></td></tr>"
              "<tr><td>Nima so'raydi</td><td>Matn qanday <u>qurilgan</u> — qaysi "
              "harakat qaysidan keyin keladi</td><td>Matn (yoki jumla) qanday "
              "<u>ish bajaryapti</u></td></tr>"
              "<tr><td>Javobning shakli</td><td>«X ni beradi, <u>keyin</u> Y ni "
              "qiladi» — ikki-uch bosqich</td><td>«<u>To</u> …» — bitta fe'l bilan "
              "boshlanadi</td></tr>"
              "<tr><td>Ichida bo'ladi</td><td><em>then · before · after · finally · "
              "goes on to</em></td><td><em>To explain · to argue · to illustrate · "
              "to introduce</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Amaliy hiyla: <strong>variantlarning shakliga qarab savolni "
                "tekshiring</strong>. Agar variantlar <em>To …</em> bilan boshlansa, "
                "bu maqsad savoli; agar ular ichida <em>then</em> bo'lsa, bu tuzilish "
                "savoli. Bir necha soniyada o'zingizni to'g'ri rejimga qo'yasiz.")
        )},

        {"rich_text": (
            "<h3>Usul — ikkalasi uchun ham bir xil boshlanadi</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Har jumlani bitta so'z bilan "
              "nomlang.</strong> O'qiyotib o'zingizga ayting: «da'vo» … «dalil» … "
              "«e'tiroz» … «xulosa». Matn qisqa, shuning uchun bu 15 soniya oladi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Burilishni toping.</strong> Deyarli "
              "har SAT parchasida bitta burilish bor: <em>but</em>, <em>however</em>, "
              "<em>yet</em>, <em>in fact</em>. Tuzilish javobining markazi — "
              "o'sha burilish.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Savolga qarab bashorat "
              "qiling.</strong> Tuzilish uchun: «avval …, keyin …». Maqsad uchun: "
              "«bu matn … qilish uchun yozilgan».</p></div>"
            + "<div class=\"pp-step\"><p><strong>4. Variantni <u>oxirigacha</u> "
              "o'qing.</strong> Bu turda tuzoqlarning ko'pi variantning "
              "<u>ikkinchi yarmida</u> yashiringan: boshi to'g'ri, oxiri "
              "o'ylab topilgan.</p></div>"
            + '</div>'
            + WARN.format(
                "4-qadam bu mavzuning eng muhim qoidasi. <strong>Yarim to'g'ri</strong> "
                "tuzog'i bu yerda boshqa hamma turdagidan ko'ra ko'proq uchraydi, "
                "chunki variantlar uzun. Variantning birinchi yarmi mos kelgani "
                "<u>hech nimani</u> isbotlamaydi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna — bitta matn, ikkita savol</h3>"
            + '<div class="sr-passage">'
            + "<p>For a century the giant sequoia was thought to owe its survival to "
              "bark thick enough to turn aside a ground fire. Foresters therefore "
              "suppressed fires wherever the trees grew. Seedling counts fell steadily "
              "under that policy, and the reason turned out to be the fires themselves: "
              "the cones of the sequoia are sealed with resin that only heat will open, "
              "and the ash bed a fire leaves behind is where the seeds germinate best.</p>"
            + '</div>'
            + "<p><strong>1-savol.</strong> <em>Which choice best describes the overall "
              "structure of the text?</em></p>"
            + choices_html([
                "It describes a long-held explanation, then presents evidence that the "
                "explanation was incomplete.",
                "It compares two species of tree and explains why one is more resilient.",
                "It criticises foresters for a policy and proposes an alternative.",
                "It defines a technical term and then gives three examples of its use.",
            ])
            + "<p><strong>2-savol.</strong> <em>What is the main purpose of the "
              "text?</em></p>"
            + choices_html([
                "To argue that fire suppression should be banned in all forests.",
                "To explain how a well-meaning policy failed because of an incomplete "
                "understanding of the tree.",
                "To describe the physical structure of sequoia bark in detail.",
                "To compare the germination rates of several conifer species.",
            ])
            + '<span class="sr-time">⏱ ~60 soniya har biriga</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>1-qadam — jumlalarni nomlaymiz.</strong> "
            "(1) eski tushuntirish · (2) o'sha tushuntirishdan kelib chiqqan siyosat · "
            "(3) natija yomon chiqdi + haqiqiy sabab.</p>"
            "<p><strong>2-qadam — burilish:</strong> <em>the reason turned out to "
            "be the fires themselves</em>. Butun matn shu bir jumla atrofida "
            "aylanadi.</p>"
            + "<h4>1-savol — tuzilish</h4>"
            + "<p>Bashorat: «avval eski qarash beriladi, keyin uni buzadigan "
              "dalil keladi».</p>"
            + why([
                (True, "It describes a long-held explanation, then presents evidence that the explanation was incomplete",
                 "aynan ikki bosqich, va <em>then</em> so'zi ularni to'g'ri tartibda "
                 "bog'laydi. <em>was thought to</em> → eski qarash; "
                 "<em>turned out to be</em> → uni buzadigan dalil."),
                (False, "It compares two species of tree and explains why one is more resilient",
                 "matnda bitta tur bor — sekvoya. Solishtirish umuman yo'q."),
                (False, "It criticises foresters for a policy and proposes an alternative",
                 "<strong>yarim to'g'ri</strong>, va aynan shuning uchun xavfli: siyosat "
                 "haqiqatan noto'g'ri chiqdi. Lekin matn o'rmonchilarni "
                 "<u>ayblamaydi</u> (ular o'sha paytdagi eng yaxshi bilim bilan ish "
                 "ko'rgan) va hech qanday <u>muqobil taklif qilmaydi</u>. "
                 "Variantning ikkinchi yarmi o'ylab topilgan."),
                (False, "It defines a technical term and then gives three examples of its use",
                 "matnda na ta'rif, na uchta misol bor. Bu variant «ilmiy matn "
                 "shunday bo'ladi» degan umumiy tasavvurdan yozilgan."),
            ])
            + "<h4>2-savol — maqsad</h4>"
            + "<p>Bashorat: «bu matn yaxshi niyat bilan qilingan ish nega teskari "
              "natija berganini tushuntirish uchun yozilgan».</p>"
            + why([
                (True, "To explain how a well-meaning policy failed because of an incomplete understanding of the tree",
                 "matnning uchala jumlasini ham qamrab oladi: tushuncha → siyosat → "
                 "muvaffaqiyatsizlik va uning sababi."),
                (False, "To argue that fire suppression should be banned in all forests",
                 "matn hech narsani taklif qilmaydi va <em>all forests</em> haqida "
                 "gapirmaydi — u faqat sekvoya haqida. <strong>Doirasi juda "
                 "keng.</strong>"),
                (False, "To describe the physical structure of sequoia bark in detail",
                 "po'stloq bir marta, bitta bo'lakda eslatilgan. "
                 "<strong>Doirasi juda tor</strong> — bu detalni butun matnning "
                 "maqsadi deb ko'rsatadi."),
                (False, "To compare the germination rates of several conifer species",
                 "yana solishtirish yo'q, va boshqa turlar ham yo'q."),
            ])
            + NOTE.format(
                "Diqqat qiling: ikkala to'g'ri javob ham bir xil matnni tasvirlaydi, "
                "lekin <u>boshqa shaklda</u>. Tuzilish javobi ikki bosqichni "
                "sanaydi; maqsad javobi <em>To explain…</em> deb boshlanadi va "
                "bitta vazifani nomlaydi. Savolni noto'g'ri o'qigan o'quvchi "
                "to'g'ri javobni <u>ikkinchi savolning</u> ro'yxatida qidiradi.")
        )},

        {
            "rich_text": q(
                "<p>Museum conservators once cleaned darkened paintings until the "
                "underlying colours reappeared, treating the discoloured varnish as dirt. "
                "Many now stop well short of that. Analysis of surviving workshop records "
                "has shown that some painters tinted their own varnish deliberately, so "
                "that removing it entirely destroys a layer the artist applied on "
                "purpose.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It presents an older practice, notes that it has changed, and gives the finding that explains the change.", "is_correct": True},
                {"text": "It describes a technique and then lists the materials it requires.", "is_correct": False},
                {"text": "It contrasts the opinions of two conservators about a single painting.", "is_correct": False},
                {"text": "It identifies a problem and then recommends that museums stop cleaning paintings.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Jumlalarni nomlaymiz:</strong> (1) eski amaliyot · "
                "(2) hozir o'zgardi · (3) nega o'zgardi. Uch bosqich, aniq "
                "tartibda.</p>"
                + why([
                    (True, "It presents an older practice, notes that it has changed, and gives the finding that explains the change",
                     "uchala bosqich ham, tartibi ham to'g'ri. <em>once</em> → eski "
                     "amaliyot; <em>Many now stop well short</em> → o'zgarish; "
                     "<em>Analysis … has shown</em> → sabab."),
                    (False, "It describes a technique and then lists the materials it requires",
                     "hech qanday materiallar ro'yxati yo'q. Lak (varnish) eslatilgan, "
                     "lekin u ro'yxat emas."),
                    (False, "It contrasts the opinions of two conservators about a single painting",
                     "matnda ikki mutaxassis ham, bitta aniq rasm ham yo'q — gap "
                     "umumiy amaliyot haqida. <strong>So'z-tuzoq</strong>: "
                     "<em>conservators</em> bor, lekin ikkitasi emas."),
                    (False, "It identifies a problem and then recommends that museums stop cleaning paintings",
                     "<strong>yarim to'g'ri</strong>: muammo bor. Lekin matn hech "
                     "narsa tavsiya qilmaydi, va <em>stop cleaning</em> matnga zid — "
                     "u <em>stop well short</em> deydi, ya'ni tozalashni "
                     "<u>to'xtatmaydi</u>, faqat oxirigacha bormaydi."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Nobody has yet built a machine that folds laundry as quickly as a "
                "person does, though machines have long been able to assemble engines. "
                "The difficulty is that a shirt has no fixed shape: it presents a "
                "different problem each time it is picked up. Tasks that people find "
                "effortless often turn out to be the ones that resist automation "
                "longest.</p>",
                "What is the main purpose of the text?"),
            "choices": [
                {"text": "To use a specific example to introduce a general point about which tasks are hard to automate.", "is_correct": True},
                {"text": "To argue that engineers should devote more resources to household robotics.", "is_correct": False},
                {"text": "To explain the mechanical steps involved in folding a shirt.", "is_correct": False},
                {"text": "To predict that machines will soon match human dexterity.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Shakl:</strong> aniq misol (kir yig'ish) → sabab (ko'ylakning "
                "shakli yo'q) → <mark>umumiy qoida</mark> (oxirgi jumla). Oxirgi jumla "
                "kir haqida emas — u <em>Tasks that people find effortless…</em> deb "
                "boshlanadi, ya'ni misoldan kengroq fikrga chiqadi.</p>"
                "<p>Maqsad savolida <u>oxirgi jumla</u> ko'pincha javobni beradi: "
                "matn nima uchun yozilganini u aytadi.</p>"
                + why([
                    (True, "To use a specific example to introduce a general point about which tasks are hard to automate",
                     "misol → umumiy qoida harakatini to'g'ri nomlaydi, va oxirgi "
                     "jumlaning kengaytirilgan da'vosini qamrab oladi."),
                    (False, "To argue that engineers should devote more resources to household robotics",
                     "matn hech narsa talab qilmaydi. Bu — o'quvchi qo'shib "
                     "yuboradigan tavsiya."),
                    (False, "To explain the mechanical steps involved in folding a shirt",
                     "<strong>doirasi juda tor</strong> va noto'g'ri: matn kir yig'ish "
                     "bosqichlarini umuman tavsiflamaydi, u faqat nega qiyinligini "
                     "aytadi."),
                    (False, "To predict that machines will soon match human dexterity",
                     "aksincha — matn bu vazifalar avtomatlashtirishga "
                     "<em>longest</em> qarshilik qilishini aytyapti."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>The letters were catalogued as forgeries in 1907 and left in a drawer "
                "for eighty years. When the paper was finally tested, the fibres and the "
                "ink both proved consistent with the claimed date. The catalogue entry has "
                "not been corrected, because the volume in which it appears is itself "
                "considered a historical document.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It reports a judgement, reports the evidence that overturned it, and notes a consequence that has not followed.", "is_correct": True},
                {"text": "It presents a mystery and then reveals the identity of the forger.", "is_correct": False},
                {"text": "It describes a scientific method and then evaluates its reliability.", "is_correct": False},
                {"text": "It recounts a dispute between archivists and eventually takes a side.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Uch jumla, uch harakat:</strong> (1) hukm — soxta deb "
                "belgilandi · (2) dalil — sinov hukmni buzdi · (3) va shunga qaramay "
                "katalog o'zgarmadi.</p>"
                "<p>Uchinchi harakat — g'alati va aynan shuning uchun muhim. "
                "Tuzilish javobi uni <mark>o'z ichiga olishi shart</mark>: "
                "matnning uchdan biri o'sha haqda.</p>"
                + why([
                    (True, "It reports a judgement, reports the evidence that overturned it, and notes a consequence that has not followed",
                     "uchala harakatni ham qamraydi, jumladan oxirgi burilishni: "
                     "kutilgan tuzatish <u>bo'lmadi</u>."),
                    (False, "It presents a mystery and then reveals the identity of the forger",
                     "soxtakorning kimligi umuman muhokama qilinmaydi — va matnga "
                     "ko'ra soxtalik yo'q ham edi."),
                    (False, "It describes a scientific method and then evaluates its reliability",
                     "sinov bir og'iz bilan eslatilgan (<em>the fibres and the ink</em>), "
                     "usul tavsiflanmagan va uning ishonchliligi baholanmagan. "
                     "<strong>Doirasi juda tor.</strong>"),
                    (False, "It recounts a dispute between archivists and eventually takes a side",
                     "<strong>yarim to'g'ri</strong> tuzog'i: ziddiyat bor "
                     "(katalog ↔ dalil), lekin bu odamlar o'rtasidagi bahs emas, va "
                     "matn hech kimning tarafini olmaydi. Variantning ikkinchi yarmi "
                     "o'ylab topilgan."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Beekeepers in the valley have kept the same local subspecies for "
                "generations, and their hives come through winters that kill imported "
                "bees outright. A survey of forty apiaries found that the local stock "
                "also carries heavier mite loads than the imported bees do, apparently "
                "without harm. Whether that tolerance is inherited or acquired through "
                "long exposure is not yet known.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It describes a local practice, reports a finding about it, and notes a question the finding leaves open.", "is_correct": True},
                {"text": "It compares the honey yields of local and imported bees.", "is_correct": False},
                {"text": "It recommends that beekeepers elsewhere adopt the local subspecies.", "is_correct": False},
                {"text": "It explains how mites damage a hive over the course of a winter.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Jumlalarni nomlaymiz:</strong> (1) mahalliy amaliyot va u "
                "ishlashi \u00b7 (2) so\u2018rov topgan yangi fakt \u00b7 (3) ochiq qolgan savol. "
                "Uchinchi harakat \u2014 <em>is not yet known</em> \u2014 6-shaklning "
                "cheklov bosqichi (21-dars).</p>"
                + why([
                    (True, "It describes a local practice, reports a finding about it, and notes a question the finding leaves open",
                     "uchala harakat ham, tartibi ham to\u2018g\u2018ri, va oxirgi bo\u2018lak "
                     "matnning ochiq savol bilan tugashini qamrab oladi."),
                    (False, "It compares the honey yields of local and imported bees",
                     "asal hosili umuman eslatilmaydi. Ikki turdagi asalari bor, "
                     "lekin ular <u>qishga chidamliligi</u> bo\u2018yicha solishtirilgan."),
                    (False, "It recommends that beekeepers elsewhere adopt the local subspecies",
                     "matn hech narsa tavsiya qilmaydi \u2014 aksincha, u sababni hali "
                     "bilmasligini tan oladi. <strong>O\u2018quvchi qo\u2018shib yuboradigan "
                     "tavsiya.</strong>"),
                    (False, "It explains how mites damage a hive over the course of a winter",
                     "kanalar zarari tushuntirilmaydi \u2014 matn mahalliy asalarilar "
                     "ularga <u>chidayotganini</u> aytadi. <strong>So\u2018z-tuzoq.</strong>"),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">overall structure</div><div class="pp-card-back">matnning umumiy tuzilishi, shakli</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">main purpose</div><div class="pp-card-back">asosiy maqsad, vazifa</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a long-held explanation</div><div class="pp-card-back">uzoq vaqt qabul qilingan tushuntirish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to overturn (a judgement)</div><div class="pp-card-back">(hukmni) ag\'darmoq, bekor qilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">incomplete understanding</div><div class="pp-card-back">to\'liq bo\'lmagan tushuncha</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to stop short of ~</div><div class="pp-card-back">~ gacha bormay to\'xtamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to resist automation</div><div class="pp-card-back">avtomatlashtirishga qarshilik qilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">well-meaning</div><div class="pp-card-back">yaxshi niyatli</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Structure</strong> = shakl («avval …, keyin …»); "
              "<strong>purpose</strong> = vazifa («To …»).</li>"
              "<li>Variantlarning shaklidan savol turini tekshiring.</li>"
              "<li>Har jumlani <u>bitta so'z bilan nomlang</u>, keyin burilishni "
              "toping.</li>"
              "<li>Variantni <strong>oxirigacha</strong> o'qing — tuzoq odatda "
              "ikkinchi yarmida.</li>"
              "<li>Maqsad savolida oxirgi jumla ko'pincha javobni beradi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 21
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_TSP,
    "title": "SAT R&W 21: Naming the Shape of a Text",
    "summary": "SAT parchalari oltita takrorlanuvchi shakldan biriga tushadi; shaklni "
               "besh so'zda nomlash tuzilish savolini deyarli avtomatik yechadi.",
    "order": 21,
    "blocks": [
        {"rich_text": (
            "<h2>Oltita shakl — va tamom</h2>"
            "<p>SAT parchalari 25–150 so'zdan iborat. Bunday qisqa matnda cheksiz "
            "ko'p tuzilish bo'lishi mumkin emas — joy yetmaydi. Amalda ular "
            "<mark>oltita shakldan biriga</mark> tushadi.</p>"
            "<p>Bu ajoyib yangilik: shakllarni tanib olsangiz, tuzilish savoliga "
            "javobni matnni <u>tugatmasdan oldin</u> bilib olasiz.</p>"
            + '<span class="sr-time">⏱ Shakl tanilsa: ~40 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Oltita shakl</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Shakl</th><th>Qanday bilinadi</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>1. Eski qarash → yangi dalil</strong></td>"
              "<td><em>was long thought · used to be described · turns out · "
              "recent measurements</em></td></tr>"
              "<tr><td><strong>2. Da'vo → dalil</strong></td>"
              "<td>Birinchi jumla da'vo, qolgani uni ko'taradi: "
              "<em>for instance · in one study</em></td></tr>"
              "<tr><td><strong>3. Muammo → yechim</strong></td>"
              "<td><em>the difficulty is · to address this · a new approach</em></td></tr>"
              "<tr><td><strong>4. Umumiy → aniq</strong> (yoki teskarisi)</td>"
              "<td>Keng qoida, keyin bitta misol — yoki bitta misol, keyin keng "
              "qoida</td></tr>"
              "<tr><td><strong>5. Ikkitasini solishtirish</strong></td>"
              "<td>Ikki odam, ikki usul, ikki davr: <em>whereas · unlike · by "
              "contrast</em></td></tr>"
              "<tr><td><strong>6. Kuzatuv → tushuntirish → cheklov</strong></td>"
              "<td>Uchinchi harakat javobni yumshatadi: <em>although it remains "
              "unclear · does not prove</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "1-shakl SAT'ning eng sevimlisi. <em>was thought</em>, "
                "<em>long assumed</em>, <em>traditionally described</em> iboralarini "
                "ko'rsangiz — matnning ikkinchi yarmida <u>albatta</u> burilish "
                "bo'ladi, va tuzilish javobi o'sha burilishni nomlashi kerak.")
        )},

        {"rich_text": (
            "<h3>Besh so'zli qoida</h3>"
            "<p>Matnni o'qib bo'lgach, variantlarga qaramasdan, shaklni "
            "<strong>besh so'zdan oshmagan</strong> holda ayting. O'zbekcha bo'lsin:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\">«Eski qarash, keyin uni buzgan dalil.»<br>"
                "«Muammo aytiladi, keyin yechim.»<br>"
                "«Bitta misol, keyin umumiy qoida.»<br>"
                "«Kuzatuv, sabab, keyin ehtiyotkorlik.»</p>")
            + "<p>Nega besh so'z? Chunki uzunroq bashorat — bu <u>qayta hikoya "
              "qilish</u>, va qayta hikoya sizni har variantda «tanish» "
              "bo'laklarni ko'rishga majbur qiladi. Qisqa bashorat esa qattiq "
              "filtr bo'lib ishlaydi.</p>"
            + WARN.format(
                "Shaklni <u>matnning mavzusi</u> bilan adashtirmang. «Sekvoya va "
                "yong'in haqida» — bu mavzu, shakl emas. Shakl har doim "
                "<strong>harakatlar</strong>ni sanaydi: nima qilindi, keyin nima "
                "qilindi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + q(
                "<p>Sourdough bread rises without added yeast because flour and water "
                "left together collect wild yeasts and bacteria from the grain and the "
                "air. Bakers have known how to keep such a culture alive for thousands of "
                "years. What they could not know is which organisms were in it: the "
                "sequencing studies that identified them are barely two decades old, and "
                "they found that no two cultures, even in the same bakery, contain quite "
                "the same mixture.</p>",
                "Which choice best describes the overall structure of the text?")
            + choices_html([
                "It gives instructions for maintaining a sourdough culture and warns "
                "against common errors.",
                "It explains a long-established practice, then describes recent work that "
                "revealed something practitioners could not have known.",
                "It compares bread made with wild yeast to bread made with commercial "
                "yeast.",
                "It argues that sequencing studies have made traditional baking knowledge "
                "obsolete.",
            ])
            + "<p><strong>Besh so'zli bashorat:</strong> «Eski amaliyot, keyin yangi "
              "kashfiyot.» — 1-shaklning bir varianti. Burilish aniq: "
              "<em>What they could not know is …</em></p>"
            + why([
                (True, "It explains a long-established practice, then describes recent work that revealed something practitioners could not have known",
                 "ikki bosqich va ularning tartibi to'g'ri, va «amaliyotchilar "
                 "bilolmagan narsa» bo'lagi matnning o'z burilishini "
                 "(<em>What they could not know</em>) aynan takrorlaydi."),
                (False, "It gives instructions for maintaining a sourdough culture and warns against common errors",
                 "matnda birorta ko'rsatma ham, ogohlantirish ham yo'q. "
                 "<em>keep such a culture alive</em> iborasi bor, lekin u faktni "
                 "aytadi, o'rgatmaydi."),
                (False, "It compares bread made with wild yeast to bread made with commercial yeast",
                 "sanoat xamirturushi bir marta, inkor shaklida eslatilgan "
                 "(<em>without added yeast</em>) — bu solishtirish emas. "
                 "<strong>So'z-tuzoq.</strong>"),
                (False, "It argues that sequencing studies have made traditional baking knowledge obsolete",
                 "<strong>yarim to'g'ri</strong>: sekvenatsiya tadqiqotlari bor. "
                 "Lekin matn an'anaviy bilimni eskirgan deb <u>aytmaydi</u> — "
                 "aksincha, novvoylar ming yillar davomida muvaffaqiyatli ishlagan. "
                 "Variantning ikkinchi yarmi o'ylab topilgan."),
            ])
        )},

        {
            "rich_text": q(
                "<p>A city that wants fewer cars in its centre can raise the price of "
                "parking or it can improve the buses, and for years the two were treated "
                "as alternatives. Cities that tried only the first found that drivers "
                "paid and kept driving. Cities that tried only the second found that the "
                "new buses filled with people who had previously walked. Where traffic "
                "actually fell, both had been done at once.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It presents two options, shows that each fails alone, and identifies what worked instead.", "is_correct": True},
                {"text": "It argues that raising parking prices is more effective than improving buses.", "is_correct": False},
                {"text": "It describes a policy and then lists the cities that have adopted it.", "is_correct": False},
                {"text": "It traces the history of urban traffic management from its origins.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Besh so'zli bashorat:</strong> «Ikki yechim, ikkovi ham "
                "yolg'iz ishlamaydi, birga ishlaydi.» Matnning to'rt jumlasi aniq "
                "to'rt harakat.</p>"
                + why([
                    (True, "It presents two options, shows that each fails alone, and identifies what worked instead",
                     "uchala harakatni ham qamraydi. <em>Where traffic actually fell, "
                     "both had been done at once</em> — uchinchi harakatning isboti."),
                    (False, "It argues that raising parking prices is more effective than improving buses",
                     "matn ikkovini <u>bir-biriga qarshi qo'ymaydi</u>: ikkalasi ham "
                     "yolg'iz muvaffaqiyatsiz chiqqan. Bu variant matnning asosiy "
                     "xulosasini teskari qiladi."),
                    (False, "It describes a policy and then lists the cities that have adopted it",
                     "birorta shahar nomi yo'q — matn <em>Cities that tried…</em> deb "
                     "umumiy gapiradi. Ro'yxat yo'q."),
                    (False, "It traces the history of urban traffic management from its origins",
                     "<em>for years</em> iborasi tarix hidini beradi va shuning uchun "
                     "bu variant jozibali. Lekin matnda na sana, na kelib chiqish, na "
                     "bosqichma-bosqich rivojlanish bor."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Rivers that carry a heavy load of sediment do not run in straight "
                "lines for long. A small bend sends the fastest water to the outer bank, "
                "which is eroded, while the slower water on the inner bank drops what it "
                "is carrying; the bend therefore deepens itself. Left alone, a river will "
                "eventually cut through the neck of a loop and abandon it, leaving a "
                "curved lake beside the new channel.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It states a general tendency, explains the mechanism behind it, and describes where the process ends.", "is_correct": True},
                {"text": "It compares rivers that carry sediment with rivers that do not.", "is_correct": False},
                {"text": "It identifies a problem caused by erosion and proposes a way to prevent it.", "is_correct": False},
                {"text": "It defines three technical terms and gives an example of each.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Besh so'zli bashorat:</strong> «Qoida, keyin mexanizm, "
                "keyin oxirgi natija.» — 6-shaklning yaqin qarindoshi.</p>"
                "<p>Jumlalarni nomlaymiz: (1) umumiy tendensiya · (2) nega shunday "
                "bo'ladi · (3) jarayon nima bilan tugaydi.</p>"
                + why([
                    (True, "It states a general tendency, explains the mechanism behind it, and describes where the process ends",
                     "uchala jumla, uchala harakat, to'g'ri tartibda. <em>Left alone, a "
                     "river will eventually…</em> uchinchi harakatning ochiq belgisi."),
                    (False, "It compares rivers that carry sediment with rivers that do not",
                     "cho'kindisiz daryolar eslatilmaydi ham. Birinchi jumla shart "
                     "qo'yadi, solishtirish qilmaydi."),
                    (False, "It identifies a problem caused by erosion and proposes a way to prevent it",
                     "<strong>yarim to'g'ri</strong>: eroziya bor. Lekin matn uni "
                     "muammo deb atamaydi (bu tabiiy jarayon), va hech qanday "
                     "oldini olish usuli taklif qilmaydi. Ikkinchi yarmi o'ylab "
                     "topilgan."),
                    (False, "It defines three technical terms and gives an example of each",
                     "matnda birorta atama ta'riflanmaydi — hatto hosil bo'lgan "
                     "ko'lning nomi ham aytilmaydi (<em>a curved lake</em>)."),
                ])
                + NOTE.format(
                    "Oxirgi variant qanday yozilganini payqang: «uchta atama, uchta "
                    "misol» — juda aniq eshitiladi. <strong>Aniqlik "
                    "ishonchlilik emas.</strong> Sanoq bo'lgan variantni har doim "
                    "sanab tekshiring: rostdan uchtami?")
            ),
        },

        {
            "rich_text": q(
                "<p>The first photographs of the ocean floor were made in the 1890s with "
                "a camera lowered on a cable and fired blind. Almost all of them were "
                "useless. But one, taken off the coast of Greece, showed ripples in the "
                "mud identical to those left by waves in shallow water — at a depth where "
                "no wave could reach. The explanation, that slow currents move along the "
                "sea floor, was not accepted for another fifty years.</p>",
                "What is the main purpose of the text?"),
            "choices": [
                {"text": "To describe how a single early result anticipated an idea that took decades to be accepted.", "is_correct": True},
                {"text": "To explain the technical limitations of nineteenth-century underwater cameras.", "is_correct": False},
                {"text": "To argue that early oceanographers were unfairly dismissed by their colleagues.", "is_correct": False},
                {"text": "To describe how ripples form in shallow water.", "is_correct": False},
            ],
            "explanation": (
                "<p>Maqsad savoli, shuning uchun javob <em>To …</em> bilan boshlanadi "
                "va bitta vazifani nomlaydi.</p>"
                "<p><strong>Matnning yuragi:</strong> <em>But one … showed ripples … "
                "at a depth where no wave could reach</em>, va oxiri: "
                "<em>was not accepted for another fifty years</em>. Ikki fakt birga "
                "<mark>«bitta erta natija o'z vaqtidan oldin bo'ldi»</mark> "
                "degan fikrni yasaydi.</p>"
                + why([
                    (True, "To describe how a single early result anticipated an idea that took decades to be accepted",
                     "matnning ikkala kalit faktini ham qamraydi: <em>one</em> foydali "
                     "surat, va ellik yillik kechikish."),
                    (False, "To explain the technical limitations of nineteenth-century underwater cameras",
                     "<strong>doirasi juda tor.</strong> Kamera va <em>fired blind</em> "
                     "birinchi jumlada, lekin matn u yerda to'xtamaydi — asosiy fikr "
                     "keyin keladi. Birinchi jumladan yozilgan variant deyarli har "
                     "doim shu tuzoq."),
                    (False, "To argue that early oceanographers were unfairly dismissed by their colleagues",
                     "matn hech kimni ayblamaydi va «adolatsiz» degan baho bermaydi — "
                     "u shunchaki g'oyaning qabul qilinishi uzoq davom etganini "
                     "aytadi. <strong>O'quvchi qo'shib yuboradigan hikoya.</strong>"),
                    (False, "To describe how ripples form in shallow water",
                     "sayoz suvdagi to'lqin izlari faqat <u>taqqoslash uchun</u> "
                     "eslatilgan. Ularning qanday hosil bo'lishi umuman "
                     "tushuntirilmaydi."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>A dictionary that records how people actually speak will end up "
                "listing meanings its own editors dislike. One that records how people "
                "ought to speak will be out of date within a generation, because the "
                "usages it condemns are so often the ones that win. Most modern "
                "dictionaries take the first course and attach a usage note to the "
                "disputed entries, which satisfies neither camp.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It sets out two approaches, gives the drawback of each, and describes the compromise generally adopted.", "is_correct": True},
                {"text": "It argues that dictionaries should stop recording disputed usages.", "is_correct": False},
                {"text": "It traces the way the meaning of a single word changed over time.", "is_correct": False},
                {"text": "It defines two kinds of dictionary and gives an example of each.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Besh so\u2018zli bashorat:</strong> \u00abIkki yo\u2018l, ikkovining "
                "kamchiligi, keyin murosa.\u00bb \u2014 5-shakl (solishtirish) va uning "
                "yechimi.</p>"
                + why([
                    (True, "It sets out two approaches, gives the drawback of each, and describes the compromise generally adopted",
                     "uchala harakat ham bor. Kamchiliklar: <em>meanings its own "
                     "editors dislike</em> va <em>out of date within a generation</em>; "
                     "murosa: <em>attach a usage note</em>."),
                    (False, "It argues that dictionaries should stop recording disputed usages",
                     "teskari: matnga ko\u2018ra zamonaviy lug\u2018atlar aynan yozib "
                     "boradigan yo\u2018lni tanlaydi. Va matn hech narsa talab qilmaydi."),
                    (False, "It traces the way the meaning of a single word changed over time",
                     "birorta aniq so\u2018z olinmagan \u2014 gap lug\u2018at tuzish "
                     "tamoyillari haqida. <strong>Doirasi butunlay boshqa.</strong>"),
                    (False, "It defines two kinds of dictionary and gives an example of each",
                     "<strong>yarim to\u2018g\u2018ri</strong> va sanoq bilan aldaydi: ikki tur "
                     "haqiqatan tasvirlangan, lekin birorta lug\u2018at nomi "
                     "keltirilmagan. Sanoq bo\u2018lgan variantni sanab tekshiring."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a general tendency</div><div class="pp-card-back">umumiy tendensiya, qonuniyat</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the mechanism behind ~</div><div class="pp-card-back">~ ning ortidagi mexanizm</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to anticipate an idea</div><div class="pp-card-back">g\'oyani o\'z vaqtidan oldin ilg\'amoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">long-established</div><div class="pp-card-back">uzoqdan beri o\'rnashgan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">practitioners</div><div class="pp-card-back">amaliyotchilar, kasb egalari</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">alternatives</div><div class="pp-card-back">bir-birini istisno qiladigan variantlar</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to abandon (a loop)</div><div class="pp-card-back">(halqani) tashlab ketmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">obsolete</div><div class="pp-card-back">eskirgan, keraksiz bo\'lib qolgan</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Oltita shakl: eski→yangi · da'vo→dalil · muammo→yechim · "
              "umumiy↔aniq · solishtirish · kuzatuv→sabab→cheklov.</li>"
              "<li>Shaklni <strong>besh so'zda</strong> ayting — uzun bashorat "
              "filtr bo'lolmaydi.</li>"
              "<li>Shakl <u>harakatlarni</u> sanaydi, mavzuni emas.</li>"
              "<li>Sanoq bo'lgan variantni (<em>three examples</em>) sanab "
              "tekshiring.</li>"
              "<li>Faqat birinchi jumladan yozilgan variant — doimiy tuzoq.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 22
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_TSP,
    "title": "SAT R&W 22: The Function of One Underlined Sentence",
    "summary": "Tagi chizilgan jumla nima ish qilyapti: da'vo, dalil, cheklov, e'tiroz, "
               "misol yoki o'tish — javobni jumlaning o'zi emas, qo'shnilari beradi.",
    "order": 22,
    "blocks": [
        {"rich_text": (
            "<h2>Bitta jumlaning vazifasi</h2>"
            "<p>Bu savol turi ekranda shunday keladi: matn ichida bitta jumlaning tagi "
            "chizilgan, va savol — <em>What is the main purpose of the underlined "
            "sentence?</em> yoki <em>Which choice best describes the function of the "
            "underlined sentence in the text as a whole?</em></p>"
            "<p>Bu yerda bitta qoida hamma narsani hal qiladi:</p>"
            + EXAMP.format(
                "<p style=\"font-size:1.08em;margin:0;\"><strong>Javob tagi chizilgan "
                "jumlaning ichida emas — uning <u>qo'shnilarida</u>.</strong> "
                "«Vazifa» degani — bu jumla <u>o'zidan oldingi va keyingi</u> jumlalar "
                "uchun nima qilyapti. Yolg'iz o'qilgan jumla hech qanday vazifaga ega "
                "emas.</p>")
            + '<span class="sr-time">⏱ ~55 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Usul — «o'chirish sinovi»</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Oldingi jumlani o'qing va "
              "nomlang.</strong> Nima qildi? Da'vo qildimi, savol qo'ydimi, fakt "
              "berdimi?</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Keyingi jumlani o'qing va "
              "nomlang.</strong> U nima qilyapti?</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. O'chirish sinovi.</strong> Tagi "
              "chizilgan jumlani xayolan o'chiring. Matn nimani <u>yo'qotadi</u>? "
              "O'sha yo'qolgan narsa — jumlaning vazifasi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>4. Vazifani fe'l bilan ayting.</strong> "
              "«dalil keltiradi», «da'voni cheklaydi», «e'tirozni oldindan "
              "aytadi», «keyingi qismga o'tkazadi».</p></div>"
            + '</div>'
            + TIP.format(
                "3-qadam — o'chirish sinovi — bu turdagi eng kuchli quroling. "
                "Agar jumlani o'chirganingizda matn hech nimani yo'qotmasa, "
                "demak siz uning vazifasini noto'g'ri tushungansiz: SAT vazifasiz "
                "jumlaning tagini chizmaydi.")
        )},

        {"rich_text": (
            "<h3>Eng ko'p uchraydigan vazifalar</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Vazifa</th><th>Belgisi</th></tr></thead>"
              "<tbody>"
              "<tr><td>Da'voni bayon qiladi</td><td>Matnning asosiy fikri, qolgani "
              "uni ko'taradi</td></tr>"
              "<tr><td>Dalil keltiradi</td><td>Raqam, tadqiqot, misol — oldingi "
              "da'voni ko'tarish uchun</td></tr>"
              "<tr><td>Da'voni cheklaydi (qualifies)</td><td><em>although · only · in "
              "some cases · does not prove</em></td></tr>"
              "<tr><td>E'tirozni tan oladi (concedes)</td><td><em>admittedly · to be "
              "sure · it is true that</em></td></tr>"
              "<tr><td>Muammoni qo'yadi</td><td>Keyingi jumlalar unga javob beradi</td></tr>"
              "<tr><td>Atamani tushuntiradi</td><td>Ta'rif yoki qayta ifodalash</td></tr>"
              "<tr><td>Qarama-qarshilikni ko'rsatadi</td><td>Kutilgan va haqiqiy "
              "natijani yonma-yon qo'yadi</td></tr>"
              "<tr><td>O'tish yasaydi</td><td>Bir mavzuni yopib, ikkinchisini "
              "ochadi</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "Eng ko'p uchraydigan noto'g'ri javob: <strong>jumlaning mazmunini "
                "qayta aytish</strong>. «U termitlar uyasining ichidagi havo "
                "harakatini tasvirlaydi» — bu rost bo'lishi mumkin, lekin bu "
                "<u>vazifa emas</u>, bu shunchaki tarjima. Vazifa har doim "
                "jumlaning <u>matndagi ishi</u>ni aytadi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + q(
                "<p>Advertisements for memory-training apps often cite studies showing "
                "that users improve at the exercises the apps contain. "
                "<span class=\"sr-focus\">Improvement on a trained task, however, is the "
                "one result such a study is guaranteed to produce.</span> The question "
                "that matters is whether the gain shows up anywhere else — in recalling a "
                "shopping list, say, or a name — and on that question the evidence has so "
                "far been thin.</p>",
                "What is the main purpose of the underlined sentence?")
            + choices_html([
                "It explains how memory-training apps are designed.",
                "It points out that the evidence being cited cannot show what it is being "
                "used to suggest.",
                "It concedes that memory-training apps produce genuine benefits.",
                "It introduces a study that contradicts the advertisers' claims.",
            ])
            + "<p><strong>1-qadam — oldingi jumla:</strong> reklamalar tadqiqotlarga "
              "havola qiladi (foydalanuvchilar mashqlarda yaxshilanadi).</p>"
            + "<p><strong>2-qadam — keyingi jumla:</strong> «asl savol — bu foyda "
              "boshqa joyda ko'rinadimi», va dalil kam.</p>"
            + "<p><strong>3-qadam — o'chirish sinovi:</strong> tagi chizilgan jumlani "
              "olib tashlasak, reklamaning dalili bilan mualliflarning shubhasi "
              "o'rtasida <u>bo'shliq</u> qoladi. Yo'qolgan narsa — nega o'sha dalil "
              "hech nimani isbotlamasligi. Vazifa: <mark>keltirilgan dalilning "
              "kuchsizligini ko'rsatish</mark>.</p>"
            + why([
                (True, "It points out that the evidence being cited cannot show what it is being used to suggest",
                 "aynan o'chirish sinovi topgan bo'shliq. <em>is guaranteed to "
                 "produce</em> — «bu natija baribir chiqadi», ya'ni u hech nimani "
                 "isbotlamaydi."),
                (False, "It explains how memory-training apps are designed",
                 "<strong>mazmunni qayta aytish</strong> tuzog'i, va u ham "
                 "noto'g'ri: jumla ilovaning tuzilishi haqida emas, "
                 "<u>tadqiqotning</u> tuzilishi haqida."),
                (False, "It concedes that memory-training apps produce genuine benefits",
                 "<strong>teskari.</strong> Jumla foydani tan olmayapti — u foyda "
                 "deb ko'rsatilgan narsa avtomatik natija ekanini aytyapti. "
                 "<em>however</em> so'zi yo'nalishni allaqachon aytib turibdi."),
                (False, "It introduces a study that contradicts the advertisers' claims",
                 "<strong>yarim to'g'ri</strong>: jumla reklamachilarga qarshi. "
                 "Lekin u birorta yangi tadqiqotni <u>keltirmaydi</u> — u mavjud "
                 "tadqiqotlarning mantiqi haqida gapiryapti. Ikkinchi yarmi o'ylab "
                 "topilgan."),
            ])
        )},

        {
            "rich_text": q(
                "<p>Restoring a wetland is usually described as putting the water back. "
                "In practice the water is the easy part. <span class=\"sr-focus\">The "
                "seed bank in the soil, which determines what will actually grow, may "
                "have been destroyed decades earlier by ploughing.</span> Projects that "
                "flood a drained field and wait often get reed and little else, and "
                "restoration teams now budget for replanting from the "
                "beginning.</p>",
                "What is the main purpose of the underlined sentence?"),
            "choices": [
                {"text": "It identifies the obstacle that explains why the simple approach described earlier does not work.", "is_correct": True},
                {"text": "It provides a definition of the term “seed bank” for readers unfamiliar with it.", "is_correct": False},
                {"text": "It criticises farmers for having ploughed wetland soils.", "is_correct": False},
                {"text": "It summarises the results of a specific restoration project.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Qo'shnilar:</strong> oldin — «suv oson qism». Keyin — "
                "«suv quygan loyihalar faqat qamish oladi, shuning uchun endi qayta "
                "ekishga pul ajratiladi».</p>"
                "<p><strong>O'chirish sinovi:</strong> jumlani olib tashlasak, "
                "«suv oson» bilan «faqat qamish chiqadi» orasidagi <u>sabab</u> "
                "yo'qoladi. Vazifa: <mark>to'siqni nomlash</mark>.</p>"
                + why([
                    (True, "It identifies the obstacle that explains why the simple approach described earlier does not work",
                     "o'chirish sinovi topgan bo'shliqni to'ldiradi: urug' banki yo'q "
                     "bo'lgani uchun suv yetarli emas."),
                    (False, "It provides a definition of the term “seed bank” for readers unfamiliar with it",
                     "jumla ichida qisqa izoh bor (<em>which determines what will "
                     "actually grow</em>), shuning uchun bu variant jozibali. Lekin "
                     "izoh — jumlaning <u>bir bo'lagi</u>, uning matndagi vazifasi "
                     "emas. Ta'rif berish uchun qolgan ikki jumla kerak emasdi."),
                    (False, "It criticises farmers for having ploughed wetland soils",
                     "matn hech kimni ayblamaydi — <em>by ploughing</em> sababni "
                     "aytadi, hukm chiqarmaydi. <strong>O'quvchi qo'shib "
                     "yuboradigan hikoya.</strong>"),
                    (False, "It summarises the results of a specific restoration project",
                     "aniq loyiha yo'q; <em>Projects that flood a drained field</em> "
                     "— umumiy gap, va u <u>keyingi</u> jumlada."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>The manuscript's marginal notes have been read as a reader's "
                "objections to the text. <span class=\"sr-focus\">They are written in "
                "three distinct hands, however, and one of them also appears in the main "
                "body.</span> A scribe correcting his own work leaves a different kind of "
                "trace from a reader arguing with a book, and the two have probably been "
                "confused here.</p>",
                "Which choice best describes the function of the underlined sentence in the text as a whole?"),
            "choices": [
                {"text": "It presents the physical evidence on which the passage's reinterpretation rests.", "is_correct": True},
                {"text": "It restates the conventional reading of the marginal notes in clearer terms.", "is_correct": False},
                {"text": "It acknowledges that the conventional reading is probably correct.", "is_correct": False},
                {"text": "It explains why the manuscript has been difficult for scholars to date.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Qo'shnilar:</strong> oldin — an'anaviy o'qish (chetdagi "
                "izohlar = o'quvchining e'tirozlari). Keyin — xulosa: kotib va "
                "o'quvchi chalkashtirilgan.</p>"
                "<p><strong>O'chirish sinovi:</strong> jumlani olib tashlasak, "
                "oxirgi jumlaning <u>asosi</u> qolmaydi — nega chalkashlik deb "
                "o'ylaymiz? Vazifa: <mark>yangi talqinning dalilini berish</mark>.</p>"
                + why([
                    (True, "It presents the physical evidence on which the passage's reinterpretation rests",
                     "uchta qo'l va ulardan birining asosiy matnda uchrashi — bu "
                     "jismoniy dalil, va oxirgi jumla to'liq shunga tayanadi."),
                    (False, "It restates the conventional reading of the marginal notes in clearer terms",
                     "<em>however</em> so'zi bu variantni darrov o'ldiradi: jumla "
                     "an'anaviy o'qishni takrorlamayapti, unga <u>qarshi</u> "
                     "turibdi."),
                    (False, "It acknowledges that the conventional reading is probably correct",
                     "yana <em>however</em>ga zid, va oxirgi jumla an'anaviy "
                     "o'qishni rad etadi."),
                    (False, "It explains why the manuscript has been difficult for scholars to date",
                     "sana aniqlash matnda umuman muhokama qilinmaydi. "
                     "<strong>Qo'lyozma → sana</strong> degan assotsiatsiyadan "
                     "yozilgan tuzoq."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Anvar's grandmother had refused a telephone for thirty years, and "
                "when one was finally installed she used it as though each call cost a "
                "day's wages. <span class=\"sr-focus\">She would state her business in a "
                "single sentence, wait for the answer, and hang up before it was "
                "finished.</span> Anvar found this comic until he understood that she was "
                "sparing the person at the other end, who might have work to get back "
                "to.</p>",
                "What is the main purpose of the underlined sentence?"),
            "choices": [
                {"text": "It gives the concrete behaviour that the sentences on either side interpret.", "is_correct": True},
                {"text": "It explains why the grandmother had refused a telephone for so long.", "is_correct": False},
                {"text": "It establishes that the grandmother disliked speaking to Anvar.", "is_correct": False},
                {"text": "It shows that the grandmother had difficulty using unfamiliar technology.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Qo'shnilar:</strong> oldin — umumiy tavsif "
                "(<em>as though each call cost a day's wages</em>). Keyin — Anvarning "
                "ikki xil talqini (avval kulgili, keyin — mehribonlik).</p>"
                "<p><strong>O'chirish sinovi:</strong> jumlani olib tashlasak, ikkala "
                "qo'shni ham <u>nimani</u> izohlayotgani noma'lum bo'lib qoladi. "
                "Vazifa: <mark>talqin qilinadigan aniq xatti-harakatni berish</mark>.</p>"
                + why([
                    (True, "It gives the concrete behaviour that the sentences on either side interpret",
                     "jumla yagona konkret harakatni tasvirlaydi, va ikkala qo'shni "
                     "ham unga tayanadi — biri umumlashtiradi, biri sababini topadi."),
                    (False, "It explains why the grandmother had refused a telephone for so long",
                     "rad etish sababi matnda umuman aytilmaydi. Bu jumla "
                     "telefondan <u>foydalanish</u> usulini ko'rsatadi, undan "
                     "voz kechish sababini emas."),
                    (False, "It establishes that the grandmother disliked speaking to Anvar",
                     "matn buni <strong>ataylab rad etadi</strong>: oxirgi jumla "
                     "uning maqsadi mehribonlik ekanini aytadi, va telefonda gaplashgan "
                     "odam har doim Anvar ham emas."),
                    (False, "It shows that the grandmother had difficulty using unfamiliar technology",
                     "<strong>o'quvchi qo'shib yuboradigan hikoya</strong>: keksa "
                     "odam + yangi texnika = qiynaladi. Lekin matnga ko'ra u "
                     "telefondan mukammal, ataylab shunday foydalanyapti — "
                     "qiynalayotgani yo'q."),
                ])
                + TIP.format(
                    "Adabiy parchada bu savol deyarli har doim shu shaklda keladi: "
                    "tagi chizilgan jumla <u>konkret harakat</u>ni beradi, "
                    "qo'shnilari esa uni <u>talqin qiladi</u>. Personajning "
                    "xarakteri haqidagi keng xulosalar (<em>disliked</em>, "
                    "<em>had difficulty</em>) esa deyarli har doim tuzoq.")
            ),
        },

        {
            "rich_text": q(
                "<p>The comet was photographed on four nights in 1861 and has not been "
                "seen since. <span class=\"sr-focus\">Its orbit, calculated from those "
                "four positions alone, carries an uncertainty of several decades at the "
                "far end of the loop.</span> Astronomers hoping to recover it therefore "
                "search a window of years rather than a date, and a failure to find it in "
                "any particular season proves very little.</p>",
                "What is the main purpose of the underlined sentence?"),
            "choices": [
                {"text": "It supplies the technical fact that accounts for the search method described next.", "is_correct": True},
                {"text": "It explains why the comet was never photographed after 1861.", "is_correct": False},
                {"text": "It suggests that the original 1861 observations were made carelessly.", "is_correct": False},
                {"text": "It establishes that the comet is unlikely ever to be seen again.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Qo\u2018shnilar:</strong> oldin \u2014 kometa 1861-yilda to\u2018rt "
                "kecha suratga olingan va boshqa ko\u2018rinmagan. Keyin \u2014 "
                "<em>therefore</em> bilan boshlanadigan usul: astronomlar sanani emas, "
                "<u>oynani</u> qidiradi.</p>"
                "<p><strong>O\u2018chirish sinovi:</strong> jumlani olib tashlasak, "
                "<em>therefore</em> osmonda osilib qoladi \u2014 <u>nega</u> oyna "
                "qidiriladi? Vazifa: <mark>usulni asoslaydigan texnik faktni "
                "berish</mark>.</p>"
                + why([
                    (True, "It supplies the technical fact that accounts for the search method described next",
                     "<em>therefore</em> so\u2018zi bog\u2018lanishni ochiq ko\u2018rsatib turibdi: "
                     "orbitaning noaniqligi \u2192 shuning uchun oyna bo\u2018yicha qidiruv."),
                    (False, "It explains why the comet was never photographed after 1861",
                     "jumla orbitani <u>hisoblash</u> haqida, kuzatuvning yo\u2018qligi "
                     "haqida emas. Sabab va oqibat almashtirilgan: kometa "
                     "topilmagani uchun orbita noaniq, aksincha emas."),
                    (False, "It suggests that the original 1861 observations were made carelessly",
                     "matn kuzatuvchilarni ayblamaydi \u2014 muammo kuzatuvlarning "
                     "<u>soni</u>da (<em>those four positions alone</em>), sifatida "
                     "emas. <strong>O\u2018quvchi qo\u2018shib yuboradigan hikoya.</strong>"),
                    (False, "It establishes that the comet is unlikely ever to be seen again",
                     "<strong>teskari.</strong> Oxirgi jumla aynan buni rad etadi: "
                     "topolmaslik <em>proves very little</em> \u2014 ya\u2019ni umid "
                     "yo\u2018qolmagan."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">the function of a sentence</div><div class="pp-card-back">jumlaning matndagi vazifasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to qualify a claim</div><div class="pp-card-back">da\'voni cheklamoq, yumshatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to concede</div><div class="pp-card-back">tan olmoq, yon bermoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an obstacle</div><div class="pp-card-back">to\'siq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a reinterpretation</div><div class="pp-card-back">qayta talqin</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to rest on ~</div><div class="pp-card-back">~ ga tayanmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">guaranteed to produce</div><div class="pp-card-back">baribir chiqadigan, muqarrar natija</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to spare someone</div><div class="pp-card-back">kimnidir ayamoq, ovora qilmaslik</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Javob jumlaning ichida emas — <strong>qo'shnilarida</strong>.</li>"
              "<li><strong>O'chirish sinovi:</strong> jumlani olib tashlang; matn "
              "nimani yo'qotsa — o'sha uning vazifasi.</li>"
              "<li>Vazifani <u>fe'l bilan</u> ayting: dalil keltiradi, cheklaydi, "
              "e'tirozni tan oladi, o'tkazadi.</li>"
              "<li>Eng ko'p tuzoq: <strong>mazmunni qayta aytish</strong> "
              "(vazifa emas).</li>"
              "<li>Adabiy parchada: jumla harakat beradi, qo'shnilari talqin qiladi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 23
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_TSP,
    "title": "SAT R&W 23: Structure Words as Signposts (however, in fact, for instance, ultimately)",
    "summary": "Kichik bog'lovchi so'zlar keyingi jumlaning vazifasini oldindan aytadi — "
               "ularni o'qish matnning xaritasini bepul beradi.",
    "order": 23,
    "blocks": [
        {"rich_text": (
            "<h2>Yo'l ko'rsatkichlari</h2>"
            "<p>12-darsda signal so'zlar bo'sh joyning <u>ma'nosini</u> ochishini "
            "ko'rdik. Endi o'sha so'zlarning ikkinchi ishini o'rganamiz: ular "
            "<mark>keyingi jumlaning vazifasini</mark> ham oldindan aytadi.</p>"
            "<p>Bu Text Structure and Purpose uchun juda qulay. Tuzilish savoli "
            "«qaysi harakat qaysidan keyin keladi» deb so'raydi — va aynan shu "
            "kichik so'zlar har harakatni o'z nomi bilan atab turibdi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>The technique was widely adopted. "
                "<strong>In fact</strong>, …</em><br>"
                "<em>In fact</em> ni ko'rgan zahoti bilasiz: keyingi jumla oldingisini "
                "<u>kuchaytiradi</u> va ehtimol kutilmagan darajaga olib chiqadi. "
                "Jumlani o'qishdan oldin uning vazifasini bilib oldingiz.</p>")
            + '<span class="sr-time">⏱ ~45 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ko'rsatkichlar lug'ati</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>So'z</th><th>Keyingi jumla nima qiladi</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>however · but · yet · by contrast</em></td>"
              "<td>Yo'nalishni buradi — odatda matnning <strong>burilish "
              "nuqtasi</strong></td></tr>"
              "<tr><td><em>in fact · indeed</em></td>"
              "<td>Oldingisini kuchaytiradi, ko'pincha kutilmagan darajaga</td></tr>"
              "<tr><td><em>for instance · for example · consider</em></td>"
              "<td>Misol keltiradi — ya'ni oldingi jumla <u>umumiy da'vo</u> edi</td></tr>"
              "<tr><td><em>admittedly · to be sure · it is true that</em></td>"
              "<td>E'tirozni tan oladi — va deyarli har doim keyin "
              "<em>but</em> keladi</td></tr>"
              "<tr><td><em>ultimately · in the end · finally</em></td>"
              "<td>Yakuniy xulosa yoki natija</td></tr>"
              "<tr><td><em>that said · still · even so</em></td>"
              "<td>Aytilganini qisman orqaga qaytaradi</td></tr>"
              "<tr><td><em>in short · in other words · that is</em></td>"
              "<td>Qayta ifodalaydi — yangi ma'lumot yo'q</td></tr>"
              "<tr><td><em>more importantly · crucially</em></td>"
              "<td>Muallif o'z asosiy fikrini shu yerda aytyapti</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "<em>admittedly</em> va <em>to be sure</em> — imtihonning eng foydali "
                "ikki so'zi. Ular «hozir men <u>o'zimga qarshi</u> gapiraman, lekin bu "
                "vaqtincha» degani. Ulardan keyingi jumla <strong>hech qachon</strong> "
                "matnning asosiy fikri bo'lmaydi — asosiy fikr undan keyingi "
                "<em>but</em> dan keyin keladi.")
        )},

        {"rich_text": (
            "<h3>Ko'rsatkichlarni xaritaga aylantirish</h3>"
            "<p>Amaliy usul: matnni o'qiyotib faqat ko'rsatkichlarni ketma-ket "
            "yozib chiqing (xayolan). Ular matnning skeletini beradi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><em>«Da'vo … <strong>For instance</strong>, "
                "… <strong>Admittedly</strong>, … <strong>But</strong> … "
                "<strong>Ultimately</strong>, …»</em></p>"
                "<p style=\"margin:0;\">Skelet: <mark>da'vo → misol → e'tirof → "
                "e'tirozni rad etish → xulosa</mark>. Matnning mavzusini bilmasangiz "
                "ham tuzilish javobini yozib bera olasiz.</p>")
            + WARN.format(
                "Ko'rsatkichsiz jumlalar ham vazifaga ega — SAT har jumlaga "
                "ko'rsatkich qo'ymaydi. Ko'rsatkich <u>borida</u> undan foydalaning; "
                "<u>yo'qida</u> 22-darsdagi o'chirish sinoviga qayting.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + q(
                "<p>Handwriting is disappearing from primary curricula, and the "
                "arguments for keeping it are usually sentimental. Admittedly, the case "
                "for cursive in particular is weak: almost nobody now writes at length by "
                "hand. But experiments in which students take notes by hand and by laptop "
                "keep producing the same result on tests of understanding, and the "
                "explanation offered is that writing by hand is slow enough to force a "
                "choice about what is worth recording.</p>",
                "Which choice best describes the overall structure of the text?")
            + choices_html([
                "It reports a trend, concedes a point to those who support it, and then "
                "gives evidence that complicates the case for it.",
                "It argues that cursive handwriting should be restored to the curriculum.",
                "It compares the note-taking habits of two groups of students in detail.",
                "It explains why handwriting was originally included in primary "
                "curricula.",
            ])
            + "<p><strong>Ko'rsatkichlarni sanaymiz:</strong> "
              "<em>Admittedly</em> → e'tirof; <em>But</em> → burilish. Ikkovi "
              "birga skeletni beradi.</p>"
            + "<p><strong>Skelet:</strong> tendensiya bor → «rost, sizniki ham "
              "to'g'ri» → <u>lekin</u> dalil boshqa narsani ko'rsatadi.</p>"
            + why([
                (True, "It reports a trend, concedes a point to those who support it, and then gives evidence that complicates the case for it",
                 "uchala harakat ham ko'rsatkichlar bilan belgilangan: tendensiya "
                 "(<em>is disappearing</em>), e'tirof (<em>Admittedly</em>), dalil "
                 "(<em>But … keep producing the same result</em>)."),
                (False, "It argues that cursive handwriting should be restored to the curriculum",
                 "<em>Admittedly</em> dan keyingi jumla aynan buning teskarisini "
                 "aytadi: <em>the case for cursive in particular is weak</em>. "
                 "E'tirof jumlasini matnning fikri deb o'qish — bu turdagi eng "
                 "ko'p uchraydigan xato."),
                (False, "It compares the note-taking habits of two groups of students in detail",
                 "<strong>yarim to'g'ri</strong>: tajribalar eslatilgan. Lekin "
                 "<em>in detail</em> yo'q — bitta jumla, va gap odatlar haqida emas, "
                 "<u>natijalar</u> haqida."),
                (False, "It explains why handwriting was originally included in primary curricula",
                 "kelib chiqish tarixi umuman muhokama qilinmaydi."),
            ])
        )},

        {
            "rich_text": q(
                "<p>Solar panels lose efficiency as they heat up, which is why a cool "
                "bright day produces more power than a hot one. For instance, an array in "
                "a mountain village may outperform an identical array in a desert with "
                "more hours of sun. Ultimately the siting decision turns on temperature "
                "as much as on sunlight, and the maps used by early installers, which "
                "showed only sunlight, sent equipment to the wrong places for "
                "years.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It states a physical fact, illustrates it, and then draws out a practical consequence.", "is_correct": True},
                {"text": "It compares the total power output of two specific installations.", "is_correct": False},
                {"text": "It criticises early installers for ignoring evidence available to them.", "is_correct": False},
                {"text": "It explains the chemistry by which a solar panel converts light to electricity.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ko'rsatkichlar:</strong> <em>For instance</em> → misol; "
                "<em>Ultimately</em> → yakuniy natija. Skelet o'zi yozilib turibdi: "
                "<mark>fakt → misol → amaliy oqibat</mark>.</p>"
                + why([
                    (True, "It states a physical fact, illustrates it, and then draws out a practical consequence",
                     "uchala harakat ham ko'rsatkichlarga to'g'ri keladi. "
                     "<em>For instance</em> dan oldingi jumla — fakt; keyingisi — "
                     "misol; <em>Ultimately</em> — oqibat."),
                    (False, "It compares the total power output of two specific installations",
                     "tog' qishlog'i va cho'l — <u>misol</u> uchun keltirilgan farazli "
                     "holat (<em>may outperform</em>), aniq ikki qurilma emas. "
                     "Va umumiy quvvat solishtirilmaydi."),
                    (False, "It criticises early installers for ignoring evidence available to them",
                     "<strong>yarim to'g'ri</strong>: o'rnatuvchilar xato qilgan. "
                     "Lekin matn ularni ayblamaydi — muammo <u>xaritalarda</u> edi "
                     "(<em>which showed only sunlight</em>), ya'ni ma'lumot mavjud "
                     "emasdi. Ikkinchi yarmi matnga zid."),
                    (False, "It explains the chemistry by which a solar panel converts light to electricity",
                     "kimyo umuman yo'q — matn faqat harorat va samaradorlik "
                     "bog'liqligini aytadi, mexanizmini emas."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Machine translation now handles routine business correspondence well "
                "enough that many firms have stopped paying for it. Admittedly, the "
                "output still needs a reader who knows both languages. That said, the "
                "reader's job has changed from writing to checking, and checking is "
                "faster. <span class=\"sr-focus\">The work that has actually vanished is "
                "not translation but the junior post in which translators used to learn "
                "the trade.</span></p>",
                "What is the main purpose of the underlined sentence?"),
            "choices": [
                {"text": "It redirects the discussion from the obvious loss to a less visible one.", "is_correct": True},
                {"text": "It concedes that machine translation still requires human oversight.", "is_correct": False},
                {"text": "It provides statistical evidence for the claim made in the first sentence.", "is_correct": False},
                {"text": "It predicts that human translators will soon be unnecessary.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ko'rsatkichlarni o'qiymiz:</strong> <em>Admittedly</em> → "
                "e'tirof; <em>That said</em> → e'tirofni qisman qaytarish. Tagi "
                "chizilgan jumlada ko'rsatkich <u>yo'q</u> — demak 22-darsdagi "
                "o'chirish sinovi kerak.</p>"
                "<p><strong>O'chirish sinovi:</strong> jumlani olib tashlasak, matn "
                "«mashina tarjimasi yaxshi ishlayapti» degan joyda tugaydi. "
                "Yo'qoladigan narsa — <mark>asl yo'qotish boshqa joyda ekani</mark>. "
                "Jumlaning butun vazifasi shu burilishda.</p>"
                + why([
                    (True, "It redirects the discussion from the obvious loss to a less visible one",
                     "<em>not translation but the junior post</em> qurilishi aynan "
                     "yo'nalishni burish: ko'rinadigan yo'qotish o'rniga ko'rinmasini "
                     "qo'yadi."),
                    (False, "It concedes that machine translation still requires human oversight",
                     "bu <u>oldingi</u> jumlaning ishi (<em>Admittedly, the output "
                     "still needs a reader</em>). Qo'shni jumlaning vazifasini tagi "
                     "chizilganiga yopishtirish — bu turdagi doimiy tuzoq."),
                    (False, "It provides statistical evidence for the claim made in the first sentence",
                     "birorta raqam yo'q, va jumla birinchi da'voni ko'tarmaydi — "
                     "u boshqa mavzuga o'tadi."),
                    (False, "It predicts that human translators will soon be unnecessary",
                     "<strong>teskari</strong>: matn tarjimonlar kerakligini "
                     "(<em>a reader who knows both languages</em>) tasdiqlaydi. "
                     "Yo'qolgan narsa — <u>o'rgatuvchi lavozim</u>, kasbning o'zi "
                     "emas."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>A city council votes on a budget line for street trees. Indeed, the "
                "sums involved are so small that the item usually passes without "
                "discussion. Ultimately, though, those trees determine which streets are "
                "walkable in July, and in a city where summer temperatures now exceed "
                "forty degrees for weeks at a time, that is not a small matter.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It describes a routine decision, emphasises how minor it appears, and then argues that its consequences are not minor.", "is_correct": True},
                {"text": "It presents two councillors' opposing views on a budget proposal.", "is_correct": False},
                {"text": "It explains how street trees reduce the temperature of a road surface.", "is_correct": False},
                {"text": "It recommends that the council increase its budget for street trees.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ko'rsatkichlar:</strong> <em>Indeed</em> → oldingisini "
                "kuchaytiradi («shu qadar kichikki, muhokamasiz o'tadi»); "
                "<em>Ultimately, though</em> → ikkitasi birga: yakuniy xulosa "
                "<u>va</u> burilish.</p>"
                "<p>Skelet: <mark>oddiy qaror → juda arzimas ko'rinadi → aslida "
                "arzimas emas</mark>.</p>"
                + why([
                    (True, "It describes a routine decision, emphasises how minor it appears, and then argues that its consequences are not minor",
                     "uchala harakat ham ko'rsatkichlarga to'g'ri keladi, va oxirgi "
                     "bo'lak <em>though</em> orqali kelgan burilishni ushlaydi."),
                    (False, "It presents two councillors' opposing views on a budget proposal",
                     "birorta a'zo gapirmaydi — matnda umuman odam yo'q. "
                     "<strong>So'z-tuzoq</strong>: <em>council</em>, <em>votes</em> "
                     "bahs tasvirini uyg'otadi."),
                    (False, "It explains how street trees reduce the temperature of a road surface",
                     "mexanizm tushuntirilmaydi. Matn daraxtlar ko'chani yurish uchun "
                     "yaroqli qilishini aytadi, <u>qanday</u> qilishini emas. "
                     "<strong>Doirasi juda tor.</strong>"),
                    (False, "It recommends that the council increase its budget for street trees",
                     "<strong>yarim to'g'ri</strong> va eng jozibali: matn "
                     "daraxtlarni muhim deb hisoblaydi. Lekin u byudjetni oshirishni "
                     "<u>talab qilmaydi</u> — u qarorning ahamiyatini "
                     "ko'rsatadi, xolos. Baho ≠ tavsiya."),
                ])
                + NOTE.format(
                    "<em>though</em> jumla oxirida yoki o'rtasida kelsa ham "
                    "<em>however</em> bilan bir xil ishlaydi. Uni "
                    "<em>although</em> bilan adashtirmang: <em>although</em> ergash "
                    "gap boshlaydi, <em>though</em> esa bu yerda mustaqil "
                    "ko'rsatkich.")
            ),
        },

        {
            "rich_text": q(
                "<p>Reintroducing a predator to a landscape is usually justified by "
                "pointing to the deer it will remove. In fact the change ecologists now "
                "emphasise is often to the deer's behaviour rather than to their "
                "number: animals that are hunted stop lingering in open valleys, and the "
                "young trees there begin to recover. Ultimately the visible result is a "
                "change in the vegetation, produced by an animal most visitors never "
                "see.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It gives the usual justification for a practice, redirects attention to a different mechanism, and names the visible outcome.", "is_correct": True},
                {"text": "It argues that predators should be reintroduced wherever they once lived.", "is_correct": False},
                {"text": "It compares the vegetation of two valleys with different predator populations.", "is_correct": False},
                {"text": "It explains the methods ecologists use to count deer in a landscape.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ko\u2018rsatkichlar:</strong> <em>In fact</em> \u2192 oldingisini "
                "kuchaytiradi va yo\u2018nalishni burab yuboradi; <em>Ultimately</em> \u2192 "
                "yakuniy natija. Skelet: <mark>odatiy asos \u2192 asl mexanizm \u2192 "
                "ko\u2018rinadigan natija</mark>.</p>"
                + why([
                    (True, "It gives the usual justification for a practice, redirects attention to a different mechanism, and names the visible outcome",
                     "uchala harakat ham ko\u2018rsatkichlarga to\u2018g\u2018ri keladi. "
                     "<em>rather than to their number</em> \u2014 yo\u2018nalishning "
                     "burilishi; <em>Ultimately</em> \u2014 natija."),
                    (False, "It argues that predators should be reintroduced wherever they once lived",
                     "matn hech narsa talab qilmaydi \u2014 u qaytarishning "
                     "<u>qanday ishlashini</u> tushuntiradi. <strong>Baho \u2260 "
                     "tavsiya.</strong>"),
                    (False, "It compares the vegetation of two valleys with different predator populations",
                     "bitta manzara tasvirlangan, ikkita emas. <em>open valleys</em> "
                     "iborasi solishtirish tuyg\u2018usini beradi, lekin taqqoslash yo\u2018q. "
                     "<strong>So\u2018z-tuzoq.</strong>"),
                    (False, "It explains the methods ecologists use to count deer in a landscape",
                     "sanash usullari umuman muhokama qilinmaydi \u2014 aksincha, matn "
                     "<u>sondan boshqa</u> narsa muhimroq deydi. "
                     "<strong>Doirasi butunlay boshqa.</strong>"),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">admittedly</div><div class="pp-card-back">tan olish kerak, rost (e\'tirof signali)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">that said</div><div class="pp-card-back">shunga qaramay, ammo</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">indeed / in fact</div><div class="pp-card-back">haqiqatan ham (kuchaytirish signali)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">ultimately</div><div class="pp-card-back">oxir-oqibat, pirovardida</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to concede a point</div><div class="pp-card-back">bir masalada yon bermoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to complicate the case for ~</div><div class="pp-card-back">~ foydasidagi dalilni qiyinlashtirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to draw out a consequence</div><div class="pp-card-back">oqibatini chiqarib ko\'rsatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to outperform</div><div class="pp-card-back">undan yaxshiroq natija bermoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Ko'rsatkich so'z keyingi jumlaning <strong>vazifasini</strong> "
              "oldindan aytadi.</li>"
              "<li>Matnni o'qiyotib faqat ko'rsatkichlarni ketma-ket ayting — bu "
              "matnning <u>skeleti</u>.</li>"
              "<li><em>Admittedly</em> / <em>to be sure</em> dan keyingi jumla "
              "<strong>hech qachon</strong> asosiy fikr emas.</li>"
              "<li><em>Ultimately</em>, <em>in the end</em> — matnning xulosasi "
              "shu yerda.</li>"
              "<li>Ko'rsatkich yo'q bo'lsa — o'chirish sinoviga qayting (22-dars).</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 24
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_TSP,
    "title": "SAT R&W 24: Text Structure and Purpose — Mixed Practice",
    "summary": "Tuzilish, matn maqsadi va jumla vazifasi aralash, imtihon tezligida: "
               "20–23-darslarda o'rganilgan usulni soatga qarshi mustahkamlash.",
    "order": 24,
    "blocks": [
        {"rich_text": (
            "<h2>Uchala savol aralash</h2>"
            "<p>Bu — <strong>Text Structure and Purpose</strong> mavzusining yakuni. "
            "Oltita savol, uch shakl aralash: <em>overall structure</em>, "
            "<em>main purpose of the text</em>, <em>purpose of the underlined "
            "sentence</em>.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Qanday ishlash kerak:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li>Taymer: <strong>6 daqiqa</strong> (bu tur Words in Context'dan "
                "sekinroq — ~60 soniya).</li>"
                "<li>Oltitasini to'xtamasdan yeching.</li>"
                "<li>Keyin tushuntirishlarni o'qing.</li>"
                "</ol>")
            + '<span class="sr-time">⏱ 6 savol · 6 daqiqa</span>'
        )},

        {"rich_text": (
            "<h3>To'rtta harakat — yodda tuting</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>Savol turini aniqlang</strong> — "
              "variantlar <em>To …</em> bilan boshlansa, bu maqsad savoli "
              "(20-dars).</p></div>"
            + "<div class=\"pp-step\"><p><strong>Ko'rsatkichlarni o'qing</strong> — "
              "<em>however · admittedly · for instance · ultimately</em> "
              "(23-dars).</p></div>"
            + "<div class=\"pp-step\"><p><strong>Shaklni besh so'zda ayting</strong> "
              "(21-dars) yoki jumla uchun <strong>o'chirish sinovi</strong>ni "
              "qiling (22-dars).</p></div>"
            + "<div class=\"pp-step\"><p><strong>Variantni oxirigacha o'qing</strong> "
              "— tuzoq odatda ikkinchi yarmida.</p></div>"
            + '</div>'
        )},

        {
            "rich_text": q(
                "<p>Wikipedia's articles are usually judged by their accuracy, and by "
                "that measure they do well. The more revealing document, however, is the "
                "talk page attached to each article, where editors argue about wording "
                "for years. A reader who wants to know which claims are contested will "
                "learn more there in ten minutes than from the article itself.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It notes the usual basis for judging something, then argues that a different feature is more informative.", "is_correct": True},
                {"text": "It questions the accuracy of Wikipedia's articles and gives examples of errors.", "is_correct": False},
                {"text": "It describes how editors resolve disagreements about wording.", "is_correct": False},
                {"text": "It compares Wikipedia with traditional printed encyclopaedias.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ko'rsatkich:</strong> <em>however</em> — burilish nuqtasi. "
                "Undan oldin odatiy o'lchov (aniqlik), keyin muallifning taklifi "
                "(muhokama sahifasi).</p>"
                + why([
                    (True, "It notes the usual basis for judging something, then argues that a different feature is more informative",
                     "ikki bosqich va <em>however</em> orqali kelgan burilish. "
                     "<em>The more revealing document</em> — «boshqa xususiyat "
                     "foydaliroq» degan da'voning ochiq ifodasi."),
                    (False, "It questions the accuracy of Wikipedia's articles and gives examples of errors",
                     "<strong>teskari</strong>: matn <em>by that measure they do "
                     "well</em> deb aniqlikni tasdiqlaydi. Va birorta xato misoli "
                     "yo'q."),
                    (False, "It describes how editors resolve disagreements about wording",
                     "muharrirlar <em>argue for years</em> — hal qilish jarayoni "
                     "tasvirlanmaydi. <strong>So'z-tuzoq.</strong>"),
                    (False, "It compares Wikipedia with traditional printed encyclopaedias",
                     "bosma ensiklopediyalar umuman eslatilmaydi."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>A rainwater tank on a roof loses very little to evaporation, costs "
                "almost nothing to run and needs no permission from anyone. It also "
                "cannot supply a household through a dry season. <span class=\"sr-focus\">"
                "The technologies that scale badly are often the ones that spread "
                "fastest, because anybody can start one without waiting.</span> Cities "
                "that dismissed roof tanks as insufficient found them installed anyway, "
                "one house at a time.</p>",
                "What is the main purpose of the underlined sentence?"),
            "choices": [
                {"text": "It generalises from the specific case in order to explain the outcome described next.", "is_correct": True},
                {"text": "It concedes that rainwater tanks cannot meet a household's full needs.", "is_correct": False},
                {"text": "It recommends that cities invest in small-scale water technologies.", "is_correct": False},
                {"text": "It explains the technical reasons a roof tank loses little water.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Qo'shnilar:</strong> oldin — bak arzon, oson, lekin "
                "yetarli emas. Keyin — shaharlar rad etgan, ammo baklar baribir "
                "o'rnatilgan.</p>"
                "<p><strong>O'chirish sinovi:</strong> jumlani olib tashlasak, "
                "oxirgi jumla <u>izohsiz</u> qoladi: nega yetarli bo'lmagan narsa "
                "baribir tarqaldi? Vazifa: <mark>aniq holatdan umumiy qoida chiqarib, "
                "keyingi natijani tushuntirish</mark>.</p>"
                + why([
                    (True, "It generalises from the specific case in order to explain the outcome described next",
                     "jumla <em>The technologies that…</em> deb boshlanadi — bakdan "
                     "kengroq darajaga chiqadi — va <em>because anybody can start one "
                     "without waiting</em> oxirgi jumlaning sababini beradi."),
                    (False, "It concedes that rainwater tanks cannot meet a household's full needs",
                     "bu <u>oldingi</u> jumlaning ishi (<em>It also cannot supply a "
                     "household through a dry season</em>). Qo'shnining vazifasini "
                     "tagi chizilganiga yopishtirish — doimiy tuzoq."),
                    (False, "It recommends that cities invest in small-scale water technologies",
                     "matn hech narsa tavsiya qilmaydi; u <u>nima sodir "
                     "bo'lganini</u> tushuntiradi."),
                    (False, "It explains the technical reasons a roof tank loses little water",
                     "bug'lanish birinchi jumlada bir og'iz eslatilgan va "
                     "tushuntirilmagan. <strong>Doirasi juda tor.</strong>"),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Every few years someone proposes replacing school grades with written "
                "comments, and every few years the proposal is abandoned. The comments "
                "take four times as long to write and are read by fewer parents. "
                "Ultimately the grade survives not because anyone defends it but because "
                "nothing else fits into the time a teacher actually has.</p>",
                "What is the main purpose of the text?"),
            "choices": [
                {"text": "To explain why a repeatedly proposed reform keeps failing for practical rather than principled reasons.", "is_correct": True},
                {"text": "To argue that written comments are a better assessment of student learning than grades.", "is_correct": False},
                {"text": "To describe the history of grading systems in schools.", "is_correct": False},
                {"text": "To criticise parents for not reading their children's written comments.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ko'rsatkich:</strong> <em>Ultimately</em> — xulosa shu "
                "yerda, va u juda aniq: <em>not because anyone defends it but "
                "because nothing else fits into the time a teacher actually "
                "has</em>. Ya'ni sabab <mark>amaliy, printsipial emas</mark>.</p>"
                + why([
                    (True, "To explain why a repeatedly proposed reform keeps failing for practical rather than principled reasons",
                     "oxirgi jumlaning <em>not … but …</em> qurilishini aynan "
                     "takrorlaydi, va <em>Every few years</em> takroriyligini ham "
                     "qamraydi."),
                    (False, "To argue that written comments are a better assessment of student learning than grades",
                     "matn izohlarning <u>sifati</u> haqida hech nima demaydi — "
                     "faqat ular ko'p vaqt olishini va kam o'qilishini aytadi. "
                     "<strong>O'quvchi qo'shib yuboradigan da'vo.</strong>"),
                    (False, "To describe the history of grading systems in schools",
                     "tarix yo'q: na sana, na bosqich, na kelib chiqish. "
                     "<em>Every few years</em> takroriylikni bildiradi, tarixni emas."),
                    (False, "To criticise parents for not reading their children's written comments",
                     "ota-onalar bir bo'lakda eslatilgan va ayblanmaydi — bu "
                     "shunchaki xarajat hisobining bir qatori."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Ergonomists studying kitchen work in the 1920s timed every step a "
                "cook took and rearranged the room to shorten the total. The resulting "
                "layouts saved real distance. What the studies did not record is that a "
                "cook standing in one place all afternoon grows tired in a different way, "
                "and later designers began putting some of the walking back.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It describes a method and its measured success, then identifies something the method could not measure.", "is_correct": True},
                {"text": "It argues that the 1920s studies were poorly designed and should be disregarded.", "is_correct": False},
                {"text": "It traces the development of the modern kitchen from the 1920s to the present.", "is_correct": False},
                {"text": "It compares the working conditions of cooks in two different decades.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Besh so'zli bashorat:</strong> «Usul ishladi, lekin bir "
                "narsani o'lchamagan.» — 1-shaklning yaqin qarindoshi, burilish "
                "<em>What the studies did not record</em> da.</p>"
                + why([
                    (True, "It describes a method and its measured success, then identifies something the method could not measure",
                     "ikki bosqich aniq: <em>saved real distance</em> (muvaffaqiyat) → "
                     "<em>did not record</em> (o'lchanmagan narsa)."),
                    (False, "It argues that the 1920s studies were poorly designed and should be disregarded",
                     "<strong>yarim to'g'ri</strong>: tadqiqotlarning chegarasi bor. "
                     "Lekin matn ularni yomon deb atamaydi — <em>saved real "
                     "distance</em> ularning muvaffaqiyatini tan oladi — va hech "
                     "narsani rad etishni taklif qilmaydi."),
                    (False, "It traces the development of the modern kitchen from the 1920s to the present",
                     "<em>later designers</em> bitta ibora — bu rivojlanish tarixi "
                     "emas. <strong>Doirasi juda keng.</strong>"),
                    (False, "It compares the working conditions of cooks in two different decades",
                     "ikki o'n yillik solishtirilmaydi; gap bitta usul va uning "
                     "cheklovi haqida."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Zilola had assumed the archive would be quiet. It was, but not in the "
                "way she expected: the silence had a shape to it, made of paper being "
                "turned three tables away and a fan somewhere behind the shelves. "
                "<span class=\"sr-focus\">By the second week she could tell, without "
                "looking up, whether the reader opposite had found what he was looking "
                "for.</span> She had come to write about the documents and was learning "
                "the room instead.</p>",
                "What is the main purpose of the underlined sentence?"),
            "choices": [
                {"text": "It gives the specific evidence of the attentiveness that the final sentence names.", "is_correct": True},
                {"text": "It shows that Zilola had become distracted from her research by other readers.", "is_correct": False},
                {"text": "It explains why the archive was quieter than Zilola had expected.", "is_correct": False},
                {"text": "It establishes that Zilola had become friendly with the other readers.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Qo'shnilar:</strong> oldin — sukunatning «shakli» bor. "
                "Keyin — <em>She had come to write about the documents and was learning "
                "the room instead</em>.</p>"
                "<p><strong>O'chirish sinovi:</strong> jumlani olib tashlasak, oxirgi "
                "jumladagi «xonani o'rganyapti» da'vosining <u>isboti</u> qolmaydi. "
                "Vazifa: <mark>o'sha da'voning konkret dalilini berish</mark>.</p>"
                + why([
                    (True, "It gives the specific evidence of the attentiveness that the final sentence names",
                     "qarab ko'rmasdan qo'shnisining holatini bilish — bu «xonani "
                     "o'rganish»ning aniq ko'rinishi. 22-darsdagi qoida: adabiy "
                     "parchada tagi chizilgan jumla harakat beradi, qo'shnisi uni "
                     "nomlaydi."),
                    (False, "It shows that Zilola had become distracted from her research by other readers",
                     "<strong>eng jozibali tuzoq</strong>, chunki oxirgi jumla "
                     "haqiqatan «hujjatlar o'rniga» deydi. Lekin matnning ohangi "
                     "ayblov emas — <em>the silence had a shape to it</em> "
                     "hayratlanish, va bu diqqatning yo'qolishi emas, "
                     "<u>o'tkirlashuvi</u>."),
                    (False, "It explains why the archive was quieter than Zilola had expected",
                     "<strong>teskari va noto'g'ri</strong>: arxiv kutilganidan "
                     "jimroq emas edi — u <em>not in the way she expected</em> "
                     "jim edi."),
                    (False, "It establishes that Zilola had become friendly with the other readers",
                     "hech kim gaplashmaydi. Zilola qo'shnisiga <u>qaramaydi</u> "
                     "ham. Do'stlik matnga o'quvchi qo'shib yuboradigan narsa."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>The standard account of the Silk Road describes caravans travelling "
                "from China to the Mediterranean. Very few did. Goods moved in short "
                "relays between neighbouring markets, changing hands many times, and the "
                "merchant who bought silk in Samarkand had usually never seen the place "
                "it was made. Distance was covered by the goods, not by the "
                "people.</p>",
                "What is the main purpose of the text?"),
            "choices": [
                {"text": "To correct a common picture of how trade along the route actually worked.", "is_correct": True},
                {"text": "To explain why silk was the most valuable commodity carried along the route.", "is_correct": False},
                {"text": "To describe the daily life of a merchant based in Samarkand.", "is_correct": False},
                {"text": "To argue that the Silk Road was less important than historians claim.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Shakl:</strong> keng tarqalgan tasavvur → "
                "<em>Very few did</em> (ikki so'zlik burilish!) → haqiqiy manzara → "
                "yakuniy formula (<em>Distance was covered by the goods, not by the "
                "people</em>).</p>"
                "<p>Maqsad savoli, shuning uchun javob bitta vazifani nomlashi kerak: "
                "<mark>noto'g'ri tasavvurni to'g'rilash</mark>.</p>"
                + why([
                    (True, "To correct a common picture of how trade along the route actually worked",
                     "<em>The standard account … Very few did</em> aynan tuzatish "
                     "harakati, va qolgan ikki jumla to'g'ri manzarani beradi."),
                    (False, "To explain why silk was the most valuable commodity carried along the route",
                     "ipak faqat misol sifatida bir marta keladi, va uning qiymati "
                     "muhokama qilinmaydi. <strong>Doirasi juda tor.</strong>"),
                    (False, "To describe the daily life of a merchant based in Samarkand",
                     "savdogar bitta bo'lakda, faqat <u>bilmagan narsasi</u> uchun "
                     "eslatilgan. Kundalik hayot tasvirlanmaydi."),
                    (False, "To argue that the Silk Road was less important than historians claim",
                     "<strong>eng nozik tuzoq</strong>: matn <u>qanday</u> "
                     "ishlaganini to'g'rilaydi, <u>qanchalik muhim</u> bo'lganini "
                     "emas. Savdo baribir bo'lgan — faqat boshqacha. "
                     "«To'g'rilash» ni «ahamiyatini kamaytirish» deb o'qish — "
                     "matnda yo'q qadam."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Xatoni turi bo'yicha tahlil qiling</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Xato turi</th><th>Nima qilish kerak</th></tr></thead>"
              "<tbody>"
              "<tr><td>Variantning boshi to'g'ri edi, oxirini o'qimadim</td>"
              "<td>20-dars, 4-qadam. Bu mavzudagi eng ko'p uchraydigan xato.</td></tr>"
              "<tr><td>Tuzilish va maqsadni adashtirdim</td>"
              "<td>20-dars. Variantlar <em>To …</em> bilan boshlansa — maqsad.</td></tr>"
              "<tr><td>Qo'shni jumlaning vazifasini tagi chizilganiga berdim</td>"
              "<td>22-dars. O'chirish sinovi.</td></tr>"
              "<tr><td>Matn tavsiya qilmagan narsani tanladim "
              "(<em>recommends</em>, <em>argues</em>)</td>"
              "<td>Baho ≠ tavsiya. Matn muhim desa, u «ko'proq qiling» demagan "
              "bo'ladi.</td></tr>"
              "<tr><td>E'tirof jumlasini asosiy fikr deb o'qidim</td>"
              "<td>23-dars. <em>Admittedly</em> dan keyingi jumla hech qachon "
              "asosiy fikr emas.</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Oltitadan 4–5 tasini to'g'ri yechsangiz — bu mavzu bo'yicha yaxshi "
                "darajadasiz. Uchtadan kam bo'lsa, xatolaringizni yuqoridagi jadval "
                "bo'yicha ajrating: deyarli har doim ular <u>bitta</u> turga "
                "yig'iladi, va o'sha bitta darsni qayta o'qish kifoya.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">the standard account</div><div class="pp-card-back">keng tarqalgan, odatiy tushuntirish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to generalise from ~</div><div class="pp-card-back">~ dan umumiy xulosa chiqarmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to scale badly</div><div class="pp-card-back">kattalashganda yomon ishlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">practical rather than principled</div><div class="pp-card-back">printsipial emas, amaliy (sabab)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to dismiss ~ as insufficient</div><div class="pp-card-back">~ ni yetarli emas deb rad etmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">attentiveness</div><div class="pp-card-back">diqqat, e\'tiborlilik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to change hands</div><div class="pp-card-back">qo\'ldan qo\'lga o\'tmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">in short relays</div><div class="pp-card-back">qisqa bosqichlarda, navbat bilan</div></div>'
            + "</div>"
            + "<h3>Xulosa — Text Structure and Purpose mavzusi yakuni</h3>"
            + "<ul>"
              "<li><strong>Structure</strong> = shakl, <strong>purpose</strong> = "
              "vazifa; variantlarning shaklidan turini biling (20-dars).</li>"
              "<li>Oltita shakl bor, va shaklni <u>besh so'zda</u> ayting "
              "(21-dars).</li>"
              "<li>Jumla vazifasi uning <strong>qo'shnilarida</strong> — o'chirish "
              "sinovi (22-dars).</li>"
              "<li>Ko'rsatkich so'zlar matnning skeletini bepul beradi (23-dars).</li>"
              "<li>Variantni <strong>oxirigacha</strong> o'qing: yarim to'g'ri — "
              "bu mavzuning bosh tuzog'i.</li>"
              "</ul>"
        )},
    ],
},

]
