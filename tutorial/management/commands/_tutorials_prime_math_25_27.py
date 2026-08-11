# -*- coding: utf-8 -*-
"""Prime Math — Blok B, darslar 25–27 (foiz oʻzgarishi, bozor matematikasi, nisbat).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_25_27.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_25_27.py

⚠️ Kumulyativ:
  • PM-25 KOʻPAYTUVCHI gʻoyasini ochadi (1,2 va 0,8) — PM-22 dagi «foiz =
    oʻnlik kasr» ustiga quriladi;
  • PM-26 PM-25 ning bozordagi qoʻllanishi: chegirma, ustama, QQS. Yangi
    formula yoʻq, faqat yangi soʻzlar;
  • PM-27 nisbatni ochadi — proporsiya, masshtab va teskari proporsionallik
    PM-28 da, shuning uchun bu darsda ular yoʻq;
  • tenglama (PM-36) hali yoʻq: nisbat masalalari «bir qism» usuli bilan
    yechiladi, x bilan emas.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_25_27.py --author=prime
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
    # PM-25 — foiz oʻzgarishi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-25: Foiz oʻzgarishi: oshdi, kamaydi, necha foizga?",
        "category": "math",
        "order": 25,
        "summary": (
            "Narx 4000 dan 5000 ga chiqsa, necha foizga oshgan? Oʻzgarish foizini "
            "topish, koʻpaytuvchi bilan tez hisoblash va «20% oshib, 20% kamaysa "
            "eski narxga qaytmaydi» degan haqiqat."
        ),
        "stories": ["Narx oshdi, keyin tushdi"],
        "content": """
<h2>PM-25: Foiz oʻzgarishi: oshdi, kamaydi, necha foizga?</h2>

<p>Bir yil oldin non <b>4000</b> soʻm edi, bugun <b>5000</b> soʻm. «Ming soʻmga qimmatlashdi»
degan gap toʻgʻri, lekin u koʻp narsa aytmaydi: bir million soʻmlik telefonning ming soʻmi
sezilmaydi ham. Shuning uchun oʻzgarishni <b>foizda</b> aytamiz — shunda oʻzgarish oʻz
kattaligiga nisbatan oʻlchanadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>miqdor necha foizga oshgani yoki kamayganini topasiz;</li>
    <li>berilgan foizga oshirilgan va kamaytirilgan qiymatni hisoblaysiz;</li>
    <li>koʻpaytuvchi bilan bir amalda ishlaysiz (1,2 va 0,8);</li>
    <li>ketma-ket ikki oʻzgarish nima uchun qoʻshilmasligini bilasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻzgarish foizi</span>
  <span class="pe-chip pe-chip--o">oʻzgarish ÷ ESKI qiymat × 100</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">oshdi: × (1 + p/100)</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">kamaydi: × (1 − p/100)</span>
</div>

<h3>1. Asos har doim ESKI qiymat</h3>

<p>Bu darsning butun mazmuni bitta jumlada: <b>oʻzgarish nimadan boshlangan boʻlsa, oʻshanga
nisbatan oʻlchanadi</b>. Non 4000 dan 5000 ga chiqdi — demak asos 4000, chunki oʻsish oʻsha
narxdan boshlandi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5000 − 4000 = 1000</span>
    <span class="pm-solve__why">Avval oʻzgarishning oʻzini topamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1000 ÷ 4000 = 0,25</span>
    <span class="pm-solve__why">Oʻzgarishni ESKI narxga boʻldik (PM-24 dagi «necha foiz?»)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">0,25 × 100 = 25%</span>
    <span class="pm-solve__why">Non 25 foizga qimmatlashgan</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Yangi narxga boʻlish — eng koʻp uchraydigan xato</p>
  <p>1000 ÷ 5000 = 20% degan javob ham «chiroyli» koʻrinadi, lekin notoʻgʻri. Oʻylab koʻring:
  narx 4000 dan oʻsdi, 5000 dan emas. Yangi qiymat hali mavjud ham emas edi, u qanday asos
  boʻlsin? <b>Qaysi son avval kelgan boʻlsa, oʻsha — asos.</b></p>
</div>

<h3>2. Kamayish ham xuddi shunday</h3>

<p>Telefon <b>3 000 000</b> soʻm edi, hozir <b>2 400 000</b> soʻm. Amal oʻzgarmaydi, faqat
farq manfiy tomonga qarab oʻlchanadi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">3 000 000 − 2 400 000 = 600 000; 600 000 ÷ 3 000 000 = 0,2</p>
  <p class="pe-ex__uz">Telefon 20 foizga arzonlashgan.</p>
  <p class="pe-ex__why">Asos — eski narx 3 000 000, chunki tushish oʻshandan boshlangan.</p>
</div>

<h3>3. Koʻpaytuvchi — bir amalda javob</h3>

