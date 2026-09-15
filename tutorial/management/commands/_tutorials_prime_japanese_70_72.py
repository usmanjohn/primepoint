# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-70, PJ-71, PJ-72: keigo bloki yopiladi.

PJ-69 suhbatdoshni koʻtargan edi; PJ-70 oʻzini pasaytiradi. Ikkala
mahsuldor qolip bir oʻzakdan yasaladi va bir-biridan faqat oxirgi
boʻlagi bilan farq qiladi:
    お + ます-oʻzak + に なる   ← boshqani koʻtaradi (PJ-69)
    お + ます-oʻzak + する      ← oʻzini pasaytiradi (PJ-70)
Shuning uchun ikkalasi doim yonma-yon koʻrsatiladi.

PJ-71 doʻkondagi tayyor iboralarni beradi, PJ-72 esa butun blokni
boshqarib turgan mantiqni ochadi: うち va そと.

⚠️ Beshta istisno ます shakli (いらっしゃいます…) faqat <ruby>尊敬語<rt>そんけいご</rt></ruby> da.
<ruby>謙譲語<rt>けんじょうご</rt></ruby> feʼllari oddiy: 参ります, 申します, いたします.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_70_72.py --author=prime
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
        "title": "PJ-70: Keigo 3: 謙譲語 — お〜する va oʻzini pastga qoʻyish",
        "category": "japanese",
        "order": 70,
        "summary": (
            "Keigoning ikkinchi tarmogʻi. Bu yerda oʻzbek tili "
            "yordam bermaydi: oʻzbekcha boshqani koʻtaradi, lekin "
            "oʻzini deyarli hech qachon pasaytirmaydi."
        ),
        "stories": ["でんわの こえ"],
        "content": """
<h2>PJ-70: Keigo 3: <ruby>謙譲語<rt>けんじょうご</rt></ruby> — お〜する</h2>

<p>Kecha siz suhbatdoshni koʻtardingiz. Bugun <b>oʻzingizni
pasaytirasiz</b> — va natija bir xil boʻladi: orangizdagi
masofa ochiladi.</p>

<p>Ikkala mahsuldor qolip bir-biriga juda oʻxshaydi, shuning
uchun ularni darrov yonma-yon qoʻyamiz:</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h"><ruby>尊敬語<rt>そんけいご</rt></ruby> (PJ-69)</p>
    <p>お<ruby>待<rt>ま</rt></ruby>ち<b>になる</b></p>
    <p>«Siz kutasiz» — boshqani koʻtaradi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h"><ruby>謙譲語<rt>けんじょうご</rt></ruby> (bugun)</p>
    <p>お<ruby>待<rt>ま</rt></ruby>ち<b>する</b></p>
    <p>«Men kutaman» — oʻzini pasaytiradi.</p></div>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>お〜する qolipini yasaysiz</li>
    <li>Xitoycha oʻzakli feʼllarga ご qoʻyasiz</li>
    <li>Maxsus <ruby>謙譲語<rt>けんじょうご</rt></ruby> feʼllarini yodlaysiz</li>
    <li>Nega bu tarmoq oʻzbek oʻquvchisiga eng notanish ekanini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻzini pasaytirish</span>
  <span class="pe-chip pe-chip--s">お</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">ます-oʻzak</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">する</span>
</div>

<p>Bir narsani boshda aytib qoʻyish kerak, chunki u bu
darsni ancha yengillashtiradi: <b>siz bu tarmoqning bir
qismini allaqachon bilasiz</b>. いただきます —
<ruby>謙譲語<rt>けんじょうご</rt></ruby> (PJ-60).
よろしくお<ruby>願<rt>ねが</rt></ruby>いします — ham shu.
Yaʼni siz bu shakllarni ibora sifatida yodlagansiz; bugun
faqat ularning <em>qoidasi</em>ni koʻrasiz.</p>

<h3>1. Qolip: お + ます-oʻzak + する</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>ます-oʻzagi</th><th><ruby>謙譲語<rt>けんじょうご</rt></ruby></th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem"><ruby>待<rt>ま</rt></ruby>つ</td><td class="pj-end"><ruby>待<rt>ま</rt></ruby>ち</td>
      <td class="pj-res">お<ruby>待<rt>ま</rt></ruby>ちします</td><td class="pj-uz">kutaman</td></tr>
  <tr><td class="pj-stem"><ruby>持<rt>も</rt></ruby>つ</td><td class="pj-end"><ruby>持<rt>も</rt></ruby>ち</td>
      <td class="pj-res">お<ruby>持<rt>も</rt></ruby>ちします</td><td class="pj-uz">koʻtarib beraman</td></tr>
  <tr><td class="pj-stem"><ruby>送<rt>おく</rt></ruby>る</td><td class="pj-end"><ruby>送<rt>おく</rt></ruby>り</td>
      <td class="pj-res">お<ruby>送<rt>おく</rt></ruby>りします</td><td class="pj-uz">yuboraman, kuzataman</td></tr>
  <tr><td class="pj-stem"><ruby>伝<rt>つた</rt></ruby>える</td><td class="pj-end"><ruby>伝<rt>つた</rt></ruby>え</td>
      <td class="pj-res">お<ruby>伝<rt>つた</rt></ruby>えします</td><td class="pj-uz">yetkazaman</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Ikki qolip bir-biridan faqat oxiri bilan farq qiladi.</b>
  お<ruby>待<rt>ま</rt></ruby>ち<b>になる</b> va
  お<ruby>待<rt>ま</rt></ruby>ち<b>する</b> — boshi bir xil, oxiri
  boshqa. Shuning uchun ularni <em>alohida</em> yodlamang;
  bitta jadvalda, yonma-yon yodlang. Adashishning yagona sababi
  — ularni ikki xil darsda koʻrish.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Kamtarroq shakli — お〜いたす.</b>
  お<ruby>待<rt>ま</rt></ruby>ち<b>いたします</b> — ish joyida va
  mijoz bilan aynan shu eshitiladi. する oʻrniga いたす
  qoʻyiladi, xolos.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Ikki qolipni ajratishning oʻzbekcha yoʻli bor.</b>
  お〜<b>になる</b> ni «qilib turadilar» deb, お〜<b>する</b> ni
  «qilib beray» deb oʻqib koʻring. «Kutib turadilar» —
  boshqaning ishi; «kutib beray» — meniki. Oʻzbekcha bu ikki
  ohangni aniq ajratadi, va agar shakl tanlashda ikkilansangiz,
  gapni avval oʻzbekcha shu ikki koʻrinishda aytib koʻring —
  javob oʻzi chiqadi.</p>
</div>

<h3>2. Xitoycha oʻzakli feʼllar: ご + ot + する</h3>

<p><ruby>案内<rt>あんない</rt></ruby>する,
<ruby>説明<rt>せつめい</rt></ruby>する kabi feʼllar
<b>ご</b> oladi — PJ-69 dagi お / ご qoidasining oʻzi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th><ruby>謙譲語<rt>けんじょうご</rt></ruby></th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem"><ruby>案内<rt>あんない</rt></ruby>する</td>
      <td class="pj-res">ご<ruby>案内<rt>あんない</rt></ruby>します</td><td class="pj-uz">yoʻl koʻrsataman</td></tr>
  <tr><td class="pj-stem"><ruby>説明<rt>せつめい</rt></ruby>する</td>
      <td class="pj-res">ご<ruby>説明<rt>せつめい</rt></ruby>します</td><td class="pj-uz">tushuntiraman</td></tr>
  <tr><td class="pj-stem"><ruby>連絡<rt>れんらく</rt></ruby>する</td>
      <td class="pj-res">ご<ruby>連絡<rt>れんらく</rt></ruby>します</td><td class="pj-uz">xabar beraman</td></tr>
  <tr><td class="pj-stem"><ruby>紹介<rt>しょうかい</rt></ruby>する</td>
      <td class="pj-res">ご<ruby>紹介<rt>しょうかい</rt></ruby>します</td><td class="pj-uz">tanishtiraman</td></tr>
</table></div>

<p>Diqqat qiling: bu qolip <b>har qanday feʼlga
qoʻyilmaydi</b>. U faqat suhbatdoshga <em>tegadigan</em>
ishlar uchun: kutish, koʻtarish, yuborish, yetkazish.
«Uxlayman», «yuguraman» kabi feʼllarga お〜する qoʻyilsa,
gap kulgili chiqadi — chunki mening uxlashim
suhbatdoshga hech qanday aloqasi yoʻq. Bu qoidani
keyingi boʻlimda yana koʻrasiz.</p>

<h3>3. Maxsus feʼllar</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oddiy feʼl</th><th><ruby>謙譲語<rt>けんじょうご</rt></ruby></th><th>ます shakli</th></tr>
  <tr><td class="pj-stem"><ruby>行<rt>い</rt></ruby>く · <ruby>来<rt>く</rt></ruby>る</td>
      <td class="pj-end"><ruby>参<rt>まい</rt></ruby>る</td><td class="pj-res"><ruby>参<rt>まい</rt></ruby>ります</td></tr>
  <tr><td class="pj-stem">いる</td>
      <td class="pj-end">おる</td><td class="pj-res">おります</td></tr>
  <tr><td class="pj-stem"><ruby>言<rt>い</rt></ruby>う</td>
      <td class="pj-end"><ruby>申<rt>もう</rt></ruby>す</td><td class="pj-res"><ruby>申<rt>もう</rt></ruby>します</td></tr>
  <tr><td class="pj-stem">する</td>
      <td class="pj-end">いたす</td><td class="pj-res">いたします</td></tr>
  <tr><td class="pj-stem"><ruby>見<rt>み</rt></ruby>る</td>
      <td class="pj-end"><ruby>拝見<rt>はいけん</rt></ruby>する</td><td class="pj-res"><ruby>拝見<rt>はいけん</rt></ruby>します</td></tr>
  <tr><td class="pj-stem"><ruby>聞<rt>き</rt></ruby>く · <ruby>訪<rt>たず</rt></ruby>ねる</td>
      <td class="pj-end"><ruby>伺<rt>うかが</rt></ruby>う</td><td class="pj-res"><ruby>伺<rt>うかが</rt></ruby>います</td></tr>
  <tr><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べる · もらう</td>
      <td class="pj-end">いただく</td><td class="pj-res">いただきます</td></tr>
  <tr><td class="pj-stem"><ruby>会<rt>あ</rt></ruby>う</td>
      <td class="pj-end">お<ruby>目<rt>め</rt></ruby>にかかる</td><td class="pj-res">お<ruby>目<rt>め</rt></ruby>にかかります</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Va mana yaxshi xabar: bu feʼllar ます da istisno
  emas.</b> PJ-69 dagi beshtasi り → い qilgan edi
  (いらっしゃ<b>い</b>ます). Bu yerda esa hammasi oddiy:
  <ruby>参<rt>まい</rt></ruby>り<b>ます</b>,
  <ruby>申<rt>もう</rt></ruby>し<b>ます</b>, いたし<b>ます</b>.
  Yaʼni <ruby>謙譲語<rt>けんじょうご</rt></ruby> ni yodlash
  <ruby>尊敬語<rt>そんけいご</rt></ruby> dan <em>osonroq</em>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">ラノと<ruby>申<rt>もう</rt></ruby>します。よろしくお<ruby>願<rt>ねが</rt></ruby>いいたします。</p>
  <p class="pe-ex__uz">Rano deb ataladi kaminaning ismi. Tanishganimizdan xursandman.</p>
  <p class="pe-ex__why">Yaponiyada rasmiy tanishuvning standart gapi. <ruby>申<rt>もう</rt></ruby>す — «aytmoq» ning kamtar shakli.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">お<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>拝見<rt>はいけん</rt></ruby>しました。</p>
  <p class="pe-ex__uz">Suratingizni koʻrdim.</p>
  <p class="pe-ex__why">Koʻrish — mening ishim, shuning uchun kamtar shakl. Mijozning koʻrishi esa ご<ruby>覧<rt>らん</rt></ruby>になる (PJ-69).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>明日<rt>あした</rt></ruby>、そちらに<ruby>伺<rt>うかが</rt></ruby>います。</p>
  <p class="pe-ex__uz">Ertaga siznikiga boraman.</p>
  <p class="pe-ex__why"><ruby>伺<rt>うかが</rt></ruby>う bitta soʻzda uchta maʼnoni koʻtaradi: soʻramoq, eshitmoq, tashrif buyurmoq.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham «arz qilaman» degan ibora bor.</b>
  «Arz qilmoqchi edim», «ijozat bersangiz aytib oʻtsam» —
  bu qurilmalar ham oʻzingizni bir pogʻona pastga
  qoʻyadi. Farqi shundaki, oʻzbekchada ular
  <em>tanlov</em>: xohlasangiz ishlatasiz, xohlamasangiz
  yoʻq. Yaponchada esa ish joyida bu tanlov emas —
  ishlatmasangiz, gap notoʻgʻri boʻladi. Shuning uchun bu
  darsdagi soʻzlarni <b>vaziyat bilan birga</b> yodlang:
  telefon, ish suhbati, mijoz.</p>
</div>

<p>Bu jadvaldagi soʻzlarning koʻpi kundalik nutqda
uchramaydi — va bu normal. Ular ish joyining, telefonning
va rasmiy xatning tili. Talaba sifatida sizga ulardan
ikkitasi yetadi: <ruby>申<rt>もう</rt></ruby>します (ismni
aytish) va いたします (よろしくお<ruby>願<rt>ねが</rt></ruby>い
いたします ichida). Qolganini <b>tanib olsangiz</b> kifoya.</p>

<h3>4. Nega bu tarmoq eng notanish</h3>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tili boshqani koʻtaradi, lekin oʻzini
  pasaytirmaydi.</b> «Keldilar», «aytdilar», «tashrif
  buyurdilar» — bularning hammasi
  <ruby>尊敬語<rt>そんけいご</rt></ruby> tomonida. Oʻzingizni
  pasaytiradigan shakl esa oʻzbekchada deyarli yoʻq:
  «kamina», «bandangiz» — bu soʻzlar bor, lekin ular
  <em>kitobiy</em> va kundalik nutqda eshitilmaydi. Yaponchada
  aksincha: <ruby>申<rt>もう</rt></ruby>します va いたします ish
  joyida har kuni, har soatda ishlatiladi. Shuning uchun bu
  dars butun kursdagi eng «begona» dars — va uni tarjima
  orqali emas, <b>vaziyat orqali</b> oʻrganish kerak.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Qoida oʻsha-oʻsha:</b>
  <ruby>謙譲語<rt>けんじょうご</rt></ruby> <em>faqat mening</em>
  ishimga qoʻyiladi. «お<ruby>客<rt>きゃく</rt></ruby>さまが
  <ruby>参<rt>まい</rt></ruby>ります» — notoʻgʻri va qoʻpol;
  mijoz uchun いらっしゃいます.</p>
</div>

<p>Bu roʻyxatni yodlashning eng oson yoʻli — uni
<em>vaziyat</em> bilan bogʻlash. Telefon koʻtarganda
<ruby>申<rt>もう</rt></ruby>します; ish suhbatida
いたします; mijozga xizmat qilganda
お<ruby>持<rt>も</rt></ruby>ちします; birovnikiga
borganda <ruby>伺<rt>うかが</rt></ruby>います. Yaʼni bu
soʻzlar lugʻat emas, <b>ssenariy</b>: har biri oʻz
sahnasiga biriktirilgan.</p>

<h3>5. Qachon kerak</h3>

<p>Bitta amaliy tekshiruv bor:
<b>mening ishim suhbatdoshga tegadimi?</b> Tegsa —
<ruby>謙譲語<rt>けんじょうご</rt></ruby>. Tegmasa — oddiy
<ruby>丁寧語<rt>ていねいご</rt></ruby> yetadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Gap</th><th>Suhbatdoshga tegadimi</th><th>Shakl</th></tr>
  <tr><td class="pj-stem">Sizni kutaman</td><td class="pj-uz">ha</td>
      <td class="pj-res">お<ruby>待<rt>ま</rt></ruby>ちします</td></tr>
  <tr><td class="pj-stem">Sumkangizni koʻtaraman</td><td class="pj-uz">ha</td>
      <td class="pj-res">お<ruby>持<rt>も</rt></ruby>ちします</td></tr>
  <tr><td class="pj-stem">Kecha kino koʻrdim</td><td class="pj-uz">yoʻq</td>
      <td class="pj-res"><ruby>見<rt>み</rt></ruby>ました</td></tr>
  <tr><td class="pj-stem">Har kuni yuguraman</td><td class="pj-uz">yoʻq</td>
      <td class="pj-res"><ruby>走<rt>はし</rt></ruby>っています</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Shuning uchun keigo suhbatning hamma joyida
  boʻlmaydi.</b> Siz mijoz bilan gapirsangiz ham, oʻz
  hordigʻingiz haqidagi gapga
  <ruby>謙譲語<rt>けんじょうご</rt></ruby> qoʻyilmaydi. Keigo —
  <em>munosabat</em>ning tili, tarjimai holning emas.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">申</span>
    <span class="pj-kanji__uz">aytmoq (kamtar)</span>
    <span class="pj-kanji__on">オン: シン</span>
    <span class="pj-kanji__kun">KUN: もう(す)</span>
    <span class="pj-kanji__note">申す (もうす) — aytmoq · 申し込む (もうしこむ) — ariza bermoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">伺</span>
    <span class="pj-kanji__uz">soʻramoq, bormoq (kamtar)</span>
    <span class="pj-kanji__on">オン: シ</span>
    <span class="pj-kanji__kun">KUN: うかが(う)</span>
    <span class="pj-kanji__note">伺う (うかがう) — soʻramoq, eshitmoq, tashrif buyurmoq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ お<ruby>客<rt>きゃく</rt></ruby>さまがお<ruby>待<rt>ま</rt></ruby>ちします</p>
  <p class="pe-fix__good">✓ お<ruby>客<rt>きゃく</rt></ruby>さまがお<ruby>待<rt>ま</rt></ruby>ち<b>になります</b> — mijozning ishi <ruby>尊敬語<rt>そんけいご</rt></ruby> oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>がお<ruby>待<rt>ま</rt></ruby>ちになります</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby>がお<ruby>待<rt>ま</rt></ruby>ち<b>します</b> — mening ishim <ruby>謙譲語<rt>けんじょうご</rt></ruby> oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ お<ruby>案内<rt>あんない</rt></ruby>します</p>
  <p class="pe-fix__good">✓ <b>ご</b><ruby>案内<rt>あんない</rt></ruby>します — xitoycha oʻzakli feʼl <b>ご</b> oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>参<rt>まい</rt></ruby>いります</p>
  <p class="pe-fix__good">✓ <ruby>参<rt>まい</rt></ruby>ります — <ruby>謙譲語<rt>けんじょうご</rt></ruby> feʼllari ます da <b>istisno emas</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>持<rt>も</rt></ruby>つ ni お〜する qolipiga qoʻying.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>お<ruby>持<rt>も</rt></ruby>ちします</b> — ます-oʻzagi <ruby>持<rt>も</rt></ruby>ち.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>案内<rt>あんない</rt></ruby>する ni kamtar shaklga qoʻying.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ご<ruby>案内<rt>あんない</rt></ruby>します</b> — xitoycha oʻzak, demak <b>ご</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Rasmiy tanishuvda ismingizni qanday aytasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ラノと<ruby>申<rt>もう</rt></ruby>します</b> — <ruby>言<rt>い</rt></ruby>います emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Kecha kino koʻrdim» ga <ruby>謙譲語<rt>けんじょうご</rt></ruby> kerakmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yoʻq. Bu ish <b>suhbatdoshga tegmaydi</b>, demak oddiy <ruby>見<rt>み</rt></ruby>ました yetadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>参<rt>まい</rt></ruby>る ning ます shakli istisnomi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yoʻq — <b><ruby>参<rt>まい</rt></ruby>ります</b>, oddiy qoida. Beshta istisno faqat <ruby>尊敬語<rt>そんけいご</rt></ruby> da.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>お〜する / お〜いたす</b> — kamtar qolip</li>
  <li><b>ご〜する</b> — xitoycha oʻzakli feʼllar uchun</li>
  <li><b><ruby>参<rt>まい</rt></ruby>る</b> — bormoq, kelmoq</li>
  <li><b>おる</b> — boʻlmoq</li>
  <li><b><ruby>申<rt>もう</rt></ruby>す</b> — aytmoq</li>
  <li><b>いたす</b> — qilmoq</li>
  <li><b><ruby>拝見<rt>はいけん</rt></ruby>する</b> — koʻrmoq</li>
  <li><b><ruby>伺<rt>うかが</rt></ruby>う</b> — soʻramoq, tashrif buyurmoq</li>
  <li><b>お<ruby>目<rt>め</rt></ruby>にかかる</b> — uchrashmoq</li>
  <li><b>よろしくお<ruby>願<rt>ねが</rt></ruby>いいたします</b> — tanishganimdan xursandman</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>お〜<b>になる</b> (boshqa) ↔ お〜<b>する</b> (men) — faqat oxiri farq qiladi.</li>
    <li><ruby>謙譲語<rt>けんじょうご</rt></ruby> feʼllari ます da <b>istisno emas</b>.</li>
    <li>Ish suhbatdoshga <b>tegmasa</b>, keigo kerak emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-71: Keigo 4: 丁寧語, ございます va doʻkondagi yapon tili",
        "category": "japanese",
        "order": 71,
        "summary": (
            "Keigo blokining eng amaliy darsi. Doʻkondagi yaponcha "
            "yasalmaydi — u yodlanadi, chunki u tayyor bloklardan "
            "iborat. Va siz uni Yaponiyada birinchi kuniyoq eshitasiz."
        ),
        "stories": ["コンビニの ことば"],
        "content": """
