# -*- coding: utf-8 -*-
"""Prime Russian — Block D yakuniga yaqin (44–46).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-44 — sifatlarning qolgan uch kelishigi. Bu yerda katta yengillik bor:
ayol jinsidagi sifat TOʻRTTA kelishikda bitta shaklda (-ОЙ).
PR-45 — koʻplik И.п. va Р.п. Toc buni «eng qiyin joyi» deb belgilagan va
bu rost: koʻplik Роди́тельный rus tilidagi eng koʻp istisnoli shakl.
PR-46 — koʻplik Д./В./Т./П. Va bu — butun blokdagi ENG OSON dars: uchta
qoʻshimcha, jins umuman yoʻq. PR-45 dan keyin bu mukofot kabi keladi.

Mashqlar:        practice/management/commands/_practice_pr_44_46.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_44_46.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_44_46.py --author=prime
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
        "title": "PR-44: Sifatlarning turlanishi 2 — Дательный, Творительный, Предложный",
        "category": "russian",
        "order": 44,
        "summary": (
            "Sifat jadvali yopiladi. Va unda katta yengillik bor: ayol jinsidagi "
            "sifat toʻrtta kelishikda bitta shaklda turadi — -ОЙ."
        ),
        "stories": ["В большом городе"],
        "content": """
<h2>PR-44: Sifatlarning turlanishi 2 — Дательный, Творительный, Предложный</h2>

<p>Kecha sifatning ikkita kelishigini oldingiz. Bugun qolgan uchtasi keladi
va jadval yopiladi. Va bu darsda <b>yaxshi xabar bor</b>: ayol jinsidagi
sifat toʻrtta kelishikda <b>bitta shaklda</b> turadi. Yaʼni jadval katta
koʻrinadi, lekin yodlanadigan narsa kutilganidan ancha kam.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uchta yangi qoʻshimchani oʻrganasiz: <b>-ому, -ым, -ом</b></li>
    <li>Ayol jinsidagi <b>-ой</b> ning toʻrtta ishini koʻrasiz</li>
    <li>Butun sifat jadvalini bir joyda olasiz</li>
    <li>Savol soʻzi bilan tekshirish usulini oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uchta yangi shakl</span>
  <span class="pe-chip pe-chip--v">но́вому до́му</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">но́вым до́мом</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">о но́вом до́ме</span>
</div>

<h3>1. Uchta yangi kelishik</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kelishik</th><th>erkak / oʻrta</th><th>ayol</th><th>koʻplik</th></tr>
  <tr><td class="pr-uz">Да́тельный</td><td class="pr-end">но́вому</td>
      <td class="pr-end">но́вой</td><td class="pr-end">но́вым</td></tr>
  <tr><td class="pr-uz">Твори́тельный</td><td class="pr-end">но́вым</td>
      <td class="pr-end">но́вой</td><td class="pr-end">но́выми</td></tr>
  <tr><td class="pr-uz">Предло́жный</td><td class="pr-end">о но́вом</td>
      <td class="pr-end">о но́вой</td><td class="pr-end">о но́вых</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Ayol jinsidagi ustunga qarang: <b>но́вой, но́вой, но́вой</b>. Va kecha
oʻrgangan Роди́тельный ham <b>но́вой</b> edi.<br><br>
Yaʼni ayol jinsida <b>toʻrtta kelishikda bitta shakl</b> ishlatiladi:
Р., Д., Т., П. — hammasi <b>-ОЙ</b>. Boshqacha shakl faqat ikkitasida:
<em>но́в<b>ая</b></em> (И.п.) va <em>но́в<b>ую</b></em> (В.п.).<br><br>
Bu PR-42 dagi <em>мое́й</em> bilan bir xil hodisa. Ayol jinsi sifatlarda
eng oson jins.</div>

<h3>2. Butun jadval — sifat toʻliq</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kelishik</th><th>но́вый (erkak)</th><th>но́вая (ayol)</th><th>но́вое (oʻrta)</th><th>но́вые (koʻplik)</th></tr>
  <tr><td class="pr-uz">Имени́тельный</td><td class="pr-res">но́вый</td>
      <td class="pr-res">но́вая</td><td class="pr-res">но́вое</td><td class="pr-res">но́вые</td></tr>
  <tr><td class="pr-uz">Роди́тельный</td><td class="pr-end">но́вого</td>
      <td class="pr-end">но́вой</td><td class="pr-end">но́вого</td><td class="pr-end">но́вых</td></tr>
  <tr><td class="pr-uz">Да́тельный</td><td class="pr-end">но́вому</td>
      <td class="pr-end">но́вой</td><td class="pr-end">но́вому</td><td class="pr-end">но́вым</td></tr>
  <tr><td class="pr-uz">Вини́тельный</td><td class="pr-end">но́вый / но́вого</td>
      <td class="pr-end">но́вую</td><td class="pr-end">но́вое</td><td class="pr-end">но́вые / но́вых</td></tr>
  <tr><td class="pr-uz">Твори́тельный</td><td class="pr-end">но́вым</td>
      <td class="pr-end">но́вой</td><td class="pr-end">но́вым</td><td class="pr-end">но́выми</td></tr>
  <tr><td class="pr-uz">Предло́жный</td><td class="pr-end">о но́вом</td>
      <td class="pr-end">о но́вой</td><td class="pr-end">о но́вом</td><td class="pr-end">о но́вых</td></tr>
