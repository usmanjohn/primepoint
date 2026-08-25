# -*- coding: utf-8 -*-
"""Prime Russian — Block H: kanal, kasb va ibora (92–94).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-92 — telefon, pochta va xabar. PR-90 uslubni tanlashni oʻrgatgan
edi; bu dars uni UCH KANALGA tarqatadi. Darsning eng foydali va eng
kam maʼlum qismi — CHATDAGI NUQTA: rus yozishmasida qisqa xabar
oxiridagi nuqta sovuq yoki jahl bilan aytilgandek eshitiladi. Buni
hech bir darslik aytmaydi, lekin har kuni kerak boʻladi.
PR-93 — ish va oʻqish leksikasi. Darsning gavhari — СДАВА́ТЬ / СДАТЬ:
bitta harf farq, natija esa qarama-qarshi. Bu PR-51 dagi feʼl turini
oʻquvchi har kuni ishlatadigan soʻzda koʻrsatadi. Oʻzbekchada ham
aynan shu juftlik bor: «imtihon topshirmoq» (jarayon) va «imtihondan
oʻtmoq» (natija).
PR-94 — frazeologizmlar. Dars roʻyxat emas: har bir ibora oʻz
HIKOYASI bilan beriladi (баклуши — yogʻoch qoshiq uchun tayyorlanadigan
boʻlaklar; нос — «burun» emas, oʻzi bilan olib yuriladigan hisob
taxtachasi). Uchta ibora esa oʻzbekchaga soʻzma-soʻz tushadi:
сидеть сложа руки = qoʻl qovushtirib oʻtirmoq · засучив рукава =
yeng shimarmoq · держать язык за зубами = tilini tiymoq.

⚠️ Oʻqish matnlarida URGʻU BELGISI YOʻQ (2026-08-24) — darsliklar saqlaydi.

Mashqlar:        practice/management/commands/_practice_pr_92_94.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_92_94.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_92_94.py --author=prime
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
        "title": "PR-92: Telefon, elektron pochta va xabar tili",
        "category": "russian",
        "order": 92,
        "summary": (
            "Bitta xabar, uch kanal, uch til. Va bitta kam maʼlum qoida: "
            "chatda qisqa xabar oxiriga nuqta qoʻysangiz, sovuq eshitiladi."
        ),
        "stories": ["Чат группы 11-«А»"],
        "content": """
<h2>PR-92: Telefon, elektron pochta va xabar tili</h2>

<p>PR-90 da uslubni tanlashni oʻrgandik. Lekin uslubni faqat
<b>kim</b> emas, <b>nima orqali</b> ham tanlaydi.</p>

<p>Bitta xabarni telefonda, elektron pochtada va chatda uch xil
aytasiz — hatto <b>bitta odamga</b> boʻlsa ham. Kanal ham til
qoʻyadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Telefon suhbatini <b>ochasiz va yopasiz</b></li>
    <li>Aloqa buzilganda nima deyishni bilasiz</li>
    <li>Elektron xatning <b>uch darajasini</b> ajratasiz</li>
    <li>Chat qisqartirishlarini <b>oʻqiy olasiz</b></li>
    <li>Chatdagi <b>nuqta qoidasini</b> bilib olasiz — buni darsliklar aytmaydi</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qoida</span>
  <span class="pe-chip pe-chip--s">bitta xabar</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">uch kanal</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">uch til</span>
</div>

<h3>1. Telefon: ochish</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Vaziyat</th><th>Rasmiy</th><th>Norasmiy</th></tr>
  <tr><td class="pr-stem">javob berish</td><td class="pr-res">Алло́? · Слу́шаю вас.</td>
      <td class="pr-end">Алло́? · Да?</td></tr>
  <tr><td class="pr-stem">oʻzini tanishtirish</td>
      <td class="pr-res">Здра́вствуйте, э́то Жасу́р Кари́мов.</td>
      <td class="pr-end">Приве́т, э́то Жасу́р.</td></tr>
  <tr><td class="pr-stem">kimnidir soʻrash</td>
      <td class="pr-res">Могу́ я поговори́ть с Мари́ной Петро́вной?</td>
      <td class="pr-end">Мари́ну мо́жно?</td></tr>
  <tr><td class="pr-stem">kimligini soʻrash</td>
      <td class="pr-res">Прости́те, с кем я говорю́?</td>
      <td class="pr-end">А э́то кто?</td></tr>
  <tr><td class="pr-stem">tugatish</td><td class="pr-res">Всего́ до́брого! До свида́ния!</td>
      <td class="pr-end">Дава́й! Пока́!</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">«Кто э́то?» — qoʻpol</span>
Telefonni koʻtarib <b>«Кто э́то?»</b> deyish rus tilida qoʻpol
eshitiladi — goʻyo siz emas, qoʻngʻiroq qilgan odam
tushuntirishi kerakdek.<br><br>
Muloyim shakli:<br>
<b>Прости́те, с кем я говорю́?</b> — Kechirasiz, kim bilan
gaplashyapman?<br>
<b>Предста́вьтесь, пожа́луйста.</b> — Oʻzingizni tanishtiring.<br><br>
Va yodda tuting: rasmiy qoʻngʻiroqda <b>qoʻngʻiroq qilgan odam</b>
birinchi boʻlib oʻzini tanishtiradi.</div>

<h3>2. Telefon: nimadir ishlamayotganda</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Rus tilida</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">Вы не туда́ попа́ли.</td>
      <td class="pr-uz">Notoʻgʻri raqamga tushdingiz.</td></tr>
  <tr><td class="pr-res">Вас пло́хо слы́шно.</td>
      <td class="pr-uz">Sizni yomon eshityapman.</td></tr>
  <tr><td class="pr-res">Связь плоха́я.</td><td class="pr-uz">Aloqa yomon.</td></tr>
  <tr><td class="pr-res">Я вам перезвоню́.</td>
      <td class="pr-uz">Sizga qayta qoʻngʻiroq qilaman.</td></tr>
  <tr><td class="pr-res">Не могли́ бы вы перезвони́ть?</td>
      <td class="pr-uz">Qayta qoʻngʻiroq qila olasizmi?</td></tr>
  <tr><td class="pr-res">Оста́вьтесь на ли́нии.</td>
      <td class="pr-uz">Liniyada qoling.</td></tr>
  <tr><td class="pr-res">Он сейча́с за́нят. Что ему́ переда́ть?</td>
      <td class="pr-uz">U hozir band. Unga nima yetkazay?</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">«Не туда́ попа́ли» — soʻzma-soʻz oʻgirilmaydi</span>
