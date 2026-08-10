# -*- coding: utf-8 -*-
"""Prime Math — Block A, darslar 4–6 (boʻlish, amallar tartibi, boʻlinish alomatlari).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_04_06.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_04_06.py
Matnlar import qilinganidan keyin bu faylni --republish bilan qayta yuklang.

⚠️ Kumulyativ: bu darslarda daraja (PM-12), kasr (PM-15) va manfiy son (PM-9)
ishlatilmaydi — ular hali oʻrgatilmagan.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_math_04_06.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Math",
    "category": "math",
    "description": (
        "Maktab matematikasi noldan — 100 ta dars. Sonlar, kasr va foiz, algebra, "
        "grafik, geometriya, statistika va matnli masalalar. Hammasi oʻzbek tilida, "
        "har bir qoida nega ishlashi tushuntirilgan."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    # PM-4 — boʻlish va qoldiq
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-4: Boʻlish, qoldiqli boʻlish va javobni tekshirish",
        "category": "math",
        "order": 4,
        "summary": (
            "Boʻlishning ikki maʼnosi, qoldiqli boʻlish va uning qoidasi, ustunda boʻlish "
            "hamda qoldiq bilan nima qilish kerakligini hal qiladigan matnli masalalar."
        ),
        "stories": ["Oʻttiz yetti kishi, oltitadan stol"],
        "content": """
<h2>PM-4: Boʻlish, qoldiqli boʻlish va javobni tekshirish</h2>

<p>Nodira opa sinfni kafega olib bordi. Bolalar <b>37</b> nafar, stollar esa
<b>6 kishilik</b>. Sardor darrov hisobladi: «37 ni 6 ga boʻlsak, 6 chiqadi». Toʻgʻri
hisobladi — lekin notoʻgʻri javob berdi. Chunki oltita stolga 36 kishi oʻtiradi, bittasi
esa tik turib qoladi. Bu darsda boʻlishni ham, undan ortib qolgan <em>qoldiq</em> bilan
nima qilishni ham oʻrganamiz — masalaning javobi koʻpincha aynan shu qoldiqda hal
boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>boʻlishning ikki maʼnosini ajrata olasiz;</li>
    <li>qoldiqli boʻlishni yozasiz va qoldiq qoidasini bilasiz;</li>
    <li>ustunda boʻlasiz va javobni koʻpaytirish bilan tekshirasiz;</li>
    <li>qoldiqni javobga qoʻshish kerakmi yoki yoʻqmi — buni masaladan oʻqiy olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Nomlar</span>
  <span class="pe-chip pe-chip--o">boʻlinuvchi</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--o">boʻluvchi</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">boʻlinma</span>
  <span class="pe-chip pe-chip--opt">(qoldiq)</span>
</div>

<h3>Boʻlishning ikki maʼnosi</h3>

<p>Bitta amal, ikki xil savol — va ikkalasi ham toʻgʻri:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Nechtadan tegadi?</p>
    <p>24 ta konfet 4 bolaga teng boʻlinsa, <b>har biriga nechtadan</b> tegadi?</p>
    <p>24 ÷ 4 = <b>6 ta</b> — bu bir kishiga tegadigan miqdor.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Nechta guruh chiqadi?</p>
    <p>24 ta konfet 4 tadan qilib solinsa, <b>nechta paket</b> chiqadi?</p>
    <p>24 ÷ 4 = <b>6 ta</b> — bu paketlar soni.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Ikkala savolda ham hisob bir xil, lekin javobning <b>nomi</b> boshqa: birinchisida
"6 ta konfet", ikkinchisida "6 ta paket". Matnli masalada javobni yozganda har doim
uning nomini ham yozing — shunda nimani hisoblaganingizni adashtirmaysiz.</div>

<h3>Boʻlish — koʻpaytirishning teskarisi</h3>

<p>Boʻlish alohida sirli amal emas. <b>24 ÷ 4</b> degani "4 ni nechaga koʻpaytirsam 24
chiqadi?" degani. Shuning uchun koʻpaytirish jadvalini bilgan odam boʻlishni ham
biladi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">4 × 6 = 24  →  24 ÷ 4 = 6  va  24 ÷ 6 = 4</p>
  <p class="pe-ex__uz">Bitta koʻpaytirishdan ikkita boʻlish chiqadi.</p>
</div>

