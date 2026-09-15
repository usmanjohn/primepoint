# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-55, PJ-56, PJ-57 (Block D oxiri).

Batchning ipi — <b>irodam bormi yoki yoʻqmi</b> degan savol, yapon
tilining eng oʻzbek pupilga sezilmaydigan oʻqi:
    PJ-55  ても      — irodam natijani oʻzgartirmaydi
    PJ-56  ために/ように — maqsad meniki (ために) yoki menga bogʻliq emas (ように)
    PJ-57  する/なる   — men qaror qildim (ことにする) yoki shunday boʻldi (ようになる)

⚠️ PJ-57 kursda <b>なる</b> ni birinchi marta ochiq oʻrgatadi
(くなる · になる · ようになる). Shu darsgacha oʻqish matnlarida なる
ishlatilmagan — gate shuni tekshiradi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_55_57.py --author=prime
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
        "title": "PJ-55: 〜ても — «…sa ham»",
        "category": "japanese",
        "order": 55,
        "summary": (
            "Shart gapining teskarisi: natija shartga qaramaydi. "
            "Va siz bu qolipni PJ-32 dan beri bilasiz — 〜てもいいです "
            "aynan shu."
        ),
        "stories": ["あめが ふっても"],
        "content": """
<h2>PJ-55: 〜ても — «…sa ham»</h2>

<p>Oxirgi besh dars shart haqida edi: agar bu boʻlsa, u boʻladi.
Bugun teskarisi. <b>Bu boʻlsa <em>ham</em>, u baribir boʻladi.</b></p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">SHART (PJ-50)</p>
    <p><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったら、<ruby>行<rt>い</rt></ruby>きません。</p>
    <p>Yomgʻir yogʻsa, bormayman. Natija <b>shartga qaraydi</b>.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">TAʼZIM (bugun)</p>
    <p><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っても、<ruby>行<rt>い</rt></ruby>きます。</p>
    <p>Yomgʻir yogʻsa ham, boraman. Natija <b>qaramaydi</b>.</p></div>
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Har qanday soʻzdan ても shaklini yasaysiz</li>
    <li>Inkor shaklini — なくても ni — tuzasiz</li>
    <li>Soʻroq soʻzi bilan «nima qilsa ham» degan qolipni yasaysiz</li>
    <li>PJ-32 dagi 〜てもいいです nima ekanini nihoyat tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">…sa ham</span>
  <span class="pe-chip pe-chip--s">て-shakli</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">も</span>
</div>

<h3>1. Yasalishi — yana eski shakl, yangi qoʻshimcha</h3>

<p>PJ-29 va PJ-30 da siz て-shaklini oʻrgangansiz. Bugun unga
<b>も</b> qoʻshiladi. Xolos — xuddi PJ-50 dagi た + ら kabi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Oraliq shakl</th><th>+ も</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-end"><ruby>降<rt>ふ</rt></ruby>って</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>っても</td><td class="pj-uz">yogʻsa ham</td></tr>
  <tr><td class="pj-stem">Feʼl (inkor)</td><td class="pj-end"><ruby>降<rt>ふ</rt></ruby>らなくて</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>らなくても</td><td class="pj-uz">yogʻmasa ham</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end"><ruby>高<rt>たか</rt></ruby>くて</td>
      <td class="pj-res"><ruby>高<rt>たか</rt></ruby>くても</td><td class="pj-uz">qimmat boʻlsa ham</td></tr>
  <tr><td class="pj-stem">い-sifat (inkor)</td><td class="pj-end"><ruby>高<rt>たか</rt></ruby>くなくて</td>
      <td class="pj-res"><ruby>高<rt>たか</rt></ruby>くなくても</td><td class="pj-uz">qimmat boʻlmasa ham</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end"><ruby>静<rt>しず</rt></ruby>かで</td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かでも</td><td class="pj-uz">tinch boʻlsa ham</td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-end"><ruby>学生<rt>がくせい</rt></ruby>で</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>でも</td><td class="pj-uz">talaba boʻlsa ham</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Ot va な-sifatda て emas, で.</b> Sababi PJ-29 da aytilgan
  edi: otning て-shakli <b>で</b>. Shuning uchun
  <ruby>学生<rt>がくせい</rt></ruby><b>でも</b> —
  «<ruby>学生<rt>がくせい</rt></ruby>てても» emas. Bu bir qarashda
  boshqa qoidadek koʻrinadi, aslida esa oʻsha bitta て-shakli.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «-sa ham» ning aynan oʻzi.</b> «Yomgʻir yogʻ<b>sa
  ham</b> boraman» — ikkala tilda ham bu qurilma ikki boʻlakdan:
  shart + «ham». Yaponchada ham xuddi shunday:
  <b>て</b> (shart boʻlagi) + <b>も</b> (ayni oʻsha «ham», PJ-19 dagi
  も). Yaʼni siz ikkita tanish narsani qoʻshyapsiz, uchinchi
  narsani emas.</p>
</div>

<p>Bu qolip bir qarashda kichkina koʻrinadi, lekin u gapga
butunlay boshqa ohang beradi. Shart gap suhbatdoshga
<em>tanlov</em> beradi: «yomgʻir yogʻsa, bormaymiz» — demak
hali hammasi ochiq. ても esa tanlovni <b>yopadi</b>: «yomgʻir
yogʻsa ham boramiz» — bu qaror allaqachon qabul qilingan.
Shuning uchun ても koʻpincha vaʼda, ahd va qatʼiyat
gaplarida chiqadi. Yapon tilida biror ishga jiddiy
kirishayotgan odam deyarli doim shu qolipni ishlatadi.</p>

<h3>2. Inkor: 〜なくても</h3>

<p>Inkor shakli alohida eʼtiborga loyiq, chunki u kundalik nutqda
juda koʻp ishlatiladi.</p>

<div class="pe-steps">
  <ol>
    <li><ruby>行<rt>い</rt></ruby>く ning ない-shakli:
    <ruby>行<rt>い</rt></ruby>か<b>ない</b> (PJ-34)</li>
    <li>ない い-sifat, demak uning て-shakli:
    <ruby>行<rt>い</rt></ruby>か<b>なくて</b></li>
    <li>Ustiga も: <ruby>行<rt>い</rt></ruby>か<b>なくても</b></li>
  </ol>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>今日<rt>きょう</rt></ruby>は<ruby>来<rt>こ</rt></ruby>なくてもいいです。</p>
  <p class="pe-ex__uz">Bugun kelmasangiz ham boʻladi.</p>
  <p class="pe-ex__why">«Kelmaslik kerak» emas — «kelish shart emas». Bu ikkisi boshqa gap.</p>
</div>

<p>Va yana bir amaliy joyi bor: bu shakl <b>ruxsat soʻrash
va berishning asosi</b>. Yaponchada «mumkinmi?» degan savol
deyarli doim ても bilan tuziladi, chunki yapon tili
toʻgʻridan-toʻgʻri «ruxsat bering» demaydi. U aylanib
oʻtadi: «qilsam ham boʻladimi?» Keyingi boʻlimda buni
yaqindan koʻrasiz.</p>

<h3>3. PJ-32 ning siri ochildi</h3>

<p>PJ-32 da siz <b>〜てもいいです</b> ni «ruxsat» qolipi deb
yodlagansiz: <ruby>食<rt>た</rt></ruby>べてもいいです — «yesangiz
boʻladi». U yerda u sehrli ibora edi. Endi uni yechib
koʻrsatsa boʻladi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>食<rt>た</rt></ruby>べて</span>
  <span class="pj-joshi__p">も<small>…SA HAM</small></span>
  <span class="pj-joshi__v">いいです</span>
  <span class="pj-joshi__uz">Yesangiz ham — yaxshi. Yaʼni: yeyishingiz mumkin.</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ham ruxsatni shu yoʻl bilan beradi.</b>
  «Yesang ham boʻladi», «Borsang ham mayli» — bu gaplar ham,
  soʻzma-soʻz olganda, ruxsat emas, <em>eʼtiroz yoʻqligi</em>.
  Yapon tili ayni shu yoʻldan boradi. Shuning uchun
  <ruby>食<rt>た</rt></ruby>べてもいいです ni endi yodlash shart
  emas — uni <b>yasash</b> mumkin.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Soʻzma-soʻz</th><th>Amalda</th></tr>
  <tr><td class="pj-stem">〜てもいいです</td><td class="pj-uz">qilsang ham — yaxshi</td>
      <td class="pj-res">ruxsat (PJ-32)</td></tr>
  <tr><td class="pj-stem">〜なくてもいいです</td><td class="pj-uz">qilmasang ham — yaxshi</td>
      <td class="pj-res">shart emas</td></tr>
  <tr><td class="pj-stem">〜てはいけません</td><td class="pj-uz">qilsang — boʻlmaydi</td>
      <td class="pj-res">taqiq (PJ-33)</td></tr>
  <tr><td class="pj-stem">〜なければなりません</td><td class="pj-uz">qilmasang — boʻlmaydi</td>
      <td class="pj-res">majburiyat (PJ-33)</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bu jadval butun N5 grammatikasining toʻrtdan birini
  bitta qoidaga bogʻlaydi.</b> Toʻrttasi ham «shart + baho»
  qurilmasi. Shuni bir marta koʻrsangiz, ularni chalkashtirish
  ancha qiyinlashadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>高<rt>たか</rt></ruby>くても<ruby>買<rt>か</rt></ruby>います。</p>
  <p class="pe-ex__uz">Qimmat boʻlsa ham sotib olaman.</p>
  <p class="pe-ex__why">い-sifatning て-shakli <b>くて</b>, ustiga も.</p>
</div>

<h3>4. Soʻroq soʻzi + ても = «nima qilsa ham»</h3>

<p>Soʻroq soʻzini ても bilan qoʻshsangiz, u <b>«farqi yoʻq»</b>
degan maʼnoni beradi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem"><ruby>何<rt>なに</rt></ruby>を〜ても</td>
      <td class="pj-res"><ruby>何<rt>なに</rt></ruby>を<ruby>食<rt>た</rt></ruby>べても</td>
      <td class="pj-uz">nima yesa ham</td></tr>
  <tr><td class="pj-stem">どこへ〜ても</td>
      <td class="pj-res">どこへ<ruby>行<rt>い</rt></ruby>っても</td>
      <td class="pj-uz">qayerga borsa ham</td></tr>
  <tr><td class="pj-stem">だれが〜ても</td>
      <td class="pj-res">だれが<ruby>来<rt>き</rt></ruby>ても</td>
      <td class="pj-uz">kim kelsa ham</td></tr>
  <tr><td class="pj-stem">いくら〜ても</td>
      <td class="pj-res">いくら<ruby>読<rt>よ</rt></ruby>んでも</td>
      <td class="pj-uz">qancha oʻqisa ham</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">いくら<ruby>探<rt>さが</rt></ruby>しても、<ruby>見<rt>み</rt></ruby>つかりませんでした。</p>
  <p class="pe-ex__uz">Qancha qidirsam ham, topolmadim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha bu qolipni ayni shu tartibda yasaydi.</b>
  «<em>Nima</em> qil<em>sa ham</em>», «<em>qayerga</em>
  bor<em>sa ham</em>», «<em>qancha</em> oʻqi<em>sa ham</em>» —
  soʻroq soʻzi oldinda, «-sa ham» orqada. Yaponchada ham:
  soʻroq soʻzi oldinda, ても orqada. Bu ikki tilning eng aniq
  ustma-ust tushgan joylaridan biri, shuning uchun bu qolipni
  oʻzbek oʻquvchisi deyarli darrov oʻzlashtiradi.</p>
</div>

<p>Diqqat qiling: bu qolipda <b>も</b> oʻz maʼnosini
yoʻqotmagan. PJ-19 da siz uni «ham» deb oʻrgangansiz —
<ruby>私<rt>わたし</rt></ruby>も, これも. Bu yerda ham u aynan
shu ish qilyapti, faqat otga emas, <em>butun shartga</em>
qoʻshilyapti: «nima yesa — <em>u ham</em> boʻladi»,
«kim kelsa — <em>u ham</em> boʻladi». Shuning uchun natija
oʻzgarmaydi: hamma yoʻl bir joyga olib boradi.</p>

<h3>5. でも — bu ham oʻsha も</h3>

<p>PJ-54 da siz <b>でも</b> ni «lekin» deb koʻrgansiz. Endi
uning qayerdan kelganini koʻrasiz: <b>で</b> (te-shakl) +
<b>も</b> — yaʼni «shunday boʻlsa ham». Gap boshiga chiqqanda
u «lekin» boʻlib qoladi.</p>

<div class="pj-say">
  <span class="pj-say__from">で + も</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">でも</span>
  <span class="pj-say__why">«shunday boʻlsa ham» → «lekin»</span>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">続</span>
    <span class="pj-kanji__uz">davom etmoq</span>
    <span class="pj-kanji__on">オン: ゾク</span>
    <span class="pj-kanji__kun">KUN: つづ(く), つづ(ける)</span>
    <span class="pj-kanji__note">続ける (つづける) — davom ettirmoq · 続く (つづく) — davom etmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">必</span>
    <span class="pj-kanji__uz">albatta, zarur</span>
    <span class="pj-kanji__on">オン: ヒツ</span>
    <span class="pj-kanji__kun">KUN: かなら(ず)</span>
    <span class="pj-kanji__note">必ず (かならず) — albatta · 必要 (ひつよう) — zarur</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>てても</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>でも</b> — otning て-shakli で (PJ-29).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>高<rt>たか</rt></ruby>いても</p>
  <p class="pe-fix__good">✓ <ruby>高<rt>たか</rt></ruby><b>くても</b> — い-sifatning て-shakli くて.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>かないても</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>か<b>なくても</b> — ない い-sifat, demak なくて.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>来<rt>こ</rt></ruby>なくてもいいです = «kelmang»</p>
  <p class="pe-fix__good">✓ <ruby>来<rt>こ</rt></ruby>なくてもいいです = «kelish <b>shart emas</b>» — taqiq emas, erkinlik.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>読<rt>よ</rt></ruby>む ning ても shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>読<rt>よ</rt></ruby>んでも</b> — て-shakli <ruby>読<rt>よ</rt></ruby>んで (PJ-30), unga も.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>安<rt>やす</rt></ruby>い ning ても shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>安<rt>やす</rt></ruby>くても</b> — い-sifatning て-shakli くて.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Yomgʻir yogʻsa ham boramiz» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っても<ruby>行<rt>い</rt></ruby>きます</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>行<rt>い</rt></ruby>かなくてもいいです» nimani anglatadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Borish shart emas.</b> «Bormang» degani emas — bu taqiq emas, erkinlik.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Kim kelsa ham, javob bir xil» — boshini yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>だれが<ruby>来<rt>き</rt></ruby>ても…</b> — soʻroq soʻzi oldinda, ても orqada.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜ても</b> — …sa ham</li>
  <li><b>〜なくても</b> — …masa ham</li>
  <li><b>〜なくてもいいです</b> — …shart emas</li>
  <li><b>いくら〜ても</b> — qancha …sa ham</li>
  <li><b><ruby>続<rt>つづ</rt></ruby>ける</b> — davom ettirmoq (II guruh)</li>
  <li><b><ruby>必<rt>かなら</rt></ruby>ず</b> — albatta</li>
  <li><b><ruby>見<rt>み</rt></ruby>つかる</b> — topilmoq (I guruh)</li>
  <li><b><ruby>諦<rt>あきら</rt></ruby>める</b> — taslim boʻlmoq (II guruh)</li>
  <li><b><ruby>練習<rt>れんしゅう</rt></ruby></b> — mashq</li>
  <li><b><ruby>試合<rt>しあい</rt></ruby></b> — musobaqa</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>て-shakli + も</b> — ot va な-sifatda で + も.</li>
    <li>〜なくてもいいです = <b>shart emas</b>, taqiq emas.</li>
    <li>Soʻroq soʻzi + ても = <b>«farqi yoʻq»</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-56: 〜ために va 〜ように — maqsad",
        "category": "japanese",
        "order": 56,
        "summary": (
            "«…ish uchun» va «…sin deb» — oʻzbekcha bu ikkisini "
            "allaqachon ajratadi, va yapon tili aynan shu chiziq "
            "boʻyicha ために bilan ように ni ajratadi."
        ),
        "stories": ["なんの ために"],
        "content": """
