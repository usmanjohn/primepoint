"""Study abroad — guides, batch 1 (Start here, Personal statement, Study plan,
Recommendation letters, Documents).

Evergreen advice. The country-specific facts were checked 2026-10-01:
Uzbekistan joined the Apostille Convention (in force 15 April 2012); Germany,
Austria and Greece still object (Belgium withdrew in 2025) — HCCH status table. requests go through my.gov.uz and issued
apostilles can be verified at apostille.davxizmat.uz. The issuing agency is
deliberately not named — it has been renamed more than once and sources
disagree; the portal is stable.

    python manage.py import_abroad abroad/management/commands/_abroad_guides_1.py --author=prime
"""

START = """
<p>Most pupils start at the wrong end: they look for a university, then discover the deadline was last month and their certificate is missing. Work backwards from the deadline instead. A scholarship application is a <strong>12-month project</strong>, and almost all of the work happens before the form opens.</p>

<h2>The year, backwards</h2>
<table>
<tr><th>When</th><th>What</th></tr>
<tr><td>12 months before</td><td>Choose your direction: which degree, which field, which 2–3 countries. Start the language certificate (IELTS, TOPIK…).</td></tr>
<tr><td>9 months before</td><td>Check your grades against the scholarship's rule. Ask your school for a transcript and, if needed, an official grade conversion.</td></tr>
<tr><td>6 months before</td><td>Pick universities and departments. Ask your recommenders. Start writing — first draft of the personal statement.</td></tr>
<tr><td>4 months before</td><td>Translations and apostille. They take weeks; do them now.</td></tr>
<tr><td>2 months before</td><td>Final letters, forms filled in, every name checked against the passport.</td></tr>
<tr><td>The window</td><td>Submit in the first days, not the last hour. Servers slow down on the final day.</td></tr>
<tr><td>After</td><td>Interview preparation, then admission letter → visa → flight.</td></tr>
</table>

<h2>Three questions to answer first</h2>
<ol class="ab-steps">
<li><strong>Why do I want to study abroad?</strong> “Everyone goes” is not an answer a committee will accept — and it will not keep you going through a hard first year.</li>
<li><strong>Which field?</strong> A scholarship funds a subject, not a country. Decide the subject first.</li>
<li><strong>Which language will I study in?</strong> English opens the most doors; Korean or Japanese open fully funded government programmes with a language year included.</li>
</ol>

<div class="ab-uz"><strong>For pupils in Uzbekistan</strong>
<p>You are not competing with the whole world: most government scholarships have a <strong>quota per country</strong>. For GKS 2027 bachelor's, Uzbekistan's Embassy track has 3 places. That is small — but it is 3 places for applicants from here, and the strongest applications are usually the most carefully prepared, not the most brilliant.</p></div>

<div class="ab-tip"><strong>Keep one folder</strong>
<p>Scan every document once, in colour, and name the files clearly (<em>passport.pdf</em>, <em>attestat_apostille.pdf</em>). Keep the originals in a single envelope. You will be asked for the same papers again and again — at admission, at the visa, at arrival.</p></div>

<p>Next: the letters. Start with the personal statement — it takes the longest.</p>
"""

