"""Study abroad — El-Yurt Umidi, DAAD and Fulbright, in depth.

Sources, read 2026-10-01:
  El-Yurt Umidi: the foundation's announcements of its open scholarship
    competitions — 2nd competition 2025 (announced 14 Nov 2025, documents on
    el-yurt.uz until 26 Nov 2025, 277 places) and 1st competition 2026
    (announced 6 Apr 2026, until 24 Apr 2026, 500 places); both give ages up
    to 30 / 22–40 / 25–45, IELTS 6.0 / 7.0, work experience >1 yr (master's) /
    >2 yrs (PhD), an admission letter from a foreign university, and coverage
    (tuition, visa, insurance, one round trip a year, housing, materials).
    Presidential Decree PF-77 (5 May 2025): scholarships without a competition
    for grant-admitted students of the world's top-100 universities; transport
    and housing for grant-admitted students at top-300 universities; priority
    fields. NOT stated: the length of the work obligation — sources disagree,
    so the page sends the pupil to the contract in the call.
  DAAD (daad.de, via its own pages): monthly €992 (students) / €1,300
    (doctoral), travel allowance, insurance; EPOS — bachelor's + at least 2
    years' professional experience, degree normally ≤ 6 years old, course
    list with deadlines per course.
  Fulbright (U.S. Embassy in Uzbekistan): citizens residing in Uzbekistan,
    bachelor's degree, ≥ 2 years' professional experience; master's up to two
    years; priority fields; online application apply.iie.org/ffsp2027 with an
    embassy voucher; 2027–28 instructions published March 2026.

    python manage.py import_abroad abroad/management/commands/_abroad_eyuf_daad_fulbright.py --author=prime --republish
"""
CHECKED = "2026-10-01"

