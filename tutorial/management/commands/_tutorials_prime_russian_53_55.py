# -*- coding: utf-8 -*-
"""Prime Russian — Block E davomi (53–55).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-53 — вид uch zamonda. Bu yerda IKKI KELASI ZAMON ochiladi: бу́ду
чита́ть (jarayon) va прочита́ю (natija). Va СВ ning kelasi zamoni hozirgi
zamon kabi tuslanadi — bu oʻquvchini chalgʻitmasligi kerak.
PR-54 — vidni tanlash. Bu amaliy dars: SIGNAL SOʻZLAR roʻyxati (ка́ждый
день → НСВ, наконе́ц → СВ) oʻquvchiga tez qaror qabul qilishga yordam
beradi.
PR-55 — harakat feʼllari boshlanadi: идти́ ↔ ходи́ть. Oʻzbekcha bu yerda
kutilmaganda yaxshi yordam beradi: boryapman ↔ borib turaman ↔ borib
keldim.

Mashqlar:        practice/management/commands/_practice_pr_53_55.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_53_55.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_53_55.py --author=prime
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
        "title": "PR-53: Vid uch zamonda: hozirgi zamonda СВ nega yoʻq?",
        "category": "russian",
        "order": 53,
        "summary": (
            "Rus tilida ikkita kelasi zamon bor — va ikkalasi ham kerak. "
            "«Бу́ду чита́ть» vaʼda bermaydi, «прочита́ю» esa beradi. Farq shu "
            "yerda."
        ),
        "stories": ["Три письма́ об одно́м дне"],
        "content": """
<h2>PR-53: Vid uch zamonda: hozirgi zamonda СВ nega yoʻq?</h2>

<p>PR-51 da bir gap aytilgan edi: «СВ da hozirgi zamon yoʻq». Bugun bu gap
toʻliq ochiladi — va undan qiziq bir natija chiqadi: rus tilida
<b>ikkita kelasi zamon</b> bor. Ular bir xil emas, va ikkalasi ham
kerak.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Vid va zamon jadvalini toʻliq koʻrasiz</li>
    <li>Ikki kelasi zamonni ajratasiz: <b>бу́ду чита́ть</b> va <b>прочита́ю</b></li>
    <li>СВ kelasi zamoni qanday yasalishini bilasiz</li>
    <li>Nega hozirgi zamonda СВ boʻlmasligini tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikkita kelasi zamon</span>
  <span class="pe-chip pe-chip--o">бу́ду чита́ть</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">прочита́ю</span>
</div>

<h3>1. Butun jadval</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Vid</th><th>Kecha</th><th>Bugun</th><th>Ertaga</th></tr>
  <tr><td class="pr-res">НСВ — чита́ть</td><td class="pr-end">чита́л</td>
      <td class="pr-end">чита́ю</td><td class="pr-end">бу́ду чита́ть</td></tr>
  <tr><td class="pr-res">СВ — прочита́ть</td><td class="pr-end">прочита́л</td>
      <td class="pr-uz">— (yoʻq)</td><td class="pr-end">прочита́ю</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Nega hozirgi zamonda СВ yoʻq — mantiq oddiy. СВ <b>tugagan</b> ishni
bildiradi. Agar ish <b>hozir</b> davom etayotgan boʻlsa, u tugamagan.
Agar u tugagan boʻlsa, u <b>hozir</b> emas. Ikkalasi bir vaqtda boʻlishi
mumkin emas.<br><br>
Shuning uchun СВ da <b>ikkita</b> zamon bor: oʻtgan (tugagan) va kelasi
(tugaydi). Oʻrtada — hech narsa.</div>

<h3>2. СВ kelasi zamoni — hozirgi zamon kabi tuslanadi</h3>

<p>Bu joyi oʻquvchini chalgʻitadi, shuning uchun diqqat qiling. НСВ da
kelasi zamon <b>ikki soʻz</b> edi (<em>бу́ду чита́ть</em>, PR-24). СВ da
esa u <b>bir soʻz</b> — va u hozirgi zamon shakli kabi tuslanadi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>НСВ (kelasi)</th><th>СВ (kelasi)</th></tr>
  <tr><td>я</td><td class="pr-uz">бу́ду чита́ть</td><td class="pr-end">прочита́ю</td></tr>
  <tr><td>ты</td><td class="pr-uz">бу́дешь чита́ть</td><td class="pr-end">прочита́ешь</td></tr>
  <tr><td>он / она́</td><td class="pr-uz">бу́дет чита́ть</td><td class="pr-end">прочита́ет</td></tr>
  <tr><td>мы</td><td class="pr-uz">бу́дем чита́ть</td><td class="pr-end">прочита́ем</td></tr>
  <tr><td>вы</td><td class="pr-uz">бу́дете чита́ть</td><td class="pr-end">прочита́ете</td></tr>
  <tr><td>они́</td><td class="pr-uz">бу́дут чита́ть</td><td class="pr-end">прочита́ют</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<em>Прочита́ю</em> shakli <em>чита́ю</em> ga juda oʻxshaydi — lekin
