# -*- coding: utf-8 -*-
"""Prime Russian — Block B, darslar 15–17.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

Har bir dars uchta boʻlakdan biri: dars + mashq + oʻqish matni.
Mashqlar:        practice/management/commands/_practice_pr_15_17.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_15_17.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_15_17.py --author=prime
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
        "title": "PR-15: Savol soʻzlari: кто, что, где, когда, почему, как, какой",
        "category": "russian",
        "order": 15,
        "summary": (
            "Rus tilida savol berish uchun yordamchi feʼl kerak emas — savol soʻzini "
            "oldinga qoʻyasiz, xolos. Joy haqidagi uchlik где/куда/откуда oʻzbekchadagi "
            "qayerda/qayerga/qayerdan bilan aynan mos keladi."
        ),
        "stories": ["Кто? Что? Где?"],
        "content": """
<h2>PR-15: Savol soʻzlari: кто, что, где, когда, почему, как, какой</h2>

<p>Ingliz tilini oʻrganganlar bu darsda yengil nafas oladi. U yerda savol berish uchun
gapni buzish, <em>do</em> yoki <em>does</em> qoʻshish, soʻzlarni oʻrin almashtirish
kerak. Rus tilida esa <b>hech nima qilmaysiz</b>: savol soʻzini gap boshiga qoʻyasiz
va tamom. Xuddi oʻzbekchadagidek. Bu darsda savol soʻzlarining butun toʻplamini bir
joyga yigʻamiz — bir nechtasini siz allaqachon bilasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Sakkizta savol soʻzini biladigan qilib oʻrganasiz</li>
    <li>Joy haqidagi uchlikni ajratasiz: <b>где / куда́ / отку́да</b></li>
    <li><b>Почему́</b> va <b>заче́м</b> orasidagi farqni bilasiz</li>
    <li>Savol ohangini toʻgʻri qoʻyasiz — u “ha/yoʻq” savolidan boshqacha</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Savol qolipi</span>
  <span class="pe-chip pe-chip--s">savol soʻzi</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">qolgan gap</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">tamom</span>
</div>

<h3>1. Butun toʻplam</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Savol</th><th>Maʼnosi</th><th>Misol</th><th>Javob</th></tr>
  <tr><td class="pr-res">кто?</td><td class="pr-uz">kim?</td>
      <td class="pr-stem">Кто э́то?</td><td class="pr-end">Э́то Афсо́на.</td></tr>
  <tr><td class="pr-res">что?</td><td class="pr-uz">nima?</td>
      <td class="pr-stem">Что э́то?</td><td class="pr-end">Э́то шко́ла.</td></tr>
  <tr><td class="pr-res">где?</td><td class="pr-uz">qayerda?</td>
      <td class="pr-stem">Где Жасу́р?</td><td class="pr-end">Здесь.</td></tr>
  <tr><td class="pr-res">куда́?</td><td class="pr-uz">qayerga?</td>
      <td class="pr-stem">Куда́?</td><td class="pr-end">Домо́й.</td></tr>
  <tr><td class="pr-res">отку́да?</td><td class="pr-uz">qayerdan?</td>
      <td class="pr-stem">Отку́да?</td><td class="pr-end">Отту́да.</td></tr>
  <tr><td class="pr-res">когда́?</td><td class="pr-uz">qachon?</td>
      <td class="pr-stem">Когда́ уро́к?</td><td class="pr-end">За́втра.</td></tr>
  <tr><td class="pr-res">почему́?</td><td class="pr-uz">nega?</td>
      <td class="pr-stem">Почему́ здесь?</td><td class="pr-end">Потому́ что бли́зко.</td></tr>
  <tr><td class="pr-res">как?</td><td class="pr-uz">qanday?</td>
      <td class="pr-stem">Как дела́?</td><td class="pr-end">Хорошо́.</td></tr>
</table></div>

<p>Bularga siz allaqachon bilgan uchtasini qoʻshing: <b>чей?</b> (kimning — PR-10),
<b>како́й?</b> (qanday — PR-12) va <b>ско́лько?</b> (nechta — PR-13). Bu uchtasi
otga moslashadi, qolgani esa hech qachon oʻzgarmaydi.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Ingliz tilida <em>Where do you live?</em> deyish uchun <b>do</b> qoʻshish kerak.
Rus tilida ham, oʻzbek tilida ham bunday yordamchi <b>yoʻq</b>: <em>Qayerda
yashaysan?</em> — <b>Где ты живёшь?</b> Savol soʻzi oldinga chiqadi, qolgani
oʻz joyida qoladi. Sizga oʻrganish uchun hech narsa yoʻq — bu allaqachon sizning
odatingiz.</div>

<h3>2. Где / Куда́ / Отку́да — joyning uch savoli</h3>

