# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-46, PJ-47, PJ-48 (Block D: gapni bogʻlash).

Uchalasi bitta ipga tizilgan: PJ-45 oddiy shaklni berdi, endi u gapning
ICHIGA kiradi. PJ-46 va PJ-47 da oddiy shakl と dan oldin turadi (u yerda
だ SAQLANADI), PJ-48 da esa otdan oldin turadi (u yerda だ → な / の).
Shu ikki qoidaning farqi — batchning asosiy oʻqitish nuqtasi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_46_48.py --author=prime
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
        "title": "PJ-46: 〜と思います — fikr bildirish",
        "category": "japanese",
        "order": 46,
        "summary": (
            "Yaponchada «menimcha» gap boshida emas, gap oxirida turadi. "
            "Bir qolip — oddiy shakl + と + 思います — va siz nihoyat oʻz "
            "fikringizni aytishingiz mumkin."
        ),
        "stories": ["ムニラさんは おこっていると おもった"],
        "content": """
<h2>PJ-46: 〜と<ruby>思<rt>おも</rt></ruby>います — fikr bildirish</h2>

<p>Qirq besh dars davomida siz <em>faktlarni</em> aytdingiz:
«bu kitob», «men bordim», «bu xona tinch». Lekin odam kuniga oʻn marta
fakt emas, <b>fikr</b> aytadi: <em>menimcha</em>, <em>oʻylashimcha</em>,
<em>shekilli</em>.</p>

<p>Yaponchada buning uchun bitta qolip bor, va u boshqa hech nimaga
oʻxshamaydi: <b>«menimcha» gapning boshida emas, oxirida turadi</b>.
Avval fikringizni toʻliq aytasiz, keyin uning ustiga
«… deb oʻylayman» degan qopqoqni qoʻyasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>〜と<ruby>思<rt>おも</rt></ruby>います qolipini tuzasiz</li>
    <li>と dan oldin nima turishini aniq bilasiz — va nega だ tushmasligini</li>
    <li>Inkorni toʻgʻri joyga qoʻyasiz</li>
    <li><ruby>思<rt>おも</rt></ruby>います va <ruby>思<rt>おも</rt></ruby>っています farqini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Fikr bildirish</span>
  <span class="pe-chip pe-chip--s"><ruby>普通体<rt>ふつうたい</rt></ruby></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">と</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v"><ruby>思<rt>おも</rt></ruby>います</span>
</div>

<h3>1. と — «deb» degan soʻz</h3>

<p>Qolipdagi <b>と</b> — PJ-19 dagi «va» maʼnosidagi と emas. Bu boshqa
qoʻshimcha (<ruby>助詞<rt>じょし</rt></ruby>), nomi
<b><ruby>引用<rt>いんよう</rt></ruby>の と</b> — «keltirish と si». U
oʻzidan oldingi butun gapni olib, uni bitta boʻlakka aylantiradi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>明日<rt>あした</rt></ruby><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>る</span>
  <span class="pj-joshi__p">と<small>DEB</small></span>
  <span class="pj-joshi__v"><ruby>思<rt>おも</rt></ruby>います</span>
  <span class="pj-joshi__uz">Ertaga yomgʻir yogʻadi <b>deb</b> oʻylayman.</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu qolip oʻzbekchaning aynan oʻzi.</b> Siz ham «Ertaga yomgʻir
  yogʻadi <em>deb</em> oʻylayman» deysiz — fikr avval, «deb oʻylayman»
  keyin. Ingliz tilida esa tartib teskari boʻladi. Shuning uchun bu
  qolip sizga koʻpchilikdan oson tushadi: と — bu oʻzbekcha
  <b>«deb»</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>本<rt>ほん</rt></ruby>は<ruby>面白<rt>おもしろ</rt></ruby>いと<ruby>思<rt>おも</rt></ruby>います。</p>
  <p class="pe-ex__uz">Bu kitob qiziqarli deb oʻylayman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>先生<rt>せんせい</rt></ruby>はもう<ruby>帰<rt>かえ</rt></ruby>ったと<ruby>思<rt>おも</rt></ruby>います。</p>
  <p class="pe-ex__uz">Oʻqituvchi allaqachon ketgan deb oʻylayman.</p>
  <p class="pe-ex__why">と dan oldin <b><ruby>帰<rt>かえ</rt></ruby>った</b> — oddiy shaklning oʻtgan zamoni (PJ-35).</p>
</div>

<h3>2. と dan oldin doim oddiy shakl</h3>

<p>Mana nega PJ-45 aynan shu darsdan oldin turgan edi. と dan oldingi
qism — gapning <em>ichi</em>, va yapon tilida gapning ichida hech qachon
です・ます turmaydi. Muloyimlik faqat eng oxirgi feʼlda koʻrinadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Nima demoqchisiz</th><th>Oddiy shaklga</th><th>Toʻliq gap</th></tr>
  <tr><td class="pj-stem"><ruby>行<rt>い</rt></ruby>きます</td><td class="pj-end"><ruby>行<rt>い</rt></ruby>く</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>くと<ruby>思<rt>おも</rt></ruby>います</td></tr>
  <tr><td class="pj-stem"><ruby>行<rt>い</rt></ruby>きません</td><td class="pj-end"><ruby>行<rt>い</rt></ruby>かない</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>かないと<ruby>思<rt>おも</rt></ruby>います</td></tr>
  <tr><td class="pj-stem"><ruby>行<rt>い</rt></ruby>きました</td><td class="pj-end"><ruby>行<rt>い</rt></ruby>った</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>ったと<ruby>思<rt>おも</rt></ruby>います</td></tr>
  <tr><td class="pj-stem"><ruby>行<rt>い</rt></ruby>きませんでした</td><td class="pj-end"><ruby>行<rt>い</rt></ruby>かなかった</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>かなかったと<ruby>思<rt>おも</rt></ruby>います</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Gapning tashqi kiyimi bitta.</b> Siz kimga gapirayotgan
  boʻlsangiz ham, <ruby>思<rt>おも</rt></ruby>います qismi oʻzgaradi
  — doʻstingizga <ruby>思<rt>おも</rt></ruby>う, ustozingizga
  <ruby>思<rt>おも</rt></ruby>います. と dan oldingi qism esa
  <em>hech qachon</em> oʻzgarmaydi.</p>
</div>

<h3>3. Ot va な-sifat: だ TUSHMAYDI</h3>

<p>Mana darsning eng koʻp xato qilinadigan joyi. PJ-45 da siz
だ ogʻzaki nutqda koʻpincha tushib qolishini oʻrgandingiz:
<ruby>学生<rt>がくせい</rt></ruby>？ deb soʻrash mumkin edi.</p>

<p><b>と dan oldin esa だ hech qachon tushmaydi.</b> Chunki bu yerda だ
— muloyimlik emas, <em>yopishtiruvchi</em>: ot bilan と ni bir-biriga
ulab turgan boʻlak. Uni olib tashlasangiz, gap qoʻlda ushlanmay
qoladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>と dan oldin</th><th>Misol</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-end">oddiy shakl</td>
      <td class="pj-res"><ruby>来<rt>く</rt></ruby>ると<ruby>思<rt>おも</rt></ruby>います</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">oʻzi, だ <b>YOʻQ</b></td>
      <td class="pj-res"><ruby>高<rt>たか</rt></ruby>いと<ruby>思<rt>おも</rt></ruby>います</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">+ <b>だ</b></td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かだと<ruby>思<rt>おも</rt></ruby>います</td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-end">+ <b>だ</b></td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>います</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>い-sifat yana istisno.</b> <ruby>高<rt>たか</rt></ruby>い<s>だ</s>と
  — notoʻgʻri. Sabab PJ-45 dagi bilan bir xil: い-sifat oʻzi kesim boʻla
  oladi, unga boglama kerak emas. Uchta soʻz turidan faqat
  <b>ikkitasi</b> だ oladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu yerda hech nima turmaydi.</b> Siz «U talaba
  <em>deb</em> oʻylayman» deysiz — «talaba» bilan «deb» orasi boʻsh.
  Yaponcha esa oʻsha boʻshliqqa <b>だ</b> qoʻyadi, chunki yapon gapi
  kesimsiz tugay olmaydi: ot oʻzi kesim boʻla olmaydi, unga boglama
  kerak. Shuning uchun «<ruby>学生<rt>がくせい</rt></ruby>と<ruby>思<rt>おも</rt></ruby>います»
  — yarim gap, va u yaponning qulogʻiga chala eshitiladi. Bu qoidani
  yodlashning oson yoʻli: <em>い bilan tugagan sifat だ olmaydi, qolgan
  hammasi oladi</em>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">イノムさんは<ruby>元気<rt>げんき</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>います。</p>
  <p class="pe-ex__uz">Inom sogʻ-salomat deb oʻylayman.</p>
  <p class="pe-ex__why"><ruby>元気<rt>げんき</rt></ruby> — な-sifat, demak <b>だ</b>.</p>
</div>

<h3>4. Inkor qayerga tushadi</h3>

<p>«Menimcha u kelmaydi» degan fikrni yaponchada ikki xil tuzish
mumkin, va ikkisi <em>bir xil narsani anglatmaydi</em>.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">ODATDAGI YOʻL</p>
    <p><ruby>来<rt>こ</rt></ruby>ないと<ruby>思<rt>おも</rt></ruby>います</p>
    <p>«Kelmaydi deb oʻylayman.» Inkor <b>ichkarida</b>. Kundalik nutqda
    deyarli doim shu.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">KAMROQ UCHRAYDI</p>
    <p><ruby>来<rt>く</rt></ruby>ると<ruby>思<rt>おも</rt></ruby>いません</p>
    <p>«Keladi deb oʻylamayman.» Inkor <b>tashqarida</b> — ancha
    qatʼiyroq, deyarli eʼtiroz.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ham xuddi shunday ikki xil.</b> «Kelmaydi deb
  oʻylayman» — yumshoq taxmin. «Keladi deb oʻylamayman» — birovning
  gapiga eʼtiroz. Farqni allaqachon his qilasiz; faqat yaponchada ham
  aynan shu farq borligini bilib qoʻying.</p>
</div>

<h3>5. Ichkaridagi zamon mustaqil</h3>

<p>Gapning ichidagi zamon <b>oʻz ishini qiladi</b> va oxiridagi
<ruby>思<rt>おも</rt></ruby>います ga qarab oʻzgarmaydi. Ichkarida —
voqeaning zamoni; tashqarida — oʻylash zamoni.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>昨日<rt>きのう</rt></ruby><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったと<ruby>思<rt>おも</rt></ruby>います。</p>
  <p class="pe-ex__uz">Kecha yomgʻir yoqqan deb oʻylayman.</p>
  <p class="pe-ex__why">Voqea — oʻtgan zamonda; oʻylash — hozir.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>試験<rt>しけん</rt></ruby>は<ruby>難<rt>むずか</rt></ruby>しくなかったと<ruby>思<rt>おも</rt></ruby>います。</p>
  <p class="pe-ex__uz">Imtihon qiyin boʻlmagan deb oʻylayman.</p>
</div>

<h3>6. <ruby>思<rt>おも</rt></ruby>います va <ruby>思<rt>おも</rt></ruby>っています</h3>

<p>PJ-31 da siz 〜ています ni oʻrgangansiz: davom etayotgan ish yoki
turgʻun holat. <ruby>思<rt>おも</rt></ruby>う bilan u ikki joyda
kerak boʻladi.</p>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name"><ruby>思<rt>おも</rt></ruby>います</span>
    <span class="pj-level__ja"><ruby>私<rt>わたし</rt></ruby>は…と<ruby>思<rt>おも</rt></ruby>います</span>
    <span class="pj-level__who">MENING fikrim, xuddi hozir aytilyapti</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name"><ruby>思<rt>おも</rt></ruby>っています</span>
    <span class="pj-level__ja">ラノさんは…と<ruby>思<rt>おも</rt></ruby>っています</span>
    <span class="pj-level__who">BOSHQA odamning fikri, yoki ancha vaqtdan beri</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>Nega boshqa odam uchun ています kerak?</b> Chunki siz birovning
  miyasiga kira olmaysiz. <ruby>思<rt>おも</rt></ruby>っています —
  «u shunday fikrda turibdi», yaʼni siz koʻrgan <em>holat</em>ni
  aytyapsiz, uning ichidagi ovozni emas. PJ-39 dagi 〜たい ham xuddi shu
  sababdan boshqa odam uchun 〜たがっています boʻladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">パリさんは<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きたいと<ruby>思<rt>おも</rt></ruby>っています。</p>
  <p class="pe-ex__uz">Pari Yaponiyaga bormoqchi (shunday fikrda).</p>
</div>

<h3>7. Soʻrash: どう<ruby>思<rt>おも</rt></ruby>いますか</h3>

<p>Birovning fikrini soʻrash uchun <b>どう</b> ishlatiladi —
«qanday», «qanaqa» (PJ-18).</p>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>映画<rt>えいが</rt></ruby>についてどう<ruby>思<rt>おも</rt></ruby>いますか。</p>
  <p class="pe-ex__uz">Bu kino haqida qanday fikrdasiz?</p>
  <p class="pe-ex__why">«<ruby>何<rt>なに</rt></ruby>を<ruby>思<rt>おも</rt></ruby>いますか» deyilmaydi — fikr «nima» emas, «qanday».</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">思</span>
    <span class="pj-kanji__uz">oʻylamoq, fikr</span>
    <span class="pj-kanji__on">オン: シ</span>
    <span class="pj-kanji__kun">KUN: おも(う)</span>
    <span class="pj-kanji__note">思う (おもう) — oʻylamoq · 思い出 (おもいで) — xotira</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">考</span>
    <span class="pj-kanji__uz">mulohaza qilmoq</span>
    <span class="pj-kanji__on">オン: コウ</span>
    <span class="pj-kanji__kun">KUN: かんが(える)</span>
    <span class="pj-kanji__note">考える (かんがえる) — bosh qotirmoq, hisoblab koʻrmoq</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b><ruby>思<rt>おも</rt></ruby>う va <ruby>考<rt>かんが</rt></ruby>える bir xil emas.</b>
  <ruby>思<rt>おも</rt></ruby>う — yurakdan chiqqan fikr, taxmin,
  tuygʻu. <ruby>考<rt>かんが</rt></ruby>える — boshda qilingan ish:
  hisoblash, rejalashtirish, oʻylab koʻrish. «Menimcha yaxshi» —
  <ruby>思<rt>おも</rt></ruby>う. «Ikki kun oʻylab koʻraman» —
  <ruby>考<rt>かんが</rt></ruby>える.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>きますと<ruby>思<rt>おも</rt></ruby>います</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>くと<ruby>思<rt>おも</rt></ruby>います — と dan oldin <b>hech qachon</b> です・ます turmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>と<ruby>思<rt>おも</rt></ruby>います</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>だ</b>と<ruby>思<rt>おも</rt></ruby>います — ot va な-sifat だ ni saqlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>高<rt>たか</rt></ruby>いだと<ruby>思<rt>おも</rt></ruby>います</p>
  <p class="pe-fix__good">✓ <ruby>高<rt>たか</rt></ruby>いと<ruby>思<rt>おも</rt></ruby>います — い-sifatga だ qoʻshilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ラノさんは<ruby>行<rt>い</rt></ruby>きたいと<ruby>思<rt>おも</rt></ruby>います</p>
  <p class="pe-fix__good">✓ ラノさんは<ruby>行<rt>い</rt></ruby>きたいと<ruby>思<rt>おも</rt></ruby>っています — boshqa odamning fikri ています bilan.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «<ruby>明日<rt>あした</rt></ruby>は<ruby>暑<rt>あつ</rt></ruby>いです» — buni fikrga aylantiring.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>明日<rt>あした</rt></ruby>は<ruby>暑<rt>あつ</rt></ruby>いと<ruby>思<rt>おも</rt></ruby>います</b> — い-sifat, です tushadi va だ qoʻshilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «この<ruby>部屋<rt>へや</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かです» — buni fikrga aylantiring.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>この<ruby>部屋<rt>へや</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かだと<ruby>思<rt>おも</rt></ruby>います</b> — な-sifat, demak <b>だ</b> saqlanadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Menimcha u kecha kelmagan» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>昨日<rt>きのう</rt></ruby><ruby>来<rt>こ</rt></ruby>なかったと<ruby>思<rt>おも</rt></ruby>います</b> — ichkarida oʻtgan zamon inkori (PJ-45).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>来<rt>こ</rt></ruby>ないと<ruby>思<rt>おも</rt></ruby>います va <ruby>来<rt>く</rt></ruby>ると<ruby>思<rt>おも</rt></ruby>いません — qaysi biri kundalik nutqda koʻproq?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>来<rt>こ</rt></ruby>ないと<ruby>思<rt>おも</rt></ruby>います</b> — inkor ichkarida. Ikkinchisi eʼtirozdek eshitiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «ムニラさんは<ruby>先生<rt>せんせい</rt></ruby>になりたいと<ruby>思<rt>おも</rt></ruby>います» — nima xato?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><ruby>思<rt>おも</rt></ruby><b>っています</b> boʻlishi kerak — bu <em>boshqa odamning</em> fikri.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>思<rt>おも</rt></ruby>う</b> — oʻylamoq (I guruh)</li>
  <li><b><ruby>考<rt>かんが</rt></ruby>える</b> — mulohaza qilmoq (II guruh)</li>
  <li><b>と</b> — «deb» (<ruby>引用<rt>いんよう</rt></ruby>の と)</li>
  <li><b>どう<ruby>思<rt>おも</rt></ruby>いますか</b> — qanday fikrdasiz?</li>
  <li><b><ruby>面白<rt>おもしろ</rt></ruby>い</b> — qiziqarli</li>
  <li><b><ruby>難<rt>むずか</rt></ruby>しい</b> — qiyin</li>
  <li><b><ruby>試験<rt>しけん</rt></ruby></b> — imtihon</li>
  <li><b><ruby>元気<rt>げんき</rt></ruby></b> — sogʻ-salomat, tetik (な-sifat)</li>
  <li><b><ruby>映画<rt>えいが</rt></ruby></b> — kino</li>
  <li><b><ruby>部屋<rt>へや</rt></ruby></b> — xona</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>と — oʻzbekcha <b>«deb»</b>. Fikr avval, <ruby>思<rt>おも</rt></ruby>います keyin.</li>
    <li>と dan oldin <b>oddiy shakl</b>, va ot bilan な-sifat <b>だ</b> ni saqlaydi.</li>
    <li>Boshqa odamning fikri — <b><ruby>思<rt>おも</rt></ruby>っています</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-47: 〜と言いました va koʻchirma gap",
        "category": "japanese",
        "order": 47,
        "summary": (
            "Birovning gapini qaytarishning ikki yoʻli. Eng muhimi: "
            "yaponchada — oʻzbekchadagidek — koʻchirma gapning zamoni "
            "siljimaydi."
        ),
        "stories": ["きたかぜと たいよう"],
        "content": """
