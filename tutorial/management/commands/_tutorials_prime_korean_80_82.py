# -*- coding: utf-8 -*-
"""Prime Korean — Block F, darslar 80–82.

80. 아/어 봤자 — behuda urinish
81. (으)ㄹ지라도, 더라도, (으)ㅁ에도 불구하고 — kuchli yon berish
82. (으)ㄹ 정도로 / (으)ㄹ 만큼 — daraja va oʻlchov

80 va 81 bir-birining teskarisi:
  봤자   — “urinsang ham FOYDASI YOʻQ”  (natija oʻzgarmaydi)
  더라도 — “boʻlsa ham BARIBIR qilaman” (irodam oʻzgarmaydi)
Ikkalasi ham yon berish, lekin biri qoʻl siltaydi, ikkinchisi turib oladi.

Oʻzbekcha kalitlar:
  아/어 봤자           = "…ganing bilan foydasi yoʻq" / "koʻpi bilan …"
  아/어도             = "…sa ham"           (oddiy)
  더라도              = "…sa ham, hatto"    (kuchli, faraz)
  (으)ㄹ지라도          = "…sa-da"           (kitobiy)
  (으)ㅁ에도 불구하고    = "…ga QARAMAY"      (FAKT, rasmiy)
  (으)ㄹ 정도로         = "…gudek darajada"
  (으)ㄹ 만큼          = "…gancha, …gan qadar"

PK-81 da 아/어도 ning yon berish maʼnosi birinchi marta ochiq
oʻrgatiladi — PK-51 da u faqat 아/어도 되다 ichida uchragan edi.
불구하고 = 不拘 (“bogʻlanmasdan”) — oʻzbekcha “qaramay” ning aynan
oʻzi; bu izoh darsda beriladi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_80_82.py --author=prime
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
    # PK-80
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-80: 아/어 봤자 — behuda urinish",
        "category": "korean",
        "order": 80,
        "summary": (
            "“Hozir borganing bilan foydasi yoʻq” va “qancha qimmat "
            "boʻlsa ham, koʻpi bilan oʻn ming” — ikki maʼno, bitta qolip."
        ),
        "stories": ["벼락치기는 통하지 않는다"],
        "content": """
<h2>PK-80: 아/어 봤자 — behuda urinish</h2>

<p>Poyezd oʻn daqiqa oldin ketdi. Doʻstingiz yugurib bormoqchi. Siz
nima deysiz? — <em>“Endi borganing bilan foydasi yoʻq.”</em> Urinishning
oʻzi mumkin, lekin <b>natija oʻzgarmaydi</b>. Koreys tilida bu fikr
uchun juda qulay qolip bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>아/어 봤자</b> bilan “urinsang ham foydasi yoʻq” deysiz</li>
    <li>Uning <b>ikkinchi</b> maʼnosini — “koʻpi bilan …” ni oʻrganasiz</li>
    <li>Ikkinchi gapda nima kelishini bilib olasiz</li>
    <li>Uni PK-41 dagi <b>아/어 보다</b> bilan bogʻlaysiz</li>
    <li><b>아무리</b> bilan birga ishlatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">아/어 봤자</span>
  <span class="pe-chip pe-chip--neg">소용없다 / 안 되다 / 마찬가지다</span>
  <span class="pe-chip pe-chip--adv">= …ganing bilan foydasi yoʻq</span>
</div>

<h3>1. Shakli</h3>

<p>Qolipning ichida siz allaqachon biladigan narsa turibdi:
PK-41 dagi <b>아/어 보다</b> — “sinab koʻrmoq”. Unga oʻtgan zamon
qoʻshilgan: <b>봤자</b> = “sinab koʻrgan taqdirda ham”. Shuning uchun
ulanish ham 아/어서 dagi kabi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>아/어 shakli</th><th>Natija</th></tr>
  <tr><td class="pk-stem">가다</td><td class="pk-end">가</td>
      <td class="pk-res">가 봤자</td></tr>
  <tr><td class="pk-stem">먹다</td><td class="pk-end">먹어</td>
      <td class="pk-res">먹어 봤자</td></tr>
  <tr><td class="pk-stem">하다</td><td class="pk-end">해</td>
      <td class="pk-res">해 봤자</td></tr>
  <tr><td class="pk-stem">기다리다</td><td class="pk-end">기다려</td>
      <td class="pk-res">기다려 봤자</td></tr>
</table></div>

