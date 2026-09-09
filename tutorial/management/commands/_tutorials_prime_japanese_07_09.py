# -*- coding: utf-8 -*-
"""Prime Japanese — Block A, darslar 7–9 (katakana).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_JAPANESE.md
Lesson list: tutorial/management/commands/toc_prime_japanese.txt

Block A darslarida grammatika yoʻq, shuning uchun oʻqish matni ham yoʻq.
Har bir darsning ikkinchi boʻlagi — 12 savollik mashq:
practice/management/commands/_practice_pj_07_09.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_07_09.py --author=prime
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
        "title": "PJ-7: Katakana 1 — ア-ソ va nega ismingiz katakana bilan yoziladi",
        "category": "japanese",
        "order": 7,
        "summary": (
            "Katakananing birinchi 15 belgisi. Ikkinchi alifbo nega kerakligi, uning "
            "burchakli shakli qayerdan kelgani va nima uchun sizning ismingiz shu yozuvda."
        ),
        "content": """
<h2>PJ-7: Katakana 1 — ア-ソ va nega ismingiz katakana bilan yoziladi</h2>

<p>Yomon xabar: yana 46 ta belgi. Yaxshi xabar: <b>ularning tovushlari sizga
allaqachon tanish</b>. Katakana yangi til emas, yangi tovush ham emas — u siz
bilgan oʻsha 46 boʻgʻinning ikkinchi kiyimi. ア = あ = "a". Xolos. Shuning uchun
bu blok hiragana blokidan ancha tez oʻtadi: siz faqat shakllarni oʻrganasiz,
tizimni emas.</p>

<p>Lekin bitta savol qoladi, va u muhim: <em>nega umuman ikkinchi alifbo kerak?</em>
Bugun shu savolga javob beramiz — va javob sizning oʻz ismingizga ham tegishli.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Katakananing birinchi 15 belgisini oʻqiysiz: ア-ソ</li>
    <li>Ikkita alifbo nega bir vaqtda yashashini tushunasiz</li>
    <li>Katakananing burchakli shakli qayerdan kelganini bilib olasiz</li>
    <li>Nega chet el ismlari — shu jumladan sizniki ham — katakanada yozilishini bilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikkita alifbo, bitta tovush</span>
  <span class="pe-chip pe-chip--s">あ hiragana</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">ア katakana</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">[a]</span>
</div>

<h3>1. Nega ikkita alifbo? — vazifa boʻlinishi</h3>

<p>PJ-1 da qisqacha koʻrgan edingiz: hiragana grammatika uchun, katakana chetdan
kelgan narsalar uchun. Endi buni chuqurroq koʻramiz, chunki bu bilim sizga har
kuni kerak boʻladi.</p>

<p>Yaponcha matnda <b>katakana koʻzga tashlanadi</b>. Uning burchakli, keskin
shakli yumaloq hiragana orasida darrov ajralib turadi. Bu — tasodif emas,
bu uning <em>ishi</em>: katakana oʻquvchiga "diqqat, bu soʻz bu yerga chetdan
kelgan" deb signal beradi.</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Chet soʻzlar</p>
    <p>Boshqa tildan olingan har qanday soʻz. Bugungi yapon tilida ular juda koʻp.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Chet el ismlari</p>
    <p>Odam ismlari, mamlakat va shahar nomlari — Yaponiyadan tashqaridagi hammasi.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Tovush taqlidi</p>
    <p>Hayvon ovozi, shovqin, holat taqlidi. Manga sahifalari shulardan iborat.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham shunga oʻxshash narsa bor.</b> Biz chet soʻzni yozganda
  koʻpincha uni <em>qiya harf</em> bilan ajratamiz yoki qoʻshtirnoqqa olamiz —
  "bu soʻz oʻzimizniki emas" degan signal. Yapon tilida bu ish uchun butun bir
  alifbo ajratilgan. Signal kuchliroq, chunki koʻz uni bir zumda ilgʻaydi.</p>
</div>

<h3>2. Shakl qayerdan kelgan — ikkita alifboning tarixi</h3>

<p>Ikkala alifbo ham <b>kanjidan</b> tugʻilgan, lekin butunlay boshqa yoʻl bilan —
va shakllaridagi farq aynan shundan.</p>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">HIRAGANA — yumaloq</p>
    <p class="pj-pair__form">安 → あ</p>
    <p>Kanjini tez, uzluksiz qoʻlyozmada yozishdan kelib chiqqan. Butun belgi siqilib,
    silliq shaklga aylangan — shuning uchun u <b>oqadi</b>.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">KATAKANA — burchakli</p>
    <p class="pj-pair__form">阿 → ア</p>
    <p>Rohiblar matn chetiga qisqa izoh yozish uchun kanjining <b>bir boʻlagini</b>
    olgan. Boʻlak — demak keskin chiziqlar, kam zarba.</p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>Buni bilish amaliy foyda beradi:</b> katakana belgilari <em>kam
  chiziqli</em> va <em>tik burchakli</em> boʻladi, chunki ular kanji parchasi.
  Hiragana esa doim egri va oqib turadi. Notanish belgi koʻrsangiz, shakliga
  qarab qaysi alifbo ekanini aytib bera olasiz.</p>
</div>

