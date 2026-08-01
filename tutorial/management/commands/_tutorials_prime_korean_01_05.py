# -*- coding: utf-8 -*-
"""Prime Korean — Block A, darslar 1–5 (Hangul).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_01_05.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Korean",
    "category": "korean",
    "description": (
        "Koreys tili noldan TOPIK II gacha — 100 ta dars. Hangul, grammatika qoliplari, "
        "oʻzbekcha tushuntirish va oʻzingiz tekshiradigan mashqlar."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-1: Hangul bilan tanishuv — dunyodagi eng mantiqiy alifbo",
        "category": "korean",
        "order": 1,
        "summary": (
            "Hangul iyeroglif emas — 24 ta harfdan iborat alifbo. Harflar qanday qilib "
            "boʻgʻin blokiga yigʻilishini tushunib, birinchi koreyscha soʻzingizni oʻqiysiz."
        ),
        "content": """
<h2>PK-1: Hangul bilan tanishuv — dunyodagi eng mantiqiy alifbo</h2>

<p>Koreys seriali koʻryapsiz, ekranda <b>한국어</b> deb yozilgan. Sizga bu uchta kichkina
rasm boʻlib koʻrinadi — xitoycha iyeroglifga oʻxshaydi, mingta belgini yodlash kerakdek.
Aslida esa bu yerda atigi <b>oltita harf</b> bor: ㅎ, ㅏ, ㄴ, ㄱ, ㅜ, ㅇ, ㅓ. Hangul —
oddiy alifbo, xuddi siz oʻqiyotgan lotin alifbosi kabi. Va u shunchalik puxta
oʻylanganki, koʻp odam uni bir hafta ichida oʻqiy boshlaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Hangul nima va u nega iyeroglif emasligini bilib olasiz</li>
    <li>24 ta asosiy harfni — 14 undosh va 10 unlini — koʻrasiz</li>
    <li>Harflar nega bir qatorga emas, boʻgʻin blokiga yigʻilishini tushunasiz</li>
    <li>Birinchi koreyscha soʻzingizni harflab oʻqiysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Koreys boʻgʻini</span>
  <span class="pe-chip pe-chip--s">초성 — bosh undosh</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">중성 — unli</span>
  <span class="pe-chip pe-chip--opt">+ 종성 — yakuniy undosh</span>
</div>

<h3>1. Hangulni bir kishi oʻylab topgan</h3>

<p>Dunyodagi deyarli barcha alifbolar asta-sekin, asrlar davomida oʻzgarib shakllangan.
Hangul esa yoʻq. Uni <b>1443-yilda 세종대왕</b> (Buyuk qirol Sejong) va uning olimlari
maxsus <em>ixtiro qilishgan</em>.</p>

<p>Sabab oddiy edi. Oʻsha paytda koreyslar oʻz tilini xitoy iyerogliflari — <b>한자</b>
bilan yozardi. Iyeroglif mingtalab, ularni yodlash uchun yillar kerak, ya'ni yozuvni
faqat boy zodagonlar bilardi. Oddiy dehqon arizasini ham yoza olmasdi. Qirol Sejong shu
adolatsizlikni tugatmoqchi boʻldi va yangi yozuvni <b>훈민정음</b> — "xalqni oʻrgatuvchi
toʻgʻri tovushlar" deb atadi.</p>

<div class="pe-call pe-tip"><span class="pe-call__t">Qiziq</span>
훈민정음 kitobining soʻzboshisida shunday deyilgan: aqlli odam bu yozuvni ertalabgacha,
aqli oʻtmasroq odam esa oʻn kunda oʻrganadi. Bu maqtanish emas — Hangul haqiqatan ham
shunday tuzilgan.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Siz uchun alifbo tushunchasi yangilik emas: oʻzbek tilida ham har harf bitta tovushni
bildiradi. Hangulda ham xuddi shunday. <b>Yangi boʻlgan yagona narsa</b> — harflarni
qatorga emas, kvadratchaga yigʻib yozish. Faqat shuni oʻrgansangiz, oʻqiy boshlaysiz.</div>

<h3>2. 24 ta harf — hammasi shu</h3>

<p>Hangulda <b>14 ta undosh (자음)</b> va <b>10 ta unli (모음)</b> bor:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">자음 — undoshlar (14)</p>
    <p style="font-size:1.35rem">ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">모음 — unlilar (10)</p>
    <p style="font-size:1.35rem">ㅏ ㅑ ㅓ ㅕ ㅗ ㅛ ㅜ ㅠ ㅡ ㅣ</p>
  </div>
</div>

<p>Bularga qoʻshimcha 5 ta qattiq undosh (ㄲ ㄸ ㅃ ㅆ ㅉ) va 11 ta qoʻshma unli (ㅐ ㅔ ㅘ …)
ham bor, lekin ular <b>yangi harf emas</b> — yuqoridagilardan yasaladi. Shuning uchun
haqiqatda yodlash kerak boʻlgan narsa juda oz.</p>

<h3>3. Undosh shakllari — bu sizning ogʻzingizning rasmi</h3>

<p>Hangulning eng chiroyli fikri shu: harf shakli oʻsha tovushni aytayotganda til va lab
qanday turishini koʻrsatadi. Beshta asosiy shakl bor, qolgani ulardan oʻsib chiqadi.</p>

<div class="pk-hangul">
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㄱ</span>
    <span class="pk-hangul__rom">g / k</span>
    <span class="pk-hangul__uz">til orqasi tanglayga koʻtariladi</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㄴ</span>
    <span class="pk-hangul__rom">n</span>
    <span class="pk-hangul__uz">til uchi yuqori tish ortida</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅁ</span>
    <span class="pk-hangul__rom">m</span>
    <span class="pk-hangul__uz">yopiq ogʻiz — lablar</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅅ</span>
    <span class="pk-hangul__rom">s</span>
    <span class="pk-hangul__uz">tishning shakli</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅇ</span>
    <span class="pk-hangul__rom">– / ng</span>
    <span class="pk-hangul__uz">ochiq tomoq</span></div>
</div>

<p>Endi sehr boshlanadi. <b>Harfga qoʻshimcha chiziq qoʻshsangiz, tovushga nafas
qoʻshiladi:</b></p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>ㄱ → ㅋ</p>
    <p>ㄱ ustiga bitta chiziq — kuchli nafasli <em>k</em>.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>ㄴ → ㄷ → ㅌ</p>
    <p>ㄴ ga chiziq — ㄷ, yana chiziq — nafasli ㅌ.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>ㅁ → ㅂ → ㅍ</p>
    <p>Lab tovushlari zinapoyasi.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">4</span>ㅅ → ㅈ → ㅊ</p>
    <p>Tish tovushlari zinapoyasi.</p></div>
</div>

<p>Ya'ni 14 ta undoshni yodlash emas, <b>5 ta shaklni</b> va bitta qoidani eslab qolish
kifoya. PK-4 va PK-5 darslarida har birini alohida oʻrganamiz.</p>

<h3>4. Unli shakllari — osmon, yer va inson</h3>

<p>Unlilar boshqa mantiqqa qurilgan. Uchta belgi bor edi:</p>

<ul class="pe-steps">
  <li><b>ㆍ</b> — osmon (dumaloq nuqta; hozir qisqa chiziqcha shaklida yoziladi)</li>
  <li><b>ㅡ</b> — yer (yotiq chiziq)</li>
  <li><b>ㅣ</b> — inson (tik chiziq)</li>
</ul>

<p>Qolgan barcha unli shu uchtasining birikmasi. Inson turibdi (ㅣ), quyosh uning
oʻng tomonida (ㆍ) — <b>ㅏ</b> boʻladi. Quyosh chap tomonda — <b>ㅓ</b>. Yer ustida
quyosh — <b>ㅗ</b>, yer ostida — <b>ㅜ</b>.</p>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Unli shaklidan uning <b>joyini</b> bilib olasiz: chiziqli tik unlilar (ㅏ ㅓ ㅣ)
undoshning <b>oʻng tomoniga</b>, yotiq unlilar (ㅗ ㅜ ㅡ) undoshning <b>tagiga</b>
yoziladi.</div>

<h3>5. Boʻgʻin bloki — Hangulning asosiy fikri</h3>

<p>Mana bu yerda Hangul lotin alifbosidan farq qiladi. Koreyschada harflar bir qatorga
tizilmaydi — ular <b>boʻgʻin (음절)</b> boʻlib, kvadratchaga yigʻiladi:</p>

<div class="pk-block">
  <span class="pk-block__cell pk-block__cell--i">ㅎ<small>초성</small></span>
  <span class="pk-block__cell pk-block__cell--m">ㅏ<small>중성</small></span>
  <span class="pk-block__cell pk-block__cell--f">ㄴ<small>종성</small></span>
  <span class="pk-block__eq">=</span>
  <span class="pk-block__out">한</span>
