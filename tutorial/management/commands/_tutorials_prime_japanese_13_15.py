# -*- coding: utf-8 -*-
"""Prime Japanese — Block B, darslar 13–15 (birinchi gaplar).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_JAPANESE.md
Lesson list: tutorial/management/commands/toc_prime_japanese.txt

PJ-13 dan boshlab har bir dars UCHTA boʻlakdan iborat:
  1. dars (bu fayl)
  2. mashq — practice/management/commands/_practice_pj_13_15.py (20 savol)
  3. oʻqish matni — corner/management/commands/_stories_prime_japanese_13_15.py (audio bilan)

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_13_15.py --author=prime
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
        "title": "PJ-13: 〜です / 〜ではありません — birinchi gapingiz va uning inkori",
        "category": "japanese",
        "order": 13,
        "summary": (
            "Yaponchadagi eng muhim soʻz — です. Bitta shakl bilan «…man», «…san», "
            "«…dir» ni ayta olasiz, savol berasiz va inkor qilasiz."
        ),
        "stories": ["はじめまして"],
        "content": """
<h2>PJ-13: 〜です / 〜ではありません — birinchi gapingiz va uning inkori</h2>

<p>Oʻn ikki dars davomida <em>oʻqishni</em> oʻrgandingiz. Bugundan boshlab
<b>gapirasiz</b>. Va birinchi qurolingiz — yapon tilidagi eng koʻp uchraydigan
soʻz: <b>です</b>.</p>

<p>Yaxshi xabar shu qadar yaxshiki, ishonish qiyin: <b>です hech qachon shaxsga
qarab oʻzgarmaydi</b>. Men, sen, u, biz, ular — hammasi uchun bitta shakl.
Ingliz tilida am/is/are, rus tilida ham oʻzgarishlar bor; yaponchada esa
yodlash kerak boʻlgani <em>bitta soʻz</em>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>«A は B です» qolipi bilan oʻzingizni tanishtirasiz</li>
    <li>Savol berasiz: 〜ですか</li>
    <li>Inkor qilasiz: 〜ではありません va uning kundalik shakli</li>
    <li>です nega [des] deb oʻqilishini eslaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Birinchi qolip</span>
  <span class="pe-chip pe-chip--s">A</span>
  <span class="pe-chip pe-chip--opt">は</span>
  <span class="pe-chip pe-chip--o">B</span>
  <span class="pe-chip pe-chip--v">です</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">A — B dir</span>
</div>

<h3>1. です — «…dir»</h3>

<p>Yapon gapi <b>oxiridan</b> tugaydi, va oxirida deyarli doim kesim turadi.
Eng oddiy kesim — <b>です</b>: u oldidagi soʻzni «…dir» qilib qoʻyadi.
Bu soʻzga alohida eʼtibor berish arziydi, chunki u yapon tilidagi eng koʻp
uchraydigan soʻz: har qanday matnni oching — deyarli har uchinchi gap
<b>です</b> bilan tugaydi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n"><ruby>学生<rt>がくせい</rt></ruby></span>
  <span class="pj-joshi__v">です</span>
  <span class="pj-joshi__uz">Men talabaman. — oʻzbekchada ham kesim oxirida: «talaba-man».</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>はアフソナです。</p>
  <p class="pe-ex__rom">watashi wa afusona desu</p>
  <p class="pe-ex__uz">Men Afsonaman.</p>
  <p class="pe-ex__why">Ism katakanada, chunki chet el ismi. は bu yerda <b>[wa]</b> deb oʻqiladi — PJ-3 dagi qoida.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>山田<rt>やまだ</rt></ruby>さんは<ruby>先生<rt>せんせい</rt></ruby>です。</p>
  <p class="pe-ex__rom">yamada-san wa sensē desu</p>
  <p class="pe-ex__uz">Yamada — oʻqituvchi.</p>
  <p class="pe-ex__why"><b>さん</b> — hurmat qoʻshimchasi, ismdan keyin qoʻyiladi. Oʻz ismingizga hech qachon さん qoʻshmaysiz.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek oʻquvchi uchun katta yengillik.</b> Oʻzbekchada kesim shaxsga
  qarab oʻzgaradi: «talaba<b>man</b>», «talaba<b>san</b>», «talaba». Uch shaxs —
  uch qoʻshimcha, va ularni yodlash kerak. Yaponchada esa <b>です</b> hamma
  shaxs uchun bitta: <ruby>私<rt>わたし</rt></ruby>は<ruby>学生<rt>がくせい</rt></ruby>です · あなたは<ruby>学生<rt>がくせい</rt></ruby>です · <ruby>山田<rt>やまだ</rt></ruby>さんは<ruby>学生<rt>がくせい</rt></ruby>です — kesim qimirlamaydi. Yaʼni
  aynan shu nuqtada yapon tili oʻzbekchadan ham sodda, va bu yengillik butun
  kurs davomida saqlanadi: yapon feʼllari <em>hech qachon</em> shaxsga qarab
  tuslanmaydi.</p>