<h3>3. Birinchi 15 belgi</h3>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ア</span><span class="pj-kana__rom">a</span>
    <span class="pj-kana__uz">= あ</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">イ</span><span class="pj-kana__rom">i</span>
    <span class="pj-kana__uz">= い</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ウ</span><span class="pj-kana__rom">u</span>
    <span class="pj-kana__uz">= う, shakli oʻxshash</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">エ</span><span class="pj-kana__rom">e</span>
    <span class="pj-kana__uz">= え</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">オ</span><span class="pj-kana__rom">o</span>
    <span class="pj-kana__uz">= お, shakli oʻxshash</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">カ</span><span class="pj-kana__rom">ka</span>
    <span class="pj-kana__uz">= か, deyarli bir xil</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">キ</span><span class="pj-kana__rom">ki</span>
    <span class="pj-kana__uz">= き, deyarli bir xil</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ク</span><span class="pj-kana__rom">ku</span>
    <span class="pj-kana__uz">ikki chiziq, oʻtkir burchak</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ケ</span><span class="pj-kana__rom">ke</span>
    <span class="pj-kana__uz">uchta chiziq</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">コ</span><span class="pj-kana__rom">ko</span>
    <span class="pj-kana__uz">ikki chiziq, burchak</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">サ</span><span class="pj-kana__rom">sa</span>
    <span class="pj-kana__uz">= さ ning yuqori qismi</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">シ</span><span class="pj-kana__rom">shi</span>
    <span class="pj-kana__uz">chiziqlar <b>pastdan</b> yuqoriga</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ス</span><span class="pj-kana__rom">su</span>
    <span class="pj-kana__uz">burchak, keyin dum</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">セ</span><span class="pj-kana__rom">se</span>
    <span class="pj-kana__uz">= せ, deyarli bir xil</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ソ</span><span class="pj-kana__rom">so</span>
    <span class="pj-kana__uz">chiziqlar <b>tepadan</b> pastga</span></div>
</div>

<div class="pe-call pe-tip">
  <p><b>Uchdan bir qismi tekin keladi.</b> Katakananing baʼzi belgilari oʻz
  hiragana juftiga juda oʻxshaydi, chunki ikkalasi bitta kanjidan chiqqan:
  <b>カ</b>~か, <b>キ</b>~き, <b>セ</b>~せ, <b>ウ</b>~う, <b>オ</b>~お.
  Ularni alohida yodlash shart emas — shunchaki "bu oʻshaning tik varianti"
  deb qarang.</p>
</div>

<h3>4. Oʻqiymiz — bu soʻzlarni allaqachon bilasiz</h3>

<p>Katakana chet soʻzlar uchun boʻlgani sababli, siz oʻqigan birinchi
katakana soʻzlari <b>tanish</b> chiqadi:</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Katakana</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td>ココア</td><td class="pj-res">kokoa</td><td class="pj-uz">kakao ichimligi</td></tr>
  <tr><td>カカオ</td><td class="pj-res">kakao</td><td class="pj-uz">kakao (doni)</td></tr>
  <tr><td>アイス</td><td class="pj-res">aisu</td><td class="pj-uz">muzqaymoq</td></tr>
  <tr><td>オアシス</td><td class="pj-res">oashisu</td><td class="pj-uz">voha</td></tr>
  <tr><td>キス</td><td class="pj-res">kisu</td><td class="pj-uz">oʻpich</td></tr>
  <tr><td>スイス</td><td class="pj-res">suisu</td><td class="pj-uz">Shveytsariya</td></tr>
  <tr><td>イエス</td><td class="pj-res">iesu</td><td class="pj-uz">ha (chet soʻz)</td></tr>
  <tr><td>カオス</td><td class="pj-res">kaosu</td><td class="pj-uz">tartibsizlik</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">オアシス</p>
  <p class="pe-ex__rom">oashisu</p>
  <p class="pe-ex__uz">voha</p>
  <p class="pe-ex__why">Toʻrtta belgi, toʻrtta zarb. Diqqat qiling: soʻz oxiridagi <b>ス</b> — asl soʻzda yolgʻiz "s" edi, lekin yaponchada yolgʻiz undosh boʻlmaydi, shuning uchun unga "u" qoʻshilgan.</p>
</div>

<h3>5. Nega ismingiz katakanada yoziladi</h3>

<p>Endi darsning asosiy savoliga keldik. Javob ikki qismdan iborat.</p>

<p><b>Birinchisi — qoida.</b> Yaponiyadan tashqarida tugʻilgan har qanday ism
katakanada yoziladi. Bu hurmatsizlik emas, aksincha: bu oʻquvchiga "bu ism
yaponcha emas, uni yaponcha kanji qoidalari bilan oʻqishga urinmang" deb
aytadi.</p>

<p><b>Ikkinchisi — tovush.</b> Ismingiz yapon tilining tovush tizimiga
<em>moslashtiriladi</em>. Yapon tilida yolgʻiz undosh yoʻq (faqat ん dan
tashqari), shuning uchun har bir undoshga unli qoʻshiladi.</p>

<div class="pj-say">
  <span class="pj-say__from">"s" yolgʻiz</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">ス [su]</span>
  <span class="pj-say__why">yaponchada undosh yolgʻiz qola olmaydi</span>
</div>

