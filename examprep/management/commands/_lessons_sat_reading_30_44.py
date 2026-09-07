# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — Reading lessons 30-33 and 40-44.

Covers "Ikki matn bog'lanishi (Cross-Text Connections)" (30-33) and
"Asosiy fikr va tafsilotlar (Central Ideas and Details)" (40-44).
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

TOPIC_XTEXT = {
    "title":   "Ikki matn bog'lanishi (Cross-Text Connections)",
    "summary": "Ikki qisqa matn beriladi: ular qayerda uchrashadi, nimada "
               "kelishmaydi va biri ikkinchisiga qanday javob berardi.",
    "icon":    "bi-arrow-left-right",
    "order":   4,
}

TOPIC_CID = {
    "title":   "Asosiy fikr va tafsilotlar (Central Ideas and Details)",
    "summary": "Matn nimani da'vo qilyapti va bitta tafsilot qayerda yozilgan — "
               "eslab qolgan narsadan emas, satrdan javob berish.",
    "icon":    "bi-bullseye",
    "order":   5,
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
    """Single passage pane + a bolded exam stem."""
    return f'<div class="sr-passage">{passage}</div><p><strong>{stem}</strong></p>'


def cross_q(text1, text2, stem):
    """Two stacked passage panes, labelled as the exam labels them, + the stem."""
    return (f'<div class="sr-passage"><p><strong>Text 1</strong></p>{text1}</div>'
            f'<div class="sr-passage"><p><strong>Text 2</strong></p>{text2}</div>'
            f'<p><strong>{stem}</strong></p>')


def choices_html(items):
    """The static A/B/C/D list used in a WORKED example (not a shuffled choices block)."""
    return '<ol type="A">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 30
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_XTEXT,
    "title": "SAT R&W 30: Two Texts, One Question — Mapping Agreement and Disagreement",
    "summary": "Ikki matn orasidagi munosabat oltita turdan biriga tushadi; uni "
               "variantlarni ochishdan oldin nomlash — bu turning butun usuli.",
    "order": 30,
    "blocks": [
        {"rich_text": (
            "<h2>Ikki matn, bitta savol</h2>"
            "<p><strong>Cross-Text Connections</strong> — <em>Craft and Structure</em> "
            "domenining uchinchi va eng qiyin turi. Ekranda ikkita qisqa matn "
            "(<em>Text 1</em> va <em>Text 2</em>), har biri 40–90 so'z, va bitta "
            "savol.</p>"
            "<p>Nega qiyin? Chunki <mark>ikkala matnni bir vaqtda boshda tutish "
            "kerak</mark>. Ko'p o'quvchi ikkinchi matnni o'qib bo'lguncha birinchisini "
            "unutadi — va keyin variantlar orasida chalkashadi.</p>"
            "<p>Yechim — <u>xotira emas, usul</u>. Bu darsda o'sha usulni "
            "o'rnatamiz.</p>"
            + '<span class="sr-time">⏱ ~90 soniya (imtihondagi eng sekin tur)</span>'
        )},

        {"rich_text": (
            "<h3>Munosabat oltita turdan biri bo'ladi</h3>"
            "<p>Ikki matn tasodifiy tanlanmaydi. Ular har doim bitta narsada "
            "uchrashadi, va munosabat amalda quyidagilardan biri:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Munosabat</th><th>Text 2 nima qilyapti</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>1. Rad etadi</strong></td>"
              "<td>Text 1 ning xulosasi noto'g'ri deydi</td></tr>"
              "<tr><td><strong>2. Cheklaydi</strong></td>"
              "<td>Rozi, lekin «faqat ma'lum hollarda» deb qo'shadi</td></tr>"
              "<tr><td><strong>3. Boshqa sabab beradi</strong></td>"
              "<td>Xuddi shu kuzatuvni boshqacha tushuntiradi</td></tr>"
              "<tr><td><strong>4. Yangi dalil qo'shadi</strong></td>"
              "<td>Text 1 muallifida bo'lmagan ma'lumot</td></tr>"
              "<tr><td><strong>5. Umumlashmaydi deydi</strong></td>"
              "<td>Natija to'g'ri, lekin faqat o'sha holatda</td></tr>"
              "<tr><td><strong>6. Faktda rozi, ma'noda emas</strong></td>"
              "<td>Nima bo'lganini bir xil ko'radi, nimani anglatishini boshqacha</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + NOTE.format(
                "Diqqat qiling: oltitadan faqat <u>bittasi</u> to'liq rad etish. "
                "Ko'p o'quvchi «ikki matn = bahs» deb o'ylaydi va har doim "
                "qarama-qarshilikni qidiradi. Aslida ikkinchi matn ko'pincha "
                "<strong>rozi bo'ladi-yu, nimadir qo'shadi</strong>.")
        )},

        {"rich_text": (
            "<h3>Usul — to'rt qadam</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Savolni birinchi o'qing.</strong> "
              "Bu yerda savolni bilish odatdagidan ham muhimroq, chunki savol "
              "<u>yo'nalishni</u> aytadi: Text 2 Text 1 ga javob beradimi, yoki "
              "aksinchami?</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Text 1 ni o'qing va uning "
              "da'vosini bitta jumlada ayting.</strong> Ovoz chiqarmasdan, o'zbekcha: "
              "«tulkilar shaharda jasurroq, chunki shahar jasurlarni tanlab "
              "oladi».</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Text 2 ni o'qing va uning "
              "da'vosini ayting.</strong> Xuddi shunday, bitta jumla.</p></div>"
            + "<div class=\"pp-step\"><p><strong>4. Munosabatni nomlang</strong> — "
              "yuqoridagi oltitadan qaysi biri? Faqat shundan keyin variantlarga "
              "qarang.</p></div>"
            + '</div>'
            + TIP.format(
                "2 va 3-qadamlar — bu <u>siqish</u>. Har matnni bitta jumlaga "
                "siqsangiz, ikkovi ham boshingizga sig'adi. Siqmasdan o'qigan odam "
                "160 so'zni eslashga urinadi va uddalay olmaydi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + cross_q(
                "<p>Urban foxes approach people far more closely than rural foxes do. "
                "The usual explanation is selective: a city is a filter, and the animals "
                "that will not tolerate close human presence do not stay to breed there. "
                "Over enough generations the urban population is simply made of the "
                "bolder line.</p>",
                "<p>Individual foxes fitted with collars have been followed from their "
                "first months in a city. The same animal that fled at fifty metres in "
                "spring will feed at ten metres by the following winter, and no "
                "generation has passed. Whatever else is happening, a fox that has met "
                "people a hundred times without harm is not the fox it was.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the explanation offered in Text 1?")
            + choices_html([
                "By agreeing that urban foxes are bolder and adding that they are also "
                "larger than rural foxes.",
                "By suggesting that the boldness may develop within a single animal's "
                "lifetime rather than across generations.",
                "By denying that urban and rural foxes differ in their behaviour toward "
                "people.",
                "By arguing that boldness makes a fox less likely to survive in a city.",
            ])
            + '<span class="sr-time">⏱ ~90 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>1-qadam — savol:</strong> Text 2 muallifi Text 1 ga javob "
            "beradi. Yo'nalish: <mark>2 → 1</mark>.</p>"
            "<p><strong>2-qadam — Text 1 bitta jumlada:</strong> «shahar tulkilari "
            "jasur, chunki shahar avlodlar davomida jasurlarni saralab olgan».</p>"
            "<p><strong>3-qadam — Text 2 bitta jumlada:</strong> «bitta tulkining o'zi "
            "bir yil ichida jasurlashadi, avlod almashmasdan».</p>"
            "<p><strong>4-qadam — munosabat:</strong> ikkovi ham tulkilar jasur "
            "ekaniga rozi. Farq — <u>sababida</u>. Bu jadvaldagi "
            "<strong>3-tur: boshqa sabab beradi</strong>.</p>"
            + why([
                (True, "By suggesting that the boldness may develop within a single animal's lifetime rather than across generations",
                 "aynan Text 2 ning dalili: <em>the same animal … and no generation has "
                 "passed</em>. «Avlodlar davomida saralash» o'rniga «bitta hayot "
                 "davomida o'rganish»."),
                (False, "By agreeing that urban foxes are bolder and adding that they are also larger",
                 "<strong>yarim to'g'ri</strong>: birinchi yarmi rost — Text 2 "
                 "jasurlikni inkor qilmaydi. Lekin o'lcham haqida ikkala matnda ham "
                 "bir og'iz yo'q. Ikkinchi yarmi o'ylab topilgan."),
                (False, "By denying that urban and rural foxes differ in their behaviour toward people",
                 "Text 2 farqni inkor qilmaydi — u farqni <u>tan oladi</u> va uning "
                 "sababini boshqacha tushuntiradi. Bu «har doim qarama-qarshilik "
                 "qidirish» odatidan tug'iladigan tuzoq."),
                (False, "By arguing that boldness makes a fox less likely to survive in a city",
                 "Text 2 ning dalilini teskari qiladi: uning tulkilari jasurlashib, "
                 "shaharda yashab yuribdi. Bu Text 1 ni ham buzadi."),
            ])
            + NOTE.format(
                "Bu savolning yuragi bitta ibora edi: <em>and no generation has "
                "passed</em>. Text 2 muallifi uni ataylab yozgan — u aynan Text 1 "
                "ning mexanizmiga tegadi. <strong>Ikki matn har doim shunday bitta "
                "nuqtada uchrashadi</strong>, va 31-dars butunlay o'sha nuqtani "
                "topish haqida.")
        )},

        {
            "rich_text": cross_q(
                "<p>The coffeehouses that spread through European cities in the "
                "seventeenth century have been described as the first genuinely public "
                "spaces for discussion. Entry cost a penny, no introduction was required, "
                "and a labourer could in principle sit at the same table as a merchant "
                "and contradict him.</p>",
                "<p>The surviving records complicate that picture. Many houses took "
                "subscriptions rather than pennies at the door, and most came to serve a "
                "particular trade — one for shipping men, another for dealers in stock. A "
                "room that anyone may enter is not the same as a room that anyone "
                "does.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the characterisation in Text 1?"),
            "choices": [
                {"text": "By arguing that access was narrower in practice than the formal openness suggests.", "is_correct": True},
                {"text": "By denying that political discussion took place in coffeehouses at all.", "is_correct": False},
                {"text": "By agreeing that coffeehouses were open to every man who could pay a penny.", "is_correct": False},
                {"text": "By claiming that printed newspapers mattered more than coffeehouses did.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Text 1 bitta jumlada:</strong> «qahvaxonalar birinchi "
                "haqiqiy ochiq muhokama maydoni edi — bir penni, tanishtiruvsiz».</p>"
                "<p><strong>Text 2 bitta jumlada:</strong> «amalda obuna kerak edi va "
                "har biri o'z kasbiga xizmat qilardi».</p>"
                "<p><strong>Munosabat:</strong> Text 2 faktni inkor qilmaydi — u "
                "<u>rasmiy ochiqlik</u> bilan <u>amaldagi ochiqlik</u>ni ajratadi. "
                "Bu <strong>2-tur: cheklaydi</strong>. Oxirgi jumla buni ochiq "
                "aytadi: <em>A room that anyone may enter is not the same as a room "
                "that anyone does.</em></p>"
                + why([
                    (True, "By arguing that access was narrower in practice than the formal openness suggests",
                     "Text 2 ning butun mazmuni: obuna, kasbiy ixtisoslashuv, va "
                     "<em>may enter</em> ↔ <em>does</em> farqi."),
                    (False, "By denying that political discussion took place in coffeehouses at all",
                     "muhokamaning <u>bo'lgani</u> inkor qilinmaydi — faqat "
                     "kimlarning qatnashgani cheklanadi. Bu «rad etish» tuzog'i: "
                     "cheklashni to'liq inkor deb o'qish."),
                    (False, "By agreeing that coffeehouses were open to every man who could pay a penny",
                     "aynan shu jumlaga Text 2 e'tiroz bildiryapti. To'g'ridan-to'g'ri "
                     "teskari."),
                    (False, "By claiming that printed newspapers mattered more than coffeehouses did",
                     "gazetalar Text 2 da faqat <u>obuna</u> misolida eslatilgan. "
                     "Ularning ahamiyati solishtirilmaydi. <strong>So'z-tuzoq.</strong>"),
                ])
            ),
        },

        {
            "rich_text": cross_q(
                "<p>Students who study a word list and then sleep recall more of it the "
                "next day than students who study the same list in the morning and stay "
                "awake for an equal interval. The standard reading of this result is that "
                "sleep does active work on a new memory, strengthening it while the "
                "learner is unconscious.</p>",
                "<p>The advantage largely disappears when the waking group spends the "
                "interval resting quietly in a darkened room instead of going about the "
                "day. What the sleeping group may be getting is not a process but a "
                "protection: several hours in which nothing new arrives to interfere with "
                "what was just learned.</p>",
                "Based on the texts, both authors would most likely agree with which "
                "statement?"),
            "choices": [
                {"text": "An interval that follows study and brings in no new material tends to improve later recall.", "is_correct": True},
                {"text": "Sleep has no measurable effect on how much a learner recalls.", "is_correct": False},
                {"text": "Studying immediately before sleeping should be discouraged.", "is_correct": False},
                {"text": "Memory is strengthened only during the deepest stages of sleep.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu savol boshqa yo'nalishda: <em>both authors would agree</em> — "
                "<mark>kesishmani</mark> qidiryapmiz, farqni emas.</p>"
                "<p><strong>Ikkovi nimada rozi?</strong> Uxlagan guruh ko'proq eslab "
                "qolgani — bu Text 1 ning kuzatuvi va Text 2 uni inkor qilmaydi. "
                "Ikkovi <u>sababda</u> ajraladi: faol jarayonmi (Text 1) yoki "
                "xalaqitning yo'qligimi (Text 2). Bu <strong>6-tur: faktda rozi, "
                "ma'noda emas</strong>.</p>"
                + why([
                    (True, "An interval that follows study and brings in no new material tends to improve later recall",
                     "Text 2 buni to'g'ridan-to'g'ri taklif qiladi, va Text 1 ham "
                     "bunga zid emas: uyqu ham aynan shunday oraliq. Ikkala matn ham "
                     "ko'tara oladigan yagona da'vo."),
                    (False, "Sleep has no measurable effect on how much a learner recalls",
                     "Text 1 buni albatta rad etadi, va Text 2 ham bunday demaydi — "
                     "u ta'sirning <u>sababi</u>ni boshqacha izohlaydi, ta'sirni "
                     "emas."),
                    (False, "Studying immediately before sleeping should be discouraged",
                     "ikkala matn ham hech narsa tavsiya qilmaydi, va bu ikkalasining "
                     "ham natijasiga zid — uxlashdan oldin o'qish foydali "
                     "chiqyapti."),
                    (False, "Memory is strengthened only during the deepest stages of sleep",
                     "uyqu bosqichlari birorta matnda eslatilmaydi. "
                     "<strong>Tashqi bilim</strong> tuzog'i: mavzu tanish bo'lgani "
                     "uchun o'quvchi o'zi bilgan narsani qo'shib yuboradi."),
                ])
                + TIP.format(
                    "<em>Both authors would agree</em> savolida to'g'ri javob deyarli "
                    "har doim <u>ehtiyotkor va tor</u> bo'ladi: ikkala matn ham "
                    "ko'tara oladigan eng kichik da'vo. Kuchli, keng bayonotlar "
                    "bu savolda deyarli har doim noto'g'ri.")
            ),
        },

        {
            "rich_text": cross_q(
                "<p>A translator's first duty is self-effacement. The reader should "
                "finish the book believing they have met the author, not the translator, "
                "and every choice that draws attention to the translation is a small "
                "failure of the craft.</p>",
                "<p>There is no neutral rendering to fall back on. A translator picks one "
                "English word where the original offers a range, decides where a sentence "
                "breaks, and chooses which of two meanings to carry across and which to "
                "let go. The result is a text that could not have been written by anyone "
                "else.</p>",
                "Which choice best describes a difference in how the two texts "
                "characterise the work of a translator?"),
            "choices": [
                {"text": "Text 1 presents the translator as a channel for another writer's work, whereas Text 2 presents translation as a series of the translator's own decisions.", "is_correct": True},
                {"text": "Text 1 considers translation an art, whereas Text 2 considers it a technical skill that can be taught.", "is_correct": False},
                {"text": "Text 1 focuses on translations of poetry, whereas Text 2 focuses on translations of prose.", "is_correct": False},
                {"text": "Text 1 argues that translations age quickly, whereas Text 2 argues that they last.", "is_correct": False},
            ],
            "explanation": (
                "<p>Savol <em>a difference in how the two texts characterise</em> — "
                "ya'ni har bir matn tarjimonni <u>kim</u> deb ko'radi.</p>"
                "<p><strong>Text 1:</strong> tarjimon ko'rinmasligi kerak — o'quvchi "
                "muallif bilan uchrashgan bo'lishi kerak. <strong>Text 2:</strong> "
                "neytral tarjima yo'q; har qadam tarjimonning qarori.</p>"
                + why([
                    (True, "Text 1 presents the translator as a channel for another writer's work, whereas Text 2 presents translation as a series of the translator's own decisions",
                     "ikkala matnning markaziy tasvirini to'g'ri juftlaydi: "
                     "<em>self-effacement</em> ↔ <em>could not have been written by "
                     "anyone else</em>."),
                    (False, "Text 1 considers translation an art, whereas Text 2 considers it a technical skill that can be taught",
                     "<strong>teskari va ikkovi ham noto'g'ri.</strong> Aynan Text 2 "
                     "ijodiy qarorlardan gapiryapti. Va o'qitish masalasi birorta "
                     "matnda yo'q."),
                    (False, "Text 1 focuses on translations of poetry, whereas Text 2 focuses on translations of prose",
                     "na she'r, na nasr eslatilmaydi. Bu variant butunlay "
                     "o'ylab topilgan farqni taklif qiladi."),
                    (False, "Text 1 argues that translations age quickly, whereas Text 2 argues that they last",
                     "vaqt va eskirish ikkala matnda ham muhokama qilinmaydi."),
                ])
            ),
        },

        {
            "rich_text": cross_q(
                "<p>Handwriting has all but vanished from the primary timetable, and the "
                "computer is the usual culprit. Once a child can type, the argument runs, "
                "the hours once given to forming letters have no defender.</p>",
                "<p>Timetables from the two decades before classroom computers arrived "
                "show the handwriting allocation already cut by half. What took the time "
                "was a steady addition of new subjects to a week that never grew longer. "
                "The computer arrived to find the space already gone.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the explanation given in Text 1?"),
            "choices": [
                {"text": "By identifying a cause that was already operating before the one Text 1 names appeared.", "is_correct": True},
                {"text": "By denying that handwriting instruction has declined in primary schools.", "is_correct": False},
                {"text": "By agreeing that computers are responsible and adding that tablets accelerated the change.", "is_correct": False},
                {"text": "By arguing that computers should be removed from primary classrooms.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Text 1 bitta jumlada:</strong> \u00abkompyuter qo\u2018l yozuvini "
                "jadvaldan siqib chiqardi\u00bb. <strong>Text 2 bitta jumlada:</strong> "
                "\u00abvaqt kompyuter kelishidan oldin ham yarmiga qisqargan edi \u2014 uni "
                "yangi fanlar yegan\u00bb.</p>"
                "<p><strong>Munosabat:</strong> 3-tur \u2014 boshqa sabab. Va u vaqt "
                "bo\u2018yicha ishlaydi: sabab deb ko\u2018rsatilgan narsa "
                "<mark>voqeadan keyin kelgan</mark>.</p>"
                + why([
                    (True, "By identifying a cause that was already operating before the one Text 1 names appeared",
                     "Text 2 ning oxirgi jumlasi buni ochiq aytadi: <em>The computer "
                     "arrived to find the space already gone.</em>"),
                    (False, "By denying that handwriting instruction has declined in primary schools",
                     "pasayish ikkala matnda ham qabul qilingan \u2014 Text 2 uning "
                     "<u>sababi</u>ga e\u2019tiroz bildiryapti, faktiga emas."),
                    (False, "By agreeing that computers are responsible and adding that tablets accelerated the change",
                     "<strong>yarim to\u2018g\u2018ri</strong> va aslida teskari: Text 2 "
                     "kompyuterni sabab sifatida rad etadi. Planshetlar esa birorta "
                     "matnda yo\u2018q."),
                    (False, "By arguing that computers should be removed from primary classrooms",
                     "hech qaysi matn tavsiya bermaydi. Text 2 nima "
                     "<u>bo\u2018lganini</u> tushuntiradi, nima qilish kerakligini emas."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to complicate a picture</div><div class="pp-card-back">tasavvurni qiyinlashtirmoq, oddiy emasligini ko\'rsatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">self-effacement</div><div class="pp-card-back">o\'zini ko\'rsatmaslik, orqada turish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to characterise ~</div><div class="pp-card-back">~ ni qanday tasvirlash, qanday ko\'rsatish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">in principle vs in practice</div><div class="pp-card-back">nazariy jihatdan ↔ amalda</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to interfere with ~</div><div class="pp-card-back">~ ga xalaqit bermoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">selective (explanation)</div><div class="pp-card-back">saralashga asoslangan (tushuntirish)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to fall back on ~</div><div class="pp-card-back">~ ga suyanmoq, zaxira sifatida ishlatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a rendering</div><div class="pp-card-back">tarjima varianti, o\'girish</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Ikki matn, 40–90 so'zdan, bitta savol — imtihondagi eng sekin tur "
              "(~90 soniya).</li>"
              "<li>Har matnni <strong>bitta jumlaga siqing</strong> — xotira emas, "
              "usul.</li>"
              "<li>Munosabatni <u>variantlardan oldin</u> nomlang: rad etadi · "
              "cheklaydi · boshqa sabab · yangi dalil · umumlashmaydi · faktda rozi.</li>"
              "<li>Oltitadan faqat bittasi to'liq rad etish — "
              "<strong>har doim bahs qidirmang</strong>.</li>"
              "<li><em>Both would agree</em> savolida javob eng <u>tor</u> "
              "bayonot bo'ladi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 31
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_XTEXT,
    "title": "SAT R&W 31: Finding the Exact Point of Contact Between Text 1 and Text 2",
    "summary": "Ikki matn faqat bitta nuqtada tegadi; qolgani fon. Tegish nuqtasini "
               "topish savolni yechadi va «rost, lekin so'ralmagan» tuzog'idan qutqaradi.",
    "order": 31,
    "blocks": [
        {"rich_text": (
            "<h2>Bitta tegish nuqtasi</h2>"
            "<p>30-darsda munosabatni nomlashni o'rgandik. Endi undan bir qadam "
            "chuqurroq: <mark>ikki matn bir-biriga faqat bitta joyda tegadi</mark>.</p>"
            "<p>Text 1 da beshta jumla bo'lishi mumkin, Text 2 da to'rtta. Lekin savol "
            "ularning hammasi haqida emas. Deyarli har doim Text 2 ning bitta jumlasi "
            "Text 1 ning bitta jumlasiga <u>to'g'ridan-to'g'ri</u> tegadi. Qolgani — "
            "fon.</p>"
            "<p>Tegish nuqtasini topsangiz, savol o'z-o'zidan yechiladi. Topmasangiz — "
            "variantlar orasida chalkashasiz, chunki ularning bir nechtasi "
            "<u>haqiqiy</u> farqlarni tasvirlaydi.</p>"
            + '<span class="sr-time">⏱ ~90 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Tegish nuqtasini qanday topish kerak</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Text 1 ning <u>da'vo</u> "
              "jumlasini toping.</strong> Har matnda bitta jumla asosiy — qolgani uni "
              "tayyorlaydi yoki ko'taradi. Odatda u ikkinchi yoki oxirgi jumla.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Text 2 ni o'qiyotib "
              "«bu qayerga tegadi?» deb so'rang.</strong> Text 2 ning qaysi jumlasi "
              "Text 1 ning da'vosiga <u>javob beryapti</u>?</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Ikki jumlani yonma-yon "
              "qo'ying.</strong> Xayolan: «Text 1 aytadi X. Text 2 aytadi Y.» "
              "Javob shu ikki jumlaning orasida.</p></div>"
            + "<div class=\"pp-step\"><p><strong>4. Qolgan hamma narsani "
              "e'tiborsiz qoldiring.</strong> Fon ma'lumoti chiroyli bo'lishi mumkin, "
              "lekin u savolga javob bermaydi — va u aynan tuzoq variantlarning "
              "manbai.</p></div>"
            + '</div>'
            + WARN.format(
                "<strong>Bu turning bosh tuzog'i:</strong> variant ikki matn "
                "o'rtasidagi <u>haqiqiy</u> farqni tasvirlaydi — lekin savol "
                "so'ragan farqni emas. Masalan matnlar mavzu bo'yicha ham, uslub "
                "bo'yicha ham farq qiladi; savol esa <em>dating method</em> haqida "
                "so'ragan. Farq rost bo'lgani yetarli emas: u "
                "<mark>tegish nuqtasidagi</mark> farq bo'lishi kerak.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + cross_q(
                "<p>The settlement was assigned to the eighth century on the strength of "
                "its pottery. The vessels found in the lower layers match, in shape and "
                "in the composition of their clay, a well-studied type produced in a "
                "neighbouring region between about 700 and 780. Since the pots were made "
                "then, the argument runs, the layer holding them was laid down then.</p>",
                "<p>Charcoal from the same layers has now been dated directly, and the "
                "results cluster near 900 — more than a century later. Fine pottery of "
                "this kind was expensive, and expensive objects are kept. A household may "
                "hand a vessel down through three generations before it is finally broken "
                "and swept into the ground.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the reasoning described in the last sentence of Text 1?")
            + choices_html([
                "By pointing out that an object can enter a layer long after the date it "
                "was made.",
                "By arguing that the pottery was produced locally rather than imported "
                "from a neighbouring region.",
                "By noting that radiocarbon dating is more precise than the study of "
                "pottery styles.",
                "By suggesting that the lower layers were disturbed by later building on "
                "the site.",
            ])
            + '<span class="sr-time">⏱ ~90 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>1-qadam — Text 1 ning da'vo jumlasi.</strong> Savolning o'zi "
            "uni ko'rsatib turibdi (<em>the last sentence</em>): "
            "<em>Since the pots were made then, … the layer holding them was laid down "
            "then.</em> Ya'ni: <mark>idish yasalgan sana = qatlam yotqizilgan "
            "sana</mark>.</p>"
            "<p><strong>2-qadam — Text 2 ning qaysi jumlasi shunga tegadi?</strong> "
            "Radiouglerod sanasi emas — u faqat <u>natija</u>. Tegish nuqtasi oxirgi "
            "jumla: <em>A household may hand a vessel down through three "
            "generations…</em> Aynan shu jumla Text 1 ning mantiqiy qadamini "
            "sindiradi.</p>"
            "<p><strong>3-qadam — yonma-yon:</strong> «Text 1: yasalgan sana = "
            "ko'milgan sana. Text 2: idish yasalgandan keyin uzoq saqlanishi mumkin.»</p>"
            + why([
                (True, "By pointing out that an object can enter a layer long after the date it was made",
                 "aynan tegish nuqtasi. Uch avlod saqlanishi mumkin bo'lgan idish "
                 "Text 1 ning «yasalgan = ko'milgan» tenglamasini buzadi."),
                (False, "By noting that radiocarbon dating is more precise than the study of pottery styles",
                 "<strong>rost, lekin so'ralmagan</strong> — va bu darsning asosiy "
                 "tuzog'i. Text 2 haqiqatan radiouglerod natijasini keltiradi. "
                 "Lekin savol <u>oxirgi jumladagi mantiq</u> haqida, usullarni "
                 "solishtirish haqida emas. Text 2 hech qayerda o'z usulini "
                 "aniqroq deb atamaydi."),
                (False, "By arguing that the pottery was produced locally rather than imported from a neighbouring region",
                 "Text 2 idishning qayerda yasalganini muhokama qilmaydi. "
                 "<strong>So'z-tuzoq</strong>: Text 1 dagi <em>neighbouring "
                 "region</em> iborasidan yozilgan."),
                (False, "By suggesting that the lower layers were disturbed by later building on the site",
                 "qatlamlarning aralashib ketishi ishonchli arxeologik e'tiroz, va "
                 "shuning uchun jozibali. Lekin Text 2 buni <u>aytmaydi</u> — uning "
                 "izohi butunlay boshqa: idish uzoq saqlangan. "
                 "<strong>Tashqi bilim.</strong>"),
            ])
            + TIP.format(
                "Ikkinchi variantga alohida e'tibor bering. U rost, u Text 2 ga mos, "
                "va u ko'p o'quvchini oladi. Uni faqat bitta narsa o'ldiradi: "
                "<u>savol nima so'raganini eslash</u>. Shuning uchun usulning "
                "1-qadami savolni birinchi o'qish edi.")
        )},

        {
            "rich_text": cross_q(
                "<p>Bees visiting a field of a single crop are more efficient "
                "pollinators than bees in mixed vegetation: they do not waste flights "
                "learning new flower shapes, and a colony placed beside a monoculture "
                "brings back more per hour. Growers who rent hives are paying for exactly "
                "that efficiency.</p>",
                "<p>Colonies wintered beside single crops fail more often than colonies "
                "kept where the vegetation is mixed. A field of one plant flowers for "
                "perhaps three weeks; a hedgerow supplies something for five months. "
                "Efficiency during the bloom is not the number that decides whether a "
                "colony is alive in March.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the claim in Text 1 that growers are paying for efficiency?"),
            "choices": [
                {"text": "By arguing that efficiency measured over a short bloom leaves out what happens to the colony over a year.", "is_correct": True},
                {"text": "By denying that bees in a single crop are more efficient pollinators.", "is_correct": False},
                {"text": "By pointing out that renting hives has become more expensive for growers in recent years.", "is_correct": False},
                {"text": "By suggesting that growers should plant several crops in the same field.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Tegish nuqtasi.</strong> Text 1 ning da'vosi: samaradorlik "
                "— to'g'ri o'lchov, dehqon shuni sotib olyapti. Text 2 ning javob "
                "beruvchi jumlasi — oxirgisi: <em>Efficiency during the bloom is not "
                "the number that decides whether a colony is alive in March.</em></p>"
                "<p>Bu <mark>o'lchov haqidagi bahs</mark>: qaysi raqam muhim? "
                "Munosabat turi — <strong>5: umumlashmaydi</strong> (samaradorlik "
                "gullash davrida to'g'ri, lekin butun yil uchun emas).</p>"
                + why([
                    (True, "By arguing that efficiency measured over a short bloom leaves out what happens to the colony over a year",
                     "aynan oxirgi jumlaning ma'nosi, va uch hafta ↔ besh oy "
                     "taqqoslashi buning isboti."),
                    (False, "By denying that bees in a single crop are more efficient pollinators",
                     "Text 2 samaradorlikni inkor qilmaydi — u uni <u>yetarli "
                     "o'lchov emas</u> deydi. «Cheklash»ni «rad etish» deb o'qish — "
                     "30-darsdagi doimiy xato."),
                    (False, "By pointing out that renting hives has become more expensive for growers in recent years",
                     "narx birorta matnda muhokama qilinmaydi. "
                     "<strong>So'z-tuzoq</strong>: Text 1 dagi <em>rent</em> va "
                     "<em>paying</em> so'zlaridan yozilgan."),
                    (False, "By suggesting that growers should plant several crops in the same field",
                     "<strong>rost bo'lishi mumkin, lekin so'ralmagan</strong>: "
                     "Text 2 aralash o'simlikni maqtaydi, ammo dehqonga hech narsa "
                     "tavsiya qilmaydi. Uning mavzusi — asalari oilasi, ekin "
                     "rejasi emas."),
                ])
            ),
        },

        {
            "rich_text": cross_q(
                "<p>The novelist's late style has often been explained by her illness. "
                "The short sentences and the thinning of description in the final two "
                "books, on this account, record a writer working with less strength than "
                "before.</p>",
                "<p>She had been cutting for a decade. Successive drafts of the earlier "
                "novels, now in the archive, show whole descriptive passages struck out "
                "in her own hand, and a letter from 1961 complains that her published "
                "work is still 'too furnished'. The last books are the end of a road she "
                "had chosen, not a place illness left her.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the explanation given in Text 1?"),
            "choices": [
                {"text": "By offering evidence that the change was a deliberate development rather than a consequence of illness.", "is_correct": True},
                {"text": "By agreeing that the late style is thinner and attributing it to the influence of other writers.", "is_correct": False},
                {"text": "By arguing that the novelist's illness has been exaggerated by her biographers.", "is_correct": False},
                {"text": "By claiming that the earlier novels are of higher quality than the final two.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Tegish nuqtasi.</strong> Text 1: uslub o'zgarishi — "
                "kasallikning izi. Text 2 ning javob beruvchi jumlasi — oxirgisi: "
                "<em>the end of a road she had chosen, not a place illness left "
                "her</em>. <em>not … </em> qurilishi Text 1 ga to'g'ridan-to'g'ri "
                "tegib turibdi.</p>"
                "<p>Munosabat: <strong>3-tur — xuddi shu kuzatuvga boshqa sabab</strong>. "
                "Ikkovi ham uslub o'zgarganiga rozi.</p>"
                + why([
                    (True, "By offering evidence that the change was a deliberate development rather than a consequence of illness",
                     "Text 2 ning ikkita dalili — qoralamalardagi o'chirishlar va "
                     "1961-yilgi xat — aynan «ataylab, uzoq vaqt davomida» "
                     "degan da'voni ko'taradi."),
                    (False, "By agreeing that the late style is thinner and attributing it to the influence of other writers",
                     "<strong>yarim to'g'ri</strong>: birinchi yarmi rost. Lekin "
                     "boshqa yozuvchilarning ta'siri Text 2 da umuman yo'q — u "
                     "yozuvchining <u>o'z</u> qaroriga ishora qiladi. Ikkinchi yarmi "
                     "o'ylab topilgan."),
                    (False, "By arguing that the novelist's illness has been exaggerated by her biographers",
                     "Text 2 kasallikni inkor ham, kamaytirib ham ko'rsatmaydi — u "
                     "kasallikni <u>sabab sifatida</u> rad etadi. Bu ikki xil "
                     "da'vo, va matnda faqat ikkinchisi bor."),
                    (False, "By claiming that the earlier novels are of higher quality than the final two",
                     "sifat baholanmaydi. Ikkala matn ham qaysi kitob yaxshiroq "
                     "ekani haqida bir og'iz gapirmaydi."),
                ])
            ),
        },

        {
            "rich_text": cross_q(
                "<p>Handaxes of a single teardrop shape were made across three "
                "continents for more than a million years. Such stability over such a "
                "span is usually read as evidence that the shape was near-optimal for "
                "butchery and that toolmakers everywhere converged on it.</p>",
                "<p>Many handaxes show no wear along their edges at all. Some are far "
                "larger than a hand can grip; some are made of stone chosen for its "
                "colour rather than its fracture. An object can be copied faithfully for "
                "a very long time without being copied because it works.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the inference drawn in Text 1?"),
            "choices": [
                {"text": "By noting that the shape's persistence need not indicate that it was well suited to its supposed use.", "is_correct": True},
                {"text": "By denying that handaxes of this shape were made across three continents.", "is_correct": False},
                {"text": "By arguing that early toolmakers lacked the skill to produce more effective shapes.", "is_correct": False},
                {"text": "By proposing that handaxes were used for cutting plants rather than for butchery.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Tegish nuqtasi.</strong> Text 1 ning mantiqiy qadami: "
                "uzoq saqlanish → demak yaxshi ishlagan. Text 2 ning oxirgi jumlasi "
                "aynan shu qadamga tegadi: <em>An object can be copied faithfully for "
                "a very long time without being copied because it works.</em></p>"
                "<p>Diqqat: Text 2 <u>boshqa maqsad taklif qilmaydi</u>. U faqat "
                "<mark>xulosaning mantiqi</mark>ni buzadi — bu SAT'ning sevimli "
                "harakati.</p>"
                + why([
                    (True, "By noting that the shape's persistence need not indicate that it was well suited to its supposed use",
                     "Text 2 ning oxirgi jumlasining aynan tarjimasi, va yeyilmagan "
                     "qirralar bilan tutib bo'lmaydigan o'lchamlar buning dalili."),
                    (False, "By proposing that handaxes were used for cutting plants rather than for butchery",
                     "<strong>eng jozibali tuzoq</strong>: matn qassoblikka shubha "
                     "qilgani uchun o'quvchi «unda nima uchun ishlatilgan?» deb "
                     "o'ylaydi va javobni o'zi to'qiydi. Text 2 birorta muqobil "
                     "maqsad taklif qilmaydi."),
                    (False, "By denying that handaxes of this shape were made across three continents",
                     "tarqalish fakti inkor qilinmaydi — Text 2 uni qabul qiladi va "
                     "undan chiqarilgan <u>xulosaga</u> e'tiroz bildiradi."),
                    (False, "By arguing that early toolmakers lacked the skill to produce more effective shapes",
                     "mahorat masalasi ko'tarilmaydi — aksincha, <em>copied "
                     "faithfully</em> yuqori mahoratni nazarda tutadi. "
                     "<strong>Tashqi bilim.</strong>"),
                ])
                + NOTE.format(
                    "To'rtala savolda ham Text 2 ning <u>oxirgi jumlasi</u> tegish "
                    "nuqtasi bo'lib chiqdi. Bu tasodif emas: Text 2 odatda dalilni "
                    "avval beradi, keyin uni Text 1 ga qaratadi. "
                    "<strong>Vaqtingiz kam bo'lsa — Text 2 ning oxirgi jumlasidan "
                    "boshlang.</strong>")
        )},

        {
            "rich_text": cross_q(
                "<p>The floor of the dry lake is remarkably smooth over several "
                "kilometres. The accepted explanation is a single catastrophic flood: a "
                "wall of water crossed the basin, scoured it flat in a matter of hours "
                "and drained away.</p>",
                "<p>Cores taken through the floor pass through dozens of thin layers, "
                "each graded from coarse grains at its base to fine ones at its top, and "
                "each capped by a band of clay of the kind that settles only in water "
                "left still for years. The basin is also unusually deep for the "
                "region.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the explanation described in Text 1?"),
            "choices": [
                {"text": "By presenting evidence that the floor was built up by many separate episodes over a long period.", "is_correct": True},
                {"text": "By noting that the basin is deeper than others in the surrounding region.", "is_correct": False},
                {"text": "By arguing that no flood has ever crossed the basin.", "is_correct": False},
                {"text": "By suggesting that the coring method is too imprecise to settle the question.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Tegish nuqtasi.</strong> Text 1 ning da\u2019vosi: "
                "<u>bitta</u> hodisa, <u>bir necha soat</u>. Text 2 ning javob "
                "beruvchi qismi: o\u2018nlab qatlam, va har biri yillar davomida tinch "
                "suvda cho\u2018kadigan gil bilan yopilgan.</p>"
                "<p>Ya\u2019ni: <mark>bitta tez hodisa \u2194 ko\u2018p va sekin "
                "hodisalar</mark>.</p>"
                + why([
                    (True, "By presenting evidence that the floor was built up by many separate episodes over a long period",
                     "har qatlamning gradatsiyasi alohida hodisani, gil qopqog\u2018i esa "
                     "orasidagi uzoq tinchlikni bildiradi \u2014 ikkovi birga Text 1 "
                     "ning \u00abbir necha soat\u00bb da\u2019vosini sindiradi."),
                    (False, "By noting that the basin is deeper than others in the surrounding region",
                     "<strong>bu darsning asosiy tuzog\u2018i</strong>: gap Text 2 da "
                     "<u>haqiqatan bor</u>. Lekin u tegish nuqtasi emas \u2014 chuqurlik "
                     "Text 1 ning tushuntirishiga hech qanday e\u2019tiroz bildirmaydi. "
                     "<strong>Rost, lekin so\u2018ralmagan.</strong>"),
                    (False, "By arguing that no flood has ever crossed the basin",
                     "<strong>haddan tashqari kuchli.</strong> Text 2 suv toshqinini "
                     "umuman inkor qilmaydi \u2014 u tekislikni <u>bitta</u> toshqin "
                     "yasagan degan da\u2019voga qarshi turibdi."),
                    (False, "By suggesting that the coring method is too imprecise to settle the question",
                     "Text 2 aynan o\u2018sha usulning natijalariga tayanadi \u2014 uni "
                     "shubha ostiga olish o\u2018z dalilini yo\u2018q qilardi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">an inference</div><div class="pp-card-back">xulosa (dalildan chiqarilgan)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to draw an inference</div><div class="pp-card-back">xulosa chiqarmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">persistence</div><div class="pp-card-back">saqlanib qolish, davomiylik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">need not indicate ~</div><div class="pp-card-back">~ ni bildirishi shart emas</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">deliberate</div><div class="pp-card-back">ataylab qilingan, o\'ylangan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to hand down</div><div class="pp-card-back">avloddan avlodga o\'tkazmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to strike out (a passage)</div><div class="pp-card-back">(parchani) o\'chirib tashlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">monoculture</div><div class="pp-card-back">yakka ekin (bitta o\'simlik ekilgan maydon)</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Ikki matn <strong>bitta nuqtada</strong> tegadi; qolgani fon.</li>"
              "<li>Text 1 ning <u>da'vo</u> jumlasini toping, keyin Text 2 ning unga "
              "javob beruvchi jumlasini.</li>"
              "<li>Vaqt kam bo'lsa — <strong>Text 2 ning oxirgi jumlasidan</strong> "
              "boshlang.</li>"
              "<li>Bosh tuzoq: <strong>rost farq, lekin savol so'ragan farq emas</strong>.</li>"
              "<li>Text 2 xulosaning mantiqini buzsa, u <u>muqobil javob taklif "
              "qilishi shart emas</u> — javobni o'zingiz to'qimang.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 32
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_XTEXT,
    "title": "SAT R&W 32: “How Would the Author of Text 2 Respond?” — Answering in the Author's Voice",
    "summary": "Javobni siz emas, Text 2 muallifi beradi — va faqat Text 2 da bor "
               "narsa bilan; yo'nalishni teskari o'qish esa doimiy xato.",
    "order": 32,
    "blocks": [
        {"rich_text": (
            "<h2>Siz emas — u javob beradi</h2>"
            "<p>Bu turdagi eng ko'p uchraydigan savol shakli: "
            "<em>Based on the texts, how would the author of Text 2 most likely respond "
            "to …?</em></p>"
            "<p>Savol sizdan fikr so'ramayapti. U sizdan <mark>boshqa odamning "
            "og'zidan gapirish</mark>ni so'rayapti. Va o'sha odam haqida siz "
            "bilgan yagona narsa — Text 2 da yozilgani.</p>"
            + EXAMP.format(
                "<p style=\"font-size:1.06em;margin:0;\">To'g'ri javob uchta shartni "
                "birdan bajaradi:<br>"
                "<strong>1.</strong> Text 2 muallifi buni aytishga <u>asosi bor</u>;<br>"
                "<strong>2.</strong> u Text 1 dagi <u>aynan o'sha</u> narsaga "
                "tegadi;<br>"
                "<strong>3.</strong> u Text 2 da <u>bor</u> — sizning bilimingizdan "
                "emas.</p>")
            + '<span class="sr-time">⏱ ~90 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Uchta manba, uchta tuzoq</h3>"
            "<p>Noto'g'ri variantlar deyarli har doim javobni <u>noto'g'ri joydan</u> "
            "oladi:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Javob qayerdan olingan</th><th>Nega tuzoq</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Sizning fikringizdan</strong></td>"
              "<td>Mavzu tanish bo'lsa, siz o'z xulosangizni muallifga "
              "yopishtirasiz</td></tr>"
              "<tr><td><strong>Text 1 dan</strong></td>"
              "<td>Variant Text 1 ning fikrini takrorlaydi — lekin javob beradigan "
              "odam Text 2 muallifi</td></tr>"
              "<tr><td><strong>Dunyoda rost narsadan</strong></td>"
              "<td>To'g'ri gap, lekin bu ikki matnning hech birida yo'q</td></tr>"
              "<tr><td><strong>Text 2 dan, lekin haddan tashqari kuchli</strong></td>"
              "<td>Text 2 «ba'zan» degan joyda variant «hech qachon» deydi</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<strong>Yo'nalish xatosi.</strong> <em>How would the author of "
                "<u>Text 2</u> respond to <u>Text 1</u></em> va "
                "<em>… <u>Text 1</u> respond to <u>Text 2</u></em> — bu ikki xil "
                "savol, va SAT ikkalasini ham beradi. Savolni o'qiyotib "
                "<u>kim gapiryapti</u> va <u>nimaga javob beryapti</u> — ikkovini "
                "ham belgilang. Yo'nalishni teskari o'qigan o'quvchi uchun "
                "to'g'ri javob variantlar orasida umuman ko'rinmaydi.")
        )},

        {"rich_text": (
            "<h3>Kuch darajasiga qarang</h3>"
            "<p>Bu turda variantlar ko'pincha bir xil fikrni <u>turli kuch</u> bilan "
            "aytadi. Text 2 ning o'z ohangi javobni tanlaydi:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Text 2 shunday yozsa</th><th>Javob shunday bo'ladi</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>may · suggests · in some cases</em></td>"
              "<td>ehtiyotkor: <em>by suggesting that…</em></td></tr>"
              "<tr><td><em>shows · demonstrates · consistently</em></td>"
              "<td>qat'iy: <em>by arguing that…</em></td></tr>"
              "<tr><td>Faqat bitta holatni keltiradi</td>"
              "<td><em>by pointing out that…</em> — kichik, aniq e'tiroz</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Ikki variant bir xil fikrni aytayotgan bo'lsa, ularning "
                "<strong>fe'llarini</strong> solishtiring: <em>suggesting</em> "
                "vs <em>proving</em>, <em>questioning</em> vs <em>refuting</em>. "
                "Text 2 hech qachon isbotlamagan narsani «isbotladi» deb "
                "ko'rsatadigan variant — tuzoq.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + cross_q(
                "<p>Children who are read to at home arrive at school with larger "
                "vocabularies, and the gap between them and other children widens over "
                "the following years. Reading aloud in the early years, then, does more "
                "than teach words: it starts a process that keeps compounding long after "
                "the reading has stopped.</p>",
                "<p>Households where an adult reads aloud differ from other households in "
                "many ways at once — in income, in hours worked, in how quiet the rooms "
                "are. Where a programme has supplied books and shown parents how to use "
                "them, vocabulary gains appear but are smaller than the gap between the "
                "two kinds of household would predict.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the conclusion drawn in Text 1?")
            + choices_html([
                "By arguing that reading aloud to children has no effect on their "
                "vocabulary.",
                "By suggesting that some of the gap may be produced by other differences "
                "between the households rather than by the reading itself.",
                "By agreeing that early reading starts a process that continues to "
                "compound for years.",
                "By recommending that schools provide books to every family in the "
                "district.",
            ])
            + '<span class="sr-time">⏱ ~90 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>Yo'nalish:</strong> Text 2 muallifi → Text 1 ning "
            "<u>xulosasiga</u>.</p>"
            "<p><strong>Text 1 bitta jumlada:</strong> «ovoz chiqarib o'qish "
            "so'z boyligini oshiradi va ta'sir yillar davomida ko'payib boradi».</p>"
            "<p><strong>Text 2 bitta jumlada:</strong> «bunday oilalar boshqa ko'p "
            "jihatdan ham farq qiladi, va kitob bergan dasturlarda foyda bor-u, "
            "kutilganidan kichik».</p>"
            "<p><strong>Kuch darajasi:</strong> Text 2 <em>smaller than … would "
            "predict</em> deydi — ya'ni foyda <u>bor</u>, lekin hammasini o'qish "
            "tushuntirmaydi. Ehtiyotkor ohang. Demak javob ham ehtiyotkor "
            "bo'lishi kerak: <mark><em>by suggesting</em>, «ba'zi qismi»</mark>.</p>"
            + why([
                (True, "By suggesting that some of the gap may be produced by other differences between the households rather than by the reading itself",
                 "<em>some</em> va <em>may</em> — Text 2 ning o'z kuch darajasiga "
                 "aynan mos. Va dalili ham shu: dastur o'qishni qo'shganda foyda "
                 "kutilganidan kichik chiqdi, demak farqning bir qismi boshqa "
                 "narsadan."),
                (False, "By arguing that reading aloud to children has no effect on their vocabulary",
                 "<strong>haddan tashqari kuchli.</strong> Text 2 aynan aksini "
                 "aytadi: <em>vocabulary gains appear</em>. Foydaning "
                 "<u>kichikligi</u>ni «yo'qligi» deb o'qish — bu turdagi eng ko'p "
                 "uchraydigan xato."),
                (False, "By agreeing that early reading starts a process that continues to compound for years",
                 "bu <strong>Text 1 ning fikri</strong>, Text 2 niki emas. "
                 "Javob beradigan odam Text 2 muallifi ekanini unutgan o'quvchi "
                 "shu variantni tanlaydi."),
                (False, "By recommending that schools provide books to every family in the district",
                 "Text 2 dasturni <u>dalil sifatida</u> keltiradi, tavsiya sifatida "
                 "emas — va uning natijasi kutilganidan zaif chiqdi, ya'ni bu "
                 "tavsiya matnning o'z dalilidan ham kelib chiqmaydi."),
            ])
            + NOTE.format(
                "Bu matn juftligi <strong>korrelyatsiya ↔ sabab</strong> "
                "muammosining klassik shakli, va SAT uni juda yaxshi ko'radi. "
                "Text 1 bog'liqlikni ko'radi va sababni chiqaradi; Text 2 "
                "«balki uchinchi narsa ikkovini ham keltirib chiqargandir» deydi. "
                "Bu shaklni tanib olsangiz, javob deyarli har doim "
                "<u>ehtiyotkor va «boshqa farqlar» haqida</u> bo'ladi.")
        )},

        {
            "rich_text": cross_q(
                "<p>Cities that painted their roofs white recorded lower indoor "
                "temperatures the following summer, in some blocks by three degrees. "
                "Since the paint is cheap and needs no machinery, it is among the few "
                "cooling measures a poor city can afford at scale.</p>",
                "<p>A white roof reflects sunlight back into the street, where it is "
                "absorbed by walls and pavement. Measurements at head height on painted "
                "blocks show air temperatures a little higher than on unpainted ones. The "
                "building is cooler; the person walking past it is not.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the recommendation in Text 1?"),
            "choices": [
                {"text": "By pointing out that the measure improves conditions indoors while making them slightly worse in the street.", "is_correct": True},
                {"text": "By arguing that white roofs do not lower indoor temperatures at all.", "is_correct": False},
                {"text": "By agreeing that white paint is the most affordable cooling measure available to a poor city.", "is_correct": False},
                {"text": "By suggesting that cities should install air conditioning in public buildings instead.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Yo'nalish:</strong> Text 2 → Text 1 ning tavsiyasiga.</p>"
                "<p><strong>Kuch darajasi:</strong> Text 2 <em>a little higher</em> "
                "deydi — kichik, aniq kuzatuv. Va u ichkaridagi sovushni inkor "
                "qilmaydi: <em>The building is cooler</em>. Demak javob "
                "<mark>kichik va aniq</mark> bo'lishi kerak: <em>by pointing "
                "out</em>.</p>"
                + why([
                    (True, "By pointing out that the measure improves conditions indoors while making them slightly worse in the street",
                     "Text 2 ning oxirgi jumlasining aynan mazmuni: <em>The building "
                     "is cooler; the person walking past it is not.</em> Ikkala "
                     "yarmi ham matnda bor."),
                    (False, "By arguing that white roofs do not lower indoor temperatures at all",
                     "<strong>haddan tashqari kuchli va matnga zid</strong>: "
                     "<em>The building is cooler</em>. Text 2 ichkaridagi foydani "
                     "tan oladi."),
                    (False, "By agreeing that white paint is the most affordable cooling measure available to a poor city",
                     "bu <strong>Text 1 ning fikri</strong>. Text 2 narx haqida "
                     "umuman gapirmaydi."),
                    (False, "By suggesting that cities should install air conditioning in public buildings instead",
                     "konditsioner birorta matnda yo'q, va Text 2 hech qanday "
                     "muqobil taklif qilmaydi. <strong>Tashqi bilim.</strong>"),
                ])
            ),
        },

        {
            "rich_text": cross_q(
                "<p>A committee that must reach a unanimous verdict deliberates longer "
                "and examines more of the evidence than one that needs only a majority. "
                "Requiring unanimity therefore produces better-reasoned decisions.</p>",
                "<p>Recordings of unanimous-verdict deliberations show that the extra time "
                "is not evenly spent. Once a large majority has formed, the discussion "
                "turns from the evidence to the holdouts, and the additional minutes go "
                "to persuading two people rather than to examining anything.</p>",
                "Based on the texts, how would the author of Text 1 most likely respond "
                "to the findings reported in Text 2?"),
            "choices": [
                {"text": "Text 1's author would need to explain why longer deliberation should still count as better reasoning.", "is_correct": True},
                {"text": "Text 1's author would agree that unanimity requirements should be abandoned entirely.", "is_correct": False},
                {"text": "Text 1's author would point out that recordings cannot capture what jurors are thinking.", "is_correct": False},
                {"text": "Text 1's author would note that majority verdicts take less time to reach.", "is_correct": False},
            ],
            "explanation": (
                "<p>⚠️ <strong>Yo'nalish teskari!</strong> Bu safar "
                "<u>Text 1</u> muallifi javob beryapti, <u>Text 2</u> ga. "
                "Savolni shoshib o'qigan o'quvchi bu savolni yo'qotadi.</p>"
                "<p><strong>Text 1 ning mantiqiy zanjiri:</strong> uzunroq muhokama → "
                "ko'proq dalil ko'rildi → yaxshiroq qaror. Text 2 o'rtadagi bo'g'inni "
                "sindiradi: qo'shimcha vaqt dalilga emas, <u>ikki kishini "
                "ko'ndirishga</u> ketgan.</p>"
                "<p>Demak Text 1 muallifi endi nimadadir hisob berishi kerak: "
                "<mark>agar qo'shimcha vaqt dalilga sarflanmagan bo'lsa, uning "
                "«yaxshiroq qaror» degan xulosasi nimaga tayanadi?</mark></p>"
                + why([
                    (True, "Text 1's author would need to explain why longer deliberation should still count as better reasoning",
                     "Text 2 aynan Text 1 ning zanjiridagi bo'g'inni oladi, shuning "
                     "uchun Text 1 muallifining vazifasi — o'sha bo'g'inni qayta "
                     "asoslash. Bu savol turining ko'p uchraydigan javob shakli: "
                     "«u endi shuni tushuntirishi kerak bo'lardi»."),
                    (False, "Text 1's author would agree that unanimity requirements should be abandoned entirely",
                     "Text 1 muallifi bir tadqiqotdan keyin o'z pozitsiyasidan "
                     "butunlay voz kechmaydi, va <em>entirely</em> "
                     "<strong>haddan tashqari kuchli</strong>. Text 2 ham bekor "
                     "qilishni taklif qilmaydi."),
                    (False, "Text 1's author would point out that recordings cannot capture what jurors are thinking",
                     "e'tiroz o'zicha aqlli, lekin u <strong>o'quvchining "
                     "o'yidan</strong> chiqadi — Text 1 da usul haqida bir og'iz "
                     "ham yo'q. Muallifga o'zingiz o'ylab topgan dalilni "
                     "yopishtirmang."),
                    (False, "Text 1's author would note that majority verdicts take less time to reach",
                     "bu Text 1 da bor, lekin u <u>Text 2 ga javob emas</u> — "
                     "shunchaki oldin aytilgan gapni takrorlaydi va Text 2 "
                     "ko'targan muammoga tegmaydi."),
                ])
                + TIP.format(
                    "Yo'nalishni belgilash uchun oddiy odat: savolni o'qiyotib "
                    "barmog'ingiz bilan «kim» va «nimaga» ni ko'rsating. "
                    "Ikki soniya, va bu savol turidagi eng qimmat xatoni butunlay "
                    "yo'q qiladi.")
            ),
        },

        {
            "rich_text": cross_q(
                "<p>Museums have begun returning objects taken during colonial rule, and "
                "the usual objection is practical: that the receiving institutions lack "
                "the climate control and security that keep fragile things intact.</p>",
                "<p>The objection describes a condition, not a principle, and conditions "
                "change. Where funds for a purpose-built store have been raised — "
                "sometimes by the returning museum itself — the argument has simply "
                "dissolved. What it was defending in the meantime was possession.</p>",
                "Based on the texts, how would the author of Text 2 most likely "
                "characterise the objection described in Text 1?"),
            "choices": [
                {"text": "As a temporary difficulty that has been treated as though it were a permanent reason.", "is_correct": True},
                {"text": "As a well-founded concern that should prevent most returns from taking place.", "is_correct": False},
                {"text": "As a problem that receiving institutions have shown no interest in solving.", "is_correct": False},
                {"text": "As evidence that colonial-era collecting was more careful than is usually admitted.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Text 2 ning kalit jumlasi:</strong> <em>The objection "
                "describes a condition, not a principle, and conditions change.</em> "
                "Bundan aniqroq bo'lmaydi — e'tiroz <mark>vaqtinchalik holat</mark>, "
                "abadiy sabab emas.</p>"
                "<p>Va oxirgi jumla ohangni beradi: <em>What it was defending in the "
                "meantime was possession</em> — ya'ni e'tiroz aslida boshqa narsani "
                "himoya qilib turgan.</p>"
                + why([
                    (True, "As a temporary difficulty that has been treated as though it were a permanent reason",
                     "<em>a condition, not a principle</em> ning aynan tarjimasi, va "
                     "<em>the argument has simply dissolved</em> uning "
                     "vaqtinchaligining isboti."),
                    (False, "As a well-founded concern that should prevent most returns from taking place",
                     "Text 2 aynan bunga qarshi turibdi. Bu <strong>Text 1 ning "
                     "pozitsiyasi</strong>ni Text 2 muallifining og'ziga solish."),
                    (False, "As a problem that receiving institutions have shown no interest in solving",
                     "matnga zid: mablag' <u>yig'ilgan</u> (<em>funds … have been "
                     "raised</em>). Text 2 qabul qiluvchi muassasalarni tanqid "
                     "qilmaydi."),
                    (False, "As evidence that colonial-era collecting was more careful than is usually admitted",
                     "kolonial davrdagi to'plash usuli baholanmaydi. "
                     "<strong>Mavzudan chiqib ketgan</strong> variant — ikkala matn "
                     "ham bugungi qaytarish haqida."),
                ])
            ),
        },

        {
            "rich_text": cross_q(
                "<p>Employees at a large firm who were offered flexible starting hours "
                "reported markedly higher satisfaction a year later, and turnover among "
                "them fell. Flexibility of this kind costs an employer almost nothing and "
                "should be offered wherever people work.</p>",
                "<p>Take-up in that firm was concentrated almost entirely among staff "
                "whose work passes to nobody at the end of the day. Where a post must be "
                "handed over to the next person on duty, the same offer was made and went "
                "almost unused, and satisfaction there did not move.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the recommendation in Text 1?"),
            "choices": [
                {"text": "By suggesting that the benefit may not extend to kinds of work the study's participants barely represented.", "is_correct": True},
                {"text": "By arguing that flexible hours reduce employee satisfaction.", "is_correct": False},
                {"text": "By agreeing that flexible starting hours should be offered in every workplace.", "is_correct": False},
                {"text": "By recommending that firms reorganise their shifts to remove handovers.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Yo\u2018nalish:</strong> Text 2 \u2192 Text 1 ning "
                "<u>tavsiyasiga</u> (<em>should be offered wherever people work</em>).</p>"
                "<p><strong>Munosabat:</strong> 5-tur \u2014 umumlashmaydi. Text 2 "
                "natijani inkor qilmaydi; u natija <u>kimlarda</u> olinganini "
                "ko\u2018rsatadi.</p>"
                "<p><strong>Kuch darajasi:</strong> Text 2 bitta firmadan gapiradi, "
                "shuning uchun javob ham ehtiyotkor bo\u2018lishi kerak \u2014 "
                "<em>may not extend</em>.</p>"
                + why([
                    (True, "By suggesting that the benefit may not extend to kinds of work the study's participants barely represented",
                     "aynan Text 2 ning dalili: navbat topshiradigan xodimlar "
                     "orasida taklif ishlamagan, ya\u2019ni <em>wherever people "
                     "work</em> asossiz."),
                    (False, "By arguing that flexible hours reduce employee satisfaction",
                     "<strong>haddan tashqari kuchli va matnga zid</strong>: Text 2 "
                     "o\u2018sha guruhda mamnunlik <em>did not move</em> deydi \u2014 "
                     "pasaydi demaydi."),
                    (False, "By agreeing that flexible starting hours should be offered in every workplace",
                     "bu <strong>Text 1 ning tavsiyasi</strong>, va Text 2 aynan "
                     "unga qarshi turibdi."),
                    (False, "By recommending that firms reorganise their shifts to remove handovers",
                     "Text 2 hech narsa tavsiya qilmaydi. Navbat topshirish uning "
                     "uchun \u2014 <u>tushuntiruvchi shart</u>, yo\u2018q qilinadigan "
                     "muammo emas. <strong>O\u2018quvchi to\u2018qiydigan uchinchi yo\u2018l.</strong>"),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to respond to a claim</div><div class="pp-card-back">da\'voga javob bermoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to point out that ~</div><div class="pp-card-back">~ ga e\'tibor qaratmoq (kichik, aniq e\'tiroz)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to compound</div><div class="pp-card-back">ortib bormoq, kuchayib ko\'payib bormoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a holdout</div><div class="pp-card-back">rozi bo\'lmay turgan kishi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a condition, not a principle</div><div class="pp-card-back">holat, printsip emas</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to dissolve (of an argument)</div><div class="pp-card-back">(dalil) o\'z-o\'zidan yo\'qolmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">unanimous</div><div class="pp-card-back">bir ovozdan, yakdil</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">well-founded</div><div class="pp-card-back">asosli, o\'rinli</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Javobni <strong>siz emas, matn muallifi</strong> beradi — va faqat "
              "o'z matnidagi narsa bilan.</li>"
              "<li>Savolda <u>kim</u> gapiryapti va <u>nimaga</u> javob beryapti — "
              "ikkovini ham belgilang.</li>"
              "<li>Variantning <strong>fe'liga</strong> qarang: "
              "<em>suggesting</em> ≠ <em>proving</em>.</li>"
              "<li>Eng ko'p xato: cheklashni <u>to'liq inkor</u> deb o'qish "
              "(<em>smaller</em> → <em>no effect</em>).</li>"
              "<li>Ikkinchi eng ko'p xato: <strong>Text 1 ning fikrini</strong> "
              "Text 2 muallifiga yopishtirish.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 33
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_XTEXT,
    "title": "SAT R&W 33: Cross-Text Connections — Mixed Practice",
    "summary": "Oltita ikki matnli savol, barcha yo'nalishlar aralash, imtihon "
               "tezligida: 30–32-darslardagi usulni soatga qarshi mustahkamlash.",
    "order": 33,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy amaliyot</h2>"
            "<p>Oltita savol, barcha shakllar aralash: <em>how would Text 2 "
            "respond</em>, <em>how would Text 1 respond</em>, <em>both would "
            "agree</em>, <em>a difference in how the two texts characterise</em>.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Qanday ishlash kerak:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li>Taymer: <strong>9 daqiqa</strong> (6 × 90 soniya). Bu tur "
                "sekin — imtihonda ham shunday.</li>"
                "<li>Har matnni <u>bitta jumlaga siqing</u>, keyin munosabatni "
                "nomlang.</li>"
                "<li>Savoldagi <u>yo'nalishni</u> barmoq bilan belgilang.</li>"
                "</ol>")
            + '<span class="sr-time">⏱ 6 savol · 9 daqiqa</span>'
        )},

        {
            "rich_text": cross_q(
                "<p>Birds in cities sing at a higher pitch than the same species in "
                "woodland. Low frequencies are swallowed by traffic noise, so a bird "
                "singing low in a city is not heard; the higher song carries. City "
                "populations have adjusted their song to the noise around them.</p>",
                "<p>High song also travels better among hard flat surfaces, and it is "
                "produced by birds perched high up. City birds sing from roofs and "
                "aerials because there is little else; woodland birds sing from within "
                "foliage. Perch height alone predicts pitch about as well as noise "
                "does.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the explanation offered in Text 1?"),
            "choices": [
                {"text": "By noting that a second factor predicts the same difference and has not been ruled out.", "is_correct": True},
                {"text": "By denying that city birds sing at a higher pitch than woodland birds.", "is_correct": False},
                {"text": "By arguing that traffic noise has no effect on any aspect of bird behaviour.", "is_correct": False},
                {"text": "By suggesting that city birds should be relocated to quieter habitats.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Munosabat:</strong> 3-tur — <u>xuddi shu kuzatuvga boshqa "
                "sabab</u>. Text 2 balandroq sayrashni inkor qilmaydi; u ikkinchi "
                "izohni qo'yadi va oxirgi jumlada uni tenglashtiradi: "
                "<em>Perch height alone predicts pitch about as well as noise "
                "does.</em></p>"
                + why([
                    (True, "By noting that a second factor predicts the same difference and has not been ruled out",
                     "Text 2 ning oxirgi jumlasining aynan mazmuni. <em>as well as</em> "
                     "— ya'ni ikkinchi omil kamida bir xil kuchda, demak Text 1 ning "
                     "izohi yagona emas."),
                    (False, "By denying that city birds sing at a higher pitch than woodland birds",
                     "farq ikkala matnda ham qabul qilingan. Text 2 uni "
                     "<u>tushuntirish</u> yo'lida raqobat qilyapti, inkor "
                     "qilmayapti."),
                    (False, "By arguing that traffic noise has no effect on any aspect of bird behaviour",
                     "<strong>haddan tashqari kuchli</strong> va matndan chiqmaydi: "
                     "Text 2 shovqinni bekor qilmaydi, u faqat <em>about as well "
                     "as</em> deb tenglashtiradi."),
                    (False, "By suggesting that city birds should be relocated to quieter habitats",
                     "birorta matn hech narsa tavsiya qilmaydi. "
                     "<strong>Tashqi bilim.</strong>"),
                ])
            ),
        },

        {
            "rich_text": cross_q(
                "<p>The diary is the most trustworthy of historical sources. Unlike a "
                "memoir, it is written before the outcome is known, and unlike a letter, "
                "it is addressed to nobody who must be impressed.</p>",
                "<p>Nineteenth-century diarists knew their volumes would be read by "
                "children and executors, and many wrote with that reader in view; a "
                "number left instructions for which years were to be destroyed. The "
                "absence of an addressee is an assumption, not a feature of the "
                "form.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the claim in Text 1 that a diary is addressed to nobody?"),
            "choices": [
                {"text": "By arguing that diarists often did write with a future reader in mind.", "is_correct": True},
                {"text": "By agreeing that diaries are more trustworthy than memoirs because they precede the outcome.", "is_correct": False},
                {"text": "By claiming that most nineteenth-century diaries have not survived.", "is_correct": False},
                {"text": "By asserting that letters are a more reliable source than diaries are.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Tegish nuqtasi</strong> savolda ko'rsatilgan: "
                "<em>addressed to nobody</em>. Text 2 ning javob beruvchi jumlasi — "
                "oxirgisi: <em>The absence of an addressee is an assumption, not a "
                "feature of the form.</em></p>"
                + why([
                    (True, "By arguing that diarists often did write with a future reader in mind",
                     "aynan Text 2 ning dalili: bolalar va vasiylar o'qishini bilgan, "
                     "ba'zilari qaysi yillarni yo'q qilishni ko'rsatib ketgan."),
                    (False, "By agreeing that diaries are more trustworthy than memoirs because they precede the outcome",
                     "bu <strong>Text 1 ning fikri</strong>, va Text 2 uni umuman "
                     "muhokama qilmaydi — uning e'tirozi faqat manzil masalasida."),
                    (False, "By claiming that most nineteenth-century diaries have not survived",
                     "saqlanish darajasi eslatilmaydi. <strong>So'z-tuzoq</strong>: "
                     "<em>destroyed</em> so'zidan yozilgan, lekin u ayrim yillarga "
                     "tegishli, umumiy saqlanishga emas."),
                    (False, "By asserting that letters are a more reliable source than diaries are",
                     "Text 2 xatlarni umuman tilga olmaydi. Text 1 dagi qiyoslash "
                     "teskari qilingan."),
                ])
            ),
        },

        {
            "rich_text": cross_q(
                "<p>Open-plan offices were introduced to increase the number of "
                "unplanned conversations between colleagues. Removing walls puts people "
                "in one another's sight, and being in sight is the first condition of "
                "speaking.</p>",
                "<p>When two firms moved to open floors, electronic badges recorded "
                "face-to-face interaction falling by roughly two thirds, while messaging "
                "between the same people rose. Removed walls did put employees in sight "
                "of each other. What people appear to have done in response was withdraw "
                "behind headphones and a screen.</p>",
                "Based on the texts, which choice best describes a difference in how the "
                "two texts treat the relationship between visibility and conversation?"),
            "choices": [
                {"text": "Text 1 treats being in sight as leading to conversation, whereas Text 2 reports that it was followed by less of it.", "is_correct": True},
                {"text": "Text 1 describes open-plan offices approvingly, whereas Text 2 describes the cost of the furniture involved.", "is_correct": False},
                {"text": "Text 1 discusses two firms in detail, whereas Text 2 discusses offices in general terms.", "is_correct": False},
                {"text": "Text 1 claims that messaging is more efficient than speaking, whereas Text 2 disputes this.", "is_correct": False},
            ],
            "explanation": (
                "<p>Savol <u>aniq bir munosabat</u> haqida: ko'rinish ↔ suhbat. "
                "Javob shu ikki tushunchani bog'lashi shart.</p>"
                "<p><strong>Text 1:</strong> ko'rinish — gapirishning birinchi sharti. "
                "<strong>Text 2:</strong> ko'rinish bo'ldi "
                "(<em>did put employees in sight</em>), suhbat esa uchdan ikkiga "
                "kamaydi.</p>"
                + why([
                    (True, "Text 1 treats being in sight as leading to conversation, whereas Text 2 reports that it was followed by less of it",
                     "ikkala matnning aynan shu munosabatga bo'lgan qarashini "
                     "juftlaydi, va Text 2 ning <em>did put … in sight</em> "
                     "e'tirofini ham saqlaydi."),
                    (False, "Text 1 describes open-plan offices approvingly, whereas Text 2 describes the cost of the furniture involved",
                     "<strong>yarim to'g'ri</strong>: Text 1 ijobiy ohangda. Lekin "
                     "mebel narxi Text 2 da umuman yo'q, va savol narx haqida "
                     "so'ramagan."),
                    (False, "Text 1 discusses two firms in detail, whereas Text 2 discusses offices in general terms",
                     "<strong>teskari</strong>: ikkita firma <u>Text 2</u> da. "
                     "Matnlarni almashtirib yuborish — bu turdagi doimiy xato."),
                    (False, "Text 1 claims that messaging is more efficient than speaking, whereas Text 2 disputes this",
                     "Text 1 xabar almashishni umuman eslatmaydi."),
                ])
            ),
        },

        {
            "rich_text": cross_q(
                "<p>A language dies when its last fluent speaker dies, and the count of "
                "living languages falls accordingly. On current rates a large share of "
                "the world's languages will be gone within the century.</p>",
                "<p>Counting fluent speakers misses what is happening in several "
                "communities where the last such speakers died decades ago. Children "
                "there are now learning the language from recordings and grammars, and "
                "using it daily among themselves. Whether the result is the same language "
                "is a question worth asking; that people are speaking it is not in "
                "doubt.</p>",
                "Based on the texts, both authors would most likely agree with which "
                "statement?"),
            "choices": [
                {"text": "The number of people who speak a language fluently can fall to zero.", "is_correct": True},
                {"text": "A language that has lost its last fluent speaker can always be brought back.", "is_correct": False},
                {"text": "Counting fluent speakers is the best available measure of a language's survival.", "is_correct": False},
                {"text": "Most of the world's languages will still be spoken in a century's time.", "is_correct": False},
            ],
            "explanation": (
                "<p><em>Both would agree</em> — kesishmani qidiramiz, va u har doim "
                "<mark>eng tor bayonot</mark> bo'ladi.</p>"
                "<p>Text 1: oxirgi ravon so'zlovchi o'ladi. Text 2: "
                "<em>the last such speakers died decades ago</em> — u ham xuddi shu "
                "faktni qabul qiladi va undan boshqa xulosa chiqaradi. Kesishma — "
                "aynan shu fakt.</p>"
                + why([
                    (True, "The number of people who speak a language fluently can fall to zero",
                     "ikkala matn ham buni ochiq aytadi. Ular <u>keyin nima "
                     "bo'lishi</u>da ajraladi, faktda emas."),
                    (False, "A language that has lost its last fluent speaker can always be brought back",
                     "<strong>haddan tashqari kuchli</strong>: <em>always</em>. "
                     "Text 2 ham bunday demaydi — u bir necha jamoani keltiradi va "
                     "hatto natija bir xil til ekaniga shubha qoldiradi."),
                    (False, "Counting fluent speakers is the best available measure of a language's survival",
                     "aynan shu Text 2 ning e'tirozi (<em>Counting fluent speakers "
                     "misses…</em>). Kesishma emas, ajralish nuqtasi."),
                    (False, "Most of the world's languages will still be spoken in a century's time",
                     "Text 1 ning bashoratiga zid, va Text 2 ham bunday keng "
                     "da'voni ko'tarmaydi."),
                ])
            ),
        },

        {
            "rich_text": cross_q(
                "<p>Public monuments should be left standing whatever their subject. A "
                "city that removes them loses the record of what it once honoured, and a "
                "generation that never sees the statue never has to reckon with the fact "
                "that it was put up.</p>",
                "<p>Nothing about a plinth in the main square records that a debate ever "
                "took place. The statues that have been moved to museums are seen by more "
                "people now than when they stood outdoors, and each is displayed beside "
                "the argument that moved it. Leaving one in place preserves the object "
                "and loses the history.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the concern raised in Text 1 about losing the record?"),
            "choices": [
                {"text": "By arguing that a statue left in place records less of the relevant history than a relocated one does.", "is_correct": True},
                {"text": "By agreeing that removing monuments destroys the historical record and accepting that cost.", "is_correct": False},
                {"text": "By pointing out that most monuments are of little artistic value.", "is_correct": False},
                {"text": "By suggesting that new monuments should be built beside the old ones.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Tegish nuqtasi:</strong> Text 1 ning tashvishi — "
                "<em>loses the record</em>. Text 2 aynan shu so'zni oladi va uni "
                "<mark>teskari buradi</mark>: oxirgi jumla — <em>Leaving one in place "
                "preserves the object and loses the history.</em></p>"
                "<p>Bu munosabatning nozik turi: Text 2 Text 1 ning <u>o'z "
                "mezoni</u>ni qabul qiladi va o'sha mezon bo'yicha Text 1 "
                "yutqazayotganini ko'rsatadi.</p>"
                + why([
                    (True, "By arguing that a statue left in place records less of the relevant history than a relocated one does",
                     "oxirgi jumlaning aynan mazmuni, va muzey misoli "
                     "(<em>displayed beside the argument that moved it</em>) uning "
                     "dalili."),
                    (False, "By agreeing that removing monuments destroys the historical record and accepting that cost",
                     "Text 2 bu zararni <u>tan olmaydi</u> — u yozuvning aksincha "
                     "ko'chirishda <u>saqlanishini</u> aytadi. Yon berish "
                     "sifatida o'qish matnni butunlay teskari qiladi."),
                    (False, "By pointing out that most monuments are of little artistic value",
                     "badiiy qiymat birorta matnda muhokama qilinmaydi. "
                     "<strong>Tashqi bilim.</strong>"),
                    (False, "By suggesting that new monuments should be built beside the old ones",
                     "Text 2 yangi haykal qurishni taklif qilmaydi — u mavjudlarini "
                     "ko'chirish haqida gapiryapti. <strong>O'quvchi o'zi "
                     "to'qiydigan uchinchi yo'l.</strong>"),
                ])
            ),
        },

        {
            "rich_text": cross_q(
                "<p>Wind turbines are often opposed on the ground that they kill birds. "
                "The figures are real, and a badly sited array on a migration route can "
                "kill a great many.</p>",
                "<p>Siting is the whole of the matter. Where arrays have been placed off "
                "migration corridors and fitted with detection systems that stop the "
                "blades when a large bird approaches, recorded deaths fall to a small "
                "fraction of the original figures. The objection is to particular "
                "turbines in particular places.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the objection described in Text 1?"),
            "choices": [
                {"text": "By arguing that the harm depends on where and how a turbine is installed rather than on turbines as such.", "is_correct": True},
                {"text": "By denying that wind turbines have ever killed a significant number of birds.", "is_correct": False},
                {"text": "By conceding that the objection applies to wind power in general and cannot be answered.", "is_correct": False},
                {"text": "By arguing that bird deaths matter less than the benefits of reducing emissions.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Munosabat:</strong> 5-tur — <u>umumlashmaydi</u>. Text 2 "
                "raqamlarni inkor qilmaydi (Text 1 ham <em>The figures are real</em> "
                "deydi); u e'tirozning <mark>doirasi</mark>ni toraytiradi: "
                "<em>The objection is to particular turbines in particular "
                "places.</em></p>"
                + why([
                    (True, "By arguing that the harm depends on where and how a turbine is installed rather than on turbines as such",
                     "<em>Siting is the whole of the matter</em> va oxirgi jumla — "
                     "ikkalasi ham aynan shu doirani toraytirish harakati."),
                    (False, "By denying that wind turbines have ever killed a significant number of birds",
                     "<strong>haddan tashqari kuchli</strong> va ikkala matnga ham "
                     "zid: Text 2 o'lim sonining <u>kamayishi</u>dan gapiradi, "
                     "ya'ni u nolga tushmagan."),
                    (False, "By conceding that the objection applies to wind power in general and cannot be answered",
                     "aynan teskari — Text 2 ning butun mazmuni e'tirozga "
                     "javob berish."),
                    (False, "By arguing that bird deaths matter less than the benefits of reducing emissions",
                     "<strong>eng jozibali tuzoq</strong>, chunki bu haqiqiy "
                     "bahsda tez-tez aytiladi. Lekin Text 2 bunday taroziga "
                     "umuman kirmaydi — emissiya birorta matnda eslatilmaydi. "
                     "<strong>Tashqi bilim.</strong>"),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Xatoni turi bo'yicha tahlil qiling</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Xato turi</th><th>Nima qilish kerak</th></tr></thead>"
              "<tbody>"
              "<tr><td>Cheklashni to'liq inkor deb o'qidim</td>"
              "<td>32-dars, kuch darajasi jadvali. <em>smaller</em> ≠ <em>no "
              "effect</em>.</td></tr>"
              "<tr><td>Text 1 ning fikrini Text 2 ga yopishtirdim</td>"
              "<td>32-dars. Kim gapiryapti?</td></tr>"
              "<tr><td>Yo'nalishni teskari o'qidim</td>"
              "<td>32-dars. Savolda «kim» va «nimaga» ni belgilang.</td></tr>"
              "<tr><td>Rost, lekin savol so'ragan farq emas</td>"
              "<td>31-dars. Tegish nuqtasini toping.</td></tr>"
              "<tr><td>Matnda yo'q muqobil yechimni o'zim to'qidim</td>"
              "<td>31-dars. Text 2 xulosani buzsa, muqobil taklif qilishi shart "
              "emas.</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Oltitadan 4–5 tasi to'g'ri bo'lsa — yaxshi daraja. Uchtadan kam "
                "bo'lsa, xatolaringizni jadval bo'yicha ajrating: bu turda ular "
                "deyarli har doim <u>bitta</u> qatorga yig'iladi.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to rule out</div><div class="pp-card-back">istisno qilmoq, chetga chiqarmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an addressee</div><div class="pp-card-back">murojaat qilinayotgan kishi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">siting</div><div class="pp-card-back">joylashtirish, o\'rin tanlash</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to reckon with ~</div><div class="pp-card-back">~ bilan hisoblashmoq, yuzlashmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a plinth</div><div class="pp-card-back">haykal poydevori</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">as such</div><div class="pp-card-back">o\'z-o\'zicha, umuman olganda</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to withdraw behind ~</div><div class="pp-card-back">~ ortiga chekinmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">on current rates</div><div class="pp-card-back">hozirgi sur\'atlarda</div></div>'
            + "</div>"
            + "<h3>Xulosa — Cross-Text Connections mavzusi yakuni</h3>"
            + "<ul>"
              "<li>Har matnni <strong>bitta jumlaga siqing</strong>, keyin "
              "munosabatni oltitadan biri deb nomlang (30-dars).</li>"
              "<li>Ikki matn <strong>bitta nuqtada</strong> tegadi — qolgani fon "
              "(31-dars).</li>"
              "<li>Javobni matn muallifi beradi, siz emas; fe'lning kuchiga qarang "
              "(32-dars).</li>"
              "<li>Eng ko'p xato: <u>cheklash</u> ni <u>inkor</u> deb o'qish.</li>"
              "<li>Ikkinchi eng ko'p xato: yo'nalishni teskari o'qish.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 40
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CID,
    "title": "SAT R&W 40: Main Idea Is What the Text Argues, Not What It Mentions",
    "summary": "Asosiy fikr — matnning da'vosi, mavzusi emas; da'vo jumlasini topish "
               "va uni o'z so'zingiz bilan aytish usuli.",
    "order": 40,
    "blocks": [
        {"rich_text": (
            "<h2>Mavzu emas — da'vo</h2>"
            "<p><em>Information and Ideas</em> domeniga o'tdik: bu domen matnning "
            "<u>mazmuni</u> haqida so'raydi (~26%, 12–14 savol). Uning birinchi "
            "turi — <strong>Central Ideas and Details</strong>.</p>"
            "<p>Savol shakli: <em>Which choice best states the main idea of the "
            "text?</em></p>"
            "<p>Bu turdagi eng katta xato juda oddiy: o'quvchi <mark>mavzuni</mark> "
            "javob deb oladi. «Bu matn termitlar haqida» — bu mavzu. Asosiy fikr esa "
            "matn termitlar haqida <u>nima da'vo qilyapti</u>.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><strong>Mavzu:</strong> shahar tulkilari.<br>"
                "<strong>Asosiy fikr:</strong> shahar tulkilarining jasurligi "
                "avlodlar saralashidan emas, bitta hayot davomidagi o'rganishdan "
                "kelib chiqishi mumkin.</p>"
                "<p style=\"margin:8px 0 0;\">Birinchisi — mavzu, ikkinchisi — "
                "<u>da'vo</u>. SAT har doim ikkinchisini so'raydi.</p>")
            + '<span class="sr-time">⏱ ~55 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Da'vo jumlasini toping</h3>"
            "<p>SAT parchasi qisqa, shuning uchun unda deyarli har doim bitta "
            "<strong>da'vo jumlasi</strong> bor — qolgan jumlalar uni tayyorlaydi "
            "yoki ko'taradi. Uni topishning uch belgisi:</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Burilishdan keyin turadi.</strong> "
              "<em>but · however · in fact · what the studies did not record</em> — "
              "burilishdan keyingi jumla deyarli har doim da'vo.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Baho yoki xulosa "
              "beradi.</strong> Fakt jumlalari o'lchov va sana beradi; da'vo jumlasi "
              "<em>therefore · suggests · the reason is · what matters is</em> "
              "kabi so'zlar bilan keladi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Qolgan jumlalar unga "
              "xizmat qiladi.</strong> Sinov oddiy: har jumla uchun «bu nima uchun "
              "shu yerda?» deb so'rang. Javob «falon jumlani "
              "ko'tarish uchun» bo'lsa — o'sha «falon» da'vo.</p></div>"
            + '</div>'
            + TIP.format(
                "Da'vo jumlasi <u>oxirgi jumla</u> bo'lish ehtimoli boshqa har qanday "
                "o'rindan yuqori. SAT parchalari dalilni oldin qo'yib, xulosani "
                "oxirida aytishni yaxshi ko'radi. Vaqtingiz kam bo'lsa — "
                "oxirgi jumladan boshlang.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + q(
                "<p>Antibiotic resistance is usually pictured as a bacterium acquiring a "
                "new ability. In most cases the ability was already there. Genes that "
                "break down antibiotic molecules have been recovered from permafrost "
                "sediments thirty thousand years old, long before any clinic existed. "
                "What modern use of antibiotics has done is not create these genes but "
                "make the bacteria carrying them the ones that survive.</p>",
                "Which choice best states the main idea of the text?")
            + choices_html([
                "Antibiotic resistance genes have been found in very old permafrost "
                "sediments.",
                "Antibiotic use has not produced resistance genes but has made them "
                "widespread by favouring the bacteria that carry them.",
                "Bacteria acquire new abilities more quickly than was once believed.",
                "Clinics should reduce the quantity of antibiotics that they prescribe.",
            ])
            + '<span class="sr-time">⏱ ~55 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>Har jumla nima uchun shu yerda?</strong></p>"
            "<ul>"
            "<li><em>Antibiotic resistance is usually pictured…</em> — keng tarqalgan "
            "tasavvur (tayyorgarlik).</li>"
            "<li><em>In most cases the ability was already there.</em> — burilish.</li>"
            "<li><em>Genes … thirty thousand years old…</em> — dalil.</li>"
            "<li><em>What modern use of antibiotics has done is not create these genes "
            "but make the bacteria carrying them the ones that survive.</em> — "
            "<mark>da'vo</mark>.</li>"
            "</ul>"
            "<p>Oxirgi jumla uchta belgini ham qanoatlantiradi: burilishdan keyin, "
            "<em>not … but …</em> qurilishi bilan xulosa beradi, va qolgan jumlalar "
            "unga xizmat qiladi.</p>"
            + why([
                (True, "Antibiotic use has not produced resistance genes but has made them widespread by favouring the bacteria that carry them",
                 "oxirgi jumlaning aynan qayta ifodasi, va matnning butun tuzilishini "
                 "(tasavvur → burilish → dalil → xulosa) qamrab oladi."),
                (False, "Antibiotic resistance genes have been found in very old permafrost sediments",
                 "<strong>doirasi juda tor</strong>: bu bitta <u>dalil</u>. Dalil rost, "
                 "lekin u nima uchun keltirilganini aytmaydi. Bir jumlani javob deb "
                 "olish — bu turdagi eng ko'p uchraydigan xato."),
                (False, "Bacteria acquire new abilities more quickly than was once believed",
                 "<strong>teskari</strong>: matn bakteriyalar yangi qobiliyat "
                 "<u>orttirmaganini</u> aytadi — u allaqachon mavjud edi. Tezlik "
                 "haqida esa bir og'iz ham yo'q."),
                (False, "Clinics should reduce the quantity of antibiotics that they prescribe",
                 "matn hech narsa tavsiya qilmaydi. Bu <u>oqilona</u> xulosa bo'lishi "
                 "mumkin, lekin oqilonalik yetarli emas: <strong>matnda yo'q "
                 "tavsiya</strong>."),
            ])
            + WARN.format(
                "Uchala noto'g'ri variant ham matnga <u>yaqin</u> edi: biri rost dalil, "
                "biri teskari, biri mantiqiy davomi. Bu turda «umuman aloqasiz» "
                "variantlar deyarli bo'lmaydi — shuning uchun "
                "<strong>da'vo jumlasini topish</strong> yagona ishonchli yo'l.")
        )},

        {
            "rich_text": q(
                "<p>Public transport maps are drawn to be legible rather than accurate. "
                "Distances are stretched where stations crowd together and squeezed where "
                "they are far apart, and lines are bent to run at neat angles. A "
                "passenger reading such a map cannot tell how far apart two stations are, "
                "and does not need to. What the map is for is deciding where to "
                "change.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "Transport maps distort geography because their purpose is to guide decisions rather than to represent distance.", "is_correct": True},
                {"text": "Transport maps bend their lines so that they run at neat angles.", "is_correct": False},
                {"text": "Passengers are frequently misled about distances by transport maps.", "is_correct": False},
                {"text": "Transport authorities should publish accurate maps alongside simplified ones.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo jumlasi:</strong> oxirgisi — <em>What the map is for "
                "is deciding where to change.</em> Qolgan hamma narsa (cho'zilgan "
                "masofalar, tekis burchaklar) unga <u>dalil</u>.</p>"
                "<p>Va birinchi jumla ikkinchi yarmini beradi: "
                "<em>legible rather than accurate</em>. Ikkovi birga: "
                "<mark>xarita geografiyani buzadi, chunki uning maqsadi boshqa</mark>.</p>"
                + why([
                    (True, "Transport maps distort geography because their purpose is to guide decisions rather than to represent distance",
                     "ikki qismli javob: buzish (dalillar) + sabab (maqsad). Matnning "
                     "birinchi va oxirgi jumlasini birga qamraydi."),
                    (False, "Transport maps bend their lines so that they run at neat angles",
                     "<strong>doirasi juda tor</strong> — bu bitta dalil, va u nima "
                     "uchun keltirilganini aytmaydi."),
                    (False, "Passengers are frequently misled about distances by transport maps",
                     "matn buni <strong>ataylab rad etadi</strong>: <em>and does not "
                     "need to</em>. Yo'lovchi aldanmayapti — unga o'sha ma'lumot "
                     "kerak emas."),
                    (False, "Transport authorities should publish accurate maps alongside simplified ones",
                     "yana <strong>matnda yo'q tavsiya</strong>. Matn tushuntiryapti, "
                     "talab qilmayapti."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>A choir singing in a stone church sounds fuller than the same choir "
                "outdoors, and singers describe the building as helping them. It does not "
                "help them make a better sound; it holds each note in the air for a "
                "second or two, so that the beginning of one phrase overlaps the end of "
                "the last. Buildings of this kind were not designed to flatter voices. "
                "Voices learned to use them.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "The fuller sound comes from the building's acoustics rather than from any improvement in the singing, and singing adapted to it.", "is_correct": True},
                {"text": "Stone churches were designed by their builders to make choirs sound better.", "is_correct": False},
                {"text": "A choir singing outdoors produces a thinner sound than one singing indoors.", "is_correct": False},
                {"text": "Singers are generally poor judges of how their own performances sound.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo jumlasi:</strong> oxirgi ikkitasi birga — "
                "<em>Buildings of this kind were not designed to flatter voices. Voices "
                "learned to use them.</em> Ikki qisqa jumla, va ikkinchisi butun "
                "matnning burilishi.</p>"
                + why([
                    (True, "The fuller sound comes from the building's acoustics rather than from any improvement in the singing, and singing adapted to it",
                     "ikkala qismni ham qamraydi: mexanizm (<em>holds each note … "
                     "overlaps</em>) va yo'nalish (<em>Voices learned to use "
                     "them</em>)."),
                    (False, "Stone churches were designed by their builders to make choirs sound better",
                     "matn buni <u>so'zma-so'z</u> rad etadi: <em>were not designed to "
                     "flatter voices</em>. <strong>Teskari</strong> — va aynan shu "
                     "jumladan yozilgan."),
                    (False, "A choir singing outdoors produces a thinner sound than one singing indoors",
                     "<strong>doirasi juda tor</strong>: bu birinchi jumladagi "
                     "kuzatuv, matnning xulosasi emas. Rost, lekin matn undan "
                     "<u>keyin</u> boshlanadi."),
                    (False, "Singers are generally poor judges of how their own performances sound",
                     "<strong>doirasi juda keng</strong> va matnda yo'q. Xonandalar "
                     "bino yordam beryapti deb aytadi — bu noto'g'ri baho emas, "
                     "shunchaki mexanizmni bilmaslik."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Nasreddin's neighbour found him on his knees under the street lamp, "
                "searching the dust. Told that the key had been lost inside the house, "
                "the neighbour asked why he was looking out here. Because in the house, "
                "Nasreddin said, there is no light. The joke has outlived a thousand "
                "cleverer ones because researchers keep doing it: measuring what the "
                "instrument can measure, and writing the conclusion about that.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "An old joke endures because it names a habit researchers still fall into: studying what is easy to measure rather than what matters.", "is_correct": True},
                {"text": "Nasreddin stories remain popular in the regions where they were first told.", "is_correct": False},
                {"text": "Researchers should improve their instruments before drawing conclusions.", "is_correct": False},
                {"text": "The joke is funnier than a thousand other stories about Nasreddin.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu parcha <u>latifa bilan boshlanadi</u>, va shuning uchun xavfli: "
                "o'quvchi latifani mavzu deb o'ylaydi. Lekin da'vo jumlasi oxirgisi: "
                "<em>The joke has outlived a thousand cleverer ones <u>because</u> "
                "researchers keep doing it</em>.</p>"
                "<p><em>because</em> — signal. Latifa <mark>misol</mark>, da'vo esa "
                "tadqiqotchilar haqida.</p>"
                + why([
                    (True, "An old joke endures because it names a habit researchers still fall into: studying what is easy to measure rather than what matters",
                     "latifani misol o'rnida qoldiradi va oxirgi jumladagi haqiqiy "
                     "da'voni oladi."),
                    (False, "Nasreddin stories remain popular in the regions where they were first told",
                     "mintaqalar ham, mashhurlik ham matnda yo'q. "
                     "<strong>Tashqi bilim</strong> — o'zbek o'quvchi Nasriddin "
                     "haqida ko'p narsa biladi va uni matnga qo'shib yuboradi."),
                    (False, "Researchers should improve their instruments before drawing conclusions",
                     "<strong>matnda yo'q tavsiya.</strong> Matn odatni "
                     "<u>nomlaydi</u>, uni tuzatish yo'lini emas."),
                    (False, "The joke is funnier than a thousand other stories about Nasreddin",
                     "<em>a thousand cleverer ones</em> iborasini noto'g'ri o'qish: "
                     "matn boshqalarni <u>aqlliroq</u> deb ataydi va bu latifa ularni "
                     "<u>umri bo'yicha</u> ortda qoldirganini aytadi — kulgililik "
                     "bo'yicha emas."),
                ])
                + TIP.format(
                    "Matn hikoya, latifa yoki bitta odam bilan boshlansa — u deyarli "
                    "har doim <strong>misol</strong>, mavzu emas. Da'vo undan "
                    "keyin keladi, ko'pincha <em>because</em>, <em>and that is "
                    "why</em> yoki <em>the same thing happens</em> bilan.")
            ),
        },

        {
            "rich_text": q(
                "<p>The first cities did not appear where farming was easiest. They "
                "appear along rivers whose floods were violent enough to require "
                "embankments and canals \u2014 work no single household could carry out and "
                "no single household could benefit from alone. Where the land gave a good "
                "crop without anyone having to agree with anyone, villages stayed "
                "villages.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "Cities arose where farming demanded coordinated work, not where the land was most generous.", "is_correct": True},
                {"text": "The earliest cities were built beside rivers whose floods were unusually violent.", "is_correct": False},
                {"text": "Villages that failed to build canals could not grow enough food to survive.", "is_correct": False},
                {"text": "Embankments and canals were the most demanding engineering works of the ancient world.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da\u2019vo jumlasi</strong> \u2014 oxirgisi, va u qarama-qarshi "
                "holatni beradi: hamkorlik kerak bo\u2018lmagan joyda shahar "
                "<u>paydo bo\u2018lmagan</u>. Birinchi jumla bilan birga u aniq bir "
                "da\u2019voni yasaydi: shaharni <mark>qiyinchilik tug\u2018dirgan, "
                "qulaylik emas</mark>.</p>"
                + why([
                    (True, "Cities arose where farming demanded coordinated work, not where the land was most generous",
                     "birinchi va oxirgi jumlani birga oladi \u2014 ikkovi ham bitta "
                     "qarama-qarshilikning ikki uchi."),
                    (False, "The earliest cities were built beside rivers whose floods were unusually violent",
                     "<strong>doirasi tor</strong>: bu bitta tafsilot, va u "
                     "<u>nima uchun</u> muhimligini aytmaydi. Toshqin o\u2018zi emas, "
                     "u talab qilgan birgalikdagi mehnat muhim."),
                    (False, "Villages that failed to build canals could not grow enough food to survive",
                     "<strong>biroz burilgan</strong> va matnga zid: qishloqlar och "
                     "qolgan deyilmagan \u2014 ular <em>stayed villages</em>, ya\u2019ni "
                     "yashab turgan, shunchaki o\u2018smagan."),
                    (False, "Embankments and canals were the most demanding engineering works of the ancient world",
                     "<strong>doirasi keng</strong>: matn qadimgi dunyodagi boshqa "
                     "inshootlar bilan solishtirmaydi. <em>most</em> so\u2018zi deyarli "
                     "har doim ogohlantirish belgisi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">the main idea</div><div class="pp-card-back">asosiy fikr (matnning da\'vosi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to state a claim</div><div class="pp-card-back">da\'voni ifodalamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to favour ~</div><div class="pp-card-back">~ ga ustunlik bermoq, tanlab qoldirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">legible</div><div class="pp-card-back">o\'qish oson, tushunarli</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to distort</div><div class="pp-card-back">buzib ko\'rsatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to flatter (a voice)</div><div class="pp-card-back">(ovozni) chiroyliroq ko\'rsatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to outlive ~</div><div class="pp-card-back">~ dan uzoqroq yashamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to fall into a habit</div><div class="pp-card-back">odatga tushib qolmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Mavzu ≠ asosiy fikr.</strong> Savol da'voni so'raydi.</li>"
              "<li>Da'vo jumlasini toping: burilishdan keyin, xulosa beradi, qolgani "
              "unga xizmat qiladi.</li>"
              "<li>Vaqt kam bo'lsa — <strong>oxirgi jumladan</strong> boshlang.</li>"
              "<li>Hikoya yoki latifa bilan boshlangan matnda u — "
              "<u>misol</u>, mavzu emas.</li>"
              "<li>Doimiy tuzoq: bitta rost <u>dalil</u>ni javob deb olish.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 41
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CID,
    "title": "SAT R&W 41: Too Broad, Too Narrow, Slightly Off — The Three Wrong Main Ideas",
    "summary": "Asosiy fikr savolida noto'g'ri variantlar deyarli har doim uch shakldan "
               "biri: doirasi keng, doirasi tor yoki bir necha so'z bilan burilgan.",
    "order": 41,
    "blocks": [
        {"rich_text": (
            "<h2>Uchta noto'g'ri asosiy fikr</h2>"
            "<p>40-darsda da'vo jumlasini topishni o'rgandik. Endi ikkinchi tomondan "
            "yondashamiz: <mark>noto'g'ri variantlar qanday yasaladi?</mark></p>"
            "<p>Bu turda variantlar juda o'xshash bo'ladi — hammasi matnga tegishli, "
            "hammasi ishonarli eshitiladi. Lekin ular deyarli har doim uch shakldan "
            "biriga tushadi, va shakllarni tanigan o'quvchi ikkitasini bir zumda "
            "o'chiradi.</p>"
            + '<span class="sr-time">⏱ ~50 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Uch shakl</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Shakl</th><th>Qanday bilinadi</th><th>Sinov</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Doirasi keng</strong></td>"
              "<td>Matndan kattaroq da'vo: <em>all · always · most · never · the "
              "most</em>, yoki matn tegmagan sohaga chiqadi</td>"
              "<td>«Matn shuni <u>isbotlaydimi</u>, yoki faqat bir holatni "
              "ko'rsatdimi?»</td></tr>"
              "<tr><td><strong>Doirasi tor</strong></td>"
              "<td>Bitta jumla, bitta dalil, bitta misol — rost, lekin matnning "
              "yarmini tashlab ketadi</td>"
              "<td>«Matnning <u>qolgan jumlalari</u> shu variant uchun kerakmi?»</td></tr>"
              "<tr><td><strong>Biroz burilgan</strong></td>"
              "<td>Bir-ikki so'z o'zgargan: sabab teskari, baho qo'shilgan, "
              "«mumkin» → «albatta»</td>"
              "<td>«Har bir so'z matnda bormi?» — variantni <u>so'zma-so'z</u> "
              "tekshiring</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<strong>Biroz burilgan</strong> — eng qiyini va eng ko'p ball "
                "yeydigani. U to'g'ri javobga 90% o'xshaydi. Uni faqat bitta narsa "
                "ochadi: variantni oxirigacha, <u>har bir so'zini</u> matnga "
                "solishtirib o'qish. Ayniqsa: <em>because</em>, <em>proves</em>, "
                "<em>all</em>, <em>only</em>, <em>should</em>.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + q(
                "<p>A dam built to store water also traps the silt a river carries. "
                "Downstream, the fields that were once renewed by an annual layer of that "
                "silt begin to thin, and farmers make up the difference with fertiliser "
                "bought in sacks. The reservoir, meanwhile, loses a little capacity every "
                "year to the sediment settling in it. One structure has turned a free "
                "annual service into two recurring costs.</p>",
                "Which choice best states the main idea of the text?")
            + choices_html([
                "Dams should not be built on rivers that carry a heavy load of silt.",
                "A dam converts a river's free delivery of silt into ongoing costs both "
                "downstream and in the reservoir itself.",
                "Sediment settling behind a dam gradually reduces the volume of water it "
                "can hold.",
                "Farmers downstream of dams rely more heavily on purchased fertiliser "
                "than other farmers do.",
            ])
            + '<span class="sr-time">⏱ ~50 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim — uch shaklni nomlaymiz</h3>"
            "<p><strong>Da'vo jumlasi</strong> — oxirgisi: <em>One structure has turned "
            "a free annual service into two recurring costs.</em> <em>two</em> so'ziga "
            "e'tibor bering: javob <u>ikkala</u> xarajatni ham qamrashi kerak.</p>"
            + why([
                (True, "A dam converts a river's free delivery of silt into ongoing costs both downstream and in the reservoir itself",
                 "oxirgi jumlaning aynan qayta ifodasi, va <em>both … and …</em> "
                 "bilan ikkala xarajatni ham ushlaydi."),
                (False, "Sediment settling behind a dam gradually reduces the volume of water it can hold",
                 "<strong>doirasi tor</strong>: bu ikki xarajatdan <u>bittasi</u>. "
                 "Sinov: matnning pastki oqim haqidagi ikki jumlasi bu variant uchun "
                 "keraksiz bo'lib qoladi — demak u asosiy fikr emas."),
                (False, "Farmers downstream of dams rely more heavily on purchased fertiliser than other farmers do",
                 "<strong>doirasi tor va biroz burilgan birga</strong>: bu ham bitta "
                 "xarajat, va ustiga matnda yo'q taqqoslash qo'shadi "
                 "(<em>than other farmers do</em>). Matn boshqa dehqonlarni "
                 "eslatmaydi."),
                (False, "Dams should not be built on rivers that carry a heavy load of silt",
                 "<strong>doirasi keng</strong>: matn xarajatlarni sanaydi, lekin "
                 "to'g'onning foydasini (<em>built to store water</em>) tarozidan "
                 "chiqarmaydi. «Qurmaslik kerak» degan hukm matndan kattaroq — bu "
                 "<u>tavsiya</u>, tavsif emas."),
            ])
            + TIP.format(
                "«Ikkala xarajatni ham qamrashi kerak» degan talab qayerdan chiqdi? "
                "Da'vo jumlasidagi bitta so'zdan: <em><u>two</u> recurring costs</em>. "
                "Bu turda <strong>sonlar va <em>both</em> kabi so'zlar</strong> "
                "javobning qanchalik keng bo'lishini aytib turadi — ularni "
                "o'qing.")
        )},

        {
            "rich_text": q(
                "<p>Volunteer river-monitoring schemes were set up to gather data that "
                "professional agencies could not afford to collect. They do gather it, "
                "and the readings hold up well against laboratory checks. But the effect "
                "that has changed policy in several districts is a different one: a "
                "council that receives a monthly report signed by two hundred residents "
                "responds to it differently from one that receives the same numbers from "
                "a contractor.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "The schemes' most consequential effect has been political rather than the data collection they were created for.", "is_correct": True},
                {"text": "Volunteer river monitoring produces readings as reliable as those from professional laboratories.", "is_correct": False},
                {"text": "Councils are more responsive to reports from residents than to reports from contractors.", "is_correct": False},
                {"text": "Professional agencies should be given the funding they need to collect river data themselves.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Burilish:</strong> <em>But the effect that has changed "
                "policy … is a different one</em>. Da'vo shundan keyin.</p>"
                + why([
                    (True, "The schemes' most consequential effect has been political rather than the data collection they were created for",
                     "burilishni ham, undan keyingi izohni ham qamraydi: dastur "
                     "ma'lumot uchun tuzilgan, lekin haqiqiy ta'siri boshqa "
                     "joyda."),
                    (False, "Volunteer river monitoring produces readings as reliable as those from professional laboratories",
                     "<strong>doirasi tor</strong>: bu <em>But</em> dan "
                     "<u>oldingi</u> qism. Matn aynan shu yerdan burilib ketadi, "
                     "demak bu tayyorgarlik, xulosa emas."),
                    (False, "Councils are more responsive to reports from residents than to reports from contractors",
                     "<strong>biroz burilgan</strong> — va juda nozik. Matn "
                     "<em>responds to it <u>differently</u></em> deydi, "
                     "«ko'proq javob beradi» demaydi. Bir so'z: "
                     "<em>differently</em> → <em>more responsive</em>. Bundan "
                     "tashqari bu ham faqat izoh, da'voning o'zi emas."),
                    (False, "Professional agencies should be given the funding they need to collect river data themselves",
                     "<strong>matnda yo'q tavsiya</strong> va doirasi keng: "
                     "moliyalash masalasi faqat birinchi jumlaning foni."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>A city counted its cyclists at nine in the morning on a Tuesday in "
                "October and found few. The count was repeated for a year and the annual "
                "figure came in low, which was taken to mean that a cycle lane could not "
                "be justified. The counts were made at junctions the existing network "
                "does not reach; the streets where people already cycle were not among "
                "them.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "A count taken in the wrong places produced a figure that could not support the conclusion drawn from it.", "is_correct": True},
                {"text": "Cycling levels in the city are lower in October than at other times of year.", "is_correct": False},
                {"text": "The city should build a cycle lane despite the low counts it recorded.", "is_correct": False},
                {"text": "Annual counts are always more reliable than counts made on a single day.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo jumlasi</strong> — oxirgisi, va u sanoqning "
                "<u>joyi</u> haqida: <em>The counts were made at junctions the existing "
                "network does not reach.</em></p>"
                + why([
                    (True, "A count taken in the wrong places produced a figure that could not support the conclusion drawn from it",
                     "matnning uchala qismini bog'laydi: sanoq → xulosa → sanoqning "
                     "nuqsoni."),
                    (False, "Cycling levels in the city are lower in October than at other times of year",
                     "<strong>doirasi tor va matnda yo'q</strong>: oktyabr faqat "
                     "birinchi sanoqning sanasi. Matn fasllarni solishtirmaydi — "
                     "aksincha, sanoq bir yil davomida takrorlangan."),
                    (False, "The city should build a cycle lane despite the low counts it recorded",
                     "<strong>matnda yo'q tavsiya.</strong> Matn sanoq yaroqsiz "
                     "deydi — bu «yo'lak qurish kerak» degani emas. Yaroqsiz dalil "
                     "hech qanday tomonni isbotlamaydi."),
                    (False, "Annual counts are always more reliable than counts made on a single day",
                     "<strong>doirasi keng</strong> (<em>always</em>) va matnga zid: "
                     "bu yerda yillik sanoq ham xato chiqdi, chunki muammo "
                     "<u>joyda</u> edi, muddatda emas."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Zamira had taught the same course for eleven years and had never "
                "been asked the question the boy in the third row asked her that "
                "morning. She answered it badly, went home, and read for four hours. What "
                "she thought about on the way to work the next day was not the answer she "
                "had found but how close she had come to teaching the course a twelfth "
                "time without noticing what she did not know.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "An unexpected question shows Zamira how easily long familiarity had hidden a gap in her understanding.", "is_correct": True},
                {"text": "Zamira is embarrassed at having answered a student's question badly.", "is_correct": False},
                {"text": "Zamira decides to change the way she has been teaching her course.", "is_correct": False},
                {"text": "Experienced teachers are usually less well prepared than they believe themselves to be.", "is_correct": False},
            ],
            "explanation": (
                "<p>Adabiy parcha, lekin usul o'zgarmaydi. <strong>Da'vo jumlasi</strong> "
                "— oxirgisi, va u <em>not … but …</em> qurilishi bilan keladi: "
                "Zamira javob haqida emas, <mark>bilmasligini sezmay qolishga "
                "qanchalik yaqin kelgani</mark> haqida o'ylayapti.</p>"
                + why([
                    (True, "An unexpected question shows Zamira how easily long familiarity had hidden a gap in her understanding",
                     "oxirgi jumlaning aynan mazmuni, va <em>eleven years</em> bilan "
                     "<em>a twelfth time</em> juftligi «uzoq tanishlik» qismini "
                     "ko'taradi."),
                    (False, "Zamira is embarrassed at having answered a student's question badly",
                     "<strong>doirasi tor va biroz burilgan</strong>: yomon javob "
                     "matnda bor, lekin oxirgi jumla uni <u>ataylab chetga suradi</u> "
                     "(<em>not the answer she had found but…</em>). Uyalish esa "
                     "matnda umuman aytilmagan."),
                    (False, "Zamira decides to change the way she has been teaching her course",
                     "hech qanday qaror yo'q — u to'rt soat o'qidi va o'ylanib "
                     "ketyapti. <strong>O'quvchi qo'shib yuboradigan davomi.</strong>"),
                    (False, "Experienced teachers are usually less well prepared than they believe themselves to be",
                     "<strong>doirasi juda keng</strong>: <em>usually</em> va "
                     "«tajribali o'qituvchilar» umuman. Matn bitta odamning bitta "
                     "ertalabi haqida."),
                ])
                + NOTE.format(
                    "Adabiy parchada «doirasi keng» tuzog'i deyarli har doim shu "
                    "shaklda keladi: bitta personajning bitta lahzasidan "
                    "<u>odamlar umuman</u> haqidagi hukm yasaladi. "
                    "Hikoya bitta odam haqida — javob ham shunday bo'lsin.")
            ),
        },

        {
            "rich_text": q(
                "<p>A hospital that began publishing the mortality rates of its "
                "individual surgeons watched those rates fall over the following two "
                "years. It also watched referrals of the most severely ill patients drop "
                "by about a third; those cases went to other hospitals, or were not "
                "referred at all. The published figure improved, and the thing the figure "
                "was meant to track did not.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "Publishing individual rates improved the measure while leaving what it was meant to measure no better.", "is_correct": True},
                {"text": "Surgeons at the hospital became more skilful in the two years after the policy began.", "is_correct": False},
                {"text": "Referrals of the most severely ill patients fell by roughly a third.", "is_correct": False},
                {"text": "Hospitals should not publish the mortality rates of individual surgeons.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da\u2019vo jumlasi</strong> \u2014 oxirgisi, va u ikki qismli: "
                "<em>The published figure improved</em> <u>va</u> <em>the thing the "
                "figure was meant to track did not</em>. Javob ikkovini ham "
                "olishi kerak.</p>"
                + why([
                    (True, "Publishing individual rates improved the measure while leaving what it was meant to measure no better",
                     "oxirgi jumlaning ikkala yarmini ham qamraydi \u2014 bu turdagi "
                     "\u00abikki qismli da\u2019vo\u00bb ning klassik shakli."),
                    (False, "Referrals of the most severely ill patients fell by roughly a third",
                     "<strong>doirasi tor</strong>: bu mexanizmning bir bo\u2018lagi. "
                     "Sinov: matnning birinchi va oxirgi jumlasi bu variant uchun "
                     "keraksiz bo\u2018lib qoladi."),
                    (False, "Surgeons at the hospital became more skilful in the two years after the policy began",
                     "<strong>biroz burilgan</strong> va bu darsning eng nozik "
                     "tuzog\u2018i: ko\u2018rsatkich tushdi, lekin matn buni "
                     "mahoratga <u>bog\u2018lamaydi</u> \u2014 aksincha, u sababni "
                     "og\u2018ir bemorlarning kamayishida ko\u2018rsatadi."),
                    (False, "Hospitals should not publish the mortality rates of individual surgeons",
                     "<strong>matnda yo\u2018q tavsiya.</strong> Matn nima "
                     "bo\u2018lganini aytadi; siyosat to\u2018g\u2018ri yoki noto\u2018g\u2018ri "
                     "ekaniga hukm chiqarmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">too broad / too narrow</div><div class="pp-card-back">doirasi juda keng / juda tor</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">recurring costs</div><div class="pp-card-back">takrorlanuvchi xarajatlar</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to hold up against ~</div><div class="pp-card-back">~ ga solishtirganda ishonchli chiqmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">consequential</div><div class="pp-card-back">oqibati katta, muhim</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to justify ~</div><div class="pp-card-back">~ ni asoslamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">familiarity</div><div class="pp-card-back">tanishlik, o\'rganib qolganlik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a gap in one\'s understanding</div><div class="pp-card-back">bilimdagi bo\'shliq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to make up the difference</div><div class="pp-card-back">yetishmaganini qoplamoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Uch shakl: <strong>doirasi keng · doirasi tor · biroz "
              "burilgan</strong>.</li>"
              "<li><u>Tor</u> sinovi: matnning qolgan jumlalari bu variant uchun "
              "kerakmi?</li>"
              "<li><u>Keng</u> sinovi: matn buni isbotladimi, yoki bir holatni "
              "ko'rsatdimi?</li>"
              "<li><u>Burilgan</u> sinovi: har bir so'z matnda bormi? "
              "(<em>because · all · only · should · more</em>)</li>"
              "<li>Da'vo jumlasidagi <strong>son va <em>both</em></strong> javobning "
              "kengligini aytadi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 42
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CID,
    "title": "SAT R&W 42: Detail Questions — Answering From the Line, Not From Memory",
    "summary": "Tafsilot savolida javob matnning aniq bir joyida turadi; xotiradan "
               "javob berish va «umumiy ma'no»ga tayanish — ikkita doimiy xato.",
    "order": 42,
    "blocks": [
        {"rich_text": (
            "<h2>Barmoq bilan ko'rsating</h2>"
            "<p><strong>Central Ideas and Details</strong> turining ikkinchi yarmi — "
            "<u>tafsilot</u> savollari. Ular shunday keladi:</p>"
            "<p><em>According to the text, what is true about …?</em> · "
            "<em>Based on the text, what did the researchers observe …?</em> · "
            "<em>The text most strongly suggests that …</em></p>"
            "<p>Bu savollar oson ko'rinadi va aynan shuning uchun ball yeydi. "
            "O'quvchi matnni o'qib bo'ladi, savolni ko'radi va "
            "<mark>eslab qolganidan javob beradi</mark> — matnga qaytmasdan.</p>"
            "<p>60 so'zlik matnni eslab qolish oson tuyuladi. Aslida siz uning "
            "<u>ma'nosini</u> eslaysiz, <u>so'zlarini</u> emas. Savol esa ko'pincha "
            "aynan so'zlar haqida.</p>"
            + '<span class="sr-time">⏱ ~40 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Usul</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Savoldan kalit so'zni oling.</strong> "
              "Savol qaysi narsa haqida so'rayapti? O'sha so'zni (yoki uning "
              "sinonimini) matndan qidiring.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. O'sha joyni topib, "
              "<u>butun jumlani</u> o'qing.</strong> Yarim jumla yetmaydi: SAT "
              "javobni ko'pincha jumlaning ikkinchi yarmiga yashiradi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Javobni o'sha jumladan "
              "ayting.</strong> Xotiradan emas, ekrandan.</p></div>"
            + "<div class=\"pp-step\"><p><strong>4. Har variant uchun isbot "
              "so'rang.</strong> «Buni matnning qaysi so'zlari aytadi?» "
              "Ko'rsatolmasangiz — bu javob emas.</p></div>"
            + '</div>'
            + TIP.format(
                "<em>The text most strongly suggests</em> shakli sizni chalg'itmasin. "
                "<em>Suggests</em> «taxmin qiling» degani emas — u «matn buni "
                "to'g'ridan-to'g'ri aytmaydi, lekin <u>albatta nazarda tutadi</u>» "
                "degani. Isbot baribir ekranda bo'lishi shart.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + q(
                "<p>The seeds of the Kazakh apple, the wild ancestor of every orchard "
                "variety, do not breed true: plant a pip from a sweet fruit and the tree "
                "that grows will usually bear a sour one. Growers therefore graft, "
                "fixing a cutting from a known tree onto a rootstock. A named variety in "
                "an orchard is not a population of related trees but one tree, copied, "
                "sometimes for centuries.</p>",
                "According to the text, why do growers graft rather than plant seeds?")
            + choices_html([
                "Because grafted trees produce fruit earlier in their lives than trees "
                "grown from seed.",
                "Because a tree grown from a seed will usually not have the qualities of "
                "the tree the seed came from.",
                "Because the wild Kazakh apple is now too rare to be grown from seed.",
                "Because rootstocks are more resistant to disease than seedlings are.",
            ])
            + '<span class="sr-time">⏱ ~40 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>1-qadam — kalit so'z:</strong> <em>graft</em>. Matndan "
            "topamiz: <em>Growers <u>therefore</u> graft…</em></p>"
            "<p><strong>2-qadam — <em>therefore</em> signal!</strong> Sabab undan "
            "oldin turibdi, ya'ni birinchi jumlada: <em>do not breed true: plant a pip "
            "from a sweet fruit and the tree that grows will usually bear a sour "
            "one</em>.</p>"
            "<p><strong>3-qadam — javob o'sha jumladan:</strong> urug'dan o'sgan daraxt "
            "ona daraxtga o'xshamaydi.</p>"
            + why([
                (True, "Because a tree grown from a seed will usually not have the qualities of the tree the seed came from",
                 "<em>do not breed true</em> iborasining ma'nosi, va ikki nuqtadan "
                 "keyingi izoh (shirin → nordon) uning isboti."),
                (False, "Because grafted trees produce fruit earlier in their lives than trees grown from seed",
                 "<strong>tashqi bilim</strong> — bog'dorchilikda bu rost, va shuning "
                 "uchun tuzoq kuchli. Lekin matn hosil vaqtini umuman "
                 "eslatmaydi."),
                (False, "Because the wild Kazakh apple is now too rare to be grown from seed",
                 "kamyoblik matnda yo'q. <strong>So'z-tuzoq</strong>: "
                 "<em>wild ancestor</em> iborasi «yo'qolib borayotgan tur» "
                 "assotsiatsiyasini uyg'otadi."),
                (False, "Because rootstocks are more resistant to disease than seedlings are",
                 "<em>rootstock</em> so'zi matnda <u>bor</u>, va bu variantni juda "
                 "ishonarli qiladi. Lekin matn uni faqat payvand qanday qilinishini "
                 "tushuntirishda ishlatadi — kasallikka chidamlilik haqida bir og'iz "
                 "ham yo'q. <strong>Matndagi so'z ≠ matndagi da'vo.</strong>"),
            ])
            + WARN.format(
                "Oxirgi ikki variantga e'tibor bering: ikkalasi ham matndagi "
                "<u>haqiqiy so'zlarni</u> ishlatadi (<em>wild</em>, "
                "<em>rootstock</em>). Bu tafsilot savollarining asosiy hiylasi — "
                "tanish so'z ko'rgan o'quvchi variantni tekshirmay tanlaydi. "
                "<strong>So'z bor bo'lishi yetarli emas; da'vo bor bo'lishi "
                "kerak.</strong>")
        )},

        {
            "rich_text": q(
                "<p>Emperor penguins huddle through the Antarctic winter in a mass that "
                "moves. Birds on the windward edge shuffle along the outside toward the "
                "sheltered side, and the whole huddle travels slowly across the ice as "
                "they do. Thermal images show that no individual stays on the cold edge "
                "for long, though none of the birds appears to be organising the "
                "rotation.</p>",
                "According to the text, what does thermal imaging reveal about the "
                "huddle?"),
            "choices": [
                {"text": "No individual bird remains on the exposed edge for an extended period.", "is_correct": True},
                {"text": "The birds on the windward edge are colder than those at the centre.", "is_correct": False},
                {"text": "One bird in each huddle directs the movement of the others.", "is_correct": False},
                {"text": "The huddle stops moving once the wind drops.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kalit so'z:</strong> <em>thermal images</em>. Uni matndan "
                "topamiz — oxirgi jumla. Endi <u>butun jumlani</u> o'qiymiz, "
                "jumladan <em>though</em> dan keyingi qismini.</p>"
                "<p><em>Thermal images show that no individual stays on the cold edge "
                "for long</em> — javob shu yerda, so'zma-so'z.</p>"
                + why([
                    (True, "No individual bird remains on the exposed edge for an extended period",
                     "matnning aynan o'sha jumlasi, boshqa so'zlar bilan: "
                     "<em>no individual stays on the cold edge for long</em>."),
                    (False, "The birds on the windward edge are colder than those at the centre",
                     "mantiqan rost tuyuladi va issiqlik tasviri haqidagi savol buni "
                     "kuchaytiradi. Lekin matn bunday taqqoslashni "
                     "<u>keltirmaydi</u> — u faqat hech kim uzoq turmasligini "
                     "aytadi. <strong>Xotiradan javob berish</strong> aynan shu "
                     "yerda yiqitadi."),
                    (False, "One bird in each huddle directs the movement of the others",
                     "matn buni <strong>so'zma-so'z rad etadi</strong>: <em>none of "
                     "the birds appears to be organising the rotation</em>. "
                     "<em>though</em> dan keyingi qismni o'qimagan o'quvchi buni "
                     "ko'rmaydi."),
                    (False, "The huddle stops moving once the wind drops",
                     "shamolning to'xtashi matnda umuman yo'q."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>The 1919 eclipse expedition is remembered for confirming that light "
                "bends near a massive body. Two teams were sent, to Brazil and to an "
                "island off West Africa, in case one was clouded out. The African plates "
                "were the poorer of the two and were nearly discarded; the Brazilian "
                "instrument had shifted in the heat, and its main set of plates gave a "
                "figure that fitted neither prediction. The result that was announced "
                "rested on the smaller, better set from each site.</p>",
                "Based on the text, what was true of the Brazilian team's main set of "
                "plates?"),
            "choices": [
                {"text": "They produced a measurement that matched neither of the predictions being tested.", "is_correct": True},
                {"text": "They were discarded before the expedition returned home.", "is_correct": False},
                {"text": "They were the clearest images obtained by either of the two teams.", "is_correct": False},
                {"text": "They were ruined by cloud on the day of the eclipse.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kalit so'z:</strong> <em>Brazilian … main set of plates</em>. "
                "Matndagi joy: <em>the Brazilian instrument had shifted in the heat, and "
                "its main set of plates gave a figure that fitted neither "
                "prediction</em>.</p>"
                "<p>Javob o'sha jumlaning <u>ikkinchi yarmida</u> — birinchi yarmi "
                "(asbob qizib siljigan) faqat sabab.</p>"
                + why([
                    (True, "They produced a measurement that matched neither of the predictions being tested",
                     "<em>gave a figure that fitted neither prediction</em> — "
                     "so'zma-so'z."),
                    (False, "They were discarded before the expedition returned home",
                     "<strong>matnlarni chalkashtirish</strong>: tashlab yuborilishiga "
                     "yaqin kelgani — <u>Afrika</u> plastinalari "
                     "(<em>were nearly discarded</em>), Braziliya emas. Va hatto ular "
                     "ham tashlanmagan — <em>nearly</em>."),
                    (False, "They were the clearest images obtained by either of the two teams",
                     "matnga zid: e'lon qilingan natija <em>the smaller, better set "
                     "from each site</em> ga tayangan, ya'ni asosiy to'plam eng "
                     "yaxshisi emas edi."),
                    (False, "They were ruined by cloud on the day of the eclipse",
                     "bulut matnda faqat <u>ehtimol</u> sifatida eslatilgan "
                     "(<em>in case one was clouded out</em>) — u haqiqatan sodir "
                     "bo'lgan deyilmagan. <strong>Faraz ≠ voqea.</strong>"),
                ])
                + NOTE.format(
                    "1919-yilgi quyosh tutilishi ekspeditsiyasi haqiqatan ikki "
                    "guruhdan iborat bo'lgan va plastinalarning bir qismi sifatsiz "
                    "chiqqan — bu ilmiy tarixda yaxshi hujjatlashtirilgan hikoya. "
                    "Lekin imtihonda mavzuni bilish yordam bermaydi: to'rtta "
                    "variantning uchtasi ham <u>tarixan tanish</u> tuyuladi.")
            ),
        },

        {
            "rich_text": q(
                "<p>The letter Umida found in her mother's box was addressed to an "
                "aunt who had died before Umida was born, and it had never been posted. "
                "It thanked the aunt for money that had paid for a year of schooling, "
                "described an examination passed, and broke off mid-sentence at the "
                "bottom of the second page. There was no third page in the box.</p>",
                "Based on the text, what is true of the letter Umida found?"),
            "choices": [
                {"text": "It was never sent to the person it was written for.", "is_correct": True},
                {"text": "It was written to Umida by her mother.", "is_correct": False},
                {"text": "Its third page was found elsewhere in the house.", "is_correct": False},
                {"text": "It was returned unopened after the aunt's death.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu savol oson ko'rinadi va shuning uchun tez o'qiladi. Lekin "
                "to'rtta variantning uchtasi matnning <u>aniq so'zlariga</u> "
                "zid.</p>"
                + why([
                    (True, "It was never sent to the person it was written for",
                     "<em>it had never been posted</em> — so'zma-so'z, birinchi "
                     "jumlada."),
                    (False, "It was written to Umida by her mother",
                     "matn xat <u>xolaga</u> yozilganini aytadi. Xat onaning "
                     "qutisida topilgani uni «onadan Umidaga» qilmaydi — "
                     "<strong>topilgan joy ≠ murojaat qilingan odam</strong>."),
                    (False, "Its third page was found elsewhere in the house",
                     "matnda <em>There was no third page in the box</em> deyilgan — "
                     "uyning boshqa joyi haqida hech nima aytilmagan. "
                     "<strong>Yo'qlik ≠ boshqa joyda bor.</strong>"),
                    (False, "It was returned unopened after the aunt's death",
                     "xat hech qachon jo'natilmagan, demak qaytarilishi ham mumkin "
                     "emas. Bu variant birinchi jumlaning o'zi bilan ziddiyatga "
                     "kiradi."),
                ])
                + TIP.format(
                    "Uchala noto'g'ri variant ham <u>bo'shliqni to'ldirish</u>dan "
                    "tug'ildi: matn aytmagan narsani o'quvchi o'zi to'qiydi "
                    "(uchinchi sahifa qayerda? xat kimga?). Adabiy parchalarda bu "
                    "ayniqsa kuchli, chunki hikoya davomini kutasiz. "
                    "<strong>Matn tugagan joyda siz ham to'xtang.</strong>")
            ),
        },

        {
            "rich_text": q(
                "<p>Lighthouse keepers recorded the weather at fixed hours whether "
                "anything was happening or not, and they went on doing it for a century. "
                "Meteorologists ignored the logbooks for decades on the ground that the "
                "observers were amateurs. What changed their minds was the fixed hours: a "
                "reading taken at the same moment every day, by someone with no theory to "
                "defend, is exactly what a long series needs.</p>",
                "According to the text, why did meteorologists change their view of the "
                "logbooks?"),
            "choices": [
                {"text": "Because the readings were taken at consistent times by observers with nothing to prove.", "is_correct": True},
                {"text": "Because the keepers were later shown to have been trained observers after all.", "is_correct": False},
                {"text": "Because no other weather records survive from that century.", "is_correct": False},
                {"text": "Because the logbooks described unusual weather events in unusual detail.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kalit so\u2018z:</strong> <em>changed their minds</em>. "
                "Matndagi joy \u2014 oxirgi jumla, va ikki nuqta javobni "
                "ochiq beradi: <em>the fixed hours</em> + <em>no theory to "
                "defend</em>.</p>"
                + why([
                    (True, "Because the readings were taken at consistent times by observers with nothing to prove",
                     "ikki nuqtadan keyingi izohning ikkala qismini ham oladi \u2014 "
                     "muntazam vaqt va xolislik."),
                    (False, "Because the keepers were later shown to have been trained observers after all",
                     "<strong>havaskorlik masalasi hal qilinmaydi.</strong> Matn "
                     "qarama-qarshi narsani aytadi: aynan havaskorlik \u2014 "
                     "<em>no theory to defend</em> \u2014 foydali bo\u2018lib chiqdi."),
                    (False, "Because no other weather records survive from that century",
                     "boshqa yozuvlarning yo\u2018qligi haqida bir og\u2018iz ham "
                     "yo\u2018q. <strong>Tashqi bilim.</strong>"),
                    (False, "Because the logbooks described unusual weather events in unusual detail",
                     "matn aynan aksini ta\u2019kidlaydi: <em>whether anything was "
                     "happening or not</em> \u2014 qiymati g\u2018ayrioddiy hodisalarda "
                     "emas, muntazamlikda."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">according to the text</div><div class="pp-card-back">matnga ko\'ra</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the text most strongly suggests</div><div class="pp-card-back">matn eng kuchli darajada shuni nazarda tutadi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to breed true</div><div class="pp-card-back">urug\'dan ona o\'simlikka o\'xshash nasl bermoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to graft</div><div class="pp-card-back">payvand qilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a rootstock</div><div class="pp-card-back">payvandtag (ildiz qismi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to be clouded out</div><div class="pp-card-back">bulut tufayli kuzatuv barbod bo\'lmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to break off mid-sentence</div><div class="pp-card-back">jumla o\'rtasida uzilib qolmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">windward</div><div class="pp-card-back">shamolga qaragan (tomon)</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Javob <strong>ekranda</strong>, xotirangizda emas — har doim "
              "matnga qayting.</li>"
              "<li>Kalit so'zni toping, keyin <u>butun jumlani</u> o'qing "
              "(<em>though</em>, <em>but</em> dan keyingi qismni ham).</li>"
              "<li><strong>Matndagi so'z ≠ matndagi da'vo</strong>: variant tanish "
              "so'z ishlatgani hech nimani isbotlamaydi.</li>"
              "<li><em>nearly</em>, <em>in case</em> kabi so'zlar voqeani "
              "<u>bo'lmagan</u> qiladi — ularni o'qing.</li>"
              "<li>Matn tugagan joyda to'xtang: bo'shliqni o'zingiz "
              "to'ldirmang.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 43
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CID,
    "title": "SAT R&W 43: Literature Passages — Character and Situation Without a Thesis",
    "summary": "Adabiy parchada da'vo jumlasi yo'q; asosiy fikr — vaziyat yoki "
               "personajning tushunchasidagi o'zgarish. «Nima o'zgardi?» degan savol.",
    "order": 43,
    "blocks": [
        {"rich_text": (
            "<h2>Da'vo jumlasi yo'q bo'lganda</h2>"
            "<p>SAT ning to'rt mavzu sohasidan biri — <strong>literature</strong>. "
            "Adabiy parchalar (hikoya, roman parchasi, ba'zan she'r) barcha savol "
            "turlarida uchraydi, va ular <mark>bitta muhim jihat bilan farq "
            "qiladi</mark>: ularda da'vo jumlasi yo'q.</p>"
            "<p>Ilmiy matnda muallif nimadir da'vo qiladi. Hikoyada esa "
            "<u>hech kim hech nimani da'vo qilmaydi</u> — odamlar shunchaki nimadir "
            "qiladi. 40-darsdagi «da'vo jumlasini toping» usuli bu yerda "
            "ishlamaydi.</p>"
            "<p>Yangi savol kerak.</p>"
            + '<span class="sr-time">⏱ ~55 soniya</span>'
        )},

        {"rich_text": (
            "<h3>«Nima o'zgardi?»</h3>"
            "<p>SAT adabiy parchasi deyarli har doim <strong>bitta o'zgarish</strong> "
            "atrofida quriladi. Parcha qisqa, shuning uchun unda katta voqea "
            "bo'lolmaydi — o'zgarish odatda ichkarida sodir bo'ladi.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>O'zgarish turi</th><th>Savol</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Tushunish</strong></td>"
              "<td>Personaj oxirida nimani bilib oldi?</td></tr>"
              "<tr><td><strong>Munosabat</strong></td>"
              "<td>U biror narsaga boshqacha qaray boshladimi?</td></tr>"
              "<tr><td><strong>Vaziyat</strong></td>"
              "<td>Tashqi holat o'zgardimi, va personaj unga qanday javob berdi?</td></tr>"
              "<tr><td><strong>Ziddiyat</strong></td>"
              "<td>Personaj <u>xohlagani</u> bilan <u>qilgani</u> orasidagi farq</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Adabiy parchada <strong>oxirgi jumla</strong> ilmiy matndagidan ham "
                "muhimroq. Yozuvchi parchani tasodifiy joyda tugatmaydi — oxirgi "
                "jumla deyarli har doim o'zgarishni ko'rsatadi yoki uni "
                "nomlaydi.")
        )},

        {"rich_text": (
            "<h3>Uchta doimiy tuzoq</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Tuzoq</th><th>Nega noto'g'ri</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Voqeani qayta aytish</strong></td>"
              "<td>«U xat oldi va o'qidi» — bu sodir bo'lgan narsa, asosiy fikr "
              "emas</td></tr>"
              "<tr><td><strong>Personajga baho berish</strong></td>"
              "<td><em>selfish · foolish · brave</em> — matn baho bermaydi, va siz ham "
              "bermang</td></tr>"
              "<tr><td><strong>Sababni to'qish</strong></td>"
              "<td>Yozuvchi sababni ataylab aytmaydi; variant uni «tushuntirsa» — "
              "tuzoq</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "Uchinchi tuzoq eng nozik. Yozuvchilar <u>ataylab</u> sababni "
                "yashiradi: Rustam nega natijani ko'rmadi? Ota nega faqat qish haqida "
                "gapirdi? Bu bo'shliqlar — adabiyotning usuli. Variant o'sha "
                "bo'shliqni to'ldirsa, u <strong>matndan kengroq</strong> "
                "bo'lib qoladi, qanchalik ishonarli tuyulmasin.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + q(
                "<p>For eleven years the shop had opened at six, and for eleven years "
                "Ozod had unlocked it. The morning after his son took over the keys he "
                "woke at five to five, dressed, and walked the same road. He stood across "
                "the street until the shutters went up at ten past six, noted the ten "
                "minutes without satisfaction, and understood, standing there in the "
                "cold, that he had come to be needed and had found instead that the shop "
                "would open without him.</p>",
                "Which choice best states the main idea of the text?")
            + choices_html([
                "Ozod is angry that his son opened the shop ten minutes late.",
                "Ozod goes to the shop expecting to find himself necessary and discovers "
                "that he is not.",
                "Ozod regrets having handed the shop over to his son so early.",
                "Ozod has kept the habits of a working life he can no longer practise.",
            ])
            + '<span class="sr-time">⏱ ~55 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>«Nima o'zgardi?»</strong> Tashqarida deyarli hech nima: bir "
            "odam ko'chada turdi. O'zgarish oxirgi jumlada, va matn uni "
            "<u>o'zi nomlaydi</u>: <em>he had come to be needed and had found instead "
            "that the shop would open without him</em>.</p>"
            "<p>Bu <mark>tushunishdagi o'zgarish</mark> — jadvaldagi birinchi tur.</p>"
            + why([
                (True, "Ozod goes to the shop expecting to find himself necessary and discovers that he is not",
                 "oxirgi jumlaning aynan qayta ifodasi: kutish (<em>come to be "
                 "needed</em>) va topilgan narsa (<em>would open without him</em>)."),
                (False, "Ozod is angry that his son opened the shop ten minutes late",
                 "<strong>voqeani qayta aytish + baho.</strong> O'n daqiqa matnda bor, "
                 "lekin <em>noted … without satisfaction</em> — bu g'azab emas, va "
                 "ayni paytda kechikish uning <u>umidini</u> oqlamagani muhim: "
                 "do'kon baribir ochildi."),
                (False, "Ozod regrets having handed the shop over to his son so early",
                 "<strong>sababni to'qish.</strong> Afsus matnda aytilmagan. Ozod "
                 "nima his qilayotgani ataylab ochiq qoldirilgan — bizga faqat "
                 "u nimani <u>tushunganini</u> aytishadi."),
                (False, "Ozod has kept the habits of a working life he can no longer practise",
                 "<strong>eng jozibali tuzoq</strong>: bu rost, va matnning "
                 "birinchi yarmini to'g'ri tasvirlaydi. Lekin odat — "
                 "<u>tayyorgarlik</u>; parcha o'sha odat uni qayerga olib "
                 "kelgani bilan tugaydi. <strong>Doirasi tor.</strong>"),
            ])
            + NOTE.format(
                "Diqqat qiling: to'g'ri javobda hech qanday <u>baho</u> yo'q. "
                "«Ozod g'amgin», «Ozod ortiqcha» — matn bunday demaydi. U faqat "
                "bitta odam bitta ertalab nimani bilib olganini aytadi. "
                "Javob ham xuddi shunday quruq bo'lishi kerak.")
        )},

        {
            "rich_text": q(
                "<p>Nigora had rehearsed the refusal on the bus. It was polite, it gave "
                "a reason that could not be argued with, and it did not apologise. When "
                "her cousin finally asked, sitting in the kitchen with the tea going "
                "cold between them, Nigora heard herself say that of course she would "
                "come, that it was no trouble at all, and that she had been hoping to be "
                "asked. She said it in the voice she used for customers.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "Nigora abandons a carefully prepared refusal the moment she is asked, and hears herself agreeing.", "is_correct": True},
                {"text": "Nigora is happy to be invited by her cousin after all.", "is_correct": False},
                {"text": "Nigora is a dishonest person who conceals her true feelings from her family.", "is_correct": False},
                {"text": "Nigora's cousin pressures her into agreeing to something she does not want to do.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>«Nima o'zgardi?»</strong> Nigora rad javobini tayyorlagan "
                "edi va uning aksini aytdi. Bu <mark>ziddiyat turi</mark>: xohlagani "
                "bilan qilgani orasidagi farq.</p>"
                "<p>Oxirgi jumla buni muhrlaydi: <em>She said it in the voice she used "
                "for customers</em> — ya'ni bu o'zi emas, o'rgangan roli.</p>"
                + why([
                    (True, "Nigora abandons a carefully prepared refusal the moment she is asked, and hears herself agreeing",
                     "<em>heard herself say</em> — hatto fe'l ham uning "
                     "boshqaruvdan chiqib ketganini ko'rsatadi. Javob ikkala qismni "
                     "ham oladi: tayyorgarlik va uning qulashi."),
                    (False, "Nigora is happy to be invited by her cousin after all",
                     "<strong>personajning so'zini haqiqat deb olish.</strong> "
                     "<em>she had been hoping to be asked</em> — bu Nigoraning "
                     "<u>aytgani</u>, va oxirgi jumla uni ataylab rad etadi."),
                    (False, "Nigora is a dishonest person who conceals her true feelings from her family",
                     "<strong>personajga baho berish.</strong> Matn hukm chiqarmaydi, "
                     "va <em>a dishonest person</em> bitta lahzadan xarakter "
                     "yasaydi. <strong>Doirasi keng.</strong>"),
                    (False, "Nigora's cousin pressures her into agreeing to something she does not want to do",
                     "<strong>sababni to'qish.</strong> Amakivachcha faqat "
                     "<em>asked</em> — bosim haqida bir og'iz ham yo'q. Nigorani "
                     "hech kim majburlamadi; u o'zi rozi bo'ldi, va parcha aynan "
                     "shuning uchun kuchli."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>The house was sold in March and the new owners repainted it in June. "
                "Karim drove past it twice a week on his way to the depot, and for a "
                "while the colour offended him. By August he was noticing it less; by "
                "October he had to look for the window that had been his. He found that "
                "he did not mind, and he minded that.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "Karim is troubled to discover that his attachment to the house has faded.", "is_correct": True},
                {"text": "Karim dislikes the colour the new owners chose for the house.", "is_correct": False},
                {"text": "Karim regrets having sold the house to the new owners.", "is_correct": False},
                {"text": "Karim has adjusted well to the loss of his former home.", "is_correct": False},
            ],
            "explanation": (
                "<p>Butun parcha oxirgi olti so'z uchun yozilgan: "
                "<mark><em>He found that he did not mind, and he minded that.</em></mark></p>"
                "<p>Ikkita <em>mind</em>: birinchisi uy haqida, ikkinchisi "
                "<u>birinchisining yo'qligi</u> haqida. O'zgarish — "
                "bog'lanishning so'nishi, va Karimni bezovta qilgan narsa aynan "
                "shu so'nish.</p>"
                + why([
                    (True, "Karim is troubled to discover that his attachment to the house has faded",
                     "ikkinchi <em>minded</em> ning ma'nosi. Va mart–oktyabr "
                     "ketma-ketligi (rangdan xafa → sezmay qo'ydi → derazani "
                     "qidiradi) so'nishning bosqichma-bosqich isboti."),
                    (False, "Karim dislikes the colour the new owners chose for the house",
                     "<strong>doirasi tor va vaqti o'tgan</strong>: "
                     "<em>for a while the colour offended him</em> — «bir muddat». "
                     "Parcha aynan shundan keyingi o'zgarish haqida."),
                    (False, "Karim regrets having sold the house to the new owners",
                     "<strong>sababni to'qish</strong>: matn uyni kim sotganini ham "
                     "aytmaydi (<em>The house was sold</em> — passiv, ataylab). "
                     "Afsus haqida bir og'iz yo'q."),
                    (False, "Karim has adjusted well to the loss of his former home",
                     "<strong>eng nozik tuzoq</strong>: birinchi yarmi rost — u "
                     "moslashdi. Lekin oxirgi to'rt so'z (<em>and he minded "
                     "that</em>) buni <u>muammoga aylantiradi</u>. "
                     "<em>Well</em> so'zi matnning butun burilishini o'chirib "
                     "tashlaydi."),
                ])
                + TIP.format(
                    "Adabiy parchada oxirgi jumla qisqa va g'alati bo'lsa — "
                    "u deyarli har doim javobdir. <em>He found that he did not mind, "
                    "and he minded that.</em> Yozuvchi bunday jumlani bekorga "
                    "yozmaydi.")
            ),
        },

        {
            "rich_text": q(
                "<p>The examiner had asked the same question of forty candidates that "
                "week and had stopped hearing the answers. Then a girl of about "
                "seventeen said she did not know, and waited. She did not soften it, did "
                "not offer a guess, did not look away. The examiner wrote something in "
                "the margin that was not a mark, and for the first time that week he "
                "listened to what the next candidate said.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "A candidate's plain admission of ignorance restores the examiner's attention to his work.", "is_correct": True},
                {"text": "The examiner decides to give the girl a higher mark than the other candidates.", "is_correct": False},
                {"text": "The examiner realises that his question was too difficult for most candidates.", "is_correct": False},
                {"text": "The girl is more honest than the other candidates the examiner has met.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>«Nima o'zgardi?»</strong> Diqqat: o'zgargan odam — "
                "<u>qiz emas, imtihonchi</u>. Parcha uning bilan boshlanadi "
                "(<em>had stopped hearing</em>) va uning bilan tugaydi "
                "(<em>for the first time that week he listened</em>).</p>"
                + why([
                    (True, "A candidate's plain admission of ignorance restores the examiner's attention to his work",
                     "birinchi va oxirgi jumla juftligi: <em>had stopped hearing</em> "
                     "→ <em>he listened</em>. Qiz — sabab, imtihonchi — o'zgargan "
                     "tomon."),
                    (False, "The examiner decides to give the girl a higher mark than the other candidates",
                     "matn buni <strong>ataylab rad etadi</strong>: "
                     "<em>wrote something in the margin that was <u>not a "
                     "mark</u></em>. Baho haqidagi variantni aynan shu ibora "
                     "o'ldiradi."),
                    (False, "The examiner realises that his question was too difficult for most candidates",
                     "<strong>sababni to'qish</strong>: savolning qiyinligi umuman "
                     "muhokama qilinmaydi. Imtihonchi eshitishni to'xtatgan edi, "
                     "chunki javoblar takrorlanardi — qiyinlikdan emas."),
                    (False, "The girl is more honest than the other candidates the examiner has met",
                     "<strong>personajga baho berish</strong> va noto'g'ri fokus: "
                     "boshqa nomzodlar yolg'on gapirdi deyilmagan, va parcha qiz "
                     "haqida emas. U qiz keltirgan <u>ta'sir</u> haqida."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>His daughter had sent the photographs by post, printed, because she "
                "knew he would not open a link. Rahim looked at the top one for a long "
                "time \u2014 a kitchen he did not recognise, a window with a different sort "
                "of light in it \u2014 and then put the whole envelope in the drawer where "
                "the bills went. He took it out again the same evening and looked at "
                "every one of them twice.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "Rahim puts away the evidence of his daughter's new life and finds that he cannot leave it there.", "is_correct": True},
                {"text": "Rahim is angry that his daughter moved away without consulting him.", "is_correct": False},
                {"text": "Rahim is unable to use the internet and must be sent printed photographs.", "is_correct": False},
                {"text": "Rahim's daughter sends the photographs in order to remind him of his loneliness.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>\u00abNima o\u2018zgardi?\u00bb</strong> Ikki harakat, bir necha "
                "soat orasida: konvertni yashirdi \u2192 qaytarib oldi va har birini "
                "<u>ikki marta</u> ko\u2018rdi. O\u2018zgarish shu ikki harakat "
                "<mark>orasida</mark> turibdi, va matn uni izohlamaydi \u2014 "
                "ko\u2018rsatadi.</p>"
                + why([
                    (True, "Rahim puts away the evidence of his daughter's new life and finds that he cannot leave it there",
                     "ikkala harakatni ham oladi va ularning ziddiyatini saqlaydi. "
                     "<em>twice</em> so\u2018zi ikkinchi harakatning kuchini beradi."),
                    (False, "Rahim is angry that his daughter moved away without consulting him",
                     "<strong>sababni to\u2018qish</strong>: g\u2018azab ham, "
                     "maslahatlashmaslik ham matnda yo\u2018q. Yozuvchi Rahimning "
                     "his-tuyg\u2018usini ataylab nomlamaydi."),
                    (False, "Rahim is unable to use the internet and must be sent printed photographs",
                     "<strong>doirasi tor</strong> va biroz burilgan: matn "
                     "<em>would not open a link</em> deydi \u2014 <u>xohlamaydi</u>, "
                     "<u>uddalay olmaydi</u> emas. Va bu birinchi jumladagi tafsilot, "
                     "parchaning mavzusi emas."),
                    (False, "Rahim's daughter sends the photographs in order to remind him of his loneliness",
                     "<strong>niyatni to\u2018qish</strong>, va u matnga zid: qizi "
                     "otasini bilgani uchun bosma qilib yuborgan \u2014 bu "
                     "e\u2019tibor, shafqatsizlik emas."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">an attachment to ~</div><div class="pp-card-back">~ ga bog\'lanish, mehr</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to fade</div><div class="pp-card-back">so\'nmoq, susaymoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to mind ~</div><div class="pp-card-back">~ dan bezovta bo\'lmoq, e\'tibor bermoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to soften (a statement)</div><div class="pp-card-back">(gapni) yumshatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an admission</div><div class="pp-card-back">tan olish, iqror</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to hear oneself say ~</div><div class="pp-card-back">o\'zining ~ deyayotganini eshitib qolmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">without satisfaction</div><div class="pp-card-back">mamnun bo\'lmasdan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">in the margin</div><div class="pp-card-back">chetiga, hoshiyaga</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Adabiy parchada da'vo jumlasi yo'q — «<strong>Nima "
              "o'zgardi?</strong>» deb so'rang.</li>"
              "<li>O'zgarish odatda <u>ichkarida</u>: tushunish, munosabat, "
              "vaziyat yoki ziddiyat.</li>"
              "<li><strong>Oxirgi jumla</strong> deyarli har doim o'zgarishni "
              "nomlaydi — ayniqsa qisqa va g'alati bo'lsa.</li>"
              "<li>Uch tuzoq: voqeani qayta aytish · personajga baho berish · "
              "sababni to'qish.</li>"
              "<li>Personajning <u>aytgani</u> — hikoyaning haqiqati emas.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 44
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CID,
    "title": "SAT R&W 44: Central Ideas and Details — Mixed Practice",
    "summary": "Asosiy fikr va tafsilot savollari aralash, ilmiy va adabiy parchalar "
               "bilan, imtihon tezligida: 40–43-darslarni soatga qarshi mustahkamlash.",
    "order": 44,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy amaliyot</h2>"
            "<p>Oltita savol: <em>main idea</em> va <em>detail</em> aralash, ilmiy, "
            "tarixiy va adabiy parchalar bilan.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Qanday ishlash kerak:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li>Taymer: <strong>5 daqiqa</strong> (6 × 50 soniya).</li>"
                "<li>Asosiy fikr savolida — <u>da'vo jumlasini</u> toping "
                "(adabiy parchada: «nima o'zgardi?»).</li>"
                "<li>Tafsilot savolida — <u>matnga qayting</u>, xotiradan javob "
                "bermang.</li>"
                "</ol>")
            + '<span class="sr-time">⏱ 6 savol · 5 daqiqa</span>'
        )},

        {
            "rich_text": q(
                "<p>Roman concrete harbour works have stood in seawater for two thousand "
                "years while modern piers crumble in fifty. The Roman mix used volcanic "
                "ash, and seawater reacting with it grows crystals inside the cracks that "
                "form. Modern concrete is designed to keep water out, because water "
                "reaching the steel inside it causes rust. The ancient material has no "
                "steel to protect and is therefore free to let the sea repair it.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "Roman concrete lasts in seawater because it has no steel to protect, allowing a reaction that closes its own cracks.", "is_correct": True},
                {"text": "Volcanic ash is a stronger building material than the cement used today.", "is_correct": False},
                {"text": "Modern concrete piers begin to crumble after about fifty years in seawater.", "is_correct": False},
                {"text": "Engineers should replace steel reinforcement with volcanic ash in marine construction.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo jumlasi</strong> — oxirgisi, va u ikki qismli: "
                "po'lat yo'q → dengiz ta'mirlashiga <u>ruxsat berilgan</u>.</p>"
                + why([
                    (True, "Roman concrete lasts in seawater because it has no steel to protect, allowing a reaction that closes its own cracks",
                     "oxirgi jumlaning aynan mazmuni, va kristallar haqidagi jumla "
                     "uning mexanizmi."),
                    (False, "Volcanic ash is a stronger building material than the cement used today",
                     "<strong>biroz burilgan</strong>: matn <em>stronger</em> "
                     "(mustahkamroq) demaydi — u <u>uzoq chidashi</u> haqida, va sabab "
                     "kuchda emas, po'latning yo'qligida."),
                    (False, "Modern concrete piers begin to crumble after about fifty years in seawater",
                     "<strong>doirasi tor</strong>: birinchi jumladagi taqqoslashning "
                     "yarmi. Matn undan keyin boshlanadi."),
                    (False, "Engineers should replace steel reinforcement with volcanic ash in marine construction",
                     "<strong>matnda yo'q tavsiya</strong> — va matnning o'zi po'lat "
                     "nima uchun ishlatilishini tushuntirib turibdi."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Between 1890 and 1914 the number of public libraries in Britain rose "
                "sharply, funded largely by a single donor who required each town to "
                "commit to a rate for the upkeep before he would pay for the building. "
                "Towns that refused the condition got nothing. The condition was the "
                "point: a building with no committed running cost tends to close within a "
                "generation.</p>",
                "According to the text, what did the donor require of a town before "
                "funding a library building?"),
            "choices": [
                {"text": "That it agree in advance to levy a rate for the library's upkeep.", "is_correct": True},
                {"text": "That it already own a suitable site for the building.", "is_correct": False},
                {"text": "That it match his contribution with an equal sum.", "is_correct": False},
                {"text": "That it keep the library open for at least a generation.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kalit so'z:</strong> <em>required</em>. Matndagi joy: "
                "<em>required each town to commit to a rate for the upkeep before he "
                "would pay for the building</em>. Javob so'zma-so'z shu yerda.</p>"
                + why([
                    (True, "That it agree in advance to levy a rate for the library's upkeep",
                     "<em>commit to a rate for the upkeep</em> — soliq yig'ishga "
                     "oldindan majburiyat olish."),
                    (False, "That it match his contribution with an equal sum",
                     "teng mablag' matnda yo'q — shart <u>doimiy xarajat</u> haqida "
                     "edi, bir martalik to'lov haqida emas. <strong>Xayriya "
                     "haqidagi umumiy tasavvurdan</strong> yozilgan tuzoq."),
                    (False, "That it already own a suitable site for the building",
                     "yer uchastkasi umuman eslatilmaydi."),
                    (False, "That it keep the library open for at least a generation",
                     "<em>a generation</em> matnda <u>bor</u>, lekin butunlay boshqa "
                     "gapda: xarajatsiz bino bir avlod ichida yopiladi. Bu shart "
                     "emas, oqibat. <strong>Matndagi so'z ≠ matndagi da'vo.</strong>"),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Sevara had promised to say nothing, and she said nothing for nine "
                "days. On the tenth her sister mentioned the wedding in passing, as "
                "settled, and Sevara heard her own voice ask what would happen to the "
                "flat. The sentence was out before she had decided to say it. In the "
                "silence that followed she understood that she had been waiting for "
                "somebody to ask her a question she could answer honestly, and that "
                "nobody was going to.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "Sevara breaks a silence she had kept and recognises that she had been waiting to be asked.", "is_correct": True},
                {"text": "Sevara is angry with her sister for discussing the wedding as though it were settled.", "is_correct": False},
                {"text": "Sevara is concerned about what will happen to the flat after the wedding.", "is_correct": False},
                {"text": "Sevara has been dishonest with her family for nine days.", "is_correct": False},
            ],
            "explanation": (
                "<p>Adabiy parcha — «<strong>Nima o'zgardi?</strong>». Tashqarida: u "
                "gapirdi. Ichkarida (oxirgi jumla): u nimani kutayotganini va uning "
                "bo'lmasligini <mark>tushunib yetdi</mark>.</p>"
                + why([
                    (True, "Sevara breaks a silence she had kept and recognises that she had been waiting to be asked",
                     "ikkala qismni ham oladi: harakat (savol og'zidan chiqib "
                     "ketdi) va tushunish (oxirgi jumla)."),
                    (False, "Sevara is concerned about what will happen to the flat after the wedding",
                     "<strong>voqeani qayta aytish</strong>: kvartira haqidagi savol "
                     "— vosita, mavzu emas. Oxirgi jumla uni "
                     "<u>o'zi tushuntiradi</u>: gap kvartirada emas, savol "
                     "berilishida."),
                    (False, "Sevara is angry with her sister for discussing the wedding as though it were settled",
                     "<strong>personajga baho + sababni to'qish.</strong> G'azab "
                     "matnda yo'q; opa mavzuni <em>in passing</em> tilga oldi, "
                     "shafqatsizlik bilan emas."),
                    (False, "Sevara has been dishonest with her family for nine days",
                     "<strong>personajga baho.</strong> U va'da berib jim turgan — "
                     "bu yolg'on emas, va matn hukm chiqarmaydi. To'qqiz kun "
                     "faktdir, «yolg'onchilik» esa sizning qo'shimchangiz."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>A trial found that a drug reduced the rate of a rare complication "
                "from four cases per thousand patients to two. The result was reported as "
                "halving the risk, which it did. It was also reported as preventing two "
                "cases in every thousand people treated, which it also did. The two "
                "sentences describe one number and produce different decisions in almost "
                "everyone who reads them.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "The same result, stated in two accurate ways, leads readers to weigh it differently.", "is_correct": True},
                {"text": "The drug reduced the rate of the complication from four cases per thousand to two.", "is_correct": False},
                {"text": "Reporting a result as a halving of risk is misleading and should be avoided.", "is_correct": False},
                {"text": "Rare complications are more difficult to study than common ones.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo jumlasi</strong> — oxirgisi. Va e'tibor bering: matn "
                "ikkala ifodani ham <u>to'g'ri</u> deb ataydi "
                "(<em>which it did</em> · <em>which it also did</em>). Demak "
                "gap aldash haqida emas, <mark>bir xil raqamning ikki xil "
                "ta'siri</mark> haqida.</p>"
                + why([
                    (True, "The same result, stated in two accurate ways, leads readers to weigh it differently",
                     "oxirgi jumlaning aynan mazmuni, va <em>accurate</em> so'zi "
                     "matnning ikki e'tirofini saqlaydi."),
                    (False, "The drug reduced the rate of the complication from four cases per thousand to two",
                     "<strong>doirasi tor</strong>: bu birinchi jumla, ya'ni "
                     "matnning <u>materiali</u>. Matn undan keyin boshlanadi."),
                    (False, "Reporting a result as a halving of risk is misleading and should be avoided",
                     "<strong>biroz burilgan va matnda yo'q tavsiya.</strong> Matn "
                     "<em>which it did</em> deb bu ifodani to'g'ri deb tan oladi. "
                     "«Aldamchi» degan baho — sizning qo'shimchangiz."),
                    (False, "Rare complications are more difficult to study than common ones",
                     "qiyinlik ham, taqqoslash ham matnda yo'q. "
                     "<strong>So'z-tuzoq</strong>: <em>rare</em> so'zidan yozilgan."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Ice cores are read like tree rings: each year's snowfall makes a "
                "layer, and the layers can be counted down. Near the surface the counting "
                "is reliable. Deeper down the weight of the ice above squeezes the layers "
                "thin, and below a certain depth two years can no longer be told apart. "
                "Dates from the deepest ice are therefore matched to other records rather "
                "than counted directly.</p>",
                "According to the text, why are dates from the deepest ice not obtained "
                "by counting layers?"),
            "choices": [
                {"text": "Because pressure from the ice above compresses the layers until adjacent years cannot be distinguished.", "is_correct": True},
                {"text": "Because snowfall was less regular in the distant past than it is today.", "is_correct": False},
                {"text": "Because the deepest ice is too fragile to be recovered intact.", "is_correct": False},
                {"text": "Because other records are known to be more accurate than ice cores.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kalit so'z:</strong> <em>deepest</em> / <em>deeper "
                "down</em>. Matndagi joy: <em>the weight of the ice above squeezes the "
                "layers thin, and below a certain depth two years can no longer be told "
                "apart</em>.</p>"
                + why([
                    (True, "Because pressure from the ice above compresses the layers until adjacent years cannot be distinguished",
                     "o'sha jumlaning aynan mazmuni: bosim → qatlamlar yupqalashadi "
                     "→ ikki yilni ajratib bo'lmaydi."),
                    (False, "Because snowfall was less regular in the distant past than it is today",
                     "qor yog'ishining o'zi o'zgargani matnda yo'q — muammo "
                     "<u>qatlamning siqilishida</u>, uning hosil bo'lishida emas."),
                    (False, "Because the deepest ice is too fragile to be recovered intact",
                     "namuna olish qiyinligi eslatilmaydi. <strong>Tashqi "
                     "bilim.</strong>"),
                    (False, "Because other records are known to be more accurate than ice cores",
                     "boshqa yozuvlar matnda <u>bor</u>, lekin ular aniqroq "
                     "deyilmagan — ular shunchaki <u>muqobil usul</u>. "
                     "<strong>Matndagi so'z ≠ matndagi da'vo.</strong>"),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Rice terraces on steep hillsides hold soil that would otherwise wash "
                "into the valley, and the walls that retain them need repair after every "
                "heavy season. In villages where the young have gone to the cities, the "
                "terraces fail in a particular order: the highest first, because they are "
                "furthest from the houses and the last to be walked to. What the "
                "hillside loses is not labour in general but the walk.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "The terraces fail in an order set by distance from the village, so what their upkeep depends on is proximity rather than effort alone.", "is_correct": True},
                {"text": "Rice terraces prevent soil on steep hillsides from washing into the valley.", "is_correct": False},
                {"text": "Young people who leave villages for the cities should be encouraged to return.", "is_correct": False},
                {"text": "Terrace walls require repair after every season of heavy rain.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo jumlasi</strong> — oxirgisi, va u juda qisqa: "
                "<mark><em>What the hillside loses is not labour in general but the "
                "walk.</em></mark> <em>not … but …</em> qurilishi asosiy fikrni "
                "aynan shu yerda joylashtiradi.</p>"
                + why([
                    (True, "The terraces fail in an order set by distance from the village, so what their upkeep depends on is proximity rather than effort alone",
                     "<em>the highest first, because they are furthest</em> "
                     "(tartib) va oxirgi jumla (masofa ↔ mehnat) — ikkovini ham "
                     "qamraydi."),
                    (False, "Rice terraces prevent soil on steep hillsides from washing into the valley",
                     "<strong>doirasi tor</strong>: birinchi jumlaning yarmi, "
                     "ya'ni fon."),
                    (False, "Terrace walls require repair after every season of heavy rain",
                     "yana <strong>doirasi tor</strong> — birinchi jumlaning "
                     "ikkinchi yarmi. Ikkala tor variant ham birinchi jumladan "
                     "yozilgan: bu tasodif emas, doimiy naqsh."),
                    (False, "Young people who leave villages for the cities should be encouraged to return",
                     "<strong>matnda yo'q tavsiya.</strong> Matn nima uchun "
                     "yuqoridagilar birinchi qulashini tushuntiradi, nima qilish "
                     "kerakligini emas."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Xatoni turi bo'yicha tahlil qiling</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Xato turi</th><th>Nima qilish kerak</th></tr></thead>"
              "<tbody>"
              "<tr><td>Birinchi jumladan yozilgan variantni tanladim</td>"
              "<td>40-dars. Da'vo jumlasi odatda <u>oxirida</u>.</td></tr>"
              "<tr><td>Rost dalilni asosiy fikr deb oldim</td>"
              "<td>41-dars, «doirasi tor» sinovi.</td></tr>"
              "<tr><td>Bir-ikki so'zi matnda yo'q variantni tanladim</td>"
              "<td>41-dars, «biroz burilgan». <em>should · all · more · "
              "misleading</em>.</td></tr>"
              "<tr><td>Matndagi tanish so'z uchun tanladim</td>"
              "<td>42-dars. So'z bor bo'lishi yetarli emas — da'vo bor bo'lsin.</td></tr>"
              "<tr><td>Adabiy parchada personajga baho berdim</td>"
              "<td>43-dars. Matn hukm chiqarmaydi.</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Bu mavzuda eng ko'p takrorlanadigan naqsh: <strong>noto'g'ri "
                "variantlar matnning birinchi jumlasidan yoziladi, to'g'ri javob "
                "esa oxirgisidan</strong>. Buni bir marta payqasangiz, "
                "o'nlab savolni tezlashtiradi.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">upkeep</div><div class="pp-card-back">saqlash xarajati, ta\'minlash</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to commit to ~</div><div class="pp-card-back">~ ga majburiyat olmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to tell apart</div><div class="pp-card-back">bir-biridan ajratmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to weigh a result</div><div class="pp-card-back">natijani baholamoq, taroziga solmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">proximity</div><div class="pp-card-back">yaqinlik (masofa jihatdan)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">in passing</div><div class="pp-card-back">o\'tib ketayotib, yo\'l-yo\'lakay</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to levy a rate</div><div class="pp-card-back">soliq solmoq, yig\'im joriy qilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to retain (soil)</div><div class="pp-card-back">(tuproqni) ushlab turmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa — Central Ideas and Details mavzusi yakuni</h3>"
            + "<ul>"
              "<li><strong>Mavzu ≠ asosiy fikr</strong>; da'vo jumlasini toping "
              "(40-dars).</li>"
              "<li>Uch noto'g'ri shakl: keng · tor · biroz burilgan (41-dars).</li>"
              "<li>Tafsilotda <strong>matnga qayting</strong> — xotira "
              "aldaydi (42-dars).</li>"
              "<li>Adabiy parchada: «<u>nima o'zgardi?</u>», baho bermang "
              "(43-dars).</li>"
              "<li>Naqsh: tuzoqlar <u>birinchi</u> jumladan, javob "
              "<u>oxirgi</u> jumladan.</li>"
              "</ul>"
        )},
    ],
},

]
