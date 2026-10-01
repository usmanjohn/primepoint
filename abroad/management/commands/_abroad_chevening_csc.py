"""Study abroad — Chevening and CSC, in depth, plus an annotated Chevening essay.

Sources, read 2026-10-01:
  Chevening (chevening.org): application timeline 2027/28 (opens 4 Aug 2026,
    closes 6 Oct 2026 11:00 UTC; interviews Mar–Apr 2027; results mid-June
    2027); eligibility (citizen of an eligible country, return home ≥ 2 years,
    2 years' / 2,800 hours' work experience after the degree, three UK
    courses, an unconditional offer by the deadline); FAQ — the Chevening
    English requirement was removed in 2020, universities keep theirs;
    references — two referees, professional or academic; offer deadline
    8 July 2027, 17:00 UK time; application criteria — four areas:
    leadership, networking, studying in the UK, career plan.
    NOT stated: a word count — secondary sites say 500; the page says "the
    limit shown in the form".
  CSC (Chinese Government Scholarship) — official notice of a Chinese embassy
    for 2026/2027 (programme-wide rules): age limits, HSK levels, the CSCA
    test for undergraduates, documents, Type A via campuschina.org, results
    July–August. Uzbekistan's agency number and deadline are set by the
    Chinese Embassy in Tashkent — not stated here, no countdown.

    python manage.py import_abroad abroad/management/commands/_abroad_chevening_csc.py --author=prime --republish
"""
CHECKED = "2026-10-01"
CHEV_TIMELINE = "https://www.chevening.org/scholarships/application-timeline/"