<h2>PJ-71: Keigo 4: <ruby>丁寧語<rt>ていねいご</rt></ruby>, ございます va doʻkondagi yapon tili</h2>

<p>Oldingi ikki dars qiyin edi: siz kimning ishi ekanini
hisoblab, keyin shakl tanlardingiz. Bugungi dars boshqacha —
va ancha oson.</p>

<p>Chunki <b>doʻkondagi yaponcha yasalmaydi. U yodlanadi.</b>
Yaponiyadagi har bir doʻkonda, har bir kassada siz
<em>aynan bir xil</em> gaplarni eshitasiz. Ular tayyor
bloklar, va ularni grammatika sifatida emas, <b>ibora</b>
sifatida oʻrganish kerak.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ございます ni tushunasiz va ishlatasiz</li>
    <li>Doʻkondagi oʻnta asosiy iborani yodlaysiz</li>
    <li>ませ nima ekanini bilib olasiz</li>
    <li>«Bayt keigo» — notoʻgʻri, lekin hamma joyda uchraydigan shakllarni taniysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Eng muloyim boglama</span>
  <span class="pe-chip pe-chip--s">です</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">でございます</span>
</div>

<h3>1. ございます — ある va です ning muloyim shakli</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oddiy</th><th><ruby>丁寧語<rt>ていねいご</rt></ruby></th><th>Eng muloyim</th></tr>
  <tr><td class="pj-stem">ある</td><td class="pj-uz">あります</td>
      <td class="pj-res">ございます</td></tr>
  <tr><td class="pj-stem">だ</td><td class="pj-uz">です</td>
      <td class="pj-res">でございます</td></tr>
  <tr><td class="pj-stem">ない</td><td class="pj-uz">ありません</td>
      <td class="pj-res">ございません</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">こちらが<ruby>新<rt>しん</rt></ruby><ruby>商品<rt>しょうひん</rt></ruby>でございます。</p>
  <p class="pe-ex__uz">Mana bu yangi mahsulot.</p>
  <p class="pe-ex__why">です ning oʻrnida でございます. Maʼno bir xil — masofa boshqa.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>ございます — <ruby>丁寧語<rt>ていねいご</rt></ruby>, yaʼni
  uchinchi tarmoq.</b> U kimningdir ishini koʻtarmaydi va
  hech kimni pasaytirmaydi — u shunchaki butun gapga eng
  qalin kiyimni kiydiradi. Shuning uchun uni narsalar va
  faktlar haqida ham ishlatsa boʻladi:
  お<ruby>手洗<rt>てあら</rt></ruby>いは<ruby>二階<rt>にかい</rt></ruby>にございます.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>ございます — PJ-69 dagi beshinchi istisno.</b>
  Uning lugʻat shakli ござる, va oddiy qoida «ござります»
  berardi. Lekin り → い: <b>ございます</b>. Shu beshta feʼl
  bitta guruh: いらっしゃる, なさる, おっしゃる, くださる,
  ござる.</p>
