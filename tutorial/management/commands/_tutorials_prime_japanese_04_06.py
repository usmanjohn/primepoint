# -*- coding: utf-8 -*-
"""Prime Japanese — Block A, darslar 4–6 (hiragananing oxiri).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_JAPANESE.md
Lesson list: tutorial/management/commands/toc_prime_japanese.txt

Block A darslarida grammatika yoʻq, shuning uchun oʻqish matni ham yoʻq.
Har bir darsning ikkinchi boʻlagi — 12 savollik mashq:
practice/management/commands/_practice_pj_04_06.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_04_06.py --author=prime
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
        "title": "PJ-4: Hiragana 3 — ま み む め も · や ゆ よ · ら り る れ ろ · わ を ん",
        "category": "japanese",
        "order": 4,
        "summary": (
            "Hiragananing oxirgi 16 belgisi. Dars oxirida siz butun asosiy alifboni "
            "bilasiz va yaponcha salomlashishni oʻz koʻzingiz bilan oʻqiysiz."
        ),
        "content": """
<h2>PJ-4: Hiragana 3 — ま み む め も · や ゆ よ · ら り る れ ろ · わ を ん</h2>

<p>Bugun hiragana tugaydi. Oʻttiz belgini bilasiz, qoladi — oʻn oltitasi. Va bu
darsning oxirida sizni mukofot kutmoqda: yaponlar kuniga necha marta aytadigan
uchta soʻzni — <b>こんにちは</b>, <b>おはよう</b>, <b>さようなら</b> — hech kimning
yordamisiz oʻqiysiz. Yoʻlda ikkita gʻalati belgi uchraydi: <b>を</b>, faqat
grammatika uchun ishlatiladigan harf, va <b>ん</b>, butun alifboda yolgʻiz oʻzi
turadigan yagona undosh.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ま-, や-, ら- va わ-qatorlarini toʻliq oʻqiysiz</li>
    <li>Yaponcha <b>r</b> ni oʻzbekcha <b>r</b> dan ajratasiz — titratmaslikni oʻrganasiz</li>
    <li>を nega [o] deb oʻqilishini va qayerda ishlatilishini bilasiz</li>
    <li>ん ning uchta xususiyatini tushunasiz va yaponcha salomlashishni oʻqiysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bugungi uchta gʻayrioddiy belgi</span>
  <span class="pe-chip pe-chip--neg">や-qatorida 3 ta</span>
  <span class="pe-chip pe-chip--neg">を = [o]</span>
  <span class="pe-chip pe-chip--neg">ん = yolgʻiz undosh</span>
</div>

<h3>1. ま-qatori — hech qanday istisnosiz</h3>

<p>Yaxshi xabar bilan boshlaymiz: bu beshtasida hech qanday tuzoq yoʻq. Qanday
yozilsa, shunday oʻqiladi.</p>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">ま</span><span class="pj-kana__rom">ma</span>
    <span class="pj-kana__uz">ま = m + a</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">み</span><span class="pj-kana__rom">mi</span>
    <span class="pj-kana__uz">み = m + i</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">む</span><span class="pj-kana__rom">mu</span>
    <span class="pj-kana__uz">む = m + u</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">め</span><span class="pj-kana__rom">me</span>
    <span class="pj-kana__uz">め = m + e</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">も</span><span class="pj-kana__rom">mo</span>
    <span class="pj-kana__uz">も = m + o</span></div>
</div>

<div class="pe-call pe-tip">
  <p><b>め va ぬ</b> — yana bir oʻxshash juftlik. Farqi bitta: <b>ぬ</b> ning dumi
  halqa hosil qiladi, <b>め</b> da halqa yoʻq — dumi shunchaki chiqib ketadi.
  Halqani qidiring.</p>
</div>

<h3>2. や-qatori — nega faqat uchta?</h3>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">や</span><span class="pj-kana__rom">ya</span>
    <span class="pj-kana__uz">や = y + a</span></div>
  <div class="pj-kana__gap"></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">ゆ</span><span class="pj-kana__rom">yu</span>
    <span class="pj-kana__uz">ゆ = y + u</span></div>
  <div class="pj-kana__gap"></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">よ</span><span class="pj-kana__rom">yo</span>
    <span class="pj-kana__uz">よ = y + o</span></div>
</div>

<p>Boʻsh katakchalar tasodifiy emas. "yi" va "ye" tovushlari yapon tilida
<b>mavjud emas</b> — shuning uchun ular uchun belgi ham yoʻq. Jadvaldagi boʻshliq
tilning oʻzidagi boʻshliqni koʻrsatadi.</p>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek oʻquvchi uchun tanish narsa.</b> Oʻzbekchada ham "ya", "yu", "yo"
  bor — <em>yaxshi</em>, <em>yulduz</em>, <em>yoʻl</em>. Ular ham bitta harfda emas,
  ikki tovushdan iborat. Yaponchada esa bu uchtasi bitta belgi bilan yoziladi.
  Bu belgilar keyinroq juda muhim boʻladi: PJ-6 da ular kichraytirilib boshqa
  belgiga yopishtiriladi va butun bir yangi tovushlar guruhini hosil qiladi.</p>
</div>

<h3>3. ら-qatori — kursdagi eng koʻp buziladigan tovush</h3>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">ら</span><span class="pj-kana__rom">ra</span>
    <span class="pj-kana__uz">titratilmaydi</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">り</span><span class="pj-kana__rom">ri</span>
    <span class="pj-kana__uz">い ga oʻxshaydi — ehtiyot</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">る</span><span class="pj-kana__rom">ru</span>
    <span class="pj-kana__uz">pastida <b>halqa</b> bor</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">れ</span><span class="pj-kana__rom">re</span>
    <span class="pj-kana__uz">dumi tashqariga chiqadi</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">ろ</span><span class="pj-kana__rom">ro</span>
    <span class="pj-kana__uz">halqasi <b>yoʻq</b></span></div>
