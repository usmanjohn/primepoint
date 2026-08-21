# -*- coding: utf-8 -*-
"""Prime Russian — Block C davomi (21–23).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-21 II tuslanishni beradi, PR-22 notoʻgʻri feʼllarni, PR-23 esa oʻtgan
zamonni — shu dars bilan matnlar nihoyat «kecha» haqida gapira oladi.

Urgʻu siyosati: PR-21 dan boshlab faqat YANGI va urgʻusi KOʻCHADIGAN
soʻzlarga belgi qoʻyiladi (STYLE_GUIDE 4-boʻlim).

Mashqlar:        practice/management/commands/_practice_pr_21_23.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_21_23.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_21_23.py --author=prime
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
        "title": "PR-21: II tuslanish: говорить, смотреть, любить (-ю, -ишь, -ит, -им, -ите, -ят)",
        "category": "russian",
        "order": 21,
        "summary": (
            "Ikkinchi tuslanishning oltita qoʻshimchasi, «я» shaklidagi harf "
            "almashinuvi (люблю́, хожу́) va feʼl qaysi tuslanishda ekanini "
            "aniqlashning ishonchli yoʻli."
        ),
        "stories": ["Я говорю́ на трёх языка́х"],
        "content": """
<h2>PR-21: II tuslanish: говорить, смотреть, любить (-ю, -ишь, -ит, -им, -ите, -ят)</h2>

<p>Kecha siz bitta naqshni oʻrgandingiz va oʻnlab feʼlni ishlata boshladingiz.
Bugun ikkinchisi keladi — va shundan keyin sizda <b>butun rus feʼl tizimi</b>
boʻladi. Chunki rus tilida tuslanish ikkitagina. Ikkitasini bilgan odam har
qanday feʼlni tuslay oladi. Yangi qoʻshimchalarni yodlashdan ham muhimroq bir
narsa bor: feʼl <b>qaysi</b> tuslanishda ekanini bilish. Bugun buni ham
oʻrganasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>II tuslanishning oltita qoʻshimchasini yodlaysiz</li>
    <li>«Я» shaklidagi harf almashinuvini tushunasiz: люблю́, хожу́, ви́жу</li>
    <li>Ж, Ш, Щ, Ч dan keyin <b>-ят</b> emas, <b>-ат</b> yozishni bilasiz</li>
    <li>Feʼlning qaysi tuslanishda ekanini aniqlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">II tuslanish</span>
  <span class="pe-chip pe-chip--s">говор</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">ю · ишь · ит · им · ите · ят</span>
</div>

<h3>1. Oltita qoʻshimcha — endi И qatori</h3>

<p>Kechagi naqshni eslang: <em>-ешь, -ет, -ем, -ете</em> — hammasida <b>Е</b> bor
edi. Bugungisi bir tomchi ham qiyin emas, chunki u aynan shu joyda <b>Е</b> ni
<b>И</b> ga almashtiradi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>я</td><td class="pr-stem">говор</td><td class="pr-end">ю́</td>
      <td class="pr-res">говорю́</td><td class="pr-uz">gapiraman</td></tr>
  <tr><td>ты</td><td class="pr-stem">говор</td><td class="pr-end">и́шь</td>
      <td class="pr-res">говори́шь</td><td class="pr-uz">gapirasan</td></tr>
  <tr><td>он / она́</td><td class="pr-stem">говор</td><td class="pr-end">и́т</td>
      <td class="pr-res">говори́т</td><td class="pr-uz">gapiradi</td></tr>
  <tr><td>мы</td><td class="pr-stem">говор</td><td class="pr-end">и́м</td>
      <td class="pr-res">говори́м</td><td class="pr-uz">gapiramiz</td></tr>
  <tr><td>вы</td><td class="pr-stem">говор</td><td class="pr-end">и́те</td>
      <td class="pr-res">говори́те</td><td class="pr-uz">gapirasiz</td></tr>
  <tr><td>они́</td><td class="pr-stem">говор</td><td class="pr-end">я́т</td>
      <td class="pr-res">говоря́т</td><td class="pr-uz">gapiradilar</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Ikkala tuslanishni <b>yonma-yon</b> yodlang, alohida emas. Farq atigi ikki
joyda:<br>
<b>I:</b> -ю, <b>-ешь -ет -ем -ете</b>, -ют &nbsp;→&nbsp; «<b>Е</b> qatori,
ikki tomonida <b>Ю</b>»<br>
<b>II:</b> -ю, <b>-ишь -ит -им -ите</b>, -ят &nbsp;→&nbsp; «<b>И</b> qatori,
oxirida <b>Я</b>»<br>
Yaʼni: oʻrtadagi unli <b>Е</b> mi yoki <b>И</b> mi, va oxirgisi <b>-ЮТ</b> mi
yoki <b>-ЯТ</b> mi. «Я» shakli ikkalasida ham bir xil: <b>-ю</b>.</div>

<h3>2. Oʻzakni topish — bu safar ikki harf ketadi</h3>

<p>I tuslanishda infinitivdan faqat <b>-ть</b> ni olib tashlagandik. II
tuslanishda undan oldingi <b>unli ham ketadi</b>:</p>

<ol class="pe-steps">
  <li>Infinitivni oling: <b>говори́ть</b>.</li>
  <li><b>-ить</b> ni olib tashlang (uch harf emas — <b>-и-ть</b>): <b>говор-</b>.</li>
  <li>Oʻzakka oltita qoʻshimchani qoʻshing.</li>
</ol>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>я</th><th>ты</th><th>он / она́</th><th>они́</th></tr>
  <tr><td class="pr-res">говори́ть</td><td class="pr-end">говорю́</td>
      <td class="pr-end">говори́шь</td><td class="pr-end">говори́т</td>
      <td class="pr-end">говоря́т</td></tr>
  <tr><td class="pr-res">смотре́ть</td><td class="pr-end">смотрю́</td>
      <td class="pr-end">смо́тришь</td><td class="pr-end">смо́трит</td>
      <td class="pr-end">смо́трят</td></tr>
  <tr><td class="pr-res">звони́ть</td><td class="pr-end">звоню́</td>
      <td class="pr-end">звони́шь</td><td class="pr-end">звони́т</td>
      <td class="pr-end">звоня́т</td></tr>
  <tr><td class="pr-res">по́мнить</td><td class="pr-end">по́мню</td>
      <td class="pr-end">по́мнишь</td><td class="pr-end">по́мнит</td>
      <td class="pr-end">по́мнят</td></tr>
  <tr><td class="pr-res">стро́ить</td><td class="pr-end">стро́ю</td>
      <td class="pr-end">стро́ишь</td><td class="pr-end">стро́ит</td>
      <td class="pr-end">стро́ят</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbek tilida <b>bitta</b> tuslanish bor: <em>oʻqi-y-man, ishla-y-man,
