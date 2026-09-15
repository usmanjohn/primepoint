# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-64, PJ-65, PJ-66 (Blok E: ovoz va nuqtai nazar).

Uchala dars ham BITTA oʻzakdan yasaladi — PJ-34 dagi あ-oʻzak:
    PJ-63  passiv      行か + れる      → 行かれる
    PJ-65  kauzativ    行か + せる      → 行かせる
    PJ-66  ikkalasi    行かせ + られる  → 行かせられる
PJ-64 esa yangi shakl emas, passivning yaponchaga xos ISHLATILISHI:
迷惑の受身 — «aziyat passivi». Yevropa tillarida bunday narsa yoʻq,
shuning uchun dars buni ochiq tan olishdan boshlanadi.

⚠️ う bilan tugagan feʼllar uchala shaklda ham わ beradi
(言う → 言われる · 言わせる · 言わせられる). Bu batchning eng koʻp
takrorlanadigan xatosi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_64_66.py --author=prime
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
        "title": "PJ-64: Passiv 2: «aziyat chekish» passivi — yaponchaning oʻziga xos shakli",
        "category": "japanese",
        "order": 64,
        "summary": (
            "«Yomgʻir menga yogʻildi» — bunday gap oʻzbekchada ham, "
            "ingliz tilida ham yoʻq. Yaponchada esa bu eng oddiy "
            "gaplardan biri, va u aynan noroziliqni bildiradi."
        ),
        "stories": ["ついてない ひ"],
        "content": """
<h2>PJ-64: Passiv 2: «aziyat chekish» passivi</h2>

<p>Bitta yaponcha gapni oʻqing:</p>

<p><ruby>雨<rt>あめ</rt></ruby>に<ruby>降<rt>ふ</rt></ruby>られました。</p>

<p>Soʻzma-soʻz: «yomgʻir tomonidan yogʻildim». Bunday gap
oʻzbekchada yoʻq — <em>yogʻmoq</em> oʻtimsiz feʼl, uni passivga
oʻtkazib boʻlmaydi. Yaponchada esa bu butunlay oddiy gap va u
bitta aniq narsani bildiradi: <b>yomgʻir yogʻdi va men shundan
zarar koʻrdim</b>.</p>

<p>Bu — <b><ruby>迷惑<rt>めいわく</rt></ruby>の<ruby>受身<rt>うけみ</rt></ruby></b>,
«tashvish passivi». Uni oʻrganmasdan yaponcha hikoyani tushunib
boʻlmaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Oʻtimsiz feʼldan passiv yasaysiz</li>
    <li>Gapning egasi nega <em>zarar koʻrgan odam</em> ekanini tushunasiz</li>
    <li>Egalik buyumi zarar koʻrgan gapni tuzasiz</li>
    <li>PJ-58 dagi 〜てしまう bilan bogʻlanishini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Aziyat passivi</span>
  <span class="pe-chip pe-chip--s">ZARAR KOʻRGAN</span>
  <span class="pe-op">は</span>
  <span class="pe-chip pe-chip--adv">SABABCHI に</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">passiv feʼl</span>
</div>

<h3>1. Oʻtimsiz feʼl ham passivga oʻtadi</h3>

<p>PJ-63 da siz oʻtimli feʼllarni koʻrgansiz:
<ruby>褒<rt>ほ</rt></ruby>める → <ruby>褒<rt>ほ</rt></ruby>められる.
U yerda mantiq tanish edi: maqtash ishi bor, va uni kimdir
qabul qiladi. Bugun esa boshqa narsa boʻladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oddiy gap</th><th>Aziyat passivi</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem"><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りました</td>
      <td class="pj-res"><ruby>雨<rt>あめ</rt></ruby>に<ruby>降<rt>ふ</rt></ruby>られました</td>
      <td class="pj-uz">yomgʻir yogʻdi — va men shilta boʻldim</td></tr>
  <tr><td class="pj-stem"><ruby>友<rt>とも</rt></ruby>だちが<ruby>来<rt>き</rt></ruby>ました</td>
      <td class="pj-res"><ruby>友<rt>とも</rt></ruby>だちに<ruby>来<rt>こ</rt></ruby>られました</td>
      <td class="pj-uz">doʻstim keldi — va ishim buzildi</td></tr>
  <tr><td class="pj-stem"><ruby>子<rt>こ</rt></ruby>どもが<ruby>泣<rt>な</rt></ruby>きました</td>
      <td class="pj-res"><ruby>子<rt>こ</rt></ruby>どもに<ruby>泣<rt>な</rt></ruby>かれました</td>
      <td class="pj-uz">bola yigʻladi — va men uxlay olmadim</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Gapning egasi umuman ishtirok etmaydi.</b> Yomgʻir
  yogʻganda siz hech nima qilmadingiz; bola yigʻlaganda ham.
  Shunga qaramay <em>siz</em> gapning egasisiz. Sababi oddiy:
  yapon tilida bu gapning mavzusi ish emas, <b>uning sizga
  tegishi</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu yerda oʻzbek tili yordam bermaydi — va shuni ochiq
  aytish kerak.</b> «Yomgʻirda qolib ketdim», «bola yigʻlab,
  uxlay olmadim» — oʻzbekchada <em>maʼno</em> bor, lekin u
  <b>qoʻshimcha soʻzlar</b> bilan beriladi. Yaponchada esa
  hech qanday qoʻshimcha soʻz yoʻq: shikoyat <b>feʼlning
  ichida</b> turadi. Shuning uchun bu darsni tarjima orqali
  emas, <em>tasvir</em> orqali oʻrganing: siz turibsiz, dunyo
  bir ish qildi, va u sizga tegdi.</p>
</div>

<h3>2. Eng yaqin oʻzbekcha qarindoshi — «-ib qoʻydi»</h3>

<p>Aslida oʻzbekchada shu ishni qiladigan bitta qurilma bor,
va siz uni PJ-58 da koʻrgansiz.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">OʻZBEKCHA</p>
    <p>Ukam tortimni yeb <b>qoʻydi</b>.</p>
    <p>Shikoyat <b>yordamchi feʼlda</b>: «-ib qoʻydi».</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">YAPONCHA</p>
    <p><ruby>弟<rt>おとうと</rt></ruby>にケーキを<ruby>食<rt>た</rt></ruby>べ<b>られました</b>。</p>
    <p>Shikoyat <b>passivda</b>.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Ikkala til ham norozilikni grammatikaga yashiradi —
  faqat boshqa joyga.</b> Oʻzbekcha uni yordamchi feʼlga
  qoʻyadi (PJ-58 dagi 〜てしまう ga toʻgʻri keladi), yaponcha
  esa <em>passivga</em>. Shuning uchun yaponcha aziyat
  passivini oʻzbekchaga tarjima qilganda deyarli doim
  <b>«-ib qoʻydi»</b> yoki <b>«-ib ketdi»</b> chiqadi. Bu —
  eng foydali tarjima qoidasi.</p>
</div>

<p>Bu shakl nega mavjud degan savolga eng qisqa javob shu:
yapon tilida <b>his-tuygʻuni aytish uchun alohida soʻz kerak
emas</b>. «Afsuski», «baxtimga qarshi», «menga xalaqit
berib» — bularning hammasi grammatikaning ichiga sigʻdirilgan.
Shuning uchun yaponcha gap qisqa boʻlsa ham, undagi maʼlumot
oʻzbekcha tarjimaga qaraganda koʻproq.</p>

<h3>3. Egalik buyumi zarar koʻrganda</h3>

<p>Oʻtimli feʼl bilan ham aziyat passivi boʻladi — va u yerda
gʻalati bir narsa koʻrinadi: <b>を qoʻshimchasi
qolaveradi</b>.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">は<small>ZARAR KOʻRGAN</small></span>
  <span class="pj-joshi__n"><ruby>弟<rt>おとうと</rt></ruby></span>
  <span class="pj-joshi__p">に<small>SABABCHI</small></span>
  <span class="pj-joshi__n">ケーキ</span>
  <span class="pj-joshi__p">を<small>QOLADI</small></span>
  <span class="pj-joshi__v"><ruby>食<rt>た</rt></ruby>べられました</span>
  <span class="pj-joshi__uz">Ukam tortimni yeb qoʻydi.</span>
</div>

<div class="pe-call pe-warn">
  <p><b>Nega を qolyapti?</b> Chunki gapning egasi tort emas,
  <b>men</b>. Oddiy passivda «ケーキは<ruby>弟<rt>おとうと</rt></ruby>に
  <ruby>食<rt>た</rt></ruby>べられました» deyish ham mumkin —
  lekin u shunchaki fakt boʻladi, shikoyat emas. Egasi
  <em>odam</em> boʻlsa, gap noroziliqqa aylanadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>電車<rt>でんしゃ</rt></ruby>で<ruby>足<rt>あし</rt></ruby>を<ruby>踏<rt>ふ</rt></ruby>まれました。</p>
  <p class="pe-ex__uz">Poyezdda oyogʻimni bosib ketishdi.</p>
  <p class="pe-ex__why">Kim bosgani aytilmagan — muhimi, <em>menga</em> tegdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>財布<rt>さいふ</rt></ruby>を<ruby>盗<rt>ぬす</rt></ruby>まれました。</p>
  <p class="pe-ex__uz">Hamyonimni oʻgʻirlab ketishdi.</p>
  <p class="pe-ex__why">Yana を qolgan — zarar koʻrgan men, hamyon emas.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ega oʻzgarmaydi, yaponchada oʻzgaradi.</b>
  «Hamyonimni oʻgʻirlab <em>ketishdi</em>» — bu gapda ega
  noaniq «ular», siz esa faqat «-im» qoʻshimchasida turibsiz.
  Yaponcha esa <b>sizni gap boshiga chiqaradi</b>:
  <ruby>私<rt>わたし</rt></ruby>は… Shuning uchun yaponcha hikoyada
  gapiruvchi doim koʻrinib turadi, hatto u hech nima
  qilmagan boʻlsa ham. Bu tilning eng koʻzga koʻrinmas, lekin
  eng kuchli odati.</p>
</div>

<h3>4. Qaysi passiv ekanini qanday bilish</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Belgi</th><th>Oddiy passiv (PJ-63)</th><th>Aziyat passivi</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-uz">oʻtimli</td>
      <td class="pj-res">oʻtimsiz ham boʻladi</td></tr>
  <tr><td class="pj-stem">Ega</td><td class="pj-uz">narsa yoki odam</td>
      <td class="pj-res">deyarli doim <b>odam</b></td></tr>
  <tr><td class="pj-stem">を</td><td class="pj-uz">yoʻqoladi</td>
      <td class="pj-res">koʻpincha <b>qoladi</b></td></tr>
  <tr><td class="pj-stem">Ohang</td><td class="pj-uz">betaraf</td>
      <td class="pj-res"><b>norozilik</b></td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Tekshirishning bir gaplik usuli.</b> Gapni oʻzbekchaga
  tarjima qilganda «-ib qoʻydi», «-ib ketdi» yoki «afsuski»
  qoʻshgingiz kelsa — bu aziyat passivi.</p>
</div>

<p>Amalda bu shakl bilan uchrashadigan birinchi joyingiz —
uzr soʻrash. Yaponiyada kimdir sizga xalaqit bergan boʻlsa,
u <ruby>迷惑<rt>めいわく</rt></ruby>をかけました deydi, siz esa
javoban aynan shu passivni ishlatib nima boʻlganini
tushuntirasiz. Yaʼni bu grammatika kitobiy emas — u har kuni,
koʻchada va ish joyida eshitiladi.</p>

<h3>5. Nima uchun bu shakl bor</h3>

<p>Sababi PJ-63 da aytilgan edi: yapon tili <b>gapning
mavzusini oʻzgartirmaslikni</b> yaxshi koʻradi. Hikoya siz
haqingizda ketayotgan boʻlsa, hatto yomgʻir haqidagi gap ham
sizdan boshlanishi kerak. Aziyat passivi shuni imkon beradi —
va yoʻl-yoʻlakay his-tuygʻuni ham olib yuradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>昨日<rt>きのう</rt></ruby>は<ruby>大変<rt>たいへん</rt></ruby>でした。<ruby>雨<rt>あめ</rt></ruby>に<ruby>降<rt>ふ</rt></ruby>られて、<ruby>電車<rt>でんしゃ</rt></ruby>に<ruby>遅<rt>おく</rt></ruby>れて、<ruby>先生<rt>せんせい</rt></ruby>に<ruby>叱<rt>しか</rt></ruby>られました。</p>
  <p class="pe-ex__uz">Kecha ogʻir kun boʻldi. Yomgʻirda qoldim, poyezdga kechikdim, oʻqituvchi koyidi.</p>
  <p class="pe-ex__why">Uchala qismda ham ega — <b>men</b>. Yaponcha yomon kun hikoyasi deyarli doim shunday yoziladi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">迷</span>
    <span class="pj-kanji__uz">adashmoq</span>
    <span class="pj-kanji__on">オン: メイ</span>
    <span class="pj-kanji__kun">KUN: まよ(う)</span>
    <span class="pj-kanji__note">迷惑 (めいわく) — tashvish · 道に迷う (みちにまよう) — yoʻldan adashmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">泣</span>
    <span class="pj-kanji__uz">yigʻlamoq</span>
    <span class="pj-kanji__on">オン: キュウ</span>
    <span class="pj-kanji__kun">KUN: な(く)</span>
    <span class="pj-kanji__note">泣く (なく) — yigʻlamoq · 泣かれる — yigʻlab tashvish berilmoq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>られました</p>
  <p class="pe-fix__good">✓ <ruby>雨<rt>あめ</rt></ruby><b>に</b><ruby>降<rt>ふ</rt></ruby>られました — sababchi doim <b>に</b> oladi, が emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ケーキ<b>が</b><ruby>弟<rt>おとうと</rt></ruby>に<ruby>食<rt>た</rt></ruby>べられて、<ruby>私<rt>わたし</rt></ruby>は<ruby>悲<rt>かな</rt></ruby>しかった</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby>は<ruby>弟<rt>おとうと</rt></ruby>にケーキ<b>を</b><ruby>食<rt>た</rt></ruby>べられました — shikoyat uchun ega <b>odam</b> boʻlishi kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>友<rt>とも</rt></ruby>だちに<ruby>来<rt>き</rt></ruby>られました</p>
  <p class="pe-fix__good">✓ <ruby>友<rt>とも</rt></ruby>だちに<ruby>来<rt>こ</rt></ruby>られました — <ruby>来<rt>く</rt></ruby>る ning ない-oʻzagi <b>こ</b> (PJ-63).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>雨<rt>あめ</rt></ruby>に<ruby>降<rt>ふ</rt></ruby>られました = «yomgʻirni yoqtiraman»</p>
  <p class="pe-fix__good">✓ Bu shakl <b>doim norozilik</b> bildiradi. Yaxshi yomgʻir uchun oddiy <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りました.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «<ruby>雨<rt>あめ</rt></ruby>に<ruby>降<rt>ふ</rt></ruby>られました» ni oʻzbekchaga tarjima qiling.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yomgʻirda qolib ketdim.</b> Soʻzma-soʻz emas — maʼnosi shu.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Bola yigʻladi va men uxlay olmadim» ni bitta gap qilib yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>子<rt>こ</rt></ruby>どもに<ruby>泣<rt>な</rt></ruby>かれました</b> — qolgani gapning ichida turibdi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «<ruby>私<rt>わたし</rt></ruby>は<ruby>弟<rt>おとうと</rt></ruby>にケーキを<ruby>食<rt>た</rt></ruby>べられました» — nega を qolgan?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki gapning egasi tort emas, <b>men</b>. Egasi odam boʻlsa, gap shikoyatga aylanadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Sababchi qaysi qoʻshimchani oladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>に</b> — <ruby>雨<rt>あめ</rt></ruby><b>に</b>, <ruby>弟<rt>おとうと</rt></ruby><b>に</b>. Bu PJ-63 dagi qoidaning oʻzi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Gap aziyat passivi ekanini qanday bilasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Tarjimada <b>«-ib qoʻydi»</b> yoki <b>«-ib ketdi»</b> qoʻshgingiz kelsa. Yana: ega odam, を qolgan, feʼl oʻtimsiz boʻlishi mumkin.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>迷惑<rt>めいわく</rt></ruby>の<ruby>受身<rt>うけみ</rt></ruby></b> — aziyat passivi</li>
  <li><b><ruby>泣<rt>な</rt></ruby>く</b> — yigʻlamoq (I guruh)</li>
  <li><b><ruby>踏<rt>ふ</rt></ruby>む</b> — bosmoq (I guruh)</li>
  <li><b><ruby>盗<rt>ぬす</rt></ruby>む</b> — oʻgʻirlamoq (I guruh)</li>
  <li><b><ruby>死<rt>し</rt></ruby>ぬ</b> — oʻlmoq (I guruh)</li>
  <li><b><ruby>大変<rt>たいへん</rt></ruby></b> — ogʻir, qiyin (な-sifat)</li>
  <li><b><ruby>迷惑<rt>めいわく</rt></ruby></b> — tashvish, bezovtalik</li>
  <li><b>ついてない</b> — omadsiz</li>
  <li><b><ruby>財布<rt>さいふ</rt></ruby></b> — hamyon</li>
  <li><b><ruby>邪魔<rt>じゃま</rt></ruby></b> — xalaqit (な-sifat)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Yaponchada <b>oʻtimsiz feʼl ham</b> passivga oʻtadi.</li>
    <li>Ega — <b>zarar koʻrgan odam</b>, va を koʻpincha qoladi.</li>
    <li>Tarjimada <b>«-ib qoʻydi»</b> chiqsa — bu aynan shu shakl.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-65: Kauzativ (使役): 行かせる — qildirmoq va ruxsat bermoq",
        "category": "japanese",
        "order": 65,
        "summary": (
            "Oʻzbekchada «oʻqi-t-dim», «kul-dir-dim» bor — demak qurilma "
            "sizda allaqachon mavjud. Yaponcha faqat bitta narsani "
            "qoʻshadi: majburmi yoki ruxsatmi."
        ),
        "stories": ["いかせて ください"],
        "content": """
