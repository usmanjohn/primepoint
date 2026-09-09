# -*- coding: utf-8 -*-
"""Prime Japanese — Block A, darslar 1–3 (uchta yozuv).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_JAPANESE.md
Lesson list: tutorial/management/commands/toc_prime_japanese.txt

Block A darslarida grammatika yoʻq, shuning uchun oʻqish matni ham yoʻq.
Har bir darsning ikkinchi boʻlagi — 12 savollik mashq:
practice/management/commands/_practice_pj_01_03.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_01_03.py --author=prime
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
        "title": "PJ-1: Yapon yozuvi — nega uchta alifbo bor va ular qanday birga ishlaydi",
        "category": "japanese",
        "order": 1,
        "summary": (
            "Yapon tilida uchta yozuv tizimi bir vaqtda ishlaydi. Bu darsda ularning har biri "
            "nima uchun kerakligini bilib olasiz va birinchi yaponcha gapni qismlarga ajratasiz."
        ),
        "content": """
<h2>PJ-1: Yapon yozuvi — nega uchta alifbo bor va ular qanday birga ishlaydi</h2>

<p>Yapon tilidagi eng oddiy gapga qarang: <b>わたしは日本語を勉強します。</b> Bu yerda
uch xil yozuv bor. <b>わたしは</b> — bitta alifbo. <b>日本語</b> — butunlay boshqa
tizim. <b>を</b> va <b>します</b> — yana birinchisi. Agar bu sizga adolatsizdek
tuyulsa, siz yolgʻiz emassiz: har bir yangi oʻquvchi shu yerda toʻxtaydi va
"nega ular bitta alifbo bilan kifoyalanmagan?" deb soʻraydi.</p>

<p>Javob bor, va u juda mantiqiy. Bugun shu javobni bilib olasiz — keyin qolgan
oʻn bir dars davomida uchala tizimni birma-bir oʻzlashtiramiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Hiragana, katakana va kanji nima uchun kerakligini tushunasiz</li>
    <li>Yaponcha gapga qarab, qaysi qism qaysi yozuvda ekanini aytib bera olasiz</li>
    <li>Yapon tili oʻzbek tiliga qayerda oʻxshashini koʻrasiz — bu butun kurs davomida yordam beradi</li>
    <li>Furigana nima ekanini va nega undan qoʻrqmaslik kerakligini bilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta gap, uchta yozuv</span>
  <span class="pe-chip pe-chip--s">KANJI = maʼno</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">HIRAGANA = grammatika</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">KATAKANA = chetdan kelgan</span>
</div>

<h3>1. Uchta tizim, uchta vazifa</h3>

<p>Eng muhim gap shu: <b>bu uchta alifbo bir-birining raqibi emas</b>. Ularning har
birining oʻz ishi bor, xuddi oʻzbek matnidagi harflar, raqamlar va tinish
belgilari kabi. Siz "12 kishi keldi" deb yozganingizda ikkita tizimni aralashtirasiz —
harflar va raqamlar — va buni gʻalati deb hisoblamaysiz. Yapon tilida ham xuddi shunday,
faqat tizimlar uchta.</p>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">あ</span>
    <span class="pj-kanji__uz">HIRAGANA — 46 ta belgi</span>
    <span class="pj-kanji__on">Vazifasi: grammatika</span>
    <span class="pj-kanji__kun">Shakli: yumaloq, oqadigan</span>
    <span class="pj-kanji__note">Qoʻshimchalar, feʼl oxirlari, sof yaponcha soʻzlar. Birinchi oʻrganiladigan tizim.</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">ア</span>
    <span class="pj-kanji__uz">KATAKANA — 46 ta belgi</span>
    <span class="pj-kanji__on">Vazifasi: chet soʻzlar</span>
    <span class="pj-kanji__kun">Shakli: burchakli, keskin</span>
    <span class="pj-kanji__note">Chet tillardan kirgan soʻzlar, chet el ismlari, tovush taqlidi. Sizning ismingiz ham shu yerda.</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">日</span>
    <span class="pj-kanji__uz">KANJI — minglab belgi</span>
    <span class="pj-kanji__on">Vazifasi: maʼno</span>
    <span class="pj-kanji__kun">Shakli: murakkab, rasmga oʻxshash</span>
    <span class="pj-kanji__note">Otlar, feʼl va sifat oʻzaklari. Har biri tovushni emas, maʼnoni bildiradi.</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Ikkitasi bir xil tovushni beradi.</b> Hiragana va katakana — bir xil 46 ta
  tovushning ikki xil kiyimi. あ va ア — ikkalasi ham "a". Yodlash ikki barobar
  koʻpayadi, lekin qoida bitta: <em>yaponcha soʻz — hiragana, chetdan kelgan
  soʻz — katakana</em>. Kanji esa butunlay boshqa dunyo: u tovushni emas, maʼnoni
  yozadi.</p>
</div>

<h3>2. Nega bitta alifbo yetmaydi?</h3>