<h3>2. Birinchi maʼno: “urinsang ham foydasi yoʻq”</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">지금 <span class="pe-hl pe-hl--neg">가 봤자</span>
     기차는 이미 떠났어요.</p>
  <p class="pe-ex__uz">Hozir borganingiz bilan poyezd allaqachon ketgan.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아무리 <span class="pe-hl pe-hl--neg">설명해 봤자</span>
     그 사람은 안 들어요.</p>
  <p class="pe-ex__uz">Qancha tushuntirsangiz ham, u odam eshitmaydi.</p>
  <p class="pe-ex__why"><b>아무리</b> (“qancha …sa ham”) — 봤자 ning eng
  koʻp uchraydigan sherigi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">지금 <span class="pe-hl pe-hl--neg">후회해 봤자</span>
     소용없어요.</p>
  <p class="pe-ex__uz">Endi pushaymon boʻlganingiz bilan foyda yoʻq.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu qolip “-ganing bilan” shaklida yashaydi:</b>
  “bor<b>ganing bilan</b> foydasi yoʻq”, “aytgan<b>ing bilan</b> u
  tushunmaydi”. Eʼtibor bering — bizda ham ish <em>oʻtgan zamonda</em>
  turadi (“borganing”), garchi u hali boʻlmagan boʻlsa ham. Koreyschada
  ham xuddi shunday: <b>봤자</b> ichida <b>았</b> bor. Ikki tilda ham
  mantiq bir xil: <em>oʻsha ishni qilib boʻlgan holatni tasavvur
  qilamiz — va koʻramizki, hech narsa oʻzgarmaydi.</em></p>
</div>

<div class="pe-call pe-rule">
  <p><b>Ikkinchi gapda nima keladi:</b><br>
  • <b>소용없다</b> — foydasi yoʻq<br>
  • <b>안 되다 / 못 하다</b> — boʻlmaydi<br>
  • <b>마찬가지다</b> — baribir, oʻsha-oʻsha<br>
  • <b>이미 …았/었다</b> — allaqachon boʻlib boʻlgan<br>
  Umumiy qoida: natija <b>salbiy yoki foydasiz</b>.</p>
</div>

<h3>3. Ikkinchi maʼno: “koʻpi bilan …”</h3>

<p>Ikkinchi maʼno biroz boshqacha: “eng koʻpi bilan shuncha, undan
ortiq emas”. Bu yerda soʻzlovchi narsani <b>kichraytirib</b>
koʻrsatadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그 가방이 <span class="pe-hl pe-hl--adv">비싸 봤자</span>
     삼만 원이에요.</p>
  <p class="pe-ex__uz">U sumka qancha qimmat boʻlsa ham, koʻpi bilan
  oʻttiz ming von.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아이가 <span class="pe-hl pe-hl--adv">먹어 봤자</span>
     얼마나 먹겠어요? 조금만 주세요.</p>
  <p class="pe-ex__uz">Bola qancha yesa ham, qancha yeyardi? Ozgina
  bering.</p>
</div>

<div class="pe-call pe-tip">
  <p>Ikkinchi maʼnoda <b>sifat</b> bilan ham ishlatiladi:
  <b>비싸 봤자 · 커 봤자 · 멀어 봤자</b>. Birinchi maʼnoda esa
  faqat feʼl bilan. Qaysi maʼno ekanini ikkinchi gap aytib
  beradi: raqam boʻlsa — “koʻpi bilan”, 소용없다 boʻlsa — “foydasi
  yoʻq”.</p>
</div>