</div>

<p>Lotin yozuvida bu qator <b>r</b> harfi bilan beriladi, lekin bu oʻzbekcha
<b>r</b> emas. Yaponcha ら tovushida <b>til tanglayga bir marta yengil urib
oʻtadi</b> — titramaydi, takrorlanmaydi. Natijada chetdan qaraganda u
oʻzbekcha <em>r</em>, <em>l</em> va <em>d</em> orasidagi tovushga oʻxshaydi.</p>

<div class="pj-say">
  <span class="pj-say__from">さくら</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[sakura]</span>
  <span class="pj-say__why">ら da til bir marta tegib oʻtadi, "rrr" boʻlmaydi</span>
</div>

<div class="pe-call pe-warn">
  <p><b>Buni hozir toʻgʻrilash oson, keyinroq qiyin.</b> Oʻzbek tilida <em>r</em>
  titraydi va bu odat avtomatik ishlaydi. Har bir ら-qatori soʻzini sekin, tilni
  <em>bir marta</em> urib mashq qiling. Bir haftalik odat butun umr eshitiladigan
  aksentdan qutqaradi.</p>
</div>

<h3>4. わ-qatori, を va ん</h3>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">わ</span><span class="pj-kana__rom">wa</span>
    <span class="pj-kana__uz">わ = w + a</span></div>
  <div class="pj-kana__gap"></div>
  <div class="pj-kana__gap"></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">を</span><span class="pj-kana__rom">o</span>
    <span class="pj-kana__uz">"wo" EMAS — [o]</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">ん</span><span class="pj-kana__rom">n</span>
    <span class="pj-kana__uz">yolgʻiz undosh</span></div>
</div>

<p><b>を</b> — butun alifbodagi eng gʻalati belgi. U <b>[o]</b> deb oʻqiladi,
xuddi お kabi. Unda nega ikkita bir xil belgi kerak? Chunki を <em>hech qachon
soʻz ichida ishlatilmaydi</em>. Uning bitta vazifasi bor: toʻldiruvchini
belgilaydigan grammatik qoʻshimcha boʻlish. Yaʼni を ni koʻrsangiz, bu soʻz emas —
bu grammatika.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n">すし</span>
  <span class="pj-joshi__p">を<small>TOʻLDIRUVCHI</small></span>
  <span class="pj-joshi__uz">sushi<b>ni</b> … — oʻzbekchadagi <em>-ni</em> qoʻshimchasi bilan bir xil ish. PJ-21 da toʻliq koʻramiz.</span>
</div>

<p><b>ん</b> — alifbodagi yagona belgi, u <em>unlisiz</em>. Uning uchta muhim
xususiyati bor:</p>

<ol class="pe-steps">
  <li><b>Hech qachon soʻz boshida kelmaydi.</b> Yaponchada ん bilan boshlanadigan soʻz yoʻq.</li>
  <li><b>Toʻliq bitta zarb</b> (mora). にほん — "ni-ho-n", ikkita emas, <b>uchta</b> zarb. Bu yapon tilidagi ritmning asosi.</li>
  <li><b>Tovushi keyingi harfga moslashadi.</b> Baʼzida "n", baʼzida "m", baʼzida burun orqali "ng" boʻlib chiqadi. Buni PJ-6 da toʻliq koʻramiz — u yerda ば va ぱ qatorlari keladi.</li>
</ol>

<h3>5. Mukofot: birinchi haqiqiy soʻzlaringiz</h3>

<p>Endi butun asosiy hiraganani bilasiz. Yaponlar kuniga eng koʻp aytadigan
soʻzlarni oʻqing:</p>

