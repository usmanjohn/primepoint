# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-85, PJ-86, PJ-87: vaqt oynasi, birga oʻzgarish, vosita.

Blok F davom etadi. Uchala dars ham **otdan yasalgan qolip** — bu Blok F
ning oʻz uslubi: yozma yapon tili grammatikani otga oʻrab ishlatadi.
    PJ-85 — うち va あいだ: ikkala soʻz ham «oraliq» degan ot, lekin
            ular ikki xil oynadan qaraydi. あいだに — chegarasi aniq
            muddat; うちに — oʻzgarib ketadigan holat, «kech
            boʻlmasdan oldin».
    PJ-86 — につれて / にしたがって: ikki narsa **birga** oʻzgaradi.
            Oʻzbekchada «…gan sari» — deyarli bir xil mexanizm.
    PJ-87 — によって: bitta qolip, toʻrtta ish (passivdagi bajaruvchi,
            sabab, vosita, «…ga qarab farq qiladi»). Va yozma
            passivning oʻzi.

⚠️ PJ-85 ning eng katta tuzogʻi — **あいだ va あいだに** orasidagi farq:
に BOR boʻlsa, ish oraliqning ichidagi bitta nuqtada boʻladi; に YOʻQ
boʻlsa, ish butun oraliq davomida davom etadi. Bitta harf, ikki maʼno.

⚠️ PJ-86 da ikkala tomon ham **oʻzgarish** boʻlishi shart. Bir martalik
voqeaga につれて tushmaydi: ✗ ベルが<ruby>鳴</ruby>るにつれて、みんな
<ruby>立</ruby>った.

⚠️ PJ-87 da に va によって ni adashtirmaslik kerak: <ruby>先生</ruby>に
<ruby>叱</ruby>られた (shaxsiy, aziyat) ≠ によって<ruby>書</ruby>かれた
(yaratish, rasmiy). Dars ikkalasini yonma-yon qoʻyadi.

