# -*- coding: utf-8 -*-
"""Prime Russian — Block D davomi (41–43).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-29…40 da oltita kelishik otlarga qoʻllandi. PR-41 dan boshlab OʻSHA
tizim boshqa soʻz turkumlariga koʻchadi — yangi tizim emas, yangi
qoʻshimchalar.

PR-41 — olmoshlar. Bu YIGʻUVCHI dars: oʻquvchi bu shakllarni bittalab
uchratgan (меня́ PR-32, мне PR-27, обо мне PR-31, мной PR-39). Bugun ular
bitta jadvalda.
PR-42 — egalik olmoshlari. Eng katta yangilik: его́ / её / их UMUMAN
turlanmaydi.
PR-43 — sifatlar boshlanadi. Bu yerda oʻzbekcha YORDAM BERMAYDI: oʻzbek
sifati hech qachon oʻzgarmaydi. Buni ochiq aytish kerak.

Mashqlar:        practice/management/commands/_practice_pr_41_43.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_41_43.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_41_43.py --author=prime
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
        "title": "PR-41: Olmoshlarning turlanishi: меня, мне, мной, обо мне",
        "category": "russian",
        "order": 41,
        "summary": (
            "Yangi hech narsa yoʻq — siz bu shakllarning hammasini allaqachon "
            "ishlatgansiz. Bugun ular bitta jadvalga yigʻiladi va nihoyat tizim "
            "koʻrinadi."
        ),
        "stories": ["Она́ мне не позвони́ла"],
        "content": """
<h2>PR-41: Olmoshlarning turlanishi: меня, мне, мной, обо мне</h2>

<p>Bu dars <b>yigʻuvchi</b> dars. Unda bitta ham yangi shakl yoʻq — siz
ularning hammasini oʻn ikki dars davomida bittalab uchratgansiz:
<em>меня́</em> (PR-32), <em>мне</em> (PR-27), <em>обо мне</em> (PR-31),
<em>мной</em> (PR-39), <em>у меня́</em> (PR-14). Bugun ular <b>bitta
jadvalda</b> turadi — va shundan keyin siz tizimni koʻrasiz, alohida
soʻzlarni emas.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Butun olmosh jadvalini bir joyda koʻrasiz</li>
    <li>Uchta yengillikni topasiz — yodlanadigan narsa kam</li>
    <li><b>Н</b> qoidasini toʻliq bilib olasiz</li>
    <li>Oʻzbekcha olmoshlar bilan yonma-yon qoʻyasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta olmosh, oltita shakl</span>
  <span class="pe-chip pe-chip--s">я</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">меня́ · мне · меня́ · мной · обо мне</span>
</div>

<h3>1. Butun jadval</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kelishik</th><th>я</th><th>ты</th><th>он / оно́</th><th>она́</th></tr>
  <tr><td class="pr-uz">Имени́тельный</td><td class="pr-res">я</td>
      <td class="pr-res">ты</td><td class="pr-res">он</td><td class="pr-res">она́</td></tr>
  <tr><td class="pr-uz">Роди́тельный</td><td class="pr-end">меня́</td>
      <td class="pr-end">тебя́</td><td class="pr-end">его́</td><td class="pr-end">её</td></tr>
  <tr><td class="pr-uz">Да́тельный</td><td class="pr-end">мне</td>
      <td class="pr-end">тебе́</td><td class="pr-end">ему́</td><td class="pr-end">ей</td></tr>
  <tr><td class="pr-uz">Вини́тельный</td><td class="pr-end">меня́</td>
      <td class="pr-end">тебя́</td><td class="pr-end">его́</td><td class="pr-end">её</td></tr>
  <tr><td class="pr-uz">Твори́тельный</td><td class="pr-end">мной</td>
      <td class="pr-end">тобо́й</td><td class="pr-end">им</td><td class="pr-end">ей</td></tr>
  <tr><td class="pr-uz">Предло́жный</td><td class="pr-end">обо мне</td>
      <td class="pr-end">о тебе́</td><td class="pr-end">о нём</td><td class="pr-end">о ней</td></tr>
</table></div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kelishik</th><th>мы</th><th>вы</th><th>они́</th></tr>
  <tr><td class="pr-uz">Имени́тельный</td><td class="pr-res">мы</td>
      <td class="pr-res">вы</td><td class="pr-res">они́</td></tr>
  <tr><td class="pr-uz">Роди́тельный</td><td class="pr-end">нас</td>
      <td class="pr-end">вас</td><td class="pr-end">их</td></tr>
  <tr><td class="pr-uz">Да́тельный</td><td class="pr-end">нам</td>
      <td class="pr-end">вам</td><td class="pr-end">им</td></tr>
  <tr><td class="pr-uz">Вини́тельный</td><td class="pr-end">нас</td>
      <td class="pr-end">вас</td><td class="pr-end">их</td></tr>
  <tr><td class="pr-uz">Твори́тельный</td><td class="pr-end">на́ми</td>
      <td class="pr-end">ва́ми</td><td class="pr-end">и́ми</td></tr>
  <tr><td class="pr-uz">Предло́жный</td><td class="pr-end">о нас</td>
      <td class="pr-end">о вас</td><td class="pr-end">о них</td></tr>
</table></div>

