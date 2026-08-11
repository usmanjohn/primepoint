# -*- coding: utf-8 -*-
"""Prime Math — Block A, darslar 10–12 (manfiy sonlar bilan amallar, daraja).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_10_12.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_10_12.py

⚠️ Kumulyativ:
  • "modul" atamasi hali oʻrgatilmagan (Blok C) — oʻrniga "nol dan uzoqligi" deyiladi;
  • kvadrat ildiz PM-13 da, kasr PM-15 da — bu darslarda ishlatilmaydi;
  • PM-10 va PM-11 da daraja yozuvi (x<sup>2</sup>) YOʻQ, u PM-12 da kiritiladi;
  • PM-12 manfiy asosni ishlatadi — bu PM-11 ga tayanadi, tartib toʻgʻri.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_10_12.py --author=prime
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
    # PM-10 — manfiy sonlarni qoʻshish va ayirish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-10: Manfiy sonlarni qoʻshish va ayirish",
        "category": "math",
        "order": 10,
        "summary": (
            "Havo −7 °C edi, 5 daraja isidi — necha boʻldi? Son oʻqida yurish, bir xil "
            "va har xil ishorali sonlarni qoʻshish, ayirishni qoʻshishga aylantirish."
        ),
        "stories": ["Lift, qavatlar va yertoʻla"],
        "content": """
<h2>PM-10: Manfiy sonlarni qoʻshish va ayirish</h2>

<p>Yanvar. Ertalab termometr <b>−7 °C</b> koʻrsatdi. Tushga borib havo <b>5 daraja
isidi</b>. Dilnoza deraza oldida turib oʻyladi: «Isidi — demak, harorat koʻtarildi.
Lekin −7 dan 5 daraja yuqorisi qayer boʻladi? Nol emas, −2 emasmi?» Aynan shu savol
bugungi darsning oʻzi. PM-9 da biz manfiy sonning <i>maʼnosini</i> oʻrgandik. Endi
ular bilan <b>ishlashni</b> oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>son oʻqida yurib har qanday qoʻshishni koʻz bilan koʻrasiz;</li>
    <li>bir xil va har xil ishorali sonlarni qoʻshasiz;</li>
    <li>ayirishni qoʻshishga aylantirasiz: <b>a − b = a + (−b)</b>;</li>
    <li>yonma-yon turgan ikki minus nega plus berishini tushunasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Son oʻqida</span>
  <span class="pe-chip pe-chip--v">+ qoʻshsak → oʻngga</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">− ayirsak → chapga</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">javob — qayerga kelib toʻxtaganingiz</span>
</div>

<h3>1. Son oʻqida yurish</h3>

<p>Manfiy sonlarni qoʻshishni yodlash shart emas — uni <b>yurish</b> deb tasavvur qiling.
Son oʻqida turasiz. Musbat son qoʻshilsa oʻngga qadam tashlaysiz, manfiy son qoʻshilsa
yoki ayirilsa chapga qadam tashlaysiz. Javob — oyogʻingiz ostidagi son.</p>

<p>Dilnozaning savoliga qaytamiz: <b>−7 + 5</b>. Demak, −7 nuqtasida turibmiz va oʻngga
5 qadam yuramiz.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__band" style="left:15%;width:25%"></span>
    <span class="pm-num__tick" style="left:0%"><i>−10</i></span>
    <span class="pm-num__tick" style="left:25%"><i>−5</i></span>
    <span class="pm-num__tick" style="left:50%"><i>0</i></span>
    <span class="pm-num__tick" style="left:75%"><i>5</i></span>
    <span class="pm-num__tick" style="left:100%"><i>10</i></span>
    <span class="pm-num__dot" style="left:15%"><i>−7</i></span>
    <span class="pm-num__dot" style="left:40%"><i>−2</i></span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">−7 + 5 = −2</p>
  <p class="pe-ex__uz">Nolgacha yetishga 7 qadam kerak edi, bizda esa atigi 5 ta qadam
  bor. Shuning uchun nolgacha yetib bormadik — manfiy tomonda qoldik.</p>
</div>

<p>Endi teskarisi: <b>−7 + 9</b>. Nolgacha 7 qadam ketdi, qoʻlimizda yana 2 qadam qoldi
— ular bizni nolning oʻng tomoniga olib oʻtadi. Javob: <b>2</b>. Koʻryapsizmi, hech
qanday qoida yodlanmadi, shunchaki yurdik.</p>

<h3>2. Bir xil ishorali sonlar</h3>

<p>Agar ikkala son ham manfiy boʻlsa, ikkala qadam ham chapga tashlanadi. Ular
<b>qoʻshiladi</b>, javob esa albatta manfiy chiqadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">−3 + (−4)</span>
    <span class="pm-solve__why">−3 dan boshlaymiz, yana 4 qadam chapga</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 + 4 = 7 qadam chapga</span>
    <span class="pm-solve__why">Ikkala harakat ham bir tomonga — qoʻshiladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">−3 + (−4) = −7</span>
    <span class="pm-solve__why">Chap tomonga ketdik, demak javob manfiy</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Hayotiy maʼno</p>
  <p>Qarzga qarz qoʻshilsa qarz kamaymaydi — koʻpayadi. 3 000 soʻm qarz ustiga yana
  4 000 soʻm qarz olsangiz, jami 7 000 soʻm qarzdorsiz: −3 000 + (−4 000) = −7 000.</p>
