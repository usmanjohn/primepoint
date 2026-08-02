# -*- coding: utf-8 -*-
"""Prime Korean — Block C, darslar 29–31 (buyruq, imkon, iltimos).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_29_31.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_29_31.py --author=prime
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
        "title": "PK-29: 동사 + (으)세요 / 지 마세요 — buyruq va taqiq",
        "category": "korean",
        "order": 29,
        "summary": (
            "Hurmatli buyruq va taqiqning asosiy qolipi. Bir shakl uch vazifada: "
            "iltimos, taqiq va suhbatdoshga nisbatan hurmatli darak."
        ),
        "stories": ["여기 앉으세요"],
        "content": """
<h2>PK-29: 동사 + (으)세요 / 지 마세요 — buyruq va taqiq</h2>

<p>Oʻqituvchi darsda “Kitobni oching” deydi. Doʻkonda sotuvchi “Bu yerga qarang”
deydi. Muzeyda esa yozuv turadi: “Rasmga olmang”. Bularning hammasi — buyruq. Koreys
tilida buyruqni hurmat bilan aytishning bitta asosiy qolipi bor va siz uni allaqachon
minglab marta eshitgansiz: <b>안녕하세요</b> ham aynan shu shakl.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Hurmatli buyruq — <b>(으)세요</b> ni yasashni oʻrganasiz</li>
    <li>Taqiq — <b>지 마세요</b> ni oʻrganasiz</li>
    <li>드세요, 주무세요, 계세요 kabi maxsus shakllarni bilib olasiz</li>
    <li>Nega bu shaklni <em>oʻzingiz haqingizda</em> ishlatib boʻlmasligini tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">oʻzak</span>
  <span class="pe-chip pe-chip--v">(으)세요</span>
  <span class="pe-chip pe-chip--opt">·</span>
  <span class="pe-chip pe-chip--s">oʻzak</span>
  <span class="pe-chip pe-chip--neg">지 마세요</span>
</div>

<h3>1. 받침 ayrisi</h3>

<p>Qoʻshimcha oʻzakka qoʻshiladi va tanlov har doimgidek <b>받침</b> ga qarab
qilinadi:</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">세요</span></p>
    <p>가<b>세요</b> · 오<b>세요</b> · 보<b>세요</b> · 공부하<b>세요</b></p>
    <p>Oʻzak unli bilan tugasa.</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">으세요</span></p>
    <p>읽<b>으세요</b> · 앉<b>으세요</b> · 받<b>으세요</b></p>
    <p>Oʻzak undosh bilan tugasa.</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>가다</td><td class="pk-stem">가</td><td class="pk-end">세요</td>
      <td class="pk-res">가세요</td><td class="pk-uz">boring</td></tr>
  <tr><td>오다</td><td class="pk-stem">오</td><td class="pk-end">세요</td>
      <td class="pk-res">오세요</td><td class="pk-uz">keling</td></tr>
  <tr><td>공부하다</td><td class="pk-stem">공부하</td><td class="pk-end">세요</td>
      <td class="pk-res">공부하세요</td><td class="pk-uz">oʻqing</td></tr>
  <tr><td>읽다</td><td class="pk-stem">읽</td><td class="pk-end">으세요</td>
      <td class="pk-res">읽으세요</td><td class="pk-uz">oʻqing (kitobni)</td></tr>
  <tr><td>앉다</td><td class="pk-stem">앉</td><td class="pk-end">으세요</td>
      <td class="pk-res">앉으세요</td><td class="pk-uz">oʻtiring</td></tr>
  <tr><td>받다</td><td class="pk-stem">받</td><td class="pk-end">으세요</td>
      <td class="pk-res">받으세요</td><td class="pk-uz">oling</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada ham buyruqning hurmatli shakli qoʻshimcha bilan yasaladi:
<br>• bor → bor<b>ing</b> · oʻqi → oʻqi<b>ng</b> · oʻtir → oʻtir<b>ing</b>
<br>Koreys tilida ham xuddi shunday — feʼlning oʻzagiga qoʻshimcha yopishadi va
soʻz tartibi umuman oʻzgarmaydi. Farqi bittagina: koreyscha qoʻshimcha
<b>받침</b> ga qarab ikki koʻrinishga ega, oʻzbekcha esa unli/undoshga qarab
<em>-ing</em> yoki <em>-ng</em> boʻladi. Ya'ni mantiq bir xil, faqat tanlov
shartlari boshqa.</div>

<h3>2. Bu “buyruq” emas — iltimos</h3>

<p>(으)세요 quruq buyruq emas. U <b>hurmatli taklif yoki iltimos</b>: “iltimos,
oʻtiring”, “marhamat, kiring”. Shuning uchun uni oʻqituvchi ham, sotuvchi ham,
doʻstingizning onasi ham bemalol ishlatadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">여기 앉으세요. 물 드세요.</p>
  <p class="pe-ex__uz">Bu yerga oʻtiring. Suv iching.</p>
  <p class="pe-ex__why">Ikkalasi ham mehmonga aytiladigan iliq gap — buyruq
     emas, marhamat.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 선생님, 이 책을 읽으세요?<br>나: 네, 매일 읽어요.</p>
  <p class="pe-ex__uz">A: Ustoz, bu kitobni oʻqiysizmi?<br>B: Ha, har kuni
     oʻqiyman.</p>
  <p class="pe-ex__why">Savol ohangi bilan aytilsa — bu buyruq emas, hurmatli
     savol. Quyidagi boʻlimga qarang.</p>
