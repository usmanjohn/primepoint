# TOPIK II Listening — 9–12-savollar: Keyingi harakat (이어질 행동), lessons 1–3 (orders 30–32).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_action_1_3.py \
#            --out examprep/management/commands/audio/action
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_action_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/action

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "9–12-savollar: Keyingi harakat (이어질 행동)",
    "summary": "Dialogdan keyin so'ralgan kishi (여자/남자) darhol nima qilishini topish: ~아 주세요 kimga yuklaydi, 제가 ~할게요 kim oladi.",
    "icon":    "bi-person-walking",
    "order":   4,
}

LESSONS = [
    # ── Lesson 1 (order 30) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 이어질 행동 1: 9–12-savollar bilan tanishuv — kim nima qiladi?",
        "summary": "이어질 행동 savolining usuli: savolda KIM so'ralganini belgilang, oxirgi replikalardagi vazifa taqsimotini kuzating.",
        "order":   30,
        "blocks": [
            {"rich_text": """
<h2>🚶 9–12-savollar: dialogdan keyin nima bo'ladi?</h2>
<p>Bu guruhda dialog to'liq tugaydi, savol esa kelajak haqida: qatnashchilardan biri
<strong>darhol keyin</strong> nima qiladi?</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>9–12.</strong> 다음 대화를 잘 듣고 <u>여자가</u> 이어서
  할 행동으로 알맞은 것을 고르십시오. — <em>Dialogni eshitib, AYOL keyin qiladigan harakatni tanlang.</em></p>
</div>
<h3>Uch qadamli usul</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p><strong>1-qadam. KIMni belgilang.</strong> Savolda 여자가 (ayol) yoki 남자가
  (erkak) turadi — audio boshlanishidan OLDIN buni katta qilib belgilab qo'ying. Yarim
  xatolar aynan "boshqa odamning harakatini" tanlashdan chiqadi.</p></div>
  <div class="pp-step"><p><strong>2-qadam. Vazifa taqsimotini kuzating.</strong> Dialog oxirida ishlar
  bo'linadi: <mark style="background:#dbeafe;">~아/어 주세요, ~아/어 줄래요?</mark> — ish
  <strong>suhbatdoshga</strong> yuklanadi; <mark style="background:#dcfce7;">제가 ~할게요 /
  ~을게요</mark> — gapirayotgan odam ishni <strong>o'ziga</strong> oladi.</p></div>
  <div class="pp-step"><p><strong>3-qadam. "Darhol keyin"ni tanlang.</strong> Savol umumiy reja emas,
  <strong>hozir</strong> qilinadigan ish haqida. 지금/바로/먼저 bilan aytilgan harakat —
  eng kuchli nomzod.</p></div>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Oxirgi ikki replika deyarli har doim yetarli. Dialog boshini
  tushunmay qolsangiz ham sarosimaga tushmang — vazifalar oxirida taqsimlanadi.
</div>
"""},
            {"rich_text": """
<h3>🎧 Namuna: birga tahlil qilamiz</h3>
<p>Eshiting va ikkala qatnashchining "olgan" ishini ayting: erkak nima qiladi, ayol nima qiladi?</p>
""",
             "audio": "topik_l_030_1.mp3",
             "audio_script": [
                 ("여자", "다음 주 회의실 예약했어요?"),
                 ("남자", "아, 깜빡했어요. 지금 바로 예약할게요."),
                 ("여자", "그럼 저는 참석자들에게 안내 메일을 보낼게요."),
             ]},
            {"rich_text": """
<p>Vazifa taqsimoti aniq eshitildi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>남자:</strong> 지금 바로 <mark style="background:#dcfce7;">예약할게요</mark> → erkak hoziroq xonani band qiladi</p>
  <p style="font-size:1.05em;margin:0;"><strong>여자:</strong> 저는 메일을 <mark style="background:#dcfce7;">보낼게요</mark> → ayol xat yuboradi</p>
</div>
<p>Savol "남자가 이어서 할 행동" bo'lsa → <strong>회의실을 예약한다</strong>; "여자가…"
bo'lsa → <strong>메일을 보낸다</strong>. Bitta dialog — ikki xil to'g'ri javob: hammasi
savolda kim so'ralganiga bog'liq!</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 다음 주 회의실 예약했어요?<br>
    <em style="color:#475569;">Kelasi hafta uchun majlislar xonasini band qildingizmi?</em></p>
    <p><strong>남자:</strong> 아, 깜빡했어요. 지금 바로 예약할게요.<br>
    <em style="color:#475569;">Voy, esimdan chiqibdi. Hoziroq band qilaman.</em></p>
    <p><strong>여자:</strong> 그럼 저는 참석자들에게 안내 메일을 보낼게요.<br>
    <em style="color:#475569;">Unda men qatnashchilarga xabar xatini yuboraman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 대화를 잘 듣고 <u>남자가</u> 이어서 할 행동으로 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_030_2.mp3",
             "audio_script": [
                 ("남자", "손님, 죄송하지만 이 신발은 지금 매장에 없습니다. 창고에 있는지 확인해 볼까요?"),
                 ("여자", "네, 부탁드려요. 저는 그동안 다른 신발을 좀 보고 있을게요."),
             ],
             "choices": [
                 {"text": "창고에 신발이 있는지 확인한다. (Omborda poyabzal borligini tekshiradi.)", "is_correct": True},
                 {"text": "다른 신발을 구경한다. (Boshqa poyabzallarni ko'radi.)", "is_correct": False},
                 {"text": "새 신발을 신어 본다. (Yangi poyabzalni kiyib ko'radi.)", "is_correct": False},
                 {"text": "신발값을 계산한다. (Poyabzal pulini to'laydi.)", "is_correct": False},
             ],
             "explanation": """
<p>Savol <strong>남자</strong> haqida. Erkak taklif qildi: 확인해 <strong>볼까요?</strong> —
ayol qabul qildi (부탁드려요) → erkak <mark style="background:#dcfce7;">omborni
tekshiradi</mark> ✅. ② — <strong>ayolning</strong> ishi (저는 그동안… 보고 있을게요) —
klassik "boshqa odam" tuzog'i! ③④ dialogda umuman yo'q. ~을까요? + 부탁드려요 = taklif
qabul qilindi, endi u bajariladi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 손님, 죄송하지만 이 신발은 지금 매장에 없습니다. 창고에 있는지 확인해 볼까요?<br>
    <em style="color:#475569;">Mijoz, uzr, bu poyabzal hozir do'konda yo'q. Omborda bormikan, tekshirib ko'raymi?</em></p>
    <p><strong>여자:</strong> 네, 부탁드려요. 저는 그동안 다른 신발을 좀 보고 있을게요.<br>
    <em style="color:#475569;">Ha, iltimos. Men bu orada boshqa poyabzallarni ko'rib turaman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 대화를 잘 듣고 <u>여자가</u> 이어서 할 행동으로 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_030_3.mp3",
             "audio_script": [
                 ("여자", "프린터가 또 고장 났나 봐요. 화면에 빨간불이 켜져 있어요."),
                 ("남자", "종이가 걸렸을 거예요. 제가 한번 볼게요."),
                 ("여자", "고마워요. 그럼 저는 서비스 센터 전화번호를 찾아 놓을게요."),
             ],
             "choices": [
                 {"text": "서비스 센터의 전화번호를 찾는다. (Xizmat markazining telefon raqamini topib qo'yadi.)", "is_correct": True},
                 {"text": "프린터를 고친다. (Printerni tuzatadi.)", "is_correct": False},
                 {"text": "새 프린터를 주문한다. (Yangi printer buyurtma qiladi.)", "is_correct": False},
                 {"text": "종이를 사러 나간다. (Qog'oz olgani chiqib ketadi.)", "is_correct": False},
             ],
             "explanation": """
<p>Savol <strong>여자</strong> haqida. Taqsimot: printerni erkak ko'radi (<strong>제가</strong>
한번 볼게요), ayol esa — 저는 전화번호를 <strong>찾아 놓을게요</strong> →
<mark style="background:#dcfce7;">raqamni topib qo'yadi</mark> ✅. ② erkakning ishi —
yana o'sha tuzoq. ④ 종이 so'zi eshitildi (종이가 걸렸다 — qog'oz tiqilib qoldi), lekin
hech kim qog'oz sotib olmayapti. ~아/어 놓다 = oldindan qilib qo'ymoq — bu guruhda tez-tez
keladi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 프린터가 또 고장 났나 봐요. 화면에 빨간불이 켜져 있어요.<br>
    <em style="color:#475569;">Printer yana buzilganga o'xshaydi. Ekranida qizil chiroq yonib turibdi.</em></p>
    <p><strong>남자:</strong> 종이가 걸렸을 거예요. 제가 한번 볼게요.<br>
    <em style="color:#475569;">Qog'oz tiqilib qolgandir. Men bir ko'rib chiqaman.</em></p>
    <p><strong>여자:</strong> 고마워요. 그럼 저는 서비스 센터 전화번호를 찾아 놓을게요.<br>
    <em style="color:#475569;">Rahmat. Unda men xizmat markazining telefon raqamini topib qo'yaman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">이어서 할 행동</div><div class="pp-card-back">keyin qiladigan harakat</div></div>
  <div class="pp-card"><div class="pp-card-front">예약하다</div><div class="pp-card-back">band qilmoq (bron)</div></div>
  <div class="pp-card"><div class="pp-card-front">깜빡하다</div><div class="pp-card-back">esidan chiqarmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">창고</div><div class="pp-card-back">ombor</div></div>
  <div class="pp-card"><div class="pp-card-front">고장 나다</div><div class="pp-card-back">buzilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">종이가 걸리다</div><div class="pp-card-back">qog'oz tiqilib qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">~아/어 놓다</div><div class="pp-card-back">oldindan qilib qo'ymoq</div></div>
  <div class="pp-card"><div class="pp-card-front">그동안</div><div class="pp-card-back">shu orada</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Avval savolda <strong>KIM</strong> so'ralganini belgilang (여자가? 남자가?).</li>
  <li>~아 주세요 → ish suhbatdoshda; 제가 ~을게요 → ish gapiruvchida.</li>
  <li>Eng kuchli tuzoq — <strong>boshqa odamning harakati</strong>: dialogda bor, lekin savoldagi kishiniki emas.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 31) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 이어질 행동 2: Uch tuzoq — boshqa odam, bo'lgan ish, uzoq reja",
        "summary": "이어질 행동 savolining uch tuzog'i: boshqa qatnashchining ishi, allaqachon qilingan ish (이미/벌써) va 'hozir emas, keyin' rejalar.",
        "order":   31,
        "blocks": [
            {"rich_text": """
<h2>🪤 Noto'g'ri variantlar qayerdan keladi?</h2>
<p>9–12-savollarda to'rt variantning uchtasi ham dialogda "eshitilgan" bo'ladi — shunda
qanday adashmaslik mumkin? Noto'g'ri variantlar deyarli doim shu <strong>uch qolipdan</strong>
yasaladi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 8px;"><strong>Tuzoq 1 — Boshqa odamning ishi.</strong>
  Savol ayol haqida, variant esa erkakning vazifasi. Davo: KIMni oldindan belgilash.</p>
  <p style="font-size:1.05em;margin:0 0 8px;"><strong>Tuzoq 2 — Allaqachon qilingan ish.</strong>
  <mark style="background:#fee2e2;">이미 / 벌써 / 어제 ~았어요</mark> bilan aytilgan ish
  "keyingi harakat" bo'lolmaydi. Davo: zamonni eshiting — o'tgan zamon = chiqarib tashlang.</p>
  <p style="font-size:1.05em;margin:0;"><strong>Tuzoq 3 — Uzoq reja.</strong> 다음 주에 /
  나중에 qilinadigan ish ham to'g'ri emas — savol <strong>darhol keyingi</strong> qadam
  haqida. Davo: 지금 / 바로 / 먼저 belgilarini qidiring.</p>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Tartib so'zlari zanjiri: <strong>먼저</strong> (avval) →
  <strong>그다음에</strong> (keyin) → <strong>이따가/나중에</strong> (keyinroq). Javob —
  zanjirning <strong>boshidagi</strong> harakat.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 대화를 잘 듣고 <u>여자가</u> 이어서 할 행동으로 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_031_1.mp3",
             "audio_script": [
                 ("여자", "공연 표는 예매했어요?"),
                 ("남자", "네, 어제 두 장 예매했어요. 그런데 공연장까지 어떻게 가는지 아세요?"),
                 ("여자", "잘 모르겠네요. 제가 지금 지하철 노선을 찾아볼게요."),
             ],
             "choices": [
                 {"text": "지하철 노선을 찾아본다. (Metro yo'nalishini qidirib ko'radi.)", "is_correct": True},
                 {"text": "공연 표를 예매한다. (Tomosha chiptasini band qiladi.)", "is_correct": False},
                 {"text": "공연장에서 남자를 기다린다. (Tomosha zalida erkakni kutadi.)", "is_correct": False},
                 {"text": "표 두 장을 환불한다. (Ikkita chiptani qaytaradi.)", "is_correct": False},
             ],
             "explanation": """
<p>Ayolning o'z og'zidan: <strong>제가 지금</strong> 지하철 노선을 찾아볼게요 → ✅ ①
(지금 — darhol belgisi!). ② — <strong>Tuzoq 2</strong>ning sof namunasi: chiptalar
<strong>어제</strong> (kecha) allaqachon olingan, buni erkak qildi — ya'ni bir variantda
ikki tuzoq birga (bo'lgan ish + boshqa odam). O'tgan zamonni eshitish — yarim javob.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 공연 표는 예매했어요?<br>
    <em style="color:#475569;">Tomosha chiptalarini band qildingizmi?</em></p>
    <p><strong>남자:</strong> 네, 어제 두 장 예매했어요. 그런데 공연장까지 어떻게 가는지 아세요?<br>
    <em style="color:#475569;">Ha, kecha ikkita band qildim. Aytgancha, tomosha zaligacha qanday borishni bilasizmi?</em></p>
    <p><strong>여자:</strong> 잘 모르겠네요. 제가 지금 지하철 노선을 찾아볼게요.<br>
    <em style="color:#475569;">Bilmayman-ov. Men hozir metro yo'nalishini qidirib ko'raman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 대화를 잘 듣고 <u>남자가</u> 이어서 할 행동으로 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_031_2.mp3",
             "audio_script": [
                 ("남자", "발표 자료는 어제 다 만들었으니까 이제 인쇄만 하면 돼요."),
                 ("여자", "그럼 인쇄는 제가 할게요. 몇 부 필요해요?"),
                 ("남자", "열 부요. 고마워요. 저는 회의실에 노트북을 설치해 놓을게요."),
             ],
             "choices": [
                 {"text": "회의실에 노트북을 설치한다. (Majlislar xonasiga noutbukni o'rnatadi.)", "is_correct": True},
                 {"text": "발표 자료를 만든다. (Taqdimot materialini tayyorlaydi.)", "is_correct": False},
                 {"text": "자료를 열 부 인쇄한다. (Materialni o'n nusxa chop etadi.)", "is_correct": False},
                 {"text": "새 노트북을 산다. (Yangi noutbuk sotib oladi.)", "is_correct": False},
             ],
             "explanation": """
<p>Uchala tuzoq bir savolda! ② — <strong>bo'lgan ish</strong> (어제 다 만들었으니까 —
kecha tayyor bo'lgan). ③ — <strong>boshqa odam</strong> (인쇄는 <strong>제가</strong>
할게요 — ayol!). ④ — umuman aytilmagan. Erkakning keyingi ishi o'z og'zidan:
저는 노트북을 <mark style="background:#dcfce7;">설치해 놓을게요</mark> ✅. Vazifa
bo'linayotganda har replika oxiridagi 을게요 kimniki ekanini kuzatib boring.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 발표 자료는 어제 다 만들었으니까 이제 인쇄만 하면 돼요.<br>
    <em style="color:#475569;">Taqdimot materialini kecha tayyorlab bo'ldim, endi faqat chop etish qoldi.</em></p>
    <p><strong>여자:</strong> 그럼 인쇄는 제가 할게요. 몇 부 필요해요?<br>
    <em style="color:#475569;">Unda chop etishni men qilaman. Necha nusxa kerak?</em></p>
    <p><strong>남자:</strong> 열 부요. 고마워요. 저는 회의실에 노트북을 설치해 놓을게요.<br>
    <em style="color:#475569;">O'n nusxa. Rahmat. Men majlislar xonasiga noutbukni o'rnatib qo'yaman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 다음 대화를 잘 듣고 <u>여자가</u> 이어서 할 행동으로 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_031_3.mp3",
             "audio_script": [
                 ("여자", "다음 주 출장 때 입을 정장을 세탁소에 맡겨야 하는데 시간이 없네요."),
                 ("남자", "세탁소는 제가 퇴근길에 들를게요. 옷 좀 주세요."),
                 ("여자", "정말요? 고마워요. 지금 가져올게요."),
             ],
             "choices": [
                 {"text": "정장을 가지러 간다. (Kostyumni olib kelgani boradi.)", "is_correct": True},
                 {"text": "세탁소에 옷을 맡긴다. (Kimyoviy tozalashga kiyim topshiradi.)", "is_correct": False},
                 {"text": "출장을 간다. (Xizmat safariga jo'naydi.)", "is_correct": False},
                 {"text": "새 정장을 사러 간다. (Yangi kostyum olgani boradi.)", "is_correct": False},
             ],
             "explanation": """
<p>Ayolning oxirgi gapi: <strong>지금 가져올게요</strong> (hozir olib kelaman) →
<mark style="background:#dcfce7;">kostyumni olib kelgani boradi</mark> ✅ — 지금 =
darhol belgisi. ② — <strong>erkakning</strong> zimmasiga o'tdi (세탁소는 제가 들를게요).
③ — <strong>uzoq reja</strong> (다음 주 — kelasi hafta!): Tuzoq 3. Uchchala davolash
usuli bitta savolda ishladi: kim? qachon bo'lgan? qachon bo'ladi?</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 다음 주 출장 때 입을 정장을 세탁소에 맡겨야 하는데 시간이 없네요.<br>
    <em style="color:#475569;">Kelasi haftadagi xizmat safarida kiyadigan kostyumni tozalashga berishim kerak edi, vaqt yo'q-da.</em></p>
    <p><strong>남자:</strong> 세탁소는 제가 퇴근길에 들를게요. 옷 좀 주세요.<br>
    <em style="color:#475569;">Tozalash joyiga ishdan qaytishda o'zim kirib o'taman. Kiyimni bering.</em></p>
    <p><strong>여자:</strong> 정말요? 고마워요. 지금 가져올게요.<br>
    <em style="color:#475569;">Rostdanmi? Rahmat. Hozir olib kelaman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">노선</div><div class="pp-card-back">yo'nalish (transport)</div></div>
  <div class="pp-card"><div class="pp-card-front">인쇄하다</div><div class="pp-card-back">chop etmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">몇 부</div><div class="pp-card-back">necha nusxa</div></div>
  <div class="pp-card"><div class="pp-card-front">설치하다</div><div class="pp-card-back">o'rnatmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">출장</div><div class="pp-card-back">xizmat safari</div></div>
  <div class="pp-card"><div class="pp-card-front">맡기다</div><div class="pp-card-back">topshirmoq, ishonib bermoq</div></div>
  <div class="pp-card"><div class="pp-card-front">들르다</div><div class="pp-card-back">yo'l-yo'lakay kirib o'tmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">퇴근길에</div><div class="pp-card-back">ishdan qaytish yo'lida</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Uch tuzoq: <strong>boshqa odam</strong>, <strong>bo'lgan ish</strong> (이미/벌써/어제), <strong>uzoq reja</strong> (다음 주에/나중에).</li>
  <li>Davolar: kimni belgilash, zamonni eshitish, 지금/바로/먼저ni qidirish.</li>
  <li>먼저 → 그다음에 → 이따가 zanjirida javob — boshidagi harakat.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 32) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 이어질 행동 3: To'liq amaliyot — to'rtta dialog imtihondagidek",
        "summary": "9–12-savollar to'liq to'plami: restoran, ofis, dorixona va telefon suhbati — har audioni bir marta eshitib, keyingi harakatni toping.",
        "order":   32,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: 9, 10, 11, 12-savollar</h2>
<p>Imtihondagi to'liq guruh — to'rtta dialog. Har birida avval savoldagi <strong>KIMni</strong>
belgilang, audioni <strong>bir marta</strong> eshiting, uch tuzoqni esdan chiqarmang:
boshqa odam · bo'lgan ish · uzoq reja.</p>
"""},
            {"rich_text": """
<p><strong>9-savol.</strong> 다음 대화를 잘 듣고 <u>여자가</u> 이어서 할 행동으로 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_032_1.mp3",
             "audio_script": [
                 ("남자", "어서 오세요. 예약하셨습니까?"),
                 ("여자", "아니요. 지금 두 사람 자리 있어요?"),
                 ("남자", "죄송합니다. 지금은 자리가 다 차서 이십 분쯤 기다리셔야 합니다. 여기 대기자 명단에 성함을 적어 주세요."),
             ],
             "choices": [
                 {"text": "명단에 이름을 적는다. (Ro'yxatga ismini yozadi.)", "is_correct": True},
                 {"text": "자리를 예약하고 집에 간다. (Joy band qilib uyiga ketadi.)", "is_correct": False},
                 {"text": "다른 식당을 찾아본다. (Boshqa restoran qidiradi.)", "is_correct": False},
                 {"text": "음식을 주문한다. (Ovqat buyurtma qiladi.)", "is_correct": False},
             ],
             "explanation": """
<p>Oxirgi replika — to'g'ridan-to'g'ri iltimos: 성함을 <strong>적어 주세요</strong>
(ismingizni yozing) → ayolning darhol keyingi ishi:
<mark style="background:#dcfce7;">ro'yxatga ism yozish</mark> ✅. ④ hali erta — avval
20 daqiqa kutish bor (savol "keyin nima" emas, "DARHOL keyin nima"!). ~아/어 주세요 ayolga
qaratilgan — demak ishni ayol bajaradi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 어서 오세요. 예약하셨습니까?<br>
    <em style="color:#475569;">Xush kelibsiz. Joy band qilganmisiz?</em></p>
    <p><strong>여자:</strong> 아니요. 지금 두 사람 자리 있어요?<br>
    <em style="color:#475569;">Yo'q. Hozir ikki kishilik joy bormi?</em></p>
    <p><strong>남자:</strong> 죄송합니다. 지금은 자리가 다 차서 이십 분쯤 기다리셔야 합니다. 여기 대기자 명단에 성함을 적어 주세요.<br>
    <em style="color:#475569;">Uzr. Hozir joylar to'la, yigirma daqiqacha kutishingiz kerak. Mana bu navbat ro'yxatiga ismingizni yozib qo'ying.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>10-savol.</strong> 다음 대화를 잘 듣고 <u>여자가</u> 이어서 할 행동으로 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_032_2.mp3",
             "audio_script": [
                 ("여자", "부장님, 신제품 발표회 장소는 정해졌어요?"),
                 ("남자", "네, 호텔 대회의실로 정했어요. 그런데 초대장이 아직 준비가 안 됐네요. 김 대리한테 초대장 제작 좀 부탁해 줄래요?"),
                 ("여자", "네, 지금 바로 전달할게요."),
             ],
             "choices": [
                 {"text": "김 대리에게 초대장 제작을 부탁한다. (Kim Teriga taklifnoma tayyorlashni topshiradi.)", "is_correct": True},
                 {"text": "발표회 장소를 정한다. (Taqdimot joyini belgilaydi.)", "is_correct": False},
                 {"text": "초대장을 직접 만든다. (Taklifnomani o'zi yasaydi.)", "is_correct": False},
                 {"text": "호텔에 전화해서 예약을 취소한다. (Mehmonxonaga qo'ng'iroq qilib bronni bekor qiladi.)", "is_correct": False},
             ],
             "explanation": """
<p>Iltimos zanjiri ehtiyot bo'lishni talab qiladi: boshliq ayoldan <strong>Kim Teriga
yetkazishni</strong> so'radi (부탁해 줄래요?), ayol rozi (지금 바로 전달할게요) → ✅ ①.
③ nozik tuzoq: taklifnomani <strong>ayol emas, Kim Teri</strong> yasaydi — ayol faqat
topshiriqni yetkazadi! ② bo'lgan ish (정해졌어요 — allaqachon hal). Kim → kimga → nimani:
zanjirni aniq eshiting.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 부장님, 신제품 발표회 장소는 정해졌어요?<br>
    <em style="color:#475569;">Boshliq, yangi mahsulot taqdimoti joyi belgilandimi?</em></p>
    <p><strong>남자:</strong> 네, 호텔 대회의실로 정했어요. 그런데 초대장이 아직 준비가 안 됐네요. 김 대리한테 초대장 제작 좀 부탁해 줄래요?<br>
    <em style="color:#475569;">Ha, mehmonxonaning katta zaliga belgiladik. Lekin taklifnomalar hali tayyor emas ekan. Kim Teridan taklifnoma tayyorlashni so'rab bera olasizmi?</em></p>
    <p><strong>여자:</strong> 네, 지금 바로 전달할게요.<br>
    <em style="color:#475569;">Xo'p, hoziroq yetkazaman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>11-savol.</strong> 다음 대화를 잘 듣고 <u>여자가</u> 이어서 할 행동으로 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_032_3.mp3",
             "audio_script": [
                 ("남자", "이 약은 하루에 세 번, 식사하고 삼십 분 후에 드세요."),
                 ("여자", "네. 그런데 요즘 밤에 잠이 안 오는데 괜찮을까요?"),
                 ("남자", "그럼 이 안내문을 먼저 읽어 보세요. 주의할 점이 다 적혀 있어요. 그래도 불편하시면 다시 오세요."),
             ],
             "choices": [
                 {"text": "안내문을 읽어 본다. (Yo'riqnomani o'qib chiqadi.)", "is_correct": True},
                 {"text": "약을 하루에 세 번 먹는다. (Dorini kuniga uch mahal ichadi.)", "is_correct": False},
                 {"text": "바로 다시 병원에 간다. (Darhol yana shifoxonaga boradi.)", "is_correct": False},
                 {"text": "밤에 일찍 잔다. (Kechasi erta uxlaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>Tartib so'zi hal qiladi: 안내문을 <strong>먼저</strong> 읽어 보세요 (AVVAL yo'riqnomani
o'qing) → ✅ ①. ② ham qilinadi, lekin u <strong>umumiy dori tartibi</strong>, "darhol
keyingi" qadam emas; ③ esa faqat <strong>shart bajarilsa</strong> (그래도 불편하시면 —
shunda ham noqulay bo'lsa) — hozir emas. 먼저 → keyin → agar: zanjirning boshini oling.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 이 약은 하루에 세 번, 식사하고 삼십 분 후에 드세요.<br>
    <em style="color:#475569;">Bu dorini kuniga uch mahal, ovqatdan o'ttiz daqiqa keyin iching.</em></p>
    <p><strong>여자:</strong> 네. 그런데 요즘 밤에 잠이 안 오는데 괜찮을까요?<br>
    <em style="color:#475569;">Xo'p. Lekin keyingi paytlarda kechasi uyqum kelmayapti, muammo bo'lmaydimi?</em></p>
    <p><strong>남자:</strong> 그럼 이 안내문을 먼저 읽어 보세요. 주의할 점이 다 적혀 있어요. 그래도 불편하시면 다시 오세요.<br>
    <em style="color:#475569;">Unda avval mana bu yo'riqnomani o'qib chiqing. Ehtiyot choralari hammasi yozilgan. Shunda ham noqulaylik bo'lsa, yana keling.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>12-savol.</strong> 다음 대화를 잘 듣고 <u>남자가</u> 이어서 할 행동으로 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_032_4.mp3",
             "audio_script": [
                 ("여자", "여보세요, 손님. 아까 저희 가게에 지갑을 두고 가셨어요."),
                 ("남자", "아, 정말요? 지금 바로 찾으러 갈게요. 몇 시까지 문을 여세요?"),
                 ("여자", "밤 아홉 시까지니까 천천히 오셔도 돼요."),
             ],
             "choices": [
                 {"text": "지갑을 찾으러 가게에 간다. (Hamyonini olgani do'konga boradi.)", "is_correct": True},
                 {"text": "가게에 지갑을 두고 나온다. (Do'konda hamyonini qoldirib chiqadi.)", "is_correct": False},
                 {"text": "아홉 시까지 가게 문을 연다. (Soat to'qqizgacha do'konni ochiq tutadi.)", "is_correct": False},
                 {"text": "새 지갑을 사러 간다. (Yangi hamyon olgani boradi.)", "is_correct": False},
             ],
             "explanation": """
<p>Erkakning o'zi aytdi: <strong>지금 바로 찾으러 갈게요</strong> (hoziroq olgani boraman) →
✅ ①. ② allaqachon bo'lib o'tgan voqea (두고 가셨어요 — qoldirib ketgansiz), ③ —
<strong>ayolning</strong> (do'konning) ishi. Telefon suhbatlarida ham qoidalar o'zgarmaydi:
kim, qachon, nima. To'rt savoldan nechtasi to'g'ri chiqdi? Endi bu guruh ham sizniki! 🎉</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 여보세요, 손님. 아까 저희 가게에 지갑을 두고 가셨어요.<br>
    <em style="color:#475569;">Allo, mijoz. Boya do'konimizda hamyoningizni qoldirib ketibsiz.</em></p>
    <p><strong>남자:</strong> 아, 정말요? 지금 바로 찾으러 갈게요. 몇 시까지 문을 여세요?<br>
    <em style="color:#475569;">Voy, rostdanmi? Hoziroq olgani boraman. Soat nechagacha ochiqsiz?</em></p>
    <p><strong>여자:</strong> 밤 아홉 시까지니까 천천히 오셔도 돼요.<br>
    <em style="color:#475569;">Kechqurun to'qqizgacha, shoshilmasangiz ham bo'ladi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">자리가 차다</div><div class="pp-card-back">joylar to'lmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">대기자 명단</div><div class="pp-card-back">navbat ro'yxati</div></div>
  <div class="pp-card"><div class="pp-card-front">성함</div><div class="pp-card-back">ism (hurmat shakli)</div></div>
  <div class="pp-card"><div class="pp-card-front">초대장</div><div class="pp-card-back">taklifnoma</div></div>
  <div class="pp-card"><div class="pp-card-front">전달하다</div><div class="pp-card-back">yetkazmoq, uzatmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">안내문</div><div class="pp-card-back">yo'riqnoma</div></div>
  <div class="pp-card"><div class="pp-card-front">지갑을 두고 가다</div><div class="pp-card-back">hamyonni qoldirib ketmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">찾으러 가다</div><div class="pp-card-back">olgani bormoq</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>KIMni belgilang → vazifa taqsimotini kuzating (~아 주세요 / 제가 ~을게요) → darhol keyingi qadamni oling.</li>
  <li>Uch tuzoq: boshqa odam · bo'lgan ish (어제/벌써) · uzoq reja yoki shartli ish (그래도 ~면).</li>
  <li>먼저 eshitilsa — javob deyarli doim o'sha yerda.</li>
</ul>
"""},
        ],
    },
]
