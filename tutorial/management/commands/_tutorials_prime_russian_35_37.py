# -*- coding: utf-8 -*-
"""Prime Russian — Block D davomi (35–37).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-35 — Р.п. predloglar bilan. Bu yerda PR-30 dagi В/НА roʻyxati UCHINCHI
marta ishlaydi: в → из, на → с. Oʻzbekcha -DAN ikkiga boʻlinadi.
PR-36 — sonlar. Kursdagi eng «ruscha» qoida: 1 / 2-3-4 / 5+ uch xil shakl.
PR-37 — Да́тельный nihoyat oʻz nomini oladi. Oʻquvchi «мне на́до» (PR-27) va
«мне нра́вится» (PR-28) ni allaqachon ishlatyapti — bugun nega bunday
ekanini biladi. К va ПО predloglari PR-38 da.

Mashqlar:        practice/management/commands/_practice_pr_35_37.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_35_37.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_35_37.py --author=prime
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
        "title": "PR-35: Родительный 2: predloglar bilan — из, от, до, у, без, для, около, после",
        "category": "russian",
        "order": 35,
        "summary": (
            "Roditelniy padeji sakkizta predlog bilan ishlaydi va ularning "
            "koʻpchiligi oʻzbekchada tanish: -dan, -siz, uchun, -gacha, keyin. "
            "Yangi narsa bittagina — «dan» ruschada ikkiga boʻlinadi."
        ),
        "stories": ["Письмо́ из Сиби́ри"],
        "content": """
<h2>PR-35: Родительный 2: predloglar bilan — из, от, до, у, без, для, около, после</h2>

<p>Kecha siz Роди́тельный'ning ikkita ishini koʻrdingiz. Bugun uchinchisi:
<b>predloglar</b>. Yaxshi xabar shundaki, bu predloglarning deyarli hammasi
oʻzbekchada bor va siz ularni allaqachon ishlatasiz — <em>-dan</em>,
<em>-siz</em>, <em>uchun</em>, <em>-gacha</em>, <em>keyin</em>. Yangi narsa
bittagina: oʻzbekcha <b>«-dan»</b> rus tilida <b>ikkiga boʻlinadi</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Sakkizta predlogni oʻrganasiz: <b>из, от, до, у, без, для, о́коло, по́сле</b></li>
    <li><b>Из</b> va <b>с</b> ni ajratasiz — bu darsning yagona qiyin joyi</li>
    <li>Predlog juftliklarini koʻrasiz: <b>в → из</b>, <b>на → с</b></li>
    <li>Olmoshlarni ishlatasiz: <b>у меня́, от тебя́, без него́</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Predlog + Роди́тельный</span>
  <span class="pe-chip pe-chip--v">из</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">шко́л<b>ы</b></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--adv">maktab<b>dan</b></span>
</div>

<h3>1. Sakkizta predlog</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Predlog</th><th>Maʼnosi</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">из</td><td class="pr-uz">-dan (ichidan)</td>
      <td class="pr-end">из шко́лы</td><td class="pr-uz">maktabdan</td></tr>
  <tr><td class="pr-res">с</td><td class="pr-uz">-dan (ustidan)</td>
      <td class="pr-end">с рабо́ты</td><td class="pr-uz">ishdan</td></tr>
  <tr><td class="pr-res">от</td><td class="pr-uz">-dan (odamdan)</td>
      <td class="pr-end">от бра́та</td><td class="pr-uz">akadan</td></tr>
  <tr><td class="pr-res">до</td><td class="pr-uz">-gacha</td>
      <td class="pr-end">до шко́лы</td><td class="pr-uz">maktabgacha</td></tr>
  <tr><td class="pr-res">у</td><td class="pr-uz">yonida; -da (egalik)</td>
      <td class="pr-end">у окна́ · у меня́</td><td class="pr-uz">deraza yonida · menda</td></tr>
  <tr><td class="pr-res">без</td><td class="pr-uz">-siz</td>
      <td class="pr-end">без са́хара</td><td class="pr-uz">shakarsiz</td></tr>
  <tr><td class="pr-res">для</td><td class="pr-uz">uchun</td>
      <td class="pr-end">для ма́мы</td><td class="pr-uz">onam uchun</td></tr>
  <tr><td class="pr-res">о́коло</td><td class="pr-uz">yaqinida</td>
      <td class="pr-end">о́коло до́ма</td><td class="pr-uz">uy yaqinida</td></tr>
  <tr><td class="pr-res">по́сле</td><td class="pr-uz">keyin</td>
      <td class="pr-end">по́сле уро́ка</td><td class="pr-uz">darsdan keyin</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻng ustunga qarang — deyarli hamma qatorda tanish narsa turibdi:<br>
<em>maktab<b>dan</b></em> · <em>shakar<b>siz</b></em> · <em>onam
<b>uchun</b></em> · <em>maktab<b>gacha</b></em> · <em>darsdan
<b>keyin</b></em>.<br><br>
Yaʼni bu maʼnolar siz uchun yangi emas. Farq faqat <b>shaklda</b>:
oʻzbekchada ular <b>qoʻshimcha</b> (<em>-dan</em>, <em>-siz</em>,
<em>-gacha</em>) yoki <b>koʻmakchi</b> (<em>uchun</em>, <em>keyin</em>) —
yaʼni soʻzdan <b>keyin</b> keladi. Ruschada esa hammasi <b>predlog</b> —
soʻzdan <b>oldin</b> keladi va ot Роди́тельный'ga kiradi.<br><br>
Bitta narsa esa haqiqatan ham yangi: oʻzbekcha <b>-dan</b> ruschada
<b>uchta</b> predlogga boʻlinadi — <em>из</em>, <em>с</em> va <em>от</em>.
Buni keyingi boʻlimda koʻramiz.</div>

