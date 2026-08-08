# -*- coding: utf-8 -*-
"""Prime Russian — Block A, darslar 1–5 (kirill alifbosi va talaffuz).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

Bu blokda grammatika yoʻq, shuning uchun oʻqish matni ham yoʻq.
Mashqlar: practice/management/commands/_practice_pr_01_05.py (12 savoldan).

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_01_05.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Russian",
    "category": "russian",
    "description": (
        "Rus tili noldan ishonchli B2 gacha — 100 ta dars. Kirill alifbosi, kelishiklar, "
        "feʼl turlari, oʻzbekcha tushuntirish va oʻzingiz tekshiradigan mashqlar."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-1: Kirill alifbosi — siz bilgan 33 harf va sizni chalgʻitadigan yettitasi",
        "category": "russian",
        "order": 1,
        "summary": (
            "Rus alifbosining 33 harfini uchta oilaga ajratamiz: siz bilganlar, sizni "
            "chalgʻitadigan soxta doʻstlar va butunlay yangilari. Dars oxirida haqiqiy "
            "ruscha soʻzlarni oʻqiysiz."
        ),
        "content": """
<h2>PR-1: Kirill alifbosi — siz bilgan 33 harf va sizni chalgʻitadigan yettitasi</h2>

<p>Bir soʻzga qarang: <b>СТОП</b>. Oʻqidingizmi? Oʻqidingiz. Endi mana bunisiga:
<b>ТАКСИ</b>. Buni ham oʻqidingiz. Tabriklaymiz — siz allaqachon rus tilida oʻqiyapsiz.
Rus alifbosi oʻzbek oʻquvchisi uchun dunyodagi eng oson toʻsiq: oʻttiz uchta harfdan
yigirma oltitasi siz uchun begona emas. Bu darsda begonalarini bir joyga yigʻamiz va
har biriga alohida qaraymiz — chunki qiyinchilik notanish harflarda emas,
<em>tanishga oʻxshab turib boshqacha oʻqiladigan</em> harflarda.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>33 harfni uchta oilaga ajratasiz va qaysi biri xavfli ekanini bilasiz</li>
    <li>Yettita “soxta doʻst” harfni bir umrga esda saqlaysiz</li>
    <li>Oʻzbek kirilli bilan rus kirilli orasidagi aniq farqni koʻrasiz</li>
    <li>Oʻn beshdan ortiq haqiqiy ruscha soʻzni lugʻatsiz oʻqiysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Рус алфави́т</span>
  <span class="pe-chip pe-chip--s">10 unli</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">21 undosh</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--opt">2 belgi (ъ ь)</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">33 harf</span>
</div>

<h3>1. Bu dars ikki xil oʻquvchi uchun</h3>

<p>Sinfda doim ikki guruh boʻladi. Birinchisi — uyda gazeta yoki eski kitoblardan
oʻzbek kirillini oʻqiy oladiganlar. Ikkinchisi — faqat lotin alifbosida oʻqiganlar.
Ikkalangiz uchun ham bu dars kerak, lekin turli sabablarga koʻra:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Oʻzbek kirillini oʻqiy olsangiz</p>
    <p>Sizga 2-boʻlim oson tuyuladi — В, Н, Р, С, У, Х larni allaqachon toʻgʻri
    oʻqiysiz. Sizning ishingiz 3-boʻlimda: rus alifbosida <b>Ы</b> va <b>Щ</b> bor,
    oʻzbek kirillida esa yoʻq edi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Faqat lotinda oʻqigan boʻlsangiz</p>
    <p>2-boʻlim — darsning eng muhim joyi. Miyangiz <b>Р</b> ni “p”, <b>С</b> ni “s”
    emas “c”, <b>Н</b> ni “h” deb oʻqishga urinadi. Shu yettita harfni bugun
    yenging — qolgani oʻz-oʻzidan keladi.</p>
  </div>
</div>

<h3>2. Uchta oila</h3>

<p>Har bir harfni yodlash shart emas. Ularni uchta uyaga joylashtirsangiz, alifbo
bir kunda oʻrganiladi.</p>

<p><b>Birinchi oila — “bir xil”.</b> Lotinga ham oʻxshaydi, lotincha ham oʻqiladi.
Bular sizga tekin beriladi:</p>

<div class="pr-cyr">
  <div class="pr-cyr__c pr-cyr__c--same">
    <span class="pr-cyr__ch">А а</span>
    <span class="pr-cyr__rom">a</span>
    <span class="pr-cyr__uz">“ana”dagi a</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--same">
    <span class="pr-cyr__ch">К к</span>
    <span class="pr-cyr__rom">k</span>
    <span class="pr-cyr__uz">“kel”dagi k</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--same">
    <span class="pr-cyr__ch">М м</span>
    <span class="pr-cyr__rom">m</span>
    <span class="pr-cyr__uz">“men”dagi m</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--same">
    <span class="pr-cyr__ch">О о</span>
    <span class="pr-cyr__rom">o</span>
    <span class="pr-cyr__uz">“ot”dagi o</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--same">
    <span class="pr-cyr__ch">Т т</span>
    <span class="pr-cyr__rom">t</span>
    <span class="pr-cyr__uz">“tosh”dagi t</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--same">
    <span class="pr-cyr__ch">Е е</span>
    <span class="pr-cyr__rom">ye / e</span>
    <span class="pr-cyr__uz">“yer”dagi ye</span>
  </div>
</div>

<p><b>Ikkinchi oila — “soxta doʻstlar”.</b> Mana shular. Lotin harfiga oʻxshaydi,
lekin butunlay boshqa tovushni beradi. Rus tilini lotin orqali oʻrganganlar
xatolarining toʻqson foizi shu yettita harfda:</p>

<div class="pr-cyr">
  <div class="pr-cyr__c pr-cyr__c--false">
    <span class="pr-cyr__ch">В в</span>
    <span class="pr-cyr__rom">v</span>
    <span class="pr-cyr__uz">“B” emas! — “vaqt”dagi v</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--false">
    <span class="pr-cyr__ch">Н н</span>
    <span class="pr-cyr__rom">n</span>
    <span class="pr-cyr__uz">“H” emas! — “non”dagi n</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--false">
    <span class="pr-cyr__ch">Р р</span>
    <span class="pr-cyr__rom">r</span>
    <span class="pr-cyr__uz">“P” emas! — “rahmat”dagi r</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--false">
    <span class="pr-cyr__ch">С с</span>
    <span class="pr-cyr__rom">s</span>
    <span class="pr-cyr__uz">“C” emas! — “salom”dagi s</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--false">
    <span class="pr-cyr__ch">У у</span>
    <span class="pr-cyr__rom">u</span>
    <span class="pr-cyr__uz">“Y” emas! — “uy”dagi u</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--false">
    <span class="pr-cyr__ch">Х х</span>
    <span class="pr-cyr__rom">x</span>
    <span class="pr-cyr__uz">“X (iks)” emas! — “xona”dagi x</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--false">
    <span class="pr-cyr__ch">И и</span>
    <span class="pr-cyr__rom">i</span>
    <span class="pr-cyr__uz">“N” emas! — “ish”dagi i</span>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bu yettitasini bitta soxta soʻz bilan yodlang: <b>ВНРСУХИ</b> — “vnrsuxi”. Kulgili
chiqadi, lekin aynan shuning uchun esda qoladi. Har safar rus soʻzini oʻqishda
qoqilsangiz, oʻzingizdan soʻrang: bu harf ВНРСУХИ ichidami?</div>

<p><b>Uchinchi oila — “yangi shakl”.</b> Bular hech nimaga oʻxshamaydi, shuning uchun
xavfsiz: miyangiz ularni chalkashtira olmaydi. Б Г Д Ё Ж З Й Л П Ф Ц Ч Ш Щ Ъ Ы Ь Э Ю Я.
Ularni keyingi uch darsda ovozi bilan birga oʻrganamiz.</p>

<h3>3. Oʻzbek kirilli bilan aniq farq</h3>