</div>

<h3>3. Ikkinchi vazifasi: suhbatdosh haqida hurmatli gap</h3>

<p>Aynan shu shakl <b>darak va savol</b> gapda ham ishlatiladi — lekin faqat
<em>siz gapirayotgan odam</em> yoki <em>hurmat qilinadigan uchinchi shaxs</em>
haqida:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Gap</th><th>Maʼnosi</th><th>Vazifasi</th></tr>
  <tr><td class="pk-res">앉으세요.</td><td class="pk-uz">Oʻtiring.</td>
      <td class="pk-stem">buyruq</td></tr>
  <tr><td class="pk-res">어디에 가세요?</td><td class="pk-uz">Qayerga ketyapsiz?</td>
      <td class="pk-stem">hurmatli savol</td></tr>
  <tr><td class="pk-res">선생님은 학교에 가세요.</td><td class="pk-uz">Ustoz maktabga
      boradilar.</td><td class="pk-stem">hurmatli darak</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Bu shaklni oʻzingiz haqingizda ishlatmang.</b> <s>저는 가세요</s> — notoʻgʻri,
chunki (으)세요 hurmat bildiradi, odam esa oʻzini hurmatlamaydi. Oʻzingiz haqingizda
oddiy <b>가요</b> deysiz. Oʻzbekchada ham “men boringlar” deb aytmaysiz-ku.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada hurmat <em>koʻplik</em> orqali beriladi: “Ustoz keldi<b>lar</b>”,
“Dadam aytdi<b>lar</b>”. Koreys tilida esa alohida hurmat qoʻshimchasi bor va
<b>(으)세요</b> — uning eng koʻp uchraydigan koʻrinishi. Ya'ni siz bilgan
narsaning boshqa shakli: fikr bir xil, quroli boshqa.</div>

<h3>4. ㄹ bilan tugagan oʻzaklar</h3>

<p>Oʻzak <b>ㄹ</b> bilan tugasa, ㄹ <em>tushib qoladi</em> va 세요 qoʻshiladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>만들다</td><td class="pk-stem">만들</td><td class="pk-res">만드세요</td>
      <td class="pk-uz">tayyorlang</td></tr>
  <tr><td>팔다</td><td class="pk-stem">팔</td><td class="pk-res">파세요</td>
      <td class="pk-uz">soting</td></tr>
  <tr><td>살다</td><td class="pk-stem">살</td><td class="pk-res">사세요</td>
      <td class="pk-uz">yashang</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<s>만들으세요</s> ham, <s>만들세요</s> ham emas — <b>만드세요</b>. ㄹ shunchaki
yoʻqoladi. Bu koreys tilidagi eng tartibli “notoʻgʻri” feʼl guruhi: ㄹ oʻzak
ㄴ, ㅂ, ㅅ dan oldin har doim ㄹ ni tashlaydi.</div>

<h3>5. Maxsus shakllar — yodlash kerak</h3>

<p>Beshta juda koʻp ishlatiladigan feʼlning hurmatli shakli butunlay boshqacha:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Oddiy feʼl</th><th>Hurmatli shakl</th><th>Maʼnosi</th></tr>
  <tr><td>먹다 / 마시다</td><td class="pk-res">드세요</td>
      <td class="pk-uz">yeng / iching (marhamat)</td></tr>
  <tr><td>자다</td><td class="pk-res">주무세요</td><td class="pk-uz">uxlang</td></tr>
  <tr><td>있다</td><td class="pk-res">계세요</td><td class="pk-uz">boʻling, turing</td></tr>
  <tr><td>말하다</td><td class="pk-res">말씀하세요</td><td class="pk-uz">gapiring</td></tr>
  <tr><td>주다</td><td class="pk-res">주세요</td><td class="pk-uz">bering</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">안녕히 주무세요. 안녕히 계세요.</p>
  <p class="pe-ex__uz">Xayrli tun (tinch uxlang). Xayr (siz qolasiz).</p>
  <p class="pe-ex__why">PK-9 dagi xayrlashuv iboralari aslida shu qolipda
     yasalgan — endi ularning ichini koʻrdingiz.</p>
</div>

<h3>6. Taqiq: 지 마세요</h3>

<p>“Qilmang” degani. Bu yerda <b>받침 ayrisi yoʻq</b> — 지 마세요 har qanday oʻzakka
toʻgʻridan-toʻgʻri yopishadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Taqiq</th><th>Maʼnosi</th></tr>
  <tr><td>가다</td><td class="pk-res">가지 마세요</td><td class="pk-uz">bormang</td></tr>
  <tr><td>먹다</td><td class="pk-res">먹지 마세요</td><td class="pk-uz">yemang</td></tr>
  <tr><td>울다</td><td class="pk-res">울지 마세요</td><td class="pk-uz">yigʻlamang</td></tr>
  <tr><td>사진을 찍다</td><td class="pk-res">사진을 찍지 마세요</td>
      <td class="pk-uz">rasmga olmang</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Taqiq uchun <b>안</b> ishlatilmaydi. <s>안 가세요</s> — bu “bormaysiz(mi)” degan
