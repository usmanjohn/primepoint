"""Study abroad — Türkiye Bursları and Stipendium Hungaricum, in depth.

Sources, read 2026-10-01:
  Türkiye Bursları (turkiyeburslari.gov.tr): /scholarshipsprograms (age and
    grade limits), /whyturkiyescholarships (stipends 6,500 / 9,500 / 13,000 TL,
    accommodation, flight, insurance, 1-year Turkish course), /evaluationand
    selectionprocess (5 stages, 30-question test for undergraduates, in-person
    interview), /applysteps (documents), /calendar (10 Jan – 20 Feb; results
    early August), 2026 announcement.
  Stipendium Hungaricum: Call for Applications 2026/2027 (bachelor's, master's,
    one-tier master's, non-degree) — stipendiumhungaricum.hu: documents, two
    programme choices, Sending Partner nomination, entrance exams (min 56/100),
    timeline (15 January 2026, 2 pm CET), provisions (HUF 43,700; PhD 140,000 /
    180,000; dorm or HUF 40,000; insurance up to HUF 65,000/yr) — the PhD
    amounts from studyinhungary.hu (Tempus Public Foundation, the programme's
    Hungarian coordinator).

    python manage.py import_abroad abroad/management/commands/_abroad_turkiye_hungary.py --author=prime --republish
"""
CHECKED = "2026-10-01"
TB = "https://www.turkiyeburslari.gov.tr"
SH_CALL = "https://stipendiumhungaricum.hu/wp-content/uploads/2025/10/BA_MA_OTM_Call_for_Applications_2026_27.pdf"