<em>чита́ю</em> <b>hozir</b>, <em>прочита́ю</em> esa <b>ertaga</b>.
Farq faqat prefiksda.<br><br>
Boshqa misollar: <em>напишу́</em> (yozaman — ertaga), <em>скажу́</em>
(aytaman), <em>сде́лаю</em> (qilaman), <em>возьму́</em> (olaman),
<em>найду́</em> (topaman), <em>куплю́</em> (sotib olaman). Ularning
hammasi <b>kelasi zamon</b>, garchi hozirgi zamon kabi
koʻrinsa ham.</div>

<h3>3. Ikki kelasi zamonning farqi</h3>

<div class="pr-aspect">
  <div class="pr-aspect__side">
    <p class="pr-aspect__h">бу́ду чита́ть — НСВ</p>
    <p class="pr-aspect__v">jarayon</p>
    <p>«Oʻqiyman, oʻqib oʻtiraman.» Tugatish haqida hech narsa aytilmagan.
       <b>Vaʼda yoʻq.</b></p>
  </div>
  <div class="pr-aspect__side pr-aspect__side--sv">
    <p class="pr-aspect__h">прочита́ю — СВ</p>
    <p class="pr-aspect__v">natija</p>
    <p>«Oʻqib chiqaman.» Kitob tugaydi. <b>Vaʼda bor.</b></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">За́втра ве́чером я
     <span class="pe-hl pe-hl--v">бу́ду чита́ть</span>.</p>
  <p class="pe-ex__uz">Ertaga kechqurun kitob oʻqiyman.</p>
  <p class="pe-ex__why">Nima qilishim aytilyapti — natija emas. Kitob
     tugaydimi, nomaʼlum.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">За́втра я
     <span class="pe-hl pe-hl--v">прочита́ю</span> э́ту кни́гу.</p>
  <p class="pe-ex__uz">Ertaga bu kitobni oʻqib chiqaman.</p>
  <p class="pe-ex__why">Bu — vaʼda. Ertaga kitob tugaydi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu yerda oʻzbekcha yana yordam beradi — chunki oʻzbekchada ham amalda
<b>ikkita kelasi zamon</b> bor:<br><br>
<em>Ertaga kitob <b>oʻqiyman</b></em> → <em>бу́ду чита́ть</em><br>
<em>Ertaga kitobni <b>oʻqib chiqaman</b></em> → <em>прочита́ю</em><br><br>
Farq ikkala tilda ham bir xil: birinchisi <b>nima qilishimni</b> aytadi,
ikkinchisi <b>nima tugashini</b>.<br><br>
Faqat bitta narsa boshqa. Oʻzbekchada <em>oʻqiyman</em> — <b>neytral</b>,
uni ikkala maʼnoda ham ishlatish mumkin. Ruschada esa <em>бу́ду
чита́ть</em> aniq jarayonni bildiradi va natija haqida <b>hech narsa
vaʼda qilmaydi</b>. Agar kimdir sizdan natija kutayotgan boʻlsa —
<em>прочита́ю</em> deb aytish kerak.</div>

<h3>4. Oʻtgan zamonda ikkalasi ham bor</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">Вчера́ я <span class="pe-hl pe-hl--v">чита́л</span>
     весь ве́чер, но не <span class="pe-hl pe-hl--v">прочита́л</span>.</p>
  <p class="pe-ex__uz">Kecha butun kechqurun oʻqidim, lekin oʻqib
     chiqmadim.</p>
  <p class="pe-ex__why">Bitta gapda ikkala vid ham bor va ular
     <b>qarama-qarshi emas</b>: jarayon boʻldi, natija boʻlmadi. Bu — vid
     tizimining butun kuchi.</p>
</div>

