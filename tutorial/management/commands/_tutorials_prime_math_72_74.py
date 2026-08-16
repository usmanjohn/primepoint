# -*- coding: utf-8 -*-
"""Prime Math — darslar 72–74 (oʻxshashlik va masshtab, simmetriya, hajm).

Blok E: Geometriya — YAKUNLOVCHI uchlik (57–74).
Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

  mashqlar — practice/management/commands/_practice_pm_72_74.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_72_74.py

⚠️ Chizmalar QOʻLDA hisoblanmagan: _svgkit.py + scratchpad/gen_pm72_74.py
   bilan generatsiya qilingan va qlmanage bilan koʻz bilan tekshirilgan.
   verify_pm_72_74.py ularni qaytadan oʻlchaydi (oʻxshash uchburchaklarning
   burchagi haqiqatan bir xilmi, soya chizmasida ikkala nisbat 0,75 mi,
   yoyilmaning oltita yogʻi 94 sm² beradimi).

⚠️ Kumulyativ chegaralar:
  • PM-72 — oʻxshashlik va masshtab. Masshtab PM-28 da kirgan, shuning
    uchun bu yerda u kengaytiriladi. Yuza k² marta oʻsishi PM-71 dagi
    «radius 2 marta → yuza 4 marta» ning umumlashmasi. ⛔ Hajm k³ —
    yoʻq, chunki hajm PM-74 da;
  • PM-73 — simmetriya va harakatlar. Koordinatalar PM-45 dan.
    ⛔ Hajm ham, silindr ham yoʻq;
  • PM-74 — hajm va sirt yuzasi. Silindr hajmi PM-71 ga tayanadi
    (asos yuzasi π × r²). ⛔ Konus, shar va piramida hajmi YOʻQ —
    ular maktab kursida keyinroq.
  • ⛔ Statistika (PM-75…) va matnli masala usullari (PM-85…) YOʻQ.
  • Faol ishlatiladi: uchburchak burchaklari 180° (PM-61); yuza
    (PM-68/69); doira yuzasi (PM-71); koordinata (PM-45); nisbat va
    proporsiya (PM-27); masshtab (PM-28); oʻnlik kasr (PM-20/21);
    daraja (PM-12); yaxlitlash (PM-14).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_72_74.py --author=prime
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
    # PM-72 — oʻxshashlik va masshtab
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-72: Oʻxshashlik va masshtab: kichik chizma, katta dunyo",
        "category": "math",
        "order": 72,
        "summary": (
            "Xarita, reja va fotosurat — hammasi bitta gʻoyaga tayanadi: shakl "
            "oʻsha, oʻlcham boshqa. Oʻxshash uchburchaklar bilan minorani "
            "oʻlchashni va masshtab bilan ishlashni oʻrganasiz."
        ),
        "stories": ["Soya bilan minorani oʻlchash — Fales usuli"],
        "content": """
<h2>PM-72: Oʻxshashlik va masshtab: kichik chizma, katta dunyo</h2>

<p>Xaritada Toshkent bir necha santimetr. Fotosuratda maktabingiz kaftga
sigʻadi. Oʻyinchoq mashina esa haqiqiysining aynan kichraytirilgan
nusxasi.</p>

<p>Hammasida bitta gʻoya ishlaydi: <b>shakl oʻsha, oʻlcham boshqa</b>. Shu
gʻoya bilan qoʻlingizni ham tekkiza olmaydigan minoraning balandligini
oʻlchash mumkin.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>oʻxshash shakllarni tanib, oʻxshashlik koeffitsientini
      topasiz;</li>
    <li>ikkita burchagi teng uchburchaklar oʻxshash ekanini
      ishlatasiz;</li>
    <li>soya orqali daraxt yoki bino balandligini hisoblaysiz;</li>
    <li>masshtabni ikki tomonga — chizmadan hayotga va aksincha —
      oʻgirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻxshash shakllarda</span>
  <span class="pe-chip pe-chip--o">burchaklar</span>
  <span class="pe-op">teng,</span>
  <span class="pe-chip pe-chip--o">tomonlar</span>
  <span class="pe-op">esa</span>
  <span class="pe-chip pe-chip--s">k</span>
  <span class="pe-op">marta farq qiladi</span>
</div>

<h3>1. Oʻxshash shakl nima</h3>

<p>Ikki shakl <b>oʻxshash</b> deyiladi, agar biri ikkinchisining aniq
kattalashtirilgan (yoki kichraytirilgan) nusxasi boʻlsa. Bunda
<b>burchaklar oʻzgarmaydi</b>, tomonlar esa hammasi <b>bir xil marta</b>
oʻzgaradi. Oʻsha «bir xil marta» — <b>oʻxshashlik koeffitsienti</b>,
k harfi bilan belgilanadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="Ikkita oʻxshash uchburchak: 3-4-5 va 9-12-15">
    <polygon class="pm-fill" points="20,180 64,180 20,147"/>
    <polyline class="pm-ln" points="20,180 64,180 20,147 20,180" fill="none"/>
    <polyline class="pm-ln" points="20,171 29,171 29,180" fill="none"/>
    <path class="pm-ln" d="M 51.2 170.4 A 16 16 0 0 0 48 180" fill="none"/>
    <text class="pm-lbl" x="4" y="168">3</text>
    <text class="pm-lbl" x="34" y="197">4</text>
    <text class="pm-lbl" x="48" y="158">5</text>
    <polygon class="pm-fill pm-fill--hl" points="112,180 244,180 112,81"/>
    <polyline class="pm-ln" points="112,180 244,180 112,81 112,180" fill="none"/>
    <polyline class="pm-ln" points="112,167 125,167 125,180" fill="none"/>
    <path class="pm-ln" d="M 216.8 159.6 A 34 34 0 0 0 210 180" fill="none"/>
    <text class="pm-lbl" x="96" y="135">9</text>
    <text class="pm-lbl" x="168" y="197">12</text>
    <text class="pm-lbl" x="190" y="118">15</text>
    <text class="pm-lbl pm-lbl--hl" x="60" y="40">k = 3</text>
  </svg>
  <figcaption>Burchaklari bir xil, tomonlari esa har biri roppa-rosa
  3 marta katta. Demak bu ikki uchburchak oʻxshash.</figcaption>
</figure>

<p>Tekshiramiz — <b>mos tomonlar</b>ni bir-biriga boʻlamiz:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">9 ÷ 3 = 3</span>
    <span class="pm-solve__why">Kichik katetlar</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 ÷ 4 = 3</span>
    <span class="pm-solve__why">Katta katetlar</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">15 ÷ 5 = 3 → k = 3</span>
    <span class="pm-solve__why">Uchalasi ham bir xil — demak
    oʻxshash</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Teng» va «oʻxshash» — bir narsa emas</p>
  <p><b>Teng</b> shakllar bir-biriga toʻliq ustma-ust tushadi: ham
  shakli, ham oʻlchami bir xil. <b>Oʻxshash</b> shakllarda esa faqat
  shakl bir xil, oʻlcham har xil boʻlishi mumkin. Teng shakllar —
  oʻxshashlikning k = 1 boʻlgan xususiy holati.</p>
</div>

<h3>2. Uchburchaklar uchun ikkita burchak yetarli</h3>

<p>Umuman olganda oʻxshashlikni tekshirish uchun hamma tomonni oʻlchash
kerak. Lekin uchburchakda ancha oson yoʻl bor.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Ikki burchak qoidasi</p>
  <p>Agar bir uchburchakning ikkita burchagi ikkinchisining ikkita
  burchagiga teng boʻlsa, bu uchburchaklar <b>oʻxshash</b>.</p>
</div>

