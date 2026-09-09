# -*- coding: utf-8 -*-
"""Prime Japanese — Block A, darslar 10–12 (kanji va sonlar).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_JAPANESE.md
Lesson list: tutorial/management/commands/toc_prime_japanese.txt

Block A ning oxirgi uch darsi. Grammatika yoʻq, oʻqish matni ham yoʻq.
Har bir darsning ikkinchi boʻlagi — 12 savollik mashq:
practice/management/commands/_practice_pj_10_12.py

BU YERDAN BOSHLAB HAR BIR KANJI FURIGANA BILAN YOZILADI (<ruby>).

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_10_12.py --author=prime
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
        "title": "PJ-10: Kanji nima — 漢字 qayerdan kelgan va nega qoʻrqmaslik kerak",
        "category": "japanese",
        "order": 10,
        "summary": (
            "Kanjining kelib chiqishi, toʻrt turi va radikallar tizimi. Nega 2000 ta "
            "belgi koʻringanidan ancha kam mehnat talab qilishini koʻrasiz."
        ),
        "content": """
<h2>PJ-10: Kanji nima — <ruby>漢字<rt>かんじ</rt></ruby> qayerdan kelgan va nega qoʻrqmaslik kerak</h2>

<p>Mana shu yerda koʻpchilik yapon tilini tashlab ketadi. "Ikki mingta belgi?
Har birining bir nechta oʻqilishi bormi? Yoʻq, rahmat." Agar sizda ham shunday
his boʻlsa — bu tabiiy, lekin bu <b>notoʻgʻri hisob-kitobga</b> asoslangan.</p>

<p>Haqiqat shuki, kanji <em>tasodifiy chizmalar toʻplami emas</em>. U tizim:
ikki mingta belgi taxminan <b>ikki yuzta qismdan</b> yigʻilgan, va bu qismlarning
koʻpi maʼno beradi. Bugun shu tizimni koʻrasiz — shundan keyin kanji qoʻrqinchli
emas, <em>qiziq</em> boʻlib qoladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Kanji qayerdan kelganini va nega yapon tilida qolganini bilasiz</li>
    <li>Kanjining toʻrt turini ajratasiz — va nega bu yodlashni yengillashtirishini koʻrasiz</li>
    <li>Radikal (<ruby>部首<rt>ぶしゅ</rt></ruby>) nima ekanini va u qanday yordam berishini tushunasiz</li>
    <li>Birinchi 20 ta belgini oʻqiysiz va chiziq tartibi qoidasini oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kanjining haqiqiy hisobi</span>
  <span class="pe-chip pe-chip--s">~2000 belgi</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">~200 qism</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">tizim</span>
</div>

<h3>1. Qayerdan kelgan</h3>

<p>Yapon tilida dastlab <b>yozuv umuman boʻlmagan</b>. Taxminan 1500 yil oldin
Xitoy yozuvi Koreya orqali Yaponiyaga kirib keldi, va yaponlar oʻz tillarini
xitoy belgilari bilan yozishga urindi. <b><ruby>漢字<rt>かんじ</rt></ruby></b>
degan soʻzning oʻzi ham shuni aytadi: <em>kan</em> (<ruby>漢<rt>かん</rt></ruby>) — Xitoydagi Han sulolasi,
<em>ji</em> (<ruby>字<rt>じ</rt></ruby>) — belgi. Yaʼni "Han belgilari".</p>

<p>Muammo shundaki, yapon tili xitoy tiliga <b>umuman oʻxshamaydi</b>. Xitoy
tilida soʻzlar tuslanmaydi, yapon tilida esa feʼl va sifat doim tuslanadi.
Shuning uchun yaponlar keyinroq kanjidan hiragana va katakanani yasadi —
grammatikani yozish uchun. Bugungi tizim shu ikki qatlamning qoʻshilishi:
<b>maʼno kanjida, grammatika kanada</b>.</p>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham shunga oʻxshash voqea boʻlgan.</b> Bizda ham yozuv
  chetdan kelgan — avval arab, keyin lotin, keyin kirill. Har safar til
  oʻzgarmadi, faqat kiyimi almashdi. Farqi shuki, yaponlar eski kiyimni
  tashlamadi: ular kanjini saqlab, uning ustiga oʻz yozuvlarini qoʻshdi.</p>
</div>

<h3>2. Toʻrt turi — va nega bu muhim</h3>

<p>Har bir kanji tasodifiy chizilmagan. Ular toʻrt usulda yasalgan, va usulni
bilsangiz, belgi <em>maʼnoli</em> koʻrina boshlaydi.</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Rasm (<ruby>象形<rt>しょうけい</rt></ruby>)</p>
    <p>Narsaning oddiylashtirilgan surati.<br>
    <ruby>山<rt>やま</rt></ruby> togʻ · <ruby>川<rt>かわ</rt></ruby> daryo ·
    <ruby>木<rt>き</rt></ruby> daraxt · <ruby>日<rt>ひ</rt></ruby> quyosh</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Belgi (<ruby>指事<rt>しじ</rt></ruby>)</p>
    <p>Mavhum tushuncha uchun oddiy shartli belgi.<br>
    <ruby>一<rt>いち</rt></ruby> bir · <ruby>二<rt>に</rt></ruby> ikki ·
    <ruby>上<rt>うえ</rt></ruby> ust · <ruby>下<rt>した</rt></ruby> ost</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Qoʻshilma (<ruby>会意<rt>かいい</rt></ruby>)</p>
    <p>Ikki maʼno qoʻshilib uchinchisini beradi.<br>
    <ruby>木<rt>き</rt></ruby> + <ruby>木<rt>き</rt></ruby> = <ruby>林<rt>はやし</rt></ruby> oʻrmoncha</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">4</span>Maʼno + tovush (<ruby>形声<rt>けいせい</rt></ruby>)</p>
    <p>Bir qism maʼnoni, ikkinchisi <b>oʻqilishni</b> beradi. Kanjilarning
    <b>80 foizdan koʻpi</b> shunday.</p></div>
</div>

<p>Uchinchi turni oʻz koʻzingiz bilan koʻring — bu kanjidagi eng chiroyli
mantiq:</p>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">木</span>
    <span class="pj-kanji__uz">daraxt</span>
    <span class="pj-kanji__on">bitta daraxt</span>
    <span class="pj-kanji__kun">KUN: き</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">林</span>
    <span class="pj-kanji__uz">oʻrmoncha</span>
    <span class="pj-kanji__on">ikkita daraxt</span>
    <span class="pj-kanji__kun">KUN: はやし</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">森</span>
    <span class="pj-kanji__uz">qalin oʻrmon</span>
    <span class="pj-kanji__on">uchta daraxt</span>
    <span class="pj-kanji__kun">KUN: もり</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>Toʻrtinchi tur eng muhimi.</b> Kanjilarning katta qismida bir qism
  <em>nima haqida</em> ekanini, boshqasi esa <em>qanday oʻqilishini</em>
  aytadi. Demak notanish belgini koʻrganingizda ham taxmin qila olasiz:
  chap tomonida <ruby>水<rt>みず</rt></ruby> (suv) belgisining qisqargan
  shakli boʻlsa, soʻz suyuqlikka aloqador.</p>
