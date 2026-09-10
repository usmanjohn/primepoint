# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-37 … PJ-39.

Uchala oʻzak endi tayyor, va bu uchlik ularni ishga soladi: ish tartibi
(て + た + lugʻat shakli bir darsda), bir vaqtda ikki ish (ます oʻzagi) va
xohish (yana ます oʻzagi, lekin natija い-sifat).

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_37_39.py --author=prime
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
        "title": "PJ-37: 〜てから, 〜まえに, 〜あとで — ish tartibi",
        "category": "japanese",
        "order": 37,
        "summary": (
            "«Oldin», «keyin» va «…gandan soʻng». Uchta qolip, uchta har xil "
            "oʻzak — va まえに ning oʻzagi gapning zamoniga umuman qaramaydi."
        ),
        "stories": ["いえを でるまえに"],
        "content": """
<h2>PJ-37: 〜てから, 〜まえに, 〜あとで — ish tartibi</h2>

<p>Sizda endi feʼlning uchala oʻzagi ham bor: <b>て</b>, <b>た</b> va
<b>lugʻat shakli</b>. Bugungi dars ularning uchalasini bir vaqtda ishga
soladi — chunki ish tartibini bildiradigan uchta qolip <em>uchta har xil
oʻzakni</em> talab qiladi.</p>

<p>Shu sababli bu dars biroz eʼtibor talab qiladi. Lekin yaxshi xabar ham
bor: qaysi oʻzak kerakligini <b>gapning zamoni hal qilmaydi</b>. Har bir
qolipning oʻzagi qatʼiy.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>«…gandan keyin» ni ikki xil aytasiz</li>
    <li>«…dan oldin» ni aytasiz — lugʻat shakli bilan</li>
    <li>Ot bilan ham ishlatasiz: の まえに / の あとで</li>
    <li>Uchtasini bir jadvalda ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Har biriga oʻz oʻzagi</span>
  <span class="pe-chip pe-chip--v">て + から</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">lugʻat + まえに</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">た + あとで</span>
</div>

<h3>1. 〜てから — «…gandan keyin»</h3>

<p>て-shakliga <b>から</b> qoʻshiladi. Bu qolip ikki ishning
<em>ketma-ketligini</em> taʼkidlaydi: birinchisi <b>tugagandan soʻng</b>
ikkinchisi boshlanadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>宿題<rt>しゅくだい</rt></ruby>をしてから、テレビを<ruby>見<rt>み</rt></ruby>ます。</p>
  <p class="pe-ex__rom">shukudai o shite kara, terebi o mimasu</p>
  <p class="pe-ex__uz">Uy vazifasini qilgandan keyin, televizor koʻraman.</p>
  <p class="pe-ex__why">から bu yerda PJ-24 dagi «…dan» (vaqt boshlanishi) ning oʻzi: «qilishdan <b>boshlab</b>». Yangi soʻz emas.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>から ni PJ-24 dagi から bilan bogʻlang.</b> U yerda
  <ruby>九時<rt>くじ</rt></ruby>から — «soat toʻqqizdan». Bu yerda
  してから — «qilgandan». Bitta qoʻshimcha, bitta maʼno: <em>boshlanish
  nuqtasi</em>. Faqat oldida ot emas, feʼl turibdi.</p>
</div>

<h3>2. 〜まえに — «…dan oldin»</h3>

<p>Mana darsning eng muhim qoidasi: まえに oldida <b>doim lugʻat shakli</b>
turadi. Gap oʻtgan zamonda boʻlsa ham.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Gap</th><th>まえに oldidagi shakl</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-uz">hozirgi</td><td class="pj-res"><ruby>寝<rt>ね</rt></ruby>るまえに<ruby>読<rt>よ</rt></ruby>みます</td>
      <td class="pj-uz">uxlashdan oldin oʻqiyman</td></tr>
  <tr><td class="pj-uz">oʻtgan</td><td class="pj-res"><ruby>寝<rt>ね</rt></ruby>るまえに<ruby>読<rt>よ</rt></ruby>みました</td>
      <td class="pj-uz">uxlashdan oldin oʻqidim</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Ikkala qatorda ham <ruby>寝<rt>ね</rt></ruby>る</b> —
  <ruby>寝<rt>ね</rt></ruby>た emas. Zamonni faqat <b>oxirgi</b> feʼl
  tashiydi; まえに oldidagi feʼl esa hech qachon oʻzgarmaydi. Bu — bu
  darsdagi eng koʻp uchraydigan xato.</p>
</div>

<h3>3. 〜たあとで — «…gandan keyin»</h3>

<p>Bu esa aksincha: あとで oldida <b>doim た-shakli</b> turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>朝<rt>あさ</rt></ruby>ごはんを<ruby>食<rt>た</rt></ruby>べたあとで、<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。</p>
  <p class="pe-ex__rom">asagohan o tabeta ato de, gakkō e ikimasu</p>
  <p class="pe-ex__uz">Nonushta qilgandan keyin, maktabga boraman.</p>
  <p class="pe-ex__why">Gap hozirgi zamonda, lekin あとで oldida baribir <b><ruby>食<rt>た</rt></ruby>べた</b> turibdi. Oʻzak qatʼiy.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">まえに</p>
    <p class="pj-big">lugʻat</p>
    <p><ruby>出<rt>で</rt></ruby>る<b>まえに</b><br>chiqishdan oldin</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">あとで</p>
    <p class="pj-big">た</p>
    <p><ruby>出<rt>で</rt></ruby>た<b>あとで</b><br>chiqqandan keyin</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Nega shunday? Mantiq bor.</b> «Chiqishdan oldin» deganda chiqish
  hali <em>boʻlmagan</em> — shuning uchun tugallanmagan, lugʻat shakli.
  «Chiqqandan keyin» deganda esa chiqish <em>boʻlib boʻlgan</em> — shuning
  uchun tugallangan, た-shakli. Oʻzbekchada ham xuddi shu farq bor:
  «chiq<b>ish</b>dan oldin» va «chiq<b>qan</b>dan keyin». Ikki tilda ham
  shakl <em>gapning</em> zamoniga emas, oʻsha ishning tugagan-tugamaganiga
  qarab tanlanadi.</p>
</div>

<h3>4. Ot bilan ishlatish</h3>

<p>Feʼl oʻrniga ot ham turishi mumkin — unda oraga <b>の</b> qoʻyiladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Ot bilan</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res"><ruby>食事<rt>しょくじ</rt></ruby>のまえに</td><td class="pj-uz">ovqatdan oldin</td></tr>
  <tr><td class="pj-res"><ruby>授業<rt>じゅぎょう</rt></ruby>のあとで</td><td class="pj-uz">darsdan keyin</td></tr>
  <tr><td class="pj-res"><ruby>三時<rt>さんじ</rt></ruby>のまえに</td><td class="pj-uz">soat uchdan oldin</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>の bu yerda ham oʻsha PJ-17 dagi の</b> — ikki otni bogʻlaydi.
  まえ va あと ning oʻzi ham ot (<em>old</em>, <em>keyin</em>), shuning
  uchun ular oldidagi otga の bilan ulanadi. Feʼl oldida esa の
  <b>qoʻyilmaydi</b>.</p>
</div>

<h3>5. てから va たあとで — farqi bormi</h3>

<p>Koʻp holatda ikkalasi ham toʻgʻri va maʼno deyarli bir xil. Farqi
nozik:</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Urgʻu</th></tr>
  <tr><td class="pj-end">〜てから</td><td class="pj-uz">Birinchi ish <b>tugashi shart</b> — keyin ikkinchisi</td></tr>
  <tr><td class="pj-end">〜たあとで</td><td class="pj-uz">Shunchaki <b>keyinroq</b> — tartib, shartsiz</td></tr>
</table></div>

<p>Yaʼni «qoʻlni yuvgandan keyin ovqatlanaman» degan gapda てから tabiiyroq
(yuvish <em>shart</em>), «darsdan keyin uyga boraman» da esa あとで
tabiiyroq. Boshlangʻich bosqichda ikkalasini ham toʻgʻri deb hisoblang.</p>

<h3>6. Uchtasi bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Oʻzak</th><th>Misol</th></tr>
  <tr><td class="pj-end">〜てから</td><td class="pj-stem">て-shakli</td>
      <td class="pj-res"><ruby>起<rt>お</rt></ruby>きてから</td></tr>
  <tr><td class="pj-end">〜まえに</td><td class="pj-stem">lugʻat shakli</td>
      <td class="pj-res"><ruby>起<rt>お</rt></ruby>きるまえに</td></tr>
  <tr><td class="pj-end">〜あとで</td><td class="pj-stem">た-shakli</td>
      <td class="pj-res"><ruby>起<rt>お</rt></ruby>きたあとで</td></tr>
</table></div>

<h3>7. Hammasi bir matnda</h3>

<p>Uchala qolipni bir kunlik tartibga tizib koʻring — aslida ular shu
uchun kerak.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>朝<rt>あさ</rt></ruby><ruby>起<rt>お</rt></ruby>きてから<ruby>顔<rt>かお</rt></ruby>を<ruby>洗<rt>あら</rt></ruby>います。<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>るまえに<ruby>宿題<rt>しゅくだい</rt></ruby>を<ruby>見<rt>み</rt></ruby>ます。<ruby>授業<rt>じゅぎょう</rt></ruby>のあとで<ruby>友<rt>とも</rt></ruby>だちに<ruby>会<rt>あ</rt></ruby>います。</p>
  <p class="pe-ex__rom">asa okite kara kao o araimasu. ie o deru mae ni shukudai o mimasu. jugyō no ato de tomodachi ni aimasu</p>
  <p class="pe-ex__uz">Ertalab turgandan keyin yuzimni yuvaman. Uydan chiqishdan oldin uy vazifasini koʻraman. Darsdan keyin doʻstlarim bilan uchrashaman.</p>
  <p class="pe-ex__why">Uch gap, uch qolip, uch xil oʻzak: <b><ruby>起<rt>お</rt></ruby>きて</b>から, <b><ruby>出<rt>で</rt></ruby>る</b>まえに, <b><ruby>授業<rt>じゅぎょう</rt></ruby>の</b>あとで.</p>
</div>

<p>Eʼtibor bering: uchala gap ham <em>hozirgi</em> zamonda, lekin
oʻzaklar har xil. Oʻzakni qolip tanlaydi, zamon emas — bugungi darsning
butun mazmuni shu bir jumlada.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>寝<rt>ね</rt></ruby>たまえに</p>
  <p class="pe-fix__good">✓ <ruby>寝<rt>ね</rt></ruby><b>る</b>まえに — まえに oldida doim <b>lugʻat shakli</b>, gap qaysi zamonda boʻlishidan qatʼi nazar.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>食<rt>た</rt></ruby>べるあとで</p>
  <p class="pe-fix__good">✓ <ruby>食<rt>た</rt></ruby><b>べた</b>あとで — あとで oldida doim <b>た-shakli</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>授業<rt>じゅぎょう</rt></ruby>あとで</p>
  <p class="pe-fix__good">✓ <ruby>授業<rt>じゅぎょう</rt></ruby><b>の</b>あとで — ot bilan ulanganda <b>の</b> kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Uxlashdan oldin kitob oʻqidim» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>寝<rt>ね</rt></ruby>るまえに<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みました。</b> まえに oldida lugʻat shakli qoladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Ovqatlangandan keyin» ni た-shakli bilan ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>食<rt>た</rt></ruby>べたあとで</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Darsdan keyin» — ot bilan qanday aytiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>授業<rt>じゅぎょう</rt></ruby>のあとで</b> — ot bilan <b>の</b> qoʻyiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Qaysi oʻzak gapning zamoniga qarab oʻzgaradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Hech qaysi.</b> Har uchala qolipning oʻzagi qatʼiy; zamonni faqat gapning oxirgi feʼli tashiydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. 〜てから va 〜たあとで farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>てから birinchi ish <b>tugashi shartligini</b> taʼkidlaydi; あとで esa shunchaki tartibni koʻrsatadi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜てから</b> — …gandan keyin (tugagach)</li>
  <li><b>〜まえに</b> — …dan oldin (lugʻat shakli!)</li>
  <li><b>〜たあとで</b> — …gandan keyin (た-shakli!)</li>
  <li><b><ruby>出<rt>で</rt></ruby>る</b> — chiqmoq (II guruh)</li>
  <li><b><ruby>食事<rt>しょくじ</rt></ruby></b> — ovqatlanish</li>
  <li><b><ruby>授業<rt>じゅぎょう</rt></ruby></b> — dars</li>
  <li><b><ruby>歩<rt>ある</rt></ruby>く</b> — yurmoq (I guruh)</li>
  <li><b>テレビ</b> — televizor</li>
  <li><b><ruby>手<rt>て</rt></ruby></b> — qoʻl</li>
  <li><b>それから</b> — keyin, undan soʻng</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>まえに → lugʻat shakli</b>, <b>あとで → た-shakli</b>. Qatʼiy.</li>
    <li>Zamonni faqat <b>oxirgi</b> feʼl tashiydi.</li>
    <li>Ot bilan ulanganda <b>の</b> qoʻyiladi, feʼl bilan — yoʻq.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-38: 〜ながら — bir vaqtda ikki ish",
        "category": "japanese",
        "order": 38,
        "summary": (
            "«…gan holda, …». Bu safar oʻzak — ます shaklining oʻzagi, va "
            "gapning asosiy ishi HAR DOIM ikkinchisi boʻladi."
        ),
        "stories": ["おんがくを ききながら"],
        "content": """
