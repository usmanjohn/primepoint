# -*- coding: utf-8 -*-
"""Prime Russian — Block B, darslar 6–8 (birinchi gaplar).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

Har bir dars uchta boʻlakdan biri: dars + mashq + oʻqish matni.
Mashqlar:      practice/management/commands/_practice_pr_06_08.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_06_08.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_06_08.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Russian",
    "category": "russian",
    "description": (
        "Rus tili noldan ishonchli B2 gacha — 100 ta dars. Kirill alifbosi, kelishiklar, "
        "feʼl turlari, oʻzbekcha tushuntirish va oʻzingiz tekshiradigan mashqlar."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-6: Это — birinchi gapingiz. «Кто это? Что это?»",
        "category": "russian",
        "order": 6,
        "summary": (
            "Ikkita soʻz bilan toʻliq ruscha gap tuzasiz. Rus tilida hozirgi zamonda "
            "“-dir” feʼli yoʻq — xuddi oʻzbekchadagidek. Кто? va Что? savollarini "
            "ajratasiz."
        ),
        "stories": ["Кто э́то?"],
        "content": """
<h2>PR-6: Это — birinchi gapingiz. «Кто это? Что это?»</h2>

<p>Beshta dars harflar bilan oʻtdi. Bugun gapirasiz — va birinchi ruscha gapingiz
atigi <b>ikkita soʻzdan</b> iborat boʻladi. <b>Э́то дом.</b> Tamom. Bu toʻliq,
toʻgʻri, tabiiy ruscha gap. Hech qanday feʼl yoʻq, hech qanday qoʻshimcha yoʻq.
Ingliz tilini oʻrgangan odam bu yerda “<em>is</em> qani?” deb hayron boʻladi;
siz esa hayron boʻlmaysiz, chunki oʻzbek tilida ham xuddi shunday.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Это</b> bilan istalgan narsani koʻrsatib, toʻliq gap tuzasiz</li>
    <li>Nega rus tilida hozirgi zamonda “-dir” feʼli yoʻqligini tushunasiz</li>
    <li><b>Кто это?</b> va <b>Что это?</b> savollarini toʻgʻri tanlaysiz</li>
    <li>Savol berasiz va <b>Нет, это не …</b> bilan rad javobini berasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Birinchi qolip</span>
  <span class="pe-chip pe-chip--s">Э́то</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">ot</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">toʻliq gap</span>
</div>

<h3>1. Rus tilida hozirgi zamonda “boʻlmoq” feʼli yoʻq</h3>

<p>Bu birinchi darsning eng katta xabari. Rus tilida <b>быть</b> (boʻlmoq) feʼli
bor, lekin u <em>hozirgi zamonda ishlatilmaydi</em>. Uning oʻrnida hech nima
turmaydi — yoki yozuvda tire (—) turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Э́то</span>
     <span class="pe-hl pe-hl--o">дом</span>.</p>
  <p class="pe-ex__rom">[э́тъ дом]</p>
  <p class="pe-ex__uz">Bu — uy.</p>
  <p class="pe-ex__why">Ikkita soʻz, toʻliq gap. Orada hech qanday feʼl yoʻq va
     boʻlishi ham shart emas.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu siz uchun yangi emas. Oʻzbek tilida ham <em>“Bu — uy.”</em> deymiz —
“Bu uy <b>dir</b>” degan shakl kitobiy va sunʼiy eshitiladi. Rus tili ham xuddi
shunday ishlaydi. Ingliz tilini oʻrgangan oʻquvchi bu yerda “<em>is</em>” ni
qoʻshib yubormoqchi boʻladi; sizda esa bunday odat yoʻq, va bu sizning
ustunligingiz. <b>Hech qachon</b> “Это <s>есть</s> дом” demang.</div>

<h3>2. Это + istalgan narsa</h3>

<p><b>Это</b> soʻzi “bu” degani va u hamma narsaga yetadi: odamga ham, buyumga
ham, joyga ham, hayvonga ham. U oʻzgarmaydi — bitta shakl, hamma holat uchun.</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Buyum</p>
    <p>Э́то стол. — Bu stol.<br>Э́то кни́га. — Bu kitob.<br>Э́то окно́. — Bu deraza.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Odam</p>
    <p>Э́то Афсо́на. — Bu Afsona.<br>Э́то брат. — Bu aka.<br>Э́то учи́тель. — Bu oʻqituvchi.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Joy va hayvon</p>
    <p>Э́то Ташке́нт. — Bu Toshkent.<br>Э́то шко́ла. — Bu maktab.<br>Э́то кот. — Bu mushuk.</p></div>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Это</b> ni <b>этот</b> bilan chalkashtirmang. Bu darsdagi <b>это</b> — “bu
(narsa)”, u mustaqil turadi: <em>Э́то кни́га</em>. <b>Этот</b> esa otning oldida
turadi: <em>э́та кни́га</em> — “bu kitob”. Ikkinchisini PR-16 da alohida
oʻrganamiz; hozircha faqat mustaqil <b>это</b> bilan ishlaymiz.</div>