</div>

<h3>3. Radikallar — 200 ta gʻisht, 2000 ta bino</h3>

<p><b>Radikal</b> (<ruby>部首<rt>ぶしゅ</rt></ruby>) — kanjining takrorlanadigan
qismi. Lugʻatlar kanjini shu qism boʻyicha tartiblaydi, va aynan shu narsa
yodlashni bir necha barobar yengillashtiradi: siz 2000 ta rasmni emas, 200 ta
gʻishtni va ularning birikmalarini oʻrganasiz.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Radikal</th><th>Maʼnosi</th><th>Undan yasalgan kanjilar</th></tr>
  <tr><td class="pj-stem">木</td><td class="pj-uz">daraxt</td>
      <td><ruby>林<rt>はやし</rt></ruby> · <ruby>森<rt>もり</rt></ruby> · <ruby>村<rt>むら</rt></ruby> qishloq · <ruby>校<rt>こう</rt></ruby> maktab</td></tr>
  <tr><td class="pj-stem">水 / 氵</td><td class="pj-uz">suv</td>
      <td><ruby>海<rt>うみ</rt></ruby> dengiz · <ruby>池<rt>いけ</rt></ruby> hovuz · <ruby>酒<rt>さけ</rt></ruby> ichimlik</td></tr>
  <tr><td class="pj-stem">人 / 亻</td><td class="pj-uz">odam</td>
      <td><ruby>休<rt>やす</rt></ruby>む dam olmoq · <ruby>体<rt>からだ</rt></ruby> tana</td></tr>
  <tr><td class="pj-stem">口</td><td class="pj-uz">ogʻiz</td>
      <td><ruby>話<rt>はな</rt></ruby>す gapirmoq · <ruby>味<rt>あじ</rt></ruby> taʼm</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b><ruby>休<rt>やす</rt></ruby>む — eng chiroyli misol.</b> Chap tomonida <b>亻</b> (odam), oʻng
  tomonida <b><ruby>木<rt>き</rt></ruby></b> (daraxt). Odam daraxtga suyanib turibdi — maʼnosi
  <em>dam olmoq</em>. Bir marta koʻrgan odam buni umr boʻyi unutmaydi.</p>
</div>

<h3>4. Nechta kerak, va nega bu qoʻrqinchli emas</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Daraja</th><th>Kanji soni</th><th>Nimaga yetadi</th></tr>
  <tr><td class="pj-stem">N5</td><td class="pj-res">~100</td><td class="pj-uz">oddiy belgilar, sonlar, kundalik soʻzlar</td></tr>
  <tr><td class="pj-stem">N4</td><td class="pj-res">~300</td><td class="pj-uz">oddiy matn, menyu, eʼlon</td></tr>
  <tr><td class="pj-stem">N3</td><td class="pj-res">~650</td><td class="pj-uz">gazeta sarlavhalari, oddiy maqola</td></tr>
  <tr><td class="pj-stem">Maktab</td><td class="pj-res">2136</td><td class="pj-uz"><ruby>常用漢字<rt>じょうようかんじ</rt></ruby> — rasmiy roʻyxat, butun gazeta</td></tr>
</table></div>

<p>Yapon bolasi bu 2136 belgini <b>toʻqqiz yilda</b> oʻrganadi — yiliga
taxminan 240 ta. Siz esa <b>Prime Japanese</b> davomida taxminan 600 tasini
koʻrasiz, ya'ni N3 darajasiga yaqin. Va eng muhimi:</p>

<div class="pe-call pe-warn">
  <p><b>Bu kursda har bir kanji furigana bilan yoziladi</b> — yuzinchi darsda
  ham. Demak siz hech qachon "bu belgini bilmayman" deb toʻxtab qolmaysiz.
  Kanjini <em>tanish</em> asta-sekin oʻz-oʻzidan keladi, chunki siz uni
  oʻqilishi bilan birga, minglab marta koʻrasiz.</p>
</div>

<h3>5. Chiziq tartibi — uchta qoida yetadi</h3>

<ol class="pe-steps">
  <li><b>Yuqoridan pastga.</b> <ruby>三<rt>さん</rt></ruby> — tepadagi chiziq birinchi.</li>
  <li><b>Chapdan oʻngga.</b> <ruby>川<rt>かわ</rt></ruby> — chapdagi chiziq birinchi.</li>
  <li><b>Gorizontal chiziq vertikaldan oldin.</b> <ruby>十<rt>じゅう</rt></ruby> — avval yotiq, keyin tik.</li>
</ol>

<div class="pj-stroke">
  <span class="pj-stroke__s" data-n="1">一</span>
  <span class="pj-stroke__s" data-n="2">十</span>
  <span class="pj-stroke__s" data-n="3">土</span>
</div>

<p>Nega bu muhim? Chunki toʻgʻri tartibda yozilgan belgi <b>toʻgʻri
koʻrinadi</b> — chiziqlarning uzunligi va burchagi oʻz-oʻzidan joyiga tushadi.
Bundan tashqari, telefon va kompyuterdagi qoʻlyozma kiritish shu tartibga
qarab ishlaydi.</p>

