"""Study abroad — batch 2: the other scholarships, as short cards.

Researched 2026-10-01. Only facts found on the official pages (or the official
announcement of the latest cycle) are stated; a period that is only a pattern
is called "usually", and a date not yet announced is an estimate.

  · Chevening 2027/28 — chevening.org application timeline: opened 4 Aug 2026,
    closes 6 Oct 2026 11:00 UTC; interviews Mar–Apr 2027; results mid-June 2027.
  · Türkiye Bursları 2026 — official announcement: 10 Jan – 20 Feb 2026.
  · MEXT — studyinjapan.go.jp: embassy and university recommendation; monthly
    ¥117,000–145,000 by programme; tuition exempt; round-trip airfare.
  · Stipendium Hungaricum — Uzbekistan's Sending Partner is the Ministry of
    Higher Education; the call usually opens in November and closes mid-January.
  · CSC, Fulbright, DAAD, Erasmus Mundus, El-Yurt Umidi — process only, no
    dates: each programme or embassy announces its own.

    python manage.py import_abroad abroad/management/commands/_abroad_scholarships_2.py --author=prime
"""
CHECKED = "2026-10-01"


def card(slug, order, name, full_name, flag, country, country_uz, levels, languages,
         summary, summary_uz, covers, covers_uz, period, period_uz, url):
    return {
        "slug": slug, "order": order, "name": name, "full_name": full_name, "flag": flag,
        "country": country, "country_uz": country_uz, "depth": "card",
        "levels": levels, "languages": languages, "fully_funded": True,
        "summary": summary, "summary_uz": summary_uz,
        "covers": covers, "covers_uz": covers_uz,
        "usual_period": period, "usual_period_uz": period_uz,
        "official_url": url, "last_checked": CHECKED,
    }


