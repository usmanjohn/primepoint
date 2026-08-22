# -*- coding: utf-8 -*-
"""Prime Russian — Block D yakuni (50) va Block E boshi (51–52).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-50 — kelishiklar blokining yakuni. Bu TAKROR darsi: yangi shakl yoʻq,
lekin yangi NARSA bor — kelishikni tanlash uchun amaliy qadamlar ketma-ketligi
va butun blok davomida toʻplangan xatolarning bir roʻyxati.

PR-51 va PR-52 — Block E boshlanadi: ВИД. Bu rus tilining IKKINCHI katta
tizimi. Kelishik otga tegishli edi, вид esa feʼlga. Oʻzbek oʻquvchi uchun
kaliti shu: tushuncha oʻzbekchada BOR (oʻqidim ↔ oʻqib chiqdim), faqat u
boshqa joyda yashaydi — feʼlning ichida emas, yonida.

Mashqlar:        practice/management/commands/_practice_pr_50_52.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_50_52.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_50_52.py --author=prime
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
        "title": "PR-50: Kelishiklar — umumiy takror va tirik gaplarda mashq",
        "category": "russian",
        "order": 50,
        "summary": (
            "Yigirma ikki dars, oltita kelishik — va bugun ular bitta tizimga "
            "yigʻiladi. Bu darsda yangi shakl yoʻq, lekin yangi narsa bor: "
            "kelishikni tanlashning amaliy tartibi."
        ),
        "stories": ["Оди́н день, шесть падеже́й"],
        "content": """
<h2>PR-50: Kelishiklar — umumiy takror va tirik gaplarda mashq</h2>

<p>PR-29 da xarita bor edi. Bugun — <b>manzil</b>. Yigirma ikki dars ichida
siz oltita kelishikni otlarda, olmoshlarda, egalik olmoshlarida,
sifatlarda va koʻplikda koʻrdingiz. Bugun yangi shakl yoʻq. Lekin yangi
narsa bor, va u amaliy: <b>gap tuzayotganda kelishikni qanday
tanlash</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Butun tizimni bitta jadvalda koʻrasiz</li>
    <li>Kelishikni tanlashning uchta qadamini oʻrganasiz</li>
    <li>Butun blokdagi eng koʻp xatolarni bir joyda koʻrib chiqasiz</li>
    <li>Tirik gapni soʻzma-soʻz tahlil qilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch qadam</span>
  <span class="pe-chip pe-chip--v">predlog bormi?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">soʻzning ishi nima?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">jins va son</span>
</div>

<h3>1. Butun tizim — bitta jadval</h3>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Savoli</th><th>моя́ но́вая кни́га</th><th>Asosiy ishi</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-case__q">кто? что?</td>
      <td class="pr-case__word">моя́ но́вая кни́га</td>
      <td class="pr-case__uz">ega; lugʻat shakli</td></tr>
  <tr><td class="pr-case__name">Роди́тельный</td><td class="pr-case__q">кого́? чего́?</td>
      <td class="pr-case__word">мое́й но́вой кни́ги</td>
      <td class="pr-case__uz">egalik · yoʻqlik · miqdor · 9 predlog</td></tr>
  <tr><td class="pr-case__name">Да́тельный</td><td class="pr-case__q">кому́? чему́?</td>
      <td class="pr-case__word">мое́й но́вой кни́ге</td>
      <td class="pr-case__uz">kimga · holat · yosh · к, по</td></tr>
  <tr><td class="pr-case__name">Вини́тельный</td><td class="pr-case__q">кого́? что?</td>
      <td class="pr-case__word">мою́ но́вую кни́гу</td>
      <td class="pr-case__uz">toʻldiruvchi · manzil · vaqt</td></tr>
  <tr><td class="pr-case__name">Твори́тельный</td><td class="pr-case__q">кем? чем?</td>
      <td class="pr-case__word">мое́й но́вой кни́гой</td>
      <td class="pr-case__uz">asbob · hamroh · kasb · joy</td></tr>
  <tr><td class="pr-case__name">Предло́жный</td><td class="pr-case__q">о ком? о чём?</td>
      <td class="pr-case__word">о мое́й но́вой кни́ге</td>
      <td class="pr-case__uz">qayerda · nima haqida</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Uchinchi ustunga qarang: <b>uchta soʻz doim birga oʻzgaradi</b>. Egalik
olmoshi, sifat va ot — ular bitta guruh. Agar otning kelishigini
bilsangiz, qolgan ikkitasi <b>oʻz-oʻzidan</b> chiqadi.<br><br>
Va ayol jinsida yana oʻsha yengillik: <em>мое́й но́вой кни́ги / кни́ге /
кни́гой</em> — sifat va olmosh uchta kelishikda <b>bir xil</b>
koʻrinadi.</div>

<h3>2. Kelishikni tanlash — uch qadam</h3>

<ol class="pe-steps">
  <li><b>Predlog bormi?</b> Agar bor boʻlsa — <b>u tanlaydi</b>. PR-48
      dagi xarita: <em>к, по</em> → Д.п.; <em>из, от, до, у, без, для,
      о́коло, по́сле, с</em> → Р.п.; <em>над, под, за, пе́ред, ме́жду,
      с</em> → Т.п.; <em>о</em> → П.п. Va <em>в, на</em> — harakat boʻlsa
      В.п., boʻlmasa П.п.</li>
  <li><b>Predlog yoʻq boʻlsa — soʻzning ishi nima?</b><br>
      Ega? → И.п. · Kimni/nimani? → В.п. · Kimniki? → Р.п. ·
      Kimga? → Д.п. · Nima bilan? → Т.п.</li>
  <li><b>Jins va son</b> — qoʻshimchani tanlaydi. Va sifat bilan olmosh
      otga ergashadi.</li>