<h3>5. Amaliy natija</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Nima demoqchisiz</th><th>Qaysi shakl</th><th>Misol</th></tr>
  <tr><td class="pr-uz">Hozir qilyapman</td><td class="pr-res">НСВ hozirgi</td>
      <td class="pr-end">Я чита́ю.</td></tr>
  <tr><td class="pr-uz">Kecha qildim (jarayon)</td><td class="pr-res">НСВ oʻtgan</td>
      <td class="pr-end">Я чита́л.</td></tr>
  <tr><td class="pr-uz">Kecha tugatdim</td><td class="pr-res">СВ oʻtgan</td>
      <td class="pr-end">Я прочита́л.</td></tr>
  <tr><td class="pr-uz">Ertaga qilaman (jarayon)</td><td class="pr-res">НСВ kelasi</td>
      <td class="pr-end">Я бу́ду чита́ть.</td></tr>
  <tr><td class="pr-uz">Ertaga tugataman</td><td class="pr-res">СВ kelasi</td>
      <td class="pr-end">Я прочита́ю.</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Сейча́с я прочита́ю кни́гу.</s> <em>(«hozir oʻqiyapman» maʼnosida)</em></p>
  <p class="pe-good">Сейча́с я <b>чита́ю</b> кни́гу — <em>прочита́ю</em> kelasi zamon</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>За́втра я бу́ду прочита́ть.</s></p>
  <p class="pe-good">За́втра я <b>прочита́ю</b> — СВ da <em>бу́ду</em> ishlatilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я бу́ду написа́ть письмо́.</s></p>
  <p class="pe-good">Я <b>напишу́</b> письмо́ — СВ oʻzi kelasi zamonni bildiradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он прочита́ет ка́ждый день.</s></p>
  <p class="pe-good">Он <b>бу́дет чита́ть</b> ка́ждый день — takror НСВ talab qiladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Nega СВ da hozirgi zamon yoʻq?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki СВ <strong>tugagan</strong> ishni
    bildiradi. Hozir davom etayotgan ish tugamagan; tugagan ish esa hozir
    emas. Ikkalasi bir vaqtda boʻlolmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>прочита́ю</b> — bu qaysi zamon?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Kelasi zamon</strong>. U hozirgi
    zamon kabi tuslanadi (<em>прочита́ю, прочита́ешь, прочита́ет…</em>),
    lekin СВ da hozirgi zamon yoʻq — shuning uchun bu shakl faqat kelasi
    zamonni bildiradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapning farqi nima?<br>
     <b>За́втра я бу́ду чита́ть. · За́втра я прочита́ю кни́гу.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — <strong>jarayon</strong>:
    oʻqiyman, lekin tugatish haqida vaʼda yoʻq. Ikkinchisi —
    <strong>natija</strong>: kitob ertaga tugaydi. Bu vaʼda.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga: <b>За́втра я ___ письмо́.</b> («yozib boʻlaman» maʼnosida)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>напишу́</strong>. СВ oʻzi kelasi
    zamonni bildiradi — <em>бу́ду</em> qoʻshilmaydi. <em>«Бу́ду
    написа́ть»</em> — xato.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Вчера́ я чита́л, но не прочита́л. &nbsp; б) Сейча́с я чита́ю.<br>
     в) За́втра я бу́ду прочита́ть. &nbsp; г) За́втра я прочита́ю.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. СВ kelasi zamonni
    <b>oʻzi</b> bildiradi, shuning uchun <em>бу́ду</em> kerak emas.
    Toʻgʻrisi — <b>За́втра я прочита́ю</b>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>прочита́ю</b><span>oʻqib chiqaman (ertaga)</span></li>
  <li><b>напишу́</b><span>yozib boʻlaman</span></li>
  <li><b>скажу́</b><span>aytaman</span></li>
  <li><b>сде́лаю</b><span>qilib boʻlaman</span></li>
  <li><b>возьму́</b><span>olaman</span></li>
  <li><b>найду́</b><span>topaman</span></li>
  <li><b>куплю́</b><span>sotib olaman</span></li>
  <li><b>обеща́ние</b><span>vaʼda</span></li>
  <li><b>вы́бор</b><span>tanlov</span></li>
  <li><b>прав</b><span>haq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>НСВ</b> — uchala zamon. <b>СВ</b> — faqat oʻtgan va kelasi.</li>
    <li>Hozirgi zamonda СВ <b>boʻlishi mumkin emas</b>: tugagan ish hozir
        emas.</li>
    <li>СВ kelasi zamoni <b>bir soʻz</b> va hozirgi zamon kabi tuslanadi:
        <em>прочита́ю, напишу́, скажу́</em>.</li>
    <li>СВ bilan <b>бу́ду ishlatilmaydi</b>.</li>
    <li><b>Бу́ду чита́ть</b> — vaʼda yoʻq. <b>Прочита́ю</b> — vaʼda
        bor.</li>
    <li>Oʻzbekchada ham ikkita kelasi zamon bor: <em>oʻqiyman</em> ↔
        <em>oʻqib chiqaman</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-54: Vidni tanlash: takror, jarayon, natija, bir marta, buyruq",
        "category": "russian",
        "order": 54,
        "summary": (
            "Vid qoida emas, tanlov. Lekin tanlovni osonlashtiradigan narsa bor: "
            "gapdagi baʼzi soʻzlar javobni deyarli har doim aytib turadi."
        ),
        "stories": ["Как я гото́вился к экза́мену"],
        "content": """
<h2>PR-54: Vidni tanlash: takror, jarayon, natija, bir marta, buyruq</h2>

<p>Ikki dars davomida siz vid <b>nima</b> ekanini va u <b>qanday</b>
yasalishini bildingiz. Bugungi savol amaliyroq: <b>qaysi birini
tanlash?</b></p>

<p>Yaxshi xabar: gapda koʻpincha <b>signal soʻzlar</b> boʻladi — ular
javobni deyarli har doim aytib turadi. Ularni bir marta yodlab olsangiz,
tanlovning yarmi oʻz-oʻzidan hal boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>НСВ signal soʻzlarini oʻrganasiz: <b>ка́ждый день, до́лго, ча́сто</b></li>
    <li>СВ signal soʻzlarini oʻrganasiz: <b>наконе́ц, вдруг, уже́</b></li>
    <li>Fon va hodisa qurilishini koʻrasiz</li>
    <li>Buyruqda vid qanday ishlashini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Signal soʻz</span>
  <span class="pe-chip pe-chip--o">ка́ждый день → НСВ</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">наконе́ц → СВ</span>
</div>

<h3>1. Signal soʻzlar</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">НСВ ni chaqiradi</p>
    <p><b>Takror:</b> ча́сто · ре́дко · иногда́ · всегда́ · обы́чно ·
       ка́ждый день · ка́ждый раз</p>
    <p><b>Davomiylik:</b> до́лго · весь день · два часа́ · всё вре́мя</p>
    <p><b>Boshqa:</b> ра́ньше · никогда́</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">СВ ni chaqiradi</p>
    <p><b>Natija:</b> наконе́ц · уже́ · до конца́ · всё</p>
    <p><b>Bir marta:</b> вдруг · сра́зу · одна́жды · оди́н раз</p>
    <p><b>Muddat:</b> за час · за три дня</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Ikkita iborani solishtiring — ular oʻxshaydi, lekin qarama-qarshi
signal beradi:<br>
<b>два часа́</b> (ikki soat davomida) → <b>НСВ</b>:
<em>Я чита́л два часа́.</em><br>
<b>за два часа́</b> (ikki soatda) → <b>СВ</b>:
<em>Я прочита́л кни́гу за два часа́.</em><br><br>
Bitta <em>за</em> predlogi butun maʼnoni oʻzgartiradi: birinchisi qancha
vaqt <b>ketgani</b>, ikkinchisi qancha vaqtda <b>tugagani</b>.</div>

<h3>2. Beshta vaziyat</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Takror → НСВ</p>
    <p><em>Ка́ждый день он <b>звони́л</b> ма́ме.</em><br>
       Har kuni — demak koʻp marta.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Jarayon → НСВ</p>
    <p><em>Он <b>звони́л</b> до́лго.</em><br>
       Uzoq — demak davom etdi.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Natija → СВ</p>
    <p><em>Наконе́ц он <b>позвони́л</b>.</em><br>
       Nihoyat — demak boʻldi.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">4</span>Bir marta → СВ</p>
    <p><em>Вчера́ он <b>позвони́л</b> оди́н раз.</em><br>
       Bir marta, tugagan.</p></div>
</div>

<h3>3. Ketma-ketlik va fon</h3>

<p>Bu ikkita qurilish hikoyada juda koʻp uchraydi va ular vidni oʻzi
tanlaydi:</p>

<div class="pe-ex">
  <p class="pe-ex__ru">Он <span class="pe-hl pe-hl--v">пришёл</span>,
     <span class="pe-hl pe-hl--v">сел</span> и
     <span class="pe-hl pe-hl--v">написа́л</span> письмо́.</p>
  <p class="pe-ex__uz">U keldi, oʻtirdi va xat yozdi.</p>
  <p class="pe-ex__why"><b>Ketma-ketlik</b> — uchta tugagan ish, birin-ketin.
     Hammasi <b>СВ</b>. Agar НСВ boʻlsa, ular bir vaqtda davom etayotgan
     boʻlardi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Я <span class="pe-hl pe-hl--o">чита́л</span>. Вдруг
     он <span class="pe-hl pe-hl--v">пришёл</span>.</p>
  <p class="pe-ex__uz">Oʻqib oʻtirgan edim. Birdan u keldi.</p>
  <p class="pe-ex__why"><b>Fon va hodisa</b>: uzun jarayon (<b>НСВ</b>) va
     uning ichida sodir boʻlgan bir narsa (<b>СВ</b>). Bu naqsh hikoyalarda
     doim uchraydi.</p>
</div>

<h3>4. Buyruqda vid</h3>

<p>Buyruq shakli PR-59 da toʻliq keladi, lekin vid tanlovi bu yerda ham
ishlaydi va uni hozir koʻrib qoʻyish foydali:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shakl</th><th>Vid</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">Чита́й!</td><td class="pr-uz">НСВ</td>
      <td class="pr-end">Umumiy taklif: «oʻqi, oʻqib tur»</td></tr>
  <tr><td class="pr-res">Прочита́й э́то!</td><td class="pr-uz">СВ</td>
      <td class="pr-end">Aniq vazifa: «buni oʻqib chiq»</td></tr>
  <tr><td class="pr-res">Не чита́й!</td><td class="pr-uz">НСВ</td>
      <td class="pr-end">Taqiq: «oʻqima»</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Inkor buyruqda deyarli har doim <b>НСВ</b> ishlatiladi:
<em>не чита́й, не де́лай, не говори́</em>. Bu qoidani hozir eslab
qoling — u PR-59 da qayta uchraydi.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Signal soʻzlar roʻyxatiga qarang — u siz uchun <b>tanish</b> boʻlishi
kerak, chunki oʻzbekchada ham xuddi shu soʻzlar shunday ishlaydi:<br><br>
<em><b>har kuni</b> oʻqirdim</em> — «oʻqib chiqardim» demaysiz.<br>
<em><b>nihoyat</b> oʻqib chiqdim</em> — «nihoyat oʻqirdim» demaysiz.<br>
<em><b>ikki soat</b> oʻqidim</em> · <em><b>ikki soatda</b> oʻqib
chiqdim</em>.<br><br>
Yaʼni tanlov mantigʻi ikkala tilda bir xil. Farq faqat shundaki,
oʻzbekchada bu tanlov <b>ixtiyoriy</b> — <em>oʻqidim</em> deb qoʻyaverish
mumkin. Ruschada esa <b>majburiy</b>. Shuning uchun signal soʻzlarni
yodlash foydali: ular sizga tanlovni tayyor holda beradi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Ка́ждый день он позвони́л ма́ме.</s></p>
  <p class="pe-good">Ка́ждый день он <b>звони́л</b> — takror НСВ talab qiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Наконе́ц он звони́л.</s></p>
  <p class="pe-good">Наконе́ц он <b>позвони́л</b> — «nihoyat» natija bildiradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он прочита́л кни́гу два часа́.</s></p>
  <p class="pe-good">Он <b>чита́л</b> кни́гу два часа́ — davomiylik НСВ</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он чита́л кни́гу за два часа́.</s></p>
  <p class="pe-good">Он <b>прочита́л</b> кни́гу за два часа́ — «за» muddatni bildiradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Не прочита́й э́ту кни́гу!</s></p>
  <p class="pe-good">Не <b>чита́й</b> э́ту кни́гу! — inkor buyruqda НСВ</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu soʻz qaysi vidni chaqiradi? <b>наконе́ц</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>СВ</strong>. «Nihoyat» kutilgan
    natijani bildiradi. Xuddi shunday: <em>вдруг, уже́, сра́зу, за
    час</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu ikki iboraning farqi nima?<br>
     <b>два часа́ · за два часа́</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><em>Два часа́</em> — qancha vaqt
    <b>ketgani</b> (НСВ): <em>чита́л два часа́</em>. <em>За два часа́</em>
    — qancha vaqtda <b>tugagani</b> (СВ): <em>прочита́л за два часа́</em>.
    Bitta predlog butun maʼnoni oʻzgartiradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Он ___, ___ и ___ письмо́.</b>
     (прийти́ / сесть / написа́ть)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>пришёл, сел, написа́л</strong> —
    hammasi СВ. <b>Ketma-ketlik</b> har doim СВ talab qiladi: uchta
    tugagan ish, birin-ketin.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga: <b>Я ___. Вдруг он ___.</b> (чита́ть / прийти́)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>чита́л … пришёл</strong>. Bu
    <b>fon va hodisa</b> qurilishi: uzun jarayon (НСВ) va uning ichida
    sodir boʻlgan bir narsa (СВ).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Inkor buyruqda qaysi vid ishlatiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Deyarli har doim <strong>НСВ</strong>:
    <em>не чита́й, не де́лай, не говори́</em>. Buyruq shakli PR-59 da
    toʻliq koʻriladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ча́сто · ре́дко</b><span>tez-tez · kamdan-kam</span></li>
  <li><b>обы́чно</b><span>odatda</span></li>
  <li><b>всегда́ · никогда́</b><span>doim · hech qachon</span></li>
  <li><b>вдруг</b><span>birdan</span></li>
  <li><b>сра́зу</b><span>darrov</span></li>
  <li><b>одна́жды</b><span>bir kuni</span></li>
  <li><b>за час</b><span>bir soatda</span></li>
  <li><b>ра́ньше</b><span>ilgari</span></li>
  <li><b>хва́тит</b><span>yetadi, boʻldi</span></li>
  <li><b>сдать экза́мен</b><span>imtihon topshirmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>НСВ signallari:</b> ка́ждый день, ча́сто, до́лго, два часа́,
        ра́ньше, никогда́.</li>
    <li><b>СВ signallari:</b> наконе́ц, вдруг, уже́, сра́зу, за час, до
        конца́.</li>
    <li><b>Два часа́</b> (НСВ) ↔ <b>за два часа́</b> (СВ) — bitta predlog
        farqi.</li>
    <li><b>Ketma-ketlik</b> → СВ: <em>пришёл, сел, написа́л</em>.</li>
    <li><b>Fon va hodisa</b> → НСВ + СВ: <em>чита́л … вдруг пришёл</em>.</li>
    <li><b>Inkor buyruq</b> → НСВ: <em>не чита́й</em>.</li>
    <li>Signal soʻzlar oʻzbekchada ham xuddi shunday ishlaydi — tanlov
        mantigʻi bir xil.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-55: Harakat feʼllari 1: идти va ходить — bir yoʻnalish va koʻp yoʻnalish",
        "category": "russian",
        "order": 55,
        "summary": (
            "Rus tilida «bormoq» uchun ikkita feʼl bor. Farqi vid emas — farqi "
            "yoʻnalishda: bir marta bir tomonga yoki muntazam, u yoqqa-bu yoqqa."
        ),
        "stories": ["Доро́га в шко́лу"],
        "content": """
