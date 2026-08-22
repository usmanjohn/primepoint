# -*- coding: utf-8 -*-
"""Prime Russian — Block E yakuni va Block F boshlanishi (62–64).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-62 — -ся ning oltita maʼnosi. Blok E ni yopadi. Bu darsning oʻzbekcha
tayanchi juda kuchli: oʻzbekchada UCHTA alohida qoʻshimcha bor (-in-, -ish-,
-il-), ruschada esa BITTA — shuning uchun rus bolasi hech oʻylamaydigan
narsani oʻzbek oʻquvchisi darrov tushunadi.
PR-63 — который. Blok F ochiladi. Asosiy gʻoya: oʻzbekcha sifatdosh gap
otdan OLDIN turadi, ruscha ergash gap esa KEYIN.
PR-64 — что va чтобы. Bitta harf farq, ikki xil gap: fakt ↔ maqsad/istak.

Mashqlar:        practice/management/commands/_practice_pr_62_64.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_62_64.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_62_64.py --author=prime
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
        "title": "PR-62: -ся feʼlining oltita maʼnosi — bir qoʻshimcha, olti vazifa",
        "category": "russian",
        "order": 62,
        "summary": (
            "Ruschada bitta -ся, oʻzbekchada esa uchta alohida qoʻshimcha: -in-, "
            "-ish-, -il-. Shuning uchun bu dars siz uchun ruslardan osonroq."
        ),
        "stories": ["Шесть значе́ний одно́й ча́стицы"],
        "content": """
<h2>PR-62: -ся feʼlining oltita maʼnosi — bir qoʻshimcha, olti vazifa</h2>

<p>Siz <b>-ся</b> ni allaqachon koʻp marta koʻrgansiz: <em>учи́ться,
нра́виться, начина́ться, стро́иться</em>. Endi uni bir joyga yigʻamiz.
Bu qoʻshimchaning butun qiyinligi shundaki, u <b>bitta</b>, lekin
vazifasi <b>olti xil</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>-ся</b> va <b>-сь</b> ni qachon yozishni bilasiz</li>
    <li>Oltita maʼnoni ajratasiz</li>
    <li>Bitta qatʼiy qoidani eslab qolasiz: <b>-ся feʼli tushum kelishigini olmaydi</b></li>
    <li>Oʻzbekcha uchta qoʻshimchani ruscha bittasiga bogʻlaysiz</li>
  </ul>
</div>

<h3>1. Shakli — bu eng oson qismi</h3>

<div class="pe-formula">
  <span class="pe-formula__label">Qoida</span>
  <span class="pe-chip pe-chip--s">undoshdan keyin</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">-СЯ</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">unlidan keyin</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">-СЬ</span>
</div>

<div class="pe-table-wrap"><table class="pr-conj">
  <tr><th>Shaxs</th><th>учи́ться</th><th>Izoh</th></tr>
  <tr><td class="pr-uz">я</td><td class="pr-end">учу́<b>сь</b></td>
      <td class="pr-uz">у — unli</td></tr>
  <tr><td class="pr-uz">ты</td><td class="pr-end">у́чишь<b>ся</b></td>
      <td class="pr-uz">ь — undosh</td></tr>
  <tr><td class="pr-uz">он / она́</td><td class="pr-end">у́чит<b>ся</b></td>
      <td class="pr-uz">т</td></tr>
  <tr><td class="pr-uz">мы</td><td class="pr-end">у́чим<b>ся</b></td>
      <td class="pr-uz">м</td></tr>
  <tr><td class="pr-uz">вы</td><td class="pr-end">у́чите<b>сь</b></td>
      <td class="pr-uz">е — unli</td></tr>
  <tr><td class="pr-uz">они́</td><td class="pr-end">у́чат<b>ся</b></td>
      <td class="pr-uz">т</td></tr>
</table></div>

<p>Oʻtgan zamonda ham xuddi shunday: <em>учи́л<b>ся</b> · учи́ла<b>сь</b> ·
учи́ли<b>сь</b></em>. Buyruqda: <em>учи́<b>сь</b> · учи́те<b>сь</b></em>.</p>

