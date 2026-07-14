# TOPIK II 쓰기 53 — drills 1–5 (see toc_topik_writing_53.txt).
# Import: python manage.py import_writing corner/management/commands/_writing_topik53_1_5.py --author=<AUTHOR>

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili resurslari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

PRACTICES = [

    # ── 53-1 · 1인 가구 증가 (line chart, 증가) ──────────────────────────
    {
        "qtype":   "53",
        "title":   "53-1: 1인 가구 증가",
        "summary": "Chiziqli grafik: yolgʻiz yashovchi xonadonlar ulushi oshib bormoqda. 증가하다, 전망되다 kabi shablon iboralarni oʻrganamiz.",
        "order":   1,
        "prompt":  '''<p>다음을 참고하여 '1인 가구 현황'에 대한 글을 200~300자로 쓰시오. 단, 글의 제목을 쓰지 마시오. <strong>(30점)</strong></p>''',
        "chart": '''<p class="wp-chart-title">1인 가구 비율</p>
<p class="small text-secondary text-center mb-2">조사 기관: 통계청</p>
<svg viewBox="0 0 480 230" role="img" aria-label="1인 가구 비율: 2000년 15%, 2010년 24%, 2020년 32%">
  <line class="wp-axis" x1="40" y1="190" x2="440" y2="190"/>
  <polyline class="wp-line" points="90,134 240,100 390,70"/>
  <circle class="wp-dot" cx="90" cy="134" r="4.5"/>
  <circle class="wp-dot" cx="240" cy="100" r="4.5"/>
  <circle class="wp-dot" cx="390" cy="70" r="4.5"/>
  <text class="wp-val" x="90" y="118">15%</text>
  <text class="wp-val" x="240" y="84">24%</text>
  <text class="wp-val" x="390" y="54">32%</text>
  <text class="wp-tick" x="90" y="212">2000년</text>
  <text class="wp-tick" x="240" y="212">2010년</text>
  <text class="wp-tick" x="390" y="212">2020년</text>
</svg>
<div class="wp-facts">
  <div class="wp-fact"><span class="wp-fact-tag">원인</span><ul><li>결혼에 대한 인식 변화</li><li>고령 인구 증가</li></ul></div>
  <div class="wp-fact"><span class="wp-fact-tag">전망</span><ul><li>2030년 — 40%에 이를 것</li></ul></div>
</div>''',
        "template_body": '''<p><span class="wp-blank" data-answer="통계청"></span>에서 1인 가구 <span class="cn-word" data-tr="ulush, foiz nisbati">비율</span>에 대한 <span class="cn-word" data-pos="verb" data-tr="soʻrov oʻtkazdi">조사를 실시하였다</span>. <span class="cn-word" data-tr="soʻrov natijasiga koʻra">조사 결과에 따르면</span> 1인 가구의 비율은 2000년 <span class="wp-blank" data-answer="15%" data-alt="15퍼센트"></span>에서 2010년 <span class="wp-blank" data-answer="24%" data-alt="24퍼센트"></span>, 2020년에는 <span class="wp-blank" data-answer="32%" data-alt="32퍼센트"></span>로 <span class="cn-word" data-pos="adv" data-tr="muntazam, toʻxtovsiz">꾸준히</span> <span class="cn-word" data-pos="verb" data-tr="oshdi, koʻpaydi">증가하였다</span>.</p>
<p>이렇게 1인 가구가 증가한 <span class="cn-word" data-tr="sabab">원인</span>으로는 첫째, <span class="wp-blank" data-answer="결혼" data-alt="결혼에 대한"></span>에 대한 <span class="cn-word" data-tr="qarash, tushuncha">인식</span>의 변화, 둘째, <span class="wp-blank" data-answer="고령 인구" data-alt="고령인구"></span>의 증가를 <span class="cn-word" data-pos="verb" data-tr="keltirish mumkin (sabab sifatida)">들 수 있다</span>.</p>
<p>이러한 <span class="cn-word" data-tr="tendensiya, yoʻnalish">추세</span>가 <span class="cn-word" data-pos="verb" data-tr="davom etsa">계속된다면</span> 2030년에는 1인 가구의 비율이 <span class="wp-blank" data-answer="40%" data-alt="40퍼센트"></span>에 <span class="cn-word" data-pos="verb" data-tr="yetishi prognoz qilinadi">이를 것으로 전망된다</span>.</p>''',
        "model_answer": '''<p>통계청에서 1인 가구 <span class="cn-word" data-tr="ulush, foiz nisbati">비율</span>에 대한 <span class="cn-word" data-pos="verb" data-tr="soʻrov oʻtkazdi">조사를 실시하였다</span>. <span class="cn-word" data-tr="soʻrov natijasiga koʻra">조사 결과에 따르면</span> 1인 가구의 비율은 2000년 15%에서 2010년 24%, 2020년에는 32%로 <span class="cn-word" data-pos="adv" data-tr="muntazam, toʻxtovsiz">꾸준히</span> <span class="cn-word" data-pos="verb" data-tr="oshdi, koʻpaydi">증가하였다</span>. 이렇게 1인 가구가 증가한 <span class="cn-word" data-tr="sabab">원인</span>으로는 첫째, 결혼에 대한 <span class="cn-word" data-tr="qarash, tushuncha">인식</span>의 변화, 둘째, 고령 인구의 증가를 <span class="cn-word" data-pos="verb" data-tr="keltirish mumkin (sabab sifatida)">들 수 있다</span>. 이러한 <span class="cn-word" data-tr="tendensiya, yoʻnalish">추세</span>가 <span class="cn-word" data-pos="verb" data-tr="davom etsa">계속된다면</span> 2030년에는 1인 가구의 비율이 40%에 <span class="cn-word" data-pos="verb" data-tr="yetishi prognoz qilinadi">이를 것으로 전망된다</span>.</p>
<p class="small text-secondary">(약 210자)</p>''',
        "tips": '''<ul>
<li>53-savol javobi doim 4 qadamdan iborat: <strong>조사 개요 → 결과 → 원인 → 전망</strong>. Shu tartibni yodlab oling — har qanday grafikga toʻgʻri keladi.</li>
<li>Birinchi jumla deyarli oʻzgarmaydi: <em>[기관]에서 [주제]에 대한 조사를 실시하였다.</em></li>
<li>Yozma uslub (문어체) shart: <em>-았/었다, -(느)ㄴ다</em>. <em>-아요/어요</em> ishlatsangiz ball yoʻqotasiz.</li>
<li>Grafikdagi HAMMA raqamni ishlating — yillar, foizlar, prognoz. Tekshiruvchi aynan shuni kutadi.</li>
<li>Oʻz fikringizni qoʻshmang — 53-savolda faqat berilgan maʼlumot yoziladi.</li>
</ul>''',
    },

    # ── 53-2 · 대학생이 선호하는 여가 활동 (paired bars 남/여) ───────────
    {
        "qtype":   "53",
        "title":   "53-2: 대학생이 선호하는 여가 활동",
        "summary": "Juft ustunli diagramma (남/여): talabalar sevimli mashgʻulotlarini taqqoslaymiz. 차지하다, 뒤를 이었다, 반면에 iboralari.",
        "order":   2,
        "prompt":  '''<p>다음을 참고하여 '대학생이 선호하는 여가 활동'에 대한 글을 200~300자로 쓰시오. 단, 글의 제목을 쓰지 마시오. <strong>(30점)</strong></p>''',
        "chart": '''<p class="wp-chart-title">대학생이 선호하는 여가 활동</p>
<p class="small text-secondary text-center mb-2">조사 기관: 한국대학교 · 대상: 대학생 500명 (남 250명, 여 250명)</p>
<div class="wp-legend"><span><span class="wp-legend-chip"></span>남학생</span><span><span class="wp-legend-chip wp-b2"></span>여학생</span></div>
<div class="wp-bars">
  <div class="wp-bar-row"><span class="wp-bar-label">운동</span><span class="wp-bar-track"><span class="wp-bar" style="width:100%"></span></span><span class="wp-bar-val">40%</span></div>
  <div class="wp-bar-row wp-row-sub"><span class="wp-bar-label"></span><span class="wp-bar-track"><span class="wp-bar wp-b2" style="width:50%"></span></span><span class="wp-bar-val">20%</span></div>
  <div class="wp-bar-row"><span class="wp-bar-label">게임</span><span class="wp-bar-track"><span class="wp-bar" style="width:75%"></span></span><span class="wp-bar-val">30%</span></div>
  <div class="wp-bar-row wp-row-sub"><span class="wp-bar-label"></span><span class="wp-bar-track"><span class="wp-bar wp-b2" style="width:38%"></span></span><span class="wp-bar-val">15%</span></div>
  <div class="wp-bar-row"><span class="wp-bar-label">영화 감상</span><span class="wp-bar-track"><span class="wp-bar" style="width:50%"></span></span><span class="wp-bar-val">20%</span></div>
  <div class="wp-bar-row wp-row-sub"><span class="wp-bar-label"></span><span class="wp-bar-track"><span class="wp-bar wp-b2" style="width:88%"></span></span><span class="wp-bar-val">35%</span></div>
  <div class="wp-bar-row"><span class="wp-bar-label">여행</span><span class="wp-bar-track"><span class="wp-bar" style="width:25%"></span></span><span class="wp-bar-val">10%</span></div>
  <div class="wp-bar-row wp-row-sub"><span class="wp-bar-label"></span><span class="wp-bar-track"><span class="wp-bar wp-b2" style="width:75%"></span></span><span class="wp-bar-val">30%</span></div>
</div>''',
        "template_body": '''<p>한국대학교에서 대학생 <span class="wp-blank" data-answer="500명" data-alt="오백 명"></span>을 <span class="cn-word" data-tr="...ni qamrab, ...oʻrtasida">대상으로</span> <span class="cn-word" data-pos="verb" data-tr="afzal koʻrmoq">선호하는</span> 여가 활동에 대한 조사를 실시하였다. 그 결과 남학생은 <span class="wp-blank" data-answer="운동"></span>이 40%로 <span class="cn-word" data-tr="eng yuqori chiqdi">가장 높게 나타났으며</span>, 게임이 <span class="wp-blank" data-answer="30%" data-alt="30퍼센트"></span>로 <span class="cn-word" data-pos="verb" data-tr="keyingi oʻrinni egalladi">뒤를 이었다</span>.</p>
<p><span class="cn-word" data-tr="aksincha, buning aksi oʻlaroq">반면에</span> 여학생은 <span class="wp-blank" data-answer="영화 감상" data-alt="영화감상|영화"></span>이 35%로 1위를 <span class="cn-word" data-pos="verb" data-tr="egallamoq">차지하였고</span>, <span class="wp-blank" data-answer="여행"></span>이 30%로 그 뒤를 이었다.</p>
<p>남학생은 <span class="cn-word" data-pos="adj" data-tr="faol, harakatchan">활동적인</span> 여가를 즐기는 반면에 여학생은 문화 활동을 더 선호하는 것을 알 수 있다. 이처럼 <span class="cn-word" data-tr="jins boʻyicha">성별에 따라</span> 선호하는 여가 활동에 <span class="cn-word" data-tr="farq bor">차이가 있는</span> 것으로 <span class="cn-word" data-pos="verb" data-tr="(natijada) koʻrindi, aniqlandi">나타났다</span>.</p>''',
        "model_answer": '''<p>한국대학교에서 대학생 500명을 <span class="cn-word" data-tr="...ni qamrab, ...oʻrtasida">대상으로</span> <span class="cn-word" data-pos="verb" data-tr="afzal koʻrmoq">선호하는</span> 여가 활동에 대한 조사를 실시하였다. 그 결과 남학생은 운동이 40%로 <span class="cn-word" data-tr="eng yuqori chiqdi">가장 높게 나타났으며</span>, 게임이 30%로 <span class="cn-word" data-pos="verb" data-tr="keyingi oʻrinni egalladi">뒤를 이었다</span>. <span class="cn-word" data-tr="aksincha, buning aksi oʻlaroq">반면에</span> 여학생은 영화 감상이 35%로 1위를 <span class="cn-word" data-pos="verb" data-tr="egallamoq">차지하였고</span>, 여행이 30%로 그 뒤를 이었다. 남학생은 <span class="cn-word" data-pos="adj" data-tr="faol, harakatchan">활동적인</span> 여가를 즐기는 반면에 여학생은 문화 활동을 더 선호하는 것을 알 수 있다. 이처럼 <span class="cn-word" data-tr="jins boʻyicha">성별에 따라</span> 선호하는 여가 활동에 <span class="cn-word" data-tr="farq bor">차이가 있는</span> 것으로 <span class="cn-word" data-pos="verb" data-tr="(natijada) koʻrindi, aniqlandi">나타났다</span>.</p>
<p class="small text-secondary">(약 240자)</p>''',
        "tips": '''<ul>
<li>Taqqoslash grafigi kelsa, <strong>반면에</strong> (aksincha) — sizning eng kuchli qurolingiz: ikki guruhni bitta jumlada qarama-qarshi qoʻyadi.</li>
<li>Reyting tasvirlash formulasi: <em>A이/가 X%로 가장 높게 나타났으며, B이/가 Y%로 뒤를 이었다.</em></li>
<li>Hamma toʻrt kategoriyani sanab oʻtirmang — 1–2-oʻrinlarni yozing, qolganini umumlashtiring. 300 belgidan oshmaslik muhim.</li>
<li>Oxirgi jumla — umumiy xulosa: <em>이처럼 ~에 따라 ~에 차이가 있는 것으로 나타났다.</em></li>
</ul>''',
    },

    # ── 53-3 · 외국인 관광객 수 변화 (line chart, 증가) ──────────────────
    {
        "qtype":   "53",
        "title":   "53-3: 외국인 관광객 수 변화",
        "summary": "Chiziqli grafik: Koreyaga kelgan sayyohlar soni. Katta raqamlar (만 명) bilan ishlash va 급격히 늘어나다 iborasi.",
        "order":   3,
        "prompt":  '''<p>다음을 참고하여 '한국을 방문한 외국인 관광객 현황'에 대한 글을 200~300자로 쓰시오. 단, 글의 제목을 쓰지 마시오. <strong>(30점)</strong></p>''',
        "chart": '''<p class="wp-chart-title">한국 방문 외국인 관광객 수</p>
<p class="small text-secondary text-center mb-2">조사 기관: 문화체육관광부</p>
<svg viewBox="0 0 480 230" role="img" aria-label="외국인 관광객 수: 2010년 880만 명, 2015년 1,320만 명, 2019년 1,750만 명">
  <line class="wp-axis" x1="40" y1="190" x2="440" y2="190"/>
  <polyline class="wp-line" points="90,124 240,91 390,59"/>
  <circle class="wp-dot" cx="90" cy="124" r="4.5"/>
  <circle class="wp-dot" cx="240" cy="91" r="4.5"/>
  <circle class="wp-dot" cx="390" cy="59" r="4.5"/>
  <text class="wp-val" x="90" y="108">880만 명</text>
  <text class="wp-val" x="240" y="75">1,320만 명</text>
  <text class="wp-val" x="390" y="43">1,750만 명</text>
  <text class="wp-tick" x="90" y="212">2010년</text>
  <text class="wp-tick" x="240" y="212">2015년</text>
  <text class="wp-tick" x="390" y="212">2019년</text>
</svg>
<div class="wp-facts">
  <div class="wp-fact"><span class="wp-fact-tag">원인</span><ul><li>한류의 세계적 인기</li><li>비자 절차 간소화</li></ul></div>
  <div class="wp-fact"><span class="wp-fact-tag">전망</span><ul><li>2030년 — 2,500만 명에 이를 것</li></ul></div>
</div>''',
        "template_body": '''<p><span class="wp-blank" data-answer="문화체육관광부"></span>에서 한국을 <span class="cn-word" data-pos="verb" data-tr="tashrif buyurmoq">방문한</span> 외국인 관광객 수를 조사하였다. 조사 결과에 따르면 외국인 관광객은 2010년 <span class="wp-blank" data-answer="880만 명" data-alt="880만명|880만"></span>에서 2015년 <span class="wp-blank" data-answer="1,320만 명" data-alt="1320만 명|1320만명|1,320만명"></span>, 2019년에는 <span class="wp-blank" data-answer="1,750만 명" data-alt="1750만 명|1750만명|1,750만명"></span>으로 <span class="cn-word" data-pos="adv" data-tr="keskin, tez surʼatda">급격히</span> <span class="cn-word" data-pos="verb" data-tr="koʻpaydi, ortdi">늘어났다</span>.</p>
<p>이렇게 관광객이 증가한 원인으로는 첫째, <span class="wp-blank" data-answer="한류"></span>가 세계적으로 <span class="cn-word" data-pos="verb" data-tr="mashhurlikka erishmoq">인기를 얻은</span> 것, 둘째, 비자 <span class="cn-word" data-tr="jarayon, tartib">절차</span>가 <span class="cn-word" data-pos="verb" data-tr="soddalashtirilmoq">간소화된</span> 것을 들 수 있다.</p>
<p><span class="cn-word" data-tr="shunga koʻra, shu sababli">이에 따라</span> 앞으로도 관광객 수는 <span class="cn-word" data-pos="adv" data-tr="doimiy ravishda">지속적으로</span> 증가하여 2030년에는 <span class="wp-blank" data-answer="2,500만 명" data-alt="2500만 명|2500만명|2,500만명"></span>에 이를 것으로 전망된다.</p>''',
        "model_answer": '''<p>문화체육관광부에서 한국을 <span class="cn-word" data-pos="verb" data-tr="tashrif buyurmoq">방문한</span> 외국인 관광객 수를 조사하였다. 조사 결과에 따르면 외국인 관광객은 2010년 880만 명에서 2015년 1,320만 명, 2019년에는 1,750만 명으로 <span class="cn-word" data-pos="adv" data-tr="keskin, tez surʼatda">급격히</span> <span class="cn-word" data-pos="verb" data-tr="koʻpaydi, ortdi">늘어났다</span>. 이렇게 관광객이 증가한 원인으로는 첫째, 한류가 세계적으로 <span class="cn-word" data-pos="verb" data-tr="mashhurlikka erishmoq">인기를 얻은</span> 것, 둘째, 비자 <span class="cn-word" data-tr="jarayon, tartib">절차</span>가 <span class="cn-word" data-pos="verb" data-tr="soddalashtirilmoq">간소화된</span> 것을 들 수 있다. <span class="cn-word" data-tr="shunga koʻra, shu sababli">이에 따라</span> 앞으로도 관광객 수는 <span class="cn-word" data-pos="adv" data-tr="doimiy ravishda">지속적으로</span> 증가하여 2030년에는 2,500만 명에 이를 것으로 전망된다.</p>
<p class="small text-secondary">(약 250자)</p>''',
        "tips": '''<ul>
<li>Katta sonlar koreyschada <strong>만</strong> (oʻn ming) birligida oʻqiladi: 880만 명 = 8,8 million kishi. Grafikdagi yozuvni AYNAN koʻchiring.</li>
<li>Tez oʻsishda <em>꾸준히</em> oʻrniga <strong>급격히</strong> (keskin) ishlating — grader aniq soʻz tanlaganingizni koʻradi.</li>
<li><em>증가하다</em> va <em>늘어나다</em> — sinonim: matnda ikkalasini almashtirib ishlatsangiz, takrorlanish kamayadi.</li>
<li>원인 formulasi: <em>원인으로는 첫째 ~ 것, 둘째 ~ 것을 들 수 있다.</em> Ot + 것 shakliga eʼtibor bering.</li>
</ul>''',
    },

    # ── 53-4 · 종이책 독서량 감소 (line chart, 감소) ─────────────────────
    {
        "qtype":   "53",
        "title":   "53-4: 종이책 독서량 감소",
        "summary": "Kamayish grafigi: endi 증가하다 emas, 감소하다 va 줄어들다. Pasayishni tasvirlashni oʻrganamiz.",
        "order":   4,
        "prompt":  '''<p>다음을 참고하여 '성인의 종이책 독서량 변화'에 대한 글을 200~300자로 쓰시오. 단, 글의 제목을 쓰지 마시오. <strong>(30점)</strong></p>''',
        "chart": '''<p class="wp-chart-title">성인 연간 종이책 독서량</p>
<p class="small text-secondary text-center mb-2">조사 기관: 문화체육관광부</p>
<svg viewBox="0 0 480 230" role="img" aria-label="성인 연간 독서량: 2013년 11권, 2017년 8권, 2021년 5권">
  <line class="wp-axis" x1="40" y1="190" x2="440" y2="190"/>
  <polyline class="wp-line" points="90,53 240,90 390,128"/>
  <circle class="wp-dot" cx="90" cy="53" r="4.5"/>
  <circle class="wp-dot" cx="240" cy="90" r="4.5"/>
  <circle class="wp-dot" cx="390" cy="128" r="4.5"/>
  <text class="wp-val" x="90" y="37">11권</text>
  <text class="wp-val" x="240" y="74">8권</text>
  <text class="wp-val" x="390" y="112">5권</text>
  <text class="wp-tick" x="90" y="212">2013년</text>
  <text class="wp-tick" x="240" y="212">2017년</text>
  <text class="wp-tick" x="390" y="212">2021년</text>
</svg>
<div class="wp-facts">
  <div class="wp-fact"><span class="wp-fact-tag">원인</span><ul><li>스마트폰 사용 시간 증가</li><li>영상 매체의 발달</li></ul></div>
  <div class="wp-fact"><span class="wp-fact-tag">전망</span><ul><li>독서량이 더욱 줄어들 것</li></ul></div>
</div>''',
        "template_body": '''<p>문화체육관광부에서 성인의 <span class="cn-word" data-tr="yillik">연간</span> <span class="cn-word" data-tr="oʻqish miqdori">독서량</span>을 조사하였다. 조사 결과에 따르면 성인 한 명이 일 년 동안 읽는 종이책은 2013년 <span class="wp-blank" data-answer="11권"></span>에서 2017년 <span class="wp-blank" data-answer="8권"></span>, 2021년에는 <span class="wp-blank" data-answer="5권"></span>으로 꾸준히 <span class="wp-blank" data-answer="감소하였다" data-alt="줄어들었다"></span>.</p>
<p>이렇게 독서량이 <span class="cn-word" data-pos="verb" data-tr="kamaymoq, qisqarmoq">줄어든</span> 원인으로는 첫째, <span class="wp-blank" data-answer="스마트폰" data-alt="스마트폰 사용 시간"></span> 사용 시간이 증가한 것, 둘째, <span class="cn-word" data-tr="video media (TV, YouTube...)">영상 매체</span>가 <span class="cn-word" data-pos="verb" data-tr="rivojlanmoq">발달한</span> 것을 들 수 있다.</p>
<p>이러한 추세가 계속된다면 앞으로 성인의 독서량은 <span class="cn-word" data-pos="adv" data-tr="yanada, yana ham">더욱</span> <span class="wp-blank" data-answer="줄어들" data-alt="감소할"></span> 것으로 전망된다.</p>''',
        "model_answer": '''<p>문화체육관광부에서 성인의 <span class="cn-word" data-tr="yillik">연간</span> <span class="cn-word" data-tr="oʻqish miqdori">독서량</span>을 조사하였다. 조사 결과에 따르면 성인 한 명이 일 년 동안 읽는 종이책은 2013년 11권에서 2017년 8권, 2021년에는 5권으로 꾸준히 <span class="cn-word" data-pos="verb" data-tr="kamaydi">감소하였다</span>. 이렇게 독서량이 <span class="cn-word" data-pos="verb" data-tr="kamaymoq, qisqarmoq">줄어든</span> 원인으로는 첫째, 스마트폰 사용 시간이 증가한 것, 둘째, <span class="cn-word" data-tr="video media (TV, YouTube...)">영상 매체</span>가 <span class="cn-word" data-pos="verb" data-tr="rivojlanmoq">발달한</span> 것을 들 수 있다. 이러한 추세가 계속된다면 앞으로 성인의 독서량은 <span class="cn-word" data-pos="adv" data-tr="yanada, yana ham">더욱</span> 줄어들 것으로 전망된다.</p>
<p class="small text-secondary">(약 220자)</p>''',
        "tips": '''<ul>
<li>Grafik PASTGA tushsa: <strong>감소하다 / 줄어들다</strong> (kamaymoq). 증가하다 bilan adashtirmang — bu eng koʻp uchraydigan xato.</li>
<li>Juftlarni yod oling: 증가하다 ↔ 감소하다, 늘어나다 ↔ 줄어들다, 높아지다 ↔ 낮아지다.</li>
<li>Kitob sanagichi — <strong>권</strong>: 11권 = 11 dona kitob. Birlikni tushirib qoldirmang.</li>
<li>Kamayish prognozi: <em>더욱 줄어들 것으로 전망된다</em> (yanada kamayishi kutilmoqda).</li>
</ul>''',
    },

    # ── 53-5 · 연령대별 온라인 쇼핑 이용률 (single bars) ─────────────────
    {
        "qtype":   "53",
        "title":   "53-5: 연령대별 온라인 쇼핑 이용률",
        "summary": "Ustunli diagramma yosh guruhlari boʻyicha: ~(으)ㄹ수록 qolipi va ~에 불과하다 iborasi bilan taqqoslash.",
        "order":   5,
        "prompt":  '''<p>다음을 참고하여 '연령대별 온라인 쇼핑 이용률'에 대한 글을 200~300자로 쓰시오. 단, 글의 제목을 쓰지 마시오. <strong>(30점)</strong></p>''',
        "chart": '''<p class="wp-chart-title">연령대별 온라인 쇼핑 이용률</p>
<p class="small text-secondary text-center mb-2">조사 기관: 통계청</p>
<div class="wp-bars">
  <div class="wp-bar-row"><span class="wp-bar-label">20대</span><span class="wp-bar-track"><span class="wp-bar" style="width:100%"></span></span><span class="wp-bar-val">92%</span></div>
  <div class="wp-bar-row"><span class="wp-bar-label">30대</span><span class="wp-bar-track"><span class="wp-bar" style="width:96%"></span></span><span class="wp-bar-val">88%</span></div>
  <div class="wp-bar-row"><span class="wp-bar-label">40대</span><span class="wp-bar-track"><span class="wp-bar" style="width:82%"></span></span><span class="wp-bar-val">75%</span></div>
  <div class="wp-bar-row"><span class="wp-bar-label">50대</span><span class="wp-bar-track"><span class="wp-bar" style="width:63%"></span></span><span class="wp-bar-val">58%</span></div>
  <div class="wp-bar-row"><span class="wp-bar-label">60대 이상</span><span class="wp-bar-track"><span class="wp-bar" style="width:37%"></span></span><span class="wp-bar-val">34%</span></div>
</div>
<div class="wp-facts">
  <div class="wp-fact"><span class="wp-fact-tag">원인</span><ul><li>스마트폰의 보급</li><li>간편 결제 서비스의 발달</li></ul></div>
</div>''',
        "template_body": '''<p>통계청에서 <span class="cn-word" data-tr="yosh guruhlari boʻyicha">연령대별</span> 온라인 쇼핑 <span class="cn-word" data-tr="foydalanish darajasi">이용률</span>을 조사하였다. 조사 결과에 따르면 <span class="wp-blank" data-answer="20대"></span>의 이용률이 <span class="wp-blank" data-answer="92%" data-alt="92퍼센트"></span>로 가장 높게 나타났으며, 30대가 <span class="wp-blank" data-answer="88%" data-alt="88퍼센트"></span>로 뒤를 이었다.</p>
<p>반면에 <span class="wp-blank" data-answer="60대 이상" data-alt="60대"></span>은 34%<span class="cn-word" data-tr="...dan iborat xolos, atigi">에 불과하여</span> 연령이 <span class="cn-word" data-pos="verb" data-tr="oshgan sari (qolip: -(으)ㄹ수록)">높아질수록</span> 이용률이 <span class="cn-word" data-pos="verb" data-tr="pasaymoq">낮아지는</span> 것으로 나타났다.</p>
<p>이처럼 온라인 쇼핑 이용률이 높은 원인으로는 스마트폰이 널리 <span class="cn-word" data-pos="verb" data-tr="keng tarqalmoq">보급되고</span> <span class="wp-blank" data-answer="간편 결제" data-alt="간편결제"></span> 서비스가 발달하여 쇼핑이 <span class="cn-word" data-pos="adj" data-tr="qulay">편리해졌기</span> 때문이다. 앞으로 온라인 쇼핑 이용률은 더욱 높아질 것으로 전망된다.</p>''',
        "model_answer": '''<p>통계청에서 <span class="cn-word" data-tr="yosh guruhlari boʻyicha">연령대별</span> 온라인 쇼핑 <span class="cn-word" data-tr="foydalanish darajasi">이용률</span>을 조사하였다. 조사 결과에 따르면 20대의 이용률이 92%로 가장 높게 나타났으며, 30대가 88%로 뒤를 이었다. 반면에 60대 이상은 34%<span class="cn-word" data-tr="...dan iborat xolos, atigi">에 불과하여</span> 연령이 <span class="cn-word" data-pos="verb" data-tr="oshgan sari (qolip: -(으)ㄹ수록)">높아질수록</span> 이용률이 <span class="cn-word" data-pos="verb" data-tr="pasaymoq">낮아지는</span> 것으로 나타났다. 이처럼 온라인 쇼핑 이용률이 높은 원인으로는 스마트폰이 널리 <span class="cn-word" data-pos="verb" data-tr="keng tarqalmoq">보급되고</span> 간편 결제 서비스가 발달하여 쇼핑이 <span class="cn-word" data-pos="adj" data-tr="qulay">편리해졌기</span> 때문이다. 앞으로 온라인 쇼핑 이용률은 더욱 높아질 것으로 전망된다.</p>
<p class="small text-secondary">(약 240자)</p>''',
        "tips": '''<ul>
<li>Yosh guruhlari grafigida hammasini sanamang: <strong>eng yuqori + ikkinchi + eng past</strong> — shu uchtasi yetadi.</li>
<li>Kichik raqamni taʼkidlash uchun: <em>~에 불과하다</em> (atigi ...xolos). Bu ibora yuqori ball beradi.</li>
<li>Qonuniyatni bitta jumlada ayting: <em>연령이 높아질수록 이용률이 낮아지는 것으로 나타났다</em> — <strong>-(으)ㄹ수록</strong> qolipi aynan shu yerda kerak.</li>
<li>원인 bitta boʻlsa: <em>원인으로는 ~기 때문이다</em> shakli ham mumkin.</li>
</ul>''',
    },
]
