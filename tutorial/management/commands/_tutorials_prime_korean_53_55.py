# -*- coding: utf-8 -*-
"""Prime Korean — Block E boshi, darslar 53–55.

53. (으)ㄹ 줄 알다/모르다 — usulni bilish va bilmaslik
54. 기로 하다 — qaror va vaʼda
55. 잖아요 — "axir bilasiz-ku"

Uchalasida ham kuchli oʻzbekcha juftlik bor:
  (으)ㄹ 줄 알다 = "suza BILAMAN"  ·  (으)ㄹ 수 있다 = "suza OLAMAN"
  기로 하다      = "-ishga qaror qildim"
  잖아요         = "-ku / -da / axir"

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_53_55.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_53_55.py --author=prime
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
        "title": "PK-53: (으)ㄹ 줄 알다/모르다 — usulni bilish va bilmaslik",
        "category": "korean",
        "order": 53,
        "summary": (
            "“Suza bilaman” va “suza olaman” — oʻzbek tilida ham ikki xil gap. "
            "Koreys tili bu farqni aynan shunday ajratadi."
        ),
        "stories": ["김치를 만들 줄 알아요?"],
        "content": """
<h2>PK-53: (으)ㄹ 줄 알다/모르다 — usulni bilish va bilmaslik</h2>

<p>Bir daqiqa oʻzbekcha oʻylab koʻring: “Men suza <b>bilaman</b>” va “Men suza
<b>olaman</b>” — bu bir xil gapmi? Yoʻq. Birinchisi <em>koʻnikma</em> haqida:
oʻrganganman, qoʻlimdan keladi. Ikkinchisi <em>imkoniyat</em> haqida: hozir
sharoit bor, sogʻman, suv ham bor. Koreys tili ham bu ikkisini ikkita boshqa
qolip bilan ajratadi — va siz ulardan birini allaqachon bilasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ 줄 알다</b> bilan koʻnikma haqida gapirasiz</li>
    <li><b>(으)ㄹ 줄 모르다</b> bilan “qoʻlimdan kelmaydi” deysiz</li>
    <li>Uni <b>(으)ㄹ 수 있다</b> (PK-30) dan ajratasiz</li>
    <li>Ikkinchi maʼnosini — “men shunday deb <em>oʻylagandim</em>” — koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ 줄</span>
  <span class="pe-chip pe-chip--v">알다 / 모르다</span>
  <span class="pe-chip pe-chip--adv">= …a bilaman / bilmayman</span>
</div>

<h3>1. 줄 — bu yana bitta ot</h3>

<p>Tanish tuzilish: <b>aniqlovchi + ot</b>. <b>줄</b> — “usul, yoʻl” degan
soʻz. Yaʼni 수영할 줄 알아요 soʻzma-soʻz “suzish <em>usulini</em> bilaman”
degani. PK-44 dagi 후, PK-46 dagi 것, PK-52 dagi 것 — hammasi shu mashinaning
qismlari edi.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄹ 줄 알다</span></p>
    <p>하다 → 할 줄 알아요</p>
    <p>타다 → 탈 줄 알아요</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">을 줄 알다</span></p>
    <p>먹다 → 먹을 줄 알아요</p>
    <p>읽다 → 읽을 줄 알아요</p>
  </div>
</div>

<p><b>ㄹ</b> oʻzaklar bitta ㄹ boʻlib qoladi: 만들다 → <b>만들 줄</b> 알아요.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 <span class="pe-hl pe-hl--v">수영할 줄 알아요</span>.</p>
  <p class="pe-ex__uz">Men suza bilaman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 김치를 <span class="pe-hl pe-hl--neg">만들 줄
     몰라요</span>.</p>
  <p class="pe-ex__uz">Men kimchi tayyorlashni bilmayman.</p>
  <p class="pe-ex__why">Inkori 안 emas — <b>모르다</b> (PK-47).</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu darsning eng katta sovgʻasi.</b> Oʻzbek tilida ham aynan shu ikki
  yoʻl bor:<br>
  “suza <b>bilaman</b>” — koʻnikma → <b>수영할 줄 알아요</b><br>
  “suza <b>olaman</b>” — imkoniyat → <b>수영할 수 있어요</b><br>
  Yaʼni oʻzbek tili bu farqni <em>allaqachon</em> ajratadi, va siz uni
  oʻylamasdan toʻgʻri ishlatasiz. Ingliz tilida esa ikkalasi ham “can” —
  shuning uchun ingliz tilidan oʻrganayotgan odam bu darsni qiyin deb topadi.
  Siz uchun esa faqat shakl yangi, fikr emas.</p>
</div>

