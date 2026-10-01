"""Study abroad — Erasmus Mundus Joint Masters (full page).

This file held the short scholarship cards of batch 2. One by one every card
became a full page in its own file (MEXT, Türkiye Bursları, Stipendium
Hungaricum, Chevening, CSC, El-Yurt Umidi, DAAD, Fulbright); Erasmus Mundus,
the last one, became a full page here on 2026-10-01. The file keeps its name
because temporary.txt already lists it for production.

Sources, read 2026-10-01:
  · erasmus-plus.ec.europa.eu — EMJM for students: bachelor's degree or final
    bachelor's year (graduate before the master's starts); apply directly to
    the consortium; applications mostly October–January; the scholarship
    covers participation costs and contributes to travel, visa and a living
    allowance; €1,400 a month, at most 24 months (programme guide).
  · EACEA — the EMJM catalogue: 60, 90 or 120 ECTS (12, 18 or 24 months),
    delivered by institutions in several countries.

    python manage.py import_abroad abroad/management/commands/_abroad_scholarships_2.py --author=prime --republish
"""
CHECKED = "2026-10-01"

COVERS = """
<ul><li>A living allowance of <strong>€1,400 a month</strong>, for up to 24 months</li><li>Participation costs (tuition and related fees)</li><li>A contribution to travel and visa costs</li></ul>
<p>Not every admitted student gets the scholarship: programmes also admit self-funded students, and award the EU scholarships to their highest-ranked applicants.</p>
<p class="ab-src">Source: Erasmus+ — Erasmus Mundus Joint Masters (students) and programme guide.</p>
"""
COVERS_UZ = """
<ul><li>Oyiga <strong>1 400 yevro</strong> yashash puli, 24 oygacha</li><li>Ishtirok xarajatlari (kontrakt va shunga bogʻliq toʻlovlar)</li><li>Yoʻl va viza xarajatlariga hissa</li></ul>
<p>Qabul qilinganlarning hammasi ham stipendiya olmaydi: dasturlar oʻz hisobidan oʻqiydigan talabalarni ham qabul qiladi va Yevropa Ittifoqi stipendiyalarini eng yuqori reytingli nomzodlarga beradi.</p>
<p class="ab-src">Manba: Erasmus+ — Erasmus Mundus Joint Masters (talabalar uchun) va dastur qoʻllanmasi.</p>
"""

BODY = """
<ul class="ab-toc">
<li><a href="#what">What it is</a></li><li><a href="#who">Who can apply</a></li><li><a href="#how">How to apply</a></li>
<li><a href="#choose">Choosing programmes</a></li><li><a href="#tips">Tips</a></li>
</ul>

<h2 id="what">What it is</h2>
<p>An Erasmus Mundus Joint Master is <strong>one master's programme run by a group of universities</strong> in different countries. You study in at least two of them — for example, a first year in Spain and a second in Sweden — and graduate with a joint or multiple degree. Programmes last 12, 18 or 24 months, and most are taught in English.</p>
<p>There is no central Erasmus Mundus application: <strong>each programme selects its own students</strong> and gives the EU scholarships to the best of them.</p>

<h2 id="who">Who can apply</h2>
<ul>
<li>Students from anywhere in the world, including Uzbekistan.</li>
<li>A bachelor's degree — or you are in your <strong>final bachelor's year</strong> and will graduate before the master's starts.</li>
<li>Each programme adds its own requirements: subject background, grades, English level.</li>
</ul>
<div class="ab-uz"><strong>A master's without work experience</strong><p>Unlike Chevening, Fulbright or DAAD's EPOS, most Erasmus Mundus programmes do not require years of work. For a strong final-year student in Uzbekistan it is often the most realistic fully funded master's in Europe.</p></div>

<h2 id="how">How to apply</h2>
<ol class="ab-steps">
<li>Search the <strong>EACEA Erasmus Mundus catalogue</strong> by field.</li>
<li>Open each programme's own website: requirements, documents, deadline.</li>
<li>Apply <strong>directly to the programme</strong>, usually between October and January for study starting the following autumn.</li>
<li>Programmes rank applicants; the top ones receive the scholarship, others may be offered a self-funded place or a waiting-list position.</li>
</ol>
<p>Typical documents: degree and transcripts (with translations), CV, motivation letter, recommendation letters, English certificate, passport — each programme lists its own.</p>

<h2 id="choose">Choosing programmes</h2>
<ul>
<li><strong>Fit beats fame.</strong> Pick programmes whose modules match what you studied and what you want to do — the motivation letter has to show it.</li>
<li><strong>Read the partner universities and the mobility path</strong> — which countries, in which semester.</li>
<li><strong>Check the deadline for scholarship applicants</strong> — some programmes have an earlier date for scholarship candidates than for self-funded ones.</li>
</ul>

<h2 id="tips">Tips</h2>
<ul>
<li>Start in <strong>September</strong>: shortlist programmes, book IELTS, ask for recommendations.</li>
<li>Write <strong>a different motivation letter for each programme</strong> — name its modules, its partner universities, and why this mobility path.</li>
<li>Documents for several EU countries: check each country's rule on apostille. Germany, Austria and Greece do not accept Uzbek apostilles.</li>
</ul>
<p class="ab-src">Sources: Erasmus+ (erasmus-plus.ec.europa.eu) — Erasmus Mundus Joint Masters for students and programme guide; EACEA catalogue (checked 1 October 2026).</p>
"""