<h3>2. Oltita maʼno</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>#</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-res">1</td><td class="pr-uz">oʻziga qaytish</td>
      <td class="pr-end">Он <b>мо́ется</b> — u yuvinyapti</td></tr>
  <tr><td class="pr-res">2</td><td class="pr-uz">bir-biriga</td>
      <td class="pr-end">Мы <b>встреча́емся</b> — biz uchrashamiz</td></tr>
  <tr><td class="pr-res">3</td><td class="pr-uz">majhul nisbat</td>
      <td class="pr-end">Дом <b>стро́ится</b> — uy qurilyapti</td></tr>
  <tr><td class="pr-res">4</td><td class="pr-uz">shaxssiz holat</td>
      <td class="pr-end">Мне не <b>спи́тся</b> — uyqum kelmayapti</td></tr>
  <tr><td class="pr-res">5</td><td class="pr-uz">faqat -ся bilan yashaydi</td>
      <td class="pr-end">Он <b>смеётся</b> — u kulyapti</td></tr>
  <tr><td class="pr-res">6</td><td class="pr-uz">maʼno butunlay oʻzgaradi</td>
      <td class="pr-end">учи́ть → <b>учи́ться</b> — oʻrgatmoq → oʻqimoq</td></tr>
</table></div>

<h3>3. Har birini yaqindan</h3>

<div class="pe-ex">
  <p class="pe-ex__t">1 — oʻziga qaytish (возвра́тное)</p>
  <p><em>мыть</em> — yuvmoq &nbsp;→&nbsp; <em><b>мы́ться</b></em> — yuvinmoq<br>
     <em>одева́ть</em> — kiydirmoq &nbsp;→&nbsp; <em><b>одева́ться</b></em> — kiyinmoq<br>
     <em>гото́вить</em> — tayyorlamoq &nbsp;→&nbsp; <em><b>гото́виться</b></em> — tayyorlanmoq</p>
  <p class="pe-ex__n">Harakat oʻzingizga qaytadi. <b>-ся = «oʻzini»</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">2 — bir-biriga (взаи́мное)</p>
  <p><em><b>встреча́ться</b></em> — uchrashmoq · <em><b>ссо́риться</b></em> — urushmoq<br>
     <em><b>обнима́ться</b></em> — quchoqlashmoq · <em><b>перепи́сываться</b></em> — yozishmoq</p>
  <p class="pe-ex__n">Kamida ikki kishi kerak: <em>Они́ <b>встреча́ются</b>
     ка́ждую суббо́ту.</em></p>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">3 — majhul nisbat (PR-61 dan)</p>
  <p><em>Дом <b>стро́ится</b>. · Магази́н <b>открыва́ется</b> в де́вять. ·
     Кни́га <b>чита́ется</b> легко́.</em></p>
  <p class="pe-ex__n">Faqat <b>НСВ</b> feʼllardan va faqat uchinchi shaxsda.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">4 — shaxssiz holat</p>
  <p><em>Мне не <b>спи́тся</b>.</em> — Uyqum kelmayapti.<br>
     <em>Мне <b>хо́чется</b> ко́фе.</em> — Kofe ichgim kelyapti.<br>
     <em>Мне <b>ка́жется</b>, э́то оши́бка.</em> — Menimcha, bu xato.</p>
  <p class="pe-ex__n">Ega yoʻq, odam esa <b>Да́тельный</b> kelishigida:
     <em>мне, тебе́, ему́</em>. PR-81 da bu toʻliq koʻriladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">5 — faqat -ся bilan yashaydi</p>
  <p><em><b>смея́ться</b></em> — kulmoq · <em><b>боя́ться</b></em> — qoʻrqmoq<br>
     <em><b>наде́яться</b></em> — umid qilmoq · <em><b>улыба́ться</b></em> — jilmaymoq<br>
     <em><b>стара́ться</b></em> — harakat qilmoq · <em><b>нра́виться</b></em> — yoqmoq</p>
  <p class="pe-ex__n"><em>«Смеять»</em> degan feʼl <b>yoʻq</b>. Bularni shunchaki
     -ся bilan birga yodlang.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">6 — maʼno oʻzgaradi</p>
  <p><em>учи́ть</em> (oʻrgatmoq) → <em><b>учи́ться</b></em> (oʻqimoq)<br>
     <em>находи́ть</em> (topmoq) → <em><b>находи́ться</b></em> (joylashmoq)<br>
     <em>занима́ть</em> (band qilmoq) → <em><b>занима́ться</b></em> (shugʻullanmoq)<br>
     <em>догова́ривать</em> (aytib boʻlmoq) → <em><b>догова́риваться</b></em> (kelishmoq)</p>
  <p class="pe-ex__n">Bu eng xavfli guruh: shakl oʻxshash, maʼno boshqa.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Bitta qatʼiy qoida</span>