<div class="pe-call pe-warn">
  <p><b>Shuning uchun ismingiz biroz uzunroq eshitiladi.</b> Bu buzilish emas —
  har bir til chet soʻzni oʻz tovushlariga moslashtiradi. Oʻzbekchada ham biz
  "Tokyo" ni "Tokio" deb aytamiz. Ismingizni toʻliq katakanada yozishni
  <b>PJ-9</b> da oʻrganamiz — u yerda uzun unlilar va chet tovushlar uchun
  maxsus birikmalar keladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ "Katakana boshqa tovushlarni bildiradi"</p>
  <p class="pe-fix__good">✓ Tovushlar <b>bir xil</b>. ア = あ = [a]. Faqat shakl va vazifa boshqa.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Katakanani keyinroq oʻrganish</p>
  <p class="pe-fix__good">✓ Menyu, doʻkon, reklama va texnika soʻzlarining katta qismi katakanada. Yaponiyada katakana koʻpincha hiraganadan koʻra tez-tez oʻqiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ク va ケ ni bir xil deb qarash</p>
  <p class="pe-fix__good">✓ <b>ク</b> ikki chiziqdan iborat va oʻtkir burchak yasaydi. <b>ケ</b> da uchinchi, tik chiziq bor. Chiziqlarni sanang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <b>ア</b> va <b>あ</b> orasida qanday farq bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Tovushida <b>hech qanday farq yoʻq</b> — ikkalasi ham [a]. Farq shaklda va vazifada: ア katakana, chet soʻzlar uchun; あ hiragana, grammatika uchun.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <b>アイス</b> qanday oʻqiladi va nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>aisu</b> — muzqaymoq. Chet soʻz, shuning uchun katakanada.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Nega katakana burchakli, hiragana esa yumaloq?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Katakana kanjining <b>bir boʻlagi</b>dan olingan — boʻlak keskin chiziqlar beradi. Hiragana esa butun kanjini tez qoʻlyozmada yozishdan chiqqan, shuning uchun u oqadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Nega chet el ismlari katakanada yoziladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Bu oʻquvchiga <b>signal</b> beradi: bu soʻz yaponcha emas. Shu bilan uni yaponcha kanji qoidalari bilan oʻqishga urinish kerak emasligi darrov maʼlum boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega <b>オアシス</b> oxirida <b>ス</b> turadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yapon tilida <b>yolgʻiz undosh boʻlmaydi</b> (ん dan tashqari). Asl soʻzdagi yolgʻiz "s" ga "u" qoʻshilib, ス boʻlgan.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ココア</b> — kakao ichimligi</li>
  <li><b>カカオ</b> — kakao doni</li>
  <li><b>アイス</b> — muzqaymoq</li>
  <li><b>オアシス</b> — voha</li>
  <li><b>キス</b> — oʻpich</li>
  <li><b>スイス</b> — Shveytsariya</li>
  <li><b>イエス</b> — ha</li>
  <li><b>カオス</b> — tartibsizlik</li>
  <li><b>アクセス</b> — kirish, ruxsat</li>
  <li><b>キオスク</b> — kiosk</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Katakana <b>yangi tovush bermaydi</b> — u siz bilgan 46 boʻgʻinning ikkinchi kiyimi.</li>
    <li>Shakli burchakli, chunki u kanjining <b>bir boʻlagi</b>dan olingan.</li>
    <li>Chet el ismlari katakanada yoziladi va yapon tovush tizimiga moslashtiriladi: yolgʻiz undoshga unli qoʻshiladi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-8: Katakana 2 — タ-ン va chalgʻituvchi juftliklar (シ/ツ, ソ/ン, ク/ワ)",
        "category": "japanese",
        "order": 8,
        "summary": (
            "Katakananing qolgan 31 belgisi va toʻrtta mashhur chalgʻituvchi juftlik. "
            "Ularni chiziq yoʻnalishi bilan bir umrga ajratasiz."
        ),
        "content": """
<h2>PJ-8: Katakana 2 — タ-ン va chalgʻituvchi juftliklar (シ/ツ, ソ/ン, ク/ワ)</h2>

<p>Bugun katakana tugaydi — qolgan 31 belgi bir darsda. Bu koʻp koʻrinadi, lekin
esingizda boʻlsin: <b>tovushlarni allaqachon bilasiz</b>. タ = た = "ta". Siz
faqat yangi shaklni yodlaysiz, yangi tizimni emas.</p>

<p>Asosiy ish esa boshqa joyda. Katakanada <b>bir-biriga juda oʻxshash toʻrtta
juftlik</b> bor va aynan ular yaponcha oʻqiyotgan har bir chet ellikni yillar
davomida qiynaydi. Bugun ularni <em>bir umrga</em> hal qiladigan bitta qoida
oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Katakananing qolgan 31 belgisini oʻqiysiz</li>
    <li>シ/ツ va ソ/ン juftliklarini <b>chiziq yoʻnalishi</b> bilan ajratasiz</li>
    <li>ク/ワ va ス/ヌ juftliklarini shaklidan farqlaysiz</li>
    <li>Dakuten va handakuten katakanada ham xuddi shunday ishlashini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bir umrlik qoida</span>
  <span class="pe-chip pe-chip--s">Hiragana qayoqqa yozilsa</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">katakana ham oʻsha yoqqa</span>
</div>

<h3>1. Qolgan belgilar</h3>

<div class="pj-kana">
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">タ</span><span class="pj-kana__rom">ta</span>
    <span class="pj-kana__uz">= た</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">チ</span><span class="pj-kana__rom">chi</span>
    <span class="pj-kana__uz">= ち</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ツ</span><span class="pj-kana__rom">tsu</span>
    <span class="pj-kana__uz">= つ</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">テ</span><span class="pj-kana__rom">te</span>
    <span class="pj-kana__uz">= て</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ト</span><span class="pj-kana__rom">to</span>
    <span class="pj-kana__uz">ikki chiziq, eng sodda</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ナ</span><span class="pj-kana__rom">na</span>
    <span class="pj-kana__uz">= な ning yuqori qismi</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ニ</span><span class="pj-kana__rom">ni</span>
    <span class="pj-kana__uz">= に, ikki chiziq</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ヌ</span><span class="pj-kana__rom">nu</span>
    <span class="pj-kana__uz">ス ga oʻxshaydi</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ネ</span><span class="pj-kana__rom">ne</span>
    <span class="pj-kana__uz">murakkabroq shakl</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ノ</span><span class="pj-kana__rom">no</span>
    <span class="pj-kana__uz">bitta chiziq — eng oddiy</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ハ</span><span class="pj-kana__rom">ha</span>
    <span class="pj-kana__uz">ikki chiziq, ochiq</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ヒ</span><span class="pj-kana__rom">hi</span>
    <span class="pj-kana__uz">= ひ</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">フ</span><span class="pj-kana__rom">fu</span>
    <span class="pj-kana__uz">bitta burchak</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ヘ</span><span class="pj-kana__rom">he</span>
    <span class="pj-kana__uz">= へ, <b>aynan bir xil</b></span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ホ</span><span class="pj-kana__rom">ho</span>
    <span class="pj-kana__uz">= ほ ga yaqin</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">マ</span><span class="pj-kana__rom">ma</span>
    <span class="pj-kana__uz">burchak va chiziq</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ミ</span><span class="pj-kana__rom">mi</span>
    <span class="pj-kana__uz">uchta chiziq</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ム</span><span class="pj-kana__rom">mu</span>
    <span class="pj-kana__uz">マ ga oʻxshaydi</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">メ</span><span class="pj-kana__rom">me</span>
    <span class="pj-kana__uz">kesishgan ikki chiziq</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">モ</span><span class="pj-kana__rom">mo</span>
    <span class="pj-kana__uz">= も</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ヤ</span><span class="pj-kana__rom">ya</span>
    <span class="pj-kana__uz">= や</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ユ</span><span class="pj-kana__rom">yu</span>
    <span class="pj-kana__uz">= ゆ ning soddalashgani</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ヨ</span><span class="pj-kana__rom">yo</span>
    <span class="pj-kana__uz">uchta gorizontal chiziq</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ラ</span><span class="pj-kana__rom">ra</span>
    <span class="pj-kana__uz">titratilmaydi</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">リ</span><span class="pj-kana__rom">ri</span>
    <span class="pj-kana__uz">= り</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ル</span><span class="pj-kana__rom">ru</span>
    <span class="pj-kana__uz">ikki chiziq, dumli</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">レ</span><span class="pj-kana__rom">re</span>
    <span class="pj-kana__uz">bitta burilish</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ロ</span><span class="pj-kana__rom">ro</span>
    <span class="pj-kana__uz">toʻrtburchak</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ワ</span><span class="pj-kana__rom">wa</span>
    <span class="pj-kana__uz">ク ga oʻxshaydi</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ヲ</span><span class="pj-kana__rom">o</span>
    <span class="pj-kana__uz">deyarli ishlatilmaydi</span></div>
  <div class="pj-kana__c pj-kana__c--kata pj-kana__c--new">
    <span class="pj-kana__ch">ン</span><span class="pj-kana__rom">n</span>
    <span class="pj-kana__uz">= ん</span></div>
</div>

<div class="pe-call pe-tip">
  <p><b>ヘ ni tekinga olasiz.</b> Hiragana <b>へ</b> va katakana <b>ヘ</b> —
  <em>aynan bir xil</em> shakl. Yaponcha yozuvdagi yagona shunday juftlik.
  Qaysi biri ekanini atrofdagi belgilardan bilib olasiz.</p>
  <p><b>ヲ</b> haqida ham xavotir olmang: u faqat hiragana を ning juftligi
  sifatida jadvalda turadi. Zamonaviy matnda deyarli uchramaydi, chunki
  grammatik qoʻshimchalar doim hiraganada yoziladi.</p>
</div>

<h3>2. Chalgʻituvchi juftliklar — bitta qoida hammasini hal qiladi</h3>

<p>Mana darsning eng qimmatli qismi. <b>シ / ツ</b> va <b>ソ / ン</b> — koʻzga
deyarli bir xil koʻrinadi. Koʻpchilik ularni yodlashga urinadi va adashaveradi.
Lekin yodlash kerak emas: qoida bor, va u <em>hiragana</em> dan kelib chiqadi.</p>

<div class="pe-call pe-rule">
  <p><b>Qoida:</b> katakana belgisi oʻzi kelib chiqqan hiragana <b>qaysi yoʻnalishda
  yozilsa, oʻsha yoʻnalishni saqlaydi</b>. Yaʼni:</p>
  <ul>
    <li><b>し</b> pastdan yuqoriga sweep qiladi → <b>シ</b> chiziqlari ham <b>pastdan</b> yuqoriga</li>
    <li><b>つ</b> chapdan oʻngga, tepadan → <b>ツ</b> chiziqlari <b>tepadan</b> pastga</li>
    <li><b>ん</b> pastdan yuqoriga → <b>ン</b> ham <b>pastdan</b> yuqoriga</li>
    <li><b>そ</b> tepadan pastga → <b>ソ</b> ham <b>tepadan</b> pastga</li>
  </ul>
</div>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">シ — shi (し dan)</p>
    <p class="pj-pair__form">シ</p>
    <p>Ikki kichik chiziq <b>chap yon</b>da, deyarli yotiq. Uzun chiziq
    <b>pastdan yuqoriga</b> koʻtariladi.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">ツ — tsu (つ dan)</p>
    <p class="pj-pair__form">ツ</p>
    <p>Ikki kichik chiziq <b>tepa</b>da, deyarli tik. Uzun chiziq
    <b>tepadan pastga</b> tushadi.</p>
  </div>
</div>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">ン — n (ん dan)</p>
    <p class="pj-pair__form">ン</p>
    <p>Kichik chiziq <b>tepa</b>da. Uzun chiziq <b>pastdan yuqoriga</b> —
    xuddi シ kabi.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">ソ — so (そ dan)</p>
    <p class="pj-pair__form">ソ</p>
    <p>Kichik chiziq <b>tepa</b>da. Uzun chiziq <b>tepadan pastga</b> —
    xuddi ツ kabi.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Amaliy usul.</b> Chop etilgan matnda chiziqning yoʻnalishini koʻrmaysiz —
  faqat natijani koʻrasiz. Shuning uchun <b>burchakka</b> qarang: シ va ン da
  kichik chiziqlar deyarli <em>yotiq</em>, ツ va ソ da esa deyarli <em>tik</em>.
  Va eng ishonchli yoʻl — <b>oʻzingiz qoʻlda yozib koʻrish</b>. Bir necha marta
  toʻgʻri yoʻnalishda yozsangiz, qoʻl eslab qoladi va koʻz ham keyin ajratadigan
  boʻladi.</p>
</div>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">ク — ku</p>
    <p class="pj-pair__form">ク</p>
    <p>Tor va <b>oʻtkir</b> burchak. Ikkinchi chiziq pastga qiya ketadi.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">ワ — wa</p>
    <p class="pj-pair__form">ワ</p>
    <p>Keng va <b>yumshoq</b> burchak, deyarli toʻrtburchak. Pastki qismi
    kengroq.</p>
  </div>
</div>

<p>Toʻrtinchi juftlik — <b>ス</b> va <b>ヌ</b>. Farqi: <b>ヌ</b> da chapdan
oʻngga kesib oʻtadigan qoʻshimcha chiziq bor, <b>ス</b> da esa yoʻq.</p>

<h3>3. Dakuten va handakuten — hech narsa oʻzgarmaydi</h3>

<p>Yaxshi xabar: PJ-6 da oʻrgangan hamma narsa katakanada <b>aynan shunday</b>
ishlaydi. Ikkita tirnoq jaranglashtiradi, doiracha p beradi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Sof</th><th>+ ゛</th><th>+ ゜</th><th>Misol</th></tr>
  <tr><td class="pj-stem">カ ka</td><td class="pj-end">ガ ga</td><td>—</td><td class="pj-uz">ガス — gaz</td></tr>
  <tr><td class="pj-stem">サ sa</td><td class="pj-end">ザ za</td><td>—</td><td class="pj-uz">ピザ — pitsa</td></tr>
  <tr><td class="pj-stem">タ ta</td><td class="pj-end">ダ da</td><td>—</td><td class="pj-uz">サラダ — salat</td></tr>
  <tr><td class="pj-stem">ハ ha</td><td class="pj-end">バ ba</td><td class="pj-res">パ pa</td><td class="pj-uz">パン — non</td></tr>
</table></div>

<h3>4. Oʻqiymiz — endi butun dunyo ochiladi</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Katakana</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td>パン</td><td class="pj-res">pan</td><td class="pj-uz">non</td></tr>
  <tr><td>ペン</td><td class="pj-res">pen</td><td class="pj-uz">ruchka</td></tr>
  <tr><td>テレビ</td><td class="pj-res">terebi</td><td class="pj-uz">televizor</td></tr>
  <tr><td>ホテル</td><td class="pj-res">hoteru</td><td class="pj-uz">mehmonxona</td></tr>
  <tr><td>トマト</td><td class="pj-res">tomato</td><td class="pj-uz">pomidor</td></tr>
  <tr><td>ラジオ</td><td class="pj-res">rajio</td><td class="pj-uz">radio</td></tr>
  <tr><td>バナナ</td><td class="pj-res">banana</td><td class="pj-uz">banan</td></tr>
  <tr><td>ミルク</td><td class="pj-res">miruku</td><td class="pj-uz">sut</td></tr>
  <tr><td>テニス</td><td class="pj-res">tenisu</td><td class="pj-uz">tennis</td></tr>
  <tr><td>ピアノ</td><td class="pj-res">piano</td><td class="pj-uz">pianino</td></tr>
  <tr><td>メロン</td><td class="pj-res">meron</td><td class="pj-uz">qovun</td></tr>
  <tr><td>ワイン</td><td class="pj-res">wain</td><td class="pj-uz">vino</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">ミルク</p>
  <p class="pe-ex__rom">miruku</p>
  <p class="pe-ex__uz">sut</p>
  <p class="pe-ex__why">Asl soʻzda "l" bor, lekin yapon tilida <b>l tovushi yoʻq</b> — u doim ラ-qatoriga aylanadi. Shuning uchun "mi-ru-ku": uchta zarb.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">ホテル</p>
  <p class="pe-ex__rom">hoteru</p>
  <p class="pe-ex__uz">mehmonxona</p>
  <p class="pe-ex__why">Yana oʻsha ikki qoida: "l" → ル, va soʻz oxiridagi yolgʻiz undoshga unli qoʻshiladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">トマト</p>
  <p class="pe-ex__rom">tomato</p>
  <p class="pe-ex__uz">pomidor</p>
  <p class="pe-ex__why">Uchta belgi, uchta zarb. Diqqat: birinchi va uchinchi belgi <b>bir xil</b> — ト. Katakana soʻzlarida bunday takror koʻp uchraydi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ シ va ツ ni yodlashga urinish</p>
  <p class="pe-fix__good">✓ Yodlamang — <b>yoʻnalishga</b> qarang. シ da kichik chiziqlar yotiq va uzun chiziq pastdan koʻtariladi; ツ da tik va tepadan tushadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ミルク ni "milk" kabi ikki zarbda aytish</p>
  <p class="pe-fix__good">✓ <b>mi-ru-ku</b>, uch zarb. Yapon tilida l yoʻq va yolgʻiz undosh boʻlmaydi, shuning uchun soʻz uzayadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ヘ ni koʻrib "bu hiraganami yoki katakanami?" deb toʻxtab qolish</p>
  <p class="pe-fix__good">✓ Ikkalasi <b>aynan bir xil</b> yoziladi va bir xil oʻqiladi — [he]. Qaysi alifbo ekani atrofdagi belgilardan maʼlum boʻladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <b>シ</b> va <b>ツ</b> ni qanday ajratasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Chiziq yoʻnalishi.</b> シ (し dan) — kichik chiziqlar chap yonda, deyarli yotiq; uzun chiziq pastdan yuqoriga. ツ (つ dan) — kichik chiziqlar tepada, deyarli tik; uzun chiziq tepadan pastga.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <b>テレビ</b> qanday oʻqiladi va nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>terebi</b> — televizor. ビ = ヒ + dakuten.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Nega <b>ミルク</b> uch zarbdan iborat?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yapon tilida <b>l tovushi yoʻq</b> (u ラ-qatoriga aylanadi) va <b>yolgʻiz undosh boʻlmaydi</b> (unga unli qoʻshiladi). Shuning uchun mi-ru-ku.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Katakana <b>ヘ</b> va hiragana <b>へ</b> orasida qanday farq bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Hech qanday farq yoʻq</b> — shakli ham, oʻqilishi ham bir xil. Bu yaponcha yozuvdagi yagona shunday juftlik.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega <b>ヲ</b> zamonaviy matnda deyarli uchramaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki u faqat grammatik qoʻshimcha tovushini bildiradi, grammatik qoʻshimchalar esa <b>doim hiraganada</b> (を) yoziladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>パン</b> — non</li>
  <li><b>ペン</b> — ruchka</li>
  <li><b>テレビ</b> — televizor</li>
  <li><b>ホテル</b> — mehmonxona</li>
  <li><b>トマト</b> — pomidor</li>
  <li><b>ミルク</b> — sut</li>
  <li><b>テニス</b> — tennis</li>
  <li><b>ピアノ</b> — pianino</li>
  <li><b>メロン</b> — qovun</li>
  <li><b>ワイン</b> — vino</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Chalgʻituvchi juftliklarni <b>chiziq yoʻnalishi</b> ajratadi — u kelib chiqqan hiraganadan meros.</li>
    <li>Dakuten va handakuten katakanada <b>aynan shunday</b> ishlaydi.</li>
    <li>Chet soʻz yaponchaga oʻtganda uzayadi: <b>l → ラ-qatori</b>, yolgʻiz undoshga <b>unli qoʻshiladi</b>.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-9: Uzun unlilar ー, chet soʻzlar va katakana bilan yozilgan dunyo",
        "category": "japanese",
        "order": 9,
        "summary": (
            "Katakananing oxirgi vositalari: uzun chiziq ー, kichik unlilar va chet "
            "tovushlar uchun birikmalar. Dars oxirida oʻz ismingizni yozasiz."
        ),
        "content": """