</ol>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Ikkinchi qadamda yordam beradigan qisqa roʻyxat — <b>feʼl kelishikni
talab qiladi</b>:<br>
<b>В.п.</b>: чита́ть, ви́деть, знать, люби́ть, ждать, де́лать<br>
<b>Д.п.</b>: дать, сказа́ть, писа́ть, звони́ть, помога́ть, отвеча́ть,
меша́ть<br>
<b>Р.п.</b>: <em>нет</em> + ot<br>
<b>Т.п.</b>: рабо́тать (kem), стать (kem)<br>
<b>П.п.</b>: ду́мать <em>о</em>, говори́ть <em>о</em>, мечта́ть
<em>о</em></div>

<h3>3. Tirik gap — soʻzma-soʻz</h3>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">У́тром</span>
     <span class="pe-hl pe-hl--o">я</span>
     <span class="pe-hl pe-hl--v">иду́</span>
     <span class="pe-hl pe-hl--adv">в шко́лу</span> и говорю́
     <span class="pe-hl pe-hl--adv">с учи́телем</span>
     <span class="pe-hl pe-hl--adv">о но́вой кни́ге</span>.</p>
  <p class="pe-ex__uz">Ertalab maktabga boraman va oʻqituvchi bilan yangi
     kitob haqida gaplashaman.</p>
</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Nega shu shaklda</th><th>Kelishik</th></tr>
  <tr><td class="pr-res">у́тром</td><td class="pr-uz">kun qismi — predlogsiz</td>
      <td class="pr-end">Твори́тельный</td></tr>
  <tr><td class="pr-res">я</td><td class="pr-uz">ega</td>
      <td class="pr-end">Имени́тельный</td></tr>
  <tr><td class="pr-res">в шко́лу</td><td class="pr-uz">harakat bor — manzil</td>
      <td class="pr-end">Вини́тельный</td></tr>
  <tr><td class="pr-res">с учи́телем</td><td class="pr-uz">predlog С — hamroh</td>
      <td class="pr-end">Твори́тельный</td></tr>
  <tr><td class="pr-res">о но́вой кни́ге</td><td class="pr-uz">predlog О — mavzu</td>
      <td class="pr-end">Предло́жный</td></tr>
</table></div>

<p>Bitta gapda toʻrtta kelishik. Va siz ularning hammasini
<b>oʻylab oʻtirmasdan</b> tanlashingiz kerak — aynan shuning uchun mashq
kerak, jadval emas.</p>

<h3>4. Butun blokdagi eng koʻp xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я в шко́ла. · Я иду́ в шко́ле.</s></p>
  <p class="pe-good">Я <b>в шко́ле</b> (qayerda) · Я иду́ <b>в шко́лу</b> (qayerga)</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Бра́та кни́га.</s></p>
  <p class="pe-good"><b>Кни́га бра́та</b> — egasi orqada, oʻzbekchaning teskarisi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>У меня́ нет кни́га. · Я иду́ из рабо́ты.</s></p>
  <p class="pe-good">нет <b>кни́ги</b> · <b>с</b> рабо́ты — «нет» Р.п. oladi, <em>рабо́та</em> НА oladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я помога́ю бра́та. · Я пишу́ с ру́чкой.</s></p>
  <p class="pe-good">помога́ю <b>бра́ту</b> (Д.п.) · пишу́ <b>ру́чкой</b> (asbob — predlogsiz)</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я два́дцать лет. · У его́ есть маши́на.</s></p>
  <p class="pe-good"><b>Мне</b> два́дцать лет · У <b>него́</b> — predlogdan keyin Н</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>пять кни́ги · мно́го челове́ков</s></p>
  <p class="pe-good">пять <b>книг</b> · мно́го <b>люде́й</b></p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Butun blokni bir joyda sanab chiqamiz.<br><br>
<b>Nima toʻgʻri keldi:</b> beshta kelishik oʻzbekchada bor va deyarli aniq
mos tushdi — <em>-ning</em> (Р.п.), <em>-ga</em> (Д.п.), <em>-ni</em>
(В.п.), <em>-da</em> (П.п.), <em>-dan</em> (Р.п. predloglar bilan).
Shuning uchun siz kelishik <b>tushunchasini</b> oʻrganmadingiz — siz uni
allaqachon bilardingiz.<br><br>
<b>Nima yangi edi:</b> bittagina kelishik — <b>Твори́тельный</b> —
oʻzbekchada alohida shakl sifatida yoʻq. Va uchta qiyinchilik:
<b>jins</b> (oʻzbekchada umuman yoʻq), <b>predloglar</b> (ular soʻzdan
oldin turadi va kelishikni tanlaydi), <b>urgʻuning koʻchishi</b>.<br><br>
Yaʼni yigirma ikki dars ichida siz aslida <b>bitta yangi tushuncha</b> va
<b>oʻntacha qoʻshimchalar toʻplami</b> oʻrgandingiz. Qolgani — oʻzbek
tilidan koʻchirish edi. Bu — kichkina ish emas, lekin u siz oʻylagandan
kichikroq.</div>

<h3>5. Keyin nima boʻladi</h3>

<p>Kelishiklar tugadi. Keyingi darsdan <b>Block E</b> boshlanadi va unda
rus tilining <b>ikkinchi katta tizimi</b> keladi — <b>вид</b> (feʼl
turi).</p>

