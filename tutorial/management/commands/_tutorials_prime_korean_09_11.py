# -*- coding: utf-8 -*-
"""Prime Korean — Block B, darslar 9–11 (birinchi gaplar).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Har bir dars uchta boʻlakdan biri: dars + mashq + oʻqish matni.
Oʻqish matnlari: corner/management/commands/_stories_prime_korean_09_11.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_09_11.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Korean",
    "category": "korean",
    "description": (
        "Koreys tili noldan TOPIK II gacha — 100 ta dars. Hangul, grammatika qoliplari, "
        "oʻzbekcha tushuntirish va oʻzingiz tekshiradigan mashqlar."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-9: Salomlashish, xayrlashish va oʻzini tanishtirish",
        "category": "korean",
        "order": 9,
        "summary": (
            "Birinchi haqiqiy koreyscha jumlalaringiz: salomlashish, minnatdorchilik, "
            "kechirim va koreyschadagi eng chalkash juftlik — 계세요 va 가세요."
        ),
        "stories": ["안녕하세요"],
        "content": """
<h2>PK-9: Salomlashish, xayrlashish va oʻzini tanishtirish</h2>

<p>Sakkiz dars davomida harflarni oʻrgandingiz. Bugundan boshlab <b>gapirasiz</b>.
Yaxshi xabar shuki, koreyscha salomlashish oʻzbekchadan ham oson: bitta soʻz —
<b>안녕하세요</b> — ertalab ham, kechqurun ham, birinchi marta koʻrganda ham,
har kuni koʻradiganingizda ham ishlaydi. Yomon xabar esa bitta: xayrlashishda
<em>ikkita</em> shakl bor va deyarli har bir yangi oʻquvchi ularni adashtiradi.
Bugun ikkalasini ham hal qilamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>안녕하세요 bilan har qanday vaziyatda salomlashasiz</li>
    <li>안녕히 계세요 va 안녕히 가세요 ni bir umrga ajratasiz</li>
    <li>Rahmat, kechirasiz, ha va yoʻq deyishni oʻrganasiz</li>
    <li>Oʻzingizni tanishtirasiz va tanishuvni yakunlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Birinchi uchrashuv</span>
  <span class="pe-chip pe-chip--v">안녕하세요</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">저는 … 입니다</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">만나서 반갑습니다</span>
</div>

<h3>1. 안녕하세요 — hamma narsaga yetadigan salom</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">안녕하세요?</p>
  <p class="pe-ex__rom">[안녕하세요]</p>
  <p class="pe-ex__uz">Assalomu alaykum. / Salom.</p>
  <p class="pe-ex__why">Soʻzma-soʻz: "Tinchlikdamisiz?" — shuning uchun oxirida savol
     belgisi turadi, garchi ohang savol ohangi boʻlmasa ham.</p>
</div>

<p>Bu bitta ibora oʻzbekchadagi <em>assalomu alaykum</em>, <em>xayrli tong</em>,
<em>xayrli kech</em> — hammasining oʻrnini bosadi. Koreys tilida vaqtga qarab
oʻzgaradigan alohida salom <b>yoʻq</b>.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Diqqat qiling: <b>안녕</b> — "tinchlik" degani, xuddi <em>salom</em> soʻzining maʼnosi
kabi. Ikkala tilda ham salomlashish "tinchlikmisiz?" degan savoldan kelib chiqqan.
Shuning uchun bu iborani yodlash sizga oson tushadi.</div>

<p>Yaqin doʻstingizga esa qisqasi aytiladi — faqat <b>안녕</b>. Buni kim bilan
ishlatish mumkinligini PK-11 darsida batafsil koʻramiz.</p>

<h3>2. Xayrlashish — darsning eng muhim qismi</h3>

<p>Koreyschada xayrlashish <b>kim ketayotganiga</b> bogʻliq. Ikkita shakl bor va ular
almashtirilmaydi:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">안녕히 계세요</p>
    <p style="font-size:1.2rem">"Tinchlikda <b>qoling</b>"</p>
    <p><b>Siz ketyapsiz</b>, u yerda qoladiganga aytasiz.</p>
    <p>Doʻkondan chiqayotganda sotuvchiga.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">안녕히 가세요</p>
    <p style="font-size:1.2rem">"Tinchlikda <b>boring</b>"</p>
    <p><b>U ketyapti</b>, siz qolasiz.</p>
    <p>Mehmoningizni kuzatayotganda.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Buni yodlashning eng oson yoʻli — <b>oyoqqa qarang</b>. Kimning oyogʻi harakatlanayapti?
Agar sizniki — siz <b>가</b>-yapsiz, demak siz qolganga <b>계세요</b> deysiz. Ikkalangiz
ham ketayotgan boʻlsangiz, ikkalangiz ham <b>안녕히 가세요</b> deysiz.</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 안녕히 계세요.<br>나: 네, 안녕히 가세요.</p>
  <p class="pe-ex__uz">A: Xayr (men ketyapman).<br>B: Ha, xayr (siz boring).</p>
  <p class="pe-ex__why">Eng koʻp uchraydigan juftlik: biri ketadi, biri qoladi.</p>