<h3>2. (으)ㄹ 줄 알다 va (으)ㄹ 수 있다 — farqi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)ㄹ 줄 알다</p>
    <p><b>Koʻnikma</b> — oʻrgangansiz, qoʻlingizdan keladi.</p>
    <p>Vaqt oʻtishi bilan yoʻqolmaydi.</p>
    <p><small>운전할 줄 알아요 — haydashni bilaman.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)ㄹ 수 있다</p>
    <p><b>Imkoniyat</b> — hozir sharoit bor.</p>
    <p>Vaziyatga qarab oʻzgaradi.</p>
    <p><small>운전할 수 있어요 — hozir hayday olaman.</small></p>
  </div>
</div>

<p>Farqni eng yaxshi koʻrsatadigan gap — ikkalasi bitta jumlada:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 <span class="pe-hl pe-hl--v">수영할 줄 알아요</span>.
     하지만 오늘은 팔이 아파서 <span class="pe-hl pe-hl--neg">수영할 수
     없어요</span>.</p>
  <p class="pe-ex__uz">Men suza bilaman. Lekin bugun qoʻlim ogʻrigani uchun
  suza olmayman.</p>
  <p class="pe-ex__why">Koʻnikma joyida, imkoniyat esa yoʻq.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Tekshirish savoli:</b> <em>bu oʻrganiladigan narsami?</em>
  Suzish, haydash, ovqat pishirish, chalish — ha → <b>줄 알다</b>.
  “Ertaga kela olaman”, “bu yerda ovqat yeya olamiz” — bu koʻnikma emas,
  sharoit → <b>수 있다</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Nega inkori 모르다?</b> Chunki qolipning oʻzagi — <b>알다</b>, yaʼni
  “bilmoq”. Oʻzbekchada ham shunday: “suza <em>bilaman</em>” ning inkori
  “suza <em>bilmayman</em>” — biz ham “bilmoq” feʼlini inkor qilamiz.
  Koreys tilida esa 알다 ning inkori alohida soʻz — <b>모르다</b> (PK-47).
  Yaʼni mantiq bir xil, faqat koreyschada inkor uchun boshqa soʻz bor.</p>
</div>

<h3>3. Faqat oʻrganiladigan ishlar bilan</h3>

<p>Shuning uchun bu qolip maʼlum feʼllar bilan tabiiy eshitiladi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">운전할 줄 알다</p>
    <p>mashina haydashni bilmoq</p></div>
  <div class="pe-card"><p class="pe-card__h">수영할 줄 알다</p>
    <p>suza bilmoq</p></div>
  <div class="pe-card"><p class="pe-card__h">피아노를 칠 줄 알다</p>
    <p>pianino chala bilmoq</p></div>
  <div class="pe-card"><p class="pe-card__h">한국어를 할 줄 알다</p>
    <p>koreyscha gapira bilmoq</p></div>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>내일 올 줄 알아요 (“ertaga kela olaman” maʼnosida)</s></p>
  <p class="pe-good">내일 <b>올 수 있어요</b>.</p>
  <p><small>“Kelish” — oʻrganiladigan koʻnikma emas, sharoit masalasi.</small></p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu qolip ham aniqlovchi + ot ekanini unutmang.</b> PK-44 da 후 (“keyin”),
  PK-46 da 것 (“narsa”), PK-52 da yana 것, bugun esa <b>줄</b> (“usul”).
  Toʻrt darsda bitta mashina ishlayapti: <em>aniqlovchi + ot + feʼl</em>.
  Oʻzbekchada ham shunday tuzilishlar bor — “borish <b>yoʻli</b>ni bilaman”,
  “kelgan<b>dan keyin</b>”. Yangi qolip koʻrsangiz, avval uni shu uchtaga
  ajratib koʻring: koʻpincha yangi narsa faqat oʻrtadagi ot boʻlib chiqadi.</p>
</div>

<h3>4. Ikkinchi maʼnosi: “shunday deb oʻylagandim”</h3>

<p><b>줄 알다</b> oʻtgan zamonda butunlay boshqa maʼno beradi:
<em>notoʻgʻri taxmin</em>. Yaʼni “men shunday deb oʻylagandim — lekin
unday emas ekan”.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">비가 <span class="pe-hl pe-hl--v">올 줄 알았어요</span>.
     그런데 안 왔어요.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻadi deb oʻylagandim. Lekin yogʻmadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시험이 <span class="pe-hl pe-hl--adv">쉬울 줄
     알았어요</span>.</p>
  <p class="pe-ex__uz">Imtihon oson boʻladi deb oʻylagandim.</p>
</div>