<p>Farqni bir jumlada aytish mumkin: kelishik <b>otga</b> tegishli edi va u
soʻzning gapdagi <b>ishini</b> koʻrsatardi. Вид esa <b>feʼlga</b> tegishli
va u harakatning <b>tugagan-tugamaganini</b> koʻrsatadi. Yangi tizim,
lekin oʻsha usul: oʻzbekcha bilan solishtirib, qadam-baqadam.</p>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Kelishikni tanlashning birinchi qadami nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Predlog bormi?</strong> Agar bor
    boʻlsa, u kelishikni tanlaydi va boshqa hech narsa
    oʻylanmaydi. Predlog yoʻq boʻlsagina soʻzning gapdagi ishiga
    qaraladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu gapdagi har bir soʻzning kelishigini ayting.<br>
     <b>Ве́чером я пишу́ бра́ту письмо́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ве́чером</strong> —
    Твори́тельный (kun qismi). <strong>Я</strong> — Имени́тельный (ega).
    <strong>Бра́ту</strong> — Да́тельный (kimga). <strong>Письмо́</strong>
    — Вини́тельный (nimani; oʻrta jins, oʻzgarmaydi).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Я говорю́ с ___ ___ ___.</b> (мой ста́рый друг)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>мои́м ста́рым дру́гом</strong>.
    <em>С</em> Твори́тельный oladi; uchta soʻz ham birga oʻzgaradi —
    olmosh <b>-им</b>, sifat <b>-ым</b>, ot <b>-ом</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nega bu ikki gap boshqa kelishik oladi?<br>
     <b>Я рабо́таю в магази́не. · Я иду́ в магази́н.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Feʼl hal qiladi. <em>Рабо́тать</em> —
    harakat emas, demak joy: <strong>Предло́жный</strong>. <em>Идти́</em>
    — harakat, demak manzil: <strong>Вини́тельный</strong>. Predlog ikkala
    gapda ham bir xil.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Oʻzbek tilida qaysi ruscha kelishikning aniq juftligi yoʻq?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Твори́тельный</strong>.
    Oʻzbekchada bu maʼno alohida kelishik bilan emas, <b>«bilan»</b> soʻzi
    bilan beriladi. Qolgan beshtasining juftligi bor — shuning uchun ular
    ancha tez oʻrganildi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>паде́ж</b><span>kelishik</span></li>
  <li><b>оконча́ние</b><span>qoʻshimcha</span></li>
  <li><b>предло́г</b><span>predlog</span></li>
  <li><b>род</b><span>jins</span></li>
  <li><b>вид</b><span>feʼl turi</span></li>
  <li><b>зда́ние</b><span>bino</span></li>
  <li><b>стадио́н</b><span>stadion</span></li>
  <li><b>доро́га</b><span>yoʻl</span></li>
  <li><b>знак</b><span>belgi</span></li>
  <li><b>про́сто</b><span>shunchaki</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Uch qadam: <b>predlog bormi → soʻzning ishi nima → jins va
        son</b>.</li>
    <li>Predlog bor boʻlsa, <b>u tanlaydi</b> — boshqa hech narsa
        oʻylanmaydi.</li>
    <li>Egalik olmoshi, sifat va ot <b>doim birga</b> oʻzgaradi.</li>
    <li>Feʼl ham kelishikni talab qiladi: <em>помога́ть</em> → Д.п.,
        <em>рабо́тать кем</em> → Т.п.</li>
    <li>Oʻzbekchada beshta kelishikning juftligi bor. Yangi boʻlgani
        <b>bittasi</b> — Твори́тельный.</li>
    <li>Uchta qiyinchilik edi: <b>jins, predloglar, urgʻu</b>.</li>
    <li>Keyingi tizim — <b>вид</b>: kelishik otga tegishli edi, вид
        feʼlga.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-51: Вид — tugallanmagan va tugallangan feʼl (что делать? / что сделать?)",
        "category": "russian",
        "order": 51,
        "summary": (
            "Rus tilining ikkinchi katta tizimi boshlanadi. Har bir feʼl ikki "
            "turdan biriga tegishli: jarayon yoki natija. Va bu tushuncha "
            "oʻzbekchada ham bor — faqat boshqa joyda yashaydi."
        ),
        "stories": ["Чита́л и прочита́л"],
        "content": """
<h2>PR-51: Вид — tugallanmagan va tugallangan feʼl (что делать? / что сделать?)</h2>

<p>Kelishiklar tugadi. Bugundan boshlab rus tilining <b>ikkinchi katta
tizimi</b> ochiladi — <b>вид</b> (feʼl turi). Kelishik <em>otga</em>
tegishli edi. Вид <em>feʼlga</em> tegishli, va u bitta savolga javob
beradi: <b>harakat tugadimi yoki yoʻqmi?</b></p>

<p>Yaxshi xabar shu: bu tushuncha oʻzbekchada <b>bor</b>. Siz uni har kuni
ishlatasiz. Faqat u boshqa joyda yashaydi — va bugungi darsning butun
maqsadi shuni koʻrsatish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Ikkita vidni ajratasiz: <b>НСВ</b> va <b>СВ</b></li>
    <li>Ularning savollarini bilasiz: <b>что де́лать?</b> / <b>что сде́лать?</b></li>
    <li><b>Чита́л</b> va <b>прочита́л</b> farqini tushunasiz</li>
    <li>Nega СВ da hozirgi zamon yoʻqligini bilasiz</li>
  </ul>
</div>

<div class="pr-aspect">
  <div class="pr-aspect__side">
    <p class="pr-aspect__h">НСВ — что де́лать?</p>
    <p class="pr-aspect__v">чита́ть</p>
    <p>Jarayon, takror, odat. «Oʻqirdim, oʻqiyapman, oʻqib turaman.»</p>
  </div>
  <div class="pr-aspect__side pr-aspect__side--sv">
    <p class="pr-aspect__h">СВ — что сде́лать?</p>
    <p class="pr-aspect__v">прочита́ть</p>
    <p>Natija, bir marta, oxirigacha. «Oʻqib chiqdim.»</p>
  </div>
</div>

<h3>1. Ikkita savol</h3>

<p>Rus tilida har bir feʼl <b>ikkita savoldan biriga</b> javob beradi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Savol</th><th>Vid</th><th>Toʻliq nomi</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">что де́лать?</td><td class="pr-end">НСВ</td>
      <td class="pr-uz">несоверше́нный вид</td><td class="pr-uz">tugallanmagan</td></tr>
  <tr><td class="pr-res">что сде́лать?</td><td class="pr-end">СВ</td>
      <td class="pr-uz">соверше́нный вид</td><td class="pr-uz">tugallangan</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Vidni aniqlashning eng tez yoʻli — <b>savolni aytib koʻrish</b>. Feʼlga
qarab oʻzingizdan soʻrang: «что <b>с</b>де́лать?» degan savolga toʻgʻri
kelyaptimi? Agar ha — bu СВ.<br><br>
Va koʻpincha buni <b>koʻz bilan</b> ham koʻrasiz: СВ feʼllarda odatda
qoʻshimcha bir boʻlak boʻladi — <em>чита́ть → <b>про</b>чита́ть</em>,
<em>писа́ть → <b>на</b>писа́ть</em>, <em>де́лать →
<b>с</b>де́лать</em>.</div>

<h3>2. Чита́л va прочита́л</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">Вчера́ ве́чером я <span class="pe-hl pe-hl--v">чита́л</span>
     кни́гу.</p>
  <p class="pe-ex__uz">Kecha kechqurun kitob oʻqidim (oʻqib oʻtirdim).</p>
  <p class="pe-ex__why"><b>НСВ</b> — jarayon. Nima qilganim aytilyapti,
     natija emas. Kitob tugadimi — nomaʼlum, va bu muhim emas.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Вчера́ я <span class="pe-hl pe-hl--v">прочита́л</span>
     кни́гу.</p>
  <p class="pe-ex__uz">Kecha kitobni oʻqib chiqdim.</p>
  <p class="pe-ex__why"><b>СВ</b> — natija. Kitob <b>tugadi</b>. Endi men
     uning oxirini bilaman.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Bu ikki savol <b>boshqa-boshqa</b> narsa soʻraydi:<br>
<em>Ты <b>чита́л</b> э́ту кни́гу?</em> — «Bu kitob bilan tanishmisan?»
Javob: ha, koʻrganman, bilaman.<br>
<em>Ты <b>прочита́л</b> э́ту кни́гу?</em> — «Oxirigacha oʻqib
chiqdingmi?» Javob: ha, tugatdim.<br>
Birinchisiga «ha» deb javob berib, ikkinchisiga «yoʻq» deyish mumkin — va
bu ziddiyat emas.</div>

<h3>3. НСВ nima uchun ishlatiladi</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Jarayon</p>
    <p><em>Я чита́л два часа́.</em><br>Ikki soat oʻqidim — davomiylik.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Takror</p>
    <p><em>Я чита́л э́ту кни́гу три ра́за.</em><br>Uch marta — takroriy.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Odat</p>
    <p><em>Ка́ждый ве́чер я чита́ю.</em><br>Har kuni — odat.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">4</span>Fakt</p>
    <p><em>Ты чита́л Толсто́го?</em><br>Umuman: tanishmisan?</p></div>
</div>

<h3>4. СВ nima uchun ishlatiladi</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Natija</p>
    <p><em>Я прочита́л кни́гу.</em><br>Kitob tugadi.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Bir marta</p>
    <p><em>Он позвони́л у́тром.</em><br>Bir marta qoʻngʻiroq qildi.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Ketma-ketlik</p>
    <p><em>Он пришёл, сел и написа́л письмо́.</em><br>Uch tugagan ish, ketma-ket.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">4</span>Kutilgan natija</p>
    <p><em>Наконе́ц он поня́л.</em><br>Nihoyat tushundi.</p></div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana bu darsning yuragi. Oʻzbek tilida bu tushuncha <b>bor</b>, va siz uni
kuniga oʻn marta ishlatasiz:<br><br>
<em>oʻqi<b>dim</b></em> — oddiy oʻtgan zamon<br>
<em>oʻqi<b>b chiqdim</b></em> — oxirigacha, tugatdim<br>
<em>yoz<b>dim</b></em> · <em>yoz<b>ib qoʻydim</b></em><br>
<em>ye<b>dim</b></em> · <em>ye<b>b qoʻydim</b></em><br><br>
Yaʼni oʻzbekchada tugallanganlikni <b>ikkinchi feʼl</b> koʻrsatadi —
<em>chiqmoq, qoʻymoq, bermoq, olmoq, yubormoq</em>. U asosiy feʼlning
<b>yonida</b> turadi.<br><br>
Rus tilida esa u feʼlning <b>ichiga</b> kiradi:
<em>чита́ть → <b>про</b>чита́ть</em>. Bitta soʻz, ikkita maʼno.<br><br>
<b>Va bitta muhim farq bor.</b> Oʻzbekchada <em>oʻqidim</em> —
<b>neytral</b>: u tugagan-tugamaganini aytmaydi. Ruschada esa neytral
shakl <b>yoʻq</b>. Har safar tanlash kerak: <em>чита́л</em> mi yoki
<em>прочита́л</em> mi. Aynan shu narsa vidni qiyin qiladi — qoida emas,
<b>majburiy tanlov</b>.</div>

<h3>5. СВ da hozirgi zamon yoʻq</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Bu mantiqiy: agar harakat <b>tugagan</b> boʻlsa, u <b>hozir</b> boʻla
olmaydi. Shuning uchun:<br>
<b>НСВ</b> — uchala zamon: <em>чита́л · чита́ю · бу́ду чита́ть</em><br>
<b>СВ</b> — faqat ikkita: <em>прочита́л · —— · прочита́ю</em><br><br>
Va diqqat: <em>прочита́ю</em> hozirgi zamonga <b>oʻxshaydi</b>, lekin u
<b>kelasi zamon</b>. Bu PR-24 da vaʼda qilingan «ikkinchi kelasi zamon» —
endi siz uning nima ekanini bilasiz.</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Vid</th><th>Kecha</th><th>Bugun</th><th>Ertaga</th></tr>
  <tr><td class="pr-res">НСВ — чита́ть</td><td class="pr-end">чита́л</td>
      <td class="pr-end">чита́ю</td><td class="pr-end">бу́ду чита́ть</td></tr>
  <tr><td class="pr-res">СВ — прочита́ть</td><td class="pr-end">прочита́л</td>
      <td class="pr-uz">— (yoʻq)</td><td class="pr-end">прочита́ю</td></tr>
</table></div>

<h3>6. Lugʻatda feʼllar juftlab beriladi</h3>

<p>Shuning uchun rus lugʻatlarida feʼllar <b>ikkitadan</b> yoziladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>НСВ</th><th>СВ</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">чита́ть</td><td class="pr-end">прочита́ть</td>
      <td class="pr-uz">oʻqimoq</td></tr>
  <tr><td class="pr-res">писа́ть</td><td class="pr-end">написа́ть</td>
      <td class="pr-uz">yozmoq</td></tr>
  <tr><td class="pr-res">де́лать</td><td class="pr-end">сде́лать</td>
      <td class="pr-uz">qilmoq</td></tr>
  <tr><td class="pr-res">смотре́ть</td><td class="pr-end">посмотре́ть</td>
      <td class="pr-uz">qaramoq</td></tr>
  <tr><td class="pr-res">звони́ть</td><td class="pr-end">позвони́ть</td>
      <td class="pr-uz">qoʻngʻiroq qilmoq</td></tr>
  <tr><td class="pr-res">учи́ть</td><td class="pr-end">вы́учить</td>
      <td class="pr-uz">yodlamoq</td></tr>
</table></div>

<p>Yangi feʼlni yodlaganda uni <b>juft holda</b> yodlang. Bu qoʻshimcha ish
emas — bu vaqtni tejaydi, chunki keyin oʻylab oʻtirmaysiz.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я прочита́ю сейча́с.</s> <em>(«hozir oʻqiyapman» maʼnosida)</em></p>
  <p class="pe-good">Я <b>чита́ю</b> сейча́с — СВ da hozirgi zamon yoʻq</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Вчера́ я прочита́л два часа́.</s></p>
  <p class="pe-good">Вчера́ я <b>чита́л</b> два часа́ — davomiylik НСВ talab qiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ка́ждый день я прочита́л кни́гу.</s></p>
  <p class="pe-good">Ка́ждый день я <b>чита́л</b> — takror НСВ talab qiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я чита́л кни́гу до конца́.</s></p>
  <p class="pe-good">Я <b>прочита́л</b> кни́гу — «oxirigacha» natija, demak СВ</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu feʼl qaysi vidda? <b>написа́ть</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>СВ</strong>. Savol: «что
    <b>с</b>де́лать? — написа́ть». Va koʻz bilan ham koʻrinadi: oldida
    <b>на-</b> qoʻshimchasi bor.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>чита́л</b> yoki <b>прочита́л</b>? &nbsp; <b>Вчера́ я ___ три
     часа́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>чита́л</strong>. «Uch soat» —
    davomiylik, jarayon. НСВ. Agar <em>прочита́л</em> deyilsa, gap
    natijaga qaraydi va «uch soat» bilan mos kelmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega СВ da hozirgi zamon yoʻq?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki СВ <strong>tugagan</strong> ishni
    bildiradi, tugagan ish esa <b>hozir</b> boʻla olmaydi. Shuning uchun
    <em>прочита́ю</em> shakli hozirgi zamonga oʻxshasa ham, u
    <strong>kelasi zamon</strong>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu ikki savol nima farq qiladi?<br>
     <b>Ты чита́л кни́гу? · Ты прочита́л кни́гу?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi: «bu kitob bilan
    tanishmisan?» Ikkinchisi: «oxirigacha oʻqib chiqdingmi?»
    Birinchisiga «ha», ikkinchisiga «yoʻq» deb javob berish mumkin — bu
    ziddiyat emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Oʻzbekchada tugallanganlik qanday koʻrsatiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ikkinchi feʼl bilan</strong>:
    <em>oʻqi<b>b chiqdim</b></em>, <em>yoz<b>ib qoʻydim</b></em>. Yaʼni
    tushuncha bor, lekin u feʼlning <b>yonida</b> turadi. Ruschada esa u
    feʼlning <b>ichiga</b> kiradi. Va bitta muhim farq: oʻzbekcha
    <em>oʻqidim</em> neytral, ruschada esa neytral shakl yoʻq — har safar
    tanlash kerak.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>вид</b><span>feʼl turi</span></li>
  <li><b>НСВ (несоверше́нный)</b><span>tugallanmagan</span></li>
  <li><b>СВ (соверше́нный)</b><span>tugallangan</span></li>
  <li><b>проце́сс</b><span>jarayon</span></li>
  <li><b>результа́т</b><span>natija</span></li>
  <li><b>прочита́ть</b><span>oʻqib chiqmoq</span></li>
  <li><b>написа́ть</b><span>yozib boʻlmoq</span></li>
  <li><b>сде́лать</b><span>qilib boʻlmoq</span></li>
  <li><b>наконе́ц</b><span>nihoyat</span></li>
  <li><b>ра́зница</b><span>farq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Har bir rus feʼli <b>ikki vidning biriga</b> tegishli.</li>
    <li><b>НСВ</b> — что де́лать? — jarayon, takror, odat, fakt.</li>
    <li><b>СВ</b> — что сде́лать? — natija, bir marta, ketma-ketlik.</li>
    <li><b>СВ da hozirgi zamon yoʻq.</b> <em>Прочита́ю</em> — kelasi
        zamon.</li>
    <li>Feʼllar lugʻatda <b>juftlab</b> beriladi — shunday ham
        yodlang.</li>
    <li>Oʻzbekchada tushuncha bor, lekin u <b>ikkinchi feʼl</b> bilan
        beriladi (<em>oʻqib chiqdim</em>).</li>
    <li>Eng katta farq: oʻzbekchada <b>neytral</b> shakl bor, ruschada —
        <b>yoʻq</b>. Tanlov majburiy.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-52: Vid juftliklarini yasash: prefiks, suffiks va butunlay boshqa oʻzak",
        "category": "russian",
        "order": 52,
        "summary": (
            "Vid juftliklari uch yoʻl bilan yasaladi. Ikkitasi qoidali va tez "
            "oʻrganiladi; uchinchisi esa yodlanadi — lekin unda atigi bir necha "
            "feʼl bor."
        ),
        "stories": ["Ремо́нт на ку́хне"],
        "content": """
