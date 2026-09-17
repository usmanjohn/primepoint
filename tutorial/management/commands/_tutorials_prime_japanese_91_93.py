# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-91, PJ-92, PJ-93: urgʻu, moyillik va ikki xil sabab.

Blok F davom etadi.
    PJ-91 — さえ, こそ, しか〜ない: <ruby>取立助詞</ruby> oilasi.
            Bular yangi maʼno qoʻshmaydi — gapdagi bitta boʻlakni
            <b>ajratib koʻrsatadi</b>. Siz は va も ni allaqachon
            bilasiz; bu dars oʻsha qatorni yopadi.
    PJ-92 — がち, っぽい, 気味: uchala qolip ham «moyillik» degan
            bitta oilada, va uchalasi ham koʻpincha salbiy.
            Farqi — がち takrorni, っぽい koʻrinishni, 気味 esa
            ozgina darajani aytadi.
    PJ-93 — おかげで va せいで: bitta sabab, ikkita baho. Oʻzbekcha
            «tufayli» ikkalasini ham koʻtaradi, «dastidan» esa
            faqat ikkinchisini.

⚠️ PJ-91 ning eng katta tuzogʻi — **しか doim inkor bilan keladi**.
<ruby>千円</ruby>しかない («faqat ming iyena bor») — feʼl inkorda,
lekin oʻzbekcha tarjima tasdiq. Bu ikki tilning eng katta ohang
farqlaridan biri.

⚠️ PJ-92 da uchala qolip ham **ulanishi** bilan ajraladi:
がち va 気味 — ます-oʻzagi yoki ot; っぽい — ot, sifat oʻzagi yoki
ます-oʻzagi, va natija **い-sifat** boʻlib tuslanadi
(<ruby>子供</ruby>っぽ<b>かった</b>).

⚠️ PJ-93 da おかげで va せいで ikkalasi ham ot oldida **の** oladi.
Va せい ning oʻz feʼli bor: <ruby>人</ruby>のせいにする — «birovni
ayblamoq».

