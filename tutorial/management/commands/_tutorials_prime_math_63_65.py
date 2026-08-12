# -*- coding: utf-8 -*-
"""Prime Math — darslar 63–65 (teng yonli uchburchak, Pifagor teoremasi va
uning qoʻllanishi).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt
**Blok E: Geometriya** — har bir darsda SVG chizma SHART.

  mashqlar — practice/management/commands/_practice_pm_63_65.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_63_65.py

⚠️ Chizmalar QOʻLDA hisoblanmagan: burchak yoylari, teng tomon belgilari va
   Pifagor isbotidagi ikki joylashtirish scratchpad/svgkit.py + gen_pm63_65.py
   bilan generatsiya qilingan, verify_pm_63_65.py esa ularni qaytadan
   tekshiradi (yoy uchlari nurlar ustida yotishi, isbotdagi sakkizta
   uchburchakning hammasi haqiqatan 3-4-5 ekani).

⚠️ Kumulyativ chegaralar:
  • PM-63 — teng yonli/teng tomonli uchburchak: asosdagi burchaklar tengligi
    va uning teskarisi, teng tomonli → 60°;
  • PM-64 — Pifagor teoremasi va ISBOTI. Isbot faqat KVADRATNING yuzasiga
    tayanadi (tomon², PM-12/PM-13 da ishlatilgan) — uchburchak yuzasi
    formulasi (PM-68) ISHLATILMAYDI: bitta katta kvadrat, oʻsha toʻrtta
    uchburchak, ikki xil joylashtirish;
  • PM-65 — qoʻllanish: narvon, tom balandligi (PM-63 bilan birga),
    koordinatadagi masofa (PM-45/46), teskari teorema bilan burchak
    tekshirish.
  • ⛔ Toʻrtburchaklar oilasi (PM-66) YOʻQ; perimetr (PM-67) va yuza
    formulalari (PM-68/69) YOʻQ; aylana va π (PM-70) YOʻQ; oʻxshashlik
    (PM-72) YOʻQ; sinus/kosinus umuman yoʻq (kursda yoʻq).
  • Faol ishlatiladi: uchburchak turlari va 180° (PM-61), uchburchak
    tengsizligi (PM-62), burchak juftliklari (PM-59), kvadrat ildiz va aniq
    kvadratlar (PM-13), daraja (PM-12), tenglama (PM-36/37), koordinata
    (PM-45/46), yaxlitlash (PM-14).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_63_65.py --author=prime
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
    # PM-63 — teng yonli va teng tomonli uchburchak
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-63: Teng yonli va teng tomonli uchburchak",
        "category": "math",
        "order": 63,
        "summary": (
            "Ikki tomoni teng boʻlsa, asosdagi ikki burchak ham teng — va "
            "teskarisi ham toʻgʻri. Shu bitta qoida bilan tomning, chodirning "
            "va teng tomonli uchburchakning hamma burchagi topiladi."
        ),
        "stories": ["Uyning tomi"],
        "content": """
<h2>PM-63: Teng yonli va teng tomonli uchburchak</h2>

<p>Koʻchaga chiqib uylarning tomiga qarang. Deyarli hammasining ikki yon
yogʻochi bir xil uzunlikda — shuning uchun tom qiyshiq emas, simmetrik
koʻrinadi. Usta buni tasodifan qilmaydi.</p>

<p>Bunday uchburchakning bitta ajoyib xossasi bor: <b>bitta burchagini
bilsangiz, qolgan ikkitasini oʻlchamasdan aytib berasiz.</b></p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>teng yonli uchburchakning qismlarini nomlaysiz: asos, yon tomon,
      uchidagi va asosdagi burchaklar;</li>
    <li>asosdagi burchaklar nega teng ekanini tushunasiz;</li>
    <li>bitta burchakdan qolgan ikkitasini hisoblaysiz;</li>
    <li>teng tomonli uchburchakning har bir burchagi nega aynan 60° ekanini
      isbotlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Teng yonli uchburchak</span>
  <span class="pe-chip pe-chip--o">AB = AC</span>
  <span class="pe-op">⟺</span>
  <span class="pe-chip pe-chip--s">∠B = ∠C</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">asosdagi burchaklar</span>
</div>

<h3>1. Qismlarning nomi</h3>

<p>Uchburchakning <b>ikki tomoni teng</b> boʻlsa, u <b>teng yonli</b> deyiladi.
Uning qismlari alohida nom oladi, chunki ularning har biri boshqacha
ishlaydi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img"
       aria-label="Teng yonli uchburchakning qismlari: asos, yon tomonlar, uchidagi burchak">
    <polygon class="pm-fill" points="160,45 55,165 265,165"/>
    <polyline class="pm-ln" points="55,165 265,165 160,45 55,165" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="112" y1="109" x2="103" y2="101"/>
    <line class="pm-ln pm-ln--hl" x1="217" y1="101" x2="208" y2="109"/>
    <path class="pm-ln pm-ln--hl" d="M 89 165 A 34 34 0 0 0 77.4 139.4" fill="none"/>
    <path class="pm-ln pm-ln--hl" d="M 242.6 139.4 A 34 34 0 0 0 231 165" fill="none"/>
    <path class="pm-ln" d="M 142.9 64.6 A 26 26 0 0 0 177.1 64.6" fill="none"/>
    <text class="pm-lbl" x="131.2" y="95.5">uchidagi</text>
    <text class="pm-lbl pm-lbl--hl" x="88" y="148">teng</text>
    <text class="pm-lbl pm-lbl--hl" x="203.2" y="148">teng</text>
    <text class="pm-lbl pm-lbl--hl" x="16" y="98">yon tomon</text>
    <text class="pm-lbl pm-lbl--hl" x="250" y="98">yon tomon</text>
    <text class="pm-lbl" x="142" y="185">asos</text>
    <text class="pm-lbl" x="152" y="36">A</text>
    <text class="pm-lbl" x="38" y="176">B</text>
    <text class="pm-lbl" x="274" y="176">C</text>
  </svg>
  <figcaption>AB = AC — teng yon tomonlar. Ular orasidagi ∠A — uchidagi
  burchak, BC — asos. Asosdagi ∠B va ∠C har doim teng.</figcaption>
</figure>

<ul>
  <li><b>Yon tomonlar</b> — teng boʻlgan ikkita tomon (chizmada kichik
    chiziqcha bilan belgilangan).</li>
  <li><b>Asos</b> — uchinchi tomon. U yon tomonlarga teng boʻlishi <i>shart
    emas</i>.</li>
  <li><b>Uchidagi burchak</b> — ikki yon tomon orasidagi burchak (∠A).</li>
  <li><b>Asosdagi burchaklar</b> — asosga tegib turgan ikkita burchak
    (∠B va ∠C).</li>
</ul>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Chizmadagi bir xil chiziqchalar</p>
  <p>Geometriyada teng tomonlar bir xil sondagi kichik chiziqcha bilan
  belgilanadi. Ikki tomonda bittadan chiziqcha boʻlsa — ular teng. Bu
  yozuvni oʻqishni oʻrganib olsangiz, chizmaning yarmi oʻzi gapirib
  beradi.</p>
</div>

<h3>2. Asosdagi burchaklar nega teng?</h3>

<p>Qogʻozdan teng yonli uchburchak qirqib oling va uni uchidagi burchakdan
asosning oʻrtasiga qarab <b>buklang</b>. Ikki yarmi ustma-ust tushadi:
yon tomonlar teng edi, buklash chizigʻi esa ikkalasiga ham umumiy.</p>

<p>Ustma-ust tushgandan keyin ∠B ∠C ning ustiga tushadi. Ikki narsa
ustma-ust tushsa, ular teng — demak <b>∠B = ∠C</b>.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Teng yonli uchburchak qoidasi</p>
  <p>Uchburchakning <b>ikki tomoni teng boʻlsa, ularning qarshisidagi ikki
  burchak ham teng</b> boʻladi.
  <br>Bu PM-62 dagi «katta tomon — katta burchak» qoidasining tabiiy
  davomi: tomonlar teng boʻlsa, burchaklar ham tenglashadi.</p>
</div>