</table></div>

<p>Jadvalda 24 katak bor, lekin <b>boshqa-boshqa shakl atigi
sakkizta</b>: <em>но́вый, но́вая, но́вое, но́вые, но́вого, но́вому,
но́вым, но́вой, но́вую, но́вых, но́выми, но́вом</em>. Va ularning
koʻpchiligi qayta-qayta takrorlanadi.</p>

<h3>3. Savol soʻzi bilan tekshirish</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Rus maktablarida oʻrgatiladigan eng foydali hiyla: <b>savol soʻzining
oxiri sifatning oxiri bilan bir xil</b>.<br>
<em>как<b>о́му</b>? → но́в<b>ому</b></em><br>
<em>как<b>и́м</b>? → но́в<b>ым</b></em><br>
<em>о как<b>о́м</b>? → о но́в<b>ом</b></em><br>
<em>как<b>о́й</b>? → но́в<b>ой</b></em><br>
Yaʼni shaklni unutsangiz, savolni ayting va oxirini koʻchiring. Bu usul
deyarli har doim ishlaydi.</div>

<h3>4. Boshqa turdagi sifatlar</h3>

<p>Hamma sifat <em>но́вый</em> kabi emas. Ikkita yana bor, va ular ham
oʻsha naqsh boʻyicha ishlaydi — faqat unlisi boshqa:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Turi</th><th>И.п.</th><th>Р.п.</th><th>Д.п.</th><th>Т.п.</th><th>П.п.</th></tr>
  <tr><td class="pr-uz">oddiy</td><td class="pr-res">но́вый</td>
      <td class="pr-end">но́вого</td><td class="pr-end">но́вому</td>
      <td class="pr-end">но́вым</td><td class="pr-end">о но́вом</td></tr>
  <tr><td class="pr-uz">urgʻu oxirda</td><td class="pr-res">большо́й</td>
      <td class="pr-end">большо́го</td><td class="pr-end">большо́му</td>
      <td class="pr-end">больши́м</td><td class="pr-end">о большо́м</td></tr>
  <tr><td class="pr-uz">yumshoq</td><td class="pr-res">си́ний</td>
      <td class="pr-end">си́него</td><td class="pr-end">си́нему</td>
      <td class="pr-end">си́ним</td><td class="pr-end">о си́нем</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<em>Большо́й</em> da Т.п. shakli <b>больши́м</b> — <em>«большы́м»</em>
emas. Sababi oʻsha imlo qoidasi (PR-4): <b>Ш dan keyin Ы
yozilmaydi</b>. Xuddi shunday <em>ру́сским</em>, <em>хоро́шим</em>,
<em>ма́леньким</em> (К dan keyin).</div>

<h3>5. Gaplarda</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">Я живу́ <span class="pe-hl pe-hl--adv">в большо́м
     го́роде</span>, а рабо́таю <span class="pe-hl pe-hl--adv">в ма́леньком
     магази́не</span>.</p>
  <p class="pe-ex__uz">Katta shaharda yashayman, kichkina doʻkonda esa
     ishlayman.</p>
  <p class="pe-ex__why">Ikkalasi ham Предло́жный: sifat <b>-ом</b>, ot
     <b>-е</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Я говорю́ <span class="pe-hl pe-hl--o">с молоды́м
     води́телем</span> о <span class="pe-hl pe-hl--adv">ста́ром
     го́роде</span>.</p>
  <p class="pe-ex__uz">Yosh haydovchi bilan eski shahar haqida
     gaplashyapman.</p>
  <p class="pe-ex__why">Bitta gapda ikkita kelishik: Твори́тельный
     (<em>с молоды́м води́телем</em>) va Предло́жный (<em>о ста́ром
     го́роде</em>).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Я иду́ по <span class="pe-hl pe-hl--adv">широ́кой
     у́лице</span> к <span class="pe-hl pe-hl--o">но́вому до́му</span>.</p>
  <p class="pe-ex__uz">Keng koʻcha boʻylab yangi uy tomon ketyapman.</p>
  <p class="pe-ex__why">Ikkala predlog ham Да́тельный oladi (PR-38): ayol
     jinsi <b>-ой</b>, erkak jinsi <b>-ому</b>.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Kechagi gap bugun ham oʻz kuchida: oʻzbekcha sifat oʻzgarmaydi, ruschada