<p>Agar oʻzbek kirillini bilsangiz, sizga faqat mana bu jadval kerak. Ikki alifbo
bir-biridan atigi olti harf bilan farq qiladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Harf</th><th>Rus tilida</th><th>Oʻzbek kirillida</th><th>Nima qilish kerak</th></tr>
  <tr><td class="pr-res">Ы ы</td><td class="pr-stem">bor</td><td>yoʻq edi</td>
      <td class="pr-uz">Yangi tovush — PR-2 da alohida oʻrganamiz</td></tr>
  <tr><td class="pr-res">Щ щ</td><td class="pr-stem">bor</td><td>yoʻq edi</td>
      <td class="pr-uz">Uzun yumshoq “sh” — PR-4 da</td></tr>
  <tr><td class="pr-res">Ў ў</td><td>yoʻq</td><td class="pr-stem">bor</td>
      <td class="pr-uz">Unutib yuboring — ruschada bunday harf yoʻq</td></tr>
  <tr><td class="pr-res">Қ қ</td><td>yoʻq</td><td class="pr-stem">bor</td>
      <td class="pr-uz">Rus tilida faqat К bor</td></tr>
  <tr><td class="pr-res">Ғ гʻ</td><td>yoʻq</td><td class="pr-stem">bor</td>
      <td class="pr-uz">Rus tilida faqat Г bor</td></tr>
  <tr><td class="pr-res">Ҳ ҳ</td><td>yoʻq</td><td class="pr-stem">bor</td>
      <td class="pr-uz">Rus tilida faqat Х bor</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Diqqat qiling: oʻzbek tilida <b>қ</b> va <b>к</b>, <b>ҳ</b> va <b>х</b> ikki xil
tovush. Rus tilida ular yoʻq — bittadan. Shuning uchun <b>ко́мната</b> (xona) dagi
к ni oʻzbekcha “қ” kabi tomoqning chuqurroq yeridan aytmang, u har doim oldingi
“k”. Bu kichik detal, lekin talaffuzingizni birdan tabiiy qiladi.</div>

<h3>4. Birinchi oʻqish — siz allaqachon biladigan soʻzlar</h3>

<p>Rus tilida yuzlab xalqaro soʻz bor, va ularning koʻpi oʻzbek tiliga ham
ruschadan kirgan. Ya'ni siz maʼnosini bilasiz — faqat oʻqishingiz kerak. Ovoz
chiqarib oʻqing:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Shahar</p>
    <p>ПАРК · БАНК · МЕТРО́ · ТЕА́ТР · МУЗЕ́Й · СТАДИО́Н</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Odamlar</p>
    <p>ДО́КТОР · СТУДЕ́НТ · ДИРЕ́КТОР · ТУРИ́СТ · А́ВТОР</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Kundalik</p>
    <p>КО́ФЕ · СПОРТ · МУ́ЗЫКА · ТЕЛЕФО́Н · КОМПЬЮ́ТЕР</p></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Э́то <span class="pe-hl pe-hl--o">рестора́н</span>.</p>
  <p class="pe-ex__rom">[э́тъ ристара́н]</p>
  <p class="pe-ex__uz">Bu — restoran.</p>
  <p class="pe-ex__why">Har bir harfni ВНРСУХИ qoidasi bilan tekshiring:
     Р = r, С = s, Н = n. “Pectopah” emas!</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Soʻz ustidagi kichik chiziqcha (<b>метро́</b>) — bu harf emas, bu <b>urgʻu belgisi</b>.
U qaysi boʻgʻinni baland aytishni koʻrsatadi. Haqiqiy ruscha matnda bu belgi
yozilmaydi — u faqat oʻquvchilar uchun kitoblarda boʻladi. Prime Russian darslarida
biz uni yozamiz, chunki ruschada urgʻu talaffuzning yarmi (PR-5 ga qarang).</div>

<h3>5. Bosma harf, kursiv va qoʻlyozma</h3>

<p>Bitta ogohlantirish, chunki bu koʻpchilikni birinchi haftada shoshirib qoʻyadi.
Kursiv (qiya) yozuvda ikkita harf butunlay boshqacha koʻrinadi:</p>

