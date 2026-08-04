# -*- coding: utf-8 -*-
"""Prime Korean — Block G ning yakuni, darslar 98–100. KURS TUGADI.

 98. 거늘, 기로서니 — adabiy va rasmiy yon berish
 99. 사자성어 va idiomalar — yozma nutqni bezash
100. Hammasi birga: TOPIK II darajasidagi matnni grammatik tahlil qilish

Oʻzbekcha kalitlar:
  -거늘        = "…ku, …ekan-ku"        (adabiy, maqol tili)
  하물며 …랴   = "qolaversa …mi?"        (거늘 ning jufti)
  기로서니     = "qanchalik … boʻlmasin" (taʼna bilan)
  사자성어     = toʻrt ieroglifli ibora
  관용 표현    = idioma

Bu uch dars bir-biriga ulanadi va butun kursni yopadi:
  98 — grammatikaning eng adabiy pogʻonasi (til zinapoyasining tepasi);
  99 — grammatika emas, LUGʻAT — yozma nutqni bezash;
  100 — hech qanday yangi qolip yoʻq. Faqat METOD: matnni ochish.

PK-100 — 100-dars. U yangi narsa oʻrgatmaydi, balki oʻquvchiga
oʻzi bilgan narsalarni koʻrsatadi. Shuning uchun uning ichida
BUTUN KURS xaritasi (Block A–G) va besh qadamli tahlil usuli bor.
Oxirida — oʻquvchiga yopiq soʻz. Bu 100-darsning haqqi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_98_100.py --author=prime
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
    # PK-98
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-98: 거늘, 기로서니 — adabiy va rasmiy yon berish",
        "category": "korean",
        "order": 98,
        "summary": (
            "“Hayvon ham yaxshilikni biladi-ku, qolaversa inson?” — "
            "maqol va klassik matnlarning tili. Yon berishning eng "
            "yuqori, eng adabiy pogʻonasi."
        ),
        "stories": ["유배지에서 온 편지"],
        "content": """
<h2>PK-98: 거늘, 기로서니 — adabiy va rasmiy yon berish</h2>

<p>Oʻzbek maqolini eslang: <em>“Hayvon ham yaxshilikni biladi,
inson-<b>ku</b>!”</em> Yoki onangizning gapi: <em>“Qanchalik band
boʻlmang, ovqat yeyish kerak-<b>ku</b>!”</em></p>

<p>Ikkala gapda ham bitta narsa bor — <b>“-ku”</b>. U shunchaki
qarama-qarshilik emas: uning ichida <em>taʼna</em>, <em>hayrat</em>
va <em>“buni oʻzing ham bilishing kerak edi”</em> degan maʼno bor.
Koreys tilida bu ish ikkita eski qolipga yuklangan.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>-거늘</b> bilan adabiy va maqol tilida gapirasiz</li>
    <li><b>하물며 … 랴</b> juftligini tanib olasiz</li>
    <li><b>기로서니</b> bilan taʼna aralash yon berish qilasiz</li>
    <li>Bularni PK-81 dagi <b>더라도 / 지라도</b> dan ajratasiz</li>
    <li>Qaysi birini <em>yozasiz</em>, qaysi birini faqat
      <em>tanib olasiz</em> — buni aniq bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip 1</span>
  <span class="pe-chip pe-chip--v">oʻzak</span>
  <span class="pe-chip pe-chip--o">거늘</span>
  <span class="pe-chip pe-chip--adv">= …ku, …ekan-ku (adabiy)</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip 2</span>
  <span class="pe-chip pe-chip--adv">아무리</span>
  <span class="pe-chip pe-chip--v">oʻzak</span>
  <span class="pe-chip pe-chip--o">기로서니</span>
  <span class="pe-chip pe-chip--neg">= qanchalik … boʻlmasin</span>
</div>

<h3>1. 거늘 — kitob va maqol tili</h3>

<p>Bu qolipni siz <em>yozmaysiz</em> — lekin uni <b>tanishingiz</b>
shart. U maqollarda, klassik matnlarda, eski xatlarda va
adabiy uslubdagi maqolalarda yashaydi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima bilan</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td class="pk-stem">feʼl</td><td class="pk-end">거늘</td>
      <td class="pk-res">알<b>거늘</b> · 가<b>거늘</b></td></tr>
  <tr><td class="pk-stem">sifat</td><td class="pk-end">거늘</td>
      <td class="pk-res">밝<b>거늘</b> · 어렵<b>거늘</b></td></tr>
  <tr><td class="pk-stem">oʻtgan zamon</td><td class="pk-end">았/었거늘</td>
      <td class="pk-res">배웠<b>거늘</b></td></tr>
  <tr><td class="pk-stem">ot</td><td class="pk-end">(이)거늘</td>
      <td class="pk-res">사람<b>이거늘</b></td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">짐승도 은혜를 <span class="pe-hl pe-hl--v">알거늘</span>,
     하물며 사람이랴.</p>
  <p class="pe-ex__uz">Hayvon ham yaxshilikni biladi-ku, qolaversa
  insonmi?</p>
  <p class="pe-ex__why">Koreys maqollarining eng mashhur
  qoliplaridan biri.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">배우지 않고서는 알 수 없<span class="pe-hl pe-hl--v">거늘</span>,
     어찌 책을 멀리하느냐.</p>
  <p class="pe-ex__uz">Oʻrganmasdan bilib boʻlmaydi-ku, nega
  kitobdan uzoqlashasan?</p>
</div>

<div class="pe-call pe-rule">
  <p><b>거늘 ning ikki ishi:</b><br>
  <b>1. Asos berish</b> — “shunday ekan…”. Ketidan xulosa yoki
  savol keladi.<br>
  <b>2. Qarama-qarshilik</b> — “shunday boʻlsa-da…”.<br>
  Ikkalasida ham gapiruvchining <em>ichki hukmi</em> bor: “bu —
  maʼlum haqiqat, sen esa boshqacha qilyapsan”.</p>
</div>

<h3>2. 하물며 … (이)랴 — 거늘 ning jufti</h3>

<p>Maqol qolipida <b>거늘</b> deyarli doim <b>하물며</b> bilan
juft keladi. Maʼnosi: “<em>qolaversa</em>, “<em>u yoqda
tursin</em>”.</p>

