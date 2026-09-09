# -*- coding: utf-8 -*-
"""Prime Japanese — Block B, darslar 16–18.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_JAPANESE.md
Lesson list: tutorial/management/commands/toc_prime_japanese.txt

Uchta boʻlak: dars + mashq (20 savol) + oʻqish matni (audio bilan).
Mashqlar:  practice/management/commands/_practice_pj_16_18.py
Matnlar:   corner/management/commands/_stories_prime_japanese_16_18.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_16_18.py --author=prime
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
        "title": "PJ-16: ここ・そこ・あそこ va に — joy va «bor» gapi (あります / います)",
        "category": "japanese",
        "order": 16,
        "summary": (
            "Joy soʻzlari bilan ko-so-a-do tizimi yopiladi, va yaponchadagi «bor» "
            "gapini quramiz — jonli narsa uchun います, jonsiz narsa uchun あります."
        ),
        "stories": ["ねこは どこですか"],
        "content": """
<h2>PJ-16: ここ・そこ・あそこ va に — joy va «bor» gapi (あります / います)</h2>

<p>Oʻtgan darsda narsalarni koʻrsatishni oʻrgandingiz. Bugun <b>joy</b>larni
koʻrsatasiz — va shu bilan ko-so-a-do jadvali toʻliq yopiladi.</p>

<p>Keyin esa yaponchadagi eng kerakli gaplardan biri keladi: <b>«…bor»</b>.
Bu yerda bitta gʻalati narsa bor va uni darrov aytib qoʻyaman: yapon tilida
<b>ikkita</b> «bor» soʻzi mavjud, va qaysi birini tanlash narsaning
<em>tirikligiga</em> bogʻliq.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ここ・そこ・あそこ・どこ bilan joyni koʻrsatasiz</li>
    <li>に qoʻshimchasi bilan «qayerda» ekanini aytasiz</li>
    <li>あります va います ni toʻgʻri tanlaysiz</li>
    <li>Ikki xil «bor» gapini qurasiz: «X qayerda» va «qayerda X bor»</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bor gapining qolipi</span>
  <span class="pe-chip pe-chip--adv">JOY</span>
  <span class="pe-chip pe-chip--opt">に</span>
  <span class="pe-chip pe-chip--s">NARSA</span>
  <span class="pe-chip pe-chip--opt">が</span>
  <span class="pe-chip pe-chip--v">あります / います</span>
</div>

<h3>1. Joy soʻzlari — jadval yopiladi</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Masofa</th><th>Narsa</th><th>Ot bilan</th><th>Joy</th><th>Hurmatli</th></tr>
  <tr><td class="pj-stem">こ — menga yaqin</td><td>これ</td><td>この</td>
      <td class="pj-res">ここ</td><td class="pj-uz">こちら</td></tr>
  <tr><td class="pj-stem">そ — senga yaqin</td><td>それ</td><td>その</td>
      <td class="pj-res">そこ</td><td class="pj-uz">そちら</td></tr>
  <tr><td class="pj-stem">あ — uzoq</td><td>あれ</td><td>あの</td>
      <td class="pj-res">あそこ</td><td class="pj-uz">あちら</td></tr>
  <tr><td class="pj-stem">ど — savol</td><td>どれ</td><td>どの</td>
      <td class="pj-res">どこ</td><td class="pj-uz">どちら</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Oxirgi ustunga eʼtibor bering.</b> こちら・そちら・あちら asli
  «bu tomon» degani, lekin ular <b>hurmatliroq</b> shakl sifatida ham ishlaydi.
  Doʻkonda sotuvchi «こちらです» desa, u «bu yoqda» ham, «mana bu» ham demoqchi.
  どちら esa «qayer» ning muloyim shakli — va PJ-15 dagi «ikkitadan qaysi biri»
  maʼnosi ham shu soʻzda.</p>
</div>

<h3>2. に — «…da, …ga»</h3>

<p><b>に</b> — joy qoʻshimchasi. U otdan keyin turadi va «qayerda» degan
savolga javob beradi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>教室<rt>きょうしつ</rt></ruby></span>
  <span class="pj-joshi__p">に<small>JOY</small></span>
  <span class="pj-joshi__n"><ruby>先生<rt>せんせい</rt></ruby></span>
  <span class="pj-joshi__p">が<small>EGA</small></span>
  <span class="pj-joshi__v">います</span>
  <span class="pj-joshi__uz">Sinfda oʻqituvchi bor. — oʻzbekchada ham: sinf-DA.</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu oʻzbekchaga aynan mos tushadi.</b> «Sinf<b>da</b>» — oʻrin-payt
  kelishigi, soʻzga yopishadi va otdan keyin turadi. Yaponcha <b>に</b> ham
  xuddi shunday: soʻzdan keyin, soʻzga yopishgan. Ingliz tilida esa
  <em>oldin</em> keladigan predlog ishlatiladi — yana bir joy, oʻzbek
  oʻquvchi ustunlikka ega.</p>
</div>