<h3>Qoldiqli boʻlish</h3>

<p>Har doim ham silliq boʻlinavermaydi. 37 ni 6 ga boʻlsak, 6 ta toʻliq oltilik chiqadi
va bitta ortib qoladi:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">37 ÷ 6</span>
    <span class="pm-solve__why">6 ni nechaga koʻpaytirsak 37 dan oshmaydi?</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">6 × 6 = 36</span>
    <span class="pm-solve__why">Bu 37 dan kichik, 6 × 7 = 42 esa katta — demak boʻlinma 6</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">37 ÷ 6 = 6 (qoldiq 1)</span>
    <span class="pm-solve__why">37 − 36 = 1 — qolgani</span>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Qoldiq har doim boʻluvchidan kichik boʻladi.</b> Agar qoldiq boʻluvchiga teng yoki
undan katta chiqsa, demak boʻlinma kichik olingan — yana bitta guruh chiqar edi.</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>6 × 6 + 1 = 37 ✓ — boʻlinma × boʻluvchi + qoldiq = boʻlinuvchi. Qoldiqli boʻlishni
  har doim shu formula bilan tekshiring.</p>
</div>

<h3>Ustunda boʻlish</h3>

<p>Katta sonni boʻlganda chapdan boshlab, razryad-razryad ishlaymiz. <b>852 ÷ 4</b>:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 ÷ 4 = 2</span>
    <span class="pm-solve__why">Yuzliklar: javobning birinchi raqami 2</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 ÷ 4 = 1, qoldiq 1</span>
    <span class="pm-solve__why">Oʻnliklar: 1 ni yozamiz, qolgan 1 oʻnlikni pastga tushiramiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 ÷ 4 = 3</span>
    <span class="pm-solve__why">Birliklar: tushgan 1 oʻnlik va 2 birlik — 12 ta birlik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">852 ÷ 4 = 213</span>
    <span class="pm-solve__why">Tekshirish: 213 × 4 = 852 ✓ (PM-3 dagi misolimiz)</span>
  </div>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>852 ÷ 4 ≈ 800 ÷ 4 = 200. Javob 200 dan sal katta boʻlishi kerak — 213 mos keladi.
  Agar 23 yoki 2 130 chiqsa, razryadda xato bor.</span>
</div>

<h3>0 va 1 bilan boʻlish</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Songa 1 ga</p>
    <p>7 ÷ 1 = 7. Bittadan guruhga ajratsak, guruhlar soni sonning oʻzi.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Nolni boʻlish</p>
    <p>0 ÷ 7 = 0. Hech narsani yetti kishiga boʻlsak, har biriga hech narsa tegadi.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Nolga boʻlish</p>
    <p>7 ÷ 0 — <b>maʼnosi yoʻq</b>. "0 ni nechaga koʻpaytirsak 7 chiqadi?" — hech qanday
    songa. Shuning uchun nolga boʻlish mumkin emas.</p>
  </div>
</div>

<h3>Matnli masala</h3>

<p>Sinfda <b>37</b> oʻquvchi bor. Kafedagi har bir stolga <b>6</b> kishi sigʻadi.
<b>Hamma oʻtirishi uchun kamida nechta stol kerak?</b></p>

<p><em>Nima soʻralyapti?</em> Stollar soni — va <b>hamma</b> oʻtirishi kerak. Demak
qoldiqni eʼtiborsiz qoldirib boʻlmaydi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">37 ÷ 6 = 6 (qoldiq 1)</span>
    <span class="pm-solve__why">Oltita stol toʻladi, bitta bola joysiz qoladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6 + 1 = 7 ta stol</span>
    <span class="pm-solve__why">Oʻsha bitta bolaga ham stol kerak</span>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bitta boʻlishdan uch xil javob chiqishi mumkin — masala qaysi birini soʻrayotganini