<h3>2. Predlog juftliklari — PR-30 roʻyxati yana ishlaydi</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
«Qayerdan?» degan savolning javobi <b>«qayerda?»</b> dan kelib chiqadi:<br>
Agar soʻz <b>В</b> olsa → «dan» uchun <b>ИЗ</b>.<br>
Agar soʻz <b>НА</b> olsa → «dan» uchun <b>С</b>.<br>
<em>в шко́ле → <b>из</b> шко́лы</em> · <em>на рабо́те → <b>с</b>
рабо́ты</em> · <em>на уро́ке → <b>с</b> уро́ка</em><br>
Yaʼni siz PR-30 da yodlagan НА-roʻyxat <b>uchinchi marta</b> ishlayapti.
Yangi hech narsa yodlash kerak emas.</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Где? (PR-30)</th><th>Куда́? (PR-33)</th><th>Отку́да? (bugun)</th></tr>
  <tr><td class="pr-res">в шко́ле</td><td class="pr-uz">в шко́лу</td>
      <td class="pr-end">из шко́лы</td></tr>
  <tr><td class="pr-res">в магази́не</td><td class="pr-uz">в магази́н</td>
      <td class="pr-end">из магази́на</td></tr>
  <tr><td class="pr-res">в Москве́</td><td class="pr-uz">в Москву́</td>
      <td class="pr-end">из Москвы́</td></tr>
  <tr><td class="pr-res">на рабо́те</td><td class="pr-uz">на рабо́ту</td>
      <td class="pr-end">с рабо́ты</td></tr>
  <tr><td class="pr-res">на уро́ке</td><td class="pr-uz">на уро́к</td>
      <td class="pr-end">с уро́ка</td></tr>
  <tr><td class="pr-res">на ры́нке</td><td class="pr-uz">на ры́нок</td>
      <td class="pr-end">с ры́нка</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>От</b> — bu uchinchi «dan», va u <b>odam</b> uchun ishlatiladi:<br>
<em>письмо́ <b>от</b> ма́мы</em> — onamdan kelgan xat<br>
<em>Я иду́ <b>от</b> врача́</em> — shifokordan (uning oldidan) kelyapman<br>
Yaʼni: joydan chiqsangiz — <em>из</em> yoki <em>с</em>. Odamning oldidan
kelsangiz — <b>от</b>. <em>«Письмо́ из ма́мы»</em> — xato.</div>

<h3>3. У — siz uni allaqachon bilasiz</h3>

<p>PR-14 da <em>У меня́ есть брат</em> ni oʻrgangan edingiz. Endi nega
<em>меня́</em> ekanini bilasiz: <b>у</b> predlogi Роди́тельный talab
qiladi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Izoh</th></tr>
  <tr><td class="pr-res">у меня́</td><td class="pr-uz">menda</td>
      <td class="pr-uz">egalik — PR-14</td></tr>
  <tr><td class="pr-res">у бра́та</td><td class="pr-uz">akamda</td>
      <td class="pr-uz">egalik</td></tr>
  <tr><td class="pr-res">у окна́</td><td class="pr-uz">deraza yonida</td>
      <td class="pr-uz">joy</td></tr>
  <tr><td class="pr-res">у до́ма</td><td class="pr-uz">uy oldida</td>
      <td class="pr-uz">joy</td></tr>
  <tr><td class="pr-res">у врача́</td><td class="pr-uz">shifokorda</td>
      <td class="pr-uz">odamning oldida</td></tr>
</table></div>

<h3>4. Olmoshlar — yangi narsa yoʻq</h3>

<p>Roditelniy olmoshlari <b>Вини́тельный bilan bir xil</b> (PR-32). Yaʼni
siz ularni allaqachon bilasiz:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Olmosh</th><th>Shakl</th><th>Predlogsiz</th><th>Predlog bilan</th></tr>
  <tr><td>я</td><td class="pr-res">меня́</td>
      <td class="pr-uz">меня́ нет</td><td class="pr-end">у меня́</td></tr>
  <tr><td>ты</td><td class="pr-res">тебя́</td>
      <td class="pr-uz">тебя́ нет</td><td class="pr-end">для тебя́</td></tr>
  <tr><td>он</td><td class="pr-res">его́ / него́</td>
      <td class="pr-uz">его́ нет</td><td class="pr-end">у <b>н</b>его́</td></tr>
  <tr><td>она́</td><td class="pr-res">её / неё</td>
      <td class="pr-uz">её нет</td><td class="pr-end">без <b>н</b>её</td></tr>
  <tr><td>мы</td><td class="pr-res">нас</td>
      <td class="pr-uz">нас нет</td><td class="pr-end">у нас</td></tr>
  <tr><td>вы</td><td class="pr-res">вас</td>
      <td class="pr-uz">вас нет</td><td class="pr-end">для вас</td></tr>
  <tr><td>они́</td><td class="pr-res">их / них</td>
      <td class="pr-uz">их нет</td><td class="pr-end">о́коло <b>н</b>их</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Uchinchi shaxsdagi <b>Н</b> ni PR-31 da koʻrgan edingiz — <em>о нём, о
ней</em>. Bu yerda ham oʻsha qoida: <b>predlogdan keyin Н qoʻshiladi</b>.
<em>Его́ нет</em> (predlogsiz) — lekin <em>у <b>н</b>его́</em> (predlog
bilan). Bitta qoida, uchinchi marta ishlayapti.</div>

