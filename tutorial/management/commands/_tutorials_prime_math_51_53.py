# -*- coding: utf-8 -*-
"""Prime Math — darslar 51–53 (real grafikni oʻqish, kesishish/sistema, oʻrniga qoʻyish).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

  mashqlar — practice/management/commands/_practice_pm_51_53.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_51_53.py

⚠️ Kumulyativ chegaralar:
  • PM-51 — grafikni oʻqish: oʻqlar va birlik, shkala, koʻtarilish/tekis/pasayish,
    masofa–vaqt grafigi, eng tez oʻzgarish. Formula tuzish emas — OʻQISH;
  • PM-52 — kesishgan nuqta = ikkala shartni bajaradigan juftlik; «sistema»
    tushunchasi; grafik usul; ikkalasi ham y = … boʻlsa TENGLASHTIRISH
    (bu PM-37 ning ikki tomonli tenglamasi). Uch hol: bitta yechim, yechim
    yoʻq, cheksiz koʻp;
  • PM-53 — oʻrniga qoʻyish usuli: ifodala → qoʻy → yech → qaytar → tekshir.
    ⛔ Qoʻshish usuli YOʻQ — u PM-54;
  • parabola (PM-56), Pifagor (PM-64), oʻrta arifmetik (PM-78) YOʻQ;
  • y = kx + b (PM-49, PM-50), tenglama (PM-36, PM-37), qavs ochish (PM-33),
    tezlik formulasi (PM-35), koordinata (PM-45) va foiz (PM-23) faol ishlatiladi.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_51_53.py --author=prime
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
    # PM-51 — real hayot grafigini oʻqish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-51: Real hayot grafigini oʻqish: tarif, harakat, oʻsish",
        "category": "math",
        "order": 51,
        "summary": (
            "Gazetadagi, telefondagi va shifokordagi grafiklarni oʻqish: oʻqlar "
            "nimani koʻrsatadi, bitta katak qancha, chiziq qayerda koʻtariladi, "
            "qayerda tekis turadi va qayerda eng tez oʻzgaradi."
        ),
        "stories": ["Grafik nima deyapti? — mavsum natijalari"],
        "content": """
<h2>PM-51: Real hayot grafigini oʻqish: tarif, harakat, oʻsish</h2>

<p>Telefoningizni oching va batareya sarfiga qarang. U yerda sonlar emas, chiziq
turadi. Yangiliklardagi valyuta kursi, shifokordagi harorat qogʻozi, sinf
devoridagi natijalar jadvali — hammasi grafik.</p>

<p>PM-48 va PM-49 da grafikni <b>oʻzimiz chizdik</b>. Endi teskari ish:
kimdir chizib qoʻygan grafikni <b>oʻqiymiz</b>. Bu — imtihonda ham, hayotda ham
eng koʻp kerak boʻladigan koʻnikma.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>notanish grafikni uch savol bilan ochasiz;</li>
    <li>koʻtarilgan, tekis va tushgan boʻlaklarni soʻz bilan tushuntirasiz;</li>
    <li>masofa–vaqt grafigidan tezlikni topasiz;</li>
    <li>eng tez oʻzgarish qayerda boʻlganini aniqlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch savol</span>
  <span class="pe-chip pe-chip--o">oʻqlarda nima?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">bitta katak qancha?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">chiziq nima qilyapti?</span>
</div>

<h3>1. Birinchi savol — oʻqlarda nima turibdi?</h3>

<p>Grafikka qarashdan oldin uning <b>yozuvlarini</b> oʻqing. Gorizontal oʻqda
odatda vaqt turadi: soat, kun, oy, yil. Vertikal oʻqda esa oʻlchanayotgan
miqdor: daraja, soʻm, kilometr, foiz.</p>

<p>Birlikni ham koʻring. «40» degan son 40 ming soʻmmi, 40 million soʻmmi yoki
40 foizmi — buni faqat oʻqdagi yozuv aytadi.</p>

<h3>2. Ikkinchi savol — bitta katak qancha?</h3>

<p>Bu — grafik oʻqishdagi eng koʻp yoʻqotiladigan ball. Katakning qiymatini
topish uchun ikkita qoʻshni sonni oling va oradagi kataklarni sanang.</p>

<div class="pe-ex">
  <p class="pe-ex__math">0 va 20 orasida 4 ta katak → 20 ÷ 4 = 5</p>
  <p class="pe-ex__uz">Bitta katak besh birlikka teng.</p>
  <p class="pe-ex__why">Kataklar teng, demak farqni ularning soniga boʻlamiz.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Har katak 1 birlik emas</p>
  <p>Koʻpchilik kataklarni sanab, «3 katak — 3 birlik» deb yozadi. Real
  grafiklarda bitta katak 2, 5, 10, 100 yoki 1000 birlik boʻlishi mumkin.
  <b>Shkalani aniqlamasdan bitta ham son aytmang.</b></p>
</div>

<h3>3. Uchinchi savol — chiziq nima qilyapti?</h3>

<p>Chiziqning har bir boʻlagi bitta jumla aytadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 165" role="img" aria-label="Grafikning uch xil boʻlagi: koʻtariladi, tekis turadi, tushadi">
    <line class="pm-ln" x1="30" y1="140" x2="305" y2="140"/>
    <line class="pm-ln" x1="40" y1="150" x2="40" y2="22"/>
    <polyline class="pm-ln pm-ln--hl" points="40,110 105,40 195,40 285,100" fill="none"/>
    <circle class="pm-pt" cx="105" cy="40" r="4"/>
    <circle class="pm-pt" cx="195" cy="40" r="4"/>
    <text class="pm-lbl pm-lbl--hl" x="52" y="132">oʻsadi</text>
    <text class="pm-lbl pm-lbl--hl" x="150" y="30" text-anchor="middle">oʻzgarmaydi</text>
    <text class="pm-lbl pm-lbl--hl" x="215" y="132">kamayadi</text>
    <text class="pm-lbl" x="292" y="158">vaqt</text>
    <text class="pm-lbl" x="48" y="20">miqdor</text>
  </svg>
  <figcaption>Koʻtarilish — oʻsish, gorizontal boʻlak — oʻzgarish yoʻq,
  pasayish — kamayish. Boʻlak qanchalik tik boʻlsa, oʻzgarish shunchalik
  tez.</figcaption>
