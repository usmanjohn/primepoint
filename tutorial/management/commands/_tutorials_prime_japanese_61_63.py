# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-61, PJ-62 (Blok D yopiladi) va PJ-63 (Blok E boshi).

PJ-61 PJ-60 ning davomi: oʻsha uchta yoʻnalish, lekin endi NARSA emas,
ISH beriladi. Oʻzbekcha «-ib bermoq» shu yerda butun darsni koʻtaradi —
shuning uchun bu dars PJ-60 dan ancha oson.

PJ-62 Blok D ni yopadi: gapiruvchining ishonch darajasi.

PJ-63 bilan Blok E boshlanadi — ovoz va nuqtai nazar. Passivning
shakli bu yerda, «aziyat passivi» esa PJ-64 da.

⚠️ 〜られる II guruh feʼllarida passiv HAM, potensial HAM boʻladi
(<ruby>食<rt>た</rt></ruby>べられる). Dars buni ochiq aytadi va
ajratish yoʻlini beradi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_61_63.py --author=prime
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
        "title": "PJ-61: Berish-olish 2: 〜てあげる, 〜てくれる, 〜てもらう",
        "category": "japanese",
        "order": 61,
        "summary": (
            "Oʻsha uchta yoʻnalish, endi narsa emas — ish beriladi. "
            "Oʻzbekcha «-ib bermoq» bu darsni deyarli tayyor holda "
            "beradi, lekin bitta jiddiy odob ogohlantirishi bor."
        ),
        "stories": ["てつだって くれた"],
        "content": """
<h2>PJ-61: Berish-olish 2: 〜てあげる, 〜てくれる, 〜てもらう</h2>

<p>Oʻtgan darsda sovgʻa berdingiz. Bugun <b>ish</b> berasiz.</p>

<p>Doʻstim menga yapon tilini <b>oʻrgatib berdi</b>.<br>
Men ukamga uy vazifasini <b>tushuntirib berdim</b>.</p>

<p>Oʻzbekchada bu qurilma allaqachon bor: asosiy feʼl <b>-ib</b>
shaklida, ustiga <b>«bermoq»</b>. Yaponchada ham xuddi shunday:
<b>て</b>-shakli, ustiga PJ-60 dagi uchta feʼldan biri.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uchta qolipni て-shakli ustiga qurasiz</li>
    <li>〜てあげる nega xavfli ekanini bilib olasiz</li>
    <li>〜てくれてありがとう deb rahmat aytasiz</li>
    <li>〜てもらえますか bilan muloyim iltimos qilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ish berish</span>
  <span class="pe-chip pe-chip--s">て-shakli</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">あげる / くれる / もらう</span>
</div>

<h3>1. Uchta qolip</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Kim qiladi</th><th>Kim uchun</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem">〜てあげる</td><td class="pj-uz">MEN</td>
      <td class="pj-end">boshqa odam</td><td class="pj-res">men qilib berdim</td></tr>
  <tr><td class="pj-stem">〜てくれる</td><td class="pj-uz">boshqa odam</td>
      <td class="pj-end">MEN</td><td class="pj-res">u menga qilib berdi</td></tr>
  <tr><td class="pj-stem">〜てもらう</td><td class="pj-uz">boshqa odam</td>
      <td class="pj-end">MEN (ega — men)</td><td class="pj-res">men qildirdim / menga qilib berishdi</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>友<rt>とも</rt></ruby>だちが<ruby>私<rt>わたし</rt></ruby>に<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてくれました。</p>
  <p class="pe-ex__uz">Doʻstim menga yapon tilini oʻrgatib berdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>は<ruby>友<rt>とも</rt></ruby>だちに<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてもらいました。</p>
  <p class="pe-ex__uz">Doʻstimdan yapon tilini oʻrganib oldim.</p>
  <p class="pe-ex__why">Bir voqea, boshqa kamera — PJ-60 dagi くれる / もらう juftligining oʻzi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «-ib bermoq» — bu darsning butun kaliti.</b>
  «Yozib <em>berdi</em>», «tushuntirib <em>berdi</em>»,
  «koʻrsatib <em>berdi</em>» — oʻzbekchada ham asosiy feʼl
  <b>-ib</b> shaklida turadi va ustiga <b>«bermoq»</b>
  qoʻshiladi. Yaponchada ham aynan shunday, faqat «bermoq»
  ikkiga boʻlingan: menga kelsa <b>くれる</b>, mendan chiqsa
  <b>あげる</b>. Yaʼni qurilma tanish — faqat yoʻnalishni
  tanlash qoʻshiladi.</p>
</div>

<p>Diqqat qiling: qurilma bir xil boʻlsa ham, <b>toʻldiruvchi
qayerda turishi</b> oʻzgaradi. Oʻzbekchada «menga yozib berdi»
deganda «menga» soʻzi yoʻnalishni butunlay hal qiladi, va feʼl
qoʻzgʻalmaydi. Yaponchada esa «<ruby>私<rt>わたし</rt></ruby>に»
yozilgan boʻlsa ham, feʼl notoʻgʻri tanlangan boʻlsa gap
buziladi. Shuning uchun yaponcha gapni qurishda birinchi savol
«kim kimga?» emas, <b>«yaxshilik qaysi tomonga ketyapti?»</b>
boʻlishi kerak.</p>

<h3>2. ⚠️ 〜てあげる — ehtiyot boʻling</h3>

<p>Mana darsning eng muhim gapi, va u grammatik emas,
<b>odob</b> haqida. <b>〜てあげる ni odamning yuziga aytish
deyarli doim notoʻgʻri.</b></p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">✗ NOTOʻGʻRI ohang</p>
    <p><ruby>手伝<rt>てつだ</rt></ruby>ってあげますよ。</p>
    <p>«Sizga yordam berib <em>qoʻyaman</em>.» — men
    marhamat qilyapman degan ohang.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">✓ TOʻGʻRI</p>
    <p><ruby>手伝<rt>てつだ</rt></ruby>いましょうか。</p>
    <p>«Yordam beraymi?» — PJ-40 dagi taklif qolipi.</p></div>
</div>

<div class="pe-call pe-warn">
  <p><b>Nega bunday?</b> Chunki 〜てあげる ishni
  <em>sovgʻa</em> qilib koʻrsatadi — yaʼni «men senga yaxshilik
  qildim» deb turadi. Yapon odobi esa yaxshilikni <b>oʻzi
  aytmaslikni</b> talab qiladi. Shuning uchun bu qolip koʻproq
  <em>uchinchi odam haqida</em> gapirganda ishlatiladi:
  «men ukamga qilib berdim» — bu yerda ukam eshitmayapti.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham shu ohang bor.</b> «Men senga qilib
  <em>beray</em>» degan gap sharoitga qarab samimiy ham,
  ustunlik qilayotgandek ham eshitilishi mumkin — siz buni
  his qilasiz. Yaponchada esa bu his <b>deyarli qoida</b>:
  ustozga, mehmonga yoki kattaroq odamga hech qachon
  〜てあげます deyilmaydi. Tanish farq, faqat ancha
  qatʼiyroq.</p>
</div>

<p>Buni boshqacha aytsak: 〜てあげる gapning markaziga
<em>sizni</em> qoʻyadi — «men qildim». Yapon tili esa suhbatda
gapiruvchini orqada turishini afzal koʻradi. Shuning uchun
yaxshilik qilganingizda uni umuman tilga olmaslik eng
xavfsiz yoʻl: shunchaki
<ruby>手伝<rt>てつだ</rt></ruby>います deysiz, va tinglovchi
buni oʻzi qadrlaydi. 〜てあげる esa hikoya qilayotganda,
uchinchi odam haqida, oʻz oʻrnini topadi.</p>

<h3>3. 〜てくれてありがとう — eng koʻp ishlatiladigan rahmat</h3>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>手伝<rt>てつだ</rt></ruby>ってくれてありがとう。</p>
  <p class="pe-ex__uz">Yordam berganingiz uchun rahmat.</p>
  <p class="pe-ex__why">て-shakli + くれて + ありがとう. Muloyimroq shakli: 〜てくれてありがとうございます.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Quruq «ありがとう» dan farqi bor.</b> Yaponchada
  rahmat aytganda <em>nima uchun</em> ekanini feʼl bilan
  koʻrsatish odat: <ruby>来<rt>き</rt></ruby>てくれてありがとう
  («kelganingiz uchun»),
  <ruby>教<rt>おし</rt></ruby>えてくれてありがとう
  («oʻrgatganingiz uchun»). Bu gapni yodlab qoʻysangiz,
  yaponcha suhbatda darrov tabiiy eshitila boshlaysiz.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ham rahmatni ishga bogʻlaydi.</b> «Kelganingiz
  uchun rahmat», «yordam berganingiz uchun rahmat» — quruq
  «rahmat» dan koʻra ancha issiqroq eshitiladi, shundaymi?
  Yaponchada bu tanlov emas, <em>odat</em>: yaponlar rahmat
  aytganda deyarli doim nima uchun ekanini qoʻshadi. Farqi
  faqat qurilishda — oʻzbekcha «-ganingiz uchun» qoʻshadi,
  yaponcha esa <b>てくれて</b>, yaʼni oʻsha «qilib berdingiz»
  degan feʼlning oʻzini.</p>
</div>

<h3>4. 〜てもらえますか — muloyim iltimos</h3>

<p>Mana bu qolip amalda eng kerakli. <b>もらう</b> ning
potensial shakli <b>もらえる</b> (PJ-42), va uni savolga
aylantirsangiz — juda muloyim iltimos chiqadi.</p>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name">〜てください</span>
    <span class="pj-level__ja"><ruby>教<rt>おし</rt></ruby>えてください</span>
    <span class="pj-level__who">oddiy iltimos (PJ-32)</span>
  </div>
  <div class="pj-level__row pj-level__row--2">
    <span class="pj-level__name">〜てもらえますか</span>
    <span class="pj-level__ja"><ruby>教<rt>おし</rt></ruby>えてもらえますか</span>
    <span class="pj-level__who">muloyimroq — «qilib bera olasizmi?»</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name">〜ていただけますか</span>
    <span class="pj-level__ja"><ruby>教<rt>おし</rt></ruby>えていただけますか</span>
    <span class="pj-level__who">eng muloyim — ustoz, mijoz, notanish odam</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>Qoida oddiy: gap uzaygan sari muloyimlashadi.</b>
  Bu yapon tilining umumiy odati — siz buni PJ-54 dagi
  けど → けれども → が zinapoyasida ham koʻrgansiz. Iltimosda
  ham xuddi shunday: qanchalik aylanib oʻtsangiz, shunchalik
  muloyim.</p>
</div>

<p>Bu zinapoya nega ishlaydi? Chunki uzun shakl iltimosni
<b>bilvosita</b> qiladi. «Oʻrgating» — buyruq. «Oʻrgatib
bera olasizmi?» — endi siz odamdan <em>imkoniyat</em>
haqida soʻrayapsiz, va u «yoʻq» deyishi osonlashadi. Yapon
odobining butun mantiqi shu: suhbatdoshga
<em>rad etish yoʻlini qoldirish</em>. Oʻzbekchada ham
«bera olasizmi?» «bering» dan muloyimroq — faqat yaponchada
bu farq ancha kattaroq va ancha koʻproq ishlatiladi.</p>

<h3>5. Qoʻshimchalar</h3>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>友<rt>とも</rt></ruby>だち</span>
  <span class="pj-joshi__p">が<small>KIM</small></span>
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">に<small>MENGA</small></span>
  <span class="pj-joshi__n"><ruby>日本語<rt>にほんご</rt></ruby></span>
  <span class="pj-joshi__p">を</span>
  <span class="pj-joshi__v"><ruby>教<rt>おし</rt></ruby>えてくれました</span>
  <span class="pj-joshi__uz">Doʻstim menga yapon tilini oʻrgatib berdi.</span>
</div>

<div class="pe-call pe-warn">
  <p><b>Baʼzi feʼllar odamni を bilan oladi.</b>
  <ruby>手伝<rt>てつだ</rt></ruby>う («yordam bermoq») —
  <ruby>弟<rt>おとうと</rt></ruby><b>を</b><ruby>手伝<rt>てつだ</rt></ruby>ってあげました.
  Sababi: bu feʼlning toʻldiruvchisi <em>odam</em>, narsa emas.
  Xuddi shunday <ruby>誘<rt>さそ</rt></ruby>う («taklif qilmoq»),
  <ruby>送<rt>おく</rt></ruby>る («kuzatib qoʻymoq»). Qolgan
  koʻpchilik feʼllar odamni <b>に</b> bilan oladi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">教</span>
    <span class="pj-kanji__uz">oʻrgatmoq</span>
    <span class="pj-kanji__on">オン: キョウ</span>
    <span class="pj-kanji__kun">KUN: おし(える), おそ(わる)</span>
    <span class="pj-kanji__note">教える (おしえる) — oʻrgatmoq · 教室 (きょうしつ) — sinfxona</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">伝</span>
    <span class="pj-kanji__uz">yetkazmoq</span>
    <span class="pj-kanji__on">オン: デン</span>
    <span class="pj-kanji__kun">KUN: つた(える), てつだ(う)</span>
    <span class="pj-kanji__note">手伝う (てつだう) — yordam bermoq · 伝える (つたえる) — yetkazmoq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>先生<rt>せんせい</rt></ruby>に<ruby>手伝<rt>てつだ</rt></ruby>ってあげます</p>
  <p class="pe-fix__good">✓ <ruby>手伝<rt>てつだ</rt></ruby>いましょうか — ustozga hech qachon 〜てあげます deyilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>友<rt>とも</rt></ruby>だちが<ruby>私<rt>わたし</rt></ruby>に<ruby>教<rt>おし</rt></ruby>えてあげました</p>
  <p class="pe-fix__good">✓ …<ruby>教<rt>おし</rt></ruby>えて<b>くれました</b> — menga kelayotgan yaxshilik doim くれる.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>読<rt>よ</rt></ruby>むてくれました</p>
  <p class="pe-fix__good">✓ <ruby>読<rt>よ</rt></ruby><b>んで</b>くれました — uchala qolip ham て-shakliga qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>弟<rt>おとうと</rt></ruby>に<ruby>手伝<rt>てつだ</rt></ruby>ってあげました</p>
  <p class="pe-fix__good">✓ <ruby>弟<rt>おとうと</rt></ruby><b>を</b><ruby>手伝<rt>てつだ</rt></ruby>ってあげました — <ruby>手伝<rt>てつだ</rt></ruby>う odamni を bilan oladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Doʻstim menga kitob oʻqib berdi» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>友<rt>とも</rt></ruby>だちが<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んでくれました</b> — menga kelayotgan yaxshilik.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Ustozga yordam taklif qilyapsiz. Nima deysiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>手伝<rt>てつだ</rt></ruby>いましょうか</b> — 〜てあげます emas, chunki u marhamat qilayotgandek eshitiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Kelganingiz uchun rahmat» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>来<rt>き</rt></ruby>てくれてありがとう</b> (muloyimroq: …ありがとうございます).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Ustozdan muloyim iltimos qilyapsiz: «oʻrgatib bera olasizmi?»</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>教<rt>おし</rt></ruby>えていただけますか</b> — eng muloyim shakl. <ruby>教<rt>おし</rt></ruby>えてもらえますか ham boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega «<ruby>先生<rt>せんせい</rt></ruby>に<ruby>教<rt>おし</rt></ruby>えてあげました» notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki 〜てあげる yaxshilikni <b>sovgʻa qilib koʻrsatadi</b>. Ustozga nisbatan bu odobsiz eshitiladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜てあげる</b> — qilib bermoq (mendan chiqadi)</li>
  <li><b>〜てくれる</b> — qilib bermoq (menga keladi)</li>
  <li><b>〜てもらう</b> — qildirmoq, qilib berishlarini olmoq</li>
  <li><b>〜てくれてありがとう</b> — …ganingiz uchun rahmat</li>
  <li><b>〜てもらえますか</b> — …qilib bera olasizmi?</li>
  <li><b>〜ていただけますか</b> — eng muloyim iltimos</li>
  <li><b><ruby>手伝<rt>てつだ</rt></ruby>う</b> — yordam bermoq (I guruh, odamni を bilan)</li>
  <li><b><ruby>教<rt>おし</rt></ruby>える</b> — oʻrgatmoq (II guruh)</li>
  <li><b><ruby>貸<rt>か</rt></ruby>す</b> — qarz bermoq (I guruh)</li>
  <li><b><ruby>直<rt>なお</rt></ruby>す</b> — tuzatmoq (I guruh)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Oʻzbekcha <b>«-ib bermoq»</b> — qurilma allaqachon sizda bor.</li>
    <li><b>〜てあげる ni yuzga aytmang</b> — oʻrniga 〜ましょうか.</li>
    <li>Muloyim iltimos: <b>〜てもらえますか / 〜ていただけますか</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-62: Taxmin: 〜でしょう, 〜かもしれません, 〜はずです",
        "category": "japanese",
        "order": 62,
        "summary": (
            "Uchta ishonch darajasi: «boʻlsa kerak», «boʻlishi mumkin» "
            "va «boʻlishi kerak». Oʻzbekchada ham uchtasi bor, shuning "
            "uchun tanlash emas, yaponcha kiyimini kiydirish qoladi."
        ),
        "stories": ["かさは どこでしょう"],
        "content": """
