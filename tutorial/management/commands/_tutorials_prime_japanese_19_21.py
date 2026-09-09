# -*- coding: utf-8 -*-
"""Prime Japanese — Block B, darslar 19–21.

⚠️ PJ-20 — kursning burilish nuqtasi: birinchi FEʼL. Shu darsdan boshlab
oʻqish matnlarida «hikoya ramkasi» istisnosi kerak emas, chunki oʻquvchi
endi feʼlni oʻzi biladi.

Uchta boʻlak: dars + mashq (20 savol) + oʻqish matni (audio bilan).

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_19_21.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Japanese",
    "category": "japanese",
    "description": (
        "Yapon tili noldan ishonchli N4 gacha — 100 ta dars. Hiragana, katakana, kanji, "
        "grammatika qoliplari, oʻzbekcha tushuntirish va oʻzingiz tekshiradigan mashqlar."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-19: も, と, や — «ham», «va», «va boshqalar»",
        "category": "japanese",
        "order": 19,
        "summary": (
            "Uchta kichik qoʻshimcha: も «ham» deydi va は/が ni siqib chiqaradi, "
            "と toʻliq roʻyxat tuzadi, や esa «va shunga oʻxshashlar» deydi."
        ),
        "stories": ["わたしも がくせいです"],
        "content": """
<h2>PJ-19: も, と, や — «ham», «va», «va boshqalar»</h2>

<p>Uchta kichkina qoʻshimcha, uchtasi ham bir boʻgʻin. Lekin ular gapga
katta narsa qoʻshadi: <b>も</b> bilan «men ham» deysiz, <b>と</b> bilan
roʻyxat tuzasiz, <b>や</b> bilan esa roʻyxatni ochiq qoldirasiz.</p>

<p>Bitta muhim nozik joy bor va uni darrov aytaman: <b>も</b> は yoki が ga
<em>qoʻshilmaydi</em> — u ularni <b>siqib chiqaradi</b>. Bu boshlovchilar eng
koʻp adashadigan nuqta.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>も bilan «ham» deysiz va uni は/が oʻrniga qoʻyasiz</li>
    <li>と bilan toʻliq roʻyxat tuzasiz</li>
    <li>や bilan «va shunga oʻxshashlar» deysiz</li>
    <li>と ning ikkinchi maʼnosini — «bilan» ni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uchta vazifa</span>
  <span class="pe-chip pe-chip--s">も = ham</span>
  <span class="pe-chip pe-chip--v">と = va (toʻliq)</span>
  <span class="pe-chip pe-chip--o">や = va (ochiq)</span>
</div>

<h3>1. も — «ham», va u nimani siqib chiqaradi</h3>

<div class="pe-ex">
  <p class="pe-ex__ja">アフソナさんは<ruby>学生<rt>がくせい</rt></ruby>です。<ruby>私<rt>わたし</rt></ruby>も<ruby>学生<rt>がくせい</rt></ruby>です。</p>
  <p class="pe-ex__rom">afusona-san wa gakusē desu. watashi mo gakusē desu</p>
  <p class="pe-ex__uz">Afsona talaba. Men ham talabaman.</p>
  <p class="pe-ex__why">Ikkinchi gapda <b>は yoʻq</b> — も uning oʻrnini egalladi. «<ruby>私<rt>わたし</rt></ruby>はも» yoki «<ruby>私<rt>わたし</rt></ruby>もは» degan birikma mavjud emas.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Qoida:</b> <b>も</b> — <b>は</b> va <b>が</b> ning <em>oʻrniga</em>
  qoʻyiladi, ular bilan birga emas. Boshqa qoʻshimchalar bilan esa
  birga ishlaydi: <ruby>学校<rt>がっこう</rt></ruby>に<b>も</b> («maktabga ham»),
  <ruby>友達<rt>ともだち</rt></ruby>と<b>も</b> («doʻst bilan ham»).</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">✗ NOTOʻGʻRI</p>
    <p class="pj-big">は + も</p>
    <p><ruby>私<rt>わたし</rt></ruby>はも<ruby>学生<rt>がくせい</rt></ruby>です<br>
    Bunday shakl yoʻq.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">✓ TOʻGʻRI</p>
    <p class="pj-big">も</p>
    <p><ruby>私<rt>わたし</rt></ruby>も<ruby>学生<rt>がくせい</rt></ruby>です<br>
    は tushib qoladi.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu muammo yoʻq</b> — biz «men <em>ham</em>» deymiz va hech
  narsa tushmaydi, chunki oʻzbekcha ega qoʻshimchasiz turadi. Yaponchada esa
  ega doim qoʻshimcha oladi, shuning uchun も kelganda joy boʻshatish kerak.
  Buni shunday tasavvur qiling: gapda <b>bitta</b> joy bor, va は, が, も
  oʻsha bitta joy uchun raqobat qiladi.</p>
</div>

<h3>2. も inkor bilan — «ham …emas»</h3>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>も<ruby>先生<rt>せんせい</rt></ruby>ではありません。</p>
  <p class="pe-ex__rom">watashi mo sensē dewa arimasen</p>
  <p class="pe-ex__uz">Men ham oʻqituvchi emasman.</p>
  <p class="pe-ex__why">も inkor gapda ham xuddi shunday ishlaydi: «boshqasi ham emas, men ham emas».</p>