<h3>3. Кто это? va Что это? — jonli va jonsiz</h3>

<p>Rus tilida ikkita savol soʻzi bor va ular <b>jonli</b> va <b>jonsiz</b> narsani
ajratadi:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Кто э́то?</p>
    <p style="font-size:1.1rem">“Bu kim?”</p>
    <p><b>Odamlar va hayvonlar</b> haqida.</p>
    <p>— Кто э́то?<br>— Э́то Жасу́р.</p>
    <p>— Кто э́то?<br>— Э́то кот.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Что э́то?</p>
    <p style="font-size:1.1rem">“Bu nima?”</p>
    <p><b>Buyum, joy, tushuncha</b> haqida.</p>
    <p>— Что э́то?<br>— Э́то шко́ла.</p>
    <p>— Что э́то?<br>— Э́то кни́га.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Yana bir tekin sovgʻa: oʻzbek tilida ham aynan shu boʻlinish bor — <em>kim?</em>
va <em>nima?</em>. Va chegara ham bir xil joyda: mushuk haqida oʻzbekcha
“bu kim?” deb ham, “bu nima?” deb ham soʻrash mumkin, ruschada esa hayvon
<b>кто</b> tomonda turadi. Yaʼni faqat bitta detalni eslab qolish kerak:
<b>hayvon — жив, demak кто</b>.</div>

<h3>4. Savol berish — soʻz tartibi oʻzgarmaydi</h3>

<p>Rus tilida oddiy savol yasash uchun <b>hech nima qilish shart emas</b>. Soʻz
tartibi oʻsha-oʻsha qoladi; faqat ohang koʻtariladi va yozuvda savol belgisi
qoʻyiladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ru">Э́то шко́ла. → Э́то шко́ла?</p>
  <p class="pe-ex__uz">Bu maktab. → Bu maktabmi?</p>
  <p class="pe-ex__why">Yagona farq — ohang. Ruschada oʻzbekchadagi
     <b>-mi</b> yoki inglizchadagi <em>is this</em> kabi maxsus vosita yoʻq.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Ohangni toʻgʻri qoʻying, chunki u yagona belgi. Savolda ovoz <b>eng muhim
soʻzda koʻtariladi va keyin pasayadi</b>: “Э́то <b>ШКО́</b>-ла?”. Darak gapda esa
ovoz oxirigacha bir tekis pasayib boradi. Ovoz chiqarib mashq qiling —
bu bitta jumlani ikki xil aytishning eng arzon usuli.</div>

<h3>5. Да va Нет — javob berish</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">— Э́то кни́га?<br>— Да, э́то кни́га.</p>
  <p class="pe-ex__uz">— Bu kitobmi?<br>— Ha, bu kitob.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Э́то соба́ка?<br>— <span class="pe-hl pe-hl--neg">Нет</span>,
     э́то <span class="pe-hl pe-hl--neg">не</span> соба́ка. Э́то кот.</p>
  <p class="pe-ex__uz">— Bu itmi?<br>— Yoʻq, bu it emas. Bu mushuk.</p>
  <p class="pe-ex__why">Ikkita boshqa soʻzga eʼtibor bering: <b>нет</b> — bu
     “yoʻq” degan <em>javob</em>, <b>не</b> esa inkor qilinayotgan soʻzning
     <em>oldida</em> turadigan zarracha.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Не</b> har doim oʻzi inkor qilayotgan soʻzning <b>oldida</b> turadi va u bilan
