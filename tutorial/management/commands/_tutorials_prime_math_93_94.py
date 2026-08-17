# -*- coding: utf-8 -*-
"""Prime Math — darslar 93–94 (yosh va sonlar masalalari; birliklar).

**Blok G ni YOPADI: Matnli masalalar ustaxonasi (85–94).**
Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md

  mashqlar — practice/management/commands/_practice_pm_93_94.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_93_94.py

⚠️ Bu ikkilik blokni yakunlaydi, shuning uchun har ikkalasi ham
   oldingi darslarga ochiq tayanadi: PM-93 jadval usulini (PM-86)
   yosh masalalariga qoʻllaydi, PM-94 esa PM-88 dagi birlik xatosini
   umumlashtirib, butun blok uchun oxirgi filtr beradi — «berilgan
   maʼlumot yetarlimi?».

⚠️ Har ikkala darsning oʻz YAKKA GʻOYASI bor va u boshqa hech qayerda
   takrorlanmaydi:
     PM-93 — yoshlar FARQI hech qachon oʻzgarmaydi;
     PM-94 — yuza birliklarida koeffitsiyent KVADRATGA koʻtariladi
             (1 m² = 10 000 sm², 100 emas).

⚠️ Kumulyativ chegaralar:
  • PM-93 — yosh masalalari (jadval: hozir / keyin / oldin) va sonlar
    haqidagi masalalar (ketma-ket sonlar, ikki xonali son 10a + b).
    ⛔ Kvadrat tenglamaga olib keladigan yosh masalalari YOʻQ;
  • PM-94 — uzunlik, massa, sigʻim, yuza va vaqt birliklari; ortiqcha
    va yetishmayotgan maʼlumot. ⛔ Hajm birliklari (sm³ ↔ m³) faqat
    eslatib oʻtiladi, mashq qilinmaydi — hajm PM-74 da boʻlgan.
  • Faol ishlatiladi: razryad (PM-1), tenglama (PM-36/37), nomaʼlum
    tanlash va jadval (PM-86), toʻrt qadam (PM-85), birlik moslash
    (PM-88), birlik narx (PM-92), yuza (PM-68).

⚠️ Arifmetika darvozasi: scratchpad/verify_pm_93_94.py hamma sonni
   qayta hisoblaydi. Yosh masalalari FORMULA bilan emas, YIL-BAYIL
   simulyatsiya bilan tekshiriladi (ikkalasiga ham bir xil yil
   qoʻshiladi va shart oʻsha yilda bajarilishi talab qilinadi);
   birliklar esa bitta asosiy birlikka keltirib solishtiriladi.

    python manage.py import_tutorials \\
        tutorial/management/commands/_tutorials_prime_math_93_94.py --author=prime
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
    # PM-93 — yosh masalalari va sonlar haqidagi masalalar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-93: Yosh masalalari va sonlar haqidagi masalalar",
        "category": "math",
        "order": 93,
        "summary": (
            "Yosh masalalarining kaliti bitta: yoshlar farqi hech qachon "
            "oʻzgarmaydi. Sonlar masalalarida esa ikki xonali son 10a + b "
            "koʻrinishida yoziladi — razryad shu yerda ish beradi."
        ),
        "stories": ["Ota va oʻgʻil"],
        "content": """
<h2>PM-93: Yosh masalalari va sonlar haqidagi masalalar</h2>

<p>Ota 35 yoshda, oʻgʻli 5 yoshda. Ota oʻgʻlidan <b>7 marta</b> katta.
Yetti yildan keyin-chi? Ota 42, oʻgʻli 12 — endi atigi 3,5 marta.</p>

<p>Nisbat oʻzgardi. Lekin bir narsa oʻzgarmadi va hech qachon
oʻzgarmaydi: <b>ular orasidagi 30 yoshlik farq</b>. Ikkalasi ham
yiliga bir yoshdan kattaradi.</p>

<p>Yosh masalalarining butun kaliti shu jumlada. Qolgani — jadval
tuzish (PM-86) va tenglama yechish (PM-37).</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>yoshlar farqining oʻzgarmasligidan foydalanasiz;</li>
    <li>«hozir / keyin / oldin» jadvalini tuzasiz;</li>
    <li>manfiy javob nimani anglatishini bilib olasiz;</li>
    <li>ketma-ket sonlar va ikki xonali sonni harf bilan yozasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Yosh masalalarining kaliti</span>
  <span class="pe-chip pe-chip--s">yoshlar farqi</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">oʻzgarmas</span>
</div>

<h3>1. Hamma bir xil tezlikda kattaradi</h3>