</div>

<p>Blok ichidagi joylashuv unliga bogʻliq:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Tik unli (ㅏ ㅓ ㅑ ㅕ ㅣ)</p>
    <p>Undosh <b>chapda</b>, unli <b>oʻngda</b>.</p>
    <p style="font-size:1.4rem">가 · 너 · 미 · 시</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Yotiq unli (ㅗ ㅜ ㅛ ㅠ ㅡ)</p>
    <p>Undosh <b>tepada</b>, unli <b>pastda</b>.</p>
    <p style="font-size:1.4rem">고 · 무 · 두 · 그</p>
  </div>
</div>

<p>Uchinchi harf — <b>받침</b> deb ataladigan yakuniy undosh — har doim <b>pastga</b>
tushadi: 간, 곰, 물, 학. Uni PK-7 darsida batafsil koʻramiz.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada "han" deb yozamiz — uchta harf, uchta joy. Koreyschada esa aynan shu uchta
tovush bitta kvadratchaga siqiladi: <b>한</b>. Tovushlar soni bir xil, faqat joylashuvi
boshqacha. Shuning uchun koreyscha matn qisqa koʻrinadi.</div>

<h3>6. Birinchi soʻzingizni oʻqing</h3>

<p>Endi darsning boshidagi soʻzga qaytamiz. Uni harflarga ajratamiz:</p>

<div class="pk-block">
  <span class="pk-block__cell pk-block__cell--i">ㄱ<small>초성</small></span>
  <span class="pk-block__cell pk-block__cell--m">ㅜ<small>중성</small></span>
  <span class="pk-block__cell pk-block__cell--f">ㄱ<small>종성</small></span>
  <span class="pk-block__eq">=</span>
  <span class="pk-block__out">국</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">한국</p>
  <p class="pe-ex__rom">han-guk</p>
  <p class="pe-ex__uz">Koreya</p>
  <p class="pe-ex__why">한 (ㅎ+ㅏ+ㄴ) + 국 (ㄱ+ㅜ+ㄱ) — beshta harf, ikkita blok.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어</p>
  <p class="pe-ex__rom">han-guk-eo</p>
  <p class="pe-ex__uz">koreys tili</p>
  <p class="pe-ex__why">Oxiriga 어 (ㅇ+ㅓ) qoʻshildi. Boshdagi ㅇ hech qanday tovush
     bermaydi — u faqat "bu yerda unli turibdi" degan belgi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">한국 사람</p>
  <p class="pe-ex__rom">han-guk sa-ram</p>
  <p class="pe-ex__uz">koreys (odam)</p>
</div>

<h3>7. Nega bu iyeroglif emas</h3>

<p>Farqni bir marta koʻrsangiz, boshqa adashmaysiz. <b>한자</b> (xitoy iyeroglifi)
bitta belgi bilan butun bir <em>maʼnoni</em> beradi: 韓 = "Koreya". Uni oʻqish uchun
oʻsha belgini avvaldan bilish shart. <b>한글</b> esa <em>tovushni</em> beradi: 한 —
bu "h + a + n", va siz uni hech qachon koʻrmagan boʻlsangiz ham oʻqiy olasiz.</p>