<p>Rus tili joy haqida <b>uch xil</b> savol beradi, va ular almashtirilmaydi:</p>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Где? — qayerda?</p>
    <p class="pr-gender__form">Turgan joy</p>
    <p>— Где Дилно́за?<br>— <b>Здесь.</b> / <b>Там.</b></p>
    <p>Harakat yoʻq.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Куда́? — qayerga?</p>
    <p class="pr-gender__form">Yoʻnalish (u tomonga)</p>
    <p>— Куда́?<br>— <b>Домо́й.</b> / <b>Туда́.</b> / <b>Сюда́.</b></p>
    <p>Harakat bor.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Отку́да? — qayerdan?</p>
    <p class="pr-gender__form">Chiqish nuqtasi</p>
    <p>— Отку́да?<br>— <b>Отту́да.</b> / <b>Отсю́да.</b></p>
    <p>Harakat bor.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu — kursning eng chiroyli mosliklaridan biri. Oʻzbek tilida ham aynan shu uchlik
bor: <em>qayer<b>da</b></em> — <em>qayer<b>ga</b></em> — <em>qayer<b>dan</b></em>.
Ingliz tili buni ikkitaga siqadi (<em>where</em> / <em>where … from</em>), rus va
oʻzbek tillari esa uchtasini ham alohida saqlaydi. Yaʼni bu tushunchani sizga
oʻrgatish shart emas — faqat uchta ruscha soʻzni yodlash kifoya.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Bu savollarga <b>ot bilan</b> javob berish uchun kelishik kerak boʻladi:
<em>Где? — <b>в шко́ле</b></em> (PR-30), <em>Куда́? — <b>в шко́лу</b></em> (PR-33),
<em>Отку́да? — <b>из шко́лы</b></em> (PR-35). Hozircha ravish bilan javob bering —
<b>здесь, там, туда́, сюда́, домо́й, отту́да</b> — bular hech qanday kelishik
talab qilmaydi va ular bilan bemalol gaplashish mumkin.</div>

<h3>3. Почему́ va заче́м — ikkita “nega”</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Почему́? — <b>sabab</b></p>
    <p style="font-size:1.05rem">“Nega? Nima sababdan?”</p>
    <p>Orqaga qaraydi: <b>nima boʻlgani uchun</b>.</p>
    <p>— Почему́ Жасу́р до́ма?<br>
       — Потому́ что сего́дня <span class="pe-hl pe-hl--neg">суббо́та</span>.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Заче́м? — <b>maqsad</b></p>
    <p style="font-size:1.05rem">“Nima maqsadda? Nima uchun?”</p>
    <p>Oldinga qaraydi: <b>nima uchun kerak</b>.</p>
    <p>— Заче́м э́то?<br>
       — Э́то пода́рок.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Ikkalasini “nega” deb tarjima qilsangiz ham boʻladi va sizni tushunishadi.
Lekin farqni bilib qoʻying: <b>почему́</b> — <em>sababi bor</em>,
<b>заче́м</b> — <em>maqsadi bor</em>. Oʻzbekchada bu farq
<em>“nega”</em> va <em>“nima uchun”</em> orasida sezilib turadi. Ikkilansangiz
<b>почему́</b> deng — u kengroq ishlatiladi.</div>

<h3>4. Savol ohangi — “ha/yoʻq” savolidan boshqacha</h3>

<p>PR-6 da koʻrdik: <em>Э́то шко́ла?</em> savolida ovoz <b>koʻtariladi</b>. Savol
soʻzi bor gapda esa aksincha — ovoz savol soʻzida <b>koʻtarilib, keyin
pasayadi</b>:</p>

<div class="pr-say">
  <span class="pr-say__from">Э́то шко́ла?</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">ovoz ↗ koʻtariladi</span>
  <span class="pr-say__why">ha/yoʻq savoli</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">Где шко́ла?</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">ГДЕ ↗ … шко́ла ↘</span>
  <span class="pr-say__why">savol soʻzi bor — ovoz keyin pasayadi</span>
</div>

<p>Buni bilmaslik xato emas, lekin bilish talaffuzingizni birdan tabiiy qiladi.
Rus quloqi bu ikki ohangni darrov ajratadi.</p>

<h3>5. Savol soʻzi doim boshdami?</h3>

