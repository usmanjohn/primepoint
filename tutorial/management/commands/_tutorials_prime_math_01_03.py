# -*- coding: utf-8 -*-
"""Prime Math — Block A, darslar 1–3 (sonlar va amallar).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md
Lesson list: tutorial/management/commands/toc_prime_math.txt

Uchta oyoq birga yoziladi:
  mashqlar — practice/management/commands/_practice_pm_01_03.py (20 savoldan)
  matnlar  — corner/management/commands/_stories_prime_math_01_03.py
Matnlar import qilinganidan keyin bu faylni --republish bilan qayta yuklang,
shunda "stories" havolalari bogʻlanadi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_math_01_03.py --author=prime
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
    # PM-1 — razryadlar
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-1: Sonlar qayerdan boshlanadi — razryadlar va raqamning oʻrni",
        "category": "math",
        "order": 1,
        "summary": (
            "Bir xil raqamlardan tuzilgan ikki son nega turlicha qiymatga ega? Razryadlar, "
            "yoyilma yozuv, nolning vazifasi va katta sonlarni xatosiz oʻqish."
        ),
        "stories": ["Narxdagi nollar"],
        "content": """
<h2>PM-1: Sonlar qayerdan boshlanadi — razryadlar va raqamning oʻrni</h2>

<p>Sherbek doʻkonda ikkita telefonga qaradi. Birinchisining narxi <b>2 350 000</b> soʻm,
ikkinchisiniki <b>235 000</b> soʻm. Ikkalasida ham bir xil raqamlar turibdi: 2, 3, 5.
Lekin birinchi telefon oʻn barobar qimmat. Nega? Chunki sonda raqamning oʻzi emas,
<em>uning turgan joyi</em> gapiradi. Shu bitta gʻoya butun matematikaning poydevori —
va bu darsda uni oxirigacha ochamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>raqam bilan sonning farqini aniq bilib olasiz;</li>
    <li>har bir raqam qaysi razryadda turganini va qanday "vazn"ga ega ekanini topasiz;</li>
    <li>katta sonlarni sinflarga ajratib, xatosiz oʻqiysiz;</li>
    <li>ikkita sonni bir qarashda taqqoslay olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Razryadlar oʻngdan chapga</span>
  <span class="pe-chip pe-chip--o">yuz minglik</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">oʻn minglik</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">minglik</span>
  <span class="pe-op">|</span>
  <span class="pe-chip pe-chip--s">yuzlik</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">oʻnlik</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">birlik</span>
</div>

<h3>Raqam va son — bir xil narsa emas</h3>

<p>Raqam bor-yoʻgʻi <b>oʻnta</b>: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Ular alifbodagi harflarga
oʻxshaydi. Son esa shu raqamlardan yozilgan "soʻz". <b>7</b> — ham raqam, ham son.
<b>2 350 000</b> esa yettita raqamdan tuzilgan bitta son.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Kundalik nutqda ikkalasini ham "raqam" deb ataymiz: "telefon raqami", "raqamlarni yoz".
Matematikada esa farq bor va u muhim: <b>raqam</b> — belgi, <b>son</b> — miqdor.
Shuning uchun "4 725 — toʻrt xonali son" deymiz, "toʻrt raqamli son" emas.</div>

<h3>Har bir razryadning oʻz vazni bor</h3>

<p>Sonni oʻngdan chapga qarab oʻqing. Eng oʻngdagi raqam — birliklar razryadida, undan
chapdagisi — oʻnliklar razryadida, keyingisi — yuzliklar razryadida va hokazo. Har bir
qadamda vazn <b>10 marta</b> oshadi.</p>

<div class="pe-table-wrap"><table>
  <tr><th>Razryad</th><th>Vazni</th><th>4 725 sonida</th><th>Nimani bildiradi</th></tr>
  <tr><td>minglik</td><td>1 000</td><td>4</td><td>4 × 1 000 = 4 000</td></tr>
  <tr><td>yuzlik</td><td>100</td><td>7</td><td>7 × 100 = 700</td></tr>
  <tr><td>oʻnlik</td><td>10</td><td>2</td><td>2 × 10 = 20</td></tr>
  <tr><td>birlik</td><td>1</td><td>5</td><td>5 × 1 = 5</td></tr>
</table></div>

<p>Sonni shu boʻlaklarga ajratib yozish <b>yoyilma yozuv</b> deyiladi. U sonning ichini
ochib koʻrsatadi:</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 725</span>
    <span class="pm-solve__why">Berilgan son</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 725 = 4 000 + 700 + 20 + 5</span>
    <span class="pm-solve__why">Har bir raqamni oʻz razryadining vazniga koʻpaytirdik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">4 × 1 000 + 7 × 100 + 2 × 10 + 5 × 1</span>
    <span class="pm-solve__why">Xuddi shu narsa, koʻpaytirish orqali yozilgani</span>
  </div>
