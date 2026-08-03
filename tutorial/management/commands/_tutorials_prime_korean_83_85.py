# -*- coding: utf-8 -*-
"""Prime Korean — Block F, darslar 83–85.

83. 에 불과하다, (으)ㄹ 따름이다, (으)ㄹ 뿐이다 — "shunchaki"
84. 든지 든지, 건 건 — tanlovdan qatʼi nazar
85. (느)니 차라리, (으)나 마나 — yaxshiroq muqobil va befoyda ish

Uchtasi ham TANLOV va CHEGARA haqida:
  83 — “bundan ortigʻi yoʻq”  (chegarani pastga qoʻyish)
  84 — “qaysi biri boʻlsa ham farqi yoʻq”  (tanlovni bekor qilish)
  85 — “u emas, bu yaxshiroq” va “qilsa ham, qilmasa ham bir xil”

Oʻzbekcha kalitlar:
  (으)ㄹ 뿐이다     = "faqat …, xolos"
  (으)ㄹ 따름이다   = "…dan oʻzga hech narsa emas"  (kitobiy, his-tuygʻu)
  명사 + 에 불과하다 = "bor-yoʻgʻi …, …dan iborat xolos"  (baho, rad)
  든지 … 든지      = "xoh …, xoh …"  /  "…mi, …mi — baribir"
  건 … 건         = shu maʼno, qisqaroq va ogʻzaki
  (느)니 차라리     = "…gandan koʻra … yaxshiroq"
  (으)나 마나      = "qilsa ham, qilmasa ham bir xil"

Ikki YANGI kichik qolip yoʻl-yoʻlakay beriladi (tocda alohida dars yoʻq,
lekin ularsiz asosiy mavzuni tushuntirib boʻlmaydi):
  * PK-84 da **거나** — “yoki” (든지 ni unga qarshi qoʻyish uchun).
  * PK-83 da **뿐** ning yakka holdagi ishlatilishi — PK-67 da u faqat
    뿐만 아니라 ichida uchragan edi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_83_85.py --author=prime
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
    # PK-83
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-83: 에 불과하다, (으)ㄹ 따름이다, (으)ㄹ 뿐이다 — “shunchaki”",
        "category": "korean",
        "order": 83,
        "summary": (
            "“Men shunchaki ishimni qildim, xolos” va “bu bor-yoʻgʻi "
            "bahona” — kamtarlik ham, rad ham bitta fikrdan chiqadi."
        ),
        "stories": ["삼 초"],
        "content": """
<h2>PK-83: 에 불과하다, (으)ㄹ 따름이다, (으)ㄹ 뿐이다 — “shunchaki”</h2>

<p>Kimdir sizga rahmat aytdi. Siz nima deysiz? — <em>“Men faqat oʻz
ishimni qildim, xolos.”</em> Yoki kimdir bahona keltirdi va siz
oʻylaysiz: <em>“Bu bor-yoʻgʻi bahona.”</em> Ikkala gapda ham bir fikr
bor: <b>bundan ortigʻi yoʻq</b>. Bugun shu fikrning uchta shakli.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ 뿐이다</b> bilan “faqat …, xolos” deysiz</li>
    <li>PK-67 dagi <b>뿐만 아니라</b> bilan bogʻlaysiz</li>
    <li>Kitobiy <b>(으)ㄹ 따름이다</b> ni oʻrganasiz</li>
    <li><b>명사 + 에 불과하다</b> bilan baho berasiz</li>
    <li>Uchtasini PK-16 dagi <b>만</b> dan ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch shakl</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ 뿐이다</span>
  <span class="pe-chip pe-chip--aux">(으)ㄹ 따름이다</span>
  <span class="pe-chip pe-chip--o">에 불과하다</span>
</div>

<h3>1. (으)ㄹ 뿐이다 — eng koʻp ishlatiladigani</h3>