<b>-ся feʼli hech qachon tushum kelishigini (Вини́тельный) olmaydi.</b><br><br>
<em>Он мо́ет <b>маши́ну</b>.</em> — u mashinani yuvyapti (obyekt bor)<br>
<em>Он мо́ется.</em> — u yuvinyapti (obyekt yoʻq)<br><br>
Shuning uchun <em>«Он мо́ется маши́ну»</em> mumkin emas. Agar gapda
«nimani?» degan soʻz boʻlsa — <b>-ся ni olib tashlang</b>.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana bu darsning eng foydali joyi. Oʻzbekchada bu vazifalarga
<b>uchta alohida qoʻshimcha</b> bor, ruschada esa <b>bitta</b>:<br><br>
<em>yuv<b>in</b>moq, kiy<b>in</b>moq</em> &nbsp;→&nbsp; <b>-ся</b> (1-maʼno)<br>
<em>koʻr<b>ish</b>moq, yoz<b>ish</b>moq</em> &nbsp;→&nbsp; <b>-ся</b> (2-maʼno)<br>
<em>qur<b>il</b>moq, yoz<b>il</b>moq</em> &nbsp;→&nbsp; <b>-ся</b> (3-maʼno)<br><br>
Yaʼni oʻzbekcha aniqroq, ruscha esa tejamkor. Siz uchun bu <b>afzallik</b>:
rus bolasi bu maʼnolarni umuman ajratmaydi, siz esa ona tilingizda
ularni allaqachon ajratasiz. Ruscha gapni oʻzbekchaga oʻgirganda oʻzingizga
savol bering: «bu yerda -in-mi, -ish-mi, yoki -il-mi?» — javob sizga
maʼnoni aytib beradi.</div>

<h3>4. -ся feʼllari va kelishiklar</h3>

<p>Obyekt olmaslik <b>hech narsa olmaslik</b> degani emas. Koʻpchilik
-ся feʼllari oʻz kelishigini talab qiladi, va uni feʼl bilan birga
yodlash kerak:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Feʼl</th><th>Kelishik</th><th>Misol</th></tr>
  <tr><td class="pr-res">боя́ться</td><td class="pr-uz">Роди́тельный</td>
      <td class="pr-end">Он бои́тся <b>соба́к</b>. — itlardan qoʻrqadi</td></tr>
  <tr><td class="pr-res">занима́ться</td><td class="pr-uz">Твори́тельный</td>
      <td class="pr-end">Я занима́юсь <b>спо́ртом</b>. — sport bilan shugʻullanaman</td></tr>
  <tr><td class="pr-res">интересова́ться</td><td class="pr-uz">Твори́тельный</td>
      <td class="pr-end">Она́ интересу́ется <b>исто́рией</b>.</td></tr>
  <tr><td class="pr-res">по́льзоваться</td><td class="pr-uz">Твори́тельный</td>
      <td class="pr-end">Я по́льзуюсь <b>словарём</b>.</td></tr>
  <tr><td class="pr-res">нра́виться</td><td class="pr-uz">Да́тельный</td>
      <td class="pr-end"><b>Мне</b> нра́вится э́тот го́род.</td></tr>
  <tr><td class="pr-res">гото́виться</td><td class="pr-uz">к + Да́тельный</td>
      <td class="pr-end">Я гото́влюсь <b>к экза́мену</b>.</td></tr>
  <tr><td class="pr-res">встреча́ться</td><td class="pr-uz">с + Твори́тельный</td>
      <td class="pr-end">Я встреча́юсь <b>с дру́гом</b>.</td></tr>
</table></div>