<h3>6. Birinchi belgilaringiz</h3>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">山</span><span class="pj-kanji__uz">togʻ</span>
    <span class="pj-kanji__on">Uchta choʻqqi</span>
    <span class="pj-kanji__kun">KUN: やま</span></div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">川</span><span class="pj-kanji__uz">daryo</span>
    <span class="pj-kanji__on">Oqayotgan suv chiziqlari</span>
    <span class="pj-kanji__kun">KUN: かわ</span></div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">日</span><span class="pj-kanji__uz">quyosh, kun</span>
    <span class="pj-kanji__on">Oʻrtasida nuqtasi bor doira</span>
    <span class="pj-kanji__kun">KUN: ひ</span></div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">月</span><span class="pj-kanji__uz">oy</span>
    <span class="pj-kanji__on">Yarim oy shakli</span>
    <span class="pj-kanji__kun">KUN: つき</span></div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">人</span><span class="pj-kanji__uz">odam</span>
    <span class="pj-kanji__on">Yurayotgan odamning ikki oyogʻi</span>
    <span class="pj-kanji__kun">KUN: ひと</span></div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">田</span><span class="pj-kanji__uz">dala</span>
    <span class="pj-kanji__on">Toʻrtga boʻlingan yer</span>
    <span class="pj-kanji__kun">KUN: た</span></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>山<rt>やま</rt></ruby>と<ruby>川<rt>かわ</rt></ruby></p>
  <p class="pe-ex__rom">yama to kawa</p>
  <p class="pe-ex__uz">togʻ va daryo</p>
  <p class="pe-ex__why">Kanji maʼnoni, hiragana と esa grammatikani tashiydi. Bu — butun yapon yozuvining ish taqsimoti, bitta qisqa iborada.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>日本人<rt>にほんじん</rt></ruby></p>
  <p class="pe-ex__rom">nihonjin</p>
  <p class="pe-ex__uz">yapon (millat)</p>
  <p class="pe-ex__why">Uchta kanji: <ruby>日<rt>にち</rt></ruby> (quyosh) + <ruby>本<rt>ほん</rt></ruby> (asos) + <ruby>人<rt>じん</rt></ruby> (odam) = "quyosh chiqadigan yerning odami". Diqqat: bu yerda <ruby>日<rt>ひ</rt></ruby> «ひ» emas, «に» deb oʻqildi — nega, buni PJ-11 da koʻramiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ "Kanjini rasm sifatida yodlash kerak"</p>
  <p class="pe-fix__good">✓ Kanji <b>qismlardan</b> yigʻiladi. <ruby>休<rt>やす</rt></ruby>む ni yodlamang — 亻 (odam) va <ruby>木<rt>き</rt></ruby> (daraxt) ni koʻring. Qismlarni bilsangiz, yangi belgi ham tanish tuyuladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Chiziq tartibini eʼtiborsiz qoldirish</p>
  <p class="pe-fix__good">✓ Uchta qoida: yuqoridan pastga, chapdan oʻngga, gorizontal vertikaldan oldin. Toʻgʻri tartibda yozilgan belgi toʻgʻri koʻrinadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ "2000 ta belgini yodlamagunimcha oʻqiy olmayman"</p>
  <p class="pe-fix__good">✓ N5 uchun ~100 ta yetadi, va bu kursda har bir kanji <b>furigana</b> bilan yoziladi. Siz birinchi kundan oʻqiysiz.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>漢字<rt>かんじ</rt></ruby> soʻzi nimani anglatadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>"Han belgilari" — <em>kan</em> (<ruby>漢<rt>かん</rt></ruby>) Xitoydagi Han sulolasi, <em>ji</em> (<ruby>字<rt>じ</rt></ruby>) belgi. Kanji taxminan 1500 yil oldin Xitoydan Koreya orqali kirib kelgan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>森<rt>もり</rt></ruby> belgisi qanday yasalgan?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Uchta <ruby>木<rt>き</rt></ruby> (daraxt) dan — qalin oʻrmon. Bu <b>qoʻshilma</b> (<ruby>会意<rt>かいい</rt></ruby>) turiga misol: maʼnolar qoʻshilib yangi maʼno beradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Radikal (<ruby>部首<rt>ぶしゅ</rt></ruby>) nima va nega u foydali?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Kanjining takrorlanadigan qismi. ~2000 belgi ~200 ta radikaldan yigʻilgan, shuning uchun siz rasmlarni emas, <b>gʻishtlarni</b> oʻrganasiz. Radikal koʻpincha maʼnoga ishora ham beradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>休<rt>やす</rt></ruby>む belgisining mantigʻi nimada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>亻 (odam) + <ruby>木<rt>き</rt></ruby> (daraxt) = odam daraxtga suyanib turibdi → <b>dam olmoq</b> (<ruby>休<rt>やす</rt></ruby>む).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Chiziq tartibining uchta asosiy qoidasi qaysi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yuqoridan pastga, chapdan oʻngga, va gorizontal chiziq vertikaldan oldin.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>漢字<rt>かんじ</rt></ruby></b> — kanji</li>
  <li><b><ruby>部首<rt>ぶしゅ</rt></ruby></b> — radikal</li>
  <li><b><ruby>山<rt>やま</rt></ruby></b> — togʻ</li>
  <li><b><ruby>川<rt>かわ</rt></ruby></b> — daryo</li>
  <li><b><ruby>木<rt>き</rt></ruby></b> — daraxt</li>
  <li><b><ruby>森<rt>もり</rt></ruby></b> — oʻrmon</li>
  <li><b><ruby>日<rt>ひ</rt></ruby></b> — quyosh, kun</li>
  <li><b><ruby>月<rt>つき</rt></ruby></b> — oy</li>
  <li><b><ruby>人<rt>ひと</rt></ruby></b> — odam</li>
  <li><b><ruby>田<rt>た</rt></ruby></b> — dala</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Kanji rasm toʻplami emas — <b>~2000 belgi ~200 ta qismdan</b> yigʻilgan.</li>
    <li>Kanjilarning 80 foizdan koʻpida bir qism maʼnoni, boshqasi <b>oʻqilishni</b> beradi.</li>
    <li>Bu kursda har bir kanji <b>furigana</b> bilan yoziladi — siz hech qachon toʻxtab qolmaysiz.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-11: On'yomi va kun'yomi — bitta belgi, ikkita oʻqilish",
        "category": "japanese",
        "order": 11,
        "summary": (
            "Nega bitta kanji bir necha xil oʻqiladi va qaysi oʻqilish qachon ishlaydi. "
            "Okurigana — hiragana dumi qanday qilib oʻqilishni koʻrsatadi."
        ),
        "content": """
<h2>PJ-11: On'yomi va kun'yomi — bitta belgi, ikkita oʻqilish</h2>

<p>Oʻtgan darsda <ruby>日<rt>ひ</rt></ruby> belgisini "quyosh, kun" deb
oʻrgandingiz va uni <b>ひ</b> deb oʻqidingiz. Keyin <ruby>日本人<rt>にほんじん</rt></ruby>
soʻzida oʻsha belgi birdan <b>に</b> boʻlib chiqdi. Xato emas — <em>qoida</em>.</p>

<p>Bu yapon tilidagi eng koʻp savol tugʻdiradigan narsa, lekin uning sababi juda
sodda va mantiqiy. Bugun shuni tushunasiz, va shundan keyin kanji oʻqilishi
tasodifiy tuyulmay qoladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Nega bitta kanji ikki xil oʻqilishini bilasiz</li>
    <li>Qaysi oʻqilish qachon ishlashini <b>taxmin qila olasiz</b></li>
    <li>Okurigana (<ruby>送<rt>おく</rt></ruby>り<ruby>仮名<rt>がな</rt></ruby>) nima ekanini va u nima uchun kerakligini tushunasiz</li>
    <li>Lugʻatda oʻqilishlar nega katakana va hiraganada berilishini bilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Asosiy qoida</span>
  <span class="pe-chip pe-chip--s">kanji + kanji</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">ON</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">yolgʻiz yoki + kana</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">KUN</span>
</div>

<h3>1. Nega ikkita oʻqilish bor</h3>

<p>Sabab tarixda. Kanji Yaponiyaga kelganda, yaponlar allaqachon <b>oʻz tillarida
gapirar edi</b>. Ularda "togʻ" degan soʻz bor edi — <b>やま</b>. Xitoydan esa
shu maʼnodagi belgi <b><ruby>山<rt>やま</rt></ruby></b> keldi, va u bilan birga uning xitoycha talaffuzi —
<b>サン</b> ga oʻxshash tovush.</p>

<p>Yaponlar ikkalasini ham saqlab qoldi:</p>

<div class="pj-yomi">
  <div class="pj-yomi__side">
    <p class="pj-yomi__h">ON'YOMI (<ruby>音読<rt>おんよ</rt></ruby>み) — xitoycha</p>
    <p class="pj-yomi__ex">サン</p>
    <p>Belgi bilan birga kelgan talaffuz. Lugʻatlarda odatda <b>katakana</b> bilan
    yoziladi.</p>
  </div>
  <div class="pj-yomi__side pj-yomi__side--kun">
    <p class="pj-yomi__h">KUN'YOMI (<ruby>訓読<rt>くんよ</rt></ruby>み) — yaponcha</p>
    <p class="pj-yomi__ex">やま</p>
    <p>Yaponlarning oʻz soʻzi, belgiga keyin biriktirilgan. Lugʻatlarda
    <b>hiragana</b> bilan yoziladi.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham shunga oʻxshash qatlam bor.</b> Biz "suv" deymiz — oʻz
  soʻzimiz. Lekin ilmiy soʻzlarda arabcha-forscha oʻzak chiqadi: "obihayot",
  "obod". Bitta tushuncha, ikki xil kelib chiqish, ikki xil uslub. Yapon tilida
  bu farq <em>yozuvda ham</em> koʻrinadi va ancha tizimliroq ishlaydi.</p>
</div>

<h3>2. Qaysi biri qachon? — bitta ishonchli qoida</h3>

<div class="pe-call pe-rule">
  <p><b>Qoida:</b> kanji <em>boshqa kanji bilan yopishgan</em> boʻlsa —
  <b>on'yomi</b>. Kanji <em>yolgʻiz</em> tursa yoki <em>hiragana dumi</em>
  bilan kelsa — <b>kun'yomi</b>.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Oʻqilishi</th><th>Qaysi</th><th>Nega</th></tr>
  <tr><td><ruby>山<rt>やま</rt></ruby></td><td class="pj-res">yama</td>
      <td class="pj-end">KUN</td><td class="pj-uz">yolgʻiz turibdi</td></tr>
  <tr><td><ruby>火山<rt>かざん</rt></ruby></td><td class="pj-res">kazan</td>
      <td class="pj-stem">ON</td><td class="pj-uz">ikki kanji yopishgan — vulqon</td></tr>
  <tr><td><ruby>人<rt>ひと</rt></ruby></td><td class="pj-res">hito</td>
      <td class="pj-end">KUN</td><td class="pj-uz">yolgʻiz — odam</td></tr>
  <tr><td><ruby>日本人<rt>にほんじん</rt></ruby></td><td class="pj-res">nihonjin</td>
      <td class="pj-stem">ON</td><td class="pj-uz">uch kanji yopishgan</td></tr>
  <tr><td><ruby>水<rt>みず</rt></ruby></td><td class="pj-res">mizu</td>
      <td class="pj-end">KUN</td><td class="pj-uz">yolgʻiz — suv</td></tr>
  <tr><td><ruby>水曜日<rt>すいようび</rt></ruby></td><td class="pj-res">suiyōbi</td>
      <td class="pj-stem">ON</td><td class="pj-uz">yopishgan — chorshanba</td></tr>
  <tr><td><ruby>見<rt>み</rt></ruby>る</td><td class="pj-res">miru</td>
      <td class="pj-end">KUN</td><td class="pj-uz">hiragana dumi bor — koʻrmoq</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Bu qoida taxmin beradi, kafolat emas.</b> Istisnolar bor va ular kam
  emas. Lekin qoida sizni <em>koʻpincha</em> toʻgʻri javobga olib boradi, va bu
  boshlovchi uchun juda katta yordam. Qolgan hollarda esa furigana bor —
  shuning uchun bu kursda hech qachon taxminga tayanib qolmaysiz.</p>
</div>

<h3>3. Okurigana — hiragana dumi bejiz emas</h3>

<p><b>Okurigana</b> (<ruby>送<rt>おく</rt></ruby>り<ruby>仮名<rt>がな</rt></ruby>)
— kanjidan keyin keladigan hiragana. U ikkita ish qiladi va ikkalasi ham
muhim.</p>

<ol class="pe-steps">
  <li><b>Oʻqilishni koʻrsatadi.</b> Dum bor — demak kun'yomi. Bu birinchi
  signal.</li>
  <li><b>Tuslanishni tashiydi.</b> Feʼl va sifat oʻzgarganda kanji
  <em>qimirlamaydi</em>, faqat dum oʻzgaradi.</li>
</ol>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Kanji</th><th>Dum</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>見<rt>み</rt></ruby>る</td><td class="pj-stem"><ruby>見<rt>み</rt></ruby></td>
      <td class="pj-end">る</td><td class="pj-uz">koʻrmoq</td></tr>
  <tr><td><ruby>見<rt>み</rt></ruby>ます</td><td class="pj-stem"><ruby>見<rt>み</rt></ruby></td>
      <td class="pj-end">ます</td><td class="pj-uz">koʻraman (hurmat)</td></tr>
  <tr><td><ruby>見<rt>み</rt></ruby>ました</td><td class="pj-stem"><ruby>見<rt>み</rt></ruby></td>
      <td class="pj-end">ました</td><td class="pj-uz">koʻrdim</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tili bilan taqqoslash aynan mos tushadi.</b> Oʻzbekchada ham
  oʻzak qimirlamaydi, faqat qoʻshimcha almashadi: <em>koʻr-</em>moq,
  <em>koʻr</em>-di, <em>koʻr</em>-adi. Yapon tilida oʻzak <b>kanjida</b>,
  qoʻshimcha esa <b>hiraganada</b> yoziladi. Yaʼni yozuvning oʻzi oʻzak va
  qoʻshimchani ajratib turadi — oʻzbekchada bu farq koʻrinmaydi.</p>
</div>

<h3>4. Nechta oʻqilish boʻlishi mumkin?</h3>

<p>Koʻpchilik kanjida bitta on va bitta kun boʻladi. Baʼzilarida bir nechta.
Ayrimlarida esa faqat bittasi bor.</p>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">日</span>
    <span class="pj-kanji__uz">quyosh, kun</span>
    <span class="pj-kanji__on">ON: ニチ · ジツ</span>
    <span class="pj-kanji__kun">KUN: ひ · か</span>
    <span class="pj-kanji__note">Eng koʻp oʻqilishli belgilardan biri — shuning uchun uni furiganasiz koʻrsangiz, kontekstga qarang.</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">人</span>
    <span class="pj-kanji__uz">odam</span>
    <span class="pj-kanji__on">ON: ジン · ニン</span>
    <span class="pj-kanji__kun">KUN: ひと</span>
    <span class="pj-kanji__note"><ruby>日本人<rt>にほんじん</rt></ruby> · <ruby>三人<rt>さんにん</rt></ruby> · <ruby>人<rt>ひと</rt></ruby></span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">本</span>
    <span class="pj-kanji__uz">kitob, asos</span>
    <span class="pj-kanji__on">ON: ホン</span>
    <span class="pj-kanji__kun">KUN: もと</span>
    <span class="pj-kanji__note">Deyarli doim ホン: <ruby>日本<rt>にほん</rt></ruby> · <ruby>本<rt>ほん</rt></ruby> — oson belgilardan.</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>日本<rt>にほん</rt></ruby>の<ruby>本<rt>ほん</rt></ruby></p>
  <p class="pe-ex__rom">nihon no hon</p>
  <p class="pe-ex__uz">Yaponiyaning kitobi</p>
  <p class="pe-ex__why">Bitta gapda <ruby>本<rt>ほん</rt></ruby> ikki marta, ikkalasida ham ホン. Birinchisi "asos" maʼnosida (<ruby>日本<rt>にほん</rt></ruby> — quyosh asosi), ikkinchisi "kitob".</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>大<rt>おお</rt></ruby>きい<ruby>山<rt>やま</rt></ruby></p>
  <p class="pe-ex__rom">ōkii yama</p>
  <p class="pe-ex__uz">katta togʻ</p>
  <p class="pe-ex__why">Ikkalasi ham kun'yomi: <ruby>大<rt>おお</rt></ruby> da hiragana dumi bor, <ruby>山<rt>やま</rt></ruby> esa yolgʻiz turibdi.</p>
</div>

<h3>5. Lugʻatda qanday koʻrinadi</h3>

<p>Yapon lugʻatlarida bitta shartli belgi bor va uni bilib qoʻygan maʼqul:
<b>on'yomi katakana bilan</b>, <b>kun'yomi hiragana bilan</b> yoziladi.
Bu — oʻqilish emas, <em>turini koʻrsatadigan</em> shartli belgi. Haqiqiy matnda
ikkalasi ham hiraganada furigana boʻlib chiqadi.</p>

<div class="pj-say">
  <span class="pj-say__from"><ruby>山<rt>やま</rt></ruby> → サン / やま</span>
  <span class="pj-say__arrow">=</span>
  <span class="pj-say__to">ON / KUN</span>
  <span class="pj-say__why">katakana on'ni, hiragana kun'ni bildiradi</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ "Har bir kanjining barcha oʻqilishlarini yodlash kerak"</p>
  <p class="pe-fix__good">✓ Oʻqilishni alohida emas, <b>soʻz ichida</b> yodlang. <ruby>日本<rt>にほん</rt></ruby> ni butun soʻz sifatida bilsangiz, <ruby>日<rt>にち</rt></ruby> ning oʻqilishi oʻz-oʻzidan kelib chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Okurigana ni "keraksiz qoʻshimcha" deb tashlab ketish</p>
  <p class="pe-fix__good">✓ Dum <b>oʻqilishni</b> va <b>tuslanishni</b> tashiydi. <ruby>見<rt>み</rt></ruby> yolgʻiz — noaniq; <ruby>見<rt>み</rt></ruby>る — aniq feʼl.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Lugʻatdagi katakanani "bu katakana bilan yoziladi" deb tushunish</p>
  <p class="pe-fix__good">✓ Bu faqat <b>shartli belgi</b>: katakana = on'yomi. Haqiqiy matnda furigana doim hiraganada boʻladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>火山<rt>かざん</rt></ruby> soʻzida qaysi oʻqilish ishlagan va nega?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>On'yomi</b>, chunki ikkita kanji bir-biriga yopishgan. Maʼnosi — vulqon (olov + togʻ).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Nega <ruby>山<rt>やま</rt></ruby> yolgʻiz turganda «やま» oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yolgʻiz turgan kanji odatda <b>kun'yomi</b> — yaponlarning oʻz soʻzi bilan oʻqiladi. やま — yaponcha "togʻ" soʻzi, belgidan ancha oldin mavjud boʻlgan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Okurigana ikkita nima ish qiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchidan, <b>kun'yomi</b> ekanini koʻrsatadi. Ikkinchidan, <b>tuslanishni</b> tashiydi — kanji qimirlamaydi, faqat dum oʻzgaradi: <ruby>見<rt>み</rt></ruby>る → <ruby>見<rt>み</rt></ruby>ます → <ruby>見<rt>み</rt></ruby>ました.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Lugʻatda oʻqilish katakanada berilgan boʻlsa, bu nimani bildiradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Bu <b>on'yomi</b> — xitoychadan kelgan oʻqilish. Bu shartli belgi, xolos: haqiqiy matnda furigana hiraganada yoziladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>日<rt>ひ</rt></ruby> belgisi <ruby>日本人<rt>にほんじん</rt></ruby> da nega «ひ» emas?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki u boshqa kanjilar bilan <b>yopishgan</b> — demak on'yomi ishlaydi. Yolgʻiz turganda esa kun'yomi «ひ» boʻlardi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>音読<rt>おんよ</rt></ruby>み</b> — on'yomi, xitoycha oʻqilish</li>
  <li><b><ruby>訓読<rt>くんよ</rt></ruby>み</b> — kun'yomi, yaponcha oʻqilish</li>
  <li><b><ruby>送<rt>おく</rt></ruby>り<ruby>仮名<rt>がな</rt></ruby></b> — okurigana</li>
  <li><b><ruby>火山<rt>かざん</rt></ruby></b> — vulqon</li>
  <li><b><ruby>日本<rt>にほん</rt></ruby></b> — Yaponiya</li>
  <li><b><ruby>日本人<rt>にほんじん</rt></ruby></b> — yapon (millat)</li>
  <li><b><ruby>本<rt>ほん</rt></ruby></b> — kitob</li>
  <li><b><ruby>見<rt>み</rt></ruby>る</b> — koʻrmoq</li>
  <li><b><ruby>大<rt>おお</rt></ruby>きい</b> — katta</li>
  <li><b><ruby>水曜日<rt>すいようび</rt></ruby></b> — chorshanba</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Ikki oʻqilish — ikki qatlam: <b>on</b> xitoychadan kelgan, <b>kun</b> yaponlarning oʻz soʻzi.</li>
    <li>Qoida: <b>kanji + kanji → on</b>, <b>yolgʻiz yoki kana dumi bilan → kun</b>.</li>
    <li>Oʻqilishni alohida emas, <b>soʻz ichida</b> yodlang — shunda istisnolar ham oʻz-oʻzidan yodda qoladi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-12: Sonlar 一〜百, sana, yosh va birinchi sanoq soʻzlari",
        "category": "japanese",
        "order": 12,
        "summary": (
            "Yaponcha sonlar va ularning tovush oʻzgarishlari, oy va kun nomlari, "
            "hafta kunlari hamda yosh. Yozuv blokining oxirgi darsi."
        ),
        "content": """
