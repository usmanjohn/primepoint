# -*- coding: utf-8 -*-
"""Prime Russian — Block D yakuni (47–49).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

Bu uchtasi YANGI tizim bermaydi — ular oltita kelishikni tartibga soladi:
PR-47 — soʻroq soʻzlari. Bitta gʻoya: savol JAVOB kutilayotgan kelishikda
beriladi. Oʻzbekcha soʻroq soʻzlari ham turlanadi (kim, kimning, kimga…),
shuning uchun bu yana bir «sovgʻa» dars.
PR-48 — predloglar xaritasi: qaysi predlog qaysi kelishikni talab qiladi.
Bu blokda tarqoq berilgan maʼlumot bir jadvalga yigʻiladi.
PR-49 — vaqt ifodalari. Bu eng amaliy dars: unda TOʻRTTA kelishik birdan
ishlaydi (в суббо́ту — В.п., в ма́е — П.п., ле́том — Т.п., пе́рвого
января́ — Р.п.), va oʻquvchi nihoyat nega bunday ekanini koʻradi.

Mashqlar:        practice/management/commands/_practice_pr_47_49.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_47_49.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_47_49.py --author=prime
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
        "title": "PR-47: Soʻroq soʻzlarining kelishiklari: кто, что, какой, чей, сколько",
        "category": "russian",
        "order": 47,
        "summary": (
            "Soʻroq soʻzlari ham turlanadi — va bitta oddiy qoida bilan: savol "
            "JAVOB kutilayotgan kelishikda beriladi. Oʻzbekcha «kim, kimning, "
            "kimga» ham xuddi shunday ishlaydi."
        ),
        "stories": ["Игра́ «Два́дцать вопро́сов»"],
        "content": """
<h2>PR-47: Soʻroq soʻzlarining kelishiklari: кто, что, какой, чей, сколько</h2>

<p>PR-15 da siz soʻroq soʻzlarini oʻrgangan edingiz — <em>кто, что, где,
когда́</em>. Oʻshanda ular oʻzgarmas soʻzlar boʻlib koʻringan edi. Endi
maʼlum boʻladiki, ularning bir qismi <b>turlanadi</b>. Va buning ortida
bitta juda oddiy gʻoya bor: <b>savol javob kutilayotgan kelishikda
beriladi</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Кто</b> va <b>что</b> ni oltita kelishikda soʻraysiz</li>
    <li><b>Како́й</b> va <b>чей</b> ni turlaysiz</li>
    <li>Savol va javob bir xil kelishikda boʻlishini koʻrasiz</li>
    <li>Oʻzbekcha soʻroq soʻzlari bilan solishtirasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta qoida</span>
  <span class="pe-chip pe-chip--v">savol</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">javob kutilayotgan kelishik</span>
</div>

<h3>1. Кто va что</h3>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>кто</th><th>что</th><th>Misol</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-case__word">кто</td>
      <td class="pr-case__word">что</td><td class="pr-case__uz">Кто пришёл?</td></tr>
  <tr><td class="pr-case__name">Роди́тельный</td><td class="pr-case__word">кого́</td>
      <td class="pr-case__word">чего́</td><td class="pr-case__uz">У кого́ есть ру́чка?</td></tr>
  <tr><td class="pr-case__name">Да́тельный</td><td class="pr-case__word">кому́</td>
      <td class="pr-case__word">чему́</td><td class="pr-case__uz">Кому́ ты пи́шешь?</td></tr>
  <tr><td class="pr-case__name">Вини́тельный</td><td class="pr-case__word">кого́</td>
      <td class="pr-case__word">что</td><td class="pr-case__uz">Кого́ ты ждёшь?</td></tr>
  <tr><td class="pr-case__name">Твори́тельный</td><td class="pr-case__word">кем</td>
      <td class="pr-case__word">чем</td><td class="pr-case__uz">С кем ты идёшь?</td></tr>
  <tr><td class="pr-case__name">Предло́жный</td><td class="pr-case__word">о ком</td>
      <td class="pr-case__word">о чём</td><td class="pr-case__uz">О чём э́та кни́га?</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bu shakllarni siz <b>allaqachon ishlatgansiz</b> — har bir kelishik darsida
uning savoli berilgan edi: <em>кого́? чего́?</em> (PR-34), <em>кому́?</em>
(PR-37), <em>чем? с кем?</em> (PR-39), <em>о чём?</em> (PR-31). Bugun ular
bitta jadvalga yigʻildi.<br><br>
Va diqqat qiling: <em>кто</em> jonli otlar kabi turlanadi (Р.п. = В.п. —
<em>кого́</em>), <em>что</em> esa jonsizlar kabi (Р.п. <em>чего́</em>,
lekin В.п. <em>что</em>). Yaʼni PR-32 dagi jonlilik qoidasi soʻroq
soʻzlarida ham ishlaydi.</div>