esa oʻzgaradi. Lekin bugun bitta muhim narsa qoʻshiladi.<br><br>
Oʻzbekchada <em>katta shahar<b>da</b></em> desangiz, <b>bitta</b>
qoʻshimcha qoʻyasiz. Ruschada esa <em>в больш<b>о́м</b>
го́род<b>е</b></em> — <b>ikkita</b> soʻz ham belgilanadi. Yaʼni ruscha bir
xil maʼlumotni <b>ikki marta</b> aytadi.<br><br>
Bu ortiqchadek koʻrinadi, lekin unda foyda bor: gapda soʻzlar
uzoq turgan boʻlsa ham, siz qaysi sifat qaysi otga tegishli ekanini
<b>oxiridan</b> bilib olasiz. Oʻzbekchada bu vazifani <b>soʻz
tartibi</b> bajaradi (sifat har doim otdan oldin). Ruscha esa soʻz
tartibini erkin qoldiradi va uning oʻrniga qoʻshimchaga
ishonadi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я живу́ в большо́й го́роде.</s></p>
  <p class="pe-good">Я живу́ <b>в большо́м го́роде</b> — erkak jins П.п. <b>-ом</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́ по широ́кому у́лице.</s></p>
  <p class="pe-good">по <b>широ́кой</b> у́лице — <em>у́лица</em> ayol jinsida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я говорю́ с молодо́й води́телем.</s></p>
  <p class="pe-good">с <b>молоды́м</b> води́телем — <em>води́тель</em> erkak jinsida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мы в большы́м до́ме.</s></p>
  <p class="pe-good">в <b>большо́м</b> до́ме — П.п. da <b>-ом</b>, va Ш dan keyin Ы yozilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ду́маю о но́вый до́ме.</s></p>
  <p class="pe-good">о <b>но́вом</b> до́ме — sifat ham Предло́жный'ga kiradi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Я живу́ в ___ го́роде.</b> (большо́й)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>большо́м</strong>. Предло́жный,
    erkak jins → <b>-ом</b>. Tekshiruv: <em>о как<b>о́м</b>? — о
    больш<b>о́м</b></em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Я иду́ по ___ у́лице.</b> (широ́кая)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>широ́кой</strong>. <em>По</em>
    Да́тельный oladi, ayol jinsi esa <b>-ой</b> — va bu shakl toʻrtta
    kelishikda ishlatiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Ayol jinsidagi sifat nechta kelishikda <b>-ой</b> boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Toʻrtta</strong>: Роди́тельный,
    Да́тельный, Твори́тельный, Предло́жный. Boshqacha shakl faqat
    <em>но́вая</em> (И.п.) va <em>но́вую</em> (В.п.).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga: <b>Я говорю́ с ___ дру́гом.</b> (ста́рый)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ста́рым</strong>. Твори́тельный,
    erkak jins → <b>-ым</b>. Tekshiruv: <em>с как<b>и́м</b>? — со
    ста́р<b>ым</b></em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Я живу́ в большо́м до́ме. &nbsp; б) Я иду́ к но́вому учи́телю.<br>
     в) Я говорю́ с молодо́й води́телем. &nbsp; г) Я ду́маю о ста́рой
     шко́ле.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>с молоды́м води́телем</b>. <em>Води́тель</em> erkak jinsida,
    shuning uchun sifat ham erkak jinsida boʻlishi kerak.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>большо́й → большо́м</b><span>katta (П.п.)</span></li>
  <li><b>ма́ленький</b><span>kichkina</span></li>
  <li><b>широ́кий</b><span>keng</span></li>
  <li><b>молодо́й</b><span>yosh</span></li>
  <li><b>си́ний</b><span>koʻk</span></li>
  <li><b>како́му? каки́м?</b><span>qanday? (Д.п., Т.п.)</span></li>
  <li><b>го́род</b><span>shahar</span></li>
  <li><b>у́лица</b><span>koʻcha</span></li>
  <li><b>кафе́</b><span>kafe</span></li>
  <li><b>свет</b><span>yorugʻlik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Д.п. <b>-ому</b> · Т.п. <b>-ым</b> · П.п. <b>-ом</b> (erkak va
        oʻrta).</li>
    <li>Ayol jinsi: <b>-ой</b> — toʻrtta kelishikda bitta shakl.</li>
    <li>Koʻplik: <b>-ым, -ыми, -ых</b> — jins yoʻq.</li>
    <li>Tekshiruv: <b>savol soʻzining oxiri sifatning oxiri bilan bir
        xil</b> — <em>како́му? → но́вому</em>.</li>
    <li>Ш, Ж, К, Г, Х dan keyin <b>-и</b>: <em>больши́м, ру́сским</em>.</li>
    <li>Ruscha maʼlumotni ikki marta aytadi (sifat + ot), shuning uchun
        soʻz tartibi erkin.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-45: Koʻplik kelishiklari 1 — Именительный va Родительный",
        "category": "russian",
        "order": 45,
        "summary": (
            "Bu kursning eng koʻp istisnoli darsi — va uni ochiq aytish kerak. "
            "Koʻplik Роди́тельный rus tilida eng koʻp yodlashni talab qiladigan "
            "shakl. Lekin uning ham tartibi bor."
        ),
        "stories": ["Пять дней без телефона"],
        "content": """
<h2>PR-45: Koʻplik kelishiklari 1 — Именительный va Родительный</h2>

<p>Sizni oldindan ogohlantiraman: <b>bu kursdagi eng koʻp istisnoli
dars</b>. Koʻplik Роди́тельный rus tilida eng koʻp yodlashni talab
qiladigan shakl, va buni yashirishning maʼnosi yoʻq. Lekin ikkita narsa
sizni qutqaradi: birinchidan, tartib bor — istisnolar tasodifiy emas.
Ikkinchidan, <b>keyingi dars kursdagi eng osoni</b>, va u ertaga keladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Koʻplik bosh kelishigini yasaysiz: <b>-Ы/-И</b> va <b>-А/-Я</b></li>
    <li>Erkak jinsdagi <b>-А</b> istisnolarini bilasiz: <b>дома́,
        города́</b></li>
    <li>Koʻplik Роди́тельный'ning uchta naqshini oʻrganasiz</li>
    <li>Eng koʻp kerak boʻladigan notoʻgʻri shakllarni yodlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Koʻplik</span>
  <span class="pe-chip pe-chip--s">стол → столы́</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">пять стол<b>о́в</b></span>
</div>

<h3>1. Bosh kelishik koʻpligi</h3>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">-<span class="pr-end">ы</span> / -<span class="pr-end">и</span></p>
    <p><em>стол → столы́</em><br><em>врач → врачи́</em><br>
       <em>рубль → рубли́</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">-<span class="pr-end">ы</span> / -<span class="pr-end">и</span></p>
    <p><em>шко́ла → шко́лы</em><br><em>кни́га → кни́ги</em><br>
       <em>неде́ля → неде́ли</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний — oʻrta</p>
    <p class="pr-gender__form">-<span class="pr-end">а</span> / -<span class="pr-end">я</span></p>
    <p><em>окно́ → о́кна</em><br><em>сло́во → слова́</em><br>
       <em>мо́ре → моря́</em></p>
  </div>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Erkak jinsdagi bir guruh ot <b>-Ы</b> emas, <b>-А́</b> oladi — va ular juda
koʻp ishlatiladi, shuning uchun roʻyxatni yodlash kerak:<br>
<em>дом → дом<b>а́</b></em> · <em>го́род → город<b>а́</b></em> ·
<em>учи́тель → учител<b>я́</b></em> · <em>до́ктор → доктор<b>а́</b></em> ·
<em>ве́чер → вечер<b>а́</b></em> · <em>по́езд → поезд<b>а́</b></em> ·
<em>глаз → глаз<b>а́</b></em> · <em>па́спорт → паспорт<b>а́</b></em><br>
Ularda urgʻu har doim oxirida. Eslash uchun: bular kundalik hayotdagi eng
koʻp uchraydigan narsalar.</div>

<h3>2. Butunlay notoʻgʻri koʻpliklar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Birlik</th><th>Koʻplik</th><th>Koʻplik Р.п.</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">челове́к</td><td class="pr-end">лю́ди</td>
      <td class="pr-end">люде́й</td><td class="pr-uz">odam(lar)</td></tr>
  <tr><td class="pr-res">ребёнок</td><td class="pr-end">де́ти</td>
      <td class="pr-end">дете́й</td><td class="pr-uz">bola(lar)</td></tr>
  <tr><td class="pr-res">друг</td><td class="pr-end">друзья́</td>
      <td class="pr-end">друзе́й</td><td class="pr-uz">doʻst(lar)</td></tr>
  <tr><td class="pr-res">брат</td><td class="pr-end">бра́тья</td>
      <td class="pr-end">бра́тьев</td><td class="pr-uz">aka(lar)</td></tr>
  <tr><td class="pr-res">сын</td><td class="pr-end">сыновья́</td>
      <td class="pr-end">сынове́й</td><td class="pr-uz">oʻgʻil(lar)</td></tr>
  <tr><td class="pr-res">де́рево</td><td class="pr-end">дере́вья</td>
      <td class="pr-end">дере́вьев</td><td class="pr-uz">daraxt(lar)</td></tr>
  <tr><td class="pr-res">стул</td><td class="pr-end">сту́лья</td>
      <td class="pr-end">сту́льев</td><td class="pr-uz">stul(lar)</td></tr>
  <tr><td class="pr-res">год</td><td class="pr-end">го́ды</td>
      <td class="pr-end">лет</td><td class="pr-uz">yil(lar)</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bu roʻyxatni bir kunda yodlashga urinmang. Uni <b>ishlatib</b>
yodlang — bular oila, doʻstlar va vaqt haqidagi soʻzlar, yaʼni siz ularni
har kuni aytasiz. <em>Мои́ друзья́</em>, <em>на́ши де́ти</em>,
<em>пять лет</em> — bir hafta ichida ular oʻz-oʻzidan
oʻtirib qoladi.</div>

<h3>3. Koʻplik Роди́тельный — uchta naqsh</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Qanday ot</th><th>Qoʻshimcha</th><th>Misollar</th></tr>
  <tr><td class="pr-uz">erkak, undosh bilan</td><td class="pr-res">-ОВ</td>
      <td class="pr-end">дом → домо́в · стол → столо́в · час → часо́в</td></tr>
  <tr><td class="pr-uz">erkak, Ж Ш Щ Ч yoki -Ь</td><td class="pr-res">-ЕЙ</td>
      <td class="pr-end">врач → враче́й · рубль → рубле́й</td></tr>
  <tr><td class="pr-uz">ayol -А, oʻrta -О</td><td class="pr-res">qoʻshimcha yoʻq</td>
      <td class="pr-end">кни́га → книг · окно́ → о́кон · сло́во → слов</td></tr>
  <tr><td class="pr-uz">ayol -Ь, oʻrta -Е</td><td class="pr-res">-ЕЙ</td>
      <td class="pr-end">тетра́дь → тетра́дей · мо́ре → море́й</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Uchinchi qatorga alohida qarang — u eng gʻalati koʻrinadi, lekin aslida
eng oson: <b>ayol va oʻrta jins oxirgi unlisini yoʻqotadi</b> va soʻz
«yalangʻoch» qoladi: <em>кни́г-а → книг</em>, <em>сло́в-о → слов</em>.
Faqat talaffuz qiyin boʻlsa, ichkariga unli qoʻshiladi:
<em>окн-о → о́к<b>о</b>н</em>, <em>де́вушк-а → де́вуш<b>е</b>к</em>.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Ochiq gapiramiz: bu dars oʻzbek oʻquvchi uchun <b>eng qiyin</b>
darslardan biri, va sabab oddiy.<br><br>
Oʻzbekchada koʻplik <b>bitta qoʻshimcha</b>: <em>-lar</em>.
<em>Kitob<b>lar</b>, uy<b>lar</b>, odam<b>lar</b>, bola<b>lar</b></em> —
istisno deyarli yoʻq. Va u kelishik qoʻshimchasidan <b>oldin</b> turadi:
<em>kitob-lar-<b>ni</b></em>, <em>kitob-lar-<b>ga</b></em> — yaʼni ikkita
qoʻshimcha bir-biriga xalaqit bermaydi.<br><br>
Ruschada esa koʻplik <b>butun soʻzni qayta yasaydi</b>:
<em>челове́к → лю́ди</em>, <em>друг → друзья́</em>,
<em>ребёнок → де́ти</em>. Bu yerda hech qanday mantiq yoʻq — faqat
tarix.<br><br>
Shuning uchun bu darsda strategiya boshqacha: <b>qoidani emas,
soʻzlarni</b> yodlang. Va yodda tuting — bu eng qiyin joyi. Undan
keyin osonlashadi, va aynan <b>ertaga</b> osonlashadi.</div>

<h3>4. Amalda — sonlar bilan</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">У меня́ <span class="pe-hl pe-hl--o">три дру́га</span>.
     А у него́ <span class="pe-hl pe-hl--o">мно́го друзе́й</span>.</p>
  <p class="pe-ex__uz">Mening uchta doʻstim bor. Uning esa koʻp doʻstlari
     bor.</p>
  <p class="pe-ex__why">PR-36 dagi qoida: 2-3-4 → Роди́тельный
     <b>birlik</b> (<em>дру́га</em>), <em>мно́го</em> → Роди́тельный
     <b>koʻplik</b> (<em>друзе́й</em>).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Во дворе́ мно́го
     <span class="pe-hl pe-hl--o">дере́вьев</span> и
     <span class="pe-hl pe-hl--o">дете́й</span>.</p>
  <p class="pe-ex__uz">Hovlida koʻp daraxt va bola bor.</p>
  <p class="pe-ex__why">Ikkalasi ham notoʻgʻri koʻplik:
     <em>де́рево → дере́вья → дере́вьев</em>,
     <em>ребёнок → де́ти → дете́й</em>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>мно́го челове́ков</s></p>
  <p class="pe-good">мно́го <b>люде́й</b> — <em>челове́к</em> ning koʻpligi butunlay boshqa</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>мои́ дру́ги</s></p>
  <p class="pe-good">мои́ <b>друзья́</b> — notoʻgʻri koʻplik</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>пять кни́гов</s></p>
  <p class="pe-good">пять <b>книг</b> — ayol jinsi qoʻshimchasini yoʻqotadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то мои́ до́мы.</s></p>
  <p class="pe-good">Э́то мои́ <b>дома́</b> — <em>дом</em> <b>-а́</b> roʻyxatida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>де́сять годо́в</s></p>
  <p class="pe-good">де́сять <b>лет</b> — bu shakl alohida yodlanadi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Koʻplikka qoʻying: <b>дом · кни́га · окно́</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>дома́ · кни́ги · о́кна</strong>.
    <em>Дом</em> — <b>-а́</b> roʻyxatidan (urgʻu oxirida!), <em>кни́га</em>
    — oddiy <b>-и</b> (К dan keyin), <em>окно́</em> — oʻrta jins
    <b>-а</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>У меня́ мно́го ___.</b> (друг)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>друзе́й</strong>. Ikki qadam:
    koʻplik <em>друзья́</em> (notoʻgʻri), keyin Роди́тельный
    <em>друзе́й</em>. Bu soʻz ikkala shaklda ham alohida
    yodlanadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>В кла́ссе два́дцать ___.</b> (учени́к)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ученико́в</strong>. Erkak jins,
    undosh bilan tugaydi → <b>-ов</b>. Va 20 — 5 dan yuqori, demak
    koʻplik Роди́тельный (PR-36).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga: <b>Здесь мно́го ___.</b> (челове́к)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>люде́й</strong>. <em>Мно́го</em>
    bilan <em>челове́к</em> ning koʻplik shakli ishlatiladi —
    <em>лю́ди → люде́й</em>. Lekin <b>son</b> bilan boshqacha:
    <em>пять челове́к</em> (PR-36).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi qatorda hammasi toʻgʻri?<br>
     а) дома́ · друзья́ · де́ти<br>
     б) до́мы · друзья́ · де́ти<br>
     в) дома́ · дру́ги · ребёнки<br>
     г) дома́ · друзья́ · ребёнки</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>а)</strong>. Uchtasi ham
    notoʻgʻri koʻplik: <em>дом → дома́</em> (<b>-а́</b> roʻyxati),
    <em>друг → друзья́</em>, <em>ребёнок → де́ти</em>. Bunday shakllar
    yodlanadi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>лю́ди → люде́й</b><span>odamlar</span></li>
  <li><b>де́ти → дете́й</b><span>bolalar</span></li>
  <li><b>друзья́ → друзе́й</b><span>doʻstlar</span></li>
  <li><b>бра́тья</b><span>akalar</span></li>
  <li><b>дере́вья</b><span>daraxtlar</span></li>
  <li><b>дома́</b><span>uylar</span></li>
  <li><b>города́</b><span>shaharlar</span></li>
  <li><b>глаза́</b><span>koʻzlar</span></li>
  <li><b>дни</b><span>kunlar</span></li>
  <li><b>но́вости</b><span>yangiliklar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Koʻplik И.п.: erkak va ayol <b>-Ы/-И</b>, oʻrta <b>-А/-Я</b>.</li>
    <li>Erkak jinsdagi <b>-А́</b> roʻyxati: <em>дома́, города́,
        учителя́, вечера́, поезда́, глаза́</em>.</li>
    <li>Notoʻgʻri koʻpliklar: <b>лю́ди, де́ти, друзья́, бра́тья,
        дере́вья, сту́лья</b>.</li>
    <li>Koʻplik Р.п.: erkak <b>-ОВ / -ЕЙ</b>, ayol va oʻrta —
        <b>qoʻshimchasiz</b>.</li>
    <li>Oʻzbekcha <em>-lar</em> istisnosiz, ruscha koʻplik esa baʼzan
        <b>butun soʻzni qayta yasaydi</b>. Bu yerda qoidani emas,
        soʻzlarni yodlang.</li>
    <li>Bu eng qiyin joyi. <b>Ertangi dars — eng osoni.</b></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-46: Koʻplik kelishiklari 2 — Дательный, Винительный, Творительный, Предложный",
        "category": "russian",
        "order": 46,
        "summary": (
            "Kechagi vaʼda bajariladi: bu — butun blokdagi eng oson dars. Uchta "
            "qoʻshimcha, jins umuman yoʻq, istisno deyarli yoʻq. Va shu bilan "
            "kelishiklar tugaydi."
        ),
        "stories": ["Письмо всем друзьям"],
        "content": """