oʻqing:
<b>«Nechta stol toʻladi?»</b> → 6.
<b>«Kamida nechta stol kerak?»</b> → 7.
<b>«Oxirgi stolda necha kishi oʻtiradi?»</b> → 1.
Uchalasi ham 37 ÷ 6 = 6 (qoldiq 1) dan chiqadi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">37 ÷ 6 = <s>5 (qoldiq 7)</s> — qoldiq boʻluvchidan katta</p>
  <p class="pe-good">37 ÷ 6 = <b>6 (qoldiq 1)</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«Kamida nechta stol kerak?» — <s>6 ta</s>, qoldiq tashlab yuborilgan</p>
  <p class="pe-good"><b>7 ta</b> — qolgan bitta bolaga ham joy kerak</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">7 ÷ 0 = <s>0</s> yoki <s>7</s></p>
  <p class="pe-good">7 ÷ 0 — <b>bunday amal yoʻq</b>, nolga boʻlib boʻlmaydi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     96 ÷ 4 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>24.</strong> Razryadlab: 8 oʻnlik ÷ 4 = 2 oʻnlik,
    qolgan 16 ÷ 4 = 4. Tekshirish: 24 × 4 = 96 ✓</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     100 ta daftar 8 tadan qilib paketlanadi. Nechta toʻla paket chiqadi va nechtasi
     ortib qoladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>12 ta paket, 4 ta daftar ortadi.</strong>
    100 ÷ 8 = 12 (qoldiq 4), chunki 8 × 12 = 96 va 100 − 96 = 4. Tekshirish:
    12 × 8 + 4 = 100 ✓</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻlinma 7 ga, boʻluvchi 9 ga, qoldiq 5 ga teng. Boʻlinuvchi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>68.</strong> Boʻlinma × boʻluvchi + qoldiq =
    7 × 9 + 5 = 63 + 5 = <b>68</b>. Qoldiq 5 boʻluvchi 9 dan kichik — qoida
    bajarilyapti.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bir sonni 5 ga boʻlganda qoldiq eng koʻpi bilan qancha boʻlishi mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>4.</strong> Qoldiq boʻluvchidan kichik boʻlishi
    shart. Agar qoldiq 5 chiqsa, u yana bitta toʻliq beshlikni beradi va boʻlinma
    bittaga oshadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     50 ta bolani 8 kishilik avtobuslarda olib ketish kerak. Nechta avtobus kerak va
     oxirgisida nechta bola boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>7 ta avtobus, oxirgisida 2 bola.</strong>
    50 ÷ 8 = 6 (qoldiq 2): oltita avtobus toʻladi, 2 bola qoladi — ularga ham avtobus
    kerak, demak 6 + 1 = <b>7</b>. Tekshirish: 6 × 8 + 2 = 50 ✓</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Boʻlinuvchi</b><span>boʻlinayotgan son; ingl. dividend</span></li>
  <li><b>Boʻluvchi</b><span>nechaga boʻlinayotgani; ingl. divisor</span></li>
  <li><b>Boʻlinma</b><span>boʻlish natijasi; ingl. quotient</span></li>
  <li><b>Qoldiq</b><span>boʻlinmay ortib qolgan qism; ingl. remainder</span></li>
  <li><b>Teng boʻlish</b><span>qoldiqsiz boʻlinish; ingl. exact division</span></li>
  <li><b>Teskari amal</b><span>boʻlish — koʻpaytirishning teskarisi; ingl. inverse operation</span></li>
  <li><b>Ustunda boʻlish</b><span>razryadlab boʻlish usuli; ingl. long division</span></li>
  <li><b>Tekshirish</b><span>boʻlinma × boʻluvchi + qoldiq; ingl. checking</span></li>
  <li><b>Nolga boʻlish</b><span>aniqlanmagan amal; ingl. division by zero</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda tuting</p>
  <ul>
    <li>Boʻlish — koʻpaytirishning teskarisi: <b>24 ÷ 4</b> = "4 ni nechaga koʻpaytirsam 24 chiqadi?".</li>
    <li><b>Qoldiq har doim boʻluvchidan kichik.</b></li>
    <li>Tekshirish: <b>boʻlinma × boʻluvchi + qoldiq = boʻlinuvchi</b>.</li>
    <li>Matnli masalada qoldiq bilan nima qilishni <b>savol</b> hal qiladi — baʼzan uni tashlaysiz, baʼzan javobga bitta qoʻshasiz.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-5 — amallar tartibi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-5: Amallar tartibi va qavslar",
        "category": "math",
        "order": 5,
        "summary": (
            "Nega bitta ifodadan ikki xil javob chiqadi? Amallar tartibi, qavslarning "
            "vazifasi, chapdan oʻngga qoidasi va xarid hisobidagi matnli masalalar."
        ),
        "stories": ["Bitta hisob, ikkita javob"],
        "content": """
<h2>PM-5: Amallar tartibi va qavslar</h2>

<p>Doskada bitta ifoda turibdi: <b>2 + 3 × 4</b>. Sardor 20 deb javob berdi, Afsona 14
deb. Ikkalasi ham xato qilmagandek — Sardor chapdan oʻngga yurdi, Afsona esa avval
koʻpaytirdi. Lekin matematikada bitta ifodaning bitta javobi boʻlishi <em>shart</em>,
aks holda hech kim bir-birini tushunmaydi. Shuning uchun butun dunyo bitta tartibga
kelishib olgan. Bu darsda oʻsha tartibni oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>amallar tartibini bilib olasiz va nega u kerakligini tushunasiz;</li>
    <li>qavslar javobni qanday oʻzgartirishini koʻrasiz;</li>
    <li>"chapdan oʻngga" qoidasini toʻgʻri qoʻllaysiz;</li>
    <li>xarid hisobini bitta ifodaga yigʻa olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tartib</span>
  <span class="pe-chip pe-chip--s">1. Qavslar</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">2. × va ÷</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">3. + va −</span>
  <span class="pe-chip pe-chip--opt">bir darajadagilar chapdan oʻngga</span>
</div>

<h3>Nega koʻpaytirish oldin bajariladi?</h3>

<p>Bu shunchaki kelishuv emas — bunda maʼno bor. <b>2 + 3 × 4</b> ni hayotdagi jumlaga
aylantiring: «Menda 2 ta daftar bor edi, keyin 3 tadan 4 ta paket oldim». 3 × 4 — bu
<em>bitta narsa</em>, yaʼni paketlardagi daftarlar. Uni birga hisoblab, keyin
boshidagi 2 taga qoʻshamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 + 3 × 4</span>
    <span class="pm-solve__why">Berilgan ifoda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 + 12</span>
    <span class="pm-solve__why">Avval koʻpaytirish: 3 × 4 = 12</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 14</span>
    <span class="pm-solve__why">Endi qoʻshish</span>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Kalkulyatorning oddiy (telefon) rejimi koʻpincha chapdan oʻngga hisoblaydi va 20 ni
beradi. Muhandislik rejimidagi kalkulyator esa 14 ni beradi. Kalkulyator xato qilmaydi —
u sizdan boshqacha tartibda oʻqiydi. Shuning uchun uzun ifodani kalkulyatorga
kiritishdan oldin qavslarni oʻzingiz qoʻying.</div>

<h3>Qavslar — tartibni buzish huquqi</h3>

<p>Qavs "avval buni hisobla" degan buyruq. U ifodaning maʼnosini butunlay
oʻzgartiradi:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Qavssiz</p>
    <p><b>2 + 3 × 4 = 14</b></p>
    <p>2 ta daftar, ustiga 3 tadan 4 paket.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Qavs bilan</p>
    <p><b>(2 + 3) × 4 = 20</b></p>
    <p>Har bir paketda 2 + 3 = 5 tadan, paket esa 4 ta.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">100 − (20 + 5) × 3 = 100 − 25 × 3 = 100 − 75 = 25</p>
  <p class="pe-ex__uz">Avval qavs, keyin koʻpaytirish, eng oxirida ayirish.</p>
  <p class="pe-ex__why">Qavsdagi natija (25) hali javob emas — u koʻpaytirishga kiradi.</p>
</div>

<h3>Bir darajadagi amallar — chapdan oʻngga</h3>

<p>Koʻpaytirish va boʻlish <b>teng huquqli</b>. Qoʻshish va ayirish ham shunday. Ular
uchrashganda tartibni faqat oʻrni hal qiladi: chapdan oʻngga.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">24 ÷ 4 × 2</span>
    <span class="pm-solve__why">Chapdagisi birinchi: 24 ÷ 4 = 6</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6 × 2 = 12</span>
    <span class="pm-solve__why">3 emas! Avval koʻpaytirsak (4 × 2 = 8) butunlay boshqa javob chiqadi</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">20 − 8 + 3 = 12 + 3 = 15</p>
  <p class="pe-ex__uz">Avval ayirish, chunki u chapda turibdi. 20 − 11 = 9 emas.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Roʻyxatdagi "×, ÷" bitta qadam, "+, −" bitta qadam. Koʻpchilik "avval koʻpaytirish, keyin
boʻlish" deb yodlab oladi va <b>24 ÷ 4 × 2</b> da adashadi. Ular bir darajada turadi —
faqat kim chapda boʻlsa, oʻsha birinchi.</div>

<h3>Matnli masala</h3>

<p>Karim aka bozorda <b>3 kg</b> olma oldi, har kilosi <b>12 000</b> soʻmdan. Yana
<b>2 kg</b> uzum oldi, har kilosi <b>15 000</b> soʻmdan. Sotuvchiga <b>100 000</b> soʻm
berdi. <b>Qancha qaytim oldi?</b></p>

<p><em>Nima soʻralyapti?</em> Qaytim. Demak avval jami xarajat, keyin ayirish.</p>

<div class="pe-table-wrap">
  <table class="pm-word">
    <tr><th>Matnda</th><th>Ifodada</th></tr>
    <tr><td>3 kg, har kilosi 12 000 soʻmdan</td><td class="pm-word__sym">3 × 12 000</td></tr>
    <tr><td>2 kg, har kilosi 15 000 soʻmdan</td><td class="pm-word__sym">2 × 15 000</td></tr>
    <tr><td>100 000 berdi, qaytim…</td><td class="pm-word__sym">100 000 − (…)</td></tr>
  </table>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">100 000 − (3 × 12 000 + 2 × 15 000)</span>
    <span class="pm-solve__why">Butun masala bitta ifodada</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">100 000 − (36 000 + 30 000)</span>
    <span class="pm-solve__why">Qavs ichida avval koʻpaytirishlar</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">100 000 − 66 000 = 34 000 soʻm</span>
    <span class="pm-solve__why">Qaytim</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>34 000 + 66 000 = 100 000 ✓ — qaytim va xarajat birga berilgan pulni beradi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">2 + 3 × 4 = <s>20</s> — chapdan oʻngga hisoblangan</p>
  <p class="pe-good">2 + 3 × 4 = <b>14</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad">20 − 8 + 3 = <s>9</s> — avval 8 + 3 qoʻshib yuborilgan</p>
  <p class="pe-good">20 − 8 + 3 = <b>15</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad">24 ÷ 4 × 2 = <s>3</s> — koʻpaytirish boʻlishdan oldin bajarilgan</p>
  <p class="pe-good">24 ÷ 4 × 2 = <b>12</b></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     5 + 2 × 6 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>17.</strong> Avval 2 × 6 = 12, keyin 5 + 12 = 17.
    Chapdan oʻngga hisoblasak 42 chiqadi — bu eng koʻp uchraydigan xato.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     (5 + 2) × 6 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>42.</strong> Qavs tartibni oʻzgartirdi:
    5 + 2 = 7, keyin 7 × 6 = 42. Bitta qavs javobni 17 dan 42 ga koʻtardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     30 − 10 ÷ 5 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>28.</strong> Boʻlish qoʻshish-ayirishdan oldin:
    10 ÷ 5 = 2, keyin 30 − 2 = 28. (30 − 10) ÷ 5 = 4 boʻlardi, lekin qavs yoʻq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     48 ÷ (2 × 3) = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>8.</strong> Qavs ichi birinchi: 2 × 3 = 6, keyin
    48 ÷ 6 = 8. Qavssiz 48 ÷ 2 × 3 boʻlsa, chapdan oʻngga: 24 × 3 = 72 — butunlay boshqa
    javob.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Kinoga 4 ta chipta olindi, har biri 25 000 soʻmdan. Yana 2 ta popkorn olindi, har
     biri 15 000 soʻmdan. Jami qancha toʻlangan? Yechimni bitta ifodada yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>4 × 25 000 + 2 × 15 000 = 100 000 + 30 000 =
    130 000 soʻm.</strong> Bu yerda qavs kerak emas: koʻpaytirishlar oʻzi birinchi
    bajariladi. Qavs faqat tartibni <em>oʻzgartirish</em> kerak boʻlgandagina
    qoʻyiladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Ifoda</b><span>sonlar va amallardan tuzilgan yozuv; ingl. expression</span></li>
  <li><b>Amallar tartibi</b><span>qaysi amal oldin bajarilishi; ingl. order of operations</span></li>
  <li><b>Qavs</b><span>"avval buni hisobla" belgisi; ingl. brackets</span></li>
  <li><b>Chapdan oʻngga</b><span>teng darajadagi amallar qoidasi; ingl. left to right</span></li>
  <li><b>Qiymat</b><span>ifodani hisoblab chiqqan son; ingl. value</span></li>
  <li><b>Teng darajali amallar</b><span>× va ÷ ; + va − ; ingl. same precedence</span></li>
  <li><b>Ichma-ich qavslar</b><span>qavs ichidagi qavs, ichkaridan boshlanadi; ingl. nested brackets</span></li>
  <li><b>Qaytim</b><span>berilgan puldan xarajat ayirilgani; ingl. change</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda tuting</p>
  <ul>
    <li>Tartib: <b>qavslar → × va ÷ → + va −</b>.</li>
    <li>Teng darajadagi amallar <b>chapdan oʻngga</b> bajariladi.</li>
    <li>Qavs — tartibni oʻzgartirishning yagona yoʻli, keraksiz joyga qoʻyilmaydi.</li>
    <li>Uzun matnli masalani <b>bitta ifodaga</b> yigʻing: shunda nima qilayotganingiz koʻrinib turadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-6 — boʻlinish alomatlari
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-6: Boʻlinish alomatlari: 2, 3, 4, 5, 6, 9, 10 ga",
        "category": "math",
        "order": 6,
        "summary": (
            "Boʻlmasdan turib boʻlinishini bilish: 2, 3, 4, 5, 6, 9 va 10 ga boʻlinish "
            "alomatlari, ular nega ishlaydi va qayerda asqotadi."
        ),
        "stories": ["Guruhlarga boʻlinamiz"],
        "content": """