<b>Попа́сть</b> = «tushmoq, yetib bormoq». Yaʼni
<em>Вы не туда́ попа́ли</em> soʻzma-soʻz «siz u yerga
tushmadingiz» degani.<br><br>
Oʻzbekchada esa raqam haqida gapiriladi: «notoʻgʻri raqam»,
«adashib qoldingiz». Shuning uchun bu iborani <b>butunligicha</b>
yodlang — qismlarga ajratib tarjima qilmang.<br><br>
Javob berish: <em>Извини́те, пожа́луйста.</em> — Kechirasiz.</div>

<h3>3. Elektron xat: uch daraja</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Daraja</th><th>Kimga</th><th>Salom</th><th>Xayr</th></tr>
  <tr><td class="pr-stem">rasmiy</td><td class="pr-uz">notanish, rahbar</td>
      <td class="pr-res">Уважа́емая Мари́на Петро́вна!</td>
      <td class="pr-end">С уваже́нием, …</td></tr>
  <tr><td class="pr-stem">yarim rasmiy</td><td class="pr-uz">hamkasb, oʻqituvchi</td>
      <td class="pr-res">Здра́вствуйте, Мари́на Петро́вна!</td>
      <td class="pr-end">Спаси́бо! С уваже́нием, …</td></tr>
  <tr><td class="pr-stem">doʻstona</td><td class="pr-uz">doʻst, guruhdosh</td>
      <td class="pr-res">Приве́т, Ка́тя!</td>
      <td class="pr-end">Пока́! · Обнима́ю!</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Oʻrtadagi daraja eng koʻp kerak boʻladi</span>
Kundalik ishda xatlarning koʻpi <b>yarim rasmiy</b> boʻladi:
<em>Здра́вствуйте</em> bilan boshlanadi, <em>С уваже́нием</em> bilan
tugaydi, lekin ichida «Довожу́ до Ва́шего све́дения» kabi ogʻir
qoliplar yoʻq.<br><br>
Ishonchingiz komil boʻlmasa — <b>bir daraja rasmiyroq</b> yozing.
Ortiqcha hurmatdan hech kim xafa boʻlmaydi.</div>

<h3>4. Xabar (чат): qisqartirishlar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Qisqartma</th><th>Toʻliq shakli</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">спс</td><td class="pr-res">спаси́бо</td><td class="pr-end">rahmat</td></tr>
  <tr><td class="pr-stem">пжл</td><td class="pr-res">пожа́луйста</td><td class="pr-end">iltimos</td></tr>
  <tr><td class="pr-stem">норм</td><td class="pr-res">норма́льно</td><td class="pr-end">yaxshi, boʻladi</td></tr>
  <tr><td class="pr-stem">оч</td><td class="pr-res">о́чень</td><td class="pr-end">juda</td></tr>
  <tr><td class="pr-stem">сек</td><td class="pr-res">секу́нду</td><td class="pr-end">bir soniya</td></tr>
  <tr><td class="pr-stem">крч</td><td class="pr-res">коро́че</td><td class="pr-end">qisqasi</td></tr>
  <tr><td class="pr-stem">др</td><td class="pr-res">день рожде́ния</td><td class="pr-end">tugʻilgan kun</td></tr>
  <tr><td class="pr-stem">ок · хор</td><td class="pr-res">хорошо́</td><td class="pr-end">mayli</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbek chatida ham xuddi shu mexanizm</span>
Eʼtibor bering: rus qisqartmalarida <b>unlilar tashlab
ketiladi</b>, undoshlar qoladi — <em>спасибо → спс</em>,
<em>пожалуйста → пжл</em>, <em>короче → крч</em>.<br><br>
Oʻzbek yozishmasida ham aynan shunday qilinadi:
<em>salom → slm</em>, <em>rahmat → rhmt</em>.<br><br>
Yaʼni bu rus tilining oʻziga xosligi emas — bu <b>yozishmaning</b>
oʻziga xosligi. Shuning uchun bunday qisqartmalarni
<b>oʻqiy olish</b> kerak, lekin ularni rasmiy xatga hech qachon
olib kirmang.</div>

<h3>5. Chatdagi nuqta — darsliklar aytmaydigan qoida</h3>

<p>Mana bu darsning eng foydali qismi.</p>

<p>Zamonaviy rus yozishmasida <b>qisqa xabar oxiriga nuqta
qoʻyilmaydi</b>. Qoʻysangiz — xabar <b>sovuq</b>, hatto
<b>jahl bilan</b> aytilgandek eshitiladi.</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">NUQTASIZ — oddiy</p>
    <p><em>— Ты придёшь?<br>— <b>Да</b></em></p>
    <p>Oddiy «ha». Hech qanday qoʻshimcha ohang yoʻq.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">NUQTA BILAN — sovuq</p>
    <p><em>— Ты придёшь?<br>— <b>Да.</b></em></p>
    <p>«Ha» — lekin xafaman yoki gapirgim yoʻq degan ohang bilan.</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoidaning chegarasi</span>
Bu faqat <b>qisqa chat xabarlariga</b> tegishli. Uzun xabarda,
bir necha gapdan iborat matnda nuqta oddiy tinish belgisi boʻlib
qoladi va hech qanday ohang bermaydi.<br><br>
Va albatta, <b>elektron xatda, arizada, hujjatda</b> nuqta
har doim oʻz oʻrnida turadi — u yerda bu qoida ishlamaydi.<br><br>
Yodda tutish oson: <em>Хорошо</em> — mayli. <em>Хорошо.</em> —
«mayli, gapni yopdik».</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ohangni nima beradi</span>
Chatda ovoz ham, yuz ham yoʻq. Shuning uchun ohang boshqa
narsalar bilan beriladi:<br><br>
<b>emoji</b> — eng koʻp ishlatiladigani<br>
<b>«))»</b> — ruscha yozishmaning oʻz belgisi, kulgi bildiradi
(qavslar soni kuchni koʻrsatadi)<br>
<b>undov belgisi</b> — iliqlik: <em>Спасибо!</em> quruq
<em>Спасибо</em> dan issiqroq<br><br>
Yaʼni <em>Спасибо))</em> — «katta rahmat», <em>Спасибо.</em> —
«rahmat, lekin xafaman».</div>