# ── El-Yurt Umidi ────────────────────────────────────────────────────────
EYUF_COVERS = """
<ul><li>Tuition at the foreign university</li><li>Housing</li><li>Medical insurance</li><li>Visa costs</li><li>Travel — one round trip a year</li><li>Study materials and other listed costs</li></ul>
<p class="ab-src">Source: the foundation's 2025–2026 competition announcements.</p>
"""
EYUF_COVERS_UZ = """
<ul><li>Xorijiy universitetdagi kontrakt</li><li>Turar joy</li><li>Tibbiy sugʻurta</li><li>Viza xarajatlari</li><li>Yoʻl — yiliga bir marta borib-kelish</li><li>Oʻquv materiallari va boshqa belgilangan xarajatlar</li></ul>
<p class="ab-src">Manba: jamgʻarmaning 2025–2026 tanlov eʼlonlari.</p>
"""
EYUF_BODY = """
<ul class="ab-toc">
<li><a href="#what">What it is</a></li><li><a href="#who">Who can apply</a></li><li><a href="#order">The order matters</a></li>
<li><a href="#top">Top-100 / Top-300</a></li><li><a href="#duty">The obligation</a></li><li><a href="#year">Calendar</a></li>
</ul>

<h2 id="what">What it is</h2>
<p>El-Yurt Umidi is Uzbekistan's own foundation, under the President, that pays for Uzbek citizens to study at leading universities abroad — bachelor's, master's and doctoral. Unlike the foreign scholarships on this site, it <strong>does not choose your university</strong>: you win a place at a university abroad yourself, and the foundation funds it.</p>

<h2 id="who">Who can apply (2025–2026 competitions)</h2>
<table>
<tr><th>Level</th><th>Age</th><th>Language</th><th>Work experience</th></tr>
<tr><td>Bachelor's</td><td>up to 30</td><td>IELTS 6.0 or equivalent</td><td>—</td></tr>
<tr><td>Master's</td><td>22–40</td><td>IELTS 7.0 or equivalent</td><td>more than 1 year</td></tr>
<tr><td>Doctoral</td><td>25–45</td><td>IELTS 7.0 or equivalent</td><td>more than 2 years</td></tr>
</table>
<p>Documents: an application to the foundation, the <strong>admission letter from the foreign university</strong>, your school certificate or diploma, the language certificate, a copy of your work record (for master's and PhD) and a motivation essay. Everything is submitted on the foundation's platform, el-yurt.uz, where you also enter the university's country, ranking and tuition.</p>

<h2 id="order">The order matters</h2>
<ol class="ab-steps">
<li><strong>Certificate first</strong> — IELTS 6.0 (bachelor's) or 7.0 (master's/PhD).</li>
<li><strong>Admission second</strong> — apply to leading universities abroad yourself and win an offer.</li>
<li><strong>Then the competition</strong> — with the offer in hand, apply to the foundation in its next round.</li>
</ol>
<div class="ab-uz"><strong>The mistake almost everyone makes</strong><p>Pupils wait for the El-Yurt Umidi competition before applying to universities — and arrive without an admission letter. University deadlines come first: see the other guides on this site for how to win the offer.</p></div>

<h2 id="top">The Top-100 and Top-300 rules (Decree PF-77, May 2025)</h2>
<ul>
<li>If you are admitted <strong>on a grant</strong> to one of the world's <strong>top-100</strong> universities, the scholarship is granted <strong>without a competition</strong>.</li>
<li>If you are admitted on a grant to a <strong>top-300</strong> university, international travel and housing costs are covered.</li>
<li>Priority fields named in the decree include energy, urban planning, transport, architecture, geodesy, engineering and public administration.</li>
</ul>
<p>Rankings here mean the global QS or THE tables — check the university's current position before you rely on this.</p>

<h2 id="duty">The obligation afterwards</h2>
<p>A scholar signs a contract that requires working in Uzbekistan — usually in the public sector — for a set number of years after graduating, and repaying the costs if the obligation is not met. The number of years depends on the level and the contract of your year: <strong>read it in the competition documents before you sign</strong>. Treat it as a job offer, not a formality.</p>

<h2 id="year">Calendar</h2>
<p>The foundation runs <strong>two open competitions a year</strong>, each with a short submission window:</p>
<table>
<tr><th>Round</th><th>Last window</th></tr>
<tr><td>Spring</td><td>6 April – 24 April 2026 (500 places)</td></tr>
<tr><td>Autumn</td><td>14 November – 26 November 2025 (277 places)</td></tr>
</table>
<p>Windows are two to three weeks long — have every document ready before the announcement.</p>
<p class="ab-src">Sources: El-Yurt Umidi foundation competition announcements (Nov 2025, Apr 2026); Presidential Decree PF-77 of 5 May 2025.</p>
"""
EYUF_BODY_UZ = """
<ul class="ab-toc">
<li><a href="#what">Bu nima</a></li><li><a href="#who">Kim topshira oladi</a></li><li><a href="#order">Tartib muhim</a></li>
<li><a href="#top">Top-100 / Top-300</a></li><li><a href="#duty">Majburiyat</a></li><li><a href="#year">Jadval</a></li>
</ul>

<h2 id="what">Bu nima</h2>
<p>«El-yurt umidi» — Oʻzbekistonning oʻz jamgʻarmasi, Prezident huzurida; u Oʻzbekiston fuqarolarining xorijdagi yetakchi universitetlarda bakalavriat, magistratura va doktoranturada oʻqishini moliyalashtiradi. Bu saytdagi xorijiy stipendiyalardan farqli oʻlaroq, u <strong>universitetingizni tanlamaydi</strong>: xorijiy universitetga oʻzingiz kirasiz, jamgʻarma esa uni moliyalashtiradi.</p>

<h2 id="who">Kim topshira oladi (2025–2026 tanlovlari)</h2>
<table>
<tr><th>Daraja</th><th>Yosh</th><th>Til</th><th>Ish staji</th></tr>
<tr><td>Bakalavriat</td><td>30 yoshgacha</td><td>IELTS 6.0 yoki unga teng</td><td>—</td></tr>
<tr><td>Magistratura</td><td>22–40</td><td>IELTS 7.0 yoki unga teng</td><td>1 yildan ortiq</td></tr>
<tr><td>Doktorantura</td><td>25–45</td><td>IELTS 7.0 yoki unga teng</td><td>2 yildan ortiq</td></tr>
</table>
<p>Hujjatlar: jamgʻarmaga ariza, <strong>xorijiy universitetning qabul xati</strong>, attestat yoki diplom, til sertifikati, mehnat daftarchasi nusxasi (magistratura va PhD uchun) va motivatsion insho. Hammasi jamgʻarmaning el-yurt.uz platformasida topshiriladi; u yerda universitetning davlati, reytingi va kontrakt narxini ham kiritasiz.</p>

<h2 id="order">Tartib muhim</h2>
<ol class="ab-steps">
<li><strong>Avval sertifikat</strong> — IELTS 6.0 (bakalavr) yoki 7.0 (magistr/PhD).</li>
<li><strong>Keyin qabul</strong> — xorijdagi yetakchi universitetlarga oʻzingiz topshirib, taklif oling.</li>
<li><strong>Shundan keyin tanlov</strong> — taklif qoʻlingizda boʻlsa, jamgʻarmaning navbatdagi bosqichiga topshiring.</li>
</ol>
<div class="ab-uz"><strong>Deyarli hamma qiladigan xato</strong><p>Oʻquvchilar universitetlarga topshirish oʻrniga «El-yurt umidi» tanlovini kutadi — va qabul xatisiz qoladi. Universitet muddatlari birinchi keladi: taklifni qanday olishni shu saytdagi boshqa qoʻllanmalardan oʻqing.</p></div>

<h2 id="top">Top-100 va Top-300 qoidalari (PF-77 Farmoni, 2025-yil may)</h2>
<ul>
<li>Dunyodagi <strong>eng yaxshi 100 ta</strong> universitetdan biriga <strong>grant asosida</strong> qabul qilinsangiz, stipendiya <strong>tanlovsiz</strong> ajratiladi.</li>
<li><strong>Eng yaxshi 300 ta</strong> universitetga grant asosida kirsangiz, xalqaro yoʻl va turar joy xarajatlari qoplanadi.</li>
<li>Farmonda ustuvor sohalar: energetika, shaharsozlik, transport, arxitektura, geodeziya, muhandislik va davlat boshqaruvi.</li>
</ul>
<p>Bu yerda reyting — QS yoki THE global jadvallari. Bunga tayanishdan oldin universitetning joriy oʻrnini tekshiring.</p>

<h2 id="duty">Keyingi majburiyat</h2>
<p>Stipendiat bitirgandan keyin Oʻzbekistonda — odatda davlat sektorida — belgilangan yil ishlashni va majburiyat bajarilmasa xarajatlarni qaytarishni nazarda tutadigan shartnoma imzolaydi. Yillar soni darajaga va oʻsha yilgi shartnomaga bogʻliq: <strong>imzolashdan oldin uni tanlov hujjatlarida oʻqing</strong>. Buni rasmiyatchilik emas, ish taklifi deb qabul qiling.</p>

<h2 id="year">Jadval</h2>
<p>Jamgʻarma <strong>yiliga ikkita ochiq tanlov</strong> oʻtkazadi, har birida hujjat topshirish muddati qisqa:</p>
<table>
<tr><th>Bosqich</th><th>Oxirgi muddat oynasi</th></tr>
<tr><td>Bahor</td><td>2026-yil 6–24-aprel (500 oʻrin)</td></tr>
<tr><td>Kuz</td><td>2025-yil 14–26-noyabr (277 oʻrin)</td></tr>
</table>
<p>Oyna ikki-uch hafta davom etadi — eʼlon chiqishidan oldin barcha hujjatlaringiz tayyor boʻlsin.</p>
<p class="ab-src">Manbalar: «El-yurt umidi» jamgʻarmasi tanlov eʼlonlari (2025-yil noyabr, 2026-yil aprel); Prezidentning 2025-yil 5-maydagi PF-77 Farmoni.</p>
"""

