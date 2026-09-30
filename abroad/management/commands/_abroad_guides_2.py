"""Study abroad — guides, batch 2 (CV, Certificates, Money, Visa and arrival,
Choosing a university) + three more annotated samples (recommendation letter,
CV, email to a professor).

Evergreen. Deliberately no fee figures, no exchange rates, no visa fees: they
differ by country and change; the guides teach the pattern and send the pupil
to the official page. The only programme-specific facts are the GKS ones
(TOPIK validity window, D-4/D-2) from the 2027 GKS-U guidelines, and the
Apostille objections (HCCH status table), both checked 2026-10-01.

    python manage.py import_abroad abroad/management/commands/_abroad_guides_2.py --author=prime
"""

CV = """
<p>An academic CV is not a job CV and not a biography. It is a <strong>one- or two-page list of evidence</strong>, in reverse order (newest first), that a committee can scan in thirty seconds.</p>

<h2>The sections, in order</h2>
<ol class="ab-steps">
<li><strong>Name and contacts</strong> — name exactly as in your passport, email, phone, city. No photo unless asked; no date of birth, marital status or religion.</li>
<li><strong>Education</strong> — school or university, dates, GPA (with the scale), notable subjects.</li>
<li><strong>Test scores</strong> — IELTS 6.5 (June 2026), TOPIK level 3 (April 2026), SAT…</li>
<li><strong>Awards and olympiads</strong> — what, level, year: “2nd place, regional informatics olympiad, 2025”.</li>
<li><strong>Projects and research</strong> — one line each, with a result or a number.</li>
<li><strong>Experience</strong> — jobs, internships, tutoring, volunteering.</li>
<li><strong>Skills</strong> — languages with levels; tools and software you really use.</li>
</ol>

<div class="ab-tip"><strong>Verbs and numbers</strong>
<p>Start each line with an action verb — <em>organised, built, taught, translated, led</em> — and add a number wherever you can: “taught Python to 12 younger pupils for 6 months” is a line a committee remembers.</p></div>

<div class="ab-mistake"><strong>What to leave out</strong>
<ul>
<li>“Hard-working, communicative, team player” — every CV says it.</li>
<li>Microsoft Word as a skill.</li>
<li>Primary-school achievements (for a bachelor's) or school achievements (for a master's), unless truly exceptional.</li>
<li>Anything you could not talk about for two minutes in an interview.</li>
</ul></div>

<p>Keep one master CV with everything, then cut a copy for each application. See the annotated sample CV.</p>
"""

CV_UZ = """
<p>Akademik CV — bu ish uchun rezyume ham, tarjimai hol ham emas. U komissiya oʻttiz soniyada koʻz yugurtirib chiqa oladigan, teskari tartibda (eng yangisi birinchi) yozilgan <strong>bir-ikki sahifalik dalillar roʻyxati</strong>.</p>

<h2>Boʻlimlar, tartib bilan</h2>
<ol class="ab-steps">
<li><strong>Ism va aloqa</strong> — ism pasportdagidek, email, telefon, shahar. Soʻralmasa rasm yoʻq; tugʻilgan sana, oilaviy holat yoki din yoʻq.</li>
<li><strong>Taʼlim</strong> — maktab yoki universitet, sanalar, GPA (shkalasi bilan), muhim fanlar.</li>
<li><strong>Test natijalari</strong> — IELTS 6.5 (2026-yil iyun), TOPIK 3-daraja (2026-yil aprel), SAT…</li>
<li><strong>Mukofotlar va olimpiadalar</strong> — nima, qaysi daraja, qaysi yil: «viloyat informatika olimpiadasi, 2-oʻrin, 2025».</li>
<li><strong>Loyihalar va tadqiqot</strong> — har biri bir qatorda, natija yoki raqam bilan.</li>
<li><strong>Tajriba</strong> — ish, amaliyot, repetitorlik, koʻngillilik.</li>
<li><strong>Koʻnikmalar</strong> — darajasi bilan tillar; haqiqatan ishlatadigan dastur va vositalar.</li>
</ol>

<div class="ab-tip"><strong>Feʼllar va raqamlar</strong>
<p>Har bir qatorni harakat feʼli bilan boshlang — <em>organised, built, taught, translated, led</em> — va imkon boricha raqam qoʻshing: «6 oy davomida 12 ta kichik oʻquvchiga Python oʻrgatdim» — komissiya eslab qoladigan qator.</p></div>

<div class="ab-mistake"><strong>Nimani yozmaslik kerak</strong>
<ul>
<li>«Mehnatkash, kirishimli, jamoada ishlay oladi» — har bir CVda bor.</li>
<li>Koʻnikma sifatida Microsoft Word.</li>
<li>Boshlangʻich maktabdagi yutuqlar (bakalavr uchun) yoki maktabdagi yutuqlar (magistratura uchun), agar chindan ham ajoyib boʻlmasa.</li>
<li>Suhbatda ikki daqiqa gapira olmaydigan har qanday narsa.</li>
</ul></div>

<p>Hamma narsa yozilgan bitta asosiy CV saqlang, keyin har bir ariza uchun undan qisqartirilgan nusxa oling. Izohli CV namunasini koʻring.</p>
"""