</div>

<div class="pj-say">
  <span class="pj-say__from">です</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[des]</span>
  <span class="pj-say__why">oxiridagi す dagi u deyarli eshitilmaydi — PJ-2 dagi qoida</span>
</div>

<h3>2. Savol — faqat か qoʻshasiz</h3>

<p>Yapon tilida savol yasash uchun soʻz tartibini <b>oʻzgartirish shart emas</b>.
Gap oxiriga <b>か</b> qoʻshasiz — tamom.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">Xabar</p>
    <p class="pj-big">〜です</p>
    <p><ruby>学生<rt>がくせい</rt></ruby>です。<br>Talaba.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">Savol</p>
    <p class="pj-big">〜ですか</p>
    <p><ruby>学生<rt>がくせい</rt></ruby>ですか。<br>Talabami?</p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>Savol belgisi odatda qoʻyilmaydi.</b> か ning oʻzi savolni bildiradi,
  shuning uchun yaponlar gap oxiriga <b>。</b> qoʻyadi. Ohang ham koʻtarilmaydi —
  bu ingliz tilidan katta farq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">アフソナさんは<ruby>日本人<rt>にほんじん</rt></ruby>ですか。</p>
  <p class="pe-ex__rom">afusona-san wa nihonjin desu ka</p>
  <p class="pe-ex__uz">Afsona yaponmi?</p>
  <p class="pe-ex__why">Javob: <b>はい</b> (ha) yoki <b>いいえ</b> (yoʻq). Ikkalasi ham hiraganada, va いいえ dagi い ikkita — uzun i.</p>
</div>

<h3>3. Inkor — 〜ではありません</h3>

<p>Endi teskarisini aytamiz. です ning inkori uzunroq, lekin qoidasi oddiy:
<b>です</b> oʻrniga <b>ではありません</b> qoʻyiladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Yaponcha</th><th>Uslub</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">tasdiq</td><td class="pj-res">です</td>
      <td class="pj-uz">hurmat</td><td class="pj-uz">…dir</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-res">ではありません</td>
      <td class="pj-uz">rasmiy</td><td class="pj-uz">…emas</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-res">じゃありません</td>
      <td class="pj-uz">kundalik</td><td class="pj-uz">…emas</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>では bu yerda «dewa» deb oʻqiladi.</b> Yana oʻsha は qoidasi: u grammatik
  qoʻshimcha boʻlgani uchun <b>[wa]</b> boʻlib oʻqiladi. Yozilishi では,
  oʻqilishi <b>[dewa]</b>. Kundalik nutqda esa u qisqarib <b>じゃ</b> boʻladi —
  aynan shuning uchun じゃありません shakli paydo boʻlgan.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>は<ruby>先生<rt>せんせい</rt></ruby>ではありません。<ruby>学生<rt>がくせい</rt></ruby>です。</p>
  <p class="pe-ex__rom">watashi wa sensē dewa arimasen. gakusē desu</p>
  <p class="pe-ex__uz">Men oʻqituvchi emasman. Talabaman.</p>
  <p class="pe-ex__why">Ikkinchi gapda <ruby>私<rt>わたし</rt></ruby>は takrorlanmadi — mavzu allaqachon maʼlum boʻlsa, yaponchada u <b>tushirib qoldiriladi</b>. Bu juda keng tarqalgan.</p>
</div>

<h3>4. Savolga javob berish</h3>

<p>«はい» va «いいえ» ning oʻzi quruq eshitiladi. Tabiiy javob ikki qismdan
iborat: avval <b>はい</b> yoki <b>いいえ</b>, keyin qisqa tasdiq yoki inkor.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Savol</th><th>Tasdiq javob</th><th>Inkor javob</th></tr>
  <tr><td><ruby>学生<rt>がくせい</rt></ruby>ですか</td>
      <td class="pj-res">はい、そうです</td>
      <td class="pj-res">いいえ、ちがいます</td></tr>
  <tr><td><ruby>先生<rt>せんせい</rt></ruby>ですか</td>
      <td class="pj-res">はい、<ruby>先生<rt>せんせい</rt></ruby>です</td>
      <td class="pj-res">いいえ、<ruby>先生<rt>せんせい</rt></ruby>ではありません</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>そうです</b> — «shunday». <b>ちがいます</b> — «yoʻq, boshqacha».
  Bu ikkalasi universal javob: nima soʻralganini takrorlamasdan, qisqa va
  tabiiy javob berasiz. Yaponlar kundalik nutqda aynan shularni ishlatadi.</p>
</div>

<h3>5. Mavzu tushib qoladi — va bu normal</h3>