# ── Chevening ────────────────────────────────────────────────────────────
CHEV_COVERS = """
<ul><li>University tuition fees</li><li>A monthly living allowance</li><li>A return economy flight to the UK</li><li>The UK visa</li><li>Arrival and departure allowances</li></ul>
<p>Plus the part people forget: a year of Chevening events, and a lifelong network of scholars across more than 160 countries.</p>
<p class="ab-src">Source: chevening.org. Exact allowances are in your award letter.</p>
"""
CHEV_COVERS_UZ = """
<ul><li>Universitet kontrakti</li><li>Oylik yashash puli</li><li>Buyuk Britaniyaga borish-kelish ekonom bileti</li><li>Buyuk Britaniya vizasi</li><li>Kelish va ketish uchun toʻlovlar</li></ul>
<p>Va koʻpchilik unutadigan qism: bir yillik Chevening tadbirlari va 160 dan ortiq davlatdagi stipendiatlarning umrbod tarmogʻi.</p>
<p class="ab-src">Manba: chevening.org. Aniq miqdorlar mukofot xatingizda.</p>
"""
CHEV_BODY = """
<ul class="ab-toc">
<li><a href="#what">What it is</a></li><li><a href="#who">Who can apply</a></li><li><a href="#essays">The four essays</a></li>
<li><a href="#courses">Three courses</a></li><li><a href="#refs">References</a></li><li><a href="#year">Timeline</a></li><li><a href="#mistakes">Mistakes</a></li>
</ul>

<h2 id="what">What it is</h2>
<p>Chevening is the UK government's scholarship for future leaders: a fully funded <strong>one-year master's</strong> at any UK university. It is not a prize for the best grades — it looks for people who already lead, who build networks, and who have a plan for their country.</p>

<h2 id="who">Who can apply</h2>
<ul>
<li>A citizen of an eligible country — Uzbekistan is one.</li>
<li>An undergraduate degree that qualifies you for a UK master's.</li>
<li><strong>At least two years' work experience</strong> after your degree — equivalent to 2,800 hours. Full-time, part-time, volunteering and internships can count.</li>
<li>Applications to <strong>three different eligible UK courses</strong>, and an unconditional offer from at least one by the deadline.</li>
<li>A commitment to <strong>return home for at least two years</strong> after the scholarship.</li>
<li>No upper age limit.</li>
</ul>
<div class="ab-fact"><strong>English</strong><p>Chevening removed its own English requirement in 2020. Your universities still set theirs — so you will usually still need IELTS or another test for the offer.</p></div>
<div class="ab-uz"><strong>Not for school leavers</strong><p>Chevening is for graduates with work experience. For a pupil now in school, it is a plan for five or six years from today: degree, two years of work where you lead something, then Chevening.</p></div>

<h2 id="essays">The four essays</h2>
<p>The application is judged on four areas, each with its own essay and a word limit shown in the form:</p>
<table>
<tr><th>Area</th><th>What they want to see</th></tr>
<tr><td><strong>Leadership and influence</strong></td><td>Times you led a project, a group or a team — ideally at work — and what changed because of you.</td></tr>
<tr><td><strong>Networking</strong></td><td>How you build and use relationships, with examples, and how you will use the Chevening network.</td></tr>
<tr><td><strong>Studying in the UK</strong></td><td>All three courses in detail: how each links your past experience to your future plan.</td></tr>
<tr><td><strong>Career plan</strong></td><td>Where you will be in the short and long term, and how the master's and Chevening get you there — for the good of your country.</td></tr>
</table>
<div class="ab-tip"><strong>Use a story structure</strong><p>For leadership and networking, use Situation → Task → Action → Result: one real situation, what needed doing, what <em>you</em> did, and a result with a number. See the annotated Chevening leadership essay.</p></div>

<h2 id="courses">Three courses</h2>
<p>You list three different UK master's courses, and apply to the universities separately — Chevening does not do it for you. The courses should tell one story: all three must fit your career plan. You need at least one <strong>unconditional</strong> offer by the offer deadline (2027/28: 8 July 2027, 17:00 UK time).</p>

<h2 id="refs">References</h2>
<p>Two referees, named when you submit: professional, academic, or one of each. Not relatives or close friends. Tell them early — they will be asked to upload their letters.</p>

<h2 id="year">Timeline (2027/28 cycle)</h2>
<ol class="ab-steps">
<li><strong>4 August – 6 October 2026</strong> — applications open (closes 11:00 UTC, 16:00 in Tashkent).</li>
<li><strong>October 2026 – January 2027</strong> — eligibility checks and reading committees.</li>
<li><strong>March – April 2027</strong> — interviews at the British Embassy.</li>
<li><strong>By 8 July 2027</strong> — an unconditional university offer.</li>
<li><strong>Mid-June 2027</strong> — results; <strong>September/October 2027</strong> — study begins.</li>
</ol>

<h2 id="mistakes">Mistakes that sink applications</h2>
<ul>
<li><strong>Leadership without a result.</strong> “I was team leader” says nothing; “I led five colleagues to cut processing time from 10 days to 4” does.</li>
<li><strong>Three unrelated courses.</strong> The committee reads it as no plan.</li>
<li><strong>A career plan that ends in the UK.</strong> The return commitment is a condition, not a formality.</li>
<li><strong>Waiting for Chevening before applying to universities.</strong> Apply in parallel — the offer deadline does not move.</li>
</ul>
<p class="ab-src">Sources: chevening.org — application timeline, eligibility, application criteria, references, FAQs (checked 1 October 2026).</p>
"""
CHEV_BODY_UZ = """
<ul class="ab-toc">
<li><a href="#what">Bu nima</a></li><li><a href="#who">Kim topshira oladi</a></li><li><a href="#essays">Toʻrt insho</a></li>
<li><a href="#courses">Uchta kurs</a></li><li><a href="#refs">Tavsiyalar</a></li><li><a href="#year">Jadval</a></li><li><a href="#mistakes">Xatolar</a></li>
</ul>

<h2 id="what">Bu nima</h2>
<p>Chevening — Buyuk Britaniya hukumatining boʻlajak yetakchilar uchun stipendiyasi: istalgan Britaniya universitetida toʻliq moliyalashtiriladigan <strong>bir yillik magistratura</strong>. Bu eng yaxshi baholar uchun mukofot emas — u allaqachon yetakchilik qilayotgan, tarmoq quradigan va davlati uchun rejasi bor odamlarni qidiradi.</p>

<h2 id="who">Kim topshira oladi</h2>
<ul>
<li>Mos davlat fuqarosi — Oʻzbekiston shular qatorida.</li>
<li>Britaniya magistraturasiga kirish huquqini beradigan bakalavr diplomi.</li>
<li>Diplomdan keyin <strong>kamida ikki yillik ish tajribasi</strong> — 2 800 soatga teng. Toʻliq yoki yarim stavka, koʻngillilik va amaliyot hisobga olinishi mumkin.</li>
<li><strong>Uchta turli mos Britaniya kursiga</strong> ariza va muddatgacha kamida bittasidan shartsiz taklif.</li>
<li>Stipendiyadan keyin <strong>kamida ikki yilga vatanga qaytish</strong> majburiyati.</li>
<li>Yuqori yosh chegarasi yoʻq.</li>
</ul>
<div class="ab-fact"><strong>Ingliz tili</strong><p>Chevening oʻzining ingliz tili talabini 2020-yilda bekor qildi. Lekin universitetlar oʻz talabini saqlaydi — shuning uchun taklif olish uchun odatda baribir IELTS yoki boshqa test kerak boʻladi.</p></div>
<div class="ab-uz"><strong>Maktab bitiruvchilari uchun emas</strong><p>Chevening — ish tajribasi bor bitiruvchilar uchun. Hozir maktabda oʻqiyotgan oʻquvchi uchun bu besh-olti yillik reja: diplom, biror narsaga yetakchilik qiladigan ikki yillik ish, keyin Chevening.</p></div>

<h2 id="essays">Toʻrt insho</h2>
<p>Ariza toʻrt yoʻnalish boʻyicha baholanadi, har birining alohida inshosi va shaklda koʻrsatilgan soʻz chegarasi bor:</p>
<table>
<tr><th>Yoʻnalish</th><th>Nimani koʻrmoqchi</th></tr>
<tr><td><strong>Yetakchilik va taʼsir</strong></td><td>Loyiha, guruh yoki jamoaga — iloji boricha ishda — rahbarlik qilgan holatlaringiz va siz tufayli nima oʻzgargani.</td></tr>
<tr><td><strong>Tarmoq qurish</strong></td><td>Munosabatlarni qanday qurib, ulardan qanday foydalanishingiz — misollar bilan, va Chevening tarmogʻidan qanday foydalanasiz.</td></tr>
<tr><td><strong>Britaniyada oʻqish</strong></td><td>Uchala kurs batafsil: har biri oʻtmishdagi tajribangizni kelajak rejangiz bilan qanday bogʻlaydi.</td></tr>
<tr><td><strong>Kasbiy reja</strong></td><td>Qisqa va uzoq muddatda qayerda boʻlasiz, magistratura va Chevening sizni bunga qanday olib boradi — davlatingiz manfaati uchun.</td></tr>
</table>
<div class="ab-tip"><strong>Hikoya tuzilmasidan foydalaning</strong><p>Yetakchilik va tarmoq inshosi uchun: Vaziyat → Vazifa → Harakat → Natija. Bitta haqiqiy vaziyat, nima qilish kerak edi, <em>siz</em> nima qildingiz va raqamli natija. Izohli Chevening yetakchilik inshosiga qarang.</p></div>

<h2 id="courses">Uchta kurs</h2>
<p>Uchta turli Britaniya magistratura kursini koʻrsatasiz va universitetlarga alohida topshirasiz — Chevening buni siz uchun qilmaydi. Kurslar bitta hikoyani aytishi kerak: uchalasi ham kasbiy rejangizga mos boʻlsin. Taklif muddatigacha (2027/28: 2027-yil 8-iyul, Britaniya vaqti bilan 17:00) kamida bitta <strong>shartsiz</strong> taklif kerak.</p>

<h2 id="refs">Tavsiyalar</h2>
<p>Ikki tavsiya beruvchi, ariza yuborishda nomlanadi: ishdan, oʻqishdan yoki biri ishdan, biri oʻqishdan. Qarindosh yoki yaqin doʻst emas. Ularni oldindan ogohlantiring — ulardan xatlarini yuklash soʻraladi.</p>

<h2 id="year">Jadval (2027/28 tsikli)</h2>
<ol class="ab-steps">
<li><strong>2026-yil 4-avgust – 6-oktabr</strong> — arizalar ochiq (11:00 UTC, Toshkent vaqti bilan 16:00 da yopiladi).</li>
<li><strong>2026-yil oktabr – 2027-yil yanvar</strong> — shartlarni tekshirish va oʻqish komissiyalari.</li>
<li><strong>2027-yil mart – aprel</strong> — Britaniya elchixonasida suhbatlar.</li>
<li><strong>2027-yil 8-iyulgacha</strong> — universitetdan shartsiz taklif.</li>
<li><strong>2027-yil iyun oʻrtasi</strong> — natijalar; <strong>2027-yil sentabr/oktabr</strong> — oʻqish boshlanadi.</li>
</ol>

<h2 id="mistakes">Arizani yiqitadigan xatolar</h2>
<ul>
<li><strong>Natijasiz yetakchilik.</strong> «Jamoa rahbari edim» hech narsa demaydi; «Besh hamkasbim bilan hujjat koʻrib chiqish muddatini 10 kundan 4 kunga qisqartirdik» — deydi.</li>
<li><strong>Bir-biriga bogʻliq boʻlmagan uchta kurs.</strong> Komissiya buni rejasizlik deb oʻqiydi.</li>
<li><strong>Britaniyada tugaydigan kasbiy reja.</strong> Qaytish majburiyati — rasmiyatchilik emas, shart.</li>
<li><strong>Universitetlarga Chevening natijasini kutib topshirish.</strong> Parallel topshiring — taklif muddati surilmaydi.</li>
</ul>
<p class="ab-src">Manbalar: chevening.org — jadval, shartlar, baholash mezonlari, tavsiyalar, savol-javoblar (2026-yil 1-oktabrda tekshirilgan).</p>
"""