<h2>PJ-12: Sonlar <ruby>一<rt>いち</rt></ruby>〜<ruby>百<rt>ひゃく</rt></ruby>, sana, yosh va birinchi sanoq soʻzlari</h2>

<p>Yozuv blokining oxirgi darsi — va darrov foyda beradigani. Sonlar narxda,
soatda, sanada va yoshda uchraydi: Yaponiyada bir kun yurgan odam ularni yuz
marta koʻradi.</p>

<p>Tizimi <b>oʻzbekchadan ham oddiy</b>: 11 dan 99 gacha hamma son qoʻshish va
koʻpaytirish bilan yasaladi. Lekin bitta ogohlantirish bor: <b>baʼzi sonlarning
ikkita oʻqilishi bor</b>, va qaysi birini tanlash keyingi soʻzga bogʻliq. Bugun
shu tuzoqlarni birma-bir belgilab chiqamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>1 dan 100 gacha sanaysiz va yozasiz</li>
    <li>4, 7, 9 sonlarining ikkita oʻqilishi qachon ishlatilishini bilasiz</li>
    <li>Oy nomlari va kun sanalarini oʻqiysiz — shu jumladan istisnolarni</li>
    <li>Hafta kunlarini va yoshni aytasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Sonning tuzilishi</span>
  <span class="pe-chip pe-chip--s">2</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">10</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">1</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v"><ruby>二十一<rt>にじゅういち</rt></ruby></span>
