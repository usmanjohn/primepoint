# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-76, PJ-77, PJ-78: Blok E yopiladi.

Uchala dars bir narsa haqida: **yapon tili kim gapirayotganiga qarab
oʻzgaradi**. PJ-73…75 «qayerdan bilaman» oʻqini qurgan edi; bu batch
uning ustiga **register** oʻqini qoʻyadi.
    PJ-76 — みたい: ようだ ning kundalik egizagi (grammatikasi osonroq,
            registri pastroq). Beshta taxmin qolipi bitta jadvalda yopiladi.
    PJ-77 — 擬音語・擬態語: lugʻatda topilmaydigan, lekin har kuni
            eshitiladigan qatlam. Katakana/hiragana boʻlinishi — PJ-7 va
            PJ-9 ga qaytish.
    PJ-78 — kim qanday gapiradi: 僕/俺/あたし, ぞ/ぜ/わ/かしら, yoshlar
            tili, manga yaponchasi. «Tanib oling, ishlatmang» darsi.

⚠️ PJ-76 ning eng katta tuzogʻi grammatika emas, **omonim**:
みたい (oʻxshaydi) ≠ <ruby>見<rt>み</rt></ruby>たい (koʻrgim bor).
Ajratuvchi belgi — oldidagi qoʻshimcha: 映画**が**見たい ↔ 映画みたい.