<h2>PJ-65: Kauzativ (<ruby>使役<rt>しえき</rt></ruby>): <ruby>行<rt>い</rt></ruby>かせる</h2>

<p>Oʻzbekcha uchta gapni oʻqing:</p>

<p>Bola kitob <b>oʻqidi</b>. → Men unga kitob <b>oʻqitdim</b>.<br>
Bola <b>kuldi</b>. → Men uni <b>kuldirdim</b>.</p>

<p>Oʻzbek tilida feʼl ichiga bitta boʻgʻin qoʻshasiz —
<b>-t-</b>, <b>-dir-</b> — va maʼno oʻzgaradi: endi ishni
boshqa odam qiladi, lekin uni <em>siz</em> boshlaysiz. Yapon
tilida ham aynan shunday, va qoʻshimchaning nomi
<b><ruby>使役形<rt>しえきけい</rt></ruby></b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uch guruh feʼlidan kauzativ yasaysiz</li>
    <li>«Majbur qildim» va «ruxsat berdim» ni ajratasiz</li>
    <li>を va に farqini toʻgʻri qoʻyasiz</li>
    <li>〜させてください bilan ruxsat soʻraysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kauzativ</span>
  <span class="pe-chip pe-chip--s">ない-oʻzak</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">せる / させる</span>
