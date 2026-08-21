# -*- coding: utf-8 -*-
"""Prime Russian — Block C yakuni (27–28).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

Bu ikki dars Block C ni yopadi va PR-29 dagi kelishiklar blokiga koʻprik
tashlaydi.

⚠️ IKKALA DARS HAM ДАТЕЛЬНЫЙ ПАДЕЖ ni talab qiladi (мне, тебе́, ему́…),
   lekin kelishiklar PR-29 dan boshlanadi va Д.п. PR-37/PR-41 da keladi.
   Shuning uchun bu yerda «мне, тебе́, ему́, ей, нам, вам, им» yopiq roʻyxat
   sifatida — yodlanadigan lugʻat sifatida — beriladi, va har ikkala darsda
   «bu shakl nega bunday — PR-37 da» deb ochiq aytiladi. Bu real rus tili
   kurslarining standart yoʻli: «мне нра́вится» boshidanoq kerak boʻladi.

Urgʻu siyosati: faqat YANGI va urgʻusi KOʻCHADIGAN soʻzlarga belgi.

Mashqlar:        practice/management/commands/_practice_pr_27_28.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_27_28.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_27_28.py --author=prime
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
        "title": "PR-27: Нужно, надо, можно, нельзя, должен — kerak va mumkin",
        "category": "russian",
        "order": 27,
        "summary": (
            "Rus tilida «kerak» va «mumkin» degan gaplarda ega umuman boʻlmaydi. "
            "Bu — oʻzbek oʻquvchi uchun tanish qurilish: «menga ishlash kerak» "
            "aynan shu shaklda ishlaydi."
        ),
        "stories": ["Пра́вила библиоте́ки"],
        "content": """
<h2>PR-27: Нужно, надо, можно, нельзя, должен — kerak va mumkin</h2>

<p>«Menga ishlash kerak». Bu oʻzbekcha gapda <b>ega yoʻq</b> — «men» emas,
«men<b>ga</b>». Rus tili aynan shunday qiladi: <em>Мне на́до рабо́тать</em>.
Shuning uchun bugungi dars — kursdagi eng oson darslardan biri. Siz bu
qurilishni allaqachon <b>oʻylamasdan</b> ishlatasiz, faqat ruscha soʻzlarni
qoʻyish qoladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>На́до</b> va <b>ну́жно</b> bilan «kerak» deysiz</li>
    <li><b>Мо́жно</b> va <b>нельзя́</b> bilan ruxsat berasiz va taqiqlaysiz</li>
    <li><b>Мне, тебе́, ему́, ей…</b> shakllarini yodlab olasiz</li>
    <li><b>До́лжен</b> ni ajratasiz — u boshqacha ishlaydi</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Shaxssiz qurilish</span>
  <span class="pe-chip pe-chip--o">Мне</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">на́до</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">рабо́тать</span>
</div>

<h3>1. Egasi yoʻq gaplar</h3>

<p>Rus tilida <em>На́до рабо́тать</em> — toʻliq, toʻgʻri gap. Unda <b>ega
umuman yoʻq</b>: kim ishlashi kerakligi aytilmagan, chunki bu hammaga
tegishli yoki kontekstdan maʼlum. Bunday gaplarni <b>shaxssiz gap</b>
(безли́чное предложе́ние) deyiladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--v">На́до</span> рабо́тать.</p>
  <p class="pe-ex__uz">Ishlash kerak.</p>
  <p class="pe-ex__why">Ega yoʻq — va u yetishmayotgandek tuyulmaydi.
     Oʻzbekchada ham xuddi shunday: «Ishlash kerak» — kim? deb soʻralmaydi.</p>
</div>

<p>Kimga tegishli ekanini aytish uchun oldiga bitta soʻz qoʻyiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--o">Мне</span>
     <span class="pe-hl pe-hl--v">на́до</span> рабо́тать.</p>
  <p class="pe-ex__uz">Menga ishlash kerak.</p>
</div>

