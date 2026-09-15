# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-67 (Blok E davomi) va PJ-68, PJ-69 (keigo boshlanadi).

PJ-67 — kursda deyarli yagona dars, unda oʻrganilgan shakl «ishlatmang»
degan ogohlantirish bilan beriladi. Buyruq shakli yaponchada qoʻpol;
uni bilish kerak, chunki u belgilarda, mangada va sport maydonida
uchraydi.

PJ-68 keigoning uch tarmogʻini ochadi, PJ-69 esa birinchisini —
<ruby>尊敬語<rt>そんけいご</rt></ruby> ni — batafsil beradi.

⚠️ Beshta istisno feʼl (いらっしゃる・なさる・おっしゃる・くださる・ござる)
ます shaklida り → い qiladi: いらっしゃいます, «いらっしゃります» EMAS.
Butun keigo blokidagi eng koʻp qilinadigan xato shu.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_67_69.py --author=prime
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
        "title": "PJ-67: Buyruq va taqiq shakllari: 行け / 行くな va ularning oʻrni",
        "category": "japanese",
        "order": 67,
        "summary": (
            "Kursdagi yagona dars, unda shakl «ishlatmang» degan "
            "ogohlantirish bilan beriladi. Lekin uni bilmasdan belgini "
            "ham, mangani ham, sport maydonidagi baqiriqni ham "
            "tushunib boʻlmaydi."
        ),
        "stories": ["がんばれ"],
        "content": """
<h2>PJ-67: Buyruq va taqiq shakllari: <ruby>行<rt>い</rt></ruby>け / <ruby>行<rt>い</rt></ruby>くな</h2>

<p>Yapon tilida buyruqning eng qisqa shakli bor:
<b><ruby>行<rt>い</rt></ruby>け</b> — «bor». Va taqiqning eng qisqa
shakli ham: <b><ruby>行<rt>い</rt></ruby>くな</b> — «borma».</p>

<p>Lekin darsni ogohlantirish bilan boshlaymiz:
<b>bu shakllarni deyarli hech qachon ishlatmaysiz.</b> Ular
yaponchada qoʻpol. Shunga qaramay ularni bilish shart —
chunki koʻchadagi belgida, mangada va sport maydonida siz
ularni har kuni koʻrasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Buyruq shaklini uch guruh feʼlidan yasaysiz</li>
    <li>Taqiq shaklini yasaysiz — u ancha oson</li>
    <li>Bu shakllar qayerda toʻgʻri ekanini bilib olasiz</li>
    <li>Yumshoqroq zinapoyani oʻrganasiz: 〜なさい, 〜てください</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qisqa shakl</span>
  <span class="pe-chip pe-chip--v">え-qator (buyruq)</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">lugʻat + な (taqiq)</span>
</div>

<h3>1. Buyruq shakli — <ruby>命令形<rt>めいれいけい</rt></ruby></h3>

<div class="pj-group">
  <div class="pj-group__c">
    <p class="pj-group__h">I — <ruby>五段<rt>ごだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>行<rt>い</rt></ruby>く → <ruby>行<rt>い</rt></ruby>け</p>
    <p>Oxirgi bogʻin <b>え-qatorga</b> tushadi. Xolos — hech nima qoʻshilmaydi.</p>
  </div>
  <div class="pj-group__c pj-group__c--2">
    <p class="pj-group__h">II — <ruby>一段<rt>いちだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>食<rt>た</rt></ruby>べる → <ruby>食<rt>た</rt></ruby>べろ</p>
    <p>る tushadi, <b>ろ</b> qoʻyiladi.</p>
  </div>
  <div class="pj-group__c pj-group__c--3">
    <p class="pj-group__h">III — <ruby>不規則<rt>ふきそく</rt></ruby></p>
    <p class="pj-group__ex">する → しろ · <ruby>来<rt>く</rt></ruby>る → <ruby>来<rt>こ</rt></ruby>い</p>
    <p><ruby>来<rt>こ</rt></ruby>い — «きろ» emas. Yodlab qoʻying.</p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>え-qator yana ishga tushdi.</b> Siz uni PJ-51 da
  koʻrgansiz: <ruby>行<rt>い</rt></ruby>け<b>ば</b>. Buyruq shakli
  — oʻsha <b><ruby>行<rt>い</rt></ruby>け</b> ning oʻzi, faqat
  ば siz. Yaʼni yangi oʻzak yodlash kerak emas.</p>
</div>

<p>Diqqat qiling: II guruhdagi <b>ろ</b> ni PJ-63 dagi
passiv va PJ-65 dagi kauzativ bilan chalkashtirmang. Ular
<em>ない-oʻzagidan</em> yasaladi, buyruq shakli esa
butunlay boshqa yoʻldan boradi: I guruhda え-qator, II guruhda
る → ろ. Yaʼni bu kursda birinchi marta uchraydigan
oʻzak — va oxirgisi ham.</p>

<h3>2. Taqiq shakli — <ruby>禁止形<rt>きんしけい</rt></ruby></h3>

<p>Bu ancha oson: <b>lugʻat shakliga な qoʻshiladi</b>. Uch
guruh uchun ham bir xil, istisno yoʻq.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Buyruq</th><th>Taqiq</th></tr>
  <tr><td class="pj-stem"><ruby>行<rt>い</rt></ruby>く</td>
      <td class="pj-uz"><ruby>行<rt>い</rt></ruby>け</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>くな</td></tr>
  <tr><td class="pj-stem"><ruby>読<rt>よ</rt></ruby>む</td>
      <td class="pj-uz"><ruby>読<rt>よ</rt></ruby>め</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>むな</td></tr>
  <tr><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べる</td>
      <td class="pj-uz"><ruby>食<rt>た</rt></ruby>べろ</td><td class="pj-res"><ruby>食<rt>た</rt></ruby>べるな</td></tr>
  <tr><td class="pj-stem">する</td>
      <td class="pj-uz">しろ</td><td class="pj-res">するな</td></tr>
  <tr><td class="pj-stem"><ruby>来<rt>く</rt></ruby>る</td>
      <td class="pj-uz"><ruby>来<rt>こ</rt></ruby>い</td><td class="pj-res"><ruby>来<rt>く</rt></ruby>るな</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada taqiq ham bitta boʻgʻin.</b> «Bor<b>ma</b>»,
  «yoz<b>ma</b>», «kel<b>ma</b>» — feʼlga <b>-ma</b> qoʻshiladi.
  Yaponchada esa <b>な</b>. Ikkala tilda ham bu eng qisqa
  taqiq shakli va ikkalasida ham u ancha keskin eshitiladi.
  Farqi shundaki, oʻzbekcha «borma» doʻstga aytilsa oddiy
  gap; yaponcha <ruby>行<rt>い</rt></ruby>くな esa deyarli
  baqiriq.</p>
</div>

<p>Diqqat qiling: buyruq shakli — kursdagi <b>eng qisqa</b>
feʼl shakli. Unda hech qanday qoʻshimcha yoʻq, hatto ます ham,
だ ham. Yapon tilida qisqalik va muloyimlik teskari
proporsional: gap qanchalik qisqa boʻlsa, shunchalik yaqin
yoki shunchalik keskin. Shuning uchun bu shaklni koʻrganda
birinchi savol «kim kimga aytyapti?» boʻlishi kerak.</p>

<h3>3. Bu shakllar qayerda toʻgʻri</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Joy</th><th>Misol</th><th>Nega toʻgʻri</th></tr>
  <tr><td class="pj-stem">Yoʻl belgisi</td><td class="pj-res"><ruby>止<rt>と</rt></ruby>まれ</td>
      <td class="pj-uz">belgi muloyim boʻlmaydi — u qisqa boʻlishi kerak</td></tr>
  <tr><td class="pj-stem">Ogohlantirish</td><td class="pj-res"><ruby>入<rt>はい</rt></ruby>るな</td>
      <td class="pj-uz">xavf bor, vaqt yoʻq</td></tr>
  <tr><td class="pj-stem">Sport maydoni</td><td class="pj-res"><ruby>頑張<rt>がんば</rt></ruby>れ</td>
      <td class="pj-uz">baqirib quvvatlash — bu buyruq emas, qoʻllab-quvvatlash</td></tr>
  <tr><td class="pj-stem">Manga, anime</td><td class="pj-res"><ruby>待<rt>ま</rt></ruby>て</td>
      <td class="pj-uz">personaj nutqi, koʻpincha erkaklar tilida</td></tr>
  <tr><td class="pj-stem">Favqulodda holat</td><td class="pj-res"><ruby>逃<rt>に</rt></ruby>げろ</td>
      <td class="pj-uz">odam hayoti xavf ostida boʻlganda odob kutilmaydi</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Bu roʻyxatda maktab ham, ish joyi ham, doʻkon ham
  yoʻq.</b> Ustozga, mijozga, notanish odamga yoki kattaroq
  odamga bu shakllar <em>hech qachon</em> aytilmaydi. Yaponiyada
  yashayotgan chet ellik ularni butun umr <b>faqat oʻqiydi</b>,
  hech qachon gapirmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham «bor!» ning kuchi joyiga qarab
  oʻzgaradi.</b> Doʻstingizga «bor» desangiz oddiy;
  ustozingizga aytsangiz qoʻpol; koʻchada notanish odamga
  baqirsangiz janjal. Yaponchada shu farq bor, faqat u
  <b>ancha kengroq</b>: u yerda oʻrtacha holat ham qoʻpol
  hisoblanadi. Shuning uchun oʻzbekcha «bor» ni yaponchaga
  <ruby>行<rt>い</rt></ruby>け deb emas,
  <ruby>行<rt>い</rt></ruby>ってください deb tarjima qiling.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>危<rt>あぶ</rt></ruby>ない！<ruby>逃<rt>に</rt></ruby>げろ！</p>
  <p class="pe-ex__uz">Xavfli! Qoching!</p>
  <p class="pe-ex__why">Favqulodda holatda odob kutilmaydi — bu yerda buyruq shakli <b>toʻgʻri</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">ここに<ruby>入<rt>はい</rt></ruby>るな。</p>
  <p class="pe-ex__uz">Bu yerga kirmang.</p>
  <p class="pe-ex__why">Ogohlantirish belgisi. Lugʻat shakli + <b>な</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha belgilarda ham qisqa shakl turadi.</b>
  «Toʻxta», «Kirish taqiqlanadi», «Tegmang» — koʻchadagi
  yozuv hech qachon «toʻxtashingizni soʻraymiz» demaydi.
  Sababi ikkala tilda ham bir xil: belgi <em>oʻqilmaydi</em>,
  u <em>koʻriladi</em>, va koʻz uzun gapni ulgurmaydi. Shuning
  uchun yaponcha <ruby>止<rt>と</rt></ruby>まれ ni qoʻpol deb emas,
  <b>qisqa</b> deb tushunish toʻgʻriroq.</p>
</div>

<h3>4. 〜なさい — oʻrtadagi shakl</h3>

<p>Buyruq va iltimos orasida bitta pogʻona bor:
<b>ます-oʻzagi + なさい</b>. Bu ota-onadan bolaga, ustozdan
oʻquvchiga aytiladigan shakl — qatʼiy, lekin qoʻpol emas.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>早<rt>はや</rt></ruby>く<ruby>食<rt>た</rt></ruby>べなさい。</p>
  <p class="pe-ex__uz">Tezroq ye.</p>
  <p class="pe-ex__why">ます-oʻzagi <ruby>食<rt>た</rt></ruby>べ, ustiga なさい.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>なさい ni faqat pastdagilarga aytish mumkin.</b>
  Ota-ona bolaga, ustoz oʻquvchiga, katta aka ukasiga. Teng
  yoshdagi doʻstga aytilsa — gʻalati, kattaroq odamga
  aytilsa — haqorat. Imtihon savollarida esa u tez-tez
  chiqadi: <ruby>答<rt>こた</rt></ruby>えなさい («javob bering»).</p>
</div>

<p>Diqqat qiling: なさい ham <b>bir tomonlama</b>. U pastga
qarab aytiladi va yuqoriga qarab hech qachon. Shuning uchun
undan ehtiyot boʻling: ustozga «<ruby>行<rt>い</rt></ruby>きなさい» deb aytish
buyruq shaklidan koʻra ham gʻalati eshitiladi, chunki u
sizni oʻz oʻrningizdan yuqoriga qoʻyadi. Yaponchada bu
grammatik xato emas, <em>mavqe</em> xatosi — va bu keyingi
uch darsning asosiy mavzusi.</p>

<h3>5. Butun zinapoya</h3>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name"><ruby>命令形<rt>めいれいけい</rt></ruby></span>
    <span class="pj-level__ja"><ruby>行<rt>い</rt></ruby>け</span>
    <span class="pj-level__who">belgi, baqiriq, manga — odamga emas</span>
  </div>
  <div class="pj-level__row pj-level__row--2">
    <span class="pj-level__name">〜なさい</span>
    <span class="pj-level__ja"><ruby>行<rt>い</rt></ruby>きなさい</span>
    <span class="pj-level__who">ota-ona → bola, ustoz → oʻquvchi</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name">〜てください</span>
    <span class="pj-level__ja"><ruby>行<rt>い</rt></ruby>ってください</span>
    <span class="pj-level__who">odatdagi iltimos — eng koʻp ishlatiladigan</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>Va zinapoya yuqoriga davom etadi.</b> PJ-61 da siz
  <ruby>行<rt>い</rt></ruby>ってもらえますか va
  <ruby>行<rt>い</rt></ruby>っていただけますか ni koʻrgansiz.
  Yaʼni yaponchada buyruqning oltita darajasi bor, va ularning
  <em>bittasi</em> — eng pastkisi — bugungi darsda.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">命</span>
    <span class="pj-kanji__uz">hayot; buyruq</span>
    <span class="pj-kanji__on">オン: メイ</span>
    <span class="pj-kanji__kun">KUN: いのち</span>
    <span class="pj-kanji__note">命令 (めいれい) — buyruq · 命 (いのち) — hayot</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">禁</span>
    <span class="pj-kanji__uz">taqiqlamoq</span>
    <span class="pj-kanji__on">オン: キン</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">禁止 (きんし) — taqiq · 立入禁止 (たちいりきんし) — kirish taqiqlangan</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>来<rt>き</rt></ruby>ろ</p>
  <p class="pe-fix__good">✓ <ruby>来<rt>こ</rt></ruby>い — <ruby>来<rt>く</rt></ruby>る ning buyruq shakli istisno.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>食<rt>た</rt></ruby>べれ</p>
  <p class="pe-fix__good">✓ <ruby>食<rt>た</rt></ruby>べ<b>ろ</b> — II guruh ろ oladi, え-qator emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>けな (taqiq sifatida)</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby><b>くな</b> — な <b>lugʻat shakliga</b> qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Ustozga: <ruby>待<rt>ま</rt></ruby>て</p>
  <p class="pe-fix__good">✓ <ruby>待<rt>ま</rt></ruby>ってください — buyruq shakli odamga aytilmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>読<rt>よ</rt></ruby>む ning buyruq shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>読<rt>よ</rt></ruby>め</b> — む → め (え-qator).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>来<rt>く</rt></ruby>る ning buyruq shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>来<rt>こ</rt></ruby>い</b> — istisno. «きろ» degan shakl yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>食<rt>た</rt></ruby>べる ning taqiq shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>食<rt>た</rt></ruby>べるな</b> — な lugʻat shakliga qoʻshiladi, istisnosiz.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>頑張<rt>がんば</rt></ruby>れ» qoʻpolmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yoʻq. Sport maydonida bu <b>quvvatlash</b>, buyruq emas — va u eng koʻp eshitiladigan buyruq shakli.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Ustozga «kuting» deysiz. Qaysi shakl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>待<rt>ま</rt></ruby>ってください</b> — yoki muloyimroq <ruby>待<rt>ま</rt></ruby>っていただけますか. <ruby>待<rt>ま</rt></ruby>て hech qachon.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>命令形<rt>めいれいけい</rt></ruby></b> — buyruq shakli</li>
  <li><b><ruby>禁止形<rt>きんしけい</rt></ruby></b> — taqiq shakli</li>
  <li><b>〜なさい</b> — qatʼiy, lekin qoʻpol emas</li>
  <li><b><ruby>頑張<rt>がんば</rt></ruby>れ</b> — «harakat qil!», quvvatlash</li>
  <li><b><ruby>止<rt>と</rt></ruby>まれ</b> — «toʻxta» (yoʻl belgisi)</li>
  <li><b><ruby>危<rt>あぶ</rt></ruby>ない</b> — xavfli</li>
  <li><b><ruby>逃<rt>に</rt></ruby>げる</b> — qochmoq (II guruh)</li>
  <li><b><ruby>立入禁止<rt>たちいりきんし</rt></ruby></b> — kirish taqiqlangan</li>
  <li><b><ruby>応援<rt>おうえん</rt></ruby>する</b> — quvvatlamoq</li>
  <li><b><ruby>選手<rt>せんしゅ</rt></ruby></b> — sportchi</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Buyruq: <b>え-qator</b> (I), <b>ろ</b> (II), <b><ruby>来<rt>こ</rt></ruby>い</b> (istisno).</li>
    <li>Taqiq: <b>lugʻat shakli + な</b>, istisnosiz.</li>
    <li>Ikkalasini ham <b>odamga aytmang</b> — oʻqing, gapirmang.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-68: Keigo 1: nega hurmat tili bor va uch tarmogʻi qanday ishlaydi",
        "category": "japanese",
        "order": 68,
        "summary": (
            "Keigo — muloyimlik emas, MAVQE. Uch tarmoq bor va ular "
            "bir-birini almashtirmaydi: biri suhbatdoshni koʻtaradi, "
            "biri meni pasaytiradi, biri esa butun gapga kiyim beradi."
        ),
        "stories": ["はじめての アルバイト"],
        "content": """