<div class="pe-call pe-tip">
  <p>Ikki maʼnoni ajratish oson: <b>hozirgi zamonda</b> (알아요) — koʻnikma.
  <b>Oʻtgan zamonda</b> (알았어요) — koʻpincha notoʻgʻri taxmin. Kontekst
  qolganini aytadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>저는 수영할 줄 안 알아요.</s></p>
  <p class="pe-good">저는 <b>수영할 줄 몰라요</b>.</p>
  <p><small>Inkori — <b>모르다</b>. PK-47 dagi 알다/모르다 juftligi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>김치를 만들을 줄 알아요.</s></p>
  <p class="pe-good">김치를 <b>만들 줄</b> 알아요.</p>
  <p><small>ㄹ oʻzak bitta ㄹ boʻlib qoladi: 만들 + ㄹ → 만들.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>먹을 줄 알아요? (“hozir yeya olasizmi?” maʼnosida)</s></p>
  <p class="pe-good"><b>먹을 수 있어요?</b></p>
  <p><small>Sharoit haqida soʻrayotgan boʻlsangiz — 수 있다.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>피아노를 치를 줄 알아요.</s></p>
  <p class="pe-good">피아노를 <b>칠 줄</b> 알아요.</p>
  <p><small>치다 → 치 + ㄹ → <b>칠</b>. Oʻzakni toʻgʻri ajrating.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 저는 <span class="pe-blank"></span>
  (운전하다) 줄 알아요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>운전할</b> — 하 da 받침 yoʻq → ㄹ 줄: 운전할 줄 알아요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 김치를 <span class="pe-blank"></span>
  (만들다) 줄 몰라요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>만들</b> — ㄹ oʻzak bitta ㄹ boʻlib qoladi. <s>만들을</s> emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Qaysi biri toʻgʻri va nega?
  “Bugun qoʻlim ogʻriyapti, shuning uchun suza olmayman.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>수영할 수 없어요</b> — bu <em>imkoniyat</em> masalasi. Koʻnikma
    joyida turibdi (수영할 줄 알아요), faqat bugun sharoit yoʻq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Bu gap nima degani?
  시험이 쉬울 줄 알았어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>“Imtihon oson boʻladi deb oʻylagandim.”</b> Oʻtgan zamonda
    줄 알다 notoʻgʻri taxminni bildiradi — demak imtihon aslida oson
    boʻlmagan.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>저는 한국어를 할 줄 안 알아요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>저는 한국어를 할 줄 몰라요.</b> Inkori 안 알다 emas,
    <b>모르다</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Oʻzbekchaga oʻgiring va farqini ayting:
  수영할 줄 알아요 / 수영할 수 있어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>“Suza bilaman”</b> (koʻnikma) va <b>“suza olaman”</b> (imkoniyat).
    Oʻzbek tili bu farqni aynan koreyschadek ajratadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ 줄 알다</b> — …a bilmoq (koʻnikma)</li>
  <li><b>(으)ㄹ 줄 모르다</b> — …a bilmaslik</li>
  <li><b>줄</b> — usul, yoʻl</li>
  <li><b>수영하다</b> — suzmoq</li>
  <li><b>운전하다</b> — mashina haydamoq</li>
  <li><b>치다</b> — chalmoq; urmoq</li>
  <li><b>피아노</b> — pianino</li>
  <li><b>팔</b> — qoʻl</li>
  <li><b>타다</b> — minmoq</li>
  <li><b>그런데</b> — lekin, ammo</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ 줄 알다</b> = koʻnikma. <b>줄</b> — “usul” degan ot.</li>
    <li>받침 yoʻq → ㄹ 줄 · 받침 bor → 을 줄 · ㄹ oʻzak → bitta ㄹ (만들 줄).</li>
    <li>Inkori — <b>모르다</b>, 안 알다 emas.</li>
    <li><b>줄 알다</b> (koʻnikma) va <b>수 있다</b> (imkoniyat) — aralashtirmang.</li>
    <li>Oʻzbekcha juftligi: “suza <b>bilaman</b>” va “suza <b>olaman</b>”.</li>
    <li>Oʻtgan zamonda: <b>줄 알았어요</b> — “shunday deb oʻylagandim”
      (lekin unday emas ekan).</li>
    <li>Faqat oʻrganiladigan ishlar bilan tabiiy: 운전, 수영, 피아노, 한국어.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-54: 기로 하다 — qaror va vaʼda",
        "category": "korean",
        "order": 54,
        "summary": (
            "“…ishga qaror qildim.” Niyat emas, qaror. PK-40 dagi (으)려고 하다 dan "
            "qanday farq qilishi va nega deyarli har doim oʻtgan zamonda kelishi."
        ),
        "stories": ["우리 같이 여행하기로 했어요"],
        "content": """
<h2>PK-54: 기로 하다 — qaror va vaʼda</h2>

<p>PK-40 da siz <b>(으)려고 하다</b> ni oʻrgandingiz — “…moqchiman”, yaʼni
koʻngildagi niyat. Lekin niyat bilan <em>qaror</em> bir xil emas.
“Bormoqchiman” — hali oʻzgarishi mumkin. “Borishga <b>qaror qildim</b>” —
masala hal. Koreys tilida bu ikkinchisining nomi — <b>기로 하다</b>. Va u
deyarli har doim <em>oʻtgan zamonda</em> keladi, chunki qaror allaqachon
qabul qilingan.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>기로 하다</b> bilan qaror haqida gapirasiz</li>
    <li>Nega u koʻpincha <b>기로 했어요</b> shaklida kelishini bilib olasiz</li>
    <li>Uni <b>(으)려고 하다</b> va <b>(으)ㄹ 거예요</b> dan ajratasiz</li>
    <li>Inkor shaklini — “…maslikka qaror qildim” — oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--v">기로</span>
  <span class="pe-chip pe-chip--v">하다</span>
  <span class="pe-chip pe-chip--adv">= …ishga qaror qildim</span>
</div>

<h3>1. Yasalishi — ayri yoʻq</h3>

<p>PK-46 dagi otlashtiruvchi <b>기</b> yana ishga tushadi. 기 undosh bilan
boshlanadi, demak 받침 ayrisi ham, notoʻgʻri feʼl oʻzgarishi ham yoʻq.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>가다</td><td class="pk-stem">가</td>
      <td class="pk-res">가기로 했어요</td><td class="pk-uz">borishga qaror qildim</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹</td>
      <td class="pk-res">먹기로 했어요</td><td class="pk-uz">yeyishga qaror qildim</td></tr>
  <tr><td>듣다</td><td class="pk-stem">듣</td>
      <td class="pk-res">듣기로 했어요</td><td class="pk-uz">tinglashga qaror qildim</td></tr>
  <tr><td>만들다</td><td class="pk-stem">만들</td>
      <td class="pk-res">만들기로 했어요</td><td class="pk-uz">tayyorlashga qaror qildim</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 내년에 한국에 <span class="pe-hl pe-hl--v">가기로
     했어요</span>.</p>
  <p class="pe-ex__uz">Men keyingi yil Koreyaga borishga qaror qildim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha tuzilishi bilan solishtiring.</b> “Bor<em>ish</em><b>ga</b>
  qaror qildim” — bu uch boʻlak: feʼlning ot shakli (“borish”), qoʻshimcha
  (“-ga”) va feʼl (“qaror qildim”). Koreyschada ham aynan uchta:
  가<b>기</b> + <b>로</b> + <b>했어요</b>. <b>기</b> — “-ish”, <b>로</b> —
  yoʻnalish qoʻshimchasi (“-ga”), <b>하다</b> — feʼl. Yaʼni bu qolip
  oʻzbekchadan soʻzma-soʻz koʻchirilgandek. Uni bir boʻlak sifatida
  yodlash oʻrniga shu uchtaga boʻlib koʻring — keyin unutmaysiz.</p>
</div>

<h3>2. Nega deyarli har doim 했어요?</h3>

<p>Chunki qaror — <em>allaqachon qabul qilingan</em> narsa. Siz gapirayotgan
paytda u oʻtmishda qolgan, natijasi esa kelajakka tegishli:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">우리는 <span class="pe-hl pe-hl--adv">주말에</span>
     같이 영화를 <span class="pe-hl pe-hl--v">보기로 했어요</span>.</p>
  <p class="pe-ex__uz">Biz dam olish kunida birga kino koʻrishga kelishdik.</p>
  <p class="pe-ex__why">Qaror kecha qabul qilingan, kino esa hali koʻrilmagan.</p>
</div>

<div class="pe-call pe-tip">
  <p>Bir necha odam birga qaror qilsa, oʻzbekchaga “<b>kelishdik</b>”,
  “<b>ahdlashdik</b>” deb tarjima qilinadi. Yolgʻiz oʻzingiz qaror qilsangiz —
  “<b>qaror qildim</b>”. Koreyschada shakl bir xil, farqni ega koʻrsatadi.</p>
</div>

<h3>3. 기로 해요 — taklif</h3>

<p>Hozirgi zamonda esa bu qolip <b>taklif</b> boʻlib chiqadi: “kelishaylik”.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그럼 내일 아침에 <span class="pe-hl pe-hl--v">만나기로
     해요</span>.</p>
  <p class="pe-ex__uz">Unda ertaga ertalab uchrashishga kelishaylik.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Inkor qayerda turishini oʻzbekcha bilan tekshiring.</b>
  “Qahva <em>ichmaslikka</em> qaror qildim” — inkor <b>“ichmaslik”</b> ichida,
  “qaror qildim” esa toza. Agar inkorni oxiriga koʻchirsangiz — “qahva
  ichishga qaror <em>qilmadim</em>” — maʼno butunlay oʻzgaradi. Koreyschada
  ham aynan shunday: <b>안 마시기로</b> 했어요 va <b>마시기로 안</b> 했어요 —
  ikki xil gap. Oʻzbekcha jumlangizda inkor qayerda tursa, koreyschada ham
  oʻsha yerda turadi.</p>
</div>

<h3>4. Inkor: “…maslikka qaror qildim”</h3>

<p>Inkor <b>기</b> dan oldin qoʻyiladi — yaʼni feʼlning oʻziga:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 커피를 <span class="pe-hl pe-hl--neg">안
     마시기로 했어요</span>.</p>
  <p class="pe-ex__uz">Men qahva ichmaslikka qaror qildim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">담배를 <span class="pe-hl pe-hl--neg">피우지 않기로
     했어요</span>.</p>
  <p class="pe-ex__uz">Chekmaslikka qaror qildim.</p>
  <p class="pe-ex__why">지 않다 (PK-21) shakli ham ishlaydi va biroz
  rasmiyroq eshitiladi.</p>
</div>

<h3>5. Uchta “kelajak” qolipi — bitta jadval</h3>

<p>Endi sizda kelajak haqida gapirishning uch yoʻli bor. Ular bir-biridan
<b>qatʼiylik darajasi</b> bilan farq qiladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Maʼnosi</th><th>Qatʼiylik</th><th>Misol</th></tr>
  <tr><td class="pk-res">(으)려고 하다</td><td class="pk-uz">niyat</td>
      <td class="pk-uz">past — oʻzgarishi mumkin</td><td>가려고 해요</td></tr>
  <tr><td class="pk-res">(으)ㄹ 거예요</td><td class="pk-uz">reja / kelasi zamon</td>
      <td class="pk-uz">oʻrtacha</td><td>갈 거예요</td></tr>
  <tr><td class="pk-res">기로 하다</td><td class="pk-uz">qaror, vaʼda</td>
      <td class="pk-res">yuqori — masala hal</td><td>가기로 했어요</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham uchtasi bor.</b> “Bor<em>moqchiman</em>” (niyat) ·
  “Bor<em>aman</em>” (reja) · “Bor<em>ishga qaror qildim</em>” (qaror).
  Siz bu uch darajani ona tilingizda oʻylamasdan tanlaysiz. Koreyschada ham
  xuddi shu uchta daraja bor, shuning uchun tarjima qilayotganda oʻzbekcha
  jumlangizga qarang — u sizga qaysi qolip kerakligini oʻzi aytadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>한국에 갈기로 했어요.</s></p>
  <p class="pe-good">한국에 <b>가기로</b> 했어요.</p>
  <p><small>Aniqlovchi emas, <b>기</b> qoʻshiladi: 가 + 기로.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>음악을 들기로 했어요.</s></p>
  <p class="pe-good">음악을 <b>듣기로</b> 했어요.</p>
  <p><small>기 undosh, shuning uchun 듣 <b>oʻzgarmaydi</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>커피를 마시기로 안 했어요 (“ichmaslikka qaror qildim”
  maʼnosida)</s></p>
  <p class="pe-good">커피를 <b>안 마시기로</b> 했어요.</p>
  <p><small>Inkor <b>기 dan oldin</b> turadi. 마시기로 안 했어요 — “qaror
  qilmadim” degan boshqa maʼno.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>내일 만나기로 했어요 (“ertaga uchrashmoqchiman”
  maʼnosida)</s></p>
  <p class="pe-good">내일 <b>만나려고 해요</b>.</p>
  <p><small>Hali qaror qilinmagan boʻlsa — (으)려고 하다 (PK-40).</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 내년에 한국에
  <span class="pe-blank"></span> (가다) 했어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>가기로</b> — oʻzakka 기로 qoʻshiladi: 가기로 했어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 매일 한국 노래를
  <span class="pe-blank"></span> (듣다) 했어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>듣기로</b> — 기 undosh bilan boshlanadi, shuning uchun 듣
    oʻzgarmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Koreyschaga oʻgiring: “Qahva
  ichmaslikka qaror qildim.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>커피를 안 마시기로 했어요.</b> Inkor 기 dan <em>oldin</em> turadi.
    (피우지 않기로 했어요 shakli ham toʻgʻri.)</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Farqini ayting: 가려고 해요 va
  가기로 했어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>가려고 해요</b> — “bormoqchiman” (niyat, oʻzgarishi mumkin).
    <b>가기로 했어요</b> — “borishga qaror qildim” (masala hal).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Nega bu qolip koʻpincha
  <b>했어요</b> shaklida keladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Chunki <b>qaror allaqachon qabul qilingan</b> — u oʻtmishda.
    Ishning oʻzi esa hali bajarilmagan, kelajakka tegishli.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Bu gap nima degani?
  그럼 내일 아침에 만나기로 해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>“Unda ertaga ertalab uchrashishga kelishaylik.”</b> Hozirgi
    zamonda bu qolip <em>taklif</em> boʻlib chiqadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>기로 하다</b> — …ishga qaror qilmoq</li>
  <li><b>기로 했어요</b> — qaror qildim / kelishdik</li>
  <li><b>기로 해요</b> — kelishaylik (taklif)</li>
  <li><b>여행하다</b> — sayohat qilmoq</li>
  <li><b>내년</b> — keyingi yil</li>
  <li><b>담배를 피우다</b> — chekmoq</li>
  <li><b>약속</b> — vaʼda, uchrashuv</li>
  <li><b>정하다</b> — belgilamoq</li>
  <li><b>같이</b> — birga</li>
  <li><b>주말</b> — dam olish kunlari</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>기로 하다</b> = “…ishga qaror qilmoq”. Oʻzak + 기로 + 하다.</li>
    <li>기 undosh, shuning uchun ayri ham, notoʻgʻri oʻzgarish ham yoʻq:
      듣기로.</li>
    <li>Deyarli har doim <b>기로 했어요</b> — qaror oʻtmishda qabul qilingan.</li>
    <li>Hozirgi zamonda <b>기로 해요</b> — taklif, “kelishaylik”.</li>
    <li>Inkor <b>기 dan oldin</b>: 안 마시기로 했어요 / 피우지 않기로 했어요.</li>
    <li>Qatʼiylik darajasi: (으)려고 하다 &lt; (으)ㄹ 거예요 &lt; 기로 하다.</li>
    <li>Oʻzbekcha tuzilishi bir xil: 기 (“-ish”) + 로 (“-ga”) + 하다.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-55: 잖아요 — “axir bilasiz-ku”",
        "category": "korean",
        "order": 55,
        "summary": (
            "Oʻzbekcha “-ku” va “-da” ning koreyschadagi juftligi. Suhbatni "
            "tirik qiladigan qoʻshimcha — va uni qachon ishlatmaslik kerakligi."
        ),
        "stories": ["제가 어제 말했잖아요"],
        "content": """