<h3>2. Кому? — yodlab qoʻyiladigan yettita shakl</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Olmosh</th><th>Bu shaklda</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td>я</td><td class="pr-res">мне</td><td class="pr-end">Мне на́до идти́.</td>
      <td class="pr-uz">men<b>ga</b></td></tr>
  <tr><td>ты</td><td class="pr-res">тебе́</td><td class="pr-end">Тебе́ на́до отдыха́ть.</td>
      <td class="pr-uz">sen<b>ga</b></td></tr>
  <tr><td>он / оно́</td><td class="pr-res">ему́</td><td class="pr-end">Ему́ на́до рабо́тать.</td>
      <td class="pr-uz">unga (erkak)</td></tr>
  <tr><td>она́</td><td class="pr-res">ей</td><td class="pr-end">Ей на́до учи́ться.</td>
      <td class="pr-uz">unga (ayol)</td></tr>
  <tr><td>мы</td><td class="pr-res">нам</td><td class="pr-end">Нам на́до спеши́ть.</td>
      <td class="pr-uz">biz<b>ga</b></td></tr>
  <tr><td>вы</td><td class="pr-res">вам</td><td class="pr-end">Вам на́до отдохну́ть.</td>
      <td class="pr-uz">siz<b>ga</b></td></tr>
  <tr><td>они́</td><td class="pr-res">им</td><td class="pr-end">Им на́до ждать.</td>
      <td class="pr-uz">ular<b>ga</b></td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻng ustunga qarang — u tasodifan yozilmagan. Bu shakl oʻzbekchadagi
<b>joʻnalish kelishigi</b> ning aynan oʻzi:<br>
<em>men<b>ga</b> kerak</em> &nbsp;→&nbsp; <b>мне</b> на́до<br>
<em>sen<b>ga</b> kerak</em> &nbsp;→&nbsp; <b>тебе́</b> на́до<br>
<em>biz<b>ga</b> kerak</em> &nbsp;→&nbsp; <b>нам</b> на́до<br>
Yaʼni siz qurilishni oʻrganishingiz shart emas — u sizda allaqachon bor. Faqat
yettita soʻzni yodlash kerak. Rus tilida bu kelishik <b>да́тельный
паде́ж</b> deb ataladi va uni <b>PR-37</b> da toʻliq koʻramiz; hozircha shu
yettita shaklni lugʻat sifatida yodlang.</div>

<h3>3. На́до va ну́жно — «kerak»</h3>

<p>Ikkalasi ham «kerak» degani va kundalik nutqda deyarli <b>bir xil</b>
ishlatiladi. Bir tomchi farq bor: <b>на́до</b> — soʻzlashuvroq,
<b>ну́жно</b> — biroz rasmiyroq va yozuvda koʻproq uchraydi.</p>

<div class="pe-ex">
  <p class="pe-ex__ru">Мне <span class="pe-hl pe-hl--v">на́до</span> идти́. —
     Уже́? — Да, уже́ по́здно.</p>
  <p class="pe-ex__uz">Men ketishim kerak. — Allaqachonmi? — Ha, kech
     boʻldi.</p>
  <p class="pe-ex__why"><em>Мне на́до идти́</em> — rus tilida xayrlashishning
     eng koʻp ishlatiladigan boshlanishi. Butun ibora sifatida yodlang.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Что <span class="pe-hl pe-hl--v">ну́жно</span> де́лать?</p>
  <p class="pe-ex__uz">Nima qilish kerak?</p>
</div>

<h3>4. Мо́жно va нельзя́ — «mumkin» va «mumkin emas»</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">мо́жно — mumkin</p>
    <p><em>Здесь <b>мо́жно</b> кури́ть.</em><br>Bu yerda chekish mumkin.</p>
    <p>Ruxsat, imkoniyat. Yolgʻiz ham ishlatiladi: <em>— Мо́жно? — Мо́жно.</em></p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">нельзя́ — mumkin emas</p>
    <p><em>Здесь <b>нельзя́</b> кури́ть.</em><br>Bu yerda chekish mumkin emas.</p>
    <p>Taqiq. Diqqat: bu <b>bitta soʻz</b>, «не мо́жно» degan shakl rus tilida
       <b>umuman yoʻq</b>.</p>
  </div>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>«Не мо́жно» degan soʻz yoʻq.</b> Oʻzbek oʻquvchi «mumkin emas» ni soʻzma-soʻz