<p>Yapon tilidagi eng koʻp hayratlanarli narsalardan biri shu: agar kim haqida
gapirayotganingiz aniq boʻlsa, <b><ruby>私<rt>わたし</rt></ruby>は</b> ni umuman aytmaysiz.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Toʻliq</th><th>Tabiiy</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>私<rt>わたし</rt></ruby>は<ruby>学生<rt>がくせい</rt></ruby>です</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>です</td>
      <td class="pj-uz">Talabaman</td></tr>
  <tr><td>あなたは<ruby>先生<rt>せんせい</rt></ruby>ですか</td>
      <td class="pj-res"><ruby>先生<rt>せんせい</rt></ruby>ですか</td>
      <td class="pj-uz">Oʻqituvchimisiz?</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu oʻzbekchaga juda yaqin.</b> Biz ham «Men talabaman» oʻrniga
  koʻpincha shunchaki «Talabaman» deymiz — qoʻshimcha kimligini aytadi.
  Yaponchada esa qoʻshimcha ham yoʻq, kontekst hal qiladi. Shuning uchun
  <b>あなた</b> («siz») soʻzini ehtiyot bilan ishlating: yaponlar uni kam
  ishlatadi va uning oʻrniga odamning <em>ismini</em> aytadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>は<ruby>学生<rt>がくせい</rt></ruby>は です</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby>は<ruby>学生<rt>がくせい</rt></ruby>です — は gapda bir marta, mavzudan keyin.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Oʻz ismiga さん qoʻshish: <ruby>私<rt>わたし</rt></ruby>はアフソナさんです</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby>はアフソナです — <b>さん</b> faqat boshqa odamga nisbatan ishlatiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ では ni «deha» deb oʻqish</p>
  <p class="pe-fix__good">✓ <b>[dewa]</b> — は grammatik qoʻshimcha boʻlgani uchun [wa] boʻladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Men talabaman» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><ruby>私<rt>わたし</rt></ruby>は<ruby>学生<rt>がくせい</rt></ruby>です。 Kontekst aniq boʻlsa, shunchaki <ruby>学生<rt>がくせい</rt></ruby>です。 ham yetadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Bu gapni savolga aylantiring: <ruby>先生<rt>せんせい</rt></ruby>です。</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><ruby>先生<rt>せんせい</rt></ruby>です<b>か</b>。 — faqat か qoʻshiladi, soʻz tartibi oʻzgarmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. です ning ikkita inkor shaklini ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ではありません</b> (rasmiy) va <b>じゃありません</b> (kundalik).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Nega <ruby>私<rt>わたし</rt></ruby>は koʻpincha tushirib qoldiriladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Kim haqida gapirilayotgani kontekstdan aniq boʻlsa, mavzuni takrorlash <b>ortiqcha</b> sanaladi. Bu yapon tilida juda keng tarqalgan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. です qanday oʻqiladi va nega?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>[des]</b> — soʻz oxiridagi す dagi «u» jarangsiz undosh yonida ovozini yoʻqotadi (PJ-2).</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>私<rt>わたし</rt></ruby></b> — men</li>
  <li><b>です</b> — …dir (kesim)</li>
  <li><b>ではありません</b> — …emas (rasmiy)</li>
  <li><b>じゃありません</b> — …emas (kundalik)</li>
  <li><b>か</b> — savol qoʻshimchasi</li>
  <li><b>はい / いいえ</b> — ha / yoʻq</li>
  <li><b><ruby>学生<rt>がくせい</rt></ruby></b> — talaba</li>
  <li><b><ruby>先生<rt>せんせい</rt></ruby></b> — oʻqituvchi</li>
  <li><b>さん</b> — hurmat qoʻshimchasi</li>
  <li><b><ruby>名前<rt>なまえ</rt></ruby></b> — ism</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>A は B です</b> — birinchi qolipingiz. です shaxsga qarab <b>oʻzgarmaydi</b>.</li>
    <li>Savol — gap oxiriga <b>か</b>. Soʻz tartibi oʻzgarmaydi, ohang koʻtarilmaydi.</li>
    <li>Inkor — <b>ではありません</b> [dewa arimasen] yoki kundalik <b>じゃありません</b>.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-14: は va が — mavzu va ega orasidagi farq",
        "category": "japanese",
        "order": 14,
        "summary": (
            "Yapon tilidagi eng koʻp savol tugʻdiradigan juftlik. は nima haqida "
            "gapirayotganingizni, が esa kim ekanini koʻrsatadi."
        ),
        "stories": ["だれが せんせいですか"],
        "content": """
<h2>PJ-14: は va が — mavzu va ega orasidagi farq</h2>

<p>Mana yapon tilidagi eng mashhur savol. Ikkala qoʻshimcha ham gapning boshiga
yaqin turadi, ikkalasi ham oʻzbekchaga tarjima qilinmaydi, va ikkalasi ham
«ega»ga oʻxshaydi. Unda farqi nima?</p>

<p>Farq bor, va u <em>grammatik</em> emas — <b>maʼlumot</b> bilan bogʻliq.
<b>は</b> «biz nima haqida gapiryapmiz» ni belgilaydi. <b>が</b> esa «kim
aynan» degan savolga javob beradi. Bugun buni bir umrga ajratamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>は mavzuni, が esa egani belgilashini tushunasiz</li>
    <li>Savol soʻzi bilan <b>doim が</b> ishlatilishini bilasiz</li>
    <li>は ning qarama-qarshi qoʻyish vazifasini koʻrasiz</li>
    <li>Qaysi birini tanlashni amaliy qoida bilan hal qilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki vazifa</span>
  <span class="pe-chip pe-chip--opt">は</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">MAVZU — «…ga kelsak»</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">が</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">EGA — «aynan u»</span>
</div>

<h3>1. は — «bu haqda gapiryapmiz»</h3>

<p><b>は</b> ni «mavzu qoʻshimchasi» deb ataymiz. U gapning <em>sarlavhasi</em>ni
qoʻyadi: «Afsonaga kelsak — u talaba». Shuning uchun uni koʻpincha
<b>«…ga kelsak»</b>, <b>«…haqida aytsak»</b> deb tarjima qilish mumkin.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n">アフソナさん</span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n"><ruby>学生<rt>がくせい</rt></ruby></span>
  <span class="pj-joshi__v">です</span>
  <span class="pj-joshi__uz">Afsona — talaba. («Afsonaga kelsak, u talaba.»)</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu vazifa soʻz tartibi bilan bajariladi.</b> «Afsona
  talaba» deganda ham biz Afsonani mavzu qilib qoʻyamiz — u gap boshida
  turibdi. Yapon tilida esa buning uchun <em>alohida qoʻshimcha</em> bor va
  shuning uchun mavzuni gapning istalgan joyiga emas, <b>eng boshiga</b>
  qoʻyish odat.</p>
</div>

<h3>2. が — «aynan u, boshqasi emas»</h3>

<p><b>が</b> egani belgilaydi va u <em>yangi</em> yoki <em>ajratilgan</em>
maʼlumotni koʻrsatadi. Eng oson yoʻli — savol bilan tekshirish.</p>

<div class="pe-call pe-rule">
  <p><b>Oltin qoida:</b> savol soʻzi (<ruby>誰<rt>だれ</rt></ruby>, <ruby>何<rt>なに</rt></ruby>,
  どれ) bilan <b>doim が</b> ishlatiladi — hech qachon は emas. Va javobda ham
  <b>が</b> saqlanadi.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">SAVOL</p>
    <p class="pj-big">が</p>
    <p><ruby>誰<rt>だれ</rt></ruby><b>が</b><ruby>先生<rt>せんせい</rt></ruby>ですか。<br>
    Kim oʻqituvchi?</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">JAVOB</p>
    <p class="pj-big">が</p>
    <p><ruby>山田<rt>やまだ</rt></ruby>さん<b>が</b><ruby>先生<rt>せんせい</rt></ruby>です。<br>
    <b>Yamada</b> oʻqituvchi.</p></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>誰<rt>だれ</rt></ruby>が<ruby>学生<rt>がくせい</rt></ruby>ですか。</p>
  <p class="pe-ex__rom">dare ga gakusē desu ka</p>
  <p class="pe-ex__uz">Kim talaba?</p>
  <p class="pe-ex__why">Bu yerda は ishlatib boʻlmaydi. «<ruby>誰<rt>だれ</rt></ruby>は» degan birikma yapon tilida <b>mavjud emas</b> — savol soʻzi hech qachon mavzu boʻla olmaydi, chunki mavzu allaqachon maʼlum narsa boʻlishi kerak.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Nega shunday?</b> Mavzu — <em>maʼlum</em> narsa: «Afsona haqida
  gapiraylik» deyish uchun Afsona kimligini bilish kerak. Savol soʻzi esa
  aynan <em>nomaʼlum</em> narsani soʻraydi. Nomaʼlum narsani mavzu qilib
  boʻlmaydi — mana shu butun qoidaning sababi.</p>
</div>

<h3>3. Bitta gap, ikki maʼno</h3>

<p>Farqni eng yaxshi koʻrsatadigan usul — bir xil soʻzlarni ikki qoʻshimcha
bilan yonma-yon qoʻyish.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yaponcha</th><th>Maʼnosi</th><th>Qachon aytiladi</th></tr>
  <tr><td><ruby>私<rt>わたし</rt></ruby><b>は</b><ruby>学生<rt>がくせい</rt></ruby>です</td>
      <td class="pj-uz">Men talabaman</td>
      <td class="pj-uz">Oddiy xabar. «Men haqimda aytsam — talabaman.»</td></tr>
  <tr><td><ruby>私<rt>わたし</rt></ruby><b>が</b><ruby>学生<rt>がくせい</rt></ruby>です</td>
      <td class="pj-uz"><b>Aynan men</b> talabaman</td>
      <td class="pj-uz">«Kim talaba?» degan savolga javob. Boshqasi emas, men.</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Ikkinchi gapni tasodifan ishlatmang.</b> «<ruby>私<rt>わたし</rt></ruby>が»
  deb oʻzingizni tanishtirsangiz, «boshqa emas, <em>men</em>!» degan maʼno
  chiqadi va gʻalati eshitiladi. Oddiy tanishuvda doim <b>は</b> ishlating.</p>
</div>

<h3>4. は ning ikkinchi vazifasi — qarama-qarshi qoʻyish</h3>

<p><b>は</b> bitta gapda ikki marta kelsa, u odatda <b>taqqoslash</b> maʼnosini
beradi: «bunisi shunday, anavisi esa boshqacha».</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>山田<rt>やまだ</rt></ruby>さんは<ruby>先生<rt>せんせい</rt></ruby>です。アフソナさんは<ruby>学生<rt>がくせい</rt></ruby>です。</p>
  <p class="pe-ex__rom">yamada-san wa sensē desu. afusona-san wa gakusē desu</p>
  <p class="pe-ex__uz">Yamada — oʻqituvchi. Afsona esa — talaba.</p>
  <p class="pe-ex__why">Ikkita は ikkita mavzuni yonma-yon qoʻyadi va oʻzbekchadagi <b>«esa»</b> ning ishini bajaradi. Bu — は ning eng koʻp uchraydigan ikkinchi vazifasi.</p>
</div>

<h3>5. が boshqa qayerda uchraydi</h3>

<p>が ning yana bir muhim vazifasi bor va uni hozirdan bilib qoʻygan maʼqul:
u <b>mavjudlik</b> va <b>his-tuygʻu</b> gaplarida egani belgilaydi. Bunday
gaplarda は emas, aynan が turadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">〜があります</td>
      <td><ruby>本<rt>ほん</rt></ruby><b>が</b>あります</td>
      <td class="pj-uz">kitob bor</td></tr>
  <tr><td class="pj-stem">〜がいます</td>
      <td><ruby>友達<rt>ともだち</rt></ruby><b>が</b>います</td>
      <td class="pj-uz">doʻst bor</td></tr>
  <tr><td class="pj-stem">〜が<ruby>好<rt>す</rt></ruby>きです</td>
      <td><ruby>日本語<rt>にほんご</rt></ruby><b>が</b><ruby>好<rt>す</rt></ruby>きです</td>
      <td class="pj-uz">yapon tilini yoqtiraman</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Oxirgi qatorga diqqat qiling.</b> Oʻzbekchada «yapon tili<b>ni</b>
  yoqtiraman» — toʻldiruvchi. Yaponchada esa <ruby>好<rt>す</rt></ruby>きです
  aslida sifat («yoqimli»), shuning uchun yoqtirilgan narsa <b>ega</b> boʻlib
  が oladi, を emas. Bu — oʻzbek va yapon tillari ajralib ketadigan kam
  nuqtalardan biri. Bu qoliplarni PJ-16 va PJ-39 da toʻliq koʻramiz;
  hozircha shuni bilib qoʻying: <b>あります · います · <ruby>好<rt>す</rt></ruby>きです bilan
  doim が</b>.</p>
</div>

<h3>6. Amaliy qoida — qaysi birini tanlash</h3>

<ol class="pe-steps">
  <li>Gapda <b>savol soʻzi</b> bormi? → <b>が</b>. Istisnosiz.</li>
  <li>Savol soʻziga <b>javob</b> beryapsizmi? → <b>が</b>.</li>
  <li>Ikki narsani <b>qarama-qarshi</b> qoʻyyapsizmi? → <b>は</b>.</li>
  <li>Boshqa hamma holatda, oddiy xabar uchun → <b>は</b>.</li>
</ol>

<div class="pe-call pe-uz">
  <p><b>Bu qoida hamma narsani qamrab olmaydi</b> — は va が farqi yapon
  grammatikasining eng chuqur mavzularidan biri va unga butun kitoblar
  bagʻishlangan. Lekin boshlovchi uchun bu toʻrt qadam <em>koʻp hollarda</em>
  toʻgʻri javob beradi. Qolganini oʻqib va eshitib, tabiiy yoʻl bilan
  oʻrganasiz — shuning uchun har bir darsning oʻqish matni bor.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>誰<rt>だれ</rt></ruby>は<ruby>先生<rt>せんせい</rt></ruby>ですか</p>
  <p class="pe-fix__good">✓ <ruby>誰<rt>だれ</rt></ruby><b>が</b><ruby>先生<rt>せんせい</rt></ruby>ですか — savol soʻzi bilan doim が.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Oddiy tanishuvda: <ruby>私<rt>わたし</rt></ruby>がアフソナです</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby><b>は</b>アフソナです — が bilan «boshqa emas, aynan men!» degan maʼno chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ は ni «ha» deb oʻqish</p>
  <p class="pe-fix__good">✓ Qoʻshimcha boʻlganda doim <b>[wa]</b>. Bu — butun kursdagi eng koʻp uchraydigan oʻqish xatosi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Kim oʻqituvchi?» — qaysi qoʻshimcha kerak?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>が</b>: <ruby>誰<rt>だれ</rt></ruby>が<ruby>先生<rt>せんせい</rt></ruby>ですか。 Savol soʻzi bilan は <b>hech qachon</b> ishlatilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Nega savol soʻzi mavzu boʻla olmaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Mavzu — <b>maʼlum</b> narsa boʻlishi kerak. Savol soʻzi esa aynan <b>nomaʼlum</b> narsani soʻraydi. Shuning uchun ular bir-biriga toʻgʻri kelmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>私<rt>わたし</rt></ruby>が<ruby>学生<rt>がくせい</rt></ruby>です — bu qanday eshitiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>«<b>Aynan men</b> talabaman» — boshqasi emas. Bu «Kim talaba?» degan savolga javob. Oddiy tanishuv uchun は kerak.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Bitta gapda ikkita は kelsa, u odatda nima maʼno beradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Qarama-qarshi qoʻyish</b> — oʻzbekchadagi «esa» ning ishi: «Bunisi shunday, anavisi esa boshqacha».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. は ni bir jumlada taʼriflang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>は — <b>mavzu</b> qoʻshimchasi: «nima haqida gapiryapmiz» ni belgilaydi va koʻpincha «…ga kelsak» deb tarjima qilinadi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>は</b> — mavzu qoʻshimchasi, [wa]</li>
  <li><b>が</b> — ega qoʻshimchasi</li>
  <li><b><ruby>誰<rt>だれ</rt></ruby></b> — kim</li>
  <li><b><ruby>何<rt>なに</rt></ruby></b> — nima</li>
  <li><b><ruby>山田<rt>やまだ</rt></ruby></b> — Yamada (familiya)</li>
  <li><b><ruby>学生<rt>がくせい</rt></ruby></b> — talaba</li>
  <li><b><ruby>先生<rt>せんせい</rt></ruby></b> — oʻqituvchi</li>
  <li><b><ruby>友達<rt>ともだち</rt></ruby></b> — doʻst</li>
  <li><b><ruby>会社員<rt>かいしゃいん</rt></ruby></b> — xizmatchi</li>
  <li><b><ruby>医者<rt>いしゃ</rt></ruby></b> — shifokor</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>は</b> mavzuni («nima haqida»), <b>が</b> egani («aynan kim») belgilaydi.</li>
    <li>Savol soʻzi bilan <b>doim が</b> — <ruby>誰<rt>だれ</rt></ruby>は degan birikma yoʻq.</li>
    <li>Ikkita は — <b>qarama-qarshi qoʻyish</b>, oʻzbekchadagi «esa».</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-15: これ・それ・あれ va この・その・あの — koʻrsatish olmoshlari",
        "category": "japanese",
        "order": 15,
        "summary": (
            "Yaponchaning ko-so-a-do tizimi: uch masofa, ikki shakl. «Bu» va «bu kitob» "
            "nega boshqacha yozilishini oʻrganasiz."
        ),
        "stories": ["これは なんですか"],
        "content": """