<h2>PR-52: Vid juftliklarini yasash: prefiks, suffiks va butunlay boshqa oʻzak</h2>

<p>Kecha siz vid <b>nima</b> ekanini bildingiz. Bugun — u <b>qanday</b>
yasalishi. Yaxshi xabar: yoʻllar atigi uchta, va ikkitasi qoidali.
Yomonroq xabar: uchinchisida qoida yoʻq. Lekin unda feʼl ham kam — oʻn
beshtacha, va ular eng koʻp ishlatiladigan feʼllar, shuning uchun tez
oʻtiradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Prefiks</b> bilan yasalgan juftliklarni oʻrganasiz</li>
    <li><b>Suffiks</b> bilan yasalganlarini bilasiz</li>
    <li>Butunlay boshqa oʻzakli juftliklarni yodlaysiz</li>
    <li>Oʻzbekcha «-b qoʻymoq» bilan solishtirasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch yoʻl</span>
  <span class="pe-chip pe-chip--v">про + чита́ть</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">реши́ть → реша́ть</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">говори́ть → сказа́ть</span>
</div>

<h3>1. Prefiks — НСВ dan СВ yasaladi</h3>

<p>Eng koʻp uchraydigan yoʻl. Feʼlning <b>oldiga</b> bir boʻlak
qoʻshiladi, va maʼno oʻzgarmaydi — faqat vid oʻzgaradi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Prefiks</th><th>НСВ</th><th>СВ</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">про-</td><td class="pr-uz">чита́ть</td>
      <td class="pr-end">прочита́ть</td><td class="pr-uz">oʻqimoq</td></tr>
  <tr><td class="pr-res">на-</td><td class="pr-uz">писа́ть</td>
      <td class="pr-end">написа́ть</td><td class="pr-uz">yozmoq</td></tr>
  <tr><td class="pr-res">с-</td><td class="pr-uz">де́лать</td>
      <td class="pr-end">сде́лать</td><td class="pr-uz">qilmoq</td></tr>
  <tr><td class="pr-res">по-</td><td class="pr-uz">смотре́ть</td>
      <td class="pr-end">посмотре́ть</td><td class="pr-uz">qaramoq</td></tr>
  <tr><td class="pr-res">по-</td><td class="pr-uz">звони́ть</td>
      <td class="pr-end">позвони́ть</td><td class="pr-uz">qoʻngʻiroq qilmoq</td></tr>
  <tr><td class="pr-res">вы-</td><td class="pr-uz">учи́ть</td>
      <td class="pr-end">вы́учить</td><td class="pr-uz">yodlamoq</td></tr>
  <tr><td class="pr-res">по-</td><td class="pr-uz">стро́ить</td>
      <td class="pr-end">постро́ить</td><td class="pr-uz">qurmoq</td></tr>
  <tr><td class="pr-res">при-</td><td class="pr-uz">гото́вить</td>
      <td class="pr-end">пригото́вить</td><td class="pr-uz">tayyorlamoq</td></tr>
  <tr><td class="pr-res">у-</td><td class="pr-uz">ви́деть</td>
      <td class="pr-end">уви́деть</td><td class="pr-uz">koʻrmoq</td></tr>
  <tr><td class="pr-res">у-</td><td class="pr-uz">слы́шать</td>
      <td class="pr-end">услы́шать</td><td class="pr-uz">eshitmoq</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Qaysi prefiks kerakligini <b>taxmin qilib boʻlmaydi</b>. Nega