oʻgirib shunday yozib yuboradi. <em>Мо́жно</em> ning inkori — alohida soʻz:
<b>нельзя́</b>. Xuddi shunday <em>на́до</em> ning inkori <em>не на́до</em>
boʻladi va u «kerak emas» degani — <em>нельзя́</em> emas:<br>
<em><b>Не на́до</b> спеши́ть</em> — shoshish shart emas.<br>
<em><b>Нельзя́</b> спеши́ть</em> — shoshish mumkin emas (taqiqlangan).</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--v">Мо́жно</span> чай?<br>
     — Коне́чно, мо́жно.</p>
  <p class="pe-ex__uz">— Choy mumkinmi?<br>— Albatta.</p>
  <p class="pe-ex__why">Yolgʻiz <em>мо́жно?</em> — rus tilida ruxsat
     soʻrashning eng qisqa va eng koʻp ishlatiladigan yoʻli.</p>
</div>

<h3>5. До́лжен — bu bittasi boshqacha</h3>

<p>Yuqoridagi toʻrttasi hech qachon oʻzgarmaydi. <b>До́лжен</b> esa
oʻzgaradi — chunki u shaxssiz emas. Uning yonida <b>haqiqiy ega</b> boʻladi
(«я», «она́», «мы»), va u <b>sifat kabi jinsga moslashadi</b>:</p>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">до́лж<span class="pr-end">ен</span></p>
    <p><em>Я до́лжен рабо́тать. Жасу́р до́лжен идти́.</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">долж<span class="pr-end">на́</span></p>
    <p><em>Я должна́ рабо́тать. Афсо́на должна́ идти́.</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Koʻplik</p>
    <p class="pr-gender__form">долж<span class="pr-end">ны́</span></p>
    <p><em>Мы должны́ рабо́тать. Они́ должны́ идти́.</em></p>
  </div>
</div>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Мне на́до…</p>
    <p><b>Мне</b> — ega emas. Feʼl oʻzgarmaydi.</p>
    <p><em>Мне на́до рабо́тать.</em><br><em>Ей на́до рабо́тать.</em></p>
    <p>Vaziyat shunday: kech boʻldi, ish bor, pul kerak.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Я до́лжен…</p>
    <p><b>Я</b> — haqiqiy ega. Soʻz jinsga moslashadi.</p>
    <p><em>Я до́лжен рабо́тать.</em><br><em>Она́ должна́ рабо́тать.</em></p>
    <p>Majburiyat: vaʼda berganman, bu mening ishim.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Maʼno farqi kichkina va boshida uni oʻylab oʻtirmang. Lekin <b>grammatik
farqni</b> darrov eslab qoling, chunki xato aynan shu yerda boʻladi:
<b>«мне» dan keyin «до́лжен» kelmaydi</b>, va <b>«я» dan keyin «на́до»
kelmaydi</b>.<br>
✅ Мне на́до &nbsp;·&nbsp; ✅ Я до́лжен<br>
❌ <s>Мне до́лжен</s> &nbsp;·&nbsp; ❌ <s>Я на́до</s></div>

<h3>6. Oʻtgan va kelasi zamonda</h3>

<p>Shaxssiz gapda zamon <b>бы́ло</b> va <b>бу́дет</b> bilan koʻrsatiladi — va
ular har doim <b>oʻrta jinsda</b> qoladi, chunki ega yoʻq:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kecha</th><th>Bugun</th><th>Ertaga</th></tr>
  <tr><td class="pr-res">Мне на́до <b>бы́ло</b> рабо́тать.</td>
      <td class="pr-end">Мне на́до рабо́тать.</td>
      <td class="pr-uz">Мне на́до <b>бу́дет</b> рабо́тать.</td></tr>
  <tr><td class="pr-res">Здесь <b>бы́ло</b> нельзя́ кури́ть.</td>
      <td class="pr-end">Здесь нельзя́ кури́ть.</td>
      <td class="pr-uz">Здесь <b>бу́дет</b> нельзя́ кури́ть.</td></tr>
