# -*- coding: utf-8 -*-
"""Prime Korean — Block F ning oxiri va Block G ning boshi, darslar 86–88.

86. (으)ㅁ으로써 — vosita va usulning otlashgan shakli   ← Block F yakuni
87. (으)ㄹ 지경이다 — chidab boʻlmas holat va chegara      ← Block G boshlanishi
88. (으)ㄹ 리가 없다 / (으)ㄹ 턱이 없다 — kuchli shubha va inkor

Oʻzbekcha kalitlar:
  (으)ㅁ으로써   = "…ish bilan, … yoʻli bilan"   (vosita — rasmiy yozma)
  (으)로서      = "… SIFATIDA"                  (maqom — 으로써 bilan adashtiriladi)
  (으)ㄹ 지경이다 = "…ay deb turibman"            (chidab boʻlmas holat)
  (으)ㄹ 리가 없다 = "…ishi mumkin emas"          (haqiqatga oid rad)
  (으)ㄹ 턱이 없다 = shu maʼno, keskin va ogʻzaki

PK-86 ikkita adashtiriladigan qoʻshimchani yonma-yon qoʻyadi:
  써 ← 쓰다 (“ishlatmoq”) → ASBOB   ·   서 ← 서다 (“turmoq”) → OʻRIN
Bu esdalik ilgagi butun darsni ushlab turadi.

PK-87 ni PK-82 dagi (으)ㄹ 정도로 bilan, PK-88 ni esa PK-73 dagi
(으)ㄹ지도 모르다 bilan solishtirish shart — 88 ishonch zinapoyasining
manfiy uchini yopadi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_86_88.py --author=prime
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
    # PK-86
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-86: (으)ㅁ으로써 — vosita va usulning otlashgan shakli",
        "category": "korean",
        "order": 86,
        "summary": (
            "“Suhbatlashish bilan muammoni hal qildik” — ishning qanday "
            "yoʻl bilan bajarilganini rasmiy tilda aytish. Va 로써 bilan "
            "로서 ning farqi."
        ),
        "stories": ["쓰레기를 줄인 도시"],
        "content": """
<h2>PK-86: (으)ㅁ으로써 — vosita va usulning otlashgan shakli</h2>

<p>Ikki oʻquvchi urishib qoldi. Ular qanday yarashdi? — <em>Suhbatlashish
bilan.</em> Oʻzbekchada bu juda oddiy: “gaplashish <b>bilan</b>”,
“yordam berish <b>orqali</b>”. Koreys tilida esa buning rasmiy,
yozma qolipi bor — va u sizga tanish boʻlgan ikki qismdan yasaladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㅁ으로써</b> bilan “…ish yoʻli bilan” deysiz</li>
    <li>PK-46 dagi <b>(으)ㅁ</b> otlashtirishini yana ishlatasiz</li>
    <li><b>로써</b> va <b>로서</b> ni bir umrga ajratasiz</li>
    <li>Oddiy <b>(으)로</b> dan farqini bilib olasiz</li>
    <li>Nega bu qolip TOPIK 쓰기 da kerakligini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">feʼl + (으)ㅁ</span>
  <span class="pe-chip pe-chip--o">으로써</span>
  <span class="pe-chip pe-chip--adv">= …ish yoʻli bilan</span>
</div>

<h3>1. Shakli</h3>

