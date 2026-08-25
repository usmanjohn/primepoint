# -*- coding: utf-8 -*-
"""Prime Russian — Block G davomi (80–82).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-80 — vaqt, sana, yosh, davomiylik. Darsning eng katta tuzogʻi:
rus tili soatni KELAYOTGAN soat ichida sanaydi («пятна́дцать мину́т
четвёртого» = 3:15), oʻzbek tili esa OʻTGAN soatdan. Ustiga за / че́рез /
на uchligi, u oʻzbekcha -da / -dan keyin / -ga ga toza tushadi.
PR-81 — shaxssiz gaplar. Oʻzbekchada ham bor va ham Дательный bilan
quriladi: «men<b>ga</b> sovuq» = «мне хо́лодно». Yagona yangi narsa —
kuchni Творительный bilan aytadigan «доро́гу занесло́ сне́гом» qurilishi.
PR-82 — tartib va jamlovchi sonlar. «Ikkalamiz» ↔ «вдвоём» juftligi
oʻzbek oʻquvchisiga tayyor kelib turibdi.

⚠️ Oʻqish matnlarida URGʻU BELGISI YOʻQ (2026-08-24 dagi qaror) —
darsliklar esa urgʻuni saqlaydi. Ikkalasini «tenglashtirmang».

Mashqlar:        practice/management/commands/_practice_pr_80_82.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_80_82.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_80_82.py --author=prime
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
        "title": "PR-80: Sana, vaqt, yosh va davomiylik",
        "category": "russian",
        "order": 80,
        "summary": (
            "Rus tili soatni kelayotgan soat ichida sanaydi — «полпя́того» bu 4:30. "
            "Ustiga sana, yosh (Да́тельный bilan) va за / че́рез / на uchligi."
        ),
        "stories": ["Сколько времени нужно, чтобы…"],
        "content": """
<h2>PR-80: Sana, vaqt, yosh va davomiylik</h2>

<p>Bitta savol: <em>«полпя́того»</em> soat necha? Koʻpchilik «besh yarim»
deb javob beradi va <b>adashadi</b>. Toʻgʻri javob — <b>4:30</b>. Chunki
rus tili soatni <b>tugagan</b> soatdan emas, <b>kelayotgan</b> soat ichida
sanaydi. Shu bitta farqni tushunsangiz, bu darsning eng qiyin joyi
ortda qoladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Soatni ayta olasiz — va yarim soat tuzogʻidan qutulasiz</li>
    <li>Sanani ikki shaklda qoʻyasiz: <b>«пя́тое ма́рта»</b> ↔ <b>«пя́того ма́рта»</b></li>
    <li>Yoshni aytasiz: <b>год / го́да / лет</b> qoidasi</li>
    <li>Davomiylikni Вини́тельный bilan berasiz</li>
    <li>Uchlikni ajratasiz: <b>за</b> · <b>че́рез</b> · <b>на</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Soat</span>
  <span class="pe-chip pe-chip--v">daqiqa</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">KEYINGI soat (Р.п.)</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">пятна́дцать мину́т четвёртого</span>
</div>

<h3>1. Soat: birinchi yarim</h3>

<p>Soatning <b>birinchi yarmida</b> (00–30 daqiqa) rus tili shunday
oʻylaydi: «biz hozir <b>toʻrtinchi soat</b> ichidamiz, undan 15 daqiqa
oʻtdi».</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soat</th><th>Ruscha</th><th>Soʻzma-soʻz</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">3:05</td><td class="pr-res">пять мину́т четвёртого</td>
      <td class="pr-uz">toʻrtinchining 5 daqiqasi</td><td class="pr-end">uchdan besh daqiqa oʻtdi</td></tr>
  <tr><td class="pr-stem">3:15</td><td class="pr-res">че́тверть четвёртого</td>
      <td class="pr-uz">toʻrtinchining choragi</td><td class="pr-end">uchdan chorak oʻtdi</td></tr>
  <tr class="pr-case__on"><td class="pr-stem">3:30</td><td class="pr-res">полчетвёртого</td>
      <td class="pr-uz">toʻrtinchining yarmi</td><td class="pr-end">uch yarim</td></tr>
  <tr><td class="pr-stem">4:30</td><td class="pr-res">полпя́того</td>
      <td class="pr-uz">beshinchining yarmi</td><td class="pr-end">toʻrt yarim</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Darsning eng katta tuzogʻi</span>
Oʻzbekcha <b>tugagan</b> soatni aytadi, ruscha <b>kelayotgan</b>
soatni:<br><br>
<em><b>uch</b> yarim</em> &nbsp;→&nbsp; <b>полчетвёртого</b>
(«toʻrtinchining yarmi»)<br>
<em><b>toʻrt</b> yarim</em> &nbsp;→&nbsp; <b>полпя́того</b><br><br>
Yaʼni ruscha son <b>har doim bittaga katta</b> koʻrinadi. Buni
shunday eslang: <em>«полпя́того»</em> — beshga <b>yetmadi</b>, yarim
soat qoldi.<br><br>
Shu tuzoqqa tushmaslikning oson yoʻli: rasmiy uslubda
<b>«четы́ре три́дцать»</b> deyish ham mumkin va hech kim
tushunmay qolmaydi.</div>

<h3>2. Soat: ikkinchi yarim</h3>

<p>30 daqiqadan keyin rus tili <b>ayirishga</b> oʻtadi —
<em>без</em> bilan:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soat</th><th>Ruscha</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">3:40</td><td class="pr-res">без двадцати́ четы́ре</td>
      <td class="pr-end">toʻrtga yigirma daqiqa qoldi</td></tr>
  <tr><td class="pr-stem">3:45</td><td class="pr-res">без че́тверти четы́ре</td>
      <td class="pr-end">toʻrtga chorak qoldi</td></tr>
  <tr><td class="pr-stem">3:55</td><td class="pr-res">без пяти́ четы́ре</td>
      <td class="pr-end">toʻrtga besh qoldi</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Ikki kichik qoida</span>