<h2>PM-6: Boʻlinish alomatlari: 2, 3, 4, 5, 6, 9, 10 ga</h2>

<p>Jismoniy tarbiya oʻqituvchisi <b>84</b> oʻquvchini teng guruhlarga ajratmoqchi.
Beshtadan boʻlsinmi? Oltitadan? U hech narsani boʻlib oʻtirmadi — songa bir qarab,
«beshtadan chiqmaydi, oltitadan chiqadi» dedi. Bu darsda ana shu tez qarashni
oʻrganamiz: <b>boʻlinish alomatlari</b> — boʻlmasdan turib javobini aytish
usullari.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>2, 3, 4, 5, 6, 9 va 10 ga boʻlinish alomatlarini bilib olasiz;</li>
    <li>3 va 9 ga boʻlinish alomati nega ishlashini tushunasiz;</li>
    <li>bir sonni bir necha alomat boʻyicha tekshira olasiz;</li>
    <li>teng boʻlish masalalarini tez yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qayerga qaraladi</span>
  <span class="pe-chip pe-chip--o">oxirgi raqam: 2, 5, 10</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">raqamlar yigʻindisi: 3, 9</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">oxirgi ikki raqam: 4</span>
  <span class="pe-chip pe-chip--opt">2 va 3 birga: 6</span>
