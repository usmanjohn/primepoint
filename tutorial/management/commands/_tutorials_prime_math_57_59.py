# -*- coding: utf-8 -*-
"""Prime Math — darslar 57–59 (geometriya alifbosi, burchak, burchak juftliklari).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt
**Blok E: Geometriya (57–74) boshlanishi** — bu blokda har bir darsda SVG chizma SHART.

  mashqlar — practice/management/commands/_practice_pm_57_59.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_57_59.py

⚠️ Kumulyativ chegaralar:
  • PM-57 — nuqta, toʻgʻri chiziq, kesma, nur; belgilash; ikki nuqta bitta
    toʻgʻri chiziqni aniqlaydi; kesmalarni qoʻshish AB + BC = AC; oʻrta nuqta;
  • PM-58 — burchak = umumiy boshlangʻich nuqtali ikki nur; ∠ABC yozuvi;
    transportir va ikki shkala tuzogʻi; oʻtkir/toʻgʻri/oʻtmas/yoyiq/toʻla;
    360° nima uchun 360; burchaklarni qoʻshish;
  • PM-59 — qoʻshni (180°), vertikal (teng), toʻldiruvchi (90°) burchaklar +
    vertikal burchaklar tengligining ISBOTI (kursdagi birinchi isbot).
  • ⛔ Parallel chiziqlar va kesuvchi (PM-60) YOʻQ; uchburchak burchaklari
    yigʻindisi (PM-61) YOʻQ; Pifagor (PM-64) YOʻQ; perimetr (PM-67) va yuza
    (PM-68) YOʻQ; aylana uzunligi va π (PM-70, PM-71) YOʻQ.
  • Faol ishlatiladi: sistema (PM-52…PM-55), tenglama (PM-36, PM-37), matndan
    ifoda (PM-30), masshtab va proporsiya (PM-28), koordinata (PM-45),
    kesmaning oʻrtasi (PM-46), boʻlish va foiz (PM-4, PM-23).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_57_59.py --author=prime
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
    # PM-57 — nuqta, chiziq, kesma, nur
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-57: Nuqta, chiziq, kesma, nur — geometriya alifbosi",
        "category": "math",
        "order": 57,
        "summary": (
            "Geometriyaning toʻrtta asosiy soʻzi: nuqta, toʻgʻri chiziq, kesma "
            "va nur. Ularni toʻgʻri belgilash, kesmalarni qoʻshish va nega ikki "
            "nuqta bitta toʻgʻri chiziqni aniqlashi."
        ),
        "stories": ["Chizgʻich va qalam — birinchi chizma"],
        "content": """
<h2>PM-57: Nuqta, chiziq, kesma, nur — geometriya alifbosi</h2>

<p>Doʻstingizga «maktabdan uyingizgacha qancha?» deb soʻrasangiz, u yoʻlning
<b>ikki uchi</b> bor deb oʻylaydi. «Quyoshdan chiqqan nur qayerda tugaydi?»
desangiz — javob yoʻq, chunki uning oxiri yoʻq. Mana shu farq geometriyaning
birinchi darsi.</p>

<p>Bu darsdan boshlab yangi blok — <b>geometriya</b> — boshlanadi. Sonlar
oʻrniga shakllar, lekin mantiq oʻsha-oʻsha. Va har bir yangi soʻz aniq
belgilanadi: geometriyada «taxminan shunday» degan gap yoʻq.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>nuqta, toʻgʻri chiziq, kesma va nurni bir-biridan ajratasiz;</li>
    <li>ularni harflar bilan toʻgʻri belgilaysiz;</li>
    <li>kesmalarni qoʻshasiz va oʻrta nuqtasini topasiz;</li>
    <li>nega ikki nuqta bitta toʻgʻri chiziqni aniqlashini tushuntirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrt soʻz</span>
  <span class="pe-chip pe-chip--o">nuqta</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">toʻgʻri chiziq</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">kesma</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--adv">nur</span>
</div>

<h3>Toʻrtala shakl bitta chizmada</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 195" role="img"
       aria-label="Nuqta, toʻgʻri chiziq, kesma va nur">
    <circle class="pm-pt" cx="60" cy="30" r="5"/>
    <text class="pm-lbl" x="53" y="19">A</text>
    <text class="pm-lbl pm-lbl--hl" x="150" y="35">nuqta A</text>

    <line class="pm-ln" x1="38" y1="75" x2="132" y2="75"/>
    <polygon class="pm-pt" points="30,75 42,70 42,80"/>
    <polygon class="pm-pt" points="140,75 128,70 128,80"/>
    <text class="pm-lbl pm-lbl--hl" x="150" y="80">toʻgʻri chiziq</text>

    <line class="pm-ln" x1="40" y1="120" x2="125" y2="120"/>
    <circle class="pm-pt" cx="40" cy="120" r="5"/>
    <circle class="pm-pt" cx="125" cy="120" r="5"/>
    <text class="pm-lbl" x="33" y="109">A</text>
    <text class="pm-lbl" x="118" y="109">B</text>
    <text class="pm-lbl pm-lbl--hl" x="150" y="125">kesma AB</text>

    <line class="pm-ln" x1="40" y1="165" x2="132" y2="165"/>
    <polygon class="pm-pt" points="140,165 128,160 128,170"/>
    <circle class="pm-pt" cx="40" cy="165" r="5"/>
    <circle class="pm-pt" cx="90" cy="165" r="4"/>
    <text class="pm-lbl" x="33" y="154">A</text>
    <text class="pm-lbl" x="84" y="154">B</text>
    <text class="pm-lbl pm-lbl--hl" x="150" y="170">nur AB</text>
  </svg>
  <figcaption>Strelka «bu tomonga cheksiz davom etadi» degani. Nuqtacha esa
  «shu yerda tugadi».</figcaption>
</figure>

<h3>Toʻrttasining farqi bitta jumlada</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Nomi</th><th>Yozuvi</th><th>Uzunligi bormi?</th></tr>
  <tr><td>Nuqta</td><td class="pm-word__sym">A</td><td>yoʻq — faqat oʻrin</td></tr>
  <tr><td>Toʻgʻri chiziq</td><td class="pm-word__sym">AB</td>
    <td>yoʻq — ikki tomonga cheksiz</td></tr>
  <tr><td>Kesma</td><td class="pm-word__sym">AB</td>
    <td>bor — oʻlchash mumkin</td></tr>
  <tr><td>Nur</td><td class="pm-word__sym">AB</td>
    <td>yoʻq — boshi bor, oxiri yoʻq</td></tr>
</table></div>