<h3>3. あります va います — qaysi birini tanlash</h3>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">あります — JONSIZ</p>
    <p class="pj-pair__form">あります</p>
    <p>Kitob, stol, pul, maktab, daraxt. Qimirlamaydigan, oʻz irodasi
    boʻlmagan hamma narsa.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">います — JONLI</p>
    <p class="pj-pair__form">います</p>
    <p>Odam, mushuk, it, baliq. Oʻz irodasi bilan harakatlanadigan
    tirik jonzot.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>があります。</p>
  <p class="pe-ex__rom">tsukue no ue ni hon ga arimasu</p>
  <p class="pe-ex__uz">Stol ustida kitob bor.</p>
  <p class="pe-ex__why">Kitob — jonsiz, demak <b>あります</b>. Diqqat: «stol ustida» = <ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby> — yaponchada joy soʻzi otdan <em>keyin</em> keladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>学生<rt>がくせい</rt></ruby>がいます。</p>
  <p class="pe-ex__rom">kyōshitsu ni gakusē ga imasu</p>
  <p class="pe-ex__uz">Sinfda talaba bor.</p>
  <p class="pe-ex__why">Talaba — jonli, demak <b>います</b>. Bu farqni yaponlar bir zumda sezadi, shuning uchun uni yodlab qoʻyish kerak.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Chegara doim aniq emas.</b> Mashina, poyezd va robot — jonsiz, demak
  <b>あります</b>, garchi ular harakatlansa ham. Oʻsimlik ham jonsiz. Lekin
  mushukni <b>います</b> deb aytasiz. Qoida: <em>oʻz irodasi bilan
  harakatlanadimi?</em> Agar ha — います.</p>
</div>

<h3>4. Ikki xil «bor» gapi</h3>

<p>Bir xil maʼlumotni ikki xil aytish mumkin, va farqi — <b>nima haqida
gapirayotganingizda</b>. Bu PJ-14 dagi は va が farqining amaliy koʻrinishi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Misol</th><th>Nimani soʻrayapti</th></tr>
  <tr><td class="pj-stem">JOY に NARSA が あります</td>
      <td><ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>があります</td>
      <td class="pj-uz">«Sinfda nima bor?» — joy maʼlum, narsa yangi</td></tr>
  <tr><td class="pj-stem">NARSA は JOY に あります</td>
      <td><ruby>本<rt>ほん</rt></ruby>は<ruby>教室<rt>きょうしつ</rt></ruby>にあります</td>
      <td class="pj-uz">«Kitob qayerda?» — narsa maʼlum, joy yangi</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Qoida sodda:</b> <em>maʼlum</em> narsa <b>は</b> oladi va gap boshiga
  chiqadi; <em>yangi</em> narsa <b>が</b> oladi. Shuning uchun «Mushuk qayerda?»
  degan savolga «<ruby>猫<rt>ねこ</rt></ruby>は…» deb javob berasiz — mushuk
  allaqachon maʼlum.</p>
</div>

<h3>5. Joy soʻzlari — <ruby>上<rt>うえ</rt></ruby> · <ruby>下<rt>した</rt></ruby> · <ruby>中<rt>なか</rt></ruby> · <ruby>前<rt>まえ</rt></ruby> · <ruby>後<rt>うし</rt></ruby>ろ</h3>

<p>«Sinfda» deyish oson, lekin «stol <em>ustida</em>» deyish uchun qoʻshimcha
soʻz kerak. Yaponchada bu soʻzlar otdan <b>keyin</b> turadi va の bilan
ulanadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pj-stem"><ruby>上<rt>うえ</rt></ruby></td><td class="pj-uz">ust</td>
      <td><ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に — stol ustida</td></tr>
  <tr><td class="pj-stem"><ruby>下<rt>した</rt></ruby></td><td class="pj-uz">ost</td>
      <td><ruby>机<rt>つくえ</rt></ruby>の<ruby>下<rt>した</rt></ruby>に — stol tagida</td></tr>
  <tr><td class="pj-stem"><ruby>中<rt>なか</rt></ruby></td><td class="pj-uz">ich</td>
      <td><ruby>鞄<rt>かばん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に — sumka ichida</td></tr>
  <tr><td class="pj-stem"><ruby>前<rt>まえ</rt></ruby></td><td class="pj-uz">old</td>
      <td><ruby>店<rt>みせ</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>に — doʻkon oldida</td></tr>
  <tr><td class="pj-stem"><ruby>後<rt>うし</rt></ruby>ろ</td><td class="pj-uz">orqa</td>
      <td><ruby>学校<rt>がっこう</rt></ruby>の<ruby>後<rt>うし</rt></ruby>ろに — maktab orqasida</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Tartib oʻzbekchaga aynan teskari emas — bir xil!</b> Oʻzbekchada
  «stol<em>ning</em> ust<em>ida</em>», yaponchada
  <ruby>机<rt>つくえ</rt></ruby><b>の</b><ruby>上<rt>うえ</rt></ruby><b>に</b>.
  Ikkalasida ham: ot → bogʻlovchi → joy soʻzi → oʻrin qoʻshimchasi.
  Ingliz tilida esa bu butunlay boshqa tartibda quriladi. Bu <b>の</b>
  qoʻshimchasiga PJ-17 da butun dars bagʻishlanadi.</p>
</div>

