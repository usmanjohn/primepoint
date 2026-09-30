"""Study abroad — batch 1: GKS (Global Korea Scholarship), in depth.

Sources, read 2026-10-01:
  · 2027 GKS-U Application Guidelines (NIIED, posted 2026-09-09 on the Study in
    Korea GKS notice board) — eligibility, schedule, documents, evaluation,
    benefits, Uzbekistan's quota, the FAQ (TOPIK 3 after the language year).
  · 2026 GKS-G Application Guidelines (NIIED notice, 2026-02-02; embassy
    notices Feb 2026) — graduate eligibility and the February timing.
Every figure below is from those documents. Amounts "may be subject to
change" (NIIED's own words) — the page says so.

Import:
    python manage.py import_abroad abroad/management/commands/_abroad_gks.py --author=prime
"""

NOTICES = "https://www.studyinkorea.go.kr/ko/notice/scholarshipsList.do?boardSort=3"
GKS_G_2026 = "https://www.studyinkorea.go.kr/ko/plan/gksNoticeRead.do?bbsId=BBSMSTR_000000000461&nttId=4420"
CHECKED = "2026-10-01"

GKS_COVERS = """
<table>
<tr><th>Item</th><th>Amount (2027 GKS-U)</th></tr>
<tr><td>Monthly allowance — language year</td><td>13,560,000 KRW per year</td></tr>
<tr><td>Monthly allowance — degree years</td><td>14,400,000 KRW per year</td></tr>
<tr><td>Tuition</td><td>NIIED pays up to 5,000,000 KRW per year; the university covers the rest and the admission fee</td></tr>
<tr><td>Korean language programme</td><td>5,200,000 KRW per year, paid to the language institute</td></tr>
<tr><td>Flight</td><td>One economy ticket to Korea (actual cost)</td></tr>
</table>
<p>The monthly allowance is <strong>all-inclusive</strong>: living costs, housing, health insurance, the Korean-proficiency grant, the TOPIK fee, the settlement allowance and the degree-completion grant all come out of it.</p>
<div class="ab-mistake"><strong>Two traps</strong>
<p>If you withdraw within the first 3 months after enrolling, you must return <em>everything</em> you received. And the flight is not paid if you are already in Korea, or fly in from a country other than your own.</p></div>
<p class="ab-src">Source: 2027 GKS-U Application Guidelines, VII. NIIED: “The scholarship amount may be subject to change.”</p>
"""

GKS_COVERS_UZ = """
<table>
<tr><th>Nima</th><th>Miqdor (2027 GKS-U)</th></tr>
<tr><td>Oylik stipendiya — til yili</td><td>yiliga 13 560 000 von</td></tr>
<tr><td>Oylik stipendiya — oʻqish yillari</td><td>yiliga 14 400 000 von</td></tr>
<tr><td>Kontrakt (oʻqish puli)</td><td>NIIED yiliga 5 000 000 vongacha toʻlaydi; qolganini va kirish toʻlovini universitet qoplaydi</td></tr>
<tr><td>Koreys tili kursi</td><td>yiliga 5 200 000 von, til markaziga toʻlanadi</td></tr>
<tr><td>Aviabilet</td><td>Koreyaga bir tomonlama ekonom bilet (haqiqiy narxi)</td></tr>
</table>
<p>Oylik stipendiya <strong>hammasini oʻz ichiga oladi</strong>: yashash, yotoqxona, tibbiy sugʻurta, koreys tili grantlari, TOPIK toʻlovi, joylashish puli va bitiruv granti — barchasi shundan.</p>
<div class="ab-mistake"><strong>Ikki tuzoq</strong>
<p>Oʻqishga kirganingizdan keyin dastlabki 3 oy ichida voz kechsangiz, olgan <em>hamma</em> pulni qaytarasiz. Agar yakuniy natija paytida allaqachon Koreyada boʻlsangiz yoki boshqa davlatdan uchsangiz, bilet toʻlanmaydi.</p></div>
<p class="ab-src">Manba: 2027 GKS-U yoʻriqnomasi, VII boʻlim. NIIED: «Stipendiya miqdori oʻzgarishi mumkin».</p>
"""

