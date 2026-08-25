# -*- coding: utf-8 -*-
"""Prime Russian — Block H boshlanishi: til jonli holda (89–91).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

Block H grammatikani emas, UNI ISHLATISHNI oʻrgatadi. Uch dars bitta
zanjir: avval gap ichida urgʻuni qayerga qoʻyishni (89), keyin butun
matnning ohangini tanlashni (90), oxirida esa tayyor rasmiy hujjat
yozishni (91).

PR-89 — soʻz tartibi. Darsning gavhari va butun kursning eng chiroyli
oʻzbekcha levarlaridan biri: OʻZBEKCHADA HAM urgʻu oladigan soʻzning
oʻz joyi bor — u FEʼLDAN OLDIN turadi. Ruschada esa GAP OXIRIDA.
Yaʼni instinkt bir xil, faqat manzil boshqa. Ikkinchi katta fikr:
rus tilida artikl yoʻq, uning vazifasini soʻz tartibi bajaradi
(Пришёл мальчик = bir bola keldi · Мальчик пришёл = oʻsha bola keldi)
— oʻzbekchada ham aynan shunday.
PR-90 — uslub. Bu dars PR-84 (yuklamalar), PR-85 (jonli soʻzlashuv) va
PR-88 (kichraytirish) ni bitta joyga yigʻadi: uchchalasi ham
NORASMIY uslubning belgisi, va rasmiy matnda uchchalasi ham
taqiqlanadi. Канцелярит haqidagi ogohlantirish ham shu yerda.
PR-91 — ariza va rasmiy xat. Darsning gavhari: arizaning shapkasi
tirik kelishik mashqi — «kimga» Дательный, «kimdan» от + Родительный.
Oʻzbekcha ariza esa aynan -GA va -DAN ishlatadi. Toʻliq moslik.

⚠️ Oʻqish matnlarida URGʻU BELGISI YOʻQ (2026-08-24) — darsliklar saqlaydi.

Mashqlar:        practice/management/commands/_practice_pr_89_91.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_89_91.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_89_91.py --author=prime
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
        "title": "PR-89: Soʻz tartibi va maʼno urgʻusi — rus tilida nima birinchi keladi",
        "category": "russian",
        "order": 89,
        "summary": (
            "Rus tilida soʻz tartibi erkin, lekin bemaʼni emas: eng muhim soʻz "
            "gap oxiriga qoʻyiladi. Oʻzbekchada esa u feʼldan oldin turadi."
        ),
        "stories": ["Одно предложение, четыре смысла"],
        "content": """
<h2>PR-89: Soʻz tartibi va maʼno urgʻusi — rus tilida nima birinchi keladi</h2>

<p>Sizga aytishgan boʻlishi mumkin: «rus tilida soʻz tartibi erkin».
Bu yarim haqiqat.</p>

<p>Tartib grammatik jihatdan erkin — gapni qanday tuzsangiz ham
<b>xato boʻlmaydi</b>. Lekin har bir tartib <b>boshqa maʼno</b>
beradi. Yaʼni tartib erkin emas — u shunchaki grammatikaga emas,
<b>maʼnoga</b> xizmat qiladi.</p>

<p>Bu darsda oʻsha maʼnoni boshqarishni oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Gapdagi <b>eng muhim soʻzni</b> toʻgʻri joyga qoʻyasiz</li>
    <li><b>Savol testi</b> bilan tartibni tekshirasiz</li>
    <li>Rus tilida <b>artikl yoʻqligini</b> soʻz tartibi bilan qoplaysiz</li>
    <li><b>Не</b> ni koʻchirib, gapning maʼnosini oʻzgartirasiz</li>
    <li>Nima <b>erkin emasligini</b> bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qoida</span>
  <span class="pe-chip pe-chip--s">tanish narsa</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--adv">gap boshida</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">yangi narsa</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">gap oxirida</span>
</div>

<h3>1. Eng muhim soʻz — oxirda</h3>

<p>Rus gapi ikkiga boʻlinadi: <b>allaqachon maʼlum</b> boʻlgan qism va
<b>yangi</b> qism. Maʼlumi oldinda, yangisi <b>oxirida</b> turadi.</p>

<p>Mana bitta gap, toʻrt xil tartibda. Soʻzlar oʻsha-oʻsha:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Tartib</th><th>Qaysi savolga javob</th><th>Nimaga urgʻu</th></tr>
  <tr><td class="pr-res">Жасу́р вчера́ купи́л <b>кни́гу</b>.</td>
      <td class="pr-uz">Что купи́л Жасу́р?</td><td class="pr-end">nimani — <b>kitobni</b></td></tr>
  <tr><td class="pr-res">Кни́гу Жасу́р купи́л <b>вчера́</b>.</td>
      <td class="pr-uz">Когда́ он её купи́л?</td><td class="pr-end">qachon — <b>kecha</b></td></tr>
  <tr><td class="pr-res">Кни́гу вчера́ купи́л <b>Жасу́р</b>.</td>
      <td class="pr-uz">Кто купи́л кни́гу?</td><td class="pr-end">kim — <b>Jasur</b></td></tr>
  <tr><td class="pr-res">Кни́гу Жасу́р вчера́ <b>купи́л</b>.</td>
      <td class="pr-uz">Он её взял и́ли купи́л?</td><td class="pr-end">nima qildi — <b>sotib oldi</b></td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekchada ham urgʻuli soʻzning oʻz joyi bor</span>
Bu sizga notanish tuygʻu emas. Oʻzbek tilida ham eng muhim soʻz
tasodifiy joyda turmaydi — u <b>feʼldan darrov oldin</b> keladi:<br><br>
<em>Jasur kecha <b>kitobni</b> sotib oldi.</em> — nimani?<br>
<em>Kitobni Jasur <b>kecha</b> sotib oldi.</em> — qachon?<br>
<em>Kitobni kecha <b>Jasur</b> sotib oldi.</em> — kim?<br><br>
Uchala gapda ham urgʻuli soʻz <b>«sotib oldi»</b> dan oldin turibdi.<br><br>
<b>Demak instinkt bir xil, faqat manzil boshqa:</b><br>
oʻzbekchada muhim soʻz <b>feʼldan oldin</b>,<br>
ruschada esa <b>gap oxirida</b>.<br><br>
Oʻzbekchada feʼl doim oxirda turgani uchun bu ikki joy koʻpincha
ustma-ust tushadi — shuning uchun oʻzbek oʻquvchi bu qoidani tez
oʻzlashtiradi.</div>