<h3>6. Inkor: ありません va いません</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Tur</th><th>Bor</th><th>Yoʻq</th></tr>
  <tr><td class="pj-stem">jonsiz</td><td class="pj-res">あります</td><td class="pj-end">ありません</td></tr>
  <tr><td class="pj-stem">jonli</td><td class="pj-res">います</td><td class="pj-end">いません</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">ここに<ruby>猫<rt>ねこ</rt></ruby>はいません。</p>
  <p class="pe-ex__rom">koko ni neko wa imasen</p>
  <p class="pe-ex__uz">Bu yerda mushuk yoʻq.</p>
  <p class="pe-ex__why">Inkor gapda が koʻpincha <b>は</b> ga almashadi — «mushukka kelsak, u yoʻq». Bu juda keng tarqalgan va tabiiy eshitiladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>先生<rt>せんせい</rt></ruby>があります</p>
  <p class="pe-fix__good">✓ …<ruby>先生<rt>せんせい</rt></ruby>が<b>います</b> — odam jonli, demak います.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>がいます</p>
  <p class="pe-fix__good">✓ …<ruby>本<rt>ほん</rt></ruby>が<b>あります</b> — kitob jonsiz.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ここは<ruby>猫<rt>ねこ</rt></ruby>がいます</p>
  <p class="pe-fix__good">✓ ここ<b>に</b><ruby>猫<rt>ねこ</rt></ruby>がいます — joy uchun に kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Sinfda oʻqituvchi bor» — あります yoki います?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>います</b> — odam jonli. <ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>先生<rt>せんせい</rt></ruby>がいます。</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Mashina uchun qaysi feʼl ishlatiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>あります</b>. Mashina harakatlanadi, lekin <em>oʻz irodasi bilan</em> emas — shuning uchun jonsiz sanaladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Kitob qayerda?» degan savolga javob qaysi qolipda boʻladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>NARSA は JOY に あります</b>: <ruby>本<rt>ほん</rt></ruby>は<ruby>教室<rt>きょうしつ</rt></ruby>にあります。 Kitob maʼlum, shuning uchun は oladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. どちら soʻzining ikkita maʼnosi qaysi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>«Qayer» ning <b>muloyim</b> shakli, va «<b>ikkitadan</b> qaysi biri» (PJ-15).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Stol ustida» ni yaponchada qanday aytasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に — joy soʻzi (<ruby>上<rt>うえ</rt></ruby>) otdan <b>keyin</b> keladi, oʻzbekchadagi «ust-i-da» kabi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ここ・そこ・あそこ・どこ</b> — bu yer, shu yer, u yer, qayer</li>
  <li><b>こちら・どちら</b> — bu tomon (hurmatli), qayer</li>
  <li><b>に</b> — …da, …ga (joy)</li>
  <li><b>あります</b> — bor (jonsiz)</li>
  <li><b>います</b> — bor (jonli)</li>
  <li><b><ruby>机<rt>つくえ</rt></ruby></b> — stol</li>
  <li><b><ruby>上<rt>うえ</rt></ruby>・<ruby>下<rt>した</rt></ruby></b> — ust, ost</li>
  <li><b><ruby>中<rt>なか</rt></ruby></b> — ich</li>
  <li><b><ruby>猫<rt>ねこ</rt></ruby></b> — mushuk</li>
  <li><b><ruby>教室<rt>きょうしつ</rt></ruby></b> — sinf xonasi</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Joy soʻzlari <b>ここ・そこ・あそこ・どこ</b> bilan ko-so-a-do jadvali yopildi.</li>
    <li>Yaponchada ikkita «bor»: <b>あります</b> jonsiz, <b>います</b> jonli narsa uchun.</li>
    <li>Qolip: <b>JOY に NARSA が あります</b>, yoki maʼlum narsa haqida gapirsangiz <b>NARSA は JOY に あります</b>.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-17: の — egalik va ikki otni bogʻlash",
        "category": "japanese",
        "order": 17,
        "summary": (
            "Yaponchadagi eng koʻp ishlaydigan bitta belgi. Egalik, bogʻlash va "
            "«meniki» — uchalasi ham bitta の bilan."
        ),
        "stories": ["わたしの かばん"],
        "content": """
<h2>PJ-17: の — egalik va ikki otni bogʻlash</h2>

<p>Bitta hiragana belgisi. Bitta tovush. Va yapon tilidagi eng koʻp
ishlaydigan grammatik vositalardan biri — shu qadarki, siz uni allaqachon
toʻrt darsdan beri koʻrib kelyapsiz: <b>この</b>, <b>その</b>,
<ruby>机<rt>つくえ</rt></ruby><b>の</b><ruby>上<rt>うえ</rt></ruby>,
<ruby>私<rt>わたし</rt></ruby><b>の</b>.</p>

<p>Bugun nihoyat unga toʻliq qaraymiz. Yaxshi xabar: <b>の</b> ning qoidasi
bitta va u juda sodda.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>の bilan egalikni bildirasiz: <ruby>私<rt>わたし</rt></ruby>の<ruby>本<rt>ほん</rt></ruby></li>
    <li>Ikki otni bogʻlaysiz: <ruby>日本語<rt>にほんご</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby></li>
    <li>«Meniki» deb otni tushirib qoldirasiz</li>
    <li>Uzun zanjir qurasiz va tartibning mantiqini tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta qoida, hamma holat uchun</span>
  <span class="pe-chip pe-chip--s">A</span>
  <span class="pe-chip pe-chip--opt">の</span>
  <span class="pe-chip pe-chip--o">B</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">A ning B si</span>
</div>

<h3>1. Egalik — «kimning»</h3>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">の<small>EGALIK</small></span>
  <span class="pj-joshi__n"><ruby>本<rt>ほん</rt></ruby></span>
  <span class="pj-joshi__uz">mening kitobim — oʻzbekchada ham: men<b>ning</b> kitob<b>im</b>.</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek oʻquvchi uchun deyarli tayyor qoida.</b> Oʻzbekchada egalik
  <em>ikki marta</em> belgilanadi: «men<b>ning</b> kitob<b>im</b>» — egada
  ham, egalik qilinganda ham qoʻshimcha bor. Yaponchada esa <b>bitta</b>
  belgi yetadi va u faqat egada turadi:
  <ruby>私<rt>わたし</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>. Yaʼni ikkinchi
  qoʻshimchani <em>unutish</em> kerak, qoʻshish emas.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">アフソナさんの<ruby>鞄<rt>かばん</rt></ruby>です。</p>
  <p class="pe-ex__rom">afusona-san no kaban desu</p>
  <p class="pe-ex__uz">Bu Afsonaning sumkasi.</p>
  <p class="pe-ex__why">Tartib: <b>ega → の → narsa</b>. Oʻzbekchada ham shunday, shuning uchun bu yerda hech qanday qiyinchilik yoʻq.</p>
</div>

<h3>2. Ikki otni bogʻlash — «qanaqa, qayerdagi, qaysi haqda»</h3>

<p>Endi <b>の</b> ning kengroq vazifasi. U faqat egalikni emas, <em>har qanday
munosabatni</em> bildiradi: A birinchi otni B ga nisbatan aniqlaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yaponcha</th><th>Munosabat</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>日本語<rt>にほんご</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby></td>
      <td class="pj-uz">nima haqida</td><td class="pj-uz">yapon tili oʻqituvchisi</td></tr>
  <tr><td><ruby>日本<rt>にほん</rt></ruby>の<ruby>時計<rt>とけい</rt></ruby></td>
      <td class="pj-uz">qayerdan</td><td class="pj-uz">yapon soati</td></tr>
  <tr><td><ruby>大学<rt>だいがく</rt></ruby>の<ruby>学生<rt>がくせい</rt></ruby></td>
      <td class="pj-uz">qayerdagi</td><td class="pj-uz">universitet talabasi</td></tr>
  <tr><td><ruby>木<rt>き</rt></ruby>の<ruby>机<rt>つくえ</rt></ruby></td>
      <td class="pj-uz">nimadan</td><td class="pj-uz">yogʻoch stol</td></tr>
  <tr><td><ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby></td>
      <td class="pj-uz">qayeri</td><td class="pj-uz">stolning usti</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Tartibni eslab qolish uchun:</b> yaponchada <b>aniqlovchi doim
  oldin</b> turadi. «Yapon tili oʻqituvchisi» — avval «yapon tili», keyin
  «oʻqituvchi». Oʻzbekchada ham xuddi shunday tartib. Shuning uchun uzun
  zanjirni oʻqiyotganda <b>oxirgi soʻz</b> asosiy narsa boʻladi —
  qolganlari uni aniqlaydi.</p>
</div>

<h3>3. «Meniki» — otni tushirib qoldirish</h3>

<p>Agar nima haqida gapirilayotgani aniq boʻlsa, <b>の</b> dan keyingi otni
umuman aytmasangiz ham boʻladi. Shunda の ning oʻzi «…niki» degan maʼnoni
oladi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">Toʻliq</p>
    <p class="pj-big">の＋ot</p>
    <p>これは<ruby>私<rt>わたし</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>です。<br>
    Bu mening kitobim.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">Ot tushirilgan</p>
    <p class="pj-big">の</p>
    <p>これは<ruby>私<rt>わたし</rt></ruby>のです。<br>
    Bu meniki.</p></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>鞄<rt>かばん</rt></ruby>は<ruby>誰<rt>だれ</rt></ruby>のですか。</p>
  <p class="pe-ex__rom">kono kaban wa dare no desu ka</p>
  <p class="pe-ex__uz">Bu sumka kimniki?</p>
  <p class="pe-ex__why">Bu yerda ikkita ish birga: この otga yopishgan (PJ-15), の esa otsiz turibdi va «kimniki» degan maʼno beryapti.</p>
</div>

<h3>4. Zanjir — の bir necha marta</h3>

<p><b>の</b> ni ketma-ket takrorlash mumkin. Har bir <b>の</b> chapdagi soʻzni
oʻngdagisiga bogʻlaydi, va zanjir <em>chapdan oʻngga</em> torayib boradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>の<ruby>友達<rt>ともだち</rt></ruby>の<ruby>本<rt>ほん</rt></ruby></p>
  <p class="pe-ex__rom">watashi no tomodachi no hon</p>
  <p class="pe-ex__uz">mening doʻstimning kitobi</p>
  <p class="pe-ex__why">Chapdan oʻngga oʻqing: men → doʻstim → kitob. Asosiy narsa — <b>oxirgi</b> soʻz, yaʼni kitob.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Ikkitadan koʻp の — ogʻir eshitiladi.</b> Grammatik jihatdan uchta,
  toʻrtta の ham mumkin, lekin yaponlar buni yoqtirmaydi. Uch bosqichdan
  uzun zanjirni ikki gapga boʻlish ancha tabiiyroq. Bu — uslub masalasi,
  xato emas.</p>
</div>

<h3>5. の qachon ISHLATILMAYDI</h3>

<p>Bir narsani darrov aytib qoʻyaman, chunki bu keyinroq koʻp xatoga sabab
boʻladi: <b>の faqat ikki OTNI bogʻlaydi</b>. Sifat bilan ishlatilmaydi.</p>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>大<rt>おお</rt></ruby>きいの<ruby>本<rt>ほん</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>大<rt>おお</rt></ruby>きい<ruby>本<rt>ほん</rt></ruby> — «katta kitob». Sifat otga toʻgʻridan-toʻgʻri yopishadi, oraliqda hech narsa yoʻq.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha shu yerda adashtiradi.</b> Biz «yogʻoch<em>dan</em> yasalgan
  stol» va «katta stol» ni bir xil tuzilishda aytamiz. Yaponchada esa farq bor:
  <ruby>木<rt>き</rt></ruby><b>の</b><ruby>机<rt>つくえ</rt></ruby> (ot + ot →
  の kerak), lekin <ruby>大<rt>おお</rt></ruby>きい<ruby>机<rt>つくえ</rt></ruby>
  (sifat + ot → の <em>yoʻq</em>). Sifatlarni PJ-25 va PJ-26 da koʻramiz;
  hozircha shuni bilib qoʻying: <b>の ikki ot orasida turadi, boshqa joyda
  emas</b>.</p>
</div>

<h3>6. この, その, あの nega の bilan tugaydi</h3>

<p>Endi PJ-15 dagi jumboq oʻz-oʻzidan yechiladi. <b>この</b> aslida
«こ + の» — «bu ning». Shuning uchun u ortidan albatta ot talab qiladi:
の bogʻlovchi, va bogʻlanadigan ikkinchi tomon boʻlishi kerak.</p>

<div class="pj-say">
  <span class="pj-say__from">この + <ruby>本<rt>ほん</rt></ruby></span>
  <span class="pj-say__arrow">=</span>
  <span class="pj-say__to">«bu» ning «kitob»i</span>
  <span class="pj-say__why">shuning uchun この yolgʻiz qololmaydi</span>
</div>

<div class="pe-call pe-tip">
  <p><b>これ</b> esa の siz — u toʻliq soʻz va hech narsani bogʻlamaydi.
  Ikki qatorni ajratadigan qoida shu bilan mantiqiy asosga ega boʻldi:
  <b>の bor — ot kerak, の yoʻq — ot kerak emas</b>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>本<rt>ほん</rt></ruby>の<ruby>私<rt>わたし</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby>の<ruby>本<rt>ほん</rt></ruby> — <b>ega oldin</b> turadi, xuddi oʻzbekchadagi kabi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>の です (egalikni ikki marta belgilash)</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>です — yaponchada bitta の yetadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ これの<ruby>本<rt>ほん</rt></ruby></p>
  <p class="pe-fix__good">✓ この<ruby>本<rt>ほん</rt></ruby> — これ da allaqachon の yoʻq, uni qoʻshib boʻlmaydi. Ot bilan この ishlatiladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Mening kitobim» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><ruby>私<rt>わたし</rt></ruby>の<ruby>本<rt>ほん</rt></ruby> — ega oldin, keyin の, keyin narsa. Oʻzbekchadagi ikkinchi qoʻshimcha («kitob<em>im</em>») yaponchada yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>日本語<rt>にほんご</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby> nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yapon tili oʻqituvchisi</b>. Bu yerda の egalikni emas, «nima haqida» degan munosabatni bildiryapti.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. これは<ruby>私<rt>わたし</rt></ruby>のです — bu nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>«Bu meniki»</b>. の dan keyingi ot tushirib qoldirilgan, chunki nima haqida gapirilayotgani aniq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>私<rt>わたし</rt></ruby>の<ruby>友達<rt>ともだち</rt></ruby>の<ruby>本<rt>ほん</rt></ruby> zanjirida asosiy narsa qaysi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>本<rt>ほん</rt></ruby></b> — oxirgi soʻz. Qolganlari uni aniqlaydi: men → doʻstim → kitob.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega この ortidan albatta ot kerak?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki この aslida <b>こ + の</b>, va の — bogʻlovchi. Bogʻlash uchun ikkinchi tomon kerak. これ da の yoʻq, shuning uchun u yolgʻiz tura oladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>の</b> — …ning, …niki (bogʻlovchi)</li>
  <li><b><ruby>誰<rt>だれ</rt></ruby>の</b> — kimniki</li>
  <li><b><ruby>鞄<rt>かばん</rt></ruby></b> — sumka</li>
  <li><b><ruby>大学<rt>だいがく</rt></ruby></b> — universitet</li>
  <li><b><ruby>会社<rt>かいしゃ</rt></ruby></b> — kompaniya</li>
  <li><b><ruby>車<rt>くるま</rt></ruby></b> — mashina</li>
  <li><b><ruby>家<rt>いえ</rt></ruby></b> — uy</li>
  <li><b><ruby>名前<rt>なまえ</rt></ruby></b> — ism</li>
  <li><b><ruby>友達<rt>ともだち</rt></ruby></b> — doʻst</li>
  <li><b><ruby>木<rt>き</rt></ruby></b> — daraxt, yogʻoch</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Bitta qoida: <b>A の B</b> = «A ning B si». Egalik ham, bogʻlash ham shu.</li>
    <li>Ot tushib qolsa, <b>の</b> ning oʻzi «…niki» maʼnosini oladi.</li>
    <li><b>この</b> = こ + の — shuning uchun u ortidan albatta ot talab qiladi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-18: Soʻroq soʻzlari — なに, だれ, どこ, いつ, どう, どれ va か",
        "category": "japanese",
        "order": 18,
        "summary": (
            "Yaponchaning butun soʻroq toʻplami bir darsda, va なに/なん farqi — "
            "boshlovchilar eng koʻp adashadigan nuqta."
        ),
        "stories": ["きょうしつは どこですか"],
        "content": """