<h3>5. Gaplarda</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">У́тром я иду́ <span class="pe-hl pe-hl--adv">из до́ма</span>
     на рабо́ту, а ве́чером — <span class="pe-hl pe-hl--adv">с рабо́ты</span>
     домо́й.</p>
  <p class="pe-ex__uz">Ertalab uydan ishga boraman, kechqurun esa ishdan
     uyga.</p>
  <p class="pe-ex__why">Bitta gapda ikkala «dan» ham bor. <em>Дом</em> В
     oladi, demak <b>из</b>. <em>Рабо́та</em> НА oladi, demak <b>с</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Вчера́ бы́ло письмо́
     <span class="pe-hl pe-hl--adv">от ма́мы</span>. Э́то фотогра́фия
     <span class="pe-hl pe-hl--adv">для тебя́</span>.</p>
  <p class="pe-ex__uz">Kecha onamdan xat keldi. Bu senga atalgan surat.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--adv">По́сле уро́ка</span>
     мы гуля́ем <span class="pe-hl pe-hl--adv">о́коло шко́лы</span>.
     Я пью чай <span class="pe-hl pe-hl--adv">без са́хара</span>.</p>
  <p class="pe-ex__uz">Darsdan keyin maktab yonida sayr qilamiz. Men choyni
     shakarsiz ichaman.</p>
  <p class="pe-ex__why">Uchta predlog, bitta kelishik. Barchasidan keyin
     <em>-а/-я</em> yoki <em>-ы/-и</em>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́ из рабо́ты.</s></p>
  <p class="pe-good">Я иду́ <b>с рабо́ты</b> — <em>рабо́та</em> НА oladi, demak С</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Письмо́ из ма́мы.</s></p>
  <p class="pe-good">Письмо́ <b>от ма́мы</b> — odam uchun ОТ</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то для ты.</s></p>
  <p class="pe-good">Э́то <b>для тебя́</b> — olmosh ham kelishikka kiradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Чай без са́хар.</s></p>
  <p class="pe-good">Чай <b>без са́хара</b> — predlogdan keyin Роди́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>У его́ есть маши́на.</s></p>
  <p class="pe-good"><b>У него́</b> есть маши́на — predlogdan keyin Н qoʻshiladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>из</b> yoki <b>с</b>? &nbsp; <b>Я иду́ ___ шко́лы, а брат ___
     рабо́ты.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>из</strong> шко́лы,
    <strong>с</strong> рабо́ты. Qoidani PR-30 dan oling: <em>в шко́ле</em> →
    demak <b>из</b>; <em>на рабо́те</em> → demak <b>с</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Э́то письмо́ ___ (ба́бушка).</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>от ба́бушки</strong>. Buvi — odam,
    demak <b>от</b>. Ayol jinsi Роди́тельный'da <b>-и</b> oladi (К dan keyin
    Ы yozilmaydi).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu iborani ruschaga oʻgiring: <b>Shakarsiz choy.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Чай без са́хара.</strong>
    Oʻzbekcha <em>-siz</em> qoʻshimchasi ruschada <b>без</b> predlogi
    boʻladi, va u soʻzdan <b>oldin</b> turadi. Ot esa Роди́тельный'ga
    kiradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga: <b>У ___ есть маши́на.</b> (он)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>него́</strong>. Predlogdan keyin
    <em>он</em> olmoshi <b>Н</b> bilan boshlanadi. Predlogsiz esa Н yoʻq:
    <em>его́ нет до́ма</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) По́сле уро́ка мы идём домо́й. &nbsp; б) Э́то пода́рок для тебя́.<br>
     в) Я иду́ из рабо́ты. &nbsp; г) О́коло до́ма есть магази́н.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>с рабо́ты</b>. <em>Рабо́та</em> НА oladigan roʻyxatda, shuning uchun
    «dan» uchun <b>С</b> kerak. Qolgan uchtasi toʻgʻri.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>отку́да?</b><span>qayerdan?</span></li>
  <li><b>из</b><span>-dan (ichidan)</span></li>
  <li><b>с</b><span>-dan (ustidan)</span></li>
  <li><b>от</b><span>-dan (odamdan)</span></li>
  <li><b>без</b><span>-siz</span></li>
  <li><b>для</b><span>uchun</span></li>
  <li><b>по́сле</b><span>keyin</span></li>
  <li><b>о́коло</b><span>yaqinida</span></li>
  <li><b>са́хар</b><span>shakar</span></li>
  <li><b>пода́рок</b><span>sovgʻa</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Sakkizta predlog Роди́тельный talab qiladi: <b>из, с, от, до, у,
        без, для, о́коло, по́сле</b>.</li>
    <li>Ularning maʼnolari oʻzbekchada bor — faqat joyi boshqa: predlog
        <b>oldinda</b> turadi.</li>
    <li><b>В → ИЗ</b>, <b>НА → С</b>. PR-30 roʻyxati uchinchi marta
        ishlayapti.</li>
    <li><b>ОТ</b> — odam uchun: <em>письмо́ от ма́мы</em>.</li>
    <li><b>У</b> + Роди́тельный — PR-14 dagi <em>у меня́ есть</em> ning
        izohi.</li>
    <li>Olmoshlar Вини́тельный bilan bir xil: <b>меня́, тебя́, его́, её,
        нас, вас, их</b>.</li>
    <li>Predlogdan keyin <em>он/она́/они́</em> ga <b>Н</b> qoʻshiladi:
        <em>у него́, без неё, о́коло них</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-36: Родительный 3: sonlar va miqdor bilan — два дома, пять домов, много книг",
        "category": "russian",
        "order": 36,
        "summary": (
            "Rus tilida son otning shaklini tanlaydi: bitta uy, ikki uyNING, besh "
            "uyLARNING. Uchta guruh, uchta shakl — va bu qoida har kuni kerak "
            "boʻladi."
        ),
        "stories": ["Ско́лько в Москве́ мосто́в?"],
        "content": """
<h2>PR-36: Родительный 3: sonlar va miqdor bilan — два дома, пять домов, много книг</h2>

<p>PR-13 da siz sonlarni oʻrgangan edingiz — <em>оди́н, два, три…</em>. Oʻshanda
bir narsa aytilmagan edi: rus tilida <b>son otning shaklini tanlaydi</b>.
<em>Оди́н дом</em>, lekin <em>два до́м<b>а</b></em>, va <em>пять
дом<b>о́в</b></em>. Bitta narsa, uchta shakl. Bugun bu qoidani toʻliq
olamiz — u har kuni kerak boʻladi: narx, vaqt, yosh, miqdor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uchta guruhni oʻrganasiz: <b>1</b> · <b>2-3-4</b> · <b>5 va undan yuqori</b></li>
    <li>Koʻplik Роди́тельный qoʻshimchalarini bilasiz</li>
    <li>Katta sonlarda oxirgi raqamga qarashni oʻrganasiz</li>
    <li><b>Мно́го, ма́ло, ско́лько</b> bilan ishlatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uchta guruh</span>
  <span class="pe-chip pe-chip--s">оди́н дом</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">два до́м<b>а</b></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">пять дом<b>о́в</b></span>
</div>

<h3>1. Uchta guruh</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Son</th><th>Otning shakli</th><th>Misol</th><th>Nima bu</th></tr>
  <tr><td class="pr-res">1</td><td class="pr-uz">bosh kelishik, birlik</td>
      <td class="pr-end">оди́н дом · одна́ кни́га</td>
      <td class="pr-uz">hech narsa oʻzgarmaydi</td></tr>
  <tr><td class="pr-res">2, 3, 4</td><td class="pr-uz">Роди́тельный, <b>birlik</b></td>
      <td class="pr-end">два до́ма · три кни́ги</td>
      <td class="pr-uz">PR-34 dagi shakl</td></tr>
  <tr><td class="pr-res">5, 6, 7…</td><td class="pr-uz">Роди́тельный, <b>koʻplik</b></td>
      <td class="pr-end">пять домо́в · пять книг</td>
      <td class="pr-uz">yangi shakl — quyida</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Два</b> yoki <b>две</b>? Bu son jinsga qarab oʻzgaradi — va faqat u:<br>
<b>два</b> — erkak va oʻrta jins: <em>два до́ма, два окна́</em><br>
<b>две</b> — ayol jinsi: <em>две кни́ги, две неде́ли</em><br>
Qolgan sonlar (<em>три, четы́ре, пять…</em>) jinsga qaramaydi. Faqat
<em>оди́н / одна́ / одно́</em> va <em>два / две</em>.</div>

<h3>2. Koʻplik Роди́тельный — qoʻshimchalar</h3>

<p>5 dan boshlab kerak boʻladigan shakl. Uchta asosiy naqsh bor:</p>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">-<span class="pr-end">ов</span> / -<span class="pr-end">ей</span></p>
    <p><em>дом → домо́в</em><br><em>час → часо́в</em><br>
       <em>рубль → рубле́й</em><br><em>врач → враче́й</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский -а</p>
    <p class="pr-gender__form">qoʻshimcha <b>yoʻq</b></p>
    <p><em>кни́га → книг</em><br><em>шко́ла → школ</em><br>
       <em>маши́на → маши́н</em><br><em>мину́та → мину́т</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний -о</p>
    <p class="pr-gender__form">qoʻshimcha <b>yoʻq</b></p>
    <p><em>ме́сто → мест</em><br><em>сло́во → слов</em><br>
       <em>окно́ → о́кон</em> <em>(О qoʻshiladi)</em></p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Ayol va oʻrta jinsdagi otlar koʻplik Роди́тельный'da <b>qoʻshimchasini
yoʻqotadi</b> — soʻz «yalangʻoch» qoladi: <em>книг, школ, слов, мест</em>.
Bu boshda gʻalati koʻrinadi, lekin aslida bu — <b>eng oson</b> shakl:
oxirgi harfni olib tashlang, tamom. Faqat baʼzan talaffuz uchun ichkariga
unli qoʻshiladi: <em>окно́ → о́к<b>о</b>н</em>, <em>де́вушка →
де́вуш<b>е</b>к</em>.</div>

<h3>3. Toʻliq misollar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ot</th><th>1</th><th>2, 3, 4</th><th>5+</th></tr>
  <tr><td class="pr-res">дом</td><td class="pr-uz">оди́н дом</td>
      <td class="pr-end">два до́ма</td><td class="pr-end">пять домо́в</td></tr>
  <tr><td class="pr-res">кни́га</td><td class="pr-uz">одна́ кни́га</td>
      <td class="pr-end">две кни́ги</td><td class="pr-end">пять книг</td></tr>
  <tr><td class="pr-res">окно́</td><td class="pr-uz">одно́ окно́</td>
      <td class="pr-end">два окна́</td><td class="pr-end">пять о́кон</td></tr>
  <tr><td class="pr-res">час</td><td class="pr-uz">оди́н час</td>
      <td class="pr-end">два часа́</td><td class="pr-end">пять часо́в</td></tr>
  <tr><td class="pr-res">год</td><td class="pr-uz">оди́н год</td>
      <td class="pr-end">два го́да</td><td class="pr-end">пять <b>лет</b></td></tr>
  <tr><td class="pr-res">рубль</td><td class="pr-uz">оди́н рубль</td>
      <td class="pr-end">два рубля́</td><td class="pr-end">пять рубле́й</td></tr>
  <tr><td class="pr-res">челове́к</td><td class="pr-uz">оди́н челове́к</td>
      <td class="pr-end">два челове́ка</td><td class="pr-end">пять <b>челове́к</b></td></tr>
  <tr><td class="pr-res">мину́та</td><td class="pr-uz">одна́ мину́та</td>
      <td class="pr-end">две мину́ты</td><td class="pr-end">пять мину́т</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Ikkita istisnoni alohida yodlang, chunki ular har kuni kerak:<br>
<b>год → лет</b>: <em>оди́н год, два го́да, пять <b>лет</b></em>. Yosh
aytilganda deyarli har doim shu shakl kerak boʻladi.<br>
<b>челове́к → челове́к</b>: <em>пять <b>челове́к</b></em>, <em>«пять
люде́й»</em> emas. Lekin sonsiz — <em>мно́го <b>люде́й</b></em>. Yaʼni son
bilan bitta shakl, <em>мно́го</em> bilan boshqasi.</div>

<h3>4. Katta sonlar — oxirgi raqamga qarang</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Yigirmadan keyin qoida oʻzgarmaydi, faqat <b>oxirgi raqamga</b> qaraladi:<br>
oxiri <b>1</b> → bosh kelishik: <em>два́дцать оди́н дом</em><br>
oxiri <b>2, 3, 4</b> → Роди́тельный birlik: <em>два́дцать два до́ма</em><br>
oxiri <b>5–9 yoki 0</b> → Роди́тельный koʻplik: <em>два́дцать пять
домо́в</em><br><br>
<b>Yagona istisno — 11 dan 14 gacha.</b> Ular «2, 3, 4» ga tugasa ham, har
doim <b>koʻplik</b> oladi: <em>оди́ннадцать домо́в</em>,
<em>двена́дцать домо́в</em>, <em>трина́дцать домо́в</em>,
<em>четы́рнадцать домо́в</em>.</div>

<h3>5. Мно́го, ма́ло, ско́лько</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Maʼnosi</th><th>Sanaladigan narsa</th><th>Sanalmaydigan narsa</th></tr>
  <tr><td class="pr-res">мно́го</td><td class="pr-uz">koʻp</td>
      <td class="pr-end">мно́го книг</td><td class="pr-uz">мно́го вре́мени</td></tr>
  <tr><td class="pr-res">ма́ло</td><td class="pr-uz">oz</td>
      <td class="pr-end">ма́ло домо́в</td><td class="pr-uz">ма́ло воды́</td></tr>
  <tr><td class="pr-res">ско́лько</td><td class="pr-uz">qancha, nechta</td>
      <td class="pr-end">ско́лько книг?</td><td class="pr-uz">ско́лько вре́мени?</td></tr>
  <tr><td class="pr-res">не́сколько</td><td class="pr-uz">bir necha</td>
      <td class="pr-end">не́сколько дней</td><td class="pr-uz">—</td></tr>
</table></div>

<p>Sanaladigan narsa — <b>koʻplik</b> Роди́тельный. Sanalmaydigan narsa
(suv, vaqt, pul) — <b>birlik</b> Роди́тельный. <em>Ско́лько вре́мени?</em> —
rus tilida «soat necha?» degan savol ham shu.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu yerda oʻzbek tili sizga <b>yarim yoʻl</b> yordam beradi.<br><br>
<b>Yordam beradigan qismi:</b> oʻzbekchada son bilan ot <b>koʻplikka
kirmaydi</b> — <em>besh kitob</em>, <em>«besh kitoblar»</em> emas. Bu
instinkt toʻgʻri va u sizni <em>«пять кни́ги»</em> tipidagi xatodan
saqlaydi… lekin faqat qisman.<br><br>
<b>Yordam bermaydigan qismi:</b> oʻzbekchada ot <b>umuman
oʻzgarmaydi</b> — <em>bir kitob, ikki kitob, besh kitob, yuz kitob</em>.
Bitta shakl, hamma son uchun. Ruschada esa uchta guruh bor va ot har
guruhda boshqacha koʻrinadi.<br><br>
Shuning uchun bu dars — <b>oʻzbek oʻquvchi uchun sof qoʻshimcha ish</b>.
Uni tan olish kerak: bu yerda oʻzbekcha yordam bermaydi, faqat mashq
yordam beradi. Yaxshi xabar shuki, qoida <b>istisnosiz</b> ishlaydi.</div>

<h3>6. Kundalik hayotda</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--v">Ско́лько</span> тебе́
     <span class="pe-hl pe-hl--o">лет</span>?<br>
     — Мне два́дцать <span class="pe-hl pe-hl--o">оди́н год</span>. А тебе́?<br>
     — Два́дцать <span class="pe-hl pe-hl--o">три го́да</span>.</p>
  <p class="pe-ex__uz">— Necha yoshdasan?<br>— Yigirma bir yoshdaman.
     Sen-chi?<br>— Yigirma uch.</p>
  <p class="pe-ex__why">Uchta javob, uchta shakl: <em>лет</em> (ско́лько
     bilan), <em>год</em> (oxiri 1), <em>го́да</em> (oxiri 3). Yosh haqidagi
     savol bu qoidani eng koʻp sinaydigan joy.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">В на́шем до́ме
     <span class="pe-hl pe-hl--o">пять этаже́й</span> и
     <span class="pe-hl pe-hl--o">со́рок кварти́р</span>.</p>
  <p class="pe-ex__uz">Bizning uyimizda besh qavat va qirq xonadon bor.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>пять кни́ги</s></p>
  <p class="pe-good">пять <b>книг</b> — 5 dan boshlab koʻplik Роди́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>два кни́ги</s></p>
  <p class="pe-good"><b>две</b> кни́ги — ayol jinsi uchun <em>две</em></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мне два́дцать оди́н лет.</s></p>
  <p class="pe-good">Мне два́дцать оди́н <b>год</b> — oxiri 1, demak bosh kelishik</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>оди́ннадцать до́ма</s></p>
  <p class="pe-good">оди́ннадцать <b>домо́в</b> — 11–14 har doim koʻplik</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>пять люде́й</s></p>
  <p class="pe-good">пять <b>челове́к</b> — son bilan boshqa shakl</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Toʻldiring: <b>оди́н дом · два ___ · пять ___</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>два до́ма · пять домо́в</strong>.
    Uchta guruh: 1 — bosh kelishik; 2-3-4 — Роди́тельный birlik; 5+ —
    Роди́тельный koʻplik.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>два</b> yoki <b>две</b>? &nbsp; <b>___ кни́ги · ___ окна́</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>две</strong> кни́ги (ayol jinsi) ·
    <strong>два</strong> окна́ (oʻrta jins). Faqat <em>оди́н</em> va
    <em>два</em> jinsga qaraydi; <em>три, четы́ре, пять</em> — yoʻq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Мне два́дцать два ___.</b> (год)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>го́да</strong>. Oxirgi raqam
    <b>2</b>, demak Роди́тельный birlik. Solishtiring: <em>два́дцать оди́н
    год</em> (oxiri 1) va <em>два́дцать пять лет</em> (oxiri 5).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga: <b>В кла́ссе двена́дцать ___.</b> (учени́к)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ученико́в</strong>. 11–14 —
    yagona istisno: ular «2» ga tugasa ham har doim <b>koʻplik</b>
    Роди́тельный oladi. Erkak jins, demak <b>-ов</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi qatorda hammasi toʻgʻri?<br>
     а) две кни́ги · пять книг · мно́го книг<br>
     б) два кни́ги · пять кни́ги · мно́го книг<br>
     в) две кни́ги · пять кни́ги · мно́го кни́ги<br>
     г) две кни́га · пять книг · мно́го книг</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>а)</strong>. Uchta shakl, uchta
    qoida: <em>две кни́ги</em> (2 + ayol jinsi), <em>пять книг</em> (5+ →
    koʻplik Роди́тельный, ayol jinsi qoʻshimchasini yoʻqotadi), <em>мно́го
    книг</em> (miqdor soʻzi ham koʻplik talab qiladi).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ско́лько?</b><span>qancha? nechta?</span></li>
  <li><b>мно́го</b><span>koʻp</span></li>
  <li><b>ма́ло</b><span>oz</span></li>
  <li><b>не́сколько</b><span>bir necha</span></li>
  <li><b>год → лет</b><span>yil (5 dan keyin)</span></li>
  <li><b>челове́к</b><span>odam</span></li>
  <li><b>рубль</b><span>rubl</span></li>
  <li><b>эта́ж</b><span>qavat</span></li>
  <li><b>мост</b><span>koʻprik</span></li>
  <li><b>число́</b><span>son, raqam</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>1</b> → bosh kelishik · <b>2, 3, 4</b> → Роди́тельный birlik ·
        <b>5+</b> → Роди́тельный koʻplik.</li>
    <li><b>Два</b> (erkak/oʻrta) va <b>две</b> (ayol) — faqat shu son jinsga
        qaraydi.</li>
    <li>Koʻplik Роди́тельный: erkak <b>-ов/-ей</b>, ayol va oʻrta —
        <b>qoʻshimcha yoʻq</b> (<em>книг, слов</em>).</li>
    <li>Katta sonlarda <b>oxirgi raqamga</b> qarang. <b>11–14</b> — istisno,
        har doim koʻplik.</li>
    <li>Yodlang: <b>пять лет</b>, <b>пять челове́к</b>.</li>
    <li><b>Мно́го, ма́ло, ско́лько</b> ham Роди́тельный talab qiladi.</li>
    <li>Oʻzbekchada ot son bilan umuman oʻzgarmaydi — bu yerda faqat mashq
        yordam beradi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-37: Дательный 1: кому? — дать, сказать, написать, помочь",
        "category": "russian",
        "order": 37,
        "summary": (
            "Siz bu kelishikni PR-27 dan beri ishlatyapsiz — «мне на́до», «мне "
            "нра́вится». Bugun u oʻz nomini oladi va otlarga ham qoʻllanadi. "
            "Oʻzbekcha -GA ning aynan oʻzi."
        ),
        "stories": ["Пода́рок учи́телю"],
        "content": """