⚠️ Kursda hech qachon berilmagan ikki shakl bu batchda ham yoʻq:
意向形 (行こう / 〜ようと思う) va 〜んです. Gate ikkalasini ham
mexanik tekshiradi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_85_87.py --author=prime
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
        "title": "PJ-85: 〜うちに va 〜あいだに",
        "category": "japanese",
        "order": 85,
        "summary": (
            "Ikki xil vaqt oynasi: あいだに — chegarasi aniq muddatning "
            "ichidagi bir nuqta; うちに — oʻzgarib ketadigan holat, "
            "«kech boʻlmasdan oldin». Va に boʻlgani bilan boʻlmagani "
            "orasidagi farq."
        ),
        "stories": ["あかるいうちに"],
        "content": """
<h2>PJ-85: 〜うちに va 〜あいだに</h2>

<p>Onasi ムニラ ga ikki gap aytdi. Ular deyarli bir xil koʻrinadi:</p>

<p><ruby>私<rt>わたし</rt></ruby>がいない<b>あいだに</b>、<ruby>掃除<rt>そうじ</rt></ruby>をしておいてね。</p>

<p><ruby>温<rt>あたた</rt></ruby>かい<b>うちに</b>、<ruby>食<rt>た</rt></ruby>べてね。</p>

<p>Ikkalasi ham oʻzbekchada «…ekan», «…gunicha» bilan tarjima
qilinadi. Lekin yapon tili ularni har xil eshitadi. Birinchisida —
<em>chegarasi aniq muddat</em>: ona chiqdi, ona qaytadi, oʻrtasida
vaqt bor. Ikkinchisida — <em>oʻzgarib ketadigan holat</em>: ovqat
sovuydi, va shu sovuguncha ulgurish kerak.</p>

<p>Farqni bitta savol hal qiladi: <b>bu oyna oʻz-oʻzidan yopiladimi,
yoki soat boʻyicha yopiladimi?</b></p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>あいだ</b> va <b>あいだに</b> orasidagi farqni bilasiz</li>
    <li><b>うちに</b> bilan «kech boʻlmasdan» degan maʼnoni berasiz</li>
    <li><b>〜ないうちに</b> bilan «… boʻlmasdan oldin» deysiz</li>
    <li>ikkala otga soʻzlarni toʻgʻri ulaysiz (な-sifat <b>な</b>, ot <b>の</b>)</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Chegarasi aniq muddat</span>
  <span class="pe-chip pe-chip--adv">boshi va oxiri bor oraliq</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">あいだに</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">shu oraliqda bir payt</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻzgarib ketadigan holat</span>
  <span class="pe-chip pe-chip--adv">hozircha davom etayotgan holat</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">うちに</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">kech boʻlmasdan</span>
</div>

<h3>1. あいだ — に bor-yoʻqligi hamma narsani hal qiladi</h3>

<p>Avval eng oson va eng koʻp adashtiradigan joyni yopamiz.
<b><ruby>間<rt>あいだ</rt></ruby></b> — «oraliq» degan ot. Undan
keyin <b>に</b> qoʻyilsa yoki qoʻyilmasa, gap butunlay
oʻzgaradi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">あいだ — butun oraliq</p>
    <p><ruby>寝<rt>ね</rt></ruby>ているあいだ、ずっと<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っていた。</p>
    <p>Men uxlab yotganimda, tinimsiz yomgʻir yogʻdi. Ish oraliqning
    <b>boshidan oxirigacha</b> davom etdi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">あいだに — oraliq ichidagi bir nuqta</p>
    <p><ruby>寝<rt>ね</rt></ruby>ているあいだに、<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した。</p>
    <p>Men uxlab yotganimda yomgʻir yogʻa boshladi. Ish oraliqning
    <b>bir joyida</b> boʻlib oʻtdi.</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Qoidani feʼl aytib beradi.</b> Oxirgi feʼl davom etadigan
  ish boʻlsa (ずっと〜ていた, <ruby>待<rt>ま</rt></ruby>っていた,
  <ruby>働<rt>はたら</rt></ruby>いていた) — <b>あいだ</b>. Bir
  martalik, tugaydigan ish boʻlsa (<ruby>来<rt>き</rt></ruby>た,
  <ruby>電話<rt>でんわ</rt></ruby>した,
  <ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した) —
  <b>あいだに</b>. に oʻsha bir nuqtani belgilaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>夏休<rt>なつやす</rt></ruby>みの<span class="pe-hl pe-hl--adv">あいだに</span>、<ruby>運転<rt>うんてん</rt></ruby>を<ruby>習<rt>なら</rt></ruby>いたい。</p>
  <p class="pe-ex__uz">Yozgi taʼtil davomida haydashni oʻrganmoqchiman.</p>
  <p class="pe-ex__why">Taʼtilning boshi ham, oxiri ham aniq — kalendarda turibdi. Shuning uchun bu yerda うち emas, <b>あいだ</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu farqni biz qoʻshimcha bilan emas, soʻz
  bilan koʻrsatamiz.</b> «Men uxlab yotganim<em>da</em> yomgʻir
  yogʻa boshladi» — bitta nuqta. «Men uxlab yotganim
  <em>davomida</em> tinimsiz yomgʻir yogʻdi» — butun oraliq.
  Koʻrdingizmi: oʻzbekchada «davomida» degan qoʻshimcha soʻz
  qoʻshildi. Yapon tilida esa aksincha — <b>に</b> qoʻshilsa
  <em>nuqta</em>, qoʻshilmasa <em>oraliq</em> boʻladi. Ikki til
  bir xil farqni koʻradi, faqat belgini teskari tomonga
  qoʻyadi. Shuning uchun bu joyda oʻzbekchadan
  toʻgʻridan-toʻgʻri koʻchirmang: avval «bitta nuqtami yoki butun
  oraliqmi?» deb hal qiling, keyin に ni qoʻying yoki
  qoʻymang.</p>
</div>

<h3>2. うちに — oyna oʻz-oʻzidan yopiladi</h3>

<p><b>うち</b> ham «ichkari, oraliq» degan ot, lekin u boshqa turdagi
oraliqni koʻrsatadi: <b>uzoq davom etmaydigan holat</b>. Ovqat
sovuydi, kun qorayadi, yoshlik oʻtadi. Shuning uchun うちに ning
ichida doim bir oz shoshilish bor — «kech boʻlmasdan».</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--adv"><ruby>若<rt>わか</rt></ruby>いうちに</span>、いろいろな<ruby>国<rt>くに</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったほうがいい。</p>
  <p class="pe-ex__uz">Yosh ekaningizda turli mamlakatlarga borgan maʼqul.</p>
  <p class="pe-ex__why">Yoshlik — kalendarda chegarasi yoʻq, lekin u albatta tugaydi. Aynan shunday holatlar <b>うちに</b> ni chaqiradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>熱<rt>あつ</rt></ruby>い<span class="pe-hl pe-hl--adv">うちに</span><ruby>食<rt>た</rt></ruby>べてください。</p>
  <p class="pe-ex__uz">Issiqligida yeng.</p>
  <p class="pe-ex__why">Oʻzbekcha «issiq<b>ligida</b>» — aynan shu qolipning oʻzi: holat davom etayotgan payt, va u uzoq turmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tili bu darsda deyarli tayyor javob beradi.</b>
  «Issiq<em>ligida</em> yeng», «yosh <em>ekaningizda</em> oʻrganing»,
  «yorugʻ<em>ida</em> qaytaylik» — bu gaplarning hammasida oʻzbekcha
  qoʻshimcha <b>holat davom etayotganini</b> va u tugashini
  bildiradi. Yaponcha <b>うちに</b> ham shu. Endi solishtiring:
  «taʼtil <em>davomida</em>», «dars <em>paytida</em>» —
  bu yerda chegara aniq, kalendar bor, shoshilish yoʻq.
  Bu — <b>あいだに</b>. Demak tanlash uchun lugʻat ochish shart emas:
  oʻzbekcha gapni ovoz chiqarib ayting va qaysi qoʻshimcha
  chiqqanini eshiting.</p>
</div>

<h3>3. 〜ないうちに — «… boʻlmasdan oldin»</h3>

<p>うちに ning eng koʻp ishlatiladigan shakli — inkor bilan. Maʼnosi
oddiy: <b>hodisa sodir boʻlgunga qadar</b>.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>雨<rt>あめ</rt></ruby></span>
  <span class="pj-joshi__p">が<small>EGA</small></span>
  <span class="pj-joshi__n"><ruby>降<rt>ふ</rt></ruby>らない<b>うちに</b></span>
  <span class="pj-joshi__v"><ruby>帰<rt>かえ</rt></ruby>りましょう</span>
  <span class="pj-joshi__uz">Yomgʻir yogʻmasdan qaytaylik — oʻzbekchada ham inkor turadi.</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--neg"><ruby>忘<rt>わす</rt></ruby>れないうちに</span>、<ruby>書<rt>か</rt></ruby>いておきます。</p>
  <p class="pe-ex__uz">Unutmasdan yozib qoʻyaman.</p>
  <p class="pe-ex__why">Oʻzbekcha «unut<b>masdan</b>» va yaponcha <b><ruby>忘<rt>わす</rt></ruby>れない</b> — ikkalasi ham inkor. Bu qolipda tarjima soʻzma-soʻz ishlaydi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Inkor い-sifatnikidek yasalmaydi.</b> «Sovumasdan oldin»
  degani uchun <ruby>冷<rt>さ</rt></ruby>め<b>ない</b>うちに
  deyiladi — feʼlning ない-shakli (PJ-34). Sifat bilan esa
  <ruby>暗<rt>くら</rt></ruby>く<b>ならない</b>うちに — yaʼni
  sifat avval feʼlga aylanadi (〜くなる), keyin inkor qilinadi.
  «<ruby>暗<rt>くら</rt></ruby>くないうちに» degan gap yaponchada
  yoʻq.</p>
</div>

<h3>4. Ikkala otga nima ulanadi</h3>

<p>うち ham, あいだ ham <b>ot</b>. Shuning uchun ularning oldiga
otni aniqlaydigan shakl tushadi — bu PJ-48 dagi aniqlovchi ergash
gapning oʻzi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Nima ulanadi</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">feʼl (davom etayotgan)</td><td class="pj-end">〜ている + うちに / あいだに</td>
      <td class="pj-res"><ruby>話<rt>はな</rt></ruby>しているうちに</td>
      <td class="pj-uz">gaplashib turganda</td></tr>
  <tr><td class="pj-stem">feʼl (inkor)</td><td class="pj-end">ない-shakli + うちに</td>
      <td class="pj-res"><ruby>暗<rt>くら</rt></ruby>くならないうちに</td>
      <td class="pj-uz">qorongʻi tushmasdan</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">yalangʻoch</td>
      <td class="pj-res"><ruby>熱<rt>あつ</rt></ruby>いうちに</td>
      <td class="pj-uz">issiqligida</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">な</td>
      <td class="pj-res"><ruby>元気<rt>げんき</rt></ruby>なうちに</td>
      <td class="pj-uz">sogʻ-salomat ekan</td></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-end">の</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>のうちに</td>
      <td class="pj-uz">talabalik paytida</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bu jadval tanish boʻlishi kerak.</b> な-sifat <b>な</b>,
  ot <b>の</b> — aynan shu ulanish PJ-81 dagi <b>はず</b> da ham
  turadi (<ruby>学生<rt>がくせい</rt></ruby>のはずです). Blok F
  ning qoliplari koʻpincha ot boʻlgani uchun, bu ikki qoʻshimcha
  qayta-qayta uchraydi. Bir marta yodda saqlang — keyingi
  oʻn darsda foydasi tegadi.</p>
</div>

<h3>5. Kutilmagan oʻzgarish: 〜ているうちに</h3>

<p>うちに ning yana bir ishi bor, va u imtihonda tez-tez soʻraladi.
<b>〜ているうちに</b> — «bir ish qilib turganda, sezmay turib
boshqa narsa oʻzgarib qoldi».</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>音楽<rt>おんがく</rt></ruby>を<span class="pe-hl pe-hl--adv"><ruby>聞<rt>き</rt></ruby>いているうちに</span>、<ruby>眠<rt>ねむ</rt></ruby>くなってきた。</p>
  <p class="pe-ex__uz">Musiqa tinglab oʻtirib, uyqum kela boshladi.</p>
  <p class="pe-ex__why">Hech kim buni rejalashtirmagan — oʻzgarish oʻz-oʻzidan yuz berdi. Shuning uchun keyingi gapda koʻpincha <b>〜てくる</b> yoki <b>〜なる</b> turadi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu «…b oʻtirib» degan qolip.</b> «Kitob
  oʻqi<em>b oʻtirib</em>, uxlab qolibman», «gaplash<em>ib
  oʻtirib</em>, poyezdni oʻtkazib yuboribmiz». Ikkala tilda ham
  gapning ichida bitta xabar bor: <em>men buni sezmadim</em>.
  Aynan shuning uchun yaponcha bunday gaplarda oxirida
  <b>〜てしまった</b> (PJ-58) ham juda tez-tez keladi —
  ikkisi bir-birini quvvatlaydi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">間</span>
    <span class="pj-kanji__uz">oraliq, orasi, vaqt</span>
    <span class="pj-kanji__on">オン: カン・ケン</span>
    <span class="pj-kanji__kun">KUN: あいだ・ま</span>
    <span class="pj-kanji__note">時間 (じかん) — vaqt · 人間 (にんげん) — inson · 間に合う (まにあう) — ulgurmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">若</span>
    <span class="pj-kanji__uz">yosh</span>
    <span class="pj-kanji__on">オン: ジャク</span>
    <span class="pj-kanji__kun">KUN: わか(い)</span>
    <span class="pj-kanji__note">若者 (わかもの) — yoshlar · 若いうちに — yosh ekan</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">冷</span>
    <span class="pj-kanji__uz">sovuq, sovumoq</span>
    <span class="pj-kanji__on">オン: レイ</span>
    <span class="pj-kanji__kun">KUN: つめ(たい)・さ(める)</span>
    <span class="pj-kanji__note">冷蔵庫 (れいぞうこ) — muzlatgich · 冷たい水 — sovuq suv</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>うちに<ruby>旅行<rt>りょこう</rt></ruby>したい</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>の</b>うちに — うち ot, ot oldidan の oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>元気<rt>げんき</rt></ruby>うちに<ruby>山<rt>やま</rt></ruby>に<ruby>登<rt>のぼ</rt></ruby>りたい</p>
  <p class="pe-fix__good">✓ <ruby>元気<rt>げんき</rt></ruby><b>な</b>うちに — な-sifat な ni saqlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>暗<rt>くら</rt></ruby>くないうちに<ruby>帰<rt>かえ</rt></ruby>ります</p>
  <p class="pe-fix__good">✓ <ruby>暗<rt>くら</rt></ruby>く<b>ならない</b>うちに — sifat avval feʼlga aylanadi (〜くなる), keyin inkor qilinadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>寝<rt>ね</rt></ruby>ているあいだ、<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した</p>
  <p class="pe-fix__good">✓ <ruby>寝<rt>ね</rt></ruby>ているあいだ<b>に</b> — bir martalik ish oraliqning bir nuqtasida boʻladi, demak に kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>夏休<rt>なつやす</rt></ruby>みのうちに<ruby>運転<rt>うんてん</rt></ruby>を<ruby>習<rt>なら</rt></ruby>いたい</p>
  <p class="pe-fix__good">✓ <ruby>夏休<rt>なつやす</rt></ruby>みの<b>あいだに</b> — chegarasi kalendarda aniq muddat; うち oʻzgarib ketadigan holat uchun.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Men uxlab yotganimda yomgʻir yogʻa boshladi» — あいだ yoki あいだに?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>あいだに</b>: <ruby>寝<rt>ね</rt></ruby>ているあいだに、<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した. Yogʻa boshlash — bir martalik ish, u oraliqning bitta nuqtasida boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Boʻsh joyni toʻldiring: <ruby>学生<rt>がくせい</rt></ruby>___うちに、たくさん<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みたい。</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>の</b> — <ruby>学生<rt>がくせい</rt></ruby>のうちに. うち ot boʻlgani uchun ot oldidan の oladi, xuddi はず dagidek.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Qorongʻi tushmasdan qaytaylik» — yaponchada boʻsh joyga nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>暗<rt>くら</rt></ruby>くならないうちに</b><ruby>帰<rt>かえ</rt></ruby>りましょう. Sifat avval <ruby>暗<rt>くら</rt></ruby>くなる feʼliga aylanadi, keyin ない-shakliga oʻtadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Yozgi taʼtil davomida haydashni oʻrganmoqchiman» — うちに yoki あいだに?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>あいだに</b>: <ruby>夏休<rt>なつやす</rt></ruby>みのあいだに. Taʼtilning boshi ham, oxiri ham kalendarda aniq — bu oyna soat boʻyicha yopiladi, oʻz-oʻzidan emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いているうちに、… — bu qolip nimani qoʻshadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Sezilmagan oʻzgarish.</b> Ish qilib turganda boshqa narsa oʻz-oʻzidan oʻzgardi: <ruby>眠<rt>ねむ</rt></ruby>くなってきた. Shuning uchun keyingi gapda koʻpincha なる yoki 〜てくる turadi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜あいだ</b> — … davomida (butun oraliq)</li>
  <li><b>〜あいだに</b> — … davomida bir payt</li>
  <li><b>〜うちに</b> — … ekan, kech boʻlmasdan</li>
  <li><b>〜ないうちに</b> — … boʻlmasdan oldin</li>
  <li><b>〜ているうちに</b> — … qilib turib (sezilmagan oʻzgarish)</li>
  <li><b><ruby>若<rt>わか</rt></ruby>い</b> — yosh</li>
  <li><b><ruby>冷<rt>さ</rt></ruby>める</b> — sovumoq</li>
  <li><b><ruby>暗<rt>くら</rt></ruby>い</b> — qorongʻi</li>
  <li><b><ruby>眠<rt>ねむ</rt></ruby>い</b> — uyqusi kelgan</li>
  <li><b><ruby>留守<rt>るす</rt></ruby></b> — uyda yoʻq, gʻoyib</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>あいだ</b> — butun oraliq; <b>あいだに</b> — oraliqdagi bir nuqta.</li>
    <li><b>うちに</b> — oyna oʻz-oʻzidan yopiladi: «kech boʻlmasdan».</li>
    <li>Ikkalasi ham <b>ot</b>: な-sifat <b>な</b>, ot <b>の</b> oladi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-86: 〜につれて, 〜にしたがって — birga oʻzgarish",
        "category": "japanese",
        "order": 86,
        "summary": (
            "Ikki narsa birga oʻzgaradi: biri ortgan sari, ikkinchisi "
            "ham oʻzgaradi. につれて — tabiiy, sekin-asta; にしたがって "
            "— shu maʼnoda ham, «koʻrsatmaga muvofiq» maʼnosida ham."
        ),
        "stories": ["さくらが きたへ すすむ"],
        "content": """