<p>Endi teskari savol: <b>800 000</b> soʻmlik mahsulot 15 foizga qimmatlashsa, yangi narx
qancha? Ikki qadamda ishlash mumkin: 15 foizni topib (120 000), narxga qoʻshish. Lekin bir
qadamda ham boʻladi.</p>

<p>Butun narx — 100%. Unga 15% qoʻshilsa, yangi narx eskining <b>115%</b> i boʻladi. 115% esa
oʻnlik kasrda <b>1,15</b>. Demak:</p>

<div class="pe-ex">
  <p class="pe-ex__math">800 000 × 1,15 = 920 000</p>
  <p class="pe-ex__uz">Sakkiz yuz mingga oʻn besh foiz qoʻshilsa, toʻqqiz yuz yigirma ming
  boʻladi.</p>
  <p class="pe-ex__why">1 — eski narxning oʻzi, 0,15 — qoʻshimcha. Ikkalasi birga 1,15.</p>
</div>

<p>Kamayishda ham xuddi shu mantiq, faqat ayirib: 20 foizga arzonlagan narx eskining
<b>80%</b> i, yaʼni <b>0,8</b> ga koʻpaytirilgani.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Oʻzgarish</th><th>Koʻpaytuvchi</th><th>Misol</th></tr>
  <tr><td>10% oshdi</td><td>× 1,1</td><td>50 000 → 55 000</td></tr>
  <tr><td>15% oshdi</td><td>× 1,15</td><td>800 000 → 920 000</td></tr>
  <tr><td>50% oshdi</td><td>× 1,5</td><td>40 000 → 60 000</td></tr>
  <tr><td>10% kamaydi</td><td>× 0,9</td><td>50 000 → 45 000</td></tr>
  <tr><td>20% kamaydi</td><td>× 0,8</td><td>60 000 → 48 000</td></tr>
  <tr><td>25% kamaydi</td><td>× 0,75</td><td>40 000 → 30 000</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Koʻpaytuvchini oʻqishni oʻrganing</p>
  <p>Koʻpaytuvchi 1 dan katta boʻlsa — oʻsish, kichik boʻlsa — kamayish. 1,08 «sakkiz foizga
  oshdi», 0,92 esa «sakkiz foizga kamaydi» degani. Bu bitta son ichida butun jumla
  yashiringan.</p>
</div>

<h3>4. Ikki oʻzgarish qoʻshilmaydi</h3>

<p>Mana bu darsning eng qiziq joyi. Narx avval <b>20 foizga oshdi</b>, keyin
<b>20 foizga tushdi</b>. Eski narxga qaytdimi? Koʻpchilik «ha» deydi. Tekshiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">100 000 × 1,2 = 120 000</span>
    <span class="pm-solve__why">20 foizga oshdi — asos eski narx 100 000</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">120 000 × 0,8 = 96 000</span>
    <span class="pm-solve__why">20 foizga tushdi — endi asos YANGI narx 120 000</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">96 000 &lt; 100 000</span>
    <span class="pm-solve__why">Narx eskisidan 4 foizga arzon boʻlib qoldi</span>
  </div>
</div>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">Eski narx</span>
    <span class="pm-model__bar" style="width:100%">100 000</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">+20%</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:120%">120 000</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">−20%</span>
    <span class="pm-model__bar" style="width:96%">96 000</span>
  </div>
  <p class="pm-model__tot">Ikkinchi 20% kattaroq sondan olindi — shuning uchun qaytmadi</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Sabab: ikki foizning asosi har xil</p>
  <p>Birinchi 20% — 100 000 dan, yaʼni 20 000. Ikkinchi 20% — 120 000 dan, yaʼni 24 000.
  Ayirilgan pul qoʻshilganidan koʻp. <b>Foizlarni qoʻshib boʻlmaydi</b> — koʻpaytuvchilarni
  koʻpaytiramiz: 1,2 × 0,8 = 0,96, demak natija eskining 96 foizi.</p>
</div>

<h3>5. Foiz va foiz punkti — bir xil emas</h3>

<p>Bank omonat stavkasi <b>10 foizdan 12 foizga</b> chiqdi. Bu necha foizga oshish? Ikki
javob ham toʻgʻri, lekin ikki xil savolga:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">2 foiz punkti</p>
    <p>Shunchaki ayirma: 12 − 10 = 2. Stavka <b>ikki punktga</b> koʻtarildi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">20 foizga</p>
    <p>Oʻzgarish foizi: 2 ÷ 10 = 0,2. Stavkaning <b>oʻzi</b> 20 foizga oshdi.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Yangilikda qaysi biri aytilayotganiga eʼtibor bering</p>
  <p>«Stavka 2 foizga oshdi» degan sarlavha koʻpincha aslida 2 <b>punkt</b>ni bildiradi.
  Farqi katta: 10 dan 12 ga oʻtish — bu 2 punkt, lekin butun boshli 20 foizlik oʻsish.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Kitob doʻkonida lugʻat 50 000 soʻm turardi.</b> Yangi yil oldidan narx 10 foizga