<h2>PJ-47: 〜と<ruby>言<rt>い</rt></ruby>いました va koʻchirma gap</h2>

<p>Oʻtgan darsda siz <em>oʻz</em> fikringizni aytdingiz. Bugun
<em>birovning</em> gapini qaytarasiz — va qolip deyarli oʻsha-oʻsha
boʻlib chiqadi. <ruby>思<rt>おも</rt></ruby>います oʻrniga
<ruby>言<rt>い</rt></ruby>いました qoʻyiladi, xolos.</p>

<p>Lekin bitta muhim tanlov paydo boʻladi: gapni <b>aynan
qaytarasizmi</b>, yoki <b>oʻz soʻzingiz bilan</b>? Yapon tili bu ikkisini
tinish belgilari bilan ajratadi va oʻrtasida chalkashish yoʻq.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Koʻchirma gapni 「」 va と bilan yozasiz</li>
    <li>Oʻzlashtirilgan gapni oddiy shakl bilan tuzasiz</li>
    <li>Zamon nega siljimasligini tushunasiz</li>
    <li><ruby>言<rt>い</rt></ruby>いました va <ruby>言<rt>い</rt></ruby>っていました farqini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Birovning gapi</span>
  <span class="pe-chip pe-chip--o">「…」 / <ruby>普通体<rt>ふつうたい</rt></ruby></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">と</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v"><ruby>言<rt>い</rt></ruby>いました</span>