BODY_UZ = """
<ul class="ab-toc">
<li><a href="#what">Bu nima</a></li><li><a href="#who">Kim topshira oladi</a></li><li><a href="#how">Qanday topshiriladi</a></li>
<li><a href="#choose">Dastur tanlash</a></li><li><a href="#tips">Maslahatlar</a></li>
</ul>

<h2 id="what">Bu nima</h2>
<p>Erasmus Mundus Joint Master — turli davlatlardagi universitetlar guruhi <strong>birgalikda oʻtkazadigan bitta magistratura dasturi</strong>. Siz ulardan kamida ikkitasida oʻqiysiz — masalan, birinchi yil Ispaniyada, ikkinchisi Shvetsiyada — va qoʻshma yoki bir nechta diplom bilan bitirasiz. Dasturlar 12, 18 yoki 24 oy davom etadi, koʻpchiligi ingliz tilida.</p>
<p>Markaziy Erasmus Mundus arizasi yoʻq: <strong>har bir dastur talabalarini oʻzi tanlaydi</strong> va Yevropa Ittifoqi stipendiyalarini eng yaxshilariga beradi.</p>

<h2 id="who">Kim topshira oladi</h2>
<ul>
<li>Dunyoning istalgan joyidan, jumladan Oʻzbekistondan talabalar.</li>
<li>Bakalavr diplomi — yoki magistratura boshlanishidan oldin bitiradigan <strong>bakalavriatning oxirgi kursi</strong> talabasi.</li>
<li>Har bir dastur oʻz talablarini qoʻshadi: fan boʻyicha tayyorgarlik, baholar, ingliz tili darajasi.</li>
</ul>
<div class="ab-uz"><strong>Ish tajribasisiz magistratura</strong><p>Chevening, Fulbright yoki DAAD EPOS'dan farqli oʻlaroq, koʻp Erasmus Mundus dasturlari yillab ish tajribasini talab qilmaydi. Oʻzbekistondagi kuchli bitiruvchi kurs talabasi uchun bu koʻpincha Yevropadagi eng real toʻliq moliyalashtirilgan magistratura.</p></div>

<h2 id="how">Qanday topshiriladi</h2>
<ol class="ab-steps">
<li><strong>EACEA Erasmus Mundus katalogi</strong>dan soha boʻyicha qidiring.</li>
<li>Har bir dasturning oʻz saytini oching: talablar, hujjatlar, muddat.</li>
<li><strong>Toʻgʻridan-toʻgʻri dasturga</strong> topshiring — odatda oktabr–yanvar oraligʻida, keyingi kuzda boshlanadigan oʻqish uchun.</li>
<li>Dasturlar nomzodlarni reytinglaydi; eng yuqoridagilar stipendiya oladi, boshqalarga oʻz hisobidan oʻrin yoki kutish roʻyxati taklif qilinishi mumkin.</li>
</ol>
<p>Odatdagi hujjatlar: diplom va baholar varaqasi (tarjima bilan), CV, motivatsion xat, tavsiyanomalar, ingliz tili sertifikati, pasport — har bir dastur oʻz roʻyxatini beradi.</p>

<h2 id="choose">Dastur tanlash</h2>
<ul>
<li><strong>Moslik — mashhurlikdan muhim.</strong> Modullari siz oʻqigan va qilmoqchi boʻlgan ishingizga mos dasturlarni tanlang — motivatsion xat buni koʻrsatishi kerak.</li>
<li><strong>Hamkor universitetlar va mobillik yoʻlini oʻqing</strong> — qaysi davlatlar, qaysi semestrda.</li>
<li><strong>Stipendiya nomzodlari uchun muddatni tekshiring</strong> — baʼzi dasturlarda stipendiya nomzodlari uchun muddat oʻz hisobidan oʻqiydiganlarnikidan oldinroq.</li>
</ul>

<h2 id="tips">Maslahatlar</h2>
<ul>
<li><strong>Sentabrda</strong> boshlang: dasturlar roʻyxatini tuzing, IELTSga yoziling, tavsiyanoma soʻrang.</li>
<li><strong>Har bir dastur uchun alohida motivatsion xat</strong> yozing — uning modullarini, hamkor universitetlarini va nega aynan shu mobillik yoʻlini tanlaganingizni ayting.</li>
<li>Bir nechta Yevropa Ittifoqi davlati uchun hujjatlar: har bir davlatning apostil qoidasini tekshiring. Germaniya, Avstriya va Gretsiya oʻzbek apostilini qabul qilmaydi.</li>
</ul>
<p class="ab-src">Manbalar: Erasmus+ (erasmus-plus.ec.europa.eu) — talabalar uchun Erasmus Mundus Joint Masters va dastur qoʻllanmasi; EACEA katalogi (2026-yil 1-oktabrda tekshirilgan).</p>
"""

