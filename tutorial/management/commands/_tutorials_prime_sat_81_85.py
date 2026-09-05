# -*- coding: utf-8 -*-
"""Prime SAT Math — lessons 81–85 (Blok E ning boshi: taktika va Desmos).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md
Lesson list: tutorial/management/commands/toc_prime_sat_math.txt

⚠️ SARLAVHALAR BAZADAN OLINGAN, aynan.

⚠️ BLOK E QOIDASI (toc sarlavhasidan): bu blok MATEMATIKA OʻRGATMAYDI —
   u testni yechish usulini oʻrgatadi. Demak har bir darsda:
     • usul aniq qadamlarga boʻlingan (ps-tactic);
     • usul QACHON ishlamasligi ham aytilgan — bu darsning yarmi;
     • misollardagi matematika ILGARIGI darslardan olinadi (kumulyativ),
       chunki yangi matematika bu blokda yoʻq.

  • SAT-81 — son qoʻyish (harfli javoblar uchun).
  • SAT-82 — javobdan teskari yurish (sonli javoblar uchun).
  • SAT-83 — Desmos: grafik va kesishish.
  • SAT-84 — Desmos: nomaʼlum doimiy uchun slider.
  • SAT-85 — Desmos: tengsizlik va soha.
  • ⛔ SAT-86 dan keyingi mavzular (eyeballing, grid-in, vaqt) YOʻQ.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_sat_81_85.py \\
        --author=prime --republish
"""

PLAYLIST = {
    "title": "Prime SAT Math",
    "category": "math",
    "description": (
        "Digital SAT matematikasi noldan — 100 dars. Savollar ingliz tilida, "
        "chunki test shunday; tushuntirish oʻzbek tilida, chunki oʻqituvchi shunday. "
        "Har bir darsda haqiqiy SAT savollari, tuzoq javoblar va 20 savollik mashq."
    ),
}