<p>Qolip ikki qismdan iborat, va ikkalasi ham sizga tanish:
<b>(으)ㅁ</b> (PK-46 — otlashtirish) va <b>(으)로</b> (PK-14 dagi
vosita qoʻshimchasi) ga <b>써</b> qoʻshilgani.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>(으)ㅁ shakli</th><th>Natija</th></tr>
  <tr><td class="pk-stem">하다</td><td class="pk-end">함</td>
      <td class="pk-res">함으로써</td></tr>
  <tr><td class="pk-stem">대화하다</td><td class="pk-end">대화함</td>
      <td class="pk-res">대화함으로써</td></tr>
  <tr><td class="pk-stem">줄이다</td><td class="pk-end">줄임</td>
      <td class="pk-res">줄임으로써</td></tr>
  <tr><td class="pk-stem">읽다</td><td class="pk-end">읽음</td>
      <td class="pk-res">읽음으로써</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">우리는 <span class="pe-hl pe-hl--o">대화함으로써</span>
     문제를 해결했다.</p>
  <p class="pe-ex__uz">Biz suhbatlashish yoʻli bilan muammoni hal
  qildik.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">쓰레기봉투를 <span class="pe-hl pe-hl--o">유료화함으로써</span>
     쓰레기가 크게 줄었다.</p>
  <p class="pe-ex__uz">Chiqindi paketini pullik qilish bilan chiqindi
  ancha kamaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">매일 십 분씩 <span class="pe-hl pe-hl--o">읽음으로써</span>
     그는 일 년에 이십 권을 읽었다.</p>
  <p class="pe-ex__uz">Har kuni oʻn daqiqadan oʻqish bilan u yiliga
  yigirmata kitob oʻqidi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu qolip juda tabiiy chiqadi.</b>
  “Gaplash<b>ish bilan</b>”, “kamaytir<b>ish orqali</b>”,
  “oʻqi<b>sh yoʻli bilan</b>”. Eʼtibor bering — bizda ham feʼl
  <em>otga aylanadi</em> (“gaplashmoq” → “gaplashish”) va keyin
  “bilan / orqali / yoʻli bilan” qoʻshiladi. Koreyschada ham
  aynan shu ikki qadam: <b>대화하다 → 대화함 → 대화함으로써</b>.
  Shuning uchun bu qolipni yodlash shart emas — oʻzbekcha jumlani
  ikki qadamga boʻlsangiz, koreyschasi chiqadi.</p>
</div>

<h3>2. 로써 va 로서 — bir harf, butunlay boshqa maʼno</h3>

<p>Koreyslar ham baʼzan adashadigan juftlik. Farqni bir marta
tushunib olsangiz, boshqa unutmaysiz.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)로<b>써</b> — ASBOB</p>
    <p><b>써 ← 쓰다</b> (“ishlatmoq”). Demak: <em>nima bilan?</em></p>
    <p><small>대화로<b>써</b> 문제를 해결했다.</small></p>
    <p><small>Suhbat <em>vosita</em> — u bilan ish bajarildi.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)로<b>서</b> — OʻRIN</p>
    <p><b>서 ← 서다</b> (“turmoq”). Demak: <em>kim sifatida?</em></p>
    <p><small>학생으로<b>서</b> 열심히 공부해야 한다.</small></p>
    <p><small>“Oʻquvchi <em>sifatida</em>” — maqom.</small></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">친구<span class="pe-hl pe-hl--s">로서</span>
     하는 말이다. 그냥 걱정할 뿐이다.</p>
  <p class="pe-ex__uz">Doʻst sifatida aytyapman. Shunchaki
  xavotirdaman, xolos.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Esda saqlash ilgagi:</b><br>
  <b>써</b> — “<b>쓰</b>다” = <em>ishlatmoq</em> → <b>asbob</b>,
  vosita, usul.<br>
  <b>서</b> — “<b>서</b>다” = <em>turmoq</em> → <b>oʻrin</b>, maqom,
  rol.<br>
  Savol bilan tekshiring: <em>nima bilan?</em> → 로써.
  <em>kim sifatida?</em> → 로서.</p>
</div>