<p><b>뿐</b> — “boshqasi yoʻq” degan ot. Siz uni PK-67 da
<b>(으)ㄹ 뿐만 아니라</b> ichida koʻrgansiz. Endi u yakka holda,
gapning oxirida turadi.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">Feʼl / sifat</p>
    <p class="pk-batchim__form">aniqlovchi + <span class="pk-par">뿐이다</span></p>
    <p>웃다 → 웃을 뿐이다</p>
    <p>기다리다 → 기다릴 뿐이다</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">Ot</p>
    <p class="pk-batchim__form">ot + <span class="pk-par">일 뿐이다</span></p>
    <p>학생 → 학생일 뿐이다</p>
    <p>농담 → 농담일 뿐이다</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 제 일을 <span class="pe-hl pe-hl--v">했을
     뿐이에요</span>.</p>
  <p class="pe-ex__uz">Men faqat oʻz ishimni qildim, xolos.</p>
  <p class="pe-ex__why">Oʻtgan zamon <b>았/었을 뿐이다</b> shaklida.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그 사람은 아무 말도 없이 <span class="pe-hl pe-hl--v">웃을
     뿐이었어요</span>.</p>
  <p class="pe-ex__uz">U odam hech narsa demay, faqat kulardi, xolos.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그건 <span class="pe-hl pe-hl--s">농담일 뿐이에요</span>.
     화내지 마세요.</p>
  <p class="pe-ex__uz">Bu shunchaki hazil. Jahlingiz chiqmasin.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu qolipning aniq jufti bor: “xolos”.</b>
  “Bir marta koʻrdim, <b>xolos</b>”, “men aytdim, <b>xolos</b>”.
  Eʼtibor bering — “xolos” ham gapning <em>oxirida</em> turadi,
  xuddi 뿐이다 kabi, va ikkalasi ham <em>kamaytirib koʻrsatish</em>
  vazifasini bajaradi. Yana bir jufti — “<b>bor-yoʻgʻi</b>”, lekin u
  gapning boshida keladi. Shuning uchun oʻzbekcha “men bor-yoʻgʻi
  ishimni qildim” = koreyscha “제 일을 <b>했을 뿐이에요</b>”.</p>
</div>

<h3>2. 만 va 뿐이다 — nima farqi bor?</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">만 <small>PK-16</small></p>
    <p><b>Tanlaydi.</b> Boshqalar orasidan bittasini ajratadi.</p>
    <p><small>저는 커피<b>만</b> 마셔요.</small></p>
    <p><small>(choy ham bor, sut ham — men kofe tanlayman)</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)ㄹ 뿐이다</p>
    <p><b>Kamaytiradi.</b> “Bundan ortigʻi yoʻq” deydi.</p>
    <p><small>저는 커피를 마셨<b>을 뿐이에요</b>.</small></p>
    <p><small>(boshqa hech narsa qilmadim — ayblamang)</small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p>Ikkalasini <b>birga</b> ham ishlatish mumkin va bu juda tabiiy:
  <b>저는 커피만 마셨을 뿐이에요</b> — “men faqat kofe ichdim,
  xolos”. 만 tanlaydi, 뿐이다 esa “boshqa hech narsa yoʻq” deb
  yopadi.</p>
</div>

<h3>3. (으)ㄹ 따름이다 — kitobiy va his-tuygʻuli</h3>

<p>Maʼnosi 뿐이다 bilan bir xil, lekin uslubi boshqa: bu
<b>yozma va rasmiy</b> til. Va u koʻpincha <b>soʻzlovchining oʻz
his-tuygʻusi</b> haqida boʻladi — minnatdorchilik, hayrat,
uyalish.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">도와주셔서 <span class="pe-hl pe-hl--aux">감사할
     따름입니다</span>.</p>
  <p class="pe-ex__uz">Yordam berganingiz uchun minnatdorman, xolos.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그 소식을 듣고 <span class="pe-hl pe-hl--aux">놀랄
     따름이었다</span>.</p>
  <p class="pe-ex__uz">Bu xabarni eshitib, hayratdan boshqa hech narsa
  qolmadi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>따름이다 ni kundalik suhbatda ishlatmang.</b> U rasmiy
  nutq, maqola va rasmiy xatning tili. Doʻstingizga
  <s>배고플 따름이야</s> desangiz, kulishadi. Kundalik gapda —
  <b>뿐이다</b>.</p>
</div>

<h3>4. 명사 + 에 불과하다 — “bor-yoʻgʻi …”</h3>