<h2>PR-55: Harakat feʼllari 1: идти va ходить — bir yoʻnalish va koʻp yoʻnalish</h2>

<p>PR-22 da siz <em>идти́</em> ni oʻrgandingiz va PR-21 da <em>ходи́ть</em>
ni koʻrdingiz. Oʻshanda ikkalasi ham «bormoq» deb tarjima qilingan edi —
va bu rost, lekin toʻliq emas. Ular <b>boshqa-boshqa narsani</b>
bildiradi, va farq vid emas: <b>ikkalasi ham НСВ</b>. Farq —
<b>yoʻnalishda</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Идти́</b> va <b>ходи́ть</b> ni ajratasiz</li>
    <li>Oʻtgan zamondagi muhim farqni bilasiz: <b>шёл</b> ↔ <b>ходи́л</b></li>
    <li>Uchinchi maʼnoni oʻrganasiz: qobiliyat</li>
    <li>Oʻzbekcha bilan solishtirasiz — bu yerda u yaxshi yordam beradi</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki yoʻnalish</span>
  <span class="pe-chip pe-chip--v">иду́</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--adv">hozir, bir tomonga</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">хожу́</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--adv">muntazam, u yoqqa-bu yoqqa</span>
</div>

<h3>1. Ikkita feʼl, ikkita yoʻnalish</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">идти́ — bir yoʻnalish</p>
    <p><em>Я <b>иду́</b> в шко́лу.</em><br>Maktabga ketyapman — hozir,
       yoʻldaman.</p>
    <p>Bitta safar, bitta tomon, aniq bir vaqt.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ходи́ть — koʻp yoʻnalish</p>
    <p><em>Я <b>хожу́</b> в шко́лу ка́ждый день.</em><br>Maktabga borib
       turaman.</p>
    <p>Takror, odat — yoki borib-kelish.</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>идти́</th><th>ходи́ть</th></tr>
  <tr><td>я</td><td class="pr-res">иду́</td><td class="pr-end">хожу́</td></tr>
  <tr><td>ты</td><td class="pr-res">идёшь</td><td class="pr-end">хо́дишь</td></tr>
  <tr><td>он / она́</td><td class="pr-res">идёт</td><td class="pr-end">хо́дит</td></tr>
  <tr><td>мы</td><td class="pr-res">идём</td><td class="pr-end">хо́дим</td></tr>
  <tr><td>вы</td><td class="pr-res">идёте</td><td class="pr-end">хо́дите</td></tr>
  <tr><td>они́</td><td class="pr-res">иду́т</td><td class="pr-end">хо́дят</td></tr>
  <tr><td class="pr-uz">oʻtgan zamon</td><td class="pr-res">шёл · шла · шли</td>
      <td class="pr-end">ходи́л · ходи́ла · ходи́ли</td></tr>