oshirildi. Bayramdan keyin doʻkon eʼlon qildi: «Hamma kitobga 10 foiz chegirma!»</p>

<p><b>Savol:</b> lugʻat endi necha soʻm turadi va bu eski narxdan qanchaga farq qiladi?</p>

<p><b>Reja:</b> ikki oʻzgarishni ketma-ket qoʻllaymiz. Ikkinchi foiz oshgan narxdan olinishini
unutmaymiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">50 000 × 1,1 = 55 000</span>
    <span class="pm-solve__why">Bayram oldidan narx 10 foizga oshdi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">55 000 × 0,9 = 49 500</span>
    <span class="pm-solve__why">Chegirma yangi narxdan hisoblanadi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">50 000 − 49 500 = 500</span>
    <span class="pm-solve__why">Eski narxdan atigi 500 soʻm arzon</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">500 ÷ 50 000 = 0,01 → 1%</span>
    <span class="pm-solve__why">«10 foiz chegirma» aslida bor-yoʻgʻi 1 foiz foyda berdi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Koʻpaytuvchilar orqali: 1,1 × 0,9 = 0,99, yaʼni natija eskining 99 foizi ✓
  50 000 × 0,99 = 49 500 ✓ Ikki yoʻl bir xil javob berdi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Bir xil foizga oshib, keyin kamaygan narx har doim eskisidan biroz past tushadi.
  Demak javob 50 000 dan sal kichik boʻlishi kerak edi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">40 000 → 50 000: 10 000 ÷ 50 000 = 20% oshdi</p>
  <p class="pe-fix__good">10 000 ÷ 40 000 = 25% oshdi</p>
  <p class="pe-fix__why">Asos yangi narx deb olingan. Oʻsish <b>eski</b> narxdan boshlangan,
  shuning uchun boʻluvchi ham eski narx — 40 000.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">30% oshdi, keyin 30% tushdi → eski narx qaytdi</p>
  <p class="pe-fix__good">1,3 × 0,7 = 0,91 → narx 9 foizga arzon</p>
  <p class="pe-fix__why">Ikkinchi foiz kattalashgan sondan olinadi. Foizlarni hech qachon
  qoʻshmang yoki ayirmang — koʻpaytuvchilarni koʻpaytiring.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">200 ni 25% ga oshirish: 200 × 0,25 = 50</p>
  <p class="pe-fix__good">200 × 1,25 = 250</p>
  <p class="pe-fix__why">50 — bu faqat <b>qoʻshimcha</b>, yangi qiymat emas. Yangi qiymat
  uchun uni eskisiga qoʻshish kerak yoki darrov 1,25 ga koʻpaytirish.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 200 dan 250 ga oshdi. Necha foizga?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>25%.</b> Oʻzgarish 50; 50 ÷ 200 = 0,25.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 80 dan 60 ga tushdi. Necha foizga?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>25%.</b> Oʻzgarish 20; 20 ÷ 80 = 0,25. Asos — eski qiymat 80.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 1200 ni 25 foizga oshiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1500.</b> 1200 × 1,25 = 1500. Yoki 1200 + 300.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 45 000 ni 40 foizga kamaytiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>27 000.</b> Koʻpaytuvchi 0,6: 45 000 × 0,6 = 27 000.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Bekzodning jamgʻarmasi 400 000 soʻm edi. U yil davomida 20
  foizga koʻpaydi, keyin Bekzod undan 10 foizini sarfladi. Hozir qancha qolgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>432 000 soʻm.</b> 400 000 × 1,2 = 480 000; keyin 480 000 × 0,9 = 432 000.
    Ikkinchi foiz yangi summadan olindi. Koʻpaytuvchilar bilan: 1,2 × 0,9 = 1,08 —
    demak jami 8 foizga koʻpaygan.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Oʻzgarish</b><span>yangi va eski qiymat orasidagi farq; ingl. change</span></li>
  <li><b>Oʻzgarish foizi</b><span>farqning eski qiymatga nisbati; ingl. percentage
    change</span></li>
  <li><b>Asos</b><span>foiz olinayotgan qiymat, bu yerda — eskisi; ingl. base</span></li>
  <li><b>Koʻpaytuvchi</b><span>oʻzgarishni bir amalda beruvchi son, 1,2 yoki 0,8; ingl.
    multiplier</span></li>
  <li><b>Oshish</b><span>qiymatning koʻpayishi; ingl. increase</span></li>
  <li><b>Kamayish</b><span>qiymatning pasayishi; ingl. decrease</span></li>
  <li><b>Foiz punkti</b><span>ikki foiz orasidagi oddiy ayirma; ingl. percentage
    point</span></li>
  <li><b>Ketma-ket oʻzgarish</b><span>biridan keyin ikkinchisi qoʻllanadigan oʻzgarish;
    ingl. successive change</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Asos — eski qiymat.</b> Oʻzgarishni yangi songa boʻlish eng koʻp uchraydigan
      xato.</li>
    <li><b>Koʻpaytuvchi bilan bir amalda:</b> +15% → ×1,15, −20% → ×0,8.</li>
    <li><b>Foizlar qoʻshilmaydi.</b> Ketma-ket oʻzgarishda koʻpaytuvchilar koʻpaytiriladi:
      1,2 × 0,8 = 0,96.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-26 — chegirma, ustama va soliq
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-26: Chegirma, ustama va soliq — bozor matematikasi",
        "category": "math",
        "order": 26,
        "summary": (
            "Chegirma, ustama va QQS — uchalasi ham bitta amal, faqat nomi boshqa. "
            "Toʻlanadigan pulni bir koʻpaytuvchi bilan topish va reklamadagi «katta "
            "chegirma»ni tekshirish."
        ),
        "stories": ["«Katta chegirma!» — reklama ortidagi hisob"],
        "content": """
<h2>PM-26: Chegirma, ustama va soliq — bozor matematikasi</h2>

<p>Bozorda uch xil soʻz eshitasiz: <b>chegirma</b>, <b>ustama</b>, <b>soliq</b>. Uchtasi ham
qoʻrqinchli koʻrinadi, lekin ularning ortida bitta amal turibdi — oʻtgan darsda oʻrgangan
koʻpaytuvchi. Farqi faqat shundaki, biri narxni tushiradi, ikkitasi koʻtaradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>chegirmadan keyingi narxni bir amalda topasiz;</li>
    <li>tannarxga ustama qoʻshib sotuv narxini hisoblaysiz;</li>
    <li>QQS qoʻshilgan toʻlovni topasiz;</li>
    <li>ketma-ket ikki chegirmani tekshirasiz va reklamaga aldanmaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uchtasi ham bitta amal</span>
  <span class="pe-chip pe-chip--s">chegirma: × (1 − p/100)</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">ustama: × (1 + p/100)</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">soliq: × (1 + p/100)</span>
</div>

<h3>1. Chegirma — narxdan olinadi</h3>

<p><b>Chegirma</b> — sotuvchi narxdan voz kechgan ulush. 320 000 soʻmlik
kurtkaga 15 foiz chegirma boʻlsa, siz narxning 85 foizini toʻlaysiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Chegirma: 320 000 × 0,15 = 48 000</span>
    <span class="pm-solve__why">Uzun yoʻl — avval chegirmaning oʻzi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">320 000 − 48 000 = 272 000</span>
    <span class="pm-solve__why">Keyin uni narxdan ayiramiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">320 000 × 0,85 = 272 000</span>
    <span class="pm-solve__why">Qisqa yoʻl — bitta koʻpaytirish, bir xil javob</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Chegirma qancha?» va «Qancha toʻlayman?» — ikki boshqa savol</p>
  <p>Imtihonda ham, doʻkonda ham eng koʻp shu yerda adashishadi. 48 000 — chegirmaning
  <b>oʻzi</b>; 272 000 — <b>toʻlanadigan</b> pul. Savolni oxirigacha oʻqing va javobingiz
  qaysi biri ekanini bilib turing.</p>
</div>

<h3>2. Ustama — tannarxga qoʻshiladi</h3>

<p>Sotuvchi mahsulotni <b>tannarx</b>da oladi va ustiga oʻz foydasini
qoʻshadi. Bu qoʻshimcha <b>ustama</b> deyiladi. Tannarx 40 000 soʻm, ustama
25 foiz boʻlsa:</p>

<div class="pe-ex">
  <p class="pe-ex__math">40 000 × 1,25 = 50 000</p>
  <p class="pe-ex__uz">Qirq mingga yigirma besh foiz ustama qoʻyilsa, sotuv narxi ellik ming
  boʻladi.</p>
  <p class="pe-ex__why">Ustama <b>tannarxdan</b> hisoblanadi — sotuv narxidan emas.</p>
</div>

<h3>3. Soliq — narxning ustiga</h3>

<p>Doʻkondagi cheklarda <b>QQS</b> degan qatorni koʻrgansiz — bu qoʻshilgan qiymat soligʻi.
Oʻzbekistonda uning stavkasi hozir <b>12 foiz</b>. U ham narxning ustiga qoʻshiladi, yaʼni
ustama bilan bir xil amal.</p>

<div class="pe-ex">
  <p class="pe-ex__math">250 000 × 1,12 = 280 000</p>
  <p class="pe-ex__uz">Ikki yuz ellik ming soʻmlik mahsulot QQS bilan ikki yuz sakson ming
  soʻm boʻladi.</p>
  <p class="pe-ex__why">Soliqning oʻzi 30 000 soʻm: 250 000 × 0,12.</p>
</div>

<div class="pe-legend">
  <span><i class="pe-chip pe-chip--s"></i> koʻpaytuvchi 1 dan <b>kichik</b> — narx tushdi</span>
  <span><i class="pe-chip pe-chip--o"></i> koʻpaytuvchi 1 dan <b>katta</b> — narx koʻtarildi</span>
</div>

<h3>4. Ikki chegirma — qoʻshilmaydi</h3>

<p>«Avval 20 foiz, kassada yana 10 foiz chegirma!» Bu 30 foiz demakmi? Yoʻq — oʻtgan darsdagi
qoida bu yerda ham ishlaydi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">0,8 × 0,9 = 0,72</span>
    <span class="pm-solve__why">Koʻpaytuvchilarni koʻpaytiramiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">0,72 → narxning 72% i toʻlanadi</span>
    <span class="pm-solve__why">Demak jami chegirma 30% emas, 28%</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Ikkinchi chegirma kichikroq sondan olinadi</p>
  <p>Birinchi chegirmadan keyin narx allaqachon pasaygan, ikkinchi 10 foiz esa oʻsha pasaygan
  narxdan hisoblanadi. Shuning uchun natija har doim ikki foizning yigʻindisidan <b>kamroq</b>
  boʻladi.</p>
</div>

<h3>5. Teskari savol: chegirmadan oldingi narx</h3>

<p>Chekda «siz 36 000 soʻm toʻladingiz, chegirma 10 foiz» deb yozilgan. Eski narx qancha edi?
Bu PM-24 dagi «butunni topish» savolining oʻzi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Toʻlangan pul — eski narxning 90% i</span>
    <span class="pm-solve__why">10 foiz chegirma qilingan edi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">36 000 ÷ 0,9 = 40 000</span>
    <span class="pm-solve__why">Koʻpaytuvchiga boʻldik — eski narx 40 000 soʻm</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>40 000 × 0,9 = 36 000 ✓ Chegirma esa 4000 soʻm boʻlgan.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Karim aka doʻkonda kurtka sotadi.</b> Kurtkaning tannarxi 40 000 soʻm. U ustiga 25
foiz ustama qoʻyib narx belgiladi. Mavsum oxirida esa oʻsha narxdan 10 foiz chegirma eʼlon
qildi.</p>

<p><b>Savol:</b> xaridor necha soʻm toʻlaydi va Karim akaning bitta kurtkadan foydasi
qancha?</p>

<p><b>Reja:</b> ustama tannarxdan, chegirma esa belgilangan narxdan hisoblanadi. Foyda —
toʻlangan pul bilan tannarx orasidagi farq.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">40 000 × 1,25 = 50 000</span>
    <span class="pm-solve__why">Tannarxga 25 foiz ustama — sotuv narxi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">50 000 × 0,9 = 45 000</span>
    <span class="pm-solve__why">Chegirma belgilangan narxdan olinadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">45 000 − 40 000 = 5000</span>
    <span class="pm-solve__why">Xaridor 45 000 toʻlaydi, foyda 5000 soʻm</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Koʻpaytuvchilar orqali: 1,25 × 0,9 = 1,125, demak yakuniy narx tannarxning 112,5 foizi.
  40 000 × 1,125 = 45 000 ✓ Foyda tannarxning 12,5 foizi ekan — 25 foiz emas, chunki
  chegirma uni yeb qoʻydi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Ustama chegirmadan katta, demak yakuniy narx tannarxdan yuqori boʻlishi kerak.
  45 000 &gt; 40 000 — mos.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">50 000 ga 20% chegirma → narx 10 000 soʻm</p>
  <p class="pe-fix__good">Chegirma 10 000, narx esa 40 000 soʻm</p>
  <p class="pe-fix__why">Chegirmaning oʻzi javob deb olingan. Toʻlanadigan pul uchun uni
  narxdan ayirish kerak — yoki darrov 0,8 ga koʻpaytirish.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">25% chegirma, keyin yana 25% chegirma = 50% chegirma</p>
  <p class="pe-fix__good">0,75 × 0,75 = 0,5625 → jami 43,75% chegirma</p>
  <p class="pe-fix__why">Foizlar qoʻshilmaydi. Ikkinchi chegirma allaqachon pasaygan narxdan
  olinadi, shuning uchun natija yarmiga yetmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Tannarx 80 000, ustama 20%: 80 000 × 0,2 = 16 000 — sotuv narxi</p>
  <p class="pe-fix__good">80 000 × 1,2 = 96 000 — sotuv narxi</p>
  <p class="pe-fix__why">16 000 — ustamaning oʻzi. Sotuv narxi tannarx <b>plyus</b> ustama.
  Nazorat: sotuv narxi tannarxdan kichik boʻlishi mumkin emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 80 000 soʻmlik mahsulotga 25 foiz chegirma. Qancha toʻlanadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>60 000 soʻm.</b> 80 000 × 0,75 = 60 000. Chegirmaning oʻzi 20 000.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 150 000 soʻmlik xizmatga 12 foiz QQS qoʻshiladi. Chek qancha
  boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>168 000 soʻm.</b> 150 000 × 1,12 = 168 000. Soliqning oʻzi 18 000 soʻm.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Tannarx 60 000, ustama 30 foiz. Sotuv narxi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>78 000 soʻm.</b> 60 000 × 1,3 = 78 000.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Avval 20 foiz, keyin 10 foiz chegirma qilindi. Jami necha foiz
  chegirma boʻldi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>28 foiz.</b> 0,8 × 0,9 = 0,72, yaʼni narxning 72 foizi toʻlanadi. 100 − 72 = 28.
    30 foiz emas!</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Dilnoza 25 foiz chegirma bilan kitob oldi va 45 000 soʻm toʻladi.
  Kitobning chegirmasiz narxi qancha edi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>60 000 soʻm.</b> Toʻlangan pul eski narxning 75 foizi: 45 000 ÷ 0,75 = 60 000.
    Tekshirish: 60 000 × 0,75 = 45 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Chegirma</b><span>narxdan tushiriladigan ulush; ingl. discount</span></li>
  <li><b>Ustama</b><span>tannarx ustiga qoʻshiladigan foyda; ingl. markup</span></li>
  <li><b>Tannarx</b><span>mahsulot sotuvchiga tushgan narx; ingl. cost price</span></li>
  <li><b>Sotuv narxi</b><span>xaridorga eʼlon qilingan narx; ingl. selling price</span></li>
  <li><b>QQS</b><span>qoʻshilgan qiymat soligʻi, narx ustiga qoʻshiladi; ingl. VAT</span></li>
  <li><b>Foyda</b><span>sotuvdan qolgan ortiqcha pul; ingl. profit</span></li>
  <li><b>Koʻpaytuvchi</b><span>narxni bir amalda oʻzgartiruvchi son; ingl. multiplier</span></li>
  <li><b>Yakuniy narx</b><span>hamma oʻzgarishdan keyingi toʻlov; ingl. final price</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Chegirma ×(1 − p), ustama va soliq ×(1 + p).</b> Uchtasi ham bitta amal.</li>
    <li><b>Ustama tannarxdan, chegirma sotuv narxidan</b> hisoblanadi — asosni adashtirmang.</li>
    <li><b>Ketma-ket chegirmalar qoʻshilmaydi:</b> 20% va 10% birgalikda 28% beradi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-27 — nisbat
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-27: Nisbat va miqdorni nisbat boʻyicha boʻlish",
        "category": "math",
        "order": 27,
        "summary": (
            "Nisbat nima va u kasrdan nimasi bilan farq qiladi. Nisbatni "
            "qisqartirish hamda miqdorni 3:4:5 kabi nisbatlarda «bir qism» usuli "
            "bilan adolatli boʻlish."
        ),
        "stories": ["Uch doʻst va bir savat olma"],
        "content": """