<h3>2. Savol testi</h3>

<p>Tartibni tekshirishning oson yoʻli bor: <b>qaysi savolga javob
beryapsiz?</b> Javob boʻlgan soʻz <b>oxirga</b> tushishi kerak.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Savol va javob</p>
  <p class="pe-ex__ru">— Кто написа́л э́то письмо́?<br>— Э́то письмо́ написа́ла <b>Дилно́за</b>.</p>
  <p class="pe-ex__uz">— Bu xatni kim yozgan? — Bu xatni <b>Dilnoza</b> yozgan.</p>
  <p class="pe-ex__ru">— Что написа́ла Дилно́за?<br>— Дилно́за написа́ла <b>письмо́</b>.</p>
  <p class="pe-ex__uz">— Dilnoza nima yozgan? — Dilnoza <b>xat</b> yozgan.</p>
  <p class="pe-ex__why">Savoldagi soʻzlar javobning <b>boshida</b>
     takrorlanadi, yangi maʼlumot esa <b>oxiriga</b> qoʻyiladi.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Yozayotganda oʻzingizdan soʻrang</span>
Har bir gapni yozgandan keyin bitta savol bering: <b>«Bu gap qaysi
savolga javob beryapti?»</b><br><br>
Agar javob soʻzi oxirda boʻlmasa — tartibni oʻzgartiring. Bu
odat sizning ruschangizni bir haftada tabiiyroq qiladi.</div>

<h3>3. Artikl yoʻq — tartib bor</h3>

<p>Rus tilida <em>the</em> ham, <em>a</em> ham yoʻq. Unda «oʻsha kitob»
va «bir kitob» qanday ajratiladi? <b>Soʻz tartibi bilan.</b></p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">EGA OXIRDA — yangi, notanish</p>
    <p><em>В ко́мнате стоя́л <b>стол</b>.</em></p>
    <p>Xonada <b>bir stol</b> turardi. — stol birinchi marta tilga
       olinyapti.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">EGA BOSHIDA — tanish, maʼlum</p>
    <p><em><b>Стол</b> стоя́л в ко́мнате.</em></p>
    <p><b>Oʻsha stol</b> xonada turardi. — stol haqida allaqachon
       gapirilgan.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekchada ham artikl yoʻq — va ham xuddi shunday hal qilinadi</span>
Oʻzbek tili ham <em>the</em> siz yashaydi, va u ham bu ishni
<b>tartib</b> bilan bajaradi:<br><br>
<em>Xonada <b>stol</b> turardi.</em> — bir stol, yangi<br>
<em><b>Stol</b> xonada turardi.</em> — oʻsha stol, tanish<br><br>
Aynan ruschadagidek. Shuning uchun rus matnini oʻqiyotganda
«bu qaysi stol — yangimi yoki tanishmi?» degan savolga
<b>javob gapning oʻzida</b> turibdi.<br><br>
Yana bir misol:<br>
<em>Пришёл <b>ма́льчик</b>.</em> — bir bola keldi<br>
<em><b>Ма́льчик</b> пришёл.</em> — oʻsha bola keldi</div>

<h3>4. Не — qayerga qoʻysangiz, oʻshani inkor qiladi</h3>

<p><b>Не</b> oʻzidan <b>keyingi</b> soʻzni inkor qiladi. Uni koʻchirsangiz,
gapning maʼnosi butunlay oʻzgaradi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Gap</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">Я <b>не</b> говори́л ему́ об э́том.</td>
      <td class="pr-uz">Men unga bu haqda aytmadim.</td></tr>
  <tr><td class="pr-res"><b>Не</b> я говори́л ему́ об э́том.</td>
      <td class="pr-uz">Unga buni <b>men emas</b>, boshqa odam aytgan.</td></tr>
  <tr><td class="pr-res">Я говори́л <b>не</b> ему́.</td>
      <td class="pr-uz">Men <b>unga emas</b>, boshqasiga aytdim.</td></tr>
  <tr><td class="pr-res">Я говори́л ему́ <b>не</b> об э́том.</td>
      <td class="pr-uz">Men unga <b>bu haqda emas</b>, boshqa narsa haqida aytdim.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Toʻrt gap — toʻrt boshqa vaziyat</span>
Bu jadval kichik koʻrinadi, lekin amalda juda muhim. Bir soʻzni bir
soʻz oʻngga surganingizda <b>kim aybdor ekani</b> oʻzgaradi.
Rasmiy xatda yoki bahsda bu farq qimmatga tushadi.</div>

<h3>5. Nima erkin EMAS</h3>

<p>Erkinlik cheksiz emas. Bu uchtasi <b>hech qachon</b> ajralmaydi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Qoida</th><th>Toʻgʻri</th><th>Boʻlmaydi</th></tr>
  <tr><td class="pr-stem">predlog + ot birga</td><td class="pr-res">в шко́лу</td>
      <td class="pr-end">шко́лу в</td></tr>
  <tr><td class="pr-stem">sifat otdan oldin</td><td class="pr-res">но́вый дом</td>
      <td class="pr-end">дом но́вый (odatiy nutqda)</td></tr>
  <tr><td class="pr-stem">не inkor soʻz oldida</td><td class="pr-res">не он</td>
      <td class="pr-end">он не (bu boshqa maʼno)</td></tr>
  <tr><td class="pr-stem">soʻroq soʻzi boshida</td><td class="pr-res">Куда́ ты идёшь?</td>
      <td class="pr-end">Ты идёшь куда́?</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ogʻzaki nutqda ohang tartibni yengadi</span>