# ── Türkiye Bursları ─────────────────────────────────────────────────────
TB_COVERS = """
<table>
<tr><th>Item</th><th>Türkiye Scholarships</th></tr>
<tr><td>Monthly stipend</td><td>6,500 TL (associate and bachelor's) · 9,500 TL (master's) · 13,000 TL (PhD)</td></tr>
<tr><td>Tuition</td><td>Covered</td></tr>
<tr><td>Housing</td><td>Dormitory for undergraduates; for graduates the first year in a dormitory, then a housing allowance (6,000 TL in Istanbul/Ankara, 5,000 TL elsewhere)</td></tr>
<tr><td>Flight</td><td>One-time ticket</td></tr>
<tr><td>Health</td><td>General health insurance</td></tr>
<tr><td>Language</td><td>A one-year Turkish language course</td></tr>
</table>
<p class="ab-src">Source: turkiyeburslari.gov.tr, “What the scholarship covers”, checked 1 October 2026. Amounts in lira change — check before you plan a budget.</p>
"""
TB_COVERS_UZ = """
<table>
<tr><th>Nima</th><th>Türkiye Bursları</th></tr>
<tr><td>Oylik stipendiya</td><td>6 500 lira (kollej va bakalavr) · 9 500 lira (magistratura) · 13 000 lira (PhD)</td></tr>
<tr><td>Kontrakt</td><td>Toʻlanadi</td></tr>
<tr><td>Uy-joy</td><td>Bakalavrlarga yotoqxona; magistr va doktorantlarga birinchi yil yotoqxona, keyin uy-joy puli (Istanbul/Anqarada 6 000 lira, boshqa joyda 5 000 lira)</td></tr>
<tr><td>Aviabilet</td><td>Bir martalik bilet</td></tr>
<tr><td>Sogʻliq</td><td>Umumiy tibbiy sugʻurta</td></tr>
<tr><td>Til</td><td>Bir yillik turk tili kursi</td></tr>
</table>
<p class="ab-src">Manba: turkiyeburslari.gov.tr, «Stipendiya nimalarni qoplaydi», 2026-yil 1-oktabrda tekshirilgan. Liradagi miqdorlar oʻzgaradi — byudjet tuzishdan oldin tekshiring.</p>
"""
TB_BODY = """
<ul class="ab-toc">
<li><a href="#what">What it is</a></li><li><a href="#who">Who can apply</a></li><li><a href="#how">How to apply</a></li>
<li><a href="#select">Selection</a></li><li><a href="#year">Calendar</a></li><li><a href="#tips">Tips</a></li>
</ul>

<h2 id="what">What it is</h2>
<p>Türkiye Scholarships is the Turkish government's programme for international students, at every level from associate degree to PhD, plus research scholarships. You apply once, online and free of charge, and — if you are selected — <strong>you are placed at a university</strong> from the programmes you listed. Most grantees start with a year of Turkish.</p>

<h2 id="who">Who can apply</h2>
<table>
<tr><th>Level</th><th>Age</th><th>Minimum grades</th></tr>
<tr><td>Associate / Bachelor's</td><td>under 21</td><td>70%</td></tr>
<tr><td>Master's</td><td>under 30</td><td>75%</td></tr>
<tr><td>PhD</td><td>under 35</td><td>75%</td></tr>
<tr><td>Medicine, dentistry, pharmacy</td><td>as above</td><td>90%</td></tr>
</table>
<p>Citizens of every country may apply, including those who graduate at the end of the current school year. Not eligible: Turkish citizens (or former citizens), and students already enrolled at a Turkish university at the level they are applying for.</p>
<div class="ab-uz"><strong>“Under 21” is strict</strong>
<p>For a bachelor's, the age limit is the one that rules most pupils out. If you are in 11th grade now, this may be your one real window — check your date of birth against this year's call.</p></div>

<h2 id="how">How to apply</h2>
<ol class="ab-steps">
<li>Create an account on the application portal (tbbs.turkiyeburslari.gov.tr) during the application period.</li>
<li>Fill in the form — including the questions about your academic interests and career goals; the expert committee reads them, so write them like a personal statement.</li>
<li>Upload: passport or ID, a photo from the last year, diploma or temporary graduation certificate, transcript, national exam results if any, and international test results (SAT, GRE, TOEFL…) if a programme requires them. PhD applicants add a research proposal and a writing sample.</li>
<li>Choose your programmes in order of preference.</li>
<li>Submit before the deadline — then watch the portal and your email for the test and interview.</li>
</ol>

<h2 id="select">Selection</h2>
<ol class="ab-steps">
<li><strong>Preliminary assessment</strong> — age, grades, documents.</li>
<li><strong>Expert evaluation</strong> — your academic record, interests and goals.</li>
<li><strong>Test</strong> — undergraduate candidates take a 30-question quantitative test (mathematics, geometry, logic) before the interview.</li>
<li><strong>Interview</strong> — in person, 15–30 minutes, with academics and experts; they check your documents and ask why you are applying and what you know about your field.</li>
<li><strong>Final assessment</strong> — the selection committee draws up the list.</li>
</ol>

<h2 id="year">Calendar</h2>
<table>
<tr><th>When</th><th>What</th></tr>
<tr><td>10 January – 20 February</td><td>Applications (2026 cycle; the same window is announced each year)</td></tr>
<tr><td>March – April</td><td>Evaluation</td></tr>
<tr><td>April – June</td><td>Interviews</td></tr>
<tr><td>Early August</td><td>Results</td></tr>
<tr><td>September</td><td>Arrival in Türkiye</td></tr>
</table>
<p>Research scholarships run in four rounds a year. The separate “Success Scholarship” is only for students already studying in Türkiye.</p>

<h2 id="tips">Tips</h2>
<ul>
<li><strong>Prepare the maths test</strong> the way you would an olympiad warm-up: geometry and logic, timed.</li>
<li><strong>Know your programmes</strong> before the interview — why each one, in that order.</li>
<li><strong>Be honest about Turkish.</strong> Most programmes are in Turkish after the language year; say you are ready to learn it, and start early.</li>
</ul>
<p class="ab-src">Sources: turkiyeburslari.gov.tr — scholarship programmes, coverage, evaluation and selection, application steps, calendar (checked 1 October 2026).</p>
"""
TB_BODY_UZ = """
<ul class="ab-toc">
<li><a href="#what">Bu nima</a></li><li><a href="#who">Kim topshira oladi</a></li><li><a href="#how">Qanday topshiriladi</a></li>
<li><a href="#select">Tanlov</a></li><li><a href="#year">Jadval</a></li><li><a href="#tips">Maslahatlar</a></li>
</ul>

<h2 id="what">Bu nima</h2>
<p>Türkiye Bursları — Turkiya hukumatining xorijlik talabalar uchun dasturi: kollejdan PhD gacha barcha darajalar va tadqiqot stipendiyalari. Bir marta, onlayn va bepul topshirasiz, tanlansangiz — <strong>siz sanab oʻtgan dasturlardan biriga universitetga joylashtirilasiz</strong>. Koʻp stipendiatlar bir yillik turk tilidan boshlaydi.</p>

<h2 id="who">Kim topshira oladi</h2>
<table>
<tr><th>Daraja</th><th>Yosh</th><th>Minimal baho</th></tr>
<tr><td>Kollej / bakalavr</td><td>21 yoshdan kichik</td><td>70%</td></tr>
<tr><td>Magistratura</td><td>30 yoshdan kichik</td><td>75%</td></tr>
<tr><td>PhD</td><td>35 yoshdan kichik</td><td>75%</td></tr>
<tr><td>Tibbiyot, stomatologiya, farmatsiya</td><td>yuqoridagidek</td><td>90%</td></tr>
</table>
<p>Barcha davlatlar fuqarolari, shu jumladan joriy oʻquv yili oxirida bitiradiganlar topshira oladi. Topshira olmaydi: Turkiya fuqarolari (yoki sobiq fuqarolari) va topshirayotgan darajasida Turkiya universitetida allaqachon oʻqiyotganlar.</p>
<div class="ab-uz"><strong>«21 yoshdan kichik» — qatʼiy</strong>
<p>Bakalavr uchun koʻp oʻquvchini aynan yosh chegarasi toʻxtatadi. Hozir 11-sinfda boʻlsangiz, bu sizning yagona haqiqiy imkoniyatingiz boʻlishi mumkin — tugʻilgan sanangizni shu yilgi eʼlon bilan solishtiring.</p></div>

<h2 id="how">Qanday topshiriladi</h2>
<ol class="ab-steps">
<li>Ariza davrida portalda (tbbs.turkiyeburslari.gov.tr) hisob oching.</li>
<li>Shaklni toʻldiring — ilmiy qiziqishlaringiz va kasbiy maqsadlaringiz haqidagi savollar bilan birga; ularni ekspert komissiya oʻqiydi, shuning uchun shaxsiy bayonot kabi yozing.</li>
<li>Yuklang: pasport yoki ID karta, oxirgi bir yilda olingan rasm, diplom yoki vaqtinchalik bitiruv maʼlumotnomasi, baholar varaqasi, bor boʻlsa milliy imtihon natijalari va dastur talab qilsa xalqaro test natijalari (SAT, GRE, TOEFL…). PhD nomzodlari tadqiqot taklifi va yozma ish namunasini qoʻshadi.</li>
<li>Dasturlarni afzallik tartibida tanlang.</li>
<li>Muddatgacha yuboring — keyin test va suhbat uchun portal va emailni kuzatib boring.</li>
</ol>

<h2 id="select">Tanlov</h2>
<ol class="ab-steps">
<li><strong>Dastlabki baholash</strong> — yosh, baholar, hujjatlar.</li>
<li><strong>Ekspert baholashi</strong> — akademik natijalaringiz, qiziqish va maqsadlaringiz.</li>
<li><strong>Test</strong> — bakalavr nomzodlari suhbatdan oldin 30 savollik miqdoriy test topshiradi (matematika, geometriya, mantiq).</li>
<li><strong>Suhbat</strong> — yuzma-yuz, 15–30 daqiqa, olimlar va mutaxassislar bilan; hujjatlaringizni tekshiradi, nega topshirayotganingiz va sohangizni qanchalik bilishingizni soʻraydi.</li>
<li><strong>Yakuniy baholash</strong> — tanlov komissiyasi roʻyxatni tuzadi.</li>
</ol>

<h2 id="year">Jadval</h2>
<table>
<tr><th>Qachon</th><th>Nima</th></tr>
<tr><td>10-yanvar – 20-fevral</td><td>Arizalar (2026 tsikli; har yili shu oraliq eʼlon qilinadi)</td></tr>
<tr><td>Mart – aprel</td><td>Baholash</td></tr>
<tr><td>Aprel – iyun</td><td>Suhbatlar</td></tr>
<tr><td>Avgust boshi</td><td>Natijalar</td></tr>
<tr><td>Sentabr</td><td>Turkiyaga kelish</td></tr>
</table>
<p>Tadqiqot stipendiyalari yiliga toʻrt bosqichda oʻtadi. Alohida «Success Scholarship» faqat Turkiyada allaqachon oʻqiyotganlar uchun.</p>

<h2 id="tips">Maslahatlar</h2>
<ul>
<li><strong>Matematika testiga</strong> olimpiada mashqi kabi tayyorlaning: geometriya va mantiq, vaqt bilan.</li>
<li><strong>Dasturlaringizni biling</strong> — suhbatdan oldin har birini nega va nega aynan shu tartibda tanlaganingizni ayta oling.</li>
<li><strong>Turk tili haqida halol boʻling.</strong> Til yilidan keyin koʻp dasturlar turk tilida; uni oʻrganishga tayyor ekaningizni ayting va erta boshlang.</li>
</ul>
<p class="ab-src">Manbalar: turkiyeburslari.gov.tr — dasturlar, qoplanadigan narsalar, baholash va tanlov, ariza qadamlari, jadval (2026-yil 1-oktabrda tekshirilgan).</p>
"""

