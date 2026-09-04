# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 61–65 (Blok C ning yakuni).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan.

⚠️ Blok C yakunlanadi. SAT-61 va SAT-62 da hisoblash deyarli yoʻq — faqat
   xulosaning oʻrinliligi. SAT-62 kursdagi yagona dars boʻlib, unda SABAB
   haqida xulosa chiqarishga ruxsat beriladi.

⚠️ Kumulyativ (SAT-1…60 erkin: foiz, jadval, oʻrtacha, ogʻish, ehtimollik,
   tanlanma):
  • SAT-61 — tanlanma ogʻishining turlari va xulosaning chegarasi.
  • SAT-62 — tajriba dizayni: tasodifiy TAQSIMLASH sababga yoʻl ochadi.
  • SAT-63 — xatolik chegarasi va ishonch oraliqlari.
  • SAT-64 — quti diagramma va gistogramma; IQR va qiyshiqlik.
  • SAT-65 — maʼlumotga qaysi model mos: chiziqli yoki koʻrsatkichli.
  • ⛔ Geometriya (SAT-66 dan) YOʻQ.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_61_65.py \\
        --author=prime --republish
"""

PLAYLIST = {
    "title": "Prime SAT Math",
    "category": "math",
    "description": (
        "Digital SAT matematikasi noldan — 100 dars. Savollar ingliz tilida, "
        "chunki test shunday; tushuntirish oʻzbek tilida, chunki oʻqituvchi shunday. "
        "Har bir darsda haqiqiy SAT savollari, tuzoq javoblar va 20 savollik mashq."
    ),
}

TUTORIALS = [

    # ══════════════════════════════════════════════════════════════════
    # SAT-61 — selection bias
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-61: Selection Bias and Generalizing Results",
        "category": "math",
        "order": 61,
        "summary": (
            "Ogʻish tanlanma olinganda paydo boʻladi, hisoblanganda emas. "
            "Uni tuzatish uchun keyinroq hech qanday amal yoʻq."
        ),
        "stories": ["Where the Bullet Holes Were Not"],
        "content": """
<h2>SAT-61: Selection Bias and Generalizing Results</h2>

<p>SAT-60 da tasodifiylik nima berishini koʻrdik. Endi teskarisiga qaraymiz:
<mark>tanlanma notoʻgʻri olinganda aynan nima buziladi</mark>. Va eng muhim
fakt shu — buzilish <b>tanlash paytida</b> sodir boʻladi, va keyin uni
tuzatadigan hech qanday hisob yoʻq.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ogʻishning toʻrt asosiy turini nomlaysiz;</li>
    <li>savolda qaysi turi borligini bir oʻqishda topasiz;</li>
    <li>xulosa qaysi guruh bilan chegaralanishini aytasiz;</li>
    <li>«hajmni oshirish yordam beradi» degan javobni oʻchirasiz.</li>
  </ul>
</div>

<h3>Toʻrt tur</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Turi</th><th>Nima boʻlgan</th><th>Misol</th></tr>
  <tr><td>self-selection</td><td class="pm-word__sym">odamlar oʻzini tanlagan</td>
      <td>eʼlonga javob berganlar</td></tr>
  <tr><td>convenience</td><td class="pm-word__sym">qulay boʻlgani olingan</td>
      <td>koridordagi birinchi 50 kishi</td></tr>
  <tr><td>undercoverage</td><td class="pm-word__sym">bir guruh roʻyxatga tushmagan</td>
      <td>faqat telefoni borlar</td></tr>
  <tr><td>non-response</td><td class="pm-word__sym">tanlanganlarning koʻpi javob bermagan</td>
      <td>1,000 dan 40 tasi javob bergan</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Toʻrttasining ham natijasi bir xil: <b>tanlanmadagi odamlar boshqa guruhdan
  tizimli ravishda farq qiladi</b>. Farq tasodifiy emas, yoʻnalishi bor — va
  aynan shu narsa uni tuzatib boʻlmaydigan qiladi.
</div>

<h3>Javob berganlar ham tanlanmadir</h3>

<p>Bu eng koʻp eʼtibordan qoladigan tur. Ming kishiga soʻrovnoma yuborilib,
qirq kishi javob bersa, tanlanma sizniki emas — <b>javob berish qarorini
qabul qilganlarniki</b>. Va odatda javob beradiganlar mavzuga qiziqishi
kuchli boʻlganlar.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Ogʻishni <b>hajm bilan tuzatib boʻlmaydi</b>. Yomon tanlangan 100 kishilik
  tanlanma ham, 100,000 kishilik tanlanma ham bir xil yoʻnalishda xato beradi
  — faqat ikkinchisi ishonarliroq koʻrinadi.
</div>

<h3>Xulosaning chegarasi</h3>

<p>Toʻgʻri tanlangan tanlanmada ham xulosa <b>tanlanma olingan guruh</b> bilan
chegaralanadi. Bitta maktabdan olingan tasodifiy tanlanma — bitta maktab
haqida; bitta viloyatdan olingani — bitta viloyat haqida.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Savolni oʻqiganda <b>ikkita guruhni belgilang</b>: tanlanma <em>qayerdan</em>
  olingan, va javob <em>kim haqida</em> gapiryapti. Ikkalasi bir xil boʻlmasa,
  javob notoʻgʻri — hisoblashsiz.
</div>

<h3>Savolning shakli ham ogʻish beradi</h3>

<p>«Do you support the excellent new library plan?» degan savol
«Do you support the new library plan?» dan boshqa javob oladi. SAT buni
kamroq soʻraydi, lekin «which of the following would most improve the
survey» turidagi savolda javob koʻpincha aynan shu boʻladi.</p>

<h3>Ogʻishning yoʻnalishini aytish</h3>

<p>SAT baʼzan «natija haqiqiy qiymatdan yuqorimi yoki pastmi?» deb soʻraydi.
Bunda ogʻishning <b>yoʻnalishini</b> oʻylash kerak, kattaligini emas.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Vaziyat</th><th>Natija qaysi tomonga ogʻadi</th></tr>
  <tr><td>kutubxonadagilardan «koʻp oʻqiysizmi» deb soʻralsa</td>
      <td class="pm-word__sym">yuqoriga</td></tr>
  <tr><td>faqat mashinasi borlardan «jamoat transporti kerakmi» deb soʻralsa</td>
      <td class="pm-word__sym">pastga</td></tr>
  <tr><td>faqat shikoyat qilganlardan xizmat soʻralsa</td>
      <td class="pm-word__sym">pastga</td></tr>
</table></div>

