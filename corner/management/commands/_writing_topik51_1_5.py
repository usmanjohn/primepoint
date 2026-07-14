# TOPIK II 쓰기 51 — drills 1–5 (see toc_topik_writing_51.txt).
# Import: python manage.py import_writing corner/management/commands/_writing_topik51_1_5.py --author=<AUTHOR>

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili resurslari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

PROMPT_51 = '''<p>다음 글의 ㉠과 ㉡에 들어갈 말을 각각 한 문장으로 쓰시오. <strong>(10점)</strong></p>'''

PRACTICES = [

    # ── 51-1 · 초대장 — 집들이 ───────────────────────────────────────────
    {
        "qtype":   "51",
        "title":   "51-1: 초대장 — 집들이에 초대합니다",
        "summary": "Taklifnoma (email koʻrinishida): -(으)려고 합니다 va -기가 어렵다 qoliplari.",
        "order":   1,
        "prompt":  PROMPT_51,
        "chart": '''<div class="wp-mail">
  <div class="wp-mail-row"><span>제목</span><span>집들이에 초대합니다</span></div>
  <div class="wp-mail-row"><span>보낸 사람</span><span>왕밍</span></div>
</div>
<div class="wp-passage">
<p>안녕하세요? 왕밍입니다.</p>
<p>지난주에 새 집으로 이사를 했습니다. 그래서 이번 주 토요일 저녁에 우리 집에서 ( <span class="wp-slot">㉠</span> ). 시간이 있으면 꼭 와 주시기 바랍니다. 그런데 우리 집이 골목 안에 있어서 처음 오시는 분은 좀 ( <span class="wp-slot">㉡</span> ). 그래서 약도를 함께 보냅니다. 약도를 보고 오시면 됩니다.</p>
<p>그럼 토요일에 만납시다.</p>
</div>''',
        "template_body": '''<p><span class="wp-frame-label">㉠</span> 그래서 이번 주 토요일 저녁에 우리 집에서 <span class="cn-word" data-tr="uy koʻrar ziyofati (yangi uyga koʻchgach)">집들이</span>를 <span class="wp-blank" data-answer="하려고 합니다" data-alt="할 예정입니다|할까 합니다|하기로 했습니다"></span>.</p>
<p><span class="wp-frame-label">㉡</span> 그런데 우리 집이 <span class="cn-word" data-tr="tor koʻcha, muyulish">골목</span> 안에 있어서 처음 오시는 분은 좀 <span class="wp-blank" data-answer="찾기가 어려울 것 같습니다" data-alt="찾기 어려울 것 같습니다|찾기가 어렵습니다|찾기 힘들 것 같습니다"></span>.</p>''',
        "model_answer": '''<p><span class="wp-frame-label">㉠</span> 집들이를 <span class="cn-word" data-pos="verb" data-tr="qilmoqchiman (reja, niyat)">하려고 합니다</span></p>
<p class="wp-alt">(또는: 집들이를 할 예정입니다 / 집들이를 할까 합니다)</p>
<p><span class="wp-frame-label">㉡</span> 집을 <span class="cn-word" data-tr="topish qiyin boʻlsa kerak">찾기가 어려울 것 같습니다</span></p>
<p class="wp-alt">(또는: 찾기 힘들 것 같습니다 / 찾기가 어렵습니다)</p>
<p>💡 ㉠: oldin <strong>이사를 했습니다</strong> + <span class="cn-word" data-tr="shuning uchun">그래서</span> keladi — demak reja: <span class="cn-word" data-tr="...moqchi boʻlmoq qolipi">-(으)려고 하다</span>. ㉡: keyingi jumla <strong>약도를 보냅니다</strong> — sabab: uyni topish qiyin. Xat <span class="cn-word" data-tr="rasmiy-muloyim uslub">-습니다체</span>da yozilgan, javob ham shu uslubda boʻlishi shart.</p>''',
        "tips": '''<ul>
<li>51-savolda javob HAR DOIM matn uslubiga mos boʻladi: bu xat <em>-습니다</em> uslubida — <em>-아요/어요</em> yozsangiz ball kesiladi.</li>
<li>Boʻsh joydan OLDINGI va KEYINGI jumlani oʻqing: 그래서 → natija/reja, 그런데 → qarama-qarshilik, 그래서 + 약도 → sabab.</li>
<li>Taklifnomalarning oltin qoliplari: <em>-(으)려고 합니다</em>, <em>꼭 와 주시기 바랍니다</em>, <em>-(으)시면 됩니다</em>.</li>
<li>Javob bitta toʻliq jumla boʻlishi kerak, lekin uzun emas — 51-savol qisqa va aniq javobni yaxshi koʻradi.</li>
</ul>''',
    },

    # ── 51-2 · 문자 메시지 — 약속 변경 ──────────────────────────────────
    {
        "qtype":   "51",
        "title":   "51-2: 문자 메시지 — 약속 시간 변경",
        "summary": "Messenjer yozishmasi: -(으)ㄹ 수 있을까요? bilan iltimos qilish va taklif qilish.",
        "order":   2,
        "prompt":  PROMPT_51,
        "chart": '''<div class="wp-chat">
  <p class="wp-chat-name">지영</p>
  <div class="wp-bubble"><p>민수 씨, 내일 2시에 만나기로 했지요? 그런데 갑자기 회사에 급한 일이 생겨서 약속 시간을 좀 ( <span class="wp-slot">㉠</span> )? 혹시 4시도 괜찮아요?</p></div>
  <p class="wp-chat-name wp-me">민수</p>
  <div class="wp-bubble wp-me"><p>네, 괜찮아요. 그럼 내일 4시에 지난번에 만났던 카페에서 ( <span class="wp-slot">㉡</span> ).</p></div>
</div>''',
        "template_body": '''<p><span class="wp-frame-label">㉠</span> <span class="cn-word" data-pos="adv" data-tr="toʻsatdan">갑자기</span> 회사에 급한 <span class="cn-word" data-tr="ish chiqib qolmoq">일이 생겨서</span> 약속 시간을 좀 <span class="wp-blank" data-answer="바꿀 수 있을까요" data-alt="바꿔도 될까요|바꿀 수 있어요|바꿔도 돼요"></span>?</p>
<p><span class="wp-frame-label">㉡</span> 그럼 내일 4시에 지난번에 만났던 카페에서 <span class="wp-blank" data-answer="만나요" data-alt="봐요|만납시다|만나는 게 어때요"></span>.</p>''',
        "model_answer": '''<p><span class="wp-frame-label">㉠</span> 약속 시간을 좀 <span class="cn-word" data-tr="oʻzgartirsak boʻladimi? (muloyim iltimos)">바꿀 수 있을까요</span>?</p>
<p class="wp-alt">(또는: 바꿔도 될까요? / 바꿀 수 있어요?)</p>
<p><span class="wp-frame-label">㉡</span> 카페에서 <span class="cn-word" data-pos="verb" data-tr="uchrashamiz">만나요</span></p>
<p class="wp-alt">(또는: 봐요 / 만나는 게 어때요?)</p>
<p>💡 ㉠: <span class="cn-word" data-tr="kelishib olgan edik qolipi">-기로 했지요</span> + 일이 생겨서 → vaqtni <strong>oʻzgartirish</strong>ni soʻrayapti; savol belgisi (?) turibdi — demak <span class="cn-word" data-tr="mumkinmi? qolipi">-(으)ㄹ 수 있을까요?</span> kerak. ㉡: <span class="cn-word" data-tr="unday boʻlsa">그럼</span> + joy va vaqt → uchrashuvni tasdiqlash. Yozishma <span class="cn-word" data-tr="oddiy-muloyim uslub">-아요/어요체</span>da — javob ham shunday.</p>''',
        "tips": '''<ul>
<li>Xabar oxirida <strong>?</strong> boʻlsa — javob soʻroq shaklida: <em>-(으)ㄹ 수 있을까요?</em>, <em>-아/어도 될까요?</em></li>
<li>Doʻstona yozishma = <em>-아요/어요</em> uslubi. Bu yerda <em>-습니다</em> gʻalati eshitiladi (lekin xato emas), <em>반말</em> esa xato.</li>
<li>혹시 (mabodo) — iltimosni yumshatadigan soʻz; oʻzingiz yozganda ham ishlating.</li>
<li>㉡ turidagi javobda oldingi gapdagi maʼlumotni (vaqt, joy) takrorlab tasdiqlang.</li>
</ul>''',
    },

    # ── 51-3 · 인터넷 게시판 — 중고 판매 ────────────────────────────────
    {
        "qtype":   "51",
        "title":   "51-3: 게시판 — 책상을 팝니다",
        "summary": "Internet eʼlon taxtasi: -(으)려고 합니다 va 연락해 주시기 바랍니다 qoliplari.",
        "order":   3,
        "prompt":  PROMPT_51,
        "chart": '''<div class="wp-mail">
  <div class="wp-mail-row"><span>게시판</span><span>사고팔고</span></div>
  <div class="wp-mail-row"><span>제목</span><span>책상을 팝니다</span></div>
</div>
<div class="wp-passage">
<p>제가 다음 달에 고향으로 돌아가게 되어서 지금 쓰는 책상을 ( <span class="wp-slot">㉠</span> ). 산 지 6개월밖에 안 돼서 새것처럼 깨끗합니다. 가격은 3만 원입니다. 책상 사진은 아래에 있습니다. 책상을 사고 싶으신 분은 저에게 문자로 ( <span class="wp-slot">㉡</span> ). 제 전화번호는 010-1234-5678입니다.</p>
</div>''',
        "template_body": '''<p><span class="wp-frame-label">㉠</span> 제가 다음 달에 <span class="cn-word" data-tr="ona shahar, vatan">고향</span>으로 <span class="cn-word" data-tr="qaytadigan boʻlib qoldim (vaziyat)">돌아가게 되어서</span> 지금 쓰는 책상을 <span class="wp-blank" data-answer="팔려고 합니다" data-alt="팔려고 해요|팔고 싶습니다|팔 생각입니다"></span>.</p>
<p><span class="wp-frame-label">㉡</span> 책상을 사고 싶으신 분은 저에게 문자로 <span class="wp-blank" data-answer="연락해 주시기 바랍니다" data-alt="연락해 주세요|연락 주시기 바랍니다|연락해 주십시오"></span>.</p>''',
        "model_answer": '''<p><span class="wp-frame-label">㉠</span> 책상을 <span class="cn-word" data-pos="verb" data-tr="sotmoqchiman">팔려고 합니다</span></p>
<p class="wp-alt">(또는: 팔고 싶습니다 / 팔 생각입니다)</p>
<p><span class="wp-frame-label">㉡</span> 문자로 <span class="cn-word" data-tr="bogʻlanishingizni soʻrayman (rasmiy iltimos)">연락해 주시기 바랍니다</span></p>
<p class="wp-alt">(또는: 연락해 주세요 / 연락해 주십시오)</p>
<p>💡 ㉠: eʼlonning sarlavhasi <strong>책상을 팝니다</strong> — birinchi boʻsh joy shu maqsadni ochadi: <span class="cn-word" data-tr="...moqchi (reja)">-(으)려고 합니다</span>. ㉡: keyingi jumlada <strong>전화번호</strong> berilgan → aloqa: <span class="cn-word" data-pos="verb" data-tr="bogʻlanmoq">연락하다</span> + <span class="cn-word" data-tr="qilib berishingizni soʻrayman">-아/어 주시기 바랍니다</span>. <span class="cn-word" data-tr="atigi ... boʻldi">-밖에 안 되다</span> (산 지 6개월밖에 안 돼서) — 51da tez-tez uchraydigan ibora.</p>''',
        "tips": '''<ul>
<li>Eʼlonlarda sarlavha — eng katta maslahat: <em>팝니다</em> → ㉠ da 팔다 boʻladi.</li>
<li>Notanish oʻquvchilarga yozilgan eʼlon = <em>-습니다</em> uslubi + <em>-아/어 주시기 바랍니다</em> iltimosi.</li>
<li><em>-게 되다</em> (vaziyat taqozosi bilan) — sabab bildirishda juda tabiiy: 돌아가게 되어서.</li>
<li>㉡ oldidan <em>-(으)신 분은</em> (…moqchi boʻlgan kishi) kelsa, javob deyarli doim iltimos qolipida tugaydi.</li>
</ul>''',
    },

    # ── 51-4 · 이메일 — 교수님께 ────────────────────────────────────────
    {
        "qtype":   "51",
        "title":   "51-4: 이메일 — 교수님께 과제 기한 문의",
        "summary": "Rasmiy email (professorga): -기가 어려울 것 같습니다 va -아/어 주시겠습니까? qoliplari.",
        "order":   4,
        "prompt":  PROMPT_51,
        "chart": '''<div class="wp-mail">
  <div class="wp-mail-row"><span>받는 사람</span><span>김민수 교수님</span></div>
  <div class="wp-mail-row"><span>제목</span><span>과제 제출 기한 문의</span></div>
</div>
<div class="wp-passage">
<p>교수님, 안녕하세요? 경영학과 3학년 흐엉입니다.</p>
<p>다름이 아니라 지난주부터 감기에 심하게 걸려서 병원에 입원을 하게 되었습니다. 그래서 이번 주 금요일까지 과제를 ( <span class="wp-slot">㉠</span> ). 죄송하지만 다음 주 월요일까지 시간을 좀 ( <span class="wp-slot">㉡</span> )? 그럼 답장 기다리겠습니다. 감사합니다.</p>
</div>''',
        "template_body": '''<p><span class="wp-frame-label">㉠</span> 병원에 입원을 하게 되었습니다. 그래서 이번 주 금요일까지 과제를 <span class="wp-blank" data-answer="제출하기가 어려울 것 같습니다" data-alt="제출하기 어려울 것 같습니다|내기가 어려울 것 같습니다|제출할 수 없을 것 같습니다|내지 못할 것 같습니다"></span>.</p>
<p><span class="wp-frame-label">㉡</span> <span class="cn-word" data-tr="uzr, lekin... (muloyim kirish)">죄송하지만</span> 다음 주 월요일까지 시간을 좀 <span class="wp-blank" data-answer="주시겠습니까" data-alt="주실 수 있으십니까|주실 수 있습니까|연장해 주시겠습니까"></span>?</p>''',
        "model_answer": '''<p><span class="wp-frame-label">㉠</span> 과제를 <span class="cn-word" data-pos="verb" data-tr="topshirmoq">제출하기</span>가 <span class="cn-word" data-tr="qiyin boʻlsa kerak (yumshoq rad)">어려울 것 같습니다</span></p>
<p class="wp-alt">(또는: 제출할 수 없을 것 같습니다 / 내지 못할 것 같습니다)</p>
<p><span class="wp-frame-label">㉡</span> 시간을 좀 <span class="cn-word" data-tr="berasizmi? (juda hurmatli soʻrov)">주시겠습니까</span>?</p>
<p class="wp-alt">(또는: 주실 수 있으십니까? / 연장해 주시겠습니까?)</p>
<p>💡 ㉠: sabab (입원) + 그래서 → natija: topshira olmaslik. Professorga toʻgʻridan-toʻgʻri <strong>못 냅니다</strong> deyish qoʻpol — <span class="cn-word" data-tr="...sa kerak, shekilli">-(으)ㄹ 것 같습니다</span> bilan yumshatiladi. ㉡: <span class="cn-word" data-tr="gap shundaki (mavzuga kirish)">다름이 아니라</span> bilan boshlangan rasmiy iltimos xati — soʻrov ham eng hurmatli shaklda: <span class="cn-word" data-tr="muddat">기한</span>ni uzaytirishni <strong>-(으)시겠습니까?</strong> bilan soʻraymiz.</p>''',
        "tips": '''<ul>
<li>Professor/rahbarga xat = eng yuqori hurmat darajasi: <em>-(으)시겠습니까?</em>, <em>-아/어 주실 수 있으십니까?</em></li>
<li>Rad etish yoki qiyinchilikni aytishda TOʻGʻRIDAN-TOʻGʻRI aytmang: <em>-기가 어려울 것 같습니다</em> — TOPIKda eng koʻp toʻgʻri javob chiqadigan qolip.</li>
<li><em>다름이 아니라</em> — rasmiy xatda asosiy gapga oʻtish iborasi; oʻrganib oling.</li>
<li>㉡ savol belgisi bilan tugaydi — javobingiz ham soʻroq boʻlishi shart.</li>
</ul>''',
    },

    # ── 51-5 · 안내문 — 동아리 모집 ─────────────────────────────────────
    {
        "qtype":   "51",
        "title":   "51-5: 안내문 — 요리 동아리 회원 모집",
        "summary": "Eʼlon-plakat: 모집합니다 va 누구나 -(으)ㄹ 수 있습니다 qoliplari.",
        "order":   5,
        "prompt":  PROMPT_51,
        "chart": '''<div class="wp-passage">
<p class="wp-passage-title">🍳 한국 요리 동아리 '맛나' 회원 모집 🍳</p>
<p>우리 동아리에서 함께 한국 요리를 배울 새 회원을 ( <span class="wp-slot">㉠</span> ). 요리를 한 번도 해 본 적이 없어도 괜찮습니다. 한국 요리에 관심이 있는 사람이라면 누구나 ( <span class="wp-slot">㉡</span> ). 신청은 이번 달 30일까지 학생회관 302호에서 받습니다. 많이 와 주시기 바랍니다.</p>
</div>''',
        "template_body": '''<p><span class="wp-frame-label">㉠</span> 우리 <span class="cn-word" data-tr="toʻgarak, klub">동아리</span>에서 함께 한국 요리를 배울 새 회원을 <span class="wp-blank" data-answer="모집합니다" data-alt="모집하고 있습니다|찾고 있습니다|구하고 있습니다"></span>.</p>
<p><span class="wp-frame-label">㉡</span> 한국 요리에 <span class="cn-word" data-tr="qiziqish">관심</span>이 있는 사람이라면 <span class="cn-word" data-tr="har kim, istalgan kishi">누구나</span> <span class="wp-blank" data-answer="신청할 수 있습니다" data-alt="가입할 수 있습니다|참여할 수 있습니다|들어올 수 있습니다"></span>.</p>''',
        "model_answer": '''<p><span class="wp-frame-label">㉠</span> 새 회원을 <span class="cn-word" data-pos="verb" data-tr="qabul qilmoq, yigʻmoq (aʼzo, xodim)">모집합니다</span></p>
<p class="wp-alt">(또는: 모집하고 있습니다 / 찾고 있습니다)</p>
<p><span class="wp-frame-label">㉡</span> 누구나 <span class="cn-word" data-pos="verb" data-tr="ariza bermoq">신청할</span> 수 있습니다</p>
<p class="wp-alt">(또는: 가입할 수 있습니다 / 참여할 수 있습니다)</p>
<p>💡 ㉠: sarlavhada <strong>회원 모집</strong> turibdi — birinchi jumla shu soʻzning feʼl shakli: <strong>모집합니다</strong>. ㉡: <span class="cn-word" data-tr="...boʻlgan kishi boʻlsa (shart)">-(이)라면</span> + 누구나 → imkoniyat: <span class="cn-word" data-tr="...sa boʻladi qolipi">-(으)ㄹ 수 있습니다</span>. Keyingi jumladagi <span class="cn-word" data-tr="ariza (topshirish)">신청</span> soʻzi ham katta maslahat.</p>''',
        "tips": '''<ul>
<li>모집 eʼlonlari deyarli bir xil qurilgan: 모집합니다 → shartlar → 누구나 -(으)ㄹ 수 있습니다 → 신청 tartibi. Skeletni yodlang.</li>
<li>㉡ ning javobi koʻpincha KEYINGI jumlada yashiringan boʻladi (bu yerda: 신청은 ... 받습니다 → 신청할 수 있습니다).</li>
<li><em>누구나</em> koʻrsangiz — javob 99% <em>-(으)ㄹ 수 있습니다</em> bilan tugaydi.</li>
<li>Eʼlon — ommaga yozilgan matn: faqat <em>-습니다</em> uslubi.</li>
</ul>''',
    },
]