<h2>PJ-68: Keigo 1: nega hurmat tili bor</h2>

<p>Bir narsani boshda aytib qoʻyish kerak, chunki u butun
blokni tushunarli qiladi:</p>

<p><b>Keigo — muloyimlik emas. Keigo — mavqe.</b></p>

<p>Siz です・ます ni PJ-13 dan beri ishlatasiz va u muloyimlik
edi: siz odamga hurmat bilan gapirasiz. Keigo esa boshqa ish
qiladi — u <em>kim yuqorida, kim pastda</em> ekanini har bir
feʼlda koʻrsatadi. Shuning uchun uni «juda muloyim yaponcha»
deb tushunish notoʻgʻri.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Keigoning uch tarmogʻini ajratasiz</li>
    <li>Har biri kimni koʻtarishini bilib olasiz</li>
    <li>Eng katta xatoni — oʻzingizga hurmat qoʻshishni — koʻrasiz</li>
    <li>Keigo qayerda majburiy, qayerda ortiqcha ekanini tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch tarmoq</span>
  <span class="pe-chip pe-chip--v"><ruby>尊敬語<rt>そんけいご</rt></ruby> ↑</span>
  <span class="pe-chip pe-chip--s"><ruby>謙譲語<rt>けんじょうご</rt></ruby> ↓</span>
  <span class="pe-chip pe-chip--adv"><ruby>丁寧語<rt>ていねいご</rt></ruby> →</span>