⚠️ Kursda hech qachon berilmagan shakllar bu batchda ham yoʻq:
意向形, 〜んです va uning yozma egizagi 〜のです.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_91_93.py --author=prime
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
        "title": "PJ-91: 〜さえ, 〜こそ, 〜しか〜ない — urgʻu qoʻshimchalari",
        "category": "japanese",
        "order": 91,
        "summary": (
            "Gapdagi bitta boʻlakni ajratib koʻrsatadigan qoʻshimchalar: "
            "さえ — «hatto … ham», こそ — «aynan shu», しか〜ない — "
            "«faqat …». Va nega しか har doim inkor bilan keladi."
        ),
        "stories": ["せんえんしか なかった"],
        "content": """
<h2>PJ-91: 〜さえ, 〜こそ, 〜しか〜ない — urgʻu qoʻshimchalari</h2>

<p>Bitta gap, toʻrt xil qoʻshimcha, toʻrt xil maʼno:</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h">は</p>
    <p><ruby>私<rt>わたし</rt></ruby><b>は</b><ruby>知<rt>し</rt></ruby>っている。</p>
    <p>Men bilaman. (boshqalar haqida gapirmadim)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">も</p>
    <p><ruby>私<rt>わたし</rt></ruby><b>も</b><ruby>知<rt>し</rt></ruby>っている。</p>
    <p>Men ham bilaman. (boshqalar ham biladi)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">さえ</p>
    <p><ruby>子供<rt>こども</rt></ruby><b>さえ</b><ruby>知<rt>し</rt></ruby>っている。</p>
    <p>Hatto bola ham biladi. (bu — eng kutilmagan misol)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">こそ</p>
    <p><ruby>私<rt>わたし</rt></ruby><b>こそ</b><ruby>知<rt>し</rt></ruby>っている。</p>
    <p>Aynan men bilaman. (boshqalar emas, men)</p>
  </div>
</div>

<p>Bu qoʻshimchalarning hech biri gapga yangi maʼno qoʻshmaydi.
Ular faqat <b>bitta boʻlakni ajratib koʻrsatadi</b> va qolganini
soyaga qoldiradi. Yaponchada bu oila
<ruby>取立助詞<rt>とりたてじょし</rt></ruby> deyiladi —
«ajratib koʻrsatuvchi qoʻshimchalar».</p>

<p>Siz <b>は</b> va <b>も</b> ni PJ-14 va PJ-19 dan beri
bilasiz. Bu dars oʻsha qatorni yopadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>〜さえ</b> bilan «hatto … ham» deysiz</li>
    <li><b>〜さえ〜ば</b> bilan «faqat … boʻlsa bas» deysiz</li>
    <li><b>〜こそ</b> bilan bir boʻlakni qatʼiy ajratasiz</li>
    <li><b>〜しか〜ない</b> ni toʻgʻri, inkor bilan yasaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Faqat va yetarli emas</span>
  <span class="pe-chip pe-chip--o">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">しか</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--neg">feʼl INKORDA</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">faqat …</span>
</div>

<h3>1. 〜さえ — «hatto … ham»</h3>

<p>さえ eng kutilmagan misolni koʻrsatadi: <em>«bunisi ham
shunday boʻlsa, qolganlari haqida gapirmasa ham boʻladi»</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s"><ruby>子供<rt>こども</rt></ruby>さえ</span><ruby>知<rt>し</rt></ruby>っていることだ。</p>
  <p class="pe-ex__uz">Buni hatto bola ham biladi.</p>
  <p class="pe-ex__why">«Bola» — bilishi eng kam kutiladigan odam. Shuni aytish orqali «demak hamma biladi» degan xulosa chiqadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>忙<rt>いそが</rt></ruby>しくて、<span class="pe-hl pe-hl--neg">ごはんを<ruby>食<rt>た</rt></ruby>べる<ruby>時間<rt>じかん</rt></ruby>さえない</span>。</p>
  <p class="pe-ex__uz">Shu qadar bandmanki, hatto ovqatlanishga ham vaqt yoʻq.</p>
  <p class="pe-ex__why">さえ inkor bilan ayniqsa kuchli chiqadi: «eng zarur narsa ham yoʻq» degani.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «hatto … ham» — bu qolipning aniq jufti, va
  u ham ikki soʻzdan iborat.</b> Diqqat qiling: biz
  «<em>hatto</em> bola <em>ham</em> biladi» deymiz — oldida bitta
  soʻz, orqasida bitta qoʻshimcha. Yaponchada esa ikkovining
  ishini bitta <b>さえ</b> bajaradi va u otdan <em>keyin</em>
  turadi. Shuning uchun tarjima qilayotganda «hatto» ni
  qidirmang: oʻzbekcha gapda «hatto» qaysi soʻzga tegib
  turgan boʻlsa, さえ ni oʻsha soʻzdan keyin qoʻying. Aksi ham
  ishlaydi — matnda さえ ni koʻrsangiz, oldingi soʻzning
  oldiga «hatto» ni qoʻyib oʻqing.</p>
</div>

<h3>2. 〜さえ〜ば — «faqat … boʻlsa, bas»</h3>

<p>さえ ning ikkinchi ishi PJ-51 dagi <b>ば</b> bilan
juftlashadi va butunlay boshqa maʼno beradi: <b>bitta shart
yetarli</b>.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>薬<rt>くすり</rt></ruby></span>
  <span class="pj-joshi__p">さえ<small>YETARLI SHART</small></span>
  <span class="pj-joshi__n"><ruby>飲<rt>の</rt></ruby>めば</span>
  <span class="pj-joshi__v"><ruby>治<rt>なお</rt></ruby>ります</span>
  <span class="pj-joshi__uz">Faqat dorini ichsangiz bas, tuzalasiz.</span>
</div>

<div class="pe-call pe-rule">
  <p><b>Ikki maʼnoni ajratish oson.</b> Gapda <b>ば</b> bormi?
  Bor boʻlsa — «faqat … boʻlsa bas». Yoʻq boʻlsa — «hatto … ham».
  Uchinchi variant yoʻq, shuning uchun bu qolip imtihonda
  qulay: koʻzingiz avval gapning oxiriga tushsin.</p>
</div>

<h3>3. 〜こそ — «aynan shu»</h3>

<p>こそ boʻlakni qatʼiy ajratadi va koʻpincha
<em>boshqasini rad etadi</em>: «boshqasi emas, mana shunisi».</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s"><ruby>今<rt>いま</rt></ruby>こそ</span><ruby>始<rt>はじ</rt></ruby>める<ruby>時<rt>とき</rt></ruby>だ。</p>
  <p class="pe-ex__uz">Aynan hozir boshlash vaqti.</p>
  <p class="pe-ex__why">«Kecha emas, ertaga emas — hozir». こそ shu rad etishni ichiga yashirgan.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>こそ ni oʻzbekchada bitta soʻz emas, urgʻu koʻtaradi.</b>
  «<em>Aynan</em> hozir», «<em>mana shu</em> kitob», «men-<em>ku</em>
  bilaman» — uchalasida ham boshqa variantlar rad etilyapti.
  Lekin eʼtibor bering: oʻzbekchada biz koʻpincha hech qanday
  soʻz qoʻshmaymiz, shunchaki <em>ovozimizni koʻtaramiz</em> —
  «HOZIR boshlash kerak». Yapon tilida ovoz bilan urgʻu berish
  odat emas, shuning uchun uning oʻrniga grammatik belgi
  turibdi. Demak こそ ni koʻrganingizda uni tarjima qilishga
  urinmang — oʻsha soʻzni <em>baland ovozda</em> oʻqing,
  maʼno oʻzi chiqadi. Bu butun
  <ruby>取立助詞<rt>とりたてじょし</rt></ruby> oilasi uchun
  toʻgʻri: ular yozuvdagi urgʻu belgilari.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Ikkita tayyor iborani yodlab qoʻying.</b>
  <b>こちらこそ</b> — «asosiy men minnatdorman», rahmatga javob.
  <b>〜からこそ</b> — «aynan shuning uchun»:
  <ruby>難<rt>むずか</rt></ruby>しいからこそ、おもしろい
  («aynan qiyin boʻlgani uchun qiziq»). Ikkalasi ham kundalik
  nutqda juda koʻp.</p>
</div>

<h3>4. 〜しか〜ない — «faqat …»</h3>

<p>Bu darsning eng muhim yarmi. しか «faqat» degani, lekin u
<b>yolgʻiz turolmaydi</b>: gapning feʼli albatta inkorda
boʻlishi shart.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>財布<rt>さいふ</rt></ruby>に<span class="pe-hl pe-hl--neg"><ruby>千円<rt>せんえん</rt></ruby>しかない</span>。</p>
  <p class="pe-ex__uz">Hamyonda faqat ming iyena bor.</p>
  <p class="pe-ex__why">Yaponcha feʼl <b>inkorda</b> (ない), oʻzbekcha tarjima esa <b>tasdiqda</b> («bor»). Bu farqni koʻrish shart.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Bu darsning eng koʻp uchraydigan xatosi.</b>
  «<ruby>千円<rt>せんえん</rt></ruby>しかある» degan gap yoʻq —
  しか qoʻyilgan gapda feʼl inkorda boʻlishi <em>shart</em>.
  Sababi mantiqiy: しか «bundan boshqa yoʻq» deb aytadi, va
  «yoʻq» degani inkor. Oʻzbekchada ham aslida shunday —
  «ming iyena<em>dan boshqa hech narsa yoʻq</em>». Biz uni
  qisqartirib «faqat ming iyena bor» deymiz, va shu
  qisqartma bizni adashtiradi.</p>
</div>

<h3>5. しか〜ない va だけ</h3>

<p>PJ-83 da <b>だけ</b> ni koʻrgansiz. Ikkalasi ham «faqat» deb
tarjima qilinadi, lekin ohangi boshqa.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">だけ — quruq chegara</p>
    <p><ruby>千円<rt>せんえん</rt></ruby>だけあります。</p>
    <p>Ming iyena bor. Fakt, bahosiz — balki yetarlidir.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">しか〜ない — kam, yetmaydi</p>
    <p><ruby>千円<rt>せんえん</rt></ruby>しかありません。</p>
    <p>Atigi ming iyena. Gapiruvchi buni <b>kam</b> deb
    hisoblaydi.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu farqni «atigi» va «bor-yoʻgʻi» soʻzlari
  koʻtaradi.</b> «Ming soʻm bor» — quruq xabar, <b>だけ</b>.
  «<em>Atigi</em> ming soʻm bor», «<em>bor-yoʻgʻi</em> ming
  soʻm» — bu yerda norozilik va kamlik bor, va aynan shu
  <b>しか〜ない</b>. Ikkovini ajratish uchun oʻzingizdan
  soʻrang: <em>«gapiruvchi bundan xursandmi?»</em> Xursand
  yoki befarq boʻlsa — だけ. Kam deb hisoblasa — しか〜ない.
  Shuning uchun «<ruby>一人<rt>ひとり</rt></ruby>だけ
  <ruby>来<rt>き</rt></ruby>た» va
  «<ruby>一人<rt>ひとり</rt></ruby>しか<ruby>来<rt>こ</rt></ruby>なかった»
  bir voqeani aytadi, lekin ikki xil kayfiyat bilan.</p>
</div>

<h3>6. Qoʻshimchaga nima boʻladi</h3>

<p>Uchala qolip ham <b>が</b> va <b>を</b> ni siqib chiqaradi —
bu PJ-83 dagi ばかり bilan bir xil qoida. Qolgan qoʻshimchalar
esa joyida qoladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Asl gap</th><th>Natija</th><th>Izoh</th></tr>
  <tr><td class="pj-stem"><ruby>子供<rt>こども</rt></ruby>が<ruby>知<rt>し</rt></ruby>っている</td>
      <td class="pj-res"><ruby>子供<rt>こども</rt></ruby>さえ<ruby>知<rt>し</rt></ruby>っている</td>
      <td class="pj-uz">が tushdi</td></tr>
  <tr><td class="pj-stem"><ruby>水<rt>みず</rt></ruby>を<ruby>飲<rt>の</rt></ruby>む</td>
      <td class="pj-res"><ruby>水<rt>みず</rt></ruby>しか<ruby>飲<rt>の</rt></ruby>まない</td>
      <td class="pj-uz">を tushdi</td></tr>
  <tr><td class="pj-stem"><ruby>東京<rt>とうきょう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>く</td>
      <td class="pj-res"><ruby>東京<rt>とうきょう</rt></ruby>へしか<ruby>行<rt>い</rt></ruby>かない</td>
      <td class="pj-uz">へ qoldi, しか undan keyin</td></tr>
  <tr><td class="pj-stem"><ruby>友<rt>とも</rt></ruby>だちと<ruby>話<rt>はな</rt></ruby>す</td>
      <td class="pj-res"><ruby>友<rt>とも</rt></ruby>だちとしか<ruby>話<rt>はな</rt></ruby>さない</td>
      <td class="pj-uz">と qoldi</td></tr>
</table></div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">財</span>
    <span class="pj-kanji__uz">boylik, mol-mulk</span>
    <span class="pj-kanji__on">オン: ザイ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">財布 (さいふ) — hamyon · 財産 (ざいさん) — mulk</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">薬</span>
    <span class="pj-kanji__uz">dori</span>
    <span class="pj-kanji__on">オン: ヤク</span>
    <span class="pj-kanji__kun">KUN: くすり</span>
    <span class="pj-kanji__note">薬局 (やっきょく) — dorixona · 薬を飲む — dori ichmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">治</span>
    <span class="pj-kanji__uz">tuzalmoq, davolamoq</span>
    <span class="pj-kanji__on">オン: ジ・チ</span>
    <span class="pj-kanji__kun">KUN: なお(る)・なお(す)</span>
    <span class="pj-kanji__note">治る — tuzalmoq · 政治 (せいじ) — siyosat</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>千円<rt>せんえん</rt></ruby>しかあります</p>
  <p class="pe-fix__good">✓ <ruby>千円<rt>せんえん</rt></ruby>しか<b>ありません</b> — しか qoʻyilsa, feʼl albatta inkorda.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>水<rt>みず</rt></ruby><b>を</b>しか<ruby>飲<rt>の</rt></ruby>まない</p>
  <p class="pe-fix__good">✓ <ruby>水<rt>みず</rt></ruby>しか<ruby>飲<rt>の</rt></ruby>まない — しか を va が ni siqib chiqaradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>薬<rt>くすり</rt></ruby>さえ<ruby>飲<rt>の</rt></ruby>むと<ruby>治<rt>なお</rt></ruby>ります</p>
  <p class="pe-fix__good">✓ <ruby>薬<rt>くすり</rt></ruby>さえ<ruby>飲<rt>の</rt></ruby><b>めば</b> — «faqat … boʻlsa bas» maʼnosi さえ va <b>ば</b> juftligidan chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby><b>が</b>こそ<ruby>知<rt>し</rt></ruby>っている</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby>こそ — こそ ham が ni siqib chiqaradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>一人<rt>ひとり</rt></ruby>しか<ruby>来<rt>き</rt></ruby>ました</p>
  <p class="pe-fix__good">✓ <ruby>一人<rt>ひとり</rt></ruby>しか<ruby>来<rt>こ</rt></ruby><b>ませんでした</b> — oʻtgan zamonda ham inkor shart.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Hamyonda faqat ming iyena bor» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>財布<rt>さいふ</rt></ruby>に<ruby>千円<rt>せんえん</rt></ruby>しかありません</b>. Oʻzbekcha «bor», yaponcha esa <b>ありません</b> — しか har doim inkorni talab qiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>薬<rt>くすり</rt></ruby>さえ___<ruby>治<rt>なお</rt></ruby>ります — boʻsh joyga nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>飲<rt>の</rt></ruby>めば</b>. さえ va <b>ば</b> birga kelsa, maʼno «faqat … boʻlsa bas» ga oʻzgaradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Hatto bola ham biladi» — さえ yoki こそ?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>さえ</b>: <ruby>子供<rt>こども</rt></ruby>さえ<ruby>知<rt>し</rt></ruby>っている. Bola — eng kutilmagan misol. こそ boʻlsa, «aynan bola biladi» degan boshqa gap chiqardi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>千円<rt>せんえん</rt></ruby>だけあります va <ruby>千円<rt>せんえん</rt></ruby>しかありません — farqi nimada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Kayfiyat.</b> だけ — quruq xabar, «ming iyena bor». しか〜ない — «atigi ming iyena», gapiruvchi buni kam deb hisoblaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>水<rt>みず</rt></ruby>を<ruby>飲<rt>の</rt></ruby>む gapiga しか qoʻshing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>水<rt>みず</rt></ruby>しか<ruby>飲<rt>の</rt></ruby>まない</b>. <b>を</b> tushib qoladi, feʼl esa inkorga oʻtadi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜さえ</b> — hatto … ham</li>
  <li><b>〜さえ〜ば</b> — faqat … boʻlsa bas</li>
  <li><b>〜こそ</b> — aynan shu</li>
  <li><b>〜からこそ</b> — aynan shuning uchun</li>
  <li><b>〜しか〜ない</b> — faqat … (atigi)</li>
  <li><b>こちらこそ</b> — asosiy men minnatdorman</li>
  <li><b><ruby>財布<rt>さいふ</rt></ruby></b> — hamyon</li>
  <li><b><ruby>薬<rt>くすり</rt></ruby></b> — dori</li>
  <li><b><ruby>治<rt>なお</rt></ruby>る</b> — tuzalmoq</li>
  <li><b><ruby>忙<rt>いそが</rt></ruby>しい</b> — band</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>しか</b> qoʻyilgan gapda feʼl <b>albatta inkorda</b>.</li>
    <li><b>さえ</b> + <b>ば</b> = «faqat … boʻlsa bas»; ば siz = «hatto … ham».</li>
    <li>Uchalasi ham <b>が</b> va <b>を</b> ni siqib chiqaradi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-92: 〜がち, 〜っぽい, 〜気味 — moyillik",
        "category": "japanese",
        "order": 92,
        "summary": (
            "Uchta qolip, bitta oila: «moyillik». がち — tez-tez shunday "
            "boʻladi; っぽい — shunga oʻxshaydi; 気味 — bir oz shunday. "
            "Uchalasi ham koʻpincha salbiy baho bilan keladi."
        ),
        "stories": ["あきは かぜぎみ"],
        "content": """