gapir-a-man</em> — hammasi bir xil ishlaydi. Rus tilida esa feʼlni koʻrganda
<b>qaysi guruhda ekanini bilib olish kerak</b>, xuddi otni koʻrganda uning
jinsini bilish kerak boʻlgani kabi. Bu — Prime Russian'dagi ikkinchi
«yodlanadigan xususiyat». Yaxshi xabar: guruh ikkitagina va ularning 90 foizini
infinitivdan koʻrib turasiz.</div>

<h3>3. «Я» shaklidagi harf almashinuvi</h3>

<p>Endi darsning eng qiziq joyi. Baʼzi feʼllarda <b>faqat «я» shaklida</b> oʻzakning
oxirgi undoshi oʻzgaradi. Qolgan beshta shaklda hech narsa boʻlmaydi. Buni
<b>чередова́ние</b> (harf almashinuvi) deyiladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Almashinuv</th><th>Infinitiv</th><th>я</th><th>ты</th><th>они́</th></tr>
  <tr><td class="pr-uz">б → бл</td><td class="pr-res">люби́ть</td>
      <td class="pr-end">люблю́</td><td class="pr-end">лю́бишь</td>
      <td class="pr-end">лю́бят</td></tr>
  <tr><td class="pr-uz">в → вл</td><td class="pr-res">гото́вить</td>
      <td class="pr-end">гото́влю</td><td class="pr-end">гото́вишь</td>
      <td class="pr-end">гото́вят</td></tr>
  <tr><td class="pr-uz">п → пл</td><td class="pr-res">спать</td>
      <td class="pr-end">сплю</td><td class="pr-end">спишь</td>
      <td class="pr-end">спят</td></tr>
  <tr><td class="pr-uz">д → ж</td><td class="pr-res">ходи́ть</td>
      <td class="pr-end">хожу́</td><td class="pr-end">хо́дишь</td>
      <td class="pr-end">хо́дят</td></tr>
  <tr><td class="pr-uz">д → ж</td><td class="pr-res">ви́деть</td>
      <td class="pr-end">ви́жу</td><td class="pr-end">ви́дишь</td>
      <td class="pr-end">ви́дят</td></tr>
  <tr><td class="pr-uz">с → ш</td><td class="pr-res">проси́ть</td>
      <td class="pr-end">прошу́</td><td class="pr-end">про́сишь</td>
      <td class="pr-end">про́сят</td></tr>
  <tr><td class="pr-uz">т → ч</td><td class="pr-res">плати́ть</td>
      <td class="pr-end">плачу́</td><td class="pr-end">пла́тишь</td>
      <td class="pr-end">пла́тят</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Ikkita narsani yodda tuting va bu jadval oʻz-oʻzidan esda qoladi:<br>
1. <b>Б, В, М, П, Ф</b> — «lab undoshlari» — «я» shaklida oʻziga <b>Л</b> qoʻshib
oladi: <em>лю<b>бл</b>ю́, гото́<b>вл</b>ю, с<b>пл</b>ю</em>.<br>
2. <b>Д, С, Т, З</b> shivirlovchiga aylanadi: <b>д→ж</b>, <b>с→ш</b>,
<b>т→ч</b>, <b>з→ж</b>.<br>
Va eng muhimi: bu <b>faqat «я»</b> shaklida boʻladi. Qolgan hamma joyda oʻzak
oʻzgarmaydi.</div>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Я</span>
     <span class="pe-hl pe-hl--v">люблю́</span> футбо́л, а
     <span class="pe-hl pe-hl--s">Шербе́к</span>
     <span class="pe-hl pe-hl--v">лю́бит</span> ша́хматы.</p>
  <p class="pe-ex__uz">Men futbolni yaxshi koʻraman, Sherbek esa shaxmatni.</p>
  <p class="pe-ex__why">Bitta feʼl, ikki shakl: «я» da <b>-бл-</b>, uchinchi
     shaxsda oddiy <b>-б-</b>. Almashinuv faqat birinchisiga tegdi.</p>
</div>

<h3>4. Ж, Ш, Щ, Ч dan keyin — «-ат», «-ят» emas</h3>

<p>Bitta imlo qoidasi bor va u PR-4 dan tanish: <b>shivirlovchidan keyin Я
yozilmaydi</b>. Shuning uchun oʻzagi <b>ж, ш, щ, ч</b> ga tugagan II tuslanish
feʼllari «они́» shaklida <b>-ат</b> oladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>я</th><th>он / она́</th><th>они́</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">слы́шать</td><td class="pr-end">слы́шу</td>
      <td class="pr-end">слы́шит</td><td class="pr-end">слы́шат</td>
      <td class="pr-uz">eshitmoq</td></tr>
  <tr><td class="pr-res">учи́ть</td><td class="pr-end">учу́</td>
      <td class="pr-end">у́чит</td><td class="pr-end">у́чат</td>
      <td class="pr-uz">oʻrganmoq, oʻrgatmoq</td></tr>
  <tr><td class="pr-res">лежа́ть</td><td class="pr-end">лежу́</td>
      <td class="pr-end">лежи́т</td><td class="pr-end">лежа́т</td>
      <td class="pr-uz">yotmoq</td></tr>
  <tr><td class="pr-res">спеши́ть</td><td class="pr-end">спешу́</td>
      <td class="pr-end">спеши́т</td><td class="pr-end">спеша́т</td>
      <td class="pr-uz">shoshmoq</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Bu <b>imlo</b> qoidasi, talaffuz qoidasi emas. <em>Слы́шат</em> va
<em>говоря́т</em> ning oxiri deyarli bir xil eshitiladi — farq faqat yozuvda.
Shuning uchun yozganda oʻzakning oxirgi harfiga qarang: <b>ж ш щ ч</b> boʻlsa
<b>-ат</b>, boshqa har qanday harf boʻlsa <b>-ят</b>.</div>

<h3>5. Feʼl qaysi tuslanishda? — ishonchli yoʻl</h3>

<p>Infinitivga qarab taxmin qilish mumkin, lekin taxmin xato qiladi. <b>Eng
ishonchli belgi — «они́» shakli</b>: agar u <b>-ят / -ат</b> bilan tugasa, feʼl
II tuslanishda; <b>-ют / -ут</b> boʻlsa, I tuslanishda. Shuning uchun yangi
feʼlni yodlaganda uni <b>ikki shaklda</b> yozib qoʻying: <em>говори́ть —
говоря́т</em>.</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">II tuslanish — koʻpincha <b>-ить</b></p>
    <p>говори́ть · звони́ть · учи́ть · люби́ть · плати́ть · ходи́ть · стро́ить</p>
    <p><b>Va sakkizta «xoin»:</b> смотре́ть, ви́деть, слы́шать, сиде́ть,
       лежа́ть, стоя́ть, спать, держа́ть — ular <b>-еть / -ать</b> bilan
       tugaydi, lekin II tuslanishda.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">I tuslanish — qolgan hammasi</p>
    <p>чита́ть · рабо́тать · знать · де́лать · ду́мать · гуля́ть · игра́ть ·
       понима́ть · слу́шать</p>
    <p><b>Va bir nechta «-ить»:</b> жить (живу́), пить (пью) — ular I
       tuslanishda. Bularni PR-22 da koʻramiz.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Yuqoridagi sakkizta feʼlni <b>bitta jumla</b> qilib yodlang, chunki ular