darak/savol, taqiq emas. Taqiq faqat <b>지 마세요</b>.</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Buyruq</p>
    <p><b>여기 앉으세요.</b></p>
    <p>Bu yerga oʻtiring.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Taqiq</p>
    <p><b>여기 앉지 마세요.</b></p>
    <p>Bu yerga oʻtirmang.</p>
  </div>
</div>

<h3>7. Rasmiy shakl: (으)십시오 / 지 마십시오</h3>

<p>Elon taxtalari, aeroport, metro, rasmiy xat — u yerda 합니다체 ishlatiladi:</p>

<div class="pk-level">
  <div class="pk-level__row pk-level__row--3">
    <span class="pk-level__name">해요체</span>
    <span class="pk-level__ko">앉으세요</span>
    <span class="pk-level__who">kundalik hurmat — eng koʻp ishlatiladi</span>
  </div>
  <div class="pk-level__row pk-level__row--4">
    <span class="pk-level__name">합니다체</span>
    <span class="pk-level__ko">앉으십시오</span>
    <span class="pk-level__who">eʼlon, rasmiy nutq, xizmat koʻrsatish</span>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">여기에서 사진을 찍지 마십시오.</p>
  <p class="pe-ex__uz">Bu yerda rasmga olmang.</p>
  <p class="pe-ex__why">Muzey yozuvi. Ogʻzaki nutqda esa 찍지 마세요 deyiladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">저는 학교에 <s>가세요</s>.</p>
  <p class="pe-good">Oʻzingiz haqingizda hurmat qoʻshimchasi ishlatilmaydi:
     저는 학교에 <b>가요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>읽세요</s> · <s>앉세요</s></p>
  <p class="pe-good">받침 bor → <b>으</b> qoʻshiladi: <b>읽으세요</b>,
     <b>앉으세요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>만들으세요</s></p>
  <p class="pe-good">ㄹ tushadi: <b>만드세요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">“Yemang” maʼnosida <s>안 먹으세요</s>.</p>
  <p class="pe-good">Taqiq — <b>먹지 마세요</b>. 안 먹으세요 esa “yemaysiz(mi)”
     degani.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Ustozga <s>먹으세요</s> deyish.</p>
  <p class="pe-good">먹다 ning hurmatli shakli boshqa: <b>드세요</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>앉다</b> dan hurmatli buyruq yasang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>앉으세요</strong>. Oʻzak <b>앉</b> — 받침
    bor (ㄵ), shuning uchun <b>으세요</b>. <s>앉세요</s> notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga nima tushadi? 여기에서 <span class="pe-blank">?</span>
     (“Bu yerda rasmga olmang.”) — 사진을 찍다</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>사진을 찍지 마세요</strong>. Taqiq har doim
    <b>지 마세요</b> — 안 emas. 지 마세요 da 받침 ayrisi yoʻq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega <s>저는 책을 읽으세요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <b>(으)세요 hurmat bildiradi</b>, odam esa
    oʻzini hurmatlamaydi. Toʻgʻrisi: <strong>저는 책을 읽어요</strong>. Bu shakl
    faqat suhbatdosh yoki hurmat qilinadigan uchinchi shaxs haqida
    ishlatiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>만들다</b> dan buyruq yasang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>만드세요</strong>. Oʻzak ㄹ bilan tugagani
    uchun ㄹ <em>tushib qoladi</em>. Xuddi shunday: 팔다 → 파세요, 살다 →
    사세요.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Mehmonga taom uzatyapsiz. 먹으세요 deysizmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Yoʻq — <strong>드세요</strong>. 먹다 va 마시다 ning
    hurmatli shakli maxsus: <b>드세요</b>. Xuddi shunday 자다 → 주무세요,
    있다 → 계세요.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)세요</b><span>…ing (hurmatli buyruq)</span></li>
  <li><b>지 마세요</b><span>…mang (taqiq)</span></li>
  <li><b>(으)십시오</b><span>…ing (rasmiy)</span></li>
  <li><b>드세요</b><span>yeng / iching (hurmatli)</span></li>
  <li><b>주무세요</b><span>uxlang (hurmatli)</span></li>
  <li><b>계세요</b><span>boʻling, turing (hurmatli)</span></li>
  <li><b>앉다</b><span>oʻtirmoq</span></li>
  <li><b>사진을 찍다</b><span>rasmga olmoq</span></li>
  <li><b>만들다</b><span>tayyorlamoq, yasamoq</span></li>
  <li><b>기다리다</b><span>kutmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>받침 yoʻq → <b>세요</b>, 받침 bor → <b>으세요</b>.</li>
    <li>ㄹ oʻzak ㄹ ni <b>tashlaydi</b>: 만들다 → 만드세요.</li>
    <li>Taqiq — faqat <b>지 마세요</b>, hech qachon 안 emas.</li>
    <li>Bu shakl <b>oʻzingiz haqingizda ishlatilmaydi</b>: 저는 가요, 가세요 emas.</li>
    <li>Savol ohangida u hurmatli savol boʻladi: <b>어디에 가세요?</b></li>
    <li>Maxsus shakllar: <b>드세요 · 주무세요 · 계세요 · 말씀하세요</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-30: 동사 + (으)ㄹ 수 있다/없다 — imkon va imkonsizlik",
        "category": "korean",
        "order": 30,
        "summary": (
            "“…ola olaman” va “…ololmayman” ni aytish. Qobiliyat ham, imkoniyat ham "
            "shu qolip bilan beriladi — va u PK-22 dagi 못 bilan qanday farq qilishini."
        ),
        "stories": ["저는 김치를 먹을 수 있어요"],
        "content": """
<h2>PK-30: 동사 + (으)ㄹ 수 있다/없다 — imkon va imkonsizlik</h2>

<p>Afsona koreyscha gapiradi, lekin xitoycha gapira <em>olmaydi</em>. Jasur suzishni
biladi, lekin bugun suza <em>olmaydi</em> — suv sovuq. Bu ikki gapda ham asosiy soʻz
bitta: <b>ola olish</b>. Koreys tilida buning uchun bitta qolip bor va u juda
mantiqiy tuzilgan.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ 수 있다</b> va <b>(으)ㄹ 수 없다</b> ni yasashni oʻrganasiz</li>
    <li>Nima uchun bu yerda 있다/없다 turganini tushunasiz</li>
    <li>Uni PK-22 dagi <b>못</b> bilan solishtirasiz</li>
    <li>Oʻtgan zamon va savol shakllarini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">oʻzak</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ 수</span>
  <span class="pe-chip pe-chip--aux">있어요</span>
  <span class="pe-chip pe-chip--opt">/</span>
  <span class="pe-chip pe-chip--neg">없어요</span>
</div>

<h3>1. 받침 ayrisi</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄹ 수 있어요</span></p>
    <p>가<b>ㄹ</b> → 갈 수 있어요 · 하<b>ㄹ</b> → 할 수 있어요</p>
    <p>ㄹ oʻzakning ostiga 받침 boʻlib yopishadi.</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">을 수 있어요</span></p>
    <p>먹<b>을</b> 수 있어요 · 읽<b>을</b> 수 있어요</p>
    <p>Alohida boʻgʻin qoʻshiladi.</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>가다</td><td class="pk-stem">가</td><td class="pk-res">갈 수 있어요</td>
      <td class="pk-uz">bora olaman</td></tr>
  <tr><td>하다</td><td class="pk-stem">하</td><td class="pk-res">할 수 있어요</td>
      <td class="pk-uz">qila olaman</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹</td><td class="pk-res">먹을 수 있어요</td>
      <td class="pk-uz">yeya olaman</td></tr>
  <tr><td>읽다</td><td class="pk-stem">읽</td><td class="pk-res">읽을 수 있어요</td>
      <td class="pk-uz">oʻqiy olaman</td></tr>
  <tr><td>만들다</td><td class="pk-stem">만들</td><td class="pk-res">만들 수 있어요</td>
      <td class="pk-uz">tayyorlay olaman</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bu ayni oʻsha ㄹ — siz uni PK-27 da <b>(으)ㄹ 거예요</b> da koʻrgansiz. Shuning uchun
qoida ham bir xil: oʻzak allaqachon ㄹ bilan tugasa, <b>yangi ㄹ qoʻshilmaydi</b> —
만들 수 있어요, <s>만들을 수 있어요</s> emas.</div>

<h3>2. Nega bu yerda 있다/없다 turibdi?</h3>

<p><b>수</b> — bu alohida soʻz, otning oʻzi. Maʼnosi “yoʻl, usul, imkon”. Demak
qolip soʻzma-soʻz shunday oʻqiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">갈 수 있어요.</p>
  <p class="pe-ex__uz">“Boradigan <b>imkon bor</b>.” → Bora olaman.</p>
  <p class="pe-ex__why">갈 = “boradigan”, 수 = “imkon”, 있어요 = “bor”.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">갈 수 없어요.</p>
  <p class="pe-ex__uz">“Boradigan <b>imkon yoʻq</b>.” → Bora olmayman.</p>
  <p class="pe-ex__why">Faqat 있어요 → 없어요 almashadi, boshqa hech narsa
     oʻzgarmaydi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu tuzilma sizga notanish emas. Oʻzbekchada ham aynan shunday deyish mumkin:
<em>“borish imkonim bor”</em>, <em>“aytishning iloji yoʻq”</em>. Va oddiy shakl ham
bir xil mantiqda ishlaydi: <b>bora olaman</b> — asosiy feʼl + yordamchi feʼl.
Koreyschada ham asosiy feʼl (갈) oldinda, imkon bildiruvchi qism (수 있어요) keyinda.
Ingliz tilida esa <em>can</em> feʼldan <em>oldin</em> keladi — ya'ni bu yerda ham
oʻzbek tili sizga yaqinroq.</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Talaffuz</span>
<b>수</b> bu qolipda deyarli har doim qattiq oʻqiladi: 갈 수 있어요 →
<b>[갈 쑤 이써요]</b>. Bu ㄹ 받침dan keyingi 경음화 (PK-8). Yozilishi esa oʻzgarmaydi.</div>

<div class="pk-say">
  <span class="pk-say__from">할 수 있어요</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[할 쑤 이써요]</span>
  <span class="pk-say__why">경음화 — ㄹ dan keyin ㅅ qattiqlashadi</span>
</div>

<h3>3. Savol va javob</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 한국어를 할 수 있어요?<br>나: 네, 조금 할 수 있어요.</p>
  <p class="pe-ex__uz">A: Koreyscha gapira olasizmi?<br>B: Ha, ozgina gapira
     olaman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 매운 음식을 먹을 수 있어요?<br>나: 아니요, 먹을 수 없어요.</p>
  <p class="pe-ex__uz">A: Achchiq ovqat yeya olasizmi?<br>B: Yoʻq, yeya olmayman.</p>
</div>

<h3>4. Oʻtgan zamon</h3>

<p>Tuslanish har doim <b>oxirgi soʻzda</b> — 있다/없다 da:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Zamon</th><th>Shakl</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">Hozirgi</td><td class="pk-stem">갈 수 있어요</td>
      <td class="pk-uz">bora olaman</td></tr>
  <tr><td class="pk-res">Oʻtgan</td><td class="pk-stem">갈 수 있었어요</td>
      <td class="pk-uz">bora oldim</td></tr>
  <tr><td class="pk-res">Inkor</td><td class="pk-stem">갈 수 없어요</td>
      <td class="pk-uz">bora olmayman</td></tr>
  <tr><td class="pk-res">Oʻtgan inkor</td><td class="pk-stem">갈 수 없었어요</td>
      <td class="pk-uz">bora olmadim</td></tr>
  <tr><td class="pk-res">Rasmiy</td><td class="pk-stem">갈 수 있습니다</td>
      <td class="pk-uz">bora olaman (합니다체)</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<s>갔을 수 있어요</s> deb yasamang — oʻtgan zamon qoʻshimchasi asosiy feʼlga emas,
<b>있다</b> ga qoʻshiladi: <b>갈 수 있었어요</b>. Bu PK-28 dagi 고 싶었어요 bilan
bir xil mantiq.</div>

<h3>5. 못 bilan farqi</h3>

<p>PK-22 da <b>못</b> ni oʻrgangansiz — u ham “olmaslik” bildiradi. Ikkalasi
koʻp joyda almashinadi, lekin ohangi boshqacha:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">못 가요</p>
    <p>Qisqa, ogʻzaki, kundalik.</p>
    <p>Koʻpincha <b>bu safar</b> imkon yoʻqligi: ishim bor, kasalman.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">갈 수 없어요</p>
    <p>Toʻliqroq, yumshoqroq, yozma nutqda ham.</p>
    <p>Koʻpincha <b>umuman</b> imkon yoʻqligi: yoʻl yopiq, ruxsat yoʻq.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Boshlangʻich darajada ikkalasini ham toʻgʻri deb hisoblang — <b>못 먹어요</b> va
<b>먹을 수 없어요</b> deyarli bir xil tushuniladi. Lekin <em>ijobiy</em> tomonda
못 ning jufti yoʻq: “yeya olaman” faqat <b>먹을 수 있어요</b>. Shuning uchun bu qolip
kengroq.</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Maʼno</th><th>못 bilan</th><th>수 bilan</th></tr>
  <tr><td class="pk-res">…ola olaman</td><td class="pk-uz">— (yoʻq)</td>
      <td class="pk-stem">할 수 있어요</td></tr>
  <tr><td class="pk-res">…ololmayman</td><td class="pk-uz">못 해요</td>
      <td class="pk-stem">할 수 없어요</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>먹 수 있어요</s></p>
  <p class="pe-good">받침 bor → 을: <b>먹을 수 있어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>만들을 수 있어요</s></p>
  <p class="pe-good">Oʻzak allaqachon ㄹ bilan tugagan: <b>만들 수 있어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>갔을 수 있어요</s> (“bora oldim” maʼnosida)</p>
  <p class="pe-good">Tuslanish 있다 da: <b>갈 수 있었어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>갈 수 안 있어요</s></p>
  <p class="pe-good">Inkor uchun alohida feʼl bor: <b>갈 수 없어요</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>읽다</b> dan “oʻqiy olaman” yasang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>읽을 수 있어요</strong>. Oʻzak 읽 — 받침 bor,
    shuning uchun <b>을 수</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Nega <s>만들을 수 있어요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Oʻzak <b>만들</b> allaqachon ㄹ bilan tugaydi —
    yangi ㄹ qoʻshilmaydi: <strong>만들 수 있어요</strong>. Xuddi PK-27 dagi
    살 거예요 kabi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>수</b> soʻzining maʼnosi nima va u nima uchun bu qolipda turibdi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><b>수</b> — “yoʻl, usul, imkon” degan ot. Shuning
    uchun qolip soʻzma-soʻz <strong>“…qiladigan imkon bor / yoʻq”</strong> deb
    oʻqiladi va oxirida 있다 yoki 없다 turadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     “Kecha kelolmadim” ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>어제 올 수 없었어요.</strong> Oʻzak 오 —
    받침 yoʻq → 올 수. Oʻtgan zamon <b>없다</b> ga qoʻshiladi. 어제 못 왔어요 ham
    toʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     <b>할 수 있어요</b> qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[할 쑤 이써요]</strong>. ㄹ 받침dan keyin ㅅ
    qattiqlashadi — 경음화 (PK-8). 있어요 esa 연음화 bilan [이써요] boʻladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ 수 있다</b><span>…ola olmoq</span></li>
  <li><b>(으)ㄹ 수 없다</b><span>…ololmaslik</span></li>
  <li><b>수</b><span>yoʻl, usul, imkon</span></li>
  <li><b>수영하다</b><span>suzmoq</span></li>
  <li><b>운전하다</b><span>haydamoq (mashina)</span></li>
  <li><b>맵다</b><span>achchiq</span></li>
  <li><b>음식</b><span>ovqat</span></li>
  <li><b>조금</b><span>ozgina</span></li>
  <li><b>혼자</b><span>yolgʻiz, oʻzi</span></li>
  <li><b>피아노</b><span>pianino</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>받침 yoʻq → <b>ㄹ 수 있어요</b>, 받침 bor → <b>을 수 있어요</b>.</li>
    <li>ㄹ oʻzak yangi ㄹ olmaydi: <b>만들 수 있어요</b>.</li>
    <li><b>수</b> = “imkon” degan ot — shuning uchun 있다/없다 keladi.</li>
    <li>Inkor — <b>없어요</b>, hech qachon <s>안 있어요</s> emas.</li>
    <li>Tuslanish oxirgi soʻzda: <b>갈 수 있었어요</b>.</li>
    <li>Talaffuz: <b>[갈 쑤]</b> — 경음화.</li>
    <li><b>못</b> qisqa va ogʻzaki, <b>수 없다</b> toʻliq va kengroq.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-31: 동사 + 아/어 주다 — iltimos qilish va yordam berish",
        "category": "korean",
        "order": 31,
        "summary": (
            "Koreysda iltimos qilishning asosiy yoʻli. Oʻzbekchadagi “-ib bering” "
            "bilan deyarli aynan bir xil ishlaydigan qolip."
        ),
        "stories": ["사진 좀 찍어 주세요"],
        "content": """