<p>Bugungi Koreyada gazeta ham, kitob ham, telefon ham deyarli butunlay Hangulda.
Iyeroglif faqat ismlarda va ilmiy matnlarda uchraydi. Ya'ni <b>Hangulni bilsangiz,
koreyscha yozilgan hamma narsani ovoz chiqarib oʻqiy olasiz</b> — maʼnosini
tushunmasangiz ham. Bu juda katta yutuq, chunki tilni oʻrganish shu yerdan boshlanadi.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">한 belgisini rasm kabi butunligicha yodlashga urinish.</p>
  <p class="pe-good">한 ni har doim harflarga ajrating: <b>ㅎ + ㅏ + ㄴ</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">아 ni "nga" deb oʻqish.</p>
  <p class="pe-good">Boshdagi <b>ㅇ jim</b>. 아 = "a". ㅇ faqat 받침 boʻlgandagina
     "ng" boʻladi: 강 = "kang".</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Harflarni qatorga yozish: ㅎㅏㄴㄱㅜㄱ</p>
  <p class="pe-good">Bloklarga yigʻish: <b>한국</b>. Koreyscha bir qatorga yozilgan
     harflar toʻplami — soʻz emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">"Avval hamma soʻzni yodlab, keyin harflarni oʻrganaman."</p>
  <p class="pe-good">Aksincha. Avval 24 ta harf — bu bir hafta. Undan keyin har bir
     yangi soʻz oʻz-oʻzidan oʻqiladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Hangulda nechta asosiy undosh va nechta asosiy unli bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>14 ta undosh (자음) va 10 ta unli (모음)</strong> —
    jami 24 ta harf. Qattiq undoshlar va qoʻshma unlilar shulardan yasaladi, shuning uchun
    ular alohida harf hisoblanmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>물</b> boʻgʻini qaysi harflardan tuzilgan? Har birining nomini ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ㅁ (초성) + ㅜ (중성) + ㄹ (종성)</strong>.
    ㅜ yotiq unli boʻlgani uchun ㅁ ning <em>tagiga</em> tushdi, ㄹ esa 받침 sifatida eng
    pastga joylashdi. Maʼnosi — "suv".</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     ㅂ harfiga bitta chiziq qoʻshsak, qaysi harf hosil boʻladi va tovush qanday
     oʻzgaradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ㅍ</strong> hosil boʻladi. Qoʻshimcha chiziq —
    qoʻshimcha <em>nafas</em> degani: ㅂ yumshoqroq <em>b/p</em>, ㅍ esa kuchli nafas
    bilan aytiladigan <em>p</em>. Xuddi shu qoida ㄱ→ㅋ, ㄷ→ㅌ, ㅈ→ㅊ juftliklarida ham
    ishlaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     ㄱ va ㅗ dan boʻgʻin tuzing. ㅗ ni qayerga yozasiz — oʻngga yoki tagiga?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>고</strong> — <em>tagiga</em>. ㅗ yotiq unli,
    shuning uchun undoshning ostiga tushadi. Agar ㅏ (tik unli) boʻlganida oʻngga
    yozilardi: <b>가</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     한자 va 한글 orasidagi farq nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>한자</strong> — xitoy iyerogliflari, har bir belgi
    butun <em>maʼnoni</em> bildiradi va uni oldindan bilish kerak.
    <strong>한글</strong> — alifbo, har bir harf <em>tovushni</em> bildiradi, shuning uchun
    notanish soʻzni ham oʻqib boʻladi. Bugungi koreys matnlari deyarli butunlay
    한글da.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>한글</b><span>koreys alifbosi</span></li>
  <li><b>한자</b><span>xitoy iyerogliflari</span></li>
  <li><b>자음</b><span>undosh</span></li>
  <li><b>모음</b><span>unli</span></li>
  <li><b>음절</b><span>boʻgʻin</span></li>
  <li><b>초성</b><span>boʻgʻindagi bosh undosh</span></li>
  <li><b>중성</b><span>boʻgʻindagi unli</span></li>
  <li><b>종성 / 받침</b><span>boʻgʻindagi yakuniy undosh</span></li>
  <li><b>세종대왕</b><span>Buyuk qirol Sejong — Hangul ixtirochisi</span></li>
  <li><b>훈민정음</b><span>Hangulning asl nomi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>Hangul — <b>alifbo</b>, iyeroglif emas. 24 ta asosiy harf, tamom.</li>
    <li>Undosh shakli — ogʻiz rasmi; <b>qoʻshimcha chiziq = qoʻshimcha nafas</b>
        (ㄱ→ㅋ, ㄷ→ㅌ, ㅂ→ㅍ, ㅈ→ㅊ).</li>
    <li>Unlilar osmon (ㆍ), yer (ㅡ) va inson (ㅣ) belgilaridan yasalgan.</li>
    <li>Harflar qatorga emas, <b>boʻgʻin blokiga</b> yigʻiladi:
        초성 + 중성 (+ 종성).</li>
    <li>Tik unli oʻngga (가), yotiq unli tagiga (고), 받침 har doim pastga (간).</li>
    <li>Boshdagi <b>ㅇ jim</b> — u faqat unli uchun joy ochib beradi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-2: Unlilar 1: ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ",
        "category": "korean",
        "order": 2,
        "summary": (
            "Oltita asosiy koreys unlisini yozish va talaffuz qilishni oʻrganasiz — "
            "jumladan oʻzbek tilida yoʻq ㅓ va ㅡ tovushlarini."
        ),
        "content": """
<h2>PK-2: Unlilar 1: ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ</h2>

<p>Koreys tilini oʻrganayotgan oʻzbek oʻquvchining eng koʻp qiladigan xatosi darsning
birinchi haftasida tugʻiladi: u <b>ㅓ</b> va <b>ㅗ</b> ni bir xil "o" deb oʻqiy
boshlaydi. Natijada 서울 (Seul) va 소울 bir xil eshitiladi, 저 ("men") esa 조 boʻlib
qoladi. Bugun shu oltita unlini oxirigacha ajratib olamiz — keyin butun kurs davomida
qiynalmaysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Oltita asosiy unlini yozasiz va tanib olasiz</li>
    <li>ㅓ va ㅗ ni bir-biridan ajratasiz — bu eng muhim juftlik</li>
    <li>Oʻzbek tilida umuman yoʻq boʻlgan ㅡ tovushini aytishni oʻrganasiz</li>
    <li>ㅇ bilan birga birinchi haqiqiy soʻzlarni oʻqiysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Unlini yolgʻiz yozish</span>
  <span class="pe-chip pe-chip--s">ㅇ (jim)</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">unli</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">아 어 오 우 으 이</span>
</div>

<h3>1. Oltita unli</h3>

<div class="pk-hangul">
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅏ</span>
    <span class="pk-hangul__rom">a</span>
    <span class="pk-hangul__uz">"ana" dagi <b>a</b></span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅓ</span>
    <span class="pk-hangul__rom">eo</span>
    <span class="pk-hangul__uz">"ona" dagi <b>o</b>, lablar yoyilgan</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅗ</span>
    <span class="pk-hangul__rom">o</span>
    <span class="pk-hangul__uz">"koʻz" dagi <b>oʻ</b>, lablar dumaloq</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅜ</span>
    <span class="pk-hangul__rom">u</span>
    <span class="pk-hangul__uz">"uy" dagi <b>u</b></span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅡ</span>
    <span class="pk-hangul__rom">eu</span>
    <span class="pk-hangul__uz">oʻzbekchada yoʻq — pastga qarang</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅣ</span>
    <span class="pk-hangul__rom">i</span>
    <span class="pk-hangul__uz">"ish" dagi <b>i</b></span></div>
</div>

<h3>2. Eng muhim juftlik: ㅓ va ㅗ</h3>

<p>Bu ikkalasi lotin yozuvida koʻpincha bir xil "o" deb koʻchiriladi va aynan shu narsa
oʻquvchini adashtiradi. Aslida ular oʻzbek tilida ham ikkita <b>alohida</b> tovush
sifatida bor — faqat siz ularga eʼtibor bermagansiz.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">ㅓ — lablar YOYILGAN</p>
    <p style="font-size:2rem">어</p>
    <p>Oʻzbekcha <b>o</b>: <em>ona, bola, non</em>.</p>
    <p>Lablaringiz dumaloq boʻlmaydi. Ogʻiz yarim ochiq, til pastda.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">ㅗ — lablar DUMALOQ</p>
    <p style="font-size:2rem">오</p>
    <p>Oʻzbekcha <b>oʻ</b>: <em>koʻz, oʻn, soʻz</em>.</p>
    <p>Lablaringizni oldinga chiqarib dumaloqlaysiz.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana eng qulay yoʻli: <b>ㅓ ≈ oʻzbekcha "o"</b> (ona), <b>ㅗ ≈ oʻzbekcha "oʻ"</b> (koʻz).
Oʻzbek tilida bu ikkisi allaqachon farqlanadi — <em>bor</em> va <em>boʻr</em> bir xil
soʻz emas. Koreyschada ham xuddi shunday: <b>서</b> va <b>소</b> butunlay boshqa
narsa. Qoʻlingizni lablaringizga qoʻying: ㅓ da lab qimirlamaydi, ㅗ da oldinga
chiqadi.</div>

<div class="pe-ex">
  <p class="pe-ex__ko">서울 — 소</p>
  <p class="pe-ex__rom">seo-ul — so</p>
  <p class="pe-ex__uz">Seul (poytaxt) — sigir</p>
  <p class="pe-ex__why">Birinchisida lab yoyiq, ikkinchisida dumaloq. Farq shu.</p>
</div>

<h3>3. Oʻzbekchada yoʻq tovush: ㅡ</h3>

<p>ㅡ — kursdagi eng notanish tovush, lekin uni aytish qiyin emas. Ikki qadam:</p>

<ol class="pe-steps">
  <li><b>"u"</b> deyishga tayyorlaning — til orqaga, yuqoriga koʻtariladi.</li>
  <li>Endi <b>lablaringizni yoying</b>, xuddi jilmayayotgandek, va shu holatda ovoz
      chiqaring. Chiqqan tovush — ㅡ.</li>
</ol>

<p>Boshqacha aytganda: <b>ㅡ = ㅜ, faqat lablar dumaloq emas.</b> Rus tilini
bilsangiz, bu deyarli <em>ы</em> tovushi.</p>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
ㅡ ni oʻzbekcha "i" deb aytmang. 그 ("u, oʻsha") ni "gi" desangiz, koreys quloqqa
기 ("energiya") eshitiladi. Farqi katta.</div>

<h3>4. Yozilishi — qayerga qoʻyiladi</h3>

<p>PK-1 dagi qoidani eslaysizmi? Unli shakli uning joyini aytib turadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Tik unli → oʻngga</p>
    <p>ㅏ · ㅓ · ㅣ</p>
    <p style="font-size:1.5rem">아 · 어 · 이</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Yotiq unli → tagiga</p>
    <p>ㅗ · ㅜ · ㅡ</p>
    <p style="font-size:1.5rem">오 · 우 · 으</p>
  </div>
</div>

<p>Diqqat qiling: yuqoridagi oltita blokda ham chapda yoki tepada <b>ㅇ</b> turibdi.
Koreys yozuvida <b>boʻgʻin hech qachon yolgʻiz unlidan boshlanmaydi</b> — kvadratcha
toʻlishi kerak. Shuning uchun tovushi yoʻq ㅇ qoʻyiladi. U hech narsa
oʻqilmaydi.</p>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>아</b> = "a", <b>오</b> = "o", <b>이</b> = "i". Boshdagi ㅇ ni <em>hech qachon</em>
oʻqimang.</div>

<h3>5. Yozish tartibi</h3>

<p>Hangul har doim <b>yuqoridan pastga, chapdan oʻngga</b> yoziladi. Har bir unli uchun:</p>

<ul>
  <li><b>ㅏ</b> — avval uzun tik chiziq, keyin oʻngdagi qisqa chiziqcha.</li>
  <li><b>ㅓ</b> — avval chapdagi qisqa chiziqcha, keyin uzun tik chiziq.</li>
  <li><b>ㅗ</b> — avval kalta tik chiziqcha, keyin ostidagi uzun yotiq chiziq.</li>
  <li><b>ㅜ</b> — avval uzun yotiq chiziq, keyin ostidagi kalta tik chiziqcha.</li>
  <li><b>ㅡ</b> — bitta uzun yotiq chiziq.</li>
  <li><b>ㅣ</b> — bitta uzun tik chiziq.</li>
</ul>

<h3>6. Birinchi soʻzlar</h3>

<p>Faqat ㅇ va shu oltita unli bilan ham haqiqiy koreyscha soʻzlar yoziladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">아이</p>
  <p class="pe-ex__rom">a-i</p>
  <p class="pe-ex__uz">bola</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">오이</p>
  <p class="pe-ex__rom">o-i</p>
  <p class="pe-ex__uz">bodring</p>
  <p class="pe-ex__why">Lablar dumaloq — <b>oʻ-i</b>, "a-i" emas.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아우</p>
  <p class="pe-ex__rom">a-u</p>
  <p class="pe-ex__uz">uka, singil (kichik aka-uka)</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">오</p>
  <p class="pe-ex__rom">o</p>
  <p class="pe-ex__uz">besh (5)</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">어 va 오 ni bir xil "o" deb oʻqish.</p>
  <p class="pe-good"><b>어</b> = oʻzbekcha "<b>o</b>" (ona), <b>오</b> = oʻzbekcha
     "<b>oʻ</b>" (koʻz). Lablarga qarang.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">으 ni "i" deb aytish.</p>
  <p class="pe-good">"u" deyishga tayyorlaning, lekin lablarni yoying. <b>으</b> —
     ㅜ ning dumaloqsiz shakli.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">아 ni "nga" yoki "ang" deb oʻqish.</p>
  <p class="pe-good">Boshdagi <b>ㅇ jim</b>. 아 = "a", tamom.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Unlini yolgʻiz yozish: ㅏ, ㅜ.</p>
  <p class="pe-good">Boʻgʻinda har doim undosh oʻrni toʻladi: <b>아</b>, <b>우</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>어</b> va <b>오</b> ni ovoz chiqarib ayting. Ularni ajratadigan asosiy belgi
     nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Lablar.</strong> 어 da lablar yoyilgan
    (oʻzbekcha "ona" dagi <em>o</em>), 오 da esa dumaloqlanib oldinga chiqadi
    (oʻzbekcha "koʻz" dagi <em>oʻ</em>).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu soʻzni oʻqing: <b>오이</b>. Maʼnosi nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>oʻ-i — "bodring"</strong>. Ikkala blokda ham
    boshdagi ㅇ jim, shuning uchun faqat ikkita unli eshitiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega <b>ㅜ</b> undoshning tagiga, <b>ㅣ</b> esa oʻngiga yoziladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>ㅜ yotiq</strong> unli — uning uzun chizigʻi
    gorizontal, shuning uchun pastga tushadi (우). <strong>ㅣ tik</strong> unli — uzun
    chizigʻi vertikal, shuning uchun oʻngga chiqadi (이). Shakl joyni aytib
    turadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     "a-u" tovushlarini Hangulda yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>아우</strong> — ikkita blok. Birinchisida ㅇ+ㅏ
    (unli tik, oʻngda), ikkinchisida ㅇ+ㅜ (unli yotiq, tagida). Maʼnosi — "uka,
    singil".</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Jasur <b>그</b> ni "gi" deb oʻqidi. Xato qayerda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>U <strong>ㅡ ni ㅣ bilan almashtirdi</strong>. 그 ning
    unlisi — ㅡ: "u" holatidagi til, lekin yoyilgan lab. "gi" deb oʻqilsa, bu allaqachon
    boshqa soʻz — <b>기</b>. Jasur lablarini yoyib, "u" ni dumaloqsiz aytib
    koʻrishi kerak.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아이</b><span>bola</span></li>
  <li><b>오이</b><span>bodring</span></li>
  <li><b>아우</b><span>uka, singil</span></li>
  <li><b>오</b><span>besh (5)</span></li>
  <li><b>이</b><span>tish; ikki (2)</span></li>
  <li><b>서울</b><span>Seul</span></li>
  <li><b>소</b><span>sigir</span></li>
  <li><b>모음</b><span>unli</span></li>
  <li><b>발음</b><span>talaffuz</span></li>
  <li><b>입술</b><span>lab</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>ㅏ</b> = a · <b>ㅓ</b> = oʻzbekcha "o" · <b>ㅗ</b> = oʻzbekcha "oʻ" ·
        <b>ㅜ</b> = u · <b>ㅣ</b> = i.</li>
    <li><b>ㅓ va ㅗ farqi — lab.</b> Yoyiq lab → ㅓ, dumaloq lab → ㅗ.</li>
    <li><b>ㅡ</b> = ㅜ ning lablari yoyilgan shakli. Oʻzbekchada bu tovush yoʻq.</li>
    <li>Tik unlilar (ㅏ ㅓ ㅣ) oʻngga, yotiq unlilar (ㅗ ㅜ ㅡ) tagiga.</li>
    <li>Unli yolgʻiz turolmaydi — oldiga jim <b>ㅇ</b> qoʻyiladi: 아, 오, 이.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-3: Unlilar 2: yotlashgan ㅑ ㅕ ㅛ ㅠ va qoʻshma unlilar ㅐ ㅔ ㅘ ㅚ ㅢ",
        "category": "korean",
        "order": 3,
        "summary": (
            "Bitta qoʻshimcha chiziqcha unliga “y” qoʻshadi, ikkita unlining "
            "birikmasi esa yangi tovush beradi. Hangul unlilar tizimi shu bilan tugaydi."
        ),
        "content": """