</div>

<h3>3. Rahmat va kechirim</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Ibora</th><th>Oʻqilishi</th><th>Maʼnosi</th><th>Qachon</th></tr>
  <tr><td class="pk-res">감사합니다</td><td class="pk-end">[감사함니다]</td>
      <td class="pk-uz">Rahmat</td><td class="pk-uz">rasmiy, eng keng tarqalgan</td></tr>
  <tr><td class="pk-res">고맙습니다</td><td class="pk-end">[고맙씀니다]</td>
      <td class="pk-uz">Rahmat</td><td class="pk-uz">biroz iliqroq, koreyscha ildizli</td></tr>
  <tr><td class="pk-res">죄송합니다</td><td class="pk-end">[죄송함니다]</td>
      <td class="pk-uz">Kechirasiz</td><td class="pk-uz">jiddiy uzr</td></tr>
  <tr><td class="pk-res">미안합니다</td><td class="pk-end">[미안함니다]</td>
      <td class="pk-uz">Kechirasiz</td><td class="pk-uz">yengilroq uzr</td></tr>
  <tr><td class="pk-res">실례합니다</td><td class="pk-end">[실례함니다]</td>
      <td class="pk-uz">Uzr, ijozat</td><td class="pk-uz">gap boshlashdan oldin</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Diqqat qildingizmi — <b>hammasi [함니다] bilan tugaydi</b>, "합니다" deb yozilsa ham.
Bu PK-8 dagi <b>비음화</b>: ㅂ dan keyin ㄴ kelgani uchun ㅂ burun tovushi ㅁ ga aylanadi.
Bir marta tushunsangiz, yuzlab soʻzga bir vaqtda tegishli boʻladi.</div>

<h3>4. 네 va 아니요</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">네. / 아니요.</p>
  <p class="pe-ex__uz">Ha. / Yoʻq.</p>
  <p class="pe-ex__why">네 kundalik nutqda <b>예</b> shaklida ham aytiladi — ikkalasi
     ham toʻgʻri.</p>
</div>

<p>Koreyslar <b>네</b> ni juda koʻp ishlatadi — koʻpincha u "ha" emas, "eshityapman,
davom eting" degani. Telefon suhbatini eshitsangiz, har ikki jumladan keyin
<em>네… 네…</em> deyilganini payqaysiz.</p>

<h3>5. Oʻzini tanishtirish</h3>

<p>Endi butun bir tanishuvni yigʻamiz. Quyidagi qolipni hozircha <b>butunligicha</b>
yodlang — ichidagi 입니다 grammatikasini keyingi dars, PK-10, toʻliq ochib beradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">안녕하세요? 저는 <span class="pe-hl pe-hl--s">아프소나</span>입니다.</p>
  <p class="pe-ex__rom">[안녕하세요 저는 아프소나임니다]</p>
  <p class="pe-ex__uz">Salom. Men Afsonaman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">만나서 반갑습니다.</p>
  <p class="pe-ex__rom">[만나서 반갑씀니다]</p>
  <p class="pe-ex__uz">Tanishganimdan xursandman.</p>
  <p class="pe-ex__why">Soʻzma-soʻz: "uchrashib, xursandman".</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">잘 부탁합니다.</p>
  <p class="pe-ex__uz">Iltimosim sizga. / Yaxshi munosabatda boʻling.</p>
  <p class="pe-ex__why">Oʻzbekchaga toʻgʻridan-toʻgʻri tarjima qilinmaydi. Tanishuvni
     yakunlaydigan odob iborasi — yangi sinfda, yangi ishda albatta aytiladi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
<b>잘 부탁합니다</b> — oʻzbekchada ekvivalenti yoʻq iboralardan. Uni "sizga
ishonaman, menga yaxshi qarang" degan iltifot deb tushuning. Koreyada tanishuv shu
ibora bilan tugamasa, suhbat chala qolgandek tuyuladi.</div>

<h3>6. Yana bir necha kundalik ibora</h3>

<ul class="pe-steps">
  <li><b>어서 오세요</b> — "Xush kelibsiz" (doʻkonda sizga aytiladi)</li>
  <li><b>잘 먹겠습니다</b> — ovqatdan <em>oldin</em>: "yaxshi yeyman"</li>
  <li><b>잘 먹었습니다</b> — ovqatdan <em>keyin</em>: "yaxshi yedim, rahmat"</li>
  <li><b>안녕히 주무세요</b> — "Xayrli tun" (yotishdan oldin)</li>
  <li><b>수고하셨습니다</b> — "Charchamang, mehnatingiz uchun rahmat"</li>