<h2>PR-46: Koʻplik kelishiklari 2 — Дательный, Винительный, Творительный, Предложный</h2>

<p>Kecha men sizga bir narsani vaʼda qilgan edim: «ertangi dars eng
osoni». Mana u. Koʻplikda qolgan kelishiklar <b>jinsga umuman
qaramaydi</b> — erkak, ayol, oʻrta, hammasi bir xil qoʻshimcha oladi.
Uchta qoʻshimcha, tamom. Va bu dars bilan <b>butun kelishik tizimi</b>
yopiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uchta qoʻshimchani oʻrganasiz: <b>-АМ, -АМИ, -АХ</b></li>
    <li>Koʻplikda jins yoʻqolishini koʻrasiz</li>
    <li>Вини́тельный'ning jonlilikka qarab tanlanishini bilasiz</li>
    <li>Ikkita istisnoni yodlaysiz: <b>детьми́, людьми́</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uchta qoʻshimcha</span>
  <span class="pe-chip pe-chip--v">-ам</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">-ами</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">-ах</span>
</div>

<h3>1. Jins yoʻqoladi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kelishik</th><th>дома́ (erkak)</th><th>кни́ги (ayol)</th><th>о́кна (oʻrta)</th></tr>
  <tr><td class="pr-uz">Да́тельный</td><td class="pr-end">дома́м</td>
      <td class="pr-end">кни́гам</td><td class="pr-end">о́кнам</td></tr>
  <tr><td class="pr-uz">Твори́тельный</td><td class="pr-end">дома́ми</td>
      <td class="pr-end">кни́гами</td><td class="pr-end">о́кнами</td></tr>
  <tr><td class="pr-uz">Предло́жный</td><td class="pr-end">о дома́х</td>
      <td class="pr-end">о кни́гах</td><td class="pr-end">об о́кнах</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Jadvalga qarang va bir narsani payqang: <b>uchta ustun ham bir xil</b>.