<h2>PK-3: Unlilar 2: yotlashgan ㅑ ㅕ ㅛ ㅠ va qoʻshma unlilar ㅐ ㅔ ㅘ ㅚ ㅢ</h2>

<p>Yaxshi xabar: bugun <b>yangi harf yoʻq</b>. Bugun oʻrganadiganingizning hammasi
PK-2 dagi oltita unlidan yasaladi — biriga chiziqcha qoʻshiladi, ikkinchisi esa
ikkitasini yonma-yon qoʻyish orqali hosil boʻladi. Shu darsdan keyin Hangul unlilar
tizimi <b>toʻliq</b> tugaydi va siz istalgan koreyscha unlini oʻqiy olasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Qoʻshimcha chiziqcha unliga "y" qoʻshishini koʻrasiz: ㅏ→ㅑ, ㅓ→ㅕ, ㅗ→ㅛ, ㅜ→ㅠ</li>
    <li>ㅐ va ㅔ ni yozasiz — va nega ularni koreyslar bir xil aytishini bilib olasiz</li>
    <li>Ikkita unlidan qoʻshma unli yasaysiz: ㅗ+ㅏ=ㅘ, ㅜ+ㅓ=ㅝ, ㅜ+ㅣ=ㅟ</li>
    <li>의 ning uch xil oʻqilishini oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki yasash usuli</span>
  <span class="pe-chip pe-chip--o">unli + chiziqcha</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">y + unli</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">unli + unli</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">qoʻshma unli</span>
</div>

<h3>1. Qoʻshimcha chiziqcha = "y"</h3>

<p>Undoshlarda chiziq nafas qoʻshgan edi. Unlilarda esa <b>chiziqcha "y" tovushini
qoʻshadi</b>. Boshqa hech narsa oʻzgarmaydi.</p>

<div class="pk-hangul">
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅑ</span>
    <span class="pk-hangul__rom">ya</span>
    <span class="pk-hangul__uz">ㅏ + chiziqcha</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅕ</span>
    <span class="pk-hangul__rom">yeo</span>
    <span class="pk-hangul__uz">ㅓ + chiziqcha — "yo" (yosh)</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅛ</span>
    <span class="pk-hangul__rom">yo</span>
    <span class="pk-hangul__uz">ㅗ + chiziqcha — "yoʻ"</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅠ</span>
    <span class="pk-hangul__rom">yu</span>
    <span class="pk-hangul__uz">ㅜ + chiziqcha</span></div>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>ㅕ va ㅛ</b> — bu yana oʻsha ㅓ/ㅗ juftligi, faqat "y" bilan. <b>여</b> =
oʻzbekcha "yo" (<em>yosh</em>), <b>요</b> = "yoʻ" (lablar dumaloq). 여기 ("bu yer") ni
요기 deb aytmang.</div>

<p>ㅡ va ㅣ ning yotlashgan shakli <b>yoʻq</b> — chunki "y+ы" va "y+i" tovushlari
amalda aytilmaydi. Ya'ni yodlash kerak boʻlgan yotlashgan unli atigi toʻrtta.</p>

<h3>2. ㅐ va ㅔ — yozilishi boshqa, tovushi bir xil</h3>

<p>Bu ikkalasi ㅏ+ㅣ va ㅓ+ㅣ birikmasidan kelib chiqqan:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">ㅐ = ㅏ + ㅣ</p>
    <p style="font-size:2rem">애</p>
    <p>Yozilishi: ㅏ ning oʻngiga yana bitta tik chiziq.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">ㅔ = ㅓ + ㅣ</p>
    <p style="font-size:2rem">에</p>
    <p>Yozilishi: ㅓ ning oʻngiga yana bitta tik chiziq.</p>
  </div>
</div>

<p>Eski koreys tilida ular ikki xil aytilardi. <b>Bugungi tilda esa deyarli barcha
koreys ularni bir xil — oʻzbekcha "e" kabi talaffuz qiladi.</b> Ya'ni siz uchun
talaffuzda muammo yoʻq; muammo faqat <em>yozuvda</em>: 개 ("it") va 게 ("qisqichbaqa")
bir xil eshitiladi, lekin har xil yoziladi.</p>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Yangi soʻz oʻrganganda ㅐ yoki ㅔ ekanini <b>koʻz bilan</b> yodlang, quloq bilan emas.
Koreyslarning oʻzi ham bu ikkisini yozuvda adashtiradi — imlo tekshiruvi shu yerda eng
koʻp ishlaydi.</div>

<p>Ularning yotlashgan shakllari ham bor: <b>ㅒ</b> (yae) va <b>ㅖ</b> (ye).
예 ("ha") — eng koʻp uchraydigani.</p>

<h3>3. Qoʻshma unlilar — ikkita unli qoʻshiladi</h3>