</div>

<h3>1. Uch tarmoq</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Tarmoq</th><th>Nima qiladi</th><th>Kimning ishi haqida</th><th>Misol</th></tr>
  <tr><td class="pj-stem"><ruby>尊敬語<rt>そんけいご</rt></ruby></td>
      <td class="pj-uz">suhbatdoshni <b>koʻtaradi</b></td>
      <td class="pj-end"><b>uning</b> ishi</td>
      <td class="pj-res"><ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がる (yemoq)</td></tr>
  <tr><td class="pj-stem"><ruby>謙譲語<rt>けんじょうご</rt></ruby></td>
      <td class="pj-uz">meni <b>pasaytiradi</b></td>
      <td class="pj-end"><b>mening</b> ishim</td>
      <td class="pj-res">いただく (yemoq)</td></tr>
  <tr><td class="pj-stem"><ruby>丁寧語<rt>ていねいご</rt></ruby></td>
      <td class="pj-uz">gapga <b>kiyim beradi</b></td>
      <td class="pj-end">kimning ishi boʻlsa ham</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べます</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Uchalasi ham «yemoq» degani.</b> Farq maʼnoda emas,
  <em>kim yuqorida turishida</em>. Mijoz yeyayotgan boʻlsa —
  <ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がる.
  Men yeyayotgan boʻlsam — いただく. Bu ikkisi almashsa, gap
  buziladi va u grammatik xato emas, <b>ijtimoiy xato</b>
  boʻladi.</p>