<h2>PK-31: 동사 + 아/어 주다 — iltimos qilish va yordam berish</h2>

<p>Koreyada koʻchada turibsiz va suratga tushmoqchisiz. Yoningizdan oʻtayotgan odamga
nima deysiz? Oʻzbekchada bu juda oson: <em>“Rasmga olib <b>bering</b>”</em>. Koreys
tilida ham xuddi shu mantiq ishlaydi — asosiy feʼlga <b>주다</b> (“bermoq”)
qoʻshiladi va ish <em>boshqa odam uchun</em> qilinishi maʼlum boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>아/어 주다</b> qolipini yasashni oʻrganasiz</li>
    <li>Iltimos qilishning eng tabiiy shakli — <b>아/어 주세요</b> ni bilib olasiz</li>
    <li>Kimga qilinganini koʻrsatuvchi <b>에게 / 한테</b> ni oʻrganasiz</li>
    <li>Iltimosni yumshatadigan <b>좀</b> ni ishlatishni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">아/어 shakli</span>
  <span class="pe-chip pe-chip--v">주다</span>
  <span class="pe-chip pe-chip--opt">→</span>
  <span class="pe-chip pe-chip--aux">주세요</span>
</div>

<h3>1. Qolip: 아/어 shakli + 주다</h3>

