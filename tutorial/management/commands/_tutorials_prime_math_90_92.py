# -*- coding: utf-8 -*-
"""Prime Math — darslar 90–92 (ish va unumdorlik; aralashma; narx-miqdor).

**Blok G: Matnli masalalar ustaxonasi (85–94).**
Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md

  mashqlar — practice/management/commands/_practice_pm_90_92.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_90_92.py

⚠️ Uchlikning ichki mantigʻi — BIR XIL UCHLIK UCHINCHI MARTA:
     PM-88  S       = v          × t
     PM-90  ish     = unumdorlik × vaqt
     PM-92  qiymat  = narx       × miqdor
   PM-92 shuni ochiq aytadi va uchalasini bitta jadvalga yigʻadi.
   PM-90 esa PM-88/89 dagi «tezliklar qoʻshiladimi?» savolini
   takrorlaydi: birga ishlaganda UNUMDORLIKLAR qoʻshiladi, vaqtlar
   emas — bu darsning eng katta xatosi shu yerda.

⚠️ Kumulyativ chegaralar:
  • PM-90 — butun ish = 1 gʻoyasi, unumdorlik 1/t, birgalikda ishlash.
    ⛔ Hovuzdan suv ketishi (manfiy unumdorlik) kursda yoʻq;
  • PM-91 — sof modda = massa × foiz. Aralashtirish, suv qoʻshish va
    bugʻlatish. ⛔ Qotishmadagi uch komponent va «alligatsiya» qoidasi
    YOʻQ — hammasi jadval + tenglama bilan;
  • PM-92 — birlik narx va uni taqqoslash quroli sifatida ishlatish.
    ⛔ Foizli chegirma qayta hisoblanmaydi (PM-26 da boʻlgan), faqat
    eslatib oʻtiladi.
  • Faol ishlatiladi: kasr qoʻshish va umumiy maxraj (PM-17), kasrga
    boʻlish (PM-18), foiz (PM-23…26), tenglama (PM-36/37), jadval
    (PM-86), S = v·t (PM-88).

⚠️ Arifmetika darvozasi: scratchpad/verify_pm_90_92.py hamma sonni
   qayta hisoblaydi. Ish masalalari FORMULA bilan emas, kun-baqun
   BAJARILGAN ULUSH yigʻindisi bilan tekshiriladi; aralashmalar esa
   sof modda balansi bilan (kirgan sof modda = chiqqan sof modda).

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_90_92.py --author=prime
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
    # PM-90 — ish va unumdorlik
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-90: Ish va unumdorlik masalalari",
        "category": "math",
        "order": 90,
        "summary": (
            "Butun ishni 1 deb olsak, hamma narsa joyiga tushadi: 6 kunda "
            "bitiradigan usta bir kunda ishning 1/6 qismini qiladi. Birga "
            "ishlaganda unumdorliklar qoʻshiladi, vaqtlar emas."
        ),
        "stories": ["Ikki usta, bitta devor"],
        "content": """
<h2>PM-90: Ish va unumdorlik masalalari</h2>

<p>Bir usta devorni 6 kunda quradi. Ikkinchisi xuddi shu devorni
12 kunda quradi. Ikkalasi birga ishlasa, necha kunda bitiradi?</p>

<p>Koʻpchilik darrov 18 deydi (6 + 12) yoki 9 deydi (oʻrtachasi).
Ikkalasi ham notoʻgʻri — va ikkalasi ham <b>mantiqan</b> notoʻgʻri:
yordamchi kelganda ish <b>tezroq</b> bitishi kerak, sekinroq emas.
Toʻgʻri javob 6 kundan ham kam.</p>

<p>Bu darsda shu masalaning kaliti bor va u juda oddiy: butun ishni
<b>1</b> deb olamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>butun ishni 1 deb olishni oʻrganasiz;</li>
    <li>unumdorlikni 1 ÷ vaqt bilan topasiz;</li>
    <li>birgalikda ishlashda unumdorliklarni qoʻshasiz;</li>
    <li>bosqichma-bosqich bajarilgan ishni jadvalga solasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ish uchligi</span>
  <span class="pe-chip pe-chip--s">ish</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">unumdorlik</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">vaqt</span>
</div>

<h3>1. Butun ishni 1 deb olamiz</h3>

<p>Devor nechta gʻishtdan iborat? Bilmaymiz — va bilishimiz shart
emas. Masalada devorning kattaligi berilmagan, demak u javobga taʼsir
qilmaydi.</p>

<p>Shuning uchun butun ishni <b>1</b> deb belgilaymiz: bitta devor,
bitta hovuz, bitta buyurtma. Endi bir kunda bajarilgan ulushni
yozish mumkin.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Unumdorlik — bir kunda bajarilgan ulush</span>
  <span class="pe-chip pe-chip--s">u</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">1</span>
  <span class="pe-op">÷</span>
  <span class="pe-chip pe-chip--o">t</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">u = 1 ÷ 6 = <sup>1</sup>/<sub>6</sub></p>
  <p class="pe-ex__uz">Devorni 6 kunda bitiradigan usta bir kunda
  devorning oltidan bir qismini quradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">u = 1 ÷ 12 = <sup>1</sup>/<sub>12</sub></p>
  <p class="pe-ex__uz">Ikkinchi usta bir kunda oʻn ikkidan bir
  qismini quradi — yaʼni ikki barobar sekin.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Bu — PM-88 dagi uchlikning oʻzi</p>
  <p>S = v × t da tezlik «bir soatda bosilgan masofa» edi. Bu yerda
  unumdorlik — «bir kunda bajarilgan ish». Formula bir xil, faqat
  nomlari boshqa: <b>ish = unumdorlik × vaqt</b>.</p>
</div>

<h3>2. Birgalikda ishlash — unumdorliklar qoʻshiladi</h3>