<h2>PJ-86: 〜につれて, 〜にしたがって — birga oʻzgarish</h2>

<p>イノム tabiat haqidagi kitobda shunday gapga duch keldi:</p>

<p><ruby>山<rt>やま</rt></ruby>を<ruby>登<rt>のぼ</rt></ruby>る<b>につれて</b>、<ruby>空気<rt>くうき</rt></ruby>が<ruby>薄<rt>うす</rt></ruby>くなる。</p>

<p>Gapning maʼnosi bitta rasmda koʻrinadi: bir tomonda —
<em>yuqoriga koʻtarilish</em>, ikkinchi tomonda —
<em>havoning siyraklashishi</em>. Ikkalasi <b>birga</b>
oʻzgaryapti: qanchalik yuqori koʻtarilsangiz, shunchalik havo
siyraklashadi.</p>

<p>Bu dars aynan shu bogʻlanish haqida. Uni yapon tilida bitta
qolip bilan aytish mumkin, va oʻzbek tilida ham bitta qolip bilan
— <b>«…gan sari»</b>. Ikkovi shu qadar bir xil ishlaydiki, bu
darsni yodlash deyarli shart emas.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>〜につれて</b> bilan «…gan sari» degan maʼnoni berasiz</li>
    <li><b>〜にしたがって</b> ni ikkala vazifasida ishlatasiz</li>
    <li>ikkala qolip ham nimaga ulanishini bilasiz</li>
    <li>bu qoliplar <b>qaysi gapga tushmasligini</b> taniysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Birga oʻzgarish</span>
  <span class="pe-chip pe-chip--s">A oʻzgaradi</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">につれて</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">B ham oʻzgaradi</span>
</div>

<h3>1. Qolip nimaga ulanadi</h3>