CERTS = """
<p>A certificate does two jobs: it <strong>opens the door</strong> (the minimum a university asks for) and it <strong>earns points</strong> (in scholarships that score language). Know which job yours is doing.</p>

<h2>Which certificate for which road</h2>
<table>
<tr><th>Certificate</th><th>What it proves</th><th>Where it matters most</th></tr>
<tr><td>IELTS / TOEFL</td><td>English for study</td><td>UK, Europe, Australia, English-taught programmes everywhere; Chevening; GKS (scored)</td></tr>
<tr><td>Duolingo English Test</td><td>English, online</td><td>Accepted by many universities, especially in the US — always check the university's list</td></tr>
<tr><td>SAT</td><td>Maths and reading for US admissions</td><td>US bachelor's; some universities elsewhere</td></tr>
<tr><td>TOPIK</td><td>Korean</td><td>Korean universities; GKS (scored, plus bonus points)</td></tr>
<tr><td>JLPT</td><td>Japanese</td><td>Japanese-taught programmes; MEXT</td></tr>
<tr><td>HSK</td><td>Chinese</td><td>Chinese-taught programmes; CSC</td></tr>
</table>

<div class="ab-uz"><strong>The GKS example — why the right certificate matters</strong>
<p>In the 2027 GKS bachelor's guidelines, TOPIK 3 earns the same share of the language score as IELTS 7.0 — and adds bonus points on top, which IELTS cannot. For many pupils in Uzbekistan, TOPIK 3 is the closer target. <a href="/abroad/scholarships/gks/">See the GKS page</a>.</p></div>

<h2>Validity</h2>
<p>Most universities accept IELTS, TOEFL and TOPIK results that are <strong>up to two years old</strong>, and some programmes name exact test sessions (GKS 2027 lists which TOPIK sessions count). Check the date rule before you book — a result that expires a week before the deadline is useless.</p>

<div class="ab-tip"><strong>Plan the timing</strong>
<p>Book the test so the result arrives <strong>at least two months before</strong> the deadline — enough time for one retake if the first score falls short.</p></div>

<p>Powerty has preparation for IELTS, TOPIK and SAT — the <a href="/examprep/">Exam prep</a> section.</p>
"""

CERTS_UZ = """
<p>Sertifikat ikki ish qiladi: u <strong>eshikni ochadi</strong> (universitet soʻraydigan minimum) va <strong>ball olib beradi</strong> (tilni baholaydigan stipendiyalarda). Sizniki qaysi ishni qilayotganini biling.</p>

<h2>Qaysi yoʻl uchun qaysi sertifikat</h2>
<table>
<tr><th>Sertifikat</th><th>Nimani isbotlaydi</th><th>Qayerda eng muhim</th></tr>
<tr><td>IELTS / TOEFL</td><td>Oʻqish uchun ingliz tili</td><td>Buyuk Britaniya, Yevropa, Avstraliya, hamma joydagi inglizcha dasturlar; Chevening; GKS (ball beradi)</td></tr>
<tr><td>Duolingo English Test</td><td>Ingliz tili, onlayn</td><td>Koʻp universitetlar, ayniqsa AQShda qabul qiladi — har doim universitet roʻyxatini tekshiring</td></tr>
<tr><td>SAT</td><td>AQSh qabuli uchun matematika va oʻqish</td><td>AQShda bakalavriat; boshqa joylardagi baʼzi universitetlar</td></tr>
<tr><td>TOPIK</td><td>Koreys tili</td><td>Koreya universitetlari; GKS (ball va qoʻshimcha ball)</td></tr>
<tr><td>JLPT</td><td>Yapon tili</td><td>Yapon tilidagi dasturlar; MEXT</td></tr>
<tr><td>HSK</td><td>Xitoy tili</td><td>Xitoy tilidagi dasturlar; CSC</td></tr>
</table>

<div class="ab-uz"><strong>GKS misoli — toʻgʻri sertifikat nega muhim</strong>
<p>2027-yilgi GKS bakalavr yoʻriqnomasida TOPIK 3 til balidan IELTS 7,0 bilan bir xil ulush beradi — ustiga IELTS bera olmaydigan qoʻshimcha ball ham qoʻshadi. Oʻzbekistondagi koʻp oʻquvchilar uchun TOPIK 3 yaqinroq maqsad. <a href="/abroad/scholarships/gks/">GKS sahifasiga qarang</a>.</p></div>

<h2>Amal qilish muddati</h2>
<p>Koʻp universitetlar <strong>ikki yildan eski boʻlmagan</strong> IELTS, TOEFL va TOPIK natijalarini qabul qiladi, baʼzi dasturlar esa aniq imtihon sessiyalarini koʻrsatadi (GKS 2027 qaysi TOPIK sessiyalari hisobga olinishini sanab oʻtgan). Roʻyxatdan oʻtishdan oldin sana qoidasini tekshiring — muddatdan bir hafta oldin eskiradigan natija befoyda.</p>

<div class="ab-tip"><strong>Vaqtni rejalashtiring</strong>
<p>Imtihonni natija muddatdan <strong>kamida ikki oy oldin</strong> keladigan qilib belgilang — birinchi ball yetmasa, bir marta qayta topshirishga vaqt qoladi.</p></div>

<p>Powerty'da IELTS, TOPIK va SAT tayyorlovi bor — <a href="/examprep/">Imtihonga tayyorgarlik</a> boʻlimi.</p>
"""