<p>Ikki usta birga ishlasa, bir kunda ikkalasining hissasi
qoʻshiladi.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">1-usta</span>
    <span class="pm-model__bar" style="width:17%">2/12</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">2-usta</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:8%">1/12</span>
  </div>
  <p class="pm-model__tot">Bir kunda birgalikda: 3/12 = 1/4 qism</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step"><sup>1</sup>/<sub>6</sub> + <sup>1</sup>/<sub>12</sub></span>
    <span class="pm-solve__why">Bir kunlik hissalar qoʻshildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">= <sup>2</sup>/<sub>12</sub> + <sup>1</sup>/<sub>12</sub> = <sup>3</sup>/<sub>12</sub> = <sup>1</sup>/<sub>4</sub></span>
    <span class="pm-solve__why">Umumiy maxraj 12 (PM-17)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">t = 1 ÷ <sup>1</sup>/<sub>4</sub> = 4 kun</span>
    <span class="pm-solve__why">Butun ish shu unumdorlikda</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>4 kunda birinchi usta 4 × <sup>1</sup>/<sub>6</sub> =
  <sup>2</sup>/<sub>3</sub>, ikkinchisi 4 × <sup>1</sup>/<sub>12</sub> =
  <sup>1</sup>/<sub>3</sub> qismini quradi.
  <sup>2</sup>/<sub>3</sub> + <sup>1</sup>/<sub>3</sub> = 1 ✓ — devor
  roppa-rosa bitgan.
  <br><b>Javob:</b> birga ishlasa 4 kunda bitiradi.</p>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Eng katta xato: vaqtlarni qoʻshish</p>
  <p>6 + 12 = 18 kun degan javob shuni bildiradiki, yordamchi kelgach
  ish uch barobar sekinlashgan. Bu maʼnosiz. Javob har doim <b>eng tez
  ishlovchining vaqtidan ham kichik</b> boʻlishi kerak — bu yerda
  6 kundan kam. 4 &lt; 6 ✓ Javobni shu bilan darrov tekshiring.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Unumdorlikni topgach toʻxtamang</p>
  <p><sup>1</sup>/<sub>4</sub> — bu <b>bir kunlik ulush</b>, javob
  emas. Vaqtni topish uchun uni teskari qilish kerak: 1 ÷
  <sup>1</sup>/<sub>4</sub> = 4. Javob «<sup>1</sup>/<sub>4</sub> kun»
  emas, «4 kun».</p>
</div>

<h3>3. Teskari masala — bittasining vaqtini topish</h3>

<p><b>Masala.</b> Bir usta ishni 12 kunda bitiradi. Ikkovi birga
ishlasa, 4 kunda bitiradi. Ikkinchi usta yolgʻiz necha kunda
bitiradi?</p>

<p>Endi qoʻshish emas, <b>ayirish</b> kerak: umumiy unumdorlikdan
birinchisiniki ayiriladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Birgalikdagi unumdorlik: 1 ÷ 4 = <sup>1</sup>/<sub>4</sub></span>
    <span class="pm-solve__why">Bir kunda birgalikda shuncha qilinadi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step"><sup>1</sup>/<sub>4</sub> − <sup>1</sup>/<sub>12</sub> = <sup>3</sup>/<sub>12</sub> − <sup>1</sup>/<sub>12</sub> = <sup>2</sup>/<sub>12</sub></span>
    <span class="pm-solve__why">Birinchisining hissasi ayirildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">= <sup>1</sup>/<sub>6</sub> → t = 6 kun</span>
    <span class="pm-solve__why">Qisqartirdik va teskari qildik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p><sup>1</sup>/<sub>12</sub> + <sup>1</sup>/<sub>6</sub> =
  <sup>1</sup>/<sub>12</sub> + <sup>2</sup>/<sub>12</sub> =
  <sup>3</sup>/<sub>12</sub> = <sup>1</sup>/<sub>4</sub> ✓ — birgalikda
  4 kun chiqadi, masaladagidek.
  <br><b>Javob:</b> ikkinchi usta yolgʻiz 6 kunda bitiradi.</p>
</div>

<h3>4. Trubalar ham xuddi shunday</h3>

<p><b>Masala.</b> Bir truba hovuzni 3 soatda toʻldiradi, ikkinchisi
6 soatda. Ikkalasi birga ochilsa, necha soatda toʻladi?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step"><sup>1</sup>/<sub>3</sub> + <sup>1</sup>/<sub>6</sub> = <sup>2</sup>/<sub>6</sub> + <sup>1</sup>/<sub>6</sub> = <sup>3</sup>/<sub>6</sub> = <sup>1</sup>/<sub>2</sub></span>
    <span class="pm-solve__why">Bir soatda hovuzning yarmi toʻladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">t = 1 ÷ <sup>1</sup>/<sub>2</sub> = 2 soat</span>
    <span class="pm-solve__why">2 &lt; 3 — eng tez trubadan ham kam ✓</span>
  </div>
</div>

<h3>Matnli masala</h3>

<p>Bir brigada uyni 8 kunda taʼmirlaydi, ikkinchisi xuddi shu ishni
24 kunda bajaradi. Avval birinchi brigada 4 kun yolgʻiz ishladi.
Keyin ikkinchi brigada ham qoʻshildi va ish oxirigacha birga
davom etdi.</p>

<p><b>Ish jami necha kunda tugadi?</b></p>