<p>Bu uchinchisi boshqacha ishlaydi: u <b>otga</b> qoʻshiladi va
<b>baho beradi</b> — koʻpincha kamsituvchi yoki rad etuvchi ohangda.
<b>불과</b> (不過) = “oshib ketmaydi”.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그것은 <span class="pe-hl pe-hl--o">변명에
     불과하다</span>.</p>
  <p class="pe-ex__uz">Bu bor-yoʻgʻi bahona.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이것은 <span class="pe-hl pe-hl--o">시작에
     불과하다</span>.</p>
  <p class="pe-ex__uz">Bu hali boshlanishi xolos.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그때 그는 <span class="pe-hl pe-hl--o">열 살에
     불과했다</span>.</p>
  <p class="pe-ex__uz">Oʻshanda u bor-yoʻgʻi oʻn yoshda edi.</p>
  <p class="pe-ex__why"><b>Raqam</b> bilan juda koʻp ishlatiladi.</p>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Nimaga qoʻshiladi</th><th>Ohangi</th><th>Uslubi</th></tr>
  <tr><td class="pk-stem">(으)ㄹ 뿐이다</td><td>feʼl · sifat · ot</td>
      <td>kamtarlik, oqlanish</td><td class="pk-uz">kundalik</td></tr>
  <tr><td class="pk-stem">(으)ㄹ 따름이다</td><td>koʻpincha his-tuygʻu</td>
      <td>samimiy, tantanali</td><td class="pk-uz">rasmiy yozma</td></tr>
  <tr><td class="pk-stem">에 불과하다</td><td><b>faqat ot</b></td>
      <td>baho, rad, kamsitish</td><td class="pk-uz">yozma</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>그건 농담 뿐이에요.</s></p>
  <p class="pe-good">그건 <b>농담일 뿐이에요</b>.</p>
  <p><small>Ot bilan <b>일</b> kerak: 이다 ning aniqlovchi
  shakli.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그것은 변명일 뿐과하다.</s></p>
  <p class="pe-good">그것은 <b>변명에 불과하다</b>.</p>
  <p><small>불과하다 ot bilan <b>에</b> orqali ulanadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>저는 제 일을 하을 뿐이에요.</s></p>
  <p class="pe-good">저는 제 일을 <b>했을 뿐이에요</b>.</p>
  <p><small>Boʻlib oʻtgan ish — <b>았/었을 뿐이다</b>.
  ❌ 하을 degan shakl yoʻq.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>친구한테 “배고플 따름이야”라고 했어요.</s></p>
  <p class="pe-good">친구한테 “<b>배고플 뿐이야</b>”라고 했어요.</p>
  <p><small>따름이다 — <b>rasmiy yozma</b>. Doʻst bilan
  gapirganda 뿐이다.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 저는 제 일을
  <span class="pe-blank"></span> 뿐이에요. (하다 — oʻtgan zamon)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>했을</b> — 았/었을 뿐이다.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 그건
  <span class="pe-blank"></span> 뿐이에요. (농담)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>농담일</b> — ot bilan 일 kerak.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Toʻldiring: 그것은 변명
  <span class="pe-blank"></span> 불과하다.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>에</b> — 명사 + <b>에 불과하다</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 만 yoki 뿐이다?
  “Men faqat kofe ichaman” (choy emas, kofe).</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>만</b> — tanlash: 저는 커피<b>만</b> 마셔요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Rasmiy nutqda “minnatdorman,
  xolos” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>감사할 따름입니다.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Bu hali boshlanishi xolos” —
  koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>이것은 시작에 불과하다.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Bu gapni 한다체 ga oʻgiring
  (PK-74): 저는 제 일을 했을 뿐이에요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>나는 내 일을 했을 뿐이다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ 뿐이다</b> — faqat …, xolos</li>
  <li><b>(으)ㄹ 따름이다</b> — …dan oʻzga hech narsa emas (kitobiy)</li>
  <li><b>에 불과하다</b> — bor-yoʻgʻi …</li>
  <li><b>변명</b> — bahona</li>
  <li><b>농담</b> — hazil</li>
  <li><b>화내다</b> — jahli chiqmoq</li>
  <li><b>감사하다</b> — minnatdor boʻlmoq</li>
  <li><b>놀라다</b> — hayron qolmoq</li>
  <li><b>대단하다</b> — ajoyib, katta ish</li>
  <li><b>겸손하다</b> — kamtar boʻlmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ 뿐이다</b> = “faqat …, xolos”. Eng koʻp
      ishlatiladigani.</li>
    <li>Ot bilan <b>일 뿐이다</b>, oʻtgan ish bilan
      <b>았/었을 뿐이다</b>.</li>
    <li><b>만</b> tanlaydi · <b>뿐이다</b> kamaytiradi. Birga ham
      boʻladi: 커피만 마셨을 뿐이에요.</li>
    <li><b>(으)ㄹ 따름이다</b> = bir xil maʼno, <b>rasmiy yozma</b>
      uslub, koʻpincha his-tuygʻu.</li>
    <li><b>명사 + 에 불과하다</b> = “bor-yoʻgʻi …”. Faqat ot bilan,
      koʻpincha raqam bilan.</li>
    <li><b>不過</b> = “oshib ketmaydi” — chegarani belgilaydi.</li>
    <li>뿐 sizga PK-67 dagi <b>뿐만 아니라</b> dan tanish.</li>
    <li>Oʻzbekcha juftlari: “<b>xolos</b>” va
      “<b>bor-yoʻgʻi</b>”.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-84
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-84: 든지 든지, 건 건 — tanlovdan qatʼi nazar",
        "category": "korean",
        "order": 84,
        "summary": (
            "“Xoh borsin, xoh bormasin — menga farqi yoʻq” va "
            "“nima boʻlsa ham mayli” — tanlovni bekor qiluvchi qolip."
        ),
        "stories": ["어떤 언어를 배우든지"],
        "content": """
<h2>PK-84: 든지 든지, 건 건 — tanlovdan qatʼi nazar</h2>

<p>Doʻstingiz soʻradi: “Choy ichasanmi, kofemi?” Siz javob berasiz:
<em>“Xoh choy, xoh kofe — farqi yoʻq.”</em> Ikkita variant bor, lekin
siz ikkalasini ham <b>bekor qilyapsiz</b>: qaysi biri boʻlsa ham
natija bir xil. Koreys tilida bu fikrning oʻz qolipi bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Avval <b>거나</b> ni — oddiy “yoki” ni oʻrganasiz</li>
    <li><b>든지 … 든지</b> bilan “xoh …, xoh …” deysiz</li>
    <li>Soʻroq soʻzlari bilan <b>뭐든지, 누구든지</b> yasaysiz</li>
    <li>Qisqa <b>건 … 건</b> shaklini oʻrganasiz</li>
    <li><b>하든 말든</b> — “qilsin, qilmasin” juftligini tuzasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">A + 든지</span>
  <span class="pe-chip pe-chip--v">B + 든지</span>
  <span class="pe-chip pe-chip--adv">= xoh A, xoh B — baribir</span>
</div>

<h3>1. Avval 거나 — oddiy “yoki”</h3>

<p>Bugungi qolipni tushunish uchun bitta kichik shakl kerak:
<b>거나</b>. U ikki feʼlni “yoki” bilan bogʻlaydi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">주말에는 책을 <span class="pe-hl pe-hl--v">읽거나</span>
     영화를 봐요.</p>
  <p class="pe-ex__uz">Dam olish kunlari kitob oʻqiyman yoki kino
  koʻraman.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Otlar uchun</b> esa PK-16 dan tanish <b>(이)나</b> ishlatiladi:
  커피<b>나</b> 차 (“kofe yoki choy”). <b>거나</b> — feʼl va sifat
  uchun.</p>
</div>

<h3>2. 든지 … 든지 — “xoh …, xoh …”</h3>

<p>Endi asosiy qolip. Farq muhim: <b>거나</b> tanlov beradi,
<b>든지 … 든지</b> esa tanlovning <b>ahamiyati yoʻqligini</b>
aytadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">거나 — TANLOV BOR</p>
    <p>커피를 마시<b>거나</b> 차를 마셔요.</p>
    <p><small>Kofe ichaman yoki choy. Bittasini tanlayman.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">든지 … 든지 — TANLOV BEKOR</p>
    <p>커피를 마시<b>든지</b> 차를 마시<b>든지</b> 상관없어요.</p>
    <p><small>Xoh kofe, xoh choy — farqi yoʻq.</small></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--v">가든지</span>
     <span class="pe-hl pe-hl--v">안 가든지</span> 마음대로 하세요.</p>
  <p class="pe-ex__uz">Xoh boring, xoh bormang — oʻzingiz bilasiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">날씨가 <span class="pe-hl pe-hl--v">좋든지</span>
     <span class="pe-hl pe-hl--v">나쁘든지</span> 우리는 출발한다.</p>
  <p class="pe-ex__uz">Ob-havo yaxshi boʻladimi, yomonmi — biz yoʻlga
  chiqamiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">학생이든지</span>
     <span class="pe-hl pe-hl--s">선생님이든지</span> 규칙은 같아요.</p>
  <p class="pe-ex__uz">Xoh oʻquvchi boʻlsin, xoh oʻqituvchi — qoida
  bir xil.</p>
  <p class="pe-ex__why">Ot bilan <b>(이)든지</b>: 받침 bor →
  이든지, yoʻq → 든지.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu qolipning ikkita aniq jufti bor.</b>
  Birinchisi — “<b>xoh …, xoh …</b>”: <em>“xoh borsin, xoh
  bormasin”</em>. Ikkinchisi — soʻroq shakli bilan takrorlash:
  <em>“yaxshimi, yomonmi — baribir”</em>. Uchinchi yoʻl ham bor:
  “…<b>sa ham</b>, …<b>masa ham</b>” — <em>“borsa ham, bormasa
  ham”</em>. Uchalasi ham koreyschadagi <b>든지 … 든지</b> ga toʻgʻri
  keladi, va uchalasida ham — xuddi koreyschadagidek — <b>ikkinchi
  qism birinchisining inkori</b> boʻlishi juda tabiiy.</p>
</div>

<h3>3. Soʻroq soʻzlari bilan: 뭐든지, 누구든지</h3>

<p>Agar 든지 <b>soʻroq soʻziga</b> qoʻshilsa, u “har qanday” degan
maʼno beradi. Bu juda koʻp ishlatiladi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Soʻroq soʻzi</th><th>+ 든지</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">뭐</td><td class="pk-res">뭐든지</td>
      <td class="pk-uz">nima boʻlsa ham, har narsa</td></tr>
  <tr><td class="pk-stem">누구</td><td class="pk-res">누구든지</td>
      <td class="pk-uz">kim boʻlsa ham, har kim</td></tr>
  <tr><td class="pk-stem">언제</td><td class="pk-res">언제든지</td>
      <td class="pk-uz">qachon boʻlsa ham, istalgan vaqtda</td></tr>
  <tr><td class="pk-stem">어디</td><td class="pk-res">어디든지</td>
      <td class="pk-uz">qayerda boʻlsa ham</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--o">언제든지</span>
     연락하세요.</p>
  <p class="pe-ex__uz">Istalgan vaqtda bogʻlaning.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 도서관은 <span class="pe-hl pe-hl--o">누구든지</span>
     이용할 수 있다.</p>
  <p class="pe-ex__uz">Bu kutubxonadan har kim foydalana oladi.</p>
</div>

<h3>4. Qisqa shakllar: 든 va 건</h3>

<p>Ogʻzaki tilda 든지 koʻpincha <b>든</b> ga qisqaradi. Yana bir
qisqa variant — <b>건</b>. Maʼnosi bir xil, lekin ohangi
<b>keskinroq</b>: “menga baribir” degan soyasi bor.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그 사람이 <span class="pe-hl pe-hl--v">오든</span>
     <span class="pe-hl pe-hl--v">말든</span> 저는 갈 거예요.</p>
  <p class="pe-ex__uz">U kelsa ham, kelmasa ham men boraman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--v">크건</span>
     <span class="pe-hl pe-hl--v">작건</span> 상관없어요.</p>
  <p class="pe-ex__uz">Katta boʻladimi, kichikmi — farqi yoʻq.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>하든 말든</b> — eng koʻp uchraydigan juftlik.
  <b>말다</b> (“qilmaslik”) ikkinchi qismda inkorni beradi:
  가든 말든 · 하든 말든 · 먹든 말든. Oʻzbekchasi ham xuddi shunday
  juft: “borsa ham, <b>bormasa ham</b>”.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Ohangga eʼtibor bering.</b> 가든 말든 — “menga qizigʻi
  yoʻq” degan soyani olib yuradi. Shuning uchun uni
  <b>oʻzingizdan kattaga</b> aytmang. Neytral variant —
  <b>가시든지 안 가시든지</b> emas, balki oddiy
  <b>편하신 대로 하세요</b> kabi boshqa ibora.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>가든지 마음대로 하세요.</s>
    <small>(“xoh boring, xoh bormang” maʼnosida)</small></p>
  <p class="pe-good"><b>가든지 안 가든지</b> 마음대로 하세요.</p>
  <p><small>Bu qolip <b>juft</b> ishlaydi — ikkita variant kerak.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>학생든지 선생님든지 규칙은 같아요.</s></p>
  <p class="pe-good"><b>학생이든지 선생님이든지</b> 규칙은 같아요.</p>
  <p><small>받침 bor otda <b>이든지</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>주말에는 책을 읽든지 영화를 봐요.</s></p>
  <p class="pe-good">주말에는 책을 <b>읽거나</b> 영화를 봐요.</p>
  <p><small>Bu yerda haqiqiy <b>tanlov</b> bor — demak
  <b>거나</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>갔든지 안 갔든지 마음대로 하세요.</s></p>
  <p class="pe-good"><b>가든지 안 가든지</b> 마음대로 하세요.</p>
  <p><small>든지 oldida odatda zamon boʻlmaydi — hali
  qilinmagan ish.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring:
  <span class="pe-blank"></span> 안 가든지 마음대로 하세요. (가다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>가든지</b> — qolip juft ishlaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring:
  <span class="pe-blank"></span> 선생님이든지 규칙은 같아요. (학생)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>학생이든지</b> — 받침 bor → 이든지.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 거나 yoki 든지?
  “Dam olish kunlari kitob oʻqiyman yoki kino koʻraman.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>거나</b> — haqiqiy tanlov:
    책을 <b>읽거나</b> 영화를 봐요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> “Istalgan vaqtda bogʻlaning” —
  koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>언제든지 연락하세요.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> “U kelsa ham, kelmasa ham men
  boraman” — koreyschada (qisqa shaklda).</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>그 사람이 오든 말든 저는 갈 거예요.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Nega
  <s>가든지 마음대로 하세요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Qolip <b>ikkita variant</b> talab qiladi:
    <b>가든지 안 가든지</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Bu gapni 한다체 ga oʻgiring
  (PK-74): 날씨가 좋든지 나쁘든지 우리는 출발해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>날씨가 좋든지 나쁘든지 우리는 출발한다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>거나</b> — yoki (feʼl va sifat uchun)</li>
  <li><b>든지 … 든지</b> — xoh …, xoh …</li>
  <li><b>건 … 건</b> — shu maʼno, keskinroq</li>
  <li><b>하든 말든</b> — qilsa ham, qilmasa ham</li>
  <li><b>상관없다</b> — farqi yoʻq</li>
  <li><b>마음대로</b> — oʻz bilganicha</li>
  <li><b>뭐든지</b> — nima boʻlsa ham</li>
  <li><b>누구든지</b> — kim boʻlsa ham</li>
  <li><b>이용하다</b> — foydalanmoq</li>
  <li><b>규칙</b> — qoida</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>거나</b> = oddiy “yoki” — tanlov <b>bor</b>.</li>
    <li><b>든지 … 든지</b> = “xoh …, xoh …” — tanlov
      <b>ahamiyatsiz</b>.</li>
    <li>Qolip <b>juft</b> ishlaydi: ikkita variant kerak.</li>
    <li>Ot bilan <b>(이)든지</b>: 학생이든지, 커피든지.</li>
    <li>Soʻroq soʻzi bilan “har qanday”: <b>뭐든지 · 누구든지 ·
      언제든지 · 어디든지</b>.</li>
    <li>Qisqa shakllar: <b>든</b> va <b>건</b>. 건 keskinroq
      eshitiladi.</li>
    <li><b>하든 말든</b> — 말다 bilan yasalgan eng koʻp uchraydigan
      juft.</li>
    <li>Oʻzbekcha juftlari: “<b>xoh …, xoh …</b>” va
      “<b>…sa ham, …masa ham</b>”.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-85
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-85: (느)니 차라리, (으)나 마나 — yaxshiroq muqobil va befoyda ish",
        "category": "korean",
        "order": 85,
        "summary": (
            "“Unday qilgandan koʻra yolgʻiz yashaganim yaxshi” va "
            "“soʻrasa ham, soʻramasa ham javob maʼlum” — tanlash va "
            "tanlamaslik."
        ),
        "stories": ["반대로 간 사람"],
        "content": """