<p>Qoida <b>ikki tomonga</b> ham ishlaydi — teskarisi ham toʻgʻri.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Teskari qoida</p>
  <p>Uchburchakning <b>ikki burchagi teng boʻlsa, ularning qarshisidagi ikki
  tomon ham teng</b> — yaʼni uchburchak teng yonli boʻladi. Buni ish paytida
  koʻp ishlatishadi: burchakni oʻlchash tomonni oʻlchashdan oson.</p>
</div>

<h3>3. Bitta burchakdan qolganini topish</h3>

<p>PM-61 dan bilamiz: uchala burchakning yigʻindisi <b>180°</b>. Teng yonli
uchburchakda esa ikkitasi teng. Ikkita maʼlumot birga — bitta burchak
yetarli boʻlib qoladi.</p>

<p><b>Holat 1. Uchidagi burchak berilgan.</b> ∠A = 40°. Asosdagi burchaklar
qancha?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠B + ∠C = 180 − 40 = 140°</span>
    <span class="pm-solve__why">Uchidagisini 180 dan ayirdik (PM-61)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠B = ∠C</span>
    <span class="pm-solve__why">Asosdagi burchaklar teng</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">∠B = ∠C = 140 ÷ 2 = 70°</span>
    <span class="pm-solve__why">140 ni ikkiga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>40 + 70 + 70 = 180 ✓ — yigʻindi joyida.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Amallar tartibi bu yerda ham tuzoq</p>
  <p>Formulani <b>(180 − 40) ÷ 2</b> deb yozing, qavs bilan. Qavssiz yozilsa,
  180 − 40 ÷ 2 = 180 − 20 = <b>160</b> chiqadi — bu bitta burchak uchun
  hech qanday maʼnoga ega emas. Avval ayirish, keyin boʻlish (PM-5).</p>
</div>

<p><b>Holat 2. Asosdagi burchak berilgan.</b> ∠B = 65°. Uchidagi burchak
qancha?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">∠C = 65°</span>
    <span class="pm-solve__why">Asosdagi ikkinchi burchak ham shuncha</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">65 + 65 = 130°</span>
    <span class="pm-solve__why">Ikkalasining yigʻindisi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">∠A = 180 − 130 = 50°</span>
    <span class="pm-solve__why">Qolgani uchidagi burchakka tegishli</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">«Bitta burchagi 40°» — bu yetarli maʼlumotmi?</p>
  <p>Yoʻq, agar <b>qaysi</b> burchak ekani aytilmagan boʻlsa. Ikki xil javob
  chiqadi:
  <br>• 40° <b>uchidagi</b> boʻlsa → 70°, 70°, 40°;
  <br>• 40° <b>asosdagi</b> boʻlsa → 40°, 40°, 100°.
  <br>Masalada «uchidagi» yoki «asosdagi» degan soʻzni har doim izlang.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">Asosdagi burchak 95° boʻla oladimi? 95 + 95 = 190 &gt; 180 ✗</p>
  <p class="pe-ex__uz">Yoʻq. Asosdagi burchak har doim 90° dan kichik.</p>
  <p class="pe-ex__why">Ikkalasi teng, yigʻindisi esa 180 dan kam boʻlishi
  kerak — chunki uchidagi burchakka ham joy qolishi shart.</p>
</div>

<h3>4. Teng tomonli uchburchak</h3>

<p>Endi eng chiroyli holat: <b>uchala tomon teng</b>. Bunday uchburchak
<b>teng tomonli</b> deyiladi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 195" role="img"
       aria-label="Teng tomonli uchburchakning har bir burchagi 60 gradus">
    <polygon class="pm-fill" points="160,20.8 75,168 245,168"/>
    <polyline class="pm-ln" points="75,168 245,168 160,20.8 75,168" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="123.9" y1="95.2" x2="113.6" y2="89.2"/>
    <line class="pm-ln pm-ln--hl" x1="121.4" y1="99.6" x2="111.1" y2="93.6"/>
    <line class="pm-ln pm-ln--hl" x1="206.4" y1="89.2" x2="196.1" y2="95.2"/>
    <line class="pm-ln pm-ln--hl" x1="208.9" y1="93.6" x2="198.6" y2="99.6"/>
    <line class="pm-ln pm-ln--hl" x1="157.5" y1="162" x2="157.5" y2="174"/>
    <line class="pm-ln pm-ln--hl" x1="162.5" y1="162" x2="162.5" y2="174"/>
    <path class="pm-ln" d="M 107 168 A 32 32 0 0 0 91 140.3" fill="none"/>
    <path class="pm-ln" d="M 229 140.3 A 32 32 0 0 0 213 168" fill="none"/>
    <path class="pm-ln" d="M 144 48.5 A 32 32 0 0 0 176 48.5" fill="none"/>
    <text class="pm-lbl" x="105.8" y="148.5">60°</text>
    <text class="pm-lbl" x="192.6" y="148.5">60°</text>
    <text class="pm-lbl" x="149.2" y="73.3">60°</text>
  </svg>
  <figcaption>Uchala tomon teng — demak uchala burchak ham teng:
  180 ÷ 3 = 60°.</figcaption>
</figure>

<p>Isbot bir qatorga sigʻadi. Qaysi tomonni «asos» deb olsangiz ham,
uchburchak teng yonli boʻlib chiqadi — demak <b>hamma burchak bir-biriga
teng</b>. Uchtasining yigʻindisi 180° edi:</p>

<div class="pm-solve">
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">180 ÷ 3 = 60°</span>
    <span class="pm-solve__why">Teng tomonli uchburchakning har bir
    burchagi</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Yodda tuting</p>
  <p>Teng tomonli uchburchakning burchaklari <b>hech qachon oʻzgarmaydi</b>:
  har doim 60°, 60°, 60°. Uchburchak katta yoki kichik boʻlishi mumkin,
  lekin burchaklari oʻsha-oʻsha. Har bir teng tomonli uchburchak ayni
  paytda teng yonli hamdir — teskarisi esa notoʻgʻri.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Tomning burchagi.</b> Karim aka uy tomini yasayapti. Tomning ikki yon
yogʻochi teng uzunlikda, ular uchida tutashadi va oʻsha yerda <b>110</b>°
burchak hosil qiladi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 185" role="img"
       aria-label="Tom uchburchagi: uchidagi burchak 110 gradus, asosdagilar 35 gradus">
    <polygon class="pm-fill" points="160,71 40,155 280,155"/>
    <polyline class="pm-ln" points="40,155 280,155 160,71 40,155" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="103.4" y1="117.9" x2="96.6" y2="108.1"/>
    <line class="pm-ln pm-ln--hl" x1="223.4" y1="108.1" x2="216.6" y2="117.9"/>
    <path class="pm-ln pm-ln--hl" d="M 135.4 88.2 A 30 30 0 0 0 184.6 88.2" fill="none"/>
    <path class="pm-ln" d="M 80 155 A 40 40 0 0 0 72.8 132.1" fill="none"/>
    <path class="pm-ln" d="M 247.2 132.1 A 40 40 0 0 0 240 155" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="145.6" y="121.5">110°</text>
    <text class="pm-lbl" x="93.6" y="141.5">?</text>
    <text class="pm-lbl" x="219.2" y="141.5">?</text>
    <line class="pm-ln pm-ln--dash" x1="40" y1="155" x2="280" y2="155"/>
  </svg>
  <figcaption>Tomning ikki yon yogʻochi teng uzunlikda. Uchidagi burchak
  110° boʻlsa, ular gorizontal bilan qanday burchak hosil qiladi?</figcaption>
</figure>

<p><b>Nima soʻralyapti:</b> yogʻochlar gorizontal devor bilan qanday burchak
hosil qiladi.</p>