Gapirganda tartibni oʻzgartirmasdan ham urgʻu qoʻyish mumkin —
ovozni koʻtarish bilan. Buni <b>логи́ческое ударе́ние</b> deyishadi:<br><br>
<em>Я <b>вчера́</b> купи́л кни́гу.</em> — «kecha» kuchli aytilsa,
tartib oʻzgarmasa ham urgʻu oʻshanga tushadi.<br><br>
Lekin <b>yozuvda ovoz yoʻq</b>. Shuning uchun yozma matnda urgʻuni
faqat <b>tartib</b> bilan koʻrsatasiz — bu darsning butun mohiyati
shunda.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">— Кто написа́л письмо́? — <s>Дилно́за написа́ла письмо́.</s></p>
  <p class="pe-good">— Письмо́ написа́ла <b>Дилно́за</b>. — javob oxirda turishi kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ты идёшь куда́?</s></p>
  <p class="pe-good"><b>Куда́</b> ты идёшь? — soʻroq soʻzi gap boshida.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я не говори́л ему́ об э́том</s> — «unga men emas, boshqa
     odam aytgan» demoqchi boʻlsangiz</p>
  <p class="pe-good"><b>Не я</b> говори́л ему́ об э́том. — <em>не</em> ni
     inkor qilinayotgan soʻz oldiga qoʻying.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Дом но́вый стои́т на углу́.</s></p>
  <p class="pe-good"><b>Но́вый дом</b> стои́т на углу́ — sifat otdan oldin turadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Savolga toʻgʻri tartibda javob bering.<br>
     <b>— Кто откры́л окно́?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Окно́ откры́л Бекзо́д.</strong>
    Savol «kim» haqida, demak <em>Бекзо́д</em> gap <b>oxirida</b>
    turishi kerak. <s>Бекзо́д откры́л окно́</s> — grammatik jihatdan
    toʻgʻri, lekin boshqa savolga javob berardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu ikki gapning farqi nimada?<br>
     <b>В саду́ игра́ли де́ти.</b> &nbsp;/&nbsp; <b>Де́ти игра́ли в саду́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi: <strong>bogʻda bolalar
    oʻynayotgan edi</strong> — bolalar <b>yangi</b> maʼlumot,
    birinchi marta tilga olinyapti. Ikkinchisi: <strong>oʻsha
    bolalar bogʻda oʻynayotgan edi</strong> — bolalar tanish, yangi
    maʼlumot esa <em>qayerda</em>. Rus tilida artikl yoʻq, shuning
    uchun bu farqni tartib koʻrsatadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     «Kitobni men olmadim, boshqa odam olgan» degan maʼnoni bering.<br>
     <b>___ брал э́ту кни́гу.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Не я</strong> брал э́ту
    кни́гу. <em>Не</em> oʻzidan keyingi soʻzni inkor qiladi, demak
    u <em>я</em> ning oldida turishi kerak. <em>Я не брал э́ту
    кни́гу</em> esa shunchaki «men olmadim» degani.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gap qaysi savolga javob beradi?<br>
     <b>Э́ту статью́ Оле́г написа́л за оди́н ве́чер.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>За ско́лько вре́мени Оле́г
    написа́л э́ту статью́?</strong> Oxirgi qism — <em>за оди́н
    ве́чер</em> — yangi maʼlumot. Maqola ham, Oleg ham allaqachon
    maʼlum, shuning uchun ular oldinda turibdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring, urgʻuni <b>«ertaga»</b> ga qoʻying.<br>
     <b>Afsona imtihonni ertaga topshiradi.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Экза́мен Афсо́на сдаёт
    за́втра.</strong> Urgʻu «ertaga» da boʻlgani uchun
    <em>за́втра</em> gap <b>oxiriga</b> tushadi. Oʻzbekchada esa u
    feʼldan oldin turibdi — ikkala tilda ham urgʻuli soʻzning oʻz
    joyi bor, faqat joyi boshqa.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>поря́док слов</b><span>soʻz tartibi</span></li>
  <li><b>логи́ческое ударе́ние</b><span>maʼno urgʻusi</span></li>
  <li><b>интона́ция</b><span>ohang</span></li>
  <li><b>изве́стное</b><span>tanish, maʼlum qism</span></li>
  <li><b>но́вое</b><span>yangi qism</span></li>
  <li><b>смысл</b><span>maʼno</span></li>
  <li><b>подчёркивать</b><span>taʼkidlamoq</span></li>
  <li><b>меня́ть места́ми</b><span>oʻrin almashtirmoq</span></li>
  <li><b>отрица́ние</b><span>inkor</span></li>
  <li><b>вопроси́тельное сло́во</b><span>soʻroq soʻzi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Soʻz tartibi <b>grammatik jihatdan</b> erkin, <b>maʼno
        jihatdan</b> emas.</li>
    <li><b>Tanish narsa boshida, yangi narsa oxirida.</b> Eng muhim
        soʻz — <b>gap oxirida</b>.</li>
    <li>Oʻzbekchada urgʻuli soʻz <b>feʼldan oldin</b> turadi. Instinkt
        bir xil, manzil boshqa.</li>
    <li><b>Savol testi:</b> javob boʻlgan soʻz oxirga tushsin.</li>
    <li>Artikl yoʻq — <b>tartib</b> «oʻsha» va «bir» ni ajratadi:
        <em>Пришёл ма́льчик</em> / <em>Ма́льчик пришёл</em>.</li>
    <li><b>Не</b> oʻzidan keyingi soʻzni inkor qiladi.</li>
    <li>Erkin <b>emas</b>: predlog + ot, sifat + ot, soʻroq soʻzi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-90: Rasmiy va norasmiy uslub: bir fikrni ikki xil aytish",
        "category": "russian",
        "order": 90,
        "summary": (
            "Bitta xabar — ikki xil kiyim. Rasmiy uslubda kichraytirish ham, "
            "yuklama ham, qisqartirish ham boʻlmaydi: uchchalasi norasmiylik belgisi."
        ),
        "stories": ["Два письма об одном и том же"],
        "content": """
<h2>PR-90: Rasmiy va norasmiy uslub: bir fikrni ikki xil aytish</h2>

<p>Sergey ertaga ishga chiqa olmaydi. U kasal. Bu xabarni ikki kishiga
yetkazishi kerak — hamkasbi Olyaga va boʻlim boshligʻi Olga
Petrovnaga.</p>

<p><b>Xabar bitta. Matn esa ikkita boʻlishi shart.</b></p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">HAMKASBIGA</p>
    <p><em>Оль, приве́т! Слу́шай, я за́втра не смогу́ — заболе́л.
       Прикро́й, е́сли что. Ну, до свя́зи!</em></p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">BOSHLIQQA</p>
    <p><em>Уважа́емая О́льга Петро́вна! Сообща́ю Вам, что за́втра,
       15 ма́рта, я не смогу́ вы́йти на рабо́ту по боле́зни.
       С уваже́нием, Серге́й Волко́в.</em></p>
  </div>
</div>

<p>Ikkalasi ham toʻgʻri rus tili. Ikkalasini almashtirib yuborsangiz —
birinchisi qoʻpol, ikkinchisi kulgili chiqadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uslubning <b>uch murvatini</b> boshqarasiz: murojaat, lugʻat, grammatika</li>
    <li>Norasmiy soʻzning <b>rasmiy juftini</b> topasiz</li>
    <li>Rasmiy matnda <b>nima boʻlmasligini</b> aniq bilasiz</li>
    <li><b>Канцеляри́т</b> nima ekanini va nega undan qochish kerakligini bilasiz</li>
    <li>Bir matnni ikkinchi uslubga <b>oʻgirasiz</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch murvat</span>
  <span class="pe-chip pe-chip--s">murojaat</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">lugʻat</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">grammatika</span>
</div>

<h3>1. Birinchi murvat — murojaat</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th></th><th>Norasmiy</th><th>Rasmiy</th></tr>
  <tr><td class="pr-stem">olmosh</td><td class="pr-res">ты</td>
      <td class="pr-end">Вы (bosh harf bilan)</td></tr>
  <tr><td class="pr-stem">ism</td><td class="pr-res">Оль, Ди́ма</td>
      <td class="pr-end">О́льга Петро́вна, Дми́трий Ива́нович</td></tr>
  <tr><td class="pr-stem">salom</td><td class="pr-res">Приве́т!</td>
      <td class="pr-end">Уважа́емая О́льга Петро́вна!</td></tr>
  <tr><td class="pr-stem">xayr</td><td class="pr-res">Дава́й! До свя́зи!</td>
      <td class="pr-end">С уваже́нием, …</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Xatda «Вы» bosh harf bilan</span>
Bitta odamga yozilgan rasmiy xatda <b>Вы</b>, <b>Вам</b>, <b>Ваш</b>
bosh harf bilan yoziladi — bu hurmat belgisi:<br><br>
<em>Сообща́ю <b>Вам</b>… · Прошу́ <b>Вас</b>… · <b>Ваше</b>
письмо́ полу́чено.</em><br><br>
Koʻpchilikka yozilsa (masalan eʼlonda) — kichik harf bilan:
<em>Уважа́емые колле́ги, про́сим вас…</em></div>

<h3>2. Ikkinchi murvat — lugʻat</h3>

<p>Rasmiy uslubning oʻz soʻzlari bor. Ular kundalik soʻzlarning
«bayramona» juftlari:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Norasmiy</th><th>Rasmiy</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">сказа́ть</td><td class="pr-end">сообщи́ть</td>
      <td class="pr-uz">xabar bermoq</td></tr>
  <tr><td class="pr-res">купи́ть</td><td class="pr-end">приобрести́</td>
      <td class="pr-uz">sotib olmoq</td></tr>
  <tr><td class="pr-res">дать</td><td class="pr-end">предоста́вить</td>
      <td class="pr-uz">bermoq, ajratmoq</td></tr>
  <tr><td class="pr-res">нача́ть</td><td class="pr-end">приступи́ть к</td>
      <td class="pr-uz">kirishmoq</td></tr>
  <tr><td class="pr-res">помо́чь</td><td class="pr-end">оказа́ть по́мощь</td>
      <td class="pr-uz">yordam koʻrsatmoq</td></tr>
  <tr><td class="pr-res">сейча́с</td><td class="pr-end">в настоя́щее вре́мя</td>
      <td class="pr-uz">hozirgi vaqtda</td></tr>
  <tr><td class="pr-res">из-за</td><td class="pr-end">в связи́ с</td>
      <td class="pr-uz">…munosabati bilan</td></tr>
  <tr><td class="pr-res">но</td><td class="pr-end">одна́ко</td>
      <td class="pr-uz">lekin, biroq</td></tr>
  <tr><td class="pr-res">о́чень</td><td class="pr-end">весьма́</td>
      <td class="pr-uz">juda, nihoyatda</td></tr>
  <tr><td class="pr-res">пото́м</td><td class="pr-end">впосле́дствии</td>
      <td class="pr-uz">keyinchalik</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekchada ham xuddi shu ikkilik bor</span>
Bu boʻlinish sizga yangi emas. Oʻzbek tilida ham bir fikrning
kundalik va rasmiy shakli bor:<br><br>
<em>aytdim</em> → <em>maʼlum qilaman</em><br>
<em>oldim</em> → <em>qabul qildim</em><br>
<em>hozir</em> → <em>ayni paytda</em><br>
<em>shuning uchun</em> → <em>shu munosabat bilan</em><br><br>
Ikkala tilda ham rasmiy soʻzlar <b>uzunroq</b> va koʻpincha
<b>oʻzlashma</b>: ruschada — kitobiy va cherkov-slavyan qatlami,
oʻzbekchada — arab va fors qatlami. Yaʼni mexanizm bir xil.</div>

<h3>3. Uchinchi murvat — grammatika</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Belgi</th><th>Norasmiy</th><th>Rasmiy</th></tr>
  <tr><td class="pr-stem">gap uzunligi</td><td class="pr-res">qisqa, uzuq</td>
      <td class="pr-end">toʻliq, tugallangan</td></tr>
  <tr><td class="pr-stem">shaxs</td><td class="pr-res">я реши́л</td>
      <td class="pr-end">бы́ло при́нято реше́ние</td></tr>
  <tr><td class="pr-stem">feʼl / ot</td><td class="pr-res">мы прове́рили</td>
      <td class="pr-end">была́ проведена́ прове́рка</td></tr>
  <tr><td class="pr-stem">predlog</td><td class="pr-res">из-за дождя́</td>
      <td class="pr-end">в связи́ с дождём</td></tr>
  <tr><td class="pr-stem">soʻrov</td><td class="pr-res">Дай, пожа́луйста…</td>
      <td class="pr-end">Прошу́ Вас предоста́вить…</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__t">Bitta fikr, ikki grammatika</p>
  <p class="pe-ex__ru">Мы реши́ли не открыва́ть филиа́л.</p>
  <p class="pe-ex__uz">Biz filial ochmaslikka qaror qildik. — norasmiy, aniq kim.</p>
  <p class="pe-ex__ru">Бы́ло при́нято реше́ние не открыва́ть филиа́л.</p>
  <p class="pe-ex__uz">Filial ochmaslik haqida qaror qabul qilindi. — rasmiy, kim ekani yashiringan.</p>
  <p class="pe-ex__why">Rasmiy uslub <b>majhul nisbat</b>ni (PR-61)
     yaxshi koʻradi — chunki u <b>shaxsni yashiradi</b>.</p>
</div>

<h3>4. Rasmiy matnda hech qachon boʻlmaydigan uchta narsa</h3>

<p>Mana bu joyda oxirgi uch dars birlashadi. Uchchalasi ham
<b>norasmiylik belgisi</b>:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Nima</th><th>Qaysi darsda</th><th>Misol</th><th>Rasmiyda</th></tr>
  <tr><td class="pr-stem">yuklamalar</td><td class="pr-uz">PR-84</td>
      <td class="pr-res">же, ведь, ну, вот, ра́зве</td><td class="pr-end">✗</td></tr>
  <tr><td class="pr-stem">jonli qisqarishlar</td><td class="pr-uz">PR-85</td>
      <td class="pr-res">щас, здра́сьте, коро́че</td><td class="pr-end">✗</td></tr>
  <tr><td class="pr-stem">kichraytirish</td><td class="pr-uz">PR-88</td>
      <td class="pr-res">неде́лька, мину́точка</td><td class="pr-end">✗</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Bitta soʻz butun xatni buzadi</span>
Rasmiy xatda <b>bitta</b> norasmiy soʻz yetadi — matnning ohangi
darrov qulaydi:<br><br>
<s>Прошу́ предоста́вить о́тпуск на <b>неде́льку</b>.</s><br>
<s>Сообща́ю, что я, <b>коро́че</b>, не смогу́ прийти́.</s><br>
<s><b>Ну</b>, прошу́ рассмотре́ть моё заявле́ние.</s><br><br>
Uchchala gapda ham qolgan hamma narsa toʻgʻri. Faqat bitta soʻz —
va xat jiddiy boʻlmay qoladi.</div>

<h3>5. Канцеляри́т — rasmiylikning kasalligi</h3>

<p>Rasmiy uslubni <b>oshirib yuborish</b> ham xato. Rus yozuvchisi
Korney Chukovskiy 1962-yilda «Живо́й как жизнь» kitobida bunday tilga
nom qoʻygan: <b>канцеляри́т</b> — «idorachilik kasalligi».</p>

<div class="pe-fix">
  <p class="pe-bad"><s>В це́лях осуществле́ния улучше́ния ка́чества
     обслу́живания населе́ния…</s></p>
  <p class="pe-good">Что́бы лу́чше обслу́живать люде́й… — bir xil maʼno,
     uch marta qisqa.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Oddiy oʻlchov</span>
Agar gapda ketma-ket <b>uchta</b> «-ение / -ание» li ot kelsa — bu
канцеляри́т. Ularning birortasini <b>feʼlga</b> aylantiring:<br><br>
<s>проведе́ние прове́рки выполне́ния пла́на</s><br>
→ <b>прове́рить, как вы́полнен план</b><br><br>
Rasmiy uslub <b>aniq</b> boʻlishi kerak, <b>ogʻir</b> emas. Yaxshi
rasmiy xat — qisqa xat.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Приве́т, О́льга Петро́вна! Я за́втра не приду́.</s></p>
  <p class="pe-good"><b>Уважа́емая О́льга Петро́вна!</b> Сообща́ю Вам, что
     за́втра я не смогу́ вы́йти на рабо́ту.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Прошу́ предоста́вить мне о́тпуск на неде́льку.</s></p>
  <p class="pe-good">…о́тпуск на <b>неде́лю</b> — rasmiy matnda kichraytirish
     boʻlmaydi (PR-88).</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Уважа́емый Дми́трий! Ты не мог бы посмотре́ть отчёт?</s></p>
  <p class="pe-good">Уважа́емый <b>Дми́трий Ива́нович</b>! Не могли́ бы
     <b>Вы</b> посмотре́ть отчёт? — murojaat va olmosh mos boʻlsin.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Осуществля́ем проведе́ние обуче́ния сотру́дников.</s></p>
  <p class="pe-good"><b>Обуча́ем сотру́дников.</b> — канцеляри́т oʻrniga feʼl.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Rasmiy juftini toping.<br>
     <b>сказа́ть · купи́ть · сейча́с · из-за</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>сообщи́ть · приобрести́ ·
    в настоя́щее вре́мя · в связи́ с</strong>. Eʼtibor bering:
    rasmiy variant deyarli har doim <b>uzunroq</b> — ikkala tilda
    ham shunday.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu gapda nima notoʻgʻri?<br>
     <b>Уважа́емая Мари́на Петро́вна! Ну, прошу́ рассмотре́ть моё
     заявле́ние.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>«Ну»</strong> — yuklama
    (PR-84), rasmiy matnda oʻrni yoʻq. Uni olib tashlash yetadi:
    <em>Уважа́емая Мари́на Петро́вна! Прошу́ рассмотре́ть моё
    заявле́ние.</em></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu gapni norasmiy uslubga oʻgiring.<br>
     <b>Бы́ло при́нято реше́ние перенести́ встре́чу.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Мы реши́ли перенести́
    встре́чу.</strong> Majhul nisbat shaxsni yashirardi; norasmiy
    uslubda esa <b>kim</b> qilgani aytiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu канцеляри́т ni tuzating.<br>
     <b>Осуществля́ем проведе́ние прове́рки докуме́нтов.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Проверя́ем
    докуме́нты.</strong> Uchta «-ение» li ot ketma-ket kelgan edi —
    bu belgining oʻzi yetarli. Bittasini feʼlga aylantirsangiz, gap
    tiklanadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu xabarni boshligʻingizga yozing (rasmiy uslubda).<br>
     <b>«Дим, я опозда́ю мину́т на два́дцать, про́бки».</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Уважа́емый Дми́трий
    Ива́нович! Сообща́ю, что задержу́сь приме́рно на два́дцать
    мину́т в связи́ с зато́рами на доро́ге. С уваже́нием,
    …</strong><br>Uch murvat ham burildi: murojaat
    (Дим → Дми́трий Ива́нович), lugʻat (про́бки → зато́ры на
    доро́ге), grammatika (uzuq gap → toʻliq gap).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>стиль</b><span>uslub</span></li>
  <li><b>официа́льный</b><span>rasmiy</span></li>
  <li><b>разгово́рный</b><span>soʻzlashuv, norasmiy</span></li>
  <li><b>сообщи́ть</b><span>xabar bermoq</span></li>
  <li><b>предоста́вить</b><span>bermoq, ajratmoq</span></li>
  <li><b>в связи́ с</b><span>…munosabati bilan</span></li>
  <li><b>в настоя́щее вре́мя</b><span>hozirgi vaqtda</span></li>
  <li><b>одна́ко</b><span>lekin, biroq</span></li>
  <li><b>с уваже́нием</b><span>hurmat bilan</span></li>
  <li><b>канцеляри́т</b><span>ogʻir idorachilik tili</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Bitta fikrning <b>ikki kiyimi</b> bor. Kiyimni vaziyat
        tanlaydi, siz emas.</li>
    <li>Uch murvat: <b>murojaat</b> (ты/Вы), <b>lugʻat</b>
        (сказа́ть/сообщи́ть), <b>grammatika</b> (я реши́л / бы́ло
        при́нято реше́ние).</li>
    <li>Xatda bitta odamga — <b>Вы</b> bosh harf bilan.</li>
    <li>Rasmiy matnda <b>yuklama yoʻq</b> (PR-84), <b>qisqarish
        yoʻq</b> (PR-85), <b>kichraytirish yoʻq</b> (PR-88).</li>
    <li>Rasmiy uslub <b>majhul nisbat</b>ni yaxshi koʻradi — u
        shaxsni yashiradi.</li>
    <li><b>Канцеляри́т</b> — rasmiylikning oshib ketgani. Ketma-ket
        uchta «-ение» koʻrsangiz, bittasini feʼlga aylantiring.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-91: Xat, ariza va rasmiy hujjat tili",
        "category": "russian",
        "order": 91,
        "summary": (
            "Arizaning shapkasi — tirik kelishik mashqi: «kimga» Дательный, "
            "«kimdan» от + Родительный. Oʻzbekcha ariza esa -GA va -DAN ishlatadi."
        ),
        "stories": ["Первое заявление Бекзода"],
        "content": """