<p>Deyarli har doim — lekin taʼkid uchun uni koʻchirish mumkin:</p>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Кто</span> э́то?<br>
     А э́то <span class="pe-hl pe-hl--s">кто</span>?</p>
  <p class="pe-ex__uz">Bu kim?<br>Bunisi-chi, kim?</p>
  <p class="pe-ex__why">Ikkinchi shakl suhbatda tez-tez uchraydi: bir nechta
     narsani ketma-ket koʻrsatganda. Maʼnosi bir xil, ohangi boshqa.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--s">Кака́я</span> э́то шко́ла?<br>
     — Но́вая.<br>
     — А <span class="pe-hl pe-hl--s">где</span> она́?<br>
     — Там.</p>
  <p class="pe-ex__uz">— Bu qanday maktab?<br>— Yangi.<br>
     — U qayerda?<br>— Ana u yerda.</p>
  <p class="pe-ex__why">Javoblar qisqa — rus suhbatida butun gapni takrorlash
     shart emas, xuddi oʻzbekchadagidek.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Где ты идёшь?</s> (harakat bor)</p>
  <p class="pe-good"><b>Куда́</b> ты идёшь? — harakat boʻlsa <b>куда́</b>, <b>где</b> emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ты где живёшь?</s> — “Do you live where?”</p>
  <p class="pe-good"><b>Где</b> ты живёшь? — savol soʻzi odatda boshda turadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Как дела́ у тебя́ есть?</s></p>
  <p class="pe-good"><b>Как дела́?</b> — turgʻun ibora, hech nima qoʻshilmaydi (PR-7)</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кто э́то кни́га?</s></p>
  <p class="pe-good"><b>Что</b> э́то? — kitob jonsiz, demak <b>что</b> (PR-6)</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>___ уро́к? — За́втра.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Когда́ уро́к?</strong> Javobda vaqt turibdi
    (<em>за́втра</em>), demak savol <b>когда́</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>Где</b> yoki <b>куда́</b>? &nbsp; <b>___ ты? — Домо́й.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Куда́ ты?</strong> Javob <em>домо́й</em>
    (“uyga”) — bu yoʻnalish, demak <b>куда́</b>. Agar javob <em>до́ма</em>
    (“uyda”) boʻlsa edi, savol <b>где</b> boʻlardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>почему́</b> yoki <b>заче́м</b>? &nbsp; <b>___ э́то? — Э́то пода́рок.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Заче́м</strong> — javob <em>maqsad</em>ni
    aytyapti (nima uchun turibdi — sovgʻa qilish uchun), sababni emas.
    <b>Почему́</b> boʻlsa, javob <em>Потому́ что…</em> bilan boshlanardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>Где шко́ла?</b> gapida ovoz qanday yuradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Ovoz <strong>savol soʻzida koʻtarilib, keyin
    pasayadi</strong>: ГДЕ ↗ шко́ла ↘. Bu “ha/yoʻq” savolidan farq qiladi —
    u yerda ovoz oxirigacha koʻtariladi: <em>Э́то шко́ла?</em> ↗</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi savol soʻzi otga <b>moslashadi</b>?<br>
     а) где &nbsp; б) когда́ &nbsp; в) како́й &nbsp; г) почему́</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в) како́й</strong> — <em>како́й / кака́я /
    како́е / каки́е</em>. Xuddi shunday <b>чей</b> (PR-10) ham moslashadi. Qolgan
    savol soʻzlari hech qachon oʻzgarmaydi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>где?</b><span>qayerda?</span></li>
  <li><b>куда́?</b><span>qayerga?</span></li>
  <li><b>отку́да?</b><span>qayerdan?</span></li>
  <li><b>когда́?</b><span>qachon?</span></li>
  <li><b>почему́?</b><span>nega? (sabab)</span></li>
  <li><b>заче́м?</b><span>nima uchun? (maqsad)</span></li>
  <li><b>как?</b><span>qanday?</span></li>
  <li><b>здесь / там</b><span>bu yerda / u yerda</span></li>
  <li><b>сюда́ / туда́</b><span>bu yerga / u yerga</span></li>
  <li><b>потому́ что</b><span>chunki</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Savol berish uchun <b>yordamchi feʼl kerak emas</b> — savol soʻzini oldinga
        qoʻying, xolos.</li>
    <li>Joyning uch savoli: <b>где</b> (qayerda) · <b>куда́</b> (qayerga) ·
        <b>отку́да</b> (qayerdan) — oʻzbekcha bilan aynan mos.</li>
    <li><b>Почему́</b> = sabab, <b>заче́м</b> = maqsad.</li>
    <li>Savol soʻzi bor gapda ovoz <b>koʻtarilib, keyin pasayadi</b>; “ha/yoʻq”
        savolida esa oxirigacha koʻtariladi.</li>
    <li>Faqat <b>чей, како́й, ско́лько</b> otga moslashadi. Qolgani oʻzgarmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-16: Bu va anavi: этот, эта, это, эти — va «тот»",
        "category": "russian",
        "order": 16,
        "summary": (
            "PR-6 dagi mustaqil «это» bilan otga yopishadigan «этот» ni bir umrga "
            "ajratasiz, va «тот» bilan uzoqdagi narsani koʻrsatishni oʻrganasiz."
        ),
        "stories": ["Э́тот и́ли тот?"],
        "content": """
<h2>PR-16: Bu va anavi: этот, эта, это, эти — va «тот»</h2>

<p>PR-6 da <b>Э́то кни́га</b> deb oʻrgandingiz — “bu kitob”. Endi <b>Э́та кни́га</b> ni
koʻrasiz va u ham “bu kitob” deb tarjima qilinadi. Ikkalasi bir xilmi? Yoʻq — va bu
farq oʻquvchilarni yillar davomida chalkashtiradi. Yaxshi xabar shuki, farqni
bir marta koʻrsangiz, u boshqa hech qachon qiyin boʻlmaydi. Bugun mana shu bitta
ishni qilamiz, keyin uzoqdagi narsani koʻrsatadigan <b>тот</b> ni qoʻshamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Mustaqil <b>э́то</b> bilan otga yopishadigan <b>э́тот</b> ni ajratasiz</li>
    <li>Toʻrt shaklni bilasiz: <b>э́тот / э́та / э́то / э́ти</b></li>
    <li><b>Тот</b> bilan uzoqdagi yoki boshqa narsani koʻrsatasiz</li>
    <li><b>Вот</b> va <b>там</b> ni oʻz oʻrnida ishlatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki xil «э́то»</span>
  <span class="pe-chip pe-chip--s">Э́то кни́га.</span>
  <span class="pe-op">= “bu — kitob”</span>
  <span class="pe-chip pe-chip--o">Э́та кни́га…</span>
  <span class="pe-op">= “bu kitob …”</span>
</div>

<h3>1. Butun farq bitta jadvalda</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Mustaqil <b>э́то</b> — PR-6</p>
    <p>Oʻzi turadi, hech nimaga moslashmaydi.</p>
    <p><b>Bitta shakl</b>, hamma holat uchun.</p>
    <p style="font-size:1.05rem">Э́то дом. <em>(bu — uy)</em><br>
       Э́то кни́га. <em>(bu — kitob)</em><br>
       Э́то о́кна. <em>(bular — derazalar)</em></p>
    <p>Maʼnosi: “<b>bu narsa — falon</b>”. Gapni <b>boshlaydi</b>.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Aniqlovchi <b>э́тот</b> — PR-16</p>
    <p>Otga yopishadi va unga moslashadi.</p>
    <p><b>Toʻrtta shakl</b>, jinsga qarab.</p>
    <p style="font-size:1.05rem">э́тот дом <em>(bu uy)</em><br>
       э́та кни́га <em>(bu kitob)</em><br>
       э́ти о́кна <em>(bu derazalar)</em></p>
    <p>Maʼnosi: “<b>aynan shu</b>, boshqasi emas”. Gapning <b>ichida</b> turadi.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Tekshiruvning eng oson yoʻli: <b>oʻzbekchaga oʻgiring va tire qoʻyib koʻring</b>.
“Bu — kitob” (tire tushadi) → mustaqil <b>э́то</b>. “Bu kitob yangi” (tire tushmaydi,
“bu” kitobga yopishgan) → <b>э́та</b>. Boshqacha aytganda: <em>“bu”</em> dan keyin
toʻxtalsangiz — <b>э́то</b>; toʻxtalmasangiz — <b>э́тот</b>.</div>

<h3>2. Toʻrtta shakl — yana oʻsha naqsh</h3>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">м. — э́тот</p>
    <p class="pr-gender__form">э́тот дом</p>
    <p>э́тот го́род · э́тот уро́к</p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">ж. — э́та</p>
    <p class="pr-gender__form">э́та кни́га</p>
    <p>э́та шко́ла · э́та ру́чка</p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">с. — э́то · мн. — э́ти</p>
    <p class="pr-gender__form">э́то окно́<br>э́ти кни́ги</p>
    <p>э́то сло́во · э́ти дома́</p>
  </div>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Oʻrta jinsning aniqlovchi shakli — <b>э́то</b>, yaʼni mustaqil <b>э́то</b> bilan
<em>bir xil koʻrinadi</em>. Shuning uchun <b>э́то окно́</b> ikki xil oʻqilishi
mumkin: “bu — deraza” yoki “bu deraza”. Qaysi biri ekanini <b>davomi</b> aytadi:
<em>Э́то окно́.</em> (nuqta — nomlash) va <em>Э́то окно́ большо́е.</em> (davom bor —
“bu deraza katta”). Boshqa jinslarda bunday chalkashlik yoʻq.</div>

<h3>3. Тот — uzoqdagi yoki boshqasi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Jins</th><th>Yaqin</th><th>Uzoq</th><th>Misol</th></tr>
  <tr><td class="pr-res">м.</td><td class="pr-stem">э́тот</td><td class="pr-end">тот</td>
      <td class="pr-uz">Э́тот дом но́вый, а тот ста́рый.</td></tr>
  <tr><td class="pr-res">ж.</td><td class="pr-stem">э́та</td><td class="pr-end">та</td>
      <td class="pr-uz">Э́та кни́га моя́, а та твоя́.</td></tr>
  <tr><td class="pr-res">с.</td><td class="pr-stem">э́то</td><td class="pr-end">то</td>
      <td class="pr-uz">Э́то окно́ большо́е, а то ма́ленькое.</td></tr>
  <tr><td class="pr-res">мн.</td><td class="pr-stem">э́ти</td><td class="pr-end">те</td>
      <td class="pr-uz">Э́ти ру́чки но́вые, а те ста́рые.</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Кака́я кни́га твоя́? <span class="pe-hl pe-hl--s">Э́та</span>
     и́ли <span class="pe-hl pe-hl--o">та</span>?<br>
     — <span class="pe-hl pe-hl--o">Та</span>.</p>
  <p class="pe-ex__uz">— Qaysi kitob seniki? Bumi yoki anavimi?<br>— Anavi.</p>
  <p class="pe-ex__why">Otni takrorlash shart emas — <b>э́та</b> va <b>та</b>
     oʻzi yetadi. Bu rus suhbatida juda koʻp uchraydi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbek tilida koʻrsatishning <b>uchta</b> darajasi bor: <em>bu</em> (juda yaqin),
<em>shu</em> (yaqin, gapirilgan), <em>u / ana u</em> (uzoq). Rus tilida esa
<b>ikkita</b>: <b>э́тот</b> va <b>тот</b>. Yaʼni oʻzbekchadagi <em>bu</em> va
<em>shu</em> — ikkalasi ham <b>э́тот</b> ga tushadi. Bu sizni yengillashtiradi:
tanlov ikkitadan, uchtadan emas. Va amalda ruslar <b>э́тот</b> ni ancha koʻp
ishlatadi — <b>тот</b> koʻpincha “boshqasi” yoki “oʻsha, gapirilgani” maʼnosini
beradi.</div>

<h3>4. Вот va там — koʻrsatish soʻzlari</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Вот</p>
    <p>“Mana”. Barmoq bilan koʻrsatasiz, narsa yaqin.<br>
       <em>Вот моя́ кни́га.</em> — Mana mening kitobim.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Там</p>
    <p>“Ana u yerda”. Narsa uzoq.<br>
       <em>Там шко́ла.</em> — Maktab ana u yerda.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Здесь</p>
    <p>“Shu yerda”. Joyni bildiradi, koʻrsatmaydi.<br>
       <em>Дилно́за здесь.</em> — Dilnoza shu yerda.</p></div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<b>Вот</b> va <b>здесь</b> ni adashtirmang. <b>Вот</b> — bu <em>koʻrsatish</em>
(“mana, qara!”), <b>здесь</b> — bu <em>joy</em> (“shu yerda”). Solishtiring:
<em>Вот шко́ла</em> = “mana maktab” (endi koʻrsatyapman), <em>Шко́ла здесь</em> =
“maktab shu yerda” (joyini aytyapman).</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́тот кни́га моя́.</s></p>
  <p class="pe-good"><b>Э́та</b> кни́га моя́. — <em>кни́га</em> ayol jinsi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́та — шко́ла.</s> (nomlamoqchi boʻlib)</p>
  <p class="pe-good"><b>Э́то</b> шко́ла. — nomlashda mustaqil <b>э́то</b> ishlatiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то дом но́вый, а э́то ста́рый.</s></p>
  <p class="pe-good">Э́тот дом но́вый, а <b>тот</b> ста́рый. — uzoqdagisi uchun <b>тот</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Здесь моя́ кни́га!</s> (koʻrsatib turib)</p>
  <p class="pe-good"><b>Вот</b> моя́ кни́га! — koʻrsatganda <b>вот</b>, <b>здесь</b> emas</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>___ шко́ла но́вая.</b> (bu maktab)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Э́та шко́ла но́вая.</strong> Bu yerda “bu”
    maktabga yopishgan (“bu maktab yangi”), demak aniqlovchi shakl kerak.
    <em>Шко́ла</em> ayol jinsi → <b>э́та</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>___ шко́ла.</b> (bu — maktab)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Э́то шко́ла.</strong> Bu yerda nomlayapmiz —
    “bu — maktab”. Mustaqil <b>э́то</b>, u hech qachon oʻzgarmaydi. Oldingi savol
    bilan yonma-yon qoʻying: butun dars shu ikki gapda.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Э́ти ру́чки но́вые, а ___ ста́рые.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>те</strong>. Koʻplikda uzoqdagisi —
    <b>те</b>. Toʻliq qator: <em>э́тот — тот, э́та — та, э́то — то,
    э́ти — те</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>Э́то окно́</b> — bu “bu — deraza” mi yoki “bu deraza” mi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ikkalasi ham boʻlishi mumkin</strong> —
    oʻrta jinsda ikki shakl bir xil koʻrinadi. Davomi hal qiladi:
    <em>Э́то окно́.</em> (nuqta) = “bu — deraza”. <em>Э́то окно́ большо́е.</em>
    (davom bor) = “bu deraza katta”.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Doʻstingizga kitobingizni koʻrsatyapsiz. <b>Вот</b> mi yoki <b>здесь</b> mi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Вот моя́ кни́га!</strong> — koʻrsatganda
    <b>вот</b> (“mana”). <b>Здесь</b> esa joyni bildiradi: <em>Моя́ кни́га
    здесь</em> — “kitobim shu yerda”.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>э́то</b><span>bu (mustaqil, nomlash)</span></li>
  <li><b>э́тот / э́та / э́ти</b><span>bu (otga yopishadi)</span></li>
  <li><b>тот / та / то / те</b><span>anavi, oʻsha</span></li>
  <li><b>вот</b><span>mana</span></li>
  <li><b>там</b><span>ana u yerda</span></li>
  <li><b>здесь</b><span>shu yerda</span></li>
  <li><b>и́ли</b><span>yoki</span></li>
  <li><b>друго́й</b><span>boshqa</span></li>
  <li><b>тако́й</b><span>shunday, bunaqa</span></li>
  <li><b>сам</b><span>oʻzi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Э́то</b> mustaqil turadi va nomlaydi: <em>Э́то кни́га</em> = “bu — kitob”.
        Hech qachon oʻzgarmaydi.</li>
    <li><b>Э́тот</b> otga yopishadi va unga moslashadi:
        <b>э́тот / э́та / э́то / э́ти</b>.</li>
    <li>Tekshiruv: oʻzbekchada “bu” dan keyin <b>toʻxtalsangiz</b> — <b>э́то</b>;
        toʻxtalmasangiz — <b>э́тот</b>.</li>
    <li>Uzoqdagisi: <b>тот / та / то / те</b>. Oʻzbekchadagi <em>bu</em> va
        <em>shu</em> — ikkalasi ham <b>э́тот</b>.</li>
    <li><b>Вот</b> = “mana” (koʻrsatish), <b>здесь</b> = “shu yerda” (joy).</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-17: Да, нет, не, ни — inkorning toʻrt shakli",
        "category": "russian",
        "order": 17,
        "summary": (
            "Bitta “yoʻq” tushunchasi ruschada toʻrtta soʻzga boʻlingan. Har birining "
            "oʻz vazifasi bor, va «не X, а Y» qurilmasi bilan aniq gapirishni "
            "oʻrganasiz."
        ),
        "stories": ["Нет, спаси́бо"],
        "content": """