<h3>6. Bitta xabar — uch kanal</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Xabar: uchrashuvni bir soatga surish kerak</p>
  <p class="pe-ex__ru"><b>Telefonda:</b> Здра́вствуйте, Мари́на Петро́вна!
     Э́то Жасу́р. Скажи́те, мы мо́жем перенести́ встре́чу на час?</p>
  <p class="pe-ex__ru"><b>Xatda:</b> Уважа́емая Мари́на Петро́вна!
     Прошу́ Вас перенести́ на́шу встре́чу на оди́н час, на 15:00.
     С уваже́нием, Жасу́р Кари́мов</p>
  <p class="pe-ex__ru"><b>Chatda:</b> Мари́на Петро́вна, здра́вствуйте!
     Мо́жем перенести́ на 15:00?</p>
  <p class="pe-ex__uz">Bitta xohish, uch xil uzunlik va uch xil ohang.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">— Алло́? — <s>Кто э́то?</s></p>
  <p class="pe-good">— <b>Прости́те, с кем я говорю́?</b> — muloyim shakli.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Вы взя́ли непра́вильный но́мер.</s></p>
  <p class="pe-good"><b>Вы не туда́ попа́ли.</b> — bu ibora butunligicha
     yodlanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Уважа́емая Мари́на Петро́вна! Спс за отве́т.</s></p>
  <p class="pe-good">…<b>Спаси́бо</b> за отве́т — chat qisqartmasi rasmiy
     xatga kirmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">— Ты придёшь на др? — <s>Да.</s></p>
  <p class="pe-good">— <b>Да</b> yoki <b>Да!</b> — chatda qisqa javob oxiriga
     nuqta qoʻysangiz, sovuq eshitiladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Telefonda notanish odam raqamingizga adashib tushdi. Nima
     deysiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Вы не туда́
    попа́ли.</strong> Muloyimroq: <em>Извини́те, вы не туда́
    попа́ли.</em> Soʻzma-soʻz «siz u yerga tushmadingiz» —
    oʻzbekchaga qismlarga ajratib oʻgirilmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu qisqartmalarni oching.<br>
     <b>спс · пжл · крч · др</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>спаси́бо · пожа́луйста ·
    коро́че · день рожде́ния</strong>. Qoida bitta: unlilar tashlab
    ketiladi, undoshlar qoladi — xuddi oʻzbekcha
    <em>slm</em>, <em>rhmt</em> kabi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Doʻstingiz chatda yozdi: <b>«Хорошо.»</b> Bu qanday ohang?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Sovuq yoki xafa</strong>
    ohang. Qisqa chat xabari oxiridagi nuqta «gapni yopdim» degan
    maʼno beradi. Oddiy roziligi <em>Хорошо</em> yoki
    <em>Хорошо!</em> boʻlardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Rahbaringizga rasmiy xat yozyapsiz. Bu gapni tuzating.<br>
     <b>Уважа́емый Оле́г Никола́евич! Крч, я не смогу́ прийти́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Уважа́емый Оле́г
    Никола́евич! Сообща́ю, что не смогу́ прису́тствовать.</strong>
    <em>Крч</em> — chat qisqartmasi, rasmiy xatga kirmaydi (PR-90).
    Bitta bunday soʻz butun xatning ohangini buzadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Rasmiy qoʻngʻiroqni boshlang. Siz — Dilnoza Yuldasheva, Marina
     Petrovna bilan gaplashmoqchisiz.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Здра́вствуйте! Э́то
    Дилно́за Ю́лдашева. Могу́ я поговори́ть с Мари́ной
    Петро́вной?</strong><br>Tartib muhim: avval salom, keyin
    <b>oʻzini tanishtirish</b>, undan keyin soʻrov. Rasmiy
    qoʻngʻiroqda qoʻngʻiroq qilgan odam birinchi boʻlib oʻzini
    aytadi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Алло́?</b><span>Alo? — telefonga javob</span></li>
  <li><b>Слу́шаю вас.</b><span>Eshitaman sizni</span></li>
  <li><b>Вы не туда́ попа́ли.</b><span>Notoʻgʻri raqamga tushdingiz</span></li>
  <li><b>Вас пло́хо слы́шно.</b><span>Sizni yomon eshityapman</span></li>
  <li><b>перезвони́ть</b><span>qayta qoʻngʻiroq qilmoq</span></li>
  <li><b>Что ему́ переда́ть?</b><span>Unga nima yetkazay?</span></li>
  <li><b>Всего́ до́брого!</b><span>Yaxshi qoling!</span></li>
  <li><b>сообще́ние</b><span>xabar</span></li>
  <li><b>голосово́е сообще́ние</b><span>ovozli xabar</span></li>
  <li><b>спс · пжл · крч</b><span>rahmat · iltimos · qisqasi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Uslubni faqat <b>kim</b> emas, <b>kanal</b> ham tanlaydi.</li>
    <li>Rasmiy qoʻngʻiroqda <b>qoʻngʻiroq qilgan odam</b> birinchi
        boʻlib oʻzini tanishtiradi.</li>
    <li><b>«Кто э́то?»</b> qoʻpol — <b>«Прости́те, с кем я
        говорю́?»</b> deng.</li>
    <li><b>Вы не туда́ попа́ли</b> — butunligicha yodlanadi.</li>
    <li>Elektron xatning <b>uch darajasi</b> bor; ikkilansangiz,
        bir daraja rasmiyroq yozing.</li>
    <li>Chat qisqartmalarida <b>unlilar tashlanadi</b>: спс, пжл,
        крч. Rasmiy xatga kirmaydi.</li>
    <li><b>Chatda qisqa javob oxiridagi nuqta sovuq eshitiladi.</b>
        <em>Хорошо</em> — mayli; <em>Хорошо.</em> — «gapni yopdik».</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-93: Ish va oʻqish leksikasi: rezyume, suhbat, imtihon",
        "category": "russian",
        "order": 93,
        "summary": (
            "«Сдава́л экза́мен» — topshirdim. «Сдал экза́мен» — oʻtdim. Bitta "
            "harf farq, natija qarama-qarshi. Rezyume, suhbat va imtihon tili."
        ),
        "stories": ["Первое собеседование"],
        "content": """
<h2>PR-93: Ish va oʻqish leksikasi: rezyume, suhbat, imtihon</h2>

<p>Ikki gap. Ular bitta harf bilan farq qiladi:</p>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">Я сдава́л экза́мен.</span>
    <span class="pr-pair__uz">Imtihon topshirdim. Natija nomaʼlum.</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">Я сдал экза́мен.</span>
    <span class="pr-pair__uz">Imtihondan oʻtdim. Natija — muvaffaqiyat.</span>
  </div>
</div>

<p>Birinchi gapni suhbatda aytsangiz, sizni imtihondan yiqilgan deb
tushunishadi. Shuning uchun bu darsni aynan shu juftlikdan
boshlaymiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Сдава́ть / сдать</b> tuzogʻidan chiqasiz</li>
    <li><b>Резюме́</b> ning qismlarini va tajriba feʼllarini olasiz</li>
    <li><b>Собесе́дование</b> savollariga tayyor qolip bilan javob berasiz</li>
    <li>Oʻqish leksikasini toʻplaysiz: се́ссия, зачёт, стипе́ндия</li>
    <li>Ish leksikasini toʻplaysiz: до́лжность, о́пыт, зарпла́та</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">сдава́ть — jarayon</span>
  <span class="pe-op">≠</span>
  <span class="pe-chip pe-chip--o">сдать — natija</span>
</div>

<h3>1. Feʼl turi tuzogʻi</h3>

<div class="pr-aspect">
  <div class="pr-aspect__side">
    <p class="pr-aspect__h">НСВ — что де́лать?</p>
    <p class="pr-aspect__v">сдава́ть экза́мен</p>
    <p>Imtihonga <b>kirmoq</b>, topshirmoq. Natija haqida hech
       narsa aytilmagan.</p>
  </div>
  <div class="pr-aspect__side pr-aspect__side--sv">
    <p class="pr-aspect__h">СВ — что сде́лать?</p>
    <p class="pr-aspect__v">сдать экза́мен</p>
    <p>Imtihondan <b>oʻtmoq</b>. Natija bor va u yaxshi.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekchada ham ikkita alohida ibora bor</span>
Bu farq siz uchun yangi emas — oʻzbek tilida ham bir emas,
<b>ikki</b> ibora ishlatiladi:<br><br>
<em>imtihon <b>topshirdim</b></em> — jarayon, kirdim va yozdim<br>
<em>imtihon<b>dan oʻtdim</b></em> — natija, muvaffaqiyat<br><br>
Ruschada bu ikki maʼno alohida soʻz emas, <b>bitta feʼlning ikki
turi</b> bilan beriladi:<br><br>
<b>сдава́ть</b> = topshirmoq &nbsp;·&nbsp; <b>сдать</b> = oʻtmoq<br><br>
Shuning uchun oʻzbekcha gapni tarjima qilishdan oldin bitta savol
bering: men <b>jarayon</b> haqida gapiryapmanmi yoki
<b>natija</b> haqidami?</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>НСВ — jarayon</th><th>СВ — natija</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">сдава́ть экза́мен</td><td class="pr-end">сдать экза́мен</td>
      <td class="pr-uz">topshirmoq / oʻtmoq</td></tr>
  <tr><td class="pr-res">поступа́ть в университе́т</td><td class="pr-end">поступи́ть в университе́т</td>
      <td class="pr-uz">hujjat topshirmoq / qabul qilinmoq</td></tr>
  <tr><td class="pr-res">устра́иваться на рабо́ту</td><td class="pr-end">устро́иться на рабо́ту</td>
      <td class="pr-uz">ishga kirmoqchi boʻlmoq / ishga kirmoq</td></tr>
  <tr><td class="pr-res">гото́виться к экза́мену</td><td class="pr-end">подгото́виться к экза́мену</td>
      <td class="pr-uz">tayyorlanmoq / tayyorlanib boʻlmoq</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Yiqilish haqida</span>
<b>Провали́ть экза́мен</b> — imtihondan yiqilmoq (neytral,
rasmiy).<br>
<b>Завали́ть экза́мен</b> — oʻsha maʼno, lekin <b>soʻzlashuv</b>
uslubi (PR-85).<br>
<b>Не сдать экза́мен</b> — eng xotirjam va eng xavfsiz shakl.<br><br>
Suhbatda oʻzingiz haqingizda gapirsangiz, <em>не сдал</em> deng —
<em>завали́л</em> juda ochiq va gʻayrirasmiy eshitiladi.</div>

<h3>2. Резюме́ — qismlari</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha nomi</th><th>Oʻzbekcha</th><th>Nima yoziladi</th></tr>
  <tr><td class="pr-stem">ФИО</td><td class="pr-uz">F.I.Sh.</td>
      <td class="pr-end">familiya, ism, otasining ismi</td></tr>
  <tr><td class="pr-stem">Контакты</td><td class="pr-uz">aloqa</td>
      <td class="pr-end">telefon, pochta, shahar</td></tr>
  <tr><td class="pr-stem">Цель</td><td class="pr-uz">maqsad</td>
      <td class="pr-end">qaysi lavozimga daʼvogarsiz</td></tr>
  <tr><td class="pr-stem">О́пыт рабо́ты</td><td class="pr-uz">ish tajribasi</td>
      <td class="pr-end">oxirgisidan boshlab</td></tr>
  <tr><td class="pr-stem">Образова́ние</td><td class="pr-uz">taʼlim</td>
      <td class="pr-end">oliygoh, fakultet, yil</td></tr>
  <tr><td class="pr-stem">Навы́ки</td><td class="pr-uz">koʻnikmalar</td>
      <td class="pr-end">dasturlar, malakalar</td></tr>
  <tr><td class="pr-stem">Языки́</td><td class="pr-uz">tillar</td>
      <td class="pr-end">daraja bilan</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Til darajasini qanday yozish kerak</span>
Rus rezyumesida tillar shunday koʻrsatiladi:<br><br>
<b>родно́й</b> — ona tili<br>
<b>свобо́дно</b> — erkin<br>
<b>хорошо́</b> — yaxshi<br>
<b>ба́зовый у́ровень</b> — boshlangʻich daraja<br><br>
Masalan: <em>Узбе́кский — родно́й. Ру́сский — свобо́дно.
Англи́йский — ба́зовый у́ровень.</em></div>

<h3>3. Tajriba haqida yozadigan feʼllar</h3>

<p>Rezyumeda tajriba <b>oʻtgan zamon</b> va <b>СВ</b> bilan
yoziladi — natija koʻrsatilishi kerak:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Feʼl</th><th>Kelishigi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">рабо́тал в …</td><td class="pr-uz">П.п.</td>
      <td class="pr-res">рабо́тал в шко́ле № 12</td></tr>
  <tr><td class="pr-stem">занима́лся …</td><td class="pr-uz">Т.п.</td>
      <td class="pr-res">занима́лся перево́дами</td></tr>
  <tr><td class="pr-stem">отвеча́л за …</td><td class="pr-uz">В.п.</td>
      <td class="pr-res">отвеча́л за докуме́нты</td></tr>
  <tr><td class="pr-stem">руководи́л …</td><td class="pr-uz">Т.п.</td>
      <td class="pr-res">руководи́л гру́ппой</td></tr>
  <tr><td class="pr-stem">уча́ствовал в …</td><td class="pr-uz">П.п.</td>
      <td class="pr-res">уча́ствовал в олимпиа́де</td></tr>
  <tr><td class="pr-stem">организова́л …</td><td class="pr-uz">В.п.</td>
      <td class="pr-res">организова́л ку́рсы</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Har bir feʼl oʻz kelishigini oladi</span>
Bu jadvalning eng muhim ustuni — <b>oʻrtadagisi</b>. Feʼl
oʻzgarganda kelishik ham oʻzgaradi:<br><br>
<em>занима́лся <b>перево́дами</b></em> — Твори́тельный<br>
<em>отвеча́л <b>за докуме́нты</b></em> — за + Вини́тельный (PR-83)<br>
<em>уча́ствовал <b>в олимпиа́де</b></em> — в + Предло́жный<br><br>
Bu feʼllarni <b>kelishigi bilan birga</b> yodlang — alohida
yodlansa, rezyumeda xato chiqadi.</div>

<h3>4. Собесе́дование — savollar va javob qoliplari</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Savol</th><th>Oʻzbekcha</th><th>Javob boshlanishi</th></tr>
  <tr><td class="pr-res">Расскажи́те о себе́.</td><td class="pr-uz">Oʻzingiz haqingizda ayting.</td>
      <td class="pr-end">Меня́ зову́т… Я зако́нчил…</td></tr>
  <tr><td class="pr-res">Почему́ вы хоти́те у нас рабо́тать?</td>
      <td class="pr-uz">Nega bizda ishlamoqchisiz?</td>
      <td class="pr-end">Мне интере́сно…</td></tr>
  <tr><td class="pr-res">Каки́е у вас си́льные сто́роны?</td>
      <td class="pr-uz">Kuchli tomonlaringiz?</td>
      <td class="pr-end">Я уме́ю… Мне легко́ даётся…</td></tr>
  <tr><td class="pr-res">Кем вы ви́дите себя́ че́рез пять лет?</td>
      <td class="pr-uz">Besh yildan keyin oʻzingizni kim deb koʻrasiz?</td>
      <td class="pr-end">Я хоте́л бы стать… (Т.п.)</td></tr>
  <tr><td class="pr-res">Есть ли у вас вопро́сы?</td>
      <td class="pr-uz">Savollaringiz bormi?</td>
      <td class="pr-end">Да, скажи́те, пожа́луйста…</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__t">«Кем стать» — Твори́тельный (PR-40)</p>
  <p class="pe-ex__ru">Я хоте́л бы стать <b>руководи́телем</b> отде́ла.</p>
  <p class="pe-ex__uz">Boʻlim rahbari boʻlmoqchiman.</p>
  <p class="pe-ex__why">«Кем?» degan savol <b>Твори́тельный</b> talab
     qiladi — <s>стать руководи́тель</s> emas.</p>
</div>

<h3>5. Oʻqish va ish leksikasi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Oʻqish</th><th>Oʻzbekcha</th><th>Ish</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">факульте́т</td><td class="pr-uz">fakultet</td>
      <td class="pr-res">до́лжность</td><td class="pr-end">lavozim</td></tr>
  <tr><td class="pr-res">курс</td><td class="pr-uz">kurs</td>
      <td class="pr-res">о́пыт рабо́ты</td><td class="pr-end">ish tajribasi</td></tr>
  <tr><td class="pr-res">се́ссия</td><td class="pr-uz">imtihon davri</td>
      <td class="pr-res">зарпла́та</td><td class="pr-end">maosh</td></tr>
  <tr><td class="pr-res">зачёт</td><td class="pr-uz">sinov (bahosiz)</td>
      <td class="pr-res">вака́нсия</td><td class="pr-end">boʻsh ish oʻrni</td></tr>
  <tr><td class="pr-res">стипе́ндия</td><td class="pr-uz">stipendiya</td>
      <td class="pr-res">резюме́</td><td class="pr-end">rezyume</td></tr>
  <tr><td class="pr-res">дипло́м</td><td class="pr-uz">diplom</td>
      <td class="pr-res">испыта́тельный срок</td><td class="pr-end">sinov muddati</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Зачёт — oʻzbekchada aynan mos soʻz yoʻq</span>
Rus oliygohida ikki xil hisobot bor:<br><br>
<b>экза́мен</b> — baho qoʻyiladi (2 dan 5 gacha)<br>
<b>зачёт</b> — baho qoʻyilmaydi, faqat «oʻtdi / oʻtmadi»
(<em>зачёт / незачёт</em>)<br><br>
Shuning uchun <em>сдать зачёт</em> — «sinovdan oʻtmoq».
<b>Се́ссия</b> esa ikkalasi ham topshiriladigan davr —
oʻzbekcha «imtihon davri».</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я сдава́л экза́мен, тепе́рь я студе́нт.</s></p>
  <p class="pe-good">Я <b>сдал</b> экза́мен — natija kerak boʻlsa, СВ.
     <em>Сдава́л</em> faqat jarayonni bildiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я хочу́ стать перево́дчик.</s></p>
  <p class="pe-good">…стать <b>перево́дчиком</b> — «кем?» degan savol
     <b>Твори́тельный</b> oladi (PR-40).</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я занима́лся перево́ды.</s></p>
  <p class="pe-good">Я занима́лся <b>перево́дами</b> — <em>занима́ться</em>
     Твори́тельный talab qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я поступа́л в университе́т в 2024 году́ и сейча́с учу́сь.</s></p>
  <p class="pe-good">Я <b>поступи́л</b> в университе́т — qabul qilingan
     boʻlsangiz, СВ kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu ikki gapning farqini ayting.<br>
     <b>Афсо́на сдава́ла экза́мен. / Афсо́на сдала́ экза́мен.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi: <strong>imtihon
    topshirdi</strong> — kirdi va yozdi, natija nomaʼlum.
    Ikkinchisi: <strong>imtihondan oʻtdi</strong> — natija bor va
    u yaxshi. Oʻzbekchada ham ikki xil ibora ishlatiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Kelishikni qoʻying.<br>
     <b>Я занима́лся ___ и отвеча́л за ___ .</b> (перево́ды · докуме́нты)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>занима́лся
    перево́дами</strong> (Твори́тельный) · <strong>отвеча́л за
    докуме́нты</strong> (за + Вини́тельный). Har bir feʼl oʻz
    kelishigini oladi — ularni juft holda yodlang.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Suhbatda savol berishdi: <b>«Кем вы ви́дите себя́ че́рез пять
     лет?»</b> Javobni boshlang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я хоте́л бы стать
    руководи́телем отде́ла.</strong> «Кем?» → <b>Твори́тельный</b>.
    <em>Хоте́л бы</em> (PR-60) javobni muloyimroq qiladi —
    <em>я ста́ну</em> juda qatʼiy eshitilardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>Экза́мен</b> va <b>зачёт</b> orasidagi farq nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Экза́мен</strong> da baho
    qoʻyiladi, <strong>зачёт</strong> da esa faqat «oʻtdi /
    oʻtmadi» (<em>зачёт / незачёт</em>). Ikkalasi ham
    <b>се́ссия</b> davrida topshiriladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Rezyumening «Языки́» boʻlimini yozing: oʻzbekcha — ona tili,
     ruscha — erkin, inglizcha — boshlangʻich.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Узбе́кский — родно́й.
    Ру́сский — свобо́дно. Англи́йский — ба́зовый
    у́ровень.</strong><br>Eʼtibor bering: til nomlari bu yerda
    <b>sifat</b> shaklida turibdi (<em>ру́сский</em>,
    <em>англи́йский</em>), «по-ру́сски» emas.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>сдава́ть экза́мен</b><span>imtihon topshirmoq (jarayon)</span></li>
  <li><b>сдать экза́мен</b><span>imtihondan oʻtmoq (natija)</span></li>
  <li><b>поступи́ть в университе́т</b><span>oliygohga qabul qilinmoq</span></li>
  <li><b>резюме́</b><span>rezyume</span></li>
  <li><b>собесе́дование</b><span>suhbat, intervyu</span></li>
  <li><b>о́пыт рабо́ты</b><span>ish tajribasi</span></li>
  <li><b>навы́ки</b><span>koʻnikmalar</span></li>
  <li><b>до́лжность</b><span>lavozim</span></li>
  <li><b>зарпла́та</b><span>maosh</span></li>
  <li><b>се́ссия · зачёт · стипе́ндия</b><span>imtihon davri · sinov · stipendiya</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Сдава́ть</b> = topshirmoq (jarayon), <b>сдать</b> =
        oʻtmoq (natija). Oʻzbekchada ham ikki ibora bor.</li>
    <li>Xuddi shunday juftlik: <b>поступа́ть / поступи́ть</b>,
        <b>устра́иваться / устро́иться</b>.</li>
    <li>Yiqilish: <b>не сдал</b> (xotirjam) · <b>провали́л</b>
        (neytral) · <b>завали́л</b> (soʻzlashuv).</li>
    <li>Tajriba feʼllari <b>kelishigi bilan</b> yodlanadi:
        <em>занима́лся</em> + Т.п., <em>отвеча́л за</em> + В.п.,
        <em>уча́ствовал в</em> + П.п.</li>
    <li><b>Кем стать?</b> → <b>Твори́тельный</b>:
        <em>стать перево́дчиком</em>.</li>
    <li><b>Зачёт</b> — bahosiz sinov; <b>экза́мен</b> — baholi;
        <b>се́ссия</b> — ikkalasining davri.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-94: Фразеологизмы — rus iboralarining ichki mantigʻi",
        "category": "russian",
        "order": 94,
        "summary": (
            "Ibora yodlanmaydi — tushuniladi. Har birining orqasida hikoya "
            "bor, uchtasi esa oʻzbekchaga soʻzma-soʻz tushadi: yeng shimarmoq."
        ),
        "stories": ["Бить баклуши и другие загадки"],
        "content": """