<div class="pe-ex">
  <p class="pe-ex__ja">こんにちは</p>
  <p class="pe-ex__rom">konnichiwa</p>
  <p class="pe-ex__uz">Assalomu alaykum. (kunduzi)</p>
  <p class="pe-ex__why">Oxiridagi は — <b>[wa]</b>, "ha" emas. PJ-3 dagi qoida esingizdami? Bu soʻz aslida grammatik qoʻshimcha bilan tugaydi, shuning uchun は shunday oʻqiladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">おはよう</p>
  <p class="pe-ex__rom">ohayō</p>
  <p class="pe-ex__uz">Xayrli tong.</p>
  <p class="pe-ex__why">Oxiridagi よう — uzun "o" beradi va lotin yozuvida <b>ō</b> deb belgilanadi. Uzun unlilarni PJ-5 da batafsil koʻramiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">さようなら</p>
  <p class="pe-ex__rom">sayōnara</p>
  <p class="pe-ex__uz">Xayr. (uzoq vaqtga)</p>
  <p class="pe-ex__why">Beshta belgi, ikkitasi bugun oʻrgangan ら-qatoridan. ら ni titratmang.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yaponcha</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td>やま</td><td class="pj-res">yama</td><td class="pj-uz">togʻ</td></tr>
  <tr><td>うみ</td><td class="pj-res">umi</td><td class="pj-uz">dengiz</td></tr>
  <tr><td>そら</td><td class="pj-res">sora</td><td class="pj-uz">osmon</td></tr>
  <tr><td>とり</td><td class="pj-res">tori</td><td class="pj-uz">qush</td></tr>
  <tr><td>くるま</td><td class="pj-res">kuruma</td><td class="pj-uz">mashina</td></tr>
  <tr><td>ゆき</td><td class="pj-res">yuki</td><td class="pj-uz">qor</td></tr>
  <tr><td>よる</td><td class="pj-res">yoru</td><td class="pj-uz">tun</td></tr>
  <tr><td>あめ</td><td class="pj-res">ame</td><td class="pj-uz">yomgʻir</td></tr>
  <tr><td>ほん</td><td class="pj-res">hon</td><td class="pj-uz">kitob</td></tr>
  <tr><td>にほん</td><td class="pj-res">nihon</td><td class="pj-uz">Yaponiya</td></tr>
  <tr><td>せんせい</td><td class="pj-res">sensē</td><td class="pj-uz">oʻqituvchi</td></tr>
  <tr><td>こころ</td><td class="pj-res">kokoro</td><td class="pj-uz">yurak, qalb</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>にほん</b> ni ajratib koʻring: <em>ni</em> (quyosh) + <em>hon</em> (asos) =
  "quyosh chiqadigan yer". Oʻzbekchada ham Yaponiyani baʼzan "Kunchiqar mamlakat"
  deb ataymiz — bu aynan shu soʻzning tarjimasi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ら-qatorini oʻzbekcha "r" kabi titratib aytish: "sakurrra"</p>
  <p class="pe-fix__good">✓ Til tanglayga <b>bir marta</b> yengil uriladi: [sakura]. Titrash yaponchada umuman yoʻq.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ を ni "wo" deb oʻqish</p>
  <p class="pe-fix__good">✓ <b>[o]</b>. "wo" — bu belgining eski nomi va kompyuterda uni yozish usuli, lekin bugungi yapon tilida u sof [o] deb aytiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ り va い ni adashtirish</p>
  <p class="pe-fix__good">✓ <b>い</b> — ikkita qisqa, alohida chiziq. <b>り</b> — oʻng chizigʻi uzun va pastga egilib ketadi. Uzunligiga qarang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <b>くるま</b> qanday oʻqiladi va nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>kuruma</b> — mashina. る dagi r ni titratmang.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Nega や-qatorida faqat uchta belgi bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yapon tilida "yi" va "ye" tovushlari <b>mavjud emas</b>, shuning uchun ular uchun belgi ham yoʻq. Jadvaldagi boʻshliq tilning oʻzidagi boʻshliqni koʻrsatadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <b>を</b> qayerda ishlatiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Faqat <b>grammatik qoʻshimcha</b> sifatida — toʻldiruvchini belgilaydi. Soʻz ichida hech qachon ishlatilmaydi. Oʻqilishi [o].</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <b>にほん</b> soʻzida nechta zarb (mora) bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Uchta</b>: に-ほ-ん. ん toʻliq bitta zarb sanaladi — bu yapon ritmining asosiy qoidasi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <b>こんにちは</b> oxiridagi は qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>[wa]</b>. Bu soʻz grammatik qoʻshimcha bilan tugaydi, shuning uchun は "ha" emas, [wa] boʻlib oʻqiladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>やま</b> — togʻ</li>
  <li><b>うみ</b> — dengiz</li>
  <li><b>そら</b> — osmon</li>
  <li><b>くるま</b> — mashina</li>
  <li><b>ゆき</b> — qor</li>
  <li><b>ほん</b> — kitob</li>
  <li><b>にほん</b> — Yaponiya</li>
  <li><b>せんせい</b> — oʻqituvchi</li>
  <li><b>こんにちは</b> — assalomu alaykum (kunduzi)</li>
  <li><b>さようなら</b> — xayr</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Yaponcha <b>r</b> titratilmaydi — til bir marta urib oʻtadi.</li>
    <li><b>を</b> = [o], faqat grammatik qoʻshimcha; <b>ん</b> — yolgʻiz undosh, soʻz boshida kelmaydi va toʻliq bitta zarb sanaladi.</li>
    <li>Asosiy hiragana tugadi: <b>46 ta belgi</b>. Endi こんにちは ni oʻzingiz oʻqiy olasiz.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-5: Hiragana 4 — butun 五十音図 ni oʻqish, soʻzlarni yigʻamiz",
        "category": "japanese",
        "order": 5,
        "summary": (
            "Yangi belgi yoʻq — bugun 46 tasini birga ishlatamiz. Uzun unlilar, yapon "
            "ritmi (mora) va tez oʻqish koʻnikmasi."
        ),
        "content": """
<h2>PJ-5: Hiragana 4 — butun 五十音図 ni oʻqish, soʻzlarni yigʻamiz</h2>

<p>Bugun bitta ham yangi belgi yoʻq. Aynan shuning uchun bu dars muhim: siz 46 ta
belgini <em>bilasiz</em>, lekin hali <em>tez oʻqiy olmaysiz</em>. Farqi katta.
Belgini eslash uchun ikki soniya oʻylash — bu hali oʻqish emas. Bugun shu ikki
soniyani nolga tushiramiz, uzun unlilarni hal qilamiz va yapon tilining ritmini
oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Butun 五十音図 (gojūon) jadvalini bir joyda koʻrasiz va uning mantiqini tushunasiz</li>
    <li>Uzun unlilarni yozilishidan tanib olasiz: おう, えい, ああ</li>
    <li>Yapon ritmini — <b>mora</b> ni — hisoblashni oʻrganasiz</li>
    <li>Uzun soʻzlarni toʻxtamasdan oʻqiysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bugungi uchta ish</span>
  <span class="pe-chip pe-chip--s">JADVAL</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">UZUN UNLI</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">RITM</span>
</div>

<h3>1. 五十音図 — "ellik tovush jadvali"</h3>

<p>Yaponlar hiraganani alifbo tartibida emas, <b>jadval</b> shaklida oʻrganadi.
Chapdagi ustun — undosh, tepadagi qator — unli. Har bir katak ularning
kesishmasi. Jadvalning nomi <b>五十音図</b> — "ellik tovush jadvali", garchi
bugun 46 ta belgi qolgan boʻlsa ham.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qator</th><th>a</th><th>i</th><th>u</th><th>e</th><th>o</th></tr>
  <tr><td class="pj-stem">—</td><td>あ</td><td>い</td><td>う</td><td>え</td><td>お</td></tr>
  <tr><td class="pj-stem">k</td><td>か</td><td>き</td><td>く</td><td>け</td><td>こ</td></tr>
  <tr><td class="pj-stem">s</td><td>さ</td><td class="pj-end">し</td><td>す</td><td>せ</td><td>そ</td></tr>
  <tr><td class="pj-stem">t</td><td>た</td><td class="pj-end">ち</td><td class="pj-end">つ</td><td>て</td><td>と</td></tr>
  <tr><td class="pj-stem">n</td><td>な</td><td>に</td><td>ぬ</td><td>ね</td><td>の</td></tr>
  <tr><td class="pj-stem">h</td><td>は</td><td>ひ</td><td class="pj-end">ふ</td><td>へ</td><td>ほ</td></tr>
  <tr><td class="pj-stem">m</td><td>ま</td><td>み</td><td>む</td><td>め</td><td>も</td></tr>
  <tr><td class="pj-stem">y</td><td>や</td><td>—</td><td>ゆ</td><td>—</td><td>よ</td></tr>
  <tr><td class="pj-stem">r</td><td>ら</td><td>り</td><td>る</td><td>れ</td><td>ろ</td></tr>
  <tr><td class="pj-stem">w</td><td>わ</td><td>—</td><td>—</td><td>—</td><td>を</td></tr>
  <tr><td class="pj-stem">—</td><td>ん</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
</table></div>

<p>Yashil rangdagi beshta belgi — siz bilgan istisnolar: <b>し</b> (shi),
<b>ち</b> (chi), <b>つ</b> (tsu), <b>ふ</b> (fu). Boshqa hammasi jadvalga
toʻliq boʻysunadi.</p>

<div class="pe-call pe-rule">
  <p><b>Bu jadval — shunchaki oʻrganish vositasi emas.</b> Yapon grammatikasining
  yarmi shu jadval boʻylab harakat qiladi: feʼl tuslanganda uning oxirgi
  boʻgʻini shu qator ichida <em>yuqoriga yoki pastga</em> siljiydi. Masalan
  よむ → よみます — む dan み ga, yaʼni u-qatoridan i-qatoriga. PJ-27 da bu
  butun tizim ochiladi. Shuning uchun jadvalni yodda saqlang.</p>
</div>

<h3>2. Uzun unlilar — bir zarb emas, ikki zarb</h3>

<p>Yapon tilida unlining <b>uzunligi maʼnoni oʻzgartiradi</b>. Bu oʻzbek tilida
deyarli sezilmaydigan narsa, shuning uchun alohida eʼtibor talab qiladi.
Hiraganada uzunlik oddiy usul bilan koʻrsatiladi: <b>yana bitta unli
qoʻshiladi</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yozilishi</th><th>Qanday uzayadi</th><th>Oʻqilishi</th><th>Misol</th></tr>
  <tr><td class="pj-stem">あ + あ</td><td>a → aa</td><td class="pj-res">ā</td><td>おかあさん — ona</td></tr>
  <tr><td class="pj-stem">い + い</td><td>i → ii</td><td class="pj-res">ī</td><td>おおきい — katta</td></tr>
  <tr><td class="pj-stem">う + う</td><td>u → uu</td><td class="pj-res">ū</td><td>ゆうき — jasorat</td></tr>
  <tr><td class="pj-stem">え + い</td><td>e → ei</td><td class="pj-res">ē</td><td>せんせい — oʻqituvchi</td></tr>
  <tr><td class="pj-stem">お + う</td><td>o → ou</td><td class="pj-res">ō</td><td>おはよう — xayrli tong</td></tr>
</table></div>

<p>Oxirgi ikkitasi eng chalgʻituvchi. <b>えい</b> yozilsa ham, "e-i" deb ikkita
alohida tovush aytilmaydi — u shunchaki <b>uzun e</b> boʻladi. Xuddi shunday
<b>おう</b> = uzun o.</p>

<div class="pj-say">
  <span class="pj-say__from">せんせい</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[sensē]</span>
  <span class="pj-say__why">えい — "sen-se-i" emas, uzun e</span>
</div>

<div class="pe-call pe-warn">
  <p><b>Uzunlik — bu shunchaki chiroy emas.</b> Ikkita soʻz faqat unli uzunligi
  bilan farq qilishi mumkin va maʼnosi butunlay boshqa boʻladi:
  <b>ゆき</b> (qor) va <b>ゆうき</b> (jasorat). Bir zarb qisqartirsangiz,
  boshqa soʻz aytgan boʻlasiz. Uzun unlini <em>haqiqatan ham</em> ikki barobar
  uzoq ushlang.</p>
</div>

<h3>3. Mora — yapon tilining zarbi</h3>

<p>Yapon tili <b>bir tekis ritm</b>da gapiriladi. Har bir kana bitta zarbga teng
va bu zarb <b>mora</b> deb ataladi. Zarblar bir xil uzunlikda boʻladi — hech
biri ikkinchisidan tez yoki sekin emas.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Zarblar</th><th>Nechta</th><th>Maʼnosi</th></tr>
  <tr><td>やま</td><td class="pj-res">や · ま</td><td>2</td><td class="pj-uz">togʻ</td></tr>
  <tr><td>にほん</td><td class="pj-res">に · ほ · ん</td><td>3</td><td class="pj-uz">Yaponiya</td></tr>
  <tr><td>せんせい</td><td class="pj-res">せ · ん · せ · い</td><td>4</td><td class="pj-uz">oʻqituvchi</td></tr>
  <tr><td>おかあさん</td><td class="pj-res">お · か · あ · さ · ん</td><td>5</td><td class="pj-uz">ona</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha bilan farq shu yerda.</b> Oʻzbek tilida boʻgʻinlar turli
  uzunlikda boʻladi va urgʻu bitta boʻgʻinni kuchaytiradi. Yapon tilida esa
  hamma zarb teng — soʻzni <em>sanagandek</em> aytasiz. <b>ん</b> ham,
  uzun unlining ikkinchi qismi ham toʻliq bitta zarb oladi. Yaponcha
  gapirayotgan odam <em>tekis</em> eshitiladi, aynan shu sababdan.</p>
</div>

<h3>4. Tez oʻqish — belgidan soʻzga</h3>

<p>Boshlovchi har bir belgini alohida tanib, keyin qoʻshadi: "ku... ru... ma...
kuruma". Bu normal, lekin bu yerda toʻxtab qolmaslik kerak. Maqsad —
<b>butun soʻzni bir qarashda koʻrish</b>. Buning yagona yoʻli: koʻp oʻqish.</p>

<div class="pe-call pe-tip">
  <p><b>Kichik ogohlantirish.</b> Quyidagi misollarda ikkita belgi hali
  oʻrganilmagan: <b>で</b> (です soʻzida) va <b>きょ</b>. Ikkalasi ham PJ-6 da
  keladi. Hozircha ularni shunchaki tanib turing — qolgan hamma belgi sizga
  tanish.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">わたしのなまえはゆきです</p>
  <p class="pe-ex__rom">watashi no namae wa yuki desu</p>
  <p class="pe-ex__uz">Mening ismim Yuki.</p>
  <p class="pe-ex__why">Yaponchada boʻshliq yoʻq, shuning uchun soʻz chegarasini oʻzingiz topasiz. Bu — kanjining nega kerakligini koʻrsatadigan eng yaxshi misol: kanji bilan yozilganda bu gap bir zumda boʻlaklarga ajraladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">きょうはあめです</p>
  <p class="pe-ex__rom">kyō wa ame desu</p>
  <p class="pe-ex__uz">Bugun yomgʻirli.</p>
  <p class="pe-ex__why">Birinchi soʻzdagi きょ — kichraytirilgan よ bilan yozilgan qoʻshma tovush. Uni PJ-6 da oʻrganamiz; hozircha shuni bilib qoʻying, bunday juftliklar bitta zarb sanaladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">やまとうみとそら</p>
  <p class="pe-ex__rom">yama to umi to sora</p>
  <p class="pe-ex__uz">Togʻ, dengiz va osmon.</p>
  <p class="pe-ex__why">Oʻrtadagi と — "va" degan qoʻshimcha. Yaponcha sanashda "va" har bir soʻzdan keyin takrorlanadi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Kuniga besh daqiqa ovoz chiqarib oʻqing.</b> Nimani oʻqish emas, qancha
  <em>tez-tez</em> oʻqish muhim. Ovoz chiqarib oʻqish koʻz va quloqni bir vaqtda
  oʻrgatadi, shuning uchun u jimgina oʻqishdan ikki barobar samarali.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ せんせい ni "sensei" deb, oxirini "se-i" qilib aytish</p>
  <p class="pe-fix__good">✓ <b>[sensē]</b>. えい — uzun <b>e</b>, ikkita alohida unli emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ゆうき ni ゆき kabi qisqa aytish</p>
  <p class="pe-fix__good">✓ Uzunlik maʼnoni oʻzgartiradi: <b>ゆき</b> — qor, <b>ゆうき</b> — jasorat. う ni toʻliq bir zarb ushlang.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ にほん ni ikki zarbda, urgʻu qoʻyib "niHON" deb aytish</p>
  <p class="pe-fix__good">✓ Uch zarb, hammasi teng: <b>に · ほ · ん</b>. Yapon ritmi tekis.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <b>おはよう</b> soʻzining oxiri qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>[ohayō]</b> — おう birikmasi uzun <b>o</b> beradi, "yo-u" emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <b>おかあさん</b> da nechta mora bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Beshta</b>: お · か · あ · さ · ん. Uzun unlining ikkinchi qismi ham, ん ham toʻliq bitta zarb sanaladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <b>ゆき</b> va <b>ゆうき</b> orasida qanday farq bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Faqat unli uzunligi — lekin maʼno butunlay boshqa: <b>ゆき</b> qor, <b>ゆうき</b> jasorat.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 五十音図 jadvalida <b>ustunlar</b> nimani bildiradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Unlilarni</b> — a, i, u, e, o. Chapdagi qatorlar esa undoshni bildiradi. Har bir katak ularning kesishmasi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Yapon tilida zarblar (mora) uzunligi qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Hammasi teng.</b> Oʻzbekchadan farqli oʻlaroq, birorta boʻgʻin urgʻu bilan choʻzilmaydi — soʻz sanagandek, tekis aytiladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>おかあさん</b> — ona</li>
  <li><b>おとうさん</b> — ota (murojaat qilganda)</li>
  <li><b>ゆうき</b> — jasorat</li>
  <li><b>くうき</b> — havo</li>
  <li><b>なまえ</b> — ism</li>
  <li><b>あめ</b> — yomgʻir</li>
  <li><b>ゆめ</b> — orzu, tush</li>
  <li><b>おはよう</b> — xayrli tong</li>
  <li><b>もり</b> — oʻrmon</li>
  <li><b>とおる</b> — oʻtib ketmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>五十音図 — undosh × unli jadvali. Yapon grammatikasining yarmi shu jadval boʻylab harakat qiladi.</li>
    <li>Uzun unli <b>maʼnoni oʻzgartiradi</b>: えい = uzun e, おう = uzun o.</li>
    <li>Har bir kana bitta <b>teng</b> zarb (mora). ん ham, uzun unlining ikkinchi qismi ham hisobga kiradi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-6: Dakuten が ざ だ ば, handakuten ぱ, yōon きゃ va sokuon っ",
        "category": "japanese",
        "order": 6,
        "summary": (
            "Hiragananing toʻrtta sozlagichi: ikki tirnoq jarangli tovush beradi, "
            "doiracha p beradi, kichik ゃゅょ qoʻshma tovush yasaydi, kichik っ esa undoshni "
            "ikkilantiradi."
        ),
        "content": """