<p>Eʼtibor bering: bularning hech qaysisi Вини́тельный emas. Qoida
buzilmayapti.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я учу́сь брата матема́тике.</s></p>
  <p class="pe-good">Я <b>учу́</b> бра́та матема́тике — obyekt bor, demak -ся yoʻq</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он смея́л.</s></p>
  <p class="pe-good">Он <b>смея́лся</b> — bu feʼl -ся siz yashamaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я учу́ся.</s></p>
  <p class="pe-good">Я <b>учу́сь</b> — unlidan keyin <b>-сь</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Библиоте́ка нахо́дит в це́нтре.</s></p>
  <p class="pe-good">Библиоте́ка <b>нахо́дится</b> в це́нтре — «joylashgan»</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>-ся</b> yoki <b>-сь</b>? &nbsp; <b>Я гото́влю___ к экза́мену.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>-сь</strong>: <em>гото́влю<b>сь</b></em>.
    Unlidan keyin har doim <b>-сь</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Qaysi maʼno? &nbsp; <b>Они́ ссо́рятся ка́ждый день.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>2-maʼno — bir-biriga</strong>.
    Urushish uchun kamida ikki kishi kerak. Oʻzbekchada bu
    <em>-ish-</em>: <em>urushmoq</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>учи́ть</b> yoki <b>учи́ться</b>? &nbsp; <b>Моя́ сестра́ ___ в
     университе́те.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>у́чится</strong>. <em>Учи́ть</em> —
    «oʻrgatmoq» yoki «yodlamoq» va u obyekt talab qiladi.
    «Universitetda oʻqimoq» — <b>учи́ться</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nima uchun bu gap notoʻgʻri? &nbsp; <b>Он одева́ется сы́на.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><em>Сы́на</em> — tushum kelishigi, lekin
    <b>-ся feʼli obyekt olmaydi</b>. Toʻgʻrisi: <b>Он одева́ет
    сы́на</b> (oʻgʻlini kiydiryapti) yoki <b>Он одева́ется</b>
    (kiyinyapti).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu ikki gapning farqi nima?<br>
     <b>Он нашёл ключи́. · Ключи́ нахо́дятся в су́мке.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — «u kalitlarni <b>topdi</b>»
    (harakat). Ikkinchisi — «kalitlar sumkada <b>turibdi</b>»
    (joylashuv). Bu 6-maʼno: -ся bilan feʼl butunlay boshqa
    maʼno oldi.</p></div>
  </details>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-63: Который — rus tilining «-gan» sifatdosh gapi",
        "category": "russian",
        "order": 63,
        "summary": (
            "Oʻzbekcha «yonimda yashaydigan odam» — sifatdosh otdan oldin. "
            "Ruscha «челове́к, кото́рый живёт ря́дом» — ergash gap otdan keyin."
        ),
        "stories": ["Челове́к, кото́рый чини́л всё"],
        "content": """
<h2>PR-63: Который — rus tilining «-gan» sifatdosh gapi</h2>

<p>Shu darsdan boshlab siz <b>uzun gap</b> qura boshlaysiz. <em>Который</em>
rus tilidagi eng koʻp ishlatiladigan bogʻlovchilardan biri, va u
oʻzbekchadagi <em>-gan / -yotgan / -adigan</em> sifatdoshining oʻrnini
bosadi. Faqat bitta katta farq bilan — <b>joyi teskari</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Который</b> ning jinsi va soni qayerdan kelishini bilasiz</li>
    <li>Uning <b>kelishigi</b> qayerdan kelishini bilasiz — bu asosiy qism</li>
    <li>Predlog bilan qanday yozilishini oʻrganasiz</li>
    <li>Vergulni har doim toʻgʻri qoʻyasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki til</span>
  <span class="pe-chip pe-chip--s">yonimda yashaydigan <b>odam</b></span>
  <span class="pe-op">↔</span>
  <span class="pe-chip pe-chip--v"><b>челове́к</b>, кото́рый живёт ря́дом</span>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha — eng muhim farq</span>
Oʻzbekchada aniqlovchi gap <b>otdan oldin</b> turadi va alohida soʻz
kerak emas:<br>
<em><b>Men oʻqiyotgan</b> kitob qiziq.</em><br><br>
Ruschada esa u <b>otdan keyin</b> turadi va <b>кото́рый</b> soʻzi
majburiy:<br>
<em>Кни́га, <b>кото́рую я чита́ю</b>, интере́сная.</em><br><br>
Yaʼni oʻzbek oʻquvchisining eng tabiiy xatosi — sifatdoshni oldinga
qoʻyish: <em>«Кото́рую я чита́ю кни́га»</em>. Bunday gap ruschada
yoʻq. <b>Avval ot, keyin vergul, keyin кото́рый.</b></div>

<h3>1. Jins va son — otdan</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ot</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td class="pr-uz">erkak</td><td class="pr-res">кото́рый</td>
      <td class="pr-end">челове́к, <b>кото́рый</b> живёт ря́дом</td></tr>
  <tr><td class="pr-uz">ayol</td><td class="pr-res">кото́рая</td>
      <td class="pr-end">де́вушка, <b>кото́рая</b> поёт</td></tr>
  <tr><td class="pr-uz">oʻrta</td><td class="pr-res">кото́рое</td>
      <td class="pr-end">окно́, <b>кото́рое</b> откры́то</td></tr>
  <tr><td class="pr-uz">koʻplik</td><td class="pr-res">кото́рые</td>
      <td class="pr-end">лю́ди, <b>кото́рые</b> ждут</td></tr>
</table></div>

<h3>2. Kelishigi — oʻz gapidan</h3>

<p>Mana darsning yuragi. <b>Который</b> ikki gapga tegishli, va u
ikkalasidan boshqa-boshqa narsa oladi:</p>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki manba</span>
  <span class="pe-chip pe-chip--s">jins + son</span>
  <span class="pe-op">←</span>
  <span class="pe-chip pe-chip--o">oldingi ot</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">kelishik</span>
  <span class="pe-op">←</span>
  <span class="pe-chip pe-chip--v">oʻz gapidagi vazifasi</span>
</div>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Misol</th><th>Nega</th></tr>
  <tr><td class="pr-res">Имени́тельный</td>
      <td class="pr-end">кни́га, <b>кото́рая</b> лежи́т на столе́</td>
      <td class="pr-uz">u oʻz gapida <b>ega</b></td></tr>
  <tr><td class="pr-res">Роди́тельный</td>
      <td class="pr-end">друг, у <b>кото́рого</b> есть маши́на</td>
      <td class="pr-uz">«у» predlogi</td></tr>
  <tr><td class="pr-res">Да́тельный</td>
      <td class="pr-end">друг, <b>кото́рому</b> я написа́л</td>
      <td class="pr-uz">«kimga yozdim?»</td></tr>
  <tr><td class="pr-res">Вини́тельный</td>
      <td class="pr-end">кни́га, <b>кото́рую</b> я чита́ю</td>
      <td class="pr-uz">«nimani oʻqiyapman?»</td></tr>
  <tr><td class="pr-res">Твори́тельный</td>
      <td class="pr-end">учи́тель, <b>кото́рым</b> все горди́лись</td>
      <td class="pr-uz">«kim bilan faxrlandilar?»</td></tr>
  <tr><td class="pr-res">Предло́жный</td>
      <td class="pr-end">дом, в <b>кото́ром</b> мы жи́ли</td>
      <td class="pr-uz">«в» predlogi</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Tekshirishning oson yoʻli</span>
Ergash gapni alohida ajratib, <em>кото́рый</em> oʻrniga otning oʻzini
qoʻying:<br><br>
<em>кни́га, кото́рую я чита́ю</em> → «я чита́ю <b>кни́гу</b>» —
Вини́тельный. Demak <b>кото́рую</b>.<br>
<em>дом, в кото́ром мы жи́ли</em> → «мы жи́ли <b>в до́ме</b>» —
Предло́жный. Demak <b>в кото́ром</b>.<br><br>
Bu usul har doim ishlaydi.</div>

<h3>3. Predlog кото́рый dan oldin turadi</h3>

<p>Rus tilida predlog hech qachon ergash gap oxirida qolmaydi — u
<b>кото́рый bilan birga</b> koʻchadi:</p>

<div class="pe-ex">
  <p class="pe-ex__t">Predlog + кото́рый</p>
  <p><em>го́род, <b>в кото́ром</b> я роди́лся</em> — men tugʻilgan shahar<br>
     <em>учи́тель, <b>о кото́ром</b> я говори́л</em> — men aytgan oʻqituvchi<br>
     <em>сосе́д, <b>с кото́рым</b> мы дружи́м</em> — biz doʻstlashgan qoʻshni<br>
     <em>по́лка, <b>на кото́рой</b> лежа́т кни́ги</em> — kitoblar turgan javon</p>
  <p class="pe-ex__n">Diqqat: vergul <b>predlogdan oldin</b> qoʻyiladi,
     кото́рый dan oldin emas.</p>
</div>

<h3>4. Yana ikkita foydali qurilish</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Сли́шком … что́бы — «juda … , shuning uchun boʻlmaydi»</p>
  <p><em>Он <b>сли́шком</b> уста́л, <b>что́бы</b> идти́ в кино́.</em><br>
     U kinoga borish uchun juda charchagan.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">Не ду́маю, что… — inkor bosh gapda qoladi</p>
  <p><em><b>Не ду́маю</b>, что он придёт.</em><br>
     Menimcha, u kelmaydi.</p>
  <p class="pe-ex__n">Rus tilida inkor birinchi feʼlga qoʻyiladi, oʻzbekchada
     esa ikkinchisiga — tarjima qilganda «yoʻq» boshqa joyga koʻchadi.</p>
</div>

<h3>5. Vergul</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Который dan oldin har doim vergul.</b> Istisnosiz. Agar ergash gap
gapning oʻrtasida boʻlsa, <b>ikki tomondan</b> ajratiladi:<br><br>
<em>Кни́га<b>,</b> кото́рую я чита́ю<b>,</b> о́чень интере́сная.</em><br><br>
Oʻzbekchada vergul kerak emas (<em>men oʻqiyotgan kitob</em>) — shuning
uchun buni alohida eslab qoling.</div>

<h3>5. Который sifat kabi tuslanadi</h3>

<p>Uni alohida yodlash shart emas: <em>кото́рый</em> aynan
<em>но́вый</em> kabi oʻzgaradi (PR-42).</p>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>erkak / oʻrta</th><th>ayol</th><th>koʻplik</th></tr>
  <tr><td class="pr-uz">Им.</td><td class="pr-res">кото́рый / кото́рое</td>
      <td class="pr-end">кото́рая</td><td class="pr-end">кото́рые</td></tr>
  <tr><td class="pr-uz">Род.</td><td class="pr-res">кото́рого</td>
      <td class="pr-end">кото́рой</td><td class="pr-end">кото́рых</td></tr>
  <tr><td class="pr-uz">Дат.</td><td class="pr-res">кото́рому</td>
      <td class="pr-end">кото́рой</td><td class="pr-end">кото́рым</td></tr>
  <tr><td class="pr-uz">Вин.</td><td class="pr-res">кото́рый / кото́рого</td>
      <td class="pr-end">кото́рую</td><td class="pr-end">кото́рые / кото́рых</td></tr>
  <tr><td class="pr-uz">Твор.</td><td class="pr-res">кото́рым</td>
      <td class="pr-end">кото́рой</td><td class="pr-end">кото́рыми</td></tr>
  <tr><td class="pr-uz">Предл.</td><td class="pr-res">о кото́ром</td>
      <td class="pr-end">о кото́рой</td><td class="pr-end">о кото́рых</td></tr>
</table></div>

<p>Tushum kelishigida jonli/jonsiz farqi ishlaydi (PR-33):
<em>стол, кото́рый я купи́л</em> — lekin <em>друг, кото́рого я
встре́тил</em>.</p>

<h3>6. Kim va nima haqida</h3>

<p><em>Который</em> ham odamga, ham narsaga ishlatiladi — oʻzbekcha
<em>-gan</em> kabi. Yaʼni ingliz tilidagi «who / which» boʻlinishi
ruschada <b>yoʻq</b>:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Odam</th><th>Narsa</th></tr>
  <tr><td class="pr-res">челове́к, кото́рый рабо́тает</td>
      <td class="pr-end">маши́на, кото́рая рабо́тает</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Кото́рую я чита́ю кни́га интере́сная.</s></p>
  <p class="pe-good">Кни́га, <b>кото́рую я чита́ю</b>, интере́сная — avval ot</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Дом, кото́рый мы жи́ли.</s></p>
  <p class="pe-good">Дом, <b>в кото́ром</b> мы жи́ли — predlog kerak</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кни́га кото́рую я чита́ю…</s></p>
  <p class="pe-good">Кни́га<b>,</b> кото́рую я чита́ю… — vergul majburiy</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Друг, кото́рый я написа́л.</s></p>
  <p class="pe-good">Друг, <b>кото́рому</b> я написа́л — «kimga?», Да́тельный</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>Э́то кни́га, ___ я купи́л вчера́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>кото́рую</strong>. «Я купи́л
    <b>кни́гу</b>» — Вини́тельный, ayol jinsi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>Э́то дом, ___ живёт моя́ ба́бушка.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в кото́ром</strong>. «Ба́бушка
    живёт <b>в до́ме</b>» — Предло́жный, predlog bilan birga.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapni bittaga birlashtiring.<br>
     <b>Я зна́ю э́того челове́ка. Он рабо́тает в шко́ле.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я зна́ю челове́ка, кото́рый
    рабо́тает в шко́ле.</strong> Ikkinchi gapda <em>он</em> ega edi —
    demak <b>кото́рый</b>, Имени́тельный.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>Э́то друг, ___ я давно́ не ви́дел.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>кото́рого</strong>. «Я не ви́дел
    <b>дру́га</b>» — jonli otda Вини́тельный = Роди́тельный
    (PR-33).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni oʻzbekchaga oʻgiring.<br>
     <b>Сосе́д, с кото́рым мы дружи́м, уе́хал.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Biz doʻstlashgan qoʻshni ketib
    qoldi.</strong> Eʼtibor bering: oʻzbekchada aniqlovchi <b>oldinda</b>,
    ruschada <b>keyinda</b> — shuning uchun oʻgirganda gapni
    agʻdarish kerak.</p></div>
  </details>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-64: Что va чтобы — bir soʻzga oʻxshaydi, ikki xil gap quradi",
        "category": "russian",
        "order": 64,
        "summary": (
            "Что — fakt: «bilaman, u keladi». Чтобы — istak yoki maqsad: "
            "«uning kelishini xohlayman». Va чтобы dan keyin oʻtgan zamon."
        ),
        "stories": ["Что́бы тебя́ по́няли"],
        "content": """