birga aytiladi: <em>не соба́ка</em>, <em>не шко́ла</em>, <em>не Жасу́р</em>.
Uni gap oxiriga qoʻymang — oʻzbekchadagi <em>emas</em> gap oxirida keladi, rus
tilidagi <b>не</b> esa oldinda.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то есть дом.</s></p>
  <p class="pe-good">Э́то дом. — hozirgi zamonda “boʻlmoq” feʼli qoʻyilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Что э́то? — Э́то Афсо́на.</s></p>
  <p class="pe-good">Кто э́то? — Э́то Афсо́на. — odam haqida <b>кто</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то соба́ка не.</s></p>
  <p class="pe-good">Э́то не соба́ка. — <b>не</b> soʻzning <b>oldida</b> turadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то кот? → Кот э́то?</s></p>
  <p class="pe-good">Э́то кот? — savolda soʻz tartibi <b>oʻzgarmaydi</b>, faqat ohang</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga nima tushadi? <b>___ э́то? — Э́то учи́тель.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Кто</strong>. Javobda odam turibdi
    (учи́тель — oʻqituvchi), demak savol <b>Кто э́то?</b> boʻladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu gapni ruschaga oʻgiring: <b>Bu — Toshkent.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Э́то Ташке́нт.</strong> Ikkita soʻz —
    va bu toʻliq gap. Orasiga hech nima qoʻyish kerak emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>Э́то соба́ка?</b> savoliga rad javobini bering (bu — mushuk).</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Нет, э́то не соба́ка. Э́то кот.</strong>
    <b>Нет</b> — javob, <b>не</b> — inkor qilinayotgan soʻz oldidagi zarracha.
    Ikkalasi bir gapda birga ishlaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Qaysi gap notoʻgʻri?<br>
     а) Э́то окно́. &nbsp; б) Э́то есть кни́га. &nbsp;
     в) Кто э́то? &nbsp; г) Э́то не стол.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б)</strong> — <b>есть</b> ortiqcha.
    Toʻgʻrisi: <b>Э́то кни́га.</b> Rus tilida hozirgi zamonda “boʻlmoq” feʼli
    qoʻyilmaydi. (<em>Есть</em> soʻzi boshqa maʼnoda ishlatiladi — PR-14 da
    koʻramiz.)</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     <b>кот</b> haqida qaysi savol toʻgʻri: <b>Кто э́то?</b> yoki <b>Что э́то?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Кто э́то?</strong> Mushuk — jonli
    mavjudot, shuning uchun rus tilida u <b>кто</b> tomonda. Faqat buyum, joy va
    tushunchalar <b>что</b> tomonda turadi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>э́то</b><span>bu</span></li>
  <li><b>кто</b><span>kim</span></li>
  <li><b>что</b><span>nima</span></li>
  <li><b>да / нет</b><span>ha / yoʻq</span></li>
  <li><b>не</b><span>emas (soʻz oldida)</span></li>
  <li><b>дом</b><span>uy</span></li>
  <li><b>шко́ла</b><span>maktab</span></li>
  <li><b>кни́га</b><span>kitob</span></li>
  <li><b>учи́тель</b><span>oʻqituvchi</span></li>
  <li><b>соба́ка / кот</b><span>it / mushuk</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Э́то + ot</b> = toʻliq ruscha gap. Hech qanday feʼl kerak emas.</li>
    <li>Rus tilida hozirgi zamonda “boʻlmoq” feʼli <b>ishlatilmaydi</b> — xuddi
        oʻzbekchadagidek.</li>
    <li><b>Кто?</b> — odam va hayvon. <b>Что?</b> — buyum, joy, tushuncha.</li>
    <li>Savolda soʻz tartibi <b>oʻzgarmaydi</b> — faqat ohang koʻtariladi.</li>
    <li><b>Нет</b> = javob “yoʻq”; <b>не</b> = inkor qilinayotgan soʻzning oldida.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-7: Salomlashish, tanishuv va murojaat: ты yoki вы?",
        "category": "russian",
        "order": 7,
        "summary": (
            "Rus tilida salomlashish, tanishish va minnatdorchilik. Eng muhimi — "
            "ты va вы orasidagi tanlov, ya'ni oʻzbekchadagi sen va siz."
        ),
        "stories": ["Два разгово́ра"],
        "content": """
<h2>PR-7: Salomlashish, tanishuv va murojaat: ты yoki вы?</h2>

<p>Rus tilida bitta soʻz sizni bir zumda yo qoʻpol, yo haddan tashqari rasmiy
qilib qoʻyishi mumkin. Bu soʻz — <b>ты</b> yoki <b>вы</b>. Yaxshi xabar shuki,
bu tanlov sizga notanish emas: oʻzbek tilida ham xuddi shu <em>sen</em> va
<em>siz</em> bor, va qoidasi deyarli bir xil. Bu darsda birinchi suhbatingizni
boshdan oxirigacha tuzamiz — salomdan xayrgacha.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Rasmiy va norasmiy salomlashishni ajratasiz</li>
    <li><b>ты</b> yoki <b>вы</b> ni toʻgʻri tanlaysiz</li>
    <li>Oʻzingizni tanishtirasiz: <b>Меня́ зову́т …</b></li>
    <li>Rahmat aytasiz, kechirim soʻraysiz va xayrlashasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Birinchi uchrashuv</span>
  <span class="pe-chip pe-chip--v">Здра́вствуйте</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">Меня́ зову́т …</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">О́чень прия́тно</span>
</div>

<h3>1. Salomlashish — ikkita darajа</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Rasmiy — <b>вы</b> bilan</p>
    <p style="font-size:1.25rem"><b>Здра́вствуйте!</b></p>
    <p>[здра́ствуйт'е] — oʻrtadagi <b>в</b> aytilmaydi!</p>
    <p>Notanish odam, oʻqituvchi, katta yoshli, xizmatchi, rahbar.</p>
    <p>Kun boʻyicha: До́брое у́тро (tong) · До́брый день (kunduz) ·
       До́брый ве́чер (kech).</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Norasmiy — <b>ты</b> bilan</p>
    <p style="font-size:1.25rem"><b>Приве́т!</b></p>
    <p>[пр'ив'э́т]</p>
    <p>Doʻst, tengdosh, sinfdosh, uka-singil, yaqin qarindosh.</p>
    <p>Yana: Здоро́во! (juda erkin, koʻproq oʻgʻil bolalar orasida).</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<b>Здра́вствуйте</b> — birinchi haftaning eng qiyin soʻzi, chunki u uzun va
ichida aytilmaydigan harf bor. Uni boʻlaklab mashq qiling:
<em>здра́ — ствуй — те</em>. Oʻrtadagi <b>в</b> tushib qoladi: [здра́-ствуй-т'е].
Agar qiynalsangiz, kunning vaqtiga qarab <b>До́брый день</b> deng — u ham
xuddi shunday muloyim va aytish osonroq.</div>

<h3>2. Ты yoki вы — asosiy tanlov</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kimga</th><th>Shakl</th><th>Salom</th><th>Oʻzbekchada</th></tr>
  <tr><td>Doʻst, tengdosh, sinfdosh</td><td class="pr-stem">ты</td>
      <td class="pr-end">Приве́т!</td><td class="pr-uz">sen</td></tr>
  <tr><td>Uka, singil, yaqin qarindosh</td><td class="pr-stem">ты</td>
      <td class="pr-end">Приве́т!</td><td class="pr-uz">sen</td></tr>
  <tr><td>Notanish odam</td><td class="pr-stem">вы</td>
      <td class="pr-end">Здра́вствуйте!</td><td class="pr-uz">siz</td></tr>
  <tr><td>Oʻqituvchi, katta yoshli</td><td class="pr-stem">вы</td>
      <td class="pr-end">Здра́вствуйте!</td><td class="pr-uz">siz</td></tr>
  <tr><td>Bir nechta odam (kim boʻlsa ham)</td><td class="pr-stem">вы</td>
      <td class="pr-end">Здра́вствуйте!</td><td class="pr-uz">sizlar</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu tizim sizda bor: <em>sen</em> — <b>ты</b>, <em>siz</em> — <b>вы</b>. Faqat
ikkita farqni bilib qoʻying. Birinchisi: oʻzbek tilida ota-onaga, buvi-buvaga
odatda <em>siz</em> deyiladi; rus oilasida esa ota-onaga ham, buvi-buvaga ham
deyarli doim <b>ты</b> deyiladi — bu qoʻpollik emas, aksincha yaqinlik belgisi.
Ikkinchisi: rus tilida <b>вы</b> koʻplik uchun ham ishlatiladi, shuning uchun
uch nafar doʻstingizga birdan murojaat qilsangiz ham <b>вы</b> deysiz.</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Ikkilansangiz — <b>вы</b> deng. Ortiqcha hurmat hech kimni xafa qilmaydi;
oʻrinsiz <b>ты</b> esa qilishi mumkin. Suhbatdosh oʻzi taklif qilganda
(<em>«Дава́й на ты»</em> — “kelinglar, senlashamiz”) shundagina <b>ты</b> ga
oʻtiladi. Bu taklifni odatda <b>katta yoshdagi</b> odam beradi.</div>

<h3>3. Tanishuv</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">— Как <span class="pe-hl pe-hl--s">вас</span> зову́т?<br>
     — <span class="pe-hl pe-hl--s">Меня́</span> зову́т Афсо́на. А
     <span class="pe-hl pe-hl--s">вас</span>?</p>
  <p class="pe-ex__rom">[как вас завут — мин'а́ завут афсона, а вас]</p>
  <p class="pe-ex__uz">— Ismingiz nima?<br>— Mening ismim Afsona. Sizniki-chi?</p>
  <p class="pe-ex__why">Soʻzma-soʻz: “sizni qanday chaqirishadi?”. Shuning uchun
     bu yerda “ism” degan soʻz umuman yoʻq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Как <span class="pe-hl pe-hl--s">тебя́</span> зову́т?<br>
     — <span class="pe-hl pe-hl--s">Меня́</span> зову́т Жасу́р.</p>
  <p class="pe-ex__uz">— Isming nima?<br>— Mening ismim Jasur.</p>
  <p class="pe-ex__why">Doʻstga <b>тебя́</b>, hurmat bilan <b>вас</b>.
     <b>Меня́</b> esa har doim bir xil — bu “meni”.</p>
</div>

<p>Tanishuv oxirida albatta shuni ayting:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>О́чень прия́тно</p>
    <p>“Tanishganimdan xursandman”. Har doim ishlaydi.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Как дела́?</p>
    <p>“Ishlar qalay?” Javob: <b>Хорошо́</b> · <b>Норма́льно</b> · <b>Непло́хо</b>.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>А вы?</p>
    <p>Savolni qaytarish. Doʻstga: <b>А ты?</b></p></div>
</div>

<h3>4. Rahmat, iltimos, kechirasiz</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Oʻqilishi</th><th>Maʼnosi</th><th>Qachon</th></tr>
  <tr><td class="pr-res">Спаси́бо</td><td class="pr-end">[спас'и́бъ]</td>
      <td class="pr-uz">Rahmat</td><td class="pr-uz">Har doim</td></tr>
  <tr><td class="pr-res">Большо́е спаси́бо</td><td class="pr-end">[бальшо́е спас'и́бъ]</td>
      <td class="pr-uz">Katta rahmat</td><td class="pr-uz">Kuchliroq</td></tr>
  <tr><td class="pr-res">Пожа́луйста</td><td class="pr-end">[пажа́лустъ]</td>
      <td class="pr-uz">Iltimos / Marhamat</td><td class="pr-uz">Soʻrashda va rahmatga javob</td></tr>
  <tr><td class="pr-res">Извини́те</td><td class="pr-end">[извин'и́т'е]</td>
      <td class="pr-uz">Kechirasiz</td><td class="pr-uz">Kichik xato, murojaat</td></tr>
  <tr><td class="pr-res">Прости́те</td><td class="pr-end">[прас'т'и́т'е]</td>
      <td class="pr-uz">Uzr soʻrayman</td><td class="pr-uz">Jiddiyroq holat</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Пожа́луйста</b> ikkita ishni bajaradi va bu oʻquvchilarni chalkashtiradi.
Soʻrovda u “iltimos”: <em>Кни́гу, пожа́луйста</em>. <b>Спаси́бо</b> ga javobda
esa u “arzimaydi”, “marhamat”: <em>— Спаси́бо! — Пожа́луйста!</em> Bitta soʻz,
ikkita vazifa. Talaffuzda esa oʻrtasi yutiladi: [пажа́лустъ], “pojalujsta” emas.</div>

<h3>5. Xayrlashish</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Rasmiy</p>
    <p style="font-size:1.25rem"><b>До свида́ния!</b></p>
    <p>[дъ свида́н'иъ] — “Koʻrishguncha”.</p>
    <p>Har qanday vaziyatda xavfsiz.</p>
    <p>Kechqurun: <b>Споко́йной но́чи</b> — xayrli tun.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Norasmiy</p>
    <p style="font-size:1.25rem"><b>Пока́!</b></p>
    <p>[пака́] — “Xayr”, doʻstlar orasida.</p>
    <p>Yana: <b>До за́втра</b> — ertagacha.</p>
    <p><b>Уви́димся</b> — koʻrishamiz.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Здра́вствуйте! Как вас зову́т?<br>
     — Меня́ зову́т Мари́на. А вас?<br>
     — Афсо́на. О́чень прия́тно.<br>
     — О́чень прия́тно. До свида́ния!</p>
  <p class="pe-ex__uz">— Assalomu alaykum! Ismingiz nima?<br>
     — Mening ismim Marina. Sizniki-chi?<br>
     — Afsona. Tanishganimdan xursandman.<br>
     — Men ham. Xayr!</p>
  <p class="pe-ex__why">Toʻrt qator — va bu toʻliq, tabiiy rus tanishuvi.
     Boshidan oxirigacha <b>вы</b> saqlangan.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Oʻqituvchiga: Приве́т! Как тебя́ зову́т?</s></p>
  <p class="pe-good">Здра́вствуйте! Как вас зову́т? — oʻqituvchiga har doim <b>вы</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Здра́вствуйте → [здравствуйте] (hamma harf bilan)</s></p>
  <p class="pe-good">[здра́ствуйт'е] — oʻrtadagi <b>в</b> aytilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Как зову́т вас?</s></p>
  <p class="pe-good">Как вас зову́т? — bu turgʻun ibora, soʻz tartibi oʻzgarmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Uch nafar doʻstga birdan: Как ты дела́?</s></p>
  <p class="pe-good">Приве́т! Как <b>вы</b>? / Как дела́? — bir nechta odamga murojaatda
     <b>вы</b> ishlatiladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Doʻkonda notanish sotuvchiga nima deysiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Здра́вствуйте!</strong> Notanish odam —
    demak <b>вы</b> darajasi. <em>Приве́т</em> bu yerda qoʻpol eshitiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga nima tushadi? <b>Как ___ зову́т?</b> (sinfdoshingizga)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>тебя́</strong>. Tengdosh — <b>ты</b>
    darajasi, va bu iborada <b>ты</b> ning shakli <b>тебя́</b> boʻladi.
    Hurmat bilan boʻlsa: <b>вас</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>Спаси́бо!</b> ga eng oddiy javob nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Пожа́луйста!</strong> Bu yerda u
    “arzimaydi” maʼnosida. Xuddi shu soʻz soʻrovda “iltimos” boʻladi —
    bitta soʻz, ikkita vazifa.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Qaysi juftlik <b>notoʻgʻri</b>?<br>
     а) Приве́т — Пока́ &nbsp; б) Здра́вствуйте — До свида́ния<br>
     в) Приве́т — До свида́ния &nbsp; г) Здра́вствуйте — Пока́</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>г)</strong> eng gʻalati. Rasmiy
    <b>Здра́вствуйте</b> bilan boshlab, norasmiy <b>Пока́</b> bilan tugatish —
    darajani suhbat oʻrtasida tushirish demak. в) ham gʻalati, lekin u
    xushmuomalalik tomonga xato, shuning uchun kechiriladi. <b>Bir suhbatda
    bitta darajada qoling.</b></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Ikkilanyapsiz: yangi qoʻshningiz sizdan bir oz katta. <b>Ты</b> mi yoki
     <b>вы</b> mi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Вы.</strong> Qoida oddiy: ikkilansang —
    <b>вы</b>. Ortiqcha hurmat hech kimni xafa qilmaydi. Keyinroq qoʻshningiz
    oʻzi <em>«Дава́й на ты»</em> desa, oʻshanda oʻtasiz.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>здра́вствуйте</b><span>assalomu alaykum (rasmiy)</span></li>
  <li><b>приве́т</b><span>salom (doʻstga)</span></li>
  <li><b>до свида́ния</b><span>xayr (rasmiy)</span></li>
  <li><b>пока́</b><span>xayr (doʻstga)</span></li>
  <li><b>меня́ зову́т</b><span>mening ismim</span></li>
  <li><b>о́чень прия́тно</b><span>tanishganimdan xursandman</span></li>
  <li><b>как дела́?</b><span>ishlar qalay?</span></li>
  <li><b>спаси́бо</b><span>rahmat</span></li>
  <li><b>пожа́луйста</b><span>iltimos / arzimaydi</span></li>
  <li><b>извини́те</b><span>kechirasiz</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Ты</b> = sen (doʻst, tengdosh, oila). <b>Вы</b> = siz (notanish, katta,
        rasmiy) <b>va</b> koʻplik.</li>
    <li>Ikkilansangiz — <b>вы</b>. Oʻtishni suhbatdosh taklif qiladi.</li>
    <li><b>Здра́вствуйте</b> [здра́ствуйт'е] — oʻrtadagi <b>в</b> aytilmaydi.</li>
    <li><b>Как вас зову́т? — Меня́ зову́т …</b> — turgʻun ibora, soʻz tartibi oʻzgarmaydi.</li>
    <li>Bir suhbatda <b>bitta darajada qoling</b>: Приве́т → Пока́,
        Здра́вствуйте → До свида́ния.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-8: Jins (род) — otlarning uch jinsi va uni oxiridan aniqlash",
        "category": "russian",
        "order": 8,
        "summary": (
            "Rus tilidagi har bir ot uch jinsdan biriga tegishli. Oʻzbek tilida bu "
            "tushuncha yoʻq — lekin jinsni soʻzning oxirgi harfidan deyarli har doim "
            "aniqlash mumkin."
        ),
        "stories": ["Стол, кни́га и окно́"],
        "content": """