<h2>PR-17: Да, нет, не, ни — inkorning toʻrt shakli</h2>

<p>Oʻzbek tilida inkor uchun asosan bitta soʻz yetadi: <b>emas</b>. Rus tilida esa
toʻrtta soʻz bor va ular bir-birining oʻrnini bosmaydi: <b>да</b>, <b>нет</b>,
<b>не</b>, <b>ни</b>. Oʻquvchilar koʻpincha <em>нет</em> bilan <em>не</em> ni
adashtiradi — bu darsning asosiy ishi ana shu ikkisini bir umrga ajratish. Yoʻl-yoʻlakay
esa siz rus tilidagi eng foydali qurilmalardan birini oʻrganasiz: <b>«не X, а Y»</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Нет</b> va <b>не</b> ni bir umrga ajratasiz</li>
    <li><b>Не</b> ni toʻgʻri joyga qoʻyasiz — u maʼnoni boshqaradi</li>
    <li><b>«не X, а Y»</b> bilan xatoni tuzatasiz</li>
    <li><b>Ни … ни …</b> bilan ikkalasini ham inkor qilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrtta soʻz</span>
  <span class="pe-chip pe-chip--v">да</span>
  <span class="pe-chip pe-chip--neg">нет</span>
  <span class="pe-chip pe-chip--neg">не</span>
  <span class="pe-chip pe-chip--neg">ни</span>