<h2>PJ-18: Soʻroq soʻzlari — なに, だれ, どこ, いつ, どう, どれ va か</h2>

<p>Bir necha darsdan beri soʻroq soʻzlarini bittalab koʻrib kelyapsiz:
<ruby>誰<rt>だれ</rt></ruby> PJ-14 da, どれ va どの PJ-15 da, どこ PJ-16 da.
Bugun hammasini bir joyga yigʻamiz va yetishmayotganlarini qoʻshamiz.</p>

<p>Bitta yangi qiyinchilik ham bor: <b>なに</b> va <b>なん</b> — bir xil soʻzning
ikki oʻqilishi, va qaysi birini tanlash keyingi tovushga bogʻliq. Bu — bugungi
darsning asosiy ishi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Yaponchaning butun soʻroq toʻplamini bir jadvalda koʻrasiz</li>
    <li>なに va なん ni qachon ishlatishni bilasiz</li>
    <li>Soʻroq soʻzi gapning qayerida turishini tushunasiz</li>
    <li>Soʻroq soʻzi bilan doim が ishlatilishini mustahkamlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Soʻroq gapning qolipi</span>
  <span class="pe-chip pe-chip--neg">SOʻROQ SOʻZI</span>
  <span class="pe-op">…</span>
  <span class="pe-chip pe-chip--v">です</span>
  <span class="pe-chip pe-chip--opt">か</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">soʻz tartibi OʻZGARMAYDI</span>