</div>

<h3>1. Yasalishi — oʻsha あ-oʻzak</h3>

<p>PJ-63 da passiv uchun <b>ない-oʻzagini</b> ishlatgan
edingiz. Kauzativ ham oʻsha oʻzakdan yasaladi — faqat れる
oʻrniga <b>せる</b> qoʻyiladi.</p>

<div class="pj-group">
  <div class="pj-group__c">
    <p class="pj-group__h">I — <ruby>五段<rt>ごだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>行<rt>い</rt></ruby>く → <ruby>行<rt>い</rt></ruby>かせる</p>
    <p>あ-qatorga tushadi, keyin <b>せる</b>.</p>
  </div>
  <div class="pj-group__c pj-group__c--2">
    <p class="pj-group__h">II — <ruby>一段<rt>いちだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>食<rt>た</rt></ruby>べる → <ruby>食<rt>た</rt></ruby>べさせる</p>
    <p>る tushadi, <b>させる</b> qoʻyiladi.</p>
  </div>
  <div class="pj-group__c pj-group__c--3">
    <p class="pj-group__h">III — <ruby>不規則<rt>ふきそく</rt></ruby></p>
    <p class="pj-group__ex">する → させる · <ruby>来<rt>く</rt></ruby>る → <ruby>来<rt>こ</rt></ruby>させる</p>
    <p>Faqat ikkita.</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Passiv (PJ-63)</th><th>Kauzativ (bugun)</th></tr>
  <tr><td class="pj-stem"><ruby>読<rt>よ</rt></ruby>む</td>
      <td class="pj-uz"><ruby>読<rt>よ</rt></ruby>まれる</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>ませる</td></tr>
  <tr><td class="pj-stem"><ruby>行<rt>い</rt></ruby>く</td>
      <td class="pj-uz"><ruby>行<rt>い</rt></ruby>かれる</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>かせる</td></tr>
  <tr><td class="pj-stem"><ruby>言<rt>い</rt></ruby>う</td>
      <td class="pj-uz"><ruby>言<rt>い</rt></ruby>われる</td><td class="pj-res"><ruby>言<rt>い</rt></ruby>わせる</td></tr>
  <tr><td class="pj-stem"><ruby>待<rt>ま</rt></ruby>つ</td>
      <td class="pj-uz"><ruby>待<rt>ま</rt></ruby>たれる</td><td class="pj-res"><ruby>待<rt>ま</rt></ruby>たせる</td></tr>
  <tr><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べる</td>
      <td class="pj-uz"><ruby>食<rt>た</rt></ruby>べられる</td><td class="pj-res"><ruby>食<rt>た</rt></ruby>べさせる</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Yana わ.</b> <ruby>言<rt>い</rt></ruby>う →
  <ruby>言<rt>い</rt></ruby><b>わ</b>せる,
  <ruby>使<rt>つか</rt></ruby>う →
  <ruby>使<rt>つか</rt></ruby><b>わ</b>せる. Bu uchinchi marta —
  PJ-34 da ない-shaklida, PJ-63 da passivda, bugun kauzativda.
  Oʻzak bitta boʻlgani uchun istisno ham bitta.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu qoʻshimcha juda kuchli.</b>
  «Oʻqi-<b>t</b>-dim», «kul-<b>dir</b>-dim»,
  «yoz-<b>dir</b>-dim», «ye-<b>diz</b>-dim» — siz buni har
  kuni ishlatasiz va hech qachon oʻylab koʻrmagansiz.
  Yaponchada ham xuddi shunday: <b>せる / させる</b> feʼlning
  ichiga kiradi va uni «qildirmoq» ga aylantiradi. Yaʼni bu
  dars yangi <em>fikr</em> emas — faqat yangi qoʻshimcha.</p>