<h2>PR-91: Xat, ariza va rasmiy hujjat tili</h2>

<p>PR-90 da uslubni tanlashni oʻrgandik. Endi eng koʻp kerak
boʻladigan uchta hujjatni <b>tayyor qolip</b> sifatida olamiz:
<b>заявле́ние</b>, <b>делово́е письмо́</b> va <b>электро́нное
письмо́</b>.</p>

<p>Yaxshi xabar: bu hujjatlarda ijod qilish kerak emas. Ular
<b>qolip</b> — qolipni bilsangiz, yozish besh daqiqada bitadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Заявле́ние</b> ni toʻgʻri shapka bilan yozasiz</li>
    <li>Shapkadagi <b>ikki kelishikni</b> aniq qoʻyasiz</li>
    <li><b>Делово́е письмо́</b> ning besh qismini bilasiz</li>
    <li>Tayyor <b>rasmiy iboralarni</b> olasiz</li>
    <li>Elektron xatning <b>mavzu satrini</b> toʻgʻri yozasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Shapka</span>
  <span class="pe-chip pe-chip--o">kimga → Да́тельный</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">kimdan → от + Роди́тельный</span>
</div>

<h3>1. Заявле́ние — qolipi</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Toʻliq namuna</p>
  <p class="pe-ex__ru">Дире́ктору шко́лы № 12<br>
     Ивано́вой М. П.<br>
     от ученика́ 9-А кла́сса<br>
     Кари́мова Жасу́ра</p>
  <p class="pe-ex__ru"><b>Заявле́ние</b></p>
  <p class="pe-ex__ru">Прошу́ Вас разреши́ть мне не посеща́ть заня́тия
     12 ма́рта 2026 го́да в связи́ с уча́стием в областно́й
     олимпиа́де по ру́сскому языку́.</p>
  <p class="pe-ex__ru">10.03.2026 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Кари́мов</p>
  <p class="pe-ex__uz">Shapka yuqori oʻngda, «Заявление» oʻrtada,
     sana chapda, imzo oʻngda.</p>