</table></div>

<p><b>До́лжен</b> da esa ega bor, shuning uchun <em>быть</em> unga
moslashadi: <em>Я <b>до́лжен был</b> рабо́тать</em> (erkak),
<em>Она́ <b>должна́ была́</b> рабо́тать</em> (ayol), <em>Мы <b>должны́
бы́ли</b> рабо́тать</em> (koʻplik).</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я на́до рабо́тать.</s></p>
  <p class="pe-good"><b>Мне</b> на́до рабо́тать — <em>на́до</em> yonida ega turmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Здесь не мо́жно кури́ть.</s></p>
  <p class="pe-good">Здесь <b>нельзя́</b> кури́ть — «не мо́жно» degan soʻz yoʻq</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Афсо́на до́лжен идти́.</s></p>
  <p class="pe-good">Афсо́на <b>должна́</b> идти́ — jinsga moslashadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мне до́лжен рабо́тать.</s></p>
  <p class="pe-good"><b>Я до́лжен</b> рабо́тать — <em>до́лжен</em> yonida haqiqiy ega boʻladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мне на́до был идти́.</s></p>
  <p class="pe-good">Мне на́до <b>бы́ло</b> идти́ — shaxssiz gapda har doim oʻrta jins</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>___ на́до отдыха́ть.</b> («senga» maʼnosida)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Тебе́</strong>. Yettita shakldan
    biri: <em>мне, тебе́, ему́, ей, нам, вам, им</em>. Oʻzbekcha «sen<b>ga</b>»
    — joʻnalish kelishigi, ruschada <b>да́тельный паде́ж</b>
    (PR-37).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu gapni ruschaga oʻgiring: <b>Bu yerda ovqatlanish mumkin emas.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Здесь нельзя́ есть.</strong>
    <em>Нельзя́</em> — bitta soʻz va u <em>мо́жно</em> ning inkori.
    <em>«Не мо́жно»</em> degan shakl rus tilida mavjud emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Дилно́за ___ идти́ домо́й.</b> (до́лжен)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>должна́</strong>. Dilnoza — qiz,
    va <em>до́лжен</em> sifat kabi jinsga moslashadi:
    <em>до́лжен / должна́ / должно́ / должны́</em>. Urgʻu ayol va koʻplik
    shakllarida oxirida.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni oʻtgan zamonga oʻtkazing: <b>Мне на́до рабо́тать.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Мне на́до бы́ло рабо́тать.</strong>
    Shaxssiz gapda ega yoʻq, shuning uchun <em>быть</em> har doim oʻrta
    jinsda qoladi — <b>бы́ло</b>. <em>«Мне на́до был»</em> — xato.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Нам ну́жно спеши́ть. &nbsp; б) Я на́до идти́.<br>
     в) Они́ должны́ ждать. &nbsp; г) Здесь мо́жно чита́ть.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б)</strong>. Toʻgʻrisi —
    <b>Мне на́до идти́</b>. <em>На́до</em> shaxssiz gapda ishlaydi va yonida
    ega turmaydi. Agar «я» ni saqlab qolmoqchi boʻlsangiz, boshqa soʻz kerak:
    <em>Я до́лжен идти́</em>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>на́до</b><span>kerak (soʻzlashuv)</span></li>
  <li><b>ну́жно</b><span>kerak (rasmiyroq)</span></li>
  <li><b>мо́жно</b><span>mumkin</span></li>
  <li><b>нельзя́</b><span>mumkin emas</span></li>
  <li><b>до́лжен / должна́</b><span>majbur, shart</span></li>
  <li><b>отдыха́ть</b><span>dam olmoq</span></li>
  <li><b>кури́ть</b><span>chekmoq</span></li>
  <li><b>пра́вило</b><span>qoida</span></li>
  <li><b>ти́хо</b><span>jimgina</span></li>
  <li><b>коне́чно</b><span>albatta</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Shaxssiz gapda <b>ega yoʻq</b>: <em>На́до рабо́тать.</em></li>
    <li>Kimga? — <b>мне, тебе́, ему́, ей, нам, вам, им</b>. Bu oʻzbekchadagi
        <b>-ga</b> ning oʻzi (да́тельный паде́ж, PR-37).</li>
    <li><b>На́до</b> = <b>ну́жно</b> = kerak. <b>Мо́жно</b> = mumkin.</li>
    <li><b>Нельзя́</b> — bitta soʻz. «Не мо́жно» degan shakl <b>yoʻq</b>.</li>
    <li><b>Не на́до</b> = kerak emas · <b>нельзя́</b> = taqiqlangan.</li>
    <li><b>До́лжен</b> boshqacha: yonida <b>haqiqiy ega</b> boʻladi va u
        jinsga moslashadi — <em>до́лжен, должна́, должны́</em>.</li>
    <li>Zamon: <em>на́до <b>бы́ло</b></em> / <em>на́до <b>бу́дет</b></em> —
        har doim oʻrta jinsda.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-28: Мне нравится — teskari qurilish va uning mantigʻi",
        "category": "russian",
        "order": 28,
        "summary": (
            "«Мне нра́вится фильм» da ega — men emas, FILM. Grammatika kitoblari buni "
            "«teskari qurilish» deydi, lekin oʻzbek oʻquvchi uchun u teskari emas: "
            "«menga film yoqadi» aynan shunday ishlaydi."
        ),
        "stories": ["Что тебе́ нра́вится?"],
        "content": """
<h2>PR-28: Мне нравится — teskari qurilish va uning mantigʻi</h2>

<p>Rus tili darsliklarida bu mavzu «qiyin» deb hisoblanadi. Ingliz oʻquvchi
uchun haqiqatan ham qiyin: u <em>I like the film</em> deb oʻylaydi va
<em>«Я нра́влюсь фильм»</em> deb yozadi. Siz esa bunday xato qilmaysiz —
chunki oʻzbekchada bu gap <b>allaqachon shu tartibda</b>: «<b>menga</b> bu
film <b>yoqadi</b>». Kim yoqtiryapti emas — <b>nima yoqyapti</b>. Bugun shu
mantiqni rus tiliga koʻchiramiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Кому + нра́вится + что</b> qolipini oʻrganasiz</li>
    <li>Feʼl <b>narsaga</b> moslashishini koʻrasiz: нра́вится / нра́вятся</li>
    <li>Oʻtgan zamonda yasaysiz: нра́вился, нра́вилась, нра́вились</li>
    <li><b>Нра́виться</b> va <b>люби́ть</b> ni ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--o">Мне</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">нра́вится</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">э́тот фильм</span>
</div>

<h3>1. Kim ega? — bu savol hamma narsani hal qiladi</h3>

<p>Gapga qarang: <em>Мне нра́вится э́тот фильм.</em> Bu yerda <b>ega —
фильм</b>, «мне» emas. Buni tekshirish oson: <b>ega har doim bosh
kelishikda</b> boʻladi, va <em>фильм</em> aynan shunday turibdi. Soʻzma-soʻz
oʻgirsak: «<b>menga bu film yoqadi</b>» — film yoqyapti, men emas.</p>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--o">Мне</span>
     <span class="pe-hl pe-hl--v">нра́вится</span>
     <span class="pe-hl pe-hl--s">э́тот фильм</span>.</p>
  <p class="pe-ex__uz">Menga bu film yoqadi.</p>
  <p class="pe-ex__why">Rangga qarang: yashil — ega. U gapning oxirida
     turibdi, lekin baribir ega. Rus tilida ega gapning istalgan joyida
     boʻlishi mumkin.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu darsning butun sirri shu: <b>bu qurilish siz uchun teskari emas</b>.<br>
<em><b>Menga</b> bu film <b>yoqadi</b></em> &nbsp;→&nbsp;
<em><b>Мне</b> <b>нра́вится</b> э́тот фильм</em><br>
<em><b>Menga</b> bu kitoblar <b>yoqadi</b></em> &nbsp;→&nbsp;
<em><b>Мне</b> <b>нра́вятся</b> э́ти кни́ги</em><br>
Oʻzbekchada ham «men» emas, «men<b>ga</b>» — joʻnalish kelishigi. Va
oʻzbekchada ham feʼl <b>yoqayotgan narsaga</b> qaraydi. Yaʼni ingliz
oʻquvchi bu yerda butun tushunchani qaytadan qurishi kerak, siz esa faqat
soʻzlarni almashtirasiz. Bu — oʻzbek tilining Prime Russian'dagi eng katta
sovgʻalaridan biri.</div>

<h3>2. Feʼl narsaga moslashadi — нра́вится yoki нра́вятся</h3>

<p>Ega — yoqayotgan narsa, demak feʼl <b>oʻshanga</b> qaraydi. Amalda bu
degani: ikkita shakl yodlanadi va tanlov <b>bitta savolga</b> qarab
qilinadi — narsa bittami yoki koʻpmi?</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Nima yoqyapti</th><th>Shakl</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-uz">bitta narsa</td><td class="pr-res">нра́вится</td>
      <td class="pr-end">Мне нра́вится э́та кни́га.</td>
      <td class="pr-uz">Menga bu kitob yoqadi.</td></tr>
  <tr><td class="pr-uz">koʻp narsa</td><td class="pr-res">нра́вятся</td>
      <td class="pr-end">Мне нра́вятся э́ти кни́ги.</td>
      <td class="pr-uz">Menga bu kitoblar yoqadi.</td></tr>
  <tr><td class="pr-uz">harakat (infinitiv)</td><td class="pr-res">нра́вится</td>
      <td class="pr-end">Мне нра́вится чита́ть.</td>
      <td class="pr-uz">Menga oʻqish yoqadi.</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Infinitiv bilan har doim <b>нра́вится</b> — birlik shakli.
<em>Мне нра́вится чита́ть, гуля́ть и спать.</em> Uchta harakat sanaldi, lekin
feʼl baribir birlikda: infinitiv hech qachon koʻplik boʻlmaydi.</div>

<h3>3. Kimga? — oʻsha yettita shakl</h3>

<p>PR-27 dagi roʻyxat bu yerda ham ishlaydi, oʻzgarishsiz:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kimga</th><th>Gap</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">мне</td><td class="pr-end">Мне нра́вится му́зыка.</td>
      <td class="pr-uz">Menga musiqa yoqadi.</td></tr>
  <tr><td class="pr-res">тебе́</td><td class="pr-end">Тебе́ нра́вится?</td>
      <td class="pr-uz">Senga yoqadimi?</td></tr>
  <tr><td class="pr-res">ему́</td><td class="pr-end">Ему́ нра́вится футбо́л.</td>
      <td class="pr-uz">Unga futbol yoqadi.</td></tr>
  <tr><td class="pr-res">ей</td><td class="pr-end">Ей нра́вятся ко́шки.</td>
      <td class="pr-uz">Unga mushuklar yoqadi.</td></tr>
  <tr><td class="pr-res">нам</td><td class="pr-end">Нам нра́вится здесь.</td>
      <td class="pr-uz">Bizga bu yer yoqadi.</td></tr>
  <tr><td class="pr-res">вам</td><td class="pr-end">Вам нра́вится Ташке́нт?</td>
      <td class="pr-uz">Sizga Toshkent yoqadimi?</td></tr>
  <tr><td class="pr-res">им</td><td class="pr-end">Им нра́вится игра́ть.</td>
      <td class="pr-uz">Ularga oʻynash yoqadi.</td></tr>
</table></div>

<p><em>Тебе́ нра́вится?</em> — bu savol rus tilida har kuni ishlatiladi va
javob ham qisqa boʻladi: <em>Да, нра́вится</em> yoki <em>Не о́чень</em>.</p>

<h3>4. Oʻtgan zamonda</h3>

<p>Feʼl egaga moslashadi — va ega yoqayotgan narsa, demak <b>oʻsha narsaning
jinsiga</b> qaraydi. Bu joyda oʻzbek oʻquvchi eng koʻp xato qiladi, chunki
avtomatik ravishda oʻzining jinsiga qarab qoʻyadi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Nima yoqqan</th><th>Shakl</th><th>Gap</th></tr>
  <tr><td class="pr-uz">фильм (erkak)</td><td class="pr-res">нра́вился</td>
      <td class="pr-end">Мне нра́вился э́тот фильм.</td></tr>
  <tr><td class="pr-uz">кни́га (ayol)</td><td class="pr-res">нра́вилась</td>
      <td class="pr-end">Мне нра́вилась э́та кни́га.</td></tr>
  <tr><td class="pr-uz">ме́сто (oʻrta)</td><td class="pr-res">нра́вилось</td>
      <td class="pr-end">Мне нра́вилось э́то ме́сто.</td></tr>
  <tr><td class="pr-uz">фи́льмы (koʻplik)</td><td class="pr-res">нра́вились</td>
      <td class="pr-end">Мне нра́вились э́ти фи́льмы.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<em>Мне нра́вилась кни́га</em> — bu gapni <b>qiz ham, yigit ham</b> aytadi.
<b>-Лась</b> qoʻshimchasi gapirayotgan odamning jinsini emas,
<em>кни́га</em> ning jinsini koʻrsatyapti. Solishtiring: PR-23 da
<em>я чита́ла</em> — u yerda ega «я» edi, shuning uchun qoʻshimcha sizga
qarardi. Bu yerda ega boshqa — shuning uchun qoʻshimcha ham boshqaga
qaraydi.</div>

<h3>5. Нра́виться va люби́ть — qaysi biri qachon</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">нра́виться — yoqadi</p>
    <p><em><b>Мне</b> нра́вится э́тот фильм.</em></p>
    <p>Ega — <b>фильм</b>. Yengilroq baho: koʻrdim, yoqdi. Yangi narsa haqida
       ham aytiladi.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">люби́ть — yaxshi koʻradi</p>
    <p><em><b>Я</b> люблю́ э́тот фильм.</em></p>
    <p>Ega — <b>я</b>, oddiy qurilish (PR-21). Chuqurroq va doimiyroq: odat,
       sevimli narsa.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bitta amaliy farqni eslab qoling: <b>odam haqida</b> aytilganda ular
butunlay boshqa maʼno beradi.<br>
<em>Ты мне <b>нра́вишься</b></em> — «sen menga yoqasan» (yaxshi
munosabat, samimiy, lekin yengil).<br>
<em>Я тебя́ <b>люблю́</b></em> — «men seni sevaman» (sevgi izhori).<br>
Ikkinchisini adashib aytib yubormang. Va birinchi gapga eʼtibor bering:
<em>нра́вишься</em> — «ты» ga moslashgan, chunki bu yerda <b>ega —
sen</b>.</div>

<h3>6. Xuddi shu mantiq: мне хо́лодно</h3>

<p><b>Мне</b> bilan boshlanadigan yana bir qurilish bor, va u aynan shu
mantiqda ishlaydi — ega yoʻq, holat esa <b>senga</b> tegishli:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">Мне хо́лодно.</td><td class="pr-uz">Menga sovuq.</td></tr>
  <tr><td class="pr-res">Мне жа́рко.</td><td class="pr-uz">Menga issiq.</td></tr>
  <tr><td class="pr-res">Мне интере́сно.</td><td class="pr-uz">Menga qiziq.</td></tr>
  <tr><td class="pr-res">Мне ску́чно.</td><td class="pr-uz">Menga zerikarli.</td></tr>
  <tr><td class="pr-res">Ему́ тру́дно.</td><td class="pr-uz">Unga qiyin.</td></tr>
</table></div>

<p>Yana bir bor oʻzbekcha bilan solishtiring — bir xil. <em>Я хо́лодно</em>
degan gap rus tilida yoʻq, xuddi «men sovuq» degan oʻzbekcha gap
gʻalati boʻlgani kabi. Bu qurilishni <b>PR-38</b> da kelishik bilan birga
yana koʻramiz.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я нра́влюсь э́тот фильм.</s></p>
  <p class="pe-good"><b>Мне нра́вится</b> э́тот фильм — ega <em>фильм</em></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мне нра́вится э́ти кни́ги.</s></p>
  <p class="pe-good">Мне <b>нра́вятся</b> э́ти кни́ги — koʻplik, demak <b>-ятся</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мне нра́вилась фильм.</s></p>
  <p class="pe-good">Мне <b>нра́вился</b> фильм — <em>фильм</em> erkak jinsida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я хо́лодно.</s></p>
  <p class="pe-good"><b>Мне</b> хо́лодно — bu holat, ega emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мне нра́вятся чита́ть и гуля́ть.</s></p>
  <p class="pe-good">Мне <b>нра́вится</b> чита́ть и гуля́ть — infinitiv har doim birlikda</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>нра́вится</b> yoki <b>нра́вятся</b>? &nbsp;
     <b>Ей ___ э́ти пе́сни.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>нра́вятся</strong>. Ega —
    <em>пе́сни</em> (qoʻshiqlar), koʻplik, demak <b>-ятся</b>. «Ей» ga
    qaramang — u ega emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu gapda ega qaysi soʻz? &nbsp; <b>Нам нра́вится Ташке́нт.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ташке́нт</strong>. U bosh
    kelishikda turibdi va feʼl aynan unga moslashgan (birlik —
    <em>нра́вится</em>). <em>Нам</em> — ega emas, u «bizga» degani.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Мне ___ э́та кни́га.</b> (oʻtgan zamon)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>нра́вилась</strong>. <em>Кни́га</em>
    — ayol jinsida, demak <b>-лась</b>. Bu gapni yigit ham aytadi:
    qoʻshimcha kitobga qaraydi, gapirayotgan odamga emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni ruschaga oʻgiring: <b>Menga oʻqish va sayr qilish yoqadi.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Мне нра́вится чита́ть и
    гуля́ть.</strong> Ikkita harakat sanaldi, lekin feʼl baribir
    <b>birlikda</b> — infinitiv hech qachon koʻplik boʻlmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu ikki gapning farqi nima?<br>
     <b>Мне нра́вится Ка́тя. · Я люблю́ Ка́тю.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — «Katya menga yoqadi»: yaxshi
    munosabat, yengil. Ikkinchisi — «men Katyani sevaman»: sevgi izhori.
    Grammatik jihatdan ham farq bor: birinchi gapda ega — <b>Ка́тя</b>,
    ikkinchisida — <b>я</b>. Odam haqida gapirganda bu ikkisini
    adashtirmang.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>нра́виться</b><span>yoqmoq</span></li>
  <li><b>мне нра́вится</b><span>menga yoqadi</span></li>
  <li><b>пе́сня</b><span>qoʻshiq</span></li>
  <li><b>мне хо́лодно</b><span>menga sovuq</span></li>
  <li><b>мне жа́рко</b><span>menga issiq</span></li>
  <li><b>интере́сно</b><span>qiziq</span></li>
  <li><b>ску́чно</b><span>zerikarli</span></li>
  <li><b>мне́ние</b><span>fikr</span></li>
  <li><b>ра́зный</b><span>turlicha, har xil</span></li>
  <li><b>не о́чень</b><span>unchalik emas</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Qolip: <b>КОМУ + нра́вится + ЧТО</b>. Ega — yoqayotgan
        <b>narsa</b>.</li>
    <li>Feʼl narsaga moslashadi: bitta narsa — <b>нра́вится</b>, koʻp narsa —
        <b>нра́вятся</b>.</li>
    <li>Infinitiv bilan har doim <b>нра́вится</b>.</li>
    <li>Oʻtgan zamonda qoʻshimcha <b>narsaning jinsiga</b> qaraydi:
        <em>нра́вился фильм</em>, <em>нра́вилась кни́га</em>.</li>
    <li><b>Нра́виться</b> = yoqadi (ega — narsa) · <b>люби́ть</b> = yaxshi
        koʻradi (ega — men).</li>
    <li><b>Мне хо́лодно, мне интере́сно</b> — aynan shu mantiq (PR-38 da
        davomi).</li>
    <li>Oʻzbekcha «men<b>ga</b> yoqadi» — bu qurilish siz uchun teskari
        emas.</li>
  </ul>
</div>
""",
    },
]