<p>Har uchala holatda ham savol bitta: <b>tanlanmadagi odamlar qaysi tomonga
qiyshaygan?</b> Javob shu yoʻnalishda boʻladi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>selection bias</b><span>tanlanma ogʻishi</span></li>
  <li><b>self-selected</b><span>oʻzini tanlagan</span></li>
  <li><b>non-response</b><span>javob bermaslik</span></li>
  <li><b>which conclusion is appropriate</b><span>qaysi xulosa oʻrinli</span></li>
  <li><b>would most improve the study</b><span>tadqiqotni eng yaxshilaydi</span></li>
  <li><b>representative of</b><span>… ni vakillik qiladi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A magazine mails a questionnaire to 5,000 readers and 300 reply. Of those,
    80% say they read every issue. What is the main problem with concluding that
    80% of readers read every issue?</p>
  </div>
  <ol class="ps-ch">
    <li>The 300 who replied are likely the most engaged readers</li>
    <li>300 is too small a number to work with</li>
    <li>The percentage should have been rounded</li>
    <li>There is no problem with the conclusion</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A</p>
      <p>Javob berish — qaror, va u tasodifiy emas. Jurnalni doim oʻqiydiganlar
      javob berishga koʻproq moyil.</p>
      <p>Muammo hajmda emas: 3,000 kishi javob berganda ham bir xil ogʻish
      qolardi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">300 is too small a number</span>
  <span class="ps-trap__why">Hajm bu yerda muammo emas. SAT bu variantni
  deyarli har bir ogʻish savolida qoʻyadi, chunki u tabiiy tuyuladi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>A researcher surveys a random sample of members of one sports club about
    exercise habits. Which conclusion is most appropriate?</p>
  </div>
  <ol class="ps-ch">
    <li>The results describe the members of that club</li>
    <li>The results describe all adults in the city</li>
    <li>The results describe all people who exercise</li>
    <li>No conclusion is possible</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A</p>
      <p>Tanlanma tasodifiy — demak xulosa mumkin, lekin faqat klub aʼzolari
      haqida.</p>
      <p>Klub aʼzolari shahar aholisining vakili emas: ular allaqachon sport
      bilan shugʻullanishni tanlagan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">No conclusion is possible</span>
  <span class="ps-trap__why">Juda ehtiyotkor javob ham notoʻgʻri boʻladi.
  Tanlanma tasodifiy olingan — u <b>oʻz guruhi</b> haqida toʻliq
  ishonchli.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ogʻish savollarida ikkita variant deyarli har doim oʻchadi:</p>
  <ol>
    <li>«The sample was too small» — hajm kamdan-kam asosiy muammo;</li>
    <li>«No conclusion is possible» — tasodifiy tanlanmada xulosa bor;</li>
    <li>Qolganidan tanlashda <b>ikki guruhni</b> solishtiring.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Javob berganlar kam — tanlanmani kattalashtiramiz</p>
  <p class="pe-good">Javob berish qarorining oʻzi ogʻish beradi</p>
  <p class="pe-fix__why">Koʻproq yuborish koʻproq shunday odamni keltiradi,
  xolos.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Bitta klubdan tasodifiy tanlanma → shahar haqida xulosa</p>
  <p class="pe-good">Faqat klub aʼzolari haqida</p>
  <p class="pe-fix__why">Tasodifiylik guruh ichida ishlaydi, guruhdan
  tashqarida emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ogʻishni <b>tasodifiy xatodan</b> ajrating. Tasodifiy xato ikki tomonga
  ham ketadi va katta tanlanmada kamayadi; ogʻish esa bitta yoʻnalishga
  ketadi va kamaymaydi. Shuning uchun ular butunlay boshqa muammo.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Tadqiqotni nima yaxshilaydi?» degan savolda toʻgʻri javob deyarli har doim
  <b>tanlash usulini</b> oʻzgartiradi: roʻyxatdan tasodifiy tanlash, hamma
  guruhni qamrash, javob bermaganlarni qayta soʻrash. Hisob usulini
  oʻzgartiradigan javoblar emas.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A survey is answered only by people who saw a poster about it. What type of
  bias is this?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Self-selection — odamlar oʻzini tanlagan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  A survey of a town uses only landline telephone numbers. What type of bias is
  this?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Undercoverage — telefoni yoʻqlar roʻyxatga
  tushmagan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A researcher interviews the first 30 people leaving a building. What type of
  bias is this?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Convenience — qulay boʻlgani uchun
  tanlangan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Does increasing a biased sample from 500 to 5,000 reduce the bias?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — ogʻish tanlash usulida, hajmda emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A random sample of one factory's workers is surveyed. To whom do the results
  apply?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Faqat oʻsha zavod ishchilariga.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>selection bias</b><span>tanlanma ogʻishi</span></li>
  <li><b>self-selected</b><span>oʻzini tanlagan</span></li>
  <li><b>convenience sample</b><span>qulaylik tanlanmasi</span></li>
  <li><b>undercoverage</b><span>qamrovning yetishmasligi</span></li>
  <li><b>non-response</b><span>javob bermaslik</span></li>
  <li><b>systematically different</b><span>tizimli ravishda farqli</span></li>
  <li><b>generalize</b><span>umumlashtirmoq</span></li>
  <li><b>representative</b><span>vakillik qiluvchi</span></li>
  <li><b>would most improve</b><span>eng koʻp yaxshilaydi</span></li>
  <li><b>leading question</b><span>yoʻnaltiruvchi savol</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Ogʻish <b>tanlash paytida</b> paydo boʻladi va keyin
        tuzatilmaydi.</li>
    <li><b>Javob berganlar ham tanlanma</b> — javob berish qarordir.</li>
    <li>Tasodifiy tanlanmada ham xulosa <b>oʻz guruhi</b> bilan
        chegaralanadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-62 — experimental design
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-62: Experimental Design — Random Assignment and Cause-and-Effect",
        "category": "math",
        "order": 62,
        "summary": (
            "Butun kursda sababni isbotlashga ruxsat beradigan yagona narsa — "
            "tasodifiy TAQSIMLASH. Tasodifiy tanlash bunga yetmaydi."
        ),
        "stories": ["Twelve Sailors, Six Pairs"],
        "content": """
<h2>SAT-62: Experimental Design — Random Assignment and Cause-and-Effect</h2>

<p>SAT-54 dan beri har bir darsda «bogʻliqlik sabab emas» deb takrorladik. Bu
darsda nihoyat <mark>istisno</mark> keladi: tasodifiy <b>taqsimlash</b> bor
tajribada sabab haqida xulosa chiqarish mumkin.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>tasodifiy tanlash va tasodifiy taqsimlashni ajratasiz;</li>
    <li>toʻrtta kombinatsiyani jadvaldan oʻqiysiz;</li>
    <li>kuzatuv va tajribani farqlaysiz;</li>
    <li>nazorat guruhi nima uchun kerakligini tushuntirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two different randomisations</span>
  <span class="pe-chip pe-chip--v">tanlash → umumlashtirish</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">taqsimlash → sabab</span>
</div>

<h3>Toʻrtta kombinatsiya</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Tasodifiy tanlash</th><th>Tasodifiy taqsimlash</th><th>Nima aytish mumkin</th></tr>
  <tr><td>bor</td><td>bor</td>
      <td class="pm-word__sym">sabab, va butun guruhga</td></tr>
  <tr><td>yoʻq</td><td>bor</td>
      <td class="pm-word__sym">sabab, lekin faqat qatnashchilar uchun</td></tr>
  <tr><td>bor</td><td>yoʻq</td>
      <td class="pm-word__sym">bogʻliqlik, butun guruhga</td></tr>
  <tr><td>yoʻq</td><td>yoʻq</td>
      <td class="pm-word__sym">faqat shu odamlarda bogʻliqlik</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkinchi qator SAT'da eng koʻp uchraydi. Koʻngillilar orasida oʻtkazilgan,
  lekin ular ikki guruhga <b>tasodifiy boʻlingan</b> tajriba — sababni
  koʻrsatadi, lekin faqat shunday koʻngillilar haqida. Ikki huquq alohida
  keladi.
</div>

<h3>Nima uchun taqsimlash ishlaydi</h3>

<p>Qatnashchilar oʻzlari tanlaganda ikki guruh boshidanoq farq qiladi:
dorini tanlaganlar koʻproq qaygʻuradigan odamlar boʻlishi mumkin. Tanga
tashlab boʻlinganda esa yosh, salomatlik, odat — hammasi <b>oʻrtacha
teng</b> taqsimlanadi, va yagona tizimli farq tadqiqotchi qoʻygan farq
boʻlib qoladi.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Savolda <b>«assigned»</b> va <b>«chose»</b> soʻzlarini qidiring. «Participants
  were randomly assigned» — sabab mumkin. «Participants who chose to take» —
  sabab mumkin emas. Bu bitta soʻz butun javobni hal qiladi.
</div>

<h3>Nazorat guruhi</h3>

<p>Nazorat guruhi taqqoslash uchun kerak: usiz «yaxshilandi» degan gap nimaga
nisbatan ekani nomaʼlum qoladi. Koʻp odam davolanmasa ham yaxshilanadi, va
koʻp odam <b>hech qanday taʼsiri yoʻq</b> dori olganda ham oʻzini yaxshi his
qiladi — shuning uchun nazorat guruhiga koʻpincha shunday dori beriladi va
kim nimani olayotganini bilmaydi.</p>

<h3>Koʻr sinov</h3>

<p>Tajribaning yana bir qismi — kim nimani olayotganini
<b>bilmasligi</b>. Bemor bilmasa, uning kutishi natijaga taʼsir qilmaydi;
oʻlchayotgan shifokor ham bilmasa, uning kutishi baholashga taʼsir
qilmaydi.</p>

<p>SAT buni odatda toʻgʻridan-toʻgʻri soʻramaydi, lekin «which of the
following would most improve the experiment» degan savolda javob koʻpincha
shu boʻladi — yoki nazorat guruhini qoʻshish, yoki taqsimlashni tasodifiy
qilish, yoki kim nimani olayotganini yashirish.</p>

<p>Yana bir ehtiyot chora — <b>guruhlar hajmi</b>. Ikki guruh juda kichik
boʻlsa, farq tasodifdan ham kelib chiqishi mumkin. Shuning uchun tajriba
natijasi ikki narsani talab qiladi: tasodifiy taqsimlash va yetarli
qatnashchi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>randomly assigned to two groups</b><span>ikki guruhga tasodifiy taqsimlangan</span></li>
  <li><b>randomly selected from</b><span>… dan tasodifiy tanlangan</span></li>
  <li><b>control group</b><span>nazorat guruhi</span></li>
  <li><b>observational study</b><span>kuzatuv tadqiqoti — sabab yoʻq</span></li>
  <li><b>it is appropriate to conclude</b><span>xulosa chiqarish oʻrinli</span></li>
  <li><b>caused</b><span>keltirib chiqardi — faqat tajribada</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>Two hundred volunteers were randomly assigned to two groups. One group
    used a new study method; the other did not. The first group's scores improved
    more. Which conclusion is most appropriate?</p>
  </div>
  <ol class="ps-ch">
    <li>The method caused higher scores for volunteers like these</li>
    <li>The method causes higher scores for all students</li>
    <li>The method is associated with higher scores, but no cause can be claimed</li>
    <li>No conclusion is possible</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A</p>
      <p>Tasodifiy <b>taqsimlash</b> bor — demak sabab haqida gapirish mumkin.
      Lekin qatnashchilar koʻngillilar edi, tasodifiy tanlanmagan.</p>
      <p>Shuning uchun xulosa «shunday koʻngillilar uchun» deb
      chegaralanadi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">The method causes higher scores for all students</span>
  <span class="ps-trap__why">Sabab toʻgʻri, guruh notoʻgʻri. Taqsimlash sababni
  beradi; umumlashtirish uchun tasodifiy <b>tanlash</b> kerak edi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>Researchers compared people who chose to walk to work with people who
    chose to drive, and found the walkers were healthier. Which conclusion is
    most appropriate?</p>
  </div>
  <ol class="ps-ch">
    <li>Walking to work is associated with better health</li>
    <li>Walking to work causes better health</li>
    <li>Better health causes walking</li>
    <li>The study proves nothing about anyone</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A</p>
      <p>Odamlar oʻzlari tanlagan — bu kuzatuv tadqiqoti, taqsimlash yoʻq.</p>
      <p>Uchinchi omillar koʻp: yashash joyi, daromad, allaqachon sogʻlom
      boʻlish. Ularning hech biri chetlatilmagan.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Better health causes walking</span>
  <span class="ps-trap__why">Sababni <b>teskari</b> yoʻnalishda daʼvo qilish
  ham daʼvodir. Kuzatuv tadqiqoti hech bir yoʻnalishni koʻrsata
  olmaydi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Har bir xulosa savolida bitta soʻzni qidiring:</p>
  <ol>
    <li><b>«assigned»</b> bor → «causes» degan javob mumkin;</li>
    <li><b>«chose»</b>, «who already», «observed» → faqat «associated
        with»;</li>
    <li>Keyin guruhga qarang: koʻngillilarmi yoki tasodifiy tanlanmami.</li>
  </ol>
  <p>Ikki tekshiruv — ikki huquq. Ular alohida keladi va alohida
  yoʻqoladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Koʻngillilar tasodifiy taqsimlangan → hamma uchun sabab</p>
  <p class="pe-good">Faqat shunday koʻngillilar uchun sabab</p>
  <p class="pe-fix__why">Taqsimlash sababni beradi, umumlashtirishni
  emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Odamlar oʻzi tanlagan → sabab</p>
  <p class="pe-good">Faqat bogʻliqlik</p>
  <p class="pe-fix__why">Tanlash qarori guruhlarni boshidanoq
  farqlantiradi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Nazorat guruhi <b>hech narsa qilmaydigan</b> guruh emas — u aynan shunday
  koʻrinadigan, lekin taʼsirsiz narsani oladigan guruh. Aks holda farq
  dorining oʻzidanmi yoki «meni davolashyapti» degan hisdanmi — bilib
  boʻlmaydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Baʼzi savollarda tajriba oʻtkazish <b>mumkin emas</b>: chekishning zararini
  odamlarni tasodifiy chektirib tekshirib boʻlmaydi. Bunday hollarda faqat
  kuzatuv qoladi, va xulosa ehtiyotkorroq boʻlishi shart.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Which randomisation allows a conclusion about cause?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Tasodifiy taqsimlash (random assignment).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Which randomisation allows generalizing to a wider group?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Tasodifiy tanlash (random selection).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A study compares people who already take a vitamin with people who do not.
  What kind of study is this?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Kuzatuv tadqiqoti — sabab haqida xulosa
  chiqarilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Why is a control group needed?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Taqqoslash uchun — usiz «yaxshilandi» nimaga
  nisbatan ekani nomaʼlum.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A random sample of a city's residents is randomly assigned to two groups in an
  experiment. What can be concluded?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Sabab haqida, va butun shahar aholisi haqida — ikkala
  huquq ham bor.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>random assignment</b><span>tasodifiy taqsimlash</span></li>
  <li><b>random selection</b><span>tasodifiy tanlash</span></li>
  <li><b>control group</b><span>nazorat guruhi</span></li>
  <li><b>treatment group</b><span>taʼsir guruhi</span></li>
  <li><b>observational study</b><span>kuzatuv tadqiqoti</span></li>
  <li><b>experiment</b><span>tajriba</span></li>
  <li><b>volunteers</b><span>koʻngillilar</span></li>
  <li><b>confounding variable</b><span>chalkashtiruvchi omil</span></li>
  <li><b>appropriate to conclude</b><span>xulosa chiqarish oʻrinli</span></li>
  <li><b>assigned vs chose</b><span>taqsimlangan / oʻzi tanlagan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Tasodifiy <b>taqsimlash</b> sababni beradi; tasodifiy <b>tanlash</b>
        umumlashtirishni.</li>
    <li>«Assigned» va «chose» — bitta soʻz, ikki boshqa xulosa.</li>
    <li>Ikki huquq <b>alohida</b>: biri boʻlmasa, ikkinchisi
        yoʻqolmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-63 — margin of error
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-63: Margin of Error and Confidence Intervals",
        "category": "math",
        "order": 63,
        "summary": (
            "Natija bitta son emas, oraliq. Kattaroq tanlanma oraliqni "
            "toraytiradi, yuqoriroq ishonch esa kengaytiradi."
        ),
        "stories": ["Two Percent, Give or Take"],
        "content": """