<p>Aslida yetardi. Yapon tilini faqat hiragana bilan yozish mumkin — bolalar kitoblari
aynan shunday yoziladi. Lekin bitta jiddiy muammo bor: <b>yapon tilida bir xil
eshitiladigan soʻzlar juda koʻp</b>.</p>

<p><b>こうしょう</b> deb oʻqiladigan soʻzlar oʻttizdan ortiq: muzokara, baland ovoz,
zavod, maktab direktori... Faqat hiragana bilan yozsangiz, hammasi bir xil koʻrinadi.
Kanji bilan yozilganda esa ularning har biri boshqacha koʻrinadi va koʻz bir zumda
farqlaydi.</p>

<div class="pe-call pe-rule">
  <p><b>Qoida:</b> kanji — yapon tilining <em>koʻz uchun</em> ishlaydigan lugʻati.
  Quloq adashadi, koʻz adashmaydi. Shuning uchun yaponlar kanjidan voz kechmagan
  va kechmaydi ham.</p>
</div>

<p>Ikkinchi sabab — <b>boʻshliq</b>. Yaponcha matnda soʻzlar orasida boʻshliq
qoʻyilmaydi. Oʻzbekchada "menkitoboʻqiyman" deb yozsak, oʻqish ogʻirlashadi.
Yaponchada esa kanji va hiragana almashib turgani soʻz chegarasini oʻzi
koʻrsatib beradi: kanji koʻrinsa — yangi soʻz boshlandi, hiragana koʻrinsa —
grammatika davom etyapti.</p>

<h3>3. Birinchi gapni qismlarga ajratamiz</h3>

<p>Endi boshidagi gapga qaytamiz. Har bir boʻlakning rangiga qarang:</p>

<div class="pj-joshi">
  <span class="pj-joshi__n">わたし</span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n"><ruby>日本語<rt>にほんご</rt></ruby></span>
  <span class="pj-joshi__p">を<small>TOʻLDIRUVCHI</small></span>
  <span class="pj-joshi__v"><ruby>勉強<rt>べんきょう</rt></ruby>します</span>
  <span class="pj-joshi__uz">Men yapon tilini oʻrganaman.</span>
</div>

<ul>
  <li><b>わたし</b> — hiragana. "Men". Sof yaponcha soʻz.</li>
  <li><b>は</b> — hiragana. Grammatik qoʻshimcha (助詞), mavzuni belgilaydi.</li>
  <li><b>日本語</b> — kanji. "Yapon tili". Maʼno tashiydigan qism.</li>
  <li><b>を</b> — hiragana. Toʻldiruvchi qoʻshimchasi.</li>
  <li><b>勉強</b> — kanji. "Oʻqish, mashgʻulot". <b>します</b> — hiragana, feʼl oxiri.</li>
</ul>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek oʻquvchi uchun katta yangilik:</b> bu gapning tartibi oʻzbekchaga
  <em>aynan</em> mos keladi. "Men — yapon tili<b>ni</b> — oʻrganaman". Feʼl oxirida,
  qoʻshimcha soʻzga yopishgan. Ingliz tilida feʼl gap oʻrtasida turadi, shuning
  uchun ingliz tili orqali yapon tilini oʻrganayotgan odam bu yerda qiynaladi.
  Siz qiynalmaysiz: yapon tili ham, oʻzbek tili ham <b>SOV</b> tili —
  ega → toʻldiruvchi → feʼl.</p>
</div>

<h3>4. Katakana qayerda ishlaydi</h3>

<p>Katakana — yaponchaning "chet el eshigi". Undan uch narsa uchun foydalaniladi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Chet soʻzlar</p>
    <p>コーヒー — kofe<br>テレビ — televizor<br>パン — non (portugalchadan)</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Chet el ismlari</p>
    <p>アフソナ — Afsona<br>ジャスル — Jasur<br>ウズベキスタン — Oʻzbekiston</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Tovush taqlidi</p>
    <p>ワンワン — vov-vov<br>ゴロゴロ — momaqaldiroq<br>キラキラ — yaltirash</p></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">アフソナさんは<ruby>日本<rt>にほん</rt></ruby>のコーヒーが<ruby>好<rt>す</rt></ruby>きです。</p>
  <p class="pe-ex__rom">afusona-san wa nihon no kōhī ga suki desu</p>
  <p class="pe-ex__uz">Afsona yapon kofesini yaxshi koʻradi.</p>
  <p class="pe-ex__why">アフソナ va コーヒー — katakana (ism va chet soʻz), 日本 va 好 — kanji, qolgani hiragana. Bitta gapda uchala yozuv ham ishlayapti.</p>
</div>

<h3>5. Furigana — sizning eng yaxshi doʻstingiz</h3>

<p>Yuqoridagi misollarda kanji ustida kichkina hiragana turganini payqadingizmi?
<ruby>日本語<rt>にほんご</rt></ruby> — ustidagi にほんご bu kanjining qanday
oʻqilishini aytadi. Bu <b>furigana</b> (ふりがな).</p>

