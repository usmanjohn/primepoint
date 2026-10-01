"""Study abroad — MEXT (Japanese Government Scholarship), in depth.

Sources, read 2026-10-01:
  · Application Guidelines, MEXT Scholarship for 2027, Undergraduate Students
    (Embassy Recommendation) — studyinjapan.go.jp (published April 2026).
  · Application Guidelines, MEXT Scholarship for 2027, Research Students
    (Embassy Recommendation) — studyinjapan.go.jp (published April 2026).
  · Embassy of Japan in Uzbekistan: MEXT 2027 "Undergraduate Students" and
    "Research Students" announcements — deadline 25 May 2026 for both.
Every figure below is from those documents; MEXT's own words: "the amount of
payment may be subject to change each fiscal year".

    python manage.py import_abroad abroad/management/commands/_abroad_mext.py --author=prime --republish
"""
CHECKED = "2026-10-01"
UG_PDF = "https://www.studyinjapan.go.jp/en/_mt/2026/04/2027_Guidelines_Undergraduate_E.pdf"
RES_PDF = "https://www.studyinjapan.go.jp/en/_mt/2026/04/01-2027_Research_Guidelines_E.pdf"
EMBASSY = "https://www.uz.emb-japan.go.jp/itpr_uz/programMEXT.html"

COVERS = """
<table>
<tr><th>Item</th><th>MEXT 2027</th></tr>
<tr><td>Monthly allowance — undergraduate</td><td>¥117,000</td></tr>
<tr><td>Monthly allowance — research student (non-regular / preparatory)</td><td>¥143,000</td></tr>
<tr><td>Monthly allowance — master's (regular student)</td><td>¥144,000</td></tr>
<tr><td>Monthly allowance — doctoral (regular student)</td><td>¥145,000</td></tr>
<tr><td>Regional supplement</td><td>+¥2,000 or ¥3,000 a month in specially designated regions</td></tr>
<tr><td>Tuition</td><td>Entrance-exam, matriculation and tuition fees waived</td></tr>
<tr><td>Flights</td><td>Economy ticket to Japan at the start, and home at the end if you return on time</td></tr>
</table>
<div class="ab-mistake"><strong>What it does not pay</strong>
<p>Travel inside your own country to the airport, airport taxes, travel insurance and extra baggage. And if you arrive outside the set dates for personal reasons, the flight is not paid.</p></div>
<p class="ab-src">Source: MEXT 2027 Application Guidelines (Undergraduate; Research Students), section “Scholarship benefits”. MEXT: “the amount of payment may be subject to change each fiscal year.”</p>
"""

COVERS_UZ = """
<table>
<tr><th>Nima</th><th>MEXT 2027</th></tr>
<tr><td>Oylik stipendiya — bakalavr</td><td>117 000 iyena</td></tr>
<tr><td>Oylik stipendiya — tadqiqotchi talaba (tayyorlov / nodaraja)</td><td>143 000 iyena</td></tr>
<tr><td>Oylik stipendiya — magistratura (daraja talabasi)</td><td>144 000 iyena</td></tr>
<tr><td>Oylik stipendiya — doktorantura (daraja talabasi)</td><td>145 000 iyena</td></tr>
<tr><td>Hududiy qoʻshimcha</td><td>maxsus hududlarda oyiga +2 000 yoki 3 000 iyena</td></tr>
<tr><td>Kontrakt</td><td>Kirish imtihoni, qabul va oʻqish toʻlovlari olinmaydi</td></tr>
<tr><td>Aviabilet</td><td>Boshida Yaponiyaga ekonom bilet, oxirida — vaqtida qaytsangiz — uyga</td></tr>
</table>
<div class="ab-mistake"><strong>Nimani toʻlamaydi</strong>
<p>Oʻz davlatingiz ichida aeroportgacha yoʻl, aeroport soliqlari, sayohat sugʻurtasi va qoʻshimcha yuk. Agar shaxsiy sabab bilan belgilangan sanalardan tashqari kelsangiz, bilet toʻlanmaydi.</p></div>
<p class="ab-src">Manba: MEXT 2027 yoʻriqnomalari (bakalavr; tadqiqotchi talabalar), «Stipendiya imtiyozlari» boʻlimi. MEXT: «toʻlov miqdori har moliyaviy yilda oʻzgarishi mumkin».</p>
"""

