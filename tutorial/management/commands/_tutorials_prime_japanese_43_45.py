# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-43, PJ-44 (Block C oxiri) va PJ-45 (Block D boshi).

PJ-45 — kursning ikkinchi burilish nuqtasi: 普通体. Undan keyin oʻqish
matnlari ham oddiy shaklda hikoya qiladi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_43_45.py --author=prime
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
        "title": "PJ-43: Sanoq soʻzlari (助数詞) va ularning tovush oʻzgarishi",
        "category": "japanese",
        "order": 43,
        "summary": (
            "Yaponchada narsani shunchaki sanab boʻlmaydi — har bir turga oʻz "
            "soʻzi bor. Va eng qiyini sonlar emas, ularning oldida sodir "
            "boʻladigan tovush oʻzgarishi."
        ),
        "stories": ["ねこが さんびき"],
        "content": """
<h2>PJ-43: Sanoq soʻzlari (<ruby>助数詞<rt>じょすうし</rt></ruby>) va ularning tovush oʻzgarishi</h2>

<p>«Uchta kitob» degan gapni yaponchada tuzib koʻring. Sizda
<ruby>三<rt>さん</rt></ruby> bor, <ruby>本<rt>ほん</rt></ruby> bor —
lekin ularni shunchaki yonma-yon qoʻyib boʻlmaydi.</p>

<p>Yapon tilida son bilan ot orasida <b>uchinchi soʻz</b> turadi: sanoq
soʻzi. U narsaning <em>turiga</em> qarab tanlanadi — yassimi, uzunmi,
tirikmi. Va uning oldida son koʻpincha <b>oʻz tovushini oʻzgartiradi</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Oltita eng kerakli sanoq soʻzini oʻrganasiz</li>
    <li>Tovush oʻzgarishini <em>qoida</em> sifatida koʻrasiz, yodlab emas</li>
    <li>Umumiy 〜つ sanogʻini bilib olasiz</li>
    <li>Sanoq soʻzini gapda toʻgʻri joyga qoʻyasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">SON + SANOQ SOʻZI</span>
  <span class="pe-chip pe-chip--s"><ruby>三<rt>さん</rt></ruby></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o"><ruby>本<rt>ほん</rt></ruby></span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v"><ruby>三本<rt>さんぼん</rt></ruby></span>
</div>

<h3>1. Oltita sanoq soʻzi</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Nimani sanaydi</th><th>Misol</th></tr>
  <tr><td class="pj-end"><ruby>人<rt>にん</rt></ruby></td><td class="pj-uz">odam</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>, <ruby>友<rt>とも</rt></ruby>だち</td></tr>
  <tr><td class="pj-end"><ruby>枚<rt>まい</rt></ruby></td><td class="pj-uz">yassi narsa</td>
      <td class="pj-res"><ruby>紙<rt>かみ</rt></ruby>, シャツ, <ruby>写真<rt>しゃしん</rt></ruby></td></tr>
  <tr><td class="pj-end"><ruby>本<rt>ほん</rt></ruby></td><td class="pj-uz">uzun narsa</td>
      <td class="pj-res"><ruby>鉛筆<rt>えんぴつ</rt></ruby>, <ruby>傘<rt>かさ</rt></ruby>, バナナ</td></tr>
  <tr><td class="pj-end"><ruby>匹<rt>ひき</rt></ruby></td><td class="pj-uz">kichik hayvon</td>
      <td class="pj-res"><ruby>猫<rt>ねこ</rt></ruby>, <ruby>犬<rt>いぬ</rt></ruby>, <ruby>魚<rt>さかな</rt></ruby></td></tr>
  <tr><td class="pj-end"><ruby>個<rt>こ</rt></ruby></td><td class="pj-uz">kichik buyum</td>
      <td class="pj-res">りんご, <ruby>卵<rt>たまご</rt></ruby></td></tr>
  <tr><td class="pj-end"><ruby>台<rt>だい</rt></ruby></td><td class="pj-uz">mashina, texnika</td>
      <td class="pj-res"><ruby>車<rt>くるま</rt></ruby>, パソコン</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b><ruby>本<rt>ほん</rt></ruby> «kitob» degani emas!</b> Sanoq soʻzi
  sifatida u <em>uzun narsa</em> ni sanaydi: qalam, soyabon, banan,
  shisha. Kitob esa <ruby>冊<rt>さつ</rt></ruby> bilan sanaladi. Bitta
  kanji ikki xil ishda — buni boshidanoq ajratib qoʻying.</p>
</div>

<h3>2. Tovush oʻzgarishi — qoida, yodlash emas</h3>

<p>Bu qismni koʻpchilik yodlaydi. Kerak emas: hammasi ikkita qoidaga
sigʻadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qoida</th><th>Qaysi sanoq soʻzida</th><th>Nima boʻladi</th></tr>
  <tr><td class="pj-stem">1, 6, 8, 10</td><td class="pj-uz">は va か qatoridagilar</td>
      <td class="pj-end">kichik <b>っ</b> qoʻshiladi</td></tr>
  <tr><td class="pj-stem">3 va <ruby>何<rt>なん</rt></ruby></td><td class="pj-uz">faqat は qatoridagilar</td>
      <td class="pj-end">は → <b>ば</b> (jaranglashadi)</td></tr>
</table></div>

<p>は qatoridagi sanoq soʻzlari — <ruby>本<rt>ほん</rt></ruby> va
<ruby>匹<rt>ひき</rt></ruby>. か qatoridagisi —
<ruby>個<rt>こ</rt></ruby>. Qolganlari
(<ruby>人<rt>にん</rt></ruby>, <ruby>枚<rt>まい</rt></ruby>,
<ruby>台<rt>だい</rt></ruby>) <b>umuman oʻzgarmaydi</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Son</th><th><ruby>本<rt>ほん</rt></ruby></th><th><ruby>匹<rt>ひき</rt></ruby></th><th><ruby>個<rt>こ</rt></ruby></th><th><ruby>枚<rt>まい</rt></ruby></th></tr>
  <tr><td class="pj-stem">1</td><td class="pj-res"><ruby>一本<rt>いっぽん</rt></ruby></td>
      <td class="pj-res"><ruby>一匹<rt>いっぴき</rt></ruby></td><td class="pj-res"><ruby>一個<rt>いっこ</rt></ruby></td>
      <td class="pj-uz"><ruby>一枚<rt>いちまい</rt></ruby></td></tr>
  <tr><td class="pj-stem">2</td><td class="pj-uz"><ruby>二本<rt>にほん</rt></ruby></td>
      <td class="pj-uz"><ruby>二匹<rt>にひき</rt></ruby></td><td class="pj-uz"><ruby>二個<rt>にこ</rt></ruby></td>
      <td class="pj-uz"><ruby>二枚<rt>にまい</rt></ruby></td></tr>
  <tr><td class="pj-stem">3</td><td class="pj-res"><ruby>三本<rt>さんぼん</rt></ruby></td>
      <td class="pj-res"><ruby>三匹<rt>さんびき</rt></ruby></td><td class="pj-uz"><ruby>三個<rt>さんこ</rt></ruby></td>
      <td class="pj-uz"><ruby>三枚<rt>さんまい</rt></ruby></td></tr>
  <tr><td class="pj-stem">6</td><td class="pj-res"><ruby>六本<rt>ろっぽん</rt></ruby></td>
      <td class="pj-res"><ruby>六匹<rt>ろっぴき</rt></ruby></td><td class="pj-res"><ruby>六個<rt>ろっこ</rt></ruby></td>
      <td class="pj-uz"><ruby>六枚<rt>ろくまい</rt></ruby></td></tr>
  <tr><td class="pj-stem">8</td><td class="pj-res"><ruby>八本<rt>はっぽん</rt></ruby></td>
      <td class="pj-res"><ruby>八匹<rt>はっぴき</rt></ruby></td><td class="pj-res"><ruby>八個<rt>はっこ</rt></ruby></td>
      <td class="pj-uz"><ruby>八枚<rt>はちまい</rt></ruby></td></tr>
  <tr><td class="pj-stem">10</td><td class="pj-res"><ruby>十本<rt>じゅっぽん</rt></ruby></td>
      <td class="pj-res"><ruby>十匹<rt>じゅっぴき</rt></ruby></td><td class="pj-res"><ruby>十個<rt>じゅっこ</rt></ruby></td>
      <td class="pj-uz"><ruby>十枚<rt>じゅうまい</rt></ruby></td></tr>
  <tr><td class="pj-stem"><ruby>何<rt>なん</rt></ruby></td><td class="pj-res"><ruby>何本<rt>なんぼん</rt></ruby></td>
      <td class="pj-res"><ruby>何匹<rt>なんびき</rt></ruby></td><td class="pj-uz"><ruby>何個<rt>なんこ</rt></ruby></td>
      <td class="pj-uz"><ruby>何枚<rt>なんまい</rt></ruby></td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu oʻzgarish tasodifiy emas — u tilni yengillashtiradi.</b>
  «さんほん» deb aytib koʻring: ん dan keyin ほ ni chiqarish qiyin, til
  oʻz-oʻzidan «ぼ» ga oʻtadi. «いちほん» ham xuddi shunday «いっぽん» ga
  siqiladi. Oʻzbekchada ham shunday jarayonlar bor — «ket+di» ogʻizda
  <em>ketti</em> boʻlib chiqadi. Farqi bitta: yapon tili bu oʻzgarishni
  <b>yozuvda ham</b> koʻrsatadi, oʻzbekcha esa yozuvda saqlab qoladi.</p>
</div>

<h3>3. <ruby>人<rt>にん</rt></ruby> — ikkita istisno</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Son</th><th>Oʻqilishi</th><th>Izoh</th></tr>
  <tr><td class="pj-stem">1</td><td class="pj-res"><ruby>一人<rt>ひとり</rt></ruby></td><td class="pj-uz">tartibsiz</td></tr>
  <tr><td class="pj-stem">2</td><td class="pj-res"><ruby>二人<rt>ふたり</rt></ruby></td><td class="pj-uz">tartibsiz</td></tr>
  <tr><td class="pj-stem">3</td><td class="pj-uz"><ruby>三人<rt>さんにん</rt></ruby></td><td class="pj-uz">odatdagidek</td></tr>
  <tr><td class="pj-stem">4</td><td class="pj-res"><ruby>四人<rt>よにん</rt></ruby></td><td class="pj-uz">よん emas, <b>よ</b></td></tr>
</table></div>

<p><ruby>一人<rt>ひとり</rt></ruby> va <ruby>二人<rt>ふたり</rt></ruby>
sizga PJ-22 dan tanish — oʻqish matnlarida koʻp marta uchragan. Endi
ular qaysi tizimga tegishli ekani ham maʼlum boʻldi, va nega 3 dan
boshlab hammasi oddiy holga qaytishi ham.</p>

<h3>4. 〜つ — universal sanoq</h3>

<p>Sanoq soʻzini bilmasangiz, <b>〜つ</b> bor. U kichik buyumlarni
sanaydi va deyarli har doim ishlaydi. Faqat <b>1 dan 10 gacha</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th></tr>
  <tr><td class="pj-res">ひとつ</td><td class="pj-res">ふたつ</td><td class="pj-res">みっつ</td>
      <td class="pj-res">よっつ</td><td class="pj-res">いつつ</td></tr>
  <tr><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th></tr>
  <tr><td class="pj-res">むっつ</td><td class="pj-res">ななつ</td><td class="pj-res">やっつ</td>
      <td class="pj-res">ここのつ</td><td class="pj-res">とお</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bular yaponcha sonlar</b> — PJ-12 dagi
  <ruby>一<rt>いち</rt></ruby>, <ruby>二<rt>に</rt></ruby> xitoycha
  sonlar edi. Shuning uchun ular butunlay boshqacha eshitiladi va
  10 dan keyin tugaydi. Doʻkonda «buni ikkitasini bering» deyish uchun
  <b>ふたつ</b> kifoya.</p>
</div>

<h3>5. Gapda qayerda turadi</h3>

<p>Sanoq soʻzi <b>otdan keyin, feʼldan oldin</b> turadi — va oʻz
qoʻshimchasini olmaydi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n">りんご</span>
  <span class="pj-joshi__p">を<small>TOʻLDIRUVCHI</small></span>
  <span class="pj-joshi__n"><ruby>三個<rt>さんこ</rt></ruby></span>
  <span class="pj-joshi__v"><ruby>買<rt>か</rt></ruby>いました</span>
  <span class="pj-joshi__uz">Uchta olma sotib oldim.</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>学生<rt>がくせい</rt></ruby>が<ruby>八人<rt>はちにん</rt></ruby>います。<ruby>猫<rt>ねこ</rt></ruby>が<ruby>三匹<rt>さんびき</rt></ruby>います。</p>
  <p class="pe-ex__rom">kyōshitsu ni gakusei ga hachinin imasu. neko ga sanbiki imasu</p>
  <p class="pe-ex__uz">Sinfda sakkiz nafar talaba bor. Uchta mushuk bor.</p>
  <p class="pe-ex__why">Sanoq soʻzi <b>が</b> yoki <b>を</b> dan keyin, feʼldan oldin. Unga hech qanday qoʻshimcha qoʻshilmaydi.</p>
</div>

<h3>6. Savol berish</h3>

<p><ruby>何<rt>なん</rt></ruby> ni sanoq soʻziga qoʻshsangiz, savol
chiqadi — va u ham oʻsha tovush qoidasiga boʻysunadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Savol</th><th>Nimani soʻraydi</th></tr>
  <tr><td class="pj-res"><ruby>何人<rt>なんにん</rt></ruby></td><td class="pj-uz">necha kishi</td></tr>
  <tr><td class="pj-res"><ruby>何本<rt>なんぼん</rt></ruby></td><td class="pj-uz">nechta (uzun narsa)</td></tr>
  <tr><td class="pj-res"><ruby>何匹<rt>なんびき</rt></ruby></td><td class="pj-uz">nechta (hayvon)</td></tr>
  <tr><td class="pj-res">いくつ</td><td class="pj-uz">nechta (umumiy)</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ さんほん</p>
  <p class="pe-fix__good">✓ <ruby>三本<rt>さんぼん</rt></ruby> — 3 va <ruby>何<rt>なん</rt></ruby> は qatorini <b>jaranglashtiradi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ りんごを<ruby>三個<rt>さんこ</rt></ruby>を<ruby>買<rt>か</rt></ruby>いました</p>
  <p class="pe-fix__good">✓ りんごを<ruby>三個<rt>さんこ</rt></ruby><ruby>買<rt>か</rt></ruby>いました — sanoq soʻzi <b>qoʻshimcha olmaydi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>猫<rt>ねこ</rt></ruby>が<ruby>三本<rt>さんぼん</rt></ruby>います</p>
  <p class="pe-fix__good">✓ <ruby>猫<rt>ねこ</rt></ruby>が<ruby>三匹<rt>さんびき</rt></ruby>います — tirik jonzot <b><ruby>匹<rt>ひき</rt></ruby></b> bilan sanaladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Uchta qalam» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>鉛筆<rt>えんぴつ</rt></ruby><ruby>三本<rt>さんぼん</rt></ruby></b> — uzun narsa, va 3 は ni ば ga aylantiradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>一匹<rt>いっぴき</rt></ruby> nega «いちひき» emas?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>1, 6, 8, 10 <b>っ</b> qoʻshadi va は qatorini <b>ぱ</b> ga oʻtkazadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Toʻrt kishi» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>四人<rt>よにん</rt></ruby></b> — よん emas, <b>よ</b>. Bu <ruby>人<rt>にん</rt></ruby> ning uchinchi istisnosi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Qaysi sanoq soʻzlari umuman oʻzgarmaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>枚<rt>まい</rt></ruby> va <ruby>台<rt>だい</rt></ruby></b> (va <ruby>人<rt>にん</rt></ruby>, oʻz istisnolaridan tashqari). Faqat は va か qatoridagilari oʻzgaradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Sanoq soʻzini bilmasangiz nima qilasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>〜つ</b> ni ishlating: ひとつ, ふたつ, みっつ… U 10 gacha ishlaydi va deyarli hech qachon xato boʻlmaydi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>助数詞<rt>じょすうし</rt></ruby></b> — sanoq soʻzi</li>
  <li><b><ruby>枚<rt>まい</rt></ruby></b> — yassi narsalar uchun</li>
  <li><b><ruby>本<rt>ほん</rt></ruby></b> — uzun narsalar uchun</li>
  <li><b><ruby>匹<rt>ひき</rt></ruby></b> — kichik hayvonlar uchun</li>
  <li><b><ruby>個<rt>こ</rt></ruby></b> — kichik buyumlar uchun</li>
  <li><b><ruby>台<rt>だい</rt></ruby></b> — texnika uchun</li>
  <li><b><ruby>犬<rt>いぬ</rt></ruby></b> — it</li>
  <li><b><ruby>傘<rt>かさ</rt></ruby></b> — soyabon</li>
  <li><b><ruby>卵<rt>たまご</rt></ruby></b> — tuxum</li>
  <li><b>いくつ</b> — nechta?</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>1, 6, 8, 10</b> → kichik <b>っ</b>; <b>3 va <ruby>何<rt>なん</rt></ruby></b> → は <b>ば</b> ga.</li>
    <li><ruby>枚<rt>まい</rt></ruby> va <ruby>台<rt>だい</rt></ruby> <b>oʻzgarmaydi</b>.</li>
    <li>Bilmasangiz — <b>〜つ</b>. U deyarli har doim ishlaydi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-44: Taqqoslash — 〜より, 〜のほうが, いちばん",
        "category": "japanese",
        "order": 44,
        "summary": (
            "«Kattaroq», «eng katta». Yaponchada sifat oʻzgarmaydi — "
            "taqqoslashni qoʻshimchalar bajaradi, va bu oʻzbek oʻquvchi "
            "uchun ancha oson."
        ),
        "stories": ["どちらが たかいですか"],
        "content": """