</figure>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Tiklik = tezlik</p>
  <p>Ikki boʻlakni taqqoslaganda <b>qaysi biri tikroq boʻlsa, oʻsha yerda
  oʻzgarish tezroq</b> boʻlgan. Bu PM-49 dagi k ning oʻzi: k qanchalik katta
  boʻlsa, chiziq shunchalik tik.</p>
</div>

<h3>4. Masofa–vaqt grafigi — safarni oʻqish</h3>

<p>Eng koʻp uchraydigan grafik turi. Gorizontal oʻqda vaqt, vertikal oʻqda uydan
bosib oʻtilgan masofa.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 245" role="img" aria-label="Uch soatlik safarning masofa-vaqt grafigi">
    <line class="pm-ln pm-ln--dash" x1="50" y1="140" x2="290" y2="140"/>
    <line class="pm-ln pm-ln--dash" x1="50" y1="80" x2="290" y2="80"/>
    <line class="pm-ln pm-ln--dash" x1="130" y1="200" x2="130" y2="30"/>
    <line class="pm-ln pm-ln--dash" x1="170" y1="200" x2="170" y2="30"/>
    <line class="pm-ln" x1="40" y1="200" x2="305" y2="200"/>
    <line class="pm-ln" x1="50" y1="215" x2="50" y2="20"/>
    <polyline class="pm-ln pm-ln--hl" points="50,200 130,140 170,140 290,20" fill="none"/>
    <circle class="pm-pt" cx="130" cy="140" r="4"/>
    <circle class="pm-pt" cx="170" cy="140" r="4"/>
    <circle class="pm-pt" cx="290" cy="20" r="4"/>
    <text class="pm-lbl pm-lbl--hl" x="150" y="130" text-anchor="middle">toʻxtash</text>
    <text class="pm-lbl" x="44" y="144" text-anchor="end">60</text>
    <text class="pm-lbl" x="44" y="84" text-anchor="end">120</text>
    <text class="pm-lbl" x="44" y="24" text-anchor="end">180</text>
    <text class="pm-lbl" x="130" y="216" text-anchor="middle">1</text>
    <text class="pm-lbl" x="170" y="216" text-anchor="middle">1,5</text>
    <text class="pm-lbl" x="290" y="216" text-anchor="middle">3</text>
    <text class="pm-lbl" x="180" y="238" text-anchor="middle">soat</text>
    <text class="pm-lbl" x="58" y="18">km</text>
  </svg>
  <figcaption>Uch soatlik safar: bir soat yoʻl, yarim soat dam, keyin yana
  yoʻl.</figcaption>
</figure>

<p>Grafik uchta jumla aytyapti.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">0 dan 1 soatgacha: 0 → 60 km</span>
    <span class="pm-solve__why">Bir soatda 60 km — tezlik 60 km/soat (PM-35)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 dan 1,5 soatgacha: 60 km da qoldi</span>
    <span class="pm-solve__why">Masofa oʻzgarmadi — mashina toʻxtagan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1,5 dan 3 soatgacha: 60 → 180 km</span>
    <span class="pm-solve__why">1,5 soatda 120 km → 120 ÷ 1,5 = 80 km/soat</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Oʻrtacha tezlik: 180 ÷ 3 = 60 km/soat</span>
    <span class="pm-solve__why">Butun masofani butun vaqtga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>60 + 0 + 120 = 180 km ✓ Uchinchi boʻlak chizmada eng tik — va hisob ham
  shuni tasdiqladi: 80 km/soat, birinchi boʻlakdagi 60 dan tezroq.
  <b>Koʻz bilan koʻrgan narsa hisob bilan mos tushdi.</b></p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Gorizontal boʻlak — «toʻxtadi», «qaytdi» emas</p>
  <p>Masofa–vaqt grafigida tekis boʻlak «uydan uzoqlik oʻzgarmadi» degani, yaʼni
  mashina turibdi. Agar chiziq <b>pastga</b> tushsa — mana shunda u orqaga,
  uyga qarab qaytyapti.</p>
</div>

<h3>5. Oʻsish grafigi — qayerda eng tez oʻsdi?</h3>

<p>Doʻkonning olti oylik daromadi (mln soʻm):</p>

<div class="pe-table-wrap"><table>
  <tr><th>Oy</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr>
  <tr><th>Daromad</th><td>12</td><td>15</td><td>15</td><td>21</td><td>24</td><td>23</td></tr>
  <tr><th>Oʻzgarish</th><td>—</td><td>+3</td><td>0</td><td>+6</td><td>+3</td><td>−1</td></tr>
</table></div>

<p>Uchinchi qator hamma savolga javob beradi. Eng koʻp oʻsish — 3-oydan 4-oyga
(+6), demak grafikning eng tik boʻlagi ham oʻsha yerda. Ikkinchidan uchinchiga
oʻtganda daromad oʻzgarmadi — chiziq gorizontal. Oxirida esa birinchi marta
kamaydi.</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Eng baland ≠ eng tez oʻsgan</p>
  <p>Grafikning eng baland nuqtasi — 5-oy (24 mln). Eng tez oʻsgan joyi esa
  3–4-oylar orasi. Bu ikki savol butunlay boshqa: biri <b>qiymat</b> haqida,
  ikkinchisi <b>oʻzgarish</b> haqida. Savolni diqqat bilan oʻqing.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Sherbekning telefoni.</b> Sherbek batareya grafigiga qaradi. Soat
<b>8:00</b> da zaryad <b>100%</b> edi, soat <b>12:00</b> da <b>40%</b> ga
tushdi. 12:00 dan 13:00 gacha telefon quvvatda turdi va <b>90%</b> ga
koʻtarildi. Soat <b>14:00</b> da esa <b>70%</b> koʻrsatdi.</p>