<h2>PR-94: Фразеологизмы — rus iboralarining ichki mantigʻi</h2>

<p>Rus tilida <b>бить баклу́ши</b> degan ibora bor. U «bekorchilik
qilmoq» degani.</p>

<p>Lekin <em>баклу́ши</em> nima? Va nega ularni <em>urish</em> kerak?</p>

<p>Aynan shu savol bu darsning kaliti. Iboralarni <b>yodlash</b>
qiyin, lekin <b>tushunish</b> oson — chunki deyarli har birining
orqasida haqiqiy hikoya turibdi. Hikoyani bilsangiz, ibora oʻzi esda
qoladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Фразеологи́зм</b> nima ekanini aniq bilasiz</li>
    <li>Toʻrtta iboraning <b>haqiqiy kelib chiqishini</b> oʻrganasiz</li>
    <li>Oʻzbekchaga <b>soʻzma-soʻz tushadigan</b> uchta iborani olasiz</li>
    <li>Kundalik iboralarni <b>maʼnosi bilan</b> toʻplaysiz</li>
    <li>Iborani <b>qayerda ishlatmaslik</b> kerakligini bilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qoida</span>
  <span class="pe-chip pe-chip--s">soʻzlar yigʻindisi</span>
  <span class="pe-op">≠</span>
  <span class="pe-chip pe-chip--o">maʼnolar yigʻindisi</span>
