# -*- coding: utf-8 -*-
"""Prime Korean — Block C boshlanishi, darslar 23–25 (sonlar va vaqt).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_23_25.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_23_25.py --author=prime
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
        "title": "PK-23: Sonlar 1: 한자어 sonlar (일, 이, 삼…) va ular nimani sanaydi",
        "category": "korean",
        "order": 23,
        "summary": (
            "Koreys tilida ikkita son tizimi bor. Birinchisi — xitoy ildizli sonlar: "
            "pul, sana, daqiqa, telefon raqami. Va ular mingga emas, oʻn mingga boʻlinadi."
        ),
        "stories": ["전화번호가 몇 번이에요?"],
        "content": """
<h2>PK-23: Sonlar 1: 한자어 sonlar (일, 이, 삼…) va ular nimani sanaydi</h2>

<p>Koreys tilida sanashning <b>ikki xil tizimi</b> bor — va ular almashtirilmaydi. Bu
yangi oʻquvchini qoʻrqitadi, lekin aslida mantiq oddiy: bittasi <em>oʻlchov va
raqamlar</em> uchun, ikkinchisi <em>narsalarni sanash</em> uchun. Bugun birinchisini
oʻrganamiz — <b>한자어</b>, ya'ni xitoy ildizli sonlarni.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>일 dan 십 gacha va undan yuqorisini oʻqiysiz</li>
    <li>한자어 sonlar aynan nimani sanashini bilib olasiz</li>
    <li>Koreys sonlari nega <b>만</b> (10 000) bilan boʻlinishini tushunasiz</li>
    <li>Ikkita talaffuz istisnosini eslab qolasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">한자어 sonlar nimani sanaydi</span>
  <span class="pe-chip pe-chip--o">pul</span>
  <span class="pe-chip pe-chip--o">sana</span>
  <span class="pe-chip pe-chip--o">daqiqa</span>
  <span class="pe-chip pe-chip--o">telefon</span>
  <span class="pe-chip pe-chip--o">qavat</span>
</div>

<h3>1. Birdan oʻngacha</h3>

<div class="pk-hangul">
  <div class="pk-hangul__c"><span class="pk-hangul__ch">일</span>
    <span class="pk-hangul__rom">1</span><span class="pk-hangul__uz">bir</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">이</span>
    <span class="pk-hangul__rom">2</span><span class="pk-hangul__uz">ikki</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">삼</span>
    <span class="pk-hangul__rom">3</span><span class="pk-hangul__uz">uch</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">사</span>
    <span class="pk-hangul__rom">4</span><span class="pk-hangul__uz">toʻrt</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">오</span>
    <span class="pk-hangul__rom">5</span><span class="pk-hangul__uz">besh</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">육</span>
    <span class="pk-hangul__rom">6</span><span class="pk-hangul__uz">olti</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">칠</span>
    <span class="pk-hangul__rom">7</span><span class="pk-hangul__uz">yetti</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">팔</span>
    <span class="pk-hangul__rom">8</span><span class="pk-hangul__uz">sakkiz</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">구</span>
    <span class="pk-hangul__rom">9</span><span class="pk-hangul__uz">toʻqqiz</span></div>
  <div class="pk-hangul__c"><span class="pk-hangul__ch">십</span>
    <span class="pk-hangul__rom">10</span><span class="pk-hangul__uz">oʻn</span></div>
</div>

<p>Nol uchun ikkita soʻz bor: <b>영</b> (matematikada) va <b>공</b> (telefon
raqamlarida).</p>

<h3>2. Oʻndan yuqorisi — qoʻshib yasaladi</h3>

<p>Bu yerda hech qanday yangi soʻz yoʻq. Sonlar shunchaki birlashtiriladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Raqam</th><th>Tuzilishi</th><th>Koreyscha</th></tr>
  <tr><td class="pk-res">11</td><td class="pk-stem">10 + 1</td><td class="pk-end">십일</td></tr>
  <tr><td class="pk-res">15</td><td class="pk-stem">10 + 5</td><td class="pk-end">십오</td></tr>
  <tr><td class="pk-res">20</td><td class="pk-stem">2 × 10</td><td class="pk-end">이십</td></tr>
  <tr><td class="pk-res">37</td><td class="pk-stem">3 × 10 + 7</td><td class="pk-end">삼십칠</td></tr>
  <tr><td class="pk-res">100</td><td class="pk-stem">—</td><td class="pk-end">백</td></tr>
  <tr><td class="pk-res">1 000</td><td class="pk-stem">—</td><td class="pk-end">천</td></tr>
  <tr><td class="pk-res">10 000</td><td class="pk-stem">—</td><td class="pk-end">만</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Tuzilish oʻzbekcha bilan bir xil: <em>oʻttiz yetti</em> = <em>uch oʻn yetti</em> →
