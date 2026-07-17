# TOPIK 말하기 (Speaking) — 1-savol: 질문에 대답하기, lessons 1–3 (orders 10–12).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_speaking_q1_1_3.py \
#            --out examprep/management/commands/audio/speaking_q1
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_speaking_q1_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/speaking_q1

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "1-savol: Savolga javob (질문에 대답하기)",
    "summary": "Kundalik mavzudagi shaxsiy savolga javob: 3 jumlalik formula (javob → sabab → misol) va soya qilinadigan namunaviy javoblar.",
    "icon":    "bi-chat-left-text",
    "order":   2,
}

LESSONS = [
    # ── Lesson 1 (order 10) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q1-1: 3 jumla formulasi — javob, sabab, misol",
        "summary": "1-topshiriq bilan tanishuv: oddiy shaxsiy savolga bo'sh qolmasdan, tartibli 3–4 jumla bilan javob berish formulasi.",
        "order":   10,
        "blocks": [
            {"rich_text": """
<h2>💬 1-topshiriq: eng oson, lekin eng muhim</h2>
<p>Birinchi topshiriqda kompyuter sizga <strong>kundalik shaxsiy savol</strong> beradi:
sevimli mashg'ulotingiz, dam olish kuningiz, oilangiz, ob-havo... Savol boshlang'ich
darajada, LEKIN bu topshiriq imtihonning <strong>birinchi taassurotu</strong>: shu yerda
ravon boshlasangiz, hayajon qolganiga ham tarqaydi.</p>
<p>Eng katta xavf — javob juda qisqa chiqishi: "네, 좋아합니다." <em>(Ha, yaxshi ko'raman.)</em>
— va sukut... Vaqt esa hali bor! Buning davosi — <strong>3 jumla formulasi</strong>:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>1️⃣ JAVOB</strong> — savolga to'g'ridan-to'g'ri: 제 취미는 축구입니다.</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>2️⃣ SABAB</strong> — nega? (-아/어서, -기 때문에): 축구를 하면 스트레스가 풀리기 때문입니다.</p>
  <p style="font-size:1.05em;margin:0;"><strong>3️⃣ MISOL/REJA</strong> — aniq detal yoki kelajak: 주말마다 친구들과 공원에서 축구를 합니다.</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Formula HAR QANDAY shaxsiy savolga tushadi: sevimli taom?
  javob+sabab+misol. Dam olish kuni? javob+sabab+misol. Tayyorlanish vaqtida uch
  katakchani xayolan to'ldiring: <strong>nima? — nega? — masalan?</strong>
</div>
"""},
            {"rich_text": """
<h3>🎧 Imtihondagidek: savolni eshiting</h3>
<p>Avval savol audiosi (imtihonda ham ayol ovozida o'qiladi). Eshitgach, pauza qilib
o'zingiz javob berib ko'ring — keyin namunani oching:</p>
""",
             "audio": "topik_s_010_1.mp3",
             "audio_script": [
                 ("여자", "취미가 무엇입니까? 그 취미를 왜 좋아합니까? 이야기해 보세요."),
             ]},
            {"rich_text": """
<p><strong>Namunaviy javob</strong> — 3 jumla formulasi ishda. Soya qilish uchun eshiting:</p>
""",
             "audio": "topik_s_010_2.mp3",
             "audio_script": [
                 ("남자", "제 취미는 축구입니다. 축구를 하면 스트레스가 풀리고 기분이 좋아지기 때문에 좋아합니다. 그래서 주말마다 친구들과 공원에서 축구를 합니다. 축구를 한 후에 같이 먹는 밥은 정말 맛있습니다."),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — avval o'zingiz aytib ko'ring!</summary>
  <div style="margin-top:10px;">
    <p><strong>제 취미는 축구입니다.</strong> <span style="background:#dbeafe;padding:1px 8px;border-radius:999px;font-size:.8em;">JAVOB</span><br>
    <em style="color:#475569;">Mening sevimli mashg'ulotim — futbol.</em></p>
    <p><strong>축구를 하면 스트레스가 풀리고 기분이 좋아지기 때문에 좋아합니다.</strong> <span style="background:#dcfce7;padding:1px 8px;border-radius:999px;font-size:.8em;">SABAB</span><br>
    <em style="color:#475569;">Futbol o'ynasam, stress tarqaladi va kayfiyatim ko'tariladi — shuning uchun yaxshi ko'raman.</em></p>
    <p><strong>그래서 주말마다 친구들과 공원에서 축구를 합니다.</strong> <span style="background:#fef3c7;padding:1px 8px;border-radius:999px;font-size:.8em;">MISOL</span><br>
    <em style="color:#475569;">Shuning uchun har dam olish kuni do'stlarim bilan bog'da futbol o'ynayman.</em></p>
    <p><strong>축구를 한 후에 같이 먹는 밥은 정말 맛있습니다.</strong> <span style="background:#fae8ff;padding:1px 8px;border-radius:999px;font-size:.8em;">BONUS detal</span><br>
    <em style="color:#475569;">Futboldan keyin birga yeyiladigan ovqat juda mazali bo'ladi.</em></p>
  </div>
</details>
<p>To'rtinchi "bonus" jumlaga e'tibor bering — kichik <strong>jonli detal</strong> javobni
yodlangan matndan tirik hikoyaga aylantiradi. Baholovchilar buni juda yaxshi ko'radi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> "주말에 보통 무엇을 합니까?" savoliga qaysi javob formulaga mos?</p>
""",
             "choices": [
                 {"text": "주말에 보통 등산을 합니다. 산에 가면 공기가 맑아서 기분이 좋아지기 때문입니다. 지난주에도 친구와 남산에 갔습니다.", "is_correct": True},
                 {"text": "네, 주말을 좋아합니다.", "is_correct": False},
                 {"text": "등산, 수영, 독서, 요리, 게임, 쇼핑을 합니다.", "is_correct": False},
                 {"text": "주말은 토요일과 일요일입니다.", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: javob (등산) + sabab (공기가 맑아서... 때문입니다) + misol (지난주에 남산). ② savolga
javob emas + juda qisqa; ③ ro'yxat — sabab ham, misol ham yo'q (ro'yxat sanash ball
bermaydi!); ④ savolni tushunmaganlik. Formula: <strong>nima → nega → masalan</strong>.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">취미</div><div class="pp-card-back">sevimli mashg'ulot</div></div>
  <div class="pp-card"><div class="pp-card-front">스트레스가 풀리다</div><div class="pp-card-back">stress tarqalmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">기분이 좋아지다</div><div class="pp-card-back">kayfiyat ko'tarilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">-기 때문에</div><div class="pp-card-back">... sababli, ... uchun</div></div>
  <div class="pp-card"><div class="pp-card-front">주말마다</div><div class="pp-card-back">har dam olish kuni</div></div>
  <div class="pp-card"><div class="pp-card-front">그래서</div><div class="pp-card-back">shuning uchun</div></div>
  <div class="pp-card"><div class="pp-card-front">공기가 맑다</div><div class="pp-card-back">havo toza</div></div>
  <div class="pp-card"><div class="pp-card-front">이야기해 보세요</div><div class="pp-card-back">gapirib bering (savol qolipida)</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>1-topshiriq — birinchi taassurot: ravon boshlang, hayajonni yenging.</li>
  <li>Formula: <strong>JAVOB → SABAB → MISOL</strong> (+ jonli bonus detal).</li>
  <li>Tayyorlanish vaqtida uch katakni to'ldiring: nima? nega? masalan?</li>
  <li>Namunani bugundan 3 kun soya qiling.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 11) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q1-2: Mavzu banki — to'rt tayyor javob",
        "summary": "Eng ko'p so'raladigan mavzular bo'yicha soya qilinadigan namunaviy javoblar: sevimli taom, fasl, do'st, o'rganayotgan til.",
        "order":   11,
        "blocks": [
            {"rich_text": """
<h2>🗂️ Mavzu banki: imtihon nimani so'raydi?</h2>
<p>1-topshiriq savollari deyarli doim shu doiradan keladi: <strong>kundalik hayot</strong>
(dam olish, ovqat, ob-havo/fasl), <strong>atrofingizdagi odamlar</strong> (oila, do'st),
<strong>o'zingiz</strong> (mashg'ulot, o'qish, reja). Quyida to'rt mavzuning namunaviy
javoblari — har biri 3 jumla formulasida. Hammasini soya qiling: imtihonda savol
qaysi mavzudan kelsa ham, og'zingizda tayyor g'ishtlar bo'ladi.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Maqsad — javoblarni so'zma-so'z aytish EMAS! G'ishtlarni
  o'zingizga moslang: 축구 → sizniki 태권도 bo'lsin, 겨울 → 여름. Qolip qoladi, mazmun sizniki.
</div>
"""},
            {"rich_text": """
<h3>🎧 Mavzu 1: Sevimli taom (좋아하는 음식)</h3>
""",
             "audio": "topik_s_011_1.mp3",
             "audio_script": [
                 ("여자", "무슨 음식을 좋아합니까? 왜 그 음식을 좋아합니까?"),
                 ("남자", "저는 삼계탕을 제일 좋아합니다. 맛도 좋고 건강에도 좋기 때문입니다. 여름에 삼계탕을 먹으면 힘이 나서 더위를 이길 수 있습니다. 우즈베키스탄에 돌아가면 가족에게도 만들어 주고 싶습니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>저는 삼계탕을 제일 좋아합니다.</strong><br><em style="color:#475569;">Men samgyetangni (tovuq sho'rva) eng yaxshi ko'raman.</em></p>
    <p><strong>맛도 좋고 건강에도 좋기 때문입니다.</strong><br><em style="color:#475569;">Chunki mazasi ham yaxshi, sog'liqqa ham foydali.</em></p>
    <p><strong>여름에 삼계탕을 먹으면 힘이 나서 더위를 이길 수 있습니다.</strong><br><em style="color:#475569;">Yozda samgyetang yesangiz, kuch kirib, issiqni yengish mumkin.</em></p>
    <p><strong>우즈베키스탄에 돌아가면 가족에게도 만들어 주고 싶습니다.</strong><br><em style="color:#475569;">O'zbekistonga qaytsam, oilamga ham pishirib bermoqchiman.</em></p>
  </div>
</details>
<h3>🎧 Mavzu 2: Sevimli fasl (좋아하는 계절)</h3>
""",
             "audio": "topik_s_011_2.mp3",
             "audio_script": [
                 ("여자", "어느 계절을 가장 좋아합니까? 그 계절에 보통 무엇을 합니까?"),
                 ("남자", "저는 봄을 가장 좋아합니다. 날씨가 따뜻하고 꽃이 많이 피기 때문입니다. 봄이 되면 가족과 함께 공원으로 소풍을 갑니다. 작년 봄에는 벚꽃 사진을 백 장이나 찍었습니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>저는 봄을 가장 좋아합니다.</strong><br><em style="color:#475569;">Men bahorni eng yaxshi ko'raman.</em></p>
    <p><strong>날씨가 따뜻하고 꽃이 많이 피기 때문입니다.</strong><br><em style="color:#475569;">Chunki havo iliq va gullar ko'p ochiladi.</em></p>
    <p><strong>봄이 되면 가족과 함께 공원으로 소풍을 갑니다.</strong><br><em style="color:#475569;">Bahor kelsa, oilam bilan bog'ga sayilga boramiz.</em></p>
    <p><strong>작년 봄에는 벚꽃 사진을 백 장이나 찍었습니다.</strong><br><em style="color:#475569;">O'tgan yil bahorda gilos guli suratini naq yuzta oldim.</em></p>
  </div>
</details>
<h3>🎧 Mavzu 3: Yaqin do'st (친한 친구)</h3>
""",
             "audio": "topik_s_011_3.mp3",
             "audio_script": [
                 ("여자", "친한 친구를 소개해 보세요. 그 친구와 무엇을 자주 합니까?"),
                 ("남자", "제 친한 친구는 밀라입니다. 고등학교 때 처음 만났는데 벌써 오 년이 되었습니다. 밀라는 성격이 밝아서 같이 있으면 저도 즐거워집니다. 우리는 주말마다 같이 한국 영화를 보면서 한국어 공부도 합니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>제 친한 친구는 밀라입니다. 고등학교 때 처음 만났는데 벌써 오 년이 되었습니다.</strong><br><em style="color:#475569;">Yaqin do'stim — Mila. Litseyda birinchi marta uchrashganmiz, mana besh yil bo'libdi.</em></p>
    <p><strong>밀라는 성격이 밝아서 같이 있으면 저도 즐거워집니다.</strong><br><em style="color:#475569;">Milaning fe'li ochiq — birga bo'lsam, men ham quvnab ketaman.</em></p>
    <p><strong>우리는 주말마다 같이 한국 영화를 보면서 한국어 공부도 합니다.</strong><br><em style="color:#475569;">Biz har dam olish kuni birga koreys kinosi ko'rib, koreys tilini ham o'rganamiz.</em></p>
  </div>
</details>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Qayta ishlatiladigan g'ishtlar:</strong> 제일/가장 좋아합니다 · -기 때문입니다 ·
  -(으)면 ... -(으)ㄹ 수 있습니다 · 벌써 ~이/가 되었습니다 · 성격이 밝다 · -(으)면서 ...도 합니다.
  Bu qoliplarga istalgan mavzuni joylang!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> "왜 한국어를 배웁니까?" savoliga SABAB jumlasi sifatida qaysi biri tabiiy?</p>
""",
             "choices": [
                 {"text": "한국 문화에 관심이 많기 때문입니다.", "is_correct": True},
                 {"text": "한국어는 언어입니다.", "is_correct": False},
                 {"text": "네, 배웁니다.", "is_correct": False},
                 {"text": "내일 학교에 갑니다.", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: -기 때문입니다 qolipidagi haqiqiy sabab. ② taʼrif (sabab emas), ③ tasdiq xolos,
④ mavzudan tashqari. SABAB jumlasining eng ishonchli qoliplari: <strong>-기 때문입니다 /
-아/어서 좋아합니다</strong>.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> Namunalardagi "벌써 오 년이 되었습니다" jumlasi javobga nima qo'shadi?</p>
""",
             "choices": [
                 {"text": "Aniq jonli detal — javobni shaxsiy va ishonarli qiladi", "is_correct": True},
                 {"text": "Hech narsa — ortiqcha jumla", "is_correct": False},
                 {"text": "Savolni takrorlaydi", "is_correct": False},
                 {"text": "Grammatik xato bor", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: raqamli aniq detal ("besh yil!") — 10-darsdagi "bonus detal" g'ishtining o'zi.
Yodlangan quruq javob bilan tirik javobning farqi ana shunday kichik detallarda.
Har mavzu javobingizga bittadan shunday detal qo'shing.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">건강에 좋다</div><div class="pp-card-back">sog'liqqa foydali</div></div>
  <div class="pp-card"><div class="pp-card-front">더위를 이기다</div><div class="pp-card-back">issiqni yengmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">꽃이 피다</div><div class="pp-card-back">gul ochilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">소풍을 가다</div><div class="pp-card-back">sayilga bormoq</div></div>
  <div class="pp-card"><div class="pp-card-front">벚꽃</div><div class="pp-card-back">gilos guli (sakura)</div></div>
  <div class="pp-card"><div class="pp-card-front">성격이 밝다</div><div class="pp-card-back">fe'li ochiq, quvnoq</div></div>
  <div class="pp-card"><div class="pp-card-front">즐거워지다</div><div class="pp-card-back">quvnab ketmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)면서</div><div class="pp-card-back">...gan holda, ...b turib</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Savollar doirasi tor: kundalik hayot · odamlar · o'zingiz — mavzu banki yetadi.</li>
  <li>Javoblarni o'zingizga moslang: qolip qoladi, mazmun sizniki.</li>
  <li>Har javobga bitta raqamli/jonli detal qo'shing.</li>
  <li>Bugungi soya rejasi: 3 mavzu × 3 jumla, har biri 3 marta ovoz chiqarib.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 12) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q1-3: To'liq amaliyot — uch savol imtihon ritmida",
        "summary": "Imtihon simulyatsiyasi: uchta savol audiosi ketma-ket — har biriga o'zingiz javob berasiz, keyin namuna bilan solishtirasiz.",
        "order":   12,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: endi siz gapirasiz!</h2>
<p>Bu darsda uchta savol — imtihon ritmida. Har savol uchun tartib:</p>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p><strong>1.</strong> Savol audiosini eshiting (bir marta — imtihondagidek).</p></div>
  <div class="pp-step"><p><strong>2.</strong> ~30 soniya o'ylang: <em>nima? nega? masalan?</em> katakchalarini to'ldiring.</p></div>
  <div class="pp-step"><p><strong>3.</strong> Telefoningizda ovoz yozgichni yoqib, 1 daqiqa davomida javob bering. To'xtamang!</p></div>
  <div class="pp-step"><p><strong>4.</strong> Namunaviy javobni eshiting, o'zingiznikini solishtiring, keyin namunani 2–3 marta soya qiling.</p></div>
</div>
"""},
            {"rich_text": """
<h3>1-savol</h3>
""",
             "audio": "topik_s_012_1.mp3",
             "audio_script": [
                 ("여자", "스트레스를 받으면 어떻게 풉니까? 이야기해 보세요."),
             ]},
            {"rich_text": """
<p><strong>Namunaviy javob</strong> (avval o'zingiz gapirdingizmi? 😉):</p>
""",
             "audio": "topik_s_012_2.mp3",
             "audio_script": [
                 ("남자", "저는 스트레스를 받으면 음악을 들으면서 산책을 합니다. 걸으면서 좋아하는 노래를 들으면 복잡한 생각이 사라지기 때문입니다. 특히 시험 기간에는 매일 저녁 삼십 분씩 걷습니다. 산책이 끝나면 마음이 가벼워져서 다시 공부할 힘이 생깁니다."),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>저는 스트레스를 받으면 음악을 들으면서 산책을 합니다.</strong><br><em style="color:#475569;">Men stress olsam, musiqa eshitib sayr qilaman.</em></p>
    <p><strong>걸으면서 좋아하는 노래를 들으면 복잡한 생각이 사라지기 때문입니다.</strong><br><em style="color:#475569;">Chunki yurib sevimli qo'shiqlarni eshitsam, chigal o'ylar tarqab ketadi.</em></p>
    <p><strong>특히 시험 기간에는 매일 저녁 삼십 분씩 걷습니다.</strong><br><em style="color:#475569;">Ayniqsa imtihon paytida har kuni kechqurun o'ttiz daqiqadan yuraman.</em></p>
    <p><strong>산책이 끝나면 마음이 가벼워져서 다시 공부할 힘이 생깁니다.</strong><br><em style="color:#475569;">Sayr tugagach, ko'nglim yengillashib, yana o'qishga kuch paydo bo'ladi.</em></p>
  </div>
</details>
<h3>2-savol</h3>
""",
             "audio": "topik_s_012_3.mp3",
             "audio_script": [
                 ("여자", "가 보고 싶은 나라가 있습니까? 왜 그 나라에 가 보고 싶습니까?"),
             ]},
            {"rich_text": """
<p><strong>Namunaviy javob:</strong></p>
""",
             "audio": "topik_s_012_4.mp3",
             "audio_script": [
                 ("남자", "저는 한국에 꼭 가 보고 싶습니다. 드라마에서 본 서울의 야경이 정말 아름다웠기 때문입니다. 한국에 가면 경복궁에도 가고 부산 바다도 보고 싶습니다. 그래서 지금 열심히 한국어를 공부하면서 여행 돈을 모으고 있습니다."),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>저는 한국에 꼭 가 보고 싶습니다.</strong><br><em style="color:#475569;">Men albatta Koreyaga borib ko'rmoqchiman.</em></p>
    <p><strong>드라마에서 본 서울의 야경이 정말 아름다웠기 때문입니다.</strong><br><em style="color:#475569;">Chunki dramada ko'rgan Seulning tungi manzarasi juda go'zal edi.</em></p>
    <p><strong>한국에 가면 경복궁에도 가고 부산 바다도 보고 싶습니다.</strong><br><em style="color:#475569;">Koreyaga borsam, Kyongbokkun saroyiga ham borib, Pusan dengizini ham ko'rmoqchiman.</em></p>
    <p><strong>그래서 지금 열심히 한국어를 공부하면서 여행 돈을 모으고 있습니다.</strong><br><em style="color:#475569;">Shuning uchun hozir astoydil koreys tilini o'rganib, sayohat puli yig'yapman.</em></p>
  </div>
</details>
<h3>3-savol</h3>
""",
             "audio": "topik_s_012_5.mp3",
             "audio_script": [
                 ("여자", "아침형 인간입니까, 저녁형 인간입니까? 이야기해 보세요."),
             ]},
            {"rich_text": """
<p><strong>Namunaviy javob:</strong></p>
""",
             "audio": "topik_s_012_6.mp3",
             "audio_script": [
                 ("남자", "저는 아침형 인간입니다. 아침에는 조용해서 집중이 잘되기 때문입니다. 매일 아침 여섯 시에 일어나서 한 시간 동안 한국어 단어를 외웁니다. 밤에 외우는 것보다 아침에 외우는 것이 기억에 더 오래 남는 것 같습니다."),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>저는 아침형 인간입니다.</strong><br><em style="color:#475569;">Men tongparast (ertalabki) odamman.</em></p>
    <p><strong>아침에는 조용해서 집중이 잘되기 때문입니다.</strong><br><em style="color:#475569;">Chunki ertalab atrof jim — diqqat yaxshi jamlanadi.</em></p>
    <p><strong>매일 아침 여섯 시에 일어나서 한 시간 동안 한국어 단어를 외웁니다.</strong><br><em style="color:#475569;">Har kuni ertalab oltida turib, bir soat koreyscha so'z yodlayman.</em></p>
    <p><strong>밤에 외우는 것보다 아침에 외우는 것이 기억에 더 오래 남는 것 같습니다.</strong><br><em style="color:#475569;">Kechasi yodlagandan ko'ra ertalab yodlagan xotirada uzoqroq qoladiganga o'xshaydi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot.</strong> O'z javobingizni yozib eshitdingiz. Uni baholashda eng muhim uch savol qaysi qatorda?</p>
""",
             "choices": [
                 {"text": "Savolga javob berdimmi? Sabab aytdimmi? To'xtab qolmadimmi?", "is_correct": True},
                 {"text": "Ovozim chiroylimi? Tez gapirdimmi? Uzun so'z ishlatdimmi?", "is_correct": False},
                 {"text": "Necha daqiqa gapirdim? Nechta so'z aytdim? Qaysi shevada gapirdim?", "is_correct": False},
                 {"text": "Grammatika kitobidagi nechta qoidani ishlatdim?", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: bu uch savol — imtihonning uch mezonining o'zi: mazmun (savolga javob), til
(sabab qolipi to'g'rimi), yetkazish (oqim uzilmadimi). Chiroyli ovoz, tezlik, murakkab
so'z — mezon emas. O'z yozuvingizni har safar shu uch savol bilan tekshiring — bu sizning
shaxsiy baholovchingiz. 1-savol turi tayyor: keyingi bekat — rol o'ynash (Q2)! 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">복잡한 생각</div><div class="pp-card-back">chigal o'ylar</div></div>
  <div class="pp-card"><div class="pp-card-front">마음이 가벼워지다</div><div class="pp-card-back">ko'ngli yengillashmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">야경</div><div class="pp-card-back">tungi manzara</div></div>
  <div class="pp-card"><div class="pp-card-front">돈을 모으다</div><div class="pp-card-back">pul yig'moq</div></div>
  <div class="pp-card"><div class="pp-card-front">아침형 인간</div><div class="pp-card-back">tongparast odam</div></div>
  <div class="pp-card"><div class="pp-card-front">집중이 잘되다</div><div class="pp-card-back">diqqat yaxshi jamlanmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">단어를 외우다</div><div class="pp-card-back">so'z yodlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">기억에 남다</div><div class="pp-card-back">xotirada qolmoq</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Mashq tartibi: savolni eshit → 30 soniya reja → yozib gapir → namuna bilan solishtir → soya qil.</li>
  <li>O'zingizni uch savol bilan baholang: javob? sabab? oqim?</li>
  <li>Telefondagi ovoz yozgich — eng arzon va eng halol o'qituvchingiz.</li>
</ul>
"""},
        ],
    },
]