<p>Bu yerda mantiq juda sodda: <b>yotiq unli + tik unli</b>, ikkalasi ham oʻqiladi va bir
tovushga qoʻshilib ketadi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Birikma</th><th>Natija</th><th>Oʻqilishi</th><th>Misol</th></tr>
  <tr><td class="pk-stem">ㅗ + ㅏ</td><td class="pk-res">ㅘ</td><td class="pk-end">wa</td>
      <td class="pk-uz">과일 — meva</td></tr>
  <tr><td class="pk-stem">ㅗ + ㅐ</td><td class="pk-res">ㅙ</td><td class="pk-end">wae</td>
      <td class="pk-uz">왜 — nega</td></tr>
  <tr><td class="pk-stem">ㅗ + ㅣ</td><td class="pk-res">ㅚ</td><td class="pk-end">oe (≈ we)</td>
      <td class="pk-uz">외국 — chet el</td></tr>
  <tr><td class="pk-stem">ㅜ + ㅓ</td><td class="pk-res">ㅝ</td><td class="pk-end">wo</td>
      <td class="pk-uz">뭐 — nima</td></tr>
  <tr><td class="pk-stem">ㅜ + ㅔ</td><td class="pk-res">ㅞ</td><td class="pk-end">we</td>
      <td class="pk-uz">웨딩 — toʻy (wedding)</td></tr>
  <tr><td class="pk-stem">ㅜ + ㅣ</td><td class="pk-res">ㅟ</td><td class="pk-end">wi</td>
      <td class="pk-uz">위 — yuqori, ust</td></tr>
  <tr><td class="pk-stem">ㅡ + ㅣ</td><td class="pk-res">ㅢ</td><td class="pk-end">ui</td>
      <td class="pk-uz">의사 — shifokor</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Qoʻshma unlilarni yodlamang — <b>ajratib oʻqing</b>. ㅘ ni koʻrsangiz, ichida ㅗ va ㅏ
turganini koʻring: "oʻ" + "a" tez aytilsa, oʻz-oʻzidan "wa" chiqadi. Oʻzbekchada ham
"suv" soʻzidagi <em>u</em> shunday yarim-undoshga aylanadi. Ya'ni bu yerda yangi tovush
emas, tezlik masalasi.</div>

<p>Bugungi tilda <b>ㅙ, ㅚ, ㅞ</b> uchalasi ham amalda deyarli bir xil — "we" kabi
oʻqiladi. Yana yozuvda ajratish kerak, talaffuzda esa qiynalmaysiz.</p>

<h3>4. 의 — uch xil oʻqiladigan yagona unli</h3>

<p>ㅢ Hangulda alohida turadi, chunki uning oʻqilishi <b>soʻzdagi joyiga</b> bogʻliq.
Uchta holat bor:</p>

<div class="pk-say">
  <span class="pk-say__from">의사</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[의사]</span>
  <span class="pk-say__why">soʻz boshida — toʻliq "ui"</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">회의</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[회이]</span>
  <span class="pk-say__why">soʻz oʻrtasida yoki oxirida — oddiy "i"</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">저의 책</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[저에 책]</span>
  <span class="pk-say__why">egalik qoʻshimchasi boʻlsa — "e"</span>
</div>

<p>Uchinchi holat — 의 qoʻshimchasi "…ning" maʼnosini bergani. Uni PK-13 darsida
oʻrganamiz; hozircha shuni bilib qoʻying: <em>qoʻshimcha boʻlsa "e" deb oʻqiladi</em>.</p>