<b>삼십칠</b>. Koreysda ham katta birlik oldin, kichigi keyin. Farqi shundaki, oʻzbekchada
“yigirma”, “oʻttiz” alohida soʻzlar, koreyschada esa ular <b>ochiq hisob</b>: 이십, 삼십.
Ya'ni yodlash kamroq.</div>

<h3>3. Eng qiyin joy: 만 = 10 000</h3>

<p>Oʻzbekchada katta sonlar <b>mingga</b> boʻlinadi: <em>ming, million, milliard</em>.
Koreysda esa <b>oʻn mingga</b> — <b>만</b>. Bu shunchaki boshqa qadam, lekin dastlab
chalkashtiradi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Raqam</th><th>Oʻzbekcha</th><th>Koreyscha</th><th>Tuzilishi</th></tr>
  <tr><td class="pk-res">10 000</td><td class="pk-uz">oʻn ming</td>
      <td class="pk-end">만</td><td class="pk-stem">1 × 만</td></tr>
  <tr><td class="pk-res">50 000</td><td class="pk-uz">ellik ming</td>
      <td class="pk-end">오만</td><td class="pk-stem">5 × 만</td></tr>
  <tr><td class="pk-res">100 000</td><td class="pk-uz">yuz ming</td>
      <td class="pk-end">십만</td><td class="pk-stem">10 × 만</td></tr>
  <tr><td class="pk-res">1 000 000</td><td class="pk-uz">bir million</td>
      <td class="pk-end">백만</td><td class="pk-stem">100 × 만</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Amaliy hiyla: katta raqamni <b>oʻngdan boshlab toʻrttadan</b> ajrating, uchtadan emas.
1 000 000 → <b>100|0000</b> → “yuz <b>만</b>” → <b>백만</b>. Oʻzbekcha vergul (1,000,000)
bu yerda yordam bermaydi — koreys miyasi boshqa joyga vergul qoʻyadi.</div>

<h3>4. Ikkita talaffuz istisnosi</h3>

<div class="pk-say">
  <span class="pk-say__from">십육</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[심뉵]</span>
  <span class="pk-say__why">16 — 비음화 bilan oʻzgaradi</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">육십</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[육씹]</span>
  <span class="pk-say__why">60 — 경음화</span>
</div>

<h3>5. Qayerda ishlatiladi</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima</th><th>Birlik</th><th>Misol</th></tr>
  <tr><td class="pk-res">Pul</td><td class="pk-stem">원</td>
      <td class="pk-uz">오천 원 — 5000 von</td></tr>
  <tr><td class="pk-res">Daqiqa</td><td class="pk-stem">분</td>
      <td class="pk-uz">삼십 분 — 30 daqiqa</td></tr>
  <tr><td class="pk-res">Yil / oy / kun</td><td class="pk-stem">년 / 월 / 일</td>
      <td class="pk-uz">이천이십육년 — 2026-yil</td></tr>
  <tr><td class="pk-res">Qavat</td><td class="pk-stem">층</td>
      <td class="pk-uz">삼 층 — 3-qavat</td></tr>
  <tr><td class="pk-res">Telefon raqami</td><td class="pk-stem">번</td>
      <td class="pk-uz">공일공… — 010…</td></tr>
  <tr><td class="pk-res">Sinf / kurs</td><td class="pk-stem">학년</td>
      <td class="pk-uz">이 학년 — 2-kurs</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 책은 만 원이에요.</p>
  <p class="pe-ex__uz">Bu kitob 10 000 von.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">제 전화번호는 공일공 이삼사오 육칠팔구예요.</p>
  <p class="pe-ex__uz">Mening telefon raqamim 010-2345-6789.</p>
  <p class="pe-ex__why">Telefon raqamida nol — <b>공</b>, va har bir raqam alohida
     oʻqiladi.</p>
</div>

<h3>6. 몇 — “nechta?”</h3>