</div>

<h3>3. Har xil ishorali sonlar</h3>

<p>Bu yerda ikki qadam bir-biriga qarshi yoʻnaladi va biri ikkinchisini <b>yeb
qoʻyadi</b>. Ular «kurashadi»: kim kuchli boʻlsa, javobning ishorasi ham oʻshaniki.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Qoida</p>
  <p>Ishoralari har xil boʻlsa: sonlarning <b>nol dan uzoqligini</b> solishtiring.
  Kattasidan kichigini <b>ayiring</b>, javobga esa <b>nol dan uzoqrogʻining</b>
  ishorasini qoʻying.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">−12 + 5 = −7</p>
  <p class="pe-ex__uz">12 nol dan uzoqroq, 5 esa yaqin. 12 − 5 = 7, ishora manfiydan
  keldi — javob −7.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">12 + (−5) = 7</p>
  <p class="pe-ex__uz">Yana oʻsha 12 − 5 = 7, lekin bu safar uzoqrogʻi musbat 12 —
  demak javob musbat.</p>
</div>

<p>Ikki misolda bir xil hisob (12 − 5 = 7) ikki xil ishora berdi. Shuning uchun
hisoblashdan oldin <b>qaysi son kuchliroq</b> ekanini aniqlab olish kerak.</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Tez tekshiruv</p>
  <p>Javobning ishorasini hisobdan <i>oldin</i> ayting. −12 + 5 da manfiy tomon
  kuchliroq, demak javob manfiy — hali hech narsa hisoblamasdan buni bilamiz.</p>
</div>

<h3>4. Ayirish — qarama-qarshi sonni qoʻshish</h3>

<p>Endi darsning eng muhim jumlasi. <b>Ayirish alohida amal emas.</b> Har qanday
ayirishni qoʻshishga aylantirish mumkin:</p>

<div class="pe-formula">
  <span class="pe-formula__label">Asosiy qoida</span>
  <span class="pe-chip pe-chip--s">a − b</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">a + (−b)</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">«ayirish» = qarama-qarshisini qoʻshish</span>
</div>

<p>PM-9 da qarama-qarshi sonlarni koʻrgan edik: 6 ning qarama-qarshisi −6, −6 niki esa 6.
Endi ular ish beradi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 − 11</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 + (−11)</span>
    <span class="pm-solve__why">Ayirishni qoʻshishga aylantirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= −7</span>
    <span class="pm-solve__why">11 nol dan uzoqroq va manfiy: 11 − 4 = 7, ishora manfiy</span>
  </div>
</div>

<p>Endi qiyinrogʻi — <b>manfiy sonni ayirish</b>. 4 − (−3) nimaga teng? Qoidaga koʻra,
−3 ning qarama-qarshisini qoʻshamiz, u esa +3:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 − (−3)</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 + 3</span>
    <span class="pm-solve__why">−3 ning qarama-qarshisi +3</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 7</span>
    <span class="pm-solve__why">Ikkala son ham musbat — oddiy qoʻshish</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Nega ikki minus plus beradi?</p>
  <p>Ayirish — «olib tashlash». Qarzni olib tashlash esa foyda. Sizda 4 000 soʻm bor va
  doʻkondagi 3 000 soʻmlik <b>qarzingiz kechirildi</b> — qarz olib tashlandi, ahvolingiz
  4 000 emas, 7 000 soʻmga teng boʻlib qoldi: 4 000 − (−3 000) = 7 000.</p>
</div>

<div class="pe-table-wrap"><table>
  <tr><th>Yozuv</th><th>Nima qilamiz</th><th>Javob</th></tr>
  <tr><td>−5 + 2</td><td>Chapdan oʻngga 2 qadam</td><td>−3</td></tr>
  <tr><td>−5 + (−2)</td><td>Yana chapga 2 qadam</td><td>−7</td></tr>
  <tr><td>−5 − 2</td><td>Chapga 2 qadam (yuqoridagi bilan bir xil)</td><td>−7</td></tr>
  <tr><td>−5 − (−2)</td><td>Oʻngga 2 qadam</td><td>−3</td></tr>
</table></div>

<p>Jadvalning ikkinchi va uchinchi qatoriga diqqat qiling: <b>−5 + (−2)</b> va
<b>−5 − 2</b> — bu bitta hisobning ikki xil yozuvi. Xuddi shunday, birinchi va
toʻrtinchi qator ham bir-biriga teng.</p>

<h3>5. Uchta va undan koʻp son</h3>

<p>Uzun ifodada shoshilmang: chapdan oʻngga, bittalab yuring.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">−8 + 15 − 4 − 6</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">7 − 4 − 6</span>
    <span class="pm-solve__why">−8 + 15 = 7 (musbat kuchliroq)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 − 6</span>
    <span class="pm-solve__why">7 − 4 = 3</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= −3</span>
    <span class="pm-solve__why">3 − 6 = −3, chunki 6 kuchliroq</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Ikkinchi yoʻl — guruhlash</p>
  <p>Musbatlarni alohida, manfiylarni alohida yigʻish ham mumkin:
  musbatlar 15, manfiylar 8 + 4 + 6 = 18. Soʻng 15 − 18 = −3. Xuddi shu javob.</p>
</div>