<p><b>Nuqta</b> — geometriyaning eng kichik soʻzi. Uning eni ham, boʻyi ham
yoʻq; u faqat <b>oʻrin</b>ni koʻrsatadi. Qogʻozdagi nuqtacha — uning rasmi,
oʻzi emas. Nuqtalar bosh harflar bilan belgilanadi: A, B, O.</p>

<p><b>Toʻgʻri chiziq</b> ikki tomonga ham cheksiz davom etadi. Uni butunlay
chizib boʻlmaydi — shuning uchun bir boʻlagini chizib, uchlariga strelka
qoʻyamiz. Ustidagi ikki nuqta bilan belgilanadi: <b>AB toʻgʻri chizigʻi</b>.</p>

<p><b>Kesma</b> — toʻgʻri chiziqning ikki nuqta orasidagi boʻlagi. Faqat
u <b>oʻlchanadi</b>: AB = 12 sm deb yozish mumkin. Maktabdan uyingizgacha
boʻlgan yoʻl — kesma.</p>

<p><b>Nur</b> — bir uchi bor, ikkinchi tomonga cheksiz. Belgilashda
<b>tartib muhim</b>: nur AB ning boshi A da, nur BA ning boshi esa B da.
Bu yagona joyki, harflarni almashtirsangiz boshqa shakl chiqadi.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Kesma AB va toʻgʻri chiziq AB — bir xil yozuv, boshqa
  narsa</p>
  <p>Ikkalasi ham «AB» deb yoziladi, farqni <b>soʻz</b> aytadi: «kesma AB» yoki
  «toʻgʻri chiziq AB». Shuning uchun javobda soʻzni tushirib qoldirmang.
  <b>«AB = 12 sm»</b> deb yozish faqat kesma haqida maʼnoga ega — toʻgʻri
  chiziqning uzunligi yoʻq.</p>
</div>

<h3>Nega ikki nuqta yetadi?</h3>

<p>Bitta nuqtadan cheksiz koʻp toʻgʻri chiziq oʻtkazish mumkin — qalamni
aylantiraverasiz. Lekin <b>ikkita</b> nuqta berilsa, ular orqali faqat
<b>bitta</b> toʻgʻri chiziq oʻtadi.</p>

<p>Buni har kuni ishlatasiz. Devorga taxta qoqayotgan usta bitta emas,
<b>ikkita</b> mix qoqadi — bitta mixda taxta aylanadi, ikkitasida qotib
qoladi. Chizgʻich ham shu qoidaga tayanadi: ikki nuqtani belgilab, ular orqali
chiziq oʻtkazasiz.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Asosiy qoida</p>
  <p>Ikki nuqta orqali <b>bitta va faqat bitta</b> toʻgʻri chiziq oʻtadi.
  Ikki toʻgʻri chiziq esa yo <b>bitta</b> nuqtada kesishadi, yo umuman
  kesishmaydi.</p>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 150" role="img" aria-label="Ikki toʻgʻri chiziq bitta nuqtada kesishadi">
    <line class="pm-ln" x1="30" y1="35" x2="290" y2="115"/>
    <line class="pm-ln" x1="30" y1="115" x2="290" y2="35"/>
    <circle class="pm-pt" cx="160" cy="75" r="6"/>
    <text class="pm-lbl pm-lbl--hl" x="168" y="66">O</text>
    <text class="pm-lbl" x="95" y="135">kesishgan yagona nuqta</text>
  </svg>
  <figcaption>Ikki toʻgʻri chiziq ikkita nuqtada kesisha olmaydi — aks holda
  ular orqali ikkita chiziq oʻtgan boʻlardi.</figcaption>
</figure>

<h3>Kesmalarni qoʻshish</h3>

<p>Agar B nuqtasi A bilan C orasida yotsa, kichik kesmalar katta kesmani
tashkil qiladi:</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 130" role="img" aria-label="AB + BC = AC">
    <line class="pm-ln pm-ln--dash" x1="40" y1="38" x2="190" y2="38"/>
    <text class="pm-lbl" x="85" y="30">AB = 12 sm</text>
    <line class="pm-ln pm-ln--dash" x1="190" y1="38" x2="280" y2="38"/>
    <text class="pm-lbl" x="196" y="30">BC = 7 sm</text>

    <line class="pm-ln" x1="40" y1="62" x2="280" y2="62"/>
    <circle class="pm-pt" cx="40" cy="62" r="5"/>
    <circle class="pm-pt" cx="190" cy="62" r="5"/>
    <circle class="pm-pt" cx="280" cy="62" r="5"/>
    <text class="pm-lbl" x="35" y="82">A</text>
    <text class="pm-lbl" x="185" y="82">B</text>
    <text class="pm-lbl" x="275" y="82">C</text>

    <line class="pm-ln pm-ln--dash" x1="40" y1="100" x2="280" y2="100"/>
    <text class="pm-lbl pm-lbl--hl" x="118" y="120">AC = 19 sm</text>
  </svg>
  <figcaption>B nuqtasi orada yotgani uchun 12 + 7 = 19.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">AB + BC = AC</span>
    <span class="pm-solve__why">B nuqtasi A bilan C orasida</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">12 + 7 = 19 sm</span>
    <span class="pm-solve__why">Butun kesmaning uzunligi</span>
  </div>
</div>

<p><b>Oʻrta nuqta</b> — kesmani ikkita teng boʻlakka boʻluvchi nuqta (PM-46 da
uni koordinatalar bilan topgan edik). Agar M — AB kesmaning oʻrtasi boʻlsa,
AM = MB = AB ÷ 2.</p>

<div class="pe-ex">
  <p class="pe-ex__math">AB = 26 sm, M — oʻrtasi → AM = 26 ÷ 2 = 13 sm</p>
  <p class="pe-ex__uz">Oʻrta nuqta kesmani teng ikkiga boʻladi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Orasida yotadi» degan shart tekinga kelmaydi</p>
  <p>AB = 12 va BC = 7 boʻlsa, AC har doim ham 19 emas. Agar C nuqtasi A bilan
  B <b>orasida</b> yotsa, u holda AC = 12 − 7 = <b>5</b>. Chizmasiz masala
  yechmang: avval nuqtalarni tartib bilan qoʻying.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Yoʻldagi uch qishloq.</b> A, B va C qishloqlari bitta toʻgʻri yoʻl ustida
joylashgan. A dan B gacha 12 km, B dan C gacha 7 km. Nodira opa A dan C ga
boradi.</p>

<p><b>Nima soʻralyapti:</b> AC masofasi. Lekin bitta savol tugʻiladi — B qayerda
turibdi?</p>