<p>Bir yil oʻtsa, hammaning yoshiga <b>bittadan</b> qoʻshiladi. Shuning
uchun jadvalning har bir ustunida bir xil son qoʻshiladi yoki
ayiriladi.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Kim</th><th>5 yil oldin</th><th>Hozir</th><th>x yildan keyin</th></tr>
  <tr><td>Ota</td><td class="pm-word__sym">30</td><td>35</td><td>35 + x</td></tr>
  <tr><td>Oʻgʻil</td><td class="pm-word__sym">0</td><td>5</td><td>5 + x</td></tr>
  <tr><td>Farqi</td><td class="pm-word__sym">30</td><td>30</td><td>30</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Eng koʻp uchraydigan xato</p>
  <p>«Ota oʻgʻlidan 30 yosh katta, 10 yildan keyin 40 yosh katta
  boʻladi» — bu <b>notoʻgʻri</b>. Oʻn yil ikkalasiga ham qoʻshiladi,
  shuning uchun farq oʻsha 30 boʻlib qoladi. Oʻzgaradigan narsa —
  <b>nisbat</b> (necha marta katta), farq emas.</p>
</div>

<h3>2. Birinchi misol — «necha yildan keyin?»</h3>

<p><b>Masala.</b> Ota 35 yoshda, oʻgʻli 5 yoshda. Necha yildan keyin
ota oʻgʻlidan 4 marta katta boʻladi?</p>

<p><b>Reja:</b> x — oʻtadigan yillar soni. Ikkalasining yoshiga ham
x qoʻshiladi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">35 + x = 4(5 + x)</span>
    <span class="pm-solve__why">Ota oʻgʻlidan 4 marta katta boʻlsin</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">35 + x = 20 + 4x</span>
    <span class="pm-solve__why">Qavsni ochdik (PM-33)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15 = 3x</span>
    <span class="pm-solve__why">x va 20 ni boshqa tomonga oʻtkazdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 5</span>
    <span class="pm-solve__why">3 ga boʻldik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>5 yildan keyin ota 40, oʻgʻil 10 yoshda boʻladi. 40 ÷ 10 = 4 ✓
  Farqi esa hamon 30 ✓
  <br><b>Javob:</b> 5 yildan keyin.</p>
</div>

<h3>3. Ikkinchi misol — «necha yil oldin?»</h3>

<p><b>Masala.</b> Hozir ota oʻgʻlidan 3 marta katta. 10 yil oldin
7 marta katta edi. Hozir har biri necha yoshda?</p>

<p><b>Reja:</b> bu safar nomaʼlum — oʻgʻilning hozirgi yoshi. Uni x deb
olamiz (PM-86: qolganlari shunga qarab aytilgan), unda ota 3x.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Kim</th><th>Hozir</th><th>10 yil oldin</th></tr>
  <tr><td>Oʻgʻil</td><td class="pm-word__sym">x</td><td>x − 10</td></tr>
  <tr><td>Ota</td><td class="pm-word__sym">3x</td><td>3x − 10</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x − 10 = 7(x − 10)</span>
    <span class="pm-solve__why">Oʻsha paytda 7 marta katta edi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x − 10 = 7x − 70</span>
    <span class="pm-solve__why">Qavsni ochdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 = 4x</span>
    <span class="pm-solve__why">3x va 70 ni boshqa tomonga oʻtkazdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 15, ota 45</span>
    <span class="pm-solve__why">4 ga boʻldik, keyin 3 ga koʻpaytirdik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Hozir: 45 va 15 → 45 ÷ 15 = 3 ✓
  <br>10 yil oldin: 35 va 5 → 35 ÷ 5 = 7 ✓
  <br>Farqi ikkala paytda ham 30 ✓
  <br><b>Javob:</b> oʻgʻil 15, ota 45 yoshda.</p>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">«Oldin» boʻlsa, ikkalasidan ham ayiring</p>
  <p>Faqat bittasining yoshidan 10 ni ayirish — juda koʻp uchraydigan
  xato. Vaqt hamma uchun bir xil oʻtadi: ustundagi <b>har bir</b>
  qatordan 10 ayiriladi.</p>
</div>

<h3>4. Manfiy javob — xato emas, maʼlumot</h3>

<p><b>Masala.</b> Opa 12 yoshda, singlisi 8 yoshda. Necha yildan keyin
opa singlisidan 2 marta katta boʻladi?</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 + x = 2(8 + x)</span>
    <span class="pm-solve__why">Shartni yozdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">12 + x = 16 + 2x</span>
    <span class="pm-solve__why">Qavsni ochdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = −4</span>
    <span class="pm-solve__why">Manfiy chiqdi (PM-10)</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Manfiy x nimani bildiradi?</p>
  <p>Bu hodisa <b>kelajakda emas, oʻtmishda</b> boʻlgan degani. Toʻrt
  yil oldin opa 8, singlisi 4 yoshda edi — va 8 roppa-rosa 4 ning ikki
  barobari ✓ Tenglama xato qilmadi; u bizga vaqt oʻqining teskari
  tomonini koʻrsatdi.</p>