<em>чита́ть</em> ga <em>про-</em>, <em>писа́ть</em> ga esa
<em>на-</em>? Qoida yoʻq — bu tarix.<br><br>
Shuning uchun feʼlni <b>juft holda</b> yodlash kerak. Bu qoʻshimcha ish
emas: baribir ikkala shaklni bilishingiz kerak, shunchaki ularni birga
yodlaysiz.<br><br>
<b>Va bitta ogohlantirish.</b> Har bir prefiks vidni oʻzgartiravermaydi —
baʼzilari <b>maʼnoni</b> ham oʻzgartiradi:
<em>чита́ть → <b>пере</b>чита́ть</em> (qayta oʻqimoq),
<em>писа́ть → <b>под</b>писа́ть</em> (imzolamoq). Bunday prefikslarni
PR-57 va PR-58 da alohida koʻramiz.</div>

<h3>2. Suffiks — СВ dan НСВ yasaladi</h3>

<p>Bu yoʻl <b>teskari</b> ishlaydi: avval СВ boʻladi, undan НСВ yasaladi.
Va bu yerda <b>qoida bor</b>:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>СВ</th><th>НСВ</th><th>Naqsh</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">реши́ть</td><td class="pr-end">реша́ть</td>
      <td class="pr-uz">-ить → -ать</td><td class="pr-uz">hal qilmoq</td></tr>
  <tr><td class="pr-res">получи́ть</td><td class="pr-end">получа́ть</td>
      <td class="pr-uz">-ить → -ать</td><td class="pr-uz">olmoq</td></tr>
  <tr><td class="pr-res">отве́тить</td><td class="pr-end">отвеча́ть</td>
      <td class="pr-uz">-ить → -ать</td><td class="pr-uz">javob bermoq</td></tr>
  <tr><td class="pr-res">изучи́ть</td><td class="pr-end">изуча́ть</td>
      <td class="pr-uz">-ить → -ать</td><td class="pr-uz">oʻrganmoq</td></tr>
  <tr><td class="pr-res">откры́ть</td><td class="pr-end">открыва́ть</td>
      <td class="pr-uz">+ -ыва-</td><td class="pr-uz">ochmoq</td></tr>
  <tr><td class="pr-res">рассказа́ть</td><td class="pr-end">расска́зывать</td>
      <td class="pr-uz">+ -ыва-</td><td class="pr-uz">soʻzlab bermoq</td></tr>
  <tr><td class="pr-res">показа́ть</td><td class="pr-end">пока́зывать</td>
      <td class="pr-uz">+ -ыва-</td><td class="pr-uz">koʻrsatmoq</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bu guruhni tanish oson: <b>uzunroq shakl НСВ boʻladi</b>. Prefiks