1. <b>«Без» dan keyin «в» qoʻyilmaydi.</b> <em>Он придёт
   <b>без че́тверти пять</b></em> — <s>в без четверти</s>
   deyilmaydi.<br>
2. Aniq soatda esa <b>в</b> kerak: <em><b>в</b> два часа́</em>,
   <em><b>в</b> семь часо́в</em>.<br><br>
Kun qismi: <b>утра́</b> (04–11), <b>дня</b> (12–17),
<b>ве́чера</b> (18–23), <b>но́чи</b> (00–03).
<em>в три часа́ дня</em> · <em>в два часа́ но́чи</em>.</div>

<h3>3. Sana: ikki shakl</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">«Bugun nechanchi?» — И.п.</p>
    <p><em>Сего́дня <b>пя́тое ма́рта</b>.</em><br>Bugun beshinchi mart.</p>
    <p>Tartib son <b>oʻrta jinsda</b> (число́), oy — Р.п. da.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">«Qachon?» — Р.п.</p>
    <p><em>Он прие́дет <b>пя́того ма́рта</b>.</em><br>U beshinchi martda keladi.</p>
    <p>Tartib son <b>Роди́тельный</b> ga oʻtadi.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">Yil bilan</p>
  <p class="pe-ex__ru">Он роди́лся <b>в 2008 году́</b>.</p>
  <p class="pe-ex__uz">U 2008-yilda tugʻilgan. — «в две ты́сячи восьмо́м году́».</p>
  <p class="pe-ex__ru">Э́то бы́ло <b>пя́того ма́рта две ты́сячи два́дцать шесто́го го́да</b>.</p>
  <p class="pe-ex__uz">Bu 2026-yilning 5-martida boʻlgan.</p>
  <p class="pe-ex__why">Uzun sonda faqat <b>oxirgi soʻz</b> oʻzgaradi:
     <em>две ты́сячи два́дцать <b>шесто́го</b></em>.</p>
</div>

<h3>4. Yosh: год / го́да / лет</h3>

<div class="pe-formula">
  <span class="pe-chip pe-chip--s">1</span>
  <span class="pe-op">→ год</span>
  <span class="pe-chip pe-chip--v">2–4</span>
  <span class="pe-op">→ го́да</span>
  <span class="pe-chip pe-chip--o">5–20</span>
  <span class="pe-op">→ лет</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">Yosh</p>
  <p class="pe-ex__ru"><b>Мне</b> два́дцать оди́н <b>год</b>.</p>
  <p class="pe-ex__ru"><b>Ему́</b> три́дцать два <b>го́да</b>.</p>
  <p class="pe-ex__ru"><b>Ей</b> со́рок пять <b>лет</b>.</p>
  <p class="pe-ex__uz">Men yigirma bir yoshdaman. · U oʻttiz ikki yoshda. · U qirq besh yoshda.</p>
  <p class="pe-ex__why">Oxirgi raqamga qarang: <em>21 → год</em>,
     <em>32 → го́да</em>, <em>45 → лет</em>. Lekin <b>11–14</b> har
     doim <b>лет</b>.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Odam Да́тельный da turadi</span>
Oʻzbekchada yosh egalik bilan aytiladi: <em>«<b>men</b> yigirma
yoshdaman»</em> — «men» bosh kelishikda.<br><br>
Ruschada esa odam <b>Да́тельный</b> ga oʻtadi:<br>
<s>Я два́дцать лет.</s> &nbsp;→&nbsp; <b>Мне</b> два́дцать лет.<br>
<s>Он три́дцать лет.</s> &nbsp;→&nbsp; <b>Ему́</b> три́дцать лет.<br><br>
Bu PR-38 dagi <em>мне хо́лодно</em> bilan bir oila: rus tilida
holat va yosh odamning <b>ustiga tushadi</b>, u esa «kimga?»
shaklida turadi.<br><br>
Oʻtgan va kelasi zamon ham shunday: <em>Ему́ <b>бы́ло</b>
три́дцать</em>, <em>Ей <b>бу́дет</b> со́рок</em>.</div>

<h3>5. Davomiylik: yalangʻoch Вини́тельный</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Qancha vaqt?</p>
  <p class="pe-ex__ru">Я жил там <b>три го́да</b>.</p>
  <p class="pe-ex__uz">U yerda uch yil yashadim.</p>
  <p class="pe-ex__ru">Он чита́л <b>весь ве́чер</b>.</p>
  <p class="pe-ex__uz">U kechqurun boʻyi oʻqidi.</p>
  <p class="pe-ex__why">Predlog <b>kerak emas</b> — vaqt oddiy
     Вини́тельный da turadi.</p>
</div>

<h3>6. За · че́рез · на — uchlik</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Predlog</th><th>Maʼnosi</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">за + В.п.</td><td class="pr-uz">shuncha vaqt <b>ichida</b> bajarildi</td>
      <td class="pr-res">Я прочита́л кни́гу <b>за два дня</b>.</td>
      <td class="pr-end">ikki kun<b>da</b> oʻqib chiqdim</td></tr>
  <tr><td class="pr-stem">че́рез + В.п.</td><td class="pr-uz">shuncha vaqt<b>dan keyin</b></td>
      <td class="pr-res"><b>Че́рез два дня</b> я верну́сь.</td>
      <td class="pr-end">ikki kun<b>dan keyin</b> qaytaman</td></tr>
  <tr><td class="pr-stem">на + В.п.</td><td class="pr-uz">shuncha vaqt<b>ga</b> moʻljallangan</td>
      <td class="pr-res">Я прие́хал <b>на два дня</b>.</td>
      <td class="pr-end">ikki kun<b>ga</b> keldim</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Uchlik bir-bir tushadi</span>
Bu jadvalni yodlash shart emas — oʻzbekcha qoʻshimchalar aynan
uchtaga boʻlinadi:<br><br>
<em>ikki kun<b>da</b></em> (bajardim) &nbsp;→&nbsp; <b>за</b> два дня<br>
<em>ikki kun<b>dan keyin</b></em> &nbsp;→&nbsp; <b>че́рез</b> два дня<br>
<em>ikki kun<b>ga</b></em> (keldim) &nbsp;→&nbsp; <b>на</b> два дня<br><br>
Farqni his qiling: <em>Я прие́хал <b>на</b> неде́лю</em> — bir
haftaga keldim (keyin ketaman). <em>Я прие́хал <b>че́рез</b>
неде́лю</em> — bir haftadan keyin keldim. Ikkinchisida men
allaqachon shu yerdaman.</div>

