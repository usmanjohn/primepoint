# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-40 … PJ-42.

PJ-40 taklif qilish (ます oʻzagi), PJ-41 imkoniyat uzun yoʻl bilan
(lugʻat shakli + ことができます) va PJ-42 qisqa yoʻl — potensial shakl,
kursdagi birinchi haqiqiy yangi tuslanish.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_40_42.py --author=prime
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
        "title": "PJ-40: 〜ましょう va 〜ませんか — taklif qilish",
        "category": "japanese",
        "order": 40,
        "summary": (
            "«Ketaylik» va «bormaysizmi?». Ikkalasi ham taklif, lekin "
            "biri javobni oldindan bilib turadi, ikkinchisi esa soʻraydi — "
            "va yapon tilida bu farq muhim."
        ),
        "stories": ["まつりへ いきませんか"],
        "content": """
<h2>PJ-40: 〜ましょう va 〜ませんか — taklif qilish</h2>

<p>Bugungi ikki qolip bilan siz birinchi marta <b>boshqa odamni ishga
chaqirasiz</b>. Shu paytgacha oʻzingiz haqingizda gapirdingiz — nima
qilayotganingiz, nima xohlayotganingiz haqida; endi «keling, birga
qilaylik» deysiz.</p>

<p>Ikkalasi ham <b>ます oʻzagidan</b> yasaladi — oʻtgan ikki darsdagi
oʻzakning oʻzi. Yangi oʻzak yoʻq, faqat yangi oxirlar.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>«…aylik» deysiz: 〜ましょう</li>
    <li>«…maysizmi?» deb taklif qilasiz: 〜ませんか</li>
    <li>«Men qilayinmi?» deb yordam taklif qilasiz: 〜ましょうか</li>
    <li>Uchtasini muloyimlik boʻyicha tartiblaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta oʻzak, uchta oxir</span>
  <span class="pe-chip pe-chip--v"><ruby>行<rt>い</rt></ruby>きましょう</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o"><ruby>行<rt>い</rt></ruby>きませんか</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s"><ruby>行<rt>い</rt></ruby>きましょうか</span>
</div>

<h3>1. 〜ましょう — «…aylik»</h3>

<p>ます ni <b>ましょう</b> ga almashtiring. Bu — birga qilishga chaqiruv.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>ます shakli</th><th>ましょう</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>行<rt>い</rt></ruby>きます</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>きましょう</td><td class="pj-uz">boraylik</td></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べます</td><td class="pj-res"><ruby>食<rt>た</rt></ruby>べましょう</td><td class="pj-uz">yeylik</td></tr>
  <tr><td><ruby>休<rt>やす</rt></ruby>みます</td><td class="pj-res"><ruby>休<rt>やす</rt></ruby>みましょう</td><td class="pj-uz">dam olaylik</td></tr>
  <tr><td>します</td><td class="pj-res">しましょう</td><td class="pj-uz">qilaylik</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu «-aylik» qoʻshimchasi:</b> «bor<b>aylik</b>»,
  «qil<b>aylik</b>», «dam ol<b>aylik</b>». Ikki tilda ham u feʼlga
  yopishadi va alohida soʻz talab qilmaydi. Farqi bitta:
  <ruby>行<rt>い</rt></ruby>きましょう <em>muloyim</em> shakl, oʻzbekcha
  «boraylik» esa neytral. Yaponcha oddiy shakli
  (<ruby>行<rt>い</rt></ruby>こう) keyingi bloklarda keladi.</p>
</div>

<h3>2. 〜ませんか — «…maysizmi?»</h3>

<p>Bu ham taklif, lekin <b>savol shaklida</b>. Yaʼni siz suhbatdoshga
tanlash imkonini berasiz.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>今日<rt>きょう</rt></ruby><ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>ませんか。</p>
  <p class="pe-ex__rom">kyō ēga o mimasen ka</p>
  <p class="pe-ex__uz">Bugun kino koʻrmaysizmi?</p>
  <p class="pe-ex__why">Shakli inkor, maʼnosi esa <b>taklif</b>. Oʻzbekchada ham xuddi shunday: «choy ichmaysizmi?» — bu rad emas, taklif.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Nega inkor shakli muloyimroq?</b> Chunki inkor savol
  suhbatdoshga «yoʻq» deyish uchun joy qoldiradi. ましょう esa javobni
  deyarli hal qilib qoʻyadi. Shuning uchun <b>yangi tanishga</b> yoki
  <b>kattaroq odamga</b> ませんか bilan murojaat qiling.</p>
</div>

<h3>3. Muloyimlik zinapoyasi</h3>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name">ましょう</span>
    <span class="pj-level__ja"><ruby>行<rt>い</rt></ruby>きましょう</span>
    <span class="pj-level__who">roziligini bilaman — doʻstlar, reja tuzilgan</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name">ませんか</span>
    <span class="pj-level__ja"><ruby>行<rt>い</rt></ruby>きませんか</span>
    <span class="pj-level__who">taklif qilaman — yangi tanish, kattaroq odam</span>
  </div>
</div>

<p>Odatiy suhbat ikkalasini birga ishlatadi: avval <b>ませんか</b> bilan
taklif qilinadi, rozilikdan keyin esa <b>ましょう</b> bilan reja tuziladi —
qayerda uchrashish, soat nechada, kim nima olib kelishi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">— <ruby>週末<rt>しゅうまつ</rt></ruby>に<ruby>海<rt>うみ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きませんか。<br>— いいですね。<ruby>朝<rt>あさ</rt></ruby><ruby>八時<rt>はちじ</rt></ruby>に<ruby>会<rt>あ</rt></ruby>いましょう。</p>
  <p class="pe-ex__rom">shūmatsu ni umi e ikimasen ka / ii desu ne. asa hachiji ni aimashō</p>
  <p class="pe-ex__uz">— Dam olish kuni dengizga bormaysizmi? — Yaxshi boʻlardi. Ertalab soat sakkizda uchrashaylik.</p>
  <p class="pe-ex__why">Taklif <b>ませんか</b> bilan, rozilik <b>いいですね</b> bilan, keyin reja <b>ましょう</b> bilan. Bu — deyarli qolipga aylangan tartib.</p>
</div>

<h3>4. 〜ましょうか — «men qilayinmi?»</h3>

<p>ましょう ga <b>か</b> qoʻshsangiz, maʼno oʻzgaradi: bu endi birga
qilish emas, <b>oʻzingiz</b> yordam berishni taklif qilish.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">BIRGA</p>
    <p><ruby>手伝<rt>てつだ</rt></ruby>いましょう</p>
    <p>Yordam beraylik. Ikkalamiz.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">MEN</p>
    <p><ruby>手伝<rt>てつだ</rt></ruby>いましょうか</p>
    <p>Yordam berayinmi? Faqat men.</p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>Bu — kundalik hayotda juda koʻp eshitiladigan ibora.</b>
  <ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けましょうか
  («derazani ochayinmi?»),
  <ruby>持<rt>も</rt></ruby>ちましょうか («koʻtarib berayinmi?»). Uni
  tayyor holda yodlab qoʻying — hatto grammatikani oʻylamasdan
  ishlatasiz.</p>
</div>

<h3>5. <ruby>一緒<rt>いっしょ</rt></ruby>に — «birga»</h3>

<p>Taklif qilganda deyarli har doim bitta soʻz qoʻshiladi:
<b><ruby>一緒<rt>いっしょ</rt></ruby>に</b> — «birga». Usiz ham gap
toʻgʻri, lekin u taklifni ancha issiqroq qiladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>昼<rt>ひる</rt></ruby>ごはんを<ruby>食<rt>た</rt></ruby>べませんか。</p>
  <p class="pe-ex__rom">issho ni hirugohan o tabemasen ka</p>
  <p class="pe-ex__uz">Birga tushlik qilmaysizmi?</p>
  <p class="pe-ex__why"><ruby>一緒<rt>いっしょ</rt></ruby>に odatda gap boshida turadi — vaqt soʻzidan keyin, toʻldiruvchidan oldin.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Kim bilan ekanini aytish kerak boʻlsa</b>, PJ-19 dagi
  <b>と</b> ishlatiladi:
  <ruby>友<rt>とも</rt></ruby>だち<b>と</b><ruby>一緒<rt>いっしょ</rt></ruby>に —
  «doʻstim bilan birga». Ikkalasi juft yuradi va shu tartibda turadi.</p>
</div>

<h3>6. ましょう taklif boʻlmaganda</h3>

<p>Bitta qoʻshimcha vazifasi bor: eʼlon va koʻrsatmalarda ましょう
<em>hech kimni chaqirmaydi</em> — u umumiy chaqiriq boʻlib turadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Ibora</th><th>Qayerda koʻrinadi</th></tr>
  <tr><td class="pj-res"><ruby>気<rt>き</rt></ruby>をつけましょう</td><td class="pj-uz">«ehtiyot boʻlaylik» — koʻcha belgilari</td></tr>
  <tr><td class="pj-res"><ruby>手<rt>て</rt></ruby>を<ruby>洗<rt>あら</rt></ruby>いましょう</td><td class="pj-uz">«qoʻlni yuvaylik» — maktab, kasalxona</td></tr>
  <tr><td class="pj-res"><ruby>静<rt>しず</rt></ruby>かにしましょう</td><td class="pj-uz">«jim boʻlaylik» — kutubxona</td></tr>
</table></div>

<p>Bu — yaponcha eʼlonlarning odatiy ohangi: buyruq emas, birgalikka
chaqiriq. PJ-33 dagi
<ruby>走<rt>はし</rt></ruby>ってはいけません qatʼiy taqiq edi; bu esa
yumshoq eslatma. Ikkalasini bir belgida ham koʻrishingiz mumkin.</p>

<h3>7. Javob berish</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Javob</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res">いいですね</td><td class="pj-uz">yaxshi boʻlardi — rozilik</td></tr>
  <tr><td class="pj-res">ぜひ</td><td class="pj-uz">albatta, jon deb</td></tr>
  <tr><td class="pj-res">はい、お<ruby>願<rt>ねが</rt></ruby>いします</td><td class="pj-uz">ha, iltimos (yordamga)</td></tr>
  <tr><td class="pj-res">すみません、ちょっと…</td><td class="pj-uz">muloyim rad javobi</td></tr>
</table></div>

<p>Oxirgisi tanish — PJ-32 dagi rad javobining oʻzi. Yapon tilida «yoʻq»
deyishning yoʻli bitta va u har joyda ishlaydi: taklifni rad qilishda ham,
ruxsat bermaslikda ham.</p>

<p>Rad qilganda sabab aytish shart emas va koʻpincha aytilmaydi ham —
«ちょっと…» ning oʻzi hammasini tushuntiradi. Sabab qoʻshsangiz
(«<ruby>宿題<rt>しゅくだい</rt></ruby>がありますから…»), gap yanada
yumshoq eshitiladi, lekin yaponlar buni ham koʻpincha yarim yoʻlda
toʻxtatib qoʻyadi.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>くましょう</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby><b>き</b>ましょう — ましょう <b>ます oʻzagiga</b> qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>きましょうでした</p>
  <p class="pe-fix__good">✓ ましょう zamon olmaydi — u doim kelajakka qaraydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Yangi tanishga: <ruby>行<rt>い</rt></ruby>きましょう</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>きま<b>せんか</b> — begona odamga taklifni <b>savol</b> shaklida bering.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>食<rt>た</rt></ruby>べる dan «yeylik» ni yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>食<rt>た</rt></ruby>べましょう</b> — ます oʻrniga ましょう.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Kino koʻrmaysizmi?» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>ませんか。</b></p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. ましょう va ませんか — qaysi biri muloyimroq?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ませんか</b> — u suhbatdoshga «yoʻq» deyish uchun joy qoldiradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Derazani ochayinmi?» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けましょうか。</b> か qoʻshilsa, maʼno «men qilayinmi» boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Taklifga rozilik qanday bildiriladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>いいですね</b> yoki <b>ぜひ</b>. Rad javobi esa — «すみません、ちょっと…».</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜ましょう</b> — …aylik</li>
  <li><b>〜ませんか</b> — …maysizmi? (taklif)</li>
  <li><b>〜ましょうか</b> — men …ayinmi?</li>
  <li><b>いいですね</b> — yaxshi boʻlardi</li>
  <li><b>ぜひ</b> — albatta, jon deb</li>
  <li><b>お<ruby>願<rt>ねが</rt></ruby>いします</b> — iltimos</li>
  <li><b><ruby>週末<rt>しゅうまつ</rt></ruby></b> — dam olish kuni</li>
  <li><b><ruby>祭<rt>まつ</rt></ruby>り</b> — bayram, xalq festivali</li>
  <li><b><ruby>一緒<rt>いっしょ</rt></ruby>に</b> — birga</li>
  <li><b><ruby>誘<rt>さそ</rt></ruby>う</b> — taklif qilmoq, chorlamoq (I guruh)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Ikkalasi ham <b>ます oʻzagidan</b>: ましょう va ませんか.</li>
    <li><b>ませんか muloyimroq</b> — u «yoʻq» uchun joy qoldiradi.</li>
    <li><b>ましょうか</b> — birga emas, <b>men</b> qilayinmi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-41: Imkoniyat 1 — 〜ことができます",
        "category": "japanese",
        "order": 41,
        "summary": (
            "«Qila olaman» ni aytishning uzun, lekin oson yoʻli. Bitta qoida, "
            "hech qanday tuslanish — va u har qanday feʼl bilan ishlaydi."
        ),
        "stories": ["ピアノを ひくことが できます"],
        "content": """