MONEY = """
<p>“Free” study abroad is almost never free. Even a full scholarship leaves you paying for something — the certificate, the translations, the visa, the first weeks before the first stipend. Plan the money the same way you plan the documents.</p>

<h2>Three kinds of scholarship</h2>
<table>
<tr><th>Kind</th><th>Pays</th><th>You still pay</th></tr>
<tr><td>Full scholarship</td><td>Tuition + monthly allowance, often flight and insurance</td><td>Costs before arrival; anything the allowance doesn't cover</td></tr>
<tr><td>Partial / tuition waiver</td><td>All or part of tuition</td><td>Living costs, housing, insurance, flight</td></tr>
<tr><td>University merit award</td><td>A discount on tuition</td><td>The rest of tuition and all living costs</td></tr>
</table>

<h2>When tuition is paid</h2>
<ul>
<li><strong>A deposit</strong> after you accept an offer — to hold your place. Some countries require it before they issue the document you need for the visa.</li>
<li><strong>Then per semester</strong> (or per year) before each term starts. Late payment can block registration.</li>
<li><strong>Admission or application fees</strong> are separate and usually not refundable.</li>
</ul>

<h2>How it is paid from Uzbekistan</h2>
<ol class="ab-steps">
<li>The university sends an <strong>invoice</strong> with its bank details (IBAN or account number, SWIFT/BIC code).</li>
<li>You make an <strong>international (SWIFT) transfer</strong> from a bank in Uzbekistan. Take the invoice and your passport; the payer is often a parent.</li>
<li>Expect <strong>bank fees on both sides</strong> and an exchange rate — send a little more, or ask the bank for “our” charges so the university receives the full amount.</li>
<li><strong>Keep the SWIFT confirmation</strong> and email it to the university. It is your proof if the money is late.</li>
</ol>

<div class="ab-mistake"><strong>Never pay a person</strong>
<p>Tuition goes to the <em>university's</em> account named on the official invoice — never to an “agent”, a private card, or an account given in a chat. If the details change by email, confirm by phone with the university's official number first.</p></div>

<h2>Proof of funds</h2>
<p>Many visas ask you to show money for the first year: a <strong>bank statement</strong> in your or a parent's name, or a <strong>scholarship letter</strong>. The required amount and how long the money must sit in the account are set by each country — read the embassy's page, not a forum.</p>

<h2>Living costs</h2>
<p>Rent, food, transport, phone, books and insurance. The university's international office usually publishes an estimate — use it, then add 20% for the first month.</p>
"""