</div>

<h3>1. Ibora nima</h3>

<p><b>Фразеологи́зм</b> — bu shunday soʻz birikmasiki, uning maʼnosi
<b>qismlaridan chiqmaydi</b>. Har bir soʻzni bilasiz, lekin
birikmaning maʼnosini bilmaysiz.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Ikki xil oʻqish</p>
  <p class="pe-ex__ru">Он <b>сел в лу́жу</b>.</p>
  <p class="pe-ex__uz">Soʻzma-soʻz: «koʻlmakka oʻtirdi». Aslida: <b>sharmanda boʻldi</b>.</p>
  <p class="pe-ex__why">Shuning uchun lugʻatdan har bir soʻzni alohida
     qidirish yordam bermaydi — ibora <b>butun</b> holda qidiriladi.</p>
</div>

<h3>2. Toʻrtta ibora — toʻrtta hikoya</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Qayerdan kelgan</th></tr>
  <tr><td class="pr-res">бить баклу́ши</td><td class="pr-uz">bekorchilik qilmoq</td>
      <td class="pr-end">Баклу́ши — yogʻoch qoshiq yasash uchun
          yorib qoʻyilgan boʻlaklar. Ularni yorish eng oson,
          malaka talab qilmaydigan ish edi.</td></tr>
  <tr><td class="pr-res">зару́бить на носу́</td><td class="pr-uz">qattiq esda tutmoq</td>
      <td class="pr-end">Bu yerdagi <em>нос</em> — burun emas.
          U <em>носи́ть</em> dan: oʻzi bilan olib yuriladigan
          hisob taxtachasi, unga oʻyiq qilingan.</td></tr>
  <tr><td class="pr-res">спустя́ рукава́</td><td class="pr-uz">beparvo, sovuqqonlik bilan</td>
      <td class="pr-end">Eski rus kiyimining yenglari juda uzun
          edi. Yeng tushirilgan holda ishlab boʻlmasdi.</td></tr>
  <tr><td class="pr-res">води́ть за́ нос</td><td class="pr-uz">aldab yurmoq</td>
      <td class="pr-end">Yarmarkalarda ayiqlarni burniga
          halqa oʻtkazib yetaklashardi.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ikki ibora — bitta juftlik</span>