⚠️ PJ-78 rostini aytadi: erkak/ayol nutqi chegarasi zamonaviy yapon
tilida **yumshayapti**. Dars uni faktdek emas, ohangdek beradi, va
chet ellik oʻquvchiga eng xavfsiz yoʻlni koʻrsatadi — <ruby>丁寧体<rt>ていねいたい</rt></ruby> va 私.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_76_78.py --author=prime
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
        "title": "PJ-76: 〜みたいです va oddiy nutqdagi taqqoslash",
        "category": "japanese",
        "order": 76,
        "summary": (
            "みたい — ようだ ning kundalik egizagi: maʼnosi bir xil, "
            "grammatikasi osonroq, registri pastroq. Dars oxirida "
            "beshta taxmin qolipi bitta jadvalga yigʻiladi."
        ),
        "stories": ["みたいな こえ"],
        "content": """
<h2>PJ-76: 〜みたいです va oddiy nutqdagi taqqoslash</h2>

<p>Yaponcha film koʻrayapsiz. Qahramon derazaga qaraydi va
«<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>るみたい»
deydi. Siz kechagi darsda buni
«<ruby>降<rt>ふ</rt></ruby>るようです» deb oʻrgandingiz.</p>

<p>Ikkalasi <b>bir xil narsani</b> bildiradi. Lekin biri
darslikda, ikkinchisi suhbatda yashaydi — va shuning uchun
kinoda, ijtimoiy tarmoqda, doʻstlar orasida siz deyarli doim
<b>みたい</b> ni eshitasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>みたい ni har qanday soʻzga toʻgʻri ulaysiz</li>
    <li>みたい bilan ようだ orasidagi <em>register</em> farqini bilasiz</li>
    <li>みたいな / みたいに bilan oʻxshatish yasaysiz</li>
    <li>みたい ni <ruby>見<rt>み</rt></ruby>たい dan ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kundalik taxmin</span>
  <span class="pe-chip pe-chip--s">oddiy shakl</span>
  <span class="pe-op">/</span>
  <span class="pe-chip pe-chip--o">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">みたいです</span>
</div>

<h3>1. Grammatikasi — darsning eng oson qismi</h3>

<p>みたい <b>hamma narsaga yalangʻoch ulanadi</b>. Na だ, na な,
na の. Yaʼni ulanish jihatidan u らしい bilan bir xil, maʼno
jihatidan esa ようだ bilan.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Soʻz</th><th>ようです</th><th>みたいです</th></tr>
  <tr><td class="pj-stem">feʼl</td><td class="pj-end"><ruby>降<rt>ふ</rt></ruby>る</td>
      <td class="pj-uz"><ruby>降<rt>ふ</rt></ruby>るようです</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>るみたいです</td></tr>
  <tr><td class="pj-stem">feʼl, oʻtgan</td><td class="pj-end"><ruby>降<rt>ふ</rt></ruby>った</td>
      <td class="pj-uz"><ruby>降<rt>ふ</rt></ruby>ったようです</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>ったみたいです</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end"><ruby>高<rt>たか</rt></ruby>い</td>
      <td class="pj-uz"><ruby>高<rt>たか</rt></ruby>いようです</td>
      <td class="pj-res"><ruby>高<rt>たか</rt></ruby>いみたいです</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end"><ruby>元気<rt>げんき</rt></ruby></td>
      <td class="pj-uz"><ruby>元気<rt>げんき</rt></ruby><b>な</b>ようです</td>
      <td class="pj-res"><ruby>元気<rt>げんき</rt></ruby>みたいです</td></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-end"><ruby>学生<rt>がくせい</rt></ruby></td>
      <td class="pj-uz"><ruby>学生<rt>がくせい</rt></ruby><b>の</b>ようです</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>みたいです</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Oxirgi ikki qatorni yodlasangiz, dars tugadi.</b>
  ようだ <b>な</b> va <b>の</b> talab qilardi; みたい <em>hech
  nima</em> talab qilmaydi. Shuning uchun «<ruby>元気<rt>げんき</rt></ruby>
  なみたいです» va «<ruby>学生<rt>がくせい</rt></ruby>のみたいです» —
  ikkalasi ham xato.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>先生<rt>せんせい</rt></ruby>は<ruby>今日<rt>きょう</rt></ruby><span class="pe-hl pe-hl--o"><ruby>忙<rt>いそが</rt></ruby>しいみたいです</span>。</p>
  <p class="pe-ex__uz">Oʻqituvchi bugun bandga oʻxshaydi.</p>
  <p class="pe-ex__why">Dalil menda — koridorda yugurib ketayotganini koʻrdim. Maʼnosi «<ruby>忙<rt>いそが</rt></ruby>しいようです» bilan bir xil, ohangi yengilroq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">パリさんのお<ruby>姉<rt>ねえ</rt></ruby>さんは<span class="pe-hl pe-hl--o"><ruby>医者<rt>いしゃ</rt></ruby>みたいです</span>よ。</p>
  <p class="pe-ex__uz">Parining opasi shifokorga oʻxshaydi-a.</p>
  <p class="pe-ex__why">Otdan keyin <b>hech qanday qoʻshimcha yoʻq</b>. «<ruby>医者<rt>いしゃ</rt></ruby>のみたい» xato.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">あの<ruby>二人<rt>ふたり</rt></ruby>は<ruby>喧嘩<rt>けんか</rt></ruby>した<span class="pe-hl pe-hl--v">みたいですね</span>。</p>
  <p class="pe-ex__uz">Anavi ikkovi urishib qolganga oʻxshaydi-a.</p>
  <p class="pe-ex__why">Oʻtgan zamon <b>gapning ichida</b> turadi — <ruby>喧嘩<rt>けんか</rt></ruby>した, keyin みたい. PJ-74 dagi そうです bilan bir xil mantiq.</p>
</div>

<h3>2. Register — darsning asl mazmuni</h3>

<p>みたい va ようだ orasidagi farq maʼnoda emas,
<b>qayerda ishlatilishida</b>.</p>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name">みたい</span>
    <span class="pj-level__ja"><ruby>降<rt>ふ</rt></ruby>るみたい</span>
    <span class="pj-level__who">doʻstlar, oila, xabar, kino — kundalik nutq</span>
  </div>
  <div class="pj-level__row pj-level__row--2">
    <span class="pj-level__name">みたいです</span>
    <span class="pj-level__ja"><ruby>降<rt>ふ</rt></ruby>るみたいです</span>
    <span class="pj-level__who">muloyim, lekin hamon kundalik — oʻqituvchi bilan boʻladi</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name">ようです</span>
    <span class="pj-level__ja"><ruby>降<rt>ふ</rt></ruby>るようです</span>
    <span class="pj-level__who">yozma til, hisobot, yangilik, rasmiy nutq</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham aynan shu juftlik bor, faqat ikki
  boshqa soʻz bilan.</b> «Yomgʻir yogʻadi<em>ganga
  oʻxshaydi</em>» — kundalik; «goʻyo yomgʻir
  yogʻadi», «yogʻsa kerak, chogʻi» — kitobiy. Hech kim insho
  yozganda «oʻxshaydi-oʻxshaydi» deb yozmaydi, va hech kim
  doʻstiga «goʻyo» demaydi. Yaponcha ham xuddi shunday
  ishlaydi — <b>maʼno bir xil, kiyim boshqa</b>. Shuning uchun
  みたい ni «xato» deb emas, «boshqa kiyim» deb yodlang: uni
  rasmiy matnda ishlatsangiz, gap notoʻgʻri boʻlmaydi —
  <em>joyida boʻlmaydi</em>.</p>
</div>

<h3>3. みたいな + ot, みたいに + feʼl</h3>

<p>みたい ham <b>な-sifat kabi</b> tuslanadi — PJ-73 dagi
そうな / そうに va PJ-75 dagi ような / ように bilan bir xil ikki
uyacha.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>子供<rt>こども</rt></ruby></span>
  <span class="pj-joshi__p">みたいな<small>+ OT</small></span>
  <span class="pj-joshi__n"><ruby>声<rt>こえ</rt></ruby></span>
  <span class="pj-joshi__uz">bolanikiga oʻxshagan ovoz</span>
</div>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>子供<rt>こども</rt></ruby></span>
  <span class="pj-joshi__p">みたいに<small>+ FEʼL</small></span>
  <span class="pj-joshi__v"><ruby>泣<rt>な</rt></ruby>いた</span>
  <span class="pj-joshi__uz">boladek yigʻladi</span>
</div>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">Kundalik</p>
    <p><ruby>雪<rt>ゆき</rt></ruby>みたいに<ruby>白<rt>しろ</rt></ruby>い</p>
    <p>Otdan keyin <b>hech nima yoʻq</b>.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">Kitobiy</p>
    <p><ruby>雪<rt>ゆき</rt></ruby><b>の</b>ように<ruby>白<rt>しろ</rt></ruby>い</p>
    <p>Otdan keyin <b>の</b> kerak.</p></div>
</div>

<h3>4. ⚠️ みたい ≠ <ruby>見<rt>み</rt></ruby>たい</h3>

<p>Bu darsning eng koʻp adashtiradigan joyi grammatika emas:
yapon tilida <b>bir xil eshitiladigan ikki boshqa soʻz</b> bor.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">みたい — oʻxshaydi</p>
    <p><ruby>映画<rt>えいが</rt></ruby>みたいです。</p>
    <p>«Kinoga oʻxshaydi». Otdan keyin <b>qoʻshimcha yoʻq</b>.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h"><ruby>見<rt>み</rt></ruby>たい — koʻrgim bor</p>
    <p><ruby>映画<rt>えいが</rt></ruby>が<ruby>見<rt>み</rt></ruby>たいです。</p>
    <p>PJ-39 dagi 〜たい. Oldida <b>が</b> (yoki を) turadi.</p></div>
</div>

<div class="pe-call pe-warn">
  <p><b>Ajratuvchi belgi — qoʻshimcha.</b>
  <ruby>見<rt>み</rt></ruby>たい — feʼl
  (<ruby>見<rt>み</rt></ruby>る + たい), shuning uchun oldida
  toʻldiruvchi va uning qoʻshimchasi boʻladi:
  <ruby>映画<rt>えいが</rt></ruby><b>が</b><ruby>見<rt>み</rt></ruby>たい.
  みたい esa otga <em>tegib</em> turadi, orada hech nima yoʻq:
  <ruby>映画<rt>えいが</rt></ruby>みたい. Yozuvda ham farq
  koʻrinadi — biri kanji bilan, biri kana bilan yoziladi.</p>
</div>

<h3>5. Kundalik taqqoslashning ikki feʼli</h3>

<p>Oʻxshashlikni <em>qolip</em> bilan emas, <b>feʼl</b> bilan ham
aytish mumkin — va kundalik nutqda koʻpincha shunday
qilinadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Qolip</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem"><ruby>似<rt>に</rt></ruby>ている</td>
      <td class="pj-end">A は B <b>に</b><ruby>似<rt>に</rt></ruby>ている</td>
      <td class="pj-res">イノムさんはお<ruby>父<rt>とう</rt></ruby>さん<b>に</b><ruby>似<rt>に</rt></ruby>ています</td>
      <td class="pj-uz">Inom otasiga oʻxshaydi</td></tr>
  <tr><td class="pj-stem"><ruby>比<rt>くら</rt></ruby>べる</td>
      <td class="pj-end">A <b>と</b> B <b>を</b><ruby>比<rt>くら</rt></ruby>べる</td>
      <td class="pj-res"><ruby>二<rt>ふた</rt></ruby>つの<ruby>店<rt>みせ</rt></ruby>を<ruby>比<rt>くら</rt></ruby>べました</td>
      <td class="pj-uz">Ikki doʻkonni taqqosladim</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b><ruby>似<rt>に</rt></ruby>ている ning qoʻshimchasi
  oʻzbekchadan koʻchiriladi — va bu kamdan-kam hol.</b>
  Oʻzbekcha «ota<em>ga</em> oʻxshaydi» deydi: <b>-ga</b>.
  Yaponcha ham <b>に</b> ishlatadi — oʻsha uyacha, oʻsha
  maʼno (PJ-21). Shuning uchun «<ruby>父<rt>ちち</rt></ruby>と
  <ruby>似<rt>に</rt></ruby>ています» degan xato aslida oʻzbekcha
  emas, ruscha yoki inglizcha fikrlashdan kelib chiqadi.
  Oʻzbekchaga ishoning: «-ga» → <b>に</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Omonimdan qoʻrqmang — oʻzbekchada ham xuddi shunday
  juftliklar bor.</b> «Bordi» — kim bordi? «Bor» soʻzidan
  yasalganmi yoki «bormoq» dan? Oʻzbek oʻquvchi bunday
  savolni hech qachon bermaydi, chunki <em>gap ichida</em>
  savol tugʻilmaydi: atrofdagi soʻzlar javobni oʻzi beradi.
  Yaponchada ham shunday — みたい va
  <ruby>見<rt>み</rt></ruby>たい bir xil eshitilsa ham,
  gap ichida ularni <b>qoʻshimcha</b> ajratadi va
  adashish deyarli imkonsiz. Shuning uchun bu juftlikni
  yodlashning eng yaxshi yoʻli — ikki tayyor gapni yonma-yon
  yodlash: <ruby>映画<rt>えいが</rt></ruby>みたい ↔
  <ruby>映画<rt>えいが</rt></ruby>が<ruby>見<rt>み</rt></ruby>たい.</p>
</div>

<h3>6. Beshta taxmin bitta jadvalda</h3>

<p>Toʻrt dars davomida siz beshta qolip koʻrdingiz. Ularni
ikki oʻq ajratadi: <b>qayerdan bilaman</b> va <b>qanday
gapirayapman</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Qayerdan bilaman</th><th>Register</th></tr>
  <tr><td class="pj-stem"><ruby>降<rt>ふ</rt></ruby>り<b>そうです</b></td>
      <td class="pj-uz">bulutni <b>koʻryapman</b></td>
      <td class="pj-res">hamma joyda</td></tr>
  <tr><td class="pj-stem"><ruby>降<rt>ふ</rt></ruby>る<b>そうです</b></td>
      <td class="pj-uz">aniq manbadan <b>eshitdim</b></td>
      <td class="pj-res">yangilik, rasmiy</td></tr>
  <tr><td class="pj-stem"><ruby>降<rt>ふ</rt></ruby>る<b>ようです</b></td>
      <td class="pj-uz">dalil bor, <b>xulosa meniki</b></td>
      <td class="pj-res">yozma, rasmiy</td></tr>
  <tr><td class="pj-stem"><ruby>降<rt>ふ</rt></ruby>る<b>らしいです</b></td>
      <td class="pj-uz"><b>odamlar</b> shunday deyishdi</td>
      <td class="pj-res">suhbat</td></tr>
  <tr><td class="pj-stem"><ruby>降<rt>ふ</rt></ruby>る<b>みたいです</b></td>
      <td class="pj-uz">dalil bor, <b>xulosa meniki</b></td>
      <td class="pj-res">faqat kundalik</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Uchinchi va beshinchi qator bir xil — va bu xato
  emas.</b> ようだ bilan みたい aynan bir maʼnoni beradi;
  ularni <em>register</em> ajratadi, mantiq emas. Shuning
  uchun bu jadvalni yodlaganda ikki ustunni birga oʻqing:
  «nimani bilaman» va «kim bilan gapirayapman». Yapon
  tilining butun mantiqi shu ikki savolda.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">似</span>
    <span class="pj-kanji__uz">oʻxshamoq</span>
    <span class="pj-kanji__on">オン: ジ</span>
    <span class="pj-kanji__kun">KUN: に(る)</span>
    <span class="pj-kanji__note">似ている (にている) — oʻxshaydi · 似合う (にあう) — mos tushmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">比</span>
    <span class="pj-kanji__uz">taqqoslamoq</span>
    <span class="pj-kanji__on">オン: ヒ</span>
    <span class="pj-kanji__kun">KUN: くら(べる)</span>
    <span class="pj-kanji__note">比べる (くらべる) — taqqoslamoq · 比較 (ひかく) — taqqoslash</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby><b>の</b>みたいです</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby>みたいです — みたい otga <b>yalangʻoch</b> ulanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>元気<rt>げんき</rt></ruby><b>な</b>みたいです</p>
  <p class="pe-fix__good">✓ <ruby>元気<rt>げんき</rt></ruby>みたいです — な ようだ uchun, みたい uchun emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>子供<rt>こども</rt></ruby>みたい<b>な</b><ruby>泣<rt>な</rt></ruby>いた</p>
  <p class="pe-fix__good">✓ <ruby>子供<rt>こども</rt></ruby>みたい<b>に</b><ruby>泣<rt>な</rt></ruby>いた — feʼldan oldin <b>に</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>映画<rt>えいが</rt></ruby>をみたいです<br><small>(«kinoni koʻrgim bor» demoqchi boʻlsangiz)</small></p>
  <p class="pe-fix__good">✓ <ruby>映画<rt>えいが</rt></ruby>が<ruby>見<rt>み</rt></ruby>たいです — <ruby>見<rt>み</rt></ruby>たい butunlay boshqa soʻz.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>父<rt>ちち</rt></ruby><b>と</b><ruby>似<rt>に</rt></ruby>ています</p>
  <p class="pe-fix__good">✓ <ruby>父<rt>ちち</rt></ruby><b>に</b><ruby>似<rt>に</rt></ruby>ています — oʻzbekcha «ota<b>ga</b> oʻxshaydi» bilan bir xil uyacha.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>元気<rt>げんき</rt></ruby> ni みたいです bilan bogʻlang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>元気<rt>げんき</rt></ruby>みたいです</b> — na だ, na な, na の. ようだ esa <ruby>元気<rt>げんき</rt></ruby><b>な</b>ようです.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Rasmiy hisobotda qaysi qolipni tanlaysiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ようです</b>. みたい faqat kundalik nutqda — maʼnosi bir xil, lekin joyi boshqa.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Boladek yigʻladi» — みたいな yoki みたいに?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>子供<rt>こども</rt></ruby>みたいに<ruby>泣<rt>な</rt></ruby>いた</b> — feʼldan oldin <b>に</b>, otdan oldin な.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>映画<rt>えいが</rt></ruby>みたいです» va «<ruby>映画<rt>えいが</rt></ruby>が<ruby>見<rt>み</rt></ruby>たいです» — farqi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisi — «kinoga oʻxshaydi», ikkinchisi — «kinoni koʻrgim bor». Ajratuvchi belgi — <b>が</b> qoʻshimchasi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Inom otasiga oʻxshaydi» — qaysi qoʻshimcha?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>に</b> — イノムさんはお<ruby>父<rt>とう</rt></ruby>さん<b>に</b><ruby>似<rt>に</rt></ruby>ています. と emas.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜みたいです</b> — …ga oʻxshaydi (kundalik)</li>
  <li><b>〜みたいな + ot</b> — …ga oʻxshagan</li>
  <li><b>〜みたいに + feʼl</b> — …dek</li>
  <li><b><ruby>見<rt>み</rt></ruby>たい</b> — koʻrgim bor (boshqa soʻz!)</li>
  <li><b><ruby>似<rt>に</rt></ruby>ている</b> — oʻxshaydi</li>
  <li><b><ruby>比<rt>くら</rt></ruby>べる</b> — taqqoslamoq</li>
  <li><b><ruby>忙<rt>いそが</rt></ruby>しい</b> — band</li>
  <li><b><ruby>映画<rt>えいが</rt></ruby></b> — kino</li>
  <li><b><ruby>声<rt>こえ</rt></ruby></b> — ovoz</li>
  <li><b><ruby>似合<rt>にあ</rt></ruby>う</b> — mos tushmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>みたい <b>yalangʻoch</b> ulanadi — na だ, na な, na の.</li>
    <li>ようだ = みたい maʼno jihatidan; ularni <b>register</b> ajratadi.</li>
    <li>みたい ≠ <ruby>見<rt>み</rt></ruby>たい — ajratuvchi belgi oldidagi <b>が</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-77: 擬音語・擬態語 — tovush va holat taqlidi soʻzlari",
        "category": "japanese",
        "order": 77,
        "summary": (
            "Lugʻatda topilmaydigan, lekin har kuni eshitiladigan "
            "qatlam. Oʻzbek tili bu yerda kuchli yordam beradi: "
            "shildir-shildir, taqa-taq, sekin-sekin — bir xil mexanizm."
        ),
        "stories": ["あめの おと"],
        "content": """