</div>

<h3>2. Eng katta xato</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">✗ OʻZINGIZGA HURMAT</p>
    <p><ruby>私<rt>わたし</rt></ruby>が<ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がります。</p>
    <p>«Men marhamat qilib yeyman» — kulgili eshitiladi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">✗ MIJOZNI PASAYTIRISH</p>
    <p>お<ruby>客<rt>きゃく</rt></ruby>さまがいただきます。</p>
    <p>«Mijoz kamtarlik bilan oladi» — haqorat.</p></div>
</div>

<div class="pe-call pe-warn">
  <p><b>Qoida bitta va u istisnosiz.</b>
  <ruby>尊敬語<rt>そんけいご</rt></ruby> —
  <em>hech qachon</em> oʻzingiz haqingizda.
  <ruby>謙譲語<rt>けんじょうご</rt></ruby> —
  <em>hech qachon</em> suhbatdosh haqida. Shu ikki qoidani
  bilsangiz, keigo xatolaringizning yarmi yoʻqoladi.</p>
</div>

<p>Bu ikki qoidani bir marta yodlab qoʻysangiz, keigo
xatolaringizning yarmi yoʻqoladi. Qolgan yarmi esa
<em>shakllarni</em> yodlashdan iborat, va u faqat vaqt
masalasi. Yaʼni bu blokdagi qiyinchilik xotira emas,
<b>nuqtai nazar</b>: har gapda «bu kimning ishi?» degan
savolni berishga oʻrganish kerak.</p>

<h3>3. Nega yaponchada bu bor</h3>

<p>Sabab PJ-60 da aytilgan edi va PJ-72 da toʻliq ochiladi:
yapon tili odamlarni <b><ruby>内<rt>うち</rt></ruby></b>
(ichkaridagilar — men, oilam, ishxonam) va
<b><ruby>外<rt>そと</rt></ruby></b> (tashqaridagilar — mijoz,
begona, boshqa kompaniya) ga boʻladi.</p>

<div class="pe-call pe-rule">
  <p><b>Va mana eng gʻalati qismi:</b> siz
  <em>oʻz boshligʻingizni ham</em> pasaytirasiz — agar u haqida
  tashqi odamga gapirsangiz. Ishxonada
  <ruby>部長<rt>ぶちょう</rt></ruby>はいらっしゃいます deysiz;
  telefonda mijozga esa
  <ruby>部長<rt>ぶちょう</rt></ruby>はおりません deysiz. Bitta
  odam, ikki xil shakl — chunki chegara siljidi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham hurmat grammatikada bor — lekin
  boshqacha.</b> «Keldi» va «kel<b>dilar</b>», «ayt<b>dilar</b>»
  — siz koʻplik qoʻshimchasi bilan odamni koʻtarasiz, va bu
  keigoning <ruby>尊敬語<rt>そんけいご</rt></ruby> tarmogʻiga
  toʻgʻri keladi. «Siz» va «sen» ham shu. Farq ikkitada:
  <b>(1)</b> oʻzbekchada oʻzini pasaytiradigan tarmoq
  deyarli yoʻq; <b>(2)</b> oʻzbekchada siz bir daraja tanlab,
  butun suhbatni shunda olib borasiz — yaponchada esa daraja
  <em>har bir feʼlda</em> qaytadan tanlanadi, chunki u
  kimning ishi ekaniga bogʻliq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">お<ruby>客<rt>きゃく</rt></ruby>さまが<ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がります。</p>
  <p class="pe-ex__uz">Mijoz yeydilar.</p>
  <p class="pe-ex__why">Uning ishi — <ruby>尊敬語<rt>そんけいご</rt></ruby>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>がいただきます。</p>
  <p class="pe-ex__uz">Men olaman.</p>
  <p class="pe-ex__why">Mening ishim — <ruby>謙譲語<rt>けんじょうご</rt></ruby>. Ikkala gapda ham feʼl «yemoq».</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham «marhamat qiling» va «ijozat bering»
  bir tomonga qaramaydi.</b> Birinchisi suhbatdoshni
  koʻtaradi, ikkinchisi oʻzingizni pasaytiradi — va siz
  ularni hech qachon almashtirmaysiz. Yaponchada shu farq
  butun bir tizimga aylangan: har bir koʻp ishlatiladigan
  feʼlning <em>ikkita</em> hurmat shakli bor, va qaysi birini
  tanlash <b>kimning ishi</b> ekaniga bogʻliq. Yaʼni tushuncha
  sizda bor — faqat u yerda u ancha kengroq.</p>
</div>