kundalik nutqda juda koʻp uchraydi: «<em>смотрю́, ви́жу, слы́шу, сижу́, лежу́,
стою́, сплю, держу́</em>» — koʻrish, eshitish, oʻtirish, yotish, turish, uxlash.
Yaʼni <b>tananing holati va sezgilari</b>. Shu maʼno guruhi ularni birga
ushlab turadi.</div>

<h3>6. Urgʻu koʻchadi — va uni belgilash kerak</h3>

<p>II tuslanishda urgʻu koʻpincha «я» shaklida <b>qoʻshimchada</b> boʻladi,
keyin esa <b>oʻzakka qaytadi</b>. Bu naqshni bir marta koʻrsangiz, keyin
oʻzingiz taniysiz:</p>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">люблю́</span>
    <span class="pr-pair__uz">я — urgʻu oxirida</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">лю́бишь</span>
    <span class="pr-pair__uz">ты — urgʻu oʻzakka qaytdi</span>
  </div>
</div>

<p>Xuddi shunday: <em>смотрю́ — смо́тришь</em>, <em>учу́ — у́чишь</em>,
<em>хожу́ — хо́дишь</em>, <em>прошу́ — про́сишь</em>. Lekin
<em>говорю́ — говори́шь — говоря́т</em> da urgʻu <b>hamma joyda oxirida</b>
qoladi. Yodlaganda urgʻuni ham yodlang — u soʻzning bir qismi.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я любю́ ко́фе.</s></p>
  <p class="pe-good">Я <b>люблю́</b> ко́фе — «я» shaklida <b>б → бл</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Они́ говорю́т.</s></p>
  <p class="pe-good">Они́ <b>говоря́т</b> — II tuslanishda koʻplik <b>-ят</b>, <b>-ют</b> emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он смотре́ет фильм.</s></p>
  <p class="pe-good">Он <b>смо́трит</b> фильм — oʻzak <b>смотр-</b>, unli ham ketadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Они́ у́чят ру́сский язы́к.</s></p>
  <p class="pe-good">Они́ <b>у́чат</b> — Ч dan keyin <b>Я</b> yozilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мы лю́бим и они́ лю́блят.</s></p>
  <p class="pe-good">Мы лю́бим и они́ <b>лю́бят</b> — <b>Л</b> faqat «я» shaklida qoʻshiladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>смотре́ть</b> ni <b>мы</b> va <b>они́</b> uchun tuslang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>смо́трим</strong> va
    <strong>смо́трят</strong>. Oʻzak <b>смотр-</b> (infinitivdan <b>-еть</b>
    olib tashlandi). <em>Смотреть</em> — oʻsha sakkizta «xoin»dan biri: u
    <b>-еть</b> bilan tugaydi, lekin II tuslanishda.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Я ___ пло́в.</b> (люби́ть)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>люблю́</strong>. «Я» shaklida
    <b>Б</b> ga <b>Л</b> qoʻshiladi, chunki Б — lab undoshi. Qolgan shakllarda
    esa oddiy: <em>лю́бишь, лю́бит, лю́бим, лю́бите, лю́бят</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki feʼl qaysi tuslanishda? <b>рабо́тают</b> · <b>у́чат</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><em>Рабо́тают</em> — <b>I</b> tuslanish
    (<b>-ют</b>), <em>у́чат</em> — <b>II</b> tuslanish (<b>-ат</b>). Eng
    ishonchli belgi aynan «они́» shakli: <b>-ют/-ут</b> = I,
    <b>-ят/-ат</b> = II.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni ruschaga oʻgiring: <b>Siz ruscha gapirasizmi?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Вы говори́те по-ру́сски?</strong>
    «Вы» uchun qoʻshimcha <b>-ите</b>. <b>По-ру́сски</b> — «ruschada» degani va
    u ravish, shuning uchun hech qachon oʻzgarmaydi:
    <em>по-узбе́кски, по-англи́йски</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi shakl notoʻgʻri?<br>
     а) она́ звони́т &nbsp; б) я хожу́<br>
     в) они́ спя́т &nbsp; г) мы смотре́ем</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>г)</strong>. Toʻgʻrisi —
    <b>мы смо́трим</b>. Xato oʻzakni notoʻgʻri ajratishdan kelib chiqadi:
    <em>смотре́ть</em> dan <b>-еть</b> ketadi, faqat <b>-ть</b> emas. Qolgan
    uchtasi toʻgʻri: <em>звони́т</em> (II), <em>хожу́</em> (д→ж almashinuvi),
    <em>спят</em> (sakkizta «xoin»dan biri).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>говори́ть</b><span>gapirmoq</span></li>
  <li><b>смотре́ть</b><span>qaramoq, koʻrmoq (film)</span></li>
  <li><b>люби́ть</b><span>sevmoq, yaxshi koʻrmoq</span></li>
  <li><b>ви́деть</b><span>koʻrmoq</span></li>
  <li><b>слы́шать</b><span>eshitmoq</span></li>
  <li><b>учи́ть</b><span>oʻrganmoq, yodlamoq</span></li>
  <li><b>звони́ть</b><span>qoʻngʻiroq qilmoq</span></li>
  <li><b>ходи́ть</b><span>yurmoq, borib turmoq</span></li>
  <li><b>гото́вить</b><span>tayyorlamoq, ovqat pishirmoq</span></li>
  <li><b>по-ру́сски</b><span>ruschada</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>II tuslanish: <b>-ю, -ишь, -ит, -им, -ите, -ят</b>. «<b>И</b> qatori,
        oxirida <b>Я</b>».</li>
    <li>Oʻzak = infinitiv minus <b>-ить / -еть / -ать</b> — unli ham ketadi.</li>
    <li>«Я» shaklida almashinuv: <b>б/в/п → +Л</b> (люблю́), <b>д→ж</b> (хожу́),
        <b>с→ш</b> (прошу́), <b>т→ч</b> (плачу́). Faqat «я» da.</li>
    <li>Ж, Ш, Щ, Ч dan keyin <b>-ат</b>: у́чат, слы́шат, лежа́т.</li>
    <li>Tuslanishni «они́» shaklidan aniqlang: <b>-ют/-ут</b> = I,
        <b>-ят/-ат</b> = II. Yangi feʼlni ikki shaklda yodlang.</li>
    <li>Sakkizta «xoin»: смотре́ть, ви́деть, слы́шать, сиде́ть, лежа́ть,
        стоя́ть, спать, держа́ть.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-22: Notoʻgʻri feʼllar: хотеть, есть, дать, идти, ехать, жить, писать",
        "category": "russian",
        "order": 22,
        "summary": (
            "Rus tilidagi eng koʻp ishlatiladigan feʼllar aynan eng notoʻgʻrilari. "
            "Oʻn ikkitasini bir darsda yigʻib olasiz — va shundan keyin kundalik "
            "nutqning katta qismi qoʻlingizda boʻladi."
        ),
        "stories": ["Ку́хня в общежи́тии"],
        "content": """
<h2>PR-22: Notoʻgʻri feʼllar: хотеть, есть, дать, идти, ехать, жить, писать</h2>

<p>Bir narsani payqagandirsiz: PR-20 va PR-21 dagi jadvallarda <em>жить</em>,
<em>есть</em>, <em>хоте́ть</em> yoʻq edi. Holbuki bular siz kuniga eng koʻp
ishlatadigan feʼllar. Sabab oddiy: ular <b>naqshga toʻliq boʻysunmaydi</b>. Va bu
tasodif emas — <b>har qanday tilda eng koʻp ishlatiladigan soʻzlar eng notoʻgʻri
boʻladi</b>, chunki ular shu qadar tez-tez aytiladiki, eski shakllar oʻz holida
saqlanib qolgan. Bugun ularni bittalab qoʻlga olamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Жить, писа́ть, идти́, е́хать</b> ni tuslaysiz — oʻzagi oʻzgaradi</li>
    <li><b>Хоте́ть</b> ning ikki tuslanishga boʻlinishini koʻrasiz</li>
    <li><b>Есть</b> va <b>дать</b> — butunlay alohida ikki feʼlni oʻrganasiz</li>
    <li><b>Идти́</b> va <b>е́хать</b> ni ajratasiz: piyodami yoki transportdami</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻzak oʻzgaradi</span>
  <span class="pe-chip pe-chip--s">жи<b>ть</b></span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">жи<b>в</b>у́</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">пи<b>с</b>а́ть</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">пи<b>ш</b>у́</span>
</div>

<h3>1. Oʻzagi oʻzgaradigan feʼllar — qoʻshimchalar esa oddiy</h3>

<p>Eng yengil guruh shu. Ular <b>I tuslanish qoʻshimchalarini</b> oladi — siz
ularni allaqachon bilasiz. Faqat oʻzak infinitivdagidan boshqacha. Yaʼni
yodlash kerak boʻlgan narsa — bitta shakl, «я» shakli. Qolgani oʻsha
naqsh.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>я</th><th>ты</th><th>он / она́</th><th>мы</th><th>они́</th></tr>
  <tr><td class="pr-res">жить</td><td class="pr-end">живу́</td>
      <td class="pr-end">живёшь</td><td class="pr-end">живёт</td>
      <td class="pr-end">живём</td><td class="pr-end">живу́т</td></tr>
  <tr><td class="pr-res">писа́ть</td><td class="pr-end">пишу́</td>
      <td class="pr-end">пи́шешь</td><td class="pr-end">пи́шет</td>
      <td class="pr-end">пи́шем</td><td class="pr-end">пи́шут</td></tr>
  <tr><td class="pr-res">идти́</td><td class="pr-end">иду́</td>
      <td class="pr-end">идёшь</td><td class="pr-end">идёт</td>
      <td class="pr-end">идём</td><td class="pr-end">иду́т</td></tr>
  <tr><td class="pr-res">е́хать</td><td class="pr-end">е́ду</td>
      <td class="pr-end">е́дешь</td><td class="pr-end">е́дет</td>
      <td class="pr-end">е́дем</td><td class="pr-end">е́дут</td></tr>
  <tr><td class="pr-res">пить</td><td class="pr-end">пью</td>
      <td class="pr-end">пьёшь</td><td class="pr-end">пьёт</td>
      <td class="pr-end">пьём</td><td class="pr-end">пьют</td></tr>
  <tr><td class="pr-res">ждать</td><td class="pr-end">жду</td>
      <td class="pr-end">ждёшь</td><td class="pr-end">ждёт</td>
      <td class="pr-end">ждём</td><td class="pr-end">ждут</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Bu jadvalda <b>-ёшь, -ёт, -ём, -ёте</b> koʻrinyapti, <b>-ешь, -ет…</b> emas.
Yangi qoʻshimcha emas — bu oʻsha I tuslanish. PR-2 dagi qoida ishlayapti:
<b>urgʻu qoʻshimchaga tushsa, Е → Ё boʻladi</b>. Solishtiring:
<em>чит<b>а́</b>ешь</em> (urgʻu oʻzakda, Е qoladi) va <em>жив<b>ёшь</b></em>
(urgʻu qoʻshimchada, Ё boʻladi).</div>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Мы</span>
     <span class="pe-hl pe-hl--v">живём</span> в Ташке́нте, а
     <span class="pe-hl pe-hl--s">ба́бушка</span>
     <span class="pe-hl pe-hl--v">живёт</span> в Самарка́нде.</p>
  <p class="pe-ex__uz">Biz Toshkentda yashaymiz, buvim esa Samarqandda.</p>
  <p class="pe-ex__why">Oʻzak <b>жив-</b>, urgʻu qoʻshimchada. <em>В
     Ташке́нте</em> — hozircha uni butun ibora sifatida yodlang; nega
     <b>-е</b> ekanini PR-30 da koʻramiz.</p>
</div>

<h3>2. Хоте́ть — bitta feʼl, ikkita tuslanish</h3>

<p>Rus tilida bunday feʼl deyarli bitta. <em>Хоте́ть</em> birlikda <b>I</b>
tuslanishda, koʻplikda esa <b>II</b> tuslanishda tuslanadi — yaʼni gap
oʻrtasida guruhini almashtiradi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>Shakl</th><th>Tuslanish</th><th>Maʼnosi</th></tr>
  <tr><td>я</td><td class="pr-res">хочу́</td><td class="pr-uz">I</td><td class="pr-uz">xohlayman</td></tr>
  <tr><td>ты</td><td class="pr-res">хо́чешь</td><td class="pr-uz">I</td><td class="pr-uz">xohlaysan</td></tr>
  <tr><td>он / она́</td><td class="pr-res">хо́чет</td><td class="pr-uz">I</td><td class="pr-uz">xohlaydi</td></tr>
  <tr><td>мы</td><td class="pr-res">хоти́м</td><td class="pr-uz">II</td><td class="pr-uz">xohlaymiz</td></tr>
  <tr><td>вы</td><td class="pr-res">хоти́те</td><td class="pr-uz">II</td><td class="pr-uz">xohlaysiz</td></tr>
  <tr><td>они́</td><td class="pr-res">хотя́т</td><td class="pr-uz">II</td><td class="pr-uz">xohlaydilar</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Yodlash uchun chegarani koʻring: <b>birlikda Ч</b> (хочу́, хо́чешь, хо́чет),
<b>koʻplikda Т</b> (хоти́м, хоти́те, хотя́т). Uchtasi <b>Ч</b>, uchtasi
<b>Т</b>. Shu holicha ovoz chiqarib bir necha marta ayting — yozib yodlashdan
tezroq oʻtiradi.</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--s">Ты</span>
     <span class="pe-hl pe-hl--v">хо́чешь</span> чай?<br>
     — Да. И Дилно́за <span class="pe-hl pe-hl--v">хо́чет</span>. Мы
     <span class="pe-hl pe-hl--v">хоти́м</span> чай.</p>
  <p class="pe-ex__uz">— Choy xohlaysanmi?<br>— Ha. Dilnoza ham xohlaydi. Biz
     choy xohlaymiz.</p>
  <p class="pe-ex__why">Uch qatorda feʼl ikki marta guruh almashtirdi:
     <b>хо́чешь / хо́чет</b> (Ч) → <b>хоти́м</b> (Т).</p>
</div>

<h3>3. Есть va дать — alohida turadigan ikkilik</h3>

<p>Bu ikkisi shu qadar qadimiyki, ularning qoʻshimchalari <b>ikkala tuslanishga
ham oʻxshamaydi</b>. Yaxshi xabar: ular <b>bir-biriga</b> oʻxshaydi, shuning
uchun juftlab yodlanadi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>есть — yemoq</th><th>дать — bermoq</th></tr>
  <tr><td>я</td><td class="pr-res">ем</td><td class="pr-res">дам</td></tr>
  <tr><td>ты</td><td class="pr-res">ешь</td><td class="pr-res">дашь</td></tr>
  <tr><td>он / она́</td><td class="pr-res">ест</td><td class="pr-res">даст</td></tr>
  <tr><td>мы</td><td class="pr-res">еди́м</td><td class="pr-res">дади́м</td></tr>
  <tr><td>вы</td><td class="pr-res">еди́те</td><td class="pr-res">дади́те</td></tr>
  <tr><td>они́</td><td class="pr-res">едя́т</td><td class="pr-res">даду́т</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Есть</b> soʻzi sizda ikki xil maʼnoda uchraydi va ularni chalkashtirmang:<br>
PR-14 dagi <em>У меня́ <b>есть</b> брат</em> — «bor», egalik.<br>
Bugungi <em>Я <b>ем</b> пло́в</em> — «yeyman», feʼl.<br>
Yozilishi bir xil (<em>есть</em>), lekin birinchisi hech qachon tuslanmaydi,
ikkinchisi esa yuqoridagi jadval boʻyicha tuslanadi.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Едя́т</b> va <b>е́дут</b> — bu ikkisi bir-biriga juda oʻxshaydi, lekin
butunlay boshqa feʼllar:<br>
<em>Они́ <b>едя́т</b></em> — ular <b>yeyaptilar</b> (есть).<br>
<em>Они́ <b>е́дут</b></em> — ular <b>ketyaptilar</b>, transportda (е́хать).<br>
Farqi urgʻuda va bitta harfda. Ovoz chiqarib ayting: [йидя́т] — [йе́дут].</div>

<h3>4. Идти́ va е́хать — piyodami yoki transportdami</h3>

<p>Oʻzbekchada «bormoq» bitta. Rus tilida esa <b>qanday borayotganingiz</b>
feʼlni tanlaydi, va buni tushirib qoldirib boʻlmaydi:</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">идти́ — oyoq bilan</p>
    <p><em>Я <b>иду́</b> в шко́лу.</em><br>Maktabga ketyapman (piyoda).</p>
    <p>Shahar ichida, yaqin joyga, oʻz oyogʻida.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">е́хать — transportda</p>
    <p><em>Я <b>е́ду</b> в Самарка́нд.</em><br>Samarqandga ketyapman (mashinada,
       poyezdda).</p>
    <p>Avtobus, mashina, poyezd, samolyot — hammasi <em>е́хать</em>
       (samolyot uchun <em>лете́ть</em> ham bor).</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu — oʻzbek oʻquvchi uchun butunlay yangi tushuncha. Oʻzbekchada
<em>maktabga <b>boraman</b></em> va <em>Samarqandga <b>boraman</b></em> — bir
xil feʼl; vositani xohlasangiz aytasiz («avtobusda»), xohlamasangiz aytmaysiz.
Rus tilida esa <b>tanlash majburiy</b>: feʼlning oʻzi piyodami yoki
transportdami ekanini aytib turadi. Shuning uchun oʻzbek oʻquvchi «Я иду́ в
Москву́» deb yuboradi — ruscha quloqqa bu «Moskvaga piyoda ketyapman» boʻlib
eshitiladi. Bu feʼllarni PR-55 va PR-56 da toʻliq koʻramiz; bugun shu farqning
oʻzini eslab qoling.</div>

<h3>5. Bu feʼllar bilan birinchi gaplar</h3>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Жасу́р</span>
     <span class="pe-hl pe-hl--v">хо́чет</span>
     <span class="pe-hl pe-hl--v">есть</span>.</p>
  <p class="pe-ex__uz">Jasur ovqatlanmoqchi (qorni och).</p>
  <p class="pe-ex__why">Ikkinchi feʼl <b>infinitiv</b>da qoladi — PR-19 dagi
     qoida. Faqat birinchi feʼl tuslanadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Мы</span>
     <span class="pe-hl pe-hl--v">пьём</span> чай и
     <span class="pe-hl pe-hl--v">говори́м</span>.</p>
  <p class="pe-ex__uz">Choy ichamiz va gaplashamiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Куда́ ты <span class="pe-hl pe-hl--v">идёшь</span>?<br>
     — Я <span class="pe-hl pe-hl--v">иду́</span> домо́й. А ты?<br>
     — Я <span class="pe-hl pe-hl--v">е́ду</span> на рабо́ту.</p>
  <p class="pe-ex__uz">— Qayerga ketyapsan?<br>— Uyga ketyapman. Sen-chi?<br>
     — Men ishga ketyapman.</p>
  <p class="pe-ex__why">Ikki javob, ikki feʼl: birinchisi piyoda, ikkinchisi
     transportda. <b>Домо́й</b> — ravish, u hech qachon oʻzgarmaydi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Они́ хо́чут ко́фе.</s></p>
  <p class="pe-good">Они́ <b>хотя́т</b> ко́фе — koʻplikda <b>Т</b>, birlikda <b>Ч</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я хотю́ спать.</s></p>
  <p class="pe-good">Я <b>хочу́</b> спать — «я» shakli <b>хочу́</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он писа́ет письмо́.</s></p>
  <p class="pe-good">Он <b>пи́шет</b> письмо́ — oʻzak <b>пиш-</b>, <b>с → ш</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мы живе́м в Ташке́нте.</s></p>
  <p class="pe-good">Мы <b>живём</b> — urgʻu qoʻshimchada, demak <b>Ё</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Они́ е́дут пло́в.</s></p>
  <p class="pe-good">Они́ <b>едя́т</b> пло́в — <em>едя́т</em> = yeydilar,
     <em>е́дут</em> = ketadilar</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>жить</b> ni <b>они́</b> uchun tuslang va urgʻuni qoʻying.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>живу́т</strong>. Oʻzak <b>жив-</b>
    (infinitivda <b>В</b> yoʻq, tuslanganda paydo boʻladi), koʻplik
    qoʻshimchasi <b>-ут</b>. Bu I tuslanish — <em>-ют</em> emas <em>-ут</em>,
    chunki oʻzak undosh bilan tugaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Мы ___ пло́в.</b> (есть)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>еди́м</strong>. <em>Есть</em> —
    alohida turadigan feʼl: <em>ем, ешь, ест, еди́м, еди́те, едя́т</em>.
    Koʻplikda oʻzak uzayadi (<b>ед-</b>). Uni <em>дать</em> bilan juftlab
    yodlang: <em>дади́м</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>иду́</b> yoki <b>е́ду</b>? &nbsp; <b>Афсо́на ___ в Москву́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>е́дет</strong> (Афсо́на — uchinchi
    shaxs). Moskva uzoq, u yerga piyoda borilmaydi — demak <em>е́хать</em>.
    <em>Идти́</em> faqat oyoq bilan yurish uchun.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni ruschaga oʻgiring: <b>Ular choy ichishni xohlaydilar.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Они́ хотя́т пить чай.</strong>
    Birinchi feʼl tuslanadi (<b>хотя́т</b> — koʻplik, demak Т), ikkinchisi
    infinitivda qoladi (<b>пить</b>). Xuddi oʻzbekchadagi «ich<b>ish</b>ni
    xohlaydilar» kabi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi shakl notoʻgʻri?<br>
     а) ты пьёшь &nbsp; б) я даю́<br>
     в) он пи́шет &nbsp; г) вы хоти́те</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б)</strong>. Toʻgʻrisi —
    <b>я дам</b>. <em>Дать</em> naqshga boʻysunmaydi:
    <em>дам, дашь, даст, дади́м, дади́те, даду́т</em>. Qolgan uchtasi toʻgʻri.
    <em>Даю́</em> shakli boshqa feʼlga tegishli — <em>дава́ть</em>, uni
    keyinroq koʻramiz.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>жить</b><span>yashamoq</span></li>
  <li><b>писа́ть</b><span>yozmoq</span></li>
  <li><b>идти́</b><span>ketmoq, yurmoq (piyoda)</span></li>
  <li><b>е́хать</b><span>ketmoq (transportda)</span></li>
  <li><b>хоте́ть</b><span>xohlamoq</span></li>
  <li><b>есть</b><span>yemoq</span></li>
  <li><b>дать</b><span>bermoq</span></li>
  <li><b>пить</b><span>ichmoq</span></li>
  <li><b>ждать</b><span>kutmoq</span></li>
  <li><b>домо́й</b><span>uyga (tomon)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Eng koʻp ishlatiladigan feʼllar eng notoʻgʻrilari — bu qonuniyat, tasodif
        emas.</li>
    <li>Oʻzagi oʻzgaradiganlar oddiy <b>I tuslanish</b> qoʻshimchalarini oladi:
        <em>жив-у́, пиш-у́, ид-у́, е́д-у</em>.</li>
    <li>Urgʻu qoʻshimchada boʻlsa <b>Е → Ё</b>: <em>живёшь, идёт, пьёт</em>.</li>
    <li><b>Хоте́ть</b>: birlikda <b>Ч</b> (хочу́, хо́чешь, хо́чет), koʻplikda
        <b>Т</b> (хоти́м, хоти́те, хотя́т).</li>
    <li><b>Есть</b> va <b>дать</b> — juftlab yodlanadi:
        <em>ем/дам, еди́м/дади́м, едя́т/даду́т</em>.</li>
    <li><b>Идти́</b> = piyoda, <b>е́хать</b> = transportda. Rus tilida bu
        tanlov majburiy.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-23: Oʻtgan zamon (прошедшее время) — jinsga qarab -л, -ла, -ло, -ли",
        "category": "russian",
        "order": 23,
        "summary": (
            "Oʻtgan zamon hozirgi zamondan ancha oson — shaxs qoʻshimchalari umuman "
            "yoʻq. Lekin u shaxs oʻrniga JINSga qaraydi, va bu oʻzbek oʻquvchi uchun "
            "butunlay yangi."
        ),
        "stories": ["Вчера́ был дождь"],
        "content": """