<h2>PJ-9: Uzun unlilar ー, chet soʻzlar va katakana bilan yozilgan dunyo</h2>

<p>46 ta katakana belgisini bilasiz. Lekin haqiqiy matnga qarasangiz, hali ham
notanish narsalar bor: uzun tik chiziq <b>ー</b>, kichraytirilgan unlilar
<b>ァ ィ ゥ ェ ォ</b>, va <b>ファ</b> yoki <b>ティ</b> kabi birikmalar. Bularning
hammasi bitta muammoni hal qiladi: <em>yapon tilida yoʻq tovushni qanday
yozish kerak?</em></p>

<p>Bugun shuni oʻrganamiz — va darsning oxirida <b>oʻz ismingizni katakanada
yozasiz</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uzun unlilarni ー chizigʻi bilan yozasiz</li>
    <li>Chet soʻz yaponchaga oʻtganda unga nima boʻlishini bilasiz</li>
    <li>ファ, ティ, ヴ kabi yangi birikmalarni oʻqiysiz</li>
    <li>Oʻz ismingizni va Oʻzbekiston shaharlarini katakanada yozasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Chet soʻz yaponchaga oʻtganda</span>
  <span class="pe-chip pe-chip--s">har undoshga unli</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">l → ラ-qatori</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">uzunlik → ー</span>