</div>

<h3>Alomatlar jadvali</h3>

<div class="pe-table-wrap"><table>
  <tr><th>Nechaga</th><th>Alomat</th><th>Misol</th></tr>
  <tr><td><b>2</b></td><td>oxirgi raqam juft: 0, 2, 4, 6, 8</td><td>84 ✓ · 47 ✗</td></tr>
  <tr><td><b>5</b></td><td>oxirgi raqam 0 yoki 5</td><td>1 350 ✓ · 84 ✗</td></tr>
  <tr><td><b>10</b></td><td>oxirgi raqam 0</td><td>1 350 ✓ · 135 ✗</td></tr>
  <tr><td><b>3</b></td><td>raqamlar yigʻindisi 3 ga boʻlinadi</td><td>84 → 8 + 4 = 12 ✓</td></tr>
  <tr><td><b>9</b></td><td>raqamlar yigʻindisi 9 ga boʻlinadi</td><td>5 274 → 18 ✓</td></tr>
  <tr><td><b>4</b></td><td>oxirgi <b>ikki</b> raqamdan tuzilgan son 4 ga boʻlinadi</td><td>3 116 → 16 ✓</td></tr>
  <tr><td><b>6</b></td><td>2 ga <b>ham</b>, 3 ga <b>ham</b> boʻlinadi</td><td>84 ✓ · 81 ✗ (toq)</td></tr>