<p>Nega ikkitasi yetarli? Chunki uchburchakda burchaklar yigʻindisi
180° (PM-61). Ikkitasi mos tushsa, uchinchisi oʻz-oʻzidan mos tushadi —
uni tekshirishning hojati yoʻq.</p>

<div class="pe-ex">
  <p class="pe-ex__math">90° va 37° ↔ 90° va 37° → oʻxshash</p>
  <p class="pe-ex__uz">Ikkala uchburchakda ham toʻgʻri burchak va 37
  gradusli burchak bor, demak ular oʻxshash.</p>
  <p class="pe-ex__why">Uchinchi burchak ikkalasida ham
  180 − 90 − 37 = 53°.</p>
</div>

<h3>3. Soya usuli: minoraga tegmasdan uni oʻlchash</h3>

<p>Quyosh juda uzoqda, shuning uchun uning nurlari yerga <b>parallel</b>
tushadi (PM-60). Demak bir vaqtning oʻzida oʻlchangan hamma soya bir xil
burchak ostida tushadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="Odam va daraxtning soyasi ikkita oʻxshash uchburchak yasaydi">
    <line class="pm-ln" x1="20" y1="175" x2="290" y2="175"/>
    <line class="pm-ln pm-ln--hl" x1="45" y1="175" x2="45" y2="157"/>
    <line class="pm-ln pm-ln--hl" x1="45" y1="175" x2="69" y2="175"/>
    <line class="pm-ln pm-ln--dash" x1="45" y1="157" x2="69" y2="175"/>
    <polyline class="pm-ln" points="45,167 53,167 53,175" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="120" y1="175" x2="120" y2="67"/>
    <ellipse class="pm-fill--hl" cx="120" cy="58" rx="30" ry="21"/>
    <ellipse class="pm-ln" cx="120" cy="58" rx="30" ry="21" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="120" y1="175" x2="264" y2="175"/>
    <line class="pm-ln pm-ln--dash" x1="120" y1="67" x2="264" y2="175"/>
    <polyline class="pm-ln" points="120,167 128,167 128,175" fill="none"/>
    <text class="pm-lbl" x="8" y="170">1,5 m</text>
    <text class="pm-lbl" x="47" y="191">2 m</text>
    <text class="pm-lbl pm-lbl--hl" x="126" y="125">h = ?</text>
    <text class="pm-lbl" x="178" y="191">12 m</text>
    <text class="pm-lbl" x="206" y="112">quyosh nuri</text>
  </svg>
  <figcaption>Odam va uning soyasi bitta uchburchak, daraxt va uning
  soyasi ikkinchisi. Nurlar parallel boʻlgani uchun ular oʻxshash.</figcaption>
</figure>

<p>Ikkala uchburchakda ham toʻgʻri burchak bor (narsa yerga tik turibdi)
va quyosh nuri bilan yer orasidagi burchak bir xil. Ikkita burchak mos
tushdi — demak uchburchaklar oʻxshash.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1,5 ÷ 2 = 0,75</span>
    <span class="pm-solve__why">Odamning boʻyi soyasining necha
    ulushi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">h ÷ 12 = 0,75</span>
    <span class="pm-solve__why">Daraxtda ham xuddi shu nisbat</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">h = 12 × 0,75 = 9 m</span>
    <span class="pm-solve__why">Daraxtning balandligi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>9 ÷ 12 = 0,75 va 1,5 ÷ 2 = 0,75 ✓ — nisbatlar bir xil.
  <br>Daraxt odamdan 6 marta baland, soyasi ham 6 marta uzun
  (12 ÷ 2 = 6) ✓</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Nisbatni toʻgʻri tomonga yozing</p>
  <p>«Boʻy ÷ soya» ikkala shaklda ham bir xil chiqadi. Agar birida
  boʻyni soyaga, ikkinchisida soyani boʻyga boʻlsangiz, javob teskari
  chiqadi. Yozib qoʻying: <b>oʻxshash narsalarning bir xil nomli
  tomonlari bir xil nomlisi bilan</b> taqqoslanadi.</p>
</div>

<h3>4. Masshtab</h3>

<p><b>Masshtab</b> — chizmadagi uzunlik haqiqiy uzunlikdan necha marta
kichik ekanini koʻrsatadi (PM-28). <b>M 1 : 50</b> degani: chizmadagi
1 santimetr hayotdagi 50 santimetr.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="Sinf xonasining 1:50 masshtabdagi chizmasi">
    <rect class="pm-fill" x="72" y="34" width="162" height="108"/>
    <rect class="pm-ln" x="72" y="34" width="162" height="108" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="123" y="22">18 sm</text>
    <text class="pm-lbl pm-lbl--hl" x="12" y="92">12 sm</text>
    <text class="pm-lbl" x="101" y="84">sinf xonasi</text>
    <text class="pm-lbl" x="107" y="104">9 m × 6 m</text>
    <text class="pm-lbl pm-lbl--hl" x="119" y="168">M 1 : 50</text>
  </svg>
  <figcaption>9 m × 6 m boʻlgan sinf 1:50 masshtabda 18 sm × 12 sm
  boʻlib chiziladi.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">9 m = 900 sm</span>
    <span class="pm-solve__why">Avval bitta birlikka oʻtdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">900 ÷ 50 = 18 sm</span>
    <span class="pm-solve__why">Chizmaga tushadigan uzunlik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">600 ÷ 50 = 12 sm</span>
    <span class="pm-solve__why">Xuddi shunday, eni</span>
  </div>
</div>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Masshtab</th><th>Chizmadagi 1 sm</th><th>Qayerda ishlatiladi</th></tr>
  <tr><td>1 : 50</td><td class="pm-word__sym">50 sm</td>
    <td>xona rejasi</td></tr>
  <tr><td>1 : 100</td><td class="pm-word__sym">1 m</td>
    <td>uy rejasi</td></tr>
  <tr><td>1 : 50 000</td><td class="pm-word__sym">500 m</td>
    <td>shahar xaritasi</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__math">7 × 50 000 = 350 000 sm = 3,5 km</p>
  <p class="pe-ex__uz">1 : 50 000 masshtabli xaritada 7 santimetr —
  hayotda 3,5 kilometr.</p>
  <p class="pe-ex__why">350 000 sm = 3500 m = 3,5 km. Birliklarni
  bosqichma-bosqich oʻgiring, birdan sakramang.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">1 : 50 — bu «50 marta katta» emas</p>
  <p>Chapdagi 1 — <b>chizma</b>, oʻngdagi 50 — <b>hayot</b>. Yaʼni chizma
  50 marta <b>kichik</b>. Chizmadan hayotga oʻtayotganda
  <b>koʻpaytiriladi</b>, hayotdan chizmaga oʻtayotganda
  <b>boʻlinadi</b>. Adashsangiz, sinf xonangiz 450 metr chiqib
  qoladi.</p>
</div>

<h3>5. Yuza esa k marta emas, k<sup>2</sup> marta oʻsadi</h3>

<p>Bu yerda deyarli hamma adashadi. Tomonlar 3 marta oshsa, yuza
<b>9 marta</b> oshadi — chunki yuzada ikkita oʻlcham ham koʻpayadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Kichik: 2 sm × 3 sm</p>
    <p>S = 6 sm<sup>2</sup></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Katta: 6 sm × 9 sm</p>
    <p>S = 54 sm<sup>2</sup></p>
  </div>
</div>

<p>Tomonlar k = 3 marta oshdi, yuza esa 54 ÷ 6 = <b>9 marta</b>, yaʼni
3<sup>2</sup> marta. Xuddi shu qoidani PM-71 da doirada koʻrgan edik:
radius 2 marta oshganda yuza 4 marta oshgan edi.</p>

<h3>Matnli masala</h3>