<h2>PJ-77: <ruby>擬音語<rt>ぎおんご</rt></ruby>・<ruby>擬態語<rt>ぎたいご</rt></ruby></h2>

<p>Yaponcha kitob oʻqiyapsiz. Bir qatorda «ザーザー» deb
yozilgan. Lugʻatga qaraysiz — yoʻq. Grammatikaga qaraysiz —
yoʻq. Lekin gap tushunarli: yomgʻir <b>quyib</b> yogʻyapti.</p>

<p>Yapon tilida bunday soʻzlar <b>mingdan oshadi</b>, va ular
lugʻatning chetidagi qiziq narsa emas — ularsiz yaponcha quruq
va bolalarcha boʻlib qoladi. Bugun ularning tizimini
koʻrasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><ruby>擬音語<rt>ぎおんご</rt></ruby> bilan <ruby>擬態語<rt>ぎたいご</rt></ruby> ni ajratasiz</li>
    <li>Nega biri katakana, ikkinchisi hiragana bilan yozilishini bilasiz</li>
    <li>Ularni gapga uch yoʻl bilan qoʻshasiz</li>
    <li>Eng koʻp uchraydigan yigirmatasini yodlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch yoʻl</span>
  <span class="pe-chip pe-chip--adv">taqlid soʻzi</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">feʼl</span>
  <span class="pe-op">/</span>
  <span class="pe-chip pe-chip--v">する</span>
  <span class="pe-op">/</span>
  <span class="pe-chip pe-chip--aux">だ</span>