<h2>PR-37: Дательный 1: кому? — дать, сказать, написать, помочь</h2>

<p>Bu kelishik siz uchun yangi emas. PR-27 da <em>мне на́до</em> dedingiz,
PR-28 da <em>мне нра́вится</em>. Oʻshanda men sizga aytgan edim: «bu
shakllar nima uchun bunday — PR-37 da». Mana, oʻsha dars. Bugun oʻsha
yettita olmosh oʻz nomini oladi va <b>otlarga</b> ham qoʻllanadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Qoʻshimchalarni oʻrganasiz: <b>-у/-ю</b> va <b>-е</b></li>
    <li>«Kimga?» degan savolga otlar bilan javob berasiz</li>
    <li>Ikki toʻldiruvchili gap tuzasiz: <b>дать кому́ что</b></li>
    <li><b>Помога́ть</b> nega Да́тельный olishini bilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kimga?</span>
  <span class="pe-chip pe-chip--v">Я дам</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">бра́т<b>у</b></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">кни́г<b>у</b></span>
</div>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Savoli</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-case__q">кто?</td>
      <td class="pr-case__word">брат</td><td class="pr-case__uz">bosh kelishik — aka</td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">Да́тельный</td>
      <td class="pr-case__q">кому́? чему́?</td>
      <td class="pr-case__word">бра́т<span class="pr-end">у</span></td>
      <td class="pr-case__uz">joʻnalish — aka<b>ga</b></td></tr>