TUTORIALS = [

    # ══════════════════════════════════════════════════════════════════
    # SAT-81 — plugging in numbers
    # ══════════════════════════════════════════════════════════════════
    {
        "title": 'SAT-81: The "Plugging In Numbers" Tactic',
        "category": "math",
        "order": 81,
        "summary": (
            "Javoblarda harf boʻlsa — algebra qilmang. Oʻzingiz bitta son "
            "tanlang va toʻrtta variantni sinab koʻring."
        ),
        "stories":  ["The Batch of Fifty"],
        "content": """
<h2>SAT-81: The "Plugging In Numbers" Tactic</h2>

<p>Sakson dars davomida matematika oʻrgandik. Bu blokda matematika
oʻrganmaymiz — <mark>testni yechish usulini oʻrganamiz</mark>. Ikkalasi
bir narsa emas: birinchisi bilimni beradi, ikkinchisi vaqtni va
xatosizlikni.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Avval ogohlantirish</span>
  Taktika matematikaning oʻrnini bosmaydi. U <b>bilgan odamni tezroq</b>
  qiladi, bilmagan odamni emas. Shuning uchun bu blok oxirida turibdi,
  boshida emas.
</div>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>bu taktika qachon ishlashini bir qarashda aniqlaysiz;</li>
    <li>yaxshi son tanlaysiz — va yomonini tanlamaysiz;</li>
    <li>ikkita variant qolganda ikkinchi sonni qoʻyasiz;</li>
    <li>usul foydasiz boʻlgan holatni taniysiz.</li>
  </ul>
</div>

<h3>Belgisi bitta</h3>

<p>Javob variantlarida <b>harf</b> bor. Ifoda soʻralgan, son emas. Shu
holatda savolning oʻzi sizga ruxsat berib turibdi: agar javob
<i>har qanday</i> qiymat uchun toʻgʻri boʻlishi kerak boʻlsa, u
<b>sizning</b> qiymatingiz uchun ham toʻgʻri boʻlishi shart.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">The move — uch qadam</span>
  <ol>
    <li><b>Tanlang:</b> oson, lekin oʻziga xos boʻlmagan son.</li>
    <li><b>Yuriting:</b> savol matnini shu son bilan bajaring va
        <b>maqsad sonni</b> yozib qoʻying.</li>
    <li><b>Sinang:</b> toʻrtala variantga oʻsha sonni qoʻying;
        maqsadni bergani javob.</li>
  </ol>
</div>

<h3>Birinchi misol</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>A shirt costs <i>d</i> dollars. During a sale its price is reduced
    by 20 percent. Which expression gives the sale price, in dollars?</p>
  </div>
  <ol class="ps-ch">
    <li>0.8<i>d</i></li>
    <li><i>d</i> − 0.2</li>
    <li>1.2<i>d</i></li>
    <li>0.2<i>d</i></li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 0.8d</p>
      <p><b>d = 100</b> deb oling. 20 foiz — 20 dollar, demak yangi narx
      <b>80</b>. Endi variantlar: 0.8 × 100 = 80 ✓, 100 − 0.2 = 99.8,
      1.2 × 100 = 120, 0.2 × 100 = 20.</p>
      <p>Faqat bittasi 80 berdi.</p>
    </div>
  </details>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Foiz bor joyda <b>100 ni tanlang</b>. Har qanday foiz darrov toʻgʻridan
  toʻgʻri sonni beradi va hech qanday kasr chiqmaydi.
</div>

<h3>Qaysi sonni tanlash kerak emas</h3>

<table class="pe-table">
  <tr><th>Son</th><th>Nima uchun xavfli</th></tr>
  <tr><td>0</td><td>Koʻpaytirishning hammasini nolga aylantiradi —
      bir nechta variant bir vaqtda toʻgʻri chiqadi.</td></tr>
  <tr><td>1</td><td>1 × 1 = 1 va 1² = 1: darajalar farqi
      koʻrinmay qoladi.</td></tr>
  <tr><td>Savolda uchragan son</td><td>Tasodifan boshqa variant bilan
      mos tushadi.</td></tr>
  <tr><td>Juda katta son</td><td>Arifmetikaning oʻzi xatoga olib
      keladi.</td></tr>
</table>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eng yaxshi tanlov — <b>2, 3, 4, 5 yoki 10</b>; foizda <b>100</b>;
  vaqt/tezlikda esa masofani boʻlinadigan qilib olish (masalan 60 km).
  «Oson, lekin oʻziga xos emas» degani shu.
</div>

<h3>Ikkita variant qolganda</h3>

<p>Baʼzan tanlangan son ikkita variantni bir xil qiymatga olib keladi.
Bu usulning kamchiligi emas — <b>usulning ishlashi</b>. Shunchaki
ikkinchi son qoʻyiladi va faqat bittasi omon qoladi.</p>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">70 s</span></p>
  <div class="ps-stem__q">
    <p>The sum of three consecutive even integers is <i>n</i>. In terms of
    <i>n</i>, what is the smallest of the three integers?</p>
  </div>
  <ol class="ps-ch">
    <li>(<i>n</i> − 6)/3</li>
    <li><i>n</i>/3</li>
    <li>(<i>n</i> + 6)/3</li>
    <li><i>n</i>/3 − 6</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) (n − 6)/3</p>
      <p><b>4, 6, 8</b> ni oling. Yigʻindisi n = 18, eng kichigi 4.</p>
      <p>(18 − 6)/3 = 4 ✓ · 18/3 = 6 · (18 + 6)/3 = 8 · 18/3 − 6 = 0.</p>
      <p>Bitta variant qoldi — ikkinchi sonning hojati ham
      boʻlmadi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">n/3</span>
  <span class="ps-trap__why">Bu <b>oʻrtadagi</b> son (6). Yigʻindini uchga
  boʻlish oʻrtachani beradi — savol esa eng kichigini soʻragan. Son
  qoʻyish bu tuzoqni bir soniyada ochib beradi.</span>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ikkinchi sonni qoʻyish kerak boʻlsa, birinchisidan <b>uzoqroq</b>ni
  oling. 2 dan keyin 3 emas, 10 tanlang — yaqin sonlar koʻpincha bir xil
  tasodifni takrorlaydi.
</div>

<h3>Qachon ishlatmaslik kerak</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>Javoblar son boʻlsa</b> — u holda boshqa taktika kerak
        (SAT-82, backsolving).</li>
    <li><b>Grid-in savolda</b> — variant yoʻq, sinab koʻrishga narsa
        yoʻq.</li>
    <li><b>Algebra 20 soniyada bitsa</b> — son qoʻyish undan sekinroq.
        Taktika vosita, majburiyat emas.</li>
  </ol>
</div>

<h3>Exam English — belgini tanish</h3>

<ul class="ps-phrase">
  <li><b>in terms of x</b><span>x orqali — javobda harf boʻladi</span></li>
  <li><b>which expression represents</b><span>qaysi ifoda ifodalaydi</span></li>
  <li><b>is equivalent to</b><span>teng kuchli</span></li>
  <li><b>for all values of n</b><span>n ning barcha qiymatlari uchun</span></li>
  <li><b>where c is a constant</b><span>bunda c — doimiy son</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad"><i>d</i> = 1 deb olish</p>
  <p class="pe-good"><i>d</i> = 100 (foiz bor)</p>
  <p class="pe-fix__why">1 bilan koʻpaytirish va daraja farqi yoʻqoladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">maqsad sonni yozib qoʻymaslik</p>
  <p class="pe-good">avval maqsadni yozing, keyin variantlarga oʻting</p>
  <p class="pe-fix__why">Yodda saqlangan son variantlar orasida
  adashadi — bu usulning eng koʻp uchraydigan xatosi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu usul <b>tekshiruv</b> sifatida ham qimmatli. Algebra bilan yechib
  boʻlgach, bitta son qoʻyib koʻring: agar ifodangiz oʻsha sonni bersa,
  ishoning; bermasa — belgida xato bor.
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val"><i>d</i> − 0.2</span>
  <span class="ps-trap__why">«20 percent» ni <b>0.2 dollar</b> deb
  oʻqigan. Foiz — son emas, <b>koʻpaytuvchi</b> (SAT-52). d = 100
  qoʻyilgan zahoti bu 99.80 beradi va xato koʻrinib qoladi: chegirma
  20 tiyin boʻlishi mumkin emas.</span>
</div>

<h3>Uchinchi qoʻllanish — oʻz algebrangizni tekshirish</h3>

<p>Bu taktikaning eng kam ishlatiladigan, lekin eng qimmatli tomoni:
u <b>javob variantisiz ham</b> ishlaydi. Grid-in savolda ifodani
algebra bilan chiqarasiz, keyin bitta son qoʻyib ikkalasini
solishtirasiz.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Masala: 3(x + 2) − x ni soddalashtiring</span>
    <span class="pm-solve__why">Siz 2x + 6 deb chiqardingiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">x = 4: asl ifoda 3(6) − 4 = 14</span>
    <span class="pm-solve__why">Boshlangʻich matn boʻyicha</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Sizniki: 2(4) + 6 = 14 ✓</span>
    <span class="pm-solve__why">Mos keldi — soddalashtirish toʻgʻri</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu tekshiruv 10 soniya oladi va <b>ishora xatosini deyarli har doim
  tutadi</b> — chunki notoʻgʻri ishora bilan yozilgan ifoda tasodifan
  bir xil son bermaydi. Agar mos kelmasa, xato sizda, javob variantida
  emas.
</div>

<div class="ps-desmos">
  <span class="ps-desmos__t">Desmos bilan bir zumda</span>
  <p>Harfli javoblarda Desmosning goʻzal bir hiylasi bor: ikkita ifoda
  <b>teng kuchli</b> boʻlsa, ularning grafiklari bir-birining ustiga
  aynan tushadi. Savoldagi ifodani va shubhali variantni ikki qatorga
  yozing — biri ikkinchisini butunlay yopib qolsa, ular teng kuchli.
  Farq qilsa, chiziqlar ajraladi.</p>
  <p>Bu son qoʻyishning ham tez, ham xatosiz shakli: bitta son bitta
  nuqtani tekshiradi, grafik esa <b>barcha</b> nuqtalarni.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  A price <i>p</i> is increased by 25 percent. Which expression gives the
  new price?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">p = 100 → 125, demak 1.25p.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Why is 1 a poor number to plug in?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1 ning har qanday darajasi 1 — darajalari
  farq qiladigan variantlar bir xil chiqadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Two answer choices both give your target. What do you do?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ikkinchi, uzoqroq sonni qoʻyasiz.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  The choices are 4, 7, 9 and 12. Is this tactic the right one?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — javoblar son, demak SAT-82 dagi
  backsolving kerak.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  Three consecutive even integers sum to <i>n</i>. What is the largest,
  in terms of <i>n</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4, 6, 8 → n = 18, eng kattasi 8, va
  (18 + 6)/3 = 8. Demak (n + 6)/3.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>in terms of</b><span>… orqali</span></li>
  <li><b>expression</b><span>ifoda</span></li>
  <li><b>equivalent</b><span>teng kuchli</span></li>
  <li><b>consecutive</b><span>ketma-ket</span></li>
  <li><b>constant</b><span>doimiy son</span></li>
  <li><b>reduced by</b><span>… ga kamaytirilgan</span></li>
  <li><b>sale price</b><span>chegirmali narx</span></li>
  <li><b>substitute</b><span>oʻrniga qoʻymoq</span></li>
  <li><b>target value</b><span>maqsad qiymat</span></li>
  <li><b>eliminate</b><span>chiqarib tashlamoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Javoblarda <b>harf</b> boʻlsa — son qoʻying.</li>
    <li>0 va 1 dan qoching; foizda 100 oling.</li>
    <li>Avval <b>maqsad sonni yozing</b>, keyin variantlarga oʻting.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-82 — backsolving
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-82: Backsolving (Working from the Options)",
        "category": "math",
        "order": 82,
        "summary": (
            "Javoblar son boʻlsa, tenglamani yechmang — javoblarni "
            "tenglamaga qoʻying. Va oʻrtasidan boshlang."
        ),
        "stories":  ["Backwards From the Curtain"],
        "content": """
<h2>SAT-82: Backsolving (Working from the Options)</h2>

<p>SAT-81 harfli javoblar uchun edi. Bu dars uning egizagi va boshqa
yarmi: <mark>javoblar son boʻlsa, toʻgʻri javob allaqachon
sahifada</mark>. Uni topish — yechishdan koʻra sinashdir.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>sinashga arziydigan savolni taniysiz;</li>
    <li>oʻrtadagi variantdan boshlab yarmini bir urinishda kesasiz;</li>
    <li>matnli masalada javobni matnga qaytarib qoʻyasiz;</li>
    <li>usul sekinroq boʻlgan holatni ham taniysiz.</li>
  </ul>
</div>

<h3>Nega bu ishlaydi</h3>

<p>Tenglamani yechish — nomaʼlumni <b>topish</b>. Javobni qoʻyib koʻrish —
uni <b>tekshirish</b>. Tekshirish deyarli har doim osonroq: unda faqat
arifmetika bor, hech qanday koʻchirish, ishora almashtirish yoki qavs
ochish yoʻq — yaʼni xato qiladigan joyning oʻzi yoʻq.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">The move</span>
  <ol>
    <li>Variantlar <b>tartiblanganini</b> tekshiring (SAT sonli
        javoblarni deyarli har doim oʻsish tartibida beradi).</li>
    <li><b>Oʻrtadagi</b> bittasidan boshlang.</li>
    <li>Katta chiqsa — kattalarini oʻchiring; kichik chiqsa —
        kichiklarini.</li>
    <li>Ikki urinishda javob qoladi.</li>
  </ol>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu — kutubxonada kitob qidirish. Hamma kitobni birma-bir koʻrmaysiz:
  oʻrtasini ochasiz, harfga qaraysiz va yarmini tashlab yuborasiz. Toʻrt
  variantda oʻrtadan boshlash <b>ikki urinish</b> bilan yetadi.
</div>

<h3>Birinchi misol — sof tenglama</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>If 2(<i>x</i> + 5) + 3<i>x</i> = 35, what is the value of
    <i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>5</li>
    <li>6</li>
    <li>7</li>
    <li>9</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 5</p>
      <p>Tartiblangan: 5, 6, 7, 9. Oʻrtadan — 6 dan boshlaymiz:
      2(11) + 18 = 40. <b>Katta chiqdi</b>, demak 7 va 9 ni ham
      hisoblamasdan oʻchiramiz.</p>
      <p>Qolgani 5: 2(10) + 15 = 20 + 15 = 35 ✓</p>
      <p>Ikki urinishda tugadi. Qavs ochilmadi, had koʻchirilmadi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">6</span>
  <span class="ps-trap__why">Qavsni ochishda 5 ni 2 ga koʻpaytirishni
  unutgan: 2x + 5 + 3x = 35 → 5x = 30 → x = 6. Aynan shu xato uchun
  qoʻyilgan variant — va sinab koʻrgan odam unga tushmaydi, chunki
  6 tenglamani <b>qanoatlantirmaydi</b>.</span>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  6 katta chiqqani uchun 7 va 9 ni <b>hisoblamasdan</b> oʻchirdik. Bitta urinish ikkita variantni yoʻq qiladi — usulning butun
  tejamkorligi shunda.
</div>

<h3>Ikkinchi misol — matnli masala</h3>

<p>Backsolving matnli masalalarda ayniqsa kuchli, chunki u yerda
tenglama tuzishning oʻzi eng qiyin qadam. Sinaganda tenglama umuman
tuzilmaydi.</p>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">75 s</span></p>
  <div class="ps-stem__q">
    <p>Tickets cost $12 for an adult and $7 for a child. A group of 15
    people paid a total of $145. How many adults were in the group?</p>
  </div>
  <ol class="ps-ch">
    <li>8</li>
    <li>7</li>
    <li>9</li>
    <li>10</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 8</p>
      <p>8 kattalar → 7 bola. Pul: 8 × 12 = 96, 7 × 7 = 49, jami
      <b>145</b> ✓</p>
      <p>Diqqat: har bir variant <b>ikkita</b> sonni belgilaydi —
      kattalar soni va undan kelib chiqadigan bolalar soni.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">7</span>
  <span class="ps-trap__why">Bu <b>bolalar</b> soni — masalaning toʻgʻri
  yechimi, lekin savolning javobi emas. SAT bu tuzoqni matnli
  masalalarda deyarli har doim qoʻyadi.</span>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Sinab koʻrgach, <b>savolni qayta oʻqing</b>. «Nechta kattalar?» degan
  savolga 7 deb javob berish — matematik xato emas, oʻqish xatosi. Va
  test bu ikkalasini bir xil baholaydi.
</div>

<h3>Qachon ishlatmaslik kerak</h3>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchta «yoʻq»</span>
  <ol>
    <li><b>Grid-in</b> savolda — variant yoʻq.</li>
    <li><b>Javoblar harfli</b> boʻlsa — u holda SAT-81.</li>
    <li>Bitta variantni sinash <b>uzoq</b> boʻlsa — masalan har safar
        ikkita tenglamani qaytadan yechish kerak boʻlsa.</li>
  </ol>
</div>

<h3>Exam English — belgini tanish</h3>

<ul class="ps-phrase">
  <li><b>what is the value of x</b><span>x ning qiymati nechaga teng</span></li>
  <li><b>how many</b><span>nechta — matnli masalaning boshi</span></li>
  <li><b>which of the following satisfies</b><span>qaysi biri shartni qanoatlantiradi</span></li>
  <li><b>a solution to the equation</b><span>tenglamaning yechimi</span></li>
  <li><b>a total of</b><span>jami</span></li>
</ul>

<div class="ps-desmos">
  <span class="ps-desmos__t">Desmos bilan yanada tez</span>
  <p>Tenglamani Desmosga ikki funksiya sifatida kiritsangiz, javob
  kesishishda koʻrinadi — sinashning ham hojati qolmaydi. Bu keyingi
  darsning mavzusi (SAT-83). Backsolving esa Desmos qulay
  boʻlmagan joyda — masalan matnli shartlarda — kuchini
  saqlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Birinchi variantdan boshlash</p>
  <p class="pe-good">Oʻrtadagisidan boshlash</p>
  <p class="pe-fix__why">Oʻrtadan boshlansa, bitta urinish yarmini
  kesadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">145 ni topib, javobni belgilamay ketish</p>
  <p class="pe-good">Savolga qaytish: «nechta kattalar?»</p>
  <p class="pe-fix__why">Toʻgʻri hisob + notoʻgʻri savol = notoʻgʻri
  javob.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki taktikani bitta jumla ajratadi: <b>javoblarda harf boʻlsa — son
  qoʻying; javoblarda son boʻlsa — javobni qoʻying.</b> Testda birinchi
  qaraydigan joyingiz — savol emas, variantlar.
</div>

<h3>Uchinchi tur — «which of the following» savollari</h3>

<p>Baʼzan savol tenglama ham, matn ham bermaydi: u <b>shart</b> beradi
va toʻrtta nomzodni qoʻyadi. Bu ham backsolving — faqat sinaladigan
narsa son emas, butun bir variant.</p>

<div class="pm-check">
  <p class="pm-check__t">Misol</p>
  <p>«Which of the following is a solution to 2<i>x</i> + 3 &gt; 11?»
  Variantlar 2, 3, 4, 5. Har birini qoʻying: 2(2) + 3 = 7, yoʻq;
  2(3) + 3 = 9, yoʻq; 2(4) + 3 = 11 — <b>tenglik, «katta» emas</b>,
  yoʻq; 2(5) + 3 = 13 ✓</p>
  <p>Bu yerda oʻrtadan boshlash shart emas, chunki javob bittadan
  ortiq boʻlishi mumkin emas va sinash arzon.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Yuqoridagi 4 — tengsizlikning <b>chegarasi</b>. «Greater than» tenglikni
  olmaydi (SAT-14). Backsolving bu farqni koʻrsatib beradi, lekin faqat
  siz belgini diqqat bilan oʻqisangiz.
</div>

<h3>Necha soniya tejaydi</h3>

<table class="pe-table">
  <tr><th>Savol</th><th>Yechish</th><th>Sinash</th></tr>
  <tr><td>Bir nomaʼlumli tenglama</td><td>40–60 s</td><td>20–40 s</td></tr>
  <tr><td>Matnli masala (tenglama tuzish kerak)</td><td>90–120 s</td>
      <td>45–70 s</td></tr>
  <tr><td>Sistema (ikki tenglama)</td><td>90 s</td>
      <td>sekin — Desmos yaxshiroq</td></tr>
</table>

<p>Oxirgi qator muhim: backsolving <b>hamma joyda emas</b>, bir nomaʼlum
boʻlgan joyda kuchli. Sistema uchun keyingi dars (SAT-83) tezroq yoʻl
beradi.</p>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  The choices are 3, 6, 9, 12. Which do you test first?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">6 yoki 9 — oʻrtadagi ikkitasidan biri.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  If 2(<i>x</i> + 3) = 20, backsolve from 4, 7, 10, 13.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">7: 2(10) = 20 ✓</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  A group of 20 paid $190 at $12 and $7. Test 10 adults.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">10 × 12 + 10 × 7 = 190 ✓ — 10 kattalar.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Why is testing easier than solving?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Tekshirishda faqat arifmetika bor —
  koʻchirish va ishora xatosi mumkin emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  The question is a grid-in. Can you backsolve?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Yoʻq — sinaydigan variant yoʻq.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>backsolve</b><span>javobdan teskari yurmoq</span></li>
  <li><b>the value of</b><span>… ning qiymati</span></li>
  <li><b>satisfies</b><span>qanoatlantiradi</span></li>
  <li><b>a total of</b><span>jami</span></li>
  <li><b>eliminate</b><span>chiqarib tashlamoq</span></li>
  <li><b>test a choice</b><span>variantni sinab koʻrmoq</span></li>
  <li><b>too large / too small</b><span>katta / kichik chiqdi</span></li>
  <li><b>in ascending order</b><span>oʻsish tartibida</span></li>
  <li><b>verify</b><span>tekshirmoq</span></li>
  <li><b>remaining choices</b><span>qolgan variantlar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Javoblar <b>son</b> boʻlsa — ularni sinang.</li>
    <li><b>Oʻrtadan</b> boshlang: bitta urinish yarmini kesadi.</li>
    <li>Topgach, <b>savolni qayta oʻqing</b> — u nimani soʻragan edi?</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-83 — Desmos I
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-83: Mastering Desmos I — Graphing and Intersections",
        "category": "math",
        "order": 83,
        "summary": (
            "Testning ichida Desmos bor. Tenglamani yechish oʻrniga ikki "
            "chiziq chizib, kesishgan joyni oʻqish mumkin."
        ),
        "stories":  ["The Cup That Paid the Rent"],
        "content": """
<h2>SAT-83: Mastering Desmos I — Graphing and Intersections</h2>

<p>Raqamli SAT topshiriladigan dasturning ichiga <b>Desmos grafik
kalkulyatori</b> qurib qoʻyilgan, va u matematikaning ikkala moduliga
ham ochiq. Bu — testdagi eng katta bitta imkoniyat, lekin faqat
<mark>uni qanday ishlatishni oldindan mashq qilgan odam uchun</mark>.
Imtihon kuni oʻrganishga kech.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>tenglamani ikki funksiyaga ajratib, yechimni kesishishdan
        olasiz;</li>
    <li>ikki nomaʼlumli sistemani bir necha soniyada yechasiz;</li>
    <li>nollarni (x bilan kesishish) topasiz;</li>
    <li>Desmosning ikkita jimgina tuzogʻini bilasiz.</li>
  </ul>
</div>

<h3>Asosiy gʻoya: tenglamani ikkiga boʻling</h3>

<p>Har qanday tenglamaning chap tomoni bitta funksiya, oʻng tomoni
ikkinchisi. Ularning grafiklari kesishgan joyda ikki tomon
<b>tenglashadi</b> — demak oʻsha nuqtaning x koordinatasi tenglamaning
yechimi.</p>

<div class="ps-desmos">
  <span class="ps-desmos__t">Keystrokes</span>
  <p>Birinchi qatorga <code>y=3x+5</code>, ikkinchisiga
  <code>y=x+11</code>. Kesishgan nuqtaga <b>bosing</b> — Desmos
  koordinatalarni koʻrsatadi: (3, 14). Javob x = 3.</p>
  <p>Qoʻl bilan tekshirish: 3(3) + 5 = 14 va 3 + 11 = 14 ✓</p>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">The move</span>
  <ol>
    <li>Tenglamaning <b>chap tomonini</b> birinchi qatorga
        <code>y=</code> bilan yozing.</li>
    <li><b>Oʻng tomonini</b> ikkinchi qatorga.</li>
    <li>Kesishishga bosing va <b>x</b> ni oʻqing.</li>
  </ol>
</div>

<h3>Sistemalar — usul aynan oʻsha</h3>

<p>Ikki nomaʼlumli sistemada ikkala tenglamani ham kiritasiz. Kesishish
nuqtasi <b>x va y ni birdan</b> beradi — SAT-19 dagi qoʻshish yoki
oʻrniga qoʻyish usullariga ehtiyoj qolmaydi.</p>

<div class="pm-check">
  <p class="pm-check__t">Misol</p>
  <p><code>y=2x-1</code> va <code>y=-x+5</code> → kesishish (2, 3).</p>
  <p>Tekshiruv: 2(2) − 1 = 3 ✓ va −2 + 5 = 3 ✓</p>
</div>

<h3>Nollar</h3>

<p>«What are the solutions of …» yoki «for what values of x does the
graph cross the x-axis» degan savolda ifodani shundayligicha kiriting:
<code>y=x^2-5x+6</code>. Grafik x oʻqini kesgan ikki nuqtaga bosing —
2 va 3 chiqadi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Desmos <b>faqat ekrandagi narsani</b> koʻrsatadi. Yechim −40 da
  boʻlsa, siz uni koʻrmaysiz va «yechim yoʻq» deb oʻylaysiz. Shubha
  tugʻilsa — <b>uzoqlashtiring</b> (zoom out). Bu birinchi tuzoq.
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ikkinchi tuzoq</span>
  Desmos trigonometriyada <b>radianda</b> ishlaydi. <code>sin(30)</code>
  30 daraja emas, 30 radian. Daraja kerak boʻlsa, sozlamalardan
  <i>degrees</i> ni tanlang yoki <code>sin(30°)</code> deb belgini
  qoʻying (SAT-77).
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">40 s</span></p>
  <div class="ps-stem__q">
    <p>The system of equations <i>y</i> = 2<i>x</i> − 1 and
    <i>y</i> = −<i>x</i> + 5 has solution (<i>x</i>, <i>y</i>). What is
    the value of <i>x</i> + <i>y</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>5</li>
    <li>2</li>
    <li>3</li>
    <li>−1</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 5</p>
      <p>Ikkalasini Desmosga kiriting: kesishish (2, 3). Demak
      x + y = 2 + 3 = 5.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2</span>
  <span class="ps-trap__why">Bu <b>faqat x</b>. Desmos toʻgʻri nuqtani
  berdi, oʻquvchi esa savolni oxirigacha oʻqimadi. Desmos tez, lekin u
  savolni oʻqib bermaydi.</span>
</div>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">50 s</span></p>
  <div class="ps-stem__q">
    <p>What is the positive solution to the equation
    <i>x</i>² − 4 = 3<i>x</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>4</li>
    <li>−1</li>
    <li>3</li>
    <li>1</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 4</p>
      <p><code>y=x^2-4</code> va <code>y=3x</code> ni kiriting: ikkita
      kesishish bor — x = −1 va x = 4. Savol musbatini soʻragan.</p>
      <p>Tekshiruv: 16 − 4 = 12 va 3 × 4 = 12 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">−1</span>
  <span class="ps-trap__why">Bu ham haqiqiy yechim — lekin manfiy.
  Ikkita kesishish boʻlganda savol qaysi birini soʻraganini
  aniqlang.</span>
</div>

<h3>Exam English — Desmos qachon kerakligini aytadigan iboralar</h3>

<ul class="ps-phrase">
  <li><b>the system of equations</b><span>tenglamalar sistemasi → ikki grafik</span></li>
  <li><b>the graph of the equation</b><span>tenglamaning grafigi</span></li>
  <li><b>crosses the x-axis</b><span>x oʻqini kesadi → nollar</span></li>
  <li><b>the solution to the equation</b><span>tenglamaning yechimi</span></li>
  <li><b>approximately</b><span>taxminan — oʻnli javob kutilyapti</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">Kesishish topildi → x yozildi</p>
  <p class="pe-good">Savolga qaytish: x mi, y mi, yoki x + y mi?</p>
  <p class="pe-fix__why">Desmos nuqtani beradi, javobni emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«Kesishish yoʻq ekan»</p>
  <p class="pe-good">Uzoqlashtiring va yana qarang</p>
  <p class="pe-fix__why">Ekrandan tashqarida qolgan yechim yoʻq
  yechim emas.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Desmos qoʻlni almashtirmaydi — u <b>tekshiradi</b>. Ideal tartib:
  savolni oʻqing, qoʻlda yoʻlni koʻring, keyin Desmosda 10 soniyada
  tasdiqlang. Faqat Desmosga tayangan oʻquvchi grid-in savolda
  qoqiladi.
</div>

<h3>Toʻrtinchi qoʻllanish — variantlarni chizib solishtirish</h3>

<p>«Which equation could represent the graph shown?» degan savolda
Desmos eng tez ishlaydi: <b>toʻrtala variantni ham</b> kiriting va
qaysi biri rasmga oʻxshaganini koʻring. Hisoblash umuman
boʻlmaydi.</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Tartib</span>
  <ol>
    <li>Rasmdan ikkita aniq narsani yozib oling — masalan y bilan
        kesishish va bitta nuqta.</li>
    <li>Toʻrtala tenglamani kiriting (har biri oʻz qatorida).</li>
    <li>Chap tomondagi dumaloq belgini bosib, keraksizlarini
        oʻchirib-yoqib solishtiring.</li>
  </ol>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Desmos qatorlarni <b>oʻchirmasdan</b> yashira oladi — chap tomondagi
  rangli doirachani bosing. Shu tufayli toʻrtta variantni ketma-ket
  yoqib-oʻchirib taqqoslash bir necha soniya oladi.
</div>

<h3>Nuqtalarni ham chizish mumkin</h3>

<p>Desmos faqat funksiyalarni emas, <b>nuqtalarni</b> ham qabul qiladi:
<code>(3,7)</code> deb yozsangiz, u ekranda paydo boʻladi. «Does the
graph pass through …» yoki «which point lies on the line» savollarida
bu darrov javob beradi.</p>

<div class="pm-check">
  <p class="pm-check__t">Misol</p>
  <p><code>y=2x+1</code> va <code>(3,7)</code> ni kiriting: nuqta aynan
  chiziq ustida. Tekshiruv: 2(3) + 1 = 7 ✓</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Desmosda <b>jadval</b> ham bor: yangi qatorga jadval qoʻshib, x
  qiymatlarini yozsangiz, u har biri uchun y ni hisoblab beradi. «The
  table shows values of the function» turidagi savollarda bu qoʻlda
  hisoblashdan tezroq — ayniqsa oltita qiymat berilgan boʻlsa.
</div>

<h3>Qancha vaqt tejaydi</h3>

<table class="pe-table">
  <tr><th>Savol</th><th>Qoʻlda</th><th>Desmos bilan</th></tr>
  <tr><td>Ikki nomaʼlumli sistema</td><td>90 s</td><td>20 s</td></tr>
  <tr><td>Kvadrat tenglamaning ildizlari</td><td>60 s</td><td>15 s</td></tr>
  <tr><td>«Which graph represents …»</td><td>60 s</td><td>25 s</td></tr>
  <tr><td>Bir qadamli chiziqli tenglama</td><td>15 s</td>
      <td>25 s — <b>sekinroq</b></td></tr>
</table>

<p>Oxirgi qator qoidani beradi: <b>Desmos har doim ham tez emas.</b>
Kiritishning oʻzi vaqt oladi, shuning uchun oddiy savolni qoʻlda
yechish tezroq. Desmos ogʻir savollar uchun saqlanadi.</p>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  How would you solve 5<i>x</i> − 2 = 2<i>x</i> + 7 with Desmos?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Ikki qator: y = 5x − 2 va y = 2x + 7;
  kesishish x = 3 da.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Find the zeros of <i>x</i>² − 7<i>x</i> + 12.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">3 va 4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Desmos shows nothing on screen. What is the first thing to try?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Uzoqlashtirish — yechim ekrandan tashqarida
  boʻlishi mumkin.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  You type sin(30) and get −0.988. Why?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Desmos radianda ishlayapti — 30 radianning
  sinusi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  A system meets at (4, −2). What is <i>y</i> − <i>x</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−2 − 4 = −6.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>graph</b><span>grafik; chizmoq</span></li>
  <li><b>intersection</b><span>kesishish nuqtasi</span></li>
  <li><b>system of equations</b><span>tenglamalar sistemasi</span></li>
  <li><b>zero / root</b><span>nol, ildiz</span></li>
  <li><b>x-axis</b><span>x oʻqi</span></li>
  <li><b>coordinates</b><span>koordinatalar</span></li>
  <li><b>zoom out</b><span>uzoqlashtirmoq</span></li>
  <li><b>degrees mode</b><span>daraja rejimi</span></li>
  <li><b>approximately</b><span>taxminan</span></li>
  <li><b>positive solution</b><span>musbat yechim</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Tenglamani <b>ikki funksiyaga</b> boʻling; javob
        kesishishda.</li>
    <li>Koʻrinmasa — <b>uzoqlashtiring</b>; trigonometriyada
        rejimni tekshiring.</li>
    <li>Desmos nuqtani beradi; <b>savolni oʻzingiz oʻqiysiz</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-84 — Desmos II: sliders
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-84: Mastering Desmos II — Sliders for Unknown Constants",
        "category": "math",
        "order": 84,
        "summary": (
            "Savolda x dan boshqa harf boʻlsa — Desmos slider taklif qiladi. "
            "Shartni bajarguncha suring va qiymatni oʻqing."
        ),
        "stories":  ["Four Greenhouses, One Difference"],
        "content": """
<h2>SAT-84: Mastering Desmos II — Sliders for Unknown Constants</h2>

<p>SAT-83 da nomaʼlum <b>x</b> edi va javob kesishishda turardi. Bu
darsda nomaʼlum <b>doimiy</b> — a, b, k, c. Grafikning oʻzi emas,
grafikni <i>boshqaradigan</i> son soʻralyapti. Desmosning slider'i
aynan shu savol turi uchun yaratilgan.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>slider'ni bir bosishda qoʻshasiz;</li>
    <li>shart bajarilguncha surib, qiymatni oʻqiysiz;</li>
    <li>qadamni (step) sozlab, aniq javob olasiz;</li>
    <li>«taxminan toʻgʻri» javobning tuzogʻidan qochasiz.</li>
  </ul>
</div>

<div class="ps-desmos">
  <span class="ps-desmos__t">Slider qanday paydo boʻladi</span>
  <p><code>y=ax^2</code> deb yozing. Desmos <b>a</b> ni tanimaydi va
  darrov «add slider: a» degan tugmani koʻrsatadi. Bosing — pastda
  surgich chiqadi, grafik esa siz surganingizda jonli
  oʻzgaradi.</p>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">The move</span>
  <ol>
    <li>Tenglamani harfi bilan birga kiriting.</li>
    <li>Slider qoʻshing.</li>
    <li>Shartni ham <b>chizmaga aylantiring</b>: nuqta boʻlsa
        <code>(2,12)</code> deb kiriting; ikkinchi grafik boʻlsa uni
        ham chizing.</li>
    <li>Shart bajarilgan joyda toʻxtang va sonni oʻqing.</li>
  </ol>
</div>

<h3>Birinchi tur — grafik nuqtadan oʻtsin</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">45 s</span></p>
  <div class="ps-stem__q">
    <p>The graph of <i>y</i> = <i>a</i><i>x</i>² in the xy-plane passes
    through the point (2, 12). What is the value of <i>a</i>?</p>
  </div>
  <ol class="ps-ch">
    <li>3</li>
    <li>6</li>
    <li>12</li>
    <li>1/3</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 3</p>
      <p>Desmosda: <code>y=ax^2</code>, slider qoʻshing, keyin
      <code>(2,12)</code> nuqtasini kiriting. a ni suring — parabola
      nuqtaga a = 3 da tegadi.</p>
      <p>Qoʻlda: 12 = a × 4, demak a = 3 ✓</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">6</span>
  <span class="ps-trap__why">12 ni 2 ga boʻlgan — yaʼni x ni kvadratga
  koʻtarishni unutgan. Slider bu xatoni qilishga imkon bermaydi, chunki
  a = 6 da parabola nuqtadan ancha yuqoridan oʻtadi.</span>
</div>

<h3>Ikkinchi tur — nechta yechim boʻlsin</h3>

<p>SAT'ning eng yoqtirgan slider savoli: «for what value of k does the
equation have exactly one solution». Qoʻlda bu diskriminant demakdir
(SAT-36). Desmosda esa bu shunchaki <b>koʻrish</b>: k ni suring va
ikkita kesishish bittaga aylangan lahzada toʻxtang.</p>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>For what value of <i>k</i> does the line <i>y</i> = <i>k</i>
    intersect the graph of <i>y</i> = <i>x</i>² − 4<i>x</i> + 3 at
    exactly one point?</p>
  </div>
  <ol class="ps-ch">
    <li>−1</li>
    <li>3</li>
    <li>2</li>
    <li>1</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) −1</p>
      <p>Gorizontal chiziq parabolani faqat <b>uchida</b> bir marta
      kesadi. Uch: x = 2 da, va u yerda y = 4 − 8 + 3 = −1.</p>
      <p>Slider bilan: k ni pastga suring — ikkita kesishish yaqinlashib
      boradi va k = −1 da bitta boʻlib qoladi.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">2</span>
  <span class="ps-trap__why">Bu uchning <b>x</b> koordinatasi. Savol esa
  gorizontal chiziqning balandligini — yaʼni <b>y</b> ni soʻragan.</span>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling — slider aniqligi</span>
  Surgichni qoʻl bilan surganingizda tushgan joyingizdagi son
  chiqadi — odatda 2.9 yoki 3.07 kabi notekis oʻnli. Javob 1/3 boʻlsa,
  ekranda 0.33 emas, 0.34 turgan boʻlishi mumkin. Slider ostidagi
  sonlarga bosib <b>min, max va step</b> ni oʻzingiz belgilang (step
  = 0.01), yoki topilgan taxminni qoʻlda tasdiqlang.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻnli sonni kasrga qaytarishni bilib qoʻying: 0.5 = 1/2, 0.25 = 1/4,
  0.333… = 1/3, 0.2 = 1/5, 0.75 = 3/4. Slider deyarli har doim oʻnli
  beradi, javob variantlari esa kasr boʻladi.
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">Uchinchi tur — variantlarni sinash</span>
  <p>Slider'ning eng sodda ishlatilishi: harf oʻrniga <b>toʻrtta
  variantni birma-bir</b> qoʻyib grafikni kuzatish. Bu SAT-82 dagi
  backsolving'ning grafik koʻrinishi va koʻpincha eng tez yoʻl —
  ayniqsa shart «kesishmaydi» yoki «ikki marta kesadi» kabi
  boʻlsa.</p>
</div>

<h3>Exam English — slider kerakligining belgilari</h3>

<ul class="ps-phrase">
  <li><b>where a is a constant</b><span>bunda a — doimiy son</span></li>
  <li><b>for what value of k</b><span>k ning qaysi qiymatida</span></li>
  <li><b>exactly one solution</b><span>aynan bitta yechim</span></li>
  <li><b>no real solutions</b><span>haqiqiy yechimi yoʻq</span></li>
  <li><b>passes through the point</b><span>nuqtadan oʻtadi</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">a = 12 ÷ 2 = 6</p>
  <p class="pe-good">12 = a × 2², demak a = 3</p>
  <p class="pe-fix__why">x avval kvadratga koʻtariladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Slider 0.3 koʻrsatdi → javob 0.3</p>
  <p class="pe-good">Qadamni kichraytiring: javob 1/3 boʻlishi mumkin</p>
  <p class="pe-fix__why">Surgichning aniqligi javobning aniqligi
  emas.</p>
</div>

<h3>Toʻrtinchi tur — «nechta yechim» savollarining oilasi</h3>

<p>Bitta slider bir savolga emas, <b>butun bir savollar oilasiga</b>
javob beradi. Yuqoridagi parabolada k ni surib boring va kesishishlar
sonini kuzating — uch xil holat ketma-ket koʻrinadi.</p>

<table class="pe-table">
  <tr><th>k</th><th>Nechta kesishish</th><th>Savolda qanday aytiladi</th></tr>
  <tr><td>k &lt; −1</td><td>0</td><td>no real solutions</td></tr>
  <tr><td>k = −1</td><td>1</td><td>exactly one solution</td></tr>
  <tr><td>k &gt; −1</td><td>2</td><td>two distinct solutions</td></tr>
</table>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu jadval SAT-36 dagi diskriminantning <b>koʻrinadigan</b> shakli.
  Qoʻlda ishlaganda ishorani hisoblaysiz; Desmosda esa parabola bilan
  chiziqning ajralib ketishini koʻz bilan koʻrasiz. Ikkalasi ham bir
  narsani aytadi, lekin ikkinchisi esdan chiqmaydi.
</div>

<h3>Ikki slider</h3>

<p>Savolda ikkita nomaʼlum doimiy boʻlsa (masalan a va b), Desmos
ikkalasiga ham surgich beradi. Bunday savol kamdan-kam uchraydi va
odatda ikkita shart bilan keladi: bittasini bajaring, keyin
ikkinchisini. <b>Bir vaqtda ikkalasini surmang</b> — ilgari topilgan
shartni buzib yuborasiz.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Slider bilan topilgan javob <b>taxmin</b>, isbot emas. Variantlardan
  ikkitasi bir-biriga yaqin boʻlsa (masalan 0.33 va 0.35), surgichga
  ishonmang — qoʻlda qoʻyib tekshiring.
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  The graph of <i>y</i> = <i>a</i><i>x</i>² passes through (3, 18).
  Find <i>a</i>.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">18 = a × 9, demak a = 2.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  For what <i>k</i> does <i>y</i> = <i>k</i> touch
  <i>y</i> = <i>x</i>² − 6<i>x</i> + 5 exactly once?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Uch x = 3 da: 9 − 18 + 5 = −4. Demak
  k = −4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Your slider reads 0.25. Which fraction is that?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">1/4.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Desmos does not offer a slider for your letter. Why might that be?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">Siz x yoki y ni yozgansiz — ular
  oʻzgaruvchi, doimiy emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  The graph of <i>y</i> = <i>a</i><i>x</i>² passes through (2, −8).
  Find <i>a</i>.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">−8 = a × 4, demak a = −2 (parabola
  pastga qaraydi).</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>slider</b><span>surgich</span></li>
  <li><b>constant</b><span>doimiy son</span></li>
  <li><b>parameter</b><span>parametr</span></li>
  <li><b>passes through</b><span>… dan oʻtadi</span></li>
  <li><b>exactly one solution</b><span>aynan bitta yechim</span></li>
  <li><b>no real solutions</b><span>haqiqiy yechimi yoʻq</span></li>
  <li><b>step</b><span>qadam (surgich aniqligi)</span></li>
  <li><b>vertex</b><span>uch (parabola cho'qqisi)</span></li>
  <li><b>touch</b><span>urinmoq, bir nuqtada tegmoq</span></li>
  <li><b>drag</b><span>surmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>x dan boshqa harf koʻrsangiz — <b>slider</b>.</li>
    <li>Shartni ham chizmaga aylantiring: nuqta yoki ikkinchi
        grafik.</li>
    <li>Oʻnli javobni <b>kasrga qaytaring</b>; qadamga ishonmang.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-85 — Desmos III: inequalities
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "SAT-85: Mastering Desmos III — Inequalities and Bounded Regions",
        "category": "math",
        "order": 85,
        "summary": (
            "Tengsizlikni kiritsangiz, Desmos soha boʻyaydi. Ikkitasining "
            "ustma-ust tushgan joyi — javob."
        ),
        "stories":  ["What Will Fit in the Hall"],
        "content": """
<h2>SAT-85: Mastering Desmos III — Inequalities and Bounded Regions</h2>

<p>Desmos darslarining uchinchisi va eng foydalisi. Tengsizliklar
sistemasi qoʻlda sekin va xatoga moyil — chunki har bir nuqtani ikki
shartga alohida tekshirish kerak. Desmosda esa
<mark>javob koʻzga koʻrinib turadi</mark>: u boʻyalgan sohaning
ichida.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>tengsizlikni Desmosga toʻgʻri kiritasiz;</li>
    <li>ikki shartning kesishgan sohasini oʻqiysiz;</li>
    <li>nuqtalarni ham chizib, javobni koʻz bilan tanlaysiz;</li>
    <li>qattiq tengsizlikning chegara tuzogʻini bilasiz.</li>
  </ul>
</div>

<div class="ps-desmos">
  <span class="ps-desmos__t">Keystrokes</span>
  <p><code>y&gt;=2x-3</code> deb yozing — Desmos uni ≥ ga aylantiradi va
  chiziqning ustidagi sohani boʻyaydi. Ikkinchi qatorga
  <code>y&lt;-x+6</code>. Endi ikki rang bor; <b>ikkalasi ustma-ust
  tushgan</b>, quyuqroq joy — sistemaning yechimi.</p>
  <p>Nuqtani tekshirish uchun uni shunchaki kiriting:
  <code>(1,2)</code>. U quyuq sohada turibdimi — javob shu.</p>
</div>

<div class="ps-tactic">
  <span class="ps-tactic__t">The move</span>
  <ol>
    <li>Ikkala tengsizlikni kiriting.</li>
    <li>Toʻrtta variant nuqtasini ham kiriting.</li>
    <li>Quyuq sohada turgan yagona nuqtani tanlang.</li>
  </ol>
</div>

<h3>Chegara: uzuq chiziq va toʻliq chiziq</h3>

<p>Bu farq bir savolning butun javobini hal qiladi.</p>

<table class="pe-table">
  <tr><th>Belgi</th><th>Chiziq</th><th>Chegara kiradimi</th></tr>
  <tr><td>&lt; yoki &gt;</td><td>uzuq (dashed)</td><td>Yoʻq</td></tr>
  <tr><td>≤ yoki ≥</td><td>toʻliq (solid)</td><td>Ha</td></tr>
</table>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Ehtiyot boʻling</span>
  Aynan chiziq ustida turgan nuqta — SAT'ning sevimli tuzogʻi. U
  <b>≤ uchun toʻgʻri, &lt; uchun notoʻgʻri</b>, va ekranda ikkalasi ham
  bir xil koʻrinadi. Shubha boʻlsa, sonlarni qoʻyib tekshiring.
</div>

<h3>SAT savollari</h3>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">60 s</span></p>
  <div class="ps-stem__q">
    <p>Which point is a solution to the system of inequalities
    <i>y</i> ≥ 2<i>x</i> − 3 and <i>y</i> &lt; −<i>x</i> + 6?</p>
  </div>
  <ol class="ps-ch">
    <li>(1, 2)</li>
    <li>(4, 1)</li>
    <li>(0, 7)</li>
    <li>(3, 3)</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) (1, 2)</p>
      <p>Birinchi shart: 2 ≥ 2(1) − 3 = −1 ✓. Ikkinchi shart:
      2 &lt; −1 + 6 = 5 ✓</p>
      <p>Boshqalar: (4, 1) da 1 ≥ 5 emas; (0, 7) da 7 &lt; 6 emas.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">(3, 3)</span>
  <span class="ps-trap__why">Birinchi shartni qanoatlantiradi
  (3 ≥ 3, chunki ≥ tenglikni oladi), lekin ikkinchisida <b>aynan
  chegarada</b> turibdi: 3 &lt; 3 <b>notoʻgʻri</b>. Qattiq tengsizlik
  oʻz chizigʻini ichiga olmaydi.</span>
</div>

<h3>Matnli shartlar — sohaning asl maʼnosi</h3>

<p>SAT tengsizliklarni deyarli har doim <b>cheklov</b> sifatida beradi:
budjet, joy, vaqt, eng kamida shuncha. «At most» — ≤, «at least» — ≥
(SAT-14). Desmos bu shartlarni oʻsha-oʻsha usulda boʻyaydi.</p>

<div class="ps-stem">
  <p class="ps-stem__tag">SAT-style question <span class="ps-time">85 s</span></p>
  <div class="ps-stem__q">
    <p>A student buys notebooks at $4 each and pens at $2 each. She has
    at most $60 to spend and needs at least 8 notebooks. Which
    combination is possible?</p>
  </div>
  <ol class="ps-ch">
    <li>10 notebooks and 10 pens</li>
    <li>5 notebooks and 20 pens</li>
    <li>12 notebooks and 8 pens</li>
    <li>8 notebooks and 15 pens</li>
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: A) 10 notebooks and 10 pens</p>
      <p>Pul: 10 × 4 + 10 × 2 = 40 + 20 = 60, va 60 ≤ 60 ✓
      Daftar: 10 ≥ 8 ✓</p>
      <p>Qolganlari: 5 daftar 8 dan kam; 12 va 8 → 64 dollar;
      8 va 15 → 62 dollar.</p>
    </div>
  </details>
</div>

<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">8 notebooks and 15 pens</span>
  <span class="ps-trap__why">Daftar sharti aynan bajarilgan (8 ≥ 8) va
  bu diqqatni chalgʻitadi — lekin pul 62 dollar, yaʼni budjetdan
  ortiq. <b>Ikkala shartni ham</b> tekshirish kerak.</span>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «At most $60» — 60 <b>ham</b> mumkin (≤). Birinchi variant aynan 60
  dollarni sarflaydi va shu sababli toʻgʻri. Agar savolda «less than
  $60» yozilganida, aynan oʻsha variant notoʻgʻri boʻlar edi. Bitta
  soʻz javobni almashtiradi.
</div>

<h3>Exam English</h3>

<ul class="ps-phrase">
  <li><b>at most</b><span>koʻpi bilan → ≤</span></li>
  <li><b>at least</b><span>eng kamida → ≥</span></li>
  <li><b>no more than</b><span>… dan ortiq emas → ≤</span></li>
  <li><b>a solution to the system</b><span>sistemaning yechimi</span></li>
  <li><b>the shaded region</b><span>boʻyalgan soha</span></li>
  <li><b>which combination is possible</b><span>qaysi kombinatsiya mumkin</span></li>
</ul>

<div class="pe-fix">
  <p class="pe-bad">(3, 3) — chegarada, demak yechim</p>
  <p class="pe-good">&lt; chegarani olmaydi; yechim emas</p>
  <p class="pe-fix__why">Uzuq chiziq — chiziqning oʻzi kirmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Bitta shart bajarildi → javob</p>
  <p class="pe-good">Ikkala shartni ham tekshiring</p>
  <p class="pe-fix__why">Sistemada yechim ikkalasiga birdan tegishli
  boʻlishi shart.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Bu savol turida Desmos shart emas — toʻrtta nuqtani qoʻlda qoʻyib
  chiqish 40 soniya oladi. Desmos ustunligi <b>soha soʻralganda</b>
  koʻrinadi: «which graph shows the solution set» degan savolda
  boʻyalgan rasm darrov solishtiriladi.
</div>

<h3>Yashirin uchinchi va toʻrtinchi shart</h3>

<p>Matnli cheklov masalalarida savolda yozilmagan, lekin har doim
mavjud boʻlgan ikkita shart bor: <b>miqdorlar manfiy boʻla
olmaydi</b>. Daftar soni ham, ruchka soni ham nol yoki undan katta.
Shuning uchun haqiqiy soha butun tekislikda emas, faqat birinchi
chorakda yotadi.</p>

<div class="ps-desmos">
  <span class="ps-desmos__t">Toʻliq kiritish</span>
  <p>Yuqoridagi masala Desmosda toʻrtta qator: <code>4x+2y&lt;=60</code>,
  <code>x&gt;=8</code>, <code>x&gt;=0</code>, <code>y&gt;=0</code>.
  Toʻrttasi ustma-ust tushgan kichkina uchburchaksimon soha — mumkin
  boʻlgan barcha xaridlar.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yana bir yashirin shart: daftar <b>butun son</b> boʻlishi kerak —
  yarim daftar sotilmaydi. Desmos buni bilmaydi va sohani tekis
  boʻyayveradi. Shuning uchun «which combination is possible» degan
  savolda javob har doim variantlar ichidan tanlanadi, sohadan
  emas.
</div>

<h3>«Which graph shows the solution set»</h3>

<p>Bu savolda toʻrtta rasm beriladi va sizdan toʻgʻrisini tanlash
soʻraladi. Ikkita narsaga qarang, shu yetadi:</p>

<div class="ps-tactic">
  <span class="ps-tactic__t">Ikki tekshiruv</span>
  <ol>
    <li><b>Chiziq turi:</b> qattiq tengsizlik uzuq chiziq beradi.
        Bu koʻpincha ikkita rasmni darrov oʻchiradi.</li>
    <li><b>Bitta oson nuqta:</b> odatda (0, 0). Uni ikkala
        tengsizlikka qoʻying va boʻyalgan tomon toʻgʻri
        tanlanganini tekshiring.</li>
  </ol>
</div>

<div class="pm-check">
  <p class="pm-check__t">(0, 0) sinovi</p>
  <p>y ≥ 2x − 3 uchun: 0 ≥ −3 ✓ — demak boshlangʻich nuqta
  <b>boʻyalgan</b> tomonda boʻlishi kerak. Rasm buning teskarisini
  koʻrsatsa, u notoʻgʻri.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
  Is (2, 5) a solution to <i>y</i> &gt; 2<i>x</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">5 &gt; 4 ✓ — ha.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
  Is (2, 4) a solution to <i>y</i> &gt; 2<i>x</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 &gt; 4 notoʻgʻri — yoʻq, chegarada
  turibdi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
  Is (2, 4) a solution to <i>y</i> ≥ 2<i>x</i>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">4 ≥ 4 ✓ — ha. Bitta belgi hammasini
  oʻzgartirdi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
  Translate "at most 30 hours" into a symbol.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">≤ 30.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
  With $60, is 14 notebooks at $4 and 2 pens at $2 possible?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">56 + 4 = 60 ≤ 60 ✓ — mumkin.</p></details>
</div>

<h3>Key words</h3>
<ul class="pe-gloss">
  <li><b>inequality</b><span>tengsizlik</span></li>
  <li><b>shaded region</b><span>boʻyalgan soha</span></li>
  <li><b>solution set</b><span>yechimlar toʻplami</span></li>
  <li><b>boundary</b><span>chegara</span></li>
  <li><b>dashed line</b><span>uzuq chiziq</span></li>
  <li><b>solid line</b><span>toʻliq chiziq</span></li>
  <li><b>at most / at least</b><span>koʻpi bilan / eng kamida</span></li>
  <li><b>constraint</b><span>cheklov</span></li>
  <li><b>overlap</b><span>ustma-ust tushgan joy</span></li>
  <li><b>combination</b><span>kombinatsiya</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Ikki tengsizlik → javob <b>quyuq</b> sohada.</li>
    <li><b>&lt; uzuq, ≤ toʻliq</b> — chegara tuzogʻi shu yerda.</li>
    <li>Nuqtani tekshirganda <b>ikkala</b> shartni ham
        yuriting.</li>
  </ul>
</div>
""",
    },
]