</div>

<h3>1. Butun toʻplam</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻroq</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pj-stem"><ruby>何<rt>なに</rt></ruby> / <ruby>何<rt>なん</rt></ruby></td>
      <td class="pj-uz">nima</td><td>これは<ruby>何<rt>なん</rt></ruby>ですか</td></tr>
  <tr><td class="pj-stem"><ruby>誰<rt>だれ</rt></ruby></td>
      <td class="pj-uz">kim</td><td><ruby>誰<rt>だれ</rt></ruby>が<ruby>先生<rt>せんせい</rt></ruby>ですか</td></tr>
  <tr><td class="pj-stem">どこ</td>
      <td class="pj-uz">qayer</td><td><ruby>教室<rt>きょうしつ</rt></ruby>はどこですか</td></tr>
  <tr><td class="pj-stem">いつ</td>
      <td class="pj-uz">qachon</td><td><ruby>試験<rt>しけん</rt></ruby>はいつですか</td></tr>
  <tr><td class="pj-stem">どう</td>
      <td class="pj-uz">qanday</td><td><ruby>日本語<rt>にほんご</rt></ruby>はどうですか</td></tr>
  <tr><td class="pj-stem">どれ / どの</td>
      <td class="pj-uz">qaysi biri / qaysi…</td><td>どれが<ruby>私<rt>わたし</rt></ruby>のですか</td></tr>
  <tr><td class="pj-stem">どちら</td>
      <td class="pj-uz">ikkitadan qaysi / qayer (muloyim)</td><td>お<ruby>国<rt>くに</rt></ruby>はどちらですか</td></tr>
  <tr><td class="pj-stem">いくら</td>
      <td class="pj-uz">qancha (narx)</td><td>これはいくらですか</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Yarmi «ど» bilan boshlanadi.</b> どこ, どれ, どの, どちら, どう — bularning
  hammasi PJ-15 dagi ko-so-a-do jadvalining <b>ど</b> ustuni. Yaʼni siz ularni
  allaqachon tizim sifatida bilasiz. Yodlash kerak boʻlgani — <ruby>何<rt>なに</rt></ruby>,
  <ruby>誰<rt>だれ</rt></ruby>, いつ va いくら.</p>