</div>

<h3>1. Нет va не — asosiy farq</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h"><b>НЕТ</b> — javob va yoʻqlik</p>
    <p><b>1.</b> Savolga javob: “yoʻq”.<br>
       — Э́то шко́ла?<br>— <b>Нет.</b></p>
    <p><b>2.</b> “Mavjud emas”:<br>
       — Здесь есть кни́га?<br>— <b>Нет.</b></p>
    <p>Oʻzi turadi. Odatda <b>gap boshida</b> yoki butun javob sifatida.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h"><b>НЕ</b> — soʻzni inkor qiladi</p>
    <p>Har doim <b>bir soʻzning oldida</b> turadi va aynan oʻshani inkor qiladi.</p>
    <p>Э́то <b>не</b> шко́ла.<br>
       Дом <b>не</b> большо́й.<br>
       <b>Не</b> здесь.</p>
    <p>Oʻzi tura olmaydi — unga inkor qilinadigan soʻz kerak.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Э́то шко́ла?<br>
     — <span class="pe-hl pe-hl--neg">Нет</span>, э́то
     <span class="pe-hl pe-hl--neg">не</span> шко́ла. Э́то библиоте́ка.</p>
  <p class="pe-ex__uz">— Bu maktabmi?<br>— Yoʻq, bu maktab emas. Bu kutubxona.</p>
  <p class="pe-ex__why">Ikkalasi bir gapda ishlayapti: <b>нет</b> — savolga javob,
     <b>не</b> — <em>шко́ла</em> soʻzini inkor qilyapti.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada <b>emas</b> soʻzning <em>orqasida</em> turadi: <em>bu maktab