</div>

<h3>1. Birdan oʻngacha</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Son</th><th>Kanji</th><th>Oʻqilishi</th><th>Ikkinchi shakli</th></tr>
  <tr><td>1</td><td class="pj-stem">一</td><td class="pj-res">いち</td><td class="pj-uz">—</td></tr>
  <tr><td>2</td><td class="pj-stem">二</td><td class="pj-res">に</td><td class="pj-uz">—</td></tr>
  <tr><td>3</td><td class="pj-stem">三</td><td class="pj-res">さん</td><td class="pj-uz">—</td></tr>
  <tr><td>4</td><td class="pj-stem">四</td><td class="pj-res">よん</td><td class="pj-uz"><b>し</b> — ehtiyot boʻling</td></tr>
  <tr><td>5</td><td class="pj-stem">五</td><td class="pj-res">ご</td><td class="pj-uz">—</td></tr>
  <tr><td>6</td><td class="pj-stem">六</td><td class="pj-res">ろく</td><td class="pj-uz">—</td></tr>
  <tr><td>7</td><td class="pj-stem">七</td><td class="pj-res">なな</td><td class="pj-uz"><b>しち</b> — ehtiyot boʻling</td></tr>
  <tr><td>8</td><td class="pj-stem">八</td><td class="pj-res">はち</td><td class="pj-uz">—</td></tr>
  <tr><td>9</td><td class="pj-stem">九</td><td class="pj-res">きゅう</td><td class="pj-uz"><b>く</b> — ehtiyot boʻling</td></tr>
  <tr><td>10</td><td class="pj-stem">十</td><td class="pj-res">じゅう</td><td class="pj-uz">—</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Uchta sonning ikkita oʻqilishi bor: 4, 7 va 9.</b> Yolgʻiz sanaganda
  odatda <b>よん · なな · きゅう</b> ishlatiladi — ular aniqroq eshitiladi.
  Sana va soatda esa koʻpincha <b>し · しち · く</b> chiqadi. Har bir holatni
  oʻz oʻrnida koʻrasiz; bu darsda eng muhimlarini belgilab qoʻyamiz.</p>