<h2>PJ-6: Dakuten が ざ だ ば, handakuten ぱ, yōon きゃ va sokuon っ</h2>

<p>46 ta belgini bilasiz — lekin yaponcha matnni ochsangiz, hali ham notanish
narsalar koʻrasiz: baʼzi belgilarning yonida ikkita tirnoq, baʼzilarida kichkina
doiracha, baʼzi joyda esa <em>kichraytirilgan</em> belgi turadi. Bular yangi harf
emas. Bular — <b>sozlagichlar</b>: siz bilgan belgini olib, uning tovushini
oʻzgartiradi. Toʻrttasi bor, va bugun toʻrttasini ham hal qilamiz. Shundan keyin
hiragana toʻliq tugaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Dakuten (゛) va handakuten (゜) belgilarini oʻqiysiz: か → が → (は →) ぱ</li>
    <li>じ/ぢ va ず/づ juftligini — "toʻrtta kana muammosi"ni — hal qilasiz</li>
    <li>Kichik ゃ ゅ ょ bilan yasalgan qoʻshma tovushlarni oʻqiysiz</li>
    <li>Kichik っ ni tanib olasiz va nega u <b>jimlik</b> ekanini tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrtta sozlagich</span>
  <span class="pe-chip pe-chip--s">゛ jarangli</span>
  <span class="pe-chip pe-chip--v">゜ p</span>
  <span class="pe-chip pe-chip--o">ゃゅょ qoʻshma</span>
  <span class="pe-chip pe-chip--neg">っ jimlik</span>