<h2>PJ-92: 〜がち, 〜っぽい, 〜<ruby>気味<rt>ぎみ</rt></ruby> — moyillik</h2>

<p>Uch gap, uch qolip, bitta odam haqida:</p>

<p>ラノさんは<ruby>忘<rt>わす</rt></ruby>れ<b>がち</b>だ。</p>

<p>ラノさんは<ruby>忘<rt>わす</rt></ruby>れ<b>っぽい</b>。</p>

<p>ラノさんは<ruby>疲<rt>つか</rt></ruby>れ<b><ruby>気味<rt>ぎみ</rt></ruby></b>だ。</p>

<p>Uchalasi ham «u bunday <em>boʻlib turadi</em>» degan
maʼnoni beradi — lekin har biri boshqa tomondan. Birinchisi
<b>chastota</b> haqida: tez-tez unutadi. Ikkinchisi
<b>xususiyat</b> haqida: u unutuvchan odam. Uchinchisi
<b>daraja</b> haqida: hozir bir oz charchagan.</p>

<p>Bu oila yapon tilida juda koʻp ishlatiladi, chunki u
<em>qatʼiy</em> gapirmaslikka imkon beradi — «kasal» emas,
«bir oz shamollagan».</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>〜がち</b> bilan «tez-tez shunday boʻladi» deysiz</li>
    <li><b>〜っぽい</b> bilan «… simon, … ga oʻxshagan» deysiz</li>
    <li><b>〜<ruby>気味<rt>ぎみ</rt></ruby></b> bilan «bir oz …» deysiz</li>
    <li>uchalasining ulanishini adashtirmaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Moyillik</span>
  <span class="pe-chip pe-chip--v">ます-oʻzagi</span>
  <span class="pe-op">yoki</span>
  <span class="pe-chip pe-chip--o">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">がち · <ruby>気味<rt>ぎみ</rt></ruby></span>