<h3>5. Soʻzlar</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">우유</p>
  <p class="pe-ex__rom">u-yu</p>
  <p class="pe-ex__uz">sut</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">여우</p>
  <p class="pe-ex__rom">yeo-u</p>
  <p class="pe-ex__uz">tulki</p>
  <p class="pe-ex__why">여 — lablar yoyiq. "yoʻ-u" emas, "yo-u".</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">왜?</p>
  <p class="pe-ex__rom">wae</p>
  <p class="pe-ex__uz">Nega?</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">뭐?</p>
  <p class="pe-ex__rom">mwo</p>
  <p class="pe-ex__uz">Nima?</p>
  <p class="pe-ex__why">ㅁ + ㅝ — kundalik nutqda eng koʻp ishlatiladigan soʻzlardan.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">여 va 요 ni bir xil oʻqish.</p>
  <p class="pe-good"><b>여</b> = "yo" (lab yoyiq), <b>요</b> = "yoʻ" (lab dumaloq) —
     xuddi ㅓ/ㅗ juftligidagidek.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">ㅘ ni yangi, mustaqil harf deb yodlash.</p>
  <p class="pe-good">Ichini koʻring: <b>ㅗ + ㅏ</b>. Tez aytsangiz "wa" chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">의사 ni "isa" deb oʻqish.</p>
  <p class="pe-good">Soʻz <b>boshida</b> ㅢ toʻliq oʻqiladi: <b>[의사]</b>. "i" ga
     faqat soʻz oʻrtasida yoki oxirida aylanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">개 va 게 ni bir xil yozish, chunki bir xil eshitiladi.</p>
  <p class="pe-good">Talaffuz bir xil, <b>imlo boshqa</b>. Har bir soʻzda ㅐ yoki ㅔ
     ekanini koʻz bilan yodlang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     ㅜ ga bitta chiziqcha qoʻshsak, qaysi harf chiqadi va u qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ㅠ — "yu"</strong>. Unlilarda qoʻshimcha
    chiziqcha har doim <em>y</em> tovushini qoʻshadi, boshqa hech narsani
    oʻzgartirmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>ㅝ</b> qaysi ikkita unlidan yasalgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ㅜ + ㅓ</strong>. "u" va oʻzbekcha "o" ni tez
    ketma-ket aytsangiz, "wo" chiqadi — 뭐 ("nima") dagi tovush.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>여우</b> ni oʻqing va maʼnosini ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>"yo-u" — tulki</strong>. Birinchi blokda ㅇ+ㅕ,
    ikkinchisida ㅇ+ㅜ. Lablar birinchi boʻgʻinda yoyilgan boʻlishi kerak.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nega <b>ㅡ</b> va <b>ㅣ</b> ning yotlashgan (chiziqchali) shakli yoʻq?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>"y" tovushi ㅣ ning oʻziga juda
    yaqin</strong> — "y+i" amalda oddiy "i" boʻlib chiqadi, "y+ы" esa aytilmaydi. Shuning
    uchun yotlashgan unlilar atigi toʻrtta: ㅑ ㅕ ㅛ ㅠ.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Afsona <b>회의</b> ni "hoe-ui" deb oʻqidi. Toʻgʻrimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Toʻliq toʻgʻri emas. Bu yerda <strong>의 soʻz oxirida
    turibdi</strong>, shuning uchun oddiy <b>[이]</b> deb oʻqiladi:
    <strong>[회이]</strong> — "hoe-i". Maʼnosi — "yigʻilish".</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>우유</b><span>sut</span></li>
  <li><b>여우</b><span>tulki</span></li>
  <li><b>왜</b><span>nega</span></li>
  <li><b>뭐</b><span>nima</span></li>
  <li><b>위</b><span>yuqori, ust</span></li>
  <li><b>의사</b><span>shifokor</span></li>
  <li><b>회의</b><span>yigʻilish</span></li>
  <li><b>과일</b><span>meva</span></li>
  <li><b>외국</b><span>chet el</span></li>
  <li><b>예</b><span>ha</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>Unliga <b>qoʻshimcha chiziqcha = "y"</b>: ㅏ→ㅑ, ㅓ→ㅕ, ㅗ→ㅛ, ㅜ→ㅠ.</li>
    <li><b>ㅐ va ㅔ</b> bugungi tilda bir xil ("e") aytiladi, lekin har xil yoziladi.</li>
    <li>Qoʻshma unli = <b>yotiq unli + tik unli</b>: ㅗ+ㅏ=ㅘ, ㅜ+ㅓ=ㅝ, ㅜ+ㅣ=ㅟ.</li>
    <li>Qoʻshma unlini yodlamang — <b>ichidagi ikkita unlini koʻring</b> va tez ayting.</li>
    <li><b>의</b>: soʻz boshida "ui", oʻrtasida/oxirida "i", qoʻshimcha boʻlsa "e".</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-4: Undoshlar 1: ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ",
        "category": "korean",
        "order": 4,
        "summary": (
            "Sakkizta oddiy undosh. Ular soʻz boshida jarangsiz, unlilar orasida esa "
            "jarangli boʻladi — oʻzbek quloqqa notanish, lekin oson qoida."
        ),
        "content": """
<h2>PK-4: Undoshlar 1: ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ</h2>

<p>Koreyscha oʻrganayotgan oʻzbek oʻquvchi tez-tez shunday deydi: "Men <b>고기</b> ni
<em>gogi</em> deb oʻqidim, koreys esa <em>kogi</em> dedi. Kim toʻgʻri?" — Ikkalasi ham.
Chunki koreys tilida <b>ㄱ, ㄷ, ㅂ, ㅈ</b> harflari "k" ham, "g" ham emas; ular ikkovining
orasida turadi va <em>soʻzdagi joyiga qarab</em> oʻzgaradi. Bugun shu sirni ochamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Sakkizta oddiy undoshni yozasiz va tanib olasiz</li>
    <li>Nega bitta harf goh "k", goh "g" boʻlishini tushunasiz</li>
    <li>ㄹ ni — na "r", na "l" boʻlgan tovushni — toʻgʻri aytasiz</li>
    <li>Endi haqiqiy koreyscha soʻzlarni mustaqil oʻqiy olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Jaranglashish qoidasi</span>
  <span class="pe-chip pe-chip--s">soʻz boshida → k, t, p, ch</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">unlilar orasida → g, d, b, j</span>
</div>

<h3>1. Sakkizta harf</h3>

<div class="pk-hangul">
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㄱ</span>
    <span class="pk-hangul__rom">g / k</span>
    <span class="pk-hangul__uz">til orqasi</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㄴ</span>
    <span class="pk-hangul__rom">n</span>
    <span class="pk-hangul__uz">oʻzbekcha n</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㄷ</span>
    <span class="pk-hangul__rom">d / t</span>
    <span class="pk-hangul__uz">til uchi</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㄹ</span>
    <span class="pk-hangul__rom">r / l</span>
    <span class="pk-hangul__uz">ikkovining orasi</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅁ</span>
    <span class="pk-hangul__rom">m</span>
    <span class="pk-hangul__uz">oʻzbekcha m</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅂ</span>
    <span class="pk-hangul__rom">b / p</span>
    <span class="pk-hangul__uz">lablar</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅅ</span>
    <span class="pk-hangul__rom">s</span>
    <span class="pk-hangul__uz">ㅣ oldida "sh"</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">ㅇ</span>
    <span class="pk-hangul__rom">– / ng</span>
    <span class="pk-hangul__uz">boshda jim</span></div>
</div>

<p>Ulardan toʻrttasi — <b>ㄴ, ㅁ, ㅅ, ㅇ</b> — sizga tanish va hech qanday muammo
tugʻdirmaydi. Qiyini uchtasi: <b>ㄱ, ㄷ, ㅂ</b> va alohida holdagi <b>ㄹ</b>.</p>

<h3>2. Nega 고기 goh "kogi", goh "gogi"</h3>

<p>Oʻzbek tilida <em>k</em> va <em>g</em> — ikki boshqa harf, ikki boshqa maʼno:
<b>kul</b> va <b>gul</b> bir xil soʻz emas. Koreys tilida esa bunday emas.
Koreys uchun <b>ㄱ bitta tovush</b>, va u avtomatik ravishda oʻzgaradi:</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">SOʻZ BOSHIDA</p>
    <p class="pk-batchim__form">ㄱ → <b>k</b></p>
    <p>고기 → [<b>k</b>ogi]</p>
    <p>가방 → [<b>k</b>abang]</p>
    <p>Ovoz paychalari tebranmaydi.</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">UNLILAR ORASIDA</p>
    <p class="pk-batchim__form">ㄱ → <b>g</b></p>
    <p>고기 → [ko<b>g</b>i]</p>
    <p>가구 → [ka<b>g</b>u]</p>
    <p>Ovoz paychalari tebranadi.</p>
  </div>
</div>

<p>Shuning uchun <b>고기</b> ("goʻsht") aslida <b>[kogi]</b> — birinchi ㄱ "k", ikkinchisi
"g". Bitta soʻzda bitta harf ikki xil eshitiladi va koreys buni <em>sezmaydi</em> ham.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">가구</p>
  <p class="pe-ex__rom">[ka-gu]</p>
  <p class="pe-ex__uz">mebel</p>
  <p class="pe-ex__why">Ikkala ㄱ bir xil harf, lekin birinchisi "k", ikkinchisi "g".</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">바다</p>
  <p class="pe-ex__rom">[pa-da]</p>
  <p class="pe-ex__uz">dengiz</p>
  <p class="pe-ex__why">ㅂ soʻz boshida "p", ㄷ unlilar orasida "d".</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu qoida siz uchun notanish, chunki oʻzbekchada <em>k/g</em>, <em>t/d</em>, <em>p/b</em>
maʼnoni ajratadi. Koreyschada esa ajratmaydi — u yerda maʼnoni <b>nafas</b> ajratadi
(PK-5 darsi). Amaliy xulosa: <b>soʻz boshida jarangsizroq ayting</b>. Agar 부산 ni
"Busan" desangiz ham tushunishadi, lekin koreys "Pusan" ga yaqinroq aytadi.</div>

<h3>3. ㄹ — na "r", na "l"</h3>

<p>ㄹ koreys tilidagi eng oʻziga xos tovush. Uni aytish uchun til uchi <b>tanglayga bir
marta tegib oʻtadi</b> — urish kabi, ushlab turmaydi. Joyiga qarab u ikki xil
eshitiladi:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Unlilar orasida → "r" ga yaqin</p>
    <p style="font-size:1.5rem">우리 · 다리 · 나라</p>
    <p>Til bir marta urib oʻtadi. Oʻzbekcha <em>r</em> dan yumshoqroq, titramaydi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Boʻgʻin oxirida → "l" ga yaqin</p>
    <p style="font-size:1.5rem">물 · 서울 · 딸</p>
    <p>Til tanglayda <em>qoladi</em>, oʻzbekcha <em>l</em> kabi.</p>
  </div>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Oʻzbekcha <b>r</b> ni titratib aytmang ("rrr"). Koreys ㄹ — bitta qisqa urish. 우리
("biz") da til faqat bir marta tegadi.</div>

<h3>4. ㅅ va ㅇ ning oʻziga xosligi</h3>

<p><b>ㅅ</b> odatda oddiy "s". Lekin <b>ㅣ, ㅑ, ㅕ, ㅛ, ㅠ</b> unlilaridan oldin u
avtomatik "sh" ga aylanadi:</p>

<div class="pk-say">
  <span class="pk-say__from">시</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[shi]</span>
  <span class="pk-say__why">ㅣ oldida ㅅ yumshaydi</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">사</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[sa]</span>
  <span class="pk-say__why">ㅏ oldida oddiy "s"</span>
</div>

<p><b>ㅇ</b> esa ikki yuzli harf: boʻgʻin <em>boshida</em> u butunlay jim, boʻgʻin
<em>oxirida</em> (받침 boʻlganda) esa "ng" tovushini beradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">강 — 아</p>
  <p class="pe-ex__rom">[kang] — [a]</p>
  <p class="pe-ex__uz">daryo — (undov)</p>
  <p class="pe-ex__why">Birinchisida ㅇ pastda — "ng". Ikkinchisida chapda — jim.</p>
</div>

<h3>5. Endi oʻqiy olasiz</h3>

<p>Sakkizta undosh va oʻn unli — bu allaqachon koreys soʻzlarining koʻpini oʻqishga
yetadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Soʻz</th><th>Harflar</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">나라</td><td class="pk-stem">ㄴㅏ + ㄹㅏ</td>
      <td class="pk-end">[na-ra]</td><td class="pk-uz">davlat</td></tr>
  <tr><td class="pk-res">사람</td><td class="pk-stem">ㅅㅏ + ㄹㅏㅁ</td>
      <td class="pk-end">[sa-ram]</td><td class="pk-uz">odam</td></tr>
  <tr><td class="pk-res">구름</td><td class="pk-stem">ㄱㅜ + ㄹㅡㅁ</td>
      <td class="pk-end">[ku-reum]</td><td class="pk-uz">bulut</td></tr>
  <tr><td class="pk-res">가방</td><td class="pk-stem">ㄱㅏ + ㅂㅏㅇ</td>
      <td class="pk-end">[ka-bang]</td><td class="pk-uz">sumka</td></tr>
  <tr><td class="pk-res">이름</td><td class="pk-stem">ㅇㅣ + ㄹㅡㅁ</td>
      <td class="pk-end">[i-reum]</td><td class="pk-uz">ism</td></tr>
  <tr><td class="pk-res">물</td><td class="pk-stem">ㅁㅜㄹ</td>
      <td class="pk-end">[mul]</td><td class="pk-uz">suv</td></tr>
  <tr><td class="pk-res">눈</td><td class="pk-stem">ㄴㅜㄴ</td>
      <td class="pk-end">[nun]</td><td class="pk-uz">koʻz; qor</td></tr>
  <tr><td class="pk-res">어머니</td><td class="pk-stem">ㅇㅓ + ㅁㅓ + ㄴㅣ</td>
      <td class="pk-end">[o-mo-ni]</td><td class="pk-uz">ona</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Sherbek shu jadvalni yopib, faqat chap ustunga qarab oʻqib chiqdi — sakkiztadan
oltitasini toʻgʻri oʻqidi. Siz ham shunday qiling: <b>oldin oʻqing, keyin
tekshiring</b>. Hangulda bu ishlaydi, chunki yozilgani aynan oʻqiladi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">부산 ni "Busan" deb, kuchli <em>b</em> bilan aytish.</p>
  <p class="pe-good">Soʻz boshida ㅂ <b>jarangsiz</b>: [pu-san] ga yaqinroq.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">우리 dagi ㄹ ni titratib "urrri" deyish.</p>
  <p class="pe-good">Til <b>bir marta</b> urib oʻtadi: [u-ri], yengil va qisqa.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">시 ni "si" deb oʻqish.</p>
  <p class="pe-good">ㅣ oldida ㅅ yumshaydi: <b>[shi]</b>. 시간 = [shi-gan].</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">강 ni "ka" deb, oxiridagi ㅇ ni tashlab yuborish.</p>
  <p class="pe-good">받침 holatidagi ㅇ — <b>"ng"</b>: [kang]. U jim emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>고기</b> soʻzidagi ikkita ㄱ nega har xil eshitiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>birinchisi soʻz boshida</strong> (jarangsiz
    — "k"), <strong>ikkinchisi ikkita unli orasida</strong> (jarangli — "g"). Natijada
    <b>[kogi]</b>. Koreys uchun bu bitta tovush, harf ham bitta.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>사람</b> ni harflarga ajrating va oʻqing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>사 = ㅅ + ㅏ · 람 = ㄹ + ㅏ + ㅁ</strong> →
    <b>[sa-ram]</b>, "odam". ㄹ unlilar orasida, shuning uchun "r" ga yaqin.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>물</b> va <b>우리</b> dagi ㄹ bir xil eshitiladimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Yoʻq. <strong>물</strong> da ㄹ boʻgʻin oxirida —
    oʻzbekcha <em>l</em> kabi: [mul]. <strong>우리</strong> da esa ikkita unli orasida —
    <em>r</em> ga yaqin: [u-ri]. Harf bitta, joyi boshqa.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     "ka-bang" tovushlarini Hangulda yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>가방</strong> — 가 (ㄱ+ㅏ) + 방 (ㅂ+ㅏ+ㅇ).
    Oxiridagi ㅇ 받침 boʻlgani uchun "ng" beradi. Maʼnosi — "sumka".</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Dilnoza <b>시간</b> ni "si-gan" deb oʻqidi. Nimani tuzatish kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchi boʻgʻinni: <strong>ㅅ + ㅣ = [shi]</strong>, "si"
    emas. ㅅ harfi ㅣ va yotlashgan unlilardan oldin har doim yumshaydi. Toʻgʻrisi —
    <b>[shi-gan]</b>, "vaqt". Ikkinchi boʻgʻindagi "g" esa toʻgʻri, chunki ㄱ unlilar
    orasida turibdi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>사람</b><span>odam</span></li>
  <li><b>나라</b><span>davlat</span></li>
  <li><b>바다</b><span>dengiz</span></li>
  <li><b>가방</b><span>sumka</span></li>
  <li><b>이름</b><span>ism</span></li>
  <li><b>물</b><span>suv</span></li>
  <li><b>눈</b><span>koʻz; qor</span></li>
  <li><b>어머니</b><span>ona</span></li>
  <li><b>우리</b><span>biz</span></li>
  <li><b>시간</b><span>vaqt</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>ㄱ ㄷ ㅂ</b> — soʻz boshida jarangsiz (k, t, p), unlilar orasida jarangli
        (g, d, b). Bitta harf, ikki koʻrinish.</li>
    <li>Koreyschada <em>k/g</em> farqi maʼnoni <b>ajratmaydi</b> — oʻzbekchadan asosiy
        farq shu.</li>
    <li><b>ㄹ</b>: unlilar orasida "r" ga, boʻgʻin oxirida "l" ga yaqin. Titratmang.</li>
    <li><b>ㅅ</b> ㅣ va ㅑㅕㅛㅠ oldida "sh" ga aylanadi: 시 = [shi].</li>
    <li><b>ㅇ</b> boshda jim, 받침 boʻlganda "ng": 아 = [a], 강 = [kang].</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-5: Undoshlar 2: ㅈ va nafasli ㅊ ㅋ ㅌ ㅍ ㅎ",
        "category": "korean",
        "order": 5,
        "summary": (
            "Qoʻshimcha chiziq — qoʻshimcha nafas. Nafasli undoshlarni oʻrganib, "
            "Hangulning 14 ta undoshini toʻliq yopasiz."
        ),
        "content": """