</div>

<h3>1. Ikki yoʻl bir jadvalda</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">KOʻCHIRMA — <ruby>直接話法<rt>ちょくせつわほう</rt></ruby></p>
    <p>ラノさんは「<ruby>明日<rt>あした</rt></ruby><ruby>行<rt>い</rt></ruby>きます」と<ruby>言<rt>い</rt></ruby>いました。</p>
    <p>Gap <b>aynan</b> qaytariladi. 「」 ichida odamning oʻz uslubi
    saqlanadi — u です・ます da gapirgan boʻlsa, shundayligicha
    qoladi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">OʻZLASHTIRILGAN — <ruby>間接話法<rt>かんせつわほう</rt></ruby></p>
    <p>ラノさんは<ruby>明日<rt>あした</rt></ruby><ruby>行<rt>い</rt></ruby>くと<ruby>言<rt>い</rt></ruby>いました。</p>
    <p>Gap <b>mazmunan</b> qaytariladi. 「」 yoʻq, uslub yoʻqoladi,
    oldida — oddiy shakl, xuddi PJ-46 dagidek.</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Ikkalasi ham toʻgʻri, lekin ular boshqa narsani aytadi.</b>
  「」 bilan siz «u <em>shu soʻzlarni</em> aytdi» deysiz. 「」 siz esa
  «u <em>shu maʼnoni</em> aytdi». Gazeta va rasmiy hujjat birinchisini,
  kundalik suhbat ikkinchisini tanlaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Soʻz tartibi oʻzbekchanikidek.</b> Siz «<em>Ertaga kelaman</em>,
  dedi Rano» emas, «Rano <em>ertaga kelaman</em> dedi» deysiz — kim
  aytgani boshda, aytgan gapi oʻrtada, «dedi» esa oxirida. Yaponcha ham
  aynan shu uchta boʻlakni shu tartibda qoʻyadi:
  ラノさんは → 「…」 → と<ruby>言<rt>い</rt></ruby>いました. Boshqa tillarda
  «dedi» koʻpincha gap boshiga chiqadi; bu yerda u hech qachon
  chiqmaydi, chunki yapon gapi <b>doim feʼl bilan tugaydi</b>.</p>