<h3>6. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>Bekzodning telefon hisobida <b>12 000 soʻm</b> bor edi. U <b>20 000 soʻmlik</b>
  internet paketini qarzga oldi. Ertasi kuni hisobiga <b>15 000 soʻm</b> tashladi.
  Hozir uning hisobida qancha pul bor?</p>
</div>

<p><b>Nima soʻralyapti?</b> Oxirgi holat — hisobdagi pul. <b>Reja:</b> boshlangʻich
puldan paket narxini ayiramiz (minusga tushishi mumkin), keyin toʻldirilgan pulni
qoʻshamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 000 − 20 000</span>
    <span class="pm-solve__why">Paket puldan qimmat — hisob minusga tushadi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= −8 000</span>
    <span class="pm-solve__why">20 000 − 12 000 = 8 000, ishora manfiy: 8 000 soʻm qarz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">−8 000 + 15 000</span>
    <span class="pm-solve__why">Hisobga 15 000 soʻm tashlandi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 7 000 soʻm</span>
    <span class="pm-solve__why">15 000 − 8 000 = 7 000, musbat kuchliroq</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Boshqa yoʻldan yuramiz: Bekzod jami 12 000 + 15 000 = 27 000 soʻm kiritdi va
  20 000 soʻm sarfladi. 27 000 − 20 000 = <b>7 000</b> ✓ — javob bir xil chiqdi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Sarf (20 000) tushumdan (27 000) kichik, demak javob musbat va 10 000 dan
  kichik boʻlishi kerak. 7 000 shu oraliqda — mantiqiy.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">−3 − 5 = −2</p>
  <p class="pe-fix__good">−3 − 5 = −8</p>
  <p class="pe-fix__why">Bu yerda ayirish emas, ikkala harakat ham chapga: −3 dan yana
  5 qadam chapga. Sonlar bir-birini yemaydi, qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">−7 + 3 = −10</p>
  <p class="pe-fix__good">−7 + 3 = −4</p>
  <p class="pe-fix__why">Ishoralari har xil, demak sonlar bir-biriga qarshi yuradi:
  7 − 3 = 4. Ishora nol dan uzoqrogʻidan — manfiy.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">5 − (−2) = 3</p>
  <p class="pe-fix__good">5 − (−2) = 7</p>
  <p class="pe-fix__why">Manfiy sonni ayirish — uni qoʻshish demak: 5 + 2 = 7. Ikki
  minus yonma-yon kelsa, plus boʻladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. −6 + 2 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>−4.</b> Ishoralar har xil: 6 − 2 = 4, uzoqrogʻi manfiy — javob −4.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. −5 + (−9) = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>−14.</b> Ikkalasi ham chapga: 5 + 9 = 14 qadam chapga.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 4 − 11 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>−7.</b> 4 + (−11): 11 − 4 = 7, uzoqrogʻi manfiy.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. −8 − (−3) = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>−5.</b> −8 + 3 ga aylanadi: 8 − 3 = 5, uzoqrogʻi manfiy — −5. Diqqat: javob
    −11 emas, chunki biz manfiy sonni <i>ayirdik</i>, qoʻshmadik.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Ertalab harorat −6 °C edi. Kunduzi 9 daraja isidi, kechqurun
  esa yana 4 daraja sovidi. Kechqurun havo necha daraja boʻldi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>−1 °C.</b> Isish — qoʻshish, sovish — ayirish:
    −6 + 9 = 3, keyin 3 − 4 = −1. Kechqurun yana noldan pastga tushib ketdi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Manfiy son</b><span>noldan kichik son; ingl. negative number</span></li>
  <li><b>Musbat son</b><span>noldan katta son; ingl. positive number</span></li>
  <li><b>Qarama-qarshi son</b><span>noldan bir xil uzoqlikdagi, ishorasi teskari son;
    ingl. opposite number</span></li>
  <li><b>Son oʻqi</b><span>sonlar tartib bilan joylashgan chiziq; ingl. number line</span></li>
  <li><b>Yigʻindi</b><span>qoʻshish natijasi; ingl. sum</span></li>
  <li><b>Ayirma</b><span>ayirish natijasi; ingl. difference</span></li>
  <li><b>Ishora</b><span>sonning oldidagi + yoki − belgisi; ingl. sign</span></li>
  <li><b>Nol</b><span>musbat ham, manfiy ham boʻlmagan chegara soni; ingl. zero</span></li>
  <li><b>Qarz</b><span>manfiy son bilan yoziladigan yetishmovchilik; ingl. debt</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Qoʻshish — yurish.</b> Musbat son oʻngga, manfiy son chapga olib boradi.</li>
    <li><b>Ishoralar bir xil boʻlsa qoʻshamiz</b> va ishorani saqlaymiz; <b>har xil
      boʻlsa ayiramiz</b> va nol dan uzoqrogʻining ishorasini olamiz.</li>
    <li><b>a − b = a + (−b).</b> Shuning uchun 5 − (−2) = 5 + 2 = 7 — ikki minus plus
      beradi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-11 — manfiy sonlarni koʻpaytirish va boʻlish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-11: Manfiy sonlarni koʻpaytirish va boʻlish — ishoralar qoidasi",
        "category": "math",
        "order": 11,
        "summary": (
            "Nega ikkita manfiy sonning koʻpaytmasi musbat chiqadi? Ishoralar qoidasi, "
            "uning sababi, minuslarni sanash usuli va qarz masalalari."
        ),
        "stories": ["Doʻkon daftaridagi qarz"],
        "content": """
<h2>PM-11: Manfiy sonlarni koʻpaytirish va boʻlish — ishoralar qoidasi</h2>

<p>Mahalladagi doʻkonchi Karim akaning eski daftari bor. Kimdir pulsiz kelsa, u qarzni
yozib qoʻyadi. Sherbek olti kun ketma-ket bir xil non oldi — har kuni <b>2 500 soʻm</b>.
Karim aka daftarni yopib dedi: «Oʻgʻlim, olti kun, har kuni ikki yarim ming.» Bu
qoʻshish emas — <b>koʻpaytirish</b>, faqat manfiy tomonga qarab.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ishoralar qoidasini bilib olasiz: bir xil → musbat, har xil → manfiy;</li>
    <li>nega (−) × (−) = (+) ekanini <i>tushunasiz</i>, yodlamaysiz;</li>
    <li>minuslarni sanab, uzun koʻpaytmaning ishorasini bir qarashda aytasiz;</li>
    <li>boʻlishda ham xuddi shu qoida ishlashini koʻrasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ishoralar qoidasi (faqat × va ÷ uchun)</span>
  <span class="pe-chip pe-chip--v">(+)(+) = +</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">(+)(−) = −</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">(−)(+) = −</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">(−)(−) = +</span>
</div>

<h3>1. Manfiyni musbatga koʻpaytirish — bu takroriy qoʻshish</h3>

<p>Bu holat eng oson, chunki PM-3 dagi taʼrif oʻzgarmaydi: koʻpaytirish — bir xil sonni
qayta-qayta qoʻshish.</p>

<div class="pe-ex">
  <p class="pe-ex__math">6 × (−2 500) = −15 000</p>
  <p class="pe-ex__uz">Olti kun, har kuni 2 500 soʻm qarz. Jami qarz — 15 000 soʻm,
  yaʼni hisobda −15 000.</p>
  <p class="pe-ex__why">Chunki (−2 500) + (−2 500) + … olti marta takrorlansa,
  javob −15 000 boʻladi: hammasi bir tomonga qoʻshiladi.</p>
</div>

<p>Demak, <b>manfiy × musbat = manfiy</b>. Koʻpaytuvchilarni oʻrnini almashtirsak ham
hech narsa oʻzgarmaydi: (−2 500) × 6 ham −15 000.</p>

<h3>2. Nega (−) × (−) = (+)</h3>

<p>Bu maktabdagi eng koʻp «shunchaki yodla» deb oʻtiladigan qoida. Aslida sabab bor va u
juda chiroyli. Quyidagi ustunga qarang — biz har safar birinchi koʻpaytuvchini bittaga
kamaytirib boramiz:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 × (−4) = −12</span>
    <span class="pm-solve__why">Tanish holat</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 × (−4) = −8</span>
    <span class="pm-solve__why">Javob 4 taga <b>oshdi</b></span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 × (−4) = −4</span>
    <span class="pm-solve__why">Yana 4 taga oshdi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">0 × (−4) = 0</span>
    <span class="pm-solve__why">Yana 4 taga oshdi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(−1) × (−4) = 4</span>
    <span class="pm-solve__why">Naqsh buzilmasa, javob 4 boʻlishi shart</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(−2) × (−4) = 8</span>
    <span class="pm-solve__why">Yana 4 taga oshdi — musbat davom etadi</span>
  </div>
</div>

<p>Har qatorda javob <b>bir xil miqdorda — 4 taga</b> oshib bordi. Matematikada naqsh
sababsiz buzilmaydi. Agar (−1) × (−4) ni −4 desak, ustun buziladi va butun arifmetika
qarama-qarshilikka tushadi. Shuning uchun javob musbat boʻlishi <i>shart</i>.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Hayotiy maʼno</p>
  <p>Karim aka Sherbekning kunlik qarzini kechira boshladi. «Uch kunlik qarzingni
  oʻchirdim» — bu <b>qarzni olib tashlash</b>, yaʼni manfiyni manfiy marta olish:
  (−3) × (−2 500) = +7 500. Sherbekning ahvoli 7 500 soʻmga <b>yaxshilandi</b>.
  Yomonlikni olib tashlash — yaxshilik.</p>
</div>

<h3>3. Qoidani ishlatamiz</h3>

<p>Amaliyotda tartib doim bitta: <b>avval sonlarni ishorasiz koʻpaytiring, keyin
ishorani qoʻying</b>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">(−7) × (−8)</span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">7 × 8 = 56</span>
    <span class="pm-solve__why">Avval ishorasiz koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(−7) × (−8) = 56</span>
    <span class="pm-solve__why">Ishoralar bir xil — javob musbat</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Eng katta xato — qoidani qoʻshishga koʻchirish</p>
  <p>«Ikki minus plus beradi» degan jumla <b>faqat koʻpaytirish va boʻlishda</b>
  ishlaydi. Qoʻshishda emas!</p>
  <p><b>−2 − 3 = −5</b>, lekin <b>(−2) × (−3) = 6</b>. Ikkita butunlay boshqa amal.
  PM-10 dagi «ikki minus plus» esa boshqa narsa edi: u <b>ayirilayotgan</b> manfiy son
  haqida — 5 − (−3) = 8.</p>
</div>

<h3>4. Boʻlish — xuddi shu qoida</h3>

<p>Boʻlish koʻpaytirishning teskarisi, shuning uchun ishoralar qoidasi soʻzma-soʻz
takrorlanadi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Ifoda</th><th>Ishoralar</th><th>Javob</th></tr>
  <tr><td>−24 ÷ 6</td><td>har xil</td><td>−4</td></tr>
  <tr><td>24 ÷ (−6)</td><td>har xil</td><td>−4</td></tr>
  <tr><td>−24 ÷ (−6)</td><td>bir xil</td><td>4</td></tr>
  <tr><td>24 ÷ 6</td><td>bir xil</td><td>4</td></tr>
</table></div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>−24 ÷ (−6) = 4 toʻgʻrimi? Koʻpaytirib koʻramiz: 4 × (−6) = −24 ✓. Har qanday
  boʻlishni shu yoʻl bilan bir soniyada tekshirsa boʻladi.</p>
</div>

<h3>5. Nechta minus bor?</h3>

<p>Uzun koʻpaytmada ishorani topish uchun hisoblash shart emas — <b>minuslarni sanang</b>.
Har bir juft minus bir-birini yoʻq qiladi.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Minuslar soni</span>
  <span class="pe-chip pe-chip--v">juft (2, 4, 6…) → javob musbat</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">toq (1, 3, 5…) → javob manfiy</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">(−2) × 3 × (−5) = 30</p>
  <p class="pe-ex__uz">Ikkita minus — juft, demak musbat. Sonlar: 2 × 3 × 5 = 30.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">(−1) × (−2) × (−3) = −6</p>
  <p class="pe-ex__uz">Uchta minus — toq, demak manfiy. Sonlar: 1 × 2 × 3 = 6.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Bir soniyalik usul</p>
  <p>(−1) × (−2) × (−3) × (−4) × (−5) — hisoblamang, sanang: beshta minus, toq son.
  Javob manfiy: −120.</p>
</div>

<h3>6. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>Beshta doʻst birgalikda bir doʻkonda qarzdor boʻlib qolishdi. Har kuni ular
  jami <b>9 000 soʻm</b>lik mahsulot qarzga olishdi va bu <b>5 kun</b> davom etdi.
  Keyin qarzni oʻzaro <b>teng</b> boʻlishdi. Har biriga qancha qarz tushdi?</p>
</div>

<p><b>Nima soʻralyapti?</b> Bir kishining qarzi. <b>Reja:</b> avval jami qarzni topamiz
(koʻpaytirish), keyin uni 5 kishiga boʻlamiz.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Bir kun</span>
    <span class="pm-model__bar" style="width:20%">−9 000</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">Besh kun</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:100%">−45 000</span>
  </div>
  <p class="pm-model__tot">Jami qarz 5 kishiga teng boʻlinadi</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 × (−9 000) = −45 000</span>
    <span class="pm-solve__why">Besh kunlik jami qarz (manfiy × musbat = manfiy)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">−45 000 ÷ 5</span>
    <span class="pm-solve__why">Qarzni 5 kishiga teng boʻlamiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= −9 000 soʻm</span>
    <span class="pm-solve__why">Ishoralar har xil — javob manfiy: har biriga 9 000
    soʻm qarz</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>5 kishi × 9 000 soʻm = 45 000 soʻm ✓ — jami qarz oʻrniga qaytdi.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Qiziq holat</p>
  <p>Bir kunlik qarz ham, bir kishining qarzi ham 9 000 soʻm chiqdi. Bu tasodif: 5 kun
  va 5 kishi teng edi. Agar 4 kishi boʻlganda, javob −45 000 ÷ 4 = −11 250 soʻm boʻlardi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">(−4) × (−5) = −20</p>
  <p class="pe-fix__good">(−4) × (−5) = 20</p>
  <p class="pe-fix__why">Ishoralar bir xil — javob musbat. «Ikkita manfiy — demak juda
  manfiy» degan tuygʻu aldaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">−2 − 3 = 6</p>
  <p class="pe-fix__good">−2 − 3 = −5</p>
  <p class="pe-fix__why">Bu qoʻshish-ayirish, koʻpaytirish emas. Ishoralar qoidasi
  bu yerda ishlamaydi: ikkala qadam ham chapga.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">(−1) × (−2) × (−3) = 6</p>
  <p class="pe-fix__good">(−1) × (−2) × (−3) = −6</p>
  <p class="pe-fix__why">Uchta minus — toq son. Birinchi ikkitasi plus berdi, uchinchisi
  javobni yana manfiyga aylantirdi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. (−6) × 7 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>−42.</b> 6 × 7 = 42, ishoralar har xil — javob manfiy.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. (−8) × (−5) = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>40.</b> 8 × 5 = 40, ishoralar bir xil — javob musbat.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. −36 ÷ (−9) = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4.</b> 36 ÷ 9 = 4, ishoralar bir xil — musbat. Tekshiruv: 4 × (−9) = −36 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. (−2) × (−3) × (−4) = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>−24.</b> Uchta minus — toq, javob manfiy. Sonlar: 2 × 3 × 4 = 24.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Toqqa chiqqan sayin havo soviydi: har 100 metrda harorat
  taxminan 1 daraja pasayadi. Etakda havo 6 °C. 900 metr koʻtarilgach, harorat necha
  daraja boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>−3 °C.</b> 900 ÷ 100 = 9 ta yuz metr. Har biri −1 daraja: 9 × (−1) = −9.
    Soʻng 6 + (−9) = −3. Etakda musbat, choʻqqida esa noldan past.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Koʻpaytma</b><span>koʻpaytirish natijasi; ingl. product</span></li>
  <li><b>Boʻlinma</b><span>boʻlish natijasi; ingl. quotient</span></li>
  <li><b>Koʻpaytuvchi</b><span>koʻpaytirilayotgan sonlarning har biri; ingl. factor</span></li>
  <li><b>Ishoralar qoidasi</b><span>bir xil ishora musbat, har xil ishora manfiy javob
    beradi; ingl. sign rule</span></li>
  <li><b>Manfiy son</b><span>noldan kichik son; ingl. negative number</span></li>
  <li><b>Juft son</b><span>2 ga qoldiqsiz boʻlinadigan son; ingl. even number</span></li>
  <li><b>Toq son</b><span>2 ga boʻlinmaydigan son; ingl. odd number</span></li>
  <li><b>Qarz</b><span>manfiy son bilan yoziladigan yetishmovchilik; ingl. debt</span></li>
  <li><b>Teng boʻlish</b><span>bir xil ulushlarga ajratish; ingl. equal sharing</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Bir xil ishora — musbat, har xil ishora — manfiy.</b> Koʻpaytirishda ham,
      boʻlishda ham.</li>
    <li><b>Minuslarni sanang:</b> juft boʻlsa musbat, toq boʻlsa manfiy.</li>
    <li><b>Bu qoida qoʻshish-ayirishga tegishli emas.</b> −2 − 3 = −5, lekin
      (−2) × (−3) = 6.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-12 — daraja
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-12: Daraja: takroriy koʻpaytirishning qisqa yozuvi",
        "category": "math",
        "order": 12,
        "summary": (
            "2 × 2 × 2 × 2 × 2 ni qisqa yozish mumkinmi? Asos va koʻrsatkich, kvadrat va "
            "kub, oʻnning darajalari, manfiy asos va darajaning amallar tartibidagi oʻrni."
        ),
        "stories": ["Shaxmat taxtasidagi bugʻdoy"],
        "content": """