<h2>PJ-62: Taxmin: 〜でしょう, 〜かもしれません, 〜はずです</h2>

<p>Ertaga yomgʻir yogʻadimi? Siz bilmaysiz — lekin
<em>qanchalik</em> bilmasligingiz ham muhim. Oʻzbekchada siz
buni uch xil aytasiz:</p>

<p>Ertaga yomgʻir yogʻ<b>sa kerak</b>. — ancha ishonchliman.<br>
Ertaga yomgʻir yogʻ<b>ishi mumkin</b>. — ehtimol, ehtimol emas.<br>
Ertaga yomgʻir yogʻ<b>ishi kerak</b>. — mantiqan shunday chiqadi.</p>

<p>Yapon tilida ham aynan shu uchtasi bor, va ular bir-biriga
almashmaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uchta qolipni ishonch darajasi boʻyicha joylashtirasiz</li>
    <li>Ot va な-sifat bilan qanday ulanishini bilib olasiz</li>
    <li>はず nega な / の talab qilishini tushunasiz</li>
    <li>でしょう？ degan savol ohangini taniysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ishonch darajasi</span>
  <span class="pe-chip pe-chip--neg">かもしれません ~50%</span>
  <span class="pe-op">&lt;</span>
  <span class="pe-chip pe-chip--adv">でしょう ~80%</span>
  <span class="pe-op">&lt;</span>
  <span class="pe-chip pe-chip--v">はずです ~90%</span>