<p><b>Reja:</b> ikki yon yogʻoch teng — demak uchburchak teng yonli, va
gorizontal chiziq uning asosi. Bizga asosdagi burchak kerak.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">180 − 110 = 70°</span>
    <span class="pm-solve__why">Ikki asos burchagiga qolgan ulush</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">70 ÷ 2 = 35°</span>
    <span class="pm-solve__why">Ular teng, shuning uchun teng ikkiga
    boʻlinadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>35 + 35 + 110 = 180 ✓
  <br><b>Javob:</b> har bir yogʻoch gorizontal bilan 35° burchak hosil
  qiladi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Uchidagi burchak 110° — yoyiq (180°) ning yarmidan koʻproq. Demak
  asosdagi ikkalasiga birgalikda yarmidan kami qoladi, har biriga esa 45°
  dan kam. 35° bu chegaraga toʻgʻri keladi.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Uchidagi 40° → asosdagi = 180 − 40 ÷ 2 = 160°</p>
  <p class="pe-fix__good">Uchidagi 40° → asosdagi = (180 − 40) ÷ 2 = 70°</p>
  <p class="pe-fix__why">Qavs tushib qolgan. Avval ayirish, keyin boʻlish —
  amallar tartibi (PM-5). 160° bitta burchak uchun juda katta: uchtasining
  yigʻindisi 180° ekanini eslang.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Teng yonli uchburchakning bitta burchagi 40° →
    qolgan ikkitasi 70° va 70°</p>
  <p class="pe-fix__good">Qaysi burchak ekani aytilmagan boʻlsa,
    <b>ikkita</b> javob bor: 70°, 70° yoki 40°, 100°</p>
  <p class="pe-fix__why">40° uchidagi ham, asosdagi ham boʻlishi mumkin.
  Masala matnida bu soʻz boʻlmasa, ikkala holatni ham yozing.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Teng yonli uchburchakning uchala burchagi teng</p>
  <p class="pe-fix__good">Faqat <b>asosdagi ikkitasi</b> teng</p>
  <p class="pe-fix__why">Uchalasi teng boʻladigan uchburchak boshqacha
  ataladi — <b>teng tomonli</b>, va u yerda har bir burchak 60°.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Asosdagi burchaklar 95° va 95°, uchidagisi −10°</p>
  <p class="pe-fix__good">Asosdagi burchak 90° dan kichik boʻlishi shart</p>
  <p class="pe-fix__why">95 + 95 = 190 va bu 180 dan katta — bunday
  uchburchak yoʻq. Javob manfiy chiqsa, demak boshlangʻich son notoʻgʻri.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Teng yonli uchburchakning uchidagi burchagi 96°.
  Asosdagi burchaklar qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>42° va 42°.</b> (180 − 96) ÷ 2 = 84 ÷ 2 = 42.
    Tekshirish: 96 + 42 + 42 = 180 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Teng yonli uchburchakning asosdagi burchagi 55°.
  Uchidagi burchak qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>70°.</b> Asosdagi ikkinchi burchak ham 55°, ikkalasi 110° beradi.
    180 − 110 = 70.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Teng yonli uchburchakning uchidagi burchagi
  toʻgʻri burchak. Asosdagi burchaklar qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>45° va 45°.</b> Toʻgʻri burchak — 90° (PM-58). (180 − 90) ÷ 2 = 45.
    Bu uchburchak ham teng yonli, ham toʻgʻri burchakli — ikkala nom bir
    vaqtda toʻgʻri.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Teng yonli uchburchakning bitta burchagi 100°.
  Qolgan ikkitasi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>40° va 40°.</b> Bu yerda ikkinchi javob yoʻq: 100° asosdagi
    boʻlsa, ikkitasi 200° boʻlib ketardi — bu esa 180 dan katta. Demak 100°
    faqat uchidagi burchak boʻla oladi va (180 − 100) ÷ 2 = 40.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Uchburchakning ikki burchagi 64° va 52°. U teng
  yonlimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Ha.</b> Uchinchi burchak: 180 − 64 − 52 = 64°. Demak ikkita
    burchak 64° ga teng, teskari qoidaga koʻra ularning qarshisidagi
    tomonlar ham teng — uchburchak teng yonli.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Dilnoza chodir tikdi. Chodirning ikki yon tomoni
  teng, uchidagi burchagi esa 44°. Chodirning yon tomoni yer bilan qanday
  burchak hosil qiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>68°.</b> Yer — chodirning asosi. (180 − 44) ÷ 2 = 136 ÷ 2 = 68.
    Tekshirish: 68 + 68 + 44 = 180 ✓ Chodir tik: asosdagi burchak 45° dan
    katta boʻlgani uchun u baland va tor koʻrinadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Teng yonli uchburchak</b><span>ikki tomoni teng uchburchak; ingl.
    isosceles triangle</span></li>
  <li><b>Teng tomonli uchburchak</b><span>uchala tomoni teng, har bir
    burchagi 60°; ingl. equilateral triangle</span></li>
  <li><b>Yon tomon</b><span>teng boʻlgan ikki tomondan biri; ingl.
    leg</span></li>
  <li><b>Asos</b><span>teng yonli uchburchakning uchinchi tomoni; ingl.
    base</span></li>
  <li><b>Uchidagi burchak</b><span>ikki yon tomon orasidagi burchak; ingl.
    apex angle</span></li>
  <li><b>Asosdagi burchaklar</b><span>asosga tegib turgan teng burchaklar;
    ingl. base angles</span></li>
  <li><b>Teskari qoida</b><span>shart bilan xulosa oʻrin almashgan qoida;
    ingl. converse</span></li>
  <li><b>Simmetrik</b><span>buklaganda ikki yarmi ustma-ust tushadigan;
    ingl. symmetric</span></li>
  <li><b>Belgi chiziqcha</b><span>chizmada teng tomonlarni koʻrsatuvchi
    kichik chiziq; ingl. tick mark</span></li>
  <li><b>Burchaklar yigʻindisi</b><span>uchburchakda har doim 180°; ingl.
    angle sum</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Ikki tomoni teng → asosdagi ikki burchak teng. Teskarisi ham
      toʻgʻri.</li>
    <li>Uchidagi burchak berilgan: asosdagi = (180 − uchidagi) ÷ 2 —
      qavs bilan.</li>
    <li>Asosdagi burchak berilgan: uchidagi = 180 − 2 × asosdagi.</li>
    <li>Asosdagi burchak har doim 90° dan kichik.</li>
    <li>Teng tomonli uchburchakning har bir burchagi 60°, doim.</li>
    <li>«Bitta burchagi 40°» — qaysi burchak ekanini aniqlang: 70°/70° yoki
      40°/100°.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-64 — Pifagor teoremasi va uning isboti
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-64: Pifagor teoremasi — va nega u ishlaydi",
        "category": "math",
        "order": 64,
        "summary": (
            "Toʻgʻri burchakli uchburchakda ikki katetning kvadratlari "
            "yigʻindisi gipotenuzaning kvadratiga teng. Formulaning oʻzi ham, "
            "uning bitta chizmaga sigʻadigan isboti ham shu darsda."
        ),
        "stories": ["Oʻn ikki tugunli arqon"],
        "content": """
<h2>PM-64: Pifagor teoremasi — va nega u ishlaydi</h2>

<p>Usta pol qoʻyishdan oldin xonaning burchagi haqiqatan toʻgʻri burchakmi
yoki yoʻqmi, tekshiradi. U transportir olmaydi — ruletka oladi. Bir tomonga
<b>3</b> metr, ikkinchisiga <b>4</b> metr belgilaydi va oʻsha ikki belgi
orasini oʻlchaydi. Agar <b>5</b> metr chiqsa, burchak toʻgʻri.</p>

<p>Nega aynan shu uchta son? Javob — matematikadagi eng mashhur
formulada.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>toʻgʻri burchakli uchburchakning katetlarini gipotenuzasidan
      ajratasiz;</li>
    <li>Pifagor teoremasini yozasiz va gipotenuzani topasiz;</li>
    <li>nomaʼlum katetni ham topasiz;</li>
    <li>teorema nega ishlashini bitta chizma bilan isbotlaysiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Pifagor teoremasi</span>
  <span class="pe-chip pe-chip--o">a<sup>2</sup></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">b<sup>2</sup></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">c<sup>2</sup></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--adv">faqat toʻgʻri burchakli uchburchakda</span>
</div>

<h3>1. Katet va gipotenuza</h3>

<p>Bitta burchagi <b>toʻgʻri</b> (90°) boʻlgan uchburchak <b>toʻgʻri
burchakli</b> deyiladi (PM-61). Uning tomonlari ikki xil ish bajaradi,
shuning uchun ikki xil nom oladi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 215" role="img"
       aria-label="Toʻgʻri burchakli uchburchak: katetlari 3 va 4, gipotenuzasi 5">
    <polygon class="pm-fill" points="55,190 223,190 55,64"/>
    <polyline class="pm-ln" points="55,64 55,190 223,190" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="223" y1="190" x2="55" y2="64"/>
    <polyline class="pm-ln" points="70,190 70,175 55,175" fill="none"/>
    <text class="pm-lbl" x="16" y="132">a = 3</text>
    <text class="pm-lbl" x="127" y="210">b = 4</text>
    <text class="pm-lbl pm-lbl--hl" x="145" y="119">c = 5</text>
    <text class="pm-lbl" x="39" y="207">C</text>
    <text class="pm-lbl" x="231" y="207">B</text>
    <text class="pm-lbl" x="39" y="56">A</text>
  </svg>
  <figcaption>Toʻgʻri burchak C uchida. Uni hosil qilgan ikki tomon —
  katetlar (a va b), qarshisidagi eng uzun tomon — gipotenuza (c).</figcaption>
</figure>

<ul>
  <li><b>Katetlar</b> — toʻgʻri burchakni hosil qilgan ikkita tomon. Ular
    bir-biriga perpendikulyar.</li>
  <li><b>Gipotenuza</b> — toʻgʻri burchakning <b>qarshisidagi</b> tomon.</li>
</ul>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Gipotenuza har doim eng uzun tomon</p>
  <p>Buni PM-62 dan bilamiz: eng katta burchak qarshisida eng uzun tomon
  turadi. Toʻgʻri burchakli uchburchakda 90° eng katta burchak (qolgan
  ikkitasiga hammasi boʻlib 90° qoladi), demak uning qarshisidagi tomon eng
  uzun. Javobda gipotenuza katetdan kichik chiqsa — xato bor.</p>
</div>

<h3>2. Teorema</h3>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Pifagor teoremasi</p>
  <p>Toʻgʻri burchakli uchburchakda <b>katetlarning kvadratlari yigʻindisi
  gipotenuzaning kvadratiga teng</b>:
  <br><b>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></b>, bunda c —
  gipotenuza.</p>
</div>

<p>Ustaning uchburchagini tekshiramiz. Katetlar 3 va 4, gipotenuza 5:</p>

<div class="pe-ex">
  <p class="pe-ex__math">3<sup>2</sup> + 4<sup>2</sup> = 9 + 16 = 25 = 5<sup>2</sup></p>
  <p class="pe-ex__uz">Uch kvadrat qoʻshuv toʻrt kvadrat besh kvadratga
  teng — demak burchak haqiqatan toʻgʻri.</p>
  <p class="pe-ex__why">Kvadratlar PM-12 dan, ularning ildizi PM-13 dan
  tanish: 25 aniq kvadrat, √25 = 5.</p>
</div>

<h3>3. Nega ishlaydi? Ikkita joylashtirish</h3>

<p>Teoremani yodlash oson, lekin ishonch faqat isbotdan keladi. Isbot uchun
bitta katta kvadrat va toʻrtta bir xil uchburchak yetadi.</p>

<p>Kvadratning tomoni — <b>a + b</b>, yaʼni ikki katetning yigʻindisi.
Ichiga oʻsha toʻgʻri burchakli uchburchakdan toʻrtta bir xilini
joylashtiramiz — ikki xil usulda.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 220" role="img"
       aria-label="Tomoni a plus b boʻlgan kvadrat: toʻrtta uchburchakdan keyin oʻrtada c kvadrat qoladi">
    <rect class="pm-fill" x="45" y="12" width="189" height="189"/>
    <polygon class="pm-fill--hl" points="45,12 126,12 45,120"/>
    <polygon class="pm-fill--hl" points="126,12 234,12 234,93"/>
    <polygon class="pm-fill--hl" points="234,93 234,201 153,201"/>
    <polygon class="pm-fill--hl" points="153,201 45,201 45,120"/>
    <polyline class="pm-ln" points="126,12 234,93 153,201 45,120 126,12" fill="none"/>
    <rect class="pm-ln" x="45" y="12" width="189" height="189" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="127.5" y="112.5">c²</text>
    <text class="pm-lbl" x="79.5" y="10">a</text>
    <text class="pm-lbl" x="174" y="10">b</text>
    <text class="pm-lbl" x="240" y="57.5">a</text>
    <text class="pm-lbl" x="240" y="152">b</text>
  </svg>
  <figcaption>Birinchi joylashtirish: toʻrtta uchburchak burchaklarga
  qoʻyildi. Oʻrtada qolgan boʻsh joy — tomoni c boʻlgan kvadrat.</figcaption>
</figure>

<figure class="pm-fig">
  <svg viewBox="0 0 320 220" role="img"
       aria-label="Xuddi shu kvadrat: bu safar boʻsh joy a kvadrat va b kvadratdan iborat">
    <rect class="pm-fill" x="45" y="12" width="189" height="189"/>
    <polygon class="pm-fill--hl" points="126,12 234,12 126,93"/>
    <polygon class="pm-fill--hl" points="234,12 234,93 126,93"/>
    <polygon class="pm-fill--hl" points="45,93 126,93 45,201"/>
    <polygon class="pm-fill--hl" points="126,93 126,201 45,201"/>
    <line class="pm-ln" x1="234" y1="12" x2="126" y2="93"/>
    <line class="pm-ln" x1="126" y1="93" x2="45" y2="201"/>
    <rect class="pm-ln" x="45" y="12" width="81" height="81" fill="none"/>
    <rect class="pm-ln" x="126" y="93" width="108" height="108" fill="none"/>
    <rect class="pm-ln" x="45" y="12" width="189" height="189" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="75.5" y="58.5">a²</text>
    <text class="pm-lbl pm-lbl--hl" x="170" y="153">b²</text>
    <text class="pm-lbl" x="79.5" y="10">a</text>
    <text class="pm-lbl" x="174" y="10">b</text>
    <text class="pm-lbl" x="240" y="57.5">a</text>
    <text class="pm-lbl" x="240" y="152">b</text>
  </svg>
  <figcaption>Ikkinchi joylashtirish: xuddi oʻsha kvadrat, xuddi oʻsha
  toʻrtta uchburchak — endi boʻsh joy ikkita kvadrat: a² va b².</figcaption>
</figure>

<div class="pe-steps">
  <ol>
    <li>Ikkala chizmada ham <b>bitta xil katta kvadrat</b> turibdi —
      yuzalari teng.</li>
    <li>Ikkala chizmadan ham <b>bir xil toʻrtta uchburchak</b> olib
      tashlandi.</li>
    <li>Teng narsalardan teng narsa olib tashlansa, <b>qolgani ham
      teng</b>.</li>
    <li>Birinchi chizmada qolgani — <b>c<sup>2</sup></b>. Ikkinchisida —
      <b>a<sup>2</sup> + b<sup>2</sup></b>.</li>
    <li>Demak <b>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></b>.</li>
  </ol>
</div>

<p>Isbotda birorta ham murakkab qadam yoʻq: faqat «bir xil narsadan bir xil
narsani ayirdik» degan fikr — bu esa tenglama yechishda ishlatgan usulimizning
oʻzi (PM-36).</p>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Oʻzingiz qirqib koʻring</p>
  <p>Qalin qogʻozdan tomonlari 3 va 4 sm boʻlgan toʻrtta bir xil toʻgʻri
  burchakli uchburchak qirqing va tomoni 7 sm boʻlgan kvadratga ikki xil
  joylashtiring. Boʻsh joy bir chizmada bitta katta kvadrat, ikkinchisida
  ikkita kichik kvadrat boʻlib qoladi — teorema qoʻlingizda.</p>
</div>

<h3>4. Gipotenuzani topish</h3>

<p>Katetlari 6 va 8 boʻlgan toʻgʻri burchakli uchburchakning gipotenuzasi
qancha?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">c<sup>2</sup> = 6<sup>2</sup> + 8<sup>2</sup></span>
    <span class="pm-solve__why">Pifagor teoremasi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">c<sup>2</sup> = 36 + 64 = 100</span>
    <span class="pm-solve__why">Kvadratlarni hisobladik (PM-12)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">c = √100 = 10</span>
    <span class="pm-solve__why">Kvadrat ildiz oldik (PM-13)</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">c<sup>2</sup> = 100 degani c = 100 emas</p>
  <p>Eng koʻp uchraydigan xato shu: hisob 100 da toʻxtab qoladi. 100 — bu
  <b>kvadrat</b>, tomonning oʻzi emas. Oxirgi qadam har doim <b>ildiz
  chiqarish</b>: c = √100 = 10. Va bu 50 ham emas — ildiz chiqarish ikkiga
  boʻlish degani emas.</p>
</div>

<h3>5. Nomaʼlum katetni topish</h3>

<p>Endi teskari savol. Gipotenuza 13, bitta katet 5. Ikkinchi katet
qancha?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">5<sup>2</sup> + b<sup>2</sup> = 13<sup>2</sup></span>
    <span class="pm-solve__why">13 — gipotenuza, shuning uchun u yolgʻiz
    tomonda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">25 + b<sup>2</sup> = 169</span>
    <span class="pm-solve__why">Kvadratlarni hisobladik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">b<sup>2</sup> = 169 − 25 = 144</span>
    <span class="pm-solve__why">Ikki tomondan 25 ni ayirdik (PM-36)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">b = √144 = 12</span>
    <span class="pm-solve__why">Ildiz chiqardik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>5<sup>2</sup> + 12<sup>2</sup> = 25 + 144 = 169 = 13<sup>2</sup> ✓
  Gipotenuza (13) ikkala katetdan ham uzun ✓</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Qoʻshish yoki ayirish — qaysi biri?</p>
  <p>Bu faqat <b>nima nomaʼlum</b> ekaniga bogʻliq:
  <br>• gipotenuza nomaʼlum → katetlarning kvadratlarini <b>qoʻshamiz</b>;
  <br>• katet nomaʼlum → gipotenuzaning kvadratidan katetnikini
  <b>ayiramiz</b>.
  <br>Adashsangiz, javobni taqqoslang: gipotenuza katetdan uzun boʻlishi
  shart.</p>
</div>

<h3>6. Pifagor uchliklari</h3>

<p>Uchala tomoni ham butun son chiqadigan holatlar kam uchraydi va shuning
uchun qadrlanadi. Ular <b>Pifagor uchliklari</b> deyiladi — yod olsangiz,
koʻp masalani hisoblamasdan yechasiz.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Uchlik</th><th>Tekshiruv</th><th>Ikki barobari</th></tr>
  <tr><td>3, 4, 5</td><td>9 + 16 = 25</td><td>6, 8, 10</td></tr>
  <tr><td>5, 12, 13</td><td>25 + 144 = 169</td><td>10, 24, 26</td></tr>
  <tr><td>8, 15, 17</td><td>64 + 225 = 289</td><td>16, 30, 34</td></tr>
</table></div>

<p>Uchlikning har bir sonini bir xil songa koʻpaytirsangiz, yana uchlik
chiqadi: 3, 4, 5 → 9, 12, 15 (uch barobari). Usta ham shundan foydalanadi —
xona katta boʻlsa, 3-4-5 oʻrniga 6-8-10 metrni oʻlchaydi.</p>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Teskari teorema</p>
  <p>Agar uchburchakning tomonlari uchun <b>a<sup>2</sup> + b<sup>2</sup> =
  c<sup>2</sup></b> tenglik bajarilsa, u <b>toʻgʻri burchakli</b> boʻladi.
  Ustaning ruletkasi aynan shuni tekshiradi: 3, 4 va 5 chiqdimi — burchak
  toʻgʻri; 5 oʻrniga 5,2 chiqdimi — burchak toʻgʻri emas.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Dala boʻylab qisqa yoʻl.</b> Maktab dalasi toʻgʻri toʻrtburchak
shaklida: bir tomoni <b>60</b> metr, ikkinchisi <b>80</b> metr. Jasur bir
burchakdan qarama-qarshi burchakka boradi. U chetlab ham borishi mumkin,
kesib ham.</p>

<p><b>Nima soʻralyapti:</b> kesib borsa, necha metr tejaydi.</p>

<p><b>Reja:</b> toʻgʻri toʻrtburchakning burchaklari toʻgʻri burchak. Demak
ikki tomoni va diagonali toʻgʻri burchakli uchburchak hosil qiladi:
katetlar 60 va 80, gipotenuza — diagonal.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 + 80 = 140 m</span>
    <span class="pm-solve__why">Chetlab borgandagi yoʻl</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">d<sup>2</sup> = 60<sup>2</sup> + 80<sup>2</sup> = 3600 + 6400 = 10 000</span>
    <span class="pm-solve__why">Diagonal — gipotenuza</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">d = √10 000 = 100 m</span>
    <span class="pm-solve__why">Ildiz chiqardik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">140 − 100 = 40 m</span>
    <span class="pm-solve__why">Kesib borsa, 40 metr tejaydi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>60, 80, 100 — bu 3, 4, 5 uchligining yigirma barobari ✓
  Diagonal (100 m) ikkala tomondan ham uzun, lekin ularning yigʻindisidan
  (140 m) qisqa — uchburchak tengsizligi (PM-62) ham bajarildi.
  <br><b>Javob:</b> 40 metr tejaladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Katetlar 6 va 8 → gipotenuza 6 + 8 = 14</p>
  <p class="pe-fix__good">c<sup>2</sup> = 36 + 64 = 100, c = 10</p>
  <p class="pe-fix__why">Tomonlar emas, <b>kvadratlar</b> qoʻshiladi. 14
  javobi uchburchak tengsizligiga ham zid: 6 + 8 = 14 boʻlsa, uchburchak
  yassilanib qolardi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">c<sup>2</sup> = 100 → c = 50</p>
  <p class="pe-fix__good">c = √100 = 10</p>
  <p class="pe-fix__why">Kvadratning teskarisi — ildiz, ikkiga boʻlish emas.
  Tekshiring: 50 × 50 = 2500, 100 emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Gipotenuza 13, katet 5 → ikkinchi katet
    √(169 + 25) = √194</p>
  <p class="pe-fix__good">√(169 − 25) = √144 = 12</p>
  <p class="pe-fix__why">Gipotenuza — eng katta son, u yigʻindi tomonda
  turadi. Katet izlanayotganda <b>ayiriladi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Tomonlari 5, 6, 7 boʻlgan uchburchak:
    5<sup>2</sup> + 6<sup>2</sup> = 7<sup>2</sup></p>
  <p class="pe-fix__good">25 + 36 = 61, 49 esa emas — bu uchburchak toʻgʻri
    burchakli emas</p>
  <p class="pe-fix__why">Pifagor teoremasi <b>faqat</b> toʻgʻri burchakli
  uchburchakda ishlaydi. Boshqa uchburchakka qoʻllash — eng jimgina
  yashiringan xato.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Katetlari 9 va 12. Gipotenuza qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>15.</b> 81 + 144 = 225, √225 = 15. Bu 3-4-5 uchligining uch
    barobari.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Gipotenuzasi 25, bitta kateti 7. Ikkinchi katet
  qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>24.</b> 25<sup>2</sup> − 7<sup>2</sup> = 625 − 49 = 576,
    √576 = 24. Tekshirish: 49 + 576 = 625 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Tomonlari 8, 15 va 17 boʻlgan uchburchak toʻgʻri
  burchaklimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Ha.</b> Eng katta tomon 17. 64 + 225 = 289 va 17<sup>2</sup> = 289
    — tenglik bajarildi, demak teskari teoremaga koʻra burchak toʻgʻri.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Tomonlari 4, 5 va 6 boʻlgan uchburchak toʻgʻri
  burchaklimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yoʻq.</b> 16 + 25 = 41, 6<sup>2</sup> esa 36. 41 ≠ 36, demak
    tenglik bajarilmaydi. (41 &gt; 36 boʻlgani uchun eng katta burchak
    aslida 90° dan kichik — uchburchak oʻtkir burchakli.)</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Toʻgʻri burchakli uchburchakning ikkala kateti
  ham 5 ga teng. Gipotenuzasi qaysi ikki butun son orasida?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>7 va 8 orasida.</b> c<sup>2</sup> = 25 + 25 = 50. 50 aniq kvadrat
    emas: 49 &lt; 50 &lt; 64, demak √49 &lt; c &lt; √64, yaʼni
    7 &lt; c &lt; 8 (PM-13). Javob butun son chiqmasligi normal — Pifagor
    uchliklari kam uchraydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Sherbek televizor tanlayapti. Ekranning eni
  <b>120</b> sm, boʻyi <b>90</b> sm. Doʻkonchi «diagonali 150 sm» dedi. U
  toʻgʻri aytdimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Ha, toʻgʻri.</b> Ekranning burchaklari toʻgʻri burchak, demak
    diagonal — gipotenuza: 120<sup>2</sup> + 90<sup>2</sup> = 14 400 +
    8100 = 22 500, √22 500 = 150. Bu ham 3-4-5 uchligi, oʻttiz barobari:
    90, 120, 150.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Toʻgʻri burchakli uchburchak</b><span>bitta burchagi 90° boʻlgan
    uchburchak; ingl. right triangle</span></li>
  <li><b>Katet</b><span>toʻgʻri burchakni hosil qiluvchi tomon; ingl.
    leg</span></li>
  <li><b>Gipotenuza</b><span>toʻgʻri burchak qarshisidagi eng uzun tomon;
    ingl. hypotenuse</span></li>
  <li><b>Pifagor teoremasi</b><span>a² + b² = c²; ingl. Pythagorean
    theorem</span></li>
  <li><b>Teorema</b><span>isbotlangan qoida; ingl. theorem</span></li>
  <li><b>Isbot</b><span>qoida nega toʻgʻri ekanini koʻrsatuvchi mulohaza;
    ingl. proof</span></li>
  <li><b>Pifagor uchligi</b><span>uchala tomoni butun son boʻlgan holat,
    masalan 3-4-5; ingl. Pythagorean triple</span></li>
  <li><b>Teskari teorema</b><span>tenglik bajarilsa, burchak toʻgʻri; ingl.
    converse</span></li>
  <li><b>Diagonal</b><span>toʻrtburchakning qarama-qarshi uchlarini
    tutashtiruvchi kesma; ingl. diagonal</span></li>
  <li><b>Kvadrat ildiz</b><span>kvadratning teskari amali; ingl. square
    root</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Katetlar — toʻgʻri burchakni hosil qilgan tomonlar, gipotenuza —
      uning qarshisidagi eng uzun tomon.</li>
    <li>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup> — faqat toʻgʻri
      burchakli uchburchakda.</li>
    <li>Isbot: bitta kvadrat, toʻrtta uchburchak, ikki xil joylashtirish.</li>
    <li>Gipotenuza nomaʼlum → qoʻshamiz; katet nomaʼlum → ayiramiz.</li>
    <li>Oxirgi qadamni unutmang: c<sup>2</sup> topilgach, ildiz chiqariladi.</li>
    <li>3-4-5, 5-12-13, 8-15-17 va ularning barobarlari — yod olishga
      arziydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-65 — Pifagorning hayotdagi qoʻllanishi
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-65: Pifagorning hayotdagi qoʻllanishi",
        "category": "math",
        "order": 65,
        "summary": (
            "Narvon, tom balandligi, arqon, xaritadagi qiya masofa — "
            "hammasida bitta yashirin toʻgʻri burchakli uchburchak bor. Uni "
            "koʻrishni va javobni yaxlitlab tekshirishni oʻrganamiz."
        ),
        "stories": ["Narvon devorga suyalganda"],
        "content": """
