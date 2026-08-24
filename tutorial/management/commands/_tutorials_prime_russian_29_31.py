# -*- coding: utf-8 -*-
"""Prime Russian — Block D boshi (29–31): kelishiklar.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-29 — butun tizimning xaritasi (hech qanday shakl yodlatilmaydi, faqat
koʻrsatiladi va oʻzbekcha kelishiklar bilan solishtiriladi).
PR-30 va PR-31 — birinchi haqiqiy kelishik: предло́жный. U birinchi
oʻrgatiladi, chunki (1) qoʻshimchasi eng oddiy — deyarli har doim -Е,
(2) predlogsiz umuman ishlatilmaydi, shuning uchun uni tanish oson,
(3) «где?» savoli birinchi kundanoq kerak boʻladi.

Urgʻu siyosati: yangi va urgʻusi koʻchadigan soʻzlarga belgi — kelishikda
urgʻu koʻp koʻchadi (стол → на столе́), shuning uchun bu blokda belgilar
koʻproq.

Mashqlar:        practice/management/commands/_practice_pr_29_31.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_29_31.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_29_31.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Russian",
    "category": "russian",
    "description": (
        "Rus tili noldan ishonchli B2 gacha — 100 ta dars. Kirill alifbosi, kelishiklar, "
        "feʼl turlari, oʻzbekcha tushuntirish va oʻzingiz tekshiradigan mashqlar."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-29: Kelishik nima? Olti падеж'ning umumiy xaritasi",
        "category": "russian",
        "order": 29,
        "summary": (
            "Kursning eng katta bloki boshlanadi. Bu darsda hech narsa yodlanmaydi — "
            "faqat xarita koʻriladi: oltita kelishik, ularning savollari va "
            "oʻzbekcha kelishiklar bilan solishtiruvi."
        ),
        "stories": ["Одно слово — шесть форм"],
        "content": """
<h2>PR-29: Kelishik nima? Olti падеж'ning umumiy xaritasi</h2>

<p>Bugundan boshlab kursning eng katta va eng muhim bloki ochiladi. Yigirma
ikkita dars, bitta mavzu: <b>kelishik</b> (паде́ж). Rus tilini oʻrganayotgan
odamlarning koʻpchiligi aynan shu yerda toʻxtaydi. Siz toʻxtamaysiz — va
buning aniq sababi bor: <b>oʻzbek tilida ham kelishik bor, va u ham
oltita</b>. Siz kelishikni oʻrganmaysiz, siz uni <b>ruschaga
koʻchirasiz</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Kelishik nima ekanini — va nima uchun kerakligini tushunasiz</li>
    <li>Oltita kelishikni va ularning savollarini koʻrasiz</li>
    <li>Ularni oʻzbekcha kelishiklar bilan yonma-yon qoʻyasiz</li>
    <li>Rus tilining uchta yangi qiyinchiligini oldindan bilib olasiz</li>
  </ul>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<b>Bu darsda hech narsa yodlash shart emas.</b> Bu xarita, dars emas.
Jadvalga qarang, savollarni oʻqing, oʻzbekcha bilan solishtiring — va
davom eting. Har bir kelishik keyingi darslarda alohida, batafsil keladi.
Xaritaning butun vazifasi — <b>siz qayerga ketayotganingizni koʻrsatish</b>.
Yoʻlni bilgan odam adashmaydi.</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kelishik nima</span>
  <span class="pe-chip pe-chip--s">otning oxiri</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">uning gapdagi ISHI</span>
</div>

<h3>1. Kelishik nima qiladi</h3>

<p>Bitta gapga uchta soʻz olamiz: <em>Афсо́на</em>, <em>кни́га</em>,
<em>чита́ть</em>. Ularni shunchaki yonma-yon qoʻysak, gap chiqmaydi. Kim kimni
oʻqiyapti? Rus tili buni <b>soʻzning oxiri bilan</b> hal qiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Афсо́на</span>
     <span class="pe-hl pe-hl--v">чита́ет</span>
     <span class="pe-hl pe-hl--o">кни́гу</span>.</p>
  <p class="pe-ex__uz">Afsona kitobni oʻqiydi.</p>
  <p class="pe-ex__why">Oxirgi soʻzga qarang: <em>кни́г<b>а</b></em> emas,
     <em>кни́г<b>у</b></em>. Bitta harf «bu — <b>toʻldiruvchi</b>» deb aytib
     turibdi. Oʻzbekchada ham xuddi shu ish bitta qoʻshimcha bilan
     qilinadi: <em>kitob<b>ni</b></em>.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana Prime Russian'ning eng katta ustunligi, va uni bir marta yaxshilab
koʻrib chiqing.<br><br>
Ingliz tilida kelishik <b>yoʻq</b>. Ingliz oʻquvchi uchun «soʻzning oxiri
uning ishini koʻrsatadi» degan fikr <b>butunlay yangi</b> — u buni noldan
tushunishi kerak, va aynan shuning uchun rus tili unga qiyin.<br><br>
Siz esa buni <b>har kuni, oʻylamasdan</b> qilasiz:<br>
<em>kitob</em> · <em>kitob<b>ning</b></em> · <em>kitob<b>ni</b></em> ·
<em>kitob<b>ga</b></em> · <em>kitob<b>da</b></em> · <em>kitob<b>dan</b></em><br>
Oltita shakl, oltita ish. Rus tilida ham oltita. <b>Tushuncha siz uchun
yangi emas — faqat qoʻshimchalar boshqa.</b></div>

<h3>2. Oltita kelishik — xarita</h3>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Savoli</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-case__q">кто? что?</td>
      <td class="pr-case__word">кни́г<span class="pr-end">а</span></td>
      <td class="pr-case__uz">bosh kelishik — kitob</td></tr>
  <tr><td class="pr-case__name">Роди́тельный</td><td class="pr-case__q">кого́? чего́?</td>
      <td class="pr-case__word">кни́г<span class="pr-end">и</span></td>
      <td class="pr-case__uz">qaratqich — kitob<b>ning</b></td></tr>
  <tr><td class="pr-case__name">Да́тельный</td><td class="pr-case__q">кому́? чему́?</td>
      <td class="pr-case__word">кни́г<span class="pr-end">е</span></td>
      <td class="pr-case__uz">joʻnalish — kitob<b>ga</b></td></tr>
  <tr><td class="pr-case__name">Вини́тельный</td><td class="pr-case__q">кого́? что?</td>
      <td class="pr-case__word">кни́г<span class="pr-end">у</span></td>
      <td class="pr-case__uz">tushum — kitob<b>ni</b></td></tr>
  <tr><td class="pr-case__name">Твори́тельный</td><td class="pr-case__q">кем? чем?</td>
      <td class="pr-case__word">кни́г<span class="pr-end">ой</span></td>
      <td class="pr-case__uz">— (oʻzbekchada «bilan»)</td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">Предло́жный</td>
      <td class="pr-case__q">о ком? о чём?</td>
      <td class="pr-case__word">о кни́г<span class="pr-end">е</span></td>
      <td class="pr-case__uz">oʻrin-payt — kitob<b>da</b>, kitob haqida</td></tr>