BODY = """
<ul class="ab-toc">
<li><a href="#what">What it is</a></li><li><a href="#routes">Two routes</a></li><li><a href="#ug">Bachelor's</a></li>
<li><a href="#exams">The exams</a></li><li><a href="#research">Master's / PhD</a></li><li><a href="#prof">The professor</a></li>
<li><a href="#docs">Documents</a></li><li><a href="#year">Timeline</a></li><li><a href="#mistakes">Mistakes</a></li>
</ul>

<h2 id="what">What it is</h2>
<p>MEXT is the scholarship of Japan's Ministry of Education (the old name, <em>Monbukagakusho</em>, is still used). It pays tuition, a monthly allowance and flights for a full degree in Japan. Most grantees first spend a year — or, for research students, six months — learning Japanese.</p>
<p>The biggest difference from GKS: <strong>MEXT tests you</strong>. The Japanese Embassy holds written exams, then an interview.</p>

<h2 id="routes">Two routes</h2>
<table>
<tr><th></th><th>Embassy recommendation</th><th>University recommendation</th></tr>
<tr><td>Who selects you first</td><td>The Embassy of Japan in Tashkent</td><td>A Japanese university that nominates you</td></tr>
<tr><td>When</td><td>Call in spring (2027 cycle: deadline 25 May 2026 in Uzbekistan)</td><td>Each university's own calendar</td></tr>
<tr><td>Best for</td><td>Most applicants from Uzbekistan</td><td>Students already in touch with a university that takes part</td></tr>
</table>
<p>This page follows the Embassy route; the programmes are: <strong>Undergraduate</strong>, <strong>Research Students</strong> (master's/PhD), plus Japanese Studies, Teacher Training and others the Embassy announces.</p>

<h2 id="ug">Bachelor's — Undergraduate Students</h2>
<ul>
<li><strong>Age:</strong> born on or after 2 April 2002 (2027 cycle).</li>
<li><strong>School:</strong> 12 years of schooling completed (or by March 2027), <em>or</em> completion of a school equivalent to a Japanese upper-secondary school.</li>
<li><strong>Language:</strong> no Japanese needed to apply — but you must be willing to study <em>in</em> Japanese.</li>
<li><strong>Fields:</strong> you choose a course (Social Sciences and Humanities A or B; Natural Sciences A, B or C) and up to three majors. Art and music are not eligible. You cannot change course later.</li>
<li><strong>Preparatory year:</strong> humanities grantees study one year at ABK College, science grantees at Osaka University — Japanese plus school subjects. Then you sit the university's entrance exam. MEXT decides the university; you cannot object.</li>
<li><strong>Length:</strong> 5 years (1 + 4); 7 years for medicine, dentistry, veterinary science and six-year pharmacy.</li>
<li><strong>Arrival:</strong> 1–7 April 2027.</li>
</ul>
<div class="ab-fact"><strong>11 years or 12?</strong>
<p>Uzbek school is 11 years. The 2027 guidelines accept either 12 years of schooling <em>or</em> a school equivalent to Japanese upper-secondary school — but <strong>direct placement needs the 12-year (or equivalent-exam) condition</strong>, so an 11-year graduate goes through the preparatory year. If your case is unclear, ask the Embassy before you apply.</p></div>
<div class="ab-uz"><strong>Direct placement</strong>
<p>If your Japanese (or, for some English-taught courses, your English) is already strong enough, you can ask to skip the preparatory year and enter a university directly — decided after the second screening. A JLPT certificate is how universities judge it. <a href="/tutorials/">Prime Japanese</a> on Powerty is built to take you from zero towards N4.</p></div>

<h2 id="exams">The written exams (Undergraduate)</h2>
<table>
<tr><th>Your course</th><th>You write</th></tr>
<tr><td>Social Sciences and Humanities A or B</td><td>Japanese, English, Mathematics (A)</td></tr>
<tr><td>Natural Sciences A</td><td>Japanese, English, Mathematics (B), Chemistry, Physics</td></tr>
<tr><td>Natural Sciences B or C</td><td>Japanese, English, Mathematics (B), Chemistry, Biology</td></tr>
</table>
<p>No calculators. Everyone sits the Japanese paper, even beginners — it is used to place you in the preparatory course. Past papers are published on Study in Japan: <strong>practise them under time</strong>; the maths and science papers are where most applicants are separated.</p>
<div class="ab-tip"><strong>Maths is the gate</strong><p>For science courses, the Mathematics (B) paper goes beyond the usual school syllabus in places. Start past papers months early, and use Powerty's maths courses to close gaps.</p></div>

<h2 id="research">Master's and PhD — Research Students</h2>
<ul>
<li><strong>Age:</strong> born on or after 2 April 1992 (2027 cycle).</li>
<li><strong>Education:</strong> 16 years of schooling, or a bachelor's-equivalent degree from a programme of three years or more — completed by the time you enrol.</li>
<li><strong>Exams:</strong> written Japanese and English tests, then an interview. The committee wants a <strong>detailed, concrete research plan</strong> and proof you have researched Japanese universities.</li>
<li><strong>Status:</strong> many start as “non-regular” research students (often with six months of Japanese), then sit the graduate-school entrance exam to become regular master's or doctoral students.</li>
</ul>

<h2 id="prof">The step that decides it: a professor's provisional acceptance</h2>
<p>If you pass the Embassy's first screening, you must <strong>contact Japanese professors yourself and obtain a letter of provisional acceptance</strong> — in the 2027 cycle, by 1 September 2026. Without one, you cannot be placed. Choose two or three professors whose recent papers match your research plan, and write to each a short, specific email.</p>
<p>See the annotated sample: <em>A first email to a professor</em>, and the <em>MEXT research plan</em> sample.</p>

<h2 id="docs">Documents (submitted on paper to the Embassy)</h2>
<ul>
<li>Application Form (2027 form), with a 4.5 × 3.5 cm photo taken within six months.</li>
<li>Academic transcripts and graduation certificate (or certificate of prospective graduation).</li>
<li>Recommendation letter — Undergraduate: from a class teacher or principal; Research: from the dean or your academic advisor (and from your employer if you work).</li>
<li>Medical certificate on the 2027 form.</li>
<li>Research Students also: <strong>Field of Study and Research Plan</strong>, Placement Preference Form, abstracts of theses if any.</li>
<li>Language certificates if you have them (JLPT, IELTS, TOEFL) — issued within the last two years.</li>
</ul>
<p>Everything in Japanese or English, or with a translation attached; one original set plus copies (Undergraduate: one copy; Research: two), each document numbered in the top-right corner as the guidelines list them.</p>

<h2 id="year">A year of MEXT, month by month (Embassy route)</h2>
<ol class="ab-steps">
<li><strong>Mid-April</strong> — the Embassy announces the call. Download this year's forms.</li>
<li><strong>By the deadline</strong> (2027 cycle: 25 May 2026) — paper documents to the Embassy of Japan in Tashkent.</li>
<li><strong>May–July</strong> — first screening: documents, written exams, interview.</li>
<li><strong>Research students, by 1 September</strong> — provisional acceptance from a Japanese professor; then the Placement Preference Form (mid-September to early October).</li>
<li><strong>From November</strong> — MEXT's second screening and university placement.</li>
<li><strong>January–March</strong> — results via the Embassy.</li>
<li><strong>April</strong> (or September/October) — arrival in Japan on a newly issued Student visa.</li>
</ol>

<h2 id="mistakes">The mistakes that sink applications</h2>
<ul>
<li><strong>Missing the spring call.</strong> Applications close about a year before you would arrive — pupils who only start looking in autumn have missed it.</li>
<li><strong>Not practising past papers.</strong> The exams are the first filter; a good personal story does not rescue a weak maths paper.</li>
<li><strong>A vague research plan.</strong> “I want to study AI” is not a plan. Name a problem, a method and a professor.</li>
<li><strong>Waiting to be placed with a professor.</strong> You must find one yourself, before the September deadline.</li>
<li><strong>Arriving on the wrong visa</strong> — MEXT requires a newly issued “Student” visa; otherwise the scholarship is suspended.</li>
</ul>
<p class="ab-src">Sources: MEXT 2027 Application Guidelines (Undergraduate; Research Students), Study in Japan; Embassy of Japan in Uzbekistan, MEXT 2027 announcements.</p>
"""