<h2>PR-23: Oʻtgan zamon (прошедшее время) — jinsga qarab -л, -ла, -ло, -ли</h2>

<p>Yigirma ikki dars davomida siz faqat <b>bugun</b> haqida gapira olardingiz.
Bugundan boshlab <b>kecha</b> ochiladi — va u siz kutgandan ancha oson. Oʻtgan
zamonda <b>oltita qoʻshimcha yoʻq</b>. Umuman yoʻq. Har bir feʼlning oʻtgan
zamonda atigi <b>toʻrtta shakli</b> bor va ular hech qanday shaxsga qaramaydi.
Lekin ular boshqa narsaga qaraydi — <b>jinsga</b>. Va aynan shu joyi oʻzbek
oʻquvchi uchun yangi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Oʻtgan zamonni yasaysiz: infinitiv minus <b>-ть</b> + <b>л/ла/ло/ли</b></li>
    <li>Feʼlning shaxsga emas, <b>jinsga</b> moslashishini tushunasiz</li>
    <li><b>Был, была́, бы́ло, бы́ли</b> ni oʻrganasiz — «boʻlmoq» nihoyat paydo boʻladi</li>
    <li>Notoʻgʻri shakllarni bilasiz: <b>шёл, шла, шли</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻtgan zamon</span>
  <span class="pe-chip pe-chip--s">чита́</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">л · ла · ло · ли</span>