<h2>PM-65: Pifagorning hayotdagi qoʻllanishi</h2>

<p>Oʻtgan darsda formulani oldik: a<sup>2</sup> + b<sup>2</sup> =
c<sup>2</sup>. Endi eng muhim savol qoladi — <b>uni qachon ishlatish
kerakligini qayerdan bilamiz?</b></p>

<p>Javob sodda: hayotda toʻgʻri burchak juda koʻp. Devor yerga tik turadi,
ustun tik qoqiladi, xaritaning katakchalari perpendikulyar. Toʻgʻri burchak
bor joyda Pifagor teoremasi ishlaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>hayotdagi vaziyatdan toʻgʻri burchakli uchburchakni ajratib
      olasiz;</li>
    <li>narvon, ustun va arqon masalalarini yechasiz;</li>
    <li>teng yonli tomning balandligini topasiz;</li>
    <li>javob butun chiqmaganda uni yaxlitlaysiz va mantiqiyligini
      tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qaysi tomon qaysi</span>
  <span class="pe-chip pe-chip--s">gipotenuza</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--aux">narvon · arqon · diagonal · qiya yoʻl</span>
</div>

<h3>1. Vaziyatni uchburchakka aylantirish</h3>

<p>Masalani oʻqib boʻlgach, hisoblashga shoshilmang. Avval toʻrtta qadam.</p>