</table></div>

<p>Qizil bilan belgilangan qator — <b>предло́жный</b>. Uni birinchi
oʻrganamiz (PR-30 va PR-31 da), chunki uning qoʻshimchasi eng oddiy va uning
savoli — «qayerda?» — birinchi kundanoq kerak.</p>

<h3>3. Har bir kelishik nima uchun kerak — bir qatorda</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Имени́тельный</p>
    <p><b>Ega.</b> Lugʻatdagi shakl.<br>
       <em>Кни́га лежи́т.</em> — Kitob yotibdi.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Роди́тельный</p>
    <p><b>Kimniki? Yoʻqlik. Miqdor.</b><br>
       <em>кни́га бра́та</em> — akaning kitobi<br>
       <em>нет кни́ги</em> — kitob yoʻq</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Да́тельный</p>
    <p><b>Kimga?</b><br>
       <em>Я дам кни́гу бра́ту.</em> — Akamga beraman.<br>
       <em>Мне хо́лодно.</em> — Menga sovuq.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">4</span>Вини́тельный</p>
    <p><b>Toʻldiruvchi. Yoʻnalish.</b><br>
       <em>Я чита́ю кни́гу.</em> — Kitobni oʻqiyman.<br>
       <em>Я иду́ в шко́лу.</em> — Maktabga.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">5</span>Твори́тельный</p>
    <p><b>Nima bilan? Kim bilan?</b><br>
       <em>Я пишу́ ру́чкой.</em> — Ruchka bilan.<br>
       <em>с бра́том</em> — akam bilan</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">6</span>Предло́жный</p>
    <p><b>Qayerda? Nima haqida?</b><br>
       <em>в шко́ле</em> — maktabda<br>
       <em>о кни́ге</em> — kitob haqida</p></div>
</div>

<h3>4. Bitta soʻz, oltita shakl</h3>

<p>Endi uchta otni yonma-yon qoʻyamiz — erkak, ayol va oʻrta jinsdan. Bu
jadvalni <b>yodlamang</b>. Faqat qarang va bir narsani payqang: har bir
ustunda oxiri oʻzgaryapti, oʻzak esa turibdi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kelishik</th><th>стол (erkak)</th><th>кни́га (ayol)</th><th>окно́ (oʻrta)</th></tr>
  <tr><td class="pr-uz">Имени́тельный</td><td class="pr-res">стол</td>
      <td class="pr-res">кни́га</td><td class="pr-res">окно́</td></tr>
  <tr><td class="pr-uz">Роди́тельный</td><td class="pr-end">стола́</td>
      <td class="pr-end">кни́ги</td><td class="pr-end">окна́</td></tr>
  <tr><td class="pr-uz">Да́тельный</td><td class="pr-end">столу́</td>
      <td class="pr-end">кни́ге</td><td class="pr-end">окну́</td></tr>
  <tr><td class="pr-uz">Вини́тельный</td><td class="pr-end">стол</td>
      <td class="pr-end">кни́гу</td><td class="pr-end">окно́</td></tr>
  <tr><td class="pr-uz">Твори́тельный</td><td class="pr-end">столо́м</td>
      <td class="pr-end">кни́гой</td><td class="pr-end">окно́м</td></tr>
  <tr><td class="pr-uz">Предло́жный</td><td class="pr-end">о столе́</td>
      <td class="pr-end">о кни́ге</td><td class="pr-end">об окне́</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Jadvalda ikkita yaxshi xabar yashiringan:<br>
1. <b>Erkak va oʻrta jins deyarli bir xil</b> — <em>стол<b>а́</b> / окн<b>а́</b></em>,
<em>стол<b>у́</b> / окн<b>у́</b></em>, <em>стол<b>о́м</b> / окн<b>о́м</b></em>.
Yaʼni amalda uchta emas, <b>ikkita</b> naqsh bor.<br>
2. <b>Baʼzi shakllar takrorlanadi</b>: <em>кни́ге</em> — ham Да́тельный, ham
Предло́жный. <em>Стол</em> — ham Имени́тельный, ham Вини́тельный. Yaʼni
36 ta shakl emas, ancha kam narsa yodlanadi.</div>

<h3>5. Uchta yangi qiyinchilik — ularni oldindan biling</h3>

<p>Tushuncha tanish, lekin uchta narsa oʻzbekchada yoʻq. Ular qayerda xato
qilishingizni oldindan aytib turadi:</p>

<ol class="pe-steps">
  <li><b>Jins.</b> Oʻzbekchada <em>kitob<b>ni</b></em> va <em>stol<b>ni</b></em>
      — bitta qoʻshimcha. Ruschada <em>кни́г<b>у</b></em>, lekin
      <em>стол</em> — jinsga qarab boshqa. Har bir kelishikda uchta variant
      bor.</li>
  <li><b>Predloglar.</b> Oʻzbekchada qoʻshimcha oʻzi yetarli:
      <em>maktab<b>da</b></em>. Ruschada koʻpincha <b>ikkita</b> narsa kerak:
      <em><b>в</b> шко́л<b>е</b></em> — predlog <b>va</b> qoʻshimcha. Ikkalasi
      birga ishlaydi.</li>
  <li><b>Urgʻu koʻchadi.</b> <em>сто́л → на стол<b>е́</b></em>,
      <em>окно́ → о́кна</em>. Kelishik oʻzgarganda urgʻu joyini almashtirishi
      mumkin, va buni har bir soʻz bilan birga yodlash kerak.</li>