<p><b>Savol:</b> ertalab va tushdan keyin qaysi biri tezroq kamaydi? Agar zaryad
tushdan keyingi tezlikda kamayishda davom etsa, soat 16:00 da necha foiz
qoladi?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ertalab: 100 − 40 = 60% , 4 soatda</span>
    <span class="pm-solve__why">8:00 dan 12:00 gacha — toʻrt soat</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 ÷ 4 = 15% har soatda</span>
    <span class="pm-solve__why">Ertalabki kamayish tezligi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Tushdan keyin: 90 − 70 = 20% , 1 soatda</span>
    <span class="pm-solve__why">13:00 dan 14:00 gacha — bir soat</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">20 &gt; 15 → tushdan keyin tezroq</span>
    <span class="pm-solve__why">Grafikning oʻsha boʻlagi tikroq</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">70 − 20 × 2 = 30%</span>
    <span class="pm-solve__why">14:00 dan 16:00 gacha yana ikki soat</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Soat 15:00 da 70 − 20 = 50%, 16:00 da 50 − 20 = 30% ✓ Grafikning
  koʻtarilgan yagona boʻlagi — 12:00 va 13:00 orasi, u yerda telefon quvvatda
  turgan. <b>Koʻtarilish har doim «qoʻshildi», pasayish «sarflandi» degani.</b></p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>90% dan soatiga 20% dan ketsa, taxminan 4–5 soatda tugaydi. 16:00 —
  quvvatdan uzilganiga uch soat, demak javob 100 dan ancha kichik, lekin hali
  nol emas. 30% — mos.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Masofa–vaqt grafigidagi gorizontal boʻlak: «uyga
    qaytdi»</p>
  <p class="pe-fix__good">Gorizontal boʻlak: «bir joyda turdi»</p>
  <p class="pe-fix__why">Masofa oʻzgarmadi, demak harakat ham yoʻq. Qaytish —
  chiziqning <b>pastga</b> tushishi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Har katak 5 birlik boʻlgan grafikda 3 katak = 3
    birlik</p>
  <p class="pe-fix__good">3 katak = 15 birlik</p>
  <p class="pe-fix__why">Shkala oʻqilmagan. Avval ikki qoʻshni sonni oling va
  oradagi kataklarni sanang: 20 ÷ 4 = 5.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Eng koʻp daromad qaysi oyda oʻsdi?» → 5-oy, chunki u
    eng baland</p>
  <p class="pe-fix__good">3–4-oylar orasi, chunki oʻsish +6 mln</p>
  <p class="pe-fix__why">Balandlik — qiymat, tiklik — oʻzgarish. Savol qaysi biri
  haqidaligini aniqlang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Grafikda 0 bilan 30 orasida 6 ta katak bor. Bitta
  katak necha birlik?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5 birlik.</b> 30 ÷ 6 = 5. Demak 4 katak koʻtarilgan chiziq
    20 birlikka oʻsgan boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Masofa–vaqt grafigida chiziq 2 soatda 90 km ga
  koʻtarildi. Tezlik qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>45 km/soat.</b> 90 ÷ 2 = 45. Masofani vaqtga boʻlamiz (PM-35).</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Ikki chiziqdan biri tikroq koʻtarilgan. Bu nimani
  bildiradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Tikroq chiziqda miqdor tezroq oʻsgan.</b> Tiklik — bir birlik vaqtdagi
    oʻzgarish, yaʼni PM-49 dagi k.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Harorat: 6:00 da 4°, 12:00 da 16°, 18:00 da 10°.
  Qaysi oraliqda oʻzgarish tezroq boʻlgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Ertalabki oraliqda.</b> 6:00–12:00: 12 daraja, 6 soatda — soatiga
    2 daraja. 12:00–18:00: 6 daraja, 6 soatda — soatiga 1 daraja. Demak
    birinchi boʻlak tikroq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bekzod velosipedda ketdi: birinchi 40 daqiqada 12 km,
  keyin 20 daqiqa doʻstini kutib turdi, soʻng 30 daqiqada yana 9 km. Grafikning
  qaysi boʻlagi gorizontal, jami masofa qancha va butun yoʻl uchun oʻrtacha
  tezlik qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Oʻrtadagi boʻlak gorizontal; jami 21 km; oʻrtacha tezlik
    14 km/soat.</b> Kutish paytida masofa oʻzgarmaydi — chiziq tekis.
    12 + 9 = 21 km. Jami vaqt: 40 + 20 + 30 = 90 daqiqa = 1,5 soat.
    21 ÷ 1,5 = 14 km/soat. Tekshirish: 14 × 1,5 = 21 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Shkala</b><span>bitta katakning qiymati; ingl. scale</span></li>
  <li><b>Oʻq yozuvi</b><span>oʻqda nima oʻlchanayotgani; ingl. axis label</span></li>
  <li><b>Masofa–vaqt grafigi</b><span>safarni koʻrsatuvchi grafik; ingl.
    distance-time graph</span></li>
  <li><b>Tiklik</b><span>chiziqning qiyaligi, oʻzgarish tezligi; ingl.
    steepness</span></li>
  <li><b>Oʻrtacha tezlik</b><span>butun masofa butun vaqtga boʻlingani; ingl.
    average speed</span></li>
  <li><b>Gorizontal boʻlak</b><span>miqdor oʻzgarmagan oraliq; ingl. flat
    section</span></li>
  <li><b>Oʻsish</b><span>chiziqning koʻtarilishi; ingl. increase</span></li>
  <li><b>Pasayish</b><span>chiziqning tushishi; ingl. decrease</span></li>
  <li><b>Eng yuqori nuqta</b><span>eng katta qiymat, eng tez oʻsish emas; ingl.
    maximum</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Avval oʻqlar va shkala, keyin sonlar.</b> Katakning qiymatini
      bilmasdan hech narsa aytmang.</li>
    <li><b>Tik — tez, tekis — oʻzgarishsiz, pastga — kamayish.</b></li>
    <li><b>Eng baland nuqta bilan eng tik boʻlak — ikki xil savol.</b></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-52 — ikki chiziqning kesishishi, sistema nima
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-52: Ikki chiziqning kesishishi — sistema nima",
        "category": "math",
        "order": 52,
        "summary": (
            "Ikki chiziq kesishgan nuqta — ikkala shartni ham bajaradigan yagona "
            "(x; y) juftligi. Tenglamalar sistemasi nima, yechimni tekshirish, "
            "grafik va tenglashtirish usullari, uchta mumkin boʻlgan hol."
        ),
        "stories": ["Qaysi tarif qachon foydali"],
        "content": """
<h2>PM-52: Ikki chiziqning kesishishi — sistema nima</h2>

<p>PM-50 da ikki tarifni taqqoslab, ular 300 daqiqada tenglashishini
<b>jadvaldan</b> koʻrgan edik. Va oʻshanda bir vaʼda berilgandi: kesishgan
nuqtani chizmasiz, hisoblab topishni oʻrganamiz.</p>

<p>Mana shu dars — oʻsha vaʼdaning bajarilishi. Yoʻl-yoʻlakay matematikaning
eng foydali qurollaridan biri — <b>sistema</b> bilan tanishamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>kesishgan nuqta nimani anglatishini aytasiz;</li>
    <li>tenglamalar sistemasini yozasiz va yechimi nima ekanini bilasiz;</li>
    <li>berilgan juftlik yechim yoki yoʻqligini tekshirasiz;</li>
    <li>ikkalasi ham y = … koʻrinishida boʻlsa, kesishgan nuqtani
      hisoblaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Sistema yechimi</span>
  <span class="pe-chip pe-chip--s">(x; y)</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">birinchi tenglamani ham</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">ikkinchisini ham bajaradi</span>
</div>

<h3>1. Kesishgan nuqta nima?</h3>

<p>Bitta chiziqning har bir nuqtasi oʻsha chiziqning tenglamasini bajaradi
(PM-48). Ikki chiziq kesishgan joyda esa bitta nuqta <b>ikkala chiziqda ham</b>
yotadi.</p>

<p>Demak uning koordinatalari ikkala tenglamani ham toʻgʻri qiladi. Butun
mavzuning mohiyati shu bitta jumlada.</p>

<div class="pe-ex">
  <p class="pe-ex__math">y = 2x + 1 va y = −x + 7 → (2; 5)</p>
  <p class="pe-ex__uz">Ikkinchi kirishda ikkala qoida ham beshni beradi.</p>
  <p class="pe-ex__why">2 × 2 + 1 = 5 ✓ va −2 + 7 = 5 ✓ — shuning uchun
  chiziqlar aynan shu nuqtada uchrashadi.</p>
</div>

<h3>2. Sistema — birga oʻqiladigan ikki tenglama</h3>

<p>Ikkita tenglama <b>bir vaqtning oʻzida</b> bajarilishi kerak boʻlsa, ular
<b>tenglamalar sistemasi</b> deyiladi. Uni shunday yozamiz:</p>

<div class="pe-formula">
  <span class="pe-formula__label">Sistema</span>
  <span class="pe-chip pe-chip--v">y = 2x + 1</span>
  <span class="pe-op">va</span>
  <span class="pe-chip pe-chip--o">y = −x + 7</span>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Yechim — juftlik, bitta son emas</p>
  <p>Ikki nomaʼlumli sistemaning yechimi — <b>(x; y) juftligi</b>. «x = 2»
  degan javob yarim javob: y ni ham aytmasangiz, masala tugamagan.</p>
</div>

<h3>3. Yechimni tekshirish</h3>

<p>Bu eng oson va eng kerakli koʻnikma. Juftlikni <b>ikkala</b> tenglamaga
qoʻyib koʻrasiz — ikkalasi ham toʻgʻri chiqsa, u yechim.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(3; 4) juftligi tekshirilsin</span>
    <span class="pm-solve__why">Sistema: x + y = 7 va 2x − y = 2</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 + 4 = 7 ✓</span>
    <span class="pm-solve__why">Birinchisi bajarildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 × 3 − 4 = 6 − 4 = 2 ✓</span>
    <span class="pm-solve__why">Ikkinchisi ham bajarildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(3; 4) — sistemaning yechimi</span>
    <span class="pm-solve__why">Ikkala shart ham toʻgʻri</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Bitta tenglama yetarli emas</p>
  <p>(5; 2) juftligini oling: 5 + 2 = 7 ✓ — birinchi tenglama bajarildi. Lekin
  2 × 5 − 2 = 8 ≠ 2 ✗. Demak (5; 2) yechim emas. <b>Faqat birinchisini
  tekshirib toʻxtash — eng koʻp uchraydigan xato.</b></p>
</div>

<h3>4. Grafik usul</h3>

<p>Ikkala chiziqni bitta koordinata tekisligiga chizasiz va kesishgan nuqtaning
koordinatalarini oʻqiysiz. Usul koʻrgazmali, lekin bitta kamchiligi bor:
kesishuv kasr sonlarda boʻlsa, chizmadan aniq oʻqib boʻlmaydi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Grafik usul</p>
    <p>Koʻrinadi, tushunarli, vaziyatni tushuntiradi. Butun sonlarda aniq.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Hisob usuli</p>
    <p>Chizma kerak emas, javob har doim aniq — kasr boʻlsa ham.</p>
  </div>
</div>

<h3>5. Tenglashtirish — hisoblab topish</h3>

<p>Ikkala tenglama ham <b>y = …</b> koʻrinishida boʻlsa, ish juda soddalashadi.
Kesishgan nuqtada ikkala y bir xil. Demak ularning oʻng tomonlarini
tenglashtirsak boʻladi — va ikki tomonida ham x turgan oddiy tenglama chiqadi
(PM-37).</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 2x + 1 , y = −x + 7</span>
    <span class="pm-solve__why">Berilgan sistema</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 1 = −x + 7</span>
    <span class="pm-solve__why">Kesishuvda ikkala y teng</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 1 = 7</span>
    <span class="pm-solve__why">Ikki tomonga x qoʻshdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x = 6 → x = 2</span>
    <span class="pm-solve__why">Birni ayirdik, uchga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">y = 2 × 2 + 1 = 5 → (2; 5)</span>
    <span class="pm-solve__why">x ni istalgan tenglamaga qaytardik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Ikkinchi tenglamada ham: −2 + 7 = 5 ✓ Ikkalasi bir xil y berdi, demak
  nuqta rostdan ham ikkala chiziqda yotadi. <b>y ni ikkinchi tenglamadan
  chiqarib tekshirish — bepul va deyarli har doim xatoni tutadi.</b></p>
</div>

<h3>6. Uchta mumkin boʻlgan hol</h3>

<div class="pe-table-wrap"><table>
  <tr><th>Chiziqlar</th><th>Misol</th><th>Yechim</th></tr>
  <tr><td>Kesishadi (k lari har xil)</td><td>y = 2x + 1 va y = −x + 7</td>
      <td>Bitta yechim: (2; 5)</td></tr>
  <tr><td>Parallel (k bir xil, b har xil)</td><td>y = 2x + 1 va y = 2x + 4</td>
      <td>Yechim yoʻq</td></tr>
  <tr><td>Ustma-ust tushgan</td><td>y = 2x + 1 va 2y = 4x + 2</td>
      <td>Cheksiz koʻp yechim</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Nega parallelda yechim yoʻq</p>
  <p>Parallel chiziqlarning tikligi bir xil (PM-50), demak ular hech qachon
  uchrashmaydi. Tenglashtirsak ham koʻramiz: 2x + 1 = 2x + 4 → 1 = 4, bu esa
  yolgʻon. <b>Yolgʻon tenglik chiqishi — «yechim yoʻq» degan javob.</b></p>
</div>

<h3>Matnli masala</h3>

<p><b>Ikki taksi xizmati.</b> «Tez taksi» oʻtirish uchun <b>8 000 soʻm</b> oladi
va har kilometr uchun <b>3 000 soʻm</b> qoʻshadi. «Yoʻlbars» oʻtirish uchun
<b>20 000 soʻm</b> oladi, lekin kilometri atigi <b>1 500 soʻm</b>.</p>

<p><b>Savol:</b> necha kilometrda ikkala xizmat bir xil pul turadi? 4 km va
12 km yoʻlga qaysi biri arzon?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Tez taksi: y = 3 000x + 8 000</span>
    <span class="pm-solve__why">b — oʻtirish haqi, k — kilometr narxi (PM-50)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Yoʻlbars: y = 1 500x + 20 000</span>
    <span class="pm-solve__why">Katta b, kichik k</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 000x + 8 000 = 1 500x + 20 000</span>
    <span class="pm-solve__why">«Bir xil pul» — ikkala y teng</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 500x = 12 000</span>
    <span class="pm-solve__why">1 500x va 8 000 ni tegishli tomonga oʻtkazdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 8 km, y = 32 000 soʻm</span>
    <span class="pm-solve__why">3 000 × 8 + 8 000 = 32 000</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Ikkinchi formulada ham: 1 500 × 8 + 20 000 = 12 000 + 20 000 = 32 000 ✓
  Endi ikki tomonini sinaymiz. <b>4 km:</b> Tez taksi 12 000 + 8 000 = 20 000,
  Yoʻlbars 6 000 + 20 000 = 26 000 — qisqa yoʻlga Tez taksi arzon.
  <b>12 km:</b> Tez taksi 36 000 + 8 000 = 44 000, Yoʻlbars 18 000 + 20 000 =
  38 000 — uzoq yoʻlga Yoʻlbars arzon.</p>
</div>

<figure class="pm-fig">
  <svg viewBox="0 0 330 245" role="img" aria-label="Ikki taksi tarifining grafigi va kesishgan nuqtasi">
    <line class="pm-ln pm-ln--dash" x1="210" y1="200" x2="210" y2="80"/>
    <line class="pm-ln pm-ln--dash" x1="50" y1="80" x2="210" y2="80"/>
    <line class="pm-ln" x1="40" y1="200" x2="315" y2="200"/>
    <line class="pm-ln" x1="50" y1="215" x2="50" y2="20"/>
    <line class="pm-ln pm-ln--hl" x1="50" y1="170" x2="290" y2="35"/>
    <line class="pm-ln" x1="50" y1="125" x2="290" y2="57.5"/>
    <circle class="pm-pt" cx="210" cy="80" r="5"/>
    <text class="pm-lbl pm-lbl--hl" x="248" y="40" text-anchor="end">Tez taksi</text>
    <text class="pm-lbl" x="288" y="92" text-anchor="end">Yoʻlbars</text>
    <text class="pm-lbl pm-lbl--hl" x="216" y="102">(8; 32 000)</text>
    <text class="pm-lbl" x="44" y="174" text-anchor="end">8</text>
    <text class="pm-lbl" x="44" y="129" text-anchor="end">20</text>
    <text class="pm-lbl" x="44" y="84" text-anchor="end">32</text>
    <text class="pm-lbl" x="44" y="39" text-anchor="end">44</text>
    <text class="pm-lbl" x="130" y="216" text-anchor="middle">4</text>
    <text class="pm-lbl" x="210" y="216" text-anchor="middle">8</text>
    <text class="pm-lbl" x="290" y="216" text-anchor="middle">12</text>
    <text class="pm-lbl" x="180" y="238" text-anchor="middle">kilometr</text>
    <text class="pm-lbl" x="58" y="18">ming soʻm</text>
  </svg>
  <figcaption>Sakkizinchi kilometrgacha Tez taksi pastda, undan keyin Yoʻlbars.
  Kesishgan nuqta — narxlar tenglashgan joy.</figcaption>
</figure>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Yoʻlbars boshida 12 000 soʻmga qimmat, lekin har kilometrda 1 500 soʻm
  yutadi. 12 000 ÷ 1 500 = 8 — sakkizinchi kilometrda farq yopiladi. Bu boshqa
  yoʻl bilan chiqqan oʻsha javob.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Javob: x = 8</p>
  <p class="pe-fix__good">Javob: (8; 32 000)</p>
  <p class="pe-fix__why">Sistemaning yechimi — juftlik. x ni topib toʻxtash
  masalani yarmida qoldirish demakdir.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">(5; 2) yechim, chunki 5 + 2 = 7 ✓</p>
  <p class="pe-fix__good">Yechim emas: 2 × 5 − 2 = 8 ≠ 2</p>
  <p class="pe-fix__why">Juftlik <b>ikkala</b> tenglamani ham bajarishi shart.
  Bittasi toʻgʻri chiqishi hech narsani isbotlamaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">y = 2x + 1 va y = 2x + 4 → 1 = 4, demak x = 0</p>
  <p class="pe-fix__good">1 = 4 yolgʻon → yechim yoʻq, chiziqlar parallel</p>
  <p class="pe-fix__why">Nomaʼlum qisqarib ketib, yolgʻon tenglik qolsa, javob
  «yechim yoʻq» boʻladi — nol emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. (1; 4) juftligi y = 3x + 1 va y = 5x − 1 sistemasining
  yechimimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Ha.</b> 3 × 1 + 1 = 4 ✓ va 5 × 1 − 1 = 4 ✓ Ikkala tenglama ham
    bajarildi, demak chiziqlar (1; 4) da kesishadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. y = x + 3 va y = 2x + 1 chiziqlari qayerda
  kesishadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(2; 5).</b> x + 3 = 2x + 1 → 3 − 1 = 2x − x → x = 2. Keyin
    y = 2 + 3 = 5. Tekshirish: 2 × 2 + 1 = 5 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. y = 4x − 2 va y = 4x + 6 chiziqlari nechta nuqtada
  kesishadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Bitta ham emas.</b> k lari bir xil (4), b lari har xil — parallel
    chiziqlar. Tenglashtirsak: −2 = 6, yolgʻon. Yechim yoʻq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. y = 5x va y = 2x + 9 sistemasini yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(3; 15).</b> 5x = 2x + 9 → 3x = 9 → x = 3. y = 5 × 3 = 15.
    Tekshirish: 2 × 3 + 9 = 15 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Ikki sport zali. «Olimp»: obuna 100 000 soʻm, har
  mashgʻulot 5 000 soʻm. «Bahodir»: obuna yoʻq, har mashgʻulot 9 000 soʻm.
  Necha mashgʻulotda narxlar tenglashadi va 30 marta boradigan Dilnozaga qaysi
  biri arzon?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>25 mashgʻulotda tenglashadi; Dilnozaga «Olimp» arzon.</b>
    Olimp: y = 5 000x + 100 000. Bahodir: y = 9 000x. Tenglashtiramiz:
    9 000x = 5 000x + 100 000 → 4 000x = 100 000 → x = 25. Ikkalasi ham
    225 000 soʻm ✓ 30 martada: Olimp 150 000 + 100 000 = 250 000, Bahodir
    270 000 — Olimp 20 000 soʻmga arzon.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Tenglamalar sistemasi</b><span>birga bajarilishi kerak boʻlgan ikki
    tenglama; ingl. system of equations</span></li>
  <li><b>Sistema yechimi</b><span>ikkalasini ham bajaradigan (x; y) juftligi;
    ingl. solution</span></li>
  <li><b>Kesishish nuqtasi</b><span>ikki chiziq uchrashgan joy; ingl. point of
    intersection</span></li>
  <li><b>Ikki nomaʼlum</b><span>x va y bir masalada; ingl. two unknowns</span></li>
  <li><b>Tenglashtirish usuli</b><span>ikkala y ni teng deb yozish; ingl.
    equating method</span></li>
  <li><b>Grafik usul</b><span>chizib, kesishuvni oʻqish; ingl. graphical
    method</span></li>
  <li><b>Yechim yoʻq</b><span>parallel chiziqlar holati; ingl. no
    solution</span></li>
  <li><b>Cheksiz koʻp yechim</b><span>ikki chiziq ustma-ust tushgani; ingl.
    infinitely many</span></li>
  <li><b>Tekshirish</b><span>juftlikni ikkala tenglamaga qoʻyish; ingl.
    verification</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Kesishgan nuqta ikkala tenglamani ham bajaradi.</b> Butun mavzu shu
      jumladan oʻsib chiqadi.</li>
    <li><b>Yechim — juftlik (x; y),</b> bitta son emas.</li>
    <li><b>Ikkalasi y = … boʻlsa, oʻng tomonlarni tenglashtiring</b> — qolgani
      oddiy tenglama.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-53 — oʻrniga qoʻyish usuli
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-53: Sistemani oʻrniga qoʻyish usuli bilan yechish",
        "category": "math",
        "order": 53,
        "summary": (
            "Bitta tenglamadan bitta nomaʼlumni ifodalab, ikkinchisiga qoʻyish: "
            "shunda ikki nomaʼlumli sistema bitta nomaʼlumli oddiy tenglamaga "
            "aylanadi. Toʻrt qadam va tekshirish."
        ),
        "stories": ["Choy va non — kafedagi hisob"],
        "content": """