guruhida esa teskari — u yerda uzunroq shakl СВ edi.<br>
<em>чита́ть (qisqa, НСВ) → прочита́ть (uzun, СВ)</em><br>
<em>откры́ть (qisqa, СВ) → открыва́ть (uzun, НСВ)</em><br>
Yaʼni uzunlikka emas, <b>yoʻnalishga</b> qarang: prefiks qoʻshilsa —
СВ tomonga; suffiks qoʻshilsa — НСВ tomonga.</div>

<h3>3. Butunlay boshqa oʻzak</h3>

<p>Bu guruhda qoida <b>yoʻq</b> — ikkita shakl bir-biriga umuman
oʻxshamaydi. Lekin ular soni kam va juda koʻp ishlatiladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>НСВ</th><th>СВ</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">говори́ть</td><td class="pr-end">сказа́ть</td>
      <td class="pr-uz">gapirmoq / aytmoq</td></tr>
  <tr><td class="pr-res">брать</td><td class="pr-end">взять</td>
      <td class="pr-uz">olmoq</td></tr>
  <tr><td class="pr-res">класть</td><td class="pr-end">положи́ть</td>
      <td class="pr-uz">qoʻymoq</td></tr>
  <tr><td class="pr-res">лови́ть</td><td class="pr-end">пойма́ть</td>
      <td class="pr-uz">tutmoq</td></tr>
  <tr><td class="pr-res">иска́ть</td><td class="pr-end">найти́</td>
      <td class="pr-uz">qidirmoq / topmoq</td></tr>
  <tr><td class="pr-res">сади́ться</td><td class="pr-end">сесть</td>
      <td class="pr-uz">oʻtirmoq</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Говори́ть — сказа́ть</b> juftligini alohida yodlang, chunki u eng koʻp