<div class="pe-call pe-tip">
  <p><b>Prime Japanese'da har bir kanji butun kurs davomida furigana bilan yoziladi.</b>
  Yuzinchi darsda ham. Bu — imtiyoz emas, yapon tilidagi oʻquv materiallari
  shunday chop etiladi. Demak siz hech qachon "bu belgini bilmayman" deb
  toʻxtab qolmaysiz: oʻqilishi doim koʻz oldingizda.</p>
</div>

<h3>6. Yoʻl xaritasi — keyingi oʻn bir dars</h3>

<ol class="pe-steps">
  <li><b>PJ-2 … PJ-5</b> — Hiragana. 46 ta belgi, toʻrt darsda. Kursdagi eng koʻp yodlash shu yerda.</li>
  <li><b>PJ-6</b> — Qoʻshimcha belgilar: が, きゃ, っ. Hiragananing "sozlagichlari".</li>
  <li><b>PJ-7 … PJ-9</b> — Katakana. Hiragana bilgandan keyin ancha oson.</li>
  <li><b>PJ-10 … PJ-12</b> — Kanji bilan tanishuv, ikki xil oʻqilish va sonlar.</li>
  <li><b>PJ-13 dan</b> — grammatika boshlanadi. Siz esa allaqachon oʻqiy olasiz.</li>