</div>

<h3>Nol — boʻshlikning belgisi</h3>

<p>Nolni "hech narsa" deb tushunish yarim haqiqat. Sonda nol <em>hech narsa</em> emas,
u — <b>"bu razryad boʻsh"</b> degan xabar. Uni tashlab yuborib boʻlmaydi, chunki qolgan
raqamlar joyidan siljib ketadi.</p>

<div class="pe-ex">
  <p class="pe-ex__math">305 = 3 × 100 + 0 × 10 + 5 × 1</p>
  <p class="pe-ex__uz">Uch yuz besh: yuzliklarda 3, oʻnliklarda hech nima, birliklarda 5.</p>
  <p class="pe-ex__why">Nolni tashlasak, 35 qoladi — bu butunlay boshqa son.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Sonning <b>oxiridagi</b> nol ham bekorga turmaydi: 36 va 360 orasida oʻn marta farq bor.
Lekin sonning <b>boshidagi</b> nol hech narsa qoʻshmaydi: 0036 — bu shunchaki 36.</div>

<h3>Katta sonlarni sinflarga ajratib oʻqiymiz</h3>

<p>Uzun sonni oʻqish uchun uni <b>oʻngdan boshlab uchtalikka</b> ajrating. Har uchtalik —
bitta <b>sinf</b>: birliklar sinfi, minglar sinfi, millionlar sinfi. Yozganda sinflar
orasiga kichik boʻshliq qoʻyiladi: <b>2 350 000</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__math">2 | 350 | 000</p>
  <p class="pe-ex__uz">Ikki million uch yuz ellik ming — oxirgi sinf boʻsh, shuning uchun
     birliklar aytilmaydi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Sonni <b>chapdan</b> boshlab oʻqiymiz, lekin sinflarga <b>oʻngdan</b> boshlab ajratamiz.
Shuning uchun avval qalam bilan boʻshliqlarni qoʻying, keyin oʻqing — shunda
"ikki million uch yuz ellik ming" oʻrniga "ikki yuz ellik ming" deb yuborilmaydi.</div>

<h3>Sonni son oʻqida koʻrish</h3>

<p>Razryad faqat yozuvda emas, <em>kattalikda</em> ham sezilib turadi. 720 sonini 0 bilan
1 000 orasiga qoʻysak, u yarmidan oʻngda turadi — chunki yuzliklar razryadida 7 bor.</p>

<div class="pm-num">
  <div class="pm-num__track">
    <span class="pm-num__tick" style="left:0%"><i>0</i></span>
    <span class="pm-num__tick" style="left:50%"><i>500</i></span>
    <span class="pm-num__tick" style="left:100%"><i>1 000</i></span>
    <span class="pm-num__dot" style="left:72%"><i>720</i></span>
  </div>
</div>

<h3>Ikki sonni taqqoslash — ikki qadam</h3>

<ol class="pe-steps">
  <li><b>Xonalar sonini sanang.</b> Koʻproq xonali son kattaroq: 1 000 &gt; 999.</li>
  <li><b>Xonalari teng boʻlsa</b>, chapdan boshlab raqamlarni juftlab solishtiring va
      birinchi farq qilgan razryadda toʻxtang.</li>
</ol>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 940 ? 8 917</span>
    <span class="pm-solve__why">Ikkalasi ham toʻrt xonali — birinchi qadam yordam bermadi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">8 = 8, 9 = 9</span>
    <span class="pm-solve__why">Mingliklar va yuzliklar teng, oldinga yuramiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">4 &gt; 1, demak 8 940 &gt; 8 917</span>
    <span class="pm-solve__why">Oʻnliklar razryadida farq chiqdi — qolganiga qarash shart emas</span>
  </div>
</div>

<h3>Matnli masala</h3>

<p><b>Afsona</b> chekka <b>1 250 000</b> soʻm deb yozishi kerak edi. Shoshib, bitta nolni
tushirib qoldirdi va chekda <b>125 000</b> soʻm boʻlib qoldi.
<b>Yozilgan summa kerakligidan necha marta kam?</b></p>