</ol>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Ikkinchi punktga qayting — u eng koʻp xato keltiradi. Rus tilida
<b>predlog oʻzi kelishikni tanlaydi</b>. <em>В</em> ikki xil kelishik bilan
ishlaydi va maʼnosi oʻzgaradi:<br>
<em>Я <b>в шко́ле</b></em> — maktabda<b>man</b> (qayerda? — Предло́жный)<br>
<em>Я иду́ <b>в шко́лу</b></em> — maktab<b>ga</b> ketyapman (qayerga? —
Вини́тельный)<br>
Bitta predlog, ikkita qoʻshimcha, ikkita maʼno. Buni PR-30 va PR-33 da
alohida koʻramiz.</div>

<h3>6. Qanday tartibda oʻrganamiz</h3>

<p>Kelishiklarni jadval tartibida emas, <b>foydalilik tartibida</b>
oʻrganamiz — birinchi darsdan keyin darrov gapira boshlaysiz:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Dars</th><th>Kelishik</th><th>Nega bu tartibda</th></tr>
  <tr><td class="pr-res">PR-30, PR-31</td><td class="pr-end">Предло́жный</td>
      <td class="pr-uz">Qoʻshimchasi eng oddiy (-Е) va «qayerda?» darrov kerak</td></tr>
  <tr><td class="pr-res">PR-32, PR-33</td><td class="pr-end">Вини́тельный</td>
      <td class="pr-uz">Har bir feʼlga toʻldiruvchi kerak boʻladi</td></tr>
  <tr><td class="pr-res">PR-34…36</td><td class="pr-end">Роди́тельный</td>
      <td class="pr-uz">Eng koʻp ishlatiladigan va eng koʻp ishli kelishik</td></tr>
  <tr><td class="pr-res">PR-37, PR-38</td><td class="pr-end">Да́тельный</td>
      <td class="pr-uz">«Мне на́до» va «мне нра́вится» ni allaqachon bilasiz</td></tr>
  <tr><td class="pr-res">PR-39, PR-40</td><td class="pr-end">Твори́тельный</td>
      <td class="pr-uz">Yagona butunlay yangi tushuncha — oxiriga qoldiriladi</td></tr>
</table></div>