<h2>PJ-41: Imkoniyat 1 — 〜ことができます</h2>

<p>Yapon tilida «qila olaman» ni ikki xil aytish mumkin. Biri — uzun,
lekin <b>hech qanday yangi tuslanish talab qilmaydigan</b> yoʻl; ikkinchisi
qisqa, lekin feʼlni oʻzgartirishni talab qiladi.</p>

<p>Bugun oson yoʻlni olamiz. Keyingi darsda qisqasini — va shunda
ikkalasini yonma-yon qoʻyib, qaysi birini qachon tanlashni
koʻrasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Lugʻat shakli + ことができます qolipini yasaysiz</li>
    <li>Otdan ham imkoniyat gapini tuzasiz: 〜ができます</li>
    <li>Inkor va oʻtgan zamon shakllarini yasaysiz</li>
    <li>こと nima uchun kerakligini va nima qilishini tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Lugʻat shakli + こと + が + できます</span>
  <span class="pe-chip pe-chip--s"><ruby>泳<rt>およ</rt></ruby>ぐ</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v"><ruby>泳<rt>およ</rt></ruby>ぐことができます</span>
</div>

<h3>1. Yasalishi</h3>

<p>Feʼlni <b>lugʻat shaklida</b> qoldiring, ustiga
<b>ことができます</b> qoʻshing. Hech narsa oʻzgarmaydi — bu qolipning
butun jozibasi shunda.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat shakli</th><th>Imkoniyat</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>泳<rt>およ</rt></ruby>ぐ</td><td class="pj-res"><ruby>泳<rt>およ</rt></ruby>ぐことができます</td><td class="pj-uz">suza olaman</td></tr>
  <tr><td><ruby>話<rt>はな</rt></ruby>す</td><td class="pj-res"><ruby>話<rt>はな</rt></ruby>すことができます</td><td class="pj-uz">gapira olaman</td></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-res"><ruby>食<rt>た</rt></ruby>べることができます</td><td class="pj-uz">yeya olaman</td></tr>
  <tr><td><ruby>来<rt>く</rt></ruby>る</td><td class="pj-res"><ruby>来<rt>く</rt></ruby>ることができます</td><td class="pj-uz">kela olaman</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Uchala guruh ham bir xil.</b> I, II, III — farqi yoʻq, chunki
  feʼl umuman tuslanmaydi. Shuning uchun bu qolip yangi feʼl
  uchraganda eng ishonchli tanlov: guruhini bilmasangiz ham
  ishlaydi.</p>