</div>

<h3>1. Yasalishi — bitta harf</h3>

<ol class="pe-steps">
  <li>Infinitivni oling: <b>чита́ть</b>.</li>
  <li><b>-ть</b> ni olib tashlang: <b>чита́-</b>. Oʻsha oʻzak, PR-20 dagi.</li>
  <li>Oxiriga <b>-л</b> qoʻying va <b>egaga qarab</b> unli qoʻshing.</li>
</ol>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">чита́<span class="pr-end">л</span></p>
    <p>Жасу́р чита́л. Я чита́л (yigit aytsa). Ты чита́л.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">чита́<span class="pr-end">ла</span></p>
    <p>Афсо́на чита́ла. Я чита́ла (qiz aytsa). Ты чита́ла.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний — oʻrta</p>
    <p class="pr-gender__form">чита́<span class="pr-end">ло</span></p>
    <p>Ра́дио рабо́тало. Kamdan-kam uchraydi — oʻrta jinsli ot kam gapiradi.</p>
  </div>
</div>

<p>Toʻrtinchisi — <b>koʻplik</b>, va u jinsga umuman qaramaydi:
<b>чита́<span class="pr-end">ли</span></b>. <em>Мы чита́ли. Они́ чита́ли. Вы
чита́ли.</em></p>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Вы</b> har doim <b>-ли</b> oladi — hatto bitta odamga hurmat bilan
murojaat qilinganda ham. <em>Мари́на Оле́говна, вы <b>чита́ли</b>?</em> —
bitta ayolga aytilyapti, lekin baribir koʻplik. PR-7 dagi qoida bu yerda ham
ishlaydi: <b>вы</b> shakli — hamisha koʻplik shakli.</div>