<h2>PR-64: Что va чтобы — bir soʻzga oʻxshaydi, ikki xil gap quradi</h2>

<p>Ikkala soʻz ham «-ki» kabi ergash gap boshlaydi, ikkalasi ham bir xil
oʻzakdan. Lekin ular <b>butunlay boshqa</b> ikki narsa uchun: biri
<b>faktni</b> aytadi, ikkinchisi <b>istak yoki maqsadni</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Fakt bilan istakni ajratasiz</li>
    <li><b>Чтобы + oʻtgan zamon</b> qoidasini oʻrganasiz</li>
    <li>Ega bir xil boʻlganda infinitiv qoʻyasiz</li>
    <li>Qaysi feʼl qaysi bogʻlovchini talab qilishini bilasiz</li>
  </ul>
</div>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">ЧТО — fakt</p>
    <p><em>Я зна́ю, <b>что</b> он придёт.</em><br>
       Bilaman<b>ki</b>, u keladi.</p>
    <p>Bu — axborot. Sodir boʻlgan yoki boʻladigan narsa.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ЧТОБЫ — istak / maqsad</p>
    <p><em>Я хочу́, <b>что́бы</b> он пришёл.</em><br>
       Uning kelishini xohlayman.</p>
    <p>Bu — hali sodir boʻlmagan narsa. Kimdir uni xohlayapti.</p>
  </div>