<h2>PM-53: Sistemani oʻrniga qoʻyish usuli bilan yechish</h2>

<p>PM-52 da sistemani tenglashtirish bilan yechdik — lekin faqat ikkala tenglama
ham <b>y = …</b> koʻrinishida boʻlgani uchun. Hayotda esa sistema koʻpincha
boshqacha keladi: <i>«ikkalasi 20 ta, jami 380 000 soʻm»</i>.</p>

<p>Bunday sistemani yechishning eng ishonchli yoʻli — <b>oʻrniga qoʻyish
usuli</b>. Uning gʻoyasi juda sodda: ikkita nomaʼlumdan birini yoʻqotamiz, keyin
qolgani bilan oddiy tenglamadek ishlaymiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>bitta tenglamadan bitta nomaʼlumni ifodalaysiz;</li>
    <li>uni ikkinchi tenglamaga qoʻyib, nomaʼlumni yoʻqotasiz;</li>
    <li>qaysi nomaʼlumni ifodalash osonroq ekanini tanlaysiz;</li>
    <li>javobni ikkala tenglamada tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrt qadam</span>
  <span class="pe-chip pe-chip--s">ifodala</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">qoʻy</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">yech</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">qaytar</span>
</div>

<h3>1. Gʻoya: bitta nomaʼlumni yoʻqotish</h3>