<h3>2. Uchta yengillik</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Р.п. = В.п.</p>
    <p><b>Har doim</b>: <em>меня́ / меня́</em>, <em>тебя́ / тебя́</em>,
       <em>его́ / его́</em>, <em>нас / нас</em>.<br>
       Bu jonli otlardagi qoidaning oʻzi (PR-32) — olmoshlar ham «jonli».
       Demak oltita emas, <b>beshta</b> shakl.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Мы va вы juda oson</p>
    <p><em>нас · нам · нас · на́ми · о нас</em><br>
       Faqat <b>toʻrtta</b> boshqa shakl, va ular bir-biriga oʻxshaydi.
       <em>Вы</em> ham xuddi shunday: <em>вас, вам, ва́ми</em>.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Она́ da «ей» ikki marta</p>
    <p><em>ей</em> — ham Да́тельный, ham Твори́тельный.<br>
       <em>Дать <b>ей</b></em> · <em>с <b>ней</b></em>.<br>
       Farqni gap va predlog koʻrsatadi.</p></div>
</div>

<h3>3. Н qoidasi — toʻliq</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Predlogdan keyin</b> <em>он / она́ / они́</em> olmoshlari <b>Н</b> bilan
boshlanadi:<br>
<em>его́ → у <b>н</b>его́</em> · <em>ему́ → к <b>н</b>ему́</em> ·
<em>её → без <b>н</b>её</em> · <em>ей → с <b>н</b>ей</em> ·
<em>их → о́коло <b>н</b>их</em> · <em>и́ми → с <b>н</b>и́ми</em><br>
Predlogsiz esa Н <b>yoʻq</b>: <em>его́ нет, я ви́жу их, дай ему́</em>.<br>
Bu qoida faqat uchinchi shaxsga tegishli. <em>Меня́, тебя́, нас, вас</em>
hech qachon oʻzgarmaydi.</div>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Predlogsiz — Н yoʻq</p>
    <p><em><b>Его́</b> нет до́ма.</em><br>
       <em>Я ви́жу <b>её</b>.</em><br>
       <em>Дай <b>им</b> кни́гу.</em></p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Predlog bilan — Н bor</p>
    <p><em>У <b>н</b>его́ есть брат.</em><br>
       <em>Я ду́маю о <b>н</b>ей.</em><br>
       <em>Мы идём с <b>н</b>и́ми.</em></p>
  </div>
</div>

<h3>4. Uchta predlog unli oladi</h3>

<p>Bu ham tanish — siz uni uch marta koʻrgansiz. Endi uchtasi birga:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Predlog</th><th>Odatda</th><th>Bu olmosh bilan</th><th>Qayerda koʻrgansiz</th></tr>
  <tr><td class="pr-res">о</td><td class="pr-uz">о кни́ге</td>
      <td class="pr-end">обо мне</td><td class="pr-uz">PR-31</td></tr>
  <tr><td class="pr-res">к</td><td class="pr-uz">к бра́ту</td>
      <td class="pr-end">ко мне</td><td class="pr-uz">PR-38</td></tr>
  <tr><td class="pr-res">с</td><td class="pr-uz">с бра́том</td>
      <td class="pr-end">со мной</td><td class="pr-uz">PR-39</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu dars siz uchun eng oson darslardan biri boʻlishi kerak — chunki
<b>oʻzbekcha olmoshlar ham aynan shunday turlanadi</b>:<br><br>
<em>men</em> · <em>men<b>ing</b></em> · <em>men<b>ga</b></em> ·
<em>men<b>i</b></em> · <em>men<b>da</b></em> · <em>men<b>dan</b></em><br>
<em>я</em> · <em>меня́</em> · <em>мне</em> · <em>меня́</em> ·
<em>обо мне</em> · <em>от меня́</em><br><br>
Oltita shakl — oltita shakl. Tushuncha bir xil, tartib bir xil, ish bir
xil. Faqat ruscha shakllar <b>bir-biriga oʻxshamaydi</b>
(<em>я → меня́ → мне → мной</em>), oʻzbekchada esa oʻzak turibdi va faqat
qoʻshimcha almashadi (<em>men-ing, men-ga, men-i</em>).<br><br>
Yaʼni bu yerda qiyinchilik <b>tushunishda emas, yodlashda</b>. Va yodlash
uchun eng yaxshi yoʻl — jadvalni emas, <b>iboralarni</b> yodlash:
<em>у меня́ есть</em>, <em>мне на́до</em>, <em>я ду́маю о тебе́</em>,
<em>пойдём со мной</em>. Siz allaqachon shunday qilgansiz.</div>