</div>

<h3>3. と — toʻliq roʻyxat</h3>

<p><b>と</b> otlarni bogʻlaydi va roʻyxat <em>toʻliq</em> ekanini bildiradi:
sanalganlardan boshqa hech narsa yoʻq.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>本<rt>ほん</rt></ruby></span>
  <span class="pj-joshi__p">と<small>VA</small></span>
  <span class="pj-joshi__n"><ruby>鞄<rt>かばん</rt></ruby></span>
  <span class="pj-joshi__p">が<small>EGA</small></span>
  <span class="pj-joshi__v">あります</span>
  <span class="pj-joshi__uz">Kitob va sumka bor — faqat shu ikkitasi.</span>
</div>

<div class="pe-call pe-warn">
  <p><b>と faqat OTLARNI bogʻlaydi.</b> Oʻzbekchada «va» gaplarni ham bogʻlaydi
  («keldi <em>va</em> ketdi»), yaponchada esa と buni qila olmaydi. Gaplarni
  bogʻlash boshqa vosita bilan qilinadi va uni PJ-33 da koʻramiz. Hozircha:
  <b>と — ot bilan ot orasida</b>.</p>
</div>

<h3>4. や — ochiq roʻyxat</h3>

<p><b>や</b> ham «va» degani, lekin u <em>«va shunga oʻxshash boshqalar»</em>
degan maʼnoni ham qoʻshadi. Roʻyxat namuna, toʻliq emas.</p>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">と — TOʻLIQ</p>
    <p class="pj-pair__form"><ruby>本<rt>ほん</rt></ruby>と<ruby>鞄<rt>かばん</rt></ruby></p>
    <p>Kitob va sumka. <b>Faqat shu ikkitasi</b>, boshqa hech narsa yoʻq.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">や — OCHIQ</p>
    <p class="pj-pair__form"><ruby>本<rt>ほん</rt></ruby>や<ruby>鞄<rt>かばん</rt></ruby></p>
    <p>Kitob, sumka va boshqalar. <b>Namuna keltirildi</b>, roʻyxat davom
    etishi mumkin.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bunga aniq muqobil bor:</b> «kitob <em>va</em> sumka» —
  と, «kitob-u sumka <em>kabilar</em>» yoki «kitob, sumka <em>va hokazo</em>» —
  や. Yaponlar bu farqni juda sezgir ishlatadi: doʻkonda sotuvchidan
  «<ruby>本<rt>ほん</rt></ruby>や<ruby>鞄<rt>かばん</rt></ruby>があります» eshitsangiz,
  u yerda boshqa narsalar ham borligini bilasiz.</p>
</div>

<h3>5. Roʻyxatdagi oxirgi と</h3>

<p>Ingliz tilida roʻyxatda «va» faqat oxirgi ikki soʻz orasida turadi. Yapon
tilida esa <b>と har bir juftlik orasida takrorlanadi</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>本<rt>ほん</rt></ruby>と<ruby>鞄<rt>かばん</rt></ruby>と<ruby>時計<rt>とけい</rt></ruby>があります。</p>
  <p class="pe-ex__rom">hon to kaban to tokē ga arimasu</p>
  <p class="pe-ex__uz">Kitob, sumka va soat bor.</p>
  <p class="pe-ex__why">Uchta narsa — ikkita と. Oʻzbekchada «kitob, sumka va soat» deymiz, yaponchada esa har bir bogʻlanish belgilanadi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Roʻyxat oxirida と qolmaydi.</b> «<ruby>本<rt>ほん</rt></ruby>と<ruby>鞄<rt>かばん</rt></ruby>と» deb toʻxtatib boʻlmaydi —
  と ikki tomonni bogʻlaydi, shuning uchun undan keyin doim nimadir kelishi
  kerak. や da esa boshqacha: u roʻyxat oxirida ham qolishi mumkin, chunki
  «va boshqalar» degan maʼno allaqachon ichida.</p>
</div>

<h3>6. と ning ikkinchi maʼnosi — «bilan»</h3>