<h2>SAT-63: Margin of Error and Confidence Intervals</h2>

<p>SAT-60 da oraliq gʻoyasini koʻrdik. Endi uni toʻliq ochamiz, chunki SAT
undan uch xil savol yasaydi: <mark>oraliqni hisoblash, uni oʻqish va nima
uni toraytirishini bilish</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>oraliqni bir qadamda yozasiz;</li>
    <li>nima uni toraytirishini va nima kengaytirishini bilasiz;</li>
    <li>ikki oraliq kesishsa nima deyish mumkinligini aytasiz;</li>
    <li>xatolik chegarasi nimani <b>qamramasligini</b> bilasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The interval</span>
  <span class="pe-chip pe-chip--v">natija − chegara</span>
  <span class="pe-op">…</span>
  <span class="pe-chip pe-chip--s">natija + chegara</span>
</div>

<h3>Oraliqni yozish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">52 foiz, xatolik chegarasi 3 foiz</span>
    <span class="pm-solve__why">Ikki tomonga ham 3 dan</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">49 foizdan 55 foizgacha</span>
    <span class="pm-solve__why">Oraliqning kengligi 6 — chegaraning ikki barobari</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oraliq «haqiqiy qiymat shu yerda» degani emas — u «shu yerda boʻlishi
  <b>ehtimoli katta</b>» degani. SAT javob variantlarida «definitely» yoki
  «must be» degan soʻzlar boʻlsa, ular deyarli har doim notoʻgʻri.