GKS_BODY = """
<ul class="ab-toc">
<li><a href="#what">What it is</a></li><li><a href="#tracks">Tracks</a></li><li><a href="#who">Who can apply</a></li>
<li><a href="#docs">Documents</a></li><li><a href="#rounds">Selection</a></li><li><a href="#lang">Language points</a></li>
<li><a href="#year">Language year</a></li><li><a href="#master">Master's (GKS-G)</a></li><li><a href="#mistakes">Mistakes</a></li>
</ul>

<h2 id="what">What it is</h2>
<p>GKS is the Korean government's scholarship for international students, run by <strong>NIIED</strong> (National Institute for International Education). It pays for a full degree in Korea: tuition, a monthly allowance, the flight and — unless you already have TOPIK 5 or 6 — <strong>one year of Korean language study first</strong>. A bachelor's scholar is funded for 5–7 years (1 language year + 4–6 degree years).</p>
<p>There are two programmes: <strong>GKS-U</strong> for a bachelor's (applications in September) and <strong>GKS-G</strong> for a master's or PhD (applications around February).</p>

<h2 id="tracks">Embassy track or University track</h2>
<table>
<tr><th></th><th>Embassy track</th><th>University track</th></tr>
<tr><td>Where you apply</td><td>Online on studyinkorea.go.kr; the Korean Embassy in Uzbekistan runs round 1</td><td>Directly to one university, by its own method</td></tr>
<tr><td>Universities</td><td>Up to <strong>3</strong>, at least one Type B (R-GKS: up to 2, Type B only)</td><td><strong>One</strong> university, one department</td></tr>
<tr><td>2027 GKS-U places for Uzbekistan</td><td>3 — General 1, R-GKS 1, Overseas Koreans 1</td><td>Open to all countries: UIC (science &amp; engineering) and associate degrees</td></tr>
<tr><td>2027 GKS-U dates</td><td>15–30 September 2026</td><td>September–November 2026, each university's own dates</td></tr>
</table>
<div class="ab-tip"><strong>Second chance</strong><p>If you fail round 1 of the Embassy track, you may still apply through the University track in the same year — so note both sets of dates. But you can only be in <em>one</em> track and <em>one</em> programme at a time; applying twice gets you disqualified.</p></div>

<h2 id="who">Who can apply (GKS-U 2027)</h2>
<ul>
<li>Citizen of an invited country (Uzbekistan is one); neither you nor your parents may hold Korean citizenship.</li>
<li><strong>Under 25</strong> — born after 1 March 2002.</li>
<li>Finished high school, or will finish by <strong>31 December 2026</strong>. People who already have a bachelor's degree cannot apply.</li>
<li>Grades: <strong>80/100 or above</strong>, <em>or</em> top 20% of the class, <em>or</em> CGPA ≥ 2.64/4.0 (2.80/4.3, 2.91/4.5, 3.23/5.0).</li>
<li>Not graduated from a Korean high school, and never had a Korean-government degree scholarship before.</li>
</ul>
<div class="ab-uz"><strong>Uzbek grades</strong><p>Our school scale is 5-point, which is not on NIIED's list. If your transcript does not show one of the accepted scales, the guideline asks for an <strong>official conversion from your school</strong> (signed and stamped) — without it your grades “cannot be evaluated”. Ask your school early.</p></div>

<h2 id="docs">Documents</h2>
<p>Seven NIIED forms, filled in on the website: <strong>(1)</strong> Application Form — in English; <strong>(2)</strong> Personal Statement and <strong>(3)</strong> Study Plan — English or Korean; <strong>(4)</strong> Recommendation Letter — from a teacher or principal, dated within one year (one is required, two are accepted); <strong>(5)</strong> Applicant Agreement; <strong>(6)</strong> Personal Medical Assessment; <strong>(7)</strong> Consent to use personal information.</p>
<p>Certificates, <strong>apostilled</strong>: proof of citizenship and family relationship for you and your parents (birth certificate), high-school graduation certificate (or certificate of expected graduation) and transcript. A document in Uzbek or Russian needs a certified translation, and the apostille goes on the original or on the translation. Optional but valuable: a TOPIK or IELTS/TOEFL report, and up to five certificates of awards or activities.</p>
<p>In round 1 you only upload scans. If you pass it, the originals go to the Embassy by its deadline — so start the apostille <em>before</em> you apply, not after.</p>
<div class="ab-tip"><strong>The name rule</strong><p>Your English name must match your passport letter for letter, on every form. A mismatch delays the visa.</p></div>

<h2 id="rounds">Selection, round by round (Embassy track, 2027 GKS-U)</h2>
<ol class="ab-steps">
<li><strong>Round 1 — Embassy</strong>: documents and an interview. Results by 16 October 2026.</li>
<li><strong>Round 2 — NIIED</strong>: the Embassy's nominees are reviewed. Results in November.</li>
<li><strong>Round 3 — Universities</strong>: the universities you chose review you. Results by 23 December; you pick your final university by 29 December.</li>
<li><strong>Final list</strong>: expected 7 January 2027 on studyinkorea.go.kr. Invitation letters follow in January.</li>
</ol>
<p>NIIED does not message you at each stage — checking the notice board and “My Page” is your job.</p>
<div class="ab-fact"><strong>Choose universities wisely</strong><p>The guidelines warn that if many applicants pick the same famous universities, you can pass NIIED and still be rejected by all three in round 3. A strong Type B choice is not a “backup” — it is often where scholars are actually placed.</p></div>

<h2 id="lang">What your language certificate is worth</h2>
<p>Korean and English are scored separately; your best report counts.</p>
<table>
<tr><th>Share of the language score</th><th>TOPIK</th><th>IELTS</th></tr>
<tr><td>100%</td><td>Level 5–6</td><td>—</td></tr>
<tr><td>90%</td><td>Level 4</td><td>8.0+</td></tr>
<tr><td>80%</td><td>Level 3</td><td>7.0+</td></tr>
<tr><td>70%</td><td>Level 2</td><td>6.0+</td></tr>
<tr><td>60%</td><td>Level 1</td><td>5.0+</td></tr>
<tr><td>50%</td><td colspan="2">No certificate</td></tr>
</table>
<p>On top of that, TOPIK 3 adds <strong>+3%</strong> of the total score, TOPIK 4 <strong>+4%</strong>, TOPIK 5–6 <strong>+5%</strong>; applying to a science or engineering department adds <strong>+5%</strong>.</p>
<div class="ab-uz"><strong>What this means for you</strong><p>TOPIK 3 earns the same share as IELTS 7.0 — <em>and</em> bonus points IELTS cannot earn. For most pupils TOPIK 3 is much closer than IELTS 7. <a href="/tutorials/">Prime Korean</a> and the TOPIK exam prep on Powerty are built for exactly this.</p></div>
<p class="ab-src">For 2027 GKS-U, TOPIK PBT 96th–109th and IBT 4th–16th are valid.</p>

<h2 id="year">The language year</h2>
<p>Unless you arrive with TOPIK 5 or 6, you spend the first year learning Korean at a language institute. <strong>By the end of that year you must reach at least TOPIK 3</strong> to start your degree; some departments demand TOPIK 4. Scholars who reach TOPIK 5 or 6 within the first six months skip the rest and start the degree the next semester.</p>

<h2 id="master">Master's and PhD: GKS-G</h2>
<p>Same structure, different dates and limits. In the 2026 cycle the guidelines were posted on 2 February 2026 and Embassy-track online applications ran from <strong>12 to 25 February 2026</strong>; University-track dates were set by each university (for example, 9 February – 31 March at one national university). Eligibility in 2026: <strong>under 40</strong> (born after 1 September 1986), a bachelor's degree (or expected), and the same 80% / top-20% / CGPA rule. Recommendations come from professors or department heads. A master's scholarship is normally 3 years: 1 language year + 2 degree years.</p>
<p>The 2027 GKS-G guidelines are expected around February 2027 — the date on this page is an estimate until they appear.</p>

<h2 id="mistakes">The mistakes that sink applications</h2>
<ul>
<li><strong>Starting the apostille after round 1.</strong> It takes weeks; the original deadline does not wait.</li>
<li><strong>A department name that is not in the “University Information” file.</strong> You may only apply to listed departments, with their exact names.</li>
<li><strong>A generic personal statement.</strong> “I love Korean culture and K-dramas” is what hundreds write. Say what <em>you</em> did and what you will study.</li>
<li><strong>A study plan with no plan.</strong> It must say what you will do in the language year, in each degree year, and after graduating.</li>
<li><strong>Applying twice</strong> — two tracks, or two programmes. Disqualification.</li>
<li><strong>Waiting for an email.</strong> Results are posted, not sent.</li>
</ul>
<p class="ab-src">Sources: NIIED, 2027 GKS-U Application Guidelines (Sept 2026); 2026 GKS-G Application Guidelines (Feb 2026); Study in Korea GKS notices.</p>
"""