<p>Ulanish juda sodda va ikkala qolip uchun bir xil:
<b><ruby>辞書形<rt>じしょけい</rt></ruby></b> yoki <b>ot</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Nima ulanadi</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">feʼl</td><td class="pj-end"><ruby>辞書形<rt>じしょけい</rt></ruby> + につれて</td>
      <td class="pj-res"><ruby>年<rt>とし</rt></ruby>をとるにつれて</td>
      <td class="pj-uz">yoshi ulgʻaygan sari</td></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-end">ot + につれて</td>
      <td class="pj-res"><ruby>時間<rt>じかん</rt></ruby>の<ruby>経過<rt>けいか</rt></ruby>につれて</td>
      <td class="pj-uz">vaqt oʻtgan sari</td></tr>
  <tr><td class="pj-stem">feʼl</td><td class="pj-end"><ruby>辞書形<rt>じしょけい</rt></ruby> + にしたがって</td>
      <td class="pj-res"><ruby>暖<rt>あたた</rt></ruby>かくなるにしたがって</td>
      <td class="pj-uz">havo isigan sari</td></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-end">ot + にしたがって</td>
      <td class="pj-res"><ruby>説明書<rt>せつめいしょ</rt></ruby>にしたがって</td>
      <td class="pj-uz">qoʻllanmaga muvofiq</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>ます-shakli bu yerga tushmaydi.</b> «<ruby>年<rt>とし</rt></ruby>を
  とりますにつれて» degan gap yoʻq — qolip <b>lugʻat shakliga</b>
  ulanadi. Oʻtgan zamon ham tushmaydi:
  «とったにつれて» notoʻgʻri. Sabab oddiy — bu qolip <em>hozir
  davom etayotgan oʻzgarish</em> haqida, shuning uchun feʼl ham
  oʻzining eng neytral shaklida turadi.</p>
</div>

<h3>2. 〜につれて — tabiiy, sekin-asta</h3>

<p>につれて eng koʻp ishlatiladigani, va uning ohangi doim bir xil:
<b>oʻzgarish oʻz-oʻzidan, sekin va bir tekis boradi</b>. Hech kim
uni boshqarmaydi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s"><ruby>年<rt>とし</rt></ruby>をとるにつれて</span>、<ruby>時間<rt>じかん</rt></ruby>が<ruby>早<rt>はや</rt></ruby>く<ruby>感<rt>かん</rt></ruby>じられるようになる。</p>
  <p class="pe-ex__uz">Yosh ulgʻaygan sari vaqt tezroq oʻtayotgandek tuyuladi.</p>
  <p class="pe-ex__why">Ikkala tomon ham asta-sekin oʻzgaradi. Shuning uchun keyingi gapda koʻpincha 〜なる, 〜てくる, 〜ようになる turadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s"><ruby>都会<rt>とかい</rt></ruby>が<ruby>大<rt>おお</rt></ruby>きくなるにつれて</span>、<ruby>空気<rt>くうき</rt></ruby>が<ruby>悪<rt>わる</rt></ruby>くなってきた。</p>
  <p class="pe-ex__uz">Shahar kattalashgan sari havo yomonlashib ketdi.</p>
  <p class="pe-ex__why">Bu yerda ikkala tomon ham sifatdan yasalgan feʼl (<ruby>大<rt>おお</rt></ruby>きくなる, <ruby>悪<rt>わる</rt></ruby>くなる) — oʻzgarish qoliplarining eng tabiiy jufti.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu darsda oʻzbek tili shunchaki tarjimon emas —
  u qolipning oʻzi.</b> «Yosh ulgʻay<em>gan sari</em> vaqt
  tezlashadi», «shahar kattalash<em>gan sari</em> havo
  yomonlashadi», «yuqoriga chiq<em>qan sari</em> havo
  siyraklashadi». Uchala gapda ham oʻzbekcha
  <b>«…gan sari»</b> turibdi va u aynan
  <b>につれて</b> ning oʻrnini egallaydi — gapning oʻrtasida,
  birinchi oʻzgarishdan keyin. Demak tarjima qilayotganda
  yaponcha gapni boshdan tuzish shart emas: oʻzbekcha gapni
  ayting, «…gan sari» qayerda turganini koʻring, va oʻsha joyga
  につれて ni qoʻying. Aksi ham ishlaydi — matnda につれて ni
  koʻrsangiz, ichingizda «…gan sari» deb oʻqing.</p>
</div>

<h3>3. 〜にしたがって — ikkita ishi bor</h3>

<p>にしたがって <b>birinchi vazifasida</b> につれて bilan deyarli
bir xil: ikki narsa birga oʻzgaradi. Lekin unda ikkinchi, butunlay
boshqa vazifa ham bor — va u <ruby>従<rt>したが</rt></ruby>う
(«ergashmoq, boʻysunmoq») degan feʼldan kelib chiqadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">1 — birga oʻzgarish</p>
    <p><ruby>北<rt>きた</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くにしたがって、<ruby>寒<rt>さむ</rt></ruby>くなる。</p>
    <p>Shimolga borgan sari sovuq boʻladi. Bu yerda につれて ham
    boʻlaveradi — maʼno bir xil.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">2 — muvofiq, ergashib</p>
    <p><ruby>説明書<rt>せつめいしょ</rt></ruby>にしたがって<ruby>組<rt>く</rt></ruby>み<ruby>立<rt>た</rt></ruby>ててください。</p>
    <p>Qoʻllanmaga muvofiq yigʻing. Bu yerda につれて <b>umuman</b>
    boʻlmaydi — qoʻllanma oʻzgarayotgani yoʻq.</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Ikkinchi vazifani tanish oson.</b> にしたがって oldida
  <em>oʻzgarmaydigan</em> ot tursa — qoida, koʻrsatma, qonun,
  buyruq, anʼana — demak maʼnosi «…ga muvofiq»:
  <ruby>規則<rt>きそく</rt></ruby>にしたがって,
  <ruby>指示<rt>しじ</rt></ruby>にしたがって,
  <ruby>習慣<rt>しゅうかん</rt></ruby>にしたがって. Oldida
  oʻzgarishni bildiradigan feʼl tursa — maʼnosi «…gan sari».</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--adv"><ruby>係<rt>かかり</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>の<ruby>指示<rt>しじ</rt></ruby>にしたがって</span>、ゆっくり<ruby>外<rt>そと</rt></ruby>へ<ruby>出<rt>で</rt></ruby>てください。</p>
  <p class="pe-ex__uz">Navbatchi xodimning koʻrsatmasiga muvofiq, sekin tashqariga chiqing.</p>
  <p class="pe-ex__why">Bu yaponcha eʼlonlarning odatiy tili — vokzalda, maktabda, samolyotda shu gapni eshitasiz.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham bitta soʻz ikkala ishni qiladi.</b>
  «Ergashmoq» ni oʻylang: «orqasidan <em>ergashdi</em>» —
  harakat; «qoidaga <em>ergashdi</em>» — rioya qilish. Yaponcha
  <ruby>従<rt>したが</rt></ruby>う ham aynan shunday ikki
  tomonlama soʻz, va にしたがって ning ikki maʼnosi oʻsha
  ikkilikdan kelib chiqqan. Rasmiy oʻzbekchada esa bu maʼno
  uchun «…ga <em>muvofiq</em>», «…ga <em>koʻra</em>»,
  «…ga <em>binoan</em>» degan soʻzlar bor — ularning
  hammasi にしたがって ning tarjimasi boʻla oladi. Qaysi biri
  chiqishini gapning rasmiyligi hal qiladi, yaponchasi esa
  oʻzgarmaydi.</p>
</div>

<h3>4. Ikkalasi qayerda ishlamaydi</h3>