BODY_UZ = """
<ul class="ab-toc">
<li><a href="#what">Bu nima</a></li><li><a href="#routes">Ikki yoʻl</a></li><li><a href="#ug">Bakalavr</a></li>
<li><a href="#exams">Imtihonlar</a></li><li><a href="#research">Magistratura / PhD</a></li><li><a href="#prof">Professor</a></li>
<li><a href="#docs">Hujjatlar</a></li><li><a href="#year">Jadval</a></li><li><a href="#mistakes">Xatolar</a></li>
</ul>

<h2 id="what">Bu nima</h2>
<p>MEXT — Yaponiya Taʼlim vazirligining stipendiyasi (eski nomi <em>Monbukagakusho</em> hanuz ishlatiladi). U Yaponiyada toʻliq oʻqish uchun kontrakt, oylik stipendiya va aviabiletni toʻlaydi. Koʻp stipendiatlar avval bir yil — tadqiqotchi talabalar olti oy — yapon tilini oʻrganadi.</p>
<p>GKSdan eng katta farqi: <strong>MEXT sizni imtihon qiladi</strong>. Yaponiya elchixonasi yozma imtihonlar, keyin suhbat oʻtkazadi.</p>

<h2 id="routes">Ikki yoʻl</h2>
<table>
<tr><th></th><th>Elchixona tavsiyasi</th><th>Universitet tavsiyasi</th></tr>
<tr><td>Sizni birinchi kim tanlaydi</td><td>Yaponiyaning Toshkentdagi elchixonasi</td><td>Sizni tavsiya qiladigan Yaponiya universiteti</td></tr>
<tr><td>Qachon</td><td>Bahorda eʼlon (2027 tsikli: Oʻzbekistonda muddat 2026-yil 25-may)</td><td>Har bir universitetning oʻz jadvali</td></tr>
<tr><td>Kimga mos</td><td>Oʻzbekistondan topshiruvchilarning koʻpchiligiga</td><td>Ishtirokchi universitet bilan allaqachon aloqasi borlarga</td></tr>
</table>
<p>Bu sahifa elchixona yoʻli haqida; dasturlar: <strong>Undergraduate</strong> (bakalavr), <strong>Research Students</strong> (magistratura/PhD), shuningdek elchixona eʼlon qiladigan yaponshunoslik, oʻqituvchilar malakasini oshirish va boshqalar.</p>

<h2 id="ug">Bakalavr — Undergraduate Students</h2>
<ul>
<li><strong>Yosh:</strong> 2002-yil 2-apreldan keyin (shu kuni ham) tugʻilgan (2027 tsikli).</li>
<li><strong>Maktab:</strong> 12 yillik taʼlim tugatilgan (yoki 2027-yil martigacha), <em>yoki</em> Yaponiyadagi yuqori oʻrta maktabga teng maktab tugatilgan.</li>
<li><strong>Til:</strong> topshirish uchun yapon tili shart emas — lekin yapon <em>tilida</em> oʻqishga tayyor boʻlishingiz kerak.</li>
<li><strong>Yoʻnalishlar:</strong> kursni tanlaysiz (Ijtimoiy va gumanitar fanlar A yoki B; Tabiiy fanlar A, B yoki C) va 3 tagacha mutaxassislik. Sanʼat va musiqa kirmaydi. Keyin kursni oʻzgartirib boʻlmaydi.</li>
<li><strong>Tayyorlov yili:</strong> gumanitarlar bir yil ABK kollejida, tabiiy fanchilar Osaka universitetida oʻqiydi — yapon tili va maktab fanlari. Keyin universitetning kirish imtihonini topshirasiz. Universitetni MEXT belgilaydi; eʼtiroz qabul qilinmaydi.</li>
<li><strong>Muddat:</strong> 5 yil (1 + 4); tibbiyot, stomatologiya, veterinariya va olti yillik farmatsiya uchun 7 yil.</li>
<li><strong>Kelish:</strong> 2027-yil 1–7-aprel.</li>
</ul>
<div class="ab-fact"><strong>11 yilmi yoki 12?</strong>
<p>Oʻzbek maktabi 11 yillik. 2027 yoʻriqnomasi 12 yillik taʼlimni <em>yoki</em> Yaponiya yuqori oʻrta maktabiga teng maktabni qabul qiladi — lekin <strong>toʻgʻridan-toʻgʻri joylashtirish uchun 12 yillik (yoki unga teng imtihon) sharti kerak</strong>, shuning uchun 11 yillik maktab bitiruvchisi tayyorlov yilidan oʻtadi. Holatingiz noaniq boʻlsa, topshirishdan oldin elchixonadan soʻrang.</p></div>
<div class="ab-uz"><strong>Toʻgʻridan-toʻgʻri joylashtirish</strong>
<p>Agar yapon tilingiz (baʼzi inglizcha kurslar uchun — ingliz tilingiz) yetarlicha kuchli boʻlsa, tayyorlov yilini oʻtkazib, toʻgʻridan-toʻgʻri universitetga kirishni soʻrashingiz mumkin — bu ikkinchi saralashdan keyin hal qilinadi. Universitetlar buni JLPT sertifikati orqali baholaydi. Powerty'dagi <a href="/tutorials/">Prime Japanese</a> sizni noldan N4 sari olib borish uchun qurilgan.</p></div>

<h2 id="exams">Yozma imtihonlar (bakalavr)</h2>
<table>
<tr><th>Kursingiz</th><th>Nimani yozasiz</th></tr>
<tr><td>Ijtimoiy va gumanitar fanlar A yoki B</td><td>Yapon tili, ingliz tili, matematika (A)</td></tr>
<tr><td>Tabiiy fanlar A</td><td>Yapon tili, ingliz tili, matematika (B), kimyo, fizika</td></tr>
<tr><td>Tabiiy fanlar B yoki C</td><td>Yapon tili, ingliz tili, matematika (B), kimyo, biologiya</td></tr>
</table>
<p>Kalkulyator mumkin emas. Yapon tili imtihonini hamma, hatto yangi boshlovchilar ham yozadi — natija sizni tayyorlov kursiga joylashtirish uchun ishlatiladi. Oʻtgan yillar savollari Study in Japan saytida eʼlon qilinadi: <strong>ularni vaqt bilan ishlang</strong>; nomzodlar asosan matematika va tabiiy fanlar qogʻozlarida ajraladi.</p>
<div class="ab-tip"><strong>Matematika — asosiy toʻsiq</strong><p>Tabiiy fanlar uchun matematika (B) qogʻozi baʼzi joylarda odatiy maktab dasturidan chiqadi. Oʻtgan yillar savollarini oylar oldin boshlang va boʻshliqlarni Powerty'dagi matematika kurslari bilan toʻldiring.</p></div>

<h2 id="research">Magistratura va PhD — Research Students</h2>
<ul>
<li><strong>Yosh:</strong> 1992-yil 2-apreldan keyin (shu kuni ham) tugʻilgan (2027 tsikli).</li>
<li><strong>Taʼlim:</strong> 16 yillik taʼlim yoki kamida uch yillik dasturda olingan bakalavrga teng daraja — oʻqishga kirgunga qadar.</li>
<li><strong>Imtihonlar:</strong> yozma yapon va ingliz tili testlari, keyin suhbat. Komissiya <strong>batafsil va aniq tadqiqot rejasi</strong>ni hamda Yaponiya universitetlarini oʻrganganingizni koʻrmoqchi.</li>
<li><strong>Maqom:</strong> koʻpchilik avval «nodaraja» tadqiqotchi talaba sifatida boshlaydi (koʻpincha olti oy yapon tili bilan), keyin magistratura yoki doktoranturaga kirish imtihonini topshiradi.</li>
</ul>

<h2 id="prof">Hal qiluvchi qadam: professorning dastlabki roziligi</h2>
<p>Elchixonaning birinchi saralashidan oʻtsangiz, Yaponiya professorlari bilan <strong>oʻzingiz bogʻlanib, dastlabki qabul xati (provisional acceptance)</strong> olishingiz kerak — 2027 tsiklida 2026-yil 1-sentabrgacha. Usiz sizni joylashtirib boʻlmaydi. Soʻnggi maqolalari tadqiqot rejangizga mos keladigan ikki-uchta professorni tanlang va har biriga qisqa, aniq xat yozing.</p>
<p>Izohli namunalarni koʻring: <em>Professorga birinchi xat</em> va <em>MEXT tadqiqot rejasi</em>.</p>

<h2 id="docs">Hujjatlar (elchixonaga qogʻozda topshiriladi)</h2>
<ul>
<li>Ariza shakli (2027 shakli), olti oy ichida olingan 4,5 × 3,5 sm rasm bilan.</li>
<li>Baholar varaqasi va tugatganlik hujjati (yoki tugatish arafasida ekanlik haqida maʼlumotnoma).</li>
<li>Tavsiyanoma — bakalavr: sinf rahbari yoki direktordan; tadqiqot: dekan yoki ilmiy rahbardan (ishlasangiz, ish beruvchidan ham).</li>
<li>2027 shaklidagi tibbiy maʼlumotnoma.</li>
<li>Tadqiqotchi talabalar yana: <strong>Field of Study and Research Plan</strong> (tadqiqot rejasi), joylashtirish istagi shakli, agar boʻlsa — ilmiy ishlar annotatsiyalari.</li>
<li>Bor boʻlsa til sertifikatlari (JLPT, IELTS, TOEFL) — soʻnggi ikki yil ichida berilgan.</li>
</ul>
<p>Hammasi yapon yoki ingliz tilida yoki tarjima ilova qilingan holda; bitta asl toʻplam va nusxalar (bakalavr: bitta nusxa; tadqiqot: ikkita), har bir hujjatning oʻng yuqori burchagida yoʻriqnomadagi raqami.</p>

<h2 id="year">MEXT yili, oyma-oy (elchixona yoʻli)</h2>
<ol class="ab-steps">
<li><strong>Aprel oʻrtasi</strong> — elchixona eʼlon beradi. Shu yilgi shakllarni yuklab oling.</li>
<li><strong>Muddatgacha</strong> (2027 tsikli: 2026-yil 25-may) — qogʻoz hujjatlar Yaponiyaning Toshkentdagi elchixonasiga.</li>
<li><strong>May–iyul</strong> — birinchi saralash: hujjatlar, yozma imtihonlar, suhbat.</li>
<li><strong>Tadqiqotchilar, 1-sentabrgacha</strong> — Yaponiya professoridan dastlabki rozilik; keyin joylashtirish istagi shakli (sentabr oʻrtasi – oktabr boshi).</li>
<li><strong>Noyabrdan</strong> — MEXTning ikkinchi saralashi va universitetga joylashtirish.</li>
<li><strong>Yanvar–mart</strong> — natijalar elchixona orqali.</li>
<li><strong>Aprel</strong> (yoki sentabr/oktabr) — yangi berilgan talaba vizasi bilan Yaponiyaga kelish.</li>
</ol>

<h2 id="mistakes">Arizani yiqitadigan xatolar</h2>
<ul>
<li><strong>Bahorgi eʼlonni oʻtkazib yuborish.</strong> Ariza kelishingizdan taxminan bir yil oldin yopiladi — kuzda qidira boshlaganlar kechikkan boʻladi.</li>
<li><strong>Oʻtgan yillar savollarini ishlamaslik.</strong> Imtihonlar — birinchi filtr; chiroyli shaxsiy hikoya zaif matematika qogʻozini qutqarmaydi.</li>
<li><strong>Mavhum tadqiqot rejasi.</strong> «Sunʼiy intellektni oʻrganmoqchiman» — reja emas. Muammo, usul va professorni ayting.</li>
<li><strong>Professorni kutib oʻtirish.</strong> Uni sentabr muddatigacha oʻzingiz topishingiz kerak.</li>
<li><strong>Notoʻgʻri viza bilan kelish</strong> — MEXT yangi berilgan «Student» vizasini talab qiladi; aks holda stipendiya toʻxtatiladi.</li>
</ul>
<p class="ab-src">Manbalar: MEXT 2027 yoʻriqnomalari (bakalavr; tadqiqotchi talabalar), Study in Japan; Yaponiyaning Oʻzbekistondagi elchixonasi, MEXT 2027 eʼlonlari.</p>
"""