GKS_BODY_UZ = """
<ul class="ab-toc">
<li><a href="#what">Bu nima</a></li><li><a href="#tracks">Yoʻllar</a></li><li><a href="#who">Kim topshira oladi</a></li>
<li><a href="#docs">Hujjatlar</a></li><li><a href="#rounds">Tanlov</a></li><li><a href="#lang">Til ballari</a></li>
<li><a href="#year">Til yili</a></li><li><a href="#master">Magistratura (GKS-G)</a></li><li><a href="#mistakes">Xatolar</a></li>
</ul>

<h2 id="what">Bu nima</h2>
<p>GKS — Koreya hukumatining xorijlik talabalar uchun stipendiyasi. Uni <strong>NIIED</strong> (Xalqaro taʼlim milliy instituti) boshqaradi. U Koreyada toʻliq oʻqishni qoplaydi: kontrakt, oylik stipendiya, aviabilet va — agar sizda TOPIK 5 yoki 6 boʻlmasa — <strong>avval bir yillik koreys tili kursi</strong>. Bakalavr stipendiyasi 5–7 yilga beriladi (1 til yili + 4–6 oʻqish yili).</p>
<p>Ikki dastur bor: bakalavr uchun <strong>GKS-U</strong> (arizalar sentabrda) va magistratura yoki doktorantura uchun <strong>GKS-G</strong> (arizalar taxminan fevralda).</p>

<h2 id="tracks">Elchixona yoʻli yoki universitet yoʻli</h2>
<table>
<tr><th></th><th>Elchixona yoʻli</th><th>Universitet yoʻli</th></tr>
<tr><td>Qayerga topshirasiz</td><td>studyinkorea.go.kr saytida onlayn; 1-bosqichni Koreyaning Oʻzbekistondagi elchixonasi oʻtkazadi</td><td>Toʻgʻridan-toʻgʻri bitta universitetga, uning oʻz tartibida</td></tr>
<tr><td>Universitetlar</td><td><strong>3</strong> tagacha, kamida bittasi Type B (R-GKS: 2 tagacha, faqat Type B)</td><td><strong>Bitta</strong> universitet, bitta yoʻnalish</td></tr>
<tr><td>2027 GKS-U: Oʻzbekiston uchun oʻrinlar</td><td>3 ta — General 1, R-GKS 1, xorijdagi koreyslar 1</td><td>Barcha davlatlarga ochiq: UIC (fan va muhandislik) va kollej (associate) darajasi</td></tr>
<tr><td>2027 GKS-U sanalari</td><td>2026-yil 15–30 sentabr</td><td>2026-yil sentabr–noyabr, har bir universitetning oʻz sanalari</td></tr>
</table>
<div class="ab-tip"><strong>Ikkinchi imkoniyat</strong><p>Elchixona yoʻlining 1-bosqichidan oʻtolmasangiz, oʻsha yili universitet yoʻli orqali ham topshira olasiz — shuning uchun ikkala sanani ham yozib qoʻying. Lekin bir vaqtda faqat <em>bitta</em> yoʻl va <em>bitta</em> dasturda boʻlish mumkin; ikki marta topshirgan chetlashtiriladi.</p></div>

<h2 id="who">Kim topshira oladi (GKS-U 2027)</h2>
<ul>
<li>Taklif qilingan davlat fuqarosi (Oʻzbekiston shular qatorida); siz ham, ota-onangiz ham Koreya fuqaroligiga ega boʻlmasligi kerak.</li>
<li><strong>25 yoshdan kichik</strong> — 2002-yil 1-martdan keyin tugʻilgan.</li>
<li>Maktabni tugatgan yoki <strong>2026-yil 31-dekabrgacha</strong> tugatadi. Bakalavr diplomi borlar topshira olmaydi.</li>
<li>Baholar: <strong>100 ballikda 80 va undan yuqori</strong>, <em>yoki</em> sinfning eng yaxshi 20 foizi, <em>yoki</em> CGPA ≥ 2,64/4,0 (2,80/4,3; 2,91/4,5; 3,23/5,0).</li>
<li>Koreyadagi maktabni tugatmagan va ilgari Koreya hukumatining oʻqish stipendiyasini olmagan.</li>
</ul>
<div class="ab-uz"><strong>Oʻzbek baholari</strong><p>Bizdagi 5 ballik tizim NIIED roʻyxatida yoʻq. Agar tabelingizda qabul qilinadigan shkalalardan biri boʻlmasa, yoʻriqnoma <strong>maktabingizdan rasmiy qayta hisob</strong> (imzo va muhr bilan) talab qiladi — usiz baholaringiz «baholanmaydi». Buni maktabdan oldinroq soʻrang.</p></div>

<h2 id="docs">Hujjatlar</h2>
<p>Saytda toʻldiriladigan yettita NIIED shakli: <strong>(1)</strong> Ariza shakli — ingliz tilida; <strong>(2)</strong> Shaxsiy bayonot (Personal Statement) va <strong>(3)</strong> Oʻqish rejasi (Study Plan) — ingliz yoki koreys tilida; <strong>(4)</strong> Tavsiyanoma — oʻqituvchi yoki direktordan, bir yil ichidagi sana bilan (bittasi shart, ikkitasi qabul qilinadi); <strong>(5)</strong> Nomzod kelishuvi; <strong>(6)</strong> Tibbiy baholash; <strong>(7)</strong> Shaxsiy maʼlumotlardan foydalanishga rozilik.</p>
<p><strong>Apostil qoʻyilgan</strong> guvohnomalar: siz va ota-onangizning fuqaroligi va qarindoshlikni tasdiqlovchi hujjat (tugʻilganlik haqida guvohnoma), maktabni tugatganlik haqidagi hujjat (attestat yoki tugatishi kutilayotgani haqida maʼlumotnoma) va baholar varaqasi. Oʻzbek yoki rus tilidagi hujjatga tasdiqlangan tarjima kerak, apostil esa asl nusxaga yoki tarjimaga qoʻyiladi. Majburiy emas, lekin qimmatli: TOPIK yoki IELTS/TOEFL natijasi va mukofot yoki faoliyat haqidagi 5 tagacha sertifikat.</p>
<p>1-bosqichda faqat skanlar yuklanadi. Undan oʻtsangiz, asl nusxalar elchixonaga uning muddatida topshiriladi — shuning uchun apostilni ariza berishdan <em>oldin</em> boshlang, keyin emas.</p>
<div class="ab-tip"><strong>Ism qoidasi</strong><p>Inglizcha ismingiz har bir shaklda pasportdagidek, harfma-harf boʻlishi kerak. Farq boʻlsa, viza kechikadi.</p></div>

<h2 id="rounds">Tanlov bosqichma-bosqich (elchixona yoʻli, 2027 GKS-U)</h2>
<ol class="ab-steps">
<li><strong>1-bosqich — elchixona</strong>: hujjatlar va suhbat. Natijalar 2026-yil 16-oktabrgacha.</li>
<li><strong>2-bosqich — NIIED</strong>: elchixona tavsiya qilganlar koʻriladi. Natijalar noyabrda.</li>
<li><strong>3-bosqich — universitetlar</strong>: siz tanlagan universitetlar koʻrib chiqadi. Natijalar 23-dekabrgacha; yakuniy universitetni 29-dekabrgacha tanlaysiz.</li>
<li><strong>Yakuniy roʻyxat</strong>: 2027-yil 7-yanvar kutilmoqda, studyinkorea.go.kr saytida. Taklifnomalar yanvarda keladi.</li>
</ol>
<p>NIIED har bosqichda sizga xabar yubormaydi — eʼlonlar sahifasi va «My Page»ni tekshirib turish sizning vazifangiz.</p>
<div class="ab-fact"><strong>Universitetlarni oʻylab tanlang</strong><p>Yoʻriqnoma ogohlantiradi: agar koʻp nomzod bir xil mashhur universitetlarni tanlasa, NIIED bosqichidan oʻtib ham 3-bosqichda uchalasidan rad javobi olish mumkin. Kuchli Type B tanlovi «zaxira» emas — koʻpincha stipendiatlar aynan shu yerga joylashadi.</p></div>

<h2 id="lang">Til sertifikatingiz qancha turadi</h2>
<p>Koreys va ingliz tili alohida baholanadi; eng yaxshi natijangiz hisobga olinadi.</p>
<table>
<tr><th>Til balining ulushi</th><th>TOPIK</th><th>IELTS</th></tr>
<tr><td>100%</td><td>5–6-daraja</td><td>—</td></tr>
<tr><td>90%</td><td>4-daraja</td><td>8,0+</td></tr>
<tr><td>80%</td><td>3-daraja</td><td>7,0+</td></tr>
<tr><td>70%</td><td>2-daraja</td><td>6,0+</td></tr>
<tr><td>60%</td><td>1-daraja</td><td>5,0+</td></tr>
<tr><td>50%</td><td colspan="2">Sertifikat yoʻq</td></tr>
</table>
<p>Bundan tashqari TOPIK 3 umumiy balga <strong>+3%</strong>, TOPIK 4 <strong>+4%</strong>, TOPIK 5–6 <strong>+5%</strong> qoʻshadi; fan yoki muhandislik yoʻnalishiga topshirish <strong>+5%</strong> beradi.</p>
<div class="ab-uz"><strong>Bu siz uchun nimani anglatadi</strong><p>TOPIK 3 IELTS 7,0 bilan bir xil ulush beradi — <em>va</em> IELTS bera olmaydigan qoʻshimcha balni ham. Koʻpchilik oʻquvchi uchun TOPIK 3 IELTS 7 dan ancha yaqin. Powerty'dagi <a href="/tutorials/">Prime Korean</a> va TOPIK tayyorlovi aynan shu uchun qurilgan.</p></div>
<p class="ab-src">2027 GKS-U uchun TOPIK PBT 96–109 va IBT 4–16 imtihonlari amal qiladi.</p>

<h2 id="year">Til yili</h2>
<p>TOPIK 5 yoki 6 bilan kelmasangiz, birinchi yil til markazida koreys tilini oʻrganasiz. <strong>Shu yil oxirigacha kamida TOPIK 3 olishingiz shart</strong>, aks holda oʻqishni boshlay olmaysiz; baʼzi yoʻnalishlar TOPIK 4 talab qiladi. Dastlabki olti oyda TOPIK 5 yoki 6 olganlar qolgan qismni oʻtkazib, keyingi semestrdan oʻqishni boshlaydi.</p>

<h2 id="master">Magistratura va doktorantura: GKS-G</h2>
<p>Tuzilishi bir xil, sanalari va chegaralari boshqa. 2026-yilgi tsiklda yoʻriqnoma 2026-yil 2-fevralda eʼlon qilindi, elchixona yoʻlida onlayn ariza <strong>2026-yil 12–25 fevral</strong> kunlari qabul qilindi; universitet yoʻlida sanalarni har bir universitet oʻzi belgiladi (masalan, bir davlat universitetida 9-fevral – 31-mart). 2026-yilgi shartlar: <strong>40 yoshdan kichik</strong> (1986-yil 1-sentabrdan keyin tugʻilgan), bakalavr diplomi (yoki tugatish arafasida) va oʻsha 80% / eng yaxshi 20% / CGPA qoidasi. Tavsiyanomalar professor yoki kafedra mudiridan olinadi. Magistratura stipendiyasi odatda 3 yil: 1 til yili + 2 oʻqish yili.</p>
<p>2027 GKS-G yoʻriqnomasi 2027-yil fevral atrofida kutilmoqda — u chiqquncha bu sahifadagi sana taxminiy.</p>

<h2 id="mistakes">Arizani yiqitadigan xatolar</h2>
<ul>
<li><strong>Apostilni 1-bosqichdan keyin boshlash.</strong> U haftalab vaqt oladi, asl nusxa muddati esa kutmaydi.</li>
<li><strong>«University Information» faylida yoʻq yoʻnalish nomi.</strong> Faqat roʻyxatdagi yoʻnalishlarga, aynan oʻsha nom bilan topshirish mumkin.</li>
<li><strong>Umumiy gaplardan iborat shaxsiy bayonot.</strong> «Koreya madaniyati va doramalarni yaxshi koʻraman» — yuzlab odam shunday yozadi. <em>Siz</em> nima qilganingizni va nimani oʻqishingizni yozing.</li>
<li><strong>Rejasiz oʻqish rejasi.</strong> Unda til yilida, har bir oʻqish yilida va bitirgandan keyin nima qilishingiz yozilishi kerak.</li>
<li><strong>Ikki marta topshirish</strong> — ikki yoʻl yoki ikki dastur. Chetlashtirish.</li>
<li><strong>Xat kutib oʻtirish.</strong> Natijalar eʼlon qilinadi, yuborilmaydi.</li>
</ul>
<p class="ab-src">Manbalar: NIIED, 2027 GKS-U yoʻriqnomasi (2026-yil sentabr); 2026 GKS-G yoʻriqnomasi (2026-yil fevral); Study in Korea GKS eʼlonlari.</p>
"""