# ── Stipendium Hungaricum ────────────────────────────────────────────────
SH_COVERS = """
<table>
<tr><th>Item</th><th>Stipendium Hungaricum</th></tr>
<tr><td>Tuition</td><td>Free — exemption from the tuition fee</td></tr>
<tr><td>Monthly stipend</td><td>HUF 43,700 for bachelor's, master's, one-tier master's and non-degree study, 12 months a year. PhD: HUF 140,000 (first 4 semesters), HUF 180,000 (next 4)</td></tr>
<tr><td>Housing</td><td>A free dormitory place, or HUF 40,000 a month towards rent</td></tr>
<tr><td>Health</td><td>Hungarian state health care, plus supplementary insurance up to HUF 65,000 a year</td></tr>
</table>
<div class="ab-mistake"><strong>The stipend is a contribution, not a salary</strong><p>The call itself says HUF 40,000 does not cover full rent in big cities, especially Budapest. Budget for the difference, or choose a dormitory.</p></div>
<p class="ab-src">Sources: Stipendium Hungaricum Call for Applications 2026/2027; Study in Hungary (Tempus Public Foundation).</p>
"""
SH_COVERS_UZ = """
<table>
<tr><th>Nima</th><th>Stipendium Hungaricum</th></tr>
<tr><td>Kontrakt</td><td>Bepul — oʻqish toʻlovidan ozod</td></tr>
<tr><td>Oylik stipendiya</td><td>Bakalavr, magistratura, yagona magistratura va nodaraja taʼlim uchun oyiga 43 700 forint, yiliga 12 oy. PhD: 140 000 forint (dastlabki 4 semestr), 180 000 forint (keyingi 4)</td></tr>
<tr><td>Uy-joy</td><td>Bepul yotoqxona yoki ijara uchun oyiga 40 000 forint</td></tr>
<tr><td>Sogʻliq</td><td>Vengriya davlat tibbiy xizmati va yiliga 65 000 forintgacha qoʻshimcha sugʻurta</td></tr>
</table>
<div class="ab-mistake"><strong>Stipendiya — ish haqi emas, yordam</strong><p>Eʼlonning oʻzida yozilgan: 40 000 forint katta shaharlarda, ayniqsa Budapeshtda ijarani toʻliq qoplamaydi. Farqni rejalashtiring yoki yotoqxonani tanlang.</p></div>
<p class="ab-src">Manbalar: Stipendium Hungaricum 2026/2027 eʼloni; Study in Hungary (Tempus Public Foundation).</p>
"""
SH_BODY = """
<ul class="ab-toc">
<li><a href="#what">What it is</a></li><li><a href="#two">Two applications</a></li><li><a href="#docs">Documents</a></li>
<li><a href="#rounds">Selection</a></li><li><a href="#year">Calendar</a></li><li><a href="#tips">Tips</a></li>
</ul>

<h2 id="what">What it is</h2>
<p>Hungary's government scholarship, run by the Tempus Public Foundation. Around 900 programmes are taught in English or other foreign languages, at bachelor's, master's, one-tier master's (medicine and similar) and PhD level — plus a one-year Hungarian-language preparatory course if you want to study in Hungarian. Hungary is in the EU and the Schengen area, so the degree is a European one.</p>

<h2 id="two">You apply in two places</h2>
<ol class="ab-steps">
<li><strong>Online, to Tempus Public Foundation</strong> — the application system at apply.stipendiumhungaricum.hu.</li>
<li><strong>To your country's Sending Partner</strong> — for Uzbekistan, the Ministry of Higher Education, Science and Innovation. It pre-selects and <em>nominates</em> applicants; only nominated applicants are considered.</li>
</ol>
<div class="ab-uz"><strong>Read the Ministry's own announcement</strong>
<p>The call says each Sending Partner sets its own procedure and deadlines. In some years the Ministry has announced that the online application alone was enough; in others there may be extra steps. Check its announcement each year — do not rely on last year's rule.</p></div>
<p>You may choose <strong>up to two programmes</strong>, in order of preference. The first choice is examined first, so your chances are higher there — choose it carefully. You cannot change the programmes, language or study mode after the deadline.</p>

<h2 id="docs">Documents (uploaded by the deadline)</h2>
<ul>
<li>The online application form (in English) with a photo taken within the last two years.</li>
<li><strong>Motivation letter</strong> — at least one page, Times New Roman 12-point, in the language of the programme (or Hungarian).</li>
<li>Proof of language proficiency at the level the university sets.</li>
<li>School-leaving certificate (bachelor's) or bachelor's diploma (master's), with translation.</li>
<li>Transcript of records, with translation.</li>
<li>Passport data page (or national ID if you have no passport yet).</li>
<li>Acceptance of the Statement for Application — clicked in the system.</li>
<li>Medical certificate — <em>only</em> if you are awarded the scholarship, presented in Hungary.</li>
</ul>
<p>Files may be at most 4 MB each. Translations are needed only when the original is not in the programme's language (or, for certificates, English).</p>

<h2 id="rounds">Selection</h2>
<ol class="ab-steps">
<li><strong>Technical check and nomination</strong> — by the end of February, the Sending Partner sends its nomination list.</li>
<li><strong>University admission</strong> — mid-March to end of May: universities contact nominated applicants for an entrance exam or interview. <strong>A score below 56 out of 100 means no scholarship.</strong></li>
<li><strong>Allocation</strong> — May–June, by Tempus Public Foundation.</li>
<li><strong>Results</strong> — end of June / mid-July; then the visa and arrival in August–September.</li>
</ol>

<h2 id="year">Calendar (2026/2027 call)</h2>
<table>
<tr><th>When</th><th>What</th></tr>
<tr><td>November – December</td><td>Read the call, prepare documents, contact the Sending Partner</td></tr>
<tr><td>15 January, 2 pm CET</td><td>Deadline: online application (and the Sending Partner's own procedure)</td></tr>
<tr><td>End of February</td><td>Nomination lists</td></tr>
<tr><td>Mid-March – end of May</td><td>University entrance exams and interviews</td></tr>
<tr><td>End of June – mid-July</td><td>Results</td></tr>
<tr><td>July – August</td><td>Visa, then arrival</td></tr>
</table>

<h2 id="tips">Tips</h2>
<ul>
<li><strong>Pick the first choice for fit, not fame.</strong> It is examined first — a programme where you meet the entrance requirements comfortably is worth more than a famous one where you are borderline.</li>
<li><strong>Prepare for the university's exam.</strong> Each programme publishes its own entrance requirements — read them in the programme list before you choose.</li>
<li><strong>Write the motivation letter for that programme,</strong> in its language, at least one page, in the required font.</li>
</ul>
<p class="ab-src">Sources: Stipendium Hungaricum Call for Applications 2026/2027 (bachelor's, master's, one-tier master's, non-degree); Study in Hungary (Tempus Public Foundation); checked 1 October 2026.</p>
"""
SH_BODY_UZ = """
<ul class="ab-toc">
<li><a href="#what">Bu nima</a></li><li><a href="#two">Ikki ariza</a></li><li><a href="#docs">Hujjatlar</a></li>
<li><a href="#rounds">Tanlov</a></li><li><a href="#year">Jadval</a></li><li><a href="#tips">Maslahatlar</a></li>
</ul>

<h2 id="what">Bu nima</h2>
<p>Vengriya hukumati stipendiyasi, uni Tempus Public Foundation boshqaradi. Taxminan 900 ta dastur ingliz yoki boshqa xorijiy tillarda oʻqitiladi: bakalavr, magistratura, yagona magistratura (tibbiyot va shunga oʻxshash) va PhD darajalarida — hamda vengr tilida oʻqimoqchi boʻlsangiz, bir yillik vengr tili tayyorlov kursi. Vengriya Yevropa Ittifoqi va Shengen hududida, shuning uchun diplom — Yevropa diplomi.</p>

<h2 id="two">Ikki joyga topshirasiz</h2>
<ol class="ab-steps">
<li><strong>Onlayn, Tempus Public Foundation'ga</strong> — apply.stipendiumhungaricum.hu tizimida.</li>
<li><strong>Davlatingizning «Sending Partner»iga</strong> — Oʻzbekiston uchun Oliy taʼlim, fan va innovatsiyalar vazirligi. U nomzodlarni saralab, <em>tavsiya qiladi</em>; faqat tavsiya qilinganlar koʻrib chiqiladi.</li>
</ol>
<div class="ab-uz"><strong>Vazirlikning oʻz eʼlonini oʻqing</strong>
<p>Eʼlonda yozilishicha, har bir «Sending Partner» oʻz tartibi va muddatlarini belgilaydi. Baʼzi yillarda vazirlik faqat onlayn ariza yetarli ekanini eʼlon qilgan; boshqa yillarda qoʻshimcha qadamlar boʻlishi mumkin. Har yili uning eʼlonini tekshiring — oʻtgan yilgi qoidaga tayanmang.</p></div>
<p>Afzallik tartibida <strong>2 tagacha dastur</strong> tanlashingiz mumkin. Birinchi tanlov birinchi koʻriladi, shuning uchun unda imkoniyatingiz yuqoriroq — uni puxta tanlang. Muddatdan keyin dasturlar, til yoki oʻqish shaklini oʻzgartirib boʻlmaydi.</p>

<h2 id="docs">Hujjatlar (muddatgacha yuklanadi)</h2>
<ul>
<li>Onlayn ariza shakli (ingliz tilida) va oxirgi ikki yil ichida olingan rasm.</li>
<li><strong>Motivatsion xat</strong> — kamida bir sahifa, Times New Roman 12 shrift, dastur tilida (yoki vengr tilida).</li>
<li>Universitet belgilagan darajadagi til sertifikati.</li>
<li>Attestat (bakalavr uchun) yoki bakalavr diplomi (magistratura uchun), tarjimasi bilan.</li>
<li>Baholar varaqasi, tarjimasi bilan.</li>
<li>Pasportning maʼlumotlar sahifasi (pasport boʻlmasa, ID karta).</li>
<li>Ariza bayonotini qabul qilish — tizimda bosiladi.</li>
<li>Tibbiy maʼlumotnoma — <em>faqat</em> stipendiya berilsa, Vengriyada koʻrsatiladi.</li>
</ul>
<p>Har bir fayl 4 MB dan oshmasin. Tarjima faqat asl hujjat dastur tilida (yoki guvohnomalar uchun — ingliz tilida) boʻlmaganda kerak.</p>

<h2 id="rounds">Tanlov</h2>
<ol class="ab-steps">
<li><strong>Texnik tekshiruv va tavsiya</strong> — fevral oxirigacha «Sending Partner» tavsiya roʻyxatini yuboradi.</li>
<li><strong>Universitet qabuli</strong> — mart oʻrtasidan may oxirigacha: universitetlar tavsiya qilinganlar bilan kirish imtihoni yoki suhbat uchun bogʻlanadi. <strong>100 dan 56 balldan past natija — stipendiya yoʻq.</strong></li>
<li><strong>Taqsimot</strong> — may–iyun, Tempus Public Foundation tomonidan.</li>
<li><strong>Natijalar</strong> — iyun oxiri / iyul oʻrtasi; keyin viza va avgust–sentabrda kelish.</li>
</ol>

<h2 id="year">Jadval (2026/2027 eʼloni)</h2>
<table>
<tr><th>Qachon</th><th>Nima</th></tr>
<tr><td>Noyabr – dekabr</td><td>Eʼlonni oʻqish, hujjatlarni tayyorlash, «Sending Partner» bilan bogʻlanish</td></tr>
<tr><td>15-yanvar, 14:00 CET</td><td>Muddat: onlayn ariza (va «Sending Partner»ning oʻz tartibi)</td></tr>
<tr><td>Fevral oxiri</td><td>Tavsiya roʻyxatlari</td></tr>
<tr><td>Mart oʻrtasi – may oxiri</td><td>Universitet kirish imtihonlari va suhbatlar</td></tr>
<tr><td>Iyun oxiri – iyul oʻrtasi</td><td>Natijalar</td></tr>
<tr><td>Iyul – avgust</td><td>Viza, keyin kelish</td></tr>
</table>

<h2 id="tips">Maslahatlar</h2>
<ul>
<li><strong>Birinchi tanlovni mashhurlik uchun emas, moslik uchun tanlang.</strong> U birinchi koʻriladi — talablariga bemalol javob beradigan dastur, zoʻrgʻa yetadigan mashhur dasturdan qimmatroq.</li>
<li><strong>Universitet imtihoniga tayyorlaning.</strong> Har bir dastur oʻz kirish talablarini eʼlon qiladi — tanlashdan oldin ularni dasturlar roʻyxatidan oʻqing.</li>
<li><strong>Motivatsion xatni aynan shu dastur uchun,</strong> uning tilida, kamida bir sahifa, talab qilingan shriftda yozing.</li>
</ul>
<p class="ab-src">Manbalar: Stipendium Hungaricum 2026/2027 eʼloni (bakalavr, magistratura, yagona magistratura, nodaraja); Study in Hungary (Tempus Public Foundation); 2026-yil 1-oktabrda tekshirilgan.</p>
"""