</div>

<h3>2. Ikki maʼno: majbur qilish va ruxsat berish</h3>

<p>Mana bu yerda yapon tili oʻzbekchadan oʻzib ketadi.
Bitta shakl <b>ikki</b> maʼnoni koʻtaradi, va ularni
kontekst hamda qoʻshimchalar ajratadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">MAJBUR QILISH</p>
    <p><ruby>先生<rt>せんせい</rt></ruby>は<ruby>学生<rt>がくせい</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>ませました。</p>
    <p>Oʻqituvchi talabalarga kitob <b>oʻqitdi</b> — ular
    xohlamagan boʻlishi mumkin.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">RUXSAT BERISH</p>
    <p><ruby>母<rt>はは</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>を<ruby>行<rt>い</rt></ruby>かせてくれました。</p>
    <p>Onam meni <b>qoʻyib yubordi</b> — men xohlagan edim.</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>〜てくれる qoʻshilsa, maʼno deyarli doim
  «ruxsat».</b> Sababi PJ-61 dan tanish: くれる yaxshilikni
  bildiradi, va majburlash yaxshilik boʻlmaydi. Shuning uchun
  <b>〜させてくれました</b> = «qilishimga ruxsat berdi»,
  <b>〜させました</b> esa koʻpincha «majbur qildi».</p>
</div>

<p>Nega bitta shakl ikki maʼnoni koʻtaradi degan savolga
javob oddiy: ikkala holatda ham <b>ish sizdan boshlanadi</b>.
Bola ketdi — chunki siz shunday qildingiz. Farq faqat shunda:
bola buni xohladimi yoki yoʻqmi. Yapon tili bu farqni
feʼlga emas, <em>gapning qolgan qismiga</em> yuklaydi.
Oʻzbek tili esa uni feʼlga yuklaydi, shuning uchun bizda
ikkita boshqa gap chiqadi.</p>