</div>

<h3>2. Shapka — tirik kelishik mashqi</h3>

<p>Mana bu darsning gavhari. Shapkaning ikki satri — <b>ikki
kelishik</b>, va ikkalasi ham majburiy:</p>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Satr</th><th>Savoli</th><th>Kelishik</th><th>Shakli</th></tr>
  <tr class="pr-case__on"><td class="pr-case__name">yuqori satr</td>
      <td class="pr-case__q">кому́?</td>
      <td class="pr-case__word">Да́тельный</td>
      <td class="pr-case__uz">Дире́ктор<b>у</b> · Ивано́в<b>ой</b></td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">pastki satr</td>
      <td class="pr-case__q">от кого́?</td>
      <td class="pr-case__word">от + Роди́тельный</td>
      <td class="pr-case__uz">от ученик<b>а́</b> · Кари́мов<b>а</b></td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha ariza aynan shu ikki kelishikni ishlatadi</span>
Oʻzbekcha arizaning shapkasini yozing va yonma-yon qoʻying:<br><br>
<em>12-son maktab direktori<br>
M. P. Ivanova<b>ga</b></em> &nbsp;←&nbsp; joʻnalish kelishigi<br>
<em>9-A sinf oʻquvchisi<br>
Jasur Karimov<b>dan</b></em> &nbsp;←&nbsp; chiqish kelishigi<br><br>
Endi ruschasiga qarang:<br><br>
<em>Дире́ктору … Ивано́в<b>ой</b></em> &nbsp;←&nbsp; <b>Да́тельный</b><br>
<em><b>от</b> ученика́ … Кари́мов<b>а</b></em> &nbsp;←&nbsp;
<b>Роди́тельный</b><br><br>
<b>-GA = Да́тельный · -DAN = от + Роди́тельный.</b> Toʻliq moslik.
Oʻzbekcha arizani qanday boshlasangiz, ruschasini ham shunday
boshlaysiz — faqat qoʻshimcha oʻrniga kelishik qoʻyasiz.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Uchta kichik, lekin koʻzga tashlanadigan qoida</span>
<b>1.</b> <em>Заявле́ние</em> soʻzidan keyin <b>nuqta qoʻyilmaydi</b>.<br>
<b>2.</b> Familiya <b>ismdan oldin</b> yoziladi:
<em>Кари́мова Жасу́ра</em>, <s>Жасу́ра Кари́мова</s> emas.<br>
<b>3.</b> Matn har doim <b>«Прошу́»</b> soʻzi bilan boshlanadi —
«Я хочу́» yoki «Мне ну́жно» emas.</div>