<p><b>Reja:</b> ikki holni ham koʻramiz, chunki matn B ning A bilan C orasida
ekanini aytmagan.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1-hol: A — B — C tartibda</span>
    <span class="pm-solve__why">B orada yotadi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">AC = 12 + 7 = 19 km</span>
    <span class="pm-solve__why">Kesmalar qoʻshiladi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2-hol: A — C — B tartibda</span>
    <span class="pm-solve__why">C orada yotadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">AC = 12 − 7 = 5 km</span>
    <span class="pm-solve__why">C nuqtasi B dan 7 km beri</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>1-hol: 12 + 7 = 19 ✓. 2-hol: 5 + 7 = 12 ✓ — yaʼni AC + CB haqiqatan AB ni
  beradi. <b>Javob:</b> 19 km yoki 5 km; qaysi biri ekanini bilish uchun
  qishloqlarning tartibi aytilishi kerak.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>AC hech qachon 19 dan katta va 5 dan kichik boʻlolmaydi — chunki
  7 km lik yoʻl A dan C ga faqat shu ikki tomonga qoʻshiladi yoki ayriladi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Toʻgʻri chiziq AB ning uzunligi 12 sm</p>
  <p class="pe-fix__good">Kesma AB ning uzunligi 12 sm</p>
  <p class="pe-fix__why">Toʻgʻri chiziq ikki tomonga cheksiz — uni oʻlchab
  boʻlmaydi. Oʻlchanadigan yagona shakl — <b>kesma</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Nur AB bilan nur BA — bir xil nur</p>
  <p class="pe-fix__good">Nur AB ning boshi A da, nur BA ning boshi B da</p>
  <p class="pe-fix__why">Nurda tartib maʼnoni oʻzgartiradi: birinchi harf —
  <b>boshi</b>. Kesmada esa AB va BA bir xil.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">AB = 12, BC = 7 → AC = 19 (har doim)</p>
  <p class="pe-fix__good">B orada boʻlsa 19; C orada boʻlsa 5</p>
  <p class="pe-fix__why">Nuqtalarning tartibi aytilmasa, ikki javob ham
  mumkin. Avval chizing, keyin qoʻshing.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Bitta nuqta orqali bitta toʻgʻri chiziq oʻtadi</p>
  <p class="pe-fix__good">Bitta nuqta orqali cheksiz koʻp chiziq oʻtadi;
    ikkitasi orqali — bittasi</p>
  <p class="pe-fix__why">Qalamni bitta nuqtada aylantirib koʻring — har bir
  burilishda yangi chiziq chiqadi. Ikkinchi nuqta uni qotiradi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Qaysi shaklning uzunligini oʻlchash mumkin: nuqta,
  toʻgʻri chiziq, kesma yoki nur?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Faqat kesma.</b> Nuqtaning oʻlchami yoʻq; toʻgʻri chiziq ikki
    tomonga, nur esa bir tomonga cheksiz davom etadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. M nuqtasi AB kesmasining oʻrtasi. AB = 34 sm boʻlsa,
  MB qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>17 sm.</b> Oʻrta nuqta kesmani teng ikkiga boʻladi: 34 ÷ 2 = 17.
    Tekshirish: 17 + 17 = 34 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. A, B, C nuqtalari shu tartibda bitta toʻgʻri
  chiziqda yotadi. AB = 9 sm, AC = 23 sm. BC qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>14 sm.</b> AB + BC = AC, demak BC = 23 − 9 = 14.
    Tekshirish: 9 + 14 = 23 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Nur CD ning boshi qaysi nuqtada?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>C nuqtasida.</b> Nurni belgilashda birinchi harf har doim uning
    boshini bildiradi, ikkinchisi esa yoʻnalishini koʻrsatadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Tekislikda 4 ta nuqta bor va ularning hech qaysi
  uchtasi bitta toʻgʻri chiziqda yotmaydi. Ular orqali nechta toʻgʻri chiziq
  oʻtkazish mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6 ta.</b> Har bir juft nuqta bitta chiziq beradi. Juftlarni sanaymiz:
    AB, AC, AD, BC, BD, CD — 6 ta. (Birinchi nuqtani 4 xil, ikkinchisini 3 xil
    tanlaymiz: 4 × 3 = 12, lekin AB bilan BA bir xil, shuning uchun
    12 ÷ 2 = 6.)</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Xonaning rejasi 1 : 50 masshtabda chizilgan. Rejadagi
  devor kesmasi 12 sm. Devor aslida necha metr?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6 metr.</b> 1 : 50 degani rejadagi 1 sm — haqiqatda 50 sm (PM-28).
    12 × 50 = 600 sm = 6 m. Tekshirish: 6 m = 600 sm, 600 ÷ 50 = 12 sm ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Nuqta</b><span>oʻlchamsiz, faqat oʻrinni koʻrsatuvchi shakl; ingl.
    point</span></li>
  <li><b>Toʻgʻri chiziq</b><span>ikki tomonga cheksiz davom etuvchi chiziq;
    ingl. line</span></li>
  <li><b>Kesma</b><span>ikki uchi bor, oʻlchanadigan chiziq boʻlagi; ingl.
    segment</span></li>
  <li><b>Nur</b><span>boshi bor, oxiri yoʻq chiziq; ingl. ray</span></li>
  <li><b>Oʻrta nuqta</b><span>kesmani teng ikkiga boʻluvchi nuqta; ingl.
    midpoint</span></li>
  <li><b>Kesishish nuqtasi</b><span>ikki chiziq uchrashgan joy; ingl. point of
    intersection</span></li>
  <li><b>Tekislik</b><span>cheksiz tekis yuza — chizmamiz shu yerda yotadi;
    ingl. plane</span></li>
  <li><b>Uch</b><span>kesma yoki nurning boshlangʻich nuqtasi; ingl.
    endpoint</span></li>
  <li><b>Masshtab</b><span>chizmadagi 1 sm haqiqatda qanchaligi; ingl.
    scale</span></li>
  <li><b>Chizma</b><span>shakllarning aniq oʻlchovli tasviri; ingl.
    diagram</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Faqat kesmaning uzunligi bor.</b> Toʻgʻri chiziq ham, nur ham
      cheksiz.</li>
    <li><b>Nurda tartib muhim:</b> nur AB ≠ nur BA. Kesmada esa AB = BA.</li>
    <li><b>Ikki nuqta bitta toʻgʻri chiziqni aniqlaydi</b> — usta ham shuning
      uchun ikkita mix qoqadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-58 — burchak va uni oʻlchash
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-58: Burchak va uni oʻlchash",
        "category": "math",
        "order": 58,
        "summary": (
            "Burchak — umumiy boshlangʻich nuqtali ikki nur. ∠ABC yozuvi, "
            "transportir bilan oʻlchash va ikki shkala tuzogʻi, oʻtkir, toʻgʻri, "
            "oʻtmas, yoyiq va toʻla burchaklar."
        ),
        "stories": ["Soat millari orasidagi burchak"],
        "content": """
<h2>PM-58: Burchak va uni oʻlchash</h2>

<p>Eshikni yarim ochsangiz — bir burchak. Toʻliq ochsangiz — boshqa burchak.
Eshikning oʻzi oʻzgarmadi, faqat <b>qanchalik burilgani</b> oʻzgardi. Burchak
mana shuni oʻlchaydi: uzunlikni emas, <b>burilishni</b>.</p>

<p>PM-57 da nur bilan tanishdik. Endi bitta nuqtadan chiqqan <b>ikkita</b> nurni
olamiz — shu joyda burchak paydo boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>burchakning uchi va tomonlarini koʻrsatasiz;</li>
    <li>∠ABC yozuvini toʻgʻri oʻqiysiz va yozasiz;</li>
    <li>transportir bilan oʻlchaysiz va ikki shkala tuzogʻiga tushmaysiz;</li>
    <li>oʻtkir, toʻgʻri, oʻtmas, yoyiq va toʻla burchakni ajratasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Burchak</span>
  <span class="pe-chip pe-chip--o">bitta uch</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">ikkita nur</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">∠ABC</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">gradus (°)</span>
</div>

<h3>Burchakning qismlari</h3>

<figure class="pm-fig">
  <svg viewBox="0 0 320 170" role="img" aria-label="Burchakning uchi va tomonlari">
    <line class="pm-ln" x1="70" y1="130" x2="285" y2="130"/>
    <line class="pm-ln" x1="70" y1="130" x2="245" y2="35"/>
    <path class="pm-ln pm-ln--hl" d="M 120 130 A 50 50 0 0 0 114 105" fill="none"/>
    <circle class="pm-pt" cx="70" cy="130" r="5"/>
    <circle class="pm-pt" cx="285" cy="130" r="4"/>
    <circle class="pm-pt" cx="245" cy="35" r="4"/>
    <text class="pm-lbl" x="60" y="150">B</text>
    <text class="pm-lbl" x="288" y="146">C</text>
    <text class="pm-lbl" x="250" y="30">A</text>
    <text class="pm-lbl pm-lbl--hl" x="128" y="118">∠ABC</text>
    <text class="pm-lbl" x="30" y="115">uch</text>
    <text class="pm-lbl" x="150" y="150">tomon</text>
  </svg>
  <figcaption>Uchi — B. Tomonlari — BA va BC nurlari. Yozuvda uch har doim
  <b>oʻrtada</b> turadi.</figcaption>
</figure>

<p><b>Uchi</b> — ikki nur chiqqan nuqta. <b>Tomonlari</b> — oʻsha ikki nurning
oʻzi. Burchak uch harf bilan belgilanadi va <b>uchning harfi oʻrtada</b>
yoziladi: ∠ABC yoki ∠CBA — ikkalasi bir xil burchak. Chalkashlik boʻlmasa,
qisqasi ham mumkin: ∠B.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Oʻrtadagi harf — bu uch</p>
  <p>∠ABC va ∠BAC <b>boshqa-boshqa</b> burchaklar: birinchisining uchi B,
  ikkinchisiniki A. Bitta harfni surib yuborish butun burchakni almashtiradi.
  Yozishdan oldin oʻzingizga ayting: «uchi qayerda?»</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Tomonning uzunligi burchakka taʼsir qilmaydi</p>
  <p>Tomonlarni uzaytirsangiz ham burchak oʻzgarmaydi — u nurlar orasidagi
  <b>burilish</b>ni oʻlchaydi. Chizmada uzun koʻringan burchak kattaroq degani
  emas.</p>
</div>

<h3>Gradus: nega aynan 360?</h3>

<p>Toʻliq bir aylanish — <b>360°</b>. Bu son osmondan tushmagan. Uni qadimgi
Bobil olimlari tanlagan: ularning sanoq sistemasi 60 lik edi, yil esa taxminan
360 kunga boʻlingan deb hisoblangan. Eng qulayi shundaki, <b>360 juda koʻp
songa qoldiqsiz boʻlinadi</b>: 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30,
36, 45, 60, 72, 90, 120, 180 ga.</p>

<p>Shuning uchun tortni 8 ta teng boʻlakka boʻlish oson: 360 ÷ 8 = 45°. Agar
aylanish 100 birlik boʻlganida, 8 ga boʻlganda kasr chiqardi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">360° ÷ 4 = 90°, 360° ÷ 2 = 180°, 360° ÷ 12 = 30°</p>
  <p class="pe-ex__uz">Chorak aylanish — 90°, yarim aylanish — 180°, soat
  siferblatidagi bir boʻlim — 30°.</p>
</div>

<h3>Burchak turlari</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Nomi</th><th>Kattaligi</th><th>Qayerda koʻrasiz</th></tr>
  <tr><td>Oʻtkir</td><td class="pm-word__sym">0° &lt; a &lt; 90°</td>
    <td>qaychining uchi</td></tr>
  <tr><td>Toʻgʻri</td><td class="pm-word__sym">a = 90°</td>
    <td>daftar varagʻining burchagi</td></tr>
  <tr><td>Oʻtmas</td><td class="pm-word__sym">90° &lt; a &lt; 180°</td>
    <td>ochilgan noutbuk</td></tr>
  <tr><td>Yoyiq</td><td class="pm-word__sym">a = 180°</td>
    <td>toʻgʻri chiziq</td></tr>
  <tr><td>Toʻla</td><td class="pm-word__sym">a = 360°</td>
    <td>toʻliq aylanish</td></tr>
</table></div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 120" role="img" aria-label="Oʻtkir, toʻgʻri, oʻtmas va yoyiq burchak">
    <line class="pm-ln" x1="20" y1="80" x2="80" y2="80"/>
    <line class="pm-ln" x1="20" y1="80" x2="70" y2="42"/>
    <path class="pm-ln pm-ln--hl" d="M 40 80 A 20 20 0 0 0 35 68" fill="none"/>
    <text class="pm-lbl" x="20" y="103">oʻtkir</text>

    <line class="pm-ln" x1="105" y1="80" x2="165" y2="80"/>
    <line class="pm-ln" x1="105" y1="80" x2="105" y2="30"/>
    <rect class="pm-ln" x="105" y="66" width="14" height="14" fill="none"/>
    <text class="pm-lbl" x="103" y="103">toʻgʻri</text>

    <line class="pm-ln" x1="205" y1="80" x2="255" y2="80"/>
    <line class="pm-ln" x1="205" y1="80" x2="170" y2="42"/>
    <path class="pm-ln pm-ln--hl" d="M 225 80 A 20 20 0 0 0 191 66" fill="none"/>
    <text class="pm-lbl" x="192" y="103">oʻtmas</text>

    <line class="pm-ln" x1="262" y1="80" x2="312" y2="80"/>
    <circle class="pm-pt" cx="287" cy="80" r="4"/>
    <path class="pm-ln pm-ln--hl" d="M 305 80 A 18 18 0 0 0 269 80" fill="none"/>
    <text class="pm-lbl" x="268" y="103">yoyiq</text>
  </svg>
  <figcaption>Toʻgʻri burchak yoy bilan emas, <b>kvadratcha</b> bilan
  belgilanadi — bu xalqaro odat.</figcaption>
</figure>

<h3>Transportir bilan oʻlchash</h3>

<p>Uch qadam, tartibi buzilmaydi:</p>

<div class="pe-steps">
  <ol>
    <li>Transportirning <b>markazi</b> burchakning uchiga aniq tushsin.</li>
    <li>Bitta tomon <b>0</b> chizigʻi ustida yotsin.</li>
    <li>Ikkinchi tomon qaysi songa tegsa — oʻsha javob.</li>
  </ol>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 320 190" role="img" aria-label="Transportir bilan burchak oʻlchash">
    <path class="pm-ln" d="M 50 150 A 110 110 0 0 1 270 150" fill="none"/>
    <line class="pm-ln" x1="50" y1="150" x2="270" y2="150"/>
    <line class="pm-ln pm-ln--hl" x1="160" y1="150" x2="215" y2="55"/>
    <line class="pm-ln pm-ln--hl" x1="160" y1="150" x2="270" y2="150"/>
    <circle class="pm-pt" cx="160" cy="150" r="5"/>
    <text class="pm-lbl pm-lbl--hl" x="196" y="76">60</text>
    <text class="pm-lbl" x="216" y="44">120</text>
    <text class="pm-lbl" x="248" y="170">0°</text>
    <text class="pm-lbl" x="30" y="170">180°</text>
    <text class="pm-lbl" x="118" y="182">markaz uchda</text>
  </svg>
  <figcaption>Bitta nur — ikkita son. Toʻgʻrisi 60°, chunki ikkinchi tomon
  <b>oʻng</b> tomondagi 0 da yotibdi.</figcaption>
</figure>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Ikki shkala tuzogʻi — eng koʻp uchraydigan xato</p>
  <p>Transportirda ikki qator son bor: biri chapdan oʻngga, ikkinchisi
  oʻngdan chapga. Bitta nur ikkalasini ham kesib oʻtadi — masalan 60 va 120.
  Qoida oddiy: <b>burchakning ikkinchi tomoni qaysi shkaladagi 0 da yotgan
  boʻlsa, javobni ham oʻsha shkaladan oʻqing.</b>
  <br>Tekshiruv usuli yanada oson: burchak koʻzga <b>oʻtkir</b> koʻrinsa, javob
  90 dan kichik boʻlishi shart.</p>
</div>

<h3>Burchaklarni qoʻshish</h3>

<p>Agar OB nuri ∠AOC ning ichida yotsa, ikki kichik burchak kattasini
tashkil qiladi — xuddi kesmalardagidek:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠AOB + ∠BOC = ∠AOC</span>
    <span class="pm-solve__why">OB nuri katta burchakning ichida</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">35° + 50° = 85°</span>
    <span class="pm-solve__why">Demak ∠AOC oʻtkir burchak</span>
  </div>
</div>

<h3>Matnli masala</h3>

<p><b>Doira shaklidagi gulzor.</b> Bogʻdagi doira shaklidagi gulzor markazidan
chiqqan yoʻlchalar bilan 8 ta teng boʻlakka boʻlingan. Bekzod ulardan 3 tasiga
lola ekdi.</p>

<p><b>Nima soʻralyapti:</b> (a) bitta boʻlakning markazdagi burchagi;
(b) lola ekilgan qismning burchagi; (c) necha boʻlak yoyiq burchak beradi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">360° ÷ 8 = 45°</span>
    <span class="pm-solve__why">Toʻla burchak 8 ta teng boʻlakka boʻlindi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 × 45° = 135°</span>
    <span class="pm-solve__why">Uch boʻlak — burchaklar qoʻshiladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">180° ÷ 45° = 4 boʻlak</span>
    <span class="pm-solve__why">Yoyiq burchak — gulzorning teng yarmi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>8 × 45° = 360° ✓ — barcha boʻlaklar toʻla aylanani beradi. 135° soni 90
  bilan 180 orasida, demak <b>oʻtmas</b> burchak — chizmada ham shunday
  koʻrinadi ✓</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>3 boʻlak — sakkizdan uchi, yaʼni yarmidan sal kam. 135° ham 180° dan
  sal kam. Javob mantiqiy.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Uchi B boʻlgan burchak: ∠BAC</p>
  <p class="pe-fix__good">Uchi B boʻlgan burchak: ∠ABC</p>
  <p class="pe-fix__why">Uchning harfi <b>oʻrtada</b> yoziladi. Bu — burchak
  yozuvining yagona qatʼiy qoidasi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Koʻzga oʻtkir koʻringan burchak: 120°</p>
  <p class="pe-fix__good">Oʻtkir burchak: 60°</p>
  <p class="pe-fix__why">Transportirning notoʻgʻri shkalasi oʻqilgan.
  Oʻtkir burchak har doim 90 dan <b>kichik</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Tomonlari uzunroq chizilgan burchak kattaroq</p>
  <p class="pe-fix__good">Burchak tomonlarning uzunligiga bogʻliq emas</p>
  <p class="pe-fix__why">Burchak — <b>burilish</b>. Nurlarni cheksiz
  uzaytirsangiz ham ular orasidagi burilish oʻzgarmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Yoyiq burchak — bu burchak emas, toʻgʻri chiziq</p>
  <p class="pe-fix__good">Yoyiq burchak — 180° li burchak</p>
  <p class="pe-fix__why">Tomonlari qarama-qarshi nurlar boʻlgani uchun u
  toʻgʻri chiziqqa oʻxshaydi, lekin baribir burchak — va uni oʻlchash
  mumkin.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. ∠MNP burchagining uchi qaysi nuqtada?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>N nuqtasida.</b> Yozuvda oʻrtadagi harf har doim uchni bildiradi;
    M va P esa tomonlaridagi nuqtalar.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 115° li burchak qaysi turga kiradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Oʻtmas.</b> 90° dan katta, 180° dan kichik. Oʻtkir boʻlishi uchun
    90 dan kichik boʻlishi kerak edi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. ∠AOB = 28° va ∠BOC = 47°. OB nuri ∠AOC ning ichida
  yotadi. ∠AOC qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>75°.</b> Burchaklar qoʻshiladi: 28 + 47 = 75. Bu hali ham 90 dan
    kichik, demak ∠AOC oʻtkir burchak.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Pitsa 12 ta teng boʻlakka kesildi. Bitta boʻlakning
  markazdagi burchagi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>30°.</b> 360 ÷ 12 = 30. Tekshirish: 12 × 30 = 360 ✓ — hamma
    boʻlaklar toʻla aylanani toʻldiradi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Sherbek shimolga qarab turibdi. U oʻng tomonga 90°
  buriladi, keyin yana oʻngga 45° buriladi. Endi qaysi tomonga qarab turibdi va
  jami necha gradus burildi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Janubi-sharqqa; jami 135°.</b> Shimoldan oʻngga 90° — bu sharq.
    Sharqdan yana 45° — sharq bilan janub orasidagi yoʻnalish, yaʼni
    janubi-sharq. Burilishlar qoʻshiladi: 90 + 45 = 135°.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Dilnoza tortni teng boʻlaklarga kesdi va har bir
  boʻlakning burchagi 24° chiqdi. U nechta boʻlak kesgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>15 ta boʻlak.</b> 360 ÷ 24 = 15. Tekshirish: 15 × 24 = 360 ✓
    Boʻlaklar soni har doim 360 ni burchakka boʻlish bilan topiladi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Burchak</b><span>umumiy boshlangʻich nuqtali ikki nur; ingl.
    angle</span></li>
  <li><b>Burchakning uchi</b><span>nurlar chiqqan nuqta; ingl. vertex</span></li>
  <li><b>Burchak tomoni</b><span>uchdan chiqqan nurlardan biri; ingl.
    side</span></li>
  <li><b>Gradus</b><span>burchak oʻlchov birligi, aylananing 360 dan biri;
    ingl. degree</span></li>
  <li><b>Transportir</b><span>burchak oʻlchaydigan asbob; ingl.
    protractor</span></li>
  <li><b>Oʻtkir burchak</b><span>90° dan kichik; ingl. acute angle</span></li>
  <li><b>Toʻgʻri burchak</b><span>aniq 90°; ingl. right angle</span></li>
  <li><b>Oʻtmas burchak</b><span>90° bilan 180° orasida; ingl. obtuse
    angle</span></li>
  <li><b>Yoyiq burchak</b><span>aniq 180°; ingl. straight angle</span></li>
  <li><b>Toʻla burchak</b><span>toʻliq aylanish, 360°; ingl. full angle</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Burchak burilishni oʻlchaydi,</b> uzunlikni emas — tomonlarni
      uzaytirish hech narsani oʻzgartirmaydi.</li>
    <li><b>Yozuvda uch oʻrtada:</b> ∠ABC ning uchi B.</li>
    <li><b>Transportirda ikki shkala bor.</b> Ikkinchi tomon qaysi 0 da yotsa,
      javobni oʻsha qatordan oʻqing.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-59 — burchak juftliklari
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-59: Burchak juftliklari: qoʻshni, vertikal, toʻldiruvchi",
        "category": "math",
        "order": 59,
        "summary": (
            "Ikki chiziq kesishganda hosil boʻlgan burchaklar bir-biriga "
            "bogʻlangan: qoʻshnilar 180° ni, toʻldiruvchilar 90° ni beradi, "
            "vertikallar esa teng. Kursdagi birinchi isbot ham shu yerda."
        ),
        "stories": ["Chorrahadagi burchaklar"],
        "content": """