<h2>PJ-38: 〜ながら — bir vaqtda ikki ish</h2>

<p>Oʻtgan darsda ishlarni <em>ketma-ket</em> qoʻydingiz: avval biri, keyin
ikkinchisi. Bugun ularni <b>bir vaqtda</b> qoʻyasiz.</p>

<p>Va bu qolip yangi oʻzak talab qiladi — toʻrtinchisini. Yaxshi xabar
shuki, u ham sizda allaqachon bor: bu <b>ます shaklining oʻzagi</b>, yaʼni
ます ni olib tashlagandagi qism.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ます oʻzagini ajratasiz</li>
    <li>Ikki ishni bir vaqtda qoʻyasiz: 〜ながら</li>
    <li>Qaysi ish <em>asosiy</em> ekanini bilib olasiz</li>
    <li>Ikkala ishning egasi bitta boʻlishi kerakligini eslab qolasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">ます oʻzagi + ながら</span>
  <span class="pe-chip pe-chip--v"><ruby>聞<rt>き</rt></ruby>き</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">ながら</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o"><ruby>聞<rt>き</rt></ruby>きながら</span>
</div>

<h3>1. ます oʻzagi nima</h3>

<p>ます shaklini oling va <b>ます</b> ni olib tashlang. Qolgani — oʻzak.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>ます shakli</th><th>Oʻzak</th><th>ながら</th></tr>
  <tr><td><ruby>聞<rt>き</rt></ruby>きます</td><td class="pj-stem"><ruby>聞<rt>き</rt></ruby>き</td>
      <td class="pj-res"><ruby>聞<rt>き</rt></ruby>きながら</td></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べます</td><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べ</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べながら</td></tr>
  <tr><td><ruby>歩<rt>ある</rt></ruby>きます</td><td class="pj-stem"><ruby>歩<rt>ある</rt></ruby>き</td>
      <td class="pj-res"><ruby>歩<rt>ある</rt></ruby>きながら</td></tr>
  <tr><td>します</td><td class="pj-stem">し</td><td class="pj-res">しながら</td></tr>
  <tr><td><ruby>来<rt>き</rt></ruby>ます</td><td class="pj-stem"><ruby>来<rt>き</rt></ruby></td>
      <td class="pj-res"><ruby>来<rt>き</rt></ruby>ながら</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bu oʻzak sizga tanish.</b> PJ-27 da <ruby>読<rt>よ</rt></ruby>む dan
  <ruby>読<rt>よ</rt></ruby>み chiqqan edi — ます uchun. Oʻsha
  <ruby>読<rt>よ</rt></ruby>み bugun ながら oladi. Yaʼni yangi qoida emas:
  bir oʻzak, ikkinchi vazifa.</p>