<b>Спустя́ рукава́</b> ning teskarisi ham bor va u xuddi shu
uzun yengdan chiqqan:<br><br>
<b>засучи́в рукава́</b> — yeng shimarib, jon-jahdi bilan<br><br>
<em>Он рабо́тал <b>спустя́ рукава́</b>.</em> — Beparvo ishladi.<br>
<em>Он взя́лся за де́ло <b>засучи́в рукава́</b>.</em> — Yeng
shimarib kirishdi.<br><br>
Ikkalasini birga yodlang — ular bir-birining juftidir.</div>

<h3>3. Uchta ibora — oʻzbekchaga soʻzma-soʻz</h3>

<p>Odatda iborani soʻzma-soʻz tarjima qilish mumkin emas. Lekin
uchta holatda ikki til <b>bir xil obrazni</b> tanlagan:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Oʻzbekcha</th><th>Maʼnosi</th></tr>
  <tr class="pr-case__on"><td class="pr-res">засучи́в рукава́</td>
      <td class="pr-end">yeng shimarib</td><td class="pr-uz">jon-jahdi bilan ishga kirishmoq</td></tr>
  <tr class="pr-case__on"><td class="pr-res">сиде́ть сложа́ ру́ки</td>
      <td class="pr-end">qoʻl qovushtirib oʻtirmoq</td><td class="pr-uz">hech narsa qilmay oʻtirmoq</td></tr>
  <tr class="pr-case__on"><td class="pr-res">держа́ть язы́к за зуба́ми</td>
      <td class="pr-end">tilini tiymoq</td><td class="pr-uz">jim turmoq, sir saqlamoq</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Nega bular mos tushdi</span>