<h3>5. Amalda</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">— Ты зна́ешь <span class="pe-hl pe-hl--o">его́</span>?<br>
     — Да. У <span class="pe-hl pe-hl--o">него́</span> есть маши́на. Я
     ча́сто говорю́ <span class="pe-hl pe-hl--o">с ним</span>.</p>
  <p class="pe-ex__uz">— Uni tanaysanmi?<br>— Ha. Uning mashinasi bor. Men u
     bilan tez-tez gaplashaman.</p>
  <p class="pe-ex__why">Bitta odam, uchta shakl: <em>его́</em>
     (predlogsiz), <em>него́</em> (predlog bilan), <em>ним</em>
     (Твори́тельный, predlog bilan).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--o">Мне</span> гру́стно.
     Она́ не звони́ла <span class="pe-hl pe-hl--o">мне</span>. Я ду́мал
     <span class="pe-hl pe-hl--o">о ней</span> весь ве́чер.</p>
  <p class="pe-ex__uz">Menga gʻamgin. U menga qoʻngʻiroq qilmadi. Butun
     kechqurun u haqida oʻyladim.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>У его́ есть брат.</s></p>
  <p class="pe-good">У <b>него́</b> есть брат — predlogdan keyin Н</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ви́жу него́.</s></p>
  <p class="pe-good">Я ви́жу <b>его́</b> — predlog yoʻq, demak Н ham yoʻq</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Пойдём с мной.</s></p>
  <p class="pe-good">Пойдём <b>со мной</b> — predlogga unli qoʻshiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он ду́мает о мне.</s></p>
  <p class="pe-good">Он ду́мает <b>обо мне</b> — oʻsha qoida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я жду он.</s></p>
  <p class="pe-good">Я жду <b>его́</b> — olmosh ham kelishikka kiradi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>У ___ есть соба́ка.</b> (она́)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>неё</strong>. <em>У</em> —
    predlog, demak <b>Н</b> qoʻshiladi: <em>её → неё</em>. Predlogsiz
    boʻlganda <em>её</em> qolardi: <em>я ви́жу её</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Nega <b>меня́</b> ikkita kelishikda bir xil?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki olmoshlarda
    <strong>Роди́тельный = Вини́тельный</strong> — har doim. Bu jonli
    otlardagi qoidaning oʻsha oʻzi (PR-32). Shuning uchun oltita emas,
    beshta shakl yodlanadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Мы идём ___.</b> («ular bilan» maʼnosida)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>с ни́ми</strong>. Твори́тельный
    shakli <em>и́ми</em>, va predlogdan keyin <b>Н</b> qoʻshiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu uchta shakl bitta olmoshdan. Qaysi olmosh?<br>
     <b>ей · её · о ней</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>она́</strong>. <em>Её</em> —
    Роди́тельный va Вини́тельный; <em>ей</em> — Да́тельный va
    Твори́тельный; <em>о ней</em> — Предло́жный. Bu olmoshda ikkita
    shakl ikki martadan ishlatiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Я ду́маю о нём. &nbsp; б) У его́ есть маши́на.<br>
     в) Дай им кни́гу. &nbsp; г) Пойдём со мной.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б)</strong>. Toʻgʻrisi —
    <b>У него́ есть маши́на</b>. Predlogdan keyin Н qoʻshiladi. Qolgan
    uchtasi toʻgʻri: <em>о нём</em> (predlog bor — Н bor), <em>им</em>
    (predlog yoʻq — Н yoʻq), <em>со мной</em> (unli
    qoʻshilgan).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>меня́ / мне / мной</b><span>meni / menga / men bilan</span></li>
  <li><b>тебя́ / тебе́ / тобо́й</b><span>seni / senga / sen bilan</span></li>
  <li><b>его́ / ему́ / им</b><span>uni / unga / u bilan</span></li>
  <li><b>её / ей</b><span>uni / unga (ayol)</span></li>
  <li><b>нас / нам / на́ми</b><span>bizni / bizga / biz bilan</span></li>
  <li><b>их / им / и́ми</b><span>ularni / ularga / ular bilan</span></li>
  <li><b>у него́</b><span>unda</span></li>
  <li><b>со мной</b><span>men bilan</span></li>
  <li><b>звони́ть</b><span>qoʻngʻiroq qilmoq</span></li>
  <li><b>бата́рея</b><span>batareya</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Yangi shakl yoʻq — hammasini allaqachon ishlatgansiz.</li>
    <li><b>Р.п. = В.п.</b> har doim: <em>меня́, тебя́, его́, нас</em>.</li>
    <li><b>Predlogdan keyin Н</b> — faqat <em>он / она́ / они́</em> da:
        <em>у него́, о ней, с ни́ми</em>.</li>
    <li>Predlogsiz Н yoʻq: <em>его́ нет, я ви́жу её</em>.</li>
    <li><b>Обо мне, ко мне, со мной</b> — uchta predlog unli oladi.</li>
    <li>Oʻzbekcha olmoshlar ham oltita shaklda turlanadi — tushuncha bir
        xil, faqat ruscha shakllar bir-biriga oʻxshamaydi.</li>
    <li>Jadvalni emas, <b>iboralarni</b> yodlang: <em>у меня́ есть, мне
        на́до, о тебе́, со мной</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-42: Egalik olmoshlarining turlanishi: моего, моей, моим, о моём",
        "category": "russian",
        "order": 42,
        "summary": (
            "Мой, твой, наш, ваш — sifat kabi turlanadi. Va bitta katta yengillik "
            "bor: его́, её, их umuman oʻzgarmaydi, hech qachon, hech qanday "
            "kelishikda."
        ),
        "stories": ["В на́шем дворе́"],
        "content": """
<h2>PR-42: Egalik olmoshlarining turlanishi: моего, моей, моим, о моём</h2>

<p>PR-10 da siz <em>мой, моя́, моё, мои́</em> ni oʻrgandingiz — lekin faqat
bosh kelishikda. Endi ular kelishiklarga kiradi. Yaxshi xabar ikkita:
birinchidan, ular <b>sifat kabi</b> turlanadi, yaʼni keyingi dars uchun
tayyorgarlik boʻladi. Ikkinchidan — va bu ancha yoqimliroq — uchtasi
<b>umuman turlanmaydi</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Мой</b> ni oltita kelishikda turlaysiz</li>
    <li><b>Наш</b> va <b>ваш</b> ning naqshini bilasiz</li>
    <li><b>Его́, её, их</b> hech qachon oʻzgarmasligini oʻrganasiz</li>
    <li><b>-ОГО</b> ning [ово] boʻlib oʻqilishini eslab qolasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Turlanadi ↔ turlanmaydi</span>
  <span class="pe-chip pe-chip--v">мой → моего́</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">его́ → его́</span>
</div>

<h3>1. Мой — toʻliq jadval</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kelishik</th><th>erkak</th><th>ayol</th><th>oʻrta</th><th>koʻplik</th></tr>
  <tr><td class="pr-uz">Имени́тельный</td><td class="pr-res">мой</td>
      <td class="pr-res">моя́</td><td class="pr-res">моё</td><td class="pr-res">мои́</td></tr>
  <tr><td class="pr-uz">Роди́тельный</td><td class="pr-end">моего́</td>
      <td class="pr-end">мое́й</td><td class="pr-end">моего́</td><td class="pr-end">мои́х</td></tr>
  <tr><td class="pr-uz">Да́тельный</td><td class="pr-end">моему́</td>
      <td class="pr-end">мое́й</td><td class="pr-end">моему́</td><td class="pr-end">мои́м</td></tr>
  <tr><td class="pr-uz">Вини́тельный</td><td class="pr-end">мой / моего́</td>
      <td class="pr-end">мою́</td><td class="pr-end">моё</td><td class="pr-end">мои́ / мои́х</td></tr>
  <tr><td class="pr-uz">Твори́тельный</td><td class="pr-end">мои́м</td>
      <td class="pr-end">мое́й</td><td class="pr-end">мои́м</td><td class="pr-end">мои́ми</td></tr>
  <tr><td class="pr-uz">Предло́жный</td><td class="pr-end">о моём</td>
      <td class="pr-end">о мое́й</td><td class="pr-end">о моём</td><td class="pr-end">о мои́х</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Jadval katta koʻrinadi, lekin unda <b>takrorlanish juda koʻp</b>:<br>
1. <b>Erkak va oʻrta jins</b> deyarli bir xil — farq faqat bosh kelishikda
va Вини́тельный'da.<br>
2. <b>Ayol jinsida</b> deyarli hamma joyda <em>мое́й</em> — toʻrtta
kelishikda bitta shakl! Faqat <em>моя́</em> va <em>мою́</em>
boshqacha.<br>
3. <b>Вини́тельный</b> yangi shakl <b>yaratmaydi</b> — u yo bosh
kelishikni, yo Роди́тельный'ni takrorlaydi (jonlilikka qarab, PR-32).<br>
Yaʼni yodlanadigan haqiqiy shakllar: <em>моего́, моему́, мои́м, о моём,
мое́й, мою́, мои́х, мои́ми</em>.</div>

<div class="pr-say">
  <span class="pr-say__from">моего́</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[маиво́]</span>
  <span class="pr-say__why">-ОГО har doim [ово] — <em>его́</em> dagi qoida (PR-32)</span>
</div>

<h3>2. Твой, наш, ваш</h3>

<p><b>Твой</b> aynan <em>мой</em> kabi turlanadi — bitta harf almashadi:
<em>твоего́, твоему́, твои́м, о твоём, твое́й, твою́</em>.</p>

<p><b>Наш</b> va <b>ваш</b> biroz boshqacha, lekin ular ham bir-biriga
oʻxshaydi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kelishik</th><th>erkak / oʻrta</th><th>ayol</th><th>koʻplik</th></tr>
  <tr><td class="pr-uz">Имени́тельный</td><td class="pr-res">наш / на́ше</td>
      <td class="pr-res">на́ша</td><td class="pr-res">на́ши</td></tr>
  <tr><td class="pr-uz">Роди́тельный</td><td class="pr-end">на́шего</td>
      <td class="pr-end">на́шей</td><td class="pr-end">на́ших</td></tr>
  <tr><td class="pr-uz">Да́тельный</td><td class="pr-end">на́шему</td>
      <td class="pr-end">на́шей</td><td class="pr-end">на́шим</td></tr>
  <tr><td class="pr-uz">Вини́тельный</td><td class="pr-end">наш / на́ше</td>
      <td class="pr-end">на́шу</td><td class="pr-end">на́ши</td></tr>
  <tr><td class="pr-uz">Твори́тельный</td><td class="pr-end">на́шим</td>
      <td class="pr-end">на́шей</td><td class="pr-end">на́шими</td></tr>
  <tr><td class="pr-uz">Предло́жный</td><td class="pr-end">о на́шем</td>
      <td class="pr-end">о на́шей</td><td class="pr-end">о на́ших</td></tr>
</table></div>

<h3>3. Его́, её, их — bular turlanmaydi</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Его́, её, их</b> egalik maʼnosida <b>hech qachon oʻzgarmaydi</b> — hech
qanday kelishikda, hech qanday jinsda, hech qanday sonda:<br>
<em><b>его́</b> дом</em> · <em>в <b>его́</b> до́ме</em> · <em>с <b>его́</b>
бра́том</em> · <em>о <b>его́</b> семье́</em><br>
<em><b>её</b> кни́га</em> · <em>без <b>её</b> кни́ги</em><br>
<em><b>их</b> дети</em> · <em>о <b>их</b> де́тях</em><br>
Va diqqat: bu yerda <b>Н qoʻshilmaydi</b>! <em>«У него́ есть»</em> —
olmosh; <em>«его́ дом»</em> — egalik. Ikkinchisida predlogdan keyin ham
<em>его́</em> qoladi.</div>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Olmosh — Н oladi</p>
    <p><em>У <b>н</b>его́ есть дом.</em><br>Uning uyi bor.</p>
    <p>Bu yerda <em>его́</em> — «u» degani, olmosh.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Egalik — Н olmaydi</p>
    <p><em>Я был в <b>его́</b> до́ме.</em><br>Men uning uyida edim.</p>
    <p>Bu yerda <em>его́</em> — «uning» degani, egalik.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbek tilida egalik <b>otning oʻzida</b> koʻrsatiladi — qoʻshimcha
bilan:<br>
<em>kitob<b>im</b></em> · <em>kitob<b>ing</b></em> · <em>kitob<b>i</b></em>
· <em>kitob<b>imiz</b></em><br>
Va kelishik qoʻshimchasi <b>undan keyin</b> keladi:
<em>kitob-im-<b>ni</b></em>, <em>kitob-im-<b>ga</b></em>. Yaʼni bitta soʻz,
ikkita qoʻshimcha.<br><br>
Ruschada esa <b>ikkita alohida soʻz</b> bor va <b>ikkalasi ham</b>
oʻzgaradi: <em>мо<b>его́</b> бра́т<b>а</b></em>. Bu koʻproq ish, lekin
mantiq oddiy — <b>egalik olmoshi otga qanday moslashsa, shunday
oʻzgaradi</b>.<br><br>
Va bitta yaxshi xabar: oʻzbekchada <em>-i</em> (uning) hech qachon
oʻzgarmaydi — <em>kitobi, kitobini, kitobiga</em>. Ruschada ham xuddi
shunday: <b>его́, её, их</b> hech qachon oʻzgarmaydi. Bu yerda ikkala til
bir xil ish qilyapti.</div>

<h3>4. Amalda</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">Э́то дом <span class="pe-hl pe-hl--o">моего́
     бра́та</span>. В <span class="pe-hl pe-hl--adv">на́шем дворе́</span>
     есть де́рево.</p>
  <p class="pe-ex__uz">Bu akamning uyi. Bizning hovlimizda daraxt bor.</p>
  <p class="pe-ex__why">Ikkala iborada ham <b>ikkita soʻz birga
     oʻzgargan</b>: <em>моего́ бра́та</em> (Роди́тельный),
     <em>на́шем дворе́</em> (Предло́жный).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Я говорю́ <span class="pe-hl pe-hl--o">с мои́м
     дру́гом</span> о <span class="pe-hl pe-hl--o">его́ рабо́те</span>.</p>
  <p class="pe-ex__uz">Doʻstim bilan uning ishi haqida gaplashyapman.</p>
  <p class="pe-ex__why"><em>Мои́м</em> oʻzgardi (Твори́тельный), lekin
     <em>его́</em> oʻzgarmadi — u hech qachon oʻzgarmaydi. Ot esa
     oʻzgardi: <em>рабо́т<b>е</b></em>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то дом мой бра́та.</s></p>
  <p class="pe-good">Э́то дом <b>моего́</b> бра́та — egalik olmoshi ham kelishikka kiradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>В наш дворе́ есть де́рево.</s></p>
  <p class="pe-good">В <b>на́шем</b> дворе́ — ot bilan birga oʻzgaradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я был в него́ до́ме.</s></p>
  <p class="pe-good">Я был в <b>его́</b> до́ме — egalik maʼnosida Н qoʻshilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ви́жу его́ до́ма.</s> <em>(«uning uyini» maʼnosida)</em></p>
  <p class="pe-good">Я ви́жу <b>его́ дом</b> — <em>дом</em> jonsiz, demak oʻzgarmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ду́маю о мой брат.</s></p>
  <p class="pe-good">Я ду́маю <b>о моём бра́те</b> — ikkala soʻz ham oʻzgaradi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Э́то кни́га ___ сестры́.</b> (моя́)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>мое́й</strong>. <em>Сестры́</em> —
    Роди́тельный, demak egalik olmoshi ham Роди́тельный'da. Ayol jinsida bu
    shakl toʻrtta kelishikda ishlatiladi: <em>мое́й</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>В ___ дворе́ игра́ют де́ти.</b> (наш)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>на́шем</strong>. <em>Во дворе́</em>
    — Предло́жный, demak egalik olmoshi ham: <em>на́шем</em>. Ikkala soʻz
    birga oʻzgaradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Я был в ___ до́ме.</b> (его́)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>его́</strong> — oʻzgarmaydi!
    <em>Его́, её, их</em> egalik maʼnosida hech qachon turlanmaydi va
    predlogdan keyin Н ham olmaydi. Faqat ot oʻzgardi:
    <em>до́м<b>е</b></em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>моего́</b> qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[маиво́]</strong>. <b>-ОГО</b>
    birikmasi har doim <b>[ово]</b> boʻlib oʻqiladi — <em>его́</em>
    [йиво́] dagi qoidaning oʻsha oʻzi (PR-32). Bu keyingi darsda
    sifatlarda ham uchraydi: <em>но́вого</em> [но́вава].</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Э́то дом моего́ бра́та. &nbsp; б) В на́шем дворе́ ти́хо.<br>
     в) Я был в него́ до́ме. &nbsp; г) Я говорю́ с мои́м дру́гом.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>в его́ до́ме</b>. <em>Его́</em> bu yerda egalik («uning»), demak Н
    qoʻshilmaydi. <em>У него́</em> boshqa narsa — u yerda <em>его́</em>
    olmosh («u»).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>моего́ / мое́й</b><span>mening (turlangan)</span></li>
  <li><b>на́шего / на́шем</b><span>bizning (turlangan)</span></li>
  <li><b>его́ / её / их</b><span>uning / ularning — oʻzgarmaydi</span></li>
  <li><b>двор</b><span>hovli</span></li>
  <li><b>сосе́д</b><span>qoʻshni</span></li>
  <li><b>подъе́зд</b><span>podyezd, kirish</span></li>
  <li><b>де́рево</b><span>daraxt</span></li>
  <li><b>го́лос</b><span>ovoz</span></li>
  <li><b>семья́</b><span>oila</span></li>
  <li><b>де́ти</b><span>bolalar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Мой, твой, наш, ваш</b> sifat kabi turlanadi va ot bilan
        <b>birga</b> oʻzgaradi.</li>
    <li>Ayol jinsida <b>мое́й</b> toʻrtta kelishikda ishlatiladi — yodlash
        oson.</li>
    <li>Erkak va oʻrta jins deyarli bir xil.</li>
    <li><b>Его́, её, их</b> — <b>hech qachon</b> oʻzgarmaydi va Н
        olmaydi.</li>
    <li>Farqni ajrating: <em>у <b>н</b>его́</em> (olmosh) va <em>в
        <b>его́</b> до́ме</em> (egalik).</li>
    <li><b>-ОГО → [ово]</b>: <em>моего́</em> [маиво́].</li>
    <li>Oʻzbekchada egalik qoʻshimcha bilan (<em>kitobim</em>), ruschada
        alohida soʻz bilan — lekin <em>-i</em> va <em>его́</em> ikkalasi
        ham oʻzgarmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-43: Sifatlarning turlanishi 1 — Родительный va Винительный",
        "category": "russian",
        "order": 43,
        "summary": (
            "Sifat otga jins va son boʻyicha moslashardi (PR-12). Endi u kelishik "
            "boʻyicha ham moslashadi. Bu yerda oʻzbekcha yordam bermaydi — lekin "
            "qoida mexanik va istisnosiz."
        ),
        "stories": ["Ста́рого моста́ бо́льше нет"],
        "content": """