SCHOLARSHIPS = [
    {
        "slug": "turkiye", "order": 3, "name": "Türkiye Bursları", "full_name": "Türkiye Scholarships",
        "flag": "🇹🇷", "country": "Türkiye", "country_uz": "Turkiya", "depth": "full",
        "levels": "bachelor,master,phd", "languages": "english,any", "fully_funded": True,
        "summary": "Türkiye's government scholarship for every level: one free online application, a year of Turkish, and university placement done for you. Applications 10 January – 20 February.",
        "summary_uz": "Turkiya hukumatining barcha darajalar uchun stipendiyasi: bitta bepul onlayn ariza, bir yil turk tili va universitetga joylashtirishni ular oʻzi qiladi. Arizalar 10-yanvar – 20-fevral.",
        "covers": TB_COVERS, "covers_uz": TB_COVERS_UZ,
        "usual_period": "10 January – 20 February each year",
        "usual_period_uz": "Har yili 10-yanvar – 20-fevral",
        "body": TB_BODY, "body_uz": TB_BODY_UZ,
        "official_url": "https://www.turkiyeburslari.gov.tr/", "last_checked": CHECKED,
    },
    {
        "slug": "hungary", "order": 4, "name": "Stipendium Hungaricum", "full_name": "Hungarian Government Scholarship",
        "flag": "🇭🇺", "country": "Hungary", "country_uz": "Vengriya", "depth": "full",
        "levels": "bachelor,master,phd", "languages": "english", "fully_funded": True,
        "summary": "A European degree in Hungary, mostly taught in English, tuition-free with a stipend and housing. Two applications: online and through Uzbekistan's Ministry. Deadline mid-January.",
        "summary_uz": "Vengriyada Yevropa diplomi, asosan ingliz tilida, bepul, stipendiya va yotoqxona bilan. Ikki ariza: onlayn va Oʻzbekiston vazirligi orqali. Muddat yanvar oʻrtasida.",
        "covers": SH_COVERS, "covers_uz": SH_COVERS_UZ,
        "usual_period": "Opens in November, closes mid-January (2026/27: 15 January, 2 pm CET)",
        "usual_period_uz": "Noyabrda ochiladi, yanvar oʻrtasida yopiladi (2026/27: 15-yanvar, 14:00 CET)",
        "body": SH_BODY, "body_uz": SH_BODY_UZ,
        "official_url": "https://stipendiumhungaricum.hu/", "last_checked": CHECKED,
    },
]