</div>

<h3>Nima oraliqni oʻzgartiradi</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Oʻzgarish</th><th>Oraliqqa taʼsiri</th></tr>
  <tr><td>tanlanma hajmi oshadi</td><td class="pm-word__sym">torayadi</td></tr>
  <tr><td>ishonch darajasi oshadi (95 dan 99 ga)</td><td class="pm-word__sym">kengayadi</td></tr>
  <tr><td>tanlanma ogʻishgan</td><td class="pm-word__sym">hech qanday — u boshqa muammo</td></tr>
</table></div>

<p>Uchinchi qator eng muhimi. <b>Xatolik chegarasi faqat tasodifiy
oʻzgaruvchanlikni qamraydi.</b> Tanlanma notoʻgʻri olingan boʻlsa, oraliq
tor boʻlishi mumkin va baribir notoʻgʻri joyda turadi.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  «Margin of error 2 foiz, demak natija juda aniq» degan xulosa faqat
  <b>tasodifiy tanlanmada</b> oʻrinli. Ogʻishgan tanlanmada tor oraliq —
  ishonchning emas, xavfning belgisi.
</div>

<h3>Ikki oraliqni taqqoslash</h3>

<p>Ikki natijaning oraliqlari <b>kesishsa</b>, farqni ishonchli deb boʻlmaydi
— haqiqiy qiymatlar teng boʻlishi ham mumkin. Kesishmasa, farq
haqiqiy.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">A: 47 foiz ± 4  →  43 dan 51 gacha</span>
    <span class="pm-solve__why">Birinchi nomzod</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">B: 50 foiz ± 4  →  46 dan 54 gacha</span>
    <span class="pm-solve__why">Ikkinchi nomzod</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">46 dan 51 gacha ikkalasiga ham tegishli</span>
    <span class="pm-solve__why">Kesishadi — yetakchini aytib boʻlmaydi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Bunday savolda ikkala oraliqni <b>yozib qoʻying</b>, keyin qarang: bittasining
  yuqori chegarasi ikkinchisining quyi chegarasidan katta boʻlsa, ular
  kesishadi. Bu ikki ayirish va bitta taqqoslash — 20 soniyalik ish.
</div>

<h3>Oraliqdan natijani qaytarish</h3>

<p>Savol teskari tomonga ham beriladi: oraliq berilib, natija va chegara
soʻraladi. Ikkalasi ham bitta qadamda chiqadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Oraliq: 44 foizdan 52 foizgacha</span>
    <span class="pm-solve__why">Kengligi 8</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Natija = oʻrtasi = (44 + 52) ÷ 2 = 48</span>
    <span class="pm-solve__why">Oraliq har doim natija atrofida simmetrik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Chegara = kenglikning yarmi = 4</span>
    <span class="pm-solve__why">Tekshiruv: 48 − 4 = 44 va 48 + 4 = 52 ✓</span>
  </div>
</div>