<h2>PR-43: Sifatlarning turlanishi 1 — Родительный va Винительный</h2>

<p>PR-12 da siz sifatning otga moslashishini oʻrgandingiz:
<em>но́в<b>ый</b> дом, но́в<b>ая</b> кни́га, но́в<b>ое</b> окно́</em>.
Oʻshanda gap faqat bosh kelishik haqida edi. Endi ot kelishikka kiradi —
va sifat <b>u bilan birga</b> kiradi. Bugun ikkita kelishikni olamiz:
Роди́тельный va Вини́тельный.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Sifatning Роди́тельный shaklini yasaysiz: <b>но́вого до́ма</b></li>
    <li>Вини́тельный'da jonlilik sifatga ham taʼsir qilishini koʻrasiz</li>
    <li><b>-ОГО</b> ning <b>[ово]</b> boʻlib oʻqilishini bilasiz</li>
    <li>Imlo qoidasini eslaysiz: Г, К, Х, Ж, Ш, Щ, Ч dan keyin <b>-И</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Sifat otga ergashadi</span>
  <span class="pe-chip pe-chip--s">но́вый дом</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">но́в<b>ого</b> до́м<b>а</b></span>
</div>

<h3>1. Роди́тельный</h3>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">-<span class="pr-end">ого</span></p>
    <p><em>но́вый дом → но́в<b>ого</b> до́ма</em><br>
       <em>ста́рый мост → ста́р<b>ого</b> моста́</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний — oʻrta</p>
    <p class="pr-gender__form">-<span class="pr-end">ого</span></p>
    <p><em>но́вое окно́ → но́в<b>ого</b> окна́</em><br>
       Erkak jins bilan <b>bir xil</b>.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">-<span class="pr-end">ой</span></p>
    <p><em>но́вая кни́га → но́в<b>ой</b> кни́ги</em><br>
       <em>ста́рая шко́ла → ста́р<b>ой</b> шко́лы</em></p>
  </div>