<h2>PM-59: Burchak juftliklari: qoʻshni, vertikal, toʻldiruvchi</h2>

<p>Ikki koʻcha kesishgan chorrahaga tepadan qarang: toʻrtta burchak koʻrinadi.
Ulardan bittasini oʻlchasangiz — qolgan uchtasini <b>oʻlchamasdan</b> ayta
olasiz. Bu darsda nima uchun shundayligini koʻramiz.</p>

<p>PM-58 da burchaklarni oʻlchadik. Endi ular <b>bir-biri bilan</b> qanday
bogʻlanishini oʻrganamiz — geometriyaning butun kuchi shu bogʻlanishlarda.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>qoʻshni, vertikal va toʻldiruvchi burchaklarni tanib olasiz;</li>
    <li>bitta burchakdan qolganlarini hisoblaysiz;</li>
    <li>vertikal burchaklar nega teng ekanini <b>isbotlaysiz</b>;</li>
    <li>burchakli masalalarni tenglama va sistema bilan yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch juftlik</span>
  <span class="pe-chip pe-chip--s">toʻldiruvchi = 90°</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">qoʻshni = 180°</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">vertikal → teng</span>
</div>

<h3>Qoʻshni burchaklar: yigʻindisi 180°</h3>

<p>Toʻgʻri chiziq ustidagi bir nuqtadan yuqoriga nur chiqaring. Chiziqning
ikki tomoni ikkita burchak hosil qiladi. Ular birgalikda <b>yoyiq burchak</b>ni
toʻldiradi, demak yigʻindisi 180°.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 130" role="img" aria-label="Qoʻshni burchaklar">
    <line class="pm-ln" x1="30" y1="95" x2="290" y2="95"/>
    <line class="pm-ln pm-ln--hl" x1="160" y1="95" x2="215" y2="25"/>
    <circle class="pm-pt" cx="160" cy="95" r="5"/>
    <path class="pm-ln" d="M 200 95 A 40 40 0 0 0 185 64" fill="none"/>
    <path class="pm-ln" d="M 194 52 A 55 55 0 0 0 105 95" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="204" y="76">a</text>
    <text class="pm-lbl pm-lbl--hl" x="127" y="38">b</text>
    <text class="pm-lbl" x="95" y="120">a + b = 180°</text>
  </svg>
  <figcaption>Ikkalasi birga toʻgʻri chiziqni, yaʼni yoyiq burchakni
  toʻldiradi.</figcaption>