<div class="pr-say">
  <span class="pr-say__from">т</span>
  <span class="pr-say__arrow">→ kursivda →</span>
  <span class="pr-say__to"><em>т</em> (lotincha “m” ga oʻxshaydi)</span>
  <span class="pr-say__why">baribir “t” oʻqiladi</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">и</span>
  <span class="pr-say__arrow">→ kursivda →</span>
  <span class="pr-say__to"><em>и</em> (lotincha “u” ga oʻxshaydi)</span>
  <span class="pr-say__why">baribir “i” oʻqiladi</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>РЕСТОРАН → “pyestopan”</s></p>
  <p class="pe-good">РЕСТОРА́Н → <b>[ристара́н]</b> — Р = r, С = s, Н = n</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>ВОДА → “boda”</s></p>
  <p class="pe-good">ВОДА́ → <b>[вада́]</b> — В har doim <b>v</b>, hech qachon “b” emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>СУП → “syup”</s></p>
  <p class="pe-good">СУП → <b>[суп]</b> — У = <b>u</b>, lotincha “y” emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Rus alifbosida Ў, Қ, Ғ, Ҳ ham bor</s></p>
  <p class="pe-good">Yoʻq — bu toʻrt harf faqat <b>oʻzbek</b> kirillida. Ruschada 33 harf</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu soʻzni oʻqing: <b>ПАРК</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[парк]</strong> — “park”. Toʻrt harfning
    hammasi birinchi oiladan: П(p), А(a), Р(<b>r</b>!), К(k). Diqqat: Р bu yerda
    ham “r”, “p” emas — “парк” soʻzida П allaqachon “p” ni beryapti.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>СПОРТ</b> soʻzida nechta “soxta doʻst” harf bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ikkita</strong> — <b>С</b> (s) va <b>Р</b> (r).
    Qolgan uchtasi (П, О, Т) chalgʻitmaydi. Soʻz [спорт] deb oʻqiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Qaysi harf oʻzbek kirillida bor, lekin rus alifbosida <b>yoʻq</b>?
     &nbsp;Щ &nbsp;·&nbsp; Ў &nbsp;·&nbsp; Ы &nbsp;·&nbsp; Ц</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ў</strong>. Щ va Ы — aksincha, ruschada bor,
    oʻzbek kirillida yoʻq edi. Ц esa ikkalasida ham bor.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>ТУРИ́СТ</b> ni oʻqing va urgʻu qayerda ekanini ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[тури́ст]</strong> — urgʻu <b>И</b> da,
    yaʼni ikkinchi boʻgʻinda. Belgi (´) aynan shuni koʻrsatadi. У = u, Р = r,
    И = i, С = s.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi oʻqish notoʻgʻri?<br>
     а) МЕТРО́ = [митро́] &nbsp; б) БАНК = [банк] &nbsp;
     в) МУЗЕ́Й = [музэ́й] &nbsp; г) СТУДЕ́НТ = [стюдэ́нт]</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>г) notoʻgʻri.</strong> <b>У</b> — bu “u”,
    “yu” emas. Toʻgʻrisi <b>[студэ́нт]</b>. Bu ВНРСУХИ dagi У harfining eng
    koʻp uchraydigan xatosi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>алфави́т</b><span>alifbo</span></li>
  <li><b>бу́ква</b><span>harf</span></li>
  <li><b>звук</b><span>tovush</span></li>
  <li><b>сло́во</b><span>soʻz</span></li>
  <li><b>ударе́ние</b><span>urgʻu</span></li>
  <li><b>чита́ть</b><span>oʻqimoq</span></li>
  <li><b>писа́ть</b><span>yozmoq</span></li>
  <li><b>э́то</b><span>bu</span></li>
  <li><b>ру́сский язы́к</b><span>rus tili</span></li>
  <li><b>уро́к</b><span>dars</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>33 harf = 10 unli + 21 undosh + 2 belgi (ъ, ь).</li>
    <li>Uchta oila: <b>bir xil</b> (А К М О Т Е), <b>soxta doʻstlar</b> (ВНРСУХИ),
        <b>yangi shakl</b> (qolgani).</li>
    <li>Xatolarning toʻqson foizi ВНРСУХИ da. В = v, Н = n, Р = r, С = s, У = u,
        Х = x, И = i.</li>
    <li>Rus alifbosida <b>Ы</b> va <b>Щ</b> bor; oʻzbek kirillidagi <b>Ў Қ Ғ Ҳ</b> yoʻq.</li>
    <li>Urgʻu belgisi (´) — harf emas, oʻqish yordamchisi. Haqiqiy matnda yozilmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-2: Unlilar: а о у э ы va yumshatuvchi juftlar я ё ю е и",
        "category": "russian",
        "order": 2,
        "summary": (
            "Rus tilidagi 10 unli aslida 5 ta juftlik. Qattiq qatorni yumshoq qatordan "
            "ajratasiz, Ы tovushini aytishni oʻrganasiz va я ё ю е ning ikki vazifasini "
            "koʻrasiz."
        ),
        "content": """
<h2>PR-2: Unlilar: а о у э ы va yumshatuvchi juftlar я ё ю е и</h2>

<p>Rus tilida oʻnta unli harf bor va bu koʻpdek tuyuladi. Aslida esa <b>beshta juftlik</b>
bor, xolos. Har bir juftlikda bir xil unli ikki marta yozilgan: bir marta “qattiq”
shaklda, bir marta “yumshoq” shaklda. Shu bitta g‘oyani tushunsangiz, rus tilining
imlosi ham, talaffuzi ham darrov mantiqiy boʻlib qoladi — chunki bu juftliklar butun
til boʻylab takrorlanadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Beshta unli juftlikni va ular nima uchun juft ekanini bilasiz</li>
    <li><b>Ы</b> tovushini — oʻzbek tilida yoʻq boʻlgan yagona unlini — aytasiz</li>
    <li>я, ё, ю, е ning ikkita butunlay boshqa vazifasini ajratasiz</li>
    <li><b>ё</b> haqidagi ikkita muhim qoidani bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Beshta juftlik</span>
  <span class="pe-chip pe-chip--s">а — я</span>
  <span class="pe-chip pe-chip--s">о — ё</span>
  <span class="pe-chip pe-chip--s">у — ю</span>
  <span class="pe-chip pe-chip--s">э — е</span>
  <span class="pe-chip pe-chip--s">ы — и</span>
</div>

<h3>1. Qattiq qator va yumshoq qator</h3>

<p>Chap ustundagi beshta harf — <b>qattiq</b> unlilar (твёрдые). Oʻng ustundagilar —
<b>yumshoq</b> unlilar (мягкие). Tovush oʻzi bir xil; farq oldidagi undoshga
tegishli.</p>

<div class="pr-cyr">
  <div class="pr-cyr__c pr-cyr__c--new">
    <span class="pr-cyr__ch">А а — Я я</span>
    <span class="pr-cyr__rom">a — ya</span>
    <span class="pr-cyr__uz">ма́ма · мя́со</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--new">
    <span class="pr-cyr__ch">О о — Ё ё</span>
    <span class="pr-cyr__rom">o — yo</span>
    <span class="pr-cyr__uz">нос · нёс</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--new">
    <span class="pr-cyr__ch">У у — Ю ю</span>
    <span class="pr-cyr__rom">u — yu</span>
    <span class="pr-cyr__uz">лу́к · люк</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--new">
    <span class="pr-cyr__ch">Э э — Е е</span>
    <span class="pr-cyr__rom">e — ye</span>
    <span class="pr-cyr__uz">э́то · нет</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--false">
    <span class="pr-cyr__ch">Ы ы — И и</span>
    <span class="pr-cyr__rom">ı — i</span>
    <span class="pr-cyr__uz">мы́ло · ми́ло</span>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Undoshdan keyin turgan yumshoq unli <b>oʻzidan oldingi undoshni yumshatadi</b>.
<b>та</b> — qattiq “ta”, <b>тя</b> — yumshoq “tya” (til tanglayga koʻtariladi).
Bu rus tilidagi eng katta imlo mantiqi: unli harf oʻzidan oldingi undosh haqida
xabar beradi.</div>

<h3>2. Ы — oʻzbek tilida yoʻq yagona unli</h3>

<p>Rostini aytamiz: <b>Ы</b> — bu darsning eng qiyin joyi, chunki bunday tovush
oʻzbek tilida yoʻq. Lekin uni chiqarishning aniq usuli bor.</p>

<ol class="pe-steps">
  <li>“<b>у</b>” deb ayting va lablaringizni doira qilib turing.</li>
  <li>Tovushni toʻxtatmang — lablaringizni tekislang, kulgandek yoying.</li>
  <li>Til joyidan qimirlamasin: u orqada, tomoqqa yaqin turaveradi.</li>
  <li>Chiqqan tovush — <b>ы</b>. “i” emas, chunki til orqada; “u” emas, chunki lab yoyilgan.</li>
</ol>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Koʻpchilik oʻzbek oʻquvchisi <b>ы</b> ni <b>и</b> deb aytadi — bu eng koʻp
uchraydigan talaffuz xatosi. Farq eshitiladi va u maʼnoni buzadi. Oʻzbek tilidagi
<em>“qish”</em> soʻzidagi i tovushi biroz orqaroq aytiladi — mana shu yoʻnalishga
yana bir qadam qoʻysangiz, ы chiqadi.</div>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">мы́ло</span>
    <span class="pr-pair__uz">sovun</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">ми́ло</span>
    <span class="pr-pair__uz">yoqimli, shirin</span>
  </div>
</div>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">был</span>
    <span class="pr-pair__uz">edi (u erkak)</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">бил</span>
    <span class="pr-pair__uz">urardi</span>
  </div>
</div>

<p>Yana bitta muhim narsa: <b>ы</b> hech qachon soʻz boshida kelmaydi. Uni doim
undoshdan keyin koʻrasiz: <b>мы</b> (biz), <b>ты</b> (sen), <b>сын</b> (oʻgʻil),
<b>кни́ги</b>… — toʻxtang, oxirgisi <b>и</b> bilan. Nega? Buni PR-4 da koʻramiz:
ж, ш, ц dan keyin <b>и</b> yoziladi, lekin <b>[ы]</b> oʻqiladi.</p>

<h3>3. Я, Ё, Ю, Е — ikkita butunlay boshqa vazifa</h3>

<p>Bu toʻrt harf ikki xil ishlaydi, va ular qayerda turganiga qarab ish oʻzgaradi.
Bu — darsning ikkinchi asosiy g‘oyasi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">1-vazifa: <b>й + unli</b></p>
    <p><b>Qayerda:</b> soʻz boshida, unlidan keyin, ъ yoki ь dan keyin.</p>
    <p><b>Ikki tovush beradi:</b><br>
       я = [йа] · ё = [йо] · ю = [йу] · е = [йэ]</p>
    <p>я́блоко [йа́блъкъ] — olma<br>
       моя́ [майа́] — mening (ayol)<br>
       ёлка [йо́лкъ] — archa<br>
       семья́ [сим'йа́] — oila</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">2-vazifa: <b>undoshni yumshatish</b></p>
    <p><b>Qayerda:</b> undoshdan keyin.</p>
    <p><b>Bitta tovush beradi</b>, oldingi undoshni yumshatadi:<br>
       мя = [м'а] · нё = [н'о] · лю = [л'у] · те = [т'э]</p>
    <p>мя́со [м'а́съ] — goʻsht<br>
       тётя [т'о́т'ъ] — xola<br>
       лю́ди [л'у́д'и] — odamlar<br>
       нет [н'эт] — yoʻq</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Моя́ семья́ — э́то ма́ма, па́па и я.</p>
  <p class="pe-ex__rom">[майа́ сим'йа́ — э́тъ ма́мъ, па́пъ и йа]</p>
  <p class="pe-ex__uz">Mening oilam — bu oyim, dadam va men.</p>
  <p class="pe-ex__why">Bu gapda <b>я</b> uch marta keladi va uchalasi ham
     1-vazifada: <b>мо-я</b> (unlidan keyin), <b>семь-я</b> (ь dan keyin),
     <b>я</b> (soʻz boshida). Hammasi [йа].</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu sizga notanish emas. Oʻzbek lotinida biz <em>yalpiz</em>, <em>yoʻl</em>,
<em>yurak</em> deb <b>ikki harf</b> bilan yozamiz; oʻzbek kirillida esa aynan
ruschadagidek <b>ялпиз</b>, <b>йўл</b>, <b>юрак</b>. Yaʼni “bitta harf — ikkita
tovush” g‘oyasi oʻzbek kirilliga ruschadan kirgan. Siz bu tizimni allaqachon
koʻrgansiz.</div>

<h3>4. Ё haqida ikkita qoida</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida 1</span>
<b>Ё har doim urgʻuli.</b> Bitta istisno ham yoʻq. Shuning uchun ё ustiga
urgʻu belgisi qoʻyilmaydi — u allaqachon urgʻuli. Soʻzda ё koʻrsangiz, urgʻuni
qidirib oʻtirmang: u shu yerda.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Ё koʻpincha “е” deb chop etiladi.</b> Gazeta, kitob va saytlarda nuqtalar
tashlab ketiladi: <b>ещё</b> oʻrniga <b>еще</b>, <b>всё</b> oʻrniga <b>все</b>.
Bu chalkashtiradi, chunki <b>всё</b> (hammasi) va <b>все</b> (hammalari) — ikki
xil soʻz. Prime Russian darslarida biz nuqtalarni <em>doim</em> qoʻyamiz, lekin
tashqaridagi matnlarda ularni oʻzingiz tiklashga tayyor boʻling.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>мы́ло va ми́ло bir xil oʻqiladi</s></p>
  <p class="pe-good">Yoʻq: <b>[мы́лъ]</b> (sovun) va <b>[м'и́лъ]</b> (yoqimli) — boshqa soʻzlar</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>мя́со → [мйа́со]</s></p>
  <p class="pe-good">мя́со → <b>[м'а́съ]</b> — undoshdan keyin я “й” bermaydi, faqat yumshatadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>я́блоко → [а́блоко]</s></p>
  <p class="pe-good">я́блоко → <b>[йа́блъкъ]</b> — soʻz boshida я = <b>йа</b>, “й” tushib qolmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>ещё soʻzida urgʻu birinchi boʻgʻinda</s></p>
  <p class="pe-good"><b>ещё</b> — urgʻu <b>ё</b> da, chunki ё har doim urgʻuli</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>ю</b> harfining juftini ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>у</strong>. Juftliklar: а—я, о—ё,
    <b>у—ю</b>, э—е, ы—и. Chap tomondagi qattiq, oʻng tomondagi yumshoq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>ЮГ</b> (janub) soʻzida ю qaysi vazifada?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>1-vazifada — [йук].</strong> Ю soʻz
    boshida turibdi, shuning uchun ikkita tovush beradi: й + у. (Oxirgi Г nega
    [к] boʻlib qolgani PR-5 da — bu <em>оглушение</em>.)</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>ЛЮ́ДИ</b> soʻzida ю qaysi vazifada?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>2-vazifada — [л'у́д'и].</strong> Ю
    undosh <b>Л</b> dan keyin turibdi, shuning uchun “й” bermaydi — faqat Л ni
    yumshatadi. “Lyudi”, “Lyyudi” emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu ikki soʻzning maʼnosi bir xilmi? <b>нос</b> — <b>нёс</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Yoʻq.</strong> <b>нос</b> [нос] — burun.
    <b>нёс</b> [н'ос] — koʻtarib ketardi. Farq faqat Н ning yumshoqligida, lekin
    bu butunlay boshqa soʻz. Mana shuning uchun yumshoq unlilar muhim.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi soʻzda urgʻu topish uchun hech narsa qilish shart emas?<br>
     а) молоко́ &nbsp; б) тётя &nbsp; в) кни́га &nbsp; г) окно́</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б) тётя.</strong> Unda <b>ё</b> bor, ё esa
    har doim urgʻuli — demak urgʻu birinchi boʻgʻinda. Qolgan soʻzlarda urgʻuni
    yodlash yoki belgidan koʻrish kerak.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>гла́сный</b><span>unli (tovush)</span></li>
  <li><b>согла́сный</b><span>undosh</span></li>
  <li><b>твёрдый</b><span>qattiq</span></li>
  <li><b>мя́гкий</b><span>yumshoq</span></li>
  <li><b>мы́ло</b><span>sovun</span></li>
  <li><b>мя́со</b><span>goʻsht</span></li>
  <li><b>лю́ди</b><span>odamlar</span></li>
  <li><b>семья́</b><span>oila</span></li>
  <li><b>я́блоко</b><span>olma</span></li>
  <li><b>ещё</b><span>hali, yana</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>10 unli = <b>5 juftlik</b>: а—я, о—ё, у—ю, э—е, ы—и.</li>
    <li><b>Ы</b> — oʻzbek tilida yoʻq. “у” deb ayting, lablarni yoying: chiqadi.
        <b>мы́ло ≠ ми́ло</b>.</li>
    <li>я ё ю е <b>soʻz boshida / unlidan keyin / ъ ь dan keyin</b> = й + unli.</li>
    <li>Oʻsha harflar <b>undoshdan keyin</b> = bitta unli + undoshni yumshatadi.</li>
    <li><b>Ё har doim urgʻuli</b>, lekin bosmada koʻpincha “е” deb yoziladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-3: Undoshlar 1: jarangli va jarangsiz juftliklar (б-п, в-ф, г-к, д-т, з-с, ж-ш)",
        "category": "russian",
        "order": 3,
        "summary": (
            "Rus undoshlarining yarmi juft boʻlib yashaydi: bir xil ogʻiz, bir xil til, "
            "farq faqat tomoqda. Bu juftliklarni bilsangiz, PR-5 dagi talaffuz qoidalari "
            "oʻz-oʻzidan tushunarli boʻladi."
        ),
        "content": """