<h2>PJ-56: 〜ために va 〜ように — maqsad</h2>

<p>Ikkita oʻzbekcha gapni oʻqing:</p>

<p>Yapon tilini <b>oʻrganish uchun</b> Yaponiyaga boraman.<br>
Bola <b>tushunsin deb</b> sekin gapiraman.</p>

<p>Ikkalasi ham maqsad. Lekin siz ularni bir xil aytmaysiz, va
sababi aniq: birinchisida maqsad <b>meniki</b> — men oʻrganaman.
Ikkinchisida u <b>menga bogʻliq emas</b> — tushunadigan men
emasman.</p>

<p><b>Yapon tili aynan shu chiziq boʻyicha ikkiga boʻlinadi:</b>
ために va ように.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ために va ように ni yasaysiz</li>
    <li>Ikkalasi orasidagi chiziqni bir savolda topasiz</li>
    <li>Ot bilan keladigan 〜のために ni ishlatasiz</li>
    <li>〜ないように — «…masin deb» ni tuzasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Maqsad</span>
  <span class="pe-chip pe-chip--s">MAQSAD</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">ために / ように</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">ISH</span>
</div>

<h3>1. Chiziq: irodam yetadimi?</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">ために — irodam yetadi</p>
    <p><ruby>日本語<rt>にほんご</rt></ruby>を<ruby>勉強<rt>べんきょう</rt></ruby>する<b>ために</b>、<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。</p>
    <p>Oʻrganish — men qiladigan ish. Lugʻat shakli.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">ように — irodam yetmaydi</p>
    <p><ruby>子<rt>こ</rt></ruby>どもが<ruby>分<rt>わ</rt></ruby>かる<b>ように</b>、ゆっくり<ruby>話<rt>はな</rt></ruby>します。</p>
    <p>Tushunish — bolaning ishi, meniki emas.</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Bitta savol, aniq javob.</b> Maqsaddagi ishni
  <em>men</em> qilamanmi va uni <em>boshqara olamanmi</em>?
  Ha — <b>ために</b>. Yoʻq — <b>ように</b>. «Yoʻq» uchta shaklda
  keladi: boshqa odam qiladi · qobiliyat (potensial shakl) ·
  inkor. Uchalasi ham <b>ように</b>.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Maqsaddagi feʼl</th><th>Qaysi biri</th><th>Misol</th></tr>
  <tr><td class="pj-stem">Men qilaman, boshqaraman</td><td class="pj-end"><b>ために</b></td>
      <td class="pj-res"><ruby>買<rt>か</rt></ruby>うために<ruby>働<rt>はたら</rt></ruby>きます</td></tr>
  <tr><td class="pj-stem">Boshqa odam qiladi</td><td class="pj-end"><b>ように</b></td>
      <td class="pj-res"><ruby>子<rt>こ</rt></ruby>どもが<ruby>寝<rt>ね</rt></ruby>るように、<ruby>電気<rt>でんき</rt></ruby>を<ruby>消<rt>け</rt></ruby>します</td></tr>
  <tr><td class="pj-stem">Qobiliyat (potensial)</td><td class="pj-end"><b>ように</b></td>
      <td class="pj-res"><ruby>読<rt>よ</rt></ruby>めるように<ruby>練習<rt>れんしゅう</rt></ruby>します</td></tr>
  <tr><td class="pj-stem">Inkor</td><td class="pj-end"><b>ように</b></td>
      <td class="pj-res"><ruby>忘<rt>わす</rt></ruby>れないように<ruby>書<rt>か</rt></ruby>きます</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha bu chiziqni allaqachon chizib qoʻygan.</b>
  «Oʻrga<em>nish uchun</em>» va «tushun<em>sin deb</em>» — ikkala
  oʻzbekcha qolip ham ayni shu farqni koʻrsatadi. «-ish uchun»
  oʻzingiz qiladigan ishga, «-sin deb» boshqasining ishiga
  qoʻyiladi. «Bola tushunish uchun sekin gapiraman» degan gap
  oʻzbekchada ham gʻalati eshitiladi — chunki bu farqni til
  oʻzi talab qiladi. Demak siz yangi tushunchani emas,
  <b>yangi ikki soʻzni</b> oʻrganyapsiz.</p>