<h2>PR-8: Jins (род) — otlarning uch jinsi va uni oxiridan aniqlash</h2>

<p>Bugungi dars — Prime Russian kursidagi birinchi haqiqatan <b>yangi</b> gʻoya.
Shu paytgacha hamma narsa oʻzbek tilidagi biror narsaga oʻxshardi. Endi esa
oʻxshamaydi: rus tilida <b>har bir ot</b> — stol ham, kitob ham, deraza ham —
uchta jinsdan biriga tegishli. Va bu tasodifiy emas: jinsni soʻzning
<b>oxirgi harfidan</b> deyarli har doim aniqlash mumkin. Shuning uchun bu
dars koʻrinishidan qiyin, amalda esa juda tartibli.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uchta jinsni — <b>мужско́й, же́нский, сре́дний</b> — bilib olasiz</li>
    <li>Istalgan otning jinsini oxirgi harfiga qarab aniqlaysiz</li>
    <li><b>-ь</b> bilan tugagan otlar nega alohida ekanini tushunasiz</li>
    <li>Otni <b>он, она́, оно́</b> olmoshlari bilan almashtirasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Jinsni oxirgi harf hal qiladi</span>
  <span class="pe-chip pe-chip--s">undosh → он</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">-а / -я → она́</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">-о / -е → оно́</span>