<h2>PJ-44: Taqqoslash — 〜より, 〜のほうが, いちばん</h2>

<p>Oʻzbekchada «katta» dan «katta<b>roq</b>» yasaladi — sifatning
oʻziga qoʻshimcha yopishadi. Yapon tilida esa sifat <b>umuman
oʻzgarmaydi</b>: <ruby>大<rt>おお</rt></ruby>きい taqqoslashda ham
<ruby>大<rt>おお</rt></ruby>きい boʻlib qoladi.</p>

<p>Unda «kattaroq» degan maʼno qayerdan chiqadi? Uni <b>gapning
tuzilishi</b> beradi: qaysi narsa qaysi qoʻshimchani olganidan.
Yaʼni sizga yangi sifat shakllari emas, uchta yangi soʻz kerak.</p>

<p>Bu — yapon tilining odati: maʼnoni soʻzning ichiga emas, uning
<em>atrofiga</em> qoʻyadi. Siz buni allaqachon koʻrgansiz — zamon
feʼlning oxirida, muloyimlik です da, savol か da turadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Ikki narsani taqqoslaysiz: <b>より</b></li>
    <li>Tanlovni bildirasiz: <b>のほうが</b></li>
    <li>Savol berasiz: <b>どちらが</b></li>
    <li>Eng ustunini aytasiz: <b>いちばん</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">A は B より SIFAT です</span>
  <span class="pe-chip pe-chip--s">A</span>
  <span class="pe-op">＞</span>
  <span class="pe-chip pe-chip--o">B より</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">SIFAT</span>