<p><b>Reja:</b> ish ikki bosqichdan iborat — jadval tuzamiz
(PM-86). Avval birinchi bosqichda qancha bajarilganini topamiz, keyin
qolganini birgalikdagi unumdorlikka boʻlamiz.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Bosqich</th><th>Unumdorlik</th><th>Bajarilgan ulush</th></tr>
  <tr><td>1-brigada, 4 kun yolgʻiz</td>
    <td class="pm-word__sym"><sup>1</sup>/<sub>8</sub></td>
    <td>4 × <sup>1</sup>/<sub>8</sub> = <sup>1</sup>/<sub>2</sub></td></tr>
  <tr><td>Ikkalasi birga</td>
    <td class="pm-word__sym"><sup>1</sup>/<sub>8</sub> + <sup>1</sup>/<sub>24</sub> = <sup>1</sup>/<sub>6</sub></td>
    <td>qolgan <sup>1</sup>/<sub>2</sub></td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 × <sup>1</sup>/<sub>8</sub> = <sup>1</sup>/<sub>2</sub></span>
    <span class="pm-solve__why">Birinchi brigada yarmini bajardi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qoldi: 1 − <sup>1</sup>/<sub>2</sub> = <sup>1</sup>/<sub>2</sub></span>
    <span class="pm-solve__why">Butundan bajarilgani ayirildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step"><sup>1</sup>/<sub>8</sub> + <sup>1</sup>/<sub>24</sub> = <sup>3</sup>/<sub>24</sub> + <sup>1</sup>/<sub>24</sub> = <sup>4</sup>/<sub>24</sub> = <sup>1</sup>/<sub>6</sub></span>
    <span class="pm-solve__why">Birgalikdagi unumdorlik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step"><sup>1</sup>/<sub>2</sub> ÷ <sup>1</sup>/<sub>6</sub> = <sup>1</sup>/<sub>2</sub> × 6 = 3 kun</span>
    <span class="pm-solve__why">Kasrga boʻlish — teskarisiga koʻpaytirish (PM-18)</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">4 + 3 = 7 kun</span>
    <span class="pm-solve__why">Ikki bosqich qoʻshildi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Birinchi brigada boshdan oxirigacha 7 kun ishladi:
  7 × <sup>1</sup>/<sub>8</sub> = <sup>7</sup>/<sub>8</sub>.
  Ikkinchisi faqat 3 kun: 3 × <sup>1</sup>/<sub>24</sub> =
  <sup>1</sup>/<sub>8</sub>.
  <br><sup>7</sup>/<sub>8</sub> + <sup>1</sup>/<sub>8</sub> = 1 ✓ — ish
  roppa-rosa tugagan.
  <br><b>Javob:</b> ish 7 kunda tugadi.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Birinchi brigada yolgʻiz ishlaganda 8 kun kerak boʻlardi.
  Yordam kelgani uchun javob 8 dan kichik boʻlishi shart. 7 &lt; 8 ✓
  Lekin ikkinchi brigada juda sekin (24 kun), shuning uchun katta
  tejash boʻlmadi — bor-yoʻgʻi bir kun.</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">6 kun va 12 kun → birga 6 + 12 = 18 kun</p>
  <p class="pe-fix__good">4 kun</p>
  <p class="pe-fix__why">Vaqtlar qoʻshilmaydi. Yordamchi kelganda ish
  tezlashadi — javob 6 dan <b>kichik</b> boʻlishi kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Birga ishlasa (6 + 12) ÷ 2 = 9 kun</p>
  <p class="pe-fix__good">4 kun</p>
  <p class="pe-fix__why">Oʻrtachasi ham 6 dan katta — demak baribir
  maʼnosiz. Qoʻshiladigan narsa vaqt emas,
  <b>unumdorlik</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad"><sup>1</sup>/<sub>6</sub> +
  <sup>1</sup>/<sub>12</sub> = <sup>2</sup>/<sub>18</sub></p>
  <p class="pe-fix__good"><sup>2</sup>/<sub>12</sub> +
  <sup>1</sup>/<sub>12</sub> = <sup>3</sup>/<sub>12</sub></p>
  <p class="pe-fix__why">Kasr qoʻshishda maxrajlar qoʻshilmaydi
  (PM-17). Umumiy maxrajga keltiriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Javob: <sup>1</sup>/<sub>4</sub> kun</p>
  <p class="pe-fix__good">Javob: 4 kun</p>
  <p class="pe-fix__why"><sup>1</sup>/<sub>4</sub> — bir kunlik ulush.
  Vaqt uning teskarisi: 1 ÷ <sup>1</sup>/<sub>4</sub> = 4.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Usta ishni 5 kunda bitiradi. Bir kunda
  ishning qanday qismini bajaradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b><sup>1</sup>/<sub>5</sub> qismini.</b> Butun ish 1 ga teng,
    unumdorlik 1 ÷ 5 = <sup>1</sup>/<sub>5</sub>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Ikki ishchi: biri 10 kunda, ikkinchisi
  10 kunda bitiradi. Birga necha kunda bitirishadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5 kunda.</b> <sup>1</sup>/<sub>10</sub> +
    <sup>1</sup>/<sub>10</sub> = <sup>2</sup>/<sub>10</sub> =
    <sup>1</sup>/<sub>5</sub>, demak 5 kun. Bir xil tezlikdagi ikki
    kishi ishni roppa-rosa ikki barobar tez bitiradi — mantiqiy.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Ikki truba: biri 4 soatda, ikkinchisi
  12 soatda toʻldiradi. Birga necha soatda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 soatda.</b> <sup>1</sup>/<sub>4</sub> +
    <sup>1</sup>/<sub>12</sub> = <sup>3</sup>/<sub>12</sub> +
    <sup>1</sup>/<sub>12</sub> = <sup>4</sup>/<sub>12</sub> =
    <sup>1</sup>/<sub>3</sub> → 3 soat. Tekshirish: 3 &lt; 4 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Bir usta 15 kunda bitiradi, ikkovi birga
  6 kunda. Ikkinchisi yolgʻiz necha kunda bitiradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>10 kunda.</b> <sup>1</sup>/<sub>6</sub> −
    <sup>1</sup>/<sub>15</sub> = <sup>5</sup>/<sub>30</sub> −
    <sup>2</sup>/<sub>30</sub> = <sup>3</sup>/<sub>30</sub> =
    <sup>1</sup>/<sub>10</sub> → 10 kun. Tekshirish:
    <sup>1</sup>/<sub>15</sub> + <sup>1</sup>/<sub>10</sub> =
    <sup>2</sup>/<sub>30</sub> + <sup>3</sup>/<sub>30</sub> =
    <sup>1</sup>/<sub>6</sub> ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Uch ishchi: har biri ishni 9 kunda bitiradi.
  Uchalasi birga necha kunda bitirishadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3 kunda.</b> <sup>1</sup>/<sub>9</sub> × 3 =
    <sup>3</sup>/<sub>9</sub> = <sup>1</sup>/<sub>3</sub> → 3 kun.
    Uch barobar koʻp kuch — uch barobar tez.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Ishchi ishni 20 kunda bitiradi. U 5 kun
  ishladi. Ishning qanday qismi qoldi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b><sup>3</sup>/<sub>4</sub> qismi.</b> Bajargani
    5 × <sup>1</sup>/<sub>20</sub> = <sup>1</sup>/<sub>4</sub>.
    Qolgani 1 − <sup>1</sup>/<sub>4</sub> = <sup>3</sup>/<sub>4</sub>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Bir brigada ishni 10 kunda bajaradi,
  ikkinchisi 15 kunda. Avval ikkalasi 3 kun birga ishladi, keyin
  birinchisi ketdi. Ikkinchisi qolgan ishni necha kunda tugatadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>7,5 kunda.</b> Birgalikdagi unumdorlik:
    <sup>1</sup>/<sub>10</sub> + <sup>1</sup>/<sub>15</sub> =
    <sup>3</sup>/<sub>30</sub> + <sup>2</sup>/<sub>30</sub> =
    <sup>1</sup>/<sub>6</sub>. 3 kunda: 3 × <sup>1</sup>/<sub>6</sub> =
    <sup>1</sup>/<sub>2</sub>. Qolgani <sup>1</sup>/<sub>2</sub>.
    Ikkinchisining unumdorligi <sup>1</sup>/<sub>15</sub>, demak
    <sup>1</sup>/<sub>2</sub> ÷ <sup>1</sup>/<sub>15</sub> = 7,5 kun.
    Tekshirish: 3 × <sup>1</sup>/<sub>10</sub> +
    10,5 × <sup>1</sup>/<sub>15</sub> = 0,3 + 0,7 = 1 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Ish</b><span>bajarilishi kerak boʻlgan butun vazifa; ingl.
    work</span></li>
  <li><b>Unumdorlik</b><span>bir vaqt birligida bajarilgan ish; ingl.
    work rate</span></li>
  <li><b>Butun ish</b><span>1 deb olinadigan toʻliq vazifa; ingl. whole
    job</span></li>
  <li><b>Ulush</b><span>ishning bajarilgan qismi; ingl. share</span></li>
  <li><b>Birgalikda ishlash</b><span>unumdorliklar qoʻshiladigan holat;
    ingl. working together</span></li>
  <li><b>Teskari son</b><span>1 ÷ son; unumdorlikdan vaqtga oʻtish;
    ingl. reciprocal</span></li>
  <li><b>Umumiy maxraj</b><span>kasrlarni qoʻshish uchun keltiriladigan
    maxraj; ingl. common denominator</span></li>
  <li><b>Bosqich</b><span>ishning bir xil tarkib bilan bajarilgan qismi;
    ingl. stage</span></li>
  <li><b>Brigada</b><span>birga ishlaydigan ishchilar guruhi; ingl.
    team</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Butun ishni 1 deb oling — devorning kattaligi kerak emas.</li>
    <li>Unumdorlik = 1 ÷ vaqt.</li>
    <li>Birga ishlaganda <b>unumdorliklar</b> qoʻshiladi, vaqtlar
      emas.</li>
    <li>Vaqtni topish uchun unumdorlikni teskari qiling.</li>
    <li>Javob eng tez ishlovchining vaqtidan kichik boʻlishi
      shart.</li>
    <li>Bosqichli ish — jadval: har bosqichda bajarilgan ulush
      yoziladi.</li>
    <li>Tekshirish: hammaning bajargan ulushi yigʻindisi roppa-rosa
      1 boʻlsin.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-91 — aralashma va foizli masalalar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-91: Aralashma va foizli masalalar",
        "category": "math",
        "order": 91,
        "summary": (
            "Aralashmada foizlar qoʻshilmaydi — sof modda qoʻshiladi. "
            "Shu bitta jumla suv qoʻshish, bugʻlatish va ikki eritmani "
            "aralashtirish masalalarining hammasini yechadi."
        ),
        "stories": ["Choyga qancha shakar"],
        "content": """
<h2>PM-91: Aralashma va foizli masalalar</h2>

<p>20% li tuzli suvga 45% li tuzli suv qoʻshildi. Yangi eritma necha
foizli boʻladi?</p>

<p>65% deb javob berish juda oson — va butunlay xato. 32,5% (oʻrtachasi)
ham xato. Foizlarni qoʻshib yoki oʻrtachalab boʻlmaydi, chunki
<b>foiz — son emas, nisbat</b>. U nimadandir olinadi.</p>

<p>Bu darsning butun mazmuni bitta jumlada: <b>aralashtirganda sof
modda qoʻshiladi, foiz emas</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>sof modda miqdorini topasiz;</li>
    <li>ikki eritmani aralashtirasiz;</li>
    <li>suv qoʻshganda va bugʻlatganda nima oʻzgarishini bilasiz;</li>
    <li>kerakli foizni beradigan miqdorni tenglama bilan topasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Aralashmaning kaliti</span>
  <span class="pe-chip pe-chip--s">sof modda</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">massa</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">foiz</span>
</div>

<h3>1. Sof modda — asosiy tushuncha</h3>

<p>«200 g eritmada 10% tuz bor» degani: eritmaning oʻzi 200 g, uning
ichidagi <b>toza tuz</b> esa:</p>

<div class="pe-ex">
  <p class="pe-ex__math">200 × 0,1 = 20 g</p>
  <p class="pe-ex__uz">Ikki yuz grammning oʻn foizi — yigirma gramm
  tuz. Qolgan 180 g — suv.</p>
  <p class="pe-ex__why">Foizni oʻnlik kasrga oʻgirib koʻpaytiramiz
  (PM-22, PM-23).</p>
</div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Har doim sof moddaga oʻting</p>
  <p>Aralashma masalasida birinchi qadam har doim bir xil: har bir
  idishdagi <b>sof modda</b> necha gramm ekanini hisoblang. Foizlar
  bilan toʻgʻridan-toʻgʻri ishlab boʻlmaydi, sof modda bilan esa
  bemalol — u oddiy massa, uni qoʻshsa ham, ayirsa ham boʻladi.</p>
</div>

<h3>2. Ikki eritmani aralashtirish</h3>

<p><b>Masala.</b> 300 g 20% li eritmaga 200 g 45% li eritma qoʻshildi.
Yangi eritma necha foizli?</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 172" role="img" aria-label="Ikki eritma aralashmoqda: boʻyalgan yuzalar yigʻindisi uchinchisiga teng">
    <rect class="pm-ln" x="30" y="40" width="54" height="90" fill="none"/>
    <rect class="pm-fill pm-fill--hl" x="30" y="112" width="54" height="18"/>
    <text class="pm-lbl" x="57" y="146" text-anchor="middle">300 g</text>
    <text class="pm-lbl" x="57" y="162" text-anchor="middle">20%</text>
    <text class="pm-lbl" x="97" y="95" text-anchor="middle">+</text>
    <rect class="pm-ln" x="110" y="40" width="36" height="90" fill="none"/>
    <rect class="pm-fill pm-fill--hl" x="110" y="89.5" width="36" height="40.5"/>
    <text class="pm-lbl" x="128" y="146" text-anchor="middle">200 g</text>
    <text class="pm-lbl" x="128" y="162" text-anchor="middle">45%</text>
    <text class="pm-lbl" x="173" y="95" text-anchor="middle">=</text>
    <rect class="pm-ln" x="200" y="40" width="90" height="90" fill="none"/>
    <rect class="pm-fill pm-fill--hl" x="200" y="103" width="90" height="27"/>
    <text class="pm-lbl pm-lbl--hl" x="245" y="146" text-anchor="middle">500 g</text>
    <text class="pm-lbl pm-lbl--hl" x="245" y="162" text-anchor="middle">30%</text>
    <text class="pm-lbl" x="57" y="32" text-anchor="middle">60 g</text>
    <text class="pm-lbl" x="128" y="32" text-anchor="middle">90 g</text>
    <text class="pm-lbl pm-lbl--hl" x="245" y="32" text-anchor="middle">150 g</text>
  </svg>
  <figcaption>Idishning eni — massa, boʻyalgan qismning balandligi —
  foiz. Demak boʻyalgan <b>yuza</b> sof moddadir: 60 + 90 = 150 g.
  Uchinchi idishning boʻyalgan yuzasi roppa-rosa birinchi ikkitasining
  yigʻindisi.</figcaption>
</figure>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Eritma</th><th>Massa × foiz</th><th>Sof tuz</th></tr>
  <tr><td>Birinchi</td><td class="pm-word__sym">300 × 0,20</td><td>60 g</td></tr>
  <tr><td>Ikkinchi</td><td class="pm-word__sym">200 × 0,45</td><td>90 g</td></tr>
  <tr><td>Aralashma</td><td class="pm-word__sym">500 g</td><td>150 g</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Sof tuz: 60 + 90 = 150 g</span>
    <span class="pm-solve__why">Sof modda qoʻshiladi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Massa: 300 + 200 = 500 g</span>
    <span class="pm-solve__why">Massalar ham qoʻshiladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">150 ÷ 500 = 0,3 = 30%</span>
    <span class="pm-solve__why">Yangi foiz — yangi massadan</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>500 g eritmaning 30% i: 500 × 0,3 = 150 g ✓
  <br><b>Javob:</b> yangi eritma 30% li.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Javob 20 bilan 45 <b>orasida</b> boʻlishi shart — aralashma
  hech qachon eng kuchlisidan kuchli, eng kuchsizidan kuchsiz
  boʻlmaydi. 30 shu oraliqda ✓ Va u 20 ga yaqinroq, chunki birinchi
  eritma koʻproq (300 &gt; 200) ✓</span>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Nega oʻrtachasi emas?</p>
  <p>(20 + 45) ÷ 2 = 32,5 — bu faqat <b>massalar teng</b> boʻlganda
  toʻgʻri boʻlardi. Bu yerda birinchi eritma koʻproq, shuning uchun
  natija uning tomoniga tortiladi. Xuddi PM-88 dagi oʻrtacha tezlik
  kabi: koʻproq turgan tomon ogʻirroq tortadi.</p>
</div>

<h3>3. Suv qoʻshish va bugʻlatish</h3>

<p>Bu ikkisi bitta gʻoyaning ikki tomoni: <b>sof modda
oʻzgarmaydi</b>, faqat umumiy massa oʻzgaradi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Suv qoʻshildi</p>
    <p>Massa <b>ortadi</b>, sof modda oʻsha.
    <br>Foiz kamayadi — suyultirish.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Suv bugʻlandi</p>
    <p>Massa <b>kamayadi</b>, sof modda oʻsha.
    <br>Foiz ortadi — quyultirish.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">400 g 15% li + 100 g suv → 60 ÷ 500 = 0,12 = 12%</p>
  <p class="pe-ex__uz">Sof modda 400 × 0,15 = 60 g edi va shundayligicha
  qoldi; massa esa 500 g boʻldi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">600 g 5% li − 100 g suv → 30 ÷ 500 = 0,06 = 6%</p>
  <p class="pe-ex__uz">Sof modda 600 × 0,05 = 30 g. Suv uchib ketdi,
  tuz qoldi — shuning uchun foiz ortdi.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Qoʻshilgan suvning foizi 0</p>
  <p>Suv — sof moddasi boʻlmagan «eritma». Uni jadvalga
  <b>0%</b> qatori sifatida yozsangiz, aralashtirish masalasi bilan
  bir xil yoʻldan yechiladi.</p>
</div>

<h3>Matnli masala</h3>

<p>Laboratoriyada 300 g 20% li eritma bor. Unga 60% li eritmadan
qoʻshib, 30% li eritma olmoqchi.</p>

<p><b>60% li eritmadan necha gramm qoʻshish kerak?</b></p>

<p><b>Reja:</b> qoʻshiladigan miqdorni x deb olamiz (PM-86) va jadval
tuzamiz. Tenglama oxirgi ustundan chiqadi: sof moddalar yigʻindisi
yangi eritmaning sof moddasiga teng.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Eritma</th><th>Massa</th><th>Sof modda</th></tr>
  <tr><td>Bor eritma (20%)</td><td class="pm-word__sym">300</td><td>60</td></tr>
  <tr><td>Qoʻshiladigan (60%)</td><td class="pm-word__sym">x</td><td>0,6x</td></tr>
  <tr><td>Natija (30%)</td><td class="pm-word__sym">300 + x</td><td>0,3(300 + x)</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 + 0,6x = 0,3(300 + x)</span>
    <span class="pm-solve__why">Sof modda balansi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 + 0,6x = 90 + 0,3x</span>
    <span class="pm-solve__why">Qavsni ochdik (PM-33)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">0,3x = 30</span>
    <span class="pm-solve__why">0,3x va 60 ni boshqa tomonga oʻtkazdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 100 g</span>
    <span class="pm-solve__why">0,3 ga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Sof modda: 60 + 100 × 0,6 = 60 + 60 = 120 g. Umumiy massa:
  300 + 100 = 400 g. Foiz: 120 ÷ 400 = 0,3 = 30% ✓
  <br><b>Javob:</b> 60% li eritmadan 100 g qoʻshish kerak.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Javobni mantiq bilan tekshirish</p>
  <p>30% — 20 bilan 60 orasida, lekin 20 ga ancha yaqin. Demak zaif
  eritma koʻproq boʻlishi kerak. 300 &gt; 100 ✓ Agar javob 500 g
  chiqqanida, darrov shubhalanish kerak edi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">20% li va 45% li aralashsa → 65% li</p>
  <p class="pe-fix__good">30% li</p>
  <p class="pe-fix__why">Foizlar qoʻshilmaydi. Natija har doim ikki
  foizning <b>orasida</b> boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">(20 + 45) ÷ 2 = 32,5%</p>
  <p class="pe-fix__good">150 ÷ 500 = 30%</p>
  <p class="pe-fix__why">Oʻrtacha faqat massalar teng boʻlganda
  toʻgʻri. Bu yerda 300 g va 200 g — teng emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Suv qoʻshildi → sof modda ham ortdi</p>
  <p class="pe-fix__good">Sof modda oʻzgarmaydi, faqat massa ortadi</p>
  <p class="pe-fix__why">Suvda tuz yoʻq. Uning foizi 0 — u faqat
  maxrajni kattalashtiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">200 g ning 10% i = 200 × 10 = 2000 g</p>
  <p class="pe-fix__good">200 × 0,1 = 20 g</p>
  <p class="pe-fix__why">Foizni oʻnlik kasrga oʻgirish unutilgan:
  10% = 0,1. Sof modda eritmadan ogʻir boʻlishi mumkin emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 400 g eritmada 25% shakar bor. Sof shakar
  necha gramm?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>100 g.</b> 400 × 0,25 = 100 g. Qolgan 300 g — suv.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 500 g eritmada 40 g tuz bor. Eritma necha
  foizli?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>8% li.</b> 40 ÷ 500 = 0,08 = 8%.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 200 g 10% li eritmaga 300 g 20% li eritma
  qoʻshildi. Yangi foiz qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>16%.</b> Sof modda: 20 + 60 = 80 g. Massa: 500 g.
    80 ÷ 500 = 0,16 = 16%. Javob 10 bilan 20 orasida va 20 ga
    yaqinroq — chunki 20% li eritma koʻproq ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 300 g 12% li eritmaga 100 g suv qoʻshildi.
  Yangi foiz qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>9%.</b> Sof modda 300 × 0,12 = 36 g va u oʻzgarmaydi.
    Yangi massa 400 g. 36 ÷ 400 = 0,09 = 9%.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. 800 g 5% li eritmadan 300 g suv bugʻlatildi.
  Yangi foiz qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>8%.</b> Sof modda 800 × 0,05 = 40 g, oʻzgarmaydi. Yangi
    massa 800 − 300 = 500 g. 40 ÷ 500 = 0,08 = 8%. Foiz ortdi —
    quyulgan ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. 200 g 40% li eritmaga necha gramm suv
  qoʻshilsa, 25% li boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>120 g.</b> Sof modda 80 g va oʻzgarmaydi. Kerakli massa:
    80 ÷ 0,25 = 320 g. Demak qoʻshiladigan suv 320 − 200 = 120 g.
    Tekshirish: 80 ÷ 320 = 0,25 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. 500 g 10% li eritmaga 40% li eritmadan
  necha gramm qoʻshilsa, 20% li boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>250 g.</b> 50 + 0,4x = 0,2(500 + x) → 50 + 0,4x = 100 + 0,2x
    → 0,2x = 50 → x = 250. Tekshirish: sof modda 50 + 100 = 150 g,
    massa 750 g, 150 ÷ 750 = 0,2 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Aralashma</b><span>ikki yoki undan koʻp modda qoʻshilgan
    massa; ingl. mixture</span></li>
  <li><b>Eritma</b><span>suyuqlikda erigan modda; ingl.
    solution</span></li>
  <li><b>Sof modda</b><span>aralashma ichidagi toza moddaning massasi;
    ingl. pure substance</span></li>
  <li><b>Konsentratsiya</b><span>sof moddaning umumiy massadagi ulushi;
    ingl. concentration</span></li>
  <li><b>Foiz</b><span>yuzdan boʻlak; ingl. percent</span></li>
  <li><b>Suyultirish</b><span>suv qoʻshib foizni kamaytirish; ingl.
    diluting</span></li>
  <li><b>Bugʻlatish</b><span>suvni uchirib foizni oshirish; ingl.
    evaporating</span></li>
  <li><b>Massa</b><span>aralashmaning umumiy ogʻirligi; ingl.
    mass</span></li>
  <li><b>Balans</b><span>kirgan va chiqqan sof modda tengligi; ingl.
    balance</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Sof modda = massa × foiz. Birinchi qadam har doim shu.</li>
    <li>Aralashtirganda <b>sof modda</b> va massa qoʻshiladi, foiz
      emas.</li>
    <li>Yangi foiz = yangi sof modda ÷ yangi massa.</li>
    <li>Suv qoʻshilsa yoki bugʻlansa, sof modda oʻzgarmaydi.</li>
    <li>Suvni 0% li eritma deb yozing — jadval oʻsha-oʻsha
      ishlaydi.</li>
    <li>Natija har doim ikki foizning orasida va koʻproq eritma
      tomoniga yaqin boʻladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-92 — narx, miqdor, qiymat
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-92: Narx, miqdor, qiymat",
        "category": "math",
        "order": 92,
        "summary": (
            "Uchinchi marta bir xil uchlik: qiymat = narx × miqdor. "
            "Birlik narx esa doʻkondagi eng foydali qurol — u katta "
            "paket haqiqatan arzonmi degan savolga javob beradi."
        ),
        "stories": ["Katta paket haqiqatan arzonmi?"],
        "content": """