<h2>PM-12: Daraja: takroriy koʻpaytirishning qisqa yozuvi</h2>

<p>Bir varaq qogʻozni ikki buklang — ikki qavat boʻldi. Yana bukdingiz — toʻrt. Yana —
sakkiz. Jasur sinfdoshlariga aytdi: «Oʻn marta buklasam, yuztacha qavat chiqadi-ku».
Aslida <b>1 024</b> qavat chiqadi. Bunday tez oʻsadigan hisoblarni yozish uchun
matematikada alohida, juda qisqa yozuv bor — <b>daraja</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>daraja yozuvini oʻqiysiz va yozasiz: asos va koʻrsatkich;</li>
    <li>kvadrat va kubni farqlaysiz, 1 dan 12 gacha kvadratlarni bilasiz;</li>
    <li>oʻnning darajalari razryadlar bilan qanday bogʻlanishini koʻrasiz;</li>
    <li>manfiy asosli darajaning ishorasini bir qarashda aytasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Taʼrif</span>
  <span class="pe-chip pe-chip--o">a<sup>n</sup></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">a × a × … × a</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">n marta</span>
</div>

<h3>1. Qisqa yozuv</h3>

<p>2 × 2 × 2 × 2 × 2 — beshta ikki. Buni <b>2<sup>5</sup></b> deb yozamiz. Pastdagi katta
son <b>asos</b> deyiladi (nimani koʻpaytiryapmiz), yuqoridagi kichik son esa
<b>koʻrsatkich</b> (necha marta koʻpaytiryapmiz).</p>