<h2>PJ-15: これ・それ・あれ va この・その・あの — koʻrsatish olmoshlari</h2>

<p>Doʻkonda turibsiz va bir narsani koʻrsatib «bu nima?» demoqchisiz. Yapon
tilida buning uchun <b>uchta</b> soʻz bor — qaysi birini tanlash narsaning
sizdan va suhbatdoshingizdan qanchalik uzoqligiga bogʻliq.</p>

<p>Oʻzbekchada ham shunga oʻxshash uchlik bor: <em>bu — shu — anavi</em>.
Demak tizim tanish. Lekin yaponchada bitta qoʻshimcha nozik joy bor:
<b>«bu»</b> va <b>«bu kitob»</b> ikki xil soʻz bilan aytiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>これ・それ・あれ ni masofaga qarab tanlaysiz</li>
    <li>この・その・あの ni otdan oldin ishlatasiz</li>
    <li>Ikki qatorning farqini bir umrga ajratasiz</li>
    <li>どれ va どの bilan savol berasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">ko-so-a-do tizimi</span>
  <span class="pe-chip pe-chip--s">こ yaqin</span>
  <span class="pe-chip pe-chip--v">そ suhbatdoshga yaqin</span>
  <span class="pe-chip pe-chip--o">あ ikkalasidan uzoq</span>
  <span class="pe-chip pe-chip--neg">ど savol</span>