<h2>PK-85: (느)니 차라리, (으)나 마나 — yaxshiroq muqobil va befoyda ish</h2>

<p>Ikki yomon variant orasida qolgansiz. Biri juda yomon, ikkinchisi
shunchaki yomon. Oʻzbekchada aytamiz: <em>“Undan koʻra buni
qilganim yaxshi.”</em> Va boshqa holat: natija allaqachon maʼlum —
<em>“soʻrasam ham, soʻramasam ham bir gap.”</em> Bugun shu ikkalasi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(느)니 차라리</b> bilan yaxshiroq muqobilni tanlaysiz</li>
    <li>Nega birinchi variant <b>doim yomon</b> ekanini bilib olasiz</li>
    <li><b>(으)나 마나</b> bilan “natija bir xil” deysiz</li>
    <li>Uni PK-80 dagi <b>아/어 봤자</b> dan ajratasiz</li>
    <li>Tayyor iboralarni oʻrganasiz: <b>보나 마나</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qolip</span>
  <span class="pe-chip pe-chip--v">(느)니 차라리</span>
  <span class="pe-chip pe-chip--neg">(으)나 마나</span>
  <span class="pe-chip pe-chip--adv">= …gandan koʻra / …sa ham baribir</span>
</div>

<h3>1. (느)니 차라리 — “…gandan koʻra …”</h3>