<div class="pe-ex">
  <p class="pe-ex__math">2<sup>5</sup> = 2 × 2 × 2 × 2 × 2 = 32</p>
  <p class="pe-ex__uz">Asos — 2, koʻrsatkich — 5. Oʻqilishi: «ikkining beshinchi
  darajasi».</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Eng koʻp uchraydigan chalkashlik</p>
  <p>2<sup>3</sup> — bu 2 × 3 <b>emas</b>. Koʻrsatkich koʻpaytuvchi emas, u
  <i>nechtaligini</i> aytadi: 2<sup>3</sup> = 2 × 2 × 2 = <b>8</b>, 2 × 3 esa 6.</p>
</div>

<h3>2. Qanday oʻqiladi</h3>

<div class="pe-table-wrap"><table>
  <tr><th>Yozuv</th><th>Oʻqilishi</th><th>Yoyilmasi</th><th>Qiymati</th></tr>
  <tr><td>7<sup>1</sup></td><td>yettining birinchi darajasi</td><td>7</td><td>7</td></tr>
  <tr><td>5<sup>2</sup></td><td>besh kvadrat</td><td>5 × 5</td><td>25</td></tr>
  <tr><td>4<sup>3</sup></td><td>toʻrt kub</td><td>4 × 4 × 4</td><td>64</td></tr>
  <tr><td>3<sup>4</sup></td><td>uchning toʻrtinchi darajasi</td><td>3 × 3 × 3 × 3</td><td>81</td></tr>