</div>

<h3>1. ー — uzun unlining katakana usuli</h3>

<p>Hiraganada uzunlikni yana bitta unli qoʻshib koʻrsatgan edingiz: おかあさん,
おはよう. Katakanada bu ish <b>ancha soddaroq</b>: shunchaki tik chiziq
qoʻyiladi.</p>

<div class="pj-say">
  <span class="pj-say__from">コーヒー</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[kōhī]</span>
  <span class="pj-say__why">ikkita ー, ikkita uzun unli — kofe</span>
</div>

<div class="pe-call pe-rule">
  <p><b>Qoida:</b> ー oldingi unlini <b>ikki barobar</b> uzaytiradi va oʻzi
  <b>toʻliq bitta zarb</b> sanaladi. コーヒー — toʻrtta belgi, <b>toʻrtta</b>
  zarb: ko · o · hi · i. Vertikal yozilgan matnda bu chiziq tik emas,
  yotiq boʻlib chiqadi — lekin vazifasi oʻsha.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Katakana</th><th>Oʻqilishi</th><th>Zarblar</th><th>Maʼnosi</th></tr>
  <tr><td>コーヒー</td><td class="pj-res">kōhī</td><td>4</td><td class="pj-uz">kofe</td></tr>
  <tr><td>ケーキ</td><td class="pj-res">kēki</td><td>3</td><td class="pj-uz">tort</td></tr>
  <tr><td>ノート</td><td class="pj-res">nōto</td><td>3</td><td class="pj-uz">daftar</td></tr>
  <tr><td>スーパー</td><td class="pj-res">sūpā</td><td>4</td><td class="pj-uz">doʻkon</td></tr>
  <tr><td>テーブル</td><td class="pj-res">tēburu</td><td>4</td><td class="pj-uz">stol</td></tr>
  <tr><td>カード</td><td class="pj-res">kādo</td><td>3</td><td class="pj-uz">karta</td></tr>