<h2>PM-92: Narx, miqdor, qiymat</h2>

<p>Doʻkonda bir xil yuvish kukunining ikkita paketi turibdi: 600 g
21 000 soʻm va 3 kg 111 000 soʻm. Qaysi biri arzon?</p>

<p>Kattasi 111 000 soʻm — qimmatroq koʻrinadi. Lekin uning ichida ham
koʻproq narsa bor. Ikkalasini solishtirish uchun ularni <b>bir xil
oʻlchovga</b> keltirish kerak. Bu darsda shuni oʻrganamiz — va javob
sizni ajablantirishi mumkin.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>qiymat, narx va miqdor uchligini toʻliq egallaysiz;</li>
    <li>birlik narxni topib, har qanday ikki taklifni solishtirasiz;</li>
    <li>koʻp mahsulotli xaridni jadval bilan hisoblaysiz;</li>
    <li>«katta paket har doim arzon» degan fikrni tekshirasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Savdo uchligi</span>
  <span class="pe-chip pe-chip--s">qiymat</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">narx</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">miqdor</span>
</div>

<h3>1. Uchinchi marta bir xil uchlik</h3>

<p>Diqqat bilan qarang — bu formulani siz allaqachon ikki marta
koʻrgansiz:</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Dars</th><th>Formula</th><th>«Bir birlikka» degani</th></tr>
  <tr><td>PM-88 — harakat</td><td class="pm-word__sym">S = v × t</td>
    <td>bir soatda bosilgan masofa</td></tr>
  <tr><td>PM-90 — ish</td><td class="pm-word__sym">ish = u × t</td>
    <td>bir kunda bajarilgan ish</td></tr>
  <tr><td>PM-92 — savdo</td><td class="pm-word__sym">qiymat = narx × miqdor</td>
    <td>bir kilogrammning narxi</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Uchalasi bitta gʻoya</p>
  <p>Oʻrtadagi harf har doim bir xil maʼnoda: <b>bitta birlikka toʻgʻri
  keladigan miqdor</b>. Tezlik — bir soatga, unumdorlik — bir kunga,
  narx — bir kilogrammga. Shuning uchun uchalasida ham teskari
  savollar bir xil yechiladi: narx = qiymat ÷ miqdor,
  miqdor = qiymat ÷ narx.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">3 × 12 000 = 36 000 soʻm</p>
  <p class="pe-ex__uz">Kilosi 12 000 soʻmdan 3 kg olma 36 000 soʻm
  turadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">36 000 ÷ 3 = 12 000 soʻm/kg</p>
  <p class="pe-ex__uz">3 kg olma 36 000 soʻm boʻlsa, bir kilosi
  12 000 soʻm.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">36 000 ÷ 12 000 = 3 kg</p>
  <p class="pe-ex__uz">36 000 soʻmga kilosi 12 000 soʻmdan 3 kg olish
  mumkin.</p>