</table></div>

<h3>Nega 3 va 9 alomati ishlaydi?</h3>

<p>Bu eng qiziq qismi. 10 = 9 + 1, 100 = 99 + 1, 1 000 = 999 + 1. Yaʼni har bir razryad
birligi «9 ga boʻlinadigan son + 1» koʻrinishida. Shuning uchun har qanday sonni
razryadlarga yoysak, uning bir qismi doim 9 ga toʻliq boʻlinadi, qolgani esa — aynan
<b>raqamlar yigʻindisi</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">84 = 8 × 10 + 4</span>
    <span class="pm-solve__why">Yoyilma yozuv (PM-1)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 8 × (9 + 1) + 4</span>
    <span class="pm-solve__why">10 ni 9 + 1 deb yozdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= 8 × 9 + (8 + 4)</span>
    <span class="pm-solve__why">Birinchi qism 9 ga ham, 3 ga ham boʻlinadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">demak faqat 8 + 4 = 12 ni tekshirsak boʻldi</span>
    <span class="pm-solve__why">12 uchga boʻlinadi → 84 ham uchga boʻlinadi</span>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Katta sonda raqamlar yigʻindisini yana bir marta yigʻish mumkin: 5 274 → 5 + 2 + 7 + 4 =
18 → 1 + 8 = 9. Toʻqqiz chiqdi, demak son 9 ga ham, 3 ga ham boʻlinadi. Yoʻl-yoʻlakay
toʻqqizlarni tashlab yuborsangiz ish yanada tezlashadi.</div>