<h3>3. を yoki に — bu ham maʼnoni koʻrsatadi</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl turi</th><th>Qoʻshimcha</th><th>Misol</th><th>Ohang</th></tr>
  <tr><td class="pj-stem">Oʻtimsiz</td><td class="pj-end"><b>を</b></td>
      <td class="pj-res"><ruby>子<rt>こ</rt></ruby>ども<b>を</b><ruby>行<rt>い</rt></ruby>かせる</td>
      <td class="pj-uz">majbur qildim</td></tr>
  <tr><td class="pj-stem">Oʻtimsiz</td><td class="pj-end"><b>に</b></td>
      <td class="pj-res"><ruby>子<rt>こ</rt></ruby>ども<b>に</b><ruby>行<rt>い</rt></ruby>かせる</td>
      <td class="pj-uz">ruxsat berdim</td></tr>
  <tr><td class="pj-stem">Oʻtimli</td><td class="pj-end">doim <b>に</b></td>
      <td class="pj-res"><ruby>子<rt>こ</rt></ruby>ども<b>に</b><ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>ませる</td>
      <td class="pj-uz">kontekst hal qiladi</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Oʻtimli feʼlda を band.</b> «<ruby>本<rt>ほん</rt></ruby>を»
  allaqachon を ni olgan, shuning uchun odam faqat
  <b>に</b> qola oladi. Bitta gapda ikkita を boʻlmaydi — bu
  yapon tilining qatʼiy qoidasi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu farq yoʻq — va shuni bilib qoʻying.</b>
  «Bolani yubordim» va «bolaga ruxsat berdim» — oʻzbekchada
  ikki boshqa gap, ikki boshqa feʼl. Yaponchada esa bitta
  feʼl, va farq faqat <b>を / に</b> da hamda
  <b>〜てくれる</b> da koʻrinadi. Shuning uchun yaponcha
  matnni oʻqiganda qoʻshimchaga eʼtibor bering: u yerda
  butun maʼno turibdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>母<rt>はは</rt></ruby>は<ruby>弟<rt>おとうと</rt></ruby>に<ruby>野菜<rt>やさい</rt></ruby>を<ruby>食<rt>た</rt></ruby>べさせました。</p>
  <p class="pe-ex__uz">Onam ukamga sabzavot yedirdi.</p>
  <p class="pe-ex__why">Oʻtimli feʼl: buyum を, odam <b>に</b>. Va ohangi — majburlash.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham «yedirdim» va «yeyishiga ruxsat
  berdim» bir xil emas.</b> Faqat oʻzbekcha bu farqni
  <em>boshqa feʼl</em> bilan koʻrsatadi: «yubordim» va «ruxsat
  berdim». Yaponcha esa bitta feʼlni saqlab, atrofidagi
  kichkina belgilarni oʻzgartiradi — <b>を / に</b> va
  <b>〜てくれる</b>. Shuning uchun yaponcha matnni oʻqiyotganda
  qoʻshimchani oʻtkazib yuborish maʼnoni teskari qilib
  qoʻyishi mumkin.</p>
</div>

<h3>4. 〜させてください — ruxsat soʻrash</h3>

<p>Bu qolip amalda eng kerakli: kauzativning て-shakli +
ください = «menga … qilishga ruxsat bering».</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>にやらせてください。</p>
  <p class="pe-ex__uz">Menga qilishga ruxsat bering. / Buni men qilay.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>少<rt>すこ</rt></ruby>し<ruby>考<rt>かんが</rt></ruby>えさせてください。</p>
  <p class="pe-ex__uz">Biroz oʻylab koʻray.</p>
  <p class="pe-ex__why">Yaponchada «oʻylab koʻraman» deyish oʻrniga koʻpincha «oʻylashimga ruxsat bering» deyiladi — bu ancha muloyim.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Muloyimroq shakli — 〜させていただけますか.</b>
  PJ-61 dagi zinapoyaning oʻzi: gap uzaygan sari
  muloyimlashadi. Ish suhbatida va rasmiy joyda aynan shu
  ishlatiladi.</p>
</div>

<p>Yana bir joyi bor, va u imtihonda koʻp uchraydi:
kauzativ <b>hurmat</b> uchun ham ishlatiladi. Kattaroq odamga
«men qilaman» deyish oʻrniga «qilishimga ruxsat bering»
desangiz, siz oʻzingizni pastroqqa qoʻyasiz — va bu yapon
odobining asosiy harakati. Shuning uchun ish joyida
<ruby>説明<rt>せつめい</rt></ruby>させていただきます
(«tushuntirishimga ruxsat bering») degan gap
<ruby>説明<rt>せつめい</rt></ruby>します dan ancha koʻp
eshitiladi.</p>

<h3>5. Nima uchun bu shakl muhim</h3>