<h2>PK-55: 잖아요 — “axir bilasiz-ku”</h2>

<p>Doʻstingiz sizdan soʻradi: “Nega bugun soyabon olding?” Siz javob berasiz:
“Axir yomgʻir yogʻyapti-<b>ku</b>!” Oʻzbekchadagi shu “<b>-ku</b>” —
suhbatdoshingiz <em>allaqachon biladigan</em> narsani eslatish uchun. Koreys
tilida uning aniq juftligi bor: <b>잖아요</b>. Bu qoʻshimcha darsliklarda kam
uchraydi, lekin koreyslar uni kuniga oʻnlab marta ishlatadi — shuning uchun uni
bilmasangiz, tirik nutqni tushunish qiyin boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>잖아요</b> ni yasashni oʻrganasiz — eng oson qoʻshimchalardan biri</li>
    <li>Uning uchta vazifasini koʻrasiz</li>
    <li>Oʻzbekcha “-ku” va “-da” bilan solishtirasiz</li>
    <li><b>Uni qachon ishlatmaslik</b> kerakligini bilib olasiz — bu muhim</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Oʻzak</span>
  <span class="pe-chip pe-chip--v">잖아요</span>
  <span class="pe-chip pe-chip--adv">= …-ku, …-da, axir …</span>