ishlatiladi va oʻzbekchada ham ikki xil tarjima qilinadi:<br>
<em>Он <b>говори́л</b> до́лго</em> — «uzoq gapirdi» (jarayon)<br>
<em>Он <b>сказа́л</b> одно́ сло́во</em> — «bitta soʻz aytdi» (natija)<br>
Va e'tibor bering: <em>говори́ть</em> «gapirmoq», <em>сказа́ть</em> esa
«aytmoq» — oʻzbekchada ham ikkita boshqa feʼl.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Kechagi solishtiruvni davom ettiramiz — va u bugun yanada aniqroq
boʻladi.<br><br>
Oʻzbekchada tugallanganlikni koʻrsatadigan <b>yopiq roʻyxat</b> bor:
<em>-b <b>qoʻymoq</b></em>, <em>-b <b>chiqmoq</b></em>, <em>-b
<b>bermoq</b></em>, <em>-b <b>olmoq</b></em>, <em>-b
<b>yubormoq</b></em>, <em>-b <b>tashlamoq</b></em>. Oltitacha
yordamchi feʼl, tamom.<br><br>
Rus tilida ham shunday yopiq roʻyxat bor — faqat u <b>prefikslardan</b>
iborat: <b>про-, на-, с-, по-, вы-, при-, у-</b>. Yettitacha, tamom.<br><br>
Yaʼni ikkala til ham bir xil ish qiladi: asosiy feʼlga <b>kichkina bir
boʻlak</b> qoʻshib, «tugadi» degan maʼnoni chiqaradi. Oʻzbekchada bu
boʻlak <b>alohida soʻz</b> va <b>orqada</b> turadi; ruschada esa u
<b>soʻzning bir qismi</b> va <b>oldinda</b> turadi.<br><br>
Va oʻxshashlik yana chuqurroq: oʻzbekchada ham qaysi yordamchi feʼl
kerakligini <b>taxmin qilib boʻlmaydi</b>. Nega «yozib <b>qoʻydim</b>»
lekin «oʻqib <b>chiqdim</b>»? Odat. Ruschada ham xuddi shunday: nega
<em>на</em>писа́ть lekin <em>про</em>чита́ть? Odat.</div>