</table></div>

<h3>1. Qoʻshimchalar</h3>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">-<span class="pr-end">у</span> / -<span class="pr-end">ю</span></p>
    <p><em>брат → бра́ту</em><br><em>оте́ц → отцу́</em><br>
       <em>учи́тель → учи́телю</em><br><em>Жасу́р → Жасу́ру</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний — oʻrta</p>
    <p class="pr-gender__form">-<span class="pr-end">у</span> / -<span class="pr-end">ю</span></p>
    <p><em>окно́ → окну́</em><br><em>письмо́ → письму́</em><br>
       <em>мо́ре → мо́рю</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">-<span class="pr-end">е</span></p>
    <p><em>ма́ма → ма́ме</em><br><em>сестра́ → сестре́</em><br>
       <em>Афсо́на → Афсо́не</em><br><em>Ка́тя → Ка́те</em></p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Ayol jinsidagi shakl sizga tanish koʻrinadi — va toʻgʻri koʻrinadi.
<em>Ма́ме</em> ham Да́тельный, ham Предло́жный (<em>о ма́ме</em>). PR-29 da
aytilgan edi: baʼzi shakllar takrorlanadi, shuning uchun yodlanadigan narsa
kutilganidan kam. Farqni <b>predlog</b> koʻrsatib turadi: predlog boʻlsa —
Предло́жный, boʻlmasa — Да́тельный.<br><br>
Va istisnolar ham tanish: <em>Росси́я → Росси́и</em>, <em>тетра́дь →
тетра́ди</em> — aynan Предло́жный'dagi kabi.</div>