<b>emas</b></em>. Ruschada <b>не</b> soʻzning <em>oldida</em> turadi:
<em>э́то <b>не</b> шко́ла</em>. Bu kichik farq, lekin u har kuni xatoga sabab
boʻladi — chunki qoʻl oʻz-oʻzidan oʻzbekcha tartibni yozadi. Har safar “emas”
deb oʻylaganingizda, uni <b>oldinga koʻchiring</b>.</div>

<h3>2. Не qayerda tursa — oʻshani inkor qiladi</h3>

<p>Bu rus tilining kuchli tomoni: <b>не</b> ni koʻchirib, gapning maʼnosini
aniq boshqarasiz.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Gap</th><th>Nima inkor qilinyapti</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res"><b>Не</b> я здесь.</td><td class="pr-stem">я</td>
      <td class="pr-uz">Men emas (boshqa odam shu yerda).</td></tr>
  <tr><td class="pr-res">Я <b>не</b> здесь.</td><td class="pr-stem">здесь</td>
      <td class="pr-uz">Men shu yerda emasman (boshqa joydaman).</td></tr>
  <tr><td class="pr-res">Э́то <b>не</b> мой дом.</td><td class="pr-stem">мой</td>
      <td class="pr-uz">Bu mening uyim emas (boshqaning uyi).</td></tr>
  <tr><td class="pr-res">Э́то мой <b>не</b> дом.</td><td class="pr-stem">дом</td>
      <td class="pr-uz">Gʻalati gap — bunday deyilmaydi.</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Не</b> ni inkor qilmoqchi boʻlgan soʻzning <b>bevosita oldiga</b> qoʻying.