<p>Xuddi shu <b>と</b> yana bir ishni bajaradi: odam bilan birga nimadir
qilishni bildiradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>友達<rt>ともだち</rt></ruby>と<ruby>学校<rt>がっこう</rt></ruby>にいます。</p>
  <p class="pe-ex__rom">tomodachi to gakkō ni imasu</p>
  <p class="pe-ex__uz">Doʻstim bilan maktabdaman.</p>
  <p class="pe-ex__why">Bu yerda と «va» emas, <b>«bilan»</b>. Farqni kontekst hal qiladi: と dan keyin roʻyxat davom etsa — «va», feʼl kelsa — «bilan».</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Yolgʻiz boʻlsangiz</b> — <ruby>一人<rt>ひとり</rt></ruby>で.
  Bu ibora juda koʻp uchraydi va uni hozirdan yodlab qoʻygan maʼqul:
  «<ruby>一人<rt>ひとり</rt></ruby>で<ruby>本<rt>ほん</rt></ruby>があります» emas,
  albatta — u feʼl bilan ishlaydi, va feʼlni keyingi darsda oʻrganamiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>はも<ruby>学生<rt>がくせい</rt></ruby>です</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby><b>も</b><ruby>学生<rt>がくせい</rt></ruby>です — も は ni siqib chiqaradi, ular birga turmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>がも<ruby>行<rt>い</rt></ruby>きます</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby><b>も</b>… — が ni ham siqib chiqaradi. Lekin に, と kabi qoʻshimchalar bilan も birga turadi: <ruby>学校<rt>がっこう</rt></ruby>にも.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Roʻyxat toʻliq boʻlsa ham や ishlatish</p>
  <p class="pe-fix__good">✓ Toʻliq roʻyxat — <b>と</b>. や «va boshqalar» degan maʼno qoʻshadi va bu koʻpincha kerak boʻlmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Men ham talabaman» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><ruby>私<rt>わたし</rt></ruby>も<ruby>学生<rt>がくせい</rt></ruby>です。 — は <b>tushib qoladi</b>, chunki も uning oʻrnini egallaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. も qaysi qoʻshimchalarni siqib chiqaradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>は va が</b>. Boshqalar bilan (に, と…) birga turadi: <ruby>学校<rt>がっこう</rt></ruby>にも, <ruby>友達<rt>ともだち</rt></ruby>とも.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. と va や orasidagi farq nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>と</b> — roʻyxat toʻliq, faqat sanalganlar. <b>や</b> — roʻyxat ochiq, «va shunga oʻxshash boshqalar».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. と gaplarni bogʻlay oladimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> と faqat <b>otlarni</b> bogʻlaydi. Gaplarni bogʻlash boshqa vosita bilan qilinadi (PJ-33).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>友達<rt>ともだち</rt></ruby>と — bu «doʻst va» mi, «doʻst bilan» mi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Kontekst hal qiladi.</b> と dan keyin yana ot kelsa — «va». Feʼl yoki kesim kelsa — «bilan».</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>も</b> — ham (は/が ni siqib chiqaradi)</li>
  <li><b>と</b> — va (toʻliq roʻyxat); bilan</li>
  <li><b>や</b> — va boshqalar (ochiq roʻyxat)</li>
  <li><b><ruby>一人<rt>ひとり</rt></ruby>で</b> — yolgʻiz</li>
  <li><b><ruby>犬<rt>いぬ</rt></ruby></b> — it</li>
  <li><b><ruby>学校<rt>がっこう</rt></ruby></b> — maktab</li>
  <li><b><ruby>友達<rt>ともだち</rt></ruby></b> — doʻst</li>
  <li><b><ruby>家族<rt>かぞく</rt></ruby></b> — oila</li>
  <li><b><ruby>兄弟<rt>きょうだい</rt></ruby></b> — aka-uka, opa-singil</li>
  <li><b><ruby>果物<rt>くだもの</rt></ruby></b> — meva</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>も</b> は va が ni <b>siqib chiqaradi</b>, boshqa qoʻshimchalar bilan esa birga turadi.</li>
    <li><b>と</b> — toʻliq roʻyxat, <b>や</b> — «va boshqalar».</li>
    <li><b>と</b> faqat <b>otlarni</b> bogʻlaydi, va u «bilan» maʼnosini ham beradi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-20: 動詞 + 〜ます / 〜ません — hozirgi-kelasi zamon",
        "category": "japanese",
        "order": 20,
        "summary": (
            "Kursning burilish nuqtasi: birinchi feʼl. ます shakli bilan har kungi "
            "ishlaringizni aytasiz — va yapon tilida kelasi zamon yoʻqligini bilib olasiz."
        ),
        "stories": ["まいにち にほんごを べんきょうします"],
        "content": """
<h2>PJ-20: <ruby>動詞<rt>どうし</rt></ruby> + 〜ます / 〜ません — hozirgi-kelasi zamon</h2>

<p>Yigirma dars davomida siz narsalarni <em>taʼrifladingiz</em>: bu nima, kim
qayerda, kimniki. Bugundan boshlab odamlar <b>ish qiladi</b>. Birinchi feʼl —
va u bilan birga butun til jonlanadi.</p>

<p>Yaxshi xabar ikkita, va ikkalasi ham katta. Birinchisi: <b>ます shakli
shaxsga qarab oʻzgarmaydi</b> — です kabi, bitta shakl hamma uchun. Ikkinchisi:
<b>yapon tilida alohida kelasi zamon yoʻq</b>. Bitta shakl «qilaman» ni ham,
«qilaman (ertaga)» ni ham bildiradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ます shakli bilan hozirgi va kelasi zamonni aytasiz</li>
    <li>ません bilan inkor qilasiz</li>
    <li>Birinchi oʻn feʼlni oʻrganasiz</li>
    <li>Vaqt soʻzlari bilan gap tuzasiz: <ruby>毎日<rt>まいにち</rt></ruby>, <ruby>今日<rt>きょう</rt></ruby>, <ruby>明日<rt>あした</rt></ruby></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta shakl, ikki zamon</span>
  <span class="pe-chip pe-chip--v">〜ます</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">hozir qilaman</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">keyin qilaman</span>
</div>

<h3>1. ます — muloyim feʼl shakli</h3>

<p>Yapon feʼllarining bir necha shakli bor. Biz eng foydalisidan boshlaymiz:
<b>ます</b> shakli. U <em>muloyim</em>, xavfsiz va deyarli har qanday vaziyatda
toʻgʻri keladi — notanish odam bilan ham, oʻqituvchi bilan ham.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n"><ruby>毎日<rt>まいにち</rt></ruby></span>
  <span class="pj-joshi__v"><ruby>働<rt>はたら</rt></ruby>きます</span>
  <span class="pj-joshi__uz">Men har kuni ishlayman. — feʼl OXIRIDA, oʻzbekcha kabi.</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu yerda yapon tili oʻzbekchadan ham sodda.</b> Oʻzbekchada feʼl
  shaxsga qarab oʻzgaradi: «ishlay<em>man</em>», «ishlay<em>san</em>»,
  «ishlay<em>di</em>» — uchta qoʻshimcha. Yaponchada esa
  <ruby>働<rt>はたら</rt></ruby>きます — <b>hamma shaxs uchun bitta</b>. Kim
  ishlayotganini gap boshidagi mavzu koʻrsatadi, feʼl esa qimirlamaydi.</p>
</div>

<h3>2. Kelasi zamon yoʻq</h3>

<p>Bu yangilik koʻpchilikni hayratga soladi: yapon tilida <b>hozirgi va kelasi
zamon uchun bitta shakl</b>. Farqni <em>vaqt soʻzi</em> koʻrsatadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yaponcha</th><th>Maʼnosi</th><th>Nima aniqlaydi</th></tr>
  <tr><td><ruby>毎日<rt>まいにち</rt></ruby><ruby>働<rt>はたら</rt></ruby>きます</td>
      <td class="pj-uz">Har kuni ishlayman</td><td class="pj-uz">odat</td></tr>
  <tr><td><ruby>今日<rt>きょう</rt></ruby><ruby>働<rt>はたら</rt></ruby>きます</td>
      <td class="pj-uz">Bugun ishlayman</td><td class="pj-uz">hozirgi</td></tr>
  <tr><td><ruby>明日<rt>あした</rt></ruby><ruby>働<rt>はたら</rt></ruby>きます</td>
      <td class="pj-uz">Ertaga ishlayman</td><td class="pj-uz">kelasi</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Feʼl bir xil, vaqt soʻzi oʻzgardi.</b> Shuning uchun yapon tilida
  «zamon» oʻrniga <b>«oʻtgan / oʻtmagan»</b> deb oʻylash toʻgʻriroq: ます
  shakli — <em>hali boʻlmagan yoki hozir boʻlayotgan</em> hamma narsa.
  Oʻtgan zamonni PJ-23 da koʻramiz.</p>
</div>

<h3>3. Birinchi feʼllaringiz</h3>

<p>Hozircha feʼllarni <b>ます shaklida</b>, tayyor soʻz sifatida yodlang.
Ularning ichki tuzilishi va lugʻat shakli PJ-27 va PJ-28 da ochiladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>行<rt>い</rt></ruby>きます</td><td class="pj-res">ikimasu</td><td class="pj-uz">boraman</td></tr>
  <tr><td><ruby>来<rt>き</rt></ruby>ます</td><td class="pj-res">kimasu</td><td class="pj-uz">kelaman</td></tr>
  <tr><td><ruby>帰<rt>かえ</rt></ruby>ります</td><td class="pj-res">kaerimasu</td><td class="pj-uz">qaytaman</td></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べます</td><td class="pj-res">tabemasu</td><td class="pj-uz">yeyman</td></tr>
  <tr><td><ruby>飲<rt>の</rt></ruby>みます</td><td class="pj-res">nomimasu</td><td class="pj-uz">ichaman</td></tr>
  <tr><td><ruby>見<rt>み</rt></ruby>ます</td><td class="pj-res">mimasu</td><td class="pj-uz">koʻraman</td></tr>
  <tr><td><ruby>読<rt>よ</rt></ruby>みます</td><td class="pj-res">yomimasu</td><td class="pj-uz">oʻqiyman</td></tr>
  <tr><td><ruby>書<rt>か</rt></ruby>きます</td><td class="pj-res">kakimasu</td><td class="pj-uz">yozaman</td></tr>
  <tr><td><ruby>起<rt>お</rt></ruby>きます</td><td class="pj-res">okimasu</td><td class="pj-uz">turaman (uygʻonaman)</td></tr>
  <tr><td><ruby>聞<rt>き</rt></ruby>きます</td><td class="pj-res">kikimasu</td><td class="pj-uz">eshitaman, tinglayman</td></tr>
  <tr><td>します</td><td class="pj-res">shimasu</td><td class="pj-uz">qilaman</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>します</b> — eng foydali feʼl. U koʻp otlar bilan birikib yangi feʼl
  yasaydi: <ruby>勉強<rt>べんきょう</rt></ruby>します (oʻqiyman),
  <ruby>電話<rt>でんわ</rt></ruby>します (telefon qilaman),
  <ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>します (xarid qilaman).
  Yaʼni bitta feʼl bilan oʻnlab yangi ish nomini aytasiz.</p>
</div>

<h3>4. Inkor: ません</h3>

<p>Inkor uchun <b>ます</b> ni <b>ません</b> ga almashtirasiz. Boshqa hech narsa
oʻzgarmaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Tasdiq</th><th>Inkor</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res"><ruby>行<rt>い</rt></ruby>きます</td>
      <td class="pj-end"><ruby>行<rt>い</rt></ruby>きません</td><td class="pj-uz">boraman / bormayman</td></tr>
  <tr><td class="pj-res"><ruby>食<rt>た</rt></ruby>べます</td>
      <td class="pj-end"><ruby>食<rt>た</rt></ruby>べません</td><td class="pj-uz">yeyman / yemayman</td></tr>
  <tr><td class="pj-res">します</td><td class="pj-end">しません</td><td class="pj-uz">qilaman / qilmayman</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>は<ruby>肉<rt>にく</rt></ruby>を<ruby>食<rt>た</rt></ruby>べません。</p>
  <p class="pe-ex__rom">watashi wa niku o tabemasen</p>
  <p class="pe-ex__uz">Men goʻsht yemayman.</p>
  <p class="pe-ex__why">Oʻrtadagi <b>を</b> — toʻldiruvchi qoʻshimchasi, oʻzbekchadagi <em>-ni</em>. Unga PJ-21 da butun dars bagʻishlanadi.</p>
</div>

<h3>5. Savol va javob</h3>

<p>Savol yasash — oʻsha eski usul: gap oxiriga <b>か</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>明日<rt>あした</rt></ruby><ruby>学校<rt>がっこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きますか。</p>
  <p class="pe-ex__rom">ashita gakkō ni ikimasu ka</p>
  <p class="pe-ex__uz">Ertaga maktabga borasizmi?</p>
  <p class="pe-ex__why">Javob: <b>はい、<ruby>行<rt>い</rt></ruby>きます</b> yoki <b>いいえ、<ruby>行<rt>い</rt></ruby>きません</b>. Yaponchada savolni feʼlni takrorlab javob berish juda tabiiy.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Diqqat: inkor savolga javob berishda ehtiyot boʻling.</b>
  «<ruby>行<rt>い</rt></ruby>きませんか» («bormaysizmi?») degan savolga
  <b>はい</b> desangiz, bu «ha, bormayman» degani — yaʼni siz savolning
  <em>mazmuni</em> bilan rozilashasiz, oʻzbekchadagi kabi emas. Bu farq
  boshlovchilarni koʻp chalgʻitadi, shuning uchun shubhalansangiz toʻliq
  javob bering: «はい、<ruby>行<rt>い</rt></ruby>きません».</p>
</div>

<h3>6. Vaqt soʻzlari</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>毎日<rt>まいにち</rt></ruby></td><td class="pj-res">mainichi</td><td class="pj-uz">har kuni</td></tr>
  <tr><td><ruby>今日<rt>きょう</rt></ruby></td><td class="pj-res">kyō</td><td class="pj-uz">bugun</td></tr>
  <tr><td><ruby>明日<rt>あした</rt></ruby></td><td class="pj-res">ashita</td><td class="pj-uz">ertaga</td></tr>
  <tr><td><ruby>毎朝<rt>まいあさ</rt></ruby></td><td class="pj-res">maiasa</td><td class="pj-uz">har ertalab</td></tr>
  <tr><td><ruby>今<rt>いま</rt></ruby></td><td class="pj-res">ima</td><td class="pj-uz">hozir</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Vaqt soʻzi odatda gap boshida turadi</b>, mavzudan keyin:
  «<ruby>私<rt>わたし</rt></ruby>は<ruby>毎日<rt>まいにち</rt></ruby>…». Lekin uni
  eng boshiga ham qoʻyish mumkin. Yapon gapida <b>faqat feʼlning oʻrni
  qatʼiy</b> — u doim oxirida. Qolgan boʻlaklar ancha erkin.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Kelasi zamon uchun alohida shakl qidirish</p>
  <p class="pe-fix__good">✓ Yapon tilida <b>kelasi zamon yoʻq</b>. <ruby>明日<rt>あした</rt></ruby><ruby>行<rt>い</rt></ruby>きます — «ertaga boraman», feʼl oʻzgarmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Feʼlni shaxsga qarab oʻzgartirishga urinish</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>きます — men ham, sen ham, u ham. Kim ekanini <b>mavzu</b> koʻrsatadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Feʼlni gap oʻrtasiga qoʻyish</p>
  <p class="pe-fix__good">✓ Feʼl <b>doim oxirida</b>. Bu yapon gapining eng qatʼiy qoidasi — oʻzbekchadagi kabi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>明日<rt>あした</rt></ruby><ruby>行<rt>い</rt></ruby>きます — bu qaysi zamon?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Kelasi</b> — lekin feʼl shakli hozirgi bilan bir xil. Zamonni <ruby>明日<rt>あした</rt></ruby> («ertaga») koʻrsatadi, feʼl emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>飲<rt>の</rt></ruby>みます ning inkori qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>飲<rt>の</rt></ruby>みません</b> — ます oʻrniga ません. Boshqa hech narsa oʻzgarmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. します feʼli nega ayniqsa foydali?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>U <b>otlar bilan birikib</b> yangi feʼl yasaydi: <ruby>勉強<rt>べんきょう</rt></ruby>します, <ruby>電話<rt>でんわ</rt></ruby>します. Bitta feʼl bilan oʻnlab yangi ish nomini aytasiz.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Yapon gapida qaysi boʻlakning oʻrni qatʼiy?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Feʼl</b> — u doim <b>oxirida</b> turadi. Qolgan boʻlaklarning tartibi ancha erkin.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. ます shakli qanday uslubda?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Muloyim</b> (<ruby>丁寧体<rt>ていねいたい</rt></ruby>). Notanish odam bilan ham, oʻqituvchi bilan ham xavfsiz. Oddiy shaklni PJ-45 da koʻramiz.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>行<rt>い</rt></ruby>きます</b> — boraman</li>
  <li><b><ruby>来<rt>き</rt></ruby>ます</b> — kelaman</li>
  <li><b><ruby>食<rt>た</rt></ruby>べます</b> — yeyman</li>
  <li><b><ruby>飲<rt>の</rt></ruby>みます</b> — ichaman</li>
  <li><b><ruby>読<rt>よ</rt></ruby>みます</b> — oʻqiyman</li>
  <li><b><ruby>書<rt>か</rt></ruby>きます</b> — yozaman</li>
  <li><b>します</b> — qilaman</li>
  <li><b><ruby>毎日<rt>まいにち</rt></ruby></b> — har kuni</li>
  <li><b><ruby>明日<rt>あした</rt></ruby></b> — ertaga</li>
  <li><b><ruby>勉強<rt>べんきょう</rt></ruby>します</b> — oʻqiyman, shugʻullanaman</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>ます</b> shakli shaxsga qarab <b>oʻzgarmaydi</b> — です kabi.</li>
    <li>Yapon tilida <b>kelasi zamon yoʻq</b>: zamonni vaqt soʻzi koʻrsatadi.</li>
    <li>Inkor — <b>ません</b>. Feʼl esa doim gap <b>oxirida</b>.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-21: を va に — toʻldiruvchi va yoʻnalish",
        "category": "japanese",
        "order": 21,
        "summary": (
            "Ikki qoʻshimcha, ikki aniq vazifa — va ikkalasi ham oʻzbekcha "
            "kelishiklarga deyarli aynan mos tushadi: を = -ni, に = -ga."
        ),
        "stories": ["ジャスルさんの いちにち"],
        "content": """