<h3>2. Olmoshlar — siz ularni allaqachon bilasiz</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Olmosh</th><th>Да́тельный</th><th>PR-27 dan</th><th>PR-28 dan</th></tr>
  <tr><td>я</td><td class="pr-res">мне</td>
      <td class="pr-uz">Мне на́до идти́.</td><td class="pr-end">Мне нра́вится.</td></tr>
  <tr><td>ты</td><td class="pr-res">тебе́</td>
      <td class="pr-uz">Тебе́ на́до отдыха́ть.</td><td class="pr-end">Тебе́ нра́вится?</td></tr>
  <tr><td>он</td><td class="pr-res">ему́</td>
      <td class="pr-uz">Ему́ на́до рабо́тать.</td><td class="pr-end">Ему́ нра́вится футбо́л.</td></tr>
  <tr><td>она́</td><td class="pr-res">ей</td>
      <td class="pr-uz">Ей на́до учи́ться.</td><td class="pr-end">Ей нра́вятся ко́шки.</td></tr>
  <tr><td>мы</td><td class="pr-res">нам</td>
      <td class="pr-uz">Нам на́до спеши́ть.</td><td class="pr-end">Нам нра́вится здесь.</td></tr>
  <tr><td>вы</td><td class="pr-res">вам</td>
      <td class="pr-uz">Вам на́до отдохну́ть.</td><td class="pr-end">Вам нра́вится Ташке́нт?</td></tr>
  <tr><td>они́</td><td class="pr-res">им</td>
      <td class="pr-uz">Им на́до ждать.</td><td class="pr-end">Им нра́вится игра́ть.</td></tr>