# ── CSC ──────────────────────────────────────────────────────────────────
CSC_COVERS = """
<p>A full Chinese Government Scholarship normally covers <strong>tuition, accommodation on campus, a monthly stipend and comprehensive medical insurance</strong>. In the 2026/2027 notices, the full scholarship offered through embassies did <strong>not</strong> include international travel. The stipend differs by level and is set by CSC — see the current year's notice.</p>
<p class="ab-src">Source: 2026/2027 Chinese Government Scholarship notices of Chinese embassies.</p>
"""
CSC_COVERS_UZ = """
<p>Toʻliq Xitoy hukumati stipendiyasi odatda <strong>kontrakt, kampusda yotoqxona, oylik stipendiya va toʻliq tibbiy sugʻurtani</strong> qoplaydi. 2026/2027 eʼlonlarida elchixonalar orqali beriladigan toʻliq stipendiya xalqaro aviabiletni <strong>oʻz ichiga olmagan</strong>. Stipendiya miqdori darajaga qarab CSC tomonidan belgilanadi — joriy yil eʼloniga qarang.</p>
<p class="ab-src">Manba: Xitoy elchixonalarining 2026/2027 Xitoy hukumati stipendiyasi eʼlonlari.</p>
"""
CSC_BODY = """
<ul class="ab-toc">
<li><a href="#what">What it is</a></li><li><a href="#routes">Routes</a></li><li><a href="#who">Who can apply</a></li>
<li><a href="#csca">The CSCA test</a></li><li><a href="#docs">Documents</a></li><li><a href="#year">Timeline</a></li>
</ul>

<h2 id="what">What it is</h2>
<p>The Chinese Government Scholarship is run by the China Scholarship Council (CSC). It funds bachelor's, master's and doctoral degrees, and non-degree study, at Chinese universities, in Chinese or in English. Chinese-taught degrees usually begin with a Chinese-language preparatory period.</p>

<h2 id="routes">Routes</h2>
<table>
<tr><th>Route</th><th>How</th></tr>
<tr><td><strong>Bilateral (Type A)</strong></td><td>Through the <strong>Chinese Embassy in Tashkent</strong>. You apply online on campuschina.org with the embassy's agency number, then submit to the embassy.</td></tr>
<tr><td><strong>University (Type B)</strong></td><td>Directly to a Chinese university that has CSC places, by its own deadline.</td></tr>
</table>
<div class="ab-uz"><strong>Ask the Embassy first</strong><p>The agency number, the deadline and any interview are announced by the Chinese Embassy in Uzbekistan. Other embassies' notices had deadlines in early to mid-February 2026 — expect something similar, but plan by Tashkent's own announcement.</p></div>

<h2 id="who">Who can apply (2026/2027 rules)</h2>
<table>
<tr><th>Level</th><th>Requirement</th><th>Age</th></tr>
<tr><td>Bachelor's</td><td>High-school graduate + CSCA score</td><td>under 25</td></tr>
<tr><td>Master's</td><td>Bachelor's degree</td><td>under 35</td></tr>
<tr><td>PhD</td><td>Master's degree</td><td>under 40</td></tr>
</table>
<p><strong>Language:</strong> Chinese-taught programmes ask for HSK — level 3 for general and language study, level 4 for master's and PhD. English-taught programmes ask for IELTS or TOEFL at the university's level.</p>

<h2 id="csca">The new CSCA test (bachelor's)</h2>
<p>In the 2026/2027 cycle, bachelor's applicants had to take the <strong>China Scholastic Competency Assessment (CSCA)</strong> and submit a valid score report. In the 2026/2027 cycle it ran in December 2025 and January 2026 — so the test comes <em>before</em> the application deadline. Register early.</p>

<h2 id="docs">Documents</h2>
<ul>
<li>The CSC online application form, and your passport.</li>
<li>Notarised highest diploma and transcripts (in Chinese or English, or with a notarised translation).</li>
<li>Language certificates (HSK / IELTS / TOEFL); CSCA report for bachelor's.</li>
<li>Study plan (bachelor's/non-degree) or research proposal (master's/PhD).</li>
<li>Recommendation letters from professors (master's/PhD) — the notice says how many.</li>
<li>Pre-admission letter from a Chinese university, if you have one — it strengthens the application.</li>
<li>Foreigner Physical Examination Form (for stays over six months) and a non-criminal record certificate.</li>
</ul>

<h2 id="year">Timeline (pattern from 2026/2027)</h2>
<ol class="ab-steps">
<li><strong>October – November</strong> — embassies announce the call; CSCA test sittings.</li>
<li><strong>By February</strong> — online application and documents to the embassy.</li>
<li><strong>February – March</strong> — interviews (where held).</li>
<li><strong>July – August</strong> — results; study starts in September.</li>
</ol>
<p class="ab-src">Sources: 2026/2027 Chinese Government Scholarship notices of Chinese embassies (programme rules); campuschina.org. Uzbekistan-specific dates: the Chinese Embassy in Tashkent.</p>
"""
CSC_BODY_UZ = """
<ul class="ab-toc">
<li><a href="#what">Bu nima</a></li><li><a href="#routes">Yoʻllar</a></li><li><a href="#who">Kim topshira oladi</a></li>
<li><a href="#csca">CSCA testi</a></li><li><a href="#docs">Hujjatlar</a></li><li><a href="#year">Jadval</a></li>
</ul>

<h2 id="what">Bu nima</h2>
<p>Xitoy hukumati stipendiyasini Xitoy stipendiya kengashi (CSC) boshqaradi. U Xitoy universitetlarida xitoy yoki ingliz tilida bakalavr, magistratura, doktorantura va nodaraja oʻqishni moliyalashtiradi. Xitoy tilidagi dasturlar odatda xitoy tili tayyorlov davridan boshlanadi.</p>

<h2 id="routes">Yoʻllar</h2>
<table>
<tr><th>Yoʻl</th><th>Qanday</th></tr>
<tr><td><strong>Ikki tomonlama (Type A)</strong></td><td><strong>Xitoyning Toshkentdagi elchixonasi</strong> orqali. campuschina.org da elchixona agentlik raqami bilan onlayn topshirasiz, keyin elchixonaga hujjat berasiz.</td></tr>
<tr><td><strong>Universitet (Type B)</strong></td><td>CSC oʻrinlari bor Xitoy universitetiga toʻgʻridan-toʻgʻri, uning oʻz muddatida.</td></tr>
</table>
<div class="ab-uz"><strong>Avval elchixonadan soʻrang</strong><p>Agentlik raqami, muddat va suhbat haqida Xitoyning Oʻzbekistondagi elchixonasi eʼlon qiladi. Boshqa elchixonalar eʼlonlarida muddat 2026-yil fevral boshi–oʻrtasida boʻlgan — shunga oʻxshashini kuting, lekin rejangizni Toshkent eʼloniga qarab tuzing.</p></div>

<h2 id="who">Kim topshira oladi (2026/2027 qoidalari)</h2>
<table>
<tr><th>Daraja</th><th>Talab</th><th>Yosh</th></tr>
<tr><td>Bakalavr</td><td>Maktab bitiruvchisi + CSCA natijasi</td><td>25 yoshdan kichik</td></tr>
<tr><td>Magistratura</td><td>Bakalavr diplomi</td><td>35 yoshdan kichik</td></tr>
<tr><td>PhD</td><td>Magistr diplomi</td><td>40 yoshdan kichik</td></tr>
</table>
<p><strong>Til:</strong> xitoy tilidagi dasturlar HSK soʻraydi — umumiy va til oʻqishi uchun 3-daraja, magistratura va PhD uchun 4-daraja. Ingliz tilidagi dasturlar universitet darajasida IELTS yoki TOEFL soʻraydi.</p>

<h2 id="csca">Yangi CSCA testi (bakalavr)</h2>
<p>2026/2027 tsiklida bakalavr nomzodlari <strong>China Scholastic Competency Assessment (CSCA)</strong> testini topshirib, amaldagi natijani taqdim etishi shart edi. 2026/2027 tsiklida u 2025-yil dekabr va 2026-yil yanvarda oʻtkazilgan — ya'ni test ariza muddatidan <em>oldin</em> boʻladi. Erta roʻyxatdan oʻting.</p>

<h2 id="docs">Hujjatlar</h2>
<ul>
<li>CSC onlayn ariza shakli va pasport.</li>
<li>Notarial tasdiqlangan eng yuqori diplom va baholar varaqasi (xitoy yoki ingliz tilida yoki notarial tarjima bilan).</li>
<li>Til sertifikatlari (HSK / IELTS / TOEFL); bakalavr uchun CSCA natijasi.</li>
<li>Oʻqish rejasi (bakalavr/nodaraja) yoki tadqiqot taklifi (magistratura/PhD).</li>
<li>Professorlardan tavsiyanomalar (magistratura/PhD) — nechtaligi eʼlonda yozilgan.</li>
<li>Bor boʻlsa, Xitoy universitetidan dastlabki qabul xati — arizani kuchaytiradi.</li>
<li>Xorijliklar uchun tibbiy koʻrik shakli (olti oydan uzoq muddat uchun) va sudlanmaganlik haqida maʼlumotnoma.</li>
</ul>

<h2 id="year">Jadval (2026/2027 namunasi)</h2>
<ol class="ab-steps">
<li><strong>Oktabr – noyabr</strong> — elchixonalar eʼlon beradi; CSCA test sanalari.</li>
<li><strong>Fevralgacha</strong> — onlayn ariza va hujjatlar elchixonaga.</li>
<li><strong>Fevral – mart</strong> — suhbatlar (oʻtkazilsa).</li>
<li><strong>Iyul – avgust</strong> — natijalar; oʻqish sentabrda boshlanadi.</li>
</ol>
<p class="ab-src">Manbalar: Xitoy elchixonalarining 2026/2027 Xitoy hukumati stipendiyasi eʼlonlari (dastur qoidalari); campuschina.org. Oʻzbekiston uchun sanalar: Xitoyning Toshkentdagi elchixonasi.</p>
"""