<div class="pe-steps">
  <p><b>1-qism:</b> kichik yoki past narsa ham shunday qiladi
  — <b>…거늘</b>.</p>
  <p><b>2-qism:</b> <b>하물며</b> + katta yoki yuqori narsa +
  <b>(이)랴</b> — “…mi?” degan javobsiz savol.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">작은 씨앗도 자라거늘,
     <span class="pe-hl pe-hl--adv">하물며</span> 사람<span class="pe-hl pe-hl--adv">이랴</span>.</p>
  <p class="pe-ex__uz">Kichkina urugʻ ham oʻsadi-ku, qolaversa
  insonmi?</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu qolip oʻzbek maqollariga juda yaqin.</b>
  “<em>Hayvon ham yaxshilikni biladi, inson-ku</em>”,
  “<em>Tosh ham eriydi, odam koʻngli-ku</em>”. Ikkala tilda ham
  bir xil mantiq: <b>pastdan yuqoriga</b> qarab dalil keltirish.
  Avval “hatto … ham shunday” deyiladi, keyin “demak …
  albatta” degan xulosa <em>aytilmaydi</em> — u savol qilib
  qoldiriladi. Bu — ikkala xalqning ham donishmandlik uslubi.
  Shuning uchun bu darsdagi misollarni oʻzbekcha maqollar bilan
  yonma-yon qoʻyib yodlang — ular oʻz-oʻzidan yodda qoladi.</p>
</div>

<h3>3. 기로서니 — taʼna aralash yon berish</h3>

<p>Bu — ogʻzaki, lekin eskicha. Uni bobo-buvilar va katta yoshli
odamlar ishlatadi. Deyarli doim <b>아무리</b> bilan boshlanadi va
ketidan <em>tanbeh</em> keladi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Shakl</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">feʼl/sifat + 기로서니</td>
      <td class="pk-res">아무리 바쁘기로서니</td>
      <td class="pk-uz">qanchalik band boʻlmang</td></tr>
  <tr><td class="pk-stem">qisqargan: 기로</td>
      <td class="pk-res">아무리 바쁘기로</td>
      <td class="pk-uz">shu maʼno, qisqaroq</td></tr>
  <tr><td class="pk-stem">ot + (이)기로서니</td>
      <td class="pk-res">아무리 아이기로서니</td>
      <td class="pk-uz">bola boʻlsa ham</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">아무리 <span class="pe-hl pe-hl--v">바쁘기로서니</span>
     밥은 먹어야지.</p>
  <p class="pe-ex__uz">Qanchalik band boʻlmang, ovqat yeyish
  kerak-ku.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아무리 <span class="pe-hl pe-hl--v">화가 나기로서니</span>
     그런 말을 하면 안 된다.</p>
  <p class="pe-ex__uz">Qanchalik jahlingiz chiqmasin, bunday gap
  aytish mumkin emas.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Ketidan nima keladi — qolipning kalitini shu belgilaydi.</b>
  <b>기로서니</b> dan keyin deyarli doim
  <b>…아/어야지</b> (“…qilish kerak-ku”),
  <b>…(으)면 안 된다</b> (PK-51) yoki
  <b>어떻게 …?</b> keladi. Yaʼni gapiruvchi sababni qabul qiladi,
  lekin <em>natijani qabul qilmaydi</em>. Mana shu — taʼnaning
  oʻzi.</p>
</div>

<h3>4. PK-81 bilan yonma-yon</h3>