MONEY_UZ = """
<p>Chet elda «bepul» oʻqish deyarli hech qachon toʻliq bepul emas. Toʻliq stipendiya boʻlsa ham nimanidir toʻlaysiz — sertifikat, tarjima, viza, birinchi stipendiyagacha boʻlgan dastlabki haftalar. Pulni ham hujjatlarni rejalashtirgandek rejalashtiring.</p>

<h2>Stipendiyaning uch turi</h2>
<table>
<tr><th>Turi</th><th>Nimani toʻlaydi</th><th>Baribir siz toʻlaysiz</th></tr>
<tr><td>Toʻliq stipendiya</td><td>Kontrakt + oylik stipendiya, koʻpincha bilet va sugʻurta</td><td>Kelishdan oldingi xarajatlar; stipendiya qoplamaydigan narsalar</td></tr>
<tr><td>Qisman / kontraktdan ozod qilish</td><td>Kontraktning hammasi yoki bir qismi</td><td>Yashash, uy-joy, sugʻurta, bilet</td></tr>
<tr><td>Universitetning yutuq granti</td><td>Kontraktdan chegirma</td><td>Kontraktning qolgani va barcha yashash xarajatlari</td></tr>
</table>

<h2>Kontrakt qachon toʻlanadi</h2>
<ul>
<li><strong>Depozit</strong> — taklifni qabul qilganingizdan keyin, joyingizni saqlab qolish uchun. Baʼzi davlatlar viza uchun kerakli hujjatni shundan keyingina beradi.</li>
<li><strong>Keyin har semestr</strong> (yoki har yil) boshlanishidan oldin. Kechiksa, roʻyxatdan oʻtish toʻxtab qolishi mumkin.</li>
<li><strong>Ariza yoki kirish toʻlovlari</strong> alohida va odatda qaytarilmaydi.</li>
</ul>

<h2>Oʻzbekistondan qanday toʻlanadi</h2>
<ol class="ab-steps">
<li>Universitet bank rekvizitlari (IBAN yoki hisob raqami, SWIFT/BIC kodi) bilan <strong>hisob-faktura (invoice)</strong> yuboradi.</li>
<li>Oʻzbekistondagi bankdan <strong>xalqaro (SWIFT) oʻtkazma</strong> qilasiz. Hisob-faktura va pasportni olib boring; toʻlovchi koʻpincha ota-onadan biri.</li>
<li><strong>Ikkala tomonda bank komissiyasi</strong> va valyuta kursini hisobga oling — biroz koʻproq yuboring yoki universitet toʻliq summani olishi uchun bankdan xarajatlarni «OUR» shartida soʻrang.</li>
<li><strong>SWIFT tasdiqnomasini saqlang</strong> va universitetga emailda yuboring. Pul kechiksa, bu sizning dalilingiz.</li>
</ol>

<div class="ab-mistake"><strong>Hech qachon shaxsga toʻlamang</strong>
<p>Kontrakt rasmiy hisob-fakturada koʻrsatilgan <em>universitet</em> hisobiga toʻlanadi — hech qachon «agent»ga, shaxsiy kartaga yoki chatda berilgan hisobga emas. Rekvizitlar emailda oʻzgarsa, avval universitetning rasmiy telefon raqami orqali tasdiqlang.</p></div>

<h2>Mablagʻ borligini tasdiqlash</h2>
<p>Koʻp vizalar birinchi yil uchun pulingiz borligini koʻrsatishni soʻraydi: sizning yoki ota-onangiz nomidagi <strong>bank koʻchirmasi</strong> yoki <strong>stipendiya xati</strong>. Kerakli summa va pul hisobda qancha turishi kerakligini har bir davlat oʻzi belgilaydi — forumni emas, elchixona sahifasini oʻqing.</p>

<h2>Yashash xarajatlari</h2>
<p>Ijara, ovqat, transport, telefon, kitoblar va sugʻurta. Universitetning xalqaro boʻlimi odatda taxminiy hisobni eʼlon qiladi — undan foydalaning va birinchi oy uchun ustiga 20% qoʻshing.</p>
"""

VISA = """
<p>Winning the scholarship is the start of a second, shorter project: getting there and settling in. It has its own paperwork.</p>

<h2>From admission to arrival</h2>
<ol class="ab-steps">
<li><strong>Admission or invitation letter</strong> — the document the visa is built on. For GKS, invitation letters and entry guidelines are emailed in January.</li>
<li><strong>Student visa</strong> — applied for at the country's embassy in Tashkent. Korea, for example, uses a D-4 visa for language study and D-2 for degree study.</li>
<li><strong>Documents for the visa</strong> — passport, admission letter, proof of funds or scholarship letter, apostilled diploma or certificate, sometimes a health check.</li>
<li><strong>Flight</strong> — only after the visa is in your passport.</li>
</ol>

<h2>Pack the paper, not only the clothes</h2>
<ul>
<li>Extra <strong>apostilled copies</strong> of your school certificate or diploma — the university, the immigration office and the embassy may each keep one.</li>
<li>Passport photos, printed admission letter, scholarship letter.</li>
<li>Scans of everything in one cloud folder.</li>
</ul>

<h2>The first month</h2>
<ul>
<li><strong>Register your residence</strong> within the deadline the country sets (in Korea, the residence card). Late registration is fined.</li>
<li>Open a local <strong>bank account</strong> — your stipend will be paid into it.</li>
<li>Get a local <strong>SIM card</strong> and join health insurance if it is not automatic.</li>
<li>Find the <strong>international office</strong> and the Uzbek students' community — they have solved every problem you are about to have.</li>
</ul>

<div class="ab-uz"><strong>The first weeks are the hardest</strong>
<p>Homesickness is normal and it passes. Keep a routine, cook one familiar meal a week, and call home at a fixed time rather than all the time. And study the language every day from day one — it is what turns a hard first semester into a good one.</p></div>
"""