</div>

<h3>1. Uchta jins</h3>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">дом · стол · брат</p>
    <p><b>Undosh</b> bilan tugaydi.</p>
    <p>Yana <b>-й</b>: музе́й, чай.</p>
    <p>Olmoshi: <b>он</b></p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">кни́га · шко́ла · семья́</p>
    <p><b>-а</b> yoki <b>-я</b> bilan tugaydi.</p>
    <p>сестра́, ко́мната, ла́мпа.</p>
    <p>Olmoshi: <b>она́</b></p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний — oʻrta</p>
    <p class="pr-gender__form">окно́ · мо́ре · сло́во</p>
    <p><b>-о</b> yoki <b>-е</b> bilan tugaydi.</p>
    <p>у́тро, ме́сто, зда́ние.</p>
    <p>Olmoshi: <b>оно́</b></p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu yerda oʻzbek tili sizga <b>yordam bera olmaydi</b>, va buni ochiq aytish
kerak. Oʻzbek tilida grammatik jins umuman yoʻq: <em>u</em> — erkak ham, ayol
ham, stol ham. Rus tilida esa <b>стол</b> haqida <b>он</b>, <b>кни́га</b> haqida
<b>она́</b> deyiladi — garchi ikkalasi ham jonsiz buyum boʻlsa ham. Bu
“stolning jinsi bor” degani emas; bu shunchaki soʻzlarning grammatik
guruhlari, xuddi papkalar kabi. Nega kerak? Chunki keyinchalik sifat, oʻtgan
zamon feʼli va egalik olmoshi <b>shu guruhga qarab</b> oʻzgaradi.</div>