SCHOLARSHIPS = [{
    "slug": "mext", "order": 2, "name": "MEXT",
    "full_name": "Japanese Government (Monbukagakusho) Scholarship", "flag": "🇯🇵",
    "country": "Japan", "country_uz": "Yaponiya", "depth": "full",
    "levels": "bachelor,master,phd", "languages": "japanese,english", "fully_funded": True,
    "summary": "Japan's government pays tuition, a monthly allowance and flights. You sit written exams at the Embassy in Tashkent; applications close in late May for study from the next April.",
    "summary_uz": "Yaponiya hukumati kontrakt, oylik stipendiya va aviabiletni toʻlaydi. Toshkentdagi elchixonada yozma imtihon topshirasiz; arizalar may oxirida yopiladi, oʻqish keyingi yil aprelidan.",
    "covers": COVERS, "covers_uz": COVERS_UZ,
    "usual_period": "Embassy call mid-April, deadline late May (2027 cycle: 25 May 2026)",
    "usual_period_uz": "Elchixona eʼloni aprel oʻrtasida, muddat may oxirida (2027 tsikli: 2026-yil 25-may)",
    "body": BODY, "body_uz": BODY_UZ,
    "official_url": "https://www.studyinjapan.go.jp/en/planning/scholarships/mext-scholarships/",
    "last_checked": CHECKED,
}]