<p>Bekzod sinf xonasining rejasini chizmoqchi. Xona 9 metr uzunlikda va
6 metr enda. Uning qoʻlida A4 qogʻoz bor: 21 sm × 29,7 sm.</p>

<p><b>1 : 50 masshtabda reja qogʻozga sigʻadimi? 1 : 25 masshtabda-chi?</b></p>

<p><b>Reja:</b> har bir masshtab uchun chizmaning oʻlchamini topamiz va
qogʻoz bilan solishtiramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">900 ÷ 50 = 18 sm; 600 ÷ 50 = 12 sm</span>
    <span class="pm-solve__why">1 : 50 masshtabdagi chizma</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">18 &lt; 29,7 va 12 &lt; 21 → sigʻadi</span>
    <span class="pm-solve__why">Qogʻozni koʻndalang qoʻyib</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">900 ÷ 25 = 36 sm; 600 ÷ 25 = 24 sm</span>
    <span class="pm-solve__why">1 : 25 masshtabdagi chizma</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">36 &gt; 29,7 → sigʻmaydi</span>
    <span class="pm-solve__why">Qogʻozning eng uzun tomoni ham
    yetmaydi</span>
  </div>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Masshtab ikki marta yiriklashsa (50 dan 25 ga), chizma ikki marta
  kattalashadi. 18 sm dan 36 sm ga — A4 dan chiqib ketishi
  kutilgan edi.</span>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>18 × 50 = 900 sm = 9 m ✓ va 12 × 50 = 600 sm = 6 m ✓
  <br><b>Javob:</b> 1 : 50 da sigʻadi, 1 : 25 da sigʻmaydi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">1 : 50 masshtab → chizmadagi 18 sm hayotda
  18 ÷ 50 = 0,36 sm</p>
  <p class="pe-fix__good">18 × 50 = 900 sm = 9 m</p>
  <p class="pe-fix__why">Chizmadan hayotga oʻtishda koʻpaytiriladi.
  Yoʻnalishni har doim tekshiring: hayotdagi son <b>kattaroq</b>
  boʻlishi kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Soya: h = 1,5 × 2 ÷ 12 = 0,25 m</p>
  <p class="pe-fix__good">h = 1,5 × 12 ÷ 2 = 9 m</p>
  <p class="pe-fix__why">Nisbat teskari yozilgan. Daraxt odamdan baland,
  demak javob 1,5 dan katta chiqishi shart. 0,25 m — bir qarichgina
  daraxt.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Tomonlar 3 marta oshdi → yuza ham 3 marta
  oshadi</p>
  <p class="pe-fix__good">Yuza 3<sup>2</sup> = 9 marta oshadi</p>
  <p class="pe-fix__why">Yuzada ikkita oʻlcham bor va ikkalasi ham 3
  marta oshadi: 3 × 3 = 9. Chizib koʻring — katta toʻrtburchakka
  kichigidan roppa-rosa toʻqqiztasi sigʻadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Oʻxshashlik: 9 ÷ 3 = 3, lekin 12 ÷ 5 = 2,4 —
  baribir oʻxshash</p>
  <p class="pe-fix__good">Mos tomonlar notoʻgʻri juftlangan</p>
  <p class="pe-fix__why">4 ga 12, 5 ga 15 mos keladi — eng kichik eng
  kichigiga, eng kattasi eng kattasiga. Juftlashni chalkashtirsangiz,
  koeffitsient har xil chiqadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Oʻxshash uchburchaklarning kichigida tomonlar
  4 sm va 6 sm. Kattasida 4 sm ga mos tomon 12 sm. Ikkinchi tomoni
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>18 sm.</b> Avval koeffitsient: k = 12 ÷ 4 = 3. Keyin ikkinchi
    tomon: 6 × 3 = 18 sm.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Oʻxshashlik koeffitsienti k = 2,5. Kichik
  shaklning tomoni 6 sm boʻlsa, kattasiniki qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>15 sm.</b> 6 × 2,5 = 15.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 1 : 100 masshtabli rejada devor 7 sm. Haqiqiy
  uzunligi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>7 m.</b> 7 × 100 = 700 sm = 7 m.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 1 : 50 000 masshtabli xaritada ikki qishloq
  orasi 4 sm. Haqiqiy masofa necha kilometr?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2 km.</b> 4 × 50 000 = 200 000 sm = 2000 m = 2 km.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Ustun 2 m, soyasi 3 m. Shu payt binoning
  soyasi 24 m. Bino necha metr?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>16 m.</b> Nisbat: 2 ÷ 3. Demak h = 24 × 2 ÷ 3 = 48 ÷ 3 = 16 m.
    Tekshirish: 16 ÷ 24 = 0,666… va 2 ÷ 3 = 0,666… ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Afsonaning surati 8 sm × 12 sm. U suratni
  kattalashtirdi va uzun tomoni 30 sm boʻldi. Qisqa tomoni qancha
  boʻladi va yuzasi necha marta oshadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>20 sm, yuzasi 6,25 marta oshadi.</b> Koeffitsient:
    k = 30 ÷ 12 = 2,5. Qisqa tomon: 8 × 2,5 = 20 sm. Yuzalar:
    8 × 12 = 96 sm<sup>2</sup> va 20 × 30 = 600 sm<sup>2</sup>;
    600 ÷ 96 = 6,25 — bu aynan 2,5<sup>2</sup>.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Oʻxshash shakllar</b><span>shakli bir xil, oʻlchami har xil
    shakllar; ingl. similar figures</span></li>
  <li><b>Oʻxshashlik koeffitsienti</b><span>tomonlar necha marta farq
    qilishi, k; ingl. scale factor</span></li>
  <li><b>Mos tomonlar</b><span>bir shakldagi tomonga ikkinchisidagi
    oʻrni bir xil tomon; ingl. corresponding sides</span></li>
  <li><b>Mos burchaklar</b><span>oʻxshash shakllardagi teng burchaklar;
    ingl. corresponding angles</span></li>
  <li><b>Teng shakllar</b><span>ham shakli, ham oʻlchami bir xil
    shakllar; ingl. congruent figures</span></li>
  <li><b>Masshtab</b><span>chizma va haqiqat orasidagi nisbat; ingl.
    scale</span></li>
  <li><b>Reja</b><span>yuqoridan koʻrinishdagi masshtabli chizma; ingl.
    plan</span></li>
  <li><b>Nisbat</b><span>ikki sonning bir-biriga boʻlinmasi; ingl.
    ratio</span></li>
  <li><b>Proporsiya</b><span>ikki nisbatning tengligi; ingl.
    proportion</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Oʻxshash shakllarda burchaklar teng, tomonlar k marta farq
      qiladi.</li>
    <li>Uchburchaklar uchun ikkita teng burchak yetarli.</li>
    <li>Soya usuli: boʻy ÷ soya ikkala narsada ham bir xil.</li>
    <li>M 1 : 50 — chizma 50 marta kichik. Chizmadan hayotga
      koʻpaytiring, hayotdan chizmaga boʻling.</li>
    <li>Tomonlar k marta oshsa, yuza k<sup>2</sup> marta oshadi.</li>
    <li>Javobni har doim mantiqqa solib koʻring: daraxt odamdan baland
      chiqishi kerak.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-73 — simmetriya, koʻchirish va burilish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-73: Simmetriya, koʻchirish va burilish",
        "category": "math",
        "order": 73,
        "summary": (
            "Kapalak, qorbobo naqshi va Samarqand gumbazi — hammasida bitta "
            "matematika bor. Simmetriya oʻqini topishni, burilish "
            "simmetriyasini sanashni va koordinatada aks ettirishni oʻrganasiz."
        ),
        "stories": ["Samarqand gumbazidagi naqsh"],
        "content": """
<h2>PM-73: Simmetriya, koʻchirish va burilish</h2>

<p>Kapalakning ikki qanoti bir xil. Qor parchasining olti nuri bir xil.
Samarqanddagi gumbazning naqshi esa qaysi tomondan qarasangiz ham
oʻzgarmaydi.</p>

<p>Bularning hammasi bitta narsaning nomi: <b>simmetriya</b>. Va u
naqqoshning ishini toʻrt barobar yengillashtiradigan aniq matematik
qurol.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>shaklning simmetriya oʻqlarini topib, sanaysiz;</li>
    <li>burilish simmetriyasi tartibini aniqlaysiz;</li>
    <li>koʻchirish, burilish va aks ettirishni farqlaysiz;</li>
    <li>koordinatada nuqtani aks ettirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">x oʻqiga nisbatan aks</span>
  <span class="pe-chip pe-chip--o">(x; y)</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">(x; −y)</span>
</div>

<h3>1. Oʻq simmetriyasi</h3>

<p>Shaklni bir chiziq boʻylab bukkanda ikki yarmi bir-birining ustiga
aniq tushsa, oʻsha chiziq — <b>simmetriya oʻqi</b>.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="Kvadratning toʻrtta simmetriya oʻqi">
    <rect class="pm-fill" x="98" y="38" width="124" height="124"/>
    <rect class="pm-ln" x="98" y="38" width="124" height="124" fill="none"/>
    <line class="pm-ln pm-ln--hl pm-ln--dash" x1="160" y1="20" x2="160" y2="180"/>
    <line class="pm-ln pm-ln--hl pm-ln--dash" x1="80" y1="100" x2="240" y2="100"/>
    <line class="pm-ln pm-ln--hl pm-ln--dash" x1="85.3" y1="25.3" x2="234.7" y2="174.7"/>
    <line class="pm-ln pm-ln--hl pm-ln--dash" x1="85.3" y1="174.7" x2="234.7" y2="25.3"/>
    <circle class="pm-pt" cx="160" cy="100" r="3.5"/>
  </svg>
  <figcaption>Kvadratda toʻrtta simmetriya oʻqi bor: ikkita tomonlar
  orasidan, ikkita burchaklardan.</figcaption>
</figure>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Shakl</th><th>Simmetriya oʻqlari</th><th>Izoh</th></tr>
  <tr><td>Kvadrat</td><td class="pm-word__sym">4</td>
    <td>2 ta oʻrta chiziq va 2 ta diagonal</td></tr>
  <tr><td>Teng tomonli uchburchak</td><td class="pm-word__sym">3</td>
    <td>har bir uchidan</td></tr>
  <tr><td>Toʻgʻri toʻrtburchak</td><td class="pm-word__sym">2</td>
    <td>faqat oʻrta chiziqlar, diagonal emas</td></tr>
  <tr><td>Romb</td><td class="pm-word__sym">2</td>
    <td>faqat ikkala diagonal</td></tr>
  <tr><td>Parallelogramm</td><td class="pm-word__sym">0</td>
    <td>bitta ham yoʻq</td></tr>
  <tr><td>Doira</td><td class="pm-word__sym">cheksiz</td>
    <td>markazdan oʻtgan har qanday chiziq</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Toʻgʻri toʻrtburchakning diagonali simmetriya
  oʻqi EMAS</p>
  <p>Bu eng koʻp uchraydigan xato. Kvadratda diagonal oʻq boʻladi,
  chunki tomonlari teng. Toʻgʻri toʻrtburchakda esa uni diagonal boʻylab
  bukkanda uzun tomon qisqa tomonning ustiga tushmaydi — bir chekkasi
  osilib qoladi. Bir varaq qogʻozni bukib koʻring, darrov
  ishonasiz.</p>
</div>

<h3>2. Burilish simmetriyasi</h3>

<p>Baʼzi shakllarning oʻqi yoʻq, lekin ularni <b>burib</b> qoʻysangiz,
oʻzgarmaganday koʻrinadi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="Naqsh 90 gradusga burilganda oʻzgarmaydi">
    <polygon class="pm-fill" points="160,105 234,105 194.7,69"/>
    <polyline class="pm-ln" points="160,105 234,105 194.7,69 160,105" fill="none"/>
    <polygon class="pm-fill pm-fill--hl" points="160,105 160,31 124,70.3"/>
    <polyline class="pm-ln" points="160,105 160,31 124,70.3 160,105" fill="none"/>
    <polygon class="pm-fill" points="160,105 86,105 125.3,141"/>
    <polyline class="pm-ln" points="160,105 86,105 125.3,141 160,105" fill="none"/>
    <polygon class="pm-fill pm-fill--hl" points="160,105 160,179 196,139.7"/>
    <polyline class="pm-ln" points="160,105 160,179 196,139.7 160,105" fill="none"/>
    <circle class="pm-pt" cx="160" cy="105" r="3.5"/>
    <path class="pm-ln pm-ln--hl" d="M 144 14.4 A 92 92 0 0 0 71.1 81.2" fill="none"/>
    <polygon class="pm-pt" points="144,14.4 136,20.4 134.1,13.2"/>
    <text class="pm-lbl pm-lbl--hl" x="28" y="38">90° burilish</text>
  </svg>
  <figcaption>Bu naqshni markazi atrofida 90° ga bursak, u aynan
  oʻzidek boʻlib qoladi. Demak uning burilish simmetriyasi 4.</figcaption>
</figure>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Burilish simmetriyasining tartibi</p>
  <p>Shakl toʻliq bir aylanish (360°) davomida necha marta oʻzidek
  koʻrinsa, oʻsha son — <b>tartib</b>. Burilish burchagi esa
  360° ÷ tartib.</p>
</div>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Shakl</th><th>Tartib</th><th>Burilish burchagi</th></tr>
  <tr><td>Kvadrat</td><td class="pm-word__sym">4</td><td>90°</td></tr>
  <tr><td>Teng tomonli uchburchak</td><td class="pm-word__sym">3</td>
    <td>120°</td></tr>
  <tr><td>Parallelogramm</td><td class="pm-word__sym">2</td><td>180°</td></tr>
  <tr><td>Doira</td><td class="pm-word__sym">cheksiz</td>
    <td>istalgan burchak</td></tr>
</table></div>

<p>Parallelogrammga eʼtibor bering: uning <b>bitta ham simmetriya oʻqi
yoʻq</b>, lekin 180° ga burilganda u oʻzidek boʻlib qoladi. Demak bu
ikki xil simmetriya bir-biridan mustaqil.</p>

<div class="pe-ex">
  <p class="pe-ex__math">360 ÷ 8 = 45°</p>
  <p class="pe-ex__uz">Sakkiz qirrali yulduz naqshi 45 gradusga
  burilganda oʻzgarmaydi.</p>
  <p class="pe-ex__why">Tartibi 8, demak burchak 360 ni 8 ga
  boʻlgandagi qiymat.</p>
</div>

<h3>3. Uchta harakat</h3>

<p>Shaklni qaerga qoʻyish yoki qanday oʻgirishning uchta yoʻli bor. Uchalasi
ham shaklning <b>oʻlchamini ham, shaklini ham oʻzgartirmaydi</b> — natija
dastlabkisiga <b>teng</b> boʻladi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Harakat</th><th>Nima qiladi</th><th>Hayotda</th></tr>
  <tr><td>Koʻchirish</td>
    <td class="pm-word__sym">siljitadi</td>
    <td>hoshiyadagi naqsh takrorlanishi</td></tr>
  <tr><td>Burilish</td>
    <td class="pm-word__sym">buradi</td>
    <td>gumbaz naqshi, gʻildirak</td></tr>
  <tr><td>Aks ettirish</td>
    <td class="pm-word__sym">koʻzguga soladi</td>
    <td>kapalak qanotlari, «A» harfi</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">PM-72 bilan farqi</p>
  <p>Oʻxshashlikda shakl <b>kattalashadi yoki kichrayadi</b>. Bu uchta
  harakatda esa oʻlcham <b>umuman oʻzgarmaydi</b> — narsa faqat joyini
  yoki holatini almashtiradi. Shuning uchun bu yerda k = 1.</p>
</div>

<h3>4. Koordinatada aks ettirish</h3>

<p>Koordinata tekisligida (PM-45) aks ettirish juda oddiy qoidaga
aylanadi: <b>bitta ishora almashadi</b>.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="A nuqtaning x oʻqiga nisbatan aksi">
    <line class="pm-ln" x1="30" y1="105" x2="295" y2="105"/>
    <line class="pm-ln" x1="150" y1="20" x2="150" y2="190"/>
    <line class="pm-ln" x1="62" y1="101" x2="62" y2="109"/>
    <line class="pm-ln" x1="84" y1="101" x2="84" y2="109"/>
    <line class="pm-ln" x1="106" y1="101" x2="106" y2="109"/>
    <line class="pm-ln" x1="128" y1="101" x2="128" y2="109"/>
    <line class="pm-ln" x1="172" y1="101" x2="172" y2="109"/>
    <line class="pm-ln" x1="194" y1="101" x2="194" y2="109"/>
    <line class="pm-ln" x1="216" y1="101" x2="216" y2="109"/>
    <line class="pm-ln" x1="238" y1="101" x2="238" y2="109"/>
    <line class="pm-ln" x1="260" y1="101" x2="260" y2="109"/>
    <line class="pm-ln" x1="146" y1="39" x2="154" y2="39"/>
    <line class="pm-ln" x1="146" y1="61" x2="154" y2="61"/>
    <line class="pm-ln" x1="146" y1="83" x2="154" y2="83"/>
    <line class="pm-ln" x1="146" y1="127" x2="154" y2="127"/>
    <line class="pm-ln" x1="146" y1="149" x2="154" y2="149"/>
    <line class="pm-ln" x1="146" y1="171" x2="154" y2="171"/>
    <line class="pm-ln pm-ln--dash" x1="216" y1="61" x2="216" y2="149"/>
    <circle class="pm-pt" cx="216" cy="61" r="4"/>
    <circle class="pm-pt" cx="216" cy="149" r="4"/>
    <text class="pm-lbl pm-lbl--hl" x="224" y="57">A (3; 2)</text>
    <text class="pm-lbl pm-lbl--hl" x="224" y="161">A′ (3; −2)</text>
    <text class="pm-lbl" x="288" y="97">x</text>
    <text class="pm-lbl" x="158" y="26">y</text>
    <text class="pm-lbl" x="136" y="121">0</text>
  </svg>
  <figcaption>A nuqta x oʻqidan 2 katak yuqorida, aksi esa 2 katak
  pastda. x oʻzgarmadi, y ishorasini almashtirdi.</figcaption>
</figure>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Nima qilinadi</th><th>Qoida</th><th>A (3; 2) qayerga tushadi</th></tr>
  <tr><td>x oʻqiga nisbatan aks</td>
    <td class="pm-word__sym">(x; −y)</td><td>(3; −2)</td></tr>
  <tr><td>y oʻqiga nisbatan aks</td>
    <td class="pm-word__sym">(−x; y)</td><td>(−3; 2)</td></tr>
  <tr><td>Boshi atrofida 180° burilish</td>
    <td class="pm-word__sym">(−x; −y)</td><td>(−3; −2)</td></tr>
  <tr><td>Koʻchirish (a; b) ga</td>
    <td class="pm-word__sym">(x + a; y + b)</td><td>(3 + a; 2 + b)</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__math">A (1; 1), B (4; 1), C (1; 3) →
  A′ (1; −1), B′ (4; −1), C′ (1; −3)</p>
  <p class="pe-ex__uz">Uchburchak x oʻqiga nisbatan aks ettirildi:
  har bir nuqtaning faqat y i ishorasini almashtirdi.</p>
  <p class="pe-ex__why">Yuzasi oʻzgarmaydi: ikkalasida ham
  (3 × 2) ÷ 2 = 3 kvadrat birlik (PM-68).</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Qaysi oʻq, qaysi ishora</p>
  <p><b>x oʻqiga</b> nisbatan aks ettirsangiz, nuqta yuqoridan pastga
  tushadi — demak <b>y</b> oʻzgaradi. <b>y oʻqiga</b> nisbatan aks
  ettirsangiz, nuqta oʻngdan chapga oʻtadi — demak <b>x</b> oʻzgaradi.
  Yaʼni <b>oʻqning nomi emas, ikkinchisi almashadi</b>. Aynan shu joyda
  yarim sinf adashadi.</p>
</div>

<h3>Matnli masala</h3>

<p>Usta devorga naqshli plitka teradi. Devor 2 metr balandlikda va
3 metr uzunlikda. Plitkalar kvadrat, tomoni 20 santimetr. Har bir
plitkadagi naqshning burilish simmetriyasi 4 — yaʼni plitkani 90° ga
bursangiz, naqsh oʻzgarmaydi.</p>

<p><b>Nechta plitka kerak va usta naqshning qancha qismini chizsa
yetarli?</b></p>

<p><b>Reja:</b> avval plitkalar sonini topamiz, keyin simmetriya
ustaning ishini necha marta kamaytirishini koʻramiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 m = 200 sm, 3 m = 300 sm</span>
    <span class="pm-solve__why">Birliklarni tenglashtirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">200 ÷ 20 = 10 qator</span>
    <span class="pm-solve__why">Balandligi boʻyicha</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">300 ÷ 20 = 15 ustun</span>
    <span class="pm-solve__why">Uzunligi boʻyicha</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">10 × 15 = 150 ta plitka</span>
    <span class="pm-solve__why">Jami</span>
  </div>
</div>

<p>Endi naqsh. Bitta plitkaning yuzasi 20 × 20 = 400 sm<sup>2</sup>.
Burilish simmetriyasi 4 boʻlgani uchun usta faqat <b>chorak</b> qismini
chizadi, qolgan uchtasi burib chiqiladi:</p>

<div class="pm-solve">
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">400 ÷ 4 = 100 sm<sup>2</sup></span>
    <span class="pm-solve__why">Chizish kerak boʻlgan qism</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Devorning yuzasi: 200 × 300 = 60 000 sm<sup>2</sup>.
  <br>Plitkalarning yuzasi: 150 × 400 = 60 000 sm<sup>2</sup> ✓ — toʻliq mos.
  <br><b>Javob:</b> 150 ta plitka; naqshning chorak qismi, yaʼni
  100 sm<sup>2</sup>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Toʻgʻri toʻrtburchakning 4 ta simmetriya oʻqi
  bor</p>
  <p class="pe-fix__good">2 ta — faqat oʻrta chiziqlar</p>
  <p class="pe-fix__why">Diagonal boʻylab bukilganda tomonlar bir-biriga
  tushmaydi. Toʻrtta oʻq faqat kvadratda boʻladi, chunki unda tomonlar
  ham teng.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Parallelogrammning 2 ta simmetriya oʻqi bor</p>
  <p class="pe-fix__good">0 ta oʻq, lekin burilish simmetriyasi 2</p>
  <p class="pe-fix__why">Uni hech qanday chiziq boʻylab bukib
  boʻlmaydi. Lekin markazi atrofida 180° ga bursangiz, u oʻzidek boʻlib
  qoladi — bu boshqa turdagi simmetriya.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">A (3; 2) ning x oʻqiga nisbatan aksi
  (−3; 2)</p>
  <p class="pe-fix__good">(3; −2)</p>
  <p class="pe-fix__why">x oʻqiga nisbatan aks ettirilganda nuqta
  pastga tushadi, demak <b>y</b> ning ishorasi almashadi. (−3; 2) — bu
  y oʻqiga nisbatan aks.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Burilishdan keyin shaklning yuzasi
  oʻzgaradi</p>
  <p class="pe-fix__good">Yuza ham, tomonlar ham oʻsha-oʻsha</p>
  <p class="pe-fix__why">Koʻchirish, burilish va aks ettirish shaklning
  faqat oʻrnini oʻzgartiradi. Oʻlcham oʻzgarishi uchun oʻxshashlik
  kerak (PM-72).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Kvadratning nechta simmetriya oʻqi bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>4 ta.</b> Ikkitasi tomonlarning oʻrtasidan, ikkitasi
    diagonallar boʻylab.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Kvadrat boʻlmagan toʻgʻri toʻrtburchakda
  nechta simmetriya oʻqi bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2 ta.</b> Faqat qarama-qarshi tomonlarning oʻrtasidan
    oʻtuvchi ikkita chiziq. Diagonallar bu yerda oʻq emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Parallelogrammning nechta simmetriya oʻqi
  bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Bitta ham yoʻq.</b> Lekin uning burilish simmetriyasi 2:
    markazi atrofida 180° ga burilsa, oʻzidek boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. A (5; −3) nuqtaning x oʻqiga nisbatan aksi
  qaysi nuqta?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(5; 3).</b> x oʻzgarmaydi, y ning ishorasi almashadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. B (−2; 4) nuqtaning y oʻqiga nisbatan aksi
  qaysi nuqta?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>(2; 4).</b> Bu safar y oʻzgarmaydi, x ning ishorasi
    almashadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Naqshning takrorlanuvchi boʻlagi 25 sm.
  Hoshiya 3 metr uzunlikda. Naqsh necha marta takrorlanadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>12 marta.</b> 3 m = 300 sm, keyin 300 ÷ 25 = 12. Bu —
    koʻchirish: bitta boʻlak oʻzgarmagan holda 12 marta siljitib
    qoʻyiladi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Simmetriya</b><span>shaklning oʻzini takrorlash xossasi; ingl.
    symmetry</span></li>
  <li><b>Simmetriya oʻqi</b><span>shaklni teng ikkiga bukadigan chiziq;
    ingl. line of symmetry</span></li>
  <li><b>Burilish simmetriyasi</b><span>burilgandan keyin oʻzgarmaslik;
    ingl. rotational symmetry</span></li>
  <li><b>Tartib</b><span>360° da necha marta oʻzidek koʻrinishi; ingl.
    order</span></li>
  <li><b>Koʻchirish</b><span>shaklni siljitish; ingl.
    translation</span></li>
  <li><b>Burilish</b><span>markaz atrofida burish; ingl.
    rotation</span></li>
  <li><b>Aks ettirish</b><span>chiziqqa nisbatan koʻzgudagidek
    oʻgirish; ingl. reflection</span></li>
  <li><b>Teng shakllar</b><span>oʻlchami ham, shakli ham bir xil; ingl.
    congruent figures</span></li>
  <li><b>Naqsh</b><span>takrorlanuvchi bezak; ingl. pattern</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Simmetriya oʻqi — buklaganda ikki yarmi mos tushadigan
      chiziq.</li>
    <li>Kvadrat 4, toʻgʻri toʻrtburchak 2, parallelogramm 0, doira
      cheksiz oʻqqa ega.</li>
    <li>Burilish simmetriyasi oʻqdan mustaqil: parallelogrammda oʻq
      yoʻq, lekin tartibi 2.</li>
    <li>Burilish burchagi = 360° ÷ tartib.</li>
    <li>Koʻchirish, burilish va aks ettirish oʻlchamni
      oʻzgartirmaydi.</li>
    <li>x oʻqiga nisbatan (x; y) → (x; −y); y oʻqiga nisbatan
      (x; y) → (−x; y).</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-74 — fazoviy shakllar: hajm va sirt yuzasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-74: Fazoviy shakllar: hajm va sirt yuzasi",
        "category": "math",
        "order": 74,
        "summary": (
            "Qogʻozdan chiqib, uch oʻlchamli dunyoga oʻtamiz: hajm nima, uni "
            "nima bilan oʻlchashadi, litr qayerdan chiqqan va silindr shaklidagi "
            "suv baki necha chelak suv sigʻdiradi."
        ),
        "stories": ["Suv baki necha chelak"],
        "content": """