<p>Son soʻrash uchun <b>몇</b> ishlatiladi va u birlikdan <em>oldin</em> turadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 전화번호가 몇 번이에요?<br>나: 공일공 … 이에요.</p>
  <p class="pe-ex__uz">A: Telefon raqamingiz necha?<br>B: 010-… .</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">지금 몇 층에 있어요?</p>
  <p class="pe-ex__uz">Hozir nechanchi qavatdasiz?</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">1 000 000 ni <s>천천</s> deb yasash.</p>
  <p class="pe-good">Koreysda oʻn ming birlik: <b>백만</b> (100 × 만).</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Telefon raqamida nolni <s>영</s> deyish.</p>
  <p class="pe-good">Telefon uchun <b>공</b>: 공일공.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">십육 ni "sib-yuk" deb oʻqish.</p>
  <p class="pe-good">비음화: <b>[심뉵]</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Yoshni 한자어 son bilan aytish.</p>
  <p class="pe-good">Yosh uchun boshqa tizim kerak — PK-24 darsi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>37</b> ni koreyschada yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>삼십칠</strong> — 3 × 10 + 7. Oʻzbekcha
    “oʻttiz yetti” bilan bir xil mantiq, faqat “oʻttiz” alohida soʻz emas,
    <em>삼십</em> boʻlib ochiq hisoblanadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>100 000</b> ni koreyschada yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>십만</strong> — 10 × 만 (10 000). Oʻngdan
    toʻrttadan ajrating: 10|0000. Oʻzbekcha “yuz ming” deb oʻylasangiz
    adashasiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega koreys sonlarini uchtadan emas, toʻrttadan ajratish kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki koreys tilida katta birlik <strong>만 = 10 000</strong>,
    ming emas. Oʻzbekcha/inglizcha vergul (1,000,000) uchtadan qoʻyiladi va koreys
    tizimiga mos kelmaydi. Toʻgʻri ajratish: <b>100|0000 = 백만</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     “Bu kitob 5000 von” ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>이 책은 오천 원이에요.</strong> Pul — 한자어 son
    bilan. 오천 = 5 × 1000.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Jasur telefon raqamini "영일영…" deb aytdi. Nimani tuzatish kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Telefon raqamida nol <strong>공</strong> deb aytiladi,
    영 emas: <b>공일공</b>. 영 esa matematikada ishlatiladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>일, 이, 삼, 사, 오</b><span>1, 2, 3, 4, 5</span></li>
  <li><b>육, 칠, 팔, 구, 십</b><span>6, 7, 8, 9, 10</span></li>
  <li><b>백 / 천 / 만</b><span>100 / 1000 / 10 000</span></li>
  <li><b>영 / 공</b><span>nol (matematika / telefon)</span></li>
  <li><b>원</b><span>von (pul birligi)</span></li>
  <li><b>분</b><span>daqiqa</span></li>
  <li><b>층</b><span>qavat</span></li>
  <li><b>번</b><span>raqam, marta</span></li>
  <li><b>전화번호</b><span>telefon raqami</span></li>
  <li><b>몇</b><span>nechta, necha</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>한자어 sonlar</b> — pul, sana, daqiqa, telefon, qavat, kurs uchun.</li>
    <li>Oʻndan yuqorisi <b>qoʻshib yasaladi</b>: 삼십칠 = 3×10+7.</li>
    <li><b>만 = 10 000.</b> Raqamni oʻngdan <b>toʻrttadan</b> ajrating.</li>
    <li>Nol: <b>영</b> matematikada, <b>공</b> telefonda.</li>
    <li>Istisnolar: 십육 <b>[심뉵]</b>, 육십 <b>[육씹]</b>.</li>
    <li><b>몇</b> — “nechta?”, birlikdan oldin turadi: 몇 번, 몇 층.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-24: Sonlar 2: 고유어 sonlar (하나, 둘…) va sanoq soʻzlari 개 / 명 / 마리",
        "category": "korean",
        "order": 24,
        "summary": (
            "Ikkinchi son tizimi — narsalarni sanash uchun. Sanoq soʻzlari sizga tanish: "
            "oʻzbekchada ham “besh dona olma”, “uch nafar odam” deymiz."
        ),
        "stories": ["학생이 몇 명 있어요?"],
        "content": """
<h2>PK-24: Sonlar 2: 고유어 sonlar (하나, 둘…) va sanoq soʻzlari 개 / 명 / 마리</h2>

<p>Ikkinchi tizim — <b>고유어</b>, ya'ni asl koreys sonlari. Ular narsalarni,
odamlarni, hayvonlarni sanaydi va yoshni aytadi. Bu darsda ikkita yangilik bor: sonlarning
oʻzi, va ulardan keyin keladigan <b>sanoq soʻzlari</b>. Ikkinchisi sizga tanish
tuyuladi — chunki oʻzbek tilida ham xuddi shunday narsa bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>하나 dan 열 gacha va oʻnliklarni oʻrganasiz</li>
    <li>Toʻrtta sonning sanoq oldidagi qisqargan shaklini bilib olasiz</li>
    <li>개, 명, 마리, 살 kabi sanoq soʻzlarini ishlatasiz</li>
    <li>Koreys va oʻzbek soʻz tartibi farqini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Sanash qolipi</span>
  <span class="pe-chip pe-chip--s">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">son</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">sanoq soʻzi</span>
</div>

<h3>1. Asl koreys sonlari</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Raqam</th><th>고유어</th><th>Raqam</th><th>고유어</th></tr>
  <tr><td class="pk-res">1</td><td class="pk-stem">하나</td>
      <td class="pk-res">6</td><td class="pk-stem">여섯</td></tr>
  <tr><td class="pk-res">2</td><td class="pk-stem">둘</td>
      <td class="pk-res">7</td><td class="pk-stem">일곱</td></tr>
  <tr><td class="pk-res">3</td><td class="pk-stem">셋</td>
      <td class="pk-res">8</td><td class="pk-stem">여덟</td></tr>
  <tr><td class="pk-res">4</td><td class="pk-stem">넷</td>
      <td class="pk-res">9</td><td class="pk-stem">아홉</td></tr>
  <tr><td class="pk-res">5</td><td class="pk-stem">다섯</td>
      <td class="pk-res">10</td><td class="pk-stem">열</td></tr>
</table></div>

<p>Oʻnliklar: <b>스물</b> (20), <b>서른</b> (30), <b>마흔</b> (40), <b>쉰</b> (50),
<b>예순</b> (60), <b>일흔</b> (70), <b>여든</b> (80), <b>아흔</b> (90).</p>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
고유어 sonlar faqat <b>99 gacha</b> boradi. 100 dan boshlab har doim 한자어 ishlatiladi:
<b>백</b>, <b>천</b>. Ya'ni 100 ta narsani sanasangiz ham — 백 개.</div>

<h3>2. Toʻrtta son sanoq oldida qisqaradi</h3>

<p>Mana darsning eng muhim qoidasi. Sanoq soʻzi qoʻshilganda toʻrtta son
<b>shaklini oʻzgartiradi</b>:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Yolgʻiz</th><th>Sanoq oldida</th><th>Misol</th></tr>
  <tr><td class="pk-stem">하나</td><td class="pk-end">한</td>
      <td class="pk-res">한 개 — bitta</td></tr>
  <tr><td class="pk-stem">둘</td><td class="pk-end">두</td>
      <td class="pk-res">두 명 — ikki kishi</td></tr>
  <tr><td class="pk-stem">셋</td><td class="pk-end">세</td>
      <td class="pk-res">세 마리 — uchta hayvon</td></tr>
  <tr><td class="pk-stem">넷</td><td class="pk-end">네</td>
      <td class="pk-res">네 권 — toʻrtta kitob</td></tr>
  <tr><td class="pk-stem">스물</td><td class="pk-end">스무</td>
      <td class="pk-res">스무 살 — yigirma yosh</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Bu qoida <b>11, 12, 13, 14</b> ga ham tegishli: 열하나 → <b>열한</b> 개,
열둘 → <b>열두</b> 개, 열셋 → <b>열세</b> 개, 열넷 → <b>열네</b> 개. Qolgan sonlar
oʻzgarmaydi: 다섯 개, 여섯 개, 일곱 개.</div>

<h3>3. Sanoq soʻzlari</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Sanoq</th><th>Nima uchun</th><th>Misol</th></tr>
  <tr><td class="pk-stem">개</td><td class="pk-uz">umumiy narsalar</td>
      <td class="pk-res">사과 세 개 — uchta olma</td></tr>
  <tr><td class="pk-stem">명</td><td class="pk-uz">odamlar</td>
      <td class="pk-res">학생 두 명 — ikki oʻquvchi</td></tr>
  <tr><td class="pk-stem">분</td><td class="pk-uz">odamlar (hurmatli)</td>
      <td class="pk-res">선생님 한 분 — bir oʻqituvchi</td></tr>
  <tr><td class="pk-stem">마리</td><td class="pk-uz">hayvonlar</td>
      <td class="pk-res">고양이 네 마리 — toʻrtta mushuk</td></tr>
  <tr><td class="pk-stem">권</td><td class="pk-uz">kitoblar</td>
      <td class="pk-res">책 다섯 권 — beshta kitob</td></tr>
  <tr><td class="pk-stem">잔</td><td class="pk-uz">stakan, piyola</td>
      <td class="pk-res">커피 두 잔 — ikki piyola kofe</td></tr>
  <tr><td class="pk-stem">병</td><td class="pk-uz">shisha</td>
      <td class="pk-res">물 한 병 — bir shisha suv</td></tr>
  <tr><td class="pk-stem">살</td><td class="pk-uz">yosh</td>
      <td class="pk-res">열다섯 살 — oʻn besh yosh</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Sanoq soʻzi sizga <b>yangilik emas</b>. Oʻzbekchada ham shunday deymiz:
<br>• besh <b>dona</b> olma → 사과 다섯 <b>개</b>
<br>• uch <b>nafar</b> odam → 사람 세 <b>명</b>
<br>• ikki <b>bosh</b> qoramol → 소 두 <b>마리</b>
<br>Ingliz tilida esa bu tizim deyarli yoʻq (<em>three apples</em>), shuning uchun
ingliz tilidan oʻrganuvchi buni noldan tushunadi. Sizda esa <b>tushuncha tayyor</b> —
faqat soʻzlarni almashtirasiz.</div>

<h3>4. Soʻz tartibi — bu yerda farq bor</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Oʻzbekcha</p>
    <p>son → sanoq → <b>ot</b></p>
    <p><em>besh dona <b>olma</b></em></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Koreyscha</p>
    <p><b>ot</b> → son → sanoq</p>
    <p><b>사과</b> 다섯 개</p>
  </div>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Oʻzbekcha tartibda oʻylab, <s>다섯 개 사과</s> demang. Koreyschada <b>ot birinchi
keladi</b>: <b>사과 다섯 개</b>. Bu — darsdagi yagona joy, oʻzbek tili sizga
<em>xalaqit</em> beradi.</div>

<div class="pe-ex">
  <p class="pe-ex__ko">교실에 학생이 열 명 있어요.</p>
  <p class="pe-ex__uz">Sinfda oʻnta oʻquvchi bor.</p>
  <p class="pe-ex__why">Ot + 이/가, keyin son + sanoq, keyin kesim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 스무 살이에요.</p>
  <p class="pe-ex__uz">Men yigirma yoshdaman.</p>
  <p class="pe-ex__why">스물 → <b>스무</b> qisqargan.</p>
</div>

<h3>5. Qaysi tizim qachon — qisqacha</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>고유어 (하나, 둘…)</th><th>한자어 (일, 이…)</th></tr>
  <tr><td class="pk-stem">narsalar — 개</td><td class="pk-end">pul — 원</td></tr>
  <tr><td class="pk-stem">odamlar — 명 / 분</td><td class="pk-end">daqiqa — 분</td></tr>
  <tr><td class="pk-stem">hayvonlar — 마리</td><td class="pk-end">sana — 년 / 월 / 일</td></tr>
  <tr><td class="pk-stem">yosh — 살</td><td class="pk-end">qavat — 층</td></tr>
  <tr><td class="pk-stem">soat — 시</td><td class="pk-end">telefon — 번</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Diqqat qiling: <b>분</b> ikki joyda turibdi! 고유어 bilan — “kishi” (한 분), 한자어 bilan
— “daqiqa” (십 분). Bir xil yoziladi, lekin qaysi son turganiga qarab maʼnosi
oʻzgaradi. Buni kontekst hal qiladi.</div>

<h3>6. 몇 bilan savol</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 학생이 몇 명 있어요?<br>나: 열 명 있어요.</p>
  <p class="pe-ex__uz">A: Nechta oʻquvchi bor?<br>B: Oʻnta bor.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 몇 살이에요?<br>나: 열여섯 살이에요.</p>
  <p class="pe-ex__uz">A: Necha yoshdasiz?<br>B: Oʻn olti yoshdaman.</p>
  <p class="pe-ex__why">PK-11 da bu savolni koʻrgan edingiz — endi javob bera
     olasiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>다섯 개 사과</s></p>
  <p class="pe-good">Ot birinchi: <b>사과 다섯 개</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>하나 개</s>, <s>둘 명</s></p>
  <p class="pe-good">Sanoq oldida qisqaradi: <b>한 개</b>, <b>두 명</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>이십 살</s>이에요.</p>
  <p class="pe-good">Yosh — 고유어: <b>스무 살</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">사람 세 <s>마리</s></p>
  <p class="pe-good">Odam uchun <b>명</b>: 사람 세 <b>명</b>. 마리 — hayvonlar
     uchun.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     “Uchta olma” ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>사과 세 개.</strong> Ikki narsaga diqqat:
    <b>ot birinchi</b> (사과), va 셋 → <b>세</b> qisqargan.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Qaysi toʻrtta son sanoq oldida qisqaradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>하나 → 한, 둘 → 두, 셋 → 세, 넷 → 네</strong>
    (va 스물 → <b>스무</b>). Qoida 11–14 ga ham tegishli: 열한 개, 열두 개.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     “Men 20 yoshdaman” ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>저는 스무 살이에요.</strong> Yosh — 고유어 tizimi,
    va 스물 sanoq (살) oldida <b>스무</b> boʻlib qisqaradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Oʻzbek tilidagi qaysi soʻzlar koreys sanoq soʻzlariga oʻxshaydi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>dona, nafar, bosh</strong> — “besh <em>dona</em>
    olma”, “uch <em>nafar</em> odam”, “ikki <em>bosh</em> qoramol”. Tushuncha bir xil;
    faqat koreyschada <b>ot birinchi</b> keladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Dilnoza “고양이 네 명 있어요” dedi. Xatoni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>명 → 마리.</strong> 고양이 — mushuk, ya'ni
    hayvon, va hayvonlar uchun sanoq soʻzi <b>마리</b>. 명 faqat odamlar uchun.
    Toʻgʻrisi: <b>고양이 네 마리 있어요.</b></p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>하나, 둘, 셋, 넷, 다섯</b><span>1–5</span></li>
  <li><b>여섯, 일곱, 여덟, 아홉, 열</b><span>6–10</span></li>
  <li><b>스물 / 서른</b><span>20 / 30</span></li>
  <li><b>개</b><span>dona (narsalar)</span></li>
  <li><b>명 / 분</b><span>nafar (odamlar / hurmatli)</span></li>
  <li><b>마리</b><span>bosh (hayvonlar)</span></li>
  <li><b>권</b><span>ta (kitoblar)</span></li>
  <li><b>잔 / 병</b><span>piyola / shisha</span></li>
  <li><b>살</b><span>yosh</span></li>
  <li><b>사과 / 고양이</b><span>olma / mushuk</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>고유어 sonlar</b> — narsalar, odamlar, hayvonlar, yosh, soat uchun.</li>
    <li>Faqat <b>99 gacha</b>; 100 dan boshlab har doim 한자어.</li>
    <li>Sanoq oldida qisqaradi: <b>한, 두, 세, 네, 스무</b>.</li>
    <li>Tartib: <b>ot → son → sanoq</b> (사과 세 개), oʻzbekchadan teskari.</li>
    <li>Sanoq soʻzi oʻzbekchadagi <b>dona / nafar / bosh</b> bilan bir xil
        tushuncha.</li>
    <li>Yosh — <b>살</b>, hech qachon 한자어 bilan emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-25: Vaqt, sana va hafta kunlari",
        "category": "korean",
        "order": 25,
        "summary": (
            "Soat aytishda ikkala son tizimi bitta jumlada uchrashadi: soat — 고유어, "
            "daqiqa — 한자어. Va hafta kunlari beshta tabiat unsuridan yasalgan."
        ),
        "stories": ["몇 시에 학교에 가요?"],
        "content": """