Bu uchtasi tasodif emas. Ular <b>tananing</b> va <b>mehnatning</b>
obraziga tayanadi — yeng, qoʻl, til. Bunday obrazlar deyarli hamma
tilda bir xil ishlaydi, chunki odam hamma joyda bir xil
ishlaydi.<br><br>
Lekin ehtiyot boʻling: <b>koʻpchilik iboralar mos tushmaydi</b>.
<em>Де́лать из му́хи слона́</em> — soʻzma-soʻz «pashshadan fil
yasamoq»; oʻzbekchada oʻsha maʼno boshqa obraz bilan beriladi.
Shuning uchun qoida bitta: <b>iborani tarjima qilmang, uning
juftini toping</b>.</div>

<h3>4. Kundalik iboralar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Soʻzma-soʻz</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">как снег на́ голову</td><td class="pr-stem">boshga qor kabi</td>
      <td class="pr-end">kutilmaganda, toʻsatdan</td></tr>
  <tr><td class="pr-res">де́лать из му́хи слона́</td><td class="pr-stem">pashshadan fil yasamoq</td>
      <td class="pr-end">kichik narsani kattalashtirmoq</td></tr>
  <tr><td class="pr-res">тяну́ть кота́ за хвост</td><td class="pr-stem">mushukni dumidan tortmoq</td>
      <td class="pr-end">ishni choʻzmoq</td></tr>
  <tr><td class="pr-res">как с гу́ся вода́</td><td class="pr-stem">gʻozdan suv kabi</td>
      <td class="pr-end">unga hech narsa taʼsir qilmaydi</td></tr>
  <tr><td class="pr-res">семь пя́тниц на неде́ле</td><td class="pr-stem">haftada yetti juma</td>
      <td class="pr-end">fikri tez-tez oʻzgaradigan odam</td></tr>
  <tr><td class="pr-res">у чёрта на кули́чках</td><td class="pr-stem">shaytonning uyida</td>
      <td class="pr-end">juda uzoqda</td></tr>
  <tr><td class="pr-res">не в свое́й таре́лке</td><td class="pr-stem">oʻz likopchasida emas</td>
      <td class="pr-end">oʻzini noqulay his qilmoq</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">«Не в свое́й таре́лке» — tarjima xatosidan tugʻilgan ibora</span>
Bu ibora fransuz tilidan kelgan deb hisoblanadi. Fransuzcha
<em>assiette</em> soʻzining <b>ikki</b> maʼnosi bor: «likopcha»
va «holat, vaziyat».<br><br>
Iborani rus tiliga oʻgirgan odam <b>notoʻgʻri maʼnoni</b>
tanlagan — «holat» oʻrniga «likopcha» deb tarjima qilgan.<br><br>
Xato qolib ketdi, ibora esa yashab qoldi. Yaʼni rus tilida ikki
yuz yildan beri odamlar «oʻz likopchasida emas» deb yurishibdi.</div>

<h3>5. Ни пу́ха ни пера́ — eng kerakli ibora</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Imtihon oldidan</p>
  <p class="pe-ex__ru">— За́втра экза́мен. <b>Ни пу́ха ни пера́!</b></p>
  <p class="pe-ex__ru">— <b>К чёрту!</b></p>
  <p class="pe-ex__uz">— Ertaga imtihon. Omad! — Rahmat! (soʻzma-soʻz: «shaytonga!»)</p>
  <p class="pe-ex__why">Bu ibora ovchilardan qolgan: <em>пух</em> —
     moʻyna, <em>перо́</em> — pat. Ovchiga «na moʻyna, na pat»
     deb tilashardi — koʻz tegmasin uchun. Javob esa faqat
     <b>«К чёрту!»</b> boʻladi.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">«Спаси́бо» deb javob berilmaydi</span>
