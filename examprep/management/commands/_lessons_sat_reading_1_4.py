# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — Reading lessons 1-4
Topic: "Strategiya va format" — the section-wide overview.
See toc_sat_reading.txt and STYLE_GUIDE_SAT_RW.md.

Language: explanation in Uzbek, exam material in English (guide §0). The strategy
topic is the one place where most QUESTIONS are also in Uzbek — a question about
how the test is built is the teacher speaking, not the test.
"""

TRACK = {
    "name":    "SAT",
    "summary": "Digital SAT — Reading and Writing bo'limiga savol turlari bo'yicha "
               "tayyorgarlik. Imtihonning matematik yarmi Prime SAT Math kursida.",
    "icon":    "bi-mortarboard",
    "color":   "#7c3aed",
    "order":   3,
}

TOPIC_STRATEGY = {
    "title":   "Strategiya va format (Reading & Writing: qanday tuzilgan)",
    "summary": "Digital SAT'ning Reading and Writing bo'limi qanday tuzilgan, "
               "qanday baholanadi va uni qanday o'qish kerak.",
    "icon":    "bi-compass",
    "order":   1,
}

# Reusable HTML fragments — keeps the callouts identical across lessons.
TIP   = ('<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>💡 Maslahat:</strong> {}</div>')
WARN  = ('<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>⚠️ Tuzoq:</strong> {}</div>')
NOTE  = ('<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>📌 Eslatma:</strong> {}</div>')
EXAMP = ('<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>📝 Namuna:</strong> {}</div>')


def why(rows):
    """Build an .sr-why choice autopsy. rows = [(ok, choice_text, uzbek_reason), ...]"""
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


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 1
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_STRATEGY,
    "title": "SAT R&W 1: How SAT Reading and Writing Works — 2 Modules, 54 Questions, 64 Minutes",
    "summary": "Digital SAT'ning Reading and Writing bo'limi tuzilishi: ikki modul, "
               "adaptiv ikkinchi modul, 54 savol, 64 daqiqa va 200–800 ball.",
    "order": 1,
    "blocks": [
        {"rich_text": (
            "<h2>Reading and Writing bo'limi qanday ishlaydi?</h2>"
            "<p>Siz allaqachon <strong>Prime SAT Math</strong> kursida imtihonning "
            "matematik yarmini o'rganyapsiz. Bu kurs — <mark>ikkinchi yarmi</mark>: "
            "<strong>Reading and Writing</strong>. Imtihon kunida u <u>birinchi</u> "
            "keladi, matematikadan oldin.</p>"
            "<p>Birinchi darsda hech qanday savol yechmaymiz. Avval <strong>o'yin "
            "maydonini</strong> bilib olamiz — nechta savol, qancha vaqt, qanday ball. "
            "Formatni bilmasdan strategiya qurib bo'lmaydi.</p>"
            '<span class="sr-time">⏱ Bu bo\'limda har savolga ~71 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Asosiy raqamlar</h3>"
            '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            "<div class=\"pp-step\"><p><strong>2 ta modul</strong> — har birida "
            "<strong>27 ta savol</strong> va <strong>32 daqiqa</strong>. Jami: "
            "<mark>54 savol, 64 daqiqa</mark>.</p></div>"
            "<div class=\"pp-step\"><p><strong>Har savolning o'z matni bor</strong> — "
            "taxminan 25–150 so'z. Bitta uzun matnga o'nta savol berilmaydi. Bu eng "
            "muhim farq, va keyingi dars butunlay shu haqda.</p></div>"
            "<div class=\"pp-step\"><p><strong>Hamma savol — 4 variantli test.</strong> "
            "Bu bo'limda javobni o'zi yozadigan savol (grid-in) <u>yo'q</u> — u faqat "
            "matematikada bor.</p></div>"
            "<div class=\"pp-step\"><p><strong>Insho (essay) yo'q.</strong> "
            "«Writing» degani bu yerda «insho yozish» emas, «tahrirlangan yozma ingliz "
            "tilini tanish» degani.</p></div>"
            "<div class=\"pp-step\"><p><strong>Noto'g'ri javob uchun ball "
            "ayirilmaydi.</strong> Shuning uchun "
            "<mark style=\"background:#dcfce7;\">hech qachon savolni bo'sh "
            "qoldirmang</mark> — bilmasangiz ham bitta variantni belgilang.</p></div>"
            "</div>"
        )},

        {"rich_text": (
            "<h3>Adaptiv ikkinchi modul</h3>"
            "<p>Digital SAT <strong>moslashuvchan (adaptive)</strong>. Bu quyidagicha "
            "ishlaydi:</p>"
            "<ul>"
            "<li><strong>1-modul</strong> — hammaga bir xil: oson, o'rta va qiyin "
            "savollar aralash.</li>"
            "<li>Kompyuter sizning 1-moduldagi natijangizni hisoblaydi.</li>"
            "<li><strong>2-modul</strong> — natijangizga qarab <u>qiyinroq</u> yoki "
            "<u>osonroq</u> variant beriladi.</li>"
            "</ul>"
            + NOTE.format(
                "Qiyinroq 2-modul — bu <strong>yaxshi xabar</strong>. Yuqori ballga "
                "faqat shu yo'l bilan chiqiladi. Savollar qiyinlashsa, demak siz "
                "birinchi modulni yaxshi yechgansiz.")
            + WARN.format(
                "Ikkala modul ham ballga qo'shiladi — «birinchi modulni tashlab, "
                "ikkinchisiga kuch to'playman» degan reja <u>ishlamaydi</u>. "
                "Aksincha: 1-modul sizning yuqori ball olish imkoningizni belgilaydi.")
        )},

        {"rich_text": (
            "<h3>Ball tizimi</h3>"
            "<p>Reading and Writing uchun alohida ball beriladi: "
            "<strong>200–800</strong>. Matematika ham <strong>200–800</strong>. "
            "Ikkovi qo'shilib, mashhur <strong>400–1600</strong> umumiy ballni "
            "beradi.</p>"
            '<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">'
            "<p style=\"margin:0 0 6px;\">R&amp;W <strong>600</strong> + Math "
            "<strong>600</strong> = <strong>1200</strong></p>"
            "<p style=\"margin:0 0 6px;\">R&amp;W <strong>700</strong> + Math "
            "<strong>750</strong> = <strong>1450</strong></p>"
            "<p style=\"margin:0;\">R&amp;W <strong>750</strong> + Math "
            "<strong>800</strong> = <strong>1550</strong></p>"
            "</div>"
            "<p>Ko'p o'zbek o'quvchilarning matematika balli ingliz tili ballidan "
            "ancha yuqori bo'ladi. Bu — <strong>yaxshi yangilik</strong>: umumiy ballni "
            "ko'tarishning eng arzon yo'li aynan shu bo'limda, chunki bu yerda "
            "yo'qotayotgan ballaringiz ko'proq.</p>"
            + TIP.format(
                "1600 ballning yarmi shu bo'limda. Matematikada 800 dan 800 ga "
                "chiqib bo'lmaydi — R&amp;W'da 550 dan 650 ga chiqish esa juda "
                "real, va u umumiy ballga xuddi shunday 100 ball qo'shadi.")
        )},

        {
            "rich_text": "<p><strong>Amaliyot 1.</strong> Reading and Writing bo'limida jami nechta savol va qancha vaqt bor?</p>",
            "choices": [
                {"text": "54 ta savol, 64 daqiqa (2 modul × 27 savol × 32 daqiqa)", "is_correct": True},
                {"text": "44 ta savol, 70 daqiqa (2 modul × 22 savol × 35 daqiqa)", "is_correct": False},
                {"text": "40 ta savol, 60 daqiqa (3 ta uzun matn)", "is_correct": False},
                {"text": "54 ta savol, 32 daqiqa (bitta modul)", "is_correct": False},
            ],
            "explanation": why([
                (True, "54 ta savol, 64 daqiqa",
                 "Ikkita modul, har birida 27 savol va 32 daqiqa. 32 ÷ 27 ≈ "
                 "<u>71 soniya</u> — har savolga o'rtacha shuncha vaqtingiz bor."),
                (False, "44 ta savol, 70 daqiqa",
                 "bu <strong>matematika</strong> bo'limining raqamlari (2 modul × 22 "
                 "savol × 35 daqiqa). Ikkovini adashtirmang."),
                (False, "40 ta savol, 60 daqiqa",
                 "bu <strong>IELTS Reading</strong>ning tuzilishi — uch uzun matn. "
                 "SAT butunlay boshqacha ishlaydi."),
                (False, "54 ta savol, 32 daqiqa",
                 "savollar soni to'g'ri, lekin 32 daqiqa — bu bitta modulning vaqti. "
                 "Ikkita modul bor."),
            ]),
        },

        {
            "rich_text": "<p><strong>Amaliyot 2.</strong> 2-modulda savollar sezilarli darajada qiyinlashdi. Bu nimani anglatadi?</p>",
            "choices": [
                {"text": "1-modulni yaxshi yechganman — bu yuqori ballga yo'l", "is_correct": True},
                {"text": "Xatolik yuz bergan, nazoratchiga aytish kerak", "is_correct": False},
                {"text": "1-modulni yomon yechganman", "is_correct": False},
                {"text": "Hech nimani anglatmaydi — 2-modul hammaga bir xil", "is_correct": False},
            ],
            "explanation": why([
                (True, "1-modulni yaxshi yechganman",
                 "adaptiv tizim shunday ishlaydi: yaxshi natija — qiyinroq ikkinchi "
                 "modul — yuqoriroq ball shipi. Qiyinlashuv bu <u>mukofot</u>, "
                 "jazo emas."),
                (False, "Xatolik yuz bergan",
                 "bu normal ish rejimi. Bluebook ilovasi shunday tuzilgan."),
                (False, "1-modulni yomon yechganman",
                 "aynan teskarisi. Yomon natijada <u>osonroq</u> modul keladi — "
                 "va u bilan olinadigan eng yuqori ball ham pastroq bo'ladi."),
                (False, "Hech nimani anglatmaydi — 2-modul hammaga bir xil",
                 "bu <strong>eski qog'oz</strong> SAT'ning qoidasi edi. Digital SAT "
                 "2023-yildan boshlab adaptiv."),
            ]),
        },

        {
            "rich_text": "<p><strong>Amaliyot 3.</strong> Vaqt tugashiga 40 soniya qoldi, ikkita savol javobsiz. Nima qilasiz?</p>",
            "choices": [
                {"text": "Ikkalasiga ham darhol tavakkal javob belgilayman", "is_correct": True},
                {"text": "Bo'sh qoldiraman — noto'g'ri javob ball ayiradi", "is_correct": False},
                {"text": "Bittasini sinchiklab yechaman, ikkinchisini bo'sh qoldiraman", "is_correct": False},
                {"text": "Ikkalasini ham o'qib chiqaman, ulgursam belgilayman", "is_correct": False},
            ],
            "explanation": why([
                (True, "Ikkalasiga ham darhol tavakkal javob belgilayman",
                 "SAT'da <u>noto'g'ri javob uchun ball ayirilmaydi</u>. To'rt "
                 "variantdan tasodifiy tanlash ham 25% imkoniyat beradi — bo'sh "
                 "katak esa aniq 0. Har doim to'ldiring."),
                (False, "Bo'sh qoldiraman",
                 "bu <strong>eski</strong> SAT (2016-yilgacha) qoidasi edi — o'shanda "
                 "noto'g'ri javob uchun chorak ball ayirilardi. Endi bunday emas."),
                (False, "Bittasini sinchiklab yechaman",
                 "40 soniyada bitta savolni yechish mumkin, lekin ikkinchisini bo'sh "
                 "qoldirish uchun <u>hech qanday sabab yo'q</u>. Avval ikkalasiga "
                 "belgilab qo'ying, keyin qolgan vaqtda bittasini o'qing."),
                (False, "Ikkalasini ham o'qib chiqaman",
                 "40 soniyada ikki matn va ikki savolni o'qib bo'lmaydi — vaqt tugaydi "
                 "va ikkalasi ham bo'sh qoladi. Bu eng ko'p uchraydigan xato."),
            ]),
        },

        {
            "rich_text": "<p><strong>Amaliyot 4.</strong> Digital SAT'ning Reading and Writing bo'limida quyidagilardan qaysi biri <u>bor</u>?</p>",
            "choices": [
                {"text": "Faqat 4 variantli test savollari", "is_correct": True},
                {"text": "Insho (essay) — 50 daqiqa", "is_correct": False},
                {"text": "Javobni o'zi yozadigan savollar (grid-in)", "is_correct": False},
                {"text": "Tinglab tushunish (listening) qismi", "is_correct": False},
            ],
            "explanation": why([
                (True, "Faqat 4 variantli test savollari",
                 "54 ta savolning hammasi bir xil shaklda: qisqa matn, bitta savol, "
                 "to'rtta variant. Boshqa shakl yo'q."),
                (False, "Insho (essay)",
                 "SAT inshosi <u>bekor qilingan</u>. IELTS Writing Task 2 odatini "
                 "bu yerga olib kelmang."),
                (False, "Javobni o'zi yozadigan savollar (grid-in)",
                 "grid-in (student-produced response) faqat <strong>matematika</strong> "
                 "bo'limida — u yerda savollarning ~25 foizi shunday."),
                (False, "Tinglab tushunish (listening) qismi",
                 "SAT'da umuman listening yo'q — bu IELTS va TOPIK'ning qismi. "
                 "SAT to'liq o'qish va yozma tildan iborat."),
            ]),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            '<div class="pp-flashcards" data-pp-flashcards>'
            '<div class="pp-card"><div class="pp-card-front">module</div><div class="pp-card-back">modul — bo\'limning bir qismi (27 savol, 32 daqiqa)</div></div>'
            '<div class="pp-card"><div class="pp-card-front">adaptive</div><div class="pp-card-back">moslashuvchan — 2-modul natijangizga qarab tanlanadi</div></div>'
            '<div class="pp-card"><div class="pp-card-front">passage</div><div class="pp-card-back">matn parchasi (SAT\'da 25–150 so\'z)</div></div>'
            '<div class="pp-card"><div class="pp-card-front">stem</div><div class="pp-card-back">savolning o\'zi (variantlardan oldingi qism)</div></div>'
            '<div class="pp-card"><div class="pp-card-front">scaled score</div><div class="pp-card-back">shkalaga o\'tkazilgan ball (200–800)</div></div>'
            '<div class="pp-card"><div class="pp-card-front">composite score</div><div class="pp-card-back">umumiy ball (400–1600)</div></div>'
            '<div class="pp-card"><div class="pp-card-front">Bluebook</div><div class="pp-card-back">imtihon topshiriladigan rasmiy ilova</div></div>'
            '<div class="pp-card"><div class="pp-card-front">no penalty for guessing</div><div class="pp-card-back">tavakkal javob uchun ball ayirilmaydi</div></div>'
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>2 modul × 27 savol × 32 daqiqa = <strong>54 savol, 64 daqiqa</strong>, "
            "har savolga ~71 soniya.</li>"
            "<li>2-modul <strong>adaptiv</strong>; ikkala modul ham ballga qo'shiladi.</li>"
            "<li>Hamma savol — <strong>4 variantli test</strong>. Insho yo'q, grid-in "
            "yo'q, listening yo'q.</li>"
            "<li><strong>Hech qachon bo'sh qoldirmang</strong> — noto'g'ri javob ball "
            "ayirmaydi.</li>"
            "<li>R&amp;W ball <strong>200–800</strong>; matematika bilan qo'shilib "
            "400–1600 bo'ladi.</li>"
            "</ul>"
            + NOTE.format(
                "Ro'yxatdan o'tish muddatlari, to'lov va imtihon markazlari vaqti-vaqti "
                "bilan o'zgaradi — ularni faqat <strong>College Board</strong>ning "
                "rasmiy saytidan tekshiring. Bu kurs sizni imtihonning "
                "<u>mazmuniga</u> tayyorlaydi.")
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 2
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_STRATEGY,
    "title": "SAT R&W 2: One Passage, One Question — Why This Test Is Not a Reading Test",
    "summary": "Har savolning o'z qisqa matni bor. Bu bitta fakt butun strategiyani "
               "belgilaydi: skimming kerak emas, har savol mustaqil, va isbot doim ekranda.",
    "order": 2,
    "blocks": [
        {"rich_text": (
            "<h2>Bitta matn — bitta savol</h2>"
            "<p>Bu kursdagi eng muhim dars. Digital SAT'ning Reading and Writing "
            "bo'limi <strong>o'qish imtihoni emas</strong> — hech bo'lmaganda siz "
            "o'rganib qolgan ma'noda emas.</p>"
            "<p>IELTS'da bitta 900 so'zli matn bor va unga 13 ta savol beriladi. "
            "Eski qog'oz SAT'da ham shunday edi. <mark>Digital SAT'da esa har bir "
            "savolning o'z matni bor</mark> — atigi 25–150 so'z, va o'sha matn faqat "
            "bitta savolga xizmat qiladi. Keyingi savol — butunlay boshqa matn, "
            "boshqa mavzu, boshqa muallif.</p>"
            "<p>54 ta savol degani — <strong>54 ta kichik dunyo</strong>.</p>"
        )},

        {"rich_text": (
            "<h3>Bu fakt nimani o'zgartiradi?</h3>"
            '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            "<div class=\"pp-step\"><p><strong>1. Skimming strategiyasi keraksiz "
            "bo'lib qoladi.</strong> «Avval matnni tez ko'zdan kechirib, umumiy "
            "mavzuni tushunib olaman» — bu 60 so'zli matnda ma'nosiz. Matnni "
            "<u>to'liq</u> o'qiysiz, chunki u qisqa.</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Har savol mustaqil.</strong> Bitta "
            "savolni tushunmasangiz, u keyingi savolga <u>hech qanday</u> ta'sir "
            "qilmaydi. Tashlab ketish arzon.</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Savolni birinchi o'qish "
            "foydali.</strong> Matn qisqa bo'lgani uchun, savolni bilib turib "
            "o'qish — vaqt tejaydi va nimaga qarash kerakligini aytadi.</p></div>"
            "<div class=\"pp-step\"><p><strong>4. Isbot doim ekranda.</strong> Javob "
            "60 so'zning ichida. Umumiy bilim, taxmin va «tuyg'u» kerak emas — va "
            "aksincha, ular <u>xato qildiradi</u>.</p></div>"
            "<div class=\"pp-step\"><p><strong>5. Vaqt bir tekis taqsimlanadi.</strong> "
            "Har savolga ~71 soniya. «Bu matnga 6 daqiqa sarflab, keyin tez "
            "yechaman» degan reja yo'q — matnlar bir-biriga bog'liq emas.</p></div>"
            "</div>"
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            "<p>Mana haqiqiy SAT savoli qanday ko'rinadi. <u>Hozircha javob "
            "bermang</u> — birgalikda yechamiz.</p>"
            '<div class="sr-passage">'
            "<p>Termite mounds on the plains of Namibia can rise several metres above "
            "the ground. For decades these structures were described as air-conditioned "
            "towers: hot air was thought to rise through a central chimney and escape at "
            "the top, drawing fresh air in below. Measurements of gas movement inside the "
            "mounds complicate that account. The internal air does not flow steadily "
            "upward at all; it moves in slow, tidal surges, shifting back and forth in "
            "response to conditions outside the mound.</p>"
            "</div>"
            "<p><strong>Which choice best states the main idea of the text?</strong></p>"
            "<ol type=\"A\">"
            "<li>Termite mounds in Namibia are unusually tall compared with mounds elsewhere.</li>"
            "<li>Measurements inside termite mounds have complicated a long-accepted explanation of how their air moves.</li>"
            "<li>Termites build tall mounds in order to protect the colony from heat.</li>"
            "<li>The chimney effect is the main mechanism that ventilates termite mounds.</li>"
            "</ol>"
            '<span class="sr-time">⏱ ~50 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Qanday yechamiz</h3>"
            "<p><strong>1-qadam. Savolni o'qing.</strong> <em>Main idea</em> so'ralyapti "
            "— matn <u>nimani da'vo qilyapti</u>, nima haqda gapiryapti emas.</p>"
            "<p><strong>2-qadam. Matnning shaklini toping.</strong> Bu yerda shakl juda "
            "aniq: <em>«uzoq vaqt shunday deb o'ylangan… lekin o'lchovlar buni "
            "qiyinlashtiradi»</em>. Ya'ni: <mark>eski tushuntirish → yangi "
            "ma'lumot</mark>. Asosiy fikr har doim shu burilishda turadi.</p>"
            "<p><strong>3-qadam. O'zingiz javobni ayting</strong>, variantlarga "
            "qaramasdan: «yangi o'lchovlar eski tushuntirishga shubha tug'dirdi».</p>"
            "<p><strong>4-qadam. Endi variantlarni solishtiring.</strong></p>"
            + why([
                (True, "Measurements … have complicated a long-accepted explanation",
                 "aynan matnning shakli: <em>were thought</em> (eski tushuntirish) → "
                 "<em>complicate that account</em> (yangi ma'lumot). Isbot ekranda "
                 "turibdi."),
                (False, "Termite mounds … are unusually tall compared with mounds elsewhere",
                 "«boshqa joylardagi uyalar bilan solishtirilganda» — matnda "
                 "<u>umuman yo'q</u>. Bu <strong>tashqi bilim</strong> tuzog'i. "
                 "Balandlik esa faqat kirish detali, asosiy fikr emas."),
                (False, "Termites build tall mounds in order to protect the colony from heat",
                 "dunyoda bu to'g'ri bo'lishi mumkin, lekin bu 60 so'z bunday demaydi. "
                 "<strong>Rost, lekin so'ralmagan.</strong>"),
                (False, "The chimney effect is the main mechanism that ventilates termite mounds",
                 "matn aynan buni <u>rad etyapti</u> (<em>does not flow steadily upward "
                 "at all</em>). Matndagi kuchli so'zni (<em>chimney</em>) qaytaradi-yu, "
                 "ma'nosini teskari qiladi — <strong>so'z-tuzoq</strong>."),
            ])
            + TIP.format(
                "3-qadam — javobni o'zingiz aytish — eng ko'p ball qutqaradigan "
                "odat. Variantlarni <u>tayyor javob bilan</u> ko'rgan odam aldanmaydi; "
                "bo'sh bosh bilan ko'rgan odam eng chiroyli variantni tanlaydi.")
        )},

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>Alisher Navoiy, writing in the late fifteenth century, argued that "
                "Chagatai Turkic was as capable of subtle literary expression as Persian, "
                "then the dominant literary language of Central Asia. His treatise "
                "<em>Muhokamat al-Lughatayn</em> does not merely assert this claim; it "
                "<span class=\"sr-blank\"></span> the claim, listing dozens of Turkic "
                "words for which, he maintains, Persian offers no single equivalent.</p>"
                "</div>"
                "<p><strong>Which choice completes the text with the most logical and "
                "precise word or phrase?</strong></p>"
            ),
            "choices": [
                {"text": "substantiates", "is_correct": True},
                {"text": "contradicts", "is_correct": False},
                {"text": "simplifies", "is_correct": False},
                {"text": "exaggerates", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joydan oldingi qism hamma narsani hal qiladi: "
                "<em>does not <u>merely assert</u> this claim; it ___ the claim</em> — "
                "«shunchaki <u>aytib qo'ymaydi</u>, balki …». Demak kerakli so'z "
                "«aytishdan kuchliroq» narsani bildirishi kerak. Keyingi qism aytadi: "
                "<em>listing dozens of Turkic words</em> — ya'ni <mark>dalil "
                "keltiradi</mark>.</p>"
                + why([
                    (True, "substantiates",
                     "«dalil bilan tasdiqlaydi». Aynan «shunchaki aytish»ning "
                     "kuchliroq juftligi, va ro'yxat keltirish bunga isbot."),
                    (False, "contradicts",
                     "«rad etadi» — o'z da'vosini o'zi rad etmaydi. Nuqta-vergul "
                     "(<em>;</em>) bu yerda qarama-qarshilikni emas, "
                     "<u>kuchaytirishni</u> bildiryapti."),
                    (False, "simplifies",
                     "«soddalashtiradi» — o'nlab so'zdan iborat ro'yxat "
                     "soddalashtirish emas, batafsillashtirish."),
                    (False, "exaggerates",
                     "«bo'rttiradi» — matnda muallifga nisbatan hech qanday tanqid "
                     "yo'q. Bu <strong>tashqi bilim</strong> tuzog'i: siz Navoiy "
                     "haqida o'ylayotgan narsangizni matnga qo'shib yuborasiz."),
                ])
                + NOTE.format(
                    "<strong>Muhokamat al-Lughatayn</strong> («Ikki til muhokamasi») "
                    "— Navoiyning 1499-yilda yozgan asari. SAT matnlari ba'zan "
                    "sizga tanish mavzuda bo'ladi; bu yordam beradi, lekin javob "
                    "baribir <u>faqat matndan</u> olinadi.")
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>Rustam had promised himself that he would not look at the results "
                "until the evening. <span class=\"sr-focus\">He looked at nine o'clock, "
                "and again at four minutes past, as though the numbers might have "
                "reconsidered.</span> By ten he had closed the page, opened it, and "
                "closed it again, and had answered none of the three messages waiting "
                "on his phone.</p>"
                "</div>"
                "<p><strong>What is the main purpose of the underlined sentence?</strong></p>"
            ),
            "choices": [
                {"text": "It illustrates the distance between what Rustam intended to do and what he actually did.", "is_correct": True},
                {"text": "It explains why Rustam does not trust the accuracy of the results.", "is_correct": False},
                {"text": "It establishes that the results Rustam received were disappointing.", "is_correct": False},
                {"text": "It suggests that Rustam is generally careless about the promises he makes.", "is_correct": False},
            ],
            "explanation": (
                "<p>Savol <em>main <u>purpose</u></em> so'rayapti — bu jumla matnda "
                "<u>nima ish qilyapti</u>? Undan oldingi jumla va'dani aytadi "
                "(<em>would not look until the evening</em>); tagi chizilgan jumla esa "
                "darhol uning buzilishini ko'rsatadi — hatto ikki marta, ikki daqiqa "
                "ichida.</p>"
                + why([
                    (True, "It illustrates the distance between what Rustam intended … and what he actually did",
                     "jumlaning vazifasi shu: va'da bilan xatti-harakat orasidagi "
                     "masofani ko'rsatish. <em>as though the numbers might have "
                     "reconsidered</em> — mayin kinoya ham xuddi shunga ishlaydi."),
                    (False, "It explains why Rustam does not trust the accuracy of the results",
                     "matn natijalarning aniqligi haqida <u>hech narsa</u> demaydi. "
                     "Rustam ishonmayapti emas — chiday olmayapti."),
                    (False, "It establishes that the results … were disappointing",
                     "<strong>yarim to'g'ri</strong> tuzog'i: Rustam bezovta, bu rost, "
                     "lekin natija yomon ekani matnda aytilmagan. U natijani ko'rganini "
                     "ham, ko'rmaganini ham bilmaymiz."),
                    (False, "It suggests that Rustam is generally careless about the promises he makes",
                     "<em>generally</em> — <strong>doirasi juda keng</strong>. Matn "
                     "bitta kunning bitta ertalabini ko'rsatadi, xarakter tavsifini "
                     "emas."),
                ])
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>For decades, wildlife reintroduction programs measured their success "
                "by a single figure: the number of animals released into the wild. A "
                "review of long-running projects has questioned that practice. Released "
                "animals frequently failed to establish breeding populations, and the "
                "projects that did succeed turned out to share a feature the release "
                "count ignored entirely — the habitat had been repaired before any "
                "animal was set free. The review therefore suggests that release numbers, "
                "considered on their own, <span class=\"sr-blank\"></span></p>"
                "</div>"
                "<p><strong>Which choice most logically completes the text?</strong></p>"
            ),
            "choices": [
                {"text": "reveal little about whether a program will actually succeed.", "is_correct": True},
                {"text": "should be increased in order to improve future programs.", "is_correct": False},
                {"text": "are the only measurement conservationists can reliably collect.", "is_correct": False},
                {"text": "explain why the habitats of released animals continue to degrade.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joy matnning <u>oxirida</u> — bu <em>Inferences</em> "
                "savolining doimiy shakli. Sizdan matnni davom ettirish emas, "
                "<mark>matn allaqachon isbotlagan xulosani aytish</mark> "
                "so'ralyapti.</p>"
                "<p>Matn nimani isbotladi? (1) sanoq bo'yicha muvaffaqiyatli deb "
                "hisoblangan loyihalar ko'pincha muvaffaqiyatsiz chiqdi; (2) haqiqatan "
                "muvaffaqiyatli bo'lganlarining umumiy jihatini sanoq "
                "<u>umuman hisobga olmagan</u>. Demak sanoqning o'zi muvaffaqiyatni "
                "bashorat qilmaydi.</p>"
                + why([
                    (True, "reveal little about whether a program will actually succeed",
                     "ikkala dalil ham aynan shunga olib boradi. <em>considered on "
                     "their own</em> («o'z-o'zicha olinganda») bo'lagi ham shu "
                     "javobga ishora."),
                    (False, "should be increased in order to improve future programs",
                     "matn sanoqning <u>o'lchov sifatida</u> yaroqsizligini aytyapti, "
                     "ko'proq hayvon qo'yib yuborish kerakligini emas. Bu — matndan "
                     "chiqmaydigan tavsiya."),
                    (False, "are the only measurement conservationists can reliably collect",
                     "matn ikkinchi o'lchovni — yashash muhitining tiklanganini — "
                     "o'zi nomlab turibdi. Ya'ni javob matnning o'ziga zid."),
                    (False, "explain why the habitats … continue to degrade",
                     "sabab-oqibat teskari qilingan. Matn muhit buzilishining sababi "
                     "haqida hech narsa demaydi."),
                ])
            ),
        },

        {
            "rich_text": (
                "<p><strong>Amaliyot 4.</strong> Imtihonda bitta savolning matnini "
                "tushunolmadingiz. Eng to'g'ri harakat qaysi?</p>"
            ),
            "choices": [
                {"text": "Bitta variant belgilab, keyingi savolga o'taman — u boshqa matn, boshqa mavzu", "is_correct": True},
                {"text": "Tushunmagunimcha o'qiyman, chunki keyingi savollar ham shu matnga tegishli", "is_correct": False},
                {"text": "Bo'sh qoldirib, modul oxirida qaytaman va butun matnni qaytadan o'qiyman", "is_correct": False},
                {"text": "Oldingi savollarning matnlariga qaytib, umumiy mavzuni tiklashga urinaman", "is_correct": False},
            ],
            "explanation": (
                why([
                    (True, "Bitta variant belgilab, keyingi savolga o'taman",
                     "har savol o'z matni bilan mustaqil. Bitta qiyin matn keyingi "
                     "savollarga <u>umuman</u> ta'sir qilmaydi, va bo'sh qoldirish "
                     "uchun sabab yo'q (ball ayirilmaydi)."),
                    (False, "Tushunmagunimcha o'qiyman, chunki keyingi savollar ham shu matnga tegishli",
                     "bu <strong>IELTS va eski qog'oz SAT</strong>ning qoidasi. "
                     "Digital SAT'da har savolning o'z matni bor — shuning uchun "
                     "bitta matnga uzoq vaqt sarflash sof zarar."),
                    (False, "Bo'sh qoldirib, modul oxirida qaytaman",
                     "qaytish yomon emas (Bluebook'da belgilab qo'yish mumkin), lekin "
                     "<u>avval javob belgilang</u>. Vaqt tugasa, bo'sh katak 0 ball."),
                    (False, "Oldingi savollarning matnlariga qaytib, umumiy mavzuni tiklashga urinaman",
                     "oldingi matnlar butunlay boshqa mavzuda — biri termitlar haqida, "
                     "biri she'r bo'lishi mumkin. Ular hech qanday «umumiy mavzu» "
                     "yaratmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            '<div class="pp-flashcards" data-pp-flashcards>'
            '<div class="pp-card"><div class="pp-card-front">main idea</div><div class="pp-card-back">asosiy fikr — matn nimani da\'vo qilyapti</div></div>'
            '<div class="pp-card"><div class="pp-card-front">main purpose</div><div class="pp-card-back">asosiy maqsad — bu jumla nima ish qilyapti</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to assert</div><div class="pp-card-back">da\'vo qilmoq (dalilsiz aytmoq)</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to substantiate</div><div class="pp-card-back">dalil bilan tasdiqlamoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to complicate an account</div><div class="pp-card-back">mavjud tushuntirishga shubha tug\'dirmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">long-accepted</div><div class="pp-card-back">uzoq vaqt qabul qilingan</div></div>'
            '<div class="pp-card"><div class="pp-card-front">on their own</div><div class="pp-card-back">o\'z-o\'zicha, yolg\'iz olinganda</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to establish (a population)</div><div class="pp-card-back">(populyatsiya) barpo qilmoq, ildiz otmoq</div></div>'
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Har savolning <strong>o'z matni</strong> bor — 25–150 so'z, faqat shu "
            "savol uchun.</li>"
            "<li>Skimming kerak emas: matn qisqa, uni <strong>to'liq</strong> o'qing.</li>"
            "<li><strong>Avval savolni</strong>, keyin matnni o'qing.</li>"
            "<li>Variantlarga qaramasdan <strong>javobni o'zingiz ayting</strong>, "
            "keyin solishtiring.</li>"
            "<li>Qiyin savol — arzon: bitta variant belgilang va keting.</li>"
            "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 3
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_STRATEGY,
    "title": "SAT R&W 3: The Four Domains and the Order They Appear In",
    "summary": "To'rtta domen — Craft and Structure, Information and Ideas, Standard "
               "English Conventions, Expression of Ideas — va ularning modul ichidagi "
               "tartibi; savol turini tanib olish ko'nikmasi.",
    "order": 3,
    "blocks": [
        {"rich_text": (
            "<h2>To'rtta domen</h2>"
            "<p>54 ta savol tasodifiy aralashtirilmagan. Ularning har biri to'rtta "
            "<strong>domen</strong>dan biriga tegishli, va modul ichida savollar "
            "<mark>domen bo'yicha guruhlangan</mark> holda keladi.</p>"
            "<p>Nega bu muhim? Chunki domen o'zgarganda — <u>fikrlash turi "
            "o'zgaradi</u>. Grammatika savolini o'qiyotganda «muallif nimani "
            "nazarda tutdi?» deb o'ylash — vaqtni behuda sarflash. Domenni tanigan "
            "o'quvchi savolni ochishdan oldin nima qilishini biladi.</p>"
        )},

        {"rich_text": (
            "<h3>Domenlar va ularning ulushi</h3>"
            '<div class="sr-data"><div class="sr-data__scroll">'
            "<table>"
            "<thead><tr><th>Domen</th><th>Ulush</th><th>Savol</th></tr></thead>"
            "<tbody>"
            "<tr><td>Craft and Structure</td><td>~28%</td><td>13–15</td></tr>"
            "<tr><td>Information and Ideas</td><td>~26%</td><td>12–14</td></tr>"
            "<tr><td>Standard English Conventions</td><td>~26%</td><td>11–15</td></tr>"
            "<tr><td>Expression of Ideas</td><td>~20%</td><td>8–12</td></tr>"
            "</tbody></table>"
            "</div></div>"
            "<p>Diqqat qiling: <strong>grammatika va uslub</strong> (oxirgi ikki domen) "
            "birgalikda savollarning <mark>deyarli yarmini</mark> tashkil qiladi. "
            "Ko'p o'quvchi SAT'ni «o'qish imtihoni» deb o'ylab, aynan shu yarmiga "
            "tayyorgarlik ko'rmaydi — va aynan shu yerda eng arzon ballar yotadi, "
            "chunki grammatika qoidalari <u>aniq</u> va o'rganib bo'ladigan.</p>"
        )},

        {"rich_text": (
            "<h3>Har domen nimani so'raydi</h3>"
            '<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">'
            '<summary style="cursor:pointer;font-weight:600;">📂 Craft and Structure — bosing</summary>'
            "<div style=\"margin-top:10px;\">"
            "<p><strong>So'z, tuzilish va maqsad.</strong> Uch savol turi:</p><ul>"
            "<li><strong>Words in Context</strong> — <em>Which choice completes the text "
            "with the most logical and precise word or phrase?</em></li>"
            "<li><strong>Text Structure and Purpose</strong> — <em>What is the main "
            "purpose of the underlined sentence?</em></li>"
            "<li><strong>Cross-Text Connections</strong> — <em>Based on the texts, how "
            "would the author of Text 2 most likely respond…?</em></li>"
            "</ul></div></details>"
            '<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">'
            '<summary style="cursor:pointer;font-weight:600;">📂 Information and Ideas — bosing</summary>'
            "<div style=\"margin-top:10px;\">"
            "<p><strong>Matndagi ma'lumot va undan chiqadigan xulosa.</strong></p><ul>"
            "<li><strong>Central Ideas and Details</strong> — <em>Which choice best "
            "states the main idea of the text?</em></li>"
            "<li><strong>Command of Evidence (Textual)</strong> — <em>Which quotation "
            "most effectively illustrates the claim?</em></li>"
            "<li><strong>Command of Evidence (Quantitative)</strong> — jadval yoki "
            "grafik bilan: <em>Which choice most effectively uses data from the table…?</em></li>"
            "<li><strong>Inferences</strong> — <em>Which choice most logically completes "
            "the text?</em></li>"
            "</ul></div></details>"
            '<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">'
            '<summary style="cursor:pointer;font-weight:600;">📂 Standard English Conventions — bosing</summary>'
            "<div style=\"margin-top:10px;\">"
            "<p><strong>Grammatika va tinish belgilari.</strong> Savol deyarli har doim "
            "bir xil: <em>Which choice completes the text so that it conforms to the "
            "conventions of Standard English?</em></p><ul>"
            "<li><strong>Boundaries</strong> — gap chegaralari, vergul, nuqtali vergul, "
            "ikki nuqta, tire.</li>"
            "<li><strong>Form, Structure, and Sense</strong> — fe'l shakllari, "
            "ega-kesim moslashuvi, olmoshlar, ko'plik va egalik.</li>"
            "</ul></div></details>"
            '<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">'
            '<summary style="cursor:pointer;font-weight:600;">📂 Expression of Ideas — bosing</summary>'
            "<div style=\"margin-top:10px;\">"
            "<p><strong>Fikrni samarali ifodalash.</strong></p><ul>"
            "<li><strong>Transitions</strong> — <em>Which choice completes the text with "
            "the most logical transition?</em></li>"
            "<li><strong>Rhetorical Synthesis</strong> — o'quvchining qaydlari beriladi: "
            "<em>The student wants to… Which choice most effectively uses relevant "
            "information from the notes to accomplish this goal?</em></li>"
            "</ul></div></details>"
            + NOTE.format(
                "Bu kursda birinchi ikki domen — <strong>Reading</strong> bo'limida, "
                "oxirgi ikkitasi — <strong>Writing</strong> bo'limida. Imtihonda esa "
                "ular bitta 54 savollik bo'limda, birga keladi.")
        )},

        {"rich_text": (
            "<h3>Tartib</h3>"
            "<p>Modul ichida savollar domen bo'yicha guruhlanadi, va <u>har guruh "
            "ichida</u> oson savoldan qiyiniga qarab boradi. Bluebook mashq "
            "testlarida tartib odatda shunday:</p>"
            "<p style=\"text-align:center;font-weight:600;\">Craft and Structure → "
            "Information and Ideas → Standard English Conventions → Expression of Ideas</p>"
            "<p>Ikki amaliy natija:</p>"
            "<ul>"
            "<li><strong>Guruh o'zgarganini sezing.</strong> Savol matni "
            "<em>«…conforms to the conventions of Standard English?»</em>ga o'zgargan "
            "payt — endi grammatika bo'limidasiz. O'qish usulingiz ham o'zgarishi "
            "kerak: matnni tahlil qilmang, <u>gapning tuzilishiga qarang</u>.</li>"
            "<li><strong>Guruh boshidagi savollar osonroq.</strong> Yangi guruh "
            "boshlanganda tezlashing — u yerda tez ball bor.</li>"
            "</ul>"
            + WARN.format(
                "Bu tartib — Bluebook mashq testlarida kuzatilgani. Ishonchli fakt "
                "shu: savollar <u>guruhlangan</u> va guruh ichida qiyinlashib boradi. "
                "Aniq ketma-ketlikni har doim o'zingizning eng so'nggi rasmiy mashq "
                "testingizda tekshiring.")
        )},

        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Savol matni: "
                "<em>«As used in the text, what does the word “reserved” most nearly "
                "mean?»</em> Bu qaysi domen?</p>"
            ),
            "choices": [
                {"text": "Craft and Structure (Words in Context)", "is_correct": True},
                {"text": "Information and Ideas (Central Ideas and Details)", "is_correct": False},
                {"text": "Expression of Ideas (Transitions)", "is_correct": False},
                {"text": "Standard English Conventions (Form, Structure, and Sense)", "is_correct": False},
            ],
            "explanation": (
                why([
                    (True, "Craft and Structure (Words in Context)",
                     "<em>most nearly mean</em> — bu Words in Context savolining ikkita "
                     "shaklidan biri (ikkinchisi — bo'sh joyni to'ldirish). So'zning "
                     "lug'atdagi ma'nosi emas, <u>shu gapdagi</u> ma'nosi so'ralyapti."),
                    (False, "Information and Ideas",
                     "bu domen matnning <em>mazmuni</em> haqida so'raydi — asosiy fikr, "
                     "dalil, xulosa. Bitta so'z haqida emas."),
                    (False, "Expression of Ideas (Transitions)",
                     "Transitions savoli bog'lovchi so'z so'raydi (<em>however</em>, "
                     "<em>therefore</em>), va u har doim <u>bo'sh joy</u> bilan keladi."),
                    (False, "Standard English Conventions",
                     "grammatika savollarining matni deyarli har doim bir xil: "
                     "<em>…conforms to the conventions of Standard English?</em>"),
                ])
            ),
        },

        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Ekranda o'quvchining tadqiqot qaydlari "
                "(bulletlar) berilgan, so'ng: <em>«The student wants to emphasise a "
                "similarity between the two artists. Which choice most effectively uses "
                "relevant information from the notes to accomplish this goal?»</em> "
                "Bu qaysi domen?</p>"
            ),
            "choices": [
                {"text": "Expression of Ideas (Rhetorical Synthesis)", "is_correct": True},
                {"text": "Information and Ideas (Command of Evidence)", "is_correct": False},
                {"text": "Craft and Structure (Text Structure and Purpose)", "is_correct": False},
                {"text": "Standard English Conventions (Boundaries)", "is_correct": False},
            ],
            "explanation": (
                why([
                    (True, "Expression of Ideas (Rhetorical Synthesis)",
                     "qaydlar ro'yxati + <em>The student wants to…</em> — bu shakl "
                     "faqat bitta savol turida uchraydi. Javobni <u>maqsad</u> "
                     "belgilaydi, ma'lumotning to'g'riligi emas."),
                    (False, "Information and Ideas (Command of Evidence)",
                     "Command of Evidence ham dalil so'raydi, lekin u <u>berilgan "
                     "matndan</u> iqtibos yoki jadvaldan raqam tanlashni so'raydi — "
                     "o'quvchining qaydlaridan jumla qurishni emas."),
                    (False, "Craft and Structure (Text Structure and Purpose)",
                     "bu domen mavjud matnning tuzilishi haqida so'raydi; bu yerda esa "
                     "siz yangi jumla <u>tanlayapsiz</u>."),
                    (False, "Standard English Conventions (Boundaries)",
                     "variantlar orasida grammatik xato yo'q — hammasi to'g'ri "
                     "yozilgan jumlalar. Farq faqat <u>maqsadga mosligida</u>."),
                ])
                + TIP.format(
                    "Rhetorical Synthesis savolida to'rtta variantning "
                    "<u>hammasi</u> qaydlardagi rost ma'lumotni ishlatadi. Shuning "
                    "uchun «qaysi biri to'g'ri?» deb so'ramang — «qaysi biri "
                    "<strong>maqsadni</strong> bajaradi?» deb so'rang.")
            ),
        },

        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Savol matni: <em>«Which choice completes "
                "the text so that it conforms to the conventions of Standard English?»</em> "
                "va variantlar: <em>researcher's · researchers · researchers' · "
                "researchers's</em>. Nima qilasiz?</p>"
            ),
            "choices": [
                {"text": "Gapning grammatikasiga qarayman: ko'plikmi yoki egalikmi, va egasi bittami yoki ko'pmi", "is_correct": True},
                {"text": "Matnning umumiy ma'nosini tahlil qilib, muallifning maqsadini aniqlayman", "is_correct": False},
                {"text": "Eng uzun variantni tanlayman — SAT rasmiy uslubni afzal ko'radi", "is_correct": False},
                {"text": "Ovoz chiqarib o'qib, qaysi biri chiroyliroq eshitilsa, o'shani tanlayman", "is_correct": False},
            ],
            "explanation": (
                why([
                    (True, "Gapning grammatikasiga qarayman: ko'plikmi yoki egalikmi",
                     "Standard English Conventions savolining javobi <u>qoida</u> bilan "
                     "hal qilinadi, tuyg'u bilan emas. Bu yerda ikki savol bor: "
                     "otdan keyin narsa <em>tegishli</em>mi (egalik) yoki shunchaki "
                     "<em>ko'p</em>mi (ko'plik)? Egasi bittami (<em>researcher's</em>) "
                     "yoki ko'pmi (<em>researchers'</em>)?"),
                    (False, "Matnning umumiy ma'nosini tahlil qilib, muallifning maqsadini aniqlayman",
                     "maqsad bu domenda umuman ahamiyatsiz. Bu — o'qish savoliga "
                     "sarflangan 60 soniya, hech qanday foydasiz."),
                    (False, "Eng uzun variantni tanlayman",
                     "SAT'da uzunlik hech narsani bildirmaydi. Aksincha, Expression of "
                     "Ideas'da qisqaroq variant ko'pincha yutadi — lekin bu ham qoida "
                     "emas, shunchaki kuzatuv."),
                    (False, "Ovoz chiqarib o'qib, qaysi biri chiroyliroq eshitilsa",
                     "«quloqqa yoqimli» usuli o'zbek o'quvchi uchun ayniqsa xavfli: "
                     "ingliz tilida apostrof <u>eshitilmaydi</u> — "
                     "<em>researchers</em> va <em>researchers'</em> bir xil aytiladi. "
                     "Quloq bu savolni hech qachon yecholmaydi."),
                ])
            ),
        },

        {
            "rich_text": (
                "<p><strong>Amaliyot 4.</strong> 1-modulda savol matnlari "
                "<em>«…conforms to the conventions of Standard English?»</em> shakliga "
                "o'tdi. Bundan qanday amaliy xulosa chiqarasiz?</p>"
            ),
            "choices": [
                {"text": "Grammatika guruhiga kirdim — tezlashaman, chunki bu savollar odatda tezroq yechiladi", "is_correct": True},
                {"text": "Imtihon oxiriga yaqinlashdim — sekinlashib, har savolni ikki marta tekshiraman", "is_correct": False},
                {"text": "Xato ko'p qilyapman — kompyuter menga osonroq savollar berayapti", "is_correct": False},
                {"text": "Hech qanday xulosa yo'q — savollar tasodifiy tartibda keladi", "is_correct": False},
            ],
            "explanation": (
                why([
                    (True, "Grammatika guruhiga kirdim — tezlashaman",
                     "domen o'zgarishi — bu <u>xarita</u>. Conventions savollari o'rtacha "
                     "25–40 soniyada yechiladi, chunki javob qoidadan chiqadi. Bu yerda "
                     "tejagan vaqtingizni qiyin o'qish savollariga sarflaysiz."),
                    (False, "Imtihon oxiriga yaqinlashdim — sekinlashaman",
                     "Bluebook tartibida grammatikadan keyin yana Expression of Ideas "
                     "guruhi keladi — oxiri emas. Va sekinlashish — vaqt tugashining "
                     "eng ko'p uchraydigan sababi."),
                    (False, "Xato ko'p qilyapman — kompyuter menga osonroq savollar berayapti",
                     "moslashuv <u>modullar orasida</u> sodir bo'ladi, modul ichida "
                     "emas. 1-modul davomida savollar sizning javoblaringizga qarab "
                     "o'zgarmaydi."),
                    (False, "Hech qanday xulosa yo'q — savollar tasodifiy tartibda keladi",
                     "aynan teskarisi — ular domen bo'yicha guruhlangan va guruh ichida "
                     "qiyinlashib boradi. Buni sezish bepul afzallik."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            '<div class="pp-flashcards" data-pp-flashcards>'
            '<div class="pp-card"><div class="pp-card-front">domain</div><div class="pp-card-back">domen — savollarning katta guruhi</div></div>'
            '<div class="pp-card"><div class="pp-card-front">Craft and Structure</div><div class="pp-card-back">so\'z ma\'nosi, matn tuzilishi va maqsadi</div></div>'
            '<div class="pp-card"><div class="pp-card-front">Information and Ideas</div><div class="pp-card-back">asosiy fikr, dalil va xulosa</div></div>'
            '<div class="pp-card"><div class="pp-card-front">Standard English Conventions</div><div class="pp-card-back">grammatika va tinish belgilari</div></div>'
            '<div class="pp-card"><div class="pp-card-front">Expression of Ideas</div><div class="pp-card-back">bog\'lovchilar va qaydlardan jumla qurish</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to conform to</div><div class="pp-card-back">(qoidaga) mos kelmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">convention</div><div class="pp-card-back">qabul qilingan qoida, me\'yor</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to illustrate a claim</div><div class="pp-card-back">da\'voni misol bilan ko\'rsatmoq</div></div>'
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>To'rt domen: Craft and Structure (~28%), Information and Ideas (~26%), "
            "Standard English Conventions (~26%), Expression of Ideas (~20%).</li>"
            "<li>Grammatika va uslub birgalikda savollarning <strong>deyarli "
            "yarmi</strong> — eng arzon ballar shu yerda.</li>"
            "<li>Savollar <strong>domen bo'yicha guruhlangan</strong>, guruh ichida "
            "oson → qiyin.</li>"
            "<li>Savol matnini o'qib domenni taniysiz — va shu bilan nima qilishni "
            "bilasiz.</li>"
            "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 4
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_STRATEGY,
    "title": "SAT R&W 4: Proof, Not Feeling — The Habit That Raises Every Score",
    "summary": "To'rt qadamli usul: savolni o'qi → javobni oldindan ayt → matndan "
               "isbotni topib ko'rsat → variantlarni yo'q qil. Har savolda ishlaydi.",
    "order": 4,
    "blocks": [
        {"rich_text": (
            "<h2>Isbot, tuyg'u emas</h2>"
            "<p>Bir xil o'quvchi bir xil matnni ikki xil yechishi mumkin. Birinchi "
            "usul: variantlarni o'qib, qaysi biri «to'g'riroq tuyulsa» — o'shani "
            "belgilash. Ikkinchi usul: matndan <u>aniq so'zlarni</u> topib, barmoq "
            "bilan ko'rsatib, «mana shu javobni isbotlaydi» deyish.</p>"
            "<p>Birinchi usul 500–570 ball beradi. Ikkinchisi 650 dan yuqoriga "
            "chiqaradi. Farq lug'atda emas — <mark>odatda</mark>.</p>"
            + NOTE.format(
                "SAT'ning o'zi shu odatga qurilgan: har savolning javobi 60 so'zlik "
                "matn ichida <u>yozib qo'yilgan</u>. Sizdan fikr so'ralmayapti. "
                "Sizdan <strong>topish</strong> so'ralyapti.")
        )},

        {"rich_text": (
            "<h3>To'rt qadam</h3>"
            '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            "<div class=\"pp-step\"><p><strong>1-qadam — savolni birinchi o'qing.</strong> "
            "<em>Main idea</em>mi, <em>main purpose</em>mi, <em>most nearly means</em>mi? "
            "Bu ikki soniya, va u qolgan hamma narsani boshqaradi. Matnni savolni "
            "bilmasdan o'qish — qorong'ida qidirish.</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam — matnni to'liq o'qing va "
            "javobni o'zingiz ayting.</strong> Variantlarga qaramang. O'zingizga "
            "o'zbekcha ayting: «javob shu bo'lishi kerak…». Bu qadam tuzoqlarga "
            "qarshi eng kuchli himoya.</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam — isbotni ko'rsating.</strong> "
            "Matnning qaysi so'zlari javobingizni isbotlaydi? Agar ko'rsatolmasangiz, "
            "javobingiz taxmin — matnga qayting.</p></div>"
            "<div class=\"pp-step\"><p><strong>4-qadam — yo'q qiling, tanlamang.</strong> "
            "Har variantni «bu <u>nega xato</u>?» deb o'qing. To'g'ri javob — "
            "qolgan bittasi. Bu ikkalasi «mumkindek» tuyulganda hal qiladi.</p></div>"
            "</div>"
            + TIP.format(
                "2-qadamni tashlab ketish — eng ko'p uchraydigan xato. Bo'sh bosh "
                "bilan variantlarni o'qigan odam eng aqlli eshitiladigan variantni "
                "tanlaydi. SAT tuzuvchilari buni biladi va o'sha variantni "
                "<u>ataylab</u> yozadi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            '<div class="sr-passage">'
            "<p>By the 1960s, the rivers that fed the Aral Sea had been diverted to "
            "irrigate cotton fields across the surrounding plains. The sea contracted "
            "steadily for the rest of the century, and the fishing towns on its former "
            "shore were left many kilometres from the water. In 2005, a dam was completed "
            "across the strait that had once joined the northern and southern basins. "
            "The northern basin, no longer draining into the south, began to refill; the "
            "southern basin continued to dry.</p>"
            "</div>"
            "<p><strong>Which choice best states the main idea of the text?</strong></p>"
            "<ol type=\"A\">"
            "<li>Cotton farming is the most water-intensive form of agriculture practised in Central Asia.</li>"
            "<li>The Aral Sea shrank after its rivers were diverted, and a later dam reversed that decline in one basin but not the other.</li>"
            "<li>The dam completed in 2005 has restored the Aral Sea to its original size.</li>"
            "<li>The fishing towns along the Aral Sea were abandoned by their residents.</li>"
            "</ol>"
            '<span class="sr-time">⏱ ~55 soniya</span>'
        )},

        {"rich_text": (
            "<h3>To'rt qadam bilan</h3>"
            "<p><strong>1-qadam.</strong> <em>Main idea</em> — matn nimani da'vo "
            "qilyapti.</p>"
            "<p><strong>2-qadam.</strong> Matnning shakli: sabab (daryolar burildi) → "
            "oqibat (dengiz qurídi) → <u>burilish</u> (to'g'on) → ikki xil natija "
            "(shimol to'ladi, janub qurishda davom etdi). Javobim: «daryolar burilgach "
            "dengiz qurídi, keyingi to'g'on esa faqat shimoliy qismini qaytardi».</p>"
            "<p><strong>3-qadam. Isbot:</strong> <em>had been diverted</em> · "
            "<em>contracted steadily</em> · <em>began to refill</em> · <em>the southern "
            "basin continued to dry</em>. To'rtta ibora — butun javob.</p>"
            "<p><strong>4-qadam.</strong></p>"
            + why([
                (True, "The Aral Sea shrank after its rivers were diverted, and a later dam reversed that decline in one basin but not the other",
                 "matnning to'rt bosqichini ham qamrab oladi, va oxirgi qarama-qarshilikni "
                 "(<em>began to refill</em> / <em>continued to dry</em>) saqlaydi."),
                (False, "Cotton farming is the most water-intensive form of agriculture practised in Central Asia",
                 "<strong>tashqi bilim.</strong> Paxta eslatilgan, lekin matn uni "
                 "boshqa ekinlar bilan solishtirmaydi — «eng ko'p suv talab qiladigan» "
                 "degan da'vo bu yerda umuman yo'q."),
                (False, "The dam … has restored the Aral Sea to its original size",
                 "<strong>yarim to'g'ri</strong>: to'g'on bor, to'lish ham bor — lekin "
                 "faqat <u>shimoliy havzada</u>, va «asl hajmiga qaytardi» matnda "
                 "aytilmagan. Bir yarim so'z bilan haddan oshirilgan javob."),
                (False, "The fishing towns … were abandoned by their residents",
                 "<strong>rost, lekin so'ralmagan</strong> — va aslida rost ham emas: "
                 "matn shaharlar suvdan uzoqda qolganini aytadi, aholi ketganini emas. "
                 "Bu bitta tafsilot, asosiy fikr emas."),
            ])
        )},

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>At his observatory in Samarkand, built in the 1420s, Ulugh Beg and his "
                "astronomers compiled a catalogue of more than a thousand stars. The "
                "catalogue's positions were calculated from measurements taken with a "
                "single enormous instrument set into the ground, whose great radius made "
                "small angular differences readable. Later astronomers found the "
                "catalogue's figures remarkably <span class=\"sr-blank\"></span>: for many "
                "stars they differed from modern values by only a few minutes of arc.</p>"
                "</div>"
                "<p><strong>Which choice completes the text with the most logical and "
                "precise word or phrase?</strong></p>"
            ),
            "choices": [
                {"text": "accurate", "is_correct": True},
                {"text": "ambitious", "is_correct": False},
                {"text": "influential", "is_correct": False},
                {"text": "outdated", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joydan keyingi ikki nuqta (<em>:</em>) — bepul sovg'a. Ikki "
                "nuqta «endi tushuntiraman» degani, ya'ni keyingi qism bo'sh joyning "
                "ma'nosini <mark>aytib beradi</mark>: <em>they differed from modern "
                "values by only a few minutes of arc</em> — zamonaviy qiymatlardan "
                "arzimas darajada farq qiladi.</p>"
                + why([
                    (True, "accurate",
                     "«aniq». Ikki nuqtadan keyingi jumla aynan aniqlikni ta'riflaydi. "
                     "Isbot: <em>differed … by only a few minutes of arc</em>."),
                    (False, "ambitious",
                     "«shijoatli» — ming yulduzli katalog haqiqatan shijoatli ish, va "
                     "ko'pchilik shuni tanlaydi. Lekin ikki nuqtadan keyingi jumla "
                     "shijoat haqida emas, <u>o'lchov xatosi</u> haqida. "
                     "<strong>Rost, lekin isbotlanmagan.</strong>"),
                    (False, "influential",
                     "«ta'sirchan» — katalogning keyingi astronomiyaga ta'siri matnda "
                     "muhokama qilinmaydi. <em>Later astronomers found…</em> ular uni "
                     "<u>tekshirdi</u> deydi, undan foydalandi demaydi."),
                    (False, "outdated",
                     "«eskirgan» — mantiqni teskari qiladi. <em>only a few minutes of "
                     "arc</em> maqtov, tanqid emas."),
                ])
                + TIP.format(
                    "Words in Context savolida <strong>ikki nuqta, tire va "
                    "nuqtali vergul</strong>ni qidiring. Ular ko'pincha bo'sh joyning "
                    "ma'nosini keyingi jumlada takrorlaydi — ya'ni javob shundoq "
                    "yozib qo'yilgan bo'ladi.")
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>When a foraging honeybee returns to the hive, it performs a repeating "
                "movement on the vertical surface of the comb. The angle of the movement "
                "corresponds to the direction of the food source relative to the sun, and "
                "its duration corresponds to the distance. Bees that watch the movement "
                "then fly out, and they arrive near the source more often than chance "
                "alone would explain.</p>"
                "</div>"
                "<p><strong>Which choice best states the main idea of the text?</strong></p>"
            ),
            "choices": [
                {"text": "A returning honeybee's movement encodes the direction and distance of food, and other bees use that information.", "is_correct": True},
                {"text": "Honeybees navigate by the position of the sun rather than by landmarks.", "is_correct": False},
                {"text": "The movement performed by returning honeybees is the most complex behaviour known in insects.", "is_correct": False},
                {"text": "Honeybees can locate food sources without any communication between individuals.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>2-qadam (javobni oldindan aytish):</strong> matnda ikki "
                "narsa bor — harakat <u>ma'lumot tashiydi</u> (burchak = yo'nalish, "
                "davomiylik = masofa), va boshqa asalarilar <u>o'sha ma'lumotdan "
                "foydalanadi</u> (<em>more often than chance alone would explain</em>). "
                "To'g'ri javob ikkalasini ham o'z ichiga olishi kerak.</p>"
                + why([
                    (True, "A returning honeybee's movement encodes the direction and distance of food, and other bees use that information",
                     "ikki qismli javob, ikki qismli matnga to'liq mos. Oxirgi jumla — "
                     "«tasodifdan ko'ra ko'proq» — ikkinchi qismning isboti."),
                    (False, "Honeybees navigate by the position of the sun rather than by landmarks",
                     "<strong>so'z-tuzoq</strong>: matnda <em>sun</em> bor, lekin u "
                     "faqat burchakni o'lchash uchun mo'ljal. Matn mo'ljallar "
                     "(<em>landmarks</em>) haqida <u>hech narsa</u> demaydi, shuning "
                     "uchun «ulardan ko'ra ko'proq» degan solishtiruv isbotsiz."),
                    (False, "The movement performed by returning honeybees is the most complex behaviour known in insects",
                     "<strong>doirasi juda keng</strong> va isbotsiz. Matn boshqa "
                     "hasharotlarni umuman eslatmaydi. Eng kuchli («eng…») da'volarga "
                     "har doim shubha bilan qarang."),
                    (False, "Honeybees can locate food sources without any communication between individuals",
                     "matnning aynan teskarisi — butun parcha aloqa haqida. "
                     "Bu variant matndagi so'zlarni ishlatib, ma'nosini ag'darib "
                     "yuboradi."),
                ])
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>Museums have long displayed objects behind glass, arranged by period "
                "and labelled with a date and a place of origin. <span class=\"sr-focus\">"
                "A visitor learns, in this arrangement, everything about when an object "
                "was made and almost nothing about what it was for.</span> Some curators "
                "have begun to group objects instead by use — the tools of a single "
                "workshop, the vessels of a single kitchen — so that a bowl sits beside "
                "the spoon that filled it.</p>"
                "</div>"
                "<p><strong>What is the main purpose of the underlined sentence?</strong></p>"
            ),
            "choices": [
                {"text": "It identifies a limitation of the traditional arrangement that the rest of the text responds to.", "is_correct": True},
                {"text": "It argues that museum labels should include more historical detail.", "is_correct": False},
                {"text": "It provides an example of an object whose purpose is difficult to determine.", "is_correct": False},
                {"text": "It concedes that grouping objects by use would confuse most visitors.", "is_correct": False},
            ],
            "explanation": (
                "<p><em>Main purpose</em> — bu jumla matnda <u>nima ish qilyapti</u>. "
                "Uch jumlaning tuzilishiga qarang: (1) an'anaviy usul; (2) tagi "
                "chizilgan jumla; (3) <em>Some curators have begun to group objects "
                "instead…</em> — <mark>instead</mark> so'zi hal qiladi. Uchinchi jumla "
                "biror <u>muammoga javob</u>, va o'sha muammoni aytgan — ikkinchi "
                "jumla.</p>"
                + why([
                    (True, "It identifies a limitation of the traditional arrangement that the rest of the text responds to",
                     "aynan shu: <em>almost nothing about what it was for</em> — "
                     "kamchilik; <em>instead</em> — unga javob. Jumlaning vazifasi "
                     "matnning burilish nuqtasini yaratish."),
                    (False, "It argues that museum labels should include more historical detail",
                     "<strong>teskari</strong>: matn tarixiy tafsilot <u>yetarli</u>, "
                     "yetishmayotgani — buyumning vazifasi, deydi. Ko'proq sana "
                     "qo'shish muammoni yomonlashtiradi."),
                    (False, "It provides an example of an object whose purpose is difficult to determine",
                     "jumlada hech qanday buyum misoli yo'q — <em>a visitor</em> haqida "
                     "umumiy gap. Misollar (kosa, qoshiq) uchinchi jumlada."),
                    (False, "It concedes that grouping objects by use would confuse most visitors",
                     "matnda tashrifchilarning chalkashishi haqida bir og'iz ham "
                     "yo'q. Bu — o'quvchi o'zi qo'shib yuboradigan e'tiroz."),
                ])
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>A common assumption holds that a language with fewer speakers must be "
                "simpler in structure than a widely spoken one. Linguists who have "
                "described small languages in detail report the opposite as often as not: "
                "many have systems of verb agreement or evidential marking far more "
                "elaborate than those of English. If the assumption were correct, such "
                "descriptions <span class=\"sr-blank\"></span></p>"
                "</div>"
                "<p><strong>Which choice most logically completes the text?</strong></p>"
            ),
            "choices": [
                {"text": "would be rare rather than commonplace.", "is_correct": True},
                {"text": "would need to be repeated by other linguists.", "is_correct": False},
                {"text": "would show that English is unusually elaborate.", "is_correct": False},
                {"text": "would apply only to languages with written traditions.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu shakl — <em>If the assumption were correct, …</em> — SAT'ning "
                "sevimli mantiqiy qolipi. Sizdan so'ralayotgani: "
                "<mark>agar taxmin to'g'ri bo'lganda, biz nimani ko'rgan bo'lardik?</mark></p>"
                "<p>Taxmin: kam so'zlovchili til — soddaroq. Kuzatuv: bunday tillarda "
                "<u>ko'pincha</u> murakkabroq tizimlar topiladi (<em>as often as "
                "not</em>). Agar taxmin to'g'ri bo'lsa, bunday tavsiflar kam "
                "uchrashi kerak edi.</p>"
                + why([
                    (True, "would be rare rather than commonplace",
                     "mantiq to'g'ridan-to'g'ri: taxmin ↔ kuzatuv qarama-qarshi, "
                     "shuning uchun taxmin to'g'ri bo'lsa, kuzatuv kamdan-kam "
                     "bo'lishi kerak edi. <em>as often as not</em> iborasi «kam emas» "
                     "deyapti — javob shu iboraga qarshi turadi."),
                    (False, "would need to be repeated by other linguists",
                     "takrorlash (replication) — ilmiy usul haqidagi umumiy fikr, "
                     "matnda esa bu masala qo'yilmagan. <strong>Tashqi bilim.</strong>"),
                    (False, "would show that English is unusually elaborate",
                     "matn ingliz tilini <u>o'lchov nuqtasi</u> sifatida ishlatadi, "
                     "uni tavsiflamaydi — va aytilgani teskari: boshqa tillar undan "
                     "murakkabroq chiqqan."),
                    (False, "would apply only to languages with written traditions",
                     "yozma an'ana matnda umuman eslatilmaydi. Grammatik jihatdan "
                     "jumla to'g'ri o'qiladi, lekin isbot yo'q — "
                     "<strong>mantiqi xato</strong> tuzog'i."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>To'rtta tuzoq — nomi bilan taniyman</h3>"
            "<p>Bu darsdagi noto'g'ri variantlarning hammasi to'rtta shakldan biriga "
            "kirdi. Ularni <u>nomi bilan</u> o'rganing — imtihonda ular yana keladi:</p>"
            '<div class="sr-data"><div class="sr-data__scroll">'
            "<table>"
            "<thead><tr><th>Tuzoq</th><th>Qanday ko'rinadi</th></tr></thead>"
            "<tbody>"
            "<tr><td>Rost, lekin so'ralmagan</td><td>Matn haqida to'g'ri gap, lekin savolga javob emas</td></tr>"
            "<tr><td>Doirasi noto'g'ri</td><td>Juda keng («eng…», «hamma…») yoki juda tor (bitta tafsilot)</td></tr>"
            "<tr><td>So'z-tuzoq</td><td>Matndagi kuchli so'zni qaytaradi, ma'nosini ag'daradi</td></tr>"
            "<tr><td>Tashqi bilim</td><td>Dunyoda rost, shu 60 so'zda isbotlanmagan</td></tr>"
            "</tbody></table>"
            "</div></div>"
            + WARN.format(
                "Eng xavflisi — <strong>tashqi bilim</strong>. Mavzuni "
                "bilganingizda kuchayadi: Orol dengizi haqidagi matnda o'zbek "
                "o'quvchi maktabda o'qigan hamma narsani eslaydi va o'sha "
                "bilimni variantlarda «tanib qoladi». Qoida bitta: "
                "<u>isbotni ekranda ko'rsatolmasangiz — bu javob emas</u>.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            '<div class="pp-flashcards" data-pp-flashcards>'
            '<div class="pp-card"><div class="pp-card-front">to state the main idea</div><div class="pp-card-back">asosiy fikrni ifodalamoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to diverge / to be diverted</div><div class="pp-card-back">boshqa tomonga burilmoq / burilgan bo\'lmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to contract (of a sea)</div><div class="pp-card-back">qisqarmoq, torayib bormoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">remarkably accurate</div><div class="pp-card-back">hayratlanarli darajada aniq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to correspond to</div><div class="pp-card-back">(biror narsaga) mos kelmoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">a limitation</div><div class="pp-card-back">kamchilik, cheklov</div></div>'
            '<div class="pp-card"><div class="pp-card-front">to concede</div><div class="pp-card-back">tan olmoq, yon bermoq</div></div>'
            '<div class="pp-card"><div class="pp-card-front">as often as not</div><div class="pp-card-back">kamida yarim hollarda, kam emas</div></div>'
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li><strong>1.</strong> Savolni birinchi o'qing — <em>idea</em>mi, "
            "<em>purpose</em>mi, <em>means</em>mi.</li>"
            "<li><strong>2.</strong> Variantlarga qaramasdan javobni o'zingiz ayting.</li>"
            "<li><strong>3.</strong> Matndan isbotni ko'rsating. Ko'rsatolmasangiz — "
            "bu taxmin.</li>"
            "<li><strong>4.</strong> «Nega xato?» deb yo'q qiling; qolgani — javob.</li>"
            "<li>To'rt tuzoq: rost-lekin-so'ralmagan · doirasi noto'g'ri · so'z-tuzoq · "
            "tashqi bilim.</li>"
            "</ul>"
        )},
    ],
},

]