<h2>PK-5: Undoshlar 2: ㅈ va nafasli ㅊ ㅋ ㅌ ㅍ ㅎ</h2>

<p>Bir varaq qogʻozni ogʻzingiz oldiga tuting va <b>달</b> deb ayting — qogʻoz
qimirlamaydi. Endi <b>탈</b> deng — qogʻoz uchib ketadi. Mana shu <em>nafas</em>
koreys tilida ikki soʻzni ajratadi: 달 — "oy", 탈 — "niqob". Oʻzbekchada bunday farq
yoʻq, shuning uchun bu darsni ovoz chiqarib oʻqing.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ㅈ ni va uning nafasli jufti ㅊ ni oʻrganasiz</li>
    <li>ㅋ ㅌ ㅍ nafasli undoshlarini ㄱ ㄷ ㅂ dan ajratasiz</li>
    <li>ㅎ ning ikki xil xatti-harakatini koʻrasiz</li>
    <li>14 ta undoshni toʻliq yopib, istalgan koreyscha soʻzni oʻqiy olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Nafas qoidasi</span>
  <span class="pe-chip pe-chip--s">oddiy undosh</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">qoʻshimcha chiziq</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">nafasli undosh</span>
</div>

<h3>1. Toʻrtta juftlik</h3>

<p>PK-1 da koʻrgan qoida shu yerda toʻliq ishga tushadi. Chapdagi harfga chiziq
qoʻshsangiz, oʻngdagisi chiqadi — va tovushga <b>kuchli nafas</b> qoʻshiladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Oddiy</th><th>Nafasli</th><th>Farqi eshitiladigan juftlik</th><th>Maʼnolari</th></tr>
  <tr><td class="pk-stem">ㄱ</td><td class="pk-end">ㅋ</td>
      <td class="pk-res">기 / 키</td><td class="pk-uz">energiya / boʻy, kalit</td></tr>
  <tr><td class="pk-stem">ㄷ</td><td class="pk-end">ㅌ</td>
      <td class="pk-res">달 / 탈</td><td class="pk-uz">oy / niqob</td></tr>
  <tr><td class="pk-stem">ㅂ</td><td class="pk-end">ㅍ</td>
      <td class="pk-res">불 / 풀</td><td class="pk-uz">olov / oʻt, yelim</td></tr>
  <tr><td class="pk-stem">ㅈ</td><td class="pk-end">ㅊ</td>
      <td class="pk-res">자다 / 차다</td><td class="pk-uz">uxlamoq / sovuq boʻlmoq</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbek tilida ham "kitob" deganda <em>k</em> dan keyin biroz nafas chiqadi — lekin bu
maʼnoni oʻzgartirmaydi, shuning uchun siz uni sezmaysiz. Koreyschada esa aynan shu nafas
<b>soʻzni almashtiradi</b>. PK-4 da koʻrgan k/g farqi koreys uchun ahamiyatsiz edi; bu
nafas farqi esa — hayotiy. Diqqatni shu yerga qarating.</div>

<h3>2. Qogʻoz sinovi</h3>

<p>Nafasni oʻzingiz eshitolmasangiz, koʻrishingiz mumkin. Bir varaq qogʻozni lablaringiz
oldida ushlang:</p>

<ol class="pe-steps">
  <li><b>바</b> deb ayting — qogʻoz deyarli qimirlamaydi.</li>
  <li><b>파</b> deb ayting — qogʻoz sezilarli uchadi.</li>
  <li>Xuddi shunday: 가 / 카, 다 / 타, 자 / 차.</li>
</ol>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Qogʻoz uchmasa, nafas yetarli emas. Koreys quloqqa nafassiz <b>파</b> — <b>바</b> boʻlib
eshitiladi. Boshida <em>ortiqcha</em> kuch bilan ayting; keyin oʻzi meʼyoriga
tushadi.</div>

<h3>3. ㅈ — oddiy, ㅊ — nafasli</h3>

<p><b>ㅈ</b> — PK-4 dagi ㄱ, ㄷ, ㅂ bilan bir guruhda: soʻz boshida "ch" ga yaqin,
unlilar orasida "j" ga aylanadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">아버지</p>
  <p class="pe-ex__rom">[a-bo-ji]</p>
  <p class="pe-ex__uz">ota</p>
  <p class="pe-ex__why">ㅈ unlilar orasida — "j". ㅂ ham jaranglashgan: "b".</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">자다</p>
  <p class="pe-ex__rom">[cha-da]</p>
  <p class="pe-ex__uz">uxlamoq</p>
  <p class="pe-ex__why">Soʻz boshida ㅈ jarangsiz — "ch" ga yaqin, lekin nafassiz.</p>