</div>

<h3>2. Oʻzlashtirilgan gap — qoida PJ-46 niki</h3>

<p>と dan oldin nima turishini siz kecha oʻrgandingiz, va bu yerda hech
narsa oʻzgarmaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>と dan oldin</th><th>Misol</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-end">oddiy shakl</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>くと<ruby>言<rt>い</rt></ruby>いました</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">oʻzi</td>
      <td class="pj-res"><ruby>忙<rt>いそが</rt></ruby>しいと<ruby>言<rt>い</rt></ruby>いました</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">+ <b>だ</b></td>
      <td class="pj-res"><ruby>大丈夫<rt>だいじょうぶ</rt></ruby>だと<ruby>言<rt>い</rt></ruby>いました</td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-end">+ <b>だ</b></td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>だと<ruby>言<rt>い</rt></ruby>いました</td></tr>
</table></div>

<div class="pj-joshi">
  <span class="pj-joshi__n">イノムさん</span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n"><ruby>母<rt>はは</rt></ruby></span>
  <span class="pj-joshi__p">に<small>KIMGA</small></span>
  <span class="pj-joshi__n"><ruby>帰<rt>かえ</rt></ruby>る</span>
  <span class="pj-joshi__p">と<small>DEB</small></span>
  <span class="pj-joshi__v"><ruby>言<rt>い</rt></ruby>いました</span>
  <span class="pj-joshi__uz">Inom onasiga qaytaman deb aytdi.</span>
</div>

<div class="pe-call pe-tip">
  <p><b>Eshituvchi に oladi.</b> Kimga aytilgani — <b>に</b> bilan
  (PJ-21 dagi «-ga»). Kim aytgani esa は yoki が bilan. Gapda
  ikkalasi ham boʻlishi mumkin, va tartibi erkin.</p>
</div>

<p>Yaʼni PJ-46 ni oʻrgangan boʻlsangiz, bu darsning yarmini
allaqachon bilasiz. Farq faqat oxirgi feʼlda:
<ruby>思<rt>おも</rt></ruby>います oʻrniga
<ruby>言<rt>い</rt></ruby>いました. Qolgan hamma narsa — oddiy shakl,
だ ning saqlanishi, い-sifatning quruq turishi — bir xil.</p>

<p>Qaysi birini tanlash kerak degan savolga oddiy javob bor:
<b>agar odamning oʻz soʻzlari muhim boʻlsa</b> — 「」 ishlating.
Sud, gazeta, hikoya ichidagi jonli nutq shunday yoziladi. <b>Agar
faqat mazmun muhim boʻlsa</b> — 「」 siz yozing. Kundalik suhbatda
odamlar deyarli doim ikkinchisini tanlaydi, chunki hech kim birovning
gapini soʻzma-soʻz eslab qolmaydi.</p>

<h3>3. Zamon SILJIMAYDI — darsning yuragi</h3>

<p>Koʻp tillarda «U ertaga boraman dedi» degan gap qaytarilganda
ichkaridagi feʼl oʻzgaradi. <b>Yapon tilida oʻzgarmaydi.</b> Ichkaridagi
zamon aytilgan paytga qarab oʻlchanadi, siz gapirayotgan paytga
emas.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">パリさんは<ruby>明日<rt>あした</rt></ruby><ruby>来<rt>く</rt></ruby>ると<ruby>言<rt>い</rt></ruby>いました。</p>
  <p class="pe-ex__uz">Pari ertaga kelaman dedi.</p>
  <p class="pe-ex__why"><ruby>言<rt>い</rt></ruby>いました — oʻtgan zamon, lekin ichkarida <ruby>来<rt>く</rt></ruby>る — hozirgi-kelasi. Ikkisi bir-biriga qaramaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ham aynan shunday ishlaydi.</b> Siz «Ertaga
  <em>kelaman</em> dedi» deysiz — «kelardim» demaysiz. Ingliz tilida esa
  feʼl orqaga suriladi. Yaʼni bu yerda oʻzbek tili sizga toʻgʻri
  javobni bepul berib turibdi: gapning ichini <b>qanday eshitgan
  boʻlsangiz, shunday qoldiring</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>先生<rt>せんせい</rt></ruby>は<ruby>試験<rt>しけん</rt></ruby>が<ruby>終<rt>お</rt></ruby>わったと<ruby>言<rt>い</rt></ruby>いました。</p>
  <p class="pe-ex__uz">Oʻqituvchi imtihon tugadi dedi.</p>
  <p class="pe-ex__why">Bu yerda ichkarisi oʻtgan zamonda, chunki <em>gapirgan paytida ham</em> ish tugagan edi.</p>
</div>

<h3>4. 「」 ichi tegilmaydi</h3>