# ── DAAD ─────────────────────────────────────────────────────────────────
DAAD_COVERS = """
<ul><li>Monthly payment — currently €992 for master's students, €1,300 for doctoral students</li><li>A travel allowance</li><li>Health, accident and liability insurance in most programmes</li><li>Depending on the programme: a German course, a research allowance, family benefits</li></ul>
<div class="ab-uz"><strong>Tuition in Germany</strong><p>Most public universities charge no tuition — only a semester contribution. The known exception is Baden-Württemberg, which charges students from outside the EU. That is why a DAAD award is mostly about living costs.</p></div>
<p class="ab-src">Source: daad.de, “DAAD Scholarships — an overview”.</p>
"""
DAAD_COVERS_UZ = """
<ul><li>Oylik toʻlov — hozir magistrlar uchun 992 yevro, doktorantlar uchun 1 300 yevro</li><li>Yoʻl puli</li><li>Koʻp dasturlarda tibbiy, baxtsiz hodisa va javobgarlik sugʻurtasi</li><li>Dasturga qarab: nemis tili kursi, tadqiqot puli, oila uchun toʻlovlar</li></ul>
<div class="ab-uz"><strong>Germaniyada kontrakt</strong><p>Koʻp davlat universitetlari kontrakt olmaydi — faqat semestr badali. Maʼlum istisno — Baden-Vyurtemberg, u Yevropa Ittifoqidan tashqaridagi talabalardan toʻlov oladi. Shuning uchun DAAD granti asosan yashash xarajatlari uchun.</p></div>
<p class="ab-src">Manba: daad.de, «DAAD stipendiyalari — umumiy maʼlumot».</p>
"""
DAAD_BODY = """
<ul class="ab-toc">
<li><a href="#what">What it is</a></li><li><a href="#epos">EPOS</a></li><li><a href="#find">Finding your programme</a></li>
<li><a href="#docs">Documents</a></li><li><a href="#germany">Germany-specific</a></li>
</ul>

<h2 id="what">What it is</h2>
<p>DAAD — the German Academic Exchange Service — is not one scholarship but <strong>a catalogue of programmes</strong>, mostly for graduates (master's) and doctoral candidates. Bachelor's degrees are generally not what DAAD funds for students from abroad. Each programme has its own rules and deadline, so the first job is to find the right one.</p>

<h2 id="epos">EPOS — the programme to know</h2>
<p><strong>EPOS (Development-Related Postgraduate Courses)</strong> funds master's (and in exceptional cases doctoral) degrees at German universities for professionals from developing and newly industrialised countries — the programme most relevant to applicants from Uzbekistan.</p>
<ul>
<li>A bachelor's degree (usually four years) in a relevant subject.</li>
<li><strong>At least two years' professional experience.</strong></li>
<li>Your degree should normally be <strong>no more than six years old</strong>.</li>
<li>A motivation that is clearly development-related: what you will change at home.</li>
<li>You apply to a <strong>course on the EPOS list</strong>, by that course's own deadline. Many deadlines fall in the autumn, a year before study starts.</li>
</ul>

<h2 id="find">Finding your programme</h2>
<ol class="ab-steps">
<li>Open the <strong>DAAD scholarship database</strong>, choose Uzbekistan as your country and your level.</li>
<li>Read each programme's “who can apply” and deadline; write down two or three.</li>
<li>For EPOS, download the current course list with deadlines and pick the courses that fit your work.</li>
<li>Read the university's own admission requirements too — the scholarship and the admission are separate decisions.</li>
</ol>

<h2 id="docs">Typical documents</h2>
<ul>
<li>DAAD application form and a CV (often in the Europass format).</li>
<li>A motivation letter tied to your work and your plan at home.</li>
<li>Recommendation letters — often including one from your employer (EPOS).</li>
<li>Degree certificates and transcripts, with certified translations.</li>
<li>Language certificate — English (IELTS/TOEFL) or German, as the course requires.</li>
</ul>

<h2 id="germany">Germany-specific</h2>
<div class="ab-mistake"><strong>No apostille for Germany</strong><p>Germany does not accept apostilles from Uzbekistan (its 2012 objection still stands). Documents need consular legalisation — plan the extra weeks.</p></div>
<p>Many German universities handle international applications through <strong>uni-assist</strong>; the programme page says whether yours does. Learning some German, even with an English-taught course, makes the years there much easier.</p>
<p class="ab-src">Sources: daad.de — DAAD Scholarships overview; EPOS programme and course list; HCCH Apostille status table (checked 1 October 2026).</p>
"""
DAAD_BODY_UZ = """
<ul class="ab-toc">
<li><a href="#what">Bu nima</a></li><li><a href="#epos">EPOS</a></li><li><a href="#find">Dasturni topish</a></li>
<li><a href="#docs">Hujjatlar</a></li><li><a href="#germany">Germaniyaga xos</a></li>
</ul>

<h2 id="what">Bu nima</h2>
<p>DAAD — Germaniya akademik almashinuv xizmati — bitta stipendiya emas, <strong>dasturlar katalogi</strong>; asosan bitiruvchilar (magistratura) va doktorantlar uchun. Xorijlik talabalar uchun bakalavriat odatda DAAD moliyalashtiradigan narsa emas. Har bir dasturning oʻz qoidalari va muddati bor, shuning uchun birinchi vazifa — mosini topish.</p>

<h2 id="epos">EPOS — bilish kerak boʻlgan dastur</h2>
<p><strong>EPOS (rivojlanish bilan bogʻliq magistratura kurslari)</strong> rivojlanayotgan va yangi sanoatlashgan davlatlardan kelgan mutaxassislarning Germaniya universitetlarida magistratura (istisno holatlarda doktorantura) oʻqishini moliyalashtiradi — Oʻzbekistondan topshiruvchilar uchun eng mos dastur.</p>
<ul>
<li>Tegishli fan boʻyicha bakalavr diplomi (odatda toʻrt yillik).</li>
<li><strong>Kamida ikki yillik ish tajribasi.</strong></li>
<li>Diplomingiz odatda <strong>olti yildan eski boʻlmasligi</strong> kerak.</li>
<li>Rivojlanish bilan aniq bogʻliq maqsad: vataningizda nimani oʻzgartirasiz.</li>
<li>Siz <strong>EPOS roʻyxatidagi kursga</strong>, oʻsha kursning oʻz muddatida topshirasiz. Koʻp muddatlar oʻqish boshlanishidan bir yil oldingi kuzga toʻgʻri keladi.</li>
</ul>

<h2 id="find">Dasturni topish</h2>
<ol class="ab-steps">
<li><strong>DAAD stipendiyalar bazasi</strong>ni oching, davlatingiz sifatida Oʻzbekistonni va darajangizni tanlang.</li>
<li>Har bir dasturning «kim topshira oladi» qismi va muddatini oʻqing; ikki-uchtasini yozib oling.</li>
<li>EPOS uchun muddatlar koʻrsatilgan joriy kurslar roʻyxatini yuklab oling va ishingizga mos kurslarni tanlang.</li>
<li>Universitetning oʻz qabul talablarini ham oʻqing — stipendiya va qabul alohida qarorlar.</li>
</ol>

<h2 id="docs">Odatdagi hujjatlar</h2>
<ul>
<li>DAAD ariza shakli va CV (koʻpincha Europass formatida).</li>
<li>Ishingiz va vatandagi rejangizga bogʻlangan motivatsion xat.</li>
<li>Tavsiyanomalar — koʻpincha ish beruvchidan ham (EPOS).</li>
<li>Diplom va baholar varaqasi, tasdiqlangan tarjimalar bilan.</li>
<li>Til sertifikati — kurs talabiga koʻra ingliz (IELTS/TOEFL) yoki nemis tili.</li>
</ul>

<h2 id="germany">Germaniyaga xos</h2>
<div class="ab-mistake"><strong>Germaniya uchun apostil yoʻq</strong><p>Germaniya Oʻzbekiston apostilini qabul qilmaydi (2012-yilgi eʼtirozi hanuz kuchda). Hujjatlarga konsullik legalizatsiyasi kerak — qoʻshimcha haftalarni rejalashtiring.</p></div>
<p>Koʻp Germaniya universitetlari xorijlik arizalarni <strong>uni-assist</strong> orqali qabul qiladi; dastur sahifasida sizniki shundaymi, yozilgan. Ingliz tilidagi kursda ham biroz nemis tilini bilish u yerdagi yillarni ancha osonlashtiradi.</p>
<p class="ab-src">Manbalar: daad.de — DAAD stipendiyalari umumiy maʼlumoti; EPOS dasturi va kurslar roʻyxati; HCCH Apostil holat jadvali (2026-yil 1-oktabrda tekshirilgan).</p>
"""