</figure>

<div class="pe-ex">
  <p class="pe-ex__math">a = 65° → b = 180° − 65° = 115°</p>
  <p class="pe-ex__uz">Qoʻshni burchakni topish uchun 180 dan ayiramiz.</p>
  <p class="pe-ex__why">Tekshirish: 65 + 115 = 180 ✓</p>
</div>

<h3>Toʻldiruvchi burchaklar: yigʻindisi 90°</h3>

<p>Toʻgʻri burchakni bitta nur bilan ikkiga boʻlsangiz, hosil boʻlgan ikki
burchak <b>toʻldiruvchi</b> deyiladi: ular birgalikda 90° ni beradi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 130" role="img" aria-label="Toʻldiruvchi burchaklar">
    <line class="pm-ln" x1="90" y1="100" x2="250" y2="100"/>
    <line class="pm-ln" x1="90" y1="100" x2="90" y2="20"/>
    <line class="pm-ln pm-ln--hl" x1="90" y1="100" x2="160" y2="35"/>
    <rect class="pm-ln" x="90" y="86" width="14" height="14" fill="none"/>
    <circle class="pm-pt" cx="90" cy="100" r="5"/>
    <text class="pm-lbl pm-lbl--hl" x="125" y="92">a</text>
    <text class="pm-lbl pm-lbl--hl" x="100" y="55">b</text>
    <text class="pm-lbl" x="150" y="122">a + b = 90°</text>
  </svg>
  <figcaption>Toʻgʻri burchak ikkiga boʻlindi — boʻlaklar bir-birini
  toʻldiradi.</figcaption>