<h3>4. 봤자 va boshqa yon berish qoliplari</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">아/어 봤자</p>
    <p><b>Qoʻl siltash.</b> “Urinma, natija oʻzgarmaydi.”</p>
    <p><small>지금 가 봤자 소용없어요.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">다가는 <small>PK-79</small></p>
    <p><b>Ogohlantirish.</b> “Toʻxtat, yomon boʻladi.”</p>
    <p><small>그렇게 놀다가는 시험에 떨어질 거예요.</small></p>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>지금 갔 봤자 소용없어요.</s></p>
  <p class="pe-good">지금 <b>가 봤자</b> 소용없어요.</p>
  <p><small>Zamon <b>봤자</b> ning ichida bor — oldiga yana
  qoʻyilmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>열심히 공부해 봤자 시험에 붙을 거예요.</s></p>
  <p class="pe-good">열심히 공부<b>하다가 보면</b> 시험에 붙을 거예요.</p>
  <p><small>봤자 dan keyin <b>ijobiy</b> natija kelmaydi. Yaxshi natija
  uchun — PK-77 dagi <b>다가 보면</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>지금 가 봤자 빨리 가세요.</s></p>
  <p class="pe-good">지금 가 봤자 <b>소용없어요</b>.</p>
  <p><small>봤자 dan keyin buyruq emas, <b>foydasizlik</b>
  keladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그 가방이 비쌌 봤자 삼만 원이에요.</s></p>
  <p class="pe-good">그 가방이 <b>비싸 봤자</b> 삼만 원이에요.</p>
  <p><small>Sifat ham 아/어 shaklida: 비싸 + 봤자.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 지금
  <span class="pe-blank"></span> 기차는 이미 떠났어요. (가다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>가 봤자</b> — 가 + 봤자.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 아무리
  <span class="pe-blank"></span> 그 사람은 안 들어요. (설명하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>설명해 봤자</b> — 하다 → 해 + 봤자.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Nega
  <s>지금 갔 봤자</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Oʻtgan zamon <b>봤자</b> ning oʻzida bor (봤 = 보 + 았).
    Toʻgʻrisi — <b>가 봤자</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Bu gap qaysi maʼnoda?
  그 가방이 비싸 봤자 삼만 원이에요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>“Koʻpi bilan”</b> maʼnosida. Ikkinchi gapda <b>raqam</b>
    turgani shuni koʻrsatadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Nega
  <s>열심히 공부해 봤자 시험에 붙을 거예요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>봤자 dan keyin natija <b>foydasiz</b> boʻlishi kerak.
    “Imtihondan oʻtish” — yaxshi natija.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Endi pushaymon boʻlganingiz
  bilan foyda yoʻq” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>지금 후회해 봤자 소용없어요.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Bu gapni 한다체 ga oʻgiring
  (PK-74): 지금 가 봤자 소용없어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>지금 가 봤자 소용없다.</b> 없다 — oʻzgarmaydi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아/어 봤자</b> — …ganing bilan foydasi yoʻq</li>
  <li><b>아무리</b> — qancha …sa ham</li>
  <li><b>소용없다</b> — foydasi yoʻq</li>
  <li><b>마찬가지다</b> — baribir, oʻsha-oʻsha</li>
  <li><b>이미</b> — allaqachon</li>
  <li><b>떠나다</b> — joʻnab ketmoq</li>
  <li><b>후회하다</b> — pushaymon boʻlmoq</li>
  <li><b>설명하다</b> — tushuntirmoq</li>
  <li><b>통하다</b> — ish bermoq, oʻtmoq</li>
  <li><b>기껏해야</b> — koʻpi bilan</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>아/어 봤자</b> = “urinsang ham foydasi yoʻq”.</li>
    <li>Ichida PK-41 dagi <b>아/어 보다</b> turibdi — “sinab
      koʻrgan taqdirda ham”.</li>
    <li>Zamon <b>봤자</b> ning oʻzida — oldiga yana
      qoʻyilmaydi.</li>
    <li>Ikkinchi gap: <b>소용없다 · 안 되다 · 마찬가지다 ·
      이미 …았다</b>.</li>
    <li>Ijobiy natija bilan <b>ishlatilmaydi</b>.</li>
    <li>Ikkinchi maʼnosi — “<b>koʻpi bilan</b>”: 비싸 봤자 삼만
      원이에요.</li>
    <li>Ikkinchi maʼnoda <b>sifat</b> bilan ham boʻladi.</li>
    <li>Oʻzbekcha juftligi: “<b>…ganing bilan foydasi yoʻq</b>”.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-81
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-81: (으)ㄹ지라도, 더라도, (으)ㅁ에도 불구하고 — kuchli yon berish",
        "category": "korean",
        "order": 81,
        "summary": (
            "“Nima boʻlsa ham boraman” va “harakat qilganiga qaramay "
            "boʻlmadi” — yon berishning uch darajasi."
        ),
        "stories": ["스무 번째 편지"],
        "content": """
<h2>PK-81: (으)ㄹ지라도, 더라도, (으)ㅁ에도 불구하고 — kuchli yon berish</h2>

<p>Oʻtgan darsda “urinsang ham foydasi yoʻq” dedik. Bugun aksincha:
<em>“Qiyin boʻlsa ham qilaman.”</em> Sharoit yomon — lekin qaror
oʻzgarmaydi. Koreys tilida bu fikrning uch darajasi bor, va ular
oʻrtasidagi farqni bilish TOPIK II da katta yordam beradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Oddiy <b>아/어도</b> ni yon berish sifatida ishlatasiz</li>
    <li><b>더라도</b> bilan uni kuchaytirasiz</li>
    <li>Kitobiy <b>(으)ㄹ지라도</b> ni oʻrganasiz</li>
    <li><b>(으)ㅁ에도 불구하고</b> bilan <b>haqiqiy faktga</b> qarshi turasiz</li>
    <li>Uchtasini bir zinapoyaga tizasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch daraja</span>
  <span class="pe-chip pe-chip--v">아/어도</span>
  <span class="pe-chip pe-chip--aux">더라도</span>
  <span class="pe-chip pe-chip--s">(으)ㅁ에도 불구하고</span>
</div>

<h3>1. 아/어도 — asos</h3>

<p>Bu shakl sizga tanish: PK-51 da <b>아/어도 되다</b> (“qilsangiz ham
boʻladi”) ni oʻrgangansiz. Oʻsha <b>아/어도</b> ning oʻzi mustaqil
holda “<b>…sa ham</b>” degan maʼnoni beradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">비가 <span class="pe-hl pe-hl--v">와도</span>
     학교에 가요.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻsa ham maktabga boraman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아무리 <span class="pe-hl pe-hl--v">바빠도</span>
     아침은 먹어요.</p>
  <p class="pe-ex__uz">Qancha band boʻlsam ham nonushta qilaman.</p>
</div>

<h3>2. 더라도 — kuchliroq va farazga asoslangan</h3>

<p><b>더라도</b> ham “…sa ham” degani, lekin ikki farq bilan:
u <b>kuchliroq</b> eshitiladi va odatda <b>hali boʻlmagan,
tasavvurdagi</b> holat haqida. Oʻzagiga toʻgʻridan toʻgʻri
qoʻshiladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">무슨 일이 <span class="pe-hl pe-hl--aux">있더라도</span>
     저는 갈 거예요.</p>
  <p class="pe-ex__uz">Nima boʻlsa ham men boraman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시간이 <span class="pe-hl pe-hl--aux">없더라도</span>
     책은 매일 읽으세요.</p>
  <p class="pe-ex__uz">Vaqtingiz boʻlmasa ham kitobni har kuni oʻqing.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">힘들<span class="pe-hl pe-hl--aux">더라도</span>
     포기하지 마세요.</p>
  <p class="pe-ex__uz">Qiyin boʻlsa ham voz kechmang.</p>
</div>

<div class="pe-call pe-tip">
  <p>Ichidagi <b>더</b> — PK-78 dagi bilan bir xil belgi:
  “<em>oʻsha holatga kirib qarab koʻrish</em>”. Shuning uchun
  더라도 sizni tasavvurdagi vaziyatning ichiga olib kiradi:
  <em>“aytaylik, hech vaqt boʻlmadi — mayli, baribir …”</em></p>
</div>

<h3>3. (으)ㄹ지라도 — kitobiy va eng kuchli</h3>

<p>Bu shakl <b>yozma matn</b>, nutq va shiorlarniki. Ogʻzaki suhbatda
deyarli eshitilmaydi, lekin TOPIK II oʻqishida uchraydi.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄹ지라도</span></p>
    <p>가다 → 갈지라도</p>
    <p>아프다 → 아플지라도</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">을지라도</span></p>
    <p>먹다 → 먹을지라도</p>
    <p>힘들다 → 힘들지라도</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">몸이 <span class="pe-hl pe-hl--s">아플지라도</span>
     약속은 지킬 것이다.</p>
  <p class="pe-ex__uz">Kasal boʻlsam-da, vaʼdani bajaraman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">결과가 <span class="pe-hl pe-hl--s">나쁠지라도</span>
     후회하지 않을 것이다.</p>
  <p class="pe-ex__uz">Natija yomon boʻlsa-da, pushaymon boʻlmayman.</p>
</div>

<h3>4. (으)ㅁ에도 불구하고 — faktga qarshi</h3>

<p>Mana bu — boshqa qush. Yuqoridagi uchtasi <em>faraz</em> haqida
edi. <b>(으)ㅁ에도 불구하고</b> esa <b>allaqachon boʻlgan haqiqat</b>
haqida: “shunday boʻlgan boʻlishiga qaramay”.</p>

<p>Yasalishi: PK-46 dagi <b>(으)ㅁ</b> otlashtirishi + 에도 불구하고.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>(으)ㅁ shakli</th><th>Natija</th></tr>
  <tr><td class="pk-stem">노력하다</td><td class="pk-end">노력함</td>
      <td class="pk-res">노력함에도 불구하고</td></tr>
  <tr><td class="pk-stem">노력했다</td><td class="pk-end">노력했음</td>
      <td class="pk-res">노력했음에도 불구하고</td></tr>
  <tr><td class="pk-stem">어리다</td><td class="pk-end">어림</td>
      <td class="pk-res">어림에도 불구하고</td></tr>
  <tr><td class="pk-stem">비 (ot)</td><td class="pk-end">—</td>
      <td class="pk-res">비에도 불구하고</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">여러 번 <span class="pe-hl pe-hl--s">노력했음에도
     불구하고</span> 결과는 좋지 않았다.</p>
  <p class="pe-ex__uz">Bir necha marta harakat qilganiga qaramay,
  natija yaxshi boʻlmadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">나이가 <span class="pe-hl pe-hl--s">어림에도
     불구하고</span> 그 학생은 아주 침착하다.</p>
  <p class="pe-ex__uz">Yoshligiga qaramay, u oʻquvchi juda vazmin.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>불구하고 ning ichida hanzuviy 不拘 bor — “bogʻlanmasdan,
  qaramasdan”.</b> Oʻzbekchadagi “<b>qaramay</b>” ham aynan shu:
  “yosh<b>ligiga qaramay</b>”, “yomgʻir<b>ga qaramay</b>”. Ikki
  tilda ham bu soʻz <em>koʻz</em> bilan bogʻliq obrazdan
  kelib chiqqan: “men bunga <em>qaramayman</em>, bu meni
  toʻxtatmaydi”. Va ikkalasida ham oldida <b>fakt</b> turadi —
  taxmin emas. Shuning uchun ❌ “ertaga yomgʻir yogʻishiga qaramay
  boraman” degan gap oʻzbekchada ham gʻalati eshitiladi.</p>
</div>

<h3>5. Zinapoya</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Faraz yoki fakt</th><th>Uslub</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pk-stem">아/어도</td><td>faraz</td><td>kundalik</td>
      <td class="pk-uz">…sa ham</td></tr>
  <tr><td class="pk-stem">더라도</td><td>faraz (kuchli)</td><td>ogʻzaki + yozma</td>
      <td class="pk-uz">nima boʻlsa ham</td></tr>
  <tr><td class="pk-stem">(으)ㄹ지라도</td><td>faraz (eng kuchli)</td><td>kitobiy</td>
      <td class="pk-uz">…sa-da</td></tr>
  <tr><td class="pk-stem">(으)ㅁ에도 불구하고</td><td><b>fakt</b></td><td>rasmiy yozma</td>
      <td class="pk-uz">…ga qaramay</td></tr>
</table></div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">노력하<b>더라도</b> 안 될 거예요.</p>
    <p><b>Faraz.</b> Hali harakat qilmagan.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">노력했<b>음에도 불구하고</b> 안 됐어요.</p>
    <p><b>Fakt.</b> Harakat qilgan — va boʻlmagan.</p>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>무슨 일이 있었더라도 저는 갈 거예요.</s></p>
  <p class="pe-good">무슨 일이 <b>있더라도</b> 저는 갈 거예요.</p>
  <p><small>더라도 farazga qaraydi — oldida oʻtgan zamon
  kerak emas.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>노력하음에도 불구하고 실패했어요.</s></p>
  <p class="pe-good"><b>노력했음에도</b> 불구하고 실패했어요.</p>
  <p><small>하다 → <b>함</b> / oʻtgan zamon → <b>했음</b>.
  ❌ 하음.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>내일 비가 옴에도 불구하고 갈 거예요.</s></p>
  <p class="pe-good">내일 비가 <b>오더라도</b> 갈 거예요.</p>
  <p><small>Ertaga — hali <b>fakt emas</b>. Faraz uchun
  <b>더라도</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>친구한테 “힘들지라도 포기하지 마”라고 했어요.</s>
    <small>(kundalik suhbatda)</small></p>
  <p class="pe-good">친구한테 “<b>힘들더라도</b> 포기하지 마”라고 했어요.</p>
  <p><small>(으)ㄹ지라도 — <b>kitobiy</b>. Doʻstga aytilganda
  gʻalati eshitiladi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 무슨 일이
  <span class="pe-blank"></span> 저는 갈 거예요. (있다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>있더라도</b> — oʻzak + 더라도, zamon yoʻq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 몸이
  <span class="pe-blank"></span> 약속은 지킬 것이다. (아프다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>아플지라도</b> — 아프 da 받침 yoʻq → ㄹ지라도.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Toʻldiring: 여러 번
  <span class="pe-blank"></span> 불구하고 결과는 좋지 않았다. (노력하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>노력했음에도</b> — 하다 → 했음 + 에도 불구하고.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 더라도 yoki 에도 불구하고?
  “Ertaga yomgʻir yogʻsa ham boraman.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>더라도</b> — ertaga hali <b>fakt emas</b>:
    내일 비가 <b>오더라도</b> 갈 거예요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> 더라도 yoki 에도 불구하고?
  “Koʻp harakat qilganiga qaramay boʻlmadi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>에도 불구하고</b> — harakat <b>boʻlgan</b>, bu fakt:
    많이 <b>노력했음에도 불구하고</b> 안 됐어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Bu gap qaysi uslubda —
  kundalik suhbatmi yoki yozma matn?
  결과가 나쁠지라도 후회하지 않을 것이다.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Yozma matn.</b> (으)ㄹ지라도 + 것이다 — ikkalasi ham
    kitobiy.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> “Yoshligiga qaramay, u
  oʻquvchi juda vazmin” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>나이가 어림에도 불구하고 그 학생은 아주 침착하다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아/어도</b> — …sa ham</li>
  <li><b>더라도</b> — nima boʻlsa ham (kuchli)</li>
  <li><b>(으)ㄹ지라도</b> — …sa-da (kitobiy)</li>
  <li><b>(으)ㅁ에도 불구하고</b> — …ga qaramay (fakt)</li>
  <li><b>노력하다</b> — harakat qilmoq</li>
  <li><b>약속을 지키다</b> — vaʼdani bajarmoq</li>
  <li><b>결과</b> — natija</li>
  <li><b>침착하다</b> — vazmin boʻlmoq</li>
  <li><b>거절하다</b> — rad etmoq</li>
  <li><b>포기하다</b> — voz kechmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>아/어도</b> = oddiy “…sa ham”. Kundalik.</li>
    <li><b>더라도</b> = kuchliroq, <b>farazga</b> asoslangan.
      Oldida zamon yoʻq.</li>
    <li><b>(으)ㄹ지라도</b> = eng kuchli va <b>kitobiy</b>.
      Suhbatda ishlatilmaydi.</li>
    <li><b>(으)ㅁ에도 불구하고</b> = <b>fakt</b>ga qarshi turish.
      Rasmiy yozma til.</li>
    <li>하다 → <b>함</b> · oʻtgan zamon → <b>했음</b>.
      Ot bilan ham boʻladi: 비에도 불구하고.</li>
    <li>Faraz → 더라도 · Fakt → 에도 불구하고. Bu asosiy
      chegara.</li>
    <li><b>不拘</b> = “qaramasdan” — oʻzbekcha “qaramay” bilan bir
      xil obraz.</li>
    <li>PK-80 dagi <b>봤자</b> qoʻl siltaydi, bugungi qoliplar
      <b>turib oladi</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-82
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-82: (으)ㄹ 정도로 / (으)ㄹ 만큼 — daraja va oʻlchov",
        "category": "korean",
        "order": 82,
        "summary": (
            "“Qornim ogʻriydigan darajada kuldim” va “yeydiganimcha "
            "yedim” — qanchalik ekanini koʻrsatishning ikki yoʻli."
        ),
        "stories": ["가장 작은 것과 가장 큰 것"],
        "content": """
<h2>PK-82: (으)ㄹ 정도로 / (으)ㄹ 만큼 — daraja va oʻlchov</h2>

<p>“Kuldim” — tushunarli. “<em>Qornim ogʻriydigan darajada</em>
kuldim” — endi men qanchalik kulganimni koʻryapsiz. Bugungi ikki
qolip aynan shuni qiladi: bir ishning <b>qanchaligini</b> boshqa bir
ish orqali oʻlchaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ 정도로</b> bilan darajani koʻrsatasiz</li>
    <li><b>(으)ㄹ 만큼</b> bilan miqdorni koʻrsatasiz</li>
    <li>Ikkalasining farqini aniq bilib olasiz</li>
    <li>Gapdagi <b>tartibni</b> toʻgʻri quyasiz — bu eng koʻp xato</li>
    <li>Ot bilan ishlatishni oʻrganasiz: 저만큼, 이 정도</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki oʻlchov</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ 정도로</span>
  <span class="pe-chip pe-chip--o">(으)ㄹ 만큼</span>
  <span class="pe-chip pe-chip--adv">= …gudek darajada / …gancha</span>
</div>

<h3>1. (으)ㄹ 정도로 — “…gudek darajada”</h3>

<p><b>정도</b> — “daraja, oʻlcham” degan ot (程度). Demak
<b>A(으)ㄹ 정도로 B</b> = “<em>A boʻladigan darajada</em> B”.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">배가 <span class="pe-hl pe-hl--v">아플 정도로</span>
     웃었어요.</p>
  <p class="pe-ex__uz">Qornim ogʻriydigan darajada kuldim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">눈을 뜰 수 <span class="pe-hl pe-hl--v">없을 정도로</span>
     바람이 강했어요.</p>
  <p class="pe-ex__uz">Koʻzni ocha olmaydigan darajada shamol kuchli edi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">말도 못 <span class="pe-hl pe-hl--v">할 정도로</span>
     피곤했어요.</p>
  <p class="pe-ex__uz">Gapira olmaydigan darajada charchagan edim.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>TARTIBGA DIQQAT — eng koʻp uchraydigan xato shu.</b><br>
  Koreyschada <b>oʻlchov birinchi</b>, asosiy ish keyin:<br>
  <b>배가 아플 정도로</b> 웃었어요. → “<em>Qornim ogʻriydigan
  darajada</em> — kuldim.”<br>
  Oʻzbekcha tarjimada ham xuddi shu tartib! Shuning uchun
  oʻzbekcha jumlani <em>gapirgan tartibda</em> yozsangiz, koreyschasi
  toʻgʻri chiqadi. ❌ <s>웃었어요 배가 아플 정도로</s> demang.</p>
</div>

<h3>2. (으)ㄹ 만큼 — “…gancha, …gan qadar”</h3>

<p><b>만큼</b> — “shuncha, oʻshancha”. U <b>darajani emas,
miqdorni yoki tenglikni</b> koʻrsatadi: “qanchaki A boʻlsa,
shunchaki B”.</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--o">먹을 만큼</span>
     드세요.</p>
  <p class="pe-ex__uz">Yeydiganingizcha oling.</p>
  <p class="pe-ex__why">Yaʼni “qancha yeysiz — shuncha”. Miqdor.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">노력한 <span class="pe-hl pe-hl--o">만큼</span>
     결과가 나와요.</p>
  <p class="pe-ex__uz">Qancha harakat qilsangiz, shuncha natija chiqadi.</p>
  <p class="pe-ex__why">Oʻtgan ish uchun aniqlovchi
  <b>(으)ㄴ 만큼</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아프소나 씨는 언니<span class="pe-hl pe-hl--o">만큼</span>
     노래를 잘해요.</p>
  <p class="pe-ex__uz">Afsona opasi qadar yaxshi qoʻshiq aytadi.</p>
  <p class="pe-ex__why"><b>Ot bilan</b> — feʼlsiz ham ishlatiladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ikkalasi uchun ham tayyor qoliplar bor.</b>
  정도로 uchun — “<b>…gudek darajada</b>”, “<b>…guday</b>”:
  <em>“yigʻlab yuboradigan darajada”, “oʻlguday charchadim”</em>.
  만큼 uchun — “<b>…gancha</b>”, “<b>…gan qadar</b>”, “<b>qancha …
  shuncha</b>”: <em>“yeydiganingcha ol”, “opasi qadar”</em>.
  Diqqat qiling: “qancha … shuncha” juftligi ikkala tilda ham
  <b>ikki qismli</b> — koreyschada birinchi qism <b>만큼</b> bilan
  tugaydi.</p>
</div>

<h3>3. 정도로 va 만큼 — farq</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)ㄹ 정도로 — DARAJA</p>
    <p>Qanchalik <b>kuchli</b> ekanini koʻrsatadi. Koʻpincha
    boʻrttirma.</p>
    <p><small>배가 아플 정도로 웃었어요.</small></p>
    <p><small>(qorin ogʻrigani — kulgining <em>oʻlchov
    tayogʻi</em>)</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)ㄹ 만큼 — MIQDOR</p>
    <p>Qanchaligini <b>tenglashtiradi</b>: shuncha — shuncha.</p>
    <p><small>먹을 만큼 드세요.</small></p>
    <p><small>(yeyish miqdori — olish miqdoriga <em>teng</em>)</small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Koʻp holatda ikkalasi ham toʻgʻri</b> — masalan
  죽을 정도로 힘들었어요 va 죽을 만큼 힘들었어요 ikkalasi ham
  “oʻlguday qiyin edi” degani. Farq faqat ohangda: <b>정도로</b>
  darajaga, <b>만큼</b> miqdorga urgʻu beradi. Lekin
  <b>tenglashtirish</b> maʼnosida faqat 만큼 ishlaydi:
  ❌ <s>언니 정도로 노래를 잘해요</s>.</p>