<p><em>Nima soʻralyapti?</em> Ikki son orasidagi farq emas, <b>necha marta</b> kamligi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1 250 000 → 125 000</span>
    <span class="pm-solve__why">Bitta nol tushdi, har bir raqam bitta razryad oʻngga surildi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">har bir razryad 10 marta yengil</span>
    <span class="pm-solve__why">Oʻngga bir qadam = vazn 10 marta kichrayadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">10 marta kam</span>
    <span class="pm-solve__why">Butun son ham 10 marta kichrayadi</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>125 000 × 10 = 1 250 000 ✓ — javob toʻgʻri.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">4 725 = <s>4 + 7 + 2 + 5 = 18</s></p>
  <p class="pe-good">4 725 = <b>4 000 + 700 + 20 + 5</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Yigirma ming = <s>200 00</s></p>
  <p class="pe-good">Yigirma ming = <b>20 000</b> — yaʼni 20 × 1 000</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">2 350 000 — <s>"ikki yuz ellik ming"</s></p>
  <p class="pe-good">2 350 000 — <b>"ikki million uch yuz ellik ming"</b></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     6 083 sonida <b>8</b> raqami qaysi razryadda turibdi va uning qiymati qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Oʻnliklar razryadida, qiymati 80.</strong>
    Oʻngdan sanaymiz: 3 — birlik, 8 — oʻnlik, 0 — yuzlik, 6 — minglik.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Yoyilmasi 5 000 + 40 + 2 boʻlgan sonni yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>5 042.</strong> Yuzliklar razryadi boʻsh, shuning
    uchun uning oʻrniga <b>0</b> yoziladi. 542 ham, 5 42 ham notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Qaysi son katta: 7 099 yoki 7 100?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>7 100 katta.</strong> Xonalari teng, mingliklar
    teng (7 = 7), yuzliklarda esa 1 &gt; 0. Oxiridagi 99 chiroyli koʻrinsa ham, u faqat
    oʻnlik va birlik razryadlarida turibdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     40 500 soni qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Qirq ming besh yuz.</strong> Uchtalikka ajratamiz:
    40 | 500. Minglar sinfida 40, birliklar sinfida 500.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bir qutida 100 ta qalam, bir yashikda 10 ta quti bor. Omborda 4 yashik, 3 quti va
     yana 7 ta yakka qalam bor. Omborda jami nechta qalam?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>4 307 ta.</strong> Bir yashik = 10 × 100 = 1 000
    qalam, demak 4 yashik — 4 000 ta. 3 quti — 300 ta. Yakka qalamlar — 7 ta.
    4 000 + 300 + 7 = <b>4 307</b>. Eʼtibor bering: bu sonning yoyilma yozuvi aynan
    masalaning oʻzi — oʻnliklar razryadi boʻsh, shuning uchun u yerda 0 turibdi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Raqam</b><span>0–9 orasidagi belgi; ingl. digit</span></li>
  <li><b>Son</b><span>raqamlardan yozilgan miqdor; ingl. number</span></li>
  <li><b>Razryad</b><span>raqamning sondagi oʻrni va vazni; ingl. place value</span></li>
  <li><b>Birlik</b><span>eng oʻngdagi razryad; ingl. ones</span></li>
  <li><b>Oʻnlik</b><span>ingl. tens</span></li>
  <li><b>Yuzlik</b><span>ingl. hundreds</span></li>
  <li><b>Minglik</b><span>ingl. thousands</span></li>
  <li><b>Yoyilma yozuv</b><span>sonni razryadlarga ajratib yozish; ingl. expanded form</span></li>
  <li><b>Sinf</b><span>uchtalik guruh (minglar, millionlar); ingl. period</span></li>
  <li><b>Xona</b><span>sondagi raqam oʻrni soni: 4 725 — toʻrt xonali; ingl. digit place</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda tuting</p>
  <ul>
    <li>Sonda raqamning <b>oʻrni</b> uning qiymatini belgilaydi: oʻngdan chapga har qadamda vazn 10 marta oshadi.</li>
    <li><b>Nol</b> — "bu razryad boʻsh" degan belgi. Uni tashlab boʻlmaydi.</li>
    <li>Katta sonni <b>oʻngdan uchtalik</b> sinflarga ajratib oʻqing.</li>
    <li>Taqqoslashda avval <b>xonalar soni</b>, keyin chapdan birinchi farq qilgan razryad.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-2 — qoʻshish va ayirish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-2: Qoʻshish va ayirish: ustunda va ogʻzaki",
        "category": "math",
        "order": 2,
        "summary": (
            "Ustunda qoʻshish va ayirishning ichki mantigʻi, ogʻzaki hisobning uchta tez "
            "usuli, javobni tekshirish odati va bozor-kassa masalalari."
        ),
        "stories": ["Sinf kassasi"],
        "content": """
<h2>PM-2: Qoʻshish va ayirish: ustunda va ogʻzaki</h2>

<p>Sinf kassasida <b>85 000</b> soʻm bor edi. Bayramga <b>47 500</b> soʻmlik shar va
shirinlik olindi. Sardor kalkulyator qidirib telefonini titkilaguncha, Dilnoza qogʻozga
qaramay javobni aytdi. Sehr emas — u shunchaki sonlarni razryadlarga ajratib oʻylashni
biladi. Bu darsda ikkala usulni ham oʻrganamiz: qogʻozdagi ishonchli <b>ustun</b> usulini
va tezkor <b>ogʻzaki</b> usullarni.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ustunda qoʻshish va ayirishni xatosiz bajarasiz — va nega shunday ishlashini bilasiz;</li>
    <li>ogʻzaki hisobning uchta usulini oʻrganasiz;</li>
    <li>javobni ikki soniyada tekshirishni odat qilasiz;</li>
    <li>kassa-hisob masalalarini bosqichma-bosqich yechasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Nomlar</span>
  <span class="pe-chip pe-chip--o">qoʻshiluvchi</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">qoʻshiluvchi</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">yigʻindi</span>
  <span class="pe-chip pe-chip--opt">kamayuvchi − ayiriluvchi = ayirma</span>
</div>

<h3>Ustunda qoʻshish: razryad razryad bilan</h3>

<p>Ustun usulining butun sirri bitta jumlada: <b>birliklar birliklar bilan, oʻnliklar
oʻnliklar bilan qoʻshiladi.</b> Shuning uchun sonlarni oʻng chekkasidan tekislab yozamiz.
Agar bir razryadda 10 dan katta son chiqsa, oʻnligini keyingi razryadga "koʻtaramiz".</p>

<table class="pm-col">
  <tr class="pm-col__carry"><td></td><td>1</td><td></td></tr>
  <tr><td></td><td>4</td><td>7</td></tr>
  <tr class="pm-col__op"><td>+</td><td>2</td><td>8</td></tr>
  <tr class="pm-col__res"><td></td><td>7</td><td>5</td></tr>
</table>

<p>Birliklar: 7 + 8 = 15. Bu 1 oʻnlik va 5 birlik. Shuning uchun 5 ni yozamiz, 1 ni
oʻnliklar ustiga koʻtaramiz. Oʻnliklar: 4 + 2 + 1 = 7. Javob: <b>75</b>.</p>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Koʻtarilgan birlik — bu "yashirin" son emas. U 10 ta birlik <b>bitta oʻnlikka</b>
almashtirilgani, xolos. Bozorda 10 ta ming soʻmlikni bitta oʻn ming soʻmlikka almashtirgan
kabi: pul miqdori oʻzgarmadi, koʻrinishi oʻzgardi.</div>

<h3>Ustunda ayirish: qarz olish</h3>

<p>Ayirishda teskarisi boʻladi. Yuqoridagi raqam yetmasa, chapdagi razryaddan bitta
"qarz" olamiz va u 10 ta birlikka aylanadi.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">500 − 236</span>
    <span class="pm-solve__why">Birliklarda 0 dan 6 ni ayirib boʻlmaydi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">500 = 4 yuzlik + 9 oʻnlik + 10 birlik</span>
    <span class="pm-solve__why">Yuzlikdan qarz oldik, u oʻnliklarga, undan birliklarga oʻtdi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">10 − 6 = 4 · 9 − 3 = 6 · 4 − 2 = 2</span>
    <span class="pm-solve__why">Endi har bir razryadda ayirish bemalol bajariladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">500 − 236 = 264</span>
    <span class="pm-solve__why">Javob</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>264 + 236 = 500 ✓ — ayirishni doim qoʻshish bilan tekshiring, bu ikki soniya vaqt oladi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Eng koʻp uchraydigan xato — "kichikdan kattani ayirib boʻlmaydi" deb, oʻrniga <em>kattadan
kichigini</em> ayirib qoʻyish: 0 − 6 oʻrniga 6 − 0. Bunda javob 264 emas, 336 chiqadi va
bu xato butun ishni buzadi. Qarz olishni oʻtkazib yubormang.</div>

<h3>Ogʻzaki hisobning uchta usuli</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Yaxlitlab, keyin tuzatish</p>
    <p>198 + 47 → 200 + 47 = 247 → 247 − 2 = <b>245</b></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Razryadlarga ajratish</p>
    <p>362 + 185 → (300 + 100) + (60 + 80) + (2 + 5) = 400 + 140 + 7 = <b>547</b></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Ayirishni "sanab yetish"ga aylantirish</p>
    <p>63 − 29 → 29 dan 63 gacha: 29 + 1 = 30, 30 + 33 = 63, demak <b>34</b></p>
  </div>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>385 + 214 ≈ 400 + 200 = 600. Demak javob 600 atrofida boʻlishi kerak — aniq
  hisob 599 ni beradi. Agar 5 999 yoki 59 chiqsa, xato razryadda.</span>
</div>

<h3>Matnli masala</h3>

<p>Sinf kassasida <b>85 000</b> soʻm bor edi. Bayram uchun <b>47 500</b> soʻmga shar va
shirinlik olindi. Ertasi kuni ota-onalar yana <b>30 000</b> soʻm qoʻshdi.
<b>Kassada qancha pul qoldi?</b></p>

<p><em>Nima soʻralyapti?</em> Oxirgi qoldiq. Demak ikkita amal kerak, va ular
<b>hodisalar tartibida</b> bajariladi: avval sarf, keyin qoʻshimcha.</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">85 000 − 47 500 = 37 500</span>
    <span class="pm-solve__why">Xaridan keyin qolgan pul</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">37 500 + 30 000 = 67 500</span>
    <span class="pm-solve__why">Ota-onalar qoʻshgandan keyingi qoldiq</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>67 500 + 47 500 = 115 000 va 85 000 + 30 000 = 115 000 ✓ — kirim va chiqim mos keldi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">47 + 28 = <s>65</s> — 7 + 8 = 15 dagi oʻnlik koʻtarilmagan</p>
  <p class="pe-good">47 + 28 = <b>75</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad">500 − 236 = <s>336</s> — har bir ustunda kattadan kichigi ayirilgan</p>
  <p class="pe-good">500 − 236 = <b>264</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad">245 + 30 = <s>545</s> — 30 yuzliklar ustiga tekislab yozilgan</p>
  <p class="pe-good">245 + 30 = <b>275</b> — sonlar doim <b>oʻng chekkasidan</b> tekislanadi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     236 + 98 = ?  (ogʻzaki hisoblang)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>334.</strong> 98 ni 100 deb yaxlitlaymiz:
    236 + 100 = 336. Ortiqcha qoʻshilgan 2 ni qaytarib olamiz: 336 − 2 = <b>334</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     704 − 268 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>436.</strong> Birliklarda 4 dan 8 ni ayirib
    boʻlmaydi, oʻnliklar esa boʻsh — shuning uchun qarz yuzlikdan olinadi:
    704 = 6 yuzlik + 9 oʻnlik + 14 birlik. 14 − 8 = 6, 9 − 6 = 3, 6 − 2 = 4.
    Tekshiruv: 436 + 268 = 704 ✓</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     199 + 199 ni eng tez qanday hisoblash mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>398.</strong> 200 + 200 = 400, keyin ortiqcha
    qoʻshilgan 1 + 1 = 2 ni ayiramiz: 400 − 2 = <b>398</b>. Ustunda yozish ham toʻgʻri,
    lekin uch barobar koʻp vaqt oladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Ayirma 341 ga, ayiriluvchi 159 ga teng. Kamayuvchi qancha?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>500.</strong> Kamayuvchi = ayirma + ayiriluvchi =
    341 + 159 = <b>500</b>. Bu aynan tekshirish qoidasining oʻzi, teskari tomondan
    ishlatilgani.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Jasur kun davomida 12 400 qadam, Dilnoza 9 850 qadam yurdi. Jasur nechta koʻp yurgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>2 550 qadam.</strong> "Nechta koʻp" — ayirish:
    12 400 − 9 850 = <b>2 550</b>. Tekshiruv: 9 850 + 2 550 = 12 400 ✓. Eʼtibor bering,
    savol "necha marta koʻp" boʻlganida bu boshqa amal boʻlardi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Qoʻshiluvchi</b><span>qoʻshilayotgan sonlar; ingl. addend</span></li>
  <li><b>Yigʻindi</b><span>qoʻshish natijasi; ingl. sum</span></li>
  <li><b>Kamayuvchi</b><span>ayirishda birinchi son; ingl. minuend</span></li>
  <li><b>Ayiriluvchi</b><span>ayirilayotgan son; ingl. subtrahend</span></li>
  <li><b>Ayirma</b><span>ayirish natijasi; ingl. difference</span></li>
  <li><b>Ustun usuli</b><span>razryadlarni tekislab yozib hisoblash; ingl. column method</span></li>
  <li><b>Koʻtarish</b><span>10 ta birlikni keyingi razryadga oʻtkazish; ingl. carrying</span></li>
  <li><b>Qarz olish</b><span>chapdagi razryaddan bitta birlik olish; ingl. borrowing</span></li>
  <li><b>Yaxlitlash</b><span>yaqin doʻng songa keltirish; ingl. rounding</span></li>
  <li><b>Taxminiy hisob</b><span>javobning kattaligini oldindan chamalash; ingl. estimation</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda tuting</p>
  <ul>
    <li>Ustunda sonlar <b>oʻng chekkasidan</b> tekislanadi — razryad razryad bilan ishlaydi.</li>
    <li>Koʻtarish va qarz olish — 10 ta birlikni bitta katta birlikka almashtirish, xolos.</li>
    <li>Ayirishni doim <b>qoʻshish bilan tekshiring</b>: ayirma + ayiriluvchi = kamayuvchi.</li>
    <li>Hisoblashdan oldin <b>taxmin qiling</b> — bu razryad xatosini darrov ushlaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-3 — koʻpaytirish
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PM-3: Koʻpaytirish — qoʻshishning qisqa yoʻli va jadval mantigʻi",
        "category": "math",
        "order": 3,
        "summary": (
            "Koʻpaytirish nima ekanini chizma bilan koʻrsatamiz, jadvalni yodlash oʻrniga "
            "uning mantigʻini oʻrganamiz, ustunda koʻpaytiramiz va matnli masala yechamiz."
        ),
        "stories": ["Bir qutida nechta?"],
        "content": """