</div>

<h3>1. Yasalishi — ayri ham, oʻzgarish ham yoʻq</h3>

<p>Bu — kursdagi eng oson qoʻshimchalardan biri. Oʻzakka shundoq qoʻshiladi:
받침 ahamiyatsiz, notoʻgʻri feʼllar ham tinch turadi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Soʻz</th><th>Oʻzak</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>가다</td><td class="pk-stem">가</td>
      <td class="pk-res">가잖아요</td><td class="pk-uz">boradi-ku</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹</td>
      <td class="pk-res">먹잖아요</td><td class="pk-uz">yeydi-ku</td></tr>
  <tr><td>듣다</td><td class="pk-stem">듣</td>
      <td class="pk-res">듣잖아요</td><td class="pk-uz">tinglaydi-ku</td></tr>
  <tr><td>좋다</td><td class="pk-stem">좋</td>
      <td class="pk-res">좋잖아요</td><td class="pk-uz">yaxshi-ku</td></tr>
  <tr><td>덥다</td><td class="pk-stem">덥</td>
      <td class="pk-res">덥잖아요</td><td class="pk-uz">issiq-ku</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Uchinchi va beshinchi qatorga qarang: <b>듣잖아요</b>, <b>덥잖아요</b> —
  hech nima oʻzgarmadi. 잖 undosh bilan boshlanadi. PK-32 dan beri
  takrorlanayotgan qoida yana ishlayapti.</p>
