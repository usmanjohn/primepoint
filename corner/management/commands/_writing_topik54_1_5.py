# TOPIK II 쓰기 54 — drills 1–5 (see toc_topik_writing_54.txt).
# Import: python manage.py import_writing corner/management/commands/_writing_topik54_1_5.py --author=<AUTHOR>

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili resurslari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

PROMPT_54 = '''<p>다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰시오. 단, 문제를 그대로 옮겨 쓰지 마시오. <strong>(50점)</strong></p>'''

PRACTICES = [

    # ── 54-1 · 의사소통의 중요성과 방법 (중요성+방법형) ─────────────────
    {
        "qtype":   "54",
        "title":   "54-1: 의사소통의 중요성과 방법",
        "summary": "Insho, 'muhimlik+usul' turi: 서론-본론-결론 skeleti va uning oltin iboralari bilan birinchi tanishuv.",
        "order":   1,
        "prompt":  PROMPT_54,
        "chart": '''<div class="wp-passage">
<p>사람은 혼자 살 수 없으며 다른 사람과 관계를 맺으며 살아간다. 이때 의사소통은 관계를 유지하는 데 중요한 역할을 한다. 아래의 내용을 중심으로 '의사소통의 중요성과 방법'에 대한 자신의 생각을 쓰라.</p>
<ul>
<li>의사소통은 왜 중요한가?</li>
<li>의사소통이 잘 이루어지지 않는 이유는 무엇인가?</li>
<li>의사소통을 원활하게 하는 방법은 무엇인가?</li>
</ul>
</div>''',
        "template_body": '''<p class="wp-part">서론</p>
<p>우리는 살면서 가족, 친구, 직장 동료 등 수많은 사람들과 <span class="cn-word" data-tr="munosabat oʻrnatmoq">관계를 맺는다</span>. 이러한 관계 속에서 생각과 감정을 주고받는 <span class="wp-blank" data-answer="의사소통"></span>은 좋은 관계를 유지하는 데 <span class="cn-word" data-tr="muhim rol oʻynaydi (insho iborasi)">중요한 역할을 한다</span>. 의사소통이 <span class="cn-word" data-pos="adv" data-tr="bemalol, silliq">원활하게</span> 이루어지면 서로를 깊이 이해하게 되고 불필요한 <span class="cn-word" data-tr="nizo, kelishmovchilik">갈등</span>도 줄어들기 <span class="cn-word" data-tr="...gani uchun (sabab, gap oxirida)">때문이다</span>.</p>
<p class="wp-part">본론 1</p>
<p>그런데 우리 주변에는 의사소통이 잘 이루어지지 않아 어려움을 겪는 사람이 적지 않다. 의사소통이 어려운 이유는 사람마다 살아온 환경과 <span class="cn-word" data-tr="qadriyatlar, dunyoqarash">가치관</span>이 다르기 <span class="wp-blank" data-answer="때문이다"></span>. 서로 다르다는 사실을 잊고 자신의 <span class="cn-word" data-tr="pozitsiya, nuqtai nazar">입장</span>에서만 생각하면 상대방의 말을 <span class="cn-word" data-tr="notoʻgʻri tushunish oson (-기 쉽다)">오해하기 쉽다</span>. 이러한 오해가 쌓이면 관계가 나빠지고 심한 경우 갈등으로 이어지기도 한다.</p>
<p class="wp-part">본론 2</p>
<p><span class="cn-word" data-tr="unday boʻlsa (yangi savolga oʻtish)">그렇다면</span> 의사소통을 원활하게 하기 위해서는 <span class="wp-blank" data-answer="어떻게 해야 할까" data-alt="어떻게 해야 하는가"></span>? <span class="cn-word" data-pos="adv" data-tr="avvalo, birinchidan">먼저</span> 상대방의 말을 끝까지 듣는 <span class="cn-word" data-tr="munosabat, yondashuv">태도</span>가 필요하다. 말을 자르지 않고 들어 주는 것만으로도 상대방은 <span class="cn-word" data-pos="verb" data-tr="hurmat qilinmoq">존중받는다고</span> 느끼게 된다. <span class="wp-blank" data-answer="다음으로" data-alt="또한|둘째"></span> 자신의 생각을 <span class="cn-word" data-pos="adv" data-tr="ochiq, samimiy tarzda">솔직하게</span>, 그러나 예의 있게 표현해야 한다. <span class="wp-blank" data-answer="예를 들어" data-alt="예컨대"></span> 기분이 상했을 때 감정적으로 말하지 않고 그 이유를 차분하게 설명하면 불필요한 오해를 막을 수 있다.</p>
<p class="wp-part">결론</p>
<p>지금까지 의사소통의 중요성과 방법에 대해 <span class="wp-blank" data-answer="살펴보았다" data-alt="알아보았다"></span>. 원활한 의사소통은 <span class="cn-word" data-pos="adv" data-tr="oʻz-oʻzidan">저절로</span> 이루어지는 것이 아니라 서로를 이해하려는 노력에서 시작된다. 따라서 우리는 상대방의 입장에서 생각하고 끝까지 들으려는 자세를 갖추도록 <span class="wp-blank" data-answer="노력해야 할 것이다" data-alt="노력해야 한다"></span>.</p>''',
        "model_answer": '''<p class="wp-part">서론</p>
<p>우리는 살면서 가족, 친구, 직장 동료 등 수많은 사람들과 <span class="cn-word" data-tr="munosabat oʻrnatmoq">관계를 맺는다</span>. 이러한 관계 속에서 생각과 감정을 주고받는 의사소통은 좋은 관계를 유지하는 데 <span class="cn-word" data-tr="muhim rol oʻynaydi (insho iborasi)">중요한 역할을 한다</span>. 의사소통이 <span class="cn-word" data-pos="adv" data-tr="bemalol, silliq">원활하게</span> 이루어지면 서로를 깊이 이해하게 되고 불필요한 <span class="cn-word" data-tr="nizo, kelishmovchilik">갈등</span>도 줄어들기 때문이다.</p>
<p class="wp-part">본론 1</p>
<p>그런데 우리 주변에는 의사소통이 잘 이루어지지 않아 어려움을 겪는 사람이 적지 않다. 의사소통이 어려운 이유는 사람마다 살아온 환경과 <span class="cn-word" data-tr="qadriyatlar, dunyoqarash">가치관</span>이 다르기 때문이다. 서로 다르다는 사실을 잊고 자신의 <span class="cn-word" data-tr="pozitsiya, nuqtai nazar">입장</span>에서만 생각하면 상대방의 말을 <span class="cn-word" data-tr="notoʻgʻri tushunish oson (-기 쉽다)">오해하기 쉽다</span>. 이러한 오해가 쌓이면 관계가 나빠지고 심한 경우 갈등으로 이어지기도 한다.</p>
<p class="wp-part">본론 2</p>
<p><span class="cn-word" data-tr="unday boʻlsa (yangi savolga oʻtish)">그렇다면</span> 의사소통을 원활하게 하기 위해서는 어떻게 해야 할까? <span class="cn-word" data-pos="adv" data-tr="avvalo, birinchidan">먼저</span> 상대방의 말을 끝까지 듣는 <span class="cn-word" data-tr="munosabat, yondashuv">태도</span>가 필요하다. 말을 자르지 않고 들어 주는 것만으로도 상대방은 <span class="cn-word" data-pos="verb" data-tr="hurmat qilinmoq">존중받는다고</span> 느끼게 된다. 다음으로 자신의 생각을 <span class="cn-word" data-pos="adv" data-tr="ochiq, samimiy tarzda">솔직하게</span>, 그러나 예의 있게 표현해야 한다. <span class="cn-word" data-tr="masalan (misol kiritish)">예를 들어</span> 기분이 상했을 때 감정적으로 말하지 않고 그 이유를 차분하게 설명하면 불필요한 오해를 막을 수 있다.</p>
<p class="wp-part">결론</p>
<p>지금까지 의사소통의 중요성과 방법에 대해 <span class="cn-word" data-tr="koʻrib chiqdik (xulosa iborasi)">살펴보았다</span>. 원활한 의사소통은 <span class="cn-word" data-pos="adv" data-tr="oʻz-oʻzidan">저절로</span> 이루어지는 것이 아니라 서로를 이해하려는 노력에서 시작된다. 따라서 우리는 상대방의 입장에서 생각하고 끝까지 들으려는 자세를 갖추도록 <span class="cn-word" data-tr="harakat qilishimiz lozim (insho yakuni)">노력해야 할 것이다</span>.</p>
<p class="small text-secondary">(약 660자)</p>''',
        "tips": '''<ul>
<li>54-insho skeleti — 4 xatboshi: <strong>서론</strong> (mavzuni kiritish, ~20%) → <strong>본론 1, 2</strong> (savollarga javob, ~60%) → <strong>결론</strong> (xulosa, ~20%). Savol qutisidagi HAR BIR savolga javob bering — biri qolsa, mazmun balli kesiladi.</li>
<li>Oltin iboralar shu inshoda: <em>~는 데 중요한 역할을 한다</em> (서론), <em>그 이유는 ~기 때문이다</em>, <em>그렇다면 ~려면 어떻게 해야 할까?</em> (본론 koʻprigi), <em>먼저/다음으로</em>, <em>지금까지 ~에 대해 살펴보았다. 따라서 ~아/어야 할 것이다</em> (결론).</li>
<li>Savol matnini AYNAN koʻchirmang (문제를 그대로 옮겨 쓰지 마시오) — oʻz soʻzlaringiz bilan qayta yozing, aks holda oʻsha qism belgilanmaydi.</li>
<li>Faqat yozma uslub: <em>-(느)ㄴ다</em>. Bitta ham <em>-아요/어요</em> boʻlmasin.</li>
<li>Vaqt: reja (개요) uchun 5 daqiqa ajrating — har xatboshiga bittadan savol. 54 uchun jami ~30 daqiqa qoldiring.</li>
</ul>''',
    },

    # ── 54-2 · 실패의 가치 (가치형) ─────────────────────────────────────
    {
        "qtype":   "54",
        "title":   "54-2: 실패의 가치",
        "summary": "Insho, 'qadriyat' turi: salbiy tushunchaning ijobiy tomonini ochish — 그러나, 밑거름 kabi iboralar.",
        "order":   2,
        "prompt":  PROMPT_54,
        "chart": '''<div class="wp-passage">
<p>사람은 누구나 살면서 크고 작은 실패를 경험한다. 실패는 고통스럽지만 우리에게 많은 것을 가르쳐 주기도 한다. 아래의 내용을 중심으로 '실패의 가치'에 대한 자신의 생각을 쓰라.</p>
<ul>
<li>사람들은 왜 실패를 두려워하는가?</li>
<li>실패를 통해 무엇을 배울 수 있는가?</li>
<li>실패를 대하는 바람직한 태도는 무엇인가?</li>
</ul>
</div>''',
        "template_body": '''<p class="wp-part">서론</p>
<p>사람은 누구나 성공하기를 바라지만 살다 보면 크고 작은 <span class="wp-blank" data-answer="실패"></span>를 <span class="cn-word" data-tr="chetlab oʻtib boʻlmaydi">피할 수 없다</span>. 그런데 많은 사람들이 실패를 <span class="cn-word" data-pos="verb" data-tr="qoʻrqmoq">두려워한다</span>. 그 이유는 실패를 곧 끝이라고 생각하기 때문이다. 오랜 시간과 노력이 <span class="cn-word" data-tr="behuda mehnat">헛수고</span>가 되었다는 생각에 <span class="cn-word" data-tr="oʻziga ishonchni yoʻqotmoq">자신감을 잃기도</span> 한다.</p>
<p class="wp-part">본론 1</p>
<p><span class="cn-word" data-tr="lekin (burilish)">그러나</span> 실패는 우리에게 소중한 <span class="cn-word" data-tr="saboq, taʼlim">가르침</span>을 준다. <span class="cn-word" data-pos="adv" data-tr="avvalo">우선</span> 실패를 통해 자신의 부족한 점을 발견할 수 있다. 성공했을 때는 보이지 않던 문제점이 실패를 겪으면서 분명하게 <span class="cn-word" data-pos="verb" data-tr="namoyon boʻlmoq">드러나기</span> <span class="wp-blank" data-answer="때문이다"></span>. <span class="wp-blank" data-answer="또한" data-alt="그리고|다음으로"></span> 실패는 어려움을 <span class="cn-word" data-tr="yengib oʻtmoq">이겨 내는</span> 힘을 길러 준다. 실제로 큰 성공을 거둔 사람들 중에는 수많은 실패를 <span class="cn-word" data-tr="bosib oʻtib qaddini rostlamoq">딛고 일어선</span> 사람이 적지 않다.</p>
<p class="wp-part">본론 2</p>
<p>그렇다면 실패를 대하는 <span class="cn-word" data-pos="adj" data-tr="maqbul, toʻgʻri">바람직한</span> 태도는 <span class="wp-blank" data-answer="무엇인가" data-alt="무엇일까"></span>? 무엇보다 실패를 끝이 아니라 <span class="wp-blank" data-answer="배움의 과정" data-alt="배우는 과정"></span>으로 받아들여야 한다. 실패했을 때 <span class="cn-word" data-pos="verb" data-tr="tushkunlikka tushmoq">좌절만 하고</span> 있으면 아무것도 달라지지 않는다. 오히려 도전하는 것 자체를 포기하게 될 뿐이다. 실패의 원인을 차분히 분석하고 같은 실수를 반복하지 않도록 노력한다면 실패는 성공으로 가는 <span class="cn-word" data-tr="poydevor, oʻgʻit (muvaffaqiyat asosi)">밑거름</span>이 될 수 있다.</p>
<p class="wp-part">결론</p>
<p>지금까지 실패의 가치에 대해 <span class="wp-blank" data-answer="살펴보았다" data-alt="알아보았다"></span>. 실패가 두려워서 아무것도 <span class="cn-word" data-pos="verb" data-tr="urinib koʻrmoq">시도하지</span> 않는 사람은 아무것도 배울 수 없다. 실패의 경험은 그 자체로 소중한 자산이 되기 때문이다. 따라서 우리는 실패를 두려워하지 말고 그 속에서 배우려는 자세를 <span class="wp-blank" data-answer="가져야 할 것이다" data-alt="가져야 한다"></span>.</p>''',
        "model_answer": '''<p class="wp-part">서론</p>
<p>사람은 누구나 성공하기를 바라지만 살다 보면 크고 작은 실패를 <span class="cn-word" data-tr="chetlab oʻtib boʻlmaydi">피할 수 없다</span>. 그런데 많은 사람들이 실패를 <span class="cn-word" data-pos="verb" data-tr="qoʻrqmoq">두려워한다</span>. 그 이유는 실패를 곧 끝이라고 생각하기 때문이다. 오랜 시간과 노력이 <span class="cn-word" data-tr="behuda mehnat">헛수고</span>가 되었다는 생각에 <span class="cn-word" data-tr="oʻziga ishonchni yoʻqotmoq">자신감을 잃기도</span> 한다.</p>
<p class="wp-part">본론 1</p>
<p><span class="cn-word" data-tr="lekin (burilish)">그러나</span> 실패는 우리에게 소중한 <span class="cn-word" data-tr="saboq, taʼlim">가르침</span>을 준다. <span class="cn-word" data-pos="adv" data-tr="avvalo">우선</span> 실패를 통해 자신의 부족한 점을 발견할 수 있다. 성공했을 때는 보이지 않던 문제점이 실패를 겪으면서 분명하게 <span class="cn-word" data-pos="verb" data-tr="namoyon boʻlmoq">드러나기</span> 때문이다. 또한 실패는 어려움을 <span class="cn-word" data-tr="yengib oʻtmoq">이겨 내는</span> 힘을 길러 준다. 실제로 큰 성공을 거둔 사람들 중에는 수많은 실패를 <span class="cn-word" data-tr="bosib oʻtib qaddini rostlamoq">딛고 일어선</span> 사람이 적지 않다.</p>
<p class="wp-part">본론 2</p>
<p>그렇다면 실패를 대하는 <span class="cn-word" data-pos="adj" data-tr="maqbul, toʻgʻri">바람직한</span> 태도는 무엇인가? 무엇보다 실패를 끝이 아니라 배움의 과정으로 받아들여야 한다. 실패했을 때 <span class="cn-word" data-pos="verb" data-tr="tushkunlikka tushmoq">좌절만 하고</span> 있으면 아무것도 달라지지 않는다. 오히려 도전하는 것 자체를 포기하게 될 뿐이다. 실패의 원인을 차분히 분석하고 같은 실수를 반복하지 않도록 노력한다면 실패는 성공으로 가는 <span class="cn-word" data-tr="poydevor, oʻgʻit (muvaffaqiyat asosi)">밑거름</span>이 될 수 있다.</p>
<p class="wp-part">결론</p>
<p>지금까지 실패의 가치에 대해 살펴보았다. 실패가 두려워서 아무것도 <span class="cn-word" data-pos="verb" data-tr="urinib koʻrmoq">시도하지</span> 않는 사람은 아무것도 배울 수 없다. 실패의 경험은 그 자체로 소중한 자산이 되기 때문이다. 따라서 우리는 실패를 두려워하지 말고 그 속에서 배우려는 자세를 가져야 할 것이다.</p>
<p class="small text-secondary">(약 640자)</p>''',
        "tips": '''<ul>
<li>'Qadriyat' turi insho harakati: salbiy koʻringan narsaning (실패) ICHIDAN foyda topish. Burilish nuqtasi — <strong>그러나</strong>: undan oldin umumiy qarash, undan keyin sizning tezisingiz.</li>
<li>본론da har fikrni misol yoki sabab bilan mustahkamlang: <em>실제로 ~는 사람이 적지 않다</em> — dalil kiritishning oson usuli.</li>
<li><em>A가 아니라 B로 받아들이다</em> (A emas, B deb qabul qilmoq) — qayta taʼriflash qolipi; 54da juda koʻp ishlaydi.</li>
<li>결론da yangi fikr kiritmang — faqat umumlashtiring va <em>따라서 ~아/어야 할 것이다</em> bilan yakunlang.</li>
<li>실패는 성공의 어머니 kabi maqollarni bilsangiz ishlatish mumkin, lekin majburiy emas — tabiiy boʻlsagina qoʻshing.</li>
</ul>''',
    },

    # ── 54-3 · 조기 외국어 교육 (찬반·장단점형) ─────────────────────────
    {
        "qtype":   "54",
        "title":   "54-3: 조기 외국어 교육의 장점과 문제점",
        "summary": "Insho, 'tarafdor-qarshi' turi: 찬성하는 사람들은 / 반면에 qoliplari va oʻz pozitsiyasini bildirish.",
        "order":   3,
        "prompt":  PROMPT_54,
        "chart": '''<div class="wp-passage">
<p>요즘 어린 나이부터 자녀에게 외국어를 가르치는 부모가 늘고 있다. 이러한 조기 외국어 교육에 대한 의견은 찬성과 반대로 나뉜다. 아래의 내용을 중심으로 '조기 외국어 교육의 장점과 문제점'에 대한 자신의 생각을 쓰라.</p>
<ul>
<li>조기 외국어 교육의 장점은 무엇인가?</li>
<li>조기 외국어 교육의 문제점은 무엇인가?</li>
<li>조기 외국어 교육에 대한 자신의 의견은 어떠한가?</li>
</ul>
</div>''',
        "template_body": '''<p class="wp-part">서론</p>
<p><span class="cn-word" data-tr="globallashuv">세계화</span> 시대가 되면서 외국어 능력은 점점 중요해지고 있다. <span class="cn-word" data-tr="shunga koʻra">이에 따라</span> 어린 나이부터 자녀에게 <span class="wp-blank" data-answer="외국어"></span>를 가르치는 부모도 늘고 있다. 그러나 <span class="cn-word" data-tr="erta yoshdan berilgan taʼlim">조기 교육</span>이 아이에게 정말 도움이 되는지에 대해서는 <span class="cn-word" data-tr="fikrlar ikkiga boʻlinadi">의견이 나뉜다</span>.</p>
<p class="wp-part">본론 1</p>
<p>조기 외국어 교육에 <span class="cn-word" data-pos="verb" data-tr="yoqlamoq, tarafdor boʻlmoq">찬성하는</span> 사람들은 어릴수록 언어를 빨리 배운다고 <span class="wp-blank" data-answer="주장한다" data-alt="말한다|이야기한다"></span>. 실제로 어린아이는 새로운 소리를 듣고 따라 하는 능력이 <span class="cn-word" data-pos="adj" data-tr="ajoyib, ustun">뛰어나서</span> 발음을 자연스럽게 <span class="cn-word" data-pos="verb" data-tr="oʻzlashtirmoq">익힐</span> 수 있다. 또한 어릴 때부터 다른 문화를 <span class="cn-word" data-pos="verb" data-tr="duch kelmoq, tanishmoq">접하면</span> 열린 <span class="cn-word" data-tr="fikrlash tarzi">사고방식</span>을 기르는 데에도 도움이 된다. 이 시기를 놓치면 같은 것을 배우는 데 더 많은 시간과 노력이 든다고 보는 것이다.</p>
<p class="wp-part">본론 2</p>
<p><span class="wp-blank" data-answer="반면에" data-alt="반면|한편"></span> 조기 외국어 교육의 <span class="wp-blank" data-answer="부정적인 측면" data-alt="문제점|단점"></span>을 <span class="cn-word" data-pos="verb" data-tr="koʻrsatib oʻtmoq, tanqid qilmoq">지적하는</span> 사람들도 있다. <span class="cn-word" data-tr="ona tili">모국어</span>가 완성되지 않은 상태에서 외국어를 배우면 두 언어 모두 제대로 익히지 못할 수 있기 때문이다. 그리고 <span class="cn-word" data-pos="adj" data-tr="haddan ortiq">지나친</span> 학습 <span class="cn-word" data-tr="yuk, bosim">부담</span>은 아이에게 스트레스를 주어 <span class="wp-blank" data-answer="오히려" data-alt="도리어"></span> 공부에 대한 <span class="cn-word" data-tr="qiziqishni yoʻqotmoq">흥미를 잃게</span> 만들기도 한다.</p>
<p class="wp-part">결론</p>
<p>나는 조기 외국어 교육이 필요하더라도 아이의 흥미와 발달 단계를 <span class="cn-word" data-pos="verb" data-tr="hisobga olmoq">고려해서</span> 이루어져야 한다고 <span class="wp-blank" data-answer="생각한다" data-alt="본다|믿는다"></span>. <span class="cn-word" data-pos="adv" data-tr="zoʻrlab, majburan">억지로</span> 시키는 공부가 아니라 놀이처럼 자연스럽게 접하게 한다면 외국어는 아이에게 즐거운 경험이 될 것이다. 중요한 것은 얼마나 일찍 시작하느냐가 아니라 아이가 얼마나 즐겁게 배우느냐이다.</p>''',
        "model_answer": '''<p class="wp-part">서론</p>
<p><span class="cn-word" data-tr="globallashuv">세계화</span> 시대가 되면서 외국어 능력은 점점 중요해지고 있다. <span class="cn-word" data-tr="shunga koʻra">이에 따라</span> 어린 나이부터 자녀에게 외국어를 가르치는 부모도 늘고 있다. 그러나 <span class="cn-word" data-tr="erta yoshdan berilgan taʼlim">조기 교육</span>이 아이에게 정말 도움이 되는지에 대해서는 <span class="cn-word" data-tr="fikrlar ikkiga boʻlinadi">의견이 나뉜다</span>.</p>
<p class="wp-part">본론 1</p>
<p>조기 외국어 교육에 <span class="cn-word" data-pos="verb" data-tr="yoqlamoq, tarafdor boʻlmoq">찬성하는</span> 사람들은 어릴수록 언어를 빨리 배운다고 <span class="cn-word" data-pos="verb" data-tr="daʼvo qilmoq, taʼkidlamoq">주장한다</span>. 실제로 어린아이는 새로운 소리를 듣고 따라 하는 능력이 <span class="cn-word" data-pos="adj" data-tr="ajoyib, ustun">뛰어나서</span> 발음을 자연스럽게 <span class="cn-word" data-pos="verb" data-tr="oʻzlashtirmoq">익힐</span> 수 있다. 또한 어릴 때부터 다른 문화를 <span class="cn-word" data-pos="verb" data-tr="duch kelmoq, tanishmoq">접하면</span> 열린 <span class="cn-word" data-tr="fikrlash tarzi">사고방식</span>을 기르는 데에도 도움이 된다. 이 시기를 놓치면 같은 것을 배우는 데 더 많은 시간과 노력이 든다고 보는 것이다.</p>
<p class="wp-part">본론 2</p>
<p>반면에 조기 외국어 교육의 부정적인 측면을 <span class="cn-word" data-pos="verb" data-tr="koʻrsatib oʻtmoq, tanqid qilmoq">지적하는</span> 사람들도 있다. <span class="cn-word" data-tr="ona tili">모국어</span>가 완성되지 않은 상태에서 외국어를 배우면 두 언어 모두 제대로 익히지 못할 수 있기 때문이다. 그리고 <span class="cn-word" data-pos="adj" data-tr="haddan ortiq">지나친</span> 학습 <span class="cn-word" data-tr="yuk, bosim">부담</span>은 아이에게 스트레스를 주어 오히려 공부에 대한 <span class="cn-word" data-tr="qiziqishni yoʻqotmoq">흥미를 잃게</span> 만들기도 한다.</p>
<p class="wp-part">결론</p>
<p>나는 조기 외국어 교육이 필요하더라도 아이의 흥미와 발달 단계를 <span class="cn-word" data-pos="verb" data-tr="hisobga olmoq">고려해서</span> 이루어져야 한다고 생각한다. <span class="cn-word" data-pos="adv" data-tr="zoʻrlab, majburan">억지로</span> 시키는 공부가 아니라 놀이처럼 자연스럽게 접하게 한다면 외국어는 아이에게 즐거운 경험이 될 것이다. 중요한 것은 얼마나 일찍 시작하느냐가 아니라 아이가 얼마나 즐겁게 배우느냐이다.</p>
<p class="small text-secondary">(약 620자)</p>''',
        "tips": '''<ul>
<li>'Tarafdor-qarshi' turida oltin juftlik: <em>찬성하는 사람들은 ~다고 주장한다</em> ↔ <em>반면에 ~을 지적하는 사람들도 있다</em>. Ikkala tomonni ham yoriting — bir tomonlama insho ball yoʻqotadi.</li>
<li>Oʻz fikringiz FAQAT 결론da: <em>나는 ~다고 생각한다</em>. Yozma uslubda 저는 emas, <strong>나는</strong>.</li>
<li>Eng kuchli pozitsiya — oʻrtachasi: "kerak, LEKIN shart bilan" (<em>~더라도 ~을 고려해야 한다</em>). Bunday javobni asoslash osonroq.</li>
<li>장점/단점 sanashda parallel qurilma ishlating: 또한 / 그리고 bilan ikkinchi dalilni qoʻshing.</li>
<li>Savol qutisida 3 savol bor: 장점 → 본론 1, 문제점 → 본론 2, 자신의 의견 → 결론. Skelet tayyor!</li>
</ul>''',
    },

    # ── 54-4 · 환경 보호를 위한 개인의 노력 (문제-원인-해결형) ──────────
    {
        "qtype":   "54",
        "title":   "54-4: 환경 보호를 위한 개인의 노력",
        "summary": "Insho, 'muammo-sabab-yechim' turi: 영향을 미치다, 실천 kabi iboralar bilan ijtimoiy mavzu.",
        "order":   4,
        "prompt":  PROMPT_54,
        "chart": '''<div class="wp-passage">
<p>오늘날 환경 오염과 지구 온난화는 인류 전체가 해결해야 할 심각한 문제가 되었다. 환경 문제를 해결하기 위해서는 정부뿐만 아니라 개인의 노력도 필요하다. 아래의 내용을 중심으로 '환경 보호를 위한 개인의 노력'에 대한 자신의 생각을 쓰라.</p>
<ul>
<li>환경 문제가 심각해진 원인은 무엇인가?</li>
<li>환경 문제는 우리 생활에 어떤 영향을 미치는가?</li>
<li>환경을 보호하기 위해 개인은 어떤 노력을 해야 하는가?</li>
</ul>
</div>''',
        "template_body": '''<p class="wp-part">서론</p>
<p>오늘날 <span class="wp-blank" data-answer="환경 오염" data-alt="환경오염|환경 문제"></span>은 어느 한 나라만의 문제가 아니라 <span class="cn-word" data-tr="insoniyat">인류</span> 전체가 해결해야 할 <span class="cn-word" data-tr="vazifa, masala">과제</span>가 되었다. 환경 문제가 이렇게 심각해진 <span class="wp-blank" data-answer="원인"></span>은 사람들이 편리한 생활만을 <span class="cn-word" data-pos="verb" data-tr="intilmoq, koʻzlamoq">추구해</span> 왔기 때문이다. 공장과 자동차가 늘어나고 <span class="cn-word" data-tr="bir martalik buyumlar">일회용품</span> 사용이 많아지면서 자연은 점점 <span class="cn-word" data-pos="verb" data-tr="vayron boʻlmoq">파괴되고</span> 있다.</p>
<p class="wp-part">본론 1</p>
<p>이러한 환경 문제는 이미 우리 생활에 큰 <span class="wp-blank" data-answer="영향" data-alt="영향을"></span>을 미치고 있다. 여름은 해마다 더 더워지고 <span class="cn-word" data-tr="mayda chang (havoda)">미세 먼지</span> 때문에 마음껏 숨 쉬기 어려운 날도 많아졌다. 오염된 환경은 결국 우리의 건강을 <span class="cn-word" data-pos="verb" data-tr="xavf solmoq">위협하고</span> 미래 <span class="cn-word" data-tr="avlod">세대</span>의 삶까지 위험하게 만든다. 또한 폭우나 가뭄 같은 이상 기후로 피해를 입는 지역도 해마다 늘어나고 있다.</p>
<p class="wp-part">본론 2</p>
<p>그렇다면 환경을 보호하기 위해 개인은 <span class="wp-blank" data-answer="어떤 노력을 해야 할까" data-alt="어떤 노력을 해야 하는가|어떻게 해야 할까"></span>? 먼저 일회용품 대신 여러 번 쓸 수 있는 물건을 사용하는 <span class="cn-word" data-tr="odat qilib olmoq">습관을 길러야</span> 한다. <span class="wp-blank" data-answer="다음으로" data-alt="또한|둘째"></span> 가까운 거리는 걷거나 대중교통을 이용하는 것이 좋다. 마지막으로 쓰레기를 줄이고 분리수거를 생활화하는 노력도 필요하다. <span class="cn-word" data-tr="shu tarzda (umumlashtirish)">이처럼</span> 작은 <span class="cn-word" data-tr="amaliy bajarish">실천</span>이 모이면 큰 변화를 만들 수 있다.</p>
<p class="wp-part">결론</p>
<p>지금까지 환경 문제의 원인과 그 영향, 개인이 할 수 있는 노력에 대해 <span class="wp-blank" data-answer="살펴보았다" data-alt="알아보았다"></span>. 환경은 한번 파괴되면 <span class="cn-word" data-pos="verb" data-tr="ortga qaytarmoq">되돌리기</span> 어렵다. 따라서 우리는 지금부터라도 생활 속의 작은 습관을 바꾸도록 <span class="wp-blank" data-answer="노력해야 할 것이다" data-alt="노력해야 한다"></span>.</p>''',
        "model_answer": '''<p class="wp-part">서론</p>
<p>오늘날 환경 오염은 어느 한 나라만의 문제가 아니라 <span class="cn-word" data-tr="insoniyat">인류</span> 전체가 해결해야 할 <span class="cn-word" data-tr="vazifa, masala">과제</span>가 되었다. 환경 문제가 이렇게 심각해진 원인은 사람들이 편리한 생활만을 <span class="cn-word" data-pos="verb" data-tr="intilmoq, koʻzlamoq">추구해</span> 왔기 때문이다. 공장과 자동차가 늘어나고 <span class="cn-word" data-tr="bir martalik buyumlar">일회용품</span> 사용이 많아지면서 자연은 점점 <span class="cn-word" data-pos="verb" data-tr="vayron boʻlmoq">파괴되고</span> 있다.</p>
<p class="wp-part">본론 1</p>
<p>이러한 환경 문제는 이미 우리 생활에 큰 <span class="cn-word" data-tr="taʼsir koʻrsatmoq (영향을 미치다)">영향을 미치고</span> 있다. 여름은 해마다 더 더워지고 <span class="cn-word" data-tr="mayda chang (havoda)">미세 먼지</span> 때문에 마음껏 숨 쉬기 어려운 날도 많아졌다. 오염된 환경은 결국 우리의 건강을 <span class="cn-word" data-pos="verb" data-tr="xavf solmoq">위협하고</span> 미래 <span class="cn-word" data-tr="avlod">세대</span>의 삶까지 위험하게 만든다. 또한 폭우나 가뭄 같은 이상 기후로 피해를 입는 지역도 해마다 늘어나고 있다.</p>
<p class="wp-part">본론 2</p>
<p>그렇다면 환경을 보호하기 위해 개인은 어떤 노력을 해야 할까? 먼저 일회용품 대신 여러 번 쓸 수 있는 물건을 사용하는 <span class="cn-word" data-tr="odat qilib olmoq">습관을 길러야</span> 한다. 다음으로 가까운 거리는 걷거나 대중교통을 이용하는 것이 좋다. 마지막으로 쓰레기를 줄이고 분리수거를 생활화하는 노력도 필요하다. <span class="cn-word" data-tr="shu tarzda (umumlashtirish)">이처럼</span> 작은 <span class="cn-word" data-tr="amaliy bajarish">실천</span>이 모이면 큰 변화를 만들 수 있다.</p>
<p class="wp-part">결론</p>
<p>지금까지 환경 문제의 원인과 그 영향, 개인이 할 수 있는 노력에 대해 살펴보았다. 환경은 한번 파괴되면 <span class="cn-word" data-pos="verb" data-tr="ortga qaytarmoq">되돌리기</span> 어렵다. 따라서 우리는 지금부터라도 생활 속의 작은 습관을 바꾸도록 노력해야 할 것이다.</p>
<p class="small text-secondary">(약 610자)</p>''',
        "tips": '''<ul>
<li>'Muammo-sabab-yechim' skeleti: 서론 = muammo + sababi, 본론 1 = taʼsiri, 본론 2 = yechimlar, 결론 = chaqiriq. Savol qutisi shu tartibni oʻzi beradi.</li>
<li>Ijtimoiy mavzu kollokatsiyalari: <em>영향을 미치다</em> (taʼsir koʻrsatmoq), <em>문제를 해결하다</em>, <em>습관을 기르다</em>, <em>-도록 노력하다</em> — bularni bloklab yodlang.</li>
<li>Yechimlarni sanashda: <em>먼저 ... 다음으로 ... 이처럼 ...</em> — uchlik har qanday 'usul' xatboshisini tashkillaydi.</li>
<li><em>A뿐만 아니라 B도</em> (savol qutisidagi 정부뿐만 아니라 개인도) — inshoda qayta ishlatsa boʻladigan qolip, lekin jumlani AYNAN koʻchirmang.</li>
<li>결론da kelajakka qaratilgan chaqiriq yaxshi taassurot qoldiradi: <em>지금부터라도 ~아/어야 할 것이다</em>.</li>
</ul>''',
    },

    # ── 54-5 · 행복한 삶의 조건 (조건형) ────────────────────────────────
    {
        "qtype":   "54",
        "title":   "54-5: 행복한 삶의 조건",
        "summary": "Insho, 'shartlar' turi: ~(이)란 ~을 말한다 taʼrif qolipi va mavhum mavzuda fikr yuritish.",
        "order":   5,
        "prompt":  PROMPT_54,
        "chart": '''<div class="wp-passage">
<p>사람은 누구나 행복하게 살기를 원한다. 그러나 무엇이 행복한 삶인지, 행복을 위해 무엇이 필요한지에 대한 생각은 사람마다 다르다. 아래의 내용을 중심으로 '행복한 삶의 조건'에 대한 자신의 생각을 쓰라.</p>
<ul>
<li>행복한 삶이란 무엇인가?</li>
<li>행복한 삶을 위해 무엇이 필요한가?</li>
<li>행복한 삶을 살기 위해 어떤 노력을 해야 하는가?</li>
</ul>
</div>''',
        "template_body": '''<p class="wp-part">서론</p>
<p>사람은 누구나 행복하게 살기를 원하지만 행복이 무엇인지 물으면 쉽게 대답하지 못한다. <span class="wp-blank" data-answer="행복한 삶" data-alt="행복"></span>이란 돈이나 성공 같은 조건이 아니라 자신의 생활에 <span class="cn-word" data-pos="verb" data-tr="qanoatlanmoq">만족하며</span> 사는 삶을 <span class="cn-word" data-tr="~(이)란 ~을 말한다: taʼrif qolipi">말한다</span>. 아무리 많은 것을 가져도 만족하지 못하면 행복하다고 말하기 어렵기 때문이다.</p>
<p class="wp-part">본론 1</p>
<p>그렇다면 행복한 삶을 위해서는 <span class="wp-blank" data-answer="무엇이 필요한가" data-alt="무엇이 필요할까"></span>? 우선 건강이 필요하다. 몸과 마음이 건강하지 않으면 아무리 좋은 것을 <span class="cn-word" data-pos="verb" data-tr="bahramand boʻlmoq">누려도</span> 기쁨을 느끼기 어렵다. 큰 성공을 거두어도 건강을 잃으면 아무 소용이 없는 것이다. 다음으로 가족이나 친구처럼 마음을 나눌 수 있는 사람이 있어야 한다. 기쁨은 나누면 커지고 슬픔은 나누면 작아지기 <span class="wp-blank" data-answer="때문이다"></span>.</p>
<p class="wp-part">본론 2</p>
<p>행복한 삶은 <span class="cn-word" data-pos="adv" data-tr="oʻz-oʻzidan">저절로</span> 오는 것이 아니라 스스로 만들어 가는 것이다. 다른 사람과 <span class="cn-word" data-pos="verb" data-tr="solishtirmoq">비교하는</span> 습관을 버리고 자신이 가진 것에 <span class="cn-word" data-pos="verb" data-tr="minnatdor boʻlmoq">감사하는</span> 태도를 가져야 한다. <span class="wp-blank" data-answer="또한" data-alt="그리고|다음으로"></span> 아무리 바쁘더라도 자신이 좋아하는 일을 할 시간을 만들고, 주변 사람들에게 마음을 표현하는 노력이 필요하다. 작은 기쁨을 자주 느끼는 사람이 더 행복하다는 연구 결과도 있다.</p>
<p class="wp-part">결론</p>
<p>지금까지 행복한 삶의 조건에 대해 <span class="wp-blank" data-answer="살펴보았다" data-alt="알아보았다"></span>. 행복은 멀리 있는 것이 아니라 <span class="cn-word" data-tr="kundalik hayot">일상</span>의 작은 만족 속에 있다. 따라서 우리는 오늘 하루의 삶에 감사하면서 자신만의 행복을 찾도록 <span class="wp-blank" data-answer="노력해야 할 것이다" data-alt="노력해야 한다"></span>.</p>''',
        "model_answer": '''<p class="wp-part">서론</p>
<p>사람은 누구나 행복하게 살기를 원하지만 행복이 무엇인지 물으면 쉽게 대답하지 못한다. 행복한 삶이란 돈이나 성공 같은 조건이 아니라 자신의 생활에 <span class="cn-word" data-pos="verb" data-tr="qanoatlanmoq">만족하며</span> 사는 삶을 <span class="cn-word" data-tr="~(이)란 ~을 말한다: taʼrif qolipi">말한다</span>. 아무리 많은 것을 가져도 만족하지 못하면 행복하다고 말하기 어렵기 때문이다.</p>
<p class="wp-part">본론 1</p>
<p>그렇다면 행복한 삶을 위해서는 무엇이 필요한가? 우선 건강이 필요하다. 몸과 마음이 건강하지 않으면 아무리 좋은 것을 <span class="cn-word" data-pos="verb" data-tr="bahramand boʻlmoq">누려도</span> 기쁨을 느끼기 어렵다. 큰 성공을 거두어도 건강을 잃으면 아무 소용이 없는 것이다. 다음으로 가족이나 친구처럼 마음을 나눌 수 있는 사람이 있어야 한다. 기쁨은 나누면 커지고 슬픔은 나누면 작아지기 때문이다.</p>
<p class="wp-part">본론 2</p>
<p>행복한 삶은 <span class="cn-word" data-pos="adv" data-tr="oʻz-oʻzidan">저절로</span> 오는 것이 아니라 스스로 만들어 가는 것이다. 다른 사람과 <span class="cn-word" data-pos="verb" data-tr="solishtirmoq">비교하는</span> 습관을 버리고 자신이 가진 것에 <span class="cn-word" data-pos="verb" data-tr="minnatdor boʻlmoq">감사하는</span> 태도를 가져야 한다. 또한 아무리 바쁘더라도 자신이 좋아하는 일을 할 시간을 만들고, 주변 사람들에게 마음을 표현하는 노력이 필요하다. 작은 기쁨을 자주 느끼는 사람이 더 행복하다는 연구 결과도 있다.</p>
<p class="wp-part">결론</p>
<p>지금까지 행복한 삶의 조건에 대해 살펴보았다. 행복은 멀리 있는 것이 아니라 <span class="cn-word" data-tr="kundalik hayot">일상</span>의 작은 만족 속에 있다. 따라서 우리는 오늘 하루의 삶에 감사하면서 자신만의 행복을 찾도록 노력해야 할 것이다.</p>
<p class="small text-secondary">(약 620자)</p>''',
        "tips": '''<ul>
<li>Mavhum mavzuda birinchi qadam — TAʼRIF: <em>~(이)란 ~을 말한다</em> (…deganda …tushuniladi). Bu jumla 서론ni ochadi va inshoga yoʻnalish beradi.</li>
<li><em>A가 아니라 B</em> qolipi bilan taʼrifni oʻtkirlashtiring: 행복이란 돈이 아니라 만족이다.</li>
<li>본론 1da shartlarni sanang (우선 … 다음으로 …), 본론 2da esa amaliy harakatlarga oʻting — savol qutisidagi 2- va 3-savollar shunday boʻlinadi.</li>
<li><em>아무리 -아/어도</em> (har qancha …boʻlsa ham) — mavhum mavzularning eng foydali qolipi; bu inshoda ikki marta ishlatildi.</li>
<li>Hikmatli yakun: <em>행복은 멀리 있는 것이 아니라 ~에 있다</em> kabi umumlashma 결론ga kuch beradi — lekin yangi dalil kiritmang.</li>
</ul>''',
    },
]