<p>Ikki nomaʼlumli tenglamani yolgʻiz oʻzini yechib boʻlmaydi: x + y = 10 ning
javoblari juda koʻp — (1; 9), (2; 8), (4; 6)… Ikkinchi tenglama esa ulardan
faqat bittasini tanlaydi.</p>

<p>Shuning uchun birinchi tenglamadan y ni x orqali <b>ifodalaymiz</b> va shu
ifodani ikkinchi tenglamada y ning oʻrniga qoʻyamiz. Natijada faqat x qoladi —
va bu allaqachon PM-36 dagi oddiy tenglama.</p>

<h3>2. Birinchi misol — eng oson holat</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + y = 10 , 2x + y = 16</span>
    <span class="pm-solve__why">Berilgan sistema</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 10 − x</span>
    <span class="pm-solve__why">Birinchisidan y ni ifodaladik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + (10 − x) = 16</span>
    <span class="pm-solve__why">Ikkinchisiga y ning oʻrniga qoʻydik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + 10 = 16 → x = 6</span>
    <span class="pm-solve__why">Oʻxshash hadlarni yigʻdik (PM-32)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">y = 10 − 6 = 4 → (6; 4)</span>
    <span class="pm-solve__why">x ni ifodaga qaytardik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>6 + 4 = 10 ✓ va 2 × 6 + 4 = 12 + 4 = 16 ✓ Ikkala tenglama ham bajarildi,
  demak (6; 4) — sistemaning yechimi.</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Qaysi nomaʼlumni ifodalash kerak?</p>
  <p><b>Koeffitsienti 1 boʻlganini.</b> x + y = 10 dagi y ni ifodalash bir
  qadam: y = 10 − x. 3x + 7y = 20 dan x ni ifodalash esa kasr chiqaradi. Osonini
  tanlash — vaqt ham, xato ham tejaydi.</p>