Faqat oʻzak boshqa. Butun blok davomida siz jins bilan kurashdingiz — va
koʻplikda u <b>umuman yoʻqoladi</b>.<br><br>
Yodlash uchun uchta bogʻin kifoya: <b>АМ — АМИ — АХ</b>. Ovoz chiqarib
uch marta ayting. Bu — rus kelishik tizimidagi eng oson narsa.<br><br>
Yumshoq oʻzaklarda ular <em>-ЯМ, -ЯМИ, -ЯХ</em> boʻladi
(<em>моря́м, моря́ми, о моря́х</em>) — lekin bu bir xil qoʻshimcha, faqat
yumshoq variantda.</div>

<h3>2. Вини́тельный — oʻsha jonlilik qoidasi</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Jonsiz = Имени́тельный</p>
    <p><em>Я ви́жу <b>дома́</b>.</em><br>
       <em>Я чита́ю <b>кни́ги</b>.</em></p>
    <p>Shakl bosh kelishik bilan bir xil.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Jonli = Роди́тельный</p>
    <p><em>Я ви́жу <b>друзе́й</b>.</em><br>
       <em>Я жду <b>дете́й</b>.</em></p>
    <p>Shakl koʻplik Роди́тельный bilan bir xil (PR-45).</p>
  </div>
