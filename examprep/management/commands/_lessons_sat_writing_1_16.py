# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — WRITING lessons 1-3 and 10-16.

The first batch of the `writing` skill: "Strategiya va format" (1-3) and the whole
of "Bog'lovchi so'zlar (Transitions)" (10-16).

⚠️ This is the OTHER half of the same 54-question section. Its two domains are
Standard English Conventions (~26%) and Expression of Ideas (~20%). There is no
essay and nothing is written by the pupil — every question is a four-choice MCQ,
exactly as in the reading half. See toc_sat_writing.txt and STYLE_GUIDE_SAT_RW.md.
"""

TRACK = {
    "name":    "SAT",
    "summary": "Digital SAT — Reading and Writing bo'limiga savol turlari bo'yicha "
               "tayyorgarlik. Imtihonning matematik yarmi Prime SAT Math kursida.",
    "icon":    "bi-mortarboard",
    "color":   "#7c3aed",
    "order":   3,
}

TOPIC_WSTRAT = {
    "title":   "Strategiya va format (Conventions & Expression: qanday tuzilgan)",
    "summary": "Imtihonning grammatika va uslub yarmi qanday tuzilgan, nega u eng "
               "tez ball keltiradi va uni qanday o'qish kerak.",
    "icon":    "bi-compass",
    "order":   1,
}

TOPIC_TRANS = {
    "title":   "Bog'lovchi so'zlar (Transitions)",
    "summary": "Ikki gap orasidagi munosabatni aniqlab, unga mos bog'lovchini "
               "tanlash — Expression of Ideas domenining eng ko'p uchraydigan turi.",
    "icon":    "bi-signpost-split",
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


def q(passage, stem):
    return f'<div class="sr-passage">{passage}</div><p><strong>{stem}</strong></p>'


def conv_q(passage):
    """Standard English Conventions: the stem never varies."""
    return q(passage, "Which choice completes the text so that it conforms to the "
                      "conventions of Standard English?")


def trans_q(passage):
    """Transitions: the stem never varies either."""
    return q(passage, "Which choice completes the text with the most logical "
                      "transition?")


def notes_q(head, bullets, goal):
    """Rhetorical Synthesis: the research-notes card, then the goal sentence."""
    items = ''.join(f'<li>{b}</li>' for b in bullets)
    return ('<div class="sr-notes">'
            f'<p class="sr-notes__head">{head}</p><ul>{items}</ul></div>'
            f'<p><strong>{goal}</strong></p>')


def choices_html(items):
    """The static A/B/C/D list used in a WORKED example (not a shuffled choices block)."""
    return '<ol type="A">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'


def qnum(n, kind):
    return (f'<p style="margin:0 0 4px;"><span style="background:#ede9fe;color:#5b21b6;'
            f'border-radius:999px;padding:2px 10px;font-size:.82rem;font-weight:600;">'
            f'{n}-savol · {kind}</span></p>')


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Writing 1
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_WSTRAT,
    "title": "SAT R&W W1: The Writing Half — Grammar Questions Are the Fastest Marks on the Test",
    "summary": "Imtihonning ikkinchi yarmi: ikki domen, savollarning 46 foizi, va "
               "nega ular o'qish savollaridan ikki barobar tez yechiladi.",
    "order": 1,
    "blocks": [
        {"rich_text": (
            "<h2>Imtihonning arzon yarmi</h2>"
            "<p>Siz o'qish yarmini tugatdingiz — sakkiz savol turi, matn tahlili, "
            "dalil, xulosa. Endi <mark>ikkinchi yarmi</mark> boshlanadi, va u "
            "butunlay boshqacha ishlaydi.</p>"
            "<p>Bu yerda sizdan muallifning niyatini tushunish so'ralmaydi. "
            "Sizdan <strong>qoidani qo'llash</strong> so'raladi. Va qoidalarning "
            "yaxshi tomoni shuki, ular <u>qoida</u>: ular bahsga o'rin "
            "qoldirmaydi, tuyg'uga bog'liq emas, va bir marta o'rganilsa "
            "har safar ishlaydi.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Domen</th><th>Ulush</th><th>Savol</th><th>Nima "
              "tekshiriladi</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Standard English Conventions</strong></td>"
              "<td>~26%</td><td>11–15</td>"
              "<td>Grammatika va tinish belgilari</td></tr>"
              "<tr><td><strong>Expression of Ideas</strong></td>"
              "<td>~20%</td><td>8–12</td>"
              "<td>Bog'lovchilar va qaydlardan jumla qurish</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + "<p>Birgalikda — <strong>~46%</strong>, ya'ni 54 savoldan taxminan "
            "25 tasi.</p>"
            + '<span class="sr-time">⏱ Conventions ~30 soniya · Expression ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Nega bu savollar tezroq</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Matn juda qisqa.</strong> "
              "Conventions savollarining matni ko'pincha 25–50 so'z — "
              "o'qish savollaridagining yarmi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Savol o'zgarmaydi.</strong> "
              "Conventions savolining matni deyarli har doim aynan bir xil: "
              "<em>Which choice completes the text so that it conforms to the "
              "conventions of Standard English?</em> Uni o'qish ham shart "
              "emas — shaklidan tanib olasiz.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Javob bahssiz.</strong> "
              "Vergul ikki mustaqil gapni bog'lay olmaydi — bu fikr emas, "
              "fakt. O'qish savolida «qaysi biri yaxshiroq» degan mulohaza "
              "bor; bu yerda yo'q.</p></div>"
            + "<div class=\"pp-step\"><p><strong>4. Variantlar bir-biriga "
              "juda o'xshaydi.</strong> Ko'pincha bitta vergul yoki bitta "
              "harf farq qiladi. Bu yomon emas — bu sizga <u>nima "
              "tekshirilayotganini</u> aytadi.</p></div>"
            + '</div>'
            + TIP.format(
                "4-qadam eng foydali hiyla. Variantlar orasidagi farqni "
                "toping — u savolning <strong>mavzusini</strong> aytadi. "
                "<em>its / it's</em> farq qilsa — bu apostrof savoli. "
                "<em>, / ; / —</em> farq qilsa — bu chegara savoli. "
                "Matnni o'qishdan oldin ham nima izlashni bilib olasiz.")
        )},

        {"rich_text": (
            "<h3>To'rt savol turi</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Tur</th><th>Domen</th><th>Savol matni</th></tr></thead>"
              "<tbody>"
              "<tr><td>Boundaries</td><td>Conventions</td>"
              "<td><em>…conforms to the conventions of Standard English?</em></td></tr>"
              "<tr><td>Form, Structure, and Sense</td><td>Conventions</td>"
              "<td>xuddi shu matn</td></tr>"
              "<tr><td>Transitions</td><td>Expression</td>"
              "<td><em>…the most logical transition?</em></td></tr>"
              "<tr><td>Rhetorical Synthesis</td><td>Expression</td>"
              "<td><em>The student wants to… Which choice most effectively "
              "uses relevant information from the notes…?</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + NOTE.format(
                "Ikki Conventions turi bir xil savol matni bilan keladi, "
                "shuning uchun ularni <u>variantlardan</u> ajratasiz: "
                "tinish belgilari farq qilsa — Boundaries; fe'l, olmosh yoki "
                "apostrof farq qilsa — Form, Structure and Sense.")
        )},

        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Reading and Writing bo'limida "
                "grammatika va uslub savollari taxminan qancha ulushni tashkil "
                "qiladi?</p>"
            ),
            "choices": [
                {"text": "Taxminan 46 foiz — 54 savoldan ~25 tasi", "is_correct": True},
                {"text": "Taxminan 20 foiz — 54 savoldan ~11 tasi", "is_correct": False},
                {"text": "Taxminan 75 foiz — bo'limning katta qismi", "is_correct": False},
                {"text": "Aniq ulush yo'q — har imtihonda tasodifiy", "is_correct": False},
            ],
            "explanation": (
                why([
                    (True, "Taxminan 46 foiz — 54 savoldan ~25 tasi",
                     "Standard English Conventions ~26% va Expression of Ideas "
                     "~20%, birgalikda ~46%. Bu deyarli yarmi — va ko'p "
                     "o'quvchi bu yarmiga umuman tayyorlanmaydi."),
                    (False, "Taxminan 20 foiz — 54 savoldan ~11 tasi",
                     "20% — bu faqat <u>Expression of Ideas</u>ning ulushi. "
                     "Grammatika (Conventions) unga qo'shilmagan."),
                    (False, "Taxminan 75 foiz — bo'limning katta qismi",
                     "juda yuqori: o'qish domenlari (Craft and Structure "
                     "~28% + Information and Ideas ~26%) o'zi ~54%."),
                    (False, "Aniq ulush yo'q — har imtihonda tasodifiy",
                     "College Board har domen uchun savol oralig'ini "
                     "e'lon qiladi; taqsimot barqaror."),
                ])
            ),
        },

        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Savolda to'rt variant shunday: "
                "<em>students · student's · students' · students's</em>. "
                "Matnni o'qishdan oldin nimani bilib oldingiz?</p>"
            ),
            "choices": [
                {"text": "Bu ko'plik va egalik savoli — otdan keyin nima kelishini tekshirishim kerak", "is_correct": True},
                {"text": "Bu bog'lovchi so'z savoli — ikki gap orasidagi munosabatni topaman", "is_correct": False},
                {"text": "Bu qaydlardan jumla qurish savoli — maqsad jumlasini qidiraman", "is_correct": False},
                {"text": "Hech nima — variantlar savol turini ko'rsatmaydi", "is_correct": False},
            ],
            "explanation": (
                why([
                    (True, "Bu ko'plik va egalik savoli",
                     "to'rtala variant ham bitta otning shakllari, va farq "
                     "faqat apostrofda. Bu <em>Form, Structure and Sense</em> "
                     "turi, va savol bitta narsani so'raydi: bu yerda ko'plik "
                     "kerakmi, egalik kerakmi, va egasi bittami yoki ko'pmi."),
                    (False, "Bu bog'lovchi so'z savoli",
                     "Transitions variantlari <em>however · therefore · for "
                     "example</em> kabi bo'lardi — bir otning shakllari "
                     "emas."),
                    (False, "Bu qaydlardan jumla qurish savoli",
                     "Rhetorical Synthesis variantlari <u>to'liq jumlalar</u> "
                     "bo'ladi, va savoldan oldin qaydlar ro'yxati "
                     "turadi."),
                    (False, "Hech nima — variantlar savol turini ko'rsatmaydi",
                     "aksincha: bu yarmda variantlar orasidagi farq deyarli "
                     "har doim savolning mavzusini aytadi. Bu bepul "
                     "ma'lumot."),
                ])
            ),
        },

        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Imtihonda 20 daqiqa qoldi va "
                "12 savol javobsiz: 6 tasi Conventions, 6 tasi uzun o'qish "
                "savoli. Qaysi tartibda ishlaysiz?</p>"
            ),
            "choices": [
                {"text": "Avval 6 ta Conventions — ular tezroq, keyin qolgan vaqtni o'qish savollariga beraman", "is_correct": True},
                {"text": "Ketma-ket, savollar tartibida — sakrash chalkashtiradi", "is_correct": False},
                {"text": "Avval o'qish savollari — ular qiyinroq, shuning uchun ko'proq vaqt kerak", "is_correct": False},
                {"text": "Farqi yo'q — hammasi bir xil vaqt oladi", "is_correct": False},
            ],
            "explanation": (
                "<p>Imtihonda <mark>hamma savol bir xil ball</mark>. Demak vaqt "
                "qolganda eng ko'p <u>savol</u> yechish kerak, eng qiyin "
                "savolni emas.</p>"
                + why([
                    (True, "Avval 6 ta Conventions — ular tezroq",
                     "Conventions savoli o'rtacha 30 soniya, uzun o'qish "
                     "savoli 90. 20 daqiqada oltita grammatika savolini "
                     "yechib, qolgan ~17 daqiqani o'qishga berish — "
                     "eng ko'p ball beradigan tartib."),
                    (False, "Avval o'qish savollari — ular qiyinroq",
                     "qiyinroq savol ko'proq ball bermaydi. Bu tartib "
                     "oxirida oson savollarni yo'qotadi."),
                    (False, "Ketma-ket, savollar tartibida",
                     "Bluebook'da savollar orasida erkin yurish mumkin va "
                     "belgilab qo'yish tugmasi bor. Tartibga qat'iy "
                     "amal qilish bepul ballni tashlab ketishdir."),
                    (False, "Farqi yo'q — hammasi bir xil vaqt oladi",
                     "bu noto'g'ri: matn uzunligi ham, fikrlash turi ham "
                     "boshqacha."),
                ])
            ),
        },

        {
            "rich_text": (
                "<p><strong>Amaliyot 4.</strong> Nega grammatika savollari "
                "o'qish savollaridan «arzonroq» hisoblanadi?</p>"
            ),
            "choices": [
                {"text": "Qoidalar aniq: javob mulohazaga emas, tekshirib bo'ladigan qoidaga tayanadi", "is_correct": True},
                {"text": "Ular kamroq ball keltiradi, shuning uchun ularga kam vaqt sarflanadi", "is_correct": False},
                {"text": "Ularda faqat ikkita variant bo'ladi", "is_correct": False},
                {"text": "Ular imtihonning oxirida keladi va odatda osonroq bo'ladi", "is_correct": False},
            ],
            "explanation": (
                why([
                    (True, "Qoidalar aniq: javob mulohazaga emas, tekshirib bo'ladigan qoidaga tayanadi",
                     "vergul ikki mustaqil gapni bog'lay olmaydi — bu qoida, "
                     "did emas. Shuning uchun bu savollarda «ikkilanish» "
                     "deyarli bo'lmaydi, va o'rganilgan qoida har safar "
                     "ishlaydi."),
                    (False, "Ular kamroq ball keltiradi",
                     "<strong>noto'g'ri va xavfli:</strong> hamma savol bir "
                     "xil ball turadi. «Arzon» degani <u>vaqt</u> jihatdan "
                     "arzon."),
                    (False, "Ularda faqat ikkita variant bo'ladi",
                     "hamma savolda to'rtta variant."),
                    (False, "Ular imtihonning oxirida keladi va odatda osonroq",
                     "guruh tartibi Bluebook'da kuzatiladi, lekin "
                     "«oxirida = oson» degan qoida yo'q — har guruh ichida "
                     "oson → qiyin."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">conventions</div><div class="pp-card-back">qabul qilingan qoidalar, me\'yorlar</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">Standard English</div><div class="pp-card-back">me\'yoriy yozma ingliz tili</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to conform to ~</div><div class="pp-card-back">~ ga mos kelmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a transition</div><div class="pp-card-back">bog\'lovchi so\'z yoki ibora</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a clause</div><div class="pp-card-back">gap bo\'lagi (ega + kesim)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">punctuation</div><div class="pp-card-back">tinish belgilari</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">possessive</div><div class="pp-card-back">egalik shakli (student\'s)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to flag a question</div><div class="pp-card-back">savolni belgilab qo\'ymoq (keyin qaytish uchun)</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Bu yarim — imtihonning <strong>~46 foizi</strong>: "
              "Conventions ~26%, Expression ~20%.</li>"
              "<li>Savollar tezroq: matn qisqa, savol o'zgarmas, javob "
              "<u>bahssiz</u>.</li>"
              "<li><strong>Variantlar orasidagi farq savolning mavzusini "
              "aytadi</strong> — matndan oldin qarang.</li>"
              "<li>Hamma savol bir xil ball: vaqt qolganda "
              "<u>tez</u> savollarni oling.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 2
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_WSTRAT,
    "title": "SAT R&W W2: There Is No Essay — What “Writing” Means on the Digital SAT",
    "summary": "Bu yarimda siz hech nima yozmaysiz: barcha savol to'rt variantli test. "
               "IELTS va TOPIK odatlarini bu yerga olib kelmang.",
    "order": 2,
    "blocks": [
        {"rich_text": (
            "<h2>Siz hech nima yozmaysiz</h2>"
            "<p>Bo'limning nomi <em>Reading and <strong>Writing</strong></em>, va "
            "bu nom ko'p o'quvchini chalg'itadi. IELTS'da Writing degani insho "
            "yozish; TOPIK'da 쓰기 degani ham yozish. Bu yerda "
            "<mark>yozish yo'q</mark>.</p>"
            + EXAMP.format(
                "<p style=\"font-size:1.06em;margin:0;\">Digital SAT'da "
                "<strong>insho yo'q</strong>. U 2021-yilda bekor qilingan va "
                "raqamli formatga umuman kirmagan. Siz birorta jumla ham "
                "yozmaysiz — 54 savolning hammasi to'rt variantli test.</p>")
            + "<p>Unda «Writing» nima degani? U <u>yozuvchining ishini "
            "tanish</u> degani: tayyor matnni o'qib, unda nima "
            "yetishmayotganini yoki nima noto'g'ri ekanini ko'rish. "
            "Ya'ni siz <strong>muallif emas, muharrirsiz</strong>.</p>"
            + '<span class="sr-time">⏱ ~40 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Boshqa imtihonlardan kelgan uch odat — ularni tashlang</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Odat</th><th>Qayerdan</th><th>Nega bu yerda "
              "zarar</th></tr></thead>"
              "<tbody>"
              "<tr><td>Uzun, murakkab jumla yaxshiroq</td><td>IELTS Task 2</td>"
              "<td>SAT'da <u>aniqlik</u> yutadi; eng uzun variant odatda "
              "tuzoq</td></tr>"
              "<tr><td>Rasmiy iboralar ball qo'shadi</td><td>IELTS/TOPIK</td>"
              "<td>Bu yerda ball yo'q — faqat to'g'ri yoki noto'g'ri</td></tr>"
              "<tr><td>Fikrimni bildirishim kerak</td><td>Insho yozish</td>"
              "<td>Sizdan fikr so'ralmaydi; matn allaqachon yozilgan</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<strong>Eng qimmat odat — «chiroylirog'ini tanlash».</strong> "
                "Conventions savolida to'rt variantdan uchtasi "
                "<u>grammatik jihatdan noto'g'ri</u>. Ular chiroyli yoki "
                "xunuk emas — ular <u>xato</u>. Savol did haqida emas.")
        )},

        {"rich_text": (
            "<h3>Nima aslida tekshiriladi</h3>"
            "<p>Ikki domen, to'rt tur — va ularning hech biri ijod "
            "so'ramaydi:</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>Boundaries</strong> — gapni "
              "qayerda tugatish va qanday belgi bilan bog'lash. "
              "Vergul, nuqta, nuqtali vergul, ikki nuqta, tire.</p></div>"
            + "<div class=\"pp-step\"><p><strong>Form, Structure, and "
              "Sense</strong> — fe'lning shakli, ega bilan moslashuv, olmosh, "
              "ko'plik va egalik, aniqlovchining o'rni.</p></div>"
            + "<div class=\"pp-step\"><p><strong>Transitions</strong> — ikki "
              "gap orasidagi munosabatni nomlash va unga mos bog'lovchini "
              "qo'yish (10–16-darslar).</p></div>"
            + "<div class=\"pp-step\"><p><strong>Rhetorical Synthesis</strong> "
              "— berilgan qaydlardan berilgan maqsadga xizmat qiladigan "
              "jumlani tanlash (20–25-darslar).</p></div>"
            + '</div>'
            + NOTE.format(
                "Diqqat qiling: to'rtala turda ham matn <u>sizga "
                "beriladi</u>. Sizning ishingiz — bo'sh joyga to'g'ri "
                "bo'lakni qo'yish. Bu tahrir ishi, ijod emas.")
        )},

        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Digital SAT'ning Reading and "
                "Writing bo'limida siz nechta jumla yozasiz?</p>"
            ),
            "choices": [
                {"text": "Birorta ham — barcha savol to'rt variantli test", "is_correct": True},
                {"text": "Bitta insho, taxminan 250–300 so'z", "is_correct": False},
                {"text": "Qisqa javoblar: har savolga bir-ikki jumla", "is_correct": False},
                {"text": "Faqat ikkinchi moduldagi yozma topshiriqda", "is_correct": False},
            ],
            "explanation": (
                why([
                    (True, "Birorta ham — barcha savol to'rt variantli test",
                     "54 savolning hammasi MCQ. Insho bekor qilingan va "
                     "raqamli formatda umuman yo'q."),
                    (False, "Bitta insho, taxminan 250–300 so'z",
                     "bu <strong>IELTS Task 2</strong>ning tavsifi. SAT "
                     "inshosi 2021-yilda bekor qilingan."),
                    (False, "Qisqa javoblar: har savolga bir-ikki jumla",
                     "qisqa javob shakli SAT'da hech qachon bo'lmagan."),
                    (False, "Faqat ikkinchi moduldagi yozma topshiriqda",
                     "ikkinchi modul birinchisidan faqat <u>qiyinligi</u> "
                     "bilan farq qiladi (adaptiv), shakli bilan emas."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The botanist Agnes Arber argued that a leaf and a stem are not two "
                "different organs but two expressions of one <span "
                "class=\"sr-blank\"></span> idea she developed over four decades of "
                "comparative work.</p>"),
            "choices": [
                {"text": "form, an", "is_correct": True},
                {"text": "form an", "is_correct": False},
                {"text": "form: an", "is_correct": False},
                {"text": "form. An", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu haqiqiy Conventions savoli — birinchisi. "
                "<strong>Variantlar orasidagi farqqa qarang:</strong> "
                "vergul, hech narsa, ikki nuqta, nuqta. Demak bu "
                "<mark>chegara savoli</mark> (Boundaries).</p>"
                "<p>Bo'sh joydan keyingi qism: <em>an idea she developed over "
                "four decades</em> — bu <u>mustaqil gap emas</u>: unda o'z "
                "kesimi yo'q, u <em>one form</em> ni izohlaydigan "
                "qo'shimcha (appozitsiya).</p>"
                + why([
                    (True, "form, an",
                     "vergul appozitsiyani asosiy gapga ulaydi: "
                     "<em>…one form, an idea she developed…</em>. Qo'shimcha "
                     "bo'lak vergul bilan qo'shiladi."),
                    (False, "form. An",
                     "nuqta ikki <u>mustaqil</u> gap orasida bo'ladi. "
                     "<em>An idea she developed over four decades of "
                     "comparative work.</em> — bu gap emas, bo'lak: kesimi "
                     "yo'q. Nuqta uni <strong>fragment</strong>ga "
                     "aylantiradi."),
                    (False, "form: an",
                     "ikki nuqtadan <u>oldin</u> to'liq gap turishi kerak — "
                     "bu yerda turibdi. Lekin ikki nuqta ro'yxat yoki "
                     "izohni e'lon qiladi, va bu yerda qo'shimcha "
                     "shunchaki otga ulanadi. Vergul aniqroq va oddiyroq."),
                    (False, "form an",
                     "hech qanday belgisiz ikki ot yonma-yon qolib ketadi va "
                     "gap o'qib bo'lmaydigan holga keladi."),
                ])
                + NOTE.format(
                    "Agnes Arber (1879–1960) — ingliz botanigi, "
                    "o'simliklarning qiyosiy morfologiyasi bo'yicha ishlagan "
                    "va barg bilan poyaning umumiy asosga ega ekani haqida "
                    "yozgan. Lekin bu savolda botanika bilimi hech nima "
                    "bermaydi — javobni faqat gapning tuzilishi beradi.")
            ),
        },

        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Conventions savolida to'rt "
                "variantdan qanchasi grammatik jihatdan to'g'ri bo'ladi?</p>"
            ),
            "choices": [
                {"text": "Bittasi — qolgan uchtasi aniq bir qoidani buzadi", "is_correct": True},
                {"text": "Ikkitasi to'g'ri, va ulardan chiroylirog'ini tanlash kerak", "is_correct": False},
                {"text": "Hammasi to'g'ri, farq faqat uslubda", "is_correct": False},
                {"text": "Bu savolga qarab o'zgaradi", "is_correct": False},
            ],
            "explanation": (
                why([
                    (True, "Bittasi — qolgan uchtasi aniq bir qoidani buzadi",
                     "shuning uchun bu savollarda ikkilanish bo'lmasligi "
                     "kerak. Ikki variant ham to'g'ri tuyulsa — demak "
                     "ulardan biri buzayotgan qoidani hali "
                     "topmagansiz."),
                    (False, "Ikkitasi to'g'ri, va ulardan chiroylirog'ini tanlash kerak",
                     "<strong>eng zararli tushuncha</strong> va u IELTS'dan "
                     "keladi. SAT «chiroyli»ni o'lchamaydi."),
                    (False, "Hammasi to'g'ri, farq faqat uslubda",
                     "unda savolning javobi bo'lmasdi."),
                    (False, "Bu savolga qarab o'zgaradi",
                     "Conventions savollarida qoida barqaror: bitta to'g'ri "
                     "javob, uchta qoida buzilishi."),
                ])
                + TIP.format(
                    "Ikki variant orasida ikkilansangiz, savolni "
                    "o'zgartiring: «bu ikkitasidan qaysi biri "
                    "<u>yaxshiroq</u>?» emas, balki "
                    "«<strong>bu ikkitasidan qaysi biri qoida "
                    "buzyapti?</strong>» Grammatikada har doim aniq javob "
                    "bor.")
            ),
        },

        {
            "rich_text": (
                "<p><strong>Amaliyot 4.</strong> Quyidagi savol matni qaysi "
                "turga tegishli: <em>«The student wants to emphasise a "
                "difference between the two methods. Which choice most "
                "effectively uses relevant information from the notes to "
                "accomplish this goal?»</em></p>"
            ),
            "choices": [
                {"text": "Rhetorical Synthesis — Expression of Ideas domeni", "is_correct": True},
                {"text": "Boundaries — Standard English Conventions domeni", "is_correct": False},
                {"text": "Transitions — Expression of Ideas domeni", "is_correct": False},
                {"text": "Command of Evidence — Information and Ideas domeni", "is_correct": False},
            ],
            "explanation": (
                why([
                    (True, "Rhetorical Synthesis — Expression of Ideas domeni",
                     "<em>The student wants to…</em> + <em>from the notes</em> "
                     "— bu ikki ibora birgalikda faqat bitta turda uchraydi. "
                     "Savoldan oldin qaydlar ro'yxati bo'ladi."),
                    (False, "Transitions — Expression of Ideas domeni",
                     "domen to'g'ri, tur noto'g'ri: Transitions savoli "
                     "<em>…the most logical transition?</em> deb tugaydi."),
                    (False, "Boundaries — Standard English Conventions domeni",
                     "Conventions savoli <em>…conforms to the conventions of "
                     "Standard English?</em> deb tugaydi va maqsad haqida "
                     "gapirmaydi."),
                    (False, "Command of Evidence — Information and Ideas domeni",
                     "Command of Evidence ham dalil so'raydi, lekin u "
                     "<u>berilgan matndan</u> — o'quvchining qaydlaridan "
                     "emas, va u o'qish yarmida."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">an appositive</div><div class="pp-card-back">appozitsiya — otni izohlovchi qo\'shimcha bo\'lak</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a fragment</div><div class="pp-card-back">to\'liqsiz gap (kesimi yo\'q)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an independent clause</div><div class="pp-card-back">mustaqil gap (o\'zi to\'liq)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to accomplish a goal</div><div class="pp-card-back">maqsadni bajarmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">relevant information</div><div class="pp-card-back">tegishli, kerakli ma\'lumot</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">comparative work</div><div class="pp-card-back">qiyosiy tadqiqot</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to emphasise</div><div class="pp-card-back">ta\'kidlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an expression of ~</div><div class="pp-card-back">~ ning ko\'rinishi, ifodasi</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Insho yo'q.</strong> Siz birorta jumla ham "
              "yozmaysiz — hammasi MCQ.</li>"
              "<li>Siz muallif emas, <strong>muharrir</strong>siz: matn "
              "berilgan, siz bo'lakni tanlaysiz.</li>"
              "<li>IELTS odatlarini tashlang: uzunlik va rasmiylik ball "
              "qo'shmaydi.</li>"
              "<li>Conventions savolida <strong>bitta</strong> variant "
              "to'g'ri, uchtasi <u>qoida buzadi</u>.</li>"
              "<li>Ikkilansangiz savolni o'zgartiring: «qaysi biri qoida "
              "buzyapti?»</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 3
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_WSTRAT,
    "title": "SAT R&W W3: Reading the Whole Sentence Before You Look at the Choices",
    "summary": "Conventions savolining usuli: bo'sh joydan KEYINGI qismni o'qing — "
               "javobni deyarli har doim o'sha qism belgilaydi.",
    "order": 3,
    "blocks": [
        {"rich_text": (
            "<h2>Bo'sh joydan keyingi qism</h2>"
            "<p>Conventions savolida eng ko'p uchraydigan xato juda oddiy: "
            "o'quvchi bo'sh joygacha o'qiydi, variantga qaraydi va "
            "tanlaydi. <mark>Bo'sh joydan keyingi qismni o'qimaydi.</mark></p>"
            "<p>Lekin javobni deyarli har doim aynan o'sha qism belgilaydi. "
            "Sabab tuzilishda: bo'sh joy ikki bo'lakni bog'laydi, va "
            "bog'lash qoidasi <u>ikkala</u> bo'lakka bog'liq.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>The dam was completed in 1974 "
                "<span class=\"sr-blank\"></span> <u>it has never been filled to "
                "capacity.</u></em></p>"
                "<p style=\"margin:8px 0 0;\">Tagi chizilgan qism — "
                "<strong>mustaqil gap</strong> (o'z egasi va kesimi bor). Shuning "
                "uchun bo'sh joyga oddiy vergul qo'yib bo'lmaydi. Buni bilish "
                "uchun bo'sh joydan keyingi qismni o'qish shart edi.</p>")
            + '<span class="sr-time">⏱ ~35 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ikki gap sinovi</h3>"
            "<p>Bu butun Conventions domenidagi eng foydali bitta harakat:</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Bo'sh joyni yoping</strong> va "
              "gapni ikkiga bo'ling: chap bo'lak va o'ng bo'lak.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Har bo'lakni alohida "
              "o'qing.</strong> Savol: «bu o'zi to'liq gapmi?» Ya'ni unda "
              "<u>ega</u> va <u>kesim</u> bormi, va u o'zicha tugaydimi?</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Natijaga qarab belgi "
              "tanlanadi:</strong></p>"
              '<div class="sr-data"><div class="sr-data__scroll">'
              "<table>"
              "<thead><tr><th>Chap</th><th>O'ng</th><th>Ruxsat etilgan</th></tr></thead>"
              "<tbody>"
              "<tr><td>to'liq</td><td>to'liq</td>"
              "<td>nuqta · nuqtali vergul · vergul + <em>and/but/so…</em></td></tr>"
              "<tr><td>to'liq</td><td>to'liqsiz</td>"
              "<td>vergul · ikki nuqta · tire</td></tr>"
              "<tr><td>to'liqsiz</td><td>to'liq</td>"
              "<td>vergul</td></tr>"
              "<tr><td>to'liqsiz</td><td>to'liqsiz</td>"
              "<td>odatda hech qanday belgi kerak emas</td></tr>"
              "</tbody></table>"
              '</div></div></div>'
            + '</div>'
            + TIP.format(
                "Birinchi qator — imtihonda eng ko'p uchraydigani, va u "
                "<strong>vergul splaysi</strong>ni o'ldiradi: ikki to'liq gapni "
                "yolg'iz vergul bog'lay olmaydi. Bu 31-darsning mavzusi, lekin "
                "sinovni hozirdan o'rganib qo'ying.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>Lichens grow on bare rock where nothing else will, and they grow "
                "very slowly — some colonies expand by less than a millimetre a "
                "<span class=\"sr-blank\"></span> makes them useful for dating the "
                "surfaces they sit on.</p>")
            + choices_html([
                "year, this",
                "year. This",
                "year this",
                "year; this,",
            ])
            + "<p><strong>Ikki gap sinovi.</strong> Chap: <em>some colonies expand "
            "by less than a millimetre a year</em> — ega (<em>colonies</em>) va "
            "kesim (<em>expand</em>) bor, to'liq. O'ng: <em>this makes them "
            "useful for dating the surfaces they sit on</em> — ega "
            "(<em>this</em>) va kesim (<em>makes</em>) bor, to'liq.</p>"
            "<p><strong>To'liq + to'liq</strong> → nuqta, nuqtali vergul yoki "
            "vergul + bog'lovchi.</p>"
            + why([
                (True, "year. This",
                 "nuqta ikki mustaqil gapni ajratadi — birinchi qatordagi "
                 "ruxsat etilgan yechim."),
                (False, "year, this",
                 "<strong>vergul splaysi:</strong> yolg'iz vergul ikki to'liq "
                 "gapni bog'lay olmaydi. Bu imtihondagi eng ko'p sinaladigan "
                 "xato."),
                (False, "year this",
                 "hech qanday belgisiz ikki gap qo'shilib ketadi "
                 "(<em>run-on</em>)."),
                (False, "year; this,",
                 "nuqtali vergul o'zi to'g'ri bo'lardi, lekin undan keyingi "
                 "vergul asossiz: <em>this</em> egadan keyin vergul "
                 "qo'yilmaydi."),
            ])
            + NOTE.format(
                "Oxirgi variantga e'tibor bering: unda <u>ikkita</u> belgi bor "
                "va biri to'g'ri. SAT tez-tez shunday qiladi — to'g'ri "
                "belgiga keraksiz ikkinchisini qo'shib, variantni "
                "buzadi. Har belgini alohida tekshiring.")
        )},

        {
            "rich_text": conv_q(
                "<p>The first accurate map of the ocean floor was assembled by hand from "
                "thousands of separate depth soundings, a task that took Marie Tharp "
                "almost two <span class=\"sr-blank\"></span> the result showed a "
                "continuous ridge running down the middle of the Atlantic.</p>"),
            "choices": [
                {"text": "decades;", "is_correct": True},
                {"text": "decades,", "is_correct": False},
                {"text": "decades", "is_correct": False},
                {"text": "decades:", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: <em>The first accurate "
                "map … took Marie Tharp almost two decades</em> — to'liq. "
                "O'ng: <em>the result showed a continuous ridge running down the "
                "middle of the Atlantic</em> — ega (<em>the result</em>), kesim "
                "(<em>showed</em>), to'liq.</p>"
                "<p><strong>To'liq + to'liq</strong> → nuqtali vergul mos "
                "keladi.</p>"
                + why([
                    (True, "decades;",
                     "nuqtali vergul aynan ikki mustaqil, ma'no jihatdan "
                     "bog'liq gapni ulash uchun."),
                    (False, "decades,",
                     "<strong>vergul splaysi</strong> — ikki to'liq gap "
                     "yolg'iz vergul bilan bog'lanmaydi."),
                    (False, "decades",
                     "belgisiz — <em>run-on</em>, ya'ni ikki gap qo'shilib "
                     "ketgan."),
                    (False, "decades:",
                     "ikki nuqtadan oldin to'liq gap bor (bu shart bajarilgan), "
                     "lekin ikki nuqta e'lon qiladi: undan keyin ro'yxat, "
                     "ta'rif yoki tushuntirish kutiladi. Bu yerda esa "
                     "<u>yangi va alohida</u> fakt keladi — natija. "
                     "Nuqtali vergul aniqroq."),
                ])
                + NOTE.format(
                    "Marie Tharp (1920–2006) — okean tubi xaritasini tuzgan "
                    "amerikalik geolog; uning xaritasi Atlantika o'rtasidagi "
                    "tizmani ko'rsatib bergan va litosfera plitalari "
                    "nazariyasiga dalil bo'lgan.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Because the instrument had to survive the vibration of launch and "
                "then operate at close to absolute <span class=\"sr-blank\"></span> "
                "engineers tested it in a chamber that reproduced both conditions at "
                "once.</p>"),
            "choices": [
                {"text": "zero,", "is_correct": True},
                {"text": "zero;", "is_correct": False},
                {"text": "zero", "is_correct": False},
                {"text": "zero:", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: "
                "<em>Because the instrument had to survive … and then operate at "
                "close to absolute zero</em> — <mark>to'liqsiz</mark>. "
                "<em>Because</em> so'zi butun bo'lakni ergash gapga aylantiradi: "
                "u o'zi tugamaydi.</p>"
                "<p>O'ng: <em>engineers tested it in a chamber…</em> — "
                "to'liq.</p>"
                "<p><strong>To'liqsiz + to'liq</strong> → vergul.</p>"
                + why([
                    (True, "zero,",
                     "ergash gap birinchi kelganda undan keyin vergul "
                     "qo'yiladi — jadvalning uchinchi qatori."),
                    (False, "zero;",
                     "nuqtali vergul <u>ikki mustaqil</u> gap orasida "
                     "bo'ladi. Chap bo'lak mustaqil emas."),
                    (False, "zero:",
                     "ikki nuqtadan <u>oldin</u> to'liq gap turishi shart. "
                     "<em>Because…</em> bilan boshlangan bo'lak to'liq "
                     "emas."),
                    (False, "zero",
                     "belgisiz ergash gap asosiy gapga yopishib qoladi va "
                     "o'qish qiyinlashadi; SAT bu yerda vergulni talab "
                     "qiladi."),
                ])
                + TIP.format(
                    "<strong><em>Because · Although · When · If · Since · "
                    "While</em></strong> bilan boshlangan bo'lak "
                    "<u>hech qachon</u> mustaqil gap bo'lmaydi. Bu so'zlarni "
                    "ko'rsangiz, chap bo'lak «to'liqsiz» ekani deyarli hal.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Flatbread is among the oldest prepared foods, and the version baked "
                "against the wall of a tandoor oven has changed very little in a "
                "thousand years. The recipe calls for three ingredients that most "
                "households already <span class=\"sr-blank\"></span> flour, salt "
                "and water.</p>"),
            "choices": [
                {"text": "have:", "is_correct": True},
                {"text": "have,", "is_correct": False},
                {"text": "have;", "is_correct": False},
                {"text": "have", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: <em>The recipe calls "
                "for three ingredients that most households already have</em> — "
                "to'liq. O'ng: <em>flour, salt and water</em> — "
                "<mark>ro'yxat</mark>, gap emas.</p>"
                "<p><strong>To'liq + to'liqsiz</strong> → vergul, ikki nuqta "
                "yoki tire. Ro'yxat e'lon qilinayotgani uchun "
                "<u>ikki nuqta</u> eng aniq belgi.</p>"
                + why([
                    (True, "have:",
                     "ikki nuqtaning asosiy vazifasi shu: to'liq gapdan keyin "
                     "ro'yxat yoki tushuntirish e'lon qilish. Chap bo'lak "
                     "to'liq — shart bajarilgan."),
                    (False, "have;",
                     "nuqtali vergul ikki <u>mustaqil gap</u> orasida "
                     "bo'ladi. <em>flour, salt and water</em> gap emas."),
                    (False, "have,",
                     "vergul grammatik jihatdan halokatli emas, lekin ro'yxat "
                     "ichida allaqachon vergullar bor — qo'shimcha vergul "
                     "chalkashtiradi va ro'yxatni e'lon qilmaydi. SAT bu "
                     "yerda ikki nuqtani talab qiladi."),
                    (False, "have",
                     "belgisiz ro'yxat fe'lga yopishib ketadi: "
                     "<em>already have flour, salt and water</em> — bu boshqa "
                     "ma'no beradi va matnning tuzilishini buzadi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Pigeons find their way home over hundreds of kilometres of "
                "unfamiliar country, and biologists have proposed magnetic sense, "
                "smell and low-frequency sound as <span class=\"sr-blank\"></span> "
                "none of the three explains every result.</p>"),
            "choices": [
                {"text": "explanations, but", "is_correct": True},
                {"text": "explanations,", "is_correct": False},
                {"text": "explanations but", "is_correct": False},
                {"text": "explanations; but,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: <em>Pigeons find … "
                "biologists have proposed … as explanations</em> — to'liq. "
                "O'ng: <em>none of the three explains every result</em> — ega "
                "(<em>none</em>), kesim (<em>explains</em>), to'liq.</p>"
                "<p><strong>To'liq + to'liq</strong> → uchta yechimdan biri. "
                "Va ma'no <u>qarama-qarshi</u>, shuning uchun "
                "<em>but</em> mos.</p>"
                + why([
                    (True, "explanations, but",
                     "vergul + bog'lovchi (FANBOYS) — ikki mustaqil gapni "
                     "ulashning uchinchi qonuniy usuli, va <em>but</em> "
                     "ma'noni to'g'ri beradi."),
                    (False, "explanations, ",
                     "<strong>vergul splaysi:</strong> vergul yolg'iz "
                     "o'zi yetmaydi — unga bog'lovchi kerak."),
                    (False, "explanations but",
                     "bog'lovchi bor, lekin vergul yo'q. Ikki mustaqil gapni "
                     "ulaganda <em>and · but · so</em> oldidan vergul "
                     "qo'yiladi."),
                    (False, "explanations; but,",
                     "nuqtali vergul o'zi to'g'ri bo'lardi, lekin undan keyin "
                     "<em>but</em> ortiqcha, va <em>but</em> dan keyingi "
                     "vergul umuman asossiz. Yana «to'g'ri belgi + keraksiz "
                     "qo'shimcha» tuzog'i."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a comma splice</div><div class="pp-card-back">vergul splaysi — ikki gapni vergul bilan bog\'lash xatosi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a run-on sentence</div><div class="pp-card-back">belgisiz qo\'shilib ketgan ikki gap</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a dependent clause</div><div class="pp-card-back">ergash gap (o\'zi to\'liq emas)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a semicolon</div><div class="pp-card-back">nuqtali vergul ( ; )</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a colon</div><div class="pp-card-back">ikki nuqta ( : )</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">FANBOYS</div><div class="pp-card-back">for, and, nor, but, or, yet, so</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a depth sounding</div><div class="pp-card-back">chuqurlik o\'lchovi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">absolute zero</div><div class="pp-card-back">mutlaq nol (−273 °C)</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Bo'sh joydan keyingi qismni o'qing</strong> — javobni "
              "u belgilaydi.</li>"
              "<li><strong>Ikki gap sinovi:</strong> chap to'liqmi? o'ng "
              "to'liqmi?</li>"
              "<li>To'liq + to'liq → nuqta · nuqtali vergul · vergul + "
              "<em>and/but/so</em>.</li>"
              "<li>To'liq + to'liqsiz → vergul · ikki nuqta · tire. "
              "To'liqsiz + to'liq → vergul.</li>"
              "<li><em>Because · Although · When · If · Since</em> bo'lakni "
              "<u>to'liqsiz</u> qiladi.</li>"
              "<li>Tuzoq: <strong>to'g'ri belgi + keraksiz ikkinchi "
              "belgi</strong>.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 10
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_TRANS,
    "title": "SAT R&W W10: Transitions — Find the Relationship First, the Word Second",
    "summary": "Bog'lovchi savolining butun usuli: variantlarni yopib, ikki gap "
               "orasidagi munosabatni o'zbekcha nomlang — keyingina so'zni tanlang.",
    "order": 10,
    "blocks": [
        {"rich_text": (
            "<h2>Avval munosabat, keyin so'z</h2>"
            "<p><strong>Transitions</strong> — <em>Expression of Ideas</em> "
            "domenining eng ko'p uchraydigan turi. Savol o'zgarmaydi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\"><em>Which choice completes "
                "the text with the most logical transition?</em></p>")
            + "<p>Ekranda ikki gap bo'ladi va ular orasida bo'sh joy. To'rtta "
            "variant — bog'lovchi so'zlar: <em>However · Therefore · For "
            "example · Similarly</em>.</p>"
            "<p>Bu tur o'zbek o'quvchi uchun ayniqsa qulay, chunki "
            "<mark>lug'at deyarli kerak emas</mark>: bog'lovchilar oz sonli va "
            "ularning ma'nosi aniq. Kerak bo'lgani — ikki gap orasidagi "
            "munosabatni to'g'ri o'qish.</p>"
            + '<span class="sr-time">⏱ ~45 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Usul — uch qadam</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Variantlarni yoping.</strong> "
              "Bu 11-darsdagi qoidaning aynan o'zi. To'rtta bog'lovchini "
              "ko'rgan miya ularni «sinab ko'ra» boshlaydi va har biri "
              "o'tadigandek tuyuladi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Ikki gapni alohida o'qing "
              "va munosabatni <u>o'zbekcha</u> ayting.</strong> "
              "«Ikkinchisi birinchisiga qarshi.» «Ikkinchisi birinchisining "
              "natijasi.» «Ikkinchisi misol.» Uch-to'rt so'z "
              "yetadi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Endi variantlarni oching</strong> "
              "va o'sha munosabatga mos so'zni toping. Odatda faqat "
              "bittasi mos keladi.</p></div>"
            + '</div>'
            + WARN.format(
                "2-qadamni tashlab ketgan o'quvchi har safar bir xil xatoni "
                "qiladi: u bog'lovchini gapga <u>qo'yib o'qiydi</u> va "
                "«yomon eshitilmadi» deb tanlaydi. Lekin bog'lovchi so'zlar "
                "grammatik jihatdan hammasi joyiga tushadi — "
                "<strong>quloq bu savolni yecholmaydi</strong>.")
        )},

        {"rich_text": (
            "<h3>Munosabatlarning to'liq ro'yxati</h3>"
            "<p>Amalda SAT beshta munosabatdan foydalanadi. Ro'yxat qisqa — "
            "uni bilib olsangiz, tur butunlay ochiladi:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Munosabat</th><th>O'zbekcha</th><th>Bog'lovchilar</th></tr></thead>"
              "<tbody>"
              "<tr><td>Contrast</td><td>ikkinchisi birinchisiga qarshi</td>"
              "<td><em>however · nevertheless · in contrast · on the other "
              "hand · still</em></td></tr>"
              "<tr><td>Cause / result</td><td>ikkinchisi natija</td>"
              "<td><em>therefore · consequently · as a result · thus · "
              "hence</em></td></tr>"
              "<tr><td>Addition</td><td>ikkinchisi qo'shimcha</td>"
              "<td><em>moreover · furthermore · in addition · also</em></td></tr>"
              "<tr><td>Example</td><td>ikkinchisi misol</td>"
              "<td><em>for example · for instance · specifically</em></td></tr>"
              "<tr><td>Sequence / time</td><td>ikkinchisi keyin sodir bo'ldi</td>"
              "<td><em>then · meanwhile · afterward · finally</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + NOTE.format(
                "Bularga yana ikkitasi qo'shiladi va ular 14-darsda "
                "ko'riladi: <strong>concession</strong> "
                "(<em>admittedly · to be sure</em>) va "
                "<strong>emphasis</strong> (<em>indeed · in fact</em>).")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + trans_q(
                "<p>Wind turbines are usually sited where the wind is strongest, and on "
                "most coasts that means the exposed headlands. Turbines on headlands are "
                "harder to reach for maintenance, and a machine that cannot be repaired "
                "quickly earns nothing while it waits. "
                "<span class=\"sr-blank\"></span> some operators now accept a slightly "
                "weaker site in exchange for a road that stays open in winter.</p>")
            + choices_html([
                "For example,",
                "Therefore,",
                "Nevertheless,",
                "Similarly,",
            ])
            + "<p><strong>2-qadam — munosabatni ayting.</strong> Birinchi qism: "
            "eng shamolli joylar borishga qiyin, va tuzatilmagan turbina pul "
            "keltirmaydi. Ikkinchi qism: shuning uchun ba'zi operatorlar "
            "zaifroq joyni tanlaydi.</p>"
            "<p>O'zbekcha: «birinchisi muammo, ikkinchisi — "
            "<mark>shundan kelib chiqqan qaror</mark>». Bu "
            "<strong>natija</strong>.</p>"
            + why([
                (True, "Therefore,",
                 "natija bog'lovchisi. Muammo → qaror zanjiri aynan shu "
                 "so'zni talab qiladi."),
                (False, "Nevertheless,",
                 "qarshilik bog'lovchisi: «shunga qaramay». Bu ikkinchi gapni "
                 "birinchisiga <u>qarshi</u> qo'yardi — lekin u qarshi emas, "
                 "u undan kelib chiqadi."),
                (False, "For example,",
                 "misol bog'lovchisi. Ikkinchi gap birinchi gapning misoli "
                 "emas — u boshqa narsa haqida (operatorlarning qarori)."),
                (False, "Similarly,",
                 "o'xshashlik bog'lovchisi: ikki o'xshash holat "
                 "solishtirilganda ishlatiladi. Bu yerda ikkinchi holat "
                 "yo'q."),
            ])
            + TIP.format(
                "E'tibor bering: <strong>to'rttala variant ham gapga "
                "grammatik jihatdan mukammal tushadi.</strong> Ularning "
                "hech biri «g'alati eshitilmaydi». Faqat mantiq ajratadi — "
                "shuning uchun munosabatni oldindan aytish shart.")
        )},

        {
            "rich_text": trans_q(
                "<p>Museums have long assumed that visitors read the labels beside the "
                "objects. Eye-tracking studies in three galleries found that most "
                "visitors look at a label for under two seconds, which is not long "
                "enough to read a sentence. <span class=\"sr-blank\"></span> the "
                "information most curators consider essential is reaching almost "
                "nobody.</p>"),
            "choices": [
                {"text": "In other words,", "is_correct": True},
                {"text": "Nevertheless,", "is_correct": False},
                {"text": "For instance,", "is_correct": False},
                {"text": "Meanwhile,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Munosabat:</strong> ikkinchi gap birinchisining "
                "natijasini <u>boshqa so'zlar bilan qaytaradi</u> — ikki "
                "soniya o'qishga yetmaydi, ya'ni ma'lumot yetib "
                "bormayapti. Bu <mark>qayta ifodalash</mark>.</p>"
                + why([
                    (True, "In other words,",
                     "aynan qayta ifodalash: xuddi shu faktni xulosa shaklida "
                     "takrorlaydi. (<em>Therefore</em> ham yaqin bo'lardi, "
                     "lekin variantlar orasida yo'q.)"),
                    (False, "Nevertheless,",
                     "qarshilik — lekin ikkinchi gap birinchisiga zid emas, "
                     "u undan kelib chiqadi."),
                    (False, "For instance,",
                     "misol kutiladi, lekin ikkinchi gap misol emas — u "
                     "umumiy xulosa."),
                    (False, "Meanwhile,",
                     "vaqt bog'lovchisi: bir vaqtda sodir bo'lgan boshqa "
                     "voqeani kiritadi. Bu yerda vaqt umuman muhim "
                     "emas."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Most edible mushrooms cannot be farmed, because they grow only in "
                "partnership with the roots of living trees and die when the tree is "
                "cut. <span class=\"sr-blank\"></span> the button mushroom grows on "
                "composted straw and needs no tree at all, which is why it is the one "
                "sold everywhere.</p>"),
            "choices": [
                {"text": "By contrast,", "is_correct": True},
                {"text": "As a result,", "is_correct": False},
                {"text": "Similarly,", "is_correct": False},
                {"text": "In addition,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Munosabat:</strong> birinchi gap — ko'p "
                "qo'ziqorinlar daraxtsiz yashay olmaydi. Ikkinchi gap — "
                "shampinyon daraxtsiz o'sadi. Ikki holat "
                "<mark>bir-biriga qarama-qarshi</mark>.</p>"
                + why([
                    (True, "By contrast,",
                     "aynan ikki qarama-qarshi holatni yonma-yon qo'yadi: "
                     "ko'pchilik ↔ shampinyon."),
                    (False, "Similarly,",
                     "<strong>to'g'ridan-to'g'ri teskari</strong> — o'xshashlik "
                     "bildiradi, holbuki bu yerda farq bor. Eng ko'p "
                     "tanlanadigan noto'g'ri javob."),
                    (False, "As a result,",
                     "natija bog'lovchisi: shampinyonning somonda o'sishi "
                     "boshqa qo'ziqorinlarning daraxtga bog'liqligidan kelib "
                     "chiqmaydi."),
                    (False, "In addition,",
                     "qo'shimcha bildiradi — ya'ni ikkinchi gap birinchisini "
                     "<u>kuchaytirishi</u> kerak edi. U esa istisnoni "
                     "beryapti."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>A language with no written form is not a language without rules. "
                "Speakers of such languages correct children who put words in the wrong "
                "order, and they agree with one another about which sentences are "
                "impossible. <span class=\"sr-blank\"></span> a speaker asked to explain "
                "the rule can rarely state it, though the same speaker applies it "
                "without error.</p>"),
            "choices": [
                {"text": "However,", "is_correct": True},
                {"text": "Consequently,", "is_correct": False},
                {"text": "For example,", "is_correct": False},
                {"text": "Moreover,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Munosabat:</strong> birinchi qism — so'zlovchilar "
                "qoidalarni <u>biladi</u> (tuzatadi, kelishadi). Ikkinchi "
                "qism — lekin ularni <u>ayta olmaydi</u>. Bu "
                "<mark>kutilmagan burilish</mark>.</p>"
                + why([
                    (True, "However,",
                     "qarshilik: bilish bor, ifodalash yo'q. <em>though the "
                     "same speaker applies it without error</em> bo'lagi ham "
                     "shu ziddiyatni kuchaytiradi."),
                    (False, "Moreover,",
                     "qo'shimcha bildiradi, ya'ni ikkinchi gap birinchisini "
                     "quvvatlashi kerak edi. Aslida u kutilgan narsani "
                     "buzadi."),
                    (False, "Consequently,",
                     "natija: qoidalarni bilish qoidani ayta olmaslikni "
                     "keltirib chiqarmaydi."),
                    (False, "For example,",
                     "misol emas: ikkinchi gap yangi va qarama-qarshi fakt "
                     "beradi."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Reintroducing a lost species is often described as putting things "
                "back as they were. The habitat, however, has usually changed in the "
                "animal's absence: other species have expanded into the space it left, "
                "and the vegetation has grown up differently. "
                "<span class=\"sr-blank\"></span> the returning animal enters a place "
                "that no longer matches the one its ancestors lived in.</p>"),
            "choices": [
                {"text": "Consequently,", "is_correct": True},
                {"text": "Nonetheless,", "is_correct": False},
                {"text": "For instance,", "is_correct": False},
                {"text": "Earlier,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Munosabat:</strong> yashash muhiti o'zgargan "
                "(sabab) → qaytgan hayvon boshqa joyga tushadi (natija). "
                "Diqqat: <em>however</em> allaqachon ikkinchi jumlada "
                "ishlatilgan — burilish o'sha yerda bo'lgan, bo'sh joyda "
                "emas.</p>"
                + why([
                    (True, "Consequently,",
                     "natija bog'lovchisi. Ikkinchi jumladagi o'zgarishlar "
                     "ro'yxati bevosita uchinchi jumlaning xulosasiga olib "
                     "boradi."),
                    (False, "Nonetheless,",
                     "<strong>eng jozibali tuzoq:</strong> matnda burilish bor, "
                     "shuning uchun yana bitta qarshilik so'zi to'g'ridek "
                     "tuyuladi. Lekin burilish <u>oldingi</u> jumlada "
                     "sodir bo'lgan; uchinchi jumla unga qarshi emas, "
                     "undan kelib chiqadi."),
                    (False, "For instance,",
                     "uchinchi jumla misol emas — u umumlashtiruvchi "
                     "xulosa."),
                    (False, "Earlier,",
                     "vaqt bog'lovchisi, va yo'nalishi ham noto'g'ri: "
                     "hayvonning qaytishi o'zgarishlardan keyin."),
                ])
                + TIP.format(
                    "<strong>Matndagi boshqa bog'lovchilarni ham "
                    "o'qing.</strong> Agar <em>however</em> yoki "
                    "<em>but</em> allaqachon ishlatilgan bo'lsa, burilish "
                    "o'sha yerda bo'lgan — bo'sh joyda yana bir marta "
                    "burilish kutilmaydi.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">however / nevertheless</div><div class="pp-card-back">lekin, shunga qaramay (qarshilik)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">therefore / consequently</div><div class="pp-card-back">shuning uchun, natijada</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">by contrast</div><div class="pp-card-back">buning aksicha, farqli o\'laroq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">in other words</div><div class="pp-card-back">boshqacha aytganda</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">moreover / furthermore</div><div class="pp-card-back">bundan tashqari (qo\'shimcha)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">for instance</div><div class="pp-card-back">masalan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">meanwhile</div><div class="pp-card-back">shu orada (vaqt)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">similarly</div><div class="pp-card-back">xuddi shunday (o\'xshashlik)</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Variantlarni yoping</strong> — to'rttasi ham "
              "grammatik jihatdan o'tadi.</li>"
              "<li>Munosabatni <u>o'zbekcha</u>, uch-to'rt so'zda ayting.</li>"
              "<li>Besh asosiy munosabat: qarshilik · natija · qo'shimcha · "
              "misol · vaqt.</li>"
              "<li>Eng ko'p tuzoq: <strong>o'xshashlik ↔ qarshilik</strong> "
              "(<em>Similarly</em> / <em>By contrast</em>).</li>"
              "<li>Matndagi <u>boshqa</u> bog'lovchilarni ham o'qing — "
              "burilish allaqachon bo'lgan bo'lishi mumkin.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 11
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_TRANS,
    "title": "SAT R&W W11: Contrast — however, nevertheless, in contrast, on the other hand",
    "summary": "Qarshilik bog'lovchilari bir xil emas: biri kutilmagan burilish, biri "
               "ikki narsani yonma-yon qo'yish, biri bitta masalaning ikki tomoni.",
    "order": 11,
    "blocks": [
        {"rich_text": (
            "<h2>Qarshilikning uch xili</h2>"
            "<p>Qarshilik — Transitions turidagi eng ko'p uchraydigan munosabat, "
            "va shuning uchun SAT uni <mark>ichidan bo'lib</mark> tekshiradi: "
            "to'rtta variantning ikkitasi ham qarshilik bildiradi, va faqat "
            "bittasi to'g'ri turdagi qarshilik bo'ladi.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Bog'lovchi</th><th>Qanday qarshilik</th>"
              "<th>Qachon ishlaydi</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>However</em></td><td>umumiy burilish</td>"
              "<td>Deyarli har qanday qarshilikda; eng xavfsiz</td></tr>"
              "<tr><td><em>Nevertheless · Still</em></td>"
              "<td>«shunga qaramay»</td>"
              "<td>Birinchi gap ikkinchisiga <u>to'sqinlik qilishi</u> "
              "kutilgan, lekin qilmagan</td></tr>"
              "<tr><td><em>By contrast · In contrast</em></td>"
              "<td>yonma-yon qo'yish</td>"
              "<td><u>Ikki alohida narsa</u> solishtirilganda: A shunday, "
              "B esa bunday</td></tr>"
              "<tr><td><em>On the other hand</em></td>"
              "<td>ikki tomon</td>"
              "<td><u>Bitta</u> masalaning ikki qarama-qarshi jihati</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Eng foydali ajratish: <strong><em>By contrast</em> ikkita "
                "SUBYEKT talab qiladi</strong> — ikki hayvon, ikki shahar, "
                "ikki usul. Agar ikkinchi gap birinchisi bilan bir xil narsa "
                "haqida bo'lsa, <em>by contrast</em> noto'g'ri; "
                "<em>however</em> to'g'ri.")
            + '<span class="sr-time">⏱ ~45 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + trans_q(
                "<p>Aluminium was once so difficult to separate from its ore that it "
                "cost more than gold, and Napoleon III is said to have reserved "
                "aluminium cutlery for his most honoured guests. "
                "<span class=\"sr-blank\"></span> an electrolytic process discovered in "
                "1886 made the metal cheap enough for saucepans within a "
                "generation.</p>")
            + choices_html([
                "By contrast,",
                "However,",
                "Similarly,",
                "For example,",
            ])
            + "<p><strong>Munosabat:</strong> qimmat edi → keyin arzon bo'ldi. "
            "Bu qarshilik. Endi <u>qaysi turdagi</u>?</p>"
            "<p>Ikkala gap ham <mark>bitta narsa</mark> haqida — alyuminiy. "
            "Ikki alohida subyekt yo'q. Demak <em>by contrast</em> emas.</p>"
            + why([
                (True, "However,",
                 "umumiy burilish: bitta mavzu, vaqt o'tishi bilan holat "
                 "o'zgardi. Eng xavfsiz va bu yerda yagona to'g'ri qarshilik."),
                (False, "By contrast,",
                 "<strong>ikki subyekt talab qiladi</strong>, va bu yerda "
                 "bittasi bor — alyuminiy. Agar ikkinchi gap oltin haqida "
                 "bo'lganida, bu variant to'g'ri bo'lardi."),
                (False, "Similarly,",
                 "o'xshashlik — lekin qimmat va arzon o'xshash emas."),
                (False, "For example,",
                 "misol emas: elektroliz jarayoni qimmatlikning misoli "
                 "emas, uning tugashining sababi."),
            ])
        )},

        {
            "rich_text": trans_q(
                "<p>Emperor penguins breed on sea ice through the Antarctic winter, "
                "incubating a single egg in temperatures that fall below −40 °C. "
                "<span class=\"sr-blank\"></span> king penguins, which look similar and "
                "live on the same continent, breed on bare ground and raise their chick "
                "across two summers.</p>"),
            "choices": [
                {"text": "By contrast,", "is_correct": True},
                {"text": "Nevertheless,", "is_correct": False},
                {"text": "Consequently,", "is_correct": False},
                {"text": "In addition,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki subyekt bormi?</strong> Ha: imperator "
                "pingvinlari va qirol pingvinlari. Ular yonma-yon "
                "qo'yilyapti, va matn buni ochiq aytadi "
                "(<em>which look similar</em>).</p>"
                + why([
                    (True, "By contrast,",
                     "aynan ikki alohida turni solishtirish uchun. Ikkala "
                     "shart ham bajarilgan: ikki subyekt va qarama-qarshi "
                     "xususiyat."),
                    (False, "Nevertheless,",
                     "«shunga qaramay» — bu bitta subyektning kutilmagan "
                     "harakati uchun. Qirol pingvinining boshqacha yashashi "
                     "imperator pingviniga qaramay emas."),
                    (False, "Consequently,",
                     "natija: bir turning sovuqda yashashi ikkinchisining "
                     "boshqacha yashashiga sabab bo'lmaydi."),
                    (False, "In addition,",
                     "qo'shimcha bildiradi, ya'ni ikkinchi gap birinchisini "
                     "quvvatlashi kerak edi. U esa farqni ko'rsatadi."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>The manuscript was buried in a cellar for the whole of the war, in a "
                "building that was shelled twice and then stood open to the weather for "
                "two winters. <span class=\"sr-blank\"></span> when the box was opened in "
                "1948 every page was legible.</p>"),
            "choices": [
                {"text": "Nevertheless,", "is_correct": True},
                {"text": "By contrast,", "is_correct": False},
                {"text": "Therefore,", "is_correct": False},
                {"text": "Meanwhile,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Qaysi turdagi qarshilik?</strong> Birinchi gap "
                "qo'lyozmaning <u>halok bo'lishini</u> kutdiradi: bombardimon, "
                "ochiq havo, ikki qish. Ikkinchi gap esa u omon qolganini "
                "aytadi.</p>"
                "<p>Ya'ni birinchisi ikkinchisiga <mark>to'sqinlik qilishi "
                "kerak edi, lekin qilmadi</mark> — bu "
                "<em>nevertheless</em> ning aniq holati.</p>"
                + why([
                    (True, "Nevertheless,",
                     "«shunga qaramay» — kutilgan to'siq va kutilmagan "
                     "natija. Jadvaldagi ikkinchi qator."),
                    (False, "By contrast,",
                     "ikki subyekt yo'q — ikkala gap ham bitta qo'lyozma "
                     "haqida."),
                    (False, "Therefore,",
                     "<strong>to'g'ridan-to'g'ri teskari:</strong> qo'lyozmaning "
                     "o'qilishi bombardimondan kelib chiqmaydi."),
                    (False, "Meanwhile,",
                     "vaqt bog'lovchisi: bir vaqtda sodir bo'lgan boshqa "
                     "voqeani kiritadi. 1948-yil urushdan keyin, "
                     "bir vaqtda emas."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Building a tram line costs several times as much per kilometre as "
                "adding a bus route, and the money is spent before a single passenger is "
                "carried. <span class=\"sr-blank\"></span> a tram lasts thirty years, "
                "carries more people per driver and does not need the road resurfaced "
                "under it every few winters.</p>"),
            "choices": [
                {"text": "On the other hand,", "is_correct": True},
                {"text": "As a result,", "is_correct": False},
                {"text": "Specifically,", "is_correct": False},
                {"text": "Likewise,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Qaysi turdagi qarshilik?</strong> Ikkala gap ham "
                "bitta masalaning — <u>tramvay qurishga arziydimi</u> — ikki "
                "tomonini beradi: qimmat (minus) va uzoq xizmat qiladi "
                "(plus).</p>"
                "<p>Bu <mark>bitta masalaning ikki tomoni</mark>, ya'ni "
                "<em>on the other hand</em> ning aniq holati.</p>"
                + why([
                    (True, "On the other hand,",
                     "bir qarorning ikki tomonini taroziga qo'yadi. "
                     "Jadvalning to'rtinchi qatori."),
                    (False, "As a result,",
                     "natija: tramvayning uzoq xizmat qilishi uning "
                     "qimmatligidan kelib chiqmaydi."),
                    (False, "Likewise,",
                     "o'xshashlik — lekin xarajat va foyda o'xshash emas, "
                     "qarama-qarshi."),
                    (False, "Specifically,",
                     "aniqlashtirish: ikkinchi gap birinchisining "
                     "tafsiloti bo'lishi kerak edi. U esa butunlay boshqa "
                     "tomonni ochadi."),
                ])
                + NOTE.format(
                    "<em>On the other hand</em> odatda <u>qaror yoki "
                    "baho</u> kontekstida keladi: arziydimi, yaxshimi, "
                    "tanlash kerakmi. Agar matn shunchaki ikki faktni "
                    "solishtirsa (qaror emas), <em>by contrast</em> "
                    "to'g'riroq.")
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Digitising a newspaper archive makes every word searchable, and "
                "researchers who once spent weeks turning pages now find what they need "
                "in minutes. <span class=\"sr-blank\"></span> a search returns only what "
                "the researcher already knows how to ask for, and the discoveries that "
                "came from turning pages at random have become rarer.</p>"),
            "choices": [
                {"text": "However,", "is_correct": True},
                {"text": "Furthermore,", "is_correct": False},
                {"text": "For this reason,", "is_correct": False},
                {"text": "By contrast,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Munosabat:</strong> birinchi gap foydani aytadi, "
                "ikkinchisi kutilmagan zararni. Bu burilish — va ikkala gap "
                "ham <u>bitta narsa</u> (raqamlashtirish) haqida.</p>"
                + why([
                    (True, "However,",
                     "umumiy burilish, bitta mavzu ichida. Bu yerda eng "
                     "xavfsiz va yagona to'g'ri qarshilik."),
                    (False, "By contrast,",
                     "yana <strong>ikki subyekt yo'q</strong> — ikkala gap "
                     "ham raqamlashtirish haqida. Bu darsning asosiy "
                     "ajratishi."),
                    (False, "Furthermore,",
                     "qo'shimcha: ikkinchi gap birinchisining foydasini "
                     "kuchaytirishi kerak edi. U esa uni kamaytiradi."),
                    (False, "For this reason,",
                     "natija: qidiruvning cheklovi qidiruvning tezligidan "
                     "kelib chiqmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">however</div><div class="pp-card-back">lekin (umumiy burilish, bitta mavzu)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">nevertheless / still</div><div class="pp-card-back">shunga qaramay (to\'siq bor edi, lekin bo\'ldi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">by contrast / in contrast</div><div class="pp-card-back">buning aksicha (IKKI subyekt kerak)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">on the other hand</div><div class="pp-card-back">ikkinchi tomondan (bitta masalaning ikki tomoni)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to incubate an egg</div><div class="pp-card-back">tuxumni bosib yotmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">legible</div><div class="pp-card-back">o\'qib bo\'ladigan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to resurface a road</div><div class="pp-card-back">yo\'l qoplamasini yangilamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an electrolytic process</div><div class="pp-card-back">elektroliz jarayoni</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Qarshilik uch xil, va SAT ularni ajratadi.</li>"
              "<li><strong><em>By contrast</em> IKKI subyekt talab "
              "qiladi</strong> — bu darsning asosiy sinovi.</li>"
              "<li><em>Nevertheless</em> = to'siq kutilgan, lekin bo'lmadi.</li>"
              "<li><em>On the other hand</em> = bitta qarorning ikki "
              "tomoni.</li>"
              "<li>Ikkilansangiz <em>However</em> — u eng keng va eng "
              "xavfsiz.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 12
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_TRANS,
    "title": "SAT R&W W12: Result and Cause — therefore, consequently, as a result, thus",
    "summary": "Natija bog'lovchilari deyarli sinonim; qiyinligi ularni bir-biridan "
               "emas, oddiy ketma-ketlikdan ajratishda.",
    "order": 12,
    "blocks": [
        {"rich_text": (
            "<h2>Natija — yoki shunchaki keyin?</h2>"
            "<p>Natija bog'lovchilari — <em>therefore · consequently · as a "
            "result · thus · hence · for this reason</em> — amalda "
            "<mark>bir-birining o'rnini bosadi</mark>. SAT ularni bir-biriga "
            "qarshi qo'yib sinamaydi, chunki farq deyarli yo'q.</p>"
            "<p>Qiyinligi boshqa joyda: <strong>natijani oddiy "
            "ketma-ketlikdan ajratish</strong>. Ikki voqea birin-ketin sodir "
            "bo'lishi mumkin, lekin biri ikkinchisini keltirib chiqarmasligi "
            "mumkin.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><strong>Sinov savoli:</strong> "
                "«agar birinchi gap bo'lmaganida, ikkinchisi ham "
                "bo'lmasmidi?»</p>"
                "<p style=\"margin:8px 0 0;\">Ha → natija "
                "(<em>therefore</em>). Yo'q, u baribir bo'lardi → "
                "ketma-ketlik (<em>then · later · meanwhile</em>).</p>")
            + '<span class="sr-time">⏱ ~45 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + trans_q(
                "<p>Nutmeg grew on a handful of small islands and nowhere else, and for "
                "two centuries a single trading company controlled every tree that "
                "produced it. The company kept the price high by burning surplus stock "
                "in public. <span class=\"sr-blank\"></span> smuggling a single "
                "seedling out of the islands carried a death sentence.</p>")
            + choices_html([
                "Meanwhile,",
                "Consequently,",
                "In contrast,",
                "For example,",
            ])
            + "<p><strong>Sinov savoli:</strong> agar kompaniya narxni "
            "monopoliya bilan ushlab turmaganida, ko'chatni olib chiqish "
            "o'lim jazosiga tortarmidi? Yo'q — jazoning butun sababi "
            "monopoliyani saqlash.</p>"
            "<p>Demak bu <mark>natija</mark>.</p>"
            + why([
                (True, "Consequently,",
                 "monopoliyani saqlash zarurati → shafqatsiz jazo. Sabab va "
                 "oqibat zanjiri to'g'ridan-to'g'ri."),
                (False, "Meanwhile,",
                 "<strong>eng jozibali tuzoq:</strong> matn tarixiy va "
                 "voqealar ketma-ket. Lekin <em>meanwhile</em> "
                 "<u>bog'liqmas</u> parallel voqeani kiritadi, bu yerda esa "
                 "aniq sababiy bog'liqlik bor."),
                (False, "In contrast,",
                 "qarshilik yo'q: jazo monopoliyaga zid emas, uni "
                 "quvvatlaydi."),
                (False, "For example,",
                 "misol emas — jazo narxni ushlab turishning misoli emas, "
                 "uning himoyasi. (Agar gap «kompaniya qattiq choralar "
                 "ko'rdi» bo'lganida, misol to'g'ri bo'lardi.)"),
            ])
        )},

        {
            "rich_text": trans_q(
                "<p>Sound travels about four times faster in water than in air, and a "
                "whale's call can cross an ocean basin. The two ears of a whale are only "
                "a few centimetres apart, which at that speed leaves almost no difference "
                "in arrival time between them. <span class=\"sr-blank\"></span> whales "
                "cannot locate a sound the way land mammals do, and they use a separate "
                "mechanism in the jaw instead.</p>"),
            "choices": [
                {"text": "As a result,", "is_correct": True},
                {"text": "Nevertheless,", "is_correct": False},
                {"text": "Similarly,", "is_correct": False},
                {"text": "Earlier,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Sinov savoli:</strong> agar quloqlar orasidagi "
                "vaqt farqi sezilarli bo'lganida, kitlar quruqlikdagi "
                "sutemizuvchilar kabi yo'nalishni aniqlay olarmidi? Ha. "
                "Demak birinchi fakt ikkinchisini "
                "<mark>keltirib chiqaradi</mark>.</p>"
                + why([
                    (True, "As a result,",
                     "fizik cheklov → boshqa mexanizm. Sabab-oqibat aniq."),
                    (False, "Nevertheless,",
                     "qarshilik — lekin ikkinchi gap birinchisiga zid emas, "
                     "undan kelib chiqadi."),
                    (False, "Similarly,",
                     "o'xshashlik: matn kitlarni quruqlik hayvonlaridan "
                     "<u>farqlaydi</u>, ularga o'xshatmaydi."),
                    (False, "Earlier,",
                     "vaqt bog'lovchisi, va bu yerda vaqt tartibi umuman "
                     "muhokama qilinmaydi."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>The town's weekly market has been held on the same square since the "
                "fourteenth century. The square was repaved in 1890 and again in 1967. "
                "<span class=\"sr-blank\"></span> a covered hall was built along its "
                "northern edge in 1904 and taken down again in the 1950s.</p>"),
            "choices": [
                {"text": "Meanwhile,", "is_correct": True},
                {"text": "Therefore,", "is_correct": False},
                {"text": "Nevertheless,", "is_correct": False},
                {"text": "In other words,", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu savol darsning asosiy ajratishini sinaydi. "
                "<strong>Sinov savoli:</strong> agar maydon 1890 va 1967-yilda "
                "qayta yotqizilmaganida, zal qurilmasmidi? "
                "<mark>Hech qanday aloqasi yo'q</mark> — bular shunchaki "
                "bir joyning turli o'zgarishlari.</p>"
                "<p>Demak bu natija emas, <u>ketma-ketlik</u>.</p>"
                + why([
                    (True, "Meanwhile,",
                     "bog'liq bo'lmagan, parallel o'zgarishni kiritadi. "
                     "Ikkala jumla ham maydonning tarixidan, lekin biri "
                     "ikkinchisini keltirib chiqarmaydi."),
                    (False, "Therefore,",
                     "<strong>bu darsning bosh tuzog'i:</strong> voqealar "
                     "ketma-ket kelgani ularni sabab va oqibat qilmaydi. "
                     "Qoplamaning yangilanishi zalning qurilishiga olib "
                     "kelmagan."),
                    (False, "Nevertheless,",
                     "qarshilik yo'q — ikki fakt bir-biriga zid emas."),
                    (False, "In other words,",
                     "qayta ifodalash: ikkinchi gap birinchisini boshqa "
                     "so'zlar bilan takrorlashi kerak edi. U esa butunlay "
                     "yangi fakt beradi."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>A vaccine must reach a clinic still cold, and in much of the world "
                "the last stretch of that journey is made by motorcycle over unpaved "
                "roads. Ice packs melt in a few hours in such conditions. "
                "<span class=\"sr-blank\"></span> a great deal of engineering effort has "
                "gone into containers that hold their temperature for days without "
                "electricity.</p>"),
            "choices": [
                {"text": "For this reason,", "is_correct": True},
                {"text": "By contrast,", "is_correct": False},
                {"text": "Admittedly,", "is_correct": False},
                {"text": "Afterward,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Sinov savoli:</strong> agar muz bir necha soatda "
                "erimaganida, uzoq muddat sovuq saqlaydigan idishlarga "
                "shuncha mehnat sarflanarmidi? Yo'q. Sabab aniq.</p>"
                + why([
                    (True, "For this reason,",
                     "muammo → unga qaratilgan yechim. "
                     "<em>Therefore</em> va <em>consequently</em> ham to'g'ri "
                     "bo'lardi — ular sinonim, va SAT ularni bir savolda "
                     "raqobatlashtirmaydi."),
                    (False, "By contrast,",
                     "ikki subyekt yo'q va qarama-qarshilik ham yo'q "
                     "(11-dars)."),
                    (False, "Admittedly,",
                     "yon berish bog'lovchisi: «rost, lekin…» ma'nosini "
                     "beradi va undan keyin qarshi dalil kutiladi. Bu yerda "
                     "qarshi dalil yo'q."),
                    (False, "Afterward,",
                     "vaqt: muhandislik ishi muzning erishidan «keyin» "
                     "emas — u <u>shu sababdan</u>."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Fruit trees in a cold climate flower only after a long enough spell "
                "of winter chill, a requirement that stops them blooming during a warm "
                "week in January. Winters in parts of the growing region are now warm "
                "enough that the requirement is not always met. "
                "<span class=\"sr-blank\"></span> orchards there have begun to flower "
                "unevenly, with some trees in blossom while their neighbours are still "
                "bare.</p>"),
            "choices": [
                {"text": "Thus,", "is_correct": True},
                {"text": "However,", "is_correct": False},
                {"text": "For instance,", "is_correct": False},
                {"text": "Likewise,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Sinov savoli:</strong> agar qishlar yetarlicha "
                "sovuq bo'lganida, bog'lar notekis gullarmidi? Yo'q — "
                "notekislikning sababi aynan sovuq talabining "
                "bajarilmasligi.</p>"
                + why([
                    (True, "Thus,",
                     "natija bog'lovchisi, va u <em>therefore</em> bilan bir "
                     "xil ishlaydi. Zanjir: talab bajarilmaydi → gullash "
                     "notekis."),
                    (False, "However,",
                     "qarshilik: uchinchi gap ikkinchisiga zid emas, undan "
                     "kelib chiqadi."),
                    (False, "For instance,",
                     "<strong>eng nozik tuzoq:</strong> notekis gullash "
                     "haqiqatan misolga o'xshaydi. Lekin u ikkinchi gapning "
                     "<u>oqibati</u> — misol emas. Misol bo'lganida u "
                     "«iliq qishning misoli» bo'lardi, «iliq qishning "
                     "natijasi» emas."),
                    (False, "Likewise,",
                     "o'xshashlik — ikkinchi o'xshash holat yo'q."),
                ])
                + TIP.format(
                    "<strong><em>For example</em> va <em>therefore</em> ni "
                    "ajratish:</strong> misol birinchi gapni "
                    "<u>ko'rsatadi</u> (u xuddi shu narsa, faqat "
                    "aniqroq); natija esa <u>undan kelib chiqadi</u> "
                    "(yangi voqea). Bu 13-darsning asosiy mavzusi.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">therefore / thus / hence</div><div class="pp-card-back">shuning uchun, demak (natija)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">consequently / as a result</div><div class="pp-card-back">natijada, oqibatda</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">for this reason</div><div class="pp-card-back">shu sababdan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">meanwhile</div><div class="pp-card-back">shu orada (bog\'liqmas parallel voqea)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a surplus</div><div class="pp-card-back">ortiqcha zaxira</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">winter chill (requirement)</div><div class="pp-card-back">qish sovug\'i talabi (o\'simliklarda)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to bloom / to blossom</div><div class="pp-card-back">gullamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">unpaved road</div><div class="pp-card-back">qoplamasiz, tuproq yo\'l</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Natija bog'lovchilari <strong>sinonim</strong> — SAT ularni "
              "bir-biriga qarshi qo'ymaydi.</li>"
              "<li>Qiyinligi: <strong>natija ↔ ketma-ketlik</strong>.</li>"
              "<li><strong>Sinov savoli:</strong> «birinchi gap bo'lmaganida, "
              "ikkinchisi ham bo'lmasmidi?»</li>"
              "<li>Ha → <em>therefore</em>. Yo'q → <em>meanwhile · then · "
              "later</em>.</li>"
              "<li>Tarixiy matnda ketma-ketlik sabab bo'lib "
              "ko'rinadi — ehtiyot bo'ling.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 13
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_TRANS,
    "title": "SAT R&W W13: Addition and Example — moreover, furthermore, for instance, specifically",
    "summary": "Bitta savol ikkovini ajratadi: ikkinchi gap YANGI fikrmi (qo'shimcha) "
               "yoki o'sha fikrning aniq ko'rinishimi (misol)?",
    "order": 13,
    "blocks": [
        {"rich_text": (
            "<h2>Yangi fikr yoki o'sha fikr?</h2>"
            "<p>Bu ikki oila juda o'xshash tuyuladi va shuning uchun SAT "
            "ularni doimiy ravishda bir savolda uchrashtiradi. Ajratish esa "
            "bitta savol bilan hal bo'ladi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\"><strong>Ikkinchi gap "
                "yangi narsa aytyaptimi, yoki o'shani aniqroq "
                "aytyaptimi?</strong></p>"
                "<p style=\"margin:8px 0 0;\">Yangi narsa → "
                "<em>moreover · furthermore · in addition</em>.<br>"
                "O'shani aniqroq → <em>for example · for instance · "
                "specifically</em>.</p>")
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Bog'lovchi</th><th>Ikkinchi gap nima "
              "qiladi</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>Moreover · Furthermore · In addition</em></td>"
              "<td>Bir xil turdagi <u>ikkinchi</u> dalil qo'shadi</td></tr>"
              "<tr><td><em>For example · For instance</em></td>"
              "<td>Umumiy gapning <u>bitta holatini</u> beradi</td></tr>"
              "<tr><td><em>Specifically · In particular</em></td>"
              "<td>Aytilganni <u>toraytiradi</u>, aniqlashtiradi</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "Farqni sezishning oson yo'li: misol <u>bo'ysunadi</u> — "
                "uni olib tashlasangiz, birinchi gap baribir turadi. "
                "Qo'shimcha esa <u>tenglashadi</u> — uni olib tashlasangiz, "
                "dalilning yarmi yo'qoladi.")
            + '<span class="sr-time">⏱ ~45 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + trans_q(
                "<p>A city's trees do more than shade its streets. Their roots take up "
                "water that would otherwise stand in the drains after a storm, and a "
                "mature street tree can hold several thousand litres over a wet season. "
                "<span class=\"sr-blank\"></span> the leaves trap airborne particles "
                "that would otherwise be breathed in, and a single avenue can measurably "
                "lower the particle count along its length.</p>")
            + choices_html([
                "For example,",
                "Moreover,",
                "Nevertheless,",
                "In other words,",
            ])
            + "<p><strong>Sinov savoli:</strong> uchinchi gap ikkinchisining "
            "misolimi? Yo'q — ildizlar suv haqida, barglar changlar haqida. "
            "Bular <mark>ikki alohida foyda</mark>, bir xil turdagi.</p>"
            "<p>Va olib tashlash sinovi: uchinchi gapni olib tashlasangiz, "
            "«daraxtlar soyadan ko'proq narsa beradi» degan da'vo "
            "zaiflashadi — demak u <u>tenglashadi</u>, bo'ysunmaydi.</p>"
            + why([
                (True, "Moreover,",
                 "ikkinchi, mustaqil foyda qo'shadi. Birinchi jumladagi "
                 "<em>do more than shade</em> aynan ro'yxat kutayotganini "
                 "bildiradi."),
                (False, "For example,",
                 "<strong>bu darsning bosh tuzog'i.</strong> Barglar changni "
                 "ushlashi suvni ushlashning misoli emas — bu boshqa "
                 "mexanizm, boshqa foyda."),
                (False, "In other words,",
                 "qayta ifodalash bo'lardi, ya'ni uchinchi gap ikkinchisini "
                 "boshqa so'z bilan takrorlashi kerak edi."),
                (False, "Nevertheless,",
                 "qarshilik yo'q — ikkala foyda ham bir yo'nalishda."),
            ])
        )},

        {
            "rich_text": trans_q(
                "<p>Not every useful measurement needs an expensive instrument. Rain "
                "gauges maintained by volunteers in their gardens have produced records "
                "longer and denser than any official network in the same region. "
                "<span class=\"sr-blank\"></span> one such record from a single village "
                "runs continuously from 1887 and has been used to correct the national "
                "series twice.</p>"),
            "choices": [
                {"text": "For instance,", "is_correct": True},
                {"text": "Furthermore,", "is_correct": False},
                {"text": "However,", "is_correct": False},
                {"text": "Consequently,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Sinov savoli:</strong> uchinchi gap yangi fikrmi? "
                "Yo'q — u ikkinchi gapdagi umumiy da'voning "
                "(<em>records longer and denser than any official "
                "network</em>) <mark>bitta aniq holati</mark>.</p>"
                "<p>Olib tashlash sinovi: uni olib tashlasangiz, ikkinchi gap "
                "baribir turadi — u shunchaki dalilsiz qoladi. Demak u "
                "<u>bo'ysunadi</u>.</p>"
                + why([
                    (True, "For instance,",
                     "bitta qishloqning bitta yozuvi — umumiy da'voning "
                     "misoli. <em>one such record</em> iborasi buni ochiq "
                     "aytadi."),
                    (False, "Furthermore,",
                     "qo'shimcha bo'lardi, ya'ni yangi va mustaqil dalil "
                     "kerak edi. Bu esa o'sha dalilning ichi."),
                    (False, "However,",
                     "qarshilik yo'q — misol da'voni quvvatlaydi."),
                    (False, "Consequently,",
                     "natija emas: 1887-yildan boshlangan yozuv "
                     "ko'ngillilarning umumiy yutug'idan kelib chiqmaydi, u "
                     "o'sha yutuqning bir qismi."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>The reintroduction programme was judged a success on several "
                "measures. The released birds survived their first winter at rates "
                "comparable to wild-hatched ones, and they bred in their second year. "
                "<span class=\"sr-blank\"></span> the cost per surviving bird fell by "
                "half over the four seasons, as the team learned which release sites "
                "worked.</p>"),
            "choices": [
                {"text": "In addition,", "is_correct": True},
                {"text": "Specifically,", "is_correct": False},
                {"text": "By contrast,", "is_correct": False},
                {"text": "For example,", "is_correct": False},
            ],
            "explanation": (
                "<p>Birinchi jumla <em>several measures</em> deydi — ya'ni "
                "ro'yxat kutilyapti. Ikkinchi jumla ikkita o'lchovni beradi "
                "(omon qolish, ko'payish). Uchinchisi "
                "<mark>uchinchi o'lchovni</mark> qo'shadi — xarajat.</p>"
                + why([
                    (True, "In addition,",
                     "ro'yxatga yangi va boshqa turdagi o'lchov qo'shiladi. "
                     "<em>several measures</em> iborasi buni oldindan "
                     "e'lon qilgan."),
                    (False, "Specifically,",
                     "aniqlashtirish bo'lardi, ya'ni uchinchi gap ikkinchi "
                     "gapdagi o'lchovlarni toraytirishi kerak edi. Xarajat "
                     "esa butunlay boshqa o'lchov."),
                    (False, "For example,",
                     "misol emas — xarajatning tushishi omon qolish "
                     "darajasining misoli emas."),
                    (False, "By contrast,",
                     "qarshilik yo'q: uchala o'lchov ham muvaffaqiyat "
                     "tomonda."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Handwriting analysis has been used to attribute anonymous documents "
                "for over a century, and its practitioners have often disagreed with one "
                "another about the same page. The disagreements cluster in a predictable "
                "place. <span class=\"sr-blank\"></span> they arise most often where the "
                "writing is fast and the letters least fully formed, which is exactly "
                "where a writer's habits are hardest to see.</p>"),
            "choices": [
                {"text": "Specifically,", "is_correct": True},
                {"text": "Moreover,", "is_correct": False},
                {"text": "Nevertheless,", "is_correct": False},
                {"text": "Meanwhile,", "is_correct": False},
            ],
            "explanation": (
                "<p>Ikkinchi jumla umumiy da'vo qiladi: kelishmovchiliklar "
                "<em>a predictable place</em> da to'planadi — lekin qayerda "
                "ekanini aytmaydi. Uchinchi jumla aynan shuni "
                "<mark>aniqlashtiradi</mark>.</p>"
                + why([
                    (True, "Specifically,",
                     "umumiy gapni toraytiradi va aniq javob beradi. Matn "
                     "ataylab «bashorat qilinadigan joy» deb qoldirib, "
                     "keyingi jumlada ochadi."),
                    (False, "Moreover,",
                     "qo'shimcha bo'lardi — yangi, mustaqil fikr kerak edi. "
                     "Bu esa o'sha fikrning ichini ochadi."),
                    (False, "Nevertheless,",
                     "qarshilik yo'q."),
                    (False, "Meanwhile,",
                     "vaqt bog'lovchisi, va parallel voqea yo'q."),
                ])
                + TIP.format(
                    "<strong><em>Specifically</em> ning belgisi:</strong> "
                    "oldingi jumlada <u>ochilmagan</u> ibora bo'ladi — "
                    "«bashorat qilinadigan joy», «ma'lum bir sharoit», "
                    "«bitta guruh». Bunday ibora ko'rsangiz, keyingi jumla "
                    "deyarli har doim uni ochadi.")
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Cast iron is strong in compression and weak in tension, which suits "
                "it to columns and not to beams. Nineteenth-century builders knew this "
                "and used it correctly in most structures. "
                "<span class=\"sr-blank\"></span> the mill floors that failed were "
                "almost all cases where a cast-iron beam had been used to span an "
                "opening that a wrought-iron one should have crossed.</p>"),
            "choices": [
                {"text": "For example,", "is_correct": True},
                {"text": "In addition,", "is_correct": False},
                {"text": "Consequently,", "is_correct": False},
                {"text": "On the other hand,", "is_correct": False},
            ],
            "explanation": (
                "<p>Ikkinchi jumla <em>in most structures</em> deydi — ya'ni "
                "istisnolar bor. Uchinchi jumla o'sha istisnolarni "
                "<mark>ko'rsatadi</mark>: aynan noto'g'ri ishlatilgan "
                "joylar qulagan.</p>"
                "<p>Bu birinchi jumladagi qoidaning (<em>weak in tension</em>) "
                "amaldagi <u>ko'rinishi</u>.</p>"
                + why([
                    (True, "For example,",
                     "qoida amalda qanday ishlashini bitta holat bilan "
                     "ko'rsatadi — misolning aniq ta'rifi."),
                    (False, "In addition,",
                     "yangi va mustaqil fikr bo'lardi. Bu esa o'sha "
                     "qoidaning ko'rinishi."),
                    (False, "Consequently,",
                     "<strong>eng nozik tuzoq:</strong> qulash haqiqatan "
                     "noto'g'ri qo'llashning natijasi. Lekin uchinchi jumla "
                     "ikkinchi jumladan (<em>used it correctly</em>) kelib "
                     "chiqmaydi — u unga <u>istisno misol</u> beradi."),
                    (False, "On the other hand,",
                     "bitta masalaning ikki tomoni emas — uchinchi jumla "
                     "birinchi qoidani tasdiqlaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">moreover / furthermore</div><div class="pp-card-back">bundan tashqari (YANGI fikr)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">in addition</div><div class="pp-card-back">qo\'shimcha ravishda</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">for example / for instance</div><div class="pp-card-back">masalan (o\'sha fikrning holati)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">specifically / in particular</div><div class="pp-card-back">aniqrog\'i, xususan (toraytiradi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">compression / tension</div><div class="pp-card-back">siqilish / cho\'zilish (kuchlar)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to span an opening</div><div class="pp-card-back">ochiq oraliqni bosib o\'tmoq (nur haqida)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a rain gauge</div><div class="pp-card-back">yog\'in o\'lchagich</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to attribute a document</div><div class="pp-card-back">hujjat muallifini aniqlamoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Bitta savol: <strong>yangi fikrmi yoki o'sha fikrning "
              "aniq ko'rinishimi?</strong></li>"
              "<li>Yangi → <em>moreover · furthermore · in addition</em>.</li>"
              "<li>O'shani ko'rsatadi → <em>for example · for "
              "instance</em>.</li>"
              "<li>O'shani toraytiradi → <em>specifically · in "
              "particular</em>.</li>"
              "<li><strong>Olib tashlash sinovi:</strong> misol bo'ysunadi "
              "(olsang gap turadi), qo'shimcha tenglashadi (olsang dalil "
              "yarmi ketadi).</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 14
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_TRANS,
    "title": "SAT R&W W14: Sequence, Concession and Emphasis — meanwhile, admittedly, indeed",
    "summary": "Qolgan uch oila: vaqt ketma-ketligi, yon berish (keyin burilish keladi) "
               "va kuchaytirish (kutilmagan darajaga chiqadi).",
    "order": 14,
    "blocks": [
        {"rich_text": (
            "<h2>Qolgan uch oila</h2>"
            "<p>10-darsdagi beshta munosabatga yana ikkitasi qo'shiladi, va "
            "ular kamroq uchraydi-yu, aniq belgilarga ega — shuning uchun "
            "ularni tanib olish oson.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Oila</th><th>Bog'lovchilar</th><th>Belgisi</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Vaqt</strong></td>"
              "<td><em>then · meanwhile · afterward · finally · "
              "subsequently</em></td>"
              "<td>Sana, davr yoki bosqichlar bor</td></tr>"
              "<tr><td><strong>Yon berish</strong></td>"
              "<td><em>admittedly · to be sure · granted · it is true "
              "that</em></td>"
              "<td>Keyingi jumlada <u>albatta burilish</u> keladi</td></tr>"
              "<tr><td><strong>Kuchaytirish</strong></td>"
              "<td><em>indeed · in fact</em></td>"
              "<td>Ikkinchi gap birinchisidan <u>kuchliroq</u></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<strong>Yon berishning qoidasi:</strong> "
                "<em>Admittedly</em> hech qachon yolg'iz kelmaydi. U "
                "«rost, lekin…» ning birinchi yarmi, va matnda "
                "<u>ikkinchi yarmi ham bo'lishi shart</u>. Agar keyingi "
                "jumlada burilish bo'lmasa — <em>admittedly</em> "
                "noto'g'ri.")
            + '<span class="sr-time">⏱ ~45 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Kuchaytirish: <em>indeed</em> va <em>in fact</em></h3>"
            "<p>Bu ikkovi bir xil ishlaydi va ular <mark>kutilmagan "
            "darajani</mark> bildiradi: birinchi gap biror narsani aytadi, "
            "ikkinchisi «va bu siz o'ylagandan ham kuchliroq» "
            "deydi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>The technique is widely used. "
                "<strong>Indeed</strong>, it is now the only method taught to "
                "students in their first year.</em></p>"
                "<p style=\"margin:8px 0 0;\">Birinchi gap: keng "
                "qo'llaniladi. Ikkinchisi: <u>yagona</u> usul. Zinapoya "
                "yuqoriga qarab ketdi.</p>")
            + TIP.format(
                "Sinov: ikkinchi gap birinchisidan <strong>kuchliroqmi</strong>? "
                "Agar u shunchaki boshqa fakt bo'lsa — bu "
                "<em>moreover</em>, <em>indeed</em> emas. "
                "<em>Indeed</em> zinapoyaning keyingi pog'onasi bo'lishi "
                "kerak.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + trans_q(
                "<p>Learning a musical instrument as an adult is often described as "
                "hopeless, and the beginner's disadvantage is real: children pick up "
                "fingering patterns faster and are less troubled by playing badly in "
                "front of others. <span class=\"sr-blank\"></span> adults learn "
                "notation and theory in a fraction of the time, and studies of amateur "
                "orchestras find that late starters catch up on repertoire within a few "
                "years.</p>")
            + choices_html([
                "Indeed,",
                "Admittedly,",
                "However,",
                "Meanwhile,",
            ])
            + "<p><strong>Munosabat:</strong> birinchi qism kattalarning "
            "kamchiligini tan oladi; ikkinchisi ularning ustunligini "
            "beradi. Bu <mark>burilish</mark>.</p>"
            "<p>Diqqat: yon berish allaqachon <u>birinchi jumla ichida</u> "
            "sodir bo'lgan (<em>the beginner's disadvantage is real</em>). "
            "Demak bo'sh joyda <em>admittedly</em> emas, uning "
            "<u>javobi</u> kerak.</p>"
            + why([
                (True, "However,",
                 "yon berishdan keyingi burilish. Birinchi jumla «rost, "
                 "kamchilik bor» dedi; bo'sh joy «lekin…» ni "
                 "boshlaydi."),
                (False, "Admittedly,",
                 "<strong>eng jozibali tuzoq:</strong> matnda yon berish "
                 "bor, shuning uchun bu so'z tanish tuyuladi. Lekin yon "
                 "berish <u>allaqachon bo'lib bo'lgan</u> — uni ikki marta "
                 "qilib bo'lmaydi."),
                (False, "Indeed,",
                 "kuchaytirish: ikkinchi jumla kattalarning kamchiligini "
                 "yanada kuchliroq qilishi kerak edi. U esa aksini "
                 "qiladi."),
                (False, "Meanwhile,",
                 "vaqt — bu yerda parallel voqea yo'q, mantiqiy qarshilik "
                 "bor."),
            ])
        )},

        {
            "rich_text": trans_q(
                "<p>The plan to run the railway through the pass was abandoned in 1889 "
                "after two surveys showed the gradient was too steep for the locomotives "
                "of the day. <span class=\"sr-blank\"></span> a tunnel eleven kilometres "
                "long was begun on the eastern approach in 1902 and opened, after two "
                "collapses and a change of contractor, in 1913.</p>"),
            "choices": [
                {"text": "Subsequently,", "is_correct": True},
                {"text": "Admittedly,", "is_correct": False},
                {"text": "In fact,", "is_correct": False},
                {"text": "By contrast,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Belgilar:</strong> 1889 → 1902 → 1913. Sanalar "
                "ketma-ket, va ikkinchi jumla birinchisidan "
                "<u>keyin</u> sodir bo'lgan voqeani aytadi. Bu "
                "<mark>vaqt ketma-ketligi</mark>.</p>"
                + why([
                    (True, "Subsequently,",
                     "«keyinchalik» — sanalar ketma-ketligiga aynan mos, va "
                     "u sabab da'vo qilmaydi (tunnel rejaning bekor "
                     "qilinishidan kelib chiqmagan)."),
                    (False, "Admittedly,",
                     "yon berish: undan keyin burilish kutilardi, va "
                     "matnda burilish yo'q."),
                    (False, "In fact,",
                     "kuchaytirish: ikkinchi jumla birinchisining kuchliroq "
                     "shakli emas — u boshqa loyiha haqida."),
                    (False, "By contrast,",
                     "ikki subyekt yonma-yon qo'yilmaydi; bu bir joyning "
                     "ketma-ket tarixi."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Sign languages are sometimes taken to be gestural versions of the "
                "spoken language around them. They are not: their grammar is organised "
                "in space and differs from the spoken grammar at almost every point. "
                "<span class=\"sr-blank\"></span> two sign languages used in countries "
                "that share a spoken language can be mutually "
                "unintelligible.</p>"),
            "choices": [
                {"text": "Indeed,", "is_correct": True},
                {"text": "Nevertheless,", "is_correct": False},
                {"text": "Meanwhile,", "is_correct": False},
                {"text": "Admittedly,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Zinapoya sinovi:</strong> ikkinchi jumla — imo "
                "tillari og'zaki tildan farq qiladi. Uchinchisi — "
                "<u>bir xil og'zaki tilga ega mamlakatlarning imo "
                "tillari bir-birini tushunmaydi</u>. Bu ancha "
                "<mark>kuchliroq</mark> da'vo.</p>"
                + why([
                    (True, "Indeed,",
                     "kuchaytirish: uchinchi jumla ikkinchisining eng keskin "
                     "ko'rinishini beradi — zinapoyaning keyingi "
                     "pog'onasi."),
                    (False, "Nevertheless,",
                     "qarshilik: uchinchi jumla ikkinchisiga zid emas, uni "
                     "quvvatlaydi."),
                    (False, "Admittedly,",
                     "yon berish: keyin burilish kelishi kerak edi, "
                     "kelmaydi."),
                    (False, "Meanwhile,",
                     "vaqt: hech qanday ketma-ketlik yo'q."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Open-source mapping projects are drawn by volunteers and are "
                "therefore uneven: a well-mapped city may sit beside a district with "
                "almost nothing on it. <span class=\"sr-blank\"></span> the coverage is "
                "thinnest in exactly the places where commercial maps are also poor, so "
                "the gap between rich and poor regions is not closed. Yet in the areas "
                "volunteers do cover, the detail exceeds anything a commercial survey "
                "would pay for.</p>"),
            "choices": [
                {"text": "Admittedly,", "is_correct": True},
                {"text": "Consequently,", "is_correct": False},
                {"text": "For instance,", "is_correct": False},
                {"text": "Subsequently,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Yon berishning belgisini qidiring:</strong> "
                "keyingi jumlada burilish bormi? Bor — <em><u>Yet</u> in the "
                "areas volunteers do cover…</em>.</p>"
                "<p>Demak matnning shakli: kamchilik → yana kamchilik "
                "(<mark>yon berish</mark>) → <em>Yet</em> → ustunlik. "
                "Bo'sh joy yon berishning ichida.</p>"
                + why([
                    (True, "Admittedly,",
                     "«rost, buni tan olish kerak» — va uchinchi jumladagi "
                     "<em>Yet</em> uning ikkinchi yarmini beradi. Yon "
                     "berish yolg'iz kelmaydi, va bu yerda kelmagan."),
                    (False, "Consequently,",
                     "natija: qamrovning kambag'al hududlarda yupqaligi "
                     "loyihaning notekisligidan avtomatik kelib "
                     "chiqmaydi — bu alohida, kuchaytiruvchi kamchilik."),
                    (False, "For instance,",
                     "misol emas: bu yangi va jiddiyroq kamchilik, "
                     "notekislikning bitta holati emas."),
                    (False, "Subsequently,",
                     "vaqt ketma-ketligi yo'q."),
                ])
                + TIP.format(
                    "<strong>Yon berish savolini <u>keyingi</u> jumladan "
                    "yeching.</strong> <em>Yet · But · However · Still</em> "
                    "ko'rsangiz — bo'sh joyda <em>admittedly</em> yoki "
                    "<em>to be sure</em> turishi mumkin. Burilish yo'q "
                    "bo'lsa — yo'q.")
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Reading aloud to a child every evening is among the most reliably "
                "useful things a parent can do, and the evidence for it is unusually "
                "consistent across studies. <span class=\"sr-blank\"></span> almost all "
                "of those studies measure vocabulary, which is the easiest outcome to "
                "count and not obviously the most important one. Even so, no other "
                "intervention that has been tried has a better record.</p>"),
            "choices": [
                {"text": "Admittedly,", "is_correct": True},
                {"text": "Consequently,", "is_correct": False},
                {"text": "For instance,", "is_correct": False},
                {"text": "Similarly,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Keyingi jumladan boshlang.</strong> Uchinchi jumla "
                "<em><u>Even so</u></em> bilan boshlanadi \u2014 bu burilish. "
                "Demak bo\u2018sh joydagi jumla <mark>yon berish</mark> "
                "bo\u2018lishi kerak: \u00abrost, bu kamchilik bor\u00bb.</p>"
                "<p>Shakl: da\u2019vo \u2192 <em>admittedly</em> kamchilik \u2192 "
                "<em>even so</em> da\u2019voga qaytish.</p>"
                + why([
                    (True, "Admittedly,",
                     "yon berish, va uning ikkinchi yarmi matnda turibdi "
                     "(<em>Even so</em>). Yolg\u2018iz kelmagan \u2014 shart "
                     "bajarilgan."),
                    (False, "Consequently,",
                     "natija: tadqiqotlarning lug\u2018atni o\u2018lchashi "
                     "dalilning izchilligidan kelib chiqmaydi."),
                    (False, "For instance,",
                     "misol emas \u2014 bu dalilning <u>cheklovi</u>, uning "
                     "ko\u2018rinishi emas."),
                    (False, "Similarly,",
                     "o\u2018xshashlik yo\u2018q; ikkinchi jumla birinchisini "
                     "kuchsizlantiradi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">subsequently</div><div class="pp-card-back">keyinchalik, shundan keyin</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">admittedly / to be sure</div><div class="pp-card-back">rost, tan olish kerak (keyin burilish keladi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">indeed / in fact</div><div class="pp-card-back">haqiqatan ham (kuchaytiradi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">mutually unintelligible</div><div class="pp-card-back">bir-birini tushunmaydigan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a gradient</div><div class="pp-card-back">nishablik, qiyalik darajasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">coverage</div><div class="pp-card-back">qamrov</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">fingering patterns</div><div class="pp-card-back">barmoq qo\'yish naqshlari (musiqada)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">repertoire</div><div class="pp-card-back">repertuar, ijro etiladigan asarlar</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Vaqt: <em>then · meanwhile · subsequently · finally</em> — "
              "sanalar va bosqichlar bor.</li>"
              "<li>Yon berish: <em>admittedly · to be sure</em> — "
              "<strong>keyingi jumlada burilish shart</strong>.</li>"
              "<li>Kuchaytirish: <em>indeed · in fact</em> — ikkinchi gap "
              "<u>kuchliroq</u>, shunchaki boshqa emas.</li>"
              "<li>Yon berish allaqachon bo'lgan bo'lsa, bo'sh joyda uning "
              "<u>javobi</u> keladi.</li>"
              "<li>Yon berish savolini <strong>keyingi jumladan</strong> "
              "yeching.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 15
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_TRANS,
    "title": "SAT R&W W15: The Transition Traps — Two Choices That Mean the Same Thing",
    "summary": "Agar ikki variant deyarli sinonim bo'lsa, ikkovi ham javob emas — "
               "imtihonda ikkita to'g'ri javob bo'lishi mumkin emas.",
    "order": 15,
    "blocks": [
        {"rich_text": (
            "<h2>Ikki sinonim = ikkovi ham noto'g'ri</h2>"
            "<p>Bu Transitions turidagi eng kuchli va eng kam ishlatiladigan "
            "hiyla, va u imtihonning o'z tuzilishidan kelib chiqadi.</p>"
            + EXAMP.format(
                "<p style=\"font-size:1.06em;margin:0;\">Har savolda "
                "<strong>aynan bitta</strong> to'g'ri javob bo'ladi. Demak "
                "agar ikki variant bir xil ma'no bersa — ular ikkovi ham "
                "noto'g'ri, chunki aks holda savolning ikkita javobi "
                "bo'lardi.</p>")
            + "<p>Amaliy natija: variantlar orasida <em>However</em> va "
            "<em>Nevertheless</em> ni ko'rsangiz — javob "
            "<mark>qolgan ikkitasidan biri</mark>. Matnni o'qimasdan turib "
            "yarim savolni yechdingiz.</p>"
            + '<span class="sr-time">⏱ ~35 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Sinonim guruhlar — ularni tanib oling</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Guruh</th><th>Amalda bir xil ishlaydi</th></tr></thead>"
              "<tbody>"
              "<tr><td>Natija</td><td><em>therefore · thus · consequently · "
              "as a result · hence · for this reason</em></td></tr>"
              "<tr><td>Qo'shimcha</td><td><em>moreover · furthermore · "
              "in addition · also · besides</em></td></tr>"
              "<tr><td>Misol</td><td><em>for example · for instance</em></td></tr>"
              "<tr><td>Umumiy qarshilik</td><td><em>however · nevertheless · "
              "nonetheless · still · yet</em></td></tr>"
              "<tr><td>Kuchaytirish</td><td><em>indeed · in fact</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "Bu ro'yxatga ehtiyot bo'lib qarang: <em>however</em> va "
                "<em>by contrast</em> <u>bir guruhda emas</u> (11-dars), "
                "va <em>moreover</em> bilan <em>for example</em> ham "
                "boshqa-boshqa (13-dars). Sinonim degani "
                "<strong>bir xil munosabat</strong> degani, shunchaki "
                "«ikkovi ham qarshilik» degani emas.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + trans_q(
                "<p>The library's rarest books are kept in a room that is deliberately "
                "kept cool and slightly dry, because paper decays faster in warm damp "
                "air. Readers who work there for a full day often complain of the cold. "
                "<span class=\"sr-blank\"></span> the room's conditions are set for the "
                "books rather than for the people, and the librarians hand out blankets "
                "at the door.</p>")
            + choices_html([
                "Therefore,",
                "Nonetheless,",
                "Consequently,",
                "For instance,",
            ])
            + "<p><strong>1-qadam — sinonimlarni toping.</strong> "
            "<em>Therefore</em> va <em>Consequently</em> — bir xil "
            "guruhdan, amalda farqsiz. Demak "
            "<mark>ikkovi ham javob emas</mark>.</p>"
            "<p>Qoldi: <em>Nonetheless</em> va <em>For instance</em>. "
            "Endi faqat shu ikkitasini tekshiramiz.</p>"
            "<p><strong>2-qadam — munosabat.</strong> O'quvchilar sovuqdan "
            "shikoyat qiladi; uchinchi jumla xona <u>kitoblar uchun</u> "
            "sozlanganini aytadi. Ya'ni shikoyat bor, lekin sharoit "
            "o'zgarmaydi — burilish.</p>"
            + why([
                (True, "Nonetheless,",
                 "qarshilik: shikoyatga qaramay sharoit kitoblar uchun "
                 "qolaveradi. Ikki sinonim chiqarib tashlangach, faqat "
                 "shu ma'no mos keladi."),
                (False, "Therefore,",
                 "<strong>sinonim juftlikning yarmi</strong> — "
                 "<em>Consequently</em> bilan bir xil ishlaydi, shuning "
                 "uchun ikkovi ham javob bo'lolmaydi. (Va mantiqan ham "
                 "noto'g'ri: shikoyat sharoitni belgilamagan.)"),
                (False, "Consequently,",
                 "yuqoridagining aynan juftligi. Bu ikkitasini birga "
                 "ko'rish savolni yarmiga qisqartiradi."),
                (False, "For instance,",
                 "misol emas: uchinchi jumla shikoyatning holati emas, "
                 "unga javob."),
            ])
        )},

        {
            "rich_text": trans_q(
                "<p>Tide mills were built where a creek could be dammed at high water and "
                "the stored water released through a wheel as the tide fell. They ran on "
                "a schedule set by the moon rather than by the working day, and a miller "
                "might be at the wheel at three in the morning. "
                "<span class=\"sr-blank\"></span> the mills were abandoned within a "
                "generation of the steam engine, which ran whenever it was "
                "fed.</p>"),
            "choices": [
                {"text": "Unsurprisingly,", "is_correct": True},
                {"text": "Moreover,", "is_correct": False},
                {"text": "In addition,", "is_correct": False},
                {"text": "Admittedly,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>1-qadam — sinonimlar:</strong> <em>Moreover</em> va "
                "<em>In addition</em> bir xil guruhdan. Ikkovi ham "
                "javob emas.</p>"
                "<p>Qoldi: <em>Unsurprisingly</em> va <em>Admittedly</em>.</p>"
                "<p><strong>2-qadam:</strong> tegirmonchi tunda ishlashi kerak "
                "edi; bug' mashinasi istagan vaqtda ishlardi. Tegirmonlarning "
                "tashlab ketilishi <mark>kutilgan natija</mark>.</p>"
                + why([
                    (True, "Unsurprisingly,",
                     "kutilgan natijani bildiradi — natija oilasining bir "
                     "shakli. Oldingi jumla noqulaylikni ko'rsatdi, bu jumla "
                     "uning oqibatini beradi."),
                    (False, "Moreover,",
                     "<strong>sinonim juftlikning yarmi</strong> "
                     "(<em>In addition</em> bilan). Va mantiqan ham "
                     "noto'g'ri: bu qo'shimcha fakt emas, oqibat."),
                    (False, "In addition,",
                     "yuqoridagining juftligi."),
                    (False, "Admittedly,",
                     "yon berish: keyin burilish kutilardi, matnda esa "
                     "burilish yo'q (14-dars)."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Bamboo reaches its full height in a single season and can be cut "
                "every three years without replanting, which makes it attractive as a "
                "building material. <span class=\"sr-blank\"></span> the stems split "
                "along their length when they dry unevenly, and the joints that give "
                "timber its strength cannot be cut into a hollow tube.</p>"),
            "choices": [
                {"text": "However,", "is_correct": True},
                {"text": "Furthermore,", "is_correct": False},
                {"text": "Besides,", "is_correct": False},
                {"text": "For example,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>1-qadam — sinonimlar:</strong> <em>Furthermore</em> "
                "va <em>Besides</em> — ikkovi ham qo'shimcha. Chiqarib "
                "tashlanadi.</p>"
                "<p>Qoldi: <em>However</em> va <em>For example</em>.</p>"
                "<p><strong>2-qadam:</strong> birinchi jumla bambukning "
                "afzalligini beradi, ikkinchisi kamchiligini. Bu "
                "<mark>burilish</mark>, misol emas.</p>"
                + why([
                    (True, "However,",
                     "afzallik → kamchilik. Umumiy qarshilik, bitta mavzu "
                     "ichida."),
                    (False, "For example,",
                     "misol emas: yorilish va bo'g'in muammosi jozibadorlikning "
                     "holati emas, unga qarshi dalil."),
                    (False, "Furthermore,",
                     "<strong>sinonim juftlik</strong> (<em>Besides</em> "
                     "bilan) — ikkovi ham javob bo'lolmaydi. Va yo'nalish "
                     "ham noto'g'ri."),
                    (False, "Besides,",
                     "yuqoridagining juftligi."),
                ])
            ),
        },

        {
            "rich_text": trans_q(
                "<p>A word processor's spell-checker catches misspellings but not the "
                "wrong word correctly spelled, and professional proofreaders still find "
                "several errors per thousand words in checked text. "
                "<span class=\"sr-blank\"></span> the errors it does catch are the ones "
                "a reader would have noticed anyway, while the ones it misses are "
                "precisely those a tired reader slides past.</p>"),
            "choices": [
                {"text": "Worse,", "is_correct": True},
                {"text": "Thus,", "is_correct": False},
                {"text": "As a result,", "is_correct": False},
                {"text": "Meanwhile,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>1-qadam — sinonimlar:</strong> <em>Thus</em> va "
                "<em>As a result</em> — natija oilasidan, amalda bir xil. "
                "Ikkovi ham javob emas.</p>"
                "<p>Qoldi: <em>Worse</em> va <em>Meanwhile</em>.</p>"
                "<p><strong>2-qadam:</strong> ikkinchi jumla birinchisidagi "
                "muammoni <u>yomonlashtiradi</u>: dastur nafaqat xato "
                "qoldiradi, balki aynan sezilmaydiganlarini qoldiradi. Bu "
                "<mark>kuchaytirish</mark>ning salbiy shakli.</p>"
                + why([
                    (True, "Worse,",
                     "muammoning kuchayishini bildiradi — <em>indeed</em> "
                     "ning salbiy qarindoshi. Ikkinchi jumla birinchisidan "
                     "jiddiyroq."),
                    (False, "Thus,",
                     "<strong>sinonim juftlik</strong> (<em>As a result</em> "
                     "bilan). Bu ikkitasini birga ko'rgan zahoti ikkovini "
                     "ham o'chiring."),
                    (False, "As a result,",
                     "yuqoridagining juftligi."),
                    (False, "Meanwhile,",
                     "vaqt: parallel voqea yo'q, mantiqiy kuchayish bor."),
                ])
                + TIP.format(
                    "Bu usul <strong>vaqt tejaydi</strong>: sinonim juftlikni "
                    "topish besh soniya oladi va savolni to'rtdan ikkiga "
                    "qisqartiradi. Uni har Transitions savolida birinchi "
                    "harakat qiling — matnni o'qishdan ham oldin.")
            ),
        },

        {
            "rich_text": trans_q(
                "<p>Some materials fail without warning. Glass does not bend before it "
                "breaks, and a ceramic bearing that has run soundly for a decade can "
                "shatter in a single revolution. <span class=\"sr-blank\"></span> "
                "engineers who use such materials design to a far larger margin than the "
                "measured strength alone would suggest.</p>"),
            "choices": [
                {"text": "Accordingly,", "is_correct": True},
                {"text": "For example,", "is_correct": False},
                {"text": "For instance,", "is_correct": False},
                {"text": "Nevertheless,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>1-qadam \u2014 sinonimlar:</strong> "
                "<em>For example</em> va <em>For instance</em> \u2014 "
                "amalda <u>butunlay</u> bir xil. Ikkovi ham javob "
                "bo\u2018lolmaydi. Bu eng oson tanaladigan juftlik.</p>"
                "<p>Qoldi: <em>Accordingly</em> va <em>Nevertheless</em>.</p>"
                "<p><strong>2-qadam:</strong> ogohlantirishsiz singan material "
                "\u2192 muhandis kattaroq zaxira qo\u2018yadi. Bu "
                "<mark>natija</mark>.</p>"
                + why([
                    (True, "Accordingly,",
                     "natija bog\u2018lovchisi (<em>therefore</em> bilan bir xil "
                     "oiladan). Xavf \u2192 unga javoban qilingan qaror."),
                    (False, "Nevertheless,",
                     "qarshilik: muhandisning ehtiyotkorligi materialning "
                     "xavfiga zid emas, undan kelib chiqadi."),
                    (False, "For example,",
                     "<strong>sinonim juftlikning yarmi.</strong> Va misol "
                     "ham emas: zaxira qo\u2018yish \u2014 ogohlantirishsiz "
                     "sinishning misoli emas, unga javob."),
                    (False, "For instance,",
                     "yuqoridagining aynan juftligi \u2014 ikkovini birga "
                     "ko\u2018rgan zahoti o\u2018chiring."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">nonetheless</div><div class="pp-card-back">shunga qaramay (= nevertheless)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">besides</div><div class="pp-card-back">bundan tashqari (= moreover)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">unsurprisingly</div><div class="pp-card-back">kutilganidek, ajablanarli emaski</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">worse</div><div class="pp-card-back">bundan ham yomoni (salbiy kuchaytirish)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a tide mill</div><div class="pp-card-back">suv ko\'tarilishida ishlaydigan tegirmon</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to split along its length</div><div class="pp-card-back">uzunasiga yorilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a proofreader</div><div class="pp-card-back">musahhih, matn tekshiruvchi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to slide past ~</div><div class="pp-card-back">~ ni sezmay o\'tib ketmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Har savolda <strong>aynan bitta</strong> to'g'ri javob "
              "bo'ladi.</li>"
              "<li>Demak <strong>ikki sinonim = ikkovi ham noto'g'ri</strong>.</li>"
              "<li>Bu birinchi harakat bo'lsin — matnni o'qishdan ham "
              "oldin.</li>"
              "<li>Sinonim = <u>bir xil munosabat</u>: "
              "<em>however</em> ≠ <em>by contrast</em>, "
              "<em>moreover</em> ≠ <em>for example</em>.</li>"
              "<li>To'rtdan ikkiga qisqargach, 10-darsdagi usulni "
              "qo'llang.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 16
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_TRANS,
    "title": "SAT R&W W16: Transitions — Mixed Practice Under Time",
    "summary": "Oltita bog'lovchi savoli, barcha munosabatlar aralash, imtihon "
               "tezligida: 10–15-darslarni soatga qarshi mustahkamlash.",
    "order": 16,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy amaliyot</h2>"
            "<p>Oltita savol, barcha munosabatlar aralash. Bu tur imtihonda "
            "eng tez yechiladiganlardan, shuning uchun taymer qattiq:</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Har savolda shu "
                "tartib:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li><strong>Sinonim juftlikni toping</strong> — bor bo'lsa, "
                "ikkovini darrov o'chiring (15-dars).</li>"
                "<li>Qolgan variantlarni yoping va munosabatni "
                "<u>o'zbekcha</u> ayting (10-dars).</li>"
                "<li>Matndagi <u>boshqa</u> bog'lovchilarni ham o'qing — "
                "burilish allaqachon bo'lgan bo'lishi mumkin.</li>"
                "</ol>")
            + "<p>Taymer: <strong>4 daqiqa</strong> (6 × 40 soniya).</p>"
            + '<span class="sr-time">⏱ 6 savol · 4 daqiqa</span>'
        )},

        {
            "rich_text": qnum(1, "Transitions") + trans_q(
                "<p>Honey never spoils: jars sealed in ancient tombs have been opened and "
                "found edible. Its sugar concentration is so high that any bacterium "
                "landing in it loses water and dies. <span class=\"sr-blank\"></span> "
                "honey diluted with water ferments within days, which is how mead has "
                "been made for thousands of years.</p>"),
            "choices": [
                {"text": "However,", "is_correct": True},
                {"text": "Consequently,", "is_correct": False},
                {"text": "Thus,", "is_correct": False},
                {"text": "For instance,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Sinonim juftlik:</strong> <em>Consequently</em> va "
                "<em>Thus</em> — ikkovi ham natija. O'chiriladi.</p>"
                "<p>Qoldi: <em>However</em> va <em>For instance</em>. "
                "Munosabat: asal buzilmaydi ↔ suyultirilgan asal bir necha "
                "kunda achiydi. <mark>Burilish.</mark></p>"
                + why([
                    (True, "However,",
                     "qarshilik: shart o'zgargach (suv qo'shilgach) natija "
                     "teskari bo'ladi."),
                    (False, "For instance,",
                     "misol emas: achish buzilmaslikning holati emas, "
                     "uning aksi."),
                    (False, "Consequently,",
                     "<strong>sinonim juftlikning yarmi</strong>, va mantiqan "
                     "ham teskari."),
                    (False, "Thus,",
                     "yuqoridagining juftligi."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Transitions") + trans_q(
                "<p>Concrete gains most of its strength in the first month but continues "
                "to harden for years, and cores drilled from bridges built in the 1930s "
                "test stronger than the same mix did when new. "
                "<span class=\"sr-blank\"></span> the steel embedded in that concrete "
                "corrodes over the same decades, so the structure as a whole is not "
                "getting stronger.</p>"),
            "choices": [
                {"text": "Meanwhile,", "is_correct": True},
                {"text": "Therefore,", "is_correct": False},
                {"text": "Specifically,", "is_correct": False},
                {"text": "Indeed,", "is_correct": False},
            ],
            "explanation": (
                "<p>Sinonim juftlik yo'q — to'rttasi ham har xil oiladan. "
                "Demak to'g'ridan-to'g'ri munosabatga o'tamiz.</p>"
                "<p>Beton kuchayadi; <u>o'sha o'n yilliklarda</u> po'lat "
                "zanglaydi. Ikki jarayon <mark>parallel kechadi</mark> va "
                "qarama-qarshi yo'nalishda.</p>"
                + why([
                    (True, "Meanwhile,",
                     "bir vaqtda kechayotgan ikkinchi jarayonni kiritadi — "
                     "<em>over the same decades</em> iborasi buni ochiq "
                     "ko'rsatib turibdi."),
                    (False, "Therefore,",
                     "natija: po'latning zanglashi betonning qotishidan "
                     "kelib chiqmaydi."),
                    (False, "Indeed,",
                     "kuchaytirish: ikkinchi jumla birinchisini kuchaytirmaydi, "
                     "u qarama-qarshi jarayonni beradi."),
                    (False, "Specifically,",
                     "aniqlashtirish: po'lat betonning tafsiloti emas, "
                     "boshqa material."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Transitions") + trans_q(
                "<p>Most of a violin's sound comes from the wooden body rather than the "
                "strings, and makers select spruce for the top by tapping boards and "
                "listening. <span class=\"sr-blank\"></span> instruments built from "
                "boards chosen by measured stiffness alone are consistently rated lower "
                "by players than those chosen by ear.</p>"),
            "choices": [
                {"text": "Indeed,", "is_correct": True},
                {"text": "Nevertheless,", "is_correct": False},
                {"text": "Nonetheless,", "is_correct": False},
                {"text": "Afterward,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Sinonim juftlik:</strong> <em>Nevertheless</em> va "
                "<em>Nonetheless</em> — ayni bir so'z, ikki shakl. "
                "O'chiriladi.</p>"
                "<p>Qoldi: <em>Indeed</em> va <em>Afterward</em>. Munosabat: "
                "ustalar quloq bilan tanlaydi → quloqsiz tanlangan yog'ochdan "
                "yasalgan skripka yomonroq baholanadi. Ikkinchi jumla "
                "birinchisini <mark>kuchaytiradi</mark>.</p>"
                + why([
                    (True, "Indeed,",
                     "kuchaytirish: quloq bilan tanlash shunchaki an'ana emas "
                     "— uni o'lchov bilan almashtirish natijani "
                     "yomonlashtiradi. Zinapoyaning keyingi pog'onasi."),
                    (False, "Afterward,",
                     "vaqt ketma-ketligi yo'q."),
                    (False, "Nevertheless,",
                     "<strong>sinonim juftlikning yarmi</strong>, va "
                     "yo'nalish ham noto'g'ri."),
                    (False, "Nonetheless,",
                     "yuqoridagining juftligi."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Transitions") + trans_q(
                "<p>A census taken during a war undercounts young men, who are away, and "
                "overcounts them a decade later when the same cohort is recorded at home. "
                "Demographers know this and correct for it. <span "
                "class=\"sr-blank\"></span> the correction depends on knowing how many "
                "were away, which is exactly the figure the census failed to "
                "collect.</p>"),
            "choices": [
                {"text": "The difficulty is that", "is_correct": True},
                {"text": "As a result,", "is_correct": False},
                {"text": "Accordingly,", "is_correct": False},
                {"text": "For example,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Sinonim juftlik:</strong> <em>As a result</em> va "
                "<em>Accordingly</em> — ikkovi ham natija. O'chiriladi.</p>"
                "<p>Qoldi: <em>The difficulty is that</em> va "
                "<em>For example</em>. Munosabat: demograflar tuzatadi → "
                "lekin tuzatish uchun kerakli raqam yo'q. Bu "
                "<mark>muammo</mark>, ya'ni burilish.</p>"
                + why([
                    (True, "The difficulty is that",
                     "burilishni ochiq nomlaydi. Bog'lovchi so'z bo'lmasa "
                     "ham, u xuddi <em>however</em> kabi ishlaydi — SAT "
                     "ba'zan shunday iboralarni ham beradi."),
                    (False, "For example,",
                     "misol emas: bu tuzatishning holati emas, uning "
                     "to'sig'i."),
                    (False, "As a result,",
                     "<strong>sinonim juftlikning yarmi</strong>, va mantiqan "
                     "ham noto'g'ri."),
                    (False, "Accordingly,",
                     "yuqoridagining juftligi."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Transitions") + trans_q(
                "<p>Cork is harvested by stripping the outer bark from a living oak, "
                "which regrows it over about nine years. The tree is not cut and can be "
                "stripped a dozen times in its life. <span class=\"sr-blank\"></span> "
                "cork oak woodlands are among the few commercial crops that support "
                "roughly the same bird populations as unmanaged forest.</p>"),
            "choices": [
                {"text": "Because of this,", "is_correct": True},
                {"text": "Admittedly,", "is_correct": False},
                {"text": "By contrast,", "is_correct": False},
                {"text": "Meanwhile,", "is_correct": False},
            ],
            "explanation": (
                "<p>Sinonim juftlik yo'q. Munosabat: daraxt kesilmaydi va "
                "o'nlab marta yig'ib olinadi → shuning uchun bunday "
                "o'rmonlar qushlarni saqlaydi. <mark>Natija.</mark></p>"
                + why([
                    (True, "Because of this,",
                     "sabab-oqibat ochiq: daraxt tirik qolgani uchun o'rmon "
                     "ham saqlanadi."),
                    (False, "By contrast,",
                     "ikki subyekt yonma-yon qo'yilmaydi — matn bitta "
                     "tizim haqida (11-dars)."),
                    (False, "Admittedly,",
                     "yon berish: keyin burilish kutilardi, yo'q "
                     "(14-dars)."),
                    (False, "Meanwhile,",
                     "parallel voqea emas — bu bevosita oqibat."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Transitions") + trans_q(
                "<p>Machine translation of legal contracts has improved to the point "
                "where a first draft can be produced in seconds. Firms that have tried it "
                "report that checking the draft takes about as long as translating from "
                "scratch used to. <span class=\"sr-blank\"></span> the errors it makes "
                "are fluent and plausible, and a checker must read every clause with the "
                "attention a translator would have given it.</p>"),
            "choices": [
                {"text": "This is because", "is_correct": True},
                {"text": "Nevertheless,", "is_correct": False},
                {"text": "In addition,", "is_correct": False},
                {"text": "Besides,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Sinonim juftlik:</strong> <em>In addition</em> va "
                "<em>Besides</em> — ikkovi ham qo'shimcha. O'chiriladi.</p>"
                "<p>Qoldi: <em>This is because</em> va <em>Nevertheless</em>. "
                "Munosabat: tekshirish nega uzoq davom etadi? Uchinchi jumla "
                "buning <mark>sababini</mark> beradi — xatolar ishonarli "
                "ko'rinadi.</p>"
                + why([
                    (True, "This is because",
                     "sabab bog'lovchisi, va yo'nalishi to'g'ri: uchinchi "
                     "jumla ikkinchisidagi holatni tushuntiradi. "
                     "(<em>Therefore</em> teskari yo'nalish bo'lardi.)"),
                    (False, "Nevertheless,",
                     "qarshilik: uchinchi jumla ikkinchisiga zid emas, uni "
                     "izohlaydi."),
                    (False, "In addition,",
                     "<strong>sinonim juftlikning yarmi</strong>, va "
                     "qo'shimcha fakt ham emas — izoh."),
                    (False, "Besides,",
                     "yuqoridagining juftligi."),
                ])
                + TIP.format(
                    "Oxirgi ikki savolda bog'lovchi <u>so'z</u> emas, "
                    "<u>ibora</u> edi: <em>The difficulty is that</em>, "
                    "<em>This is because</em>. SAT bularni ham beradi, va "
                    "ular xuddi bir so'zli bog'lovchilar kabi ishlaydi — "
                    "munosabatni ular ham aytadi.")
            ),
        },

        {"rich_text": (
            "<h3>Xatoni turi bo'yicha tahlil qiling</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Xato turi</th><th>Qaysi darsga qaytish</th></tr></thead>"
              "<tbody>"
              "<tr><td>Sinonim juftlikni sezmadim</td><td>15-dars — birinchi "
              "harakat</td></tr>"
              "<tr><td>Munosabatni aytmasdan tanladim</td><td>10-dars — "
              "variantlarni yoping</td></tr>"
              "<tr><td><em>By contrast</em> ni bitta mavzuga qo'ydim</td>"
              "<td>11-dars — ikki subyekt qoidasi</td></tr>"
              "<tr><td>Ketma-ketlikni natija deb oldim</td><td>12-dars — "
              "«birinchisi bo'lmaganida?» sinovi</td></tr>"
              "<tr><td>Misol bilan qo'shimchani adashtirdim</td><td>13-dars — "
              "olib tashlash sinovi</td></tr>"
              "<tr><td><em>Admittedly</em> ni burilishsiz qo'ydim</td>"
              "<td>14-dars — keyingi jumladan yeching</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + NOTE.format(
                "Transitions — imtihonda <strong>eng tez</strong> "
                "yechiladigan turlardan. 40 soniyadan ko'p vaqt "
                "sarflasangiz, deyarli har doim sabab bitta: munosabatni "
                "aytmasdan variantlarni «sinab ko'rgansiz».")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">The difficulty is that ~</div><div class="pp-card-back">muammo shundaki ~ (burilish iborasi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">This is because ~</div><div class="pp-card-back">buning sababi shuki ~</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">Because of this,</div><div class="pp-card-back">shu sababli</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to ferment</div><div class="pp-card-back">achimoq, bijg\'imoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to corrode</div><div class="pp-card-back">zanglamoq, yemirilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">stiffness</div><div class="pp-card-back">qattiqlik, egilmaslik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a cohort</div><div class="pp-card-back">bir yilda tug\'ilgan guruh (demografiyada)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">from scratch</div><div class="pp-card-back">noldan, boshidan</div></div>'
            + "</div>"
            + "<h3>Xulosa — Transitions mavzusi yakuni</h3>"
            + "<ul>"
              "<li><strong>Sinonim juftlikni birinchi qidiring</strong> — "
              "besh soniya, savol yarmi (15-dars).</li>"
              "<li>Munosabatni <u>o'zbekcha</u> ayting, keyin variantlarni "
              "oching (10-dars).</li>"
              "<li>Yetti munosabat: qarshilik · natija · qo'shimcha · misol · "
              "vaqt · yon berish · kuchaytirish.</li>"
              "<li>Bog'lovchi <u>ibora</u> ham bo'lishi mumkin: "
              "<em>This is because · The difficulty is that</em>.</li>"
              "<li>Maqsad: <strong>40 soniya</strong> har savolga.</li>"
              "</ul>"
        )},
    ],
},

]