</ol>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ "Avval kanjini oʻrganaman, kana keyin."</p>
  <p class="pe-fix__good">✓ Avval hiragana. Kanjisiz gap tushunarli qoladi, hiraganasiz esa hech qanday gap tuzib boʻlmaydi — barcha qoʻshimchalar va feʼl oxirlari hiraganada.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ "Katakana keraksiz, uni keyinroq oʻrganaman."</p>
  <p class="pe-fix__good">✓ Menyu, doʻkon, reklama va texnika soʻzlarining yarmi katakanada. Yaponiyaga borgan odam katakanani hiraganadan koʻra tez-tez oʻqiydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ "Romaji (lotin harflari) bilan oʻrganaveraman."</p>
  <p class="pe-fix__good">✓ Romaji — birinchi oʻn ikki darsdagi tayanch tayoq, keyin tashlanadi. Romajida qolgan oʻquvchi hech qachon yaponcha matn oʻqiy olmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <b>テレビ</b> qaysi yozuvda va nega?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Katakana. Bu soʻz ingliz tilidagi "television" dan kirgan — chet soʻz, demak katakana.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Gapda kanji koʻrinsa, bu nimadan darak beradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yangi soʻz boshlanganidan. Yaponchada boʻshliq yoʻq, shuning uchun kanji va hiragananing almashinuvi soʻz chegarasini koʻrsatadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Nega faqat hiragana bilan yozish qulay emas?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yapon tilida bir xil eshitiladigan soʻzlar juda koʻp (こうしょう — oʻttizdan ortiq maʼno). Kanji ularni koʻz uchun ajratib beradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <b>ジャスル</b> — bu nima va nega bu yozuvda?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>"Jasur" ismi. Chet el ismi boʻlgani uchun katakanada yoziladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>日本語<rt>にほんご</rt></ruby> ustidagi にほんご nima deyiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Furigana. Kanjining qanday oʻqilishini koʻrsatadi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ひらがな</b> — hiragana, yumaloq yozuv</li>
  <li><b>カタカナ</b> — katakana, burchakli yozuv</li>
  <li><b><ruby>漢字<rt>かんじ</rt></ruby></b> — kanji, maʼno bildiruvchi belgilar</li>
  <li><b>ふりがな</b> — kanji ustidagi oʻqilish</li>
  <li><b><ruby>助詞<rt>じょし</rt></ruby></b> — grammatik qoʻshimcha</li>
  <li><b>わたし</b> — men</li>
  <li><b><ruby>日本語<rt>にほんご</rt></ruby></b> — yapon tili</li>
  <li><b><ruby>勉強<rt>べんきょう</rt></ruby>する</b> — oʻrganmoq</li>
  <li><b>コーヒー</b> — kofe</li>
  <li><b>ローマ<ruby>字<rt>じ</rt></ruby></b> — romaji, lotin yozuvi</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Uchta yozuv raqib emas: <b>kanji maʼno</b>, <b>hiragana grammatika</b>, <b>katakana chetdan kelgan</b>.</li>
    <li>Hiragana va katakana bir xil 46 tovushni beradi — farqi vazifasida, tovushida emas.</li>
    <li>Yapon tili ham oʻzbek tili kabi SOV: feʼl oxirida, qoʻshimcha soʻzga yopishadi. Bu — sizning ustunligingiz.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-2: Hiragana 1 — あ い う え お · か き く け こ · さ し す せ そ",
        "category": "japanese",
        "order": 2,
        "summary": (
            "Hiragananing birinchi 15 belgisi: beshta unli va ularning k- hamda s- qatorlari. "
            "Dars oxirida siz oʻnlab haqiqiy yaponcha soʻzni oʻqiy olasiz."
        ),
        "content": """
<h2>PJ-2: Hiragana 1 — あ い う え お · か き く け こ · さ し す せ そ</h2>

<p>Yapon tilida <b>beshta unli bor</b>. Hammasi boʻlib beshta — oʻzbek tilidagi
oltitadan ham kam, ingliz tilidagi oʻn ikkitadan esa ikki barobar kam. Va ularning
har biri doim bir xil oʻqiladi: あ har doim "a", hech qachon boshqa narsa emas.
Bugun shu beshtasini, keyin ularga <b>k</b> va <b>s</b> qoʻshib hosil boʻlgan
oʻn belgini oʻrganamiz. Oxirida <b>あさ</b> (ertalab) va <b>すし</b> (sushi) kabi
haqiqiy soʻzlarni oʻqiysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Beshta yapon unlisini yozasiz va aytasiz</li>
    <li>Hiragananing tuzilish mantiqini tushunasiz: undosh + unli = bitta belgi</li>
    <li>か-qatori va さ-qatorini toʻliq oʻqiysiz</li>
    <li>Oʻn beshta belgidan tuzilgan yaponcha soʻzlarni oʻqiy olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Hiragananing mantigʻi</span>
  <span class="pe-chip pe-chip--s">UNDOSH</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">UNLI</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">BITTA BELGI</span>
</div>

<h3>1. Beshta unli — butun tizimning poydevori</h3>

<p>Boshqa har bir hiragana belgisi shu beshtadan birini oxirida saqlaydi. Shuning uchun
ularni mustahkam oʻrganish kerak: bugun sarflagan yigirma daqiqangiz keyingi
oʻn dars davomida foyda beradi.</p>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">あ</span><span class="pj-kana__rom">a</span>
    <span class="pj-kana__uz">"ota" dagi a</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">い</span><span class="pj-kana__rom">i</span>
    <span class="pj-kana__uz">"ikki" dagi i</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">う</span><span class="pj-kana__rom">u</span>
    <span class="pj-kana__uz">lab choʻzilmaydigan u</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">え</span><span class="pj-kana__rom">e</span>
    <span class="pj-kana__uz">"eshik" dagi e</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">お</span><span class="pj-kana__rom">o</span>
    <span class="pj-kana__uz">"olma" dagi o</span></div>
</div>

<div class="pe-call pe-uz">
  <p><b>う — yagona qiyin unli.</b> Oʻzbekcha "u" da lablar oldinga choʻziladi
  ("uch"). Yaponchada esa lablar <em>deyarli qimirlamaydi</em> — ogʻiz yassi
  qoladi, tovush "u" va "ы" orasida chiqadi. Agar lablaringizni choʻzsangiz,
  yaponcha emas, ingliz aksenti eshitiladi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Yodlash uchun tartib:</b> <b>a-i-u-e-o</b>. Har bir yapon lugʻati, har bir
  jadval, har bir feʼl tuslanishi shu tartibda yuradi. Bir marta yodlang —
  yuzinchi darsgacha ishlatasiz.</p>
</div>

<h3>2. か-qatori: undosh qoʻshamiz</h3>

<p>Endi mantiq ochiladi. Beshta unlining oldiga <b>k</b> tovushini qoʻysangiz,
beshta yangi belgi hosil boʻladi. Yodlash kerak boʻlgani — shakli, tovushi esa
oʻz-oʻzidan kelib chiqadi.</p>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">か</span><span class="pj-kana__rom">ka</span>
    <span class="pj-kana__uz">か = k + a</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">き</span><span class="pj-kana__rom">ki</span>
    <span class="pj-kana__uz">き = k + i</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">く</span><span class="pj-kana__rom">ku</span>
    <span class="pj-kana__uz">く = k + u</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">け</span><span class="pj-kana__rom">ke</span>
    <span class="pj-kana__uz">け = k + e</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">こ</span><span class="pj-kana__rom">ko</span>
    <span class="pj-kana__uz">こ = k + o</span></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Qoida:</b> hiragana — alifbo emas, <b>boʻgʻin yozuvi</b>. Bitta belgi bitta
  harfni emas, bitta <em>boʻgʻin</em>ni bildiradi. Shuning uchun か ni "k" va "a"
  ga ajratib boʻlmaydi — u bitta butun.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek oʻquvchi uchun yaxshi xabar:</b> oʻzbekcha "ka", "ki", "ku" ni
  yozganda ikkita harf kerak. Yaponchada bitta belgi yetadi. Yozuv qisqaroq,
  lekin belgilar koʻproq — savdo shunday.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Bugungi mehnatingiz ikki marta foyda beradi.</b> Yapon tilida ikkinchi
  alifbo ham bor — katakana. Uning baʼzi belgilari hiragana juftiga juda
  oʻxshaydi, chunki ikkalasi bitta kanjidan chiqqan: <b>か</b> ning katakana
  jufti <b>カ</b>, <b>き</b> niki esa <b>キ</b>. Yaʼni bugun oʻrgangan
  shakllaringizning bir qismini PJ-7 da qaytadan yodlashingiz shart
  boʻlmaydi.</p>
</div>

<h3>3. さ-qatori va uning ikkita tuzogʻi</h3>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">さ</span><span class="pj-kana__rom">sa</span>
    <span class="pj-kana__uz">さ = s + a</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">し</span><span class="pj-kana__rom">shi</span>
    <span class="pj-kana__uz">"si" EMAS — "shi"</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">す</span><span class="pj-kana__rom">su</span>
    <span class="pj-kana__uz">す = s + u</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">せ</span><span class="pj-kana__rom">se</span>
    <span class="pj-kana__uz">せ = s + e</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">そ</span><span class="pj-kana__rom">so</span>
    <span class="pj-kana__uz">そ = s + o</span></div>
</div>

<p><b>Birinchi tuzoq: し.</b> Mantiqan u "si" boʻlishi kerak edi, lekin yaponlar uni
"shi" deb aytadi. Bu istisno emas — butun tilda shunday: <b>s + i doim "shi"</b>.
Xuddi shu narsa keyinroq t-qatorida ham uchraydi.</p>

<div class="pj-say">
  <span class="pj-say__from">し</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[shi]</span>
  <span class="pj-say__why">"si" degan tovush yapon tilida umuman yoʻq</span>
</div>

<p><b>Ikkinchi tuzoq: す.</b> Jarangsiz undoshlar orasida yoki soʻz oxirida
undagi <b>u</b> deyarli eshitilmaydi. <b>すき</b> ("yoqtirmoq") "suki" emas,
<b>[ski]</b> boʻlib chiqadi — u tovushi bor, lekin ovoz bermaydi.</p>

<div class="pj-say">
  <span class="pj-say__from">すき</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[ski]</span>
  <span class="pj-say__why">jarangsiz k oldidan u ovozsiz qoladi</span>
</div>

<div class="pe-call pe-tip">
  <p>Xuddi shu hodisa <b>し</b> va <b>く</b> da ham boʻladi. Buni bilib qoʻyish
  kifoya — atayin "yutish"ga urinmang, tez gapirsangiz oʻzi shunday chiqadi.</p>
</div>

<h3>4. Endi oʻqiymiz</h3>

<p>Oʻn besh belgi bilan qancha soʻz oʻqish mumkinligini koʻring:</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yaponcha</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td>あさ</td><td class="pj-res">asa</td><td class="pj-uz">ertalab</td></tr>
  <tr><td>いす</td><td class="pj-res">isu</td><td class="pj-uz">stul</td></tr>
  <tr><td>すし</td><td class="pj-res">sushi</td><td class="pj-uz">sushi</td></tr>
  <tr><td>あき</td><td class="pj-res">aki</td><td class="pj-uz">kuz</td></tr>
  <tr><td>かさ</td><td class="pj-res">kasa</td><td class="pj-uz">soyabon</td></tr>
  <tr><td>いけ</td><td class="pj-res">ike</td><td class="pj-uz">hovuz</td></tr>
  <tr><td>こえ</td><td class="pj-res">koe</td><td class="pj-uz">ovoz</td></tr>
  <tr><td>あかい</td><td class="pj-res">akai</td><td class="pj-uz">qizil</td></tr>
  <tr><td>おおきい</td><td class="pj-res">ōkii</td><td class="pj-uz">katta</td></tr>
  <tr><td>せかい</td><td class="pj-res">sekai</td><td class="pj-uz">dunyo</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">あかい かさ</p>
  <p class="pe-ex__rom">akai kasa</p>
  <p class="pe-ex__uz">qizil soyabon</p>
  <p class="pe-ex__why">Beshta belgi — あ か い か さ — va ularning hammasini bugun oʻrgandingiz. Bitta ham notanish belgi yoʻq.</p>
</div>

<h3>5. Yozish — chiziqlar tartibi bejiz emas</h3>

<p>Har bir belgi belgilangan tartibda yoziladi: <b>yuqoridan pastga, chapdan oʻngga</b>.
Bu qoidaga amal qilsangiz, qoʻlyozmangiz oʻqiladigan boʻladi va keyinchalik kanji
yozish ancha oson kechadi.</p>

<div class="pj-stroke">
  <span class="pj-stroke__s" data-n="1">一</span>
  <span class="pj-stroke__s" data-n="2">十</span>
  <span class="pj-stroke__s" data-n="3">あ</span>
</div>

<p>あ uchta chiziqdan iborat: gorizontal chiziq, vertikal chiziq, keyin pastdagi
halqa. Uni bir zarbda chizishga urinmang.</p>

<div class="pe-call pe-warn">
  <p><b>Har kuni oʻn daqiqa qoʻlda yozing.</b> Faqat koʻz bilan oʻqib yodlagan
  odam belgilarni bir haftada unutadi; qoʻl bilan yozgan odam esa yodida saqlaydi.
  Bu kursdagi eng samarali oʻn daqiqa.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ し ni "si" deb oʻqish</p>
  <p class="pe-fix__good">✓ <b>[shi]</b>. Yapon tilida "si" tovushi umuman yoʻq. すし = "susi" emas, <b>sushi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ う ni lab choʻzib "u" deb aytish</p>
  <p class="pe-fix__good">✓ Lablar qimirlamaydi, ogʻiz yassi qoladi. Ingliz tilidagi "oo" ga oʻxshamaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ さ va き ni adashtirish</p>
  <p class="pe-fix__good">✓ <b>さ</b> da bitta gorizontal chiziq, <b>き</b> da ikkita. Chiziqlarni sanang — shu bilan farqlanadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <b>かき</b> qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>kaki</b> — xurmo mevasi. か = ka, き = ki.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. "sekai" ni hiraganada yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>せかい</b> — se + ka + i. Uchta boʻgʻin, uchta belgi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <b>し</b> nega "si" emas?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yapon tilida "si" tovushi mavjud emas. s + i birikmasi doim <b>[shi]</b> boʻlib chiqadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <b>いす</b> nima degani va qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>isu</b> — stul. Oxirgi す dagi u yengil aytiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Beshta unlini toʻgʻri tartibda ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>あ い う え お</b> — a, i, u, e, o. Bu tartib butun kurs davomida ishlatiladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>あさ</b> — ertalab</li>
  <li><b>いす</b> — stul</li>
  <li><b>すし</b> — sushi</li>
  <li><b>あき</b> — kuz</li>
  <li><b>かさ</b> — soyabon</li>
  <li><b>いけ</b> — hovuz</li>
  <li><b>すき</b> — yoqtirmoq, yoqadigan</li>
  <li><b>あかい</b> — qizil</li>
  <li><b>おおきい</b> — katta</li>
  <li><b>せかい</b> — dunyo</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Beshta unli — <b>あ い う え お</b> — butun tizimning poydevori, shu tartibda yodlanadi.</li>
    <li>Hiragana boʻgʻin yozuvi: <b>undosh + unli = bitta belgi</b>.</li>
    <li>Ikkita istisno: <b>し = [shi]</b>, va <b>す</b> dagi u jarangsiz undosh yonida eshitilmaydi (すき → [ski]).</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-3: Hiragana 2 — た ち つ て と · な に ぬ ね の · は ひ ふ へ ほ",
        "category": "japanese",
        "order": 3,
        "summary": (
            "Hiragananing keyingi 15 belgisi: t-, n- va h- qatorlari, hamda yaponchaning "
            "eng mashhur uchta tovush istisnosi — ち, つ va ふ."
        ),
        "content": """