</div>

<h3>1. 〜より — «…dan koʻra»</h3>

<p><b>より</b> <em>past</em> tomonni belgilaydi — yaʼni oʻzidan oldingi
narsa kamroq.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>富士山<rt>ふじさん</rt></ruby></span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n">この<ruby>山<rt>やま</rt></ruby></span>
  <span class="pj-joshi__p">より<small>…DAN</small></span>
  <span class="pj-joshi__v"><ruby>高<rt>たか</rt></ruby>いです</span>
  <span class="pj-joshi__uz">Fuji bu togʻdan baland.</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu «-dan» kelishigi</b> — «bu togʻ<b>dan</b>
  baland». Ikki tilda ham sifat qimirlamaydi va qoʻshimcha <em>past</em>
  tomonga yopishadi. Rus yoki ingliz tilidan kelgan oʻquvchi bu yerda
  sifatni oʻzgartirmoqchi boʻladi; oʻzbek oʻquvchi esa toʻgʻri qoladi.
  Bu — kursdagi eng qulay mosliklardan biri.</p>
</div>

<h3>2. 〜のほうが — «… tomoni koʻproq»</h3>

<p><b>ほう</b> — «tomon» degan ot. のほうが esa <em>yuqori</em> tomonni
belgilaydi. Koʻpincha より bilan birga keladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>電車<rt>でんしゃ</rt></ruby>のほうがバスより<ruby>速<rt>はや</rt></ruby>いです。</p>
  <p class="pe-ex__rom">densha no hō ga basu yori hayai desu</p>
  <p class="pe-ex__uz">Poyezd avtobusdan tezroq.</p>
  <p class="pe-ex__why"><b>のほうが</b> — yuqori tomon, <b>より</b> — past tomon. Ikkalasi bir gapda turishi mumkin va tartibi ham almashishi mumkin.</p>