</div>

<h3>1. Dakuten (濁点) — ikkita tirnoq</h3>

<p>Belgining oʻng yuqori burchagiga ikkita kichik tirnoq qoʻyilsa, uning undoshi
<b>jaranglashadi</b>. Bu — oʻzbek tilida ham bor juftliklar: <em>k → g</em>,
<em>s → z</em>, <em>t → d</em>, <em>h → b</em>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qator</th><th>a</th><th>i</th><th>u</th><th>e</th><th>o</th></tr>
  <tr><td class="pj-stem">k → g</td><td>が</td><td>ぎ</td><td>ぐ</td><td>げ</td><td>ご</td></tr>
  <tr><td class="pj-stem">s → z</td><td>ざ</td><td class="pj-end">じ</td><td>ず</td><td>ぜ</td><td>ぞ</td></tr>
  <tr><td class="pj-stem">t → d</td><td>だ</td><td class="pj-end">ぢ</td><td class="pj-end">づ</td><td>で</td><td>ど</td></tr>
  <tr><td class="pj-stem">h → b</td><td>ば</td><td>び</td><td>ぶ</td><td>べ</td><td>ぼ</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu mantiq oʻzbekchada ham bor.</b> Oʻzbek tilida ham jarangsiz va jarangli
  juftliklar mavjud: <em>k–g</em>, <em>t–d</em>, <em>s–z</em>, <em>p–b</em>. Farqi
  shundaki, oʻzbekchada ular butunlay boshqa harflar bilan yoziladi; yaponchada esa
  bitta belgi olinib, ustiga ikkita tirnoq qoʻyiladi. Yaponcha usul kamroq
  yodlashni talab qiladi — siz allaqachon が ni bilasiz, chunki か ni bilasiz.</p>