</div>

<p>Diqqat qiling: bu chiziq <em>maqsad</em> boʻyicha emas,
<em>maqsaddagi feʼl</em> boʻyicha oʻtadi. Bitta va oʻsha
istak ikki xil aytilishi mumkin: «yaponcha
<ruby>勉強<rt>べんきょう</rt></ruby>する ために» (oʻqish —
mening ishim) va «yaponcha
<ruby>話<rt>はな</rt></ruby>せる ように» (gapira olish —
natija). Ikkalasining orqasida bir xil orzu turibdi, lekin
gapda turgan feʼl boshqa — va yapon tili aynan shu feʼlga
qaraydi, orzuga emas.</p>

<h3>2. ために — yasalishi</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Nima qoʻshiladi</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-end">lugʻat shakli + ために</td>
      <td class="pj-res"><ruby>買<rt>か</rt></ruby>うために</td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-end">ot + <b>の</b> + ために</td>
      <td class="pj-res"><ruby>健康<rt>けんこう</rt></ruby><b>の</b>ために</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>ために dan oldin inkor turmaydi.</b>
  «<ruby>忘<rt>わす</rt></ruby>れないために» notoʻgʻri — inkor
  <em>boshqarib boʻlmaydigan</em> narsa, demak u
  <b>ように</b> ga tegishli:
  <ruby>忘<rt>わす</rt></ruby>れない<b>ように</b>. Bu darsda eng
  koʻp qilinadigan xato shu.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>健康<rt>けんこう</rt></ruby>のために、<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>走<rt>はし</rt></ruby>っています。</p>
  <p class="pe-ex__uz">Sogʻliq uchun har kuni ertalab yuguraman.</p>
  <p class="pe-ex__why">Ot + <b>の</b> + ために. «<ruby>健康<rt>けんこう</rt></ruby>ために» notoʻgʻri.</p>