<p>Qolip: <b>A(느)니 차라리 B</b> = “A ni qilgandan koʻra, B
yaxshiroq”. Muhim sharti bor: <b>A ham, B ham yoqimsiz</b>, lekin
soʻzlovchi B ni afzal koʻradi. Bu — <em>iloji boricha
kamroq yomon</em> tanlov.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그 일을 <span class="pe-hl pe-hl--v">하느니</span>
     차라리 그만두는 것이 낫다.</p>
  <p class="pe-ex__uz">U ishni qilgandan koʻra, tashlab qoʻygan
  yaxshiroq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이렇게 <span class="pe-hl pe-hl--v">기다리느니</span>
     차라리 걸어가는 것이 낫다.</p>
  <p class="pe-ex__uz">Bunday kutgandan koʻra, piyoda ketganim
  yaxshiroq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">싸운 친구에게 <span class="pe-hl pe-hl--v">먼저
     연락하느니</span> 차라리 기다리는 것이 낫다.</p>
  <p class="pe-ex__uz">Urishgan doʻstga birinchi boʻlib yozgandan
  koʻra, kutganim yaxshiroq.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>(느)니 ning uch qoidasi:</b><br>
  1. Faqat <b>feʼl</b> bilan (sifat va ot bilan emas).<br>
  2. Oldida <b>zamon boʻlmaydi</b>: ❌ <s>했느니</s>.<br>
  3. <b>차라리</b> majburiy emas, lekin deyarli har doim yoniga
  keladi va maʼnoni ochiq qiladi.<br>
  Ikkinchi gapda koʻpincha <b>…는 것이 낫다</b> yoki
  <b>(으)ㄹ 것이다</b> turadi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada aynan shu qolip bor: “…gandan koʻra”.</b>
  <em>“Kutgandan koʻra piyoda ketgan yaxshi”</em>,
  <em>“yolgʻon gapirgandan koʻra jim turgan afzal”</em>. Va bizda
  ham gapning ikkinchi qismida <b>“yaxshi / afzal / durust”</b>
  kabi baho soʻzi keladi — koreyschada u <b>낫다</b>.
  Yana bir jufti — “<b>koʻra</b>” soʻzining oʻzi: u ham, koreyscha
  <b>차라리</b> ham gapga <em>“ikkovi ham yomon, lekin…”</em>
  degan soyani beradi.</p>