<h3>2. Nega jinsni bilish shart</h3>

<p>Jins oʻzicha kerak emas — u <b>boshqa soʻzlarni boshqaradi</b>. Mana nima
uchun buni birinchi haftadanoq oʻrganamiz:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Jins</th><th>Sifat (PR-12)</th><th>Egalik (PR-10)</th><th>Oʻtgan zamon (PR-23)</th></tr>
  <tr><td class="pr-res">м. дом</td><td class="pr-stem">но́в<span class="pr-end">ый</span> дом</td>
      <td class="pr-stem">мой дом</td><td class="pr-stem">дом бы<span class="pr-end">л</span></td></tr>
  <tr><td class="pr-res">ж. кни́га</td><td class="pr-stem">но́в<span class="pr-end">ая</span> кни́га</td>
      <td class="pr-stem">моя́ кни́га</td><td class="pr-stem">кни́га бы<span class="pr-end">ла</span></td></tr>
  <tr><td class="pr-res">с. окно́</td><td class="pr-stem">но́в<span class="pr-end">ое</span> окно́</td>
      <td class="pr-stem">моё окно́</td><td class="pr-stem">окно́ бы<span class="pr-end">ло</span></td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Shu jadvalga qarang va bitta naqshni koʻring: <b>-ый / -ая / -ое</b>,