</div>

<h3>3. どちらが — «qaysi biri?»</h3>

<p>Ikki narsadan bittasini soʻrashning tayyor qolipi bor. Uni butunicha
yodlab qoʻying.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Savol</th><th>Javob</th></tr>
  <tr><td class="pj-res">A と B と、どちらが<ruby>高<rt>たか</rt></ruby>いですか</td>
      <td class="pj-uz">A のほうが<ruby>高<rt>たか</rt></ruby>いです</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Savolda <ruby>何<rt>なに</rt></ruby> ishlatilmaydi.</b> Ikki narsa
  orasidan tanlashda yaponcha doim <b>どちら</b> soʻraydi —
  <ruby>何<rt>なに</rt></ruby> uchta va undan koʻp narsa uchun. Kundalik
  nutqda どちら qisqarib <b>どっち</b> boʻladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">— <ruby>猫<rt>ねこ</rt></ruby>と<ruby>犬<rt>いぬ</rt></ruby>と、どちらが<ruby>好<rt>す</rt></ruby>きですか。<br>— <ruby>猫<rt>ねこ</rt></ruby>のほうが<ruby>好<rt>す</rt></ruby>きです。</p>
  <p class="pe-ex__rom">neko to inu to, dochira ga suki desu ka / neko no hō ga suki desu</p>
  <p class="pe-ex__uz">— Mushuk bilan itdan qaysi biri yoqadi? — Mushuk koʻproq yoqadi.</p>
  <p class="pe-ex__why">Diqqat: ikkala narsa ham <b>と</b> oladi, hatto ikkinchisi ham. Bu qolipning bir qismi.</p>