</div>

<h3>2. 11 dan 99 gacha — faqat qoʻshish va koʻpaytirish</h3>

<p>Bu yerda yapon tili saxiy: yangi soʻz yodlash <b>kerak emas</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Son</th><th>Tuzilishi</th><th>Kanji</th><th>Oʻqilishi</th></tr>
  <tr><td>11</td><td class="pj-uz">10 + 1</td><td class="pj-stem">十一</td><td class="pj-res">じゅういち</td></tr>
  <tr><td>15</td><td class="pj-uz">10 + 5</td><td class="pj-stem">十五</td><td class="pj-res">じゅうご</td></tr>
  <tr><td>20</td><td class="pj-uz">2 × 10</td><td class="pj-stem">二十</td><td class="pj-res">にじゅう</td></tr>
  <tr><td>34</td><td class="pj-uz">3 × 10 + 4</td><td class="pj-stem">三十四</td><td class="pj-res">さんじゅうよん</td></tr>
  <tr><td>68</td><td class="pj-uz">6 × 10 + 8</td><td class="pj-stem">六十八</td><td class="pj-res">ろくじゅうはち</td></tr>
  <tr><td>99</td><td class="pj-uz">9 × 10 + 9</td><td class="pj-stem">九十九</td><td class="pj-res">きゅうじゅうきゅう</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchadan ham tartibliroq.</b> Bizda "oʻn bir", "yigirma", "oʻttiz" —
  har biri alohida soʻz. Yapon tilida esa 20 shunchaki "ikki oʻn", 34 esa
  "uch oʻn toʻrt".</p>
</div>

<h3>3. Yuz, ming va tovush oʻzgarishlari</h3>

<p>Yuzdan yuqorida bitta tuzoq bor: baʼzi birikmalarda tovush <b>oʻzgaradi</b>.
Bu tartibsizlik emas — talaffuzni yengillashtiradigan tabiiy hodisa. Ularni
yodlab qoʻygan maʼqul: narxlarda doim uchraydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Son</th><th>Kutilgan</th><th>Haqiqiy</th><th>Nima oʻzgardi</th></tr>
  <tr><td>100</td><td class="pj-uz">—</td><td class="pj-res">ひゃく</td><td class="pj-uz">asosiy shakl</td></tr>
  <tr><td>300</td><td class="pj-uz">さんひゃく</td><td class="pj-res">さんびゃく</td><td class="pj-uz">ひ → び</td></tr>
  <tr><td>600</td><td class="pj-uz">ろくひゃく</td><td class="pj-res">ろっぴゃく</td><td class="pj-uz">ひ → ぴ, oldida っ</td></tr>
  <tr><td>800</td><td class="pj-uz">はちひゃく</td><td class="pj-res">はっぴゃく</td><td class="pj-uz">ひ → ぴ, oldida っ</td></tr>
  <tr><td>1000</td><td class="pj-uz">—</td><td class="pj-res">せん</td><td class="pj-uz">asosiy shakl</td></tr>
  <tr><td>3000</td><td class="pj-uz">さんせん</td><td class="pj-res">さんぜん</td><td class="pj-uz">せ → ぜ</td></tr>
  <tr><td>8000</td><td class="pj-uz">はちせん</td><td class="pj-res">はっせん</td><td class="pj-uz">oldida っ</td></tr>
  <tr><td>10 000</td><td class="pj-uz">まん</td><td class="pj-res">いちまん</td><td class="pj-uz">doim いち bilan</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>10 000 ni eslab qoling:</b> u «まん» emas, doim <b>いちまん</b>.</p>