<h2>PM-3: Koʻpaytirish — qoʻshishning qisqa yoʻli va jadval mantigʻi</h2>

<p>Omborda oltita yashik turibdi, har birida yigirma toʻrttadan choynak. Bekzod ularni
sanay boshladi: 24 + 24 + 24… Uchinchi yashikda adashib ketdi va yana boshidan sanadi.
Koʻpaytirish aynan shu muammoni hal qilish uchun oʻylab topilgan: <b>bir xil sonni
koʻp marta qoʻshishning qisqa yoʻli</b>. Bu darsda uni chizmada koʻramiz, jadvalning
ichki mantigʻini ochamiz va ustunda ishlashni oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>koʻpaytirishni qoʻshish orqali tushuntira olasiz;</li>
    <li>jadvalni yodlash oʻrniga uning qoidalaridan foydalanasiz;</li>
    <li>ustunda ikki va uch xonali sonni koʻpaytirasiz;</li>
    <li>koʻpaytirish kerak boʻlgan matnli masalani tanib olasiz.</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Nomlar</span>
  <span class="pe-chip pe-chip--o">koʻpaytuvchi</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--o">koʻpaytuvchi</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">koʻpaytma</span>
  <span class="pe-chip pe-chip--opt">4 × 6 = 6 + 6 + 6 + 6</span>