<h3>3. (으)로 va (으)ㅁ으로써 — nima farqi bor?</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Nima bilan</th><th>Uslub</th><th>Misol</th></tr>
  <tr><td class="pk-stem">(으)로 <small>PK-14</small></td>
      <td>oddiy, moddiy asbob</td><td class="pk-uz">kundalik</td>
      <td>연필로 썼어요.</td></tr>
  <tr><td class="pk-stem">(으)로써</td>
      <td>mavhum vosita (ot)</td><td class="pk-uz">rasmiy</td>
      <td>대화로써 해결했다.</td></tr>
  <tr><td class="pk-stem">(으)ㅁ으로써</td>
      <td><b>harakatning oʻzi</b> vosita</td><td class="pk-uz">rasmiy yozma</td>
      <td>대화함으로써 해결했다.</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bu qolip TOPIK 쓰기 51–54 ning tili.</b> Grafik yoki
  jadval tahlilida “<em>nima qilish bilan natija oʻzgardi</em>”
  degan gap juda koʻp kerak boʻladi:
  <b>정책을 시행함으로써 … 이/가 감소하였다</b>. Uni yodlab qoʻysangiz,
  bir necha bandni tayyor holda yozasiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>학생으로써 열심히 공부해야 한다.</s></p>
  <p class="pe-good">학생<b>으로서</b> 열심히 공부해야 한다.</p>
  <p><small>“Oʻquvchi <b>sifatida</b>” — maqom, demak
  <b>로서</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>대화하음으로써 문제를 해결했다.</s></p>
  <p class="pe-good"><b>대화함으로써</b> 문제를 해결했다.</p>
  <p><small>하다 → <b>함</b>. ❌ 하음 degan shakl yoʻq.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>친구한테 “대화함으로써 풀자”라고 했어요.</s></p>
  <p class="pe-good">친구한테 “<b>얘기해서</b> 풀자”라고 했어요.</p>
  <p><small>(으)ㅁ으로써 — <b>rasmiy yozma</b> til. Kundalik gapda
  oddiy <b>아/어서</b> (PK-35) yetarli.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>읽는 것으로써 실력이 늘었다.</s></p>
  <p class="pe-good"><b>읽음으로써</b> 실력이 늘었다.</p>
  <p><small>Bu qolipda <b>(으)ㅁ</b> ishlatiladi — 는 것 emas.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 우리는
  <span class="pe-blank"></span> 문제를 해결했다. (대화하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>대화함으로써</b> — 하다 → 함 + 으로써.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 매일 십 분씩
  <span class="pe-blank"></span> 실력이 늘었다. (읽다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>읽음으로써</b> — 받침 bor → 음 + 으로써.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 로써 yoki 로서?
  “Oʻquvchi sifatida qattiq oʻqishim kerak.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>로서</b> — maqom: 학생<b>으로서</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 로써 yoki 로서?
  “Suhbat yoʻli bilan hal qildik.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>로써</b> — vosita: 대화<b>로써</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> <b>써</b> va <b>서</b> ni
  qaysi feʼllar yordamida eslab qolamiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>써 ← 쓰다</b> (ishlatmoq) = asbob ·
    <b>서 ← 서다</b> (turmoq) = oʻrin.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Nega
  <s>대화하음으로써</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>하 da 받침 yoʻq, shuning uchun 음 emas, <b>ㅁ</b>
    qoʻshiladi: <b>함</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> “Chiqindi paketini pullik
  qilish bilan chiqindi kamaydi” — koreyschada (한다체).</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>쓰레기봉투를 유료화함으로써 쓰레기가 줄었다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㅁ으로써</b> — …ish yoʻli bilan</li>
  <li><b>(으)로서</b> — … sifatida</li>
  <li><b>대화하다</b> — suhbatlashmoq</li>
  <li><b>해결하다</b> — hal qilmoq</li>
  <li><b>줄이다 / 줄다</b> — kamaytirmoq / kamaymoq</li>
  <li><b>유료화하다</b> — pullik qilmoq</li>
  <li><b>시행하다</b> — joriy qilmoq</li>
  <li><b>정책</b> — siyosat, chora</li>
  <li><b>감소하다</b> — kamaymoq (rasmiy)</li>
  <li><b>방식</b> — usul, yoʻl</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㅁ으로써</b> = “…ish yoʻli bilan”. Rasmiy yozma
      til.</li>
    <li>Ikki qadam: feʼl → <b>(으)ㅁ</b> → <b>으로써</b>.</li>
    <li>하다 → <b>함</b>, 읽다 → <b>읽음</b>. ❌ 하음.</li>
    <li><b>써 ← 쓰다</b> = asbob · <b>서 ← 서다</b> = oʻrin.</li>
    <li>Savol bilan tekshiring: <em>nima bilan?</em> → 로써 ·
      <em>kim sifatida?</em> → 로서.</li>
    <li>Kundalik gapda oddiy <b>아/어서</b> yetarli — bu qolip
      qogʻoz uchun.</li>
    <li>TOPIK 쓰기 da grafik tahlilining tayyor jumlasi:
      <b>…함으로써 …이/가 감소하였다</b>.</li>
    <li>Oʻzbekcha juftligi: “<b>…ish bilan / orqali</b>”.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-87
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-87: (으)ㄹ 지경이다 — chidab boʻlmas holat va chegara",
        "category": "korean",
        "order": 87,
        "summary": (
            "“Ochlikdan oʻlay deb turibman” — chegaraga yetgan holatni "
            "aytish. Block G ning boshi."
        ),
        "stories": ["이사하는 날"],
        "content": """
<h2>PK-87: (으)ㄹ 지경이다 — chidab boʻlmas holat va chegara</h2>

<p>Ertalabdan beri hech narsa yemadingiz. Kimdir soʻraydi:
“Ochsizmi?” Siz “ha” demaysiz. Siz aytasiz: <em>“Ochlikdan oʻlay deb
turibman.”</em> Bu — oddiy “och” emas. Bu <b>chegara</b>: bir qadam
qolgan. Koreys tilida shu chegaraning nomi bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ 지경이다</b> bilan chegaraga yetgan holatni aytasiz</li>
    <li>Nega u deyarli har doim <b>yomon</b> holat ekanini bilib olasiz</li>
    <li>Tayyor iboralarni oʻrganasiz: <b>죽을 지경, 미칠 지경</b></li>
    <li>Uni PK-82 dagi <b>(으)ㄹ 정도로</b> dan ajratasiz</li>
    <li><b>이 지경이 되다</b> iborasini oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">aniqlovchi (으)ㄹ</span>
  <span class="pe-chip pe-chip--neg">지경이다</span>
  <span class="pe-chip pe-chip--adv">= …ay deb turibman</span>
</div>

<h3>1. 지경 nima degani?</h3>

<p><b>지경</b> — hanzuviy soʻz: <b>地境</b>, yaʼni “yer chegarasi”.
Demak <b>(으)ㄹ 지경이다</b> soʻzma-soʻz “<em>… boʻladigan chegarada
turibman</em>”. Hali sodir boʻlmagan — lekin bir qadam qolgan.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">배가 고파서 <span class="pe-hl pe-hl--neg">쓰러질
     지경이에요</span>.</p>
  <p class="pe-ex__uz">Ochlikdan yiqilay deb turibman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">일이 너무 많아서 <span class="pe-hl pe-hl--neg">미칠
     지경이다</span>.</p>
  <p class="pe-ex__uz">Ish shunchalik koʻpki, aqldan ozay deyapman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">사흘 동안 못 자서 <span class="pe-hl pe-hl--neg">죽을
     지경이었다</span>.</p>
  <p class="pe-ex__uz">Uch kun uxlamay, oʻlgudek holga tushdim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu qolipning aniq jufti bor: “-ay deb
  turibman”.</b> “Oʻl<b>ay deb turibman</b>”, “yiqil<b>ay deb
  turibman</b>”, “yigʻlab yubor<b>ay dedim</b>”. Ikkala tilda ham
  <em>ish hali boʻlmagan</em> — faqat unga bir qadam qolgan. Va
  ikkalasida ham bu <b>shikoyat</b> ohangi: “ahvolim shu darajaga
  yetdi”. Yana bir jufti — “<b>…gudek holga tushdim</b>”.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>(으)ㄹ 지경이다 ning uch xususiyati:</b><br>
  1. Holat deyarli har doim <b>yomon</b>: 죽다, 미치다, 쓰러지다,
  울다, 굶다.<br>
  2. Oldida koʻpincha sabab turadi — <b>아/어서</b> (PK-35) yoki
  <b>(으)니까</b> (PK-48).<br>
  3. Bu <b>soʻzlovchining oʻz holati</b>. Boshqa haqida gapirilsa,
  hamdardlik ohangi boʻladi.</p>
</div>

<h3>2. Tayyor iboralar</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Ibora</th><th>Soʻzma-soʻz</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pk-stem">죽을 지경이다</td><td class="pk-end">oʻlish chegarasida</td>
      <td class="pk-uz">oʻlay deb turibman</td></tr>
  <tr><td class="pk-stem">미칠 지경이다</td><td class="pk-end">aqldan ozish chegarasida</td>
      <td class="pk-uz">aqldan ozay deyapman</td></tr>
  <tr><td class="pk-stem">쓰러질 지경이다</td><td class="pk-end">yiqilish chegarasida</td>
      <td class="pk-uz">yiqilay deb turibman</td></tr>
  <tr><td class="pk-stem">울 지경이다</td><td class="pk-end">yigʻlash chegarasida</td>
      <td class="pk-uz">yigʻlab yuboray dedim</td></tr>
</table></div>

<h3>3. 이 지경이 되다 — “shu holga kelmoq”</h3>

<p><b>지경</b> mustaqil ot ham. <b>이 지경</b> = “bu ahvol”.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">어쩌다가 <span class="pe-hl pe-hl--o">이 지경이
     되었을까</span> 생각했다.</p>
  <p class="pe-ex__uz">Qanday qilib shu ahvolga tushdik ekan, deb
  oʻyladim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">집이 <span class="pe-hl pe-hl--o">이 지경이</span>
     될 때까지 아무도 몰랐다.</p>
  <p class="pe-ex__uz">Uy shu ahvolga kelguncha hech kim bilmadi.</p>
</div>

<h3>4. 정도로 va 지경이다 — juda yaqin, lekin bir xil emas</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)ㄹ 정도로 <small>PK-82</small></p>
    <p><b>Darajani oʻlchaydi</b> va <em>gap oʻrtasida</em> turadi.
    Yaxshi ham, yomon ham boʻladi.</p>
    <p><small>배가 아플 정도로 <b>웃었어요</b>.</small></p>
    <p><small>“Qornim ogʻriydigan darajada kuldim.”</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)ㄹ 지경이다</p>
    <p><b>Holatni aytadi</b> va <em>gapning oxirida</em> turadi.
    Deyarli har doim yomon.</p>
    <p><small>배가 고파서 <b>죽을 지경이에요</b>.</small></p>
    <p><small>“Ochlikdan oʻlay deb turibman.”</small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Oson tekshiruv:</b> gapdan keyin yana feʼl bormi?<br>
  Bor → <b>정도로</b> (u oʻsha feʼlni oʻlchaydi).<br>
  Yoʻq, gap shu bilan tugadi → <b>지경이다</b>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>배가 고파서 죽은 지경이에요.</s></p>
  <p class="pe-good">배가 고파서 <b>죽을 지경이에요</b>.</p>
  <p><small>지경 oldida <b>(으)ㄹ</b> — hali boʻlmagan holat.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>너무 기뻐서 춤출 지경이에요.</s></p>
  <p class="pe-good">너무 기뻐서 <b>춤출 정도로</b> 좋았어요.</p>
  <p><small>지경 — <b>yomon</b> holat uchun. Quvonch uchun
  <b>정도로</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>죽을 지경으로 배가 고파요.</s></p>
  <p class="pe-good">배가 고파서 <b>죽을 지경이에요</b>.</p>
  <p><small>지경 gapning <b>oxirida</b>, 이다 bilan turadi —
  oʻrtasida emas.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>사흘 동안 못 자서 죽는 지경이었다.</s></p>
  <p class="pe-good">사흘 동안 못 자서 <b>죽을 지경이었다</b>.</p>
  <p><small>는 emas — hamisha <b>(으)ㄹ</b>.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 배가 고파서
  <span class="pe-blank"></span> 지경이에요. (쓰러지다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>쓰러질</b> — 지경 oldida (으)ㄹ.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 일이 너무 많아서
  <span class="pe-blank"></span> 지경이다. (미치다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>미칠</b> — <b>미칠 지경이다</b> tayyor ibora.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> <b>지경</b> (地境) ning
  soʻzma-soʻz maʼnosi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>“<b>Yer chegarasi</b>”. Shuning uchun qolip “… boʻladigan
    chegarada turibman” degani.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Nega
  <s>너무 기뻐서 춤출 지경이에요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>지경 <b>yomon</b> holat uchun. Quvonch uchun —
    <b>춤출 정도로 좋았어요</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> 정도로 yoki 지경이다?
  “Qornim ogʻriydigan darajada kuldim.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>정도로</b> — keyin yana feʼl bor (웃었어요):
    배가 아플 <b>정도로</b> 웃었어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Uch kun uxlamay, oʻlgudek
  holga tushdim” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>사흘 동안 못 자서 죽을 지경이었어요.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> <b>이 지경이 되다</b> nimani
  bildiradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>“<b>Shu ahvolga kelmoq</b>”. 지경 bu yerda mustaqil ot —
    “ahvol, holat”.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ 지경이다</b> — …ay deb turibman</li>
  <li><b>지경</b> — chegara, ahvol</li>
  <li><b>쓰러지다</b> — yiqilmoq</li>
  <li><b>미치다</b> — aqldan ozmoq</li>
  <li><b>굶다</b> — och qolmoq</li>
  <li><b>어쩌다가</b> — qanday qilib, tasodifan</li>
  <li><b>참다</b> — chidamoq</li>
  <li><b>한계</b> — chegara, limit</li>
  <li><b>겨우</b> — zoʻrgʻa</li>
  <li><b>정신이 없다</b> — boshi qotgan boʻlmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ 지경이다</b> = “…ay deb turibman” — chegaraga
      yetgan holat.</li>
    <li><b>地境</b> = “yer chegarasi”. Ish hali boʻlmagan, bir
      qadam qolgan.</li>
    <li>Holat deyarli har doim <b>yomon</b>.</li>
    <li>Oldida <b>(으)ㄹ</b>, hech qachon 는 yoki (으)ㄴ emas.</li>
    <li>Tayyor iboralar: <b>죽을 · 미칠 · 쓰러질 · 울 지경이다</b>.</li>
    <li>Koʻpincha sabab bilan yuradi: <b>아/어서 … 지경이다</b>.</li>
    <li>정도로 = gap <b>oʻrtasida</b>, darajani oʻlchaydi ·
      지경이다 = gap <b>oxirida</b>, holatni aytadi.</li>
    <li><b>이 지경이 되다</b> = “shu ahvolga kelmoq”.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-88
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-88: (으)ㄹ 리가 없다 / (으)ㄹ 턱이 없다 — kuchli shubha va inkor",
        "category": "korean",
        "order": 88,
        "summary": (
            "“U yolgʻon gapirishi mumkin emas” — imkonsizlikni emas, "
            "ishonmaslikni aytish. Ishonch zinapoyasining eng pastki "
            "pogʻonasi."
        ),
        "stories": ["사람들이 믿지 않았던 것들"],
        "content": """
<h2>PK-88: (으)ㄹ 리가 없다 / (으)ㄹ 턱이 없다 — kuchli shubha va inkor</h2>

<p>Kimdir sizga aytdi: “Doʻstingiz sizni aldadi.” Siz bir soniya ham
oʻylamay javob berasiz: <em>“Yoʻq, uning bunday qilishi mumkin
emas.”</em> Siz “u qila olmaydi” demadingiz — u qila oladi. Siz
<b>ishonmadingiz</b>. Bu ikkovi butunlay boshqa narsa, va koreys tilida
ular boshqa qolip bilan aytiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ 리가 없다</b> bilan kuchli ishonmaslikni aytasiz</li>
    <li>Uni <b>(으)ㄹ 수 없다</b> dan ajratasiz — bu eng muhimi</li>
    <li>Ogʻzaki <b>(으)ㄹ 턱이 없다</b> ni oʻrganasiz</li>
    <li>PK-73 dagi ishonch zinapoyasini <b>oxirigacha</b> toʻldirasiz</li>
    <li>Oʻtgan zamon shaklini tuzasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">aniqlovchi (으)ㄹ</span>
  <span class="pe-chip pe-chip--neg">리가 없다</span>
  <span class="pe-chip pe-chip--adv">= …ishi mumkin emas</span>
</div>

<h3>1. 리 nima degani?</h3>

<p><b>리</b> — hanzuviy <b>理</b>: “aql, mantiq, sabab”. Demak
<b>(으)ㄹ 리가 없다</b> = “<em>bunday boʻlishining mantigʻi yoʻq</em>”.
Siz dalilga emas, <b>aqlga</b> tayanyapsiz.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그 사람이 거짓말을 <span class="pe-hl pe-hl--neg">할
     리가 없어요</span>.</p>
  <p class="pe-ex__uz">U odamning yolgʻon gapirishi mumkin emas.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 시간에 문을 <span class="pe-hl pe-hl--neg">열었을
     리가 없다</span>.</p>
  <p class="pe-ex__uz">Bu vaqtda ochilgan boʻlishi mumkin emas.</p>
  <p class="pe-ex__why">Oʻtgan zamon — <b>았/었을 리가 없다</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아프소나 씨가 시험에 <span class="pe-hl pe-hl--neg">떨어질
     리가 없어요</span>. 매일 공부했잖아요.</p>
  <p class="pe-ex__uz">Afsonaning imtihondan yiqilishi mumkin emas.
  Axir u har kuni oʻqigan-ku.</p>
  <p class="pe-ex__why">PK-55 dagi <b>잖아요</b> bilan juda yaxshi
  yuradi — ikkalasi ham dalilga ishora qiladi.</p>
</div>

<h3>2. 을 수 없다 va 을 리가 없다 — eng muhim farq</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)ㄹ 수 없다 <small>PK-30</small></p>
    <p><b>Imkoni yoʻq.</b> Fizik yoki sharoit toʻsigʻi.</p>
    <p><small>그 사람이 올 수 없어요.</small></p>
    <p><small>“U kela olmaydi” — kasal, band, yoʻli yoʻq.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)ㄹ 리가 없다</p>
    <p><b>Ishonmayman.</b> Imkon bor, lekin men buni
    haqiqat deb qabul qilmayman.</p>
    <p><small>그 사람이 올 리가 없어요.</small></p>
    <p><small>“U keladi deb oʻylamayman” — undan
    kutilmaydi.</small></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ikkalasi ham “mumkin emas” deb tarjima
  qilinadi</b> — shuning uchun bu yerda adashish oson. Lekin
  bizda ham farq bor, faqat boshqa soʻzlar bilan:
  “kel<b>a olmaydi</b>” (imkon yoʻq — 수 없다) va
  “kel<b>ishi mumkin emas</b> / <b>hech qachon kelmasdi</b>”
  (ishonmayman — 리가 없다). Eng aniq oʻzbekcha jufti —
  suhbatdagi bitta soʻz: <b>“Qayoqda!”</b> Aynan shu ohang
  <b>(으)ㄹ 리가 없어요</b> da bor.</p>
