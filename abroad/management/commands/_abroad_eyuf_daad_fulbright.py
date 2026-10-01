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