</div>

<h3>Koʻpaytirish — bu toʻrtburchak</h3>

<p>Koʻpaytmani rasm sifatida koʻrish eng foydali odat. 4 qator, har qatorda 6 ta katak —
jami nechta katak bor?</p>

<figure class="pm-fig">
  <svg viewBox="0 0 320 200" role="img" aria-label="Toʻrt qator, olti ustundan iborat katakli toʻrtburchak">
    <rect class="pm-fill" x="60" y="20" width="216" height="144"/>
    <line class="pm-ln" x1="60" y1="20" x2="276" y2="20"/>
    <line class="pm-ln" x1="60" y1="56" x2="276" y2="56"/>
    <line class="pm-ln" x1="60" y1="92" x2="276" y2="92"/>
    <line class="pm-ln" x1="60" y1="128" x2="276" y2="128"/>
    <line class="pm-ln" x1="60" y1="164" x2="276" y2="164"/>
    <line class="pm-ln" x1="60" y1="20" x2="60" y2="164"/>
    <line class="pm-ln" x1="96" y1="20" x2="96" y2="164"/>
    <line class="pm-ln" x1="132" y1="20" x2="132" y2="164"/>
    <line class="pm-ln" x1="168" y1="20" x2="168" y2="164"/>
    <line class="pm-ln" x1="204" y1="20" x2="204" y2="164"/>
    <line class="pm-ln" x1="240" y1="20" x2="240" y2="164"/>
    <line class="pm-ln" x1="276" y1="20" x2="276" y2="164"/>
    <text class="pm-lbl" x="30" y="97" text-anchor="middle">4 qator</text>
    <text class="pm-lbl" x="168" y="188" text-anchor="middle">6 ustun</text>
    <text class="pm-lbl pm-lbl--hl" x="168" y="12" text-anchor="middle">4 × 6 = 24</text>
  </svg>
  <figcaption>Koʻpaytma — toʻrtburchakdagi kataklar soni.</figcaption>