</table></div>

<p>Oʻn dars davomida siz bu yettita shaklni ishlatib keldingiz. Endi
ularning nomi bor: <b>Да́тельный паде́ж</b>.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu — butun blokdagi eng aniq moslik, hatto <em>-ni</em> dan ham aniqroq:<br>
<em>aka<b>ga</b> aytdim</em> → <em>сказа́л бра́т<b>у</b></em><br>
<em>onam<b>ga</b> yozdim</em> → <em>написа́л ма́м<b>е</b></em><br>
<em>men<b>ga</b> kerak</em> → <em><b>мне</b> на́до</em><br>
Joʻnalish kelishigi ikkala tilda ham bir xil ishni qiladi va bir xil
joyda turadi. Bu yerda hech qanday tuzoq yoʻq.<br><br>
Va bitta joyda oʻzbekcha sizga <b>ingliz oʻquvchidan koʻra toʻgʻriroq</b>
javob beradi — <em>помога́ть</em> feʼlida. Buni keyingi boʻlimda
koʻring.</div>

<h3>3. Qaysi feʼllar Да́тельный oladi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Feʼl</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-res">дать</td><td class="pr-uz">bermoq</td>
      <td class="pr-end">Я дам бра́ту кни́гу.</td></tr>
  <tr><td class="pr-res">сказа́ть</td><td class="pr-uz">aytmoq</td>
      <td class="pr-end">Я сказа́л ма́ме пра́вду.</td></tr>
  <tr><td class="pr-res">писа́ть</td><td class="pr-uz">yozmoq</td>
      <td class="pr-end">Афсо́на пи́шет ба́бушке.</td></tr>
  <tr><td class="pr-res">звони́ть</td><td class="pr-uz">qoʻngʻiroq qilmoq</td>
      <td class="pr-end">Я звоню́ дру́гу.</td></tr>
  <tr><td class="pr-res">помога́ть</td><td class="pr-uz">yordam bermoq</td>
      <td class="pr-end">Бекзо́д помога́ет ба́бушке.</td></tr>
  <tr><td class="pr-res">отвеча́ть</td><td class="pr-uz">javob bermoq</td>
      <td class="pr-end">Он отвеча́ет учи́телю.</td></tr>
  <tr><td class="pr-res">объясня́ть</td><td class="pr-uz">tushuntirmoq</td>
      <td class="pr-end">Учи́тель объясня́ет кла́ссу.</td></tr>
  <tr><td class="pr-res">меша́ть</td><td class="pr-uz">xalaqit bermoq</td>
      <td class="pr-end">Не меша́й бра́ту.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Помога́ть</b> — ingliz tilini biladigan odam uchun tuzoq, siz uchun esa
yoʻq. Ingliz tilida «help» toʻgʻridan-toʻgʻri toʻldiruvchi oladi, shuning
uchun ular <em>«помога́ть бра́та»</em> deb yozadi.<br>
Oʻzbekchaga qarang: <em>aka<b>ga</b> yordam berdim</em> — <b>-ga</b>! Yaʼni
oʻzbekcha sizga darrov toʻgʻri javobni beradi: <b>помога́ть бра́ту</b>.
Xuddi shunday <em>звони́ть</em> (kimga qoʻngʻiroq qilmoq),
<em>отвеча́ть</em> (kimga javob bermoq), <em>меша́ть</em> (kimga xalaqit
bermoq) — hammasida oʻzbekcha <b>-ga</b> beradi va hammasi toʻgʻri.</div>

<h3>4. Ikki toʻldiruvchili gap</h3>