DEADLINES = [
    {
        "scholarship": "turkiye",
        "label": "Türkiye Bursları 2027", "label_uz": "Türkiye Bursları 2027",
        "opens": None, "closes": "2027-02-20", "is_estimate": True,
        "note": "The official calendar gives 10 January – 20 February each year; confirm when the 2027 call is announced.",
        "note_uz": "Rasmiy jadvalda har yili 10-yanvar – 20-fevral; 2027 eʼloni chiqqanda tasdiqlang.",
        "source_url": f"{TB}/calendar", "last_checked": CHECKED,
    },
    {
        "scholarship": "hungary",
        "label": "Stipendium Hungaricum 2027/28", "label_uz": "Stipendium Hungaricum 2027/28",
        "opens": None, "closes": "2027-01-15", "is_estimate": True,
        "note": "Estimate from the 2026/27 call (15 January 2026, 2 pm CET). The Ministry's own procedure may have an earlier date.",
        "note_uz": "2026/27 eʼloni asosida taxmin (2026-yil 15-yanvar, 14:00 CET). Vazirlikning oʻz tartibida muddat oldinroq boʻlishi mumkin.",
        "source_url": SH_CALL, "last_checked": CHECKED,
    },
]

# Türkiye: leading state universities — orientation only; Türkiye Scholarships
# places the scholar. Hungary: Stipendium Hungaricum host institutions as listed
# at apply.stipendiumhungaricum.hu/institutions (read 2026-10-01).
UNIVERSITIES = [
    {'name': 'Middle East Technical University (METU)', 'name_local': 'Orta Doğu Teknik Üniversitesi', 'city': 'Ankara', 'country': 'Türkiye', 'url': 'https://www.metu.edu.tr/', 'strengths': 'State university in Ankara; teaching is in English.', 'strengths_uz': 'Anqaradagi davlat universiteti; oʻqitish ingliz tilida.'},
    {'name': 'Boğaziçi University', 'name_local': 'Boğaziçi Üniversitesi', 'city': 'Istanbul', 'country': 'Türkiye', 'url': 'https://bogazici.edu.tr/en', 'strengths': 'State university in Istanbul; teaching is in English.', 'strengths_uz': 'Istanbuldagi davlat universiteti; oʻqitish ingliz tilida.'},
    {'name': 'Istanbul Technical University', 'name_local': 'İstanbul Teknik Üniversitesi', 'city': 'Istanbul', 'country': 'Türkiye', 'url': 'https://www.itu.edu.tr/en', 'strengths': 'State technical university: engineering and architecture.', 'strengths_uz': 'Davlat texnika universiteti: muhandislik va arxitektura.'},
    {'name': 'Hacettepe University', 'name_local': 'Hacettepe Üniversitesi', 'city': 'Ankara', 'country': 'Türkiye', 'url': 'https://www.hacettepe.edu.tr/english', 'strengths': 'State university known for medicine and health sciences.', 'strengths_uz': 'Tibbiyot va sogʻliqni saqlash fanlari bilan tanilgan davlat universiteti.'},
    {'name': 'Ankara University', 'name_local': 'Ankara Üniversitesi', 'city': 'Ankara', 'country': 'Türkiye', 'url': 'https://www.ankara.edu.tr/en/', 'strengths': 'Large state university in the capital, with many faculties.', 'strengths_uz': 'Poytaxtdagi, koʻp fakultetli katta davlat universiteti.'},
    {'name': 'Istanbul University', 'name_local': 'İstanbul Üniversitesi', 'city': 'Istanbul', 'country': 'Türkiye', 'url': 'https://istanbul.edu.tr/en', 'strengths': 'Large historic state university in Istanbul.', 'strengths_uz': 'Istanbuldagi katta va tarixiy davlat universiteti.'},
    {'name': 'Ege University', 'name_local': 'Ege Üniversitesi', 'city': 'İzmir', 'country': 'Türkiye', 'url': 'https://ege.edu.tr/en', 'strengths': 'Large state university in İzmir, on the Aegean coast.', 'strengths_uz': 'Egey sohilidagi Izmirda joylashgan katta davlat universiteti.'},
    {'name': 'Marmara University', 'name_local': 'Marmara Üniversitesi', 'city': 'Istanbul', 'country': 'Türkiye', 'url': 'https://www.marmara.edu.tr/en', 'strengths': 'Large state university in Istanbul.', 'strengths_uz': 'Istanbuldagi katta davlat universiteti.'},
    {'name': 'Eötvös Loránd University (ELTE)', 'name_local': 'Eötvös Loránd Tudományegyetem', 'city': 'Budapest', 'country': 'Hungary', 'url': 'https://www.elte.hu/en', 'strengths': "Stipendium Hungaricum host. One of Hungary's largest universities: sciences, humanities, IT.", 'strengths_uz': 'Stipendium Hungaricum qabul qiluvchisi. Vengriyaning eng katta universitetlaridan: tabiiy, gumanitar fanlar, IT.'},
    {'name': 'Budapest University of Technology and Economics (BME)', 'name_local': 'Budapesti Műszaki és Gazdaságtudományi Egyetem', 'city': 'Budapest', 'country': 'Hungary', 'url': 'https://www.bme.hu/en', 'strengths': "Stipendium Hungaricum host. Hungary's leading technical university.", 'strengths_uz': 'Stipendium Hungaricum qabul qiluvchisi. Vengriyaning yetakchi texnika universiteti.'},
    {'name': 'Semmelweis University', 'name_local': 'Semmelweis Egyetem', 'city': 'Budapest', 'country': 'Hungary', 'url': 'https://semmelweis.hu/english/', 'strengths': 'Stipendium Hungaricum host. Medicine, dentistry and pharmacy.', 'strengths_uz': 'Stipendium Hungaricum qabul qiluvchisi. Tibbiyot, stomatologiya va farmatsiya.'},
    {'name': 'Corvinus University of Budapest', 'name_local': 'Budapesti Corvinus Egyetem', 'city': 'Budapest', 'country': 'Hungary', 'url': 'https://www.uni-corvinus.hu/?lang=en', 'strengths': 'Stipendium Hungaricum host. Economics, business and social sciences.', 'strengths_uz': 'Stipendium Hungaricum qabul qiluvchisi. Iqtisodiyot, biznes va ijtimoiy fanlar.'},
    {'name': 'University of Debrecen', 'name_local': 'Debreceni Egyetem', 'city': 'Debrecen', 'country': 'Hungary', 'url': 'https://unideb.hu/en', 'strengths': 'Stipendium Hungaricum host. Large university in eastern Hungary with many international students.', 'strengths_uz': 'Stipendium Hungaricum qabul qiluvchisi. Sharqiy Vengriyadagi, xorijlik talabalari koʻp katta universitet.'},
    {'name': 'University of Szeged', 'name_local': 'Szegedi Tudományegyetem', 'city': 'Szeged', 'country': 'Hungary', 'url': 'https://u-szeged.hu/english', 'strengths': 'Stipendium Hungaricum host. Large university in southern Hungary.', 'strengths_uz': 'Stipendium Hungaricum qabul qiluvchisi. Janubiy Vengriyadagi katta universitet.'},
    {'name': 'University of Pécs', 'name_local': 'Pécsi Tudományegyetem', 'city': 'Pécs', 'country': 'Hungary', 'url': 'https://international.pte.hu/', 'strengths': 'Stipendium Hungaricum host. Large university in south-western Hungary.', 'strengths_uz': 'Stipendium Hungaricum qabul qiluvchisi. Janubi-gʻarbiy Vengriyadagi katta universitet.'},
    {'name': 'Hungarian University of Agriculture and Life Sciences (MATE)', 'name_local': 'Magyar Agrár- és Élettudományi Egyetem', 'city': 'Gödöllő', 'country': 'Hungary', 'url': 'https://uni-mate.hu/', 'strengths': 'Stipendium Hungaricum host. Agriculture, food science and environmental studies.', 'strengths_uz': 'Stipendium Hungaricum qabul qiluvchisi. Qishloq xoʻjaligi, oziq-ovqat va atrof-muhit fanlari.'},
    {'name': 'Óbuda University', 'name_local': 'Óbudai Egyetem', 'city': 'Budapest', 'country': 'Hungary', 'url': 'https://uni-obuda.hu/en/', 'strengths': 'Stipendium Hungaricum host. Engineering and IT.', 'strengths_uz': 'Stipendium Hungaricum qabul qiluvchisi. Muhandislik va IT.'},
]