<h3>7. Takrorlanish</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Necha marta?</p>
  <p class="pe-ex__ru">Я хожу́ в бассе́йн <b>два ра́за в неде́лю</b>.</p>
  <p class="pe-ex__uz">Haftasiga ikki marta basseynga boraman.</p>
  <p class="pe-ex__ru">Он звони́т <b>раз в ме́сяц</b>.</p>
  <p class="pe-ex__uz">Oyiga bir marta qoʻngʻiroq qiladi.</p>
  <p class="pe-ex__why">Qolip: <b>N раз в</b> + Вини́тельный.
     «Bir marta» uchun <em>оди́н</em> aytilmaydi — shunchaki
     <em>раз</em>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Полпя́того — э́то 5:30.</s></p>
  <p class="pe-good">Полпя́того = <b>4:30</b> — «beshinchi soatning yarmi»</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я два́дцать лет.</s></p>
  <p class="pe-good"><b>Мне</b> два́дцать лет — odam Да́тельный da turadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я прочита́л кни́гу че́рез два дня.</s>
     <em>(ikki kunda oʻqidim)</em></p>
  <p class="pe-good">…<b>за</b> два дня — <em>че́рез</em> «keyin» degani</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ему́ три́дцать два лет.</s></p>
  <p class="pe-good">Ему́ три́дцать два <b>го́да</b> — oxirgi raqam 2, demak <em>го́да</em></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Soat necha? &nbsp; <b>полсе́дьмого</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>6:30</strong> — «yettinchi
    soatning yarmi». Ruscha son har doim bittaga katta
    koʻrinadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Ему́ два́дцать оди́н ___.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>год</strong>. Oxirgi raqam
    <b>1</b>, demak <em>год</em>. <em>Два́дцать два го́да</em>,
    <em>два́дцать пять лет</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>За</b>, <b>че́рез</b> yoki <b>на</b>? &nbsp;
     <b>Я прие́хал сюда́ ___ неде́лю и в суббо́ту уезжа́ю.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>на</strong> неде́лю — «bir
    haftaga keldim», moʻljallangan muddat. Oʻzbekcha
    «hafta<b>ga</b>» dagi <em>-ga</em> shuni koʻrsatib
    turibdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Sanani ikki shaklda ayting. &nbsp; <b>1-sentabr</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>«Bugun nechanchi?» —
    <strong>пе́рвое сентября́</strong> (И.п.). «Qachon?» —
    <strong>пе́рвого сентября́</strong> (Р.п.). Oy har ikkala
    holatda ham Роди́тельный da qoladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Ishni uch soatda tugatdim va ikki soatdan keyin uyga qaytdim.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я зако́нчил рабо́ту за три
    часа́ и че́рез два часа́ верну́лся домо́й.</strong> «Uch
    soat<b>da</b>» → <em>за</em>, «ikki soat<b>dan keyin</b>» →
    <em>че́рез</em>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>Кото́рый час?</b><span>Soat necha?</span></li>
  <li><b>че́тверть</b><span>chorak</span></li>
  <li><b>полшесто́го</b><span>5:30</span></li>
  <li><b>без че́тверти</b><span>chorak kam</span></li>
  <li><b>число́</b><span>sana, kun</span></li>
  <li><b>год / го́да / лет</b><span>yil (sonlar bilan)</span></li>
  <li><b>за</b> + В.п.<span>…da (bajarildi)</span></li>
  <li><b>че́рез</b> + В.п.<span>…dan keyin</span></li>
  <li><b>на</b> + В.п.<span>…ga (muddatga)</span></li>
  <li><b>раз в неде́лю</b><span>haftasiga bir marta</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Rus tili soatni <b>kelayotgan soat ichida</b> sanaydi:
        <em>полпя́того</em> = <b>4:30</b>.</li>
    <li>30 daqiqadan keyin <b>без</b> bilan ayiriladi:
        <em>без че́тверти пять</em>.</li>
    <li>Sana: «bugun nechanchi?» → <b>И.п.</b>, «qachon?» →
        <b>Р.п.</b> Uzun sonda faqat oxirgi soʻz oʻzgaradi.</li>
    <li>Yosh: odam <b>Да́тельный</b> da — <em>мне два́дцать
        лет</em>. 1 → год, 2–4 → го́да, 5–20 → лет.</li>
    <li>Davomiylik — <b>predlogsiz Вини́тельный</b>:
        <em>три го́да</em>.</li>
    <li><b>За</b> = …da (bajardim) · <b>че́рез</b> = …dan keyin ·
        <b>на</b> = …ga (muddatga).</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-81: Shaxssiz gaplar: холодно, темнеет, мне не спится, говорят",
        "category": "russian",
        "order": 81,
        "summary": (
            "Egasi yoʻq gaplar. Oʻzbekchada ham bor va ham Да́тельный bilan "
            "quriladi: «menga sovuq» = «мне хо́лодно». Bu dars sizga tanish."
        ),
        "stories": ["Темнеет рано"],
        "content": """
<h2>PR-81: Shaxssiz gaplar: холодно, темнеет, мне не спится, говорят</h2>

<p><em>«Темне́ет»</em> — kim qorongʻilashtiryapti? Hech kim.
<em>«Мне хо́лодно»</em> — kim sovuq? Hech kim, shunchaki <b>menga</b>
sovuq. Rus tilida bunday gaplar juda koʻp va ular <b>egasiz</b> —
gapda Имени́тельный da turgan soʻz umuman yoʻq. Yaxshi xabar:
oʻzbekchada ham xuddi shunday gaplar bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Shaxssiz gapni tanib olasiz: <b>egasi yoʻq, feʼl oʻrta jinsda</b></li>
    <li>Beshta asosiy turini oʻrganasiz</li>
    <li>Odamni <b>Да́тельный</b> ga qoʻyasiz: <em>мне, ему́, нам</em></li>
    <li>Oʻtgan va kelasi zamonini yasaysiz: <b>бы́ло хо́лодно</b>, <b>бу́дет хо́лодно</b></li>
    <li>Rus tiliga xos qurilishni olasiz: <b>доро́гу занесло́ сне́гом</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--o">odam (Д.п.)</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">holat soʻzi</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">Мне хо́лодно</span>
</div>

<h3>1. Beshta turi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Tur</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">Tabiat</td><td class="pr-res">Темне́ет. Света́ет. Моро́зит.</td>
      <td class="pr-end">Qorongʻilashyapti. Tong otyapti. Ayoz.</td></tr>
  <tr><td class="pr-stem">Holat (Д.п.)</td><td class="pr-res">Мне хо́лодно. Ему́ гру́стно.</td>
      <td class="pr-end">Menga sovuq. Uning koʻngli gʻash.</td></tr>
  <tr><td class="pr-stem">Zarurat</td><td class="pr-res">Мне ну́жно идти́. Нельзя́ кури́ть.</td>
      <td class="pr-end">Borishim kerak. Chekish mumkin emas.</td></tr>
  <tr><td class="pr-stem">-ся bilan</td><td class="pr-res">Мне не спи́тся. Хо́чется ча́ю.</td>
      <td class="pr-end">Uyqum kelmayapti. Choy ichgim kelyapti.</td></tr>
  <tr><td class="pr-stem">Yoʻqlik</td><td class="pr-res">Вре́мени нет. Де́нег не хвата́ет.</td>
      <td class="pr-end">Vaqt yoʻq. Pul yetmayapti.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bu dars sizga tanish</span>
Oʻzbekchada ham egasiz gaplar bor, va eng qizigʻi — ular ham
<b>joʻnalish shakli</b> bilan quriladi:<br><br>
<em>men<b>ga</b> sovuq</em> &nbsp;→&nbsp; <b>мне</b> хо́лодно<br>
<em>un<b>ga</b> qiziq</em> &nbsp;→&nbsp; <b>ему́</b> интере́сно<br>
<em>biz<b>ga</b> qiyin</em> &nbsp;→&nbsp; <b>нам</b> тру́дно<br><br>
Yaʼni oʻzbekcha <b>-ga</b> = ruscha <b>Да́тельный</b>. Bu PR-38 da
boshlangan chiziq, endi u butun bir gap turiga aylanadi.<br><br>
Xato qilmaslikning yoʻli oddiy: oʻzbekchada «men» emas,
«men<b>ga</b>» desangiz — ruschada ham <em>я</em> emas,
<em>мне</em> qoʻying.</div>

<h3>2. Zamon: бы́ло va бу́дет</h3>

<p>Shaxssiz gapda feʼl <b>oʻrta jinsda</b> turadi, chunki
moslashadigan ega yoʻq.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Hozirgi</th><th>Oʻtgan</th><th>Kelasi</th></tr>
  <tr><td class="pr-res">Мне хо́лодно.</td><td class="pr-uz">Мне <b>бы́ло</b> хо́лодно.</td>
      <td class="pr-end">Мне <b>бу́дет</b> хо́лодно.</td></tr>
  <tr><td class="pr-res">Темне́ет.</td><td class="pr-uz">Стемне́ло.</td>
      <td class="pr-end">Стемне́ет.</td></tr>
  <tr><td class="pr-res">Ну́жно идти́.</td><td class="pr-uz">Ну́жно <b>бы́ло</b> идти́.</td>
      <td class="pr-end">Ну́жно <b>бу́дет</b> идти́.</td></tr>
  <tr><td class="pr-res">Вре́мени нет.</td><td class="pr-uz">Вре́мени <b>не́ было</b>.</td>
      <td class="pr-end">Вре́мени <b>не бу́дет</b>.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ikkita ehtiyot joyi</span>
1. <b>Бы́ло</b> har doim <b>oʻrta jinsda</b>: <em>Мне бы́ло
   хо́лодно</em> — ayol aytsa ham <s>была́</s> emas.<br>
2. <b>Не́ было</b> alohida yoziladi va urgʻu <em>не</em> ga
   tushadi. Undan keyin ot <b>Роди́тельный</b> da qoladi:
   <em>вре́мени не́ было</em>, <em>де́нег не́ было</em>.</div>

<h3>3. -ся bilan quriladiganlari</h3>

<p>Bu guruh PR-62 dagi <b>-ся</b> ning toʻrtinchi maʼnosi. U
«men xohlamadim» emas, «<b>oʻz-oʻzidan shunday chiqdi</b>» degan
maʼnoni beradi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Holat, ixtiyor emas</p>
  <p class="pe-ex__ru">Мне не <b>спи́тся</b>.</p>
  <p class="pe-ex__uz">Uyqum kelmayapti. — Xohlayman, lekin uxlay olmayapman.</p>
  <p class="pe-ex__ru">Мне <b>хо́чется</b> ча́ю.</p>
  <p class="pe-ex__uz">Choy ichgim kelyapti.</p>
  <p class="pe-ex__ru">Мне <b>ка́жется</b>, что он прав.</p>
  <p class="pe-ex__uz">Menimcha, u haq.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">«…gim kelyapti»</span>
Oʻzbekchada bu qurilishning aynan juftligi bor va u ham
egasiz:<br><br>
<em>uxla<b>gim kelmayapti</b></em> &nbsp;→&nbsp; мне не
<b>спи́тся</b><br>
<em>choy ich<b>gim kelyapti</b></em> &nbsp;→&nbsp; мне
<b>хо́чется</b> ча́ю<br>
<em>ishla<b>gim kelmayapti</b></em> &nbsp;→&nbsp; мне не
<b>рабо́тается</b><br><br>
Ikkala tilda ham gapning markazida <b>odam emas, holat</b>
turadi. Odam esa chetda, «kimga?» shaklida.<br><br>
Diqqat: <em>хоте́ть</em> bilan <em>хо́чется</em> bir xil emas.
<em>Я хочу́ чай</em> — qatʼiy istak. <em>Мне хо́чется ча́ю</em> —
yumshoq, «choy ichsam yomon boʻlmasdi».</div>

<h3>4. «Говоря́т» — nomaʼlum shaxs</h3>

<p>Feʼl <b>они́</b> shaklida turadi, lekin «ular» kim ekani
aytilmaydi. Bu ham shaxssiz gapning bir turi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Kim aytdi — muhim emas</p>
  <p class="pe-ex__ru"><b>Говоря́т</b>, зима́ бу́дет холо́дной.</p>
  <p class="pe-ex__uz">Aytishlaricha, qish sovuq boʻlarmish.</p>
  <p class="pe-ex__ru">В Росси́и <b>пьют</b> мно́го ча́я.</p>
  <p class="pe-ex__uz">Rossiyada koʻp choy ichishadi.</p>
  <p class="pe-ex__ru">Меня́ <b>пригласи́ли</b> на сва́дьбу.</p>
  <p class="pe-ex__uz">Meni toʻyga taklif qilishdi.</p>
  <p class="pe-ex__why">Oʻzbekchada bu <b>-shadi / -ishdi</b>
     qoʻshimchasi bilan beriladi — aynan shu vazifa.</p>
</div>

<h3>5. Kuch Твори́тельный da</h3>

<p>Bu qurilish rus tiliga juda xos va oʻzbekchada toʻgʻridan-toʻgʻri
juftligi yoʻq. Tabiat kuchi ish qiladi, lekin u <b>ega emas</b> —
u Твори́тельный da turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Kuch — qurol kabi</p>
  <p class="pe-ex__ru">Доро́гу <b>занесло́ сне́гом</b>.</p>
  <p class="pe-ex__uz">Yoʻlni qor bosib qoldi.</p>
  <p class="pe-ex__ru">Кры́шу <b>сорва́ло ве́тром</b>.</p>
  <p class="pe-ex__uz">Tomni shamol uchirib ketdi.</p>
  <p class="pe-ex__ru">Ло́дку <b>унесло́ тече́нием</b>.</p>
  <p class="pe-ex__uz">Qayiqni oqim olib ketdi.</p>
  <p class="pe-ex__why">Obyekt <b>Вини́тельный</b> da
     (<em>доро́гу</em>), kuch <b>Твори́тельный</b> da
     (<em>сне́гом</em>), feʼl esa <b>oʻrta jinsda</b>.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Mana bu joyda oʻzbekcha yordam bermaydi</span>
Bu darsdagi yagona <b>butunlay yangi</b> qurilish shu. Oʻzbekchada
yoʻlni qor bossa, biz baribir <b>ega</b> qoʻyamiz: «<b>qor</b> yoʻlni
bosib qoldi».<br><br>
Ruschada esa ega umuman yoʻqoladi va qor <b>qurol</b> kabi
Твори́тельный ga tushadi:<br>
<em>Доро́гу занесло́ <b>сне́гом</b>.</em><br><br>
Shuning uchun bu uchta gapni <b>tayyor holda</b> yodlab qoʻying —
ular kundalik havo xabarlarida va yangiliklarda doim
uchraydi:<br>
<em>занесло́ сне́гом</em> · <em>сорва́ло ве́тром</em> ·
<em>унесло́ тече́нием</em>.</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Nega ruslar shunday deydi</span>
<em>«Ве́тер сорва́л кры́шу»</em> ham toʻgʻri. Lekin
<em>«Кры́шу сорва́ло ве́тром»</em> boshqa narsani aytadi:
shamol <b>ayblanmayapti</b>, shunchaki shunday boʻlib qoldi.<br><br>
Rus tili tabiat hodisalarini shunday koʻrsatishni yaxshi
koʻradi — hech kim javobgar emas, voqea oʻzi sodir boʻldi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я хо́лодно.</s></p>
  <p class="pe-good"><b>Мне</b> хо́лодно — odam Да́тельный da</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мне была́ хо́лодно.</s> <em>(ayol aytyapti)</em></p>
  <p class="pe-good">Мне <b>бы́ло</b> хо́лодно — shaxssiz gapda har doim oʻrta jins</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>У меня́ нет вре́мя.</s></p>
  <p class="pe-good">У меня́ нет <b>вре́мени</b> — <em>нет</em> dan keyin Роди́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Доро́гу занесла́ снег.</s></p>
  <p class="pe-good">Доро́гу занесло́ <b>сне́гом</b> — kuch Твори́тельный da, feʼl oʻrta jinsda</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>___ о́чень гру́стно
     сего́дня.</b> (я)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Мне</strong>. Holat
    bildiruvchi gapda odam <b>Да́тельный</b> da turadi.
    Oʻzbekcha «men<b>ga</b> gʻamgin» ham shuni koʻrsatib
    turibdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Dilnoza gapiryapti. Xatoni toping. &nbsp;
     <b>Мне была́ хо́лодно в по́езде.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Мне бы́ло хо́лодно.</strong>
    Shaxssiz gapda moslashadigan ega yoʻq, shuning uchun feʼl
    <b>har doim oʻrta jinsda</b> — kim gapirayotganidan qatʼi
    nazar.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapning farqi nima?<br>
     <b>Я хочу́ спать. · Мне не спи́тся.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — <b>istak</b>:
    «uxlagim kelyapti». Ikkinchisi — <b>holat</b>: «uxlay
    olmayapman, uyqum kelmayapti». Ikkinchisida men hech narsa
    qilmayapman, holat oʻz-oʻzidan shunday.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni shaxssiz qiling. &nbsp; <b>Ве́тер сорва́л кры́шу.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Кры́шу сорва́ло
    ве́тром.</strong> Obyekt Вини́тельный da qoladi
    (<em>кры́шу</em>), kuch Твори́тельный ga oʻtadi
    (<em>ве́тром</em>), feʼl esa oʻrta jinsga
    (<em>сорва́ло</em>).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Kechqurun qorongʻi tushdi va bizga sovuq boʻldi.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ве́чером стемне́ло, и нам
    ста́ло хо́лодно.</strong> Ikkala qism ham shaxssiz: birinchisida
    ega umuman yoʻq, ikkinchisida odam <em>нам</em> shaklida
    chetda turibdi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>темне́ет / стемне́ло</b><span>qorongʻilashyapti / qorongʻi tushdi</span></li>
  <li><b>света́ет</b><span>tong otyapti</span></li>
  <li><b>моро́зит</b><span>ayoz uryapti</span></li>
  <li><b>мне хо́лодно</b><span>menga sovuq</span></li>
  <li><b>мне не спи́тся</b><span>uyqum kelmayapti</span></li>
  <li><b>хо́чется</b><span>…gim kelyapti</span></li>
  <li><b>ка́жется</b><span>menimcha, koʻrinishicha</span></li>
  <li><b>говоря́т</b><span>aytishlaricha</span></li>
  <li><b>не хвата́ет</b><span>yetmayapti</span></li>
  <li><b>занести́ сне́гом</b><span>qor bosib qolmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Shaxssiz gapda <b>Имени́тельный da ega yoʻq</b>, feʼl esa
        oʻrta jinsda.</li>
    <li>Odam <b>Да́тельный</b> da turadi — oʻzbekcha
        <b>-ga</b> ning oʻzi: <em>мне хо́лодно</em>.</li>
    <li>Oʻtgan zamon har doim <b>бы́ло</b>, jinsdan qatʼi
        nazar.</li>
    <li><b>Мне не спи́тся</b> — istak emas, holat. Oʻzbekcha
        «…gim kelmayapti».</li>
    <li><b>Говоря́т, пи́шут, пригласи́ли</b> — «ular» kim ekani
        aytilmaydi (oʻzbekcha <b>-ishdi</b>).</li>
    <li>Kuch <b>Твори́тельный</b> da: <em>доро́гу занесло́
        сне́гом</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-82: Jamlovchi va tartib sonlar: двое, оба, первый, тридцать первое",
        "category": "russian",
        "order": 82,
        "summary": (
            "Tartib sonlar sifat kabi turlanadi, jamlovchi sonlar esa oʻzbekcha "
            "«ikkalamiz, uchovi» ga toʻgʻri keladi — вдвоём, втроём."
        ),
        "stories": ["Трое в лодке"],
        "content": """