<b>мой / моя́ / моё</b>, <b>был / была́ / бы́ло</b>. Uchala qatorda ham
<b>bir xil uchlik</b> takrorlanyapti. Rus tilining yarmi shu uchlikdan iborat.
Bugun jinsni oʻrgansangiz, kelasi darslar sizga tayyor boʻlib keladi.</div>

<h3>3. Он, она́, оно́ — otni almashtiradigan olmoshlar</h3>

<p>Rus tilida <b>он</b> faqat “u (erkak)” degani emas. U <b>har qanday erkak
jinsdagi ot</b>ning oʻrniga turadi — jonli boʻladimi, jonsizmi.</p>

<div class="pe-ex">
  <p class="pe-ex__ru">— Где стол? — <span class="pe-hl pe-hl--s">Он</span> здесь.</p>
  <p class="pe-ex__uz">— Stol qayerda? — U shu yerda.</p>
  <p class="pe-ex__why">Стол — erkak jinsi, shuning uchun <b>он</b>. Oʻzbekcha
     “u” bilan tarjima qilinadi, lekin ruschada tanlov jinsga bogʻliq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Где кни́га? — <span class="pe-hl pe-hl--s">Она́</span> здесь.</p>
  <p class="pe-ex__uz">— Kitob qayerda? — U shu yerda.</p>
  <p class="pe-ex__why">Кни́га — ayol jinsi → <b>она́</b>. Kitobning jinsi yoʻq,
     lekin <em>soʻzning</em> jinsi bor.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Где окно́? — <span class="pe-hl pe-hl--s">Оно́</span> здесь.</p>
  <p class="pe-ex__uz">— Deraza qayerda? — U shu yerda.</p>
  <p class="pe-ex__why">Окно́ — oʻrta jins → <b>оно́</b>. Bu shakl oʻzbek
     oʻquvchisi eng koʻp unutadigan shakl, chunki oʻzbekchada uchinchi variant
     yoʻq.</p>
</div>

<h3>4. Ikkita istisno, ikkalasi ham oson</h3>

<p><b>Birinchi istisno: tabiiy jins yutadi.</b> Bir nechta soʻz <b>-а</b> bilan
tugaydi, lekin erkakni bildiradi. Ular <b>erkak jinsida</b> qoladi, chunki
maʼno shakldan kuchliroq:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>па́па</p>
    <p>dada — <b>он</b>, garchi <b>-а</b> bilan tugasa ham</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>де́душка</p>
    <p>bobo — <b>он</b></p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>дя́дя · мужчи́на</p>
    <p>amaki · erkak — <b>он</b></p></div>
</div>

<p><b>Ikkinchi istisno: -ь bilan tugagan otlar.</b> Bu yerda oxirgi harf
javob bermaydi — <b>-ь</b> ham erkak, ham ayol jinsida boʻlishi mumkin:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">-ь erkak jinsida</p>
    <p>день (kun) · слова́рь (lugʻat) · учи́тель (oʻqituvchi) · дождь (yomgʻir)</p>
    <p><b>Ishonchli belgi:</b> <b>-тель</b> va <b>-арь</b> bilan tugasa —
       har doim erkak jinsi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">-ь ayol jinsida</p>
    <p>ночь (tun) · дверь (eshik) · тетра́дь (daftar) · жизнь (hayot)</p>
    <p><b>Ishonchli belgi:</b> <b>-ость</b> bilan tugasa — har doim ayol jinsi
       (ра́дость, мо́лодость, но́вость).</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>-ь</b> bilan tugagan yangi soʻzni <b>jinsi bilan birga yodlang</b> — xuddi