</div>

<h3>2. (으)나 마나 — “qilsa ham, qilmasa ham bir xil”</h3>

<p><b>마나</b> ichida <b>말다</b> (“qilmaslik”) turibdi. Yaʼni
soʻzma-soʻz: “qilsa ham, qilmasa ham”. Maʼnosi — <b>natija
oldindan maʼlum</b>, shuning uchun qilishning hojati yoʻq.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">나 마나</span></p>
    <p>보다 → 보나 마나</p>
    <p>가다 → 가나 마나</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">으나 마나</span></p>
    <p>먹다 → 먹으나 마나</p>
    <p>묻다 → 물으나 마나</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--neg">보나 마나</span>
     그 사람이 이길 것이다.</p>
  <p class="pe-ex__uz">Koʻrmasam ham bilaman — u yutadi.</p>
  <p class="pe-ex__why"><b>보나 마나</b> — eng koʻp uchraydigan
  tayyor ibora.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--neg">물어보나 마나</span>
     대답은 똑같아요.</p>
  <p class="pe-ex__uz">Soʻrasangiz ham, soʻramasangiz ham javob
  bir xil.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 약은 <span class="pe-hl pe-hl--neg">먹으나 마나</span>
     효과가 없어요.</p>
  <p class="pe-ex__uz">Bu dorini ichsangiz ham, ichmasangiz ham foydasi
  yoʻq.</p>