SCHOLARSHIPS = [
    {
        "slug": "chevening", "order": 6, "name": "Chevening", "full_name": "UK Government's Chevening Scholarships",
        "flag": "🇬🇧", "country": "United Kingdom", "country_uz": "Buyuk Britaniya", "depth": "full",
        "levels": "master", "languages": "english", "fully_funded": True,
        "summary": "A fully funded one-year master's at any UK university, for graduates with two years' work experience who lead and plan to return home.",
        "summary_uz": "Istalgan Britaniya universitetida toʻliq moliyalashtiriladigan bir yillik magistratura — yetakchilik qiladigan va vatanga qaytishni rejalashtirgan, ikki yillik ish tajribasi bor bitiruvchilar uchun.",
        "covers": CHEV_COVERS, "covers_uz": CHEV_COVERS_UZ,
        "usual_period": "Opens in August, closes in early October",
        "usual_period_uz": "Avgustda ochilib, oktabr boshida yopiladi",
        "body": CHEV_BODY, "body_uz": CHEV_BODY_UZ,
        "official_url": "https://www.chevening.org/scholarship/uzbekistan/", "last_checked": CHECKED,
    },
    {
        "slug": "csc", "order": 5, "name": "CSC", "full_name": "Chinese Government Scholarship", "flag": "🇨🇳",
        "country": "China", "country_uz": "Xitoy", "depth": "full",
        "levels": "bachelor,master,phd", "languages": "english,any", "fully_funded": True,
        "summary": "China's government scholarship through the Chinese Embassy or a university. Bachelor's applicants now need the CSCA test; Chinese-taught programmes ask for HSK.",
        "summary_uz": "Xitoy hukumati stipendiyasi — Xitoy elchixonasi yoki universitet orqali. Bakalavr nomzodlariga endi CSCA testi kerak; xitoy tilidagi dasturlar HSK soʻraydi.",
        "covers": CSC_COVERS, "covers_uz": CSC_COVERS_UZ,
        "usual_period": "Calls in autumn, deadlines usually by February — Tashkent's embassy sets its own",
        "usual_period_uz": "Eʼlonlar kuzda, muddat odatda fevralgacha — Toshkent elchixonasi oʻzi belgilaydi",
        "body": CSC_BODY, "body_uz": CSC_BODY_UZ,
        "official_url": "https://www.campuschina.org/", "last_checked": CHECKED,
    },
]