</div>

<p>Bu uch pogʻonani bir gapda aralashtirmaslik kerak.
です bilan boshlab でございます bilan tugatgan gap notekis
eshitiladi — xuddi PJ-69 dagi uch yoʻlni aralashtirgandek.
Doʻkonda ishlaydigan odam butun smenasi davomida bir
darajada qoladi, va bu mashq bilan keladi.</p>

<h3>2. Doʻkondagi oʻnta ibora</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Ibora</th><th>Qachon</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">いらっしゃいませ</td><td class="pj-uz">kirganda</td>
      <td class="pj-res">xush kelibsiz</td></tr>
  <tr><td class="pj-stem"><ruby>少々<rt>しょうしょう</rt></ruby>お<ruby>待<rt>ま</rt></ruby>ちください</td>
      <td class="pj-uz">kutish kerak boʻlganda</td><td class="pj-res">bir oz kuting</td></tr>
  <tr><td class="pj-stem">かしこまりました</td><td class="pj-uz">buyurtma qabul qilinganda</td>
      <td class="pj-res">tushundim, boʻladi</td></tr>
  <tr><td class="pj-stem"><ruby>申<rt>もう</rt></ruby>し<ruby>訳<rt>わけ</rt></ruby>ございません</td>
      <td class="pj-uz">uzr soʻraganda</td><td class="pj-res">kechirasiz (juda rasmiy)</td></tr>
  <tr><td class="pj-stem">ありがとうございました</td><td class="pj-uz">chiqayotganda</td>
      <td class="pj-res">rahmat</td></tr>
  <tr><td class="pj-stem">またお<ruby>越<rt>こ</rt></ruby>しくださいませ</td>
      <td class="pj-uz">xayrlashganda</td><td class="pj-res">yana keling</td></tr>
  <tr><td class="pj-stem">こちらでございます</td><td class="pj-uz">koʻrsatganda</td>
      <td class="pj-res">mana shu</td></tr>
  <tr><td class="pj-stem">お<ruby>会計<rt>かいけい</rt></ruby>は〜でございます</td>
      <td class="pj-uz">narx aytganda</td><td class="pj-res">hisobingiz …</td></tr>
  <tr><td class="pj-stem">レシートでございます</td><td class="pj-uz">chek berganda</td>
      <td class="pj-res">mana chek</td></tr>
  <tr><td class="pj-stem">おつりでございます</td><td class="pj-uz">qaytim berganda</td>
      <td class="pj-res">mana qaytim</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham doʻkon tili tayyor bloklardan
  iborat.</b> «Xush kelibsiz», «marhamat», «xizmat»,
  «yana keling», «sogʻ boʻling» — siz bularni <em>yasamaysiz</em>,
  ularni butunligicha aytasiz, va har bir doʻkonda bir xil
  eshitasiz. Yaponcha ham xuddi shunday, faqat u yerda bu
  bloklar ancha koʻp va ancha uzun. Shuning uchun bu darsni
  grammatika kabi emas, <b>lugʻat kabi</b> oʻrganing —
  har bir iborani butunligicha yodlang.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">お<ruby>手洗<rt>てあら</rt></ruby>いは<ruby>二階<rt>にかい</rt></ruby>にございます。</p>
  <p class="pe-ex__uz">Hojatxona ikkinchi qavatda.</p>
  <p class="pe-ex__why">ございます narsalar haqida ham ishlatiladi — u hech kimni koʻtarmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham «bor» ning muloyim shakli yoʻq.</b>
  «Bor» — «mavjud» — «hozir» degan soʻzlar bir-biridan
  uslub bilan farq qiladi, lekin ularning hech biri
  <em>grammatik</em> daraja emas. Yaponchada esa
  ある → あります → ございます aniq uch pogʻona, va uchinchisi
  faqat xizmat koʻrsatishda chiqadi. Shuning uchun
  ございます eshitsangiz, darrov bilasiz: siz mijozsiz.</p>