</div>

<h3>2. Qolip</h3>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>音楽<rt>おんがく</rt></ruby></span>
  <span class="pj-joshi__p">を<small>TOʻLDIRUVCHI</small></span>
  <span class="pj-joshi__v"><ruby>聞<rt>き</rt></ruby>きながら</span>
  <span class="pj-joshi__v"><ruby>勉強<rt>べんきょう</rt></ruby>します</span>
  <span class="pj-joshi__uz">Musiqa tinglagan holda oʻqiyman.</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きながら<ruby>宿題<rt>しゅくだい</rt></ruby>をします。</p>
  <p class="pe-ex__rom">ongaku o kikinagara shukudai o shimasu</p>
  <p class="pe-ex__uz">Musiqa tinglab, uy vazifasi qilaman.</p>
  <p class="pe-ex__why">Ikkala ish bir vaqtda ketyapti. Zamonni oxirgi feʼl tashiydi — ながら hech qachon oʻzgarmaydi.</p>
</div>

<h3>3. Asosiy ish — ikkinchisi</h3>

<p>Mana darsning eng muhim qoidasi. ながら bilan belgilangan ish
<b>ikkinchi darajali</b>; gapning asl mazmuni — <em>oxirgi</em> feʼlda.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">OʻQIYAPMAN</p>
    <p><ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>します</p>
    <p>Asosiy ish — <b>oʻqish</b>. Musiqa fon.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">TINGLAYAPMAN</p>
    <p><ruby>勉強<rt>べんきょう</rt></ruby>しながら<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きます</p>
    <p>Asosiy ish — <b>tinglash</b>. Oʻqish fon.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu farq shu qadar aniq emas.</b> «Musiqa tinglab
  oʻqiyman» va «Oʻqib musiqa tinglayman» — ikkalasi ham gʻalati
  eshitilmaydi va koʻpincha bir xil tushuniladi. Yaponchada esa oxirgi
  feʼl <em>doim</em> asosiy ish, va buni oʻzgartirib boʻlmaydi. Shuning
  uchun tarjima qilayotganda oʻzingizdan soʻrang: <b>men aslida nima
  qilyapman?</b> Oʻsha feʼl gap oxiriga tushadi.</p>