</div>

<h3>3. Ikkinchi misol — bittasi allaqachon ifodalangan</h3>

<p>Baʼzan ishning yarmi qilib qoʻyilgan boʻladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 3x − 2 , 2x + y = 13</span>
    <span class="pm-solve__why">Birinchisi tayyor ifoda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + (3x − 2) = 13</span>
    <span class="pm-solve__why">y ning oʻrniga 3x − 2 qoʻydik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5x − 2 = 13 → 5x = 15</span>
    <span class="pm-solve__why">2x va 3x oʻxshash hadlar</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 3 , y = 3 × 3 − 2 = 7 → (3; 7)</span>
    <span class="pm-solve__why">Tekshirish: 2 × 3 + 7 = 13 ✓</span>
  </div>
</div>

<h3>4. Uchinchi misol — koeffitsientli holat</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2x + 3y = 27 , x − y = 1</span>
    <span class="pm-solve__why">Berilgan sistema</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = y + 1</span>
    <span class="pm-solve__why">Ikkinchisidan x ni ifodaladik (koeffitsienti 1)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2(y + 1) + 3y = 27</span>
    <span class="pm-solve__why">Birinchisiga qoʻydik — qavs bilan!</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2y + 2 + 3y = 27</span>
    <span class="pm-solve__why">Qavsni ochdik (PM-33)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5y = 25 → y = 5</span>
    <span class="pm-solve__why">Ikkidan ayirdik, beshga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 5 + 1 = 6 → (6; 5)</span>
    <span class="pm-solve__why">Tekshirish: 12 + 15 = 27 ✓ va 6 − 5 = 1 ✓</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Qavsni unutmang</p>
  <p>Ifodani qoʻyayotganda uni <b>doim qavsga oling</b>. 15 000(20 − x) ni
  qavssiz yozsangiz, minus faqat birinchi hadga tegadi va butun yechim
  buziladi: toʻgʻrisi 300 000 <b>−</b> 15 000x, notoʻgʻrisi 300 000 + 15 000x.
  Bu — manfiy ishorali eng koʻp uchraydigan xato (PM-33).</p>
