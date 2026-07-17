# TOPIK 말하기 (Speaking) — 5-savol: 자료 해석하기, lessons 1–3 (orders 50–52).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_speaking_q5_1_3.py \
#            --out examprep/management/commands/audio/speaking_q5
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_speaking_q5_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/speaking_q5

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "5-savol: Grafik tahlili (자료 해석하기)",
    "summary": "Grafik va so'rov natijalarini og'zaki tahlil qilish — og'zaki 쓰기 53: kirish, o'zgarish, sabab-istiqbol uch bosqichi.",
    "icon":    "bi-bar-chart",
    "order":   6,
}

LESSONS = [
    # ── Lesson 1 (order 50) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q5-1: Og'zaki 쓰기 53 — uch bosqichli tahlil",
        "summary": "5-topshiriq bilan tanishuv: grafikni KIRISH → O'ZGARISH → SABAB/ISTIQBOL tartibida gapirish; yozish shablonlari og'izga ko'chadi.",
        "order":   50,
        "blocks": [
            {"rich_text": """
<h2>📊 5-topshiriq: grafik endi gapiradi</h2>
<p>Ekranda <strong>grafik yoki so'rov natijasi</strong> chiqadi (쓰기 53 dagi kabi!) va siz
uni <strong>og'zaki</strong> tahlil qilasiz. Xushxabar: siz buni allaqachon bilasiz — yozish
bo'limida o'rgangan barcha shablonlar (늘다, 줄다, 차지하다, 전망...) shu yerda aynan ishlaydi.
Farq bitta: yozmaysiz, <strong>aytasiz</strong> — demak soya mashqi kerak.</p>
<h3>Uch bosqich</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi bosqich ▸">
  <div class="pp-step"><p><strong>1. KIRISH — bu qanday ma'lumot?</strong><br>
  이 자료는 ~을/를 대상으로 ~에 대해 조사한 것입니다. (Bu ma'lumot ~lar orasida ~ haqida
  o'tkazilgan so'rov.)</p></div>
  <div class="pp-step"><p><strong>2. O'ZGARISH — raqamlar nima deydi?</strong><br>
  ~년에는 ~였는데 ~년에는 ~(으)로 늘었습니다/줄었습니다. 특히 ~이/가 1위를 차지했습니다.
  (…yilda … edi, …yilda …ga oshdi/kamaydi. Ayniqsa … 1-o'rinni egalladi.)</p></div>
  <div class="pp-step"><p><strong>3. SABAB yoki ISTIQBOL — nega / endi nima bo'ladi?</strong><br>
  이러한 변화의 원인은 ~기 때문입니다. / 앞으로 ~(으)ㄹ 것으로 보입니다.
  (Bu o'zgarish sababi — ... / Kelgusida ... bo'lishi kutiladi.)</p></div>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Raqamlarni OG'ZAKI aytish mashqi shart:</strong> 25% → 이십오 퍼센트,
  2020년 → 이천이십 년, 3배 → 세 배. Yozishda oson — og'izda adashadi! Har grafik
  mashqida raqamlarni ovoz chiqarib ayting.
</div>
"""},
            {"rich_text": """
<h3>Namuna grafigi</h3>
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:16px;margin:12px 0;">
  <p style="font-weight:700;text-align:center;margin:0 0 10px;">대학생의 아침 식사 여부 (아침을 먹지 않는 학생 비율)</p>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:70px;font-size:.85em;">2015년</span><div style="height:22px;background:#93c5fd;border-radius:4px;width:30%;"></div><span style="font-size:.85em;">30%</span></div>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:70px;font-size:.85em;">2025년</span><div style="height:22px;background:#3b82f6;border-radius:4px;width:60%;"></div><span style="font-size:.85em;">60%</span></div>
  <p style="font-size:.8em;color:#64748b;margin:10px 0 0;">원인: ① 아침에 시간이 없어서 ② 입맛이 없어서</p>
</div>
<p>Endi shu grafikning to'liq og'zaki tahlilini eshiting — uch bosqichni sanang:</p>
""",
             "audio": "topik_s_050_1.mp3",
             "audio_script": [
                 ("남자", "이 자료는 대학생을 대상으로 아침 식사에 대해 조사한 것입니다. 조사 결과에 따르면 아침을 먹지 않는 학생이 이천십오 년에는 삼십 퍼센트였는데, 이천이십오 년에는 육십 퍼센트로 두 배나 늘었습니다. 이러한 변화의 원인은 두 가지입니다. 첫째, 아침에 시간이 없기 때문입니다. 둘째, 아침에 입맛이 없기 때문입니다. 아침을 먹지 않으면 건강에 나쁘기 때문에, 앞으로 이 문제에 대한 관심이 더 필요할 것으로 보입니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — avval o'zingiz aytib ko'ring!</summary>
  <div style="margin-top:10px;">
    <p><strong>이 자료는 대학생을 대상으로 아침 식사에 대해 조사한 것입니다.</strong> <span style="background:#dbeafe;padding:1px 8px;border-radius:999px;font-size:.8em;">1 KIRISH</span><br>
    <em style="color:#475569;">Bu ma'lumot talabalar orasida nonushta haqida o'tkazilgan so'rov.</em></p>
    <p><strong>아침을 먹지 않는 학생이 이천십오 년에는 삼십 퍼센트였는데, 이천이십오 년에는 육십 퍼센트로 두 배나 늘었습니다.</strong> <span style="background:#dcfce7;padding:1px 8px;border-radius:999px;font-size:.8em;">2 O'ZGARISH</span><br>
    <em style="color:#475569;">Nonushta qilmaydigan talabalar 2015-yilda 30% edi, 2025-yilda 60% ga — naq ikki baravar oshdi.</em></p>
    <p><strong>이러한 변화의 원인은 두 가지입니다. 첫째... 둘째...</strong> <span style="background:#fef3c7;padding:1px 8px;border-radius:999px;font-size:.8em;">3 SABAB</span><br>
    <em style="color:#475569;">Bu o'zgarishning sababi ikkita. Birinchidan — vaqt yo'qligi. Ikkinchidan — ishtaha yo'qligi.</em></p>
    <p><strong>앞으로 이 문제에 대한 관심이 더 필요할 것으로 보입니다.</strong> <span style="background:#fae8ff;padding:1px 8px;border-radius:999px;font-size:.8em;">+ ISTIQBOL</span><br>
    <em style="color:#475569;">Kelgusida bu muammoga ko'proq e'tibor kerak bo'ladi, shekilli.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> Grafik tahlilining birinchi jumlasi qaysi bo'lishi kerak?</p>
""",
             "choices": [
                 {"text": "이 자료는 ~을 대상으로 ~에 대해 조사한 것입니다.", "is_correct": True},
                 {"text": "제 취미는 축구입니다.", "is_correct": False},
                 {"text": "저는 아침을 안 먹습니다.", "is_correct": False},
                 {"text": "그래프가 예쁩니다.", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: avval ma'lumotni tanishtirish — kim orasida, nima haqida. ③ — Q5 dagi eng ko'p
xato: grafik topshirig'ida O'Z odatingizni gapirish! Bu yerda siz tahlilchi, qahramon emas.
Shaxsiy fikr faqat oxirgi istiqbol jumlasiga ozgina sig'adi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">~을/를 대상으로</div><div class="pp-card-back">...lar orasida (so'rov)</div></div>
  <div class="pp-card"><div class="pp-card-front">조사하다</div><div class="pp-card-back">so'rov o'tkazmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">~에 따르면</div><div class="pp-card-back">...ga ko'ra</div></div>
  <div class="pp-card"><div class="pp-card-front">두 배나 늘다</div><div class="pp-card-back">naq ikki baravar oshmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">원인은 두 가지입니다</div><div class="pp-card-back">sababi ikkita</div></div>
  <div class="pp-card"><div class="pp-card-front">첫째... 둘째...</div><div class="pp-card-back">birinchidan... ikkinchidan...</div></div>
  <div class="pp-card"><div class="pp-card-front">~(으)ㄹ 것으로 보입니다</div><div class="pp-card-back">... bo'lishi kutiladi</div></div>
  <div class="pp-card"><div class="pp-card-front">입맛이 없다</div><div class="pp-card-back">ishtahasi yo'q</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Q5 = og'zaki 쓰기 53: KIRISH → O'ZGARISH → SABAB/ISTIQBOL.</li>
  <li>Siz tahlilchisiz — o'z odatingizni emas, RAQAMLARNI gapiring.</li>
  <li>Raqamlarni ovoz chiqarib aytishni alohida mashq qiling (이천이십오 년!).</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 51) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q5-2: Raqamlar tili — o'sish, tartib va taqqoslash",
        "summary": "Og'zaki grafik lug'ati: o'sish-kamayish darajalari, reyting tili (1위, 그 뒤를 이어), taqqoslash — va ranking namunasi.",
        "order":   51,
        "blocks": [
            {"rich_text": """
<h2>🔢 Raqamlar tili: uch guruh ibora</h2>
<h3>① O'sish-kamayish (darajasi bilan!)</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>꾸준히 늘었습니다</strong> — barqaror oshdi &nbsp;|&nbsp; <strong>크게/급격히 증가했습니다</strong> — keskin o'sdi</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>절반으로 줄었습니다</strong> — yarmiga tushdi &nbsp;|&nbsp; <strong>조금씩 감소했습니다</strong> — asta-sekin kamaydi</p>
  <p style="font-size:1.05em;margin:0;"><strong>두 배가 되었습니다</strong> — ikki baravar bo'ldi &nbsp;|&nbsp; <strong>거의 변화가 없습니다</strong> — deyarli o'zgarmadi</p>
</div>
<h3>② Reyting tili (so'rov natijalari uchun)</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>~이/가 1위를 차지했습니다</strong> — ... 1-o'rinni egalladi</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>그 뒤를 이어 ~이/가 2위였습니다</strong> — undan keyin ... 2-o'rin</p>
  <p style="font-size:1.05em;margin:0;"><strong>~이/가 가장 낮게 나타났습니다</strong> — ... eng past chiqdi</p>
</div>
<h3>③ Taqqoslash</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>A는 B보다 두 배 높았습니다</strong> — A B dan ikki baravar yuqori</p>
  <p style="font-size:1.05em;margin:0;"><strong>반면(에) B는 ~에 그쳤습니다</strong> — aksincha, B ... bilan cheklandi</p>
</div>
<p>Tinglash 그래프 darslaridan tanishmi? Xuddi o'sha til — u yerda quloq bilan tushundingiz,
endi og'iz bilan aytasiz. Bir lug'at — uch ko'nikma!</p>
"""},
            {"rich_text": """
<h3>Reyting namunasi</h3>
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:16px;margin:12px 0;">
  <p style="font-weight:700;text-align:center;margin:0 0 10px;">직장인이 점심시간에 하는 일 (설문 조사)</p>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:110px;font-size:.85em;">동료와 식사</span><div style="height:22px;background:#3b82f6;border-radius:4px;width:45%;"></div><span style="font-size:.85em;">45%</span></div>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:110px;font-size:.85em;">혼자 휴식</span><div style="height:22px;background:#60a5fa;border-radius:4px;width:30%;"></div><span style="font-size:.85em;">30%</span></div>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:110px;font-size:.85em;">운동/산책</span><div style="height:22px;background:#93c5fd;border-radius:4px;width:15%;"></div><span style="font-size:.85em;">15%</span></div>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:110px;font-size:.85em;">자기 계발</span><div style="height:22px;background:#bfdbfe;border-radius:4px;width:10%;"></div><span style="font-size:.85em;">10%</span></div>
</div>
""",
             "audio": "topik_s_051_1.mp3",
             "audio_script": [
                 ("남자", "이 자료는 직장인을 대상으로 점심시간에 하는 일에 대해 조사한 것입니다. 조사 결과, 동료와 식사한다는 응답이 사십오 퍼센트로 1위를 차지했습니다. 그 뒤를 이어 혼자 휴식한다는 응답이 삼십 퍼센트로 2위였습니다. 다음으로 운동이나 산책이 십오 퍼센트였고, 자기 계발은 십 퍼센트로 가장 낮게 나타났습니다. 이 결과를 보면 직장인들은 점심시간을 주로 사람들과의 관계나 휴식에 사용한다는 것을 알 수 있습니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>조사 결과, 동료와 식사한다는 응답이 사십오 퍼센트로 1위를 차지했습니다.</strong><br><em style="color:#475569;">So'rov natijasida "hamkasblar bilan ovqatlanaman" degan javob 45% bilan 1-o'rinni egalladi.</em></p>
    <p><strong>그 뒤를 이어 혼자 휴식한다는 응답이 삼십 퍼센트로 2위였습니다.</strong><br><em style="color:#475569;">Undan keyin "yolg'iz dam olaman" degani 30% bilan 2-o'rin.</em></p>
    <p><strong>자기 계발은 십 퍼센트로 가장 낮게 나타났습니다.</strong><br><em style="color:#475569;">O'z ustida ishlash 10% bilan eng past chiqdi.</em></p>
    <p><strong>이 결과를 보면 ... 알 수 있습니다.</strong><br><em style="color:#475569;">Bu natijaga qarab ... deyish mumkin (umumlashtiruvchi yakun).</em></p>
  </div>
</details>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Yakun jumlasi:</strong> reyting ma'lumotida sabab bo'lmasa, yakunni
  <strong>이 결과를 보면 ~다는 것을 알 수 있습니다</strong> bilan umumlashtiring — tahlil
  tugallangan eshitiladi.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 2-o'rinni aytishning to'g'ri qolipi qaysi?</p>
""",
             "choices": [
                 {"text": "그 뒤를 이어 ~이/가 2위였습니다.", "is_correct": True},
                 {"text": "2등은 이것입니다.", "is_correct": False},
                 {"text": "다음 그림을 보세요.", "is_correct": False},
                 {"text": "두 번째로 좋아합니다.", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: rasmiy tahlil tili. ② juda og'zaki-sodda, ④ shaxsiy did ("yaxshi ko'raman") —
tahlilchi bunday demaydi. Tinglashdagi 이어서/그 뒤를 이어 signali endi sizning og'zingizda.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> "자기 계발은 십 퍼센트에 그쳤습니다"dagi 그치다 nimani bildiradi?</p>
""",
             "choices": [
                 {"text": "Shu (past) darajadan oshmadi, ... bilangina cheklandi", "is_correct": True},
                 {"text": "Keskin o'sdi", "is_correct": False},
                 {"text": "Birinchi o'rinni oldi", "is_correct": False},
                 {"text": "Ikki baravar bo'ldi", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: ~에 그치다 = "...da to'xtab qoldi" — kichik ko'rsatkichni professional aytish yo'li.
Past raqam uchun: ~에 그쳤습니다 / 가장 낮게 나타났습니다. Yuqori raqam uchun: 1위를
차지했습니다. Har raqamga o'z libosi!</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">응답</div><div class="pp-card-back">javob (so'rovda)</div></div>
  <div class="pp-card"><div class="pp-card-front">1위를 차지하다</div><div class="pp-card-back">1-o'rinni egallamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">그 뒤를 이어</div><div class="pp-card-back">undan keyin (2-o'rin)</div></div>
  <div class="pp-card"><div class="pp-card-front">~에 그치다</div><div class="pp-card-back">... bilan cheklanmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">가장 낮게 나타나다</div><div class="pp-card-back">eng past chiqmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">자기 계발</div><div class="pp-card-back">o'z ustida ishlash</div></div>
  <div class="pp-card"><div class="pp-card-front">직장인</div><div class="pp-card-back">ishlaydigan odam, xodim</div></div>
  <div class="pp-card"><div class="pp-card-front">알 수 있습니다</div><div class="pp-card-back">bilish (deyish) mumkin</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Uch ibora guruhi: o'sish-kamayish (darajasi bilan!) · reyting · taqqoslash.</li>
  <li>Past raqam — ~에 그쳤습니다; yuqorisi — 1위를 차지했습니다.</li>
  <li>Sababsiz ma'lumotda yakun: 이 결과를 보면 ~다는 것을 알 수 있습니다.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 52) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q5-3: To'liq amaliyot — ikki grafik gapiradi",
        "summary": "Ikki ma'lumot to'plami: onlayn xarid o'sishi (sabablari bilan) va uyqu vaqti taqqoslash — o'zingiz tahlil qilasiz.",
        "order":   52,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: tahlilchi kursisiga o'tiring</h2>
<p>Tartib: grafikni o'qing → 60–90 soniya reja (uch bosqich katagi) → yozib 1,5 daqiqa
gapiring → namunani eshitib soya qiling. Raqamlarni ovoz chiqarib!</p>
<h3>1-grafik</h3>
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:16px;margin:12px 0;">
  <p style="font-weight:700;text-align:center;margin:0 0 10px;">온라인 쇼핑 이용률의 변화</p>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:70px;font-size:.85em;">2015년</span><div style="height:22px;background:#93c5fd;border-radius:4px;width:25%;"></div><span style="font-size:.85em;">25%</span></div>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:70px;font-size:.85em;">2020년</span><div style="height:22px;background:#60a5fa;border-radius:4px;width:50%;"></div><span style="font-size:.85em;">50%</span></div>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:70px;font-size:.85em;">2025년</span><div style="height:22px;background:#3b82f6;border-radius:4px;width:75%;"></div><span style="font-size:.85em;">75%</span></div>
  <p style="font-size:.8em;color:#64748b;margin:10px 0 0;">원인: ① 스마트폰 사용 증가 ② 배송 속도 향상 &nbsp;·&nbsp; 전망: 계속 증가</p>
</div>
<p>Avval o'zingiz! Keyin namuna:</p>
""",
             "audio": "topik_s_052_1.mp3",
             "audio_script": [
                 ("남자", "이 자료는 온라인 쇼핑 이용률의 변화를 조사한 것입니다. 온라인 쇼핑 이용률은 이천십오 년에 이십오 퍼센트였는데, 이천이십 년에는 오십 퍼센트, 이천이십오 년에는 칠십오 퍼센트로 십 년 동안 세 배나 증가했습니다. 이러한 변화의 원인은 두 가지입니다. 첫째, 스마트폰 사용이 늘었기 때문입니다. 둘째, 배송 속도가 빨라졌기 때문입니다. 앞으로도 온라인 쇼핑 이용률은 계속 증가할 것으로 보입니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>온라인 쇼핑 이용률은 ... 십 년 동안 세 배나 증가했습니다.</strong><br><em style="color:#475569;">Onlayn xarid ulushi o'n yilda naq uch baravar oshdi (25→50→75%).</em></p>
    <p><strong>첫째, 스마트폰 사용이 늘었기 때문입니다. 둘째, 배송 속도가 빨라졌기 때문입니다.</strong><br><em style="color:#475569;">Birinchidan — smartfon ishlatish ko'paygani. Ikkinchidan — yetkazib berish tezlashgani.</em></p>
    <p><strong>앞으로도 계속 증가할 것으로 보입니다.</strong><br><em style="color:#475569;">Kelgusida ham o'sishda davom etishi kutiladi.</em></p>
  </div>
</details>
<h3>2-grafik (taqqoslash turi)</h3>
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:16px;margin:12px 0;">
  <p style="font-weight:700;text-align:center;margin:0 0 10px;">고등학생 평균 수면 시간 비교</p>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:90px;font-size:.85em;">권장 시간</span><div style="height:22px;background:#86efac;border-radius:4px;width:66%;"></div><span style="font-size:.85em;">8시간</span></div>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:90px;font-size:.85em;">실제 시간</span><div style="height:22px;background:#fca5a5;border-radius:4px;width:50%;"></div><span style="font-size:.85em;">6시간</span></div>
  <p style="font-size:.8em;color:#64748b;margin:10px 0 0;">원인: ① 학원과 숙제 ② 밤늦게 스마트폰 사용</p>
</div>
<p>Yana avval o'zingiz! Keyin namuna:</p>
""",
             "audio": "topik_s_052_2.mp3",
             "audio_script": [
                 ("남자", "이 자료는 고등학생의 평균 수면 시간을 조사한 것입니다. 전문가들이 권장하는 수면 시간은 여덟 시간입니다. 그런데 고등학생들의 실제 수면 시간은 여섯 시간으로, 권장 시간보다 두 시간이나 부족했습니다. 그 원인은 두 가지입니다. 첫째, 학원과 숙제 때문에 늦게 자기 때문입니다. 둘째, 밤늦게까지 스마트폰을 사용하기 때문입니다. 수면 부족은 건강과 학습에 나쁜 영향을 주기 때문에, 학생들의 수면 시간에 더 많은 관심이 필요할 것으로 보입니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>실제 수면 시간은 여섯 시간으로, 권장 시간보다 두 시간이나 부족했습니다.</strong><br><em style="color:#475569;">Haqiqiy uyqu vaqti olti soat — tavsiya etilganidan naq ikki soat kam.</em></p>
    <p><strong>수면 부족은 건강과 학습에 나쁜 영향을 주기 때문에...</strong><br><em style="color:#475569;">Uyqu yetishmasligi salomatlik va o'qishga yomon ta'sir qilgani uchun... (istiqbol o'rniga — muammoga e'tibor chaqiruvi).</em></p>
  </div>
</details>
<p><strong>~보다 ~이나 부족했습니다</strong> — taqqoslash grafigining yulduz jumlasi.
이나 qo'shimchasi ("naq!") farqning kattaligini his qildiradi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot.</strong> Q5 da eng ko'p ball yeydigan xato qaysi?</p>
""",
             "choices": [
                 {"text": "Grafikni unutib, o'z hayotini gapirish ('men ham kech uxlayman...')", "is_correct": True},
                 {"text": "Raqamlarni aniq aytish", "is_correct": False},
                 {"text": "첫째/둘째 bilan sabablarni sanash", "is_correct": False},
                 {"text": "Istiqbol jumlasi bilan yakunlash", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: Q5 — tahlil topshirig'i, shaxsiy hikoya emas. Ma'lumotdagi raqamlar, sabablar va
tendensiya — sizning materialingiz; o'z tajribangiz esa Q1 va Q4 ga tegishli. ②③④ —
aksincha, aynan ball keltiradigan harakatlar. Q5 tayyor — endi eng katta cho'qqi: Q6! 🏔️</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">이용률</div><div class="pp-card-back">foydalanish ulushi</div></div>
  <div class="pp-card"><div class="pp-card-front">배송 속도</div><div class="pp-card-back">yetkazib berish tezligi</div></div>
  <div class="pp-card"><div class="pp-card-front">향상</div><div class="pp-card-back">yaxshilanish</div></div>
  <div class="pp-card"><div class="pp-card-front">권장하다</div><div class="pp-card-back">tavsiya etmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">수면 시간</div><div class="pp-card-back">uyqu vaqti</div></div>
  <div class="pp-card"><div class="pp-card-front">~보다 ~이나 부족하다</div><div class="pp-card-back">...dan naq ...ga kam</div></div>
  <div class="pp-card"><div class="pp-card-front">영향을 주다</div><div class="pp-card-back">ta'sir ko'rsatmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">관심이 필요하다</div><div class="pp-card-back">e'tibor kerak</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Uch bosqich har grafikda ishlaydi: kirish → raqamlar → sabab/istiqbol.</li>
  <li>Taqqoslashda: ~보다 ~이나 부족했습니다/높았습니다.</li>
  <li>쓰기 53 shablonlaringiz endi ikki imtihonda xizmat qiladi — bir mehnat, ikki foyda (꿩 먹고 알 먹기!).</li>
</ul>
"""},
        ],
    },
]