<p>Diqqat qiling: xatolik chegarasi <b>foizda</b> berilsa, u foiz
punktlarida oʻlchanadi. «52 foiz, chegara 3 foiz» degani 52 ning 3 foizi
(1.56) emas, balki 3 <b>punkt</b> — yaʼni 49 dan 55 gacha. Bu SAT'da
tez-tez chalkashtiriladi.</p>

<p>Nihoyat, chegara <b>butun sonlar</b> haqida ham beriladi, faqat foiz
emas: «oʻrtacha 42 daqiqa, chegara 5 daqiqa» degani 37 dan 47 gacha. Amal
bir xil — oʻqish esa diqqatliroq boʻlishi kerak, chunki birlik
oʻzgargan.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>margin of error</b><span>xatolik chegarasi</span></li>
  <li><b>confidence interval</b><span>ishonch oraliqi</span></li>
  <li><b>plausible values</b><span>ehtimoliy qiymatlar</span></li>
  <li><b>most likely to reduce the margin of error</b><span>chegarani eng koʻp kamaytiradi</span></li>
  <li><b>the intervals overlap</b><span>oraliqlar kesishadi</span></li>
  <li><b>95 percent confidence</b><span>95 foizli ishonch</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>A poll of a random sample estimates 38% support with a margin of error of
    2.5%. Which interval contains the plausible values?</p>
  </div>
  <ol class="ps-ch">
    <li>35.5% to 40.5%</li>
    <li>38% to 40.5%</li>
    <li>35.5% to 38%</li>
    <li>36% to 40%</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 35.5% to 40.5%</p>
      <p>Ikki tomonga ham 2.5 foizdan.</p>
      <p>Oraliqning kengligi 5 — chegaraning ikki barobari.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">38% to 40.5%</span>
  <span class="ps-trap__why">Chegara faqat bir tomonga qoʻshilgan. U
  <b>ikkala</b> tomonga ham qoʻllanadi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>A researcher wants to reduce the margin of error in a future study. Which
    change is most likely to achieve this?</p>
  </div>
  <ol class="ps-ch">
    <li>Increasing the sample size</li>
    <li>Increasing the confidence level</li>
    <li>Asking simpler questions</li>
    <li>Repeating the same study</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) Increasing the sample size</p>
      <p>Kattaroq tanlanma — kichikroq tasodifiy oʻzgaruvchanlik.</p>
      <p><b>Ishonch darajasini oshirish</b> teskari ishlaydi: 99 foizli
      ishonch 95 foizlidan <b>kengroq</b> oraliq beradi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Increasing the confidence level</span>
  <span class="ps-trap__why">Koʻproq ishonch — koʻproq ehtiyotkorlik, demak
  <b>kengroq</b> oraliq. Ikki narsa teskari yoʻnalishda harakat
  qiladi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Uch qoidani yodda tuting:</p>
  <ol>
    <li>Oraliq = natija <b>± chegara</b>, kengligi chegaraning ikki
        barobari;</li>
    <li>Hajm oshsa <b>torayadi</b>, ishonch oshsa <b>kengayadi</b>;</li>
    <li>Kesishgan oraliqlar farqni <b>isbotlamaydi</b>.</li>
  </ol>
  <p>Va tortdan tashqari: chegara ogʻishni qamramaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">52% ± 3 → 52 dan 55 gacha</p>
  <p class="pe-good">49 dan 55 gacha</p>
  <p class="pe-fix__why">Chegara ikkala tomonga ham qoʻllanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Ishonchni 99 foizga oshirsak oraliq torayadi</p>
  <p class="pe-good">Kengayadi</p>
  <p class="pe-fix__why">Koʻproq ishonch uchun koʻproq qiymatni qamrash
  kerak.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oraliq <b>50 foizni qamrasa</b>, «koʻpchilik qoʻllab-quvvatlaydi» deb
  boʻlmaydi — hatto natija 51 foiz boʻlsa ham. Saylov haqidagi savollarda
  SAT aynan shu xulosani tekshiradi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Chegarani sezilarli kamaytirish uchun tanlanmani <b>bir necha barobar</b>
  oshirish kerak — ikki barobar oshirish chegarani ikki barobar
  kamaytirmaydi. SAT bu nisbatni soʻramaydi, faqat yoʻnalishni biladi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A poll reports 61% with a margin of error of 4%. What is the interval?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">57% dan 65% gacha.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  An interval runs from 44% to 52%. What were the estimate and the margin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">48% va 4% — oʻrtasi va yarim kenglik.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Does raising the confidence level from 95% to 99% widen or narrow the
  interval?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Kengaytiradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Two results are 30% ± 3 and 34% ± 3. Can we say they differ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — 27–33 va 31–37 kesishadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Does a small margin of error mean the sample was well chosen?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — chegara ogʻishni umuman
  oʻlchamaydi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>margin of error</b><span>xatolik chegarasi</span></li>
  <li><b>confidence interval</b><span>ishonch oraliqi</span></li>
  <li><b>confidence level</b><span>ishonch darajasi</span></li>
  <li><b>plausible values</b><span>ehtimoliy qiymatlar</span></li>
  <li><b>overlap</b><span>kesishmoq</span></li>
  <li><b>estimate</b><span>baho, taxminiy qiymat</span></li>
  <li><b>narrow / widen</b><span>toraymoq / kengaymoq</span></li>
  <li><b>random variation</b><span>tasodifiy oʻzgaruvchanlik</span></li>
  <li><b>does not account for</b><span>… ni qamramaydi</span></li>
  <li><b>a majority</b><span>koʻpchilik (50 foizdan koʻp)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Oraliq = natija <b>± chegara</b>, ikkala tomonga ham.</li>
    <li>Hajm oshsa <b>torayadi</b>; ishonch oshsa <b>kengayadi</b>.</li>
    <li>Chegara <b>ogʻishni qamramaydi</b> — u faqat tasodifni
        oʻlchaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-64 — boxplots and histograms
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-64: Comparing Data Sets — Boxplots and Histograms",
        "category": "math",
        "order": 64,
        "summary": (
            "Quti diagramma beshta sonni koʻrsatadi va qutining oʻzi "
            "maʼlumotning oʻrtadagi yarmini qamraydi."
        ),
        "stories": ["The Same Middle, a Different Tail"],
        "content": """
<h2>SAT-64: Comparing Data Sets — Boxplots and Histograms</h2>

<p>Bu dars Blok C ning statistika qismini yakunlaydi. Ikki tasvir bor va
ularning ishi boshqa: <mark>quti diagramma beshta sonni beradi, gistogramma
esa shaklni</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>quti diagrammaning beshta sonini oʻqiysiz;</li>
    <li>qutining oʻzi nimani anglatishini bilasiz;</li>
    <li>IQR ni hisoblaysiz va nima uchun kerakligini aytasiz;</li>
    <li>gistogramma shaklidan oʻrtacha va medianani solishtirasiz.</li>
  </ul>
</div>

<h3>Beshta son</h3>

<p>Maʼlumot: 2, 4, 5, 7, 8, 10, 12, 15, 18, 30 — oʻn ta qiymat, tartiblangan.
Mediana oʻrtadagi ikkitasining oʻrtasi: (8 + 10) ÷ 2 = 9. Pastki yarmining
medianasi 5, yuqori yarmining medianasi 15.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 160" role="img"
       aria-label="Boxplot with minimum 2, lower quartile 5, median 9,
                   upper quartile 15 and maximum 30">
    <line class="pm-ln" x1="40" y1="130" x2="310" y2="130"/>
    <line class="pm-ln" x1="57" y1="60" x2="57" y2="110"/>
    <line class="pm-ln" x1="300" y1="60" x2="300" y2="110"/>
    <line class="pm-ln" x1="57" y1="85" x2="83" y2="85"/>
    <line class="pm-ln" x1="170" y1="85" x2="300" y2="85"/>
    <rect class="pm-fill" x="83" y="60" width="87" height="50"/>
    <line class="pm-ln" x1="118" y1="60" x2="118" y2="110"/>
    <text class="pm-lbl" x="48"  y="126">2</text>
    <text class="pm-lbl" x="78"  y="126">5</text>
    <text class="pm-lbl" x="113" y="126">9</text>
    <text class="pm-lbl" x="164" y="126">15</text>
    <text class="pm-lbl" x="292" y="126">30</text>
    <text class="pm-lbl" x="100" y="52">box = middle half</text>
  </svg>
  <figcaption>Quti 5 dan 15 gacha choʻzilgan; ichidagi chiziq — mediana, 9.
  Oʻng «moʻylov» ancha uzun, chunki 30 boshqalardan uzoqda.</figcaption>
</figure>

<div class="pe-formula">
  <span class="pe-formula__label">The box</span>
  <span class="pe-chip pe-chip--v">IQR = yuqori chorak − pastki chorak</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">15 − 5 = 10</span>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qutining ichida maʼlumotning <b>oʻrtadagi yarmi</b> yotadi — bu yerda 5 dan
  15 gacha. Har bir «moʻylov» esa qolgan chorakdan bittasini koʻrsatadi.
  Demak toʻrtta qism bor va har birida qiymatlarning <b>chorak qismi</b>.
</div>

<h3>Uzun moʻylov nimani anglatadi</h3>

<p>Uzun moʻylov <b>koʻp qiymat</b> degani emas — u shu chorakdagi qiymatlar
keng tarqalgan degani. Yuqoridagi rasmda oʻng moʻylov chapdagisidan uzun,
lekin ikkalasida ham bir xil miqdorda maʼlumot bor: chorakdan bittadan.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Quti diagramma <b>nechta</b> qiymat borligini koʻrsatmaydi. Ikki diagramma
  bir xil koʻrinishi mumkin, lekin biri 20 ta, ikkinchisi 2,000 ta
  qiymatdan tuzilgan boʻlishi mumkin.
</div>

<h3>Gistogramma shakli</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Shakl</th><th>Nomi</th><th>Oʻrtacha va mediana</th></tr>
  <tr><td>oʻngda uzun dum</td><td class="pm-word__sym">skewed right</td>
      <td>oʻrtacha medianadan katta</td></tr>
  <tr><td>chapda uzun dum</td><td class="pm-word__sym">skewed left</td>
      <td>oʻrtacha medianadan kichik</td></tr>
  <tr><td>simmetrik</td><td class="pm-word__sym">symmetric</td>
      <td>taxminan teng</td></tr>
</table></div>

<p>Qoidani yodlash oson: <b>oʻrtacha dum tomonga tortiladi</b>. Chunki
dumdagi bir nechta uzoq qiymat oʻrtachaga sezilarli hissa qoʻshadi,
medianaga esa deyarli yoʻq (SAT-55).</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ikki maʼlumotni taqqoslash savolida <b>tartib bilan</b> qarang: avval
  medianalar, keyin qutilarning kengligi (IQR), keyin chekkalar. Uchta
  taqqoslash — va SAT'ning har qanday savoli shu uchtadan biri
  boʻladi.
</div>

<h3>Ikki diagrammani taqqoslash</h3>

<p>SAT koʻpincha ikkita quti diagrammani yonma-yon beradi va bitta savol
soʻraydi. Javob deyarli har doim shu uchtadan biri boʻladi:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Savol</th><th>Nimaga qarash kerak</th></tr>
  <tr><td>qaysi maʼlumotning markazi yuqori?</td>
      <td class="pm-word__sym">mediana chizigʻining oʻrni</td></tr>
  <tr><td>qaysi biri kengroq tarqalgan?</td>
      <td class="pm-word__sym">qutining kengligi (IQR)</td></tr>
  <tr><td>qaysi birida chetdagi qiymat bor?</td>
      <td class="pm-word__sym">gʻayrioddiy uzun moʻylov</td></tr>
</table></div>

<p>Gistogramma va quti diagramma bir xil maʼlumotdan tuzilishi mumkin,
lekin ular boshqa narsani koʻrsatadi. Gistogramma <b>shaklni</b> beradi —
qayerda toʻplanish bor, nechta choʻqqi bor. Quti diagramma esa
<b>beshta aniq sonni</b> beradi va ikki maʼlumotni yonma-yon qoʻyishga
qulay. Savol shakl haqida boʻlsa gistogrammaga, aniq son haqida boʻlsa
qutiga qarang.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>boxplot / box-and-whisker plot</b><span>quti diagramma</span></li>
  <li><b>interquartile range</b><span>choraklararo oraliq (IQR)</span></li>
  <li><b>the middle 50 percent</b><span>oʻrtadagi 50 foiz — qutining ichi</span></li>
  <li><b>skewed to the right</b><span>oʻngga qiyshaygan</span></li>
  <li><b>which data set has a greater median</b><span>qaysida mediana kattaroq</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>From the boxplot shown, what is the interquartile range?</p>
  </div>
  <ol class="ps-ch">
    <li>10</li>
    <li>28</li>
    <li>9</li>
    <li>15</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 10</p>
      <p>15 − 5 = 10 — qutining kengligi.</p>
      <p><b>28</b> — bu butun oraliq (30 − 2), IQR emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">28</span>
  <span class="ps-trap__why">Oraliq va IQR chalkashtirilgan. Oraliq
  moʻylovning chetidan chetigacha; IQR faqat <b>qutining</b>
  kengligi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>A histogram of house prices has a long tail to the right. What is true
    about the mean and the median?</p>
  </div>
  <ol class="ps-ch">
    <li>The mean is greater than the median</li>
    <li>The median is greater than the mean</li>
    <li>They are equal</li>
    <li>Neither can be found from a histogram</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A</p>
      <p>Oʻrtacha dum tomonga tortiladi, va dum oʻngda.</p>
      <p>Shuning uchun uy narxlari haqidagi hisobotlarda mediana
      ishlatiladi (SAT-55).</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">The median is greater than the mean</span>
  <span class="ps-trap__why">Yoʻnalish teskari olingan. Dum <b>qayerda</b>
  boʻlsa, oʻrtacha oʻsha tomonga tortiladi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Quti diagramma savolida beshta sonni <b>chetiga yozib qoʻying</b>:</p>
  <ol>
    <li>eng kichik, pastki chorak, mediana, yuqori chorak, eng katta;</li>
    <li>IQR = yuqori chorak − pastki chorak;</li>
    <li>oraliq = eng katta − eng kichik.</li>
  </ol>
  <p>Ikki diagramma berilganda ularni yonma-yon yozing — taqqoslash
  savollari darrov ochiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">IQR = 30 − 2 = 28</p>
  <p class="pe-good">IQR = 15 − 5 = 10</p>
  <p class="pe-fix__why">IQR faqat qutining kengligi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Uzun moʻylov — u yerda koʻproq maʼlumot bor</p>
  <p class="pe-good">Har bir moʻylovda chorak qism</p>
  <p class="pe-fix__why">Uzunlik miqdorni emas, tarqoqlikni
  koʻrsatadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  IQR — chetdagi qiymatlarga <b>chidamli</b> oʻlchov: u faqat oʻrtadagi
  yarmiga qaraydi. Shuning uchun maʼlumotda gʻalati qiymat bor deb
  gumon qilinganda oraliq oʻrniga IQR ishlatiladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Gistogramma ustunlari <b>oraliqlarni</b> sanaydi, alohida qiymatlarni
  emas. «10 dan 20 gacha» ustuni 12 ta boʻlsa — bu oʻsha oraliqqa tushgan
  12 ta qiymat, 12 raqami emas.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A boxplot has quartiles 12 and 28. What is the IQR?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">16.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  What fraction of the data lies inside the box?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yarmi — oʻrtadagi 50 foiz.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A histogram has a long tail to the left. Which is larger, the mean or the
  median?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Mediana — oʻrtacha chapga tortilgan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Two boxplots look identical. Must the two data sets have the same number of
  values?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — quti diagramma miqdorni
  koʻrsatmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  In the data 2, 4, 5, 7, 8, 10, 12, 15, 18, 30, what is the median?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">9 — oʻrtadagi ikkitasining oʻrtasi.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>boxplot</b><span>quti diagramma</span></li>
  <li><b>quartile</b><span>chorak</span></li>
  <li><b>interquartile range</b><span>choraklararo oraliq</span></li>
  <li><b>whisker</b><span>moʻylov (chiziqcha)</span></li>
  <li><b>the middle 50 percent</b><span>oʻrtadagi 50 foiz</span></li>
  <li><b>skewed right / left</b><span>oʻngga / chapga qiyshaygan</span></li>
  <li><b>symmetric</b><span>simmetrik</span></li>
  <li><b>tail</b><span>dum (uzun chetki qism)</span></li>
  <li><b>resistant to outliers</b><span>chetdagi qiymatlarga chidamli</span></li>
  <li><b>bin / interval</b><span>oraliq (gistogramma ustuni)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Quti — <b>oʻrtadagi yarim</b>; IQR uning kengligi.</li>
    <li>Uzun moʻylov <b>tarqoqlikni</b> bildiradi, miqdorni emas.</li>
    <li><b>Oʻrtacha dum tomonga tortiladi</b>; mediana joyida
        qoladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-65 — choosing a model from data
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-65: Linear vs. Exponential Data Modeling",
        "category": "math",
        "order": 65,
        "summary": (
            "Blok C ning yakuni: jadval yoki grafik berilganda qaysi model "
            "mos kelishini aniqlash va uni kontekstda oʻqish."
        ),
        "stories": ["Two, Four, and Then What?"],
        "content": """