</div>

<h3>1. Чтобы ning ikki qurilishi</h3>

<div class="pe-formula">
  <span class="pe-formula__label">Ega boshqa</span>
  <span class="pe-chip pe-chip--s">что́бы</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">oʻtgan zamon</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ega bir xil</span>
  <span class="pe-chip pe-chip--s">что́бы</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">infinitiv</span>
</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ega</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-uz">boshqa</td>
      <td class="pr-res">Я хочу́, что́бы ты <b>пришёл</b>.</td>
      <td class="pr-end">Kelishingni xohlayman.</td></tr>
  <tr><td class="pr-uz">boshqa</td>
      <td class="pr-res">Ма́ма проси́ла, что́бы мы <b>помы́ли</b> посу́ду.</td>
      <td class="pr-end">Oyim idishlarni yuvishimizni soʻradi.</td></tr>
  <tr><td class="pr-uz">bir xil</td>
      <td class="pr-res">Я пришёл, что́бы <b>поговори́ть</b>.</td>
      <td class="pr-end">Gaplashgani keldim.</td></tr>
  <tr><td class="pr-uz">bir xil</td>
      <td class="pr-res">Он у́чится, что́бы <b>стать</b> врачо́м.</td>
      <td class="pr-end">Shifokor boʻlish uchun oʻqiyapti.</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Diqqat</span>