<h2>PR-3: Undoshlar 1: jarangli va jarangsiz juftliklar (б-п, в-ф, г-к, д-т, з-с, ж-ш)</h2>

<p>Barmogʻingizni tomogʻingizga qoʻying va “<b>ззззз</b>” deng. Titrayaptimi? Endi
qoʻlni olmasdan “<b>сссс</b>” deng. Titrash toʻxtadi. Ogʻzingiz, tilingiz, tishingiz
bir xil holatda turibdi — faqat tomoq ishlashdan toʻxtadi. Mana shu — rus tilidagi
oltita undosh juftligining butun siri. Va bu sirni bilish keyinchalik sizga eng
qiyin talaffuz qoidalarini tekinga beradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Oltita jarangli–jarangsiz juftlikni tomoq testi bilan ajratasiz</li>
    <li>Juftsiz undoshlarni — doim jarangli va doim jarangsizlarini — bilasiz</li>
    <li>Har bir undoshning qattiq va yumshoq shakli borligini koʻrasiz</li>
    <li>Nega <b>хлеб</b> [хлеп] deb oʻqilishini oldindan tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tomoq testi</span>
  <span class="pe-chip pe-chip--v">tomoq titraydi</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">зво́нкий — jarangli</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">tomoq jim</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">глухо́й — jarangsiz</span>
</div>

<h3>1. Oltita juftlik</h3>

<p>Har bir qatorda ikkita harf bir xil tarzda aytiladi. Farq faqat bitta: ovoz
paychalari ishlaydimi yoki yoʻqmi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Jarangli</th><th>Jarangsiz</th><th>Qayerda yasaladi</th><th>Ruscha misol</th></tr>
  <tr><td class="pr-stem">Б б</td><td class="pr-end">П п</td><td>ikki lab</td>
      <td class="pr-uz">брат (aka) — парк (park)</td></tr>
  <tr><td class="pr-stem">В в</td><td class="pr-end">Ф ф</td><td>tish + past lab</td>
      <td class="pr-uz">вода́ (suv) — фи́льм (film)</td></tr>
  <tr><td class="pr-stem">Г г</td><td class="pr-end">К к</td><td>tilning orqasi</td>
      <td class="pr-uz">го́род (shahar) — кот (mushuk)</td></tr>
  <tr><td class="pr-stem">Д д</td><td class="pr-end">Т т</td><td>til + tish</td>
      <td class="pr-uz">дом (uy) — там (u yerda)</td></tr>
  <tr><td class="pr-stem">З з</td><td class="pr-end">С с</td><td>til + tish, siljish</td>
      <td class="pr-uz">зима́ (qish) — сын (oʻgʻil)</td></tr>
  <tr><td class="pr-stem">Ж ж</td><td class="pr-end">Ш ш</td><td>til orqaroq, shivirlash</td>
      <td class="pr-uz">жена́ (xotin) — шко́ла (maktab)</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Yaxshi xabar: <b>oltita juftlikning hammasi oʻzbek tilida ham bor</b> —
b–p, v–f, g–k, d–t, z–s, j–sh. Bu ovozlarni chiqarishni oʻrganishingiz shart emas,
siz ularni bolalikdan aytasiz. Sizga faqat <em>rus tili bu juftliklar bilan nima
qilishini</em> bilish kerak — va u juda qiziq narsalar qiladi (PR-5).</div>

<h3>2. Juftsiz undoshlar</h3>

<p>Qolgan undoshlarning jufti yoʻq. Ular ikki guruhga boʻlinadi va bu ham keyin
kerak boʻladi:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Doim jarangli</p>
    <p style="font-size:1.3rem"><b>Л М Н Р Й</b></p>
    <p>Bular hech qachon jarangsizlanmaydi. Soʻz oxirida ham oʻzicha qoladi:
    <b>стол</b> [стол], <b>дом</b> [дом], <b>сын</b> [сын], <b>мир</b> [мир].</p>
    <p>Ularni <em>сонорные</em> deb ham atashadi — “ovozdorlar”.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Doim jarangsiz</p>
    <p style="font-size:1.3rem"><b>Х Ц Ч Щ</b></p>
    <p>Bularning jarangli jufti yoʻq. <b>хлеб</b>, <b>цирк</b>, <b>чай</b>,
    <b>щи</b> — hammasida tomoq jim.</p>
    <p>Bu toʻrttasini PR-4 da alohida koʻramiz, chunki ularning oʻz odati bor.</p>
  </div>
</div>

<h3>3. Har bir undoshning ikkita yuzi bor: qattiq va yumshoq</h3>