<h2>PK-25: Vaqt, sana va hafta kunlari</h2>

<p>Ikkita son tizimini alohida oʻrgandingiz. Bugun ular <b>bitta jumlada
uchrashadi</b> — va aynan shu joy koreys tilining eng mashhur “tuzoqlaridan” biri:
soat 고유어 bilan, daqiqa esa 한자어 bilan aytiladi. Bir marta tushunsangiz, boshqa
adashmaysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Soatni toʻgʻri aytasiz — ikkala tizimni bir jumlada</li>
    <li>Sanani yozasiz va oʻqiysiz</li>
    <li>Hafta kunlarini beshta unsur orqali eslab qolasiz</li>
    <li>몇 시, 며칠, 무슨 요일 savollarini berasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Soat — ikki tizim birga</span>
  <span class="pe-chip pe-chip--v">고유어 + 시</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">한자어 + 분</span>
</div>

<h3>1. Soat: 고유어 + 시</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Soat</th><th>Koreyscha</th><th>Soat</th><th>Koreyscha</th></tr>
  <tr><td class="pk-res">1:00</td><td class="pk-stem">한 시</td>
      <td class="pk-res">7:00</td><td class="pk-stem">일곱 시</td></tr>
  <tr><td class="pk-res">2:00</td><td class="pk-stem">두 시</td>
      <td class="pk-res">8:00</td><td class="pk-stem">여덟 시</td></tr>
  <tr><td class="pk-res">3:00</td><td class="pk-stem">세 시</td>
      <td class="pk-res">9:00</td><td class="pk-stem">아홉 시</td></tr>
  <tr><td class="pk-res">4:00</td><td class="pk-stem">네 시</td>
      <td class="pk-res">10:00</td><td class="pk-stem">열 시</td></tr>
  <tr><td class="pk-res">5:00</td><td class="pk-stem">다섯 시</td>
      <td class="pk-res">11:00</td><td class="pk-stem">열한 시</td></tr>
  <tr><td class="pk-res">6:00</td><td class="pk-stem">여섯 시</td>
      <td class="pk-res">12:00</td><td class="pk-stem">열두 시</td></tr>