</div>

<h3>5. Sonlar haqidagi masalalar</h3>

<p>Ikkinchi oila — sonlarning oʻzi haqidagi masalalar. Ular ham
xuddi shu yoʻldan yechiladi: nomaʼlumni tanlab, qolganini u orqali
yozamiz.</p>

<h4>Ketma-ket sonlar</h4>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Qanday sonlar</th><th>Qanday yoziladi</th><th>Misol</th></tr>
  <tr><td>Ketma-ket uchta son</td>
    <td class="pm-word__sym">x, x + 1, x + 2</td><td>23, 24, 25</td></tr>
  <tr><td>Ketma-ket uchta juft son</td>
    <td class="pm-word__sym">x, x + 2, x + 4</td><td>10, 12, 14</td></tr>
  <tr><td>Ketma-ket uchta toq son</td>
    <td class="pm-word__sym">x, x + 2, x + 4</td><td>7, 9, 11</td></tr>
</table></div>

<p><b>Masala.</b> Ketma-ket uchta sonning yigʻindisi 72. Sonlarni
toping.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">x + (x + 1) + (x + 2) = 72</span>
    <span class="pm-solve__why">Uchta ketma-ket son</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3x + 3 = 72</span>
    <span class="pm-solve__why">Oʻxshash hadlar</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 23 → 23, 24, 25</span>
    <span class="pm-solve__why">3 ni ayirib, 3 ga boʻldik</span>
  </div>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Uchta yaqin sonning yigʻindisi 72 boʻlsa, ularning har biri
  72 ÷ 3 = 24 atrofida. Javob 23, 24, 25 — roppa-rosa shunday. Aslida
  oʻrtadagi son har doim oʻrtacha arifmetikka teng (PM-78).</span>
</div>

<h4>Ikki xonali son — razryad ish beradi</h4>

<p>Ikki xonali sonni <b>a + b</b> deb yozib boʻlmaydi. 57 soni 5 va 7
raqamlaridan iborat, lekin uning qiymati 5 + 7 = 12 emas.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki xonali son (PM-1)</span>
  <span class="pe-chip pe-chip--o">10a</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">b</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--aux">a — oʻnliklar, b — birliklar</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">57 = 10 × 5 + 7</p>
  <p class="pe-ex__uz">Besh oʻnlik va yetti birlik.</p>
  <p class="pe-ex__why">Raqamlar oʻrni almashsa: 75 = 10 × 7 + 5.</p>
</div>

<p><b>Masala.</b> Ikki xonali sonning raqamlari yigʻindisi 12. Raqamlar
oʻrni almashtirilsa, son 18 ga ortadi. Sonni toping.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">a + b = 12</span>
    <span class="pm-solve__why">Birinchi shart</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">10b + a = (10a + b) + 18</span>
    <span class="pm-solve__why">Almashgan son 18 ga katta</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">9b − 9a = 18 → b − a = 2</span>
    <span class="pm-solve__why">Ixchamladik va 9 ga boʻldik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">a = 5, b = 7 → son 57</span>
    <span class="pm-solve__why">Yigʻindi 12, farq 2 (PM-87 usuli)</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>5 + 7 = 12 ✓ Almashtirsak 75 boʻladi: 75 − 57 = 18 ✓
  <br><b>Javob:</b> son 57.</p>
</div>

<h3>Matnli masala</h3>

<p>Hozir onaning yoshi qizinikidan 4 marta katta. 6 yildan keyin ona
qizidan 3 marta katta boʻladi.</p>

<p><b>Hozir har biri necha yoshda?</b></p>

<p><b>Reja:</b> hamma narsa qizga qarab aytilgan, demak x — qizning
hozirgi yoshi. Jadval tuzamiz.</p>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Kim</th><th>Hozir</th><th>6 yildan keyin</th></tr>
  <tr><td>Qiz</td><td class="pm-word__sym">x</td><td>x + 6</td></tr>
  <tr><td>Ona</td><td class="pm-word__sym">4x</td><td>4x + 6</td></tr>