SCHOLARSHIPS = [
    {
        "slug": "gks", "order": 1, "name": "GKS",
        "full_name": "Global Korea Scholarship (formerly KGSP)",
        "country": "South Korea", "country_uz": "Janubiy Koreya", "flag": "🇰🇷",
        "depth": "full", "levels": "bachelor,master,phd", "languages": "korean,english,any",
        "fully_funded": True,
        "summary": "The Korean government pays for your whole degree plus a year of Korean first. Bachelor's applications in September, master's around February.",
        "summary_uz": "Koreya hukumati butun oʻqishingizni va undan oldin bir yillik koreys tilini toʻlaydi. Bakalavrga arizalar sentabrda, magistraturaga taxminan fevralda.",
        "covers": GKS_COVERS, "covers_uz": GKS_COVERS_UZ,
        "usual_period": "Bachelor: September · Master/PhD: February–March",
        "usual_period_uz": "Bakalavr: sentabr · Magistratura/PhD: fevral–mart",
        "body": GKS_BODY, "body_uz": GKS_BODY_UZ,
        "official_url": "https://www.studyinkorea.go.kr/",
        "last_checked": CHECKED,
    },
]

DEADLINES = [
    {
        "scholarship": "gks",
        "label": "GKS-U 2027 — Embassy track", "label_uz": "GKS-U 2027 — elchixona yoʻli",
        "opens": "2026-09-15", "closes": "2026-09-30",
        "note": "Closed 30 Sep, 18:00 KST. Round 1 results by 16 October; final list expected 7 January 2027.",
        "note_uz": "30-sentabr, 18:00 (Koreya vaqti) da yopildi. 1-bosqich natijalari 16-oktabrgacha; yakuniy roʻyxat 2027-yil 7-yanvarda kutilmoqda.",
        "source_url": NOTICES, "last_checked": CHECKED,
    },
    {
        "scholarship": "gks",
        "label": "GKS-U 2027 — University track", "label_uz": "GKS-U 2027 — universitet yoʻli",
        "opens": "2026-09-01", "closes": "2026-11-30",
        "note": "Each university sets its own deadline between September and November — many close earlier than 30 November. Check the university's own GKS announcement.",
        "note_uz": "Har bir universitet oʻz muddatini sentabr–noyabr oraligʻida belgilaydi — koʻplari 30-noyabrdan oldin yopiladi. Universitetning oʻz GKS eʼlonini tekshiring.",
        "source_url": NOTICES, "last_checked": CHECKED,
    },
    {
        "scholarship": "gks",
        "label": "GKS-G 2027 — Embassy track", "label_uz": "GKS-G 2027 — elchixona yoʻli",
        "opens": None, "closes": "2027-02-25", "is_estimate": True,
        "note": "Estimate from the 2026 cycle (online 12–25 February 2026). The 2027 guidelines are expected around February 2027.",
        "note_uz": "2026-yilgi tsikl asosida taxmin (onlayn 2026-yil 12–25 fevral). 2027 yoʻriqnomasi 2027-yil fevral atrofida kutilmoqda.",
        "source_url": GKS_G_2026, "last_checked": CHECKED,
    },
]