<h3>2. Savol va javob — bir xil kelishikda</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Savol</th><th>Javob</th><th>Kelishik</th></tr>
  <tr><td class="pr-res">Кто э́то?</td><td class="pr-end">Брат.</td>
      <td class="pr-uz">Имени́тельный</td></tr>
  <tr><td class="pr-res">У кого́ есть кни́га?</td><td class="pr-end">У бра́та.</td>
      <td class="pr-uz">Роди́тельный</td></tr>
  <tr><td class="pr-res">Кому́ ты пи́шешь?</td><td class="pr-end">Бра́ту.</td>
      <td class="pr-uz">Да́тельный</td></tr>
  <tr><td class="pr-res">Кого́ ты ждёшь?</td><td class="pr-end">Бра́та.</td>
      <td class="pr-uz">Вини́тельный</td></tr>
  <tr><td class="pr-res">С кем ты идёшь?</td><td class="pr-end">С бра́том.</td>
      <td class="pr-uz">Твори́тельный</td></tr>
  <tr><td class="pr-res">О ком ты ду́маешь?</td><td class="pr-end">О бра́те.</td>
      <td class="pr-uz">Предло́жный</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Chap va oʻng ustunga qarang — <b>savol qanday kelishikda boʻlsa, javob ham
oʻsha kelishikda</b>. Va predlog ham savoldan javobga koʻchadi:
<em><b>У</b> кого́? — <b>У</b> бра́та</em>, <em><b>С</b> кем? — <b>С</b>
бра́том</em>.<br><br>
Bu amalda juda foydali: agar javobning shaklini bilmasangiz, <b>savolni
ayting</b> va uning shaklini koʻchiring. Bu PR-44 dagi sifat hiylasining
kengaytirilgan varianti.</div>

<h3>3. Како́й — sifat kabi turlanadi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kelishik</th><th>erkak</th><th>ayol</th><th>koʻplik</th></tr>
  <tr><td class="pr-uz">Имени́тельный</td><td class="pr-res">како́й</td>
      <td class="pr-res">кака́я</td><td class="pr-res">каки́е</td></tr>
  <tr><td class="pr-uz">Роди́тельный</td><td class="pr-end">како́го</td>
      <td class="pr-end">како́й</td><td class="pr-end">каки́х</td></tr>
  <tr><td class="pr-uz">Да́тельный</td><td class="pr-end">како́му</td>
      <td class="pr-end">како́й</td><td class="pr-end">каки́м</td></tr>
  <tr><td class="pr-uz">Вини́тельный</td><td class="pr-end">како́й / како́го</td>
      <td class="pr-end">каку́ю</td><td class="pr-end">каки́е / каки́х</td></tr>
  <tr><td class="pr-uz">Твори́тельный</td><td class="pr-end">каки́м</td>
      <td class="pr-end">како́й</td><td class="pr-end">каки́ми</td></tr>
  <tr><td class="pr-uz">Предло́жный</td><td class="pr-end">о како́м</td>
      <td class="pr-end">о како́й</td><td class="pr-end">о каки́х</td></tr>
</table></div>

<p>Jadval tanish koʻrinadi — chunki bu <b>aynan sifat naqshi</b> (PR-43,
PR-44). Va ayol jinsida yana oʻsha: <b>како́й</b> toʻrtta kelishikda.</p>

<h3>4. Чей — «kimniki?»</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Jins / son</th><th>Bosh shakl</th><th>Misol</th></tr>
  <tr><td class="pr-uz">erkak</td><td class="pr-res">чей</td>
      <td class="pr-end">Чей э́то дом?</td></tr>
  <tr><td class="pr-uz">ayol</td><td class="pr-res">чья</td>
      <td class="pr-end">Чья э́то кни́га?</td></tr>
  <tr><td class="pr-uz">oʻrta</td><td class="pr-res">чьё</td>
      <td class="pr-end">Чьё э́то окно́?</td></tr>
  <tr><td class="pr-uz">koʻplik</td><td class="pr-res">чьи</td>
      <td class="pr-end">Чьи э́то кни́ги?</td></tr>
</table></div>

<p>Turlangan shakllari <em>мой</em> kabi ishlaydi (PR-42):
<em>чьего́, чьему́, чьим, о чьём, чьей, чью</em>. Amalda esa <b>bosh
kelishik shakllari</b> eng koʻp kerak boʻladi — <em>чей? чья? чьё?
чьи?</em></p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu dars — yana bir «sovgʻa». Oʻzbek tilida soʻroq soʻzlari ham
<b>aynan shunday turlanadi</b>:<br><br>
<em>kim</em> · <em>kim<b>ning</b></em> · <em>kim<b>ga</b></em> ·
<em>kim<b>ni</b></em> · <em>kim<b>da</b></em> · <em>kim<b>dan</b></em><br>
<em>кто</em> · <em>кого́</em> · <em>кому́</em> · <em>кого́</em> ·
<em>о ком</em> · <em>от кого́</em><br><br>
<em>nima</em> · <em>nima<b>ning</b></em> · <em>nima<b>ga</b></em> ·
<em>nima<b>ni</b></em> · <em>nima<b>da</b></em><br>
<em>что</em> · <em>чего́</em> · <em>чему́</em> · <em>что</em> ·
<em>о чём</em><br><br>
Va eng muhimi: oʻzbekchada ham <b>savol va javob bir xil kelishikda</b>
boʻladi. «Kim<b>ga</b> yozding?» — «Aka<b>mga</b>». «Kim<b>ni</b>
kutyapsan?» — «Aka<b>mni</b>». Yaʼni bugungi qoida siz uchun mutlaqo
tabiiy — uni faqat ruscha shakllarga koʻchirish qoladi.</div>

<h3>5. Ско́лько</h3>