</div>

<p>Oʻtgan zamon oddiy qoʻshiladi: 먹<b>었</b>잖아요, 갔잖아요, 말했잖아요.</p>

<h3>2. Birinchi vazifasi: eslatish</h3>

<p>Suhbatdoshingiz biladigan (yoki bilishi kerak boʻlgan) narsani eslatasiz:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">제가 어제 <span class="pe-hl pe-hl--v">말했잖아요</span>.</p>
  <p class="pe-ex__uz">Axir men kecha aytdim-ku.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">오늘 일요일<span class="pe-hl pe-hl--v">이잖아요</span>.
     학교에 안 가요.</p>
  <p class="pe-ex__uz">Bugun yakshanba-ku. Maktabga bormaymiz.</p>
  <p class="pe-ex__why">Ot bilan <b>이잖아요</b> boʻladi — lekin ayrisi bor,
  quyida qarang.</p>
</div>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">ot + <span class="pk-par">이잖아요</span></p>
    <p>학생<b>이</b>잖아요 · 일요일<b>이</b>잖아요</p>
    <p>이 saqlanadi.</p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">ot + <span class="pk-par">잖아요</span></p>
    <p>친구잖아요 · 의사잖아요</p>
    <p>이 <b>tushadi</b>.</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p>Bu ayri sizga tanish — PK-10 dagi <b>이에요 / 예요</b> qoidasining
  aynan oʻzi. 이다 qayerda kelsa, shu qoida ishlaydi.</p>