</table></div>

<p>Ikkinchi daraja alohida nom oldi — <b>kvadrat</b>, chunki tomoni 5 boʻlgan kvadratning
yuzasi aynan 5 × 5. Uchinchi daraja — <b>kub</b>, qirrasi 4 boʻlgan kubning hajmi
4 × 4 × 4. Nomlar shakllardan kelib chiqqan.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 160" role="img" aria-label="Tomoni 5 boʻlgan kvadrat">
    <rect class="pm-fill pm-fill--hl" x="40" y="20" width="120" height="120"/>
    <rect class="pm-ln" x="40" y="20" width="120" height="120" fill="none"/>
    <text class="pm-lbl" x="85" y="155">5</text>
    <text class="pm-lbl" x="20" y="85">5</text>
    <text class="pm-lbl pm-lbl--hl" x="185" y="85">5 × 5 = 5² = 25 ta katak</text>
  </svg>
  <figcaption>«Kvadrat» soʻzi shakldan kelgan: tomoni 5 boʻlgan kvadratda 25 ta katak bor.</figcaption>
</figure>

<h3>3. Kvadratlar jadvali — yodda tursin</h3>

<p>Quyidagi 12 ta son butun maktab davomida kerak boʻladi. Ularni bilgan oʻquvchi keyingi
darsda (kvadrat ildiz) hech qiynalmaydi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>n</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td>
      <td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr>
  <tr><th>n<sup>2</sup></th><td>1</td><td>4</td><td>9</td><td>16</td><td>25</td><td>36</td>
      <td>49</td><td>64</td><td>81</td><td>100</td><td>121</td><td>144</td></tr>