<p>PR-2 da unlilar juft boʻlishini koʻrdik. Endi mantiq yopiladi: <b>undoshlar ham
juft</b> — qattiq va yumshoq. Va qaysi biri ekanini <em>keyingi harf</em> aytib
beradi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Keyin nima kelsa</th><th>Undosh qanday</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-end">а о у э ы</td><td class="pr-res">QATTIQ</td>
      <td class="pr-stem">н</td><td class="pr-uz">но́вый [но́вый] — yangi</td></tr>
  <tr><td class="pr-end">я ё ю е и</td><td class="pr-res">YUMSHOQ</td>
      <td class="pr-stem">н'</td><td class="pr-uz">не́бо [н'э́бъ] — osmon</td></tr>
  <tr><td class="pr-end">ь (yumshoq belgi)</td><td class="pr-res">YUMSHOQ</td>
      <td class="pr-stem">т'</td><td class="pr-uz">мать [мат'] — ona</td></tr>
  <tr><td class="pr-end">boshqa undosh / soʻz oxiri</td><td class="pr-res">QATTIQ</td>
      <td class="pr-stem">т</td><td class="pr-uz">там [там] — u yerda</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ru">Мой <span class="pe-hl pe-hl--s">брат</span> —
     <span class="pe-hl pe-hl--v">до́ктор</span>.</p>
  <p class="pe-ex__rom">[мой брат — до́ктър]</p>
  <p class="pe-ex__uz">Mening akam — shifokor.</p>
  <p class="pe-ex__why">Hamma undoshlar qattiq: keyin а, о kelgan yoki soʻz
     tugagan. Rus tilida gapning oddiy holati shu.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Э́то <span class="pe-hl pe-hl--o">дя́дя Оле́г</span>.</p>
  <p class="pe-ex__rom">[э́тъ д'а́д'ъ ал'э́к]</p>
  <p class="pe-ex__uz">Bu — Oleg amaki.</p>
  <p class="pe-ex__why">Bu yerda <b>д</b> ikki marta yumshoq (д'), chunki
     keyin <b>я</b> turibdi. Yumshoqlik belgisi — [ ' ].</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbek tilida undoshning qattiq–yumshoqligi <b>maʼnoni oʻzgartirmaydi</b>. Rus
tilida oʻzgartiradi, va bu oʻzbek oʻquvchisi uchun eng notanish g‘oya:
<b>мат</b> (shaxmatda mot) — <b>мать</b> (ona); <b>угол</b> (burchak) —
<b>у́голь</b> (koʻmir). Yumshoqlikni “ozgina i qoʻshish” deb tushunmang: “mati”
emas, <b>[мат']</b> — til tanglayga tegib turadi, lekin unli chiqmaydi.</div>

<h3>4. Nega bu darс keyin ham kerak boʻladi</h3>

<p>Juftliklarni yodlash oʻz-oʻzicha zerikarli. Lekin ularsiz rus talaffuzining
ikki asosiy qoidasini tushunib boʻlmaydi. Oldindan bir qarab qoʻyaylik:</p>

<div class="pr-say">
  <span class="pr-say__from">хлеб</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[хлеп]</span>
  <span class="pr-say__why">soʻz oxirida б oʻz juftiga — п ga aylanadi</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">во́дка</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[во́тка]</span>
  <span class="pr-say__why">jarangsiz к dan oldin д ham jarangsizlanadi → т</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">сде́лать</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[зд'э́лът']</span>
  <span class="pr-say__why">teskarisi ham boʻladi: jarangli д dan oldin с → з</span>
</div>

<p>Uchala holatda ham tovush <b>oʻz juftiga</b> oʻtdi — boshqa tovushga emas.
Shuning uchun juftliklarni bilish shart: qoidani yodlamaysiz, uni koʻrasiz.
Toʻliq tushuntirish PR-5 da.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Г ni oʻzbekcha “гʻ” kabi aytish: <b>го́род</b> → [гʻорот]</s></p>
  <p class="pe-good"><b>го́род</b> → <b>[го́рът]</b> — rus Г har doim oddiy “g”, “gʻ” emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>мать → “mati”</s></p>
  <p class="pe-good">мать → <b>[мат']</b> — ь unli emas, u faqat т ni yumshatadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>В ni soʻz oxirida “v” deb aytish: <b>Ки́ев</b> → [ки́ев]</s></p>
  <p class="pe-good"><b>Ки́ев</b> → <b>[ки́иф]</b> — soʻz oxirida В oʻz juftiga (Ф) oʻtadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>стол → [стоl] yumshoq “l” bilan</s></p>
  <p class="pe-good">стол → <b>[стол]</b> — keyin ь ham, yumshoq unli ham yoʻq, demak qattiq Л</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>З</b> harfining jarangsiz jufti qaysi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>С</strong>. Til va tish bir xil holatda,
    farq faqat tomoqda: <b>з</b> da titraydi, <b>с</b> da jim. Tekshirib koʻring:
    “зззз” → “ссс”.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Qaysi undoshning jufti <b>yoʻq</b>?
     &nbsp;Б &nbsp;·&nbsp; Ж &nbsp;·&nbsp; Р &nbsp;·&nbsp; Д</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Р</strong> — u doim jarangli, jufti yoʻq
    (Л М Н Р Й guruhidan). Qolganlarining jufti bor: Б—П, Ж—Ш, Д—Т.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>ДЕНЬ</b> soʻzida Д qattiqmi yoki yumshoq?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Yumshoq — [д'эн'].</strong> Chunki
    keyin <b>е</b> (yumshoq unli) turibdi. Oxiridagi <b>Н</b> ham yumshoq, chunki
    undan keyin <b>ь</b> bor. Yaʼni soʻzda ikkita yumshoq undosh.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nega <b>друг</b> soʻzi [друк] deb oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <b>Г</b> soʻz oxirida turibdi va u
    <strong>oʻz jarangsiz juftiga — К ga</strong> aylanadi. Boshqa tovushga emas,
    aynan oʻz juftiga. Shuning uchun juftliklarni bilish kerak edi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi soʻzda hamma undosh <b>qattiq</b>?<br>
     а) мать &nbsp; б) стол &nbsp; в) дя́дя &nbsp; г) день</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б) стол.</strong> С, Т, Л — uchalasidan
    keyin ham yo qattiq unli (о), yo soʻz oxiri. “мать” da ь bor, “дя́дя” da я bor,
    “день” da е va ь bor — hammasi yumshatadi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>зво́нкий</b><span>jarangli</span></li>
  <li><b>глухо́й</b><span>jarangsiz</span></li>
  <li><b>па́ра</b><span>juftlik</span></li>
  <li><b>брат</b><span>aka, uka</span></li>
  <li><b>вода́</b><span>suv</span></li>
  <li><b>го́род</b><span>shahar</span></li>
  <li><b>дом</b><span>uy</span></li>
  <li><b>зима́</b><span>qish</span></li>
  <li><b>шко́ла</b><span>maktab</span></li>
  <li><b>друг</b><span>doʻst</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Oltita juftlik: <b>б-п, в-ф, г-к, д-т, з-с, ж-ш</b>. Farq faqat tomoqda.</li>
    <li>Doim jarangli: <b>Л М Н Р Й</b>. Doim jarangsiz: <b>Х Ц Ч Щ</b>.</li>
    <li>Har bir undoshning qattiq va yumshoq shakli bor; buni <b>keyingi harf</b>
        hal qiladi.</li>
    <li>Yumshoqlik <b>maʼnoni oʻzgartiradi</b>: мат ≠ мать, угол ≠ уголь.</li>
    <li>Tovush oʻzgarganda u <b>oʻz juftiga</b> oʻtadi — shuning uchun juftliklar kerak.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-4: Undoshlar 2: shivirlovchilar ж ш щ ч ц, й harfi va ikki belgi ъ ь",
        "category": "russian",
        "order": 4,
        "summary": (
            "Rus tilining eng oʻjar beshta undoshi: ж, ш, ц doim qattiq, ч va щ doim "
            "yumshoq — nima yozilishidan qatʼi nazar. Shu bilan birga ъ va ь belgilarining "
            "vazifasini hal qilamiz."
        ),
        "content": """
<h2>PR-4: Undoshlar 2: shivirlovchilar ж ш щ ч ц, й harfi va ikki belgi ъ ь</h2>

<p>Oʻtgan darsda shunday qoida oʻrgandik: undoshning qattiq yoki yumshoqligini
keyingi harf hal qiladi. Endi rus tili sizga beshta undoshni koʻrsatadi va deydi:
“bularga u qoida taʼsir qilmaydi”. Ular oʻz bilganini qiladi — <b>ж, ш, ц</b> har
doim qattiq, <b>ч, щ</b> har doim yumshoq, ortidan nima yozilishidan qatʼi nazar.
Bu darsda oʻsha beshtasini, <b>й</b> harfini va rus alifbosidagi ovozsiz ikki
belgini hal qilamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Ж, Ш, Ц ning doim qattiq, Ч va Щ ning doim yumshoq ekanini bilasiz</li>
    <li><b>жи-ши</b> imlo qoidasini va nega u aldov ekanini tushunasiz</li>
    <li>Ш va Щ orasidagi farqni eshitasiz va ayta olasiz</li>
    <li>Ъ va Ь — tovushi yoʻq ikki harfning vazifasini ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Beshta oʻjar undosh</span>
  <span class="pe-chip pe-chip--o">Ж Ш Ц</span>
  <span class="pe-op">= doim QATTIQ</span>
  <span class="pe-chip pe-chip--s">Ч Щ</span>
  <span class="pe-op">= doim YUMSHOQ</span>
</div>

<h3>1. Beshta oʻjar undosh</h3>

<div class="pr-cyr">
  <div class="pr-cyr__c pr-cyr__c--new">
    <span class="pr-cyr__ch">Ж ж</span>
    <span class="pr-cyr__rom">j</span>
    <span class="pr-cyr__uz">“jon”dagi j · doim qattiq</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--new">
    <span class="pr-cyr__ch">Ш ш</span>
    <span class="pr-cyr__rom">sh</span>
    <span class="pr-cyr__uz">“shahar”dagi sh · doim qattiq</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--new">
    <span class="pr-cyr__ch">Ц ц</span>
    <span class="pr-cyr__rom">ts</span>
    <span class="pr-cyr__uz">“sement”dagi s+t · doim qattiq</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--new">
    <span class="pr-cyr__ch">Ч ч</span>
    <span class="pr-cyr__rom">ch</span>
    <span class="pr-cyr__uz">“choy”dagi ch · doim yumshoq</span>
  </div>
  <div class="pr-cyr__c pr-cyr__c--new">
    <span class="pr-cyr__ch">Щ щ</span>
    <span class="pr-cyr__rom">shsh</span>
    <span class="pr-cyr__uz">uzun yumshoq sh · doim yumshoq</span>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Beshtadan toʻrttasi sizda bor: <b>ж</b> = j, <b>ш</b> = sh, <b>ц</b> ≈ s/ts,
<b>ч</b> = ch. Faqat <b>щ</b> yangi — oʻzbek kirillida bu harf yoʻq edi. Lekin
tovushi qiyin emas: bu shunchaki <em>uzunroq va yumshoqroq</em> “sh”. Til
tanglayga koʻproq yaqinlashadi va tovush biroz choʻziladi.</div>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">наш</span>
    <span class="pr-pair__uz">bizning · qisqa, qattiq [ш]</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">площадь</span>
    <span class="pr-pair__uz">maydon · uzun, yumshoq [щ']</span>
  </div>
</div>

<h3>2. Жи-ши qoidasi — imlo bilan talaffuz kelishmagan joy</h3>

<p>Rus maktabida bolalar shu qofiyani yodlaydi: <em>«жи-ши пиши с буквой И»</em> —
“жи va ши ni И bilan yoz”. Lekin bu <b>imlo</b> qoidasi, <b>talaffuz</b> qoidasi
emas. Yozganda И, oʻqiganda [Ы]:</p>

<div class="pr-say">
  <span class="pr-say__from">жить</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[жыт']</span>
  <span class="pr-say__why">ж qattiq — И uni yumshata olmaydi</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">маши́на</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[машы́нъ]</span>
  <span class="pr-say__why">ш qattiq — “mashina” emas, “mashına”</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">цирк</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[цырк]</span>
  <span class="pr-say__why">ц ham qattiq — И yana [ы] boʻlib chiqadi</span>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Ж, Ш, Ц dan keyin И yoziladi — lekin [Ы] oʻqiladi.</b> Shuningdek
ж/ш dan keyin <b>ё</b> emas, koʻpincha <b>о</b> yoki <b>е</b> yoziladi, va
<b>ю/я</b> deyarli hech qachon yozilmaydi. Bu qoidalarni yodlash shart emas:
esda tuting-ki bu uch harf yumshamaydi, qolganini imlo oʻzi hal qiladi.</div>

<h3>3. Й — unli emas, undosh</h3>

<p><b>Й</b> ni “qisqa и” deb atashadi (и краткое), lekin u undosh. U hech qachon
oʻzi boʻgʻin yasamaydi. Uni PR-2 dagi я ё ю е ning ichidagi “й” bilan solishtiring —
bu oʻsha tovush, faqat ochiq yozilgan:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Yozilishi</th><th>Oʻqilishi</th><th>Maʼnosi</th><th>Izoh</th></tr>
  <tr><td class="pr-res">чай</td><td class="pr-end">[чай]</td><td class="pr-uz">choy</td>
      <td class="pr-uz">Й soʻz oxirida — unlidan keyin</td></tr>
  <tr><td class="pr-res">музе́й</td><td class="pr-end">[музэ́й]</td><td class="pr-uz">muzey</td>
      <td class="pr-uz">shu joyda</td></tr>
  <tr><td class="pr-res">мой</td><td class="pr-end">[мой]</td><td class="pr-uz">mening</td>
      <td class="pr-uz">shu joyda</td></tr>
  <tr><td class="pr-res">йо́гурт</td><td class="pr-end">[йо́гурт]</td><td class="pr-uz">yogurt</td>
      <td class="pr-uz">kamdan-kam: soʻz boshida</td></tr>
</table></div>

<h3>4. Ъ va Ь — tovushi yoʻq ikki harf</h3>

<p>Rus alifbosining oxirgi sirlari. Bu ikki harfning <b>oʻz tovushi yoʻq</b>:
ular faqat qoʻshni harflarga koʻrsatma beradi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Ь — мя́гкий знак (yumshoq belgi)</p>
    <p><b>Vazifasi:</b> oldidagi undoshni yumshatadi.</p>
    <p><b>Qayerda:</b> soʻz oxirida yoki soʻz ichida.</p>
    <p>мать [мат'] — ona<br>
       соль [сол'] — tuz<br>
       день [д'эн'] — kun<br>
       писа́ть [п'иса́т'] — yozmoq</p>
    <p><b>Juda koʻp uchraydi</b> — deyarli har bir infinitiv shu bilan tugaydi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Ъ — твёрдый знак (qattiq belgi)</p>
    <p><b>Vazifasi:</b> ajratadi — keyingi я ё ю е ni “й + unli” qilib oʻqitadi.</p>
    <p><b>Qayerda:</b> deyarli faqat prefiksdan keyin.</p>
    <p>объясни́ть [аб-йисн'и́т'] — tushuntirmoq<br>
       съесть [с-йэст'] — yeb qoʻymoq<br>
       подъе́зд [пад-йэ́ст] — podyezd</p>
    <p><b>Juda kam uchraydi</b> — butun matnda bir-ikki marta.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Мать <span class="pe-hl pe-hl--v">говори́т</span>:
     «<span class="pe-hl pe-hl--o">Соль</span> на столе́».</p>
  <p class="pe-ex__rom">[мат' гъвар'и́т: сол' нъ стал'э́]</p>
  <p class="pe-ex__uz">Ona aytadi: “Tuz stolda”.</p>
  <p class="pe-ex__why">Ikkita <b>ь</b>: <b>мать</b> va <b>соль</b>. Ikkalasida ham
     u faqat oxirgi undoshni yumshatadi — hech qanday unli qoʻshmaydi.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Ь ni unli deb oʻqimang.</b> Oʻzbek oʻquvchisining eng koʻp uchraydigan
xatosi: <em>писать</em> ni “pisati”, <em>соль</em> ni “soli” deb aytish.
Yumshoq belgi <b>hech qanday tovush chiqarmaydi</b>. U shunchaki tilingizga
“tanglayga tegib tur” deydi. Soʻz oxiridagi undosh yumshoq boʻladi va shu yerda
toʻxtaydi.</div>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">у́гол</span>
    <span class="pr-pair__uz">burchak</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">у́голь</span>
    <span class="pr-pair__uz">koʻmir</span>
  </div>
</div>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">брат</span>
    <span class="pr-pair__uz">aka (ot)</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">брать</span>
    <span class="pr-pair__uz">olmoq (feʼl)</span>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Ikkinchi juftlikni yaxshilab yodlang: <b>-ть</b> bilan tugagan soʻz deyarli har
doim <b>feʼlning infinitivi</b> — “-moq”. читать (oʻqimoq), писать (yozmoq),
говорить (gapirmoq), жить (yashamoq). Notanish soʻz oxirida <b>-ть</b> koʻrsangiz,
bu feʼl. Bu kichik belgi sizga lugʻatsiz yuzlab soʻzni taniydi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>маши́на → [маши́на] yumshoq “shi” bilan</s></p>
  <p class="pe-good">маши́на → <b>[машы́нъ]</b> — Ш doim qattiq, И dan keyin ham</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>соль → “soli”</s></p>
  <p class="pe-good">соль → <b>[сол']</b> — ь tovush emas, u faqat Л ni yumshatadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>ещё → [есho]</s></p>
  <p class="pe-good">ещё → <b>[йищ'о́]</b> — Щ uzun yumshoq “sh”, va ё urgʻuli</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ъ ham undoshni yumshatadi</s></p>
  <p class="pe-good">Yoʻq — <b>Ъ ajratadi</b>, <b>Ь yumshatadi</b>. Ular teskari ish qiladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>ЖИЗНЬ</b> (hayot) soʻzidagi ЖИ qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[жы]</strong>. Yozilishi И, oʻqilishi
    [ы] — chunki <b>Ж doim qattiq</b>. Butun soʻz: [жызн']. Oxiridagi ь Н ni
    yumshatadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Qaysi undosh <b>doim yumshoq</b>?
     &nbsp;Ж &nbsp;·&nbsp; Ц &nbsp;·&nbsp; Ч &nbsp;·&nbsp; Ш</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ч</strong> (va bu yerda yoʻq boʻlgan Щ).
    Ж, Ц, Ш — uchalasi doim qattiq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>СЕМЬЯ́</b> soʻzida Ь nima qilyapti?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Bu yerda u <strong>ikki ish</strong> qilyapti:
    М ni yumshatadi <em>va</em> ajratadi, shuning uchun Я [йа] boʻlib oʻqiladi:
    <b>[сим'йа́]</b>. “Semya” emas, “sim-YA”. Soʻz ichidagi ь koʻpincha shunday
    ishlaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu soʻzlardan qaysi biri <b>feʼl</b>?<br>
     а) мать &nbsp; б) брать &nbsp; в) соль &nbsp; г) день</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б) брать</strong> — olmoq. U <b>-ть</b>
    bilan tugaydi, bu infinitiv belgisi. Qolganlari otlar: мать (ona), соль (tuz),
    день (kun) — ular <b>-ть</b> emas, oddiy undosh + ь bilan tugagan.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi soʻzda <b>Ъ</b> boʻlishi kerak?<br>
     а) сесть &nbsp; б) съесть &nbsp; в) семья &nbsp; г) писать</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б) съесть</strong> (yeb qoʻymoq) — bu
    <b>с-</b> prefiksi + <b>есть</b>. Prefiksdan keyin, е dan oldin — Ъ ning
    aynan oʻz joyi: [с-йэст']. Ъ siz yozsangiz “сесть” (oʻtirmoq) chiqadi —
    butunlay boshqa soʻz!</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>жить</b><span>yashamoq</span></li>
  <li><b>маши́на</b><span>mashina</span></li>
  <li><b>цирк</b><span>sirk</span></li>
  <li><b>чай</b><span>choy</span></li>
  <li><b>ещё</b><span>hali, yana</span></li>
  <li><b>пло́щадь</b><span>maydon</span></li>
  <li><b>мать</b><span>ona</span></li>
  <li><b>соль</b><span>tuz</span></li>
  <li><b>брать</b><span>olmoq</span></li>
  <li><b>объясни́ть</b><span>tushuntirmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Ж Ш Ц</b> — doim qattiq. <b>Ч Щ</b> — doim yumshoq. Keyingi harf ularga
        taʼsir qilmaydi.</li>
    <li><b>жи-ши</b>: И yoziladi, <b>[ы]</b> oʻqiladi. Ци da ham shunday.</li>
    <li><b>Щ</b> = uzun yumshoq Ш. Oʻzbek kirillida yoʻq edi — yangi harf.</li>
    <li><b>Ь</b> yumshatadi (мать, соль), <b>Ъ</b> ajratadi (съесть). Ikkalasining
        ham tovushi yoʻq.</li>
    <li><b>-ть</b> bilan tugagan soʻz — deyarli har doim feʼlning infinitivi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-5: Urgʻu (ударение), аканье va soʻz oxiridagi jarangsizlanish",
        "category": "russian",
        "order": 5,
        "summary": (
            "Rus tilida urgʻu maʼnoni oʻzgartiradi va qolgan barcha unlilarni qisqartiradi. "
            "Uchta talaffuz qoidasi — аканье, иканье va оглушение — bilan har qanday soʻzni "
            "toʻgʻri oʻqiy boshlaysiz."
        ),
        "content": """