</div>

<h3>1. Uch masofa</h3>

<p>Yapon tilidagi masofa <b>ikki kishiga</b> nisbatan oʻlchanadi — bu ingliz
tilidan ham, oʻzbekchadan ham nozikroq.</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>これ — bu</p>
    <p><b>Menga yaqin.</b> Qoʻlimdagi narsa, oldimdagi narsa.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>それ — shu</p>
    <p><b>Senga yaqin.</b> Suhbatdoshimning qoʻlidagi yoki yonidagi narsa.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>あれ — anavi</p>
    <p><b>Ikkalamizdan ham uzoq.</b> Narigi tomondagi narsa.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha bilan farq shu yerda.</b> Oʻzbekchada «bu» va «shu» koʻpincha
  bir xil ishlatiladi va farqi aniq emas. Yaponchada esa <b>それ</b> ning
  maʼnosi qatʼiy: «<em>sen</em>ga yaqin narsa». Doʻkonda sotuvchi ushlab turgan
  narsani koʻrsatsangiz — それ. Oʻzingiz ushlab tursangiz — これ. Bu farqni
  yaponlar juda aniq his qiladi.</p>
</div>

<h3>2. Ikkinchi qator: この・その・あの</h3>

<p>Endi darsning asosiy nozikligi. Yuqoridagi uchtasi <b>yolgʻiz</b> turadi —
ular «narsa» degan maʼnoni oʻzida saqlaydi. Agar narsaning <em>nomini</em>
aytmoqchi boʻlsangiz, boshqa qator kerak.</p>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">これ — YOLGʻIZ turadi</p>
    <p class="pj-pair__form">これです</p>
    <p>«Bu». Oʻzi ot vazifasini bajaradi. Ortidan ot <b>kelmaydi</b>.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">この — OT bilan keladi</p>
    <p class="pj-pair__form">この<ruby>本<rt>ほん</rt></ruby></p>
    <p>«Bu kitob». Yolgʻiz turolmaydi — ortidan <b>albatta</b> ot kerak.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">これは<ruby>本<rt>ほん</rt></ruby>です。</p>
  <p class="pe-ex__rom">kore wa hon desu</p>
  <p class="pe-ex__uz">Bu — kitob.</p>
  <p class="pe-ex__why">これ yolgʻiz turibdi va mavzu boʻlyapti: «bu narsa — kitob».</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>本<rt>ほん</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>のです。</p>
  <p class="pe-ex__rom">kono hon wa watashi no desu</p>
  <p class="pe-ex__uz">Bu kitob — meniki.</p>
  <p class="pe-ex__why">この darrov <ruby>本<rt>ほん</rt></ruby> ga yopishdi. «この は…» deb yozib boʻlmaydi — この hech qachon yolgʻiz qolmaydi.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Eslab qolish usuli:</b> <b>これ</b> oxirida <b>れ</b> bor — u
  <em>toʻliq</em> soʻz, oʻzi yetadi. <b>この</b> oxirida <b>の</b> bor — u
  <em>bogʻlovchi</em>, ortidan nimadir kelishi shart. Har safar shubhalansangiz,
  oxirgi boʻgʻinga qarang.</p>