<h2>PM-27: Nisbat va miqdorni nisbat boʻyicha boʻlish</h2>

<p>Buvijon xamir qorayotganda oʻlchov idishini olmaydi. U shunday deydi: «Har besh kosa unga
ikki kosa suv». Un koʻp boʻlsa, suv ham koʻpayadi; kam boʻlsa, birga kamayadi. Muhimi —
<b>ular orasidagi munosabat</b>. Bu munosabatning nomi <b>nisbat</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>nisbatni oʻqiysiz va yozasiz: 5:2;</li>
    <li>nisbatni qisqartirasiz va teng nisbatlarni topasiz;</li>
    <li>miqdorni berilgan nisbatda boʻlasiz;</li>
    <li>nisbat va kasrni bir-biridan ajratasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Miqdorni nisbatda boʻlish</span>
  <span class="pe-chip pe-chip--v">qismlar soni = a + b</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">bir qism = miqdor ÷ qismlar soni</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">har biri = bir qism × oʻz soni</span>
</div>

<h3>1. Nisbat nima</h3>

<p>Sinfda 12 ta oʻgʻil va 18 ta qiz bor. Ularning soni <b>12 : 18</b> nisbatda deymiz va
«oʻn ikkiga oʻn sakkiz» deb oʻqiymiz. Nisbatni ham xuddi kasr kabi qisqartirsa boʻladi —
ikkala sonni bir xil songa boʻlamiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 : 18</span>
    <span class="pm-solve__why">Berilgan nisbat</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 ÷ 6 = 2, 18 ÷ 6 = 3</span>
    <span class="pm-solve__why">EKUB 6 ga boʻldik (PM-8)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2 : 3</span>
    <span class="pm-solve__why">Har ikki oʻgʻilga uch qiz — eng sodda koʻrinish</span>
  </div>