</div>

<p>Koʻplikda esa jins yoʻqoladi va bitta shakl qoladi: <b>-ЫХ / -ИХ</b> —
<em>но́в<b>ых</b> домо́в</em>, <em>ста́р<b>ых</b> книг</em>.</p>

<div class="pr-say">
  <span class="pr-say__from">но́вого</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[но́вава]</span>
  <span class="pr-say__why">-ОГО har doim [ово] — <em>его́</em>, <em>моего́</em> dagi qoida</span>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Imlo qoidasi bu yerda ham ishlaydi (PR-4): <b>Г, К, Х, Ж, Ш, Щ, Ч</b> dan
keyin <b>Ы yozilmaydi</b>:<br>
<em>ру́сский → ру́сск<b>их</b></em> (<em>«ру́сскых»</em> emas)<br>
<em>хоро́ший → хоро́ш<b>их</b></em> · <em>большо́й → больш<b>и́х</b></em><br>
Xuddi shu qoida <em>кни́га → кни́ги</em> (PR-34) da ham ishlagan edi. U
kelishiklarda qayta-qayta uchraydi.</div>

<h3>2. Вини́тельный — jonlilik sifatga ham tegadi</h3>

<p>PR-32 dagi qoida endi ikkita soʻzga birdan qoʻllanadi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Nima</th><th>Bosh kelishik</th><th>Вини́тельный</th><th>Nega</th></tr>
  <tr><td class="pr-uz">erkak, jonsiz</td><td class="pr-res">но́вый дом</td>
      <td class="pr-end">но́вый дом</td><td class="pr-uz">oʻzgarmaydi</td></tr>
  <tr><td class="pr-uz">erkak, jonli</td><td class="pr-res">но́вый учи́тель</td>
      <td class="pr-end">но́вого учи́теля</td><td class="pr-uz">Роди́тельный shakli</td></tr>
  <tr><td class="pr-uz">ayol</td><td class="pr-res">но́вая кни́га</td>
      <td class="pr-end">но́вую кни́гу</td><td class="pr-uz">har doim -УЮ</td></tr>
  <tr><td class="pr-uz">oʻrta</td><td class="pr-res">но́вое окно́</td>
      <td class="pr-end">но́вое окно́</td><td class="pr-uz">hech qachon oʻzgarmaydi</td></tr>
  <tr><td class="pr-uz">koʻplik, jonsiz</td><td class="pr-res">но́вые дома́</td>
      <td class="pr-end">но́вые дома́</td><td class="pr-uz">oʻzgarmaydi</td></tr>
  <tr><td class="pr-uz">koʻplik, jonli</td><td class="pr-res">но́вые учителя́</td>
      <td class="pr-end">но́вых учителе́й</td><td class="pr-uz">Роди́тельный shakli</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bir narsani payqang: <b>Вини́тельный hech qanday yangi shakl