START_UZ = """
<p>Koʻp oʻquvchilar teskari tomondan boshlaydi: avval universitet qidiradi, keyin muddat oʻtgan oyda tugaganini va sertifikat yoʻqligini bilib qoladi. Buning oʻrniga muddatdan orqaga qarab ishlang. Stipendiyaga topshirish — <strong>12 oylik loyiha</strong>, va ishning deyarli hammasi ariza ochilishidan oldin qilinadi.</p>

<h2>Yil — orqadan oldinga</h2>
<table>
<tr><th>Qachon</th><th>Nima</th></tr>
<tr><td>12 oy oldin</td><td>Yoʻnalishni tanlang: qaysi daraja, qaysi soha, qaysi 2–3 davlat. Til sertifikatiga tayyorlanishni boshlang (IELTS, TOPIK…).</td></tr>
<tr><td>9 oy oldin</td><td>Baholaringizni stipendiya qoidasi bilan solishtiring. Maktabdan baholar varaqasi va kerak boʻlsa rasmiy qayta hisobni soʻrang.</td></tr>
<tr><td>6 oy oldin</td><td>Universitet va yoʻnalishlarni tanlang. Tavsiyanoma yozadiganlardan soʻrang. Yozishni boshlang — shaxsiy bayonotning birinchi qoralamasi.</td></tr>
<tr><td>4 oy oldin</td><td>Tarjima va apostil. Ular haftalab vaqt oladi — hozir qiling.</td></tr>
<tr><td>2 oy oldin</td><td>Yakuniy xatlar, toʻldirilgan shakllar, har bir ism pasport bilan solishtirilgan.</td></tr>
<tr><td>Ariza oynasi</td><td>Birinchi kunlarda topshiring, oxirgi soatda emas. Oxirgi kuni sayt sekinlashadi.</td></tr>
<tr><td>Keyin</td><td>Suhbatga tayyorgarlik, keyin qabul xati → viza → parvoz.</td></tr>
</table>

<h2>Avval javob berish kerak boʻlgan uchta savol</h2>
<ol class="ab-steps">
<li><strong>Nega chet elda oʻqimoqchiman?</strong> «Hamma ketyapti» — komissiya qabul qiladigan javob emas, va u sizni qiyin birinchi yilda ushlab ham turmaydi.</li>
<li><strong>Qaysi soha?</strong> Stipendiya davlatni emas, fanni moliyalaydi. Avval fanni hal qiling.</li>
<li><strong>Qaysi tilda oʻqiyman?</strong> Ingliz tili eng koʻp eshikni ochadi; koreys yoki yapon tili esa til yili bilan birga toʻliq moliyalanadigan davlat dasturlarini ochadi.</li>
</ol>

<div class="ab-uz"><strong>Oʻzbekistondagi oʻquvchilar uchun</strong>
<p>Siz butun dunyo bilan raqobat qilmaysiz: koʻp davlat stipendiyalarida <strong>har bir davlatga kvota</strong> bor. GKS 2027 bakalavr dasturida Oʻzbekistonning elchixona yoʻliga 3 ta oʻrin berilgan. Bu kam — lekin bu shu yerdan topshiruvchilar uchun 3 ta oʻrin, va eng kuchli arizalar odatda eng iqtidorlilarniki emas, eng puxta tayyorlanganlarniki boʻladi.</p></div>

<div class="ab-tip"><strong>Bitta papka tuting</strong>
<p>Har bir hujjatni bir marta, rangli qilib skanerlang va fayllarga aniq nom bering (<em>passport.pdf</em>, <em>attestat_apostil.pdf</em>). Asl nusxalarni bitta konvertda saqlang. Sizdan oʻsha qogʻozlar qayta-qayta soʻraladi — qabulda, vizada, kelganingizda.</p></div>

<p>Keyingisi: xatlar. Shaxsiy bayonotdan boshlang — u eng koʻp vaqt oladi.</p>
"""

STATEMENT = """
<p>The personal statement (also called a motivation letter or statement of purpose) is the only part of your application where the committee hears <em>your voice</em>. Grades say what you achieved; the statement says who you are and why you will use the chance well.</p>

<h2>What committees actually look for</h2>
<ul>
<li><strong>Direction</strong> — a clear field and a reason for it.</li>
<li><strong>Evidence</strong> — things you have done, not things you feel.</li>
<li><strong>Reflection</strong> — what those things taught you.</li>
<li><strong>Fit</strong> — why this programme, this country, now.</li>
<li><strong>Return</strong> — what you will do with it afterwards.</li>
</ul>

<h2>A shape that works</h2>
<ol class="ab-steps">
<li><strong>A moment.</strong> Open with one specific scene that shows your interest being born. Not “since childhood”.</li>
<li><strong>What you did about it.</strong> Courses, projects, olympiads, clubs, volunteering — with numbers.</li>
<li><strong>What it taught you.</strong> One honest lesson, even about a failure.</li>
<li><strong>Why here.</strong> A reason tied to your field: a professor, a lab, an industry, a teaching method.</li>
<li><strong>Your plan and your return.</strong> What you will study, then what you will build or change at home.</li>
</ol>

<div class="ab-mistake"><strong>Sentences every committee has read a thousand times</strong>
<ul>
<li>“Since my early childhood I have been fascinated by…”</li>
<li>“I am a hard-working, responsible and creative person.” (Show it; never claim it.)</li>
<li>“I love Korean culture, K-pop and dramas.” (For GKS this is the most common — and weakest — reason.)</li>
<li>“Your prestigious university is one of the best in the world.”</li>
</ul></div>

<h2>The rules of writing it</h2>
<ul>
<li><strong>Specific beats impressive.</strong> “I taught 12 younger pupils Python every Saturday” beats “I am passionate about education”.</li>
<li><strong>Follow the form.</strong> If the official form has headings or a word limit, obey them exactly.</li>
<li><strong>Write it yourself, in your own English.</strong> Simple correct sentences are better than borrowed beautiful ones. Committees and software check for copied text, and an AI-written letter sounds like every other one.</li>
<li><strong>Draft, wait, cut.</strong> Write a first draft, leave it for three days, then cut every sentence that could be in someone else's letter.</li>
<li><strong>One reader who knows you, one who doesn't.</strong> A teacher checks the facts; a stranger checks whether it is clear.</li>
</ul>

<div class="ab-uz"><strong>Writing in English when you think in Uzbek</strong>
<p>Plan in Uzbek — the planner on each sample lets you. Then write short English sentences, one idea each. Long sentences translated word by word from Uzbek are where most grammar mistakes hide.</p></div>

<p>See the annotated sample: a GKS personal statement with notes on why each paragraph works.</p>
"""