<h2>PR-82: Jamlovchi va tartib sonlar: двое, оба, первый, тридцать первое</h2>

<p>Oʻzbekchada <em>«ikkalamiz bordik»</em> deysiz. Ruschada bunga
maxsus soʻz bor: <b>вдвоём</b>. Va <em>«uch kishi qayiqda»</em> uchun —
<b>тро́е в ло́дке</b>. Bu <b>jamlovchi sonlar</b>, va ular oddiy
<em>два, три</em> dan boshqacha ishlaydi. Dars ularni va <b>tartib
sonlar</b>ni bir joyga yigʻadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Tartib sonlarni yasaysiz va turlaysiz</li>
    <li>Uzun sonda faqat <b>oxirgi soʻz</b> oʻzgarishini bilasiz</li>
    <li>Jamlovchi sonlarni qachon ishlatishni oʻrganasiz: <b>дво́е, тро́е</b></li>
    <li>Bitta qatʼiy cheklovni eslab qolasiz: ayollarga <b>jamlovchi son qoʻyilmaydi</b></li>
    <li><b>Вдвоём, втроём</b> va <b>о́ба / о́бе</b> ni olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tartib</span>
  <span class="pe-chip pe-chip--s">пе́рвый · второ́й · тре́тий</span>
  <span class="pe-op">·</span>
  <span class="pe-formula__label">Jamlovchi</span>
  <span class="pe-chip pe-chip--v">дво́е · тро́е · че́тверо</span>