<h3>4. Qayerda majburiy, qayerda ortiqcha</h3>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name">Oddiy shakl</span>
    <span class="pj-level__ja"><ruby>食<rt>た</rt></ruby>べる</span>
    <span class="pj-level__who">oila, yaqin doʻst</span>
  </div>
  <div class="pj-level__row pj-level__row--2">
    <span class="pj-level__name"><ruby>丁寧語<rt>ていねいご</rt></ruby></span>
    <span class="pj-level__ja"><ruby>食<rt>た</rt></ruby>べます</span>
    <span class="pj-level__who">ustoz, sinfdosh, notanish odam — <b>90% holat</b></span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name"><ruby>尊敬語<rt>そんけいご</rt></ruby> / <ruby>謙譲語<rt>けんじょうご</rt></ruby></span>
    <span class="pj-level__ja"><ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がる / いただく</span>
    <span class="pj-level__who">mijoz, ish suhbati, rasmiy xat</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Talaba sifatida sizga <ruby>丁寧語<rt>ていねいご</rt></ruby> yetadi.</b> Ustoz bilan
  です・ます — bu toʻliq toʻgʻri va hech kim sizdan koʻproq
  kutmaydi. Keigo ish joyida, doʻkonda va rasmiy joyda kerak
  boʻladi. Shuning uchun uni <em>tanish</em> uchun oʻrganing,
  <em>har kuni ishlatish</em> uchun emas.</p>
</div>

<p>Va oxirgi bir izoh: keigoni bilmasdan ham Yaponiyada
yashash mumkin. Chet elliklardan uni hech kim talab
qilmaydi, va です・ます bilan gapiradigan odamga hech kim
eʼtiroz bildirmaydi. Lekin keigoni <b>tushunmasdan</b>
yashash qiyin — chunki doʻkonda, poyezdda va telefonda
sizga aynan shu tilda murojaat qilishadi. Shuning uchun bu
blokning maqsadi <em>gapirish</em> emas, <b>eshitganini
tushunish</b>.</p>

<h3>5. Blokning xaritasi</h3>

<p>Keigo toʻrtta darsdan iborat, va ular bir-birining ustiga
quriladi:</p>