</table></div>

<h3>2. Oʻtgan zamondagi farq — bu eng muhimi</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Oʻtgan zamonda farq juda aniq va juda muhim:<br>
<em>Вчера́ я <b>шёл</b> в магази́н</em> — «doʻkonga <b>ketayotgan
edim</b>». Yoʻlda edim; yetib bordimmi — nomaʼlum.<br>
<em>Вчера́ я <b>ходи́л</b> в магази́н</em> — «doʻkonga <b>borib
keldim</b>». Bordim, qaytdim, hozir uydaman.<br><br>
Yaʼni <b>ходи́л</b> — bu <b>borib-kelish</b>, tugagan safar. Shuning
uchun u koʻpincha СВ kabi tuyuladi, lekin u НСВ.</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Где ты был вчера́?<br>
     — Я <span class="pe-hl pe-hl--o">ходи́л</span> к врачу́.</p>
  <p class="pe-ex__uz">— Kecha qayerda eding?<br>— Shifokorga borib
     keldim.</p>
  <p class="pe-ex__why">Savolga javob — butun safar haqida. Agar
     <em>шёл</em> deyilsa, gap yoʻl haqida boʻlardi:
     «ketayotgan edim».</p>
</div>

<h3>3. Uchinchi maʼno: qobiliyat</h3>