Agar butun gapni inkor qilmoqchi boʻlsangiz, uni kesimning oldiga qoʻying.
Va uni gap oxiriga <b>hech qachon</b> qoʻymang — bu oʻzbekcha odat, ruschada
xato.</div>

<h3>3. «Не X, а Y» — tuzatish qurilmasi</h3>

<p>Bu rus tilida har kuni ishlatiladigan qolip. U “X emas, balki Y” degani, va u
<b>а</b> bogʻlovchisi bilan yuradi:</p>

<div class="pe-ex">
  <p class="pe-ex__ru">Он <span class="pe-hl pe-hl--neg">не</span> студе́нт,
     <span class="pe-hl pe-hl--adv">а</span> учи́тель.</p>
  <p class="pe-ex__uz">U talaba emas, balki oʻqituvchi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Э́то <span class="pe-hl pe-hl--neg">не</span> моя́ кни́га,
     <span class="pe-hl pe-hl--adv">а</span> её.</p>
  <p class="pe-ex__uz">Bu mening kitobim emas, balki uniki.</p>
  <p class="pe-ex__why">Ikkinchi qismda otni takrorlash shart emas — <b>её</b>
     oʻzi yetadi.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>А</b> va <b>но</b> — ikkalasi ham “lekin” deb tarjima qilinadi, lekin ular
boshqa ish qiladi. <b>А</b> — <em>solishtirish va tuzatish</em>: “bu emas, balki
u”. <b>Но</b> — <em>kutilmagan qarshilik</em>: “lekin baribir”. Solishtiring:<br>
<em>Он не студе́нт, <b>а</b> учи́тель.</em> — tuzatish.<br>
<em>Шко́ла но́вая, <b>но</b> ма́ленькая.</em> — qarshilik.</div>

<h3>4. Ни — inkorni kuchaytiradi</h3>

<p>Toʻrtinchi soʻz. <b>Ни</b> yolgʻiz ishlamaydi — u <b>ни … ни …</b> juftligida
keladi va “na … na …” degani:</p>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--neg">Ни</span> э́то,
     <span class="pe-hl pe-hl--neg">ни</span> то.</p>
  <p class="pe-ex__uz">Na bu, na anavi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Здесь <span class="pe-hl pe-hl--neg">ни</span> шко́лы,
     <span class="pe-hl pe-hl--neg">ни</span> библиоте́ки.</p>
  <p class="pe-ex__uz">Bu yerda na maktab, na kutubxona bor.</p>
  <p class="pe-ex__why">Bu qurilmada ot shaklini oʻzgartirdi
     (<em>шко́ла → шко́лы</em>) — bu <b>родительный падеж</b>, PR-34 da
     oʻrganamiz. Hozircha qolipni tanib qoʻying.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu ham tayyor bilim: oʻzbekcha <b>na … na …</b> ruscha <b>ни … ни …</b> bilan
aynan bir xil ishlaydi — <em>na bu, na u</em> = <b>ни э́то, ни то</b>. Ikkala
tilda ham juftlik takrorlanadi va ikkala qismni birdan inkor qiladi. Tarjima
qilishda hech nima oʻzgartirish kerak emas.</div>

<h3>5. Да — va bitta ogohlantirish</h3>