DEADLINES = [
    {
        "scholarship": "chevening",
        "label": "Chevening 2027/28", "label_uz": "Chevening 2027/28",
        "opens": "2026-08-04", "closes": "2026-10-06",
        "note": "Closes 6 October 2026 at 11:00 UTC (16:00 Tashkent). Interviews March–April 2027; results mid-June 2027.",
        "note_uz": "2026-yil 6-oktabr, 11:00 UTC (Toshkent vaqti bilan 16:00) da yopiladi. Suhbatlar 2027-yil mart–aprel; natijalar 2027-yil iyun oʻrtasida.",
        "source_url": CHEV_TIMELINE, "last_checked": CHECKED,
    },
    {
        "scholarship": "chevening",
        "label": "Chevening 2027/28 — unconditional university offer", "label_uz": "Chevening 2027/28 — universitetdan shartsiz taklif",
        "opens": None, "closes": "2027-07-08",
        "note": "For applicants in the current cycle: at least one unconditional UK offer by 17:00 UK time.",
        "note_uz": "Joriy tsikl nomzodlari uchun: Britaniya vaqti bilan 17:00 gacha kamida bitta shartsiz taklif.",
        "source_url": CHEV_TIMELINE, "last_checked": CHECKED,
    },
]

# China: leading universities — orientation only; the CSC host list is on
# campuschina.org (unreachable from here on 2026-10-01).
UNIVERSITIES = [
    {'name': 'Tsinghua University', 'name_local': '清华大学', 'city': 'Beijing', 'country': 'China', 'url': 'https://www.tsinghua.edu.cn/en/', 'strengths': 'Leading university, especially strong in engineering.', 'strengths_uz': 'Yetakchi universitet, ayniqsa muhandislikda kuchli.'},
    {'name': 'Peking University', 'name_local': '北京大学', 'city': 'Beijing', 'country': 'China', 'url': 'https://english.pku.edu.cn/', 'strengths': 'Leading comprehensive university.', 'strengths_uz': 'Yetakchi koʻp tarmoqli universitet.'},
    {'name': 'Fudan University', 'name_local': '复旦大学', 'city': 'Shanghai', 'country': 'China', 'url': 'https://www.fudan.edu.cn/en/', 'strengths': 'Leading comprehensive university in Shanghai.', 'strengths_uz': 'Shanxaydagi yetakchi koʻp tarmoqli universitet.'},
    {'name': 'Shanghai Jiao Tong University', 'name_local': '上海交通大学', 'city': 'Shanghai', 'country': 'China', 'url': 'https://en.sjtu.edu.cn/', 'strengths': 'Engineering, medicine and business.', 'strengths_uz': 'Muhandislik, tibbiyot va biznes.'},
    {'name': 'Zhejiang University', 'name_local': '浙江大学', 'city': 'Hangzhou', 'country': 'China', 'url': 'https://www.zju.edu.cn/english/', 'strengths': 'Large comprehensive university.', 'strengths_uz': 'Katta koʻp tarmoqli universitet.'},
    {'name': 'Nanjing University', 'name_local': '南京大学', 'city': 'Nanjing', 'country': 'China', 'url': 'https://www.nju.edu.cn/en/', 'strengths': 'Leading comprehensive university.', 'strengths_uz': 'Yetakchi koʻp tarmoqli universitet.'},
    {'name': 'Wuhan University', 'name_local': '武汉大学', 'city': 'Wuhan', 'country': 'China', 'url': 'https://en.whu.edu.cn/', 'strengths': 'Large comprehensive university in central China.', 'strengths_uz': 'Markaziy Xitoydagi katta koʻp tarmoqli universitet.'},
    {'name': 'Beijing Language and Culture University', 'name_local': '北京语言大学', 'city': 'Beijing', 'country': 'China', 'url': 'https://english.blcu.edu.cn/', 'strengths': 'Specialises in teaching Chinese to international students — a common start for the language year.', 'strengths_uz': 'Xorijlik talabalarga xitoy tilini oʻrgatishga ixtisoslashgan — til yili uchun koʻp tanlanadigan joy.'},
]

