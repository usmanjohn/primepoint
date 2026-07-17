# TOPIK 말하기 (Speaking) — Metod va strategiya, lessons 1–2 (orders 1–2).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_speaking_strategy_1_2.py \
#            --out examprep/management/commands/audio/speaking_strategy
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_speaking_strategy_1_2.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/speaking_strategy

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "Metod va strategiya (말하기 전략)",
    "summary": "Gapirish imtihoni qanday ishlaydi: 6 topshiriq, baholash mezonlari va soya (shadowing) + 3 kunlik jumla metodi.",
    "icon":    "bi-compass",
    "order":   1,
}

LESSONS = [
    # ── Lesson 1 (order 1) ────────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 1: Imtihon qanday ishlaydi — 6 topshiriq",
        "summary": "TOPIK 말하기 평가 bilan tanishuv: kompyuterga gapirasiz, 6 topshiriq osondan qiyinga, uch mezon bo'yicha baholanadi.",
        "order":   1,
        "blocks": [
            {"rich_text": """
<h2>🎤 TOPIK 말하기: kompyuterga gapirish imtihoni</h2>
<p>TOPIK 말하기 평가 — 2022-yildan beri o'tkaziladigan <strong>alohida</strong> imtihon
(o'qish-tinglash-yozishdan mustaqil). Siz xonada <strong>kompyuter va mikrofon</strong>
qarshisida o'tirasiz: savol ekranda ko'rinadi va ovozda eshitiladi, siz belgilangan vaqtda
javobingizni <span style="background:#dbeafe;">mikrofonga gapirasiz</span>. Odam bilan
suhbat YO'Q — bu ham yaxshi (hayajon kamroq!), ham qiyin (kompyuter yordam bermaydi).</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>1.</strong> 질문에 대답하기 — savolga javob (kundalik mavzu) · <span style="background:#dcfce7;padding:1px 8px;border-radius:999px;font-size:.85em;">boshlang'ich</span></p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>2.</strong> 그림 보고 역할 수행하기 — rasmga qarab rol o'ynash · <span style="background:#dcfce7;padding:1px 8px;border-radius:999px;font-size:.85em;">boshlang'ich</span></p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>3.</strong> 그림 보고 이야기하기 — 4 rasmdan hikoya aytish · <span style="background:#fef3c7;padding:1px 8px;border-radius:999px;font-size:.85em;">o'rta</span></p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>4.</strong> 대화 완성하기 — dialogni fikringiz bilan yakunlash · <span style="background:#fef3c7;padding:1px 8px;border-radius:999px;font-size:.85em;">o'rta</span></p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>5.</strong> 자료 해석하기 — grafikni og'zaki tahlil qilish · <span style="background:#fee2e2;padding:1px 8px;border-radius:999px;font-size:.85em;">yuqori</span></p>
  <p style="font-size:1.05em;margin:0;"><strong>6.</strong> 의견 제시하기 — ijtimoiy mavzuda fikr bildirish · <span style="background:#fee2e2;padding:1px 8px;border-radius:999px;font-size:.85em;">yuqori</span></p>
</div>
<p>Jami ~30 daqiqa, ball 0–200, natija 1–6 <strong>daraja</strong> ko'rinishida beriladi.
Har topshiriqda avval <strong>tayyorlanish vaqti</strong> (o'ylash), keyin <strong>javob
vaqti</strong> (gapirish) beriladi — aniq soniyalar topshiriqqa qarab farq qiladi
(oxirgi jadval uchun topik.go.kr ga qarang).</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Sizga tanish ikki do'st:</strong> 5-topshiriq — bu og'zaki <strong>쓰기 53</strong>
  (grafik tili: 늘다, 줄다, 절반...), 6-topshiriq — og'zaki <strong>쓰기 54</strong>
  (shablon + [주제] almashtirish). Yozish bo'limida o'rgangan shablonlaringiz shu yerda
  ikkinchi umrini boshlaydi!
</div>
"""},
            {"rich_text": """
<h3>Uch mezon: sizni nimaga qarab baholashadi?</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi mezon ▸">
  <div class="pp-step"><p><strong>1. Mazmun va topshiriq (내용 및 과제 수행).</strong> Savolga
  AYNAN javob berdingizmi? Rol o'ynashda so'ralgan ishni qildingizmi? Chiroyli, lekin
  mavzudan tashqari gap — ball olmaydi. <em>Davo: javob formulalari (keyingi darslar).</em></p></div>
  <div class="pp-step"><p><strong>2. Til (언어 사용).</strong> Grammatika to'g'riligi va lug'at
  boyligi. Muhim sir: <strong>xatosiz sodda jumla murakkab xatoli jumladan yaxshi</strong>.
  <em>Davo: yodlangan tayyor jumlalar — ularda xato bo'lmaydi.</em></p></div>
  <div class="pp-step"><p><strong>3. Yetkazish (발화 전달력).</strong> Talaffuz, tezlik, ravonlik.
  Uzuq-yuluq "어... 어..." — ballni yeydi. <em>Davo: soya metodi (2-dars) — og'iz
  mashq qilgan jumla o'z-o'zidan ravon chiqadi.</em></p></div>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Jim qolish — eng katta xato. Mukammal gap qidirib sukut
  saqlagandan ko'ra, sodda gap bilan <strong>gapirishda davom etish</strong> har doim
  ko'proq ball beradi. Bilmagan so'z chiqsa — aylanib o'ting: 그 단어... 음... "kutubxona"
  esga kelmasa "책을 읽는 곳" deng!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> Imtihon tuzilishi bo'yicha qaysi gap TO'G'RI?</p>
""",
             "choices": [
                 {"text": "Savollar osondan qiyinga boradi va kompyuterga javob beriladi.", "is_correct": True},
                 {"text": "Imtihonda odam bilan yuzma-yuz suhbatlashiladi.", "is_correct": False},
                 {"text": "Faqat bitta uzun topshiriq bo'ladi.", "is_correct": False},
                 {"text": "Tayyorlanish vaqti berilmaydi.", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: 6 topshiriq boshlang'ichdan yuqori darajagacha zinapoya bo'lib boradi, javob
mikrofon orqali kompyuterga yoziladi. Suhbatdosh odam yo'q (②), topshiriq oltita (③),
va har birida avval o'ylash vaqti beriladi (④).</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> Javob paytida so'z esga kelmay qoldi. Eng to'g'ri harakat qaysi?</p>
""",
             "choices": [
                 {"text": "So'zni tasvirlab, aylanib o'tib gapirishda davom etish", "is_correct": True},
                 {"text": "Javobni to'xtatib, jim qutish", "is_correct": False},
                 {"text": "O'zbekcha aytib qo'yish", "is_correct": False},
                 {"text": "Boshidan qayta boshlash", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: ravonlik mezonida jimlik eng qimmat xato — sodda tasvirlash (책을 읽는 곳)
bilan oqim saqlanadi. ② ball yo'qotadi, ③ baholanmaydi, ④ vaqtni yeydi. Qoida:
<strong>to'xtama, aylanib o't!</strong></p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">말하기 평가</div><div class="pp-card-back">gapirish imtihoni</div></div>
  <div class="pp-card"><div class="pp-card-front">과제</div><div class="pp-card-back">topshiriq</div></div>
  <div class="pp-card"><div class="pp-card-front">준비 시간</div><div class="pp-card-back">tayyorlanish vaqti</div></div>
  <div class="pp-card"><div class="pp-card-front">발음</div><div class="pp-card-back">talaffuz</div></div>
  <div class="pp-card"><div class="pp-card-front">유창성</div><div class="pp-card-back">ravonlik</div></div>
  <div class="pp-card"><div class="pp-card-front">역할 수행</div><div class="pp-card-back">rol bajarish</div></div>
  <div class="pp-card"><div class="pp-card-front">자료 해석</div><div class="pp-card-back">maʼlumot (grafik) tahlili</div></div>
  <div class="pp-card"><div class="pp-card-front">의견 제시</div><div class="pp-card-back">fikr bildirish</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>6 topshiriq, ~30 daqiqa, kompyuterga gapirasiz; 0–200 ball → 1–6 daraja.</li>
  <li>Uch mezon: mazmun · til · yetkazish — uchalasiga ham tayyor jumlalar yordam beradi.</li>
  <li>Oltin qoida: hech qachon jim qolmang — sodda gap bilan aylanib o'ting.</li>
  <li>5–6-topshiriqlar = og'zaki 쓰기 53–54: shablonlaringiz tayyor!</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 2) ────────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 2: Soya metodi — og'zingizni mashq qildiring",
        "summary": "Shadowing (소리 그림자): namunaviy javobni eshitib, soyadek ergashib takrorlash + 3 kunlik jumla metodining og'zaki shakli.",
        "order":   2,
        "blocks": [
            {"rich_text": """
<h2>🗣️ Gapirish — bilim emas, MUSHAK ishi</h2>
<p>Ko'p talaba gapirish imtihonida yiqilishining sababi bilim emas: ular so'zlarni
<strong>ko'z bilan</strong> biladi, lekin <strong>og'iz</strong> ularni hech qachon
aytmagan. Gapirish — sport kabi: qoidani o'qish bilan suzishni o'rganib bo'lmaydi.
Og'iz mushaklari har jumlani <strong>jismonan mashq qilishi</strong> kerak.</p>
<h3>Soya metodi (쉐도잉) — qanday qilinadi</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p><strong>1-qadam. Eshiting.</strong> Namunaviy javob audiosini bir marta
  to'liq eshiting — hech narsa demasdan, faqat ohang va tezlikka quloq soling.</p></div>
  <div class="pp-step"><p><strong>2-qadam. Skript bilan soya qiling.</strong> Audioni qayta qo'yib,
  <strong>0,5–1 soniya orqada</strong> ergashib ayting — xuddi soyadek. Skriptga qarab
  turing. To'xtamang, xato ketsa ham oqim bilan boring.</p></div>
  <div class="pp-step"><p><strong>3-qadam. Skriptsiz soya qiling.</strong> Endi faqat quloq bilan.
  3–4 martadan keyin og'zingiz jumlalarni "o'zi" ayta boshlaydi — bu mushak xotirasi!</p></div>
  <div class="pp-step"><p><strong>4-qadam. Yolg'iz ayting.</strong> Audiosiz, o'zingiz. Telefonga yozib
  oling va namuna bilan solishtiring — talaffuz farqlari darhol eshitiladi.</p></div>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 3 kunlik jumla metodi — endi og'zaki:</strong> yozish bo'limidagi qoidangiz
  shu yerda ham ishlaydi: har namunaviy javobdan <strong>kuniga 3 jumlani, 3 kun davomida,
  har kuni 3 marta ovoz chiqarib</strong> ayting. Yodlangan jumla imtihonda o'ylamasdan,
  xatosiz va ravon chiqadi — uch mezonning uchchalasiga ball!
</div>
"""},
            {"rich_text": """
<h3>🎧 Birinchi soya mashqingiz</h3>
<p>Quyida qisqa namunaviy javob (o'zini tanishtirish — har imtihonning "isinish" mavzusi).
Yuqoridagi 4 qadamni aynan shu audio bilan bajarib ko'ring:</p>
""",
             "audio": "topik_s_002_1.mp3",
             "audio_script": [
                 ("남자", "안녕하세요. 저는 아지즈라고 합니다. 우즈베키스탄에서 왔습니다. 지금은 대학교에서 한국어를 공부하고 있습니다. 한국 문화에 관심이 많아서 한국어를 배우기 시작했습니다. 앞으로 한국 회사에서 일하고 싶습니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — avval o'zingiz aytib ko'ring, keyin oching!</summary>
  <div style="margin-top:10px;">
    <p><strong>안녕하세요. 저는 아지즈라고 합니다.</strong><br>
    <em style="color:#475569;">Assalomu alaykum. Men Aziz deb atalaman.</em></p>
    <p><strong>우즈베키스탄에서 왔습니다. 지금은 대학교에서 한국어를 공부하고 있습니다.</strong><br>
    <em style="color:#475569;">O'zbekistondan kelganman. Hozir universitetda koreys tilini o'rganyapman.</em></p>
    <p><strong>한국 문화에 관심이 많아서 한국어를 배우기 시작했습니다.</strong><br>
    <em style="color:#475569;">Koreys madaniyatiga qiziqishim katta bo'lgani uchun koreys tilini o'rganishni boshladim.</em></p>
    <p><strong>앞으로 한국 회사에서 일하고 싶습니다.</strong><br>
    <em style="color:#475569;">Kelajakda koreys kompaniyasida ishlamoqchiman.</em></p>
  </div>
</details>
<p>E'tibor bering: beshta jumla, hammasi sodda, hammasi <strong>-ㅂ니다</strong> uslubida
(imtihonda hurmat uslubi xavfsiz tanlov). Shu beshtasini 3 kun soya qilsangiz — o'zingizni
tanishtirish savoli endi sizniki.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> Soya metodining to'g'ri tartibi qaysi?</p>
""",
             "choices": [
                 {"text": "Eshitish → skript bilan soya → skriptsiz soya → yolg'iz aytish", "is_correct": True},
                 {"text": "Yodlash → yozish → o'qish → eshitish", "is_correct": False},
                 {"text": "Skriptni tarjima qilish → lug'at yozish → test yechish", "is_correct": False},
                 {"text": "Faqat eshitish, aytish shart emas", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: avval quloq (ohang), keyin ko'z+og'iz (skript bilan), keyin faqat og'iz
(skriptsiz), oxirida mustaqil + yozib solishtirish. ③ — o'qish bo'limining usullari,
gapirishda og'iz ishlashi shart; ④ — eshitish yolg'iz mushak xotirasi bermaydi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> Nega yodlangan tayyor jumla imtihonda kuchli qurol?</p>
""",
             "choices": [
                 {"text": "Xatosiz, o'ylamasdan va ravon chiqadi — uch mezonga ham foyda", "is_correct": True},
                 {"text": "Baholovchi yodlanganini sezsa qo'shimcha ball beradi", "is_correct": False},
                 {"text": "Uzun bo'lgani uchun vaqtni to'ldiradi", "is_correct": False},
                 {"text": "Yodlangan jumla bilan hamma savolga javob berish mumkin", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: tayyor jumlada grammatik xato yo'q (til mezoni), o'ylash vaqti ketmaydi (mazmunga
vaqt qoladi) va og'iz uni mashq qilgan (ravonlik). ④ — yo'q: jumla savolga MOS bo'lishi
kerak, shuning uchun mavzular bo'yicha jumla banki yig'amiz (keyingi darslar).</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">-(이)라고 합니다</div><div class="pp-card-back">... deb atalaman</div></div>
  <div class="pp-card"><div class="pp-card-front">-에서 왔습니다</div><div class="pp-card-back">...dan kelganman</div></div>
  <div class="pp-card"><div class="pp-card-front">-에 관심이 많다</div><div class="pp-card-back">...ga qiziqishi katta</div></div>
  <div class="pp-card"><div class="pp-card-front">-기 시작했습니다</div><div class="pp-card-back">...ishni boshladim</div></div>
  <div class="pp-card"><div class="pp-card-front">앞으로</div><div class="pp-card-back">kelajakda, bundan buyon</div></div>
  <div class="pp-card"><div class="pp-card-front">-고 싶습니다</div><div class="pp-card-back">...moqchiman (hurmat uslubi)</div></div>
  <div class="pp-card"><div class="pp-card-front">쉐도잉</div><div class="pp-card-back">soya metodi (shadowing)</div></div>
  <div class="pp-card"><div class="pp-card-front">근육 기억</div><div class="pp-card-back">mushak xotirasi</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Gapirish — mushak ishi: og'iz aytmagan jumla imtihonda chiqmaydi.</li>
  <li>Soya: eshit → skript bilan ayt → skriptsiz ayt → yolg'iz ayt (yozib solishtir).</li>
  <li>Kuniga 3 jumla × 3 kun × 3 marta ovoz chiqarib — yozishdagi metodingizning og'zaki shakli.</li>
  <li>Imtihonda -ㅂ니다 uslubi — xavfsiz tanlov.</li>
</ul>
"""},
        ],
    },
]