</div>

<h3>3. Ikkinchi vazifasi: sababni koʻrsatish</h3>

<p>Nima uchundir soʻralganda, javobni 잖아요 bilan berish juda tabiiy:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">— 왜 우산을 가져왔어요?<br>
     — 비가 <span class="pe-hl pe-hl--v">오잖아요</span>.</p>
  <p class="pe-ex__uz">— Nega soyabon olib keldingiz?<br>
     — Axir yomgʻir yogʻyapti-ku.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Diqqat: 잖아요 sabab bogʻlovchisi EMAS.</b> “Axir yomgʻir yogʻyapti-ku”
  gapida sabab bor, lekin uni <em>bogʻlovchi</em> emas, <b>ohang</b>
  bildiryapti — gap oxiridagi qoʻshimcha. PK-35, PK-48 va PK-49 dagi
  아/어서 · (으)니까 · 기 때문에 ikki qismni bir-biriga bogʻlaydi;
  잖아요 esa bitta gapning oxirida turadi va uni eslatmaga aylantiradi.
  Oʻzbekchada ham shunday: “-ku” bogʻlovchi emas, gapga qoʻshiladigan
  yumshatuvchi zarra.</p>
</div>

<h3>4. Uchinchi vazifasi: yumshoq eʼtiroz</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">— 이 식당은 비싸요.<br>
     — 하지만 음식이 <span class="pe-hl pe-hl--v">맛있잖아요</span>.</p>
  <p class="pe-ex__uz">— Bu oshxona qimmat.<br>
     — Lekin ovqati mazali-ku.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida buning ikkita juftligi bor:</b> “-<b>ku</b>” va
  “-<b>da</b>”, koʻpincha “<b>axir</b>” bilan birga. “Aytdim-<em>ku</em>!”,
  “Yomgʻir yogʻyapti-<em>da</em>”, “Axir bilasiz-<em>ku</em>”. Bu shakllar
  yangi maʼlumot bermaydi — ular <em>“buni siz allaqachon bilasiz”</em>
  degan ishorani qoʻshadi. 잖아요 aynan shu ishni qiladi. Shuning uchun
  koreyscha gapni tarjima qilganda “-ku” yoki “-da” ni qoʻshib koʻring:
  ohang darrov toʻgʻri chiqadi.</p>
</div>

<h3>5. Qachon ISHLATMASLIK kerak</h3>

<p>Endi eng muhim qismi. <b>잖아요</b> ohangi ichida “<em>buni bilishingiz
kerak edi</em>” degan maʼno bor. Shuning uchun uni notoʻgʻri joyda ishlatish
qoʻpol eshitiladi.</p>

<div class="pe-call pe-warn">
  <p><b>Uchta holatda ishlatmang:</b><br>
  1. Suhbatdosh <b>bilmaydigan</b> narsa haqida — u yangi maʼlumotni
     “bilishing kerak edi” degandek eshitadi.<br>
  2. <b>Katta yoshli</b> yoki <b>notanish</b> odam bilan — ohang
     dagʻal chiqadi.<br>
  3. <b>Rasmiy</b> vaziyatda — imtihon javobida, ish suhbatida,
     yozma matnda.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>선생님, 숙제가 어렵잖아요.</s></p>
  <p class="pe-good">선생님, 숙제가 <b>어려워요</b>.</p>
  <p><small>Oʻqituvchiga 잖아요 bilan gapirish “axir bilasiz-ku” degandek
  chiqadi — bu hurmatsizlik.</small></p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham xuddi shu tuygʻu bor.</b> Tengdoshingizga
  “aytdim-ku!” desangiz — normal. Lekin oʻqituvchingizga yoki notanish
  kishiga shunday desangiz, u dagʻal eshitiladi: goʻyo uni ayblayapsiz.
  Yaʼni bu qoidani yodlash shart emas — ona tilingizdagi tuygʻuga ishoning.
  Kimga “-ku” deyish mumkin boʻlsa, oʻshanga 잖아요 ham mumkin.</p>