CHECKLISTS = {
    "chevening": [
        {"text": "Bachelor's degree finished at least two years before the deadline", "text_uz": "Bakalavr diplomi muddatdan kamida ikki yil oldin olingan"},
        {"text": "2,800 hours (about two years) of work experience after the degree", "text_uz": "Diplomdan keyin 2 800 soat (taxminan ikki yil) ish tajribasi"},
        {"text": "Three different UK master's courses chosen — one story", "text_uz": "Uchta turli Britaniya magistratura kursi tanlandi — bitta hikoya"},
        {"text": "Applied to the three universities (separately from Chevening)", "text_uz": "Uchta universitetga topshirildi (Chevening'dan alohida)"},
        {"text": "IELTS or the test your universities ask for", "text_uz": "Universitetlaringiz soʻraydigan IELTS yoki boshqa test"},
        {"text": "Essay — leadership and influence (STAR, with a number)", "text_uz": "Insho — yetakchilik va taʼsir (STAR, raqam bilan)"},
        {"text": "Essay — networking", "text_uz": "Insho — tarmoq qurish"},
        {"text": "Essay — studying in the UK (all three courses)", "text_uz": "Insho — Britaniyada oʻqish (uchala kurs)"},
        {"text": "Essay — career plan (short and long term, at home)", "text_uz": "Insho — kasbiy reja (qisqa va uzoq muddat, vatanda)"},
        {"text": "Two referees agreed (professional or academic)", "text_uz": "Ikki tavsiya beruvchi rozi (ishdan yoki oʻqishdan)"},
        {"text": "Degree certificate and transcript uploaded", "text_uz": "Diplom va transkript yuklandi"},
        {"text": "Submitted before 11:00 UTC on the deadline day", "text_uz": "Muddat kuni 11:00 UTC dan oldin yuborildi"},
    ],
    "csc": [
        {"text": "Route chosen: Chinese Embassy (Type A) or a university (Type B)", "text_uz": "Yoʻl tanlandi: Xitoy elchixonasi (Type A) yoki universitet (Type B)"},
        {"text": "Embassy's agency number and deadline for this year noted", "text_uz": "Elchixonaning shu yilgi agentlik raqami va muddati yozib olindi"},
        {"text": "CSCA taken and score report ready (bachelor's)", "text_uz": "CSCA topshirildi va natija tayyor (bakalavr)"},
        {"text": "HSK (Chinese-taught) or IELTS/TOEFL (English-taught)", "text_uz": "HSK (xitoy tilida) yoki IELTS/TOEFL (ingliz tilida)"},
        {"text": "Notarised diploma and transcripts (+ notarised translation)", "text_uz": "Notarial diplom va baholar varaqasi (+ notarial tarjima)"},
        {"text": "Study plan or research proposal", "text_uz": "Oʻqish rejasi yoki tadqiqot taklifi"},
        {"text": "Recommendation letters from professors (master's/PhD)", "text_uz": "Professorlardan tavsiyanomalar (magistratura/PhD)"},
        {"text": "Pre-admission letter from a Chinese university (if possible)", "text_uz": "Xitoy universitetidan dastlabki qabul xati (iloji boʻlsa)"},
        {"text": "Foreigner Physical Examination Form", "text_uz": "Xorijliklar uchun tibbiy koʻrik shakli"},
        {"text": "Non-criminal record certificate", "text_uz": "Sudlanmaganlik haqida maʼlumotnoma"},
        {"text": "Online form on campuschina.org submitted, then documents to the embassy", "text_uz": "campuschina.org da onlayn shakl yuborildi, keyin hujjatlar elchixonaga"},
    ],
}