<p><em>Ско́лько</em> deyarli har doim bosh shaklda ishlatiladi va undan
keyin <b>Роди́тельный</b> keladi (PR-36):</p>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--v">Ско́лько</span>
     <span class="pe-hl pe-hl--o">книг</span> ты чита́ешь?<br>
     — <span class="pe-hl pe-hl--o">Пять книг</span> в ме́сяц.</p>
  <p class="pe-ex__uz">— Nechta kitob oʻqiysan?<br>— Oyiga besh kitob.</p>
  <p class="pe-ex__why">Savolda ham, javobda ham koʻplik Роди́тельный —
     <em>книг</em>. Qoida bir xil ishlaydi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Кто ты ждёшь?</s></p>
  <p class="pe-good"><b>Кого́</b> ты ждёшь? — javob Вини́тельный'da, savol ham</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кто ты пи́шешь?</s></p>
  <p class="pe-good"><b>Кому́</b> ты пи́шешь? — <em>писа́ть</em> Да́тельный oladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>С кто ты идёшь?</s></p>
  <p class="pe-good"><b>С кем</b> ты идёшь? — predlog kelishikni tanlaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Чей э́то кни́га?</s></p>
  <p class="pe-good"><b>Чья</b> э́то кни́га? — <em>кни́га</em> ayol jinsida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>О что э́та кни́га?</s></p>
  <p class="pe-good"><b>О чём</b> э́та кни́га? — Предло́жный shakli</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu javobga savol tuzing: <b>— Бра́ту.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Кому́?</strong> Javob
    Да́тельный'da (<em>бра́ту</em>), demak savol ham: <em>Кому́ ты
    пи́шешь?</em></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu javobga savol tuzing: <b>— С бра́том.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>С кем?</strong> Predlog ham
    savolga koʻchadi. Javob Твори́тельный'da, demak savol
    <em>с кем</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>кто</b> yoki <b>кого́</b>? &nbsp; <b>___ ты ви́дишь?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Кого́</strong>. <em>Ви́деть</em>
    Вини́тельный oladi, va <em>кто</em> jonli otlar kabi turlanadi — В.п.
    da <em>кого́</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>чей / чья / чьё / чьи</b>? &nbsp; <b>___ э́то ключи́?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Чьи</strong>. <em>Ключи́</em> —
    koʻplik, demak koʻplik shakli. <em>Чей</em> otga jins va son boʻyicha
    moslashadi, xuddi <em>мой</em> kabi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi savol notoʻgʻri?<br>
     а) Кому́ ты звони́шь? &nbsp; б) О чём вы говори́те?<br>
     в) Кто ты ждёшь? &nbsp; г) С кем она́ рабо́тает?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Кого́ ты ждёшь?</b> Javob <em>бра́та</em> boʻlardi, yaʼni
    Вини́тельный — demak savol ham shu kelishikda.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>кого́? кому́? кем?</b><span>kimni? kimga? kim bilan?</span></li>
  <li><b>чего́? чему́? чем?</b><span>nimaning? nimaga? nima bilan?</span></li>
  <li><b>о ком? о чём?</b><span>kim haqida? nima haqida?</span></li>
  <li><b>како́й?</b><span>qanday?</span></li>
  <li><b>чей? чья?</b><span>kimniki?</span></li>
  <li><b>ско́лько?</b><span>qancha?</span></li>
  <li><b>уга́дывать</b><span>topmoq, taxmin qilmoq</span></li>
  <li><b>отве́т</b><span>javob</span></li>
  <li><b>игра́</b><span>oʻyin</span></li>
  <li><b>по о́череди</b><span>navbat bilan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Bitta qoida: <b>savol javob kutilayotgan kelishikda beriladi</b>.</li>
    <li><b>Кто</b> jonli otlar kabi turlanadi (Р.п. = В.п. = кого́),
        <b>что</b> jonsizlar kabi.</li>
    <li>Predlog savoldan javobga koʻchadi: <em>у кого́? — у бра́та</em>.</li>
    <li><b>Како́й</b> sifat kabi turlanadi; ayol jinsida <em>како́й</em>
        toʻrtta kelishikda.</li>
    <li><b>Чей</b> otga jins va son boʻyicha moslashadi:
        <em>чей, чья, чьё, чьи</em>.</li>
    <li><b>Ско́лько</b> dan keyin Роди́тельный.</li>
    <li>Oʻzbekcha soʻroq soʻzlari ham turlanadi (<em>kim, kimning,
        kimga…</em>) — bu qoida siz uchun tabiiy.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-48: Predlog xaritasi: qaysi predlog qaysi kelishikni talab qiladi",
        "category": "russian",
        "order": 48,
        "summary": (
            "Yigirma dars davomida predloglar bittalab berildi. Bugun ular bitta "
            "xaritaga yigʻiladi — va maʼlum boʻladiki, ular tasodifiy emas: har "
            "bir kelishikning oʻz predloglari bor."
        ),
        "stories": ["Как я потеря́лся в метро́"],
        "content": """
<h2>PR-48: Predlog xaritasi: qaysi predlog qaysi kelishikni talab qiladi</h2>

<p>Rus tilida <b>predlog kelishikni tanlaydi</b> — buni siz PR-29 dan beri
bilasiz. Lekin shu paytgacha predloglar bittalab, oʻz darsida berildi:
<em>в</em> va <em>на</em> PR-30 da, <em>о</em> PR-31 da, <em>из</em> va
<em>от</em> PR-35 da, <em>к</em> va <em>по</em> PR-38 da, <em>над</em> va
<em>под</em> PR-40 da. Bugun ularni <b>bitta xaritaga</b> yigʻamiz. Yangi
hech narsa yoʻq — faqat tartib.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Butun predlog xaritasini bir joyda koʻrasiz</li>
    <li>Ikki kelishik oladigan predloglarni ajratasiz</li>
    <li>Antonim juftliklarni topasiz: <b>в ↔ из</b>, <b>к ↔ от</b></li>
    <li>Yodlash strategiyasini olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Asosiy qoida</span>
  <span class="pe-chip pe-chip--v">predlog</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">kelishikni tanlaydi</span>
</div>

<h3>1. Xarita</h3>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Predloglar</th><th>Misol</th></tr>
  <tr><td class="pr-case__name">Роди́тельный</td>
      <td class="pr-case__q">из · с · от · до · у · без · для · о́коло · по́сле</td>
      <td class="pr-case__uz">из шко́лы · без са́хара</td></tr>
  <tr><td class="pr-case__name">Да́тельный</td>
      <td class="pr-case__q">к · по</td>
      <td class="pr-case__uz">к бра́ту · по у́лице</td></tr>
  <tr><td class="pr-case__name">Вини́тельный</td>
      <td class="pr-case__q">в · на · че́рез · за</td>
      <td class="pr-case__uz">в шко́лу · че́рез мост</td></tr>
  <tr><td class="pr-case__name">Твори́тельный</td>
      <td class="pr-case__q">с · над · под · за · пе́ред · ме́жду · ря́дом с</td>
      <td class="pr-case__uz">с бра́том · под столо́м</td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">Предло́жный</td>
      <td class="pr-case__q">в · на · о (об, обо) · при</td>
      <td class="pr-case__uz">в шко́ле · о кни́ге</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Jadvalda ikkita narsani payqang.<br><br>
1. <b>Роди́тельный eng koʻp predlog oladi</b> — toʻqqiztasi. Shuning uchun
u rus tilidagi eng koʻp uchraydigan kelishik. Agar predlogni bilmasangiz
va taxmin qilish kerak boʻlsa — Роди́тельный eng ehtimolli javob.<br><br>
2. <b>Да́тельный faqat ikkita</b> — <em>к</em> va <em>по</em>. Bu roʻyxatni
yodlash bir daqiqa vaqt oladi.<br><br>
Va <b>Имени́тельный</b> jadvalda yoʻq: bosh kelishik <b>hech qachon</b>
predlog bilan kelmaydi. Bu ham foydali qoida.</div>

<h3>2. Ikki kelishik oladigan predloglar</h3>

<p>Uchta predlog ikki xil ishlaydi — va farqni <b>maʼno</b> hal qiladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Predlog</th><th>Qayerda? (harakat yoʻq)</th><th>Qayerga? (harakat bor)</th></tr>
  <tr><td class="pr-res">в</td><td class="pr-uz">в шко́л<b>е</b> — Предло́жный</td>
      <td class="pr-end">в шко́л<b>у</b> — Вини́тельный</td></tr>
  <tr><td class="pr-res">на</td><td class="pr-uz">на рабо́т<b>е</b> — Предло́жный</td>
      <td class="pr-end">на рабо́т<b>у</b> — Вини́тельный</td></tr>
  <tr><td class="pr-res">за</td><td class="pr-uz">за до́м<b>ом</b> — Твори́тельный</td>
      <td class="pr-end">за дом — Вини́тельный</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Tanlov <b>harakat bor-yoʻqligiga</b> qarab qilinadi:<br>
<b>Harakat yoʻq</b> (turibman, yashayman, ishlayman) → joy kelishigi.<br>
<b>Harakat bor</b> (ketyapman, qoʻyyapman) → Вини́тельный.<br>
Bu qoidani feʼldan bilib olasiz: <em>быть, жить, рабо́тать, стоя́ть,
лежа́ть</em> — joy. <em>Идти́, е́хать, класть</em> — harakat.</div>

<h3>3. Antonim juftliklar</h3>

<p>Predloglarni <b>yakka</b> emas, <b>juft</b> qilib yodlang — shunda ular
ikki barobar tez oʻtiradi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Qayerga?</th><th>Qayerdan?</th><th>Izoh</th></tr>
  <tr><td class="pr-res">в шко́лу</td><td class="pr-end">из шко́лы</td>
      <td class="pr-uz">ichiga ↔ ichidan</td></tr>
  <tr><td class="pr-res">на рабо́ту</td><td class="pr-end">с рабо́ты</td>
      <td class="pr-uz">ustiga ↔ ustidan</td></tr>
  <tr><td class="pr-res">к врачу́</td><td class="pr-end">от врача́</td>
      <td class="pr-uz">odam tomon ↔ odamdan</td></tr>
  <tr><td class="pr-res">до шко́лы</td><td class="pr-end">по́сле уро́ка</td>
      <td class="pr-uz">joy chegarasi ↔ vaqt chegarasi</td></tr>
</table></div>

<p>Uchta juftlik — uchta qoida. Va ularning hammasi PR-30 dagi
<b>В/НА roʻyxati</b>ga tayanadi: soʻz <em>в</em> olsa, «dan» uchun
<em>из</em>; <em>на</em> olsa — <em>с</em>.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu xaritani oʻzbekcha bilan solishtirish foydali, chunki ikkala tilda ham
<b>bir xil ish</b> qilinadi — faqat boshqa vosita bilan:<br><br>
Oʻzbekchada bu maʼnolar <b>qoʻshimcha</b> yoki <b>koʻmakchi</b> bilan
beriladi va ular soʻzdan <b>keyin</b> turadi:
<em>maktab<b>ga</b></em>, <em>maktab<b>dan</b></em>, <em>stol
<b>ustida</b></em>, <em>uy <b>oldida</b></em>.<br><br>
Ruschada esa <b>predlog</b> soʻzdan <b>oldin</b> turadi va <b>ot ham
oʻzgaradi</b>: <em><b>в</b> шко́л<b>у</b></em>, <em><b>из</b>
шко́л<b>ы</b></em>, <em><b>на</b> стол<b>е́</b></em>, <em><b>пе́ред</b>
до́м<b>ом</b></em>.<br><br>
Yaʼni ruscha maʼlumotni <b>ikki joyda</b> koʻrsatadi — predlogda va
qoʻshimchada. Bu koʻproq ish, lekin xato qilish qiyinroq: agar ikkalasi
mos kelmasa, xato darrov koʻrinadi.</div>

<h3>4. Yodlash strategiyasi</h3>

<ol class="pe-steps">
  <li><b>Predlogni yakka yodlamang</b> — uni butun ibora bilan yodlang:
      <em>в шко́ле</em>, <em>на рабо́ту</em>, <em>под столо́м</em>.</li>
  <li><b>Juftlab yodlang</b>: <em>в ↔ из</em>, <em>на ↔ с</em>,
      <em>к ↔ от</em>.</li>
  <li><b>Da'telniyni alohida yodlang</b> — u faqat ikkita:
      <em>к</em> va <em>по</em>.</li>
  <li><b>Qolganda Роди́тельный</b> — u eng koʻp predlog oladi.</li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__ru">Я е́ду <span class="pe-hl pe-hl--o">на рабо́ту</span>
     <span class="pe-hl pe-hl--adv">на метро́</span>, а
     <span class="pe-hl pe-hl--adv">по́сле рабо́ты</span> иду́
     <span class="pe-hl pe-hl--adv">пешко́м</span>.</p>
  <p class="pe-ex__uz">Ishga metroda boraman, ishdan keyin esa piyoda
     yuraman.</p>
  <p class="pe-ex__why">Bitta gapda uchta predlog: <em>на рабо́ту</em>
     (В.п., manzil), <em>на метро́</em> (П.п., vosita — <em>метро́</em>
     turlanmaydi), <em>по́сле рабо́ты</em> (Р.п., vaqt).</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́ к шко́лу.</s></p>
  <p class="pe-good">Я иду́ <b>в шко́лу</b> — joy uchun В, odam uchun К</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я е́ду из рабо́ты.</s></p>
  <p class="pe-good">Я е́ду <b>с рабо́ты</b> — <em>на рабо́те</em> → demak С</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кни́га под стол.</s></p>
  <p class="pe-good">Кни́га <b>под столо́м</b> — harakat yoʻq, demak Твори́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я живу́ в го́род.</s></p>
  <p class="pe-good">Я живу́ <b>в го́роде</b> — <em>жить</em> harakat emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>по у́лицу</s></p>
  <p class="pe-good"><b>по у́лице</b> — ПО har doim Да́тельный oladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>По</b> qaysi kelishikni oladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Да́тельный</strong>. Va
    Да́тельный faqat ikkita predlog oladi: <em>к</em> va <em>по</em>. Bu
    roʻyxatni yodlash oson.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu ikki iboraning farqi nima?<br>
     <b>за до́мом · за дом</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><em>За до́мом</em> — <strong>uy
    orqasida</strong> (harakat yoʻq, Твори́тельный). <em>За дом</em> —
    <strong>uy orqasiga</strong> (harakat bor, Вини́тельный). Bir xil
    predlog, ikki kelishik.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Qaysi kelishik hech qachon predlog bilan kelmaydi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Имени́тельный</strong> (bosh
    kelishik). U gapning egasi, va ega hech qachon predlog olmaydi. Aksincha
    — <b>Предло́жный</b> hech qachon predlogSIZ kelmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu iboraning juftini toping: <b>к врачу́</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>от врача́</strong>. <em>К</em>
    (Да́тельный) va <em>от</em> (Роди́тельный) — antonim juftlik: odam
    tomon ↔ odamdan.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gapda predlog va kelishik <b>mos kelmaydi</b>?<br>
     а) Я живу́ в го́роде. &nbsp; б) Я иду́ в го́род.<br>
     в) Кни́га лежи́т под стол. &nbsp; г) Мы идём к врачу́.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Кни́га лежи́т под столо́м</b>. <em>Лежа́ть</em> harakat emas, demak
    Твори́тельный kerak. <em>Под стол</em> faqat harakat bilan boʻlardi:
    <em>Я кладу́ кни́гу под стол</em>.</p><p>Qolgan uchtasi toʻgʻri:
    <em>живу́ в го́роде</em> (harakat yoʻq → П.п.), <em>иду́ в го́род</em>
    (harakat bor → В.п.), <em>к врачу́</em> (К har doim Д.п.).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>предло́г</b><span>predlog</span></li>
  <li><b>че́рез</b><span>orqali, -dan (kesib oʻtib)</span></li>
  <li><b>ме́жду</b><span>orasida</span></li>
  <li><b>ря́дом с</b><span>yonida</span></li>
  <li><b>метро́</b><span>metro (turlanmaydi)</span></li>
  <li><b>пешко́м</b><span>piyoda</span></li>
  <li><b>ста́нция</b><span>bekat, stansiya</span></li>
  <li><b>вы́ход</b><span>chiqish</span></li>
  <li><b>потеря́ться</b><span>adashmoq</span></li>
  <li><b>наприме́р</b><span>masalan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Predlog kelishikni tanlaydi</b> — bu butun tizimning kaliti.</li>
    <li><b>Роди́тельный</b> eng koʻp predlog oladi (toʻqqizta),
        <b>Да́тельный</b> eng kam (ikkita: <em>к, по</em>).</li>
    <li><b>Имени́тельный</b> hech qachon predlog olmaydi;
        <b>Предло́жный</b> hech qachon predlogsiz kelmaydi.</li>
    <li>Uchta predlog ikki kelishik oladi: <b>в, на, за</b> — farqni
        <b>harakat</b> hal qiladi.</li>
    <li>Juftlab yodlang: <b>в ↔ из</b>, <b>на ↔ с</b>, <b>к ↔ от</b>.</li>
    <li>Predlogni yakka emas, <b>butun ibora</b> bilan yodlang.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-49: Sonlarning kelishigi va vaqt ifodalari: в понедельник, в мае, в 2026 году",
        "category": "russian",
        "order": 49,
        "summary": (
            "Kursdagi eng amaliy dars: vaqt haqida gapirish. Va u ayni paytda "
            "eng yaxshi takror — chunki vaqt ifodalarida TOʻRTTA kelishik birdan "
            "ishlaydi."
        ),
        "stories": ["Календа́рь Ни́ны"],
        "content": """