</div>

<p>Bu kursda kam uchraydigan holat: qolip <em>uzunroq</em>, lekin
<em>osonroq</em>. Odatda yapon grammatikasi teskari yoʻldan boradi —
qisqartirish uchun tuslanish talab qiladi. Keyingi darsda aynan shunday
boʻladi.</p>

<h3>2. こと nima qilyapti</h3>

<p>こと — «ish, narsa» degan ot, va siz uni PJ-35 da koʻrgansiz:
<ruby>行<rt>い</rt></ruby>った<b>こと</b>があります. Bu yerda ham u
xuddi shu ishni bajaradi — <b>feʼlni otga aylantiradi</b>.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>泳<rt>およ</rt></ruby>ぐこと</span>
  <span class="pj-joshi__p">が<small>EGA</small></span>
  <span class="pj-joshi__v">できます</span>
  <span class="pj-joshi__uz">Suzish mumkin. — soʻzma-soʻz: «suzish ishi bajariladi».</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham xuddi shunday qilish mumkin:</b> «suz<b>ish</b>ni
  bilaman», «gapir<b>ish</b>ni uddalayman» — bu yerda ham feʼl
  «-ish» qoʻshimchasi bilan otga aylanadi. Yaponcha こと oʻsha
  «-ish» ning oʻzi. Shuning uchun bu qolipni yodlashning eng oson yoʻli
  — uni <b>«…ish mumkin»</b> deb tarjima qilish.</p>