<h3>3. Tayyor iboralar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Qachon</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">Прошу́ Вас разреши́ть…</td><td class="pr-uz">ruxsat soʻrash</td>
      <td class="pr-end">ruxsat berishingizni soʻrayman</td></tr>
  <tr><td class="pr-res">Прошу́ предоста́вить…</td><td class="pr-uz">taʼtil, hujjat</td>
      <td class="pr-end">berishingizni soʻrayman</td></tr>
  <tr><td class="pr-res">Прошу́ рассмотре́ть…</td><td class="pr-uz">ariza, taklif</td>
      <td class="pr-end">koʻrib chiqishingizni soʻrayman</td></tr>
  <tr><td class="pr-res">Довожу́ до Ва́шего све́дения, что…</td>
      <td class="pr-uz">xabar berish</td><td class="pr-end">maʼlum qilamanki…</td></tr>
  <tr><td class="pr-res">В связи́ с…</td><td class="pr-uz">sabab</td>
      <td class="pr-end">…munosabati bilan</td></tr>
  <tr><td class="pr-res">На основа́нии…</td><td class="pr-uz">hujjatga tayanish</td>
      <td class="pr-end">…asosida</td></tr>
  <tr><td class="pr-res">Зара́нее благодарю́.</td><td class="pr-uz">xat oxiri</td>
      <td class="pr-end">oldindan rahmat</td></tr>
  <tr><td class="pr-res">С уваже́нием, …</td><td class="pr-uz">imzo oldidan</td>
      <td class="pr-end">hurmat bilan</td></tr>