<p>Bitta qoida ikkala qolipni ham boshqaradi, va imtihon savollari
aynan shu yerdan yasaladi: <b>ikkala tomon ham oʻzgarish boʻlishi
shart</b>. Bir martalik, tugaydigan voqea bu qoliplarni
olmaydi.</p>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ベルが<ruby>鳴<rt>な</rt></ruby>るにつれて、みんなが<ruby>立<rt>た</rt></ruby>った</p>
  <p class="pe-fix__good">✓ ベルが<ruby>鳴<rt>な</rt></ruby>ると、みんなが<ruby>立<rt>た</rt></ruby>った — qoʻngʻiroq bir marta jiringlaydi, bu oʻzgarish emas; PJ-51 dagi <b>と</b> kerak.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Ikkinchi chegara — buyruq va iltimos.</b> につれて li gapning
  oxiriga «shunday qiling» degan gap qoʻyilmaydi:
  «<ruby>寒<rt>さむ</rt></ruby>くなるにつれて、コートを
  <ruby>着<rt>き</rt></ruby>てください» notoʻgʻri eshitiladi.
  Sabab oddiy: qolip <em>kuzatilgan oʻzgarish</em> haqida xabar
  beradi, kimgadir buyurmaydi. Buyruq kerak boʻlsa, PJ-50 dagi
  <b>たら</b> ga oʻting:
  <ruby>寒<rt>さむ</rt></ruby>くなったら、コートを<ruby>着<rt>き</rt></ruby>てください.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu chegara oʻzbek tilida ham bor, faqat biz uni
  oʻylab koʻrmaganmiz.</b> «Sovuq boʻl<em>gan sari</em> palto
  kiying» deb aytib koʻring — quloqqa gʻalati tegadi, chunki
  «…gan sari» kuzatishni bildiradi, buyruqni emas. Biz bunday
  paytda «sovuq boʻl<em>sa</em>, palto kiying» deymiz.
  Yaponcha ham aynan shu yoʻldan boradi: kuzatish uchun
  <b>につれて</b>, buyruq yoki maslahat uchun <b>たら</b>.
  Demak bu qoidani yodlash shart emas — oʻzbekcha gapni ovoz
  chiqarib ayting, va gʻalati eshitilsa, yaponchasi ham
  gʻalati boʻladi.</p>
</div>

<h3>5. Uchalasi bitta jadvalda</h3>