<h2>PJ-3: Hiragana 2 — た ち つ て と · な に ぬ ね の · は ひ ふ へ ほ</h2>

<p>Oʻtgan darsda oʻn besh belgi oʻrgandingiz. Bugun yana oʻn beshta qoʻshiladi —
va shu bilan hiragananing uchdan ikki qismi tugaydi. Bu darsda yaponchaning eng
mashhur uchta tovush istisnosi ham bor: <b>ち</b>, <b>つ</b> va <b>ふ</b>. Ularni
bugun bir marta toʻgʻri oʻrgansangiz, keyinchalik hech qachon adashmaysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>た-, な- va は-qatorlarini toʻliq oʻqiysiz</li>
    <li>ち = chi, つ = tsu, ふ = fu ekanini biladigan boʻlasiz va sababini tushunasiz</li>
    <li>ぬ / ね / の va は / ほ juftliklarini shaklidan farqlaysiz</li>
    <li>Oʻttiz belgidan tuzilgan haqiqiy yaponcha soʻzlarni oʻqiysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bugungi uchta istisno</span>
  <span class="pe-chip pe-chip--neg">ち = chi</span>
  <span class="pe-chip pe-chip--neg">つ = tsu</span>
  <span class="pe-chip pe-chip--neg">ふ = fu</span>