</div>

<h3>1. Ikki turi</h3>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h"><ruby>擬音語<rt>ぎおんご</rt></ruby> — TOVUSH</p>
    <p class="pj-pair__form">ザーザー</p>
    <p>Quloq eshitadigan narsa: yomgʻir, eshik, it, momaqaldiroq. Odatda <b>katakana</b>.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h"><ruby>擬態語<rt>ぎたいご</rt></ruby> — HOLAT</p>
    <p class="pj-pair__form">きらきら</p>
    <p>Tovushi yoʻq narsa: yaltirash, charchash, hayajon. Odatda <b>hiragana</b>.</p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>Yozuv qoidasi — PJ-7 va PJ-9 ga qaytish.</b> Katakana
  chet soʻzlar uchun emas edi: u <em>«bu soʻz oddiy yapon soʻzi
  emas»</em> degan belgi. Tovush ham shunday — u soʻz emas,
  <b>shovqin</b>, shuning uchun katakana. Holat esa
  <em>tuygʻu</em>, va tuygʻu yaponcha — shuning uchun hiragana.
  Qoida qatʼiy emas (mangada ikkalasi ham katakana boʻlishi
  mumkin), lekin roman va gazetada shu tartib ishlaydi.</p>
</div>

<h3>2. Shakli — toʻrt qolip</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">AB-AB (takrorlanish)</td><td class="pj-end">きらきら · ドキドキ · ワンワン</td>
      <td class="pj-uz">davomli, takroriy ish</td></tr>
  <tr><td class="pj-stem">A-っ-と</td><td class="pj-end">ぱっと · さっと · ぐっと</td>
      <td class="pj-uz">bir lahzalik, tez ish</td></tr>
  <tr><td class="pj-stem">AB-り</td><td class="pj-end">ゆっくり · しっかり · のんびり</td>
      <td class="pj-uz">holat, tarz</td></tr>
  <tr><td class="pj-stem">AB-ん</td><td class="pj-end">ぴょんぴょん · どんどん</td>
      <td class="pj-uz">zarb bilan takrorlanish</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu darsda oʻzbek tili sizni deyarli yetaklab boradi.</b>
  Oʻzbekchada ham xuddi shu mexanizm ishlaydi va xuddi shu
  qoliplar bor: <em>shildir-shildir</em>, <em>taqa-taq</em>,
  <em>lip-lip</em>, <em>gurs-gurs</em>, <em>sekin-sekin</em>,
  <em>zir-zir</em>. Yaʼni takrorlanish orqali tovush va
  holat yasash — ikki tilning <b>umumiy</b> odati. Shuning
  uchun bu darsni «yangi grammatika» deb emas,
  «tanish mexanizm, yangi soʻzlar» deb qabul qiling. Va
  tarjima qilganda oʻzbekcha taqlid soʻzini izlang: ザーザー —
  «shovullab», ぽつぽつ — «tomchilab», ぴかぴか —
  «yalt-yalt». Soʻzma-soʻz tarjima bu yerda ishlamaydi.</p>
</div>

<h3>3. Gapga qoʻshishning uch yoʻli</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yoʻl</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">+ feʼl (hol sifatida)</td>
      <td class="pj-end"><ruby>雨<rt>あめ</rt></ruby>がザーザー<ruby>降<rt>ふ</rt></ruby>る</td>
      <td class="pj-uz">yomgʻir shovullab yogʻadi</td></tr>
  <tr><td class="pj-stem">+ する (feʼl yasaydi)</td>
      <td class="pj-end"><ruby>胸<rt>むね</rt></ruby>がドキドキする</td>
      <td class="pj-uz">yurak duk-duk uradi</td></tr>
  <tr><td class="pj-stem">+ だ / です (holat)</td>
      <td class="pj-end">お<ruby>腹<rt>なか</rt></ruby>がぺこぺこだ</td>
      <td class="pj-uz">qornim juda ochdi</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>朝<rt>あさ</rt></ruby>から<ruby>雨<rt>あめ</rt></ruby>が<span class="pe-hl pe-hl--adv">ザーザー</span><ruby>降<rt>ふ</rt></ruby>っている。</p>
  <p class="pe-ex__uz">Ertalabdan yomgʻir shovullab yogʻyapti.</p>
  <p class="pe-ex__why">ザーザー — hol. Qoʻshimcha kerak emas; <b>と</b> qoʻyish ham mumkin, lekin kundalik nutqda tashlab ketiladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>試験<rt>しけん</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>、<ruby>胸<rt>むね</rt></ruby>が<span class="pe-hl pe-hl--v">ドキドキしました</span>。</p>
  <p class="pe-ex__uz">Imtihon oldidan yuragim duk-duk urdi.</p>
  <p class="pe-ex__why">する qoʻshilgani uchun bu endi <b>feʼl</b> — tuslanadi, oʻtgan zamonga kiradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>三時間<rt>さんじかん</rt></ruby><ruby>歩<rt>ある</rt></ruby>いたので、<ruby>足<rt>あし</rt></ruby>が<span class="pe-hl pe-hl--o">くたくたです</span>。</p>
  <p class="pe-ex__uz">Uch soat yurganim uchun oyoqlarim charchab ketdi.</p>
  <p class="pe-ex__why">くたくた — です bilan keladi, する bilan emas. Har bir soʻz oʻz yoʻlini tanlaydi, shuning uchun ular <b>juftlik bilan</b> yodlanadi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Uch yoʻlni oʻzbekcha bilan tekshirib koʻrish mumkin.</b>
  «Shovullab yogʻdi» — taqlid soʻzi feʼlga qoʻshildi, xuddi
  ザーザー<ruby>降<rt>ふ</rt></ruby>る kabi. «Yuragi duk-duk
  qildi» — taqlid soʻzi <em>oʻzi</em> feʼlga aylandi, xuddi
  ドキドキする kabi. «Qornim ochqoq» — taqlid soʻzi
  <em>holat</em> boʻldi, xuddi ぺこぺこだ kabi. Yaʼni uchala
  yoʻl oʻzbekchada ham bor; yodlash kerak boʻlgan narsa —
  qaysi yaponcha soʻz qaysi yoʻlni tanlaydi.</p>
</div>