# ── Fulbright ────────────────────────────────────────────────────────────
FUL_COVERS = """
<ul><li>Tuition and fees</li><li>A monthly stipend</li><li>Health insurance</li><li>Books and supplies</li><li>Round-trip airfare to the United States</li><li>J-1 visa support</li></ul>
<p class="ab-src">Source: U.S. Embassy in Uzbekistan, Fulbright Foreign Student Program.</p>
"""
FUL_COVERS_UZ = """
<ul><li>Kontrakt va toʻlovlar</li><li>Oylik stipendiya</li><li>Tibbiy sugʻurta</li><li>Kitob va oʻquv anjomlari</li><li>AQShga borish-kelish aviabileti</li><li>J-1 vizasi boʻyicha yordam</li></ul>
<p class="ab-src">Manba: AQShning Oʻzbekistondagi elchixonasi, Fulbright Foreign Student Program.</p>
"""
FUL_BODY = """
<ul class="ab-toc">
<li><a href="#what">What it is</a></li><li><a href="#who">Who can apply</a></li><li><a href="#fields">Priority fields</a></li>
<li><a href="#how">How to apply</a></li><li><a href="#tips">Tips</a></li>
</ul>

<h2 id="what">What it is</h2>
<p>The Fulbright Foreign Student Program brings graduates and young professionals to the United States for a <strong>master's degree of up to two years</strong>. In Uzbekistan it is run by the U.S. Embassy in Tashkent, and the embassy decides who goes forward.</p>

<h2 id="who">Who can apply</h2>
<ul>
<li>A citizen of Uzbekistan, <strong>living in Uzbekistan</strong> throughout the application and selection.</li>
<li>A completed bachelor's degree.</li>
<li><strong>At least two years of professional experience.</strong></li>
</ul>
<p>English-test and other requirements are in the embassy's instructions for the current round — read them before you start.</p>

<h2 id="fields">Priority fields (2027–28 round)</h2>
<p>All fields are open, but the embassy gives priority to: <strong>artificial intelligence, data science, digital skills, STEM fields supporting the AI and critical-minerals economy, nuclear engineering and civil nuclear policy, and space/aerospace engineering</strong>.</p>

<h2 id="how">How to apply</h2>
<ol class="ab-steps">
<li>The embassy announces the round and publishes the instructions (for 2027–28, in March 2026).</li>
<li>The online application at <strong>apply.iie.org</strong> opens with a <strong>voucher</strong> distributed by the embassy — follow the embassy's announcement to get it.</li>
<li>Essays, references, transcripts and test scores go into the online application.</li>
<li>Shortlisted candidates are interviewed; grantees travel to the U.S. the following year.</li>
</ol>

<h2 id="tips">Tips</h2>
<ul>
<li><strong>Watch the embassy from late winter.</strong> The round is announced once a year; missing it costs a year.</li>
<li><strong>Connect your field to the priorities</strong> where it is honest to do so — and to a clear plan for Uzbekistan.</li>
<li><strong>Your work experience is the story.</strong> Fulbright looks for professionals: what you did, what changed, what you will do next.</li>
</ul>
<p class="ab-src">Sources: U.S. Embassy in Uzbekistan — Fulbright Foreign Student Program page and 2027–28 instructions (checked 1 October 2026).</p>
"""
FUL_BODY_UZ = """
<ul class="ab-toc">
<li><a href="#what">Bu nima</a></li><li><a href="#who">Kim topshira oladi</a></li><li><a href="#fields">Ustuvor sohalar</a></li>
<li><a href="#how">Qanday topshiriladi</a></li><li><a href="#tips">Maslahatlar</a></li>
</ul>

<h2 id="what">Bu nima</h2>
<p>Fulbright Foreign Student Program bitiruvchilar va yosh mutaxassislarni AQShga <strong>ikki yilgacha boʻlgan magistratura</strong> uchun olib boradi. Oʻzbekistonda uni Toshkentdagi AQSh elchixonasi oʻtkazadi va kim keyingi bosqichga oʻtishini elchixona hal qiladi.</p>

<h2 id="who">Kim topshira oladi</h2>
<ul>
<li>Ariza va tanlov davomida <strong>Oʻzbekistonda yashaydigan</strong> Oʻzbekiston fuqarosi.</li>
<li>Tugatilgan bakalavriat.</li>
<li><strong>Kamida ikki yillik ish tajribasi.</strong></li>
</ul>
<p>Ingliz tili testi va boshqa talablar joriy bosqich uchun elchixona yoʻriqnomasida — boshlashdan oldin oʻqing.</p>

<h2 id="fields">Ustuvor sohalar (2027–28 bosqichi)</h2>
<p>Barcha sohalar ochiq, lekin elchixona quyidagilarga ustuvorlik beradi: <strong>sunʼiy intellekt, maʼlumotlar ilmi, raqamli koʻnikmalar, sunʼiy intellekt va muhim minerallar iqtisodiyotini qoʻllab-quvvatlovchi STEM sohalari, yadro muhandisligi va tinch yadro siyosati, kosmik/aerokosmik muhandislik</strong>.</p>

<h2 id="how">Qanday topshiriladi</h2>
<ol class="ab-steps">
<li>Elchixona bosqichni eʼlon qiladi va yoʻriqnomani chiqaradi (2027–28 uchun — 2026-yil martda).</li>
<li><strong>apply.iie.org</strong> dagi onlayn ariza elchixona tarqatadigan <strong>vaucher</strong> bilan ochiladi — uni olish uchun elchixona eʼloniga amal qiling.</li>
<li>Insholar, tavsiyalar, baholar varaqasi va test natijalari onlayn arizaga kiritiladi.</li>
<li>Saralanganlar suhbatdan oʻtadi; stipendiatlar keyingi yili AQShga boradi.</li>
</ol>

<h2 id="tips">Maslahatlar</h2>
<ul>
<li><strong>Qish oxiridan elchixonani kuzating.</strong> Bosqich yiliga bir marta eʼlon qilinadi; uni oʻtkazib yuborish bir yilga tushadi.</li>
<li><strong>Sohangizni ustuvorliklar bilan bogʻlang</strong> — halol boʻlsa — va Oʻzbekiston uchun aniq reja bilan.</li>
<li><strong>Ish tajribangiz — sizning hikoyangiz.</strong> Fulbright mutaxassislarni qidiradi: nima qildingiz, nima oʻzgardi, keyin nima qilasiz.</li>
</ul>
<p class="ab-src">Manbalar: AQShning Oʻzbekistondagi elchixonasi — Fulbright Foreign Student Program sahifasi va 2027–28 yoʻriqnomasi (2026-yil 1-oktabrda tekshirilgan).</p>
"""