<h2>PR-5: Urgʻu (ударение), аканье va soʻz oxiridagi jarangsizlanish</h2>

<p>Alifbo tugadi. Endi eng qiziq narsa: rus tilida soʻz <b>yozilganidek
oʻqilmaydi</b>. <em>Молоко</em> deb yozilib, [мълако́] deb aytiladi. <em>Хлеб</em>
deb yozilib, [хлеп] deb aytiladi. Bu tartibsizlik emas — bu uchta aniq qoida, va
uchalasi ham bitta narsadan kelib chiqadi: <b>urgʻu</b>. Bu darsdan keyin siz
rus soʻzini koʻrib, uni qanday aytishni bilasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Urgʻu nega rus tilida shunchalik muhim ekanini tushunasiz</li>
    <li>Urgʻusiz О ni [a] deb aytasiz — bu <b>аканье</b></li>
    <li>Urgʻusiz Е va Я ni [и] deb aytasiz — bu <b>иканье</b></li>
    <li>Soʻz oxiridagi jarangli undoshni jarangsizlantirasiz — bu <b>оглушение</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta soʻz</span>
  <span class="pe-chip pe-chip--v">1 ta urgʻuli boʻgʻin</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--opt">qolgani qisqaradi</span>
</div>

<h3>1. Urgʻu — rus tilining yuragi</h3>