</div>

<h3>3. Ot bilan: 〜ができます</h3>

<p>Agar imkoniyat <em>koʻnikma</em> haqida boʻlsa va uning oti boʻlsa,
こと kerak emas — otning oʻzi <b>が</b> oladi. Bu koʻproq til, musiqa
asbobi, sport va kasb-hunar bilan ishlaydi: yaʼni <em>oʻrganib
olinadigan</em> narsalar bilan.</p>

<p>Farqni sezish oson: <ruby>日本語<rt>にほんご</rt></ruby>ができます
degan odam til <em>biladi</em>; <ruby>日本語<rt>にほんご</rt></ruby>を
<ruby>話<rt>はな</rt></ruby>すことができます degan odam esa aniq bitta
ishni — gapirishni — uddalaydi. Birinchisi kengroq.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yaponcha</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res"><ruby>日本語<rt>にほんご</rt></ruby>ができます</td><td class="pj-uz">yapon tilini bilaman</td></tr>
  <tr><td class="pj-res">ピアノができます</td><td class="pj-uz">pianino chala olaman</td></tr>
  <tr><td class="pj-res"><ruby>料理<rt>りょうり</rt></ruby>ができます</td><td class="pj-uz">ovqat pishira olaman</td></tr>
</table></div>

<h3>4. Inkor va oʻtgan zamon</h3>