DEADLINES = [
    {
        "scholarship": "mext",
        "label": "MEXT 2027 — Embassy (Undergraduate, Research)", "label_uz": "MEXT 2027 — elchixona (bakalavr, tadqiqot)",
        "opens": "2026-04-15", "closes": "2026-05-25",
        "note": "Closed. Research applicants who passed the first screening needed a professor's provisional acceptance by 1 September 2026; results January–March 2027.",
        "note_uz": "Yopilgan. Birinchi saralashdan oʻtgan tadqiqotchilar 2026-yil 1-sentabrgacha professor roziligini olishi kerak edi; natijalar 2027-yil yanvar–mart.",
        "source_url": EMBASSY, "last_checked": CHECKED,
    },
    {
        "scholarship": "mext",
        "label": "MEXT 2028 — Embassy (Undergraduate, Research)", "label_uz": "MEXT 2028 — elchixona (bakalavr, tadqiqot)",
        "opens": None, "closes": "2027-05-25", "is_estimate": True,
        "note": "Estimate from the 2027 cycle (call around mid-April, deadline 25 May 2026 in Uzbekistan). Start exam practice now.",
        "note_uz": "2027 tsikli asosida taxmin (eʼlon aprel oʻrtasi atrofida, Oʻzbekistonda muddat 2026-yil 25-may). Imtihonga tayyorgarlikni hozir boshlang.",
        "source_url": EMBASSY, "last_checked": CHECKED,
    },
]