</div>

<p>Yana bir amaliy belgi bor, va u koʻp hollarda ishlaydi:
<b>ために dan oldin va keyin ega bir xil boʻladi</b>,
ように da esa koʻpincha boshqa. «Men sotib olaman — men
ishlayman»: bitta odam, ために. «Bola tushunadi — men
gapiraman»: ikki odam, ように. Bu qoida emas, lekin
tekshiruv sifatida juda tez ishlaydi.</p>

<h3>3. ように — yasalishi</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Nima qoʻshiladi</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td class="pj-stem">Potensial shakl</td><td class="pj-end">+ ように</td>
      <td class="pj-res"><ruby>話<rt>はな</rt></ruby>せるように</td></tr>
  <tr><td class="pj-stem">Inkor</td><td class="pj-end">ない + ように</td>
      <td class="pj-res"><ruby>遅<rt>おく</rt></ruby>れないように</td></tr>
  <tr><td class="pj-stem">Boshqa odamning ishi</td><td class="pj-end">lugʻat shakli + ように</td>
      <td class="pj-res"><ruby>見<rt>み</rt></ruby>えるように</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>漢字<rt>かんじ</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れないように、<ruby>毎日<rt>まいにち</rt></ruby><ruby>書<rt>か</rt></ruby>いています。</p>
  <p class="pe-ex__uz">Kanjini unutmasligim uchun har kuni yozib turaman.</p>
  <p class="pe-ex__why">Oʻzbekchada ham «unutmasligim uchun» — «unutmaslik uchun» emas. Inkor irodadan tashqarida.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>日本語<rt>にほんご</rt></ruby>の<ruby>新聞<rt>しんぶん</rt></ruby>が<ruby>読<rt>よ</rt></ruby>めるように、<ruby>漢字<rt>かんじ</rt></ruby>を<ruby>勉強<rt>べんきょう</rt></ruby>しています。</p>
  <p class="pe-ex__uz">Yaponcha gazeta oʻqiy olishim uchun kanji oʻrganyapman.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Potensial shakl nega ように oladi?</b> Chunki
  «oʻqiy ol<em>ish</em>» — bu qaror emas, <b>natija</b>. Siz
  «ertaga oʻqiy oladigan boʻlaman» deb qaror qila olmaysiz;
  siz faqat mashq qilasiz, qobiliyat esa oʻzi keladi.
  Oʻzbekchada ham «oʻqiy olishim uchun» deymiz —
  «oʻqiy olish uchun» emas. Egalik qoʻshimchasi aynan shuni
  koʻrsatib turibdi: bu men qiladigan ish emas, men bilan
  <em>boʻladigan</em> narsa.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Ot bilan ために — oʻzbekchada ham «uchun».</b>
  «<ruby>健康<rt>けんこう</rt></ruby>のために» = «sogʻliq <em>uchun</em>»,
  «<ruby>将来<rt>しょうらい</rt></ruby>のために» = «kelajak <em>uchun</em>».
  Bu yerda ikki til deyarli ustma-ust tushadi — faqat
  yaponcha otdan keyin <b>の</b> talab qiladi, oʻzbekcha esa
  hech narsa talab qilmaydi. Shuning uchun oʻzbek oʻquvchisi
  aynan shu の ni tushirib qoldiradi: «<ruby>健康<rt>けんこう</rt></ruby>
  ために» — bu darsdagi eng koʻp uchraydigan ikkinchi xato.</p>