<h2>SAT-65: Linear vs. Exponential Data Modeling</h2>

<p>SAT-44 da modelni tanidik, SAT-45 da yozdik. Endi Blok C ni yakunlaymiz:
<mark>haqiqiy maʼlumot berilganda qaysi model mos kelishini aniqlash</mark> —
va bu safar sonlar tekis boʻlmasligi mumkin.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>jadvaldan modelni ikki qadamda aniqlaysiz;</li>
    <li>sonlar taxminiy boʻlganda ham qaror qilasiz;</li>
    <li>grafik shaklidan modelni oʻqiysiz;</li>
    <li>modelning chegarasini kontekstda aytasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two steps, always in this order</span>
  <span class="pe-chip pe-chip--v">ayiring</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">boʻling</span>
</div>

<h3>Haqiqiy maʼlumot tekis boʻlmaydi</h3>

<p>Darslikdagi jadvalda nisbatlar aynan 2 ga teng chiqadi. Haqiqiy
maʼlumotda esa 1.98, 2.03, 1.99 boʻlishi mumkin — va bu <b>hali ham</b>
koʻrsatkichli model.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Yil</th><th>Qiymat</th><th>Ayirma</th><th>Nisbat</th></tr>
  <tr><td>0</td><td>200</td><td>—</td><td>—</td></tr>
  <tr><td>1</td><td>238</td><td>38</td><td class="pm-word__sym">1.19</td></tr>
  <tr><td>2</td><td>284</td><td>46</td><td class="pm-word__sym">1.19</td></tr>
  <tr><td>3</td><td>338</td><td>54</td><td class="pm-word__sym">1.19</td></tr>