<p>Keyin sifatlar, olmoshlar va koʻplik keladi (PR-41…46) — ular <b>oʻsha
oltita kelishikning</b> boshqa soʻz turkumlaridagi koʻrinishi. Yaʼni yangi
tizim emas, oʻsha tizim.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Афсо́на чита́ет кни́га.</s></p>
  <p class="pe-good">Афсо́на чита́ет <b>кни́гу</b> — toʻldiruvchi Вини́тельный'da</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я в шко́ла.</s></p>
  <p class="pe-good">Я <b>в шко́ле</b> — predlog bor, demak qoʻshimcha ham kerak</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́ в шко́ле.</s></p>
  <p class="pe-good">Я иду́ <b>в шко́лу</b> — «qayerga?» boshqa kelishik talab qiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кни́га брат.</s></p>
  <p class="pe-good">Кни́га <b>бра́та</b> — «kimniki?» Роди́тельный'da</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Kelishik nima qiladi — bir jumlada ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Soʻzning <strong>oxirini</strong>
    oʻzgartirib, uning <strong>gapdagi ishini</strong> koʻrsatadi: ega,
    toʻldiruvchi, egalik, joy… Oʻzbekchada ham xuddi shu ish qilinadi:
    <em>kitob → kitobni → kitobga</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Qaysi ruscha kelishik oʻzbekcha <b>-ni</b> ga toʻgʻri keladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Вини́тельный</strong> (tushum
    kelishigi). <em>kitob<b>ni</b> oʻqidim</em> → <em>я чита́л
    кни́г<b>у</b></em>. Savoli: <em>кого́? что?</em></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Qaysi ruscha kelishikning oʻzbekchada aniq juftligi <b>yoʻq</b>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Твори́тельный</strong>. Oʻzbekchada
    bu maʼno alohida kelishik bilan emas, <b>«bilan»</b> soʻzi bilan
    beriladi: <em>ruchka bilan yozdim</em> → <em>я писа́л
    ру́чк<b>ой</b></em>. Shuning uchun u kursda eng oxirida (PR-39,
    PR-40) oʻrgatiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nega <b>предло́жный</b> shunday nomlanadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki u <strong>hech qachon predlogsiz
    ishlatilmaydi</strong> (предло́г — predlog). <em>В шко́ле, на рабо́те,
    о кни́ге</em> — har doim oldida <em>в</em>, <em>на</em> yoki <em>о</em>
    turadi. Bu uni tanishni osonlashtiradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu ikki gapning farqi nima?<br>
     <b>Я в шко́ле. · Я иду́ в шко́лу.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — <strong>qayerda</strong>
    (maktabdaman), ikkinchisi — <strong>qayerga</strong> (maktabga
    ketyapman). Predlog bir xil (<em>в</em>), lekin kelishik boshqa:
    Предло́жный va Вини́тельный. Rus tilida predlogning oʻzi yetarli emas —
    qoʻshimcha ham maʼno beradi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>паде́ж</b><span>kelishik</span></li>
  <li><b>предло́г</b><span>predlog</span></li>
  <li><b>оконча́ние</b><span>qoʻshimcha, soʻz oxiri</span></li>
  <li><b>фо́рма</b><span>shakl</span></li>
  <li><b>вопро́с</b><span>savol</span></li>
  <li><b>систе́ма</b><span>tizim</span></li>
  <li><b>пра́вило</b><span>qoida</span></li>
  <li><b>род</b><span>jins</span></li>
  <li><b>ударе́ние</b><span>urgʻu</span></li>
  <li><b>сло́во</b><span>soʻz</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Kelishik — soʻzning oxiri, u soʻzning <b>gapdagi ishini</b>
        koʻrsatadi.</li>
    <li>Rus tilida oltita, oʻzbek tilida ham oltita. <b>Tushuncha siz uchun
        yangi emas.</b></li>
    <li>Xarita: Имени́тельный (kim? nima?) · Роди́тельный (-ning) ·
        Да́тельный (-ga) · Вини́тельный (-ni) · Твори́тельный (bilan) ·
        Предло́жный (-da, haqida).</li>
    <li>Erkak va oʻrta jins deyarli bir xil turlanadi — amalda ikkita
        naqsh.</li>
    <li>Uchta yangi qiyinchilik: <b>jins</b>, <b>predloglar</b>, <b>urgʻuning
        koʻchishi</b>.</li>
    <li>Bitta predlog ikki kelishik bilan ishlashi mumkin:
        <em>в шко́л<b>е</b></em> (qayerda) — <em>в шко́л<b>у</b></em>
        (qayerga).</li>
    <li>Bu dars — xarita. Yodlash keyingi darslarda.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-30: Предложный 1: где? — в школе, на работе, в Ташкенте",
        "category": "russian",
        "order": 30,
        "summary": (
            "Birinchi haqiqiy kelishik, va u eng osoni: qoʻshimcha deyarli har doim "
            "-Е. Butun qiyinchilik bitta savolda — В mi yoki НА mi?"
        ),
        "stories": ["Где мои ключи?"],
        "content": """
<h2>PR-30: Предложный 1: где? — в школе, на работе, в Ташкенте</h2>

<p>Kecha xaritani koʻrdingiz. Bugun birinchi kelishikni haqiqatan ham
ishlatasiz — va u xaritadagi eng oson kelishik. Sababi oddiy:
<b>qoʻshimchasi deyarli har doim bitta harf — <span class="pr-end">Е</span></b>.
Erkakmi, ayolmi, oʻrtami — farqi yoʻq. Bugungi darsning butun qiyinchiligi
boshqa joyda: <b>в</b> mi yoki <b>на</b> mi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>«Qayerda?» degan savolga javob berasiz: <b>в шко́ле, на рабо́те</b></li>
    <li>Bitta qoidani oʻrganasiz: oxiriga <b>-Е</b></li>
    <li>Uchta istisnoni bilasiz: <b>-ИИ</b>, <b>-И</b> va <b>-У</b></li>
    <li><b>В</b> va <b>на</b> ni ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Предло́жный</span>
  <span class="pe-chip pe-chip--v">в / на</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">шко́л</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">е</span>
</div>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Savoli</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-case__q">кто? что?</td>
      <td class="pr-case__word">шко́ла</td><td class="pr-case__uz">bosh kelishik — maktab</td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">Предло́жный</td>
      <td class="pr-case__q">где?</td>
      <td class="pr-case__word">в шко́л<span class="pr-end">е</span></td>
      <td class="pr-case__uz">oʻrin-payt — maktab<b>da</b></td></tr>
</table></div>

<h3>1. Bitta qoida: oxiriga -Е</h3>

<p>Otni oling, oxirgi unlisini olib tashlang (agar bor boʻlsa) va
<b>-Е</b> qoʻying. Hammasi shu:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ot</th><th>Jinsi</th><th>Qayerda?</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">шко́ла</td><td class="pr-uz">ayol</td>
      <td class="pr-end">в шко́ле</td><td class="pr-uz">maktabda</td></tr>
  <tr><td class="pr-res">рабо́та</td><td class="pr-uz">ayol</td>
      <td class="pr-end">на рабо́те</td><td class="pr-uz">ishda</td></tr>
  <tr><td class="pr-res">ко́мната</td><td class="pr-uz">ayol</td>
      <td class="pr-end">в ко́мнате</td><td class="pr-uz">xonada</td></tr>
  <tr><td class="pr-res">дом</td><td class="pr-uz">erkak</td>
      <td class="pr-end">в до́ме</td><td class="pr-uz">uyda</td></tr>
  <tr><td class="pr-res">магази́н</td><td class="pr-uz">erkak</td>
      <td class="pr-end">в магази́не</td><td class="pr-uz">doʻkonda</td></tr>
  <tr><td class="pr-res">Ташке́нт</td><td class="pr-uz">erkak</td>
      <td class="pr-end">в Ташке́нте</td><td class="pr-uz">Toshkentda</td></tr>
  <tr><td class="pr-res">стол</td><td class="pr-uz">erkak</td>
      <td class="pr-end">на столе́</td><td class="pr-uz">stolda</td></tr>
  <tr><td class="pr-res">окно́</td><td class="pr-uz">oʻrta</td>
      <td class="pr-end">в окне́</td><td class="pr-uz">derazada</td></tr>
  <tr><td class="pr-res">письмо́</td><td class="pr-uz">oʻrta</td>
      <td class="pr-end">в письме́</td><td class="pr-uz">xatda</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻng ustunga qarang — hammasi <b>-DA</b> bilan tugagan.
<em>maktab<b>da</b></em>, <em>uy<b>da</b></em>, <em>stol<b>da</b></em>. Bu
oʻzbekchadagi <b>oʻrin-payt kelishigi</b>, va u aynan shu ishni qiladi.
Yaʼni <b>kelishikning oʻzi sizga tekin beriladi</b>.<br><br>
Bitta farq bor va u butun darsning qiyinchiligi: oʻzbekchada
<b>-da</b> hamma soʻz uchun bitta. Ruschada esa qoʻshimchadan tashqari
<b>predlog</b> ham kerak, va u ikki xil: <em><b>в</b> шко́ле</em>, lekin
<em><b>на</b> рабо́те</em>. Qaysi soʻz qaysi predlogni oladi — buni soʻz
bilan birga yodlash kerak.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Urgʻu koʻchishi mumkin: <em>сто́л → на стол<b>е́</b></em>,
<em>окно́ → в окн<b>е́</b></em>, <em>письмо́ → в письм<b>е́</b></em>.
Bir boʻgʻinli erkak otlarda urgʻu koʻpincha qoʻshimchaga oʻtadi. Yangi soʻzni
yodlaganda uni <b>predlog bilan birga va urgʻusi bilan</b> yodlang:
«на стол<b>е́</b>» — bitta boʻlak.</div>

<h3>2. Uchta istisno</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>-ия · -ие · -ий → <b>-ИИ</b></p>
    <p><em>Росси́я → в Росси́и</em><br>
       <em>ле́кция → на ле́кции</em><br>
       <em>общежи́тие → в общежи́тии</em><br>
       <em>Ита́лия → в Ита́лии</em><br>
       Bu tugallanishdagi <b>hamma</b> soʻz shunday.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Ayol jinsi <b>-ь</b> → <b>-И</b></p>
    <p><em>тетра́дь → в тетра́ди</em><br>
       <em>пло́щадь → на пло́щади</em><br>
       <em>Сиби́рь → в Сиби́ри</em></p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Kichik roʻyxat: <b>-У́</b></p>
    <p><em>лес → в лесу́</em> · <em>сад → в саду́</em><br>
       <em>пол → на полу́</em> · <em>шкаф → в шкафу́</em><br>
       <em>бе́рег → на берегу́</em><br>
       <em>аэропо́рт → в аэропорту́</em></p></div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Uchinchi guruh — <b>yopiq roʻyxat</b>, unda oʻn beshtacha soʻz bor va ular
hammasi <b>joy</b> bildiradi. Ularning urgʻusi har doim qoʻshimchada:
<em>в лес<b>у́</b></em>, <em>на пол<b>у́</b></em>. Bularni alohida yodlang —
qoida yoʻq, faqat roʻyxat. Qolgan hamma soʻz birinchi guruhda: <b>-Е</b>.</div>

<h3>3. В yoki НА — darsning yuragi</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">В — <b>ichida</b></p>
    <p>Devori, chegarasi bor joy:<br>
       <em>в до́ме · в ко́мнате · в шко́ле · в магази́не · в маши́не ·
       в су́мке · в го́роде · в Ташке́нте · в кни́ге</em></p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">НА — <b>ustida</b> yoki <b>ochiq joyda</b></p>
    <p>Yuza, ochiq maydon, tadbir:<br>
       <em>на столе́ · на у́лице · на по́лке · на этаже́ · на пло́щади ·
       на стадио́не · на берегу́</em></p>
  </div>
</div>

<p>Shu yerga qadar mantiq ishlaydi. Lekin bir guruh soʻz bor — ularda
<b>mantiq yoʻq</b>, faqat odat. Ular <b>НА</b> oladi va yodlanadi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Oʻzbekcha</th><th>Ibora</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">на рабо́те</td><td class="pr-uz">ishda</td>
      <td class="pr-res">на по́чте</td><td class="pr-uz">pochtada</td></tr>
  <tr><td class="pr-res">на уро́ке</td><td class="pr-uz">darsda</td>
      <td class="pr-res">на вокза́ле</td><td class="pr-uz">vokzalda</td></tr>
  <tr><td class="pr-res">на ле́кции</td><td class="pr-uz">maʼruzada</td>
      <td class="pr-res">на заво́де</td><td class="pr-uz">zavodda</td></tr>
  <tr><td class="pr-res">на ры́нке</td><td class="pr-uz">bozorda</td>
      <td class="pr-res">на ку́хне</td><td class="pr-uz">oshxonada</td></tr>
  <tr><td class="pr-res">на экза́мене</td><td class="pr-uz">imtihonda</td>
      <td class="pr-res">на ю́ге</td><td class="pr-uz">janubda</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu roʻyxatni koʻrib xafa boʻlmang — <b>oʻzbekchada ham xuddi shunday
mantiqsiz odatlar bor</b>. Nega «maktab<b>da</b>» lekin «yoʻl<b>da</b>»?
Nega «uy<b>ga</b> boraman» lekin «Toshkent<b>ga</b> boraman»? Chunki til
shunday. Rus tilida bu tanlov predlogda koʻrinadi, xolos.<br><br>
Amaliy maslahat: <b>ish, dars, tadbir, ochiq maydon</b> — koʻpincha
<em>на</em>. <b>Bino, shahar, idish, kitob</b> — koʻpincha <em>в</em>.
Bu qoida emas, lekin oʻntadan sakkiztasida ishlaydi.</div>

<h3>4. До́ма — predlogsiz</h3>

<p>Baʼzi joylar umuman kelishik olmaydi, chunki ular <b>ravish</b>:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ravish</th><th>Maʼnosi</th><th>Eslatma</th></tr>
  <tr><td class="pr-res">до́ма</td><td class="pr-uz">uyda</td>
      <td class="pr-uz">«в до́ме» emas! U «bino ichida» degani</td></tr>
  <tr><td class="pr-res">здесь</td><td class="pr-uz">bu yerda</td>
      <td class="pr-uz">oʻzgarmaydi</td></tr>
  <tr><td class="pr-res">там</td><td class="pr-uz">u yerda</td>
      <td class="pr-uz">oʻzgarmaydi</td></tr>
  <tr><td class="pr-res">везде́</td><td class="pr-uz">hamma joyda</td>
      <td class="pr-uz">oʻzgarmaydi</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Где Жасу́р?<br>
     — Он <span class="pe-hl pe-hl--adv">до́ма</span>. А Афсо́на
     <span class="pe-hl pe-hl--adv">на рабо́те</span>.</p>
  <p class="pe-ex__uz">— Jasur qayerda?<br>— U uyda. Afsona esa ishda.</p>
  <p class="pe-ex__why">Ikkita javob, ikki xil qurilish: <em>до́ма</em> —
     ravish, <em>на рабо́те</em> — predlog + Предло́жный.</p>
</div>

<h3>5. Gaplarda</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">Ключи́ <span class="pe-hl pe-hl--adv">на столе́</span>,
     а телефо́н <span class="pe-hl pe-hl--adv">в су́мке</span>.</p>
  <p class="pe-ex__uz">Kalitlar stolda, telefon esa sumkada.</p>
  <p class="pe-ex__why">Stol — yuza, demak <b>на</b>. Sumka — ichi bor,
     demak <b>в</b>. Bu yerda mantiq toʻgʻri ishlaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Мы <span class="pe-hl pe-hl--v">живём</span>
     <span class="pe-hl pe-hl--adv">в Ташке́нте</span>, а ба́бушка —
     <span class="pe-hl pe-hl--adv">в дере́вне</span>.</p>
  <p class="pe-ex__uz">Biz Toshkentda yashaymiz, buvim esa qishloqda.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Ты <span class="pe-hl pe-hl--v">был</span>
     <span class="pe-hl pe-hl--adv">на ры́нке</span>?<br>
     — Нет, я был <span class="pe-hl pe-hl--adv">в магази́не</span>.</p>
  <p class="pe-ex__uz">— Bozorda boʻldingmi?<br>— Yoʻq, doʻkonda edim.</p>
  <p class="pe-ex__why">Bozor — ochiq maydon, demak <b>на</b>. Doʻkon — bino,
     demak <b>в</b>. Ikkalasi ham <b>-е</b> bilan tugadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я в шко́ла.</s></p>
  <p class="pe-good">Я <b>в шко́ле</b> — predlog bor, demak qoʻshimcha ham kerak</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он в рабо́те.</s></p>
  <p class="pe-good">Он <b>на рабо́те</b> — «рабо́та» НА oladigan roʻyxatda</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мы живём в Росси́е.</s></p>
  <p class="pe-good">Мы живём <b>в Росси́и</b> — <b>-ия</b> soʻzlari <b>-ии</b> oladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я в до́ме.</s> <em>(«uydaman» maʼnosida)</em></p>
  <p class="pe-good">Я <b>до́ма</b> — bu ravish, kelishik kerak emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кни́га на столу́.</s></p>
  <p class="pe-good">Кни́га <b>на столе́</b> — <em>стол</em> <b>-у́</b> roʻyxatida yoʻq</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Афсо́на сейча́с ___ (шко́ла).</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в шко́ле</strong>. Maktab — bino,
    demak <b>в</b>; qoʻshimcha esa oddiy <b>-е</b>:
    <em>шко́ла → шко́л- → шко́ле</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>в</b> yoki <b>на</b>? &nbsp; <b>Ма́ма ___ рабо́те, па́па ___
     магази́не.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>на</strong> рабо́те,
    <strong>в</strong> магази́не. <em>Рабо́та</em> — yodlanadigan
    НА-roʻyxatdan (ish, dars, imtihon, bozor…). <em>Магази́н</em> esa bino,
    demak <b>в</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Мой брат живёт ___ (Росси́я).</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в Росси́и</strong>. Birinchi istisno:
    <b>-ия</b> ga tugagan soʻzlar <b>-е</b> emas, <b>-ии</b> oladi. Xuddi
    shunday: <em>на ле́кции</em>, <em>в общежи́тии</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapda xato bormi? <b>Ве́чером мы бу́дем в до́ме.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Grammatik jihatdan toʻgʻri, lekin maʼnosi
    gʻalati. «Uyda boʻlamiz» demoqchi boʻlsangiz — <strong>бу́дем
    до́ма</strong>. <em>В до́ме</em> «bino <b>ichida</b>» degani va u
    koʻchada turgan odam aytadigan gap.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi qatorda hammasi toʻgʻri?<br>
     а) в шко́ле · на рабо́те · в Росси́и<br>
     б) в шко́ла · на рабо́те · в Росси́и<br>
     в) в шко́ле · в рабо́те · в Росси́е<br>
     г) на шко́ле · на рабо́те · в Росси́и</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>а)</strong>. Uchtasi ham uchta
    boshqa qoidani sinaydi: oddiy <b>-е</b>, НА-roʻyxat, va <b>-ии</b>
    istisnosi. Qolgan variantlarda bittasi har doim buziladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>где?</b><span>qayerda?</span></li>
  <li><b>в шко́ле</b><span>maktabda</span></li>
  <li><b>на рабо́те</b><span>ishda</span></li>
  <li><b>в ко́мнате</b><span>xonada</span></li>
  <li><b>на у́лице</b><span>koʻchada</span></li>
  <li><b>в лесу́</b><span>oʻrmonda</span></li>
  <li><b>на полу́</b><span>polda</span></li>
  <li><b>ключ</b><span>kalit</span></li>
  <li><b>карма́н</b><span>choʻntak</span></li>
  <li><b>дере́вня</b><span>qishloq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Предло́жный «<b>qayerda?</b>» degan savolga javob beradi va har doim
        predlog bilan keladi.</li>
    <li>Asosiy qoida: oxiriga <b>-Е</b>. Jinsdan qatʼi nazar.</li>
    <li>Uchta istisno: <b>-ия/-ие → -ИИ</b>, ayol <b>-ь → -И</b>, va
        <b>-У́</b> yopiq roʻyxati (в лесу́, на полу́).</li>
    <li><b>В</b> = ichida · <b>НА</b> = ustida yoki ochiq joyda.</li>
    <li>Yodlanadigan НА-roʻyxat: <em>на рабо́те, на уро́ке, на ры́нке,
        на по́чте, на вокза́ле, на ку́хне, на экза́мене</em>.</li>
    <li><b>До́ма, здесь, там</b> — ravish, kelishik olmaydi.</li>
    <li>Urgʻu koʻchishi mumkin: <em>стол → на стол<b>е́</b></em>. Soʻzni
        predlog va urgʻusi bilan birga yodlang.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-31: Предложный 2: о чём? о ком? — о фильме, о тебе",
        "category": "russian",
        "order": 31,
        "summary": (
            "Oʻsha kelishik, oʻsha qoʻshimchalar — faqat boshqa predlog va boshqa "
            "savol: «nima haqida?». Bu dars bilan siz nihoyat fikr bildira "
            "boshlaysiz."
        ),
        "stories": ["О чём эта книга?"],
        "content": """