<p><em>Ходи́ть</em> ning yana bir ishi bor — u <b>umumiy qobiliyat</b>ni
bildiradi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Gap</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">Ребёнок уже́ хо́дит.</td>
      <td class="pr-end">Bola endi yura oladi.</td></tr>
  <tr><td class="pr-res">Он не хо́дит по́сле опера́ции.</td>
      <td class="pr-end">Operatsiyadan keyin yura olmaydi.</td></tr>
  <tr><td class="pr-res">Ты хо́дишь в теа́тр?</td>
      <td class="pr-end">Teatrga borib turasanmi? (odat)</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu dars odatda qiyin hisoblanadi — lekin oʻzbek oʻquvchi uchun emas,
chunki oʻzbekchada <b>aynan shu uchta shakl bor</b>:<br><br>
<em>bor<b>yapman</b></em> → <b>иду́</b> (hozir, yoʻldaman)<br>
<em>bor<b>ib turaman</b></em> → <b>хожу́</b> (muntazam)<br>
<em>bor<b>ib keldim</b></em> → <b>ходи́л</b> (borib-kelish)<br><br>
Uchta maʼno — uchta shakl. Ikkala tilda ham.<br><br>
Faqat bitta narsani eslab qoling: oʻzbekcha <em>bordim</em> — neytral, u
uchala maʼnoda ham ishlatiladi. Ruschada esa tanlash kerak. Shuning uchun
gapni tuzayotganda oʻzingizdan soʻrang: <b>«yoʻlda edimmi yoki borib
keldimmi?»</b> Javob shaklni oʻzi tanlaydi.</div>