</div>

<h3>2. なに yoki なん — darsning asosiy qoidasi</h3>

<p>Bitta kanji, <ruby>何<rt>なに</rt></ruby>, ikki xil oʻqiladi. Qoida
<em>talaffuzga</em> asoslangan: <b>なん</b> ni aytish osonroq boʻlgan joyda
なん ishlatiladi.</p>

<div class="pj-yomi">
  <div class="pj-yomi__side">
    <p class="pj-yomi__h">なん — d, t, n dan oldin</p>
    <p class="pj-yomi__ex"><ruby>何<rt>なん</rt></ruby>です か</p>
    <p>です, で, と, の va sanoq soʻzlaridan oldin. Bu — eng koʻp uchraydigan
    holat.</p>
  </div>
  <div class="pj-yomi__side pj-yomi__side--kun">
    <p class="pj-yomi__h">なに — qolgan hamma joyda</p>
    <p class="pj-yomi__ex"><ruby>何<rt>なに</rt></ruby>が</p>
    <p>が, を, は va koʻpchilik boshqa qoʻshimchalardan oldin.</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yaponcha</th><th>Oʻqilishi</th><th>Nega</th></tr>
  <tr><td><ruby>何<rt>なん</rt></ruby>ですか</td><td class="pj-res">nan desu ka</td>
      <td class="pj-uz">です dan oldin → なん</td></tr>
  <tr><td><ruby>何<rt>なん</rt></ruby>の<ruby>本<rt>ほん</rt></ruby></td><td class="pj-res">nan no hon</td>
      <td class="pj-uz">の dan oldin → なん</td></tr>
  <tr><td><ruby>何<rt>なん</rt></ruby><ruby>人<rt>にん</rt></ruby></td><td class="pj-res">nan nin</td>
      <td class="pj-uz">sanoq soʻzi → なん</td></tr>
  <tr><td><ruby>何<rt>なに</rt></ruby>が</td><td class="pj-res">nani ga</td>
      <td class="pj-uz">が dan oldin → なに</td></tr>
  <tr><td><ruby>何<rt>なに</rt></ruby>を</td><td class="pj-res">nani o</td>
      <td class="pj-uz">を dan oldin → なに</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu qoidani yodlashning eng oson yoʻli — ovoz.</b> «なにです» deb ayting,
  keyin «なんです» deb ayting. Ikkinchisi tilga ancha yengil tushadi, chunki
  <b>ん</b> va <b>で</b> bir joyda — ikkalasi ham til uchi bilan chiqadi.
  Yapon tili shunday qoidalarga toʻla: qiyin birikma <em>oʻz-oʻzidan</em>
  yengillashadi. PJ-6 dagi ん → [m] oʻzgarishi ham xuddi shu mantiq edi.</p>