</ul>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Salomlashganda <b>bosh egiladi</b>. Kattaroq yoshdagi odamga chuqurroq, tengdoshga
yengil. Qoʻl berib koʻrishish ham bor, lekin bosh egish har doim ishlaydi va hech
qachon xato boʻlmaydi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">Doʻkondan chiqayotib sotuvchiga <s>안녕히 가세요</s> deyish.</p>
  <p class="pe-good">Sotuvchi qoladi, siz ketasiz → <b>안녕히 계세요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">감사합니다 ni "kam-sa-hap-ni-da" deb oʻqish.</p>
  <p class="pe-good">비음화: <b>[감사함니다]</b>. ㅂ + ㄴ → ㅁ.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Ertalab alohida, kechqurun alohida salom qidirish.</p>
  <p class="pe-good"><b>안녕하세요</b> hamma vaqt uchun yetarli.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Notanish kattaroq odamga <s>안녕</s> deyish.</p>
  <p class="pe-good">안녕 — faqat yaqin doʻst va oʻzingizdan kichiklarga.
     Qolganlarga <b>안녕하세요</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Kafedan chiqib ketyapsiz. Ofitsiantga nima deysiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>안녕히 계세요</strong> — "tinchlikda qoling".
    Ofitsiant kafeda <em>qoladi</em>, ketayotgan siz. Oyoqqa qarang: kimning oyogʻi
    harakatlanmoqda?</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>감사합니다</b> qanday oʻqiladi va nega?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[감사함니다]</strong>. Bu PK-8 dagi
    <em>비음화</em>: 받침 ㅂ dan keyin ㄴ kelgani uchun ㅂ burun tovushi ㅁ ga aylanadi.
    Shu qoida 합니다 bilan tugaydigan <b>barcha</b> shakllarga tegishli.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga nima tushadi?<br>
     가: 안녕히 가세요.<br>나: 네, <span class="pe-blank">?</span></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>안녕히 계세요</strong>. Birinchi kishi "boring"
    dedi — demak <em>u</em> qolyapti va <em>siz</em> ketyapsiz. Shuning uchun siz unga
    "qoling" deysiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Ovqatdan oldin va keyin nima deyiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Oldin — <strong>잘 먹겠습니다</strong> ("yaxshi
    yeyman"), keyin — <strong>잘 먹었습니다</strong> ("yaxshi yedim"). Farqi bitta
    boʻgʻinda: 겠 (kelasi) va 었 (oʻtgan).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Jasur yangi sinfga kirdi va "안녕하세요? 저는 자수르입니다." dedi. Tanishuvni
     tugatish uchun yana nima deyishi kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>만나서 반갑습니다</strong> ("tanishganimdan
    xursandman") va <strong>잘 부탁합니다</strong>. Koreyada tanishuv shu ikkinchi ibora
    bilan yakunlanadi — usiz suhbat chala qolgandek tuyuladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>안녕하세요</b><span>salom, assalomu alaykum</span></li>
  <li><b>안녕히 계세요</b><span>xayr (qoluvchiga)</span></li>
  <li><b>안녕히 가세요</b><span>xayr (ketuvchiga)</span></li>
  <li><b>감사합니다</b><span>rahmat</span></li>
  <li><b>죄송합니다</b><span>kechirasiz</span></li>
  <li><b>네 / 아니요</b><span>ha / yoʻq</span></li>
  <li><b>만나서 반갑습니다</b><span>tanishganimdan xursandman</span></li>
  <li><b>잘 부탁합니다</b><span>iltimosim sizga (tanishuv yakuni)</span></li>
  <li><b>어서 오세요</b><span>xush kelibsiz</span></li>
  <li><b>실례합니다</b><span>uzr, ijozat</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>안녕하세요</b> — ertalab ham, kechqurun ham, har doim.</li>
    <li><b>계세요 = qoling · 가세요 = boring.</b> Kimning oyogʻi harakatlanyapti?</li>
    <li>합니다 bilan tugaydigan hamma narsa <b>[함니다]</b> deb oʻqiladi (비음화).</li>
    <li>네 koʻpincha "ha" emas, "eshityapman" degani.</li>
    <li>Tanishuv <b>잘 부탁합니다</b> bilan yakunlanadi.</li>
    <li>Salomlashganda <b>bosh egiladi</b> — bu hech qachon xato boʻlmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-10: 명사 + 입니다 / 입니까? — rasmiy \"…dir\" va savol",
        "category": "korean",
        "order": 10,
        "summary": (
            "Koreys tilidagi eng sodda gap: ot + 입니다. Kesim gap oxiriga tushadi — "
            "xuddi oʻzbekchadagidek, shuning uchun bu qolip sizga tanish tuyuladi."
        ),
        "stories": ["저는 학생입니다"],
        "content": """
<h2>PK-10: 명사 + 입니다 / 입니까? — rasmiy "…dir" va savol</h2>

<p>Koreys tilidagi eng birinchi va eng sodda gap qolipi shu. U bilan siz oʻzingizni
tanishtirasiz, narsalarni nomlaysiz, savol berasiz. Va eng yaxshi tomoni — bu qolip
oʻzbek oʻquvchisi uchun <b>tabiiy</b> tuyuladi, chunki ikkala tilda ham kesim
gapning <em>oxirida</em> turadi. Ingliz tilini oʻrganayotgan bola bu yerda qiynaladi;
siz qiynalmaysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>명사 + 입니다 qolipi bilan gap tuzasiz</li>
    <li>입니까? bilan savol berasiz</li>
    <li>이/가 아닙니다 bilan inkor qilasiz</li>
    <li>씨 va 저 soʻzlarini toʻgʻri ishlatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Eng sodda koreys gapi</span>
  <span class="pe-chip pe-chip--s">저는</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">입니다</span>
</div>

<div class="pe-legend">
  <span><i style="background:#2563eb"></i>ega — 주어</span>
  <span><i style="background:#d97706"></i>ot — 명사</span>
  <span><i style="background:#16a34a"></i>kesim — 서술어</span>
</div>

<h3>1. 입니다 — "…dir"</h3>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">저는</span>
     <span class="pe-hl pe-hl--o">학생</span><span class="pe-hl pe-hl--v">입니다</span>.</p>
  <p class="pe-ex__rom">[저는 학쌩임니다]</p>
  <p class="pe-ex__uz">Men talabaman.</p>
</div>

<p>입니다 otga <b>toʻgʻridan-toʻgʻri, boʻshliqsiz</b> yopishadi. Va u har qanday otga
bir xil qoʻshiladi — <b>받침 bor-yoʻqligi ahamiyatsiz</b>:</p>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">학생 + <span class="pk-end">입니다</span></p>
    <p>학생<b>입니다</b> · 선생님<b>입니다</b></p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">의사 + <span class="pk-end">입니다</span></p>
    <p>의사<b>입니다</b> · 친구<b>입니다</b></p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bu qolipdan zavq oling — koreys tilida <b>받침ga qarab shakl tanlamaydigan</b>
grammatika kam. Keyinroq oʻrganadigan 이에요/예요 shakli aynan shu yerda ikkiga
boʻlinadi. 입니다 esa hech qachon boʻlinmaydi.</div>

<h3>2. Talaffuz: 입니다 → [임니다]</h3>

<div class="pk-say">
  <span class="pk-say__from">입니다</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[임니다]</span>
  <span class="pk-say__why">비음화 — ㅂ dan keyin ㄴ kelsa, ㅂ → ㅁ</span>
</div>

<p>Buni PK-8 da koʻrgan edingiz. Endi u har bir gapingizda qatnashadi, shuning uchun
hozirdan toʻgʻri odatlaning: <b>"im-ni-da"</b>, hech qachon "ip-ni-da" emas.</p>

<h3>3. 입니까? — savol</h3>

<p>Savol yasash uchun 다 ni <b>까</b> ga almashtirasiz. Boshqa hech narsa oʻzgarmaydi —
soʻz tartibi ham, ohang ham.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">학생<span class="pe-hl pe-hl--v">입니까</span>?</p>
  <p class="pe-ex__rom">[학쌩임니까]</p>
  <p class="pe-ex__uz">Talabamisiz?</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 자수르 씨는 의사입니까?<br>나: 네, 의사입니다.</p>
  <p class="pe-ex__uz">A: Jasur janob shifokormi?<br>B: Ha, shifokor.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada ham savol qoʻshimcha bilan yasaladi: <em>talaba</em> → <em>talaba<b>mi</b></em>.
Koreyschada ham xuddi shunday — <em>입니다</em> → <em>입니<b>까</b></em>. Ingliz tilidagidek
soʻzlarni oʻrin almashtirish (<em>Are you…?</em>) <b>kerak emas</b>. Bu ikki tilning
juda oʻxshash joyi.</div>

<h3>4. 아닙니다 — inkor</h3>

<p>"…emas" deyish uchun 입니다 emas, boshqa soʻz ishlatiladi: <b>아닙니다</b>. Va uning
oldidagi ot <b>이</b> yoki <b>가</b> qoʻshimchasini oladi — mana bu yerda 받침 qoidasi
birinchi marta ishga tushadi:</p>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">ot + <span class="pk-par">이</span> 아닙니다</p>
    <p>학생<b>이</b> 아닙니다</p>
    <p>선생님<b>이</b> 아닙니다</p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">ot + <span class="pk-par">가</span> 아닙니다</p>
    <p>의사<b>가</b> 아닙니다</p>
    <p>친구<b>가</b> 아닙니다</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 의사가 아닙니다. 학생입니다.</p>
  <p class="pe-ex__uz">Men shifokor emasman. Talabaman.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Bu <b>받침 ayrisi</b> — koreys grammatikasining eng koʻp takrorlanadigan qoidasi.
Soʻz undosh bilan tugasa bir shakl, unli bilan tugasa boshqasi. Buni bir marta
oʻzlashtirsangiz, keyingi oʻnlab darsda ishingiz oson boʻladi.</div>

<h3>5. 씨 — ismga qoʻshiladigan hurmat</h3>

<p>Koreysda odamning ismini yolgʻiz aytish qoʻpol tuyuladi. Ismdan keyin <b>씨</b>
qoʻshiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">아프소나 씨는 학생입니다.</p>
  <p class="pe-ex__uz">Afsona xonim talaba.</p>
  <p class="pe-ex__why">씨 alohida yoziladi — ismdan keyin boʻshliq qoʻyiladi.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>씨 ni oʻzingizga qoʻllamang.</b> "저는 아프소나 씨입니다" — notoʻgʻri, chunki
oʻzingizni hurmatlab boʻlmaydi. Toʻgʻrisi: <b>저는 아프소나입니다</b>.</div>

<h3>6. 저 va 나</h3>

<p>"Men" degan soʻz koreyschada ikkita:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">저 — kamtar "men"</p>
    <p>Kattaroq odamga, notanishga, rasmiy vaziyatda.</p>
    <p><b>저는 학생입니다.</b></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">나 — oddiy "men"</p>
    <p>Yaqin doʻstga, oʻzidan kichikka.</p>
    <p><b>나는 학생이야.</b></p>
  </div>
</div>

<p>입니다 rasmiy shakl boʻlgani uchun u deyarli har doim <b>저</b> bilan keladi. Bu
tanlovni PK-11 darsi toʻliq ochib beradi.</p>

<h3>7. Yigʻamiz</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">안녕하세요? 저는 셰르벡입니다.<br>
     한국 사람이 아닙니다. 우즈베키스탄 사람입니다.<br>
     만나서 반갑습니다.</p>
  <p class="pe-ex__uz">Salom. Men Sherbekman.<br>
     Koreys emasman. Oʻzbekistonlikman.<br>
     Tanishganimdan xursandman.</p>
  <p class="pe-ex__why">Uchta gap, uchtasi ham bugungi qolipda. Siz allaqachon
     oʻzingizni tanishtira olasiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>입니다 학생</s>.</p>
  <p class="pe-good">저는 <b>학생입니다</b>. Kesim har doim gap <b>oxirida</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>의사이 아닙니다</s>.</p>
  <p class="pe-good">의사 unli bilan tugaydi → <b>의사가 아닙니다</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저는 아프소나 <s>씨</s>입니다.</p>
  <p class="pe-good">저는 <b>아프소나입니다</b>. 씨 faqat boshqalarga.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">입니다 ni "ip-ni-da" deb oʻqish.</p>
  <p class="pe-good"><b>[임니다]</b> — 비음화.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga nima tushadi?<br>저는 <span class="pe-blank">?</span> (선생님)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>선생님입니다</strong> — "Men oʻqituvchiman".
    입니다 otga boʻshliqsiz yopishadi va 받침 bor-yoʻqligiga qaramaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     "학생입니다" ni savolga aylantiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>학생입니까?</strong> — faqat <b>다</b> ni
    <b>까</b> ga almashtirdik. Soʻz tartibi oʻzgarmaydi, xuddi oʻzbekchadagi
    <em>-mi</em> qoʻshimchasi kabi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Toʻgʻri shaklni tanlang: 친구<span class="pe-blank">?</span> 아닙니다.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>가</strong> — 친구<b>가</b> 아닙니다. 친구 unli
    (ㅜ) bilan tugaydi, shuning uchun 받침 yoʻq tomon: <b>가</b>. Agar 학생 boʻlganida
    <b>이</b> boʻlardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nega "저는 자수르 씨입니다" notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>씨 — hurmat qoʻshimchasi</strong> va uni
    oʻzingizga qoʻllab boʻlmaydi. Toʻgʻrisi: <b>저는 자수르입니다</b>. 씨 faqat boshqa
    odamning ismiga qoʻshiladi: 자수르 씨는 학생입니다.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni koreyschaga oʻgiring: "Men shifokor emasman."</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>저는 의사가 아닙니다.</strong> Uchta narsaga
    diqqat: <b>저는</b> (rasmiy "men"), <b>의사가</b> (unli bilan tugagani uchun 가), va
    kesim gap <b>oxirida</b>. Oʻzbekchadagi soʻz tartibi bilan bir xil.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>입니다</b><span>…dir (rasmiy)</span></li>
  <li><b>입니까?</b><span>…mi? (rasmiy savol)</span></li>
  <li><b>아닙니다</b><span>…emas</span></li>
  <li><b>저</b><span>men (kamtar)</span></li>
  <li><b>씨</b><span>janob/xonim (ismdan keyin)</span></li>
  <li><b>학생</b><span>oʻquvchi, talaba</span></li>
  <li><b>선생님</b><span>oʻqituvchi</span></li>
  <li><b>의사</b><span>shifokor</span></li>
  <li><b>친구</b><span>doʻst</span></li>
  <li><b>사람</b><span>odam, kishi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>ot + 입니다</b> = "…dir". Boʻshliqsiz yopishadi, 받침ga qaramaydi.</li>
    <li>Savol: <b>다 → 까</b>. Soʻz tartibi oʻzgarmaydi.</li>
    <li>Inkor: <b>이/가 아닙니다</b> — bu yerda 받침 ayrisi ishlaydi.</li>
    <li><b>Kesim har doim gap oxirida</b> — xuddi oʻzbekchadagidek.</li>
    <li><b>씨</b> faqat boshqalarga, hech qachon oʻzingizga.</li>
    <li>입니다 = <b>[임니다]</b>. Har gapda takrorlanadi, hozirdan toʻgʻri odatlaning.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-11: Nutq darajalari: 존댓말 va 반말 — kimga qanday gapirasiz",
        "category": "korean",
        "order": 11,
        "summary": (
            "Koreys tilida munosabat feʼlning oxiriga yoziladi. Uch daraja, ularni "
            "kim bilan ishlatish va oʻzbekcha siz/sen bilan taqqoslash."
        ),
        "stories": ["누구한테 어떻게 말해요?"],
        "content": """
<h2>PK-11: Nutq darajalari: 존댓말 va 반말 — kimga qanday gapirasiz</h2>

<p>Koreyada ikki kishi tanishganda deyarli har doim beriladigan savol bor:
<b>몇 살이에요?</b> — "Necha yoshdasiz?". Oʻzbekistonda bu biroz gʻalati tuyulishi
mumkin, Koreyada esa mutlaqo tabiiy. Sababi oddiy: <b>javobni bilmasdan turib, ular
gapira olmaydi</b>. Chunki koreys tilida har bir gapning oxiri suhbatdoshingiz bilan
munosabatingizni oshkor qiladi. Bugun shu tizimni tushunamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>존댓말 va 반말 nima ekanini bilib olasiz</li>
    <li>Uchta amaliy darajani ajratasiz: 합니다체, 해요체, 반말</li>
    <li>Kimga qaysi darajada gapirishni aniqlaysiz</li>
    <li>저/나 va 제/내 juftliklarini toʻgʻri tanlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bir xil maʼno, uch xil munosabat</span>
  <span class="pe-chip pe-chip--neg">먹습니다</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">먹어요</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--opt">먹어</span>
</div>

<h3>1. Munosabat feʼlning oxirida yashaydi</h3>

<p>Oʻzbekchada "kelmoq" feʼlini kimga aytayotganingizga qarab oʻzgartirasiz:
<em>keldingiz</em> yoki <em>kelding</em>. Koreyschada ham xuddi shunday, faqat
<b>darajalar koʻproq</b> va ular <b>har bir gapda</b> majburiy.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Sizda bu tushuncha <b>allaqachon bor</b> — bu koreys tilini oʻrganishdagi katta
afzalligingiz. Ingliz tilida "you" bitta va oʻquvchi bu tizimni noldan tushunishi
kerak. Siz esa <em>siz/sen</em> farqini tugʻilganingizdan beri bilasiz. Koreyschada
faqat shuni bilib olish kerak: bu farq <b>olmoshda emas, feʼl oxirida</b>
koʻrsatiladi.</div>

<h3>2. Uchta amaliy daraja</h3>

<div class="pk-level">
  <div class="pk-level__row pk-level__row--4">
    <span class="pk-level__name">합니다체</span>
    <span class="pk-level__ko">먹습니다</span>
    <span class="pk-level__who">rasmiy: yigʻilish, xabarlar, harbiy, mijoz</span>
  </div>
  <div class="pk-level__row pk-level__row--3">
    <span class="pk-level__name">해요체</span>
    <span class="pk-level__ko">먹어요</span>
    <span class="pk-level__who">kundalik hurmat — eng koʻp ishlatiladi</span>
  </div>
  <div class="pk-level__row pk-level__row--1">
    <span class="pk-level__name">반말</span>
    <span class="pk-level__ko">먹어</span>
    <span class="pk-level__who">yaqin doʻst, tengdosh, oʻzidan kichik</span>
  </div>
</div>

<p>Yuqoridagi ikkitasi — 합니다체 va 해요체 — birgalikda <b>존댓말</b> (hurmat nutqi)
deb ataladi. Uchinchisi <b>반말</b> ("yarim nutq") deyiladi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">합니다체 — qat'iy rasmiy</p>
    <p>Sovuqroq, masofali, professional.</p>
    <p>Yangiliklar diktori, xizmatchi, taqdimot.</p>
    <p><b>저는 학생입니다.</b></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">해요체 — iliq hurmat</p>
    <p>Muloyim, lekin yaqin. <b>Eng xavfsiz tanlov.</b></p>
    <p>Doʻkonda, sinfda, katta yoshdagi qoʻshni bilan.</p>
    <p><b>저는 학생이에요.</b></p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Qaysi birini tanlashni bilmasangiz — <b>해요체</b> ni ishlating. U deyarli hech qachon
xato boʻlmaydi: rasmiy vaziyatda biroz iliq tuyuladi, xolos. 반말ni notoʻgʻri
ishlatish esa qoʻpollik hisoblanadi. Shuning uchun bu kursning koʻp darslari
해요체 ustiga quriladi (PK-18 darsidan boshlab).</div>

<h3>3. Kimga qaysi daraja</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Suhbatdosh</th><th>Daraja</th><th>Nega</th></tr>
  <tr><td class="pk-res">Oʻqituvchi, boshliq</td><td class="pk-end">존댓말</td>
      <td class="pk-uz">maqom yuqori — yoshdan qatʼi nazar</td></tr>
  <tr><td class="pk-res">Notanish odam</td><td class="pk-end">존댓말</td>
      <td class="pk-uz">munosabat hali aniqlanmagan</td></tr>
  <tr><td class="pk-res">Kattaroq yoshdagi</td><td class="pk-end">존댓말</td>
      <td class="pk-uz">bir yosh katta boʻlsa ham</td></tr>
  <tr><td class="pk-res">Yaqin tengdosh doʻst</td><td class="pk-end">반말</td>
      <td class="pk-uz">kelishilgandan keyin</td></tr>
  <tr><td class="pk-res">Kichik yoshdagi bola</td><td class="pk-end">반말</td>
      <td class="pk-uz">tabiiy</td></tr>
  <tr><td class="pk-res">Mijoz (siz xizmatchi boʻlsangiz)</td><td class="pk-end">합니다체</td>
      <td class="pk-uz">professional masofa</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Yosh farqi bir yil boʻlsa ham ahamiyatli.</b> Koreyada bir yosh katta odam
<em>tengdosh emas</em>. Shuning uchun 몇 살이에요? savoli qoʻpollik emas — u suhbatni
qanday davom ettirishni aniqlash uchun kerak.</div>

<h3>4. 반말ga oʻtish — bu kelishuv</h3>

<p>반말ga oʻz-oʻzidan oʻtilmaydi. Odatda kattaroq yoki maqomi yuqoriroq odam taklif
qiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">말 놓으세요.</p>
  <p class="pe-ex__uz">Erkin gapiravering. (soʻzma-soʻz: "nutqni qoʻyib yuboring")</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">우리 말 놓을까요?</p>
  <p class="pe-ex__uz">반말ga oʻtsakmikan?</p>
</div>

<p>Bu taklif kelmagunicha <b>존댓말da qoling</b>. Chet ellik uchun bu xato hech qachon
kechirilmaydigan narsa emas, lekin toʻgʻri qilsangiz — darhol seziladi va hurmat
qozonasiz.</p>

<h3>5. Olmoshlar ham oʻzgaradi</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Maʼnosi</th><th>존댓말</th><th>반말</th></tr>
  <tr><td class="pk-res">men</td><td class="pk-end">저</td><td class="pk-stem">나</td></tr>
  <tr><td class="pk-res">mening</td><td class="pk-end">제</td><td class="pk-stem">내</td></tr>
  <tr><td class="pk-res">biz</td><td class="pk-end">저희</td><td class="pk-stem">우리</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">제 이름은 지영입니다.</p>
  <p class="pe-ex__uz">Mening ismim Jiyoung.</p>
  <p class="pe-ex__why">존댓말 — shuning uchun 내 emas, <b>제</b>.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Gap oxiri hurmatli, lekin olmosh oddiy boʻlsa — gap <b>gʻalati</b> chiqadi:
<s>나는 학생입니다</s>. Ikkalasi mos kelishi kerak: <b>저는 학생입니다</b> yoki
<b>나는 학생이야</b>.</div>

<h3>6. Odamni qanday chaqirasiz</h3>

<p>Koreyada suhbatdoshga "siz" deb murojaat qilish odatiy emas — <b>당신</b> soʻzi bor,
lekin u deyarli ishlatilmaydi va koʻpincha qoʻpol tuyuladi. Uning oʻrniga
<b>ism yoki lavozim</b> ishlatiladi:</p>

<ul class="pe-steps">
  <li><b>지영 씨</b> — ism + 씨 (tengdosh yoki biroz rasmiy)</li>
  <li><b>선생님</b> — "oʻqituvchi" (lekin har qanday hurmatli kishiga ham)</li>
  <li><b>사장님</b> — "direktor"</li>
  <li><b>언니 / 누나 / 오빠 / 형</b> — kattaroq aka-opaga (hatto qarindosh boʻlmasa ham)</li>
</ul>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu sizga tanish: oʻzbeklar ham notanish kattaroq odamga <em>aka</em>, <em>opa</em>,
<em>amaki</em> deb murojaat qiladi. Koreysda ham xuddi shu mantiq —
<b>오빠</b>, <b>언니</b>, <b>아저씨</b>. Qarindoshlik atamalari jamiyatga
kengaytirilgan.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">Notanish odamga darhol 반말 bilan gapirish.</p>
  <p class="pe-good">Har doim <b>존댓말</b>dan boshlang. 반말ga faqat taklif
     kelgandan keyin oʻting.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">나는 학생<s>입니다</s>.</p>
  <p class="pe-good"><b>저는</b> 학생입니다 — olmosh va gap oxiri mos kelishi kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Suhbatdoshni <s>당신</s> deb chaqirish.</p>
  <p class="pe-good">Ism + <b>씨</b> yoki lavozim: <b>지영 씨</b>, <b>선생님</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">"Bir yosh katta — deyarli tengdosh, 반말 boʻlaveradi."</p>
  <p class="pe-good">Koreyada <b>bir yosh ham farq</b>. 존댓말 ishlating.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Koreyada tanishganda nega 몇 살이에요? deb soʻraladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>javobni bilmasdan qaysi nutq darajasida
    gapirishni tanlab boʻlmaydi</strong>. Yosh farqi bir yil boʻlsa ham munosabatni
    oʻzgartiradi, shuning uchun bu savol qoʻpollik emas — amaliy zarurat.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Qaysi daraja "eng xavfsiz tanlov" hisoblanadi va nega?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>해요체</strong>. U muloyim, lekin sovuq emas.
    Rasmiy vaziyatda biroz iliq tuyulishi mumkin — bu kichik kamchilik. 반말ni notoʻgʻri
    ishlatish esa <em>qoʻpollik</em> hisoblanadi, ya'ni xatosi ancha
    qimmat.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nima uchun "나는 학생입니다" gʻalati?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>olmosh va gap oxiri mos emas</strong>.
    나 — 반말 olmoshi, 입니다 — eng rasmiy shakl. Toʻgʻrisi: <b>저는 학생입니다</b>
    (rasmiy) yoki <b>나는 학생이야</b> (반말).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     "말 놓으세요" nima degani va kim aytadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>"Erkin gapiravering" — ya'ni <strong>반말ga oʻtishga
    ruxsat</strong>. Odatda buni <em>kattaroq yoki maqomi yuqoriroq</em> odam aytadi.
    Bu taklif kelmaguncha 존댓말da qolish kerak.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Dilnoza yangi ish joyida boshligʻiga "안녕? 나는 딜노자야." dedi. Ikkita xatoni
     toping va tuzating.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi: <strong>안녕</strong> — 반말 salomi, boshliqqa
    <b>안녕하세요</b> deyish kerak. Ikkinchisi: <strong>나는 … 야</strong> ham 반말,
    toʻgʻrisi <b>저는 딜노자입니다</b> (yoki 딜노자예요). Toʻgʻri shakl:
    <b>안녕하세요? 저는 딜노자입니다.</b></p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>존댓말</b><span>hurmat nutqi</span></li>
  <li><b>반말</b><span>erkin, yaqin nutq</span></li>
  <li><b>합니다체</b><span>qat'iy rasmiy daraja</span></li>
  <li><b>해요체</b><span>kundalik hurmat darajasi</span></li>
  <li><b>저 / 나</b><span>men (hurmatli / oddiy)</span></li>
  <li><b>제 / 내</b><span>mening (hurmatli / oddiy)</span></li>
  <li><b>몇 살이에요?</b><span>Necha yoshdasiz?</span></li>
  <li><b>말 놓으세요</b><span>erkin gapiravering</span></li>
  <li><b>선생님</b><span>oʻqituvchi; hurmatli murojaat</span></li>
  <li><b>당신</b><span>siz (deyarli ishlatilmaydi)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>Koreys tilida munosabat <b>feʼlning oxirida</b> koʻrsatiladi, olmoshda emas.</li>
    <li>Uch daraja: <b>합니다체</b> (rasmiy) · <b>해요체</b> (kundalik hurmat) ·
        <b>반말</b> (yaqin).</li>
    <li>Bilmasangiz — <b>해요체</b>. U deyarli hech qachon xato emas.</li>
    <li><b>Bir yosh ham farq.</b> Tengdosh boʻlmasa, 존댓말.</li>
    <li>반말ga oʻtish — <b>kelishuv</b>, oʻz-oʻzidan boʻlmaydi.</li>
    <li>Olmosh va gap oxiri <b>mos kelishi</b> shart: 저 → 입니다, 나 → 이야.</li>
    <li>당신 emas — <b>ism + 씨</b> yoki lavozim.</li>
  </ul>
</div>
""",
    },
]