<p>Siz endi «bir narsa ikkinchisiga bogʻliq» degan maʼnoni
beradigan uchta qolipni bilasiz. Ular bir-birining oʻrnini
bosmaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Nima haqida</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem">〜につれて</td><td class="pj-uz">birga, sekin-asta oʻzgarish</td>
      <td class="pj-res"><ruby>年<rt>とし</rt></ruby>をとるにつれて</td>
      <td class="pj-end">ulgʻaygan sari</td></tr>
  <tr><td class="pj-stem">〜にしたがって</td><td class="pj-uz">oʻsha maʼno, yoki «…ga muvofiq»</td>
      <td class="pj-res"><ruby>規則<rt>きそく</rt></ruby>にしたがって</td>
      <td class="pj-end">qoidaga muvofiq</td></tr>
  <tr><td class="pj-stem">〜と (PJ-51)</td><td class="pj-uz">har safar shunday boʻladi</td>
      <td class="pj-res"><ruby>春<rt>はる</rt></ruby>になると</td>
      <td class="pj-end">bahor kelsa</td></tr>
  <tr><td class="pj-stem">〜たら (PJ-50)</td><td class="pj-uz">bir martalik shart</td>
      <td class="pj-res"><ruby>寒<rt>さむ</rt></ruby>くなったら</td>
      <td class="pj-end">sovuq boʻlsa</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Yozma til belgisi.</b> につれて va にしたがって —
  maqola, darslik, yangilik va ilmiy matnning soʻzlari.
  Kundalik suhbatda yaponlar buning oʻrniga oddiygina
  <b>〜と</b> yoki <b>だんだん</b> deyishadi:
  <ruby>春<rt>はる</rt></ruby>になると、だんだん<ruby>暖<rt>あたた</rt></ruby>かくなる.
  Shuning uchun bu darsni <em>oʻqish</em> uchun oʻrganing —
  gapirish uchun emas.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">従</span>
    <span class="pj-kanji__uz">ergashmoq, boʻysunmoq</span>
    <span class="pj-kanji__on">オン: ジュウ</span>
    <span class="pj-kanji__kun">KUN: したが(う)</span>
    <span class="pj-kanji__note">従業員 (じゅうぎょういん) — xodim · 規則に従う — qoidaga rioya qilmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">増</span>
    <span class="pj-kanji__uz">koʻpaymoq, ortmoq</span>
    <span class="pj-kanji__on">オン: ゾウ</span>
    <span class="pj-kanji__kun">KUN: ふ(える)・ま(す)</span>
    <span class="pj-kanji__note">増加 (ぞうか) — oʻsish · 人が増える — odam koʻpaymoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">減</span>
    <span class="pj-kanji__uz">kamaymoq</span>
    <span class="pj-kanji__on">オン: ゲン</span>
    <span class="pj-kanji__kun">KUN: へ(る)</span>
    <span class="pj-kanji__note">減少 (げんしょう) — kamayish · 人が減る — odam kamaymoq</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s"><ruby>人口<rt>じんこう</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えるにつれて</span>、<ruby>車<rt>くるま</rt></ruby>の<ruby>数<rt>かず</rt></ruby>も<ruby>増<rt>ふ</rt></ruby>えた。</p>
  <p class="pe-ex__uz">Aholi koʻpaygan sari mashinalar soni ham ortdi.</p>
  <p class="pe-ex__why">Ikkinchi tomonda <b>も</b> turgani bejiz emas: «u ham» degan soʻz ikki oʻzgarishning birga borayotganini kuchaytiradi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>年<rt>とし</rt></ruby>をとりますにつれて</p>
  <p class="pe-fix__good">✓ <ruby>年<rt>とし</rt></ruby>をとるにつれて — qolip lugʻat shakliga ulanadi, ます-shakliga emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>年<rt>とし</rt></ruby>をとったにつれて</p>
  <p class="pe-fix__good">✓ <ruby>年<rt>とし</rt></ruby>をとるにつれて — oʻtgan zamon ham tushmaydi; oʻzgarish hozir davom etyapti.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>説明書<rt>せつめいしょ</rt></ruby>につれて<ruby>組<rt>く</rt></ruby>み<ruby>立<rt>た</rt></ruby>てる</p>
  <p class="pe-fix__good">✓ <ruby>説明書<rt>せつめいしょ</rt></ruby><b>にしたがって</b> — «muvofiq» maʼnosi faqat にしたがって da bor.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>寒<rt>さむ</rt></ruby>くなるにつれて、コートを<ruby>着<rt>き</rt></ruby>てください</p>
  <p class="pe-fix__good">✓ <ruby>寒<rt>さむ</rt></ruby>くなったら、コートを<ruby>着<rt>き</rt></ruby>てください — bu qolipdan keyin iltimos kelmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ドアが<ruby>開<rt>ひら</rt></ruby>くにつれて、<ruby>人<rt>ひと</rt></ruby>が<ruby>入<rt>はい</rt></ruby>ってきた</p>
  <p class="pe-fix__good">✓ ドアが<ruby>開<rt>ひら</rt></ruby>くと、<ruby>人<rt>ひと</rt></ruby>が<ruby>入<rt>はい</rt></ruby>ってきた — bir martalik voqea, oʻzgarish emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Yosh ulgʻaygan sari» — boʻsh joyga nima tushadi? <ruby>年<rt>とし</rt></ruby>を___につれて</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>とる</b> — <ruby>年<rt>とし</rt></ruby>をとるにつれて. Lugʻat shakli; とります ham, とった ham bu yerga tushmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>説明書<rt>せつめいしょ</rt></ruby>___<ruby>組<rt>く</rt></ruby>み<ruby>立<rt>た</rt></ruby>ててください — につれて yoki にしたがって?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>にしたがって</b>. Qoʻllanma oʻzgarayotgani yoʻq — bu «…ga muvofiq» maʼnosi, va u faqat にしたがって da bor.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Nega «ベルが<ruby>鳴<rt>な</rt></ruby>るにつれて、みんなが<ruby>立<rt>た</rt></ruby>った» notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki qoʻngʻiroq <b>bir marta</b> jiringlaydi — bu oʻzgarish emas, voqea. につれて ikkala tomondan ham oʻzgarish talab qiladi. Toʻgʻrisi — ベルが<ruby>鳴<rt>な</rt></ruby>ると.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Sovuq boʻlsa, palto kiying» — につれて ishlatsa boʻladimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> Bu qolipdan keyin iltimos yoki buyruq kelmaydi. Toʻgʻrisi — <ruby>寒<rt>さむ</rt></ruby>くなったら、コートを<ruby>着<rt>き</rt></ruby>てください.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. につれて va にしたがって qaysi maʼnoda bir xil, qaysi maʼnoda emas?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>«…gan sari»</b> maʼnosida ikkalasi ham boʻladi. Lekin <b>«…ga muvofiq»</b> maʼnosi faqat にしたがって da bor: <ruby>規則<rt>きそく</rt></ruby>にしたがって — «qoidaga muvofiq».</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜につれて</b> — … gan sari</li>
  <li><b>〜にしたがって</b> — … gan sari; … ga muvofiq</li>
  <li><b><ruby>増<rt>ふ</rt></ruby>える</b> — koʻpaymoq</li>
  <li><b><ruby>減<rt>へ</rt></ruby>る</b> — kamaymoq</li>
  <li><b><ruby>年<rt>とし</rt></ruby>をとる</b> — yoshi ulgʻaymoq</li>
  <li><b><ruby>指示<rt>しじ</rt></ruby></b> — koʻrsatma</li>
  <li><b><ruby>説明書<rt>せつめいしょ</rt></ruby></b> — qoʻllanma</li>
  <li><b><ruby>空気<rt>くうき</rt></ruby></b> — havo</li>
  <li><b><ruby>人口<rt>じんこう</rt></ruby></b> — aholi soni</li>
  <li><b>だんだん</b> — asta-sekin</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>につれて</b> = oʻzbekcha <b>«…gan sari»</b>, oʻsha joyda turadi.</li>
    <li>Ikkala tomon ham <b>oʻzgarish</b> boʻlishi shart — bir martalik voqea emas.</li>
    <li><b>にしたがって</b> ning ikkinchi ishi bor: «…ga muvofiq».</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-87: 〜によって va passivning yozma ishlatilishi",
        "category": "japanese",
        "order": 87,
        "summary": (
            "Bitta qolip, toʻrtta ish: passivdagi bajaruvchi "
            "(«… tomonidan»), sabab («… tufayli»), vosita («… orqali») "
            "va farqlanish («…ga qarab»). Va nega yozma matnda passiv "
            "shunchalik koʻp."
        ),
        "stories": ["まちの としょかんが ひらいた"],
        "content": """
<h2>PJ-87: 〜によって va passivning yozma ishlatilishi</h2>

<p>ムニラ yaponcha gazetani ochdi va bir sahifada toʻrtta gapga
duch keldi. Toʻrtalasida ham <b>によって</b> turibdi:</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h">1</p>
    <p>この<ruby>橋<rt>はし</rt></ruby>は<ruby>百年前<rt>ひゃくねんまえ</rt></ruby>に<ruby>一人<rt>ひとり</rt></ruby>の<ruby>技師<rt>ぎし</rt></ruby>によって<ruby>作<rt>つく</rt></ruby>られた。</p>
    <p>Bu koʻprik yuz yil oldin bir muhandis <b>tomonidan</b> qurilgan.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">2</p>
    <p><ruby>台風<rt>たいふう</rt></ruby>によって、<ruby>多<rt>おお</rt></ruby>くの<ruby>家<rt>いえ</rt></ruby>が<ruby>壊<rt>こわ</rt></ruby>れた。</p>
    <p>Tayfun <b>tufayli</b> koʻp uy buzildi.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">3</p>
    <p><ruby>問題<rt>もんだい</rt></ruby>は<ruby>話<rt>はな</rt></ruby>し<ruby>合<rt>あ</rt></ruby>いによって<ruby>解決<rt>かいけつ</rt></ruby>した。</p>
    <p>Muammo suhbat <b>orqali</b> hal boʻldi.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">4</p>
    <p><ruby>人<rt>ひと</rt></ruby>によって<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>う。</p>
    <p>Odam<b>ga qarab</b> fikrlash tarzi har xil boʻladi.</p>
  </div>
</div>

<p>Bitta qolip, toʻrtta oʻzbekcha tarjima. Bu yodlash kerak
boʻlgan toʻrtta alohida qoida emas — によって ning ichida bitta
maʼno bor, va toʻrtalasi oʻshanda birlashadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>によって</b> ning toʻrtta vazifasini ajratasiz</li>
    <li>passivda <b>に</b> va <b>によって</b> orasidan toʻgʻrisini tanlaysiz</li>
    <li><b>による + ot</b> shaklini yasaysiz</li>
    <li>yozma matnda passiv nega shunchalik koʻp ekanini bilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta qolip</span>
  <span class="pe-chip pe-chip--o">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">によって</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">shu narsa gapni harakatga keltirdi</span>
</div>

<h3>1. Ichidagi bitta maʼno</h3>

<p>によって — <ruby>因<rt>よ</rt></ruby>る degan feʼldan
(«bogʻliq boʻlmoq, kelib chiqmoq»). Shuning uchun qolipning
maʼnosi har doim bitta: <b>gapda boʻlgan ish mana shu narsadan
kelib chiqdi</b>. «Kim qildi», «nima sabab boʻldi», «nima orqali
boʻldi», «nimaga qarab farq qiladi» — bularning hammasi oʻsha
bitta savolning toʻrt tomoni.</p>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham shunga oʻxshash bitta soʻz bor:
  «koʻra».</b> «Qonun<em>ga koʻra</em>», «hisobot<em>ga
  koʻra</em>», «holat<em>ga koʻra</em>» — hammasida bitta maʼno:
  <em>manba shu</em>. Faqat bizda bu soʻz toʻrt tomonning
  hammasiga yetmaydi, shuning uchun oʻzbekcha tarjimada toʻrt
  xil soʻz chiqadi: <b>tomonidan</b>, <b>tufayli</b>,
  <b>orqali</b>, <b>ga qarab</b>. Yaponcha esa bitta soʻz bilan
  kifoyalanadi. Bu tarjimonning ishini qiyinlashtiradi, lekin
  oʻquvchining ishini osonlashtiradi — yodlash uchun bitta
  qolip, tanlash uchun bitta savol: <em>«gapdagi ish qayerdan
  kelib chiqdi?»</em></p>
</div>

<h3>2. Passivdagi bajaruvchi — «… tomonidan»</h3>

<p>Birinchi va eng muhim vazifasi. PJ-63 da siz passivni
oʻrgangansiz va bajaruvchini <b>に</b> bilan koʻrsatgansiz.
Yozma matnda esa koʻpincha <b>によって</b> turadi — lekin ikkisi
oʻrin almashtira olmaydi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">に — menga taʼsir qildi</p>
    <p><ruby>先生<rt>せんせい</rt></ruby>に<ruby>叱<rt>しか</rt></ruby>られた。</p>
    <p>Ustoz meni urishdi. Gapning markazida — <b>men</b>, va
    men bundan aziyat chekdim (PJ-64).</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">によって — yaratildi, aniqlandi</p>
    <p>『<ruby>坊<rt>ぼっ</rt></ruby>ちゃん』は<ruby>夏目漱石<rt>なつめそうせき</rt></ruby>によって<ruby>書<rt>か</rt></ruby>かれた。</p>
    <p>«Bocchan» Natsume Soseki tomonidan yozilgan. Hech kim
    aziyat chekmadi — bu shunchaki maʼlumot.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu chegara oʻzbek oʻquvchisi uchun koʻrinmaydi, chunki
  biz majhul nisbatni kam ishlatamiz.</b> «Ustoz meni urishdi»
  deymiz — faol gap, ega ustoz. Yaponcha esa oʻsha voqeani
  <em>men</em> tomonidan koʻrsatadi:
  <ruby>先生<rt>せんせい</rt></ruby>に<ruby>叱<rt>しか</rt></ruby>られた.
  Shuning uchun «tomonidan» degan oʻzbekcha soʻzni koʻrsangiz
  ham, uni avtomatik ravishda によって deb tarjima qilmang.
  Bitta savol soʻrang: <em>«bu gapda kimdir aziyat chekyaptimi,
  yoki dunyoda yangi narsa paydo boʻlyaptimi?»</em> Aziyat —
  <b>に</b>. Yaratish, qurish, kashf etish, qaror qilish —
  <b>によって</b>. Oʻzbekcha «tomonidan» ham aslida aynan
  ikkinchi guruhda tabiiy eshitiladi: «koʻprik muhandis
  tomonidan qurilgan» — toʻgʻri; «men ustoz tomonidan
  urishildim» — gʻalati.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Qoida qisqa: yaratish feʼllari によって ni oladi.</b>
  <ruby>作<rt>つく</rt></ruby>る, <ruby>書<rt>か</rt></ruby>く,
  <ruby>建<rt>た</rt></ruby>てる, <ruby>発見<rt>はっけん</rt></ruby>する,
  <ruby>発明<rt>はつめい</rt></ruby>する,
  <ruby>決<rt>き</rt></ruby>める — yaʼni dunyoda yangi narsa
  paydo qilgan yoki bir masalani hal qilgan feʼllar. Qolgan
  hollarda, ayniqsa gap <em>odam haqida</em> va u
  <em>taʼsir koʻrgan</em> boʻlsa — oddiy <b>に</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>寺<rt>てら</rt></ruby>は<span class="pe-hl pe-hl--s"><ruby>八世紀<rt>はちせいき</rt></ruby>に<ruby>建<rt>た</rt></ruby>てられた</span>。</p>
  <p class="pe-ex__uz">Bu ibodatxona sakkizinchi asrda qurilgan.</p>
  <p class="pe-ex__why">Bajaruvchi umuman aytilmagan — chunki u muhim emas. Yozma matnda passivning eng koʻp uchraydigan koʻrinishi aynan shu.</p>
</div>

<h3>3. Sabab va vosita</h3>

<p>Ikkinchi va uchinchi vazifalar bir-biriga yaqin, va ularni
tanish oson: <b>によって</b> oldida odam emas, <em>hodisa</em>
yoki <em>usul</em> turadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oldida nima</th><th>Maʼnosi</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem">odam, tashkilot</td><td class="pj-end">bajaruvchi</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>によって<ruby>作<rt>つく</rt></ruby>られた</td>
      <td class="pj-uz">talabalar tomonidan qilingan</td></tr>
  <tr><td class="pj-stem">tabiiy hodisa</td><td class="pj-end">sabab</td>
      <td class="pj-res"><ruby>地震<rt>じしん</rt></ruby>によって<ruby>壊<rt>こわ</rt></ruby>れた</td>
      <td class="pj-uz">zilzila tufayli buzildi</td></tr>
  <tr><td class="pj-stem">usul, yoʻl</td><td class="pj-end">vosita</td>
      <td class="pj-res"><ruby>実験<rt>じっけん</rt></ruby>によって<ruby>確<rt>たし</rt></ruby>かめる</td>
      <td class="pj-uz">tajriba orqali tekshirmoq</td></tr>
  <tr><td class="pj-stem">oʻzgaruvchi shart</td><td class="pj-end">farqlanish</td>
      <td class="pj-res"><ruby>季節<rt>きせつ</rt></ruby>によって<ruby>違<rt>ちが</rt></ruby>う</td>
      <td class="pj-uz">fasllarga qarab farq qiladi</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--adv"><ruby>大雨<rt>おおあめ</rt></ruby>によって</span>、<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まった。</p>
  <p class="pe-ex__uz">Kuchli yomgʻir tufayli poyezd toʻxtadi.</p>
  <p class="pe-ex__why">Bu yerda PJ-53 dagi <b>ので</b> ham boʻlardi. Farq — ohang: によって yozma va rasmiy, yangiliklar tili.</p>
</div>

<h3>4. «…ga qarab farq qiladi»</h3>

<p>Toʻrtinchi vazifa qolgan uchtasidan sezilarli boshqacha, va
uni tanish oson: gapning oxirida deyarli har doim
<b><ruby>違<rt>ちが</rt></ruby>う</b>,
<b><ruby>変<rt>か</rt></ruby>わる</b> yoki
<b><ruby>決<rt>き</rt></ruby>まる</b> turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s"><ruby>国<rt>くに</rt></ruby>によって</span><ruby>朝<rt>あさ</rt></ruby>ごはんが<ruby>違<rt>ちが</rt></ruby>う。</p>
  <p class="pe-ex__uz">Mamlakatga qarab nonushta har xil boʻladi.</p>
  <p class="pe-ex__why">«Mamlakatlar tomonidan» emas — bu yerda によって sabab ham, bajaruvchi ham emas: u faqat <em>nimaga qarab farq borligini</em> koʻrsatadi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Bu vazifaning tez-tez uchraydigan juftliklari.</b>
  <ruby>人<rt>ひと</rt></ruby>によって — odamga qarab ·
  <ruby>場合<rt>ばあい</rt></ruby>によって — holatga qarab ·
  <ruby>店<rt>みせ</rt></ruby>によって — doʻkonga qarab ·
  <ruby>地方<rt>ちほう</rt></ruby>によって — hududga qarab.
  Ular shu qadar koʻp ishlatiladiki, yodlab qoʻygan maʼqul —
  matnda koʻrsangiz, keyin albatta
  <ruby>違<rt>ちが</rt></ruby>う keladi.</p>
</div>

<h3>5. による + ot</h3>

<p>によって ni otga ulash kerak boʻlsa, oxiri <b>による</b> ga
oʻzgaradi. Bu aynan PJ-48 dagi aniqlovchi ergash gap —
<ruby>因<rt>よ</rt></ruby>る feʼli lugʻat shaklida turib, otni
aniqlaydi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>地震<rt>じしん</rt></ruby></span>
  <span class="pj-joshi__p">による<small>ANIQLOVCHI</small></span>
  <span class="pj-joshi__n"><ruby>被害<rt>ひがい</rt></ruby></span>
  <span class="pj-joshi__v">は<ruby>大<rt>おお</rt></ruby>きかった</span>
  <span class="pj-joshi__uz">Zilziladan koʻrilgan zarar katta edi.</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--o"><ruby>台風<rt>たいふう</rt></ruby>による<ruby>被害<rt>ひがい</rt></ruby></span>が<ruby>新聞<rt>しんぶん</rt></ruby>に<ruby>出<rt>で</rt></ruby>ていた。</p>
  <p class="pe-ex__uz">Tayfundan koʻrilgan zarar gazetada chiqqan edi.</p>
  <p class="pe-ex__why">によって<ruby>被害<rt>ひがい</rt></ruby> deb boʻlmaydi: ot oldiga faqat <b>による</b> tushadi.</p>
</div>

<h3>6. Nega yozma matnda passiv shuncha koʻp</h3>

<p>Yaponcha maqola, yangilik va darslik passivni juda koʻp
ishlatadi — va buning sababi grammatik emas, <b>uslubiy</b>.</p>

<div class="pe-steps">
  <ol>
    <li><b>Bajaruvchi muhim emas.</b> «Kim qurgan» emas,
    «qurilgan» degan fakt muhim:
    この<ruby>寺<rt>てら</rt></ruby>は<ruby>建<rt>た</rt></ruby>てられた.</li>
    <li><b>Mavzuni oʻzgartirmaslik kerak.</b> Butun xat boshi
    koʻprik haqida boʻlsa, koʻprik は bilan boshda qoladi —
    passiv shuni imkon beradi.</li>
    <li><b>Xolislik.</b> «Men oʻylaymanki» degan gap ilmiy
    matnda oʻrinsiz; oʻrniga
    <ruby>考<rt>かんが</rt></ruby>えられている («shunday deb
    hisoblanadi») yoziladi.</li>
  </ol>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>方法<rt>ほうほう</rt></ruby>は<ruby>世界中<rt>せかいじゅう</rt></ruby>で<span class="pe-hl pe-hl--v"><ruby>使<rt>つか</rt></ruby>われている</span>。</p>
  <p class="pe-ex__uz">Bu usul butun dunyoda qoʻllanadi.</p>
  <p class="pe-ex__why">Kim qoʻllashi aytilmagan va kerak ham emas. Aynan shu — yozma yapon tilining odatiy ovozi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tili bu yerda yapon tiliga juda yaqin turadi.</b>
  «Bu usul butun dunyoda <em>qoʻllanadi</em>», «koʻprik yuz yil
  oldin <em>qurilgan</em>», «shunday deb <em>hisoblanadi</em>» —
  biz ham ilmiy va rasmiy matnda majhul nisbatni tanlaymiz va
  bajaruvchini aytmaymiz. Farqi shundaki, oʻzbekchada bu
  <em>ixtiyoriy</em> — «olimlar hisoblaydi» desangiz ham
  boʻladi. Yapon tilida esa bu deyarli <em>majburiy</em>:
  ilmiy matnda «<ruby>私<rt>わたし</rt></ruby>は…と
  <ruby>思<rt>おも</rt></ruby>う» deb yozgan talabaga ustoz
  albatta izoh yozadi. Shuning uchun yaponcha matn oʻqiyotganda
  passivni «kim?» deb qidirmang — koʻpincha javob yoʻq, va
  boʻlishi ham kerak emas.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">因</span>
    <span class="pj-kanji__uz">sabab, kelib chiqmoq</span>
    <span class="pj-kanji__on">オン: イン</span>
    <span class="pj-kanji__kun">KUN: よ(る)</span>
    <span class="pj-kanji__note">原因 (げんいん) — sabab · 〜による — …dan kelib chiqqan</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">被</span>
    <span class="pj-kanji__uz">zarar koʻrmoq, ustiga olmoq</span>
    <span class="pj-kanji__on">オン: ヒ</span>
    <span class="pj-kanji__kun">KUN: こうむ(る)</span>
    <span class="pj-kanji__note">被害 (ひがい) — zarar · 被災地 (ひさいち) — ofat hududi</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">害</span>
    <span class="pj-kanji__uz">zarar, ziyon</span>
    <span class="pj-kanji__on">オン: ガイ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">公害 (こうがい) — ekologik ifloslanish · 害虫 (がいちゅう) — zararkunanda</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>先生<rt>せんせい</rt></ruby>によって<ruby>叱<rt>しか</rt></ruby>られた</p>
  <p class="pe-fix__good">✓ <ruby>先生<rt>せんせい</rt></ruby><b>に</b><ruby>叱<rt>しか</rt></ruby>られた — odam aziyat chekkan passivda oddiy に turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>台風<rt>たいふう</rt></ruby>によって<ruby>被害<rt>ひがい</rt></ruby>が<ruby>大<rt>おお</rt></ruby>きかった</p>
  <p class="pe-fix__good">✓ <ruby>台風<rt>たいふう</rt></ruby><b>による</b><ruby>被害<rt>ひがい</rt></ruby> — ot oldida shakl による ga oʻzgaradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>だによって<ruby>作<rt>つく</rt></ruby>られた</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby>によって — によって otga yalangʻoch ulanadi, だ ham, の ham olmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>人<rt>ひと</rt></ruby>によって<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>が<ruby>作<rt>つく</rt></ruby>られた («odamga qarab har xil» maʼnosida)</p>
  <p class="pe-fix__good">✓ <ruby>人<rt>ひと</rt></ruby>によって<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>が<b><ruby>違<rt>ちが</rt></ruby>う</b> — «farq qiladi» maʼnosida oxirida <ruby>違<rt>ちが</rt></ruby>う, <ruby>変<rt>か</rt></ruby>わる yoki <ruby>決<rt>き</rt></ruby>まる turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>は、この<ruby>方法<rt>ほうほう</rt></ruby>がいいと<ruby>思<rt>おも</rt></ruby>う (ilmiy maqolada)</p>
  <p class="pe-fix__good">✓ この<ruby>方法<rt>ほうほう</rt></ruby>がいいと<b><ruby>考<rt>かんが</rt></ruby>えられている</b> — yozma matn xolis ovozni talab qiladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Ustoz meni urishdi» — に yoki によって?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>に</b>: <ruby>先生<rt>せんせい</rt></ruby>に<ruby>叱<rt>しか</rt></ruby>られた. Gap odam haqida va u taʼsir koʻrgan — によって esa yaratish va rasmiy xabar uchun.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Boʻsh joyni toʻldiring: <ruby>台風<rt>たいふう</rt></ruby>___<ruby>被害<rt>ひがい</rt></ruby>が<ruby>新聞<rt>しんぶん</rt></ruby>に<ruby>出<rt>で</rt></ruby>ていた。</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>による</b> — otdan oldin qolip による ga oʻzgaradi: <ruby>台風<rt>たいふう</rt></ruby>による<ruby>被害<rt>ひがい</rt></ruby>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>国<rt>くに</rt></ruby>によって<ruby>朝<rt>あさ</rt></ruby>ごはんが___ — oxiriga qaysi feʼl tabiiy?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>違<rt>ちが</rt></ruby>う</b> (yoki <ruby>変<rt>か</rt></ruby>わる). «…ga qarab» maʼnosida gap deyarli har doim shu uchta feʼlning biri bilan tugaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Bu ibodatxona sakkizinchi asrda qurilgan» — bajaruvchini aytish kerakmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> この<ruby>寺<rt>てら</rt></ruby>は<ruby>八世紀<rt>はちせいき</rt></ruby>に<ruby>建<rt>た</rt></ruby>てられた. Yozma matnda bajaruvchisiz passiv — eng odatiy koʻrinish.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. によって ning toʻrtta vazifasini ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Bajaruvchi</b> (… tomonidan), <b>sabab</b> (… tufayli), <b>vosita</b> (… orqali), <b>farqlanish</b> (…ga qarab). Toʻrtalasi bitta savolga javob beradi: gapdagi ish qayerdan kelib chiqdi?</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜によって</b> — … tomonidan; tufayli; orqali; ga qarab</li>
  <li><b>〜による + ot</b> — …dan kelib chiqqan …</li>
  <li><b><ruby>被害<rt>ひがい</rt></ruby></b> — zarar, talafot</li>
  <li><b><ruby>原因<rt>げんいん</rt></ruby></b> — sabab</li>
  <li><b><ruby>地震<rt>じしん</rt></ruby></b> — zilzila</li>
  <li><b><ruby>台風<rt>たいふう</rt></ruby></b> — tayfun</li>
  <li><b><ruby>解決<rt>かいけつ</rt></ruby>する</b> — hal qilmoq</li>
  <li><b><ruby>場合<rt>ばあい</rt></ruby></b> — holat, vaziyat</li>
  <li><b><ruby>方法<rt>ほうほう</rt></ruby></b> — usul</li>
  <li><b><ruby>考<rt>かんが</rt></ruby>えられている</b> — shunday deb hisoblanadi</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Bitta savol toʻrtala vazifani ochadi: <b>ish qayerdan kelib chiqdi?</b></li>
    <li>Passivda: yaratish → <b>によって</b>, odam aziyat chekkan → <b>に</b>.</li>
    <li>Ot oldida shakl <b>による</b> ga oʻzgaradi.</li>
  </ul>
</div>
""",
    },
]