<h3>Bitta sonni bir necha alomatdan oʻtkazamiz</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>84</p>
    <p>Juft → <b>2 ✓</b>. 8 + 4 = 12 → <b>3 ✓</b>. Ikkalasi ham boʻlgani uchun
    <b>6 ✓</b>. Oxirgi ikki raqam 84 ÷ 4 = 21 → <b>4 ✓</b>. 12 toʻqqizga boʻlinmaydi →
    <b>9 ✗</b>. Oxirgi raqam 4 → <b>5 ✗</b>, <b>10 ✗</b>.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>1 350</p>
    <p>Oxiri 0 → <b>10 ✓</b>, <b>5 ✓</b>, <b>2 ✓</b>. 1 + 3 + 5 + 0 = 9 → <b>9 ✓</b> va
    <b>3 ✓</b>, demak <b>6 ✓</b>. Oxirgi ikki raqam 50, u 4 ga boʻlinmaydi →
    <b>4 ✗</b>.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Alomat — bu <b>boʻlinadi yoki yoʻq</b> degan savolga javob, <em>nechta chiqadi</em>
degan savolga emas. 84 uchga boʻlinishini bir soniyada aytasiz, lekin 28 chiqishini
bilish uchun baribir boʻlish kerak.</div>

<h3>Matnli masala</h3>