</div>

<p>Bir narsani boshda aytib qoʻyish kerak: bu uchtasi
<b>faktni almashtirmaydi</b>. Agar bilsangiz, shunchaki
ayting — <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>って
います. Taxmin qoliplari faqat <em>bilmagan</em> paytda
ishlatiladi, va ularning vazifasi bilmasligingizni
<b>aniq oʻlchab koʻrsatish</b>. Yaponchada bu juda muhim,
chunki noaniq narsani aniqdek aytish qoʻpol hisoblanadi.</p>

<h3>1. かもしれません — «boʻlishi mumkin»</h3>

<p>Eng past daraja. Gapiruvchi <b>bilmaydi</b> va shuni ochiq
aytadi. Boʻlishi ham, boʻlmasligi ham mumkin.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>明日<rt>あした</rt></ruby><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>るかもしれません。</p>
  <p class="pe-ex__uz">Ertaga yomgʻir yogʻishi mumkin.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Ogʻzaki shakli — かも.</b> Doʻstlar suhbatida
  «<ruby>雨<rt>あめ</rt></ruby>かも» deb qisqartiriladi.
  Yozma ishda esa toʻliq <b>かもしれません</b>.</p>
</div>

<p>Diqqat qiling: かもしれません <em>inkor</em> emas. U
«boʻlmaydi» degani emas, «bilmayman» degani. Shuning uchun
undan keyin koʻpincha ikkinchi gap keladi:
«<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>るかも
しれません。かさを<ruby>持<rt>も</rt></ruby>っていきます» —
«yogʻishi mumkin, shuning uchun soyabon olaman». Bu qolip
ehtiyotkorlik qaroriga asos boʻlib xizmat qiladi.</p>