</div>

<h3>1. 〜がち — «tez-tez shunday boʻladi»</h3>

<p>がち <b>chastota</b>ni aytadi: bu hodisa koʻp takrorlanadi.
Ohangi deyarli doim salbiy — odatda yaxshi boʻlmagan narsa
takrorlanadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>電車<rt>でんしゃ</rt></ruby>は<span class="pe-hl pe-hl--v"><ruby>遅<rt>おく</rt></ruby>れがち</span>だ。</p>
  <p class="pe-ex__uz">Bu poyezd tez-tez kechikib qoladi.</p>
  <p class="pe-ex__why">Har safar emas, lekin koʻp. がち aynan shu «koʻpincha» degan maʼnoni beradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>冬<rt>ふゆ</rt></ruby>は<span class="pe-hl pe-hl--v"><ruby>曇<rt>くも</rt></ruby>りがち</span>の<ruby>日<rt>ひ</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い。</p>
  <p class="pe-ex__uz">Qishda bulutli kunlar koʻp boʻladi.</p>
  <p class="pe-ex__why">Otdan keyin ham ulanadi. Ot oldida <b>の</b> qoʻshiladi: <ruby>曇<rt>くも</rt></ruby>りがちの<ruby>日<rt>ひ</rt></ruby>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada がち ni «-ib qoladi» va «tez-tez» koʻtaradi.</b>
  «Kechik<em>ib qoladi</em>», «unut<em>ib qoladi</em>»,
  «kasal bo<em>lib turadi</em>» — bu iboralarning hammasida
  ish <em>bir marta</em> emas, <em>qayta-qayta</em> boʻlgani
  aytilyapti, va ularning ohangi ham yoqimsiz. Yaponcha
  <b>がち</b> aynan shu ikki narsani birga olib yuradi:
  takror va norozilik. Shuning uchun uni «har doim» deb
  tarjima qilmang — «har doim» qatʼiy, がち esa
  «koʻpincha, lekin har safar emas». Oʻzbekcha
  «-ib qoladi» ham aynan shunday yumshoq: «poyezd
  kechikib qoladi» degan gap poyezd <em>har kuni</em>
  kechikadi degani emas.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Ikkita tayyor birikma bor.</b>
  <b><ruby>病気<rt>びょうき</rt></ruby>がち</b> — «tez-tez
  kasal boʻladigan» (otdan), va
  <b><ruby>遠慮<rt>えんりょ</rt></ruby>がち</b> — «tortinchoq,
  ehtiyot bilan». Ikkalasi ham lugʻatda alohida soʻz sifatida
  turadi.</p>
</div>

<h3>2. 〜っぽい — «… simon»</h3>

<p>っぽい <b>koʻrinish</b> yoki <b>xususiyat</b> haqida:
«shunga oʻxshaydi», «shunday sifati bor». U eng
<em>soʻzlashuv</em> qolipi, va natija <b>い-sifat</b> boʻlib
tuslanadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oldida nima</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-res"><ruby>子供<rt>こども</rt></ruby>っぽい</td>
      <td class="pj-uz">bolalarcha</td></tr>
  <tr><td class="pj-stem">rang</td><td class="pj-res"><ruby>白<rt>しろ</rt></ruby>っぽい</td>
      <td class="pj-uz">oqishroq</td></tr>
  <tr><td class="pj-stem">ます-oʻzagi</td><td class="pj-res"><ruby>忘<rt>わす</rt></ruby>れっぽい</td>
      <td class="pj-uz">unutuvchan</td></tr>
  <tr><td class="pj-stem">ます-oʻzagi</td><td class="pj-res"><ruby>怒<rt>おこ</rt></ruby>りっぽい</td>
      <td class="pj-uz">jizzaki</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>っぽい い-sifat boʻlib tuslanadi.</b> Shuning uchun
  uning oʻtgan zamoni <b>っぽかった</b>, inkori esa
  <b>っぽくない</b>:
  <ruby>子供<rt>こども</rt></ruby>っぽかった
  («bolalarcha edi»). «っぽいでした» degan gap notoʻgʻri —
  bu PJ-25 dagi い-sifat qoidasining oʻzi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">その<ruby>言<rt>い</rt></ruby>い<ruby>方<rt>かた</rt></ruby>は<span class="pe-hl pe-hl--adv"><ruby>子供<rt>こども</rt></ruby>っぽい</span>ですよ。</p>
  <p class="pe-ex__uz">Bunday gapirish bolalarcha boʻlib qoladi.</p>
  <p class="pe-ex__why">Gapiruvchi bola emas — u faqat <em>bolaga oʻxshab</em> gapiryapti. Bu PJ-88 dagi として ning teskarisi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada «-simon» va «-cha» shu ishni qiladi.</b>
  «Bola<em>cha</em>», «tuxum<em>simon</em>», «oq<em>ish</em>» —
  uchala qoʻshimcha ham bitta narsani aytadi: <em>aynan u emas,
  lekin unga tortadi</em>. Yaponcha <b>っぽい</b> ham shunday,
  va u ayniqsa rangda qulay:
  <ruby>白<rt>しろ</rt></ruby>っぽい — «oqishroq»,
  <ruby>赤<rt>あか</rt></ruby>っぽい — «qizgʻishroq». Bir narsaga
  eʼtibor bering: oʻzbekchada bu qoʻshimchalar soʻzning
  <em>ichiga</em> kiradi va yangi soʻz yasaydi, yaponchada esa
  っぽい tashqaridan yopishadi va istalgan otga ulanaveradi.
  Shuning uchun lugʻatda yoʻq birikmani ham bemalol yasashingiz
  mumkin — yaponlar kundalik nutqda aynan shunday qiladi.</p>