yaratmaydi</b>. U yo bosh kelishikni takrorlaydi, yo Роди́тельный'ni — va
tanlov jonlilikka qarab qilinadi. Yagona haqiqiy yangi shakl —
<b>ayol jinsidagi -УЮ</b>. Yaʼni bugun siz aslida <b>ikkita</b> yangi
qoʻshimchani oʻrganyapsiz: <em>-ого</em> va <em>-ую</em>. Qolgani —
takrorlanish.</div>

<h3>3. Gaplarda</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">Я чита́ю <span class="pe-hl pe-hl--o">но́вую
     кни́гу</span>, а он чита́ет <span class="pe-hl pe-hl--o">ста́рый
     журна́л</span>.</p>
  <p class="pe-ex__uz">Men yangi kitobni oʻqiyapman, u esa eski jurnalni.</p>
  <p class="pe-ex__why">Ikkalasi ham Вини́тельный. Ayol jinsi
     <em>-ую</em> oldi, jonsiz erkak esa umuman oʻzgarmadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Я ви́жу <span class="pe-hl pe-hl--o">но́вого
     учи́теля</span> и <span class="pe-hl pe-hl--o">но́вый дом</span>.</p>
  <p class="pe-ex__uz">Yangi oʻqituvchini va yangi uyni koʻryapman.</p>
  <p class="pe-ex__why">Bitta gapda ikkala variant ham bor. Oʻqituvchi —
     jonli, demak <em>но́вого учи́теля</em>. Uy — jonsiz, demak
     <em>но́вый дом</em>. Sifat otga <b>toʻliq ergashadi</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">У <span class="pe-hl pe-hl--o">ста́рого моста́</span>
     нет <span class="pe-hl pe-hl--o">но́вой доро́ги</span>.</p>
  <p class="pe-ex__uz">Eski koʻprikda yangi yoʻl yoʻq.</p>
  <p class="pe-ex__why">Ikkita Роди́тельный: predlogdan keyin
     (<em>у ста́рого моста́</em>) va <em>нет</em> dan keyin
     (<em>но́вой доро́ги</em>).</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu yerda ochiq gapirish kerak: <b>oʻzbekcha bu darsda yordam