<h3>2. でしょう — «boʻlsa kerak»</h3>

<p>Oʻrtacha-yuqori daraja. Gapiruvchi ishonadi, lekin kafolat
bermaydi. Ob-havo maʼlumotining tili shu.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>明日<rt>あした</rt></ruby>は<ruby>晴<rt>は</rt></ruby>れるでしょう。</p>
  <p class="pe-ex__uz">Ertaga ochiq boʻlsa kerak.</p>
  <p class="pe-ex__why">Yaponcha ob-havo maʼlumoti deyarli har gapni でしょう bilan tugatadi.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>でしょう ikkinchi ishda ham yuradi: tasdiq soʻrash.</b>
  Ohangni koʻtarsangiz, u «shundaymi?» degan maʼnoni beradi:
  「<ruby>寒<rt>さむ</rt></ruby>いでしょう？」 — «Sovuq-a?»
  Bu yerda taxmin yoʻq — gapiruvchi javobni biladi va
  suhbatdoshdan roziligini soʻrayapti.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham uch daraja bor — va siz ularni
  aralashtirmaysiz.</b> «Yomgʻir yogʻ<em>ishi mumkin</em>»,
  «yomgʻir yogʻ<em>sa kerak</em>», «yomgʻir yogʻ<em>ishi
  kerak</em>» — uchtasi uch xil ishonch. Demak bu darsda
  yangi <em>tushuncha</em> yoʻq; faqat uchta oʻzbekcha
  qolipga uchta yaponcha kiyim topish kerak. Shuning uchun
  darsni yodlashdan emas, <b>oʻzbekcha gapni aytib, keyin
  uni kiyintirishdan</b> boshlang.</p>
</div>

<h3>3. はずです — «boʻlishi kerak»</h3>

<p>Eng yuqori daraja, lekin u <b>fakt emas</b>: bu
<em>mantiqiy kutish</em>. Sizda dalil bor va shundan xulosa
chiqaryapsiz.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">ラノさんは<ruby>今<rt>いま</rt></ruby><ruby>教室<rt>きょうしつ</rt></ruby>にいるはずです。</p>
  <p class="pe-ex__uz">Rano hozir sinfda boʻlishi kerak.</p>
  <p class="pe-ex__why">Nega? Chunki dars boshlandi. Dalil bor, shuning uchun はず.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>はず «majburiyat» degani EMAS.</b> Oʻzbekcha
  «boʻlishi kerak» ikki xil ishlaydi: «u sinfda boʻlishi
  kerak» (taxmin) va «sen darsga kelishing kerak»
  (majburiyat). Yaponchada bular butunlay boshqa qoliplar:
  taxmin — <b>はず</b>, majburiyat —
  <b>なければなりません</b> (PJ-33). Ularni chalkashtirmang.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>はずでした — kutish puchga chiqqanda.</b>
  「<ruby>来<rt>く</rt></ruby>るはずでした」 — «kelishi kerak
  edi» (lekin kelmadi). Yaponchada bu juda koʻp ishlatiladi
  va oʻzbekchada ham shunday: «kelishi kerak edi-ku».</p>
</div>

<div class="pe-call pe-uz">
  <p><b>でしょう？ — oʻzbekcha «-a?» va «-ku».</b> «Sovuq-<em>a</em>?»,
  «Charchading-<em>ku</em>» — bu gaplarda ham siz javobni
  bilasiz va shunchaki rozilik soʻrayapsiz. Yaponcha
  <b>でしょう？</b> aynan shu ish qiladi, va u kundalik
  suhbatda taxmin maʼnosidan <em>koʻproq</em> uchraydi.
  Farqni ohang ajratadi: pasaysa — taxmin, koʻtarilsa —
  savol.</p>
</div>