</table></div>

<h3>4. Делово́е письмо́ — besh qism</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Qolip</p>
  <p class="pe-ex__ru"><b>Уважа́емая Мари́на Петро́вна!</b></p>
  <p class="pe-ex__ru">Довожу́ до Ва́шего све́дения, что докуме́нты
     на́шей гру́ппы гото́вы.</p>
  <p class="pe-ex__ru">Прошу́ Вас сообщи́ть, когда́ мы мо́жем их
     принести́.</p>
  <p class="pe-ex__ru">Зара́нее благодарю́ за отве́т.</p>
  <p class="pe-ex__ru"><b>С уваже́нием,<br>Жасу́р Кари́мов</b></p>
  <p class="pe-ex__uz">Murojaat → xabar → soʻrov → minnatdorchilik → imzo.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Murojaatdan keyin — undov belgisi</span>
Rus ish xatida murojaatdan keyin <b>undov belgisi</b> qoʻyiladi va
keyingi gap <b>yangi qatordan, bosh harf bilan</b> boshlanadi:<br><br>
<b>Уважа́емый Дми́трий Ива́нович!</b><br>
<b>С</b>ообща́ю Вам, что…<br><br>
Vergul ham uchraydi, lekin undov belgisi <b>rasmiyroq</b> va ish
yozishmalarida shu meʼyor hisoblanadi.<br><br>
Va yodda tuting: <em>Уважа́ем<b>ый</b></em> — erkakka,
<em>Уважа́ем<b>ая</b></em> — ayolga.</div>

<h3>5. Электро́нное письмо́</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Qismi</th><th>Qoida</th><th>Misol</th></tr>
  <tr><td class="pr-stem">Те́ма</td><td class="pr-uz">qisqa, aniq, feʼlsiz</td>
      <td class="pr-res">Заявле́ние на уча́стие в олимпиа́де</td></tr>
  <tr><td class="pr-stem">Приве́тствие</td><td class="pr-uz">ism + otasining ismi</td>
      <td class="pr-res">Уважа́емая Мари́на Петро́вна!</td></tr>
  <tr><td class="pr-stem">Те́ло</td><td class="pr-uz">bir gap — bir fikr</td>
      <td class="pr-res">Прошу́ Вас рассмотре́ть…</td></tr>
  <tr><td class="pr-stem">По́дпись</td><td class="pr-uz">har doim boʻlsin</td>
      <td class="pr-res">С уваже́нием, Жасу́р Кари́мов</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Mavzu satri — xatning yuzi</span>