<div class="pe-steps">
  <ol>
    <li><b>PJ-68</b> (bugun) — uch tarmoq va ularning mantigʻi</li>
    <li><b>PJ-69</b> — <ruby>尊敬語<rt>そんけいご</rt></ruby>: suhbatdoshni koʻtarish</li>
    <li><b>PJ-70</b> — <ruby>謙譲語<rt>けんじょうご</rt></ruby>: oʻzini pasaytirish</li>
    <li><b>PJ-71</b> — <ruby>丁寧語<rt>ていねいご</rt></ruby> va doʻkondagi yapon tili</li>
  </ol>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">お<ruby>客<rt>きゃく</rt></ruby>さまが<ruby>来<rt>こ</rt></ruby>られました。→ お<ruby>客<rt>きゃく</rt></ruby>さまがいらっしゃいました。</p>
  <p class="pe-ex__uz">Mijoz keldilar.</p>
  <p class="pe-ex__why">Birinchisi ham hurmat (PJ-63 dagi passiv shakli!), ikkinchisi esa toʻliq <ruby>尊敬語<rt>そんけいご</rt></ruby>. Ikkalasi ham toʻgʻri — ikkinchisi kuchliroq.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Passiv shakl hurmat sifatida — tanish narsa.</b>
  Oʻzbekchada ham «aytildi», «koʻrsatildi» degan shakllar
  rasmiy nutqda odamni nomlamaslik uchun ishlatiladi.
  Yaponchada esa PJ-63 dagi <ruby>受身形<rt>うけみけい</rt></ruby>
  toʻgʻridan-toʻgʻri <b>yengil hurmat shakli</b> boʻlib ham
  xizmat qiladi: <ruby>読<rt>よ</rt></ruby>まれる,
  <ruby>行<rt>い</rt></ruby>かれる. Bu keigoning eng oson
  darajasi va uni siz allaqachon yasay olasiz.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">敬</span>
    <span class="pj-kanji__uz">hurmat</span>
    <span class="pj-kanji__on">オン: ケイ</span>
    <span class="pj-kanji__kun">KUN: うやま(う)</span>
    <span class="pj-kanji__note"><ruby>敬語<rt>けいご</rt></ruby> (けいご) — hurmat tili · 尊敬 (そんけい) — hurmat</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">謙</span>
    <span class="pj-kanji__uz">kamtarlik</span>
    <span class="pj-kanji__on">オン: ケン</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note"><ruby>謙譲語<rt>けんじょうご</rt></ruby> (けんじょうご) — kamtarlik tili</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>が<ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がります</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby>がいただきます — <ruby>尊敬語<rt>そんけいご</rt></ruby> oʻzingizga ishlatilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ お<ruby>客<rt>きゃく</rt></ruby>さまがいただきます</p>
  <p class="pe-fix__good">✓ お<ruby>客<rt>きゃく</rt></ruby>さまが<ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がります — <ruby>謙譲語<rt>けんじょうご</rt></ruby> suhbatdoshga ishlatilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Keigo = «juda muloyim yaponcha»</p>
  <p class="pe-fix__good">✓ Keigo = <b>mavqe</b>. U kim yuqorida ekanini koʻrsatadi, muloyimlikni emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Ustoz bilan har doim keigo kerak</p>
  <p class="pe-fix__good">✓ Talaba uchun <b>です・ます yetadi</b>. Keigo ish joyida va doʻkonda kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Keigoning uch tarmogʻini ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>尊敬語<rt>そんけいご</rt></ruby></b> (koʻtaradi), <b><ruby>謙譲語<rt>けんじょうご</rt></ruby></b> (pasaytiradi), <b><ruby>丁寧語<rt>ていねいご</rt></ruby></b> (kiyim beradi).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Mijoz yeyayapti. Qaysi feʼl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がる</b> — <ruby>尊敬語<rt>そんけいご</rt></ruby>, chunki bu <em>uning</em> ishi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Men yeyayapman. Qaysi feʼl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>いただく</b> — <ruby>謙譲語<rt>けんじょうご</rt></ruby>, chunki bu <em>mening</em> ishim.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Nega oʻz boshligʻingizni mijozga gapirganda pasaytirasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki u sizning <b><ruby>内<rt>うち</rt></ruby></b> ingizda — mijoz esa <ruby>外<rt>そと</rt></ruby>. Chegara siljigan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Talaba sifatida ustoz bilan qaysi daraja yetadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>丁寧語<rt>ていねいご</rt></ruby></b> — です・ます. Bu toʻliq toʻgʻri va hech kim koʻproq kutmaydi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>敬語<rt>けいご</rt></ruby></b> — hurmat tili</li>
  <li><b><ruby>尊敬語<rt>そんけいご</rt></ruby></b> — koʻtaruvchi tarmoq</li>
  <li><b><ruby>謙譲語<rt>けんじょうご</rt></ruby></b> — pasaytiruvchi tarmoq</li>
  <li><b><ruby>丁寧語<rt>ていねいご</rt></ruby></b> — です・ます</li>
  <li><b><ruby>内<rt>うち</rt></ruby> / <ruby>外<rt>そと</rt></ruby></b> — ichki / tashqi guruh</li>
  <li><b>お<ruby>客<rt>きゃく</rt></ruby>さま</b> — mijoz</li>
  <li><b><ruby>部長<rt>ぶちょう</rt></ruby></b> — boʻlim boshligʻi</li>
  <li><b><ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がる</b> — yemoq (<ruby>尊敬語<rt>そんけいご</rt></ruby>)</li>
  <li><b>いただく</b> — olmoq, yemoq (<ruby>謙譲語<rt>けんじょうご</rt></ruby>)</li>
  <li><b>アルバイト</b> — yarim kunlik ish</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Keigo — <b>mavqe</b>, muloyimlik emas.</li>
    <li><ruby>尊敬語<rt>そんけいご</rt></ruby> oʻzingizga, <ruby>謙譲語<rt>けんじょうご</rt></ruby> suhbatdoshga <b>hech qachon</b>.</li>
    <li>Talaba uchun <b>です・ます yetadi</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-69: Keigo 2: 尊敬語 — お〜になる va maxsus feʼllar",
        "category": "japanese",
        "order": 69,
        "summary": (
            "Suhbatdoshni koʻtaradigan tarmoq. Uchta yoʻli bor, va "
            "beshta maxsus feʼlning ます shakli istisno: いらっしゃいます, "
            "«いらっしゃります» emas."
        ),
        "stories": ["おきゃくさまが いらっしゃる"],
        "content": """
<h2>PJ-69: Keigo 2: <ruby>尊敬語<rt>そんけいご</rt></ruby> — お〜になる va maxsus feʼllar</h2>

<p>Kecha siz uch tarmoqni koʻrdingiz. Bugun birinchisini
ochamiz: <b><ruby>尊敬語<rt>そんけいご</rt></ruby></b> —
suhbatdoshning ishini koʻtaradigan shakl.</p>

<p>Bitta qoidani takrorlab qoʻyamiz, chunki u yerda butun
dars turibdi: <b>bu shakl hech qachon oʻzingiz haqingizda
ishlatilmaydi.</b> U faqat <em>boshqa odamning</em> ishiga
qoʻyiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uchta yasash yoʻlini oʻrganasiz</li>
    <li>Beshta maxsus feʼlni yodlab olasiz</li>
    <li>Ularning ます shaklidagi istisnoni bilib olasiz</li>
    <li>Qaysi yoʻl qachon ishlatilishini tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch yoʻl</span>
  <span class="pe-chip pe-chip--v">maxsus feʼl</span>
  <span class="pe-op">&gt;</span>
  <span class="pe-chip pe-chip--s">お〜になる</span>
  <span class="pe-op">&gt;</span>
  <span class="pe-chip pe-chip--adv">passiv shakl</span>
</div>

<h3>1. Birinchi yoʻl: maxsus feʼllar</h3>

<p>Eng koʻp ishlatiladigan feʼllarning oʻz
<ruby>尊敬語<rt>そんけいご</rt></ruby> soʻzi bor. Bular
yodlanadi — qoida yoʻq.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oddiy feʼl</th><th><ruby>尊敬語<rt>そんけいご</rt></ruby></th><th>ます shakli</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">いる · <ruby>行<rt>い</rt></ruby>く · <ruby>来<rt>く</rt></ruby>る</td>
      <td class="pj-end">いらっしゃる</td><td class="pj-res">いらっしゃ<b>い</b>ます</td>
      <td class="pj-uz">boʻlmoq, bormoq, kelmoq</td></tr>
  <tr><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べる · <ruby>飲<rt>の</rt></ruby>む</td>
      <td class="pj-end"><ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がる</td>
      <td class="pj-res"><ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がります</td>
      <td class="pj-uz">yemoq, ichmoq</td></tr>
  <tr><td class="pj-stem"><ruby>言<rt>い</rt></ruby>う</td>
      <td class="pj-end">おっしゃる</td><td class="pj-res">おっしゃ<b>い</b>ます</td>
      <td class="pj-uz">aytmoq</td></tr>
  <tr><td class="pj-stem">する</td>
      <td class="pj-end">なさる</td><td class="pj-res">なさ<b>い</b>ます</td>
      <td class="pj-uz">qilmoq</td></tr>
  <tr><td class="pj-stem"><ruby>見<rt>み</rt></ruby>る</td>
      <td class="pj-end">ご<ruby>覧<rt>らん</rt></ruby>になる</td>
      <td class="pj-res">ご<ruby>覧<rt>らん</rt></ruby>になります</td>
      <td class="pj-uz">koʻrmoq</td></tr>
  <tr><td class="pj-stem"><ruby>知<rt>し</rt></ruby>っている</td>
      <td class="pj-end">ご<ruby>存<rt>ぞん</rt></ruby>じだ</td>
      <td class="pj-res">ご<ruby>存<rt>ぞん</rt></ruby>じです</td>
      <td class="pj-uz">bilmoq</td></tr>
  <tr><td class="pj-stem">くれる</td>
      <td class="pj-end">くださる</td><td class="pj-res">くださ<b>い</b>ます</td>
      <td class="pj-uz">bermoq (menga)</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>⚠️ Beshta feʼlning ます shakli istisno.</b>
  いらっしゃる, なさる, おっしゃる, くださる va ござる —
  bularda <b>り → い</b> boʻladi:
  いらっしゃ<b>い</b>ます, なさ<b>い</b>ます,
  おっしゃ<b>い</b>ます, くださ<b>い</b>ます, ござ<b>い</b>ます.
  Oddiy qoida boʻyicha «いらっしゃ<s>り</s>ます» chiqardi —
  lekin bunday shakl <em>yoʻq</em>. Butun keigo blokidagi eng
  koʻp qilinadigan xato shu.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>ください — endi tushunarli boʻldi.</b> PJ-32 dan beri
  siz <ruby>待<rt>ま</rt></ruby>ってください deb yozasiz.
  U aslida <b>くださる</b> ning buyruq shakli — yaʼni PJ-67
  dagi <ruby>命令形<rt>めいれいけい</rt></ruby>. Shuning uchun u くださり emas, <b>ください</b>.
  Uch dars bir joyda uchrashdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>先生<rt>せんせい</rt></ruby>は<ruby>何<rt>なん</rt></ruby>とおっしゃいましたか。</p>
  <p class="pe-ex__uz">Oʻqituvchi nima dedilar?</p>
  <p class="pe-ex__why">おっしゃ<b>い</b>ます — り emas. Beshta istisnodan biri.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham alohida hurmat soʻzlari bor.</b>
  «Vafot etdilar» — «oʻldi» emas; «tashrif buyurdilar» —
  «keldi» emas; «marhamat qildilar» — «berdi» emas. Bu
  soʻzlarni siz qoidadan yasamaysiz, ularni <em>yodlaysiz</em>.
  Yaponcha <ruby>尊敬語<rt>そんけいご</rt></ruby> feʼllari ham xuddi
  shunday ishlaydi — shuning uchun ularni grammatika deb emas,
  <b>lugʻat</b> deb oʻrganing.</p>
</div>

<h3>2. Ikkinchi yoʻl: お + ます-oʻzak + になる</h3>

<p>Maxsus feʼli yoʻq feʼllar uchun mahsuldor qolip bor:
<b>お</b> + ます-oʻzagi + <b>になる</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>ます-oʻzagi</th><th><ruby>尊敬語<rt>そんけいご</rt></ruby></th></tr>
  <tr><td class="pj-stem"><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-end"><ruby>読<rt>よ</rt></ruby>み</td>
      <td class="pj-res">お<ruby>読<rt>よ</rt></ruby>みになる</td></tr>
  <tr><td class="pj-stem"><ruby>書<rt>か</rt></ruby>く</td><td class="pj-end"><ruby>書<rt>か</rt></ruby>き</td>
      <td class="pj-res">お<ruby>書<rt>か</rt></ruby>きになる</td></tr>
  <tr><td class="pj-stem"><ruby>待<rt>ま</rt></ruby>つ</td><td class="pj-end"><ruby>待<rt>ま</rt></ruby>ち</td>
      <td class="pj-res">お<ruby>待<rt>ま</rt></ruby>ちになる</td></tr>
  <tr><td class="pj-stem"><ruby>使<rt>つか</rt></ruby>う</td><td class="pj-end"><ruby>使<rt>つか</rt></ruby>い</td>
      <td class="pj-res">お<ruby>使<rt>つか</rt></ruby>いになる</td></tr>
  <tr><td class="pj-stem"><ruby>出<rt>で</rt></ruby>かける</td><td class="pj-end"><ruby>出<rt>で</rt></ruby>かけ</td>
      <td class="pj-res">お<ruby>出<rt>で</rt></ruby>かけになる</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>ます-oʻzagi tanish narsa.</b> PJ-20 da siz uni
  <ruby>読<rt>よ</rt></ruby>み<b>ます</b> da koʻrgansiz, PJ-39 da
  <ruby>読<rt>よ</rt></ruby>み<b>たい</b> da, PJ-67 da
  <ruby>読<rt>よ</rt></ruby>み<b>なさい</b> da. Bugun toʻrtinchi
  marta. Yaʼni bu ham yangi oʻzak emas.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Maxsus feʼli bor feʼllarga bu qolip qoʻyilmaydi.</b>
  «お<ruby>行<rt>い</rt></ruby>きになる» va
  «お<ruby>食<rt>た</rt></ruby>べになる» — notabiiy.
  Ular uchun いらっしゃる va
  <ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がる bor.
  Shuningdek する va <ruby>来<rt>く</rt></ruby>る ham お-qolipini
  olmaydi.</p>
</div>

<p>Bu qolipning qulayligi shundaki, u <b>deyarli har qanday
feʼlga</b> qoʻyiladi — yodlash kerak emas, yasash kifoya.
Shuning uchun maxsus feʼlni eslay olmasangiz, お〜になる
sizni qutqaradi. Yagona shart — feʼlning maxsus
<ruby>尊敬語<rt>そんけいご</rt></ruby> soʻzi boʻlmasligi kerak.</p>

<h3>3. Uchinchi yoʻl: passiv shakl</h3>

<p>PJ-63 dagi passiv shakl <b>yengil hurmat</b> sifatida ham
ishlaydi — va bu keigoning eng oson darajasi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>社長<rt>しゃちょう</rt></ruby>はもう<ruby>帰<rt>かえ</rt></ruby>られました。</p>
  <p class="pe-ex__uz">Direktor allaqachon ketdilar.</p>
  <p class="pe-ex__why">Bu passiv emas — <b>hurmat</b>. Kontekst ajratadi: direktor «qaytarilmaydi».</p>
</div>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name">Passiv shakl</span>
    <span class="pj-level__ja"><ruby>読<rt>よ</rt></ruby>まれる</span>
    <span class="pj-level__who">yengil hurmat — ish joyida kundalik</span>
  </div>
  <div class="pj-level__row pj-level__row--2">
    <span class="pj-level__name">お〜になる</span>
    <span class="pj-level__ja">お<ruby>読<rt>よ</rt></ruby>みになる</span>
    <span class="pj-level__who">oʻrtacha — xizmat koʻrsatishda</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name">Maxsus feʼl</span>
    <span class="pj-level__ja">いらっしゃる</span>
    <span class="pj-level__who">eng kuchli — mijoz, rasmiy marosim</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham uch daraja bor — va siz ularni
  sezasiz.</b> «Keldi» → «kel<b>dilar</b>» → «tashrif
  <b>buyurdilar</b>». Birinchisi betaraf, ikkinchisi
  qoʻshimcha bilan hurmat, uchinchisi esa <em>butunlay
  boshqa soʻz</em>. Yaponcha ham aynan shu uch pogʻonani
  yuradi: qoʻshimcha (passiv) → qolip (お〜になる) → alohida
  soʻz (いらっしゃる). Shuning uchun bu tizim sizga notanish
  emas — faqat u yaponchada ancha keng ishlatiladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">こちらの<ruby>本<rt>ほん</rt></ruby>をご<ruby>覧<rt>らん</rt></ruby>になりますか。</p>
  <p class="pe-ex__uz">Bu kitobni koʻrasizmi?</p>
  <p class="pe-ex__why">Doʻkonda eng koʻp eshitiladigan gaplardan biri.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Nega uch xil yoʻl bor?</b> Chunki hurmat ham
  <em>darajalanadi</em>. Oʻzbekchada siz «keldi» va «keldilar»
  orasida tanlaysiz, lekin uchinchi pogʻona — «tashrif
  buyurdilar» — faqat rasmiy joyda chiqadi. Yaponcha ham
  shunday: passiv shakl ish joyida kundalik, お〜になる
  xizmat koʻrsatishda, maxsus feʼllar esa mijoz va marosim
  uchun. Yaʼni siz bitta narsani emas, <b>bitta
  zinapoyani</b> oʻrganyapsiz.</p>
</div>

<p>Yana bir amaliy joyi bor: bu qolip <b>savolda</b> juda
koʻp ishlatiladi. Doʻkonda xodim sizga hech qachon
«qilasizmi?» demaydi — u «qilasizmi» ni koʻtarib beradi.
Shuning uchun Yaponiyada birinchi kuningizdayoq siz bu
shaklni <em>eshitasiz</em>, garchi oʻzingiz aytmasangiz ham.
Va aynan shu sababdan uni tanish har kuni kerak boʻladi.</p>

<h3>4. Otlar va sifatlarga お / ご</h3>

<p>Suhbatdoshga tegishli narsalarga ham hurmat qoʻshiladi:
yaponcha soʻzga <b>お</b>, xitoycha soʻzga <b>ご</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>お + yaponcha</th><th>ご + xitoycha</th></tr>
  <tr><td class="pj-res">お<ruby>名前<rt>なまえ</rt></ruby> — ismingiz</td>
      <td class="pj-res">ご<ruby>家族<rt>かぞく</rt></ruby> — oilangiz</td></tr>
  <tr><td class="pj-res">お<ruby>電話<rt>でんわ</rt></ruby> — telefoningiz</td>
      <td class="pj-res">ご<ruby>住所<rt>じゅうしょ</rt></ruby> — manzilingiz</td></tr>
  <tr><td class="pj-res">お<ruby>時間<rt>じかん</rt></ruby> — vaqtingiz</td>
      <td class="pj-res">ご<ruby>意見<rt>いけん</rt></ruby> — fikringiz</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Qoida 100% emas, lekin 90% ishlaydi.</b> Soʻzning
  oʻqilishi <em>kun</em> boʻlsa — <b>お</b>; <em>on</em> boʻlsa
  — <b>ご</b>. PJ-11 dagi ikki oʻqilish shu yerda ishga
  tushdi. Istisnolar bor
  (お<ruby>電話<rt>でんわ</rt></ruby>, お<ruby>茶<rt>ちゃ</rt></ruby>),
  lekin ularni alohida yodlash osonroq.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">尊</span>
    <span class="pj-kanji__uz">hurmat qilmoq</span>
    <span class="pj-kanji__on">オン: ソン</span>
    <span class="pj-kanji__kun">KUN: たっと(い)</span>
    <span class="pj-kanji__note">尊敬 (そんけい) — hurmat · <ruby>尊敬語<rt>そんけいご</rt></ruby> (そんけいご)</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">召</span>
    <span class="pj-kanji__uz">chaqirmoq (hurmat)</span>
    <span class="pj-kanji__on">オン: ショウ</span>
    <span class="pj-kanji__kun">KUN: め(す)</span>
    <span class="pj-kanji__note">召し上がる (めしあがる) — yemoq (<ruby>尊敬語<rt>そんけいご</rt></ruby>)</span>
  </div>
</div>

<p>Bu uch yoʻl bir gapda aralashtirilmaydi. Agar mijoz bilan
gapirayotgan boʻlsangiz, butun gap bir darajada turishi kerak
— bittasi maxsus feʼl, ikkinchisi passiv shakl boʻlsa, gap
notekis eshitiladi. Yapon xizmat koʻrsatish tilida bu
<em>eng koʻp seziladigan</em> xato, chunki u odamning
tajribasizligini darrov koʻrsatib qoʻyadi.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ いらっしゃります</p>
  <p class="pe-fix__good">✓ いらっしゃ<b>い</b>ます — beshta istisno feʼlda り → い.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>はお<ruby>読<rt>よ</rt></ruby>みになります</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby>は<ruby>読<rt>よ</rt></ruby>みます — <ruby>尊敬語<rt>そんけいご</rt></ruby> oʻzingizga ishlatilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ お<ruby>行<rt>い</rt></ruby>きになる</p>
  <p class="pe-fix__good">✓ いらっしゃる — maxsus feʼli bor feʼlga お-qolipi qoʻyilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ご<ruby>名前<rt>なまえ</rt></ruby></p>
  <p class="pe-fix__good">✓ お<ruby>名前<rt>なまえ</rt></ruby> — <ruby>名前<rt>なまえ</rt></ruby> kun-oʻqilish, demak <b>お</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. いらっしゃる ning ます shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>いらっしゃいます</b> — り emas, <b>い</b>. Bu istisno.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>読<rt>よ</rt></ruby>む ni お〜になる qolipiga qoʻying.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>お<ruby>読<rt>よ</rt></ruby>みになる</b> — ます-oʻzagi <ruby>読<rt>よ</rt></ruby>み.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Mijoz yeyayaptilar» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>お<ruby>客<rt>きゃく</rt></ruby>さまが<ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がります</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. ご<ruby>家族<rt>かぞく</rt></ruby> nega ご oladi, お emas?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki <ruby>家族<rt>かぞく</rt></ruby> — <b>on-oʻqilish</b> (xitoycha soʻz). Kun-oʻqilishga お qoʻyiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Keigoning eng oson darajasi qaysi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Passiv shakl</b> — <ruby>読<rt>よ</rt></ruby>まれる, <ruby>帰<rt>かえ</rt></ruby>られる. Siz uni PJ-63 dan beri yasay olasiz.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>いらっしゃる</b> — boʻlmoq, bormoq, kelmoq (<ruby>尊敬語<rt>そんけいご</rt></ruby>)</li>
  <li><b><ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がる</b> — yemoq, ichmoq</li>
  <li><b>おっしゃる</b> — aytmoq</li>
  <li><b>なさる</b> — qilmoq</li>
  <li><b>くださる</b> — bermoq (menga)</li>
  <li><b>ご<ruby>覧<rt>らん</rt></ruby>になる</b> — koʻrmoq</li>
  <li><b>ご<ruby>存<rt>ぞん</rt></ruby>じだ</b> — bilmoq</li>
  <li><b>お〜になる</b> — mahsuldor <ruby>尊敬語<rt>そんけいご</rt></ruby> qolipi</li>
  <li><b><ruby>社長<rt>しゃちょう</rt></ruby></b> — kompaniya direktori</li>
  <li><b>お<ruby>客<rt>きゃく</rt></ruby>さま</b> — mijoz</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Uch yoʻl: <b>maxsus feʼl &gt; お〜になる &gt; passiv shakl</b>.</li>
    <li>Beshta istisno feʼlda <b>り → い</b>: いらっしゃいます.</li>
    <li><b>Hech qachon oʻzingiz haqingizda</b>.</li>
  </ul>
</div>
""",
    },
]