<h3>4. Идти́ ning boshqa ishlari</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Gap</th><th>Maʼnosi</th><th>Izoh</th></tr>
  <tr><td class="pr-res">Идёт дождь.</td><td class="pr-end">Yomgʻir yogʻyapti.</td>
      <td class="pr-uz">ob-havo — PR-23 dan tanish</td></tr>
  <tr><td class="pr-res">Идёт фильм.</td><td class="pr-end">Film ketyapti.</td>
      <td class="pr-uz">tadbir davom etyapti</td></tr>
  <tr><td class="pr-res">Авто́бус идёт в центр.</td><td class="pr-end">Avtobus markazga boradi.</td>
      <td class="pr-uz">transport marshruti</td></tr>
  <tr><td class="pr-res">Вре́мя идёт.</td><td class="pr-end">Vaqt oʻtyapti.</td>
      <td class="pr-uz">koʻchma maʼno</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<em>Идти́</em> va <em>ходи́ть</em> — <b>faqat oyoq bilan</b> yurish
uchun. Transportda ketish uchun boshqa juftlik bor:
<b>е́хать ↔ е́здить</b>. Ular ertaga, PR-56 da keladi.<br>
Yagona istisno — transportning oʻzi: <em>авто́бус <b>идёт</b></em>,
<em>по́езд <b>идёт</b></em>. Bu yerda transport «yuradi» deb
qaraladi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́ в шко́лу ка́ждый день.</s></p>
  <p class="pe-good">Я <b>хожу́</b> в шко́лу ка́ждый день — takror koʻp yoʻnalish</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Вчера́ я шёл к врачу́ и верну́лся.</s></p>
  <p class="pe-good">Вчера́ я <b>ходи́л</b> к врачу́ — borib-kelish</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Сейча́с я хожу́ в магази́н.</s></p>
  <p class="pe-good">Сейча́с я <b>иду́</b> в магази́н — hozir, yoʻldaman</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ребёнок уже́ идёт.</s> <em>(«yura oladi» maʼnosida)</em></p>
  <p class="pe-good">Ребёнок уже́ <b>хо́дит</b> — qobiliyat koʻp yoʻnalish bilan</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>иду́</b> yoki <b>хожу́</b>? &nbsp; <b>Я ___ в шко́лу ка́ждый
     день.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>хожу́</strong>. «Ка́ждый день» —
    takror, demak koʻp yoʻnalish. Oʻzbekcha tekshiruv: «borib turaman» —
    demak <em>ходи́ть</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>шёл</b> yoki <b>ходи́л</b>? &nbsp; <b>Вчера́ я ___ в магази́н и
     купи́л хлеб.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ходи́л</strong>. Bordim va
    qaytdim — borib-kelish. Oʻzbekcha: «borib keldim».
    <em>Шёл</em> boʻlsa, gap yoʻl haqida boʻlardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapning farqi nima?<br>
     <b>Я шёл в магази́н. · Я ходи́л в магази́н.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — «doʻkonga <b>ketayotgan
    edim</b>» (yoʻlda edim). Ikkinchisi — «doʻkonga <b>borib keldim</b>»
    (bordim va qaytdim). Oʻzbekchada ham ikkita boshqa
    ibora.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga: <b>Ребёнок уже́ ___.</b> («yura oladi» maʼnosida)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>хо́дит</strong>. Umumiy qobiliyat
    — bu <em>ходи́ть</em> ning uchinchi ishi. <em>Идёт</em> «hozir
    ketyapti» degan boʻlardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Сейча́с я иду́ домо́й. &nbsp; б) Я хожу́ в теа́тр ре́дко.<br>
     в) Я иду́ в шко́лу ка́ждый день. &nbsp; г) Идёт дождь.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Я хожу́ в шко́лу ка́ждый день</b>. «Ка́ждый день» takrorni
    bildiradi, demak koʻp yoʻnalish kerak.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>идти́ → иду́, шёл</b><span>ketmoq (hozir, bir tomonga)</span></li>
  <li><b>ходи́ть → хожу́, ходи́л</b><span>borib turmoq; borib kelmoq</span></li>
  <li><b>пешко́м</b><span>piyoda</span></li>
  <li><b>доро́га</b><span>yoʻl</span></li>
  <li><b>киломе́тр</b><span>kilometr</span></li>
  <li><b>ре́дко · ча́сто</b><span>kamdan-kam · tez-tez</span></li>
  <li><b>верну́ться</b><span>qaytmoq</span></li>
  <li><b>жа́ловаться</b><span>shikoyat qilmoq</span></li>
  <li><b>идёт дождь</b><span>yomgʻir yogʻyapti</span></li>
  <li><b>вре́мя идёт</b><span>vaqt oʻtyapti</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Ikkalasi ham <b>НСВ</b> — farq vid emas, <b>yoʻnalish</b>.</li>
    <li><b>Идти́</b> — hozir, bir tomonga. <b>Ходи́ть</b> — muntazam yoki
        borib-kelish.</li>
    <li>Oʻtgan zamonda: <b>шёл</b> = yoʻlda edim · <b>ходи́л</b> = borib
        keldim.</li>
    <li><b>Ходи́ть</b> qobiliyatni ham bildiradi: <em>ребёнок уже́
        хо́дит</em>.</li>
    <li><b>Идти́</b> ob-havo, tadbir, transport va vaqt uchun ham:
        <em>идёт дождь, идёт фильм, вре́мя идёт</em>.</li>
    <li>Oʻzbekchada uchta shakl bor: <em>boryapman · borib turaman · borib
        keldim</em>. Ular toʻgʻridan-toʻgʻri mos keladi.</li>
    <li>Transport uchun boshqa juftlik: <b>е́хать ↔ е́здить</b> (PR-56).</li>
  </ul>
</div>
""",
    },
]