<p><em>Дать</em>, <em>сказа́ть</em>, <em>писа́ть</em> kabi feʼllar
<b>ikkita</b> toʻldiruvchi oladi: kimga (Да́тельный) va nimani
(Вини́тельный).</p>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Афсо́на</span>
     <span class="pe-hl pe-hl--v">пи́шет</span>
     <span class="pe-hl pe-hl--o">ба́бушке</span>
     <span class="pe-hl pe-hl--adv">письмо́</span>.</p>
  <p class="pe-ex__uz">Afsona buvisiga xat yozyapti.</p>
  <p class="pe-ex__why">Ikkita toʻldiruvchi, ikkita kelishik:
     <em>ба́бушк<b>е</b></em> — kimga (Да́тельный),
     <em>письмо́</em> — nimani (Вини́тельный, oʻrta jins, oʻzgarmaydi).
     Oʻzbekchadagi tartib ham xuddi shunday.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Что ты <span class="pe-hl pe-hl--v">сказа́л</span>
     <span class="pe-hl pe-hl--o">учи́телю</span>?<br>
     — Пра́вду.</p>
  <p class="pe-ex__uz">— Oʻqituvchiga nima dedingiz?<br>— Haqiqatni.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я помога́ю бра́та.</s></p>
  <p class="pe-good">Я помога́ю <b>бра́ту</b> — «akaga yordam beraman»</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я звоню́ ма́му.</s></p>
  <p class="pe-good">Я звоню́ <b>ма́ме</b> — «onamga qoʻngʻiroq qilaman»</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я дам брат кни́гу.</s></p>
  <p class="pe-good">Я дам <b>бра́ту</b> кни́гу — kimga? Да́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он сказа́л Афсо́ну пра́вду.</s></p>
  <p class="pe-good">Он сказа́л <b>Афсо́не</b> пра́вду — ayol jinsi <b>-е</b> oladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Учи́тель объясня́ет класс.</s></p>
  <p class="pe-good">Учи́тель объясня́ет <b>кла́ссу</b> — «sinfga tushuntiradi»</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Я звоню́ ___.</b> (ма́ма)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ма́ме</strong>. Ayol jinsi
    Да́тельный'da <b>-е</b> oladi. Oʻzbekcha tekshiruv: «onam<b>ga</b>
    qoʻngʻiroq qilaman» — <em>-ga</em> bor, demak Да́тельный.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Бекзо́д помога́ет ___.</b> (учи́тель)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>учи́телю</strong>. Erkak jins,
    <b>-ь</b> ga tugaydi, demak <b>-ю</b>. Va <em>помога́ть</em> Да́тельный
    oladi — oʻzbekchadagi «oʻqituvchi<b>ga</b> yordam beradi» toʻgʻri
    javobni koʻrsatib turibdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu gapda ikkita toʻldiruvchini toping va kelishiklarini ayting.<br>
     <b>Я дам бра́ту кни́гу.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>бра́ту</strong> — kimga?
    Да́тельный. <strong>кни́гу</strong> — nimani? Вини́тельный. Bunday
    feʼllar (<em>дать, сказа́ть, писа́ть</em>) ikkita toʻldiruvchi
    oladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nega <b>ма́ме</b> ikkita kelishikda bir xil koʻrinadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Ayol jinsida <strong>Да́тельный</strong> va
    <strong>Предло́жный</strong> shakllari bir xil: <em>дать ма́ме</em> va
    <em>о ма́ме</em>. Farqni <b>predlog</b> koʻrsatadi — predlog boʻlsa
    Предло́жный, boʻlmasa Да́тельный.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Он отвеча́ет учи́телю. &nbsp; б) Я помога́ю сестру́.<br>
     в) Афсо́на пи́шет ба́бушке. &nbsp; г) Мне на́до идти́.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б)</strong>. Toʻgʻrisi —
    <b>Я помога́ю сестре́</b>. <em>Помога́ть</em> Да́тельный oladi, ayol
    jinsi esa <b>-е</b>. <em>Сестру́</em> — Вини́тельный shakli va u bu
    feʼl bilan ishlamaydi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>кому́? чему́?</b><span>kimga? nimaga?</span></li>
  <li><b>помога́ть</b><span>yordam bermoq (+ Д.п.)</span></li>
  <li><b>звони́ть</b><span>qoʻngʻiroq qilmoq (+ Д.п.)</span></li>
  <li><b>объясня́ть</b><span>tushuntirmoq</span></li>
  <li><b>отвеча́ть</b><span>javob bermoq</span></li>
  <li><b>меша́ть</b><span>xalaqit bermoq</span></li>
  <li><b>пра́вда</b><span>haqiqat, rost</span></li>
  <li><b>пода́рок</b><span>sovgʻa</span></li>
  <li><b>класс</b><span>sinf</span></li>
  <li><b>пра́здник</b><span>bayram</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Да́тельный = oʻzbekcha <b>-GA</b>. Blokdagi eng aniq moslik.</li>
    <li>Erkak va oʻrta: <b>-у / -ю</b>. Ayol: <b>-е</b>.</li>
    <li>Ayol jinsida Да́тельный va Предло́жный <b>bir xil</b> koʻrinadi —
        farqni predlog koʻrsatadi.</li>
    <li>Olmoshlar: <b>мне, тебе́, ему́, ей, нам, вам, им</b> — PR-27 dan
        beri tanish.</li>
    <li>Feʼllar: <b>дать, сказа́ть, писа́ть, звони́ть, помога́ть,
        отвеча́ть, объясня́ть, меша́ть</b>.</li>
    <li><b>Помога́ть бра́ту</b>, <em>«бра́та»</em> emas — oʻzbekcha
        «-ga» toʻgʻri javobni beradi.</li>
    <li>Ikki toʻldiruvchi: <b>дать кому́ (Д.п.) что (В.п.)</b>.</li>
  </ul>
</div>
""",
    },
]