<h2>PR-31: Предложный 2: о чём? о ком? — о фильме, о тебе</h2>

<p>Kecha oʻrgangan qoʻshimchalaringiz bugun <b>bitta harf ham
oʻzgarmaydi</b>. Faqat predlog boshqa: <em>в</em> va <em>на</em> oʻrniga
<b>о</b>. Va u bilan birga butunlay boshqa savol keladi — «<b>nima
haqida?</b>». Shu ikki harf sizga fikr bildirish, kitob va film muhokama
qilish, kimnidir oʻylash imkonini beradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>О</b> predlogi bilan «nima haqida» deysiz</li>
    <li><b>О, об, обо</b> ni toʻgʻri tanlaysiz</li>
    <li>Bu predlogni talab qiladigan feʼllarni bilasiz</li>
    <li>Olmoshlarni oʻrganasiz: <b>обо мне, о тебе́, о нём</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Nima haqida</span>
  <span class="pe-chip pe-chip--v">о</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">фи́льм</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">е</span>
</div>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Savoli</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-case__q">что?</td>
      <td class="pr-case__word">фильм</td><td class="pr-case__uz">bosh kelishik — film</td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">Предло́жный</td>
      <td class="pr-case__q">о чём?</td>
      <td class="pr-case__word">о фи́льм<span class="pr-end">е</span></td>
      <td class="pr-case__uz">film <b>haqida</b></td></tr>