</div>

<h3>3. Soʻroq soʻzi gapning qayerida turadi</h3>

<p>Mana yapon tilining eng qulay xususiyatlaridan biri: soʻroq soʻzi
<b>javob turadigan joyda</b> turadi. Gapni qayta qurish kerak emas.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">SAVOL</p>
    <p><ruby>教室<rt>きょうしつ</rt></ruby>は<b>どこ</b>ですか。<br>
    Sinf qayerda?</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">JAVOB</p>
    <p><ruby>教室<rt>きょうしつ</rt></ruby>は<b>あそこ</b>です。<br>
    Sinf u yerda.</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Soʻroq soʻzini javob bilan almashtiring — gap tayyor.</b> どこ oʻrniga
  あそこ qoʻydingiz, boshqa hech narsa oʻzgarmadi. Ingliz tilida savol berish
  uchun gapni butunlay qayta qurish kerak; yaponchada esa <em>bitta soʻz</em>
  almashadi. Oʻzbekchada ham shunday: «Sinf <em>qayerda</em>?» → «Sinf
  <em>u yerda</em>».</p>
</div>

<h3>4. Soʻroq soʻzi bilan doim が</h3>

<p>PJ-14 dagi qoidani yana bir marta mustahkamlaymiz, chunki u bu yerda
<b>hamma</b> soʻroq soʻziga tegishli.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>何<rt>なに</rt></ruby>が<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にありますか。</p>
  <p class="pe-ex__rom">nani ga tsukue no ue ni arimasu ka</p>
  <p class="pe-ex__uz">Stol ustida nima bor?</p>
  <p class="pe-ex__why">が dan oldin turgani uchun <b>なに</b> oʻqiladi. Va は emas, が — chunki soʻroq soʻzi hech qachon mavzu boʻla olmaydi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Lekin diqqat:</b> soʻroq soʻzi gapning <em>kesim</em> qismida boʻlsa,
  mavzu odatdagidek <b>は</b> oladi:
  «<ruby>教室<rt>きょうしつ</rt></ruby><b>は</b>どこですか» — bu yerda «sinf»
  maʼlum, «qayer» esa nomaʼlum. Qoida buzilmadi: <b>soʻroq soʻzining oʻzi</b>
  は olmaydi, gapning boshqa qismi esa bemalol oladi.</p>
</div>

<h3>5. «Nechta?» — <ruby>何<rt>なん</rt></ruby> va sanoq soʻzlari</h3>