CHECKLISTS = {
    "turkiye": [
        {"text": "Age under the limit on the day of application (bachelor's: under 21)", "text_uz": "Ariza kuni yosh chegarasidan kichik (bakalavr: 21 yoshdan kichik)"},
        {"text": "Grades at least 70% (bachelor's), 75% (graduate), 90% (medicine, dentistry, pharmacy)", "text_uz": "Baholar kamida 70% (bakalavr), 75% (magistr/PhD), 90% (tibbiyot, stomatologiya, farmatsiya)"},
        {"text": "Account on the application portal", "text_uz": "Ariza portalida hisob"},
        {"text": "Passport or ID card, and a photo from the last year", "text_uz": "Pasport yoki ID karta va oxirgi bir yilda olingan rasm"},
        {"text": "Diploma or temporary graduation certificate", "text_uz": "Diplom yoki vaqtinchalik bitiruv maʼlumotnomasi"},
        {"text": "Transcript", "text_uz": "Baholar varaqasi"},
        {"text": "Test results a programme requires (SAT, GRE, TOEFL…)", "text_uz": "Dastur talab qiladigan test natijalari (SAT, GRE, TOEFL…)"},
        {"text": "Answers on interests and goals written like a personal statement", "text_uz": "Qiziqish va maqsadlar haqidagi javoblar shaxsiy bayonot kabi yozildi"},
        {"text": "Programmes chosen in order of preference", "text_uz": "Dasturlar afzallik tartibida tanlandi"},
        {"text": "Practised for the 30-question maths/logic test (bachelor's)", "text_uz": "30 savollik matematika/mantiq testiga tayyorlandim (bakalavr)"},
    ],
    "hungary": [
        {"text": "Up to two programmes chosen — the first one carefully", "text_uz": "2 tagacha dastur tanlandi — birinchisi puxta oʻylab"},
        {"text": "Entrance requirements of both programmes read", "text_uz": "Ikkala dasturning kirish talablari oʻqildi"},
        {"text": "Motivation letter: 1+ page, Times New Roman 12, in the programme's language", "text_uz": "Motivatsion xat: 1+ sahifa, Times New Roman 12, dastur tilida"},
        {"text": "Language certificate at the level the university sets", "text_uz": "Universitet belgilagan darajadagi til sertifikati"},
        {"text": "School certificate or diploma + translation", "text_uz": "Attestat yoki diplom + tarjima"},
        {"text": "Transcript + translation", "text_uz": "Baholar varaqasi + tarjima"},
        {"text": "Passport data page and a photo from the last two years", "text_uz": "Pasportning maʼlumotlar sahifasi va oxirgi ikki yildagi rasm"},
        {"text": "Online application submitted on apply.stipendiumhungaricum.hu", "text_uz": "apply.stipendiumhungaricum.hu da onlayn ariza yuborildi"},
        {"text": "The Ministry's own procedure for this year followed", "text_uz": "Vazirlikning shu yilgi tartibiga amal qilindi"},
        {"text": "Ready for the university's entrance exam or interview (March–May)", "text_uz": "Universitetning kirish imtihoni yoki suhbatiga tayyor (mart–may)"},
    ],
}