</div>

<h3>1. Tartib sonlar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Son</th><th>Tartib son</th><th>Son</th><th>Tartib son</th></tr>
  <tr><td class="pr-stem">1</td><td class="pr-res">пе́рвый</td>
      <td class="pr-stem">7</td><td class="pr-res">седьмо́й</td></tr>
  <tr><td class="pr-stem">2</td><td class="pr-res">второ́й</td>
      <td class="pr-stem">8</td><td class="pr-res">восьмо́й</td></tr>
  <tr><td class="pr-stem">3</td><td class="pr-res">тре́тий</td>
      <td class="pr-stem">9</td><td class="pr-res">девя́тый</td></tr>
  <tr><td class="pr-stem">4</td><td class="pr-res">четвёртый</td>
      <td class="pr-stem">10</td><td class="pr-res">деся́тый</td></tr>
  <tr><td class="pr-stem">5</td><td class="pr-res">пя́тый</td>
      <td class="pr-stem">40</td><td class="pr-res">сороково́й</td></tr>
  <tr><td class="pr-stem">6</td><td class="pr-res">шесто́й</td>
      <td class="pr-stem">100</td><td class="pr-res">со́тый</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Тре́тий — yolgʻiz istisno</span>
Boshqa tartib sonlar oddiy sifat kabi turlanadi
(<em>пя́тый, пя́тая, пя́тое</em>), lekin <b>тре́тий</b> oʻzining
namunasiga ega:<br><br>
<em>тре́тий, тре́тья, тре́тье, тре́тьи</em><br>
<em>тре́тьего, тре́тьему, тре́тьим, о тре́тьем</em><br><br>
Yumshoq belgi bilan — uni yodlab qoʻying.</div>