<p>Har bir ruscha soʻzda faqat <b>bitta</b> urgʻuli boʻgʻin bor. U boshqalardan
uzunroq, balandroq va aniqroq aytiladi. Qolgan boʻgʻinlar esa siqiladi, qisqaradi
va ba'zan deyarli eshitilmay qoladi.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana bu joy oʻzbek oʻquvchisi uchun eng qiyin, chunki oʻzbek tilida urgʻu
<b>deyarli doim oxirgi boʻgʻinda</b> va u maʼnoni <b>hech qachon
oʻzgartirmaydi</b>: <em>kitob</em>, <em>maktab</em>, <em>oʻqituvchi</em>. Rus
tilida urgʻu <b>istalgan boʻgʻinda</b> boʻlishi mumkin, soʻz oʻzgarganda
<b>joyini almashtiradi</b> va ba'zan <b>maʼnoni butunlay oʻzgartiradi</b>.
“Ruschada oʻzbek aksenti” degani, koʻpincha, aynan shu — hamma boʻgʻinni bir xil
kuch bilan aytish.</div>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">за́мок</span>
    <span class="pr-pair__uz">qulf</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">замо́к</span>
    <span class="pr-pair__uz">qalʼa, saroy</span>
  </div>
</div>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">му́ка</span>
    <span class="pr-pair__uz">azob</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">мука́</span>
    <span class="pr-pair__uz">un</span>
  </div>
</div>

<p>Va urgʻu koʻchib yuradi. Bitta soʻzning ichida:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Birlik</th><th>Koʻplik</th><th>Urgʻu</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">рука́</td><td class="pr-res">ру́ки</td>
      <td class="pr-end">oxirdan → boshga</td><td class="pr-uz">qoʻl → qoʻllar</td></tr>
  <tr><td class="pr-res">окно́</td><td class="pr-res">о́кна</td>
      <td class="pr-end">oxirdan → boshga</td><td class="pr-uz">deraza → derazalar</td></tr>
  <tr><td class="pr-res">го́род</td><td class="pr-res">города́</td>
      <td class="pr-end">boshdan → oxirga</td><td class="pr-uz">shahar → shaharlar</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Urgʻuni <b>soʻz bilan birga yodlang</b>, xuddi u harfning bir qismidek. Yangi
soʻzni daftarga yozganda urgʻusini ham qoʻying. Bu bir soniya vaqt oladi va sizni
bir yillik xatodan qutqaradi. Prime Russian darslarida PR-20 gacha urgʻu
<em>hamma joyda</em> belgilangan — bepul foydalaning.</div>

<h3>2. Аканье — urgʻusiz О qayerga ketadi</h3>

<p>Birinchi va eng koʻp uchraydigan qoida. <b>Urgʻusiz О harfi [а] boʻlib
oʻqiladi.</b> Urgʻudan uzoqlashgan sari u yanada qisqaradi va deyarli
eshitilmaydigan [ъ] ga aylanadi.</p>

<div class="pr-say">
  <span class="pr-say__from">вода́</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[вада́]</span>
  <span class="pr-say__why">urgʻudan oldingi о → toʻliq [а]</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">молоко́</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[мълако́]</span>
  <span class="pr-say__why">yaqindagi о → [а], uzoqdagisi → [ъ]</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">хорошо́</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[хърашо́]</span>
  <span class="pr-say__why">uchta о — uchtasi ham boshqacha oʻqiladi</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">Москва́</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[масква́]</span>
  <span class="pr-say__why">“Moskva” emas, “Maskva”</span>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Urgʻudan <b>bir boʻgʻin oldin</b>gi О — aniq [а]. Undan <b>uzoqroqda</b>gi О va