STATEMENT_UZ = """
<p>Shaxsiy bayonot (motivatsion xat yoki maqsad bayonoti ham deyiladi) — arizangizning komissiya <em>sizning ovozingizni</em> eshitadigan yagona qismi. Baholar nimaga erishganingizni aytadi; bayonot esa kim ekaningizni va bu imkoniyatdan qanday foydalanishingizni aytadi.</p>

<h2>Komissiya aslida nimani qidiradi</h2>
<ul>
<li><strong>Yoʻnalish</strong> — aniq soha va uning sababi.</li>
<li><strong>Dalil</strong> — his qilgan narsalaringiz emas, qilgan ishlaringiz.</li>
<li><strong>Fikrlash</strong> — bu ishlar sizga nimani oʻrgatgani.</li>
<li><strong>Moslik</strong> — nega aynan shu dastur, shu davlat, hozir.</li>
<li><strong>Qaytish</strong> — keyin undan qanday foydalanasiz.</li>
</ul>

<h2>Ishlaydigan tuzilma</h2>
<ol class="ab-steps">
<li><strong>Bir lahza.</strong> Qiziqishingiz tugʻilganini koʻrsatadigan bitta aniq voqea bilan boshlang. «Bolaligimdan» bilan emas.</li>
<li><strong>Buning uchun nima qildingiz.</strong> Kurslar, loyihalar, olimpiadalar, toʻgaraklar, koʻngillilik — raqamlar bilan.</li>
<li><strong>Bu sizga nima oʻrgatdi.</strong> Bitta halol xulosa, hatto muvaffaqiyatsizlik haqida boʻlsa ham.</li>
<li><strong>Nega aynan shu yer.</strong> Sohangizga bogʻliq sabab: professor, laboratoriya, sanoat, oʻqitish usuli.</li>
<li><strong>Rejangiz va qaytishingiz.</strong> Nimani oʻqiysiz, keyin uyda nimani qurasiz yoki oʻzgartirasiz.</li>
</ol>

<div class="ab-mistake"><strong>Komissiya ming marta oʻqigan gaplar</strong>
<ul>
<li>«Bolaligimdan … ga qiziqib kelaman…»</li>
<li>«Men mehnatkash, masʼuliyatli va ijodkor insonman.» (Koʻrsating; hech qachon daʼvo qilmang.)</li>
<li>«Men koreys madaniyati, K-pop va doramalarni yaxshi koʻraman.» (GKS uchun bu eng keng tarqalgan — va eng zaif — sabab.)</li>
<li>«Sizning nufuzli universitetingiz dunyodagi eng yaxshilaridan biri.»</li>
</ul></div>

<h2>Yozish qoidalari</h2>
<ul>
<li><strong>Aniqlik — taassurotdan kuchli.</strong> «Har shanba 12 ta kichik oʻquvchiga Python oʻrgatdim» — «Taʼlimga ishtiyoqim baland»dan kuchli.</li>
<li><strong>Shaklga amal qiling.</strong> Rasmiy shaklda sarlavhalar yoki soʻz chegarasi boʻlsa, ularga aynan rioya qiling.</li>
<li><strong>Oʻzingiz, oʻz inglizchangizda yozing.</strong> Oddiy toʻgʻri gaplar oʻzlashtirilgan chiroyli gaplardan yaxshi. Komissiya va dasturlar koʻchirilgan matnni tekshiradi, sunʼiy intellekt yozgan xat esa boshqa hammasiga oʻxshab ketadi.</li>
<li><strong>Yozing, kuting, qisqartiring.</strong> Birinchi qoralamani yozing, uch kun qoldiring, keyin boshqa birovning xatida ham boʻlishi mumkin boʻlgan har bir gapni oʻchiring.</li>
<li><strong>Sizni taniydigan bir oʻquvchi, tanimaydigan bitta.</strong> Oʻqituvchi faktlarni tekshiradi; begona odam — tushunarliligini.</li>
</ul>

<div class="ab-uz"><strong>Oʻzbekcha oʻylab, inglizcha yozish</strong>
<p>Rejani oʻzbekcha tuzing — har bir namunadagi reja varagʻi shunga imkon beradi. Keyin qisqa inglizcha gaplar yozing, har birida bitta fikr. Oʻzbekchadan soʻzma-soʻz tarjima qilingan uzun gaplar — grammatik xatolarning asosiy uyasi.</p></div>

<p>Izohli namunani koʻring: har bir xatboshi nega ishlashi tushuntirilgan GKS shaxsiy bayonoti.</p>
"""