<h3>4. Yasalishi — jadval</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>かもしれません</th><th>でしょう</th><th>はずです</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-uz"><ruby>降<rt>ふ</rt></ruby>るかも…</td>
      <td class="pj-uz"><ruby>降<rt>ふ</rt></ruby>るでしょう</td><td class="pj-res"><ruby>降<rt>ふ</rt></ruby>るはずです</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-uz"><ruby>寒<rt>さむ</rt></ruby>いかも…</td>
      <td class="pj-uz"><ruby>寒<rt>さむ</rt></ruby>いでしょう</td><td class="pj-res"><ruby>寒<rt>さむ</rt></ruby>いはずです</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-uz"><ruby>静<rt>しず</rt></ruby>かかも…</td>
      <td class="pj-uz"><ruby>静<rt>しず</rt></ruby>かでしょう</td><td class="pj-res"><ruby>静<rt>しず</rt></ruby>か<b>な</b>はずです</td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-uz"><ruby>学生<rt>がくせい</rt></ruby>かも…</td>
      <td class="pj-uz"><ruby>学生<rt>がくせい</rt></ruby>でしょう</td><td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby><b>の</b>はずです</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Ikkita qoida, ikkalasi ham tanish.</b>
  <b>かもしれません</b> va <b>でしょう</b> oldida ot va な-sifat
  <em>quruq</em> turadi — xuddi PJ-52 dagi なら kabi.
  <b>はず</b> esa <em>ot</em> (u «kutish» degan maʼnodagi
  soʻz), shuning uchun undan oldin PJ-48 ning qoidasi
  ishlaydi: な-sifat <b>な</b>, ot <b>の</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu — kursda toʻrtinchi marta.</b> Siz endi shu naqshni
  taniysiz: agar qolipning markazida <b>ot</b> tursa, undan
  oldin な / の keladi. とき (PJ-49), ので (PJ-53),
  こと (PJ-57) va bugun はず — toʻrttasi ham ot. Yaʼni bu yangi
  qoida emas, bir qoidaning toʻrtinchi koʻrinishi. Oʻzbekchada
  ham «kelishi <em>kerak</em>» dagi «kerak» — soʻz, qoʻshimcha
  emas; shuning uchun undan oldin feʼl toʻliq shaklda
  turadi.</p>
</div>

<p>Yana bir amaliy joyi bor: bu uchtasi <b>gapning eng
oxirida</b> turadi va undan keyin hech nima kelmaydi. Yaʼni
siz gapni odatdagidek quryapsiz, keyin uning ustiga
<em>ishonch qopqogʻini</em> qoʻyasiz. Shuning uchun ularni
oʻrganish oson: gapni oʻzgartirish kerak emas, faqat
oxiriga bir narsa qoʻshiladi. Yagona eʼtibor talab
qiladigan joy — はず oldidagi な / の.</p>