<div class="pe-ex">
  <p class="pe-ex__t">Faqat oxirgi soʻz oʻzgaradi</p>
  <p class="pe-ex__ru">Сего́дня <b>три́дцать пе́рвое</b> ма́я.</p>
  <p class="pe-ex__uz">Bugun 31-may. — «три́дцать» oʻzgarmadi.</p>
  <p class="pe-ex__ru">Он роди́лся в <b>две ты́сячи восьмо́м</b> году́.</p>
  <p class="pe-ex__uz">U 2008-yilda tugʻilgan. — faqat «восьмо́м» turlandi.</p>
  <p class="pe-ex__why">Bu PR-80 dagi sanalar bilan bir qoida:
     uzun tartib sonda oxirgi soʻzdan boshqasi <b>qotib
     qoladi</b>.</p>
</div>

<h3>2. Jamlovchi sonlar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Son</th><th>Jamlovchi</th><th>«Birga»</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">2</td><td class="pr-res">дво́е</td>
      <td class="pr-end">вдвоём</td><td class="pr-uz">ikkalasi, ikkovlashib</td></tr>
  <tr><td class="pr-stem">3</td><td class="pr-res">тро́е</td>
      <td class="pr-end">втроём</td><td class="pr-uz">uchalasi, uchovlashib</td></tr>
  <tr><td class="pr-stem">4</td><td class="pr-res">че́тверо</td>
      <td class="pr-end">вчетверо́м</td><td class="pr-uz">toʻrtalasi</td></tr>
  <tr><td class="pr-stem">5</td><td class="pr-res">пя́теро</td>
      <td class="pr-end">впятеро́м</td><td class="pr-uz">beshalasi</td></tr>
  <tr><td class="pr-stem">6</td><td class="pr-res">ше́стеро</td>
      <td class="pr-end">вшестеро́м</td><td class="pr-uz">oltalasi</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekchada bu bor</span>