STUDY_PLAN = """
<p>A study plan is not a second personal statement. The statement answers <em>who are you and why</em>; the plan answers <strong>what exactly will you do, and when</strong>. GKS asks for both, as separate forms, and many universities ask for a plan for a master's.</p>

<h2>What goes in it</h2>
<ol class="ab-steps">
<li><strong>Study goal</strong> — one sentence: degree, field, focus.</li>
<li><strong>Language preparation</strong> — for GKS, the language year: which level by when, and how.</li>
<li><strong>Course plan</strong> — early years (foundations), later years (specialisation). Use <em>real course names</em> from your chosen department.</li>
<li><strong>Beyond classes</strong> — clubs, labs, internships, a graduation project.</li>
<li><strong>After graduation</strong> — the first years, then the long term.</li>
</ol>

<div class="ab-tip"><strong>The single most convincing thing</strong>
<p>Open your chosen department's website and read its curriculum. Name three or four actual courses in your plan. It takes an hour, and it tells the committee you have already started.</p></div>

<h2>For a master's: research, not courses</h2>
<p>A master's plan is closer to a small research proposal: the question you want to study, why it matters, which method you might use, and which professor's work it connects to. Read two or three of that professor's recent papers first — and say how your question relates to them.</p>

<div class="ab-mistake"><strong>Common weaknesses</strong>
<ul>
<li>Only wishes: “I will study hard and gain knowledge.” Say what, when, how.</li>
<li>A plan that contradicts the personal statement (different field, different goal).</li>
<li>No language plan for a programme taught in Korean or Japanese.</li>
<li>An “after graduation” that is only “I will find a good job”.</li>
</ul></div>

<div class="ab-uz"><strong>Be honest about returning</strong>
<p>You do not have to promise to come home the day after graduation. “Two or three years of experience abroad, then back to Uzbekistan to…” is realistic and committees accept it. What they will not accept is a plan with no answer at all.</p></div>
"""

STUDY_PLAN_UZ = """
<p>Oʻqish rejasi — ikkinchi shaxsiy bayonot emas. Bayonot <em>kimsiz va nega</em> degan savolga javob beradi; reja esa <strong>aynan nima qilasiz va qachon</strong> degan savolga. GKS ikkalasini alohida shakl sifatida soʻraydi, koʻp universitetlar esa magistratura uchun reja talab qiladi.</p>

<h2>Unga nima kiradi</h2>
<ol class="ab-steps">
<li><strong>Oʻqish maqsadi</strong> — bir gap: daraja, soha, yoʻnalish.</li>
<li><strong>Tilga tayyorgarlik</strong> — GKS uchun til yili: qachongacha qaysi daraja va qanday.</li>
<li><strong>Fanlar rejasi</strong> — dastlabki yillar (asoslar), keyingi yillar (ixtisoslik). Tanlagan yoʻnalishingizdagi <em>haqiqiy fan nomlaridan</em> foydalaning.</li>
<li><strong>Darsdan tashqari</strong> — toʻgaraklar, laboratoriyalar, amaliyot, bitiruv loyihasi.</li>
<li><strong>Bitirgandan keyin</strong> — dastlabki yillar, keyin uzoq muddat.</li>
</ol>

<div class="ab-tip"><strong>Eng ishonarli narsa</strong>
<p>Tanlagan yoʻnalishingiz saytini ochib, oʻquv rejasini oʻqing. Rejangizda uch-toʻrtta haqiqiy fan nomini keltiring. Bu bir soat oladi va komissiyaga siz allaqachon boshlaganingizni koʻrsatadi.</p></div>

<h2>Magistratura uchun: fanlar emas, tadqiqot</h2>
<p>Magistratura rejasi kichik tadqiqot taklifiga yaqin: oʻrganmoqchi boʻlgan savolingiz, u nega muhim, qaysi usulni qoʻllashingiz mumkin va u qaysi professorning ishiga bogʻlanadi. Avval oʻsha professorning soʻnggi ikki-uchta maqolasini oʻqing — va savolingiz ularga qanday bogʻliqligini yozing.</p>

<div class="ab-mistake"><strong>Keng tarqalgan kamchiliklar</strong>
<ul>
<li>Faqat orzular: «Yaxshi oʻqib, bilim olaman.» Nima, qachon, qanday — shuni yozing.</li>
<li>Shaxsiy bayonotga zid reja (boshqa soha, boshqa maqsad).</li>
<li>Koreys yoki yapon tilida oʻqitiladigan dastur uchun til rejasining yoʻqligi.</li>
<li>«Bitirgandan keyin» qismida faqat «yaxshi ish topaman».</li>
</ul></div>

<div class="ab-uz"><strong>Qaytish haqida halol boʻling</strong>
<p>Bitirgan kuningizning ertasiga qaytishga vaʼda berish shart emas. «Chet elda ikki-uch yil tajriba, keyin Oʻzbekistonga qaytib …» — bu real va komissiya uni qabul qiladi. Qabul qilmaydigani — umuman javobi yoʻq reja.</p></div>
"""