</div>

<h3>4. Ot sifatida: 이 정도, 그만큼</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">이 <span class="pe-hl pe-hl--o">정도</span>면
     충분해요.</p>
  <p class="pe-ex__uz">Shuncha boʻlsa yetarli.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">노력했으니까 <span class="pe-hl pe-hl--o">그만큼</span>
     결과도 좋을 거예요.</p>
  <p class="pe-ex__uz">Harakat qilgansiz, shuning uchun natija ham
  shunchalik yaxshi boʻladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>웃었어요 배가 아플 정도로.</s></p>
  <p class="pe-good"><b>배가 아플 정도로</b> 웃었어요.</p>
  <p><small>Oʻlchov <b>oldin</b>, asosiy feʼl <b>keyin</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>배가 아픈 정도로 웃었어요.</s></p>
  <p class="pe-good">배가 <b>아플 정도로</b> 웃었어요.</p>
  <p><small>정도로 oldida <b>(으)ㄹ</b> aniqlovchisi turadi —
  hali boʻlmagan, faqat oʻlchov sifatida tasavvur qilingan
  holat.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>아프소나 씨는 언니 정도로 노래를 잘해요.</s></p>
  <p class="pe-good">아프소나 씨는 언니<b>만큼</b> 노래를 잘해요.</p>
  <p><small>Ikki odamni <b>tenglashtirish</b> — faqat
  <b>만큼</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>먹을 정도로 드세요.</s></p>
  <p class="pe-good"><b>먹을 만큼</b> 드세요.</p>
  <p><small>Bu yerda gap <b>miqdor</b> haqida — “qancha yeysiz,
  shuncha oling”.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 배가
  <span class="pe-blank"></span> 정도로 웃었어요. (아프다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>아플</b> — 정도로 oldida (으)ㄹ aniqlovchisi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring:
  <span class="pe-blank"></span> 만큼 드세요. (먹다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>먹을</b> — “yeydiganingizcha”.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 정도로 yoki 만큼?
  아프소나 씨는 언니<span class="pe-blank"></span> 노래를 잘해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>만큼</b> — ikki odamni tenglashtiryapmiz.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Nega
  <s>웃었어요 배가 아플 정도로</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Koreyschada oʻlchov <b>oldin</b> keladi:
    <b>배가 아플 정도로 웃었어요</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> “Koʻzni ocha olmaydigan
  darajada shamol kuchli edi” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>눈을 뜰 수 없을 정도로 바람이 강했어요.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Qancha harakat qilsangiz,
  shuncha natija chiqadi” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>노력한 만큼 결과가 나와요.</b> Oʻtgan ish → 은 만큼.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Bu gapni 한다체 ga oʻgiring
  (PK-74): 말도 못 할 정도로 피곤했어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>말도 못 할 정도로 피곤했다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ 정도로</b> — …gudek darajada</li>
  <li><b>(으)ㄹ 만큼</b> — …gancha, …gan qadar</li>
  <li><b>정도</b> — daraja, oʻlcham</li>
  <li><b>눈을 뜨다</b> — koʻz ochmoq</li>
  <li><b>강하다</b> — kuchli boʻlmoq</li>
  <li><b>충분하다</b> — yetarli boʻlmoq</li>
  <li><b>상상하다</b> — tasavvur qilmoq</li>
  <li><b>믿기 어렵다</b> — ishonish qiyin</li>
  <li><b>차이</b> — farq</li>
  <li><b>비교하다</b> — solishtirmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ 정도로</b> = daraja: “…gudek darajada”.
      <b>정도</b> = oʻlcham.</li>
    <li><b>(으)ㄹ 만큼</b> = miqdor va tenglik: “…gancha, …qadar”.</li>
    <li>Ikkalasida ham oldida <b>(으)ㄹ</b> aniqlovchisi turadi
      (oʻtgan ish uchun <b>(으)ㄴ 만큼</b>).</li>
    <li><b>Tartib:</b> oʻlchov birinchi, asosiy feʼl keyin —
      배가 아플 정도로 웃었어요.</li>
    <li>Ikki narsani <b>tenglashtirish</b> — faqat 만큼:
      언니만큼 잘해요.</li>
    <li>Ot sifatida ham: <b>이 정도</b>, <b>그만큼</b>.</li>
    <li>죽을 정도로 = 죽을 만큼 — koʻp holatda ikkalasi ham
      toʻgʻri.</li>
    <li>Oʻzbekcha juftlari: “<b>…gudek darajada</b>” va
      “<b>…gancha / …gan qadar</b>”.</li>
  </ul>
</div>
""",
    },
]