</div>

<h3>3. ませ nima?</h3>

<p>いらっしゃい<b>ませ</b>, ください<b>ませ</b> —
bu <b>ませ</b> qayerdan kelgan?</p>

<div class="pj-say">
  <span class="pj-say__from">ます</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">ませ</span>
  <span class="pj-say__why">ます ning buyruq shakli (PJ-67 dagi え-qator)</span>
</div>

<div class="pe-call pe-rule">
  <p><b>Yaʼni ませ — buyruq shakli.</b> Lekin u qoʻpol emas,
  aksincha: eng muloyim taklif shakli. Sababi u faqat
  <em>mijozga</em> qaratilgan tayyor iboralarda qoladi va
  boshqa hech qayerda ishlatilmaydi. PJ-67, PJ-69 va bugun
  bir joyda uchrashdi.</p>
</div>

<h3>4. «Bayt keigo» — hamma joyda, lekin tanqid ostida</h3>

<p>Doʻkonlarda tez-tez eshitiladigan uchta shakl bor.
Ular <em>rasmiy jihatdan notoʻgʻri</em> hisoblanadi, lekin
amalda hamma ishlatadi. Ularni <b>taniy olish</b> kerak —
gapirish shart emas.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Eshitiladigan shakl</th><th>Muammo</th><th>Toʻgʻrisi</th></tr>
  <tr><td class="pj-stem">コーヒーのほうをお<ruby>持<rt>も</rt></ruby>ちしました</td>
      <td class="pj-uz">のほう bu yerda hech nimani taqqoslamaydi</td>
      <td class="pj-res">コーヒーをお<ruby>持<rt>も</rt></ruby>ちしました</td></tr>
  <tr><td class="pj-stem"><ruby>千円<rt>せんえん</rt></ruby>になります</td>
      <td class="pj-uz">narx «boʻlmaydi» — u shunchaki shu</td>
      <td class="pj-res"><ruby>千円<rt>せんえん</rt></ruby>でございます</td></tr>
  <tr><td class="pj-stem">よろしかったでしょうか</td>
      <td class="pj-uz">hozirgi ish uchun oʻtgan zamon</td>
      <td class="pj-res">よろしいでしょうか</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Nega bunday boʻlgan?</b> Chunki bu shakllar
  <em>uzunroq</em>, va yaponchada uzunlik muloyimlik bilan
  bogʻliq (PJ-61, PJ-67). Xodimlar muloyimroq boʻlishga
  urinib, gapni choʻzishgan. Til olimlari qarshi, mijozlar
  esa eʼtibor bermaydi — shuning uchun bu shakllar qolgan.</p>