# From the Type A / Type B lists in the 2027 GKS-U guidelines (II.4). KAIST is
# not on the GKS-U list, so it is not here — only listed universities are.
UNIVERSITIES = [
    {"name": "Seoul National University", "name_local": "서울대학교", "city": "Seoul", "country": "South Korea",
     "url": "https://en.snu.ac.kr/", "gks_university_track": False,
     "strengths": "GKS-U Type A. National university with almost every field.",
     "strengths_uz": "GKS-U Type A. Deyarli barcha yoʻnalishlari bor davlat universiteti."},
    {"name": "Yonsei University", "name_local": "연세대학교", "city": "Seoul", "country": "South Korea",
     "url": "https://www.yonsei.ac.kr/en_sc/", "gks_university_track": False,
     "strengths": "GKS-U Type A. Large private university; its Korean Language Institute is one of the oldest.",
     "strengths_uz": "GKS-U Type A. Katta xususiy universitet; koreys tili instituti eng qadimiylaridan."},
    {"name": "Korea University", "name_local": "고려대학교", "city": "Seoul", "country": "South Korea",
     "url": "https://www.korea.edu/", "gks_university_track": False,
     "strengths": "GKS-U Type A. Large private university, strong in business, law and engineering.",
     "strengths_uz": "GKS-U Type A. Katta xususiy universitet; biznes, huquq va muhandislik kuchli."},
    {"name": "Sungkyunkwan University", "name_local": "성균관대학교", "city": "Seoul / Suwon", "country": "South Korea",
     "url": "https://www.skku.edu/eng/", "gks_university_track": False,
     "strengths": "GKS-U Type A. Humanities in Seoul, science and engineering in Suwon.",
     "strengths_uz": "GKS-U Type A. Gumanitar fanlar Seulda, fan va muhandislik Suvonda."},
    {"name": "Hanyang University", "name_local": "한양대학교", "city": "Seoul", "country": "South Korea",
     "url": "https://www.hanyang.ac.kr/web/eng", "gks_university_track": False,
     "strengths": "GKS-U Type A. Known above all for engineering.",
     "strengths_uz": "GKS-U Type A. Avvalo muhandisligi bilan mashhur."},
    {"name": "POSTECH", "name_local": "포항공과대학교", "city": "Pohang", "country": "South Korea",
     "url": "https://www.postech.ac.kr/eng/", "gks_university_track": False,
     "strengths": "GKS-U Type A. Small research university of science and technology.",
     "strengths_uz": "GKS-U Type A. Kichik, tadqiqotga yoʻnaltirilgan fan va texnologiya universiteti."},
    {"name": "UNIST", "name_local": "울산과학기술원", "city": "Ulsan", "country": "South Korea",
     "url": "https://www.unist.ac.kr/", "gks_university_track": False,
     "strengths": "GKS-U Type A. Science and technology institute; many courses taught in English.",
     "strengths_uz": "GKS-U Type A. Fan va texnologiya instituti; koʻp darslar ingliz tilida."},
    {"name": "Kyung Hee University", "name_local": "경희대학교", "city": "Seoul", "country": "South Korea",
     "url": "https://www.khu.ac.kr/eng/main/index.do", "gks_university_track": False,
     "strengths": "GKS-U Type A. Broad private university with a large international community.",
     "strengths_uz": "GKS-U Type A. Keng yoʻnalishli xususiy universitet, xorijlik talabalar koʻp."},
    {"name": "Ewha Womans University", "name_local": "이화여자대학교", "city": "Seoul", "country": "South Korea",
     "url": "https://www.ewha.ac.kr/ewhaen/index.do", "gks_university_track": False,
     "strengths": "GKS-U Type A. Women's university — applicants must be women.",
     "strengths_uz": "GKS-U Type A. Ayollar universiteti — faqat qizlar topshiradi."},
    {"name": "Sogang University", "name_local": "서강대학교", "city": "Seoul", "country": "South Korea",
     "url": "https://www.sogang.ac.kr/en/home", "gks_university_track": False,
     "strengths": "GKS-U Type A. Compact private university in central Seoul.",
     "strengths_uz": "GKS-U Type A. Seul markazidagi ixcham xususiy universitet."},
    {"name": "Hankuk University of Foreign Studies", "name_local": "한국외국어대학교", "city": "Seoul", "country": "South Korea",
     "url": "https://www.hufs.ac.kr/sites/hufs-eng/index.do", "gks_university_track": False,
     "strengths": "GKS-U Type A. Languages, international relations and area studies.",
     "strengths_uz": "GKS-U Type A. Tillar, xalqaro munosabatlar va mintaqashunoslik."},
    {"name": "Inha University", "name_local": "인하대학교", "city": "Incheon", "country": "South Korea",
     "url": "https://www.inha.ac.kr/sites/eng/index.do", "gks_university_track": False,
     "strengths": "GKS-U Type A. Engineering-focused; Tashkent has an Inha branch, so the name is familiar here.",
     "strengths_uz": "GKS-U Type A. Muhandislikka yoʻnalgan; Toshkentda Inha filiali bor, shuning uchun nomi tanish."},
    {"name": "Ajou University", "name_local": "아주대학교", "city": "Suwon", "country": "South Korea",
     "url": "https://www.ajou.ac.kr/en/index.do", "gks_university_track": True,
     "strengths": "GKS-U Type A, and in 2027 also a University-track (UIC) school for AI and computer engineering.",
     "strengths_uz": "GKS-U Type A; 2027-yilda sunʼiy intellekt va kompyuter muhandisligi boʻyicha universitet yoʻli (UIC) ham bor."},
    {"name": "Pusan National University", "name_local": "부산대학교", "city": "Busan", "country": "South Korea",
     "url": "https://www.pusan.ac.kr/eng/Main.do", "gks_university_track": False,
     "strengths": "GKS-U Type B. Large national university in Korea's second city.",
     "strengths_uz": "GKS-U Type B. Koreyaning ikkinchi shahridagi katta davlat universiteti."},
    {"name": "Kyungpook National University", "name_local": "경북대학교", "city": "Daegu", "country": "South Korea",
     "url": "https://en.knu.ac.kr/", "gks_university_track": False,
     "strengths": "GKS-U Type B. Large national university in Daegu.",
     "strengths_uz": "GKS-U Type B. Tegudagi katta davlat universiteti."},
    {"name": "Chonnam National University", "name_local": "전남대학교", "city": "Gwangju", "country": "South Korea",
     "url": "https://global.jnu.ac.kr/", "gks_university_track": False,
     "strengths": "GKS-U Type B. National university in Gwangju.",
     "strengths_uz": "GKS-U Type B. Kvanjudagi davlat universiteti."},
    {"name": "Chungnam National University", "name_local": "충남대학교", "city": "Daejeon", "country": "South Korea",
     "url": "https://plus.cnu.ac.kr/html/en/", "gks_university_track": False,
     "strengths": "GKS-U Type B. National university in Daejeon, Korea's science city.",
     "strengths_uz": "GKS-U Type B. Koreyaning «fan shahri» Tejondagi davlat universiteti."},
    {"name": "Keimyung University", "name_local": "계명대학교", "city": "Daegu", "country": "South Korea",
     "url": "https://www.kmu.ac.kr/uni/eng/main.jsp", "gks_university_track": True,
     "strengths": "GKS-U Type B, and in 2027 a UIC school (mechanical engineering). Home of the textbook our Keimyung readings follow.",
     "strengths_uz": "GKS-U Type B; 2027-yilda UIC (mexanika muhandisligi) ham bor. Burchakdagi Keimyung oʻqish matnlari shu universitet darsligiga tayanadi."},
]