</div>

<h3>3. Ishonch zinapoyasi — toʻliq</h3>

<p>PK-73 da siz taxminlarni tizib chiqqan edingiz. Endi
zinapoyaning <b>eng pastki pogʻonasi</b> ham bor.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Ishonch</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pk-stem">(으)ㄹ 거예요 <small>PK-27</small></td>
      <td>yuqori</td><td class="pk-uz">…adi</td></tr>
  <tr><td class="pk-stem">(으)ㄹ 테니까 <small>PK-64</small></td>
      <td>yuqori</td><td class="pk-uz">…sa kerak</td></tr>
  <tr><td class="pk-stem">(으)ㄹ 것 같다 <small>PK-52</small></td>
      <td>oʻrtacha</td><td class="pk-uz">…ga oʻxshaydi</td></tr>
  <tr><td class="pk-stem">(으)ㄹ지도 모르다 <small>PK-73</small></td>
      <td>past</td><td class="pk-uz">balki …ar</td></tr>
  <tr><td class="pk-stem">(으)ㄹ 리가 없다</td>
      <td><b>nol — teskari tomon</b></td><td class="pk-uz">…ishi mumkin emas</td></tr>
</table></div>

<h3>4. (으)ㄹ 턱이 없다 — ogʻzaki va keskin</h3>