<b>Чтобы dan keyingi oʻtgan zamon — oʻtmish emas!</b><br><br>
<em>Я хочу́, что́бы ты <b>пришёл</b> за́втра.</em> — Ertaga kelishingni
xohlayman.<br><br>
Bu shakl PR-60 dagi <em>бы</em> bilan bir oila: <em>что́бы</em> =
<em>что</em> + <em>бы</em>, va <em>бы</em> har doim oʻtgan zamon
talab qiladi. Yaʼni bu <b>zamon emas, shakl</b>.</div>

<h3>2. Qaysi feʼl nimani talab qiladi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>ЧТО oladi</th><th>ЧТОБЫ oladi</th></tr>
  <tr><td class="pr-res">знать — bilmoq</td><td class="pr-end">хоте́ть — xohlamoq</td></tr>
  <tr><td class="pr-res">ду́мать — oʻylamoq</td><td class="pr-end">проси́ть — soʻramoq</td></tr>
  <tr><td class="pr-res">говори́ть — aytmoq</td><td class="pr-end">тре́бовать — talab qilmoq</td></tr>
  <tr><td class="pr-res">ви́деть — koʻrmoq</td><td class="pr-end">ну́жно / на́до — kerak</td></tr>
  <tr><td class="pr-res">слы́шать — eshitmoq</td><td class="pr-end">сове́товать — maslahat bermoq</td></tr>
  <tr><td class="pr-res">чу́вствовать — sezmoq</td><td class="pr-end">боя́ться — qoʻrqmoq</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Bitta savol yetarli</span>
Oʻzingizga soʻrang: <b>«bu allaqachon fakt, yoki kimdir shuni
xohlayaptimi?»</b><br><br>
Fakt → <b>что</b>. Istak, iltimos, maqsad, talab → <b>что́бы</b>.<br><br>
<em>Я слы́шал, <b>что</b> он прие́хал.</em> — eshitdim, keldi (fakt)<br>
<em>Я хочу́, <b>что́бы</b> он прие́хал.</em> — kelishini xohlayman (istak)</div>