urgʻu kabi. Daftaringizga <em>дверь (ж.)</em>, <em>слова́рь (м.)</em> deb
yozing. Bu bir soniya vaqt oladi va sizni bir yillik xatodan qutqaradi. Yaxshi
xabar: bunday soʻzlar koʻp emas, va ikkita ishonchli belgi bor — <b>-тель / -арь
= erkak</b>, <b>-ость = ayol</b>.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Где кни́га? — Он здесь.</s></p>
  <p class="pe-good">Где кни́га? — <b>Она́</b> здесь. — кни́га ayol jinsi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>па́па — ayol jinsi, chunki -а bilan tugaydi</s></p>
  <p class="pe-good">па́па — <b>erkak</b> jinsi: maʼno shakldan kuchliroq</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Окно́? — Он здесь.</s></p>
  <p class="pe-good">Окно́? — <b>Оно́</b> здесь. — oʻrta jinsni unutmang</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>дверь va слова́рь — ikkalasi ham bir xil jinsda</s></p>
  <p class="pe-good"><b>дверь</b> — ayol, <b>слова́рь</b> — erkak. <b>-ь</b> ni
     jinsi bilan yodlash kerak</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>ко́мната</b> (xona) qaysi jinsda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ayol jinsi (же́нский)</strong> —
    <b>-а</b> bilan tugaydi. Olmoshi <b>она́</b>. Sifat bilan:
    <em>но́вая ко́мната</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>мо́ре</b> (dengiz) qaysi olmosh bilan almashtiriladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>оно́</strong> — <b>-е</b> bilan tugagan
    ot oʻrta jinsda. Xuddi shunday: <em>зда́ние, по́ле, со́лнце</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>де́душка</b> qaysi jinsda va nega?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Erkak jinsi</strong>, garchi <b>-а</b>
    bilan tugasa ham. Bu istisno: <b>tabiiy jins shaklni yutadi</b>. Xuddi
    shunday: па́па, дя́дя, мужчи́на.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Qaysi soʻz <b>ayol</b> jinsida?<br>
     а) слова́рь &nbsp; б) учи́тель &nbsp; в) но́вость &nbsp; г) день</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в) но́вость</strong> (yangilik) —
    <b>-ость</b> bilan tugagan soʻz har doim ayol jinsida. Qolgan uchtasi
    erkak jinsida: <em>слова́рь</em> (-арь), <em>учи́тель</em> (-тель),
    <em>день</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Nega jinsni bilish kerak? Bitta jumlada ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>sifat, egalik olmoshi va oʻtgan
    zamon feʼli otning jinsiga qarab oʻzgaradi</strong>: <em>но́в<b>ый</b> дом —
    но́в<b>ая</b> кни́га — но́в<b>ое</b> окно́</em>. Jinsni bilmasangiz, bu
    uchtasining hech birini toʻgʻri qoʻya olmaysiz.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>род</b><span>jins (grammatik)</span></li>
  <li><b>мужско́й / же́нский / сре́дний</b><span>erkak / ayol / oʻrta</span></li>
  <li><b>он / она́ / оно́</b><span>u (jinsga qarab)</span></li>
  <li><b>ко́мната</b><span>xona</span></li>
  <li><b>окно́</b><span>deraza</span></li>
  <li><b>дверь</b><span>eshik (ayol j.)</span></li>
  <li><b>слова́рь</b><span>lugʻat (erkak j.)</span></li>
  <li><b>тетра́дь</b><span>daftar (ayol j.)</span></li>
  <li><b>мо́ре</b><span>dengiz (oʻrta j.)</span></li>
  <li><b>здесь</b><span>shu yerda</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Har bir ot uch jinsdan birida: <b>мужско́й · же́нский · сре́дний</b>.</li>
    <li>Jinsni <b>oxirgi harf</b> aytadi: undosh → <b>он</b>, -а/-я → <b>она́</b>,
        -о/-е → <b>оно́</b>.</li>
    <li>Jins buyumga emas, <b>soʻzga</b> tegishli: стол — <b>он</b>,
        кни́га — <b>она́</b>.</li>
    <li>Istisnolar: <b>па́па, де́душка, дя́дя</b> — erkak jinsi (maʼno yutadi);
        <b>-ь</b> — ikki xil boʻlishi mumkin.</li>
    <li><b>-тель / -арь</b> = erkak, <b>-ость</b> = ayol. Qolgan <b>-ь</b> larni
        jinsi bilan yodlang.</li>
    <li>Jins kerak, chunki <b>sifat, egalik va oʻtgan zamon</b> unga qarab oʻzgaradi.</li>
  </ul>
</div>
""",
    },
]