<h2>PM-74: Fazoviy shakllar: hajm va sirt yuzasi</h2>

<p>Shu paytgacha hamma shaklimiz qogʻozda yotardi. Lekin xona, quti,
suv baki va choynak qogʻozda yotmaydi — ularning <b>ichi</b> bor.</p>

<p>Ichiga qancha narsa sigʻishi — <b>hajm</b>. Ustini qoplashga qancha
material ketishi — <b>sirt yuzasi</b>. Bular ikki xil savol va ikki xil
birlik.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>hajmni V = a × b × c bilan hisoblaysiz;</li>
    <li>qutining yoyilmasidan sirt yuzasini topasiz;</li>
    <li>sm<sup>3</sup>, m<sup>3</sup> va litrni bir-biriga
      oʻgirasiz;</li>
    <li>silindrning hajmini topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Hajm</span>
  <span class="pe-chip pe-chip--s">V</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">asos yuzasi</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">balandlik</span>
</div>

<h3>1. Hajm — nechta kubcha sigʻadi</h3>

<p>Yuza «nechta birlik kvadrat sigʻadi» degani edi (PM-68). Hajm ham
xuddi shunday, faqat kvadrat oʻrniga <b>kubcha</b>: tomoni 1 sm boʻlgan
kichkina kub — <b>1 kub santimetr</b>, sm<sup>3</sup>.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 215" role="img" aria-label="Toʻgʻri burchakli parallelepiped: a, b va c qirralari">
    <polygon class="pm-fill" points="58,92 198,92 198,182 58,182"/>
    <polygon class="pm-fill pm-fill--hl" points="58,92 198,92 253,50 113,50"/>
    <polygon class="pm-fill" points="198,92 253,50 253,140 198,182"/>
    <polyline class="pm-ln" points="58,92 198,92 198,182 58,182 58,92" fill="none"/>
    <polyline class="pm-ln" points="58,92 113,50 253,50 198,92" fill="none"/>
    <polyline class="pm-ln" points="253,50 253,140 198,182" fill="none"/>
    <line class="pm-ln pm-ln--dash" x1="113" y1="50" x2="113" y2="140"/>
    <line class="pm-ln pm-ln--dash" x1="113" y1="140" x2="253" y2="140"/>
    <line class="pm-ln pm-ln--dash" x1="113" y1="140" x2="58" y2="182"/>
    <text class="pm-lbl" x="112" y="202">a = 5 sm</text>
    <text class="pm-lbl" x="14" y="142">c = 4 sm</text>
    <text class="pm-lbl" x="258" y="64">b = 3 sm</text>
  </svg>
  <figcaption>Toʻgʻri burchakli parallelepiped. Punktir chiziqlar —
  koʻrinmayotgan, orqadagi qirralar.</figcaption>