</div>

<p><b>ㅊ</b> esa har doim kuchli nafas bilan: 차 ("choy; mashina"), 친구 ("doʻst"),
축구 ("futbol"), 김치 ("kimchi").</p>

<h3>4. ㅋ ㅌ ㅍ</h3>

<p>Bu uchtasi eng oson qismi — ular <b>joyiga qarab oʻzgarmaydi</b>. Soʻzning qayerida
boʻlishidan qatʼi nazar, har doim bir xil, kuchli nafasli:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">커피</p>
  <p class="pe-ex__rom">[kho-phi]</p>
  <p class="pe-ex__uz">kofe</p>
  <p class="pe-ex__why">Ikkala undosh ham nafasli. "ko-fi" emas — ㅍ "f" emas, "p".</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">코</p>
  <p class="pe-ex__rom">[kho]</p>
  <p class="pe-ex__uz">burun</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">포도</p>
  <p class="pe-ex__rom">[pho-do]</p>
  <p class="pe-ex__uz">uzum</p>
  <p class="pe-ex__why">ㅍ nafasli, ㄷ esa unlilar orasida jaranglashib "d" boʻldi.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>ㅍ ≠ f.</b> Koreys tilida <em>f</em> tovushi umuman yoʻq. Chet soʻzlar ham ㅍ bilan
yoziladi: coffee → 커피, France → 프랑스. Shuning uchun 커피 ni "kofi" emas,
<b>"kho-phi"</b> deb ayting.</div>

<h3>5. ㅎ — ikki yuzli harf</h3>

<p><b>ㅎ</b> soʻz boshida oddiy oʻzbekcha "h": 하나 ("bir"), 형 ("aka"), 한국 ("Koreya").
Lekin unlilar orasida u <b>kuchsizlanadi va koʻpincha butunlay yoʻqoladi</b>:</p>

<div class="pk-say">
  <span class="pk-say__from">좋아요</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[조아요]</span>
  <span class="pk-say__why">ㅎ unlilar orasida tushib qoladi</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">전화</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[저놔]</span>
  <span class="pk-say__why">ㅎ zaiflashadi, ㄴ oldinga koʻchadi</span>
</div>

<p>Bundan tashqari ㅎ oddiy undosh bilan uchrashganda uni <b>nafasliga aylantiradi</b> —
bu 격음화 deb ataladi va PK-8 darsida toʻliq koʻriladi. Hozircha bitta misolni eslab
qoling:</p>

<div class="pk-say">
  <span class="pk-say__from">축하</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[추카]</span>
  <span class="pk-say__why">ㄱ + ㅎ = ㅋ</span>
</div>

<h3>6. 14 ta undosh — toʻliq roʻyxat</h3>

<p>Tabrik: shu dars bilan Hangulning barcha asosiy undoshlarini koʻrib boʻldingiz.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Guruh</th><th>Harflar</th><th>Xususiyati</th></tr>
  <tr><td class="pk-res">Oddiy</td><td class="pk-stem">ㄱ ㄷ ㅂ ㅅ ㅈ</td>
      <td class="pk-uz">soʻz boshida jarangsiz, unlilar orasida jarangli</td></tr>
  <tr><td class="pk-res">Nafasli</td><td class="pk-end">ㅋ ㅌ ㅍ ㅊ ㅎ</td>
      <td class="pk-uz">har doim kuchli nafas bilan, oʻzgarmaydi</td></tr>
  <tr><td class="pk-res">Burun tovushlari</td><td class="pk-stem">ㄴ ㅁ ㅇ</td>
      <td class="pk-uz">oʻzbekchadagidek; ㅇ boshda jim</td></tr>
  <tr><td class="pk-res">Oquvchi</td><td class="pk-stem">ㄹ</td>
      <td class="pk-uz">unlilar orasida "r", boʻgʻin oxirida "l"</td></tr>
</table></div>

<p>Qolgan beshta qattiq undosh (ㄲ ㄸ ㅃ ㅆ ㅉ) PK-6 darsida — ular ham yangi harf emas,
oddiy undoshning ikki marta yozilgan shakli.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">커피 ni "kofi" deb aytish.</p>
  <p class="pe-good">Koreyschada <b>f yoʻq</b>. ㅍ = nafasli "p": <b>[kho-phi]</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">달 va 탈 ni bir xil aytish.</p>
  <p class="pe-good">달 = nafassiz "oy", <b>탈</b> = kuchli nafasli "niqob". Qogʻoz
     sinovidan oʻtkazing.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">축하 ni "chuk-ha" deb boʻgʻinlab oʻqish.</p>
  <p class="pe-good">ㄱ va ㅎ birikib nafasli ㅋ beradi: <b>[추카]</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">아버지 ni "a-po-chi" deb, hamma undoshni jarangsiz aytish.</p>
  <p class="pe-good">Unlilar orasidagi oddiy undoshlar jaranglashadi:
     <b>[a-bo-ji]</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     ㄷ ga chiziq qoʻshsak qaysi harf chiqadi? Ikkalasi bilan bittadan soʻz ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ㅌ</strong> chiqadi. Misol: <b>달</b> ("oy",
    nafassiz) va <b>탈</b> ("niqob", nafasli). Bitta qoʻshimcha chiziq — butunlay boshqa
    soʻz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>커피</b> nima uchun "kofe" ga oʻxshamaydi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki koreys tilida <strong>f tovushi yoʻq</strong> —
    uning oʻrniga nafasli <b>ㅍ</b> ishlatiladi. Shuning uchun "coffee" → <b>커피</b>,
    oʻqilishi [kho-phi]. Xuddi shu sababdan "France" → 프랑스.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>아버지</b> dagi ㅂ va ㅈ nega jarangli eshitiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki ikkalasi ham <strong>ikkita unli orasida</strong>
    turibdi — PK-4 dagi jaranglashish qoidasi. Natijada <b>[a-bo-ji]</b>, "a-po-chi"
    emas. Bu qoida faqat oddiy undoshlarga (ㄱ ㄷ ㅂ ㅈ) tegishli; nafasli ㅋ ㅌ ㅍ ㅊ
    hech qachon oʻzgarmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>축하</b> qanday oʻqiladi va nega?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[추카]</strong>. Birinchi boʻgʻinning 받침i ㄱ
    keyingi boʻgʻindagi ㅎ bilan uchrashadi va ikkovi birikib <b>nafasli ㅋ</b> beradi. Bu
    hodisa <em>격음화</em> deb ataladi — PK-8 da toʻliq koʻramiz. Maʼnosi —
    "tabrik".</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bekzod <b>좋아요</b> ni "cho-ha-yo" deb oʻqidi. Toʻgʻrilang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Toʻgʻrisi — <strong>[조아요]</strong>, "cho-a-yo". 받침
    holatidagi <b>ㅎ ikkita unli orasida qolganda tushib ketadi</b>. Bu koreys tilida juda
    tez-tez uchraydi, chunki 좋다 ("yaxshi") — eng koʻp ishlatiladigan
    soʻzlardan.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아버지</b><span>ota</span></li>
  <li><b>친구</b><span>doʻst</span></li>
  <li><b>커피</b><span>kofe</span></li>
  <li><b>코</b><span>burun</span></li>
  <li><b>포도</b><span>uzum</span></li>
  <li><b>하나</b><span>bir (1)</span></li>
  <li><b>형</b><span>aka (oʻgʻil bola uchun)</span></li>
  <li><b>김치</b><span>kimchi</span></li>
  <li><b>축하</b><span>tabrik</span></li>
  <li><b>좋아요</b><span>yaxshi, yoqadi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>Qoʻshimcha chiziq = qoʻshimcha nafas</b>: ㄱ→ㅋ, ㄷ→ㅌ, ㅂ→ㅍ, ㅈ→ㅊ.</li>
    <li>Koreyschada nafas <b>maʼnoni ajratadi</b>: 달 (oy) ≠ 탈 (niqob).</li>
    <li>Nafasli undoshlar joyiga qarab <b>oʻzgarmaydi</b> — har doim bir xil kuchli.</li>
    <li><b>ㅍ ≠ f.</b> Koreys tilida f tovushi yoʻq: coffee → 커피.</li>
    <li><b>ㅎ</b> boshda "h", unlilar orasida yoʻqoladi (좋아요 → [조아요]), oddiy undosh
        bilan uchrashsa uni nafasliga aylantiradi (축하 → [추카]).</li>
    <li>Nafasni tekshirish uchun <b>qogʻoz sinovi</b>: 바 / 파.</li>
  </ul>
</div>
""",
    },
]