soʻz oxiridagi О — juda qisqa [ъ], oʻzbekchada oʻxshashi yoʻq, deyarli
“yutilgan” tovush: <b>го́род</b> [го́рът], <b>ма́сло</b> [ма́слъ].</div>

<h3>3. Иканье — urgʻusiz Е va Я qayerga ketadi</h3>

<p>Xuddi shu narsa yumshoq unlilar bilan ham boʻladi: <b>urgʻusiz Е va Я [и]
boʻlib oʻqiladi.</b></p>

<div class="pr-say">
  <span class="pr-say__from">сестра́</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[систра́]</span>
  <span class="pr-say__why">urgʻusiz е → [и]</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">язы́к</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[йизы́к]</span>
  <span class="pr-say__why">urgʻusiz я → [йи]</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">пятёрка</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[п'ит'о́ркъ]</span>
  <span class="pr-say__why">urgʻu ё da, shuning uchun я → [и]</span>
</div>

<h3>4. Оглушение — soʻz oxiridagi jarangsizlanish</h3>

<p>Uchinchi qoida, va bu yerda PR-3 dagi juftliklar ish beradi. <b>Soʻz oxirida
jarangli undosh oʻz jarangsiz juftiga aylanadi.</b> Rus tili soʻzni jarangli
tovush bilan tugatishni yoqtirmaydi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Yozilishi</th><th>Oʻqilishi</th><th>Nima boʻldi</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">хлеб</td><td class="pr-end">[хлеп]</td>
      <td class="pr-stem">б → п</td><td class="pr-uz">non</td></tr>
  <tr><td class="pr-res">друг</td><td class="pr-end">[друк]</td>
      <td class="pr-stem">г → к</td><td class="pr-uz">doʻst</td></tr>
  <tr><td class="pr-res">сад</td><td class="pr-end">[сат]</td>
      <td class="pr-stem">д → т</td><td class="pr-uz">bogʻ</td></tr>
  <tr><td class="pr-res">нож</td><td class="pr-end">[нош]</td>
      <td class="pr-stem">ж → ш</td><td class="pr-uz">pichoq</td></tr>
  <tr><td class="pr-res">глаз</td><td class="pr-end">[глас]</td>
      <td class="pr-stem">з → с</td><td class="pr-uz">koʻz</td></tr>
  <tr><td class="pr-res">Ки́ев</td><td class="pr-end">[ки́иф]</td>
      <td class="pr-stem">в → ф</td><td class="pr-uz">Kiyev</td></tr>
</table></div>

<p>Shu narsa soʻz <em>ichida</em> ham boʻladi, agar jarangli undosh jarangsizning
oldida tursa — va teskarisi ham:</p>

<div class="pr-say">
  <span class="pr-say__from">ло́дка</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[ло́ткъ]</span>
  <span class="pr-say__why">jarangsiz к dan oldin д → т</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">про́сьба</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[про́з'бъ]</span>
  <span class="pr-say__why">teskarisi: jarangli б dan oldin с → з</span>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bu qoida nega borligini bilsangiz, uni hech qachon unutmaysiz: <b>ogʻiz keyingi
tovushga oldindan tayyorlanadi</b>. Tomoq bir tovushda ishlab, keyingisida
darrov toʻxtay olmaydi — shuning uchun ikkala tovush ham bir xil boʻlib qoladi.
Buni <em>ассимиляция</em> deyishadi. Oʻzbek tilida ham xuddi shu narsa bor:
<em>ketdi</em> ni tez aytsangiz “ketti” chiqadi.</div>

<h3>5. Hammasini birga qoʻyamiz</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">Хлеб и молоко́ — на столе́.</p>
  <p class="pe-ex__rom">[хлеп и мълако́ — нъ стал'э́]</p>
  <p class="pe-ex__uz">Non va sut — stolda.</p>
  <p class="pe-ex__why">Bitta qisqa gapda uchala qoida ham ishladi:
     <b>хлеб</b> → [хлеп] (оглушение), <b>молоко</b> → [мълако́] (аканье),
     <b>на столе</b> → [нъ стал'э́] (аканье, ikki marta).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Моя́ сестра́ хорошо́ говори́т по-ру́сски.</p>
  <p class="pe-ex__rom">[майа́ систра́ хърашо́ гъвар'и́т па-ру́ски]</p>
  <p class="pe-ex__uz">Mening singlim yaxshi ruscha gapiradi.</p>
  <p class="pe-ex__why">Urgʻuli boʻgʻinlarni sanang: <b>-я́, -тра́, -шо́, -ри́т,
     ру́-</b>. Faqat shu beshtasi toʻliq aytiladi; qolgan hammasi qisqargan.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>молоко́ → [моloko]</s></p>
  <p class="pe-good">молоко́ → <b>[мълако́]</b> — urgʻusiz О hech qachon [о] emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>хлеб → [хлеб]</s></p>
  <p class="pe-good">хлеб → <b>[хлеп]</b> — soʻz oxirida Б oʻz jufti П ga oʻtadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Har bir boʻgʻinni bir xil kuch bilan aytish</s></p>
  <p class="pe-good">Bitta boʻgʻin <b>uzun va baland</b>, qolgani qisqa — bu talaffuzning yarmi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>за́мок va замо́к — bir xil soʻz, urgʻu muhim emas</s></p>
  <p class="pe-good"><b>за́мок</b> = qulf, <b>замо́к</b> = qalʼa — urgʻu maʼnoni oʻzgartiradi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>ХОРОШО́</b> — uchta О qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[хърашо́]</strong>. Oxirgi О urgʻuli —
    toʻliq [о]. Undan oldingisi [а]. Eng birinchisi urgʻudan uzoq — deyarli
    eshitilmaydigan [ъ]. Uch xil О, bitta soʻzda.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>САД</b> (bogʻ) qanday oʻqiladi va nega?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[сат]</strong> — <em>оглушение</em>.
    Soʻz oxiridagi <b>Д</b> oʻz jarangsiz juftiga, <b>Т</b> ga aylanadi.
    Diqqat: yozganda baribir <b>сад</b> — talaffuz oʻzgardi, imlo emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>МУ́КА</b> va <b>МУКА́</b> — farqi nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Faqat urgʻu, lekin maʼno butunlay boshqa:
    <strong>му́ка</strong> — azob, qiynoq. <strong>мука́</strong> — un (nondan
    yasaladigan). Ikkala soʻz bir xil harflardan tuzilgan.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>СЕСТРА́</b> soʻzidagi Е qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[и]</strong> — butun soʻz [систра́].
    Bu <em>иканье</em>: urgʻusiz Е va Я [и] boʻlib qisqaradi. Urgʻu oxirgi
    <b>А</b> da.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi oʻqish <b>notoʻgʻri</b>?<br>
     а) вода́ = [вада́] &nbsp; б) нож = [нош] &nbsp;
     в) го́род = [го́род] &nbsp; г) Москва́ = [масква́]</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в) notoʻgʻri.</strong> Ikkita xato bor:
    ikkinchi О urgʻusiz, demak [ъ] boʻlishi kerak; oxiridagi <b>Д</b> esa
    jarangsizlanib <b>Т</b> boʻladi. Toʻgʻrisi — <b>[го́рът]</b>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ударе́ние</b><span>urgʻu</span></li>
  <li><b>слог</b><span>boʻgʻin</span></li>
  <li><b>хлеб</b><span>non</span></li>
  <li><b>молоко́</b><span>sut</span></li>
  <li><b>вода́</b><span>suv</span></li>
  <li><b>сестра́</b><span>opa, singil</span></li>
  <li><b>хорошо́</b><span>yaxshi</span></li>
  <li><b>язы́к</b><span>til</span></li>
  <li><b>за́мок / замо́к</b><span>qulf / qalʼa</span></li>
  <li><b>по-ру́сски</b><span>ruschada</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Har bir soʻzda <b>bitta</b> urgʻuli boʻgʻin. U uzun va aniq, qolgani qisqa.</li>
    <li>Urgʻu <b>maʼnoni oʻzgartiradi</b> (за́мок ≠ замо́к) va soʻz oʻzgarganda
        <b>koʻchadi</b> (рука́ → ру́ки).</li>
    <li><b>Аканье:</b> urgʻusiz О → [а], uzoqdagisi → [ъ]. молоко́ [мълако́].</li>
    <li><b>Иканье:</b> urgʻusiz Е va Я → [и]. сестра́ [систра́].</li>
    <li><b>Оглушение:</b> soʻz oxirida jarangli undosh oʻz juftiga oʻtadi.
        хлеб [хлеп], друг [друк].</li>
    <li>Yangi soʻzni <b>urgʻusi bilan birga</b> yodlang — bu bir soniya, foydasi bir yil.</li>
  </ul>
</div>
""",
    },
]