</table></div>

<h3>2. Chet soʻzga nima boʻladi — uchta qoida</h3>

<p>Yapon tilining tovush tizimi juda tor: 46 boʻgʻin, yolgʻiz undosh yoʻq.
Chet soʻz shu tizimga <b>majburan</b> moslashadi va shuning uchun uzayadi.</p>

<ol class="pe-steps">
  <li><b>Har bir yolgʻiz undoshga unli qoʻshiladi.</b> Odatda <b>u</b> qoʻshiladi,
  lekin <b>t</b> va <b>d</b> dan keyin <b>o</b> qoʻshiladi — chunki トゥ emas,
  ト tabiiyroq. Shuning uchun "test" → <b>テスト</b> [tesuto].</li>
  <li><b>l tovushi yoʻq</b> — u doim ラ-qatoriga aylanadi. "hotel" → <b>ホテル</b>.</li>
  <li><b>Uzunlik ー bilan, ikkilangan undosh ッ bilan</b> koʻrsatiladi.
  "cake" → <b>ケーキ</b>, "cut" → <b>カット</b>.</li>
</ol>

<div class="pe-call pe-uz">
  <p><b>Shuning uchun yaponcha chet soʻzlar uzun eshitiladi.</b> Oʻzbekchada
  "test" bitta boʻgʻin, yaponchada <b>uchta zarb</b>: te-su-to. Bu — buzilish
  emas, moslashish. Oʻzbek tili ham xuddi shunday qiladi: biz "Tokyo" ni
  "Tokio" deb, "sport" ni baʼzan "isport" deb aytamiz, chunki oʻz tilimizning
  tovush qoliplariga solamiz.</p>