<h2>PJ-21: を va に — toʻldiruvchi va yoʻnalish</h2>

<p>Oʻtgan darsda feʼlni oldingiz. Endi unga <em>nima</em> va <em>qayerga</em>
qoʻshish kerak — va aynan shu ikkita qoʻshimcha buni qiladi.</p>

<p>Bu dars oʻzbek oʻquvchi uchun kursdagi eng oson darslardan biri boʻlishi
kerak, chunki <b>を</b> va <b>に</b> oʻzbekcha <em>-ni</em> va <em>-ga</em>
kelishiklariga deyarli aynan mos tushadi. Ingliz tilini oʻrgangan odam bu
yerda qiynaladi; siz esa allaqachon bu tizim ichida yashaysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>を bilan toʻldiruvchini belgilaysiz</li>
    <li>に bilan yoʻnalishni va vaqtni koʻrsatasiz</li>
    <li>に ning uch vazifasini bir joyda koʻrasiz</li>
    <li>を [o] deb oʻqilishini yana bir marta mustahkamlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻzbekcha bilan yonma-yon</span>
  <span class="pe-chip pe-chip--o">を = -ni</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--adv">に = -ga</span>
</div>

<h3>1. を — «nimani»</h3>

<p><b>を</b> feʼlning toʻldiruvchisini belgilaydi: ish <em>nimaga</em>
qaratilgan.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n"><ruby>本<rt>ほん</rt></ruby></span>
  <span class="pj-joshi__p">を<small>TOʻLDIRUVCHI</small></span>
  <span class="pj-joshi__v"><ruby>読<rt>よ</rt></ruby>みます</span>
  <span class="pj-joshi__uz">Men kitobni oʻqiyman. — kitob-NI, aynan を ning ishi.</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu — kursdagi eng toza moslik.</b> Oʻzbekcha «kitob<b>ni</b> oʻqiyman»
  va yaponcha <ruby>本<rt>ほん</rt></ruby><b>を</b><ruby>読<rt>よ</rt></ruby>みます —
  <em>bir xil tuzilish</em>: ot, qoʻshimcha, feʼl. Ikkala tilda ham qoʻshimcha
  soʻzga yopishadi va feʼl oxirida turadi. Ingliz tilida esa toʻldiruvchi
  hech qanday belgi olmaydi va faqat <em>oʻrni</em> bilan tanaladi — shuning
  uchun ingliz tili orqali oʻrganayotgan odam bu yerda qiynaladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>毎朝<rt>まいあさ</rt></ruby>コーヒーを<ruby>飲<rt>の</rt></ruby>みます。</p>
  <p class="pe-ex__rom">maiasa kōhī o nomimasu</p>
  <p class="pe-ex__uz">Har ertalab kofe ichaman.</p>
  <p class="pe-ex__why">Vaqt soʻzi boshida, toʻldiruvchi を bilan, feʼl oxirida. Bu — yaponcha gapning eng oddiy toʻliq shakli.</p>
