# TOPIK II Listening — 43–46-savollar: Hujjatli film va ma'ruza (다큐멘터리·강연), lessons 1–3 (orders 100–102).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_docu_1_3.py \
#            --out examprep/management/commands/audio/docu
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_docu_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/docu

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "43–46-savollar: Hujjatli film va ma'ruza (다큐멘터리·강연)",
    "summary": "Hujjatli hikoyachi ovozi: bosh mazmun, 'nega?' savoli (이유) va ma'ruzachining gapirish uslubi (말하기 방식).",
    "icon":    "bi-film",
    "order":   11,
}

LESSONS = [
    # ── Lesson 1 (order 100) ──────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 다큐 1: 43–44-savollar — hikoyachi ovozi va \"nega?\"",
        "summary": "다큐멘터리 juftligi: yakka hikoyachi tabiat/tarix haqida gapiradi; bosh mazmun + aniq bir harakatning SABABI so'raladi.",
        "order":   100,
        "blocks": [
            {"rich_text": """
<h2>🎬 43–44-savollar: hujjatli film ovozi</h2>
<p>Bu juftlik — <strong>다큐멘터리</strong>: bitta hikoyachi (해설) tabiat, fan yoki tarix
haqida badiiy ohangda so'zlaydi. Savollar:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>43.</strong> 이 이야기의 중심 내용으로 알맞은 것을 고르십시오. — <em>bosh mazmun.</em></p>
  <p style="font-size:1.08em;margin:0;"><strong>44.</strong> ~하는 이유로 알맞은 것을 고르십시오. — <em>aniq bir harakatning SABABI.</em></p>
</div>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p><strong>44 birinchi!</strong> Audio boshlanishidan oldin 44-savolning
  matnini o'qing — u sizga "X nega Y qiladi?" deb aniq nishon beradi. Birinchi eshitishda
  aynan o'sha joyni oving: sabab <mark style="background:#dbeafe;">~기 때문이다 / ~기
  위해서다 / ~려고</mark> bilan keladi.</p></div>
  <div class="pp-step"><p><strong>43 — katta rasm.</strong> Hujjatli matnning bosh mazmuni odatda
  <strong>oxirgi jumlada</strong> she'riy xulosa bo'lib keladi (이렇게/결국 + umumlashma).</p></div>
  <div class="pp-step"><p><strong>Hikoyachi uslubiga ko'nikish:</strong> gaplar qisqa, zamon ba'zan
  hozirgi (만든다, 이겨 낸다) — bu badiiy uslub, chalg'imang.</p></div>
</div>
"""},
            {"rich_text": """
<p><strong>43-savol.</strong> 이 이야기의 중심 내용으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_100_1.mp3",
             "audio_script": [
                 ("남자", "남극의 겨울. 황제펭귄들은 서로 몸을 붙여 거대한 원을 만든다. 바깥쪽에 선 펭귄들이 차가운 바람을 막는 동안 안쪽의 펭귄들은 몸을 데운다. 시간이 지나면 안과 밖의 펭귄들이 자리를 바꾼다. 이렇게 자리를 바꾸는 것은 모두가 함께 살아남기 위해서다. 혹독한 추위 속에서 황제펭귄들은 홀로가 아니라 함께 모여 긴 겨울을 이겨 낸다."),
             ],
             "choices": [
                 {"text": "황제펭귄은 서로 협력해서 추위를 이겨 낸다. (Imperator pingvinlari hamkorlikda sovuqni yengadi.)", "is_correct": True},
                 {"text": "남극의 겨울은 짧고 따뜻하다. (Antarktida qishi qisqa va iliq.)", "is_correct": False},
                 {"text": "펭귄은 혼자 있는 것을 좋아한다. (Pingvin yolg'izlikni yoqtiradi.)", "is_correct": False},
                 {"text": "펭귄은 바람이 불면 바다로 들어간다. (Pingvin shamol tursa dengizga kiradi.)", "is_correct": False},
             ],
             "explanation": """
<p>Oxirgi jumla — she'riy xulosa: <strong>홀로가 아니라 함께</strong> 모여 겨울을 이겨
낸다 → ✅ ① (협력 = birga harakat — paraphrase). Yana o'sha oltin qolip: "A가 아니라 B" —
javob B (함께!) tomonida. ③ aynan teskarisi. Hujjatli matnning har detali (davra, joy
almashish) — shu bitta soyabon ostida.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 남극의 겨울. 황제펭귄들은 서로 몸을 붙여 거대한 원을 만든다.
    바깥쪽에 선 펭귄들이 차가운 바람을 막는 동안 안쪽의 펭귄들은 몸을 데운다. 시간이 지나면
    안과 밖의 펭귄들이 자리를 바꾼다. 이렇게 자리를 바꾸는 것은 모두가 함께 살아남기 위해서다.
    혹독한 추위 속에서 황제펭귄들은 홀로가 아니라 함께 모여 긴 겨울을 이겨 낸다.<br>
    <em style="color:#475569;">Antarktida qishi. Imperator pingvinlari bir-biriga suyanib ulkan
    davra hosil qiladi. Tashqarida turganlari sovuq shamolni to'sib turar ekan, ichkaridagilari
    isinib oladi. Vaqt o'tishi bilan ichkari va tashqaridagi pingvinlar joy almashadi. Bu joy
    almashish — hammaning birga omon qolishi uchun. Shafqatsiz sovuqda imperator pingvinlari
    yolg'iz emas, birgalikda uzun qishni yengib o'tadi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>44-savol.</strong> 펭귄들이 자리를 바꾸는 이유로 알맞은 것을 고르십시오. <em>(audio yuqorida — ikkinchi marta eshiting)</em></p>
""",
             "choices": [
                 {"text": "모두가 함께 살아남기 위해서 (Hammaning birga omon qolishi uchun)", "is_correct": True},
                 {"text": "먹이를 찾기 위해서 (Ozuqa topish uchun)", "is_correct": False},
                 {"text": "새끼를 낳기 위해서 (Bola tug'ish uchun)", "is_correct": False},
                 {"text": "바람의 방향이 바뀌어서 (Shamol yo'nalishi o'zgargani uchun)", "is_correct": False},
             ],
             "explanation": """
<p>Sabab jumlasi qolip bilan keldi: 자리를 바꾸는 것은 ~ 살아남기 <strong>위해서다</strong> →
✅ ①. 44-savolda javob har doim matnda <strong>ochiq aytiladi</strong> — taxmin qilish
kerak emas, faqat ~기 위해서 / ~기 때문에 jumlasini ovlash kerak. ②③④ mantiqan mumkin
tuyuladi — lekin matnda YO'Q: o'z bilimingizdan emas, eshitilgandan javob bering!</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">다큐멘터리</div><div class="pp-card-back">hujjatli film</div></div>
  <div class="pp-card"><div class="pp-card-front">남극</div><div class="pp-card-back">Antarktida (Janubiy qutb)</div></div>
  <div class="pp-card"><div class="pp-card-front">황제펭귄</div><div class="pp-card-back">imperator pingvini</div></div>
  <div class="pp-card"><div class="pp-card-front">막다</div><div class="pp-card-back">to'smoq</div></div>
  <div class="pp-card"><div class="pp-card-front">데우다</div><div class="pp-card-back">isitmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">살아남다</div><div class="pp-card-back">omon qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">혹독하다</div><div class="pp-card-back">shafqatsiz, qattiq</div></div>
  <div class="pp-card"><div class="pp-card-front">이겨 내다</div><div class="pp-card-back">yengib o'tmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>44 ni birinchi o'qing — u aniq nishon beradi; javob ~기 위해서 / ~기 때문에 jumlasida ochiq turadi.</li>
  <li>43 — oxirgi jumladagi she'riy xulosa (이렇게/결국 + "A가 아니라 B").</li>
  <li>O'z bilimingizdan emas — faqat eshitilgandan javob bering.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 101) ──────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 다큐 2: Gapirish uslubi (말하기 방식) — 45–46-savollar",
        "summary": "45–46 ma'ruza juftligi: mazmun + ma'ruzachi QANDAY tushuntiryapti (misol bilan, taqqoslab, tartib bilan…).",
        "order":   101,
        "blocks": [
            {"rich_text": """
<h2>🗣️ 46-savol: U QANDAY tushuntiryapti?</h2>
<p>45–46 juftligi — ma'ruza; 45 tanish 내용 일치, 46 esa yangi savol:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>46.</strong> 여자의 말하기 방식으로 가장 알맞은 것을
  고르십시오. — <em>ma'ruzachining tushuntirish USLUBI.</em></p>
</div>
<p>Variantlar tayyor ro'yxatdan — har birining o'z ovozli belgisi bor:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>예를 들어 설명하고 있다</strong> — misollar bilan (belgi: 예를 들어, ~처럼)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>비교를 통해 설명하고 있다</strong> — taqqoslab (belgi: ~보다, 반면에, 비교해 보세요)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>과정을 순서대로 설명하고 있다</strong> — bosqichma-bosqich (belgi: 먼저, 그다음에, 마지막으로)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>연구 결과를 근거로 주장하고 있다</strong> — tadqiqotga tayanib (belgi: 연구에 따르면, 조사 결과)</p>
  <p style="font-size:1.05em;margin:0;"><strong>질문을 던지며 화제를 제시하고 있다</strong> — savol tashlab (belgi: ~을까요? bilan boshlash)</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Usul:</strong> 46 uchun MAZMUNNI emas, <strong>signal so'zlarni</strong> sanang:
  nechta 예를 들어? ~보다 bormi? 먼저-그다음 zanjiri-chi? Eng ko'p belgi to'plagan uslub —
  javob.
</div>
"""},
            {"rich_text": """
<p><strong>45-savol.</strong> 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_101_1.mp3",
             "audio_script": [
                 ("여자", "조선 시대에도 오늘날의 냉장고나 세탁기처럼 생활을 돕는 도구들이 있었습니다. 예를 들어 다듬이는 옷의 주름을 펴 주는 다리미 역할을 했고, 맷돌은 콩을 가는 기계 역할을 했지요. 우물가의 빨래터는 마을의 세탁기이자 사랑방이었습니다. 이처럼 우리 조상들은 필요한 도구를 스스로 만들어 생활을 편리하게 했습니다."),
             ],
             "choices": [
                 {"text": "맷돌은 콩을 가는 데 사용되었다. (Qo'l tegirmoni loviya maydalashda ishlatilgan.)", "is_correct": True},
                 {"text": "조선 시대에는 생활 도구가 전혀 없었다. (Choson davrida ro'zg'or asboblari umuman bo'lmagan.)", "is_correct": False},
                 {"text": "다듬이는 음식을 만드는 도구였다. (Tadimi — ovqat tayyorlash asbobi edi.)", "is_correct": False},
                 {"text": "조상들은 도구를 다른 나라에서 사 왔다. (Ajdodlar asboblarni chetdan sotib olgan.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② butun ma'ruzaga zid (도구들이 <strong>있었습니다</strong>!), ③ vazifa
almashtirilgan (다듬이 — <strong>kiyim g'ijimini</strong> yozadigan asbob, ovqat emas!),
④ teskari (<strong>스스로 만들어</strong> — o'zlari yasagan!). ✅ ①: 맷돌은 콩을 가는
기계 역할 — aynan aytilgan. Ikki asbob yonma-yon kelsa (다듬이/맷돌), vazifalarini
almashtirib berish — bu blokning sevimli tuzog'i.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 조선 시대에도 오늘날의 냉장고나 세탁기처럼 생활을 돕는 도구들이
    있었습니다. 예를 들어 다듬이는 옷의 주름을 펴 주는 다리미 역할을 했고, 맷돌은 콩을 가는
    기계 역할을 했지요. 우물가의 빨래터는 마을의 세탁기이자 사랑방이었습니다. 이처럼 우리
    조상들은 필요한 도구를 스스로 만들어 생활을 편리하게 했습니다.<br>
    <em style="color:#475569;">Choson davrida ham bugungi muzlatkich yoki kir mashinasi kabi
    turmushga yordam beradigan asboblar bo'lgan. Masalan, tadimi kiyim g'ijimini yozadigan
    dazmol vazifasini, qo'l tegirmoni esa loviya maydalaydigan mashina vazifasini bajargan.
    Quduq bo'yidagi kir yuvish joyi qishloqning kir mashinasi ham, suhbat maskani ham edi.
    Shu tariqa ajdodlarimiz kerakli asboblarni o'zlari yasab, turmushni qulay qilishgan.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>46-savol.</strong> 여자의 말하기 방식으로 가장 알맞은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "옛날 도구를 오늘날의 물건에 비유하고 예를 들어 설명하고 있다. (Qadimgi asboblarni bugungi buyumlarga o'xshatib, misollar bilan tushuntirmoqda.)", "is_correct": True},
                 {"text": "실험 과정을 순서대로 보여 주고 있다. (Tajriba jarayonini tartib bilan ko'rsatmoqda.)", "is_correct": False},
                 {"text": "연구 결과의 문제점을 비판하고 있다. (Tadqiqot natijasi kamchiliklarini tanqid qilmoqda.)", "is_correct": False},
                 {"text": "듣는 사람에게 결정을 요구하고 있다. (Tinglovchidan qaror talab qilmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Signal so'zlarni sanaymiz: 냉장고나 세탁기<strong>처럼</strong> (o'xshatish!) +
<strong>예를 들어</strong> + 다리미 <strong>역할</strong>, 세탁기<strong>이자</strong>… +
<strong>이처럼</strong> (misollardan xulosa) → ✅ ①. Birorta 먼저/그다음 yo'q (② yo'q),
tanqid ohangi yo'q (③ yo'q). 46 — mazmun savoli emas, <strong>shakl</strong> savoli:
faqat belgilar hisobi!</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">말하기 방식</div><div class="pp-card-back">gapirish uslubi</div></div>
  <div class="pp-card"><div class="pp-card-front">예를 들어</div><div class="pp-card-back">masalan</div></div>
  <div class="pp-card"><div class="pp-card-front">비유하다</div><div class="pp-card-back">o'xshatmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">도구</div><div class="pp-card-back">asbob</div></div>
  <div class="pp-card"><div class="pp-card-front">주름을 펴다</div><div class="pp-card-back">g'ijimni yozmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">역할을 하다</div><div class="pp-card-back">vazifasini bajarmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">~(이)자</div><div class="pp-card-back">ham …, ham … (ikki vazifa)</div></div>
  <div class="pp-card"><div class="pp-card-front">스스로</div><div class="pp-card-back">o'zi, mustaqil</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>46 — shakl savoli: 예를 들어 / ~보다 / 먼저-그다음 / 연구에 따르면 belgilarini sanang.</li>
  <li>Variantdagi har bir fe'l (비유하고, 예를 들어) audiodagi o'z belgisiga ega bo'lishi shart.</li>
  <li>Ikki asbob/tushuncha yonma-yon kelsa — vazifalari almashtirilgan tuzoqni kuting.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 102) ──────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 다큐 3: To'liq amaliyot — sahro kemasi va so'z kuchi",
        "summary": "43–46 to'liq mashqi: tuya haqidagi hujjatli lavha (mazmun+sabab) va iltimos-buyruq taqqoslangan ma'ruza (mazmun+uslub).",
        "order":   102,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: 43–44 va 45–46 juftliklari</h2>
<p>Hujjatli lavhada 44-savolni oldindan o'qib, sabab jumlasini oving; ma'ruzada signal
so'zlarni sanang. Har juftlik — ikki eshitish.</p>
"""},
            {"rich_text": """
<p><strong>43-savol.</strong> 이 이야기의 중심 내용으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_102_1.mp3",
             "audio_script": [
                 ("남자", "사막의 낮은 뜨겁고 밤은 차갑다. 낙타는 이 극한의 땅에서 살아남도록 만들어진 동물이다. 등의 혹에는 물이 아니라 지방이 들어 있어 먹이가 없을 때 에너지로 쓴다. 또 낙타는 한 번에 물을 백 리터 넘게 마시고 이를 몸속에 저장한다. 물을 저장할 수 있기 때문에 낙타는 물 없이도 사막을 며칠씩 걸을 수 있다. 그래서 사람들은 낙타를 사막의 배라고 부른다."),
             ],
             "choices": [
                 {"text": "낙타는 사막에서 살아남기에 알맞은 몸을 가졌다. (Tuya sahroda omon qolishga mos tanaga ega.)", "is_correct": True},
                 {"text": "사막의 밤은 낮보다 뜨겁다. (Sahroda kecha kunduzdan issiqroq.)", "is_correct": False},
                 {"text": "낙타는 물을 전혀 마시지 않는다. (Tuya umuman suv ichmaydi.)", "is_correct": False},
                 {"text": "사막에서는 배로 이동해야 한다. (Sahroda kema bilan yurish kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Skelet: muhit (issiq-sovuq) → moslashuvlar (o'rkach, suv zaxirasi) → laqab (사막의 배).
Hammasini yopadigan soyabon: <mark style="background:#dcfce7;">sahroga mos tana</mark> ✅.
④ metaforani so'zma-so'z o'qigan tuzoq (사막의 <strong>배</strong> = "sahro kemasi" —
laqab!) — sarlavha darslaridan tanish xato. Metafora eshitsangiz: bu nom, fakt emas.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 사막의 낮은 뜨겁고 밤은 차갑다. 낙타는 이 극한의 땅에서 살아남도록
    만들어진 동물이다. 등의 혹에는 물이 아니라 지방이 들어 있어 먹이가 없을 때 에너지로 쓴다.
    또 낙타는 한 번에 물을 백 리터 넘게 마시고 이를 몸속에 저장한다. 물을 저장할 수 있기 때문에
    낙타는 물 없이도 사막을 며칠씩 걸을 수 있다. 그래서 사람들은 낙타를 사막의 배라고 부른다.<br>
    <em style="color:#475569;">Sahroning kunduzi issiq, kechasi sovuq. Tuya — mana shu ekstremal
    zaminda omon qolishga yaratilgan jonivor. O'rkachida suv emas, yog' bor — ozuqa yo'q paytda
    energiya sifatida ishlatadi. Yana tuya bir safarda yuz litrdan ortiq suv ichib, uni tanasida
    saqlaydi. Suvni zaxira qila olgani uchun tuya suvsiz ham sahroda bir necha kunlab yura oladi.
    Shuning uchun odamlar tuyani "sahro kemasi" deb atashadi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>44-savol.</strong> 낙타가 물 없이 사막을 걸을 수 있는 이유로 알맞은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "물을 몸속에 저장할 수 있어서 (Suvni tanasida zaxira qila olgani uchun)", "is_correct": True},
                 {"text": "혹에 물이 들어 있어서 (O'rkachida suv bo'lgani uchun)", "is_correct": False},
                 {"text": "밤에만 걸어 다녀서 (Faqat kechasi yurgani uchun)", "is_correct": False},
                 {"text": "사막에 비가 자주 와서 (Sahroda yomg'ir tez-tez yoqqani uchun)", "is_correct": False},
             ],
             "explanation": """
<p>Sabab jumlasi qolipda: 물을 저장할 수 있<strong>기 때문에</strong> → ✅ ①. ② — dunyodagi
eng mashhur noto'g'ri tasavvur, va matn uni ataylab inkor qildi: 혹에는 물이
<strong>아니라 지방</strong>이! O'z "bilimingiz" javob bilan to'qnashsa — har doim
<strong>matn g'olib</strong>. 44-savol ana shuni sinaydi.</p>
"""},
            {"rich_text": """
<p><strong>45-savol.</strong> 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_102_2.mp3",
             "audio_script": [
                 ("여자", "같은 뜻이라도 어떻게 말하느냐에 따라 결과는 전혀 달라집니다. \"문 닫아라\"와 \"문 좀 닫아 줄래요?\"를 비교해 보세요. 뜻은 같지만 듣는 사람의 기분은 전혀 다르지요. 명령하는 말은 상대의 마음을 닫게 하고, 부탁하는 말은 상대의 마음을 엽니다. 그래서 부탁하는 말은 명령하는 말보다 사람을 움직이는 힘이 훨씬 큽니다."),
             ],
             "choices": [
                 {"text": "부탁하는 말이 명령하는 말보다 힘이 크다. (Iltimos ohangidagi gap buyruqdan kuchliroq.)", "is_correct": True},
                 {"text": "명령하는 말이 사람을 더 잘 움직인다. (Buyruq ohangi odamni yaxshiroq harakatlantiradi.)", "is_correct": False},
                 {"text": "두 표현은 뜻이 서로 다르다. (Ikki ibora ma'nosi har xil.)", "is_correct": False},
                 {"text": "말은 결과에 영향을 주지 않는다. (Gapirish natijaga ta'sir qilmaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② teskari, ③ matnga zid (뜻은 <strong>같지만</strong>!), ④ birinchi jumlaga
zid (결과는 전혀 <strong>달라집니다</strong>). ✅ ①: 부탁하는 말은 ~보다 힘이 훨씬
큽니다 — aynan xulosa jumlasi. ~보다 taqqoslashlarida yo'nalishni almashtirib berish (A>B
ni B>A qilish) — eng arzon va eng ko'p ishlaydigan tuzoq.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 같은 뜻이라도 어떻게 말하느냐에 따라 결과는 전혀 달라집니다.
    "문 닫아라"와 "문 좀 닫아 줄래요?"를 비교해 보세요. 뜻은 같지만 듣는 사람의 기분은 전혀
    다르지요. 명령하는 말은 상대의 마음을 닫게 하고, 부탁하는 말은 상대의 마음을 엽니다.
    그래서 부탁하는 말은 명령하는 말보다 사람을 움직이는 힘이 훨씬 큽니다.<br>
    <em style="color:#475569;">Ma'no bir xil bo'lsa ham, qanday aytilishiga qarab natija butunlay
    o'zgaradi. "Eshikni yop!" bilan "Eshikni yopib bera olasizmi?"ni solishtiring. Ma'no bir,
    lekin eshituvchining kayfiyati butunlay boshqa. Buyruq ohangi suhbatdosh qalbini yopadi,
    iltimos ohangi esa ochadi. Shuning uchun iltimos gapning odamni harakatlantirish kuchi
    buyruqnikidan ancha katta.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>46-savol.</strong> 여자의 말하기 방식으로 가장 알맞은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "두 표현을 비교하며 자신의 주장을 펴고 있다. (Ikki iborani taqqoslab, o'z fikrini bayon qilmoqda.)", "is_correct": True},
                 {"text": "과정을 순서대로 설명하고 있다. (Jarayonni tartib bilan tushuntirmoqda.)", "is_correct": False},
                 {"text": "연구 결과의 숫자를 나열하고 있다. (Tadqiqot raqamlarini sanab o'tmoqda.)", "is_correct": False},
                 {"text": "다른 사람의 의견을 그대로 전달만 하고 있다. (Boshqaning fikrini shunchaki yetkazmoqda xolos.)", "is_correct": False},
             ],
             "explanation": """
<p>Belgilar hisobi: <strong>비교해 보세요</strong> (ochiq taqqoslash chaqirig'i!) + ikki
misol yonma-yon + ~<strong>보다</strong> 훨씬 큽니다 → taqqoslash + xulosa-da'vo → ✅ ①.
먼저/그다음 yo'q, raqam yo'q, iqtibos yo'q. Mavzu yakunlandi — endi eng qiyin blok
(47–50) qoldi, keyin esa katta final! 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">낙타</div><div class="pp-card-back">tuya</div></div>
  <div class="pp-card"><div class="pp-card-front">혹</div><div class="pp-card-back">o'rkach</div></div>
  <div class="pp-card"><div class="pp-card-front">지방</div><div class="pp-card-back">yog' (organizmda)</div></div>
  <div class="pp-card"><div class="pp-card-front">저장하다</div><div class="pp-card-back">zaxira qilmoq, saqlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">극한</div><div class="pp-card-back">ekstremal, chegaraviy</div></div>
  <div class="pp-card"><div class="pp-card-front">명령하다</div><div class="pp-card-back">buyurmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">비교하다</div><div class="pp-card-back">taqqoslamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">주장을 펴다</div><div class="pp-card-back">fikrini bayon qilmoq</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>44 (sabab): javob matnda ochiq (~기 때문에/위해서); o'z bilimingiz emas — matn g'olib.</li>
  <li>Metafora (사막의 배) — nom, fakt emas; so'zma-so'z o'qigan variant tuzoq.</li>
  <li>46 (uslub): belgilarni sanang — 비교해 보세요, 예를 들어, 먼저-그다음, ~에 따르면.</li>
</ul>
"""},
        ],
    },
]