<h3>2. Butun jadval — oltita emas, toʻrtta</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>он</th><th>она́</th><th>оно́</th><th>они́ / мы / вы</th></tr>
  <tr><td class="pr-res">рабо́тать</td><td class="pr-end">рабо́тал</td>
      <td class="pr-end">рабо́тала</td><td class="pr-end">рабо́тало</td>
      <td class="pr-end">рабо́тали</td></tr>
  <tr><td class="pr-res">говори́ть</td><td class="pr-end">говори́л</td>
      <td class="pr-end">говори́ла</td><td class="pr-end">говори́ло</td>
      <td class="pr-end">говори́ли</td></tr>
  <tr><td class="pr-res">смотре́ть</td><td class="pr-end">смотре́л</td>
      <td class="pr-end">смотре́ла</td><td class="pr-end">смотре́ло</td>
      <td class="pr-end">смотре́ли</td></tr>
  <tr><td class="pr-res">хоте́ть</td><td class="pr-end">хоте́л</td>
      <td class="pr-end">хоте́ла</td><td class="pr-end">хоте́ло</td>
      <td class="pr-end">хоте́ли</td></tr>
  <tr><td class="pr-res">писа́ть</td><td class="pr-end">писа́л</td>
      <td class="pr-end">писа́ла</td><td class="pr-end">писа́ло</td>
      <td class="pr-end">писа́ли</td></tr>
  <tr><td class="pr-res">е́хать</td><td class="pr-end">е́хал</td>
      <td class="pr-end">е́хала</td><td class="pr-end">е́хало</td>
      <td class="pr-end">е́хали</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Kechagi darsning eng qiyin joyini eslang: <em>хочу́ — хо́чешь — хоти́м —