</figure>

<p>Bu qutining tubiga nechta kubcha teriladi? Tub — 5 × 3 li toʻgʻri
toʻrtburchak, demak 15 ta. Endi shunday qavatlardan nechtasi bor?
Balandligi 4, demak 4 ta qavat:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5 × 3 = 15 ta</span>
    <span class="pm-solve__why">Bitta qavatdagi kubchalar (asos
    yuzasi)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 × 4 = 60 ta</span>
    <span class="pm-solve__why">Toʻrtta qavat (balandlik)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">V = 5 × 3 × 4 = 60 sm<sup>3</sup></span>
    <span class="pm-solve__why">Uchala qirraning koʻpaytmasi</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Bitta qoida — hamma prizmaga</p>
  <p>V = <b>asos yuzasi × balandlik</b>. Bu qoida qutida ham, uch
  burchakli prizmada ham, silindrda ham ishlaydi. Faqat asosning yuzasi
  har xil formula bilan topiladi.</p>
</div>

<p><b>Kub</b> — hamma qirrasi teng parallelepiped, shuning uchun
V = a<sup>3</sup>. Masalan a = 6 sm boʻlsa, V = 6 × 6 × 6 =
216 sm<sup>3</sup>.</p>

<h3>2. Sirt yuzasi va yoyilma</h3>