<p>PJ-12 da sanoq soʻzlari haqida ogohlantirgan edim. Ular soʻroq bilan ham
birikadi va bu birikma har kuni kerak boʻladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Savol</th><th>Oʻqilishi</th><th>Nimani sanaydi</th></tr>
  <tr><td><ruby>何人<rt>なんにん</rt></ruby></td><td class="pj-res">nannin</td>
      <td class="pj-uz">necha kishi</td></tr>
  <tr><td><ruby>何時<rt>なんじ</rt></ruby></td><td class="pj-res">nanji</td>
      <td class="pj-uz">soat necha</td></tr>
  <tr><td><ruby>何月<rt>なんがつ</rt></ruby></td><td class="pj-res">nangatsu</td>
      <td class="pj-uz">qaysi oy</td></tr>
  <tr><td><ruby>何歳<rt>なんさい</rt></ruby></td><td class="pj-res">nansai</td>
      <td class="pj-uz">necha yosh</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Hammasi <b>なん</b> bilan — sanoq soʻzi doim なん ni talab qiladi.
  Bu qoidaning eng foydali tomoni shu: <ruby>何<rt>なん</rt></ruby> dan keyin
  nima kelishini bilmasangiz ham, sanoq soʻzi koʻrsangiz oʻqilishi
  <b>なん</b> ekaniga ishonch hosil qilishingiz mumkin.</p>
</div>

<h3>6. どう va boshqa foydali savollar</h3>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>日本語<rt>にほんご</rt></ruby>はどうですか。</p>
  <p class="pe-ex__rom">nihongo wa dō desu ka</p>
  <p class="pe-ex__uz">Yapon tili qanday? (yoqyaptimi?)</p>
  <p class="pe-ex__why">どう — «qanday, qay ahvolda». Bu savol fikr soʻraydi va yaponlar uni juda koʻp ishlatadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">お<ruby>国<rt>くに</rt></ruby>はどちらですか。</p>
  <p class="pe-ex__rom">okuni wa dochira desu ka</p>
  <p class="pe-ex__uz">Qayerdansiz? (qaysi mamlakatdan)</p>
  <p class="pe-ex__why">Boshidagi <b>お</b> — hurmat belgisi, boshqa odamning narsasi haqida gapirganda qoʻshiladi. どちら bu yerda どこ ning muloyim shakli.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ これは<ruby>何<rt>なに</rt></ruby>ですか</p>
  <p class="pe-fix__good">✓ これは<ruby>何<rt>なん</rt></ruby>ですか — です dan oldin doim <b>なん</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>何<rt>なん</rt></ruby>がありますか</p>
  <p class="pe-fix__good">✓ <ruby>何<rt>なに</rt></ruby>がありますか — が dan oldin <b>なに</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ どこは<ruby>教室<rt>きょうしつ</rt></ruby>ですか</p>
  <p class="pe-fix__good">✓ <ruby>教室<rt>きょうしつ</rt></ruby>はどこですか — soʻroq soʻzi javob turadigan joyda turadi, gap boshiga koʻchmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. これは<ruby>何<rt>?</rt></ruby>ですか — なに yoki なん?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>なん</b>. です dan oldin doim なん — «なんです» tilga yengilroq tushadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>何<rt>?</rt></ruby>がありますか — qaysi oʻqilish?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>なに</b>. が dan oldin なに ishlatiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Soʻroq soʻzi gapning qayerida turadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Javob turadigan joyda.</b> Gapni qayta qurish kerak emas — soʻroq soʻzini javob bilan almashtirsangiz, gap tayyor.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Nega «<ruby>教室<rt>きょうしつ</rt></ruby>はどこですか» da は ishlatilgan?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Qoida <b>soʻroq soʻzining oʻziga</b> tegishli: どこ は olmaydi. Sinf esa maʼlum narsa, shuning uchun u bemalol は oladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Soʻroq soʻzlarining qaysi qismi ko-so-a-do jadvalidan keladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ど</b> bilan boshlanadiganlar: どこ, どれ, どの, どちら, どう. Ular PJ-15 dagi jadvalning oxirgi qatori.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>何<rt>なに</rt></ruby> / <ruby>何<rt>なん</rt></ruby></b> — nima</li>
  <li><b><ruby>誰<rt>だれ</rt></ruby></b> — kim</li>
  <li><b>どこ</b> — qayer</li>
  <li><b>いつ</b> — qachon</li>
  <li><b>どう</b> — qanday</li>
  <li><b>いくら</b> — qancha (narx)</li>
  <li><b>どちら</b> — qayer (muloyim)</li>
  <li><b><ruby>国<rt>くに</rt></ruby></b> — mamlakat</li>
  <li><b><ruby>試験<rt>しけん</rt></ruby></b> — imtihon</li>
  <li><b>お</b> — hurmat belgisi (boshqaning narsasi)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Soʻroq soʻzlarining yarmi ko-so-a-do jadvalining <b>ど</b> ustuni — ularni allaqachon bilasiz.</li>
    <li><b>なん</b> です・の va sanoq soʻzlaridan oldin, <b>なに</b> が・を dan oldin.</li>
    <li>Soʻroq soʻzi <b>javob turadigan joyda</b> turadi va <b>は olmaydi</b>.</li>
  </ul>
</div>
""",
    },
]