</div>

<h3>4. いちばん — «eng»</h3>

<p>Uch va undan koʻp narsa ichidan eng ustunini aytish uchun sifat oldiga
<b>いちばん</b> qoʻyiladi. Sifat yana oʻzgarmaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res">〜の<ruby>中<rt>なか</rt></ruby>で</td><td class="pj-uz">…lar ichida</td></tr>
  <tr><td class="pj-res">いちばん + SIFAT</td><td class="pj-uz">eng …</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">クラスの<ruby>中<rt>なか</rt></ruby>でイムロンさんがいちばん<ruby>速<rt>はや</rt></ruby>く<ruby>泳<rt>およ</rt></ruby>げます。</p>
  <p class="pe-ex__rom">kurasu no naka de imuron-san ga ichiban hayaku oyogemasu</p>
  <p class="pe-ex__uz">Sinf ichida Imron eng tez suza oladi.</p>
  <p class="pe-ex__why">いちばん feʼl bilan ham ishlaydi. Va <ruby>速<rt>はや</rt></ruby>い bu yerda <b><ruby>速<rt>はや</rt></ruby>く</b> boʻldi — sifat feʼlni taʼriflaganda く oladi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>いちばん aslida «birinchi oʻrin» degani</b> —
  <ruby>一番<rt>いちばん</rt></ruby>. Shuning uchun u sifatga
  yopishmaydi, oldida alohida turadi. Yozuvda koʻpincha hiragana bilan
  yoziladi.</p>
</div>

<h3>5. Sifat feʼlni taʼriflaganda: 〜く</h3>

<p>Oʻtgan misolda bitta yangi narsa oʻtib ketdi:
<ruby>速<rt>はや</rt></ruby>い → <b><ruby>速<rt>はや</rt></ruby>く</b>.
Sifat <em>otni</em> taʼriflasa oʻzgarmaydi, lekin <em>feʼlni</em>
taʼriflasa い → <b>く</b> boʻladi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">OTNI</p>
    <p><ruby>速<rt>はや</rt></ruby>い<ruby>電車<rt>でんしゃ</rt></ruby></p>
    <p>tez poyezd — sifat oʻzgarmaydi</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">FEʼLNI</p>
    <p><ruby>速<rt>はや</rt></ruby>く<ruby>泳<rt>およ</rt></ruby>ぐ</p>
    <p>tez suzmoq — い <b>く</b> ga</p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>Bu shakl sizga tanish.</b> PJ-25 da inkor
  <ruby>安<rt>やす</rt></ruby><b>く</b>ない edi, PJ-33 da
  <ruby>使<rt>つか</rt></ruby>わな<b>く</b>てもいいです edi. Oʻsha bir
  <b>く</b>. な-sifat esa bu oʻrinda <b>に</b> oladi:
  <ruby>静<rt>しず</rt></ruby>か<b>に</b><ruby>話<rt>はな</rt></ruby>す
  («jimgina gapirmoq»).</p>
</div>

<h3>6. Savol: eng ustuni qaysi</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Nima haqida</th><th>Soʻroq soʻzi</th></tr>
  <tr><td class="pj-uz">narsa</td><td class="pj-res"><ruby>何<rt>なに</rt></ruby>がいちばん…ですか</td></tr>
  <tr><td class="pj-uz">odam</td><td class="pj-res"><ruby>誰<rt>だれ</rt></ruby>がいちばん…ですか</td></tr>
  <tr><td class="pj-uz">joy</td><td class="pj-res">どこがいちばん…ですか</td></tr>
</table></div>

<p>Javobda ham <b>が</b> qoladi:
「<ruby>夏<rt>なつ</rt></ruby>がいちばん<ruby>好<rt>す</rt></ruby>きです」.
Bu — PJ-26 dan beri tanish qoida: taqqoslash va yoqtirish gaplarida
narsa <em>ega</em> boʻlib turadi, は emas <b>が</b> oladi. Toʻrt dars
davomida bir xil qoida turli joyda chiqyapti — yodlab emas, tanib
oling.</p>