</div>

<p>Yashil rangdagi uchtasi — istisnolar: <b>じ</b> "ji", <b>ぢ</b> ham "ji",
<b>づ</b> esa "zu". Bu oʻsha し = shi va ち = chi qoidasining davomi.</p>

<h3>2. Toʻrtta kana muammosi: じ/ぢ va ず/づ</h3>

<p>Ikkita tovush, toʻrtta belgi. <b>じ</b> va <b>ぢ</b> ikkalasi ham [ji],
<b>ず</b> va <b>づ</b> ikkalasi ham [zu] deb oʻqiladi. Unda qaysi birini
yozish kerak?</p>

<div class="pj-yomi">
  <div class="pj-yomi__side">
    <p class="pj-yomi__h">じ va ず — deyarli doim</p>
    <p class="pj-yomi__ex">じかん · みず</p>
    <p>Shubhalansangiz, じ yoki ず yozing. Yaponcha soʻzlarning 99 foizi shulardan foydalanadi.</p>
  </div>
  <div class="pj-yomi__side pj-yomi__side--kun">
    <p class="pj-yomi__h">ぢ va づ — kamdan-kam</p>
    <p class="pj-yomi__ex">はなぢ · つづく</p>
    <p>Faqat ikki holatda: ち yoki つ dan yasalgan soʻz qoʻshilganda, yoki ち/つ takrorlanganda.</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Yodlab oʻtirmang.</b> ぢ va づ shunchalik kam uchraydiki, ularni
  <em>tanish</em> yetarli — <em>yozish</em>ni bilish shart emas. Yozganda doim
  じ va ず ni tanlang, va deyarli har doim toʻgʻri boʻlasiz.</p>