<p>PK-81 da yon berishning uch shaklini oʻrgangansiz. Endi
ularni bugungi ikkitasi bilan bir jadvalga qoʻyamiz — bu
darsning eng foydali qismi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Dars</th><th>Uslub</th><th>Ichida nima bor</th></tr>
  <tr><td class="pk-stem">아/어도</td><td class="pk-end">PK-51</td>
      <td class="pk-uz">kundalik</td><td>oddiy yon berish</td></tr>
  <tr><td class="pk-stem">더라도</td><td class="pk-end">PK-81</td>
      <td class="pk-uz">neytral</td><td>faraz + yon berish</td></tr>
  <tr><td class="pk-stem">(으)ㄹ지라도</td><td class="pk-end">PK-81</td>
      <td class="pk-uz">yozma</td><td>kuchli yon berish</td></tr>
  <tr><td class="pk-stem">(으)ㅁ에도 불구하고</td><td class="pk-end">PK-81</td>
      <td class="pk-uz">rasmiy yozma</td><td>hujjat tili</td></tr>
  <tr><td class="pk-stem">기로서니</td><td class="pk-end">PK-98</td>
      <td class="pk-uz">eskicha ogʻzaki</td><td><b>+ taʼna</b></td></tr>
  <tr><td class="pk-stem">거늘</td><td class="pk-end">PK-98</td>
      <td class="pk-uz">adabiy, maqol</td><td><b>+ hukm</b></td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Yozma ishda qaysini ishlatasiz?</b> TOPIK 쓰기 da
  <b>더라도</b>, <b>(으)ㄹ지라도</b> va <b>(으)ㅁ에도 불구하고</b>
  ishlating. <b>거늘</b> va <b>기로서니</b> ni <em>yozmang</em> —
  ular imtihon uslubiga mos emas va hissiy baho olib keladi.
  Ularning vazifasi boshqa: <b>oʻqishda tanib olish</b>. TOPIK
  읽기 da eski matn yoki maqol berilsa, siz endi toʻxtab
  qolmaysiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>바쁘기로서니 밥은 먹어야지.</s></p>
  <p class="pe-good"><b>아무리</b> 바쁘기로서니 밥은 먹어야지.</p>
  <p><small><b>아무리</b> siz bu qolip toʻliq eshitilmaydi — u
  qolipning bir qismi kabi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>아무리 바쁘기로서니 집에 갔다.</s></p>
  <p class="pe-good">아무리 바쁘기로서니 밥은 <b>먹어야지</b>.</p>
  <p><small>Ketidan oddiy xabar emas, <b>tanbeh</b> kelishi
  kerak: 아/어야지 · (으)면 안 된다 · 어떻게 …?</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>이 문제는 어렵거늘 다시 풀겠습니다.</s></p>
  <p class="pe-good">이 문제는 <b>어렵더라도</b> 다시 풀겠습니다.</p>
  <p><small>거늘 — adabiy, maqol tili. Oddiy rasmiy gapda
  <b>더라도</b> (PK-81) ishlatiladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>짐승도 은혜를 알거늘 사람도 안다.</s></p>
  <p class="pe-good">짐승도 은혜를 알거늘, <b>하물며 사람이랴</b>.</p>
  <p><small>거늘 ning kuchi javobsiz savolda. Xulosani ochiq
  aytib qoʻysangiz, qolip oʻz ishini yoʻqotadi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 아무리
  <span class="pe-blank"></span> 밥은 먹어야지. (바쁘다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>바쁘기로서니</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> 기로서니 dan oldin qaysi
  soʻz deyarli doim turadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>아무리</b>. Usiz qolip toʻliq eshitilmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 기로서니 dan keyin qanday
  gap keladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Tanbeh</b>: 아/어야지 · (으)면 안 된다 · 어떻게 …?
    Oddiy xabar emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Toʻldiring: 짐승도 은혜를
  <span class="pe-blank"></span>, 하물며 사람이랴. (알다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>알거늘</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> <b>하물며</b> nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>“<b>Qolaversa</b>, u yoqda tursin”. 거늘 ning doimiy
    jufti.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> TOPIK 쓰기 da qaysi
  qolipni ishlatasiz — 거늘 yoki 더라도?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>더라도</b> (PK-81). 거늘 — faqat oʻqishda tanib olish
    uchun.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Bu ikki qolipning ichida
  더라도 da yoʻq boʻlgan nima bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>기로서니</b> da — taʼna. <b>거늘</b> da — hukm.
    더라도 esa neytral.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">8</span> Oʻzbekchaga oʻgiring:
  <b>아무리 화가 나기로서니 그런 말을 하면 안 된다.</b></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>“Qanchalik jahlingiz chiqmasin, bunday gap aytish mumkin
    emas.”</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>-거늘</b> — …ku, …ekan-ku (adabiy)</li>
  <li><b>하물며</b> — qolaversa, u yoqda tursin</li>
  <li><b>기로서니</b> — qanchalik … boʻlmasin</li>
  <li><b>아무리</b> — qanchalik</li>
  <li><b>짐승</b> — hayvon, jonivor</li>
  <li><b>은혜</b> — yaxshilik, minnatdorlik qarzi</li>
  <li><b>씨앗</b> — urugʻ</li>
  <li><b>어찌</b> — qanday qilib (adabiy)</li>
  <li><b>멀리하다</b> — uzoqlashmoq</li>
  <li><b>타이르다</b> — nasihat qilmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>-거늘</b> = adabiy, maqol tili. Asos beradi yoki
      qarama-qarshi qoʻyadi.</li>
    <li>Doimiy jufti: <b>하물며 … (이)랴</b> — javobsiz savol.</li>
    <li><b>기로서니</b> = yon berish + <b>taʼna</b>. Doim
      <b>아무리</b> bilan.</li>
    <li>Ketidan tanbeh: <b>아/어야지 · (으)면 안 된다 ·
      어떻게 …?</b></li>
    <li>Yozma ishda <b>더라도 / 지라도 / ㅁ에도 불구하고</b>
      ishlating.</li>
    <li>Bu ikkisining vazifasi — <b>oʻqishda tanib olish</b>.</li>
    <li>Oʻzbekcha juftligi: “<b>-ku</b>”, “<b>qanchalik …
      boʻlmasin</b>”.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-99
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-99: 사자성어 va idiomalar — yozma nutqni bezash",
        "category": "korean",
        "order": 99,
        "summary": (
            "고진감래, 새옹지마, 발이 넓다 — koreys yozma nutqining "
            "bezagi. Oʻn ikkita 사자성어, oʻnta idioma va ularni "
            "qayerda ishlatish (hamda qayerda ishlatmaslik) qoidasi."
        ),
        "stories": ["할아버지와 말 한 마리"],
        "content": """
<h2>PK-99: 사자성어 va idiomalar — yozma nutqni bezash</h2>

<p>Oʻzbek tilida insho yozayotgan oʻquvchi oxirida nima qiladi?
Maqol keltiradi: <em>“Sabrning tagi sariq oltin.”</em> Bitta jumla
— va butun matn tugallangandek boʻladi.</p>

<p>Koreys tilida ham xuddi shunday. Faqat u yerda maqolning oʻrniga
koʻpincha <b>사자성어</b> — toʻrt ieroglifdan iborat siqilgan ibora
turadi. Bu darsda kursning oxirgi grammatikasidan keyingi eng
foydali narsani olasiz: <em>tayyor jumlalar</em>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Eng koʻp ishlatiladigan <b>12 ta 사자성어</b> ni oʻrganasiz</li>
    <li><b>10 ta 관용 표현</b> (idioma) ni bilib olasiz</li>
    <li>Ularning oʻzbekcha maqol juftini topasiz</li>
    <li>Yozma ishda ularni <em>qayerga</em> qoʻyishni bilasiz</li>
    <li>Eng koʻp qilinadigan xatoni — <b>koʻp ishlatishni</b> —
      oldini olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tuzilishi</span>
  <span class="pe-chip pe-chip--s">漢字</span>
  <span class="pe-chip pe-chip--o">漢字</span>
  <span class="pe-chip pe-chip--v">漢字</span>
  <span class="pe-chip pe-chip--adv">漢字</span>
  <span class="pe-chip pe-chip--opt">= bitta butun fikr</span>
</div>

<h3>1. 사자성어 nima?</h3>

<p><b>사자성어 (四字成語)</b> — “toʻrt harfli tayyor ibora”. Har
bir ieroglif bitta soʻz, toʻrttasi birgalikda bitta <em>hikoya</em>
yoki <em>hikmat</em> beradi. Koreys tilida ularning koʻpi Xitoy
klassikasidan kelgan.</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">고</span>진<span class="pe-hl pe-hl--v">감</span>래
     (苦盡甘來)</p>
  <p class="pe-ex__uz">Achchiq tugaydi, shirin keladi. →
  Mashaqqatdan keyin rohat.</p>
  <p class="pe-ex__why">苦 achchiq · 盡 tugamoq · 甘 shirin ·
  來 kelmoq. Toʻrt soʻz — butun bir maqol.</p>
</div>

<h3>2. Eng kerakli 12 ta</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>사자성어</th><th>Maʼnosi</th><th>Oʻzbekcha juftligi</th></tr>
  <tr><td class="pk-stem">고진감래</td><td class="pk-uz">mashaqqatdan keyin rohat</td>
      <td class="pk-res">Sabrning tagi sariq oltin</td></tr>
  <tr><td class="pk-stem">새옹지마</td><td class="pk-uz">yaxshi-yomon almashadi, hech kim bilmaydi</td>
      <td class="pk-res">Har balo bir savob</td></tr>
  <tr><td class="pk-stem">유비무환</td><td class="pk-uz">tayyorgarlik boʻlsa, tashvish yoʻq</td>
      <td class="pk-res">Ehtiyot — imonning yarmi</td></tr>
  <tr><td class="pk-stem">일석이조</td><td class="pk-uz">bitta ish, ikkita foyda</td>
      <td class="pk-res">Bir oʻq bilan ikki quyon</td></tr>
  <tr><td class="pk-stem">백문불여일견</td><td class="pk-uz">yuz marta eshitgandan bir marta koʻrgan afzal</td>
      <td class="pk-res">Aynan shu maqol oʻzbekchada ham bor</td></tr>
  <tr><td class="pk-stem">작심삼일</td><td class="pk-uz">qaror uch kun turadi</td>
      <td class="pk-res">Tavbasi uch kunlik</td></tr>
  <tr><td class="pk-stem">우이독경</td><td class="pk-uz">hoʻkiz qulogʻiga kitob oʻqigan bilan</td>
      <td class="pk-res">Eshakka gapirgan bilan</td></tr>
  <tr><td class="pk-stem">전화위복</td><td class="pk-uz">balo baraka boʻlib qaytdi</td>
      <td class="pk-res">Har ishda bir xayr bor</td></tr>
  <tr><td class="pk-stem">인과응보</td><td class="pk-uz">har ish oʻz javobini oladi</td>
      <td class="pk-res">Nima eksang, shuni oʻrasan</td></tr>
  <tr><td class="pk-stem">십시일반</td><td class="pk-uz">oʻn qoshiq — bir kosa</td>
      <td class="pk-res">Koʻpdan quyon qochib qutulmas</td></tr>
  <tr><td class="pk-stem">다다익선</td><td class="pk-uz">koʻp boʻlgani yaxshi</td>
      <td class="pk-res">Koʻp boʻlsa, kam boʻlmaydi</td></tr>
  <tr><td class="pk-stem">금상첨화</td><td class="pk-uz">yaxshining ustiga yana yaxshi</td>
      <td class="pk-res">Oltinga zar qoʻshgandek</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu jadvalning oʻng ustuni — Prime Korean ning eng katta
  imkoniyati.</b> Ingliz tilida koreys 사자성어 sining tayyor
  juftligi koʻpincha <em>yoʻq</em>: “고진감래” ni inglizga
  tarjima qilish uchun butun bir jumla kerak. Oʻzbek tilida esa
  deyarli har biriga <b>tayyor maqol</b> topiladi — chunki
  ikkala xalq ham asrlar davomida shu fikrni oʻz maqoliga
  siqqan. Shuning uchun siz bu iboralarni <em>yodlamaysiz</em> —
  siz faqat <b>oʻzbekcha maqolingizga koreyscha nom
  qoʻyasiz</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">지금은 힘들지만 <span class="pe-hl pe-hl--s">고진감래</span>라는
     말이 있다.</p>
  <p class="pe-ex__uz">Hozir qiyin, lekin “고진감래” degan gap
  bor.</p>
  <p class="pe-ex__why">Eng koʻp ishlatiladigan qolip:
  <b>…(이)라는 말이 있다</b> — “… degan gap bor”.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">인생은 <span class="pe-hl pe-hl--s">새옹지마</span>다.
     좋은 일과 나쁜 일은 함께 온다.</p>
  <p class="pe-ex__uz">Hayot — 새옹지마. Yaxshilik bilan yomonlik
  birga keladi.</p>
</div>

<h3>3. 관용 표현 — tana aʼzolari bilan idiomalar</h3>

<p>Ikkinchi guruh — kundalik idiomalar. Ularning koʻpi tana aʼzosi
bilan tuzilgan, va bu yerda ham oʻzbekcha bilan qiziq
oʻxshashliklar bor.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Idioma</th><th>Soʻzma-soʻz</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">발이 넓다</td><td class="pk-end">oyogʻi keng</td>
      <td class="pk-uz">tanish-bilishi koʻp</td></tr>
  <tr><td class="pk-stem">손이 크다</td><td class="pk-end">qoʻli katta</td>
      <td class="pk-uz">saxovatli, koʻp qiladi</td></tr>
  <tr><td class="pk-stem">눈이 높다</td><td class="pk-end">koʻzi baland</td>
      <td class="pk-uz">talabchan, tanlaydi</td></tr>
  <tr><td class="pk-stem">귀가 얇다</td><td class="pk-end">qulogʻi yupqa</td>
      <td class="pk-uz">tez ishonadi</td></tr>
  <tr><td class="pk-stem">입이 무겁다</td><td class="pk-end">ogʻzi ogʻir</td>
      <td class="pk-uz">sir saqlaydi</td></tr>
  <tr><td class="pk-stem">코가 높다</td><td class="pk-end">burni baland</td>
      <td class="pk-uz">kibrli</td></tr>
  <tr><td class="pk-stem">발등에 불이 떨어지다</td><td class="pk-end">oyoq ustiga oʻt tushdi</td>
      <td class="pk-uz">muddat yaqinlashdi, shoshildi</td></tr>
  <tr><td class="pk-stem">시간 가는 줄 모르다</td><td class="pk-end">vaqt ketganini bilmaslik</td>
      <td class="pk-uz">vaqt oʻtganini sezmay qolmoq</td></tr>
  <tr><td class="pk-stem">한 우물을 파다</td><td class="pk-end">bitta quduq qazimoq</td>
      <td class="pk-uz">bir ishga umr berish</td></tr>
  <tr><td class="pk-stem">그림의 떡</td><td class="pk-end">rasmdagi non</td>
      <td class="pk-uz">yetib boʻlmaydigan narsa</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Uchtasi oʻzbekchada deyarli aynan bor.</b>
  <b>입이 무겁다</b> — biz ham “<em>ogʻzi mahkam</em>” deymiz.
  <b>코가 높다</b> — “<em>burni koʻtarilgan</em>”.
  <b>그림의 떡</b> — “<em>rasmdagi osh</em>”. Qolganlarini esa
  soʻzma-soʻz tarjimasi bilan yodlang: koreyscha tasvir shu
  qadar aniqki, bir marta koʻrsangiz unutmaysiz —
  <em>qulogʻi yupqa</em> odam har gapni oʻtkazib yuboradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">우리 형은 <span class="pe-hl pe-hl--s">발이 넓어서</span>
     모르는 사람이 없다.</p>
  <p class="pe-ex__uz">Akamning tanishi koʻp — bilmaydigan odami
  yoʻq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">한 가지 일을 삼십 년 동안 했다. 그는
     <span class="pe-hl pe-hl--s">한 우물을 판</span> 사람이다.</p>
  <p class="pe-ex__uz">Bir ishni oʻttiz yil qildi. U — bir quduq
  qazigan odam.</p>
</div>

<h3>4. Qayerga qoʻyasiz? — TOPIK 쓰기 qoidasi</h3>

<div class="pe-steps">
  <p><b>1. Bittasini tanlang.</b> Butun inshoda <b>bitta</b>
  사자성어 yetarli.</p>
  <p><b>2. Xulosaga qoʻying.</b> Eng kuchli oʻrni — oxirgi
  banddagi umumlashtirish.</p>
  <p><b>3. Tayyor qolip bilan kiriting:</b>
  <b>…(이)라는 말이 있다</b> yoki <b>…(이)라고 할 수 있다</b>.</p>
  <p><b>4. Maʼnosini bir jumlada oching.</b> Faqat ibora
  yozib qoʻysangiz, tekshiruvchi uni <em>bezak</em> deb hisoblaydi;
  maʼnosini ochsangiz — <em>fikr</em> deb hisoblaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">준비한 사람만이 기회를 잡는다.
     <span class="pe-hl pe-hl--s">유비무환</span>이라는 말이 있듯이,
     미리 대비하는 태도가 무엇보다 중요하다.</p>
  <p class="pe-ex__uz">Faqat tayyorlangan odam imkoniyatni ushlaydi.
  “유비무환” degan gap borki, oldindan tayyorgarlik koʻrish
  hammasidan muhim.</p>
  <p class="pe-ex__why">Ibora + uning maʼnosi + xulosa. Uchalasi
  bir bandda — TOPIK 쓰기 54 ning ideal yakuni.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Eng koʻp qilinadigan xato — koʻp ishlatish.</b> Uchta
  사자성어 qoʻyilgan insho bilimni emas, <em>ishonchsizlikni</em>
  koʻrsatadi. Koreys tekshiruvchisi buni darhol sezadi:
  “oʻquvchi yodlagan iboralarini toʻkib tashlagan”. Bitta ibora,
  toʻgʻri joyda — bu kuch. Uchta ibora — bu bezak. Xuddi oʻzbek
  inshosidagidek.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>고진감래. 그래서 열심히 해야 한다.</s></p>
  <p class="pe-good"><b>고진감래라는 말이 있다.</b> 힘든 시간이
  지나면 좋은 날이 온다.</p>
  <p><small>Iborani yolgʻiz tashlab ketmang — kirituvchi qolip va
  maʼnosini oching.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>친구가 발이 큽니다.</s></p>
  <p class="pe-good">친구가 <b>발이 넓습니다</b>.</p>
  <p><small>발이 <b>크다</b> — oyogʻi katta (haqiqiy oʻlcham).
  Tanish-bilish koʻpligi — <b>넓다</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>이 글에서 저는 새옹지마, 고진감래, 유비무환을
  말하고 싶습니다.</s></p>
  <p class="pe-good">이 글에서 저는 <b>유비무환</b>의 중요성을
  말하고 싶습니다.</p>
  <p><small>Bitta ibora — bitta fikr. Uchtasi birga kelsa,
  hech biri ishlamaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>야, 너 진짜 발이 넓기 짝이 없다!</s></p>
  <p class="pe-good">야, 너 진짜 발이 넓다!</p>
  <p><small>Idioma — kundalik nutqning oʻzi. Uni yozma qolip
  (PK-96) bilan bezash gʻalati chiqadi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> <b>고진감래</b> ning
  oʻzbekcha juftligi qaysi maqol?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>“<b>Sabrning tagi sariq oltin</b>” — mashaqqatdan keyin
    rohat.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> <b>새옹지마</b> nimani
  anglatadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Yaxshi va yomon almashadi, hech kim oxirini bilmaydi.
    Oʻzbekcha: “<b>Har balo bir savob</b>”.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> <b>귀가 얇다</b> — soʻzma-soʻz
  va aslida nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Soʻzma-soʻz “qulogʻi yupqa”. Maʼnosi: <b>tez
    ishonadi</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Toʻldiring:
  우리 형은 <span class="pe-blank"></span> 모르는 사람이 없다.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>발이 넓어서</b> — tanish-bilishi koʻp.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Iborani inshoga kiritishning
  tayyor qolipi qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>…(이)라는 말이 있다</b> yoki <b>…(이)라고 할 수 있다</b>.
    Keyin maʼnosini bir jumlada oching.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Bitta inshoda nechta
  사자성어 ishlatasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Bittasi</b>. Uchtasi bilimni emas, ishonchsizlikni
    koʻrsatadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> <b>발이 크다</b> va
  <b>발이 넓다</b> farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>크다</b> — oyoqning haqiqiy oʻlchami. <b>넓다</b> —
    tanish-bilishi koʻp.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">8</span> Bu jumlani toʻldiring
  (한다체): 준비한 사람만이 기회를 잡는다.
  <span class="pe-blank"></span>이라는 말이 있다.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>유비무환</b> — tayyorgarlik boʻlsa, tashvish yoʻq.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>사자성어</b> — toʻrt ieroglifli ibora</li>
  <li><b>관용 표현</b> — idioma, turgʻun ibora</li>
  <li><b>속담</b> — maqol</li>
  <li><b>고진감래</b> — mashaqqatdan keyin rohat</li>
  <li><b>새옹지마</b> — yaxshi-yomon almashadi</li>
  <li><b>유비무환</b> — tayyorgarlik boʻlsa, tashvish yoʻq</li>
  <li><b>전화위복</b> — balo baraka boʻlib qaytdi</li>
  <li><b>발이 넓다</b> — tanish-bilishi koʻp</li>
  <li><b>입이 무겁다</b> — sir saqlaydi</li>
  <li><b>한 우물을 파다</b> — bir ishga umr bermoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>사자성어</b> — toʻrt ieroglif, bitta hikmat.</li>
    <li>Deyarli har biriga <b>oʻzbekcha maqol</b> juftligi bor —
      yodlash oʻrniga shuni ishlating.</li>
    <li>Kirituvchi qolip: <b>…(이)라는 말이 있다</b>.</li>
    <li>Iborani yolgʻiz tashlamang — <b>maʼnosini oching</b>.</li>
    <li>Bitta inshoda <b>bitta</b> ibora, xulosa bandida.</li>
    <li><b>관용 표현</b> — kundalik nutqning idiomalari, koʻpi
      tana aʼzosi bilan.</li>
    <li>발이 <b>넓다</b> ≠ 발이 크다.</li>
    <li>Idiomani yozma qolip bilan bezamang.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-100
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-100: Hammasi birga — TOPIK II matnini grammatik tahlil qilish",
        "category": "korean",
        "order": 100,
        "summary": (
            "Oxirgi dars. Yangi qolip yoʻq — faqat usul: har qanday "
            "koreyscha jumlani besh qadamda ochish. Va butun kursning "
            "xaritasi bir sahifada."
        ),
        "stories": ["끝까지 간 사람들"],
        "content": """
<h2>PK-100: Hammasi birga — TOPIK II darajasidagi matnni grammatik tahlil qilish</h2>

<p>Bu darsda yangi grammatika yoʻq. Bittasi ham.</p>

<p>Chunki hammasi allaqachon sizda. PK-1 da siz <b>ㅏ</b> harfini
oʻrgangan edingiz. Bugun quyidagi jumlani oʻqiysiz va uning har
bir boʻlagi qayerdan kelganini <em>ayta olasiz</em>:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">인구 감소로 인해 문을 닫는 학교가 늘고 있지만,
     이것이 교육의 질 저하로 이어진다고 보기는 어렵다.</p>
  <p class="pe-ex__uz">Aholi kamayishi tufayli yopilayotgan
  maktablar koʻpayib borayotgan boʻlsa-da, buni taʼlim sifatining
  pasayishiga olib keladi deb qarash qiyin.</p>
</div>

<p>Qoʻrqmang. Oxirigacha oʻqisangiz, bu jumla oddiy boʻlib
qoladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Har qanday jumlani <b>besh qadamda</b> ochishni
      oʻrganasiz</li>
    <li>Uchta haqiqiy TOPIK II jumlasini birga tahlil qilasiz</li>
    <li>Butun kursning <b>xaritasini</b> bir jadvalda koʻrasiz</li>
    <li>Tahlil qilayotganda qilinadigan xatolarni bilib olasiz</li>
    <li>Bundan keyin nima qilishni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Usul</span>
  <span class="pe-chip pe-chip--v">1 kesim</span>
  <span class="pe-chip pe-chip--o">2 qoʻshimcha</span>
  <span class="pe-chip pe-chip--s">3 aniqlovchi</span>
  <span class="pe-chip pe-chip--adv">4 bogʻlovchi</span>
  <span class="pe-chip pe-chip--opt">5 qolip</span>
</div>

<h3>1. Besh qadam</h3>

<div class="pe-steps">
  <p><b>1-qadam. Oxiriga qarang.</b> Koreys tilida eng muhim
  narsa hamisha oxirida. Kesimni toping — u gapning <em>nima
  qilyapti</em> sini aytadi va butun jumlaning zamonini,
  darajasini, uslubini belgilaydi.</p>
  <p><b>2-qadam. Qoʻshimchalarni yeching.</b> 은/는, 이/가, 을/를,
  에, 에서, 로 — bularni koʻrsangiz, har bir otning gapdagi
  <em>vazifasini</em> bilasiz. Kim? Kimni? Qayerda? Nima bilan?</p>
  <p><b>3-qadam. Aniqlovchilarni ajrating.</b> 는 / (으)ㄴ / (으)ㄹ
  / 던 — bulardan keyin doim <b>ot</b> keladi. Aniqlovchi
  qayerda boshlanishini toping, va u butun boʻlakni bitta
  “katta ot” deb oʻqing.</p>
  <p><b>4-qadam. Bogʻlovchilarni toping.</b> 고, 지만, 아/어서,
  (으)니까, (으)면, (으)면서, 는데도 — jumla shu yerlarda
  <em>boʻlinadi</em>. Uzun jumlani qisqa jumlalarga kesing.</p>
  <p><b>5-qadam. Qoliplarni tanib oling.</b> Qolgan hamma narsa —
  siz oʻrgangan qoliplar: 것 같다, 수 있다, 게 되다, 로 인해,
  기 때문에, 는 바람에, 을 뿐만 아니라…</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Nega bu usul oʻzbek oʻquvchisiga oson?</b> Chunki oʻzbek
  tili ham xuddi shunday ishlaydi. Bizda ham kesim oxirida
  (“Men kitobni oʻqi<b>dim</b>”), bizda ham qoʻshimchalar otga
  yopishadi (“kitob<b>ni</b>”, “maktab<b>da</b>”), bizda ham
  aniqlovchi otdan oldin turadi (“<b>oʻqiyotgan</b> bola”).
  Ingliz tilida bularning birortasi ham yoʻq. Shuning uchun
  ingliz oʻquvchisi koreyscha jumlani <em>teskari</em> oʻqishga
  majbur — siz esa <b>oʻz tilingizdagidek</b> oʻqiysiz. Bu —
  butun kurs davomida sizning eng katta ustunligingiz edi.</p>
</div>

<h3>2. Birinchi tahlil — oddiy jumla</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">요즘 스마트폰을 오래 보는 사람이 늘고 있다.</p>
  <p class="pe-ex__uz">Soʻnggi paytda smartfonga uzoq qaraydigan
  odamlar koʻpayib bormoqda.</p>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qadam</th><th>Nima topildi</th><th>Qaysi dars</th></tr>
  <tr><td class="pk-stem">1 kesim</td><td class="pk-end">늘고 있다</td>
      <td class="pk-uz">PK-42 (고 있다) + PK-74 (한다체)</td></tr>
  <tr><td class="pk-stem">2 qoʻshimcha</td><td class="pk-end">스마트폰<b>을</b> · 사람<b>이</b></td>
      <td class="pk-uz">PK-17 · PK-12</td></tr>
  <tr><td class="pk-stem">3 aniqlovchi</td><td class="pk-end">오래 보<b>는</b> + 사람</td>
      <td class="pk-uz">PK-43</td></tr>
  <tr><td class="pk-stem">4 bogʻlovchi</td><td class="pk-end">yoʻq — bitta jumla</td>
      <td class="pk-uz">—</td></tr>
  <tr><td class="pk-stem">5 qolip</td><td class="pk-end">고 있다 — davom etayotgan holat</td>
      <td class="pk-uz">PK-42</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Diqqat — 3-qadamning kuchi.</b> “스마트폰을 오래 보는
  사람” — bu <em>toʻrt soʻz</em> emas, bitta narsa: “smartfonga
  uzoq qaraydigan odam”. Aniqlovchini bir butun deb koʻrsangiz,
  jumla darhol qisqaradi: <b>[katta ot]이 늘고 있다</b>. Uzun
  TOPIK jumlalarining 90 foizi shu bilan ochiladi.</p>
</div>

<h3>3. Ikkinchi tahlil — oʻrta jumla</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">전문가들은 이 문제가 기술 발전으로 인해
     더 커질 것이라고 말한다.</p>
  <p class="pe-ex__uz">Mutaxassislar bu muammo texnologiya
  rivoji tufayli yanada kattalashadi deb aytmoqda.</p>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qadam</th><th>Nima topildi</th><th>Qaysi dars</th></tr>
  <tr><td class="pk-stem">1 kesim</td><td class="pk-end">말한다</td>
      <td class="pk-uz">PK-74 (한다체)</td></tr>
  <tr><td class="pk-stem">2 qoʻshimcha</td><td class="pk-end">전문가들<b>은</b> · 문제<b>가</b></td>
      <td class="pk-uz">PK-12</td></tr>
  <tr><td class="pk-stem">3 aniqlovchi</td><td class="pk-end">yoʻq</td>
      <td class="pk-uz">—</td></tr>
  <tr><td class="pk-stem">4 bogʻlovchi</td><td class="pk-end">yoʻq</td>
      <td class="pk-uz">—</td></tr>
  <tr><td class="pk-stem">5 qolip</td><td class="pk-end">…(으)로 인해 · …(으)ㄹ 것이다 · …라고 말하다</td>
      <td class="pk-uz">PK-97 · PK-27 · PK-60</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Bu jumlaning butun siri — koʻchirma gap.</b>
  <b>…라고 말한다</b> ni koʻrsangiz, undan oldingi hamma narsa
  <em>bitta gap</em> ekanini bilasiz: “이 문제가 … 커질 것이다”.
  Yaʼni jumla ikki qavatli: <b>[gap]라고 말한다</b>. TOPIK 읽기
  matnlarining yarmi shunday tuzilgan — chunki maqola hamisha
  <em>kimningdir gapini</em> keltiradi.</p>
</div>

<h3>4. Uchinchi tahlil — darsning boshidagi jumla</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">인구 감소로 인해 문을 닫는 학교가 늘고 있지만,
     이것이 교육의 질 저하로 이어진다고 보기는 어렵다.</p>
</div>

<p>Avval <b>4-qadam</b> ni bajaramiz — bogʻlovchini topamiz va
jumlani ikkiga kesamiz:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Birinchi yarim</p>
    <p>인구 감소<b>로 인해</b> 문을 닫<b>는</b> 학교<b>가</b>
    늘<b>고 있</b><b>지만</b>,</p>
    <p><small>로 인해 (97) · 는 aniqlovchi (43) · 고 있다 (42) ·
    지만 (34)</small></p>
    <p><small>“Aholi kamayishi tufayli yopilayotgan maktablar
    koʻpayib boryapti, <b>lekin</b>…”</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Ikkinchi yarim</p>
    <p>이것<b>이</b> … 저하<b>로</b> 이어진다<b>고</b> 보<b>기는</b>
    어렵다.</p>
    <p><small>이/가 (12) · 로 (14) · 다고 (60) · 기 (46) ·
    한다체 (74)</small></p>
    <p><small>“…buni pasayishga olib keladi deb <b>qarash
    qiyin</b>.”</small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Ikkinchi yarimning yuragi — 보기는 어렵다.</b>
  보다 → <b>보기</b> (PK-46 otlashtirish) → “qarash” degan ot →
  ega qilib qoʻyildi (<b>는</b>) → kesim <b>어렵다</b>.
  Yaʼni: “<em>qarash — qiyin</em>”. Bu qolip TOPIK 읽기 da juda
  koʻp uchraydi va u <b>ehtiyotkor rad javob</b> beradi:
  “bunday deyish qiyin”, yaʼni “men bunga qoʻshilmayman, lekin
  qatʼiy inkor ham qilmayman”.</p>
</div>

<h3>5. Butun kursning xaritasi</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Block</th><th>Darslar</th><th>Nima berdi</th></tr>
  <tr><td class="pk-stem">A — Hangul</td><td class="pk-end">1–8</td>
      <td class="pk-uz">yozuv, boʻgʻin, 받침, talaffuz qoidalari</td></tr>
  <tr><td class="pk-stem">B — Birinchi gaplar</td><td class="pk-end">9–22</td>
      <td class="pk-uz">qoʻshimchalar, 있다/없다, feʼl, zamon, inkor</td></tr>
  <tr><td class="pk-stem">C — Kundalik muloqot</td><td class="pk-end">23–36</td>
      <td class="pk-uz">sonlar, soʻroq, xohish, imkon, bogʻlovchilar</td></tr>
  <tr><td class="pk-stem">D — Oʻrta daraja</td><td class="pk-end">37–52</td>
      <td class="pk-uz"><b>aniqlovchi</b>, otlashtirish, sabab, majburiyat</td></tr>
  <tr><td class="pk-stem">E — Oʻrta-yuqori</td><td class="pk-end">53–68</td>
      <td class="pk-uz"><b>koʻchirma gap</b>, nisbat, murakkab bogʻlanish</td></tr>
  <tr><td class="pk-stem">F — Yuqori</td><td class="pk-end">69–86</td>
      <td class="pk-uz">nozik maʼnolar, afsus, faraz, daraja</td></tr>
  <tr><td class="pk-stem">G — Ilgʻor</td><td class="pk-end">87–100</td>
      <td class="pk-uz">yozma uslub, kinoya, hayrat, rasmiy sabab</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Butun kursning uchta ustuni:</b><br>
  <b>1. 받침 tarmogʻi</b> — 은/는, 이/가, 을/를, (으)로, (으)면,
  (으)ㄴ … Koreys grammatikasining yarmi shu bitta savolga
  qaraydi: soʻz undosh bilan tugadimi?<br>
  <b>2. Aniqlovchi</b> (43–45, 90) — 는 · (으)ㄴ · (으)ㄹ · 던.
  Uzun jumlalarni ochadigan kalit.<br>
  <b>3. Koʻchirma gap</b> (60–62, 92, 93, 95) — 다고 하다 dan
  답시고 gacha. Koreys tilida <em>kimning gapi</em> ekani hamisha
  koʻrinib turadi.<br>
  Shu uchtasini mustahkam bilsangiz, qolgani — tafsilot.</p>
</div>

<h3>Tahlil qilayotganda uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>“읽던 책” = oʻqigan kitob</s></p>
  <p class="pe-good">“읽<b>던</b> 책” = <b>tugatmagan</b> kitob</p>
  <p><small>읽<b>은</b> 책 — oʻqib boʻlgan. 던 (PK-90) —
  boshlangan, tugamagan.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>“간다니” = borarkansiz-a?</s></p>
  <p class="pe-good">“간다<b>니</b>” = borarkan-a! (hayrat)</p>
  <p><small>Tasdiqlash — <b>간다면서요?</b> (92). Hayrat —
  <b>간다니!</b> (93). Bir harf farq qiladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>“가려던 참” va “가려니 했다” bir xil</s></p>
  <p class="pe-good">참 = <b>niyat</b> (90) · 려니 하다 =
  <b>taxmin</b> (94)</p>
  <p><small>려 ning oʻzi hech narsa demaydi — maʼnoni undan
  keyingi qism beradi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Notanish soʻz koʻrsam, jumlani tashlab
  ketaman</s></p>
  <p class="pe-good">Avval <b>grammatikani</b> oching, keyin
  soʻzni taxmin qiling.</p>
  <p><small>TOPIK 읽기 da notanish soʻz doim boʻladi. Lekin
  agar 로 인해 va 지만 ni koʻrsangiz, jumlaning
  <em>tuzilishini</em> bilasiz — maʼnoning yarmi shu.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Tahlil qiling:
  <b>매일 운동하는 사람이 많아지고 있다.</b> — aniqlovchi qayerda?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>운동하는</b> + 사람 (PK-43). Butun boʻlak: “har kuni
    sport bilan shugʻullanadigan odam” — bitta katta ot.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Tahlil qiling:
  <b>비가 오는 바람에 행사가 취소되었다.</b> — qaysi qolip va
  qaysi dars?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>는 바람에</b> — kutilmagan salbiy sabab, <b>PK-69</b>.
    Kesim — majhul nisbat 취소되다 (PK-56).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Tahlil qiling:
  <b>전문가들은 이 문제가 커질 것이라고 말한다.</b> — jumla necha
  qavatli?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Ikki qavatli</b>: [이 문제가 커질 것이다] +
    <b>라고 말한다</b> (PK-60). Ichkarisi — boshqa odamning
    gapi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> <b>보기는 어렵다</b> nima
  degani va qaysi darsdan?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>보다 → <b>보기</b> (PK-46) = “qarash”. “Qarash qiyin” —
    ehtiyotkor rad javob.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Uzun jumlani birinchi
  navbatda nima bilan kesasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Bogʻlovchi bilan</b> (4-qadam): 지만, 아/어서, (으)면서,
    (으)니까… Jumla shu yerlarda boʻlinadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Kursning uchta ustuni
  nima edi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>받침 tarmogʻi · aniqlovchi · koʻchirma gap.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Matnda notanish soʻz
  uchrasa nima qilasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Avval <b>grammatikani</b> ochaman — tuzilma maʼnoning
    yarmini beradi. Soʻzni keyin taxmin qilaman.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">8</span> Darsning boshidagi jumlani
  endi oʻzingiz oʻzbekchaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>“Aholi kamayishi tufayli yopilayotgan maktablar koʻpayib
    borayotgan boʻlsa-da, buni taʼlim sifatining pasayishiga
    olib keladi deb qarash qiyin.”</p>
  </details>
</div>

<h3>Bundan keyin nima qilasiz?</h3>

<div class="pe-steps">
  <p><b>1. Oʻqing.</b> Prime Korean Readings — 92 ta matn.
  Ularni qaytadan, audio bilan oʻqing. Endi siz ularni
  <em>tahlil qila olasiz</em>.</p>
  <p><b>2. Imtihonga tayyorlaning.</b> Saytdagi <b>examprep
  TOPIK</b> boʻlimi — savol turlari, vaqt va strategiya.
  Grammatika sizda bor; endi imtihon usulini oling.</p>
  <p><b>3. Jadvaldan foydalaning.</b> <b>Grammatika</b> va
  <b>lugʻat</b> banklari — qaraladigan maʼlumotnoma. Unutgan
  qolipingizni bir daqiqada topasiz.</p>
  <p><b>4. Yozing.</b> Har kuni uchta jumla — 한다체 da.
  Kuniga uch daqiqa. Bir yilda ming jumla.</p>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>분석하다</b> — tahlil qilmoq</li>
  <li><b>구조</b> — tuzilma</li>
  <li><b>서술어</b> — kesim</li>
  <li><b>조사</b> — qoʻshimcha (yordamchi)</li>
  <li><b>관형사형</b> — aniqlovchi shakl</li>
  <li><b>연결 어미</b> — bogʻlovchi qoʻshimcha</li>
  <li><b>인용</b> — koʻchirma</li>
  <li><b>저하</b> — pasayish</li>
  <li><b>이어지다</b> — davom etmoq, olib bormoq</li>
  <li><b>전문가</b> — mutaxassis</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning — va kursning — xulosasi</p>
  <ul>
    <li>Besh qadam: <b>kesim → qoʻshimcha → aniqlovchi →
      bogʻlovchi → qolip</b>.</li>
    <li>Aniqlovchi boʻlagini <b>bitta katta ot</b> deb oʻqing.</li>
    <li><b>라고 하다</b> ni koʻrsangiz, jumla ikki qavatli.</li>
    <li>Uzun jumlani bogʻlovchi bilan <b>kesing</b>.</li>
    <li>Uchta ustun: <b>받침 · aniqlovchi · koʻchirma gap</b>.</li>
    <li>Notanish soʻz — grammatika ochilgach, taxmin
      qilinadi.</li>
    <li>Koreys va oʻzbek tillari bir xil tartibda ishlaydi —
      bu sizning ustunligingiz edi va shunday qoladi.</li>
  </ul>
</div>

<div class="pe-call pe-tip">
  <p><b>Yuz dars.</b> PK-1 da siz <b>ㅏ</b> ni koʻrgan edingiz va
  u shunchaki chiziq edi. Bugun siz gazeta jumlasini ochib,
  har bir boʻlagining nomini aytasiz.</p>
  <p>Orada 92 ta matn oʻqidingiz, 2000 dan ortiq savolga javob
  berdingiz, va bir marta ham inglizcha tarjimaga qaramadingiz —
  chunki kerak boʻlmadi. Koreys tili sizga oʻz tilingiz orqali
  keldi.</p>
  <p>Til bilish — bu yodlangan qoliplar soni emas. Bu —
  <em>toʻxtamaslik</em>. Endi siz notanish jumlani koʻrganda
  yopmaysiz: ochasiz.</p>
  <p><b>수고하셨습니다. 여기까지 온 것만으로도 충분히 대단하다.</b><br>
  <small>Mehnatingiz uchun rahmat. Shu yergacha yetib kelganingiz
  oʻzi katta ish.</small></p>
</div>
""",
    },
]