</table></div>

<p>Diqqat: <b>한 시, 두 시, 세 시, 네 시, 열한 시, 열두 시</b> — PK-24 dagi qisqarish
qoidasi shu yerda ishlaydi.</p>

<h3>2. Daqiqa: 한자어 + 분</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">세 시 삼십 분</p>
  <p class="pe-ex__uz">3:30 — soat uch yarim</p>
  <p class="pe-ex__why"><b>세</b> — 고유어 (soat), <b>삼십</b> — 한자어 (daqiqa).
     Bitta jumlada ikki tizim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아홉 시 십오 분</p>
  <p class="pe-ex__uz">9:15</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Eslash uchun oddiy fikr: <b>soat sanaladi, daqiqa oʻlchanadi</b>. Sanaladigan narsa —
고유어 (PK-24), oʻlchanadigan narsa — 한자어 (PK-23). Shuning uchun 시 birinchi
tizimni, 분 esa ikkinchisini oladi.</div>

<p><b>반</b> — “yarim”: 두 시 <b>반</b> = 2:30. Kundalik nutqda 삼십 분 dan koʻra
koʻproq ishlatiladi.</p>

<p><b>오전</b> — tushdan oldin, <b>오후</b> — tushdan keyin. Ular soatdan
<em>oldin</em> turadi: <b>오후 세 시</b>.</p>