SCHOLARSHIPS = [
    {
        "slug": "eyuf", "order": 10, "name": "El-Yurt Umidi", "full_name": "“El-Yurt Umidi” Foundation (Uzbekistan)",
        "flag": "🇺🇿", "country": "Uzbekistan → abroad", "country_uz": "Oʻzbekiston → xorij", "depth": "full",
        "levels": "bachelor,master,phd", "languages": "english,any", "fully_funded": True,
        "summary": "Uzbekistan's own foundation: win a place at a leading university abroad, then it pays. Two competitions a year; IELTS 6.0 for bachelor's, 7.0 for master's.",
        "summary_uz": "Oʻzbekistonning oʻz jamgʻarmasi: xorijdagi yetakchi universitetga kiring — keyin u toʻlaydi. Yiliga ikki tanlov; bakalavr uchun IELTS 6.0, magistratura uchun 7.0.",
        "covers": EYUF_COVERS, "covers_uz": EYUF_COVERS_UZ,
        "usual_period": "Two competitions a year — spring (April) and autumn (November), 2–3 weeks each",
        "usual_period_uz": "Yiliga ikki tanlov — bahorda (aprel) va kuzda (noyabr), har biri 2–3 hafta",
        "body": EYUF_BODY, "body_uz": EYUF_BODY_UZ,
        "official_url": "https://eyuf.uz/", "last_checked": CHECKED,
    },
    {
        "slug": "daad", "order": 8, "name": "DAAD", "full_name": "German Academic Exchange Service scholarships",
        "flag": "🇩🇪", "country": "Germany", "country_uz": "Germaniya", "depth": "full",
        "levels": "master,phd", "languages": "english", "fully_funded": True,
        "summary": "Germany's catalogue of scholarships for master's and doctoral study. For professionals from Uzbekistan the key one is EPOS: two years' work experience, courses with their own deadlines.",
        "summary_uz": "Germaniyaning magistratura va doktorantura uchun stipendiyalar katalogi. Oʻzbekistonlik mutaxassislar uchun asosiysi EPOS: ikki yillik ish tajribasi, har bir kursning oʻz muddati.",
        "covers": DAAD_COVERS, "covers_uz": DAAD_COVERS_UZ,
        "usual_period": "Depends on the programme — many EPOS courses close in the autumn a year before study",
        "usual_period_uz": "Dasturga bogʻliq — koʻp EPOS kurslari oʻqishdan bir yil oldingi kuzda yopiladi",
        "body": DAAD_BODY, "body_uz": DAAD_BODY_UZ,
        "official_url": "https://www.daad.de/en/studying-in-germany/scholarships/", "last_checked": CHECKED,
    },
    {
        "slug": "fulbright", "order": 7, "name": "Fulbright", "full_name": "Fulbright Foreign Student Program",
        "flag": "🇺🇸", "country": "United States", "country_uz": "AQSh", "depth": "full",
        "levels": "master", "languages": "english", "fully_funded": True,
        "summary": "A master's in the United States for up to two years, for graduates with two years' work experience. Run by the U.S. Embassy in Tashkent; priority to AI, STEM and aerospace fields.",
        "summary_uz": "AQShda ikki yilgacha magistratura — ikki yillik ish tajribasi bor bitiruvchilar uchun. Toshkentdagi AQSh elchixonasi oʻtkazadi; sunʼiy intellekt, STEM va aerokosmik sohalarga ustuvorlik.",
        "covers": FUL_COVERS, "covers_uz": FUL_COVERS_UZ,
        "usual_period": "Once a year, announced by the U.S. Embassy (2027–28 instructions: March 2026)",
        "usual_period_uz": "Yiliga bir marta, AQSh elchixonasi eʼlon qiladi (2027–28 yoʻriqnomasi: 2026-yil mart)",
        "body": FUL_BODY, "body_uz": FUL_BODY_UZ,
        "official_url": "https://uz.usembassy.gov/fulbright-foreign-student-program/", "last_checked": CHECKED,
    },
]

DEADLINES = [
    {
        "scholarship": "eyuf",
        "label": "El-Yurt Umidi — spring competition 2026", "label_uz": "«El-yurt umidi» — 2026-yil bahorgi tanlov",
        "opens": "2026-04-06", "closes": "2026-04-24",
        "note": "500 places; documents on el-yurt.uz.",
        "note_uz": "500 oʻrin; hujjatlar el-yurt.uz da.",
        "source_url": "https://eyuf.uz/", "last_checked": CHECKED,
    },
    {
        "scholarship": "eyuf",
        "label": "El-Yurt Umidi — autumn competition 2026", "label_uz": "«El-yurt umidi» — 2026-yil kuzgi tanlov",
        "opens": None, "closes": "2026-11-26", "is_estimate": True,
        "note": "Estimate from 2025 (window 14–26 November 2025). The window is only 2–3 weeks — have your admission letter and IELTS ready now.",
        "note_uz": "2025-yil asosida taxmin (oyna 2025-yil 14–26-noyabr). Oyna atigi 2–3 hafta — qabul xati va IELTS hozirdan tayyor boʻlsin.",
        "source_url": "https://eyuf.uz/", "last_checked": CHECKED,
    },
]