</div>

<h3>2. Birlik narx — solishtirish quroli</h3>

<p>Ikki paketni solishtirish uchun ikkalasining <b>bir kilogrammga
toʻgʻri keladigan narxini</b> hisoblaymiz. Shundan keyin taqqoslash
oddiy son bilan bajariladi.</p>

<p><b>Masala.</b> Guruchning 900 g li paketi 27 000 soʻm, 1,5 kg li
paketi 42 000 soʻm. Qaysi biri arzon?</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Paket</th><th>Narx ÷ miqdor</th><th>1 kg uchun</th></tr>
  <tr><td>900 g — 27 000 soʻm</td>
    <td class="pm-word__sym">27 000 ÷ 0,9</td><td>30 000 soʻm/kg</td></tr>
  <tr><td>1,5 kg — 42 000 soʻm</td>
    <td class="pm-word__sym">42 000 ÷ 1,5</td><td>28 000 soʻm/kg</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">28 000 &lt; 30 000</span>
    <span class="pm-solve__why">Katta paket bir kilogramm uchun arzonroq</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">900 g — bu 0,9 kg</p>
  <p>Birliklarni moslamasdan boʻlish mumkin emas — bu PM-88 dagi minut
  va soat xatosining oʻzi. 27 000 ÷ 900 = 30 desangiz, javob
  «grammiga 30 soʻm» boʻladi; uni 28 000 bilan solishtirib
  boʻlmaydi. <b>Ikkalasini bir xil birlikda hisoblang.</b></p>