</table></div>

<h3>1. Qoʻshimchalar — oʻsha uchtasi</h3>

<p>PR-30 dagi qoida oʻzgarishsiz ishlaydi. Faqat oldiga <b>о</b>
qoʻyiladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ot</th><th>Qayerda? (PR-30)</th><th>Nima haqida? (bugun)</th></tr>
  <tr><td class="pr-res">кни́га</td><td class="pr-uz">в кни́ге</td>
      <td class="pr-end">о кни́ге</td></tr>
  <tr><td class="pr-res">фильм</td><td class="pr-uz">в фи́льме</td>
      <td class="pr-end">о фи́льме</td></tr>
  <tr><td class="pr-res">шко́ла</td><td class="pr-uz">в шко́ле</td>
      <td class="pr-end">о шко́ле</td></tr>
  <tr><td class="pr-res">брат</td><td class="pr-uz">—</td>
      <td class="pr-end">о бра́те</td></tr>
  <tr><td class="pr-res">Росси́я</td><td class="pr-uz">в Росси́и</td>
      <td class="pr-end">о Росси́и</td></tr>
  <tr><td class="pr-res">ле́то</td><td class="pr-uz">—</td>
      <td class="pr-end">о ле́те</td></tr>
  <tr><td class="pr-res">любо́вь</td><td class="pr-uz">—</td>
      <td class="pr-end">о любви́ <em>(istisno)</em></td></tr>