</table></div>

<p>Kublardan esa dastlabki beshtasi yetarli: 1<sup>3</sup> = 1, 2<sup>3</sup> = 8,
3<sup>3</sup> = 27, 4<sup>3</sup> = 64, 5<sup>3</sup> = 125. Diqqat qiling — 64 ham
kvadrat (8<sup>2</sup>), ham kub (4<sup>3</sup>). Bunday sonlar kam uchraydi.</p>

<h3>4. Oʻnning darajalari</h3>

<p>PM-1 dagi razryadlar aslida oʻnning darajalari edi — biz buni endi yozib qoʻya olamiz.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Daraja</th><th>Qiymati</th><th>Nollar soni</th></tr>
  <tr><td>10<sup>1</sup></td><td>10</td><td>1</td></tr>
  <tr><td>10<sup>2</sup></td><td>100</td><td>2</td></tr>
  <tr><td>10<sup>3</sup></td><td>1 000</td><td>3</td></tr>
  <tr><td>10<sup>6</sup></td><td>1 000 000</td><td>6</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Qoida</p>
  <p>10 ning darajasida <b>nollar soni koʻrsatkichga teng</b>. Shuning uchun bir million
  — 10<sup>6</sup>, bir milliard — 10<sup>9</sup>.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Nima uchun kerak</p>
  <p>Katta sonlarni yozish qisqaradi. Yerdan Quyoshgacha taxminan 150 000 000 km — buni
  15 × 10<sup>7</sup> km deb yozsa, nollarni sanab oʻtirmaysiz.</p>
</div>

<h3>5. Manfiy asos — PM-11 ish beradi</h3>

<p>Asos manfiy boʻlsa, ishorani aniqlash uchun oʻtgan darsdagi usul ishlaydi:
<b>minuslarni sanaymiz</b>. Koʻrsatkich — bu aynan minuslar soni.</p>

<div class="pe-ex">
  <p class="pe-ex__math">(−3)<sup>2</sup> = (−3) × (−3) = 9</p>
  <p class="pe-ex__uz">Ikkita minus — juft, javob musbat.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">(−3)<sup>3</sup> = (−3) × (−3) × (−3) = −27</p>
  <p class="pe-ex__uz">Uchta minus — toq, javob manfiy.</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Qoida</p>
  <p>Manfiy asos, <b>juft</b> koʻrsatkich → javob <b>musbat</b>. Manfiy asos,
  <b>toq</b> koʻrsatkich → javob <b>manfiy</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Qavs bormi yoki yoʻqmi — bu hamma narsani hal qiladi</p>
  <p><b>(−4)<sup>2</sup> = 16</b>, chunki qavs butun manfiy sonni darajaga koʻtaradi.<br>
  <b>−4<sup>2</sup> = −16</b>, chunki bu yerda avval 4 kvadratga koʻtariladi (16), keyin
  oldiga minus qoʻyiladi. Minus darajaga kirmagan.</p>
  <p>Imtihonlarda shu ikki yozuvni chalkashtirish juda koʻp uchraydi. Qavsga qarang.</p>
</div>

<h3>6. Amallar tartibida darajaning oʻrni</h3>

<p>PM-5 dagi zinapoyaga endi yangi pogʻona qoʻshiladi. Daraja qavsdan keyin, lekin
koʻpaytirish-boʻlishdan <b>oldin</b> bajariladi.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Amallar tartibi</span>
  <span class="pe-chip pe-chip--s">1. qavs</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">2. daraja</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">3. × va ÷</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">4. + va −</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 + 3 × 4<sup>2</sup></span>
    <span class="pm-solve__why">Berilgan</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 + 3 × 16</span>
    <span class="pm-solve__why">Avval daraja: 4<sup>2</sup> = 16</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 + 48</span>
    <span class="pm-solve__why">Keyin koʻpaytirish</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 50</span>
    <span class="pm-solve__why">Oxirida qoʻshish</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Solishtiring</p>
  <p>(2 + 3) × 4<sup>2</sup> = 5 × 16 = <b>80</b>. Qavs tartibni oʻzgartirdi va javob
  ham butunlay boshqa chiqdi.</p>