CHECKLISTS = {
    "gks-u": [
        {"text": "Passport — the English name on every form matches it exactly", "text_uz": "Pasport — har bir shakldagi inglizcha ism unga aynan mos",
         "hint": "A mismatch delays the visa.", "hint_uz": "Farq boʻlsa, viza kechikadi."},
        {"text": "Grades checked: 80/100, top 20%, or CGPA 2.64/4.0 — and a school-stamped conversion if needed",
         "text_uz": "Baholar tekshirildi: 80/100, eng yaxshi 20% yoki CGPA 2,64/4,0 — kerak boʻlsa maktab muhri bilan qayta hisob",
         "hint": "Uzbek 5-point grades are not on NIIED's list.", "hint_uz": "Oʻzbekcha 5 ballik tizim NIIED roʻyxatida yoʻq."},
        {"text": "Universities and departments chosen from this year's “University Information” file (up to 3, at least 1 Type B)",
         "text_uz": "Universitet va yoʻnalishlar shu yilgi «University Information» faylidan tanlandi (3 tagacha, kamida 1 ta Type B)"},
        {"text": "Birth certificate (citizenship and parents) — translated and apostilled",
         "text_uz": "Tugʻilganlik haqida guvohnoma (fuqarolik va ota-ona) — tarjima va apostil"},
        {"text": "High-school graduation certificate (attestat) or certificate of expected graduation — translated and apostilled",
         "text_uz": "Attestat yoki tugatish arafasida ekanlik haqida maʼlumotnoma — tarjima va apostil"},
        {"text": "High-school transcript — translated and apostilled",
         "text_uz": "Baholar varaqasi (tabel) — tarjima va apostil",
         "hint": "Apostille for education documents is requested on my.gov.uz; it takes weeks.",
         "hint_uz": "Taʼlim hujjatlariga apostil my.gov.uz orqali soʻraladi; haftalab vaqt oladi."},
        {"text": "Form 2 — Personal Statement (English or Korean)", "text_uz": "2-shakl — Shaxsiy bayonot (ingliz yoki koreys tilida)"},
        {"text": "Form 3 — Study Plan (English or Korean)", "text_uz": "3-shakl — Oʻqish rejasi (ingliz yoki koreys tilida)"},
        {"text": "Form 4 — Recommendation letter from a teacher or principal, dated within a year",
         "text_uz": "4-shakl — oʻqituvchi yoki direktordan tavsiyanoma, bir yil ichidagi sana bilan"},
        {"text": "Forms 1, 5, 6, 7 — application, agreement, medical assessment, consent (signed)",
         "text_uz": "1, 5, 6, 7-shakllar — ariza, kelishuv, tibbiy baholash, rozilik (imzolangan)"},
        {"text": "TOPIK or IELTS/TOEFL report (optional — but worth points)",
         "text_uz": "TOPIK yoki IELTS/TOEFL natijasi (majburiy emas — lekin ball beradi)"},
        {"text": "Up to 5 certificates of awards or activities (optional)",
         "text_uz": "Mukofot yoki faoliyat haqidagi 5 tagacha sertifikat (majburiy emas)"},
        {"text": "Everything uploaded on studyinkorea.go.kr before the deadline — then originals ready for round 2",
         "text_uz": "Hammasi muddatgacha studyinkorea.go.kr ga yuklandi — asl nusxalar 2-bosqichga tayyor"},
    ],
    "gks-g": [
        {"text": "Passport — English name matches every form", "text_uz": "Pasport — inglizcha ism har bir shaklga mos"},
        {"text": "Bachelor's diploma (or certificate of expected graduation) — translated and apostilled",
         "text_uz": "Bakalavr diplomi (yoki tugatish arafasida ekanlik haqida maʼlumotnoma) — tarjima va apostil"},
        {"text": "University transcript with CGPA — translated and apostilled",
         "text_uz": "CGPA koʻrsatilgan universitet transkripti — tarjima va apostil"},
        {"text": "Birth certificate (citizenship and parents) — translated and apostilled",
         "text_uz": "Tugʻilganlik haqida guvohnoma — tarjima va apostil"},
        {"text": "Department chosen from the “University Information” file; professor's research read",
         "text_uz": "Yoʻnalish «University Information» faylidan tanlandi; professorning ishlari oʻqildi"},
        {"text": "Personal Statement and Study Plan (research-focused)", "text_uz": "Shaxsiy bayonot va oʻqish rejasi (tadqiqotga yoʻnalgan)"},
        {"text": "Recommendation letter(s) from professors — check this year's form for how many",
         "text_uz": "Professorlardan tavsiyanoma(lar) — nechta kerakligini shu yilgi shakldan tekshiring"},
        {"text": "TOPIK or IELTS/TOEFL report", "text_uz": "TOPIK yoki IELTS/TOEFL natijasi"},
        {"text": "Publications, awards, certificates (optional)", "text_uz": "Maqolalar, mukofotlar, sertifikatlar (majburiy emas)"},
        {"text": "Signed forms and one original set + copies as the guidelines ask",
         "text_uz": "Imzolangan shakllar va yoʻriqnoma soʻragan asl nusxa + nusxalar"},
    ],
    "general": [
        {"text": "Valid passport (at least 6 months beyond your planned arrival)", "text_uz": "Amal qiluvchi pasport (kelish sanasidan kamida 6 oy ortiq)"},
        {"text": "Language certificate: IELTS / TOEFL / TOPIK / JLPT — as the university asks",
         "text_uz": "Til sertifikati: IELTS / TOEFL / TOPIK / JLPT — universitet talabiga koʻra"},
        {"text": "School certificate (attestat) or diploma + transcript", "text_uz": "Attestat yoki diplom + baholar varaqasi"},
        {"text": "Certified translations and apostille", "text_uz": "Tasdiqlangan tarjimalar va apostil"},
        {"text": "Motivation letter / personal statement", "text_uz": "Motivatsion xat / shaxsiy bayonot"},
        {"text": "Two recommendation letters", "text_uz": "Ikkita tavsiyanoma"},
        {"text": "CV (for master's and most scholarships)", "text_uz": "CV (magistratura va koʻp stipendiyalar uchun)"},
        {"text": "Proof of funds or scholarship letter (for the visa)", "text_uz": "Mablagʻ borligini tasdiqlovchi hujjat yoki stipendiya xati (viza uchun)"},
        {"text": "Passport photos to the required size", "text_uz": "Talab qilingan oʻlchamdagi fotosuratlar"},
        {"text": "Medical certificate if required", "text_uz": "Kerak boʻlsa, tibbiy maʼlumotnoma"},
    ],
}