</div>

<h3>1. た-qatori — ikkita istisno bir joyda</h3>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">た</span><span class="pj-kana__rom">ta</span>
    <span class="pj-kana__uz">た = t + a</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">ち</span><span class="pj-kana__rom">chi</span>
    <span class="pj-kana__uz">"ti" EMAS — "chi"</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">つ</span><span class="pj-kana__rom">tsu</span>
    <span class="pj-kana__uz">"tu" EMAS — "tsu"</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">て</span><span class="pj-kana__rom">te</span>
    <span class="pj-kana__uz">て = t + e</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">と</span><span class="pj-kana__rom">to</span>
    <span class="pj-kana__uz">と = t + o</span></div>
</div>

<p>Oʻtgan darsda <b>し = [shi]</b> ni koʻrgan edingiz. Endi shu hodisa yana ikki
marta takrorlanadi. Bu tasodif emas: yapon tilida <b>i</b> va <b>u</b> unlilaridan
oldingi til tovushlari <em>yumshaydi</em> va shakli oʻzgaradi.</p>

<div class="pj-say">
  <span class="pj-say__from">ち</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[chi]</span>
  <span class="pj-say__why">t + i yumshab "chi" boʻladi — "ti" tovushi yoʻq</span>
</div>

<div class="pj-say">
  <span class="pj-say__from">つ</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[tsu]</span>
  <span class="pj-say__why">t va s birga chiqadi — oʻzbekcha "s" dan oldin qisqa "t"</span>