</table></div>

<p>Ayirmalar oʻsib boradi — demak chiziqli emas. Nisbatlar esa uchala
qadamda ham taxminan 1.19 — demak koʻrsatkichli, yiliga qariyb 19
foiz.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Nisbatlar <b>aynan</b> teng boʻlishini kutmang. Ular bir-biriga yaqin
  boʻlsa yetarli, ayirmalar esa aniq yoʻnalishda oʻzgarayotgan boʻlsa —
  javob koʻrsatkichli.
</div>

<h3>Grafik shaklidan</h3>

<ul>
  <li><b>Toʻgʻri chiziq</b> — chiziqli model;</li>
  <li><b>Yuqoriga egilgan</b>, tobora tikroq — koʻrsatkichli oʻsish;</li>
  <li><b>Pastga egilgan</b>, tobora tekisroq, lekin nolga yetmaydigan —
      koʻrsatkichli kamayish.</li>
</ul>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Koʻrsatkichli kamayish grafigi nolga <b>yaqinlashadi, lekin
  yetmaydi</b>. Chiziqli kamayish esa nolni kesib oʻtadi va manfiy tomonga
  ketadi — bu koʻpincha kontekstda maʼnosiz. Model tanlashda shu farq
  yordam beradi.
</div>

<h3>Modelning chegarasi</h3>