</div>

<p>2:3 va 12:18 — <b>bir xil nisbat</b>. Sinfdagi bolalar soni oʻzgarmadi, faqat munosabat
sodda tilda aytildi.</p>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Nisbat — qismlar orasida, kasr — butunga nisbatan</p>
  <p>Bu darsning eng muhim jumlasi. <b>2:3</b> degani birinchi qism butunning 2/3 qismi
  degani <b>emas</b>! Butun bu yerda 2 + 3 = 5 ta qismdan iborat, shuning uchun birinchisi
  butunning <b>2/5</b> qismi. Nisbatda sonlar bir-biri bilan, kasrda esa butun bilan
  taqqoslanadi.</p>
</div>

<h3>2. Miqdorni nisbatda boʻlish — «bir qism» usuli</h3>

<p>Endi asosiy koʻnikma. <b>60 ta daftarni 1:3 nisbatda ikki sinfga boʻlish</b> kerak. Uch
qadamda ishlaymiz.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">1-sinf</span>
    <span class="pm-model__bar" style="width:25%">1 qism</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">2-sinf</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:75%">3 qism</span>
  </div>
  <p class="pm-model__tot">Jami 4 ta teng qism = 60 ta daftar</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 + 3 = 4</span>
    <span class="pm-solve__why">Jami nechta teng qism borligini sanadik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 ÷ 4 = 15</span>
    <span class="pm-solve__why">Bitta qism nechtaga tengligini topdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">15 va 15 × 3 = 45</span>
    <span class="pm-solve__why">Birinchi sinfga 15 ta, ikkinchisiga 45 ta daftar</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>15 + 45 = 60 ✓ qismlar butunni toʻldirdi. Va 15 : 45 = 1 : 3 ✓ nisbat saqlanib qoldi.
  <b>Har doim shu ikki nazoratni qiling</b> — ular deyarli hamma xatoni tutadi.</p>
