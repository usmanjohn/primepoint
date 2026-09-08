# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — Reading lessons 70-74.

Covers "Mantiqiy xulosa (Inferences)" — the last question type in the
Information and Ideas domain. See toc_sat_reading.txt and STYLE_GUIDE_SAT_RW.md.
"""

TRACK = {
    "name":    "SAT",
    "summary": "Digital SAT — Reading and Writing bo'limiga savol turlari bo'yicha "
               "tayyorgarlik. Imtihonning matematik yarmi Prime SAT Math kursida.",
    "icon":    "bi-mortarboard",
    "color":   "#7c3aed",
    "order":   3,
}

TOPIC_INF = {
    "title":   "Mantiqiy xulosa (Inferences)",
    "summary": "Matn oxiridagi bo'sh joyni to'ldirish: matn allaqachon isbotlagan "
               "xulosani aytish — na kamroq, na ko'proq.",
    "icon":    "bi-lightbulb",
    "order":   8,
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


def inf_q(passage):
    """An Inferences question: the passage ends in a blank, and the stem never varies."""
    return (f'<div class="sr-passage">{passage}</div>'
            f'<p><strong>Which choice most logically completes the text?</strong></p>')


def choices_html(items):
    """The static A/B/C/D list used in a WORKED example (not a shuffled choices block)."""
    return '<ol type="A">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 70
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_INF,
    "title": "SAT R&W 70: Inferences — “Which Choice Most Logically Completes the Text?”",
    "summary": "Matn oxirida bo'sh joy: sizdan taxmin emas, matn allaqachon qilib "
               "qo'ygan ishning xulosasini aytish so'raladi.",
    "order": 70,
    "blocks": [
        {"rich_text": (
            "<h2>Taxmin emas — hisob</h2>"
            "<p><strong>Inferences</strong> — <em>Information and Ideas</em> "
            "domenining oxirgi turi. Uni tanish oson, chunki u har doim bir xil "
            "ko'rinadi: <mark>matn bo'sh joy bilan tugaydi</mark>, va savol "
            "hech qachon o'zgarmaydi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\"><em>Which choice most "
                "logically completes the text?</em></p>")
            + "<p>O'zbekcha «xulosa chiqarish» degani ba'zan «taxmin qilish» ma'nosini "
            "beradi. Bu yerda <u>umuman</u> unday emas. Matn ikki-uch fakt beradi, "
            "va o'sha faktlar birgalikda bitta narsani majburlaydi. Sizning ishingiz "
            "— o'sha narsani <strong>aytish</strong>, o'ylab topish emas.</p>"
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Uch qoida</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Javob matndan "
              "<u>chiqishi</u> kerak.</strong> Faktlar A va B berilgan bo'lsa, javob "
              "A va B dan kelib chiqadigan narsa. Yangi ma'lumot qo'shsa — "
              "javob emas.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Javob matndan "
              "<u>kuchliroq</u> bo'lmasligi kerak.</strong> Matn bitta holatni "
              "ko'rsatgan bo'lsa, javob «har doim» demasin (73-dars).</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Javob matnning "
              "<u>maqsadiga</u> tegishli bo'lsin.</strong> Matndan chiqadigan "
              "arzimas narsa ham bor — masalan «demak tadqiqot o'tkazilgan». "
              "Javob matn <u>qurgan</u> fikrni yakunlaydi.</p></div>"
            + '</div>'
            + TIP.format(
                "Eng foydali odat: bo'sh joyga yetganda <strong>to'xtang va "
                "o'z jumlangizni ayting</strong> — o'zbekcha bo'lsa ham. "
                "«Demak mushuklarni odamlar olib borgan.» Shundan keyin "
                "variantlarni ochasiz. Bu 11-darsdagi bashorat usulining "
                "aynan o'zi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + inf_q(
                "<p>Cat bones have been found in human graves on Cyprus that are older "
                "than the earliest Egyptian images of domestic cats. No wild cat has "
                "ever been native to Cyprus, and the island has been separated from the "
                "mainland by open sea for far longer than cats have existed. A cat "
                "cannot swim that distance, and no natural process would carry one "
                "across. The burials therefore indicate that "
                "<span class=\"sr-blank\"></span></p>")
            + choices_html([
                "cats reached Cyprus without any help from people.",
                "people were carrying cats across open water before the earliest "
                "Egyptian images of them were made.",
                "the Egyptian images have been dated incorrectly and are older than has "
                "been supposed.",
                "cats were first domesticated on Cyprus rather than in Egypt.",
            ])
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>Faktlarni sanaymiz:</strong></p>"
            "<ul>"
            "<li>Kiprdagi qabrlarda mushuk suyaklari bor;</li>"
            "<li>ular Misr tasvirlaridan <u>eski</u>;</li>"
            "<li>Kiprda yovvoyi mushuk hech qachon bo'lmagan;</li>"
            "<li>mushuk u yerga o'zi yetib bora olmaydi.</li>"
            "</ul>"
            "<p><strong>Bu faktlar nimani majburlaydi?</strong> Mushuk orolda bor. "
            "O'zi kelmagan. Demak <mark>kimdir olib borgan</mark> — va bu "
            "Misr tasvirlaridan oldin bo'lgan.</p>"
            "<p><strong>O'z jumlam:</strong> «odamlar mushuklarni dengiz orqali "
            "olib o'tgan, Misr tasvirlaridan ham oldin».</p>"
            + why([
                (True, "people were carrying cats across open water before the earliest Egyptian images of them were made",
                 "to'rtala faktni ham ishlatadi va ulardan tashqariga chiqmaydi. "
                 "«Olib o'tgan» — bu suyaklarning u yerda bo'lishining yagona "
                 "qolgan izohi."),
                (False, "cats reached Cyprus without any help from people",
                 "<strong>matnga to'g'ridan-to'g'ri zid:</strong> "
                 "<em>A cat cannot swim that distance, and no natural process would "
                 "carry one across.</em>"),
                (False, "cats were first domesticated on Cyprus rather than in Egypt",
                 "<strong>matndan kuchliroq</strong> — 2-qoidani buzadi. "
                 "Mushukni kemada olib o'tish uni <u>xonakilashtirish</u> "
                 "degani emas, va matn «birinchi marta qayerda» degan savolga "
                 "umuman kirmaydi. Eng jozibali noto'g'ri javob."),
                (False, "the Egyptian images have been dated incorrectly and are older than has been supposed",
                 "<strong>yangi ma'lumot</strong> — 1-qoidani buzadi. Matn "
                 "Misr sanalarini shubha ostiga olmaydi; u ularni "
                 "<u>mustahkam nuqta</u> sifatida ishlatadi."),
            ])
            + NOTE.format(
                "Kiprdagi mushuk dafnlari haqiqatan arxeologiyada mashhur: orolda "
                "tabiiy mushuk turi bo'lmagan, shuning uchun har bir mushuk "
                "u yerga <u>odam bilan</u> kelgan. Lekin imtihonda bu bilim "
                "yordam bermaydi — javob baribir matnning o'zidan chiqadi.")
        )},

        {
            "rich_text": inf_q(
                "<p>A pharmacy's records show that patients who collect a repeat "
                "prescription on the day it falls due nearly always collect the next one "
                "on time as well, while patients who collect a few days late rarely "
                "become punctual afterwards. The pattern holds whether the medicine is "
                "taken once a day or four times, whether it treats a painful condition "
                "or a silent one, and whether the course lasts a month or a decade. What "
                "the records suggest is that collection timing "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "has more to do with the patient's own habits than with the particular treatment.", "is_correct": True},
                {"text": "improves once a patient understands the purpose of the medicine.", "is_correct": False},
                {"text": "is determined mainly by how often the medicine must be taken.", "is_correct": False},
                {"text": "could be improved if pharmacies sent reminders to late collectors.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Matnning yuragi</strong> — ikkinchi jumla, va u uzun "
                "bo'lgani uchun oson o'tkazib yuboriladi. U uchta narsani "
                "sanaydi: dorining <u>chastotasi</u>, <u>turi</u> va "
                "<u>davomiyligi</u>. Va uchalasida ham naqsh o'zgarmaydi.</p>"
                "<p>Agar dorining hech qanday xususiyati natijani "
                "o'zgartirmasa, farq <mark>dorida emas, odamda</mark>.</p>"
                + why([
                    (True, "has more to do with the patient's own habits than with the particular treatment",
                     "ikkinchi jumla aynan shu xulosa uchun yozilgan: dorining "
                     "har qanday xususiyati chetlashtirilgan, bemor qolgan."),
                    (False, "is determined mainly by how often the medicine must be taken",
                     "<strong>matnga zid:</strong> <em>whether the medicine is taken "
                     "once a day or four times</em> — chastota naqshni "
                     "o'zgartirmaydi."),
                    (False, "improves once a patient understands the purpose of the medicine",
                     "<strong>yangi ma'lumot.</strong> Tushunish, bilim yoki "
                     "tushuntirish matnda umuman yo'q. Va matn kechikkanlar "
                     "<em>rarely become punctual</em> deydi — yaxshilanish "
                     "kutilmaydi."),
                    (False, "could be improved if pharmacies sent reminders to late collectors",
                     "<strong>tavsiya, xulosa emas.</strong> Matn nima "
                     "<u>sodir bo'layotganini</u> aytadi; nima qilish kerakligi "
                     "boshqa savol. Eslatmalar ham matnda yo'q."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>Two neighbouring villages were flooded in the same week. In one the "
                "mud was cleared within a month; in the other it lay for a year. The "
                "damage was of similar extent in both, and the money for the clean-up "
                "came from the same district fund and was released on the same day. The "
                "village that cleared quickly had, before the flood, a committee that "
                "met every month to run an entirely unrelated matter — the upkeep of a "
                "shared orchard. What the flood revealed was that "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "the ability to organise quickly was already present in one village and absent in the other before the emergency began.", "is_correct": True},
                {"text": "the second village received less money for its clean-up than the first did.", "is_correct": False},
                {"text": "shared orchards make a village better prepared for natural disasters.", "is_correct": False},
                {"text": "the flood caused more damage in the village that took longer to clear it.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu matn <u>chetlashtirish</u> orqali ishlaydi: zarar bir xil "
                "(chetlashtirildi), pul bir xil va bir kunda (chetlashtirildi). "
                "Qolgan yagona farq — <mark>oldindan mavjud bo'lgan "
                "qo'mita</mark>.</p>"
                "<p>Va e'tibor bering: qo'mita <em>an entirely unrelated "
                "matter</em> bilan shug'ullangan. Ya'ni tayyorgarlik "
                "toshqinga qaratilmagan edi — birga ishlash "
                "<u>ko'nikmasi</u> mavjud edi.</p>"
                + why([
                    (True, "the ability to organise quickly was already present in one village and absent in the other before the emergency began",
                     "<em>before the flood</em> va <em>entirely unrelated</em> "
                     "ikkovi ham shu xulosaga ishlaydi: masala toshqinga "
                     "tayyorgarlikda emas, avvaldan mavjud tashkilotchilikda."),
                    (False, "the second village received less money for its clean-up than the first did",
                     "<strong>matnga zid:</strong> <em>the same district fund … "
                     "released on the same day</em>."),
                    (False, "the flood caused more damage in the village that took longer to clear it",
                     "<strong>matnga zid:</strong> <em>The damage was of similar "
                     "extent in both</em>."),
                    (False, "shared orchards make a village better prepared for natural disasters",
                     "<strong>matndan kuchliroq va kulgili darajada aniq.</strong> "
                     "Bog' — bu misol, sabab emas. Qo'mita har qanday ish bilan "
                     "shug'ullanishi mumkin edi; muhimi — u <u>bor</u> edi."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>An editor comparing two editions of the same 1890s novel found that "
                "the American edition lacks a paragraph present in the British one — the "
                "only passage in which the narrator's income is stated. The American "
                "publisher's surviving correspondence contains no discussion of cuts of "
                "any kind, and the compositor's marks on the surviving proof sheets "
                "indicate that the page was set from copy in which the paragraph was "
                "already missing. The evidence therefore points to the conclusion that "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "the paragraph was already absent from the copy the American publisher worked from.", "is_correct": True},
                {"text": "the American publisher removed the paragraph because of its content.", "is_correct": False},
                {"text": "the author revised the novel after the British edition appeared.", "is_correct": False},
                {"text": "the British edition was printed later than the American one.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki dalil, bitta yo'nalish:</strong> nashriyot "
                "yozishmalarida kesish haqida hech nima yo'q, va terish "
                "belgilariga ko'ra abzats <u>allaqachon</u> yo'q edi. Ikkovi "
                "birga aytadi: kesish <mark>amerikalik nashriyotgacha</mark> "
                "sodir bo'lgan.</p>"
                + why([
                    (True, "the paragraph was already absent from the copy the American publisher worked from",
                     "aynan shuni ikkala dalil ham ko'rsatadi — na ko'proq, "
                     "na kamroq. Kim olib tashlagani noma'lumligicha qoladi, va "
                     "javob ham buni ochiq qoldiradi."),
                    (False, "the author revised the novel after the British edition appeared",
                     "<strong>eng nozik tuzoq.</strong> Bu <u>mumkin</u> — muallif "
                     "ham «nashriyotgacha» toifasiga kiradi. Lekin matn kim "
                     "kesganini aniqlamaydi, shuning uchun muallifni nomlash "
                     "matndan <u>kuchliroq</u> bo'lib qoladi. Xulosa ehtiyotkor "
                     "bo'lishi kerak (73-dars)."),
                    (False, "the American publisher removed the paragraph because of its content",
                     "<strong>matnga zid:</strong> yozishmalarda kesish yo'q va "
                     "nusxa allaqachon abzatssiz kelgan."),
                    (False, "the British edition was printed later than the American one",
                     "<strong>yangi ma'lumot:</strong> nashr sanalari muhokama "
                     "qilinmaydi, va bu abzatsning yo'qligini ham "
                     "tushuntirmaydi."),
                ])
                + TIP.format(
                    "Ikki variant bir yo'nalishda bo'lsa — biri keng, biri aniq — "
                    "deyarli har doim <strong>kengrog'i</strong> to'g'ri. "
                    "Matn «nashriyotgacha» degan darajagacha isbotladi; "
                    "«muallif» degan darajagacha yetmadi.")
            ),
        },

        {
            "rich_text": inf_q(
                "<p>Birds fitted with tracking tags set off from their wintering grounds "
                "within a few days of the same date each year. In some years they leave "
                "when the local temperature, the day length and the abundance of insects "
                "are all still well below the values those measures had reached on the "
                "departure date in other years. Whatever it is that starts the journey, "
                "the tags indicate that it <span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "is not a response to conditions at the place the birds are leaving.", "is_correct": True},
                {"text": "is triggered by the arrival of warm weather at the breeding grounds far to the north.", "is_correct": False},
                {"text": "varies more between individual birds than it does between years.", "is_correct": False},
                {"text": "has shifted earlier in the year as the climate has warmed.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Mantiq:</strong> qushlar deyarli bir xil sanada "
                "jo'naydi. Lekin o'sha sanada mahalliy sharoitlar yildan yilga "
                "<u>juda har xil</u> bo'ladi. Agar sabab mahalliy sharoit "
                "bo'lganida, jo'nash sanasi ham o'sha sharoit bilan birga "
                "siljigan bo'lardi.</p>"
                "<p>Demak: <mark>sabab mahalliy sharoit emas</mark>. Matn "
                "sababning <u>nima ekanini</u> aytmaydi — faqat nima "
                "<u>emasligini</u>.</p>"
                + why([
                    (True, "is not a response to conditions at the place the birds are leaving",
                     "matn isbotlagan yagona narsa, va u inkor shaklida — "
                     "bu Inferences turida tez-tez uchraydi."),
                    (False, "is triggered by the arrival of warm weather at the breeding grounds far to the north",
                     "<strong>eng jozibali tuzoq:</strong> aqlli gipoteza, va u "
                     "«mahalliy emas» degan xulosani to'ldirgandek tuyuladi. "
                     "Lekin qushlar minglab kilometr uzoqdagi ob-havoni "
                     "bila olmaydi, va matn shimoldagi sharoit haqida bir og'iz "
                     "ham gapirmaydi. <u>Yangi ma'lumot.</u>"),
                    (False, "varies more between individual birds than it does between years",
                     "matn <em>within a few days of the same date each year</em> "
                     "deydi — bu yillar orasidagi barqarorlik. Alohida qushlar "
                     "orasidagi farq umuman o'lchanmagan."),
                    (False, "has shifted earlier in the year as the climate has warmed",
                     "<strong>matnga zid:</strong> sana deyarli o'zgarmaydi. "
                     "Iqlim mavzusi tanish bo'lgani uchun bu variant "
                     "jozibali — 72-darsning mavzusi shu."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to complete the text</div><div class="pp-card-back">matnni mantiqan yakunlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to indicate that ~</div><div class="pp-card-back">~ ekanini ko\'rsatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to point to a conclusion</div><div class="pp-card-back">xulosaga olib bormoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a repeat prescription</div><div class="pp-card-back">takroriy retsept</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">punctual</div><div class="pp-card-back">vaqtida keladigan, aniq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">of similar extent</div><div class="pp-card-back">taxminan bir xil hajmda</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a compositor</div><div class="pp-card-back">harf teruvchi (bosmaxonada)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">wintering grounds</div><div class="pp-card-back">qishlash joyi</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Bo'sh joy <strong>har doim matn oxirida</strong>, savol hech "
              "qachon o'zgarmaydi.</li>"
              "<li>Javob matndan <u>chiqadi</u>, matnga hech nima "
              "<u>qo'shmaydi</u>.</li>"
              "<li>Bo'sh joyga yetganda <strong>to'xtang va o'z jumlangizni "
              "ayting</strong>.</li>"
              "<li>Matn ko'pincha faktlarni <u>chetlashtirish</u> orqali ishlaydi: "
              "«zarar bir xil, pul bir xil…» — qolgani javob.</li>"
              "<li>Ikki variant bir yo'nalishda bo'lsa, <strong>kengrog'i</strong> "
              "to'g'ri.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 71
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_INF,
    "title": "SAT R&W 71: The Blank Is Always at the End — Reading Toward It",
    "summary": "Bo'sh joyning o'rni ma'lum bo'lgani uchun matnni boshqacha o'qish "
               "mumkin: har jumla xulosaga nima qo'shayotganini kuzatib borish.",
    "order": 71,
    "blocks": [
        {"rich_text": (
            "<h2>Oxirini bilib o'qish</h2>"
            "<p>Inferences savolining bitta bepul afzalligi bor: siz "
            "<mark>bo'sh joy qayerdaligini oldindan bilasiz</mark>. U har doim "
            "oxirida.</p>"
            "<p>Bu o'qish usulini o'zgartiradi. Siz matnni «nima haqda ekan?» deb "
            "emas, <strong>«bu jumla xulosaga nima qo'shyapti?»</strong> deb "
            "o'qiysiz. Har jumla — dalilning bir bo'lagi, va oxirida ular "
            "yig'iladi.</p>"
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Bo'sh joydan oldingi so'zlarni birinchi o'qing</h3>"
            "<p>63-darsdagi qoida bu yerda ham ishlaydi, va bu yerda u yanada "
            "foydaliroq: bo'sh joydan oldingi bir-ikki so'z javobning "
            "<u>shaklini</u> aytadi.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Bo'sh joydan oldin</th><th>Javob nima bo'ladi</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>therefore · it follows that</em></td>"
              "<td>Faktlardan majburiy chiqadigan xulosa</td></tr>"
              "<tr><td><em>suggests that · indicates that</em></td>"
              "<td>Ehtiyotkor xulosa — «isbotladi» emas</td></tr>"
              "<tr><td><em>only if · unless</em></td>"
              "<td>Shart: xulosa emas, balki <u>kerakli sharoit</u></td></tr>"
              "<tr><td><em>this is because</em></td>"
              "<td>Sabab — oldingi gapni tushuntiradi</td></tr>"
              "<tr><td><em>what the finding shows is that</em></td>"
              "<td>Tadqiqotning ma'nosi, natijasi emas</td></tr>"
              "<tr><td><em>would have to</em></td>"
              "<td>Zaruriy shart: «bu rost bo'lishi uchun nima kerak?»</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<em>only if</em> va <em>would have to</em> — eng ko'p "
                "chalkashtiradiganlari. Ular <u>xulosa</u> emas, "
                "<u>shart</u> so'raydi. «Bu gipoteza to'g'ri bo'lishi uchun "
                "yana nima rost bo'lishi kerak?» Bu boshqa savol, va boshqa "
                "javob turini talab qiladi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + inf_q(
                "<p>A manuscript in a monastery library is written on parchment whose "
                "surface shows the faint traces of an earlier text that was scraped away. "
                "Under ultraviolet light the older writing can be read: it is a "
                "mathematical treatise. Parchment was expensive and was regularly reused, "
                "and a scribe reusing a sheet chose the text he valued less. For the "
                "monastery to have scraped this particular sheet, it would have to be "
                "true that <span class=\"sr-blank\"></span></p>")
            + choices_html([
                "the mathematical treatise was the only copy then in existence.",
                "the monastery valued the text it wrote on the sheet more highly than "
                "the treatise it removed.",
                "the scribe who scraped the sheet was unable to read mathematics.",
                "parchment had become more expensive than it had been in earlier "
                "centuries.",
            ])
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>1-qadam — bo'sh joydan oldingi so'zlar:</strong> "
            "<em>it would have to be true that</em>. Jadvalga ko'ra bu "
            "<mark>xulosa emas, shart</mark>. Savol: «monastir shu varaqni "
            "qirib tashlagan bo'lsa, yana nima rost bo'lishi kerak?»</p>"
            "<p><strong>2-qadam — matnning qoidasi:</strong> "
            "<em>a scribe reusing a sheet chose the text he valued less</em>. "
            "Bu qoida berilgan, va uni faktga qo'llash kerak.</p>"
            "<p><strong>3-qadam — qo'llaymiz:</strong> matematik risola "
            "qirib tashlangan. Qoida bo'yicha, qirib tashlangan matn — "
            "<u>kamroq qadrlangani</u>. Demak ustiga yozilgani "
            "<u>ko'proq</u> qadrlangan.</p>"
            + why([
                (True, "the monastery valued the text it wrote on the sheet more highly than the treatise it removed",
                 "matnda berilgan qoidaning bu holatga to'g'ridan-to'g'ri "
                 "qo'llanishi. <em>would have to be true</em> aynan shuni "
                 "so'raydi: bu shart bo'lmasa, qirish sodir bo'lmasdi."),
                (False, "the scribe who scraped the sheet was unable to read mathematics",
                 "<strong>yangi ma'lumot</strong>, va u qoidaga ham zid: "
                 "qoida <u>qadrlash</u> haqida, <u>o'qiy olish</u> haqida emas. "
                 "Savodsiz kotib ham baholay olardi."),
                (False, "the mathematical treatise was the only copy then in existence",
                 "<strong>matndan kuchliroq.</strong> Nusxalar soni umuman "
                 "muhokama qilinmaydi — va agar bu yagona nusxa bo'lsa, "
                 "monastir uni qadrsiz deb hisoblagani <u>g'alatiroq</u> "
                 "bo'lardi."),
                (False, "parchment had become more expensive than it had been in earlier centuries",
                 "matn pergament qimmat ekanini aytadi, lekin uning "
                 "<u>qimmatlashganini</u> emas. Va narx o'zgarishi shu "
                 "varaqning tanlanishini tushuntirmaydi."),
            ])
            + NOTE.format(
                "Bu shakl — <strong>palimpsest</strong> deb ataladi: qirib "
                "tashlangan va ustiga qayta yozilgan pergament. Ultrabinafsha "
                "nur ostida eski matn o'qilishi mumkin, va bu yo'l bilan "
                "yo'qolgan deb hisoblangan asarlar topilgan. Ammo yana o'sha "
                "qoida: mavzuni bilish javobni bermaydi.")
        )},

        {
            "rich_text": inf_q(
                "<p>Sourdough starters kept in different bakeries develop different "
                "mixtures of yeasts and bacteria, and bakers often say the difference "
                "comes from the air of the room. When several starters were moved to a "
                "single laboratory and fed identical flour on an identical schedule, "
                "each kept the mixture it had arrived with for months. If the bakers' "
                "explanation were correct, the starters would have been expected to "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "become more like one another once they shared the same air.", "is_correct": True},
                {"text": "stop fermenting altogether when moved away from their bakeries.", "is_correct": False},
                {"text": "keep their original mixtures for a much longer period than they did.", "is_correct": False},
                {"text": "develop mixtures that no bakery had recorded before.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'sh joydan oldingi so'zlar:</strong> "
                "<em>If the bakers' explanation were correct, … would have been "
                "expected to</em>. Bu 31-darsdagi shaklning aynan o'zi: "
                "<mark>gipoteza to'g'ri bo'lganda biz nimani ko'rgan "
                "bo'lardik?</mark></p>"
                "<p>Novvoylarning izohi: farq <u>xonaning havosidan</u>. Agar "
                "shunday bo'lsa, bir xil havoga ko'chirilgan xamirturushlar "
                "bir-biriga o'xshab qolishi kerak edi. Lekin ular "
                "o'zgarmadi — demak izoh noto'g'ri.</p>"
                + why([
                    (True, "become more like one another once they shared the same air",
                     "gipotezaning bevosita bashorati. Va u kuzatilganiga zid "
                     "(<em>each kept the mixture it had arrived with</em>) — "
                     "shuning uchun izoh yiqiladi."),
                    (False, "keep their original mixtures for a much longer period than they did",
                     "<strong>teskari:</strong> ular aynan shunday qilishdi. "
                     "Bu havoga bog'liq emaslikning dalili, havo "
                     "gipotezasining bashorati emas."),
                    (False, "stop fermenting altogether when moved away from their bakeries",
                     "<strong>haddan tashqari kuchli</strong> va gipotezadan "
                     "chiqmaydi: havo aralashmani belgilaydi degan da'vo "
                     "achitish butunlay to'xtaydi degani emas."),
                    (False, "develop mixtures that no bakery had recorded before",
                     "<strong>yangi ma'lumot.</strong> Laboratoriya havosi "
                     "yangi mikroorganizmlar keltiradi degan taxmin matnda "
                     "yo'q."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>A city's bus lanes operate only between seven and ten in the morning. "
                "Outside those hours the lane is open to all traffic, and a bus travelling "
                "the route at midday takes about the same time as a car. Between seven "
                "and ten the bus is faster than a car on the same journey by roughly a "
                "third. The operator wants to know whether extending the lane's hours "
                "would speed up the evening service, and the answer depends on whether "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "the evening service is slowed by the same congestion that the morning lane protects buses from.", "is_correct": True},
                {"text": "passengers would prefer to travel in the evening rather than in the morning.", "is_correct": False},
                {"text": "the buses used in the evening are the same models as those used in the morning.", "is_correct": False},
                {"text": "the lane could be extended without reducing the number of parking spaces.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'sh joydan oldingi so'zlar:</strong> "
                "<em>the answer depends on whether</em> — bu ham "
                "<mark>shart</mark> so'raydi, xulosa emas.</p>"
                "<p><strong>Mantiq:</strong> yo'lak ertalab foyda beradi, "
                "chunki ertalab tirbandlik bor (peshinda avtobus mashina bilan "
                "teng). Kechqurun yo'lakni uzaytirish foyda berishi uchun "
                "kechqurun ham <u>xuddi shunday tirbandlik</u> bo'lishi "
                "kerak.</p>"
                + why([
                    (True, "the evening service is slowed by the same congestion that the morning lane protects buses from",
                     "yo'lakning ishlash mexanizmi shu: u avtobusni "
                     "tirbandlikdan ajratadi. Tirbandlik bo'lmasa — "
                     "peshindagidek — yo'lak hech nima bermaydi."),
                    (False, "passengers would prefer to travel in the evening rather than in the morning",
                     "<strong>yangi ma'lumot</strong> va boshqa savol: yo'lovchi "
                     "afzalligi avtobusning <u>tezligiga</u> ta'sir qilmaydi."),
                    (False, "the lane could be extended without reducing the number of parking spaces",
                     "amaliy to'siq bo'lishi mumkin, lekin savol "
                     "<u>tezlashadimi</u> degan savol edi, "
                     "<u>amalga oshiriladimi</u> emas."),
                    (False, "the buses used in the evening are the same models as those used in the morning",
                     "avtobus modeli matnda umuman yo'q, va peshindagi "
                     "taqqoslash sabab tirbandlik ekanini allaqachon "
                     "ko'rsatgan."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>Handwritten shop ledgers from a nineteenth-century town record the "
                "price of bread week by week for forty years. The figures rise sharply in "
                "three separate years. In two of those years the town's newspaper reports "
                "a failed harvest in the surrounding district. For the third, the "
                "newspaper for that year has not survived, though the ledgers of two "
                "neighbouring towns show no rise at all. Taken together, the sources "
                "suggest that the third rise <span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "had a cause local to the town rather than a regional harvest failure.", "is_correct": True},
                {"text": "was caused by a harvest failure that the missing newspaper would have recorded.", "is_correct": False},
                {"text": "was an error made by the shopkeeper who kept the ledger.", "is_correct": False},
                {"text": "lasted longer than either of the other two rises.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Dalillarni yig'amiz:</strong> ikki ko'tarilish "
                "mintaqaviy hosilsizlik bilan mos keladi. Uchinchisida gazeta "
                "yo'q — lekin <u>qo'shni shaharlarning daftarlarida "
                "ko'tarilish yo'q</u>.</p>"
                "<p>Mintaqaviy hosilsizlik qo'shni shaharlarga ham ta'sir "
                "qilardi. Ular jim — demak sabab <mark>mintaqaviy emas, "
                "mahalliy</mark>.</p>"
                + why([
                    (True, "had a cause local to the town rather than a regional harvest failure",
                     "qo'shni daftarlar aynan shu xulosa uchun keltirilgan: "
                     "ular mintaqaviy sababni chetlashtiradi. Gazetaning "
                     "yo'qligi muammo emas — dalil boshqa joydan keldi."),
                    (False, "was caused by a harvest failure that the missing newspaper would have recorded",
                     "<strong>eng jozibali tuzoq:</strong> naqshni davom "
                     "ettiradi (ikkitasi hosilsizlik edi, uchinchisi ham "
                     "shundaydir). Lekin qo'shni daftarlar buni "
                     "<u>rad etadi</u> — va ular matnda aynan shuning uchun "
                     "turibdi."),
                    (False, "was an error made by the shopkeeper who kept the ledger",
                     "<strong>yangi ma'lumot.</strong> Xato ehtimoli hech "
                     "qayerda ko'tarilmaydi, va u boshqa ikki ko'tarilishning "
                     "haqiqiyligini ham shubha ostiga olardi."),
                    (False, "lasted longer than either of the other two rises",
                     "davomiylik umuman o'lchanmagan — matn faqat "
                     "ko'tarilishlarning <u>bo'lganini</u> aytadi."),
                ])
                + TIP.format(
                    "Matnda bir dalil <u>yo'q</u> deyilsa (gazeta saqlanmagan), "
                    "darrov qarang: muallif <strong>o'rniga boshqa dalil "
                    "keltiradimi?</strong> Deyarli har doim keltiradi — va "
                    "o'sha o'rinbosar dalil javobning kalitidir.")
            ),
        },

        {
            "rich_text": inf_q(
                "<p>A museum introduced late opening on Thursday evenings and wants to "
                "know whether it has reached people who would not otherwise have come. "
                "Attendance on Thursday evenings is high. The museum\u2019s total "
                "attendance for the month, however, is almost exactly what it was before "
                "the late openings began. The late openings will have brought in new "
                "visitors only if <span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "the people coming on Thursday evenings are not largely the same people who used to come during the day.", "is_correct": True},
                {"text": "Thursday evening attendance continues to grow over the coming months.", "is_correct": False},
                {"text": "the museum counts its daytime visitors as accurately as its evening ones.", "is_correct": False},
                {"text": "no other museum in the city has introduced late opening as well.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo\u2018sh joydan oldingi so\u2018zlar:</strong> "
                "<em>only if</em> \u2014 <mark>shart</mark> so\u2018raydi.</p>"
                "<p><strong>Muammo:</strong> kechqurun ko\u2018p odam keladi, lekin "
                "oylik jami o\u2018zgarmagan. Bu ikki narsani anglatishi mumkin: "
                "(1) yangi odamlar kelgan va eski kunduzgilar kamaygan \u2014 lekin "
                "unda jami tushishi kerak edi; yoki (2) <u>o\u2018sha odamlar "
                "shunchaki vaqtini almashtirgan</u>.</p>"
                "<p>Demak «yangi tashrifchi» degan da\u2019vo faqat ikkinchi "
                "izoh <u>noto\u2018g\u2018ri</u> bo\u2018lgandagina to\u2018g\u2018ri.</p>"
                + why([
                    (True, "the people coming on Thursday evenings are not largely the same people who used to come during the day",
                     "aynan kerakli shart: agar bular o\u2018sha odamlar bo\u2018lsa, "
                     "kechki gavjumlik shunchaki ko\u2018chirilgan tashrif, yangi "
                     "auditoriya emas \u2014 va o\u2018zgarmagan jami buni aynan "
                     "ko\u2018rsatib turibdi."),
                    (False, "Thursday evening attendance continues to grow over the coming months",
                     "kelajakdagi o\u2018sish <u>hozirgi</u> savolga javob "
                     "bermaydi \u2014 va u ham o\u2018sha odamlarning ko\u2018chishi "
                     "bo\u2018lishi mumkin."),
                    (False, "the museum counts its daytime visitors as accurately as its evening ones",
                     "<strong>yangi ma\u2019lumot:</strong> matn hisob usulini "
                     "shubha ostiga olmaydi. Agar olganda, jami raqamning "
                     "o\u2018zi ham ishonchsiz bo\u2018lardi."),
                    (False, "no other museum in the city has introduced late opening as well",
                     "boshqa muzeylar matnda yo\u2018q. Ular raqobat qilsa ham, "
                     "bu muzeyning o\u2018z tashrifchilari yangimi degan savolga "
                     "ta\u2019sir qilmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">it would have to be true that ~</div><div class="pp-card-back">~ rost bo\'lishi shart bo\'lardi (shart so\'raydi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the answer depends on whether ~</div><div class="pp-card-back">javob ~ ga bog\'liq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">would have been expected to ~</div><div class="pp-card-back">~ qilishi kutilardi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">parchment</div><div class="pp-card-back">pergament (teridan yasalgan yozuv materiali)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to scrape away</div><div class="pp-card-back">qirib tashlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a starter (sourdough)</div><div class="pp-card-back">xamirturush, achitqi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">congestion</div><div class="pp-card-back">tirbandlik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a ledger</div><div class="pp-card-back">hisob daftari</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Bo'sh joy oxirida — demak har jumlani «bu xulosaga nima "
              "qo'shyapti?» deb o'qing.</li>"
              "<li><strong>Bo'sh joydan oldingi so'zlar javobning shaklini "
              "aytadi</strong>.</li>"
              "<li><em>only if · would have to · depends on whether</em> = "
              "<u>shart</u> so'raydi, xulosa emas.</li>"
              "<li><em>If … were correct, … would be expected to</em> = "
              "gipotezaning bashorati.</li>"
              "<li>Bir dalil yo'q deyilsa — muallifning <u>o'rinbosar "
              "dalilini</u> qidiring.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 72
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_INF,
    "title": "SAT R&W 72: Inference vs Outside Knowledge — Staying Inside the 60 Words",
    "summary": "Dunyoda rost bo'lgan gap matnda isbotlanmagan bo'lishi mumkin; mavzu "
               "tanish bo'lganda bu tuzoq eng kuchli ishlaydi.",
    "order": 72,
    "blocks": [
        {"rich_text": (
            "<h2>Bilimingiz sizga qarshi</h2>"
            "<p>4-darsda to'rt tuzoqni sanagandik, va ulardan biri "
            "<strong>tashqi bilim</strong> edi. Inferences turida u boshqa hamma "
            "turdagidan ko'ra kuchliroq ishlaydi.</p>"
            "<p>Sabab oddiy: bu turda sizdan <u>xulosa chiqarish</u> so'ralyapti, "
            "ya'ni matnda so'zma-so'z yozilmagan narsani aytish. Miya buni "
            "«o'ylab top» degan ruxsat deb tushunadi — va o'zi bilgan hamma "
            "narsani ishga soladi.</p>"
            + EXAMP.format(
                "<p style=\"font-size:1.06em;margin:0;\"><strong>Farq shu:</strong><br>"
                "<u>Xulosa</u> — matndagi faktlardan <mark>majburan</mark> "
                "chiqadigan narsa.<br>"
                "<u>Tashqi bilim</u> — matndagi faktlar bilan "
                "<mark>mos keladigan</mark>, lekin ulardan chiqmaydigan narsa.</p>")
            + "<p>Ikkinchisi juda ishonarli tuyuladi, chunki u ko'pincha "
            "<u>rost</u>.</p>"
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Barmoq sinovi</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Variantni tanlang.</strong> "
              "Keyin darrov so'rang: <u>«matnning qaysi so'zlari buni "
              "majburlaydi?»</u></p></div>"
            + "<div class=\"pp-step\"><p><strong>2. O'sha so'zlarni "
              "ko'rsating.</strong> Barmoq bilan, aniq joyga. Ikki-uch so'z "
              "bo'lsin.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Ko'rsatolmasangiz — "
              "javob emas.</strong> «Bu shunday bo'lishi kerak-ku» degan tuyg'u "
              "isbot emas.</p></div>"
            + '</div>'
            + WARN.format(
                "<strong>O'zbek o'quvchi uchun eng xavfli mavzular:</strong> "
                "Orol dengizi, Ipak yo'li, Samarqand va Buxoro, paxta, "
                "Al-Xorazmiy, Navoiy, iqlim o'zgarishi. Bu mavzularda siz "
                "matndan ko'ra ko'proq bilasiz — va aynan shu sizni yiqitadi. "
                "Mavzu tanish bo'lsa, <u>barmoq sinovini ikki marta</u> "
                "qiling.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + inf_q(
                "<p>Between the eighth and the twelfth centuries, paper-making spread "
                "westward from Central Asia along the trade roads, reaching Baghdad, then "
                "Cairo, then the Iberian peninsula. Each of those cities already had a "
                "large body of scribes copying manuscripts on parchment when paper "
                "arrived. Records of book prices in each city fall sharply within two "
                "generations of paper's arrival and not before. The sequence indicates "
                "that <span class=\"sr-blank\"></span></p>")
            + choices_html([
                "paper was invented in Central Asia and carried west by merchants.",
                "the fall in book prices in each city followed the arrival of paper "
                "rather than preceding it.",
                "parchment was no longer used for books once paper became available.",
                "the scribes in those cities resisted the introduction of paper.",
            ])
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p>Bu matn o'zbek o'quvchi uchun ataylab xavfli: Ipak yo'li, "
            "Samarqand qog'ozi, Bag'dod — hammasi tanish. Shuning uchun "
            "<strong>barmoq sinovi</strong>ni qat'iy qo'llaymiz.</p>"
            "<p><strong>Matn nimani aytadi?</strong> Faqat uch narsani: "
            "(1) qog'oz g'arbga tarqaldi; (2) har shaharda oldindan kotiblar bor "
            "edi; (3) kitob narxi qog'oz kelganidan keyin ikki avlod ichida "
            "tushdi — <u>oldin emas</u>.</p>"
            "<p>Uchinchi faktdagi <mark><em>and not before</em></mark> — butun "
            "savolning kaliti. Muallif uni ataylab qo'shgan.</p>"
            + why([
                (True, "the fall in book prices in each city followed the arrival of paper rather than preceding it",
                 "aynan <em>within two generations of paper's arrival <u>and not "
                 "before</u></em> ning qayta ifodasi. Barmoq shu yerga "
                 "qo'yiladi."),
                (False, "paper was invented in Central Asia and carried west by merchants",
                 "<strong>tashqi bilim.</strong> Matn qog'oz "
                 "<u>tarqalganini</u> aytadi, <u>ixtiro qilinganini</u> emas — "
                 "va savdogarlarni umuman eslatmaydi. Bu dunyoda rost "
                 "bo'lishi mumkin, lekin matnda yo'q."),
                (False, "parchment was no longer used for books once paper became available",
                 "<strong>matndan kuchliroq.</strong> Matn pergamentning "
                 "to'xtaganini aytmaydi — u faqat qog'oz kelganini aytadi. "
                 "«Yangi narsa keldi» ≠ «eskisi yo'qoldi»."),
                (False, "the scribes in those cities resisted the introduction of paper",
                 "<strong>yangi ma'lumot.</strong> Kotiblar eslatilgan, lekin "
                 "faqat <u>bor edi</u> deb. Ularning munosabati haqida bir "
                 "og'iz ham yo'q — qarshilik hikoyasini o'quvchi o'zi "
                 "qo'shadi."),
            ])
            + NOTE.format(
                "Diqqat qiling: to'g'ri javob eng <u>kamtarin</u> variant edi. "
                "U shunchaki matndagi vaqt tartibini qaytardi. Qolgan uchtasi "
                "qiziqarliroq hikoya aytardi — va aynan shuning uchun "
                "noto'g'ri.")
        )},

        {
            "rich_text": inf_q(
                "<p>The rivers feeding a large inland sea were diverted for irrigation, "
                "and the sea shrank over the following decades. A dam later separated its "
                "northern basin from its southern one. The northern basin, no longer "
                "draining southward, began to refill, and fish returned to it within a "
                "few years; the southern basin continued to dry. Since neither basin "
                "received more river water than before, the northern recovery indicates "
                "that <span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "retaining the water already reaching the basin was enough to reverse its decline.", "is_correct": True},
                {"text": "the irrigation schemes that diverted the rivers have since been abandoned.", "is_correct": False},
                {"text": "cotton farming is the most water-intensive form of agriculture in the region.", "is_correct": False},
                {"text": "the southern basin will eventually refill once a second dam is built.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu Orol dengizining hikoyasi, va shuning uchun bu savol "
                "o'zbek o'quvchi uchun eng qiyini. Siz bu mavzuda matndan "
                "ancha ko'p bilasiz.</p>"
                "<p><strong>Matn nimani aytadi?</strong> Daryolar burildi; "
                "dengiz qurídi; to'g'on shimolni ajratdi; shimol to'la boshladi; "
                "janub qurishda davom etdi. Va hal qiluvchi bo'lak: "
                "<mark><em>neither basin received more river water than "
                "before</em></mark>.</p>"
                "<p>Ya'ni tiklanish yangi suvdan emas. Yagona o'zgargan narsa — "
                "mavjud suvning <u>oqib ketmasligi</u>.</p>"
                + why([
                    (True, "retaining the water already reaching the basin was enough to reverse its decline",
                     "<em>neither basin received more river water</em> bandi "
                     "aynan shu xulosa uchun qo'yilgan: sabab yangi suv emas, "
                     "borini ushlab qolish."),
                    (False, "the irrigation schemes that diverted the rivers have since been abandoned",
                     "<strong>matnga zid:</strong> agar sug'orish to'xtaganida, "
                     "havzalar ko'proq suv olardi — matn esa olmaganini "
                     "aytadi."),
                    (False, "cotton farming is the most water-intensive form of agriculture in the region",
                     "<strong>tashqi bilim, sof holda.</strong> Paxta bu matnda "
                     "umuman eslatilmagan. Siz uni maktabdan bilasiz — va "
                     "aynan shu sabab bu variant xavfli."),
                    (False, "the southern basin will eventually refill once a second dam is built",
                     "<strong>bashorat, xulosa emas.</strong> Ikkinchi to'g'on "
                     "matnda yo'q, va janubiy havzaning sharoiti shimolnikidan "
                     "farq qilishi mumkin."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>A ninth-century scholar's treatise on calculation describes a system "
                "of ten symbols, including one for nothing, and explains how any quantity "
                "may be written with them. The treatise survives only in Latin "
                "translations made three centuries later. Those translations disagree "
                "with one another about several passages, and in each case where they "
                "disagree, at least one of them uses a term that had no equivalent in the "
                "language of the original. This pattern suggests that the disagreements "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "arose in the process of translation rather than in the original treatise.", "is_correct": True},
                {"text": "show that the scholar's own text was internally inconsistent.", "is_correct": False},
                {"text": "were caused by the translators' poor understanding of mathematics.", "is_correct": False},
                {"text": "prove that the decimal system was invented in Latin-speaking Europe.", "is_correct": False},
            ],
            "explanation": (
                "<p>Yana tanish mavzu — Al-Xorazmiy va o'nlik sanoq. "
                "Barmoq sinovi.</p>"
                "<p><strong>Kalit bo'lak:</strong> <em>in each case where they "
                "disagree, at least one of them uses a term that had no "
                "equivalent in the language of the original</em>. Ya'ni "
                "kelishmovchilik har safar <mark>tilda mavjud bo'lmagan "
                "atama</mark> bilan birga keladi — bu tarjimaning izi.</p>"
                + why([
                    (True, "arose in the process of translation rather than in the original treatise",
                     "naqsh aynan shuni ko'rsatadi: nomuvofiqlik asl matndan "
                     "emas, tilni o'girishdan tug'ilgan."),
                    (False, "show that the scholar's own text was internally inconsistent",
                     "asl matn saqlanmagan — matn shuni ochiq aytadi "
                     "(<em>survives only in Latin translations</em>). Uning "
                     "izchilligi haqida hukm chiqarish mumkin emas."),
                    (False, "were caused by the translators' poor understanding of mathematics",
                     "<strong>yangi ma'lumot va haqorat.</strong> Matn "
                     "tarjimonlarning bilimini baholamaydi — muammo "
                     "<u>tilda</u>, malakada emas."),
                    (False, "prove that the decimal system was invented in Latin-speaking Europe",
                     "<strong>tashqi bilim teskari qilingan</strong>, va "
                     "<em>prove</em> so'zi ham haddan tashqari kuchli "
                     "(73-dars). Matn tizimni risola <u>tasvirlaganini</u> "
                     "aytadi, kim ixtiro qilganini emas."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>A caravanserai excavated on a trade route contains stabling for about "
                "forty animals and sleeping space for roughly the same number of people. "
                "Its storerooms, however, could hold several times the goods that forty "
                "animals could carry in one journey. The building stands a day's travel "
                "from the next such site in either direction. The layout suggests that "
                "the caravanserai <span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "served as a place where goods were held between journeys, not only as overnight lodging.", "is_correct": True},
                {"text": "was the largest building of its kind anywhere on the route.", "is_correct": False},
                {"text": "was used mainly by merchants trading in silk.", "is_correct": False},
                {"text": "was built by the state rather than by private merchants.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Nomuvofiqlikni toping.</strong> Otxona 40 ta hayvon "
                "uchun, yotoqxona 40 kishi uchun — mos. Lekin ombor "
                "<u>bir necha barobar ko'p</u> mol sig'diradi. Bu ortiqcha "
                "hajm nima uchun?</p>"
                "<p>Agar bino faqat tunash uchun bo'lganida, ombor bir kunlik "
                "yukdan katta bo'lishi kerak emas edi. Demak mol u yerda "
                "<mark>qoladi</mark>.</p>"
                + why([
                    (True, "served as a place where goods were held between journeys, not only as overnight lodging",
                     "ombor va hayvon sig'imi orasidagi nomuvofiqlikning "
                     "yagona izohi. <em>not only</em> bo'lagi ham to'g'ri "
                     "— matn tunash funksiyasini inkor qilmaydi."),
                    (False, "was used mainly by merchants trading in silk",
                     "<strong>tashqi bilim.</strong> «Karvonsaroy» so'zi "
                     "Ipak yo'lini eslatadi, lekin matnda birorta mol turi "
                     "nomlanmagan."),
                    (False, "was the largest building of its kind anywhere on the route",
                     "<strong>matndan kuchliroq:</strong> boshqa binolar bilan "
                     "solishtirilmagan. Matn faqat ular <u>bir kunlik "
                     "masofada</u> ekanini aytadi."),
                    (False, "was built by the state rather than by private merchants",
                     "<strong>yangi ma'lumot.</strong> Kim qurgani muhokama "
                     "qilinmaydi — bu ham tarixdan kelgan taxmin."),
                ])
                + TIP.format(
                    "To'rt savolda ham to'g'ri javob <u>matndagi bitta "
                    "g'alati tafsilotni</u> tushuntirdi: «and not before», "
                    "«neither basin received more water», «no equivalent in the "
                    "original», «several times the goods». "
                    "<strong>Matndagi eng g'alati bo'lak deyarli har doim "
                    "javobning kalitidir</strong> — u bekorga yozilmaydi.")
            ),
        },

        {
            "rich_text": inf_q(
                "<p>Honeybee colonies across a region declined sharply over five years. "
                "Beekeepers reported the same rate of loss whether their hives stood "
                "beside orchards, beside grain fields, or in woodland with no farming "
                "within several kilometres. Within each of those settings some apiaries "
                "lost most of their colonies while others lost almost none, and the "
                "difference followed which beekeeper managed them rather than where the "
                "hives stood. The pattern suggests that the main cause of the losses "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "varied between beekeepers rather than between locations.", "is_correct": True},
                {"text": "was the use of pesticides on the surrounding farmland.", "is_correct": False},
                {"text": "affected woodland colonies more severely than those beside orchards.", "is_correct": False},
                {"text": "has since been identified and dealt with by the region\u2019s beekeepers.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu matn <u>chetlashtirish</u> orqali ishlaydi, va u ikki "
                "bosqichli. Birinchi: joy ahamiyatsiz \u2014 bog\u2018, dala va "
                "o\u2018rmonda yo\u2018qotish bir xil. Ikkinchi: har bir joy ichida "
                "farq bor, va u <mark>asalarichiga ergashadi</mark>.</p>"
                + why([
                    (True, "varied between beekeepers rather than between locations",
                     "matnning oxirgi jumlasi aynan shuni aytadi: "
                     "<em>followed which beekeeper managed them rather than where "
                     "the hives stood</em>."),
                    (False, "was the use of pesticides on the surrounding farmland",
                     "<strong>tashqi bilim, eng kuchli shaklda.</strong> Bu \u2014 "
                     "asalarilar yo\u2018qolishining mashhur izohi, va ko\u2018pchilik "
                     "uni biladi. Lekin matn uni <u>ataylab rad etadi</u>: "
                     "dehqonchilik yo\u2018q o\u2018rmonda ham yo\u2018qotish bir xil "
                     "bo\u2018lgan."),
                    (False, "affected woodland colonies more severely than those beside orchards",
                     "<strong>matnga zid:</strong> <em>the same rate of loss</em> "
                     "\u2014 uchala joyda ham bir xil."),
                    (False, "has since been identified and dealt with by the region\u2019s beekeepers",
                     "<strong>yangi ma\u2019lumot.</strong> Matn sababni "
                     "topilgan deb aytmaydi \u2014 u faqat sabab qayerda "
                     "<u>emasligini</u> ko\u2018rsatadi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to precede</div><div class="pp-card-back">oldin kelmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to retain water</div><div class="pp-card-back">suvni ushlab qolmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to reverse a decline</div><div class="pp-card-back">pasayishni orqaga qaytarmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a basin</div><div class="pp-card-back">havza</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to arise in the process of ~</div><div class="pp-card-back">~ jarayonida paydo bo\'lmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">stabling</div><div class="pp-card-back">otxona, hayvonlar uchun joy</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">lodging</div><div class="pp-card-back">tunash joyi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">internally inconsistent</div><div class="pp-card-back">o\'z ichida ziddiyatli</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><u>Xulosa</u> matndan <strong>majburan chiqadi</strong>; "
              "<u>tashqi bilim</u> unga shunchaki <strong>mos keladi</strong>.</li>"
              "<li><strong>Barmoq sinovi:</strong> matnning qaysi so'zlari buni "
              "majburlaydi? Ko'rsatolmasangiz — javob emas.</li>"
              "<li>Tanish mavzuda (Orol, Ipak yo'li, Al-Xorazmiy) sinovni "
              "<u>ikki marta</u> qiling.</li>"
              "<li>To'g'ri javob odatda eng <strong>kamtarin</strong> variant "
              "bo'ladi; qiziqarli hikoya aytgani — tuzoq.</li>"
              "<li>Matndagi eng <strong>g'alati tafsilot</strong> javobning "
              "kalitidir.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 73
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_INF,
    "title": "SAT R&W 73: Hedged Conclusions — may, suggests, is likely to",
    "summary": "Xulosaning kuchi dalilning kuchiga teng bo'lishi kerak: bitta tajriba "
               "«mumkin», barqaror naqsh «ehtimol», mantiqiy zarurat «albatta».",
    "order": 73,
    "blocks": [
        {"rich_text": (
            "<h2>Dalil qancha ko'tarsa — shuncha</h2>"
            "<p>Inferences turida ikki variant ko'pincha <u>bir xil narsani</u> "
            "aytadi va faqat <mark>kuchi</mark> bilan farq qiladi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>… <u>may</u> help patients remember advice</em><br>"
                "<em>… <u>has been shown to</u> help patients remember advice</em></p>")
            + "<p>Ikkalasi ham mazmunan to'g'ri tuyuladi. Lekin faqat bittasi "
            "matndagi dalilga <strong>tengdir</strong>. Bu turdagi eng ko'p "
            "yo'qotiladigan ball aynan shu yerda.</p>"
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Kuch shkalasi</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Matndagi dalil</th><th>Javob shunday bo'lishi kerak</th></tr></thead>"
              "<tbody>"
              "<tr><td>Bitta holat, kichik tajriba, takrorlanmagan</td>"
              "<td><em>may · could · in this case</em></td></tr>"
              "<tr><td>Barqaror naqsh, ko'p kuzatuv</td>"
              "<td><em>suggests · is likely · tends to</em></td></tr>"
              "<tr><td>To'liq ro'yxat, hech qanday istisnosiz</td>"
              "<td><em>is · are · every</em> — kuchli da'vo o'rinli</td></tr>"
              "<tr><td>Mantiqiy zarurat (boshqa imkon yo'q)</td>"
              "<td><em>must · cannot</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + "<p>Va matnning o'zidagi so'zlarni o'qing — ular kuchni "
            "<u>oldindan cheklaydi</u>:</p>"
            + "<ul>"
              "<li><em>in a single trial · was not repeated · a small sample</em> "
              "→ javob ehtiyotkor bo'lsin;</li>"
              "<li><em>in every case recorded · none has been found · the survey "
              "covered the whole</em> → kuchli javob o'rinli;</li>"
              "<li><em>if … then</em> → mantiqiy zarurat, <em>must</em> "
              "mumkin.</li>"
              "</ul>"
            + WARN.format(
                "Tuzoq <u>ikki tomonga</u> ham ishlaydi. Haddan tashqari kuchli "
                "javob (<em>proves · always · never · the most</em>) eng ko'p "
                "uchraydi. Lekin <strong>haddan tashqari kuchsiz</strong> javob "
                "ham tuzoq: matn to'liq ro'yxat bergan bo'lsa, "
                "«balki biroz ko'proqdir» degan variant dalilni "
                "behuda qiladi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + inf_q(
                "<p>In a trial at one hospital, patients given a printed summary of their "
                "consultation recalled more of the advice a week later than patients who "
                "received none. Fifty-two patients took part. The trial has not been "
                "repeated, and the two groups were not matched for age, which is known to "
                "affect recall. On this evidence, printed summaries "
                "<span class=\"sr-blank\"></span></p>")
            + choices_html([
                "have been shown to improve how much advice patients remember.",
                "may improve how much advice patients remember, though this trial is too "
                "small and too uncontrolled to establish it.",
                "are the most effective means available of improving patient recall.",
                "have no measurable effect on how much advice patients remember.",
            ])
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>Matn kuchni o'zi cheklaydi.</strong> Uchta cheklov "
            "sanalgan: <em>one hospital</em>, <em>fifty-two patients</em>, "
            "<em>has not been repeated</em>, va ustiga <em>not matched for "
            "age</em>.</p>"
            "<p>Muallif bu cheklovlarni bekorga yozmagan. Ular javobning "
            "kuchini <mark>eng past darajaga</mark> tushiradi: "
            "<em>may</em>.</p>"
            + why([
                (True, "may improve how much advice patients remember, though this trial is too small and too uncontrolled to establish it",
                 "yagona variant dalilning kuchiga teng: ta'sir "
                 "<u>bo'lishi mumkin</u>, lekin bu tajriba uni isbotlamaydi. "
                 "Va u matndagi to'rtala cheklovni ham hisobga oladi."),
                (False, "have been shown to improve how much advice patients remember",
                 "<strong>haddan tashqari kuchli.</strong> <em>have been "
                 "shown</em> = isbotlangan. Takrorlanmagan, yosh bo'yicha "
                 "moslashtirilmagan 52 kishilik tajriba hech nimani "
                 "isbotlamaydi. Eng ko'p tanlanadigan noto'g'ri javob."),
                (False, "are the most effective means available of improving patient recall",
                 "<strong>ikki barobar kuchli:</strong> nafaqat isbotlangan, "
                 "balki eng yaxshisi. Matn boshqa usullarni umuman "
                 "solishtirmaydi."),
                (False, "have no measurable effect on how much advice patients remember",
                 "<strong>teskari tomonga kuchli.</strong> Tajriba farq "
                 "topdi — u ishonchsiz bo'lishi mumkin, lekin «ta'sir yo'q» "
                 "degan xulosa ham xuddi shunday asossiz."),
            ])
            + TIP.format(
                "Matnda cheklovlar sanalgan bo'lsa — <em>small · not repeated · "
                "preliminary · a single</em> — javob deyarli har doim "
                "<strong>eng ehtiyotkor</strong> variant bo'ladi. Muallif "
                "o'sha so'zlarni sizga yordam berish uchun yozgan.")
        )},

        {
            "rich_text": inf_q(
                "<p>A survey of this coast recorded 340 shipwrecks. The survey covered "
                "the entire coastline, and wrecks here have been registered by the "
                "harbour authority whenever they occur since the register opened. Every "
                "one of the 340 lies within two kilometres of a headland; none has been "
                "found on the long open stretches between them. On this evidence, "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "the danger of wreck on this coast is concentrated near its headlands.", "is_correct": True},
                {"text": "headlands may possibly be somewhat more hazardous than open coast.", "is_correct": False},
                {"text": "headlands are the most dangerous coastal feature anywhere in the world.", "is_correct": False},
                {"text": "ships have deliberately avoided the open stretches between headlands.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu safar dalil <u>kuchli</u>: to'liq qirg'oq qamrab olingan, "
                "hamma halokat ro'yxatga olingan, va 340 dan "
                "<mark>bittasi ham</mark> ochiq joyda emas. Bunday dalil "
                "kuchli xulosani ko'taradi.</p>"
                + why([
                    (True, "the danger of wreck on this coast is concentrated near its headlands",
                     "to'liq ro'yxat + istisnosiz naqsh = qat'iy da'vo o'rinli. "
                     "Va u <em>this coast</em> bilan chegaralangan — matn "
                     "isbotlagan doiraning aynan o'zi."),
                    (False, "headlands may possibly be somewhat more hazardous than open coast",
                     "<strong>haddan tashqari kuchsiz</strong> — va bu darsning "
                     "ikkinchi tuzog'i. <em>may possibly … somewhat</em> uchta "
                     "yumshatuvchi so'z; 340 dan 340 tasi shundan ancha "
                     "ko'proqni ko'taradi. Dalilni behuda qiladi."),
                    (False, "headlands are the most dangerous coastal feature anywhere in the world",
                     "<strong>doirasi haddan tashqari keng:</strong> so'rov "
                     "bitta qirg'oqni qamragan. Dunyo haqidagi da'vo matndan "
                     "chiqmaydi."),
                    (False, "ships have deliberately avoided the open stretches between headlands",
                     "<strong>muqobil izoh, dalilsiz.</strong> Ochiq joylarda "
                     "halokat yo'qligi ular xavfsiz ekanini ham, kemalar u "
                     "yerdan yurmaganini ham anglatishi mumkin — matn "
                     "ikkinchisini ko'rsatmaydi."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>A ledger was kept in a locked room to which exactly three people held "
                "keys: the manager, the auditor and the night porter. Entries in the "
                "ledger were altered at some point between Friday evening and Monday "
                "morning. The manager was abroad from Thursday until the following "
                "Tuesday, and the auditor was in hospital for the whole of that weekend. "
                "If the alteration was made by a keyholder, then it "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "must have been made by the night porter.", "is_correct": True},
                {"text": "was probably made by the night porter, though the others cannot be entirely ruled out.", "is_correct": False},
                {"text": "may have been made by somebody who did not hold a key.", "is_correct": False},
                {"text": "shows that the night porter had a reason to alter the ledger.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bu mantiqiy zarurat</strong> — shkalaning eng yuqori "
                "pog'onasi. Uchta kalit egasi bor; ikkitasi jismonan "
                "imkonsiz holatda; savolning o'zi <em>If the alteration was "
                "made by a keyholder</em> deb shartni qo'yib bergan.</p>"
                "<p>Uchtadan ikkitasi chiqarilsa, bittasi qoladi. "
                "<mark>Boshqa imkon yo'q</mark> — demak <em>must</em>.</p>"
                + why([
                    (True, "must have been made by the night porter",
                     "<em>must</em> aynan o'rinli: shart berilgan bo'lsa, "
                     "chetlashtirish to'liq va yagona nomzod qoladi."),
                    (False, "was probably made by the night porter, though the others cannot be entirely ruled out",
                     "<strong>haddan tashqari kuchsiz.</strong> Boshqalar "
                     "<u>chetlashtirilgan</u> — biri chet elda, biri "
                     "kasalxonada. «Istisno qilib bo'lmaydi» degani matnga "
                     "zid."),
                    (False, "may have been made by somebody who did not hold a key",
                     "<strong>shartni buzadi:</strong> savol "
                     "<em>If … by a keyholder</em> deb boshlangan. Shart "
                     "berilgan savolda shartdan chiqib ketib bo'lmaydi."),
                    (False, "shows that the night porter had a reason to alter the ledger",
                     "<strong>yangi ma'lumot:</strong> imkoniyat sabab emas. "
                     "Kim qilgani va nega qilgani — ikki xil savol."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>A single fragment of woven cloth was recovered from a waterlogged pit "
                "and dated to the fourth millennium BCE — older than any other textile so "
                "far found in the region. Waterlogging preserves plant fibre almost "
                "indefinitely; on dry sites, which make up the great majority of those "
                "excavated in the region, fibre decays within a few centuries. The "
                "fragment therefore shows that weaving "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "was already being practised in the region by that date.", "is_correct": True},
                {"text": "began in the region at about that date.", "is_correct": False},
                {"text": "was more widespread in the fourth millennium BCE than it later became.", "is_correct": False},
                {"text": "was the only craft practised in the region at that time.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kalit bo'lak:</strong> quruq joylarda tola bir necha "
                "asrda chiriydi, va <em>the great majority</em> qazishmalar "
                "aynan quruq joylarda. Demak eski matolar "
                "<mark>bo'lgan bo'lsa ham saqlanmagan bo'lardi</mark>.</p>"
                "<p>Ya'ni: <u>topilgan eng eskisi</u> ≠ <u>mavjud bo'lgan eng "
                "eskisi</u>.</p>"
                + why([
                    (True, "was already being practised in the region by that date",
                     "<em>by that date</em> — «o'sha sanaga kelib». Bu "
                     "topilma ko'taradigan aniq da'vo: shu sanada to'quv bor "
                     "edi. Undan oldin ham bo'lganmi — topilma "
                     "aytmaydi."),
                    (False, "began in the region at about that date",
                     "<strong>haddan tashqari kuchli</strong>, va matn buni "
                     "aynan rad etish uchun saqlanish haqidagi jumlani "
                     "yozgan. Eng eski <u>topilma</u> boshlanish sanasi "
                     "emas."),
                    (False, "was more widespread in the fourth millennium BCE than it later became",
                     "<strong>yangi ma'lumot:</strong> keyingi davrlar bilan "
                     "solishtirish yo'q. Bitta parcha tarqalganlik haqida hech "
                     "nima demaydi."),
                    (False, "was the only craft practised in the region at that time",
                     "<strong>haddan tashqari kuchli va bema'ni:</strong> "
                     "boshqa hunarlar umuman muhokama qilinmaydi."),
                ])
                + NOTE.format(
                    "«Eng eski topilgan ≠ eng eski mavjud bo'lgan» — bu "
                    "arxeologiya va paleontologiyada doimiy qoida, va SAT uni "
                    "juda yaxshi ko'radi. Matn saqlanish sharoiti haqida "
                    "gapirsa (<em>waterlogged · preserved only where · decays</em>), "
                    "javob deyarli har doim <u>ehtiyotkor</u> shaklda "
                    "bo'ladi.")
            ),
        },

        {
            "rich_text": inf_q(
                "<p>Records exist for eleven winters at a mountain pass. In each of those "
                "eleven the pass was closed by snow for at least three weeks, and in nine "
                "of them for more than six. No winter in the record has passed without a "
                "closure. An engineer planning a route intended to stay open all year "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "should expect a closure every winter unless the route avoids the pass.", "is_correct": True},
                {"text": "can rely on the closure lasting more than six weeks each winter.", "is_correct": False},
                {"text": "has no basis in the records for predicting closures at all.", "is_correct": False},
                {"text": "may find that some winters bring no closure to the pass.", "is_correct": False},
            ],
            "explanation": (
                "<p>Matnda ikkita <u>har xil kuchdagi</u> fakt bor, va ularni "
                "aralashtirmaslik kerak:</p>"
                "<ul>"
                "<li><em>each of those eleven … at least three weeks</em> — "
                "<strong>istisnosiz</strong>;</li>"
                "<li><em>in nine of them … more than six</em> — "
                "<strong>ko'pchilikda, hammasida emas</strong>.</li>"
                "</ul>"
                + why([
                    (True, "should expect a closure every winter unless the route avoids the pass",
                     "birinchi faktga tayanadi, va u istisnosiz — shuning uchun "
                     "<em>every winter</em> o'rinli. <em>unless the route "
                     "avoids the pass</em> bo'lagi ham to'g'ri chegara."),
                    (False, "can rely on the closure lasting more than six weeks each winter",
                     "<strong>ikkinchi faktni birinchisining kuchida "
                     "aytadi:</strong> o'n bir qishdan to'qqiztasi, "
                     "hammasi emas. <em>each winter</em> — ikki qishda "
                     "noto'g'ri."),
                    (False, "may find that some winters bring no closure to the pass",
                     "<strong>matnga zid:</strong> <em>No winter in the record "
                     "has passed without a closure.</em>"),
                    (False, "has no basis in the records for predicting closures at all",
                     "<strong>haddan tashqari kuchsiz</strong> — o'n bir yillik "
                     "istisnosiz yozuv juda yaxshi asos. Dalilni behuda "
                     "qiladi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to establish (a claim)</div><div class="pp-card-back">(da\'voni) isbotlab qo\'ymoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">has been shown to ~</div><div class="pp-card-back">~ ekani isbotlangan (kuchli)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to rule out</div><div class="pp-card-back">istisno qilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">uncontrolled (of a trial)</div><div class="pp-card-back">nazorat guruhisiz, sharoitlari tenglashtirilmagan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">waterlogged</div><div class="pp-card-back">suvga to\'yingan (tuproq)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to decay</div><div class="pp-card-back">chirimoq, parchalanmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">by that date</div><div class="pp-card-back">o\'sha sanaga kelib (ehtiyotkor shakl)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to be concentrated near ~</div><div class="pp-card-back">~ atrofida to\'plangan bo\'lmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Xulosaning kuchi dalilning kuchiga <strong>teng</strong> "
              "bo'lsin.</li>"
              "<li>Cheklovlar sanalgan bo'lsa (<em>small · not repeated</em>) — "
              "javob <u>eng ehtiyotkori</u>.</li>"
              "<li>To'liq ro'yxat, istisnosiz naqsh — <u>kuchli</u> javob "
              "o'rinli.</li>"
              "<li>Shart berilgan bo'lsa (<em>If …</em>) — <em>must</em> "
              "mumkin.</li>"
              "<li><strong>Kuchsiz javob ham tuzoq:</strong> «may possibly "
              "somewhat» dalilni behuda qiladi.</li>"
              "<li>Saqlanish sharoiti eslatilsa: <u>eng eski topilgan ≠ eng "
              "eski bo'lgan</u>.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 74
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_INF,
    "title": "SAT R&W 74: Inferences — Mixed Practice",
    "summary": "Oltita xulosa savoli, barcha tuzoq turlari aralash, imtihon "
               "tezligida: 70–73-darslarni soatga qarshi mustahkamlash.",
    "order": 74,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy amaliyot</h2>"
            "<p>Oltita savol. Hammasi bir xil savol matni bilan keladi, lekin "
            "ichida turli tuzoqlar bor: tashqi bilim, haddan tashqari kuchli "
            "xulosa, shart savoli, matnga zid variant.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Har savolda shu tartib:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li>Bo'sh joydan oldingi so'zlarni o'qing (71-dars).</li>"
                "<li>Bo'sh joyga yetganda <u>to'xtang va o'z jumlangizni "
                "ayting</u> (70-dars).</li>"
                "<li>Har variantga <u>barmoq sinovi</u>: qaysi so'zlar buni "
                "majburlaydi? (72-dars)</li>"
                "<li>Kuchini tekshiring: dalil shuncha ko'taradimi? "
                "(73-dars)</li>"
                "</ol>")
            + "<p>Taymer: <strong>7 daqiqa</strong> (6 × 70 soniya).</p>"
            + '<span class="sr-time">⏱ 6 savol · 7 daqiqa</span>'
        )},

        {
            "rich_text": inf_q(
                "<p>Nurses on a night shift were asked to record how long they thought "
                "each of their tasks had taken. Their estimates were close to the "
                "measured times for tasks lasting under a minute, and grew steadily less "
                "accurate for longer ones, always in the same direction: the longer the "
                "task, the more it was underestimated. The pattern held for every nurse "
                "in the study. The results suggest that the error "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "is a systematic feature of the estimating rather than a difference between individual nurses.", "is_correct": True},
                {"text": "arises because nurses on night shifts are more tired than those on day shifts.", "is_correct": False},
                {"text": "would disappear if nurses were given clocks to check while working.", "is_correct": False},
                {"text": "was larger for some nurses than the measurement error itself.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki kalit ibora:</strong> <em>always in the same "
                "direction</em> va <em>held for every nurse</em>. Xato "
                "tasodifiy ham emas, shaxsga bog'liq ham emas — u "
                "<mark>tizimli</mark>.</p>"
                + why([
                    (True, "is a systematic feature of the estimating rather than a difference between individual nurses",
                     "ikkala iborani ham ishlatadi: bir yo'nalishda "
                     "(tizimli) va hamma hamshirada (shaxsiy emas)."),
                    (False, "arises because nurses on night shifts are more tired than those on day shifts",
                     "<strong>tashqi bilim.</strong> Kunduzgi smena bilan "
                     "solishtiruv umuman yo'q — faqat tungi smena "
                     "o'lchangan."),
                    (False, "would disappear if nurses were given clocks to check while working",
                     "<strong>yangi ma'lumot va bashorat.</strong> Soat, "
                     "aralashuv yoki tuzatish matnda yo'q."),
                    (False, "was larger for some nurses than the measurement error itself",
                     "o'lchov xatosi muhokama qilinmaydi, va matn "
                     "hamshiralar orasidagi farqni emas, "
                     "<u>o'xshashlikni</u> ta'kidlaydi."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>A composer's notebooks contain sketches for a symphony in a hand that "
                "becomes steadily less steady across the pages, and the sketches break off "
                "in the middle of the final movement. Those last pages are dated in the same "
                "year as a letter in which he describes losing the use of his right hand. A "
                "copyist's fair manuscript of the finished symphony exists and is dated two "
                "years later. For both documents to be genuine, it would have to be the case "
                "that <span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "the symphony was finished after the composer had lost the use of his right hand.", "is_correct": True},
                {"text": "the composer recovered the use of his right hand within two years.", "is_correct": False},
                {"text": "the copyist wrote the symphony himself and attributed it to the composer.", "is_correct": False},
                {"text": "the letter describing the loss of his hand was written much later than its date suggests.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'sh joydan oldingi so'zlar:</strong> "
                "<em>it would have to be the case that</em> — 71-darsga ko'ra "
                "bu <mark>shart</mark>, xulosa emas.</p>"
                "<p><strong>Ziddiyat:</strong> qo'l ishlamay qolgan, lekin ikki "
                "yildan keyin tugallangan asar bor. Ikkala hujjat ham haqiqiy "
                "bo'lishi uchun asar <u>qo'l bilan yozishdan boshqa yo'l</u> "
                "bilan tugallangan bo'lishi kerak — aytib turib, chap qo'l "
                "bilan, yoki boshqacha.</p>"
                + why([
                    (True, "the symphony was finished after the composer had lost the use of his right hand",
                     "eskizlar oxirgi qismning o'rtasida uzilgan, ya'ni asar o'sha "
                     "paytda tugallanmagan edi; tugallangan nusxa esa ikki yildan "
                     "keyin mavjud. Ikkala hujjat ham haqiqiy bo'lsa, ish qo'l "
                     "ishlamay qolganidan <u>keyin</u> davom etgan. Qanday davom "
                     "etgani — chap qo'l bilanmi, aytib turibmi — ochiq qoladi, va "
                     "javob ham buni ochiq qoldiradi."),
                    (False, "the composer recovered the use of his right hand within two years",
                     "<strong>bitta mumkin yo'l, lekin yagona emas</strong> — u chap "
                     "qo'l bilan yozgan yoki aytib turgan bo'lishi ham mumkin. "
                     "<em>would have to be</em> <u>majburiy</u> shartni so'raydi, "
                     "mumkin bo'lganini emas."),
                    (False, "the copyist wrote the symphony himself and attributed it to the composer",
                     "<strong>ikkala hujjatning haqiqiyligini buzadi</strong> — "
                     "savolning sharti esa ikkovi ham haqiqiy deb qo'ygan."),
                    (False, "the letter describing the loss of his hand was written much later than its date suggests",
                     "yana shartni buzadi: xat haqiqiy bo'lsa, sanasi ham "
                     "haqiqiy."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>A single leaf impression in fine-grained rock preserves the outline "
                "of a flowering plant older than any other flowering-plant fossil from "
                "the continent. Fine-grained rock of this kind forms only in still water "
                "and is rare in the sequence; the coarser rocks that make up most of it "
                "preserve nothing so delicate. The impression therefore establishes that "
                "flowering plants <span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "were present on the continent at least as early as the rock that holds the impression.", "is_correct": True},
                {"text": "first appeared on the continent at the time the impression was formed.", "is_correct": False},
                {"text": "were rare on the continent before the impression was formed.", "is_correct": False},
                {"text": "grew only beside still water during that period.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu 73-darsdagi mato savolining aynan qardoshi, va bir xil "
                "qoida ishlaydi: matn <u>saqlanish sharoiti</u> haqida "
                "gapiryapti (<em>fine-grained rock … is rare</em>).</p>"
                "<p>Nozik jinsda saqlanadi, qo'polida yo'q. Demak eski gullar "
                "bo'lgan bo'lsa ham, <mark>iz qoldirmagan bo'lardi</mark>.</p>"
                + why([
                    (True, "were present on the continent at least as early as the rock that holds the impression",
                     "<em>at least as early as</em> — topilma ko'taradigan aniq "
                     "chegara. Undan oldinroq ham bo'lgan bo'lishi mumkin, "
                     "va javob buni ochiq qoldiradi."),
                    (False, "first appeared on the continent at the time the impression was formed",
                     "<strong>haddan tashqari kuchli.</strong> Eng eski "
                     "<u>topilma</u> paydo bo'lish sanasi emas — va matn "
                     "aynan buni ogohlantirish uchun jins haqida yozgan."),
                    (False, "were rare on the continent before the impression was formed",
                     "<strong>yangi ma'lumot:</strong> kam uchraydigani "
                     "<u>jins</u>, o'simlik emas. Matndagi <em>rare</em> "
                     "so'ziga yopishgan tuzoq."),
                    (False, "grew only beside still water during that period",
                     "<strong>saqlanish sharoitini yashash sharoiti bilan "
                     "adashtirish.</strong> Tinch suv — bu o'simlik "
                     "<u>saqlanadigan</u> joy, o'sadigan joy emas. Barg suvga "
                     "tushib qolgan bo'lishi mumkin."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>A dictionary compiled in the 1750s glosses a common word with a "
                "definition that no reader today would recognise. The same compiler's "
                "private letters, written across the same decade, use the word in the "
                "modern sense throughout. The dictionary drew its examples from printed "
                "books, most of them published fifty years or more before it was "
                "compiled. The discrepancy suggests that the dictionary's definition "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "recorded an older written usage rather than the speech of the compiler's own day.", "is_correct": True},
                {"text": "was an error that the compiler failed to notice.", "is_correct": False},
                {"text": "shows that the word changed its meaning during the 1750s.", "is_correct": False},
                {"text": "was copied without acknowledgement from an earlier dictionary.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Uch fakt:</strong> lug'atdagi ma'no eski; tuzuvchining "
                "o'z xatlarida ma'no zamonaviy; lug'at misollari "
                "<u>ellik yil va undan eski</u> kitoblardan olingan.</p>"
                "<p>Uchinchi fakt ikkinchisini tushuntiradi: tuzuvchi xato "
                "qilmagan — u <mark>boshqa manbani yozib olgan</mark>.</p>"
                + why([
                    (True, "recorded an older written usage rather than the speech of the compiler's own day",
                     "manbalar haqidagi jumla aynan shu xulosa uchun turibdi. "
                     "Va u tuzuvchining xatlaridagi ziddiyatni ham "
                     "tushuntiradi."),
                    (False, "was an error that the compiler failed to notice",
                     "<strong>matn buni chetlashtiradi:</strong> manbalar eski "
                     "edi, ya'ni ta'rif o'z manbasiga sodiq. Bu xato emas, "
                     "usulning oqibati."),
                    (False, "shows that the word changed its meaning during the 1750s",
                     "<strong>vaqtni siqib yuboradi:</strong> farq lug'at bilan "
                     "ellik yil oldingi kitoblar orasida, o'sha o'n yillik "
                     "ichida emas."),
                    (False, "was copied without acknowledgement from an earlier dictionary",
                     "<strong>yangi ma'lumot va ayblov:</strong> matn "
                     "misollar <u>kitoblardan</u> olinganini aytadi, boshqa "
                     "lug'atdan emas."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>In a pilot scheme at one school, pupils who were given a free "
                "breakfast scored higher on an attention test at eleven o'clock than "
                "pupils who were not. Twenty-eight pupils took part; the scheme ran for "
                "three weeks and has not been repeated, and pupils chose for themselves "
                "whether to take the breakfast. On this evidence the scheme "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "may have improved attention, though the study is too small and its groups too self-selected to show it.", "is_correct": True},
                {"text": "has been shown to improve pupils' attention in the late morning.", "is_correct": False},
                {"text": "should be introduced in every school in the district.", "is_correct": False},
                {"text": "had no effect on the attention of the pupils who took part.", "is_correct": False},
            ],
            "explanation": (
                "<p>73-darsning kuch shkalasi. Matn <u>uchta</u> cheklov "
                "sanaydi: 28 o'quvchi, uch hafta, takrorlanmagan — va ustiga "
                "eng jiddiysi: <em>pupils chose for themselves</em>, ya'ni "
                "guruhlar <mark>o'zini o'zi tanlagan</mark>.</p>"
                "<p>Nonushtani tanlagan o'quvchilar boshqa jihatlardan ham "
                "farq qilishi mumkin. Demak javob eng ehtiyotkori.</p>"
                + why([
                    (True, "may have improved attention, though the study is too small and its groups too self-selected to show it",
                     "dalilning kuchiga teng, va o'z-o'zini tanlash "
                     "muammosini ham nomlaydi."),
                    (False, "has been shown to improve pupils' attention in the late morning",
                     "<strong>haddan tashqari kuchli:</strong> "
                     "<em>has been shown</em> = isbotlangan. Uch cheklov buni "
                     "ko'tarmaydi."),
                    (False, "should be introduced in every school in the district",
                     "<strong>tavsiya, xulosa emas</strong> — va u zaif "
                     "dalildan chiqarilgan."),
                    (False, "had no effect on the attention of the pupils who took part",
                     "<strong>teskari tomonga kuchli:</strong> farq kuzatilgan. "
                     "U ishonchsiz, lekin «ta'sir yo'q» ham asossiz."),
                ])
            ),
        },

        {
            "rich_text": inf_q(
                "<p>Two villages on the same river drew their drinking water from it "
                "until a well was sunk in one of them. Cases of a waterborne illness fell "
                "in the village with the well and stayed at their previous level in the "
                "other. The river was tested and found to carry the organism responsible; "
                "the well water did not. For the well to explain the fall, it would also "
                "have to be true that <span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "the villagers with the well actually stopped drinking the river water.", "is_correct": True},
                {"text": "the two villages were of a similar size before the well was sunk.", "is_correct": False},
                {"text": "the organism responsible cannot survive in well water.", "is_correct": False},
                {"text": "the second village would benefit from a well of its own.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'sh joydan oldingi so'zlar:</strong> "
                "<em>it would <u>also</u> have to be true that</em> — shart "
                "so'ralyapti, va <em>also</em> so'zi «yana bir narsa" \
                " kerak» deydi.</p>"
                "<p><strong>Zanjir:</strong> quduq qazildi → daryo suvi "
                "ichilmay qo'yildi → kasallik kamaydi. O'rtadagi bo'g'in "
                "matnda <u>aytilmagan</u> — quduqning mavjudligi odamlarning "
                "undan foydalanishini anglatmaydi.</p>"
                + why([
                    (True, "the villagers with the well actually stopped drinking the river water",
                     "aynan yetishmayotgan bo'g'in. Quduq bo'lsa-yu, odamlar "
                     "baribir daryodan ichsa, tushuntirish qulaydi."),
                    (False, "the organism responsible cannot survive in well water",
                     "<strong>matn buni allaqachon aytgan:</strong> "
                     "<em>the well water did not</em> carry the organism. "
                     "Yangi shart emas, takror."),
                    (False, "the two villages were of a similar size before the well was sunk",
                     "hajm foydali bo'lishi mumkin, lekin kasallik "
                     "<u>darajasi</u> solishtirilgan, soni emas — va matn "
                     "ikkinchi qishloqda daraja <u>o'zgarmaganini</u> aytadi."),
                    (False, "the second village would benefit from a well of its own",
                     "<strong>bashorat va tavsiya</strong> — birinchi "
                     "qishloqdagi pasayishni tushuntirishga hech qanday "
                     "aloqasi yo'q."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Xatoni turi bo'yicha tahlil qiling</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Xato turi</th><th>Nima qilish kerak</th></tr></thead>"
              "<tbody>"
              "<tr><td>Dunyoda rost, matnda yo'q gapni tanladim</td>"
              "<td>72-dars. Barmoq sinovi.</td></tr>"
              "<tr><td><em>proves · shown · always</em> ni tanladim</td>"
              "<td>73-dars. Cheklovlar sanalganmi?</td></tr>"
              "<tr><td>Haddan tashqari ehtiyotkor variantni tanladim</td>"
              "<td>73-dars. To'liq ro'yxat kuchli javobni ko'taradi.</td></tr>"
              "<tr><td>Shart so'ralganda xulosa berdim</td>"
              "<td>71-dars. <em>would have to · only if · depends on</em>.</td></tr>"
              "<tr><td>Tavsiya yoki bashoratni tanladim</td>"
              "<td>70-dars. Matn nima <u>sodir bo'lganini</u> aytadi.</td></tr>"
              "<tr><td>Saqlanish sharoitini e'tiborsiz qoldirdim</td>"
              "<td>73-dars. Eng eski topilgan ≠ eng eski bo'lgan.</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Bu turdagi eng qisqa tekshiruv: javobni tanlagach, "
                "<strong>matnning ikki-uch so'zini ko'rsating</strong>. "
                "Ko'rsatolmasangiz — qaytadan o'qing. Bu bitta odat "
                "Inferences savollarining yarmini yechadi.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">systematic (error)</div><div class="pp-card-back">tizimli (xato) — tasodifiy emas</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to underestimate</div><div class="pp-card-back">kam baholamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">self-selected (groups)</div><div class="pp-card-back">o\'zini o\'zi tanlagan (guruhlar)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a fair manuscript</div><div class="pp-card-back">oqqa ko\'chirilgan qo\'lyozma</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a discrepancy</div><div class="pp-card-back">nomuvofiqlik, tafovut</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to gloss (a word)</div><div class="pp-card-back">(so\'zga) izoh, ta\'rif bermoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">waterborne</div><div class="pp-card-back">suv orqali yuqadigan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">at least as early as ~</div><div class="pp-card-back">kamida ~ chalik erta</div></div>'
            + "</div>"
            + "<h3>Xulosa — Inferences mavzusi yakuni</h3>"
            + "<ul>"
              "<li>Javob matndan <strong>chiqadi</strong>; unga hech nima "
              "<u>qo'shmaydi</u> (70-dars).</li>"
              "<li>Bo'sh joydan oldingi so'zlar javobning <strong>turini</strong> "
              "aytadi (71-dars).</li>"
              "<li><strong>Barmoq sinovi</strong> — tanish mavzuda ikki marta "
              "(72-dars).</li>"
              "<li>Xulosaning kuchi dalilning kuchiga <strong>teng</strong> "
              "(73-dars).</li>"
              "<li>To'g'ri javob odatda eng <u>kamtarin</u> variant bo'ladi.</li>"
              "</ul>"
        )},
    ],
},

]