# Undergraduate grantees are placed at Japanese national universities (2027
# guidelines, preamble). These are national universities; placement is MEXT's
# decision, so the list is orientation, not a menu.
UNIVERSITIES = [
    {"name": "The University of Tokyo", "name_local": "東京大学", "city": "Tokyo", "country": "Japan",
     "url": "https://www.u-tokyo.ac.jp/en/",
     "strengths": "National university; Japan's largest research university.",
     "strengths_uz": "Davlat universiteti; Yaponiyaning eng yirik tadqiqot universiteti."},
    {"name": "Kyoto University", "name_local": "京都大学", "city": "Kyoto", "country": "Japan",
     "url": "https://www.kyoto-u.ac.jp/en",
     "strengths": "National university known for research in the sciences.",
     "strengths_uz": "Tabiiy fanlar boʻyicha tadqiqotlari bilan mashhur davlat universiteti."},
    {"name": "Osaka University", "name_local": "大阪大学", "city": "Osaka", "country": "Japan",
     "url": "https://www.osaka-u.ac.jp/en",
     "strengths": "National university; runs the MEXT preparatory year for science grantees.",
     "strengths_uz": "Davlat universiteti; tabiiy fanlar stipendiatlari uchun MEXT tayyorlov yilini oʻtkazadi."},
    {"name": "Tohoku University", "name_local": "東北大学", "city": "Sendai", "country": "Japan",
     "url": "https://www.tohoku.ac.jp/en/",
     "strengths": "National university, strong in engineering and materials science.",
     "strengths_uz": "Muhandislik va materialshunoslikda kuchli davlat universiteti."},
    {"name": "Nagoya University", "name_local": "名古屋大学", "city": "Nagoya", "country": "Japan",
     "url": "https://en.nagoya-u.ac.jp/",
     "strengths": "National university in Japan's industrial heartland.",
     "strengths_uz": "Yaponiyaning sanoat markazidagi davlat universiteti."},
    {"name": "Kyushu University", "name_local": "九州大学", "city": "Fukuoka", "country": "Japan",
     "url": "https://www.kyushu-u.ac.jp/en/",
     "strengths": "National university in southern Japan with many international students.",
     "strengths_uz": "Janubiy Yaponiyadagi, xorijlik talabalari koʻp davlat universiteti."},
    {"name": "Hokkaido University", "name_local": "北海道大学", "city": "Sapporo", "country": "Japan",
     "url": "https://www.global.hokudai.ac.jp/",
     "strengths": "National university, known for agriculture and veterinary science.",
     "strengths_uz": "Qishloq xoʻjaligi va veterinariya bilan tanilgan davlat universiteti."},
    {"name": "Institute of Science Tokyo", "name_local": "東京科学大学", "city": "Tokyo", "country": "Japan",
     "url": "https://www.isct.ac.jp/en",
     "strengths": "National science, engineering and medicine university (formed in 2024 from Tokyo Tech and Tokyo Medical and Dental University).",
     "strengths_uz": "Fan, muhandislik va tibbiyot davlat universiteti (2024-yilda Tokyo Tech va Tokyo tibbiyot-stomatologiya universitetidan tuzilgan)."},
    {"name": "University of Tsukuba", "name_local": "筑波大学", "city": "Tsukuba", "country": "Japan",
     "url": "https://www.tsukuba.ac.jp/en/",
     "strengths": "National university in Japan's science city.",
     "strengths_uz": "Yaponiyaning «fan shahri»dagi davlat universiteti."},
    {"name": "Hiroshima University", "name_local": "広島大学", "city": "Higashi-Hiroshima", "country": "Japan",
     "url": "https://www.hiroshima-u.ac.jp/en",
     "strengths": "Broad national university with a large international-student office.",
     "strengths_uz": "Keng yoʻnalishli, katta xalqaro boʻlimi bor davlat universiteti."},
]