VISA_UZ = """
<p>Stipendiyani yutish — ikkinchi, qisqaroq loyihaning boshlanishi: yetib borish va joylashish. Uning ham oʻz hujjatlari bor.</p>

<h2>Qabuldan yetib borishgacha</h2>
<ol class="ab-steps">
<li><strong>Qabul yoki taklif xati</strong> — viza shu hujjatga asoslanadi. GKS uchun taklifnomalar va kirish yoʻriqnomalari yanvarda emailga yuboriladi.</li>
<li><strong>Talaba vizasi</strong> — oʻsha davlatning Toshkentdagi elchixonasida rasmiylashtiriladi. Masalan, Koreyada til oʻrganish uchun D-4, daraja uchun D-2 vizasi beriladi.</li>
<li><strong>Viza uchun hujjatlar</strong> — pasport, qabul xati, mablagʻ yoki stipendiya xati, apostilli diplom yoki attestat, baʼzan tibbiy koʻrik.</li>
<li><strong>Parvoz</strong> — faqat viza pasportingizda boʻlgandan keyin.</li>
</ol>

<h2>Faqat kiyim emas, qogʻozlarni ham joylang</h2>
<ul>
<li>Attestat yoki diplomingizning qoʻshimcha <strong>apostilli nusxalari</strong> — universitet, migratsiya idorasi va elchixona har biri bittadan olib qolishi mumkin.</li>
<li>Rasmlar, chop etilgan qabul xati, stipendiya xati.</li>
<li>Hammasining skanlari bitta bulutli papkada.</li>
</ul>

<h2>Birinchi oy</h2>
<ul>
<li>Davlat belgilagan muddatda <strong>yashash joyini roʻyxatdan oʻtkazing</strong> (Koreyada — yashash kartasi). Kechiktirilsa, jarima solinadi.</li>
<li>Mahalliy <strong>bank hisobi</strong> oching — stipendiyangiz shunga tushadi.</li>
<li>Mahalliy <strong>SIM-karta</strong> oling va agar avtomatik boʻlmasa, tibbiy sugʻurtaga yoziling.</li>
<li><strong>Xalqaro boʻlim</strong>ni va oʻzbek talabalari jamoasini toping — ular siz duch keladigan har bir muammoni allaqachon hal qilgan.</li>
</ul>

<div class="ab-uz"><strong>Birinchi haftalar eng qiyini</strong>
<p>Vatanni sogʻinish tabiiy va u oʻtib ketadi. Kun tartibini saqlang, haftada bir marta tanish taom pishiring va uyga har doim emas, belgilangan vaqtda qoʻngʻiroq qiling. Va birinchi kundan har kuni til oʻrganing — qiyin birinchi semestrni yaxshisiga aylantiradigan narsa aynan shu.</p></div>
"""

CHOOSE = """
<p>“Which is the best university?” is the wrong question. The right one is: <strong>which university is best for me, in my field, with the money and the language I have?</strong></p>

<h2>Rankings — useful, and misleading</h2>
<p>QS, Times Higher Education and ARWU rank universities mostly by <strong>research and reputation</strong>, not by how well they teach bachelor's students. Use them to make a long list, never to make the final choice.</p>
<ul>
<li>Look at the <strong>subject ranking</strong> for your field, not the overall table.</li>
<li>A university ranked 300th overall may be in the top 50 for your subject.</li>
<li>Rankings change every year; a few places up or down mean nothing.</li>
</ul>

<h2>Five questions that matter more</h2>
<ol class="ab-steps">
<li><strong>Does it teach my field in a language I can learn?</strong> Check the language of instruction for <em>your</em> programme.</li>
<li><strong>Can I get in?</strong> Compare your grades and certificate with the admitted students', not with the minimum.</li>
<li><strong>Can I afford the city?</strong> Seoul and a regional city are different budgets.</li>
<li><strong>Does my scholarship place students there?</strong> In GKS, a strong regional (Type B) university is a real choice, not a backup.</li>
<li><strong>What happens after?</strong> Look at where graduates of your programme work.</li>
</ol>

<div class="ab-tip"><strong>Build a list of five</strong>
<p>Two “reach” choices (hard to get into), two “match” (your level), one “safe”. For a scholarship with several choices, like GKS, the same logic applies.</p></div>

<div class="ab-mistake"><strong>Beware the agency list</strong>
<p>An agency's “top universities” list is often the list of universities that pay the agency. Check every university on its own official website and in the scholarship's official list.</p></div>
"""

CHOOSE_UZ = """
<p>«Qaysi universitet eng yaxshi?» — notoʻgʻri savol. Toʻgʻrisi: <strong>mening sohamda, mening pulim va tilim bilan qaysi universitet men uchun eng yaxshi?</strong></p>

<h2>Reytinglar — foydali, lekin chalgʻituvchi</h2>
<p>QS, Times Higher Education va ARWU universitetlarni asosan <strong>tadqiqot va obroʻ</strong> boʻyicha baholaydi, bakalavrlarni qanchalik yaxshi oʻqitishi boʻyicha emas. Ulardan uzun roʻyxat tuzish uchun foydalaning, yakuniy tanlov uchun hech qachon.</p>
<ul>
<li>Umumiy jadvalga emas, sohangizning <strong>fan reytingi</strong>ga qarang.</li>
<li>Umumiy reytingda 300-oʻrindagi universitet sizning faningiz boʻyicha eng yaxshi 50 talikda boʻlishi mumkin.</li>
<li>Reytinglar har yili oʻzgaradi; bir necha pogʻona yuqori yoki past hech narsani anglatmaydi.</li>
</ul>

<h2>Muhimroq beshta savol</h2>
<ol class="ab-steps">
<li><strong>U mening sohamni men oʻrgana oladigan tilda oʻqitadimi?</strong> Aynan <em>sizning</em> dasturingiz qaysi tilda ekanini tekshiring.</li>
<li><strong>Kira olamanmi?</strong> Baho va sertifikatingizni minimum bilan emas, qabul qilinganlarniki bilan solishtiring.</li>
<li><strong>Shahar menga qurbim yetadimi?</strong> Seul va viloyat shahri — ikki xil byudjet.</li>
<li><strong>Stipendiyam u yerga talaba joylashtiradimi?</strong> GKSda kuchli viloyat (Type B) universiteti — zaxira emas, haqiqiy tanlov.</li>
<li><strong>Keyin nima boʻladi?</strong> Dasturingiz bitiruvchilari qayerda ishlashiga qarang.</li>
</ol>

<div class="ab-tip"><strong>Beshtalik roʻyxat tuzing</strong>
<p>Ikkita «orzu» (kirish qiyin), ikkita «mos» (darajangizda), bitta «ishonchli». GKS kabi bir nechta tanlovli stipendiyada ham shu mantiq ishlaydi.</p></div>

<div class="ab-mistake"><strong>Agentlik roʻyxatidan ehtiyot boʻling</strong>
<p>Agentlikning «top universitetlar» roʻyxati koʻpincha agentlikka pul toʻlaydigan universitetlar roʻyxati boʻladi. Har bir universitetni uning rasmiy saytida va stipendiyaning rasmiy roʻyxatida tekshiring.</p></div>
"""