<div class="pe-steps">
  <ol>
    <li><b>Chizing.</b> Kichkina boʻlsa ham, qoʻlda. Chizmasiz masala
      qiyinlashadi.</li>
    <li><b>Toʻgʻri burchakni toping.</b> Devor bilan yer, ustun bilan yer,
      xaritadagi ikki yoʻnalish — deyarli har doim shu yerda.</li>
    <li><b>Gipotenuzani belgilang.</b> U toʻgʻri burchakka <i>tegmaydigan</i>
      tomon: narvonning oʻzi, tortilgan arqon, qiya yoʻl.</li>
    <li><b>Nomaʼlumni qoʻying</b> va formulani yozing.</li>
  </ol>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Narvon hech qachon katet emas</p>
  <p>Eng koʻp uchraydigan xato shu. Narvon devorga <b>suyaladi</b> — u qiya
  turadi va toʻgʻri burchakni hosil qilmaydi. Toʻgʻri burchakni <b>devor
  bilan yer</b> hosil qiladi. Demak narvon — har doim gipotenuza, yaʼni
  uchtasining eng uzuni.</p>
</div>

<h3>2. Narvon devorga suyalganda</h3>

<p>Narvonning uzunligi <b>5</b> metr. Uning oyogʻi devordan <b>3</b> metr
narida turibdi. Narvonning uchi devorning qaysi balandligiga yetadi?</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 225" role="img"
       aria-label="Devorga suyalgan narvon: oyogʻi 3 metr, balandligi 4 metr, narvon 5 metr">
    <polygon class="pm-fill" points="70,200 190,200 70,40"/>
    <line class="pm-ln" x1="70" y1="200" x2="70" y2="22"/>
    <line class="pm-ln" x1="40" y1="200" x2="230" y2="200"/>
    <line class="pm-ln pm-ln--hl" x1="190" y1="200" x2="70" y2="40"/>
    <polyline class="pm-ln" points="85,200 85,185 70,185" fill="none"/>
    <text class="pm-lbl" x="18" y="125">4 m</text>
    <text class="pm-lbl" x="118" y="220">3 m</text>
    <text class="pm-lbl pm-lbl--hl" x="138" y="114">5 m</text>
    <text class="pm-lbl" x="12" y="30">devor</text>
    <text class="pm-lbl" x="236" y="196">yer</text>
  </svg>
  <figcaption>Devor yerga perpendikulyar — demak narvon, devor va yer
  toʻgʻri burchakli uchburchak hosil qiladi. Narvonning oʻzi —
  gipotenuza.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">a<sup>2</sup> + 3<sup>2</sup> = 5<sup>2</sup></span>
    <span class="pm-solve__why">Narvon (5) — gipotenuza, u yolgʻiz
    tomonda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">a<sup>2</sup> = 25 − 9 = 16</span>
    <span class="pm-solve__why">Katet izlanmoqda — ayiramiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">a = √16 = 4 m</span>
    <span class="pm-solve__why">Narvonning uchi 4 metr balandlikka
    yetadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>9 + 16 = 25 ✓ Balandlik (4 m) narvondan (5 m) qisqa — mantiqan ham
  toʻgʻri, chunki narvon qiya turibdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">Narvon 5 m, oyogʻi 4 m narida → a<sup>2</sup> = 25 − 16 = 9, a = 3 m</p>
  <p class="pe-ex__uz">Oyoq uzoqroqqa surilsa, narvon pastroqqa yetadi.</p>
  <p class="pe-ex__why">Narvonning uzunligi oʻzgarmadi — u faqat qiyaroq
  boʻldi.</p>