Bu — juda muhim amaliy detal. <em>Ни пу́ха ни пера́!</em> ga
<b>«Спаси́бо»</b> deyilmaydi — ishonchga koʻra, bu omadni
qaytaradi.<br><br>
Yagona toʻgʻri javob: <b>«К чёрту!»</b><br><br>
Bu qoʻpol emas, aksincha — hamma shunday deydi va hech kim
xafa boʻlmaydi.</div>

<h3>6. Ibora muzlagan — oʻzgartirilmaydi</h3>

<p>Iboradagi soʻzlarni almashtirib boʻlmaydi. Ular <b>bir butun</b>
boʻlib yodlanadi:</p>

<div class="pe-fix">
  <p class="pe-bad"><s>бить баклу́шу</s> · <s>сиде́ть сложи́в ру́ки</s></p>
  <p class="pe-good"><b>бить баклу́ши</b> · <b>сиде́ть сложа́ ру́ки</b> —
     shakl qotib qolgan.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Uslub: qayerda ishlatilmaydi</span>
Iboralar <b>ogʻzaki va neytral</b> nutqning bezagi. Lekin
PR-90 va PR-91 dagi qoida bu yerda ham ishlaydi:<br><br>
✗ arizada va rasmiy xatda<br>
✗ ilmiy matnda<br>
✗ yangilik xabarida<br><br>
<s>Прошу́ Вас не тяну́ть кота́ за хвост.</s> — arizada bunday
yozilmaydi.<br>
✓ <em>Прошу́ рассмотре́ть моё заявле́ние в кратча́йший срок.</em></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">— Ни пу́ха ни пера́! — <s>Спаси́бо!</s></p>
  <p class="pe-good">— <b>К чёрту!</b> — yagona toʻgʻri javob.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>«Зару́бить на носу́» — burunga biror narsa yozmoq.</s></p>
  <p class="pe-good">Bu yerdagi <b>нос</b> — burun emas, oʻzi bilan olib
     yuriladigan <b>hisob taxtachasi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он рабо́тал засучи́в рукава́, поэ́тому ничего́ не
     сде́лал.</s></p>
  <p class="pe-good">…<b>спустя́ рукава́</b> — «beparvo».
     <em>Засучи́в рукава́</em> esa aksincha, «jon-jahdi bilan».</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Прошу́ Вас не тяну́ть кота́ за хвост.</s></p>
  <p class="pe-good">Rasmiy matnda ibora ishlatilmaydi:
     <b>в кратча́йший срок</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>«Зару́бить на носу́»</b> dagi <b>нос</b> nimani anglatadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Hisob taxtachasi</strong>
    — <em>носи́ть</em> feʼlidan, chunki uni oʻzi bilan olib
    yurishardi. Unga oʻyiq (<em>зару́бка</em>) qilib, qarzni yoki
    hisobni belgilashardi. Burunga hech qanday aloqasi yoʻq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu uch iboraning oʻzbekcha juftini toping.<br>
     <b>засучи́в рукава́ · сиде́ть сложа́ ру́ки · держа́ть язы́к за зуба́ми</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>yeng shimarib · qoʻl
    qovushtirib oʻtirmoq · tilini tiymoq</strong>. Uchtasi ham
    soʻzma-soʻz mos tushadi, chunki ikkala til ham bir xil
    obrazni — yeng, qoʻl, til — tanlagan.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Doʻstingiz ertaga imtihon topshiradi. Nima deysiz va u nima
     deb javob beradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>— <strong>Ни пу́ха ни
    пера́!</strong><br>— <strong>К чёрту!</strong><br>
    <em>Спаси́бо</em> deyilmaydi — ishonchga koʻra bu omadni
    qaytaradi. Ibora ovchilardan qolgan: «na moʻyna, na pat».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga qaysi ibora tushadi?<br>
     <b>Он обеща́л зако́нчить в понеде́льник, пото́м в сре́ду, пото́м
     в пя́тницу. У него́ ___ .</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>семь пя́тниц на
    неде́ле</strong> — fikri tez-tez oʻzgaradigan, soʻzida
    turmaydigan odam haqida.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapda xato bor. Toping.<br>
     <b>Прошу́ Вас не тяну́ть кота́ за хвост и рассмотре́ть моё
     заявле́ние.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Grammatika toʻgʻri, lekin
    <strong>uslub</strong> buzilgan: ariza — rasmiy hujjat, iboraga
    u yerda oʻrin yoʻq (PR-90, PR-91). Toʻgʻrisi:
    <em>Прошу́ рассмотре́ть моё заявле́ние <strong>в кратча́йший
    срок</strong>.</em></p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>фразеологи́зм</b><span>ibora, turgʻun birikma</span></li>
  <li><b>бить баклу́ши</b><span>bekorchilik qilmoq</span></li>
  <li><b>зару́бить на носу́</b><span>qattiq esda tutmoq</span></li>
  <li><b>спустя́ рукава́</b><span>beparvo</span></li>
  <li><b>засучи́в рукава́</b><span>yeng shimarib</span></li>
  <li><b>сиде́ть сложа́ ру́ки</b><span>qoʻl qovushtirib oʻtirmoq</span></li>
  <li><b>держа́ть язы́к за зуба́ми</b><span>tilini tiymoq</span></li>
  <li><b>как снег на́ голову</b><span>kutilmaganda</span></li>
  <li><b>не в свое́й таре́лке</b><span>oʻzini noqulay his qilmoq</span></li>
  <li><b>ни пу́ха ни пера́ — к чёрту!</b><span>omad! — rahmat!</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Ibora maʼnosi <b>qismlaridan chiqmaydi</b> — lugʻatdan
        butun holda qidiriladi.</li>
    <li>Deyarli har birining orqasida <b>hikoya</b> bor. Hikoyani
        bilsangiz, ibora oʻzi esda qoladi.</li>
    <li><b>Нос</b> «зару́бить на носу́» da burun emas — hisob
        taxtachasi.</li>
    <li>Uchtasi oʻzbekchaga soʻzma-soʻz tushadi: <b>yeng
        shimarib</b>, <b>qoʻl qovushtirib</b>, <b>tilini
        tiymoq</b>. Qolganlarini tarjima qilmang — juftini toping.</li>
    <li><b>Ни пу́ха ни пера́!</b> ga javob faqat <b>«К чёрту!»</b>,
        hech qachon «спаси́бо» emas.</li>
    <li>Ibora shakli <b>qotib qolgan</b> — soʻzlari almashtirilmaydi.</li>
    <li>Rasmiy matnda, arizada va ilmiy ishda — <b>ibora yoʻq</b>.</li>
  </ul>
</div>
""",
    },
]