хотя́т</em>. Endi oʻsha feʼlning oʻtgan zamoniga qarang:
<em>хоте́л — хоте́ла — хоте́ли</em>. Hech qanday almashinuv, hech qanday ikki
guruh — infinitivning oʻzagi oʻz holida qolyapti. <b>Oʻtgan zamon rus feʼl
tizimining eng osoni.</b> Notoʻgʻri feʼllar ham bu yerda deyarli
toʻgʻrilanadi.</div>

<h3>3. Был, была́, бы́ло, бы́ли — «boʻlmoq» nihoyat koʻrinadi</h3>

<p>PR-11 da siz bir gʻalati narsani oʻrgangan edingiz: hozirgi zamonda
<em>быть</em> feʼli <b>umuman aytilmaydi</b>. <em>Я студе́нт.</em> — feʼlsiz.
Oʻtgan zamonda esa u <b>qaytib keladi</b>, va uni tushirib boʻlmaydi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Hozir (feʼlsiz)</th><th>Kecha (feʼl bilan)</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">Он до́ма.</td><td class="pr-end">Он <b>был</b> до́ма.</td>
      <td class="pr-uz">U uyda edi.</td></tr>
  <tr><td class="pr-res">Она́ до́ма.</td><td class="pr-end">Она́ <b>была́</b> до́ма.</td>
      <td class="pr-uz">U (ayol) uyda edi.</td></tr>
  <tr><td class="pr-res">Э́то интере́сно.</td><td class="pr-end">Э́то <b>бы́ло</b> интере́сно.</td>
      <td class="pr-uz">Bu qiziq edi.</td></tr>
  <tr><td class="pr-res">Мы до́ма.</td><td class="pr-end">Мы <b>бы́ли</b> до́ма.</td>
      <td class="pr-uz">Biz uyda edik.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Urgʻuga qarang: <b>был</b>, <b>бы́ло</b>, <b>бы́ли</b> — urgʻu boshida, lekin
<b>была́</b> — oxirida. Bu tasodifiy emas: <em>жить</em>, <em>дать</em>,
<em>пить</em> kabi qadimiy feʼllarda ham aynan <b>ayol jinsi</b> shakli
urgʻuni oxiriga tortadi: <em>жила́, дала́, пила́</em>. Erkak va koʻplikda esa
urgʻu joyida qoladi: <em>жил, жи́ли</em>.</div>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">был</span>
    <span class="pr-pair__uz">erkak — urgʻu boshida</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">была́</span>
    <span class="pr-pair__uz">ayol — urgʻu oxiriga koʻchdi</span>
  </div>
</div>

<h3>4. Notoʻgʻri shakllar — ular kam</h3>

<p>PR-22 dagi notoʻgʻri feʼllarning deyarli hammasi oʻtgan zamonda toʻgʻri
ishlaydi (<em>хоте́л, е́хал, писа́л, жил</em>). Faqat bir nechtasi
oʻzgacha:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>он</th><th>она́</th><th>они́</th><th>Izoh</th></tr>
  <tr><td class="pr-res">идти́</td><td class="pr-end">шёл</td>
      <td class="pr-end">шла</td><td class="pr-end">шли</td>
      <td class="pr-uz">butunlay boshqa oʻzak</td></tr>
  <tr><td class="pr-res">есть</td><td class="pr-end">ел</td>
      <td class="pr-end">е́ла</td><td class="pr-end">е́ли</td>
      <td class="pr-uz">qisqa, lekin qoidali</td></tr>
  <tr><td class="pr-res">дать</td><td class="pr-end">дал</td>
      <td class="pr-end">дала́</td><td class="pr-end">да́ли</td>
      <td class="pr-uz">ayol jinsida urgʻu oxirida</td></tr>
  <tr><td class="pr-res">жить</td><td class="pr-end">жил</td>
      <td class="pr-end">жила́</td><td class="pr-end">жи́ли</td>
      <td class="pr-uz">ayol jinsida urgʻu oxirida</td></tr>
  <tr><td class="pr-res">пить</td><td class="pr-end">пил</td>
      <td class="pr-end">пила́</td><td class="pr-end">пи́ли</td>
      <td class="pr-uz">ayol jinsida urgʻu oxirida</td></tr>
</table></div>

<p><b>Шёл — шла — шли</b> ni alohida yodlang. U <em>идти́</em> ning oʻtgan
zamoni, garchi bitta ham umumiy harfi boʻlmasa. Bu — rus tilidagi eng koʻp
uchraydigan notoʻgʻri shakl, va u ob-havo haqida ham ishlatiladi:
<em>Вчера́ <b>шёл</b> дождь</em> — kecha yomgʻir yogʻdi.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana bu darsning yuragi. Oʻzbek tilida oʻtgan zamon <b>shaxsni</b> koʻrsatadi
va jinsni <b>hech qachon</b> koʻrsatmaydi: <em>oʻqi<b>di</b>m,
oʻqi<b>di</b>ng, oʻqi<b>di</b></em> — kim oʻqiganini bilamiz, erkakmi yoki
ayolmi — bilmaymiz. Rus tilida esa <b>aynan teskarisi</b>: <em>чита́л /
чита́ла</em> — erkakmi yoki ayolmi ekanini bilamiz, kim ekanini (men, sen,
u — ) feʼldan bilmaymiz. Shuning uchun ruschada olmoshni <b>tushirib
qoldirmaslik kerak</b>: <em>Я чита́л</em> — «men» boʻlmasa, gap kim haqida
ekani nomaʼlum qoladi.<br><br>
Va eng koʻp qilinadigan xato shu yerda tugʻiladi: oʻzbek oʻquvchi jinsni
umuman payqamaydi va qiz bola haqida <em>«Афсо́на чита́л»</em> deb yozadi.
Har safar oʻtgan zamon yozayotganda oʻzingizdan soʻrang: <b>ega erkakmi,
ayolmi, koʻplikmi?</b></div>