SAMPLES = [{
    "slug": "hungary-motivation-letter", "order": 10, "kind": "statement", "scholarship": "hungary",
    "title": "Stipendium Hungaricum motivation letter — Aziza, civil engineering (bachelor's)",
    "title_uz": "Stipendium Hungaricum motivatsion xati — Aziza, qurilish muhandisligi (bakalavr)",
    "intro": "<p>Aziza is fictional: a school-leaver from Namangan applying for an English-taught bachelor's in civil engineering. The call asks for at least one page, Times New Roman 12, in the programme's language — and the letter is read by the <em>university</em>, so it must be about that programme.</p>",
    "intro_uz": "<p>Aziza — oʻylab topilgan qahramon: Namangandagi bitiruvchi, ingliz tilida oʻqitiladigan qurilish muhandisligi bakalavriatiga topshiryapti. Eʼlon kamida bir sahifa, Times New Roman 12, dastur tilida soʻraydi — xatni esa <em>universitet</em> oʻqiydi, shuning uchun u aynan shu dastur haqida boʻlishi kerak.</p>",
    "letter": """
<p>Dear Admissions Committee,</p>
<p>I am applying for the Bachelor of Science in Civil Engineering as my first choice under the Stipendium Hungaricum programme. In 2023 an old footbridge over the canal in my neighbourhood in Namangan was closed because it had become unsafe, and for a year children walked two kilometres around it to reach school. When the new bridge was built, I spent weekends watching the engineers work and asking them questions. That was when I decided that I want to design structures that people can trust.</p>
<p>At school I have concentrated on the subjects this programme builds on. My average grade in mathematics and physics over the last three years is 5 out of 5, and in 2025 I took third place in the regional physics olympiad. To test my interest in practice, I built a model truss bridge from wooden sticks for our school science fair; it held 18 kilograms, and the failures of my first two models taught me more than the success of the third.</p>
<p>I chose this programme because its first two years focus on mechanics, materials and structural analysis, which are exactly the foundations I want, and because it is taught in English, the language in which I have studied for my IELTS certificate. I also value studying in the European Union, where building standards are among the strictest in the world.</p>
<p>After graduating, I plan to return to Uzbekistan, where cities such as Namangan are growing fast and many schools, bridges and homes are being built. I want to work on public infrastructure and, in the future, help introduce the safety standards I will learn in Hungary.</p>
<p>Thank you for considering my application.</p>
<p>Sincerely,<br>Aziza Rahimova</p>
""",
    "notes": [
        {"para": 2, "en": "Names the programme and that it is the <strong>first choice</strong> — the first choice is examined first, so say so. Then a real moment, not “since childhood”.", "uz": "Dasturni va uning <strong>birinchi tanlov</strong> ekanini aytadi — birinchi tanlov birinchi koʻriladi. Keyin «bolaligimdan» emas, haqiqiy lahza."},
        {"para": 3, "en": "Evidence with numbers, and a lesson from failure (two broken models) — the kind of detail an engineering committee remembers.", "uz": "Raqamli dalil va muvaffaqiyatsizlikdan saboq (ikki singan model) — muhandislik komissiyasi eslab qoladigan tafsilot."},
        {"para": 4, "en": "“Why this programme” answered with the programme's own content and its language. Replace the modules with the real ones from your programme's page.", "uz": "«Nega aynan shu dastur» — dasturning oʻz mazmuni va tili bilan javob. Modullarni oʻz dasturingiz sahifasidagi haqiqiylari bilan almashtiring."},
        {"para": 5, "en": "A realistic plan at home. The programme's mission is to build ties with the sending countries — show you are one.", "uz": "Vatandagi real reja. Dasturning maqsadi — yuboruvchi davlatlar bilan aloqalar qurish; siz shunday koʻprik ekaningizni koʻrsating."},
    ],
    "prompts": [
        {"en": "The programme and why it is your FIRST choice.", "uz": "Dastur va nega u sizning BIRINCHI tanlovingiz.", "lines": 2},
        {"en": "A real moment that led you to this field.", "uz": "Sizni shu sohaga olib kelgan haqiqiy lahza.", "lines": 3},
        {"en": "Your evidence: grades in the key subjects, olympiads, a project — with numbers.", "uz": "Dalillaringiz: asosiy fanlardan baholar, olimpiadalar, loyiha — raqamlar bilan.", "lines": 4},
        {"en": "Three things in THIS programme (modules, language, place) that fit you.", "uz": "AYNAN shu dasturdagi sizga mos uchta narsa (modullar, til, joy).", "lines": 3},
        {"en": "What you will do in Uzbekistan after graduating.", "uz": "Bitirgandan keyin Oʻzbekistonda nima qilasiz.", "lines": 3},
    ],
}, {
    "slug": "turkiye-statement", "order": 12, "kind": "statement", "scholarship": "turkiye",
    "title": "Türkiye Bursları answers on interests and goals — Kamola, medicine (bachelor's)",
    "title_uz": "Türkiye Bursları: qiziqishlar va maqsadlar haqidagi javoblar — Kamola, tibbiyot (bakalavr)",
    "intro": "<p>The Türkiye Scholarships form asks about your academic interests and career goals, and the expert committee reads the answers before the interview. Kamola is fictional: a school-leaver from Khorezm applying for medicine — a field where the minimum grade is 90%. Check this year's form for the exact questions and character limits.</p>",
    "intro_uz": "<p>Türkiye Bursları shakli ilmiy qiziqishlaringiz va kasbiy maqsadlaringiz haqida soʻraydi; ekspert komissiya javoblarni suhbatdan oldin oʻqiydi. Kamola — oʻylab topilgan qahramon: Xorazmlik bitiruvchi, tibbiyotga topshiryapti — bu sohada minimal baho 90%. Aniq savollar va belgi chegarasini shu yilgi shakldan tekshiring.</p>",
    "letter": """
<h4>Why this field</h4>
<p>My grandmother lives in a village two hours from the nearest hospital. When she had a stroke in 2024, the first hours were lost on the road. Since then I have wanted to become a doctor who works where doctors are fewest, and to understand how emergency care can reach such villages faster.</p>
<h4>What I have done</h4>
<p>My grades in biology and chemistry have been 5 out of 5 for three years, and I placed second in the regional biology olympiad in 2025. For six months I volunteered on Saturdays at our district clinic, helping nurses record patients, which showed me how much of medicine is organisation and communication.</p>
<h4>Why Türkiye</h4>
<p>Türkiye has built a strong network of city and regional hospitals, and its medical faculties train doctors for very different regions. I also want to study in a country that is culturally close to Uzbekistan, and I am ready to learn Turkish in the preparatory year, since medicine must be learned in the language of the patients.</p>
<h4>Career goal</h4>
<p>After graduating, I will return to Khorezm to work in emergency medicine at the regional hospital, and in the long term help set up first-aid training for village health workers, so that the first hour is no longer lost.</p>
""",
    "notes": [
        {"para": 1, "en": "A personal reason told in two sentences, then turned into a <strong>direction</strong> (rural emergency care) — not just “I want to help people”.", "uz": "Ikki gapda shaxsiy sabab, keyin <strong>yoʻnalish</strong>ga aylantirilgan (qishloqdagi tez yordam) — shunchaki «odamlarga yordam bermoqchiman» emas."},
        {"para": 2, "en": "Evidence for a 90% field: top grades in the subjects that matter, an olympiad, and real contact with medicine.", "uz": "90% talab qilinadigan soha uchun dalil: kerakli fanlardan eng yuqori baholar, olimpiada va tibbiyot bilan haqiqiy aloqa."},
        {"para": 3, "en": "“Why Türkiye” with a real reason about its system, and an honest, positive answer about learning Turkish — the interviewers will ask.", "uz": "«Nega Turkiya» — uning tizimi haqidagi haqiqiy sabab bilan, va turk tilini oʻrganish haqida halol, ijobiy javob — suhbatda albatta soʻraladi."},
        {"para": 4, "en": "The goal closes the circle opened in the first answer. Committees notice when the story holds together.", "uz": "Maqsad birinchi javobda ochilgan doirani yopadi. Komissiya hikoya yaxlit ekanini sezadi."},
    ],
    "prompts": [
        {"en": "The moment that pointed you to your field — and the direction it gave you.", "uz": "Sizni sohangizga yoʻnaltirgan lahza — va u bergan yoʻnalish.", "lines": 3},
        {"en": "Your evidence: grades in the key subjects, olympiads, volunteering — with numbers.", "uz": "Dalillaringiz: asosiy fanlardan baholar, olimpiadalar, koʻngillilik — raqamlar bilan.", "lines": 4},
        {"en": "One real reason to study this field in Türkiye.", "uz": "Bu sohani aynan Turkiyada oʻqish uchun bitta haqiqiy sabab.", "lines": 2},
        {"en": "Your honest answer: are you ready to study in Turkish after the language year?", "uz": "Halol javobingiz: til yilidan keyin turk tilida oʻqishga tayyormisiz?", "lines": 2},
        {"en": "Where you will work after graduating — and what will change there.", "uz": "Bitirgandan keyin qayerda ishlaysiz — va u yerda nima oʻzgaradi.", "lines": 3},
    ],
}]