</div>

<p>Yaʼni Вини́тельный koʻplikda ham <b>yangi shakl yaratmaydi</b> — u yo
И.п. ni, yo Р.п. ni takrorlaydi. Bu PR-32 dagi qoidaning oʻsha oʻzi,
faqat endi koʻplikda.</p>

<h3>3. Ikkita istisno</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Д.п.</th><th>Т.п.</th><th>П.п.</th></tr>
  <tr><td class="pr-res">де́ти</td><td class="pr-end">де́тям</td>
      <td class="pr-end">детьми́ <em>(!)</em></td><td class="pr-end">о де́тях</td></tr>
  <tr><td class="pr-res">лю́ди</td><td class="pr-end">лю́дям</td>
      <td class="pr-end">людьми́ <em>(!)</em></td><td class="pr-end">о лю́дях</td></tr>
  <tr><td class="pr-res">друзья́</td><td class="pr-end">друзья́м</td>
      <td class="pr-end">друзья́ми</td><td class="pr-end">о друзья́х</td></tr>
  <tr><td class="pr-res">дере́вья</td><td class="pr-end">дере́вьям</td>
      <td class="pr-end">дере́вьями</td><td class="pr-end">о дере́вьях</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Детьми́</b> va <b>людьми́</b> — <em>«де́тями»</em>, <em>«лю́дями»</em>