</div>

<h3>6. 잖아요 va oddiy 아/어요 — ohangdagi farq</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">비가 와요</p>
    <p><b>Yangi maʼlumot.</b></p>
    <p>“Yomgʻir yogʻyapti.” — suhbatdosh buni bilmasligi mumkin.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">비가 오잖아요</p>
    <p><b>Eslatma.</b></p>
    <p>“Axir yomgʻir yogʻyapti-ku.” — suhbatdosh buni koʻrib turibdi.</p>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>음악을 들잖아요.</s></p>
  <p class="pe-good">음악을 <b>듣잖아요</b>.</p>
  <p><small>잖 undosh — 듣 oʻzgarmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>오늘 일요일잖아요.</s></p>
  <p class="pe-good">오늘 <b>일요일이잖아요</b>.</p>
  <p><small>Ot bilan <b>이</b> qoʻshiladi: 일요일 + 이잖아요.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>제 이름은 셰르벡이잖아요 (yangi tanishga)</s></p>
  <p class="pe-good">제 이름은 <b>셰르벡이에요</b>.</p>
  <p><small>Suhbatdosh bilmaydigan narsa haqida 잖아요 ishlatilmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>말하잖았어요.</s></p>
  <p class="pe-good"><b>말했잖아요</b>.</p>
  <p><small>Zamon <b>잖아요 dan oldin</b> qoʻyiladi: 말했 + 잖아요.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 제가 어제
  <span class="pe-blank"></span> (말하다, oʻtgan zamon) 잖아요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>말했</b> — 말했잖아요 (“axir kecha aytdim-ku”). Zamon 잖아요 dan
    oldin turadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 오늘 <span class="pe-blank"></span>
  (일요일) 잖아요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>일요일이</b> — ot bilan 이 qoʻshiladi: 일요일이잖아요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Xatoni toping:
  <s>음악을 들잖아요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>듣잖아요.</b> 잖 undosh bilan boshlanadi, shuning
    uchun ㄷ oʻzgarmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Bu gapda nima notoʻgʻri?
  Yangi tanishgan odamga: <s>제 이름은 자수르잖아요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Suhbatdosh ismingizni <b>bilmaydi</b> — 잖아요 esa “buni bilasiz-ku”
    degan maʼno beradi. Toʻgʻrisi: <b>제 이름은 자수르예요.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Oʻzbekchaga oʻgiring:
  — 왜 안 갔어요? — 비가 왔잖아요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>— Nega bormadingiz? — <b>Axir yomgʻir yogʻdi-ku.</b>
    잖아요 sababni eslatma ohangida beryapti.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Oʻqituvchingizga 잖아요 bilan
  gapirsa boʻladimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Yoʻq.</b> Ohangi “buni bilishingiz kerak edi” degandek chiqadi va
    hurmatsizlik boʻlib eshitiladi. Oʻzbekchada ham oʻqituvchiga
    “aytdim-ku!” demaysiz — xuddi shu tuygʻu.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>잖아요</b> — …-ku, …-da (eslatma ohangi)</li>
  <li><b>(이)잖아요</b> — … -ku (ot bilan; unlidan keyin 이 tushadi)</li>
  <li><b>일요일</b> — yakshanba</li>
  <li><b>가져오다</b> — olib kelmoq</li>
  <li><b>비싸다</b> — qimmat</li>
  <li><b>맛있다</b> — mazali</li>
  <li><b>말하다</b> — aytmoq, gapirmoq</li>
  <li><b>식당</b> — oshxona</li>
  <li><b>어렵다</b> — qiyin</li>
  <li><b>왜</b> — nega</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>잖아요</b> = “…-ku, …-da” — suhbatdosh biladigan narsani eslatadi.</li>
    <li>Ayri yoʻq, notoʻgʻri oʻzgarish yoʻq: 듣잖아요, 덥잖아요.</li>
    <li>Zamon <b>잖아요 dan oldin</b>: 말했잖아요.</li>
    <li>Ot bilan <b>(이)잖아요</b>: 일요일<b>이</b>잖아요, lekin 친구잖아요.</li>
    <li>Uch vazifasi: eslatish · sababni koʻrsatish · yumshoq eʼtiroz.</li>
    <li><b>Ishlatmang:</b> suhbatdosh bilmaydigan narsa haqida, katta yoshli
      yoki notanish odam bilan, rasmiy vaziyatda.</li>
    <li>Oʻzbekcha tuygʻuga ishoning: kimga “-ku” deyish mumkin boʻlsa,
      oʻshanga 잖아요 ham mumkin.</li>
  </ul>
</div>
""",
    },
]