</div>

<h3>4. ように yana bir ishda: iltimosni yetkazish</h3>

<p>ように gap oxirida ham turadi — bunda u yumshoq iltimos yoki
tilak bildiradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>忘<rt>わす</rt></ruby>れないようにしてください。</p>
  <p class="pe-ex__uz">Unutmaslikka harakat qiling.</p>
  <p class="pe-ex__why">〜ようにする — «shunday boʻlishiga harakat qilmoq». PJ-57 da bu qolip davom etadi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>〜ようにしています — odat haqida.</b>
  <ruby>毎日<rt>まいにち</rt></ruby><ruby>野菜<rt>やさい</rt></ruby>を
  <ruby>食<rt>た</rt></ruby>べるようにしています — «har kuni sabzavot
  yeyishga harakat qilaman». Bu shunchaki
  <ruby>食<rt>た</rt></ruby>べています dan farq qiladi: u yerda odat,
  bu yerda <em>ongli saʼy-harakat</em>.</p>
</div>

<p>Bu ikki soʻzni ajratishda yodlash deyarli kerak emas,
chunki chiziq mantiqiy. Maqsad — siz <em>qila oladigan</em>
narsa boʻlsa, siz uni oʻz zimmangizga olasiz: ために. Maqsad
sizning qoʻlingizdan chiqib ketgan boʻlsa — qobiliyat oʻzi
keladi, inkor oʻzi boʻladi, boshqa odam oʻzi tushunadi —
siz faqat <em>tilay</em> olasiz: ように. Shuning uchun
ために «niyat», ように esa «tilak» deb ham tarjima qilinadi.</p>

<h3>5. ために ning ikkinchi maʼnosi: sabab</h3>