emas. Bu ikkitasi butun tizimda yagona istisno, va ular juda koʻp
ishlatiladi:<br>
<em>Я говорю́ <b>с людьми́</b></em> — odamlar bilan gaplashaman.<br>
<em>Она́ рабо́тает <b>с детьми́</b></em> — bolalar bilan ishlaydi.<br>
Ikkitasini birga yodlang — ular qofiyalanadi.</div>

<h3>4. Sifat bilan birga</h3>

<p>Sifatning koʻplik shakllari PR-44 dan tanish, va ular bu yerda ot bilan
birga ishlaydi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kelishik</th><th>Sifat</th><th>Ot</th><th>Birga</th></tr>
  <tr><td class="pr-uz">Да́тельный</td><td class="pr-res">но́вым</td>
      <td class="pr-res">друзья́м</td><td class="pr-end">но́вым друзья́м</td></tr>
  <tr><td class="pr-uz">Твори́тельный</td><td class="pr-res">ра́зными</td>
      <td class="pr-res">людьми́</td><td class="pr-end">с ра́зными людьми́</td></tr>
  <tr><td class="pr-uz">Предло́жный</td><td class="pr-res">ста́рых</td>
      <td class="pr-res">друзья́х</td><td class="pr-end">о ста́рых друзья́х</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ru">Я пишу́ <span class="pe-hl pe-hl--o">ста́рым
     друзья́м</span> и рабо́таю <span class="pe-hl pe-hl--o">с ра́зными
     людьми́</span>.</p>
  <p class="pe-ex__uz">Eski doʻstlarga yozaman va turli odamlar bilan
     ishlayman.</p>
  <p class="pe-ex__why">Ikkita kelishik: Да́тельный (<em>-ым …-ям</em>) va
     Твори́тельный (<em>-ыми …-ьми́</em>). Sifat va ot birga
     oʻzgardi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Va mana bu yerda oʻzbekcha nihoyat <b>toʻliq yordam beradi</b>.<br><br>
Oʻzbekchada koʻplik va kelishik <b>alohida ikkita qoʻshimcha</b>:<br>
<em>doʻst-<b>lar</b>-<b>ga</b></em> · <em>doʻst-<b>lar</b>-<b>da</b></em> ·
<em>doʻst-<b>lar</b>-<b>dan</b></em><br>
Ruschada ham xuddi shunday ishlaydi — koʻplik oʻzagi bir marta yasaladi,
keyin unga kelishik qoʻshimchasi qoʻyiladi:<br>
<em>друзь-<b>я́м</b></em> · <em>о друзь-<b>я́х</b></em> ·
<em>с друзь-<b>я́ми</b></em><br><br>
Ikkala tilda ham jins koʻplikda ahamiyatini yoʻqotadi. Shuning uchun bu
dars siz uchun tabiiy tuyuladi: koʻplikda ruscha oʻzbekchaga
<b>eng yaqin</b> holatga keladi.</div>