<p>Qutini kesib, yozib qoʻysak, oltita toʻgʻri toʻrtburchak chiqadi.
Bu — qutining <b>yoyilmasi</b>. Sirt yuzasi esa shu oltitasining
yigʻindisi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="Qutining yoyilmasi: oltita toʻgʻri toʻrtburchak">
    <rect class="pm-fill--hl" x="92" y="48" width="50" height="30"/>
    <rect class="pm-ln" x="92" y="48" width="50" height="30" fill="none"/>
    <text class="pm-lbl" x="105" y="67">a×b</text>
    <rect class="pm-fill" x="62" y="78" width="30" height="40"/>
    <rect class="pm-ln" x="62" y="78" width="30" height="40" fill="none"/>
    <text class="pm-lbl" x="65" y="102">b×c</text>
    <rect class="pm-fill" x="92" y="78" width="50" height="40"/>
    <rect class="pm-ln" x="92" y="78" width="50" height="40" fill="none"/>
    <text class="pm-lbl" x="105" y="102">a×c</text>
    <rect class="pm-fill" x="142" y="78" width="30" height="40"/>
    <rect class="pm-ln" x="142" y="78" width="30" height="40" fill="none"/>
    <text class="pm-lbl" x="145" y="102">b×c</text>
    <rect class="pm-fill" x="172" y="78" width="50" height="40"/>
    <rect class="pm-ln" x="172" y="78" width="50" height="40" fill="none"/>
    <text class="pm-lbl" x="185" y="102">a×c</text>
    <rect class="pm-fill--hl" x="92" y="118" width="50" height="30"/>
    <rect class="pm-ln" x="92" y="118" width="50" height="30" fill="none"/>
    <text class="pm-lbl" x="105" y="137">a×b</text>
    <text class="pm-lbl" x="101" y="38">a = 5</text>
    <text class="pm-lbl" x="28" y="102">c = 4</text>
    <text class="pm-lbl" x="32" y="67">b = 3</text>
  </svg>
  <figcaption>Oltita yoq, juft-juft teng: ikkita a×b, ikkita b×c,
  ikkita a×c.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">a × b = 5 × 3 = 15</span>
    <span class="pm-solve__why">Tub va usti</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">b × c = 3 × 4 = 12</span>
    <span class="pm-solve__why">Yon tomonlar</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">a × c = 5 × 4 = 20</span>
    <span class="pm-solve__why">Old va orqa</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">S = 2 × (15 + 12 + 20) =
    94 sm<sup>2</sup></span>
    <span class="pm-solve__why">Har biridan ikkitadan</span>
  </div>