</div>

<h3>3. Toʻliq jadval</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Masofa</th><th>Yolgʻiz (narsa)</th><th>Ot bilan</th><th>Joy</th></tr>
  <tr><td class="pj-stem">こ — menga yaqin</td><td class="pj-res">これ</td>
      <td class="pj-end">この＋ot</td><td class="pj-uz">ここ — bu yer</td></tr>
  <tr><td class="pj-stem">そ — senga yaqin</td><td class="pj-res">それ</td>
      <td class="pj-end">その＋ot</td><td class="pj-uz">そこ — shu yer</td></tr>
  <tr><td class="pj-stem">あ — uzoq</td><td class="pj-res">あれ</td>
      <td class="pj-end">あの＋ot</td><td class="pj-uz">あそこ — u yer</td></tr>
  <tr><td class="pj-stem">ど — savol</td><td class="pj-res">どれ</td>
      <td class="pj-end">どの＋ot</td><td class="pj-uz">どこ — qayer</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bu jadval butun kursda ishlaydi.</b> ko-so-a-do tizimi yapon tilining
  eng tartibli qismlaridan biri: boshlangʻich harf masofani, qolgan qismi esa
  turini bildiradi. Joy soʻzlarini (ここ・そこ・あそこ) PJ-16 da toʻliq
  koʻramiz — hozircha ular shu jadvalda turgani yetadi.</p>