<p>Koʻchirma gapda odamning butun uslubi saqlanadi: muloyimligi,
soʻroq か si, hatto <ruby>敬語<rt>けいご</rt></ruby> si. Siz uni
tuzatmaysiz.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">ムニラさんは「すみません、<ruby>時間<rt>じかん</rt></ruby>がありません」と<ruby>言<rt>い</rt></ruby>いました。</p>
  <p class="pe-ex__uz">Munira «kechirasiz, vaqtim yoʻq» dedi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Tinish belgisiga eʼtibor bering.</b> Yaponchada qoʻshtirnoq —
  <b>「」</b>, hech qachon <em>«»</em> yoki ingliz qoʻshtirnogʻi emas.
  Va 「」 ichidagi gap oxiridagi 。 koʻpincha <b>yozilmaydi</b>:
  「<ruby>行<rt>い</rt></ruby>きます」と<ruby>言<rt>い</rt></ruby>いました。 —
  nuqta faqat gap oxirida.</p>
</div>

<h3>5. <ruby>言<rt>い</rt></ruby>いました va <ruby>言<rt>い</rt></ruby>っていました</h3>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name"><ruby>言<rt>い</rt></ruby>いました</span>
    <span class="pj-level__ja">…と<ruby>言<rt>い</rt></ruby>いました</span>
    <span class="pj-level__who">bir marta, aniq paytda aytdi</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name"><ruby>言<rt>い</rt></ruby>っていました</span>
    <span class="pj-level__ja">…と<ruby>言<rt>い</rt></ruby>っていました</span>
    <span class="pj-level__who">«aytgan edi» — eshitganingizni boshqaga yetkazyapsiz</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">ラノさんは<ruby>今日<rt>きょう</rt></ruby><ruby>来<rt>こ</rt></ruby>ないと<ruby>言<rt>い</rt></ruby>っていました。</p>
  <p class="pe-ex__uz">Rano bugun kelmayman degan edi.</p>
  <p class="pe-ex__why">Siz uchinchi odamga xabar yetkazyapsiz — shuning uchun ています shakli tabiiyroq.</p>
</div>

<h3>6. と boshqa feʼllar bilan ham</h3>

<p>と faqat <ruby>思<rt>おも</rt></ruby>う va
<ruby>言<rt>い</rt></ruby>う bilan emas — u <em>soʻz yoki fikr</em> bilan
ishlaydigan har qanday feʼl oldida turadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pj-stem"><ruby>言<rt>い</rt></ruby>う</td><td class="pj-uz">aytmoq</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>くと<ruby>言<rt>い</rt></ruby>いました</td></tr>
  <tr><td class="pj-stem"><ruby>聞<rt>き</rt></ruby>く</td><td class="pj-uz">eshitmoq, soʻramoq</td>
      <td class="pj-res"><ruby>来<rt>く</rt></ruby>ると<ruby>聞<rt>き</rt></ruby>きました</td></tr>
  <tr><td class="pj-stem"><ruby>書<rt>か</rt></ruby>く</td><td class="pj-uz">yozmoq</td>
      <td class="pj-res"><ruby>休<rt>やす</rt></ruby>みだと<ruby>書<rt>か</rt></ruby>きました</td></tr>
  <tr><td class="pj-stem"><ruby>思<rt>おも</rt></ruby>う</td><td class="pj-uz">oʻylamoq</td>
      <td class="pj-res"><ruby>高<rt>たか</rt></ruby>いと<ruby>思<rt>おも</rt></ruby>います</td></tr>
</table></div>

<h3>7. って — ogʻzaki nutqdagi と</h3>

<p>Doʻstlar bilan gaplashganda と oʻrniga koʻpincha <b>って</b>
aytiladi. Maʼnosi bir xil, faqat uslubi oddiy.</p>

<div class="pj-say">
  <span class="pj-say__from"><ruby>行<rt>い</rt></ruby>くと<ruby>言<rt>い</rt></ruby>っていました</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to"><ruby>行<rt>い</rt></ruby>くって</span>
  <span class="pj-say__why">ogʻzaki nutqda <ruby>言<rt>い</rt></ruby>う ham tushib qolishi mumkin</span>
</div>