RECOMMENDATION = """
<p>A recommendation letter is someone else's voice saying what you cannot say about yourself. A strong one is <strong>specific</strong>; a weak one could be about any pupil in the class.</p>

<h2>Whom to ask</h2>
<ul>
<li>Someone who has <strong>taught you and knows your work</strong> — a subject teacher, a class teacher, the principal who knows you; for a master's, a professor or supervisor.</li>
<li>Knowing you well beats a famous title. A teacher who can describe your project is worth more than a director who has never spoken to you.</li>
<li>Follow the rules: GKS bachelor's asks for a teacher or principal, dated within one year of the deadline.</li>
</ul>

<h2>How to ask</h2>
<ol class="ab-steps">
<li><strong>Ask early</strong> — at least a month before you need it. Teachers are busy.</li>
<li><strong>Ask in person</strong>, then send the details in writing.</li>
<li><strong>Give them a “brag sheet”</strong> — one page that makes their job easy (below).</li>
<li><strong>Give them the form</strong> if the scholarship has one, and the deadline.</li>
<li><strong>Thank them</strong> — and tell them the result, whatever it is.</li>
</ol>

<div class="ab-tip"><strong>The brag sheet — one page you hand your recommender</strong>
<ul>
<li>What you are applying for, and the deadline.</li>
<li>Your grades in their subject, and your class rank if you know it.</li>
<li>Two or three things you did in their class or school that they may remember — with dates.</li>
<li>One quality you hope they can speak to (curiosity, persistence, leadership) and a moment that shows it.</li>
<li>Your personal statement's first draft, so the letters agree.</li>
</ul></div>

<h2>What a strong letter contains</h2>
<ul>
<li>How the recommender knows you and for how long.</li>
<li>A <strong>comparison</strong>: “among the best three of the 120 pupils I have taught in five years”.</li>
<li>One or two <strong>stories</strong> that show a quality.</li>
<li>A clear closing recommendation.</li>
</ul>

<div class="ab-mistake"><strong>Do not write it yourself for them to sign</strong>
<p>It happens, and committees can tell: the letter sounds exactly like the applicant's own statement. If a teacher asks you to draft it, give them the brag sheet instead and let them write in their own words — even in Uzbek, with a certified translation, if the rules allow.</p></div>
"""