</div>

<h3>4. あの ning ikkinchi hayoti</h3>

<p><b>あの</b> ning yana bir vazifasi bor va u kundalik nutqda juda koʻp
uchraydi: gap boshida yolgʻiz aytilsa, u <b>«kechirasiz…»</b> degan maʼnoni
beradi — odamga murojaat qilishdan oldingi ehtiyotkor tovush.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">あの、すみません。これは<ruby>何<rt>なん</rt></ruby>ですか。</p>
  <p class="pe-ex__rom">ano, sumimasen. kore wa nan desu ka</p>
  <p class="pe-ex__uz">Kechirasiz… bu nima?</p>
  <p class="pe-ex__why">Birinchi あの — koʻrsatish emas, murojaat. Vergul bilan ajratilgani shuni bildiradi. Oʻzbekchada ham «anavi…» deb duduqlanamiz — mantiq bir xil.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Yana bir foydali qoʻllanish:</b> <b>あの</b> ikkala suhbatdosh ham
  biladigan, lekin hozir koʻrinmayotgan narsa haqida ham ishlatiladi —
  «oʻsha, bilasan-ku». <b>その</b> esa suhbatda endigina tilga olingan narsani
  koʻrsatadi. Yaʼni masofa faqat fazoda emas, <em>xotirada</em> ham
  oʻlchanadi. Bu nozik farqni hozir yodlash shart emas, lekin matnlarda
  koʻrganingizda tanib olasiz.</p>