</table></div>

<p>Yaʼni yangi qoʻshimcha yoʻq. Yangi predlog bor, va u <b>uch shaklda</b>
yoziladi.</p>

<h3>2. О, об yoki обо?</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Tanlov keyingi soʻzning <b>birinchi tovushiga</b> qarab qilinadi:<br>
<b>об</b> — soʻz <b>а, э, и, о, у</b> bilan boshlansa:
<em>об А́нне, об окне́, об уро́ке, об Ита́лии</em>.<br>
<b>о</b> — qolgan hamma holatda, yaʼni undoshdan oldin <b>va</b> е, ё, ю, я
dan oldin: <em>о кни́ге, о фи́льме, о Евро́пе, о я́блоке</em>.<br>
<b>обо</b> — faqat ikkita soʻz bilan: <em>обо мне</em> va <em>обо
всём</em>.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Qoida <b>harfga</b> emas, <b>tovushga</b> qaraydi. <em>Е, ё, ю, я</em>
harflari soʻz boshida ikkita tovushni bildiradi — [йэ], [йо], [йу], [йа] —
yaʼni ular aslida <b>Й</b> tovushidan boshlanadi, unlidan emas. Shuning uchun
<em><b>о</b> Евро́пе</em>, <em><b>о</b> я́блоке</em> — <em>об</em>
emas.</div>

<div class="pr-say">
  <span class="pr-say__from">об окне́</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[абакне́]</span>
  <span class="pr-say__why">об + unli — aynan shuning uchun Б qoʻshiladi</span>
</div>

<h3>3. Qaysi feʼllar «о» talab qiladi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Feʼl</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-res">ду́мать о</td><td class="pr-uz">-ni oʻylamoq</td>
      <td class="pr-end">Я ду́маю о рабо́те.</td></tr>
  <tr><td class="pr-res">говори́ть о</td><td class="pr-uz">-haqida gapirmoq</td>
      <td class="pr-end">Мы говори́м о фи́льме.</td></tr>
  <tr><td class="pr-res">чита́ть о</td><td class="pr-uz">-haqida oʻqimoq</td>
      <td class="pr-end">Я чита́ю о Сиби́ри.</td></tr>
  <tr><td class="pr-res">знать о</td><td class="pr-uz">-haqida bilmoq</td>
      <td class="pr-end">Ты зна́ешь об э́том?</td></tr>
  <tr><td class="pr-res">по́мнить о</td><td class="pr-uz">-ni esda tutmoq</td>
      <td class="pr-end">По́мни о ма́ме.</td></tr>
  <tr><td class="pr-res">спра́шивать о</td><td class="pr-uz">-haqida soʻramoq</td>
      <td class="pr-end">Он спра́шивает о тебе́.</td></tr>
  <tr><td class="pr-res">мечта́ть о</td><td class="pr-uz">-ni orzu qilmoq</td>
      <td class="pr-end">Я мечта́ю о мо́ре.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada bu maʼno <b>«haqida»</b> soʻzi bilan beriladi va u otdan
<b>keyin</b> turadi:<br>
<em>kitob <b>haqida</b></em> → <em><b>о</b> кни́г<b>е</b></em><br>
<em>sen <b>haqingda</b></em> → <em><b>о</b> тебе́</em><br>
Ikkita farq bor. Birinchisi — <b>joyi</b>: ruschada bu soʻz oldinda turadi
(shuning uchun «predlog»), oʻzbekchada esa orqada (shuning uchun
«koʻmakchi»). Ikkinchisi — ruschada <b>ot ham oʻzgaradi</b>:
<em>кни́г<b>е</b></em>, oʻzbekchada esa ot oʻz holida qoladi:
<em>kitob haqida</em>.<br><br>
Va bir joyda oʻzbekcha aniqroq: <em>ду́мать о</em> — «-ni oʻylamoq» ham,
«haqida oʻylamoq» ham boʻladi. <em>Я ду́маю о тебе́</em> — «seni oʻylayapman».
Bu yerda «haqingda» deb tarjima qilish shart emas.</div>

<h3>4. Olmoshlar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Olmosh</th><th>Bu shaklda</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td>я</td><td class="pr-res">обо мне</td>
      <td class="pr-end">Он ду́мает обо мне.</td><td class="pr-uz">men haqimda</td></tr>
  <tr><td>ты</td><td class="pr-res">о тебе́</td>
      <td class="pr-end">Я ду́маю о тебе́.</td><td class="pr-uz">sen haqingda</td></tr>
  <tr><td>он / оно́</td><td class="pr-res">о нём</td>
      <td class="pr-end">Мы говори́м о нём.</td><td class="pr-uz">u haqida (erkak)</td></tr>
  <tr><td>она́</td><td class="pr-res">о ней</td>
      <td class="pr-end">Она́ зна́ет о ней.</td><td class="pr-uz">u haqida (ayol)</td></tr>
  <tr><td>мы</td><td class="pr-res">о нас</td>
      <td class="pr-end">Они́ говоря́т о нас.</td><td class="pr-uz">biz haqimizda</td></tr>
  <tr><td>вы</td><td class="pr-res">о вас</td>
      <td class="pr-end">Я чита́л о вас.</td><td class="pr-uz">siz haqingizda</td></tr>
  <tr><td>они́</td><td class="pr-res">о них</td>
      <td class="pr-end">Что ты зна́ешь о них?</td><td class="pr-uz">ular haqida</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Uchinchi shaxs olmoshlariga qarang: <em>о <b>н</b>ём, о <b>н</b>ей,