Rus tilining bu qismi oʻzbek oʻquvchisiga tayyor kelib
turibdi:<br><br>
<em><b>ikkalasi</b> keldi</em> &nbsp;→&nbsp; пришли́ <b>дво́е</b><br>
<em><b>ikkalamiz</b> bordik</em> &nbsp;→&nbsp; мы пошли́
<b>вдвоём</b><br>
<em><b>uchovlashib</b> qildik</em> &nbsp;→&nbsp; мы сде́лали
<b>втроём</b><br><br>
Yaʼni oʻzbekcha <b>«-alasi / -ovlashib»</b> = ruscha
<b>дво́е / вдвоём</b> oilasi. Farqi bittagina: ruschada
bu shakllar <b>faqat 2 dan 7 gacha</b> mavjud, undan
keyin oddiy sonlar ishlatiladi.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Tartib sonlarda nima yangi</span>
Oʻzbekcha tartib son <b>hech qachon oʻzgarmaydi</b>:
<em>birinchi kun</em>, <em>birinchi kun<b>da</b></em>,
<em>birinchi kun<b>ni</b></em> — soʻzning oʻzi bir xil turaveradi,
qoʻshimcha faqat <b>otga</b> qoʻshiladi.<br><br>
Ruschada esa <b>ikkalasi ham</b> oʻzgaradi:<br>
<em>пе́рв<b>ый</b> день</em> → <em>в пе́рв<b>ый</b> день</em> →
<em>пе́рв<b>ого</b> дня</em><br><br>
Yaʼni tartib son — bu <b>sifat</b>, va PR-12 dagi oddiy sifat
qoidasi unga toʻliq tegishli. Yangi qoida yoʻq, faqat yangi
soʻzlar.</div>

<h3>3. Qachon jamlovchi son ishlatiladi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Holat</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-uz">Erkaklar guruhi</td><td class="pr-res">тро́е рабо́чих</td>
      <td class="pr-end">uchta ishchi</td></tr>
  <tr><td class="pr-uz">Bolalar</td><td class="pr-res">дво́е дете́й</td>
      <td class="pr-end">ikkita bola</td></tr>
  <tr><td class="pr-uz">«Bizlar»</td><td class="pr-res">нас бы́ло пя́теро</td>
      <td class="pr-end">beshtamiz edik</td></tr>
  <tr><td class="pr-uz">Faqat koʻplik otlar</td><td class="pr-res">дво́е су́ток</td>
      <td class="pr-end">ikki kecha-kunduz</td></tr>
  <tr><td class="pr-uz">Hayvon bolalari</td><td class="pr-res">че́тверо котя́т</td>
      <td class="pr-end">toʻrtta mushukcha</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ayollarga qoʻyilmaydi</span>
Bu darsning yagona qatʼiy taqiqi:<br><br>
<s>дво́е де́вушек</s> &nbsp;→&nbsp; <b>две де́вушки</b><br>
<s>тро́е сестёр</s> &nbsp;→&nbsp; <b>три сестры́</b><br><br>
Ayol kishilar bilan <b>oddiy son</b> ishlatiladi. Aralash guruh
boʻlsa — jamlovchi mumkin: <em>нас бы́ло тро́е</em>.<br><br>
Yodda tuting: <em>дво́е су́ток</em> toʻgʻri, lekin
<s>дво́е часо́в</s> notoʻgʻri — <em>два часа́</em>. Jamlovchi
son faqat yuqoridagi beshta holatda.</div>

<h3>4. Kelishik: дво́е ham turlanadi</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Turlanishi</p>
  <p class="pe-ex__ru">Пришли́ <b>тро́е</b>. <span class="pr-uz">(И.п.)</span></p>
  <p class="pe-ex__ru">Я ви́дел <b>трои́х</b>. <span class="pr-uz">(В.п., jonli)</span></p>
  <p class="pe-ex__ru">Я дал кни́ги <b>трои́м</b>. <span class="pr-uz">(Д.п.)</span></p>
  <p class="pe-ex__uz">Uchtasi keldi. · Uchtasini koʻrdim. · Uchtasiga kitob berdim.</p>
  <p class="pe-ex__why">Jamlovchi sondan keyingi ot esa
     <b>Роди́тельный koʻplikda</b> turadi: <em>тро́е
     дете́й</em>.</p>
</div>

<h3>5. О́ба va о́бе — «ikkalasi ham»</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">О́БА — erkak va oʻrta</p>
    <p><em><b>о́ба</b> бра́та</em> — ikkala aka<br>
       <em><b>о́ба</b> окна́</em> — ikkala deraza</p>
    <p>Turlanishi: <em>обо́их, обо́им, обо́ими</em>.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">О́БЕ — ayol</p>
    <p><em><b>о́бе</b> сестры́</em> — ikkala singil<br>
       <em><b>о́бе</b> кни́ги</em> — ikkala kitob</p>
    <p>Turlanishi: <em>обе́их, обе́им, обе́ими</em>.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ikkitasini ajratish oson</span>