<p>Bu yerda <b>받침 ayrisi yoʻq</b>. PK-18 da oʻrgangan <b>아/어</b> shaklini olasiz
va uning yoniga 주다 ni qoʻyasiz:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>아/어 shakli</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>읽다</td><td class="pk-stem">읽어</td><td class="pk-res">읽어 주다</td>
      <td class="pk-uz">oʻqib bermoq</td></tr>
  <tr><td>사다</td><td class="pk-stem">사</td><td class="pk-res">사 주다</td>
      <td class="pk-uz">sotib olib bermoq</td></tr>
  <tr><td>하다</td><td class="pk-stem">해</td><td class="pk-res">해 주다</td>
      <td class="pk-uz">qilib bermoq</td></tr>
  <tr><td>가르치다</td><td class="pk-stem">가르쳐</td><td class="pk-res">가르쳐 주다</td>
      <td class="pk-uz">oʻrgatib bermoq</td></tr>
  <tr><td>만들다</td><td class="pk-stem">만들어</td><td class="pk-res">만들어 주다</td>
      <td class="pk-uz">tayyorlab bermoq</td></tr>
  <tr><td>찍다</td><td class="pk-stem">찍어</td><td class="pk-res">찍어 주다</td>
      <td class="pk-uz">rasmga olib bermoq</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu qolip oʻzbek tilida <b>aynan bor</b>: <em>oʻqi<b>b bering</b></em>,