CHECKLISTS = {
    "eyuf": [
        {"text": "Age within the limit for your level", "text_uz": "Darajangiz uchun yosh chegarasida"},
        {"text": "IELTS 6.0 (bachelor's) or 7.0 (master's/PhD) — or an equivalent certificate", "text_uz": "IELTS 6.0 (bakalavr) yoki 7.0 (magistr/PhD) — yoki unga teng sertifikat"},
        {"text": "Work experience: more than 1 year (master's), more than 2 years (PhD)", "text_uz": "Ish staji: 1 yildan ortiq (magistr), 2 yildan ortiq (PhD)"},
        {"text": "Applied to leading universities abroad — check their QS/THE ranking", "text_uz": "Xorijdagi yetakchi universitetlarga topshirildi — QS/THE reytingini tekshiring"},
        {"text": "Admission letter from a foreign university", "text_uz": "Xorijiy universitetdan qabul xati"},
        {"text": "School certificate or diploma copy", "text_uz": "Attestat yoki diplom nusxasi"},
        {"text": "Work record copy (master's/PhD)", "text_uz": "Mehnat daftarchasi nusxasi (magistr/PhD)"},
        {"text": "Motivation essay", "text_uz": "Motivatsion insho"},
        {"text": "The obligation contract read — years of work in Uzbekistan understood", "text_uz": "Majburiyat shartnomasi oʻqildi — Oʻzbekistonda necha yil ishlash tushunildi"},
        {"text": "Submitted on el-yurt.uz inside the competition window", "text_uz": "Tanlov oynasi ichida el-yurt.uz da topshirildi"},
    ],
    "daad": [
        {"text": "Programme found in the DAAD database (country: Uzbekistan)", "text_uz": "DAAD bazasida dastur topildi (davlat: Oʻzbekiston)"},
        {"text": "For EPOS: bachelor's degree, 2+ years' work, degree ≤ 6 years old", "text_uz": "EPOS uchun: bakalavr diplomi, 2+ yil ish, diplom ≤ 6 yil"},
        {"text": "Course chosen and its own deadline noted", "text_uz": "Kurs tanlandi va uning oʻz muddati yozib olindi"},
        {"text": "DAAD form and CV (Europass)", "text_uz": "DAAD shakli va CV (Europass)"},
        {"text": "Motivation letter tied to your work and plan at home", "text_uz": "Ishingiz va vatandagi rejangizga bogʻlangan motivatsion xat"},
        {"text": "Recommendation letters, including your employer (EPOS)", "text_uz": "Tavsiyanomalar, ish beruvchidan ham (EPOS)"},
        {"text": "Degree and transcripts with certified translations", "text_uz": "Diplom va baholar varaqasi, tasdiqlangan tarjima bilan"},
        {"text": "Consular legalisation — Germany does not accept Uzbek apostilles", "text_uz": "Konsullik legalizatsiyasi — Germaniya oʻzbek apostilini qabul qilmaydi"},
        {"text": "Language certificate (English or German, as the course asks)", "text_uz": "Til sertifikati (kurs talabiga koʻra ingliz yoki nemis tili)"},
    ],
    "fulbright": [
        {"text": "Living in Uzbekistan through the whole selection", "text_uz": "Butun tanlov davomida Oʻzbekistonda yashash"},
        {"text": "Bachelor's degree completed", "text_uz": "Bakalavriat tugatilgan"},
        {"text": "At least two years of professional experience", "text_uz": "Kamida ikki yillik ish tajribasi"},
        {"text": "This year's embassy instructions read (English tests, deadlines)", "text_uz": "Elchixonaning shu yilgi yoʻriqnomasi oʻqildi (ingliz tili testlari, muddatlar)"},
        {"text": "Voucher for apply.iie.org received from the embassy", "text_uz": "apply.iie.org uchun vaucher elchixonadan olindi"},
        {"text": "Essays: your work, your field, your plan for Uzbekistan", "text_uz": "Insholar: ishingiz, sohangiz, Oʻzbekiston uchun rejangiz"},
        {"text": "References and transcripts uploaded", "text_uz": "Tavsiyalar va baholar varaqasi yuklandi"},
        {"text": "Test scores ready as the instructions require", "text_uz": "Yoʻriqnoma talab qilgan test natijalari tayyor"},
    ],
}