<h2>PR-49: Sonlarning kelishigi va vaqt ifodalari: в понедельник, в мае, в 2026 году</h2>

<p>Bu dars ikki barobar foydali. Birinchidan, u <b>eng amaliy</b>: vaqt
haqida gapirish har kuni kerak. Ikkinchidan, u <b>eng yaxshi takror</b> —
chunki rus tilida vaqt ifodalarida <b>toʻrtta kelishik birdan</b> ishlaydi,
va nihoyat maʼlum boʻladiki, bu tasodifiy emas.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Hafta kunlarini aytasiz: <b>в понеде́льник</b></li>
    <li>Oy va yilni aytasiz: <b>в ма́е, в 2026 году́</b></li>
    <li>Fasl va kun qismini aytasiz: <b>ле́том, у́тром</b></li>
    <li>Soatni aytasiz: <b>в два часа́</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrtta kelishik</span>
  <span class="pe-chip pe-chip--o">в суббо́ту</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">в ма́е</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">ле́том</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--adv">пе́рвого ма́я</span>
</div>

<h3>1. Xarita — qaysi vaqt qaysi kelishikda</h3>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Nima</th><th>Qolip</th><th>Kelishik</th><th>Misol</th></tr>
  <tr><td class="pr-case__name">Hafta kuni</td><td class="pr-case__q">в + В.п.</td>
      <td class="pr-case__word">Вини́тельный</td>
      <td class="pr-case__uz">в понеде́льник, в суббо́ту</td></tr>
  <tr><td class="pr-case__name">Oy</td><td class="pr-case__q">в + П.п.</td>
      <td class="pr-case__word">Предло́жный</td>
      <td class="pr-case__uz">в ма́е, в январе́</td></tr>
  <tr><td class="pr-case__name">Yil</td><td class="pr-case__q">в + П.п.</td>
      <td class="pr-case__word">Предло́жный</td>
      <td class="pr-case__uz">в 2026 году́</td></tr>
  <tr><td class="pr-case__name">Fasl, kun qismi</td><td class="pr-case__q">predlogsiz</td>
      <td class="pr-case__word">Твори́тельный</td>
      <td class="pr-case__uz">ле́том, у́тром</td></tr>
  <tr><td class="pr-case__name">Sana</td><td class="pr-case__q">predlogsiz</td>
      <td class="pr-case__word">Роди́тельный</td>
      <td class="pr-case__uz">пе́рвого ма́я</td></tr>
  <tr><td class="pr-case__name">Soat</td><td class="pr-case__q">в + В.п.</td>
      <td class="pr-case__word">Вини́тельный</td>
      <td class="pr-case__uz">в два часа́</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Jadval katta koʻrinadi, lekin unda <b>mantiq bor</b>:<br>