</figure>

<div class="pe-call pe-uz">
  <p class="pe-call__t">90 va 180 ni adashtirmang</p>
  <p><b>Toʻldiruvchi</b> — 90° gacha (toʻgʻri burchakni toʻldiradi).
  <b>Qoʻshni</b> — 180° gacha (yoyiq burchakni toʻldiradi). Chizmaga qarang:
  agar ikki burchak birga <b>toʻgʻri chiziq</b> hosil qilsa — 180;
  agar <b>burchakcha</b> hosil qilsa — 90.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Tekshiruvni ishorasidan biling</p>
  <p>Oʻtkir burchakning qoʻshnisi <b>har doim</b> oʻtmas boʻladi va aksincha —
  chunki ikkalasi birga 180° ni beradi. Javobingiz «65° va 40°» chiqsa,
  qoʻshimcha hisobsiz ham xato borligini bilasiz.</p>
</div>

<h3>Vertikal burchaklar: ular teng</h3>

<p>Ikki toʻgʻri chiziq kesishganda toʻrtta burchak hosil boʻladi. Bir-biriga
<b>qarama-qarshi</b> yotganlari vertikal burchaklar deyiladi — va ular har doim
teng.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 190" role="img" aria-label="Ikki chiziq kesishganda hosil boʻlgan toʻrt burchak">
    <line class="pm-ln" x1="30" y1="35" x2="290" y2="145"/>
    <line class="pm-ln" x1="30" y1="145" x2="290" y2="35"/>
    <circle class="pm-pt" cx="160" cy="90" r="5"/>
    <text class="pm-lbl pm-lbl--hl" x="155" y="60">1</text>
    <text class="pm-lbl pm-lbl--hl" x="205" y="97">2</text>
    <text class="pm-lbl pm-lbl--hl" x="155" y="128">3</text>
    <text class="pm-lbl pm-lbl--hl" x="108" y="97">4</text>
    <text class="pm-lbl" x="52" y="178">∠1 = ∠3 · ∠2 = ∠4 · ∠1 + ∠2 = 180°</text>
  </svg>
  <figcaption>Qarama-qarshi yotgan juftliklar teng, yonma-yon yotganlari esa
  180° ni beradi.</figcaption>