</div>

<h3>3. 나 마나 va 봤자 — yaqin, lekin bir xil emas</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">아/어 봤자 <small>PK-80</small></p>
    <p><b>Qilish behuda.</b> Urinasan — natija oʻzgarmaydi.</p>
    <p><small>지금 가 봤자 소용없어요.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)나 마나</p>
    <p><b>Ikkala yoʻl bir xil.</b> Natija <em>allaqachon
    maʼlum</em> — tekshirishning hojati yoʻq.</p>
    <p><small>보나 마나 그 사람이 이길 거예요.</small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Oson tekshiruv:</b> gap <em>harakatning foydasizligi</em>
  haqidami yoki <em>natija oldindan maʼlumligi</em> haqidami?<br>
  “Yugursang ham poyezdga ulgurmaysan” → <b>봤자</b>.<br>
  “Qaramasam ham bilaman, u yutadi” → <b>나 마나</b>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>그 일을 했느니 차라리 그만두는 것이 낫다.</s></p>
  <p class="pe-good">그 일을 <b>하느니</b> 차라리 그만두는 것이 낫다.</p>
  <p><small>(느)니 oldida <b>zamon boʻlmaydi</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>날씨가 나쁘니 차라리 집에 있어요.</s>
    <small>(“yomon boʻlgandan koʻra” maʼnosida)</small></p>
  <p class="pe-good">밖에 <b>나가느니</b> 차라리 집에 있는 것이 낫다.</p>
  <p><small>(느)니 faqat <b>feʼl</b> bilan. 나쁘다 — sifat, va
  <b>나쁘니</b> butunlay boshqa maʼno beradi (“yomon boʻlgani
  uchun”).</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>물어보나 말나 대답은 똑같아요.</s></p>
  <p class="pe-good"><b>물어보나 마나</b> 대답은 똑같아요.</p>
  <p><small>Shakl <b>마나</b> — 말다 dan, lekin ㄹ tushadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>먹나 마나 효과가 없어요.</s></p>
  <p class="pe-good"><b>먹으나 마나</b> 효과가 없어요.</p>
  <p><small>먹 da 받침 bor → <b>으나 마나</b>.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 이렇게
  <span class="pe-blank"></span> 차라리 걸어가는 것이 낫다. (기다리다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>기다리느니</b> — oʻzak + 느니, zamon yoʻq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 이 약은
  <span class="pe-blank"></span> 마나 효과가 없어요. (먹다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>먹으나</b> — 받침 bor → 으나 마나.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Toʻldiring:
  <span class="pe-blank"></span> 마나 그 사람이 이길 것이다. (보다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>보나</b> — 받침 yoʻq. <b>보나 마나</b> tayyor ibora.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Nega
  <s>그 일을 했느니</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>(느)니 oldida zamon qoʻyilmaydi. Toʻgʻrisi —
    <b>하느니</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> 봤자 yoki 나 마나?
  “Qaramasam ham bilaman — u yutadi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>나 마나</b> — natija oldindan maʼlum:
    <b>보나 마나</b> 그 사람이 이길 거예요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “U ishni qilgandan koʻra
  tashlab qoʻygan yaxshiroq” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>그 일을 하느니 차라리 그만두는 것이 낫다.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> <b>마나</b> ning ichida qaysi
  feʼl turibdi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>말다</b> — “qilmaslik”. Shuning uchun qolipning maʼnosi
    “qilsa ham, <em>qilmasa</em> ham”.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(느)니 차라리</b> — …gandan koʻra … yaxshiroq</li>
  <li><b>(으)나 마나</b> — qilsa ham, qilmasa ham bir xil</li>
  <li><b>차라리</b> — koʻra, aksincha</li>
  <li><b>낫다</b> — yaxshiroq boʻlmoq</li>
  <li><b>그만두다</b> — tashlab qoʻymoq</li>
  <li><b>이기다</b> — yutmoq</li>
  <li><b>효과</b> — samara, foyda</li>
  <li><b>똑같다</b> — bir xil</li>
  <li><b>싸우다</b> — urishmoq</li>
  <li><b>참다</b> — chidamoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>A(느)니 차라리 B</b> = “A dan koʻra B yaxshiroq”.</li>
    <li><b>Ikkala variant ham yoqimsiz</b> — bu kamroq yomonini
      tanlash.</li>
    <li>Faqat feʼl bilan, oldida zamon yoʻq.</li>
    <li>Ikkinchi gapda koʻpincha <b>는 것이 낫다</b>.</li>
    <li><b>(으)나 마나</b> ichida <b>말다</b> bor — “qilsa ham,
      qilmasa ham”.</li>
    <li>받침 yoʻq → <b>나 마나</b> · 받침 bor → <b>으나 마나</b>.</li>
    <li>Tayyor iboralar: <b>보나 마나 · 물어보나 마나</b>.</li>
    <li>봤자 = harakat behuda · <b>나 마나 = natija oldindan
      maʼlum</b>.</li>
  </ul>
</div>
""",
    },
]