<p>Sinfda <b>84</b> ta daftar bor. Ularni oʻquvchilarga <b>teng</b> ulashish kerak,
qoldiqsiz. <b>Sinfda 5 ta, 6 ta yoki 9 ta oʻquvchi boʻlsa, qaysi holatda teng ulashish
mumkin?</b></p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 ta oʻquvchi?</span>
    <span class="pm-solve__why">84 ning oxirgi raqami 4 — 0 ham, 5 ham emas → boʻlinmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">9 ta oʻquvchi?</span>
    <span class="pm-solve__why">8 + 4 = 12, u 9 ga boʻlinmaydi → boʻlinmaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6 ta oʻquvchi ✓ — har biriga 14 tadan</span>
    <span class="pm-solve__why">84 juft (2 ✓) va 12 uchga boʻlinadi (3 ✓), demak 6 ga boʻlinadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>6 × 14 = 84 ✓ — qoldiqsiz chiqdi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">«123 uchga boʻlinadi, chunki <s>oxirgi raqami 3</s>»</p>
  <p class="pe-good">123 uchga boʻlinadi, chunki <b>1 + 2 + 3 = 6</b> uchga boʻlinadi
  (oxirgi raqamga qarash faqat 2, 5 va 10 uchun ishlaydi)</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«3 116 ning oxirgi raqami 6, demak <s>4 ga boʻlinadi</s>»</p>
  <p class="pe-good">Oxirgi <b>ikki</b> raqamga qaraladi: 16 ÷ 4 = 4 ✓ — javob toʻgʻri,
  lekin sabab notoʻgʻri edi. 3 126 da esa 26 toʻrtga boʻlinmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«84 juft, demak <s>6 ga boʻlinadi</s>»</p>
  <p class="pe-good">6 uchun <b>ikkala</b> shart kerak: juft <b>va</b> raqamlar yigʻindisi
  3 ga boʻlinsin. 82 juft, lekin 8 + 2 = 10 → 6 ga boʻlinmaydi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     5 274 qaysi sonlarga boʻlinadi: 2, 3, 5, 9?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>2, 3 va 9 ga.</strong> Oxirgi raqam 4 — juft,
    demak 2 ✓. Raqamlar yigʻindisi 5 + 2 + 7 + 4 = 18: uchga ham, toʻqqizga ham boʻlinadi
    → 3 ✓ va 9 ✓. Oxirgi raqam 5 ham, 0 ham emas → 5 ✗</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     3 116 soni 4 ga boʻlinadimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ha.</strong> Oxirgi ikki raqamdan tuzilgan son —
    16, u 4 ga boʻlinadi (16 ÷ 4 = 4). Butun sonni boʻlish shart emas: 3 100 ning oʻzi
    100 ga karrali, 100 esa 4 ga boʻlinadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bir son 2 ga ham, 3 ga ham boʻlinadi. U yana qaysi songa albatta boʻlinadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>6 ga.</strong> Bu 6 ning alomatining oʻzi:
    son ham juft, ham uchga karrali boʻlsa, u oltiga boʻlinadi. Masalan 84: 84 ÷ 6 =
    14.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     4 ★ 5 sonidagi ★ oʻrniga qaysi raqamni qoʻysak, son 9 ga boʻlinadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>0 yoki 9.</strong> Yigʻindi 4 + ★ + 5 = 9 + ★
    boʻlishi kerak va u 9 ga boʻlinsin. ★ = 0 boʻlsa yigʻindi 9, ★ = 9 boʻlsa 18 —
    ikkalasi ham 9 ga boʻlinadi. Demak 405 va 495.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     96 ta konfetni qoldiqsiz teng ulashmoqchimiz. 4, 5 yoki 8 kishi boʻlsa, qaysi
     holatlarda chiqadi va har biriga nechtadan tegadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>4 kishiga 24 tadan, 8 kishiga 12 tadan;
    5 kishiga chiqmaydi.</strong> Oxirgi ikki raqam 96 toʻrtga boʻlinadi → 4 ✓
    (96 ÷ 4 = 24). Oxirgi raqam 6 — 0 ham, 5 ham emas → 5 ✗. 8 uchun alomat oʻrganmadik,
    shuning uchun boʻlib koʻramiz: 96 ÷ 8 = 12 ✓</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Boʻlinish alomati</b><span>boʻlmasdan aniqlash usuli; ingl. divisibility rule</span></li>
  <li><b>Karrali</b><span>berilgan songa qoldiqsiz boʻlinadigan son; ingl. multiple</span></li>
  <li><b>Boʻluvchi</b><span>sonni qoldiqsiz boʻladigan son; ingl. divisor</span></li>
  <li><b>Juft son</b><span>2 ga boʻlinadigan son; ingl. even number</span></li>
  <li><b>Toq son</b><span>2 ga boʻlinmaydigan son; ingl. odd number</span></li>
  <li><b>Raqamlar yigʻindisi</b><span>sondagi raqamlarni qoʻshish; ingl. digit sum</span></li>
  <li><b>Qoldiqsiz</b><span>teng, ortmasdan; ingl. exactly, without remainder</span></li>
  <li><b>Umumiy boʻluvchi</b><span>ikki sonni ham boʻladigan son; ingl. common divisor</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda tuting</p>
  <ul>
    <li><b>Oxirgi raqam</b> — 2, 5, 10 uchun. <b>Oxirgi ikki raqam</b> — 4 uchun.</li>
    <li><b>Raqamlar yigʻindisi</b> — 3 va 9 uchun, va bu 10 = 9 + 1 boʻlgani uchun ishlaydi.</li>
    <li><b>6</b> ga boʻlinish = 2 ga <b>va</b> 3 ga boʻlinish.</li>
    <li>Alomat "boʻlinadimi?" degan savolga javob beradi, "nechta chiqadi?" degan savolga emas.</li>
  </ul>
</div>
""",
    },
]