</div>

<h3>3. Handakuten (半濁点) — kichkina doiracha</h3>

<p>Faqat <b>は-qatori</b> uchun ishlaydi va <b>p</b> tovushini beradi. Yaʼni は
qatori uch xil boʻlishi mumkin: sof (は = ha), tirnoqli (ば = ba), doirali
(ぱ = pa).</p>

<div class="pj-kana pj-kana--free">
  <div class="pj-kana__c"><span class="pj-kana__ch">は</span>
    <span class="pj-kana__rom">ha</span><span class="pj-kana__uz">sof</span></div>
  <div class="pj-kana__c pj-kana__c--new"><span class="pj-kana__ch">ば</span>
    <span class="pj-kana__rom">ba</span><span class="pj-kana__uz">dakuten ゛</span></div>
  <div class="pj-kana__c pj-kana__c--new"><span class="pj-kana__ch">ぱ</span>
    <span class="pj-kana__rom">pa</span><span class="pj-kana__uz">handakuten ゜</span></div>
  <div class="pj-kana__c pj-kana__c--new"><span class="pj-kana__ch">ぴ</span>
    <span class="pj-kana__rom">pi</span><span class="pj-kana__uz">ひ + ゜</span></div>
  <div class="pj-kana__c pj-kana__c--new"><span class="pj-kana__ch">ぷ</span>
    <span class="pj-kana__rom">pu</span><span class="pj-kana__uz">ふ + ゜</span></div>
  <div class="pj-kana__c pj-kana__c--new"><span class="pj-kana__ch">ぺ</span>
    <span class="pj-kana__rom">pe</span><span class="pj-kana__uz">へ + ゜</span></div>
  <div class="pj-kana__c pj-kana__c--new"><span class="pj-kana__ch">ぽ</span>
    <span class="pj-kana__rom">po</span><span class="pj-kana__uz">ほ + ゜</span></div>
</div>

<p>Endi PJ-4 da vaʼda qilingan qoidani ham yopamiz: <b>ん</b> tovushi keyingi
harfga moslashadi. <b>b</b>, <b>p</b> yoki <b>m</b> dan oldin u <b>[m]</b> boʻlib
chiqadi — chunki ogʻiz allaqachon shu tovushga tayyorlanadi.</p>

<div class="pj-say">
  <span class="pj-say__from">しんぶん</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[shimbun]</span>
  <span class="pj-say__why">ん + b → [m]; atayin qilmaysiz, ogʻiz oʻzi shunday qiladi</span>
</div>

<h3>4. Yōon (拗音) — kichraytirilgan ゃ ゅ ょ</h3>

<p>i-ustunidagi belgiga <b>kichik</b> ゃ, ゅ yoki ょ yopishtirilsa, ikkalasi
birga <b>bitta</b> tovush hosil qiladi. Kattaligiga qarang: katta よ — alohida
belgi, kichik ょ — oldingisining bir qismi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Asos</th><th>+ ゃ</th><th>+ ゅ</th><th>+ ょ</th></tr>
  <tr><td class="pj-stem">き</td><td class="pj-res">きゃ kya</td><td class="pj-res">きゅ kyu</td><td class="pj-res">きょ kyo</td></tr>
  <tr><td class="pj-stem">し</td><td class="pj-res">しゃ sha</td><td class="pj-res">しゅ shu</td><td class="pj-res">しょ sho</td></tr>
  <tr><td class="pj-stem">ち</td><td class="pj-res">ちゃ cha</td><td class="pj-res">ちゅ chu</td><td class="pj-res">ちょ cho</td></tr>
  <tr><td class="pj-stem">に</td><td class="pj-res">にゃ nya</td><td class="pj-res">にゅ nyu</td><td class="pj-res">にょ nyo</td></tr>
  <tr><td class="pj-stem">ひ</td><td class="pj-res">ひゃ hya</td><td class="pj-res">ひゅ hyu</td><td class="pj-res">ひょ hyo</td></tr>
  <tr><td class="pj-stem">じ</td><td class="pj-res">じゃ ja</td><td class="pj-res">じゅ ju</td><td class="pj-res">じょ jo</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Qoʻshma tovush bitta zarb (mora) sanaladi.</b> Bu juda muhim:
  <b>きょう</b> ("bugun") — uch belgi, lekin <b>ikki</b> zarb: kyo + o. Agar uni
  "ki-yo-u" deb uch zarbda aytsangiz, yaponcha eshitilmaydi. Kichik belgi
  <em>hech qachon</em> oʻz zarbini olmaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">きょうはでんしゃでとうきょうへいきます</p>
  <p class="pe-ex__rom">kyō wa densha de tōkyō e ikimasu</p>
  <p class="pe-ex__uz">Bugun poyezdda Tokioga boraman.</p>
  <p class="pe-ex__why">Uchta qoʻshma tovush: きょ, しゃ, きょ. Sanang — bu gapda oʻn ikki zarb bor, oʻn beshta belgi emas.</p>