</div>

<h3>3. Tomning balandligi</h3>

<p>Bu yerda ikkita dars birlashadi: PM-63 (teng yonli uchburchak) va PM-64
(Pifagor).</p>

<p>Tomning asosi <b>12</b> metr, ikki yon yogʻochi esa <b>10</b> metrdan.
Tomning uchi shiftdan qancha baland?</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 210" role="img"
       aria-label="Teng yonli tom: asosi 12 metr, yon tomoni 10 metr, balandligi 8 metr">
    <polygon class="pm-fill" points="158,41 50,185 266,185"/>
    <polyline class="pm-ln" points="50,185 266,185 158,41 50,185" fill="none"/>
    <line class="pm-ln pm-ln--dash" x1="158" y1="41" x2="158" y2="185"/>
    <line class="pm-ln pm-ln--hl" x1="108.8" y1="116.6" x2="99.2" y2="109.4"/>
    <line class="pm-ln pm-ln--hl" x1="216.8" y1="109.4" x2="207.2" y2="116.6"/>
    <polyline class="pm-ln" points="171,185 171,172 158,172" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="58" y="113">10 m</text>
    <text class="pm-lbl pm-lbl--hl" x="224" y="113">10 m</text>
    <text class="pm-lbl" x="72" y="203">6 m</text>
    <text class="pm-lbl" x="202" y="203">6 m</text>
    <text class="pm-lbl" x="166" y="113">h = ?</text>
  </svg>
  <figcaption>Balandlik teng yonli uchburchakni ikkita bir xil toʻgʻri
  burchakli uchburchakka boʻladi. Har birining kateti — 6 m va h,
  gipotenuzasi — 10 m.</figcaption>