<p>Ikki sabab bor. Birinchisi: yaponchada <b>ruxsat soʻrash</b>
kauzativsiz deyarli mumkin emas — «qilaman» deyish qoʻpol,
«qilishimga ruxsat bering» esa tabiiy. Ikkinchisi: keyingi
dars (PJ-66) bu shaklning ustiga passivni qoʻyadi va
«majburan qildim» degan maʼnoni chiqaradi. Yaʼni bugungi
shaklni mustahkam oʻzlashtirmasdan ertaga oʻtib boʻlmaydi.</p>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">使</span>
    <span class="pj-kanji__uz">ishlatmoq</span>
    <span class="pj-kanji__on">オン: シ</span>
    <span class="pj-kanji__kun">KUN: つか(う)</span>
    <span class="pj-kanji__note">使役 (しえき) — kauzativ · 使う (つかう) — ishlatmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">許</span>
    <span class="pj-kanji__uz">ruxsat bermoq</span>
    <span class="pj-kanji__on">オン: キョ</span>
    <span class="pj-kanji__kun">KUN: ゆる(す)</span>
    <span class="pj-kanji__note">許す (ゆるす) — kechirmoq, ruxsat bermoq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>言<rt>い</rt></ruby>あせる</p>
  <p class="pe-fix__good">✓ <ruby>言<rt>い</rt></ruby><b>わ</b>せる — う bilan tugagan feʼlda doim わ.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>食<rt>た</rt></ruby>べせる</p>
  <p class="pe-fix__good">✓ <ruby>食<rt>た</rt></ruby><b>べさせる</b> — II guruh <b>させる</b> oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>子<rt>こ</rt></ruby>どもを<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>ませる</p>
  <p class="pe-fix__good">✓ <ruby>子<rt>こ</rt></ruby>ども<b>に</b><ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>ませる — bitta gapda ikkita を boʻlmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>来<rt>き</rt></ruby>させる</p>
  <p class="pe-fix__good">✓ <ruby>来<rt>こ</rt></ruby>させる — ない-oʻzagi <b>こ</b>, xuddi passivdagi kabi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>読<rt>よ</rt></ruby>む ning kauzativ shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>読<rt>よ</rt></ruby>ませる</b> — ない-oʻzagi <ruby>読<rt>よ</rt></ruby>ま, ustiga せる.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>食<rt>た</rt></ruby>べる ning kauzativ shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>食<rt>た</rt></ruby>べさせる</b> — II guruh <b>させる</b> oladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Menga qilishga ruxsat bering» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>私<rt>わたし</rt></ruby>にやらせてください</b> — kauzativning て-shakli + ください.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>子<rt>こ</rt></ruby>ども___<ruby>行<rt>い</rt></ruby>かせました» — ruxsat berganingizni koʻrsatish uchun qaysi qoʻshimcha?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>に</b> — を majburlash ohangini beradi, に esa ruxsat.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «〜させてくれました» qaysi maʼnoni beradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Ruxsat berdi.</b> くれる yaxshilikni bildiradi, va majburlash yaxshilik boʻlmaydi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>使役形<rt>しえきけい</rt></ruby></b> — kauzativ shakl</li>
  <li><b>〜せる / 〜させる</b> — qildirmoq, ruxsat bermoq</li>
  <li><b>〜させてください</b> — …qilishimga ruxsat bering</li>
  <li><b><ruby>許<rt>ゆる</rt></ruby>す</b> — ruxsat bermoq (I guruh)</li>
  <li><b>やる</b> — qilmoq (oddiy shakl, I guruh)</li>
  <li><b><ruby>手伝<rt>てつだ</rt></ruby>う</b> — yordam bermoq (I guruh)</li>
  <li><b><ruby>参加<rt>さんか</rt></ruby>する</b> — qatnashmoq</li>
  <li><b><ruby>留学<rt>りゅうがく</rt></ruby></b> — chet elda oʻqish</li>
  <li><b><ruby>反対<rt>はんたい</rt></ruby>する</b> — qarshi chiqmoq</li>
  <li><b><ruby>決<rt>き</rt></ruby>める</b> — hal qilmoq (II guruh)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Oʻzbekcha <b>«-tir- / -dir-»</b> — qurilma allaqachon sizda bor.</li>
    <li>Bitta shakl, ikki maʼno: <b>majbur</b> yoki <b>ruxsat</b>.</li>
    <li>Oʻtimli feʼlda odam <b>doim に</b> oladi — を band.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-66: Kauzativ-passiv: 行かせられる — majburan",
        "category": "japanese",
        "order": 66,
        "summary": (
            "Kauzativ ustiga passiv qoʻyiladi va «majburan qildim» "
            "chiqadi. Yaponchaning eng uzun feʼl shakli — lekin u "
            "ikkita tanish qoʻshimchaning yigʻindisi, xolos."
        ),
        "stories": ["ピアノの れんしゅう"],
        "content": """
<h2>PJ-66: Kauzativ-passiv: <ruby>行<rt>い</rt></ruby>かせられる — majburan</h2>

<p>Kecha siz «qildirdim» dedingiz. Bugun oʻsha gapni
<b>qildirilgan odamning ogʻzidan</b> aytasiz.</p>

<p><ruby>母<rt>はは</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>にピアノを<ruby>練習<rt>れんしゅう</rt></ruby><b>させました</b>。<br>
<ruby>私<rt>わたし</rt></ruby>は<ruby>母<rt>はは</rt></ruby>にピアノを<ruby>練習<rt>れんしゅう</rt></ruby><b>させられました</b>。</p>

<p>Ikkinchi gap bitta narsani qoʻshadi: <em>men xohlamagan
edim</em>. Bu shakl <b>doim</b> norozilik bildiradi — xuddi
PJ-64 dagi aziyat passivi kabi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Kauzativ-passivni ikki bosqichda yasaysiz</li>
    <li>I guruhning qisqa shaklini (〜される) taniysiz</li>
    <li>す bilan tugagan feʼlda nega qisqa shakl yoʻqligini bilib olasiz</li>
    <li>Qoʻshimchalarni toʻgʻri joylashtirasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Majburan</span>
  <span class="pe-chip pe-chip--s">kauzativ</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">passiv</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--neg">せられる</span>
</div>

<p>Bu shakl yapon tilidagi eng uzun feʼl shakli, va koʻp
oʻquvchi uni koʻrib qoʻrqib ketadi. Qoʻrqmaslikning sababi
bor: <b>u yangi emas</b>. Siz PJ-63 da passivni, PJ-65 da
kauzativni qurgansiz — bugun faqat ikkalasini birga
qoʻyasiz. Va natija ham tanish: u <em>oddiy II guruh
feʼli</em> boʻlib tuslanadi, yaʼni ます, た va ない
shakllarini allaqachon bilasiz.</p>

<h3>1. Ikki bosqichda yasash</h3>

<p>Yangi qoida yoʻq — siz ikkita tanish qoʻshimchani ketma-ket
qoʻyasiz.</p>

<div class="pe-steps">
  <ol>
    <li><b>Kauzativ</b> yasang (PJ-65):
    <ruby>行<rt>い</rt></ruby>く → <ruby>行<rt>い</rt></ruby>か<b>せる</b></li>
    <li>Natija <b>II guruh</b> feʼli boʻlib qoldi
    (せ<b>る</b> bilan tugaydi)</li>
    <li>Unga <b>II guruh passivini</b> qoʻshing (PJ-63):
    せる → せ<b>られる</b></li>
    <li>Natija: <ruby>行<rt>い</rt></ruby>か<b>せられる</b></li>
  </ol>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Kauzativ</th><th>Kauzativ-passiv</th><th>Qisqa shakl</th></tr>
  <tr><td class="pj-stem"><ruby>行<rt>い</rt></ruby>く</td><td class="pj-uz"><ruby>行<rt>い</rt></ruby>かせる</td>
      <td class="pj-end"><ruby>行<rt>い</rt></ruby>かせられる</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>かされる</td></tr>
  <tr><td class="pj-stem"><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-uz"><ruby>読<rt>よ</rt></ruby>ませる</td>
      <td class="pj-end"><ruby>読<rt>よ</rt></ruby>ませられる</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>まされる</td></tr>
  <tr><td class="pj-stem"><ruby>待<rt>ま</rt></ruby>つ</td><td class="pj-uz"><ruby>待<rt>ま</rt></ruby>たせる</td>
      <td class="pj-end"><ruby>待<rt>ま</rt></ruby>たせられる</td><td class="pj-res"><ruby>待<rt>ま</rt></ruby>たされる</td></tr>
  <tr><td class="pj-stem"><ruby>話<rt>はな</rt></ruby>す</td><td class="pj-uz"><ruby>話<rt>はな</rt></ruby>させる</td>
      <td class="pj-end"><ruby>話<rt>はな</rt></ruby>させられる</td><td class="pj-res"><b>yoʻq</b></td></tr>
  <tr><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-uz"><ruby>食<rt>た</rt></ruby>べさせる</td>
      <td class="pj-end"><ruby>食<rt>た</rt></ruby>べさせられる</td><td class="pj-res"><b>yoʻq</b></td></tr>
  <tr><td class="pj-stem">する</td><td class="pj-uz">させる</td>
      <td class="pj-end">させられる</td><td class="pj-res"><b>yoʻq</b></td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Qisqa shakl faqat I guruhda, va す dan tashqari.</b>
  〜せられる → 〜される deb qisqaradi, lekin
  <ruby>話<rt>はな</rt></ruby>す kabi feʼllarda bu
  «<ruby>話<rt>はな</rt></ruby>さされる» boʻlib ketardi — ikkita
  さ ketma-ket. Yapon tili buni qabul qilmaydi, shuning uchun
  す bilan tugagan feʼllar <b>faqat uzun shaklni</b>
  ishlatadi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Qaysi birini yozish kerak?</b> Ikkalasi ham toʻgʻri.
  Qisqa shakl ogʻzaki nutqda koʻproq, uzun shakl yozma va
  rasmiy matnda. Imtihonda ikkalasi ham hisobga olinadi —
  lekin <b>す</b> bilan tugagan feʼlda qisqa shakl
  <em>xato</em>.</p>
</div>

<p>Diqqat qiling: bu shakl uzun boʻlgani uchun qoʻrqinchli
koʻrinadi, aslida esa unda yangi hech narsa yoʻq. Siz
allaqachon kauzativni bilasiz va allaqachon II guruh
passivini bilasiz — bu ikkisini ketma-ket qoʻyish, xolos.
Agar shakl chalkash tuyulsa, uni <em>ikkiga boʻlib</em>
yozib koʻring: <ruby>行<rt>い</rt></ruby>か | せ | られる.
Uch boʻlak, uchtasi ham tanish.</p>

<h3>2. Qoʻshimchalar</h3>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">は<small>MAJBURLANGAN</small></span>
  <span class="pj-joshi__n"><ruby>母<rt>はは</rt></ruby></span>
  <span class="pj-joshi__p">に<small>MAJBURLAGAN</small></span>
  <span class="pj-joshi__n">ピアノ</span>
  <span class="pj-joshi__p">を</span>
  <span class="pj-joshi__v"><ruby>練習<rt>れんしゅう</rt></ruby>させられました</span>
  <span class="pj-joshi__uz">Onam meni pianino mashq qilishga majbur qilardi.</span>
</div>

<div class="pe-call pe-rule">
  <p><b>に — majburlagan odam.</b> Bu PJ-63 va PJ-64 dagi
  qoidaning oʻzi: passiv gapda ishni boshlagan odam doim
  <b>に</b> oladi. Yaʼni siz uchinchi marta bir xil
  qoʻshimchani koʻryapsiz.</p>
</div>

<p>Qisqarish qoidasi bir qarashda gʻalati koʻrinadi, lekin
u aslida talaffuzdan kelib chiqqan. <b>せられ</b> degan
uch boʻgʻinni tez aytish qiyin, shuning uchun til uni
<b>され</b> ga siqib qoʻygan. す bilan tugagan feʼllarda esa
siqish ishlamaydi: oʻzak allaqachon <em>さ</em> bilan
tugaydi, va さされ ikkita bir xil bogʻinni yonma-yon
qoʻyardi. Yapon tili buni yoqtirmaydi — siz buni PJ-43 dagi
sanoq soʻzlarida ham koʻrgansiz.</p>

<h3>3. Maʼnosi doim salbiy</h3>

<p>Bu shakl <b>hech qachon</b> betaraf boʻlmaydi. Uni
ishlatgan odam ishni yoqtirmaganini aytadi — hatto gapda
boshqa hech qanday belgi boʻlmasa ham.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>子<rt>こ</rt></ruby>どものとき、<ruby>毎日<rt>まいにち</rt></ruby>ピアノを<ruby>練習<rt>れんしゅう</rt></ruby>させられました。</p>
  <p class="pe-ex__uz">Bolaligimda har kuni pianino mashq qildirishardi.</p>
  <p class="pe-ex__why">Gapda «yoqmasdi» degan soʻz yoʻq — u <b>feʼlning ichida</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>一時間<rt>いちじかん</rt></ruby><ruby>待<rt>ま</rt></ruby>たされました。</p>
  <p class="pe-ex__uz">Bir soat kuttirishdi.</p>
  <p class="pe-ex__why">Qisqa shakl. «<ruby>待<rt>ま</rt></ruby>ちました» boʻlsa betaraf boʻlardi — «kutdim».</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ham ikki qoʻshimchani ustma-ust qoʻya
  oladi.</b> «Yoz-<b>dir</b>-il-di», «oʻqi-<b>t</b>-il-di» —
  bu yerda ham avval kauzativ, keyin passiv keladi, aynan
  yaponchadagi tartibda. Farq shundaki, oʻzbekcha bu shaklni
  kam ishlatadi va u salbiy ohang olib yurmaydi. Yaponcha esa
  uni har kuni ishlatadi, va u <em>doim</em> shikoyat
  bildiradi. Shuning uchun tarjimada koʻpincha
  <b>«majburan»</b>, <b>«…shga majbur qilishdi»</b> yoki
  <b>«…tirishdi»</b> qoʻshiladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>嫌<rt>きら</rt></ruby>いな<ruby>野菜<rt>やさい</rt></ruby>を<ruby>食<rt>た</rt></ruby>べさせられました。</p>
  <p class="pe-ex__uz">Yoqtirmaydigan sabzavotimni yedirishardi.</p>
  <p class="pe-ex__why">II guruh — qisqa shakl yoʻq, faqat <b>させられる</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «-tir-il-» ham bor, lekin u sovuq.</b>
  «Yozdirildi», «oʻqitildi» — bu shakllar rasmiy hujjatlarda
  uchraydi va hech qanday shikoyat bildirmaydi. Yaponcha
  <b>〜させられる</b> esa aksincha: u deyarli doim
  <em>shaxsiy</em> va <em>norozi</em>. Shuning uchun uni
  oʻzbekchaga oddiy qoʻshimcha bilan emas, <b>«majburan»</b>
  yoki <b>«…tirishardi»</b> degan soʻz bilan tarjima qilish
  toʻgʻriroq.</p>
</div>

<h3>4. Uchtasi bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Kim qiladi</th><th>Ohang</th><th>Misol</th></tr>
  <tr><td class="pj-stem">Passiv (PJ-63)</td><td class="pj-uz">boshqa odam</td>
      <td class="pj-uz">betaraf yoki salbiy</td>
      <td class="pj-res"><ruby>褒<rt>ほ</rt></ruby>められる</td></tr>
  <tr><td class="pj-stem">Aziyat passivi (PJ-64)</td><td class="pj-uz">boshqa odam yoki tabiat</td>
      <td class="pj-uz"><b>doim salbiy</b></td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>られる</td></tr>
  <tr><td class="pj-stem">Kauzativ (PJ-65)</td><td class="pj-uz"><b>men</b> boshlayman</td>
      <td class="pj-uz">majbur yoki ruxsat</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>かせる</td></tr>
  <tr><td class="pj-stem">Kauzativ-passiv</td><td class="pj-uz">boshqa odam boshlaydi, <b>men</b> qilaman</td>
      <td class="pj-uz"><b>doim salbiy</b></td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>かせられる</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Toʻrttasi ham bitta oʻzakdan.</b> PJ-34 da siz
  <ruby>行<rt>い</rt></ruby>か<em>ない</em> deb yozgansiz.
  Oʻsha <b><ruby>行<rt>い</rt></ruby>か</b> oʻzagidan uchta dars chiqdi:
  <ruby>行<rt>い</rt></ruby>か<b>れる</b> · <ruby>行<rt>い</rt></ruby>か<b>せる</b> ·
  <ruby>行<rt>い</rt></ruby>か<b>せられる</b>. Shuning uchun
  agar ない-shaklini yaxshi bilsangiz, bu uch dars ham
  sizniki. Agar bilmasangiz — PJ-34 ga qaytish
  darslarni qaytadan oʻqishdan tezroq.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">練</span>
    <span class="pj-kanji__uz">mashq qilmoq</span>
    <span class="pj-kanji__on">オン: レン</span>
    <span class="pj-kanji__kun">KUN: ね(る)</span>
    <span class="pj-kanji__note">練習 (れんしゅう) — mashq · 訓練 (くんれん) — mashgʻulot</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">無</span>
    <span class="pj-kanji__uz">yoʻq, -siz</span>
    <span class="pj-kanji__on">オン: ム, ブ</span>
    <span class="pj-kanji__kun">KUN: な(い)</span>
    <span class="pj-kanji__note">無理 (むり) — imkonsiz, ortiqcha · 無料 (むりょう) — bepul</span>
  </div>
</div>

<p>Oxirgi bir eslatma: bu shakl yozma matnda kam uchraydi.
Gazeta va ilmiy maqola his-tuygʻu bildirmaydi, shuning uchun
u yerda oddiy passiv turadi. Kauzativ-passiv esa hikoyada,
suhbatda va xotira yozuvlarida yashaydi — yaʼni odam
oʻzi haqida gapirgan joyda.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>話<rt>はな</rt></ruby>さされる</p>
  <p class="pe-fix__good">✓ <ruby>話<rt>はな</rt></ruby>させられる — す bilan tugagan feʼlda qisqa shakl <b>yoʻq</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>食<rt>た</rt></ruby>べさされる</p>
  <p class="pe-fix__good">✓ <ruby>食<rt>た</rt></ruby>べさせられる — II guruhda ham qisqa shakl yoʻq.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>は<ruby>母<rt>はは</rt></ruby><b>が</b>ピアノを<ruby>練習<rt>れんしゅう</rt></ruby>させられました</p>
  <p class="pe-fix__good">✓ <ruby>母<rt>はは</rt></ruby><b>に</b>… — majburlagan odam doim <b>に</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>かせられました = «borishga ruxsat berishdi»</p>
  <p class="pe-fix__good">✓ Bu shakl <b>doim majburlash</b>. Ruxsat uchun — <ruby>行<rt>い</rt></ruby>かせてくれました (PJ-65).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>読<rt>よ</rt></ruby>む ning kauzativ-passiv shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>読<rt>よ</rt></ruby>ませられる</b> (qisqa shakli: <b><ruby>読<rt>よ</rt></ruby>まされる</b>).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>話<rt>はな</rt></ruby>す ning qisqa shakli bormi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> «<ruby>話<rt>はな</rt></ruby>さされる» ikkita さ beradi — yapon tili buni qabul qilmaydi. Faqat <ruby>話<rt>はな</rt></ruby>させられる.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>食<rt>た</rt></ruby>べる ning kauzativ-passiv shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>食<rt>た</rt></ruby>べさせられる</b> — II guruhda qisqa shakl yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>一時間<rt>いちじかん</rt></ruby><ruby>待<rt>ま</rt></ruby>たされました» va «<ruby>一時間<rt>いちじかん</rt></ruby><ruby>待<rt>ま</rt></ruby>ちました» — farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisida <b>norozilik</b> bor — «kuttirishdi». Ikkinchisi betaraf — «kutdim».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bu shakl qaysi oʻzakdan boshlanadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ない-oʻzagidan</b> (PJ-34). Passiv, kauzativ va kauzativ-passiv — uchalasi ham oʻsha oʻzakdan.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>使役受身<rt>しえきうけみ</rt></ruby></b> — kauzativ-passiv</li>
  <li><b>〜せられる / 〜される</b> — majburan qilmoq</li>
  <li><b><ruby>練習<rt>れんしゅう</rt></ruby>する</b> — mashq qilmoq</li>
  <li><b><ruby>無理<rt>むり</rt></ruby></b> — imkonsiz, ortiqcha (な-sifat)</li>
  <li><b><ruby>待<rt>ま</rt></ruby>たされる</b> — kuttirilmoq</li>
  <li><b><ruby>嫌<rt>きら</rt></ruby>い</b> — yoqtirmaydigan (な-sifat)</li>
  <li><b><ruby>今<rt>いま</rt></ruby>になって</b> — endi, hozirga kelib</li>
  <li><b><ruby>感謝<rt>かんしゃ</rt></ruby>する</b> — minnatdor boʻlmoq</li>
  <li><b><ruby>続<rt>つづ</rt></ruby>ける</b> — davom ettirmoq (II guruh)</li>
  <li><b>やめる</b> — tashlamoq, toʻxtatmoq (II guruh)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Kauzativ + passiv — <b>ikkita tanish qoʻshimcha</b>, yangisi yoʻq.</li>
    <li>Qisqa shakl <b>faqat I guruhda</b>, す dan tashqari.</li>
    <li>Maʼnosi <b>doim salbiy</b> — ruxsat uchun 〜させてくれる.</li>
  </ul>
</div>
""",
    },
]