SAMPLES = [{
    "slug": "chevening-leadership-essay", "order": 7, "kind": "statement", "scholarship": "chevening",
    "title": "Chevening leadership essay — Jasur, public health",
    "title_uz": "Chevening yetakchilik inshosi — Jasur, sogʻliqni saqlash",
    "intro": "<p>Jasur is fictional: a pharmacist in a regional health department, three years after graduating. This is his answer on leadership and influence, built as Situation → Task → Action → Result. Keep to the word limit shown in the form.</p>",
    "intro_uz": "<p>Jasur — oʻylab topilgan qahramon: bitirganiga uch yil boʻlgan, viloyat sogʻliqni saqlash boshqarmasidagi farmatsevt. Bu — uning yetakchilik va taʼsir haqidagi javobi, Vaziyat → Vazifa → Harakat → Natija tuzilmasida. Shaklda koʻrsatilgan soʻz chegarasiga amal qiling.</p>",
    "letter": """
<p>In my first year at the regional health department, I noticed that rural clinics ran out of basic medicines every winter, while the central warehouse was full. Nobody owned the problem: clinics blamed the warehouse, the warehouse blamed late orders.</p>
<p>I asked my manager for permission to find the cause. With no authority over the clinics, my task was to persuade twelve clinic heads, and the warehouse team, to change how they ordered.</p>
<p>First, I visited four clinics and learned that orders were written by hand and sent by post once a month, so they arrived after the stock had already run out. I then built a simple shared spreadsheet where clinics recorded stock every week, and I trained one nurse in each clinic to use it. When two clinic heads refused, I did not argue; I showed them a month of their own data, where their shortages were visible in red, and offered to fill the sheet myself for the first month.</p>
<p>Within six months, all twelve clinics were reporting weekly, and winter stock-outs fell from 31 to 6. The department adopted the spreadsheet for the whole region, and I now lead a team of three extending it to vaccines.</p>
<p>I learned that leadership without authority means making the problem visible and making the first step easy. At a UK university I want to learn how to turn tools like mine into health information systems that last beyond one enthusiastic person.</p>
""",
    "notes": [
        {"para": 1, "en": "<strong>Situation</strong> in two sentences — a real problem with a clear cost, and the reason nobody had fixed it.", "uz": "Ikki gapda <strong>vaziyat</strong> — aniq zarari bor haqiqiy muammo va nega uni hech kim hal qilmagani."},
        {"para": 2, "en": "<strong>Task</strong> — and the hard part named honestly: he had no authority. That is what makes it leadership, not management.", "uz": "<strong>Vazifa</strong> — va qiyin tomoni halol aytilgan: uning vakolati yoʻq edi. Aynan shu buni boshqaruv emas, yetakchilik qiladi."},
        {"para": 3, "en": "<strong>Action</strong>, in the first person, step by step — including how he won over people who said no. Committees look for influence, not just effort.", "uz": "<strong>Harakat</strong> — birinchi shaxsda, qadamma-qadam, «yoʻq» deganlarni qanday koʻndirgani bilan. Komissiya faqat mehnatni emas, taʼsirni qidiradi."},
        {"para": 4, "en": "<strong>Result</strong> in numbers (31 → 6), then proof it lasted: the region adopted it and he now leads a team.", "uz": "Raqamlardagi <strong>natija</strong> (31 → 6), keyin uning davom etgani isboti: viloyat qabul qildi va u endi jamoaga rahbarlik qiladi."},
        {"para": 5, "en": "A short lesson, then a bridge to the UK master's — so this essay supports the other three.", "uz": "Qisqa xulosa, keyin Britaniya magistraturasiga koʻprik — shunda bu insho qolgan uchtasini qoʻllab-quvvatlaydi."},
    ],
    "prompts": [
        {"en": "A problem at work or in your community that nobody owned. What did it cost?", "uz": "Ishda yoki jamoangizda hech kim masʼuliyatni olmagan muammo. Uning zarari nima edi?", "lines": 3},
        {"en": "What did YOU have to achieve — and what made it hard (no authority, no budget, resistance)?", "uz": "SIZ nimaga erishishingiz kerak edi — va nima qiyinlashtirdi (vakolat, byudjet yoʻqligi, qarshilik)?", "lines": 3},
        {"en": "Three things you did, in order. How did you win over someone who said no?", "uz": "Qilgan uchta ishingiz, tartib bilan. «Yoʻq» degan odamni qanday koʻndirdingiz?", "lines": 5},
        {"en": "The result as a number — and the sign that it lasted after you.", "uz": "Natija raqamda — va sizdan keyin ham davom etganining belgisi.", "lines": 3},
        {"en": "What you learned about leading, and what the UK course will add to it.", "uz": "Yetakchilik haqida nimani oʻrgandingiz va Britaniya kursi bunga nima qoʻshadi.", "lines": 3},
    ],
}, {
    "slug": "chevening-networking-essay", "order": 8, "kind": "statement", "scholarship": "chevening",
    "title": "Chevening networking essay — Jasur, public health",
    "title_uz": "Chevening tarmoq qurish inshosi — Jasur, sogʻliqni saqlash",
    "intro": "<p>The same fictional applicant, on networking. Chevening wants proof that you build relationships <em>on purpose</em> and use them to get things done — then a concrete plan for the Chevening network.</p>",
    "intro_uz": "<p>Oʻsha oʻylab topilgan nomzod, tarmoq qurish haqida. Chevening siz munosabatlarni <em>ongli ravishda</em> qurishingiz va ular orqali ish bitirishingizni isbotlashni, keyin Chevening tarmogʻi uchun aniq rejani koʻrmoqchi.</p>",
    "letter": """
<p>When our medicine-stock spreadsheet worked in twelve clinics, I knew it would die with me unless other people owned it. So I started building a network around it rather than around myself.</p>
<p>I created a monthly call for the twelve nurses who kept the data, where they, not I, presented problems and fixes. Within three months two nurses were training colleagues in a neighbouring district without my involvement. I also invited the regional IT officer, who had no reason to help, to one call; he saw a problem he could solve and moved the spreadsheet onto the department's server.</p>
<p>Outside work, I joined an online group of young health professionals from Central Asia. After I shared our results there, a pharmacist from Kyrgyzstan adapted the method for her clinics, and we now compare our data every quarter.</p>
<p>I have learned to give first: share the tool, the data or the introduction, and ask for nothing at the start. Relationships built that way last longer than any project.</p>
<p>As a Chevening Scholar I would join the health-sector community of scholars and alumni, and after returning I plan to start a small network of Uzbek Chevening alumni in public health, meeting twice a year with the Ministry's digital team.</p>
""",
    "notes": [
        {"para": 1, "en": "Links to the leadership essay, then states the <strong>reason</strong> for networking: so the work outlives him. Purpose, not popularity.", "uz": "Yetakchilik inshosiga bogʻlanadi, keyin tarmoq qurish <strong>sababini</strong> aytadi: ish undan keyin ham yashashi uchun. Mashhurlik emas, maqsad."},
        {"para": 2, "en": "Two <strong>specific</strong> relationships, and what each produced — including one with someone who had no reason to help.", "uz": "Ikkita <strong>aniq</strong> munosabat va har biri nima bergani — jumladan, yordam berishga sababi yoʻq odam bilan."},
        {"para": 3, "en": "Shows the network reaching beyond his job and his country, with a result (a colleague abroad using the method).", "uz": "Tarmoq ishi va davlatidan tashqariga chiqqanini natija bilan koʻrsatadi (xorijdagi hamkasb usulni qoʻllamoqda)."},
        {"para": 4, "en": "One sentence of reflection — his own rule for networking.", "uz": "Bir gapli xulosa — tarmoq qurish boʻyicha uning oʻz qoidasi."},
        {"para": 5, "en": "A concrete plan for the Chevening network: who, how often, for what. Committees mark down vague “I will network with other scholars”.", "uz": "Chevening tarmogʻi uchun aniq reja: kim, qanchalik tez-tez, nima uchun. Komissiya mavhum «boshqa stipendiatlar bilan tanishaman» uchun ball tushiradi."},
    ],
    "prompts": [
        {"en": "Why do YOU need a network — what work should outlive you?", "uz": "Tarmoq SIZGA nima uchun kerak — qaysi ishingiz sizdan keyin ham yashashi kerak?", "lines": 3},
        {"en": "Two relationships you built on purpose, and what each produced.", "uz": "Ongli ravishda qurgan ikkita munosabatingiz va har biri nima bergani.", "lines": 5},
        {"en": "A connection outside your job or country — and its result.", "uz": "Ishingiz yoki davlatingizdan tashqaridagi aloqa — va uning natijasi.", "lines": 3},
        {"en": "Your own rule for building relationships, in one sentence.", "uz": "Munosabat qurish boʻyicha oʻz qoidangiz, bir gapda.", "lines": 2},
        {"en": "How exactly you will use the Chevening network — who, how often, for what.", "uz": "Chevening tarmogʻidan aynan qanday foydalanasiz — kim, qanchalik tez-tez, nima uchun.", "lines": 3},
    ],
}, {
    "slug": "chevening-career-plan-essay", "order": 9, "kind": "statement", "scholarship": "chevening",
    "title": "Chevening career-plan essay — Jasur, public health",
    "title_uz": "Chevening kasbiy reja inshosi — Jasur, sogʻliqni saqlash",
    "intro": "<p>The fourth essay ties everything together: where you will be soon after returning, where in ten years, and why this master's in the UK is the step between. Keep it consistent with the other three.</p>",
    "intro_uz": "<p>Toʻrtinchi insho hammasini bogʻlaydi: qaytgandan keyin tez orada qayerda boʻlasiz, oʻn yildan keyin qayerda va nega Britaniyadagi aynan shu magistratura ular orasidagi qadam. Qolgan uchtasi bilan mos boʻlsin.</p>",
    "letter": """
<p><strong>Immediately after returning</strong>, I will go back to the regional health department as head of its medicine-supply data unit. My first goal is to extend our stock-reporting system from medicines to vaccines and consumables in all districts of the region within two years.</p>
<p><strong>In the medium term</strong>, I aim to join the Ministry of Health's digital health team and lead the design of a national reporting standard for primary-care supplies, so that every region measures stock the same way and shortages are seen weeks in advance.</p>
<p><strong>In the long term</strong>, within ten years, I want to lead Uzbekistan's national health information programme, making sure that decisions about medicines, staff and budgets are based on data from every clinic, not on paper reports that arrive too late.</p>
<p><strong>Why this master's.</strong> My three chosen courses — in health informatics, health data science and global health policy — each give me something I do not have: how to design information systems that last, how to analyse health data rigorously, and how countries turn data into policy. The UK's own experience of building national health data systems is exactly what I want to learn from.</p>
<p>The Chevening network will connect me with scholars who have done similar work in other countries, and I will bring those contacts home to the Ministry team.</p>
""",
    "notes": [
        {"para": 1, "en": "The short-term goal is <strong>specific and realistic</strong>: a named role, a named task, a time frame.", "uz": "Qisqa muddatli maqsad <strong>aniq va real</strong>: nomlangan lavozim, nomlangan vazifa, muddat."},
        {"para": 2, "en": "The medium-term step grows naturally out of the first — the committee can see the path.", "uz": "Oʻrta muddatli qadam birinchisidan tabiiy oʻsib chiqadi — komissiya yoʻlni koʻra oladi."},
        {"para": 3, "en": "An ambitious long-term goal is welcome — but it must serve the country, and it does.", "uz": "Katta uzoq muddatli maqsad qabul qilinadi — lekin u davlatga xizmat qilishi kerak, bu yerda shunday."},
        {"para": 4, "en": "Each of the <strong>three courses</strong> is justified by a gap in his skills. Do the same with your real course names.", "uz": "<strong>Uchala kurs</strong>ning har biri uning koʻnikmalaridagi boʻshliq bilan asoslangan. Siz ham haqiqiy kurs nomlaringiz bilan shunday qiling."},
        {"para": 5, "en": "Ends by returning home with something to give — the return commitment turned into a strength.", "uz": "Vatanga nimadir olib qaytish bilan tugaydi — qaytish majburiyati kuchli tomonga aylangan."},
    ],
    "prompts": [
        {"en": "The job you will return to (or aim for) — and your first goal there, with a time frame.", "uz": "Qaytib boradigan (yoki intiladigan) ishingiz — va u yerdagi birinchi maqsadingiz, muddati bilan.", "lines": 3},
        {"en": "Your next step, 3–5 years after returning.", "uz": "Qaytgandan keyin 3–5 yildagi keyingi qadamingiz.", "lines": 3},
        {"en": "Where you want to be in ten years — and who in Uzbekistan benefits.", "uz": "Oʻn yildan keyin qayerda boʻlishni xohlaysiz — va Oʻzbekistonda kim foyda koʻradi.", "lines": 3},
        {"en": "For each of your three courses: which gap in your skills does it fill?", "uz": "Uchala kursingizning har biri: koʻnikmalaringizdagi qaysi boʻshliqni toʻldiradi?", "lines": 5},
        {"en": "What you will bring home from the Chevening network.", "uz": "Chevening tarmogʻidan vatanga nima olib qaytasiz.", "lines": 2},
    ],
}]