<p>Model <b>maʼlumot toʻplangan oraliqda</b> ishonchli (SAT-54). Bakteriya
soni oʻn soat davomida ikkilanib borgani, uning bir hafta davom etishini
anglatmaydi: oziq tugaydi, joy tugaydi. SAT bu savolni «is this model
appropriate for large values» degan shaklda beradi.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Kontekstga qarang: <b>foiz, ikkilanish, qadrsizlanish</b> — koʻrsatkichli;
  <b>doimiy toʻlov, har birlikka bir xil narx, doimiy tezlik</b> — chiziqli.
  Jadval berilmagan savollarda javob shu soʻzlarda yashiringan.
</div>

<h3>Chiziqli model qanchalik yaxshi mos kelgan</h3>

<p>SAT baʼzan chiziqli modelni beradi va uning maʼlumotga qanchalik mos
kelganini soʻraydi. Buning uchun qoldiqlarga qaraladi (SAT-54): agar ular
bir tomonda musbat, boshqasida manfiy boʻlsa — maʼlumot aslida
<b>egri</b>, va chiziqli model notoʻgʻri tanlangan.</p>

<p>Bu Blok C dagi eng koʻp bogʻlangan gʻoya: model tanlash (SAT-44),
qoldiq (SAT-54) va maʼlumotga moslik (SAT-65) — bir xil savolning uch
koʻrinishi.</p>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>which model best fits the data</b><span>qaysi model maʼlumotga mos</span></li>
  <li><b>increases by a constant factor</b><span>oʻzgarmas koeffitsientga koʻpayadi</span></li>
  <li><b>increases by a constant amount</b><span>oʻzgarmas miqdorga oshadi</span></li>
  <li><b>appropriate for large values of t</b><span>t katta boʻlganda oʻrinlimi</span></li>
  <li><b>approaches zero but never reaches it</b><span>nolga yaqinlashadi, lekin yetmaydi</span></li>
</ul>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>A table shows values 200, 238, 284 and 338 at times 0, 1, 2 and 3. Which
    model best fits the data?</p>
  </div>
  <ol class="ps-ch">
    <li>Exponential, because each value is about 1.19 times the one before</li>
    <li>Linear, because the values increase by about 38 each time</li>
    <li>Linear, because the values increase by about 46 each time</li>
    <li>Neither model fits</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) Exponential</p>
      <p>Ayirmalar 38, 46, 54 — teng emas va oʻsib bormoqda. Nisbatlar esa
      uchala qadamda ham taxminan 1.19.</p>
      <p>Bu yiliga qariyb 19 foizlik oʻsish.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Linear, because the values increase by about 38</span>
  <span class="ps-trap__why">Faqat birinchi ayirma tekshirilgan. Chiziqli
  deyish uchun <b>hamma</b> ayirma taxminan teng boʻlishi kerak.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">55 s</span></p>
  <div class="ps-stem__q">
    <p>A bacteria population doubles every hour and is modelled for the first ten
    hours. Is the model appropriate for predicting the population after two
    weeks?</p>
  </div>
  <ol class="ps-ch">
    <li>No, because the model is only supported over the range of the data</li>
    <li>Yes, because the model is a formula</li>
    <li>Yes, because doubling always continues</li>
    <li>No, because exponential models are never accurate</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A</p>
      <p>Model oʻn soatlik maʼlumot asosida qurilgan. Ikki hafta uning
      chegarasidan juda uzoq.</p>
      <p><b>«Exponential models are never accurate»</b> juda keng —
      ular oʻz oraliqlarida juda aniq ishlaydi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">Yes, because the model is a formula</span>
  <span class="ps-trap__why">Formulaga har qanday sonni qoʻyish mumkin — bu
  javobning maʼnoli boʻlishini anglatmaydi.</span>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Model tanlash savolida uch qadam:</p>
  <ol>
    <li>Ketma-ket ayirmalarni yozing — teng boʻlsa chiziqli, tamom;</li>
    <li>Boʻlmasa nisbatlarni yozing — yaqin boʻlsa koʻrsatkichli;</li>
    <li>Javobning <b>sababi</b>ga qarang: u toʻgʻri hisobga
        asoslanganmi.</li>
  </ol>
  <p>SAT javoblari koʻpincha «Linear, because…» shaklida beriladi va
  sababning oʻzi notoʻgʻri boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Nisbatlar 1.98 va 2.03 — demak koʻrsatkichli emas</p>
  <p class="pe-good">Koʻrsatkichli — nisbatlar yaqin</p>
  <p class="pe-fix__why">Haqiqiy maʼlumot hech qachon aynan tekis
  boʻlmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Model formula, demak istalgan t uchun ishlaydi</p>
  <p class="pe-good">Faqat maʼlumot oraliqida ishonchli</p>
  <p class="pe-fix__why">Ekstrapolatsiya — tekshirilmagan hudud.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kamayishda ham xuddi shu ikki qadam ishlaydi: ayirmalar teng boʻlsa
  chiziqli kamayish, nisbatlar teng boʻlsa koʻrsatkichli. 100, 90, 81, 72.9
  — nisbatlar 0.9, demak koʻrsatkichli.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Blok C shu dars bilan tugaydi. Uning barcha savollarida bitta umumiy
  narsa bor edi: <b>hisoblash oson, jumla qiyin</b>. Keyingi blokda
  geometriya boshlanadi va muvozanat teskari tomonga siljiydi.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Values are 5, 9, 13, 17. Which model fits?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Chiziqli — har safar 4 qoʻshiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Values are 5, 10, 20, 40. Which model fits?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Koʻrsatkichli — nisbat 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Values are 400, 360, 324, 291.6. Which model fits, and at what rate?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Koʻrsatkichli kamayish, nisbat 0.9 — har safar
  10 foizdan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  A graph curves upward and gets steeper. Which model is this?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Koʻrsatkichli oʻsish.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A model built from 5 years of data is used to predict 50 years ahead. What is
  the concern?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Bashorat maʼlumot oraliqidan juda uzoq — model
  u yerda tekshirilmagan.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>best fits the data</b><span>maʼlumotga eng mos keladi</span></li>
  <li><b>constant factor</b><span>oʻzgarmas koeffitsient</span></li>
  <li><b>constant amount</b><span>oʻzgarmas miqdor</span></li>
  <li><b>successive differences</b><span>ketma-ket ayirmalar</span></li>
  <li><b>successive ratios</b><span>ketma-ket nisbatlar</span></li>
  <li><b>extrapolate</b><span>maʼlumot tashqarisiga choʻzmoq</span></li>
  <li><b>approaches zero</b><span>nolga yaqinlashadi</span></li>
  <li><b>appropriate model</b><span>oʻrinli model</span></li>
  <li><b>over the range of the data</b><span>maʼlumot oraliqida</span></li>
  <li><b>approximately</b><span>taxminan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Avval <b>ayiring</b>, keyin <b>boʻling</b> — shu tartibda.</li>
    <li>Haqiqiy maʼlumotda nisbatlar <b>taxminan</b> teng boʻlsa
        yetarli.</li>
    <li>Model faqat <b>maʼlumot oraliqida</b> ishonchli.</li>
  </ul>
</div>
""",
    },
]