<em>yoz<b>ib bering</b></em>, <em>ochi<b>b bering</b></em>. Ikkala tilda ham asosiy
feʼl oldinda, “bermoq” esa keyinda turadi va ishning <em>kimningdir foydasiga</em>
qilinganini bildiradi. Shuning uchun 읽어 주세요 ni yodlash shart emas — uni
<b>“oʻqib bering”</b> deb oʻylang, tuzilishi bir xil. Ingliz tilida esa bunday qolip
umuman yoʻq (<em>read it for me</em> — butunlay boshqa tuzilma).</div>

<h3>2. Iltimos: 아/어 주세요</h3>

<p>Endi PK-29 ni bu yerga ulaymiz: 주다 ning hurmatli buyruq shakli — <b>주세요</b>.
Demak <b>아/어 주세요</b> = “…qilib bering”. Bu koreys tilidagi eng koʻp ishlatiladigan
iltimos qolipi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">사진을 찍어 주세요.</p>
  <p class="pe-ex__uz">Rasmga olib bering.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 선생님, 다시 말해 주세요.<br>나: 네, 천천히 말할 거예요.</p>
  <p class="pe-ex__uz">A: Ustoz, yana bir marta aytib bering.<br>B: Ha, sekin
     aytaman.</p>
  <p class="pe-ex__why">다시 = yana, 천천히 = sekin. Darsda eng koʻp keradigan
     gap shu.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">문을 열어 주세요. 창문은 닫아 주세요.</p>
  <p class="pe-ex__uz">Eshikni ochib bering. Derazani esa yopib bering.</p>