</figure>

<p>Tom uchburchagi teng yonli, lekin toʻgʻri burchakli emas — demak Pifagor
teoremasini unga <b>toʻgʻridan-toʻgʻri</b> qoʻllab boʻlmaydi. Uchidan
asosga perpendikulyar tushiramiz: u uchburchakni ikkita bir xil <b>toʻgʻri
burchakli</b> uchburchakka boʻladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 ÷ 2 = 6 m</span>
    <span class="pm-solve__why">Perpendikulyar asosni teng ikkiga
    boʻladi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">6<sup>2</sup> + h<sup>2</sup> = 10<sup>2</sup></span>
    <span class="pm-solve__why">Yon yogʻoch (10) — gipotenuza</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">h<sup>2</sup> = 100 − 36 = 64</span>
    <span class="pm-solve__why">Ayiramiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">h = √64 = 8 m</span>
    <span class="pm-solve__why">Tomning balandligi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Asosning oʻzi emas, YARMI</p>
  <p>Bu yerda eng koʻp yoʻqotiladigan ball shu. Toʻgʻri burchakli
  uchburchakning kateti — asosning <b>yarmi</b> (6), butun asos (12) emas.
  Butun asosni qoʻysangiz, h<sup>2</sup> = 100 − 144 = −44 chiqadi. Kvadrat
  manfiy boʻlmaydi — bu darhol xatoni koʻrsatuvchi belgi.</p>
</div>

<h3>4. Xaritadagi qiya masofa</h3>

<p>PM-46 da faqat gorizontal va vertikal kesmani oʻlchagan edik. Endi qiya
kesma ham qoʻlimizdan keladi.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 210" role="img"
       aria-label="Koordinata tekisligida A(1;2) va B(5;5) nuqtalar orasidagi masofa">
    <line class="pm-ln pm-ln--dash" x1="75" y1="190" x2="75" y2="10"/>
    <line class="pm-ln pm-ln--dash" x1="105" y1="190" x2="105" y2="10"/>
    <line class="pm-ln pm-ln--dash" x1="135" y1="190" x2="135" y2="10"/>
    <line class="pm-ln pm-ln--dash" x1="165" y1="190" x2="165" y2="10"/>
    <line class="pm-ln pm-ln--dash" x1="195" y1="190" x2="195" y2="10"/>
    <line class="pm-ln pm-ln--dash" x1="225" y1="190" x2="225" y2="10"/>
    <line class="pm-ln pm-ln--dash" x1="45" y1="160" x2="225" y2="160"/>
    <line class="pm-ln pm-ln--dash" x1="45" y1="130" x2="225" y2="130"/>
    <line class="pm-ln pm-ln--dash" x1="45" y1="100" x2="225" y2="100"/>
    <line class="pm-ln pm-ln--dash" x1="45" y1="70" x2="225" y2="70"/>
    <line class="pm-ln pm-ln--dash" x1="45" y1="40" x2="225" y2="40"/>
    <line class="pm-ln pm-ln--dash" x1="45" y1="10" x2="225" y2="10"/>
    <line class="pm-ln" x1="45" y1="190" x2="237" y2="190"/>
    <line class="pm-ln" x1="45" y1="190" x2="45" y2="4"/>
    <polyline class="pm-ln" points="75,130 195,130 195,40" fill="none"/>
    <line class="pm-ln pm-ln--hl" x1="75" y1="130" x2="195" y2="40"/>
    <polyline class="pm-ln" points="182,130 182,117 195,117" fill="none"/>
    <circle class="pm-pt" cx="75" cy="130" r="4"/>
    <circle class="pm-pt" cx="195" cy="40" r="4"/>
    <text class="pm-lbl" x="33" y="134">A(1; 2)</text>
    <text class="pm-lbl" x="203" y="44">B(5; 5)</text>
    <text class="pm-lbl" x="129" y="148">4</text>
    <text class="pm-lbl" x="203" y="89">3</text>
    <text class="pm-lbl pm-lbl--hl" x="109" y="79">d = ?</text>
    <text class="pm-lbl" x="31" y="206">O</text>
  </svg>
  <figcaption>Gorizontal qadam 4, vertikal qadam 3. Ular toʻgʻri burchak
  hosil qiladi — demak toʻgʻridan-toʻgʻri masofa gipotenuza.</figcaption>
</figure>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">|5 − 1| = 4</span>
    <span class="pm-solve__why">Gorizontal qadam (PM-46)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">|5 − 2| = 3</span>
    <span class="pm-solve__why">Vertikal qadam</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">d<sup>2</sup> = 4<sup>2</sup> + 3<sup>2</sup> = 16 + 9 = 25</span>
    <span class="pm-solve__why">Ikki qadam toʻgʻri burchak hosil qiladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">d = √25 = 5 birlik</span>
    <span class="pm-solve__why">Ikki nuqta orasidagi qiya masofa</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Nega qadamlarni qoʻshib yuborib boʻlmaydi</p>
  <p>4 + 3 = 7 — bu <b>katakchalar boʻylab</b> yurgandagi yoʻl: avval oʻngga,
  keyin yuqoriga. Toʻgʻridan-toʻgʻri masofa esa 5. Farq — 2 birlik, va u
  PM-62 dagi qoidaning oʻzi: toʻgʻri yoʻl har doim qisqaroq.</p>
</div>

<h3>5. Javob butun chiqmasa</h3>

<p>Hayotdagi sonlar Pifagor uchligiga kamdan kam toʻgʻri keladi. Narvon
<b>6</b> metr, oyogʻi devordan <b>2</b> metr narida boʻlsin.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">a<sup>2</sup> = 36 − 4 = 32</span>
    <span class="pm-solve__why">Odatdagidek ayiramiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">25 &lt; 32 &lt; 36 → 5 &lt; a &lt; 6</span>
    <span class="pm-solve__why">32 ikki aniq kvadrat orasida (PM-13)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5,6<sup>2</sup> = 31,36 &nbsp; 5,7<sup>2</sup> = 32,49</span>
    <span class="pm-solve__why">Ikkita oʻnlikni sinab koʻrdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">a ≈ 5,7 m</span>
    <span class="pm-solve__why">32 soni 32,49 ga yaqinroq (PM-14)</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Javob butun chiqmasa — bu xato emas</p>
  <p>Koʻp oʻquvchi «√32 butun chiqmadi, demak adashdim» deb qaytadan
  hisoblaydi. Aslida bu normal: butun javob faqat Pifagor uchliklarida
  chiqadi. Bunday paytda javob <b>taxminiy</b> yoziladi va <b>≈</b> belgisi
  qoʻyiladi.</p>