<p>できます oddiy feʼl, shuning uchun u odatdagidek tuslanadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Yaponcha</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-res"><ruby>泳<rt>およ</rt></ruby>ぐことができます</td><td class="pj-uz">suza olaman</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-res"><ruby>泳<rt>およ</rt></ruby>ぐことができません</td><td class="pj-uz">suza olmayman</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-res"><ruby>泳<rt>およ</rt></ruby>ぐことができました</td><td class="pj-uz">suza oldim</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>は<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>話<rt>はな</rt></ruby>すことができますが、<ruby>漢字<rt>かんじ</rt></ruby>を<ruby>書<rt>か</rt></ruby>くことができません。</p>
  <p class="pe-ex__rom">watashi wa nihongo o hanasu koto ga dekimasu ga, kanji o kaku koto ga dekimasen</p>
  <p class="pe-ex__uz">Yapon tilida gapira olaman, lekin iyeroglif yoza olmayman.</p>
  <p class="pe-ex__why">Diqqat: feʼlning oʻz toʻldiruvchisi <b>を</b> ni saqlaydi (<ruby>日本語<rt>にほんご</rt></ruby>を), こと esa <b>が</b> oladi. Ikki qoʻshimcha bir gapda.</p>
</div>

<h3>5. Koʻnikma haqida gapirish: <ruby>上手<rt>じょうず</rt></ruby> va <ruby>下手<rt>へた</rt></ruby></h3>

<p>«Qila olaman» bilan yonma-yon yuradigan ikkita な-sifat bor:
<b><ruby>上手<rt>じょうず</rt></ruby></b> («mohir») va
<b><ruby>下手<rt>へた</rt></ruby></b> («uquvsiz»). Ular ham
<b>が</b> oladi — PJ-26 dagi <ruby>好<rt>す</rt></ruby>き kabi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">ムニラさんは<ruby>料理<rt>りょうり</rt></ruby>が<ruby>上手<rt>じょうず</rt></ruby>です。<ruby>私<rt>わたし</rt></ruby>は<ruby>下手<rt>へた</rt></ruby>です。</p>
  <p class="pe-ex__rom">munira-san wa ryōri ga jōzu desu. watashi wa heta desu</p>
  <p class="pe-ex__uz">Munira ovqat pishirishga mohir. Men uquvsizman.</p>
  <p class="pe-ex__why">が yana oʻsha joyda. «Uddalash», «yoqish», «xohish» — hammasi holat, va holat gapida narsa <b>ega</b> boʻlib turadi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b><ruby>上手<rt>じょうず</rt></ruby> ni oʻzingiz haqingizda
  ishlatmang.</b> «Men mohirman» degan gap yaponchada maqtanchoqlik
  boʻlib eshitiladi. Oʻzingiz haqingizda
  <ruby>下手<rt>へた</rt></ruby> yoki
  «まだ<ruby>上手<rt>じょうず</rt></ruby>ではありません» deng — kamtarlik
  bu yerda odat emas, <em>qoida</em>.</p>
</div>

<h3>6. Qachon ishlatiladi</h3>