</div>

<h3>3. 주세요 ning ikki xil ishlatilishi</h3>

<p>Diqqat: <b>주세요</b> yolgʻiz ham ishlatiladi, lekin maʼnosi boshqa boʻladi:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Ot + 을/를 주세요</p>
    <p><b>물을 주세요.</b></p>
    <p>Suv bering. — <em>Narsani</em> soʻrayapsiz.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Feʼl + 아/어 주세요</p>
    <p><b>물을 사 주세요.</b></p>
    <p>Suv sotib olib bering. — <em>Ishni</em> soʻrayapsiz.</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Otdan keyin — toʻgʻridan-toʻgʻri <b>주세요</b>. Feʼldan keyin — avval
<b>아/어</b> shakli, keyin 주세요. <s>물 주어 주세요</s> ham,
<s>사 주세요를 물</s> ham emas.</div>

<h3>4. Kimga? — 에게 / 한테</h3>

<p>Ish kimning foydasiga qilinganini aytish uchun odamga <b>에게</b> yoki
<b>한테</b> qoʻshiladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Shakl</th><th>Uslubi</th><th>Misol</th></tr>
  <tr><td class="pk-stem">한테</td><td class="pk-uz">ogʻzaki, kundalik</td>
      <td class="pk-res">친구한테 책을 사 줬어요.</td></tr>
  <tr><td class="pk-stem">에게</td><td class="pk-uz">yozma, rasmiy</td>
      <td class="pk-res">친구에게 책을 사 줬어요.</td></tr>
  <tr><td class="pk-stem">께</td><td class="pk-uz">hurmatli (ustoz, ota-ona)</td>
      <td class="pk-res">선생님께 편지를 써 줬어요.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu — oʻzbekchadagi <b>-ga</b> qoʻshimchasi: “doʻstim<b>ga</b> oldim”,
“ustoz<b>ga</b> yozdim”. Farqi shuki, koreys tilida <em>odam</em> uchun
에게/한테, <em>joy</em> uchun esa 에 ishlatiladi (PK-14). Ya'ni:
<br>• 학교<b>에</b> 가요 — maktab<b>ga</b> boraman (joy)
<br>• 친구<b>한테</b> 줘요 — doʻstim<b>ga</b> beraman (odam)
<br>Oʻzbekchada ikkalasi ham <em>-ga</em>, koreysda esa ikki xil qoʻshimcha.
Aynan shu yerda oʻzbek oʻquvchisi eng koʻp adashadi.</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어머니가 저에게 김치를 만들어 주셨어요.</p>
  <p class="pe-ex__uz">Onam menga kimchi tayyorlab berdilar.</p>
  <p class="pe-ex__why">주셨어요 — 주다 ning hurmatli oʻtgan zamoni. Hozircha uni
     shunchaki tanib olish yetarli.</p>
</div>

<h3>5. Iltimosni yumshatuvchi 좀</h3>

<p><b>좀</b> — “ozgina” degan soʻzning qisqargani, lekin iltimosda u miqdor emas,
<em>xushmuomalalik</em> bildiradi. Oʻzbekchadagi “iltimos” yoki “-chi” kabi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">사진 좀 찍어 주세요.</p>
  <p class="pe-ex__uz">Rasmga olib yuboring-chi. / Iltimos, rasmga olib bering.</p>
  <p class="pe-ex__why">좀 gapni yumshoq va tabiiy qiladi. Usiz ham toʻgʻri, lekin
     quruqroq eshitiladi.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