<h3>3. Что́бы «uchun» maʼnosida</h3>

<p>Ega bir xil boʻlsa, <em>что́бы</em> oʻzbekchadagi <b>«-sh uchun»</b>
ga toʻgʻri keladi va infinitiv oladi:</p>

<div class="pe-ex">
  <p class="pe-ex__t">Maqsad</p>
  <p><em>Что́бы <b>вы́учить</b> язы́к, ну́жно говори́ть ка́ждый день.</em><br>
     Tilni oʻrganish uchun har kuni gapirish kerak.</p>
  <p><em>Я встал ра́но, что́бы не <b>опозда́ть</b>.</em><br>
     Kechikmaslik uchun erta turdim.</p>
  <p class="pe-ex__n">Bunday gap <em>что́бы</em> bilan boshlanishi ham
     mumkin — u holda vergul oʻrtada.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada bu ikki maʼno <b>butunlay boshqa qurilish</b> bilan
beriladi, shuning uchun ularni ajratish siz uchun qiyin emas:<br><br>
Fakt: <em>Bilaman<b>ki</b>, u keladi</em> yoki <em>uning
kel<b>ishini</b> bilaman</em> &nbsp;→&nbsp; <b>что</b><br>
Istak: <em>uning kel<b>ishini</b> xohlayman</em> &nbsp;→&nbsp;
<b>что́бы</b> + oʻtgan zamon<br>
Maqsad: <em>gaplash<b>ish uchun</b> keldim</em> &nbsp;→&nbsp;
<b>что́бы</b> + infinitiv<br><br>
Qiyinligi bitta: oʻzbekcha <em>-shini</em> ikkala holatda ham
ishlatiladi (<em>kelishini bilaman</em> / <em>kelishini
xohlayman</em>), ruschada esa bu ikki gap boshqa-boshqa quriladi.
Shuning uchun tarjima qilganda feʼlga qarang: <b>bilmoq</b> — что,
<b>xohlamoq</b> — что́бы.</div>

<h3>4. Vergul</h3>

<p>Ikkalasidan oldin ham <b>vergul majburiy</b>:
<em>Я зна́ю<b>,</b> что…</em> · <em>Я хочу́<b>,</b> что́бы…</em><br>
Agar <em>что́бы</em> gap boshida tursa, vergul ergash gap
tugagandan keyin qoʻyiladi: <em>Что́бы не опозда́ть<b>,</b> я встал
ра́но.</em></p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я хочу́, что́бы ты придёшь.</s></p>
  <p class="pe-good">Я хочу́, что́бы ты <b>пришёл</b> — что́бы dan keyin oʻtgan zamon</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я зна́ю, что́бы он рабо́тает здесь.</s></p>
  <p class="pe-good">Я зна́ю, <b>что</b> он рабо́тает здесь — bu fakt</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я пришёл, что́бы я поговори́л.</s></p>
  <p class="pe-good">Я пришёл, что́бы <b>поговори́ть</b> — ega bir xil, infinitiv</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ма́ма проси́ла что мы помы́ли посу́ду.</s></p>
  <p class="pe-good">Ма́ма проси́ла, <b>что́бы</b> мы помы́ли посу́ду — iltimos</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>что</b> yoki <b>что́бы</b>? &nbsp; <b>Я ду́маю, ___ э́то
     хоро́шая иде́я.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>что</strong>. <em>Ду́мать</em> —
    fikr bildirish, yaʼni fakt. Istak emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>Я хочу́, что́бы ты ___ мне.</b> (помо́чь)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>помо́г</strong>. Ega boshqa
    (<em>я</em> ↔ <em>ты</em>), demak <b>oʻtgan zamon</b>. Bu oʻtmish
    haqida emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>Он прие́хал в Москву́, что́бы ___.</b> (учи́ться)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>учи́ться</strong> — infinitiv.
    Ikkala qismda ham ega <em>он</em>, demak oʻtgan zamon
    emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu ikki gapning farqi nima?<br>
     <b>Я сказа́л, что он пришёл. · Я сказа́л, что́бы он пришёл.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — <b>xabar</b>: «u kelganini
    aytdim». Ikkinchisi — <b>buyruq yoki iltimos</b>: «kelsin dedim».
    <em>Сказа́ть</em> ikkala bogʻlovchini ham oladi, va maʼno
    butunlay oʻzgaradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Kechikmaslik uchun erta turdim.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я встал ра́но, что́бы не
    опозда́ть.</strong> Oʻzbekcha «-sh uchun» = <b>что́бы</b> +
    infinitiv, chunki ikkala qismda ham ega bitta.</p></div>
  </details>
</div>
""",
    },
]