SCHOLARSHIPS = [
    card("mext", 2, "MEXT", "Japanese Government (Monbukagakusho) Scholarship", "🇯🇵",
         "Japan", "Yaponiya", "bachelor,master,phd", "japanese,english",
         "Japan's government scholarship. Apply through the Embassy of Japan (embassy recommendation) or be nominated by a Japanese university.",
         "Yaponiya hukumati stipendiyasi. Yaponiya elchixonasi orqali (elchixona tavsiyasi) topshirasiz yoki Yaponiya universiteti sizni tavsiya qiladi.",
         "<ul><li>Tuition exempt</li><li>Monthly allowance of ¥117,000–145,000, depending on the programme</li><li>Round-trip airfare</li><li>Undergraduates usually start with a preparatory year that includes Japanese</li></ul><p class=\"ab-src\">Source: Study in Japan (official), checked 1 Oct 2026.</p>",
         "<ul><li>Kontrakt toʻlanmaydi</li><li>Dasturga qarab oyiga 117 000–145 000 iyena</li><li>Borish-kelish aviabileti</li><li>Bakalavrlar odatda yapon tili ham oʻqitiladigan tayyorlov yilidan boshlaydi</li></ul><p class=\"ab-src\">Manba: Study in Japan (rasmiy), 2026-yil 1-oktabrda tekshirilgan.</p>",
         "Embassy round usually in spring (about April–May) for study from the following April",
         "Elchixona bosqichi odatda bahorda (taxminan aprel–may), oʻqish keyingi yil aprelidan",
         "https://www.studyinjapan.go.jp/en/planning/scholarships/mext-scholarships/"),
    card("turkiye", 3, "Türkiye Bursları", "Türkiye Scholarships", "🇹🇷",
         "Türkiye", "Turkiya", "bachelor,master,phd", "english,any",
         "Türkiye's government scholarship for every level, with one online application and university placement done for you.",
         "Turkiya hukumatining barcha darajalar uchun stipendiyasi: bitta onlayn ariza, universitetga joylashtirishni ular oʻzi qiladi.",
         "<ul><li>Tuition</li><li>Monthly stipend</li><li>Accommodation</li><li>Health insurance</li><li>University placement</li></ul><p>Amounts and the Turkish-language year are described in the official call.</p><p class=\"ab-src\">Source: turkiyeburslari.gov.tr, 2026 announcement.</p>",
         "<ul><li>Kontrakt</li><li>Oylik stipendiya</li><li>Yotoqxona</li><li>Tibbiy sugʻurta</li><li>Universitetga joylashtirish</li></ul><p>Miqdorlar va turk tili yili rasmiy eʼlonda yozilgan.</p><p class=\"ab-src\">Manba: turkiyeburslari.gov.tr, 2026-yil eʼloni.</p>",
         "Usually January–February (2026: 10 January – 20 February)",
         "Odatda yanvar–fevral (2026: 10-yanvar – 20-fevral)",
         "https://www.turkiyeburslari.gov.tr/"),
    card("hungary", 4, "Stipendium Hungaricum", "Hungarian Government Scholarship", "🇭🇺",
         "Hungary", "Vengriya", "bachelor,master,phd", "english",
         "Study in Hungary, mostly in English, on a government scholarship. You apply twice: on the Stipendium Hungaricum portal and through Uzbekistan's Sending Partner.",
         "Vengriyada, asosan ingliz tilida, davlat stipendiyasi bilan oʻqish. Ikki joyga topshirasiz: Stipendium Hungaricum portaliga va Oʻzbekistonning «Sending Partner»i orqali.",
         "<ul><li>Tuition-free study</li><li>Monthly stipend</li><li>Accommodation or a housing contribution</li><li>Medical insurance</li></ul><p>Uzbekistan's Sending Partner is the Ministry of Higher Education, Science and Innovation — follow its own call too.</p><p class=\"ab-src\">Source: stipendiumhungaricum.hu.</p>",
         "<ul><li>Bepul oʻqish</li><li>Oylik stipendiya</li><li>Yotoqxona yoki uy-joy uchun toʻlov</li><li>Tibbiy sugʻurta</li></ul><p>Oʻzbekistonning «Sending Partner»i — Oliy taʼlim, fan va innovatsiyalar vazirligi; uning eʼloniga ham amal qiling.</p><p class=\"ab-src\">Manba: stipendiumhungaricum.hu.</p>",
         "Usually opens in November and closes in mid-January",
         "Odatda noyabrda ochilib, yanvar oʻrtalarida yopiladi",
         "https://stipendiumhungaricum.hu/"),
    card("csc", 5, "CSC", "Chinese Government Scholarship", "🇨🇳",
         "China", "Xitoy", "bachelor,master,phd", "english,any",
         "China's government scholarship. Apply through the Chinese Embassy (bilateral programme) or through a Chinese university, on the Campus China portal.",
         "Xitoy hukumati stipendiyasi. Xitoy elchixonasi (ikki tomonlama dastur) yoki Xitoy universiteti orqali, Campus China portalida topshiriladi.",
         "<p>A full scholarship usually includes tuition, accommodation, a monthly stipend and medical insurance; Chinese-taught programmes start with a Chinese-language year. Exact terms are in each year's call.</p>",
         "<p>Toʻliq stipendiya odatda kontrakt, yotoqxona, oylik stipendiya va tibbiy sugʻurtani oʻz ichiga oladi; xitoy tilidagi dasturlar xitoy tili yilidan boshlanadi. Aniq shartlar har yilgi eʼlonda.</p>",
         "Usually winter to early spring; each embassy and university sets its own deadline",
         "Odatda qishdan erta bahorgacha; har bir elchixona va universitet oʻz muddatini belgilaydi",
         "https://www.campuschina.org/"),
    card("chevening", 6, "Chevening", "UK Government's Chevening Scholarships", "🇬🇧",
         "United Kingdom", "Buyuk Britaniya", "master", "english",
         "A one-year master's at any UK university, funded by the UK government, for future leaders with work experience.",
         "Buyuk Britaniyaning istalgan universitetida bir yillik magistratura, Buyuk Britaniya hukumati hisobidan — ish tajribasi bor boʻlajak yetakchilar uchun.",
         "<ul><li>Tuition</li><li>Monthly living allowance</li><li>Return flight to the UK</li><li>Visa costs</li></ul><p>Chevening asks for work experience and a commitment to return home after the degree — read the eligibility page before you start.</p><p class=\"ab-src\">Source: chevening.org.</p>",
         "<ul><li>Kontrakt</li><li>Oylik yashash puli</li><li>Buyuk Britaniyaga borish-kelish bileti</li><li>Viza xarajatlari</li></ul><p>Chevening ish tajribasi va oʻqishdan keyin vatanga qaytish majburiyatini talab qiladi — boshlashdan oldin shartlar sahifasini oʻqing.</p><p class=\"ab-src\">Manba: chevening.org.</p>",
         "Opens in August, closes in early October",
         "Avgustda ochilib, oktabr boshida yopiladi",
         "https://www.chevening.org/scholarship/uzbekistan/"),
    card("fulbright", 7, "Fulbright", "Fulbright Foreign Student Program", "🇺🇸",
         "United States", "AQSh", "master", "english",
         "A master's in the United States for graduates from Uzbekistan, run by the U.S. Embassy in Tashkent.",
         "Oʻzbekistonlik bitiruvchilar uchun AQShda magistratura; Toshkentdagi AQSh elchixonasi oʻtkazadi.",
         "<p>Tuition, a monthly stipend, health insurance and visa support. Applicants need a bachelor's degree and professional experience; the embassy's page lists the current requirements and English tests.</p><p class=\"ab-src\">Source: U.S. Embassy in Uzbekistan.</p>",
         "<p>Kontrakt, oylik stipendiya, tibbiy sugʻurta va viza yordami. Nomzodga bakalavr diplomi va ish tajribasi kerak; amaldagi talablar va ingliz tili testlari elchixona sahifasida.</p><p class=\"ab-src\">Manba: AQShning Oʻzbekistondagi elchixonasi.</p>",
         "Once a year — announced by the U.S. Embassy in Tashkent",
         "Yiliga bir marta — Toshkentdagi AQSh elchixonasi eʼlon qiladi",
         "https://uz.usembassy.gov/fulbright-foreign-student-program/"),
    card("daad", 8, "DAAD", "German Academic Exchange Service scholarships", "🇩🇪",
         "Germany", "Germaniya", "master,phd", "english",
         "Germany's scholarship organisation: many programmes for master's and PhD students, each with its own rules and deadline.",
         "Germaniyaning stipendiya tashkiloti: magistratura va PhD uchun koʻplab dasturlar, har birining oʻz qoidasi va muddati bor.",
         "<p>Use the DAAD scholarship database: choose your country and level and it lists what you can apply for. Many German university programmes are tuition-free anyway, so a DAAD award is often about living costs.</p><div class=\"ab-mistake\"><strong>Documents for Germany</strong><p>Germany does not accept apostilles from Uzbekistan — plan for consular legalisation.</p></div>",
         "<p>DAAD stipendiyalar bazasidan foydalaning: davlatingiz va darajani tanlasangiz, nimaga topshirish mumkinligini koʻrsatadi. Koʻp nemis universitet dasturlari baribir bepul, shuning uchun DAAD granti koʻpincha yashash xarajatlari uchun.</p><div class=\"ab-mistake\"><strong>Germaniya uchun hujjatlar</strong><p>Germaniya Oʻzbekiston apostilini qabul qilmaydi — konsullik legalizatsiyasini rejalashtiring.</p></div>",
         "Depends on the programme — see the DAAD database",
         "Dasturga bogʻliq — DAAD bazasiga qarang",
         "https://www.daad.de/en/studying-in-germany/scholarships/"),
    card("erasmus", 9, "Erasmus Mundus", "Erasmus Mundus Joint Masters", "🇪🇺",
         "European Union", "Yevropa Ittifoqi", "master", "english",
         "One master's in two or more European countries. Each joint programme picks its students and gives full scholarships to the best.",
         "Ikki yoki undan ortiq Yevropa davlatida bitta magistratura. Har bir qoʻshma dastur talabalarni oʻzi tanlaydi va eng yaxshilariga toʻliq stipendiya beradi.",
         "<p>You apply to a programme, not to a central office. Browse the official catalogue, then follow that programme's own deadline and requirements.</p>",
         "<p>Siz markaziy idoraga emas, dasturga topshirasiz. Rasmiy katalogni koʻrib chiqing, keyin oʻsha dasturning oʻz muddati va talablariga amal qiling.</p>",
         "Set by each programme — many close between October and January",
         "Har bir dastur oʻzi belgilaydi — koʻplari oktabr–yanvar oraligʻida yopiladi",
         "https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en"),
    card("eyuf", 10, "El-Yurt Umidi", "“El-Yurt Umidi” Foundation (Uzbekistan)", "🇺🇿",
         "Uzbekistan → abroad", "Oʻzbekiston → xorij", "bachelor,master,phd", "english,any",
         "Uzbekistan's own foundation that funds study at leading universities abroad, for bachelor's, master's and doctoral programmes.",
         "Oʻzbekistonning oʻz jamgʻarmasi: xorijdagi yetakchi universitetlarda bakalavriat, magistratura va doktoranturada oʻqishni moliyalashtiradi.",
         "<p>Selections are announced as “open scholarship competitions”, several times a year, each with its own list of places and conditions. Applications go through the foundation's admission portal.</p>",
         "<p>Tanlovlar yiliga bir necha marta «ochiq stipendiya tanlovi» sifatida eʼlon qilinadi, har birining oʻz oʻrinlar roʻyxati va shartlari bor. Hujjatlar jamgʻarmaning qabul portali orqali topshiriladi.</p>",
         "Several competitions a year — watch the foundation's announcements",
         "Yiliga bir necha tanlov — jamgʻarma eʼlonlarini kuzatib boring",
         "https://eyuf.uz/"),
]