</div>

<h3>3. 〜<ruby>気味<rt>ぎみ</rt></ruby> — «bir oz …»</h3>

<p><ruby>気味<rt>ぎみ</rt></ruby> <b>daraja</b> haqida:
holat bor, lekin kuchli emas. Koʻpincha gapiruvchining oʻz
ahvoli haqida ishlatiladi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>今日<rt>きょう</rt></ruby></span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n"><ruby>風邪<rt>かぜ</rt></ruby><ruby>気味<rt>ぎみ</rt></ruby></span>
  <span class="pj-joshi__v">です</span>
  <span class="pj-joshi__uz">Bugun bir oz shamollaganman.</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>最近<rt>さいきん</rt></ruby><span class="pe-hl pe-hl--adv"><ruby>太<rt>ふと</rt></ruby>り<ruby>気味<rt>ぎみ</rt></ruby></span>なので、<ruby>歩<rt>ある</rt></ruby>くようにしています。</p>
  <p class="pe-ex__uz">Soʻnggi paytda biroz semirib ketdim, shuning uchun koʻproq yurishga harakat qilyapman.</p>
  <p class="pe-ex__why">«Semirdim» deyish qoʻpol. <ruby>気味<rt>ぎみ</rt></ruby> gapni yumshatadi — bu uning asosiy ishi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu yumshatishni «-roq» va «bir oz»
  qiladi.</b> «Charchag<em>anroq</em>man», «<em>bir oz</em>
  shamollabman», «<em>biroz</em> kech qoldik» — uchalasida
  ham holat bor, lekin biz uni ataylab kuchsizlantiryapmiz.
  Yaponcha <b><ruby>気味<rt>ぎみ</rt></ruby></b> aynan shu
  ishni qiladi, va yapon madaniyatida bu juda muhim: oʻzing
  haqingda qatʼiy gapirish — koʻtarinki, boshqa odam
  haqida qatʼiy gapirish esa qoʻpol. Shuning uchun
  <ruby>気味<rt>ぎみ</rt></ruby> ni «kerak boʻlmagan
  qoʻshimcha» deb tashlab ketmang — u gapning odobini
  koʻtarib turgan boʻlak.</p>
</div>

<h3>4. Uchalasi bitta jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Nima haqida</th><th>Ulanishi</th><th>Natija</th></tr>
  <tr><td class="pj-stem">〜がち</td><td class="pj-uz">chastota — tez-tez</td>
      <td class="pj-end">ます-oʻzagi / ot</td>
      <td class="pj-res">な-sifat</td></tr>
  <tr><td class="pj-stem">〜っぽい</td><td class="pj-uz">xususiyat — oʻxshash</td>
      <td class="pj-end">ot / sifat oʻzagi / ます-oʻzagi</td>
      <td class="pj-res">い-sifat</td></tr>
  <tr><td class="pj-stem">〜<ruby>気味<rt>ぎみ</rt></ruby></td><td class="pj-uz">daraja — bir oz</td>
      <td class="pj-end">ます-oʻzagi / ot</td>
      <td class="pj-res">な-sifat</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bitta soʻz, uchala qolip.</b>
  <ruby>忘<rt>わす</rt></ruby>れ<b>がち</b> — «tez-tez unutadi»
  (bu safar ham unutdi). <ruby>忘<rt>わす</rt></ruby>れ<b>っぽい</b>
  — «unutuvchan» (uning tabiati shunday).
  Uchinchisi bu feʼl bilan ishlamaydi, chunki
  <ruby>気味<rt>ぎみ</rt></ruby> <em>holat</em> talab qiladi,
  takrorlanadigan harakatni emas.</p>
</div>

<h3>5. Nega uchalasi ham salbiy</h3>

<p>Bu oilaning qiziq tomoni shu: uchala qolip ham deyarli
<b>faqat yoqimsiz narsalar</b> bilan keladi. «Tez-tez
kechikadi», «tez-tez kasal boʻladi», «bolalarcha»,
«jizzaki», «bir oz charchagan» — hammasi shikoyat yoki
uzr.</p>