</div>

<h3>3. Uch va undan koʻp qismli nisbat</h3>

<p>Usul umuman oʻzgarmaydi. <b>96 ta olmani 3:4:5 nisbatda</b> uch bolaga boʻlamiz:</p>

<div class="pe-ex">
  <p class="pe-ex__math">3 + 4 + 5 = 12; 96 ÷ 12 = 8</p>
  <p class="pe-ex__uz">Jami oʻn ikki qism, bitta qism sakkizta olma.</p>
  <p class="pe-ex__why">Endi har biriga: 8 × 3 = 24, 8 × 4 = 32, 8 × 5 = 40.</p>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>24 + 32 + 40 = 96 ✓ Va nisbat: 24 : 32 : 40 ni 8 ga qisqartirsak — 3 : 4 : 5 ✓</p>
</div>

<h3>4. Nisbat qurilishda va oshxonada</h3>

<p>Nisbat eng koʻp aralashmalarda ishlatiladi, chunki u miqdorga emas, <b>tarkibga</b>
tegishli. Sement va qum 1:3 nisbatda aralashtirilsa, 24 kg aralashmada nechadan
boʻladi?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 + 3 = 4 qism</span>
    <span class="pm-solve__why">Aralashma toʻrt qismdan iborat</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">24 ÷ 4 = 6 kg</span>
    <span class="pm-solve__why">Bitta qism</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6 kg sement, 18 kg qum</span>
    <span class="pm-solve__why">Sement aralashmaning 1/4 qismi, 1/3 emas!</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Nisbatni foizga aylantirsa ham boʻladi</p>
  <p>1:3 nisbatda sement — 1/4, yaʼni <b>25%</b>, qum esa 3/4, yaʼni <b>75%</b>. PM-22 dagi
  uch qiyofa shu yerda ham ish beradi: nisbat → kasr → foiz.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Uch doʻst — Afsona, Jasur va Sherbek — bogʻda olma terishdi.</b> Ular ishni birga