SAMPLES = [
    {
        "slug": "gks-personal-statement", "order": 1, "kind": "statement", "scholarship": "gks",
        "title": "GKS-U personal statement — Madina, applying for computer science",
        "title_uz": "GKS-U shaxsiy bayonoti — Madina, kompyuter fanlariga",
        "intro": "<p>Madina is fictional: a school-leaver from Samarkand applying to a computer-science department through the Embassy track. The official Form 2 has its own headings each year — follow them; what matters here is <em>how</em> each paragraph earns its place.</p>",
        "intro_uz": "<p>Madina — oʻylab topilgan qahramon: Samarqanddagi bitiruvchi, elchixona yoʻli orqali kompyuter fanlari yoʻnalishiga topshiryapti. Rasmiy 2-shaklning har yili oʻz sarlavhalari boʻladi — ularga amal qiling; bu yerda muhimi — har bir xatboshi oʻz oʻrnini <em>qanday</em> oqlashi.</p>",
        "letter": """
<p>The first program I ever wrote did not work. I was fourteen, and I wanted our school's paper timetable to become a phone app so my classmates would stop photographing the notice board. It took me three weeks to understand why every lesson appeared on Monday. When it finally worked, sixty students used it every morning, and I understood what I want to do with my life: build small tools that remove small frustrations for many people.</p>
<p>Since then I have taught myself Python and web development from free online courses, mostly at night after homework. In Year 10 I led a team of four in the regional informatics olympiad and we placed second. More useful than the medal was what I learned about working in a team: I wrote less code than before, and spent more time explaining it.</p>
<p>I am applying to Korea because of what I saw in its classrooms, not on its screens. Two years ago I joined an online Korean course, and our teacher showed us how Korean schools use digital textbooks. Korea turned into one of the most connected countries in the world within one generation. I want to study how software helped do that, in the place where it happened.</p>
<p>I am not starting from zero. I passed TOPIK level 2 this year, and I study Korean for an hour every day. I know the language year will be hard; I am ready for it, because I have already seen how much a language opens.</p>
<p>My mother is a primary-school teacher, and many of her colleagues still copy marks into paper journals by hand. After my degree I want to return to Uzbekistan and build simple, reliable software for schools like hers. I believe the best thing I can bring back from Korea is not only knowledge, but the habit of making technology serve ordinary people.</p>
""",
        "notes": [
            {"para": 1, "en": "Opens with a <strong>specific moment</strong>, not “Since childhood I have loved computers”. The detail (every lesson on Monday) proves it really happened.",
             "uz": "<strong>Aniq bir lahza</strong> bilan boshlanadi, «Bolaligimdan kompyuterni yaxshi koʻraman» bilan emas. Tafsilot (hamma dars dushanbaga tushgani) bu haqiqatan boʻlganini isbotlaydi."},
            {"para": 1, "en": "The last sentence turns the story into a <strong>direction</strong>: the reader now knows what she wants.",
             "uz": "Oxirgi gap hikoyani <strong>maqsadga</strong> aylantiradi: oʻquvchi endi uning nima istashini biladi."},
            {"para": 2, "en": "Evidence, with numbers: self-taught, team of four, second place. Then a <strong>lesson learned</strong> — committees want to see reflection, not a list of prizes.",
             "uz": "Raqamlar bilan dalil: mustaqil oʻrgangan, toʻrt kishilik jamoa, ikkinchi oʻrin. Keyin <strong>chiqarilgan xulosa</strong> — komissiya sovrinlar roʻyxatini emas, fikrlashni koʻrmoqchi."},
            {"para": 3, "en": "“Why Korea” without K-dramas. A <strong>reason connected to her field</strong> — this is the paragraph most applicants waste.",
             "uz": "«Nega Koreya» — doramalarsiz. <strong>Yoʻnalishiga bogʻliq sabab</strong> — koʻp nomzodlar aynan shu xatboshini behuda sarflaydi."},
            {"para": 4, "en": "Answers the committee's silent worry (“will she survive the language year?”) with a certificate and a habit.",
             "uz": "Komissiyaning aytilmagan xavotiriga («til yilini uddalay oladimi?») sertifikat va odat bilan javob beradi."},
            {"para": 5, "en": "The ending returns home: a <strong>concrete plan</strong> to use the degree in Uzbekistan. GKS exists to build ties between countries — say how you will be one.",
             "uz": "Yakun uyga qaytadi: diplomni Oʻzbekistonda qanday ishlatishning <strong>aniq rejasi</strong>. GKS davlatlar oʻrtasida koʻprik qurish uchun bor — siz qanday koʻprik boʻlishingizni ayting."},
        ],
        "prompts": [
            {"en": "A moment — not a feeling — when you first knew this field was yours. What exactly happened?", "uz": "Bu soha sizniki ekanini ilk bor sezgan lahza — his emas, voqea. Aniq nima boʻlgan?", "lines": 5},
            {"en": "Three things you have DONE for this field (courses, projects, olympiads, clubs). Add a number to each.", "uz": "Shu soha uchun QILGAN uchta ishingiz (kurslar, loyihalar, olimpiadalar, toʻgaraklar). Har biriga raqam qoʻshing.", "lines": 5},
            {"en": "What did one of them teach you about yourself?", "uz": "Ulardan biri sizga oʻzingiz haqingizda nimani oʻrgatdi?", "lines": 3},
            {"en": "Why this country for THIS field? One reason a K-drama fan could not have written.", "uz": "Nega aynan SHU soha uchun shu davlat? Doramalar muxlisi yoza olmaydigan bitta sabab.", "lines": 4},
            {"en": "What will worry the committee about you — and what is your proof it shouldn't?", "uz": "Komissiyani siz haqingizda nima xavotirga soladi — va buning keragi yoʻqligiga dalilingiz nima?", "lines": 3},
            {"en": "After graduating: what will you build or change at home? Name a place or a person it helps.", "uz": "Bitirgandan keyin: uyda nimani qurasiz yoki oʻzgartirasiz? U yordam beradigan joy yoki odamni ayting.", "lines": 4},
        ],
    },
    {
        "slug": "gks-study-plan", "order": 2, "kind": "study_plan", "scholarship": "gks",
        "title": "GKS-U study plan — Madina, computer science",
        "title_uz": "GKS-U oʻqish rejasi — Madina, kompyuter fanlari",
        "intro": "<p>The same applicant's Form 3. The personal statement says <em>who you are</em>; the study plan says <em>what you will do, year by year</em>. Keep them consistent — committees read them side by side.</p>",
        "intro_uz": "<p>Oʻsha nomzodning 3-shakli. Shaxsiy bayonot <em>kim ekaningizni</em> aytadi; oʻqish rejasi <em>yilma-yil nima qilishingizni</em>. Ikkalasi bir-biriga mos boʻlsin — komissiya ularni yonma-yon oʻqiydi.</p>",
        "letter": """
<h4>Study goal</h4>
<p>I want to become a software engineer who builds reliable, simple educational software. My goal in Korea is a bachelor's degree in computer science with a focus on software engineering and human–computer interaction.</p>
<h4>Korean language year</h4>
<p>My first target is TOPIK level 4 by the end of the language year, not only the required level 3, because lectures and group projects will be in Korean. Besides classes, I will join a language-exchange club and keep a daily diary in Korean.</p>
<h4>Years 1–2</h4>
<p>I will focus on the foundations: programming, data structures, discrete mathematics and computer architecture. I plan to join a student developer club and take part in at least one hackathon each year.</p>
<h4>Years 3–4</h4>
<p>I will take courses in software engineering, databases and human–computer interaction, and look for an undergraduate research or internship position in a lab working on educational technology. My graduation project will be a school-management tool tested with real teachers.</p>
<h4>After graduation</h4>
<p>I plan to work for two or three years in a Korean or international technology company to gain industry experience, then return to Uzbekistan to develop digital tools for schools, and to help other Uzbek students apply to study in Korea.</p>
""",
        "notes": [
            {"para": 1, "en": "One clear goal in the first sentence. Everything after it should serve this goal.", "uz": "Birinchi gapda bitta aniq maqsad. Undan keyingi hamma narsa shu maqsadga xizmat qilishi kerak."},
            {"para": 2, "en": "Aims higher than the minimum (TOPIK 4, not 3) and gives the <strong>reason</strong>. Concrete habits make the plan believable.", "uz": "Minimumdan yuqori maqsad (3 emas, TOPIK 4) va uning <strong>sababi</strong>. Aniq odatlar rejani ishonarli qiladi."},
            {"para": 3, "en": "Real course names. Look them up in your chosen department's curriculum — a committee notices when you have.", "uz": "Haqiqiy fan nomlari. Ularni tanlagan yoʻnalishingiz oʻquv rejasidan toping — komissiya buni sezadi."},
            {"para": 4, "en": "Shows growth from courses to research to a <strong>project connected to her personal statement</strong>.", "uz": "Fanlardan tadqiqotga va <strong>shaxsiy bayonotiga bogʻliq loyihaga</strong> oʻsishni koʻrsatadi."},
            {"para": 5, "en": "Honest and realistic: work first, then return. And it gives back to Uzbekistan — the reason GKS invests in you.", "uz": "Halol va real: avval ish, keyin qaytish. Va Oʻzbekistonga foyda — GKS aynan shuning uchun sizga sarmoya kiritadi."},
        ],
        "prompts": [
            {"en": "Your goal in one sentence: which degree, which focus, to become what?", "uz": "Bir gapda maqsadingiz: qaysi daraja, qaysi yoʻnalish, kim boʻlish uchun?", "lines": 3},
            {"en": "Language year: which TOPIK level by when, and three habits that will get you there.", "uz": "Til yili: qachongacha qaysi TOPIK darajasi va unga olib boradigan uchta odat.", "lines": 4},
            {"en": "Years 1–2: five real course names from your chosen department's curriculum.", "uz": "1–2-yillar: tanlagan yoʻnalishingiz oʻquv rejasidan beshta haqiqiy fan nomi.", "lines": 4},
            {"en": "Years 3–4: a lab, a club, an internship or a project — and why it fits your goal.", "uz": "3–4-yillar: laboratoriya, toʻgarak, amaliyot yoki loyiha — va nega u maqsadingizga mos.", "lines": 4},
            {"en": "After graduation: first 3 years, then 10 years from now. Where is Uzbekistan in it?", "uz": "Bitirgandan keyin: dastlabki 3 yil, keyin 10 yildan keyin. Bunda Oʻzbekiston qayerda?", "lines": 4},
        ],
    },
]