좀 feʼldan <em>oldin</em> turadi va koʻpincha 을/를 tushirib qoldiriladi:
<b>사진 좀 찍어 주세요</b>. Bu notoʻgʻri emas — bu tabiiy ogʻzaki nutq (PK-26 da
soʻroq soʻzlari bilan ham shunday koʻrgansiz).</div>

<h3>6. Zamon va inkor</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Shakl</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">Iltimos</td><td class="pk-stem">읽어 주세요</td>
      <td class="pk-uz">oʻqib bering</td></tr>
  <tr><td class="pk-res">Hozirgi</td><td class="pk-stem">읽어 줘요</td>
      <td class="pk-uz">oʻqib beradi</td></tr>
  <tr><td class="pk-res">Oʻtgan</td><td class="pk-stem">읽어 줬어요</td>
      <td class="pk-uz">oʻqib berdi</td></tr>
  <tr><td class="pk-res">Kelasi</td><td class="pk-stem">읽어 줄 거예요</td>
      <td class="pk-uz">oʻqib beradi (reja)</td></tr>
  <tr><td class="pk-res">Taqiq</td><td class="pk-stem">읽어 주지 마세요</td>
      <td class="pk-uz">oʻqib bermang</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Tuslanish har doim <b>주다</b> da boʻladi, asosiy feʼlda emas:
<s>읽었어 줘요</s> notoʻgʻri, toʻgʻrisi <b>읽어 줬어요</b>. Bu PK-28 dagi
고 싶었어요 va PK-30 dagi 갈 수 있었어요 bilan bir xil qoida — <em>oxirgi soʻz
tuslanadi</em>.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>읽고 주세요</s></p>
  <p class="pe-good">고 emas, <b>아/어</b> shakli: <b>읽어 주세요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>읽었어 줬어요</s></p>
  <p class="pe-good">Tuslanish faqat 주다 da: <b>읽어 줬어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">친구<s>에</s> 책을 사 줬어요.</p>
  <p class="pe-good">Odam → <b>한테 / 에게</b>: 친구<b>한테</b> 책을 사 줬어요.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>물을 주어 주세요</s></p>
  <p class="pe-good">Ot bilan 주다 takrorlanmaydi: <b>물을 주세요</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>가르치다</b> dan “oʻrgatib bering” yasang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>가르쳐 주세요</strong>. Avval 아/어 shakli —
    가르치 + 어 → <b>가르쳐</b>, keyin 주세요.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>물을 주세요</b> va <b>물을 사 주세요</b> farqi nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — <strong>narsa</strong> soʻrayapti
    (“suv bering”). Ikkinchisi — <strong>ish</strong> soʻrayapti (“suv sotib olib
    bering”). Otdan keyin toʻgʻridan-toʻgʻri 주세요, feʼldan keyin esa avval
    아/어 shakli kerak.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga nima tushadi? 친구<span class="pe-blank">?</span> 책을 사 줬어요.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>한테</strong> (yoki yozma nutqda
    <b>에게</b>). Odamga — 한테/에게, joyga — 에. <s>친구에</s> notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     “Onam menga ovqat tayyorlab berdilar” ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>어머니가 저에게 음식을 만들어 주셨어요.</strong>
    Oddiyroq shakli ham toʻgʻri: 어머니가 음식을 만들어 줬어요. Tuslanish
    <b>주다</b> da.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     <b>좀</b> nima uchun qoʻshiladi va qayerda turadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>좀 iltimosni <strong>yumshatadi</strong> —
    oʻzbekchadagi “iltimos” yoki “-chi” kabi. U <b>feʼldan oldin</b> turadi:
    사진 좀 찍어 주세요. Bu yerda u “ozgina” degan miqdorni bildirmaydi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아/어 주다</b><span>…ib bermoq</span></li>
  <li><b>아/어 주세요</b><span>…ib bering (iltimos)</span></li>
  <li><b>한테 / 에게</b><span>…ga (odamga)</span></li>
  <li><b>좀</b><span>iltimos, -chi (yumshatuvchi)</span></li>
  <li><b>다시</b><span>yana, qaytadan</span></li>
  <li><b>천천히</b><span>sekin</span></li>
  <li><b>가르치다</b><span>oʻrgatmoq</span></li>
  <li><b>열다 / 닫다</b><span>ochmoq / yopmoq</span></li>
  <li><b>도와주다</b><span>yordam bermoq</span></li>
  <li><b>편지</b><span>xat</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>아/어 shakli + 주다</b> — 받침 ayrisi yoʻq.</li>
    <li>Oʻzbekchadagi <b>“-ib bering”</b> bilan bir xil tuzilma.</li>
    <li>Iltimosning asosiy shakli — <b>아/어 주세요</b>.</li>
    <li>Ot bilan esa toʻgʻridan-toʻgʻri <b>주세요</b>: 물을 주세요.</li>
    <li>Odam → <b>한테 / 에게 / 께</b>, joy → 에.</li>
    <li><b>좀</b> feʼldan oldin turib iltimosni yumshatadi.</li>
    <li>Tuslanish har doim <b>주다</b> da: 읽어 <b>줬어요</b>.</li>
  </ul>
</div>
""",
    },
]