<p>Bu qolip keyingi darsdagi qisqa shakldan biroz <b>rasmiyroq</b>
eshitiladi. U yozma tilda, eʼlonlarda va rasmiy suhbatda koʻproq
uchraydi — yaʼni odam odamga emas, tashkilot odamga gapirganda.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qayerda</th><th>Misol</th></tr>
  <tr><td class="pj-uz">Eʼlon</td><td class="pj-res">ここで<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ることができます</td></tr>
  <tr><td class="pj-uz">Rasmiy savol</td><td class="pj-res"><ruby>来<rt>く</rt></ruby>ることができますか</td></tr>
  <tr><td class="pj-uz">Yozma til</td><td class="pj-res"><ruby>予約<rt>よやく</rt></ruby>することができます</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Boshlangʻich bosqichda bu — sizning ishonchli quroliningiz.</b>
  Keyingi darsda qisqa shakl keladi va u kundalik nutqda koʻproq
  ishlatiladi, lekin u har bir guruh uchun alohida qoida talab qiladi.
  Shoshilmang: ことができます bilan siz istalgan feʼldan imkoniyat gapini
  <b>bugunoq</b> tuza olasiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>泳<rt>およ</rt></ruby>ぎことができます</p>
  <p class="pe-fix__good">✓ <ruby>泳<rt>およ</rt></ruby><b>ぐ</b>ことができます — こと oldida <b>lugʻat shakli</b> turadi, ます oʻzagi emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>泳<rt>およ</rt></ruby>ぐことをできます</p>
  <p class="pe-fix__good">✓ <ruby>泳<rt>およ</rt></ruby>ぐこと<b>が</b>できます — こと bu yerda <b>ega</b>, toʻldiruvchi emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>日本語<rt>にほんご</rt></ruby>をできます</p>
  <p class="pe-fix__good">✓ <ruby>日本語<rt>にほんご</rt></ruby><b>が</b>できます — できます ham が oladi, xuddi <ruby>好<rt>す</rt></ruby>き kabi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>読<rt>よ</rt></ruby>む dan «oʻqiy olaman» ni yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>読<rt>よ</rt></ruby>むことができます</b> — lugʻat shakli oʻzgarmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. こと bu qolipda nima qilyapti?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Feʼlni otga aylantiryapti</b> — oʻzbekchadagi «-ish» kabi: «suz<b>ish</b> mumkin».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Yapon tilini bilaman» ni ot bilan ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>日本語<rt>にほんご</rt></ruby>ができます。</b> Ot bilan こと kerak emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Suza olmayman» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>泳<rt>およ</rt></ruby>ぐことができません。</b> できます oddiy feʼl kabi tuslanadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega bu qolip yangi feʼl uchun ishonchli?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki feʼl <b>umuman tuslanmaydi</b> — guruhini bilmasangiz ham ishlaydi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜ことができます</b> — …ish mumkin, qila olaman</li>
  <li><b>〜ができます</b> — (ot bilan) uddalayman</li>
  <li><b>こと</b> — ish, narsa (feʼlni otga aylantiradi)</li>
  <li><b>ピアノ</b> — pianino, royal</li>
  <li><b><ruby>料理<rt>りょうり</rt></ruby></b> — ovqat, pishirish</li>
  <li><b><ruby>弾<rt>ひ</rt></ruby>く</b> — chalmoq (I guruh)</li>
  <li><b><ruby>運転<rt>うんてん</rt></ruby>する</b> — mashina haydamoq</li>
  <li><b><ruby>予約<rt>よやく</rt></ruby>する</b> — oldindan buyurtma bermoq</li>
  <li><b><ruby>上手<rt>じょうず</rt></ruby></b> — mohir (な-sifat)</li>
  <li><b><ruby>下手<rt>へた</rt></ruby></b> — uquvsiz (な-sifat)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Lugʻat shakli + ことができます</b> — feʼl tuslanmaydi.</li>
    <li>こと feʼlni <b>otga</b> aylantiradi, shuning uchun <b>が</b> oladi.</li>
    <li>Ot bilan こと kerak emas: <ruby>日本語<rt>にほんご</rt></ruby>ができます.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-42: Imkoniyat 2 — potensial shakl (読める, 食べられる)",
        "category": "japanese",
        "order": 42,
        "summary": (
            "Qisqa yoʻl. Feʼlning oʻzi oʻzgaradi — va natija har doim "
            "II guruh feʼli boʻlib chiqadi, shuning uchun keyingisi tanish."
        ),
        "stories": ["いまは およげます"],
        "content": """
<h2>PJ-42: Imkoniyat 2 — potensial shakl (<ruby>読<rt>よ</rt></ruby>める, <ruby>食<rt>た</rt></ruby>べられる)</h2>

<p>Oʻtgan darsda imkoniyatni <em>qoʻshimcha soʻzlar</em> bilan aytdingiz.
Bugun feʼlning oʻzini oʻzgartirasiz — va natija ancha qisqa, kundalik
nutqda esa ancha koʻp uchraydi.</p>

<p>Bu — kursdagi <b>birinchi haqiqiy yangi tuslanish</b>: shu paytgacha
oʻzaklar allaqachon mavjud edi, endi esa yangi shakl yasaymiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uchala guruhda potensial shakl yasaysiz</li>
    <li>を oʻrniga <b>が</b> qoʻyishni oʻrganasiz</li>
    <li>Natija har doim II guruh feʼli ekanini koʻrasiz</li>
    <li>Qaysi qolipni qachon tanlashni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Guruhga qarab</span>
  <span class="pe-chip pe-chip--s">I: う → え + る</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">II: る → られる</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">III: できる · <ruby>来<rt>こ</rt></ruby>られる</span>
</div>

<h3>1. I guruh — え qatoriga</h3>

<p>Oxirgi tovushni <b>え qatoriga</b> koʻtaring va <b>る</b> qoʻshing.
Bu — toʻrtinchi qator: ます い ga, ない あ ga, potensial esa
<b>え</b> ga.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat</th><th>え qatori</th><th>Potensial</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-uz">め</td>
      <td class="pj-res"><ruby>読<rt>よ</rt></ruby>める</td><td class="pj-uz">oʻqiy olmoq</td></tr>
  <tr><td><ruby>書<rt>か</rt></ruby>く</td><td class="pj-uz">け</td>
      <td class="pj-res"><ruby>書<rt>か</rt></ruby>ける</td><td class="pj-uz">yoza olmoq</td></tr>
  <tr><td><ruby>泳<rt>およ</rt></ruby>ぐ</td><td class="pj-uz">げ</td>
      <td class="pj-res"><ruby>泳<rt>およ</rt></ruby>げる</td><td class="pj-uz">suza olmoq</td></tr>
  <tr><td><ruby>話<rt>はな</rt></ruby>す</td><td class="pj-uz">せ</td>
      <td class="pj-res"><ruby>話<rt>はな</rt></ruby>せる</td><td class="pj-uz">gapira olmoq</td></tr>
  <tr><td><ruby>買<rt>か</rt></ruby>う</td><td class="pj-uz">え</td>
      <td class="pj-res"><ruby>買<rt>か</rt></ruby>える</td><td class="pj-uz">sotib ola olmoq</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>う → え, «わ» emas.</b> ない-shaklida
  <ruby>買<rt>か</rt></ruby>う <b>わ</b> ni olgan edi
  (<ruby>買<rt>か</rt></ruby>わない), bu yerda esa oddiy <b>え</b>:
  <ruby>買<rt>か</rt></ruby>える. Ikkalasini aralashtirmang.</p>
</div>

<h3>2. II guruh — られる</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat</th><th>Potensial</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-res"><ruby>食<rt>た</rt></ruby>べられる</td><td class="pj-uz">yeya olmoq</td></tr>
  <tr><td><ruby>見<rt>み</rt></ruby>る</td><td class="pj-res"><ruby>見<rt>み</rt></ruby>られる</td><td class="pj-uz">koʻra olmoq</td></tr>
  <tr><td><ruby>起<rt>お</rt></ruby>きる</td><td class="pj-res"><ruby>起<rt>お</rt></ruby>きられる</td><td class="pj-uz">tura olmoq</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Kundalik nutqda ら tashlab ketiladi:</b>
  <ruby>食<rt>た</rt></ruby>べ<b>れる</b>,
  <ruby>見<rt>み</rt></ruby><b>れる</b>. Bu — «<ruby>ら抜<rt>らぬ</rt></ruby>き
  <ruby>言葉<rt>ことば</rt></ruby>» deb ataladi va yoshlar orasida juda
  keng tarqalgan. Lekin imtihonda va yozma tilda <b>ら</b> ni tashlamang
  — u yerda られる toʻgʻri hisoblanadi.</p>
</div>

<h3>3. III guruh — yodlanadi</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat</th><th>Potensial</th><th>Maʼnosi</th></tr>
  <tr><td>する</td><td class="pj-res">できる</td><td class="pj-uz">qila olmoq</td></tr>
  <tr><td><ruby>来<rt>く</rt></ruby>る</td><td class="pj-res"><ruby>来<rt>こ</rt></ruby>られる</td><td class="pj-uz">kela olmoq</td></tr>
</table></div>

<p>する ning qoʻshma feʼllari ham shu yoʻldan boradi:
<ruby>勉強<rt>べんきょう</rt></ruby>する →
<ruby>勉強<rt>べんきょう</rt></ruby><b>できる</b>,
<ruby>運転<rt>うんてん</rt></ruby>する →
<ruby>運転<rt>うんてん</rt></ruby><b>できる</b>. Yaʼni yuzlab feʼl
uchun bitta shakl kifoya.</p>

<div class="pe-call pe-rule">
  <p><b>できる tanish.</b> Oʻtgan darsda uni ことが<b>できます</b> ichida
  koʻrgansiz — u oʻsha feʼlning oʻzi. Yaʼni する ning potensial shakli
  butun kurs davomida sizning oldingizda turgan edi.
  <ruby>来<rt>く</rt></ruby>る esa yana oʻqilishini oʻzgartiradi:
  <ruby>来<rt>こ</rt></ruby>られる.</p>
</div>

<h3>4. Natija — har doim II guruh</h3>

<p>Mana eng foydali xabar. Har qanday potensial shakl <b>る</b> bilan
tugaydi va undan oldin <b>え</b> yoki <b>い</b> turadi — yaʼni u
<b>II guruh feʼli</b>. Demak keyingisini siz allaqachon bilasiz.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th><ruby>読<rt>よ</rt></ruby>める</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">ます</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>めます</td><td class="pj-uz">oʻqiy olaman</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>めません</td><td class="pj-uz">oʻqiy olmayman</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>めました</td><td class="pj-uz">oʻqiy oldim</td></tr>
  <tr><td class="pj-stem">て</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>めて</td><td class="pj-uz">oʻqiy olib</td></tr>
</table></div>

<h3>5. を oʻrniga が</h3>

<p>Potensial gapda toʻldiruvchi odatda <b>を</b> emas, <b>が</b> oladi —
chunki gap endi <em>ish</em> haqida emas, <em>imkoniyat</em> haqida.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">ODDIY</p>
    <p><ruby>本<rt>ほん</rt></ruby><b>を</b><ruby>読<rt>よ</rt></ruby>みます</p>
    <p>Kitob oʻqiyman — ish.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">POTENSIAL</p>
    <p><ruby>本<rt>ほん</rt></ruby><b>が</b><ruby>読<rt>よ</rt></ruby>めます</p>
    <p>Kitob oʻqiy olaman — imkoniyat.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>が bu yerda tasodif emas.</b> PJ-26 da
  <ruby>好<rt>す</rt></ruby>き が oldi, PJ-39 da ほしい が oldi, PJ-41 da
  できます が oldi — endi potensial shakl ham. Qoida bitta va u butun
  kursni bogʻlaydi: <b>yapon tilida «xohish, yoqish, uddalash» —
  holat</b>, ish emas. Holat gapida esa narsa <em>ega</em> boʻlib turadi.
  Oʻzbekchada ham «menga musiqa <em>yoqadi</em>» degan gapda musiqa —
  ega. Shuni eslasangiz, が ni hech qachon unutmaysiz.</p>
</div>

<h3>6. Qaysi qolipni tanlash</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Qayerda</th></tr>
  <tr><td class="pj-end">Potensial shakl</td><td class="pj-uz">kundalik nutq — eng koʻp ishlatiladi</td></tr>
  <tr><td class="pj-end">〜ことができます</td><td class="pj-uz">rasmiy til, eʼlon, yozma matn</td></tr>
</table></div>

<p>Maʼnosi bir xil, shuning uchun xato qilish qiyin. Yangi feʼl uchrasa va
guruhiga ishonchingiz komil boʻlmasa — ことができます bilan ayting,
u har doim toʻgʻri.</p>

<p>Bir nozik farq bor: potensial shakl koʻpincha <b>shaxsiy qobiliyat</b>
haqida, ことができます esa <b>sharoit ruxsat berishi</b> haqida ham
gapiradi. «Bu yerda rasmga olsa boʻladi» degan eʼlonda
<ruby>撮<rt>と</rt></ruby>ることができます tabiiyroq eshitiladi —
chunki gap sizning qobiliyatingiz haqida emas, qoida haqida. Lekin bu
qatʼiy chegara emas va boshlangʻich bosqichda uni oʻylab
oʻtirmasangiz ham boʻladi.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>買<rt>か</rt></ruby>われる</p>
  <p class="pe-fix__good">✓ <ruby>買<rt>か</rt></ruby><b>える</b> — potensialda う <b>え</b> ga koʻtariladi; わ faqat ない-shaklida.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>めます</p>
  <p class="pe-fix__good">✓ <ruby>本<rt>ほん</rt></ruby><b>が</b><ruby>読<rt>よ</rt></ruby>めます — potensial gapda toʻldiruvchi が oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>食<rt>た</rt></ruby>べられるます</p>
  <p class="pe-fix__good">✓ <ruby>食<rt>た</rt></ruby>べ<b>られます</b> — natija II guruh feʼli, demak る tushadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>泳<rt>およ</rt></ruby>ぐ ning potensial shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>泳<rt>およ</rt></ruby>げる</b> — ぐ え qatoriga: げ, keyin る.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>食<rt>た</rt></ruby>べる ning potensial shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>食<rt>た</rt></ruby>べられる</b> — II guruhda る oʻrniga られる.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Kitob oʻqiy olaman» da toʻldiruvchi qaysi qoʻshimchani oladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>が</b>: <ruby>本<rt>ほん</rt></ruby>が<ruby>読<rt>よ</rt></ruby>めます. Imkoniyat — holat, ish emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Potensial shakl qaysi guruhga tegishli boʻlib chiqadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>II guruh</b> — る bilan tugaydi va oldida え yoki い turadi. Demak ます, ない, て — hammasi tanish.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. する ning potensial shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>できる</b> — va siz uni oʻtgan darsdan ことができます ichida bilasiz.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>読<rt>よ</rt></ruby>める</b> — oʻqiy olmoq</li>
  <li><b><ruby>書<rt>か</rt></ruby>ける</b> — yoza olmoq</li>
  <li><b><ruby>泳<rt>およ</rt></ruby>げる</b> — suza olmoq</li>
  <li><b><ruby>話<rt>はな</rt></ruby>せる</b> — gapira olmoq</li>
  <li><b><ruby>食<rt>た</rt></ruby>べられる</b> — yeya olmoq</li>
  <li><b>できる</b> — qila olmoq (する ning potensiali)</li>
  <li><b><ruby>来<rt>こ</rt></ruby>られる</b> — kela olmoq</li>
  <li><b><ruby>ら抜<rt>らぬ</rt></ruby>き<ruby>言葉<rt>ことば</rt></ruby></b> — ら tashlangan nutq</li>
  <li><b><ruby>練習<rt>れんしゅう</rt></ruby>する</b> — mashq qilmoq</li>
  <li><b>まだ</b> — hali</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>I: <b>え qatori + る</b> · II: <b>られる</b> · III: できる, <ruby>来<rt>こ</rt></ruby>られる.</li>
    <li>Natija <b>doim II guruh feʼli</b> — keyingi tuslanish tanish.</li>
    <li>Toʻldiruvchi <b>が</b> oladi: <ruby>本<rt>ほん</rt></ruby>が<ruby>読<rt>よ</rt></ruby>めます.</li>
  </ul>
</div>
""",
    },
]