</table></div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x + 6 = 3(x + 6)</span>
    <span class="pm-solve__why">6 yildan keyingi shart</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4x + 6 = 3x + 18</span>
    <span class="pm-solve__why">Qavsni ochdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">x = 12, ona 48</span>
    <span class="pm-solve__why">3x va 6 ni oʻtkazdik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>Hozir: 48 va 12 → 48 ÷ 12 = 4 ✓
  <br>6 yildan keyin: 54 va 18 → 54 ÷ 18 = 3 ✓
  <br>Farqi ikkala paytda ham 36 ✓ — oʻzgarmadi, shunday boʻlishi
  kerak edi.
  <br><b>Javob:</b> qiz 12, ona 48 yoshda.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">Ota 30 yosh katta → 10 yildan keyin 40 yosh
  katta boʻladi</p>
  <p class="pe-fix__good">Farq hamon 30</p>
  <p class="pe-fix__why">Oʻn yil ikkalasiga ham qoʻshiladi. Oʻzgaradigan
  narsa — nisbat, farq emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">5 yil oldin: ota 35 − 5 = 30, oʻgʻil 5</p>
  <p class="pe-fix__good">Ota 30, oʻgʻil 0</p>
  <p class="pe-fix__why">Ayirish faqat bittasiga qoʻllanilgan. Ustundagi
  har bir qatordan bir xil son ayiriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Ketma-ket uchta son: x, x + 2, x + 4</p>
  <p class="pe-fix__good">x, x + 1, x + 2</p>
  <p class="pe-fix__why">x, x + 2, x + 4 — bu ketma-ket <b>juft</b>
  yoki <b>toq</b> sonlar. Oddiy ketma-ket sonlar bittadan
  farq qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">Ikki xonali son = a + b</p>
  <p class="pe-fix__good">10a + b</p>
  <p class="pe-fix__why">a — oʻnliklar raqami, uning qiymati 10 barobar
  (PM-1). 57 ≠ 5 + 7.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Aka 14, uka 9 yoshda. 6 yildan keyin
  ularning farqi qancha boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>5 yosh.</b> Farq hech qachon oʻzgarmaydi: 14 − 9 = 5. Olti
    yildan keyin 20 va 15 — farqi hamon 5.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Ota 40, oʻgʻli 8 yoshda. Necha yildan keyin
  ota oʻgʻlidan 3 marta katta boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>8 yildan keyin.</b> 40 + x = 3(8 + x) → 40 + x = 24 + 3x →
    16 = 2x → x = 8. Tekshirish: 48 va 16, 48 ÷ 16 = 3 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Hozir ona qizidan 5 marta katta. 4 yildan
  keyin 3 marta katta boʻladi. Hozir necha yoshda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Qiz 4, ona 20.</b> 5x + 4 = 3(x + 4) → 5x + 4 = 3x + 12 →
    2x = 8 → x = 4. Tekshirish: 4 yildan keyin 24 va 8, 24 ÷ 8 = 3 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Ketma-ket toʻrtta sonning yigʻindisi 90.
  Eng kichigini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>21.</b> x + (x+1) + (x+2) + (x+3) = 90 → 4x + 6 = 90 →
    4x = 84 → x = 21. Sonlar 21, 22, 23, 24; yigʻindisi 90 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Ketma-ket ikkita juft sonning yigʻindisi 46.
  Sonlarni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>22 va 24.</b> x + (x + 2) = 46 → 2x = 44 → x = 22. Juft
    sonlar ikkitadan farq qiladi. Tekshirish: 22 + 24 = 46 ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Ikki xonali sonning oʻnliklar raqami 4,
  birliklar raqami 9. Bu son qanday va raqamlar almashsa qanday
  boʻladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>49 va 94.</b> 10 × 4 + 9 = 49; almashgach 10 × 9 + 4 = 94.
    Farq 94 − 49 = 45 — u har doim 9 ning karralisi boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Ikki xonali sonning raqamlari yigʻindisi 9.
  Raqamlar almashtirilsa, son 27 ga ortadi. Sonni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>36.</b> a + b = 9; 10b + a = 10a + b + 27 → 9b − 9a = 27 →
    b − a = 3. Yigʻindisi 9, farqi 3 → a = 3, b = 6. Son 36.
    Tekshirish: 3 + 6 = 9 ✓, 63 − 36 = 27 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Yosh</b><span>tugʻilgandan beri oʻtgan yillar soni; ingl.
    age</span></li>
  <li><b>Yoshlar farqi</b><span>ikki kishi yoshi orasidagi oʻzgarmas
    ayirma; ingl. age difference</span></li>
  <li><b>Nisbat</b><span>«necha marta katta» degan savolning javobi;
    ingl. ratio</span></li>
  <li><b>Oʻzgarmas</b><span>vaqt oʻtishi bilan qiymati oʻzgarmaydigan
    kattalik; ingl. constant</span></li>
  <li><b>Ketma-ket sonlar</b><span>bittadan farq qiladigan sonlar; ingl.
    consecutive numbers</span></li>
  <li><b>Raqam</b><span>sonni yozishda ishlatiladigan belgi (0…9); ingl.
    digit</span></li>
  <li><b>Oʻnliklar raqami</b><span>ikki xonali sondagi chapdagi raqam;
    ingl. tens digit</span></li>
  <li><b>Birliklar raqami</b><span>ikki xonali sondagi oʻngdagi raqam;
    ingl. units digit</span></li>
  <li><b>Razryad</b><span>raqamning sondagi oʻrni va qiymati; ingl.
    place value</span></li>
  <li><b>Manfiy javob</b><span>hodisa oʻtmishda boʻlganini bildiruvchi
    natija; ingl. negative solution</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Yoshlar farqi hech qachon oʻzgarmaydi — faqat nisbat
      oʻzgaradi.</li>
    <li>Jadval tuzing: hozir / keyin / oldin.</li>
    <li>«Keyin» boʻlsa ikkalasiga ham qoʻshing, «oldin» boʻlsa
      ikkalasidan ham ayiring.</li>
    <li>Manfiy javob — hodisa oʻtmishda boʻlgan degani, xato
      emas.</li>
    <li>Ketma-ket sonlar: x, x + 1, x + 2. Juft va toqlari:
      x, x + 2, x + 4.</li>
    <li>Ikki xonali son 10a + b — a + b emas.</li>
    <li>Raqamlar almashganda farq har doim 9 ga boʻlinadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-94 — oʻlchov birliklari; ortiqcha va yetishmayotgan maʼlumot
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-94: Oʻlchov birliklari; ortiqcha va yetishmayotgan maʼlumot",
        "category": "math",
        "order": 94,
        "summary": (
            "Blokning oxirgi darsi ikki filtr beradi: birliklar bir xilmi "
            "va berilgan maʼlumot yetarlimi. Yuza birliklarida "
            "koeffitsiyent kvadratga koʻtariladi — 1 m² = 10 000 sm²."
        ),
        "stories": ["Retseptdagi xato — gramm va kilogramm"],
        "content": """
<h2>PM-94: Oʻlchov birliklari; ortiqcha va yetishmayotgan maʼlumot</h2>

<p>Blokning oxirgi darsi. Toʻqqizta darsda masalani oʻqishni, chizishni
va yechishni oʻrgandik. Endi ikkita oxirgi filtr qoladi — va ular
tekshirilmaganda eng koʻp ball yoʻqoladi.</p>

<p><b>Birinchi filtr:</b> hamma son bir xil birlikdami?
<br><b>Ikkinchi filtr:</b> berilgan maʼlumot yetarlimi — va ortiqchasi
yoʻqmi?</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>uzunlik, massa, sigʻim va vaqt birliklarini almashtirasiz;</li>
    <li>yuza birliklaridagi kvadrat qoidasini oʻrganasiz;</li>
    <li>masaladagi ortiqcha sonni tanib olasiz;</li>
    <li>yechib boʻlmaydigan masalani ajrata olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki filtr</span>
  <span class="pe-chip pe-chip--s">birliklar bir xilmi?</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--adv">maʼlumot yetarlimi?</span>
</div>

<h3>1. Asosiy birliklar</h3>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Nima oʻlchanadi</th><th>Bogʻlanish</th><th>Misol</th></tr>
  <tr><td>Uzunlik</td><td class="pm-word__sym">1 m = 100 sm = 1000 mm</td>
    <td>3 m 40 sm = 340 sm</td></tr>
  <tr><td>Uzunlik (katta)</td><td class="pm-word__sym">1 km = 1000 m</td>
    <td>1 km 500 m = 1500 m</td></tr>
  <tr><td>Massa</td><td class="pm-word__sym">1 kg = 1000 g</td>
    <td>2,5 kg = 2500 g</td></tr>
  <tr><td>Massa (katta)</td><td class="pm-word__sym">1 t = 1000 kg</td>
    <td>3,2 t = 3200 kg</td></tr>
  <tr><td>Sigʻim</td><td class="pm-word__sym">1 l = 1000 ml</td>
    <td>0,75 l = 750 ml</td></tr>
  <tr><td>Vaqt</td><td class="pm-word__sym">1 soat = 60 minut</td>
    <td>1 soat 30 minut = 90 minut</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p class="pe-call__t">Yagona qoida</p>
  <p>Kichik birlikka oʻtganda <b>koʻpaytiriladi</b>, katta birlikka
  oʻtganda <b>boʻlinadi</b>. Shubhalansangiz oʻzingizdan soʻrang:
  javob kattaroq chiqishi kerakmi yoki kichikroq? 2,5 kg ni grammga
  oʻgirsak, son <b>katta</b> boʻlishi shart — chunki gramm kichik
  birlik.</p>
</div>

<h3>2. Yuza birliklari — bu yerda kvadrat bor</h3>

<p>Bu darsning eng muhim yarim sahifasi. 1 m = 100 sm boʻlgani uchun
koʻpchilik 1 m² = 100 sm² deb oʻylaydi. Bu <b>yuz barobar</b>
xato.</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 205" role="img" aria-label="Bir kvadrat metr yuz katakka boʻlingan, har bir katak 100 kvadrat santimetr">
    <rect class="pm-ln" x="90" y="15" width="160" height="160" fill="none"/>
    <rect class="pm-fill pm-fill--hl" x="90" y="15" width="16" height="16"/>
    <line class="pm-ln pm-ln--dash" x1="106" y1="15" x2="106" y2="175"/>
    <line class="pm-ln pm-ln--dash" x1="122" y1="15" x2="122" y2="175"/>
    <line class="pm-ln pm-ln--dash" x1="138" y1="15" x2="138" y2="175"/>
    <line class="pm-ln pm-ln--dash" x1="154" y1="15" x2="154" y2="175"/>
    <line class="pm-ln pm-ln--dash" x1="170" y1="15" x2="170" y2="175"/>
    <line class="pm-ln pm-ln--dash" x1="186" y1="15" x2="186" y2="175"/>
    <line class="pm-ln pm-ln--dash" x1="202" y1="15" x2="202" y2="175"/>
    <line class="pm-ln pm-ln--dash" x1="218" y1="15" x2="218" y2="175"/>
    <line class="pm-ln pm-ln--dash" x1="234" y1="15" x2="234" y2="175"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="31" x2="250" y2="31"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="47" x2="250" y2="47"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="63" x2="250" y2="63"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="79" x2="250" y2="79"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="95" x2="250" y2="95"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="111" x2="250" y2="111"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="127" x2="250" y2="127"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="143" x2="250" y2="143"/>
    <line class="pm-ln pm-ln--dash" x1="90" y1="159" x2="250" y2="159"/>
    <polyline class="pm-ln pm-ln--hl" points="98,15 98,7 252,7" fill="none"/>
    <text class="pm-lbl pm-lbl--hl" x="256" y="11" text-anchor="start">100 sm²</text>
    <text class="pm-lbl" x="170" y="196" text-anchor="middle">100 sm</text>
    <text class="pm-lbl" x="44" y="99" text-anchor="middle">100 sm</text>
  </svg>
  <figcaption>Tomoni 100 sm boʻlgan kvadrat — 1 m². U 10 × 10 = 100 ta
  katakka boʻlingan; har bir katak 10 sm × 10 sm = 100 sm². Demak
  1 m² = 100 × 100 = <b>10 000</b> sm².</figcaption>
</figure>

<div class="pe-formula">
  <span class="pe-formula__label">Yuza qoidasi</span>
  <span class="pe-chip pe-chip--o">1 m = 100 sm</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">1 m² = 100<sup>2</sup> = 10 000 sm²</span>
</div>

<div class="pe-table-wrap"><table class="pm-word">
  <tr><th>Uzunlikda</th><th>Yuzada</th><th>Nega</th></tr>
  <tr><td>1 m = 100 sm</td><td class="pm-word__sym">1 m² = 10 000 sm²</td>
    <td>100 × 100</td></tr>
  <tr><td>1 sm = 10 mm</td><td class="pm-word__sym">1 sm² = 100 mm²</td>
    <td>10 × 10</td></tr>
  <tr><td>1 km = 1000 m</td><td class="pm-word__sym">1 km² = 1 000 000 m²</td>
    <td>1000 × 1000</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p class="pe-call__t">Nega kvadratga koʻtariladi?</p>
  <p>Chunki yuza — <b>ikkita</b> uzunlikning koʻpaytmasi. Har ikkala
  tomon 100 barobar kattaradi, demak yuza 100 × 100 = 10 000 barobar
  kattaradi. Xuddi shu sabab hajmda kubga koʻtariladi:
  1 m<sup>3</sup> = 1 000 000 sm<sup>3</sup>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__math">5 m² = 5 × 10 000 = 50 000 sm²</p>
  <p class="pe-ex__uz">Besh kvadrat metr — ellik ming kvadrat
  santimetr.</p>
</div>

<h3>3. Ortiqcha maʼlumot</h3>

<p>Masalada berilgan har bir son kerak boʻlishi shart emas. Baʼzan
ortiqcha son ataylab qoʻyiladi — u sizni oʻqiganingizni
tekshiradi.</p>

<div class="pe-ex">
  <p class="pe-ex__uz"><b>Masala.</b> Afsona 5 ta daftar oldi, har biri
  3 000 soʻm. U yana 2 ta ruchka ham oldi. Doʻkongacha 15 daqiqa
  yurdi. <b>Daftarlar uchun qancha toʻladi?</b></p>
  <p class="pe-ex__math">5 × 3 000 = 15 000 soʻm</p>
  <p class="pe-ex__why">«2 ta ruchka» va «15 daqiqa» — ortiqcha.
  Savol faqat daftarlar haqida.</p>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Qanday tanib olinadi</p>
  <p>PM-85 dagi birinchi qadamga qayting: <b>soʻralgan savolni</b>
  alohida yozing. Keyin har bir sonni koʻrib chiqing va soʻrang: «bu
  son shu savolga kerakmi?» Kerak boʻlmasa, ustidan chizib
  tashlang.</p>
</div>

<h3>4. Yetishmayotgan maʼlumot</h3>

<p>Teskari hol ham bor: masala yechilmaydi, chunki bir maʼlumot
berilmagan. Buni <b>aytish</b> ham toʻgʻri javob.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Yechiladi</p>
    <p>3 kg olma (kilosi 12 000) va 2 kg nok (kilosi 15 000).
    <br>Jami: 36 000 + 30 000 = 66 000 soʻm.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Yechilmaydi</p>
    <p>3 kg olma (kilosi 12 000) va 2 kg nok.
    <br>Nokning narxi berilmagan — jami summani topib boʻlmaydi.</p>
  </div>
</div>

<div class="pe-call pe-warn">
  <p class="pe-call__t">Yetishmagan sonni oʻzingiz oʻylab topmang</p>
  <p>«Nok ham 12 000 boʻlsa kerak» degan taxmin bilan yechilgan masala
  — xato javob. Agar maʼlumot yetmasa, javob shunday boʻladi:
  <b>«Nokning narxi berilmagani uchun masalani yechib
  boʻlmaydi»</b>.</p>
</div>

<h3>Matnli masala</h3>

<p>Sinf xonasining uzunligi 8 m, eni 6 m. Polga kvadrat shaklidagi
plitka yotqizilmoqchi; plitkaning tomoni 40 sm. Xonaning balandligi
3 m.</p>

<p><b>Nechta plitka kerak boʻladi?</b></p>

<p><b>1-filtr — birliklar.</b> Xona metrda, plitka santimetrda
berilgan. Bittasiga keltiramiz.</p>

<p><b>2-filtr — maʼlumot.</b> Balandlik 3 m — <b>ortiqcha</b>. Pol
yuzasi balandlikka bogʻliq emas.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Pol yuzasi: 8 × 6 = 48 m²</span>
    <span class="pm-solve__why">Toʻgʻri toʻrtburchak yuzasi (PM-68)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">40 sm = 0,4 m</span>
    <span class="pm-solve__why">Plitkani ham metrga oʻgirdik</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Plitka yuzasi: 0,4 × 0,4 = 0,16 m²</span>
    <span class="pm-solve__why">Kvadrat yuzasi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">48 ÷ 0,16 = 300 ta</span>
    <span class="pm-solve__why">Pol yuzasi ÷ bitta plitka yuzasi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz — santimetrda</p>
  <p>Xona: 800 sm × 600 sm = 480 000 sm². Plitka: 40 × 40 = 1600 sm².
  <br>480 000 ÷ 1600 = 300 ✓ — ikkala yoʻl bir xil javob berdi.
  <br><b>Javob:</b> 300 ta plitka kerak.</p>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>Bir metrga 2,5 ta plitka sigʻadi (100 ÷ 40), demak bir
  kvadrat metrga 2,5 × 2,5 ≈ 6 ta. 48 m² uchun taxminan
  48 × 6 = 288 ta. Aniq javob 300 — yaqin ✓</span>
</div>

<div class="pe-call pe-tip">
  <p class="pe-call__t">Nega ikki yoʻl bilan yechdik</p>
  <p>Birlik xatosi shunchalik koʻp uchraydiki, uni ushlashning eng
  ishonchli yoʻli — masalani <b>boshqa birlikda</b> qayta yechish.
  Ikkala javob bir xil chiqsa, birlik xatosi yoʻq.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">1 m² = 100 sm²</p>
  <p class="pe-fix__good">1 m² = 10 000 sm²</p>
  <p class="pe-fix__why">Yuza ikkita uzunlikning koʻpaytmasi, shuning
  uchun koeffitsiyent kvadratga koʻtariladi: 100 × 100.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">1 km 500 m = 1500 km</p>
  <p class="pe-fix__good">1500 m yoki 1,5 km</p>
  <p class="pe-fix__why">Son toʻgʻri hisoblangan, lekin birlik notoʻgʻri
  yozilgan. Javobning yonidagi birlik ham javobning bir qismi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">2,5 kg = 250 g</p>
  <p class="pe-fix__good">2500 g</p>
  <p class="pe-fix__why">Kichik birlikka oʻtilyapti — son
  <b>kattalashishi</b> kerak. 1 kg = 1000 g, demak 2,5 × 1000.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">«Nok narxi berilmagan, lekin olmaday boʻlsa
  kerak»</p>
  <p class="pe-fix__good">«Maʼlumot yetarli emas, masala
  yechilmaydi»</p>
  <p class="pe-fix__why">Oʻylab topilgan son bilan chiqarilgan javob —
  xato javob. Yetishmayotgan maʼlumotni aytish esa toʻgʻri
  javobdir.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. 4 m 25 sm necha santimetr?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>425 sm.</b> 4 × 100 + 25 = 425.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. 3,5 kg necha gramm?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>3500 g.</b> 3,5 × 1000. Kichik birlik — son kattalashdi ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. 7 m² necha kvadrat santimetr?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>70 000 sm².</b> 7 × 10 000. Yuzada koeffitsiyent kvadratga
    koʻtariladi, shuning uchun 100 emas, 10 000 ga koʻpaytiriladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 2500 ml necha litr?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>2,5 l.</b> 2500 ÷ 1000. Katta birlikka oʻtilyapti — son
    kichraydi ✓</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Sherbek 20 daqiqada 6 ta masala yechdi. Uning
  sinfida 28 oʻquvchi bor. Bitta masalaga oʻrtacha necha daqiqa
  ketgan?» — masalada ortiqcha son bormi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Ha — «28 oʻquvchi» ortiqcha.</b> Javob:
    20 ÷ 6 ≈ 3,3 daqiqa. Sinfdagi oʻquvchilar soni Sherbekning
    tezligiga hech qanday aloqasi yoʻq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. «Bogʻning uzunligi 30 m. Uning yuzasi
  qancha?» — bu masala yechiladimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>Yoʻq — eni berilmagan.</b> Yuza uchun ikkita oʻlcham kerak.
    Faqat uzunlik bilan yuzani topib boʻlmaydi. Toʻgʻri javob —
    maʼlumot yetishmasligini aytish.</p>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">7. Xonaning poli 5 m × 4 m. Unga tomoni 50 sm
  boʻlgan kvadrat plitka yotqiziladi. Nechta plitka kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <p><b>80 ta.</b> Pol yuzasi 5 × 4 = 20 m². Plitka 50 sm = 0,5 m,
    yuzasi 0,5 × 0,5 = 0,25 m². 20 ÷ 0,25 = 80. Tekshirish
    santimetrda: 500 × 400 = 200 000 sm²; 50 × 50 = 2500 sm²;
    200 000 ÷ 2500 = 80 ✓</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Oʻlchov birligi</b><span>miqdorni oʻlchash uchun qabul
    qilingan meʼyor; ingl. unit of measurement</span></li>
  <li><b>Uzunlik</b><span>mm, sm, m, km bilan oʻlchanadigan kattalik;
    ingl. length</span></li>
  <li><b>Massa</b><span>g, kg, tonna bilan oʻlchanadigan kattalik; ingl.
    mass</span></li>
  <li><b>Sigʻim</b><span>ml va litr bilan oʻlchanadigan hajm; ingl.
    capacity</span></li>
  <li><b>Yuza</b><span>sm², m² bilan oʻlchanadigan kattalik; ingl.
    area</span></li>
  <li><b>Kvadrat metr</b><span>tomoni 1 m boʻlgan kvadratning yuzasi;
    ingl. square metre</span></li>
  <li><b>Koeffitsiyent</b><span>almashtirishda koʻpaytiriladigan son;
    ingl. conversion factor</span></li>
  <li><b>Ortiqcha maʼlumot</b><span>savolga kerak boʻlmagan berilgan
    son; ingl. redundant information</span></li>
  <li><b>Yetishmayotgan maʼlumot</b><span>yechish uchun zarur, lekin
    berilmagan son; ingl. missing information</span></li>
  <li><b>Yechilmaydigan masala</b><span>maʼlumoti yetarli boʻlmagan
    masala; ingl. unsolvable problem</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Qisqacha</p>
  <ul>
    <li>Hisoblashdan oldin hamma sonni bitta birlikka keltiring.</li>
    <li>Kichik birlikka — koʻpaytiring, katta birlikka —
      boʻling.</li>
    <li>Yuzada koeffitsiyent kvadratga koʻtariladi:
      1 m² = 10 000 sm².</li>
    <li>Javobning yonidagi birlik ham javobning bir qismi.</li>
    <li>Har bir berilgan sonni tekshiring: u shu savolga kerakmi?</li>
    <li>Maʼlumot yetmasa, buni aytish — toʻgʻri javob. Son oʻylab
      topilmaydi.</li>
    <li>Birlik xatosini ushlashning eng ishonchli yoʻli — masalani
      boshqa birlikda qayta yechish.</li>
  </ul>
</div>
""",
    },
]