</div>

<h3>5. Savol berish: どれ va どの</h3>

<div class="pe-ex">
  <p class="pe-ex__ja">どれが<ruby>私<rt>わたし</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>ですか。</p>
  <p class="pe-ex__rom">dore ga watashi no hon desu ka</p>
  <p class="pe-ex__uz">Qaysi biri mening kitobim?</p>
  <p class="pe-ex__why">Diqqat: <b>が</b>, は emas. PJ-14 dagi qoida ishlayapti — savol soʻzi bilan doim が.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">どの<ruby>本<rt>ほん</rt></ruby>があなたのですか。</p>
  <p class="pe-ex__rom">dono hon ga anata no desu ka</p>
  <p class="pe-ex__uz">Qaysi kitob sizniki?</p>
  <p class="pe-ex__why">どの ham ot talab qiladi — xuddi この kabi. Ikkalasi ham の bilan tugaydi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Ikkitadan tanlashda どれ ishlatilmaydi.</b> Faqat ikki narsa boʻlsa,
  yaponlar <b>どちら</b> soʻzini ishlatadi. どれ uch va undan koʻp narsa
  orasidan tanlaganda ishlaydi. Oʻzbekchada bunday farq yoʻq, shuning uchun
  buni alohida eslab qoling.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ この は<ruby>本<rt>ほん</rt></ruby>です</p>
  <p class="pe-fix__good">✓ <b>これ</b>は<ruby>本<rt>ほん</rt></ruby>です — この yolgʻiz qololmaydi, ortidan albatta ot kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ これ<ruby>本<rt>ほん</rt></ruby>はわたしのです</p>
  <p class="pe-fix__good">✓ <b>この</b><ruby>本<rt>ほん</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>のです — ot bilan これ emas, この ishlatiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ どれは<ruby>本<rt>ほん</rt></ruby>ですか</p>
  <p class="pe-fix__good">✓ どれ<b>が</b><ruby>本<rt>ほん</rt></ruby>ですか — savol soʻzi bilan doim が.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Suhbatdoshingiz ushlab turgan narsani qanday koʻrsatasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>それ</b> — «senga yaqin narsa». Oʻzingiz ushlab tursangiz これ, ikkalangizdan ham uzoq boʻlsa あれ.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. これ va この ni qanday ajratasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>これ</b> yolgʻiz turadi, oʻzi «narsa» maʼnosini saqlaydi. <b>この</b> esa ortidan <b>albatta ot</b> talab qiladi. Oxirgi boʻgʻinga qarang: れ toʻliq, の bogʻlovchi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Bu kitob meniki» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>この<ruby>本<rt>ほん</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>のです。 — ot bor, demak この.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. どれ dan keyin は yoki が — qaysi biri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>が</b>. どれ — savol soʻzi, savol soʻzi esa hech qachon mavzu boʻla olmaydi (PJ-14).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Faqat ikki narsadan birini tanlash kerak boʻlsa, qaysi soʻz ishlatiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>どちら</b>. どれ uch va undan koʻp narsa orasidan tanlaganda ishlatiladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>これ・それ・あれ</b> — bu, shu, anavi</li>
  <li><b>この・その・あの</b> — bu…, shu…, anavi… (ot bilan)</li>
  <li><b>どれ / どの</b> — qaysi biri / qaysi…</li>
  <li><b>どちら</b> — ikkitadan qaysi biri</li>
  <li><b><ruby>本<rt>ほん</rt></ruby></b> — kitob</li>
  <li><b><ruby>鞄<rt>かばん</rt></ruby></b> — sumka</li>
  <li><b><ruby>時計<rt>とけい</rt></ruby></b> — soat</li>
  <li><b>ペン</b> — ruchka</li>
  <li><b><ruby>傘<rt>かさ</rt></ruby></b> — soyabon</li>
  <li><b><ruby>何<rt>なん</rt></ruby></b> — nima</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Uch masofa: <b>こ</b> menga yaqin, <b>そ</b> senga yaqin, <b>あ</b> ikkalamizdan uzoq.</li>
    <li><b>これ</b> yolgʻiz turadi, <b>この</b> ortidan albatta ot talab qiladi.</li>
    <li>Savol soʻzlari <b>どれ · どの · どこ</b> — va ular bilan doim <b>が</b>.</li>
  </ul>
</div>
""",
    },
]