<b>Qisqa vaqt</b> (kun, soat) — <em>в</em> + Вини́тельный. Yaʼni «shu
nuqtaga» degandek, xuddi manzil kabi.<br>
<b>Uzun vaqt</b> (oy, yil) — <em>в</em> + Предло́жный. Yaʼni «shu
ichida», xuddi joy kabi.<br>
<b>Takrorlanadigan vaqt</b> (fasl, kun qismi) — Твори́тельный,
predlogsiz. Bu «shu vaqt bilan» degandek.<br><br>
Yaʼni rus tili vaqtni <b>joy kabi</b> koʻradi: kichkina joyga kirasiz
(В.п.), katta joy ichida turasiz (П.п.).</div>

<h3>2. Hafta kunlari</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kun</th><th>«…kuni»</th><th>Kun</th><th>«…kuni»</th></tr>
  <tr><td class="pr-res">понеде́льник</td><td class="pr-end">в понеде́льник</td>
      <td class="pr-res">пя́тница</td><td class="pr-end">в пя́тницу</td></tr>
  <tr><td class="pr-res">вто́рник</td><td class="pr-end">во вто́рник</td>
      <td class="pr-res">суббо́та</td><td class="pr-end">в суббо́ту</td></tr>
  <tr><td class="pr-res">среда́</td><td class="pr-end">в сре́ду</td>
      <td class="pr-res">воскресе́нье</td><td class="pr-end">в воскресе́нье</td></tr>
  <tr><td class="pr-res">четве́рг</td><td class="pr-end">в четве́рг</td>
      <td class="pr-uz">—</td><td class="pr-uz">—</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Ikkita joyda diqqat kerak:<br>
