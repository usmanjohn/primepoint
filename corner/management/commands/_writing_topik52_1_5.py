# TOPIK II 쓰기 52 — drills 1–5 (see toc_topik_writing_52.txt).
# Import: python manage.py import_writing corner/management/commands/_writing_topik52_1_5.py --author=<AUTHOR>

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili resurslari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

PROMPT_52 = '''<p>다음 글의 ㉠과 ㉡에 들어갈 말을 각각 한 문장으로 쓰시오. <strong>(10점)</strong></p>'''

PRACTICES = [

    # ── 52-1 · 물 마시기의 효과 ─────────────────────────────────────────
    {
        "qtype":   "52",
        "title":   "52-1: 물 마시기의 효과",
        "summary": "설명문: -는 것이 좋다 (maslahat) va 오히려 -(으)ㄹ 수 있다 (teskari natija) qoliplari.",
        "order":   1,
        "prompt":  PROMPT_52,
        "chart": '''<div class="wp-passage">
<p>우리 몸의 70%는 물로 되어 있다. 그래서 사람들은 보통 목이 마를 때 물을 마신다. 그런데 전문가들은 목이 마르지 않아도 물을 자주 ( <span class="wp-slot">㉠</span> ) 말한다. 물을 충분히 마시면 피로가 풀리고 건강에 도움이 되기 때문이다. 하지만 아무리 물이 몸에 좋아도 한꺼번에 너무 많이 마시면 오히려 건강에 ( <span class="wp-slot">㉡</span> ).</p>
</div>''',
        "template_body": '''<p><span class="wp-frame-label">㉠</span> 그런데 <span class="cn-word" data-tr="mutaxassis">전문가</span>들은 목이 마르지 않아도 물을 자주 <span class="wp-blank" data-answer="마시는 것이 좋다고" data-alt="마시라고|마셔야 한다고"></span> 말한다.</p>
<p><span class="wp-frame-label">㉡</span> 하지만 <span class="cn-word" data-tr="har qancha ...boʻlsa ham">아무리</span> 물이 몸에 좋아도 <span class="cn-word" data-pos="adv" data-tr="birdaniga">한꺼번에</span> 너무 많이 마시면 <span class="cn-word" data-pos="adv" data-tr="aksincha, teskarisiga">오히려</span> 건강에 <span class="wp-blank" data-answer="해로울 수 있다" data-alt="나쁠 수 있다|안 좋을 수 있다|해가 될 수 있다"></span>.</p>''',
        "model_answer": '''<p><span class="wp-frame-label">㉠</span> 물을 자주 <span class="cn-word" data-tr="ichgan maʼqul degan (maslahat + bilvosita gap)">마시는 것이 좋다고</span> 말한다</p>
<p class="wp-alt">(또는: 마시라고 / 마셔야 한다고 말한다)</p>
<p><span class="wp-frame-label">㉡</span> 오히려 건강에 <span class="cn-word" data-pos="adj" data-tr="zararli boʻlishi mumkin">해로울 수 있다</span></p>
<p class="wp-alt">(또는: 나쁠 수 있다 / 해가 될 수 있다)</p>
<p>💡 ㉠: gap <strong>말한다</strong> bilan tugaydi — demak bilvosita gap: <span class="cn-word" data-tr="...deb (bilvosita gap)">-다고</span> kerak; mutaxassis maslahati esa <span class="cn-word" data-tr="...gan maʼqul qolipi">-는 것이 좋다</span>. Keyingi jumla <span class="cn-word" data-tr="...gani uchun (sabab)">-기 때문이다</span> bilan sababini beradi. ㉡: <strong>하지만</strong> + <strong>오히려</strong> → oldingi ijobiy gapning teskarisi, ehtimollik bilan: <span class="cn-word" data-tr="...boʻlishi mumkin">-(으)ㄹ 수 있다</span>.</p>''',
        "tips": '''<ul>
<li>52-savol YOZMA uslubda: <em>-(느)ㄴ다 / -다</em>. <em>-습니다</em> yoki <em>-아요</em> yozsangiz ball kesiladi — bu 51 bilan asosiy farqi.</li>
<li>Gap <em>말한다 / 한다</em> bilan tugasa, boʻsh joyda <strong>-다고/-라고</strong> (bilvosita gap) boʻlishi shart.</li>
<li><strong>오히려</strong> koʻrsangiz — kutilganning TESKARISI keladi: yaxshi narsa → zarar.</li>
<li>Keyingi jumla <em>-기 때문이다</em> boʻlsa, u boʻsh joydagi fikrning sababi — javobni tekshirishga ishlating.</li>
</ul>''',
    },

    # ── 52-2 · 메모하는 습관 ────────────────────────────────────────────
    {
        "qtype":   "52",
        "title":   "52-2: 메모하는 습관",
        "summary": "설명문: -는 것이 좋다 va -도록 (maqsad) qoliplari, 경우가 많다 iborasi.",
        "order":   2,
        "prompt":  PROMPT_52,
        "chart": '''<div class="wp-passage">
<p>사람들은 중요한 일을 잊어버리지 않으려고 메모를 한다. 그런데 메모를 해 놓고 그 메모를 어디에 두었는지 몰라서 못 찾는 경우가 많다. 그래서 메모는 여기저기에 하지 말고 수첩 한 곳에 모아서 ( <span class="wp-slot">㉠</span> ). 또한 메모를 할 때는 나중에 다시 봐도 이해할 수 있도록 날짜와 내용을 함께 ( <span class="wp-slot">㉡</span> ).</p>
</div>''',
        "template_body": '''<p><span class="wp-frame-label">㉠</span> 그래서 메모는 여기저기에 하지 말고 <span class="cn-word" data-tr="yon daftarcha">수첩</span> 한 곳에 <span class="cn-word" data-pos="verb" data-tr="toʻplamoq, jamlamoq">모아서</span> <span class="wp-blank" data-answer="하는 것이 좋다" data-alt="정리하는 것이 좋다|보관하는 것이 좋다|해야 한다"></span>.</p>
<p><span class="wp-frame-label">㉡</span> 나중에 다시 봐도 이해할 수 있도록 날짜와 내용을 함께 <span class="wp-blank" data-answer="적는 것이 좋다" data-alt="쓰는 것이 좋다|적어야 한다|써야 한다"></span>.</p>''',
        "model_answer": '''<p><span class="wp-frame-label">㉠</span> 한 곳에 모아서 <span class="cn-word" data-tr="qilgan maʼqul">하는 것이 좋다</span></p>
<p class="wp-alt">(또는: 정리하는 것이 좋다 / 보관하는 것이 좋다)</p>
<p><span class="wp-frame-label">㉡</span> 날짜와 내용을 함께 <span class="cn-word" data-pos="verb" data-tr="yozib qoʻymoq">적는</span> 것이 좋다</p>
<p class="wp-alt">(또는: 쓰는 것이 좋다 / 적어야 한다)</p>
<p>💡 ㉠: oldin muammo aytildi (<span class="cn-word" data-tr="holat koʻp uchraydi">경우가 많다</span>) + <strong>그래서</strong> → yechim-maslahat: <strong>-는 것이 좋다</strong>. <span class="cn-word" data-tr="qilmasdan (taqiq + alternativa)">-지 말고</span> dan keyin doim ijobiy maslahat keladi. ㉡: <span class="cn-word" data-tr="...adigan qilib (maqsad)">-도록</span> maqsadni beradi — unga erishish usuli boʻsh joyda. <span class="cn-word" data-pos="verb" data-tr="unutmoq">잊어버리다</span> ham 52da tez-tez chiqadigan feʼl.</p>''',
        "tips": '''<ul>
<li><em>-지 말고</em> (unday qilmasdan) koʻrsangiz — boʻsh joyda uning muqobili + <em>-는 것이 좋다</em> keladi.</li>
<li><em>-도록</em> maqsad jumlasi: "keyin qarasa ham tushunadigan qilib" → nima qilish kerakligi javobda.</li>
<li>Ikkala boʻsh joy ham maslahat bilan tugasa, bir xil qolipni takrorlashdan qoʻrqmang — TOPIK javoblarida bu tabiiy.</li>
<li>또한 (shuningdek) — ikkinchi maslahatni kirituvchi bogʻlovchi; ㉡ mustaqil yangi fikr emas, ㉠ ga parallel.</li>
</ul>''',
    },

    # ── 52-3 · 칭찬의 두 얼굴 ───────────────────────────────────────────
    {
        "qtype":   "52",
        "title":   "52-3: 칭찬의 두 얼굴",
        "summary": "설명문: -게 된다 (natija) va 결과보다 과정 (taqqoslash) — mavhum mavzuli klassik 52.",
        "order":   3,
        "prompt":  PROMPT_52,
        "chart": '''<div class="wp-passage">
<p>칭찬은 사람의 기분을 좋게 하고 자신감을 키워 준다. 그래서 칭찬을 들으면 그 일을 더 열심히 ( <span class="wp-slot">㉠</span> ). 하지만 칭찬이 언제나 좋은 결과를 가져오는 것은 아니다. 결과만 칭찬을 하면 사람들은 좋은 결과를 얻으려고 과정을 소홀히 하기 쉽다. 따라서 결과보다는 열심히 노력한 ( <span class="wp-slot">㉡</span> ) 것이 더 중요하다.</p>
</div>''',
        "template_body": '''<p><span class="wp-frame-label">㉠</span> <span class="cn-word" data-tr="maqtov">칭찬</span>은 <span class="cn-word" data-tr="oʻziga ishonch">자신감</span>을 키워 준다. 그래서 칭찬을 들으면 그 일을 더 열심히 <span class="wp-blank" data-answer="하게 된다" data-alt="하려고 한다|하게 만든다"></span>.</p>
<p><span class="wp-frame-label">㉡</span> <span class="cn-word" data-pos="adv" data-tr="shu sababli, demak">따라서</span> <span class="cn-word" data-tr="natija">결과</span>보다는 열심히 노력한 <span class="wp-blank" data-answer="과정을 칭찬하는" data-alt="과정을 칭찬해 주는"></span> 것이 더 중요하다.</p>''',
        "model_answer": '''<p><span class="wp-frame-label">㉠</span> 그 일을 더 열심히 <span class="cn-word" data-tr="qiladigan boʻlib qoladi (tabiiy natija)">하게 된다</span></p>
<p class="wp-alt">(또는: 하려고 한다 / 하게 만든다)</p>
<p><span class="wp-frame-label">㉡</span> 노력한 <span class="cn-word" data-tr="jarayon">과정</span>을 칭찬하는 것이 더 중요하다</p>
<p class="wp-alt">(또는: 과정을 칭찬해 주는 것이 더 중요하다)</p>
<p>💡 ㉠: sabab (자신감을 키워 준다) + 그래서 → tabiiy natija: <span class="cn-word" data-tr="...boʻlib qoladi qolipi">-게 되다</span>. ㉡: matn qarama-qarshilik ustiga qurilgan — <strong>결과만</strong> maqtash yomon (odamlar jarayonni <span class="cn-word" data-tr="eʼtiborsiz qoldirmoq">소홀히 하기</span> boshlaydi), demak <strong>결과보다는 과정</strong>. <span class="cn-word" data-tr="...gani uchun oson/tez boʻladi">-기 쉽다</span> ham eslab qolinadigan qolip.</p>''',
        "tips": '''<ul>
<li>52da koʻpincha ㉡ ning javobi MATN ICHIDA turadi: bu yerda 과정 soʻzi oldingi jumlada bor — uni qayta ishlating.</li>
<li><em>A보다는 B가 중요하다</em> — taqqoslash skeleti; ㉡ oldida 보다는 koʻrinsa, javob qarama-qarshi juftlikning ikkinchi aʼzosi.</li>
<li><em>-는 것은 아니다</em> (har doim ham unday emas) — matnning burilish nuqtasi; undan keyingi gaplar salbiy tomonni ochadi.</li>
<li>Yozma uslubni saqlang: 하게 된다 (✓), 하게 돼요 (✗).</li>
</ul>''',
    },

    # ── 52-4 · 웃음과 건강 ──────────────────────────────────────────────
    {
        "qtype":   "52",
        "title":   "52-4: 웃음과 건강",
        "summary": "설명문: 연구에 따르면 -다고 한다 (tadqiqot natijasi) va 높아진다 qoliplari.",
        "order":   4,
        "prompt":  PROMPT_52,
        "chart": '''<div class="wp-passage">
<p>웃음은 건강에 좋은 영향을 준다. 웃으면 스트레스가 풀리고 몸의 면역력도 ( <span class="wp-slot">㉠</span> ). 그런데 이러한 효과는 진짜 웃음일 때만 나타나는 것이 아니다. 연구에 따르면 일부러 웃는 가짜 웃음도 진짜 웃음과 비슷한 ( <span class="wp-slot">㉡</span> ). 그러므로 기분이 좋지 않을 때일수록 한번 크게 웃어 보는 것이 어떨까?</p>
</div>''',
        "template_body": '''<p><span class="wp-frame-label">㉠</span> 웃으면 스트레스가 풀리고 몸의 <span class="cn-word" data-tr="immunitet">면역력</span>도 <span class="wp-blank" data-answer="높아진다" data-alt="좋아진다|강해진다|올라간다"></span>.</p>
<p><span class="wp-frame-label">㉡</span> <span class="cn-word" data-tr="tadqiqotga koʻra">연구에 따르면</span> <span class="cn-word" data-pos="adv" data-tr="ataylab, qasddan">일부러</span> 웃는 가짜 웃음도 진짜 웃음과 비슷한 <span class="wp-blank" data-answer="효과가 있다고 한다" data-alt="효과를 낸다고 한다|효과가 나타난다고 한다"></span>.</p>''',
        "model_answer": '''<p><span class="wp-frame-label">㉠</span> 면역력도 <span class="cn-word" data-pos="verb" data-tr="yuqorilashadi, koʻtariladi">높아진다</span></p>
<p class="wp-alt">(또는: 좋아진다 / 강해진다)</p>
<p><span class="wp-frame-label">㉡</span> 진짜 웃음과 비슷한 <span class="cn-word" data-tr="samarasi bor deydi (manba + bilvosita gap)">효과가 있다고 한다</span></p>
<p class="wp-alt">(또는: 효과를 낸다고 한다 / 효과가 나타난다고 한다)</p>
<p>💡 ㉠: <strong>-도</strong> yukламаsi oldingi ijobiy natijaga (<span class="cn-word" data-tr="charchoq/stress yozilmoq">스트레스가 풀리다</span>) parallel javobni talab qiladi: 면역력은 <strong>높아지다</strong> bilan birikadi. ㉡: <span class="cn-word" data-tr="taʼsir koʻrsatmoq">영향을 주다</span> / <span class="cn-word" data-tr="samara, effekt">효과</span> — matnning kalit soʻzlari; <strong>연구에 따르면</strong> boshlagan gap albatta <strong>-다고 한다</strong> bilan tugaydi (birovning xulosasini yetkazish).</p>''',
        "tips": '''<ul>
<li><strong>연구에 따르면 / 조사에 따르면</strong> koʻrdingizmi — gap oxiri <em>-다고 한다</em> boʻladi. Bu 52ning eng sevimli juftligi.</li>
<li>면역력이 높아지다, 스트레스가 풀리다, 영향을 주다 — sogʻliq mavzusining tayyor kollokatsiyalari; birga yodlang.</li>
<li><em>-도</em> yuklamasi javobni oldingi feʼlga OHANGDOSH qiladi: 풀리고 ... 도 높아진다.</li>
<li><em>-(으)ㄹ수록</em> (…gan sari) va <em>-어 보는 것이 어떨까?</em> — matn yakunidagi taklif shakllariga ham eʼtibor bering.</li>
</ul>''',
    },

    # ── 52-5 · 새해 계획과 실천 ─────────────────────────────────────────
    {
        "qtype":   "52",
        "title":   "52-5: 새해 계획과 실천",
        "summary": "설명문: 많지 않다 (inkor) va -부터 -는 것이 좋다 (maslahat) qoliplari.",
        "order":   5,
        "prompt":  PROMPT_52,
        "chart": '''<div class="wp-passage">
<p>새해가 되면 많은 사람들이 운동이나 외국어 공부 같은 새로운 계획을 세운다. 하지만 그 계획을 연말까지 실천하는 사람은 그리 ( <span class="wp-slot">㉠</span> ). 처음부터 계획을 너무 크게 세우기 때문이다. 계획을 끝까지 지키고 싶다면 큰 목표가 아니라 매일 실천할 수 있는 작은 목표부터 ( <span class="wp-slot">㉡</span> ).</p>
</div>''',
        "template_body": '''<p><span class="wp-frame-label">㉠</span> 하지만 그 계획을 연말까지 <span class="cn-word" data-pos="verb" data-tr="amalga oshirmoq, bajarish">실천하는</span> 사람은 그리 <span class="wp-blank" data-answer="많지 않다" data-alt="많지 않은 것 같다|없다"></span>.</p>
<p><span class="wp-frame-label">㉡</span> 계획을 끝까지 <span class="cn-word" data-pos="verb" data-tr="rioya qilmoq, ushlab turmoq">지키고</span> 싶다면 큰 <span class="cn-word" data-tr="maqsad">목표</span>가 아니라 매일 실천할 수 있는 작은 목표부터 <span class="wp-blank" data-answer="세우는 것이 좋다" data-alt="시작하는 것이 좋다|세워야 한다|정하는 것이 좋다"></span>.</p>''',
        "model_answer": '''<p><span class="wp-frame-label">㉠</span> 실천하는 사람은 그리 <span class="cn-word" data-tr="koʻp emas">많지 않다</span></p>
<p class="wp-alt">(또는: 많지 않은 것 같다 / 별로 없다)</p>
<p><span class="wp-frame-label">㉡</span> 작은 목표부터 <span class="cn-word" data-tr="reja tuzmoq (계획/목표을 세우다)">세우는</span> 것이 좋다</p>
<p class="wp-alt">(또는: 시작하는 것이 좋다 / 정하는 것이 좋다)</p>
<p>💡 ㉠: <strong>하지만</strong> oldingi gapni (koʻpchilik reja tuzadi) teskarisiga buradi + <span class="cn-word" data-pos="adv" data-tr="uncha (inkor bilan)">그리</span> — faqat inkor bilan ishlatiladi: <strong>그리 많지 않다</strong>. Keyingi jumla <strong>-기 때문이다</strong> bilan buning sababini beradi. ㉡: <span class="cn-word" data-tr="A emas, B (tuzatish)">-이/가 아니라</span> + <strong>-부터</strong> (…dan boshlab) → maslahat qolipi <strong>-는 것이 좋다</strong>. <span class="cn-word" data-tr="reja tuzmoq">계획을 세우다</span> — oʻzgarmas birikma.</p>''',
        "tips": '''<ul>
<li><strong>그리 / 별로 / 전혀</strong> — bu ravishlar FAQAT inkor bilan yuradi: boʻsh joy albatta <em>-지 않다 / 없다</em> bilan tugaydi.</li>
<li><em>A가 아니라 B부터 ~</em> — tuzatish qolipi: javob B haqidagi maslahat boʻladi.</li>
<li>계획을 세우다, 계획을 지키다, 계획을 실천하다 — 계획 feʼllari toʻplami; 52 va 54da ishlatiladi.</li>
<li>Sabab jumlasi (<em>-기 때문이다</em>) boʻsh joydan KEYIN kelsa, javobingiz oʻsha sababning natijasi boʻlishi kerak.</li>
</ul>''',
    },
]