о <b>н</b>их</em> — hammasida <b>Н</b> paydo boʻlgan. Bu tasodif emas:
<b>predlogdan keyin он/она́/они́ olmoshlari Н bilan boshlanadi</b>. Bu qoida
hamma kelishikda ishlaydi va siz uni yana koʻp koʻrasiz:
<em>у <b>н</b>его́</em> (PR-14 da uchragan!), <em>к <b>н</b>ей</em>,
<em>с <b>н</b>ими</em>. Bitta qoida — koʻp joyda.</div>

<h3>5. Savol berish</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--v">О чём</span> э́та
     кни́га?<br>
     — <span class="pe-hl pe-hl--adv">О дру́жбе</span>.</p>
  <p class="pe-ex__uz">— Bu kitob nima haqida?<br>— Doʻstlik haqida.</p>
  <p class="pe-ex__why"><em>О чём?</em> — narsa haqida. <em>О ком?</em> —
     odam haqida. Ikkalasi ham savol soʻzining oʻzi Предло́жный'da turgan
     shakli: <em>что → о чём</em>, <em>кто → о ком</em>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--v">О ком</span> ты
     ду́маешь?<br>
     — <span class="pe-hl pe-hl--adv">О ба́бушке</span>. Она́
     <span class="pe-hl pe-hl--adv">в дере́вне</span>, одна́.</p>
  <p class="pe-ex__uz">— Kim haqida oʻylayapsan?<br>— Buvim haqida. U
     qishloqda, yolgʻiz.</p>
  <p class="pe-ex__why">Bitta gapda ikkala predlog ham bor:
     <em>о ба́бушке</em> (haqida) va <em>в дере́вне</em> (qayerda) — lekin
     kelishik <b>bitta</b> va qoʻshimcha ham bir xil.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ду́маю о ты.</s></p>
  <p class="pe-good">Я ду́маю <b>о тебе́</b> — olmosh ham kelishikka kiradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он ду́мает о мне.</s></p>
  <p class="pe-good">Он ду́мает <b>обо мне</b> — bu ikkita istisnodan biri</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мы говори́м о фильм.</s></p>
  <p class="pe-good">Мы говори́м <b>о фи́льме</b> — predlog bor, demak <b>-е</b> ham</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я чита́л об кни́ге.</s></p>
  <p class="pe-good">Я чита́л <b>о кни́ге</b> — <b>об</b> faqat unlidan oldin</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Что ты зна́ешь о он?</s></p>
  <p class="pe-good">Что ты зна́ешь <b>о нём</b>? — predlogdan keyin <b>Н</b> qoʻshiladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Мы говори́м ___ (фильм).</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>о фи́льме</strong>. <em>Фильм</em>
    undoshdan boshlanadi, demak <b>о</b>; qoʻshimcha esa oʻsha PR-30 dagi
    <b>-е</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>о</b> yoki <b>об</b>? &nbsp; <b>___ уро́ке</b> · <b>___ Евро́пе</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>об</strong> уро́ке,
    <strong>о</strong> Евро́пе. Birinchisi <b>У</b> — unli tovush, demak
    <em>об</em>. Ikkinchisi <b>Е</b> — u soʻz boshida [йэ] boʻlib oʻqiladi,
    yaʼni undosh tovushdan boshlanadi, demak <em>о</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu gapni ruschaga oʻgiring: <b>Men sen haqingda oʻylayapman.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я ду́маю о тебе́.</strong> Yoki
    oddiy oʻzbekchada: «seni oʻylayapman» — <em>ду́мать о</em> ikkala
    maʼnoni ham beradi. <em>«О ты»</em> — xato: olmosh ham kelishikka
    kiradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nega bu shakllarda <b>Н</b> bor? &nbsp; <b>о нём · о ней · о них</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>predlogdan keyin</strong>
    <em>он / она́ / они́</em> olmoshlari <b>Н</b> bilan boshlanadi. Bu qoida
    hamma kelishikda ishlaydi — <em>у него́</em>, <em>к ней</em>,
    <em>с ни́ми</em>. Predlogsiz esa Н yoʻq: <em>его́, её, их</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Я чита́ю о Росси́и. &nbsp; б) Он ду́мает о мне.<br>
     в) Мы говори́м об уро́ке. &nbsp; г) Что ты зна́ешь о них?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б)</strong>. Toʻgʻrisi —
    <b>обо мне</b>. Bu rus tilidagi ikkita <em>обо</em> holatidan biri
    (ikkinchisi — <em>обо всём</em>). Qolgan uchtasi toʻgʻri:
    <em>о Росси́и</em> (-ия istisnosi), <em>об уро́ке</em> (unli), va
    <em>о них</em> (predlogdan keyin Н).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>о чём?</b><span>nima haqida?</span></li>
  <li><b>о ком?</b><span>kim haqida?</span></li>
  <li><b>обо мне</b><span>men haqimda</span></li>
  <li><b>ду́мать о</b><span>-ni oʻylamoq</span></li>
  <li><b>мечта́ть о</b><span>-ni orzu qilmoq</span></li>
  <li><b>дру́жба</b><span>doʻstlik</span></li>
  <li><b>любо́вь</b><span>sevgi</span></li>
  <li><b>исто́рия</b><span>hikoya; tarix</span></li>
  <li><b>мо́ре</b><span>dengiz</span></li>
  <li><b>оди́ночество</b><span>yolgʻizlik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Oʻsha kelishik, oʻsha qoʻshimchalar — faqat predlog <b>о</b> va savol
        <b>о чём? о ком?</b></li>
    <li><b>Об</b> — unli tovushdan oldin (об окне́, об уро́ке).
        <b>Обо</b> — faqat <em>обо мне</em> va <em>обо всём</em>.</li>
    <li>Е, ё, ю, я soʻz boshida <b>undosh</b> tovushdan boshlanadi — shuning
        uchun <em>о Евро́пе</em>.</li>
    <li>Feʼllar: <b>ду́мать · говори́ть · чита́ть · знать · по́мнить ·
        спра́шивать · мечта́ть</b> + о.</li>
    <li>Olmoshlar: <b>обо мне, о тебе́, о нём, о ней, о нас, о вас,
        о них</b>.</li>
    <li>Predlogdan keyin <em>он/она́/они́</em> ga <b>Н</b> qoʻshiladi — bu
        qoida hamma kelishikda ishlaydi.</li>
    <li>Oʻzbekcha <b>«haqida»</b> otdan keyin turadi, ruscha <b>о</b> esa
        oldin — va ruschada ot ham oʻzgaradi.</li>
  </ul>
</div>
""",
    },
]