<div class="pe-call pe-warn">
  <p><b>Shuning uchun ularni maqtovda ishlatmang.</b>
  «<ruby>元気<rt>げんき</rt></ruby>がち» yoki
  «<ruby>上手<rt>じょうず</rt></ruby>っぽい» degan gaplar
  gʻalati eshitiladi — birinchisi umuman yoʻq, ikkinchisi esa
  «yaxshi bajarayotgandek koʻrinadi, lekin aslida yoʻq»
  degan kinoya boʻlib chiqadi. Maqtov uchun PJ-73 dagi
  <b>〜そうです</b> yoki PJ-75 dagi <b>〜ようです</b> bor.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">気</span>
    <span class="pj-kanji__uz">ruh, kayfiyat, havo</span>
    <span class="pj-kanji__on">オン: キ・ケ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">気味 (ぎみ) — bir oz · 天気 (てんき) — ob-havo · 元気 (げんき) — sogʻlom</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">邪</span>
    <span class="pj-kanji__uz">yovuz, notoʻgʻri</span>
    <span class="pj-kanji__on">オン: ジャ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">風邪 (かぜ) — shamollash · 邪魔 (じゃま) — xalaqit</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">曇</span>
    <span class="pj-kanji__uz">bulutli boʻlmoq</span>
    <span class="pj-kanji__on">オン: ドン</span>
    <span class="pj-kanji__kun">KUN: くも(る)</span>
    <span class="pj-kanji__note">曇り (くもり) — bulutli · 曇りがち — koʻpincha bulutli</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>忘<rt>わす</rt></ruby>れるがち</p>
  <p class="pe-fix__good">✓ <ruby>忘<rt>わす</rt></ruby>れがち — がち ます-oʻzagiga ulanadi, lugʻat shakliga emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>子供<rt>こども</rt></ruby>っぽいでした</p>
  <p class="pe-fix__good">✓ <ruby>子供<rt>こども</rt></ruby>っぽ<b>かった</b> — っぽい い-sifat, shuning uchun oʻzi tuslanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>風邪<rt>かぜ</rt></ruby>の<ruby>気味<rt>ぎみ</rt></ruby>です</p>
  <p class="pe-fix__good">✓ <ruby>風邪<rt>かぜ</rt></ruby><ruby>気味<rt>ぎみ</rt></ruby>です — <ruby>気味<rt>ぎみ</rt></ruby> otga yalangʻoch yopishadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>曇<rt>くも</rt></ruby>りがち<ruby>日<rt>ひ</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>曇<rt>くも</rt></ruby>りがち<b>の</b><ruby>日<rt>ひ</rt></ruby> — がち otni aniqlaganda の oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>上手<rt>じょうず</rt></ruby>っぽいですね (maqtov sifatida)</p>
  <p class="pe-fix__good">✓ <ruby>上手<rt>じょうず</rt></ruby>そうですね — bu oila maqtov uchun emas; <b>そう</b> (PJ-73) toʻgʻri keladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Bu poyezd tez-tez kechikadi» — qaysi qolip?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>がち</b>: この<ruby>電車<rt>でんしゃ</rt></ruby>は<ruby>遅<rt>おく</rt></ruby>れがちだ. がち chastota haqida — «koʻpincha shunday boʻladi».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>忘<rt>わす</rt></ruby>れる ni がち bilan qoʻshing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>忘<rt>わす</rt></ruby>れがち</b>. ます-shakli <ruby>忘<rt>わす</rt></ruby>れます, oʻzagi <ruby>忘<rt>わす</rt></ruby>れ — oʻshanga ulanadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Bolalarcha edi» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>子供<rt>こども</rt></ruby>っぽかった</b>. っぽい い-sifat boʻlgani uchun oʻzi tuslanadi; «っぽいでした» notoʻgʻri.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Bugun bir oz shamollaganman» — qaysi qolip?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>気味<rt>ぎみ</rt></ruby></b>: <ruby>今日<rt>きょう</rt></ruby>は<ruby>風邪<rt>かぜ</rt></ruby><ruby>気味<rt>ぎみ</rt></ruby>です. Holat bor, lekin kuchli emas — va gap shu bilan yumshaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>忘<rt>わす</rt></ruby>れがち va <ruby>忘<rt>わす</rt></ruby>れっぽい — farqi nimada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>がち</b> — chastota: bu safar ham unutdi, tez-tez shunday boʻladi. <b>っぽい</b> — xususiyat: u unutuvchan odam, tabiati shunday.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜がち</b> — tez-tez … boʻladi</li>
  <li><b>〜っぽい</b> — … simon, … ga oʻxshagan</li>
  <li><b>〜<ruby>気味<rt>ぎみ</rt></ruby></b> — bir oz …</li>
  <li><b><ruby>風邪<rt>かぜ</rt></ruby><ruby>気味<rt>ぎみ</rt></ruby></b> — bir oz shamollagan</li>
  <li><b><ruby>忘<rt>わす</rt></ruby>れっぽい</b> — unutuvchan</li>
  <li><b><ruby>怒<rt>おこ</rt></ruby>りっぽい</b> — jizzaki</li>
  <li><b><ruby>曇<rt>くも</rt></ruby>り</b> — bulutli havo</li>
  <li><b><ruby>遅<rt>おく</rt></ruby>れる</b> — kechikmoq</li>
  <li><b><ruby>太<rt>ふと</rt></ruby>る</b> — semirmoq</li>
  <li><b><ruby>遠慮<rt>えんりょ</rt></ruby></b> — tortinish, andisha</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>がち</b> chastota, <b>っぽい</b> xususiyat, <b><ruby>気味<rt>ぎみ</rt></ruby></b> daraja.</li>
    <li><b>っぽい</b> — い-sifat: っぽかった, っぽくない.</li>
    <li>Uchalasi ham deyarli doim <b>salbiy</b>; maqtov uchun そう yoki よう.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-93: 〜おかげで va 〜せいで — yaxshi va yomon sabab",
        "category": "japanese",
        "order": 93,
        "summary": (
            "Bitta sabab, ikkita baho: おかげで — «… sharofati bilan» "
            "(natija yaxshi), せいで — «… dastidan» (natija yomon). "
            "Va nega neytral sabab uchun PJ-53 dagi ので qoladi."
        ),
        "stories": ["そつぎょうの スピーチ"],
        "content": """
<h2>PJ-93: 〜おかげで va 〜せいで — yaxshi va yomon sabab</h2>

<p>Bitta voqea, ikki xil gap:</p>

<p><ruby>先生<rt>せんせい</rt></ruby>の<b>おかげで</b><ruby>合格<rt>ごうかく</rt></ruby>しました。</p>

<p><ruby>雨<rt>あめ</rt></ruby>の<b>せいで</b><ruby>試合<rt>しあい</rt></ruby>が<ruby>中止<rt>ちゅうし</rt></ruby>になりました。</p>

<p>Ikkalasi ham sabab koʻrsatadi, va ikkalasini ham oʻzbekchada
«tufayli» deb tarjima qilish mumkin. Lekin yapon quloq ularni
bir xil eshitmaydi: birinchisida <b>minnatdorchilik</b>,
ikkinchisida <b>ayb</b> bor.</p>

<p>PJ-53 da siz <b>から</b> va <b>ので</b> ni oʻrgangansiz —
ular <em>bahosiz</em> sabab. Bu dars oʻsha qatorga ikkita
<em>baholi</em> sababni qoʻshadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>〜おかげで</b> bilan yaxshi natijaning sababini aytasiz</li>
    <li><b>〜せいで</b> bilan yomon natijaning sababini aytasiz</li>
    <li>ikkovining <b>ulanishini</b> toʻgʻri yasaysiz</li>
    <li><b>〜せいにする</b> bilan «ayblamoq» deysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Yaxshi natija</span>
  <span class="pe-chip pe-chip--s">sabab</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">おかげで</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">… sharofati bilan</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Yomon natija</span>
  <span class="pe-chip pe-chip--s">sabab</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">せいで</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--neg">… dastidan</span>
</div>

<h3>1. Ulanish — ikkovi uchun bir xil</h3>

<p>おかげ ham, せい ham <b>ot</b>. Shuning uchun ularning
oldiga otni aniqlaydigan shakl tushadi — bu PJ-85 dagi
うち va あいだ bilan bir xil qoida.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Nima ulanadi</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-end">の</td>
      <td class="pj-res"><ruby>先生<rt>せんせい</rt></ruby>のおかげで</td>
      <td class="pj-uz">ustoz sharofati bilan</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">な</td>
      <td class="pj-res"><ruby>元気<rt>げんき</rt></ruby>なおかげで</td>
      <td class="pj-uz">sogʻ boʻlgani uchun</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">yalangʻoch</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>いおかげで</td>
      <td class="pj-uz">arzon boʻlgani uchun</td></tr>
  <tr><td class="pj-stem">feʼl</td><td class="pj-end">oddiy shakl</td>
      <td class="pj-res"><ruby>手伝<rt>てつだ</rt></ruby>ってくれたおかげで</td>
      <td class="pj-uz">yordam bergani uchun</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Bu jadval tanish boʻlishi kerak.</b> Ot <b>の</b>,
  な-sifat <b>な</b> — aynan shu ulanish PJ-81 dagi
  <b>はず</b> da ham, PJ-85 dagi <b>うち</b> da ham turadi.
  Blok F ning qoliplari koʻpincha ot boʻlgani uchun, bu ikki
  qoʻshimcha qayta-qayta uchraydi. せい ham xuddi shunday
  ulanadi — ikkovini alohida yodlash shart emas.</p>
</div>

<h3>2. 〜おかげで — «… sharofati bilan»</h3>

<p>おかげ soʻzining oʻzi «yordam, marhamat» degani, va
gapda u <b>minnatdorchilik</b> olib yuradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s"><ruby>先生<rt>せんせい</rt></ruby>のおかげで</span><ruby>試験<rt>しけん</rt></ruby>に<ruby>合格<rt>ごうかく</rt></ruby>しました。</p>
  <p class="pe-ex__uz">Ustoz sharofati bilan imtihondan oʻtdim.</p>
  <p class="pe-ex__why">Bu yerda ので ham grammatik toʻgʻri boʻlardi, lekin minnatdorchilik yoʻqolardi. おかげで rahmatning oʻzi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>«Sharofati bilan» — oʻzbek tilidagi tayyor kalit, va u
  ham ikki soʻzdan iborat.</b> Diqqat qiling: biz uni
  <em>faqat</em> yaxshi natija bilan ishlatamiz. «Ustoz
  sharofati bilan yiqildim» degan gap quloqqa gʻalati tegadi —
  xuddi yaponcha <ruby>先生<rt>せんせい</rt></ruby>のおかげで
  <ruby>落<rt>お</rt></ruby>ちました degandek. Ikkala tilda ham
  bu gʻalatilik <em>kinoya</em> boʻlib eshitiladi, va aynan
  shuning uchun おかげで ni tanbeh sifatida ham ishlatish
  mumkin. Demak bu qolipni yodlashning eng ishonchli yoʻli —
  «sharofati bilan» iborasini eslab qolish: u qayerda
  tabiiy boʻlsa, おかげで ham oʻsha yerda tabiiy, va qayerda
  kinoya boʻlsa — yaponchada ham kinoya.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Bitta tayyor iborani yodlab qoʻying.</b>
  <b>おかげさまで</b> — «rahmat, yaxshiman». Bu «qalaysiz?»
  degan savolga beriladigan eng odatiy javob, va uning
  ichida «sizning marhamatingiz bilan» degan maʼno bor.
  Yaponlar buni har kuni ishlatadi, koʻpincha rahmat
  aytadigan aniq odam boʻlmasa ham.</p>
</div>

<h3>3. 〜せいで — «… dastidan»</h3>

<p>せい — «ayb, aybdorlik» degani. Shuning uchun せいで doim
yomon natija bilan keladi va gapda <b>ayblash</b> bor.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>雨<rt>あめ</rt></ruby></span>
  <span class="pj-joshi__p">のせいで<small>YOMON SABAB</small></span>
  <span class="pj-joshi__n"><ruby>試合<rt>しあい</rt></ruby>が</span>
  <span class="pj-joshi__v"><ruby>中止<rt>ちゅうし</rt></ruby>になった</span>
  <span class="pj-joshi__uz">Yomgʻir dastidan oʻyin bekor qilindi.</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--neg"><ruby>寝<rt>ね</rt></ruby>すぎたせいで</span>、<ruby>約束<rt>やくそく</rt></ruby>に<ruby>遅<rt>おく</rt></ruby>れてしまった。</p>
  <p class="pe-ex__uz">Koʻp uxlab qolganim dastidan uchrashuvga kech qoldim.</p>
  <p class="pe-ex__why">せいで oʻzini ham aybalashi mumkin. Oxiridagi 〜てしまった (PJ-58) afsusni kuchaytiradi va bu qolip bilan tez-tez keladi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>せい ning oʻz feʼli bor.</b>
  <b>〜のせいにする</b> — «… ni ayblamoq»:
  <ruby>人<rt>ひと</rt></ruby>のせいにしてはいけない
  («birovni ayblamaslik kerak»). Bu ibora tarbiya haqidagi
  gaplarda juda koʻp uchraydi, shuning uchun uni alohida
  yodlab qoʻying.</p>
</div>

<h3>4. Uchtasi bitta jadvalda</h3>

<p>Endi sizda sabab koʻrsatishning uchta darajasi bor.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Baho</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem">〜おかげで</td><td class="pj-uz">yaxshi — minnatdorchilik</td>
      <td class="pj-res"><ruby>薬<rt>くすり</rt></ruby>のおかげで<ruby>治<rt>なお</rt></ruby>った</td>
      <td class="pj-end">sharofati bilan</td></tr>
  <tr><td class="pj-stem">〜ので (PJ-53)</td><td class="pj-uz">bahosiz</td>
      <td class="pj-res"><ruby>薬<rt>くすり</rt></ruby>を<ruby>飲<rt>の</rt></ruby>んだので<ruby>治<rt>なお</rt></ruby>った</td>
      <td class="pj-end">shuning uchun</td></tr>
  <tr><td class="pj-stem">〜せいで</td><td class="pj-uz">yomon — ayb</td>
      <td class="pj-res"><ruby>薬<rt>くすり</rt></ruby>のせいで<ruby>眠<rt>ねむ</rt></ruby>くなった</td>
      <td class="pj-end">dastidan</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu uchlik toʻliq bor, va aynan shuning
  uchun bu dars oson.</b> «Ustoz <em>sharofati bilan</em>
  oʻtdim» — rahmat. «Yomgʻir <em>dastidan</em> bekor boʻldi» —
  norozilik. «Yomgʻir yoqqani <em>uchun</em> bekor boʻldi» —
  quruq xabar. Uch soʻz, uch ohang, xuddi yaponchadagidek.
  Lekin bitta tuzoq bor: oʻzbekcha «<em>tufayli</em>»
  ikkalasiga ham ishlaydi — «ustoz tufayli oʻtdim» ham,
  «yomgʻir tufayli bekor boʻldi» ham toʻgʻri. Shuning uchun
  «tufayli» ni koʻrganingizda toʻxtang va oʻzingizdan
  soʻrang: <em>«natija yaxshimi yoki yomonmi?»</em> Javob
  qolipni tanlaydi, va bu savol hech qachon
  adashtirmaydi.</p>
</div>

<h3>5. Nozik joylar</h3>

<div class="pe-steps">
  <ol>
    <li><b>おかげで kinoya ham boʻlishi mumkin.</b>
    <ruby>君<rt>きみ</rt></ruby>のおかげで<ruby>遅<rt>おく</rt></ruby>れたよ
    («sening <em>sharofating</em> bilan kech qoldim») — bu
    ochiq tanbeh. Yozganda ehtiyot boʻling: kinoya ovoz bilan
    beriladi, matnda esa koʻrinmaydi.</li>
    <li><b>せいで ni oʻzingiz haqingizda ishlatish odobli.</b>
    Boshqa odamga <ruby>君<rt>きみ</rt></ruby>のせいで deyish
    — ochiq ayblash, va yaponchada bu juda kuchli eshitiladi.
    Shuning uchun rasmiy matnda uning oʻrniga PJ-87 dagi
    <b>によって</b> yoki oddiy <b>ので</b> turadi.</li>
    <li><b>Natija ikkala qolipda ham gapning oxirida.</b>
    Sabab birinchi, natija keyin — tartib hech qachon
    almashmaydi.</li>
  </ol>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s">みなさんが<ruby>手伝<rt>てつだ</rt></ruby>ってくれたおかげで</span>、<ruby>無事<rt>ぶじ</rt></ruby>に<ruby>終<rt>お</rt></ruby>わりました。</p>
  <p class="pe-ex__uz">Hammangiz yordam berganingiz sharofati bilan eson-omon tugadi.</p>
  <p class="pe-ex__why">Feʼl bilan ulanish — oddiy shakl (PJ-45). Bu gap nutq va xatlarda deyarli tayyor qolip.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «-ning aybi bilan» va yaponcha せいにする bir
  xil mexanizm.</b> «Buni men<em>ing aybim bilan</em> boʻldi
  deb aytdi» degan gapni yaponchada
  <ruby>私<rt>わたし</rt></ruby>のせいにした deb aytamiz — yaʼni
  «aybni menga yukladi». Ikkala tilda ham «ayb» degan
  <em>ot</em> markazda turibdi, va uning atrofiga grammatika
  qurilgan. Shuning uchun せい ni «sabab» deb emas,
  <b>«ayb»</b> deb yodlang — shunda せいで ning nega faqat
  yomon natija bilan kelishi oʻz-oʻzidan tushunarli
  boʻladi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">合</span>
    <span class="pj-kanji__uz">mos kelmoq, qoʻshilmoq</span>
    <span class="pj-kanji__on">オン: ゴウ・ガッ</span>
    <span class="pj-kanji__kun">KUN: あ(う)</span>
    <span class="pj-kanji__note">合格 (ごうかく) — imtihondan oʻtish · 間に合う (まにあう) — ulgurmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">格</span>
    <span class="pj-kanji__uz">daraja, maqom</span>
    <span class="pj-kanji__on">オン: カク</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">性格 (せいかく) — xarakter · 価格 (かかく) — narx</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">無</span>
    <span class="pj-kanji__uz">yoʻq, -siz</span>
    <span class="pj-kanji__on">オン: ム・ブ</span>
    <span class="pj-kanji__kun">KUN: な(い)</span>
    <span class="pj-kanji__note">無事 (ぶじ) — eson-omon · 無理 (むり) — imkonsiz</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>雨<rt>あめ</rt></ruby>せいで<ruby>中止<rt>ちゅうし</rt></ruby>になった</p>
  <p class="pe-fix__good">✓ <ruby>雨<rt>あめ</rt></ruby><b>の</b>せいで — せい ot, ot oldidan の oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>先生<rt>せんせい</rt></ruby>のせいで<ruby>合格<rt>ごうかく</rt></ruby>しました</p>
  <p class="pe-fix__good">✓ <ruby>先生<rt>せんせい</rt></ruby>の<b>おかげで</b> — natija yaxshi, demak minnatdorchilik qolipi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>雨<rt>あめ</rt></ruby>のおかげで<ruby>試合<rt>しあい</rt></ruby>が<ruby>中止<rt>ちゅうし</rt></ruby>になった</p>
  <p class="pe-fix__good">✓ <ruby>雨<rt>あめ</rt></ruby>の<b>せいで</b> — natija yomon; おかげで qoʻyilsa, kinoya boʻlib eshitiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>元気<rt>げんき</rt></ruby>のおかげで<ruby>働<rt>はたら</rt></ruby>ける</p>
  <p class="pe-fix__good">✓ <ruby>元気<rt>げんき</rt></ruby><b>な</b>おかげで — な-sifat な ni saqlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>人<rt>ひと</rt></ruby>のせいでする</p>
  <p class="pe-fix__good">✓ <ruby>人<rt>ひと</rt></ruby>のせい<b>に</b>する — «ayblamoq» degan iborada で emas, <b>に</b> turadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Ustoz sharofati bilan imtihondan oʻtdim» — おかげで yoki せいで?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>おかげで</b>: <ruby>先生<rt>せんせい</rt></ruby>のおかげで<ruby>合格<rt>ごうかく</rt></ruby>しました. Natija yaxshi, va gapda minnatdorchilik bor.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Boʻsh joyni toʻldiring: <ruby>元気<rt>げんき</rt></ruby>___おかげで<ruby>働<rt>はたら</rt></ruby>けます。</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>な</b> — <ruby>元気<rt>げんき</rt></ruby>なおかげで. な-sifat おかげ oldida な ni saqlaydi, xuddi はず va うち dagidek.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Yomgʻir dastidan oʻyin bekor qilindi» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>雨<rt>あめ</rt></ruby>のせいで<ruby>試合<rt>しあい</rt></ruby>が<ruby>中止<rt>ちゅうし</rt></ruby>になりました</b>. Ot oldidan <b>の</b> tushishini unutmang.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Birovni ayblamaslik kerak» — qaysi ibora?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>人<rt>ひと</rt></ruby>のせいにしてはいけない</b>. «Ayblamoq» — せい<b>に</b>する; bu yerda で emas, に turadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Neytral, bahosiz sabab uchun qaysi qolip?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>から</b> yoki <b>ので</b> (PJ-53). おかげで va せいで sababga baho qoʻshadi; ので esa faqat xabar beradi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜おかげで</b> — … sharofati bilan</li>
  <li><b>おかげさまで</b> — rahmat, yaxshiman</li>
  <li><b>〜せいで</b> — … dastidan</li>
  <li><b>〜のせいにする</b> — … ni ayblamoq</li>
  <li><b><ruby>合格<rt>ごうかく</rt></ruby>する</b> — imtihondan oʻtmoq</li>
  <li><b><ruby>中止<rt>ちゅうし</rt></ruby>になる</b> — bekor qilinmoq</li>
  <li><b><ruby>無事<rt>ぶじ</rt></ruby>に</b> — eson-omon</li>
  <li><b><ruby>試合<rt>しあい</rt></ruby></b> — musobaqa, oʻyin</li>
  <li><b><ruby>手伝<rt>てつだ</rt></ruby>う</b> — yordam bermoq</li>
  <li><b><ruby>寝<rt>ね</rt></ruby>すぎる</b> — koʻp uxlab qolmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>おかげで</b> yaxshi natija, <b>せいで</b> yomon natija, <b>ので</b> bahosiz.</li>
    <li>Ikkalasi ham <b>ot</b>: ot <b>の</b>, な-sifat <b>な</b> oladi.</li>
    <li><b>せい</b> = «ayb», shuning uchun <b>せいにする</b> — «ayblamoq».</li>
  </ul>
</div>
""",
    },
]