GUIDES = [
    {"slug": "academic-cv", "order": 6, "category": "letters", "icon": "bi-person-vcard", "minutes": 4,
     "title": "The academic CV", "title_uz": "Akademik CV",
     "summary": "One or two pages of evidence, newest first — sections, verbs, numbers, and what to leave out.",
     "summary_uz": "Bir-ikki sahifa dalil, eng yangisi birinchi — boʻlimlar, feʼllar, raqamlar va nimani yozmaslik kerak.",
     "body": CV, "body_uz": CV_UZ},
    {"slug": "certificates", "order": 7, "category": "documents", "icon": "bi-patch-check", "minutes": 4,
     "title": "Certificates: which one does what", "title_uz": "Sertifikatlar: qaysi biri nima qiladi",
     "summary": "IELTS, TOEFL, Duolingo, SAT, TOPIK, JLPT, HSK — which road each opens, and why TOPIK 3 can beat IELTS 7 for GKS.",
     "summary_uz": "IELTS, TOEFL, Duolingo, SAT, TOPIK, JLPT, HSK — har biri qaysi yoʻlni ochadi va nega GKSda TOPIK 3 IELTS 7 dan ustun kelishi mumkin.",
     "body": CERTS, "body_uz": CERTS_UZ},
    {"slug": "money", "order": 8, "category": "money", "icon": "bi-cash-coin", "minutes": 5,
     "title": "Money: tuition, when and how it is paid", "title_uz": "Pul: kontrakt, qachon va qanday toʻlanadi",
     "summary": "Full vs partial scholarships, deposits and semesters, SWIFT transfers from Uzbekistan, proof of funds.",
     "summary_uz": "Toʻliq va qisman stipendiya, depozit va semestrlar, Oʻzbekistondan SWIFT oʻtkazma, mablagʻni tasdiqlash.",
     "body": MONEY, "body_uz": MONEY_UZ},
    {"slug": "visa-and-arrival", "order": 9, "category": "after", "icon": "bi-airplane", "minutes": 4,
     "title": "Visa and the first month", "title_uz": "Viza va birinchi oy",
     "summary": "From admission letter to student visa to residence registration — and the papers to pack.",
     "summary_uz": "Qabul xatidan talaba vizasigacha va yashash joyini roʻyxatdan oʻtkazishgacha — hamda olib ketiladigan qogʻozlar.",
     "body": VISA, "body_uz": VISA_UZ},
    {"slug": "choosing-a-university", "order": 10, "category": "choose", "icon": "bi-bar-chart-steps", "minutes": 4,
     "title": "Choosing a university (and reading rankings)", "title_uz": "Universitet tanlash (va reytinglarni oʻqish)",
     "summary": "What rankings measure and what they miss, five better questions, and a list of five.",
     "summary_uz": "Reytinglar nimani oʻlchaydi va nimani oʻtkazib yuboradi, beshta yaxshiroq savol va beshtalik roʻyxat.",
     "body": CHOOSE, "body_uz": CHOOSE_UZ},
]