<p>Ot bilan kelganda ために baʼzan maqsad emas, <b>sabab</b>
bildiradi. Uni kontekst ajratadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>事故<rt>じこ</rt></ruby>のために、<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まりました。</p>
  <p class="pe-ex__uz">Hodisa tufayli poyezdlar toʻxtadi.</p>
  <p class="pe-ex__why">«Hodisa uchun» emas — hodisa maqsad boʻla olmaydi. Demak bu <b>sabab</b>.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Ajratish oson:</b> maqsad <em>kelajakda</em> turadi va
  yaxshi narsa boʻladi; sabab <em>oʻtmishda</em> turadi va
  koʻpincha yomon narsa boʻladi. «Sogʻliq uchun yuguraman» —
  maqsad. «Hodisa tufayli toʻxtadi» — sabab. Yaponlar ham buni
  faqat mazmundan biladi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">健</span>
    <span class="pj-kanji__uz">sogʻlom</span>
    <span class="pj-kanji__on">オン: ケン</span>
    <span class="pj-kanji__kun">KUN: すこ(やか)</span>
    <span class="pj-kanji__note">健康 (けんこう) — sogʻliq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">将</span>
    <span class="pj-kanji__uz">kelgusi, boshliq</span>
    <span class="pj-kanji__on">オン: ショウ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">将来 (しょうらい) — kelajak</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>忘<rt>わす</rt></ruby>れないために</p>
  <p class="pe-fix__good">✓ <ruby>忘<rt>わす</rt></ruby>れない<b>ように</b> — inkor doim ように.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>読<rt>よ</rt></ruby>めるために</p>
  <p class="pe-fix__good">✓ <ruby>読<rt>よ</rt></ruby>める<b>ように</b> — qobiliyat ham ように.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>健康<rt>けんこう</rt></ruby>ために</p>
  <p class="pe-fix__good">✓ <ruby>健康<rt>けんこう</rt></ruby><b>の</b>ために — ot ために oldida の oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>勉強<rt>べんきょう</rt></ruby>しますために</p>
  <p class="pe-fix__good">✓ <ruby>勉強<rt>べんきょう</rt></ruby>する<b>ために</b> — lugʻat shakli, ます emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Kanjini unutmasligim uchun» — qaysi biri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>忘<rt>わす</rt></ruby>れないように</b> — inkor irodadan tashqarida, demak ように.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Mashina sotib olish uchun ishlayman» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>車<rt>くるま</rt></ruby>を<ruby>買<rt>か</rt></ruby>うために<ruby>働<rt>はたら</rt></ruby>きます</b> — sotib olish men qiladigan ish.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Sogʻliq uchun» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>健康<rt>けんこう</rt></ruby>のために</b> — ot bilan <b>の</b> kerak.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>読<rt>よ</rt></ruby>めるように» va «<ruby>読<rt>よ</rt></ruby>むために» — farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisi — <b>qobiliyat</b> («oʻqiy olishim uchun»), ikkinchisi — <b>ish</b> («oʻqish uchun»). Qobiliyat boshqarilmaydi, shuning uchun ように.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «<ruby>事故<rt>じこ</rt></ruby>のために<ruby>遅<rt>おく</rt></ruby>れました» — bu maqsadmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yoʻq, <b>sabab</b>. Hodisa maqsad boʻla olmaydi — va u oʻtmishda turibdi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜ために</b> — …ish uchun (irodam yetadi)</li>
  <li><b>〜ように</b> — …sin deb (irodam yetmaydi)</li>
  <li><b>〜ないように</b> — …masin deb</li>
  <li><b>〜ようにしています</b> — …ishga harakat qilaman</li>
  <li><b><ruby>健康<rt>けんこう</rt></ruby></b> — sogʻliq</li>
  <li><b><ruby>将来<rt>しょうらい</rt></ruby></b> — kelajak</li>
  <li><b><ruby>野菜<rt>やさい</rt></ruby></b> — sabzavot</li>
  <li><b><ruby>夢<rt>ゆめ</rt></ruby></b> — orzu, tush</li>
  <li><b><ruby>看護師<rt>かんごし</rt></ruby></b> — hamshira</li>
  <li><b><ruby>貯<rt>た</rt></ruby>める</b> — jamgʻarmoq (II guruh)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Bitta savol: <b>irodam yetadimi?</b> Ha — ために, yoʻq — ように.</li>
    <li><b>Inkor va potensial shakl doim ように</b>.</li>
    <li>Ot ために oldida <b>の</b> oladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-57: 〜ようになります va 〜ことにします — oʻzgarish va qaror",
        "category": "japanese",
        "order": 57,
        "summary": (
            "Yapon tilining eng yaponcha juftligi: なる (oʻzi shunday "
            "boʻldi) va する (men shunday qildim). Va nihoyat なる "
            "feʼlining oʻzi."
        ),
        "stories": ["はなせる ように なった"],
        "content": """
<h2>PJ-57: 〜ようになります va 〜ことにします — oʻzgarish va qaror</h2>

<p>Yapon tilida ikkita feʼl butun tilni ikkiga boʻlib turadi:</p>

<p><b>する</b> — <em>men qilaman</em>. Iroda, qaror, tanlov.<br>
<b>なる</b> — <em>shunday boʻladi</em>. Oʻzgarish, natija, tabiiy yoʻl.</p>

<p>Bugun ikkalasini ham oʻrganasiz, va bir narsani sezasiz:
<b>yapon tili imkoni boricha なる ni tanlaydi</b> — hatto qaror
odam tomonidan qilingan boʻlsa ham.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>なる feʼlini sifat va ot bilan ishlatasiz</li>
    <li>〜ようになります — «…adigan boʻldim» ni yasaysiz</li>
    <li>〜ことにします — «qaror qildim» ni yasaysiz</li>
    <li>〜ことになります nega boshqa maʼno berishini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki yoʻl</span>
  <span class="pe-chip pe-chip--v">する — men qildim</span>
  <span class="pe-op">↔</span>
  <span class="pe-chip pe-chip--s">なる — shunday boʻldi</span>
</div>

<h3>1. Avval なる ning oʻzi</h3>

<p>なる — «boʻlmoq», «aylanmoq». U I guruh feʼli va uch xil
qoʻshiladi. Bu yerda ham oʻsha tanish uch yoʻl:</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Qoida</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">い → <b>く</b> + なる</td>
      <td class="pj-res"><ruby>寒<rt>さむ</rt></ruby>くなります</td><td class="pj-uz">sovuq boʻladi</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">+ <b>に</b> + なる</td>
      <td class="pj-res"><ruby>元気<rt>げんき</rt></ruby>になります</td><td class="pj-uz">tuzalib ketadi</td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-end">+ <b>に</b> + なる</td>
      <td class="pj-res"><ruby>先生<rt>せんせい</rt></ruby>になります</td><td class="pj-uz">oʻqituvchi boʻladi</td></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-end">+ <b>ように</b> + なる</td>
      <td class="pj-res"><ruby>話<rt>はな</rt></ruby>せるようになります</td><td class="pj-uz">gapira oladigan boʻladi</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «boʻlmoq» ham aynan shunday tarqaladi.</b>
  «Sovuq <em>boʻldi</em>», «sogʻlom <em>boʻldi</em>»,
  «oʻqituvchi <em>boʻldi</em>», «gapiradigan <em>boʻldi</em>» —
  toʻrtta boshqa qurilma, bitta feʼl. Yaponchada ham bitta
  feʼl: <b>なる</b>. Faqat unga ulanish uchun sifat
  <b>く</b> ga, ot <b>に</b> ga, feʼl esa <b>ように</b> ga
  tayanadi. Oʻzbekchada bu ulanishlar koʻrinmaydi, yaponchada
  koʻrinadi — shuning uchun jadvalni bir marta yodlab
  qoʻyish kerak.</p>
</div>

<p>Bu farqni koʻrish uchun bitta oddiy tekshiruv bor:
gapni «kim qildi?» degan savol bilan sinang. «Sovuq
boʻldi» — kim qildi? Hech kim. «Oʻqituvchi boʻldi» — kim
qildi? Yana hech kim: u <em>boʻldi</em>, uni hech kim
qilmadi. Aynan shu sababdan bu gaplarning hammasida なる
turadi. Agar savolga «men» deb javob bera olsangiz, unda
gapda <b>する</b> boʻlishi kerak — va bu tekshiruv butun
darsning qolgan qismida ham ishlaydi.</p>

<h3>2. 〜ようになります — «…adigan boʻldim»</h3>

<p>Bu qolip <b>qobiliyat yoki odatdagi oʻzgarish</b>ni
bildiradi: ilgari boʻlmagan edi, endi bor.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>日本語<rt>にほんご</rt></ruby>が<ruby>話<rt>はな</rt></ruby>せるようになりました。</p>
  <p class="pe-ex__uz">Yaponcha gapiradigan boʻldim.</p>
  <p class="pe-ex__why">Potensial shakl + ようになる — eng koʻp uchraydigan ishlatilishi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>野菜<rt>やさい</rt></ruby>を<ruby>食<rt>た</rt></ruby>べるようになりました。</p>
  <p class="pe-ex__uz">Sabzavot yeydigan boʻldim.</p>
  <p class="pe-ex__why">Qobiliyat emas, <b>odat</b> oʻzgardi. Ilgari yemas edim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>«-adigan boʻldim» — bu qolipning oʻzbekcha nusxasi.</b>
  Diqqat qiling: oʻzbekcha ham bu yerda ikkita boʻlak ishlatadi
  — «gapira<em>digan</em>» (sifatdosh) + «<em>boʻldim</em>».
  Yaponchada ham ikkita: <b>ように</b> + <b>なる</b>. Ikkala
  tilda ham oddiy «gapirdim» yetarli emas, chunki gap
  <em>ishning oʻzi</em> haqida emas, <em>oʻzgarish</em>
  haqida.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Inkorda ように koʻpincha tushib qoladi.</b>
  «Yemaydigan boʻldim» — odatda
  <ruby>食<rt>た</rt></ruby>べ<b>なくなりました</b>, yaʼni
  ない → なく + なる. «<ruby>食<rt>た</rt></ruby>べないように
  なりました» ham uchraydi, lekin birinchisi ancha
  tabiiyroq.</p>
</div>

<p>Bu qolipning kuchi shundaki, u <b>vaqtni ichiga
oladi</b>. «Gapiraman» degan gap bir nuqtani aytadi;
«gapiradigan boʻldim» esa butun bir yoʻlni — ilgari
boʻlmagan, oradan vaqt oʻtgan, endi bor. Shuning uchun
yaponlar oʻzlari haqida gapirganda bu qolipni juda koʻp
ishlatadi: u maqtanchoqlik emas, chunki gapning egasi
<em>oʻzgarish</em>, odam emas.</p>

<h3>3. 〜ことにします — «qaror qildim»</h3>

<p>Bu — <b>sizning</b> qaroringiz. Lugʻat shakli yoki ない-shakli
ustiga <b>ことにする</b> qoʻyiladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">Tasdiq</td><td class="pj-res"><ruby>毎日<rt>まいにち</rt></ruby><ruby>走<rt>はし</rt></ruby>ることにしました</td>
      <td class="pj-uz">har kuni yugurishga qaror qildim</td></tr>
  <tr><td class="pj-stem">Inkor</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>かないことにしました</td>
      <td class="pj-uz">bormaslikka qaror qildim</td></tr>
  <tr><td class="pj-stem">Davomiy</td><td class="pj-res"><ruby>毎朝<rt>まいあさ</rt></ruby><ruby>読<rt>よ</rt></ruby>むことにしています</td>
      <td class="pj-uz">har kuni ertalab oʻqishni odat qilganman</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>ことにしました va ことにしています farqi.</b>
  Birinchisi — qaror <em>qilingan payt</em>ga ishora qiladi
  («oʻshanda qaror qildim»). Ikkinchisi — qaror hali ham
  <em>kuchda</em> ekanini aytadi («shunday qilib
  yuraman»). PJ-31 dagi ています ning oʻsha ishi.</p>
</div>

<h3>4. 〜ことになります — qaror meniki emas</h3>

<p>する oʻrniga なる qoʻysangiz, qaror <b>sizdan chiqmaydi</b>:
uni maktab, kompaniya, oila yoki shart-sharoit qiladi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">ことにしました</p>
    <p><ruby>来月<rt>らいげつ</rt></ruby><ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くことにしました。</p>
    <p>Men qaror qildim.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">ことになりました</p>
    <p><ruby>来月<rt>らいげつ</rt></ruby><ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くことになりました。</p>
    <p>Shunday boʻlib qoldi — ishxona yubordi, hujjat chiqdi.</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Va mana yaponcha odob.</b> Koʻp hollarda qarorni
  aslida <em>oʻzingiz</em> qilgan boʻlsangiz ham,
  <b>ことになりました</b> deyiladi. Sababi: «men qaror qildim»
  degan gap yaponchada oʻzini oldinga surishdek eshitiladi.
  Toʻy, ish oʻzgarishi, koʻchish — bularning hammasi
  yaponchada «shunday boʻlib qoldi» deb eʼlon qilinadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>来年<rt>らいねん</rt></ruby><ruby>結婚<rt>けっこん</rt></ruby>することになりました。</p>
  <p class="pe-ex__uz">Kelasi yili turmush quradigan boʻldik.</p>
  <p class="pe-ex__why">Qarorni ular qilgan, lekin yaponchada shunday eʼlon qilinadi — kamtarlik shunday ishlaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham xuddi shu kamtarlik bor.</b>
  «Kelasi yili toʻy <em>boʻladigan boʻldik</em>»,
  «Toshkentga <em>koʻchadigan boʻldik</em>» — siz bu gaplarda
  ham qarorni oʻzingizga olmayapsiz. «Men qaror qildim» deb
  aytish ikkala tilda ham quruqroq va qattiqroq eshitiladi.
  Farqi shundaki, yaponchada bu tanlov emas —
  <b>deyarli qoida</b>.</p>
</div>

<h3>5. Uchalasi bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Kim qiladi</th><th>Nimani bildiradi</th></tr>
  <tr><td class="pj-stem">〜ようになる</td><td class="pj-uz">hech kim — oʻzi</td>
      <td class="pj-res">qobiliyat yoki odat oʻzgardi</td></tr>
  <tr><td class="pj-stem">〜ことにする</td><td class="pj-uz">men</td>
      <td class="pj-res">qaror qildim</td></tr>
  <tr><td class="pj-stem">〜ことになる</td><td class="pj-uz">boshqa kuch (yoki kamtarlik)</td>
      <td class="pj-res">shunday boʻlib qoldi</td></tr>
  <tr><td class="pj-stem">〜ようにする</td><td class="pj-uz">men</td>
      <td class="pj-res">shunday boʻlishiga harakat qilaman (PJ-56)</td></tr>
</table></div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">決</span>
    <span class="pj-kanji__uz">hal qilmoq</span>
    <span class="pj-kanji__on">オン: ケツ</span>
    <span class="pj-kanji__kun">KUN: き(める), き(まる)</span>
    <span class="pj-kanji__note">決める (きめる) — hal qilmoq · 決まる (きまる) — hal boʻlmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">変</span>
    <span class="pj-kanji__uz">oʻzgarish; gʻalati</span>
    <span class="pj-kanji__on">オン: ヘン</span>
    <span class="pj-kanji__kun">KUN: か(わる), か(える)</span>
    <span class="pj-kanji__note">変わる (かわる) — oʻzgarmoq · 大変 (たいへん) — ogʻir, juda</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b><ruby>決<rt>き</rt></ruby>める / <ruby>決<rt>き</rt></ruby>まる ham oʻsha juftlik.</b>
  <ruby>決<rt>き</rt></ruby>める — men hal qilaman (する tomoni),
  <ruby>決<rt>き</rt></ruby>まる — hal boʻladi (なる tomoni).
  Yapon tilida bunday juftliklar oʻnlab, va ularning barchasi
  ayni shu chiziq boʻyicha ajraladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>寒<rt>さむ</rt></ruby>いになります</p>
  <p class="pe-fix__good">✓ <ruby>寒<rt>さむ</rt></ruby><b>く</b>なります — い-sifat く ga tushadi, に olmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>先生<rt>せんせい</rt></ruby>くなります</p>
  <p class="pe-fix__good">✓ <ruby>先生<rt>せんせい</rt></ruby><b>に</b>なります — ot に oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>話<rt>はな</rt></ruby>せるになりました</p>
  <p class="pe-fix__good">✓ <ruby>話<rt>はな</rt></ruby>せる<b>ように</b>なりました — feʼl ように orqali ulanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>きますことにしました</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>く<b>ことにしました</b> — こと ot, demak oldida oddiy shakl (PJ-48).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «<ruby>寒<rt>さむ</rt></ruby>い» ni なる bilan ulang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>寒<rt>さむ</rt></ruby>くなります</b> — い-sifat <b>く</b> ga tushadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «<ruby>先生<rt>せんせい</rt></ruby>» ni なる bilan ulang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>先生<rt>せんせい</rt></ruby>になります</b> — ot <b>に</b> oladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Yaponcha gapiradigan boʻldim» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>日本語<rt>にほんご</rt></ruby>が<ruby>話<rt>はな</rt></ruby>せるようになりました</b> — potensial shakl + ように + なる.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>行<rt>い</rt></ruby>くことにしました» va «<ruby>行<rt>い</rt></ruby>くことになりました» — farqi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisida <b>men</b> qaror qildim; ikkinchisida <b>shunday boʻlib qoldi</b> — yoki men kamtarlik qilyapman.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega yaponlar toʻy haqida «<ruby>結婚<rt>けっこん</rt></ruby>することになりました» deydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki «men qaror qildim» degan gap <b>oʻzini oldinga surishdek</b> eshitiladi. なる — kamtarlik. Oʻzbekcha «toʻy boʻladigan boʻldik» ham xuddi shunday.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>なる</b> — boʻlmoq (I guruh)</li>
  <li><b>〜ようになる</b> — …adigan boʻlmoq</li>
  <li><b>〜ことにする</b> — qaror qilmoq</li>
  <li><b>〜ことになる</b> — shunday boʻlib qolmoq</li>
  <li><b><ruby>決<rt>き</rt></ruby>める</b> — hal qilmoq (II guruh)</li>
  <li><b><ruby>変<rt>か</rt></ruby>わる</b> — oʻzgarmoq (I guruh)</li>
  <li><b><ruby>結婚<rt>けっこん</rt></ruby></b> — turmush qurish</li>
  <li><b><ruby>来月<rt>らいげつ</rt></ruby></b> — kelasi oy</li>
  <li><b><ruby>最初<rt>さいしょ</rt></ruby></b> — boshida, avval</li>
  <li><b><ruby>少<rt>すこ</rt></ruby>しずつ</b> — asta-sekin</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>なる ga ulanish: い-sifat <b>く</b> · ot <b>に</b> · feʼl <b>ように</b>.</li>
    <li>する = <b>men qildim</b>; なる = <b>shunday boʻldi</b>.</li>
    <li>Yapon tili shubha boʻlsa <b>なる</b> ni tanlaydi — bu kamtarlik.</li>
  </ul>
</div>
""",
    },
]