<h3>5. Kelishiklar bloki yopildi</h3>

<p>PR-29 da siz xaritani koʻrgan edingiz. Oʻn sakkiz dars oʻtdi va endi
xaritada <b>boʻsh joy qolmadi</b>: oltita kelishik, otlarda, olmoshlarda,
egalik olmoshlarida, sifatlarda va koʻplikda.</p>

<p>Keyingi darslarda (PR-47…50) yangi tizim yoʻq — ular <b>mustahkamlash
va tartibga solish</b>: soʻroq soʻzlari, predloglar xaritasi, sana va
vaqt, va yakuniy takror. Shundan keyin Block E boshlanadi — feʼl turi
(вид), rus tilining ikkinchi katta tizimi.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я говорю́ с лю́дями.</s></p>
  <p class="pe-good">Я говорю́ <b>с людьми́</b> — ikkita istisnodan biri</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Она́ рабо́тает с де́тями.</s></p>
  <p class="pe-good">Она́ рабо́тает <b>с детьми́</b> — ikkinchi istisno</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я пишу́ ста́рым друзьёв.</s></p>
  <p class="pe-good">Я пишу́ ста́рым <b>друзья́м</b> — Да́тельный <b>-ям</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ду́маю о друзья́м.</s></p>
  <p class="pe-good">Я ду́маю <b>о друзья́х</b> — Предло́жный <b>-ях</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ви́жу друзья́.</s></p>
  <p class="pe-good">Я ви́жу <b>друзе́й</b> — jonli, demak Роди́тельный shakli</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Я пишу́ ___.</b> (друзья́)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>друзья́м</strong>. <em>Писа́ть</em>
    Да́тельный oladi (PR-37), koʻplik Да́тельный esa <b>-ам / -ям</b>.
    Yumshoq oʻzak, demak <b>-ям</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Я говорю́ с ___.</b> (лю́ди)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>людьми́</strong> —
    <em>«лю́дями»</em> emas! Bu ikkita istisnodan biri. Ikkinchisi —
    <em>детьми́</em>. Ular qofiyalanadi, shuning uchun birga
    yodlanadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Я ду́маю о ___.</b> (но́вые города́)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>но́вых города́х</strong>.
    Предло́жный koʻplik: sifat <b>-ых</b>, ot <b>-ах</b>. Jins bu yerda
    umuman ishlamaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu ikki gapdan qaysi birida shakl oʻzgaradi va nega?<br>
     <b>Я ви́жу дома́. · Я ви́жу друзе́й.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Ikkinchisida. <em>Друзья́</em> —
    <strong>jonli</strong>, shuning uchun Вини́тельный Роди́тельный
    shaklini oladi: <em>друзе́й</em>. <em>Дома́</em> jonsiz, demak
    oʻzgarmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Я пишу́ ста́рым друзья́м. &nbsp; б) Я ду́маю о де́тях.<br>
     в) Я говорю́ с лю́дями. &nbsp; г) Я ви́жу но́вые дома́.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>с людьми́</b>. Qolgan uchtasi toʻgʻri: <em>друзья́м</em> (Д.п.
    <b>-ям</b>), <em>о де́тях</em> (П.п. <b>-ях</b>), <em>но́вые дома́</em>
    (В.п., jonsiz — oʻzgarmaydi).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>-ам / -ями / -ах</b><span>koʻplik Д./Т./П.</span></li>
  <li><b>друзья́м</b><span>doʻstlarga</span></li>
  <li><b>с людьми́</b><span>odamlar bilan</span></li>
  <li><b>с детьми́</b><span>bolalar bilan</span></li>
  <li><b>о города́х</b><span>shaharlar haqida</span></li>
  <li><b>глаза́ми</b><span>koʻzlar bilan</span></li>
  <li><b>ра́зные</b><span>turli</span></li>
  <li><b>дороги́е</b><span>aziz(lar)</span></li>
  <li><b>разгово́р</b><span>suhbat</span></li>
  <li><b>сле́дующий</b><span>keyingi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Koʻplikda <b>jins yoʻqoladi</b> — uchta jins uchun bitta
        qoʻshimcha.</li>
    <li><b>АМ — АМИ — АХ</b> (yumshoq oʻzakda <b>ЯМ — ЯМИ — ЯХ</b>).</li>
    <li>Вини́тельный yangi shakl yaratmaydi: jonsiz = И.п., jonli =
        Р.п.</li>
    <li>Ikkita istisno: <b>детьми́</b> va <b>людьми́</b>.</li>
    <li>Sifat ham koʻplikda jinssiz: <b>-ым, -ыми, -ых</b>.</li>
    <li>Oʻzbekchada ham koʻplik va kelishik alohida qoʻshimchalar
        (<em>doʻst-lar-ga</em>) — bu yerda ikki til eng yaqin turadi.</li>
    <li><b>Kelishiklar bloki yopildi.</b> PR-47…50 — mustahkamlash.</li>
  </ul>
</div>
""",
    },
]