</figure>

<p>Rasmga qarab ikkita muhim narsani darrov koʻrish mumkin. Birinchisi: qatorlab sanasak
6 + 6 + 6 + 6, ustunlab sanasak 4 + 4 + 4 + 4 + 4 + 4 — natija bir xil. Demak
<b>4 × 6 = 6 × 4</b>. Ikkinchisi: koʻpaytirish jadvalining yarmini yodlash yetarli.</p>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Koʻpaytirish jadvalida 100 ta katak bor, lekin oʻrin almashtirish qoidasi tufayli
yodlanadigan yangi natijalar 55 tadan oshmaydi. 0, 1, 10 ustunlarini va 5 ga
koʻpaytirishni ham chiqarib tashlasangiz, "qiyin" katak juda kam qoladi.</div>

<h3>Jadvalning ichidagi qoidalar</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>0 va 1</p>
    <p>Har qanday son × 0 = 0 (nol marta olingan). Har qanday son × 1 — oʻzi.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>10, 100 ga koʻpaytirish</p>
    <p>36 × 10 = 360, 36 × 100 = 3 600. Raqamlar razryad boʻyicha chapga suriladi.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>9 ga koʻpaytirish</p>
    <p>9 × 7 = 63. Natijaning raqamlari yigʻindisi doim 9 ga teng: 6 + 3 = 9.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Boʻlaklab koʻpaytirish</p>
    <p>7 × 12 = 7 × 10 + 7 × 2 = 70 + 14 = 84. Qiyin koʻpaytmani ikkita osoniga boʻling.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