</div>

<h3>3. Katta paket har doim arzonmi?</h3>

<p>Yoʻq. Va doʻkonlar buni yaxshi biladi.</p>

<p><b>Masala.</b> Sharbatning 500 ml li shishasi 8 000 soʻm, 2 l li
shishasi 34 000 soʻm. Qaysi biri arzon?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 000 ÷ 0,5 = 16 000 soʻm/litr</span>
    <span class="pm-solve__why">Kichik shisha</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">34 000 ÷ 2 = 17 000 soʻm/litr</span>
    <span class="pm-solve__why">Katta shisha</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">16 000 &lt; 17 000</span>
    <span class="pm-solve__why">Bu safar KICHIK shisha arzonroq</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Kichik shishadan 4 tasi ham 2 litr beradi: 4 × 8 000 =
  32 000 soʻm. Katta shisha esa 34 000 soʻm — 2 000 soʻm qimmat ✓
  <br><b>Javob:</b> 500 ml li shisha arzonroq.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">«Katta paket — tejamkor» degan yozuv daʼvo, dalil emas</p>
  <p>U koʻpincha rost, lekin har doim emas. Birlik narxni hisoblash
  bir necha soniya vaqt oladi va daʼvoni tekshiradi. Bu — PM-81 dagi
  aldamchi diagrammalar bilan bir oiladagi mavzu: raqamlar rost, taassurot
  esa notoʻgʻri.</p>