<div class="pe-call pe-tip">
  <p><b>って ni yozmang, lekin taniy oling.</b> U animeda, qoʻshiqda va
  suhbatda toʻxtovsiz uchraydi. Yozma ishda, imtihonda va ustoz bilan
  esa doim <b>と</b>.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">言</span>
    <span class="pj-kanji__uz">aytmoq, soʻz</span>
    <span class="pj-kanji__on">オン: ゲン</span>
    <span class="pj-kanji__kun">KUN: い(う), こと</span>
    <span class="pj-kanji__note">言う (いう) — aytmoq · 言葉 (ことば) — soʻz, til</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">話</span>
    <span class="pj-kanji__uz">gapirmoq, suhbat</span>
    <span class="pj-kanji__on">オン: ワ</span>
    <span class="pj-kanji__kun">KUN: はな(す), はなし</span>
    <span class="pj-kanji__note">話す (はなす) — gapirmoq · 電話 (でんわ) — telefon</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b><ruby>言<rt>い</rt></ruby>う va <ruby>話<rt>はな</rt></ruby>す —
  «aytmoq» va «gapirmoq».</b> <ruby>言<rt>い</rt></ruby>う ning
  toʻldiruvchisi — <em>soʻz</em> («shunday dedi»).
  <ruby>話<rt>はな</rt></ruby>す ning toʻldiruvchisi — <em>mavzu</em>
  («yapon tilida gapiradi», «voqeani gapirib berdi»). Oʻzbekchada ham
  «gap aytdi» va «gaplashdi» bir narsa emas.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ラノさんは<ruby>行<rt>い</rt></ruby>きますと<ruby>言<rt>い</rt></ruby>いました</p>
  <p class="pe-fix__good">✓ …<ruby>行<rt>い</rt></ruby>くと… (「」 siz) yoki ✓ …「<ruby>行<rt>い</rt></ruby>きます」と… (「」 bilan). Ikkisini aralashtirmang.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>大丈夫<rt>だいじょうぶ</rt></ruby>と<ruby>言<rt>い</rt></ruby>いました</p>
  <p class="pe-fix__good">✓ <ruby>大丈夫<rt>だいじょうぶ</rt></ruby><b>だ</b>と<ruby>言<rt>い</rt></ruby>いました — な-sifat だ ni talab qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>明日<rt>あした</rt></ruby><ruby>来<rt>き</rt></ruby>たと<ruby>言<rt>い</rt></ruby>いました</p>
  <p class="pe-fix__good">✓ <ruby>明日<rt>あした</rt></ruby><ruby>来<rt>く</rt></ruby>ると<ruby>言<rt>い</rt></ruby>いました — zamon siljimaydi; «ertaga» bilan oʻtgan zamon turmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>を「ありがとう」と<ruby>言<rt>い</rt></ruby>いました</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby><b>に</b>「ありがとう」と<ruby>言<rt>い</rt></ruby>いました — eshituvchi に oladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 「<ruby>明日<rt>あした</rt></ruby><ruby>休<rt>やす</rt></ruby>みます」 ni oʻzlashtirilgan gapga aylantiring.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>明日<rt>あした</rt></ruby><ruby>休<rt>やす</rt></ruby>むと<ruby>言<rt>い</rt></ruby>いました</b> — 「」 tushadi, ichkarisi oddiy shaklga oʻtadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «<ruby>先生<rt>せんせい</rt></ruby>は<ruby>元気<rt>げんき</rt></ruby>と<ruby>言<rt>い</rt></ruby>いました» — nima yetishmayapti?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>だ</b>: <ruby>元気<rt>げんき</rt></ruby><b>だ</b>と<ruby>言<rt>い</rt></ruby>いました. <ruby>元気<rt>げんき</rt></ruby> — な-sifat.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Kimga aytilgani qaysi qoʻshimcha bilan koʻrsatiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>に</b> — <ruby>母<rt>はは</rt></ruby><b>に</b><ruby>言<rt>い</rt></ruby>いました.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Rano bugun kelmayman degan edi» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ラノさんは<ruby>今日<rt>きょう</rt></ruby><ruby>来<rt>こ</rt></ruby>ないと<ruby>言<rt>い</rt></ruby>っていました</b> — eshitganingizni yetkazyapsiz, demak ています.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega «<ruby>明日<rt>あした</rt></ruby><ruby>来<rt>く</rt></ruby>ると<ruby>言<rt>い</rt></ruby>いました» da ichkarisi oʻtgan zamonga oʻtmaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki ichkaridagi zamon <b>aytilgan paytga</b> qarab oʻlchanadi. U gapirganda «kelish» hali oldinda edi — oʻzbekchada ham «kelaman dedi».</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>言<rt>い</rt></ruby>う</b> — aytmoq (I guruh)</li>
  <li><b><ruby>話<rt>はな</rt></ruby>す</b> — gapirmoq (I guruh)</li>
  <li><b><ruby>聞<rt>き</rt></ruby>く</b> — eshitmoq, soʻramoq (I guruh)</li>
  <li><b>「」</b> — <ruby>鉤括弧<rt>かぎかっこ</rt></ruby>, yaponcha qoʻshtirnoq</li>
  <li><b>って</b> — ogʻzaki nutqdagi と</li>
  <li><b><ruby>言葉<rt>ことば</rt></ruby></b> — soʻz, til</li>
  <li><b><ruby>大丈夫<rt>だいじょうぶ</rt></ruby></b> — yaxshi, muammo yoʻq (な-sifat)</li>
  <li><b><ruby>忙<rt>いそが</rt></ruby>しい</b> — band</li>
  <li><b><ruby>終<rt>お</rt></ruby>わる</b> — tugamoq (I guruh)</li>
  <li><b><ruby>休<rt>やす</rt></ruby>む</b> — dam olmoq, dars qoldirmoq (I guruh)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>「」 — aynan qaytarish; 「」 siz oddiy shakl — mazmunan qaytarish.</li>
    <li><b>Zamon siljimaydi</b> — oʻzbekchadagidek.</li>
    <li>Eshitganingizni yetkazsangiz — <b><ruby>言<rt>い</rt></ruby>っていました</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-48: Aniqlovchi ergash gap: 私が読んだ本 — otni butun gap bilan aniqlash",
        "category": "japanese",
        "order": 48,
        "summary": (
            "Yaponchada «men kecha oʻqigan kitob» degan gap oʻzbekchadagi "
            "kabi tuziladi: aniqlovchi otdan oldin. Bitta qoida, va "
            "yapon tili birdan uzun gap yoza boshlaydi."
        ),
        "stories": ["わすれものの はこ"],
        "content": """
<h2>PJ-48: Aniqlovchi ergash gap: <ruby>私<rt>わたし</rt></ruby>が<ruby>読<rt>よ</rt></ruby>んだ<ruby>本<rt>ほん</rt></ruby></h2>

<p>Siz <ruby>高<rt>たか</rt></ruby>い<ruby>本<rt>ほん</rt></ruby>
(«qimmat kitob») deyishni PJ-25 dan beri bilasiz. Endi bitta savol:
agar «qimmat» oʻrniga butun bir gap qoʻymoqchi boʻlsangiz-chi?
<em>Men kecha kutubxonadan olgan</em> kitob.</p>

<p>Javob shunchalik oddiyki, ishonish qiyin: <b>gapni ham xuddi sifat
kabi otning oldiga qoʻyasiz</b>. Hech qanday bogʻlovchi soʻz yoʻq,
hech qanday vergul yoʻq. Faqat feʼl oddiy shaklda turadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Otni butun gap bilan aniqlaysiz</li>
    <li>Ergash gap ichida ega nega が olishini bilib olasiz</li>
    <li>Ot va な-sifatda だ nega な / の ga aylanishini koʻrasiz</li>
    <li>Uzun aniqlovchini oxiridan boshlab oʻqishni oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Aniqlovchi ergash gap</span>
  <span class="pe-chip pe-chip--s">GAP (<ruby>普通体<rt>ふつうたい</rt></ruby>)</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">OT</span>
</div>

<h3>1. Sifat qanday tursa, gap ham shunday turadi</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Aniqlovchi</th><th>Yaponcha</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem">Sifat</td><td class="pj-res"><ruby>高<rt>たか</rt></ruby>い<ruby>本<rt>ほん</rt></ruby></td>
      <td class="pj-uz">qimmat kitob</td></tr>
  <tr><td class="pj-stem">Gap</td><td class="pj-res"><ruby>私<rt>わたし</rt></ruby>が<ruby>読<rt>よ</rt></ruby>んだ<ruby>本<rt>ほん</rt></ruby></td>
      <td class="pj-uz">men oʻqigan kitob</td></tr>
  <tr><td class="pj-stem">Gap (inkor)</td><td class="pj-res"><ruby>私<rt>わたし</rt></ruby>が<ruby>読<rt>よ</rt></ruby>まない<ruby>本<rt>ほん</rt></ruby></td>
      <td class="pj-uz">men oʻqimaydigan kitob</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu — butun kursdagi eng katta sovgʻa.</b> Oʻzbek tilida ham
  aniqlovchi otdan <em>oldin</em> turadi: «men oʻqi<b>gan</b> kitob»,
  «Rano pishir<b>gan</b> osh». Koʻp tillarda esa u otdan
  <em>keyin</em> keladi va oʻrtasida maxsus bogʻlovchi olmosh talab
  qilinadi. Yaponcha bu yerda oʻzbekchaning aynan nusxasi — faqat
  «-gan» oʻrniga <b>oddiy shakl</b> turadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">これはラノさんが<ruby>作<rt>つく</rt></ruby>った<ruby>料理<rt>りょうり</rt></ruby>です。</p>
  <p class="pe-ex__uz">Bu — Rano tayyorlagan taom.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>日本語<rt>にほんご</rt></ruby>が<ruby>話<rt>はな</rt></ruby>せる<ruby>人<rt>ひと</rt></ruby>を<ruby>探<rt>さが</rt></ruby>しています。</p>
  <p class="pe-ex__uz">Yaponcha gapira oladigan odam qidiryapman.</p>
  <p class="pe-ex__why">Ichkarida potensial shakl (PJ-42) — u ham oddiy shakl, demak toʻgʻridan-toʻgʻri otning oldiga turaveradi.</p>
</div>

<h3>2. Bogʻlovchi soʻz yoʻq, vergul yoʻq</h3>

<p>Yapon tilida ergash gapni otga ulaydigan maxsus olmosh umuman
yoʻq. Hech qanday bogʻlovchi qoʻshilmaydi — gap bilan ot shunchaki
yonma-yon turadi. Shuning uchun boshda gapni koʻzingiz bilan
ajratish qiyin boʻladi; keyin esa buni sezmay ham qoʻyasiz.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>昨日<rt>きのう</rt></ruby></span>
  <span class="pj-joshi__n"><ruby>買<rt>か</rt></ruby>った</span>
  <span class="pj-joshi__n"><ruby>本<rt>ほん</rt></ruby></span>
  <span class="pj-joshi__p">を<small>TOʻLDIRUVCHI</small></span>
  <span class="pj-joshi__v"><ruby>読<rt>よ</rt></ruby>みました</span>
  <span class="pj-joshi__uz">Kecha sotib olgan kitobimni oʻqidim. — «<ruby>昨日<rt>きのう</rt></ruby><ruby>買<rt>か</rt></ruby>った<ruby>本<rt>ほん</rt></ruby>» butunligicha bitta ot boʻlagi.</span>
</div>

<div class="pe-call pe-rule">
  <p><b>Aniqlovchi + ot = bitta ot.</b> U gapda oddiy otdek yashaydi:
  を, が, に, は — hammasini ola oladi. Shuning uchun uni oʻqiyotganda
  ichida nechta soʻz borligi muhim emas; muhimi —
  <em>qayerda tugashi</em>.</p>
</div>

<h3>3. Ichkaridagi ega が oladi, は EMAS</h3>

<p>Mana ikkinchi qoida, va u oʻta muhim.
<b>Ergash gap ichida は turolmaydi.</b> Sababi PJ-14 da aytilgan edi:
は — butun <em>gapning</em> mavzusini koʻrsatadi, ergash gap esa mavzu
qoʻya oladigan joy emas. U yerda faqat ega bor, ega esa <b>が</b>
oladi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">✓ TOʻGʻRI</p>
    <p><ruby>私<rt>わたし</rt></ruby><b>が</b><ruby>作<rt>つく</rt></ruby>った<ruby>料理<rt>りょうり</rt></ruby></p>
    <p>men tayyorlagan taom</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">✗ NOTOʻGʻRI</p>
    <p><ruby>私<rt>わたし</rt></ruby><b>は</b><ruby>作<rt>つく</rt></ruby>った<ruby>料理<rt>りょうり</rt></ruby></p>
    <p>は ergash gap ichiga kira olmaydi</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu joyda ham qoʻshimcha tushib qoladi.</b> Siz «men
  oʻqigan kitob» deysiz — «men» quruq turadi, «-ning» ham «-i» ham
  yoʻq. Yaponcha esa boʻsh joy qoldirmaydi: u yerga <b>が</b> qoʻyadi.
  Shuning uchun oʻzbek oʻquvchisi koʻpincha が ni <em>unutadi</em>,
  yaponlar esa は ni qoʻyib <em>xato</em> qiladi. Ikkala xatoning
  dorisi bitta: ergash gap ichida koʻzingiz doim <b>が</b> ni
  qidirsin.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>が oʻrniga の ham boʻladi.</b>
  <ruby>私<rt>わたし</rt></ruby><b>の</b><ruby>作<rt>つく</rt></ruby>った<ruby>料理<rt>りょうり</rt></ruby>
  — bir xil maʼno, biroz kitobiyroq ohang. Boshda が ni ishlating;
  の ni esa kitob oʻqiyotganda tanib olsangiz kifoya.</p>
</div>

<h3>4. Ot va な-sifat: bu yerda だ turmaydi</h3>

<p>Ikki dars davomida siz «と dan oldin <b>だ</b> saqlanadi» degan
qoidani oʻrgandingiz. <b>Otdan oldin esa だ turolmaydi</b> — u oʻz
shaklini oʻzgartiradi. Bu ikkalasini yonma-yon koʻrish kerak.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>と dan oldin (PJ-46/47)</th><th>OT dan oldin (bugun)</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-end"><ruby>行<rt>い</rt></ruby>くと</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>く<ruby>人<rt>ひと</rt></ruby></td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end"><ruby>高<rt>たか</rt></ruby>いと</td>
      <td class="pj-res"><ruby>高<rt>たか</rt></ruby>い<ruby>本<rt>ほん</rt></ruby></td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end"><ruby>静<rt>しず</rt></ruby>か<b>だ</b>と</td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>か<b>な</b><ruby>部屋<rt>へや</rt></ruby></td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-end"><ruby>学生<rt>がくせい</rt></ruby><b>だ</b>と</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby><b>の</b>ラノさん</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>だ ning uchta yuzi.</b> Yolgʻiz turganda — <b>だ</b>
  (<ruby>静<rt>しず</rt></ruby>かだ). と oldida — <b>だ</b>.
  Ot oldida — <b>な</b> (な-sifat) yoki <b>の</b> (ot). Uchalasi ham
  bitta boglama, faqat qoʻshnisiga qarab kiyimini almashtiradi.
  Aynan shuning uchun bu soʻz turi «な-sifat» deb ataladi.</p>
</div>

<h3>5. Uzun aniqlovchini qanday oʻqish kerak</h3>

<p>Yapon gazetasi va kitobi uzun aniqlovchilarga toʻla. Boshda ular
devordek koʻrinadi. Bitta usul bor, va u har doim ishlaydi.</p>

<div class="pe-steps">
  <ol>
    <li><b>Oxirini toping.</b> Aniqlovchi doim <em>ot</em> bilan
    tugaydi, ot esa qoʻshimcha (を, が, は…) oldida turadi.</li>
    <li><b>Oldingi feʼlni toping.</b> Otdan chapga qarab birinchi
    uchragan oddiy shakldagi feʼl — aniqlovchining kesimi.</li>
    <li><b>Oʻsha feʼldan chapga qarab</b> ergash gapning boshlanishini
    qidiring: が bilan turgan ega, vaqt soʻzi, joy.</li>
    <li><b>Oʻngdan chapga tarjima qiling:</b> «… gan OT».</li>
  </ol>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek oʻquvchisi buni oʻngdan chapga oʻqiydi — va toʻgʻri
  qiladi.</b> «<em>Kecha Munira kutubxonadan olgan</em> kitob» degan
  oʻzbekcha gapni ham siz oxiridagi «kitob» dan tushunasiz: avval
  nimadir haqida gap ketayotganini bilasiz, keyin u nima ekanini.
  Yaponchada ham xuddi shunday — faqat bu yerda uni <em>ataylab</em>
  qilish kerak, chunki boshida koʻz chapdan oʻngga yugurib ketadi va
  ergash gapni asosiy gap deb oʻylaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>昨日<rt>きのう</rt></ruby>ムニラさんが<ruby>図書館<rt>としょかん</rt></ruby>で<ruby>借<rt>か</rt></ruby>りた<ruby>本<rt>ほん</rt></ruby>はとても<ruby>面白<rt>おもしろ</rt></ruby>いです。</p>
  <p class="pe-ex__uz">Kecha Munira kutubxonadan olgan kitob juda qiziqarli.</p>
  <p class="pe-ex__why">Aniqlovchi <ruby>昨日<rt>きのう</rt></ruby> dan <ruby>借<rt>か</rt></ruby>りた gacha; <ruby>本<rt>ほん</rt></ruby> — u aniqlayotgan ot; は dan keyin esa asosiy gap boshlanadi.</p>
</div>

<h3>6. Aniqlovchi ichida ham zamon mustaqil</h3>

<p>PJ-47 dagi qoida bu yerda ham ishlaydi: ichkaridagi feʼlning zamoni
gap oxiridagi feʼlga qaramaydi. U <em>otga nisbatan</em> qachon
sodir boʻlganini koʻrsatadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>明日<rt>あした</rt></ruby><ruby>来<rt>く</rt></ruby>る<ruby>人<rt>ひと</rt></ruby>は<ruby>誰<rt>だれ</rt></ruby>ですか。</p>
  <p class="pe-ex__uz">Ertaga keladigan odam kim?</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>昨日<rt>きのう</rt></ruby><ruby>来<rt>き</rt></ruby>た<ruby>人<rt>ひと</rt></ruby>は<ruby>先生<rt>せんせい</rt></ruby>でした。</p>
  <p class="pe-ex__uz">Kecha kelgan odam oʻqituvchi edi.</p>
  <p class="pe-ex__why">Bitta ot, ikki xil zamon — «keladigan» va «kelgan». Oʻzbekchada ham qoʻshimcha oʻzgaradi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">作</span>
    <span class="pj-kanji__uz">yasamoq, tayyorlamoq</span>
    <span class="pj-kanji__on">オン: サク</span>
    <span class="pj-kanji__kun">KUN: つく(る)</span>
    <span class="pj-kanji__note">作る (つくる) — yasamoq · 作文 (さくぶん) — insho</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">探</span>
    <span class="pj-kanji__uz">qidirmoq</span>
    <span class="pj-kanji__on">オン: タン</span>
    <span class="pj-kanji__kun">KUN: さが(す)</span>
    <span class="pj-kanji__note">探す (さがす) — qidirmoq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>は<ruby>読<rt>よ</rt></ruby>んだ<ruby>本<rt>ほん</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby><b>が</b><ruby>読<rt>よ</rt></ruby>んだ<ruby>本<rt>ほん</rt></ruby> — ergash gap ichida は turolmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>読<rt>よ</rt></ruby>みました<ruby>本<rt>ほん</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>読<rt>よ</rt></ruby>んだ<ruby>本<rt>ほん</rt></ruby> — otdan oldin faqat oddiy shakl.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>静<rt>しず</rt></ruby>かだ<ruby>部屋<rt>へや</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>静<rt>しず</rt></ruby><b>かな</b><ruby>部屋<rt>へや</rt></ruby> — otdan oldin だ → な.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ムニラさんが<ruby>作<rt>つく</rt></ruby>った、<ruby>料理<rt>りょうり</rt></ruby></p>
  <p class="pe-fix__good">✓ ムニラさんが<ruby>作<rt>つく</rt></ruby>った<ruby>料理<rt>りょうり</rt></ruby> — vergul qoʻyilmaydi, ular yopishib turadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Inom sotib olgan velosiped» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>イノムさんが<ruby>買<rt>か</rt></ruby>った<ruby>自転車<rt>じてんしゃ</rt></ruby></b> — ega が, feʼl oddiy shaklda, ot oxirida.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «<ruby>静<rt>しず</rt></ruby>か» soʻzini <ruby>部屋<rt>へや</rt></ruby> ga ulang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>静<rt>しず</rt></ruby>かな<ruby>部屋<rt>へや</rt></ruby></b> — otdan oldin だ oʻrniga <b>な</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby>» — bu yerda nega の?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki aniqlovchi <b>ot</b> (<ruby>日本語<rt>にほんご</rt></ruby>). Ot otni aniqlaganda だ emas, <b>の</b> ishlatiladi (PJ-17).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>昨日<rt>きのう</rt></ruby>パリさんが<ruby>話<rt>はな</rt></ruby>した<ruby>人<rt>ひと</rt></ruby>» ni tarjima qiling.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Kecha Pari gaplashgan odam.</b> Oxiridan boshlab oʻqing: <ruby>人<rt>ひと</rt></ruby> → <ruby>話<rt>はな</rt></ruby>した → パリさんが → <ruby>昨日<rt>きのう</rt></ruby>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega ergash gap ichida は ishlatilmaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki は <b>butun gapning mavzusini</b> koʻrsatadi (PJ-14), ergash gap esa mavzu qoʻyiladigan joy emas. U yerda faqat ega bor — demak <b>が</b>.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>作<rt>つく</rt></ruby>る</b> — yasamoq, tayyorlamoq (I guruh)</li>
  <li><b><ruby>探<rt>さが</rt></ruby>す</b> — qidirmoq (I guruh)</li>
  <li><b><ruby>借<rt>か</rt></ruby>りる</b> — qarzga olmoq (II guruh)</li>
  <li><b><ruby>図書館<rt>としょかん</rt></ruby></b> — kutubxona</li>
  <li><b><ruby>料理<rt>りょうり</rt></ruby></b> — taom, pishirish</li>
  <li><b><ruby>自転車<rt>じてんしゃ</rt></ruby></b> — velosiped</li>
  <li><b><ruby>誰<rt>だれ</rt></ruby></b> — kim</li>
  <li><b><ruby>作文<rt>さくぶん</rt></ruby></b> — insho</li>
  <li><b>な</b> — otdan oldingi な-sifat shakli</li>
  <li><b>の</b> — otdan oldingi ot shakli</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Gap ham sifat kabi <b>otdan oldin</b> turadi — oʻzbekchadagidek.</li>
    <li>Ichkaridagi ega <b>が</b> oladi, は emas.</li>
    <li>と oldida <b>だ</b>, ot oldida <b>な</b> yoki <b>の</b>.</li>
  </ul>
</div>
""",
    },
]