</div>

<p>Kub uchun bu yanada oson: oltita bir xil kvadrat, demak
S = 6 × a<sup>2</sup>. a = 6 boʻlsa, S = 6 × 36 = 216 sm<sup>2</sup>.</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Bir xil son, boshqa maʼno</p>
  <p>Tomoni 6 boʻlgan kubda hajm ham 216, sirt yuzasi ham 216 chiqdi.
  Lekin biri 216 <b>kub</b> santimetr, ikkinchisi 216 <b>kvadrat</b>
  santimetr — butunlay boshqa narsalar. Javobni birligisiz yozish shu
  yerda katta xato boʻladi.</p>
</div>

<h3>3. Litr — hayotdagi hajm birligi</h3>

<p>Doʻkonda hech kim «uch ming kub santimetr sut» deb soʻramaydi.
Suyuqlik uchun <b>litr</b> ishlatiladi va u kub santimetr bilan juda
oddiy bogʻlangan.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Yodda tuting</span>
  <span class="pe-chip pe-chip--aux">1 litr</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">1000 sm<sup>3</sup></span>
  <span class="pe-op">va</span>
  <span class="pe-chip pe-chip--aux">1 m<sup>3</sup></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">1000 litr</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">40 × 25 × 30 = 30 000 sm<sup>3</sup> = 30 litr</p>
  <p class="pe-ex__uz">40 sm, 25 sm va 30 sm oʻlchamli akvariumga 30 litr
  suv sigʻadi.</p>
  <p class="pe-ex__why">30 000 ni 1000 ga boʻldik. Yaʼni oxiridan uchta
  nolni oʻchirsangiz, litr chiqadi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">1 litr 100 sm<sup>3</sup> emas</p>
  <p>Hajmda uchta oʻlcham bor, shuning uchun nollar ham uchtadan
  yuradi: 1 litr = 1000 sm<sup>3</sup> (tomoni 10 sm boʻlgan kub:
  10 × 10 × 10). Xuddi shunday, 1 m<sup>3</sup> = 1000 litr, 100 emas.
  Yuzada bu boshqacha edi: 1 m<sup>2</sup> = 10 000 sm<sup>2</sup>
  (PM-68).</p>
</div>

<h3>4. Silindr</h3>

<p>Suv baki, konserva bankasi, quduq halqasi — hammasi silindr. Unga ham
oʻsha bitta qoida ishlaydi: <b>asos yuzasi × balandlik</b>. Asos esa
doira, uning yuzasini PM-71 da topganmiz.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="Silindr: radiusi r, balandligi h">
    <rect class="pm-fill" x="98" y="52" width="124" height="106"/>
    <path class="pm-fill" d="M 98 158 A 62 19 0 0 0 222 158 Z"/>
    <path class="pm-ln pm-ln--dash" d="M 98 158 A 62 19 0 0 1 222 158" fill="none"/>
    <path class="pm-ln" d="M 98 158 A 62 19 0 0 0 222 158" fill="none"/>
    <line class="pm-ln" x1="98" y1="52" x2="98" y2="158"/>
    <line class="pm-ln" x1="222" y1="52" x2="222" y2="158"/>
    <ellipse class="pm-fill--hl" cx="160" cy="52" rx="62" ry="19"/>
    <ellipse class="pm-ln" cx="160" cy="52" rx="62" ry="19" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="160" y1="52" x2="222" y2="52"/>
    <circle class="pm-pt" cx="160" cy="52" r="3"/>
    <line class="pm-ln pm-ln--dash" x1="248" y1="52" x2="248" y2="158"/>
    <text class="pm-lbl pm-lbl--hl" x="182" y="44">r</text>
    <text class="pm-lbl pm-lbl--hl" x="254" y="109">h</text>
    <text class="pm-lbl pm-lbl--hl" x="48" y="190">V = π × r² × h</text>
  </svg>
  <figcaption>Silindr — bir-birining ustiga terilgan doiralar. Asosi
  π × r<sup>2</sup>, balandligi h.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">S = 3,14 × 1<sup>2</sup> =
    3,14 m<sup>2</sup></span>
    <span class="pm-solve__why">Asosning yuzasi, r = 1 m (PM-71)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">V = 3,14 × 2 = 6,28 m<sup>3</sup></span>
    <span class="pm-solve__why">Balandlikka koʻpaytirdik, h = 2 m</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">6,28 × 1000 = 6280 litr</span>
    <span class="pm-solve__why">Fermer xoʻjaligining suv baki</span>
  </div>