</div>

<h3>4. Koʻp mahsulotli xarid — jadval</h3>

<p><b>Masala.</b> Kilosi 12 000 soʻmdan 2 kg guruch, kilosi
9 000 soʻmdan 3 kg un va kilosi 12 000 soʻmdan 1,5 kg shakar olindi.
Jami qancha toʻlanadi?</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Mahsulot</th><th>Narx × miqdor</th><th>Qiymat</th></tr>
  <tr><td>Guruch</td><td class="pm-word__sym">12 000 × 2</td><td>24 000 soʻm</td></tr>
  <tr><td>Un</td><td class="pm-word__sym">9 000 × 3</td><td>27 000 soʻm</td></tr>
  <tr><td>Shakar</td><td class="pm-word__sym">12 000 × 1,5</td><td>18 000 soʻm</td></tr>
  <tr><td>Jami</td><td class="pm-word__sym">—</td><td>69 000 soʻm</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Oxirgi ustunni qoʻshing, oʻrtadagini emas</p>
  <p>Bu — PM-88 dagi qoidaning oʻzi: masofalar qoʻshiladi, tezliklar
  qoʻshilmaydi. Bu yerda qiymatlar qoʻshiladi, narxlar qoʻshilmaydi.
  12 000 + 9 000 + 12 000 = 33 000 degan son hech narsani
  anglatmaydi.</p>
</div>

<h3>Matnli masala</h3>

<p>Afsona bozorga 150 000 soʻm bilan bordi. Kilosi 54 000 soʻmdan
2 kg goʻsht va kilosi 6 000 soʻmdan 3 kg kartoshka oldi. Qolgan pulga
kilosi 8 000 soʻmdan olma olmoqchi.</p>

<p><b>Necha kilogramm olma olishi mumkin?</b></p>