RECOMMENDATION_UZ = """
<p>Tavsiyanoma — siz oʻzingiz haqingizda ayta olmaydigan narsani boshqa birovning ovozi bilan aytish. Kuchli tavsiyanoma <strong>aniq</strong> boʻladi; zaifi esa sinfdagi istalgan oʻquvchi haqida boʻlishi mumkin.</p>

<h2>Kimdan soʻrash kerak</h2>
<ul>
<li><strong>Sizga dars bergan va ishingizni biladigan</strong> odamdan — fan oʻqituvchisi, sinf rahbari, sizni taniydigan direktor; magistratura uchun professor yoki ilmiy rahbar.</li>
<li>Sizni yaxshi bilish mashhur unvondan muhimroq. Loyihangizni tasvirlab bera oladigan oʻqituvchi siz bilan hech gaplashmagan direktordan qimmatroq.</li>
<li>Qoidalarga amal qiling: GKS bakalavr dasturi oʻqituvchi yoki direktordan, muddatdan oldingi bir yil ichidagi sana bilan tavsiyanoma soʻraydi.</li>
</ul>

<h2>Qanday soʻrash kerak</h2>
<ol class="ab-steps">
<li><strong>Erta soʻrang</strong> — kerak boʻlishidan kamida bir oy oldin. Oʻqituvchilar band.</li>
<li><strong>Yuzma-yuz soʻrang</strong>, keyin tafsilotlarni yozma yuboring.</li>
<li><strong>Ularga «yutuqlar varagʻi»ni bering</strong> — ishini osonlashtiradigan bir sahifa (pastda).</li>
<li><strong>Shaklni bering</strong>, agar stipendiyada boʻlsa, va muddatni.</li>
<li><strong>Rahmat ayting</strong> — va natija qanday boʻlmasin, xabar bering.</li>
</ol>

<div class="ab-tip"><strong>Yutuqlar varagʻi — tavsiya beruvchiga beriladigan bir sahifa</strong>
<ul>
<li>Nimaga topshiryapsiz va muddat.</li>
<li>Uning fanidan baholaringiz, bilsangiz sinfdagi oʻrningiz.</li>
<li>Uning darsida yoki maktabda qilgan va u eslashi mumkin boʻlgan ikki-uchta ishingiz — sanalari bilan.</li>
<li>U tasdiqlab berishini xohlagan bitta fazilatingiz (qiziquvchanlik, qatʼiyat, yetakchilik) va uni koʻrsatadigan lahza.</li>
<li>Xatlar bir-biriga mos boʻlishi uchun shaxsiy bayonotingizning birinchi qoralamasi.</li>
</ul></div>

<h2>Kuchli tavsiyanomada nima boʻladi</h2>
<ul>
<li>Tavsiya beruvchi sizni qanday va qancha vaqtdan beri taniydi.</li>
<li><strong>Taqqoslash</strong>: «besh yilda dars bergan 120 ta oʻquvchim ichida eng yaxshi uchtasidan biri».</li>
<li>Fazilatni koʻrsatadigan bir-ikkita <strong>voqea</strong>.</li>
<li>Aniq yakuniy tavsiya.</li>
</ul>

<div class="ab-mistake"><strong>Uni oʻzingiz yozib, imzolatmang</strong>
<p>Bu boʻlib turadi va komissiya buni sezadi: xat nomzodning oʻz bayonotiga aynan oʻxshab qoladi. Agar oʻqituvchi sizdan qoralama soʻrasa, oʻrniga yutuqlar varagʻini bering va oʻz soʻzlari bilan yozishiga imkon bering — qoidalar ruxsat bersa, hatto oʻzbekcha, tasdiqlangan tarjima bilan.</p></div>
"""

DOCUMENTS = """
<p>Documents do not win scholarships — but a missing stamp can lose one. Most programmes ask for the same core set, and the slow part is not collecting them: it is <strong>translation and apostille</strong>.</p>

<h2>The core set</h2>
<table>
<tr><th>Document</th><th>Notes</th></tr>
<tr><td>Passport</td><td>Valid well beyond your arrival date. Your English name everywhere must match it exactly.</td></tr>
<tr><td>School certificate (attestat) or diploma</td><td>Or a certificate of expected graduation, if you are still in your final year.</td></tr>
<tr><td>Transcript</td><td>All your grades. If the scholarship uses a different scale, ask the school for an official conversion.</td></tr>
<tr><td>Birth certificate</td><td>Some programmes (GKS among them) use it to prove your parents' citizenship.</td></tr>
<tr><td>Language certificate</td><td>IELTS / TOEFL / TOPIK / JLPT — check the validity window.</td></tr>
<tr><td>Letters</td><td>Personal statement, study plan, recommendation(s), CV.</td></tr>
<tr><td>Photos, medical form</td><td>To the exact size and format asked.</td></tr>
</table>

<h2>Translation and apostille, in plain words</h2>
<p><strong>Translation:</strong> a document in Uzbek or Russian must be translated into English (or the host country's language) by a translator and <strong>certified by a notary</strong>.</p>
<p><strong>Apostille:</strong> an official stamp that tells another country “this document is genuine”. Uzbekistan is a member of the Apostille Convention, so most countries accept an apostille instead of a slower consular legalisation. For education documents the request is made through <strong>my.gov.uz</strong>, and an issued apostille can be checked at <strong>apostille.davxizmat.uz</strong>.</p>
<div class="ab-mistake"><strong>Not every country accepts it</strong>
<p>When Uzbekistan joined the Convention in 2012, Germany, Austria and Greece objected, and those objections still stand — so for these three countries an Uzbek apostille is <em>not</em> enough and documents need consular legalisation instead. (Belgium withdrew its objection in 2025.) Check your target country before you start.</p>
<p class="ab-src">Source: HCCH status table of the Apostille Convention, checked 1 October 2026.</p></div>
<div class="ab-fact"><strong>Which gets the apostille — the original or the translation?</strong>
<p>It depends on the programme. GKS accepts either: the apostille may go on the original or on the certified translation. Read your programme's rule before you pay for anything.</p></div>

<div class="ab-mistake"><strong>The timeline trap</strong>
<p>An apostille takes weeks, not days, and you may need several: one set for the application, one for the university, one for the visa. Order <strong>more than one</strong> apostilled copy of your school certificate — GKS itself advises scholars to prepare multiple copies before leaving.</p></div>

<h2>Small things that cause big delays</h2>
<ul>
<li>A name spelled two ways (Madina / Madinа with a Cyrillic “а”, or a different transliteration of your surname).</li>
<li>Documents smaller than A4 — attach them to an A4 sheet.</li>
<li>Files uploaded in the wrong order or without the number the guidelines ask for.</li>
<li>A recommendation letter dated more than a year ago.</li>
</ul>
<p>Use <em>My checklist</em> to tick each document as it becomes ready.</p>
"""