bermaydi</b>.<br><br>
Oʻzbekchada sifat <b>hech qachon</b> oʻzgarmaydi:<br>
<em><b>yangi</b> kitob</em> · <em><b>yangi</b> kitobni</em> ·
<em><b>yangi</b> kitobda</em> · <em><b>yangi</b> kitoblar</em><br>
Bitta shakl, hamma joyda. Ruschada esa sifat otga <b>uch tomondan</b>
moslashadi: jins, son <b>va</b> kelishik.<br><br>
Demak bu sof qoʻshimcha ish. Lekin ikkita narsa uni yengillashtiradi:<br>
1. Sifat <b>oʻz qaroriga ega emas</b> — u otga ergashadi. Otning
kelishigini bilsangiz, sifatniki oʻz-oʻzidan chiqadi.<br>
2. Qoida <b>istisnosiz</b>. Otlarda istisnolar koʻp edi (<em>лет,
челове́к, вре́мени</em>) — sifatlarda esa yoʻq.<br><br>
Shuning uchun bu darsni yodlash emas, <b>mashq qilish</b> kerak.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я чита́ю но́вая кни́гу.</s></p>
  <p class="pe-good">Я чита́ю <b>но́вую</b> кни́гу — sifat ham Вини́тельный'ga kiradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то дом но́вый учи́теля.</s></p>
  <p class="pe-good">Э́то дом <b>но́вого</b> учи́теля — ikkala soʻz ham Роди́тельный'da</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ви́жу но́вого до́ма.</s></p>
  <p class="pe-good">Я ви́жу <b>но́вый дом</b> — uy jonsiz, demak oʻzgarmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>У ру́сскых книг.</s></p>
  <p class="pe-good">У <b>ру́сских</b> книг — К dan keyin Ы yozilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ви́жу но́вый учи́теля.</s></p>
  <p class="pe-good">Я ви́жу <b>но́вого учи́теля</b> — jonli boʻlsa, ikkalasi ham oʻzgaradi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Я чита́ю ___ ___.</b> (но́вая кни́га)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>но́вую кни́гу</strong>.
    Вини́тельный: ayol jinsi sifat <b>-ую</b> oladi, ot esa <b>-у</b>.
    Ikkalasi birga oʻzgaradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Э́то дом ___ ___.</b> (ста́рый сосе́д)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ста́рого сосе́да</strong>.
    Egalik — Роди́тельный (PR-34), demak sifat <b>-ого</b>, ot
    <b>-а</b>. Va egasi orqada turibdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapdan qaysi birida sifat oʻzgaradi va nega?<br>
     <b>Я ви́жу но́вый дом. · Я ви́жу но́вого учи́теля.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Ikkinchisida. <em>Учи́тель</em> —
    <strong>jonli</strong>, shuning uchun Вини́тельный Роди́тельный
    shaklini oladi: <em>но́вого учи́теля</em>. <em>Дом</em> jonsiz, demak
    hech narsa oʻzgarmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>ста́рого</b> qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[ста́рава]</strong>. <b>-ОГО</b>
    har doim <b>[ово]</b> boʻlib oʻqiladi. Bu <em>его́</em> [йиво́] va
    <em>моего́</em> [маиво́] dagi qoidaning oʻsha oʻzi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Я чита́ю но́вую кни́гу. &nbsp; б) Э́то дом ста́рого сосе́да.<br>
     в) Я ви́жу но́вого до́ма. &nbsp; г) У ру́сских книг.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Я ви́жу но́вый дом</b>. Uy jonsiz, demak Вини́тельный bosh
    kelishik bilan bir xil qoladi — sifat ham, ot ham.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>но́вый → но́вого</b><span>yangi (Р.п.)</span></li>
  <li><b>ста́рый → ста́рого</b><span>eski (Р.п.)</span></li>
  <li><b>но́вую</b><span>yangi (В.п., ayol)</span></li>
  <li><b>ру́сских</b><span>ruscha (koʻplik Р.п.)</span></li>
  <li><b>мост</b><span>koʻprik</span></li>
  <li><b>доро́га</b><span>yoʻl</span></li>
  <li><b>рабо́чий</b><span>ishchi</span></li>
  <li><b>широ́кий</b><span>keng</span></li>
  <li><b>све́тлый</b><span>yorugʻ</span></li>
  <li><b>бо́льше нет</b><span>endi yoʻq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Sifat otga <b>ergashadi</b> — otning kelishigini bilsangiz,
        sifatniki oʻz-oʻzidan chiqadi.</li>
    <li>Роди́тельный: erkak va oʻrta <b>-ОГО</b>, ayol <b>-ОЙ</b>, koʻplik
        <b>-ЫХ / -ИХ</b>.</li>
    <li>Вини́тельный yangi shakl yaratmaydi — yagona yangilik ayol
        jinsidagi <b>-УЮ</b>.</li>
    <li>Jonlilik sifatga ham tegadi: <em>но́в<b>ого</b> учи́теля</em>,
        lekin <em>но́в<b>ый</b> дом</em>.</li>
    <li><b>-ОГО → [ово]</b>: <em>но́вого</em> [но́вава].</li>
    <li>Г, К, Х, Ж, Ш, Щ, Ч dan keyin <b>-И</b>: <em>ру́сских,
        хоро́ших</em>.</li>
    <li>Oʻzbekchada sifat oʻzgarmaydi — bu sof qoʻshimcha ish, lekin
        <b>istisnosiz</b>.</li>
  </ul>
</div>
""",
    },
]