</div>

<h3>Matnli masala</h3>

<p><b>Sinf kinoga bordi.</b> Kattalar chiptasi <b>25 000 soʻm</b>, bolalar
chiptasi <b>15 000 soʻm</b>. Kassaga jami <b>20 ta</b> chipta uchun
<b>380 000 soʻm</b> toʻlandi.</p>

<p><b>Savol:</b> nechta katta va nechta bolalar chiptasi olingan?</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Kattalar</span>
    <span class="pm-model__bar" style="width:40%">x ta</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Bolalar</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:60%">y ta</span>
  </div>
  <p class="pm-model__tot">Jami: x + y = 20 ta chipta, 380 000 soʻm</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x — kattalar, y — bolalar chiptasi soni</span>
    <span class="pm-solve__why">Nomaʼlumlarni nomladik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + y = 20</span>
    <span class="pm-solve__why">Chiptalar soni</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">25 000x + 15 000y = 380 000</span>
    <span class="pm-solve__why">Toʻlangan pul</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">y = 20 − x</span>
    <span class="pm-solve__why">Birinchisidan ifodaladik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">25 000x + 15 000(20 − x) = 380 000</span>
    <span class="pm-solve__why">Qoʻydik — qavs bilan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">25 000x + 300 000 − 15 000x = 380 000</span>
    <span class="pm-solve__why">Qavsni ochdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">10 000x = 80 000 → x = 8</span>
    <span class="pm-solve__why">300 000 ni oʻng tomonga oʻtkazdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">y = 20 − 8 = 12</span>
    <span class="pm-solve__why">8 ta katta, 12 ta bolalar chiptasi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>8 + 12 = 20 ✓ Pul: 25 000 × 8 = 200 000 va 15 000 × 12 = 180 000,
  jami 200 000 + 180 000 = 380 000 ✓ <b>Ikkala shart ham bajarildi.</b></p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Hamma chipta bolalarniki boʻlganda 20 × 15 000 = 300 000 soʻm boʻlardi.
  Haqiqatda 80 000 soʻm koʻp toʻlangan. Har bir katta chipta 10 000 soʻm
  qoʻshadi, demak 80 000 ÷ 10 000 = 8 ta katta chipta. Ikkinchi yoʻl bilan
  oʻsha javob chiqdi.</span>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Sonlarni kichraytirib olish mumkin</p>
  <p>25 000x + 15 000y = 380 000 tenglamasining ikkala tomonini 5 000 ga
  boʻlsangiz, 5x + 3y = 76 chiqadi — ish ancha yengillashadi. Tekshiring:
  5 × 8 + 3 × 12 = 40 + 36 = 76 ✓</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">x = 8 topildi — javob: 8</p>
  <p class="pe-fix__good">Javob: (8; 12) — 8 ta katta, 12 ta bolalar
    chiptasi</p>
  <p class="pe-fix__why">Topilgan qiymatni ifodaga qaytarish — usulning toʻrtinchi
  qadami. Usiz masala yarim qolgan.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">25 000x + 15 000 × 20 − x = 380 000</p>
  <p class="pe-fix__good">25 000x + 15 000(20 − x) = 380 000</p>
  <p class="pe-fix__why">Ifoda qavssiz qoʻyilgan: koʻpaytuvchi butun qavsga
  tegishli. Qavssiz yozuv butunlay boshqa tenglama.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">y = 10 − x ni <b>oʻsha</b> birinchi tenglamaga
    qaytarish</p>
  <p class="pe-fix__good">Ifodani <b>ikkinchi</b> tenglamaga qoʻyish</p>
  <p class="pe-fix__why">Oʻz tenglamasiga qoʻysangiz 10 = 10 chiqadi — toʻgʻri,
  lekin foydasiz. Yangi maʼlumot faqat ikkinchi tenglamada bor.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. y = x + 2 va x + y = 10 sistemasini yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(4; 6).</b> x + (x + 2) = 10 → 2x + 2 = 10 → 2x = 8 → x = 4,
    y = 4 + 2 = 6. Tekshirish: 4 + 6 = 10 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. x = 2y va x + y = 12 sistemasini yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(8; 4).</b> 2y + y = 12 → 3y = 12 → y = 4, x = 2 × 4 = 8.
    Tekshirish: 8 + 4 = 12 ✓ va 8 = 2 × 4 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. x + y = 7 va 3x + y = 17 sistemasini yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(5; 2).</b> y = 7 − x → 3x + (7 − x) = 17 → 2x + 7 = 17 → 2x = 10 →
    x = 5, y = 2. Tekshirish: 3 × 5 + 2 = 17 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 4x + y = 9 va 3x − 2y = 4 sistemasida qaysi
  nomaʼlumni ifodalash oson va yechim nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Birinchi tenglamadan y ni; yechim (2; 1).</b> y ning koeffitsienti 1,
    demak y = 9 − 4x. Qoʻyamiz: 3x − 2(9 − 4x) = 4 → 3x − 18 + 8x = 4 →
    11x = 22 → x = 2, y = 9 − 8 = 1. Tekshirish: 6 − 2 = 4 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Afsona 5 ta daftar va 3 ta ruchka uchun 73 000 soʻm
  toʻladi. Bitta daftar ruchkadan 5 000 soʻm qimmat. Daftar va ruchkaning
  narxini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Daftar 11 000 soʻm, ruchka 6 000 soʻm.</b> d — daftar, r — ruchka
    narxi. Shartlar: d = r + 5 000 va 5d + 3r = 73 000. Qoʻyamiz:
    5(r + 5 000) + 3r = 73 000 → 5r + 25 000 + 3r = 73 000 → 8r = 48 000 →
    r = 6 000, d = 11 000. Tekshirish: 5 × 11 000 = 55 000, 3 × 6 000 = 18 000,
    jami 73 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Oʻrniga qoʻyish usuli</b><span>nomaʼlumni ifoda bilan almashtirish;
    ingl. substitution method</span></li>
  <li><b>Nomaʼlumni ifodalash</b><span>y ni x orqali yozish; ingl. express in
    terms of</span></li>
  <li><b>Nomaʼlumni yoʻqotish</b><span>ikkitasidan bittasini qoldirish; ingl.
    eliminate</span></li>
  <li><b>Koeffitsient</b><span>nomaʼlum oldidagi son; ingl. coefficient</span></li>
  <li><b>Sistema yechimi</b><span>(x; y) juftligi; ingl. solution of a
    system</span></li>
  <li><b>Qavs ochish</b><span>koʻpaytuvchini har bir hadga tarqatish; ingl.
    expanding brackets</span></li>
  <li><b>Qaytarib qoʻyish</b><span>topilgan qiymatdan ikkinchisini topish; ingl.
    back-substitution</span></li>
  <li><b>Tekshirish</b><span>javobni ikkala tenglamaga qoʻyish; ingl.
    checking</span></li>
  <li><b>Sodalashtirish</b><span>ikkala tomonni bir songa boʻlish; ingl.
    simplifying</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Ifodala → qoʻy → yech → qaytar.</b> Toʻrt qadam, har doim shu
      tartibda.</li>
    <li><b>Koeffitsienti 1 boʻlgan nomaʼlumni ifodalang</b> — kasr chiqmaydi.</li>
    <li><b>Ifodani qavsga oling</b> va javobni <b>ikkala</b> tenglamada
      tekshiring.</li>
  </ul>
</div>
""",
    },
]