<h3>4. Amalda</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">Ма́ма <span class="pe-hl pe-hl--v">гото́вила</span>
     у́жин два часа́. В во́семь она́
     <span class="pe-hl pe-hl--v">пригото́вила</span> его́.</p>
  <p class="pe-ex__uz">Onam kechki ovqatni ikki soat tayyorladi. Soat
     sakkizda tayyorlab boʻldi.</p>
  <p class="pe-ex__why">Bitta juftlik, ikkita jumla: davomiylik (НСВ) va
     natija (СВ). Oʻzbekchada ham xuddi shunday — «tayyorladi» va
     «tayyorlab boʻldi».</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Он до́лго
     <span class="pe-hl pe-hl--v">иска́л</span> ключи́ и наконе́ц
     <span class="pe-hl pe-hl--v">нашёл</span> их.</p>
  <p class="pe-ex__uz">U kalitlarni uzoq qidirdi va nihoyat topdi.</p>
  <p class="pe-ex__why">Butunlay boshqa oʻzak: <em>иска́ть — найти́</em>.
     Oʻzbekchada ham ikkita boshqa feʼl: «qidirmoq» va «topmoq».</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я прочита́ть кни́гу вчера́.</s></p>
  <p class="pe-good">Я <b>прочита́л</b> кни́гу вчера́ — infinitiv kesim boʻlolmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он сказа́л до́лго.</s></p>
  <p class="pe-good">Он <b>говори́л</b> до́лго — davomiylik НСВ talab qiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ка́ждый день он сказа́л пра́вду.</s></p>
  <p class="pe-good">Ка́ждый день он <b>говори́л</b> пра́вду — takror НСВ</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он до́лго иска́л и иска́л ключи́.</s> <em>(«topdi» maʼnosida)</em></p>
  <p class="pe-good">Он до́лго иска́л и <b>нашёл</b> ключи́ — natija СВ talab qiladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>де́лать</b> feʼlining СВ jufti qaysi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>сде́лать</strong>. Prefiks
    <b>с-</b>. Qaysi prefiks kerakligini taxmin qilib boʻlmaydi — shuning
    uchun juftlab yodlanadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>откры́ть</b> feʼlining НСВ jufti qaysi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>открыва́ть</strong>. Bu ikkinchi
    guruh: СВ dan НСВ <b>suffiks</b> bilan yasaladi. Bu yerda uzunroq
    shakl — НСВ.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>говори́ть</b> feʼlining СВ jufti qaysi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>сказа́ть</strong>. Uchinchi
    guruh: butunlay boshqa oʻzak. Oʻzbekchada ham ikkita boshqa feʼl —
    «gapirmoq» va «aytmoq».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu juftlikda qaysi biri НСВ?<br>
     <b>рассказа́ть · расска́зывать</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>расска́зывать</strong> — unda
    <b>-ыва-</b> suffiksi bor. Suffiks qoʻshilsa — НСВ tomonga; prefiks
    qoʻshilsa — СВ tomonga. Yoʻnalishga qarang, uzunlikka emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Boʻsh joyga: <b>Он до́лго ___ ключи́ и наконе́ц ___ их.</b>
     (иска́ть / найти́)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>иска́л … нашёл</strong>.
    «До́лго» — davomiylik, demak НСВ. «Наконе́ц» — natija, demak СВ.
    Bu ikki soʻz vidni deyarli har doim aytib turadi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>реши́ть / реша́ть</b><span>hal qilmoq</span></li>
  <li><b>откры́ть / открыва́ть</b><span>ochmoq</span></li>
  <li><b>рассказа́ть / расска́зывать</b><span>soʻzlab bermoq</span></li>
  <li><b>сказа́ть</b><span>aytmoq (СВ)</span></li>
  <li><b>взять</b><span>olmoq (СВ)</span></li>
  <li><b>найти́</b><span>topmoq (СВ)</span></li>
  <li><b>положи́ть</b><span>qoʻymoq (СВ)</span></li>
  <li><b>ремо́нт</b><span>taʼmir</span></li>
  <li><b>кра́сить / покра́сить</b><span>boʻyamoq</span></li>
  <li><b>выбира́ть / вы́брать</b><span>tanlamoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Prefiks</b>: НСВ → СВ. <em>чита́ть → прочита́ть</em>.
        Qaysi prefiks — taxmin qilib boʻlmaydi.</li>
    <li><b>Suffiks</b>: СВ → НСВ. <em>откры́ть → открыва́ть</em>.
        Bu yerda qoida bor.</li>
    <li><b>Boshqa oʻzak</b>: <em>говори́ть — сказа́ть</em>,
        <em>брать — взять</em>, <em>иска́ть — найти́</em>. Yodlanadi,
        lekin ular kam.</li>
    <li>Yoʻnalishga qarang: prefiks → СВ tomonga, suffiks → НСВ
        tomonga.</li>
    <li>Feʼlni har doim <b>juft holda</b> yodlang.</li>
    <li>Oʻzbekchada ham yopiq roʻyxat bor — <em>qoʻymoq, chiqmoq,
        bermoq…</em> Ikkala tilda ham qaysi biri kerakligi
        <b>odat</b>.</li>
  </ul>
</div>
""",
    },
]