</div>

<h3>4. Ega bitta boʻlishi kerak</h3>

<p>Ikkala ishni ham <b>bir odam</b> bajarishi shart. «Men oʻqiyapman,
singlim televizor koʻryapti» degan gapni ながら bilan tuzib boʻlmaydi —
u yerda ikki xil ega bor va gap maʼnosiz chiqadi.</p>

<div class="pe-call pe-warn">
  <p><b>Bu — ながら ning eng qatʼiy cheklovi.</b> Ikki egali gapni ulash
  uchun boshqa vositalar bor va ular keyingi darslarda keladi. ながら
  faqat <em>bitta odam bir vaqtda ikki ish</em> qilganda ishlaydi.</p>
</div>

<h3>5. Har ikki ish ham davomli boʻlishi kerak</h3>

<p>ながら bilan ulangan ishlar <b>vaqt oladigan</b> ishlar boʻlishi kerak:
yurish, tinglash, yeyish, gaplashish. Bir zumda tugaydigan ishlar
(kirmoq, boshlamoq) bu qolipga toʻgʻri kelmaydi.</p>

<p>Buni tekshirish oson: ishni «hozir qilyapman» deb ayta olasizmi?
<ruby>歩<rt>ある</rt></ruby>いています — ha, yurish davom etadi.
<ruby>入<rt>はい</rt></ruby>っています esa «kiryapman» emas, «kirgan
holatdaman» degani — demak kirish bir zumda tugagan. Shu sababli
«<ruby>入<rt>はい</rt></ruby>りながら» deb boʻlmaydi.</p>