<p><b>Reja:</b> avval xaridlarni jadvalga solamiz, qolgan pulni
topamiz, keyin uni olmaning narxiga boʻlamiz.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Mahsulot</th><th>Narx × miqdor</th><th>Qiymat</th></tr>
  <tr><td>Goʻsht</td><td class="pm-word__sym">54 000 × 2</td><td>108 000 soʻm</td></tr>
  <tr><td>Kartoshka</td><td class="pm-word__sym">6 000 × 3</td><td>18 000 soʻm</td></tr>
  <tr><td>Sarflandi</td><td class="pm-word__sym">108 000 + 18 000</td><td>126 000 soʻm</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Sarflandi: 108 000 + 18 000 = 126 000 soʻm</span>
    <span class="pm-solve__why">Qiymatlar qoʻshildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qoldi: 150 000 − 126 000 = 24 000 soʻm</span>
    <span class="pm-solve__why">Boshlangʻich puldan ayirildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">24 000 ÷ 8 000 = 3 kg</span>
    <span class="pm-solve__why">miqdor = qiymat ÷ narx</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Hamma xarid: 108 000 + 18 000 + 3 × 8 000 = 108 000 + 18 000 +
  24 000 = 150 000 soʻm ✓ — puli tugadi, qarz ham qolmadi.
  <br><b>Javob:</b> Afsona 3 kg olma olishi mumkin.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Goʻsht taxminan 110 ming, kartoshka 20 ming — birgalikda
  130 ming atrofida. 150 mingdan 20 ming qoladi, olma kilosi 8 ming,
  demak 2–3 kg. Aniq hisob 3 kg berdi ✓</span>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">111 000 &gt; 21 000, demak kichik paket
  arzon</p>
  <p class="pe-fix__good">Birlik narxni solishtiring: 37 000 va
  35 000 soʻm/kg</p>
  <p class="pe-fix__why">Umumiy narx miqdorni hisobga olmaydi.
  Solishtirish faqat bir xil oʻlchovda maʼnoli.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">27 000 ÷ 900 = 30 va 42 000 ÷ 1,5 = 28 000,
  demak birinchisi arzon</p>
  <p class="pe-fix__good">27 000 ÷ 0,9 = 30 000 va 42 000 ÷ 1,5 =
  28 000</p>
  <p class="pe-fix__why">Biri grammda, biri kilogrammda hisoblangan.
  30 va 28 000 ni solishtirish maʼnosiz.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Narxlar qoʻshildi: 12 000 + 9 000 + 12 000 =
  33 000</p>
  <p class="pe-fix__good">Qiymatlar qoʻshiladi: 24 000 + 27 000 +
  18 000 = 69 000</p>
  <p class="pe-fix__why">Narx — bir kilogrammning narxi. Uni qoʻshish
  hech qanday haqiqiy summani bermaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Katta paket har doim arzonroq</p>
  <p class="pe-fix__good">Har safar birlik narxni hisoblang</p>
  <p class="pe-fix__why">Sharbat misolida katta shisha litriga
  1 000 soʻm qimmat chiqdi. Daʼvoni tekshirmasdan ishonmaslik
  kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Kilosi 15 000 soʻmdan 4 kg shakar necha
  soʻm turadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>60 000 soʻm.</b> qiymat = narx × miqdor = 15 000 × 4.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 5 kg kartoshka 35 000 soʻm turdi. Bir kilosi
  necha soʻm?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>7 000 soʻm.</b> narx = qiymat ÷ miqdor = 35 000 ÷ 5.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 96 000 soʻmga kilosi 16 000 soʻmdan necha kg
  goʻsht olish mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>6 kg.</b> miqdor = qiymat ÷ narx = 96 000 ÷ 16 000 = 6.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Sut: 750 ml 9 000 soʻm yoki 1,5 l
  17 000 soʻm. Qaysi biri arzon?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>1,5 litrlik.</b> 9 000 ÷ 0,75 = 12 000 soʻm/litr;
    17 000 ÷ 1,5 ≈ 11 333 soʻm/litr. Katta paket litriga taxminan
    667 soʻm arzon.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Yogʻ: 400 g 14 000 soʻm yoki 1 kg
  36 000 soʻm. Qaysi biri arzon?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>400 grammlik.</b> 14 000 ÷ 0,4 = 35 000 soʻm/kg, kattasi esa
    36 000 soʻm/kg. Bu safar kichik paket arzon — «katta har doim
    tejamkor» degan fikr yana ishlamadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Kilosi 10 000 soʻmdan 2,5 kg olma va kilosi
  20 000 soʻmdan 1,5 kg uzum olindi. Jami qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>55 000 soʻm.</b> Olma 10 000 × 2,5 = 25 000; uzum
    20 000 × 1,5 = 30 000; jami 25 000 + 30 000 = 55 000.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Bekzodda 100 000 soʻm bor. U kilosi
  22 000 soʻmdan 3 kg olma oldi. Qolgan pulga kilosi 17 000 soʻmdan
  necha kg nok olishi mumkin va qancha pul ortadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2 kg nok, 0 soʻm ortadi.</b> Olma: 22 000 × 3 = 66 000.
    Qoldi: 100 000 − 66 000 = 34 000. Nok: 34 000 ÷ 17 000 = 2 kg
    roppa-rosa. Tekshirish: 66 000 + 34 000 = 100 000 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Narx</b><span>bir birlik mahsulotning puli; ingl. unit
    price</span></li>
  <li><b>Miqdor</b><span>olingan mahsulot soni yoki ogʻirligi; ingl.
    quantity</span></li>
  <li><b>Qiymat</b><span>hammasi uchun toʻlanadigan pul; ingl. total
    cost</span></li>
  <li><b>Birlik narx</b><span>bir kg yoki bir litrga toʻgʻri keladigan
    narx; ingl. price per unit</span></li>
  <li><b>Taqqoslash</b><span>ikki taklifni bir xil oʻlchovga keltirib
    solishtirish; ingl. comparison</span></li>
  <li><b>Paket</b><span>maʼlum miqdordagi mahsulot oʻrami; ingl.
    pack</span></li>
  <li><b>Chegirma</b><span>narxning kamaytirilgan qismi; ingl.
    discount</span></li>
  <li><b>Byudjet</b><span>xarid uchun ajratilgan pul; ingl.
    budget</span></li>
  <li><b>Qoldiq</b><span>xariddan keyin ortgan pul; ingl.
    change</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>qiymat = narx × miqdor — S = v·t va ish = u·t bilan bir xil
      uchlik.</li>
    <li>narx = qiymat ÷ miqdor; miqdor = qiymat ÷ narx.</li>
    <li>Ikki taklifni solishtirish uchun <b>birlik narx</b>ni
      hisoblang.</li>
    <li>Avval birliklarni moslang: 900 g — bu 0,9 kg.</li>
    <li>Koʻp mahsulotli xarid — jadval; qiymatlar qoʻshiladi, narxlar
      emas.</li>
    <li>Katta paket har doim arzon emas — tekshirmasdan
      ishonmang.</li>
  </ul>
</div>
""",
    },
]