</div>

<h3>7. Matnli masala</h3>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Masala</p>
  <p>Laboratoriyada bakteriyalar har soatda soni <b>ikki baravar</b> ortadi. Tajriba
  boshida idishda <b>4 ta</b> bakteriya bor edi. <b>5 soatdan</b> keyin nechta boʻladi?</p>
</div>

<p><b>Nima soʻralyapti?</b> 5 soatdan keyingi soni. <b>Reja:</b> har soat ×2 boʻladi,
demak 5 soatda beshta ikkiga koʻpaytiriladi — bu 2<sup>5</sup>.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 × 2 × 2 × 2 × 2 × 2</span>
    <span class="pm-solve__why">Har soatda bir marta ikkiga koʻpaytiramiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 × 2<sup>5</sup></span>
    <span class="pm-solve__why">Beshta ikkini daraja bilan qisqartirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 × 32</span>
    <span class="pm-solve__why">2<sup>5</sup> = 32</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= 128 ta bakteriya</span>
    <span class="pm-solve__why">Javob</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Soat-soat sanaymiz: 4 → 8 → 16 → 32 → 64 → <b>128</b>. Beshta oʻqni bosib oʻtdik,
  javob mos keldi ✓</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Har soatda soni ikki baravar oshsa, 5 soatda taxminan 30 barobar oshadi
  (2<sup>5</sup> = 32). 4 ning 30 barobari — 120 atrofida. 128 shu yerda.</span>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Nega bu muhim</p>
  <p>Ikkilanib oʻsish odamning tasavvuridan tezroq ketadi. Shu darsning oʻqish matnida
  shaxmat taxtasi va bugʻdoy haqidagi qadimiy rivoyatni oʻqiysiz — u aynan shu haqda.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">3<sup>4</sup> = 12</p>
  <p class="pe-fix__good">3<sup>4</sup> = 81</p>
  <p class="pe-fix__why">Koʻrsatkich koʻpaytuvchi emas. 3 × 3 × 3 × 3 = 81, 3 × 4 esa
  butunlay boshqa hisob.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">(−2)<sup>4</sup> = −16</p>
  <p class="pe-fix__good">(−2)<sup>4</sup> = 16</p>
  <p class="pe-fix__why">Toʻrtta minus — juft son, demak javob musbat. Minuslarni sanang.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">−5<sup>2</sup> = 25</p>
  <p class="pe-fix__good">−5<sup>2</sup> = −25</p>
  <p class="pe-fix__why">Qavs yoʻq — demak avval 5 kvadratga koʻtariladi (25), minus
  esa tashqarida qoladi. Agar (−5)<sup>2</sup> yozilganda, javob 25 boʻlardi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 2<sup>6</sup> = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>64.</b> 2 × 2 × 2 × 2 × 2 × 2. Ikkilarni bosqichma-bosqich sanang:
    2, 4, 8, 16, 32, 64.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 5<sup>3</sup> = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>125.</b> 5 × 5 = 25, 25 × 5 = 125.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. (−2)<sup>3</sup> = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>−8.</b> Uchta minus — toq, javob manfiy. Sonlar: 2 × 2 × 2 = 8.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 10<sup>5</sup> = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>100 000.</b> Bir va beshta nol — koʻrsatkich nollar sonini aytadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Omborda 4 ta javon bor. Har javonda 4 ta quti, har qutida
  4 ta paket, har paketda 4 ta daftar. Omborda jami nechta daftar bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>256 ta.</b> 4 × 4 × 4 × 4 = 4<sup>4</sup> = 256. Bosqichlar: 4 javon → 16 quti
    → 64 paket → 256 daftar.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Daraja</b><span>bir sonni oʻziga qayta-qayta koʻpaytirish yozuvi;
    ingl. power</span></li>
  <li><b>Asos</b><span>darajada koʻpaytirilayotgan son; ingl. base</span></li>
  <li><b>Koʻrsatkich</b><span>necha marta koʻpaytirilishini bildiruvchi kichik son;
    ingl. exponent</span></li>
  <li><b>Kvadrat</b><span>ikkinchi daraja, n<sup>2</sup>; ingl. square</span></li>
  <li><b>Kub</b><span>uchinchi daraja, n<sup>3</sup>; ingl. cube</span></li>
  <li><b>Aniq kvadrat</b><span>butun sonning kvadrati boʻlgan son (1, 4, 9, 16…);
    ingl. perfect square</span></li>
  <li><b>Oʻnning darajasi</b><span>10, 100, 1 000 kabi sonlar; ingl. power of ten</span></li>
  <li><b>Amallar tartibi</b><span>qaysi amal oldin bajarilishi; ingl. order of
    operations</span></li>
  <li><b>Ikkilanish</b><span>har qadamda ikki baravar ortish; ingl. doubling</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>a<sup>n</sup> — n ta a ning koʻpaytmasi.</b> Koʻrsatkich koʻpaytuvchi emas:
      2<sup>3</sup> = 8, 2 × 3 = 6.</li>
    <li><b>Manfiy asosda minuslarni sanang:</b> juft koʻrsatkich musbat, toq koʻrsatkich
      manfiy javob beradi.</li>
    <li><b>Qavsga qarang:</b> (−5)<sup>2</sup> = 25, lekin −5<sup>2</sup> = −25.</li>
  </ul>
</div>
""",
    },
]