<h3>4. Eng koʻp uchraydigan yigirmata</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soha</th><th>Soʻz</th><th>Maʼnosi</th><th>Qanday ishlatiladi</th></tr>
  <tr><td class="pj-stem">ob-havo</td><td class="pj-end">ザーザー</td><td class="pj-uz">quyib (yogʻmoq)</td>
      <td class="pj-res">ザーザー<ruby>降<rt>ふ</rt></ruby>る</td></tr>
  <tr><td class="pj-stem">ob-havo</td><td class="pj-end">しとしと</td><td class="pj-uz">mayda, tinim bilan</td>
      <td class="pj-res">しとしと<ruby>降<rt>ふ</rt></ruby>る</td></tr>
  <tr><td class="pj-stem">ob-havo</td><td class="pj-end">ぽつぽつ</td><td class="pj-uz">tomchilab</td>
      <td class="pj-res">ぽつぽつ<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>す</td></tr>
  <tr><td class="pj-stem">tovush</td><td class="pj-end">ゴロゴロ</td><td class="pj-uz">momaqaldiroq guldurashi</td>
      <td class="pj-res">ゴロゴロ<ruby>鳴<rt>な</rt></ruby>る</td></tr>
  <tr><td class="pj-stem">tovush</td><td class="pj-end">ドンドン</td><td class="pj-uz">gurs-gurs (eshik)</td>
      <td class="pj-res">ドンドンたたく</td></tr>
  <tr><td class="pj-stem">tovush</td><td class="pj-end">パチパチ</td><td class="pj-uz">qars-qars (qarsak)</td>
      <td class="pj-res">パチパチ<ruby>拍手<rt>はくしゅ</rt></ruby>する</td></tr>
  <tr><td class="pj-stem">hayvon</td><td class="pj-end">ワンワン</td><td class="pj-uz">vov-vov (it)</td>
      <td class="pj-res">ワンワン<ruby>鳴<rt>な</rt></ruby>く</td></tr>
  <tr><td class="pj-stem">hayvon</td><td class="pj-end">ニャーニャー</td><td class="pj-uz">miyov-miyov (mushuk)</td>
      <td class="pj-res">ニャーニャー<ruby>鳴<rt>な</rt></ruby>く</td></tr>
  <tr><td class="pj-stem">tuygʻu</td><td class="pj-end">ドキドキ</td><td class="pj-uz">duk-duk (hayajon, qoʻrquv)</td>
      <td class="pj-res">ドキドキする</td></tr>
  <tr><td class="pj-stem">tuygʻu</td><td class="pj-end">わくわく</td><td class="pj-uz">quvonchli kutish</td>
      <td class="pj-res">わくわくする</td></tr>
  <tr><td class="pj-stem">tuygʻu</td><td class="pj-end">いらいら</td><td class="pj-uz">asabiylashish</td>
      <td class="pj-res">いらいらする</td></tr>
  <tr><td class="pj-stem">tana</td><td class="pj-end">ぺこぺこ</td><td class="pj-uz">qorin juda ochgan</td>
      <td class="pj-res">ぺこぺこ<b>だ</b></td></tr>
  <tr><td class="pj-stem">tana</td><td class="pj-end">くたくた</td><td class="pj-uz">holdan toygan</td>
      <td class="pj-res">くたくた<b>だ</b></td></tr>
  <tr><td class="pj-stem">tana</td><td class="pj-end">ぐっすり</td><td class="pj-uz">qattiq (uxlamoq)</td>
      <td class="pj-res">ぐっすり<ruby>寝<rt>ね</rt></ruby>る</td></tr>
  <tr><td class="pj-stem">harakat</td><td class="pj-end">ゆっくり</td><td class="pj-uz">sekin, shoshmasdan</td>
      <td class="pj-res">ゆっくり<ruby>歩<rt>ある</rt></ruby>く</td></tr>
  <tr><td class="pj-stem">harakat</td><td class="pj-end">のろのろ</td><td class="pj-uz">imillab</td>
      <td class="pj-res">のろのろ<ruby>歩<rt>ある</rt></ruby>く</td></tr>
  <tr><td class="pj-stem">harakat</td><td class="pj-end">さっと</td><td class="pj-uz">bir zumda</td>
      <td class="pj-res">さっと<ruby>立<rt>た</rt></ruby>つ</td></tr>
  <tr><td class="pj-stem">harakat</td><td class="pj-end">しっかり</td><td class="pj-uz">mustahkam, jiddiy</td>
      <td class="pj-res">しっかり<ruby>勉強<rt>べんきょう</rt></ruby>する</td></tr>
  <tr><td class="pj-stem">koʻrinish</td><td class="pj-end">きらきら</td><td class="pj-uz">yulduzdek yaltirash</td>
      <td class="pj-res">きらきら<ruby>光<rt>ひか</rt></ruby>る</td></tr>
  <tr><td class="pj-stem">koʻrinish</td><td class="pj-end">ぴかぴか</td><td class="pj-uz">yalt-yalt (yangi, toza)</td>
      <td class="pj-res">ぴかぴか<b>だ</b></td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bu jadvalni yodlashning eng oson yoʻli — juftlik.</b>
  Har bir soʻzni <em>oʻz feʼli bilan</em> yodlang:
  ザーザー<ruby>降<rt>ふ</rt></ruby>る, ドキドキする,
  ぺこぺこだ, ぐっすり<ruby>寝<rt>ね</rt></ruby>る. Yolgʻiz
  soʻzni yodlash foydasiz, chunki qaysi biri する oladi, qaysi
  biri だ oladi — hech qanday qoida bilan chiqmaydi. Bu
  yodlanadigan narsa, lekin juftlik bilan yodlansa, bir marta
  yetadi.</p>
</div>

<h3>5. Ikki ogohlantirish</h3>