</div>

<h3>4. Oy nomlari — 〜<ruby>月<rt>がつ</rt></ruby></h3>

<p>Oylar oddiy: son + <ruby>月<rt>がつ</rt></ruby>, alohida nom yoʻq —
"yanvar" shunchaki "birinchi oy". Lekin <b>uchta oyda</b> majburiy oʻqilish
bor.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oy</th><th>Kanji</th><th>Oʻqilishi</th><th>Diqqat</th></tr>
  <tr><td>yanvar</td><td class="pj-stem">一月</td><td class="pj-res">いちがつ</td><td class="pj-uz">—</td></tr>
  <tr><td>aprel</td><td class="pj-stem">四月</td><td class="pj-res">しがつ</td><td class="pj-uz"><b>よんがつ EMAS</b></td></tr>
  <tr><td>iyul</td><td class="pj-stem">七月</td><td class="pj-res">しちがつ</td><td class="pj-uz"><b>ななかつ EMAS</b></td></tr>
  <tr><td>sentabr</td><td class="pj-stem">九月</td><td class="pj-res">くがつ</td><td class="pj-uz"><b>きゅうがつ EMAS</b></td></tr>
  <tr><td>oktabr</td><td class="pj-stem">十月</td><td class="pj-res">じゅうがつ</td><td class="pj-uz">—</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Aynan shu uchtasi — 4, 7, 9 — muammo tugʻdiradi.</b> Oylarda ular
  <b>し · しち · く</b> shaklini <em>majburan</em> oladi: «よんがつ» deb
  aytsangiz, yaponcha eshitilmaydi.</p>
</div>

<h3>5. Kun sanalari — darsdagi eng qiyin jadval</h3>

<p>Rostini aytamiz: <b>oyning birinchi oʻn kuni butunlay istisno</b> — ular
qadimgi yaponcha sanoqdan yasalgan va yodlash kerak. 11-kundan boshlab esa
hammasi qoidaga qaytadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Kun</th><th>Kanji</th><th>Oʻqilishi</th><th>Kun</th><th>Kanji</th><th>Oʻqilishi</th></tr>
  <tr><td>1</td><td class="pj-stem">一日</td><td class="pj-res">ついたち</td>
      <td>6</td><td class="pj-stem">六日</td><td class="pj-res">むいか</td></tr>
  <tr><td>2</td><td class="pj-stem">二日</td><td class="pj-res">ふつか</td>
      <td>7</td><td class="pj-stem">七日</td><td class="pj-res">なのか</td></tr>
  <tr><td>3</td><td class="pj-stem">三日</td><td class="pj-res">みっか</td>
      <td>8</td><td class="pj-stem">八日</td><td class="pj-res">ようか</td></tr>
  <tr><td>4</td><td class="pj-stem">四日</td><td class="pj-res">よっか</td>
      <td>9</td><td class="pj-stem">九日</td><td class="pj-res">ここのか</td></tr>
  <tr><td>5</td><td class="pj-stem">五日</td><td class="pj-res">いつか</td>
      <td>10</td><td class="pj-stem">十日</td><td class="pj-res">とおか</td></tr>
</table></div>

<p>11-kundan keyin qoida qaytadi: son + <ruby>日<rt>にち</rt></ruby>. Lekin
uchta istisno qoladi — yuqoridagi jadvaldan meros:</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Kun</th><th>Oʻqilishi</th><th>Izoh</th></tr>
  <tr><td>11</td><td class="pj-res">じゅういちにち</td><td class="pj-uz">qoidaga toʻliq mos</td></tr>
  <tr><td>14</td><td class="pj-res">じゅうよっか</td><td class="pj-uz"><b>istisno</b> — よっか saqlanadi</td></tr>
  <tr><td>20</td><td class="pj-res">はつか</td><td class="pj-uz"><b>istisno</b> — mutlaqo alohida soʻz</td></tr>
  <tr><td>24</td><td class="pj-res">にじゅうよっか</td><td class="pj-uz"><b>istisno</b> — yana よっか</td></tr>
  <tr><td>30</td><td class="pj-res">さんじゅうにち</td><td class="pj-uz">qoidaga mos</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Qanday yodlash kerak.</b> Jadval sifatida emas, <em>ovoz chiqarib</em>:
  ついたち・ふつか・みっか・よっか・いつか・むいか・なのか・ようか・ここのか・
  とおか. Ular bir ritmga tushadi va qoʻshiqdek yodda qoladi. Keyin faqat
  uchtasini qoʻshasiz: <b>14 · 20 · 24</b>.</p>
</div>

<h3>6. Hafta kunlari va yosh</h3>

<p>Hafta kunlari chiroyli tizimga ega: tabiat unsuri +
<ruby>曜日<rt>ようび</rt></ruby>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Kun</th><th>Kanji</th><th>Oʻqilishi</th><th>Unsur</th></tr>
  <tr><td>dushanba</td><td class="pj-stem">月曜日</td><td class="pj-res">げつようび</td><td class="pj-uz">oy</td></tr>
  <tr><td>seshanba</td><td class="pj-stem">火曜日</td><td class="pj-res">かようび</td><td class="pj-uz">olov</td></tr>
  <tr><td>chorshanba</td><td class="pj-stem">水曜日</td><td class="pj-res">すいようび</td><td class="pj-uz">suv</td></tr>
  <tr><td>payshanba</td><td class="pj-stem">木曜日</td><td class="pj-res">もくようび</td><td class="pj-uz">daraxt</td></tr>
  <tr><td>juma</td><td class="pj-stem">金曜日</td><td class="pj-res">きんようび</td><td class="pj-uz">oltin</td></tr>
  <tr><td>shanba</td><td class="pj-stem">土曜日</td><td class="pj-res">どようび</td><td class="pj-uz">tuproq</td></tr>
  <tr><td>yakshanba</td><td class="pj-stem">日曜日</td><td class="pj-res">にちようび</td><td class="pj-uz">quyosh</td></tr>
</table></div>

