# TOPIK 말하기 (Speaking) — 3-savol: 그림 보고 이야기하기, lessons 1–3 (orders 30–32).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_speaking_q3_1_3.py \
#            --out examprep/management/commands/audio/speaking_q3
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_speaking_q3_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/speaking_q3

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "3-savol: Rasm hikoyasi (그림 보고 이야기하기)",
    "summary": "To'rt rasmdan hikoya aytish: o'tgan zamon, vaqt bog'lovchilari (그런데, 그래서, 결국) va his-tuyg'u jumlalarining skeleti.",
    "icon":    "bi-images",
    "order":   4,
}

# Panel card helper convention: each picture is shown as an emoji card with a Korean
# caption — the lessons describe the four panels this way (no image files needed).

LESSONS = [
    # ── Lesson 1 (order 30) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q3-1: Hikoya skeleti — kim, nima bo'ldi, oxiri nima",
        "summary": "3-topshiriq bilan tanishuv: 4 rasm = 4 jumla emas! Sahna → voqea → harakat → yakun+his skeleti va vaqt bog'lovchilari.",
        "order":   30,
        "blocks": [
            {"rich_text": """
<h2>🖼️ 3-topshiriq: to'rt rasm — bitta hikoya</h2>
<p>Ekranda <strong>to'rtta ketma-ket rasm</strong> chiqadi — kichik voqea: kimdir nimadir
qilmoqchi edi, nimadir yuz berdi, oxiri qandaydir tugadi. Vazifangiz — rasmlarni
<strong>hikoya</strong> qilib aytish. Eng katta xato: har rasmga bittadan quruq jumla
("erkak avtobusda. keyin yugurdi. keyin taksi. tamom") — bu ro'yxat, hikoya emas!</p>
<h3>Hikoya skeleti — 4 rasm, 4 vazifa</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p><strong>1-rasm = SAHNA.</strong> Qachon, kim, qayerda, nima qilmoqchi:
  어느 날 아침, 민수 씨는 회사에 가려고 버스를 기다리고 있었습니다.</p></div>
  <div class="pp-step"><p><strong>2-rasm = MUAMMO.</strong> 그런데 (lekin/shunda) bilan kirib keladi:
  그런데 갑자기 비가 오기 시작했습니다.</p></div>
  <div class="pp-step"><p><strong>3-rasm = HARAKAT.</strong> 그래서 (shuning uchun) bilan:
  그래서 민수 씨는 편의점으로 뛰어가서 우산을 샀습니다.</p></div>
  <div class="pp-step"><p><strong>4-rasm = YAKUN + HIS.</strong> 결국/다행히 + his-tuyg'u jumlasi:
  다행히 회사에 늦지 않게 도착해서 기분이 좋았습니다.</p></div>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Uch oltin qoida:</strong> ① hammasi <strong>o'tgan zamonda</strong> (-았/었습니다);
  ② qahramonga <strong>ism bering</strong> (민수 씨, 수미 씨) — "erkak/ayol" deyish quruq;
  ③ har rasmga kamida <strong>2 jumla</strong>: harakat + detal yoki his.
</div>
"""},
            {"rich_text": """
<h3>Namuna: to'rt panel</h3>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;">
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">⏰😴</div><p style="margin:6px 0 0;font-size:.85em;"><strong>①</strong> 늦잠을 잤어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🏃💨</div><p style="margin:6px 0 0;font-size:.85em;"><strong>②</strong> 버스 정류장으로 뛰어갔어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🚌😢</div><p style="margin:6px 0 0;font-size:.85em;"><strong>③</strong> 버스가 떠났어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🚕⏱️</div><p style="margin:6px 0 0;font-size:.85em;"><strong>④</strong> 택시를 타고 도착했어요</p>
  </div>
</div>
<p>Endi shu to'rt panelning <strong>hikoya</strong> shaklini eshiting — skelet qanday
ishlayotganini kuzating:</p>
""",
             "audio": "topik_s_030_1.mp3",
             "audio_script": [
                 ("남자", "어느 날 아침, 민수 씨는 늦잠을 잤습니다. 눈을 떠 보니 벌써 여덟 시 반이었습니다. 민수 씨는 세수도 못 하고 버스 정류장으로 뛰어갔습니다. 그런데 정류장에 도착했을 때 버스가 막 떠나고 있었습니다. 민수 씨는 너무 속상했습니다. 그래서 할 수 없이 택시를 탔습니다. 다행히 길이 막히지 않아서 학교에 늦지 않게 도착했습니다. 민수 씨는 오늘부터 일찍 자기로 결심했습니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — avval o'zingiz aytib ko'ring!</summary>
  <div style="margin-top:10px;">
    <p><strong>어느 날 아침, 민수 씨는 늦잠을 잤습니다. 눈을 떠 보니 벌써 여덟 시 반이었습니다.</strong> <span style="background:#dbeafe;padding:1px 8px;border-radius:999px;font-size:.8em;">① SAHNA</span><br>
    <em style="color:#475569;">Bir kuni ertalab Minsu uxlab qolibdi. Ko'zini ochsa — allaqachon sakkiz yarim.</em></p>
    <p><strong>민수 씨는 세수도 못 하고 버스 정류장으로 뛰어갔습니다.</strong> <span style="background:#dbeafe;padding:1px 8px;border-radius:999px;font-size:.8em;">② HARAKAT</span><br>
    <em style="color:#475569;">Minsu yuz ham yuvolmasdan bekat tomon yugurdi.</em></p>
    <p><strong>그런데 정류장에 도착했을 때 버스가 막 떠나고 있었습니다. 민수 씨는 너무 속상했습니다.</strong> <span style="background:#fee2e2;padding:1px 8px;border-radius:999px;font-size:.8em;">③ MUAMMO+HIS</span><br>
    <em style="color:#475569;">Lekin bekatga yetganida avtobus endigina jo'nab ketayotgan edi. Minsu juda xafa bo'ldi.</em></p>
    <p><strong>그래서 할 수 없이 택시를 탔습니다. 다행히 ... 늦지 않게 도착했습니다. 오늘부터 일찍 자기로 결심했습니다.</strong> <span style="background:#dcfce7;padding:1px 8px;border-radius:999px;font-size:.8em;">④ YAKUN+XULOSA</span><br>
    <em style="color:#475569;">Shuning uchun noiloj taksiga o'tirdi. Xayriyat, yo'l tiqilmagan ekan — kechikmasdan yetib bordi. Va bugundan erta yotishga qaror qildi.</em></p>
  </div>
</details>
<p>Sanang: 8 jumla, hammasi o'tgan zamonda, uchta bog'lovchi (그런데, 그래서, 다행히),
ikkita his (속상했습니다, 결심했습니다). Bu — 3-topshiriqning to'liq bali.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 4 rasmli hikoyada 그런데 bog'lovchisining vazifasi nima?</p>
""",
             "choices": [
                 {"text": "Muammo/burilishni kiritish (2–3-rasm)", "is_correct": True},
                 {"text": "Hikoyani boshlash", "is_correct": False},
                 {"text": "Xulosa chiqarish", "is_correct": False},
                 {"text": "Sabab ko'rsatish", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: 그런데 = "lekin/shu payt" — rejadagi ish buzilgan joyda keladi. Boshlash — 어느 날,
xulosa — 결국/다행히, sabab — 그래서. To'rt bog'lovchi to'rt vazifa: ularni almashtirmang.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> Qaysi hikoya boshlanishi eng yaxshi?</p>
""",
             "choices": [
                 {"text": "어느 날 아침, 수미 씨는 공원에서 운동을 하고 있었습니다.", "is_correct": True},
                 {"text": "여자가 있습니다. 공원입니다.", "is_correct": False},
                 {"text": "이 그림에는 공원이 보입니다.", "is_correct": False},
                 {"text": "운동은 건강에 좋습니다.", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: qachon (어느 날 아침) + kim (수미 씨 — ismli!) + qayerda (공원) + nima (운동) —
bitta jumlada to'liq sahna. ② quruq ro'yxat, ③ rasmni tasvirlash (hikoya emas!),
④ umumiy gap — hikoyaga aloqasi yo'q.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">어느 날</div><div class="pp-card-back">bir kuni</div></div>
  <div class="pp-card"><div class="pp-card-front">늦잠을 자다</div><div class="pp-card-back">uxlab qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">눈을 떠 보니</div><div class="pp-card-back">ko'zini ochsa</div></div>
  <div class="pp-card"><div class="pp-card-front">막 떠나다</div><div class="pp-card-back">endigina jo'nab ketmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">속상하다</div><div class="pp-card-back">xafa bo'lmoq, ichi achimoq</div></div>
  <div class="pp-card"><div class="pp-card-front">할 수 없이</div><div class="pp-card-back">noiloj</div></div>
  <div class="pp-card"><div class="pp-card-front">-지 않게</div><div class="pp-card-back">...may (kechikmay)</div></div>
  <div class="pp-card"><div class="pp-card-front">-기로 결심하다</div><div class="pp-card-back">...ishga qaror qilmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>4 rasm = sahna → muammo (그런데) → harakat (그래서) → yakun+his (결국/다행히).</li>
  <li>O'tgan zamon, ismli qahramon, har rasmga 2 jumla.</li>
  <li>His jumlalari (속상했습니다, 기뻤습니다) — hikoyani tiriltiradigan ziravor.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 31) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q3-2: Ziravorlar banki — vaqt, his va jonli detal",
        "summary": "Hikoyani boyitadigan g'ishtlar: vaqt iboralari, his-tuyg'u lug'ati, '-려고 했는데' qolipi va ikkinchi to'liq namuna.",
        "order":   31,
        "blocks": [
            {"rich_text": """
<h2>🧂 Oddiy hikoyani baland balga aylantiradigan ziravorlar</h2>
<p>Skeletni bilasiz. Endi uni <strong>boyitamiz</strong> — baholovchining "til boyligi"
katagiga to'g'ri tegadigan uch guruh g'isht:</p>
<h3>① Vaqt iboralari (hikoyaning yelimi)</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>어느 날 / 지난 주말에</strong> — bir kuni / o'tgan dam olishda (ochilish)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>-(으)려고 했는데</strong> — ...moqchi edi-yu (reja + buzilish, bitta qolipda!)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>-았/었을 때 / 그때</strong> — ...ganda / o'sha payt</p>
  <p style="font-size:1.05em;margin:0;"><strong>잠시 후 / 결국 / 마지막으로</strong> — birozdan keyin / oxir-oqibat / nihoyat</p>
</div>
<h3>② His-tuyg'u lug'ati (4-rasmning yuragi)</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>당황했습니다</strong> — sarosimaga tushdi &nbsp;|&nbsp; <strong>속상했습니다</strong> — xafa bo'ldi</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>걱정이 되었습니다</strong> — xavotir bosdi &nbsp;|&nbsp; <strong>안심했습니다</strong> — ko'ngli joyiga tushdi</p>
  <p style="font-size:1.05em;margin:0;"><strong>뿌듯했습니다</strong> — faxrlandi &nbsp;|&nbsp; <strong>고마운 마음이 들었습니다</strong> — minnatdor bo'ldi</p>
</div>
<h3>③ Jonli detal (Q1 dagi "bonus"ning hikoya shakli)</h3>
<p>Raqam yoki kichik aniqlik qo'shing: 버스 → <strong>마을버스</strong>, 우산 → <strong>파란색
우산</strong>, 늦었다 → <strong>십 분이나 늦었다</strong>. Bitta detal — bitta tabassum baholovchidan.</p>
"""},
            {"rich_text": """
<h3>Ikkinchi namuna: yomg'ir va mehribon notanish</h3>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;">
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🏞️🚶‍♀️</div><p style="margin:6px 0 0;font-size:.85em;"><strong>①</strong> 수미 씨가 산책하러 나갔어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🌧️😨</div><p style="margin:6px 0 0;font-size:.85em;"><strong>②</strong> 갑자기 비가 왔어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">☂️🤝</div><p style="margin:6px 0 0;font-size:.85em;"><strong>③</strong> 할머니가 우산을 씌워 줬어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🏠😊</div><p style="margin:6px 0 0;font-size:.85em;"><strong>④</strong> 같이 이야기하며 집에 갔어요</p>
  </div>
</div>
""",
             "audio": "topik_s_031_1.mp3",
             "audio_script": [
                 ("남자", "지난 주말 오후, 수미 씨는 기분 전환을 하려고 공원에 산책하러 나갔습니다. 그런데 삼십 분쯤 걸었을 때 갑자기 하늘이 어두워지더니 비가 쏟아지기 시작했습니다. 우산이 없어서 수미 씨는 정말 당황했습니다. 그때 지나가던 할머니가 웃으면서 파란색 우산을 씌워 주셨습니다. 수미 씨는 너무 고마운 마음이 들었습니다. 두 사람은 우산을 같이 쓰고 이야기를 하면서 집까지 걸어갔습니다. 수미 씨는 다음에 꼭 할머니께 따뜻한 차를 대접하기로 결심했습니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>지난 주말 오후, 수미 씨는 기분 전환을 하려고 공원에 산책하러 나갔습니다.</strong><br><em style="color:#475569;">O'tgan dam olish kuni tushdan keyin Sumi kayfiyatini yozish uchun bog'ga sayrga chiqdi.</em></p>
    <p><strong>그런데 삼십 분쯤 걸었을 때 갑자기 하늘이 어두워지더니 비가 쏟아지기 시작했습니다.</strong><br><em style="color:#475569;">Lekin o'ttiz daqiqacha yurganida to'satdan osmon qorayib, yomg'ir quyib yubordi.</em></p>
    <p><strong>우산이 없어서 수미 씨는 정말 당황했습니다. 그때 지나가던 할머니가 웃으면서 파란색 우산을 씌워 주셨습니다.</strong><br><em style="color:#475569;">Soyaboni yo'q Sumi rosa sarosimaga tushdi. Shu payt o'tib ketayotgan buvi jilmayib, ko'k soyabonini tutib qoldi.</em></p>
    <p><strong>두 사람은 우산을 같이 쓰고 이야기를 하면서 집까지 걸어갔습니다. ... 따뜻한 차를 대접하기로 결심했습니다.</strong><br><em style="color:#475569;">Ikkovlon bitta soyabon ostida suhbatlashib uygacha yurishdi. Sumi keyingi safar buviga albatta iliq choy tutishga qaror qildi.</em></p>
  </div>
</details>
<p>Ziravorlarni toping: <strong>-(으)려고</strong> (reja), <strong>-았을 때</strong> +
<strong>갑자기</strong> (burilish), <strong>당황했습니다 → 고마운 마음</strong> (his almashinuvi!),
<strong>파란색</strong> uzun detali, <strong>-기로 결심했습니다</strong> yakuni.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> "-(으)려고 했는데" qolipi hikoyada nima uchun oltin?</p>
""",
             "choices": [
                 {"text": "Bitta qolipda reja VA buzilishni beradi — 1–2-rasmni bir jumlaga bog'laydi", "is_correct": True},
                 {"text": "Eng uzun grammatika bo'lgani uchun", "is_correct": False},
                 {"text": "Kelasi zamonni bildirgani uchun", "is_correct": False},
                 {"text": "Faqat 4-rasmda ishlatilgani uchun", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: 영화를 보려고 했는데 표가 없었습니다 — "ko'rmoqchi edi-yu, chipta yo'q edi": reja
(1-rasm) + muammo (2-rasm) bitta oqimda. 3-topshiriq hikoyalarining eng ko'p ishlatiladigan
ochilish quroli.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> Namunada Sumining hissi qanday almashdi?</p>
""",
             "choices": [
                 {"text": "당황 (sarosima) → 고마움 (minnatdorlik)", "is_correct": True},
                 {"text": "기쁨 (quvonch) → 슬픔 (qayg'u)", "is_correct": False},
                 {"text": "His umuman aytilmagan", "is_correct": False},
                 {"text": "속상함 (xafalik) → 화남 (jahl)", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: yomg'irda 당황했습니다, buvining soyabonidan keyin 고마운 마음이 들었습니다. His
almashinuvi (yomon → yaxshi) — 4 rasmli hikoyalarning eng tabiiy egri chizig'i: uni har
hikoyangizga soling.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">기분 전환</div><div class="pp-card-back">kayfiyatni yozish</div></div>
  <div class="pp-card"><div class="pp-card-front">비가 쏟아지다</div><div class="pp-card-back">yomg'ir quymoq</div></div>
  <div class="pp-card"><div class="pp-card-front">당황하다</div><div class="pp-card-back">sarosimaga tushmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">우산을 씌워 주다</div><div class="pp-card-back">soyabon tutib turmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">안심하다</div><div class="pp-card-back">ko'ngli joyiga tushmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">뿌듯하다</div><div class="pp-card-back">faxrlanmoq, ko'ngli to'lmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">대접하다</div><div class="pp-card-back">mehmon qilmoq, tutmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)려고 했는데</div><div class="pp-card-back">...moqchi edi-yu (reja+buzilish)</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Ziravor uch guruh: vaqt iboralari · his lug'ati · jonli detal (rang, raqam).</li>
  <li>-(으)려고 했는데 — reja va muammoni bitta jumlada beradigan oltin qolip.</li>
  <li>His egri chizig'i: yomon his → yaxshi his (yoki aksincha) — hikoyaning yuragi.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 32) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q3-3: To'liq amaliyot — ikki hikoya imtihon ritmida",
        "summary": "Ikki 4-panelli vaziyat: yo'qolgan kuchukcha va tug'ilgan kun sovg'asi — o'zingiz aytasiz, keyin namuna bilan solishtirasiz.",
        "order":   32,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: endi hikoyachi sizsiz</h2>
<p>Ikki hikoya. Tartib: panellarni o'qing → 60–90 soniya reja (skelet kataklarini
to'ldiring: sahna? muammo? harakat? yakun+his?) → telefonga yozib 1,5 daqiqa gapiring →
namunani eshitib soya qiling.</p>
<h3>1-hikoya: panellar</h3>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;">
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🏞️🐶</div><p style="margin:6px 0 0;font-size:.85em;"><strong>①</strong> 공원에서 강아지를 발견했어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🏷️📞</div><p style="margin:6px 0 0;font-size:.85em;"><strong>②</strong> 목걸이의 전화번호로 전화했어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🏃‍♀️😭</div><p style="margin:6px 0 0;font-size:.85em;"><strong>③</strong> 주인이 울면서 뛰어왔어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🍞🙏</div><p style="margin:6px 0 0;font-size:.85em;"><strong>④</strong> 주인이 빵을 선물했어요</p>
  </div>
</div>
<p>Avval o'zingiz gapiring! Keyin namuna:</p>
""",
             "audio": "topik_s_032_1.mp3",
             "audio_script": [
                 ("남자", "어느 날 저녁, 지훈 씨는 공원에서 운동을 하다가 혼자 돌아다니는 작은 강아지를 발견했습니다. 강아지는 배가 고픈지 계속 지훈 씨를 따라왔습니다. 지훈 씨는 강아지의 목걸이에 있는 전화번호를 보고 바로 전화를 걸었습니다. 잠시 후 주인 아주머니가 울면서 뛰어왔습니다. 아주머니는 강아지를 안고 몇 번이나 고맙다고 말했습니다. 다음 날 아주머니는 지훈 씨에게 직접 만든 빵을 선물해 주셨습니다. 지훈 씨는 작은 도움이 이렇게 큰 기쁨이 될 수 있다는 것을 알고 마음이 뿌듯했습니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>어느 날 저녁, 지훈 씨는 공원에서 운동을 하다가 혼자 돌아다니는 작은 강아지를 발견했습니다.</strong><br><em style="color:#475569;">Bir kuni kechqurun Jihun bog'da shug'ullanayotib, yolg'iz izg'ib yurgan kichkina kuchukchani ko'rib qoldi.</em></p>
    <p><strong>지훈 씨는 강아지의 목걸이에 있는 전화번호를 보고 바로 전화를 걸었습니다.</strong><br><em style="color:#475569;">Jihun kuchukcha bo'yinbog'idagi telefon raqamini ko'rib, darhol qo'ng'iroq qildi.</em></p>
    <p><strong>잠시 후 주인 아주머니가 울면서 뛰어왔습니다. 아주머니는 강아지를 안고 몇 번이나 고맙다고 말했습니다.</strong><br><em style="color:#475569;">Birozdan keyin egasi — bir ayol yig'lab yugurib keldi. U kuchukchani quchoqlab, qayta-qayta rahmat aytdi.</em></p>
    <p><strong>지훈 씨는 작은 도움이 이렇게 큰 기쁨이 될 수 있다는 것을 알고 마음이 뿌듯했습니다.</strong><br><em style="color:#475569;">Jihun kichik yordam shunchalik katta quvonch bo'lishi mumkinligini bilib, ko'ngli faxrga to'ldi.</em></p>
  </div>
</details>
<h3>2-hikoya: panellar</h3>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;">
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🎂💡</div><p style="margin:6px 0 0;font-size:.85em;"><strong>①</strong> 엄마 생신 선물을 준비하기로 했어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">💰😟</div><p style="margin:6px 0 0;font-size:.85em;"><strong>②</strong> 돈이 부족했어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">👩‍🍳💌</div><p style="margin:6px 0 0;font-size:.85em;"><strong>③</strong> 직접 미역국을 끓이고 편지를 썼어요</p>
  </div>
  <div style="flex:1 1 150px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:12px;text-align:center;">
    <div style="font-size:2em;">🥲❤️</div><p style="margin:6px 0 0;font-size:.85em;"><strong>④</strong> 엄마가 감동해서 눈물을 흘렸어요</p>
  </div>
</div>
<p>Yana avval o'zingiz! Keyin namuna:</p>
""",
             "audio": "topik_s_032_2.mp3",
             "audio_script": [
                 ("남자", "다음 주가 엄마 생신이라서 수진 씨는 특별한 선물을 준비하려고 했습니다. 그런데 지갑을 열어 보니 돈이 오천 원밖에 없었습니다. 수진 씨는 잠시 고민하다가 좋은 생각이 떠올랐습니다. 생신 날 아침, 수진 씨는 일찍 일어나서 직접 미역국을 끓이고 마음을 담은 편지를 썼습니다. 엄마는 미역국을 드시고 편지를 읽으시더니 눈물을 흘리셨습니다. 그리고 이렇게 말씀하셨습니다. 세상에서 제일 좋은 선물이라고요. 수진 씨는 선물은 가격이 아니라 마음이라는 것을 깨달았습니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>다음 주가 엄마 생신이라서 수진 씨는 특별한 선물을 준비하려고 했습니다.</strong><br><em style="color:#475569;">Kelasi hafta onasining tug'ilgan kuni bo'lgani uchun Sujin alohida sovg'a tayyorlamoqchi edi.</em></p>
    <p><strong>그런데 지갑을 열어 보니 돈이 오천 원밖에 없었습니다.</strong><br><em style="color:#475569;">Lekin hamyonini ochsa — bor-yo'g'i besh ming von.</em></p>
    <p><strong>생신 날 아침, 수진 씨는 일찍 일어나서 직접 미역국을 끓이고 마음을 담은 편지를 썼습니다.</strong><br><em style="color:#475569;">Tug'ilgan kun tongida Sujin erta turib, o'z qo'li bilan miyokkuk (dengiz karami sho'rvasi) pishirdi va mehr to'la xat yozdi.</em></p>
    <p><strong>수진 씨는 선물은 가격이 아니라 마음이라는 것을 깨달았습니다.</strong><br><em style="color:#475569;">Sujin sovg'aning qadri narxida emas, mehrda ekanini angladi.</em></p>
  </div>
</details>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Yakun jumlasining siri:</strong> ikkala namuna ham <strong>kichik hikmat</strong>
  bilan tugadi (도움 → 기쁨; 가격 → 마음). "A가 아니라 B라는 것을 깨달았습니다" qolipi —
  4-rasmning eng baland yakuni. O'qish darslaridan tanish qolip — endi og'zingizda!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot.</strong> O'z yozuvingizni tekshiring: Q3 uchun BESH nazorat savoli qaysi qatorda?</p>
""",
             "choices": [
                 {"text": "O'tgan zamonmi? Ism berdimmi? 그런데/그래서 bormi? His aytdimmi? Yakun hikmatlimi?", "is_correct": True},
                 {"text": "Rasm nechta? Rang nechta? Ovoz balandmi? Tez gapirdimmi? Kuldimmi?", "is_correct": False},
                 {"text": "Necha so'z? Necha jumla? Necha daqiqa? Necha xato? Necha ball?", "is_correct": False},
                 {"text": "Hikoya rostmi? Qahramon kimning tanishi? Qaysi shahar? Pul qancha? Ob-havo qanday?", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: beshta katak — skelet (zamon, ism, bog'lovchilar) + jon (his, hikmat). Har
yozuvingizni shu beshlik bilan o'zingiz baholang. Q3 tayyor: endi sizda hikoyachi
darajasi bor — keyingi bekat: dialog yakunlash (Q4)! 🎬</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">발견하다</div><div class="pp-card-back">topib olmoq, ko'rib qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">목걸이</div><div class="pp-card-back">bo'yinbog', marjon</div></div>
  <div class="pp-card"><div class="pp-card-front">전화를 걸다</div><div class="pp-card-back">qo'ng'iroq qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">몇 번이나</div><div class="pp-card-back">qayta-qayta, necha marta</div></div>
  <div class="pp-card"><div class="pp-card-front">생신</div><div class="pp-card-back">tug'ilgan kun (hurmat)</div></div>
  <div class="pp-card"><div class="pp-card-front">미역국을 끓이다</div><div class="pp-card-back">miyokkuk pishirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">눈물을 흘리다</div><div class="pp-card-back">ko'z yoshi to'kmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">깨닫다</div><div class="pp-card-back">anglamoq</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Skelet + ziravor + hikmatli yakun = to'liq ball hikoyasi.</li>
  <li>"A가 아니라 B라는 것을 깨달았습니다" — 4-rasmning eng kuchli yopilishi.</li>
  <li>Besh nazorat: zamon · ism · bog'lovchi · his · hikmat.</li>
</ul>
"""},
        ],
    },
]