<h3>5. Uchtasini yonma-yon qoʻyish</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Gap</th><th>Nimaga asoslangan</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem"><ruby>来<rt>く</rt></ruby>るかもしれません</td>
      <td class="pj-uz">hech nimaga — shunchaki ehtimol</td>
      <td class="pj-res">kelishi mumkin</td></tr>
  <tr><td class="pj-stem"><ruby>来<rt>く</rt></ruby>るでしょう</td>
      <td class="pj-uz">tajriba, umumiy bilim</td>
      <td class="pj-res">kelsa kerak</td></tr>
  <tr><td class="pj-stem"><ruby>来<rt>く</rt></ruby>るはずです</td>
      <td class="pj-uz">aniq dalil — vaʼda bergan, chipta olgan</td>
      <td class="pj-res">kelishi kerak</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Tanlashning oson yoʻli: «nega shunday deb
  oʻylaysiz?»</b> Javobingiz yoʻq boʻlsa — かもしれません.
  «Odatda shunday» boʻlsa — でしょう. Aniq bir dalil
  aytib bera olsangiz — <b>はずです</b>.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">晴</span>
    <span class="pj-kanji__uz">ochiq havo</span>
    <span class="pj-kanji__on">オン: セイ</span>
    <span class="pj-kanji__kun">KUN: は(れる)</span>
    <span class="pj-kanji__note">晴れる (はれる) — ochilmoq · 晴れ (はれ) — quyoshli havo</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">曇</span>
    <span class="pj-kanji__uz">bulutli</span>
    <span class="pj-kanji__on">オン: ドン</span>
    <span class="pj-kanji__kun">KUN: くも(る)</span>
    <span class="pj-kanji__note">曇る (くもる) — bulutlanmoq · 曇り (くもり) — bulutli havo</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>だでしょう</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby>でしょう — でしょう oldida ot quruq turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>はずです</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>の</b>はずです — はず ot, demak ot oldida の.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>静<rt>しず</rt></ruby>かだはずです</p>
  <p class="pe-fix__good">✓ <ruby>静<rt>しず</rt></ruby>か<b>な</b>はずです — な-sifat otdan oldin な kiyadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>くはずです = «borishim kerak» (majburiyat)</p>
  <p class="pe-fix__good">✓ はず = <b>taxmin</b>. Majburiyat uchun — <ruby>行<rt>い</rt></ruby>かなければなりません (PJ-33).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Uchtasini ishonch darajasi boʻyicha tartiblang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>かもしれません → でしょう → はずです</b> — pastdan yuqoriga.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «<ruby>静<rt>しず</rt></ruby>か» ni はずです bilan ulang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>静<rt>しず</rt></ruby>かなはずです</b> — はず ot, demak な.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «<ruby>学生<rt>がくせい</rt></ruby>» ni でしょう bilan ulang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>学生<rt>がくせい</rt></ruby>でしょう</b> — でしょう oldida だ tushadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Rano vaʼda bergan edi. U keladi deb qanday aytasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>来<rt>く</rt></ruby>るはずです</b> — aniq dalil bor (vaʼda), demak はず.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «<ruby>寒<rt>さむ</rt></ruby>いでしょう？» — bu taxminmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yoʻq. Ohang koʻtarilgan, demak bu <b>tasdiq soʻrash</b>: «Sovuq-a?» Gapiruvchi javobni biladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜かもしれません</b> — …boʻlishi mumkin</li>
  <li><b>〜でしょう</b> — …boʻlsa kerak</li>
  <li><b>〜はずです</b> — …boʻlishi kerak (mantiqan)</li>
  <li><b>〜はずでした</b> — …boʻlishi kerak edi (lekin boʻlmadi)</li>
  <li><b>だろう</b> — でしょう ning oddiy shakli</li>
  <li><b><ruby>晴<rt>は</rt></ruby>れる</b> — ochilmoq (II guruh)</li>
  <li><b><ruby>曇<rt>くも</rt></ruby>る</b> — bulutlanmoq (I guruh)</li>
  <li><b><ruby>天気予報<rt>てんきよほう</rt></ruby></b> — ob-havo maʼlumoti</li>
  <li><b><ruby>多分<rt>たぶん</rt></ruby></b> — ehtimol</li>
  <li><b>きっと</b> — albatta, shubhasiz</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>かもしれません &lt; でしょう &lt; はずです</b> — past, oʻrta, yuqori.</li>
    <li>はず — <b>ot</b>, demak undan oldin な / の.</li>
    <li>はず = <b>taxmin</b>, majburiyat emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-63: Passiv (受身) 1: shakl va oddiy ishlatilishi",
        "category": "japanese",
        "order": 63,
        "summary": (
            "Blok E boshlanadi. Passiv oʻzbekchada ham bor, lekin "
            "yaponchada u ancha koʻp ishlatiladi — va bitta shakl "
            "potensial bilan ustma-ust tushadi."
        ),
        "stories": ["まちの ニュース"],
        "content": """
<h2>PJ-63: Passiv (<ruby>受身<rt>うけみ</rt></ruby>) 1: shakl va oddiy ishlatilishi</h2>

<p>Shu paytgacha gaplaringizda <b>kim qilgani</b> muhim edi.
Bugundan boshlab gapni teskari tomondan qurishni oʻrganasiz:
ish <em>kimga qilingani</em> muhim boʻlgan gapni.</p>

<p>Oʻzbekchada bu qurilma bor:
«kitob <b>oʻqildi</b>», «xat <b>yozildi</b>», «men
<b>maqtaldim</b>». Yaponchada ham bor —
<b><ruby>受身形<rt>うけみけい</rt></ruby></b> — lekin u
oʻzbekchadan ikki narsada farq qiladi, va ikkalasini ham
bugun koʻrasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uch guruh feʼlidan passiv shaklini yasaysiz</li>
    <li>Passiv gapdagi qoʻshimchalarni joylashtirasiz</li>
    <li>Nega yaponchada passiv koʻproq ishlatilishini bilib olasiz</li>
    <li>〜られる ning ikki maʼnosini ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Passiv</span>
  <span class="pe-chip pe-chip--s">ない-oʻzak</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">れる / られる</span>
</div>

<h3>1. Yasalishi</h3>

<p>Passiv <b>ない-shaklining oʻzagidan</b> yasaladi — yaʼni
PJ-34 da oʻrgangan shakldan ない ni olib tashlaysiz va
oʻrniga <b>れる</b> qoʻyasiz.</p>

<div class="pj-group">
  <div class="pj-group__c">
    <p class="pj-group__h">I — <ruby>五段<rt>ごだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>読<rt>よ</rt></ruby>む → <ruby>読<rt>よ</rt></ruby>まれる</p>
    <p>Oxirgi bogʻin <b>あ-qatorga</b> tushadi va れる qoʻshiladi.</p>
  </div>
  <div class="pj-group__c pj-group__c--2">
    <p class="pj-group__h">II — <ruby>一段<rt>いちだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>食<rt>た</rt></ruby>べる → <ruby>食<rt>た</rt></ruby>べられる</p>
    <p>る tushadi, <b>られる</b> qoʻyiladi.</p>
  </div>
  <div class="pj-group__c pj-group__c--3">
    <p class="pj-group__h">III — <ruby>不規則<rt>ふきそく</rt></ruby></p>
    <p class="pj-group__ex">する → される · <ruby>来<rt>く</rt></ruby>る → <ruby>来<rt>こ</rt></ruby>られる</p>
    <p>Faqat ikkita, yodlab qoʻying.</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Guruh</th><th>ない-shakli</th><th>Passiv</th></tr>
  <tr><td class="pj-stem"><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-uz">I</td>
      <td class="pj-end"><ruby>読<rt>よ</rt></ruby>ま<s>ない</s></td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>まれる</td></tr>
  <tr><td class="pj-stem"><ruby>書<rt>か</rt></ruby>く</td><td class="pj-uz">I</td>
      <td class="pj-end"><ruby>書<rt>か</rt></ruby>か<s>ない</s></td><td class="pj-res"><ruby>書<rt>か</rt></ruby>かれる</td></tr>
  <tr><td class="pj-stem"><ruby>言<rt>い</rt></ruby>う</td><td class="pj-uz">I</td>
      <td class="pj-end"><ruby>言<rt>い</rt></ruby>わ<s>ない</s></td><td class="pj-res"><ruby>言<rt>い</rt></ruby>われる</td></tr>
  <tr><td class="pj-stem"><ruby>作<rt>つく</rt></ruby>る</td><td class="pj-uz">I</td>
      <td class="pj-end"><ruby>作<rt>つく</rt></ruby>ら<s>ない</s></td><td class="pj-res"><ruby>作<rt>つく</rt></ruby>られる</td></tr>
  <tr><td class="pj-stem"><ruby>褒<rt>ほ</rt></ruby>める</td><td class="pj-uz">II</td>
      <td class="pj-end"><ruby>褒<rt>ほ</rt></ruby>め<s>ない</s></td><td class="pj-res"><ruby>褒<rt>ほ</rt></ruby>められる</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>う bilan tugaydigan feʼllarda わ chiqadi.</b>
  <ruby>言<rt>い</rt></ruby>う → <ruby>言<rt>い</rt></ruby><b>わ</b>れる,
  <ruby>使<rt>つか</rt></ruby>う → <ruby>使<rt>つか</rt></ruby><b>わ</b>れる.
  Bu yangi qoida emas — siz uni PJ-34 dagi ない-shaklida
  koʻrgansiz: <ruby>言<rt>い</rt></ruby>わない. Passiv oʻsha
  oʻzakdan yasalgani uchun わ shu yerda ham qoladi.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Passiv feʼl II guruh feʼliga aylanadi.</b>
  <ruby>読<rt>よ</rt></ruby>まれ<b>る</b> endi
  <ruby>食<rt>た</rt></ruby>べる kabi tuslanadi:
  <ruby>読<rt>よ</rt></ruby>まれます,
  <ruby>読<rt>よ</rt></ruby>まれた,
  <ruby>読<rt>よ</rt></ruby>まれない. Shuning uchun passivni
  yasab boʻlgach, qolgan hamma narsa tanish.</p>
</div>

<p>Diqqat qiling: passiv oʻzagi <b>ない-shakli bilan bir
xil</b>, va bu tasodif emas. Yapon feʼlining beshta oʻzagi
bor, va ular boshqa-boshqa qoʻshimchalarni koʻtaradi. Siz
ulardan ikkitasini allaqachon bilasiz: ます oldidagi
い-oʻzak (PJ-20) va ない oldidagi あ-oʻzak (PJ-34). Bugun
oʻsha あ-oʻzak ikkinchi ishga tushdi. Keyingi ikki dars —
kauzativ (PJ-65) va kauzativ-passiv (PJ-66) — ham
<em>oʻsha</em> oʻzakdan yasaladi, shuning uchun uni hozir
mustahkam oʻzlashtirib olish keyingi uch darsni ham
yengillashtiradi.</p>

<h3>2. Qoʻshimchalar: に — «tomonidan»</h3>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">は<small>KIMGA</small></span>
  <span class="pj-joshi__n"><ruby>先生<rt>せんせい</rt></ruby></span>
  <span class="pj-joshi__p">に<small>TOMONIDAN</small></span>
  <span class="pj-joshi__v"><ruby>褒<rt>ほ</rt></ruby>められました</span>
  <span class="pj-joshi__uz">Men oʻqituvchi tomonidan maqtaldim.</span>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oddiy gap</th><th>Passiv gap</th></tr>
  <tr><td class="pj-stem"><ruby>先生<rt>せんせい</rt></ruby><b>が</b><ruby>私<rt>わたし</rt></ruby><b>を</b><ruby>褒<rt>ほ</rt></ruby>めました</td>
      <td class="pj-res"><ruby>私<rt>わたし</rt></ruby><b>は</b><ruby>先生<rt>せんせい</rt></ruby><b>に</b><ruby>褒<rt>ほ</rt></ruby>められました</td></tr>
  <tr><td class="pj-stem"><ruby>母<rt>はは</rt></ruby><b>が</b>ケーキ<b>を</b><ruby>作<rt>つく</rt></ruby>りました</td>
      <td class="pj-res">ケーキ<b>は</b><ruby>母<rt>はは</rt></ruby><b>に</b><ruby>作<rt>つく</rt></ruby>られました</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada passiv bor, lekin u kim qilganini
  yashiradi.</b> «Kitob oʻqildi» — kim oʻqigani aytilmaydi,
  va «Alisher tomonidan oʻqildi» degan gap kitobiy, sunʼiy
  eshitiladi. Yaponchada esa aksincha: <b>に</b> bilan kim
  qilgani doim aytilishi mumkin va bu butunlay tabiiy.
  Shuning uchun yaponcha passivni oʻzbekcha passiv bilan emas,
  koʻpincha <em>oddiy gap</em> bilan tarjima qilish
  toʻgʻriroq: «oʻqituvchi meni maqtadi».</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>歌<rt>うた</rt></ruby>は<ruby>子<rt>こ</rt></ruby>どもたちに<ruby>選<rt>えら</rt></ruby>ばれました。</p>
  <p class="pe-ex__uz">Bu qoʻshiqni bolalar tanlashdi.</p>
  <p class="pe-ex__why">Oʻzbekchaga oddiy gap bilan tarjima qilindi — «bolalar tomonidan tanlandi» sunʼiy eshitiladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha passiv qiluvchini yashiradi, yaponchasi
  koʻrsatadi.</b> «Kitob oʻqildi» — kim? Aytilmaydi.
  «Alisher tomonidan oʻqildi» — grammatik jihatdan mumkin,
  lekin hech kim bunday gapirmaydi. Yaponchada esa
  <b>に</b> bilan qiluvchini aytish shunchalik oddiyki, uni
  aytmaslik baʼzan gʻalati tuyuladi. Shuning uchun yaponcha
  passiv gapni oʻzbekchaga <em>passiv bilan</em> tarjima
  qilishga urinmang — koʻpincha oddiy gap toʻgʻriroq
  chiqadi.</p>
</div>

<h3>3. Nega yaponchada passiv koʻp ishlatiladi</h3>

<p>Yapon tili gapning <b>mavzusini oʻzgartirmaslikni</b>
yaxshi koʻradi. Agar hikoya siz haqingizda ketayotgan boʻlsa,
har bir gap sizdan boshlanishi kerak — hatto ishni boshqa
odam qilgan boʻlsa ham. Passiv shuni imkon beradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>は<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>って、<ruby>先生<rt>せんせい</rt></ruby>に<ruby>名前<rt>なまえ</rt></ruby>を<ruby>呼<rt>よ</rt></ruby>ばれました。</p>
  <p class="pe-ex__uz">Sinfga kirdim va oʻqituvchi ismimni chaqirdi.</p>
  <p class="pe-ex__why">Ikkala qismda ham ega — <b>men</b>. Passiv boʻlmasa, gap oʻrtasida ega oʻqituvchiga oʻtib ketardi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Ikkinchi sabab — narsa haqida gapirish.</b>
  Kim qilgani muhim boʻlmaganda yaponcha ham xuddi oʻzbekcha
  kabi passivga oʻtadi: この<ruby>本<rt>ほん</rt></ruby>は
  <ruby>百年前<rt>ひゃくねんまえ</rt></ruby>に
  <ruby>書<rt>か</rt></ruby>かれました — «bu kitob yuz yil
  oldin yozilgan». Yangiliklar va ilmiy matnlar shunday
  yoziladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>祭<rt>まつ</rt></ruby>りは<ruby>三百年前<rt>さんびゃくねんまえ</rt></ruby>から<ruby>行<rt>おこな</rt></ruby>われています。</p>
  <p class="pe-ex__uz">Bu bayram uch yuz yildan beri oʻtkaziladi.</p>
  <p class="pe-ex__why">Passiv + ています — «hozir ham davom etadigan holat» (PJ-31). Yangiliklar tili shunday.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bir narsani ochiq aytib qoʻyaylik: bu shakl sizga
  notanish emas.</b> Oʻzbekchada «yoz<b>il</b>di»,
  «oʻq<b>il</b>di», «ayt<b>il</b>di», «top<b>il</b>di» —
  oʻzakka bitta boʻgʻin qoʻshiladi va feʼl teskari
  aylanadi. Yaponchada ham xuddi shunday, faqat boʻgʻin
  boshqa: <b>れる</b>. Yaʼni siz yangi fikrni emas, yangi
  qoʻshimchani oʻrganyapsiz — va bu darsdagi hamma
  qiyinchilik faqat oʻsha qoʻshimchani <em>qayerga</em>
  ulashda.</p>
</div>

<h3>4. ⚠️ 〜られる ning ikki maʼnosi</h3>

<p>Mana darsdagi eng chalkash joy. II guruh feʼllarida
<b>passiv va potensial shakl bir xil</b>:</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">POTENSIAL (PJ-42)</p>
    <p><ruby>私<rt>わたし</rt></ruby>はさしみが<ruby>食<rt>た</rt></ruby>べられます。</p>
    <p>«Men sashimi yeya olaman.» Toʻldiruvchi <b>が</b>.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">PASSIV (bugun)</p>
    <p>ケーキは<ruby>弟<rt>おとうと</rt></ruby>に<ruby>食<rt>た</rt></ruby>べられました。</p>
    <p>«Tortni ukam yeb qoʻydi.» Qiluvchi <b>に</b>.</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Ajratishning uchta belgisi.</b> (1) Gapda
  <b>に</b> bilan odam turibdimi? Unda passiv. (2)
  Toʻldiruvchi <b>が</b> bilanmi? Unda potensial. (3) Ega
  <em>jonsiz narsa</em>mi? Unda deyarli doim passiv —
  tort oʻzi yeya olmaydi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>I guruhda bunday muammo yoʻq.</b>
  <ruby>読<rt>よ</rt></ruby>める — potensial,
  <ruby>読<rt>よ</rt></ruby>まれる — passiv: ikki boshqa shakl.
  Chalkashlik faqat II guruh va <ruby>来<rt>く</rt></ruby>る
  da chiqadi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">受</span>
    <span class="pj-kanji__uz">qabul qilmoq</span>
    <span class="pj-kanji__on">オン: ジュ</span>
    <span class="pj-kanji__kun">KUN: う(ける)</span>
    <span class="pj-kanji__note">受身 (うけみ) — passiv · 受ける (うける) — qabul qilmoq, topshirmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">褒</span>
    <span class="pj-kanji__uz">maqtamoq</span>
    <span class="pj-kanji__on">オン: ホウ</span>
    <span class="pj-kanji__kun">KUN: ほ(める)</span>
    <span class="pj-kanji__note">褒める (ほめる) — maqtamoq · 褒められる — maqtalmoq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>言<rt>い</rt></ruby>あれる</p>
  <p class="pe-fix__good">✓ <ruby>言<rt>い</rt></ruby><b>わ</b>れる — う bilan tugagan feʼlda あ emas, <b>わ</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>食<rt>た</rt></ruby>べれる (passiv sifatida)</p>
  <p class="pe-fix__good">✓ <ruby>食<rt>た</rt></ruby><b>べられる</b> — II guruh passivi doim られる.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>は<ruby>先生<rt>せんせい</rt></ruby><b>が</b><ruby>褒<rt>ほ</rt></ruby>められました</p>
  <p class="pe-fix__good">✓ <ruby>先生<rt>せんせい</rt></ruby><b>に</b><ruby>褒<rt>ほ</rt></ruby>められました — qiluvchi <b>に</b> oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>来<rt>き</rt></ruby>られる</p>
  <p class="pe-fix__good">✓ <ruby>来<rt>こ</rt></ruby>られる — ない-oʻzagi <ruby>来<rt>こ</rt></ruby>ない, demak <b>こ</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>書<rt>か</rt></ruby>く ning passiv shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>書<rt>か</rt></ruby>かれる</b> — ない-oʻzagi <ruby>書<rt>か</rt></ruby>か, ustiga れる.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>言<rt>い</rt></ruby>う ning passiv shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>言<rt>い</rt></ruby>われる</b> — う bilan tugagan feʼlda <b>わ</b> chiqadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>来<rt>く</rt></ruby>る ning passiv shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>来<rt>こ</rt></ruby>られる</b> — ない-shakli <ruby>来<rt>こ</rt></ruby>ない.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>先生<rt>せんせい</rt></ruby>が<ruby>私<rt>わたし</rt></ruby>を<ruby>褒<rt>ほ</rt></ruby>めました» ni passivga oʻtkazing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>私<rt>わたし</rt></ruby>は<ruby>先生<rt>せんせい</rt></ruby>に<ruby>褒<rt>ほ</rt></ruby>められました</b></p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «ケーキは<ruby>弟<rt>おとうと</rt></ruby>に<ruby>食<rt>た</rt></ruby>べられました» — passivmi yoki potensialmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Passiv</b> — <ruby>弟<rt>おとうと</rt></ruby> <b>に</b> bilan turibdi, va ega (tort) jonsiz narsa.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>受身形<rt>うけみけい</rt></ruby></b> — passiv shakl</li>
  <li><b>〜れる / 〜られる</b> — passiv qoʻshimchasi</li>
  <li><b><ruby>褒<rt>ほ</rt></ruby>める</b> — maqtamoq (II guruh)</li>
  <li><b><ruby>叱<rt>しか</rt></ruby>る</b> — koyimoq (I guruh)</li>
  <li><b><ruby>呼<rt>よ</rt></ruby>ぶ</b> — chaqirmoq (I guruh)</li>
  <li><b><ruby>建<rt>た</rt></ruby>てる</b> — qurmoq (II guruh)</li>
  <li><b><ruby>選<rt>えら</rt></ruby>ぶ</b> — tanlamoq (I guruh)</li>
  <li><b><ruby>使<rt>つか</rt></ruby>う</b> — ishlatmoq (I guruh)</li>
  <li><b><ruby>発見<rt>はっけん</rt></ruby>する</b> — kashf qilmoq</li>
  <li><b><ruby>行<rt>おこな</rt></ruby>う</b> — oʻtkazmoq (I guruh)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Passiv <b>ない-oʻzagidan</b>: I guruh れる, II guruh られる.</li>
    <li>Qiluvchi <b>に</b> oladi — va yaponchada uni aytish tabiiy.</li>
    <li>II guruhda られる <b>passiv ham, potensial ham</b> — に va が ajratadi.</li>
  </ul>
</div>
""",
    },
]