<p>Yosh — son + <ruby>歳<rt>さい</rt></ruby>. Uchta joyda tovush oʻzgaradi,
bittasida esa butunlay boshqa soʻz chiqadi:</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yosh</th><th>Oʻqilishi</th><th>Izoh</th></tr>
  <tr><td>1</td><td class="pj-res">いっさい</td><td class="pj-uz">いちさい emas</td></tr>
  <tr><td>8</td><td class="pj-res">はっさい</td><td class="pj-uz">はちさい emas</td></tr>
  <tr><td>10</td><td class="pj-res">じゅっさい</td><td class="pj-uz">じっさい ham toʻgʻri</td></tr>
  <tr><td>20</td><td class="pj-res">はたち</td><td class="pj-uz"><b>butunlay alohida soʻz</b></td></tr>
  <tr><td>15</td><td class="pj-res">じゅうごさい</td><td class="pj-uz">qoidaga mos</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>四月<rt>しがつ</rt></ruby><ruby>二十日<rt>はつか</rt></ruby>、<ruby>月曜日<rt>げつようび</rt></ruby></p>
  <p class="pe-ex__rom">shigatsu hatsuka, getsuyōbi</p>
  <p class="pe-ex__uz">20-aprel, dushanba</p>
  <p class="pe-ex__why">Ikkita istisno bitta sanada: <ruby>四月<rt>しがつ</rt></ruby> (よんがつ emas) va <ruby>二十日<rt>はつか</rt></ruby> (にじゅうにち emas). Yapon sanalari yozilishida ham katta boʻlakdan kichigiga qarab boradi: yil → oy → kun.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>は<ruby>十五歳<rt>じゅうごさい</rt></ruby>です</p>
  <p class="pe-ex__rom">watashi wa jūgosai desu</p>
  <p class="pe-ex__uz">Men oʻn besh yoshdaman.</p>
  <p class="pe-ex__why">15 qoidaga toʻliq mos: じゅう + ご + さい. Faqat 1, 8, 10 va 20 da oʻzgarish bor.</p>
</div>

<h3>7. Sanoq soʻzlari — qisqacha ogohlantirish</h3>

<p>Narsani sanash uchun sonning oʻzi <b>yetmaydi</b>: son bilan narsa orasiga
<em>sanoq soʻzi</em> qoʻyiladi va u narsaning turiga qarab oʻzgaradi. Odam uchun
<ruby>人<rt>にん</rt></ruby>, yassi narsa uchun <ruby>枚<rt>まい</rt></ruby>.</p>

<div class="pj-say">
  <span class="pj-say__from"><ruby>一人<rt>ひとり</rt></ruby> · <ruby>二人<rt>ふたり</rt></ruby></span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to"><ruby>三人<rt>さんにん</rt></ruby></span>
  <span class="pj-say__why">birinchi ikkitasi istisno, uchinchisidan qoida boshlanadi</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham bu bor</b> — "bir <em>bosh</em> qoʻy", "uch
  <em>nafar</em> odam". Farqi shuki, oʻzbekchada bu ixtiyoriy, yapon tilida
  <b>majburiy</b>. Toʻliq tizimni PJ-43 da koʻramiz; hozircha
  <ruby>一人<rt>ひとり</rt></ruby> va <ruby>二人<rt>ふたり</rt></ruby> ni
  yodlab qoʻying.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Aprelni «よんがつ» deb aytish</p>
  <p class="pe-fix__good">✓ <b>しがつ</b>. Oylarda 4, 7, 9 majburan し · しち · く shaklini oladi — bu tanlov emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Oyning 20-kunini «にじゅうにち» deb aytish</p>
  <p class="pe-fix__good">✓ <b>はつか</b> — butunlay alohida soʻz. Xuddi shunday 14 va 24 da ham よっか saqlanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ 10 000 ni «まん» deb aytish</p>
  <p class="pe-fix__good">✓ <b>いちまん</b> — doim いち bilan. «まん» yolgʻiz ishlatilmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>三十四<rt>さんじゅうよん</rt></ruby> — bu qaysi son va qanday yasalgan?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>34</b> — 3 × 10 + 4. Yaponchada 11 dan 99 gacha hamma son shu tarzda qoʻshish va koʻpaytirish bilan yasaladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Aprel oyi qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>しがつ</b> (<ruby>四月<rt>しがつ</rt></ruby>). «よんがつ» notoʻgʻri — oylarda 4 majburan «し» boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Oyning 20-kuni qanday aytiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>はつか</b>. Bu — qoidaga boʻysunmaydigan alohida soʻz, xuddi 14 (じゅうよっか) va 24 (にじゅうよっか) kabi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Payshanba kuni qaysi unsur bilan bogʻliq?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Daraxt</b> — <ruby>木曜日<rt>もくようび</rt></ruby>. Hafta kunlari tabiat unsurlaridan yasalgan: oy, olov, suv, daraxt, oltin, tuproq, quyosh.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Yigirma yosh qanday aytiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>はたち</b> — «にじゅっさい» emas. Bu butunlay alohida soʻz va Yaponiyada muhim yosh sanaladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>一<rt>いち</rt></ruby> · <ruby>二<rt>に</rt></ruby> · <ruby>三<rt>さん</rt></ruby></b> — 1, 2, 3</li>
  <li><b><ruby>四<rt>よん</rt></ruby> · <ruby>七<rt>なな</rt></ruby> · <ruby>九<rt>きゅう</rt></ruby></b> — ikkinchi shakli し · しち · く</li>
  <li><b><ruby>十<rt>じゅう</rt></ruby> · <ruby>百<rt>ひゃく</rt></ruby> · <ruby>千<rt>せん</rt></ruby></b> — 10, 100, 1000</li>
  <li><b><ruby>一万<rt>いちまん</rt></ruby></b> — 10 000</li>
  <li><b><ruby>四月<rt>しがつ</rt></ruby></b> — aprel</li>
  <li><b><ruby>二十日<rt>はつか</rt></ruby></b> — oyning 20-kuni</li>
  <li><b><ruby>曜日<rt>ようび</rt></ruby></b> — hafta kuni</li>
  <li><b><ruby>歳<rt>さい</rt></ruby></b> — yosh (sanoq soʻzi)</li>
  <li><b><ruby>二十歳<rt>はたち</rt></ruby></b> — yigirma yosh</li>
  <li><b><ruby>一人<rt>ひとり</rt></ruby> · <ruby>二人<rt>ふたり</rt></ruby></b> — bir kishi, ikki kishi</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>11 dan 99 gacha yangi soʻz yoʻq — faqat <b>qoʻshish va koʻpaytirish</b>.</li>
    <li>Muammo doim <b>4, 7 va 9</b> da: oylarda ular majburan し · しち · く boʻladi.</li>
    <li>Oyning birinchi oʻn kuni butunlay istisno, ustiga <b>14 · 20 · 24</b> qoʻshiladi. Yozuv bloki tugadi — PJ-13 dan grammatika boshlanadi.</li>
  </ul>
</div>
""",
    },
]