<b>Во вто́рник</b> — <em>в</em> emas, <b>во</b>. Sababi tanish: keyingi
soʻz ikki undosh bilan boshlanadi (<em>вт-</em>), shuning uchun predlogga
unli qoʻshiladi — xuddi <em>во дворе́</em>, <em>со мной</em> kabi.<br>
<b>В сре́ду</b> — urgʻu <b>koʻchadi</b>: <em>сред<b>а́</b> → в
<b>сре́</b>ду</em>. Bu yagona kun, unda urgʻu joyini
almashtiradi.</div>

<h3>3. Oylar va yillar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Oy</th><th>«…da»</th><th>Oy</th><th>«…da»</th></tr>
  <tr><td class="pr-res">янва́рь</td><td class="pr-end">в январе́</td>
      <td class="pr-res">ию́ль</td><td class="pr-end">в ию́ле</td></tr>
  <tr><td class="pr-res">февра́ль</td><td class="pr-end">в феврале́</td>
      <td class="pr-res">а́вгуст</td><td class="pr-end">в а́вгусте</td></tr>
  <tr><td class="pr-res">март</td><td class="pr-end">в ма́рте</td>
      <td class="pr-res">сентя́брь</td><td class="pr-end">в сентябре́</td></tr>
  <tr><td class="pr-res">апре́ль</td><td class="pr-end">в апре́ле</td>
      <td class="pr-res">октя́брь</td><td class="pr-end">в октябре́</td></tr>
  <tr><td class="pr-res">май</td><td class="pr-end">в ма́е</td>
      <td class="pr-res">ноя́брь</td><td class="pr-end">в ноябре́</td></tr>
  <tr><td class="pr-res">ию́нь</td><td class="pr-end">в ию́не</td>
      <td class="pr-res">дека́брь</td><td class="pr-end">в декабре́</td></tr>