</div>

<h3>3. Yangi birikmalar — yaponchada yoʻq tovushlar uchun</h3>

<p>Baʼzi chet tovushlar yapon tilida umuman yoʻq: "fa", "ti", "di", "she", "che",
"we". Ular uchun <b>kichraytirilgan unli</b> ishlatiladi — xuddi kichik ゃゅょ
kabi, faqat bu safar oddiy unlilar kichrayadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Birikma</th><th>Oʻqilishi</th><th>Qanday yasalgan</th><th>Misol</th></tr>
  <tr><td class="pj-res">ファ</td><td>fa</td><td class="pj-stem">フ + kichik ァ</td><td class="pj-uz">ファイル — fayl</td></tr>
  <tr><td class="pj-res">フィ</td><td>fi</td><td class="pj-stem">フ + kichik ィ</td><td class="pj-uz">フィルム — plyonka</td></tr>
  <tr><td class="pj-res">ティ</td><td>ti</td><td class="pj-stem">テ + kichik ィ</td><td class="pj-uz">パーティー — bazm</td></tr>
  <tr><td class="pj-res">ディ</td><td>di</td><td class="pj-stem">デ + kichik ィ</td><td class="pj-uz">ディスク — disk</td></tr>
  <tr><td class="pj-res">シェ</td><td>she</td><td class="pj-stem">シ + kichik ェ</td><td class="pj-uz">シェフ — oshpaz</td></tr>
  <tr><td class="pj-res">チェ</td><td>che</td><td class="pj-stem">チ + kichik ェ</td><td class="pj-uz">チェス — shaxmat</td></tr>
  <tr><td class="pj-res">ジェ</td><td>je</td><td class="pj-stem">ジ + kichik ェ</td><td class="pj-uz">ジェット — reaktiv</td></tr>
  <tr><td class="pj-res">ウィ</td><td>wi</td><td class="pj-stem">ウ + kichik ィ</td><td class="pj-uz">ウィルス — virus</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Mantiq bitta:</b> katta belgining unlisini <em>oʻchirib</em>, kichik
  unli bilan almashtirasiz. フ ["fu"] + kichik ァ = "f" + "a" = <b>ファ</b>.
  Yodlash shart emas — qoidani bilsangiz, har qanday birikmani oʻzingiz
  oʻqiy olasiz.</p>
</div>

<p><b>ヴ</b> belgisi ham bor — u ウ ga dakuten qoʻyib yasaladi va "v" tovushini
beradi. Lekin yaponlar odatda uning oʻrniga ba-qatorini ishlatadi:
"violin" koʻpincha <b>バイオリン</b> deb yoziladi, ヴァイオリン emas.</p>

<h3>4. Endi ismingizni yozamiz</h3>