</div>

<h3>5. Sokuon (促音) — kichik っ, tovushi yoʻq belgi</h3>

<p>Kichik <b>っ</b> — hiragananing eng gʻalati belgisi, chunki uning
<em>oʻz tovushi yoʻq</em>. U keyingi undoshni <b>ikkilantiradi</b>, va aslida
uning oʻzi bir zarblik <b>jimlik</b>dir: ogʻiz keyingi tovushga tayyorlanib
toʻxtab turadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">っ YOʻQ</p>
    <p class="pj-big">きて</p>
    <p><b>[kite]</b> — "kel". Ikki zarb, tekis.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">っ BOR</p>
    <p class="pj-big">きって</p>
    <p><b>[kitte]</b> — "marka". Uch zarb: ki · (jimlik) · te.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu tovush oʻzbek tilida ham bor.</b> "yotti" yoki "kitob<em>b</em>op" degan
  soʻzlarda undosh ikkilanadi va oʻrtada qisqa toʻxtash seziladi. Yapon tilida
  aynan shu — faqat u yozuvda alohida belgi bilan koʻrsatiladi va <b>toʻliq bir
  zarb</b> sanaladi. Toʻxtashni qisqartirsangiz, boshqa soʻz chiqadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">がっこうにいきます</p>
  <p class="pe-ex__rom">gakkō ni ikimasu</p>
  <p class="pe-ex__uz">Maktabga boraman.</p>
  <p class="pe-ex__why">がっこう — が · っ · こ · う, toʻrt zarb. っ ning oʻzi jimlik, lekin u ham sanaladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">ざっしをよみます</p>
  <p class="pe-ex__rom">zasshi o yomimasu</p>
  <p class="pe-ex__uz">Jurnal oʻqiyman.</p>
  <p class="pe-ex__why">っ dan keyin し kelsa, lotin yozuvida <b>ssh</b> boʻlib chiqadi. Bu — ikkilangan [sh] tovushi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Kattalikni ajratish.</b> Ekranda kichik っ ゃ ゅ ょ katta つ や ゆ よ dan
  taxminan yarim barobar kichik va katakning pastki chetiga tushib turadi.
  Qoʻlda yozganda ham xuddi shunday qiling — aks holda <em>きって</em> (marka)
  <em>きつて</em> ga aylanadi va soʻz maʼnosini yoʻqotadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ きょう ni "ki-yo-u" deb uch zarbda aytish</p>
  <p class="pe-fix__good">✓ <b>[kyō]</b> — ikki zarb. Kichik ょ oʻz zarbini olmaydi, u き ga qoʻshilib bitta tovush yasaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ きって ni きて kabi, toʻxtashsiz aytish</p>
  <p class="pe-fix__good">✓ <b>[kitte]</b> — oʻrtada bir zarblik jimlik bor. <b>きて</b> "kel", <b>きって</b> "marka" — butunlay boshqa soʻzlar.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Kichik ゃ ni katta や kabi yozish</p>
  <p class="pe-fix__good">✓ Kattaligi maʼno beradi: <b>きゃ</b> = "kya" (bitta zarb), <b>きや</b> = "ki-ya" (ikki zarb).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <b>か</b> ga dakuten (゛) qoʻyilsa nima boʻladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>が</b> [ga]. Dakuten jarangsiz undoshni jaranglashtiradi: k → g.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <b>きょう</b> da nechta zarb (mora) bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Ikkita</b>: kyo + o. Kichik ょ き ga qoʻshilib bitta tovush yasaydi va oʻz zarbini olmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <b>きて</b> va <b>きって</b> orasidagi farq nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>きて</b> [kite] — "kel", ikki zarb. <b>きって</b> [kitte] — "marka", uch zarb: oʻrtada bir zarblik jimlik bor.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Handakuten (゜) qaysi qatorga qoʻyiladi va nima beradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Faqat <b>は-qatoriga</b>, va <b>p</b> tovushini beradi: は → ぱ, ひ → ぴ, ふ → ぷ.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Yozayotganda [ji] tovushi uchun じ yoki ぢ — qaysi birini tanlaysiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Deyarli doim <b>じ</b>. ぢ juda kam uchraydi — faqat ち dan yasalgan soʻz qoʻshilganda. Shubhalansangiz じ yozing.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>がっこう</b> — maktab</li>
  <li><b>じかん</b> — vaqt, soat</li>
  <li><b>みず</b> — suv</li>
  <li><b>でんしゃ</b> — poyezd</li>
  <li><b>きょう</b> — bugun</li>
  <li><b>きって</b> — pochta markasi</li>
  <li><b>ざっし</b> — jurnal</li>
  <li><b>しんぶん</b> — gazeta</li>
  <li><b>べんきょう</b> — oʻqish, mashgʻulot</li>
  <li><b>とうきょう</b> — Tokio</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Toʻrtta sozlagich: <b>゛</b> jaranglashtiradi, <b>゜</b> p beradi, kichik <b>ゃゅょ</b> qoʻshma tovush yasaydi, kichik <b>っ</b> undoshni ikkilantiradi.</li>
    <li>Qoʻshma tovush <b>bitta</b> zarb; kichik っ esa <b>toʻliq bitta</b> zarb — garchi u jimlik boʻlsa ham.</li>
    <li>Hiragana tugadi. PJ-7 dan katakana boshlanadi va u ancha oson kechadi.</li>
  </ul>
</div>
""",
    },
]