</table></div>

<p><b>Yil</b> ham Предло́жный oladi, lekin bitta oʻziga xosligi bor:
<em>год → в год<b>у́</b></em> — bu PR-30 dagi <b>-У́</b> roʻyxatidan
(<em>в лесу́, на полу́</em>). Shuning uchun: <b>в 2026 году́</b>.</p>

<h3>4. Fasllar va kun qismlari — Твори́тельный</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Fasl</th><th>«…da»</th><th>Kun qismi</th><th>«…da»</th></tr>
  <tr><td class="pr-res">зима́</td><td class="pr-end">зимо́й</td>
      <td class="pr-res">у́тро</td><td class="pr-end">у́тром</td></tr>
  <tr><td class="pr-res">весна́</td><td class="pr-end">весно́й</td>
      <td class="pr-res">день</td><td class="pr-end">днём</td></tr>
  <tr><td class="pr-res">ле́то</td><td class="pr-end">ле́том</td>
      <td class="pr-res">ве́чер</td><td class="pr-end">ве́чером</td></tr>
  <tr><td class="pr-res">о́сень</td><td class="pr-end">о́сенью</td>
      <td class="pr-res">ночь</td><td class="pr-end">но́чью</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Bu shakllarda <b>predlog yoʻq</b> — faqat Твори́тельный qoʻshimchasi.
<em>Ле́том, у́тром, ве́чером, зимо́й</em> — hammasi
<b>-ОМ / -ОЙ / -ЬЮ</b>.<br>
Siz bu soʻzlarni PR-20 dan beri ishlatasiz (<em>Ве́чером — магази́н</em>),
lekin faqat endi nega bunday ekanini bilasiz: bular <b>Твори́тельный
padejida qotib qolgan ravishlar</b>.</div>

<h3>5. Soat va sana</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--v">Ско́лько
     вре́мени</span>?<br>
     — <span class="pe-hl pe-hl--o">Два часа́</span>. Уро́к
     <span class="pe-hl pe-hl--adv">в три часа́</span>.</p>
  <p class="pe-ex__uz">— Soat necha?<br>— Soat ikki. Dars soat uchda.</p>
  <p class="pe-ex__why">Vaqtni aytish — bosh kelishik (<em>два часа́</em>).
     «Soat nechada» — <em>в</em> + Вини́тельный. Va <em>час</em> PR-36
     qoidasi boʻyicha oʻzgaradi: <em>час, два часа́, пять часо́в</em>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Како́е сего́дня число́?<br>
     — <span class="pe-hl pe-hl--s">Пе́рвое ма́я</span>. А экза́мен
     <span class="pe-hl pe-hl--adv">пя́того ма́я</span>.</p>
  <p class="pe-ex__uz">— Bugun nechanchi sana?<br>— Birinchi may. Imtihon
     esa beshinchi mayda.</p>
  <p class="pe-ex__why">Sana aytilsa — bosh kelishik (<em>пе́рвое</em>).
     «Qaysi kuni» — <b>Роди́тельный</b> (<em>пя́того</em>). Oy esa har doim
     Роди́тельный'da: <em>ма́я</em>.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada vaqt ifodalari ancha oddiy — deyarli hammasi <b>-DA</b>