SAMPLES = [{
    "slug": "daad-epos-motivation", "order": 13, "kind": "statement", "scholarship": "daad",
    "title": "DAAD EPOS motivation letter — Nodira, water management (master's)",
    "title_uz": "DAAD EPOS motivatsion xati — Nodira, suv resurslarini boshqarish (magistratura)",
    "intro": "<p>Nodira is fictional: a hydraulic engineer from Karakalpakstan with three years at a regional water authority, applying to an EPOS-listed master's course. EPOS looks for a <strong>development-related</strong> motivation: what you will change at home, and why this course is the tool. Follow the length and format the course asks for.</p>",
    "intro_uz": "<p>Nodira — oʻylab topilgan qahramon: Qoraqalpogʻistonlik gidrotexnik muhandis, viloyat suv xoʻjaligi boshqarmasida uch yil ishlagan, EPOS roʻyxatidagi magistratura kursiga topshiryapti. EPOS <strong>rivojlanish bilan bogʻliq</strong> maqsadni qidiradi: vataningizda nimani oʻzgartirasiz va nega aynan shu kurs buning vositasi. Kurs soʻragan hajm va formatga amal qiling.</p>",
    "letter": """
<p>Dear Selection Committee,</p>
<p>I am applying for the Master's programme in Integrated Water Resources Management with a DAAD EPOS scholarship. For three years I have worked as an engineer at the irrigation authority of a district in Karakalpakstan, where every summer I see the same choice: which farms receive water and which do not, decided by phone calls rather than data.</p>
<p>In my work I maintain canals and pumping stations, and I led a small project to install water meters at 14 canal outlets. For the first time we could show how much water each farm actually received; in the first season, losses on two canals fell by about a fifth after repairs that the data had pointed to. The project also taught me that technology is the easy part: the farmers trusted the numbers only after we explained them at village meetings.</p>
<p>This course fits my work because it combines hydrology with water governance and economics — exactly the gap I feel. I know how to fix a canal; I do not yet know how to design a fair allocation system or argue for it with institutions. The course's field project would let me work on a real basin, and I would like to base my thesis on data from my district.</p>
<p>After the degree, I will return to the irrigation authority, which has agreed to keep my position, and propose a district water-allocation plan based on measured data. In the longer term I want to contribute to basin-level planning in the Amu Darya delta, where every cubic metre matters.</p>
<p>Sincerely,<br>Nodira Ismoilova</p>
""",
    "notes": [
        {"para": 2, "en": "Course, scholarship and her job in the first lines — then the <strong>development problem</strong> she lives with. EPOS wants exactly this link.", "uz": "Birinchi qatorlarda kurs, stipendiya va ishi — keyin u har kuni duch keladigan <strong>rivojlanish muammosi</strong>. EPOS aynan shu bogʻliqlikni xohlaydi."},
        {"para": 3, "en": "Professional evidence with numbers, plus a lesson about people, not only technology — a sign of someone who can lead change.", "uz": "Raqamli kasbiy dalil va faqat texnologiya emas, odamlar haqidagi saboq — oʻzgarishga yetakchilik qila oladigan odam belgisi."},
        {"para": 4, "en": "“Why this course” answered by naming <strong>the gap in her skills</strong> the course fills. Use the real modules of your course.", "uz": "«Nega aynan shu kurs» — kurs toʻldiradigan <strong>koʻnikmalaridagi boʻshliq</strong>ni nomlash bilan javob. Kursingizning haqiqiy modullaridan foydalaning."},
        {"para": 5, "en": "A concrete return: the same employer, a named proposal, a wider goal. If your employer will support you, say so — and ask them to confirm it in their letter.", "uz": "Aniq qaytish: oʻsha ish beruvchi, nomlangan taklif, kengroq maqsad. Ish beruvchingiz qoʻllasa, buni ayting — va ulardan buni xatlarida tasdiqlashni soʻrang."},
    ],
    "prompts": [
        {"en": "The course, and the development problem you meet in your work.", "uz": "Kurs va ishingizda duch keladigan rivojlanish muammosi.", "lines": 3},
        {"en": "Something you did about it — with numbers — and what it taught you about people.", "uz": "Bu borada nima qildingiz — raqamlar bilan — va bu sizga odamlar haqida nima oʻrgatdi.", "lines": 4},
        {"en": "The gap in your skills, and which modules of the course fill it.", "uz": "Koʻnikmalaringizdagi boʻshliq va kursning qaysi modullari uni toʻldiradi.", "lines": 3},
        {"en": "Your plan at home: employer, proposal, wider goal.", "uz": "Vatandagi rejangiz: ish beruvchi, taklif, kengroq maqsad.", "lines": 3},
    ],
},
{
    "slug": "fulbright-study-objectives", "order": 15, "kind": "statement", "scholarship": "fulbright",
    "title": "Fulbright study objectives — Malika, data science (master's)",
    "title_uz": "Fulbright oʻqish maqsadlari — Malika, maʼlumotlar ilmi (magistratura)",
    "intro": "<p>Malika is fictional: a data analyst with three years at a regional statistics office. The Fulbright application asks for essays about what you will study and why — the exact essays and limits are in the embassy's current instructions. This one shows a study-objectives essay in a priority field.</p>",
    "intro_uz": "<p>Malika — oʻylab topilgan qahramon: viloyat statistika boshqarmasida uch yil ishlagan maʼlumotlar tahlilchisi. Fulbright arizasi nimani va nega oʻqishingiz haqida insholar soʻraydi — aniq insholar va chegaralar elchixonaning joriy yoʻriqnomasida. Bu yerda ustuvor sohadagi oʻqish maqsadlari inshosi koʻrsatilgan.</p>",
    "letter": """
<p>I want to earn a master's degree in data science in the United States so that Uzbekistan's regional statistics can be used to make decisions, not only reports.</p>
<p>For three years I have worked as an analyst at the statistics office of my region. Every month we publish dozens of tables on employment, prices and agriculture, but local officials rarely use them, because they arrive late and are hard to read. On my own initiative I built a simple dashboard of monthly food prices for the regional administration; it became the first of our products that officials asked for every week. It showed me both the value of our data and how much I still need to learn.</p>
<p>In a U.S. master's programme I want to gain three things. First, rigorous training in statistical learning and machine learning, so that I can build forecasts officials can trust. Second, experience with data engineering — the pipelines that turn raw survey files into timely, clean datasets. Third, an understanding of responsible data use: privacy and fairness matter when government data describes real people.</p>
<p>I am drawn to programmes that combine these with applied projects for public agencies, so that my thesis can be a real forecasting tool rather than an exercise. Learning alongside students from many countries will also show me how other governments organise their data.</p>
<p>After returning, I plan to lead a small analytics team at my office, starting with a monthly forecast of regional prices and employment, and to share the methods with other regional offices. In the long term I want to help build a national standard for open, timely regional statistics.</p>
""",
    "notes": [
        {"para": 1, "en": "The degree and its <strong>purpose at home</strong> in one sentence — a reader knows the whole essay from it.", "uz": "Daraja va uning <strong>vatandagi maqsadi</strong> bir gapda — oʻquvchi butun inshoni shundan biladi."},
        {"para": 2, "en": "The problem from her own work, and something she did on her own initiative, with a visible result. Fulbright looks for professionals who already act.", "uz": "Oʻz ishidagi muammo va oʻz tashabbusi bilan qilgan, natijasi koʻrinadigan ish. Fulbright allaqachon harakat qilayotgan mutaxassislarni qidiradi."},
        {"para": 3, "en": "<strong>Three specific things</strong> to learn — each tied to a gap. This is the heart of a study-objectives essay; it also connects naturally to the embassy's priority fields.", "uz": "Oʻrganiladigan <strong>uchta aniq narsa</strong> — har biri boʻshliqqa bogʻlangan. Bu oʻqish maqsadlari inshosining yuragi; u elchixonaning ustuvor sohalariga ham tabiiy bogʻlanadi."},
        {"para": 4, "en": "What kind of programme suits her — without naming universities she cannot be sure of. Fulbright often handles placement, so describe the fit.", "uz": "Unga qanday dastur mos kelishi — aniq boʻlmagan universitetlarni nomlamasdan. Joylashtirishni koʻpincha Fulbright hal qiladi, shuning uchun moslikni tasvirlang."},
        {"para": 5, "en": "A return plan in steps: a team, a first product, a wider goal for the country.", "uz": "Bosqichli qaytish rejasi: jamoa, birinchi mahsulot, davlat uchun kengroq maqsad."},
    ],
    "prompts": [
        {"en": "The degree you want and its purpose at home, in one sentence.", "uz": "Xohlagan darajangiz va uning vatandagi maqsadi, bir gapda.", "lines": 2},
        {"en": "A problem from your work, and something you did about it on your own initiative.", "uz": "Ishingizdagi muammo va bu borada oʻz tashabbusingiz bilan qilgan ishingiz.", "lines": 4},
        {"en": "Three things you will learn — each tied to a gap in your skills.", "uz": "Oʻrganadigan uchta narsa — har biri koʻnikmalaringizdagi boʻshliqqa bogʻlangan.", "lines": 4},
        {"en": "What kind of programme fits you (projects, courses, setting).", "uz": "Sizga qanday dastur mos (loyihalar, fanlar, muhit).", "lines": 3},
        {"en": "Your plan after returning: first step and long-term goal.", "uz": "Qaytgandan keyingi rejangiz: birinchi qadam va uzoq muddatli maqsad.", "lines": 3},
    ],
},
{
    "slug": "eyuf-motivation-essay", "order": 16, "kind": "statement", "scholarship": "eyuf", "letter_lang": "uz",
    "title": "El-Yurt Umidi motivation essay — Shahzod, urban planning (master's)",
    "title_uz": "«El-yurt umidi» motivatsion inshosi — Shahzod, shaharsozlik (magistratura)",
    "intro": "<p>Shahzod is fictional: an architect with three years at a district khokimiyat's construction department, who has already won a place on a master's in urban planning abroad. The foundation funds study that will be used in Uzbekistan — so the essay is about the work waiting for you at home. Write it in the language the competition asks for; this sample is in Uzbek.</p>",
    "intro_uz": "<p>Shahzod — oʻylab topilgan qahramon: tuman hokimligi qurilish boʻlimida uch yil ishlagan arxitektor, xorijda shaharsozlik magistraturasiga allaqachon qabul qilingan. Jamgʻarma Oʻzbekistonda qoʻllaniladigan oʻqishni moliyalashtiradi — shuning uchun insho vatanda sizni kutayotgan ish haqida. Tanlov soʻragan tilda yozing; bu namuna oʻzbek tilida.</p>",
    "letter": """
<p>Men xorijdagi universitetning shaharsozlik magistratura dasturiga qabul qilindim va oʻqishimni «El-yurt umidi» jamgʻarmasi orqali moliyalashtirishni soʻrayman. Tanlagan yoʻnalishim Farmonda koʻrsatilgan ustuvor sohalardan biri — urbanizatsiya bilan bevosita bogʻliq.</p>
<p>Uch yildan beri tuman hokimligi qurilish boʻlimida arxitektor boʻlib ishlayman. Tumanimizda har yili yangi uy-joy massivlari quriladi, lekin maktab, bogʻcha va jamoat transporti ularga yetib bormaydi: yangi mahallalar shahar ichidagi orolchalarga aylanmoqda. Ikki yil oldin men birinchi marta yangi massivlar uchun piyodalar yoʻlaklari va avtobus bekatlari sxemasini tayyorladim; ulardan uchtasi qurildi va bir massivda bekatgacha boʻlgan yoʻl 25 daqiqadan 8 daqiqaga qisqardi.</p>
<p>Shu ish menga bilimim yetmayotgan joyni koʻrsatdi: men alohida obyektni loyihalay olaman, lekin butun hududning uzoq muddatli rejasini — aholi, transport va ijtimoiy obyektlarni birga — tuza olmayman. Magistratura dasturi aynan shu boʻshliqni toʻldiradi: shaharni rejalashtirish, transport va geografik axborot tizimlari boʻyicha fanlar, real shahar loyihasida amaliyot.</p>
<p>Oʻqishni tugatgach, men Oʻzbekistonga qaytib, majburiyatimga muvofiq davlat tizimida ishlayman. Maqsadim — tumanimiz uchun birinchi kompleks rivojlanish rejasini tayyorlash va keyinchalik shu tajribani viloyatning boshqa tumanlariga yoyish.</p>
<p>Bu imkoniyat men uchun shaxsiy yutuq emas, balki yangi mahallalarimizdagi minglab oilalarning kundalik hayotini yaxshilash yoʻli deb bilaman.</p>
""",
    "notes": [
        {"para": 1, "en": "States the admission is <strong>already won</strong> (the foundation requires it) and links the field to the decree's priority areas.", "uz": "Qabul <strong>allaqachon olingani</strong>ni aytadi (jamgʻarma buni talab qiladi) va yoʻnalishni Farmondagi ustuvor sohalar bilan bogʻlaydi."},
        {"para": 2, "en": "A real problem in his district, and what he already did, <strong>with a number</strong> (25 → 8 minutes).", "uz": "Tumanidagi haqiqiy muammo va u allaqachon qilgan ish, <strong>raqam bilan</strong> (25 → 8 daqiqa)."},
        {"para": 3, "en": "The honest gap in his skills — and how the programme fills it.", "uz": "Koʻnikmalaridagi halol boʻshliq — va dastur uni qanday toʻldirishi."},
        {"para": 4, "en": "Accepts the <strong>work obligation</strong> openly and turns it into a plan: a first concrete result, then spreading it.", "uz": "<strong>Ishlash majburiyati</strong>ni ochiq qabul qiladi va uni rejaga aylantiradi: birinchi aniq natija, keyin uni yoyish."},
        {"para": 5, "en": "A short closing that puts the people who benefit at the centre.", "uz": "Foyda koʻradigan odamlarni markazga qoʻyadigan qisqa yakun."},
    ],
    "prompts": [
        {"en": "The programme you were admitted to, and how it connects to Uzbekistan's priority fields.", "uz": "Qabul qilingan dasturingiz va u Oʻzbekistonning ustuvor sohalari bilan qanday bogʻlanadi.", "lines": 3},
        {"en": "A problem in your workplace or region, and what you already did — with a number.", "uz": "Ish joyingiz yoki hududingizdagi muammo va allaqachon qilgan ishingiz — raqam bilan.", "lines": 4},
        {"en": "The gap in your skills and how the programme fills it.", "uz": "Koʻnikmalaringizdagi boʻshliq va dastur uni qanday toʻldiradi.", "lines": 3},
        {"en": "Your plan within the work obligation: first result, then wider.", "uz": "Ishlash majburiyati doirasidagi rejangiz: birinchi natija, keyin kengroq.", "lines": 3},
        {"en": "Who in Uzbekistan benefits from your study?", "uz": "Oʻqishingizdan Oʻzbekistonda kim foyda koʻradi?", "lines": 2},
    ],
}]