qilishdi, lekin har xil vaqt ishladi: Afsona 3 soat, Jasur 4 soat, Sherbek 5 soat. Olmani
sotib, jami <b>96 000 soʻm</b> olishdi va pulni ishlagan vaqtlariga qarab boʻlishga kelishdi.</p>

<p><b>Savol:</b> har biri necha soʻm oladi?</p>

<p><b>Reja:</b> vaqtlar nisbati 3:4:5. Demak pulni ham shu nisbatda boʻlamiz — «bir qism»
usuli bilan.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3 + 4 + 5 = 12</span>
    <span class="pm-solve__why">Jami 12 ta teng qism</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">96 000 ÷ 12 = 8000</span>
    <span class="pm-solve__why">Bir soatlik ish — bitta qism — 8000 soʻm</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">24 000 · 32 000 · 40 000</span>
    <span class="pm-solve__why">8000 ni 3, 4 va 5 ga koʻpaytirdik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>24 000 + 32 000 + 40 000 = 96 000 ✓ Va nisbat 24 : 32 : 40 = 3 : 4 : 5 ✓ Sherbek eng
  koʻp ishladi va eng koʻp oldi — javob adolatli koʻrinadi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Uch kishiga teng boʻlinganda har biriga 32 000 dan tushardi. Afsona kamroq
  ishlagani uchun undan kam, Sherbek esa koʻproq olishi kerak. Javoblar shu tartibda.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">40 ni 3:5 nisbatda boʻlish: 40 ÷ 3 = 13,3 va 40 ÷ 5 = 8</p>
  <p class="pe-fix__good">40 ÷ 8 = 5; 15 va 25</p>
  <p class="pe-fix__why">Miqdor nisbatdagi sonlarga alohida boʻlingan. Avval <b>qismlar
  soni</b>ni topish kerak: 3 + 5 = 8. Nazorat: 13,3 + 8 = 40 boʻlmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">2:3 nisbatda birinchi qism butunning 2/3 i</p>
  <p class="pe-fix__good">Birinchi qism butunning 2/5 i</p>
  <p class="pe-fix__why">Nisbatdagi sonlar bir-biri bilan taqqoslanadi. Butun esa 2 + 3 = 5
  ta qismdan iborat, shuning uchun maxraj — 5.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Sement va qum 1:3 → sement aralashmaning uchdan biri</p>
  <p class="pe-fix__good">Sement aralashmaning toʻrtdan biri</p>
  <p class="pe-fix__why">«Bir qism sementga uch qism qum» degani jami toʻrt qism. Qurilishda
  bu xato devorni buzadi, imtihonda esa ballni.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 15 : 20 nisbatini qisqartiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 : 4.</b> Ikkalasini EKUB 5 ga boʻldik.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 120 ni 2:3 nisbatda boʻling.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>48 va 72.</b> Qismlar 2 + 3 = 5; bir qism 120 ÷ 5 = 24; 24 × 2 = 48,
    24 × 3 = 72. Tekshirish: 48 + 72 = 120 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 2:3 nisbatda ikkinchi qism butunning qanchasi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3/5 qismi.</b> Jami qismlar 5 ta, ikkinchisiga ulardan 3 tasi tegadi. Foizda —
    60%.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Nisbat 5:2. Kichik qism 8 ta boʻlsa, katta qism nechta?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>20 ta.</b> Kichik qism 2 ta ulushga toʻgʻri keladi: 8 ÷ 2 = 4 — bitta ulush.
    Katta qism 5 ulush: 4 × 5 = 20.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Buvijon xamirni un va suvdan 5:2 nisbatda qoradi. Jami 700 gramm
  aralashma kerak boʻlsa, necha gramm un olishi kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>500 gramm.</b> Qismlar 5 + 2 = 7; bir qism 700 ÷ 7 = 100 g. Un 5 qism: 500 g,
    suv 2 qism: 200 g. Tekshirish: 500 + 200 = 700 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Nisbat</b><span>ikki yoki undan koʻp miqdor orasidagi munosabat, a:b; ingl.
    ratio</span></li>
  <li><b>Qism (ulush)</b><span>nisbatdagi bitta teng boʻlak; ingl. part</span></li>
  <li><b>Qismlar soni</b><span>nisbatdagi sonlar yigʻindisi; ingl. total parts</span></li>
  <li><b>Teng nisbat</b><span>qisqartirilganda bir xil boʻladigan nisbatlar; ingl.
    equivalent ratio</span></li>
  <li><b>Sodda koʻrinish</b><span>toʻliq qisqartirilgan nisbat; ingl. simplest form</span></li>
  <li><b>Aralashma</b><span>bir necha moddaning nisbatda qoʻshilishi; ingl. mixture</span></li>
  <li><b>EKUB</b><span>eng katta umumiy boʻluvchi, qisqartirishda kerak; ingl. GCD</span></li>
  <li><b>Adolatli boʻlish</b><span>hissaga qarab taqsimlash; ingl. fair share</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Nisbat qismlarni oʻzaro</b>, kasr esa butunga nisbatan taqqoslaydi: 2:3 da
      birinchisi butunning 2/5 i.</li>
    <li><b>«Bir qism» usuli:</b> qismlarni qoʻshing, miqdorni shunga boʻling, keyin har
      birini oʻz soniga koʻpaytiring.</li>
    <li><b>Ikki nazorat:</b> qismlar yigʻindisi butunga teng boʻlsin va javoblar nisbati
      berilganidek qisqarsin.</li>
  </ul>
</div>
""",
    },
]