SAMPLES = [
    {
        "slug": "recommendation-letter", "order": 3, "kind": "recommendation", "scholarship": "gks",
        "title": "A teacher's recommendation letter", "title_uz": "Oʻqituvchining tavsiyanomasi",
        "intro": "<p>Written by Madina's (fictional) informatics teacher. Show this page to <em>your</em> teacher together with your brag sheet — it shows what a specific letter looks like.</p>",
        "intro_uz": "<p>Madinaning (oʻylab topilgan) informatika oʻqituvchisi yozgan. Bu sahifani yutuqlar varagʻingiz bilan birga <em>oʻz</em> oʻqituvchingizga koʻrsating — aniq tavsiyanoma qanday boʻlishini koʻrsatadi.</p>",
        "letter": """
<p>I have taught informatics at School No. 12 in Samarkand for eleven years, and I taught Madina Karimova for three of them, from Year 9 to Year 11. I am writing to recommend her for the Global Korea Scholarship without reservation.</p>
<p>Among the roughly 300 pupils I have taught, Madina is one of the three most capable programmers. In Year 10 she led our school team of four at the regional informatics olympiad, where they placed second. What impressed me more than the result was how she led: she spent the evenings before the competition explaining her code to the weaker team members instead of writing more of it herself.</p>
<p>She is also persistent. When her timetable app for our school failed on its first day, she did not give up; she came to my office every break for a week until it worked. Sixty pupils now use it every morning.</p>
<p>Madina has already started learning Korean on her own and passed TOPIK level 2 this year. I am confident she will complete the language year successfully and make the most of her studies in Korea. I recommend her most highly.</p>
""",
        "notes": [
            {"para": 1, "en": "How long and in what role the teacher knows her — the committee's first question.", "uz": "Oʻqituvchi uni qancha vaqt va qaysi rolda taniydi — komissiyaning birinchi savoli."},
            {"para": 2, "en": "A <strong>comparison</strong> with a number (“one of three among 300”) and a story that shows leadership, not just the word.", "uz": "Raqamli <strong>taqqoslash</strong> («300 tadan eng yaxshi uchtadan biri») va faqat soʻzni emas, yetakchilikni koʻrsatadigan voqea."},
            {"para": 3, "en": "A second quality with its own evidence — and it agrees with her personal statement.", "uz": "Oʻz dalili bilan ikkinchi fazilat — va u shaxsiy bayonotiga mos keladi."},
            {"para": 4, "en": "Answers the language-year worry and ends with a clear recommendation.", "uz": "Til yili haqidagi xavotirga javob beradi va aniq tavsiya bilan tugaydi."},
        ],
        "prompts": [
            {"en": "Which teacher knows your work best — and for how long?", "uz": "Qaysi oʻqituvchi ishingizni eng yaxshi biladi — va qancha vaqtdan beri?", "lines": 2},
            {"en": "Two moments in their class they may remember (with dates).", "uz": "Ularning darsida sodir boʻlgan va ular eslashi mumkin boʻlgan ikkita lahza (sanalar bilan).", "lines": 4},
            {"en": "One quality you hope they will describe — and the proof.", "uz": "Ular tasvirlashini xohlagan bitta fazilatingiz — va dalili.", "lines": 3},
            {"en": "Your grades in their subject and anything you won.", "uz": "Ularning fanidan baholaringiz va yutgan narsalaringiz.", "lines": 2},
            {"en": "The deadline, and the date you will give them this sheet (at least one month before).", "uz": "Muddat va bu varaqni ularga beradigan sanangiz (kamida bir oy oldin).", "lines": 2},
        ],
    },
    {
        "slug": "academic-cv", "order": 4, "kind": "cv", "scholarship": None,
        "title": "A school-leaver's academic CV", "title_uz": "Bitiruvchining akademik CV si",
        "intro": "<p>A one-page CV for a bachelor's application (fictional applicant). Every line is evidence, newest first.</p>",
        "intro_uz": "<p>Bakalavr arizasi uchun bir sahifalik CV (oʻylab topilgan nomzod). Har bir qator — dalil, eng yangisi birinchi.</p>",
        "letter": """
<p><strong>MADINA KARIMOVA</strong><br>Samarkand, Uzbekistan · madina.karimova@email.com · +998 90 000 00 00</p>
<p><strong>EDUCATION</strong><br>School No. 12, Samarkand — general secondary education, 2015–2026 (expected June 2026)<br>Average grade 4.8 / 5.0 (official conversion: 96 / 100). Strongest subjects: informatics, mathematics, English.</p>
<p><strong>TEST SCORES</strong><br>IELTS Academic 6.5 (March 2026) · TOPIK II level 3 (April 2026)</p>
<p><strong>AWARDS</strong><br>2nd place, regional informatics olympiad, team captain (2025)<br>Certificate of excellence, school science fair (2024)</p>
<p><strong>PROJECTS</strong><br>School timetable app (2024) — built with Python and a simple web page; used daily by 60 pupils.<br>Korean vocabulary bot (2025) — a Telegram bot that sends 10 words a day; 40 users.</p>
<p><strong>EXPERIENCE</strong><br>Volunteer tutor, 2024–2026 — taught Python basics to 12 younger pupils every Saturday for six months.</p>
<p><strong>SKILLS</strong><br>Languages: Uzbek (native), Russian (fluent), English (IELTS 6.5), Korean (TOPIK 3)<br>Programming: Python, HTML/CSS, basic SQL</p>
""",
        "notes": [
            {"para": 1, "en": "Name as in the passport, and only the contacts a committee needs. No photo, birth date or family status.", "uz": "Ism pasportdagidek va komissiyaga kerak boʻlgan aloqa maʼlumotlari xolos. Rasm, tugʻilgan sana yoki oilaviy holat yoʻq."},
            {"para": 2, "en": "Gives the Uzbek grade <strong>and</strong> the official conversion — the committee should not have to guess.", "uz": "Oʻzbekcha baho <strong>va</strong> rasmiy qayta hisob — komissiya taxmin qilishga majbur boʻlmasin."},
            {"para": 3, "en": "Test, level and month. A date shows the result is still valid.", "uz": "Test, daraja va oy. Sana natija hali amal qilishini koʻrsatadi."},
            {"para": 5, "en": "Each project: what, with what, and a <strong>number</strong> that proves someone used it.", "uz": "Har bir loyiha: nima, nima bilan va kimdir undan foydalanganini isbotlaydigan <strong>raqam</strong>."},
            {"para": 7, "en": "Languages with real levels — the certificate, not “good”.", "uz": "Tillar haqiqiy darajasi bilan — «yaxshi» emas, sertifikat."},
        ],
        "prompts": [
            {"en": "Education: school, years, average grade — and the official conversion if needed.", "uz": "Taʼlim: maktab, yillar, oʻrtacha baho — va kerak boʻlsa rasmiy qayta hisob.", "lines": 3},
            {"en": "Every test you have taken: name, score, month.", "uz": "Topshirgan barcha testlaringiz: nomi, bali, oyi.", "lines": 2},
            {"en": "Awards and olympiads: what, which level, which year.", "uz": "Mukofot va olimpiadalar: nima, qaysi daraja, qaysi yil.", "lines": 3},
            {"en": "Projects: what you built or did, and a number for each.", "uz": "Loyihalar: nima qurdingiz yoki qildingiz va har biriga raqam.", "lines": 4},
            {"en": "Experience: tutoring, volunteering, jobs — with how long and how many.", "uz": "Tajriba: repetitorlik, koʻngillilik, ish — qancha vaqt va nechta bilan.", "lines": 3},
        ],
    },
    {
        "slug": "email-to-professor", "order": 5, "kind": "email", "scholarship": None,
        "title": "A first email to a professor (master's)", "title_uz": "Professorga birinchi xat (magistratura)",
        "intro": "<p>For a research master's, contacting a possible supervisor before you apply can help — some programmes even require it. A good first email is short, specific and easy to answer.</p>",
        "intro_uz": "<p>Tadqiqotga yoʻnaltirilgan magistratura uchun ariza berishdan oldin boʻlajak ilmiy rahbar bilan bogʻlanish foydali — baʼzi dasturlar buni hatto talab qiladi. Yaxshi birinchi xat qisqa, aniq va javob berish oson boʻladi.</p>",
        "letter": """
<p><strong>Subject:</strong> Prospective master's student — machine learning for crop monitoring</p>
<p>Dear Professor Kim,</p>
<p>I am a final-year computer science student at the National University of Uzbekistan, and I plan to apply for a master's in your department through the Global Korea Scholarship.</p>
<p>I read your 2025 paper on detecting drought stress from satellite images, and I was struck by how your model worked with low-resolution data. My graduation project uses a similar approach to estimate cotton yields in the Syrdarya region, where high-resolution images are rarely available.</p>
<p>I would be grateful to know whether you expect to accept a master's student in your lab for the next academic year. I have attached my CV and a one-page summary of my project.</p>
<p>Thank you for your time.<br>Sincerely,<br>Jasur Toshmatov</p>
""",
        "notes": [
            {"para": 1, "en": "A subject line that tells the professor who you are and the topic before opening the email.", "uz": "Professor xatni ochmasdan kim ekaningizni va mavzuni biladigan sarlavha."},
            {"para": 3, "en": "Who you are and why you are writing — in two lines.", "uz": "Kim ekaningiz va nega yozayotganingiz — ikki qatorda."},
            {"para": 4, "en": "Proof you actually read their work, and a <strong>link to your own</strong>. This is the paragraph that gets replies.", "uz": "Ularning ishini haqiqatan oʻqiganingiz isboti va <strong>oʻz ishingizga bogʻlanish</strong>. Javob keltiradigan xatboshi aynan shu."},
            {"para": 5, "en": "One clear question that is easy to answer, plus short attachments.", "uz": "Javob berish oson boʻlgan bitta aniq savol va qisqa ilovalar."},
        ],
        "prompts": [
            {"en": "Which professor, and which of their recent papers did you read?", "uz": "Qaysi professor va uning qaysi soʻnggi maqolasini oʻqidingiz?", "lines": 2},
            {"en": "One specific thing in that paper that connects to your own work.", "uz": "Oʻsha maqoladagi oʻz ishingizga bogʻlanadigan bitta aniq narsa.", "lines": 3},
            {"en": "Your project in two sentences.", "uz": "Loyihangiz ikki gapda.", "lines": 3},
            {"en": "The one question you will ask.", "uz": "Beradigan yagona savolingiz.", "lines": 2},
        ],
    },
]