</div>

<div class="pj-say">
  <span class="pj-say__from">を</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[o]</span>
  <span class="pj-say__why">«wo» emas — PJ-4 dagi qoida, va u faqat qoʻshimcha</span>
</div>

<h3>2. に — «qayerga»</h3>

<p><b>に</b> harakatning <em>yoʻnalishini</em> koʻrsatadi. U
<ruby>行<rt>い</rt></ruby>きます, <ruby>来<rt>き</rt></ruby>ます,
<ruby>帰<rt>かえ</rt></ruby>ります kabi feʼllar bilan ishlaydi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>学校<rt>がっこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。</p>
  <p class="pe-ex__rom">gakkō ni ikimasu</p>
  <p class="pe-ex__uz">Maktabga boraman.</p>
  <p class="pe-ex__why">Yana aynan moslik: «maktab<b>ga</b>» = <ruby>学校<rt>がっこう</rt></ruby><b>に</b>.</p>
</div>

<h3>3. に ning uch vazifasi</h3>

<p>PJ-16 da <b>に</b> ni «qayerda» maʼnosida koʻrgan edingiz. Endi uchta
vazifasi bir jadvalda turadi — va ularning hammasi bitta gʻoyaga bogʻlanadi:
<b>に nuqtani koʻrsatadi</b>, fazoda ham, vaqtda ham.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Vazifa</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">joy (turish)</td>
      <td><ruby>教室<rt>きょうしつ</rt></ruby>にいます</td><td class="pj-uz">sinfdaman</td></tr>
  <tr><td class="pj-stem">yoʻnalish</td>
      <td><ruby>学校<rt>がっこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます</td><td class="pj-uz">maktabga boraman</td></tr>
  <tr><td class="pj-stem">vaqt (nuqta)</td>
      <td><ruby>七時<rt>しちじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きます</td><td class="pj-uz">soat yettida turaman</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Vaqtda に doim qoʻyilmaydi.</b> Aniq <em>son</em> bilan aytilgan
  vaqtga に qoʻyiladi: <ruby>七時<rt>しちじ</rt></ruby>に,
  <ruby>月曜日<rt>げつようび</rt></ruby>に. Lekin
  <ruby>今日<rt>きょう</rt></ruby>, <ruby>明日<rt>あした</rt></ruby>,
  <ruby>毎日<rt>まいにち</rt></ruby> kabi soʻzlarga <b>に qoʻyilmaydi</b> —
  ular oʻzi vaqtni bildiradi. «<ruby>明日<rt>あした</rt></ruby>に» notoʻgʻri.</p>
