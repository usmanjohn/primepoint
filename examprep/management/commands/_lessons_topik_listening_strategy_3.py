# TOPIK II Listening — Metod va strategiya, lesson 3 (order 3): imtihon tuzilishi va taktika.
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_strategy_3.py \
#            --out examprep/management/commands/audio/strategy
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_strategy_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/strategy

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "Metod va strategiya (듣기 전략)",
    "summary": "Tinglashni qanday rivojlantirish: podkast metodi, imtihon tuzilishi va umumiy taktika.",
    "icon":    "bi-compass",
    "order":   1,
}

LESSONS = [
    # ── Lesson 3 (order 3) ────────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK Listening 3: Imtihon qanday ishlaydi — tuzilish va taktika",
        "summary": "듣기 bo'limining tuzilishi: 50 savol, qaysilari bir marta eshitiladi, va eng muhim taktika — variantlarni oldindan o'qish.",
        "order":   3,
        "blocks": [
            {"rich_text": """
<h2>🗺️ 듣기 bo'limi xaritasi: 50 savol, 60 daqiqa</h2>
<p>Tinglash bo'limida <strong>50 savol</strong> bor va hammasi bitta uzluksiz audio oqimida
keladi — <strong>pauza tugmasi yo'q, orqaga qaytib bo'lmaydi</strong>. Shuning uchun bu
bo'limda vaqtni siz emas, audio boshqaradi. Sizning quroling — <strong>tayyorgarlik</strong>.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>1–20-savollar</strong> — audio <mark style="background:#fee2e2;">faqat BIR marta</mark> eshittiriladi. Qisqa dialoglar, tez sur'at.</p>
  <p style="font-size:1.05em;margin:0;"><strong>21–50-savollar</strong> — audio <mark style="background:#dcfce7;">IKKI marta</mark> eshittiriladi va har matnga <strong>ikkitadan savol</strong> beriladi (juft savollar).</p>
</div>
<h3>Savol guruhlari (bizning darslar xaritasi ham shu)</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.02em;margin:0 0 5px;"><strong>1–3</strong> mos rasm/grafik · <strong>4–8</strong> keyingi replika · <strong>9–12</strong> keyingi harakat</p>
  <p style="font-size:1.02em;margin:0 0 5px;"><strong>13–16</strong> mazmun mosligi · <strong>17–20</strong> asosiy fikr</p>
  <p style="font-size:1.02em;margin:0;"><strong>21–50</strong> juft savollar: suhbat, intervyu, munozara, ma'ruza, hujjatli matn — tobora uzunroq va qiyinroq.</p>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Qiyinlik zinapoya kabi o'sadi: 1-savol eng oson, 50-savol eng
  qiyin. Maqsadingiz TOPIK II 3–4-daraja bo'lsa, kuchingizni 1–30 ga qarating; 5–6-daraja
  uchun 31–50 hal qiluvchi.
</div>
"""},
            {"rich_text": """
<h3>⭐ Eng muhim taktika: variantlarni OLDINDAN o'qing</h3>
<p>Audio siz uchun kutmaydi — lekin sizga ishlaydigan bitta narsa bor: <strong>savollar
orasidagi pauzalar</strong> va boshidagi ko'rsatma o'qilayotgan vaqt. Shu sekundlarda
<strong>keyingi savolning variantlarini</strong> o'qib chiqing:</p>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p><strong>1-qadam.</strong> Variantlarni ko'z yugurtirib, <strong>takrorlanayotgan
  so'zlarni</strong> toping — ular mavzuni oldindan aytadi (hamma variantda 회의 bo'lsa —
  majlis haqida eshitasiz).</p></div>
  <div class="pp-step"><p><strong>2-qadam.</strong> Variantlar orasidagi <strong>farqni</strong> belgilang:
  raqamlar farq qiladimi? Kim bajarayotgani farq qiladimi? Endi nimani eshitish kerakligini
  aniq bilasiz.</p></div>
  <div class="pp-step"><p><strong>3-qadam.</strong> Eshitayotganda javobni <strong>darhol</strong> belgilang
  va keyingi savolning variantlariga o'ting. Ikkilangan bo'lsangiz ham to'xtamang —
  belgilab qo'ying va oldinga! Bitta savolga qadalib qolish = keyingi ikki savolni ham yo'qotish.</p></div>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Audio tugagandan keyin "o'ylab ko'raman" degan vaqt YO'Q —
  keyingi savol darhol boshlanadi. Javobni eshitayotib belgilash odatini hozirdan,
  shu darslardayoq shakllantiring.
</div>
"""},
            {"rich_text": """
<h3>🎧 Sinab ko'ramiz: oldin variantlar, keyin audio</h3>
<p>Quyida savol va variantlar bor. Avval ularni o'qing: hamma variant — <strong>soat</strong>.
Demak vazifangiz bitta: <strong>vaqtni</strong> ushlash (va tuzoqqa tushmaslik!). Endi audioni
bir marta eshiting.</p>
<p><strong>Amaliyot 1.</strong> 회의는 몇 시부터 시작합니까? <em>(Majlis soat nechada boshlanadi?)</em></p>
""",
             "audio": "topik_l_003_1.mp3",
             "audio_script": [
                 ("여자", "내일 회의가 몇 시부터예요?"),
                 ("남자", "오후 두 시부터인데, 삼십 분 일찍 와서 자료를 준비해 주세요."),
                 ("여자", "네, 그럼 한 시 반까지 갈게요."),
             ],
             "choices": [
                 {"text": "오후 2시 (tushdan keyin soat 2 da)", "is_correct": True},
                 {"text": "오후 1시 30분 (tushdan keyin 1:30 da)", "is_correct": False},
                 {"text": "오후 2시 30분 (tushdan keyin 2:30 da)", "is_correct": False},
                 {"text": "오전 10시 (ertalab soat 10 da)", "is_correct": False},
             ],
             "explanation": """
<p>Savol <strong>majlis</strong> haqida: 회의는 <strong>두 시부터</strong> (soat 2 dan) ✅.
② klassik tuzoq: 한 시 반 (1:30) ham eshitildi — lekin bu ayolning <strong>kelish</strong>
vaqti (삼십 분 일찍 — yarim soat erta), majlis vaqti emas! Variantlarni oldindan o'qigan
odam "ikki soat ham aytiladi, savol qaysi biri haqida?" deb tayyor turadi. Raqamli savollarda
doim <strong>ikkita raqam</strong> aytiladi — savolga mosini oling.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 내일 회의가 몇 시부터예요?<br>
    <em style="color:#475569;">Ertaga majlis soat nechadan boshlanadi?</em></p>
    <p><strong>남자:</strong> 오후 두 시부터인데, 삼십 분 일찍 와서 자료를 준비해 주세요.<br>
    <em style="color:#475569;">Tushdan keyin ikkidan, lekin yarim soat erta kelib, materiallarni tayyorlab qo'ying.</em></p>
    <p><strong>여자:</strong> 네, 그럼 한 시 반까지 갈게요.<br>
    <em style="color:#475569;">Xo'p, unda bir yarimgacha boraman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> Imtihon tuzilishi bo'yicha qaysi gap to'g'ri?</p>
""",
             "choices": [
                 {"text": "1–20-savollarning audiosi bir marta, 21–50-savollarniki ikki marta eshittiriladi.", "is_correct": True},
                 {"text": "Hamma savolning audiosi ikki marta eshittiriladi.", "is_correct": False},
                 {"text": "Audioni xohlagan payt to'xtatib, qayta eshitish mumkin.", "is_correct": False},
                 {"text": "Qiyin savollar bo'limning boshida keladi.", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: 1–20 — bir marta (shuning uchun bu guruhga alohida tayyorlanamiz!), 21–50 — ikki
marta va juft savollar bilan. ③ imtihonda audio uzluksiz oqim — to'xtatib bo'lmaydi
(bizning darslarda esa xohlagancha qayta eshitishingiz mumkin — bundan foydalaning!).
④ teskari: qiyinlik oxirga qarab o'sadi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">회의</div><div class="pp-card-back">majlis, yig'ilish</div></div>
  <div class="pp-card"><div class="pp-card-front">자료</div><div class="pp-card-back">material, hujjat</div></div>
  <div class="pp-card"><div class="pp-card-front">일찍</div><div class="pp-card-back">erta, oldinroq</div></div>
  <div class="pp-card"><div class="pp-card-front">준비하다</div><div class="pp-card-back">tayyorlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">시작하다</div><div class="pp-card-back">boshlanmoq, boshlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">오전 / 오후</div><div class="pp-card-back">tushgacha / tushdan keyin</div></div>
  <div class="pp-card"><div class="pp-card-front">한 시 반</div><div class="pp-card-back">bir yarim (1:30)</div></div>
  <div class="pp-card"><div class="pp-card-front">문제</div><div class="pp-card-back">savol, masala</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>50 savol / 60 daqiqa, uzluksiz oqim: 1–20 bir marta, 21–50 ikki marta (juft savollar).</li>
  <li>Oltin taktika: pauzalarda <strong>keyingi savolning variantlarini</strong> o'qing — farqni belgilang.</li>
  <li>Javobni eshitayotib belgilang va oldinga o'ting — bitta savolga qadalmang.</li>
  <li>Raqamli savollarda doim ikkita raqam aytiladi — savolga mosini tanlang.</li>
</ul>
"""},
        ],
    },
]