</div>

<div class="pe-call pe-uz">
  <p><b>つ ni qanday chiqarish kerak.</b> Oʻzbek tilida bu tovush bor — faqat siz
  uni sezmaysiz. "otsa" deb ayting va oʻrtadagi <em>ts</em> ni ushlang. Aynan shu
  つ. Rus tilidagi <em>ц</em> ham xuddi shu tovush. Uni "tu" deb aytish — eng
  koʻp uchraydigan boshlovchi xatosi.</p>
</div>

<h3>2. な-qatori — shakli oʻxshash uchtalik</h3>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">な</span><span class="pj-kana__rom">na</span>
    <span class="pj-kana__uz">な = n + a</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">に</span><span class="pj-kana__rom">ni</span>
    <span class="pj-kana__uz">に = n + i</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">ぬ</span><span class="pj-kana__rom">nu</span>
    <span class="pj-kana__uz">halqasi <b>yopiq</b></span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">ね</span><span class="pj-kana__rom">ne</span>
    <span class="pj-kana__uz">halqasi <b>bitta</b>, oʻngda</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">の</span><span class="pj-kana__rom">no</span>
    <span class="pj-kana__uz">bitta silliq <b>halqa</b></span></div>
</div>

<p>な-qatorining tovushlari oson — hech qanday istisno yoʻq. Qiyinchilik
<em>shaklda</em>: <b>ぬ</b>, <b>ね</b> va <b>の</b> uchalasi ham halqa bilan
tugaydi va boshlovchilar ularni doim adashtiradi.</p>

<div class="pe-call pe-tip">
  <p><b>Farqlash usuli:</b> <b>の</b> — eng sodda, faqat bitta halqa, boshqa hech
  narsa yoʻq. <b>ね</b> da halqadan chapda tik chiziq bor. <b>ぬ</b> ね ga oʻxshaydi,
  lekin uning "dumi" halqani kesib oʻtadi. Qoida: <em>sodda = の, tik chiziqli =
  ね, kesib oʻtgan = ぬ</em>.</p>
</div>

<p><b>の</b> ni alohida eslab qoling — u shunchaki belgi emas, yapon tilidagi eng
koʻp uchraydigan grammatik qoʻshimchalardan biri. PJ-17 da unga butun bir dars
bagʻishlanadi.</p>

<h3>3. は-qatori va uchinchi istisno</h3>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">は</span><span class="pj-kana__rom">ha</span>
    <span class="pj-kana__uz">は = h + a</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">ひ</span><span class="pj-kana__rom">hi</span>
    <span class="pj-kana__uz">ひ = h + i</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">ふ</span><span class="pj-kana__rom">fu</span>
    <span class="pj-kana__uz">"hu" ham, "fu" ham emas</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">へ</span><span class="pj-kana__rom">he</span>
    <span class="pj-kana__uz">へ = h + e</span></div>
  <div class="pj-kana__c pj-kana__c--new">
    <span class="pj-kana__ch">ほ</span><span class="pj-kana__rom">ho</span>
    <span class="pj-kana__uz">ほ = h + o</span></div>
</div>

<p><b>ふ</b> — yaponchaning eng noaniq tovushi. Lotin yozuvida u <b>fu</b> deb
yoziladi, lekin ingliz tilidagi <em>f</em> emas: yuqori tishlar pastki labga
tegmaydi. Ikkala lab bir-biriga yaqin turadi va havo ular orasidan oʻtadi —
xuddi <b>shamdagi olovni puflagandek</b>.</p>

<div class="pj-say">
  <span class="pj-say__from">ふ</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[fu]</span>
  <span class="pj-say__why">tish labga tegmaydi — bu "h" va "f" orasidagi tovush</span>
</div>

<div class="pe-call pe-warn">
  <p><b>は ning ikkinchi hayoti.</b> Bu belgi grammatik qoʻshimcha sifatida
  ishlatilganda "ha" emas, <b>[wa]</b> deb oʻqiladi. Nega — buni PJ-14 da
  toʻliq koʻramiz. Hozircha shuni eslab qoling: <em>soʻz ichida は = ha, soʻzdan
  keyin yolgʻiz turgan は = wa</em>. Bu — butun kursdagi eng koʻp uchraydigan
  oʻqish xatosi.</p>
</div>