"36 ni 10 ga koʻpaytirsang, oxiriga nol qoʻshasan" — bu qoida ishlaydi, lekin sababini
bilish muhimroq: har bir raqam bitta razryad chapga suriladi, birliklar razryadi esa boʻsh
qoladi va u yerga 0 yoziladi (PM-1 ni eslang). Kasrlarga oʻtganda "nol qoʻshish" qoidasi
ishdan chiqadi, sabab esa ishlayveradi.</div>

<h3>Ustunda koʻpaytirish</h3>

<p>Ustunda ham xuddi qoʻshishdagi kabi razryadlar bilan ishlaymiz va koʻtarishni
unutmaymiz.</p>

<table class="pm-col">
  <tr class="pm-col__carry"><td></td><td>2</td><td></td></tr>
  <tr><td></td><td>2</td><td>4</td></tr>
  <tr class="pm-col__op"><td>×</td><td></td><td>6</td></tr>
  <tr class="pm-col__res"><td>1</td><td>4</td><td>4</td></tr>
</table>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">4 × 6 = 24</span>
    <span class="pm-solve__why">Birliklar: 4 ni yozamiz, 2 oʻnlikni koʻtaramiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2 × 6 = 12, 12 + 2 = 14</span>
    <span class="pm-solve__why">Oʻnliklar, ustiga koʻtarilgan 2 qoʻshiladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">24 × 6 = 144</span>
    <span class="pm-solve__why">Javob</span>
  </div>
</div>

<div class="pm-est">
  <span class="pm-est__t">Taxmin</span>
  <span>24 × 6 ≈ 25 × 6 = 150. Javob 150 atrofida — 144 mos keladi. Agar 84 yoki 1 440
  chiqsa, xato bor.</span>
</div>

<p>Uch xonali son bilan ham xuddi shunday: <b>213 × 4</b> → birliklar 3 × 4 = 12
(2 ni yozamiz, 1 ni koʻtaramiz), oʻnliklar 1 × 4 = 4, ustiga 1 → 5, yuzliklar
2 × 4 = 8. Natija: <b>852</b>.</p>

<h3>Matnli masala</h3>

<p>Omborda <b>6 ta</b> yashik bor, har birida <b>24 tadan</b> choynak. Yana <b>3 ta</b>
choynak yashiksiz, alohida turibdi. <b>Omborda jami nechta choynak bor?</b></p>

<p><em>Nima soʻralyapti?</em> Umumiy soni. "Har birida 24 tadan" — bu takrorlanish, demak
koʻpaytirish. Yakka choynaklar esa oxirida qoʻshiladi.</p>

