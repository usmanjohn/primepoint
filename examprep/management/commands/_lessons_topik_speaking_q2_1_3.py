# TOPIK 말하기 (Speaking) — 2-savol: 그림 보고 역할 수행하기, lessons 1–3 (orders 20–22).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_speaking_q2_1_3.py \
#            --out examprep/management/commands/audio/speaking_q2
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_speaking_q2_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/speaking_q2

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "2-savol: Rol o'ynash (그림 보고 역할 수행하기)",
    "summary": "Vaziyat rasmiga qarab rol bajarish: xuddi o'sha odamga gapirayotgandek — muloyim so'rov, savol va iltimos qoliplari bilan.",
    "icon":    "bi-person-badge",
    "order":   3,
}

LESSONS = [
    # ── Lesson 1 (order 20) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q2-1: Rol o'ynash formulasi — salom, maqsad, iltimos",
        "summary": "2-topshiriq bilan tanishuv: vaziyatga kirib, ko'rinmas suhbatdoshga gapirish; universal 4 qadamli tuzilma.",
        "order":   20,
        "blocks": [
            {"rich_text": """
<h2>🎭 2-topshiriq: siz endi aktyorsiz</h2>
<p>Ekranda <strong>vaziyat rasmi</strong> va topshiriq matni chiqadi: masalan, "siz do'kondasiz;
kecha olgan ko'ylagingizni almashtirmoqchisiz. Sotuvchi bilan gaplashing." Endi siz o'sha
odam bilan <strong>haqiqatan gaplashayotgandek</strong> gapirasiz — kompyuter javob
qaytarmaydi, lekin siz dialogning O'Z tomoningizni to'liq aytib berasiz.</p>
<p>Eng katta xato — vaziyatni <strong>tasvirlab berish</strong>: "Bu rasmda odam do'konda
turibdi..." — YO'Q! Siz rasmni tushuntirmaysiz, rasm ICHIGA kirasiz: "저기요, 어제 이 옷을
샀는데요..." Farqni his qiling: hikoyachi emas — <strong>qahramon</strong>.</p>
<h3>Universal 4 qadam</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p><strong>1. Murojaat / salom.</strong> 저기요 (kechirasiz — do'konda),
  여보세요 (allo — telefonda), 안녕하세요 (umumiy). Suhbat eshigi ochildi.</p></div>
  <div class="pp-step"><p><strong>2. Vaziyatni aytish.</strong> Nima bo'ldi / kimsiz: 어제 이 옷을
  샀는데요, 사이즈가 좀 큰 것 같아요. (-는데요 — yumshoq kirish qolipi!)</p></div>
  <div class="pp-step"><p><strong>3. Iltimos / savol.</strong> Muloyim qoliplar: 바꿔 주시겠어요?
  (almashtirib bera olasizmi?), -(으)ㄹ 수 있을까요? (mumkinmi?), 혹시 ~이/가 있나요?</p></div>
  <div class="pp-step"><p><strong>4. Qo'shimcha detal + yakun.</strong> Aniq ma'lumot bering (o'lcham,
  vaqt, joy) va rahmat bilan yoping: 네, 감사합니다!</p></div>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Baholovchi 2-topshiriqda aynan <strong>muloyimlik
  qoliplari</strong>ni kutadi: -아/어 주시겠어요? · -(으)ㄹ 수 있을까요? · 혹시 · 좀. Bu to'rt
  "sehrli kalit"ni har rol o'ynashda kamida ikki marta ishlating!
</div>
"""},
            {"rich_text": """
<h3>🎧 Namuna: do'konda almashtirish</h3>
<p><strong>Vaziyat:</strong> 옷 가게 — kecha olgan ko'ylagingiz katta chiqdi. Sotuvchi bilan
gaplashing. Avval topshiriq audiosi, keyin namunaviy javob:</p>
""",
             "audio": "topik_s_020_1.mp3",
             "audio_script": [
                 ("여자", "옷 가게에서 어제 산 옷을 바꾸려고 합니다. 점원에게 이야기해 보세요."),
             ]},
            {"rich_text": """
<p><strong>Namunaviy javob</strong> — 4 qadamni sanab boring:</p>
""",
             "audio": "topik_s_020_2.mp3",
             "audio_script": [
                 ("남자", "저기요, 안녕하세요. 어제 여기에서 이 티셔츠를 샀는데요. 집에 가서 입어 보니까 사이즈가 좀 큰 것 같아요. 혹시 한 사이즈 작은 것으로 바꿀 수 있을까요? 영수증은 여기 있습니다. 네, 감사합니다!"),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — avval o'zingiz aytib ko'ring!</summary>
  <div style="margin-top:10px;">
    <p><strong>저기요, 안녕하세요.</strong> <span style="background:#dbeafe;padding:1px 8px;border-radius:999px;font-size:.8em;">1 MUROJAAT</span><br>
    <em style="color:#475569;">Kechirasiz, assalomu alaykum.</em></p>
    <p><strong>어제 여기에서 이 티셔츠를 샀는데요. 집에 가서 입어 보니까 사이즈가 좀 큰 것 같아요.</strong> <span style="background:#dcfce7;padding:1px 8px;border-radius:999px;font-size:.8em;">2 VAZIYAT</span><br>
    <em style="color:#475569;">Kecha shu yerdan bu futbolkani olgandim. Uyga borib kiyib ko'rsam, o'lchami kattaroq ekan.</em></p>
    <p><strong>혹시 한 사이즈 작은 것으로 바꿀 수 있을까요?</strong> <span style="background:#fef3c7;padding:1px 8px;border-radius:999px;font-size:.8em;">3 ILTIMOS</span><br>
    <em style="color:#475569;">Mabodo bir o'lcham kichigiga almashtirsam bo'ladimi?</em></p>
    <p><strong>영수증은 여기 있습니다. 네, 감사합니다!</strong> <span style="background:#fae8ff;padding:1px 8px;border-radius:999px;font-size:.8em;">4 DETAL+YAKUN</span><br>
    <em style="color:#475569;">Chek mana. Xo'p, rahmat!</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> Rol o'ynashda eng katta xato qaysi?</p>
""",
             "choices": [
                 {"text": "Rasmni chetdan tasvirlab berish ('rasmda bir odam turibdi...')", "is_correct": True},
                 {"text": "Muloyim qoliplarni ishlatish", "is_correct": False},
                 {"text": "Aniq detallarni aytish", "is_correct": False},
                 {"text": "Rahmat bilan yakunlash", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: 2-topshiriq — tasvirlash emas, ROL BAJARISH. Siz hikoyachi emas, qahramonsiz:
rasm ichiga kirib, suhbatdoshga to'g'ridan-to'g'ri gapirasiz. ②③④ — aksincha, aynan
kutiladigan to'g'ri harakatlar.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> "혹시 한 사이즈 작은 것으로 바꿀 수 있을까요?" jumlasida nechta "sehrli kalit" bor?</p>
""",
             "choices": [
                 {"text": "Ikkitasi: 혹시 va -(으)ㄹ 수 있을까요?", "is_correct": True},
                 {"text": "Bittasi: faqat 혹시", "is_correct": False},
                 {"text": "Hech qanday muloyim qolip yo'q", "is_correct": False},
                 {"text": "To'rttasi ham bor", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: 혹시 (mabodo — yumshatuvchi) + -(으)ㄹ 수 있을까요? (mumkinmikan — muloyim so'rov).
Bitta jumlada ikki kalit — baholovchi qulog'iga musiqa! To'rt kalit ro'yxati:
혹시 · 좀 · -아/어 주시겠어요? · -(으)ㄹ 수 있을까요?</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">저기요</div><div class="pp-card-back">kechirasiz (chaqirish)</div></div>
  <div class="pp-card"><div class="pp-card-front">-는데요</div><div class="pp-card-back">yumshoq kirish (...gandim)</div></div>
  <div class="pp-card"><div class="pp-card-front">혹시</div><div class="pp-card-back">mabodo</div></div>
  <div class="pp-card"><div class="pp-card-front">-아/어 주시겠어요?</div><div class="pp-card-back">...b bera olasizmi?</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)ㄹ 수 있을까요?</div><div class="pp-card-back">... mumkinmikan?</div></div>
  <div class="pp-card"><div class="pp-card-front">바꾸다</div><div class="pp-card-back">almashtirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">영수증</div><div class="pp-card-back">chek</div></div>
  <div class="pp-card"><div class="pp-card-front">점원</div><div class="pp-card-back">sotuvchi, xodim</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Rasmni tasvirlamang — ichiga kiring: siz qahramonsiz.</li>
  <li>4 qadam: murojaat → vaziyat (-는데요) → iltimos (sehrli kalitlar) → detal + rahmat.</li>
  <li>To'rt sehrli kalit: 혹시 · 좀 · -아/어 주시겠어요? · -(으)ㄹ 수 있을까요?</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 21) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q2-2: Sahna banki — telefon va yuzma-yuz",
        "summary": "Eng ko'p tushadigan sahnalar: restoranga qo'ng'iroq (bron), do'stdan iltimos, yo'qolgan buyum — soya qilinadigan modellari bilan.",
        "order":   21,
        "blocks": [
            {"rich_text": """
<h2>🗂️ Sahna banki: uch klassik vaziyat</h2>
<p>2-topshiriq sahnalari ikki oilaga bo'linadi: <strong>yuzma-yuz</strong> (do'kon, restoran,
kutubxona) va <strong>telefon</strong> (bron qilish, so'rash, o'zgartirish). Telefonda
bitta qo'shimcha qadam bor: <strong>o'zingizni tanishtirish</strong> (여보세요, 저는 ~인데요).
Quyida uchta model — soya qiling va qoliplarini oling.</p>
"""},
            {"rich_text": """
<h3>🎧 Sahna 1: Restoranga qo'ng'iroq — joy bron qilish</h3>
""",
             "audio": "topik_s_021_1.mp3",
             "audio_script": [
                 ("여자", "식당에 전화해서 자리를 예약하려고 합니다. 직원에게 이야기해 보세요."),
                 ("남자", "여보세요, 안녕하세요. 자리를 예약하고 싶은데요. 이번 주 토요일 저녁 일곱 시에 네 명 자리 있을까요? 아, 그리고 혹시 창가 자리로 부탁드려도 될까요? 친구 생일이라서요. 네, 감사합니다. 토요일에 뵙겠습니다!"),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>여보세요, 안녕하세요. 자리를 예약하고 싶은데요.</strong><br><em style="color:#475569;">Allo, assalomu alaykum. Joy bron qilmoqchi edim.</em></p>
    <p><strong>이번 주 토요일 저녁 일곱 시에 네 명 자리 있을까요?</strong><br><em style="color:#475569;">Shu hafta shanba kechki yettida to'rt kishilik joy bormikan?</em></p>
    <p><strong>아, 그리고 혹시 창가 자리로 부탁드려도 될까요? 친구 생일이라서요.</strong><br><em style="color:#475569;">Ha aytgancha, mabodo deraza oldidagi joyni so'rasam bo'ladimi? Do'stimning tug'ilgan kuni-da.</em></p>
    <p><strong>네, 감사합니다. 토요일에 뵙겠습니다!</strong><br><em style="color:#475569;">Xo'p, rahmat. Shanbada ko'rishguncha!</em></p>
  </div>
</details>
<p>E'tibor: <strong>uch aniq detal</strong> (kun, soat, kishi soni) + sabab (-(이)라서요) —
rol o'ynashda detallar mazmun balining yarmi!</p>
<h3>🎧 Sahna 2: Do'stdan iltimos — uchrashuvni ko'chirish</h3>
""",
             "audio": "topik_s_021_2.mp3",
             "audio_script": [
                 ("여자", "친구와 내일 만나기로 했는데 약속을 바꿔야 합니다. 친구에게 이야기해 보세요."),
                 ("남자", "여보세요, 나야. 내일 만나기로 했잖아. 정말 미안한데, 내일 갑자기 아르바이트가 생겨서 못 갈 것 같아. 혹시 토요일로 바꿔도 괜찮아? 대신 토요일에는 내가 맛있는 점심 살게. 정말 미안해!"),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>여보세요, 나야. 내일 만나기로 했잖아.</strong><br><em style="color:#475569;">Allo, bu men. Ertaga uchrashamiz degandik-ku.</em></p>
    <p><strong>정말 미안한데, 내일 갑자기 아르바이트가 생겨서 못 갈 것 같아.</strong><br><em style="color:#475569;">Juda uzr-u, ertaga to'satdan ishim chiqib qoldi, borolmasam kerak.</em></p>
    <p><strong>혹시 토요일로 바꿔도 괜찮아? 대신 토요일에는 내가 맛있는 점심 살게.</strong><br><em style="color:#475569;">Mabodo shanbaga ko'chirsak maylimi? Evaziga shanbada tushlikni men olib beraman.</em></p>
  </div>
</details>
<p>Do'st bilan — <strong>반말</strong> (oddiy uslub: 나야, 괜찮아?). Rasmdagi suhbatdosh KIM
ekanligiga qarab uslubni tanlang: xodim/notanish → -요/-ㅂ니다, yaqin do'st → 반말.
Va iltimosning oltin tuzilmasi: <strong>uzr + sabab + taklif + evaz</strong> (대신 ~ㄹ게).</p>
<h3>🎧 Sahna 3: Yo'qotilgan buyum — kafega qo'ng'iroq</h3>
""",
             "audio": "topik_s_021_3.mp3",
             "audio_script": [
                 ("여자", "카페에 가방을 놓고 왔습니다. 카페에 전화해서 이야기해 보세요."),
                 ("남자", "여보세요, 거기 하늘 카페지요? 제가 한 시간쯤 전에 거기에 있었는데요. 창가 자리에 까만색 가방을 놓고 온 것 같아요. 혹시 가방을 보셨을까요? 아, 있어요? 정말 다행이네요! 제가 삼십 분 안에 찾으러 가겠습니다. 감사합니다!"),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>여보세요, 거기 하늘 카페지요? 제가 한 시간쯤 전에 거기에 있었는데요.</strong><br><em style="color:#475569;">Allo, Hanul kafemi? Men bir soatcha oldin o'sha yerda edim.</em></p>
    <p><strong>창가 자리에 까만색 가방을 놓고 온 것 같아요. 혹시 가방을 보셨을까요?</strong><br><em style="color:#475569;">Deraza oldidagi joyda qora sumkamni qoldirib kelganga o'xshayman. Mabodo sumkani ko'rdingizmi?</em></p>
    <p><strong>아, 있어요? 정말 다행이네요! 제가 삼십 분 안에 찾으러 가겠습니다.</strong><br><em style="color:#475569;">Voy, bormi? Juda xayriyat-e! O'ttiz daqiqa ichida olib ketgani boraman.</em></p>
  </div>
</details>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Sahna 3 dagi pro-harakat:</strong> suhbatdosh javobini <strong>o'zingiz
  tasavvur qilib</strong>, unga munosabat bildiring ("아, 있어요? 다행이네요!") — dialog
  jonli chiqadi va rol o'ynash bali ko'tariladi.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> Rasmda siz kutubxonachi bilan gaplashyapsiz. Qaysi uslub to'g'ri?</p>
""",
             "choices": [
                 {"text": "-요 / -ㅂ니다 (hurmat uslubi)", "is_correct": True},
                 {"text": "반말 (nya, 괜찮아 uslubi)", "is_correct": False},
                 {"text": "Ikkalasini aralashtirib", "is_correct": False},
                 {"text": "Uslub muhim emas", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: notanish odam / xizmat xodimi → doim hurmat uslubi. 반말 faqat rasmda YAQIN DO'ST
ko'rsatilganda. Aralashtirish (③) — til mezonida ayanchli xato: bitta rolda bitta uslub!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> Do'stga iltimosning oltin tuzilmasi qaysi?</p>
""",
             "choices": [
                 {"text": "Uzr → sabab → taklif → evaz (대신 ~ㄹ게)", "is_correct": True},
                 {"text": "Talab → sukut → xayrlashish", "is_correct": False},
                 {"text": "Sabab → sabab → sabab", "is_correct": False},
                 {"text": "Taklif → uzrsiz yakun", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: 미안한데 (uzr) → 아르바이트가 생겨서 (sabab) → 토요일로 바꿔도 괜찮아? (taklif) →
대신 점심 살게 (evaz). Evaz jumlasi — munosabatni saqlovchi sehr: iltimos og'irligini
yengillashtiradi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">예약하다</div><div class="pp-card-back">bron qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">창가 자리</div><div class="pp-card-back">deraza oldidagi joy</div></div>
  <div class="pp-card"><div class="pp-card-front">-(이)라서요</div><div class="pp-card-back">...ligi uchun-da (sabab)</div></div>
  <div class="pp-card"><div class="pp-card-front">약속을 바꾸다</div><div class="pp-card-back">uchrashuvni ko'chirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">대신</div><div class="pp-card-back">evaziga, o'rniga</div></div>
  <div class="pp-card"><div class="pp-card-front">놓고 오다</div><div class="pp-card-back">qoldirib kelmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">다행이네요</div><div class="pp-card-back">xayriyat-e</div></div>
  <div class="pp-card"><div class="pp-card-front">뵙겠습니다</div><div class="pp-card-back">ko'rishguncha (hurmat)</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Telefonda qo'shimcha qadam: o'zingizni tanishtiring (저는 ~인데요).</li>
  <li>Suhbatdoshga qarab uslub: xodim → 존댓말, do'st → 반말. Aralashtirmang!</li>
  <li>Detallar (kun, soat, rang, son) — mazmun balining yarmi.</li>
  <li>Pro-harakat: suhbatdosh javobiga munosabat bildiring (아, 있어요? 다행이네요!).</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 22) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q2-3: To'liq amaliyot — uch rol imtihon ritmida",
        "summary": "Uch vaziyat: dorixona, qo'shnidan iltimos, do'stni taklif qilish — o'zingiz gapirasiz, keyin namuna bilan solishtirasiz.",
        "order":   22,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: uch sahna, uch rol</h2>
<p>Tartib o'sha-o'sha: topshiriqni eshiting → 30 soniya reja (4 qadam katagi: murojaat?
vaziyat? iltimos? detal?) → telefonga yozib 1 daqiqa gapiring → namunani eshitib soya
qiling. Boshladik!</p>
"""},
            {"rich_text": """
<h3>1-sahna</h3>
""",
             "audio": "topik_s_022_1.mp3",
             "audio_script": [
                 ("여자", "약국에 왔습니다. 약사에게 증상을 이야기하고 약을 사 보세요."),
             ]},
            {"rich_text": """
<p><strong>Namunaviy javob</strong> (avval o'zingiz!):</p>
""",
             "audio": "topik_s_022_2.mp3",
             "audio_script": [
                 ("남자", "안녕하세요. 어제저녁부터 목이 아프고 기침이 나는데요. 열은 없는데 콧물이 조금 나요. 감기약 좀 주시겠어요? 아, 그리고 제가 우유를 마시면 배가 아파서요. 혹시 우유와 같이 먹으면 안 되는 약인지 확인해 주실 수 있을까요? 감사합니다."),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>어제저녁부터 목이 아프고 기침이 나는데요. 열은 없는데 콧물이 조금 나요.</strong><br><em style="color:#475569;">Kecha kechqurundan tomog'im og'rib, yo'tal turdi. Isitma yo'q-u, burnim ozgina oqyapti.</em></p>
    <p><strong>감기약 좀 주시겠어요?</strong><br><em style="color:#475569;">Shamollash dorisidan bera olasizmi?</em></p>
    <p><strong>혹시 우유와 같이 먹으면 안 되는 약인지 확인해 주실 수 있을까요?</strong><br><em style="color:#475569;">Mabodo sut bilan ichib bo'lmaydigan dori emasligini tekshirib bera olasizmi?</em></p>
  </div>
</details>
<h3>2-sahna</h3>
""",
             "audio": "topik_s_022_3.mp3",
             "audio_script": [
                 ("여자", "내일 하루 여행을 갑니다. 옆집 사람에게 택배를 부탁해 보세요."),
             ]},
            {"rich_text": """
<p><strong>Namunaviy javob:</strong></p>
""",
             "audio": "topik_s_022_4.mp3",
             "audio_script": [
                 ("남자", "안녕하세요. 옆집에 사는 사람인데요. 다름이 아니라 부탁이 하나 있어서요. 제가 내일 하루 여행을 가는데 그날 중요한 택배가 올 예정이에요. 혹시 택배를 좀 받아 주실 수 있을까요? 모레 아침에 찾으러 오겠습니다. 정말 감사합니다. 여행에서 맛있는 거 사 올게요!"),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>옆집에 사는 사람인데요. 다름이 아니라 부탁이 하나 있어서요.</strong><br><em style="color:#475569;">Qo'shni xonadonda yashayman. Gap shundaki, bitta iltimosim bor edi.</em></p>
    <p><strong>제가 내일 하루 여행을 가는데 그날 중요한 택배가 올 예정이에요. 혹시 택배를 좀 받아 주실 수 있을까요?</strong><br><em style="color:#475569;">Ertaga bir kunga safarga ketyapman, o'sha kuni muhim pochta jo'natmasi keladi. Mabodo jo'natmani qabul qilib tura olasizmi?</em></p>
    <p><strong>모레 아침에 찾으러 오겠습니다. 여행에서 맛있는 거 사 올게요!</strong><br><em style="color:#475569;">Indinga ertalab olib ketgani kelaman. Safardan shirinlik olib kelaman!</em></p>
  </div>
</details>
<p><strong>다름이 아니라</strong> ("gap shundaki") — iltimos oldidan keladigan oltin ibora:
suhbatdoshni tayyorlaydi. Va yana <strong>evaz</strong> g'ishti: 맛있는 거 사 올게요! 😄</p>
<h3>3-sahna</h3>
""",
             "audio": "topik_s_022_5.mp3",
             "audio_script": [
                 ("여자", "주말에 집에서 파티를 합니다. 친구에게 전화해서 초대해 보세요."),
             ]},
            {"rich_text": """
<p><strong>Namunaviy javob:</strong></p>
""",
             "audio": "topik_s_022_6.mp3",
             "audio_script": [
                 ("남자", "여보세요, 나야! 뭐 해? 다른 게 아니라, 이번 주 토요일에 우리 집에서 작은 파티를 하려고 해. 새집으로 이사했잖아. 저녁 여섯 시까지 올 수 있어? 지하철 이 호선 공원역에서 걸어서 오 분이야. 음식은 내가 준비할 테니까 몸만 와. 꼭 와야 돼!"),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>이번 주 토요일에 우리 집에서 작은 파티를 하려고 해. 새집으로 이사했잖아.</strong><br><em style="color:#475569;">Shu shanba uyimizda kichik bazm qilmoqchimiz. Yangi uyga ko'chdik-ku.</em></p>
    <p><strong>저녁 여섯 시까지 올 수 있어? 지하철 이 호선 공원역에서 걸어서 오 분이야.</strong><br><em style="color:#475569;">Kechki oltigacha kela olasanmi? Metroning 2-yo'nalishi, Bog' bekatidan piyoda besh daqiqa.</em></p>
    <p><strong>음식은 내가 준비할 테니까 몸만 와. 꼭 와야 돼!</strong><br><em style="color:#475569;">Ovqatni o'zim tayyorlayman, o'zing kelsang bas. Albatta kel!</em></p>
  </div>
</details>
<p><strong>몸만 와</strong> ("faqat o'zing kel") — taklifning eng shirin koreyscha iborasi.
Taklif detallari to'liq: kun, vaqt, manzil, sabab — baholovchi kutgan hamma katak yopildi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot.</strong> O'z yozuvingizni tekshiring: rol o'ynash uchun TO'RT nazorat savoli qaysi qatorda?</p>
""",
             "choices": [
                 {"text": "Rolga kirdimmi? Uslub mosmi? Sehrli kalit ishlatdimmi? Detal aytdimmi?", "is_correct": True},
                 {"text": "Rasm chiroylimi? Ovozim balandmi? Tez gapirdimmi? Kulib turdimmi?", "is_correct": False},
                 {"text": "Necha so'z? Necha daqiqa? Necha jumla? Necha grammatika?", "is_correct": False},
                 {"text": "Suhbatdosh javob berdimi? Kompyuter tushundimi? Baholovchi kim? Ball qancha?", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: to'rt nazorat = topshiriqning mohiyati: qahramon bo'lish (tasvirlamaslik), to'g'ri
uslub (존댓말/반말), muloyimlik kalitlari, aniq detallar. Q2 tayyor — keyingi bekat: to'rt
rasmdan hikoya (Q3)! 🎭</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">증상</div><div class="pp-card-back">kasallik belgisi</div></div>
  <div class="pp-card"><div class="pp-card-front">기침이 나다</div><div class="pp-card-back">yo'tal tutmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">콧물이 나다</div><div class="pp-card-back">burun oqmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">다름이 아니라</div><div class="pp-card-back">gap shundaki</div></div>
  <div class="pp-card"><div class="pp-card-front">택배를 받다</div><div class="pp-card-back">jo'natmani qabul qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">이사하다</div><div class="pp-card-back">ko'chmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">몸만 와</div><div class="pp-card-back">faqat o'zing kel</div></div>
  <div class="pp-card"><div class="pp-card-front">꼭</div><div class="pp-card-back">albatta</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>4 qadam har sahnada ishlaydi: murojaat → vaziyat → iltimos → detal+yakun.</li>
  <li>다름이 아니라 — iltimos eshigi; 대신/맛있는 거 사 올게 — evaz g'ishti.</li>
  <li>To'rt nazorat savoli bilan o'z yozuvingizni tekshiring.</li>
</ul>
"""},
        ],
    },
]