DOCUMENTS_UZ = """
<p>Hujjatlar stipendiyani yutib bermaydi — lekin yetishmagan bitta muhr uni boy berishi mumkin. Koʻp dasturlar bir xil asosiy toʻplamni soʻraydi, va sekin qismi ularni yigʻish emas: <strong>tarjima va apostil</strong>.</p>

<h2>Asosiy toʻplam</h2>
<table>
<tr><th>Hujjat</th><th>Izoh</th></tr>
<tr><td>Pasport</td><td>Kelish sanangizdan ancha keyingacha amal qilsin. Inglizcha ismingiz hamma joyda unga aynan mos boʻlishi kerak.</td></tr>
<tr><td>Attestat yoki diplom</td><td>Yoki bitiruv sinfida boʻlsangiz, tugatish arafasida ekanlik haqida maʼlumotnoma.</td></tr>
<tr><td>Baholar varaqasi</td><td>Barcha baholaringiz. Stipendiya boshqa shkaladan foydalansa, maktabdan rasmiy qayta hisob soʻrang.</td></tr>
<tr><td>Tugʻilganlik haqida guvohnoma</td><td>Baʼzi dasturlar (GKS ham) ota-onangiz fuqaroligini shu bilan tasdiqlaydi.</td></tr>
<tr><td>Til sertifikati</td><td>IELTS / TOEFL / TOPIK / JLPT — amal qilish muddatini tekshiring.</td></tr>
<tr><td>Xatlar</td><td>Shaxsiy bayonot, oʻqish rejasi, tavsiyanoma(lar), CV.</td></tr>
<tr><td>Rasmlar, tibbiy shakl</td><td>Aynan soʻralgan oʻlcham va formatda.</td></tr>
</table>

<h2>Tarjima va apostil — oddiy qilib</h2>
<p><strong>Tarjima:</strong> oʻzbek yoki rus tilidagi hujjat tarjimon tomonidan ingliz tiliga (yoki qabul qiluvchi davlat tiliga) tarjima qilinishi va <strong>notarius tomonidan tasdiqlanishi</strong> kerak.</p>
<p><strong>Apostil:</strong> boshqa davlatga «bu hujjat haqiqiy» deb aytadigan rasmiy muhr. Oʻzbekiston Apostil konvensiyasi aʼzosi, shuning uchun koʻp davlatlar sekinroq konsullik legalizatsiyasi oʻrniga apostilni qabul qiladi. Taʼlim hujjatlari uchun ariza <strong>my.gov.uz</strong> orqali beriladi, qoʻyilgan apostilni esa <strong>apostille.davxizmat.uz</strong> saytida tekshirish mumkin.</p>
<div class="ab-mistake"><strong>Uni hamma davlat ham qabul qilmaydi</strong>
<p>Oʻzbekiston 2012-yilda konvensiyaga qoʻshilganda Germaniya, Avstriya va Gretsiya eʼtiroz bildirgan va bu eʼtirozlar hozir ham kuchda — shu uch davlat uchun oʻzbek apostili <em>yetarli emas</em>, hujjatlarga konsullik legalizatsiyasi kerak. (Belgiya 2025-yilda eʼtirozini qaytarib oldi.) Boshlashdan oldin maqsad davlatingizni tekshiring.</p>
<p class="ab-src">Manba: Apostil konvensiyasining HCCH holat jadvali, 2026-yil 1-oktabrda tekshirilgan.</p></div>
<div class="ab-fact"><strong>Apostil qayerga qoʻyiladi — aslgami yoki tarjimagami?</strong>
<p>Dasturga bogʻliq. GKS ikkalasini ham qabul qiladi: apostil asl nusxaga yoki tasdiqlangan tarjimaga qoʻyilishi mumkin. Pul toʻlashdan oldin dasturingiz qoidasini oʻqing.</p></div>

<div class="ab-mistake"><strong>Vaqt tuzogʻi</strong>
<p>Apostil kunlar emas, haftalar oladi, va sizga bir nechta kerak boʻlishi mumkin: biri ariza uchun, biri universitet uchun, biri viza uchun. Attestatingizning <strong>bir nechta</strong> apostilli nusxasini buyurtma qiling — GKSning oʻzi ham stipendiatlarga ketishdan oldin bir nechta nusxa tayyorlashni maslahat beradi.</p></div>

<h2>Katta kechikishga sabab boʻladigan mayda narsalar</h2>
<ul>
<li>Ikki xil yozilgan ism (Madina / kirillcha «а» bilan Madinа yoki familiyaning boshqacha transliteratsiyasi).</li>
<li>A4 dan kichik hujjatlar — ularni A4 varaqqa yopishtiring.</li>
<li>Notoʻgʻri tartibda yoki yoʻriqnoma soʻragan raqamsiz yuklangan fayllar.</li>
<li>Bir yildan eski sanali tavsiyanoma.</li>
</ul>
<p>Har bir hujjat tayyor boʻlganda uni <em>Mening roʻyxatim</em>da belgilab boring.</p>
"""