</div>

<h3>Matnli masala</h3>

<p><b>Ustunga tortilgan arqon.</b> Karim aka hovliga <b>12</b> metrli ustun
tikladi. Ustun qulamasligi uchun uning eng uchidan yerga arqon tortadi.
Arqonning yerdagi uchi ustun tagidan <b>5</b> metr narida qoqiladi. Shunday
arqondan <b>3</b> ta kerak, arqonning bir metri <b>6000</b> soʻm turadi.</p>

<p><b>Nima soʻralyapti:</b> uchala arqon uchun qancha pul kerak.</p>

<p><b>Reja:</b> ustun yerga tik — demak toʻgʻri burchak ustunning tagida.
Arqon qiya, demak u gipotenuza. Avval bitta arqonni topamiz, keyin
uchtasini, keyin narxini.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">c<sup>2</sup> = 12<sup>2</sup> + 5<sup>2</sup></span>
    <span class="pm-solve__why">Katetlar — ustun (12) va yerdagi masofa (5)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">c<sup>2</sup> = 144 + 25 = 169</span>
    <span class="pm-solve__why">Gipotenuza nomaʼlum — qoʻshamiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">c = √169 = 13 m</span>
    <span class="pm-solve__why">Bitta arqonning uzunligi (5-12-13 uchligi)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">13 × 3 = 39 m</span>
    <span class="pm-solve__why">Uchta arqon</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">39 × 6000 = 234 000 soʻm</span>
    <span class="pm-solve__why">Umumiy narx</span>
  </div>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Arqon ustundan (12 m) uzun, lekin 12 + 5 = 17 m dan qisqa boʻlishi
  kerak (PM-62). 13 m shu oraliqda ✓ Narx esa 40 × 6000 = 240 000 atrofida
  — 234 000 soʻm mantiqiy.</span>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>144 + 25 = 169 = 13<sup>2</sup> ✓
  <br><b>Javob:</b> 39 metr arqon, 234 000 soʻm.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Narvon 5 m, oyogʻi 3 m → balandlik
    √(25 + 9) = √34</p>
  <p class="pe-fix__good">√(25 − 9) = √16 = 4 m</p>
  <p class="pe-fix__why">Narvon — gipotenuza, katet emas. Javob narvonning
  oʻzidan uzun chiqsa (√34 ≈ 5,8), darhol xato deb biling.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Tom: asos 12, yon 10 → h<sup>2</sup> = 100 − 144</p>
  <p class="pe-fix__good">Asosning yarmi olinadi: h<sup>2</sup> = 100 − 36 = 64</p>
  <p class="pe-fix__why">Perpendikulyar teng yonli uchburchakni ikkiga
  boʻladi, shuning uchun katet — 6, 12 emas. Kvadrat manfiy chiqishi
  mumkin emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">A(1; 2) va B(5; 5) orasidagi masofa: 4 + 3 = 7</p>
  <p class="pe-fix__good">√(16 + 9) = √25 = 5</p>
  <p class="pe-fix__why">4 + 3 — katakchalar boʻylab yurgandagi yoʻl.
  Toʻgʻridan-toʻgʻri masofa esa gipotenuza va u har doim qisqaroq.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Katetlar 60 sm va 0,8 m → c<sup>2</sup> = 3600 + 0,64</p>
  <p class="pe-fix__good">Avval bir birlikka keltiring: 60 sm = 0,6 m →
    0,36 + 0,64 = 1, c = 1 m</p>
  <p class="pe-fix__why">Har xil birlikdagi sonlarni qoʻshib boʻlmaydi.
  Birinchi qadam — hammasini metrga (yoki hammasini santimetrga)
  aylantirish.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Narvonning uzunligi 10 m, oyogʻi devordan 6 m
  narida. Narvonning uchi qanday balandlikka yetadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>8 m.</b> a<sup>2</sup> = 100 − 36 = 64, a = 8. Bu 3-4-5
    uchligining ikki barobari: 6, 8, 10.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Teng yonli tomning asosi 16 m, yon yogʻochlari
  17 m dan. Tomning balandligi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>15 m.</b> Asosning yarmi: 16 ÷ 2 = 8. h<sup>2</sup> = 289 − 64 =
    225, h = √225 = 15. Bu 8-15-17 uchligi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. A(2; 1) va B(10; 7) nuqtalar orasidagi masofani
  toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10 birlik.</b> Gorizontal qadam |10 − 2| = 8, vertikal qadam
    |7 − 1| = 6. d<sup>2</sup> = 64 + 36 = 100, d = 10.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Bayroq ustuni 9 m balandlikda. Uning uchidan
  yerga arqon tortilgan; arqonning yerdagi uchi ustundan 12 m narida.
  Arqonning uzunligi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>15 m.</b> Arqon — gipotenuza: c<sup>2</sup> = 81 + 144 = 225,
    c = 15. Diqqat: bu safar arqon ustundan ham, yerdagi masofadan ham
    uzun — chunki u gipotenuza.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Kvadrat shaklidagi maydonning tomoni 10 m. Uning
  diagonali qaysi ikki butun son orasida?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>14 va 15 orasida.</b> d<sup>2</sup> = 100 + 100 = 200.
    14<sup>2</sup> = 196, 15<sup>2</sup> = 225, demak 196 &lt; 200 &lt; 225
    va 14 &lt; d &lt; 15. Aniqrogʻi d ≈ 14,1.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Bekzod velosipedda uydan 300 m sharqqa, soʻng
  400 m shimolga yurdi. Agar toʻgʻridan-toʻgʻri qaytsa, necha metr yoʻl
  tejaydi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>200 m tejaydi.</b> Sharq va shimol perpendikulyar yoʻnalishlar,
    demak toʻgʻri qaytish yoʻli — gipotenuza: 300<sup>2</sup> +
    400<sup>2</sup> = 90 000 + 160 000 = 250 000, √250 000 = 500 m. Borgan
    yoʻli esa 300 + 400 = 700 m. Farq: 700 − 500 = 200 m.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Gipotenuza</b><span>qiya tomon: narvon, arqon, diagonal; ingl.
    hypotenuse</span></li>
  <li><b>Katet</b><span>toʻgʻri burchakni hosil qiluvchi tomon: devor, yer;
    ingl. leg</span></li>
  <li><b>Balandlik</b><span>uchdan asosga tushirilgan perpendikulyar; ingl.
    height</span></li>
  <li><b>Diagonal</b><span>qarama-qarshi burchaklarni tutashtiruvchi kesma;
    ingl. diagonal</span></li>
  <li><b>Qiya masofa</b><span>ikki nuqta orasidagi toʻgʻri chiziq; ingl.
    straight-line distance</span></li>
  <li><b>Taxminiy javob</b><span>≈ belgisi bilan yoziladigan yaxlitlangan
    natija; ingl. approximation</span></li>
  <li><b>Yaxlitlash</b><span>javobni yaqin oʻnlikka keltirish; ingl.
    rounding</span></li>
  <li><b>Birliklarni keltirish</b><span>hamma sonni bir xil oʻlchovga
    oʻtkazish; ingl. unit conversion</span></li>
  <li><b>Chizma</b><span>masalani koʻrsatuvchi sxema; ingl. diagram</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Toʻgʻri burchakni toping — devor bilan yer, ustun bilan yer,
      xaritadagi ikki yoʻnalish.</li>
    <li>Narvon, arqon, diagonal va qiya yoʻl — har doim gipotenuza.</li>
    <li>Teng yonli tomda katet — asosning <b>yarmi</b>.</li>
    <li>Koordinatada: qadamlarni qoʻshmang, kvadratlarini qoʻshing.</li>
    <li>Javob butun chiqmasa — yaxlitlang va ≈ belgisini qoʻying.</li>
    <li>Birliklar bir xil boʻlsin; javobni har doim mantiqan tekshiring.</li>
  </ul>
</div>
""",
    },
]