<h3>3. Sana: hammasi 한자어</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">이천이십육년 팔월 이일</p>
  <p class="pe-ex__uz">2026-yil 2-avgust</p>
  <p class="pe-ex__why">Tartib: <b>yil → oy → kun</b>, kattadan kichikka.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Tartib oʻzbekcha bilan bir xil: <em>2026-yil 2-avgust</em> — avval yil, keyin oy, keyin
kun. Ingliz tilida esa teskari (<em>August 2, 2026</em>). Yana bir joyda oʻzbek tili
sizga yordam beradi.</div>

<h3>4. Oylar — va ikkita istisno</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Oy</th><th>Koreyscha</th><th>Oy</th><th>Koreyscha</th></tr>
  <tr><td class="pk-res">1</td><td class="pk-stem">일월</td>
      <td class="pk-res">7</td><td class="pk-stem">칠월</td></tr>
  <tr><td class="pk-res">2</td><td class="pk-stem">이월</td>
      <td class="pk-res">8</td><td class="pk-stem">팔월</td></tr>
  <tr><td class="pk-res">3</td><td class="pk-stem">삼월</td>
      <td class="pk-res">9</td><td class="pk-stem">구월</td></tr>
  <tr><td class="pk-res">4</td><td class="pk-stem">사월</td>
      <td class="pk-res">10</td><td class="pk-end">시월 ⚠</td></tr>
  <tr><td class="pk-res">5</td><td class="pk-stem">오월</td>
      <td class="pk-res">11</td><td class="pk-stem">십일월</td></tr>
  <tr><td class="pk-res">6</td><td class="pk-end">유월 ⚠</td>
      <td class="pk-res">12</td><td class="pk-stem">십이월</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Ikkita oy qoidadan chetga chiqadi:
<br>• 6-oy — <s>육월</s> emas, <b>유월</b> (ㄱ tushib qolgan)
<br>• 10-oy — <s>십월</s> emas, <b>시월</b> (ㅂ tushib qolgan)
<br>Sabab talaffuz qulayligi. Faqat shu ikkitasi — qolgani qoidaga boʻysunadi.</div>

<h3>5. Hafta kunlari — beshta unsur</h3>

<p>Koreys hafta kunlari <b>tabiat unsurlari</b> nomidan yasalgan. Bir marta koʻrsangiz,
yodlash osonlashadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Kun</th><th>Koreyscha</th><th>Belgi</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">Dushanba</td><td class="pk-stem">월요일</td>
      <td class="pk-end">월</td><td class="pk-uz">oy</td></tr>
  <tr><td class="pk-res">Seshanba</td><td class="pk-stem">화요일</td>
      <td class="pk-end">화</td><td class="pk-uz">olov</td></tr>
  <tr><td class="pk-res">Chorshanba</td><td class="pk-stem">수요일</td>
      <td class="pk-end">수</td><td class="pk-uz">suv</td></tr>
  <tr><td class="pk-res">Payshanba</td><td class="pk-stem">목요일</td>
      <td class="pk-end">목</td><td class="pk-uz">yogʻoch</td></tr>
  <tr><td class="pk-res">Juma</td><td class="pk-stem">금요일</td>
      <td class="pk-end">금</td><td class="pk-uz">metall, oltin</td></tr>
  <tr><td class="pk-res">Shanba</td><td class="pk-stem">토요일</td>
      <td class="pk-end">토</td><td class="pk-uz">tuproq</td></tr>
  <tr><td class="pk-res">Yakshanba</td><td class="pk-stem">일요일</td>
      <td class="pk-end">일</td><td class="pk-uz">quyosh</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Qiziq taqqoslash: oʻzbek hafta kunlari <b>sanoqqa</b> qurilgan — <em>dushanba</em>
(ikkinchi), <em>seshanba</em> (uchinchi), <em>chorshanba</em> (toʻrtinchi). Koreys
kunlari esa <b>unsurlarga</b> qurilgan: oy, olov, suv, yogʻoch, metall, tuproq, quyosh.
Ikkala tizim ham mantiqiy — faqat mantiqi boshqa. Ingliz kunlari esa qadimgi xudolar
nomidan va hech qanday tartibi yoʻq.</div>