SCHOLARSHIPS = [{
    "slug": "erasmus", "order": 9, "name": "Erasmus Mundus", "full_name": "Erasmus Mundus Joint Masters",
    "flag": "🇪🇺", "country": "European Union", "country_uz": "Yevropa Ittifoqi", "depth": "full",
    "levels": "master", "languages": "english", "fully_funded": True,
    "summary": "One master's in two or more European countries, mostly in English, with €1,400 a month for the best applicants. No work experience needed; final-year students can apply.",
    "summary_uz": "Ikki yoki undan ortiq Yevropa davlatida, asosan ingliz tilida bitta magistratura; eng yaxshi nomzodlarga oyiga 1 400 yevro. Ish tajribasi shart emas; bitiruvchi kurs talabalari topshira oladi.",
    "covers": COVERS, "covers_uz": COVERS_UZ,
    "usual_period": "Each programme sets its own deadline — mostly October to January",
    "usual_period_uz": "Har bir dastur oʻz muddatini belgilaydi — asosan oktabrdan yanvargacha",
    "body": BODY, "body_uz": BODY_UZ,
    "official_url": "https://erasmus-plus.ec.europa.eu/opportunities/opportunities-for-individuals/students/erasmus-mundus-joint-masters-scholarships",
    "last_checked": CHECKED,
}]

DEADLINES = []

CHECKLISTS = {
    "erasmus": [
        {"text": "Bachelor's degree, or graduating before the master's starts", "text_uz": "Bakalavr diplomi yoki magistratura boshlanishidan oldin bitirish"},
        {"text": "3–5 programmes shortlisted from the EACEA catalogue", "text_uz": "EACEA katalogidan 3–5 ta dastur tanlandi"},
        {"text": "Each programme's deadline noted — including any earlier one for scholarship applicants", "text_uz": "Har bir dasturning muddati yozib olindi — stipendiya nomzodlari uchun oldingisi ham"},
        {"text": "IELTS or the English test each programme asks for", "text_uz": "Har bir dastur soʻraydigan IELTS yoki ingliz tili testi"},
        {"text": "Degree/transcripts with certified translations", "text_uz": "Diplom va baholar varaqasi, tasdiqlangan tarjima bilan"},
        {"text": "CV", "text_uz": "CV"},
        {"text": "A separate motivation letter for each programme", "text_uz": "Har bir dastur uchun alohida motivatsion xat"},
        {"text": "Recommendation letters as each programme asks", "text_uz": "Har bir dastur soʻragan tavsiyanomalar"},
        {"text": "Passport", "text_uz": "Pasport"},
        {"text": "Apostille or legalisation rule checked for each country on the mobility path", "text_uz": "Mobillik yoʻlidagi har bir davlat uchun apostil yoki legalizatsiya qoidasi tekshirildi"},
    ],
}