<div class="pm-model">
  <div class="pm-model__row">
    <span class="pm-model__lbl">6 yashik</span>
    <span class="pm-model__bar" style="width:62%">6 × 24</span>
  </div>
  <div class="pm-model__row">
    <span class="pm-model__lbl">yakka</span>
    <span class="pm-model__bar pm-model__bar--alt" style="width:12%">3</span>
  </div>
  <p class="pm-model__tot">Jami = 6 × 24 + 3</p>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">6 × 24 = 144</span>
    <span class="pm-solve__why">Yashiklardagi choynaklar</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">144 + 3 = 147</span>
    <span class="pm-solve__why">Yakka turganlarini qoʻshdik</span>
  </div>
</div>

<div class="pm-check">
  <p class="pm-check__t">Tekshiramiz</p>
  <p>147 − 3 = 144, 144 ÷ 6 = 24 ✓ — har yashikda yana 24 tadan chiqdi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">24 × 6 = <s>124</s> — 4 × 6 = 24 dagi koʻtarilgan 2 unutilgan</p>
  <p class="pe-good">24 × 6 = <b>144</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad">7 × 12 = <s>72</s> — 7 × 10 bajarilib, 7 × 2 tashlab ketilgan</p>
  <p class="pe-good">7 × 12 = 70 + 14 = <b>84</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad">36 × 10 = <s>306</s> — nol notoʻgʻri joyga qoʻyilgan</p>
  <p class="pe-good">36 × 10 = <b>360</b></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     8 × 7 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>56.</strong> Esdan chiqsa, boʻlaklang:
    8 × 7 = 8 × 5 + 8 × 2 = 40 + 16 = <b>56</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     45 × 3 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>135.</strong> Boʻlaklab: 40 × 3 = 120,
    5 × 3 = 15, 120 + 15 = <b>135</b>. Taxmin: 45 × 3 ≈ 50 × 3 = 150 — javob shunga
    yaqin, demak razryad xatosi yoʻq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     6 × 25 ni ogʻzaki hisoblashning tez yoʻlini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>150.</strong> 25 — chorak yuz. 4 × 25 = 100,
    demak 6 × 25 = 100 + 2 × 25 = 100 + 50 = <b>150</b>. Yoki: 6 × 25 = 3 × 50 = 150.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     124 × 5 = ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>620.</strong> Ustunda: 4 × 5 = 20 (0 yozamiz,
    2 koʻtariladi), 2 × 5 = 10, +2 = 12 (2 yozamiz, 1 koʻtariladi), 1 × 5 = 5, +1 = 6.
    Tez usul: 124 × 10 = 1 240, uning yarmi = <b>620</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Sinfda 4 qator parta bor, har qatorda 7 tadan parta, har partada 2 oʻquvchi oʻtiradi.
     Sinfda nechta oʻquvchi bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>56 ta.</strong> Avval partalar: 4 × 7 = 28.
    Keyin oʻquvchilar: 28 × 2 = <b>56</b>. Ikki bosqichli masalada har bosqichning
    <em>nima</em> ekanini aytib qoʻying ("28 — bu partalar soni"), shunda oxirida nimani
    hisoblaganingizni adashtirmaysiz.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Koʻpaytuvchi</b><span>koʻpaytirilayotgan sonlar; ingl. factor</span></li>
  <li><b>Koʻpaytma</b><span>koʻpaytirish natijasi; ingl. product</span></li>
  <li><b>Oʻrin almashtirish</b><span>a × b = b × a; ingl. commutative property</span></li>
  <li><b>Boʻlaklab koʻpaytirish</b><span>7 × 12 = 7 × 10 + 7 × 2; ingl. distributive property</span></li>
  <li><b>Karrali</b><span>berilgan songa boʻlinadigan son; ingl. multiple</span></li>
  <li><b>Toʻrtburchak modeli</b><span>koʻpaytmani kataklar soni sifatida koʻrish; ingl. area model</span></li>
  <li><b>Koʻtarish</b><span>oʻnlikni keyingi razryadga oʻtkazish; ingl. carrying</span></li>
  <li><b>Ikki barobar</b><span>2 ga koʻpaytirish; ingl. double</span></li>
  <li><b>Taxminiy hisob</b><span>javobni oldindan chamalash; ingl. estimation</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda tuting</p>
  <ul>
    <li>Koʻpaytirish — bir xil sonni takror qoʻshish; uni <b>toʻrtburchak</b> sifatida tasavvur qiling.</li>
    <li><b>a × b = b × a</b> — shuning uchun jadvalning yarmi yetarli.</li>
    <li>Qiyin koʻpaytmani <b>boʻlaklang</b>: 7 × 12 = 7 × 10 + 7 × 2.</li>
    <li>Matnda "har birida … tadan" degan soʻzlar koʻpaytirishni bildiradi.</li>
  </ul>
</div>
""",
    },
]