</figure>

<h3>Isbot — kursdagi birinchisi</h3>

<p>«Teng» deyish kifoya emas; geometriyada <b>nega</b> tengligini koʻrsatish
kerak. Isbot deganda mana shu — bir necha maʼlum qoidadan yangi qoidani
keltirib chiqarish. Bizga faqat bitta narsa kerak: qoʻshni burchaklar
180° beradi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠1 + ∠2 = 180°</span>
    <span class="pm-solve__why">Ular qoʻshni — birga yoyiq burchak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠2 + ∠3 = 180°</span>
    <span class="pm-solve__why">Bular ham qoʻshni</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠1 + ∠2 = ∠2 + ∠3</span>
    <span class="pm-solve__why">Ikkalasi ham 180° ga teng, demak oʻzaro
    teng</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">∠1 = ∠3</span>
    <span class="pm-solve__why">Ikki tomondan ∠2 ni ayirdik (PM-36)</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Isbotning mohiyati</p>
  <p>Biz bitta ham burchakni oʻlchamadik. Faqat maʼlum qoidadan foydalanib,
  yangi qoidani <b>keltirib chiqardik</b> — endi u <b>hamma</b> kesishgan
  chiziqlar uchun toʻgʻri, faqat bizning chizmamiz uchun emas. Oʻlchov bitta
  chizma haqida gapiradi, isbot esa barchasi haqida.</p>
</div>

<h3>Bitta burchakdan toʻrttasini topish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠1 = 65°</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠2 = 180° − 65° = 115°</span>
    <span class="pm-solve__why">∠1 ga qoʻshni</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠3 = 65°</span>
    <span class="pm-solve__why">∠1 ga vertikal — teng</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">∠4 = 115°</span>
    <span class="pm-solve__why">∠2 ga vertikal — teng</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Toʻrtta burchak birgalikda toʻla aylanani berishi kerak:
  65 + 115 + 65 + 115 = 360° ✓</p>
</div>

<h3>Burchaklar va tenglama</h3>

<p>Burchak masalalari koʻpincha tenglamaga aylanadi. Ikkita namuna:</p>

<div class="pe-ex">
  <p class="pe-ex__math">Qoʻshni burchaklardan biri ikkinchisidan 3 marta
  katta.</p>
  <p class="pe-ex__uz">x + 3x = 180 → 4x = 180 → x = 45. Burchaklar 45° va
  135°.</p>
  <p class="pe-ex__why">Tekshirish: 45 + 135 = 180 ✓ va 135 ÷ 45 = 3 ✓</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">Burchak oʻzining toʻldiruvchisidan 20° katta.</p>
  <p class="pe-ex__uz">x + y = 90 va x − y = 20 → x = 55°, y = 35° (PM-54
  dagi qoʻshish usuli).</p>
  <p class="pe-ex__why">Tekshirish: 55 + 35 = 90 ✓ va 55 − 35 = 20 ✓</p>
</div>

<h3>Matnli masala</h3>