</div>

<h3>4. を olmaydigan feʼllar</h3>

<p>Bir narsani hozirdan aytib qoʻyish kerak, chunki u keyinroq koʻp xatoga
sabab boʻladi: <b>hamma feʼl ham を olmaydi</b>. Faqat <em>oʻtimli</em>
feʼllar oladi — yaʼni «nimani?» degan savolga javob beradiganlari.</p>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">を OLADI</p>
    <p class="pj-pair__form"><ruby>読<rt>よ</rt></ruby>みます</p>
    <p>«Nimani oʻqiyman?» — savol maʼnoli. Shuning uchun toʻldiruvchi bor:
    <ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">を OLMAYDI</p>
    <p class="pj-pair__form"><ruby>行<rt>い</rt></ruby>きます</p>
    <p>«Nimani boraman?» — maʼnosiz. Bunday feʼl <b>に</b> oladi:
    <ruby>学校<rt>がっこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Sinash usuli oʻzbekchada ham ishlaydi.</b> Feʼlga «nimani?» deb savol
  bering. «Kitobni oʻqiyman» — maʼnoli, demak <b>を</b>. «Maktabni boraman» —
  maʼnosiz, demak <b>に</b>. Oʻzbek tilida ham xuddi shu farq bor va siz uni
  oʻylamasdan toʻgʻri ishlatasiz — endi shu sezgingizga ishonishingiz
  mumkin.</p>