<p><b>턱</b> — bu hanzuviy emas, sof koreyscha soʻz: “asos, sabab”.
Maʼnosi 리가 없다 bilan bir xil, lekin <b>keskinroq</b> va
<b>ogʻzaki</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그런 이야기를 그 사람이 <span class="pe-hl pe-hl--neg">알
     턱이 없어요</span>.</p>
  <p class="pe-ex__uz">Bunday gapni u odam bilishiga aql bovar
  qilmaydi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>턱이 없다 ohangi qattiq.</b> Unda bir oz “bu kulgili
  gap” degan soya bor. Shuning uchun uni <b>oʻzidan kattaga</b>
  yoki rasmiy vaziyatda ishlatmang — u yerda
  <b>리가 없다</b> yoki oddiy <b>아닐 것이다</b>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>그 사람이 거짓말을 하는 리가 없어요.</s></p>
  <p class="pe-good">그 사람이 거짓말을 <b>할 리가 없어요</b>.</p>
  <p><small>리 oldida hamisha <b>(으)ㄹ</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>다리가 아파서 걸을 리가 없어요.</s></p>
  <p class="pe-good">다리가 아파서 <b>걸을 수 없어요</b>.</p>
  <p><small>Bu <b>imkonsizlik</b> — 수 없다. 리가 없다 esa
  ishonmaslik.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>이 시간에 문을 열 리가 없었어요.</s>
    <small>(“ochilgan boʻlishi mumkin emas” maʼnosida)</small></p>
  <p class="pe-good">이 시간에 문을 <b>열었을 리가 없어요</b>.</p>
  <p><small>Oʻtgan zamon <b>았/었을</b> ichida — 없다 da
  emas.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>선생님이 그런 말을 할 턱이 없습니다.</s></p>
  <p class="pe-good">선생님이 그런 말을 <b>할 리가 없습니다</b>.</p>
  <p><small>턱이 없다 — keskin va ogʻzaki. Rasmiy vaziyatda
  <b>리가 없다</b>.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 그 사람이 거짓말을
  <span class="pe-blank"></span> 리가 없어요. (하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>할</b> — 리 oldida (으)ㄹ.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 이 시간에 문을
  <span class="pe-blank"></span> 리가 없다. (열다 — oʻtgan zamon)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>열었을</b> — 았/었을 리가 없다.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 수 없다 yoki 리가 없다?
  “Oyogʻi ogʻriydi, shuning uchun yura olmaydi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>수 없다</b> — haqiqiy imkonsizlik:
    걸을 <b>수 없어요</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 수 없다 yoki 리가 없다?
  “U keladi deb oʻylamayman — undan kutilmaydi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>리가 없다</b> — imkon bor, lekin ishonmayman:
    올 <b>리가 없어요</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> <b>리</b> (理) ning maʼnosi
  nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>“<b>Aql, mantiq, sabab</b>”. Shuning uchun qolip “bunday
    boʻlishining mantigʻi yoʻq” degani.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Ishonch zinapoyasida
  <b>리가 없다</b> qayerda turadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Eng pastda — hatto <b>(으)ㄹ지도 모르다</b> dan ham past.
    U taxmin emas, <b>rad</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Bu gapni 한다체 ga oʻgiring
  (PK-74): 그 사람이 거짓말을 할 리가 없어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>그 사람이 거짓말을 할 리가 없다.</b> 없다 oʻzgarmaydi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ 리가 없다</b> — …ishi mumkin emas</li>
  <li><b>(으)ㄹ 턱이 없다</b> — shu maʼno, keskin va ogʻzaki</li>
  <li><b>거짓말</b> — yolgʻon</li>
  <li><b>속이다</b> — aldamoq</li>
  <li><b>사실</b> — haqiqat, fakt</li>
  <li><b>증거</b> — dalil</li>
  <li><b>의심하다</b> — shubhalanmoq</li>
  <li><b>당연하다</b> — tabiiy, albatta shunday</li>
  <li><b>말도 안 되다</b> — aql bovar qilmaydi</li>
  <li><b>믿다</b> — ishonmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ 리가 없다</b> = “…ishi mumkin emas” — kuchli
      ishonmaslik.</li>
    <li><b>理</b> = aql, mantiq. Siz dalilga emas, mantiqqa
      tayanasiz.</li>
    <li><b>수 없다 = imkoni yoʻq</b> · <b>리가 없다 = ishonmayman</b>.
      Bu darsning eng muhim farqi.</li>
    <li>Oʻtgan zamon <b>았/었을 리가 없다</b> ichida.</li>
    <li>Oldida hamisha <b>(으)ㄹ</b> — 는 yoki (으)ㄴ emas.</li>
    <li><b>턱이 없다</b> — bir xil maʼno, keskin va ogʻzaki.
      Kattaga aytilmaydi.</li>
    <li>Ishonch zinapoyasi endi toʻliq: 거예요 → 테니까 → 것 같다 →
      을지도 모르다 → <b>리가 없다</b>.</li>
    <li>Oʻzbekcha jufti — bitta soʻz: “<b>Qayoqda!</b>”</li>
  </ul>
</div>
""",
    },
]