<h3>5. Inkor va savol</h3>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Дилно́за</span>
     <span class="pe-hl pe-hl--neg">не</span>
     <span class="pe-hl pe-hl--v">рабо́тала</span> вчера́.</p>
  <p class="pe-ex__uz">Dilnoza kecha ishlamadi.</p>
  <p class="pe-ex__why">Inkor oʻsha qoida boʻyicha: <b>не</b> feʼl oldida.
     Ayol jinsi — <b>-ла</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Ты <span class="pe-hl pe-hl--v">был</span> до́ма?<br>
     — Нет, я <span class="pe-hl pe-hl--v">был</span> в шко́ле.</p>
  <p class="pe-ex__uz">— Uyda edingmi?<br>— Yoʻq, maktabda edim.</p>
  <p class="pe-ex__why">Ikkala gapda ham <b>был</b> — chunki gapirayotgan
     odam erkak. Agar qiz gapirsa, ikkalasi ham <b>была́</b> boʻlardi.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Oʻtgan zamonni birinchi kunlarda mashq qilishning eng foydali yoʻli — oʻzingiz
haqingizda gapirish. Agar siz yigit boʻlsangiz, <b>hamma gapingizda -л</b>
boʻladi: <em>Я чита́л, я рабо́тал, я е́хал, я был</em>. Qiz boʻlsangiz —
<b>hammasi -ла</b>. Yaʼni oʻzingiz haqingizda gapirganda tanlash yoʻq,
avtomatik. Qiyinchilik faqat boshqa odam haqida gapirganda boshlanadi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Афсо́на чита́л кни́гу.</s></p>
  <p class="pe-good">Афсо́на <b>чита́ла</b> — ega ayol, demak <b>-ла</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мы рабо́тал вчера́.</s></p>
  <p class="pe-good">Мы <b>рабо́тали</b> — koʻplik uchun <b>-ли</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Вчера́ я не рабо́таю.</s></p>
  <p class="pe-good">Вчера́ я не <b>рабо́тал</b> — <em>вчера́</em> oʻtgan zamon talab qiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Она́ идла́ домо́й.</s></p>
  <p class="pe-good">Она́ <b>шла</b> домо́й — <em>идти́</em> ning oʻtgan zamoni butunlay boshqa</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Вчера́ он до́ма.</s></p>
  <p class="pe-good">Вчера́ он <b>был</b> до́ма — oʻtgan zamonda <em>быть</em> tushirilmaydi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>говори́ть</b> ni <b>Дилно́за</b> uchun oʻtgan zamonga qoʻying.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>говори́ла</strong>. Oʻzak
    <b>говори́-</b> (infinitivdan <b>-ть</b> olib tashlandi), Dilnoza — qiz,
    demak <b>-ла</b>. Eʼtibor bering: hozirgi zamondagi <em>говори́т</em> ga
    xos ikki tuslanish farqi bu yerda umuman yoʻq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Вчера́ ___ дождь.</b> (идти́)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>шёл</strong>. <em>Дождь</em> — erkak
    jinsidagi ot (undosh bilan tugaydi), shuning uchun <b>шёл</b>. Ruschada
    yomgʻir «yogʻmaydi» — u <b>yuradi</b>. Bu ibora shundayligicha yodlanadi:
    <em>шёл дождь</em>, <em>шёл снег</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Toʻldiring: <b>Мари́на Оле́говна, вы ___ фильм?</b> (смотре́ть)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>смотре́ли</strong>. Gap bitta ayolga
    aytilyapti, lekin <b>вы</b> har doim koʻplik shaklini oladi — demak
    <b>-ли</b>, <em>смотре́ла</em> emas. Bu hurmat shakli, PR-7 dagi
    qoida.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni ruschaga oʻgiring (aytayotgan odam — qiz):
     <b>Kecha uyda edim va kitob oʻqidim.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Вчера́ я была́ до́ма и чита́ла
    кни́гу.</strong> Ikkala feʼl ham <b>-ла</b>, chunki gapirayotgan odam qiz.
    <em>Была́</em> da urgʻu oxirida. Va <em>быть</em> ni tushirib qoldirmang —
    oʻtgan zamonda u majburiy.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap toʻgʻri?<br>
     а) Они́ была́ до́ма. &nbsp; б) Жасу́р е́хала в Москву́.<br>
     в) Мы бы́ли в шко́ле. &nbsp; г) Афсо́на был здесь.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Qolganlarida jins yoki son
    xato: <em>они́</em> koʻplik — <b>бы́ли</b> boʻlishi kerak edi;
    <em>Жасу́р</em> — yigit, demak <b>е́хал</b>; <em>Афсо́на</em> — qiz, demak
    <b>была́</b>. Uchalasi ham bitta savolga javob bermaslikdan kelib chiqadi:
    <b>ega erkakmi, ayolmi, koʻplikmi?</b></p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>вчера́</b><span>kecha</span></li>
  <li><b>был / была́ / бы́ли</b><span>edi / edilar</span></li>
  <li><b>шёл / шла / шли</b><span>ketdi, yurdi (идти́)</span></li>
  <li><b>дождь</b><span>yomgʻir</span></li>
  <li><b>снег</b><span>qor</span></li>
  <li><b>у́тром</b><span>ertalab</span></li>
  <li><b>днём</b><span>kunduzi</span></li>
  <li><b>ве́чером</b><span>kechqurun</span></li>
  <li><b>пото́м</b><span>keyin</span></li>
  <li><b>неде́ля</b><span>hafta</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Yasalishi: infinitiv minus <b>-ть</b> + <b>л / ла / ло / ли</b>.</li>
    <li>Shaxs qoʻshimchalari <b>yoʻq</b> — atigi toʻrtta shakl.</li>
    <li>Feʼl <b>jinsga</b> qaraydi: <em>Жасу́р чита́л</em> — <em>Афсо́на
        чита́ла</em>. Oʻzbekchada bunday narsa yoʻq, shuning uchun har safar
        tekshiring.</li>
    <li><b>Вы</b> har doim <b>-ли</b>, hatto bitta odamga aytilsa ham.</li>
    <li>Oʻtgan zamonda <b>быть</b> qaytib keladi: <em>был, была́, бы́ло,
        бы́ли</em>. Ayol jinsida urgʻu oxirida.</li>
    <li>Yodlang: <b>шёл — шла — шли</b> (идти́). Va: <em>шёл дождь</em>.</li>
  </ul>
</div>
""",
    },
]