<p><b>Да</b> — “ha”. Lekin u har doim ham tasdiq emas: suhbatda ruslar uni
“eshityapman, davom eting” maʼnosida ham ishlatadi, xuddi oʻzbekchadagi
<em>“ha-ha”</em> kabi.</p>

<div class="pe-ex">
  <p class="pe-ex__ru">— Э́то <span class="pe-hl pe-hl--neg">не</span> твоя́ ру́чка?<br>
     — <span class="pe-hl pe-hl--neg">Нет</span>, не моя́.</p>
  <p class="pe-ex__uz">— Bu sening ruchkang emasmi?<br>— Yoʻq, meniki emas.</p>
  <p class="pe-ex__why">Inkor savolga javob berishda rus va oʻzbek tillari
     <b>bir xil</b> ishlaydi: “yoʻq” degani “yoʻq, emas”. Ingliz tilida bu joy
     chalkash, sizda esa chalkash emas.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то шко́ла не.</s></p>
  <p class="pe-good">Э́то <b>не</b> шко́ла. — <b>не</b> soʻzning oldida turadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то нет шко́ла.</s></p>
  <p class="pe-good">Э́то <b>не</b> шко́ла. — gap ichida <b>не</b>, <b>нет</b> emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он не студе́нт, но учи́тель.</s></p>
  <p class="pe-good">Он не студе́нт, <b>а</b> учи́тель. — tuzatishda <b>а</b>, <b>но</b> emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ни э́то.</s> (yolgʻiz)</p>
  <p class="pe-good"><b>Ни</b> э́то, <b>ни</b> то. — <b>ни</b> juftlikda ishlaydi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Э́то ___ мой телефо́н.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>не</strong>. Gap ichida, soʻzning oldida —
    <b>не</b>. <b>Нет</b> esa javob sifatida gap boshida turadi:
    <em>Нет, э́то не мой телефо́н.</em></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Ikki gapning farqi nima?<br>
     <b>Не я здесь.</b> — <b>Я не здесь.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Не я здесь</strong> = “shu yerda men
    emasman (boshqa odam)”. <strong>Я не здесь</strong> = “men shu yerda emasman
    (boshqa joydaman)”. <b>Не</b> qayerda tursa, oʻshani inkor qiladi — shuning
    uchun uning joyi maʼnoni boshqaradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Он не врач, ___ учи́тель.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>а</strong>. Bu <b>«не X, а Y»</b>
    qurilmasi — tuzatish. <b>Но</b> bu yerda notoʻgʻri, chunki u qarshilik
    bildiradi: <em>Он врач, но молодо́й</em> — “u shifokor, lekin yosh”.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Oʻzbekchaga oʻgiring: <b>Ни э́то, ни то.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Na bu, na anavi.</strong> Ruscha
    <b>ни … ни …</b> va oʻzbekcha <b>na … na …</b> aynan bir xil ishlaydi —
    ikkalasi ham juftlikda keladi va ikkala qismni inkor qiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gapda xato bor?<br>
     а) Нет, э́то не дом. &nbsp; б) Дом не большо́й.<br>
     в) Э́то не моя́ кни́га, а её. &nbsp; г) Э́то кни́га не.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>г)</strong>. <b>Не</b> gap oxiriga
    qoʻyilmaydi — bu oʻzbekcha <em>emas</em> ning taʼsiri. Toʻgʻrisi:
    <b>Э́то не кни́га.</b></p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>да</b><span>ha</span></li>
  <li><b>нет</b><span>yoʻq (javob); yoʻq (mavjud emas)</span></li>
  <li><b>не</b><span>emas (soʻz oldida)</span></li>
  <li><b>ни … ни …</b><span>na … na …</span></li>
  <li><b>а</b><span>balki, esa (tuzatish)</span></li>
  <li><b>но</b><span>lekin (qarshilik)</span></li>
  <li><b>библиоте́ка</b><span>kutubxona</span></li>
  <li><b>спаси́бо, нет</b><span>yoʻq, rahmat</span></li>
  <li><b>коне́чно</b><span>albatta</span></li>
  <li><b>то́же</b><span>ham</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Нет</b> — javob (“yoʻq”) va yoʻqlik. Oʻzi turadi, odatda gap boshida.</li>
    <li><b>Не</b> — bitta soʻzni inkor qiladi va uning <b>oldida</b> turadi.
        Hech qachon gap oxirida emas.</li>
    <li><b>Не</b> qayerda tursa — oʻshani inkor qiladi: <em>Не я здесь</em> ≠
        <em>Я не здесь</em>.</li>
    <li><b>«Не X, а Y»</b> — tuzatish qurilmasi. <b>А</b> tuzatadi, <b>но</b>
        qarshilik bildiradi.</li>
    <li><b>Ни … ни …</b> = oʻzbekcha <b>na … na …</b>, juftlikda ishlaydi.</li>
  </ul>
</div>
""",
    },
]