CHECKLISTS = {
    "mext-u": [
        {"text": "Born on or after 2 April 2002 (check this year's date)", "text_uz": "2002-yil 2-apreldan keyin tugʻilgan (shu yilgi sanani tekshiring)"},
        {"text": "School finished by March of the arrival year (12 years, or an upper-secondary equivalent)", "text_uz": "Kelish yilining martigacha maktab tugatilgan (12 yil yoki yuqori oʻrta maktabga teng)",
         "hint": "Uzbek school is 11 years — direct placement needs 12; ask the Embassy if unsure.", "hint_uz": "Oʻzbek maktabi 11 yillik — toʻgʻridan-toʻgʻri joylashtirish uchun 12 yil kerak; noaniq boʻlsa, elchixonadan soʻrang."},
        {"text": "Course chosen (Humanities A/B or Sciences A/B/C) and up to three majors", "text_uz": "Kurs tanlandi (gumanitar A/B yoki tabiiy A/B/C) va 3 tagacha mutaxassislik"},
        {"text": "Past exam papers practised under time (Japanese, English, Maths, sciences)", "text_uz": "Oʻtgan yillar imtihon savollari vaqt bilan ishlandi (yapon, ingliz, matematika, tabiiy fanlar)"},
        {"text": "Application Form (this year's) with a 4.5 × 3.5 cm photo", "text_uz": "Ariza shakli (shu yilgi) va 4,5 × 3,5 sm rasm"},
        {"text": "Transcripts for all school years — translated into English or Japanese", "text_uz": "Barcha yillar baholar varaqasi — ingliz yoki yapon tiliga tarjima"},
        {"text": "Graduation certificate or certificate of prospective graduation", "text_uz": "Attestat yoki tugatish arafasida ekanlik haqida maʼlumotnoma"},
        {"text": "Recommendation letter from the class teacher or principal", "text_uz": "Sinf rahbari yoki direktordan tavsiyanoma"},
        {"text": "Medical certificate on this year's form, signed by a doctor", "text_uz": "Shu yilgi shakldagi, shifokor imzolagan tibbiy maʼlumotnoma"},
        {"text": "Language certificates (JLPT, IELTS…) if you have them — 2 copies", "text_uz": "Bor boʻlsa til sertifikatlari (JLPT, IELTS…) — 2 nusxa"},
        {"text": "One original set + one copy set, each document numbered top-right", "text_uz": "Bitta asl toʻplam + bitta nusxa, har bir hujjat oʻng yuqorida raqamlangan"},
        {"text": "Delivered to the Embassy of Japan in Tashkent before the deadline", "text_uz": "Muddatgacha Yaponiyaning Toshkentdagi elchixonasiga topshirildi"},
    ],
    "mext-r": [
        {"text": "Born on or after 2 April 1992 (check this year's date)", "text_uz": "1992-yil 2-apreldan keyin tugʻilgan (shu yilgi sanani tekshiring)"},
        {"text": "Bachelor's degree (16 years of education), or completed by enrolment", "text_uz": "Bakalavr diplomi (16 yillik taʼlim) yoki oʻqishga kirgunga qadar tugatiladi"},
        {"text": "Field of Study and Research Plan — a problem, a method, a professor", "text_uz": "Tadqiqot rejasi — muammo, usul, professor"},
        {"text": "Two or three professors found whose recent papers match your plan", "text_uz": "Soʻnggi maqolalari rejangizga mos ikki-uchta professor topildi"},
        {"text": "Application Form and Placement Preference Form (this year's)", "text_uz": "Ariza shakli va joylashtirish istagi shakli (shu yilgi)"},
        {"text": "University transcripts and degree certificate — translated", "text_uz": "Universitet transkripti va diplomi — tarjima bilan"},
        {"text": "Recommendation from your dean or academic advisor (and employer, if working)", "text_uz": "Dekan yoki ilmiy rahbardan tavsiyanoma (ishlasangiz, ish beruvchidan ham)"},
        {"text": "Medical certificate on this year's form", "text_uz": "Shu yilgi shakldagi tibbiy maʼlumotnoma"},
        {"text": "Thesis abstracts, language certificates (3 copies) if you have them", "text_uz": "Bor boʻlsa ilmiy ishlar annotatsiyasi, til sertifikatlari (3 nusxa)"},
        {"text": "After the first screening: provisional acceptance from a professor before the deadline", "text_uz": "Birinchi saralashdan keyin: muddatgacha professordan dastlabki rozilik"},
    ],
}