<p>Yaʼni PJ-31 dagi ajratish — davomli ish va bir zumlik ish — bu yerda
yana ishga tushadi. Yapon grammatikasi shunday: bir marta oʻrganilgan
farq keyingi darslarda qayta-qayta chiqadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>歩<rt>ある</rt></ruby>きながら<ruby>話<rt>はな</rt></ruby>しました。</p>
  <p class="pe-ex__rom">arukinagara hanashimashita</p>
  <p class="pe-ex__uz">Yurgan holda gaplashdik.</p>
  <p class="pe-ex__why">Ikkalasi ham davomli ish. Zamonni <b><ruby>話<rt>はな</rt></ruby>しました</b> tashidi; ながら oʻzgarmadi.</p>
</div>

<h3>6. て bilan aralashtirmang</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pj-end">〜て</td><td class="pj-uz">avval biri, keyin ikkinchisi</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べて、<ruby>行<rt>い</rt></ruby>きます</td></tr>
  <tr><td class="pj-end">〜ながら</td><td class="pj-uz">ikkalasi bir vaqtda</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べながら<ruby>見<rt>み</rt></ruby>ます</td></tr>
</table></div>

<h3>7. Kundalik hayotda eng koʻp uchraydigan juftliklar</h3>

<p>Baʼzi ながら birikmalari shu qadar koʻp ishlatiladiki, ularni tayyor
ibora sifatida yodlash mumkin.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Ibora</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res"><ruby>歩<rt>ある</rt></ruby>きながら<ruby>話<rt>はな</rt></ruby>す</td><td class="pj-uz">yurgan holda gaplashmoq</td></tr>
  <tr><td class="pj-res"><ruby>食<rt>た</rt></ruby>べながらテレビを<ruby>見<rt>み</rt></ruby>る</td><td class="pj-uz">ovqatlanib televizor koʻrmoq</td></tr>
  <tr><td class="pj-res"><ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>する</td><td class="pj-uz">musiqa bilan oʻqimoq</td></tr>
  <tr><td class="pj-res"><ruby>働<rt>はたら</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>する</td><td class="pj-uz">ishlab, oʻqimoq</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Oxirgisiga alohida eʼtibor bering.</b>
  <ruby>働<rt>はたら</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>する
  — bu yerda «bir vaqtda» degani ayni daqiqa emas, <em>hayotning bir
  davri</em>: odam ishlaydi va shu bilan birga oʻqiydi. Yaponiyada bu juda
  keng tarqalgan holat va bu ibora ish suhbatlarida ham, tanishuvda ham
  tez-tez eshitiladi. Yaʼni ながら uzun muddatga ham yaraydi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>聞<rt>き</rt></ruby>くながら</p>
  <p class="pe-fix__good">✓ <ruby>聞<rt>き</rt></ruby><b>き</b>ながら — ながら <b>ます oʻzagiga</b> qoʻshiladi, lugʻat shakliga emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>聞<rt>き</rt></ruby>きながらました</p>
  <p class="pe-fix__good">✓ <ruby>聞<rt>き</rt></ruby>きながら…<b>ました</b> — ながら zamon olmaydi; u oxirgi feʼlda turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>が<ruby>読<rt>よ</rt></ruby>みながら<ruby>妹<rt>いもうと</rt></ruby>が<ruby>見<rt>み</rt></ruby>ます</p>
  <p class="pe-fix__good">✓ ながら bilan <b>ega bitta</b> boʻlishi shart. Ikki odam boʻlsa, bu qolip ishlamaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>歩<rt>ある</rt></ruby>く dan ながら yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>歩<rt>ある</rt></ruby>きながら</b> — ます oʻzagi <ruby>歩<rt>ある</rt></ruby>き.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Musiqa tinglab oʻqiyman» da asosiy ish qaysi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Oʻqish</b> — u gap oxirida turadi. Tinglash — fon.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. ながら oldida qaysi shakl turadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ます oʻzagi</b>: <ruby>食<rt>た</rt></ruby>べ, <ruby>聞<rt>き</rt></ruby>き, し.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. ながら ning eng qatʼiy cheklovi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Ega bitta boʻlishi kerak</b> — ikkala ishni ham bir odam bajarishi shart.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. 〜て va 〜ながら farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>〜て — <b>ketma-ket</b>, 〜ながら — <b>bir vaqtda</b>.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜ながら</b> — …gan holda, bir vaqtda</li>
  <li><b>ます oʻzagi</b> — ます siz qolgan qism</li>
  <li><b><ruby>歩<rt>ある</rt></ruby>きながら</b> — yurgan holda</li>
  <li><b><ruby>聞<rt>き</rt></ruby>きながら</b> — tinglagan holda</li>
  <li><b><ruby>働<rt>はたら</rt></ruby>く</b> — ishlamoq (I guruh)</li>
  <li><b><ruby>笑<rt>わら</rt></ruby>う</b> — kulmoq (I guruh)</li>
  <li><b><ruby>妹<rt>いもうと</rt></ruby></b> — singil</li>
  <li><b><ruby>兄<rt>あに</rt></ruby></b> — aka</li>
  <li><b>いつも</b> — doim, har doim</li>
  <li><b>アルバイト</b> — yarim kunlik ish</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>ます oʻzagi + ながら</b> — toʻrtinchi oʻzak, lekin tanish.</li>
    <li>Asosiy ish — <b>oxirgi</b> feʼl. ながら fon.</li>
    <li><b>Ega bitta</b>, va ikkala ish ham davomli boʻlishi kerak.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-39: Xohish — 〜たいです va 〜がほしいです",
        "category": "japanese",
        "order": 39,
        "summary": (
            "«Qilmoqchiman» va «kerak». Ikkalasi ham い-sifat boʻlib "
            "tuslanadi — yaʼni PJ-25 dagi qoida yana ishga tushadi — va "
            "ikkalasi ham が oladi."
        ),
        "stories": ["にほんへ いきたいです"],
        "content": """
<h2>PJ-39: Xohish — 〜たいです va 〜がほしいです</h2>

<p>Shu paytgacha siz nima qilayotganingizni, nima qilganingizni va nima
qilish shartligini ayta olardingiz. Bugun eng shaxsiy narsani aytasiz:
<b>nimani xohlaysiz</b>.</p>

<p>Ikkita qolip bor — biri <em>ish</em> uchun («bormoqchiman»), ikkinchisi
<em>narsa</em> uchun («velosiped kerak») — va ikkalasining ham kutilmagan
umumiy tomoni bor: ular <b>sifat</b> boʻlib tuslanadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>«…moqchiman» ni aytasiz: ます oʻzagi + たい</li>
    <li>«… kerak» ni aytasiz: ot + がほしい</li>
    <li>Ikkalasini い-sifat kabi tuslaysiz</li>
    <li>Nega boshqa odam haqida bunday aytilmasligini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikkalasi ham い-sifat</span>
  <span class="pe-chip pe-chip--v"><ruby>行<rt>い</rt></ruby>きたい</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">ほしい</span>
</div>

<h3>1. 〜たいです — «…moqchiman»</h3>

<p>Oʻzak — yana <b>ます oʻzagi</b>, oʻtgan darsdagining oʻzi. Unga
<b>たい</b> qoʻshiladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>ます shakli</th><th>Oʻzak</th><th>たい</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>行<rt>い</rt></ruby>きます</td><td class="pj-stem"><ruby>行<rt>い</rt></ruby>き</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>きたいです</td><td class="pj-uz">bormoqchiman</td></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べます</td><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べ</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べたいです</td><td class="pj-uz">yemoqchiman</td></tr>
  <tr><td><ruby>休<rt>やす</rt></ruby>みます</td><td class="pj-stem"><ruby>休<rt>やす</rt></ruby>み</td>
      <td class="pj-res"><ruby>休<rt>やす</rt></ruby>みたいです</td><td class="pj-uz">dam olmoqchiman</td></tr>
  <tr><td>します</td><td class="pj-stem">し</td>
      <td class="pj-res">したいです</td><td class="pj-uz">qilmoqchiman</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu «-moqchiman» qoʻshimchasi</b> — va u ham feʼlga
  yopishadi, alohida soʻz emas: «bor<b>moqchiman</b>»,
  <ruby>行<rt>い</rt></ruby>き<b>たいです</b>. Ikki tilda ham xohish
  feʼlning bir qismi boʻlib qoladi; rus yoki ingliz tilidagidek alohida
  «xohlayman» feʼli kerak emas. Bu — yana bir bevosita moslik.</p>
</div>

<h3>2. たい い-sifat kabi tuslanadi</h3>

<p>Mana kutilmagan qismi. <b>たい</b> い bilan tugaydi — va u haqiqiy
い-sifat kabi tuslanadi. Yaʼni PJ-25 dagi qoida bu yerda qayta
ishlaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Yaponcha</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>きたいです</td><td class="pj-uz">bormoqchiman</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>きたくないです</td><td class="pj-uz">bormoqchi emasman</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>きたかったです</td><td class="pj-uz">bormoqchi edim</td></tr>
  <tr><td class="pj-stem">oʻtgan inkor</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>きたくなかったです</td><td class="pj-uz">bormoqchi emas edim</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>い → くない, い → かった.</b> Bu aynan
  <ruby>安<rt>やす</rt></ruby>い → <ruby>安<rt>やす</rt></ruby>くない →
  <ruby>安<rt>やす</rt></ruby>かった bilan bir xil. Yangi qoida yodlash
  kerak emas — feʼl <em>sifatga</em> aylanib boʻlgan, keyingisi tanish.</p>
</div>

<h3>3. Toʻldiruvchi: を yoki が</h3>

<p>たい bilan toʻldiruvchi ikki xil belgilanishi mumkin, va ikkalasi ham
toʻgʻri.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">すし<b>が</b><ruby>食<rt>た</rt></ruby>べたいです。／ すし<b>を</b><ruby>食<rt>た</rt></ruby>べたいです。</p>
  <p class="pe-ex__rom">sushi ga tabetai desu / sushi o tabetai desu</p>
  <p class="pe-ex__uz">Sushi yemoqchiman.</p>
  <p class="pe-ex__why">が biroz anʼanaviyroq va xohishni kuchliroq koʻrsatadi; を kundalik nutqda koʻp eshitiladi. Boshlangʻich bosqichda <b>が</b> ni tanlang — u sifat mantiqiga mos.</p>
</div>

<h3>4. 〜がほしいです — «… kerak»</h3>

<p>Bu esa <b>narsa</b> uchun. Feʼl emas, <b>ot</b> qoʻyiladi va u
<b>が</b> oladi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n"><ruby>時間<rt>じかん</rt></ruby></span>
  <span class="pj-joshi__p">が<small>EGA</small></span>
  <span class="pj-joshi__v">ほしいです</span>
  <span class="pj-joshi__uz">Menga vaqt kerak.</span>
</div>

<div class="pe-call pe-tip">
  <p><b>ほしい ham い-sifat</b> — va bu safar rostakam sifat, hech qanday
  feʼl ichida emas. Shuning uchun u ham
  <ruby>好<rt>す</rt></ruby>き kabi <b>が</b> oladi: PJ-26 dagi
  «<ruby>音楽<rt>おんがく</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです»
  qolipining oʻzi.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Yaponcha</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-res"><ruby>自転車<rt>じてんしゃ</rt></ruby>がほしいです</td><td class="pj-uz">velosiped kerak</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-res"><ruby>自転車<rt>じてんしゃ</rt></ruby>はほしくないです</td><td class="pj-uz">velosiped kerak emas</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-res"><ruby>自転車<rt>じてんしゃ</rt></ruby>がほしかったです</td><td class="pj-uz">velosiped kerak edi</td></tr>
</table></div>

<h3>5. Ikkalasini ajratish</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">ISH — たい</p>
    <p class="pj-big">feʼl</p>
    <p><ruby>本<rt>ほん</rt></ruby>が<ruby>読<rt>よ</rt></ruby>み<b>たい</b>です<br>kitob oʻqimoqchiman</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">NARSA — ほしい</p>
    <p class="pj-big">ot</p>
    <p><ruby>本<rt>ほん</rt></ruby>が<b>ほしい</b>です<br>kitob kerak</p></div>
</div>

<h3>6. Muloyimlik: xohishni qanday aytish kerak</h3>

<p>Bitta amaliy ogohlantirish. 〜たいです — bu <em>oʻz</em> xohishingizni
tugʻridan-tugʻri aytish, va u baʼzan juda ochiq eshitiladi. Doʻstlar
orasida muammo yoʻq; lekin ustozdan yoki katta yoshli odamdan biror narsa
soʻraganda undan foydalanmang.</p>

<div class="pe-call pe-warn">
  <p><b>Masalan:</b> ustozga «<ruby>本<rt>ほん</rt></ruby>が
  <ruby>借<rt>か</rt></ruby>りたいです» («kitob olmoqchiman») deyish biroz
  qoʻpol chiqadi — bu oʻz xohishini roʻyxatga olib qoʻygandek. Toʻgʻri
  yoʻli — PJ-32 dagi qolip:
  «<ruby>本<rt>ほん</rt></ruby>を<ruby>借<rt>か</rt></ruby>りてもいいですか»
  yoki «<ruby>貸<rt>か</rt></ruby>してください». Yaʼni <b>xohish emas,
  ruxsat</b> soʻraladi.</p>
</div>

<p>Bu farq yapon tilida juda muhim: kimga gapirayotganingiz qaysi qolipni
tanlashingizni belgilaydi. Xuddi PJ-34 dagi «iltimos» va «qoida»
ajratimi kabi.</p>

<h3>7. Boshqa odam haqida aytilmaydi</h3>

<p>Mana bu qoida oʻzbek oʻquvchi uchun gʻalati tuyuladi, lekin u yapon
tilining muhim odatlaridan biri.</p>

<div class="pe-call pe-warn">
  <p><b>«<ruby>彼<rt>かれ</rt></ruby>は<ruby>行<rt>い</rt></ruby>きたいです»
  deyilmaydi.</b> Sababi mantiqiy: xohish — <em>ichki</em> tuygʻu, va
  yapon tilida boshqa odamning ichini bilib turgandek gapirish odobsizlik
  hisoblanadi. Siz faqat <b>oʻzingiz</b> haqingizda va <b>savol
  berganda</b> ishlata olasiz:
  <ruby>行<rt>い</rt></ruby>きたいですか — «bormoqchimisiz?». Boshqa odam
  haqida gapirish uchun alohida shakl bor va u keyinroq keladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">— <ruby>夏休<rt>なつやす</rt></ruby>みに<ruby>何<rt>なに</rt></ruby>がしたいですか。<br>— <ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きたいです。でもお<ruby>金<rt>かね</rt></ruby>がほしいです。</p>
  <p class="pe-ex__rom">natsuyasumi ni nani ga shitai desu ka / nihon e ikitai desu. demo okane ga hoshii desu</p>
  <p class="pe-ex__uz">— Yozgi taʼtilda nima qilmoqchisiz? — Yaponiyaga bormoqchiman. Lekin pul kerak.</p>
  <p class="pe-ex__why">Savol <b>ですか</b> bilan — bu ruxsat etilgan. Javobda ikkala qolip ham bor: ish uchun <b>たい</b>, narsa uchun <b>ほしい</b>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>くたいです</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby><b>き</b>たいです — たい <b>ます oʻzagiga</b> qoʻshiladi, lugʻat shakliga emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>きたいでした</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>きた<b>かった</b>です — たい い-sifat: zamonni <b>oʻzi</b> tashiydi, です emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>自転車<rt>じてんしゃ</rt></ruby>をほしいです</p>
  <p class="pe-fix__good">✓ <ruby>自転車<rt>じてんしゃ</rt></ruby><b>が</b>ほしいです — ほしい sifat, feʼl emas; を olmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>休<rt>やす</rt></ruby>む dan «dam olmoqchiman» ni yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>休<rt>やす</rt></ruby>みたいです</b> — ます oʻzagi <ruby>休<rt>やす</rt></ruby>み + たい.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Bormoqchi edim» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>行<rt>い</rt></ruby>きたかったです</b> — たい い-sifat, demak い → かった.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Velosiped kerak» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>自転車<rt>じてんしゃ</rt></ruby>がほしいです。</b> Ot + <b>が</b> + ほしい.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. たい va ほしい farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>たい — <b>ish</b> xohlanadi (feʼl bilan), ほしい — <b>narsa</b> xohlanadi (ot bilan).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega «<ruby>彼<rt>かれ</rt></ruby>は<ruby>行<rt>い</rt></ruby>きたいです» deyilmaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Xohish — <b>ichki tuygʻu</b>. Yapon tilida boshqa odamning ichini bilgandek gapirilmaydi. Savolda esa mumkin: 〜たいですか.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜たいです</b> — …moqchiman</li>
  <li><b>〜たくないです</b> — …moqchi emasman</li>
  <li><b>〜たかったです</b> — …moqchi edim</li>
  <li><b>ほしい</b> — kerak, xohlanadi (い-sifat)</li>
  <li><b><ruby>自転車<rt>じてんしゃ</rt></ruby></b> — velosiped</li>
  <li><b>お<ruby>金<rt>かね</rt></ruby></b> — pul</li>
  <li><b><ruby>夏休<rt>なつやす</rt></ruby>み</b> — yozgi taʼtil</li>
  <li><b><ruby>旅行<rt>りょこう</rt></ruby></b> — sayohat</li>
  <li><b><ruby>新<rt>あたら</rt></ruby>しい</b> — yangi</li>
  <li><b><ruby>彼<rt>かれ</rt></ruby></b> — u (erkak)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>ます oʻzagi + たい</b>, va natija — <b>い-sifat</b>.</li>
    <li><b>Ot + が + ほしい</b> — narsa uchun. を olmaydi.</li>
    <li>Faqat <b>oʻzingiz</b> haqingizda; boshqa odamga — savol shaklida.</li>
  </ul>
</div>
""",
    },
]