</div>

<h3>Matnli masala</h3>

<p>Dilnozaning akvariumi toʻgʻri burchakli quti shaklida: uzunligi
60 sm, eni 30 sm, balandligi 40 sm. Suv yuqori chetidan 5 sm past
quyiladi. Suv 7 litrli chelakda tashiladi.</p>

<p><b>Necha chelak suv kerak? Va akvarium uchun necha kvadrat metr
shisha ketgan (usti ochiq)?</b></p>

<p><b>Reja:</b> avval suvning balandligini aniqlaymiz, hajmni topib
litrga oʻgiramiz, keyin beshta yoqning yuzasini qoʻshamiz.</p>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Toʻla boʻlganda 60 × 30 × 40 = 72 000 sm<sup>3</sup> = 72 litr
  boʻlardi. Suv sal kamroq, demak javob 60–70 litr atrofida.</span>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">40 − 5 = 35 sm</span>
    <span class="pm-solve__why">Suvning balandligi — qutiniki
    emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 × 30 × 35 = 63 000 sm<sup>3</sup></span>
    <span class="pm-solve__why">Suvning hajmi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">63 000 ÷ 1000 = 63 litr</span>
    <span class="pm-solve__why">Litrga oʻgirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">63 ÷ 7 = 9 chelak</span>
    <span class="pm-solve__why">Toʻliq toʻqqizta</span>
  </div>
</div>

<p>Endi shisha. Usti ochiq, demak <b>beshta</b> yoq bor: tub, ikkita
uzun yon va ikkita qisqa yon.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Tub: 60 × 30 = 1800 sm<sup>2</sup></span>
    <span class="pm-solve__why">Bitta</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Uzun yonlar: 2 × (60 × 40) =
    4800 sm<sup>2</sup></span>
    <span class="pm-solve__why">Ikkita</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qisqa yonlar: 2 × (30 × 40) =
    2400 sm<sup>2</sup></span>
    <span class="pm-solve__why">Ikkita</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">1800 + 4800 + 2400 = 9000 sm<sup>2</sup>
    = 0,9 m<sup>2</sup></span>
    <span class="pm-solve__why">1 m<sup>2</sup> = 10 000 sm<sup>2</sup>
    (PM-68)</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>63 litr — taxminimizdagi 60–70 oraligʻida ✓
  <br>9 × 7 = 63 ✓ — chelaklar roppa-rosa yetdi.
  <br><b>Javob:</b> 9 chelak suv va 0,9 m<sup>2</sup> shisha.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">V = 5 × 3 × 4 = 60 sm<sup>2</sup></p>
  <p class="pe-fix__good">60 sm<sup>3</sup></p>
  <p class="pe-fix__why">Uchta uzunlik koʻpaytirildi, demak birlik ham
  uchinchi darajada. sm<sup>2</sup> — yuzaning birligi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">1 litr = 100 sm<sup>3</sup></p>
  <p class="pe-fix__good">1 litr = 1000 sm<sup>3</sup></p>
  <p class="pe-fix__why">Litr — tomoni 10 sm boʻlgan kub:
  10 × 10 × 10 = 1000. Shu bitta xato butun masalani oʻn barobar
  buzadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Akvariumdagi suv: 60 × 30 × 40 = 72 litr</p>
  <p class="pe-fix__good">60 × 30 × 35 = 63 litr</p>
  <p class="pe-fix__why">Formulaga qutining emas, <b>suvning</b>
  balandligi qoʻyiladi. Masalada «5 sm past» deyilgan — bu son shunchaki
  qoʻyilgan emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">S = 15 + 12 + 20 = 47 sm<sup>2</sup></p>
  <p class="pe-fix__good">S = 2 × 47 = 94 sm<sup>2</sup></p>
  <p class="pe-fix__why">Uchta emas, oltita yoq bor: har birining
  qarama-qarshisi ham mavjud. Yoyilmaga qarang va sanang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Qutining qirralari 4 sm, 5 sm va 2 sm. Hajmi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>40 sm<sup>3</sup>.</b> V = 4 × 5 × 2 = 40.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Kubning qirrasi 3 sm. Hajmi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>27 sm<sup>3</sup>.</b> V = 3<sup>3</sup> = 3 × 3 × 3 = 27.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Oʻsha 4 sm × 5 sm × 2 sm qutining sirt yuzasi
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>76 sm<sup>2</sup>.</b> 4 × 5 = 20, 5 × 2 = 10, 4 × 2 = 8;
    yigʻindisi 38; S = 2 × 38 = 76.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Kubning qirrasi 5 sm. Sirt yuzasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>150 sm<sup>2</sup>.</b> S = 6 × a<sup>2</sup> = 6 × 25 =
    150.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. 2500 sm<sup>3</sup> necha litr?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2,5 litr.</b> 2500 ÷ 1000 = 2,5.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Silindrning radiusi 2 m, balandligi 3 m.
  Hajmi qancha? (π ≈ 3,14)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>37,68 m<sup>3</sup>.</b> Asos yuzasi: 3,14 × 4 =
    12,56 m<sup>2</sup>. Hajm: 12,56 × 3 = 37,68 m<sup>3</sup>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Jasurlarning suv baki 1 m × 0,8 m × 0,5 m.
  Oila kuniga 80 litr suv sarflaydi. Toʻla bak necha kunga yetadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5 kunga.</b> Hajm: 1 × 0,8 × 0,5 = 0,4 m<sup>3</sup>. Litrga:
    0,4 × 1000 = 400 litr. Kunlar: 400 ÷ 80 = 5.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Hajm</b><span>jism ichiga sigʻadigan joy, V; ingl.
    volume</span></li>
  <li><b>Kub santimetr</b><span>sm<sup>3</sup> — tomoni 1 sm boʻlgan
    kub; ingl. cubic centimetre</span></li>
  <li><b>Litr</b><span>1000 sm<sup>3</sup>; ingl. litre</span></li>
  <li><b>Toʻgʻri burchakli parallelepiped</b><span>oddiy quti shakli;
    ingl. cuboid</span></li>
  <li><b>Kub</b><span>hamma qirrasi teng parallelepiped; ingl.
    cube</span></li>
  <li><b>Qirra</b><span>ikki yoq kesishgan chiziq; ingl. edge</span></li>
  <li><b>Yoq</b><span>jismning yassi tomoni; ingl. face</span></li>
  <li><b>Sirt yuzasi</b><span>hamma yoqlarning yuzasi; ingl. surface
    area</span></li>
  <li><b>Yoyilma</b><span>jismning yozib qoʻyilgan koʻrinishi; ingl.
    net</span></li>
  <li><b>Silindr</b><span>asosi doira boʻlgan jism; ingl.
    cylinder</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Hajm — nechta birlik kub sigʻishi, sm<sup>3</sup> yoki
      m<sup>3</sup> da.</li>
    <li>V = asos yuzasi × balandlik — qutida ham, silindrda ham.</li>
    <li>Quti: V = a × b × c. Kub: V = a<sup>3</sup>.</li>
    <li>Sirt yuzasi: S = 2 × (ab + bc + ac). Kub: S = 6a<sup>2</sup>.</li>
    <li>1 litr = 1000 sm<sup>3</sup>, 1 m<sup>3</sup> = 1000 litr.</li>
    <li>Silindr: V = π × r<sup>2</sup> × h.</li>
  </ul>
</div>
""",
    },
]