</div>

<h3>5. Toʻliq gap quramiz</h3>

<p>Endi hamma boʻlak bor. Yaponcha gapning odatiy tartibi shunday:</p>

<ol class="pe-steps">
  <li><b>Mavzu</b> — <ruby>私<rt>わたし</rt></ruby>は</li>
  <li><b>Vaqt</b> — <ruby>毎日<rt>まいにち</rt></ruby></li>
  <li><b>Joy / yoʻnalish</b> — <ruby>学校<rt>がっこう</rt></ruby>に</li>
  <li><b>Toʻldiruvchi</b> — <ruby>本<rt>ほん</rt></ruby>を</li>
  <li><b>Feʼl</b> — <ruby>読<rt>よ</rt></ruby>みます</li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>は<ruby>毎日<rt>まいにち</rt></ruby><ruby>学校<rt>がっこう</rt></ruby>で<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます。</p>
  <p class="pe-ex__rom">watashi wa mainichi gakkō de hon o yomimasu</p>
  <p class="pe-ex__uz">Men har kuni maktabda kitob oʻqiyman.</p>
  <p class="pe-ex__why">Diqqat: bu yerda に emas, <b>で</b> ishlatilgan — chunki maktab <em>yoʻnalish</em> emas, <em>ish bajarilayotgan joy</em>. Bu ikkalasining farqi keyingi darsning asosiy mavzusi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Tartib qatʼiy emas — feʼldan boshqasi erkin.</b> Vaqtni mavzudan oldin
  ham qoʻyish mumkin. Yaponcha gap qoʻshimchalar bilan ushlab turiladi, oʻrin
  bilan emas — shuning uchun boʻlaklarni surish maʼnoni buzmaydi. Faqat
  <b>feʼl oxirida qolishi shart</b>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ を ni «wo» deb oʻqish</p>
  <p class="pe-fix__good">✓ <b>[o]</b>. «wo» — belgining eski nomi va uni kompyuterda yozish usuli, xolos.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>明日<rt>あした</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます</p>
  <p class="pe-fix__good">✓ <ruby>明日<rt>あした</rt></ruby><ruby>行<rt>い</rt></ruby>きます — <ruby>明日<rt>あした</rt></ruby> oʻzi vaqtni bildiradi, に kerak emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>本<rt>ほん</rt></ruby>に<ruby>読<rt>よ</rt></ruby>みます</p>
  <p class="pe-fix__good">✓ <ruby>本<rt>ほん</rt></ruby><b>を</b><ruby>読<rt>よ</rt></ruby>みます — kitob toʻldiruvchi, yoʻnalish emas. Oʻzbekchada ham «kitob<em>ni</em>», «kitob<em>ga</em>» emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Kitobni oʻqiyman» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます。 — <b>を</b>, chunki kitob toʻldiruvchi: oʻzbekchadagi «-ni».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Maktabga boraman» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><ruby>学校<rt>がっこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。 — <b>に</b>, chunki bu yoʻnalish: oʻzbekchadagi «-ga».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. に ning uch vazifasi qaysi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Joy</b> (turish), <b>yoʻnalish</b> va <b>aniq vaqt</b>. Uchalasi bitta gʻoyaga bogʻlanadi: に <em>nuqtani</em> koʻrsatadi — fazoda ham, vaqtda ham.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>明日<rt>あした</rt></ruby> ga に qoʻyiladimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> <ruby>明日<rt>あした</rt></ruby>, <ruby>今日<rt>きょう</rt></ruby>, <ruby>毎日<rt>まいにち</rt></ruby> oʻzi vaqtni bildiradi. に faqat <b>son bilan</b> aytilgan vaqtga qoʻyiladi: <ruby>七時<rt>しちじ</rt></ruby>に.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Yaponcha gapda qaysi boʻlakning oʻrni qatʼiy?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Faqat <b>feʼl</b> — u oxirida. Qolgan boʻlaklar qoʻshimchalar bilan ushlab turiladi, shuning uchun ularni surish mumkin.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>を</b> — toʻldiruvchi qoʻshimchasi (-ni), [o]</li>
  <li><b>に</b> — yoʻnalish, joy, aniq vaqt (-ga, -da)</li>
  <li><b><ruby>肉<rt>にく</rt></ruby></b> — goʻsht</li>
  <li><b><ruby>魚<rt>さかな</rt></ruby></b> — baliq</li>
  <li><b><ruby>水<rt>みず</rt></ruby></b> — suv</li>
  <li><b><ruby>手紙<rt>てがみ</rt></ruby></b> — xat</li>
  <li><b><ruby>音楽<rt>おんがく</rt></ruby></b> — musiqa</li>
  <li><b><ruby>映画<rt>えいが</rt></ruby></b> — kino</li>
  <li><b><ruby>帰<rt>かえ</rt></ruby>ります</b> — qaytaman</li>
  <li><b><ruby>七時<rt>しちじ</rt></ruby></b> — soat yetti</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>を = -ni</b> (toʻldiruvchi), <b>に = -ga</b> (yoʻnalish) — oʻzbekcha bilan deyarli aynan moslik.</li>
    <li><b>に</b> nuqtani koʻrsatadi: joy, yoʻnalish yoki <b>aniq</b> vaqt.</li>
    <li><ruby>今日<rt>きょう</rt></ruby>, <ruby>明日<rt>あした</rt></ruby>, <ruby>毎日<rt>まいにち</rt></ruby> ga <b>に qoʻyilmaydi</b>.</li>
  </ul>
</div>
""",
    },
]