</div>

<p>Bu iboralarning yana bir foydasi bor: ular
<b>butun blokning takroriy mashqi</b>. いらっしゃいませ
ichida PJ-69 dagi maxsus feʼl bor;
お<ruby>待<rt>ま</rt></ruby>ちください ichida PJ-70 dagi お-qolipi;
くださいませ ichida PJ-67 dagi buyruq shakli; ございます
ichida esa beshta istisnodan biri. Yaʼni oʻnta iborani
yodlagan odam toʻrtta darsning grammatikasini ham
takrorlab chiqadi.</p>

<h3>5. Nima uchun bu dars amaliy</h3>

<div class="pe-ex">
  <p class="pe-ex__ja">いらっしゃいませ。<ruby>少々<rt>しょうしょう</rt></ruby>お<ruby>待<rt>ま</rt></ruby>ちください。</p>
  <p class="pe-ex__uz">Xush kelibsiz. Bir oz kuting.</p>
  <p class="pe-ex__why">Bu ikki gapni Yaponiyada birinchi kuningizdayoq oʻn marta eshitasiz.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu blokning haqiqiy maqsadi shu yerda koʻrinadi.</b>
  PJ-68 da aytilgan edi: keigoni <em>gapirish</em> uchun emas,
  <b>eshitganini tushunish</b> uchun oʻrganasiz. Doʻkonda
  sizdan hech kim keigo kutmaydi — siz «ありがとう» desangiz
  ham boʻladi. Lekin xodim sizga
  «<ruby>少々<rt>しょうしょう</rt></ruby>お<ruby>待<rt>ま</rt></ruby>ち
  ください» desa va siz tushunmasangiz, muloqot toʻxtaydi.
  Shuning uchun bu oʻn ibora butun keigo blokidagi eng
  foydali oʻn qator.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">越</span>
    <span class="pj-kanji__uz">oʻtmoq, kelmoq</span>
    <span class="pj-kanji__on">オン: エツ</span>
    <span class="pj-kanji__kun">KUN: こ(す), こ(える)</span>
    <span class="pj-kanji__note">お越しください — «keling» (juda muloyim)</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">訳</span>
    <span class="pj-kanji__uz">tarjima; sabab</span>
    <span class="pj-kanji__on">オン: ヤク</span>
    <span class="pj-kanji__kun">KUN: わけ</span>
    <span class="pj-kanji__note">申し訳ございません — «uzr» · 翻訳 (ほんやく) — tarjima</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ござります</p>
  <p class="pe-fix__good">✓ ござ<b>い</b>ます — beshta istisno feʼldan biri.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ありがとうございました = «rahmat edi»</p>
  <p class="pe-fix__good">✓ Oʻtgan zamon <b>ish tugaganini</b> bildiradi: xarid boʻldi, xizmat tugadi. Bu tabiiy.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>千円<rt>せんえん</rt></ruby>になります (yozma ishda)</p>
  <p class="pe-fix__good">✓ <ruby>千円<rt>せんえん</rt></ruby>でございます — narx «boʻlmaydi», u shunchaki shu.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ませ ni boshqa feʼllarga qoʻshish: <ruby>食<rt>た</rt></ruby>べませ</p>
  <p class="pe-fix__good">✓ ませ faqat tayyor iboralarda qoladi: いらっしゃいませ, くださいませ.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. です ning eng muloyim shakli qaysi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>でございます</b> — <ruby>丁寧語<rt>ていねいご</rt></ruby> ning eng qalin kiyimi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Doʻkonga kirdingiz. Nima eshitasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>いらっしゃいませ</b> — Yaponiyadagi har bir doʻkonda aynan shu.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. ませ qayerdan kelgan?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ます ning buyruq shakli</b> (PJ-67 dagi え-qator). Lekin u qoʻpol emas — u faqat tayyor iboralarda qolgan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>千円<rt>せんえん</rt></ruby>になります» nega tanqid qilinadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki narx <b>«boʻlmaydi»</b> — u shunchaki shu. Toʻgʻrisi — <ruby>千円<rt>せんえん</rt></ruby>でございます.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bu darsning amaliy maqsadi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Eshitganini tushunish.</b> Sizdan keigo kutilmaydi, lekin xodimning gapini tushunmasangiz muloqot toʻxtaydi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ございます</b> — ある / です ning eng muloyim shakli</li>
  <li><b>いらっしゃいませ</b> — xush kelibsiz</li>
  <li><b><ruby>少々<rt>しょうしょう</rt></ruby>お<ruby>待<rt>ま</rt></ruby>ちください</b> — bir oz kuting</li>
  <li><b>かしこまりました</b> — tushundim, boʻladi</li>
  <li><b><ruby>申<rt>もう</rt></ruby>し<ruby>訳<rt>わけ</rt></ruby>ございません</b> — kechirasiz</li>
  <li><b>またお<ruby>越<rt>こ</rt></ruby>しくださいませ</b> — yana keling</li>
  <li><b>お<ruby>会計<rt>かいけい</rt></ruby></b> — hisob</li>
  <li><b>おつり</b> — qaytim</li>
  <li><b><ruby>商品<rt>しょうひん</rt></ruby></b> — mahsulot</li>
  <li><b>コンビニ</b> — doimiy ishlaydigan kichik doʻkon</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Doʻkondagi yaponcha <b>yasalmaydi — yodlanadi</b>.</li>
    <li>ございます — ある va です ning eng muloyim shakli.</li>
    <li>Maqsad — <b>eshitganini tushunish</b>, gapirish emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-72: うちとそと — ichki va tashqi guruh",
        "category": "japanese",
        "order": 72,
        "summary": (
            "Keigo blokining kaliti. Yapon tili odamlarni ikki "
            "doiraga boʻladi, va chegara suhbatdoshga qarab "
            "SILJIYDI — shuning uchun otangiz ikki xil ataladi."
        ),
        "stories": ["ちちと おとうさん"],
        "content": """
<h2>PJ-72: <ruby>内<rt>うち</rt></ruby>と<ruby>外<rt>そと</rt></ruby> — ichki va tashqi guruh</h2>

<p>Uch dars davomida siz shakllarni oʻrgandingiz. Bugun
ularni <b>boshqarib turgan mantiq</b>ni koʻrasiz — va u
keigoning yarmini oʻz-oʻzidan tushuntirib beradi.</p>

<p>Yapon tili odamlarni ikkiga boʻladi:</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h"><ruby>内<rt>うち</rt></ruby> — ICHKARI</p>
    <p>Men, oilam, sinfim, ishxonam.</p>
    <p>Ularni <b>pasaytiraman</b>.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h"><ruby>外<rt>そと</rt></ruby> — TASHQARI</p>
    <p>Mijoz, begona, boshqa kompaniya.</p>
    <p>Ularni <b>koʻtaraman</b>.</p></div>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Chegara qayerda turishini bilib olasiz</li>
    <li>Chegaraning <b>siljishini</b> koʻrasiz</li>
    <li>Oila aʼzolarining ikki xil nomini oʻrganasiz</li>
    <li>Nega boshligʻingizni pasaytirishingizni tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta qoida</span>
  <span class="pe-chip pe-chip--s"><ruby>内<rt>うち</rt></ruby> ↓</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v"><ruby>外<rt>そと</rt></ruby> ↑</span>
</div>

<h3>1. Oila: ikki xil nom</h3>

<p>Eng koʻrinadigan joyi — oila aʼzolari. Yapon tilida
har biri uchun <b>ikkita soʻz</b> bor: biri oʻz oilangiz
uchun, biri boshqaning oilasi uchun.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Kim</th><th>MENING (<ruby>内<rt>うち</rt></ruby>)</th><th>SIZNING (<ruby>外<rt>そと</rt></ruby>)</th></tr>
  <tr><td class="pj-stem">ota</td><td class="pj-end"><ruby>父<rt>ちち</rt></ruby></td>
      <td class="pj-res">お<ruby>父<rt>とう</rt></ruby>さん</td></tr>
  <tr><td class="pj-stem">ona</td><td class="pj-end"><ruby>母<rt>はは</rt></ruby></td>
      <td class="pj-res">お<ruby>母<rt>かあ</rt></ruby>さん</td></tr>
  <tr><td class="pj-stem">aka</td><td class="pj-end"><ruby>兄<rt>あに</rt></ruby></td>
      <td class="pj-res">お<ruby>兄<rt>にい</rt></ruby>さん</td></tr>
  <tr><td class="pj-stem">opa</td><td class="pj-end"><ruby>姉<rt>あね</rt></ruby></td>
      <td class="pj-res">お<ruby>姉<rt>ねえ</rt></ruby>さん</td></tr>
  <tr><td class="pj-stem">uka</td><td class="pj-end"><ruby>弟<rt>おとうと</rt></ruby></td>
      <td class="pj-res"><ruby>弟<rt>おとうと</rt></ruby>さん</td></tr>
  <tr><td class="pj-stem">singil</td><td class="pj-end"><ruby>妹<rt>いもうと</rt></ruby></td>
      <td class="pj-res"><ruby>妹<rt>いもうと</rt></ruby>さん</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Va mana eng gʻalati qismi:</b> uyda oʻz otangizga
  murojaat qilganda siz <b>お<ruby>父<rt>とう</rt></ruby>さん</b>
  deysiz. Lekin tashqaridagi odamga u haqida gapirganda
  <b><ruby>父<rt>ちち</rt></ruby></b> deysiz. Bitta odam,
  ikki nom — chunki <em>tinglovchi</em> oʻzgargan.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham ikki shakl bor — lekin ular bunday
  ishlamaydi.</b> «Dadam» va «otangiz» — farq <em>egalik</em>da,
  hurmatda emas. Va eng muhimi: oʻzbek tilida siz oʻz
  otangizni begonaga gapirganda <b>hech qachon
  pasaytirmaysiz</b>. «Dadam keldilar» deysiz, va bu toʻliq
  tabiiy. Yaponchada esa aynan shu holatda hurmat
  <em>olib tashlanadi</em>:
  <ruby>父<rt>ちち</rt></ruby>が<ruby>参<rt>まい</rt></ruby>りました.
  Bu — butun kursdagi eng begona qoida, va u oddiy
  sababdan kelib chiqadi: yaponchada hurmat <b>odamga</b>
  emas, <b>chegaraga</b> beriladi.</p>
</div>

<p>Bu jadvalning chap ustuni — oʻzingiz haqingizda
gapirganda ishlatiladigan soʻzlar — birinchi qarashda
qoʻpol tuyuladi. «Otam» oʻrniga quruq
<ruby>父<rt>ちち</rt></ruby> deyish oʻzbek quloqqa sovuq
eshitiladi. Lekin yaponcha buni hurmatsizlik deb
tushunmaydi: aksincha, oʻz oilangizni pasaytirish —
<em>suhbatdoshga</em> koʻrsatilgan hurmat. Bu tizimning
butun mantigʻi shu bitta almashuvda turibdi.</p>

<h3>2. Chegara siljiydi</h3>

<p>Bu tizimning eng chalkash qismi shu: <b>bir xil odam
goh ichkarida, goh tashqarida boʻladi</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Kim bilan gapiryapsiz</th><th>Boshligʻingiz qayerda</th><th>Qaysi shakl</th></tr>
  <tr><td class="pj-stem">Ishxona ichida, hamkasb bilan</td>
      <td class="pj-uz"><ruby>外<rt>そと</rt></ruby> — u sizdan yuqori</td>
      <td class="pj-res"><ruby>部長<rt>ぶちょう</rt></ruby>はいらっしゃいます</td></tr>
  <tr><td class="pj-stem">Telefonda, mijoz bilan</td>
      <td class="pj-uz"><ruby>内<rt>うち</rt></ruby> — u sizning tomoningizda</td>
      <td class="pj-res"><ruby>部長<rt>ぶちょう</rt></ruby>はおります</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Va ism ham oʻzgaradi.</b> Ishxona ichida
  <ruby>田中<rt>たなか</rt></ruby><b>さん</b> deysiz; mijozga
  esa <ruby>田中<rt>たなか</rt></ruby> — <b>さん siz</b>.
  Oʻz guruhingiz aʼzosiga tashqi odam oldida さん qoʻshilmaydi.
  Bu chet elliklar eng koʻp adashadigan joy.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>母<rt>はは</rt></ruby>は<ruby>先生<rt>せんせい</rt></ruby>です。お<ruby>母<rt>かあ</rt></ruby>さんは？</p>
  <p class="pe-ex__uz">Onam oʻqituvchi. Onangiz-chi?</p>
  <p class="pe-ex__why">Bitta gapda ikkala shakl: meniki pasayadi, sizniki koʻtariladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu ikkilik faqat egalikda.</b>
  «Onam» va «onangiz» — farq <em>kimniki</em> ekanida,
  hurmatda emas; ikkalasi ham bir xil darajada hurmatli.
  Yaponchada esa <ruby>母<rt>はは</rt></ruby> va
  お<ruby>母<rt>かあ</rt></ruby>さん <b>boshqa-boshqa soʻzlar</b>, va
  ularning biri ataylab pastroq turadi. Shuning uchun
  yaponcha oila soʻzlarini yodlaganda ularni juft-juft
  yodlang — yolgʻiz yodlangan soʻz yarim foydali.</p>
</div>

<h3>3. Kompaniya: <ruby>弊社<rt>へいしゃ</rt></ruby> va <ruby>御社<rt>おんしゃ</rt></ruby></h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Kim</th><th>Ogʻzaki</th><th>Yozma</th></tr>
  <tr><td class="pj-stem">Bizning kompaniya</td><td class="pj-uz"><ruby>弊社<rt>へいしゃ</rt></ruby></td>
      <td class="pj-res"><ruby>弊社<rt>へいしゃ</rt></ruby> · <ruby>当社<rt>とうしゃ</rt></ruby></td></tr>
  <tr><td class="pj-stem">Sizning kompaniya</td><td class="pj-uz"><ruby>御社<rt>おんしゃ</rt></ruby></td>
      <td class="pj-res"><ruby>貴社<rt>きしゃ</rt></ruby></td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b><ruby>弊<rt>へい</rt></ruby> — «yomon», «kamtarin».</b>
  Yaʼni «bizning arzimas kompaniyamiz». Bu soʻzning oʻzi
  <ruby>謙譲語<rt>けんじょうご</rt></ruby> ning fikrini
  koʻrsatib turibdi: oʻzimni pasaytirsam, siz yuqorida
  qolasiz.</p>
</div>

<p>Bu chegara koʻrinmaydi, lekin u har suhbatda bor va
yaponlar uni bolalikdan sezadi. Chet ellik uchun esa u
eng qiyin qism — chunki uni <em>yodlab</em> boʻlmaydi,
har safar qaytadan hisoblash kerak. Yaxshi xabar shuki,
hisoblash bitta savoldan iborat: <b>hozir men kim bilan
gapiryapman, va u mening doiramning ichidami?</b></p>

<h3>4. Uchta darsni bitta qoida bogʻlaydi</h3>

<div class="pe-steps">
  <ol>
    <li>Ish <b><ruby>外<rt>そと</rt></ruby></b> ning ishimi? →
    <ruby>尊敬語<rt>そんけいご</rt></ruby> (PJ-69)</li>
    <li>Ish <b><ruby>内<rt>うち</rt></ruby></b> ning ishimi? →
    <ruby>謙譲語<rt>けんじょうご</rt></ruby> (PJ-70)</li>
    <li>Ikkisiga ham tegmasa? → oddiy
    <ruby>丁寧語<rt>ていねいご</rt></ruby> (PJ-71)</li>
  </ol>
</div>

<div class="pe-call pe-rule">
  <p><b>Yaʼni keigo — uchta alohida tizim emas, bitta
  tizimning uch tomoni.</b> Siz shakllarni yodlashingiz kerak,
  lekin <em>qaysi birini tanlash</em> savolini hisoblab
  oʻtirmaysiz: chegarani koʻrsangiz, javob oʻzi chiqadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">A: お<ruby>父<rt>とう</rt></ruby>さんはいらっしゃいますか。<br>
  B: いいえ、<ruby>父<rt>ちち</rt></ruby>はおりません。</p>
  <p class="pe-ex__uz">A: Otangiz uydami? — B: Yoʻq, dadam yoʻqlar.</p>
  <p class="pe-ex__why">Bitta odam, ikki gapda ikki xil ataladi — va ikkala gap ham toʻgʻri. A tashqaridan soʻrayapti, B ichkaridan javob beryapti.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>弊社<rt>へいしゃ</rt></ruby>の<ruby>田中<rt>たなか</rt></ruby>が<ruby>伺<rt>うかが</rt></ruby>います。</p>
  <p class="pe-ex__uz">Bizning kompaniyadan Tanaka boradi.</p>
  <p class="pe-ex__why">Uchta belgi bir gapda: kompaniya pasaygan, さん tushgan, feʼl kamtar shaklda.</p>
</div>

<h3>5. Qayerda chegara yoʻq</h3>

<p>Bu tizim doim ishlamaydi. Yaqin doʻstlar orasida, oilada
va tengdoshlar bilan chegara <b>yoʻqoladi</b> — u yerda
oddiy shakl (PJ-45) ishlatiladi va hech qanday keigo kerak
emas.</p>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name">Chegara yoʻq</span>
    <span class="pj-level__ja"><ruby>食<rt>た</rt></ruby>べる</span>
    <span class="pj-level__who">oila, yaqin doʻst</span>
  </div>
  <div class="pj-level__row pj-level__row--2">
    <span class="pj-level__name">Chegara bor, tenglar</span>
    <span class="pj-level__ja"><ruby>食<rt>た</rt></ruby>べます</span>
    <span class="pj-level__who">sinfdosh, notanish tengdosh, ustoz</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name">Chegara bor, tengsiz</span>
    <span class="pj-level__ja"><ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がる / いただく</span>
    <span class="pj-level__who">mijoz, katta rahbar, rasmiy marosim</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham chegara bor — faqat u
  qoʻzgʻalmaydi.</b> Siz «sen» va «siz» orasida bir marta
  tanlaysiz va butun munosabat davomida shunda qolasiz.
  Yaponchada esa chegara <em>har suhbatda qayta
  chiziladi</em>: bir xil odam ertalab
  <ruby>内<rt>うち</rt></ruby> da, tushdan keyin
  <ruby>外<rt>そと</rt></ruby> da boʻlishi mumkin. Shuning
  uchun yaponcha keigoni yodlash emas, <b>qayerda
  turganingizni sezish</b> mashqi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">内</span>
    <span class="pj-kanji__uz">ichkari</span>
    <span class="pj-kanji__on">オン: ナイ</span>
    <span class="pj-kanji__kun">KUN: うち</span>
    <span class="pj-kanji__note">内 (うち) — oʻz guruhim · 案内 (あんない) — yoʻl koʻrsatish</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">社</span>
    <span class="pj-kanji__uz">kompaniya; ibodatxona</span>
    <span class="pj-kanji__on">オン: シャ</span>
    <span class="pj-kanji__kun">KUN: やしろ</span>
    <span class="pj-kanji__note">会社 (かいしゃ) — kompaniya · 弊社 (へいしゃ) — bizning kompaniya</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Begonaga: お<ruby>父<rt>とう</rt></ruby>さんは<ruby>先生<rt>せんせい</rt></ruby>です</p>
  <p class="pe-fix__good">✓ <ruby>父<rt>ちち</rt></ruby>は<ruby>先生<rt>せんせい</rt></ruby>です — oʻz otangiz tashqi odamga <b>pasaytiriladi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Mijozga: <ruby>田中<rt>たなか</rt></ruby>さんはおりません</p>
  <p class="pe-fix__good">✓ <ruby>田中<rt>たなか</rt></ruby>はおりません — oʻz guruhingiz aʼzosiga <b>さん qoʻshilmaydi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Mijozga: <ruby>部長<rt>ぶちょう</rt></ruby>はいらっしゃいません</p>
  <p class="pe-fix__good">✓ <ruby>部長<rt>ぶちょう</rt></ruby>はおりません — chegara siljidi, boshliq endi <ruby>内<rt>うち</rt></ruby>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Oʻz kompaniyangiz haqida: <ruby>御社<rt>おんしゃ</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>弊社<rt>へいしゃ</rt></ruby> — <ruby>御社<rt>おんしゃ</rt></ruby> suhbatdoshning kompaniyasi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Begonaga oʻz otangiz haqida gapiryapsiz. Qaysi soʻz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>父<rt>ちち</rt></ruby></b> — お<ruby>父<rt>とう</rt></ruby>さん emas. Oʻz oilangiz <ruby>内<rt>うち</rt></ruby>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Uyda otangizga murojaat qilyapsiz. Qaysi soʻz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>お<ruby>父<rt>とう</rt></ruby>さん</b> — uyda chegara yoʻq, u sizning ustingizda.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Mijoz telefonda boshligʻingizni soʻradi. Qaysi feʼl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>おります</b> — chegara siljidi, boshliq endi sizning <ruby>内<rt>うち</rt></ruby> ingizda.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Oʻz kompaniyangizni qanday ataysiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>弊社<rt>へいしゃ</rt></ruby></b> — «kamtarin kompaniyamiz». Suhbatdoshniki — <ruby>御社<rt>おんしゃ</rt></ruby>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega yaponchada hurmat odamga emas, chegaraga beriladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki tizim <b>munosabat</b>ni koʻrsatadi, shaxsni emas. Bir xil odam chegaraning ikki tomonida boʻlishi mumkin.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>内<rt>うち</rt></ruby></b> — oʻz guruhim</li>
  <li><b><ruby>外<rt>そと</rt></ruby></b> — tashqaridagilar</li>
  <li><b><ruby>父<rt>ちち</rt></ruby> / お<ruby>父<rt>とう</rt></ruby>さん</b> — mening otam / sizning otangiz</li>
  <li><b><ruby>母<rt>はは</rt></ruby> / お<ruby>母<rt>かあ</rt></ruby>さん</b> — mening onam / sizning onangiz</li>
  <li><b><ruby>兄<rt>あに</rt></ruby> / お<ruby>兄<rt>にい</rt></ruby>さん</b> — mening akam / sizning akangiz</li>
  <li><b><ruby>弊社<rt>へいしゃ</rt></ruby></b> — bizning kompaniya</li>
  <li><b><ruby>御社<rt>おんしゃ</rt></ruby></b> — sizning kompaniyangiz</li>
  <li><b><ruby>部長<rt>ぶちょう</rt></ruby></b> — boʻlim boshligʻi</li>
  <li><b>おる</b> — いる ning kamtar shakli</li>
  <li><b><ruby>紹介<rt>しょうかい</rt></ruby>する</b> — tanishtirmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b><ruby>内<rt>うち</rt></ruby> pasayadi, <ruby>外<rt>そと</rt></ruby> koʻtariladi.</b></li>
    <li>Chegara <b>siljiydi</b> — bir xil odam ikki tomonda boʻlishi mumkin.</li>
    <li>Hurmat <b>odamga emas, chegaraga</b> beriladi.</li>
  </ul>
</div>
""",
    },
]