<b>О́бе</b> ichida <b>е</b> bor — «жЕнский» dagi <b>е</b> kabi.
<b>О́ба</b> esa qolgan hamma narsa uchun.<br><br>
Va <em>о́ба</em> «ikkalasi <b>ham</b>» degani, <em>два</em> esa
shunchaki «ikkita». <em>Пришли́ <b>о́ба</b> бра́та</em> — ikkala
aka <b>ham</b> keldi, biri ham qolmadi.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">«Ikkalasi ham» — bizda ham juft</span>
<b>О́ба / о́бе</b> oʻzbekcha <em>«ikkalasi <b>ham</b>»</em> ga
toʻgʻri keladi, va ikkala tilda ham u <b>oddiy «ikkita»dan
kuchliroq</b>:<br><br>
<em>ikkita aka keldi</em> &nbsp;→&nbsp; пришли́ <b>два</b> бра́та
(shunchaki soni)<br>
<em>ikkala aka <b>ham</b> keldi</em> &nbsp;→&nbsp; пришли́
<b>о́ба</b> бра́та (biri ham qolmadi)<br><br>
Oʻzbekcha <em>«ham»</em> soʻzini eshitsangiz — ruschada
<em>о́ба / о́бе</em> qoʻying.</div>

<h3>6. Yarim, uchdan bir, chorak</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Kasrlar</p>
  <p class="pe-ex__ru"><b>полови́на</b> кни́ги · <b>треть</b> кла́сса · <b>че́тверть</b> ча́са</p>
  <p class="pe-ex__uz">kitobning yarmi · sinfning uchdan biri · soatning choragi</p>
  <p class="pe-ex__ru">Он съел <b>полторы́</b> лепёшки.</p>
  <p class="pe-ex__uz">U bir yarim non yedi.</p>
  <p class="pe-ex__why"><b>Полтора́</b> (erkak/oʻrta) ·
     <b>полторы́</b> (ayol) — «bir yarim».</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>дво́е де́вушек</s></p>
  <p class="pe-good"><b>две де́вушки</b> — ayollarga jamlovchi son qoʻyilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>о́ба сестры́</s></p>
  <p class="pe-good"><b>о́бе</b> сестры́ — ayol jinsida <em>о́бе</em></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>в две ты́сячи восьмы́х года́х</s></p>
  <p class="pe-good">в две ты́сячи <b>восьмо́м году́</b> — faqat oxirgi soʻz turlanadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>тре́тий день</s> → <s>в тре́тим дне</s></p>
  <p class="pe-good">в <b>тре́тьем</b> дне — <em>тре́тий</em> yumshoq namunada turlanadi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Toʻgʻri variantni tanlang. &nbsp;
     <b>В ко́мнате бы́ли ___ .</b> (uchta qiz)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>три де́вушки</strong>. Ayol
    kishilarga jamlovchi son <b>qoʻyilmaydi</b> —
    <s>тро́е де́вушек</s> notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>О́ба</b> yoki <b>о́бе</b>? &nbsp; <b>___ кни́ги
     интере́сные.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>О́бе</strong> —
    <em>кни́га</em> ayol jinsida. Eslatma: <em>о́б<b>е</b></em>
    ichidagi <b>е</b> — «женский» dagi <b>е</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bir soʻz bilan ayting. &nbsp; <b>Biz uchovlashib bordik.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Мы пошли́ втроём.</strong>
    Oʻzbekcha «-ovlashib» aynan shu <em>в-</em> li shaklga
    tushadi: <em>вдвоём, втроём, вчетверо́м</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Он роди́лся в две ты́сячи
     ___ году́.</b> (2010)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>деся́том</strong>. Faqat
    oxirgi soʻz tartib songa aylanadi va turlanadi;
    <em>две ты́сячи</em> oʻzgarmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Bizlar uchta edik va ikkala qayiq ham kichkina edi.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Нас бы́ло тро́е, и о́бе
    ло́дки бы́ли ма́ленькие.</strong> «Bizlar uchta» — jamlovchi
    son <em>тро́е</em>. <em>Ло́дка</em> ayol jinsida, demak
    <em>о́бе</em>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>пе́рвый / второ́й / тре́тий</b><span>birinchi / ikkinchi / uchinchi</span></li>
  <li><b>дво́е / тро́е / че́тверо</b><span>ikkalasi / uchalasi / toʻrtalasi</span></li>
  <li><b>вдвоём / втроём</b><span>ikkovlashib / uchovlashib</span></li>
  <li><b>о́ба / о́бе</b><span>ikkalasi ham</span></li>
  <li><b>полови́на</b><span>yarim</span></li>
  <li><b>треть</b><span>uchdan bir</span></li>
  <li><b>че́тверть</b><span>chorak</span></li>
  <li><b>полтора́ / полторы́</b><span>bir yarim</span></li>
  <li><b>су́тки</b><span>kecha-kunduz</span></li>
  <li><b>котёнок / котя́та</b><span>mushukcha / mushukchalar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Tartib sonlar <b>sifat kabi</b> turlanadi;
        <b>тре́тий</b> — yagona istisno.</li>
    <li>Uzun sonda <b>faqat oxirgi soʻz</b> oʻzgaradi:
        <em>в две ты́сячи восьмо́м году́</em>.</li>
    <li><b>Дво́е / тро́е</b> — erkaklar, bolalar, «bizlar»,
        koʻplik otlar va hayvon bolalari uchun.</li>
    <li><b>Ayollarga jamlovchi son qoʻyilmaydi</b>:
        <em>две де́вушки</em>.</li>
    <li>Oʻzbekcha <b>«ikkalamiz»</b> = <b>вдвоём</b>,
        <b>«uchovlashib»</b> = <b>втроём</b>.</li>
    <li><b>О́ба</b> (erkak/oʻrta) ↔ <b>о́бе</b> (ayol) — «ikkalasi
        <em>ham</em>».</li>
  </ul>
</div>
""",
    },
]