bilan:<br>
<em>dushanba<b>da</b></em> · <em>may<b>da</b></em> · <em>yoz<b>da</b></em> ·
<em>ertalab</em> · <em>soat ikki<b>da</b></em><br><br>
Ruschada esa <b>toʻrtta boshqa qurilish</b>:<br>
<em>в понеде́льник</em> (В.п.) · <em>в ма́е</em> (П.п.) ·
<em>ле́том</em> (Т.п.) · <em>пя́того ма́я</em> (Р.п.)<br><br>
Bu koʻproq ish, lekin bir narsa yordam beradi: <b>bu iboralar yopiq
roʻyxat</b>. Hafta kunlari — yettita. Oylar — oʻn ikkita. Fasllar —
toʻrtta. Kun qismlari — toʻrtta. Yigirma yettita ibora, tamom. Ularni
qoida sifatida emas, <b>tayyor boʻlak</b> sifatida yodlang — xuddi
oʻzbekchadagi «ertalab» soʻzi kabi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>в понеде́льнике</s></p>
  <p class="pe-good"><b>в понеде́льник</b> — hafta kuni Вини́тельный oladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>в май</s></p>
  <p class="pe-good"><b>в ма́е</b> — oy Предло́жный oladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>в ле́те</s></p>
  <p class="pe-good"><b>ле́том</b> — fasl predlogsiz, Твори́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>в 2026 го́де</s></p>
  <p class="pe-good">в 2026 <b>году́</b> — <em>год</em> <b>-У́</b> roʻyxatida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>в вто́рник</s></p>
  <p class="pe-good"><b>во</b> вто́рник — ikki undoshdan oldin predlogga unli qoʻshiladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Экза́мен ___.</b> (суббо́та)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в суббо́ту</strong>. Hafta kuni —
    <em>в</em> + Вини́тельный, ayol jinsi <b>-у</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Мы е́дем в дере́вню ___.</b> (ию́ль)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в ию́ле</strong>. Oy —
    <em>в</em> + Предло́жный. Solishtiring: hafta kuni Вини́тельный
    olardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>___ здесь о́чень хо́лодно.</b> (зима́)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Зимо́й</strong> — predlogsiz,
    Твори́тельный. Fasllar va kun qismlari shu qurilishda:
    <em>ле́том, у́тром, ве́чером, но́чью</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga: <b>Он роди́лся в 2001 ___.</b> (год)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>году́</strong>. <em>Год</em> —
    PR-30 dagi <b>-У́</b> roʻyxatidan, xuddi <em>в лесу́</em>,
    <em>на полу́</em> kabi. <em>«В го́де»</em> — xato.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi qatorda hammasi toʻgʻri?<br>
     а) в понеде́льник · в ма́е · ле́том<br>
     б) в понеде́льнике · в ма́е · ле́том<br>
     в) в понеде́льник · в май · в ле́те<br>
     г) в понеде́льник · в ма́е · в ле́том</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>а)</strong>. Uchta boshqa
    qurilish: hafta kuni <b>В.п.</b>, oy <b>П.п.</b>, fasl esa
    <b>predlogsiz Т.п.</b></p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>в понеде́льник</b><span>dushanba kuni</span></li>
  <li><b>во вто́рник</b><span>seshanba kuni</span></li>
  <li><b>в ма́е</b><span>mayda</span></li>
  <li><b>в году́</b><span>yilda</span></li>
  <li><b>ле́том · зимо́й</b><span>yozda · qishda</span></li>
  <li><b>у́тром · но́чью</b><span>ertalab · kechasi</span></li>
  <li><b>число́</b><span>sana</span></li>
  <li><b>календа́рь</b><span>kalendar</span></li>
  <li><b>неде́ля</b><span>hafta</span></li>
  <li><b>ме́сяц</b><span>oy</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Hafta kuni</b> — <em>в</em> + Вини́тельный:
        <b>в понеде́льник</b>.</li>
    <li><b>Oy va yil</b> — <em>в</em> + Предло́жный: <b>в ма́е,
        в 2026 году́</b>.</li>
    <li><b>Fasl va kun qismi</b> — predlogsiz Твори́тельный:
        <b>ле́том, у́тром</b>.</li>
    <li><b>Sana</b> — Роди́тельный: <b>пя́того ма́я</b>.</li>
    <li>Mantiq: qisqa vaqt — В.п. (nuqtaga), uzun vaqt — П.п. (ichida).</li>
    <li><b>Во вто́рник</b> va <b>в сре́ду</b> (urgʻu koʻchadi) — ikkita
        diqqat joyi.</li>
    <li>Bu iboralar <b>yopiq roʻyxat</b> — yigirma yettita. Ularni tayyor
        boʻlak sifatida yodlang.</li>
  </ul>
</div>
""",
    },
]