GUIDES = [
    {"slug": "start-here", "order": 1, "category": "start", "icon": "bi-signpost-2", "minutes": 4,
     "title": "Start here: the 12-month plan", "title_uz": "Shu yerdan boshlang: 12 oylik reja",
     "summary": "Work backwards from the deadline — almost all the work happens before the form opens.",
     "summary_uz": "Muddatdan orqaga qarab ishlang — ishning deyarli hammasi ariza ochilishidan oldin qilinadi.",
     "body": START, "body_uz": START_UZ},
    {"slug": "personal-statement", "order": 2, "category": "letters", "icon": "bi-pen", "minutes": 6,
     "title": "The personal statement (motivation letter)", "title_uz": "Shaxsiy bayonot (motivatsion xat)",
     "summary": "The only part where the committee hears your voice: a shape that works, and the sentences to never write.",
     "summary_uz": "Komissiya ovozingizni eshitadigan yagona qism: ishlaydigan tuzilma va hech qachon yozilmaydigan gaplar.",
     "body": STATEMENT, "body_uz": STATEMENT_UZ},
    {"slug": "study-plan", "order": 3, "category": "letters", "icon": "bi-calendar3-range", "minutes": 4,
     "title": "The study plan", "title_uz": "Oʻqish rejasi",
     "summary": "Not a second statement: what exactly you will do, year by year — and for a master's, your research question.",
     "summary_uz": "Ikkinchi bayonot emas: yilma-yil aynan nima qilishingiz — magistratura uchun esa tadqiqot savolingiz.",
     "body": STUDY_PLAN, "body_uz": STUDY_PLAN_UZ},
    {"slug": "recommendation-letters", "order": 4, "category": "letters", "icon": "bi-people", "minutes": 4,
     "title": "Recommendation letters", "title_uz": "Tavsiyanomalar",
     "summary": "Whom to ask, how to ask, and the one-page “brag sheet” that makes a teacher's letter specific.",
     "summary_uz": "Kimdan va qanday soʻrash, hamda oʻqituvchi xatini aniq qiladigan bir sahifalik «yutuqlar varagʻi».",
     "body": RECOMMENDATION, "body_uz": RECOMMENDATION_UZ},
    {"slug": "documents", "order": 5, "category": "documents", "icon": "bi-folder2-open", "minutes": 5,
     "title": "Documents, translation and apostille", "title_uz": "Hujjatlar, tarjima va apostil",
     "summary": "The core set every programme asks for — and why the apostille must be started months early.",
     "summary_uz": "Har bir dastur soʻraydigan asosiy toʻplam — va nega apostilni oylar oldin boshlash kerak.",
     "body": DOCUMENTS, "body_uz": DOCUMENTS_UZ},
]