<div class="pe-call pe-warn">
  <p><b>Birinchi: baʼzi soʻzlar する bilan butunlay boshqa
  maʼno beradi.</b> ぺこぺこ<b>だ</b> — «qornim ochdi», lekin
  ぺこぺこ<b>する</b> — «taʼzim qilib turmoq, xushomad
  qilmoq». Ikkinchisi umuman boshqa gap. Shuning uchun
  jadvaldagi oxirgi ustunni oʻzgartirmang.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Ikkinchi: rasmiy matnda ehtiyot boʻling.</b> Bu
  soʻzlar kundalik nutq, manga va romanning tili. Ilmiy
  maqolada yoki rasmiy hisobotda ular kam uchraydi — faqat
  ob-havo maʼlumoti va tibbiy tavsif istisno
  («<ruby>頭<rt>あたま</rt></ruby>がガンガンします» —
  shifokorga aytiladigan normal gap).</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Va bitta xushxabar: bu qatlam sizga <em>hozir</em>
  kerak boʻladi.</b> Prime Japanese ning oʻqish matnlarida,
  yaponcha kliplarda va mangada bu soʻzlar birinchi qatorda
  turadi. Yigirmatasini yodlasangiz, yapon tili
  quloqda <b>birdan tirikroq</b> eshitiladi — chunki
  odamlar aynan shunday gapiradi. Oʻzbekcha ham
  shunday: «yomgʻir yogʻdi» bilan «yomgʻir shovullab
  quydi» orasidagi farq — ikkinchisini <em>koʻrasiz</em>.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">鳴</span>
    <span class="pj-kanji__uz">jaranglamoq; (hayvon) tovush chiqarmoq</span>
    <span class="pj-kanji__on">オン: メイ</span>
    <span class="pj-kanji__kun">KUN: な(る) · な(く)</span>
    <span class="pj-kanji__note">鳴る (なる) — jiringlamoq · 鳴く (なく) — sayramoq, vovillamoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">音</span>
    <span class="pj-kanji__uz">tovush, ovoz</span>
    <span class="pj-kanji__on">オン: オン · イン</span>
    <span class="pj-kanji__kun">KUN: おと · ね</span>
    <span class="pj-kanji__note">音 (おと) — tovush · 音楽 (おんがく) — musiqa · 擬音語 (ぎおんご) — tovush taqlidi</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ザーザー<b>の</b><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ります</p>
  <p class="pe-fix__good">✓ <ruby>雨<rt>あめ</rt></ruby>が<b>ザーザー</b><ruby>降<rt>ふ</rt></ruby>ります — bu soʻzlar <b>hol</b>, sifat emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>胸<rt>むね</rt></ruby>がドキドキです</p>
  <p class="pe-fix__good">✓ <ruby>胸<rt>むね</rt></ruby>がドキドキ<b>します</b> — ドキドキ <b>する</b> oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ お<ruby>腹<rt>なか</rt></ruby>がぺこぺこ<b>します</b></p>
  <p class="pe-fix__good">✓ お<ruby>腹<rt>なか</rt></ruby>がぺこぺこ<b>です</b> — ぺこぺこする «xushomad qilmoq» degan boshqa maʼno.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>犬<rt>いぬ</rt></ruby>が<b>わんわん</b>と<ruby>鳴<rt>な</rt></ruby>きます</p>
  <p class="pe-fix__good">✓ <ruby>犬<rt>いぬ</rt></ruby>が<b>ワンワン</b>と<ruby>鳴<rt>な</rt></ruby>きます — tovush → <b>katakana</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. ザーザー va きらきら — qaysi biri <ruby>擬音語<rt>ぎおんご</rt></ruby>?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ザーザー</b> — uni quloq eshitadi, shuning uchun katakana. きらきら — yaltirash, tovushi yoʻq, shuning uchun hiragana.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Yuragim duk-duk urdi» — qaysi shakl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>胸<rt>むね</rt></ruby>がドキドキしました</b> — ドキドキ <b>する</b> oladi, です emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Qornim juda ochdi» — ぺこぺこ bilan qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>お<ruby>腹<rt>なか</rt></ruby>がぺこぺこです</b>. ぺこぺこします deyilsa, «xushomad qilyapman» boʻlib qoladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Momaqaldiroq guldurashi — qaysi soʻz va qaysi feʼl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ゴロゴロ<ruby>鳴<rt>な</rt></ruby>る</b> — tovush, demak katakana; <ruby>鳴<rt>な</rt></ruby>る «jaranglamoq».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. ゆっくり va のろのろ — ikkalasi «sekin». Farqi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ゆっくり</b> — yaxshi maʼnoda, shoshmasdan. <b>のろのろ</b> — yomon maʼnoda, imillab. Taqlid soʻzlarining koʻpi shunday <em>baho</em> olib yuradi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>擬音語<rt>ぎおんご</rt></ruby></b> — tovush taqlidi (katakana)</li>
  <li><b><ruby>擬態語<rt>ぎたいご</rt></ruby></b> — holat taqlidi (hiragana)</li>
  <li><b>ザーザー</b> — quyib yogʻmoq</li>
  <li><b>ドキドキする</b> — yurak duk-duk urmoq</li>
  <li><b>わくわくする</b> — hayajon bilan kutmoq</li>
  <li><b>ぺこぺこだ</b> — qorni juda ochgan</li>
  <li><b>くたくただ</b> — holdan toygan</li>
  <li><b>ぐっすり<ruby>寝<rt>ね</rt></ruby>る</b> — qattiq uxlamoq</li>
  <li><b><ruby>鳴<rt>な</rt></ruby>る · <ruby>鳴<rt>な</rt></ruby>く</b> — jaranglamoq · sayramoq</li>
  <li><b><ruby>光<rt>ひか</rt></ruby>る</b> — yaltiramoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Tovush → <b>katakana</b>; holat → <b>hiragana</b>.</li>
    <li>Har bir soʻz <b>oʻz feʼli bilan</b> yodlanadi: する, だ yoki toʻgʻridan-toʻgʻri feʼl.</li>
    <li>ぺこぺこ<b>だ</b> ≠ ぺこぺこ<b>する</b> — する maʼnoni butunlay oʻzgartirishi mumkin.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-78: Erkak va ayol nutqi, yoshlar tili va manga yaponchasi",
        "category": "japanese",
        "order": 78,
        "summary": (
            "Nega qahramon 俺, qahramon qiz あたし deydi, va nega "
            "darslikda faqat 私 bor. Blok E ning yopiluvchi darsi: "
            "tanib oling, lekin oʻzingiz <ruby>丁寧体<rt>ていねいたい</rt></ruby> da qoling."
        ),
        "stories": ["ふたつの ことばづかい"],
        "content": """
<h2>PJ-78: Erkak va ayol nutqi, yoshlar tili va manga yaponchasi</h2>

<p>Anime koʻrganda sezgansiz: qahramon oʻzini
<ruby>俺<rt>おれ</rt></ruby> deb ataydi, qahramon qiz
あたし deydi, qariya
<ruby>儂<rt>わし</rt></ruby> deydi — darslikda esa faqat
<ruby>私<rt>わたし</rt></ruby> bor.</p>

<p>Ularning hammasi «men» degani. Va hammasi toʻgʻri — lekin
ular <b>bir odamning tilida emas</b>. Yapon tili
gapiruvchining kimligini oʻzining grammatikasiga yozib
qoʻyadi, va buni bilmasangiz, kinoning yarmi eshitilmay
qoladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Oltita «men» ni va ularning ohangini ajratasiz</li>
    <li>ぞ・ぜ・わ・かしら kabi qoʻshimchalarni tanib olasiz</li>
    <li>Yoshlar tilining eng koʻp beshta soʻzini bilasiz</li>
    <li>Mangada koʻrasiz-u, oʻzingiz ishlatmaysiz — nimani va nega</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Eng xavfsiz yoʻl</span>
  <span class="pe-chip pe-chip--s"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v"><ruby>丁寧体<rt>ていねいたい</rt></ruby></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--opt">ism + さん</span>
</div>

<h3>1. Oltita «men»</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Kim ishlatadi</th><th>Ohangi</th></tr>
  <tr><td class="pj-stem"><ruby>私<rt>わたくし</rt></ruby></td><td class="pj-uz">hamma</td>
      <td class="pj-res">eng rasmiy — marosim, nutq, ish suhbati</td></tr>
  <tr><td class="pj-stem"><ruby>私<rt>わたし</rt></ruby></td><td class="pj-uz">hamma</td>
      <td class="pj-res"><b>neytral.</b> Erkak uchun ham, ayol uchun ham xavfsiz</td></tr>
  <tr><td class="pj-stem"><ruby>僕<rt>ぼく</rt></ruby></td><td class="pj-uz">erkak</td>
      <td class="pj-res">muloyim, kamtar — oʻquvchi, talaba, yumshoq ohang</td></tr>
  <tr><td class="pj-stem"><ruby>俺<rt>おれ</rt></ruby></td><td class="pj-uz">erkak</td>
      <td class="pj-res">dangal, yaqin — faqat doʻst va tengdosh bilan</td></tr>
  <tr><td class="pj-stem">あたし</td><td class="pj-uz">ayol</td>
      <td class="pj-res">yengil, kundalik — rasmiy joyda emas</td></tr>
  <tr><td class="pj-stem">うち</td><td class="pj-uz">yosh qizlar</td>
      <td class="pj-res">juda kundalik, Kansay ohangi bilan</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Bitta amaliy qoida butun jadvalni oʻrnini bosadi:
  <ruby>私<rt>わたし</rt></ruby> hech qachon xato emas.</b>
  Qolgan beshtasi <em>joyiga qarab</em> toʻgʻri yoki notoʻgʻri
  boʻladi, <ruby>私<rt>わたし</rt></ruby> esa hamma joyda
  ishlaydi. Shuning uchun chet ellik oʻquvchi uchun tavsiya
  bitta: <b>jadvalni tanib oling, oʻzingiz
  <ruby>私<rt>わたし</rt></ruby> da qoling</b> — hech
  boʻlmaganda Yaponiyada bir yil yashab, qulogʻingiz
  oʻrganmaguncha.</p>
</div>

<h3>2. Gap oxiridagi qoʻshimchalar</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qoʻshimcha</th><th>Ohangi</th><th>Misol</th></tr>
  <tr><td class="pj-stem">ね</td><td class="pj-uz">neytral — «-a», tasdiq izlash</td>
      <td class="pj-res"><ruby>暑<rt>あつ</rt></ruby>いですね</td></tr>
  <tr><td class="pj-stem">よ</td><td class="pj-uz">neytral — «ayta turay»</td>
      <td class="pj-res"><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りますよ</td></tr>
  <tr><td class="pj-stem">よね</td><td class="pj-uz">neytral — «shundaymi-a?»</td>
      <td class="pj-res">これでいいですよね</td></tr>
  <tr><td class="pj-stem">な · なあ</td><td class="pj-uz">erkakcha moyil — oʻzi bilan gaplashish</td>
      <td class="pj-res"><ruby>暑<rt>あつ</rt></ruby>いなあ</td></tr>
  <tr><td class="pj-stem">ぞ · ぜ</td><td class="pj-uz"><b>erkakcha, dangal</b> — mangada koʻp</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>くぞ</td></tr>
  <tr><td class="pj-stem">わ</td><td class="pj-uz"><b>ayolcha</b>, kattaroq avlod</td>
      <td class="pj-res">そう<ruby>思<rt>おも</rt></ruby>うわ</td></tr>
  <tr><td class="pj-stem">の</td><td class="pj-uz">ayolcha moyil; savol ham boʻladi</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>くの</td></tr>
  <tr><td class="pj-stem">かしら</td><td class="pj-uz"><b>ayolcha</b> — «qiziq, …mikin»</td>
      <td class="pj-res"><ruby>来<rt>く</rt></ruby>るかしら</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">イノム: おい、もう<ruby>時間<rt>じかん</rt></ruby>だ<span class="pe-hl pe-hl--neg">ぞ</span>。<ruby>行<rt>い</rt></ruby>く<span class="pe-hl pe-hl--neg">ぜ</span>。</p>
  <p class="pe-ex__uz">Inom: Hoy, vaqt boʻldi. Ketdik.</p>
  <p class="pe-ex__why">ぞ va ぜ juda dangal — <b>faqat</b> yaqin doʻstlar orasida. Oʻqituvchiga aytilsa, qoʻpollik boʻladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">ムニラ: <ruby>今日<rt>きょう</rt></ruby>は<ruby>来<rt>こ</rt></ruby>ない<span class="pe-hl pe-hl--o">の</span>？ <ruby>雨<rt>あめ</rt></ruby>だから<ruby>無理<rt>むり</rt></ruby>かな。</p>
  <p class="pe-ex__uz">Munira: Bugun kelmaysanmi? Yomgʻir boʻlgani uchun boʻlmasa kerak.</p>
  <p class="pe-ex__why">の bilan tugagan savol — kundalik va yumshoq. Ayol nutqida ayniqsa koʻp, lekin erkaklar ham ishlatadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">パリ: <ruby>来<rt>く</rt></ruby>るかしら。ラノさん、<ruby>遅<rt>おそ</rt></ruby>いわね。</p>
  <p class="pe-ex__uz">Pari: Kelarmikin. Rano kechikdi-ya.</p>
  <p class="pe-ex__why">かしら va わ — ayolcha qoʻshimchalar, lekin bugungi yosh yaponlar orasida kamdan-kam. Ularni kinoda va kitobda koʻrasiz.</p>
</div>

<h3>3. だ ning tushishi</h3>

<p>Kundalik nutqda ayol kishi <b>だ</b> ni koʻpincha tashlab
ketadi, erkak esa saqlaydi. Bu — jadvaldan ham nozikroq,
lekin quloqqa juda aniq tegadigan farq.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">Erkakcha moyil</p>
    <p>これ、きれい<b>だ</b>な。</p>
    <p><ruby>学生<rt>がくせい</rt></ruby><b>だ</b>よ。</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">Ayolcha moyil</p>
    <p>これ、きれいね。</p>
    <p><ruby>学生<rt>がくせい</rt></ruby><b>な</b>の。</p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>Oxirgi qatorga qarang: だ tushganda, の dan oldin
  <b>な</b> paydo boʻladi.</b>
  <ruby>学生<rt>がくせい</rt></ruby><b>な</b>の,
  <ruby>元気<rt>げんき</rt></ruby><b>な</b>の — bu PJ-75 dagi
  ようだ ning <b>な</b> si bilan bir xil mexanizm: ot va
  な-sifat oʻzidan keyin biror narsa kelsa, bogʻlovchi talab
  qiladi.</p>
</div>

<h3>4. «Siz» muammosi</h3>

<div class="pe-call pe-warn">
  <p><b>あなた neytral emas.</b> Darsliklarda u «siz» deb
  beriladi, lekin haqiqiy nutqda あなた sovuq, baʼzan
  yuqoridan qaraganday eshitiladi — yoki, xotin eriga
  aytsa, juda yaqin. Toʻgʻri yoʻl:
  <b>ismni ishlatish</b> — <ruby>田中<rt>たなか</rt></ruby>さん
  は<ruby>何歳<rt>なんさい</rt></ruby>ですか. Oʻzbekchada
  «siz» deyiladigan joyda yaponchada <em>ism</em>
  turadi.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Ohangi</th></tr>
  <tr><td class="pj-stem">あなた</td><td class="pj-uz">sovuq yoki juda yaqin — ehtiyot boʻling</td></tr>
  <tr><td class="pj-stem"><ruby>君<rt>きみ</rt></ruby></td><td class="pj-uz">yuqoridan pastga (ustoz → shogird), qoʻshiqlarda koʻp</td></tr>
  <tr><td class="pj-stem">お<ruby>前<rt>まえ</rt></ruby></td><td class="pj-uz">dangal yoki qoʻpol — faqat yaqin doʻst</td></tr>
  <tr><td class="pj-stem">あんた</td><td class="pj-uz">qoʻpol, gʻazabli ohang</td></tr>
  <tr><td class="pj-stem">ism + さん</td><td class="pj-res"><b>doim toʻgʻri</b></td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida grammatik jins YOʻQ — na feʼlda, na
  olmoshda — shuning uchun bu darsning yarmi butunlay
  yangi oʻq.</b> «Keldim» deganda oʻzbekcha gapiruvchining
  erkak yoki ayol ekanini bildirmaydi; yaponcha esa
  <ruby>俺<rt>おれ</rt></ruby>が<ruby>来<rt>き</rt></ruby>たぜ
  bilan あたし<ruby>来<rt>き</rt></ruby>たわ ni aniq ajratadi.
  Lekin darsning ikkinchi yarmi tanish: oʻzbekchada ham
  <em>register</em> bor — «sen» va «siz», «zoʻr» va
  «ajoyib», «qalesan» va «assalomu alaykum». Yaʼni yoshga va
  yaqinlikka qarab gapni oʻzgartirish oʻzbek oʻquvchisiga
  yangilik emas; faqat jins oʻqini qoʻshib qoʻying.</p>
</div>

<h3>5. Yoshlar tili</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Maʼnosi</th><th>Oʻrniga rasmiy</th></tr>
  <tr><td class="pj-stem">めっちゃ</td><td class="pj-uz">juda (kuchaytiruvchi)</td>
      <td class="pj-res">とても</td></tr>
  <tr><td class="pj-stem">やばい</td><td class="pj-uz">dahshat! zoʻr! (ikki maʼno ham)</td>
      <td class="pj-res"><ruby>大変<rt>たいへん</rt></ruby>です · すごいです</td></tr>
  <tr><td class="pj-stem">マジ</td><td class="pj-uz">rostdan? chin</td>
      <td class="pj-res"><ruby>本当<rt>ほんとう</rt></ruby>ですか</td></tr>
  <tr><td class="pj-stem">〜じゃん</td><td class="pj-uz">…-da, …shunday-ku</td>
      <td class="pj-res">〜ですね · 〜でしょう</td></tr>
  <tr><td class="pj-stem">うざい</td><td class="pj-uz">jonga tegadigan</td>
      <td class="pj-res">うるさいです</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Bu soʻzlarni oʻqituvchi, mijoz yoki katta yoshli
  odam bilan ishlatib boʻlmaydi.</b> Gap notoʻgʻri emas —
  <em>odobsiz</em>. Yapon tilida bu farq ancha keskin:
  «めっちゃやばいっす» deb javob bergan oʻquvchi PJ-68…72
  dagi butun keigo tizimini bir soʻz bilan buzadi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Yoshlar tili oʻzbekchada ham bor, va u ham
  shu tezlikda almashadi.</b> Bir avlod «zoʻr» deydi,
  keyingisi boshqa soʻz topadi; oʻqituvchi bilan esa
  hech kim bu soʻzlarni ishlatmaydi. Farqi shundaki,
  oʻzbekchada bu <em>odob</em> masalasi, yaponchada esa
  <b>grammatika</b> masalasi ham: めっちゃ deganingizda siz
  faqat soʻz emas, <em>butun registr</em>ni almashtirasiz —
  keyingi feʼl ham <ruby>普通体<rt>ふつうたい</rt></ruby> ga tushib ketadi. Shuning uchun
  yaponchada «bitta soʻz» qoʻshib qoʻyish boʻlmaydi: yo
  butun gap kundalik, yo butun gap rasmiy.</p>
</div>

<h3>6. Manga yaponchasi — tanib oling, ishlatmang</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Toʻliq shakli</th><th>Kim aytadi</th></tr>
  <tr><td class="pj-stem">してる · <ruby>見<rt>み</rt></ruby>てる</td>
      <td class="pj-end">している · <ruby>見<rt>み</rt></ruby>ている</td>
      <td class="pj-uz">hamma, kundalik nutqda</td></tr>
  <tr><td class="pj-stem">〜なきゃ</td><td class="pj-end">〜なければならない</td>
      <td class="pj-uz">hamma, kundalik nutqda</td></tr>
  <tr><td class="pj-stem">〜とく</td><td class="pj-end">〜ておく</td>
      <td class="pj-uz">hamma, kundalik nutqda</td></tr>
  <tr><td class="pj-stem">やめろ！ · <ruby>行<rt>い</rt></ruby>くぞ！</td>
      <td class="pj-end">やめてください · <ruby>行<rt>い</rt></ruby>きましょう</td>
      <td class="pj-uz">jangovar sahna, erkak qahramon</td></tr>
  <tr><td class="pj-stem">〜じゃ · 〜のう</td><td class="pj-end">〜だ · 〜ね</td>
      <td class="pj-uz">qariya, ustoz — «kino qariyasi» tili</td></tr>
  <tr><td class="pj-stem">〜ですわ · 〜ですの</td><td class="pj-end">〜です</td>
      <td class="pj-uz">boy xonim, «oʻrdakcha» qahramon</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Jadvalning yuqori uch qatori bilan pastki uch qatori
  orasida katta farq bor.</b> してる, 〜なきゃ, 〜とく —
  bular <em>haqiqiy</em> kundalik yaponcha, ularni doʻstlar
  bilan bemalol ishlatasiz. 〜じゃ, 〜ですわ, やめろ！ esa
  <b>badiiy til</b>: ular qahramonni tanishtirish uchun
  oʻylab topilgan va koʻchada deyarli eshitilmaydi. Ikkisini
  aralashtirmang.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Va endi rostini: bu chegara yumshayapti.</b> Ellik yil
  oldin あたし bilan <ruby>俺<rt>おれ</rt></ruby> orasidagi
  devor baland edi. Bugun koʻp yosh yapon qizi «neytral»
  gapiradi — わ ham, かしら ham ishlatmaydi (ular endi
  ancha kattaroq avlodning tili). Yosh yigitlar esa
  rasmiy joyda <ruby>私<rt>わたし</rt></ruby> ga
  osonlik bilan oʻtadi. Shuning uchun bu darsni
  <b>qoida</b> deb emas, <b>ohanglar xaritasi</b> deb
  oʻqing: eshitganda kim qanday odam ekanini tushunish
  uchun kerak, oʻzingiz gapirish uchun emas. Oʻzingiz uchun
  yoʻl bitta va u oʻzgarmaydi —
  <ruby>私<rt>わたし</rt></ruby> va <ruby>丁寧体<rt>ていねいたい</rt></ruby>.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">僕</span>
    <span class="pj-kanji__uz">men (erkak, muloyim)</span>
    <span class="pj-kanji__on">オン: ボク</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">僕 (ぼく) — men · 僕たち (ぼくたち) — biz</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">俺</span>
    <span class="pj-kanji__uz">men (erkak, dangal)</span>
    <span class="pj-kanji__on">オン: —</span>
    <span class="pj-kanji__kun">KUN: おれ</span>
    <span class="pj-kanji__note">俺 (おれ) — men · 俺たち (おれたち) — biz</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ (qiz gapiryapti) <ruby>俺<rt>おれ</rt></ruby>は<ruby>学生<rt>がくせい</rt></ruby>だぜ</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby>は<ruby>学生<rt>がくせい</rt></ruby>です — <ruby>俺<rt>おれ</rt></ruby> va ぜ erkak nutqi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ (yangi tanishga) あなたは<ruby>何歳<rt>なんさい</rt></ruby>ですか</p>
  <p class="pe-fix__good">✓ <ruby>田中<rt>たなか</rt></ruby>さんは<ruby>何歳<rt>なんさい</rt></ruby>ですか — «siz» oʻrniga <b>ism</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ (oʻqituvchiga) めっちゃやばいっす</p>
  <p class="pe-fix__good">✓ とても<ruby>大変<rt>たいへん</rt></ruby>です — yoshlar tili katta odam bilan ishlatilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ (mijozga) お<ruby>前<rt>まえ</rt></ruby>、<ruby>何<rt>なに</rt></ruby>が<ruby>欲<rt>ほ</rt></ruby>しい</p>
  <p class="pe-fix__good">✓ お<ruby>客<rt>きゃく</rt></ruby>さま、<ruby>何<rt>なに</rt></ruby>をお<ruby>探<rt>さが</rt></ruby>しですか — PJ-69 dagi <ruby>尊敬語<rt>そんけいご</rt></ruby>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Ish suhbatida oʻzingizni qanday ataysiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>私<rt>わたし</rt></ruby></b> (yoki juda rasmiy joyda <ruby>私<rt>わたくし</rt></ruby>). <ruby>僕<rt>ぼく</rt></ruby> yumshoq, lekin ish suhbatida <ruby>私<rt>わたし</rt></ruby> xavfsizroq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. ぞ va ぜ — kim, kimga aytadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Erkak kishi, <b>faqat yaqin doʻst yoki tengdoshga</b>. Oʻqituvchiga aytilsa qoʻpollik.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «<ruby>学生<rt>がくせい</rt></ruby>なの» — nega <b>な</b> paydo boʻldi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>だ</b> tushirilganda の dan oldin bogʻlovchi kerak boʻladi — PJ-75 dagi ようだ ning <b>な</b> si bilan bir xil mexanizm.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Yangi tanishgan odamga «siz» ni qanday aytasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Ism + さん</b>. あなた sovuq eshitiladi, <ruby>君<rt>きみ</rt></ruby> yuqoridan pastga.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. してる va 〜ですわ — qaysi biri haqiqiy kundalik yaponcha?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>してる</b> — している ning qisqargani, hamma ishlatadi. 〜ですわ esa <b>badiiy til</b>, koʻchada eshitilmaydi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>僕<rt>ぼく</rt></ruby></b> — men (erkak, muloyim)</li>
  <li><b><ruby>俺<rt>おれ</rt></ruby></b> — men (erkak, dangal)</li>
  <li><b>あたし</b> — men (ayol, kundalik)</li>
  <li><b>ぞ · ぜ</b> — erkakcha, dangal qoʻshimcha</li>
  <li><b>わ · かしら</b> — ayolcha qoʻshimcha</li>
  <li><b>お<ruby>前<rt>まえ</rt></ruby> · <ruby>君<rt>きみ</rt></ruby></b> — sen (ehtiyot bilan)</li>
  <li><b>めっちゃ</b> — juda (yoshlar tili)</li>
  <li><b>やばい</b> — dahshat! zoʻr!</li>
  <li><b>〜じゃん</b> — …-da, …-ku</li>
  <li><b>〜なきゃ</b> — 〜なければならない ning qisqargani</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><ruby>私<rt>わたし</rt></ruby> <b>hech qachon xato emas</b> — qolgani joyiga qarab.</li>
    <li>«Siz» oʻrniga <b>ism + さん</b>; あなた neytral emas.</li>
    <li>Bu dars <b>ohanglar xaritasi</b>: eshitib tanish uchun, oʻzi gapirish uchun emas.</li>
  </ul>
</div>
""",
    },
]