<h3>6. Savollar</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Savol</th><th>Maʼnosi</th><th>Javob namunasi</th></tr>
  <tr><td class="pk-stem">몇 시예요?</td><td class="pk-uz">Soat necha?</td>
      <td class="pk-res">세 시예요.</td></tr>
  <tr><td class="pk-stem">며칠이에요?</td><td class="pk-uz">Nechanchi sana?</td>
      <td class="pk-res">팔월 이일이에요.</td></tr>
  <tr><td class="pk-stem">무슨 요일이에요?</td><td class="pk-uz">Hafta kuni qaysi?</td>
      <td class="pk-res">월요일이에요.</td></tr>
  <tr><td class="pk-stem">몇 살이에요?</td><td class="pk-uz">Necha yoshdasiz?</td>
      <td class="pk-res">열여섯 살이에요.</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 여덟 시에 학교에 가요.</p>
  <p class="pe-ex__uz">Men soat sakkizda maktabga boraman.</p>
  <p class="pe-ex__why">Vaqt + <b>에</b> (PK-14). Diqqat: 오늘, 어제, 내일 esa 에
     olmaydi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>삼 시 삼십 분</s></p>
  <p class="pe-good">Soat — 고유어: <b>세 시</b> 삼십 분.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">두 시 <s>서른 분</s></p>
  <p class="pe-good">Daqiqa — 한자어: 두 시 <b>삼십 분</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>육월</s>, <s>십월</s></p>
  <p class="pe-good"><b>유월</b> (6-oy), <b>시월</b> (10-oy).</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">여덟 시<s>에서</s> 학교에 가요.</p>
  <p class="pe-good">Vaqt uchun <b>에</b>: 여덟 시<b>에</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>3:30</b> ni koreyschada ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>세 시 삼십 분</strong> (yoki <b>세 시 반</b>).
    Soat — 고유어 (세), daqiqa — 한자어 (삼십). Ikki tizim bitta jumlada.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Nega soat 고유어, daqiqa esa 한자어 bilan aytiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Oddiy fikr: <strong>soat sanaladi, daqiqa
    oʻlchanadi</strong>. Sanaladigan narsalar 고유어 tizimini oladi (PK-24),
    oʻlchanadigan narsalar esa 한자어 ni (PK-23).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     6-oy va 10-oy qanday yoziladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>유월</strong> va <strong>시월</strong>.
    <s>육월</s> va <s>십월</s> notoʻgʻri — talaffuz qulayligi uchun bitta undosh tushib
    qolgan. Faqat shu ikkita oy istisno.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>수요일</b> qaysi kun va nega shunday atalgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Chorshanba.</strong> <b>수</b> — “suv”. Koreys
    hafta kunlari beshta unsur va ikki yoritqichdan yasalgan: oy, olov, suv, yogʻoch,
    metall, tuproq, quyosh.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Sherbek “저는 여덟 시에 학교에 가요” dedi. Toʻgʻrimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Toʻliq toʻgʻri.</strong> Uchta narsa joyida:
    soat 고유어 bilan (<b>여덟 시</b>), vaqt <b>에</b> oladi (PK-14), va 가다 yoʻnalish
    bildirgani uchun 학교<b>에</b>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>시 / 분</b><span>soat / daqiqa</span></li>
  <li><b>반</b><span>yarim</span></li>
  <li><b>오전 / 오후</b><span>tushdan oldin / keyin</span></li>
  <li><b>년 / 월 / 일</b><span>yil / oy / kun</span></li>
  <li><b>유월 / 시월</b><span>6-oy / 10-oy (istisno)</span></li>
  <li><b>요일</b><span>hafta kuni</span></li>
  <li><b>월요일 / 금요일</b><span>dushanba / juma</span></li>
  <li><b>주말 / 평일</b><span>dam olish kuni / ish kuni</span></li>
  <li><b>며칠</b><span>nechanchi sana</span></li>
  <li><b>무슨 요일</b><span>qaysi hafta kuni</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>Soat — 고유어 + 시</b>, <b>daqiqa — 한자어 + 분</b>. Bitta jumlada ikki
        tizim.</li>
    <li>Eslash: <b>soat sanaladi, daqiqa oʻlchanadi</b>.</li>
    <li>한 시, 두 시, 세 시, 네 시 — qisqarish qoidasi (PK-24).</li>
    <li>Sana hammasi 한자어, tartib <b>yil → oy → kun</b> — oʻzbekcha kabi.</li>
    <li>Istisnolar: <b>유월</b> (6), <b>시월</b> (10).</li>
    <li>Hafta kunlari — <b>beshta unsur</b>: 월·화·수·목·금·토·일.</li>
    <li>Vaqt <b>에</b> oladi, lekin 오늘 / 어제 / 내일 olmaydi.</li>
  </ul>
</div>
""",
    },
]