<h3>7. Uchtasi bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Nechta narsa</th><th>Misol</th></tr>
  <tr><td class="pj-end">A は B より</td><td class="pj-uz">2</td>
      <td class="pj-res"><ruby>電車<rt>でんしゃ</rt></ruby>はバスより<ruby>速<rt>はや</rt></ruby>いです</td></tr>
  <tr><td class="pj-end">A のほうが</td><td class="pj-uz">2 (tanlov)</td>
      <td class="pj-res"><ruby>電車<rt>でんしゃ</rt></ruby>のほうが<ruby>速<rt>はや</rt></ruby>いです</td></tr>
  <tr><td class="pj-end">いちばん</td><td class="pj-uz">3+</td>
      <td class="pj-res"><ruby>電車<rt>でんしゃ</rt></ruby>がいちばん<ruby>速<rt>はや</rt></ruby>いです</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ バスは<ruby>電車<rt>でんしゃ</rt></ruby>より<ruby>速<rt>はや</rt></ruby>いです («avtobus tezroq» demoqchi boʻlib)</p>
  <p class="pe-fix__good">✓ より <b>past</b> tomonni belgilaydi. Bu gap «avtobus poyezddan tez» degani — yaʼni teskari.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>猫<rt>ねこ</rt></ruby>と<ruby>犬<rt>いぬ</rt></ruby>、<ruby>何<rt>なに</rt></ruby>が<ruby>好<rt>す</rt></ruby>きですか</p>
  <p class="pe-fix__good">✓ <ruby>猫<rt>ねこ</rt></ruby>と<ruby>犬<rt>いぬ</rt></ruby><b>と、どちら</b>が<ruby>好<rt>す</rt></ruby>きですか — ikki narsa uchun <b>どちら</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ いちばん<ruby>高<rt>たか</rt></ruby>いいです</p>
  <p class="pe-fix__good">✓ いちばん<ruby>高<rt>たか</rt></ruby>いです — sifat <b>oʻzgarmaydi</b>, いちばん shunchaki oldida turadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Poyezd avtobusdan tez» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>電車<rt>でんしゃ</rt></ruby>はバスより<ruby>速<rt>はや</rt></ruby>いです。</b> より past tomonda.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. より qaysi tomonni belgilaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Past</b> tomonni — oʻzidan oldingi narsa kamroq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Ikki narsadan qaysi biri deb qanday soʻraysiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>A と B と、どちらが…ですか。</b> <ruby>何<rt>なに</rt></ruby> emas — u uchta va undan koʻp narsa uchun.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Sifat taqqoslashda oʻzgaradimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> <ruby>高<rt>たか</rt></ruby>い har doim <ruby>高<rt>たか</rt></ruby>い. Ishni qoʻshimchalar bajaradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Sinfda eng tez» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>クラスの<ruby>中<rt>なか</rt></ruby>でいちばん<ruby>速<rt>はや</rt></ruby>いです。</b></p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜より</b> — …dan koʻra (past tomon)</li>
  <li><b>〜のほうが</b> — … tomoni koʻproq (yuqori tomon)</li>
  <li><b>どちら</b> — qaysi biri (ikkitasidan bittasi)</li>
  <li><b>いちばん</b> — eng</li>
  <li><b>〜の<ruby>中<rt>なか</rt></ruby>で</b> — …lar ichida</li>
  <li><b><ruby>電車<rt>でんしゃ</rt></ruby></b> — poyezd</li>
  <li><b><ruby>速<rt>はや</rt></ruby>い</b> — tez</li>
  <li><b><ruby>山<rt>やま</rt></ruby></b> — togʻ, tepalik</li>
  <li><b>クラス</b> — sinf, oʻquv guruhi</li>
  <li><b><ruby>夏<rt>なつ</rt></ruby></b> — yoz</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Sifat <b>oʻzgarmaydi</b> — ishni qoʻshimchalar bajaradi.</li>
    <li><b>より</b> past tomonda, <b>のほうが</b> yuqori tomonda.</li>
    <li>Ikkita narsa — <b>どちら</b>; uchta va undan koʻp — <b>いちばん</b>.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-45: Oddiy shakl (普通体) — 丁寧体 dan oʻtish",
        "category": "japanese",
        "order": 45,
        "summary": (
            "Kursning ikkinchi burilish nuqtasi. Kitob, gazeta, kundalik "
            "va doʻstlar bilan suhbat — hammasi shu shaklda. Va siz uni "
            "allaqachon bilasiz."
        ),
        "stories": ["にっき — はじめての でんしゃ"],
        "content": """
<h2>PJ-45: Oddiy shakl (<ruby>普通体<rt>ふつうたい</rt></ruby>) — <ruby>丁寧体<rt>ていねいたい</rt></ruby> dan oʻtish</h2>

<p>Qirq toʻrt dars davomida siz bitta uslubda gapirdingiz:
<b><ruby>丁寧体<rt>ていねいたい</rt></ruby></b> — です・ます uslubi.
U muloyim, ishonchli va deyarli hech qachon xato boʻlmaydi.</p>

<p>Lekin yapon kitobi, gazetasi, romani va kundaligi <b>bu uslubda
yozilmaydi</b>. Doʻstlar ham bunday gaplashmaydi. Ular
<b><ruby>普通体<rt>ふつうたい</rt></ruby></b> — oddiy shaklni
ishlatadi.</p>

<p>Yaxshi xabar: siz uni allaqachon bilasiz. Lugʻat shakli, ない-shakli,
た-shakli — hammasi <ruby>普通体<rt>ふつうたい</rt></ruby> ning oʻzi va
siz ularni PJ-28, PJ-34, PJ-35 da yasagansiz. Bugun faqat ularni
<em>bir jadvalga</em> yigʻamiz va otlar bilan sifatlarni ham shu
tizimga qoʻshamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Feʼlning toʻrtta oddiy shaklini bir jadvalda koʻrasiz</li>
    <li>Sifat va otni oddiy shaklga oʻtkazasiz</li>
    <li>だ ning qachon tushib qolishini bilib olasiz</li>
    <li>Qaysi uslubni qachon tanlashni tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki uslub, bir til</span>
  <span class="pe-chip pe-chip--v"><ruby>行<rt>い</rt></ruby>きます</span>
  <span class="pe-op">↔</span>
  <span class="pe-chip pe-chip--s"><ruby>行<rt>い</rt></ruby>く</span>
</div>

<h3>1. Feʼl — hammasi tanish</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th><ruby>丁寧体<rt>ていねいたい</rt></ruby></th><th><ruby>普通体<rt>ふつうたい</rt></ruby></th><th>Qayerdan tanish</th></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-uz"><ruby>行<rt>い</rt></ruby>きます</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>く</td><td class="pj-uz">PJ-28 lugʻat shakli</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-uz"><ruby>行<rt>い</rt></ruby>きません</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>かない</td><td class="pj-uz">PJ-34 ない-shakli</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-uz"><ruby>行<rt>い</rt></ruby>きました</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>った</td><td class="pj-uz">PJ-35 た-shakli</td></tr>
  <tr><td class="pj-stem">oʻtgan inkor</td><td class="pj-uz"><ruby>行<rt>い</rt></ruby>きませんでした</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>かなかった</td><td class="pj-uz"><b>yangi</b></td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Faqat bitta shakl yangi.</b> <ruby>行<rt>い</rt></ruby>か<b>なかった</b>
  — bu ない ning oʻtgan zamoni, va ない い-sifat boʻlgani uchun u
  PJ-25 qoidasi boʻyicha yasaladi: い → かった. Yaʼni yangi qoida ham
  emas — eskisining yangi joyda ishlashi.</p>
</div>

<h3>2. い-sifat — です ni olib tashlang</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th><ruby>丁寧体<rt>ていねいたい</rt></ruby></th><th><ruby>普通体<rt>ふつうたい</rt></ruby></th></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-uz"><ruby>安<rt>やす</rt></ruby>いです</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>い</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-uz"><ruby>安<rt>やす</rt></ruby>くないです</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>くない</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-uz"><ruby>安<rt>やす</rt></ruby>かったです</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>かった</td></tr>
  <tr><td class="pj-stem">oʻtgan inkor</td><td class="pj-uz"><ruby>安<rt>やす</rt></ruby>くなかったです</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>くなかった</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>い-sifat eng oson.</b> です ni olib tashlaysiz — tamom. Bu PJ-25
  da aytgan gapning isboti: <em>sifat oʻzi kesim, です faqat muloyimlik
  uchun</em>. Muloyimlik kerak boʻlmasa, です ham kerak emas.</p>
</div>

<h3>3. な-sifat va ot — だ paydo boʻladi</h3>

<p>Bu yerda esa yangi soʻz keladi: <b>だ</b> — です ning oddiy shakli.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th><ruby>丁寧体<rt>ていねいたい</rt></ruby></th><th><ruby>普通体<rt>ふつうたい</rt></ruby></th></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-uz"><ruby>学生<rt>がくせい</rt></ruby>です</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>だ</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-uz"><ruby>学生<rt>がくせい</rt></ruby>ではありません</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>じゃない</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-uz"><ruby>学生<rt>がくせい</rt></ruby>でした</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>だった</td></tr>
  <tr><td class="pj-stem">oʻtgan inkor</td><td class="pj-uz"><ruby>学生<rt>がくせい</rt></ruby>ではありませんでした</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>じゃなかった</td></tr>
</table></div>

<p>な-sifat ham xuddi shunday, chunki u PJ-26 dan beri <b>ot kabi</b>
tuslanadi: <ruby>静<rt>しず</rt></ruby>かだ,
<ruby>静<rt>しず</rt></ruby>かじゃない,
<ruby>静<rt>しず</rt></ruby>かだった.</p>

<div class="pe-call pe-warn">
  <p><b>じゃ — ではの qisqargan shakli.</b> ではない ham toʻgʻri va u
  rasmiyroq, kitobiy eshitiladi. Kundalik nutqda esa deyarli doim
  <b>じゃない</b>. Ikkalasini ham tanib oling.</p>
</div>

<h3>4. だ koʻpincha tushib qoladi</h3>

<p>Mana kutilmagan qismi. Ogʻzaki nutqda <b>だ</b> koʻpincha umuman
aytilmaydi — ayniqsa savolda va ayollar nutqida.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">YOZUVDA</p>
    <p><ruby>学生<rt>がくせい</rt></ruby>だ。</p>
    <p>Kitob, maqola, kundalik.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">SUHBATDA</p>
    <p><ruby>学生<rt>がくせい</rt></ruby>？</p>
    <p>だ tushadi. Ohang savolni koʻrsatadi.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Feʼl bilan bunday boʻlmaydi</b> —
  <ruby>行<rt>い</rt></ruby>く hech qachon qisqarmaydi. Faqat
  <b>だ</b> tushadi, chunki u boglama, yaʼni maʼno tashimaydigan
  boʻlak. Oʻzbekchada ham «U talaba» deymiz — «U talaba<em>dir</em>»
  demaymiz. Boglama ikki tilda ham eng oson tushib qoladigan qism.</p>
</div>

<h3>5. Qaysi uslubni qachon</h3>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name"><ruby>普通体<rt>ふつうたい</rt></ruby></span>
    <span class="pj-level__ja"><ruby>行<rt>い</rt></ruby>く</span>
    <span class="pj-level__who">oila, yaqin doʻst, kundalik, kitob, gazeta</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name"><ruby>丁寧体<rt>ていねいたい</rt></ruby></span>
    <span class="pj-level__ja"><ruby>行<rt>い</rt></ruby>きます</span>
    <span class="pj-level__who">ustoz, begona, ish, xizmat — eng koʻp ishlatiladigan</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p><b>Shubha boʻlsa — です・ます.</b> Ortiqcha muloyimlik hech qachon
  xato emas; yetarli boʻlmagan muloyimlik esa haqoratdek eshitilishi
  mumkin. Yaponiyada oʻqiyotgan chet ellik <ruby>普通体<rt>ふつうたい</rt></ruby>
  ni <em>oʻqiy</em> biladi, lekin gapirganda deyarli doim
  <ruby>丁寧体<rt>ていねいたい</rt></ruby> ishlatadi. Siz ham shunday
  qiling.</p>
</div>

<h3>6. Nega baribir oʻrganish kerak</h3>

<p>Sababi oddiy: <b>keyingi grammatikaning yarmi undan yasaladi</b>.
〜と<ruby>思<rt>おも</rt></ruby>います, 〜とき, 〜たら, 〜ので —
hammasi oldida oddiy shaklni talab qiladi. Yaʼni siz uni gapirish uchun
emas, <em>gap qurish</em> uchun oʻrganasiz.</p>

<p>Buni shunday tasavvur qiling: <ruby>丁寧体<rt>ていねいたい</rt></ruby>
— gapning <b>tashqi kiyimi</b>, va u faqat eng oxirida koʻrinadi.
Gapning ichida esa hamma narsa oddiy shaklda turadi, chunki u yerda
kimga gapirayotganingiz muhim emas — u yerda faqat <em>maʼno</em>
bor.</p>

<p>Shuning uchun bu dars Blok D ning boshi. Undan keyingi oʻn yetti dars
gaplarni bir-biriga ulashni oʻrgatadi, va har birida oddiy shakl gapning
ichida turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>明日<rt>あした</rt></ruby><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ると<ruby>思<rt>おも</rt></ruby>います。</p>
  <p class="pe-ex__rom">ashita ame ga furu to omoimasu</p>
  <p class="pe-ex__uz">Ertaga yomgʻir yogʻadi deb oʻylayman.</p>
  <p class="pe-ex__why">Gap oxiri <b>muloyim</b> (<ruby>思<rt>おも</rt></ruby>います), lekin ichkarisi <b>oddiy shaklda</b> (<ruby>降<rt>ふ</rt></ruby>る). Bu — keyingi darslarning asosiy qolipi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>安<rt>やす</rt></ruby>いだ</p>
  <p class="pe-fix__good">✓ <ruby>安<rt>やす</rt></ruby>い — <b>い-sifatga だ qoʻshilmaydi</b>. だ faqat ot va な-sifat bilan.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>きませんでした → <ruby>行<rt>い</rt></ruby>かないだった</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>か<b>なかった</b> — ない い-sifat, demak い → かった.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Ustozga: <ruby>行<rt>い</rt></ruby>く</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>きます — kattaroq odamga doim <ruby>丁寧体<rt>ていねいたい</rt></ruby>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>食<rt>た</rt></ruby>べませんでした ni oddiy shaklga oʻtkazing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>食<rt>た</rt></ruby>べなかった</b> — ない → なかった.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>安<rt>やす</rt></ruby>いです ni oddiy shaklga oʻtkazing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>安<rt>やす</rt></ruby>い</b> — です ni olib tashlang, xolos. だ qoʻshilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>学生<rt>がくせい</rt></ruby>ではありません ni oddiy shaklga oʻtkazing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>学生<rt>がくせい</rt></ruby>じゃない</b> (yoki rasmiyroq: <ruby>学生<rt>がくせい</rt></ruby>ではない).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Ustoz bilan qaysi uslubda gapirasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>丁寧体<rt>ていねいたい</rt></ruby></b> — です・ます. Shubha boʻlsa doim shuni tanlang.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega oddiy shaklni oʻrganish kerak?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki keyingi grammatikaning yarmi — 〜と<ruby>思<rt>おも</rt></ruby>います, 〜とき, 〜たら — <b>oldida oddiy shaklni talab qiladi</b>.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>普通体<rt>ふつうたい</rt></ruby></b> — oddiy shakl</li>
  <li><b><ruby>丁寧体<rt>ていねいたい</rt></ruby></b> — muloyim shakl</li>
  <li><b>だ</b> — です ning oddiy shakli</li>
  <li><b>じゃない</b> — ではありません ning oddiy shakli</li>
  <li><b>だった</b> — でした ning oddiy shakli</li>
  <li><b>〜なかった</b> — oʻtgan zamon inkori</li>
  <li><b><ruby>日記<rt>にっき</rt></ruby></b> — kundalik</li>
  <li><b><ruby>雨<rt>あめ</rt></ruby></b> — yomgʻir</li>
  <li><b><ruby>降<rt>ふ</rt></ruby>る</b> — yogʻmoq (I guruh)</li>
  <li><b><ruby>思<rt>おも</rt></ruby>う</b> — oʻylamoq (I guruh)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Feʼlda faqat <b>bitta</b> shakl yangi: 〜なかった.</li>
    <li><b>だ faqat ot va な-sifat bilan</b> — い-sifatga qoʻshilmaydi.</li>
    <li>Gapirganda <b>です・ます</b>; oddiy shakl esa <b>gap qurish</b> uchun.</li>
  </ul>
</div>
""",
    },
]