SAMPLES = [{
    "slug": "erasmus-motivation", "order": 14, "kind": "statement", "scholarship": "erasmus",
    "title": "Erasmus Mundus motivation letter — Bekzod, data science (final-year student)",
    "title_uz": "Erasmus Mundus motivatsion xati — Bekzod, maʼlumotlar ilmi (bitiruvchi kurs talabasi)",
    "intro": "<p>Bekzod is fictional: a final-year applied-mathematics student in Tashkent, with no full-time work yet — the typical Erasmus Mundus applicant. A joint master is chosen for its <strong>modules and its mobility path</strong>, so the letter must be about that programme and no other.</p>",
    "intro_uz": "<p>Bekzod — oʻylab topilgan qahramon: Toshkentdagi amaliy matematika bitiruvchi kurs talabasi, hali toʻliq ish tajribasi yoʻq — Erasmus Mundus uchun odatiy nomzod. Qoʻshma magistratura <strong>modullari va mobillik yoʻli</strong> uchun tanlanadi, shuning uchun xat aynan oʻsha dastur haqida boʻlishi kerak.</p>",
    "letter": """
<p>Dear Selection Committee,</p>
<p>I am a final-year student of applied mathematics in Tashkent, graduating in June, and I am applying to your joint master's in data science. Last year, for my course project, I analysed three years of public transport data from my city and found that two bus routes carried a third of all passengers while their timetables had not changed in a decade. Presenting this to the city transport office was the first time I saw data change a real decision: one route now runs every eight minutes instead of fifteen.</p>
<p>My studies have given me a solid base in statistics, linear algebra and programming in Python, and I have completed online courses in machine learning. What I lack is experience with large real-world datasets and with the ethics of using personal data — two areas this programme treats seriously.</p>
<p>The programme's structure is the reason I am applying to it and not to a single university. The first year's focus on statistical foundations matches what I need to strengthen, and the second year's specialisation in urban data at the partner university is exactly the field my project opened for me. Studying in two countries would also let me compare how two European cities use data in transport.</p>
<p>After graduating, I want to return to Uzbekistan and work in a city administration or a transport company, helping Tashkent and other growing cities plan with data. I also plan to keep sharing what I learn with students at my university's data club, which I co-founded in my second year.</p>
<p>Sincerely,<br>Bekzod Tursunov</p>
""",
    "notes": [
        {"para": 2, "en": "Who he is (final-year, graduating before the start — an eligibility point) and a <strong>project with a real result</strong> instead of work experience.", "uz": "U kim (bitiruvchi kurs, oʻqish boshlanishidan oldin bitiradi — shart sifatida muhim) va ish tajribasi oʻrniga <strong>haqiqiy natijali loyiha</strong>."},
        {"para": 3, "en": "An honest account of strengths <strong>and gaps</strong> — and the gaps are exactly what the programme teaches.", "uz": "Kuchli tomonlar <strong>va boʻshliqlar</strong>ning halol bayoni — boʻshliqlar esa aynan dastur oʻrgatadigan narsalar."},
        {"para": 4, "en": "Why this joint programme: year by year, and why the <strong>mobility path</strong> matters. Replace the details with your programme's real ones.", "uz": "Nega aynan shu qoʻshma dastur: yilma-yil va nega <strong>mobillik yoʻli</strong> muhim. Tafsilotlarni dasturingizning haqiqiylari bilan almashtiring."},
        {"para": 5, "en": "A realistic plan at home, plus something he already does for others — committees like applicants who multiply what they learn.", "uz": "Vatandagi real reja va boshqalar uchun allaqachon qilayotgan ishi — komissiya oʻrganganini koʻpaytiradigan nomzodlarni yoqtiradi."},
    ],
    "prompts": [
        {"en": "Your year of study, graduation date, and one project with a real result.", "uz": "Kursingiz, bitirish sanasi va haqiqiy natijali bitta loyiha.", "lines": 3},
        {"en": "What you are strong in — and two honest gaps.", "uz": "Nimada kuchlisiz — va ikkita halol boʻshliq.", "lines": 3},
        {"en": "For THIS programme: what you take in year one, where you go in year two, and why.", "uz": "AYNAN shu dastur uchun: birinchi yilda nima oʻqiysiz, ikkinchi yilda qayerga borasiz va nega.", "lines": 4},
        {"en": "Your plan in Uzbekistan, and how you will pass on what you learn.", "uz": "Oʻzbekistondagi rejangiz va oʻrganganingizni boshqalarga qanday yetkazasiz.", "lines": 3},
    ],
}]