<b>Те́ма</b> ni «Вопро́с» yoki «Здра́вствуйте» deb yozmang — bunday
xat ochilmaydi. Mavzuda <b>nima</b> haqida ekani turishi kerak:<br><br>
✗ <s>Те́ма: Вопро́с</s><br>
✓ <b>Те́ма: Заявле́ние на о́тпуск с 12 по 19 ма́рта</b><br><br>
Yaxshi mavzu satri — ot bilan tugagan qisqa ibora, feʼlsiz.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Дире́ктор шко́лы Ивано́ва М. П.</s></p>
  <p class="pe-good">Дире́ктор<b>у</b> шко́лы Ивано́в<b>ой</b> М. П. —
     «kimga?» → <b>Да́тельный</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>от учени́к 9-А кла́сса Кари́мов Жасу́р</s></p>
  <p class="pe-good">от ученик<b>а́</b> 9-А кла́сса Кари́мов<b>а</b> Жасу́р<b>а</b>
     — «kimdan?» → <b>Роди́тельный</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Заявле́ние.</s> — nuqta bilan</p>
  <p class="pe-good"><b>Заявле́ние</b> — sarlavhadan keyin nuqta
     qoʻyilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я хочу́ пойти́ на олимпиа́ду.</s></p>
  <p class="pe-good"><b>Прошу́ Вас разреши́ть</b> мне уча́ствовать в
     олимпиа́де — arizada «xohlayman» emas, «soʻrayman».</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Shapkaning yuqori satrini yozing.<br>
     <b>Дире́ктор заво́да — Петро́в Ива́н Серге́евич</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Дире́ктору заво́да<br>
    Петро́ву И. С.</strong> — «kimga?» degan savolga javob, demak
    <b>Да́тельный</b>. Oʻzbekchada bu <em>-ga</em>:
    «zavod direktori Petrov I. S.<b>ga</b>».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Shapkaning pastki satrini yozing.<br>
     <b>Студе́нтка Ю́лдашева Дилно́за</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>от студе́нтки
    Ю́лдашевой Дилно́зы</strong> — «kimdan?», demak <b>от +
    Роди́тельный</b>. Uchala soʻz ham oʻzgardi:
    <em>студе́нтка → студе́нтки</em>,
    <em>Ю́лдашева → Ю́лдашевой</em>,
    <em>Дилно́за → Дилно́зы</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu boshlanish qaysi qoidani buzyapti?<br>
     <b>Уважа́емый Дми́трий Ива́нович, ты не мог бы посмотре́ть отчёт?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Ikkitasini. Birinchidan,
    murojaatdan keyin <strong>undov belgisi</strong> boʻlishi kerak.
    Ikkinchidan, <em>Уважа́емый + ism va otasining ismi</em> bilan
    <strong>ты</strong> birga kelmaydi — <b>Вы</b> boʻlishi shart:
    <em>Уважа́емый Дми́трий Ива́нович! Не могли́ бы Вы посмотре́ть
    отчёт?</em></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Elektron xatning mavzu satrini tuzating.<br>
     <b>Те́ма: Здра́вствуйте, у меня́ вопро́с</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Masalan: <strong>Те́ма: Вопро́с о
    сро́ках пода́чи докуме́нтов</strong>. Mavzu satrida salom ham,
    feʼl ham kerak emas — faqat <b>nima haqida</b> ekani, qisqa ot
    iborasi bilan.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Toʻliq ariza matnini yozing.<br>
     <b>Bekzod 3 apreldan 5 aprelgacha darsga kela olmaydi — akasining
     toʻyi bor.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Прошу́ Вас разреши́ть мне
    не посеща́ть заня́тия с 3 по 5 апре́ля в связи́ со сва́дьбой
    бра́та.</strong><br>Qolip: <em>Прошу́ Вас</em> + infinitiv +
    <em>в связи́ с</em> + sabab (Твори́тельный). Eʼtibor bering:
    <em>со</em> сва́дьбой — ikki undosh yonma-yon kelgani uchun
    <em>с</em> ga <b>о</b> qoʻshiladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>заявле́ние</b><span>ariza</span></li>
  <li><b>делово́е письмо́</b><span>ish xati</span></li>
  <li><b>Прошу́ Вас…</b><span>sizdan soʻrayman</span></li>
  <li><b>разреши́ть</b><span>ruxsat bermoq</span></li>
  <li><b>рассмотре́ть</b><span>koʻrib chiqmoq</span></li>
  <li><b>довожу́ до Ва́шего све́дения</b><span>maʼlum qilamanki</span></li>
  <li><b>на основа́нии</b><span>…asosida</span></li>
  <li><b>по́дпись</b><span>imzo</span></li>
  <li><b>уважа́емый / уважа́емая</b><span>hurmatli</span></li>
  <li><b>те́ма письма́</b><span>xat mavzusi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Shapka — <b>ikki kelishik</b>: «kimga» <b>Да́тельный</b>,
        «kimdan» <b>от + Роди́тельный</b>.</li>
    <li>Oʻzbekcha ariza aynan shuni qiladi: <b>-GA</b> va
        <b>-DAN</b>. Toʻliq moslik.</li>
    <li><b>Заявле́ние</b> dan keyin nuqta yoʻq; familiya ismdan
        oldin; matn <b>«Прошу́»</b> bilan boshlanadi.</li>
    <li>Ish xati besh qismli: murojaat → xabar → soʻrov →
        minnatdorchilik → imzo.</li>
    <li>Murojaatdan keyin <b>undov belgisi</b>, keyin yangi qatordan
        bosh harf.</li>
    <li>Elektron xatning <b>mavzusi</b> — qisqa ot iborasi, feʼlsiz
        va salomsiz.</li>
  </ul>
</div>
""",
    },
]