DEADLINES = [
    {
        "scholarship": "chevening",
        "label": "Chevening 2027/28", "label_uz": "Chevening 2027/28",
        "opens": "2026-08-04", "closes": "2026-10-06",
        "note": "Closes 6 October 2026 at 11:00 UTC (16:00 Tashkent). Interviews March–April 2027; results mid-June 2027.",
        "note_uz": "2026-yil 6-oktabr, 11:00 UTC (Toshkent vaqti bilan 16:00) da yopiladi. Suhbatlar 2027-yil mart–aprel; natijalar 2027-yil iyun oʻrtasida.",
        "source_url": "https://www.chevening.org/scholarships/application-timeline/", "last_checked": CHECKED,
    },
    {
        "scholarship": "hungary",
        "label": "Stipendium Hungaricum 2027/28", "label_uz": "Stipendium Hungaricum 2027/28",
        "opens": None, "closes": "2027-01-15", "is_estimate": True,
        "note": "Estimate: the call usually closes in mid-January. Confirm the date in the official call when it opens (usually November).",
        "note_uz": "Taxmin: eʼlon odatda yanvar oʻrtasida yopiladi. Sanani rasmiy eʼlon chiqqanda tasdiqlang (odatda noyabrda).",
        "source_url": "https://stipendiumhungaricum.hu/apply/", "last_checked": CHECKED,
    },
    {
        "scholarship": "turkiye",
        "label": "Türkiye Bursları 2027", "label_uz": "Türkiye Bursları 2027",
        "opens": None, "closes": "2027-02-20", "is_estimate": True,
        "note": "Estimate from the 2026 cycle (10 January – 20 February 2026).",
        "note_uz": "2026-yilgi tsikl asosida taxmin (2026-yil 10-yanvar – 20-fevral).",
        "source_url": "https://www.turkiyeburslari.gov.tr/announcements/turkiye-scholarships-2026-applications-121", "last_checked": CHECKED,
    },
]