<h3>4. Oʻttiz belgi bilan oʻqiymiz</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yaponcha</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td>ちち</td><td class="pj-res">chichi</td><td class="pj-uz">ota (oʻz otasi)</td></tr>
  <tr><td>つき</td><td class="pj-res">tsuki</td><td class="pj-uz">oy</td></tr>
  <tr><td>てつ</td><td class="pj-res">tetsu</td><td class="pj-uz">temir</td></tr>
  <tr><td>なつ</td><td class="pj-res">natsu</td><td class="pj-uz">yoz</td></tr>
  <tr><td>ねこ</td><td class="pj-res">neko</td><td class="pj-uz">mushuk</td></tr>
  <tr><td>いぬ</td><td class="pj-res">inu</td><td class="pj-uz">it</td></tr>
  <tr><td>はな</td><td class="pj-res">hana</td><td class="pj-uz">gul</td></tr>
  <tr><td>ふね</td><td class="pj-res">fune</td><td class="pj-uz">kema</td></tr>
  <tr><td>ほし</td><td class="pj-res">hoshi</td><td class="pj-uz">yulduz</td></tr>
  <tr><td>ひと</td><td class="pj-res">hito</td><td class="pj-uz">odam</td></tr>
  <tr><td>ちかてつ</td><td class="pj-res">chikatetsu</td><td class="pj-uz">metro</td></tr>
  <tr><td>ひとつ</td><td class="pj-res">hitotsu</td><td class="pj-uz">bitta</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>ちかてつ</b> ni ajratib koʻring: <em>chika</em> (yer osti) + <em>tetsu</em>
  (temir) = "yer osti temiri" — metro. Yapon tilidagi soʻzlarning koʻpi shunday
  qurilgan: kichik boʻlaklardan yigʻilgan. Oʻzbekcha "temir yoʻl" ham xuddi shu
  mantiq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">なつの ほし</p>
  <p class="pe-ex__rom">natsu no hoshi</p>
  <p class="pe-ex__uz">yozning yulduzi</p>
  <p class="pe-ex__why">Oʻrtadagi <b>の</b> — oʻzbekchadagi <em>-ning</em>. Ikki otni bogʻlaydi va yapon tilidagi eng koʻp uchraydigan qoʻshimchalardan biri. PJ-17 da unga butun bir dars bagʻishlanadi.</p>
</div>

<h3>5. Shakli oʻxshash juftliklar</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">は — ha</p>
    <p class="pj-big">は</p>
    <p>Chap tomonda tik chiziq, oʻngda halqa <b>ochiq</b> qoladi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">ほ — ho</p>
    <p class="pj-big">ほ</p>
    <p>は bilan bir xil, faqat tepada <b>qoʻshimcha gorizontal chiziq</b> bor.</p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>ほ = は + bitta chiziq.</b> Shu bilan farqlanadi. Xuddi shunday
  <b>い</b> (i) va <b>り</b> (ri) ham oʻxshash — り ni keyingi darsda koʻramiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ つ ni "tu" deb oʻqish</p>
  <p class="pe-fix__good">✓ <b>[tsu]</b>. "otsa" soʻzining oʻrtasidagi tovush. なつ = "natu" emas, <b>natsu</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ち ni "ti" deb oʻqish</p>
  <p class="pe-fix__good">✓ <b>[chi]</b>. ちち = "titi" emas, <b>chichi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ふ ni ingliz tilidagi "f" kabi, tishni labga tegizib aytish</p>
  <p class="pe-fix__good">✓ Tish labga tegmaydi. Ikki lab orasidan havo puflanadi — shamni oʻchirgandek.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <b>なつ</b> qanday oʻqiladi va nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>natsu</b> — yoz. つ = tsu, "tu" emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <b>ぬ</b>, <b>ね</b>, <b>の</b> ni qanday farqlaysiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>の</b> — faqat bitta halqa, boshqa hech narsa yoʻq. <b>ね</b> — halqa + chapda tik chiziq. <b>ぬ</b> — ね ga oʻxshaydi, lekin dumi halqani kesib oʻtadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. "hoshi" ni hiraganada yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ほし</b> — yulduz. ほ + し (shi).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <b>ほ</b> va <b>は</b> ning yozilishida qanday farq bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ほ</b> = は + tepada qoʻshimcha gorizontal chiziq. Boshqa hammasi bir xil.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <b>ちかてつ</b> — bu nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>chikatetsu</b> — metro. <em>chika</em> (yer osti) + <em>tetsu</em> (temir).</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>つき</b> — oy</li>
  <li><b>なつ</b> — yoz</li>
  <li><b>ねこ</b> — mushuk</li>
  <li><b>いぬ</b> — it</li>
  <li><b>はな</b> — gul</li>
  <li><b>ふね</b> — kema</li>
  <li><b>ほし</b> — yulduz</li>
  <li><b>ひと</b> — odam</li>
  <li><b>ちかてつ</b> — metro (yer osti temiri)</li>
  <li><b>ひとつ</b> — bitta</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Uchta istisno: <b>ち = chi</b>, <b>つ = tsu</b>, <b>ふ = fu</b>. Sababi bitta — i va u oldidan tovush yumshaydi.</li>
    <li>Shakli oʻxshaganlar: <b>ぬ / ね / の</b> va <b>は / ほ</b>. Halqa va chiziqlarni sanang.</li>
    <li><b>は</b> qoʻshimcha boʻlib kelganda <b>[wa]</b> oʻqiladi — bu haqda PJ-14 da.</li>
  </ul>
</div>
""",
    },
]