<p>Mana darsning mukofoti. Qoidalarni ismingizga qoʻllaymiz: har bir undoshga
unli qoʻshing, "l" ni ラ-qatoriga aylantiring, uzun unlini ー bilan bering.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Ism</th><th>Katakana</th><th>Nega shunday</th></tr>
  <tr><td>Afsona</td><td class="pj-res">アフソナ</td><td class="pj-uz">a-fu-so-na — "f" ga unli qoʻshildi</td></tr>
  <tr><td>Jasur</td><td class="pj-res">ジャスル</td><td class="pj-uz">ja-su-ru — oxirgi "r" ga unli qoʻshildi</td></tr>
  <tr><td>Sherbek</td><td class="pj-res">シェルベク</td><td class="pj-uz">she-ru-be-ku — シェ birikmasi, "l" → ル</td></tr>
  <tr><td>Dilnoza</td><td class="pj-res">ディルノザ</td><td class="pj-uz">di-ru-no-za — ディ birikmasi, "l" → ル</td></tr>
  <tr><td>Bekzod</td><td class="pj-res">ベクゾド</td><td class="pj-uz">be-ku-zo-do — "d" dan keyin "o" qoʻshildi</td></tr>
  <tr><td>Oʻzbekiston</td><td class="pj-res">ウズベキスタン</td><td class="pj-uz">u-zu-be-ki-su-ta-n — oxirgi "n" uchun ン</td></tr>
  <tr><td>Toshkent</td><td class="pj-res">タシケント</td><td class="pj-uz">ta-shi-ke-n-to — "sh" → シ, "t" ga "o"</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">ワタシハ アフソナデス</p>
  <p class="pe-ex__rom">watashi wa afusona desu</p>
  <p class="pe-ex__uz">Men Afsonaman.</p>
  <p class="pe-ex__why">Bu yerda hammasi katakanada yozilgan — faqat mashq uchun. Haqiqiy matnda ワタシハ va デス hiraganada boʻlardi (わたしは …です), chunki ular yaponcha soʻz va grammatika. Faqat ism katakanada qoladi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Bitta ismning bir necha yozuvi boʻlishi mumkin.</b> "Sherbek" ni
  シェルベク ham, シェルベック ham yozish mumkin — qaysi biri "toʻgʻri"
  ekanini ism egasi hal qiladi. Rasmiy hujjatda qanday yozgan boʻlsangiz,
  shunisi sizniki. Adashishdan qoʻrqmang.</p>
</div>

<h3>5. Katakana bilan yozilgan dunyo</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Katakana</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td>アメリカ</td><td class="pj-res">amerika</td><td class="pj-uz">Amerika</td></tr>
  <tr><td>ロシア</td><td class="pj-res">roshia</td><td class="pj-uz">Rossiya</td></tr>
  <tr><td>インド</td><td class="pj-res">indo</td><td class="pj-uz">Hindiston</td></tr>
  <tr><td>フランス</td><td class="pj-res">furansu</td><td class="pj-uz">Fransiya</td></tr>
  <tr><td>コンピューター</td><td class="pj-res">konpyūtā</td><td class="pj-uz">kompyuter</td></tr>
  <tr><td>インターネット</td><td class="pj-res">intānetto</td><td class="pj-uz">internet</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">インターネット</p>
  <p class="pe-ex__rom">intānetto</p>
  <p class="pe-ex__uz">internet</p>
  <p class="pe-ex__why">Yetti belgi, yetti zarb. Uchta qoidaning uchalasi ham bu yerda: ー uzun unli beradi, ッ "t" ni ikkilantiradi, oxirgi "t" ga esa "o" qoʻshilgan.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ー ni zarb sanamaslik: コーヒー ni ikki zarbda aytish</p>
  <p class="pe-fix__good">✓ <b>Toʻrt zarb</b>: ko · o · hi · i. ー toʻliq bitta zarb, xuddi ん va ッ kabi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Kichik ァ ni katta ア kabi yozish</p>
  <p class="pe-fix__good">✓ Kattaligi maʼno beradi: <b>ファ</b> = "fa" (bitta zarb), <b>フア</b> = "fu-a" (ikki zarb).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Chet soʻzni oʻz tilidagidek talaffuz qilish: "internet"</p>
  <p class="pe-fix__good">✓ Yaponcha shakli <b>boshqa soʻz</b>: [intānetto], yetti zarb. Yaponiyada asl talaffuz bilan aytsangiz, tushunilmasligi mumkin.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <b>コーヒー</b> da nechta zarb bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Toʻrtta</b>: ko · o · hi · i. Har bir ー toʻliq bitta zarb sanaladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Nega "test" yaponchada <b>テスト</b> boʻladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yolgʻiz undosh boʻlmaydi, shuning uchun har biriga unli qoʻshiladi. "s" ga "u", <b>"t" ga esa "o"</b> qoʻshiladi — shuning uchun テスト, uch zarb.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <b>ファ</b> qanday yasalgan?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>フ</b> ["fu"] + <b>kichik ァ</b>. Katta belgining unlisi oʻchiriladi va kichik unli bilan almashtiriladi: "f" + "a" = fa.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. "Dilnoza" ismidagi "l" ga nima boʻladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yapon tilida <b>l tovushi yoʻq</b>, shuning uchun u ラ-qatoriga aylanadi: <b>ディルノザ</b> — di-ru-no-za.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega ismingiz hiraganada emas, katakanada yoziladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chet el ismlari doim katakanada yoziladi — bu oʻquvchiga "bu ism yaponcha emas" degan signal beradi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>コーヒー</b> — kofe</li>
  <li><b>ケーキ</b> — tort</li>
  <li><b>ノート</b> — daftar</li>
  <li><b>スーパー</b> — doʻkon</li>
  <li><b>テーブル</b> — stol</li>
  <li><b>テスト</b> — test, imtihon</li>
  <li><b>ウズベキスタン</b> — Oʻzbekiston</li>
  <li><b>タシケント</b> — Toshkent</li>
  <li><b>コンピューター</b> — kompyuter</li>
  <li><b>インターネット</b> — internet</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>ー</b> oldingi unlini uzaytiradi va <b>toʻliq bitta zarb</b> sanaydi.</li>
    <li>Chet soʻz yaponchaga oʻtganda uzayadi: har undoshga unli, <b>l → ラ-qatori</b>, uzunlik ー bilan.</li>
    <li>Kichik unli katta belgining unlisini almashtiradi: フ + ァ = <b>ファ</b>. Yozuv bloki tugadi — PJ-10 dan kanji boshlanadi.</li>
  </ul>
</div>
""",
    },
]