SAMPLES = [{
    "slug": "mext-research-plan", "order": 6, "kind": "study_plan", "scholarship": "mext",
    "title": "MEXT research plan — Dilnoza, water management",
    "title_uz": "MEXT tadqiqot rejasi — Dilnoza, suv resurslarini boshqarish",
    "intro": "<p>Dilnoza is fictional: an agricultural-engineering graduate from Tashkent applying as a Research Student. The official “Field of Study and Research Plan” form has its own boxes each year; this shows what a concrete plan sounds like.</p>",
    "intro_uz": "<p>Dilnoza — oʻylab topilgan qahramon: Toshkentdagi qishloq xoʻjaligi muhandisligi bitiruvchisi, tadqiqotchi talaba sifatida topshiryapti. Rasmiy «Field of Study and Research Plan» shaklining har yili oʻz kataklari boʻladi; bu yerda aniq reja qanday eshitilishi koʻrsatilgan.</p>",
    "letter": """
<h4>Research theme</h4>
<p>Estimating irrigation water demand for cotton and wheat fields in the Syrdarya region using satellite data and low-cost soil-moisture sensors.</p>
<h4>Background</h4>
<p>About 90% of Uzbekistan's water use goes to agriculture, and much of it is lost through over-irrigation. Farmers decide when to water by habit, because field measurements are expensive. During my bachelor's thesis I installed six soil-moisture sensors on a 12-hectare farm and found that fields were irrigated on average four days earlier than the crop needed.</p>
<h4>Research plan</h4>
<p>First, I will compare satellite estimates of evapotranspiration with ground sensor data from test fields. Second, I will build a model that predicts the next irrigation date from both sources. Third, I will test whether the model's advice reduces water use without lowering yield.</p>
<h4>Why Japan, and why this laboratory</h4>
<p>Professor Tanaka's laboratory has published work on combining remote sensing with field sensors in rice paddies, including a 2024 study on sensor networks that cost less than a tenth of commercial systems. I want to learn this method and adapt it to dry-land crops.</p>
<h4>After the degree</h4>
<p>I plan to return to the Ministry of Water Resources' research institute, where I worked before, and pilot the model with farmer cooperatives in Syrdarya.</p>
""",
    "notes": [
        {"para": 2, "en": "One sentence that names the <strong>place, the crop, the data and the method</strong>. A committee knows what you will do before reading further.",
         "uz": "<strong>Joy, ekin, maʼlumot va usulni</strong> nomlaydigan bitta gap. Komissiya davomini oʻqimasdan nima qilishingizni biladi."},
        {"para": 4, "en": "The problem in numbers, then <strong>her own evidence</strong> from her thesis. This is what separates a plan from a wish. <em>Check every figure you cite against a source.</em>",
         "uz": "Raqamlardagi muammo, keyin diplom ishidan <strong>oʻz dalili</strong>. Rejani orzudan ajratadigan narsa shu. <em>Keltirgan har bir raqamni manba bilan tekshiring.</em>"},
        {"para": 6, "en": "Three steps, in order, each doable. The third step tests the result — reviewers look for that.",
         "uz": "Tartibli uchta qadam, har biri bajarsa boʻladigan. Uchinchi qadam natijani sinaydi — ekspertlar aynan shuni qidiradi."},
        {"para": 8, "en": "“Why Japan” answered with a <strong>specific professor and paper</strong> — the same professor she will ask for provisional acceptance.",
         "uz": "«Nega Yaponiya» — <strong>aniq professor va maqola</strong> bilan javob. Dastlabki roziligini soʻraydigan professor ham aynan u."},
        {"para": 10, "en": "A concrete return: an institution, a region, partners. MEXT asks grantees to be bridges between the two countries.",
         "uz": "Aniq qaytish: muassasa, hudud, hamkorlar. MEXT stipendiatlardan ikki davlat oʻrtasida koʻprik boʻlishni kutadi."},
    ],
    "prompts": [
        {"en": "Your research theme in one sentence: place, object, data, method.", "uz": "Tadqiqot mavzuingiz bir gapda: joy, obyekt, maʼlumot, usul.", "lines": 3},
        {"en": "The problem, with two facts you can cite from a source.", "uz": "Muammo — manbadan keltira oladigan ikki fakt bilan.", "lines": 4},
        {"en": "What have YOU already done on it (thesis, job, data)?", "uz": "Bu borada SIZ allaqachon nima qilgansiz (diplom ishi, ish, maʼlumot)?", "lines": 3},
        {"en": "Three steps of your research, in order.", "uz": "Tadqiqotingizning uchta qadami, tartib bilan.", "lines": 4},
        {"en": "Two professors in Japan and one recent paper of each that connects to your plan.", "uz": "Yaponiyadagi ikki professor va har birining rejangizga bogʻlanadigan bitta soʻnggi maqolasi.", "lines": 4},
        {"en": "After the degree: which institution, which place, which people will use your work?", "uz": "Darajadan keyin: qaysi muassasa, qaysi joy, qaysi odamlar ishingizdan foydalanadi?", "lines": 3},
    ],
}]