<p><b>Chorraha.</b> Ikki toʻgʻri koʻcha kesishadi. Yoʻl xaritasida ulardan
hosil boʻlgan burchaklardan biri <b>72°</b> deb koʻrsatilgan. Yoʻl belgisini
oʻrnatuvchi usta qolgan uchta burchakni ham bilishi kerak.</p>

<p><b>Nima soʻralyapti:</b> toʻrtala burchak va ularning yigʻindisi.</p>

<p><b>Reja:</b> berilgan burchakka qoʻshnisini 180° dan topamiz, keyin har
biriga vertikalini yozamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1-burchak = 72°</span>
    <span class="pm-solve__why">Xaritada berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2-burchak = 180° − 72° = 108°</span>
    <span class="pm-solve__why">Qoʻshni burchak</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3-burchak = 72°</span>
    <span class="pm-solve__why">1-burchakka vertikal</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">4-burchak = 108°</span>
    <span class="pm-solve__why">2-burchakka vertikal</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>72 + 108 + 72 + 108 = 360° ✓ — toʻla aylana.
  <br><b>Javob:</b> 72°, 108°, 72° va 108°. Usta bitta oʻlchov bilan butun
  chorrahani biladi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>72° oʻtkir, demak qoʻshnisi albatta oʻtmas boʻlishi kerak — 108°
  shu talabga javob beradi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Vertikal burchaklarning yigʻindisi 180°</p>
  <p class="pe-fix__good">Vertikal burchaklar <b>teng</b>; 180° beradiganlari
    qoʻshnilari</p>
  <p class="pe-fix__why">Qarama-qarshi yotgan burchak — teng nusxa. Yonma-yon
  yotgani esa toʻgʻri chiziqni toʻldiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Toʻldiruvchi burchak: 180° − 40° = 140°</p>
  <p class="pe-fix__good">Toʻldiruvchi burchak: 90° − 40° = 50°</p>
  <p class="pe-fix__why">Toʻldiruvchi 90 ga qadar toʻldiradi, 180 ga qadar
  emas. 140° — bu 40° ning <b>qoʻshnisi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Chizmada teng koʻringani uchun ∠1 = ∠2</p>
  <p class="pe-fix__good">∠1 = ∠3, chunki ular vertikal</p>
  <p class="pe-fix__why">Geometriyada «koʻzga shunday koʻrindi» dalil emas.
  Chizma qoʻlda chizilgani uchun aldashi mumkin — qoidaga tayaning.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">130° li burchakning toʻldiruvchisi 40°</p>
  <p class="pe-fix__good">130° li burchakning toʻldiruvchisi <b>yoʻq</b></p>
  <p class="pe-fix__why">Toʻldiruvchisi boʻlishi uchun burchak 90° dan kichik
  boʻlishi shart, aks holda ikkinchisi manfiy chiqib qoladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Burchak 38°. Uning qoʻshnisi va toʻldiruvchisi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Qoʻshnisi 142°, toʻldiruvchisi 52°.</b> 180 − 38 = 142 va
    90 − 38 = 52. Tekshirish: 38 + 142 = 180 ✓, 38 + 52 = 90 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Ikki chiziq kesishdi va burchaklardan biri 90°
  chiqdi. Qolgan uchtasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Uchalasi ham 90°.</b> Qoʻshnisi 180 − 90 = 90, vertikallari ham
    90. Demak bitta toʻgʻri burchak butun chorrahani toʻgʻri burchakka
    aylantiradi — bunday chiziqlar perpendikulyar deyiladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Qoʻshni burchaklardan biri ikkinchisidan 40° katta.
  Ularni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>110° va 70°.</b> x + y = 180 va x − y = 40. Qoʻshamiz: 2x = 220,
    x = 110, keyin y = 70. Tekshirish: 110 + 70 = 180 ✓ va 110 − 70 = 40 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Burchak oʻzining toʻldiruvchisiga teng. U necha
  gradus?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>45°.</b> x + x = 90, demak 2x = 90 va x = 45. Toʻgʻri burchakni teng
    ikkiga boʻlgan holat.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Burchak oʻzining qoʻshnisidan 4 marta kichik. Ikkala
  burchakni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>36° va 144°.</b> x + 4x = 180, 5x = 180, x = 36, demak ikkinchisi
    4 × 36 = 144. Tekshirish: 36 + 144 = 180 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Bogʻdagi ikki yoʻlcha kesishadi. Bogʻbon
  burchaklardan birini 55° deb oʻlchadi. Qolgan uchtasini oʻlchamasdan ayting
  va toʻrttasining yigʻindisini tekshiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>125°, 55° va 125°.</b> Qoʻshnisi 180 − 55 = 125; vertikallari esa
    55 va 125. Yigʻindisi: 55 + 125 + 55 + 125 = 360° ✓ — toʻla aylana, demak
    hisob toʻgʻri.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Qoʻshni burchaklar</b><span>yigʻindisi 180° boʻlgan yonma-yon
    burchaklar; ingl. adjacent (supplementary) angles</span></li>
  <li><b>Toʻldiruvchi burchaklar</b><span>yigʻindisi 90° boʻlgan burchaklar;
    ingl. complementary angles</span></li>
  <li><b>Vertikal burchaklar</b><span>kesishgan chiziqlarda qarama-qarshi
    yotgan teng burchaklar; ingl. vertical angles</span></li>
  <li><b>Perpendikulyar</b><span>toʻgʻri burchak ostida kesishuvchi; ingl.
    perpendicular</span></li>
  <li><b>Isbot</b><span>maʼlum qoidalardan yangi qoidani keltirib chiqarish;
    ingl. proof</span></li>
  <li><b>Yoyiq burchak</b><span>180° li burchak; ingl. straight angle</span></li>
  <li><b>Toʻla burchak</b><span>360° li burchak; ingl. full angle</span></li>
  <li><b>Kesishish</b><span>ikki chiziqning umumiy nuqtasi; ingl.
    intersection</span></li>
  <li><b>Burchak bissektrisasi</b><span>burchakni teng ikkiga boʻluvchi nur;
    ingl. angle bisector</span></li>
  <li><b>Qarama-qarshi nurlar</b><span>bir nuqtadan ikki tomonga ketgan
    nurlar; ingl. opposite rays</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Qoʻshni — 180°, toʻldiruvchi — 90°, vertikal — teng.</b> Uch juftlik,
      uch qoida.</li>
    <li><b>Bitta burchak yetadi:</b> kesishgan chiziqlarning qolgan uchtasi
      undan chiqadi.</li>
    <li><b>Chizmaga emas, qoidaga ishoning.</b> Vertikal burchaklar teng —
      buni oʻlchov emas, <b>isbot</b> koʻrsatdi.</li>
  </ul>
</div>
""",
    },
]
